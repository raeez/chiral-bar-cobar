"""Bind frozen source, exact build inputs, calculations, and rendered pages."""
from pathlib import Path
import hashlib
import json
import subprocess

root=Path(__file__).resolve().parents[4]
report=Path(__file__).resolve().parent
source=root/'research-candidates/cbc_native026/candidate007'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((report/'source-manifest.json').read_text())
checks=[]
for row in manifest['source_files']:
    p=root/row['path']
    checks.append({'path':row['path'],'expected':row['sha256'],'actual':sha(p),
                   'match':sha(p)==row['sha256']})
assert all(row['match'] for row in checks)
(report/'source-verification.json').write_text(json.dumps(checks,indent=2)+'\n')

objects=report/'tex-inputs'
objects.mkdir(exist_ok=True)
closure=[]
for kind,entry in [('native','main'),('proof','comparison_main'),('subregular','subregular_main')]:
    cwd=source/('cbc' if kind=='native' else 'proof')
    out=report/('build-'+kind)
    build=json.loads((report/(kind+'-build.json')).read_text())
    assert build['converged'] and all(r['exit']==0 for r in build['passes'])
    paths=set()
    for line in (out/(entry+'.fls')).read_text().splitlines():
        if line.startswith('INPUT '):
            p=Path(line[6:]);p=p if p.is_absolute() else cwd/p
            paths.add(p.resolve())
    rows=[]
    for p in sorted(paths):
        if not p.is_file():
            rows.append({'path':str(p),'regular_file':False,'exists':p.exists()})
            continue
        digest=sha(p);obj=objects/digest
        if not obj.exists():obj.write_bytes(p.read_bytes())
        rows.append({'path':str(p),'regular_file':True,'sha256':digest,
                     'object':str(obj.relative_to(root))})
    pdf=out/(entry+'.pdf')
    info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
    pagecount=int(next(x.split(':',1)[1].strip() for x in info.splitlines() if x.startswith('Pages:')))
    closure.append({'kind':kind,'cwd':str(cwd),'entrypoint':entry+'.tex',
                    'pdf':str(pdf.relative_to(root)),'pdf_sha256':sha(pdf),
                    'pages':pagecount,'recorded_inputs':rows,
                    'build_record_sha256':sha(report/(kind+'-build.json'))})
(report/'build-input-closure.json').write_text(json.dumps(closure,indent=2)+'\n')

renders=[]
for p in sorted(report.glob('render-*/*.png')):
    renders.append({'path':str(p.relative_to(root)),'sha256':sha(p)})
(report/'render-binding.json').write_text(json.dumps({'pdfs':[{k:r[k] for k in ['kind','pdf','pdf_sha256','pages']} for r in closure],
    'rasters':renders,'inspection_scope':'All fourteen standalone pages, focused pages 45–59, and all listed final native integration pages. Earlier native rasters are retained separately and compared by hash. No whole-native mathematical or firewall acceptance.'},indent=2)+'\n')

files=[]
for base in [source,report]:
    for p in sorted(base.rglob('*')):
        if p.is_file() and p.name!='final-manifest.json' and '__pycache__' not in p.parts:
            files.append({'path':str(p.relative_to(root)),'sha256':sha(p)})
(report/'final-manifest.json').write_text(json.dumps({'source_manifest_sha256':sha(report/'source-manifest.json'),
    'mathematical_status':'Subregular quotient/bar/module constructions and connected repairs await fresh independent review; whole native union remains unaccepted.',
    'files':files},indent=2)+'\n')
print(json.dumps({'source_manifest':sha(report/'source-manifest.json'),'final_manifest':sha(report/'final-manifest.json'),
    'files':len(files),'tex_input_objects':len(list(objects.iterdir())),
    'pdfs':[{k:r[k] for k in ['kind','pdf_sha256','pages']} for r in closure]},indent=2))
