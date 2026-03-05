"""Tests for cross-algebra integration.

Unified checks across all 11 algebras in the compute engine.
"""

import pytest

from compute.lib.cross_algebra import (
    ALGEBRA_REGISTRY,
    algebras_by_property,
    curved_algebras,
    uncurved_algebras,
    kac_moody_algebras,
    self_dual_algebras,
    koszul_dual_pairs,
    complementarity_table,
    pole_order_table,
    bar_degree_2_dim,
    curvature_sources,
    verify_cross_algebra,
)


class TestRegistry:
    def test_count(self):
        assert len(ALGEBRA_REGISTRY) == 11

    def test_all_have_generators(self):
        for name, data in ALGEBRA_REGISTRY.items():
            assert data["n_generators"] > 0, f"{name} missing generators"

    def test_all_have_pole_order(self):
        for name, data in ALGEBRA_REGISTRY.items():
            assert data["max_pole_order"] >= 0, f"{name} missing pole order"


class TestCurvedUncurved:
    def test_uncurved_list(self):
        uc = uncurved_algebras()
        assert "free_fermion" in uc
        assert "betagamma" in uc
        assert "bc" in uc

    def test_curved_list(self):
        c = curved_algebras()
        assert "Virasoro" in c
        assert "W3" in c
        assert "sl2" in c
        assert "E8" in c

    def test_partition(self):
        c = set(curved_algebras())
        uc = set(uncurved_algebras())
        assert len(c | uc) == 11
        assert len(c & uc) == 0


class TestKacMoody:
    def test_km_list(self):
        km = kac_moody_algebras()
        assert set(km) == {"Heisenberg", "sl2", "sl3", "E8", "B2", "G2"}

    def test_virasoro_not_km(self):
        assert "Virasoro" not in kac_moody_algebras()


class TestSelfDual:
    def test_km_self_dual(self):
        sd = self_dual_algebras()
        for a in ["sl2", "sl3", "E8", "B2", "G2"]:
            assert a in sd

    def test_heisenberg_not_self_dual(self):
        """CRITICAL: Heisenberg is NOT self-dual."""
        assert "Heisenberg" not in self_dual_algebras()

    def test_virasoro_not_self_dual(self):
        assert "Virasoro" not in self_dual_algebras()


class TestComplementarity:
    def test_virasoro(self):
        assert complementarity_table()["Virasoro"] == 26

    def test_w3(self):
        assert complementarity_table()["W3"] == 100

    def test_e8(self):
        assert complementarity_table()["E8"] == 496

    def test_km_2dim(self):
        """For KM: c + c' = 2*dim(g)."""
        ct = complementarity_table()
        for alg in ["sl2", "sl3", "E8", "B2", "G2"]:
            assert ct[alg] == 2 * ALGEBRA_REGISTRY[alg]["n_generators"]


class TestPoleOrders:
    def test_km_pole_2(self):
        pot = pole_order_table()
        for alg in ["Heisenberg", "sl2", "sl3", "E8", "B2", "G2"]:
            assert pot[alg] == 2

    def test_virasoro_pole_4(self):
        assert pole_order_table()["Virasoro"] == 4

    def test_w3_pole_6(self):
        assert pole_order_table()["W3"] == 6

    def test_fermion_pole_1(self):
        assert pole_order_table()["free_fermion"] == 1


class TestBarDeg2:
    def test_sl2(self):
        assert bar_degree_2_dim("sl2") == 9

    def test_e8(self):
        assert bar_degree_2_dim("E8") == 248**2

    def test_virasoro(self):
        assert bar_degree_2_dim("Virasoro") == 1


class TestKoszulPairs:
    def test_bg_bc(self):
        pairs = koszul_dual_pairs()
        names = [(a, b) for a, b in pairs]
        assert ("betagamma", "bc") in names or ("bc", "betagamma") in names


class TestSpectralCollapse:
    def test_km_E1(self):
        for alg in kac_moody_algebras():
            assert ALGEBRA_REGISTRY[alg]["spectral_collapse"] == 1

    def test_virasoro_E2(self):
        assert ALGEBRA_REGISTRY["Virasoro"]["spectral_collapse"] == 2

    def test_betagamma_E2(self):
        assert ALGEBRA_REGISTRY["betagamma"]["spectral_collapse"] == 2


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_cross_algebra().items():
            assert ok, f"Failed: {name}"
