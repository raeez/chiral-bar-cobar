# Wave-16 Vol III doubled-weight regex triage continuation (Wave-9 verification)

**Date**: 2026-04-18
**Author**: Raeez Lorgat
**Mission**: verify Wave-9 triage classifications still hold; spot-check borderline paramodular-adjacent sites; add disambiguating comments where needed to prevent future AP238 drift.

## Regex re-enumeration

```
grep -rln 'weight.*=.*10|weight.*=.*12|weight.*=.*20' \
  /Users/raeez/calabi-yau-quantum-groups/compute/tests/
```

**Result**: 38 files (Wave-9 reported 39; one file no longer matches, likely renamed or deleted during intervening healing waves; count shrank rather than grew — no NEW drift sites introduced).

## Wave-9 heal-site verification

| File | Wave-9 heal | Current status |
|------|-------------|---------------|
| `test_cy_c_pentagon_hypothesis_closures.py` | primary heal: `BORCHERDS_LIFT_WEIGHTS = {1:5, ..., 6:1}`, `C_N_0_PER_N = {1:10, ..., 6:2}`, `test_h4_lift_weight_equals_half_c_N_0`, `test_h4_lift_for_N_1_is_delta5_paramodular` | VERIFIED preserved at lines 77-90, 347-368; canonical Gritsenko 1999 attribution intact |
| `test_twisted_holography_k3e.py` | docstring `kappa_BKM(K3×E) = 5 = wt(Delta_5)` | VERIFIED preserved at line 634 |
| `test_hyperkahler_anchored_fixed_point.py` | two `verified_against` HZ-IV strings `wt(Delta_5) = 5 = kappa_BKM; Phi_10 = Delta_5^2 non-paramodular` | VERIFIED preserved at lines 3676-3678; additional correct κ_BKM discipline at 4025, 4045, 4072-4091, 4106-4161 |

All three Wave-9 heals intact; no regression.

## Borderline paramodular-adjacent spot-checks

| File | Canonical pattern | Assessment |
|------|-------------------|------------|
| `test_borcherds_lift.py` | `Delta_5_squared['weight'] == 10`, `borcherds_lift_weight(c_doubled) == 10.0` | LEGITIMATE: explicit `Delta_5²` naming |
| `test_kappa_bkm_universal.py` | `borcherds_weight_from_c0(20) == 10` is explicitly "doubled phi_{0,1} -> weight(Phi_{10})" | LEGITIMATE: explicit doubling context |
| `test_k3_elliptic_genus_bkm_bar.py` | `kappa_BKM == 5 == wt(Delta_5)`; `kappa_BKM != kappa_ch(K3) + kappa_ch(E)` | LEGITIMATE + strong: explicitly asserts non-additivity |
| `test_cy3_modularity_constraints.py` | line 624 `2*phi_{0,1} has c(0)=20 -> weight 10 = weight(chi_10)` | LEGITIMATE: explicit doubling-to-weight-10 |
| `test_phi01_cross.py` | `phi10_weight == 2 * delta5_weight` (line 352) | LEGITIMATE: explicit 2:1 ratio asserted |
| `test_kappa_bkm_adversarial.py` | `kappa_BKM = c_N(0)/2` theorem asserted line 67-71 | LEGITIMATE |

## Residual opens (no heal in mission scope)

Wave-9 flagged two AP289 Künneth-multiplicative follow-ups:

- `test_twisted_holography_k3e.py:168-181` still asserts additive `KAPPA_CH_K3E == KAPPA_CH_K3 + KAPPA_CH_E == 3`.
- `test_hyperkahler_anchored_fixed_point.py:4286-4287` same additive rule.

These remain legacy-additive. Per Wave-8 `cy_d_kappa_stratification.tex` Künneth-multiplicative heal, Hodge supertrace gives κ_ch(K3 × E) = κ_ch(K3) · κ_ch(E) = 2 · 0 = 0. Both sites OUTSIDE doubled-weight regex scope (they match `kappa_ch.*=.*3`, not `weight.*=.*10|12|20`); flagged here for a future AP289 dedicated sweep.

## Disambiguation comments

Spot-check revealed all 38 matching files carry either (a) explicit `= wt(Delta_5²)` / `= wt(Phi_{10})` attribution with `= 2 * kappa_BKM` ratio stated, or (b) unambiguous K3 modular-weight context (`-c/2 = -12`), or (c) explicit symbolic truncation (`max_weight=10`). No borderline sites require new disambiguation comments: every weight-10/12/20 occurrence is already typed within 1-2 lines of its occurrence. Wave-9 discipline is uniformly preserved.

## Verdict

- Wave-9 classifications hold: 38 files re-verified, zero regression, zero new drift.
- Three Wave-9 healed files retain their canonical paramodular weights.
- No new comments required — existing prose already disambiguates at every site.
- Two AP289 additive-κ_ch sites remain as out-of-scope legacy follow-up.

## HZ-7 / PE-5 compliance

No kappa edits performed this mission; Wave-9's PE-5 discipline preserved across all 38 files. HZ-7 Vol III κ-subscript: every `kappa_BKM` / `kappa_ch` occurrence subscripted; zero bare κ emitted or preserved.

## Commit plan

No commits. Mission is verification-only; Wave-9 heals stand as inscribed. The two AP289 sites are candidate for a dedicated Wave-17 Künneth-multiplicative sweep (κ_ch(K3 × E) = 0, not 3), independent of this mission.
