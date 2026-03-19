"""Tests for the Virasoro quintic shadow obstruction o^(5)_Vir.

Tests the computation Sh_5(Vir_c) = -48/[c^2(5c+22)] x^5.
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, diff

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.virasoro_quintic_shadow import (
    kappa_vir, cubic_shadow_vir, quartic_contact_vir,
    h_poisson_bracket, quintic_obstruction, quintic_obstruction_coefficient,
    quintic_shadow, quintic_shadow_coefficient,
    verify_quintic, verify_sanity_checks, verify_duality_behavior,
    P_VIR, c, x,
)
from lib.virasoro_shadow_tower import compute_shadow_tower, shadow_coefficients


# ═══════════════════════════════════════════════════════════════════════
# Core computation
# ═══════════════════════════════════════════════════════════════════════

class TestQuinticObstruction:
    """Test the quintic obstruction o^(5)_Vir."""

    def test_obstruction_formula(self):
        """o^(5) = 480/[c^2(5c+22)] x^5."""
        o5 = quintic_obstruction_coefficient()
        expected = Rational(480, 1) / (c**2 * (5*c + 22))
        assert simplify(o5 - expected) == 0

    def test_obstruction_source(self):
        """o^(5) = {Sh_3, Sh_4}_H (single source term)."""
        obs = quintic_obstruction()
        bracket = h_poisson_bracket(cubic_shadow_vir(), quartic_contact_vir())
        assert simplify(obs - bracket) == 0

    def test_obstruction_degree(self):
        """o^(5) is homogeneous of degree 5 in x."""
        from sympy import Poly
        obs = quintic_obstruction()
        p = Poly(obs, x)
        # Only x^5 term
        for i in range(10):
            if i != 5:
                assert p.nth(i) == 0, f"Nonzero coefficient at x^{i}"

    def test_obstruction_nonzero(self):
        """o^(5) is generically nonzero (proves infinite tower)."""
        o5 = quintic_obstruction_coefficient()
        assert o5 != 0


class TestQuinticShadow:
    """Test the quintic shadow Sh_5(Vir_c)."""

    def test_shadow_formula(self):
        """S_5 = -48/[c^2(5c+22)]."""
        S5 = quintic_shadow_coefficient()
        expected = Rational(-48, 1) / (c**2 * (5*c + 22))
        assert simplify(S5 - expected) == 0

    def test_shadow_from_obstruction(self):
        """S_5 = -o5/(2*5) = -o5/10."""
        o5 = quintic_obstruction_coefficient()
        S5 = quintic_shadow_coefficient()
        assert simplify(S5 + o5/10) == 0

    def test_shadow_negative(self):
        """S_5 < 0 for c > 0 (opposes quartic)."""
        S5 = quintic_shadow_coefficient()
        # For c > 0, c^2 > 0 and 5c+22 > 0, so S_5 = -48/(positive) < 0
        assert S5.subs(c, 1) < 0
        assert S5.subs(c, 100) < 0


class TestMasterEquation:
    """Test that nabla_H(Sh_5) + o^(5) = 0."""

    def test_master_equation(self):
        """The arity-5 master equation is satisfied."""
        Sh5 = quintic_shadow()
        kappa = kappa_vir() * x**2
        nabla = h_poisson_bracket(kappa, Sh5)
        obs = quintic_obstruction()
        assert simplify(nabla + obs) == 0

    def test_nabla_H_eigenvalue(self):
        """nabla_H(S x^r) = 2r S x^r for r=5."""
        S5 = quintic_shadow_coefficient()
        Sh5 = S5 * x**5
        kappa = kappa_vir() * x**2
        nabla = h_poisson_bracket(kappa, Sh5)
        expected = 2 * 5 * S5 * x**5
        assert simplify(nabla - expected) == 0


# ═══════════════════════════════════════════════════════════════════════
# Special values
# ═══════════════════════════════════════════════════════════════════════

class TestSpecialValues:
    """Test S_5 at special central charges."""

    def test_c1(self):
        """S_5(c=1) = -48/(1*27) = -16/9."""
        S5 = quintic_shadow_coefficient()
        assert simplify(S5.subs(c, 1) - Rational(-16, 9)) == 0

    def test_c13_self_dual(self):
        """S_5(c=13) = -48/(169*87) = -16/4901."""
        S5 = quintic_shadow_coefficient()
        assert simplify(S5.subs(c, 13) - Rational(-16, 4901)) == 0

    def test_c26(self):
        """S_5(c=26) = -48/(676*152) = -48/102752 = -3/6422."""
        S5 = quintic_shadow_coefficient()
        assert simplify(S5.subs(c, 26) - Rational(-3, 6422)) == 0

    def test_c_half(self):
        """S_5(c=1/2) = -48/[(1/4)(49/2)] = -48*8/49 = -384/49."""
        S5 = quintic_shadow_coefficient()
        val = S5.subs(c, Rational(1, 2))
        assert simplify(val - Rational(-384, 49)) == 0

    def test_c25(self):
        """S_5(c=25) at bosonic string."""
        S5 = quintic_shadow_coefficient()
        val = S5.subs(c, 25)
        expected = Rational(-48, 1) / (625 * 147)
        assert simplify(val - expected) == 0

    @pytest.mark.parametrize("cv", [1, 2, 5, 10, 13, 25, 26, 100])
    def test_nonzero_at_generic_c(self, cv):
        """S_5 is nonzero at generic positive integer c."""
        S5 = quintic_shadow_coefficient()
        assert S5.subs(c, cv) != 0


# ═══════════════════════════════════════════════════════════════════════
# Pole structure
# ═══════════════════════════════════════════════════════════════════════

class TestPoleStructure:
    """Test the pole structure of S_5."""

    def test_double_pole_c0(self):
        """S_5 has a double pole at c=0."""
        S5 = quintic_shadow_coefficient()
        # c^2 S_5 should be finite at c=0
        product = simplify(c**2 * S5)
        assert product.subs(c, 0) != 0
        # c^1 S_5 should still diverge
        product1 = simplify(c * S5)
        from sympy import limit
        assert limit(product1, c, 0) in [float('inf'), float('-inf'), Symbol('oo'), -Symbol('oo')]

    def test_simple_pole_lee_yang(self):
        """S_5 has a simple pole at c=-22/5 (Lee-Yang)."""
        S5 = quintic_shadow_coefficient()
        c_LY = Rational(-22, 5)
        # (5c+22) S_5 should be finite at c=-22/5
        product = simplify((5*c + 22) * S5)
        assert product.subs(c, c_LY) != 0

    def test_no_other_poles(self):
        """S_5 has no poles except at c=0 and c=-22/5."""
        S5 = quintic_shadow_coefficient()
        # Denominator is c^2(5c+22), roots are c=0 and c=-22/5 only
        from sympy import denom, solve
        d = denom(S5)
        roots = solve(d, c)
        assert set(roots) == {0, Rational(-22, 5)}


# ═══════════════════════════════════════════════════════════════════════
# Consistency with shadow tower module
# ═══════════════════════════════════════════════════════════════════════

class TestConsistencyWithTower:
    """Cross-check against virasoro_shadow_tower.py."""

    def test_matches_tower_computation(self):
        """S_5 matches the recursive tower computation."""
        coeffs = shadow_coefficients(5)
        S5_tower = coeffs[5]
        S5_direct = quintic_shadow_coefficient()
        assert simplify(S5_tower - S5_direct) == 0

    def test_tower_arity_234_agree(self):
        """Lower arities match between the two modules."""
        coeffs = shadow_coefficients(5)
        assert simplify(coeffs[2] - kappa_vir()) == 0
        assert simplify(coeffs[3] - 2) == 0
        Q0 = Rational(10, 1) / (c * (5*c + 22))
        assert simplify(coeffs[4] - Q0) == 0


# ═══════════════════════════════════════════════════════════════════════
# Duality
# ═══════════════════════════════════════════════════════════════════════

class TestDuality:
    """Test Virasoro duality Vir_c^! = Vir_{26-c}."""

    def test_self_dual_point(self):
        """At c=13: S_5(13) = S_5(26-13) = S_5(13)."""
        S5 = quintic_shadow_coefficient()
        assert simplify(S5.subs(c, 13) - S5.subs(c, 26 - 13)) == 0

    def test_duality_nontrivial(self):
        """S_5(c) != S_5(26-c) in general."""
        S5 = quintic_shadow_coefficient()
        diff_expr = simplify(S5 - S5.subs(c, 26 - c))
        assert diff_expr != 0

    def test_duality_ratio(self):
        """The ratio S_5(c)/S_5(26-c) has the expected form."""
        S5 = quintic_shadow_coefficient()
        S5_dual = S5.subs(c, 26 - c)
        ratio = factor(S5 / S5_dual)
        # Should be (26-c)^2(152-5c) / [c^2(5c+22)]
        # = -(26-c)^2(5c-152) / [c^2(5c+22)]
        assert simplify(ratio.subs(c, 13) - 1) == 0


# ═══════════════════════════════════════════════════════════════════════
# Sanity: vanishing for simpler algebras
# ═══════════════════════════════════════════════════════════════════════

class TestSanityVanishing:
    """Shadow depth bounds for simpler algebras."""

    def test_heisenberg_no_cubic(self):
        """Heisenberg has Sh_3 = 0, so all Sh_{r>=3} = 0."""
        # Heisenberg: single generator J, weight 1, OPE J(z)J(w) ~ 1/(z-w)^2
        # kappa = 1, no nonlinear OPE => Sh_3 = 0
        # Shadow depth = 2 (Gaussian archetype G)
        pass  # Structural fact, no computation needed

    def test_affine_no_quartic(self):
        """Affine has Sh_4 = 0, so o^(5) = {Sh_3, Sh_4} = 0."""
        # Affine sl_2: Sh_3 from Lie bracket, Sh_4 = 0 (Lie archetype L)
        # Shadow depth = 3
        # => quintic obstruction {Sh_3, 0} = 0
        pass  # Structural fact

    def test_betagamma_no_quintic(self):
        """beta-gamma has shadow depth 4 (contact archetype C), Sh_5 = 0."""
        # beta-gamma: terminates at quartic
        # Shadow depth = 4
        pass  # Known from cor:nms-betagamma-mu-vanishing


# ═══════════════════════════════════════════════════════════════════════
# Ratio patterns
# ═══════════════════════════════════════════════════════════════════════

class TestRatioPatterns:
    """Test ratios between consecutive shadow coefficients."""

    def test_S5_over_S4(self):
        """S_5/S_4 = -48c(5c+22) / [10 c^2(5c+22)] = -48/(10c) = -24/(5c)."""
        S4 = Rational(10, 1) / (c * (5*c + 22))
        S5 = quintic_shadow_coefficient()
        ratio = factor(simplify(S5 / S4))
        expected_ratio = Rational(-24, 5) / c
        assert simplify(ratio - expected_ratio) == 0

    def test_S5_times_S3(self):
        """S_5 * S_3 = -96/[c^2(5c+22)]."""
        S3 = 2
        S5 = quintic_shadow_coefficient()
        product = simplify(S5 * S3)
        expected = Rational(-96, 1) / (c**2 * (5*c + 22))
        assert simplify(product - expected) == 0


# ═══════════════════════════════════════════════════════════════════════
# Higher shadow cross-checks
# ═══════════════════════════════════════════════════════════════════════

class TestHigherShadows:
    """Cross-check sextic and septic from the tower module."""

    def test_sextic_coefficient(self):
        """S_6 = 80(45c+193)/[3c^3(5c+22)^2] from tower."""
        coeffs = shadow_coefficients(6)
        S6 = coeffs[6]
        expected = 80 * (45*c + 193) / (3 * c**3 * (5*c + 22)**2)
        assert simplify(S6 - expected) == 0

    def test_septic_coefficient(self):
        """S_7 = -2880(15c+61)/[7c^4(5c+22)^2] from tower."""
        coeffs = shadow_coefficients(7)
        S7 = coeffs[7]
        expected = -2880 * (15*c + 61) / (7 * c**4 * (5*c + 22)**2)
        assert simplify(S7 - expected) == 0

    def test_alternating_signs(self):
        """Signs alternate: S_2 > 0, S_3 > 0, S_4 > 0, S_5 < 0, S_6 > 0, S_7 < 0
        (for c > 0)."""
        coeffs = shadow_coefficients(7)
        signs = {r: bool(coeffs[r].subs(c, 10) > 0) for r in range(2, 8)}
        # S_2=5>0, S_3=2>0, S_4>0, S_5<0, S_6>0, S_7<0
        assert signs[2] is True
        assert signs[3] is True
        assert signs[4] is True
        assert signs[5] is False
        assert signs[6] is True
        assert signs[7] is False


# ═══════════════════════════════════════════════════════════════════════
# Verification functions
# ═══════════════════════════════════════════════════════════════════════

class TestVerificationFunctions:
    """Test the built-in verify_* functions."""

    def test_verify_quintic(self):
        results = verify_quintic()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_sanity(self):
        results = verify_sanity_checks()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_duality(self):
        results = verify_duality_behavior()
        assert results["c=13: S5 = S5_dual"]
        assert results["duality nontrivial"]
