#!/usr/bin/env python3
"""Optional integration with the existing Magic Mapper 1.1.2 installation."""
import base64
import json
import os
import subprocess
import sys

MAPPER = '/media/developer/apps/usr/palm/applications/com.github.afonsojramos.magicmapper'
CTL = os.path.join(MAPPER, 'runtime', 'mapperctl.py')
BACKUP_DIR = '/media/developer/g5-tv-launcher'
BACKUP = os.path.join(BACKUP_DIR, 'home-key-previous.json')
TARGET = {'function': 'launch_app', 'inputs': {'app_id': 'org.schrotty74.g5launcher'}}


def invoke(*args):
    proc = subprocess.run([sys.executable, CTL] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
    try:
        data = json.loads(proc.stdout.decode('utf-8'))
    except (ValueError, UnicodeError):
        raise RuntimeError('Magic Mapper antwortet nicht wie erwartet.')
    if proc.returncode != 0 or data.get('ok') is not True:
        raise RuntimeError('Magic Mapper konnte die Änderung nicht anwenden.')
    return data


def read_status():
    try:
        with open(os.path.join(MAPPER, 'appinfo.json'), encoding='utf-8') as f:
            app = json.load(f)
    except (OSError, ValueError):
        raise RuntimeError('Magic Mapper 1.1.2 wurde nicht gefunden.')
    if app.get('id') != 'com.github.afonsojramos.magicmapper' or app.get('version') != '1.1.2' or not os.path.isfile(CTL):
        raise RuntimeError('Diese Magic-Mapper-Version wird noch nicht unterstützt.')
    state = invoke('status').get('status')
    if not isinstance(state, dict) or not isinstance(state.get('config'), dict):
        raise RuntimeError('Magic Mapper meldet keine gültige Konfiguration.')
    return state


def is_target(value):
    return value == TARGET


def save_backup(config):
    os.makedirs(BACKUP_DIR, mode=0o700, exist_ok=True)
    payload = {'format': 'g5-home-key', 'version': 1, 'existed': 'home' in config, 'home': config.get('home')}
    fd = os.open(BACKUP, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())


def read_backup():
    try:
        with open(BACKUP, encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, ValueError):
        raise RuntimeError('Keine lesbare Sicherung der vorherigen Home-Belegung gefunden.')
    if not isinstance(data, dict) or data.get('format') != 'g5-home-key' or data.get('version') != 1 or not isinstance(data.get('existed'), bool):
        raise RuntimeError('Sicherung der Home-Belegung ist ungültig.')
    return data


def encoded_config(config):
    return base64.b64encode(json.dumps(config, ensure_ascii=False).encode('utf-8')).decode('ascii')


def apply_config(before, desired):
    # Refuse to overwrite a change made since the status was read.
    fresh = read_status()
    if fresh.get('config') != before or not fresh.get('active'):
        raise RuntimeError('Magic Mapper wurde zwischenzeitlich geändert oder beendet. Bitte erneut versuchen.')
    try:
        invoke('configure', encoded_config(desired))
        confirmed = read_status()
        if not confirmed.get('active') or confirmed.get('config') != desired:
            raise RuntimeError('Magic Mapper meldet die neue Belegung nicht als aktiv.')
    except Exception:
        # Restore the prior config only while the current file is still ours.
        try:
            current = read_status().get('config')
            if current == desired:
                invoke('configure', encoded_config(before))
        except Exception:
            raise RuntimeError('Änderung fehlgeschlagen; Wiederherstellung in Magic Mapper prüfen. Die Sicherung bleibt erhalten.')
        raise RuntimeError('Änderung fehlgeschlagen. Status und Belegung in Magic Mapper prüfen.')


def main(action):
    state = read_status()
    config = state['config']
    active = bool(state.get('active'))
    installed = bool(state.get('installed'))
    if action == 'status':
        return {'ok': True, 'active': active, 'installed': installed, 'mapped': is_target(config.get('home')), 'canRestore': os.path.isfile(BACKUP)}
    if not active or not installed:
        raise RuntimeError('Magic Mapper muss aktiv sein und bereits beim Start laufen. Es wurden keine Autostart-Einstellungen geändert.')
    if action == 'enable':
        if is_target(config.get('home')):
            if not os.path.isfile(BACKUP):
                raise RuntimeError('Home ist bereits zugeordnet, aber eine Sicherung der vorherigen Belegung fehlt.')
            return {'ok': True, 'message': 'Home ist bereits für diesen Launcher eingerichtet.'}
        if os.path.exists(BACKUP):
            raise RuntimeError('Eine frühere Home-Sicherung ist vorhanden. Bitte die Belegung zuerst in Magic Mapper prüfen.')
        save_backup(config)
        desired = dict(config)
        desired['home'] = TARGET
        try:
            apply_config(config, desired)
        except Exception:
            # Remove the snapshot only if the original configuration is active again.
            try:
                after = read_status()
                if after.get('active') and after.get('config') == config:
                    os.unlink(BACKUP)
            except Exception:
                pass
            raise
        return {'ok': True, 'message': 'Home-Taste für diesen Launcher eingerichtet.'}
    if action == 'restore':
        backup = read_backup()
        if not is_target(config.get('home')):
            raise RuntimeError('Home wurde zwischenzeitlich anders belegt. Die aktuelle Belegung bleibt erhalten.')
        desired = dict(config)
        if backup['existed']:
            desired['home'] = backup.get('home')
        else:
            desired.pop('home', None)
        apply_config(config, desired)
        os.unlink(BACKUP)
        return {'ok': True, 'message': 'Vorherige Home-Belegung wiederhergestellt.'}
    raise RuntimeError('Unbekannte Aktion.')


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2 or sys.argv[1] not in ('status', 'enable', 'restore'):
            raise RuntimeError('Ungültige Aktion.')
        result = main(sys.argv[1])
    except Exception as error:
        result = {'ok': False, 'message': str(error)}
    print(json.dumps(result, ensure_ascii=False))
