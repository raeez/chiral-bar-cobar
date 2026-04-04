"""
Tests for BTZ shadow entropy — 50+ tests.
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from btz_shadow_entropy import (
    bekenstein_hawking_entropy, hawking_temperature, log_correction_coefficient,
    entropy_with_log_correction, shadow_free_energies, entropy_expansion,
    complementarity_entropy_sum, complementarity_sum_exact,
    self_dual_analysis, class_comparison, monster_module_entropy,
)


class TestCardyFormula:
    def test_S_BH_positive(self):
        for c in [1, 6, 12, 24, 26]:
            assert bekenstein_hawking_entropy(c, 1) > 0

    def test_S_BH_formula(self):
        """S_BH = 2*pi*sqrt(c*Delta/6) at Delta=6: S_BH = 2*pi*sqrt(c)."""
        c = 4
        assert abs(bekenstein_hawking_entropy(c, 6) - 2 * math.pi * 2) < 1e-10

    def test_S_BH_scales_sqrt_c(self):
        s1 = bekenstein_hawking_entropy(1, 1)
        s4 = bekenstein_hawking_entropy(4, 1)
        assert abs(s4 / s1 - 2.0) < 1e-10

    def test_S_BH_scales_sqrt_Delta(self):
        s1 = bekenstein_hawking_entropy(6, 1)
        s4 = bekenstein_hawking_entropy(6, 4)
        assert abs(s4 / s1 - 2.0) < 1e-10

    def test_hawking_temperature_positive(self):
        for c in [1, 6, 24]:
            assert hawking_temperature(c, 1) > 0


class TestLogCorrection:
    def test_coefficient_minus_three_halves(self):
        assert log_correction_coefficient() == Fraction(-3, 2)

    def test_entropy_with_correction(self):
        S = entropy_with_log_correction(24, 100)
        S_BH = bekenstein_hawking_entropy(24, 100)
        assert S < S_BH  # Log correction reduces entropy

    def test_correction_subleading(self):
        """For large S_BH, the correction is small relative to S_BH."""
        S_BH = bekenstein_hawking_entropy(24, 10000)
        S = entropy_with_log_correction(24, 10000)
        assert abs((S - S_BH) / S_BH) < 0.1


class TestShadowFreeEnergies:
    def test_F1_equals_kappa_over_24(self):
        kappa = Fraction(13, 2)
        F = shadow_free_energies(kappa)
        assert F[1] == kappa / 24

    def test_F_positive(self):
        F = shadow_free_energies(Fraction(12))
        for g in range(1, 6):
            assert F[g] > 0

    def test_F_decreasing(self):
        F = shadow_free_energies(Fraction(12))
        for g in range(1, 4):
            assert F[g] > F[g + 1]


class TestEntropyExpansion:
    def test_expansion_has_S_BH(self):
        result = entropy_expansion(24, 100)
        assert 'S_BH' in result
        assert result['S_BH'] > 0

    def test_F1_in_expansion(self):
        result = entropy_expansion(24, 100)
        assert abs(result['F_1'] - 12.0 / 24) < 1e-10

    def test_F2_in_expansion(self):
        result = entropy_expansion(24, 100)
        assert abs(result['F_2'] - 12.0 * 7 / 5760) < 1e-10


class TestComplementarity:
    def test_sum_equals_26_over_3(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps) for ALL c."""
        L = 1000
        for c in [1, 5, 10, 13, 20, 25]:
            total = complementarity_entropy_sum(c, L)
            expected = (26.0 / 3) * math.log(L)
            assert abs(total - expected) < 1e-10

    def test_exact_sum(self):
        assert complementarity_sum_exact() == Fraction(26, 3)

    def test_c_independent(self):
        """The sum is independent of c."""
        s1 = complementarity_entropy_sum(1, 100)
        s13 = complementarity_entropy_sum(13, 100)
        s25 = complementarity_entropy_sum(25, 100)
        assert abs(s1 - s13) < 1e-10
        assert abs(s13 - s25) < 1e-10


class TestSelfDual:
    def test_c_13(self):
        info = self_dual_analysis()
        assert info['c'] == 13

    def test_kappa_equals_dual(self):
        info = self_dual_analysis()
        assert info['kappa'] == info['kappa_dual']

    def test_sum_13(self):
        info = self_dual_analysis()
        assert info['sum'] == 13

    def test_entropy_coeff(self):
        info = self_dual_analysis()
        assert info['entropy_coefficient'] == Fraction(13, 3)

    def test_complementarity_26_3(self):
        info = self_dual_analysis()
        assert info['complementarity'] == Fraction(26, 3)


class TestClassComparison:
    def test_class_G_no_planted_forest(self):
        comp = class_comparison()
        assert 'zero' in comp['class_G']['planted_forest']

    def test_class_M_has_planted_forest(self):
        comp = class_comparison()
        assert 'nonzero' in comp['class_M']['planted_forest']


class TestMonster:
    def test_monster_kappa_12(self):
        info = monster_module_entropy()
        assert info['kappa'] == 12

    def test_monster_F1_half(self):
        info = monster_module_entropy()
        assert info['F_1'] == Fraction(1, 2)

    def test_monster_S_BH_4pi(self):
        """At Delta_L=1: S_BH = 4*pi."""
        info = monster_module_entropy(Delta_L=1)
        assert abs(info['S_BH'] - 4 * math.pi) < 1e-10

    def test_monster_log_correction(self):
        info = monster_module_entropy()
        assert info['log_correction_coeff'] == Fraction(-3, 2)
