#!/usr/bin/env python3
"""Opt-in boot and wake launcher for rooted webOS; no key mappings are changed."""
import fcntl
import json
import os
import signal
import subprocess
import tempfile
import sys
import time

APP_ID = 'org.schrotty74.g5launcher'
APP_DIR = '/media/developer/apps/usr/palm/applications/' + APP_ID
HELPER = APP_DIR + '/autostart_helper.py'
BOOT_SCRIPT = APP_DIR + '/autostart_boot.sh'
STATE_DIR = '/var/lib/webosbrew/g5-tv-launcher'
HOOK = '/var/lib/webosbrew/init.d/60-g5-tv-launcher-autostart'
PID_FILE = STATE_DIR + '/autostart.pid'
LOCK_FILE = STATE_DIR + '/autostart.lock'
LOG_FILE = STATE_DIR + '/autostart.log'
MARKER = '# Managed by org.schrotty74.g5launcher autostart v1'
HOOK_CONTENT = ('#!/bin/sh\n' + MARKER + '\n'
                + 'nohup python3 ' + HELPER + ' watch boot </dev/null >/dev/null 2>&1 &\nexit 0\n')
POWER_URI = 'luna://com.webos.service.tvpower/power/getPowerState'
LAUNCH_URI = 'luna://com.webos.applicationManager/launch'


def legacy_hook():
    try:
        if os.path.islink(HOOK): return False
        with open(HOOK, encoding='utf-8') as f: return f.read() == HOOK_CONTENT
    except (FileNotFoundError, IsADirectoryError, UnicodeError):
        return False


def linked_hook():
    try:
        return os.path.islink(HOOK) and os.readlink(HOOK) == BOOT_SCRIPT
    except OSError:
        return False


def own_hook():
    # The legacy file remains valid until the safe migration has finished.
    return linked_hook() or legacy_hook()


def stop_worker():
    pid = worker_pid()
    if pid:
        os.kill(pid, signal.SIGTERM)
        for _ in range(30):
            if not worker_pid(): break
            time.sleep(.1)
    if worker_pid():
        raise RuntimeError('Autostart-Überwachung konnte nicht beendet werden.')


def start_worker():
    if worker_pid(): return
    with open(os.devnull, 'rb') as null_in, open(LOG_FILE, 'ab') as log:
        subprocess.Popen([sys.executable, HELPER, 'watch', 'wake'], stdin=null_in,
                         stdout=log, stderr=log, start_new_session=True, close_fds=True)
    for _ in range(30):
        if worker_pid(): return
        time.sleep(.1)
    raise RuntimeError('Autostart konnte nicht gestartet werden.')


def check_files():
    if not os.path.isfile(HELPER) or not os.path.isfile(BOOT_SCRIPT):
        raise RuntimeError('Autostart-Helfer wurde nicht gefunden.')
    if not os.access(BOOT_SCRIPT, os.X_OK):
        raise RuntimeError('Autostart-Skript ist nicht ausführbar.')


def migrate_legacy():
    if not legacy_hook(): return
    check_files()
    os.makedirs(STATE_DIR, mode=0o700, exist_ok=True)
    # An old worker uses the former ownership check: stop only our verified PID.
    stop_worker()
    parent = os.path.dirname(HOOK)
    fd, temp = tempfile.mkstemp(prefix='.g5-autostart-', dir=parent)
    os.close(fd)
    os.unlink(temp)
    try:
        os.symlink(BOOT_SCRIPT, temp)
        if not legacy_hook():
            raise RuntimeError('Autostart-Datei wurde zwischenzeitlich geändert.')
        os.replace(temp, HOOK)
    finally:
        if os.path.lexists(temp): os.unlink(temp)
    # Start the new watcher immediately; no reboot is necessary.
    start_worker()


def worker_pid():
    try:
        with open(PID_FILE, encoding='ascii') as f:
            value = f.read().strip()
        if not value.isdigit() or int(value) <= 1:
            return None
        pid = int(value)
        with open('/proc/%d/cmdline' % pid, 'rb') as f:
            args = f.read().split(b'\0')
        if HELPER.encode() not in args or b'watch' not in args:
            return None
        os.kill(pid, 0)
        return pid
    except (OSError, ValueError):
        return None


def get_status():
    if os.path.lexists(HOOK) and not own_hook():
        return {'ok': False, 'message': 'Autostart-Datei gehört nicht diesem Launcher.'}
    return {'ok': True, 'enabled': own_hook(), 'running': bool(worker_pid())}


def enable():
    try:
        mounted = os.path.samefile('/usr/palm/applications/com.webos.app.home', '/var/lib/webosbrew/g5-tv-launcher/home-mode/app')
    except OSError:
        mounted = False
    if mounted:
        raise RuntimeError('Direkte Home-Übernahme ist aktiv. Zuerst im Menü die Methode wechseln.')
    if os.path.lexists(HOOK) and not own_hook():
        raise RuntimeError('Autostart-Datei gehört nicht diesem Launcher.')
    check_files()
    os.makedirs(os.path.dirname(HOOK), exist_ok=True)
    os.makedirs(STATE_DIR, mode=0o700, exist_ok=True)
    if legacy_hook(): migrate_legacy()
    created = False
    if not linked_hook():
        os.symlink(BOOT_SCRIPT, HOOK)
        created = True
    try:
        start_worker()
    except Exception:
        if created and linked_hook(): os.unlink(HOOK)
        raise
    return get_status()


def disable():
    if os.path.lexists(HOOK) and not own_hook():
        raise RuntimeError('Autostart-Datei gehört nicht diesem Launcher.')
    if own_hook(): os.unlink(HOOK)
    stop_worker()
    return get_status()


def wake_transition(previous, current):
    return previous in ('Suspend', 'Active Standby') and current == 'Active'


def launch():
    payload = json.dumps({'id': APP_ID}, separators=(',', ':'))
    try:
        result = subprocess.run(['luna-send', '-n', '1', '-f', LAUNCH_URI, payload],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
        response = json.loads(result.stdout.decode('utf-8'))
        return result.returncode == 0 and response.get('returnValue') is True
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return False


def worker(boot):
    os.makedirs(STATE_DIR, mode=0o700, exist_ok=True)
    lock = open(LOCK_FILE, 'a+')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return 0
    with open(PID_FILE, 'w', encoding='ascii') as f: f.write(str(os.getpid()))
    child = None
    def stop(_sig, _frame):
        if child and child.poll() is None:
            child.terminate()
        raise SystemExit(0)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        # Wait for webOS startup and the normal LG Home launch to settle.
        # Bounded retries are used only around power-on, not while browsing apps.
        if boot:
            time.sleep(10)
            for _ in range(6):
                if not own_hook() or launch(): break
                time.sleep(5)
        while own_hook():
            try:
                child = subprocess.Popen(['luna-send', '-i', '-f', POWER_URI, '{"subscribe":true}'],
                                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                         text=True, bufsize=1)
                previous = None
                buf = ''
                for line in child.stdout:
                    buf += line
                    if len(buf) > 65536: buf = ''
                    try: data = json.loads(buf)
                    except ValueError: continue
                    buf = ''
                    state = data.get('state')
                    if not isinstance(state, str): continue
                    if wake_transition(previous, state) and own_hook():
                        time.sleep(2.5)
                        if own_hook(): launch()
                    previous = state
                child.wait(timeout=5)
            except (OSError, subprocess.TimeoutExpired):
                if child and child.poll() is None: child.terminate()
            finally:
                child = None
            if own_hook(): time.sleep(10)
    finally:
        try:
            with open(PID_FILE, encoding='ascii') as f: mine = f.read().strip() == str(os.getpid())
            if mine: os.unlink(PID_FILE)
        except OSError: pass
        lock.close()
    return 0


def main():
    action = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if action == 'watch':
        return worker(len(sys.argv) > 2 and sys.argv[2] == 'boot')
    if action not in ('status', 'enable', 'disable'):
        raise RuntimeError('Ungültige Aktion.')
    if action == 'status' and legacy_hook():
        migrate_legacy()
    result = {'status': get_status, 'enable': enable, 'disable': disable}[action]()
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, RuntimeError) as exc:
        print(json.dumps({'ok': False, 'message': str(exc)}, ensure_ascii=False))
        sys.exit(1)
