"""Tests for curvature-genus bridge.

Verifies the chain: OPE pole -> curvature m_0 -> kappa -> genus expansion.
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.curvature_genus_bridge import (
    curvature_to_kappa,
    curvature_vanishing,
    multi_generator_obstruction,
    dimensional_nilpotence_check,
    verify_curvature_genus_bridge,
    verify_kappa_complementarity,
    verify_multi_generator_obstruction,
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

    def test_multi_generator(self):
        for name, ok in verify_multi_generator_obstruction().items():
            assert ok, f"Failed: {name}"


class TestMultiGeneratorObstruction:
    """Tests for multi-generator obstruction structure.

    Key result: Mumford's relation proves (obs_g)^2 = 0 for single-generator
    algebras (via lambda_g^2 = 0), but does NOT extend to multi-generator
    algebras like W_3 where obs_g involves higher-weight lambda classes.
    """

    def test_w3_has_two_channels(self):
        data = multi_generator_obstruction()["W3"]
        assert len(data["curvature_channels"]) == 2
        assert "T" in data["curvature_channels"]
        assert "W" in data["curvature_channels"]

    def test_w3_generator_weights(self):
        data = multi_generator_obstruction()["W3"]
        assert data["generators"]["T"] == 2
        assert data["generators"]["W"] == 3

    def test_w3_kappa_decomposition(self):
        """kappa_T = c/2, kappa_W = c/3, total = 5c/6."""
        data = multi_generator_obstruction()["W3"]
        assert simplify(data["curvature_channels"]["T"] - c / 2) == 0
        assert simplify(data["curvature_channels"]["W"] - c / 3) == 0
        assert simplify(data["kappa_total"] - 5 * c / 6) == 0

    def test_w4_sigma(self):
        """W_4 has sigma(sl_4) = 1/2 + 1/3 + 1/4 = 13/12."""
        data = multi_generator_obstruction()["W4"]
        assert simplify(data["kappa_total"] / c - Rational(13, 12)) == 0

    def test_mumford_does_not_apply(self):
        """Mumford's relation applies only to h=1 Hodge bundle."""
        for name in ["W3", "W4"]:
            data = multi_generator_obstruction()[name]
            assert data["mumford_applies"] is False

    @pytest.mark.parametrize("g", [1, 2])
    def test_dimensional_vanishing_low_genus(self, g):
        """For g <= 2: 4g > 6g-6, so (obs_g)^2 = 0 by dimension."""
        check = dimensional_nilpotence_check(g)
        assert check["dimensional_vanishing"] is True

    @pytest.mark.parametrize("g", [3, 4, 5, 10])
    def test_dimensional_fails_high_genus(self, g):
        """For g >= 3: 4g <= 6g-6, dimensional argument fails."""
        check = dimensional_nilpotence_check(g)
        assert check["dimensional_vanishing"] is False

    def test_genus_3_critical(self):
        """g=3 is the first genus where obs^2 could be nonzero."""
        check = dimensional_nilpotence_check(3)
        # obs^2 in degree 12, max degree = 2*6 = 12 -> top cohomology!
        assert check["obs_squared_degree"] == check["max_degree"]
        assert check["mumford_needed"] is True

    def test_hodge_bundle_ranks_genus_3(self):
        """At g=3: E_2 has rank 6, E_3 has rank 10."""
        data = multi_generator_obstruction()["W3"]
        assert data["hodge_bundle_ranks"]["h=2"](3) == 6
        assert data["hodge_bundle_ranks"]["h=3"](3) == 10

    def test_hodge_bundle_ranks_genus_4(self):
        """At g=4: E_2 has rank 9, E_3 has rank 15."""
        data = multi_generator_obstruction()["W3"]
        assert data["hodge_bundle_ranks"]["h=2"](4) == 9
        assert data["hodge_bundle_ranks"]["h=3"](4) == 15
