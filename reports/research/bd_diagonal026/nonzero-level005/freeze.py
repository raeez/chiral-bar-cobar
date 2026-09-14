#!/usr/bin/env python3
"""Freeze the four-input source and its immutable mathematical dependency."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

REPORT=Path(__file__).resolve().parent
ROOT=REPORT.parents[3]
SOURCE=ROOT/'research-candidates/bd_diagonal026/nonzero-level005'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


build=json.loads((REPORT/'build-record.json').read_text())
assert build['diagnostics']==[]
for path,expected in build['recorder_inputs'].items():
    assert digest(Path(path))==expected,path
assert digest(REPORT/'build/four-input-source.pdf')==build['pdf_sha256']
checks=json.loads((REPORT/'exact-checks.json').read_text())
assert checks['result']=='passed'
visual=json.loads((REPORT/'visual-inspection.json').read_text())
assert visual['result']=='passed' and visual['pdf_sha256']==build['pdf_sha256']
page_count=int(re.search(r'^Pages:\s+(\d+)',build['pdfinfo'],re.M).group(1))
assert len(visual['pages'])==page_count
for item in visual['pages']:
    assert digest(ROOT/item['path'])==item['sha256']
inputs=json.loads((REPORT/'input-freeze.json').read_text())
for item in inputs['mathematical_inputs']:
    assert digest(ROOT/item['path'])==item['sha256']
old=json.loads((ROOT/'reports/research/bd_diagonal026/nonzero-level004/manifest.json').read_text())
for item in old['files']:
    assert digest(ROOT/item['path'])==item['sha256'],item['path']

owned_sources=[{'path':str(p.relative_to(ROOT)),'sha256':digest(p)} for p in sorted(SOURCE.glob('*.tex'))]
dependencies=[{'path':p,'sha256':digest(ROOT/p)} for p in inputs['native_include_dependencies']]
all_sources=sorted(owned_sources+dependencies,key=lambda x:x['path'])
source_aggregate=hashlib.sha256(''.join(x['path']+'\0'+x['sha256']+'\n' for x in all_sources).encode()).hexdigest()
for item in all_sources:
    source=(ROOT/item['path']).read_text()
    assert not re.search(r'\b(?:agent|archive|audit|worktree|manifest|TODO|pipeline|candidate|acceptance)\b',source,re.I),item['path']
(REPORT/'source-manifest.json').write_text(json.dumps({
    'owned_source_files':owned_sources,'immutable_dependencies':dependencies,
    'source_aggregate_sha256':source_aggregate,
    'native_include':str((SOURCE/'four-input-body.tex').relative_to(ROOT)),
    'required_preceding_include':inputs['native_include_dependencies'][0],
    'bibliography_key':'BDtranslated'},indent=2)+'\n')

patch=b''
for path in sorted(SOURCE.glob('*.tex')):
    run=subprocess.run(['git','diff','--no-index','--binary','--','/dev/null',str(path.relative_to(ROOT))],cwd=ROOT,capture_output=True)
    assert run.returncode==1,run.stderr.decode(errors='replace')
    patch+=run.stdout
(REPORT/'source-additions.patch').write_bytes(patch)
excluded={REPORT/'manifest.json',REPORT/'manifest.sha256',REPORT/'freeze-verification.json'}
paths=sorted(p for folder in (SOURCE,REPORT) for p in folder.rglob('*') if p.is_file() and p not in excluded)
files=[{'path':str(p.relative_to(ROOT)),'sha256':digest(p),'size':p.stat().st_size} for p in paths]
aggregate=hashlib.sha256(''.join(x['path']+'\0'+x['sha256']+'\n' for x in files).encode()).hexdigest()
anchors={}
for item in all_sources:
    path=ROOT/item['path']
    anchors[item['path']]={m.group(1):n for n,line in enumerate(path.read_text().splitlines(),1)
                          for m in re.finditer(r'\\label\{([^}]+)\}',line)}
staged=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
assert not staged
record={
    'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'worktree':str(ROOT),'branch':inputs['branch'],'base_head':inputs['base_commit'],
    'source_aggregate_sha256':source_aggregate,'source_diff_sha256':hashlib.sha256(patch).hexdigest(),
    'owned_file_aggregate_sha256':aggregate,'files':files,'mathematical_anchors':anchors,
    'immutable_mathematical_dependencies':dependencies,'pdf_sha256':build['pdf_sha256'],'pages':page_count,
    'native_include':str((SOURCE/'four-input-body.tex').relative_to(ROOT)),
    'acceptance_boundary':'All global four-input coefficient cochain maps, all fifteen partition types, actual input translations, fixed nonzero level, and permutation equivariance. Explicit relative cohomology. Sectorwise 3+1 and 1+3 factorization cuts; exact strict 2+2 and all-word coproduct obstructions.',
    'mathematical_status':'Constructed and locally verified. Fresh independent review of the exact dependency and new source remains required.',
    'residual_obligations':['Native integration-candidate review.','A source or coproduct repair resolving the stated strict deconcatenation obstructions.','All-arity coherence after such a repair.','No minimality claim for the chosen four-input added complex.'],
    'runtime_controls':{'required':{'model':'gpt-6-astra','reasoning_effort':'ultra'},'coordinator_report':'Matching metadata verified for the resumed assignment.','direct_local_observation':'Not exposed.'},
    'commands':['/opt/homebrew/bin/python3 reports/research/bd_diagonal026/nonzero-level005/check_exact.py','python3 reports/research/bd_diagonal026/nonzero-level005/build.py','python3 reports/research/bd_diagonal026/nonzero-level005/freeze.py'],
    'preserved004_files':len(old['files']),'staged_paths':staged,
    'git_status':subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
    'excluded_self_referential_records':[str(p.relative_to(ROOT)) for p in sorted(excluded)]}
(REPORT/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
manifest_hash=digest(REPORT/'manifest.json')
(REPORT/'manifest.sha256').write_text(manifest_hash+'  manifest.json\n')
for item in files:
    assert digest(ROOT/item['path'])==item['sha256'],item['path']
(REPORT/'freeze-verification.json').write_text(json.dumps({
    'result':'passed','manifest_sha256':manifest_hash,'verified_owned_file_count':len(files),
    'source_aggregate_sha256':source_aggregate,'pdf_sha256':build['pdf_sha256'],
    'limit':'Hash agreement and local checks do not establish independent mathematical acceptance.'},indent=2)+'\n')
print(json.dumps({'manifest':manifest_hash,'source_aggregate':source_aggregate,
                  'source_diff':record['source_diff_sha256'],'pdf':build['pdf_sha256'],
                  'pages':page_count,'owned_files':len(files)},indent=2))
