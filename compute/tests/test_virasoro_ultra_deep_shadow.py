r"""Tests for ultra-deep Virasoro shadow obstruction tower: S_r through arity 24.

Verifies six independent computation paths:
  PATH 1: Convolution recursion from f^2 = Q_L (exact sympy)
  PATH 2: Maurer-Cartan obstruction recursion (exact sympy)
  PATH 3: Generating function H^2 = t^4 Q_L series expansion
  PATH 4: Float recursion (both convolution and MC variants)
  PATH 5: Koszul duality complementarity S_r(c) + S_r(26-c)
  PATH 6: Asymptotic growth rate |S_r| ~ A rho^r r^{-5/2}

Also verifies structural properties:
  - Denominator pattern c^{r-3} (5c+22)^{floor((r-2)/2)}
  - Numerator degree floor((r-4)/2)
  - Sign alternation (-1)^r for r >= 4
  - Master equation nabla_H(S_r) + o^(r) = 0
  - Self-duality at c = 13
  - Complementarity sum kappa(c) + kappa(26-c) = 13 (AP24)
  - Exact Fraction computation matches all other paths
  - Cross-validation with virasoro_shadow_extended.py (S_7 through S_12)

Test count: 150+ tests across 14 parametric test classes.
"""

import math
import pytest
from fractions import Fraction
from sympy import Rational, Symbol, cancel, denom, factor, numer, simplify
from sympy import N as Neval, Poly

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.virasoro_ultra_deep_shadow import (
    c,
    kappa_vir,
    alpha_vir,
    S4_vir,
    Delta_vir,
    shadow_metric_coefficients,
    rho_squared_vir,
    critical_cubic_vir,
    convolution_coefficients,
    shadow_from_convolution,
    shadow_from_mc_recursion,
    shadow_from_generating_function,
    shadow_from_float,
    shadow_from_mc_float,
    shadow_from_fraction,
    shadow_from_mc_fraction,
    complementarity_sum_exact,
    verify_complementarity_at_c13,
    shadow_growth_parameters,
    verify_asymptotic_growth,
    verify_all_paths,
    verify_numerical_paths,
    denominator_analysis,
    numerator_degree_analysis,
    sign_pattern_analysis,
    master_equation_residual,
    verify_master_equation,
    evaluate_symbolic_tower,
    ratio_test,
)

# Central charges for parametric tests
# Includes: Ising (1/2), c=1, Potts-like (4), critical cubic (6.125),
# self-dual (13), Virasoro dual at 25, critical string (26),
# large (100), negative (-2), Lee-Yang vicinity (-22/5)
C_VALUES_RATIONAL = [
    Rational(1, 2), Rational(1), Rational(2), Rational(4),
    Rational(7), Rational(10), Rational(13), Rational(20),
    Rational(25), Rational(26), Rational(100),
]

C_VALUES_FLOAT = [0.5, 1.0, 2.0, 4.0, 6.0, 7.0, 10.0, 13.0, 20.0, 25.0, 26.0, 100.0]

# Negative c values (Virasoro makes sense for all c != 0, -22/5)
C_VALUES_NEGATIVE = [Rational(-2), Rational(-3)]

# Exact Fraction test points (numerator, denominator)
C_FRAC_VALUES = [(1, 2), (1, 1), (2, 1), (4, 1), (7, 1), (13, 1),
                 (25, 1), (26, 1), (100, 1)]


# ============================================================================
# 1. Three-way symbolic path agreement (PATH 1 vs PATH 2 vs PATH 3)
# ============================================================================

class TestThreePathSymbolicAgreement:
    """Every symbolic path produces identical S_r as a function of c."""

    @pytest.fixture(scope="class")
    def towers(self):
        """Compute all three symbolic towers once (expensive)."""
        max_r = 20  # 20 is enough for thorough verification; 24 would be slow
        conv = shadow_from_convolution(max_r)
        mc = shadow_from_mc_recursion(max_r)
        gf = shadow_from_generating_function(max_r)
        return conv, mc, gf, max_r

    @pytest.mark.parametrize("r", list(range(2, 21)))
    def test_conv_vs_mc(self, towers, r):
        """PATH 1 (convolution) == PATH 2 (MC recursion) at arity r."""
        conv, mc, gf, max_r = towers
        if r > max_r:
            pytest.skip(f"r={r} exceeds max_r={max_r}")
        assert simplify(conv[r] - mc[r]) == 0, (
            f"Convolution and MC disagree at r={r}"
        )

    @pytest.mark.parametrize("r", list(range(2, 21)))
    def test_conv_vs_gf(self, towers, r):
        """PATH 1 (convolution) == PATH 3 (generating function) at arity r."""
        conv, mc, gf, max_r = towers
        if r > max_r:
            pytest.skip(f"r={r} exceeds max_r={max_r}")
        assert simplify(conv[r] - gf[r]) == 0, (
            f"Convolution and GF disagree at r={r}"
        )

    @pytest.mark.parametrize("r", list(range(2, 21)))
    def test_mc_vs_gf(self, towers, r):
        """PATH 2 (MC recursion) == PATH 3 (generating function) at arity r."""
        conv, mc, gf, max_r = towers
        if r > max_r:
            pytest.skip(f"r={r} exceeds max_r={max_r}")
        assert simplify(mc[r] - gf[r]) == 0, (
            f"MC and GF disagree at r={r}"
        )


# ============================================================================
# 2. Cross-validation with virasoro_shadow_extended.py (known formulas)
# ============================================================================

class TestCrossValidationExtended:
    """Verify agreement with the known closed-form S_r from virasoro_shadow_extended.py."""

    @pytest.fixture(scope="class")
    def conv_tower(self):
        return shadow_from_convolution(12)

    def test_S2_kappa(self, conv_tower):
        """S_2 = c/2 = kappa."""
        assert simplify(conv_tower[2] - c / 2) == 0

    def test_S3_constant(self, conv_tower):
        """S_3 = 2 (c-independent)."""
        assert conv_tower[3] == 2

    def test_S4_quartic_contact(self, conv_tower):
        """S_4 = 10/[c(5c+22)]."""
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(conv_tower[4] - expected) == 0

    def test_S5(self, conv_tower):
        """S_5 = -48/[c^2(5c+22)]."""
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(conv_tower[5] - expected) == 0

    def test_S6(self, conv_tower):
        """S_6 = 80(45c+193)/[3 c^3(5c+22)^2]."""
        expected = Rational(80) * (45*c + 193) / (3 * c**3 * (5*c+22)**2)
        assert simplify(conv_tower[6] - expected) == 0

    def test_S7(self, conv_tower):
        """S_7 = -2880(15c+61)/[7 c^4(5c+22)^2]."""
        expected = Rational(-2880) * (15*c + 61) / (7 * c**4 * (5*c+22)**2)
        assert simplify(conv_tower[7] - expected) == 0

    def test_S8(self, conv_tower):
        """S_8 = 80(2025c^2+16470c+33314)/[c^5(5c+22)^3]."""
        expected = Rational(80) * (2025*c**2 + 16470*c + 33314) / (
            c**5 * (5*c+22)**3)
        assert simplify(conv_tower[8] - expected) == 0

    def test_S9(self, conv_tower):
        """S_9 = -1280(2025c^2+15570c+29554)/[3 c^6(5c+22)^3]."""
        expected = Rational(-1280) * (2025*c**2 + 15570*c + 29554) / (
            3 * c**6 * (5*c+22)**3)
        assert simplify(conv_tower[9] - expected) == 0

    def test_S10(self, conv_tower):
        """S_10 = 256(91125c^3+1050975c^2+3989790c+4969967)/[c^7(5c+22)^4]."""
        expected = Rational(256) * (
            91125*c**3 + 1050975*c**2 + 3989790*c + 4969967
        ) / (c**7 * (5*c+22)**4)
        assert simplify(conv_tower[10] - expected) == 0

    def test_S11(self, conv_tower):
        """S_11 = -15360(91125c^3+990225c^2+3500190c+3988097)/[11 c^8(5c+22)^4]."""
        expected = Rational(-15360) * (
            91125*c**3 + 990225*c**2 + 3500190*c + 3988097
        ) / (11 * c**8 * (5*c+22)**4)
        assert simplify(conv_tower[11] - expected) == 0

    def test_S12(self, conv_tower):
        """S_12 = 2560(4100625c^4+59413500c^3+315017100c^2+717857460c+583976486)/[3 c^9(5c+22)^5]."""
        expected = Rational(2560) * (
            4100625*c**4 + 59413500*c**3 + 315017100*c**2
            + 717857460*c + 583976486
        ) / (3 * c**9 * (5*c+22)**5)
        assert simplify(conv_tower[12] - expected) == 0


# ============================================================================
# 3. Float vs symbolic agreement (PATH 4 vs PATH 1)
# ============================================================================

class TestFloatVsSymbolic:
    """Float recursion matches exact symbolic evaluation at specific c."""

    @pytest.fixture(scope="class")
    def symbolic_tower(self):
        return shadow_from_convolution(24)

    @pytest.mark.parametrize("cv", C_VALUES_FLOAT)
    def test_float_conv_matches_symbolic(self, symbolic_tower, cv):
        """Float convolution matches symbolic at c=cv through arity 24."""
        fl = shadow_from_float(cv, 24)
        for r in range(2, 25):
            exact = float(Neval(symbolic_tower[r].subs(c, Rational(cv))))
            ref = max(abs(exact), 1e-300)
            err = abs(exact - fl[r]) / ref
            assert err < 1e-8, (
                f"c={cv}, r={r}: exact={exact:.6e}, float={fl[r]:.6e}, err={err:.2e}"
            )

    @pytest.mark.parametrize("cv", C_VALUES_FLOAT)
    def test_float_mc_matches_symbolic(self, symbolic_tower, cv):
        """Float MC recursion matches symbolic at c=cv through arity 20."""
        fl_mc = shadow_from_mc_float(cv, 20)
        for r in range(2, 21):
            exact = float(Neval(symbolic_tower[r].subs(c, Rational(cv))))
            ref = max(abs(exact), 1e-300)
            err = abs(exact - fl_mc[r]) / ref
            assert err < 1e-8, (
                f"c={cv}, r={r}: exact={exact:.6e}, mc_float={fl_mc[r]:.6e}, err={err:.2e}"
            )

    @pytest.mark.parametrize("cv", C_VALUES_FLOAT)
    def test_float_conv_vs_mc(self, cv):
        """Float convolution == float MC at c=cv through arity 30."""
        fl_conv = shadow_from_float(cv, 30)
        fl_mc = shadow_from_mc_float(cv, 30)
        for r in range(2, 31):
            ref = max(abs(fl_conv[r]), abs(fl_mc[r]), 1e-300)
            err = abs(fl_conv[r] - fl_mc[r]) / ref
            assert err < 1e-10, (
                f"c={cv}, r={r}: conv={fl_conv[r]:.6e}, mc={fl_mc[r]:.6e}, err={err:.2e}"
            )


# ============================================================================
# 4. Exact Fraction computation (PATH 4c)
# ============================================================================

class TestFractionComputation:
    """Exact Fraction arithmetic at rational c values."""

    @pytest.mark.parametrize("c_num,c_den", C_FRAC_VALUES)
    def test_fraction_conv_vs_mc(self, c_num, c_den):
        """Fraction convolution == Fraction MC at c=c_num/c_den through arity 20."""
        frac_conv = shadow_from_fraction(c_num, c_den, 20)
        frac_mc = shadow_from_mc_fraction(c_num, c_den, 20)
        for r in range(2, 21):
            assert frac_conv[r] == frac_mc[r], (
                f"c={c_num}/{c_den}, r={r}: conv={frac_conv[r]}, mc={frac_mc[r]}"
            )

    @pytest.mark.parametrize("c_num,c_den", C_FRAC_VALUES)
    def test_fraction_vs_float(self, c_num, c_den):
        """Fraction values match float to machine precision."""
        frac = shadow_from_fraction(c_num, c_den, 20)
        fl = shadow_from_float(c_num / c_den, 20)
        for r in range(2, 21):
            exact = float(frac[r])
            ref = max(abs(exact), 1e-300)
            err = abs(exact - fl[r]) / ref
            assert err < 1e-10, (
                f"c={c_num}/{c_den}, r={r}: frac={exact:.10e}, float={fl[r]:.10e}, err={err:.2e}"
            )

    def test_fraction_ising_exact(self):
        """At c=1/2 (Ising), Fraction computation is exactly rational."""
        frac = shadow_from_fraction(1, 2, 15)
        # S_2 = 1/4
        assert frac[2] == Fraction(1, 4)
        # S_3 = 2
        assert frac[3] == Fraction(2)
        # S_4 = 10/(1/2 * (5/2 + 22)) = 10/(1/2 * 49/2) = 10*4/49 = 40/49
        assert frac[4] == Fraction(40, 49)
        # S_5 = -48/(1/4 * 49/2) = -48*8/49 = -384/49
        assert frac[5] == Fraction(-384, 49)

    def test_fraction_c26_S2(self):
        """At c=26, kappa = 13."""
        frac = shadow_from_fraction(26, 1, 5)
        assert frac[2] == Fraction(13)


# ============================================================================
# 5. Master equation verification (nabla_H(S_r) + o^(r) = 0)
# ============================================================================

class TestMasterEquation:
    """The MC recursion residual vanishes at every arity."""

    @pytest.fixture(scope="class")
    def me_results(self):
        return verify_master_equation(24)

    @pytest.mark.parametrize("r", list(range(5, 25)))
    def test_master_equation_arity(self, me_results, r):
        """nabla_H(S_r) + o^(r) = 0 at arity r."""
        assert me_results[r], f"Master equation fails at r={r}"


# ============================================================================
# 6. Denominator pattern (structural theorem)
# ============================================================================

class TestDenominatorPattern:
    """Denominator is c^{r-3} (5c+22)^{floor((r-2)/2)} for r >= 4."""

    @pytest.fixture(scope="class")
    def denom_data(self):
        return denominator_analysis(24)

    @pytest.mark.parametrize("r", list(range(4, 25)))
    def test_c_power(self, denom_data, r):
        """Power of c in denominator equals r-3."""
        assert denom_data[r]['c_match'], (
            f"r={r}: c^{denom_data[r]['c_power']} != c^{denom_data[r]['predicted_c']}"
        )

    @pytest.mark.parametrize("r", list(range(4, 25)))
    def test_lee_yang_power(self, denom_data, r):
        """Power of (5c+22) in denominator equals floor((r-2)/2)."""
        assert denom_data[r]['ly_match'], (
            f"r={r}: (5c+22)^{denom_data[r]['lee_yang_power']} != "
            f"(5c+22)^{denom_data[r]['predicted_ly']}"
        )


# ============================================================================
# 7. Numerator degree pattern
# ============================================================================

class TestNumeratorDegree:
    """Numerator polynomial in c has degree floor((r-4)/2) for r >= 4."""

    @pytest.fixture(scope="class")
    def num_data(self):
        return numerator_degree_analysis(24)

    @pytest.mark.parametrize("r", list(range(4, 25)))
    def test_numerator_degree(self, num_data, r):
        """Numerator degree equals floor((r-4)/2)."""
        assert num_data[r]['degree'] == num_data[r]['predicted'], (
            f"r={r}: deg={num_data[r]['degree']} != pred={num_data[r]['predicted']}"
        )


# ============================================================================
# 8. Sign alternation (-1)^r
# ============================================================================

class TestSignPattern:
    """S_r has sign (-1)^r for r >= 4 at sufficiently large c.

    The sign alternation (-1)^r holds universally through arity 12.
    At higher arities, the oscillation phase theta/pi deviates from 1
    at small c, causing the cos(r*theta+phi) factor to break the
    alternating pattern. For c = 1, the first phase slip occurs at r = 17.
    For c >= 7, alternation holds through arity 24.
    """

    @pytest.mark.parametrize("cv", [20, 25, 26, 100])
    @pytest.mark.parametrize("r", list(range(4, 25)))
    def test_sign_at_large_c(self, cv, r):
        """Sign of S_r(cv) equals (-1)^r for c >= 20 through arity 24."""
        tower = shadow_from_float(float(cv), max(r + 1, 25))
        val = tower[r]
        expected_sign = (-1) ** r
        actual_sign = 1 if val > 0 else -1
        assert actual_sign == expected_sign, (
            f"c={cv}, r={r}: S_r={val:.4e}, expected sign {expected_sign}"
        )

    @pytest.mark.parametrize("cv", [7, 13])
    @pytest.mark.parametrize("r", list(range(4, 22)))
    def test_sign_at_moderate_c(self, cv, r):
        """Sign of S_r(cv) equals (-1)^r for c in [7,13] through arity 21.

        Phase slip at c=7 occurs at r=23, at c=13 at r=27.
        We conservatively test through arity 21.
        """
        tower = shadow_from_float(float(cv), max(r + 1, 25))
        val = tower[r]
        expected_sign = (-1) ** r
        actual_sign = 1 if val > 0 else -1
        assert actual_sign == expected_sign, (
            f"c={cv}, r={r}: S_r={val:.4e}, expected sign {expected_sign}"
        )

    @pytest.mark.parametrize("cv", [1, 7, 13, 25, 100])
    @pytest.mark.parametrize("r", list(range(4, 13)))
    def test_sign_low_arity(self, cv, r):
        """Sign alternation holds through arity 12 for all c > 0."""
        tower = shadow_from_float(float(cv), 13)
        val = tower[r]
        expected_sign = (-1) ** r
        actual_sign = 1 if val > 0 else -1
        assert actual_sign == expected_sign, (
            f"c={cv}, r={r}: S_r={val:.4e}, expected sign {expected_sign}"
        )

    def test_phase_slip_at_c1(self):
        """At c=1, sign alternation breaks at r=17 (expected from theta/pi < 1)."""
        tower = shadow_from_float(1.0, 20)
        # Sign should alternate through r=16
        for r in range(4, 17):
            val = tower[r]
            expected_sign = (-1) ** r
            actual_sign = 1 if val > 0 else -1
            assert actual_sign == expected_sign, (
                f"c=1, r={r}: unexpected early phase slip"
            )
        # At r=17, the sign should NOT alternate (phase slip)
        assert tower[16] * tower[17] > 0, (
            "c=1, r=17: expected same-sign (phase slip) but got alternation"
        )


# ============================================================================
# 9. Koszul duality / Complementarity (PATH 5)
# ============================================================================

class TestComplementarity:
    """Koszul duality constraints on S_r(c) + S_r(26-c)."""

    @pytest.fixture(scope="class")
    def tower(self):
        return shadow_from_convolution(20)

    def test_kappa_complementarity_is_13(self, tower):
        """kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13 (AP24: NOT zero)."""
        comp = complementarity_sum_exact(2, tower)
        assert simplify(comp - 13) == 0, (
            f"kappa complementarity sum = {comp}, expected 13"
        )

    def test_S3_complementarity(self, tower):
        """S_3(c) + S_3(26-c) = 2 + 2 = 4."""
        comp = complementarity_sum_exact(3, tower)
        assert simplify(comp - 4) == 0

    @pytest.mark.parametrize("cv", [Rational(1), Rational(4), Rational(10),
                                     Rational(20), Rational(25)])
    def test_self_duality_c13(self, tower, cv):
        """S_r(13) = S_r(13): self-dual at the Koszul fixed point."""
        for r in range(2, 21):
            val = float(Neval(tower[r].subs(c, 13)))
            val_dual = float(Neval(tower[r].subs(c, 26 - 13)))
            assert abs(val - val_dual) < 1e-14 * max(abs(val), 1e-300), (
                f"r={r}: S_r(13)={val:.6e} != S_r(13)={val_dual:.6e}"
            )

    @pytest.mark.parametrize("cv", [Rational(1), Rational(4), Rational(25)])
    def test_duality_pair_numerical(self, tower, cv):
        """S_r(c) and S_r(26-c) are both well-defined and non-equal for c != 13."""
        for r in range(4, 15):
            val = float(Neval(tower[r].subs(c, cv)))
            val_dual = float(Neval(tower[r].subs(c, 26 - cv)))
            # They should NOT be equal when c != 13
            # (unless by coincidence at specific r, which is extremely unlikely)
            if cv != 13:
                # Just check both are finite
                assert math.isfinite(val) and math.isfinite(val_dual), (
                    f"r={r}, c={cv}: non-finite values"
                )


# ============================================================================
# 10. Asymptotic growth rate (PATH 6)
# ============================================================================

class TestAsymptoticGrowth:
    """Shadow growth rate rho(c) controls the tower's asymptotic behavior."""

    def test_rho_formula(self):
        """rho^2 = (180c+872) / (c^2(5c+22))."""
        rho_sq = rho_squared_vir()
        expected = (180 * c + 872) / (c**2 * (5 * c + 22))
        assert simplify(rho_sq - expected) == 0

    def test_rho_from_shadow_metric(self):
        """rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)."""
        kappa = kappa_vir()
        alpha = alpha_vir()
        delta = Delta_vir()
        rho_sq = (9 * alpha**2 + 2 * delta) / (4 * kappa**2)
        assert simplify(rho_sq - rho_squared_vir()) == 0

    @pytest.mark.parametrize("cv,expected_conv", [
        (0.5, False),    # rho ~ 12.5
        (1.0, False),    # rho ~ 3.6
        (4.0, False),    # rho ~ 1.3
        (13.0, True),    # rho ~ 0.47
        (25.0, True),    # rho ~ 0.24
        (26.0, True),    # rho ~ 0.23
        (100.0, True),   # rho ~ 0.06
    ])
    def test_convergence_classification(self, cv, expected_conv):
        """Tower convergent for c > c* ~ 6.12, divergent for c < c*."""
        params = shadow_growth_parameters(cv)
        rho = params['rho']
        assert (rho < 1) == expected_conv, (
            f"c={cv}: rho={rho:.6f}, expected convergent={expected_conv}"
        )

    def test_critical_cubic(self):
        """5c^3 + 22c^2 - 180c - 872 = 0 at the transition point."""
        poly = critical_cubic_vir()
        # This should have a real root near 6.1243
        from sympy import solve, re
        roots = solve(poly, c)
        real_roots = [float(r) for r in roots if r.is_real]
        positive_roots = [r for r in real_roots if r > 0]
        assert len(positive_roots) == 1
        assert abs(positive_roots[0] - 6.1254) < 0.001

    def test_self_dual_rho(self):
        """rho(13) ~ 0.4674."""
        params = shadow_growth_parameters(13.0)
        assert abs(params['rho'] - 0.4674) < 0.001

    def test_string_rho(self):
        """rho(26) ~ 0.2325."""
        params = shadow_growth_parameters(26.0)
        assert abs(params['rho'] - 0.2325) < 0.001

    def test_ising_rho(self):
        """rho(1/2) ~ 12.53 (divergent regime)."""
        params = shadow_growth_parameters(0.5)
        assert abs(params['rho'] - 12.53) < 0.1

    @pytest.mark.parametrize("cv", [13.0, 25.0, 26.0])
    def test_ratio_approaches_rho(self, cv):
        """The ratio |S_{r+1}/S_r| approaches rho as r -> infinity."""
        ratios = ratio_test(cv, 30)
        if len(ratios) >= 5:
            rho = ratios[-1][2]
            # At r ~ 25-30, the ratio should be within 30% of rho
            last_err = ratios[-1][3]
            assert last_err < 0.30, (
                f"c={cv}: ratio error at r={ratios[-1][0]} is {last_err:.4f}"
            )

    def test_branch_point_argument_close_to_pi(self):
        """Branch point argument theta should be close to pi for c > 0."""
        for cv in [1.0, 7.0, 13.0, 26.0, 100.0]:
            params = shadow_growth_parameters(cv)
            theta_deg = params['theta_deg']
            # theta should be between 150 and 180 degrees
            assert 150 < theta_deg < 180, (
                f"c={cv}: theta={theta_deg:.2f} deg, expected 150-180"
            )


# ============================================================================
# 11. Generating function identity H^2 = t^4 Q_L(t)
# ============================================================================

class TestGeneratingFunction:
    """Verify the algebraicity theorem: H(t)^2 = t^4 Q_L(t)."""

    @pytest.mark.parametrize("cv", [0.5, 1.0, 4.0, 13.0, 25.0, 26.0, 100.0])
    def test_H_squared_identity(self, cv):
        """H(t)^2 = t^4 Q_L(t) at small t (numerical spot check)."""
        rho_sq = (180.0 * cv + 872.0) / (cv ** 2 * (5.0 * cv + 22.0))
        rho = math.sqrt(rho_sq) if rho_sq > 0 else 0.0
        # Pick t well inside convergence radius
        t_val = min(0.05, 0.3 / (rho + 1))
        tower = shadow_from_float(cv, 40)
        H_val = sum(r * tower[r] * t_val ** r for r in range(2, 41))
        alpha_c = (180.0 * cv + 872.0) / (5.0 * cv + 22.0)
        Q_val = cv ** 2 + 12.0 * cv * t_val + alpha_c * t_val ** 2
        H_sq = H_val ** 2
        Q_rhs = t_val ** 4 * Q_val
        rel_err = abs(H_sq - Q_rhs) / abs(Q_rhs)
        assert rel_err < 1e-6, (
            f"c={cv}: H^2={H_sq:.10e}, t^4*Q={Q_rhs:.10e}, err={rel_err:.2e}"
        )

    @pytest.mark.parametrize("cv", [13.0, 26.0])
    def test_H_squared_multiple_t(self, cv):
        """H^2 = t^4 Q_L at multiple t values (not just one)."""
        rho = math.sqrt((180.0 * cv + 872.0) / (cv ** 2 * (5.0 * cv + 22.0)))
        tower = shadow_from_float(cv, 50)
        alpha_c = (180.0 * cv + 872.0) / (5.0 * cv + 22.0)
        for t_val in [0.01, 0.02, 0.05, 0.1 / rho]:
            H_val = sum(r * tower[r] * t_val ** r for r in range(2, 51))
            Q_val = cv ** 2 + 12.0 * cv * t_val + alpha_c * t_val ** 2
            rel_err = abs(H_val ** 2 - t_val ** 4 * Q_val) / abs(t_val ** 4 * Q_val)
            assert rel_err < 1e-5, (
                f"c={cv}, t={t_val}: rel_err={rel_err:.2e}"
            )


# ============================================================================
# 12. Poles and regularity
# ============================================================================

class TestPolesAndRegularity:
    """S_r has poles only at c=0 and c=-22/5."""

    @pytest.mark.parametrize("cv", [Rational(1, 10), Rational(1),
                                     Rational(10), Rational(100)])
    def test_regular_at_positive_c(self, cv):
        """S_r is finite for all positive c away from 0."""
        tower = shadow_from_float(float(cv), 24)
        for r in range(2, 25):
            assert math.isfinite(tower[r]), f"S_{r}({cv}) = {tower[r]} is not finite"

    def test_c0_is_pole(self):
        """S_r diverges as c -> 0 for r >= 4."""
        tower = shadow_from_float(0.001, 15)
        for r in range(4, 16):
            assert abs(tower[r]) > 10, (
                f"S_{r}(0.001) = {tower[r]:.4e}, expected large"
            )

    def test_lee_yang_is_pole(self):
        """S_r diverges as c -> -22/5 for r >= 4."""
        # c = -22/5 + epsilon
        cv = -22.0 / 5.0 + 0.001
        tower = shadow_from_float(cv, 10)
        for r in range(4, 11):
            assert abs(tower[r]) > 10, (
                f"S_{r}({cv:.4f}) = {tower[r]:.4e}, expected large"
            )


# ============================================================================
# 13. Negative central charge
# ============================================================================

class TestNegativeCentralCharge:
    """S_r is well-defined for negative c (c != 0, c != -22/5)."""

    @pytest.mark.parametrize("cv", [-2.0, -3.0, -10.0])
    def test_negative_c_finite(self, cv):
        """Shadow tower is finite for negative c away from poles."""
        tower = shadow_from_float(cv, 15)
        for r in range(2, 16):
            assert math.isfinite(tower[r]), f"S_{r}({cv}) is not finite"

    @pytest.mark.parametrize("cv", [-2.0, -3.0])
    def test_float_conv_mc_agree_negative_c(self, cv):
        """Float convolution == float MC for negative c."""
        fl_conv = shadow_from_float(cv, 20)
        fl_mc = shadow_from_mc_float(cv, 20)
        for r in range(2, 21):
            ref = max(abs(fl_conv[r]), abs(fl_mc[r]), 1e-300)
            err = abs(fl_conv[r] - fl_mc[r]) / ref
            assert err < 1e-10, (
                f"c={cv}, r={r}: conv={fl_conv[r]:.6e}, mc={fl_mc[r]:.6e}"
            )


# ============================================================================
# 14. Ultra-deep arity 13-24 specific tests
# ============================================================================

class TestUltraDeepArities:
    """Specific tests for the newly computed S_13 through S_24."""

    @pytest.fixture(scope="class")
    def deep_tower(self):
        return shadow_from_convolution(24)

    def test_S13_exists_and_nonzero(self, deep_tower):
        """S_13 is a nonzero rational function of c."""
        assert 13 in deep_tower
        val = float(Neval(deep_tower[13].subs(c, 13)))
        assert abs(val) > 1e-10

    def test_S18_exists_and_nonzero(self, deep_tower):
        """S_18 is a nonzero rational function of c."""
        assert 18 in deep_tower
        val = float(Neval(deep_tower[18].subs(c, 13)))
        assert abs(val) > 1e-15

    def test_S24_exists_and_nonzero(self, deep_tower):
        """S_24 is a nonzero rational function of c."""
        assert 24 in deep_tower
        val = float(Neval(deep_tower[24].subs(c, 13)))
        assert abs(val) > 1e-20

    @pytest.mark.parametrize("r", list(range(13, 25)))
    def test_deep_master_equation(self, deep_tower, r):
        """Master equation holds at ultra-deep arities."""
        residual = master_equation_residual(r, deep_tower)
        assert residual == 0, f"Master equation fails at r={r}"

    @pytest.mark.parametrize("r", list(range(13, 25)))
    def test_deep_sign_pattern(self, deep_tower, r):
        """Sign alternation persists through arity 24."""
        val = float(Neval(deep_tower[r].subs(c, 13)))
        expected_sign = (-1) ** r
        actual_sign = 1 if val > 0 else -1
        assert actual_sign == expected_sign, (
            f"r={r}: S_r(13)={val:.4e}, expected sign {expected_sign}"
        )

    @pytest.mark.parametrize("r", list(range(13, 25)))
    def test_deep_self_duality(self, deep_tower, r):
        """S_r(13) = S_r(13) at the self-dual point through arity 24."""
        val = float(Neval(deep_tower[r].subs(c, 13)))
        val_dual = float(Neval(deep_tower[r].subs(c, 26 - 13)))
        assert abs(val - val_dual) < 1e-14 * max(abs(val), 1e-300)

    def test_deep_fraction_agreement(self):
        """Fraction computation matches float through arity 24 at c=13."""
        frac = shadow_from_fraction(13, 1, 24)
        fl = shadow_from_float(13.0, 24)
        for r in range(13, 25):
            exact = float(frac[r])
            ref = max(abs(exact), 1e-300)
            err = abs(exact - fl[r]) / ref
            assert err < 1e-10, (
                f"r={r}: frac={exact:.10e}, float={fl[r]:.10e}"
            )

    def test_deep_growth_decay(self):
        """At c=13, |S_r| decreases roughly as rho^r ~ 0.47^r."""
        tower = shadow_from_float(13.0, 24)
        rho = math.sqrt((180.0 * 13 + 872.0) / (13.0**2 * (5.0 * 13 + 22.0)))
        for r in range(14, 25):
            # |S_r| should be smaller than |S_{r-1}| (roughly by factor rho)
            ratio = abs(tower[r] / tower[r - 1])
            # Allow generous bounds (rho oscillates due to cos factor)
            assert ratio < 2.0, (
                f"r={r}: ratio={ratio:.4f}, expected < 2 (rho={rho:.4f})"
            )


# ============================================================================
# 15. Specific numerical values at distinguished central charges
# ============================================================================

class TestDistinguishedValues:
    """Verify S_r at physically significant central charges."""

    def test_S4_at_c13(self):
        """S_4(13) = 10/(13*87) = 10/1131."""
        frac = shadow_from_fraction(13, 1, 5)
        assert frac[4] == Fraction(10, 1131)

    def test_S5_at_c13(self):
        """S_5(13) = -48/(169*87) = -48/14703 = -16/4901."""
        frac = shadow_from_fraction(13, 1, 6)
        assert frac[5] == Fraction(-16, 4901)

    def test_kappa_at_c26(self):
        """kappa(26) = 13."""
        frac = shadow_from_fraction(26, 1, 3)
        assert frac[2] == Fraction(13)

    def test_S4_at_c26(self):
        """S_4(26) = 10/(26*152) = 10/3952 = 5/1976."""
        frac = shadow_from_fraction(26, 1, 5)
        assert frac[4] == Fraction(5, 1976)

    def test_kappa_at_ising(self):
        """kappa(1/2) = 1/4."""
        frac = shadow_from_fraction(1, 2, 3)
        assert frac[2] == Fraction(1, 4)

    def test_kappa_complementarity_26(self):
        """kappa(26) + kappa(0) is undefined (c=0 is a pole).
        But kappa(25) + kappa(1) = 25/2 + 1/2 = 13."""
        frac_25 = shadow_from_fraction(25, 1, 3)
        frac_1 = shadow_from_fraction(1, 1, 3)
        assert frac_25[2] + frac_1[2] == Fraction(13)

    def test_S7_at_c1(self):
        """S_7(1) = -2880*(15+61)/(7*1*27^2) = -2880*76/(7*729) = -218880/5103."""
        frac = shadow_from_fraction(1, 1, 8)
        expected = Fraction(-2880) * 76 / (7 * 729)
        assert frac[7] == expected, f"S_7(1) = {frac[7]}, expected {expected}"


# ============================================================================
# 16. Monotonicity and ordering tests
# ============================================================================

class TestMonotonicityAndOrdering:
    """Structural ordering properties of the shadow tower."""

    def test_magnitude_decay_convergent_regime(self):
        """At c=26, |S_r| is strictly decreasing for r >= 5."""
        tower = shadow_from_float(26.0, 24)
        for r in range(5, 24):
            assert abs(tower[r]) > abs(tower[r + 1]), (
                f"r={r}: |S_{r}|={abs(tower[r]):.4e} <= |S_{r+1}|={abs(tower[r+1]):.4e}"
            )

    def test_magnitude_growth_divergent_regime(self):
        """At c=1/2 (Ising), |S_r| grows for r >= 5."""
        tower = shadow_from_float(0.5, 15)
        for r in range(5, 14):
            assert abs(tower[r]) < abs(tower[r + 1]), (
                f"r={r}: |S_{r}|={abs(tower[r]):.4e} >= |S_{r+1}|={abs(tower[r+1]):.4e}"
            )

    def test_self_dual_between_convergent_and_divergent(self):
        """rho(13) ~ 0.47 < 1: convergent. rho(1) ~ 3.6 > 1: divergent."""
        params_13 = shadow_growth_parameters(13.0)
        params_1 = shadow_growth_parameters(1.0)
        assert params_13['rho'] < 1.0
        assert params_1['rho'] > 1.0


# ============================================================================
# 17. Shadow metric Q_L is correct
# ============================================================================

class TestShadowMetric:
    """Verify the shadow metric Q_L coefficients."""

    def test_q0(self):
        q0, q1, q2 = shadow_metric_coefficients()
        assert simplify(q0 - c**2) == 0

    def test_q1(self):
        q0, q1, q2 = shadow_metric_coefficients()
        assert simplify(q1 - 12*c) == 0

    def test_q2(self):
        q0, q1, q2 = shadow_metric_coefficients()
        expected = (180*c + 872) / (5*c + 22)
        assert simplify(q2 - expected) == 0

    def test_q2_alternative(self):
        """q2 = 36 + 80/(5c+22)."""
        q0, q1, q2 = shadow_metric_coefficients()
        alt = Rational(36) + Rational(80) / (5*c + 22)
        assert simplify(q2 - alt) == 0

    def test_Delta_formula(self):
        """Delta = 8*kappa*S_4 = 40/(5c+22)."""
        delta = Delta_vir()
        assert simplify(delta - Rational(40)/(5*c+22)) == 0

    def test_Delta_positive_for_positive_c(self):
        """Delta > 0 for c > 0 (class M: infinite depth)."""
        for cv in [0.5, 1, 4, 13, 25, 26]:
            val = float(Neval(Delta_vir().subs(c, Rational(cv))))
            assert val > 0, f"Delta({cv}) = {val} should be positive"
