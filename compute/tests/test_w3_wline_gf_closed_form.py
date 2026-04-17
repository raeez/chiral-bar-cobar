r"""Test: W_3 W-line generating function F'(z) = (1 - sqrt(1-12z))/3.

PLATONIC INSCRIPTION (iter 60, 2026-04-17):
    thm:w3-wline-generating-function (exact algebraic GF),
    cor:w3-wline-self-consistency (F'(1/12) = 1/3),
    rem:w3-wline-catalan-identity (Catalan-reduction),
    in chapters/theory/shadow_tower_higher_coefficients.tex.

CLAIMS:
    (1) F'(z) = (1 - sqrt(1-12z))/3 (algebraic GF).
    (2) F(z) = z/3 + [(1-12z)^{3/2} - 1]/54.
    (3) Radius of convergence = 1/12.
    (4) F'(1/12) = 1/3 (self-consistency at radius).
    (5) a_n = 2*C_{n-2}*3^{n-2}/n where C_m is the m-th Catalan.

HZ-IV VERIFICATION:
    derived_from: compute/lib/w3_wline_shadow_tower.py::normalized_recursion
        (Poisson-bracket recurrence).

    verified_against: symbolic Taylor expansion of the algebraic
        generating function F'(z) = (1 - sqrt(1-12z))/3 via sympy.

    disjoint_rationale: path 1 computes a_n via bilinear convolution
        of previous shadows; path 2 computes [z^n] F(z) via power-series
        expansion of an algebraic function solved from a quadratic
        functional equation. The match is an algebraic identity
        independent of the convolution logic.
"""
import math
import unittest
import sys

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

import sympy as sp
from compute.lib.w3_wline_shadow_tower import normalized_recursion


class TestW3WlineGeneratingFunction(unittest.TestCase):
    """Path 2: algebraic GF expansion matches recursion output."""

    def test_gf_derivative_taylor_matches_recursion(self):
        """F'(z) = (1-sqrt(1-12z))/3 gives n*a_n as [z^{n-1}] coefficient."""
        z = sp.Symbol('z')
        Fprime = (1 - sp.sqrt(1 - 12 * z)) / 3
        # Taylor expand to 20 terms
        series = sp.series(Fprime, z, 0, 20).removeO()
        a_rec = normalized_recursion(20)
        # a_n = [z^{n-1}] F'(z) / n
        for n in range(2, 20):
            coeff_zn_minus_1 = series.coeff(z, n - 1)
            a_from_gf = coeff_zn_minus_1 / n
            self.assertEqual(
                sp.Rational(a_from_gf), sp.Rational(a_rec[n]),
                f"Mismatch at n={n}: GF={a_from_gf}, rec={a_rec[n]}"
            )

    def test_gf_evaluated_at_radius_is_one_third(self):
        """F'(1/12) = 1/3 (self-consistency at radius of convergence)."""
        z_val = sp.Rational(1, 12)
        Fprime_at_radius = (1 - sp.sqrt(1 - 12 * z_val)) / 3
        self.assertEqual(Fprime_at_radius, sp.Rational(1, 3))

    def test_gf_satisfies_quadratic_functional_equation(self):
        """(3/2) F'(z)^2 - F'(z) + 2z = 0 holds identically."""
        z = sp.Symbol('z')
        Fprime = (1 - sp.sqrt(1 - 12 * z)) / 3
        quadratic = sp.Rational(3, 2) * Fprime**2 - Fprime + 2 * z
        self.assertEqual(sp.simplify(quadratic), 0)


class TestW3WlineCatalanIdentity(unittest.TestCase):
    """Path 3: Catalan reduction a_n = 2 * C_{n-2} * 3^{n-2} / n."""

    def test_catalan_reduction_matches_recursion(self):
        """a_n = 2 * C_{n-2} * 3^{n-2} / n via standard Catalan numbers."""
        def catalan(m):
            # C_m = C(2m, m) / (m+1)
            from math import comb
            return comb(2 * m, m) // (m + 1)

        a_rec = normalized_recursion(20)
        for n in range(2, 20):
            a_from_catalan = 2 * catalan(n - 2) * 3 ** (n - 2) // n
            # Integer division valid since a_n is integer
            self.assertEqual(
                a_from_catalan, a_rec[n],
                f"Mismatch at n={n}: catalan={a_from_catalan}, rec={a_rec[n]}"
            )


class TestW3WlineSelfConsistencyNumerical(unittest.TestCase):
    """The self-consistency sum converges to 1/3 with Stirling tail."""

    def test_partial_sum_near_target(self):
        """Sum_{n=2..300} n*a_n*12^{1-n} approaches 1/3 with Stirling tail."""
        from fractions import Fraction
        a = normalized_recursion(100)
        B = Fraction(12)
        partial = Fraction(0)
        for n in sorted(a.keys()):
            partial += Fraction(n) * a[n] * B ** (1 - n)
        # At N=100, residual ~ 0.0188
        residual = float(Fraction(1, 3) - partial)
        self.assertGreater(residual, 0)
        self.assertLess(residual, 0.03)
        # Stirling tail: 1/(3*sqrt(pi*N))
        stirling_tail = 1 / (3 * math.sqrt(math.pi * 100))
        # Match to 3 decimals (sub-leading Stirling corrections 1/N suppress at N=100)
        self.assertAlmostEqual(residual, stirling_tail, places=3)


if __name__ == '__main__':
    unittest.main()
