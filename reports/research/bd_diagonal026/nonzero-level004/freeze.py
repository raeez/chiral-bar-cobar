#!/usr/bin/env python3
"""Freeze the owned source, input closure, and verification evidence."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

REPORT = Path(__file__).resolve().parent
ROOT = REPORT.parents[3]
SOURCE = ROOT/'research-candidates/bd_diagonal026/nonzero-level004'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


build = json.loads((REPORT/'build-record.json').read_text())
assert build['diagnostics'] == []
for name, expected in build['recorder_inputs'].items():
    assert digest(Path(name)) == expected, name
assert digest(REPORT/'build/translated-source.pdf') == build['pdf_sha256']
checks = json.loads((REPORT/'exact-checks.json').read_text())
assert checks['result'] == 'passed'
visual = json.loads((REPORT/'visual-inspection.json').read_text())
assert visual['pdf_sha256'] == build['pdf_sha256']
assert visual['result'] == 'passed'
for item in visual['pages']:
    assert digest(ROOT/item['path']) == item['sha256']
inputs = json.loads((REPORT/'input-freeze.json').read_text())
for item in inputs['mathematical_inputs']:
    assert digest(ROOT/item['path']) == item['sha256']

source_files = [{'path':str(p.relative_to(ROOT)), 'sha256':digest(p)}
                for p in sorted(SOURCE.glob('*.tex'))]
source_aggregate = hashlib.sha256(''.join(x['path']+'\0'+x['sha256']+'\n'
                                        for x in source_files).encode()).hexdigest()
(REPORT/'source-manifest.json').write_text(json.dumps({
    'source_files':source_files, 'source_aggregate_sha256':source_aggregate,
    'include':str((SOURCE/'translated-source-body.tex').relative_to(ROOT)),
    'bibliography_key':'BDtranslated'}, indent=2)+'\n')
patch = b''
for path in sorted(SOURCE.glob('*.tex')):
    run = subprocess.run(['git','diff','--no-index','--binary','--','/dev/null',
                          str(path.relative_to(ROOT))],cwd=ROOT,capture_output=True)
    assert run.returncode == 1, run.stderr.decode(errors='replace')
    patch += run.stdout
(REPORT/'source-additions.patch').write_bytes(patch)

excluded = {REPORT/'manifest.json',REPORT/'manifest.sha256',REPORT/'freeze-verification.json'}
paths = sorted(p for directory in (SOURCE,REPORT) for p in directory.rglob('*')
               if p.is_file() and p not in excluded)
files = [{'path':str(p.relative_to(ROOT)),'sha256':digest(p),'size':p.stat().st_size}
         for p in paths]
aggregate = hashlib.sha256(''.join(x['path']+'\0'+x['sha256']+'\n'
                                   for x in files).encode()).hexdigest()
anchors = {}
for path in SOURCE.glob('*body.tex'):
    anchors[str(path.relative_to(ROOT))] = {
        match.group(1):number for number,line in enumerate(path.read_text().splitlines(),1)
        for match in re.finditer(r'\\label\{([^}]+)\}',line)}
staged = subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
assert not staged
record = {
    'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'worktree':str(ROOT),'branch':inputs['branch'],'base_head':inputs['base_commit'],
    'source_aggregate_sha256':source_aggregate,
    'source_diff_sha256':hashlib.sha256(patch).hexdigest(),
    'owned_file_aggregate_sha256':aggregate,'files':files,'mathematical_anchors':anchors,
    'pdf_sha256':build['pdf_sha256'],'pages':12,
    'native_include':str((SOURCE/'translated-source-body.tex').relative_to(ROOT)),
    'acceptance_boundary':'Global binary and ternary native cochain maps on actual global coefficients and all finite input jets; regular four-current collision subcomplex only.',
    'mathematical_status':'Constructed and locally verified. Fresh independent review of these exact bytes remains required.',
    'residual_obligations':['Full four-input coefficient comparison.','All higher partition operations.','Ordered-surjection and deconcatenation identities.','All-arity bar or coalgebra comparison.','Separate native integration-candidate review.'],
    'runtime_controls':{'required':{'model':'gpt-6-astra','reasoning_effort':'ultra'},'observed':'unverified'},
    'commands':['/opt/homebrew/bin/python3 reports/research/bd_diagonal026/nonzero-level004/check_exact.py','python3 reports/research/bd_diagonal026/nonzero-level004/build.py','python3 reports/research/bd_diagonal026/nonzero-level004/freeze.py'],
    'staged_paths':staged,'git_status':subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
    'excluded_self_referential_records':[str(p.relative_to(ROOT)) for p in sorted(excluded)]}
(REPORT/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
manifest_hash = digest(REPORT/'manifest.json')
(REPORT/'manifest.sha256').write_text(manifest_hash+'  manifest.json\n')
for item in files:
    assert digest(ROOT/item['path']) == item['sha256'], item['path']
(REPORT/'freeze-verification.json').write_text(json.dumps({
    'result':'passed','manifest_sha256':manifest_hash,'verified_file_count':len(files),
    'source_aggregate_sha256':source_aggregate,'pdf_sha256':build['pdf_sha256'],
    'limit':'Hash agreement and local checks do not establish independent mathematical acceptance.'},indent=2)+'\n')
print(json.dumps({'manifest':manifest_hash,'source_aggregate':source_aggregate,
                  'source_diff':record['source_diff_sha256'],'files':len(files),
                  'pdf':build['pdf_sha256']},indent=2))
