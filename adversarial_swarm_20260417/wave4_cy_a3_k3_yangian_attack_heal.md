# Wave 4: CY-A_3 + K3 Yangian + BFN Φ ADE attack/heal

## Targets

- `thm:total-ainf-compat` (Costello TCFT) at Vol III `chapters/theory/m3_b2_saga.tex:547`.
- `thm:derived-framing-m3b2` (infinity-categorical resolution) at `m3_b2_saga.tex:697`.
- `thm:k3-abelian-yangian-presentation` at Vol III `chapters/examples/k3_yangian_chapter.tex:853`.
- `thm:bfn-phi-ade-identification` at `k3_yangian_chapter.tex:110`.
- `conj:osp-yangian-mukai` at `k3_yangian_chapter.tex:1855`.

## Phase 1 attack: findings

### (i) CY-A_3 infinity-categorical framework — RIGOROUS

Ambient is Francis-Gaitsgory factorization / infinity-categorical
obstruction theory. The claim "`[m_3, B^{(2)}] ≠ 0` chain-level is
NOT an obstruction" is cleanly stratified:

- **Level 1 (strict, chain):** FALSE for non-formal A∞-algebras
  (`prop:chain-nonvanishing-generic`). Not pretended otherwise.
- **Level 2 (homotopy, total):** `{b, B^{(2)}} = 0` via Costello
  open-closed TCFT (`thm:total-ainf-compat`). The CRITICAL caveat
  is clearly flagged: `B^{(2)}` here is `B^{(2)}_{TCFT}`, NOT
  `B^{(2)}_{naive}`; their chain-level identification is
  CONJECTURAL for non-formal algebras (`rem:tcft-vs-naive-b2`).
  This is the honest open frontier of CY-A_3.
- **Level 3 (derived, ∞-cat):** Obstruction class
  `[Obs_A∞] ∈ HH^{-2}_{E_1}(HH_*(C), HH_*(C))` vanishes by
  Francis-Gaitsgory Dunn additivity + unit-connectedness of
  `π_0(HH_*(C)) = k`. Goodwillie tower argument closes all higher
  obstructions. Rigorous.

No confabulation detected. The "universally" scope of Obs_A∞ = 0 via
Costello TCFT is honestly restricted: Level 2 is universal at the
moduli-operad level; chain-level promotion is non-formal-conditional.

### (ii) K3 Yangian presentation — PROPERLY DECOUPLED (AP239 healed)

The Abelian K3 Yangian `thm:k3-abelian-yangian-presentation` depends
ONLY on rank-24, signature-(4,20), even unimodular lattice + CY_2
constraint `Σh_i = 0`. This is correctly flagged at
`rem:k3-yangian-lattice-scope` (lines 835-851): "the 'K3' label
reflects the physical source... but the mathematical object is the
rank-24 indefinite-signature Heisenberg Yangian". AP239 healed.

### (iii) osp vs gl type — CORRECT (AP246 healed)

Mukai form is orthogonal signature (4,20) → `Y_osp(4|20)`, NOT
`Y(gl(4|20))`. The `rem:gl-to-osp-correction` (line 1895) explicitly
acknowledges the earlier draft misnomer and renames throughout.

### (iv) NUMERICAL INCONSISTENCY — osp(4|20) dim count [HEALED THIS WAVE]

`k3_yangian_chapter.tex:2014-2029` had:
```
  216 + 2·80 = 376, which equals C(25,2) - 24 = 276
```
Multiple errors: (a) `216 + 2·80 = 376`, but standard superdim is
`216 + 80 = 296` (even once, odd once). (b) `376 ≠ 276`. (c) The
"naive" `C(25,2) - 24 = 276` misidentifies `dim gl(m|n)`, which is
`(m+n)^2 = 576` for (4,20). Healed this session with corrected
identities: even 216, odd 80, total 296; gl(4|20) comparison 576.

### (v) BFN ADE three-path disjointness — AP243 PROPAGATION DEBT [HEALED THIS WAVE]

`thm:bfn-phi-ade-identification:136` asserted "Three disjoint
verification paths" without noting the V1/V3 shared Kronheimer
input chain registered by AP243. V2 (BFN affine-Grassmannian) is
genuinely input-disjoint; V1 (BKR derived McKay) and V3
(moment-map normalization) both take Kronheimer `~S_g` as input
and are algebraically-disjoint only at the verification layer.

Healed: added `rem:bfn-ade-input-dependency` noting TWO
input-disjoint paths (V2 versus V1+V3 block) with three
verification-layer checks. Preserves both the sheaf/RTT/moment-map
disjointness claim and the honest input-dependency accounting.

### (vi) Mukai rank/signature — CORRECT

Mukai lattice `\widetilde{H}(S, Z) ≃ U^3 ⊕ E_8(-1)^2` has rank 24,
signature (4,20). Chapter uses this consistently; distinguishes
from `H^2(K3)` (rank 22, signature (3,19)). No rank confusion.

### (vii) κ_BKM vs κ_ch bare kappa — HZ-7 Vol III discipline

Lines 4998-5004 show `κ^Hilb_BKM(K3^[n])` subscripted. Hook linter
false-positived on the superscript. Not a violation.

### (viii) Φ-scope per-d — AP247 registered

Per-d scope correct at conjecture statements; no functor-promotion
over d detected in this chapter.

## Summary

- CY-A_3 framework: SOUND. Chain-level TCFT/naive identification
  gap is the honest remaining frontier, properly flagged.
- K3 Yangian presentation: SOUND. Lattice decoupling correctly
  inscribed.
- osp type assignment: SOUND (AP246 healed).
- osp(4|20) dim arithmetic: CORRECTED (216 + 80 = 296; gl ≈ 576).
- BFN ADE three-path claim: HEALED via input-vs-verification
  stratification remark.
- No AP/HZ/Pattern/Cache tokens introduced in typeset prose
  (constitutional hygiene preserved).

## Files touched

- `~/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`
  (two edits: dimension arithmetic heal + AP243 input-dependency remark)

## Residual open (genuine frontier, not debt)

- Chain-level identification `B^{(2)}_{TCFT} ≃ B^{(2)}_{naive}` for
  non-formal A∞ algebras (explicit chain homotopy).
- `conj:osp-yangian-mukai` at rank (4,20): full reflection equation
  verified only at rank (1,2) and (2,2); rank-(4,20) is open.
- Conjecture `conj:bfn-k3-yangian-mukai` for generic K3 moduli
  requires non-quiver BFN extension.
