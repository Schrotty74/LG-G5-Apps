"""Host-side regression tests. No TV commands, mounts or system writes run."""
import base64
import importlib.util
import json
import io
from contextlib import redirect_stdout, redirect_stderr
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

SPEC = importlib.util.spec_from_file_location('home_mode', Path(__file__).parent / 'app/home_mode_helper.py')
h = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(h)


class HomeModeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        for name in ['STATE', 'STAGE', 'CONFIG', 'PREFS', 'BEAT', 'HOOK', 'PID', 'TARGET']:
            filename = self.temp.name if name == 'STATE' else self.temp.name + '/' + name.lower()
            p = patch.object(h, name, filename)
            p.start()
            self.addCleanup(p.stop)
        self.payload = base64.b64encode(json.dumps({'showClock': True, 'city': '', 'favorites': ['demo.app']}).encode()).decode()

    def test_stage_copies_weather_assets_for_direct_home(self):
        Path(h.TARGET).mkdir()
        with patch.object(h, 'owned_mount', return_value=False), patch.object(h, 'bridge_start', return_value={'port': 1234, 'token': 'test'}):
            h.stage()
        source = Path(h.APP) / 'weather-icons'
        expected = [p.relative_to(source) for p in source.rglob('*') if p.is_file()]
        self.assertTrue(expected)
        for item in expected:
            self.assertEqual((Path(h.STAGE) / 'weather-icons' / item).read_bytes(), (source / item).read_bytes())

    def test_boot_failure_records_traceback_and_recovers(self):
        h.atomic(h.CONFIG, {'method': 'direct'})
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(h, 'own_hook', return_value=True), patch.object(h, 'take', side_effect=PermissionError(13, 'Permission denied', '')), patch.object(h, 'recover') as recover, redirect_stdout(stdout), redirect_stderr(stderr):
            self.assertEqual(h.boot(), {'ok': True})
        recover.assert_called_once()
        self.assertIn('BOOT DIAGNOSTIC: take', stdout.getvalue())
        self.assertIn('PermissionError', stderr.getvalue())
        self.assertEqual(h.load(h.CONFIG)['method'], 'lg')

    def test_direct_boot_does_not_check_magic_mapper(self):
        h.atomic(h.CONFIG, {'method': 'direct'})
        with patch.object(h, 'own_hook', return_value=True), patch.object(h, 'remove_legacy', side_effect=AssertionError('Magic Mapper checked')), patch.object(h, 'take'), patch.object(h, 'verify_view'), patch.object(h, 'start_watch'), redirect_stdout(io.StringIO()):
            self.assertEqual(h.boot(), {'ok': True})

    def test_preferences_preserve_favorites_and_unknown_existing_keys(self):
        data = h.preferences(self.payload)
        self.assertEqual(h.load(h.PREFS), data)
        self.assertEqual(data['favorites'], ['demo.app'])
        self.assertEqual(os.stat(h.PREFS).st_mode & 0o777, 0o600)

    def test_invalid_preferences_do_not_replace_existing(self):
        h.preferences(self.payload)
        old = Path(h.PREFS).read_bytes()
        with self.assertRaises(Exception):
            h.preferences(base64.b64encode(b'[]').decode())
        self.assertEqual(Path(h.PREFS).read_bytes(), old)

    def test_foreign_hook_not_overwritten_or_deleted(self):
        Path(h.HOOK).write_text('someone else')
        for on in [True, False]:
            with self.assertRaises(RuntimeError):
                h.hook(on)
        self.assertEqual(Path(h.HOOK).read_text(), 'someone else')

    def test_own_hook_removed(self):
        os.symlink(h.BOOT, h.HOOK)
        h.hook(False)
        self.assertFalse(os.path.lexists(h.HOOK))

    def test_owned_mount_uses_inode_identity(self):
        Path(h.TARGET).mkdir()
        Path(h.STAGE).symlink_to(h.TARGET)
        self.assertTrue(h.owned_mount())
        Path(h.STAGE).unlink()
        Path(h.STAGE).mkdir()
        self.assertFalse(h.owned_mount())

    def test_foreign_takeover_refused_before_mutation(self):
        with patch.object(h, 'foreign_mount', return_value=True), patch.object(h, 'snapshot_legacy') as snap:
            with self.assertRaisesRegex(RuntimeError, 'Glasshouse'):
                h.switch('direct', self.payload)
            snap.assert_not_called()
        self.assertFalse(os.path.exists(h.CONFIG))

    def test_pending_transaction_requires_recovery(self):
        h.atomic(h.CONFIG, {'transition': 'direct'})
        with self.assertRaisesRegex(RuntimeError, 'interrupted'):
            h.switch('direct', self.payload)

    def test_release_always_attempted_after_block_timeout(self):
        calls = []
        def luna(method, payload):
            calls.append(method)
            if method.endswith('/blockSystemApp'):
                raise RuntimeError('timeout')
            return {'returnValue': True}
        with patch.object(h, 'luna', side_effect=luna):
            with self.assertRaisesRegex(RuntimeError, 'timeout'):
                h.reread(lambda x: True)
        self.assertEqual(calls[-1], 'com.webos.applicationManager/releaseBlockSystemApp')

    def test_release_failure_is_not_success(self):
        with patch.object(h, 'luna', side_effect=RuntimeError('refused')), patch.object(h.time, 'sleep'):
            with self.assertRaisesRegex(RuntimeError, 'could not be released'):
                h.reread(lambda x: True)

    def test_rescan_checks_actual_manifest(self):
        with patch.object(h, 'luna', return_value={'returnValue': True}), patch.object(h, 'info', return_value={'type': 'native'}), patch.object(h.time, 'sleep'):
            with self.assertRaisesRegex(RuntimeError, 'did not load'):
                h.reread(h.direct_manifest)

    def test_direct_manifest_requires_vendor_type_and_category(self):
        self.assertFalse(h.direct_manifest({'type': 'web', 'appCategory': ['home']}))
        self.assertFalse(h.direct_manifest({'vendor': h.VENDOR, 'type': 'web'}))
        self.assertTrue(h.direct_manifest({'vendor': h.VENDOR, 'type': 'web', 'appCategory': ['home']}))

    def test_custom_mapper_home_not_changed(self):
        mapper = Mock()
        mapper.is_target.return_value = False
        with patch.object(h, 'module', return_value=mapper), patch.object(h, 'mapper_status', return_value={'config': {'home': {'other': 'app'}, 'netflix': 'unchanged'}}):
            with self.assertRaisesRegex(RuntimeError, 'different Home mapping'):
                h.remove_legacy()
            mapper.main.assert_not_called()

    def test_our_mapper_entry_and_autostart_removed(self):
        mapper, auto = Mock(), Mock()
        mapper.is_target.side_effect = [True]
        mapper.read_backup.return_value = {'existed': False}
        auto.own_hook.return_value = True
        with patch.object(h, 'module', side_effect=lambda name: mapper if name == 'home_key_helper' else auto), patch.object(h, 'mapper_status', side_effect=[{'config': {'home': 'ours'}}, {'config': {'netflix': 'preserved'}}]):
            h.remove_legacy()
        mapper.main.assert_called_once_with('restore')
        auto.disable.assert_called_once()

    def test_missing_mapper_is_allowed(self):
        mapper = Mock(CTL=self.temp.name + '/missing')
        with patch.object(h, 'module', return_value=mapper):
            self.assertIsNone(h.mapper_status())
        mapper.read_status.assert_not_called()

    def transaction(self, failure=False):
        saved = {'auto': True, 'mapped': True}
        mocks = {}
        for name, value in [('foreign_mount', False), ('glasshouse_enabled', False), ('owned_mount', False), ('snapshot_legacy', saved), ('info', {'type': 'native'}), ('state_status', {'ok': True, 'method': 'direct'})]:
            p = patch.object(h, name, return_value=value)
            mocks[name] = p.start()
            self.addCleanup(p.stop)
        for name in ['stage', 'remove_legacy', 'restore_legacy', 'hook', 'release', 'start_watch']:
            p = patch.object(h, name)
            mocks[name] = p.start()
            self.addCleanup(p.stop)
        def take():
            # The rollback journal must already exist before takeover.
            self.assertEqual(h.load(h.CONFIG)['transition'], 'direct')
        p = patch.object(h, 'take', side_effect=take)
        mocks['take'] = p.start()
        self.addCleanup(p.stop)
        p = patch.object(h, 'verify_view', side_effect=RuntimeError('no heartbeat') if failure else None)
        mocks['verify_view'] = p.start()
        self.addCleanup(p.stop)
        return mocks, saved

    def test_success_commits_only_after_view_verified(self):
        mocks, _ = self.transaction()
        self.assertEqual(h.switch('direct', self.payload)['method'], 'direct')
        self.assertEqual(h.load(h.CONFIG)['method'], 'direct')
        self.assertNotIn('transition', h.load(h.CONFIG))
        mocks['verify_view'].assert_called_once()
        mocks['start_watch'].assert_called_once()

    def test_view_failure_restores_previous_legacy_method(self):
        mocks, saved = self.transaction(failure=True)
        h.atomic(h.CONFIG, {'method': 'legacy'})
        with self.assertRaisesRegex(RuntimeError, 'Previous method restored'):
            h.switch('direct', self.payload)
        mocks['restore_legacy'].assert_called_once_with(saved)
        self.assertEqual(h.load(h.CONFIG)['method'], 'legacy')
        mocks['start_watch'].assert_not_called()

    def test_failed_rollback_keeps_journal_for_recovery(self):
        mocks, _ = self.transaction(failure=True)
        h.atomic(h.CONFIG, {'method': 'legacy'})
        mocks['restore_legacy'].side_effect = RuntimeError('mapper unavailable')
        with self.assertRaisesRegex(RuntimeError, 'Recovery incomplete'):
            h.switch('direct', self.payload)
        self.assertEqual(h.load(h.CONFIG)['transition'], 'direct')

    def test_recovery_clears_our_startup_before_touching_home(self):
        events = []
        with patch.object(h, 'foreign_mount', return_value=False), patch.object(h, 'glasshouse_enabled', return_value=False), patch.object(h, 'owned_mount', return_value=True), patch.object(h, 'hook', side_effect=lambda on: events.append(('hook', on))), patch.object(h, 'release', side_effect=lambda: events.append('release')), patch.object(h, 'launch_home'):
            self.assertTrue(h.recover()['ok'])
        self.assertEqual(events, [('hook', False), 'release'])
        self.assertEqual(h.load(h.CONFIG)['method'], 'lg')

    def test_recovery_never_unmounts_foreign_home(self):
        with patch.object(h, 'foreign_mount', return_value=True), patch.object(h, 'release') as release:
            with self.assertRaises(RuntimeError):
                h.recover()
            release.assert_not_called()


if __name__ == '__main__':
    unittest.main()
