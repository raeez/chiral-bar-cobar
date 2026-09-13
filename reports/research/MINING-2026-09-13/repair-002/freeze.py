"""Freeze candidate 002 while preserving every byte of candidate 001."""

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

REPAIR = Path(__file__).resolve().parent
REPORT = REPAIR.parent
ROOT = REPORT.parents[2]
FROZEN = REPORT / 'frozen-002'
assert not FROZEN.exists(), 'Do not overwrite a prior freeze.'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


old_manifest = REPORT / 'candidate-manifest.json'
assert sha(old_manifest) == '15421b8281971f004e49ffd6b2f9eb078a77df88977d2ef12b7ff6fc1991d9d6'
old = json.loads(old_manifest.read_text())
for entry in old['files']:
    assert sha(Path(entry['frozen_path'])) == entry['sha256']

base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip()
assert base == old['base_commit']
sources = old['changed_source_paths']
chapter = 'platonic/chapters/ordered_native_collision.tex'
for name in sources:
    if name != chapter:
        prior = next(e for e in old['files'] if e['path'] == name)
        assert sha(ROOT / name) == prior['sha256']

before = (REPORT / 'frozen-001' / chapter).read_bytes()
after = (ROOT / chapter).read_bytes()
prefix_marker = b'Dual collision maps are defined weight by weight'
suffix_marker = b'\\Needspace{16\\baselineskip}\n\\begin{proposition}[Completed reconstruction and collision]'
prefix = before[:before.index(prefix_marker)]
suffix = before[before.index(suffix_marker):]
assert after.startswith(prefix)
assert after.endswith(suffix)

aggregate = subprocess.check_output(['git', 'diff', '--no-ext-diff', base, '--', sources[0], sources[2]], cwd=ROOT)
extra = subprocess.run(['git', 'diff', '--no-index', '--', '/dev/null', chapter], cwd=ROOT, capture_output=True)
assert extra.returncode == 1
aggregate += extra.stdout
(REPAIR / 'aggregate-source.patch').write_bytes(aggregate)

owned = subprocess.check_output(['git', 'ls-files', '--modified', '--others', '--exclude-standard'], cwd=ROOT).decode().splitlines()
paths = set(owned)
paths.update(str(p.relative_to(ROOT)) for p in REPAIR.rglob('*') if p.is_file())
paths.add('out/platonic.pdf')
entries = []
FROZEN.mkdir()
for relative in sorted(paths):
    if '/frozen-' in relative or Path(relative).name.startswith('candidate-manifest'):
        continue
    assert relative in sources or relative == 'out/platonic.pdf' or relative.startswith('reports/research/MINING-2026-09-13/')
    path = ROOT / relative
    if not path.is_file():
        continue
    target = FROZEN / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, target)
    entries.append({'path': relative, 'source_path': str(path),
                    'frozen_path': str(target), 'bytes': path.stat().st_size,
                    'sha256': sha(path)})

dependencies = old['build_dependencies']
for entry in dependencies:
    path = Path(entry['path'])
    if not path.is_absolute():
        path = ROOT / path
    assert sha(path) == entry['sha256']

manifest = {
    'candidate': 'vol1-native-collision-002',
    'status': 'frozen for renewed independent review; not accepted',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'previous_candidate': {'manifest': str(old_manifest), 'sha256': sha(old_manifest),
                           'verdict': 'BLOCK: dual collision coefficient extension was not stated'},
    'base_commit': base, 'principal_repo': '/Users/raeez/chiral-bar-cobar',
    'worktree': str(ROOT), 'branch': old['branch'],
    'changed_source_paths': sources,
    'manuscript_changes_since_001': [chapter],
    'aggregate_source_diff_sha256': hashlib.sha256(aggregate).hexdigest(),
    'repair_diff': {'path': str(REPAIR / 'source-repair.patch'),
                    'sha256': sha(REPAIR / 'source-repair.patch')},
    'unchanged_mathematical_regions': {
        'prefix_bytes': len(prefix), 'prefix_sha256': hashlib.sha256(prefix).hexdigest(),
        'suffix_bytes': len(suffix), 'suffix_sha256': hashlib.sha256(suffix).hexdigest(),
        'verification': 'Current chapter has the exact001 prefix before the repaired assertion and the exact001 suffix beginning at the cobar proposition.'},
    'files': entries, 'build_dependencies': dependencies,
    'build': {'command': 'TEXINPUTS=/Users/raeez/latex-template: make platonic',
              'entrypoint': 'platonic/main.tex', 'pdf': 'out/platonic.pdf', 'pages': 603,
              'result': '0 errors, 0 undefined references, 0 undefined citations',
              'visual_inspection_physical_pages': [49,50,51,52,53,54],
              'current_render_directory': str(REPAIR / 'render')},
    'calculation': {'command': '/opt/homebrew/bin/python3 reports/research/MINING-2026-09-13/repair-002/check_dual_collision.py',
                    'result': 'all exact targeted checks passed'},
    'repair_claims': ['Typed finite-weight dual map after extension from Ldelta_p^*C_I to C_J.',
                      'Finite-semifree dual/base-change comparison with the differential and connection.',
                      'Convolution, degreewise weight completion and nested composition.',
                      'Binary idempotent obstruction to a unital unextended reverse map.'],
    'acceptance_limits': old['acceptance_limits'],
    'old_freeze_verification': 'All88 frozen001 entries and its manifest remain unchanged.'}
path = REPORT / 'candidate-manifest-002.json'
path.write_text(json.dumps(manifest, indent=2) + '\n')
for entry in entries:
    assert sha(Path(entry['source_path'])) == entry['sha256']
    assert sha(Path(entry['frozen_path'])) == entry['sha256']
for entry in old['files']:
    assert sha(Path(entry['frozen_path'])) == entry['sha256']
print(json.dumps({'manifest': str(path), 'manifest_sha256': sha(path),
                  'source': next(e for e in entries if e['path'] == chapter),
                  'pdf': next(e for e in entries if e['path'] == 'out/platonic.pdf'),
                  'aggregate_source_diff_sha256': manifest['aggregate_source_diff_sha256'],
                  'frozen_files': len(entries)}, indent=2))
