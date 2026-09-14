from pathlib import Path
import subprocess, hashlib, json, os, sys, time, re
root=Path(__file__).resolve().parents[4]
kind=sys.argv[1]
source=root/'research-candidates/cbc_native026/candidate002'/('cbc' if kind=='native' else 'proof')
entry='main.tex' if kind=='native' else 'comparison_main.tex'
stem=Path(entry).stem
out=root/'reports/research/cbc_native026/candidate002'/('build-'+kind)
out.mkdir(parents=True,exist_ok=True)
for p in source.rglob('*.tex'):(out/p.relative_to(source).parent).mkdir(parents=True,exist_ok=True)
argv=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','-cnf-line=buf_size=1000000',f'-output-directory={out}',entry]
env=dict(os.environ,SOURCE_DATE_EPOCH='1789344000',FORCE_SOURCE_DATE='1')
rows=[];prev=None;stable=0
for i in range(1,7):
    start=time.time()
    with (out/f'pass-{i}.stdout.log').open('w') as log:
        proc=subprocess.run(argv,cwd=source,env=env,stdout=log,stderr=subprocess.STDOUT)
    hashes={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.rglob('*')) if p.suffix in ('.aux','.toc','.out')}
    rows.append({'pass':i,'exit':proc.returncode,'seconds':round(time.time()-start,2),'auxiliary_hashes':hashes})
    print(kind,i,'exit',proc.returncode,flush=True)
    if proc.returncode:break
    stable=stable+1 if hashes==prev else 0
    if stable>=2:break
    prev=hashes
log=(out/(stem+'.log')).read_text(errors='replace')
pdf=out/(stem+'.pdf')
report={'source':str(source/entry),'argv':argv,'passes':rows,'converged':stable>=2,'warnings':[x for x in log.splitlines() if re.search('undefined|Overfull|multiply defined|Label.*changed|rerunfilecheck Warning',x)],'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.exists() else None,'toolchain':subprocess.run(['pdflatex','--version'],capture_output=True,text=True).stdout,'environment':{'SOURCE_DATE_EPOCH':env['SOURCE_DATE_EPOCH'],'FORCE_SOURCE_DATE':'1'}}
(out.parent/(kind+'-build.json')).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'converged':report['converged'],'warnings':report['warnings'][:20]}),flush=True)
if rows[-1]['exit'] or not report['converged']:sys.exit(1)
