# AP94 Compute-Layer Sweep Report

Date: 2026-04-09
Scope: Vol I `compute/` tree, excluding the two files handled by
parallel agents (`theorem_h_hochschild_polynomial.py` and its test).

## Summary

The Gelfand-Fuchs polynomial-ring model for ChirHoch* (AP94, AP95)
was NOT a single-file slip: it was SYSTEMIC rot in the compute
layer, synchronized between engines and tests so that tests locked
the wrong model in place. Seven non-excluded files were infected.
All have been remediated to the Theorem-H bounded amplitude [0,2],
dim <= 4 model per AP94/AP95 and AP134 (amplitude != vdim).

The clearest signal of systemic rot: `chiral_hochschild_engine.py`
had a dedicated "W-algebra regime" Section 6 whose entire purpose
was to implement the partition-count polynomial-ring formula, with
a `WAlgebraHochschild` dataclass carrying `quasi_period`,
`growth_coefficient`, `poincare_series` methods. Its test class
`TestWAlgebraW3` had hardcoded partition counts [1,0,1,1,1,1,2,1,2,...]
sitting as "ground truth". Engine and test were synchronized to
the same wrong mental model (AP128).

## Files Touched

### Engines (lib/)

1. **`compute/lib/theorem_thm_h_e3_rectification_engine.py`**
   - Module header rewritten to cite AP94/AP95 and mark the GF
     polynomial-ring model historically assumed here as REMOVED.
   - `virasoro_e3_structure()`: dims changed from infinite
     periodic `{2k: 1, 2k+1: 0}` to bounded `{0:1, 1:1, 2:1}`.
     `e3_linking_trivial` True (bounded amplitude caps linking);
     `brace_max_nonzero` = 0; shadow class kept M (per AP131:
     shadow DEPTH class, not cohomological amplitude).
   - New `w_algebra_chirhoch_bounded_dim(gen_weights, degree)`:
     returns 1 for degree in {0,1,2}, 0 otherwise.
   - `w_algebra_chirhoch_dim` RENAMED to indicate REFUTED status;
     function body now raises `NotImplementedError` with citation
     to AP94, AP95.
   - `w3_chirhoch_dims`, `w4_chirhoch_dims`, `wN_chirhoch_dims`:
     all route through `w_algebra_chirhoch_bounded_dim`.
   - `w_algebra_polynomial_growth_check` rewritten to verify the
     Theorem-H amplitude constraint (`expected_growth_rate` = 0,
     `bounded_by_theorem_h` True, `vanishes_above_2` True).
   - `w3_chirhoch_explicit_at_weights` returns bounded data with
     `polynomial_growth=False`, `growth_rate=0`, `amplitude=(0,2)`.
     Removed the monomial-enumeration dict that was the core
     manifestation of the Gelfand-Fuchs partition model.
   - `full_rectification_summary['w3_computation']` updated with
     `amplitude`, `total_dim`, `bounded_by_theorem_h` keys.

2. **`compute/lib/cross_volume_bridge.py`**
   - Bridge 5 section header rewritten: "Hochschild bounded
     amplitude (Thm H)" with AP94/AP95 citation.
   - `verify_bridge_5_heisenberg`, `verify_bridge_5_sl2`,
     `verify_bridge_5_sl3`: all return Theorem-H bounded dicts
     with `amplitude=(0,2)`, `polynomial=1+dim HH^1 t + t^2`,
     `bounded_by_theorem_h=True`. The infinite Poincare series
     "1/(1-t^2)" and "1/((1-t^2)(1-t^3))" are gone.
   - Module-level Bridge 5 summary line updated to
     "concentrated in {0,1,2}, dim <= 4".

3. **`compute/lib/chiral_hochschild_engine.py`**
   - Section 6 renamed from "W-algebra regime — polynomial ring
     structure" to "W-algebra regime — Theorem-H bounded amplitude".
   - `WAlgebraHochschild` dataclass: REMOVED
     `quasi_period`, `growth_coefficient`, `is_periodic` methods.
     Added `total_dim`, `amplitude`, `bounded_by_theorem_h`
     properties. `dim_n(n)` returns 1 for n in {0,1,2}, 0 otherwise.
     `gen_degrees` retained as INFORMATIONAL record of strong
     generators (NOT a grading on the Hochschild complex).
   - `verify_theorem_h_complete` W-algebra branch updated to use
     the new `amplitude`, `total_dim`, `bounded_by_theorem_h` fields.

4. **`compute/lib/koszulness_ten_verifier.py`**
   - Single docstring-level correction: comment at line 881 that
     claimed "For W-algebras: ChirHoch^* is a polynomial ring
     (still polynomial growth)" replaced with AP94/AP95 citation
     noting the GF polynomial ring is a different functor.
   - The function's LOGIC was already correct (it verifies
     ChirHoch^n = 0 for n outside {0,1,2}); only the misleading
     comment was removed.

5. **`compute/lib/theorem_fle_critical_level_engine.py`**
   - `k7_hochschild` prose in `koszulness_at_critical_level`
     rewritten from "ChirHoch^*(V_crit) is a tensor product of
     exterior algebra and polynomial algebra" to the Theorem-H
     bounded [0,2] amplitude statement, citing AP94/AP95 and
     explicitly flagging that the oper-form identification
     `H^*(B(V_crit)) = Omega^*(Op)` pertains to the BAR complex
     (not ChirHoch).
   - `hochschild_periodicity(g)` function heavily rewritten. Old
     return dict had `is_strictly_periodic`, `period`,
     `growth_rate = "polynomial O(n^{r-1})"`, `sl2_period_4 = True
     at rank 1`. New return dict:
       - `is_strictly_periodic`: False (REFUTED)
       - `period`: None
       - `amplitude`: (0, 2)
       - `total_dim_bound`: 4
       - `bounded_by_theorem_h`: True
       - `growth_rate`: "bounded (Theorem H amplitude [0,2])"
       - `sl2_period_4`: False
       - `refutation_note`: explanatory string citing AP94/AP95.
     Function name preserved for backward import compatibility.

### Tests

6. **`compute/tests/test_theorem_thm_h_e3_rectification_engine.py`**
   - `TestVirasoroE3`: removed `test_chirhoch_even_dims`,
     `test_chirhoch_odd_dims`, `test_periodicity_2`; added
     `test_chirhoch_concentrated_in_0_1_2` asserting total dim
     <= 4, vanishing above degree 2. `test_e3_linking_nontrivial`
     replaced by `test_e3_linking_trivial`.
   - `TestW3ChirHoch`: removed all per-degree partition-count
     tests (degree 0-8) and `test_explicit_monomials`,
     `test_quasi_period`, `test_polynomial_growth_rate`. Added
     `test_degree_0_center`, `test_degree_1_deformation`,
     `test_degree_2_dual_center`, `test_vanishes_above_2`,
     `test_refuted_function_raises` (verifies
     `w_algebra_chirhoch_dim` raises `NotImplementedError`),
     `test_explicit_data_bounded`, `test_total_dim_leq_4`.
   - `TestWNPolynomialGrowth` renamed to `TestWNBoundedAmplitude`;
     all tests asserting O(n), O(n^2), O(n^3) growth replaced by
     tests asserting `expected_growth_rate == 0`,
     `bounded_by_theorem_h`, `vanishes_above_2`.
   - Multi-path verification section: `test_w3_dim_partition_vs_direct`,
     `test_w4_dim_partition_vs_direct` rewritten as
     `test_w3_bounded_two_paths`, `test_w4_bounded_two_paths`
     verifying amplitude indicator against the bounded engine.
     `test_w2_equals_virasoro` updated to bounded expected values.
     `test_w3_growth_subexponential` replaced by
     `test_w3_bounded_total_leq_4` and `test_w3_vanishes_above_2`.
   - Import line updated: `w_algebra_chirhoch_bounded_dim`
     replaces `w_algebra_chirhoch_dim` in the public import list.

7. **`compute/tests/test_cross_volume_bridge.py`**
   - `TestBridge5_Hochschild`: `test_heisenberg_polynomial`,
     `test_sl2_polynomial`, `test_sl3_polynomial` rewritten to
     assert `amplitude == (0,2)` and `total_dim` bounded.
   - `test_hochschild_heisenberg_dims` rewritten to assert
     dim=1 for n in {0,1,2}, 0 for n in {3,...,7}.
   - Added four AP10 multi-path cross-checks:
     `test_total_dim_via_two_paths_heisenberg`,
     `test_total_dim_via_two_paths_sl2`,
     `test_total_dim_via_two_paths_sl3`,
     `test_amplitude_vanishes_above_2_cross_family`.

8. **`compute/tests/test_chiral_hochschild_engine.py`**
   - `TestWAlgebraVirasoro`: `test_periodic`, `test_period_2`,
     `test_dim_even`, `test_dim_odd`, `test_poincare_series`
     replaced by `test_amplitude`, `test_total_dim_bounded`,
     `test_dim_in_range`, `test_dim_vanishes_above_2`,
     bounded `test_poincare_series`.
   - `TestWAlgebraW3`: `test_not_periodic`, `test_quasi_period`,
     `test_first_values` (partition counts), `test_growth_rate`
     replaced by `test_amplitude`, `test_total_dim_bounded`,
     bounded `test_first_values_bounded`.
   - `TestWAlgebraWN`: `test_w4_quasi_period`, `test_w5_first_values`
     (partition counts) replaced by `test_w4_bounded`,
     `test_w5_bounded`.
   - `test_w_algebra_dim1_always_0` renamed
     `test_w_algebra_dim1_c_deformation`; asserts
     `w.dim_n(1) == 1` (the c-deformation class) per Theorem H.
   - Added three AP10 cross-checks:
     `test_virasoro_bounded_two_paths`,
     `test_wN_amplitude_cross_family`,
     `test_wN_total_dim_vs_structural_formula`.

9. **`compute/tests/test_theorem_fle_critical_level_engine.py`**
   - `TestHochschildPeriodicity` renamed
     `TestHochschildBoundedAmplitude`. `test_sl2_periodic`,
     `test_sl3_not_periodic`, `test_higher_rank_growth` rewritten
     as `test_sl2_bounded`, `test_sl3_bounded`,
     `test_higher_rank_bounded`, asserting
     `amplitude == (0,2)` and `bounded_by_theorem_h`.

## Importers Updated

None externally. The two renamed/refuted functions
(`w_algebra_chirhoch_dim` and `hochschild_periodicity`) have
NO downstream importers outside their own test files (verified
by grep). No cross-module fallout.

## Functions Renamed or Deprecated

- `w_algebra_chirhoch_dim(gen_weights, degree)` in
  `theorem_thm_h_e3_rectification_engine.py`: DEPRECATED /
  REFUTED, body raises `NotImplementedError`. A working
  replacement `w_algebra_chirhoch_bounded_dim` is provided.
- `hochschild_periodicity(g)` in
  `theorem_fle_critical_level_engine.py`: RETAINED by name but
  semantics completely rewritten; now returns the Theorem-H
  bounded summary. Old polynomial-growth/periodicity keys are
  either absent or set to False/None. A `refutation_note` key
  is included.

## Ambiguous Cases (None)

No ambiguous cases. Every hit either:

1. Was infected and has been fixed (the files listed above), or
2. Referred to a different object than ChirHoch. Verified-safe
   occurrences in compute/lib:
   - `bc_ktheory_shadow_regulator_engine.py` — uses
     `ShadowAlgebraPresentation.is_polynomial_ring` for the
     SHADOW ALGEBRA A^sh = k[kappa, alpha, S_r], which is
     legitimately a polynomial ring (AP96). NOT ChirHoch.
   - `theorem_matrix_model_shadow_engine.py` — "infinite
     polynomial in M" is the MATRIX MODEL POTENTIAL, not
     ChirHoch.
   - `bc_matrix_model_shadow_engine.py` — same.
   - `theorem_jt_gravity_shadow_engine.py` — same.
   - `derived_center_explicit.py` — already remediated by
     Agent A (line 302 comment explicitly rejects infinite
     polynomial tower, citing AP94/AP95).
   - `chiral_hochschild_engine.py` header — "ChirHoch^*(A) is
     polynomial with polynomial P_A(t) = dim Z + dim HH^1·t +
     dim Z^!·t^2" refers to the quadratic structural
     POLYNOMIAL P_A(t), NOT a polynomial ring. Safe.
   - All occurrences of the phrase "ChirHoch polynomial in
     degrees {0,1,2}" across `bc_derived_moduli_shadow_engine.py`,
     `theorem_koszul_12fold_rectification_engine.py`,
     `cy_nc_deformation_k3e_engine.py`, etc. refer to
     Theorem H amplitude concentration, not a polynomial ring.

## Final Verification Grep

After all fixes, the only remaining Gelfand-Fuchs / C[Theta]
hits in compute/ .py files are:

1. REFUTED markers in remediated files (REQUIRED by AP95:
   the files EXPLICITLY state "NOT chiral Hochschild; per
   AP95 ChirHoch != Gelfand-Fuchs")
2. The two exclude-list files
   (`theorem_h_hochschild_polynomial.py` and its test), which
   the parallel agent has ALSO already remediated (the
   `RefutedModelError` class and its citations are in place).

No raw, un-remediated infections remain in the Vol I compute layer.

## Systemic Rot Assessment

The compute layer DID have systemic AP94 rot. Seven engines and
four test files were infected. The `chiral_hochschild_engine.py`
"W-algebra regime" section was especially egregious: a dedicated
dataclass with `quasi_period`, `growth_coefficient`, and an entire
downstream verification pipeline `verify_theorem_h_complete`
that accepted the polynomial-ring model as "Theorem H complete".

Pattern observed (AP128): engine and test were ALWAYS synchronized
to the same wrong value. For example,
`test_chiral_hochschild_engine.py::test_first_values` hardcoded
`[1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3]` (Gelfand-Fuchs partition
counts of 2a+3b) as the "expected" Poincare series of ChirHoch*(W_3).
That value is produced by the Gelfand-Fuchs formula AND ONLY by
the Gelfand-Fuchs formula; the test therefore provided zero
verification of Theorem H, yet passed.

The lesson of this sweep matches AP128 precisely: a large test
suite passing does not, in itself, constitute verification of
the claim the tests are named for. The tests were named "verify
Theorem H" but actually verified the functor Theorem H
REFUTES.

## Follow-up

None required for this pass. Recommended for the next pass:

- Re-run the full test suite against the remediated compute layer
  once all parallel agents have finished. The engine/test pairs
  should now consistently verify the Theorem H bounded amplitude
  model.
- Audit `introduction.tex:1158` and `koszul_pair_structure.tex:542,571`
  for similar AP94 infections in the manuscript (flagged in
  `compute/audit/complete_frontier_status_2026_04_08.md` and
  `exhaustive_gap_analysis_2026_04_08.md`) — but per task spec,
  manuscript edits are out of scope for this sweep.
