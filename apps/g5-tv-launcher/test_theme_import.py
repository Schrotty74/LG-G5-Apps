import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('theme_import', Path(__file__).parent / 'app/theme_import.py')
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

class ImportTests(unittest.TestCase):
    def test_lists_and_reads_only_safe_small_regular_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            mod.ROOT = tmp
            Path(tmp, 'theme.json').write_text(json.dumps({'format':'g5-theme','version':1,'id':'spring','name':'Spring','background':'#112233','accent':'#aabbcc','glow':'#334455'}))
            Path(tmp, 'big.json').write_bytes(b'x' * (mod.MAX_BYTES + 1))
            Path(tmp, 'other.txt').write_text('{}')
            Path(tmp, 'cmdlist_factory.json').write_text('{}')
            Path(tmp, 'cmdlist_tvlink_cmdprocessor.json').write_text('{"name":"not a theme"}')
            Path(tmp, 'broken.json').write_text('{')
            os.symlink('theme.json', Path(tmp, 'link.json'))
            self.assertEqual(mod.list_themes(), ['theme.json'])
            self.assertEqual(mod.read_theme('theme.json')['format'], 'g5-theme')
            for name in ['../etc/passwd', 'link.json', 'big.json']:
                with self.assertRaises((ValueError, OSError)):
                    mod.read_theme(name)

if __name__ == '__main__':
    unittest.main()
