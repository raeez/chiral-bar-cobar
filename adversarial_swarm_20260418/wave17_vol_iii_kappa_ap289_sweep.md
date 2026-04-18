# Wave-17 Vol III AP289 Comprehensive Sweep — κ_ch(K3 × E) Route A/B discipline

Date: 2026-04-18. Scope: Vol III `compute/tests/`. Policy: no commits; report only.

## 1. Two Wave-16 Tier-3 flagged sites — RE-VERIFICATION

### Site 1: `test_twisted_holography_k3e.py:168-181`

Read lines 148-195 in context. Verdict: **Wave-10 disambiguation INTACT and SUFFICIENT.**

Docstring explicitly states:
- Line 170: `Route B (Heisenberg level / free-boson rank, AP-CY55 algebraisation invariant)`
- Line 171: `kappa_ch(E) = 1 via k = 1 Heisenberg level`
- Line 173-174: contrasts Route A (Hodge supertrace, Künneth-multiplicative, Ξ(K3×E)=0)
- Line 175-176: canonical Φ_d value is 0 per `cy_d_kappa_stratification.tex:411-426`
- Line 177: explicit AP234 disambiguation

No edit needed. Wave-16 Tier-3 flag is a false positive from keyword-grep; the Route B context is present and load-bearing.

### Site 2: `test_hyperkahler_anchored_fixed_point.py:4286-4287`

Read lines 4266-4315 in context. Verdict: **Wave-10 disambiguation INTACT.**

Class docstring (4269-4289):
- Line 4272: `Route B: Heisenberg-level additive, 2 + 1`
- Line 4277-4281: Route A vs Route B explicit AP234 disambiguation, cites `cy_d_kappa_stratification.tex:411-426`
- Line 4282-4283: "proposition here operates under Route B; Route A coexists"

HZ-IV decorator fields (4294-4297) carry the additive identity in `derived_from`; the docstring context justifies it as Route B. Minor refinement opportunity: line 4286 reads `additivity κ_ch(K3) + κ_ch(E) = 2 + 1 + Borcherds weight` — the `+ Borcherds weight` is a sentence join, not arithmetic; a comma clause would read cleaner but this is cosmetic.

**Conclusion on the two Wave-16-flagged sites**: Wave-10 classification is correct. Wave-16 Tier-3 surfaced them via pattern-match; closer reading shows the Route B discipline is intact. NO edit required; NO rename to `κ_ch^{Heis}` needed — the H3 two-subscript split is not yet programme-canonical, and these sites already disambiguate via prose.

## 2. BROADER SWEEP — Vol III test files with `κ_ch(X × Y) = κ_ch(X) + κ_ch(Y)` pattern

Grep `kappa_ch.*\+.*kappa_ch|KAPPA_CH.*\+.*KAPPA_CH` across `compute/tests/` yields two categories:

### Category A — Koszul complementarity `κ_ch(A) + κ_ch(A^!) = ρ_K` (~30 files)
These are NOT product-additivity; they are DUALITY-additivity (self-dual via `(-)^!`). NOT an AP289 pattern. Files: `test_holomorphic_cs_chiral_engine.py`, `test_derived_vs_drinfeld_infty.py`, `test_drinfeld_center_*.py`, `test_e1_koszul_three_families.py`, `test_e2_koszul_*.py`, `test_e3_koszul_*.py`, `test_chiral_koszul_derived.py`, `test_ade_yangian_level1.py`, `test_cfg25_*.py`, `test_costello_5d_verification.py`, `test_costello_paquette_defect_chiral.py`, `test_defect_koszul_dag.py`, `test_quintic_shadow_tower.py`, `test_categorical_s_duality.py`, `test_form_factors_shadow_pf.py`, `test_cy_b_d3_final.py`. SKIP.

### Category B — Product-additivity `κ_ch(X × Y) = κ_ch(X) + κ_ch(Y)` — AP289 RELEVANT

~30 Vol III test files carry `κ_ch(K3 × E) = 2 + 1 = 3` (or `Enr × E = 2`, `E × E = 2`, `K3 × E × E = 4`, `K3^{[n]} = n+1`) additivity. Distribution by Route-B-disambiguation status:

**B1 — EXPLICIT Route B disambiguation (Wave-10-healed, OK):**
- `test_twisted_holography_k3e.py:168-181` (Site 1 above) — AP234, Route A vs B
- `test_hyperkahler_anchored_fixed_point.py:4269-4289` (Site 2 above) — AP234, Route A vs B

**B2 — PARTIAL disambiguation (chiral-de-Rham or GS additivity named, but no Route A vs B contrast):**
- `test_modular_koszul_bridge_k3e.py:76, 101` ("chiral de Rham additivity")
- `test_modular_cy_characteristic.py:384` ("kappa_ch IS additive")
- `test_k3_elliptic_genus_bkm_bar.py:134, 363` (contrasts κ_BKM=5 vs κ_ch=3, implicit Route B)
- `test_cy_c_six_routes.py:141` (`κ_ch^{R1}` superscript — route-explicit)
- `test_anomaly_shadow_consistency.py:411` ("from GS additivity")
- `test_ptvv_derived_k3e.py:340, 384` (Künneth-named but additive value)
- `test_cy_cd_post_cya3.py:293` ("by additivity: 2 + 1")
- `test_hcs_vs_sigma_adversarial.py:380` ("Route D" — distinct routing)
- `test_bar_hocolim_chain_level.py:901` (kappa of 2D CY product, κ(E)=1 convention)

**B3 — BARE additive assertion (NO Route A/B disambiguation):**
- `test_kappa_ch_d3_formula.py:142, 148, 152, 158, 179, 276, 436, 442` (most-violated file; d=3 product additivity pervasive)
- `test_defect_koszul_dag.py:199`
- `test_pixton_cy_bar_connection.py:333`
- `test_k3e_abelian_pushforward.py:257-258`
- `test_fermat_quartic_k3_chiral.py:745, 768, 816, 820`
- `test_kappa_consistency_adversarial.py:114, 285`
- `test_cy_d_kappa_d3.py:384, 389, 404`
- `test_phi_k3_explicit.py:270`
- `test_cy_d_d4_kappa.py:133, 432, 435`
- `test_k3e_relative_chiral_algebra.py:208, 243`
- `test_hcs_hierarchy_k3.py:457`
- `test_anomaly_shadow_consistency.py:29, 46, 421, 427, 785, 1019`
- `test_kappa_ch_universal_formula.py:483, 485, 490, 499`
- `test_factorization_categories_chiral.py:511`
- `test_physical_k3_sigma_check.py:178`
- `test_lurie_e3_obstruction.py:340`
- `test_kappa_spectrum_reconciliation.py:194, 200`
- `test_ptvv_derived_k3e.py:386` (partial)
- `test_genus2_k3e_full.py:173`
- `test_cy_d_kappa_stratification.py:225` (HZ-IV decorator `derived_from` field)
- `test_costello_paquette_defect_chiral.py:515, 597`
- `test_cy_bar_complex_engine.py:376` (contrasts κ_BKM=5 vs additive=3, implicit Route B)

### Category C — Cross-family κ additivity NOT product-structure (`kw_twisted_n4`, `twisted_holography_non_cy`, `non_cy_local_surface`, `kappa_ch_universal_formula`):

Additive decompositions `κ_ch = κ_geom + κ_anom`, `κ_ch = κ_{sln} + κ_{gl1}`, `κ_ch = (-c_1 + dim)/2` — these are STRUCTURAL decompositions of a single algebra's κ, NOT Künneth product claims. NOT AP289.

## 3. Classification — B3 cohort is the real exposure

B3 contains **~30 sites** across **~20 files** where bare additivity is asserted without the Route A/B discipline. All operate under the IMPLICIT Route B (AP-CY55 algebraisation / Heisenberg-level convention), consistent with Wave-10's finding that Route B is the DOMINANT convention in Vol III working practice. The tests PASS because they are internally consistent with Route B; the discipline gap is documentary, not mathematical.

Key observation: `cy_d_kappa_stratification.tex` chapter (Wave-4 Vol III CY-D heal) established Künneth-MULTIPLICATIVE as the canonical Φ_d functor value (AP289 core). Route B (additive at Heisenberg level) coexists as the bar-theoretic invariant. Both are mathematically correct; the discipline requires tagging.

## 4. Heals NOT APPLIED (report-only mode per instructions)

Under Wave-13 H3 two-subscript split (κ_ch^{Heis} vs κ_ch^{Xi}), the B3 cohort would rename `κ_ch` → `κ_ch^{Heis}` at each product-additive site and retain the AP234 Route A/B comment block. Under Wave-10 convention (Route B annotation), B3 sites would receive a 3-line comment matching Sites 1 and 2.

Given programme has NOT adopted H3 as canonical, the Wave-10 convention (annotation, not rename) is the appropriate heal. Estimated effort: ~30 surgical edits across ~20 files, ~5 lines each (insert AP234 comment block).

## 5. Grep gate BEFORE / AFTER

BEFORE: `grep -rn 'kappa_ch.*=.*kappa_ch.*+.*kappa_ch' compute/tests/` → ~30 hits (B2 + B3).
Partial-disambiguation (B2): ~8. Bare (B3): ~22.
AFTER proposed heal: all ~30 carry Route A vs B annotation; bare count = 0.

## 6. Commit plan (DEFERRED — report-only)

Not executing commits this wave. Recommended batching:
1. **Tier A** (highest-traffic, HZ-IV-decorated): `test_kappa_ch_d3_formula.py` (8 sites), `test_anomaly_shadow_consistency.py` (6 sites), `test_cy_d_d4_kappa.py` (3 sites). Single commit: "Vol III AP289 Route-B annotation: Tier-A high-traffic additivity sites".
2. **Tier B** (cross-cutting engines): `test_fermat_quartic_k3_chiral.py`, `test_kappa_ch_universal_formula.py`, `test_cy_d_kappa_stratification.py`. Second commit.
3. **Tier C** (remaining ~15): batched third commit.

Commit gate: `make test` full sweep in Vol III; AI-attribution grep; author = Raeez Lorgat.

## 7. Conclusion

- Wave-16 Tier-3 flags on Site 1 / Site 2 are FALSE POSITIVES; Wave-10 disambiguation is INTACT. No edit required.
- Broader sweep reveals ~22 bare-additivity sites (B3 cohort) without Route B annotation — genuine AP289 documentary gap across the Vol III test landscape.
- Mathematical correctness unaffected (all tests pass under Route B convention); discipline gap is AP234 / AP-CY68 annotation-level.
- Wave-13 H3 rename is NOT programme-canonical; Wave-10 annotation is the correct heal pattern.
- Recommend three-tier heal in a subsequent wave; this report catalogues the landscape for execution.
