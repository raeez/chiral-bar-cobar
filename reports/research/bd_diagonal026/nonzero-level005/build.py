#!/usr/bin/env python3
"""Build the assigned mathematical source and retain exact diagnostics."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess

REPORT = Path(__file__).resolve().parent
ROOT = REPORT.parents[3]
SOURCE = ROOT / 'research-candidates/bd_diagonal026/nonzero-level005'
BUILD = REPORT / 'build'
BUILD.mkdir(exist_ok=True)
env = dict(os.environ)
env['SOURCE_DATE_EPOCH'] = '1789344000'
env['FORCE_SOURCE_DATE'] = '1'
env['TEXINPUTS'] = '/Users/raeez/latex-template:' + env.get('TEXINPUTS', '')
command = ['/Library/TeX/texbin/pdflatex', '-no-shell-escape', '-halt-on-error',
           '-interaction=nonstopmode', '-file-line-error', '-recorder',
           f'-output-directory={BUILD}', 'four-input-source.tex']
passes = []
previous = None
for number in range(1, 6):
    run = subprocess.run(command, cwd=SOURCE, env=env, capture_output=True)
    raw = run.stdout + run.stderr
    (BUILD / f'pass-{number}.stdout.bin').write_bytes(raw)
    (BUILD / f'pass-{number}.stdout.log').write_text(raw.decode('utf-8', 'replace'))
    state = b''.join((BUILD / f'four-input-source.{suffix}').read_bytes()
                     for suffix in ('aux', 'toc', 'out')
                     if (BUILD / f'four-input-source.{suffix}').exists())
    digest = hashlib.sha256(state).hexdigest()
    passes.append({'number': number, 'exit_code': run.returncode,
                   'auxiliary_sha256': digest})
    if run.returncode:
        print(raw.decode('utf-8', 'replace')[-14000:])
        raise SystemExit(run.returncode)
    if number > 1 and digest == previous:
        break
    previous = digest
else:
    raise RuntimeError('Auxiliary state did not stabilize.')

log = (BUILD / 'four-input-source.log').read_text(errors='replace')
diagnostics = re.findall(r'^.*(?:undefined|multiply defined|Overfull|^!).*$', log, re.M)
pdf = BUILD / 'four-input-source.pdf'
subprocess.run(['/opt/homebrew/bin/pdftotext', '-layout', str(pdf),
                str(BUILD / 'four-input-source.txt')], check=True)
info = subprocess.run(['/opt/homebrew/bin/pdfinfo', str(pdf)],
                      capture_output=True, text=True, check=True).stdout
(BUILD / 'pdfinfo.txt').write_text(info)
inputs = {}
for line in (BUILD / 'four-input-source.fls').read_text().splitlines():
    if not line.startswith('INPUT '):
        continue
    path = Path(line[6:])
    if not path.is_absolute():
        path = SOURCE / path
    path = path.resolve()
    if path.is_file() and BUILD not in path.parents:
        inputs[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
record = {'command': command, 'cwd': str(SOURCE),
          'environment': {key: env[key] for key in
                          ('SOURCE_DATE_EPOCH', 'FORCE_SOURCE_DATE', 'TEXINPUTS')},
          'passes': passes, 'diagnostics': diagnostics,
          'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
          'pdfinfo': info, 'recorder_inputs': inputs,
          'pdflatex_version': subprocess.check_output([command[0], '--version'], text=True),
          'mathematical_acceptance': 'Independent exact-source review remains required.'}
(REPORT / 'build-record.json').write_text(json.dumps(record, indent=2) + '\n')
print(info)
print('Diagnostics:', diagnostics)
print('PDF SHA-256:', record['pdf_sha256'])
if diagnostics:
    raise SystemExit(1)
