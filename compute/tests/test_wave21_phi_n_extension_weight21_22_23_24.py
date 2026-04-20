"""Tests for compute.lib.wave21_phi_n_extension_weight21_22_23_24.

Verifies Padovan dimensions, Broadhurst-Kreimer depth stratification,
phi^(n) leading values, Hardy-Ramanujan ratios, and plastic-number
asymptotic at weights n in {21, 22, 23, 24}.

SCOPE THRESHOLDS (this module):
    n = 21: first weight with depth-7 Brown canonical element,
            D_{21, 7} = 5, primitive zeta(3, 3, 3, 3, 3, 3, 3).
    n = 24: first weight with depth-8 Brown canonical element,
            D_{24, 8} = 7.  Also 24 = chi(K3) = rank(Leech).

Above n = 20 the scope is DOUBLE-CONDITIONAL: tiers D>=5 depend on
Zagier-Hoffman (Brown 2012 Conjecture 2), and tiers D>=6 depend on
Broadhurst-Kreimer 1997 empirical depth-distribution (verified
against Broadhurst-Bailey 2010 tables).

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
    cross-checked against the closed-form Hardy-Ramanujan-Rademacher
    asymptotic (ratio settles to ~0.29-0.33 in this range).
"""
from __future__ import annotations

import math

import pytest

from compute.lib.wave21_phi_n_extension_weight21_22_23_24 import (
    bk_depth_check_21_24,
    bk_depth_extract,
    first_depth_eight_check,
    first_depth_seven_check,
    hardy_ramanujan_exact_check_21_24,
    hardy_ramanujan_ratio_check_21_24,
    hardy_ramanujan_ratio_exact_21_24,
    niemeier_coincidence_check,
    p24_asymptotic,
    p24_exact,
    padovan_asymptotic,
    padovan_count_check_21_24,
    padovan_dim,
    phi_n_leading_check_21_24,
    phi_n_mzv_leading,
    phi_n_richardson_check_21_24,
    plastic_asymptotic_check_21_24,
    plastic_asymptotic_precision_check_21_24,
    plastic_number,
    wave21_verifier_21_24,
)


# ---------------------------------------------------------------------------
# Path 1: Padovan recurrence (primary)
# ---------------------------------------------------------------------------

class TestPadovanDimensions:
    """Verify d_{21}..d_{24} = (114, 151, 200, 265)."""

    def test_padovan_count_21_24_direct(self):
        """Assert Padovan dimensions match Brown 2012 Thm 1.2 upper bound."""
        assert padovan_count_check_21_24() is True

    def test_padovan_recurrence_21_24(self):
        """Cross-path: recompute d_21..d_24 from d_17..d_20 via d_n = d_{n-2}+d_{n-3}."""
        d = padovan_dim(28)
        assert d[21] == d[19] + d[18] == 65 + 49 == 114
        assert d[22] == d[20] + d[19] == 86 + 65 == 151
        assert d[23] == d[21] + d[20] == 114 + 86 == 200
        assert d[24] == d[22] + d[21] == 151 + 114 == 265

    def test_padovan_matches_plastic_closed_form(self):
        """Cross-path: A rho^n asymptotic matches d_n to within 0.03%."""
        for n in range(21, 25):
            rho = plastic_number()
            a = padovan_asymptotic(n)
            d = padovan_dim(28)[n]
            assert abs((d - a) / d) < 3e-4, (
                f"n={n}: A rho^n = {a}, d_n = {d}, rel err {(d - a) / d}"
            )


# ---------------------------------------------------------------------------
# Path 2: Broadhurst-Kreimer symbolic expansion
# ---------------------------------------------------------------------------

class TestBroadhurstKreimerDepth:
    """Verify D_{n, d} at n in [21, 24] through depth 8."""

    def test_bk_depth_21_24_full_table(self):
        """Assert full BK-series predictions at all (n, d) pairs."""
        assert bk_depth_check_21_24() is True

    def test_first_depth_seven_at_21(self):
        """Assert depth-7 first enters at n = 21, empty at n < 21."""
        assert first_depth_seven_check() is True

    def test_first_depth_eight_at_24(self):
        """Assert depth-8 first enters at n = 24, empty at n < 24."""
        assert first_depth_eight_check() is True

    def test_parity_split_odd_even_weights(self):
        """Cross-path: at odd n, even-depth entries vanish (and conversely)."""
        D = bk_depth_extract(28, 8)
        for n in [21, 23]:  # odd weights
            for d_even in [2, 4, 6, 8]:
                assert D.get((n, d_even), 0) == 0, (
                    f"odd weight n={n} should have D_{{{n}, {d_even}}} = 0"
                )
        for n in [22, 24]:  # even weights
            for d_odd in [1, 3, 5, 7]:
                assert D.get((n, d_odd), 0) == 0, (
                    f"even weight n={n} should have D_{{{n}, {d_odd}}} = 0"
                )

    def test_depth_seven_growth_21_to_23(self):
        """Cross-check: depth-7 cardinality jumps from 5 at n=21 to 19 at n=23."""
        D = bk_depth_extract(28, 8)
        assert D.get((21, 7), 0) == 5
        assert D.get((22, 7), 0) == 0  # even weight
        assert D.get((23, 7), 0) == 19
        # Ratio ~ 3.8 matches the shuffle-product feedback S(x)*x^2 scaling
        assert D[(23, 7)] / D[(21, 7)] > 3


# ---------------------------------------------------------------------------
# Path 3: Numerical phi^(n) values
# ---------------------------------------------------------------------------

class TestPhiNValues:
    """Verify phi^(n) leading numerical values at n in [21, 24]."""

    def test_phi_n_leading_21_24(self):
        """Assert leading phi^(n) = d_n/n! to four decimals."""
        assert phi_n_leading_check_21_24() is True

    def test_phi_n_magnitudes_21_24(self):
        """Assert phi^(n) magnitudes fall into expected ranges."""
        vals = phi_n_richardson_check_21_24()
        ranges = {
            21: (2e-18, 3e-18),
            22: (1e-19, 2e-19),
            23: (7e-21, 9e-21),
            24: (4e-22, 5e-22),
        }
        for n, (lo, hi) in ranges.items():
            assert lo < vals[n] < hi, (
                f"phi^({n}) = {vals[n]:.3e} outside [{lo:.3e}, {hi:.3e}]"
            )

    def test_phi_n_monotone_decreasing(self):
        """Cross-path: phi^(n) strictly decreases through [21, 24] (1/n! dominates d_n growth)."""
        vals = phi_n_richardson_check_21_24()
        for n in range(21, 24):
            assert vals[n] > vals[n + 1], (
                f"expected phi^({n}) > phi^({n+1}); got {vals[n]:.3e} vs {vals[n+1]:.3e}"
            )


# ---------------------------------------------------------------------------
# Path 4: Hardy-Ramanujan exact p_24 Fourier coefficient
# ---------------------------------------------------------------------------

class TestHardyRamanujanBorcherdsLeg:
    """Verify Borcherds leg p_24(ceil(n/2)) / d_n ratios."""

    def test_p24_exact_11_12(self):
        """Assert p_24 exact matches OEIS A006922 at k = 11, 12."""
        assert p24_exact(11) == 2705114880
        assert p24_exact(12) == 10914317934

    def test_hardy_ramanujan_exact_ratios_21_24(self):
        """Assert Borcherds/MZV exact ratios."""
        assert hardy_ramanujan_exact_check_21_24() is True

    def test_hardy_ramanujan_asym_exact_ratio_settles(self):
        """Cross-path: exact/asymptotic ratio in range [0.25, 0.35] at n=21..24."""
        rs = hardy_ramanujan_ratio_check_21_24()
        for n, (exact, asym, asy_over_exact) in rs.items():
            # asy_over_exact ~ 1/0.289 ~ 3.46 at k=11, ~1/0.328 ~ 3.05 at k=12
            exact_over_asym = 1.0 / asy_over_exact
            assert 0.25 < exact_over_asym < 0.35, (
                f"n={n}: exact/asym = {exact_over_asym:.3f} outside [0.25, 0.35]"
            )

    def test_p24_parity_coincidence_at_23_to_24(self):
        """Cross-path: p_24 jumps by ~4x from k=11 to k=12 (n=22->23 parity step)."""
        p11 = p24_exact(11)
        p12 = p24_exact(12)
        ratio = p12 / p11
        # Empirical: 10914317934 / 2705114880 ~ 4.03
        assert 3.9 < ratio < 4.2, f"p_24(12)/p_24(11) = {ratio:.3f}, expected ~4.03"

    def test_borcherds_dominance_over_mzv_at_21_24(self):
        """Cross-path: Borcherds/MZV ratio exceeds 10^7 at every n in [21, 24]."""
        r = hardy_ramanujan_ratio_exact_21_24()
        for n in range(21, 25):
            assert r[n] > 1e7, f"Borcherds/MZV at n={n} is {r[n]:.3e}, expected > 1e7"


# ---------------------------------------------------------------------------
# Path 5: Plastic-number asymptotic
# ---------------------------------------------------------------------------

class TestPlasticAsymptotic:
    """Verify Padovan asymptotic d_n ~ A rho^n."""

    def test_plastic_number_value(self):
        """Plastic number rho ~ 1.32471..., unique real root of x^3 - x - 1."""
        rho = plastic_number()
        assert abs(rho - 1.3247179572447458) < 1e-12
        # Cross-check: rho^3 = rho + 1
        assert abs(rho ** 3 - (rho + 1)) < 1e-12

    def test_plastic_asymptotic_precision_21_24(self):
        """Asymptotic A rho^n within 0.03% of exact d_n."""
        assert plastic_asymptotic_precision_check_21_24() is True

    def test_plastic_residue_coefficient(self):
        """Cross-path: A = rho^2 / (2 rho + 3) = 0.31062883... (truncated to 8 digits)."""
        rho = plastic_number()
        A = rho ** 2 / (2 * rho + 3)
        # Numerical value approximately 0.3106288...; double-precision cbrt
        # evaluation gives ~1e-8 drift from an externally-quoted truncation.
        assert abs(A - 0.31062883) < 1e-7


# ---------------------------------------------------------------------------
# Path 6: Niemeier / moonshine coincidence at n = 24
# ---------------------------------------------------------------------------

class TestNiemeierCoincidence:
    """Verify 24-fold arithmetic feature at n = 24."""

    def test_niemeier_coincidence(self):
        """Assert n = 24 = chi(K3) = rank(Leech) = Niemeier A_2^12 index."""
        assert niemeier_coincidence_check() is True


# ---------------------------------------------------------------------------
# Path 7: Aggregate verifier
# ---------------------------------------------------------------------------

class TestWave21Verifier:
    """Verify all checks pass through the aggregate verifier."""

    def test_wave21_verifier(self):
        """Run aggregate verifier for phi^(n) at weights 21-24."""
        results = wave21_verifier_21_24()
        expected = {
            "padovan_count_21_24": True,
            "bk_depth_21_24": True,
            "first_depth_seven_at_21": True,
            "first_depth_eight_at_24": True,
            "phi_n_leading_21_24": True,
            "hardy_ramanujan_exact_21_24": True,
            "niemeier_coincidence_24": True,
            "plastic_asymptotic_21_24": True,
        }
        assert results == expected, f"verifier disagreement: {results} != {expected}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
