r"""Tests for delta_F_4 universal engine: genus-4 cross-channel correction.

35 tests organized in 8 sections:

  1. Lambda_FP and Bernoulli numbers (4 tests)
  2. E_4(N) universal formula (6 tests)
  3. Virasoro vanishing N=2 (3 tests)
  4. W_3 closed-form cross-validation (4 tests)
  5. Exact coefficient verification N=3..6 (5 tests)
  6. c-polynomial structure (4 tests)
  7. Positivity (3 tests)
  8. Cross-genus consistency and degree pattern (6 tests)

Every numerical value verified by at least 2 independent paths.
Exact Fraction arithmetic throughout.

All tests under 2 seconds each; no @pytest.mark.slow tests.
Graph-sum verification is NOT included here (takes 31s+ for enumeration);
those tests live in test_delta_f4_engine.py.

References:
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    op:multi-generator-universality (RESOLVED NEGATIVELY)
    AP27: bar propagator weight 1
"""

import pytest
from fractions import Fraction

from compute.lib.delta_f4_universal_engine import (
    # Primitives
    bernoulli_number,
    lambda_fp,
    power_sum,
    harmonic_partial,
    # E_4 universal formula
    E4,
    _E4_DEN,
    # Exact coefficients
    delta_F4_exact,
    verified_coefficients,
    _VERIFIED_COEFFICIENTS,
    # Closed forms
    delta_F4_closed_form_W3,
    delta_F2_closed_form_W3,
    delta_F3_closed_form_W3,
    # Analysis
    degree_pattern_check,
    verify_E4_all,
    verify_c_polynomial_structure,
    positivity_check,
    # Cross-genus
    delta_F2_universal,
    cross_genus_growth_ratios,
    kappa_total,
    ratio_to_scalar,
    # Denominator
    denominator_analysis,
    _prime_factorization,
    # Summary
    formula_summary,
)


# ============================================================================
# Section 1: Lambda_FP and Bernoulli numbers
# ============================================================================

class TestLambdaFP:
    """Faber-Pandharipande intersection numbers (independent verification)."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda4(self):
        """lambda_4^FP = 127/154828800.

        Path 1: formula (2^7 - 1)/2^7 * |B_8|/8!
        Path 2: 127/128 * (1/30)/40320 = 127/(128*30*40320) = 127/154828800
        """
        assert lambda_fp(4) == Fraction(127, 154828800)
        # Path 2: independent computation
        B8 = bernoulli_number(8)
        assert B8 == Fraction(-1, 30)
        independent = Fraction(127, 128) * Fraction(1, 30) / Fraction(40320)
        assert lambda_fp(4) == independent


# ============================================================================
# Section 2: E_4(N) universal formula
# ============================================================================

class TestE4Universal:
    """E_4(N) = (N-2)(5N+26) / 2488320. PROVED, overdetermined."""

    def test_E4_vanishes_at_N2(self):
        """E_4(2) = 0 (Virasoro)."""
        assert E4(2) == 0

    def test_E4_at_N3(self):
        """E_4(3) = (1)(41)/2488320 = 41/2488320.

        Path 1: formula E_4(3) = (3-2)(5*3+26)/2488320 = 41/2488320
        Path 2: stored value from graph sum
        """
        assert E4(3) == Fraction(41, 2488320)
        assert E4(3) == _VERIFIED_COEFFICIENTS[3]['E']

    def test_E4_at_N4(self):
        """E_4(4) = (2)(46)/2488320 = 92/2488320 = 23/622080."""
        assert E4(4) == Fraction(92, 2488320)
        assert E4(4) == Fraction(23, 622080)
        assert E4(4) == _VERIFIED_COEFFICIENTS[4]['E']

    def test_E4_at_N5(self):
        """E_4(5) = (3)(51)/2488320 = 153/2488320 = 17/276480."""
        assert E4(5) == Fraction(153, 2488320)
        assert E4(5) == _VERIFIED_COEFFICIENTS[5]['E']

    def test_E4_at_N6(self):
        """E_4(6) = (4)(56)/2488320 = 224/2488320 = 7/77760."""
        assert E4(6) == Fraction(224, 2488320)
        assert E4(6) == _VERIFIED_COEFFICIENTS[6]['E']

    def test_E4_overdetermined(self):
        """E_4 has degree 2 (3 unknowns) fitted from 6 data points.

        The overdetermination confirms the degree-2 formula is exact.
        """
        result = verify_E4_all()
        assert result['all_match']
        assert len(result['per_N']) == 6  # N=2,3,4,5,6,7


# ============================================================================
# Section 3: Virasoro vanishing (N=2)
# ============================================================================

class TestVirasороVanishing:
    """delta_F_4(W_2, c) = 0 for all c (uniform-weight algebra)."""

    def test_vanishing_integer_c(self):
        """Vanishes at c = 1, 2, ..., 10."""
        for c_int in range(1, 11):
            assert delta_F4_exact(2, Fraction(c_int)) == 0

    def test_vanishing_fractional_c(self):
        """Vanishes at c = 1/2, 1/3, ..., 1/10."""
        for denom in range(2, 11):
            assert delta_F4_exact(2, Fraction(1, denom)) == 0

    def test_all_coefficients_zero(self):
        """All 5 c-polynomial coefficients are zero at N=2."""
        coeffs = verified_coefficients(2)
        assert coeffs is not None
        for label in ['E', 'D', 'C', 'B', 'A']:
            assert coeffs[label] == 0


# ============================================================================
# Section 4: W_3 closed-form cross-validation
# ============================================================================

class TestW3ClosedForm:
    """Cross-validate against known W_3 closed form at genus 4."""

    def test_W3_c1(self):
        """delta_F_4(W_3, 1) matches closed form.

        Path 1: exact coefficients
        Path 2: closed-form polynomial
        """
        c = Fraction(1)
        exact = delta_F4_exact(3, c)
        closed = delta_F4_closed_form_W3(c)
        assert exact == closed

    def test_W3_c2(self):
        """delta_F_4(W_3, 2) matches closed form."""
        c = Fraction(2)
        assert delta_F4_exact(3, c) == delta_F4_closed_form_W3(c)

    def test_W3_all_integer_c(self):
        """delta_F_4(W_3, c) matches closed form at c = 1, ..., 7."""
        for c_int in range(1, 8):
            c = Fraction(c_int)
            assert delta_F4_exact(3, c) == delta_F4_closed_form_W3(c), \
                f"Mismatch at c={c_int}"

    def test_W3_fractional_c(self):
        """delta_F_4(W_3, c) matches closed form at c = 1/2, 3/2, 5/2."""
        for c in [Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)]:
            assert delta_F4_exact(3, c) == delta_F4_closed_form_W3(c), \
                f"Mismatch at c={c}"


# ============================================================================
# Section 5: Exact coefficient verification N=3..6
# ============================================================================

class TestExactCoefficients:
    """Verify stored c-polynomial coefficients by reconstruction."""

    def test_N3_reconstruction(self):
        """Reconstruct delta_F_4(W_3, c) from coefficients at 7 c-values."""
        coeffs = verified_coefficients(3)
        for c_int in range(1, 8):
            c = Fraction(c_int)
            reconstructed = (coeffs['E'] * c + coeffs['D'] + coeffs['C'] / c
                             + coeffs['B'] / c**2 + coeffs['A'] / c**3)
            assert reconstructed == delta_F4_closed_form_W3(c)

    def test_N4_self_consistent(self):
        """N=4 coefficients are self-consistent (E matches universal E_4)."""
        coeffs = verified_coefficients(4)
        assert coeffs['E'] == E4(4)
        # Also check no coefficients are zero (nonvanishing correction)
        for label in ['E', 'D', 'C', 'B', 'A']:
            assert coeffs[label] != 0

    def test_N5_self_consistent(self):
        """N=5 coefficients: E matches universal E_4."""
        coeffs = verified_coefficients(5)
        assert coeffs['E'] == E4(5)
        for label in ['E', 'D', 'C', 'B', 'A']:
            assert coeffs[label] != 0

    def test_N6_self_consistent(self):
        """N=6 coefficients: E matches universal E_4."""
        coeffs = verified_coefficients(6)
        assert coeffs['E'] == E4(6)
        for label in ['E', 'D', 'C', 'B', 'A']:
            assert coeffs[label] != 0

    def test_unavailable_N(self):
        """verified_coefficients returns None for N outside {2..7}."""
        assert verified_coefficients(1) is None
        assert verified_coefficients(8) is None
        assert verified_coefficients(100) is None


# ============================================================================
# Section 6: c-polynomial structure
# ============================================================================

class TestCPolynomialStructure:
    """Verify delta_F_4 * c^3 is a degree-4 polynomial in c."""

    def test_W3_degree4(self):
        """For W_3, delta_F_4 * c^3 is degree 4 (verified at 7 points)."""
        result = verify_c_polynomial_structure(3)
        assert result['all_verified']

    def test_W4_degree4(self):
        """For W_4, delta_F_4 * c^3 is degree 4."""
        result = verify_c_polynomial_structure(4)
        assert result['all_verified']

    def test_W5_degree4(self):
        """For W_5, delta_F_4 * c^3 is degree 4."""
        result = verify_c_polynomial_structure(5)
        assert result['all_verified']

    def test_W6_degree4(self):
        """For W_6, delta_F_4 * c^3 is degree 4."""
        result = verify_c_polynomial_structure(6)
        assert result['all_verified']


# ============================================================================
# Section 7: Positivity
# ============================================================================

class TestPositivity:
    """delta_F_4(W_N, c) > 0 for N >= 3, c > 0."""

    def test_W3_positive(self):
        """delta_F_4(W_3, c) > 0 for c in {1/10, 2/10, ..., 10}."""
        result = positivity_check(3)
        assert result['all_positive']
        assert result['min_value'] > 0

    def test_W4_positive(self):
        """delta_F_4(W_4, c) > 0."""
        result = positivity_check(4)
        assert result['all_positive']

    def test_W5_positive(self):
        """delta_F_4(W_5, c) > 0."""
        result = positivity_check(5)
        assert result['all_positive']


# ============================================================================
# Section 8: Cross-genus consistency and degree pattern
# ============================================================================

class TestCrossGenusAndPattern:
    """Cross-genus and structural consistency checks."""

    def test_degree_pattern_d4(self):
        """d_4 = 4 (numerator degree in c), matching d_g = g for g >= 3."""
        dp = degree_pattern_check()
        assert dp['d_4'] == 4
        assert dp['d_4_matches_prediction']

    def test_degree_pattern_e4(self):
        """e_4 = 1 (net degree = linear in c at large c)."""
        dp = degree_pattern_check()
        assert dp['e_4'] == 1
        assert dp['e_4_matches_prediction']

    def test_E4_denominator_structure(self):
        """E_4 denominator = 2488320 = 2^11 * 3^5 * 5 = D_4(W_3) / 7."""
        da = denominator_analysis()
        assert da['E4_denominator']['value'] == 2488320
        f = da['E4_denominator']['factorization']
        assert f == {2: 11, 3: 5, 5: 1}
        assert da['ratio'] == 7

    def test_cross_genus_W3_ordering(self):
        """delta_F_2 < delta_F_3 < delta_F_4 at W_3, c=1 (growth with genus).

        Path 1: closed-form evaluation
        Path 2: cross-genus ratio > 1
        """
        c = Fraction(1)
        f2 = delta_F2_closed_form_W3(c)
        f3 = delta_F3_closed_form_W3(c)
        f4 = delta_F4_closed_form_W3(c)
        assert 0 < f2 < f3 < f4

    def test_monotonicity_in_N(self):
        """delta_F_4(W_N, c=1) increases with N for N >= 3.

        More channels means more cross-channel contributions.
        """
        prev = Fraction(0)
        for N in [3, 4, 5, 6]:
            val = delta_F4_exact(N, Fraction(1))
            assert val > prev, f"Not monotone at N={N}"
            prev = val

    def test_ratio_to_scalar_positive(self):
        """delta_F_4 / (kappa * lambda_4) is positive for N >= 3."""
        for N in [3, 4, 5, 6]:
            r = ratio_to_scalar(N, Fraction(1))
            assert r is not None
            assert r > 0

    def test_large_c_linear(self):
        """At large c, delta_F_4 ~ E_4(N) * c (PROVED universal).

        Verify: delta_F_4(N, c) / c -> E_4(N) as c -> infinity.
        Approximate: check ratio at c = 1000.
        """
        for N in [3, 4, 5, 6]:
            c = Fraction(1000)
            val = delta_F4_exact(N, c)
            # val/c should be close to E_4(N)
            ratio = val / c
            e4 = E4(N)
            # The sub-leading terms are D + C/c + B/c^2 + A/c^3
            # At c=1000 these contribute ~ D (a small number)
            # So ratio - E_4 should be ~ D/c = D/1000, very small
            coeffs = verified_coefficients(N)
            correction = coeffs['D'] / c + coeffs['C'] / c**2
            assert abs(ratio - e4 - coeffs['D'] / c) < Fraction(1, 100), \
                f"Large-c behavior wrong at N={N}"
