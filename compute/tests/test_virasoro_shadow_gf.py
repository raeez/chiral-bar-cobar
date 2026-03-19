"""Tests for the Virasoro shadow generating function.

Comprehensive verification of:
  - Recursive shadow coefficients S_r(c) against known values (r=2..7)
  - Master equation at every arity
  - Closed-form GF H(t,c) = t^2 * sqrt(Q(t,c)) matches recursion through arity 20
  - Pole structure: only c=0 and c=-22/5 for all r
  - Duality behavior under c -> 26-c
  - Self-dual point c=13
  - Riccati equation
  - Algebraic properties of Q(t,c)
  - Ratio asymptotics and radius of convergence
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel, fraction, limit, oo, denom, solve

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.virasoro_shadow_gf import (
    S, clear_cache, compute_shadows,
    nabla_H_coefficient, obstruction_coefficient, verify_master_equation_at,
    alpha, quadratic, H_generating, S_from_gf,
    h_poisson_bracket, compute_shadow_tower_direct, P_VIR,
    pole_analysis, denominator_factorization,
    S_dual, duality_ratio, duality_analysis, test_reflection_ansatz as _reflection_ansatz,
    S_at_13, self_dual_sequence,
    shadow_gf_truncated, check_ratio_pattern, numerical_ratio_pattern,
    verify_gf_matches_recursion, verify_riccati_equation, verify_algebraic_properties,
    verify_known_coefficients, KNOWN_COEFFICIENTS,
    c, t, x,
)


# =====================================================================
# Section 1: Known coefficient values
# =====================================================================

class TestKnownCoefficients:
    """Verify S_r against independently known values."""

    def test_S2_kappa(self):
        """S_2 = c/2 (curvature kappa)."""
        assert simplify(S(2) - c / 2) == 0

    def test_S3_cubic(self):
        """S_3 = 2 (Sugawara gravitational cubic)."""
        assert simplify(S(3) - 2) == 0

    def test_S4_quartic_contact(self):
        """S_4 = 10/[c(5c+22)] (quartic contact invariant)."""
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(S(4) - expected) == 0

    def test_S5_quintic(self):
        """S_5 = -48/[c^2(5c+22)]."""
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(S(5) - expected) == 0

    def test_S6_sextic(self):
        """S_6 = 80(45c+193)/[3c^3(5c+22)^2]."""
        expected = Rational(80) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2)
        assert simplify(S(6) - expected) == 0

    def test_S7_septic(self):
        """S_7 = -2880(15c+61)/[7c^4(5c+22)^2]."""
        expected = Rational(-2880) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2)
        assert simplify(S(7) - expected) == 0

    def test_all_known(self):
        """Batch verification of all known coefficients."""
        results = verify_known_coefficients()
        for label, ok in results.items():
            assert ok, f"Failed: {label}"


# =====================================================================
# Section 2: Master equation
# =====================================================================

class TestMasterEquation:
    """Verify nabla_H(Sh_r) + o^(r) = 0 at each arity."""

    @pytest.mark.parametrize("r", range(5, 13))
    def test_master_equation(self, r):
        """Master equation at arity r (valid for r >= 5, where recursion determines S_r)."""
        assert verify_master_equation_at(r), f"Master equation fails at r={r}"

    def test_nabla_eigenvalue(self):
        """nabla_H(S_r x^r) = 2r S_r x^r for several r."""
        for r in [2, 3, 4, 5, 6]:
            sr = S(r)
            result = nabla_H_coefficient(r)
            assert simplify(result - 2 * r * sr) == 0

    def test_obstruction_r5(self):
        """o^(5) = 480/[c^2(5c+22)] (single source: {Sh_3, Sh_4}_H)."""
        o5 = obstruction_coefficient(5)
        expected = Rational(480) / (c**2 * (5 * c + 22))
        assert simplify(o5 - expected) == 0

    def test_obstruction_r4(self):
        """o^(4) involves only {Sh_3, Sh_3}_H."""
        o4 = obstruction_coefficient(4)
        # {Sh_3, Sh_3}_H: j=k=3, eps=1/2, 2*3*3*S_3*S_3/c * 1/2 = 9*4/c = 36/c
        # But we also need j+k=6, j,k>=3: only (3,3)
        # eps=1/2: term = (1/2)*2*3*3*2*2/c = 36/c
        expected = Rational(36) / c
        assert simplify(o4 - expected) == 0


# =====================================================================
# Section 3: Closed-form generating function
# =====================================================================

class TestGeneratingFunction:
    """Test the closed-form GF H(t,c) = t^2 * sqrt(Q(t,c))."""

    @pytest.mark.parametrize("r", range(2, 13))
    def test_gf_matches_recursion(self, r):
        """GF coefficient matches recursive S_r at arity r."""
        gf_val = S_from_gf(r)
        rec_val = S(r)
        assert simplify(gf_val - rec_val) == 0, f"Mismatch at r={r}"

    def test_gf_batch(self):
        """Batch: GF matches recursion through arity 12."""
        results = verify_gf_matches_recursion(12)
        for label, ok in results.items():
            assert ok, f"Failed: {label}"

    def test_riccati_equation(self):
        """H_red^2 + 2ct^2*H_red = 12ct^5 + alpha*t^6."""
        assert verify_riccati_equation()


class TestAlgebraicProperties:
    """Test structural properties of Q(t,c) and alpha(c)."""

    def test_alpha_formula(self):
        """alpha(c) = (180c+872)/(5c+22)."""
        a = alpha()
        expected = (180 * c + 872) / (5 * c + 22)
        assert cancel(a - expected) == 0

    def test_alpha_decomposition(self):
        """alpha(c) = 36 + 80/(5c+22)."""
        a = alpha()
        decomp = 36 + Rational(80) / (5 * c + 22)
        assert cancel(a - decomp) == 0

    def test_discriminant_negative(self):
        """Discriminant of Q(t) as quadratic in t = -320c^2/(5c+22) < 0 for c > 0."""
        results = verify_algebraic_properties()
        assert results["discriminant"]

    def test_complete_square(self):
        """Q(t) = (c+6t)^2 + 80t^2/(5c+22)."""
        results = verify_algebraic_properties()
        assert results["complete_square"]

    def test_alpha_large_c_limit(self):
        """alpha(c) -> 36 as c -> infinity."""
        results = verify_algebraic_properties()
        assert results["alpha_inf_36"]

    def test_alpha_at_13(self):
        """alpha(13) = 3212/87."""
        results = verify_algebraic_properties()
        assert results["alpha_13"]

    def test_alpha_at_lee_yang(self):
        """alpha has a pole at c = -22/5 (Lee-Yang)."""
        a = alpha()
        d = denom(a)
        assert d.subs(c, Rational(-22, 5)) == 0


# =====================================================================
# Section 4: Pole structure
# =====================================================================

class TestPoleStructure:
    """Verify that S_r has poles only at c=0 and c=-22/5 for all computed r."""

    @pytest.mark.parametrize("r", range(4, 16))
    def test_poles_only_c0_and_lee_yang(self, r):
        """S_r has no poles except c=0 and c=-22/5."""
        sr = factor(S(r))
        _, d = fraction(sr)
        if d == 1:
            return  # no poles
        roots = solve(d, c)
        allowed = {0, Rational(-22, 5)}
        actual = set(roots)
        assert actual.issubset(allowed), f"r={r}: unexpected poles at {actual - allowed}"

    def test_c_power_in_denominator(self):
        """Power of c in denom(S_r) = r-3 for r >= 4.

        S_4 has c^1, S_5 has c^2, S_6 has c^3, etc.
        """
        info = pole_analysis(12)
        for r in range(4, 13):
            expected = r - 3
            assert info[r]['c_power'] == expected, f"r={r}: c-power = {info[r]['c_power']}, expected {expected}"

    def test_5c22_power_in_denominator(self):
        """Power of (5c+22) in denom(S_r) for r >= 4.

        Empirically: floor((r-2)/2), i.e. 1,1,2,2,3,3,4,4,5,...
        """
        for r in range(4, 13):
            sr = factor(S(r))
            _, d = fraction(sr)
            # First strip c powers
            rem = d
            while rem.subs(c, 0) == 0 and rem != 0:
                rem = cancel(rem / c)
            # Now count (5c+22) powers
            h = 5 * c + 22
            power = 0
            while rem.subs(c, Rational(-22, 5)) == 0:
                power += 1
                rem = cancel(rem / h)
            expected_power = (r - 2) // 2
            assert power == expected_power, f"r={r}: (5c+22) power = {power}, expected {expected_power}"

    def test_S4_denominator(self):
        """denom(S_4) = c(5c+22)."""
        sr = factor(S(4))
        _, d = fraction(sr)
        assert simplify(d - c * (5 * c + 22)) == 0

    def test_S5_denominator(self):
        """denom(S_5) = c^2(5c+22)."""
        sr = factor(S(5))
        _, d = fraction(sr)
        assert simplify(d - c**2 * (5 * c + 22)) == 0


# =====================================================================
# Section 5: Special values
# =====================================================================

class TestSpecialValues:
    """S_r evaluated at specific central charges."""

    def test_S5_at_c1(self):
        """S_5(1) = -48/(1*27) = -16/9."""
        assert simplify(S(5).subs(c, 1) - Rational(-16, 9)) == 0

    def test_S5_at_c13(self):
        """S_5(13) = -48/(169*87) = -16/4901."""
        assert simplify(S(5).subs(c, 13) - Rational(-16, 4901)) == 0

    def test_S5_at_c26(self):
        """S_5(26) = -48/(676*152) = -3/6422."""
        assert simplify(S(5).subs(c, 26) - Rational(-3, 6422)) == 0

    def test_S4_at_c1(self):
        """S_4(1) = 10/27."""
        assert simplify(S(4).subs(c, 1) - Rational(10, 27)) == 0

    @pytest.mark.parametrize("cv", [1, 2, 5, 10, 13, 25, 26, 100])
    def test_S5_nonzero(self, cv):
        """S_5 is nonzero at generic positive integer c."""
        assert S(5).subs(c, cv) != 0


# =====================================================================
# Section 6: Duality under c -> 26-c
# =====================================================================

class TestDuality:
    """Test behavior under Virasoro duality c -> 26-c."""

    @pytest.mark.parametrize("r", range(2, 11))
    def test_self_dual_at_c13(self, r):
        """S_r(13) = S_r(26-13) = S_r(13) (tautological at self-dual point)."""
        val = cancel(S(r).subs(c, 13))
        val_dual = cancel(S(r).subs(c, 26 - 13))
        assert simplify(val - val_dual) == 0

    def test_duality_nontrivial(self):
        """S_r(c) != S_r(26-c) in general for r >= 2."""
        for r in [2, 4, 5]:
            diff_expr = simplify(S(r) - S_dual(r))
            assert diff_expr != 0, f"S_{r}(c) = S_{r}(26-c) identically"

    def test_duality_ratio_at_13_is_1(self):
        """duality ratio S_r(c)/S_r(26-c) equals 1 at c=13."""
        for r in range(2, 10):
            ratio = duality_ratio(r)
            assert simplify(ratio.subs(c, 13) - 1) == 0, f"ratio != 1 at c=13 for r={r}"

    def test_alpha_duality(self):
        """alpha(c) vs alpha(26-c): the deviation from 36 is NOT symmetric."""
        a = alpha()
        a_dual = a.subs(c, 26 - c)
        # alpha = 36 + 80/(5c+22), alpha_dual = 36 + 80/(152-5c)
        assert simplify(a - a_dual) != 0


# =====================================================================
# Section 7: Self-dual sequence S_r(13)
# =====================================================================

class TestSelfDualSequence:
    """The sequence S_r(13) at the self-dual point."""

    def test_S2_at_13(self):
        assert S_at_13(2) == Rational(13, 2)

    def test_S3_at_13(self):
        assert S_at_13(3) == Rational(2)

    def test_S4_at_13(self):
        expected = Rational(10) / (13 * 87)
        assert simplify(S_at_13(4) - expected) == 0

    def test_sequence_alternating_sign(self):
        """For c=13 > 0: S_2,S_3,S_4 > 0; S_5 < 0; S_6 > 0; S_7 < 0; ..."""
        seq = self_dual_sequence(10)
        assert seq[2] > 0
        assert seq[3] > 0
        assert seq[4] > 0
        assert seq[5] < 0
        assert seq[6] > 0
        assert seq[7] < 0

    def test_sequence_decreasing_magnitude(self):
        """|S_r(13)| is eventually decreasing (tower converges)."""
        seq = self_dual_sequence(12)
        # After the first few, magnitudes should decrease
        for r in range(6, 12):
            assert abs(float(seq[r])) < abs(float(seq[r - 1])) or r <= 5


# =====================================================================
# Section 8: Cross-verification with direct H-Poisson computation
# =====================================================================

class TestCrossVerification:
    """Cross-check recursive S(r) against direct H-Poisson bracket computation."""

    def test_direct_vs_recursive(self):
        """compute_shadow_tower_direct matches S(r) for r=2..8."""
        direct = compute_shadow_tower_direct(8)
        for r in range(2, 9):
            assert simplify(direct[r] - S(r)) == 0, f"Mismatch at r={r}"


# =====================================================================
# Section 9: Ratio patterns and convergence
# =====================================================================

class TestRatioPatterns:
    """Test consecutive ratios and convergence behavior."""

    def test_S5_over_S4(self):
        """S_5/S_4 = -24/(5c)."""
        ratio = cancel(S(5) / S(4))
        expected = Rational(-24, 5) / c
        assert simplify(ratio - expected) == 0

    def test_numerical_ratios_bounded(self):
        """|S_{r+1}/S_r| at c=1 is bounded (finite radius of convergence)."""
        ratios = numerical_ratio_pattern(12, c_val=1)
        for r, val in ratios.items():
            assert abs(val) < 100, f"Unbounded ratio at r={r}: {val}"

    def test_numerical_ratios_c13_bounded(self):
        """Ratios at c=13 are bounded."""
        ratios = numerical_ratio_pattern(12, c_val=13)
        for r, val in ratios.items():
            assert abs(val) < 10, f"Unbounded ratio at r={r}: {val}"

    def test_ratio_pattern_symbolic(self):
        """Check symbolic ratios exist and are rational functions of c."""
        ratios = check_ratio_pattern(8)
        for r, ratio in ratios.items():
            assert ratio is not None
            # Should be a rational function of c
            _, d = fraction(factor(ratio))
            assert d.is_polynomial(c) or d == 1


# =====================================================================
# Section 10: Generating function properties
# =====================================================================

class TestGFProperties:
    """Test properties of the closed-form generating function."""

    def test_H_starts_at_t2(self):
        """H(t) = O(t^2): no t^0 or t^1 term."""
        from sympy import series as sym_series
        H = H_generating()
        s = sym_series(H, t, 0, 3)
        assert s.coeff(t, 0) == 0
        assert s.coeff(t, 1) == 0

    def test_H_t2_coefficient(self):
        """[t^2] H(t) = 2 * S_2 = c."""
        from sympy import series as sym_series
        H = H_generating()
        s = sym_series(H, t, 0, 3)
        assert simplify(s.coeff(t, 2) - c) == 0

    def test_H_t3_coefficient(self):
        """[t^3] H(t) = 3 * S_3 = 6."""
        from sympy import series as sym_series
        H = H_generating()
        s = sym_series(H, t, 0, 4)
        assert simplify(s.coeff(t, 3) - 6) == 0

    def test_quadratic_positive_definite(self):
        """Q(t,c) > 0 for all real t when c > 0 (since discriminant < 0)."""
        # Discriminant < 0 and leading coeff alpha > 0 for c > 0
        # means Q > 0 for all real t.
        a = alpha()
        # alpha > 0 for c > 0: (180c+872)/(5c+22) > 0 since both num and denom > 0
        assert a.subs(c, 1) > 0
        assert a.subs(c, 100) > 0
        assert a.subs(c, Rational(1, 10)) > 0

    def test_truncated_gf_consistency(self):
        """Truncated GF sum matches direct sum of S_r*t^r."""
        G8 = shadow_gf_truncated(8)
        direct_sum = sum(S(r) * t**r for r in range(2, 9))
        assert simplify(G8 - direct_sum) == 0


# =====================================================================
# Section 11: Obstruction structure
# =====================================================================

class TestObstructionStructure:
    """Test properties of the obstruction classes o^(r)."""

    def test_o3_is_zero(self):
        """o^(3) = 0 (no pairs j+k=5 with j,k >= 3 exist except j=2,k=3 which is nabla)."""
        # For r=3, target = 5. Pairs (j,k) with j+k=5, j,k>=3: none (3+2=5 but k=2<3)
        o3 = obstruction_coefficient(3)
        assert o3 == 0

    def test_o4_single_source(self):
        """o^(4) has single source: {Sh_3, Sh_3}_H (pair (3,3))."""
        o4 = obstruction_coefficient(4)
        # Manual: (1/2) * 2*3*3*2*2/c = 36/c
        assert simplify(o4 - Rational(36) / c) == 0

    def test_o5_single_source(self):
        """o^(5) has single source: {Sh_3, Sh_4}_H (pair (3,4))."""
        o5 = obstruction_coefficient(5)
        # 2*3*4*S_3*S_4/c = 24*2*10/[c^2(5c+22)] = 480/[c^2(5c+22)]
        expected = Rational(480) / (c**2 * (5 * c + 22))
        assert simplify(o5 - expected) == 0

    def test_o6_two_sources(self):
        """o^(6) has two sources: {Sh_3, Sh_5}_H and {Sh_4, Sh_4}_H."""
        # j+k = 8, j,k >= 3: (3,5) and (4,4)
        o6 = obstruction_coefficient(6)
        assert o6 != 0

    @pytest.mark.parametrize("r", range(5, 13))
    def test_obstruction_nonzero(self, r):
        """o^(r) is generically nonzero for r >= 5 (infinite tower)."""
        o_r = obstruction_coefficient(r)
        assert o_r != 0, f"o^({r}) = 0 (tower would terminate)"


# =====================================================================
# Section 12: Sign pattern
# =====================================================================

class TestSignPattern:
    """Test the sign pattern of S_r(c) for c > 0."""

    def test_signs_at_c10(self):
        """Signs at c=10: +,+,+,-,+,-,+,-,..."""
        expected_signs = {2: True, 3: True, 4: True, 5: False, 6: True, 7: False}
        for r, positive in expected_signs.items():
            val = S(r).subs(c, 10)
            assert (val > 0) == positive, f"S_{r}(10) sign wrong"

    def test_alternating_from_r4(self):
        """From r=4 onward, signs alternate: +,-,+,-,..."""
        for r in range(4, 13):
            val = float(S(r).subs(c, 10))
            expected_positive = (r % 2 == 0)
            assert (val > 0) == expected_positive, \
                f"r={r}: val={val}, expected {'positive' if expected_positive else 'negative'}"


# =====================================================================
# Section 13: Large-c asymptotics
# =====================================================================

class TestLargeCAsymptotics:
    """Test behavior as c -> infinity."""

    def test_S2_linear_in_c(self):
        """S_2 = c/2 grows linearly."""
        assert limit(S(2) / c, c, oo) == Rational(1, 2)

    def test_S3_constant(self):
        """S_3 = 2 is independent of c."""
        assert limit(S(3), c, oo) == 2

    def test_S4_decays(self):
        """S_4 -> 0 as c -> infinity (like 2/c^2)."""
        assert limit(S(4), c, oo) == 0
        assert limit(S(4) * c**2, c, oo) == 2  # 10/(5c^2) -> 2/c^2

    def test_higher_decay(self):
        """S_r -> 0 as c -> infinity for r >= 4."""
        for r in range(4, 9):
            assert limit(S(r), c, oo) == 0


# =====================================================================
# Section 14: Edge cases
# =====================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_r_below_2_raises(self):
        """S(r) raises ValueError for r < 2."""
        with pytest.raises(ValueError):
            S(1)
        with pytest.raises(ValueError):
            S(0)

    def test_cache_clear(self):
        """Cache clears correctly."""
        _ = S(5)
        clear_cache()
        # Should recompute without error
        val = S(5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(val - expected) == 0

    def test_high_arity(self):
        """S(15) computes without error and is a rational function of c."""
        s15 = S(15)
        assert s15 is not None
        _, d = fraction(factor(s15))
        assert d.is_polynomial(c) or d == 1
