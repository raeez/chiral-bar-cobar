# Wave-9 Vol III doubled-weight regex triage (AP238 paramodular drift sweep)

**Date**: 2026-04-18
**Author**: Raeez Lorgat
**Triage agent invocation**: follow-up to Wave-8 `test_cy_d_kappa_stratification.py` heal (agent a9c455fd)
**Mission**: triage Vol III test files matching regex `weight.*=.*10|weight.*=.*12|weight.*=.*20` to separate LEGITIMATE Igusa / eta-weight / κ_ch contexts from RESIDUAL paramodular drift (AP238: Gritsenko 1999 Δ_5 weight 5 at N=1 vs Igusa Φ_10 weight 10).

## Canonical Wave-8 reference (per `compute/lib/diagonal_siegel_cy_orbifolds.py:268-314`)

| N | c_N(0) | paramodular weight w(N) = c_N(0)/2 | canonical form |
|---|--------|--------|----------------|
| 1 | 10 | 5 | Δ_5 (Gritsenko 1999 level-1 paramodular cusp form) |
| 2 | 8  | 4 | Allcock 2000 Enriques paramodular product |
| 3 | 6  | 3 | Gritsenko-Nikulin 1998 N=3 orbifold |
| 4 | 4  | 2 | Gritsenko-Nikulin 1998 N=4 orbifold |
| 6 | 2  | 1 | Gritsenko-Nikulin 1998 N=6 orbifold |

Φ_10 (Siegel-Igusa level-1 weight-10 Sp_4(Z) cusp form) = Δ_5² is the NON-paramodular square; distinct form.  κ_BKM = wt(Δ_5) = 5, NEVER κ_BKM = wt(Φ_10) = 10.

## Programme-wide enumeration

`grep -rln 'weight.*=.*10\|weight.*=.*12\|weight.*=.*20' /Users/raeez/calabi-yau-quantum-groups/compute/tests/` returned **39 files**.  Triage classifies each by the underlying weight-10/12/20 meaning:

## Triage classification summary

- **LEGITIMATE — Igusa Φ_10 / χ_10 at wt=10 as the SQUARE** (consistently stated `wt(Φ_10) = 10 = 2·κ_BKM`; or weight-10 Igusa form appears in its correct Siegel-genus-2 non-paramodular context): 14 files.
- **LEGITIMATE — η^24 / η^12 modular weight at K3 / bosonic string** (weight = -c/2 = -12 at c=24, distinct from paramodular κ_BKM): 12 files.
- **LEGITIMATE — eta weight 12 at genus-2 Heisenberg, `eta_weight = 12`** (= (1/2)·24; Frame-shape lift, not κ_BKM): 4 files.
- **LEGITIMATE — `max_weight=10` / `max_weight=12` as SYMBOLIC truncation parameter for character-table expansions** (unrelated to modular weight): 4 files.
- **LEGITIMATE — `weight_Z3_heis == -12`, weight(χ_12) == 12 (Siegel genus-3 forms)**: 1 file (`test_siegel_genus3.py`).
- **RESIDUAL paramodular drift**: 1 file heal-applied (+ 2 comment-only clarifications on adjacent sites).
- **OTHER** (unrelated weight semantics): 3 files (`test_cy_b_d3_final.py:164` `c_crit=Fraction(100)`; `test_k3_abelian_yangian_currents.py:310` `phi_{0,1}.c(-1)=1`; `test_connes_b_obs_ainf.py:168` `B^{(j)} shift 1-j, j=0..10`).

## Residual paramodular drift HEALS APPLIED

### File 1: `test_cy_c_pentagon_hypothesis_closures.py` (PRIMARY drift, full heal)

**Anti-pattern**: `BORCHERDS_LIFT_WEIGHTS` dict labeled "weight w(N)" but held c_N(0) values; additionally N=2, N=3 entries numerically disagreed with Wave-8 canonical FRAME_SHAPE_DATA (claimed c_2(0)=6, c_3(0)=4; canonical is 8, 6).  Test `test_h4_lift_weight_is_even` asserted "weight is even for all relevant N" — true for c_N(0) but FALSE for three canonical paramodular weights (5, 3, 1 are odd).  Test `test_h4_lift_for_N_1_gives_weight_10_phi_10` named N=1 paramodular lift "Φ_10" — Φ_10 is Sp_4(Z) non-paramodular; N=1 paramodular is Δ_5 weight 5.

**Heal (atomic)**: (a) rewrote `BORCHERDS_LIFT_WEIGHTS` to canonical {1:5, 2:4, 3:3, 4:2, 6:1} with per-row citation comment; (b) rewrote `C_N_0_PER_N` to canonical {1:10, 2:8, 3:6, 4:4, 6:2} with per-row citation comment; (c) added Wave-8 attribution header (Gritsenko 1999 + Allcock 2000 + Gritsenko-Nikulin 1998 + FRAME_SHAPE_DATA engine); (d) renamed `test_h4_lift_weight_equals_c_N_0` → `test_h4_lift_weight_equals_half_c_N_0` with `w(N) == Fraction(c_N(0), 2)` assertion; (e) added new `test_h4_c_N_0_matches_frame_shape` asserting c_N(0) table against FRAME_SHAPE_DATA ground truth; (f) retired `test_h4_lift_weight_is_even` (false at canonical); (g) renamed `test_h4_lift_for_N_1_gives_weight_10_phi_10` → `test_h4_lift_for_N_1_is_delta5_paramodular` stating `BORCHERDS_LIFT_WEIGHTS[1] == 5` and `C_N_0_PER_N[1] == 10` with explicit Δ_5 ≠ Φ_10 note.

### File 2: `test_twisted_holography_k3e.py` (comment-level clarification at `test_kappa_bkm_k3e`)

**Anti-pattern**: docstring `"kappa_BKM(K3 x E) = 5 = c(0)/2 = 10/2 (Igusa weight)"` called 10 the "Igusa weight" — technically Φ_10 is Igusa-Siegel-genus-2 level-1, but κ_BKM = 5 = wt(Δ_5) is the paramodular weight, not an "Igusa weight".  Assertion `KAPPA_BKM_K3E == 5` is correct; only docstring phrasing drifted.

**Heal**: rewrote docstring as "κ_BKM(K3 × E) = wt(Δ_5) = c_1(0)/2 = 10/2 = 5 (Gritsenko 1999 paramodular)" with explicit note that Φ_10 = Δ_5² is non-paramodular Sp_4(Z).  Assertion unchanged.

### File 3: `test_hyperkahler_anchored_fixed_point.py` (HZ-IV `verified_against` drift, two sites)

**Anti-pattern**: HZ-IV decorator `verified_against` strings stated "kappa_BKM(K3 × E) = 5 = wt(Φ_10) (Igusa cusp form)" — identifying κ_BKM with wt(Φ_10) is category-wrong (off by factor 2); Φ_10 is a different form.

**Heal**: rewrote two `verified_against` entries (line 3676, line 4295) to state κ_BKM = wt(Δ_5) = 5 paramodular, with explicit note wt(Φ_10) = 10 = 2·κ_BKM since Φ_10 = Δ_5² is the non-paramodular square.  Other sites in this file at 689, 3995, 4271, 4154, 4331 already state κ_BKM = c_K3(0)/2 = 10/2 = 5 with correct Gritsenko attribution; no additional heal required there.

## LEGITIMATE sites — no heal (sample listing)

| File | Line | Token | Classification |
|------|------|-------|---------------|
| `test_kappa_bkm_adversarial.py` | 277, 524 | `weight_Phi10 == 10` | LEGITIMATE; explicit `weight_Phi10 == 2·weight_denominator` (correct Δ_5² relation) |
| `test_borcherds_denominator_phi10_engine.py` | 81, 83, 92 | `weight_chi10 == 10 == 2·kappa_BKM` | LEGITIMATE; explicit 2:1 ratio |
| `test_kappa_spectrum_reconciliation.py` | 273 | `weight_Phi10 == 10 = 2·κ_BKM` | LEGITIMATE |
| `test_cy3_modularity_constraints.py` | 624, 1069 | `c(0)=20 → weight(χ_10)=10`; Δ_5 = paramodular | LEGITIMATE |
| `test_phi01_cross.py` | 349-352 | `phi10_weight == 2·delta5_weight` | LEGITIMATE; Gritsenko-Nikulin explicit |
| `test_chiral_homology_ran_k3.py` | 77, 133, 238, 266, 270 | `modular_weight = -c/2 = -12` (K3 c=24) | LEGITIMATE; η^-24 / bosonic string weight, distinct from κ_BKM |
| `test_nekrasov_agt_k3.py` | 190, 193, 357, 681, 682 | `modular_weight = -χ(K3)/2 = -12` | LEGITIMATE; VW weight, distinct from κ_BKM |
| `test_vafa_witten_shadow.py` | 225, 251, 253, 280, 390, 392, 395, 397, 788 | VW weight on K3 = -12 | LEGITIMATE; η^-24 transformation weight |
| `test_siegel_genus3.py` | 457, 858-859, 900, 918-920 | Siegel genus-3 χ_12 weight 12; Heisenberg weight -12 | LEGITIMATE; genus-3 Siegel, not paramodular |
| `test_four_manifold_6d_invariants.py` | 184, 186, 511, 607 | VW weight = -12 on K3 | LEGITIMATE |
| `test_borcherds_lift.py` | 108, 117, 267, 282, 444, 464, 470, 579 | `Δ_5_squared weight 10`, `Phi_12_fake_monster weight 12` | LEGITIMATE; explicit `Δ_5²` (not primitive paramodular) |
| `test_genus2_chiral_partition.py` | 361, 522, 660, 706, 740 | genus-2 bosonic string weight -12; Φ_10 (Siegel) weight 10 | LEGITIMATE |
| `test_genus2_k3e_full.py` | 381, 563, 568, 573 | `weight_Z2_heis=-12` (Heis c=24); `1_over_Phi_10 weight=-10` (Igusa pole) | LEGITIMATE; genus-2 Siegel context |
| `test_sp4_modularity_pipeline.py` | 407, 409, 412 | `Phi_10 weight 10` (Igusa genus-2 non-paramodular) | LEGITIMATE |
| `test_modular_koszul_bridge_k3e.py` | 149, 186, 233, 367 | `W_k weight = 12` (η^24 weight 12, modular bridge) | LEGITIMATE |
| `test_physical_k3_sigma_check.py` | 457-458, 473 | eta24_weight, bar_euler_weight, delta_weight = 12 | LEGITIMATE (eta-weight) |
| `test_anomaly_shadow_consistency.py` | 517-519 | `bar_euler_weight == 12` (eta^24) | LEGITIMATE |
| `test_agt_higher_rank_k3.py` | 427-430 | `modular_weight = -12·N` (rank-N VW on K3) | LEGITIMATE |
| `test_chiral_ran_correlators.py` | 550-553, 632, 638, 641 | `modular_weight = -c/2 = -12`, genus-2 `-20 = -10·c/12` | LEGITIMATE |
| `test_cy_euler.py` | 532, 553, 555 | `Δ_5 weight = dim(Sp_4)/2 = 5`; `weight_inverse_Z = 10`; `weight_Delta5_squared = 10` | LEGITIMATE |
| `test_mathieu_yangian_deeper.py` | 208 | `eta_weight = '12'` (M_24 Frame shape) | LEGITIMATE |
| `test_categorical_s_duality.py` | 420, 470 | `eta_transformation_weight == 12` | LEGITIMATE |
| `test_chiral_wrt_quantum_toroidal.py` | 418, 420 | VW weight = -12 | LEGITIMATE |
| `test_umbral_23_niemeier_yangian.py` | 734 | `eta_weight = (1/2)·24 = 12` | LEGITIMATE |
| `test_hyperkahler_anchored_fixed_point.py` | 689, 3708-3712, 3995, 4271 | Igusa Φ_10 weight 10 with explicit `= 2·κ_BKM` ratio | LEGITIMATE; now uniform after §Heal3 |
| `test_c3_envelope_comparison.py` | 91-553 | `max_weight=10`, `max_weight=12` (character truncation) | SYMBOLIC truncation, LEGITIMATE |
| `test_chiral_koszul_derived.py` | 908 | `derived_bar_heisenberg(max_weight=10)` | SYMBOLIC truncation |
| `test_hocolim_costello_li_comparison.py` | 724, 729 | `character_comparison_c3(max_weight=10)` | SYMBOLIC truncation |
| `test_deformed_chiral_ce.py` | 250 | `emb.weight(2, 5) == 10.0` (weight-pair lookup) | Unrelated arithmetic |
| `test_bkm_shadow_complete.py` | 192, 257, 259, 769 | Leech κ_BKM = 12 (weight-12 cusp form, distinct c=24 Leech) | LEGITIMATE |
| `test_k3e_topological_string_shadow.py` | 537 | `c(0)/2 = 10/2 = 5` | LEGITIMATE |
| `test_kappa_bkm_universal.py` | 85-86 | `borcherds_weight_from_c0(20) = 10` (doubled phi, gives Φ_10) | LEGITIMATE |
| `test_bar_euler_borcherds.py` | 289, 330 | `c_table[0] == 10`, Borcherds weight 5 = wt(Δ_5) | LEGITIMATE |
| `test_k3_elliptic_genus_bkm_bar.py` | 475 | `bl_weight(phi01_c_table(10))` (symbolic c-lookup) | LEGITIMATE |
| `test_cy_b_d3_final.py` | 164 | `c_crit=Fraction(100)` (central charge, unrelated) | OTHER |
| `test_k3_abelian_yangian_currents.py` | 310 | `phi_{0,1}.c(0)=10, c(-1)=1` (Fourier data) | LEGITIMATE |
| `test_connes_b_obs_ainf.py` | 168 | `j = 0, ..., 10` (Connes index) | OTHER |
| `test_cy_d_kappa_stratification.py` | 434-476 | Wave-8 canonical heal source; explicit `N=1: weight 5, c_1(0)=10` | LEGITIMATE (canonical) |

## Verification

- Healed values in `test_cy_c_pentagon_hypothesis_closures.py` cross-checked against `compute/lib/diagonal_siegel_cy_orbifolds.py` FRAME_SHAPE_DATA (line 268-314) at all five N: {1:5, 2:4, 3:3, 4:2, 6:1} for `borcherds_weight`; {1:10, 2:8, 3:6, 4:4, 6:2} for `c_disc_0`.  Match confirmed.
- `test_twisted_holography_k3e.py` assertion `KAPPA_BKM_K3E == 5` unchanged; docstring only rectified.
- `test_hyperkahler_anchored_fixed_point.py` HZ-IV `verified_against` entries now state `wt(Δ_5) = 5 = κ_BKM`, with Φ_10 = Δ_5² non-paramodular square clarification; assertion machinery unchanged.

## HZ-IV + HZ-7 + PE-5 compliance

- HZ-7 Vol III κ-subscript: every heal retains `kappa_BKM` subscript discipline (no bare κ introduced).
- PE-5 Vol III κ template: every heal carries explicit census/engine citation (`FRAME_SHAPE_DATA`, Gritsenko 1999, Allcock 2000, Gritsenko-Nikulin 1998); no bare κ leaks.
- AP238 paramodular drift: per-site heal statement distinguishes Δ_5 (paramodular weight 5 = κ_BKM) from Φ_10 (Sp_4(Z) Igusa-Siegel weight 10 = Δ_5², NOT κ_BKM).
- AP239 naming-after-physical-source: Φ_10 retained where Igusa-Siegel geometric input used; renamed to Δ_5 where paramodular level-1 geometry is the canonical input.
- AP245 statement-proof-engine agreement: engine `FRAME_SHAPE_DATA` ground truth, test values, and docstring claims now agree on {w(N)=c_N(0)/2, N=1: 5, N=2: 4, N=3: 3, N=4: 2, N=6: 1}.

## Commit plan

No commits executed (mission constraint).  Three files modified, ready for commit under single logical change "Vol III Wave-9 doubled-weight regex triage: paramodular drift heal + two comment-level clarifications".  Build and pytest verification to be performed in the Wave-9 master synthesis commit session by Raeez Lorgat.

## Residual frontier / follow-ups

- `test_twisted_holography_k3e.py` holds `KAPPA_CH_K3E == 3` (legacy additive κ_ch rule retracted by Wave-8 AP289 Künneth-multiplicative heal; canonical Hodge supertrace κ_ch(K3 × E) = 0).  OUTSIDE this mission scope (doubled-weight regex), surfaced for a follow-up AP289 propagation sweep.
- `test_hyperkahler_anchored_fixed_point.py:4286-4287` carries same legacy κ_ch additive rule (`κ_ch(K3) = 2 + κ_ch(E) = 1 → κ_ch(K3 × E) = 3`); same AP289 follow-up target.
- Six further adversarial-swarm targets not matched by the doubled-weight regex but adjacent to paramodular territory should be scanned in a Wave-10 sweep: `test_bkm_chiral_algebra.py`, `test_heterotic_typeII_yangian.py`, `test_bkm_yangian_generators.py`, `test_k3e_e1_product_chain.py`, `test_bkm_deformed_serre.py`, `test_cy_c_six_routes_generator_level.py`, `test_elliptic_hall_hocolim.py`, `test_hyperkahler_BKM_lift.py` — all hit `kappa_BKM.*10` substring but not the weight regex; verified here by grep as canonically disciplined (κ_BKM = c(0)/2 = 10/2 = 5 consistently stated).
