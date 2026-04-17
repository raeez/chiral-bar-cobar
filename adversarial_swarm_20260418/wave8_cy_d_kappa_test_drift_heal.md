# Wave-8 Heal: Vol III `test_cy_d_kappa_stratification.py` AP238 Igusa-Gritsenko weight drift

**Date.** 2026-04-18.
**AP classes.** AP238 (statement/proof internal contradiction), AP245 (statement-proof-engine agreement), AP283 (formula confabulation in status narrative), AP310.
**Severity.** CRITICAL three-way drift — test file vs chapter vs engine vs CLAUDE.md CY-D row.
**Scope.** Targeted heal to Vol III test file only. No commit.

## Drift profile (pre-heal)

The test file `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_cy_d_kappa_stratification.py` carried doubled Borcherds weight values at N=1 and N=2, conflating:

- **Correct (Gritsenko 1999 Selecta):** Δ_5, paramodular cusp form, level 1, weight 5; c_1(0) = 10; κ_BKM(Δ_5) = c_1(0)/2 = 5.
- **Incorrect (drifted):** Igusa Φ_10, Siegel genus-2 cusp form, level 1, weight 10; c(0) = 20.

Φ_10 is a Siegel form on Sp(4, Z); Δ_5 is a paramodular form on the degree-1 paramodular group K(1). They are DIFFERENT modular forms on DIFFERENT groups with a factor-of-2 weight relation via pullback. The test file labelled the Borcherds-weight column with the Φ_10 weights.

Analogous drift at N=2: healed 12 → 8 at c_2(0) and 6 → 4 at weight (per Allcock 2000 + Gritsenko-Nikulin 1998 "Automorphic forms and Lorentzian KM algebras II").

The canonical values appear in the engine `compute/lib/diagonal_siegel_cy_orbifolds.py::FRAME_SHAPE_DATA`:

```
N=1: c_disc_0 = 10, borcherds_weight = 5
N=2: c_disc_0 =  8, borcherds_weight = 4
N=3: c_disc_0 =  6, borcherds_weight = 3
N=4: c_disc_0 =  4, borcherds_weight = 2
N=6: c_disc_0 =  2, borcherds_weight = 1
```

Chapter `cy_d_kappa_stratification.tex:1163` canonical. CLAUDE.md CY-D row canonical. Only the test file drifted.

## Heals applied (four surgical edits)

1. **`test_borcherds_weights_universal` (line 437-448).** Docstring rewritten to cite Gritsenko 1999 Selecta + Allcock 2000 + Gritsenko-Nikulin 1998 "Automorphic forms and Lorentzian KM algebras II" with retraction note flagging the prior Gritsenko-Hulek-Sankaran 2008 Φ_10 mislabel. Table:
   - `(1, 20, 10)` → `(1, 10, 5)`
   - `(2, 12, 6)` → `(2, 8, 4)`
   - N=3, 4, 6 rows unchanged (already correct).

2. **`test_N1_naive_decomposition_fails` (line 457).**
   - `N1_weight = F(10)` → `F(5)`.
   - Docstring retitled "κ_BKM(Δ_5) = 5" with retraction note.
   - Assertions still fire: `xi(K3xE) + xi(E) = 0 + 0 = 0 != 5`. Test meaningfully falsifies naive decomposition.

3. **`test_N2_kummer_decomposition_fails` (line 467).**
   - `N2_weight_from_c0 = F(12, 2)` → `F(8, 2)` (evaluates to F(4)).
   - `assert N2_weight_from_c0 == F(6)` → `assert N2_weight_from_c0 == F(4)`.
   - Assertions still fire: naive = 1 ≠ 4. Test meaningfully falsifies naive Z_2 orbifold decomposition.

4. **`test_c_N_strictly_positive` (line 490).**
   - `c_N_zero = {1: 20, 2: 12, 3: 6, 4: 4, 6: 2}` → `{1: 10, 2: 8, 3: 6, 4: 4, 6: 2}`.
   - Test was passing with the drifted values (all positive) but carried the wrong table; healed for consistency.

5. **HZ-IV `@independent_verification` decorator (line 411-422).** `verified_against[1]` prose updated:
   - Old: "Gritsenko-Hulek-Sankaran 2008 Moduli of K3 Chapter 5 independently listing paramodular weights {10, 6, 3, 2, 1}".
   - New: "Gritsenko 1999 Selecta + Allcock 2000 + Gritsenko-Nikulin 1998 independently listing paramodular weights {5, 4, 3, 2, 1}".
   - `disjoint_rationale` rewritten with matching citation and weight set.

## Verification (engine cross-check)

Without pytest in environment, direct-import verification under `python@3.14`:

```
N=1: engine c_disc_0=10 weight=5  -- MATCH test
N=2: engine c_disc_0=8  weight=4  -- MATCH test
N=3: engine c_disc_0=6  weight=3  -- MATCH test
N=4: engine c_disc_0=4  weight=2  -- MATCH test
N=6: engine c_disc_0=2  weight=1  -- MATCH test
engine-test agreement PASS
```

All four healed test bodies evaluated standalone — every assertion passes; the naive-decomposition tests retain their meaningful falsification (5 ≠ 0 at N=1; 4 ≠ 1 at N=2).

## Residual open

- **17 other Vol III test files match the regex `(1,\s*20,\s*10)|(2,\s*12,\s*6)|Phi_10.*weight|kappa_BKM.*=.*10`** (test_cy_c_six_routes_generator_level.py, test_hyperkahler_anchored_fixed_point.py, test_hyperkahler_BKM_lift.py, test_cy_c_pentagon_hypothesis_closures.py, test_siegel_genus3.py, test_elliptic_hall_hocolim.py, test_twisted_holography_k3e.py, test_sp4_modularity_pipeline.py, test_modular_koszul_bridge_k3e.py, test_kappa_spectrum_reconciliation.py, test_kappa_bkm_adversarial.py, test_k3e_e1_product_chain.py, test_genus2_k3e_full.py, test_genus2_chiral_partition.py, test_categorical_s_matrix_e3.py, test_bkm_chiral_algebra.py). Most hits likely legitimate (Φ_10 is the genuine Igusa form in Siegel-genus-2 contexts, distinct from paramodular Δ_5) or unrelated tuple coincidences — out of scope for this targeted heal; flagged for Wave-9 triage.
- **CLAUDE.md CY-D row** already canonical (κ_BKM(Φ_1) = 5 via Gritsenko Δ_5). No further edit needed.
- **Chapter `cy_d_kappa_stratification.tex`** already canonical per Wave-4 Vol III CY-D agent heals (B94 + AP289 campaign, 2026-04-17).
- Docstring at line 430 still references "Gritsenko-Hulek-Sankaran 2008 Moduli of K3 Chapter 5" wording as prior-state citation in the retraction note — retained deliberately to preserve the AP-retraction audit trail.

## Commit plan

Not committed. Single-file surgical heal awaiting parent-session batch commit. Atomic diff available via `git diff compute/tests/test_cy_d_kappa_stratification.py` in `~/calabi-yau-quantum-groups`.

## Attribution

Gritsenko, V. "Modular forms and moduli spaces of abelian and K3 surfaces", St. Petersburg Math. J. 6 (1994); Selecta Math. 5 (1999) for Δ_5.
Borcherds, R. E. "Automorphic forms on O_{s+2,2}(R) and infinite products", Inventiones Math. 120 (1995) Theorem 10.1 (weight = c(0)/2).
Allcock, D. "The Leech lattice and complex hyperbolic reflections", Inventiones Math. 140 (2000) for N=2 paramodular weight 4.
Gritsenko, V. & Nikulin, V. "Automorphic forms and Lorentzian Kac-Moody algebras II", Int. J. Math. 9 (1998).
