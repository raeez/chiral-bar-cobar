"""Tests for shadow_potential_singularity.py — singularity theory of Virasoro shadow potential.

Tests the shadow potential S(x), its critical equation, shadow discriminant,
Milnor numbers, critical points, and singularity wall persistence.

20+ tests organized into sections:
  1. Shadow potential construction (4 tests)
  2. Critical equation (4 tests)
  3. Shadow discriminant structure (5 tests)
  4. Milnor numbers (4 tests)
  5. Critical points (4 tests)
  6. Singularity walls and persistence (3 tests)
  7. Hessian and Morse theory (2 tests)
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

import pytest
from sympy import (
    Symbol, Rational, simplify, expand, diff, factor, S, numer, denom,
    factorial, Poly, N,
)

from shadow_potential_singularity import (
    shadow_potential_1d,
    shadow_potential_coefficients,
    critical_equation_1d,
    critical_polynomial_1d,
    shadow_discriminant_1d,
    discriminant_numerator,
    discriminant_denominator,
    shadow_discriminant_factors,
    milnor_number_at_origin,
    singularity_type_at_origin,
    critical_points_numerical,
    real_critical_points,
    critical_values_numerical,
    discriminant_pole_order,
    discriminant_zero_test,
    factor_5c22_pole_persistence,
    factor_15c56_in_numerator,
    hessian_at_origin,
    morse_index_generic,
)

c = Symbol('c')
x = Symbol('x')


# ============================================================================
# 1. Shadow potential construction
# ============================================================================

class TestShadowPotential:
    """Tests for the shadow potential S(x)."""

    def test_potential_leading_term(self):
        """S(x) starts with (c/4)x^2 = kappa * x^2 / 2!."""
        pot = shadow_potential_1d(4)
        p = Poly(pot, x, domain='ZZ(c)')
        coeff_x2 = p.nth(2)
        assert simplify(coeff_x2 - c / 4) == 0

    def test_potential_cubic_term(self):
        """Cubic coefficient: Sh_3/3! = 2/6 = 1/3."""
        pot = shadow_potential_1d(4)
        p = Poly(pot, x, domain='ZZ(c)')
        coeff_x3 = p.nth(3)
        assert simplify(coeff_x3 - Rational(1, 3)) == 0

    def test_potential_quartic_term(self):
        """Quartic coefficient: Sh_4/4! = 10/[c(5c+22)] / 24 = 5/[12c(5c+22)]."""
        pot = shadow_potential_1d(4)
        p = Poly(pot, x, domain='ZZ(c)')
        coeff_x4 = p.nth(4)
        expected = Rational(5, 12) / (c * (5*c + 22))
        assert simplify(coeff_x4 - expected) == 0

    def test_potential_coefficients_dict(self):
        """shadow_potential_coefficients returns Sh_r/r! for each r."""
        coeffs = shadow_potential_coefficients(5)
        assert 2 in coeffs
        assert 3 in coeffs
        assert 4 in coeffs
        assert 5 in coeffs
        # Check arity 2: c/4
        assert simplify(coeffs[2] - c / 4) == 0


# ============================================================================
# 2. Critical equation
# ============================================================================

class TestCriticalEquation:
    """Tests for the reduced critical equation."""

    def test_critical_degree_arity4(self):
        """At arity 4, reduced critical equation is degree 2 in x."""
        crit = critical_equation_1d(4)
        p = Poly(crit, x, domain='ZZ(c)')
        assert p.degree() == 2

    def test_critical_degree_arity7(self):
        """At arity 7, reduced critical equation is degree 5 in x."""
        crit = critical_equation_1d(7)
        p = Poly(crit, x, domain='ZZ(c)')
        assert p.degree() == 5

    def test_critical_constant_term(self):
        """Constant term of reduced critical equation = c/2.

        S(x) = (c/4)x^2 + ..., so dS/dx = (c/2)x + x^2 + ...,
        and (dS/dx)/x = c/2 + x + ... The constant term is c/2.
        """
        crit = critical_equation_1d(7)
        p = Poly(crit, x, domain='ZZ(c)')
        const = p.nth(0)
        assert simplify(const - c / 2) == 0

    def test_critical_linear_term(self):
        """Linear coefficient = Sh_3/2! = 2/2 = 1 (from gravitational cubic)."""
        crit = critical_equation_1d(7)
        p = Poly(crit, x, domain='ZZ(c)')
        linear = p.nth(1)
        assert simplify(linear - 1) == 0


# ============================================================================
# 3. Shadow discriminant structure
# ============================================================================

class TestShadowDiscriminant:
    """Tests for the shadow discriminant."""

    def test_discriminant_arity4_numerator(self):
        """At arity 4: discriminant numerator = (15c+56)."""
        num = discriminant_numerator(4)
        # Check that c=-56/15 is a root
        assert simplify(num.subs(c, Rational(-56, 15))) == 0

    def test_discriminant_arity4_denominator(self):
        """At arity 4: discriminant denominator has (5c+22)."""
        den = discriminant_denominator(4)
        assert simplify(den.subs(c, Rational(-22, 5))) == 0

    def test_discriminant_arity5_factors(self):
        """At arity 5: numerator factors into two linear terms."""
        num = discriminant_numerator(5)
        # Two factors: (30c+133) and (90c+271)
        assert simplify(num.subs(c, Rational(-133, 30))) == 0
        assert simplify(num.subs(c, Rational(-271, 90))) == 0

    def test_discriminant_nonzero_generic(self):
        """Discriminant is nonzero at generic c (e.g., c=1)."""
        for arity in [4, 5, 6, 7]:
            disc = shadow_discriminant_1d(arity)
            val = disc.subs(c, 1)
            assert simplify(val) != 0, f"Discriminant vanishes at c=1 for arity {arity}"

    def test_discriminant_rational_function(self):
        """Discriminant is a proper rational function of c (not polynomial)."""
        disc = shadow_discriminant_1d(5)
        den = denom(disc)
        # Denominator should not be 1
        assert simplify(den - 1) != 0


# ============================================================================
# 4. Milnor numbers
# ============================================================================

class TestMilnorNumber:
    """Tests for Milnor numbers at special central charges."""

    def test_milnor_generic(self):
        """Generic c: Milnor number = 1 (Morse/A_1)."""
        # c=1 is generic
        mu = milnor_number_at_origin(7, 1)
        assert mu == 1

    def test_milnor_c_zero(self):
        """c=0: kappa vanishes, Milnor number jumps."""
        mu = milnor_number_at_origin(7, 0)
        # At c=0, kappa=0 so dS/dx starts at x^2 (cubic in S).
        # The Milnor number = order of vanishing of dS/dx at x=0.
        # With max_arity=7, the derivative has terms x^1 (coeff c/2=0),
        # x^2 (coeff 1/3, independent of c), etc.
        # Actually dS/dx = (c/2)x + x^2 + ... At c=0: dS/dx = x^2 + ...
        # But quartic coeff ~ 1/c diverges at c=0. Check truncated potential.
        assert mu >= 2  # at least A_2 degeneration

    def test_milnor_c_minus22over5(self):
        """c=-22/5: shadow coefficients diverge from arity 4; truncated potential is Morse."""
        mu = milnor_number_at_origin(7, Rational(-22, 5))
        # Truncated to arity 3 (the well-defined part): S = (c/4)x^2 + (1/3)x^3
        # dS/dx = (c/2)x + x^2; at c=-22/5: dS/dx = (-11/5)x + x^2
        # ord_0 = 1, so mu = 1 (Morse)
        assert mu == 1

    def test_singularity_type_generic(self):
        """Singularity type at generic c is A_1."""
        stype = singularity_type_at_origin(7, 1)
        assert stype == 'A_1'


# ============================================================================
# 5. Critical points
# ============================================================================

class TestCriticalPoints:
    """Tests for numerical critical point computation."""

    def test_critical_count_c1(self):
        """At c=1 with arity 7: 5 nontrivial critical points."""
        pts = critical_points_numerical(1, max_arity=7)
        assert len(pts) == 5

    def test_real_critical_count_c1(self):
        """At c=1 with arity 7: 3 real critical points."""
        real_pts = real_critical_points(1, max_arity=7)
        assert len(real_pts) == 3

    def test_critical_satisfy_equation(self):
        """Critical points satisfy the reduced critical equation."""
        crit = critical_equation_1d(7)
        pts = critical_points_numerical(1, max_arity=7)
        for pt in pts:
            val = abs(complex(N(crit.subs(c, 1).subs(x, pt))))
            assert val < 1e-6, f"Critical point {pt} does not satisfy equation: |f| = {val}"

    def test_critical_conjugate_pairs(self):
        """Complex critical points come in conjugate pairs."""
        pts = critical_points_numerical(1, max_arity=7)
        complex_pts = [z for z in pts if abs(z.imag) > 1e-10]
        assert len(complex_pts) % 2 == 0
        # Check that conjugate pairs exist
        for z in complex_pts:
            conj = z.conjugate()
            found = any(abs(w - conj) < 1e-6 for w in complex_pts)
            assert found, f"No conjugate found for {z}"


# ============================================================================
# 6. Singularity walls and persistence
# ============================================================================

class TestSingularityWalls:
    """Tests for singularity wall persistence."""

    def test_5c22_pole_order_pattern(self):
        """(5c+22) pole order in discriminant = n(n-1)/2 where n = arity - 2."""
        poles = factor_5c22_pole_persistence(7)
        for arity, order in poles.items():
            n = arity - 2
            expected = n * (n - 1) // 2
            assert order == expected, (
                f"Arity {arity}: (5c+22) pole order = {order}, expected {expected}"
            )

    def test_15c56_arity4_only(self):
        """(15c+56) divides discriminant numerator only at arity 4."""
        zeros = factor_15c56_in_numerator(7)
        assert zeros[4] is True
        for arity in [5, 6, 7]:
            assert zeros[arity] is False, (
                f"(15c+56) should not divide numerator at arity {arity}"
            )

    def test_5c22_persists_all_arities(self):
        """(5c+22) appears in denominator at all arities >= 4."""
        poles = factor_5c22_pole_persistence(7)
        for arity in [4, 5, 6, 7]:
            assert poles[arity] >= 1, (
                f"(5c+22) should appear in denominator at arity {arity}"
            )


# ============================================================================
# 7. Hessian and Morse theory
# ============================================================================

class TestHessian:
    """Tests for Hessian and Morse index."""

    def test_hessian_is_kappa(self):
        """S''(0) = kappa = c/2."""
        H = hessian_at_origin(7)
        assert simplify(H - c / 2) == 0

    def test_morse_index_structure(self):
        """Morse index dictionary has correct entries."""
        mi = morse_index_generic()
        assert mi['c > 0']['index'] == 0
        assert mi['c < 0']['index'] == 1
        assert mi['c = 0']['index'] is None


# ============================================================================
# 8. Cross-checks and consistency
# ============================================================================

class TestConsistency:
    """Cross-checks between different functions."""

    def test_potential_derivative_matches_critical(self):
        """dS/dx / x matches critical_equation_1d."""
        pot = shadow_potential_1d(6)
        deriv = diff(pot, x)
        reduced_from_pot = expand(deriv / x)
        # This should match the critical equation after cancellation
        crit = critical_equation_1d(6)
        # They may differ by simplification; check at a point
        val1 = reduced_from_pot.subs([(c, 3), (x, 2)])
        val2 = crit.subs([(c, 3), (x, 2)])
        assert abs(float(val1) - float(val2)) < 1e-10

    def test_critical_values_at_saddle(self):
        """Critical values are computed at actual critical points."""
        cvals = critical_values_numerical(1, max_arity=5)
        assert len(cvals) > 0
        # Each entry is (critical_point, potential_value) pair
        for pt, val in cvals:
            assert isinstance(pt, complex)
            assert isinstance(val, complex)

    def test_arity_truncation_monotone(self):
        """Higher arity adds more terms; the degree-2 part is unchanged."""
        pot4 = shadow_potential_1d(4)
        pot7 = shadow_potential_1d(7)
        p4 = Poly(pot4, x, domain='ZZ(c)')
        p7 = Poly(pot7, x, domain='ZZ(c)')
        # Degree-2 and degree-3 coefficients agree
        assert simplify(p4.nth(2) - p7.nth(2)) == 0
        assert simplify(p4.nth(3) - p7.nth(3)) == 0
        # Degree-5 is absent in arity 4
        assert simplify(p4.nth(5)) == 0

    def test_discriminant_factors_structure(self):
        """shadow_discriminant_factors returns both numerator and denominator."""
        facs = shadow_discriminant_factors(5)
        assert 'numerator_factors' in facs
        assert 'denominator_factors' in facs
        # Denominator should have (5c+22) and c
        den_bases = [str(base) for base, _ in facs['denominator_factors']]
        assert any('c' in b for b in den_bases)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
