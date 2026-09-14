#!/usr/bin/env python3
"""Freeze owned candidate files and their exact source additions."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

REPORT = Path(__file__).resolve().parent
ROOT = REPORT.parents[3]
SOURCE = ROOT / 'research-candidates/bd_diagonal026/nonzero-level002'
source_manifest = json.loads((REPORT / 'source-manifest.json').read_text())
for item in source_manifest['source_files']:
    actual = hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest()
    assert actual == item['sha256'], item['path']

patch = b''
for path in sorted(SOURCE.glob('*.tex')):
    run = subprocess.run(['git', 'diff', '--no-index', '--binary', '--', '/dev/null',
                          str(path.relative_to(ROOT))], cwd=ROOT, capture_output=True)
    assert run.returncode == 1, run.stderr.decode(errors='replace')
    patch += run.stdout
(REPORT / 'source-additions.patch').write_bytes(patch)

excluded = {REPORT / 'manifest.json', REPORT / 'manifest.sha256',
            REPORT / 'freeze-verification.json'}
paths = sorted(p for directory in (SOURCE, REPORT) for p in directory.rglob('*')
               if p.is_file() and p not in excluded)
entries = [{'path': str(p.relative_to(ROOT)), 'size': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]
aggregate = hashlib.sha256(''.join(item['path'] + '\0' + item['sha256'] + '\n'
                                   for item in entries).encode()).hexdigest()
anchors = {}
for path in sorted(SOURCE.glob('*body.tex')):
    anchors[str(path.relative_to(ROOT))] = {
        match.group(1): number
        for number, line in enumerate(path.read_text().splitlines(), 1)
        for match in re.finditer(r'\\label\{([^}]+)\}', line)}
record = {
    'frozen_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'worktree': str(ROOT),
    'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip(),
    'base_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
    'source_aggregate_sha256': source_manifest['source_aggregate_sha256'],
    'source_diff_sha256': hashlib.sha256(patch).hexdigest(),
    'owned_file_aggregate_sha256': aggregate,
    'files': entries, 'mathematical_anchors': anchors,
    'include': source_manifest['include'],
    'checks': ['/opt/homebrew/bin/python3 reports/research/bd_diagonal026/nonzero-level002/check_exact.py',
               'python3 reports/research/bd_diagonal026/nonzero-level002/build.py'],
    'mathematical_status': 'Constructed and frozen. Independent exact-source acceptance remains pending.',
    'residuals': [
        'The native comparison is on the complement of the two adjacent diagonals.',
        'Both source extensions change cohomology; no source quasi-isomorphism is claimed.',
        'All old mixed images in the all-word native comparison are zero.',
        'The original binary source has no regular coefficient-compatible normal connection commuting with its differential.',
        'Broader source-translation descent, gluing over removed diagonals, and higher compatibility remain unresolved.'],
    'independently_observed_runtime_controls': 'Unverified',
    'git_status': subprocess.check_output(['git', 'status', '--porcelain=v1'], cwd=ROOT, text=True),
    'staged_paths': subprocess.check_output(['git', 'diff', '--cached', '--name-only'], cwd=ROOT, text=True).splitlines(),
    'excluded_self_referential_records': [str(p.relative_to(ROOT)) for p in sorted(excluded)]}
assert not record['staged_paths']
manifest = REPORT / 'manifest.json'
manifest.write_text(json.dumps(record, indent=2) + '\n')
digest = hashlib.sha256(manifest.read_bytes()).hexdigest()
(REPORT / 'manifest.sha256').write_text(digest + '  manifest.json\n')
for item in entries:
    assert hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() == item['sha256']
(REPORT / 'freeze-verification.json').write_text(json.dumps({
    'manifest_sha256': digest, 'verified_file_count': len(entries),
    'source_aggregate_sha256': source_manifest['source_aggregate_sha256'],
    'result': 'All frozen file hashes match. This does not establish mathematical acceptance.'}, indent=2) + '\n')
print('Manifest SHA-256:', digest)
print('Source aggregate:', source_manifest['source_aggregate_sha256'])
print('Source diff:', record['source_diff_sha256'])
print('Verified files:', len(entries))
