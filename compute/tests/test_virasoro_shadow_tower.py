"""
Tests for the Virasoro shadow Postnikov tower computation.

Verifies:
  - Known shadow values at arities 2-5
  - Recursive obstruction equation
  - Sign alternation pattern
  - Pole structure
  - Complementarity potential
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, S

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from virasoro_shadow_tower import (
    compute_shadow_tower, shadow_coefficients,
    h_poisson_bracket, verify_known_values, P, c, x
)


class TestKnownValues:
    """Verify shadow coefficients against known formulas."""

    def test_sh2_is_kappa(self):
        coeffs = shadow_coefficients(2)
        assert simplify(coeffs[2] - c/2) == 0

    def test_sh3_is_cubic(self):
        coeffs = shadow_coefficients(3)
        assert simplify(coeffs[3] - 2) == 0

    def test_sh4_is_quartic_contact(self):
        coeffs = shadow_coefficients(4)
        Q0 = Rational(10, 1) / (c * (5*c + 22))
        assert simplify(coeffs[4] - Q0) == 0

    def test_sh5_formula(self):
        """cor:virasoro-quintic-shadow-explicit"""
        coeffs = shadow_coefficients(5)
        expected = Rational(-48, 1) / (c**2 * (5*c + 22))
        assert simplify(coeffs[5] - expected) == 0

    def test_verify_all_known(self):
        verify_known_values()


class TestObstructionEquation:
    """Verify the master equation ∇_H(Sh_r) + o^(r) = 0."""

    def test_quintic_obstruction_matches_theorem(self):
        """thm:w-virasoro-quintic-forced"""
        shadows = compute_shadow_tower(4)
        o5 = h_poisson_bracket(shadows[3], shadows[4])
        o5 = simplify(o5)
        expected = 480 / (c**2 * (5*c + 22)) * x**5
        assert simplify(o5 - expected) == 0

    def test_quintic_nonzero_generically(self):
        shadows = compute_shadow_tower(5)
        assert shadows[5] != 0


class TestStructuralProperties:
    """Test structural properties of the shadow obstruction tower."""

    def test_sign_alternation_through_7(self):
        """Signs of coefficients at c=1."""
        coeffs = shadow_coefficients(7)
        signs = []
        for r in range(2, 8):
            val = coeffs[r].subs(c, 1)
            signs.append(1 if val > 0 else -1)
        # Expected: +, +, +, -, +, -
        assert signs == [1, 1, 1, -1, 1, -1]

    def test_pole_at_critical_level(self):
        """All shadows r >= 4 have a pole at c = 0."""
        coeffs = shadow_coefficients(7)
        for r in range(4, 8):
            val = coeffs[r].subs(c, 0)
            # Should diverge (pole), which sympy represents as zoo or oo
            from sympy import zoo, oo, nan
            assert val in (zoo, oo, -oo, nan) or not val.is_finite

    def test_collision_free_pole(self):
        """All shadows r >= 4 have a pole at c = -22/5."""
        coeffs = shadow_coefficients(7)
        for r in range(4, 8):
            val = coeffs[r].subs(c, Rational(-22, 5))
            from sympy import zoo, oo, nan
            assert val in (zoo, oo, -oo, nan) or not val.is_finite

    def test_sh6_numerator(self):
        """Sh_6 has numerator 45c + 193."""
        coeffs = shadow_coefficients(6)
        from sympy import numer, denom
        # Factor and check
        expr = factor(coeffs[6])
        # Should contain (45*c + 193) factor
        s = str(expr)
        assert '45*c + 193' in s or '193 + 45*c' in s

    def test_sh7_numerator(self):
        """Sh_7 has numerator 15c + 61."""
        coeffs = shadow_coefficients(7)
        expr = factor(coeffs[7])
        s = str(expr)
        assert '15*c + 61' in s or '61 + 15*c' in s


class TestComplementarityPotential:
    """Test the complementarity potential S_Vir(x)."""

    def test_heisenberg_limit(self):
        """At c → ∞, higher shadows vanish and S → (c/4)x²."""
        coeffs = shadow_coefficients(7)
        from sympy import limit, oo
        for r in range(4, 8):
            lim = limit(coeffs[r], c, oo)
            assert lim == 0

    def test_potential_at_c26(self):
        """Evaluate at c=26 (bosonic string critical dimension)."""
        coeffs = shadow_coefficients(7)
        for r in range(2, 8):
            val = coeffs[r].subs(c, 26)
            assert val.is_finite


class TestConsistency:
    """Cross-check the tower against known results."""

    def test_genus1_hessian_correction(self):
        """
        The genus-1 Hessian correction δH^(1)_Vir = 120/[c²(5c+22)]x²
        should be consistent with the shadow obstruction tower.
        """
        # δH^(1) = 120/[c²(5c+22)] x²
        # This is a genus-1 correction, not a genus-0 shadow
        # But it should be consistent: δH^(1) involves Sh_4 through
        # the genus-loop operator
        coeffs = shadow_coefficients(4)
        Q0 = coeffs[4]
        delta_H1 = 120 / (c**2 * (5*c + 22))
        # The relation: δH^(1) = (some function of) Q0 and κ
        # δH^(1)/Q0 = 120/[c²(5c+22)] / [10/(c(5c+22))] = 12/c
        ratio = simplify(delta_H1 / Q0)
        assert simplify(ratio - 12/c) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
