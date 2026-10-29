#!/usr/bin/env python3
"""Restricted local bridge for direct Home. No shell execution endpoint."""
import base64
import hmac
import json
import os
import re
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

MAX_BODY = 350000
ICON_ROOTS = ('/usr/palm/applications/', '/usr/palm/plugins/inputapps/',
              '/media/developer/apps/usr/palm/applications/',
              '/media/system/apps/usr/palm/applications/',
              '/media/cryptofs/apps/usr/palm/applications/',
              '/mnt/otncabi/usr/palm/applications/')
ALLOWED_HOME = frozenset(('heartbeat', 'prefs-load', 'prefs-save', 'status', 'lg', 'legacy', 'recover'))


def execute(action, data, helper, backup):
    if action == 'apps':
        out = subprocess.run(['luna-send', '-n', '1', '-f',
                              'luna://com.webos.applicationManager/listLaunchPoints',
                              '{"subscribe":false}'], capture_output=True, timeout=10, check=True)
        return out.stdout.decode('utf-8')
    if action == 'icon':
        path = data.get('path')
        if not isinstance(path, str) or not re.fullmatch(r'/[A-Za-z0-9._/-]+\.(?:png|jpe?g|gif|webp|svg)', path, re.I):
            raise ValueError('Invalid icon path')
        actual = os.path.realpath(path)
        if not any(actual.startswith(prefix) for prefix in ICON_ROOTS):
            raise ValueError('Icon is outside application directories')
        fd = os.open(actual, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
        with os.fdopen(fd, 'rb') as f:
            content = f.read(524289)
        if len(content) > 524288:
            raise ValueError('Icon is too large')
        return base64.b64encode(content).decode('ascii')
    if action == 'home':
        operation = data.get('operation')
        if operation not in ALLOWED_HOME:
            raise ValueError('Invalid Home operation')
        # A switch may close the Home page before its debounced save fires.
        if operation in ('lg', 'legacy') and isinstance(data.get('settings'), dict):
            encoded = base64.b64encode(json.dumps(data['settings'], ensure_ascii=False).encode()).decode()
            saved = subprocess.run(['python3', helper, 'prefs-save', encoded], capture_output=True, text=True, timeout=25)
            if not json.loads(saved.stdout).get('ok'):
                raise ValueError('Could not save settings before switching Home')
        args = ['python3', helper, operation]
        if operation == 'prefs-save':
            settings = data.get('settings')
            if not isinstance(settings, dict):
                raise ValueError('Invalid settings')
            args.append(base64.b64encode(json.dumps(settings, ensure_ascii=False).encode()).decode())
        p = subprocess.run(args, capture_output=True, text=True, timeout=90)
        result = json.loads(p.stdout)
        if not result.get('ok'):
            raise ValueError(result.get('message', 'Home operation failed'))
        return json.dumps(result, ensure_ascii=False)
    if action == 'settings':
        p = subprocess.run(['luna-send', '-n', '1', '-f',
                            'luna://com.webos.service.applicationManager/launch',
                            '{"id":"com.palm.app.settings"}'], capture_output=True, text=True, timeout=10, check=True)
        return p.stdout
    if action in ('legacy-status', 'autostart-status'):
        filename = 'home_key_helper.py' if action == 'legacy-status' else 'autostart_helper.py'
        script = os.path.join(os.path.dirname(helper), filename)
        p = subprocess.run(['python3', script, 'status'], capture_output=True, text=True, timeout=25)
        result = json.loads(p.stdout)
        if not result.get('ok'):
            raise ValueError(result.get('message', 'Status unavailable'))
        return json.dumps(result, ensure_ascii=False)
    if action == 'backup-read':
        with open(backup, 'r', encoding='utf-8') as f:
            text = f.read(262145)
        if len(text.encode('utf-8')) > 262144:
            raise ValueError('Backup too large')
        return text
    if action == 'backup-write':
        data = data.get('backup')
        if not isinstance(data, dict) or data.get('format') != 'g5-home-settings' or not isinstance(data.get('settings'), dict):
            raise ValueError('Invalid backup')
        import tempfile
        os.makedirs(os.path.dirname(backup), mode=0o700, exist_ok=True)
        fd, tmp = tempfile.mkstemp(prefix='.backup-', dir=os.path.dirname(backup))
        try:
            with os.fdopen(fd, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, backup)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        return 'G5_BACKUP_OK'
    raise ValueError('Unknown operation')


def handler(token, helper, backup):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def do_POST(self):
            if self.path != '/api' or not hmac.compare_digest(self.headers.get('X-G5-Token', ''), token):
                self.send_error(403)
                return
            try:
                length = int(self.headers.get('Content-Length', '0'))
                if length <= 0 or length > MAX_BODY:
                    raise ValueError('Invalid request size')
                data = json.loads(self.rfile.read(length).decode('utf-8'))
                if not isinstance(data, dict):
                    raise ValueError('Invalid request')
                output = execute(data.get('action'), data, helper, backup)
                payload = {'returnValue': True, 'stdoutString': output}
            except Exception as error:
                payload = {'returnValue': False, 'errorText': str(error)}
            raw = json.dumps(payload, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', 'null')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_OPTIONS(self):
            self.send_response(204)
            self.send_header('Access-Control-Allow-Origin', 'null')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-G5-Token')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.end_headers()
    return Handler


def start(token, helper, backup, port=0):
    return ThreadingHTTPServer(('127.0.0.1', port), handler(token, helper, backup))


if __name__ == '__main__':
    import sys
    import tempfile
    config_path, helper_path, backup_path = sys.argv[1:4]
    with open(config_path, encoding='utf-8') as f:
        config = json.load(f)
    server = start(config['token'], helper_path, backup_path)
    config['port'] = server.server_port
    config['pid'] = os.getpid()
    fd, tmp = tempfile.mkstemp(prefix='.bridge-', dir=os.path.dirname(config_path))
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        json.dump(config, f)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, config_path)
    server.serve_forever()
