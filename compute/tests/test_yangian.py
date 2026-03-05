"""Tests for Yangian bar complex module."""

import pytest
from compute.lib.yangian_bar import (
    YANGIAN_DATA,
    yangian_generator_count,
    yangian_rtt_relation_count,
    e1_bar_structure,
    e1_bar_deg2_dim,
    yangian_koszulness_status,
    coulomb_branch_data,
    verify_yangian,
    yangian_bar_cohomology_conjectured,
    yangian_bar_kunneth_gl2,
    yangian_serre_correction,
    YANGIAN_BAR_COHOMOLOGY_KNOWN,
)


class TestGenerators:
    def test_sl2_level0(self):
        assert yangian_generator_count("sl2", 0) == 3

    def test_sl2_level1(self):
        assert yangian_generator_count("sl2", 1) == 6

    def test_sl2_level2(self):
        assert yangian_generator_count("sl2", 2) == 9

    def test_sl3_level0(self):
        assert yangian_generator_count("sl3", 0) == 8


class TestRTT:
    def test_sl2(self):
        assert yangian_rtt_relation_count("sl2") == 9

    def test_sl3(self):
        assert yangian_rtt_relation_count("sl3") == 64


class TestE1Structure:
    def test_operad(self):
        data = e1_bar_structure("sl2")
        assert "E_1" in data["operad"]

    def test_config_space(self):
        data = e1_bar_structure("sl2")
        assert data["config_space"] == "Conf_n(R)"

    def test_koszul_dual_sl2(self):
        data = e1_bar_structure("sl2")
        assert data["koszul_dual"] == "U_q(sl_2)"


class TestBarDeg2:
    def test_sl2(self):
        assert e1_bar_deg2_dim("sl2") == 9

    def test_sl3(self):
        assert e1_bar_deg2_dim("sl3") == 64


class TestKoszulness:
    def test_sl2_conjectured(self):
        status = yangian_koszulness_status("sl2")
        assert status["status"] == "conjectured"


class TestCoulomb:
    def test_sl2(self):
        data = coulomb_branch_data("sl2")
        assert "Coulomb" in data["geometry"]
        assert "Higgs" in data["koszul_dual"]


class TestChiralBarCohomology:
    """Tests for the conjectured chiral bar cohomology H^n = 3^n + 1."""

    def test_known_values(self):
        for n, expected in YANGIAN_BAR_COHOMOLOGY_KNOWN.items():
            assert yangian_bar_cohomology_conjectured(n) == expected

    def test_h0(self):
        assert yangian_bar_cohomology_conjectured(0) == 1

    def test_h4_prediction(self):
        assert yangian_bar_cohomology_conjectured(4) == 82

    def test_h5_prediction(self):
        assert yangian_bar_cohomology_conjectured(5) == 244

    def test_recurrence(self):
        """Verify a(n) = 4a(n-1) - 3a(n-2) for n >= 3."""
        for n in range(3, 10):
            a_n = yangian_bar_cohomology_conjectured(n)
            a_n1 = yangian_bar_cohomology_conjectured(n - 1)
            a_n2 = yangian_bar_cohomology_conjectured(n - 2)
            assert a_n == 4 * a_n1 - 3 * a_n2

    def test_kunneth_match_deg1(self):
        assert yangian_bar_kunneth_gl2(1) == 4

    def test_kunneth_match_deg2(self):
        assert yangian_bar_kunneth_gl2(2) == 10

    def test_kunneth_deviates_deg3(self):
        """gl_2 Kunneth gives 25, Yangian gives 28."""
        assert yangian_bar_kunneth_gl2(3) == 25
        assert yangian_bar_cohomology_conjectured(3) == 28

    def test_serre_correction_vanishes_low_degree(self):
        assert yangian_serre_correction(1) == 0
        assert yangian_serre_correction(2) == 0

    def test_serre_correction_deg3(self):
        assert yangian_serre_correction(3) == 3


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_yangian().items():
            assert ok, f"Failed: {name}"
