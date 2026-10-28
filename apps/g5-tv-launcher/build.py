#!/usr/bin/env python3
"""Build a webOS IPK using only Python 3, on macOS or Linux."""
from __future__ import annotations
import argparse
import gzip
import io
from pathlib import Path
import tarfile

ROOT = Path(__file__).resolve().parent
APP = ROOT / 'app'
VERSION = '0.2.44'
APP_ID = 'org.schrotty74.g5launcher'

def tar_bytes(entries):
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode='w', format=tarfile.USTAR_FORMAT) as archive:
        for name, data in entries:
            info = tarfile.TarInfo(name)
            info.uid = info.gid = info.mtime = 0
            info.uname = info.gname = ''
            if data is None:
                info.type = tarfile.DIRTYPE
                info.mode = 0o755
                archive.addfile(info)
            else:
                info.mode = 0o644
                info.size = len(data)
                archive.addfile(info, io.BytesIO(data))
    raw = output.getvalue()
    offset = 0
    while raw[offset:offset + 512] != bytes(512):
        header = raw[offset:offset + 512]
        size = int(header[124:136].strip(b'\0 ') or b'0', 8)
        offset += 512 + ((size + 511) // 512) * 512
    return gzip.compress(raw[:offset + 1024], mtime=0)

def write_ar_entry(stream, name, data):
    header = (f'{name + "/":<16}{0:<12}{0:<6}{0:<6}{"100644":<8}{len(data):<10}`\n').encode('ascii')
    if len(header) != 60:
        raise ValueError('Invalid ar header')
    stream.write(header)
    stream.write(data)
    if len(data) % 2:
        stream.write(b'\n')

def main():
    parser = argparse.ArgumentParser(description='Build the G5 TV Launcher IPK')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist', help='output directory (default: dist/)')
    args = parser.parse_args()
    if not (APP / 'appinfo.json').is_file():
        parser.error('app/appinfo.json is missing')
    import json
    metadata = json.loads((APP / 'appinfo.json').read_text(encoding='utf-8'))
    if metadata.get('version') != VERSION or metadata.get('id') != APP_ID:
        parser.error('build version or app ID does not match app/appinfo.json')
    base = './usr/palm/applications/' + APP_ID
    dirs = ['.', './usr', './usr/palm', './usr/palm/applications', base]
    dirs.extend(base + '/' + d.relative_to(APP).as_posix() for d in sorted(APP.rglob('*')) if d.is_dir())
    entries = [(d, None) for d in dirs]
    entries += [(base + '/' + f.relative_to(APP).as_posix(), f.read_bytes()) for f in sorted(APP.rglob('*')) if f.is_file()]
    control = (f'Package: {APP_ID}\nVersion: {VERSION}\nSection: utils\nArchitecture: all\nMaintainer: Schrotty74\nDescription: G5 Home launcher for LG webOS TV\n').encode()
    args.output.mkdir(parents=True, exist_ok=True)
    target = args.output / f'g5-tv-launcher_{VERSION}_all.ipk'
    with target.open('wb') as stream:
        stream.write(b'!<arch>\n')
        write_ar_entry(stream, 'debian-binary', b'2.0\n')
        write_ar_entry(stream, 'control.tar.gz', tar_bytes([('./control', control)]))
        write_ar_entry(stream, 'data.tar.gz', tar_bytes(entries))
    print(target)

if __name__ == '__main__':
    main()
