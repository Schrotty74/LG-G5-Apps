#!/usr/bin/env python3
"""Opt-in Home takeover. Original LG files are never overwritten.

Independent implementation informed by Glasshouse's documented mount/rescan
approach. No Glasshouse runtime or server is required.
"""
import base64
import fcntl
import importlib.util
import json
import os
import secrets
import shutil
import signal
import subprocess
import sys
import tempfile
import time

APP_ID = 'org.schrotty74.g5launcher'
LG_HOME = 'com.webos.app.home'
APP = os.path.dirname(os.path.realpath(__file__))
TARGET = '/usr/palm/applications/' + LG_HOME
STATE = '/var/lib/webosbrew/g5-tv-launcher/home-mode'
STAGE = STATE + '/app'
CONFIG = STATE + '/mode.json'
PREFS = STATE + '/preferences.json'
BEAT = STATE + '/heartbeat'
HOOK = '/var/lib/webosbrew/init.d/61-g5-tv-launcher-home'
BOOT = APP + '/home_mode_boot.sh'
HELPER = APP + '/home_mode_helper.py'
PID = STATE + '/watch.pid'
BRIDGE_CONFIG = STATE + '/bridge.json'
BRIDGE = APP + '/home_bridge.py'
BACKUP = '/media/developer/g5-tv-launcher/backup.json'
VENDOR = 'Schrotty74 Home takeover'


def load(path, default=None):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def atomic(path, data):
    os.makedirs(os.path.dirname(path), mode=0o700, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix='.g5-', dir=os.path.dirname(path))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def run(args, timeout=12):
    p = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       timeout=timeout, text=True)
    if p.returncode:
        raise RuntimeError('Command failed: ' + args[0])
    return p.stdout


def luna(method, payload):
    value = json.loads(run(['luna-send', '-n', '1', '-f', 'luna://' + method,
                           json.dumps(payload)], timeout=8))
    if value.get('returnValue') is not True:
        raise RuntimeError(str(value.get('errorText', method + ' refused')))
    return value


def info():
    return luna('com.webos.applicationManager/getAppInfo', {'id': LG_HOME})['appInfo']


def owned_mount():
    try:
        a, b = os.stat(TARGET), os.stat(STAGE)
        return (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)
    except OSError:
        return False


def foreign_mount():
    # Do not stack our mount over Glasshouse or another owner's mount.
    with open('/proc/self/mountinfo', encoding='utf-8') as f:
        return any(line.split()[4] == TARGET for line in f) and not owned_mount()


def glasshouse_enabled():
    config = load('/var/lib/tvweb/home.json', {})
    return isinstance(config, dict) and (config.get('enabled') is True or config.get('restorePending') is True)


def own_hook():
    return os.path.islink(HOOK) and os.readlink(HOOK) == BOOT


def hook(on):
    if os.path.lexists(HOOK) and not own_hook():
        raise RuntimeError('The Home startup hook belongs to another application.')
    if on:
        if not os.path.isfile(BOOT) or not os.access(BOOT, os.X_OK):
            raise RuntimeError('The Home startup script is missing or not executable.')
        os.makedirs(os.path.dirname(HOOK), exist_ok=True)
        if not own_hook():
            os.symlink(BOOT, HOOK)
    elif own_hook():
        os.unlink(HOOK)


def module(name):
    spec = importlib.util.spec_from_file_location('g5_' + name, APP + '/' + name + '.py')
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def mapper_status():
    mapper = module('home_key_helper')
    if not os.path.exists(mapper.CTL):
        return None
    # An installed mapper that cannot be inspected is a conflict, not "absent".
    return mapper.read_status()


def snapshot_legacy():
    auto = module('autostart_helper').get_status()
    if not auto.get('ok'):
        raise RuntimeError(auto.get('message', 'Cannot inspect legacy autostart.'))
    state = mapper_status()
    mapper = module('home_key_helper')
    mapped = bool(state and mapper.is_target(state['config'].get('home')))
    return {'auto': bool(auto['enabled']), 'mapped': mapped}


def remove_legacy():
    mapper = module('home_key_helper')
    state = mapper_status()
    if state and mapper.is_target(state['config'].get('home')):
        previous = mapper.read_backup()
        # A non-default previous Home action would still intercept Home.
        if previous['existed']:
            raise RuntimeError('The saved Home mapping is not LG default. Restore it in Magic Mapper and remove its Home mapping before using direct Home.')
        mapper.main('restore')
        state = mapper_status()
    if state and 'home' in state['config']:
        raise RuntimeError('Magic Mapper has a different Home mapping. Remove that Home mapping first; other buttons may stay mapped.')
    auto = module('autostart_helper')
    if auto.own_hook() or auto.worker_pid():
        auto.disable()


def restore_legacy(saved):
    auto = module('autostart_helper')
    mapper = module('home_key_helper')
    current = snapshot_legacy()
    if saved.get('mapped') and not current['mapped']:
        mapper.main('enable')
    elif not saved.get('mapped') and current['mapped']:
        mapper.main('restore')
    if saved.get('auto'):
        auto.enable()
    elif auto.own_hook() or auto.worker_pid():
        auto.disable()


def preferences(encoded):
    if len(encoded) > 350000:
        raise RuntimeError('Settings payload is too large.')
    data = json.loads(base64.b64decode(encoded, validate=True).decode('utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('showClock'), bool) or not isinstance(data.get('city'), str):
        raise RuntimeError('Invalid launcher settings.')
    atomic(PREFS, data)
    return data


def bridge_start():
    # The token is stored only in owner-readable state and embedded in the
    # mounted app page. The bridge listens on loopback, never on the LAN.
    os.makedirs(STATE, mode=0o700, exist_ok=True)
    old = load(BRIDGE_CONFIG, {})
    pid = old.get('pid') if isinstance(old, dict) else None
    if isinstance(pid, int) and pid > 1:
        try:
            with open('/proc/%d/cmdline' % pid, 'rb') as f:
                args = f.read().split(b'\0')
            if BRIDGE.encode() in args and BRIDGE_CONFIG.encode() in args:
                os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
    token = secrets.token_urlsafe(32)
    atomic(BRIDGE_CONFIG, {'token': token})
    with open(os.devnull, 'rb') as inp, open(STATE + '/bridge.log', 'ab') as out:
        proc = subprocess.Popen([sys.executable, BRIDGE, BRIDGE_CONFIG, HELPER, BACKUP],
                                stdin=inp, stdout=out, stderr=out, start_new_session=True, close_fds=True)
    for _ in range(40):
        cfg = load(BRIDGE_CONFIG, {})
        if cfg.get('pid') == proc.pid and isinstance(cfg.get('port'), int) and cfg.get('token') == token:
            return cfg
        if proc.poll() is not None:
            break
        time.sleep(.1)
    if proc.poll() is None:
        proc.terminate()
    raise RuntimeError('The local Home bridge failed to start.')


def bridge_stop():
    cfg = load(BRIDGE_CONFIG, {})
    pid = cfg.get('pid') if isinstance(cfg, dict) else None
    if isinstance(pid, int) and pid > 1:
        try:
            with open('/proc/%d/cmdline' % pid, 'rb') as f:
                args = f.read().split(b'\0')
            if BRIDGE.encode() in args and BRIDGE_CONFIG.encode() in args:
                os.kill(pid, signal.SIGTERM)
        except OSError:
            pass
    try:
        os.unlink(BRIDGE_CONFIG)
    except FileNotFoundError:
        pass


def stage():
    if not os.path.isdir(TARGET):
        raise RuntimeError('LG Home directory was not found.')
    if owned_mount():
        # Never rewrite a running mounted application in place.
        return
    cfg = bridge_start()
    os.makedirs(STAGE, mode=0o700, exist_ok=True)
    for name in ['index.html', 'script.js', 'home_bridge.js', 'home_mode.js', 'i18n.js', 'style.css', 'icon.png', 'largeIcon.png']:
        shutil.copyfile(APP + '/' + name, STAGE + '/' + name)
    shutil.copytree(APP + '/scenes', STAGE + '/scenes', dirs_exist_ok=True)
    shutil.copytree(APP + '/weather-icons', STAGE + '/weather-icons', dirs_exist_ok=True)
    with open(STAGE + '/index.html', encoding='utf-8') as f:
        page = f.read()
    bootstrap = '<script>window.G5_DIRECT_HOME=true;window.G5_BRIDGE=' + json.dumps({'port': cfg['port'], 'token': cfg['token']}) + ';</script>'
    page = page.replace('<head>', '<head>' + bootstrap, 1)
    with open(STAGE + '/index.html', 'w', encoding='utf-8') as f:
        f.write(page)
    meta = load(APP + '/appinfo.json')
    meta.update(id=LG_HOME, vendor=VENDOR, title='G5 Home', visible=False,
                appCategory=['home'], resolution='1920x1080')
    atomic(STAGE + '/appinfo.json', meta)
    # The mounted UI must be readable by WebAppMgr, while the private state
    # and preferences outside this subtree remain owner-only.
    for parent, dirs, files in os.walk(STAGE):
        os.chmod(parent, 0o755)
        for name in files:
            os.chmod(os.path.join(parent, name), 0o644)


def reread(expected):
    # On webOS 25, block/release makes SAM reread this app without a SAM restart.
    payload = {'id': LG_HOME}
    schema = '/etc/palm/schemas/sam/applicationManager.blockSystemApp.schema'
    try:
        with open(schema, encoding='utf-8') as f:
            if '"forceBlockSystemApp"' in f.read():
                payload['forceBlockSystemApp'] = False
    except FileNotFoundError:
        pass
    block_error = None
    try:
        luna('com.webos.applicationManager/blockSystemApp', payload)
    except Exception as e:
        block_error = e
    finally:
        released = False
        for _ in range(3):
            try:
                luna('com.webos.applicationManager/releaseBlockSystemApp', {'id': LG_HOME})
                released = True
                break
            except Exception:
                time.sleep(.4)
        if not released:
            raise RuntimeError('LG Home could not be released. Run the recovery command; it will retry releaseBlockSystemApp.')
    if block_error:
        raise block_error
    for _ in range(12):
        value = info()
        if expected(value):
            return
        time.sleep(.3)
    raise RuntimeError('webOS did not load the requested Home entry.')


def stop_lg_process():
    for pid in os.listdir('/proc'):
        if not pid.isdigit():
            continue
        try:
            with open('/proc/' + pid + '/cmdline', 'rb') as f:
                argv = [x.decode('utf-8', 'replace') for x in f.read().split(b'\0') if x]
            native = argv and argv[0] == '/usr/bin/' + LG_HOME
            flutter = argv and os.path.basename(argv[0]) == 'flutter-client' and '-i' in argv and argv[argv.index('-i') + 1:argv.index('-i') + 2] == [LG_HOME]
            if native or flutter:
                os.kill(int(pid), signal.SIGTERM)
        except (OSError, IndexError):
            pass


def direct_manifest(value):
    return value.get('vendor') == VENDOR and value.get('type') == 'web' and 'home' in value.get('appCategory', [])


def take():
    if glasshouse_enabled() or foreign_mount():
        raise RuntimeError('Another Home takeover is enabled. Switch Glasshouse Home off first.')
    stage()
    if not owned_mount():
        run(['/bin/mount', '--bind', STAGE, TARGET])
    if not owned_mount():
        raise RuntimeError('The Home mount could not be verified.')
    reread(direct_manifest)
    stop_lg_process()


def release():
    if foreign_mount():
        raise RuntimeError('Another application owns the Home mount; it was not changed.')
    if owned_mount():
        try:
            run(['/bin/umount', TARGET])
        except Exception:
            # A running page may hold the bind mount. Detach only our mount.
            if owned_mount():
                run(['/bin/umount', '-l', TARGET])
    if owned_mount():
        raise RuntimeError('The Home mount is still active.')
    original = load(TARGET + '/appinfo.json')
    reread(lambda value: value.get('vendor') == original.get('vendor') and value.get('type') == original.get('type'))
    # Only after SAM reports LG's manifest do we close the old web page.
    try:
        luna('com.palm.webappmanager/killApp', {'appId': LG_HOME})
    except Exception:
        pass
    bridge_stop()


def launch_home():
    luna('com.webos.applicationManager/launch', {'id': LG_HOME})


def fresh_beat(since):
    try:
        return os.path.getmtime(BEAT) >= since
    except OSError:
        return False


def verify_view():
    since = time.time()
    launch_home()
    for _ in range(70):
        if fresh_beat(since):
            points = luna('com.webos.applicationManager/listLaunchPoints', {'subscribe': False})
            if not isinstance(points.get('launchPoints'), list):
                raise RuntimeError('The local Home bridge cannot read the app list.')
            return
        time.sleep(.5)
    raise RuntimeError('The direct Home page did not send a heartbeat within 35 seconds; check Homebrew service access under the LG Home identity.')


def state_status():
    config = load(CONFIG, {})
    mounted = owned_mount()
    current = info()
    legacy = snapshot_legacy()
    direct = mounted and direct_manifest(current)
    foreign = foreign_mount() or glasshouse_enabled()
    method = 'direct' if direct else ('legacy' if legacy['mapped'] or legacy['auto'] else 'lg')
    return {'ok': True, 'method': method, 'configured': config.get('method', 'lg'),
            'mounted': mounted, 'registered': direct_manifest(current),
            'verified': direct and fresh_beat(time.time() - 45),
            'startup': own_hook(), 'watching': bool(watch_pid()),
            'legacy': legacy, 'conflict': foreign,
            'transition': config.get('transition'), 'error': config.get('error', '')}


def watch_pid():
    try:
        pid = int(open(PID, encoding='ascii').read().strip())
        if pid <= 1:
            return None
        with open('/proc/%d/cmdline' % pid, 'rb') as f:
            args = f.read().split(b'\0')
        if HELPER.encode() not in args or b'watch' not in args:
            return None
        os.kill(pid, 0)
        return pid
    except (OSError, ValueError):
        return None


def start_watch():
    if watch_pid():
        return
    with open(os.devnull, 'rb') as inp, open(STATE + '/watch.log', 'ab') as out:
        subprocess.Popen([sys.executable, HELPER, 'watch'], stdin=inp, stdout=out,
                         stderr=out, start_new_session=True, close_fds=True)
    for _ in range(30):
        if watch_pid():
            return
        time.sleep(.1)
    raise RuntimeError('The Home recovery monitor did not start.')


def switch(method, encoded=None):
    config = load(CONFIG, {})
    if config.get('transition'):
        raise RuntimeError('A previous switch was interrupted. Use Restore LG Home first.')
    if foreign_mount() or glasshouse_enabled():
        raise RuntimeError('Switch Glasshouse Home off before changing the launcher method.')
    saved = snapshot_legacy()
    previous = 'direct' if owned_mount() else 'legacy'
    if method == 'direct' and owned_mount() and direct_manifest(info()):
        start_watch()
        return state_status()
    # Durable journal precedes any system change.
    atomic(CONFIG, {'method': config.get('method', 'lg'), 'transition': method,
                    'previous': previous, 'legacy': saved})
    try:
        if method == 'direct':
            if not encoded:
                raise RuntimeError('Launcher settings are required before switching.')
            preferences(encoded)
            remove_legacy()
            hook(True)
            take()
            verify_view()
            atomic(CONFIG, {'method': 'direct', 'legacy': saved})
            start_watch()
        else:
            if owned_mount() or direct_manifest(info()):
                release()
            hook(False)
            if method == 'legacy':
                restore_legacy({'auto': True, 'mapped': True})
            else:
                remove_legacy()
            atomic(CONFIG, {'method': method})
            if method == 'lg':
                launch_home()
    except Exception as failure:
        rollback_error = None
        try:
            if previous == 'direct':
                remove_legacy()
                hook(True)
                take()
                atomic(CONFIG, {'method': 'direct', 'legacy': saved, 'error': str(failure)})
                start_watch()
            else:
                if owned_mount() or direct_manifest(info()):
                    release()
                else:
                    bridge_stop()
                hook(False)
                restore_legacy(saved)
                atomic(CONFIG, {'method': 'legacy' if saved['auto'] or saved['mapped'] else 'lg', 'error': str(failure)})
        except Exception as e:
            rollback_error = str(e)
        if rollback_error:
            raise RuntimeError(str(failure) + ' Recovery incomplete: ' + rollback_error + '. Use the recovery command.')
        raise RuntimeError(str(failure) + ' Previous method restored.')
    return state_status()


def recover():
    # No mapper is required for the independent emergency route.
    if foreign_mount() or glasshouse_enabled():
        raise RuntimeError('A different Home takeover is active; disable it in its owner application.')
    hook(False)  # Prevent reactivation even if later restoration needs retrying.
    if owned_mount() or direct_manifest(info()):
        release()
    else:
        # A prior interrupted block is released without changing any files.
        luna('com.webos.applicationManager/releaseBlockSystemApp', {'id': LG_HOME})
        bridge_stop()
    atomic(CONFIG, {'method': 'lg'})
    launch_home()
    return {'ok': True, 'method': 'lg'}


def boot():
    config = load(CONFIG, {})
    if config.get('transition'):
        # An interrupted transaction must never turn a takeover on at boot.
        return recover()
    if config.get('method') != 'direct' or not own_hook():
        return {'ok': True}
    try:
        remove_legacy()
        take()
        verify_view()
        start_watch()
    except Exception as e:
        recover()
        atomic(CONFIG, {'method': 'lg', 'error': 'Boot recovery: ' + str(e)})
    return {'ok': True}


def watch():
    # Only our own worker PID can be acted upon. No global process restarts.
    fd = open(STATE + '/watch.lock', 'a+')
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return
    with open(PID, 'w', encoding='ascii') as f:
        f.write(str(os.getpid()))
    foreground_since = None
    try:
        while load(CONFIG, {}).get('method') == 'direct' and own_hook():
            time.sleep(4)
            config = load(CONFIG, {})
            if config.get('transition'):
                continue
            try:
                front = luna('com.webos.applicationManager/getForegroundAppInfo', {}).get('appId')
                if front != LG_HOME:
                    foreground_since = None
                    continue
                if foreground_since is None:
                    foreground_since = time.time()
                if time.time() - foreground_since > 45 and not fresh_beat(time.time() - 45):
                    with locked():
                        config = load(CONFIG, {})
                        if config.get('method') != 'direct' or config.get('transition'):
                            continue
                        recover()
                        atomic(CONFIG, {'method': 'lg', 'error': 'Home page stopped answering; LG Home restored.'})
                    break
            except Exception as e:
                print('Home monitor:', str(e), flush=True)
    finally:
        try:
            if int(open(PID).read()) == os.getpid():
                os.unlink(PID)
        except (OSError, ValueError):
            pass
        fd.close()


class locked:
    def __enter__(self):
        os.makedirs(STATE, mode=0o700, exist_ok=True)
        self.file = open(STATE + '/operation.lock', 'a+')
        try:
            fcntl.flock(self.file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            self.file.close()
            raise RuntimeError('A Home operation is already running. Wait and refresh the status.')
        return self

    def __exit__(self, *_):
        self.file.close()


def main(args):
    action = args[0] if args else 'status'
    if action == 'heartbeat':
        if not owned_mount():
            raise RuntimeError('Direct Home is not mounted.')
        with open(BEAT, 'w', encoding='ascii') as f:
            f.write(str(time.time()))
        return {'ok': True}
    if action == 'prefs-load':
        return {'ok': True, 'settings': load(PREFS)}
    if action == 'prefs-save' and len(args) == 2:
        preferences(args[1])
        return {'ok': True}
    if action == 'watch':
        watch()
        return {'ok': True}
    with locked():
        if action == 'status':
            return state_status()
        if action in ('direct', 'legacy', 'lg'):
            return switch(action, args[1] if len(args) == 2 else None)
        if action == 'recover':
            return recover()
        if action == 'boot':
            return boot()
        raise RuntimeError('Unknown Home operation.')


if __name__ == '__main__':
    try:
        result = main(sys.argv[1:])
    except Exception as error:
        result = {'ok': False, 'message': str(error)}
    print(json.dumps(result, ensure_ascii=False))
    sys.exit(0 if result.get('ok') else 1)
