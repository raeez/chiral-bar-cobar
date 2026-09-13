"""Freeze owned bytes for review. This script performs no Git mutation."""

from pathlib import Path
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FROZEN = HERE / 'frozen-001'
assert not FROZEN.exists(), 'Never overwrite an existing freeze.'
source_paths = ['platonic/chapters/Volume_I_Ordered_Chiral_Geometry.tex',
                'platonic/chapters/ordered_native_collision.tex',
                'platonic/references.bib']
base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT).decode().strip()
branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT).decode().strip()
owned = subprocess.check_output(['git', 'ls-files', '--modified', '--others', '--exclude-standard'], cwd=ROOT).decode().splitlines()
owned = sorted(set(owned))
assert all(p in source_paths or p.startswith('reports/research/MINING-2026-09-13/') for p in owned)
patch = subprocess.check_output(['git', 'diff', '--no-ext-diff', base, '--', source_paths[0], source_paths[2]], cwd=ROOT)
extra = subprocess.run(['git', 'diff', '--no-index', '--', '/dev/null', source_paths[1]], cwd=ROOT, capture_output=True)
assert extra.returncode == 1
patch += extra.stdout
(HERE / 'source.patch').write_bytes(patch)
owned.append(str((HERE / 'source.patch').relative_to(ROOT)))
FROZEN.mkdir()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


entries = []
for relative in owned + ['out/platonic.pdf']:
    if relative.endswith('candidate-manifest.json') or '/frozen-' in relative:
        continue
    path = ROOT / relative
    if not path.is_file():
        continue
    target = FROZEN / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, target)
    entries.append({'path': relative, 'source_path': str(path),
                    'frozen_path': str(target), 'bytes': path.stat().st_size,
                    'sha256': digest(path)})

dependencies = []
for relative in ['Makefile', 'platonic/main.tex', 'platonic/platonic.sty',
                 'platonic/integrated_macros.tex', 'platonic/compat_reconstruction.tex']:
    path = ROOT / relative
    dependencies.append({'path': relative, 'sha256': digest(path), 'base': base})
template = Path('/Users/raeez/latex-template/raeez-math-template.sty')
dependencies.append({'path': str(template), 'sha256': digest(template),
                     'consumer_symlink': 'raeez-math-template.sty -> ../latex-template/raeez-math-template.sty',
                     'resolution': 'TEXINPUTS=/Users/raeez/latex-template:'})

manifest = {
    'candidate': 'vol1-native-collision-001',
    'status': 'frozen for independent review; not accepted',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'principal_repo': '/Users/raeez/chiral-bar-cobar',
    'base_commit': base, 'principal_branch': 'develop',
    'worktree': str(ROOT), 'branch': branch,
    'changed_source_paths': source_paths,
    'aggregate_source_diff_sha256': hashlib.sha256(patch).hexdigest(),
    'files': entries, 'build_dependencies': dependencies,
    'build': {'command': 'TEXINPUTS=/Users/raeez/latex-template: make platonic',
              'entrypoint': 'platonic/main.tex', 'pdf': 'out/platonic.pdf',
              'pages': 603, 'result': '0 errors, 0 undefined references, 0 undefined citations',
              'visual_inspection_physical_pages': [45,46,47,48,49,50,51,53,54,601,602]},
    'calculation': {'command': '/opt/homebrew/bin/python3 reports/research/MINING-2026-09-13/calculations/check_collisions.py',
                    'result': 'all exact finite checks passed'},
    'acceptance_limits': ['Only the declared finite-power differential-module collision and bar/cobar claims are candidates.',
                          'Full Ran descent, punctured-expansion comparison, and identification of the omega-weighted state algebra remain unproved.',
                          'Unmodified book claims and inherited front-matter/metadata defects are not accepted by this regional candidate.',
                          'No staging, commit, push, publication or central accepted-PDF replacement is authorized by this freeze.']}
(HERE / 'candidate-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
for entry in entries:
    assert digest(Path(entry['source_path'])) == entry['sha256']
    assert digest(Path(entry['frozen_path'])) == entry['sha256']
print(json.dumps({'manifest': str(HERE / 'candidate-manifest.json'),
                  'manifest_sha256': digest(HERE / 'candidate-manifest.json'),
                  'source_diff_sha256': manifest['aggregate_source_diff_sha256'],
                  'source_files': [e for e in entries if e['path'] in source_paths],
                  'pdf': next(e for e in entries if e['path'] == 'out/platonic.pdf')}, indent=2))
