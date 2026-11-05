import subprocess,tempfile,unittest
from pathlib import Path
CLI=Path(__file__).resolve().parents[1]/'envfence.py'
class T(unittest.TestCase):
 def test_missing(self):
  with tempfile.TemporaryDirectory()as d:
   p=Path(d);(p/'.env.example').write_text('KNOWN=x\n');(p/'a.py').write_text("os.environ.get('MISSING')\n");r=subprocess.run(['python3',str(CLI),d,'--strict'],text=True,capture_output=True);self.assertEqual(r.returncode,2);self.assertIn('MISSING',r.stdout)
if __name__=='__main__':unittest.main()
