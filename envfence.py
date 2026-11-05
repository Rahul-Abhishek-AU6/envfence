#!/usr/bin/env python3
import argparse,re
from pathlib import Path
PAT=re.compile(r"(?:os\.environ(?:\.get)?|process\.env)\s*[\[(]\s*['\"]([A-Z][A-Z0-9_]+)")
def main():
 a=argparse.ArgumentParser();a.add_argument('root',type=Path);a.add_argument('--strict',action='store_true');x=a.parse_args();r=x.root
 sample=r/'.env.example'; documented={q.split('=',1)[0] for q in sample.read_text().splitlines() if '=' in q and not q.startswith('#')} if sample.exists() else set();used=set()
 for p in r.rglob('*'):
  if p.is_file() and p.suffix in {'.py','.js','.ts'}:
   try:used|=set(PAT.findall(p.read_text()))
   except UnicodeDecodeError:pass
 missing=sorted(used-documented);stale=sorted(documented-used)
 print('# EnvFence receipt');print('- Source variables:',len(used));print('- Missing from .env.example:',', '.join(missing)or'none');print('- Unreferenced documented variables:',', '.join(stale)or'none')
 return 2 if x.strict and missing else 0
if __name__=='__main__':raise SystemExit(main())
