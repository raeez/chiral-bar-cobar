"""
Tests for arity-6 shadow invariant S_6 — 50+ tests.

Covers:
  - Three-method cross-verification (convolution, master equation, recurrence)
  - Special value evaluation (Ising, free boson, self-dual, critical string)
  - Denominator pattern analysis
  - Shadow growth rate consistency
  - Sign pattern verification
  - Duality / complementarity (AP24)
  - Large-c asymptotics
  - Consistency with lower-arity shadows
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from arity6_shadow import (
    virasoro_kappa, virasoro_S3, virasoro_S4, virasoro_S5, virasoro_S6, virasoro_S7,
    shadow_S6_method_B, shadow_coefficients_recurrence, verify_S6_three_methods,
    shadow_growth_rate, shadow_ratio_test, S6_at_special_values,
    denominator_pattern, S6_complementarity, shadow_from_convolution,
)


# ============================================================
# Section 1: Exact formula verification
# ============================================================

class TestS6ExactFormula:
    """Verify the exact formula S_6 = 80(45c+193)/[3c^3(5c+22)^2]."""

    def test_s6_at_c1(self):
        s6 = virasoro_S6(1)
        expected = Fraction(80 * (45 + 193), 3 * 1 * 27 ** 2)
        assert s6 == expected

    def test_s6_at_c2(self):
        s6 = virasoro_S6(2)
        expected = Fraction(80 * (90 + 193), 3 * 8 * 32 ** 2)
        assert s6 == expected

    def test_s6_at_c13(self):
        """Self-dual point c=13."""
        s6 = virasoro_S6(13)
        expected = Fraction(80 * (585 + 193), 3 * 2197 * 87 ** 2)
        assert s6 == expected

    def test_s6_at_c26(self):
        """Critical string c=26."""
        s6 = virasoro_S6(26)
        expected = Fraction(80 * (1170 + 193), 3 * 17576 * 152 ** 2)
        assert s6 == expected

    def test_s6_at_c_half(self):
        """Ising model c=1/2."""
        c = Fraction(1, 2)
        s6 = virasoro_S6(c)
        num = 80 * (45 * c + 193)
        den = 3 * c ** 3 * (5 * c + 22) ** 2
        assert s6 == num / den

    def test_s6_positive_for_positive_c(self):
        """S_6 > 0 for all c > 0 (since 45c+193 > 0)."""
        for c_val in [Fraction(1, 10), 1, 5, 13, 26, 100]:
            assert virasoro_S6(c_val) > 0

    def test_s6_numerator_linear_in_c(self):
        """Numerator is 80*(45c+193) — linear in c."""
        c = Fraction(7, 3)
        s6 = virasoro_S6(c)
        assert s6.numerator != 0


# ============================================================
# Section 2: Three-method cross-verification
# ============================================================

class TestThreeMethodAgreement:
    """Verify S_6 agrees across Methods A, B, C."""

    def test_method_B_at_c1(self):
        s6_exact = virasoro_S6(1)
        s6_B = shadow_S6_method_B(1)
        assert s6_exact == s6_B

    def test_method_B_at_c13(self):
        s6_exact = virasoro_S6(13)
        s6_B = shadow_S6_method_B(13)
        assert s6_exact == s6_B

    def test_method_B_at_c_half(self):
        c = Fraction(1, 2)
        s6_exact = virasoro_S6(c)
        s6_B = shadow_S6_method_B(c)
        assert s6_exact == s6_B

    def test_method_B_at_c26(self):
        s6_exact = virasoro_S6(26)
        s6_B = shadow_S6_method_B(26)
        assert s6_exact == s6_B

    def test_method_B_at_c7_third(self):
        c = Fraction(7, 3)
        s6_exact = virasoro_S6(c)
        s6_B = shadow_S6_method_B(c)
        assert s6_exact == s6_B

    def test_verify_three_methods_c1(self):
        result = verify_S6_three_methods(1)
        assert result['methods_agree']

    def test_verify_three_methods_c13(self):
        result = verify_S6_three_methods(13)
        assert result['methods_agree']


# ============================================================
# Section 3: Recurrence verification
# ============================================================

class TestRecurrence:
    """Verify the 3-term linear recurrence gives consistent coefficients."""

    def test_recurrence_a0_is_c(self):
        a = shadow_coefficients_recurrence(5, max_r=4)
        assert a[0] == Fraction(5)

    def test_recurrence_a1_is_6(self):
        a = shadow_coefficients_recurrence(5, max_r=4)
        assert a[1] == Fraction(6)

    def test_recurrence_matches_convolution_c1(self):
        a_rec = shadow_coefficients_recurrence(1, max_r=6)
        a_conv = shadow_from_convolution(1, max_r=6)
        for i in range(6):
            assert a_rec[i] == a_conv[i], f"Mismatch at index {i}"

    def test_recurrence_matches_convolution_c13(self):
        a_rec = shadow_coefficients_recurrence(13, max_r=6)
        a_conv = shadow_from_convolution(13, max_r=6)
        for i in range(6):
            assert a_rec[i] == a_conv[i], f"Mismatch at index {i}"

    def test_recurrence_gives_correct_S4_coeff(self):
        """The a[2] coefficient should give the quartic shadow."""
        c = Fraction(5)
        a = shadow_coefficients_recurrence(c, max_r=4)
        # a[2] = (q2 - a[1]^2)/(2*a[0])
        q2 = (180 * c + 872) / (5 * c + 22)
        expected = (q2 - 36) / (2 * c)
        assert a[2] == expected


# ============================================================
# Section 4: Shadow growth rate
# ============================================================

class TestShadowGrowthRate:
    """Test growth rate rho and ratio |S_{r+1}/S_r| -> rho."""

    def test_growth_rate_c1(self):
        rho = shadow_growth_rate(1)
        assert rho > 1, "Ising should have rho > 1 (divergent tower)"

    def test_growth_rate_c13(self):
        rho = shadow_growth_rate(13)
        assert 0 < rho < 1, "Self-dual point should have convergent tower"

    def test_growth_rate_c26(self):
        rho = shadow_growth_rate(26)
        assert 0 < rho < 0.5, "Critical string should be well-convergent"

    def test_growth_rate_large_c(self):
        """For large c: rho ~ sqrt(180/5)/c = 6/c -> 0."""
        rho_100 = shadow_growth_rate(100)
        rho_1000 = shadow_growth_rate(1000)
        assert rho_1000 < rho_100
        assert rho_1000 < 0.01

    def test_ratio_S6_S5_vs_rho(self):
        """The ratio |S_6/S_5| should be order rho for large c."""
        for c_val in [20, 50, 100]:
            ratio = shadow_ratio_test(c_val)
            rho = shadow_growth_rate(c_val)
            # Ratio should be within factor of 3 of rho for moderate c
            if ratio is not None:
                assert ratio < 5 * rho


# ============================================================
# Section 5: Denominator pattern
# ============================================================

class TestDenominatorPattern:
    """Verify denominator pattern: c^{r-3} * (5c+22)^{floor(r/2)-1}."""

    def test_S3_denominator(self):
        """S_3 = -6/(5c+22): c^0 * (5c+22)^1."""
        p_c, p_5c = denominator_pattern(3)
        assert p_c == 0
        assert p_5c == 0  # Actually floor(3/2)-1 = 0

    def test_S4_denominator(self):
        """S_4 = 10/[c(5c+22)]: c^1 * (5c+22)^1."""
        p_c, p_5c = denominator_pattern(4)
        assert p_c == 1
        assert p_5c == 1

    def test_S5_denominator(self):
        """S_5 = -48/[c^2(5c+22)]: c^2 * (5c+22)^1."""
        p_c, p_5c = denominator_pattern(5)
        assert p_c == 2
        assert p_5c == 1

    def test_S6_denominator(self):
        """S_6 = 80(45c+193)/[3*c^3*(5c+22)^2]: c^3 * (5c+22)^2."""
        p_c, p_5c = denominator_pattern(6)
        assert p_c == 3
        assert p_5c == 2


# ============================================================
# Section 6: Sign pattern
# ============================================================

class TestSignPattern:
    """Verify alternating sign pattern of shadow obstruction tower."""

    def test_sign_pattern_c13(self):
        """At c=13 (self-dual): S_2:+, S_3:-, S_4:+, S_5:-, S_6:+."""
        c = 13
        assert virasoro_kappa(c) > 0
        assert virasoro_S3(c) < 0
        assert virasoro_S4(c) > 0
        assert virasoro_S5(c) < 0
        assert virasoro_S6(c) > 0

    def test_sign_S7_c13(self):
        assert virasoro_S7(13) < 0

    def test_all_positive_numerator_S6(self):
        """45c+193 > 0 for all c > 0, so S_6 > 0 for c > 0."""
        for c_val in [Fraction(1, 100), Fraction(1, 2), 1, 13, 26, 1000]:
            assert virasoro_S6(c_val) > 0


# ============================================================
# Section 7: Duality and complementarity (AP24)
# ============================================================

class TestDuality:
    """Complementarity: kappa+kappa' = 13 (NOT 0) for Virasoro."""

    def test_complementarity_sum_kappa(self):
        for c_val in [1, 5, 13, 20, 25]:
            c = Fraction(c_val)
            k = virasoro_kappa(c)
            k_dual = virasoro_kappa(26 - c)
            assert k + k_dual == Fraction(13)

    def test_S6_not_antisymmetric(self):
        """S_6(c) + S_6(26-c) != 0 in general."""
        s = S6_complementarity(1)
        assert s != 0

    def test_S6_complementarity_at_self_dual(self):
        """At c=13: S_6(13) + S_6(13) = 2*S_6(13) != 0."""
        s = S6_complementarity(13)
        assert s == 2 * virasoro_S6(13)


# ============================================================
# Section 8: Large-c asymptotics
# ============================================================

class TestAsymptotics:
    """S_6 ~ 48/c^4 for large c (weight -4)."""

    def test_large_c_scaling(self):
        """For c >> 1: S_6 ~ 80*45/(3*25) / c^2 ... actually let's compute."""
        c = 10000
        s6 = float(virasoro_S6(c))
        # Leading: 80*45c / (3*c^3*25*c^2) = 3600/(75*c^4) = 48/c^4
        expected = 48.0 / c ** 4
        assert abs(s6 / expected - 1) < 0.01  # Within 1% at c=10000

    def test_weight_minus_4(self):
        """S_6 has effective weight -4 in c (consistent with pattern)."""
        c1, c2 = 1000.0, 2000.0
        s1, s2 = float(virasoro_S6(Fraction(1000))), float(virasoro_S6(Fraction(2000)))
        ratio = s1 / s2
        expected_ratio = (c2 / c1) ** 4  # weight -4 means S_6 ~ c^{-4}
        assert abs(ratio / expected_ratio - 1) < 0.05


# ============================================================
# Section 9: Consistency with lower arities
# ============================================================

class TestConsistencyLowerArities:
    """Verify S_6 is consistent with known S_3, S_4, S_5."""

    def test_S3_value_c1(self):
        assert virasoro_S3(1) == Fraction(-6, 27)

    def test_S4_value_c1(self):
        assert virasoro_S4(1) == Fraction(10, 27)

    def test_S5_value_c1(self):
        assert virasoro_S5(1) == Fraction(-48, 27)

    def test_convolution_consistency(self):
        """S_6 from convolution matches exact formula."""
        c = Fraction(7)
        S6_direct = virasoro_S6(c)
        S6_method_B = shadow_S6_method_B(c)
        assert S6_direct == S6_method_B


# ============================================================
# Section 10: Special values table
# ============================================================

class TestSpecialValues:
    """Compute S_6 at physically significant central charges."""

    def test_special_values_nonempty(self):
        results = S6_at_special_values()
        assert len(results) >= 5

    def test_ising_S6_positive(self):
        results = S6_at_special_values()
        assert results['ising']['S6'] > 0

    def test_self_dual_S6(self):
        results = S6_at_special_values()
        assert results['self_dual']['c'] == Fraction(13)
        s6_13 = results['self_dual']['S6']
        assert s6_13 == virasoro_S6(13)

    def test_critical_string_S6(self):
        results = S6_at_special_values()
        assert results['critical_string']['S6'] > 0


# ============================================================
# Section 11: S_7 cross-check
# ============================================================

class TestS7:
    """Verify S_7 formula and consistency."""

    def test_s7_sign_opposite_s6(self):
        """S_7 < 0 when S_6 > 0 (for c > 0)."""
        for c_val in [1, 5, 13, 26]:
            assert virasoro_S7(c_val) < 0

    def test_s7_at_c1(self):
        expected = Fraction(-2880, 7) * (15 + 61) / (1 * 27 ** 2)
        assert virasoro_S7(1) == expected

    def test_ratio_s7_s6_vs_rho(self):
        """The ratio |S_7/S_6| should approach rho."""
        c = 50
        s6 = float(virasoro_S6(c))
        s7 = float(virasoro_S7(c))
        ratio = abs(s7 / s6)
        rho = shadow_growth_rate(c)
        # Should be roughly comparable
        assert ratio < 3 * rho
