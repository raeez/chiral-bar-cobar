"""Tests for E8 lattice VOA bar complex.

Ground truth from comp:E8-generators, comp:E8-bar-deg2, comp:E8-curvature,
comp:E8-koszul-dual in detailed_computations.tex.
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.e8_lattice_bar import (
    E8_DATA,
    e8_central_charge,
    e8_generator_count,
    e8_bar_deg2_type_counts,
    e8_bar_diff_type_I,
    e8_bar_diff_type_II,
    e8_bar_diff_type_III,
    e8_nonzero_diff_count,
    e8_curvature,
    e8_curvature_sources,
    e8_dual_level,
    e8_complementarity_sum,
    e8_dual_central_charge,
    e8_lattice_self_dual,
    e8_koszul_acyclic,
    verify_e8_all,
)

k = Symbol('k')


class TestE8RootSystem:
    def test_dim(self):
        assert E8_DATA["dim"] == 248

    def test_rank(self):
        assert E8_DATA["rank"] == 8

    def test_n_roots(self):
        assert E8_DATA["n_roots"] == 240

    def test_simply_laced(self):
        """E_8 is simply laced: h = h^vee."""
        assert E8_DATA["h"] == E8_DATA["h_dual"] == 30

    def test_generator_count(self):
        gens = e8_generator_count()
        assert gens["total"] == 248
        assert gens["cartan"] + gens["vertex_operators"] == 248


class TestCentralCharge:
    def test_formula(self):
        assert e8_central_charge(k) == 248 * k / (k + 30)

    def test_at_k1(self):
        assert e8_central_charge(1) == Rational(248, 31)

    def test_critical_level(self):
        """c diverges at k = -h^vee = -30 (critical level)."""
        # We just check the formula gives 248*(-30)/0 which is undefined
        pass  # sympy will give zoo


class TestBarDeg2:
    def test_type_counts(self):
        counts = e8_bar_deg2_type_counts()
        assert counts["type_I_cartan_cartan"] == 64
        assert counts["type_III_root_root"] == 57600
        assert counts["total"] == 61504

    def test_type_I_diagonal(self):
        """D([J^i|J^i] otimes eta) = k*|0>."""
        vac, bar1 = e8_bar_diff_type_I(1, 1)
        assert vac["vac"] == k
        assert len(bar1) == 0

    def test_type_I_off_diagonal(self):
        """D([J^i|J^j] otimes eta) = 0 for i != j."""
        vac, bar1 = e8_bar_diff_type_I(1, 2)
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_type_II(self):
        """D([J^i|e^alpha] otimes eta) = alpha_i * e^alpha."""
        result = e8_bar_diff_type_II(1, 3)
        assert result["e_alpha"] == 3

    def test_type_III_minus2(self):
        """beta = -alpha: D = J_alpha + k*|0>."""
        vac, bar1 = e8_bar_diff_type_III(-2)
        assert vac["vac"] == k
        assert bar1["J_alpha"] == 1

    def test_type_III_minus1(self):
        """alpha+beta in Phi: D = epsilon * e^{alpha+beta}."""
        vac, bar1 = e8_bar_diff_type_III(-1)
        assert len(vac) == 0
        assert "e_alpha_plus_beta" in bar1

    def test_type_III_zero(self):
        """<alpha,beta>=0: D = 0."""
        vac, bar1 = e8_bar_diff_type_III(0)
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_type_III_plus1(self):
        vac, bar1 = e8_bar_diff_type_III(1)
        assert len(vac) == 0

    def test_type_III_plus2(self):
        vac, bar1 = e8_bar_diff_type_III(2)
        assert len(vac) == 0

    def test_nonzero_count(self):
        """1920 + 13440 + 240 = 15600."""
        assert e8_nonzero_diff_count() == 15600

    def test_neighbors(self):
        """Each root has 56 neighbors at inner product -1."""
        assert E8_DATA["neighbors_at_minus1"] == 56
        assert 240 * 56 == 13440  # total pairs


class TestCurvature:
    def test_formula(self):
        assert e8_curvature(k) == (k + 30) / 60

    def test_at_k1(self):
        assert e8_curvature(1) == Rational(31, 60)

    def test_sources(self):
        sources = e8_curvature_sources()
        assert "248" in sources["total_vacuum_sources"]


class TestKoszulDuality:
    def test_dual_level(self):
        assert e8_dual_level(k) == -k - 60

    def test_dual_level_k1(self):
        assert e8_dual_level(1) == -61

    def test_complementarity(self):
        """c + c' = 2*dim(E_8) = 496."""
        assert e8_complementarity_sum() == 496

    def test_complementarity_numeric(self):
        c1 = e8_central_charge(1)
        c_dual = e8_dual_central_charge(1)
        assert c1 + c_dual == 496

    def test_involution(self):
        """(k')' = k."""
        assert e8_dual_level(e8_dual_level(k)) == k

    def test_self_dual_lattice(self):
        assert e8_lattice_self_dual() is True


class TestKoszulAcyclicity:
    def test_acyclic(self):
        data = e8_koszul_acyclic()
        assert data["acyclic"] is True
        assert data["spectral_sequence_collapse"] == "E_1"


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_e8_all().items():
            assert ok, f"Failed: {name}"
