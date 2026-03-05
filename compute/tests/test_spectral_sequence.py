"""Tests for spectral sequence computations.

Ground truth from prop:virasoro-koszul-acyclic, prop:E8-koszul-acyclic,
comp:virasoro-dim-table.
"""

import pytest

from compute.lib.spectral_sequence import (
    VIRASORO_BAR_COH,
    HEISENBERG_BAR_COH,
    SL2_BAR_COH,
    spectral_sequence_collapse,
    e2_page_virasoro,
    e2_page_heisenberg,
    e2_page_sl2,
    catalan,
    associahedron_f_vector,
    check_koszul_property,
    verify_spectral_sequences,
)


class TestVirasoroBarCoh:
    def test_first_dims(self):
        assert VIRASORO_BAR_COH[1] == 1
        assert VIRASORO_BAR_COH[2] == 2
        assert VIRASORO_BAR_COH[3] == 5

    def test_dim_5(self):
        assert VIRASORO_BAR_COH[5] == 30

    def test_dim_10(self):
        assert VIRASORO_BAR_COH[10] == 3610

    def test_e2_page(self):
        page = e2_page_virasoro(5)
        assert page == {1: 1, 2: 2, 3: 5, 4: 12, 5: 30}


class TestHeisenbergBarCoh:
    def test_all_one(self):
        for n in range(1, 11):
            assert HEISENBERG_BAR_COH[n] == 1

    def test_e2_page(self):
        page = e2_page_heisenberg(5)
        assert all(d == 1 for d in page.values())


class TestSl2BarCoh:
    def test_first_dims(self):
        assert SL2_BAR_COH[1] == 3
        assert SL2_BAR_COH[2] == 8
        assert SL2_BAR_COH[3] == 27


class TestCollapsePages:
    def test_kac_moody_E1(self):
        for alg in ["sl2", "sl3", "E8"]:
            data = spectral_sequence_collapse(alg)
            assert data["collapse_page"] == 1, f"{alg} should collapse at E_1"

    def test_heisenberg_E1(self):
        assert spectral_sequence_collapse("Heisenberg")["collapse_page"] == 1

    def test_virasoro_E2(self):
        assert spectral_sequence_collapse("Virasoro")["collapse_page"] == 2

    def test_betagamma_E2(self):
        assert spectral_sequence_collapse("betagamma")["collapse_page"] == 2

    def test_bc_E2(self):
        assert spectral_sequence_collapse("bc")["collapse_page"] == 2


class TestCatalan:
    def test_values(self):
        assert catalan(1) == 1
        assert catalan(2) == 2
        assert catalan(3) == 5
        assert catalan(4) == 14
        assert catalan(5) == 42


class TestAssociahedron:
    def test_K2(self):
        assert associahedron_f_vector(2) == [1]

    def test_K3(self):
        assert associahedron_f_vector(3) == [2, 1]

    def test_K4_pentagon(self):
        """K_4 = pentagon: 5 vertices, 5 edges, 1 face."""
        assert associahedron_f_vector(4) == [5, 5, 1]


class TestKoszulProperty:
    def test_consistent(self):
        # Trivial check: bar coh matches itself
        assert check_koszul_property(VIRASORO_BAR_COH, VIRASORO_BAR_COH)

    def test_inconsistent(self):
        wrong = {1: 1, 2: 3}  # dim H^2 should be 2
        assert not check_koszul_property(VIRASORO_BAR_COH, wrong)


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_spectral_sequences().items():
            assert ok, f"Failed: {name}"
