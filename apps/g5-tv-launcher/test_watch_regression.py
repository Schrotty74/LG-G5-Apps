import importlib.util, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('helper',Path(__file__).parent/'app/home_mode_helper.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
class MonitorTest(unittest.TestCase):
 def test_stale_heartbeat_does_not_restore_lg_home(self):
  with tempfile.TemporaryDirectory() as d:
   with patch.object(h,'STATE',d), patch.object(h,'PID',d+'/watch.pid'), patch.object(h,'CONFIG',d+'/mode.json'), patch.object(h,'load',side_effect=[{'method':'direct'},{'method':'direct'},{'method':'direct'},{'method':'direct'},{'method':'lg'}]), patch.object(h,'own_hook',return_value=True), patch.object(h.time,'sleep'), patch.object(h.time,'time',side_effect=[0,0,0,60,60]), patch.object(h,'fresh_beat',return_value=False), patch.object(h,'luna',return_value={'appId':h.LG_HOME}), patch.object(h,'recover') as recover:
    h.watch();recover.assert_not_called()
if __name__=='__main__':unittest.main()
