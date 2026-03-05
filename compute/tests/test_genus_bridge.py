"""Tests for genus expansion bridge."""

import pytest
from sympy import Rational, Symbol

from compute.lib.genus_bridge import (
    GENUS_KAPPA,
    COMPLEMENTARITY_KAPPA,
    kappa,
    mirzakhani_volume_growth,
    moduli_dimension,
    genus_universality_ratio,
    three_theorems_showcase,
    verify_genus_bridge,
)

k = Symbol('k')
c = Symbol('c')


class TestKappa:
    def test_heisenberg(self):
        assert kappa("Heisenberg", k) == k / 2

    def test_sl2(self):
        assert kappa("sl2", k) == Rational(3) * (k + 2) / 4

    def test_virasoro(self):
        assert kappa("Virasoro", c) == c / 2

    def test_w3(self):
        assert kappa("W3", c) == 5 * c / 6

    def test_e8(self):
        assert kappa("E8", k) == Rational(248) * (k + 30) / 60


class TestComplementarity:
    def test_sl2_vir(self):
        assert COMPLEMENTARITY_KAPPA["sl2_Virasoro"] == 26

    def test_sl3_w3(self):
        assert COMPLEMENTARITY_KAPPA["sl3_W3"] == 100

    def test_e8_km(self):
        assert COMPLEMENTARITY_KAPPA["E8_KM"] == 496


class TestModuli:
    def test_dim_g2(self):
        assert moduli_dimension(2) == 3

    def test_dim_g3(self):
        assert moduli_dimension(3) == 6

    def test_formula(self):
        for g in range(2, 10):
            assert moduli_dimension(g) == 3 * g - 3


class TestThreeTheorems:
    def test_sl2_showcase(self):
        data = three_theorems_showcase()
        assert data["sl2_to_Virasoro"]["complementarity_sum"] == 26

    def test_sl3_showcase(self):
        data = three_theorems_showcase()
        assert data["sl3_to_W3"]["complementarity_sum"] == 100


class TestMirzakhani:
    def test_growth(self):
        vol = mirzakhani_volume_growth(5)
        assert "(2*5)!" in vol
        assert "3628800" in vol  # 10! = 3628800


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_genus_bridge().items():
            assert ok, f"Failed: {name}"
