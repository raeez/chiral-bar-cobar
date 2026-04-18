# Attack-heal: AP236 cleanup sweep (Vol I)

Date: 2026-04-18
Author: Raeez Lorgat
Scope: Vol I `chapters/`, `standalone/`, `appendices/`
Mission: AP236 forbidden-token sweep per Manuscript Metadata Hygiene (CLAUDE.md CONSTITUTIONAL).

## Phase 1: Attack / census

Ran the AP236 pre-commit gate regex:

```
grep -rn '\bAP[0-9]\+\b\|\bHZ-[0-9IVX]\+\b\|V[0-9]-AP[0-9]\+\|AP-CY[0-9]\+\|\bPattern [0-9]\+\b\|Cache #[0-9]\+\|first_principles_cache' \
  chapters/ standalone/ 2>/dev/null | grep -v ':[0-9]*:\s*%' | grep -v 'HZ-IV'
```

Findings (typeset prose only, excluding `%` comments and HZ-IV):

- 4 instances of forbidden `\ap{N}` macro tokens in `chapters/examples/bar_complex_tables.tex`
  (lines 4136, 4172, 4187, 4207). Macro is NOT defined anywhere in the programme
  (`grep -rn 'newcommand.*\\ap\b\|providecommand.*\\ap\b\|DeclareRobustCommand.*\\ap\b' /Users/raeez/chiral-bar-cobar/`
  returns zero hits); tokens would render as undefined control sequences or literal
  slugs in the compiled PDF. The slugs are cross-references to AP62 and AP63
  (generating-function content tied to Orlik-Solomon form factor; chiral bar
  cohomology vs Chevalley-Eilenberg resolution).

- 6 instances of `; AP255` slug embedded inside `\detokenize{...}` blocks in
  `standalone/theorem_index.tex` (lines 2379, 2382, 2389, 2390, 2391, 2392),
  attached to PHANTOM FILE warnings. `\detokenize{...}` renders the text
  verbatim to the PDF; this is a direct typeset-prose violation.

No other Vol I typeset-prose hits on `AP\d+`, `HZ-\d+` (except allowed HZ-IV),
`V\d-AP\d+`, `AP-CY\d+`, `FM\d+`, `B\d+` (as blacklist slug), `Pattern \d+`,
`Cache #\d+`, or `first_principles_cache`.

## Phase 2: Heal

Applied AP236 healing protocol (a) parenthetical slug removal / (c) prose
rephrase-to-mathematical-content:

### Heal 1: bar_complex_tables.tex:4136 (AP63 reference)

Before:
```
$\dim H^2 = 5$, \emph{not} $6$ (\ap{63}): the chiral bar complex
departs from the Chevalley-Eilenberg count on the negative
subalgebra, and the standard Riordan recursion fails.
```
After:
```
$\dim H^2 = 5$, \emph{not} $6$: the chiral bar complex
departs from the Chevalley-Eilenberg count on the negative
subalgebra, because the chiral OPE introduces an Orlik-Solomon form
factor absent from the Lie-algebraic resolution, and the standard
Riordan recursion fails.
```
Rationale: AP63 mathematical content (Orlik-Solomon form factor) inscribed
inline; slug removed.

### Heal 2: bar_complex_tables.tex:4172 (table cell AP63 reference)

Before: `$H^2 = 5$ (not $6$; \ap{63}) &`
After: `$H^2 = 5$ (not $6$) &`
Rationale: parenthetical slug in tabular cell; the surrounding caption now
carries the full mathematical explanation (Heal 3), so redundant slug removed.

### Heal 3: bar_complex_tables.tex:4187 (table caption AP63 reference)

Before:
```
...the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.
```
After:
```
...the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; the departure is the Orlik-Solomon form factor of the chiral OPE, detailed in Section~\ref{sec:sl3-bar-table}.
```
Rationale: caption now names the mathematical mechanism (Orlik-Solomon form
factor) rather than pointing to a catalogue index; reader gets the content,
not the scaffolding label.

### Heal 4: bar_complex_tables.tex:4207 (remark-body AP62 reference)

Before:
```
question. \ap{62}: the generating functions here record full graded
dimensions, not Euler characteristics; individual bar cohomology
dimensions depend on the full OPE bracket and are not reconstructible
from $\dim \mathfrak{g}$ alone.
```
After:
```
question. We emphasise: the generating functions here record full
graded dimensions, not Euler characteristics; individual bar
cohomology dimensions depend on the full OPE bracket and are not
reconstructible from $\dim \mathfrak{g}$ alone.
```
Rationale: AP62 substantive content ("generating functions record full graded
dimensions, not Euler characteristics") already inline immediately after the
slug; slug replaced with neutral lead-in ("We emphasise:").

### Heals 5-10: theorem_index.tex (six PHANTOM FILE warnings with `; AP255` slug)

Lines 2379, 2382, 2389, 2390, 2391, 2392. Applied `replace_all: true` on
the common substring `[PHANTOM FILE: chapter does not exist on disk; AP255]`,
replacing with `[PHANTOM FILE: chapter does not exist on disk]`.

Rationale: AP236 protocol (a) — parenthetical catalogue tag removal. The
substantive warning "[PHANTOM FILE: chapter does not exist on disk]" retains
the structural information the reader needs; the `; AP255` suffix is pure
scaffolding and would rot with any AP renumbering.

## Phase 3: Verification

Pre-commit gate re-run post-heal:

```
grep -rn '\bAP[0-9]\+\b\|\bHZ-[0-9IVX]\+\b\|V[0-9]-AP[0-9]\+\|AP-CY[0-9]\+\|\bPattern [0-9]\+\b\|Cache #[0-9]\+\|first_principles_cache' \
  chapters/ standalone/ 2>/dev/null | grep -v ':[0-9]*:\s*%' | grep -v 'HZ-IV' | wc -l
=> 0
```

Direct `\ap{N}` grep re-run:
```
grep -rn '\\ap\{[0-9]+\}' chapters/ standalone/ appendices/
=> no matches
```

Both zero. Vol I typeset prose is now clean with respect to the AP236
pre-commit gate.

## Phase 4: Patch / delivery

This session edits the main repo working tree directly (not a worktree);
no `git apply` patch needed. Files modified:

- `chapters/examples/bar_complex_tables.tex` (heals 1-4)
- `standalone/theorem_index.tex` (heals 5-10)

`git diff --stat` will show 2 files changed; the diffs are the exact
substitutions documented above, no additional content.

## Phase 5: No new APs

No new failure mode surfaced during this sweep. AP236 itself (constitutional,
already catalogued) is the governing pattern; reservation block AP1421-AP1440
unused (AP314 discipline: do not inscribe new APs when existing ones suffice).

## Notes

- Hygiene-gate grep covers `chapters/` + `standalone/`; `appendices/` also
  grep-clean for `\ap{N}` (zero hits) and for the broader AP236 regex.
- All remaining AP/HZ/V-AP/AP-CY tokens in Vol I live inside `%` comments
  (allowed per AP236 "ALLOWED: LaTeX comments starting with %") or as
  scaffolding in `references.bib` comments.
- The `AP281 alias layer` comment in `standalone/references.bib:1196` starts
  with `%` and is a permitted scaffolding comment (not typeset).
