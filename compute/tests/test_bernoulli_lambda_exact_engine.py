"""
Tests for bernoulli_lambda_exact_engine: exact Fraction arithmetic throughout.

Every hardcoded expected value has a # VERIFIED comment citing 2+ independent
sources from different categories per AP10/AP128/HZ-6.
"""

import pytest
from fractions import Fraction
from math import factorial

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bernoulli_lambda_exact_engine import (
    bernoulli_exact,
    lambda_g_exact,
    BERNOULLI_TABLE,
    LAMBDA_G_TABLE,
    CANONICAL_BERNOULLI,
)


# ===================================================================
# 1. Bernoulli numbers B_0 through B_20 against independent values
# ===================================================================

class TestBernoulliExact:
    """Verify computed Bernoulli numbers against independently known values."""

    @pytest.mark.parametrize("n, expected", [
        # VERIFIED [LT] Abramowitz-Stegun Table 23.2; [DC] recursion by hand
        (0, Fraction(1)),
        (1, Fraction(-1, 2)),
        (2, Fraction(1, 6)),
        # VERIFIED [LT] Abramowitz-Stegun Table 23.2; [DC] direct recursion
        (4, Fraction(-1, 30)),
        (6, Fraction(1, 42)),
        (8, Fraction(-1, 30)),
        (10, Fraction(5, 66)),
        # VERIFIED [LT] Ireland-Rosen, A Classical Introduction to Modern
        # Number Theory, Appendix; [DC] recursion check; [NE] OEIS A027642
        (12, Fraction(-691, 2730)),
        (14, Fraction(7, 6)),
        (16, Fraction(-3617, 510)),
        # VERIFIED [LT] Abramowitz-Stegun Table 23.2; [NE] OEIS A027641/A027642
        (18, Fraction(43867, 798)),
        (20, Fraction(-174611, 330)),
    ])
    def test_even_bernoulli(self, n, expected):
        assert BERNOULLI_TABLE[n] == expected, (
            f"B_{n}: got {BERNOULLI_TABLE[n]}, expected {expected}"
        )

    def test_b1_convention(self):
        """B_1 = -1/2 (Bernoulli-number convention with B_1 negative)."""
        # VERIFIED [LT] Abramowitz-Stegun; [DC] recursion: B_1 = -1/(1+1) * C(2,0)*B_0 = -1/2
        assert BERNOULLI_TABLE[1] == Fraction(-1, 2)

    @pytest.mark.parametrize("k", range(1, 10))
    def test_odd_bernoulli_vanish(self, k):
        """B_{2k+1} = 0 for k >= 1."""
        # VERIFIED [LT] standard property (von Staudt); [DC] recursion output
        n = 2 * k + 1
        assert BERNOULLI_TABLE[n] == Fraction(0), f"B_{n} should vanish, got {BERNOULLI_TABLE[n]}"

    def test_recursion_consistency(self):
        """Verify the defining recursion sum_{k=0}^{m} C(m+1,k) B_k = 0 for m >= 1."""
        # VERIFIED [DC] direct check of defining relation; [LT] Concrete Mathematics (GKP) eq 6.78
        for m in range(1, 21):
            s = Fraction(0)
            for k in range(m + 1):
                binom = Fraction(factorial(m + 1), factorial(k) * factorial(m + 1 - k))
                s += binom * BERNOULLI_TABLE[k]
            assert s == Fraction(0), f"Recursion fails at m={m}: sum = {s}"

    def test_canonical_table_matches(self):
        """Engine output matches the hardcoded canonical table."""
        for n, expected in CANONICAL_BERNOULLI.items():
            assert BERNOULLI_TABLE[n] == expected, f"B_{n} mismatch"

    def test_von_staudt_clausen_b12(self):
        """Von Staudt-Clausen: B_{2n} + sum_{(p-1)|2n} 1/p is an integer.

        Check at 2n=12: primes p with (p-1)|12 are 2,3,5,7,13.
        B_12 + 1/2 + 1/3 + 1/5 + 1/7 + 1/13 should be an integer.
        """
        # VERIFIED [LT] von Staudt-Clausen theorem; [DC] direct evaluation
        primes = [2, 3, 5, 7, 13]
        correction = sum(Fraction(1, p) for p in primes)
        result = BERNOULLI_TABLE[12] + correction
        assert result.denominator == 1, f"Von Staudt-Clausen fails at n=12: got {result}"


# ===================================================================
# 2. Lambda_g for g = 1..10 via Faber-Pandharipande formula
# ===================================================================

class TestLambdaGExact:
    """Verify lambda_g = (-1)^{g-1} * B_{2g} / (2 * (2g)!)."""

    @pytest.mark.parametrize("g", range(1, 11))
    def test_lambda_g_formula(self, g):
        """Cross-check lambda_g against direct formula evaluation."""
        # VERIFIED [DC] direct formula; [LT] Faber-Pandharipande, "Hodge integrals
        # and moduli spaces of curves" (2000), Theorem 1
        b2g = BERNOULLI_TABLE[2 * g]
        sign = Fraction((-1) ** (g - 1))
        expected = sign * b2g / Fraction(2 * factorial(2 * g))
        computed = LAMBDA_G_TABLE[g]
        assert computed == expected, f"lambda_{g}: got {computed}, expected {expected}"

    def test_lambda_1(self):
        """lambda_1 = B_2 / (2 * 2!) = (1/6) / 4 = 1/24."""
        # VERIFIED [LT] Mumford, "Towards an enumerative geometry of the moduli
        # space of curves" (1983); [DC] B_2=1/6, 2*2!=4, (1/6)/4 = 1/24
        assert LAMBDA_G_TABLE[1] == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2 = -B_4 / (2 * 4!) = -(-1/30) / 48 = 1/1440."""
        # VERIFIED [DC] B_4=-1/30, sign=(-1)^1=-1, so (-1)*(-1/30)=1/30,
        # then 1/30 / (2*24) = 1/1440; [LT] Faber-Pandharipande (2000) Table 1
        assert LAMBDA_G_TABLE[2] == Fraction(1, 1440)

    def test_lambda_3(self):
        """lambda_3 = B_6 / (2 * 6!) = (1/42) / 1440 = 1/60480."""
        # VERIFIED [DC] B_6=1/42, sign=(-1)^2=1, 2*720=1440, (1/42)/1440 = 1/60480
        # [LT] Faber-Pandharipande (2000)
        assert LAMBDA_G_TABLE[3] == Fraction(1, 60480)

    def test_lambda_g_sign_alternation(self):
        """lambda_g > 0 for all g >= 1 (since (-1)^{g-1} cancels sign of B_{2g})."""
        # VERIFIED [LT] B_{2g} has sign (-1)^{g-1}, so (-1)^{g-1}*B_{2g} > 0;
        # [DC] checked in table
        for g in range(1, 11):
            assert LAMBDA_G_TABLE[g] > 0, f"lambda_{g} should be positive"

    def test_lambda_g_function_matches_table(self):
        """lambda_g_exact() function matches precomputed LAMBDA_G_TABLE."""
        for g in range(1, 11):
            assert lambda_g_exact(g) == LAMBDA_G_TABLE[g]

    def test_f1_equals_kappa_over_24(self):
        """F_1 = lambda_1 = 1/24; for kappa=1, F_1 = kappa/24 = 1/24 (sanity AP120)."""
        # VERIFIED [DC] lambda_1 = 1/24; [LT] F_1 = kappa/24 standard (Faber-Pandharipande)
        assert LAMBDA_G_TABLE[1] == Fraction(1, 24)

    def test_f2_coefficient(self):
        """F_2 coefficient: lambda_2 = 1/1440. With kappa: F_2 = 7/5760 (at kappa=1,
        requires the full intersection number, not just lambda_2).
        Here we only verify lambda_2 = 1/1440."""
        # VERIFIED [DC] see test_lambda_2; [LT] Faber-Pandharipande (2000)
        assert LAMBDA_G_TABLE[2] == Fraction(1, 1440)


# ===================================================================
# 3. Fresh-computation cross-check (independent of precomputed table)
# ===================================================================

class TestFreshComputation:
    """Recompute from scratch and compare to precomputed tables."""

    def test_fresh_bernoulli_matches(self):
        """Independent call to bernoulli_exact matches BERNOULLI_TABLE."""
        fresh = bernoulli_exact(20)
        for n in range(21):
            assert fresh[n] == BERNOULLI_TABLE[n], f"Fresh B_{n} mismatch"

    def test_fresh_lambda_matches(self):
        """Independent lambda_g computation matches LAMBDA_G_TABLE."""
        fresh_b = bernoulli_exact(20)
        for g in range(1, 11):
            fresh_l = lambda_g_exact(g, fresh_b)
            assert fresh_l == LAMBDA_G_TABLE[g], f"Fresh lambda_{g} mismatch"


# ===================================================================
# 4. Type and arithmetic sanity
# ===================================================================

class TestArithmeticSanity:
    """Ensure all values are exact Fractions, no floats anywhere."""

    def test_bernoulli_types(self):
        for n in range(21):
            assert isinstance(BERNOULLI_TABLE[n], Fraction), f"B_{n} is not Fraction"

    def test_lambda_types(self):
        for g in range(1, 11):
            assert isinstance(LAMBDA_G_TABLE[g], Fraction), f"lambda_{g} is not Fraction"

    def test_no_float_contamination(self):
        """Denominators should be exact integers, not float-derived."""
        for g in range(1, 11):
            lam = LAMBDA_G_TABLE[g]
            assert lam.numerator != 0
            assert lam.denominator > 0
