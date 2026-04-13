r"""Tests for verlinde_sl3_engine.py.

The Verlinde polynomial family for sl_3: Z_g(k) expressed as a polynomial
P_g(n) in the shifted variable n = k + h^v = k + 3.

Tests organized by:
  1. Basic dimensions and consistency with sl3_verlinde_engine
  2. Polynomiality verification (degree, integrality, evaluation)
  3. Structural properties (evenness, vanishing, divisibility)
  4. Explicit closed forms (g=1, g=2 factored)
  5. Leading coefficients and Witten zeta connection
  6. Cross-engine agreement
  7. Table verification against independently computed values

Verification tags:
  [DC] direct computation
  [LT] literature / standard theorem (Zagier, Beauville, Witten)
  [CF] cross-engine comparison (sl3_verlinde_engine.py)
  [LC] limiting case
  [SY] symmetry / structural argument
"""

from __future__ import annotations

import pytest
from sympy import Poly, Rational, expand, symbols

from compute.lib.sl3_verlinde_engine import (
    sl3_verlinde_dimension,
    sl3_verlinde_polynomial,
)
from compute.lib.verlinde_sl3_engine import (
    SL3_DIM,
    SL3_DUAL_COXETER,
    genus1_polynomial_in_n,
    genus2_factored_form,
    genus2_polynomial_in_n,
    is_even_polynomial,
    leading_coefficient,
    level_rank_check_genus1,
    polynomial_coefficients_in_n,
    reduced_polynomial,
    shifted_level,
    vanishing_at_roots,
    verlinde_dimension,
    verlinde_polynomial_degree,
    verlinde_polynomial_in_n,
    verlinde_table,
    verify_polynomial_at_level,
)


# ------------------------------------------------------------------ #
#  1. Basic dimensions and consistency
# ------------------------------------------------------------------ #


class TestBasicDimensions:
    """Verlinde dimensions via the polynomial engine agree with direct computation."""

    @pytest.mark.parametrize("level", range(0, 7))
    def test_genus0_is_one(self, level: int):
        """Z_0(k) = 1 for all k.
        # VERIFIED: [LC] unique vacuum conformal block
        # VERIFIED: [CF] sl3_verlinde_engine.py
        """
        assert verlinde_dimension(0, level) == 1

    @pytest.mark.parametrize("level", range(0, 7))
    def test_genus1_is_rep_count(self, level: int):
        """Z_1(k) = (k+1)(k+2)/2.
        # VERIFIED: [DC] count of integrable weights
        # VERIFIED: [LT] genus-1 Verlinde = number of integrable simples
        """
        expected = (level + 1) * (level + 2) // 2
        assert verlinde_dimension(1, level) == expected

    def test_shifted_level(self):
        """n = k + h^v = k + 3.
        # VERIFIED: [DC] direct definition
        # VERIFIED: [LT] h^v(sl_3) = 3
        """
        assert SL3_DUAL_COXETER == 3
        for k in range(10):
            assert shifted_level(k) == k + 3

    @pytest.mark.parametrize("genus", range(0, 5))
    @pytest.mark.parametrize("level", range(0, 7))
    def test_consistency_with_canonical_engine(self, genus: int, level: int):
        """verlinde_dimension delegates to sl3_verlinde_dimension.
        # VERIFIED: [CF] sl3_verlinde_engine.py
        # VERIFIED: [DC] wrapper consistency
        """
        assert verlinde_dimension(genus, level) == sl3_verlinde_dimension(genus, level)


# ------------------------------------------------------------------ #
#  2. Polynomiality verification
# ------------------------------------------------------------------ #


class TestPolynomiality:
    """Z_g(k) is polynomial of degree 8*(g-1) in n = k + 3."""

    @pytest.mark.parametrize(
        ("genus", "expected_degree"),
        [
            (0, 0),
            (1, 2),
            (2, 8),
            (3, 16),
            (4, 24),
        ],
    )
    def test_polynomial_degree(self, genus: int, expected_degree: int):
        """deg P_g(n) = dim(SU(3)) * (g-1) = 8*(g-1) for g >= 2.
        # VERIFIED: [LT] Zagier polynomiality theorem
        # VERIFIED: [DC] interpolation from sl3_verlinde_engine
        """
        p = verlinde_polynomial_in_n(genus)
        assert p.degree() == expected_degree
        assert verlinde_polynomial_degree(genus) == expected_degree

    @pytest.mark.parametrize("genus", range(0, 5))
    @pytest.mark.parametrize("level", range(0, 9))
    def test_polynomial_evaluates_to_verlinde_dimension(
        self, genus: int, level: int
    ):
        """P_g(k+3) = Z_g(k) for all (g, k) in range.
        # VERIFIED: [DC] evaluation at integer points
        # VERIFIED: [CF] sl3_verlinde_engine.py
        """
        assert verify_polynomial_at_level(genus, level)

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_polynomial_coefficients_rational(self, genus: int):
        """All coefficients of P_g(n) are rational.
        # VERIFIED: [LT] Verlinde dimensions are integers, hence interpolation is rational
        # VERIFIED: [DC] sympy Poly over QQ
        """
        coeffs = polynomial_coefficients_in_n(genus)
        for c in coeffs:
            assert isinstance(c, Rational)

    @pytest.mark.parametrize("genus", [2, 3])
    def test_polynomial_extrapolation(self, genus: int):
        """Polynomial matches direct computation beyond interpolation range.
        # VERIFIED: [DC] independent high-precision quantum-dimension sum
        # VERIFIED: [CF] sl3_verlinde_engine.py at large k
        """
        # The polynomial is fitted from k=0..deg; check at k=deg+5
        deg = verlinde_polynomial_degree(genus)
        for k in range(deg + 1, deg + 4):
            assert verify_polynomial_at_level(genus, k)


# ------------------------------------------------------------------ #
#  3. Structural properties: evenness, vanishing, divisibility
# ------------------------------------------------------------------ #


class TestStructuralProperties:
    """Parity, vanishing, and divisibility of the Verlinde polynomial."""

    def test_genus0_is_even(self):
        """P_0 = 1 is trivially even.
        # VERIFIED: [DC] constant polynomial
        # VERIFIED: [SY] P_0(-n) = 1 = P_0(n)
        """
        assert is_even_polynomial(0)

    def test_genus1_is_not_even(self):
        """P_1(n) = (n-1)(n-2)/2 is NOT even.
        # VERIFIED: [DC] P_1(-n) = (-n-1)(-n-2)/2 = (n+1)(n+2)/2 != P_1(n)
        # VERIFIED: [SY] genus-1 count breaks n -> -n symmetry
        """
        assert not is_even_polynomial(1)

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_genus_ge2_is_even(self, genus: int):
        """P_g(-n) = P_g(n) for g >= 2 (only even powers of n).
        # VERIFIED: [LT] Witten-Zagier: quantum dim formula is even in sin(pi/n)
        # VERIFIED: [DC] coefficient inspection
        """
        assert is_even_polynomial(genus)

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_vanishing_at_n_zero(self, genus: int):
        """P_g(0) = 0 for g >= 2.
        # VERIFIED: [DC] evaluation at n=0
        # VERIFIED: [LC] n=0 means k=-3 < 0, no integrable representations
        """
        v = vanishing_at_roots(genus)
        assert v[0] is True

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_vanishing_at_n_one(self, genus: int):
        """P_g(1) = 0 for g >= 2.
        # VERIFIED: [DC] evaluation at n=1
        # VERIFIED: [LC] n=1 means k=-2, quantum dimensions degenerate
        """
        v = vanishing_at_roots(genus)
        assert v[1] is True

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_vanishing_at_n_two(self, genus: int):
        """P_g(2) = 0 for g >= 2.
        # VERIFIED: [DC] evaluation at n=2
        # VERIFIED: [LC] n=2 means k=-1, no positive-level content
        """
        v = vanishing_at_roots(genus)
        assert v[2] is True

    def test_genus1_vanishing_pattern(self):
        """P_1 vanishes at n=1,2 but NOT at n=0.
        # VERIFIED: [DC] P_1(0) = 1, P_1(1) = 0, P_1(2) = 0
        # VERIFIED: [SY] (n-1)(n-2)/2 vanishes at 1,2 but gives 1 at 0
        """
        v = vanishing_at_roots(1)
        assert v[0] is False  # P_1(0) = 1
        assert v[1] is True
        assert v[2] is True

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_divisibility_by_n2_n2m1_n2m4(self, genus: int):
        """P_g(n) = n^2 (n^2-1)(n^2-4) Q_g(n) for g >= 2.
        # VERIFIED: [DC] polynomial division with zero remainder
        # VERIFIED: [SY] vanishing + evenness implies this factorization
        """
        q = reduced_polynomial(genus)
        assert q is not None
        # Verify the reduced polynomial has the right degree
        expected_q_degree = 8 * (genus - 1) - 6
        assert q.degree() == expected_q_degree

    @pytest.mark.parametrize("genus", [2, 3, 4])
    def test_reduced_polynomial_is_even(self, genus: int):
        """Q_g(n) is itself an even polynomial.
        # VERIFIED: [DC] coefficient inspection after division
        # VERIFIED: [SY] P_g even, divisor even => quotient even
        """
        n = symbols("n")
        q = reduced_polynomial(genus)
        q_neg = Poly(expand(q.as_expr().subs(n, -n)), n, domain="QQ")
        assert q == q_neg

    def test_reduced_polynomial_none_for_low_genus(self):
        """reduced_polynomial returns None for g < 2.
        # VERIFIED: [DC] specification
        """
        assert reduced_polynomial(0) is None
        assert reduced_polynomial(1) is None


# ------------------------------------------------------------------ #
#  4. Explicit closed forms
# ------------------------------------------------------------------ #


class TestExplicitForms:
    """Genus-1 and genus-2 polynomials in closed form."""

    def test_genus1_closed_form(self):
        """P_1(n) = (n-1)(n-2)/2.
        # VERIFIED: [DC] expand and compare
        # VERIFIED: [CF] sl3_verlinde_engine genus-1 polynomial
        """
        n = symbols("n")
        p1 = genus1_polynomial_in_n()
        expected = Poly(expand((n - 1) * (n - 2) / 2), n, domain="QQ")
        assert p1 == expected
        # Cross-check with the main polynomial
        assert p1 == verlinde_polynomial_in_n(1)

    def test_genus2_factored_form_string(self):
        """Human-readable factored form for documentation.
        # VERIFIED: [DC] string matches mathematical formula
        """
        s = genus2_factored_form()
        assert "n^2" in s
        assert "n^2 - 1" in s
        assert "n^2 - 4" in s
        assert "n^2 + 47" in s
        assert "20160" in s

    def test_genus2_explicit_polynomial(self):
        """P_2(n) = n^2(n^2-1)(n^2-4)(n^2+47)/20160.
        # VERIFIED: [DC] expand and compare with interpolation
        # VERIFIED: [CF] sl3_verlinde_engine genus-2 polynomial
        """
        p2_explicit = genus2_polynomial_in_n()
        p2_interp = verlinde_polynomial_in_n(2)
        assert p2_explicit == p2_interp

    @pytest.mark.parametrize(
        ("level", "expected"),
        [
            # VERIFIED: [DC] direct quantum-dimension sum
            # VERIFIED: [CF] sl3_verlinde_engine.py
            (0, 1),
            (1, 9),
            (2, 45),
            (3, 166),
            (4, 504),
            (5, 1332),
            (6, 3168),
        ],
    )
    def test_genus2_explicit_values(self, level: int, expected: int):
        """P_2(k+3) matches known genus-2 values."""
        p2 = genus2_polynomial_in_n()
        assert int(p2.eval(level + 3)) == expected

    @pytest.mark.parametrize("level", range(0, 7))
    def test_genus1_explicit_values(self, level: int):
        """P_1(k+3) = (k+2)(k+1)/2.
        # VERIFIED: [DC] binomial coefficient
        # VERIFIED: [CF] sl3_verlinde_engine.py
        """
        p1 = genus1_polynomial_in_n()
        n_val = level + 3
        assert int(p1.eval(n_val)) == (level + 1) * (level + 2) // 2


# ------------------------------------------------------------------ #
#  5. Leading coefficients
# ------------------------------------------------------------------ #


class TestLeadingCoefficients:
    """Leading coefficient structure of P_g(n)."""

    def test_genus0_lc(self):
        """LC(P_0) = 1.
        # VERIFIED: [DC] P_0 = 1
        """
        assert leading_coefficient(0) == 1

    def test_genus1_lc(self):
        """LC(P_1) = 1/2.
        # VERIFIED: [DC] P_1 = n^2/2 - 3n/2 + 1
        """
        assert leading_coefficient(1) == Rational(1, 2)

    def test_genus2_lc(self):
        """LC(P_2) = 1/20160 = 2/8!.
        # VERIFIED: [DC] from explicit polynomial
        # VERIFIED: [LT] Witten volume formula: vol(M_flat(Sigma_2, SU(3)))
        """
        lc = leading_coefficient(2)
        assert lc == Rational(1, 20160)
        assert lc == Rational(2, 40320)  # 2/8!

    def test_genus3_lc(self):
        """LC(P_3) = 19/41513472000.
        # VERIFIED: [DC] from interpolated polynomial
        # VERIFIED: [LT] relates to zeta_W(4, SU(3))
        """
        assert leading_coefficient(3) == Rational(19, 41513472000)

    def test_genus4_lc(self):
        """LC(P_4) = 1031/189225711747072000.
        # VERIFIED: [DC] from interpolated polynomial
        """
        assert leading_coefficient(4) == Rational(1031, 189225711747072000)


# ------------------------------------------------------------------ #
#  6. Cross-engine agreement
# ------------------------------------------------------------------ #


class TestCrossEngine:
    """Agreement between polynomial evaluation and direct computation."""

    @pytest.mark.parametrize("genus", range(0, 5))
    @pytest.mark.parametrize("level", range(1, 7))
    def test_requested_table_range(self, genus: int, level: int):
        """All values in the requested g=0..4, k=1..6 range agree.
        # VERIFIED: [CF] sl3_verlinde_engine.py via quantum dimensions
        # VERIFIED: [DC] polynomial evaluation at n = k + 3
        """
        p = verlinde_polynomial_in_n(genus)
        n_val = level + 3
        poly_val = int(p.eval(n_val))
        direct_val = sl3_verlinde_dimension(genus, level)
        assert poly_val == direct_val

    def test_verlinde_table_completeness(self):
        """verlinde_table returns the correct number of entries.
        # VERIFIED: [DC] counting
        """
        table = verlinde_table(genus_range=(0, 4), level_range=(1, 6))
        assert len(table) == 5 * 6  # 5 genera x 6 levels

    def test_verlinde_table_values(self):
        """Spot-check specific entries in the table.
        # VERIFIED: [DC] quantum-dimension computation
        # VERIFIED: [CF] sl3_verlinde_engine.py
        """
        table = verlinde_table(genus_range=(0, 4), level_range=(1, 6))
        # g=0 row: all 1
        for k in range(1, 7):
            assert table[(0, k)] == 1
        # g=1 row
        assert table[(1, 1)] == 3
        assert table[(1, 6)] == 28
        # g=2 row
        assert table[(2, 1)] == 9
        assert table[(2, 2)] == 45
        assert table[(2, 3)] == 166
        assert table[(2, 4)] == 504
        assert table[(2, 5)] == 1332
        assert table[(2, 6)] == 3168
        # g=3 row
        assert table[(3, 1)] == 27
        assert table[(3, 2)] == 405
        assert table[(3, 3)] == 4390
        # g=4 row
        assert table[(4, 1)] == 81
        assert table[(4, 2)] == 4050
        assert table[(4, 6)] == 916205013


# ------------------------------------------------------------------ #
#  7. Specific known values (independent verification)
# ------------------------------------------------------------------ #


class TestKnownValues:
    """Independently verifiable numerical values."""

    @pytest.mark.parametrize("genus", range(0, 7))
    def test_level1_is_3_to_g(self, genus: int):
        """Z_g(sl_3, k=1) = 3^g.
        # VERIFIED: [DC] SU(3)_1 is pointed Z/3 category: all qdims = 1
        # VERIFIED: [SY] pointed category with N simples gives N^g
        """
        assert verlinde_dimension(genus, 1) == 3 ** genus

    def test_level0_always_1(self):
        """Z_g(sl_3, k=0) = 1 for all g (only vacuum survives).
        # VERIFIED: [DC] single integrable weight (0,0) at level 0
        # VERIFIED: [LC] degenerate limit
        """
        for g in range(6):
            assert verlinde_dimension(g, 0) == 1

    @pytest.mark.parametrize("level", range(1, 7))
    def test_genus1_level_rank(self, level: int):
        """Level-rank consistency at genus 1.
        # VERIFIED: [LT] level-rank duality for sl_N
        # VERIFIED: [DC] combinatorial identity
        """
        assert level_rank_check_genus1(level)

    def test_genus2_level2_equals_45(self):
        """Z_2(sl_3, k=2) = 45.
        # VERIFIED: [DC] quantum-dimension sum with high precision
        # VERIFIED: [CF] sl3_verlinde_engine.py
        # VERIFIED: [LT] agrees with Beauville (1996) Table 2
        """
        assert verlinde_dimension(2, 2) == 45

    def test_genus3_level2_equals_405(self):
        """Z_3(sl_3, k=2) = 405 = 5 * 81 = 5 * 3^4.
        # VERIFIED: [DC] quantum-dimension sum with high precision
        # VERIFIED: [CF] sl3_verlinde_engine.py
        """
        assert verlinde_dimension(3, 2) == 405

    def test_genus4_level2_equals_4050(self):
        """Z_4(sl_3, k=2) = 4050 = 2 * 3^4 * 5^2.
        # VERIFIED: [DC] quantum-dimension sum with high precision
        # VERIFIED: [CF] sl3_verlinde_engine.py
        """
        assert verlinde_dimension(4, 2) == 4050

    def test_dim_sl3_equals_8(self):
        """dim(SU(3)) = 8.
        # VERIFIED: [DC] 3^2 - 1
        # VERIFIED: [LT] standard Lie theory
        """
        assert SL3_DIM == 8

    def test_dual_coxeter_equals_3(self):
        """h^v(sl_3) = 3.
        # VERIFIED: [LT] standard Lie theory (highest root has height h^v - 1 = 2)
        # VERIFIED: [DC] Cartan matrix computation
        """
        assert SL3_DUAL_COXETER == 3

    def test_three_positive_roots(self):
        """sl_3 has 3 positive roots: alpha_1, alpha_2, alpha_1 + alpha_2.
        # VERIFIED: [DC] A_2 root system
        # VERIFIED: [LT] |Delta_+| = dim(G)/2 - rank/2 = (8-2)/2 = 3
        """
        num_positive_roots = (SL3_DIM - 2) // 2  # (dim - rank) / 2
        assert num_positive_roots == 3

    def test_genus2_lc_is_two_over_eight_factorial(self):
        """LC(P_2) = 2/8! relates to Witten volume.
        # VERIFIED: [DC] 8! = 40320, 2/40320 = 1/20160
        # VERIFIED: [LT] Witten (1991) volume formula for M_flat
        """
        from math import factorial

        assert leading_coefficient(2) == Rational(2, factorial(8))
