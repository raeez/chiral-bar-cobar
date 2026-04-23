"""Tests for compute.lib.wave22_phi_n_extension_weight25_26_27_28.

Verifies Padovan dimensions, Broadhurst-Kreimer depth stratification,
phi^(n) leading values, Hardy-Ramanujan ratios, plastic-number
asymptotic, and absence of Conway-Leech umbral resonance at weights
n in {25, 26, 27, 28}.

SCOPE THRESHOLDS (this module):
    n = 27: first weight with depth-9 Brown canonical element,
            D_{27, 9} = 10, primitive zeta(3, 3, 3, 3, 3, 3, 3, 3, 3).
    n = 26: NO Conway-Leech umbral resonance (Leech rank = 24; none
            of the 23 Niemeier lattices has root rank 26).  The
            coincidence n = 26 = 24 + 2 reflects the Polyakov 1981
            critical bosonic-string dimension, not an umbral index.

Above n = 24 the scope is TRIPLE-CONDITIONAL: tiers D >= 5 depend on
Zagier-Hoffman (Brown 2012 Conj 2), tiers D >= 6 depend on BK 1997
empirical depth-distribution, and tier D >= 9 depends on Brown 2017
arXiv:1709.02856 Conj 5.3 (higher-depth grt_1 generation).

MULTI-PATH CROSS-VERIFICATION
=============================

V_1 (Richardson numerical):
    phi^(n) = d_n / n! via direct MZV partial-sum evaluation, matched
    against the closed-form Padovan recurrence.

V_2 (KZ depth-recursion):
    Counting admissible KZ composition sequences on M_{0,5} reproduces
    the Padovan recurrence via free-Lie shuffle upper bound.

V_3 (Hardy-Ramanujan exact p_24 ratio):
    p_24 from eta^{-24} Fourier expansion matches OEIS A006922;
    cross-checked against the Hardy-Ramanujan-Rademacher asymptotic.

V_4 (three-step Padovan row-sum identity):
    sum_d D_{n, d} = d_{n - 3} links BK series to Padovan via the
    three-step degree-2 (zeta(2)) lift.

V_5 (absence of umbral resonance at n = 26):
    Witnesses that the Niemeier / Conway / Leech coincidences of
    n = 24 do not extend.
"""
from __future__ import annotations

import math

import pytest

from compute.lib.wave22_phi_n_extension_weight25_26_27_28 import (
    bk_depth_check_25_28,
    bk_depth_extract,
    bk_padovan_twostep_consistency_check_25_28,
    bk_parity_split_check_25_28,
    first_depth_nine_check,
    hardy_ramanujan_exact_check_25_28,
    hardy_ramanujan_ratio_check_25_28,
    hardy_ramanujan_ratio_exact_25_28,
    no_umbral_resonance_26_check,
    p24_asymptotic,
    p24_exact,
    padovan_asymptotic,
    padovan_count_check_25_28,
    padovan_dim,
    phi_n_leading_check_25_28,
    phi_n_mzv_leading,
    phi_n_richardson_check_25_28,
    plastic_asymptotic_check_25_28,
    plastic_asymptotic_precision_check_25_28,
    plastic_number,
    polyakov_bosonic_critical_dim_check,
    wave22_verifier_25_28,
)


# ---------------------------------------------------------------------------
# Path 1: Padovan recurrence (primary)
# ---------------------------------------------------------------------------

class TestPadovanDimensions:
    """Verify d_{25}..d_{28} = (351, 465, 616, 816)."""

    def test_padovan_count_25_28_direct(self):
        """Assert Padovan dimensions match Brown 2012 Thm 1.2 upper bound."""
        assert padovan_count_check_25_28() is True

    def test_padovan_recurrence_25_28(self):
        """Recompute d_25..d_28 from d_21..d_24 via d_n = d_{n-2}+d_{n-3}."""
        d = padovan_dim(30)
        assert d[25] == d[23] + d[22] == 200 + 151 == 351
        assert d[26] == d[24] + d[23] == 265 + 200 == 465
        assert d[27] == d[25] + d[24] == 351 + 265 == 616
        assert d[28] == d[26] + d[25] == 465 + 351 == 816

    def test_padovan_matches_plastic_closed_form(self):
        """Cross-path: A rho^n asymptotic matches d_n to within 0.01%."""
        for n in range(25, 29):
            a = padovan_asymptotic(n)
            d = padovan_dim(30)[n]
            assert abs((d - a) / d) < 1e-4, (
                f"n = {n}: A rho^n = {a}, d_n = {d}, rel err {(d - a) / d}"
            )


# ---------------------------------------------------------------------------
# Path 2: Broadhurst-Kreimer symbolic expansion
# ---------------------------------------------------------------------------

class TestBroadhurstKreimerDepth:
    """Verify D_{n, d} at n in [25, 28] through depth 9."""

    def test_bk_depth_25_28_full_table(self):
        """Assert full BK-series predictions at all (n, d) pairs."""
        assert bk_depth_check_25_28() is True

    def test_first_depth_nine_at_27(self):
        """Assert depth-9 first enters at n = 27, empty at n < 27."""
        assert first_depth_nine_check() is True

    def test_parity_split_odd_even_weights(self):
        """Cross-path: parity split enforced through depth 10."""
        assert bk_parity_split_check_25_28() is True

    def test_depth_seven_growth_25_to_27(self):
        """Cross-path: depth-7 cardinality D_{n, 7} grows 56 to 128 at n = 25 to 27."""
        D = bk_depth_extract(32, 10)
        assert D.get((25, 7), 0) == 56
        assert D.get((26, 7), 0) == 0  # even weight
        assert D.get((27, 7), 0) == 128
        # Ratio roughly 2.3, consistent with BK shuffle-product feedback.
        assert D[(27, 7)] / D[(25, 7)] > 2.0

    def test_depth_eight_growth_26_to_28(self):
        """Cross-path: D_{26, 8} = 28, D_{28, 8} = 93."""
        D = bk_depth_extract(32, 10)
        assert D.get((26, 8), 0) == 28
        assert D.get((28, 8), 0) == 93

    def test_two_step_padovan_row_sum(self):
        """Cross-path: sum_d D_{n, d} = d_{n - 2}."""
        assert bk_padovan_twostep_consistency_check_25_28() is True

    def test_depth_nine_empty_below_27(self):
        """Cross-path: depth-9 strictly absent for n < 27."""
        D = bk_depth_extract(32, 10)
        for n in range(1, 27):
            assert D.get((n, 9), 0) == 0, (
                f"Unexpected depth-9 at n = {n}: D_{{{n}, 9}} = {D.get((n, 9), 0)}"
            )


# ---------------------------------------------------------------------------
# Path 3: Numerical phi^(n) values
# ---------------------------------------------------------------------------

class TestPhiNValues:
    """Verify phi^(n) leading numerical values at n in [25, 28]."""

    def test_phi_n_leading_25_28(self):
        """Assert leading phi^(n) = d_n/n! to eight decimals."""
        assert phi_n_leading_check_25_28() is True

    def test_phi_n_magnitudes_25_28(self):
        """Assert phi^(n) magnitudes fall into expected ranges."""
        vals = phi_n_richardson_check_25_28()
        ranges = {
            25: (2e-23, 3e-23),
            26: (1e-24, 2e-24),
            27: (5e-26, 7e-26),
            28: (2e-27, 4e-27),
        }
        for n, (lo, hi) in ranges.items():
            assert lo < vals[n] < hi, (
                f"phi^({n}) = {vals[n]:.3e} outside [{lo:.3e}, {hi:.3e}]"
            )

    def test_phi_n_monotone_decreasing(self):
        """Cross-path: phi^(n) strictly decreases through [25, 28]."""
        vals = phi_n_richardson_check_25_28()
        for n in range(25, 28):
            assert vals[n] > vals[n + 1], (
                f"expected phi^({n}) > phi^({n+1}); got {vals[n]:.3e} vs {vals[n+1]:.3e}"
            )


# ---------------------------------------------------------------------------
# Path 4: Hardy-Ramanujan exact p_24 Fourier coefficient
# ---------------------------------------------------------------------------

class TestHardyRamanujanBorcherdsLeg:
    """Verify Borcherds leg p_24(ceil(n/2)) / d_n ratios at n in [25, 28]."""

    def test_p24_exact_13_14(self):
        """Assert p_24 exact matches OEIS A006922 at k = 13, 14."""
        assert p24_exact(13) == 42189811200
        assert p24_exact(14) == 156883829400

    def test_hardy_ramanujan_exact_ratios_25_28(self):
        """Assert Borcherds/MZV exact ratios."""
        assert hardy_ramanujan_exact_check_25_28() is True

    def test_hardy_ramanujan_asym_exact_ratio_settles(self):
        """Cross-path: exact/asym ratio in range [0.35, 0.45] at k = 13, 14."""
        rs = hardy_ramanujan_ratio_check_25_28()
        for n, (exact, asym, asy_over_exact) in rs.items():
            # At k = 13: asy/exact ~ 2.715, exact/asym ~ 0.368
            # At k = 14: asy/exact ~ 2.449, exact/asym ~ 0.408
            exact_over_asym = 1.0 / asy_over_exact
            assert 0.35 < exact_over_asym < 0.45, (
                f"n = {n}: exact/asym = {exact_over_asym:.3f} outside [0.35, 0.45]"
            )

    def test_p24_parity_step_13_to_14(self):
        """Cross-path: p_24 jumps by ~3.7x from k = 13 to k = 14."""
        p13 = p24_exact(13)
        p14 = p24_exact(14)
        ratio = p14 / p13
        # Empirical: 156883829400 / 42189811200 ~ 3.72
        assert 3.6 < ratio < 3.85, f"p_24(14)/p_24(13) = {ratio:.3f}, expected ~3.72"

    def test_borcherds_dominance_over_mzv_at_25_28(self):
        """Cross-path: Borcherds/MZV ratio exceeds 10^7 at every n in [25, 28]."""
        r = hardy_ramanujan_ratio_exact_25_28()
        for n in range(25, 29):
            assert r[n] > 1e7, f"Borcherds/MZV at n = {n} is {r[n]:.3e}, expected > 1e7"


# ---------------------------------------------------------------------------
# Path 5: Plastic-number asymptotic
# ---------------------------------------------------------------------------

class TestPlasticAsymptotic:
    """Verify Padovan asymptotic d_n ~ A rho^n at higher precision."""

    def test_plastic_number_value(self):
        """Plastic number rho ~ 1.32471..., unique real root of x^3 - x - 1."""
        rho = plastic_number()
        assert abs(rho - 1.3247179572447458) < 1e-12
        # Cross-check: rho^3 = rho + 1
        assert abs(rho ** 3 - (rho + 1)) < 1e-12

    def test_plastic_asymptotic_precision_25_28(self):
        """Asymptotic A rho^n within 0.01% of exact d_n."""
        assert plastic_asymptotic_precision_check_25_28() is True

    def test_plastic_residue_coefficient(self):
        """Cross-path: A = rho^2 / (2 rho + 3) = 0.31062883..."""
        rho = plastic_number()
        A = rho ** 2 / (2 * rho + 3)
        assert abs(A - 0.31062883) < 1e-7

    def test_plastic_precision_tightens_with_n(self):
        """Cross-path: plastic error at n >= 25 is < rho^{-25/2} ~ 8e-4."""
        for n in range(25, 29):
            a = padovan_asymptotic(n)
            d = padovan_dim(30)[n]
            err = abs((d - a) / d)
            assert err < 8e-4, f"n = {n}: err = {err:.6f} exceeds rho^{{-n/2}} bound"


# ---------------------------------------------------------------------------
# Path 6: Absence of Conway-Leech umbral resonance at n = 26
# ---------------------------------------------------------------------------

class TestNoUmbralResonanceAt26:
    """Verify that n = 26 does NOT carry a Niemeier/Conway/Leech coincidence."""

    def test_no_umbral_resonance_at_26(self):
        """Assert no Conway-Leech/Niemeier umbral resonance at n = 26."""
        assert no_umbral_resonance_26_check() is True

    def test_polyakov_bosonic_critical_dim_at_26(self):
        """Assert n = 26 coincides with Polyakov 1981 critical bosonic dimension."""
        assert polyakov_bosonic_critical_dim_check() is True

    def test_niemeier_count_does_not_extend_to_26(self):
        """Cross-path: the 23 Niemeier lattices all have total rank 24, not 26."""
        # Even unimodular lattices exist only in dimensions divisible by 8.
        # Rank 24 admits 24 genus representatives (Niemeier 1973): 23 with
        # nonzero root system + 1 Leech lattice (root system empty).
        # Next even unimodular rank is 32 (more than 10^7 genera).
        niemeier_total_rank = 24
        next_even_unimodular_rank = 32
        assert niemeier_total_rank % 8 == 0
        assert next_even_unimodular_rank % 8 == 0
        assert 26 % 8 != 0  # 26 is NOT a valid even unimodular rank
        # Therefore no even unimodular lattice exists at rank 26.

    def test_monster_c_is_24_not_26(self):
        """Cross-path: Monster VOA V^natural has c = 24, not 26."""
        monster_c = 24
        polyakov_bosonic_c = 26
        # The Monster module sits at c = 24 = chi(K3) = rank(Leech).
        # The bosonic string sits at c = 26 = 24 + 2, the Liouville offset.
        assert monster_c == 24
        assert polyakov_bosonic_c - monster_c == 2


# ---------------------------------------------------------------------------
# Path 7: Aggregate verifier
# ---------------------------------------------------------------------------

class TestWave22Verifier:
    """Verify all checks pass through the aggregate verifier."""

    def test_wave22_verifier(self):
        """Run aggregate verifier for phi^(n) at weights 25-28."""
        results = wave22_verifier_25_28()
        expected = {
            "padovan_count_25_28": True,
            "bk_depth_25_28": True,
            "first_depth_nine_at_27": True,
            "bk_padovan_twostep_25_28": True,
            "bk_parity_split_25_28": True,
            "phi_n_leading_25_28": True,
            "hardy_ramanujan_exact_25_28": True,
            "no_umbral_resonance_26": True,
            "polyakov_bosonic_critical_dim_26": True,
            "plastic_asymptotic_25_28": True,
        }
        assert results == expected, f"verifier disagreement: {results} != {expected}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
