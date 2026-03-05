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


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_yangian().items():
            assert ok, f"Failed: {name}"
