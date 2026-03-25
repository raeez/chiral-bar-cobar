"""Tests for compute/lib/curvature_genus_bridge.py.

Key result: the chain OPE -> m_0 -> kappa(A) -> F_g(A) = kappa * lambda_g
connects bar complex curvatures to genus expansions.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.curvature_genus_bridge import (
    curvature_to_kappa,
    verify_kappa_complementarity,
    curvature_vanishing,
    verify_curvature_genus_bridge,
    multi_generator_obstruction,
    dimensional_nilpotence_check,
    verify_multi_generator_obstruction,
)


class TestCurvatureToKappa:
    """Map from bar complex curvature to obstruction coefficient kappa."""

    def test_virasoro_kappa_equals_m0(self):
        """Vir: kappa = m_0 = c/2."""
        data = curvature_to_kappa()
        c = Symbol('c')
        assert data["Virasoro"]["kappa"] == c / 2
        assert data["Virasoro"]["curvature_m0"] == c / 2

    def test_w3_kappa_is_sum_of_channels(self):
        """W_3: kappa = m_0^T + m_0^W = c/2 + c/3 = 5c/6."""
        data = curvature_to_kappa()
        c = Symbol('c')
        m0 = data["W3"]["curvature_m0"]
        assert simplify(m0["T"] + m0["W"] - 5 * c / 6) == 0

    def test_sl2_kappa_formula(self):
        data = curvature_to_kappa()
        k = Symbol('k')
        assert simplify(data["sl2"]["kappa"] - 3 * (k + 2) / 4) == 0

    def test_sl3_kappa_formula(self):
        data = curvature_to_kappa()
        k = Symbol('k')
        assert simplify(data["sl3"]["kappa"] - 4 * (k + 3) / 3) == 0

    def test_pole_orders(self):
        """Pole orders: KM=2, Vir=4, W_3=6."""
        data = curvature_to_kappa()
        assert data["sl2"]["pole_order"] == 2
        assert data["Virasoro"]["pole_order"] == 4
        assert data["W3"]["pole_order"] == 6


class TestKappaComplementarity:
    """kappa(A) + kappa(A!) for Koszul pairs."""

    def test_all_complementarity_checks_pass(self):
        results = verify_kappa_complementarity()
        for name, ok in results.items():
            assert ok, f"Complementarity failed: {name}"

    def test_virasoro_sum_is_13(self):
        """Vir_c + Vir_{26-c}: kappa sum = 13."""
        results = verify_kappa_complementarity()
        assert results["Vir: kappa+kappa' = 13"]

    def test_km_antisymmetry(self):
        """KM: kappa(g_k) + kappa(g_{k'}) = 0 (Feigin-Frenkel: k' = -k - 2h^vee)."""
        results = verify_kappa_complementarity()
        assert results["sl2: kappa+kappa' = 0"]
        assert results["sl3: kappa+kappa' = 0"]

    def test_w3_sum(self):
        results = verify_kappa_complementarity()
        assert results["W3: kappa+kappa' = 250/3"]


class TestCurvatureVanishing:
    """Conditions under which m_0 = 0 (uncurved bar complex)."""

    def test_heisenberg_vanishes_at_kappa_0(self):
        data = curvature_vanishing()
        assert data["Heisenberg"]["condition"] == "kappa = 0"

    def test_virasoro_vanishes_at_c_0(self):
        data = curvature_vanishing()
        assert data["Virasoro"]["condition"] == "c = 0"

    def test_km_vanishes_at_k_0(self):
        data = curvature_vanishing()
        assert data["sl2"]["condition"] == "k = 0"


class TestCurvatureGenusBridge:
    """Full bridge verification: OPE pole -> curvature -> kappa -> genus."""

    def test_all_bridge_checks_pass(self):
        results = verify_curvature_genus_bridge()
        for name, ok in results.items():
            assert ok, f"Bridge check failed: {name}"


class TestDimensionalNilpotence:
    """Dimensional argument for (obs_g)^2 = 0."""

    def test_genus1_vanishes(self):
        check = dimensional_nilpotence_check(1)
        assert check["dimensional_vanishing"]

    def test_genus2_vanishes(self):
        check = dimensional_nilpotence_check(2)
        assert check["dimensional_vanishing"]

    def test_genus3_fails(self):
        """At g=3: obs^2 degree = 12 = max degree, dimensional argument fails."""
        check = dimensional_nilpotence_check(3)
        assert not check["dimensional_vanishing"]
        assert check["obs_squared_degree"] == check["max_degree"]

    def test_genus4_fails(self):
        check = dimensional_nilpotence_check(4)
        assert not check["dimensional_vanishing"]


class TestMultiGeneratorObstruction:
    """Multi-generator obstruction structure for W-algebras."""

    def test_w3_kappa_decomposition(self):
        results = verify_multi_generator_obstruction()
        assert results["W3: kappa_T + kappa_W = 5c/6"]

    def test_w4_sigma(self):
        """W_4: sigma = 1/2 + 1/3 + 1/4 = 13/12."""
        results = verify_multi_generator_obstruction()
        assert results["W4: sigma = 13/12"]

    def test_hodge_ranks_genus3(self):
        """Hodge bundle ranks at g=3: rank E_2 = 6, rank E_3 = 10."""
        results = verify_multi_generator_obstruction()
        assert results["g=3: rank E_2 = 6"]
        assert results["g=3: rank E_3 = 10"]

    def test_all_multi_generator_checks(self):
        results = verify_multi_generator_obstruction()
        for name, ok in results.items():
            assert ok, f"Multi-generator check failed: {name}"
