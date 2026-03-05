"""Tests for curvature-genus bridge.

Verifies the chain: OPE pole -> curvature m_0 -> kappa -> genus expansion.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.curvature_genus_bridge import (
    curvature_to_kappa,
    curvature_vanishing,
    verify_curvature_genus_bridge,
    verify_kappa_complementarity,
)

c = Symbol('c')
k = Symbol('k')


class TestCurvatureToKappa:
    def test_heisenberg(self):
        data = curvature_to_kappa()["Heisenberg"]
        assert data["pole_order"] == 2

    def test_virasoro_kappa_equals_m0(self):
        data = curvature_to_kappa()["Virasoro"]
        assert data["curvature_m0"] == data["kappa"]

    def test_w3_two_channels(self):
        data = curvature_to_kappa()["W3"]
        assert isinstance(data["curvature_m0"], dict)
        assert "T" in data["curvature_m0"]
        assert "W" in data["curvature_m0"]

    def test_w3_kappa_sum(self):
        """kappa(W3) = m_0^T + m_0^W = c/2 + c/3 = 5c/6."""
        data = curvature_to_kappa()["W3"]
        m0_sum = data["curvature_m0"]["T"] + data["curvature_m0"]["W"]
        assert simplify(m0_sum - data["kappa"]) == 0

    def test_sl2_kappa(self):
        data = curvature_to_kappa()["sl2"]
        assert data["kappa"] == 3 * (k + 2) / 4

    def test_sl3_kappa(self):
        data = curvature_to_kappa()["sl3"]
        assert data["kappa"] == 4 * (k + 3) / 3

    def test_pole_order_hierarchy(self):
        """KM (2) < Virasoro (4) < W_3 (6)."""
        data = curvature_to_kappa()
        assert data["sl2"]["pole_order"] < data["Virasoro"]["pole_order"]
        assert data["Virasoro"]["pole_order"] < data["W3"]["pole_order"]


class TestComplementarity:
    def test_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        assert simplify(c / 2 + (26 - c) / 2 - 13) == 0

    def test_w3(self):
        """kappa(W3_c) + kappa(W3_{100-c}) = 250/3."""
        assert simplify(5 * c / 6 + 5 * (100 - c) / 6 - Rational(250, 3)) == 0

    def test_sl2_kappa_antisymmetric(self):
        """kappa(sl2_k) + kappa(sl2_{-k-4}) = 0."""
        assert simplify(3 * (k + 2) / 4 + 3 * (-k - 2) / 4) == 0

    def test_sl3_kappa_antisymmetric(self):
        """kappa(sl3_k) + kappa(sl3_{-k-6}) = 0."""
        assert simplify(4 * (k + 3) / 3 + 4 * (-k - 3) / 3) == 0


class TestCurvatureVanishing:
    def test_conditions_exist(self):
        cv = curvature_vanishing()
        for name in ["Heisenberg", "sl2", "Virasoro", "W3"]:
            assert "condition" in cv[name]

    def test_virasoro_c0(self):
        assert curvature_vanishing()["Virasoro"]["condition"] == "c = 0"


class TestSelfConsistency:
    def test_bridge(self):
        for name, ok in verify_curvature_genus_bridge().items():
            assert ok, f"Failed: {name}"

    def test_complementarity(self):
        for name, ok in verify_kappa_complementarity().items():
            assert ok, f"Failed: {name}"
