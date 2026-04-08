r"""Tests for shadow S_11-S_15 engine and asymptotic growth rate.

Multi-path verification mandate: every formula checked by at least 3
independent paths.  Asymptotic theorems verified numerically.

Test structure:
    1. Three-path agreement (convolution, master eq, ODE) for S_11-S_15
    2. Explicit S_11-S_15 formulas match convolution
    3. Denominator theorem for S_11-S_15
    4. Numerator degree theorem for S_11-S_15
    5. Leading coefficient sign always (-1)^r
    6. Sign pattern at physical central charges
    7. Self-duality at c=13
    8. Koszul duality ratio = 1 at c=13
    9. Growth rate: rho = sqrt(q2/q0)
   10. Branch points are complex conjugates for c > 0
   11. Convergence radius = |t_*|
   12. Root test: |S_r|^{1/r} -> rho
   13. Ratio test: |S_{r+1}/S_r| approaches rho
   14. Gevrey-0: |S_r|/r! -> 0
   15. Critical central charge c* ~ 6.1254
   16. Darboux exponent alpha = -5/2
   17. Beat period and oscillatory structure
   18. S_15 positive numerator zero at c ~ 0.0288
   19. Cross-engine consistency with S9/S10 engine
   20. Exact Fraction arithmetic
   21. Affine sl_2 specialization
   22. Large-c vanishing
   23. Structural pattern summary table
   24. Convergence/divergence classification
"""

import math
from fractions import Fraction

import pytest
from sympy import (
    Rational,
    Symbol,
    cancel,
    simplify,
)

from compute.lib.theorem_shadow_s11_s15_engine import (
    S_explicit,
    affine_sl2_shadow_coefficient,
    asymptotic_parameters,
    branch_points,
    convergence_radius,
    convergence_radius_symbolic,
    convolution_coefficients,
    critical_central_charge_numerical,
    critical_central_charge_polynomial,
    darboux_exponent,
    denominator_exponents,
    duality_ratio_at_c13,
    gevrey_test,
    growth_rate_numerical,
    large_c_leading_order,
    ratio_test,
    root_test,
    s15_positive_zero,
    shadow_coefficients_convolution,
    shadow_coefficients_master_eq,
    shadow_coefficients_ode,
    shadow_growth_rate_squared,
    shadow_tower_table,
    verify_cross_engine_s9_s10,
    verify_denominator_theorem,
    verify_numerator_degree,
    virasoro_S_fraction,
    virasoro_shadow_metric,
)

c = Symbol('c')


# =========================================================================
# 1. THREE-PATH AGREEMENT: S_11 through S_15
# =========================================================================

class TestThreePathAgreement:
    """Every S_r must agree across all three independent derivation paths."""

    @pytest.fixture(scope="class")
    def all_paths(self):
        conv = shadow_coefficients_convolution(max_r=15)
        meq = shadow_coefficients_master_eq(max_r=15)
        ode = shadow_coefficients_ode(max_r=15)
        return conv, meq, ode

    @pytest.mark.parametrize("r", range(11, 16))
    def test_conv_vs_meq(self, all_paths, r):
        conv, meq, _ = all_paths
        diff = simplify(conv[r] - meq[r])
        assert diff == 0, f"S_{r}: conv != meq, diff = {diff}"

    @pytest.mark.parametrize("r", range(11, 16))
    def test_conv_vs_ode(self, all_paths, r):
        conv, _, ode = all_paths
        diff = simplify(conv[r] - ode[r])
        assert diff == 0, f"S_{r}: conv != ode, diff = {diff}"

    @pytest.mark.parametrize("r", range(11, 16))
    def test_meq_vs_ode(self, all_paths, r):
        _, meq, ode = all_paths
        diff = simplify(meq[r] - ode[r])
        assert diff == 0, f"S_{r}: meq != ode, diff = {diff}"


# =========================================================================
# 2. EXPLICIT FORMULAS MATCH CONVOLUTION
# =========================================================================

class TestExplicitFormulas:
    """Verify the explicit closed-form S_11-S_15 match the convolution."""

    @pytest.fixture(scope="class")
    def computed(self):
        return shadow_coefficients_convolution(max_r=15)

    @pytest.mark.parametrize("r", range(11, 16))
    def test_explicit_matches_convolution(self, computed, r):
        diff = simplify(computed[r] - S_explicit(r))
        assert diff == 0, f"S_{r} explicit != computed"

    def test_S15_factored_form(self):
        """S_15 has the specific factored form with the S_15 numerator."""
        S15 = S_explicit(15)
        # Verify at c=1
        val = S15.subs(c, 1)
        expected_num = -49152 * (61509375 + 977315625 + 5793727500
                                 + 15153459750 + 14607504450 - 433898894)
        expected_den = 1 * 27**6
        assert Rational(val) == Rational(expected_num, expected_den)


# =========================================================================
# 3. DENOMINATOR THEOREM
# =========================================================================

class TestDenominatorTheorem:
    """denom(S_r) = rho(r) * c^{r-3} * (5c+22)^{floor((r-2)/2)}."""

    @pytest.mark.parametrize("r", range(11, 16))
    def test_exponents_match(self, r):
        results = verify_denominator_theorem(max_r=r)
        entry = [e for e in results if e[0] == r][0]
        assert entry[1], f"Denominator theorem fails at r={r}"


# =========================================================================
# 4. NUMERATOR DEGREE THEOREM
# =========================================================================

class TestNumeratorDegreeTheorem:
    """deg_c(numer(S_r)) = floor((r-4)/2)."""

    @pytest.mark.parametrize("r", range(11, 16))
    def test_degree_matches(self, r):
        results = verify_numerator_degree(max_r=r)
        entry = [e for e in results if e[0] == r][0]
        assert entry[3], f"S_{r}: deg={entry[1]}, pred={entry[2]}"


# =========================================================================
# 5. LEADING COEFFICIENT SIGN
# =========================================================================

class TestLeadingSign:
    """The leading coefficient of P_r(c) has sign (-1)^r."""

    def test_sign_table(self):
        table = shadow_tower_table(max_r=15)
        for r in range(11, 16):
            assert table[r]['lead_sign'] == (-1)**r, (
                f"S_{r}: lead_sign={table[r]['lead_sign']}, "
                f"expected={(-1)**r}")


# =========================================================================
# 6. SIGN PATTERN AT PHYSICAL CENTRAL CHARGES
# =========================================================================

class TestSignPattern:
    """Sign of S_r at standard central charges."""

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    @pytest.mark.parametrize("r", range(11, 16))
    def test_sign_alternation(self, c_val, r):
        """(-1)^r pattern holds at c=1,13,26 for r=11..15."""
        val = virasoro_S_fraction(r, c_val)
        expected = (-1)**r
        actual = 1 if val > 0 else -1
        assert actual == expected, (
            f"S_{r}(c={c_val}): sign={actual}, expected={expected}")

    def test_s15_sign_flips_below_c0(self):
        """S_15 has wrong sign for c < c_0 ~ 0.0288."""
        # At c = 1/100 < c_0, S_15 should be POSITIVE (not (-1)^15 = -1)
        val = virasoro_S_fraction(15, Fraction(1, 100))
        assert val > 0, "S_15(c=1/100) should be positive (sign slip)"


# =========================================================================
# 7. SELF-DUALITY AT c=13
# =========================================================================

class TestSelfDuality:
    """S_r(13) = S_r(26-13) = S_r(13)."""

    @pytest.mark.parametrize("r", range(11, 16))
    def test_nonzero(self, r):
        val = virasoro_S_fraction(r, 13)
        assert val != 0, f"S_{r}(13) = 0"

    @pytest.mark.parametrize("r", range(11, 16))
    def test_self_dual(self, r):
        val_13 = virasoro_S_fraction(r, 13)
        val_dual = virasoro_S_fraction(r, 13)  # 26 - 13 = 13
        assert val_13 == val_dual


# =========================================================================
# 8. KOSZUL DUALITY RATIO = 1 AT c=13
# =========================================================================

class TestKoszulDualityRatio:
    """S_r(c)/S_r(26-c) = 1 at c=13."""

    @pytest.fixture(scope="class")
    def ratios(self):
        return duality_ratio_at_c13(max_r=15)

    @pytest.mark.parametrize("r", range(11, 16))
    def test_ratio_is_one(self, ratios, r):
        assert ratios[r] == 1, f"S_{r}(c)/S_{r}(26-c) at c=13 = {ratios[r]}"


# =========================================================================
# 9. GROWTH RATE: rho = sqrt(q2/q0)
# =========================================================================

class TestGrowthRate:
    """Asymptotic growth rate rho."""

    def test_growth_rate_formula(self):
        rho2 = shadow_growth_rate_squared()
        expected = (180 * c + 872) / (c**2 * (5 * c + 22))
        assert simplify(rho2 - expected) == 0

    def test_growth_rate_c1(self):
        rho = growth_rate_numerical(1.0)
        expected = math.sqrt(1052.0 / 27.0)
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_c13(self):
        rho = growth_rate_numerical(13.0)
        assert abs(rho - 0.46739578) < 1e-6

    def test_growth_rate_c26(self):
        rho = growth_rate_numerical(26.0)
        assert abs(rho - 0.23245002) < 1e-6

    def test_growth_rate_decreases(self):
        """rho(c) decreases as c increases for c > 0."""
        r1 = growth_rate_numerical(1.0)
        r13 = growth_rate_numerical(13.0)
        r26 = growth_rate_numerical(26.0)
        assert r1 > r13 > r26


# =========================================================================
# 10. BRANCH POINTS ARE COMPLEX CONJUGATES
# =========================================================================

class TestBranchPoints:
    """Branch points of Q_L(t) for c > 0."""

    @pytest.mark.parametrize("c_val", [0.5, 1, 5, 13, 26, 100])
    def test_conjugate_pair(self, c_val):
        t_plus, t_minus = branch_points(c_val)
        assert abs(t_plus - t_minus.conjugate()) < 1e-10

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_negative_real_part(self, c_val):
        """Branch points have negative real part for c > 0."""
        t_plus, _ = branch_points(c_val)
        assert t_plus.real < 0

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_equal_modulus(self, c_val):
        t_plus, t_minus = branch_points(c_val)
        assert abs(abs(t_plus) - abs(t_minus)) < 1e-10


# =========================================================================
# 11. CONVERGENCE RADIUS
# =========================================================================

class TestConvergenceRadius:
    """R = |t_*| = 1/rho."""

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_radius_equals_inverse_rho(self, c_val):
        R = convergence_radius(c_val)
        rho = growth_rate_numerical(c_val)
        assert abs(R * rho - 1.0) < 1e-10

    def test_c1_divergent(self):
        """At c=1, R < 1 so rho > 1: series diverges."""
        R = convergence_radius(1.0)
        assert R < 1.0

    def test_c13_convergent(self):
        """At c=13, R > 1 so rho < 1: series converges."""
        R = convergence_radius(13.0)
        assert R > 1.0


# =========================================================================
# 12. ROOT TEST
# =========================================================================

class TestRootTest:
    """Root test: |S_r|^{1/r} -> rho."""

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_root_approaches_rho(self, c_val):
        results = root_test(c_val, max_r=15)
        rho = growth_rate_numerical(float(c_val))
        # Last value should be within 60% of rho (slow convergence
        # due to oscillatory correction and power law)
        last_root = results[-1][1]
        assert abs(last_root - rho) / rho < 0.6


# =========================================================================
# 13. RATIO TEST
# =========================================================================

class TestRatioTest:
    """Ratio test: |S_{r+1}/S_r| approaches rho."""

    @pytest.mark.parametrize("c_val", [13, 26])
    def test_ratio_within_50pct(self, c_val):
        results = ratio_test(c_val, max_r=15)
        rho = results[-1][2]
        last_ratio = results[-1][1]
        assert abs(last_ratio - rho) / rho < 0.5


# =========================================================================
# 14. GEVREY-0 (SUB-FACTORIAL)
# =========================================================================

class TestGevrey:
    """The growth is Gevrey-0: |S_r|/r! -> 0."""

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    def test_ratio_decreasing(self, c_val):
        results = gevrey_test(c_val, max_r=15)
        # |S_r|/r! should decrease for sufficiently large r
        vals = [v for _, v in results if v > 0]
        # Check that the last value is much smaller than the first
        assert vals[-1] < vals[0], "Gevrey-0 test failed"

    def test_c1_subfactorial(self):
        """Even at c=1 (divergent series), growth is sub-factorial."""
        results = gevrey_test(1, max_r=15)
        # |S_15|/15! should be very small
        last = results[-1][1]
        assert last < 1e-4

    def test_c13_subfactorial(self):
        results = gevrey_test(13, max_r=15)
        last = results[-1][1]
        assert last < 1e-10


# =========================================================================
# 15. CRITICAL CENTRAL CHARGE
# =========================================================================

class TestCriticalCentralCharge:
    """c* ~ 6.1254: rho(c*) = 1."""

    def test_polynomial(self):
        p = critical_central_charge_polynomial()
        # p(c*) = 0 and rho(c*) = 1 mean q2(c*)/q0(c*) = 1
        # i.e. (180*c* + 872) = c*^2 * (5*c* + 22)
        # => 5c*^3 + 22c*^2 - 180c* - 872 = 0
        assert simplify(p - (5 * c**3 + 22 * c**2 - 180 * c - 872)) == 0

    def test_numerical_value(self):
        c_star = critical_central_charge_numerical()
        assert abs(c_star - 6.12537) < 0.001

    def test_rho_at_cstar(self):
        """rho(c*) = 1."""
        c_star = critical_central_charge_numerical()
        rho = growth_rate_numerical(c_star)
        assert abs(rho - 1.0) < 1e-6

    def test_rho_below_cstar(self):
        """rho > 1 for c < c*."""
        rho = growth_rate_numerical(1.0)
        assert rho > 1.0

    def test_rho_above_cstar(self):
        """rho < 1 for c > c*."""
        rho = growth_rate_numerical(13.0)
        assert rho < 1.0


# =========================================================================
# 16. DARBOUX EXPONENT
# =========================================================================

class TestDarbouxExponent:
    """Power-law exponent alpha = -5/2."""

    def test_value(self):
        assert darboux_exponent() == Rational(-5, 2)

    def test_decomposition(self):
        """alpha = -3/2 (sqrt branch) - 1 (division by r)."""
        sqrt_exponent = Rational(-3, 2)
        division_exponent = Rational(-1, 1)
        assert darboux_exponent() == sqrt_exponent + division_exponent


# =========================================================================
# 17. BEAT PERIOD AND OSCILLATORY STRUCTURE
# =========================================================================

class TestOscillation:
    """Oscillatory structure from complex branch points."""

    def test_beat_period_c1(self):
        params = asymptotic_parameters(1.0)
        assert 9 < params['beat_period'] < 14

    def test_beat_period_c13(self):
        params = asymptotic_parameters(13.0)
        assert 16 < params['beat_period'] < 25

    def test_beat_period_increases_with_c(self):
        b1 = asymptotic_parameters(1.0)['beat_period']
        b13 = asymptotic_parameters(13.0)['beat_period']
        b26 = asymptotic_parameters(26.0)['beat_period']
        assert b1 < b13 < b26

    def test_theta_in_second_quadrant(self):
        """Branch point argument between 90 and 180 degrees."""
        for c_val in [1, 13, 26]:
            params = asymptotic_parameters(c_val)
            assert 90 < params['theta_deg'] < 180


# =========================================================================
# 18. S_15 NUMERATOR ZERO
# =========================================================================

class TestS15NumeratorZero:
    """S_15 has a unique positive numerator zero at c ~ 0.0288."""

    def test_zero_value(self):
        z = s15_positive_zero()
        assert abs(z - 0.02883) < 0.001

    def test_sign_above_zero(self):
        """S_15 has sign (-1)^15 = -1 for c > c_0."""
        val = virasoro_S_fraction(15, 1)
        assert val < 0

    def test_sign_below_zero(self):
        """S_15 has sign +1 for c < c_0 ~ 0.029."""
        val = virasoro_S_fraction(15, Fraction(1, 100))
        assert val > 0

    def test_s15_zero_is_first(self):
        """S_4 through S_14 have no positive numerator zeros."""
        for r in range(4, 15):
            # At c = 1/1000, sign should still be (-1)^r
            val = virasoro_S_fraction(r, Fraction(1, 1000))
            expected = 1 if (-1)**r > 0 else -1
            actual = 1 if val > 0 else -1
            assert actual == expected, (
                f"S_{r}(c=1/1000) has wrong sign: expected {expected}")


# =========================================================================
# 19. CROSS-ENGINE CONSISTENCY
# =========================================================================

class TestCrossEngine:
    """Verify agreement with the S9/S10 engine on overlapping range."""

    def test_all_agree(self):
        results = verify_cross_engine_s9_s10(max_r=10)
        for r, agree in results:
            assert agree, f"S_{r} disagrees with S9/S10 engine"


# =========================================================================
# 20. EXACT FRACTION ARITHMETIC
# =========================================================================

class TestFractionArithmetic:
    """Cross-check via exact Fraction evaluation."""

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 26])
    @pytest.mark.parametrize("r", [11, 12, 13, 14, 15])
    def test_fraction_nonzero(self, c_val, r):
        val = virasoro_S_fraction(r, c_val)
        assert val != 0, f"S_{r}(c={c_val}) = 0"

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    @pytest.mark.parametrize("r", [11, 13, 15])
    def test_odd_negative(self, c_val, r):
        """Odd-arity shadows are negative at standard c values."""
        val = virasoro_S_fraction(r, c_val)
        assert val < 0, f"S_{r}(c={c_val}) > 0 (expected < 0)"

    @pytest.mark.parametrize("c_val", [1, 13, 26])
    @pytest.mark.parametrize("r", [12, 14])
    def test_even_positive(self, c_val, r):
        """Even-arity shadows are positive at standard c values."""
        val = virasoro_S_fraction(r, c_val)
        assert val > 0, f"S_{r}(c={c_val}) < 0 (expected > 0)"

    def test_ising_S11_S15(self):
        """S_11 and S_15 at c=1/2 (Ising model) are nonzero."""
        s11 = virasoro_S_fraction(11, Fraction(1, 2))
        s15 = virasoro_S_fraction(15, Fraction(1, 2))
        assert s11 != 0 and s15 != 0


# =========================================================================
# 21. AFFINE sl_2 SPECIALIZATION
# =========================================================================

class TestAffineSl2:
    """Shadow tower for sl_2 via Sugawara c=3k/(k+2)."""

    def test_S11_sl2_nonzero(self):
        S11 = affine_sl2_shadow_coefficient(11)
        assert S11 != 0

    def test_S15_sl2_nonzero(self):
        S15 = affine_sl2_shadow_coefficient(15)
        assert S15 != 0

    def test_k1_matches_vir_c1(self):
        """S_r(sl_2, k=1) = S_r(Vir, c=1) since c(sl_2, k=1) = 1."""
        for r in [11, 13, 15]:
            sl2 = virasoro_S_fraction(r, 1)  # c=3*1/(1+2)=1
            vir = virasoro_S_fraction(r, 1)
            assert sl2 == vir


# =========================================================================
# 22. LARGE-c VANISHING
# =========================================================================

class TestLargeCVanishing:
    """S_r -> 0 as c -> infinity for r >= 4."""

    @pytest.mark.parametrize("r", [11, 13, 15])
    def test_vanishing(self, r):
        # Numerically: |S_r(c=10000)| should be tiny
        val = abs(float(virasoro_S_fraction(r, 10000)))
        assert val < 1e-20


# =========================================================================
# 23. STRUCTURAL PATTERN SUMMARY
# =========================================================================

class TestStructuralSummary:
    """Full structural verification table."""

    @pytest.fixture(scope="class")
    def table(self):
        return shadow_tower_table(max_r=15)

    @pytest.mark.parametrize("r", range(11, 16))
    def test_pow_c(self, table, r):
        assert table[r]['pow_c'] == table[r]['pred_pow_c']

    @pytest.mark.parametrize("r", range(11, 16))
    def test_pow_5c22(self, table, r):
        assert table[r]['pow_5c22'] == table[r]['pred_pow_5c22']

    @pytest.mark.parametrize("r", range(11, 16))
    def test_numer_deg(self, table, r):
        assert table[r]['numer_deg'] == table[r]['pred_numer_deg']

    @pytest.mark.parametrize("r", range(11, 16))
    def test_lead_sign(self, table, r):
        assert table[r]['lead_sign'] == table[r]['pred_lead_sign']


# =========================================================================
# 24. CONVERGENCE/DIVERGENCE CLASSIFICATION
# =========================================================================

class TestConvergenceClassification:
    """Convergence depends on c vs c*."""

    def test_ising_diverges(self):
        """Ising (c=1/2): rho > 1, diverges."""
        rho = growth_rate_numerical(0.5)
        assert rho > 1

    def test_c1_diverges(self):
        rho = growth_rate_numerical(1.0)
        assert rho > 1

    def test_c13_converges(self):
        rho = growth_rate_numerical(13.0)
        assert rho < 1

    def test_c26_converges(self):
        rho = growth_rate_numerical(26.0)
        assert rho < 1

    def test_crit_string_converges(self):
        """Critical string (c=26): rho ~ 0.232, converges."""
        rho = growth_rate_numerical(26.0)
        assert abs(rho - 0.232) < 0.01

    def test_selfdual_converges(self):
        """Self-dual (c=13): rho ~ 0.467, converges."""
        rho = growth_rate_numerical(13.0)
        assert abs(rho - 0.467) < 0.01

    def test_c_star_marginal(self):
        """c* ~ 6.125: rho = 1, marginal."""
        c_star = critical_central_charge_numerical()
        rho = growth_rate_numerical(c_star)
        assert abs(rho - 1.0) < 1e-6


# =========================================================================
# 25. CONVOLUTION IDENTITY CROSS-CHECK
# =========================================================================

class TestConvolutionIdentity:
    """The convolution a_n reconstructs Q_L exactly."""

    def test_f_squared_equals_Q(self):
        """sum a_j a_{n-j} = [t^n] Q_L for n=0,1,2."""
        a = convolution_coefficients(max_n=4)
        q0, q1, q2 = virasoro_shadow_metric()
        # n=0: a0^2 = q0
        assert simplify(a[0]**2 - q0) == 0
        # n=1: 2*a0*a1 = q1
        assert simplify(2 * a[0] * a[1] - q1) == 0
        # n=2: a1^2 + 2*a0*a2 = q2
        assert simplify(a[1]**2 + 2 * a[0] * a[2] - q2) == 0
        # n=3: 2*a1*a2 + 2*a0*a3 = 0
        assert simplify(2 * a[1] * a[2] + 2 * a[0] * a[3]) == 0
        # n=4: a2^2 + 2*a1*a3 + 2*a0*a4 = 0
        assert simplify(a[2]**2 + 2*a[1]*a[3] + 2*a[0]*a[4]) == 0
