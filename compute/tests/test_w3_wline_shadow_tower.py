"""Tests for W3 W-line shadow obstruction tower + W3 sigma-ring finite generation.

Covers:
  - W-line tower: 15 even-arity entries through arity 32
  - Z_2 parity: all odd arities vanish
  - Denominator pattern: c^{2n-3} (5c+22)^{3(n-1)}
  - Integer sequence a_n = 1, 2, 9, 54, 378, ...
  - Sigma invariant Delta^(r) = S_r(c) + S_r(100-c) on W-line
  - Finite generation: arities 6+ are ring products of arity 4
"""

from fractions import Fraction
from sympy import Symbol, Rational, simplify, factor, cancel, numer, denom, Poly, diff, S
import pytest

from compute.lib.w3_wline_shadow_tower import (
    compute_wline_tower,
    compute_wline_tower_even_only,
    sigma_invariant,
    c, x,
)

# ===========================================================================
# Basic structure
# ===========================================================================

class TestWlineTowerStructure:
    def test_S2_is_c_over_3(self):
        S = compute_wline_tower(4)
        assert simplify(S[2] - c / 3) == 0

    def test_S3_vanishes(self):
        S = compute_wline_tower(4)
        assert S[3] == 0

    def test_S4_quartic(self):
        S = compute_wline_tower(4)
        expected = Rational(2560) / (c * (5 * c + 22) ** 3)
        assert simplify(S[4] - expected) == 0

    def test_all_odd_vanish(self):
        S = compute_wline_tower(20)
        for r in range(3, 21, 2):
            assert S[r] == 0, f"Odd arity {r} should vanish"

    def test_all_even_nonzero(self):
        S = compute_wline_tower(20)
        for r in range(4, 21, 2):
            assert S[r] != 0, f"Even arity {r} should be nonzero"

    def test_15_even_entries(self):
        S = compute_wline_tower(32)
        nonzero = [r for r in range(4, 33, 2) if S.get(r, 0) != 0]
        assert len(nonzero) >= 15


# ===========================================================================
# Denominator pattern: c^{2n-3} (5c+22)^{3(n-1)}
# ===========================================================================

class TestDenominatorPattern:
    def test_S4_denom(self):
        """r=4 (n=2): c^1 (5c+22)^3."""
        S = compute_wline_tower(4)
        d = denom(cancel(S[4]))
        # Should be c * (5c+22)^3
        assert simplify(d - c * (5 * c + 22) ** 3) == 0

    def test_S6_denom(self):
        """r=6 (n=3): c^3 (5c+22)^6."""
        S = compute_wline_tower(6)
        d = factor(denom(cancel(S[6])))
        # c^3 * (5c+22)^6, possibly with rational constant
        # Check degree in c: should be 3 + 6 = 9
        p = Poly(d, c)
        assert p.degree() == 3 + 6  # c^3 * (linear)^6

    def test_S8_denom_degree(self):
        """r=8 (n=4): c^5 (5c+22)^9, total degree 14."""
        S = compute_wline_tower(8)
        d = factor(denom(cancel(S[8])))
        p = Poly(d, c)
        assert p.degree() == 5 + 9  # c^5 * (linear)^9


# ===========================================================================
# Integer sequence a_n
# ===========================================================================

class TestIntegerSequence:
    def test_normalized_sequence(self):
        """Extract a_n from S_{2n} and verify first values."""
        S = compute_wline_tower(12)
        Q_WW = Rational(2560) / (c * (5 * c + 22) ** 3)
        assert simplify(S[4] - Q_WW) == 0
        S6_val = S[6].subs(c, 1)
        assert S6_val < 0, "S_6 should be negative (sign (-1)^3)"

    def test_recursion_a3_equals_2(self):
        S = compute_wline_tower(6)
        expected_S6 = -2 * 2560 ** 2 / (c ** 3 * (5 * c + 22) ** 6)
        assert simplify(S[6] / expected_S6 - 1) == 0

    def test_recursion_a4_equals_9(self):
        S = compute_wline_tower(8)
        expected_S8 = 9 * 2560 ** 3 / (c ** 5 * (5 * c + 22) ** 9)
        assert simplify(S[8] / expected_S8 - 1) == 0

    def test_closed_form_gf(self):
        """Verify the closed form a_n = (-12)^n C(3/2, n) / 54 for all computed entries."""
        from sympy import binomial, Integer
        S = compute_wline_tower(32)
        for m in range(2, 17):
            r = 2 * m
            a_n = binomial(Rational(3, 2), m) * (-12) ** m / 54
            expected = (-1) ** m * a_n * Integer(2560) ** (m - 1) / (
                c ** (2 * m - 3) * (5 * c + 22) ** (3 * (m - 1))
            )
            assert simplify(cancel(S[r] - expected)) == 0, f"Closed form fails at n={m}"


# ===========================================================================
# Sigma invariant: Delta^(r) = S_r(c) + S_r(100-c)
# ===========================================================================

class TestSigmaInvariant:
    def test_delta2_constant(self):
        """Delta^(2) = c/3 + (100-c)/3 = 100/3."""
        S = compute_wline_tower(4)
        delta = sigma_invariant(S[2], 100)
        assert simplify(delta - Rational(100, 3)) == 0

    def test_delta4_nonzero(self):
        """Delta^(4) should be nonzero and depend on c."""
        S = compute_wline_tower(4)
        delta = sigma_invariant(S[4], 100)
        assert delta != 0
        assert simplify(diff(delta, c)) != 0  # c-dependent

    def test_delta6_nonzero(self):
        S = compute_wline_tower(6)
        delta = sigma_invariant(S[6], 100)
        assert delta != 0


# ===========================================================================
# Finite generation on W-line: S_{2m} determined by S_4 for m >= 3
# ===========================================================================

class TestFiniteGenerationWline:
    def test_S6_from_S4(self):
        """S_6 is determined by {S_4, S_4}_H on the W-line."""
        S = compute_wline_tower(6)
        # Master equation: S_6 = -(1/12) * (1/2) * {Sh_4, Sh_4}_H coeff
        # {Sh_4, Sh_4} = (4*S4*x^3)*(3/c)*(4*S4*x^3) = 48*S4^2/c * x^6
        # o^(6) = 1/2 * 48*S4^2/c = 24*S4^2/c
        # S_6 = -(24*S4^2/c) / 12 = -2*S4^2/c
        S4 = S[4]
        S6_expected = -2 * S4 ** 2 / c
        assert simplify(S[6] - S6_expected) == 0

    def test_S8_from_S4_S6(self):
        """S_8 is determined by {S_4, S_6}_H."""
        S = compute_wline_tower(8)
        S4, S6 = S[4], S[6]
        # {Sh_4, Sh_6}: (4*S4*x^3)*(3/c)*(6*S6*x^5) = 72*S4*S6/c * x^8
        # o^(8) = 72*S4*S6/c (j=4,k=6, j!=k)
        # S_8 = -(72*S4*S6/c) / 16 = -9*S4*S6/(2c)
        S8_expected = -9 * S4 * S6 / (2 * c)
        assert simplify(S[8] - S8_expected) == 0

    def test_single_generator(self):
        """On the W-line, S_4 is the SOLE generator (S_2 = kappa is inert, S_3 = 0).
        All even arities >= 6 are ring products involving S_4."""
        S = compute_wline_tower(12)
        # S_6 = -2*S4^2/c (from (4,4))
        # S_8 = -9*S4*S6/(2c) = -9*S4*(-2*S4^2/c)/(2c) = 9*S4^3/c^2
        S4 = S[4]
        S6_check = simplify(S[6] - (-2 * S4 ** 2 / c))
        S8_check = simplify(S[8] - (9 * S4 ** 3 / c ** 2))
        assert S6_check == 0, f"S6 mismatch: {S6_check}"
        assert S8_check == 0, f"S8 mismatch: {S8_check}"


# ===========================================================================
# Sigma-ring finite generation on W-line
# ===========================================================================

class TestSigmaRingWline:
    def test_delta_from_products(self):
        """Delta^(6) on W-line should equal the sigma-invariant of the ring product."""
        S = compute_wline_tower(6)
        S4 = S[4]

        # Direct sigma-invariant
        delta6_direct = sigma_invariant(S[6], 100)

        # From ring product: S_6 = -2*S4^2/c at c, and at c'=100-c:
        # S_6(c') = -2*S4(c')^2/c'
        # Delta_6 = S_6(c) + S_6(c') = -2S4(c)^2/c - 2S4(100-c)^2/(100-c)
        S4_dual = S4.subs(c, 100 - c)
        delta6_products = cancel(-2 * S4 ** 2 / c + (-2) * S4_dual ** 2 / (100 - c))

        assert simplify(delta6_direct - delta6_products) == 0
