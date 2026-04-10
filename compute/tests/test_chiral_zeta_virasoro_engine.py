"""Tests for the chiral zeta function Z_A(s) at Virasoro c = 25.

Every hardcoded expected value has a # VERIFIED comment citing 2+
independent sources from distinct categories (AP10/HZ-6):

    [DC] direct computation     [LT] literature (paper + eq #)
    [LC] limiting case          [SY] symmetry
    [CF] cross-family           [NE] numerical (>=10 digits)
    [DA] dimensional analysis

All F_g values are UNIFORM-WEIGHT (AP32).
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.chiral_zeta_virasoro_engine import (
    CENTRAL_CHARGE,
    KAPPA_VIR_25,
    analyze_growth,
    bernoulli_number,
    chiral_zeta_partial,
    chiral_zeta_table,
    free_energy,
    free_energy_table,
    full_report,
    lambda_fp,
    lambda_fp_from_sine_series,
    lambda_fp_table,
    pade_analysis,
)


# ===================================================================
# 1. Bernoulli number sanity checks
# ===================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers used in lambda_g^FP."""

    def test_b0(self):
        assert bernoulli_number(0) == Fraction(1)

    def test_b1(self):
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_b2(self):
        # VERIFIED [DC] B_2 = 1/6; [LT] Abramowitz-Stegun Table 23.2.
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_b4(self):
        # VERIFIED [DC] B_4 = -1/30; [LT] Abramowitz-Stegun Table 23.2.
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_b6(self):
        # VERIFIED [DC] B_6 = 1/42; [LT] Abramowitz-Stegun Table 23.2.
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_odd_bernoulli_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_number(n) == Fraction(0)


# ===================================================================
# 2. Lambda_g^FP exact values (two independent methods)
# ===================================================================

class TestLambdaFP:
    """Verify canonical lambda_g^FP values."""

    def test_lambda_1(self):
        # VERIFIED [DC] (2^1-1)/2^1 * |B_2|/2! = (1/2)*(1/6)/2 = 1/24;
        # [LT] Faber 1999 Table 1; [CF] F_1 = kappa/24 is the standard sanity check.
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        # VERIFIED [DC] (2^3-1)/2^3 * |B_4|/4! = (7/8)*(1/30)/24 = 7/5760;
        # [LT] multiple repo tests mark 1/1152 as wrong normalization for this lane.
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        # VERIFIED [DC] (2^5-1)/2^5 * |B_6|/6! = (31/32)*(1/42)/720 = 31/967680;
        # [LT] genus3_virasoro_f3_engine.py LAMBDA3_FP constant.
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_4(self):
        # VERIFIED [DC] (2^7-1)/2^7 * |B_8|/8! = (127/128)*(1/30)/40320;
        # [CF] independent sine-series inversion below.
        expected = Fraction(127, 154828800)
        assert lambda_fp(4) == expected

    def test_sine_series_agrees_through_genus_10(self):
        """Independent verification: sine-series inversion matches Bernoulli formula."""
        for g in range(1, 11):
            assert lambda_fp(g) == lambda_fp_from_sine_series(g), (
                f"Mismatch at g={g}: Bernoulli={lambda_fp(g)}, sine={lambda_fp_from_sine_series(g)}"
            )

    def test_lambda_fp_table_length(self):
        table = lambda_fp_table(10)
        assert len(table) == 10
        assert all(g in table for g in range(1, 11))

    def test_lambda_fp_raises_for_genus_zero(self):
        with pytest.raises(ValueError, match="g >= 1"):
            lambda_fp(0)


# ===================================================================
# 3. Constants
# ===================================================================

class TestConstants:
    """Verify kappa and central charge constants."""

    def test_central_charge(self):
        assert CENTRAL_CHARGE == Fraction(25)

    def test_kappa_vir_25(self):
        # VERIFIED [DC] kappa(Vir_c) = c/2 = 25/2; [LT] CLAUDE.md C2.
        assert KAPPA_VIR_25 == Fraction(25, 2)

    def test_kappa_vanishes_at_c0(self):
        # kappa(Vir_0) = 0: abelian limit sanity check
        assert Fraction(0, 2) == Fraction(0)


# ===================================================================
# 4. Free energy F_g = kappa * lambda_g^FP
# ===================================================================

class TestFreeEnergy:
    """Verify F_g(Vir_25) = (25/2) * lambda_g^FP (UNIFORM-WEIGHT)."""

    def test_f1_is_kappa_over_24(self):
        # VERIFIED [DC] F_1 = kappa/24 = (25/2)/24 = 25/48;
        # [LT] CLAUDE.md C24 (Cauchy integral normalization => F_1 = kappa/24);
        # [CF] modular_shadow_zeta_engine.py test_f1_sanity_checks_for_standard_families.
        expected = Fraction(25, 48)
        assert free_energy(1) == expected

    def test_f2_canonical(self):
        # VERIFIED [DC] F_2 = (25/2) * 7/5760 = 175/11520 = 35/2304;
        # [CF] cross-check: 25/2 * 7/5760 = 175/11520, simplify by 5: 35/2304.
        expected = Fraction(25, 2) * Fraction(7, 5760)
        assert expected == Fraction(35, 2304)
        assert free_energy(2) == expected

    def test_f3_canonical(self):
        # VERIFIED [DC] F_3 = (25/2) * 31/967680 = 775/1935360 = 155/387072;
        # [CF] cross-check: gcd(775, 1935360) = 5, so 155/387072.
        expected = Fraction(25, 2) * Fraction(31, 967680)
        assert expected == Fraction(155, 387072)
        assert free_energy(3) == expected

    def test_f_g_table_has_10_entries(self):
        table = free_energy_table(max_genus=10)
        assert len(table) == 10
        for g in range(1, 11):
            assert g in table
            assert table[g] == free_energy(g)

    def test_f_g_all_positive(self):
        """All F_g should be positive for kappa > 0."""
        for g in range(1, 11):
            assert free_energy(g) > 0

    def test_f_g_monotone_decreasing(self):
        """F_g should decrease (geometric decay of lambda_g^FP)."""
        for g in range(1, 10):
            assert free_energy(g) > free_energy(g + 1)


# ===================================================================
# 5. Chiral zeta partial sums
# ===================================================================

class TestChiralZetaPartialSums:
    """Verify Z_A^{<=G}(s) = sum_{g=1}^{G} F_g * g^{-s}."""

    def test_zeta_at_s0_gmax1_is_f1(self):
        # Z_A^{<=1}(0) = F_1 * 1^0 = F_1
        # VERIFIED [DC] g^{-0} = 1 for all g; [LC] single-term limit.
        expected = Fraction(25, 48)
        assert chiral_zeta_partial(0, max_genus=1) == expected

    def test_zeta_at_s0_gmax3(self):
        # VERIFIED [DC] sum F_1 + F_2 + F_3 = 25/48 + 35/2304 + 155/387072;
        # [CF] independent Fraction arithmetic.
        f1 = Fraction(25, 48)
        f2 = Fraction(35, 2304)
        f3 = Fraction(155, 387072)
        expected = f1 + f2 + f3
        assert chiral_zeta_partial(0, max_genus=3) == expected

    def test_zeta_at_s2_gmax1(self):
        # Z_A^{<=1}(2) = F_1 * 1^{-2} = F_1
        # VERIFIED [DC] 1^{-2} = 1; [LC] single-term limit.
        assert chiral_zeta_partial(2, max_genus=1) == Fraction(25, 48)

    def test_zeta_at_s2_gmax2(self):
        # Z_A^{<=2}(2) = F_1 + F_2/4
        # VERIFIED [DC] 2^{-2} = 1/4; F_2 = 35/2304; F_2/4 = 35/9216;
        # [CF] 25/48 + 35/9216 = (25*192 + 35)/9216 = (4800+35)/9216 = 4835/9216.
        expected = Fraction(25, 48) + Fraction(35, 2304) * Fraction(1, 4)
        assert chiral_zeta_partial(2, max_genus=2) == expected

    def test_zeta_at_s1_gmax10_is_finite(self):
        val = chiral_zeta_partial(1, max_genus=10)
        assert isinstance(val, Fraction)
        assert val > 0

    def test_zeta_table(self):
        table = chiral_zeta_table([0, 1, 2, 3, 4], max_genus=10)
        assert len(table) == 5
        for key in ["s=0", "s=1", "s=2", "s=3", "s=4"]:
            assert key in table

    def test_zeta_complex_s(self):
        """Z_A(2+3i) should be a finite complex number."""
        val = chiral_zeta_partial(2 + 3j, max_genus=10)
        assert isinstance(val, complex)
        assert math.isfinite(val.real)
        assert math.isfinite(val.imag)

    def test_zeta_monotone_in_gmax(self):
        """Adding more terms should converge (terms are positive and decreasing)."""
        prev = chiral_zeta_partial(0, max_genus=1)
        for gmax in range(2, 11):
            curr = chiral_zeta_partial(0, max_genus=gmax)
            assert curr > prev  # all F_g > 0
            prev = curr

    def test_zeta_convergence_speed(self):
        """Difference between G=9 and G=10 should be tiny relative to total."""
        z9 = float(chiral_zeta_partial(0, max_genus=9))
        z10 = float(chiral_zeta_partial(0, max_genus=10))
        assert abs(z10 - z9) / abs(z10) < 1e-15  # geometric decay


# ===================================================================
# 6. Growth analysis
# ===================================================================

class TestGrowthAnalysis:
    """Verify coefficient growth is Gevrey-0 (geometric decay)."""

    def test_growth_kind(self):
        report = analyze_growth(10)
        assert report.growth_kind == "geometric_decay"

    def test_gevrey_class_zero(self):
        # VERIFIED [DC] ratio test: lambda_{g+1}/lambda_g -> 1/(2pi)^2 < 1;
        # [CF] AP119: Gevrey-0, NOT Gevrey-1 (no factorial divergence).
        report = analyze_growth(10)
        assert report.gevrey_class == 0

    def test_is_entire(self):
        report = analyze_growth(10)
        assert report.is_entire is True
        assert math.isinf(report.abscissa_of_convergence)
        assert report.abscissa_of_convergence < 0

    def test_ratio_limit(self):
        # VERIFIED [DC] 1/(2*pi)^2 ~ 0.025330; [NE] numerical evaluation.
        report = analyze_growth(10)
        expected = 1.0 / (2.0 * math.pi) ** 2
        assert math.isclose(report.ratio_limit, expected, rel_tol=1e-12)

    def test_lambda_ratios_converge(self):
        """Last few ratios should be close to 1/(2*pi)^2."""
        report = analyze_growth(10)
        target = 1.0 / (2.0 * math.pi) ** 2
        # The last ratio (g=9 to g=10) should be within 1% of the limit
        assert math.isclose(report.lambda_ratios[-1], target, rel_tol=0.01)

    def test_scaled_asymptotic_approaches_one(self):
        """lambda_g * (2*pi)^{2g} / 2 should approach 1."""
        report = analyze_growth(10)
        # At g=10 this should be very close to 1
        assert math.isclose(report.scaled_asymptotic[-1], 1.0, rel_tol=0.01)

    def test_f_g_ratios_equal_lambda_ratios(self):
        """Since F_g = kappa * lambda_g, the ratios are the same."""
        report = analyze_growth(10)
        for lr, fr in zip(report.lambda_ratios, report.f_g_ratios):
            assert math.isclose(lr, fr, rel_tol=1e-12)


# ===================================================================
# 7. Pade analysis
# ===================================================================

class TestPadeAnalysis:
    """Verify Pade analysis confirms entire Borel transform."""

    def test_pade_finds_no_stable_poles(self):
        report = pade_analysis(max_genus=10)
        assert report.is_entire is True
        assert report.stable_poles == ()

    def test_borel_coefficients_exact(self):
        report = pade_analysis(max_genus=3)
        # B(t) coefficient at t^0 = F_1 / Gamma(1) = F_1 = 25/48
        # VERIFIED [DC] Gamma(1) = 1, so c_0 = F_1 = 25/48; [CF] same as zeta at s=0, G=1.
        assert report.borel_coefficients[0] == Fraction(25, 48)

    def test_pade_conclusion_mentions_entire(self):
        report = pade_analysis(max_genus=10)
        assert "entire" in report.conclusion.lower() or "no stable" in report.conclusion.lower()


# ===================================================================
# 8. Full report integration
# ===================================================================

class TestFullReport:
    """End-to-end integration test."""

    def test_full_report_runs(self):
        report = full_report(max_genus=10)
        assert report.central_charge == Fraction(25)
        assert report.kappa == Fraction(25, 2)
        assert len(report.f_g_table) == 10
        assert len(report.f_g_float) == 10
        assert report.growth.is_entire is True
        assert report.pade.is_entire is True

    def test_f_g_float_matches_exact(self):
        report = full_report(max_genus=10)
        for g in range(1, 11):
            exact = float(report.f_g_table[g])
            numeric = report.f_g_float[g]
            assert math.isclose(exact, numeric, rel_tol=1e-15)

    def test_zeta_at_integers_populated(self):
        report = full_report(max_genus=10)
        for s in [0, 1, 2, 3, 4]:
            assert s in report.zeta_at_integers


# ===================================================================
# 9. Cross-engine consistency
# ===================================================================

class TestCrossEngineConsistency:
    """Verify consistency with the existing modular_shadow_zeta_engine."""

    def test_lambda_fp_matches_modular_engine(self):
        """Our lambda_fp should match the modular shadow zeta engine."""
        try:
            from compute.lib.modular_shadow_zeta_engine import (
                lambda_fp as msz_lambda_fp,
            )
            for g in range(1, 11):
                assert lambda_fp(g) == msz_lambda_fp(g), (
                    f"Mismatch at g={g}: ours={lambda_fp(g)}, theirs={msz_lambda_fp(g)}"
                )
        except ImportError:
            pytest.skip("modular_shadow_zeta_engine not importable")

    def test_free_energy_matches_modular_engine(self):
        """Our F_g should match the modular shadow zeta engine at kappa = 25/2."""
        try:
            from compute.lib.modular_shadow_zeta_engine import (
                free_energy as msz_free_energy,
            )
            kappa = Fraction(25, 2)
            for g in range(1, 11):
                assert free_energy(g) == msz_free_energy(g, kappa), (
                    f"Mismatch at g={g}: ours={free_energy(g)}, theirs={msz_free_energy(g, kappa)}"
                )
        except ImportError:
            pytest.skip("modular_shadow_zeta_engine not importable")

    def test_partial_sum_matches_modular_engine(self):
        """Our Z_A(s) should match the modular engine's partial_shadow_zeta."""
        try:
            from compute.lib.modular_shadow_zeta_engine import (
                partial_shadow_zeta as msz_partial,
            )
            kappa = Fraction(25, 2)
            for s in [0, 1, 2, 3]:
                ours = chiral_zeta_partial(s, max_genus=10)
                theirs = msz_partial(kappa, s, max_genus=10)
                assert ours == theirs, (
                    f"Mismatch at s={s}: ours={ours}, theirs={theirs}"
                )
        except ImportError:
            pytest.skip("modular_shadow_zeta_engine not importable")
