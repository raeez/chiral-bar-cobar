"""Preserve exact discovery sources and public records without executing them."""

from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
REC = Path('/Users/raeez/mathematics/worktrees/frontier-recovery-astra-ultra-20260913')
REPORT = REC / 'reports/research/RECOVERY-2026-09-13'
RAW = HERE / 'materials/raw'
RAW.mkdir(parents=True, exist_ok=True)
rx = re.compile(r'order.chart|ordered.collisio|ordered.coefficient|merged.state|Thom.Sullivan', re.I)
sources = []
by_hash = {}


def preserve(path, scope):
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    destination = RAW / (sha[:20] + path.suffix)
    if destination.exists():
        assert destination.read_bytes() == data
    else:
        destination.write_bytes(data)
    text = data.decode('utf8', errors='replace')
    hits = [i for i, line in enumerate(text.splitlines(), 1) if rx.search(line)]
    row = {'source': str(path), 'sha256': sha, 'bytes': len(data),
           'preserved': str(destination.relative_to(HERE)),
           'scope': scope, 'matching_line_anchors': hits}
    if sha in by_hash:
        row['disposition'] = 'duplicate'
        row['duplicate_of'] = by_hash[sha]
    else:
        by_hash[sha] = str(path)
        row['disposition'] = 'pending'
    sources.append(row)
    return row


names = ['ordered_chiral_substance-final-01.md', 'collision_bar_exact_review-final-01.md',
         'bar_chapter_exact_review-final-01.md', 'bar_chapter_exact_review-final-02.md',
         'recovery_bar_construction-final-01.md', 'critique_g01--p004-final-01.md',
         'critique_g01--p005-final-01.md', 'critique_g01--p006-final-01.md',
         'critique_g01--p011-final-01.md', 'critique_g01--p012-final-01.md',
         'semantic_wave_reconcile-final-01.md']
for name in names:
    path = REPORT / 'returns' / name
    if path.exists():
        preserve(path, 'Retained complete return; statement-level dispositions below control use.')

# Preserve distinct intermediate versions, including rejected candidates.
for folder in [REC / 'manuscript', REPORT / 'candidates']:
    for path in sorted(folder.rglob('*')):
        if path.is_file() and path.suffix in ('.tex', '.md') and any(
            word in path.name for word in ('ordered-coefficient-bar', 'ordered-collisions-and-residues', 'ordered_chiral_substance')):
            preserve(path, 'Complete intermediate source version; hash identity controls deduplication.')

catalogue = Path('/Users/raeez/mathematics/worktrees/frontier-catalogue-20260913/reports/research/COVERAGE-2026-09-13/semantic/documents')
for sha in ['c78745d9a966c927739a49f3b22192c389065372a24de6990b6e58355e9bc75d',
            'ebc8bb469caa65b9042f8361e2d94043a2058141da1a1e1b23e85cbd51c34db0']:
    path = catalogue / sha[:2] / (sha + '.txt')
    row = preserve(path, 'Untrusted extracted manuscript; complete bytes retained, only declared ranges used.')
    assert row['sha256'] == sha

# Index additional relevant returns without falsely claiming full reading.
known = {row['source'] for row in sources}
for path in sorted((REPORT / 'returns').glob('*.md')):
    if str(path) not in known and rx.search(path.read_text()):
        preserve(path, 'Discovery match retained; complete mathematical adjudication remains pending.')

# Public intermediate outputs from the directly relevant proof sessions.
# Analysis-channel messages and reasoning objects are never selected.
manifest = json.loads((REPORT / 'returns-manifest-049.json').read_text())
sessions = {}
for row in manifest['entries']:
    if Path(row['path']).name in names:
        sessions[row['source']] = row['task']
public = []
for filename, task in sessions.items():
    path = Path(filename)
    selected = []
    for lineno, raw_line in enumerate(path.read_bytes().splitlines(keepends=True), 1):
        try:
            row = json.loads(raw_line)
        except json.JSONDecodeError:
            continue
        if row.get('type') != 'response_item':
            continue
        payload = row.get('payload', {})
        kind = payload.get('type')
        visible = (kind == 'message' and payload.get('role') == 'assistant'
                   and payload.get('channel') in ('final', 'commentary'))
        visible = visible or kind in ('function_call_output', 'custom_tool_call_output')
        if not visible:
            continue
        serialized = json.dumps(payload, ensure_ascii=False)
        if not rx.search(serialized):
            continue
        sha = hashlib.sha256(raw_line).hexdigest()
        selected.append(raw_line)
        public.append({'source': filename, 'line': lineno, 'sha256': sha,
                       'record_type': kind, 'task': task,
                       'disposition': 'pending',
                       'obligation': 'Preserved public intermediate exposure; compare exact mathematical content with the integrated proofs. No private reasoning inferred.'})
    if selected:
        data = b''.join(selected)
        sha = hashlib.sha256(data).hexdigest()
        dest = RAW / (sha[:20] + '-public.jsonl')
        dest.write_bytes(data)
        for record in public:
            if record['source'] == filename:
                record['preserved'] = str(dest.relative_to(HERE))

inventory = {'created_utc': datetime.now(timezone.utc).isoformat(),
             'source_policy': 'All retained and extracted material is discovery evidence. Exact manuscript proofs and explicit calculations establish the candidate claims.',
             'sources': sources, 'public_fragments': public,
             'limits': ['Additional discovery matches remain explicitly pending.',
                        'No analysis-channel or private reasoning records were preserved or reconstructed.',
                        'No archived source code was executed.']}
(HERE / 'source-inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')
print(json.dumps({'source_occurrences':len(sources), 'distinct_source_hashes':len(by_hash), 'public_fragments':len(public)}))
