#!/usr/bin/env python3
"""Read only small, regular JSON theme files directly inside /tmp."""
import json
import os
import re
import stat
import sys

ROOT = '/tmp'
MAX_BYTES = 80000
NAME = re.compile(r'^[A-Za-z0-9_][A-Za-z0-9_.-]{0,114}\.json$')


def list_themes():
    entries = []
    with os.scandir(ROOT) as items:
        for item in items:
            if not NAME.fullmatch(item.name):
                continue
            try:
                if item.is_file(follow_symlinks=False) and valid_theme(read_theme(item.name)):
                    entries.append(item.name)
            except (OSError, ValueError, UnicodeError, TypeError):
                continue
    return sorted(entries)[:100]


def valid_theme(t):
    if not isinstance(t, dict) or t.get('format') != 'g5-theme' or type(t.get('version')) is not int or t['version'] != 1:
        return False
    if not isinstance(t.get('id'), str) or not re.fullmatch(r'[-a-z0-9]{1,32}', t['id']):
        return False
    if not isinstance(t.get('name'), str) or not t['name'].strip() or len(t['name']) > 60:
        return False
    if any(not isinstance(t.get(k), str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', t[k]) for k in ('background', 'accent', 'glow')):
        return False
    image = t.get('image', '')
    return isinstance(image, str) and (not image or (len(image) <= 70000 and bool(re.fullmatch(r'data:image/(?:png|jpeg|webp);base64,[A-Za-z0-9+/]+={0,2}', image))))


def read_theme(name):
    if not isinstance(name, str) or not NAME.fullmatch(name):
        raise ValueError('Invalid theme file name')
    if not hasattr(os, 'O_NOFOLLOW'):
        raise RuntimeError('Safe file access unavailable')
    fd = os.open(os.path.join(ROOT, name), os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as f:
        if not stat.S_ISREG(os.fstat(f.fileno()).st_mode):
            raise ValueError('Not a regular file')
        raw = f.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError('Theme file too large')
    return json.loads(raw.decode('utf-8'))


def main(args):
    if args == ['list']:
        return {'ok': True, 'files': list_themes()}
    if len(args) == 2 and args[0] == 'read':
        return {'ok': True, 'theme': read_theme(args[1])}
    raise ValueError('Invalid request')


if __name__ == '__main__':
    try:
        result = main(sys.argv[1:])
    except (OSError, ValueError, UnicodeError) as error:
        result = {'ok': False, 'message': str(error)}
    print(json.dumps(result, ensure_ascii=False))
    sys.exit(0 if result['ok'] else 1)
