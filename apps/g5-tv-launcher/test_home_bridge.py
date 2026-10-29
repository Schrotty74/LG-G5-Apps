import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

spec = importlib.util.spec_from_file_location('home_bridge', Path(__file__).parent / 'app/home_bridge.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.server = b.start('test-secret', str(self.root / 'helper.py'), str(self.root / 'backup.json'))
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        self.url = 'http://127.0.0.1:%d/api' % self.server.server_port

    def request(self, body, token='test-secret'):
        req = Request(self.url, data=json.dumps(body).encode(),
                      headers={'Content-Type': 'application/json', 'X-G5-Token': token}, method='POST')
        with urlopen(req, timeout=2) as response:
            return json.load(response)

    def test_only_localhost(self):
        self.assertEqual(self.server.server_address[0], '127.0.0.1')

    def test_wrong_token_cannot_execute(self):
        with patch.object(b, 'execute') as execute, self.assertRaises(HTTPError) as error:
            self.request({'action':'apps'}, 'wrong')
        self.assertEqual(error.exception.code, 403)
        execute.assert_not_called()

    def test_arbitrary_command_is_not_an_action(self):
        result = self.request({'action':'exec', 'command':'id'})
        self.assertFalse(result['returnValue'])

    def test_icon_rejects_symlink_outside_allowed_root(self):
        allowed = self.root / 'allowed'
        allowed.mkdir()
        outside = self.root / 'secret.png'
        outside.write_bytes(b'private')
        (allowed / 'image.png').symlink_to(outside)
        with patch.object(b, 'ICON_ROOTS', (str(allowed) + '/',)):
            result = self.request({'action':'icon','path':str(allowed / 'image.png')})
        self.assertFalse(result['returnValue'])

    def test_only_status_actions_allowed_for_legacy(self):
        result = self.request({'action':'home','operation':'direct'})
        self.assertFalse(result['returnValue'])

    def test_app_list_uses_fixed_argument_array(self):
        with patch.object(b.subprocess, 'run') as run:
            run.return_value.stdout = b'{"returnValue":true,"launchPoints":[]}'
            result = self.request({'action':'apps', 'command':'ignored'})
        self.assertTrue(result['returnValue'])
        self.assertEqual(json.loads(result['stdoutString'])['launchPoints'], [])
        self.assertEqual(run.call_args.args[0][0], 'luna-send')
        self.assertNotIn('shell', run.call_args.kwargs)

    def test_backup_roundtrip_and_reject_invalid(self):
        original = {'format':'g5-home-settings','version':1,'settings':{'favorites':['example.app']}}
        self.assertTrue(self.request({'action':'backup-write','backup':original})['returnValue'])
        self.assertFalse(self.request({'action':'backup-write','backup':{'settings':{}}})['returnValue'])
        restored = self.request({'action':'backup-read'})
        self.assertEqual(json.loads(restored['stdoutString']), original)
        self.assertEqual((self.root / 'backup.json').stat().st_mode & 0o777, 0o600)


if __name__ == '__main__':
    unittest.main()
