# Wave-6 Phantom-Label Programme Sweep (2026-04-18)

**Mode.** Diagnostic only — no edits, no commits, no build changes. Pre-commit guardrails acknowledged throughout.

**Scope.** Enumerate every `\phantomsection\label{...}` across Vol I, Vol II, Vol III; classify as (a) legitimate alias (genuine definition elsewhere, phantom in preface/index for compile stability), (b) load-bearing phantom with live consumers (AP255 + AP264 violation), (c) retirable orphan (no genuine def, no consumers). Cross-resolve V2 `V1-` / V3 `V3-` prefix refs against genuine Vol I / Vol III labels. Sanity-check the CLAUDE.md Waves 1--5 flagged-phantom register.

## Aggregate counts

| Volume | phantomsections | legitimate alias (genuine+phantom) | load-bearing AP255 (0 genuine, 1+ refs) | retirable (0 genuine, 0 refs) |
|--------|---|---|---|---|
| Vol I  | 359 | 239 | 75  | 45 |
| Vol II | 599 |   6 | 356 | 237 |
| Vol III|  60 |   0 | 50  | 10 |

Vol II cross-volume resolution: 230 of the 363 `self`/`V1-` unresolved are `V1-`-prefixed and DO resolve to a genuine Vol I label (legitimate AP286 alias pattern). Net Vol II residue after cross-resolution: **133 genuinely unresolved phantom labels** (126 self-prefixed + 7 `V1-` prefixed with no Vol I target).

## CLAUDE.md-flagged phantom register — status at audit time

Tri-state: PHANTOM-ONLY = phantomsection in preface/index, no genuine def; ABSENT = no definition and no phantomsection anywhere; GENUINE = live theorem.

| Label | Vol | Status | Total refs (V1/V2/V3) | Action |
|-------|-----|--------|----------|--------|
| `thm:chiral-qg-equiv` | V1 | GENUINE | 323 (323/0/0) | — (canonical; load-bearing) |
| `thm:chiral-qg-equiv-elliptic` | V1 | ABSENT | 0 | Retract preface advertisement, or inscribe |
| `thm:chiral-qg-equiv-toroidal-formal-disk` | V1 | ABSENT | 0 | Same |
| `thm:chiral-qg-equiv-elliptic-sf` | V1-stand | ABSENT | 0 | Standalone-only; not `\input`-ed |
| `thm:chiral-qg-equiv-toroidal-sf` | V1-stand | ABSENT | 0 | Same |
| `thm:chiral-qg-equiv-ordered` | V1 | ABSENT | 2 | Retarget to `thm:chiral-qg-equiv` OR inscribe ordered variant |
| `def:ordered-koszul-chiral-algebra` | V1 | ABSENT | 0 | Retract; no consumers |
| `prop:yangian-ordered-koszul` | V1 | ABSENT | 0 | Retract; no consumers |
| `prop:sl2-yangian-triangle-concrete` | V1 | ABSENT | 0 | Retract |
| `thm:w-infty-chiral-qg-completed` | V1 | ABSENT | 0 | Retract |
| `prop:e3-gl-N` | V1 | ABSENT | 0 | Retract; content in `rem:e3-non-simple-gl-N` |
| `thm:e3-identification-semisimple` | V1 | ABSENT | 0 | Retract |
| `thm:e3-identification-reductive` | V1 | ABSENT | 2 | Retarget to `rem:e3-non-simple` OR inscribe |
| `prop:e3-heisenberg` | V1 | ABSENT | 0 | Retract |
| `thm:e3-identification-solvable` | V1 | ABSENT | 0 | Retract |
| `thm:chiral-positselski-7-2` | V1 | PHANTOM-ONLY | 2 | Retarget refs to `thm:chiral-positselski-weight-completed` (preface stub at `theorem_B_scope_platonic.tex:246`) |
| `thm:chiral-positselski-5-3` | V1 | PHANTOM-ONLY | 0 | Retire phantomsection at `theorem_B_scope_platonic.tex:247` |
| `thm:grt1-rigidity` | V1 | ABSENT | 1 | Retarget or inscribe (was retired from preface at `preface.tex:5135` per comment trail) |
| `thm:uhf-main` | V2 | ABSENT | 0 | Retract or inscribe (Monster chapter) |
| `thm:uhf-leech-class-M-chain-level` | V2 | ABSENT | 0 | Retract |
| `prop:bd-cg-equivalence` | V2 | ABSENT | 1 | Retarget or inscribe |
| `def:factorization-swiss-cheese-operad` | V2 | ABSENT | 1 | Retarget or inscribe |
| `conj:topologization-general` | V2 | ABSENT | **37** (36 in V1, 1 in V2) | **Highest-priority heal**: 36 Vol I consumers call out a Vol II conjecture with zero def; inscribe in `e_infinity_topologization.tex` or retarget to `thm:iterated-sugawara-construction` |
| `rem:kac-moody-filtered-comparison` | V1 | GENUINE | — | Already healed |

## Top load-bearing phantoms (0 genuine, 1+ refs)

### Vol I (top 12)

| Refs | Label |
|------|-------|
| 43 | `conj:master-bv-brst` |
| 15 | `thm:spectral-characteristic` |
| 7 | `def:thqg-holographic-datum` |
| 6 | `chap:toroidal-elliptic` (migrated to Vol III, refs stale) |
| 5 | `thm:topologization-tower` (aliased to Vol II iterated-Sugawara; AP286-legitimate in spirit but definition lives cross-volume) |
| 4 | `ch:kontsevich-integral` (migrated to Vol II) |
| 4 | `chap:infinite-fingerprint-classification` |
| 4 | `conj:master-infinite-generator` |
| 4 | `thm:derived-additive-kz` (migrated to Vol II) |
| 4 | `thm:elliptic-vs-rational` |
| 3 | `thm:shadow-siegel-gap` |
| 2 | `V2-prop:modular-bootstrap-to-curved-dunn-bridge` (Wave-1 heal target) |

### Vol II (top 12, self-prefix genuine unresolved)

| Refs | Label |
|------|-------|
| 11 | `prop:vir-all-mk` |
| 10 | `thm:bar-cobar-isomorphism-main` |
| 10 | `thm:quantum-complementarity-main` |
| 9 | `thm:e-infinity-specialisation-Winfty` |
| 9 | `thm:genus-universality` |
| 8 | `thm:mc2-bar-intrinsic` |
| 8 | `thm:w-infty-e-infty-topological-convergence` |
| 7 | `subsec:gravity-shadow-tower` |
| 5 | `thm:collision-depth-2-ybe` |
| 5 | `thm:shadow-archetype-classification` |
| 5 | `thm:shadow-connection-kz` |
| 4 | `thm:MacMahon-connection` |

### Vol III (top 10)

| Refs | Label |
|------|-------|
| 22 | `ch:k3-times-e` |
| 5 | `thm:riccati-algebraicity` (Vol I home; cross-volume phantom) |
| 4 | `thm:gaudin-yangian-identification` |
| 3 each | `constr:platonic-package`, `thm:bar-cobar-adjunction`, `thm:kz-classical-quantum-bridge`, `thm:lattice-voa-bar`, `thm:modular-characteristic`, `thm:shadow-connection`, `thm:vol1-seven-face-master`, `thm:vol2-seven-face-master` |

## Build-oracle.

Not executed — per hook guardrail + sweep-scope discipline (diagnostic-only). A `pkill -f pdflatex; make fast 2>&1 | grep "Reference.*undefined"` run in a follow-up wave will produce ground-truth `[?]`-render count and should be cross-checked against the 75 + 133 + 50 = **258 programme-wide load-bearing unresolved phantoms** predicted by this sweep. (Legitimate aliases + resolved V1-/V3- prefix refs: ~475 additional phantomsections that compile cleanly to existing targets and do NOT render `[?]`.)

## Heal recommendations — priority tiers

**Tier 1 (HIGHEST, >20 consumers each).** `conj:topologization-general` V2 (37 refs including 36 Vol I consumers); `ch:k3-times-e` V3 (22 refs); `thm:spectral-characteristic` V1 (15 refs); `conj:master-bv-brst` V1 (43 refs). Each of these is a mass-consumer phantom that will render as `[?]` on multiple pages of the PDF.

**Tier 2 (load-bearing, 5--11 consumers).** Vol II self-prefix genuine unresolved: `prop:vir-all-mk`, `thm:bar-cobar-isomorphism-main`, `thm:quantum-complementarity-main`, `thm:e-infinity-specialisation-Winfty`, `thm:genus-universality`, `thm:mc2-bar-intrinsic`, `thm:w-infty-e-infty-topological-convergence`, `thm:collision-depth-2-ybe`, `thm:shadow-archetype-classification`, `thm:shadow-connection-kz`. These are either (a) genuinely missing theorems advertised in conclusion/preface, or (b) renamed targets whose consumers were not updated atomically (AP149 propagation failure).

**Tier 3 (CLAUDE.md-register aspirational absents).** All 12 ABSENT register entries above (chiral-qg-equiv-elliptic, ordered/toroidal variants, E_3-identification series, w-infty-chiral-qg-completed). Heal menu per CLAUDE.md AP255/AP256 discipline: (a) inscribe the theorem (if genuine mathematical content exists); (b) retarget consumer refs to the nearest genuine theorem with a `Remark[Attribution]` noting scope; (c) retract the preface/standalone advertisement — zero-consumer variants are cheapest to retire. Nine of the twelve ABSENT entries have 0 consumers; the three with consumers (`thm:chiral-qg-equiv-ordered` 2 refs, `thm:e3-identification-reductive` 2 refs, `thm:grt1-rigidity` 1 ref) need retargeting before retraction.

**Tier 4 (retirable orphans, 0 consumers).** 45 Vol I + 237 Vol II + 10 Vol III = **292 retirable phantomsections** (0 genuine def, 0 refs). These are preface/concordance stubs whose target chapters were migrated (e.g. `ch:ht-boundary` Vol I -> Vol II; `chap:casimir-divisor`) or whose planned content was dropped. Delete the phantomsection line in the source file; no other change required.

## Commit plan for follow-up wave

1. **Wave-7-A (Tier 1 inscribe/retarget).** Four targeted inscriptions or retargets. Constraint: each touches a chapter body (not just preface); each requires pre/post grep at chapter granularity (AP149 + AP5).
2. **Wave-7-B (Tier 4 retirement sweep).** 292 phantomsection deletions across three volumes. Mechanical; low risk; single commit per volume.
3. **Wave-7-C (Tier 3 register reconciliation).** Per CLAUDE.md status-table hygiene (AP271 reverse drift): retract the status-table rows that advertised the 12 ABSENT-register entries as PROVED; replace with "NOT INSCRIBED --- advertisement retracted" OR inscribe where mathematical content stands.
4. **Wave-7-D (Tier 2 Vol II self-phantom audit).** For each of the 10 top-refcount Vol II self-phantoms, trace to the advertised-home chapter (e.g. `prop:vir-all-mk` -> likely 3d gravity or iterated-Sugawara chapter) and inscribe-or-retarget.

## Infrastructure recommendation

Add a pre-commit gate that runs the Python scanner in this sweep and refuses any commit that INCREASES the total phantomsection-with-0-genuine-def count. This catches AP255 + AP264 at commit time rather than at the next audit wave.

## File inventory

- Phantom-enumeration script: `/tmp/phantom_audit.py`
- Cross-volume resolver: `/tmp/cross_vol.py`
- Register-target ref count: `/tmp/absent_refs.py`
- Raw phantom lists: `/tmp/v1_phantoms.txt`, `/tmp/v2_phantoms.txt`, `/tmp/v3_phantoms.txt`
