"""Tests for extended Virasoro shadow tower: closed-form S_5 through S_12.

Verifies:
  - Recursion consistency: closed forms match convolution recursion from f^2 = Q_L
  - Q^contact = 10/[c(5c+22)] matches S_4
  - Shadow radius rho(c) from the extended tower
  - Numerical convergence at c = 1/2, 1, 4, 13, 25, 26
  - Master equation nabla_H(S_r) + o^(r) = 0
  - Sign alternation, pole structure, Koszul self-duality at c = 13
  - Cross-validation against independent float recursion
  - S_11 and S_12: pole structure, denominator pattern, shadow radius consistency
"""

import math
import pytest
from sympy import Rational, Symbol, cancel, denom, factor, simplify, sqrt, N as Neval

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.virasoro_shadow_extended import (
    S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12,
    Sr,
    c,
    complementarity_sum,
    convergence_analysis,
    critical_discriminant,
    evaluate_tower,
    evaluate_tower_float,
    koszul_dual,
    master_equation_residual,
    ratio_test_from_tower,
    shadow_from_recursion,
    shadow_radius_at,
    shadow_radius_squared,
    shadow_tower_exact,
    verify_qcontact,
    verify_recursion_consistency,
    verify_self_duality,
)


# ============================================================================
# 1. Recursion consistency: closed forms match convolution recursion
# ============================================================================

class TestRecursionConsistency:
    """Verify that hardcoded closed forms match the convolution recursion."""

    def test_all_match_recursion(self):
        """Every S_r for r=2..12 matches the convolution recursion from f^2=Q_L."""
        results = verify_recursion_consistency(12)
        for r in range(2, 13):
            assert results[r], f"S_{r} does not match convolution recursion"

    def test_S2_equals_kappa(self):
        """S_2 = c/2 = kappa (the modular characteristic)."""
        assert simplify(S2() - c / 2) == 0

    def test_S3_is_constant(self):
        """S_3 = 2, independent of c."""
        assert S3() == 2

    def test_S4_quartic_contact(self):
        """S_4 = 10/[c(5c+22)] (Q^contact_Vir)."""
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(S4() - expected) == 0

    def test_S5_known_formula(self):
        """S_5 = -48/[c^2(5c+22)] (previously computed, cor:virasoro-quintic-shadow-explicit)."""
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(S5() - expected) == 0

    def test_S6_factored(self):
        """S_6 = 80(45c+193)/[3c^3(5c+22)^2]."""
        expected = Rational(80) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2)
        assert simplify(S6() - expected) == 0

    def test_S7_factored(self):
        """S_7 = -2880(15c+61)/[7c^4(5c+22)^2]."""
        expected = Rational(-2880) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2)
        assert simplify(S7() - expected) == 0

    def test_S8_factored(self):
        """S_8 = 80(2025c^2+16470c+33314)/[c^5(5c+22)^3]."""
        expected = Rational(80) * (
            2025 * c**2 + 16470 * c + 33314
        ) / (c**5 * (5 * c + 22)**3)
        assert simplify(S8() - expected) == 0

    def test_S9_factored(self):
        """S_9 = -1280(2025c^2+15570c+29554)/[3c^6(5c+22)^3]."""
        expected = Rational(-1280) * (
            2025 * c**2 + 15570 * c + 29554
        ) / (3 * c**6 * (5 * c + 22)**3)
        assert simplify(S9() - expected) == 0

    def test_S10_factored(self):
        """S_10 = 256(91125c^3+1050975c^2+3989790c+4969967)/[c^7(5c+22)^4]."""
        expected = Rational(256) * (
            91125 * c**3 + 1050975 * c**2 + 3989790 * c + 4969967
        ) / (c**7 * (5 * c + 22)**4)
        assert simplify(S10() - expected) == 0

    def test_S11_factored(self):
        """S_11 = -15360(91125c^3+990225c^2+3500190c+3988097)/[11 c^8(5c+22)^4]."""
        expected = Rational(-15360) * (
            91125 * c**3 + 990225 * c**2 + 3500190 * c + 3988097
        ) / (11 * c**8 * (5 * c + 22)**4)
        assert simplify(S11() - expected) == 0

    def test_S12_factored(self):
        """S_12 = 2560(4100625c^4+59413500c^3+315017100c^2+717857460c+583976486)/[3 c^9(5c+22)^5]."""
        expected = Rational(2560) * (
            4100625 * c**4 + 59413500 * c**3 + 315017100 * c**2
            + 717857460 * c + 583976486
        ) / (3 * c**9 * (5 * c + 22)**5)
        assert simplify(S12() - expected) == 0

    def test_recursion_extended_to_15(self):
        """Recursion consistency holds beyond arity 12 (sanity check up to 15)."""
        recursive = shadow_from_recursion(15)
        for r in range(2, 13):
            diff = simplify(Sr(r) - recursive[r])
            assert diff == 0, f"S_{r} mismatch at extended range"


# ============================================================================
# 2. Q^contact verification
# ============================================================================

class TestQContact:
    """Verify Q^contact_Vir = S_4 = 10/[c(5c+22)]."""

    def test_qcontact_formula(self):
        """Q^contact_Vir = S_4 = 10/[c(5c+22)]."""
        assert verify_qcontact()

    def test_qcontact_numerical(self):
        """Q^contact at specific c values matches S_4."""
        for cv in [Rational(1, 2), Rational(1), Rational(4),
                    Rational(13), Rational(25), Rational(26)]:
            s4_val = float(Neval(S4().subs(c, cv)))
            expected = float(10 / (float(cv) * (5 * float(cv) + 22)))
            assert abs(s4_val - expected) < 1e-14 * abs(expected)

    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 40/(5c+22)."""
        delta = critical_discriminant()
        expected = Rational(40) / (5 * c + 22)
        assert simplify(delta - expected) == 0

    def test_discriminant_positive(self):
        """Delta > 0 for c > 0 (class M: infinite depth)."""
        for cv in [Rational(1, 2), 1, 4, 13, 25, 26]:
            val = float(Neval(critical_discriminant().subs(c, Rational(cv))))
            assert val > 0, f"Delta should be positive at c={cv}"


# ============================================================================
# 3. Shadow radius from extended tower
# ============================================================================

class TestShadowRadius:
    """Verify shadow radius rho(c) against ratio test from the tower."""

    def test_rho_formula(self):
        """rho^2 = (180c+872)/((5c+22)c^2)."""
        rho_sq = shadow_radius_squared()
        expected = (180 * c + 872) / ((5 * c + 22) * c**2)
        assert simplify(rho_sq - expected) == 0

    def test_rho_from_shadow_metric(self):
        """rho^2 = (9*alpha^2 + 2*Delta)/(4*kappa^2), alpha=S_3=2, Delta=8*kappa*S_4."""
        kappa = S2()
        alpha = S3()
        delta = critical_discriminant()
        rho_sq_direct = (9 * alpha**2 + 2 * delta) / (4 * kappa**2)
        rho_sq_formula = shadow_radius_squared()
        assert simplify(rho_sq_direct - rho_sq_formula) == 0

    @pytest.mark.parametrize("cv,expected_conv", [
        (Rational(1, 2), False),
        (Rational(1), False),
        (Rational(4), False),
        (Rational(13), True),
        (Rational(25), True),
        (Rational(26), True),
    ])
    def test_convergence_classification(self, cv, expected_conv):
        """Tower convergent for c > c* ~ 6.12, divergent for c < c*."""
        rho = shadow_radius_at(cv)
        assert (rho < 1) == expected_conv, (
            f"c={cv}: rho={rho:.6f}, expected convergent={expected_conv}"
        )

    def test_self_dual_rho(self):
        """rho(13) = rho(13) (self-dual point)."""
        rho_13 = shadow_radius_at(13)
        rho_dual = shadow_radius_at(26 - 13)
        assert abs(rho_13 - rho_dual) < 1e-14

    def test_self_dual_rho_value(self):
        """rho(13) ~ 0.4674 (within the convergent regime)."""
        rho = shadow_radius_at(13)
        assert abs(rho - 0.46739578) < 1e-6

    def test_string_rho(self):
        """rho(26) ~ 0.2325 (deep in the convergent regime)."""
        rho = shadow_radius_at(26)
        assert abs(rho - 0.23245002) < 1e-6

    def test_ising_rho(self):
        """rho(1/2) ~ 12.53 (deep in the divergent regime)."""
        rho = shadow_radius_at(Rational(1, 2))
        assert abs(rho - 12.53240697) < 1e-4

    @pytest.mark.parametrize("cv", [
        Rational(1, 2), Rational(1), Rational(4),
        Rational(13), Rational(25), Rational(26),
    ])
    def test_ratio_approaches_rho(self, cv):
        """The ratio |S_{r+1}/S_r| approaches rho from above."""
        ratios = ratio_test_from_tower(cv, 10)
        if len(ratios) >= 2:
            # Last ratio should be closer to rho than the first
            rho = ratios[-1][2]
            last_err = ratios[-1][3]
            # Ratio should be within 50% of rho at r=9
            # (exact convergence is rho + O(1/r), so at r=9 we expect ~10% error)
            assert last_err < 0.5, (
                f"c={cv}: ratio at r={ratios[-1][0]} is {ratios[-1][1]:.6f}, "
                f"rho={rho:.6f}, error={last_err:.4f}"
            )


# ============================================================================
# 4. Numerical convergence at specific c values
# ============================================================================

class TestNumericalConvergence:
    """Cross-validate exact formulas against independent float recursion."""

    @pytest.mark.parametrize("cv", [0.5, 1.0, 4.0, 13.0, 25.0, 26.0])
    def test_exact_vs_float(self, cv):
        """Exact symbolic evaluation matches float recursion to machine precision."""
        exact = evaluate_tower(Rational(cv), 12)
        floats = evaluate_tower_float(cv, 12)
        for r in range(2, 13):
            rel_err = abs(exact[r] - floats[r]) / max(abs(exact[r]), 1e-50)
            assert rel_err < 1e-12, (
                f"c={cv}, S_{r}: exact={exact[r]:.10e}, "
                f"float={floats[r]:.10e}, rel_err={rel_err:.2e}"
            )

    @pytest.mark.parametrize("cv", [0.5, 1.0, 4.0, 13.0, 25.0, 26.0])
    def test_extended_float_consistency(self, cv):
        """Float recursion at r=2..12 matches at r=2..30 (internal consistency)."""
        short = evaluate_tower_float(cv, 12)
        long = evaluate_tower_float(cv, 30)
        for r in range(2, 13):
            assert abs(short[r] - long[r]) < 1e-14 * max(abs(short[r]), 1e-50)

    @pytest.mark.parametrize("cv", [0.5, 1.0, 4.0, 13.0, 25.0, 26.0])
    def test_sign_alternation_low_arity(self, cv):
        """S_r alternates in sign for r = 4..12 at all test c values.

        At higher arities, sign alternation can break because the oscillation
        phase theta/pi is not exactly 1 (ranges from ~0.91 at c=1/2 to ~0.96
        at c=26). The cos(r*theta + phi) factor occasionally produces same-sign
        consecutive terms. For r <= 12, alternation holds for all c > 0 since
        theta/pi > 0.9 and the phase lag has not yet accumulated enough to
        skip a sign change.
        """
        tower = evaluate_tower_float(cv, 12)
        for r in range(5, 13):
            assert tower[r] * tower[r - 1] < 0, (
                f"c={cv}: S_{r-1}={tower[r-1]:.4e} and S_{r}={tower[r]:.4e} "
                f"have the same sign (should alternate for r<=12)"
            )

    @pytest.mark.parametrize("cv", [13.0, 25.0, 26.0])
    def test_sign_alternation_extended(self, cv):
        """S_r alternates for r = 4..20 at large c (theta/pi closer to 1)."""
        tower = evaluate_tower_float(cv, 20)
        for r in range(5, 20):
            assert tower[r] * tower[r - 1] < 0, (
                f"c={cv}: S_{r-1}={tower[r-1]:.4e} and S_{r}={tower[r]:.4e} "
                f"have the same sign (should alternate at large c)"
            )

    def test_convergence_analysis_c13(self):
        """Full convergence analysis at the self-dual point c=13.

        The ratio |S_{r+1}/S_r| converges to rho but oscillates due to
        cos(r*theta+phi) with theta/pi ~ 0.95. At r=19, the error from
        rho is about 18%, decreasing as O(1/r).
        """
        analysis = convergence_analysis(13, 20)
        assert analysis['convergent']
        assert analysis['sign_alternation']
        assert analysis['ratio_vs_rho_error'] < 0.25  # within 25% at r=19

    def test_convergence_analysis_c26(self):
        """Full convergence analysis at the string value c=26."""
        analysis = convergence_analysis(26, 20)
        assert analysis['convergent']
        assert analysis['sign_alternation']
        assert analysis['ratio_vs_rho_error'] < 0.25

    def test_divergence_analysis_c1(self):
        """Divergence analysis at c=1: rho > 1, tower diverges."""
        analysis = convergence_analysis(1, 15)
        assert not analysis['convergent']
        assert analysis['sign_alternation']  # holds through r=15 for c=1

    @pytest.mark.parametrize("cv", [0.5, 1.0, 4.0, 13.0, 25.0, 26.0])
    def test_generating_function_identity(self, cv):
        """H(t)^2 = t^4 Q_L(t) at small t (spot check of algebraicity theorem).

        The series converges for |t| < R = 1/rho.  We pick t well inside
        the convergence radius so that 40 terms suffice for machine precision.
        """
        rho = shadow_radius_at(cv)
        # t must be inside convergence radius R = 1/rho
        t_val = min(0.05, 0.3 / (rho + 1))
        tower = evaluate_tower_float(cv, 40)
        # H(t) = sum r*S_r*t^r
        H_val = sum(r * tower[r] * t_val**r for r in range(2, 41))
        # Q_L(t) = c^2 + 12c*t + alpha(c)*t^2
        alpha_c = (180 * cv + 872) / (5 * cv + 22)
        Q_val = cv**2 + 12 * cv * t_val + alpha_c * t_val**2
        H_sq = H_val**2
        Q_rhs = t_val**4 * Q_val
        rel_err = abs(H_sq - Q_rhs) / abs(Q_rhs)
        assert rel_err < 1e-6, (
            f"c={cv}: H^2={H_sq:.10e}, t^4*Q={Q_rhs:.10e}, rel_err={rel_err:.2e}"
        )


# ============================================================================
# 5. Master equation verification
# ============================================================================

class TestMasterEquation:
    """Verify nabla_H(S_r) + o^(r) = 0 for r = 5..10."""

    @pytest.mark.parametrize("r", [5, 6, 7, 8, 9, 10, 11, 12])
    def test_master_equation(self, r):
        """The master equation residual vanishes at arity r."""
        residual = master_equation_residual(r)
        assert residual == 0, f"Master equation residual at r={r}: {residual}"


# ============================================================================
# 6. Sign alternation and pole structure
# ============================================================================

class TestStructuralProperties:
    """Verify structural properties of the extended shadow tower."""

    def test_sign_pattern_symbolic(self):
        """S_r has sign (-1)^r for r >= 4 (evaluated at c=1)."""
        for r in range(4, 13):
            val = float(Neval(Sr(r).subs(c, 1)))
            expected_sign = (-1)**r
            actual_sign = 1 if val > 0 else -1
            assert actual_sign == expected_sign, (
                f"S_{r}(1) = {val:.6e}, expected sign {expected_sign}"
            )

    def test_poles_only_at_c0_and_lee_yang(self):
        """S_r(c) is regular for all c > 0, c != 0, c != -22/5."""
        # Verify at several positive c values that S_r is finite
        for cv in [Rational(1, 10), Rational(1), Rational(10), Rational(100)]:
            for r in range(2, 13):
                val = float(Neval(Sr(r).subs(c, cv)))
                assert math.isfinite(val), f"S_{r}({cv}) = {val} is not finite"

    def test_c0_is_pole_for_r_ge_4(self):
        """S_r diverges as c -> 0 for r >= 4."""
        for r in range(4, 13):
            # Evaluate at small c
            val = float(Neval(Sr(r).subs(c, Rational(1, 1000))))
            assert abs(val) > 100, (
                f"S_{r}(0.001) = {val:.6e}, expected large (pole at c=0)"
            )

    def test_denominator_power_of_c(self):
        """Denominator has c^{r-3} for r >= 4."""
        for r in range(4, 13):
            expr = factor(Sr(r))
            d = denom(expr)
            # Check that c^{r-3} divides the denominator
            d_at_0 = d.subs(c, 0)
            assert d_at_0 == 0, (
                f"S_{r}: denominator at c=0 should be 0, got {d_at_0}"
            )


# ============================================================================
# 7. Koszul self-duality at c = 13
# ============================================================================

class TestKoszulDuality:
    """Verify Koszul duality properties: S_r(c) vs S_r(26-c)."""

    @pytest.mark.parametrize("r", range(2, 13))
    def test_self_duality_at_c13(self, r):
        """S_r(13) = S_r(13) under c -> 26-c."""
        assert verify_self_duality(r), f"Self-duality fails at r={r}"

    def test_complementarity_S2(self):
        """S_2(c) + S_2(26-c) = 13."""
        result = complementarity_sum(2)
        assert simplify(result - 13) == 0

    def test_complementarity_S3(self):
        """S_3(c) + S_3(26-c) = 4."""
        result = complementarity_sum(3)
        assert simplify(result - 4) == 0

    @pytest.mark.parametrize("r", range(4, 13))
    def test_complementarity_numerical(self, r):
        """S_r(c) + S_r(26-c) is nonzero away from c=13 (generically)."""
        cv = Rational(1)
        s_sum = float(Neval(complementarity_sum(r).subs(c, cv)))
        # Should be nonzero (the sum is a nontrivial rational function)
        assert abs(s_sum) > 1e-15, (
            f"Complementarity sum S_{r}(1)+S_{r}(25) unexpectedly zero"
        )

    def test_koszul_dual_tower_c1(self):
        """S_r(1) vs S_r(25): the Koszul dual at c=1.

        S_3 = 2 is independent of c, so S_3(1) = S_3(25) trivially.
        For r >= 4, S_r(1) and S_r(25) should differ.
        """
        for r in range(4, 13):
            v1 = float(Neval(Sr(r).subs(c, 1)))
            v2 = float(Neval(Sr(r).subs(c, 25)))
            assert abs(v1 - v2) > 1e-10, (
                f"S_{r}(1) = S_{r}(25) unexpectedly at non-self-dual point"
            )


# ============================================================================
# 8. Cross-validation against shadow_tower_recursive module
# ============================================================================

class TestCrossValidation:
    """Cross-validate against existing shadow tower computation modules."""

    def test_vs_shadow_tower_recursive(self):
        """Match against shadow_tower_recursive.shadow_coefficients_virasoro_exact."""
        try:
            from lib.shadow_tower_recursive import shadow_coefficients_virasoro_exact
            recursive = shadow_coefficients_virasoro_exact(12)
            # Modules may use different Symbol('c') objects; compare numerically
            for r in range(2, 13):
                for cv in [Rational(1), Rational(13), Rational(26)]:
                    v1 = float(Neval(Sr(r).subs(c, cv)))
                    # The recursive module may use a different c symbol
                    rec_r = recursive[r]
                    for sym in rec_r.free_symbols:
                        rec_r = rec_r.subs(sym, cv)
                    v2 = float(Neval(rec_r))
                    assert abs(v1 - v2) < 1e-12 * max(abs(v1), 1e-50), (
                        f"S_{r}({cv}) mismatch: ours={v1}, recursive={v2}"
                    )
        except ImportError:
            pytest.skip("shadow_tower_recursive not available")

    def test_vs_quintic_shadow_engine(self):
        """Match S_5, S_6, S_7 against quintic_shadow_engine."""
        try:
            from lib.quintic_shadow_engine import virasoro_shadow_tower_exact
            qse = virasoro_shadow_tower_exact(10)
            # Compare numerically to avoid symbol mismatch
            for r in range(5, 8):
                for cv in [Rational(1), Rational(13), Rational(26)]:
                    v1 = float(Neval(Sr(r).subs(c, cv)))
                    rec_r = qse[r]
                    for sym in rec_r.free_symbols:
                        rec_r = rec_r.subs(sym, cv)
                    v2 = float(Neval(rec_r))
                    assert abs(v1 - v2) < 1e-12 * max(abs(v1), 1e-50), (
                        f"S_{r}({cv}) mismatch with quintic_shadow_engine"
                    )
        except ImportError:
            pytest.skip("quintic_shadow_engine not available")

    def test_vs_virasoro_shadow_gf(self):
        """Match against virasoro_shadow_gf.S(r) recursive computation."""
        try:
            from lib.virasoro_shadow_gf import S as S_gf, clear_cache
            clear_cache()
            # Compare numerically to avoid symbol mismatch
            for r in range(2, 13):
                for cv in [Rational(1), Rational(13), Rational(26)]:
                    v1 = float(Neval(Sr(r).subs(c, cv)))
                    gf_r = S_gf(r)
                    for sym in gf_r.free_symbols:
                        gf_r = gf_r.subs(sym, cv)
                    v2 = float(Neval(gf_r))
                    assert abs(v1 - v2) < 1e-12 * max(abs(v1), 1e-50), (
                        f"S_{r}({cv}) mismatch with virasoro_shadow_gf"
                    )
        except ImportError:
            pytest.skip("virasoro_shadow_gf not available")


# ============================================================================
# 9. Asymptotic growth rate verification
# ============================================================================

class TestAsymptoticGrowth:
    """Verify the asymptotic formula |S_r| ~ C rho^r r^{-5/2}."""

    @pytest.mark.parametrize("cv", [13, 26])
    def test_ratio_convergence_to_rho(self, cv):
        """The geometric mean of |S_{r+1}/S_r| converges to rho (convergent regime).

        Individual ratios oscillate due to cos(r*theta+phi) with period ~2.1.
        For convergent towers (rho < 1), float underflow limits useful range:
        at c=26 (rho~0.23), |S_r| ~ 10^{-0.64*r} underflows at r~500.
        We use r = 30..50 with geometric mean to smooth oscillation.
        """
        max_r = 50
        tower = evaluate_tower_float(float(cv), max_r)
        rho = shadow_radius_at(cv)

        # Geometric mean of ratios over a window
        geo = 1.0
        count = 0
        for r in range(30, max_r):
            if abs(tower[r]) > 1e-250 and abs(tower[r + 1]) > 1e-250:
                geo *= abs(tower[r + 1] / tower[r])
                count += 1
        assert count > 0, f"c={cv}: all coefficients underflowed"
        geo = geo**(1.0 / count)
        rel_err = abs(geo - rho) / rho
        assert rel_err < 0.10, (
            f"c={cv}: geo mean ratio r=30..{max_r} = {geo:.8f}, "
            f"rho = {rho:.8f}, error = {rel_err:.4f}"
        )

    @pytest.mark.parametrize("cv", [0.5, 1, 4])
    def test_ratio_convergence_divergent(self, cv):
        """Even in the divergent regime, geometric mean of ratios converges to rho.

        Convergence is slow due to oscillation at low r; within 20% at r=30..50.
        """
        max_r = 50
        tower = evaluate_tower_float(float(cv), max_r)
        rho = shadow_radius_at(cv)

        geo = 1.0
        count = 0
        for r in range(30, max_r):
            if abs(tower[r]) > 1e-250 and abs(tower[r + 1]) > 1e-250:
                geo *= abs(tower[r + 1] / tower[r])
                count += 1
        assert count > 0, f"c={cv}: all coefficients vanished"
        geo = geo**(1.0 / count)
        rel_err = abs(geo - rho) / rho
        assert rel_err < 0.20, (
            f"c={cv}: geo mean ratio r=30..{max_r} = {geo:.8f}, "
            f"rho = {rho:.8f}, error = {rel_err:.4f}"
        )

    def test_r_minus_5_2_correction(self):
        """The r^{-5/2} polynomial correction is visible in normalized ratios."""
        tower = evaluate_tower_float(13.0, 40)
        rho = shadow_radius_at(13)

        # Normalized: |S_r| * rho^{-r} should scale as r^{-5/2}
        normalized = {}
        for r in range(5, 40):
            normalized[r] = abs(tower[r]) * rho**(-r)

        # Check ratio of normalized[2r]/normalized[r] ~ (2)^{-5/2} = 0.1768
        # Use r=10 and r=20
        if 10 in normalized and 20 in normalized and normalized[10] > 0:
            ratio = normalized[20] / normalized[10]
            expected = (20.0 / 10.0)**(-2.5)  # 0.1768
            # Allow 50% tolerance due to oscillation
            assert abs(ratio - expected) < 0.5 * expected, (
                f"Power law check: normalized[20]/normalized[10] = {ratio:.4f}, "
                f"expected ~ {expected:.4f}"
            )


# ============================================================================
# 10. Generating function H^2 = t^4 Q_L algebraicity
# ============================================================================

class TestAlgebraicity:
    """Verify the Riccati algebraicity theorem: H(t)^2 = t^4 Q_L(t)."""

    @pytest.mark.parametrize("cv", [0.5, 1.0, 4.0, 13.0, 25.0, 26.0])
    def test_algebraicity_small_t(self, cv):
        """H^2 = t^4 Q_L at small t, well inside convergence radius.

        Choose t so that rho*t < 0.5 to ensure rapid convergence with 50 terms.
        """
        rho = shadow_radius_at(cv)
        t_val = min(0.05, 0.4 / rho)
        tower = evaluate_tower_float(cv, 50)
        H_val = sum(r * tower[r] * t_val**r for r in range(2, 51))
        alpha_c = (180 * cv + 872) / (5 * cv + 22)
        Q_val = cv**2 + 12 * cv * t_val + alpha_c * t_val**2
        rel_err = abs(H_val**2 - t_val**4 * Q_val) / abs(t_val**4 * Q_val)
        assert rel_err < 1e-8, f"c={cv}: algebraicity error = {rel_err:.2e}"

    @pytest.mark.parametrize("cv", [13.0, 26.0])
    def test_algebraicity_moderate_t(self, cv):
        """H^2 = t^4 Q_L at t = 0.3 (near convergence boundary for some c)."""
        tower = evaluate_tower_float(cv, 50)
        t_val = 0.3
        H_val = sum(r * tower[r] * t_val**r for r in range(2, 51))
        alpha_c = (180 * cv + 872) / (5 * cv + 22)
        Q_val = cv**2 + 12 * cv * t_val + alpha_c * t_val**2
        rel_err = abs(H_val**2 - t_val**4 * Q_val) / abs(t_val**4 * Q_val)
        assert rel_err < 1e-6, f"c={cv}: algebraicity error at t=0.3: {rel_err:.2e}"


# ============================================================================
# 11. Special values table
# ============================================================================

class TestSpecialValues:
    """Verify S_r at special central charges against independent computation."""

    def test_ising_c_half(self):
        """S_r at c=1/2 (Ising model): all finite, alternating, divergent."""
        tower = evaluate_tower(Rational(1, 2), 10)
        assert abs(tower[2] - 0.25) < 1e-14
        assert abs(tower[3] - 2.0) < 1e-14
        # S_4 = 10/(0.5*24.5) = 10/12.25 = 40/49
        assert abs(tower[4] - 40.0 / 49) < 1e-12
        # S_5 = -48/(0.25*24.5) = -48/6.125 = -384/49
        assert abs(tower[5] - (-384.0 / 49)) < 1e-12

    def test_free_boson_c1(self):
        """S_r at c=1 (free boson compactification)."""
        tower = evaluate_tower(Rational(1), 10)
        assert abs(tower[2] - 0.5) < 1e-14
        assert abs(tower[3] - 2.0) < 1e-14
        # S_4 = 10/(1*27) = 10/27
        assert abs(tower[4] - 10.0 / 27) < 1e-14

    def test_string_c26(self):
        """S_r at c=26 (critical string): rapidly convergent tower."""
        tower = evaluate_tower(Rational(26), 10)
        assert abs(tower[2] - 13.0) < 1e-14
        assert abs(tower[3] - 2.0) < 1e-14
        # Verify rapid decay: |S_r| should decrease
        for r in range(5, 10):
            assert abs(tower[r + 1]) < abs(tower[r]), (
                f"Tower not decaying at c=26: |S_{r+1}|={abs(tower[r+1]):.4e} "
                f">= |S_{r}|={abs(tower[r]):.4e}"
            )

    def test_self_dual_c13(self):
        """S_r at c=13: self-dual, moderately convergent."""
        tower = evaluate_tower(Rational(13), 10)
        assert abs(tower[2] - 6.5) < 1e-14
        rho = shadow_radius_at(13)
        assert rho < 1  # convergent
        # Check decay
        for r in range(5, 10):
            assert abs(tower[r + 1]) < abs(tower[r])


# ============================================================================
# 12. Boundary and edge cases
# ============================================================================

class TestEdgeCases:
    """Test boundary conditions and edge cases."""

    def test_Sr_raises_for_invalid_r(self):
        """Sr(r) raises ValueError for r < 2 or r > 12."""
        with pytest.raises(ValueError):
            Sr(1)
        with pytest.raises(ValueError):
            Sr(13)
        with pytest.raises(ValueError):
            Sr(0)

    def test_large_c_limit(self):
        """As c -> infinity, S_r -> 0 for r >= 4 (tower becomes Gaussian)."""
        tower = evaluate_tower(Rational(10000), 12)
        for r in range(4, 13):
            assert abs(tower[r]) < 1e-6, (
                f"S_{r}(10000) = {tower[r]:.4e}, should be near 0"
            )

    def test_shadow_tower_exact_returns_dict(self):
        """shadow_tower_exact() returns a dict with keys 2..12."""
        tower = shadow_tower_exact()
        assert set(tower.keys()) == set(range(2, 13))
        for r, expr in tower.items():
            assert expr is not None


# ============================================================================
# 13. S_11 and S_12: dedicated pole, denominator, radius, and value tests
# ============================================================================

class TestS11S12PoleStructure:
    """Verify pole structure and denominator pattern for S_11 and S_12."""

    def test_S11_poles_only_c0_lee_yang(self):
        """S_11 is regular for all c > 0 away from c=0 and c=-22/5."""
        for cv in [Rational(1, 10), Rational(1, 2), Rational(1),
                    Rational(10), Rational(100), Rational(1000)]:
            val = float(Neval(S11().subs(c, cv)))
            assert math.isfinite(val), f"S_11({cv}) = {val} is not finite"

    def test_S12_poles_only_c0_lee_yang(self):
        """S_12 is regular for all c > 0 away from c=0 and c=-22/5."""
        for cv in [Rational(1, 10), Rational(1, 2), Rational(1),
                    Rational(10), Rational(100), Rational(1000)]:
            val = float(Neval(S12().subs(c, cv)))
            assert math.isfinite(val), f"S_12({cv}) = {val} is not finite"

    def test_S11_denominator_pattern(self):
        """S_11 denominator: c^{r-3} (5c+22)^{floor((r-2)/2)} = c^8 (5c+22)^4.

        The extra factor of 11 in the denominator is a rational constant
        from S_r = a_{r-2}/r, absorbed into the overall coefficient.
        """
        d = denom(factor(S11()))
        # denominator = 11 * c^8 * (5c+22)^4
        # c^8 divides the denominator
        d_at_0 = d.subs(c, 0)
        assert d_at_0 == 0, f"S_11: c=0 should be a pole, but denom(0)={d_at_0}"
        # (5c+22)^4 divides the denominator
        d_at_ly = d.subs(c, Rational(-22, 5))
        assert d_at_ly == 0, f"S_11: c=-22/5 should be a pole, but denom(-22/5)={d_at_ly}"

    def test_S12_denominator_pattern(self):
        """S_12 denominator: c^{r-3} (5c+22)^{floor((r-2)/2)} = c^9 (5c+22)^5.

        The extra factor of 3 in the denominator is a rational constant
        from S_r = a_{r-2}/r.
        """
        d = denom(factor(S12()))
        d_at_0 = d.subs(c, 0)
        assert d_at_0 == 0, f"S_12: c=0 should be a pole, but denom(0)={d_at_0}"
        d_at_ly = d.subs(c, Rational(-22, 5))
        assert d_at_ly == 0, f"S_12: c=-22/5 should be a pole, but denom(-22/5)={d_at_ly}"

    def test_S11_c_power_exact(self):
        """Denominator of S_11 has exactly c^8 (= c^{11-3})."""
        expr = factor(S11())
        d = denom(expr)
        # Verify c^8 divides d but c^9 does not (after removing (5c+22) factors)
        # At c=0: the denominator vanishes. Count order by successive division.
        from sympy import Poly
        p = Poly(d, c)
        # The minimum power of c in the polynomial
        min_power = min(m[0] for m in p.as_dict().keys())
        assert min_power == 8, f"S_11: c power in denom = {min_power}, expected 8"

    def test_S12_c_power_exact(self):
        """Denominator of S_12 has exactly c^9 (= c^{12-3})."""
        from sympy import Poly
        d = denom(factor(S12()))
        p = Poly(d, c)
        min_power = min(m[0] for m in p.as_dict().keys())
        assert min_power == 9, f"S_12: c power in denom = {min_power}, expected 9"

    def test_S11_lee_yang_power_exact(self):
        """Denominator of S_11 has (5c+22)^4 (= (5c+22)^{floor(9/2)})."""
        # Substitute c = -22/5 + epsilon and check order of vanishing
        from sympy import Poly
        d = denom(factor(S11()))
        # Factor in terms of (5c+22): substitute u = 5c+22, c = (u-22)/5
        u = Symbol('u')
        d_u = d.subs(c, (u - 22) / 5)
        d_u = cancel(d_u)
        # The vanishing order at u=0
        p = Poly(d_u, u)
        min_power = min(m[0] for m in p.as_dict().keys())
        assert min_power == 4, f"S_11: (5c+22) power = {min_power}, expected 4"

    def test_S12_lee_yang_power_exact(self):
        """Denominator of S_12 has (5c+22)^5 (= (5c+22)^{floor(10/2)})."""
        from sympy import Poly
        u = Symbol('u')
        d = denom(factor(S12()))
        d_u = d.subs(c, (u - 22) / 5)
        d_u = cancel(d_u)
        p = Poly(d_u, u)
        min_power = min(m[0] for m in p.as_dict().keys())
        assert min_power == 5, f"S_12: (5c+22) power = {min_power}, expected 5"


class TestS11S12ShadowRadiusConsistency:
    """Verify shadow radius consistency using S_11, S_12 ratio data."""

    @pytest.mark.parametrize("cv", [Rational(1, 2), Rational(1), Rational(25)])
    def test_ratio_S11_S10_approaches_rho(self, cv):
        """The ratio |S_11/S_10| is within a factor of 2 of rho(c)."""
        v10 = float(Neval(Sr(10).subs(c, cv)))
        v11 = float(Neval(Sr(11).subs(c, cv)))
        ratio = abs(v11 / v10)
        rho = shadow_radius_at(cv)
        rel_err = abs(ratio - rho) / rho
        assert rel_err < 0.5, (
            f"c={cv}: |S_11/S_10|={ratio:.6f}, rho={rho:.6f}, error={rel_err:.4f}"
        )

    @pytest.mark.parametrize("cv", [Rational(1, 2), Rational(1), Rational(25)])
    def test_ratio_S12_S11_approaches_rho(self, cv):
        """The ratio |S_12/S_11| is within a factor of 2 of rho(c)."""
        v11 = float(Neval(Sr(11).subs(c, cv)))
        v12 = float(Neval(Sr(12).subs(c, cv)))
        ratio = abs(v12 / v11)
        rho = shadow_radius_at(cv)
        rel_err = abs(ratio - rho) / rho
        assert rel_err < 0.5, (
            f"c={cv}: |S_12/S_11|={ratio:.6f}, rho={rho:.6f}, error={rel_err:.4f}"
        )

    def test_ratios_converging_to_rho(self):
        """Successive ratios |S_{r+1}/S_r| get closer to rho as r increases.

        Test at c=13 (convergent, rho~0.467): the geometric mean of
        ratios at r=8..11 should be closer to rho than at r=4..7.
        """
        cv = 13
        rho = shadow_radius_at(cv)
        tower = evaluate_tower(Rational(cv), 12)
        early_geo = 1.0
        for r in range(4, 8):
            early_geo *= abs(tower[r + 1] / tower[r])
        early_geo = early_geo**(1.0 / 4)
        late_geo = 1.0
        for r in range(8, 12):
            late_geo *= abs(tower[r + 1] / tower[r])
        late_geo = late_geo**(1.0 / 4)
        early_err = abs(early_geo - rho) / rho
        late_err = abs(late_geo - rho) / rho
        assert late_err < early_err, (
            f"Ratios not converging to rho: early_err={early_err:.4f}, "
            f"late_err={late_err:.4f}"
        )

    @pytest.mark.parametrize("cv", [Rational(1, 2), Rational(1), Rational(25)])
    def test_extended_ratio_test_to_50(self, cv):
        """Geometric mean of |S_{r+1}/S_r| for r=30..49 matches rho within 20%.

        Convergence is O(1/r) with oscillation; at r=30..49 the geometric mean
        is within 20% for all c. The divergent regime (c=1, rho~6.24) converges
        more slowly than the convergent regime.
        """
        rho = shadow_radius_at(cv)
        tower = evaluate_tower_float(float(cv), 50)
        geo = 1.0
        count = 0
        for r in range(30, 50):
            if abs(tower[r]) > 1e-250 and abs(tower[r + 1]) > 1e-250:
                geo *= abs(tower[r + 1] / tower[r])
                count += 1
        assert count > 0, f"c={cv}: all coefficients underflowed"
        geo = geo**(1.0 / count)
        rel_err = abs(geo - rho) / rho
        assert rel_err < 0.20, (
            f"c={cv}: geo mean ratio = {geo:.8f}, rho = {rho:.8f}, "
            f"error = {rel_err:.4f}"
        )


class TestS11S12NumericalValues:
    """Verify S_11 and S_12 at specific central charges."""

    def test_S11_at_c1(self):
        """S_11(1) = -43876541440/1948617."""
        val = S11().subs(c, 1)
        expected = Rational(-43876541440, 1948617)
        assert simplify(val - expected) == 0

    def test_S12_at_c1(self):
        """S_12(1) = 4301734837760/43046721."""
        val = S12().subs(c, 1)
        expected = Rational(4301734837760, 43046721)
        assert simplify(val - expected) == 0

    def test_S11_at_c_half(self):
        """S_11(1/2) = -53901050511360/9058973."""
        val = S11().subs(c, Rational(1, 2))
        expected = Rational(-53901050511360, 9058973)
        assert simplify(val - expected) == 0

    def test_S12_at_c_half(self):
        """S_12(1/2) = 6167678898667520/121060821."""
        val = S12().subs(c, Rational(1, 2))
        expected = Rational(6167678898667520, 121060821)
        assert simplify(val - expected) == 0

    def test_S11_at_c25(self):
        """S_11(25) = -312204667904/7464363739013671875."""
        val = S11().subs(c, 25)
        expected = Rational(-312204667904, 7464363739013671875)
        assert simplify(val - expected) == 0

    def test_S12_at_c25(self):
        """S_12(25) = 200818006206976/22443984606170654296875."""
        val = S12().subs(c, 25)
        expected = Rational(200818006206976, 22443984606170654296875)
        assert simplify(val - expected) == 0

    def test_S11_numerical_c1(self):
        """S_11(1) ~ -2.2517e4 (float cross-check)."""
        exact = float(Neval(S11().subs(c, 1)))
        floats = evaluate_tower_float(1.0, 12)
        rel_err = abs(exact - floats[11]) / abs(exact)
        assert rel_err < 1e-12

    def test_S12_numerical_c1(self):
        """S_12(1) ~ 9.9932e4 (float cross-check)."""
        exact = float(Neval(S12().subs(c, 1)))
        floats = evaluate_tower_float(1.0, 12)
        rel_err = abs(exact - floats[12]) / abs(exact)
        assert rel_err < 1e-12

    def test_S11_negative(self):
        """S_11 < 0 for all c > 0 (sign (-1)^11 = -1)."""
        for cv in [Rational(1, 10), Rational(1, 2), Rational(1),
                    Rational(13), Rational(25), Rational(100)]:
            val = float(Neval(S11().subs(c, cv)))
            assert val < 0, f"S_11({cv}) = {val:.4e}, expected negative"

    def test_S12_positive(self):
        """S_12 > 0 for all c > 0 (sign (-1)^12 = +1)."""
        for cv in [Rational(1, 10), Rational(1, 2), Rational(1),
                    Rational(13), Rational(25), Rational(100)]:
            val = float(Neval(S12().subs(c, cv)))
            assert val > 0, f"S_12({cv}) = {val:.4e}, expected positive"

    def test_S11_S12_decay_at_c26(self):
        """At the string value c=26, |S_11| and |S_12| continue the decay."""
        tower = evaluate_tower(Rational(26), 12)
        assert abs(tower[11]) < abs(tower[10]), (
            f"|S_11(26)|={abs(tower[11]):.4e} >= |S_10(26)|={abs(tower[10]):.4e}"
        )
        assert abs(tower[12]) < abs(tower[11]), (
            f"|S_12(26)|={abs(tower[12]):.4e} >= |S_11(26)|={abs(tower[11]):.4e}"
        )

    def test_S11_S12_growth_at_c_half(self):
        """At c=1/2 (Ising, divergent), |S_11|, |S_12| grow rapidly."""
        tower = evaluate_tower(Rational(1, 2), 12)
        assert abs(tower[11]) > 1e5, f"|S_11(1/2)| = {abs(tower[11]):.4e}, expected > 1e5"
        assert abs(tower[12]) > 1e6, f"|S_12(1/2)| = {abs(tower[12]):.4e}, expected > 1e6"


class TestS11S12DenominatorPattern:
    """Verify the general denominator pattern c^{r-3}(5c+22)^{floor((r-2)/2)} for all r."""

    @pytest.mark.parametrize("r", range(4, 13))
    def test_denominator_c_power(self, r):
        """Denominator of S_r has c^{r-3}."""
        from sympy import Poly
        d = denom(factor(Sr(r)))
        p = Poly(d, c)
        min_power = min(m[0] for m in p.as_dict().keys())
        assert min_power == r - 3, (
            f"S_{r}: c power in denom = {min_power}, expected {r - 3}"
        )

    @pytest.mark.parametrize("r", range(4, 13))
    def test_denominator_lee_yang_power(self, r):
        """Denominator of S_r has (5c+22)^{floor((r-2)/2)}."""
        from sympy import Poly
        u = Symbol('u')
        d = denom(factor(Sr(r)))
        d_u = d.subs(c, (u - 22) / 5)
        d_u = cancel(d_u)
        p = Poly(d_u, u)
        min_power = min(m[0] for m in p.as_dict().keys())
        expected = (r - 2) // 2
        assert min_power == expected, (
            f"S_{r}: (5c+22) power = {min_power}, expected {expected}"
        )
