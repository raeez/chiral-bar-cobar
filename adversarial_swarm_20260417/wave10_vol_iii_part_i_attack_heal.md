# Wave-10 Vol III Part I Foundations — Attack/Heal Report

**Date**: 2026-04-17
**Target**: Vol III Part I "Foundations: CY Categories and Cyclic A_inf" (main.tex:603)
**Scope**: 4 chapters
- `chapters/theory/introduction.tex` (1791 lines)
- `chapters/theory/cy_categories.tex` (256 lines)
- `chapters/theory/cyclic_ainf.tex` (239 lines)
- `chapters/theory/hochschild_calculus.tex` (379 lines)

## Phase 1: Attack (AP247 / HZ-7 / AP-CY62 / AP-CY65)

### (i) CG deficiency opening
PASS. `introduction.tex` opens with the structural problem (CY category → chiral algebra matching bar complex / cyclic bar data), NOT a results list. Part I main.tex preamble (lines 606–652) similarly states the PROBLEM of Hochschild identification as the categorical raw material.

### (ii) AP247 — Phi as single functor vs programme
**VIOLATION, HEALED.** Three sites:

- `introduction.tex:43-50` boxed formula framed Φ as "the translation is *one* symmetric monoidal functor", with a case-split codomain over d. This is the canonical AP247 violation.
- `introduction.tex:86-88` "The per-d theorems CY-A_1, ..., CY-A_{d ≥ 4} are evaluations of the unified Φ, not parallel theorems" — DIRECT contradiction of AP247.
- `cy_categories.tex:4` "the Vol III functor Φ acts: Φ takes a cyclic A_inf CY category of dimension d as input" — single-functor phrasing.
- `cyclic_ainf.tex:180-185` mixed: text says "correspondence Φ_d" but displayed formula writes Φ without index.

### (iii) Derived McKay
Not in Part I. Bridgeland-King-Reid lives in Part II `cy_to_chiral.tex:389, 1015-1239`. Correct scope (orbifold CY_d, A_1/A_n). No Part I violation.

### (iv) Koszul duality distinction (AP-CY62)
PASS. Hochschild_calculus.tex:6-15 has canonical three-Hochschild separation (cat / top / chiral). Part I does NOT conflate CY-Koszul with chiral-Koszul.

### (v) HZ-7 bare κ
PASS. Zero bare `\kappa` in all four Part I chapters. Each chapter carries the `κ_bullet ∈ {ch, cat, BKM, fiber}` convention remark.

### (vi) AP-CY65 spectral parameters
PASS. `introduction.tex:123, 206, 786` correctly attribute spectral parameters to evaluation modules; no claim that Y(g) lacks spectral parameters.

### (vii) Cross-volume Vol I imports
PASS. cy_categories.tex:8, cyclic_ainf.tex:8 reference Vol I climax-platonic, universal-conductor. Hochschild_calculus.tex:14 cites Vol I Theorem H.

### (viii) Mukai pairing
PASS. cy_categories.tex Theorem CY-D_2 uses Mukai-pairing scoping. Explicit `h^{1,0}=0` hypothesis in CY-D_2 (Wave-6 #34 lineage visible).

### (ix) AP248 dioperad
No SC-structure claims in Part I; SC lives Part VI. No violation.

## Phase 2: Heal

Three surgical edits:

### Heal H1 — introduction.tex boxed formula
Rewrote lines 42-50 box to: `Φ_d : CY_d-Cat → E_n(d)-ChirAlg(M_d)` as a family `{Φ_d}_{d ≥ 1}`. Added explanatory sentence: "The programme is a family, not a single functor: the operadic level n(d) jumps between dimensions, so no single codomain category holds all Φ_d simultaneously. The uniform presentation in the universal properties is what unifies the programme; the per-d evaluations remain parallel theorems sharing one axiomatic skeleton."

### Heal H2 — introduction.tex "unified Phi" retraction
Rewrote lines 86-88: "CY-A_d are parallel theorems sharing the (U1)-(U4) skeleton; their coincidence on this skeleton is the content of the correspondence programme, not a reduction to a single underlying functor."

### Heal H3 — cy_categories.tex opening
Rewrote line 4: "the Vol III correspondence programme `{Φ_d}_{d ≥ 1}` acts: each Φ_d takes a cyclic A_inf CY category of dimension d as input..."

### Heal H4 — cyclic_ainf.tex signature formula
Rewrote lines 180-185: display now reads `Φ_d : CY_d-Cat → E_{n(d)}-ChirAlg` with index, matching text "correspondence programme `{Φ_d}_{d ≥ 1}`".

## Residual findings (not in scope, flagged)

- Hook pre-existing warnings on AP24 (`κ_ch + κ_ch^! = K`) at introduction.tex:637 — this is the scalar complementarity variant (Trinity K convention, per AP234 distinction between κ+κ^! and K). Pre-existing, not in Part I wave-10 scope.
- Hook warning AP14 at introduction.tex:465 — pre-existing "inversion (recovering the algebra), not Koszul duality" — correct math (AP25/AP34/AP50 discipline).

## Voice check
Russian-school: Kontsevich/Costello at cy_categories.tex:4; Stasheff/Keller/Kontsevich-Soibelman at cyclic_ainf.tex:43; Bridgeland-King-Reid deferred to Part II as appropriate.

## HZ-7 zero-tolerance grep
`grep '\\kappa[^_{]'` across all 4 chapters: 0 hits. Compliant.

## Constitutional hygiene
No AP-index leakage to typeset prose. Healed paragraphs contain only mathematical substance (family indexing, operadic-level dispatch, parallel-theorem semantics). No `AP\d+` tokens, no `HZ-\d+`, no cache indices.
