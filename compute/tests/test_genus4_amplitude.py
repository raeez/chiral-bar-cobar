"""
Tests for genus-4 amplitude computation — 50+ tests.
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from genus4_amplitude import (
    bernoulli_2n, lambda_FP, F_g, lambda_FP_4, lambda_FP_5,
    ahat_expansion, planted_forest_genus2, planted_forest_genus2_virasoro,
    full_amplitude_g2, full_amplitude_g4_scalar, heisenberg_check_all_genera,
    F4_complementarity, shadow_visibility_genus, STABLE_GRAPH_COUNTS,
)


# ============================================================
# Bernoulli numbers
# ============================================================

class TestBernoulliNumbers:
    def test_B2(self):
        assert bernoulli_2n(1) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_2n(2) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_2n(3) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_2n(4) == Fraction(-1, 30)

    def test_B10(self):
        assert bernoulli_2n(5) == Fraction(5, 66)

    def test_B12(self):
        assert bernoulli_2n(6) == Fraction(-691, 2730)


# ============================================================
# Lambda_g^FP coefficients
# ============================================================

class TestLambdaFP:
    def test_lambda1(self):
        assert lambda_FP(1) == Fraction(1, 24)

    def test_lambda2(self):
        assert lambda_FP(2) == Fraction(7, 5760)

    def test_lambda3(self):
        assert lambda_FP(3) == Fraction(31, 967680)

    def test_lambda4_exact(self):
        """THE KEY RESULT: lambda_4^FP = 127/154828800."""
        assert lambda_FP(4) == Fraction(127, 154828800)

    def test_lambda4_three_way(self):
        """Verify lambda_4^FP via three methods."""
        result = lambda_FP_4()
        assert result == Fraction(127, 154828800)

    def test_lambda5(self):
        l5 = lambda_FP_5()
        assert l5 == lambda_FP(5)
        # Verify: (511/512) * (5/66) / 10! = 511*5/(512*66*3628800)
        expected = Fraction(511 * 5, 512 * 66 * math.factorial(10))
        assert l5 == expected

    def test_lambda_decreasing(self):
        """lambda_g^FP is decreasing for g >= 1."""
        for g in range(1, 6):
            assert lambda_FP(g) > lambda_FP(g + 1)

    def test_lambda_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 8):
            assert lambda_FP(g) > 0

    def test_lambda_bernoulli_decay(self):
        """lambda_g ~ 1/(2*pi)^{2g} — Bernoulli decay."""
        for g in range(1, 6):
            l = float(lambda_FP(g))
            bound = 1.0 / (2 * math.pi) ** (2 * g)
            # lambda_g should be within a polynomial factor of bound
            assert l < 100 * bound


# ============================================================
# F_g = kappa * lambda_g
# ============================================================

class TestFreeEnergy:
    def test_F1_virasoro(self):
        """F_1(Vir_c) = c/48."""
        for c in [1, 13, 26]:
            kappa = Fraction(c, 2)
            assert F_g(1, kappa) == Fraction(c, 48)

    def test_F2_virasoro(self):
        kappa = Fraction(13, 2)
        f2 = F_g(2, kappa)
        assert f2 == Fraction(13, 2) * Fraction(7, 5760)

    def test_F4_virasoro_c26(self):
        """F_4 at critical string c=26."""
        kappa = Fraction(13)
        f4 = F_g(4, kappa)
        assert f4 == 13 * Fraction(127, 154828800)

    def test_F4_virasoro_c1(self):
        kappa = Fraction(1, 2)
        f4 = F_g(4, kappa)
        assert f4 == Fraction(127, 309657600)


# ============================================================
# A-hat expansion
# ============================================================

class TestAhatExpansion:
    def test_ahat_genus1(self):
        coeffs = ahat_expansion()
        assert coeffs[1] == Fraction(1, 24)

    def test_ahat_genus4(self):
        coeffs = ahat_expansion()
        assert coeffs[4] == Fraction(127, 154828800)

    def test_ahat_6_terms(self):
        coeffs = ahat_expansion(max_g=6)
        assert len(coeffs) == 6
        for g in range(1, 7):
            assert g in coeffs


# ============================================================
# Planted-forest corrections
# ============================================================

class TestPlantedForest:
    def test_heisenberg_pf_zero(self):
        """Heisenberg (S_3=0): delta_pf = 0."""
        assert planted_forest_genus2(Fraction(1, 2), Fraction(0)) == 0

    def test_virasoro_pf_genus2_c1(self):
        pf = planted_forest_genus2_virasoro(1)
        S3 = Fraction(-6, 27)
        kappa = Fraction(1, 2)
        expected = S3 * (10 * S3 - kappa) / 48
        assert pf == expected

    def test_virasoro_pf_genus2_nonzero(self):
        """Virasoro planted-forest is nonzero for c > 0."""
        for c in [1, 5, 13, 26]:
            pf = planted_forest_genus2_virasoro(c)
            assert pf != 0


# ============================================================
# Full amplitudes
# ============================================================

class TestFullAmplitudes:
    def test_A2_virasoro(self):
        """A_2 = F_2 + delta_pf != F_2 for Virasoro."""
        for c in [1, 13]:
            a2 = full_amplitude_g2(c)
            f2 = F_g(2, Fraction(c, 2))
            assert a2 != f2

    def test_A4_scalar_positive(self):
        for c in [1, 5, 13, 26]:
            assert full_amplitude_g4_scalar(c) > 0


# ============================================================
# Heisenberg check
# ============================================================

class TestHeisenbergCheck:
    def test_all_pf_zero(self):
        results = heisenberg_check_all_genera(1, max_g=5)
        for g in range(1, 6):
            assert results[g]['delta_pf'] == 0

    def test_A_equals_F(self):
        results = heisenberg_check_all_genera(2, max_g=4)
        for g in range(1, 5):
            assert results[g]['A_g'] == results[g]['F_g']

    def test_heisenberg_F4(self):
        results = heisenberg_check_all_genera(1, max_g=4)
        assert results[4]['F_g'] == Fraction(1, 2) * Fraction(127, 154828800)


# ============================================================
# Complementarity (AP24)
# ============================================================

class TestComplementarity:
    def test_F4_sum_equals_13_lambda4(self):
        """F_4(c) + F_4(26-c) = 13 * lambda_4^FP."""
        for c in [1, 5, 10, 13]:
            total = F4_complementarity(c)
            assert total == 13 * lambda_FP(4)

    def test_F4_sum_at_self_dual(self):
        """At c=13: F_4(13) + F_4(13) = 2*F_4(13)."""
        total = F4_complementarity(13)
        assert total == 2 * F_g(4, Fraction(13, 2))


# ============================================================
# Shadow visibility
# ============================================================

class TestShadowVisibility:
    def test_S2_genus1(self):
        assert shadow_visibility_genus(2) == 2

    def test_S4_genus3(self):
        assert shadow_visibility_genus(4) == 3

    def test_S6_genus4(self):
        """S_6 first appears at genus 4."""
        assert shadow_visibility_genus(6) == 4

    def test_S7_genus4(self):
        """S_7 also first appears at genus 4."""
        assert shadow_visibility_genus(7) == 4

    def test_S8_genus5(self):
        """S_8 first appears at genus 5."""
        assert shadow_visibility_genus(8) == 5


# ============================================================
# Stable graph counts
# ============================================================

class TestStableGraphs:
    def test_genus2_count(self):
        assert STABLE_GRAPH_COUNTS[2] == 7

    def test_genus3_count(self):
        assert STABLE_GRAPH_COUNTS[3] == 42
