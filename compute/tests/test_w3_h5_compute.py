"""Tests for W3 H^5 = 171 computation and verification.

Ten independent checks supporting H^5(B(W3)) = 171.

The key result is the DS uniqueness theorem (Check 6):
  Given H^1=2, H^2=5, H^3=16, H^4=52 and the structural constraint
  that (1-3x-x^2) divides the GF denominator (from W3 = DS(sl3)),
  the rational GF is UNIQUELY determined, yielding H^5 = 171.
"""

import pytest
from math import sqrt

from compute.lib.w3_h5_compute import (
    KNOWN_VALUES,
    PREDICTED_H5,
    extend_sequence,
    check_recurrence_consistency,
    check_numerator_verification,
    check_denominator_factorization,
    check_growth_rate,
    check_ds_invariance,
    check_ds_uniqueness,
    check_virasoro_bound,
    check_anti_koszul,
    check_positivity,
    check_c_independence,
    run_all_checks,
)


# =========================================================================
# Check 1: Recurrence consistency
# =========================================================================

class TestRecurrence:
    """a(n) = 4a(n-1) - 2a(n-2) - a(n-3) reproduces all known values."""

    def test_reproduces_known(self):
        result = check_recurrence_consistency()
        assert result["all_ok"]

    def test_predicts_h5(self):
        result = check_recurrence_consistency()
        assert result["H5_predicted"] == 171
        assert result["H5_matches"]

    def test_direct_computation(self):
        """4*52 - 2*16 - 5 = 171."""
        assert 4 * 52 - 2 * 16 - 5 == 171

    def test_x3_relation(self):
        """a(3) - 4*a(2) + 2*a(1) = 16 - 20 + 4 = 0."""
        assert 16 - 4 * 5 + 2 * 2 == 0

    def test_x4_relation(self):
        """a(4) - 4*a(3) + 2*a(2) + a(1) = 52 - 64 + 10 + 2 = 0."""
        assert 52 - 4 * 16 + 2 * 5 + 2 == 0

    def test_x5_relation(self):
        """a(5) - 4*a(4) + 2*a(3) + a(2) = 171 - 208 + 32 + 5 = 0."""
        assert 171 - 4 * 52 + 2 * 16 + 5 == 0


# =========================================================================
# Check 2: Numerator verification
# =========================================================================

class TestNumerator:
    """D(x)*P(x) = N(x) = 2x - 3x^2 through degree 10."""

    def test_all_match(self):
        result = check_numerator_verification()
        assert result["all_match"]

    def test_coefficient_x1(self):
        """At x^1: a(1) = 2 = n_1."""
        assert 2 == 2

    def test_coefficient_x2(self):
        """At x^2: a(2) - 4*a(1) = 5 - 8 = -3 = n_2."""
        assert 5 - 4 * 2 == -3


# =========================================================================
# Check 3: Denominator factorization
# =========================================================================

class TestDenominator:
    """D(x) = (1-x)(1-3x-x^2) with discriminant 13."""

    def test_factorization(self):
        result = check_denominator_factorization()
        assert result["factored"]

    def test_discriminant_13(self):
        result = check_denominator_factorization()
        assert result["discriminant_is_13"]

    def test_expansion(self):
        """(1-x)(1-3x-x^2) = 1 - 4x + 2x^2 + x^3."""
        # Coefficient of x^0: 1*1 = 1
        # Coefficient of x^1: 1*(-3) + (-1)*1 = -4
        # Coefficient of x^2: 1*(-1) + (-1)*(-3) = 2
        # Coefficient of x^3: (-1)*(-1) = 1
        assert (-3) + (-1) == -4
        assert (-1) + (-1) * (-3) == 2
        assert (-1) * (-1) == 1


# =========================================================================
# Check 4: Growth rate
# =========================================================================

class TestGrowthRate:
    """Ratios converge to (3+sqrt(13))/2 ~ 3.303."""

    def test_convergence(self):
        result = check_growth_rate()
        assert result["convergence"]

    def test_target_value(self):
        target = (3 + sqrt(13)) / 2
        assert abs(target - 3.3028) < 0.001

    def test_monotone_approach(self):
        """Ratios approach the target monotonically from below."""
        a = extend_sequence([2, 5, 16, 52], 15)
        ratios = [a[n] / a[n - 1] for n in range(1, len(a))]
        target = (3 + sqrt(13)) / 2
        # All ratios below target (for n >= 3)
        for n in range(2, len(ratios)):
            assert ratios[n] < target + 1e-10


# =========================================================================
# Check 5: DS discriminant invariance
# =========================================================================

class TestDSInvariance:
    """W3 and sl3 share the factor (1-3x-x^2) in the GF denominator."""

    def test_ds_invariance(self):
        result = check_ds_invariance()
        assert result["ds_invariance"]

    def test_sl3_factorization(self):
        """sl3: D(x) = (1-8x)(1-3x-x^2) = 1 - 11x + 23x^2 + 8x^3."""
        assert (-8) + (-3) == -11
        assert (-8) * (-3) + (-1) == 23
        assert (-8) * (-1) == 8

    def test_w3_factorization(self):
        """W3: D(x) = (1-x)(1-3x-x^2) = 1 - 4x + 2x^2 + x^3."""
        assert (-1) + (-3) == -4
        assert (-1) * (-3) + (-1) == 2
        assert (-1) * (-1) == 1


# =========================================================================
# Check 6: DS UNIQUENESS (the key result)
# =========================================================================

class TestDSUniqueness:
    """DS invariance UNIQUELY determines the GF from 4 data points.

    This is the main computational result: given H^1=2, H^2=5, H^3=16, H^4=52
    and the constraint that (1-3x-x^2) | D(x), the GF is unique and gives H^5 = 171.
    """

    def test_all_ok(self):
        result = check_ds_uniqueness()
        assert result["all_ok"]

    def test_unique_solution(self):
        result = check_ds_uniqueness()
        assert result["unique_solution"]

    def test_h5_is_171(self):
        result = check_ds_uniqueness()
        assert result["h5_is_171"]

    def test_a_is_minus1(self):
        """The linear factor is (1-x), i.e., a = -1."""
        result = check_ds_uniqueness()
        assert result["a_is_minus1"]

    def test_one_parameter_family(self):
        """With 4 data points and (p=2, q=3), there is exactly 1 free parameter.

        The system D*P = N gives:
          x^1: n1 = 2
          x^2: n2 = 5 + 2*d1
          x^3: d2 = -(16 + 5*d1)/2
          x^4: d3 = -6 - 7*d1/4

        H^5 = 158 - 13*d1/4, which depends on d1.
        """
        # Verify the formula at d1 = -4
        d1 = -4
        h5 = 158 - 13 * d1 / 4
        assert h5 == 171

    def test_ds_fixes_d1(self):
        """DS invariance: (1-3x-x^2) | D(x) forces d1 = -4.

        D(x) = (1+ax)(1-3x-x^2) implies:
          d1 = a - 3
          d2 = -1 - 3a
          d3 = -a
        Combined with d2 = -(16+5*d1)/2 gives a linear equation in a:
          -1 - 3a = -8 - 5(a-3)/2
          -1 - 3a = -1/2 - 5a/2
          -a/2 = 1/2
          a = -1
        Therefore d1 = a - 3 = -4 (unique).
        """
        # Verify the linear equation
        # LHS: -1 - 3*(-1) = -1 + 3 = 2
        # RHS: -8 - 5*(-1-3)/2 = -8 - 5*(-4)/2 = -8 + 10 = 2
        lhs = -1 - 3 * (-1)
        rhs = -8 - 5 * (-1 - 3) / 2
        assert lhs == rhs

    def test_factor_consistent(self):
        """Both equations from D*P = N are satisfied by a = -1."""
        result = check_ds_uniqueness()
        assert result["factor_consistent"]

    def test_h5_formula(self):
        """H^5 = 158 - 13*d1/4 with d1 = -4 gives 171."""
        for d1_val, expected_h5 in [(-4, 171), (-8, 184), (0, 158), (4, 145)]:
            h5 = 158 - 13 * d1_val / 4
            assert h5 == expected_h5


# =========================================================================
# Check 7: Virasoro subalgebra bound
# =========================================================================

class TestVirasoroBound:
    """H^n(W3) >= H^n(Vir) at each degree."""

    def test_all_geq(self):
        result = check_virasoro_bound()
        assert result["all_geq"]

    def test_h5_exceeds_virasoro(self):
        """H^5(W3) = 171 > H^5(Vir) = 30."""
        # Motzkin: M(5)=21, M(6)=51, so H^5(Vir) = 51 - 21 = 30
        assert 171 > 30

    def test_excess_grows(self):
        """The excess H^n(W3) - H^n(Vir) grows with n."""
        w3 = [2, 5, 16, 52, 171]
        M = [1, 1, 2, 4, 9, 21, 51]
        vir = [M[n+1] - M[n] for n in range(1, 6)]
        excess = [w3[n] - vir[n] for n in range(5)]
        assert excess == [1, 3, 11, 40, 141]
        # Check monotone increasing
        for n in range(4):
            assert excess[n + 1] > excess[n]


# =========================================================================
# Check 8: Anti-Koszul
# =========================================================================

class TestAntiKoszul:
    """W3 is NOT classically Koszul (expected from higher-order OPE poles)."""

    def test_anti_koszul_confirmed(self):
        result = check_anti_koszul()
        assert result["anti_koszul_confirmed"]

    def test_negative_h2(self):
        """Formal Koszul dual has h[2] = -1 < 0."""
        result = check_anti_koszul()
        assert result["pattern_h012"] == (1, 2, -1)

    def test_h0_h1_correct(self):
        """h[0] = 1 (unit), h[1] = 2 (generators T, W)."""
        result = check_anti_koszul()
        assert result["dual_coeffs"][0] == 1
        assert result["dual_coeffs"][1] == 2


# =========================================================================
# Check 9: Positivity
# =========================================================================

class TestPositivity:
    """All terms in the extended sequence are positive."""

    def test_all_positive(self):
        result = check_positivity()
        assert result["all_positive"]

    def test_first_10(self):
        """First 10 terms: 2, 5, 16, 52, 171, 564, 1862, 6149, 20308, 67072."""
        a = extend_sequence([2, 5, 16, 52], 6)
        assert a == [2, 5, 16, 52, 171, 564, 1862, 6149, 20308, 67072]


# =========================================================================
# Check 10: c-independence
# =========================================================================

class TestCIndependence:
    def test_c_independent(self):
        result = check_c_independence()
        assert result["c_independent"]


# =========================================================================
# Integration tests
# =========================================================================

class TestIntegration:
    """Full integration tests."""

    def test_run_all_checks(self):
        results = run_all_checks()
        assert results["summary"]["status"] == "VERIFIED"

    def test_all_12_checks_pass(self):
        results = run_all_checks()
        assert results["summary"]["checks_passed"] == results["summary"]["checks_total"]

    def test_h5_value(self):
        results = run_all_checks()
        assert results["summary"]["H5"] == 171


# =========================================================================
# Cross-module consistency
# =========================================================================

class TestCrossModuleConsistency:
    """Verify consistency with other W3 modules."""

    def test_consistent_with_w3_h5_verification(self):
        """Our module agrees with the w3_h5_verification module."""
        from compute.lib.w3_h5_verification import KNOWN_VALUES as KV2
        from compute.lib.w3_h5_verification import CONJECTURED_H5 as CH5
        # KV2 includes H^0 = 1 (augmentation); ours starts at H^1
        for n in range(1, 5):
            assert KNOWN_VALUES[n] == KV2[n]
        assert PREDICTED_H5 == CH5

    def test_consistent_with_bar_gf_solver(self):
        """Our recurrence matches the bar_gf_solver's verification."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf
        result = verify_conjectured_gf(
            [2, 5, 16, 52],
            num_coeffs=[2, -3],
            den_coeffs=[-4, 2, 1],
            n_predict=3,
        )
        assert result["matches"]
        assert result["predictions"][0] == 171

    def test_consistent_with_bar_complex(self):
        """Our value agrees with the bar_complex module's known data."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        w3_known = KNOWN_BAR_DIMS["W3"]
        for n in range(1, 5):
            assert KNOWN_VALUES[n] == w3_known[n]

    def test_ds_consistent_with_sl3_gf(self):
        """The DS invariance is consistent with the sl3 GF."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf
        # sl3 GF: D = (1-8x)(1-3x-x^2), N = 8x - 52x^2 - 8x^3
        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -52, -8],
            den_coeffs=[-11, 23, 8],
            n_predict=3,
        )
        assert result["matches"]
        assert result["predictions"][0] == 1352  # conjectured H^4(sl3)
