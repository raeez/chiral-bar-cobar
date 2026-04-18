# Wave-17 AP313 Verification — Vol II lower-5 thqg AP287 heal status

**Date**: 2026-04-18
**Verifier**: diagnostic (no edits, no commits)
**Context**: Agent aea77b6c24beb6c6a returned truncated "Acknowledged." after
35 tool uses. This note audits whether the claimed Option A heals
(Volume~I prose prefix + umbrella "Scope restriction inherited from Vol~I"
remark) actually landed on disk for the five target files.

## Expected deliverable

`adversarial_swarm_20260418/wave17_vol_ii_lower5_thqg_ap287.md` — **ABSENT**.
No session note was produced. AP313 truncated-result pattern confirmed at
the deliverable layer.

## Per-file verification table

| File | Umbrella remark | Volume~I prose prefix hits | \ref{V1-...} count | Verdict |
|---|---|---|---|---|
| `thqg_soft_graviton_theorems.tex` | **YES** (L139) | 9 | 16 | **PASS** |
| `thqg_modular_bootstrap.tex` | NO | 1 (L1612) | 14 | **FAIL (AP320)** |
| `thqg_gravitational_complexity.tex` | NO | 2 (L835, L2612) | 24 | **FAIL (AP320)** |
| `thqg_gravitational_s_duality.tex` | NO | 5 (L1679, L1683, L1686, L1693, L1843) | 22 | **PARTIAL (AP321)** |
| `thqg_3d_gravity_movements_vi_x.tex` | NO | 2 (L121, L1733) | 5 | **FAIL (AP320)** |

Legend:
- **PASS** = umbrella remark + ≥5 Volume~I prose prefixes, discipline installed
- **PARTIAL** = multiple prose prefixes + Attribution remark on one theorem, but
  no file-level umbrella scope remark (AP321: partial discipline; the
  Attribution remark at L1683 covers Facet IV only, not the chapter)
- **FAIL (AP320)** = sparse prose prefixes, no umbrella remark, no Attribution
  remark; load-bearing \ref{V1-...} citations inherit external scope without
  discipline

## Edits landed count

- Agent aea77b6c landed the heal on **1 of 5** target files.
- `thqg_soft_graviton_theorems.tex` is the ONLY file with the canonical
  Option A structure (umbrella remark at L139 explicitly enumerating Vol~I
  theorems + 9 Volume~I prose prefixes).
- The other four files retain residual Volume~I prose from prior sessions
  (Wave-14/16) but received no umbrella remark insertion.

## Cumulative Vol II AP287 heal totals

| Wave | Commit | Files touched | Heals | Discipline structure |
|---|---|---|---|---|
| Wave-14 | ab2135ad | thqg_symplectic_polarization.tex | 6 | umbrella + prose |
| Wave-16 | ad23acfe | 4 top thqg files | 19 | umbrella + prose |
| Wave-17 | (uncommitted) | thqg_soft_graviton_theorems.tex only | ~9 | umbrella + prose |
| Wave-17 residual | — | 4 files unhealed | 0 | — |

**Files now carrying full AP287 discipline**: 6 of ~14 target thqg files
(symplectic_polarization + 4 top + soft_graviton) plus 3 earlier files
(yangian, holographic_reconstruction, fredholm_partition_functions,
critical_string_dichotomy) = 9 files with umbrella remark.

**\ref{V1-...} coverage estimate**: the 5 Wave-17 target files contain
14+24+22+5+16 = 81 \ref{V1-...} citations. 16 are under full discipline
(soft_graviton only); 65 are NOT. Cumulative Vol II AP287 coverage of the
464-ref baseline: approximately ~45-50% (rough estimate — soft_graviton 16
+ Wave-14/16 discipline on 5 files ~120+ refs + pre-existing umbrella-remark
files ~50 refs = ~200/464).

## Residual open

Four files require Option A heal application:
1. `thqg_modular_bootstrap.tex` (14 V1 refs, 1 prose prefix)
2. `thqg_gravitational_complexity.tex` (24 V1 refs, 2 prose prefixes)
3. `thqg_gravitational_s_duality.tex` (22 V1 refs, 5 prose prefixes + 1
   Attribution remark — partially healed, needs chapter-level umbrella)
4. `thqg_3d_gravity_movements_vi_x.tex` (5 V1 refs, 2 prose prefixes)

Estimated heal volume: ~25 edits (4 umbrella remarks + ~20 prose prefix
additions at load-bearing proof sites).

## Commit plan

Deferred to Wave-18 follow-up. Beilinson discipline: no commits authored
under the truncated Wave-17 pass. When heal is applied:
- Single commit per file (4 commits) OR single heal commit covering all 4
- Author: Raeez Lorgat only, no AI attribution
- Pre-commit: verify Vol II build passes, no stray \ref{V1-...} with AP321
  drift

## AP classification

- **AP313** (truncated-result pattern): confirmed at session-note layer
  (no deliverable note produced)
- **AP320** (agent partial landing): confirmed — 1 of 5 files healed
- **AP316** (silent no-op on remaining files): plausible but ruled out —
  agent did land substantive edits on soft_graviton, so the 140s / 35
  tool-use budget was not wholly vacuous; the pattern is closer to
  "heal first file, run out of budget, return truncated ack" than to
  "pure confabulation"
- **AP321** (partial discipline drift): gravitational_s_duality file
  carries one Attribution remark scoped to Facet IV, missing the chapter
  umbrella remark; this is the subtle partial case
