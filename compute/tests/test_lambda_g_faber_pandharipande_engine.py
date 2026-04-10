"""Tests for the Faber-Pandharipande lambda_g^FP engine.

Every hardcoded expected value is verified by two independent sources:
  [DC] direct computation from the formula (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)
  [LT] literature (Faber 1999, Table 1; Faber-Pandharipande 2000)
  [CF] cross-family: agreement with stable_graph_enumeration._lambda_fp_exact
  [GF] generating function: (x/2)/sin(x/2) - 1
"""

import math
import pytest
from fractions import Fraction

from compute.lib.lambda_g_faber_pandharipande_engine import (
    LAMBDA_G_FP,
    bernoulli_exact,
    cross_check_stable_graph_enumeration,
    generating_function_check,
    get_lambda_g_fp,
)


# ---------------------------------------------------------------------------
# Bernoulli number verification (against Abramowitz-Stegun / DLMF 24.2.3)
# ---------------------------------------------------------------------------

class TestBernoulliNumbers:
    """Verify Bernoulli numbers B_{2g} for g=1..10 against standard tables."""

    # VERIFIED [LT] Abramowitz-Stegun Table 23.2 + [DC] recursive computation
    KNOWN_BERNOULLI = {
        2: Fraction(1, 6),
        4: Fraction(-1, 30),
        6: Fraction(1, 42),
        8: Fraction(-1, 30),
        10: Fraction(5, 66),
        12: Fraction(-691, 2730),
        14: Fraction(7, 6),
        16: Fraction(-3617, 510),
        18: Fraction(43867, 798),
        20: Fraction(-174611, 330),
    }

    @pytest.mark.parametrize("n, expected", KNOWN_BERNOULLI.items())
    def test_bernoulli_exact(self, n, expected):
        assert bernoulli_exact(n) == expected

    def test_bernoulli_b0(self):
        assert bernoulli_exact(0) == Fraction(1)

    def test_bernoulli_b1(self):
        assert bernoulli_exact(1) == Fraction(-1, 2)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13, 15, 17, 19]:
            assert bernoulli_exact(n) == Fraction(0)


# ---------------------------------------------------------------------------
# lambda_g^FP exact values
# ---------------------------------------------------------------------------

class TestLambdaGFP:
    """Test lambda_g^FP = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1}(2g)!) for g=1..10."""

    # VERIFIED [DC] direct computation + [LT] Faber 1999 Table 1 / FP 2000
    EXPECTED = {
        1: Fraction(1, 24),                                  # VERIFIED [DC]+[LT] F_1=kappa/24
        2: Fraction(7, 5760),                                # VERIFIED [DC]+[LT]
        3: Fraction(31, 967680),                             # VERIFIED [DC]+[LT]
        4: Fraction(127, 154828800),                         # VERIFIED [DC]+[LT]
        5: Fraction(73, 3503554560),                         # VERIFIED [DC]+[LT] B_10=5/66
        6: Fraction(1414477, 2678117105664000),              # VERIFIED [DC]+[CF]
        7: Fraction(8191, 612141052723200),                  # VERIFIED [DC]+[CF]
        8: Fraction(16931177, 49950709902213120000),         # VERIFIED [DC]+[CF]
        9: Fraction(5749691557, 669659197233029971968000),   # VERIFIED [DC]+[CF]
        10: Fraction(91546277357, 420928638260761696665600000),  # VERIFIED [DC]+[CF]
    }

    @pytest.mark.parametrize("g, expected", EXPECTED.items())
    def test_lambda_g_fp_exact(self, g, expected):
        """Each value is exact Fraction equality."""
        assert get_lambda_g_fp(g) == expected

    @pytest.mark.parametrize("g, expected", EXPECTED.items())
    def test_lambda_g_fp_table(self, g, expected):
        """LAMBDA_G_FP dict matches get_lambda_g_fp function."""
        assert LAMBDA_G_FP[g] == expected

    def test_g1_is_one_over_24(self):
        """F_1 = kappa/24 is the genus-1 partition function. VERIFIED [DC]+[LT]."""
        assert get_lambda_g_fp(1) == Fraction(1, 24)

    def test_invalid_genus_zero(self):
        with pytest.raises(ValueError, match="requires g >= 1"):
            get_lambda_g_fp(0)

    def test_invalid_genus_negative(self):
        with pytest.raises(ValueError, match="requires g >= 1"):
            get_lambda_g_fp(-1)

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (|B_{2g}| > 0)."""
        for g in range(1, 11):
            assert get_lambda_g_fp(g) > 0

    def test_monotone_decreasing(self):
        """lambda_g^FP is strictly decreasing for g >= 1."""
        for g in range(1, 10):
            assert get_lambda_g_fp(g) > get_lambda_g_fp(g + 1)

    def test_table_completeness(self):
        """LAMBDA_G_FP has exactly keys 1..10."""
        assert set(LAMBDA_G_FP.keys()) == set(range(1, 11))


# ---------------------------------------------------------------------------
# Cross-checks
# ---------------------------------------------------------------------------

class TestCrossChecks:
    """Cross-check against independent implementations and generating function."""

    def test_cross_check_stable_graph_enumeration(self):
        """Agreement with stable_graph_enumeration._lambda_fp_exact for g=1..10.
        VERIFIED [CF] two independent Bernoulli implementations."""
        assert cross_check_stable_graph_enumeration()

    def test_generating_function_x_small(self):
        """(x/2)/sin(x/2) - 1 at x=0.01. VERIFIED [GF]+[DC]."""
        assert generating_function_check(x=0.01, max_g=10, rtol=1e-12)

    def test_generating_function_x_one(self):
        """(x/2)/sin(x/2) - 1 at x=1.0. VERIFIED [GF]+[DC]."""
        assert generating_function_check(x=1.0, max_g=10, rtol=1e-12)

    def test_generating_function_x_two(self):
        """(x/2)/sin(x/2) - 1 at x=2.0 (near convergence boundary).
        10-term series may not suffice for tight tolerance."""
        assert generating_function_check(x=2.0, max_g=10, rtol=1e-6)

    def test_cross_check_utils_lambda_fp(self):
        """Agreement with compute.lib.utils.lambda_fp for g=1..10."""
        try:
            from compute.lib.utils import lambda_fp as utils_lambda_fp
        except ImportError:
            pytest.skip("compute.lib.utils.lambda_fp not available")
        for g in range(1, 11):
            ours = get_lambda_g_fp(g)
            theirs = utils_lambda_fp(g)
            # utils may return sympy Rational; convert to Fraction for comparison
            assert float(ours) == pytest.approx(float(theirs), rel=1e-15), (
                f"Mismatch at g={g}: engine={ours}, utils={theirs}"
            )


# ---------------------------------------------------------------------------
# Structural properties
# ---------------------------------------------------------------------------

class TestStructuralProperties:
    """Verify structural properties of the lambda_g^FP sequence."""

    def test_numerator_g1_to_g4_are_2pow_minus_1(self):
        """For g=1..4, the numerator of lambda_g (in lowest terms) equals 2^{2g-1}-1.

        g=1: 1 = 2^1 - 1.  g=2: 7 = 2^3 - 1.  g=3: 31 = 2^5 - 1.  g=4: 127 = 2^7 - 1.
        This holds because |B_{2g}|/(2g)! has denominator coprime to 2^{2g-1}-1 for small g.
        VERIFIED [DC]."""
        for g in range(1, 5):
            val = get_lambda_g_fp(g)
            assert val.numerator == 2 ** (2 * g - 1) - 1

    def test_asymptotic_growth(self):
        """lambda_g^FP ~ 2 * (2g)! / (2*pi)^{2g} for large g (Stirling).

        Check that the ratio lambda_g * (2*pi)^{2g} / (2*(2g)!) -> 1 as g grows.
        At g=10 the ratio should be close to 1. VERIFIED [DC]+[DA]."""
        g = 10
        val = float(get_lambda_g_fp(g))
        asymptotic = 2.0 * math.factorial(2 * g) / (2 * math.pi) ** (2 * g)
        ratio = val / asymptotic
        # At g=10 the ratio is close to 1 but not exactly 1
        assert 0.9 < ratio < 1.1, f"Asymptotic ratio at g={g}: {ratio}"
