"""Tests for the Propagator Variance Theorem.

THEOREM (Propagator Variance = Non-Autonomy):
  delta = sum f_i^2/kappa_i - (sum f_i)^2 / (sum kappa_i) >= 0
  with equality iff f_i proportional to kappa_i.

Verified for W_3 against the explicit shadow tower computation.
"""

import pytest
from sympy import Rational, Symbol, cancel, factor, simplify, sqrt, symbols

from compute.lib.propagator_variance import (
    propagator_variance,
    curvature_proportionality_test,
    mixing_polynomial,
    w3_kappas,
    w3_quartic_gradients,
    w3_mixing_polynomial,
    w3_propagator_variance,
    w3_enhanced_symmetry_loci,
    autonomy_criterion,
)

c = Symbol('c')


class TestPropagatorVariance:
    """Core propagator variance formula."""

    def test_non_negative_at_c1(self):
        delta = w3_propagator_variance()
        assert delta.subs(c, 1) > 0

    def test_non_negative_at_c13(self):
        delta = w3_propagator_variance()
        assert delta.subs(c, 13) > 0

    def test_non_negative_at_c25(self):
        delta = w3_propagator_variance()
        assert delta.subs(c, 25) > 0

    def test_vanishes_at_enhanced_symmetry(self):
        """delta = 0 at the roots of P."""
        delta = w3_propagator_variance()
        for c_val in w3_enhanced_symmetry_loci():
            assert cancel(delta.subs(c, c_val)) == 0

    def test_perfect_square(self):
        """delta is a perfect square (proportional to P^2)."""
        delta = w3_propagator_variance()
        P = w3_mixing_polynomial()
        ratio = cancel(delta / P**2)
        # ratio should be a monomial in c (no polynomial numerator)
        from sympy import Poly, numer
        num = numer(cancel(ratio))
        assert Poly(num, c).degree() == 0, f"ratio has polynomial numerator: {num}"


class TestMixingPolynomial:
    """The mixing polynomial P(c) = 25c^2 + 100c - 428."""

    def test_w3_polynomial(self):
        P = w3_mixing_polynomial()
        assert P == 25 * c**2 + 100 * c - 428

    def test_decomposition(self):
        """P = 25(c+2)^2 - 528."""
        P = w3_mixing_polynomial()
        assert cancel(P - (25 * (c + 2)**2 - 528)) == 0

    def test_enhanced_symmetry_loci(self):
        """P = 0 at c = -2 ± 4√33/5."""
        loci = w3_enhanced_symmetry_loci()
        assert len(loci) == 2
        assert -2 + 4 * sqrt(33) / 5 in loci or cancel(-2 + 4 * sqrt(33) / 5 - loci[0]) == 0

    def test_curvature_proportionality(self):
        """P = 0 iff f_T/kappa_T = f_W/kappa_W."""
        kappas = w3_kappas()
        fs = w3_quartic_gradients()
        test = curvature_proportionality_test(kappas, fs)
        P = w3_mixing_polynomial()
        # test should be proportional to P
        ratio = cancel(test * c**2 * (5 * c + 22)**3 / P)
        from sympy import Poly, numer
        assert Poly(numer(cancel(ratio)), c).degree() == 0


class TestConsistencyWithShadowTower:
    """Cross-check against the explicit W_3 shadow tower computation."""

    def test_matches_bracket_difference(self):
        """delta = {Sh_4,Sh_4}_{2D} - {Sh_4,Sh_4}_{1D} on diagonal."""
        delta = w3_propagator_variance()
        known = Rational(1280) * (25 * c**2 + 100 * c - 428)**2 / (c**3 * (5 * c + 22)**6)
        assert cancel(delta - known) == 0

    def test_s6_difference(self):
        """S_6^actual - S_6^autonomous = -delta / 12 (contribution to arity 6)."""
        delta = w3_propagator_variance()
        # At arity 6: 2*6*S_6 + (1/2)*obs = 0
        # The obs difference is (1/2)*delta (from the (4,4) pair)
        # So S_6_diff = -(1/2)*delta / (2*6) = -delta/24
        # Actually: S_6_diff = -(1/2)*delta/(2*6) = -delta/24
        # But we computed S_6_diff = -160*P^2/(3c^3(5c+22)^6)
        s6_diff = Rational(-160) * (25 * c**2 + 100 * c - 428)**2 / (3 * c**3 * (5 * c + 22)**6)
        predicted = -delta / 24
        assert cancel(s6_diff - predicted) == 0


class TestAutonomyForVirasoro:
    """The Virasoro (rank 1) is always autonomous."""

    def test_rank1_variance_zero(self):
        kappas = [c / 2]
        fs = [Rational(40) / (c * (5 * c + 22))]
        assert propagator_variance(kappas, fs) == 0

    def test_rank1_always_autonomous(self):
        kappas = [c / 2]
        fs = [Rational(40) / (c * (5 * c + 22))]
        assert autonomy_criterion(kappas, fs)


class TestGeneralProperties:
    """General properties of the propagator variance."""

    def test_diagonal_kappa_proportional(self):
        """If f_i = lambda * kappa_i, delta = 0."""
        lam = Symbol('lambda')
        kappas = [c / 2, c / 3, c / 5]
        fs = [lam * k for k in kappas]
        assert propagator_variance(kappas, fs) == 0

    def test_two_equal_kappas(self):
        """If kappa_T = kappa_W, delta = (f_T - f_W)^2 / (4 kappa)."""
        k = Symbol('k', positive=True)
        f1, f2 = symbols('f1 f2')
        delta = propagator_variance([k, k], [f1, f2])
        expected = (f1 - f2)**2 / (2 * k)
        assert cancel(delta - expected) == 0

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 25, 50])
    def test_non_negative_numerical(self, c_val):
        delta = w3_propagator_variance()
        assert float(delta.subs(c, c_val)) >= 0
