from pathlib import Path
import subprocess,os,json,hashlib
root=Path(__file__).resolve().parents[4];s=root/'research-candidates/cbc_native026/candidate003/proof';r=Path(__file__).resolve().parent;b=r/'build';b.mkdir(exist_ok=True)
argv=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-recorder',f'-output-directory={b}','main.tex'];env=dict(os.environ,SOURCE_DATE_EPOCH='1789344000',FORCE_SOURCE_DATE='1')
prev=None;stable=0;rows=[]
for i in range(1,7):
 with (b/f'pass-{i}.txt').open('w') as out:p=subprocess.run(argv,cwd=s,env=env,stdout=out,stderr=subprocess.STDOUT)
 rows.append({'pass':i,'exit':p.returncode});print(rows[-1],flush=True)
 if p.returncode:raise SystemExit(p.returncode)
 h={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in b.glob('*') if p.suffix in ['.aux','.out']};stable=stable+1 if h==prev else 0;prev=h
 if stable>=2:break
log=(b/'main.log').read_text();(r/'build-report.json').write_text(json.dumps({'argv':argv,'passes':rows,'converged':stable>=2,'warnings':[x for x in log.splitlines() if 'Warning' in x or 'Overfull' in x],'pdf_sha256':hashlib.sha256((b/'main.pdf').read_bytes()).hexdigest(),'toolchain':subprocess.check_output(['pdflatex','--version'],text=True),'environment':{k:env[k] for k in ['SOURCE_DATE_EPOCH','FORCE_SOURCE_DATE']}},indent=2)+'\n')
