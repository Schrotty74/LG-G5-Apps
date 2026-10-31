#!/usr/bin/env python3
"""Read only small, regular JSON theme files directly inside /tmp."""
import json
import math
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


def valid_scene(scene):
    if not isinstance(scene, list) or len(scene) > 100:
        return False
    def number(value, low, high):
        return not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value) and low <= value <= high
    for item in scene:
        if not isinstance(item, dict) or item.get('type') not in ('rect', 'ellipse', 'polygon'):
            return False
        if any(k not in ('type', 'color', 'x', 'y', 'width', 'height', 'points', 'opacity', 'animation') for k in item):
            return False
        if not isinstance(item.get('color'), str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', item['color']):
            return False
        if item['type'] == 'polygon':
            points = item.get('points')
            if not isinstance(points, list) or not 3 <= len(points) <= 40 or any(not isinstance(p, list) or len(p) != 2 or not number(p[0], 0, 1000) or not number(p[1], 0, 500) for p in points):
                return False
        elif not all(number(item.get(k), low, high) for k, low, high in (('x',0,1000), ('y',0,500), ('width',1,1000), ('height',1,500))):
            return False
        if 'opacity' in item and not number(item['opacity'], 0, 1):
            return False
        if 'animation' in item:
            a = item['animation']
            if not isinstance(a, dict) or any(k not in ('type','duration','dx','dy') for k in a) or a.get('type') not in ('move','blink','sway') or not number(a.get('duration'), .5, 60):
                return False
            if any(k in a and not number(a[k], -300, 300) for k in ('dx','dy')):
                return False
    return True


def valid_theme(t):
    if not isinstance(t, dict) or t.get('format') != 'g5-theme' or type(t.get('version')) is not int or t['version'] != 1:
        return False
    if not isinstance(t.get('id'), str) or not re.fullmatch(r'[-a-z0-9]{1,32}', t['id']):
        return False
    if not isinstance(t.get('name'), str) or not t['name'].strip() or len(t['name']) > 60:
        return False
    if any(not isinstance(t.get(k), str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', t[k]) for k in ('background', 'accent', 'glow')):
        return False
    if t.get('animation', 'none') not in ('none', 'neon', 'rain', 'snow', 'particles'):
        return False
    options = t.get('animationOptions', {})
    if not isinstance(options, dict) or any(k not in ('color', 'duration', 'opacity', 'direction') for k in options):
        return False
    if 'color' in options and (not isinstance(options['color'], str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', options['color'])):
        return False
    for key, low, high in (('duration', 0.5, 30), ('opacity', 0, 1)):
        if key in options and (isinstance(options[key], bool) or not isinstance(options[key], (int, float)) or not low <= options[key] <= high):
            return False
    if 'direction' in options and options['direction'] not in ('normal', 'reverse', 'alternate'):
        return False
    if not valid_scene(t.get('scene', [])):
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
