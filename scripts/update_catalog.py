#!/usr/bin/env python3
"""Update repo.json from approved assets of one published GitHub release."""
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import re
import tarfile
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'repo.json'
APPS = {
    'g5-tv-launcher': 'org.schrotty74.g5launcher',
    'g5-system-monitor': 'org.schrotty74.g5systemmonitor',
}
PATTERN = re.compile(r'^(g5-tv-launcher|g5-system-monitor)_(\d+\.\d+\.\d+)_all\.ipk$')

def package_info(raw):
    if raw[:8] != b'!<arch>\n': raise ValueError('Invalid IPK archive')
    pos, members = 8, {}
    while pos < len(raw):
        header = raw[pos:pos+60]
        if len(header) != 60 or header[58:60] != b'`\n': raise ValueError('Invalid ar header')
        name = header[:16].decode('ascii').strip().rstrip('/')
        size = int(header[48:58].decode('ascii').strip())
        pos += 60
        if pos + size > len(raw): raise ValueError('Truncated archive')
        if name in members: raise ValueError('Duplicate ar entry')
        members[name] = raw[pos:pos+size]
        pos += size + size % 2
    if pos != len(raw) or 'data.tar.gz' not in members: raise ValueError('Missing data archive')
    with tarfile.open(fileobj=io.BytesIO(members['data.tar.gz']), mode='r:gz') as tar:
        matches = [m for m in tar.getmembers() if m.isfile() and re.fullmatch(r'(?:\./)?usr/palm/applications/org\.schrotty74\.g5(?:launcher|systemmonitor)/appinfo\.json', m.name)]
        if len(matches) != 1 or matches[0].size > 65536: raise ValueError('Invalid app metadata')
        return json.load(tar.extractfile(matches[0]))

def update(catalog, release, download):
    if release.get('draft') or release.get('prerelease'): return False
    packages = {p.get('id'): p for p in catalog['packages']}
    assets = {}
    for asset in release.get('assets', []):
        match = PATTERN.fullmatch(asset.get('name', ''))
        if not match: continue
        app, version = match.groups()
        if app in assets: raise ValueError('Multiple published packages for '+app)
        assets[app] = (version, asset)
    if not assets: return False
    updates = []
    for app, (version, asset) in assets.items():
        if APPS[app] not in packages: raise ValueError('App missing from catalog')
        current = packages[APPS[app]]['manifest']['version']
        if not re.fullmatch(r'\d+\.\d+\.\d+',current): raise ValueError('Invalid catalog version')
        if tuple(map(int, version.split('.'))) < tuple(map(int, current.split('.'))): continue
        url = asset.get('browser_download_url','')
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme != 'https' or parsed.netloc != 'github.com' or not parsed.path.startswith('/Schrotty74/LG-G5-Apps/releases/download/') or parsed.path.split('/')[-1] != asset['name']:
            raise ValueError('Unexpected asset URL')
        raw = download(url)
        if len(raw) != asset.get('size'): raise ValueError('Asset size mismatch')
        meta = package_info(raw)
        if meta.get('id') != APPS[app] or meta.get('version') != version: raise ValueError('IPK identity or version mismatch')
        digest = hashlib.sha256(raw).hexdigest()
        if asset.get('digest') and asset['digest'] != 'sha256:'+digest: raise ValueError('GitHub digest mismatch')
        updates.append((packages[APPS[app]]['manifest'],version,url,digest,len(raw)))
    changed = False
    for m,version,url,digest,size in updates:
        new = {'version':version,'ipkUrl':url,'ipkHash':{'sha256':digest},'ipkSize':size}
        for key,value in new.items():
            if m.get(key) != value: m[key]=value;changed=True
    return changed

def main():
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    release = event['release']
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    def download(url):
        req=urllib.request.Request(url,headers={'User-Agent':'g5-app-catalog'})
        with urllib.request.urlopen(req,timeout=90) as response:
            data=response.read(50_000_001)
            if len(data)>50_000_000: raise ValueError('Package exceeds size limit')
            return data
    if update(catalog, release, download):
        CATALOG.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print('Catalog updated')
    else: print('No catalog changes')
if __name__ == '__main__': main()
