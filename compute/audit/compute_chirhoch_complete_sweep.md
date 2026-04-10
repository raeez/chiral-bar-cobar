# ChirHoch AP94/AP95/AP96/AP97/AP98 Compute-Layer Sweep

**Scope.** Complete sweep of `compute/lib/*.py` and `compute/tests/*.py`
for remaining ChirHoch violations of the polynomial-ring (Gelfand-Fuchs)
model, beyond the 5 files already under parallel-agent rectification.

**Excluded from this sweep** (being fixed by parallel agents):
1. `compute/lib/derived_center_explicit.py`
2. `compute/lib/theorem_h_hochschild_polynomial.py`
3. `compute/lib/theorem_thm_h_e3_rectification_engine.py`
4. `compute/tests/test_derived_center_explicit.py`
5. `compute/tests/test_theorem_h_hochschild_polynomial.py`

## Files grepped

All 24 `compute/lib/*.py` files with any mention of `ChirHoch`, and all
15 `compute/tests/test_*.py` files with any mention of `ChirHoch`.  In
addition, `compute/lib/open_sft_bar.py` was audited because it contains
a `C[theta]` pattern (complete-intersection Ext, not ChirHoch).  Full
list:

```
compute/lib/
  chriss_ginzburg_universal.py        AUDITED + FIXED
  chiral_hochschild_engine.py         AUDITED + FIXED
  theorem_fle_critical_level_engine.py AUDITED (clean)
  koszulness_ten_verifier.py          AUDITED (clean)
  cross_volume_bridge.py              AUDITED (clean)
  theorem_koszul_12fold_rectification_engine.py AUDITED (clean)
  theorem_swiss_cheese_kontsevich_engine.py     AUDITED (clean)
  theorem_pentagon_koszul_engine.py   AUDITED (clean)
  theorem_linshaw_rigidity_engine.py  AUDITED (needs-manual-review: see below)
  cy_twisted_holography_k3e_engine.py AUDITED (needs-manual-review: see below)
  bv_brst_purity_engine.py            AUDITED (clean)
  cy_nc_deformation_k3e_engine.py     AUDITED (clean)
  cy_koszul_dual_k3e_engine.py        AUDITED (clean)
  holographic_code_engine.py          AUDITED (clean)
  shadow_channel_decomposition.py     AUDITED (clean)
  bc_grand_unified_atlas_engine.py    AUDITED (clean)
  bc_nc_motives_shadow_engine.py      AUDITED (clean)
  bc_derived_moduli_shadow_engine.py  AUDITED (clean)
  factorization_homology_engine.py    AUDITED (clean)
  annulus_trace_verification.py       AUDITED (clean)
  swiss_cheese_chain_model.py         AUDITED (clean)
  derived_center_genus2_engine.py     AUDITED (clean, no ChirHoch hits)
  open_closed_derived_center.py       AUDITED (clean, no ChirHoch hits)
  sp4_hochschild_serre.py             AUDITED (clean, no ChirHoch hits)
  open_sft_bar.py                     AUDITED + CLARIFYING COMMENT ADDED
compute/tests/
  test_chiral_hochschild_engine.py    AUDITED (clean)
  test_cross_volume_bridge.py         AUDITED (clean)
  test_theorem_fle_critical_level_engine.py AUDITED (clean)
  test_theorem_thm_h_e3_rectification_engine.py AUDITED (clean)
  test_theorem_swiss_cheese_kontsevich_engine.py AUDITED (clean)
  test_theorem_koszul_12fold_rectification_engine.py AUDITED (clean)
  test_theorem_linshaw_rigidity_engine.py AUDITED (see Linshaw note)
  test_cy_twisted_holography_k3e_engine.py AUDITED (see K3xE note)
  test_cy_nc_deformation_k3e_engine.py AUDITED (clean: HH^2 = HH^2(X) CY case)
  test_open_closed_derived_center.py  AUDITED (clean)
  test_bc_grand_unified_atlas_engine.py AUDITED (clean)
  test_mc_programme_verification.py   AUDITED (clean)
  test_swiss_cheese_chain_model.py    AUDITED (clean)
  test_koszulness_ten_verifier.py     AUDITED (clean)
```

## Active violations found and fixed

### 1. `compute/lib/chiral_hochschild_engine.py`, line 571-576 (FIXED)

The docstring for `_virasoro_derivation_analysis` contained the
verbatim active statement:

```
NOTE: Virasoro is in the W-algebra regime, so the full
ChirHoch* = C[Θ] with |Θ| = 2. The derivation analysis
captures the degree-1 part. For the W-algebra regime,
ChirHoch^1 in the quadratic sense is dimension 1, but
the polynomial ring structure gives infinite-dimensional
total cohomology.
```

This is an AP94/AP95 violation: the docstring asserted the forbidden
C[Theta] polynomial model as the "full" ChirHoch* for Virasoro.

**Fix.** Replaced with a docstring that explicitly cites Theorem H
bounded amplitude [0,2] with dim <= 4 per AP94/AP95, noting that
the Gelfand-Fuchs polynomial-ring model is continuous Lie cohomology
of the Witt algebra and a DIFFERENT functor from chiral Hochschild.
Numerical result `dim ChirHoch^1(Vir_c) = 1` (c-deformation class)
is preserved.

### 2. `compute/lib/chriss_ginzburg_universal.py`, lines 626-647 (FIXED)

The `pi_hochschild_polynomial` function contained an internally
inconsistent AP94 "rectification": the docstring said the polynomial
model was refuted, but the replacement Betti numbers were

```
virasoro: polynomial = [1, 0, 1], betti_numbers = {0: 1, 1: 0, 2: 1}
w3:       polynomial = [1, 0, 1], betti_numbers = {0: 1, 1: 0, 2: 1}
```

This is an AP98 violation via a DIFFERENT mistake: the total dimension
is 2 (correct bound <= 4), BUT `dim ChirHoch^1 = 0` contradicts the
other rectification engines, which all give `dim ChirHoch^1(Vir_c) = 1`
(the c-deformation) per Theorem H and per the derivation analysis in
`chiral_hochschild_engine.py`, `theorem_thm_h_e3_rectification_engine.py`,
`theorem_h_hochschild_polynomial.py`, and `derived_center_explicit.py`.

This is a SILENT violation introduced by a prior partial rectification
that over-corrected: zeroing out ChirHoch^1 while stripping the
polynomial-ring model.

**Fix.** Replaced with Theorem-H consistent values:

```
virasoro: polynomial = [1, 1, 1], betti_numbers = {0: 1, 1: 1, 2: 1}
w3:       polynomial = [1, 1, 1], betti_numbers = {0: 1, 1: 1, 2: 1}
```

Total dim = 3 for both families (strict <= 4 per AP98), with
`dim ChirHoch^1 = 1` tracking the c-deformation class per
`chiral_hochschild_engine._virasoro_derivation_analysis` and
`theorem_h_hochschild_polynomial.WAlgebraHochschild`.

### 3. `compute/lib/open_sft_bar.py`, line 1168 (CLARIFYING COMMENT ADDED)

The `conifold_bar_analysis` docstring contains the pattern

```
Ext*(O_0, O_0) = Wedge*(C^4) tensor C[theta] with |theta| = 2.
```

This is NOT an AP94 violation: it is the classical Eisenbud /
complete-intersection Ext algebra for the conifold singularity
R = C[x,y,z,w]/(xy-zw), a CORRECT statement about commutative-algebra
Ext.  But the surface pattern `C[theta] with |theta|=2` is identical
to the forbidden Gelfand-Fuchs ChirHoch model and could confuse future
AP94 sweeps.

**Action.** Added an inline clarifying comment stating that this is
classical Eisenbud complete-intersection Ext, NOT ChirHoch, and that
per AP94/AP95 these are distinct.  The line retains the mathematical
statement unchanged.

## Violations flagged as needs-manual-review (NOT touched)

### A. `compute/lib/theorem_linshaw_rigidity_engine.py`

This file intentionally implements Linshaw-Qi's
H^2_{1/2}(V, V) rigidity convention, which gives

```
dim ChirHoch^1(Vir_c)      = 0   (pole-order inner-derivation principle)
dim ChirHoch^1(V_k(g))     = 0
dim ChirHoch^1(free fermion) = 0
dim ChirHoch^1(betagamma)  = 0
```

These CONFLICT with the bar-complex ChirHoch convention used in
`chiral_hochschild_engine.py`, `chriss_ginzburg_universal.py`, and
`theorem_h_hochschild_polynomial.py`, which all give
`dim ChirHoch^1 = 1` for Virasoro and `= 2` for betagamma etc.

This is NOT an AP94 violation: there is no polynomial-ring or
Gelfand-Fuchs claim.  It is a genuine semantic discrepancy between
two compute modules about what `ChirHoch^1` means (Linshaw's
vertex-algebra H^2_{1/2} pole-order definition vs the bar-complex
derivation-class definition).

The file's top docstring (lines 21-38) explicitly positions itself as
interfacing with Linshaw-Qi's H^2_{1/2}, not the monograph's
ChirHoch^1, so the internal consistency is fine, but consumers who
mix this engine's ChirHochData with other engines' HochschildPolynomial
will get incompatible numbers.

**Recommendation.** Rename `ChirHochData` in this file to
`LinshawRigidityData` (or similar) and rename its fields from
`dim_H0/H1/H2` to `dim_H2_half_n` (tracking H^{2-n}_{1/2} or similar)
to prevent cross-module confusion.  OR: reconcile conventions by
settling on a single definition of ChirHoch^1 (bar-complex
derivation-class) and updating the Linshaw engine to compute
H^2_{1/2} under its own name.  This is a design decision beyond
AP94 scope; flagging for manual review.

### B. `compute/lib/cy_twisted_holography_k3e_engine.py`, lines 940-1027

The `derived_center_k3e` function computes

```
ChirHoch^0 = 24
ChirHoch^1 = 576   (= rank^2)
ChirHoch^2 = 24
Total = 624
```

for the 24-free-boson (K3 x E boundary) algebra.  This gives total
dim 624, far above the "total dim <= 4" bound.

This is NOT a strict AP98 violation (AP98 bounds ChirHoch*(Vir_c)
specifically; free-field algebras with rank 24 genuinely have
rank-proportional ChirHoch^1 by the End(h) derivation count), but
it DOES conflict with how other engines compute ChirHoch for
Heisenberg-type algebras:

- `chiral_hochschild_engine._heisenberg_derivation_analysis` gives
  `dim ChirHoch^1(H_k) = 1`, NOT rank.
- `cross_volume_bridge.verify_bridge_5_heisenberg` gives
  `dim ChirHoch^1 = 1`, matching the engine.

The K3xE engine treats ChirHoch^1 as `End(h) = h tensor h*` (576),
while the standard Heisenberg convention in the canonical engine
gives 1 (a single level-deformation class, with the full OPE
current-algebra derivations counted as inner in the chiral sense).

**Recommendation.** Reconcile the rank-24 Heisenberg convention with
the canonical engine.  Either (a) the K3xE engine should reduce to
Theorem H amplitude [0,2] with dim HH^1 = 1 (the level deformation),
treating the 24 currents as inner via the current algebra; or
(b) the canonical engine should be generalized to count rank when
the rank is large.  This is a convention choice beyond AP94 scope;
flagging for manual review.

## Legitimate CE / Lie-cohomology citations (LEAVE in place)

Every other `Gelfand-Fuchs` or `polynomial-ring` mention in the
compute layer is a REFUTATION note or a classical-Lie-cohomology
citation distinguishing ChirHoch from Chevalley-Eilenberg /
Gelfand-Fuchs continuous Lie cohomology.  These are not violations;
they are anti-confusion prose that should remain.  Representative
occurrences (non-exhaustive):

- `compute/lib/cross_volume_bridge.py:397-401` ("earlier
  Gelfand-Fuchs polynomial-ring model ... is REFUTED")
- `compute/lib/chiral_hochschild_engine.py:573-577, 758-767`
  (refutation note inside `_virasoro_derivation_analysis` and
  the W-algebra section header)
- `compute/lib/theorem_fle_critical_level_engine.py:495-513,
  762-805` (explicit REFUTED docstrings)
- `compute/lib/koszulness_ten_verifier.py:881-884` (refutation note
  inside `verify_chirhoch_range`)

All of these are refutation-context citations distinguishing the
forbidden model from Theorem H, not active uses of the model.

## Final verification grep

Post-fix grep over `compute/lib` and `compute/tests` for the
canonical AP94 signatures, restricted to the non-excluded files:

```
pattern: C\[Theta\]|C\[Θ\]|Gelfand.?Fuchs|polynomial ring model
excluded: derived_center_explicit.py, theorem_h_hochschild_polynomial.py,
          theorem_thm_h_e3_rectification_engine.py,
          test_derived_center_explicit.py,
          test_theorem_h_hochschild_polynomial.py
```

Remaining hits in non-excluded files, classified:

| File                                    | Line       | Classification              |
|-----------------------------------------|------------|-----------------------------|
| cross_volume_bridge.py                  | 397-398    | REFUTATION note (legitimate)|
| open_sft_bar.py                         | 1177       | Clarifying comment (fixed)  |
| open_sft_bar.py                         | 725,1172   | Eisenbud CI Ext (not ChirHoch)|
| chriss_ginzburg_universal.py            | 595,630-646| Refutation note (legitimate)|
| chiral_hochschild_engine.py             | 575-577,764| Refutation note (legitimate)|
| koszulness_ten_verifier.py              | 881-884    | Refutation note (legitimate)|
| theorem_fle_critical_level_engine.py    | 500,763,774,801 | Refutation note (legitimate)|
| test_chiral_hochschild_engine.py        | 550-551,663| Refutation note (legitimate)|
| test_theorem_fle_critical_level_engine.py | 449      | Refutation note (legitimate)|

Zero active uses of the polynomial-ring (Gelfand-Fuchs) model remain
in non-excluded compute/lib or compute/tests files.  Every remaining
reference is a prose anti-confusion citation.

## Summary

- **2 active infections fixed** (chiral_hochschild_engine.py,
  chriss_ginzburg_universal.py).
- **1 clarifying comment added** (open_sft_bar.py, pattern match
  against classical Eisenbud Ext, not a violation).
- **2 cross-engine semantic discrepancies flagged** for manual review
  (theorem_linshaw_rigidity_engine.py Linshaw convention clash;
  cy_twisted_holography_k3e_engine.py rank-24 Heisenberg convention
  clash).  Neither is an AP94 violation proper; both concern
  ChirHoch^1 conventions across engines.
- **All other Gelfand-Fuchs mentions** in the non-excluded compute
  layer are refutation-context citations that should remain.

The compute layer is CLEAN of active AP94/AP95/AP96/AP97/AP98
polynomial-ring violations in non-excluded files after this sweep.
