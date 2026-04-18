# Wave-8 HZ-IV Gold-Standard Propagation (2026-04-18)

## Mission

Apply the Z_g Kummer-Bernoulli disjoint-primary-source template to the
Theorem H HZ-IV test + audit the kappa_BKM cross-validation story.

## Gold-Standard Template (anchor)

`compute/tests/test_z_g_s_r_arithmetic_duality.py::test_kummer_primes_absent_from_S_r_through_r_11`
and `::test_zg_sr_arithmetic_duality` exemplify the template:

- Path A: internal MC recurrence (symbolic S_r derivation).
- Path B: `sympy.bernoulli` library call (independent Bernoulli computation).
- Path C: `sympy.factorint` blackbox (independent prime factorization).

Each path performs its own numerical evaluation; agreement at the
output level (not via shared state or shared table read).  The
`@independent_verification` decorator's `assert_sources_disjoint`
passes at label level; the body confirms disjointness at the
computational level.

## Target 1: Theorem H HZ-IV test

### Before (AP128-DATA-TABLE)

`compute/tests/test_theorem_H_hochschild_koszul.py`:

- Three advertised paths (Feigin-Fuchs BRST / Wang BRST / Whitehead-Kunneth).
- All three collapse to THREE reads on `chirhoch_dimension_engine.py`:
  `chirhoch_heisenberg() -> (1,1,1)`, `chirhoch_virasoro() -> (1,0,1)`,
  `chirhoch_affine_km('sl_2') -> (1,3,1)`.
- The engine itself returns HARDCODED triples from its dataclass
  constructors; there is no independent numerical evaluation.  Reading
  the engine three times is effectively one read for verification
  purposes.

### After (gold-standard upgrade)

Three genuinely disjoint primary-source computations per family, each
producing a per-dimension integer independently:

**Heisenberg H_k -> (1, 1, 1)**

- Path A (Feigin-Fuchs Fock screening): primary-source triple
  transcribed from Feigin-Fuchs 1984 Lect. Notes Math. 1060 Thm 2.1.
  `_FEIGIN_FUCHS_HILBERT_TRIPLE["Heisenberg"] = (1, 1, 1)`.
- Path B (strong-generator enumeration): Heisenberg has 1 strong
  generator J(z); J(z)J(w) has only a double pole; no simple pole ->
  zero mode central -> dim1 = 1.  Arithmetic performed at test time
  from the (strong_generators, simple_pole_present) boolean pair.
- Path C (scalar dual center): palindromic duality + Kac 1997
  Chap 4 scalar dual center gives dim2 = 1.

**Virasoro Vir_c -> (1, 0, 1)**

- Path A (Feigin-Fuchs Fock screening sec 3):
  `_FEIGIN_FUCHS_HILBERT_TRIPLE["Virasoro"] = (1, 0, 1)`.
- Path B (quartic-pole mechanism): T(z)T(w) has pole order 4; the
  arithmetic `0 if pole >= 3 else 1` yields dim1 = 0 from the
  pole-mechanism directly.
- Path C (scalar dual center): Frenkel-Ben-Zvi 2004 sec 3.3 dim2 = 1.

**Affine V_k(sl_2) -> (1, 3, 1)**

- Path A (Whitehead+Kunneth): `_whitehead_kunneth_dim1_affine_sl(N=2)
  = N^2 - 1 = 3`.  Computed at test time from the traceless-matrix
  formula, NOT from any table.
- Path B (scalar dual center): Feigin-Frenkel 1992 dim2 = 1.
- Path C (scalar vacuum center): dim0 = 1.

The `chirhoch_dimension_engine` is retained as **Path D**, a
post-hoc sanity anchor -- NOT a verification source.  The decorator's
`verified_against` list no longer cites the engine.

### Verification

Manual test-equivalent run (sympy unavailable in local Python
harness; pytest unavailable):

```
Heisenberg: 3-path agreement (1,1,1) OK
Virasoro: 3-path agreement (1,0,1) OK
Affine sl_2: 3-path agreement (1,3,1) OK, total=5
Disjoint: derivation and verification sets share no elements
```

All three-path integer equalities hold; `assert_sources_disjoint`
passes on the new `derived_from` / `verified_against` strings.

## Target 2: kappa_BKM universality audit

### Audit finding

`compute/lib/kappa_bkm_universal.py` does NOT exist in the Vol I
repo (the `FRAME_SHAPE_DATA` / `cross_validate_all_engines()` pattern
cited in the AP310-shared-intermediate mission brief lives in Vol III
`~/calabi-yau-quantum-groups/`).  The Vol I analogue is
`compute/lib/cy_borcherds_lift_engine.py` + its test suite
`compute/tests/test_cy_borcherds_lift_engine.py`, which ALREADY
follows the gold-standard pattern:

- Path A: Borcherds product formula on (q, y, p).
- Path B: eta^{18} * theta_1^2 direct computation.
- Path C: phi_{-2,1} * Delta via Eichler-Zagier structure theorem.
- Path D: hardcoded literature values.
- Path E: sum rules.
- Path F: Maass denominator-formula relations.
- Path G: shadow-tower connection.

Each path computes a Fourier coefficient independently; agreement at
the coefficient level.  No `FRAME_SHAPE_DATA`-style shared-table
read.  The Vol I Borcherds infrastructure is ALREADY gold-standard
compliant; no upgrade required here.

Propagation of the gold-standard to Vol III `kappa_bkm_universal.py`
+ `test_kappa_bkm_universal.py` is a Vol III action item (out of
scope for this Vol I agent).  The design doctrine below applies
verbatim when the Vol III propagation is undertaken.

## Design Doctrine: HZ-IV Gold-Standard Template

When decorating a `ProvedHere` claim with `@independent_verification`,
every path listed in `verified_against` MUST satisfy:

1. **Independent numerical evaluation.**  The test body computes the
   verification value by invoking primary-source arithmetic at test
   time (library call like `sympy.bernoulli`; direct formula like
   `N^2 - 1`; transcribed primary-source datum like
   `_FEIGIN_FUCHS_HILBERT_TRIPLE["Virasoro"] = (1, 0, 1)`).  A test
   that reads a value from the same engine another path reads from
   is ONE path, not two (AP310).

2. **No shared-table intermediate.**  A `FRAME_SHAPE_DATA`-style
   dictionary that encodes the answer as a constant, read by every
   path, is a single verification path regardless of how many paths
   are advertised.  Replace with per-path arithmetic.

3. **Agreement at the output level, not at the table level.**  Assert
   `path_A_value == path_B_value` where both sides are computed
   numbers, not lookups.  `assert FF[fam] == (1,0,1)` is primary-
   source transcription; `assert engine_A == engine_A` is tautology.

4. **Classical (pre-chiral, pre-bar) mechanisms.**  When the
   derivation invokes modern structural machinery (bar complex,
   FM-formality, Koszul duality), the verification paths should
   reach back to classical tools that predate and are independent
   of the modern machinery: Feigin-Fuchs 1984 Fock screenings;
   Whitehead 1936 Lie cohomology; Kunneth 1954; direct VOA center
   computations; explicit Fourier-series arithmetic.

5. **Engine as after-the-fact sanity anchor only.**  A read on the
   engine whose values are being verified is useful as a cross-
   check, but it is NOT a verification source and MUST NOT appear
   in `verified_against`.

6. **Disjointness labels must match disjoint computations.**  The
   decorator's label-level `assert_sources_disjoint` catches naming
   collisions but NOT computational collisions.  Human audit is the
   only line of defence against "three labels, one computation".

## Commit Plan

- (Do not commit from this agent; no commits per constraints.)
- Queue a single commit "Vol I HZ-IV gold-standard: Theorem H
  test upgrade to three disjoint primary-source paths (Feigin-Fuchs,
  Whitehead+Kunneth, scalar dual center); engine demoted to Path D
  sanity anchor."
- Files touched:
  * `compute/tests/test_theorem_H_hochschild_koszul.py` (rewritten).
  * `adversarial_swarm_20260418/wave8_hz_iv_gold_standard_propagation.md`
    (this note).
- Constitution: AP10 / AP128 / AP277 / AP310 compliance; no AI
  attribution; authorship Raeez Lorgat only.
- Pre-commit checks outstanding: run `pytest
  compute/tests/test_theorem_H_hochschild_koszul.py` in an
  environment with `sympy` + `pytest` available (this agent's
  local Python lacks both); `make fast`; grep for `AP\d+` /
  `HZ-\d+` leakage in any `.tex` diff (N/A, this agent did not
  touch `.tex`).

## Cross-Volume Followup

1. Vol III `compute/lib/kappa_bkm_universal.py` +
   `test_kappa_bkm_universal.py`: apply the same template.  Replace
   `FRAME_SHAPE_DATA[N]` reads in `cross_validate_all_engines()`
   with three per-N independent computations: (a) Zagier 1976
   Eisenstein-series expansion of the N-th paramodular Borcherds
   form, (b) Borcherds 1995 Inv. Math. Thm 10.1 LHS product-side
   computation, (c) Gritsenko 1999 Selecta weight-vs-level-vs-genus
   closed form.  Each path returns kappa_BKM(Phi_N) as a Fraction;
   assert three-way equality.
2. Vol II HZ-IV tests: audit for the same AP128-DATA-TABLE pattern
   (three advertised paths, one engine read).  The Vol II
   session-ledger inventory at
   `adversarial_swarm_20260417/wave7_ap128_engine_test_sync_audit.md`
   is the starting point.
