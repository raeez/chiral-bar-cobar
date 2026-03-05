"""Tests for deformation quantization module."""

import pytest
from compute.lib.deformation_bar import (
    QUANTIZATION_LEVELS,
    QUANTIZATION_MAPS,
    pinf_vs_coisson,
    star_product_expansion,
    deformation_obstructions,
    deformation_examples,
    verify_deformation,
)


class TestQuantizationLevels:
    def test_three_levels(self):
        assert len(QUANTIZATION_LEVELS) == 3

    def test_classical_not_chiral(self):
        assert not QUANTIZATION_LEVELS["classical"]["is_chiral"]

    def test_singly_quantum_chiral(self):
        assert QUANTIZATION_LEVELS["singly_quantum"]["is_chiral"]

    def test_doubly_quantum_noncommutative(self):
        assert not QUANTIZATION_LEVELS["doubly_quantum"]["commutative"]


class TestPinfVsCoisson:
    def test_coisson_not_chiral(self):
        data = pinf_vs_coisson()
        assert not data["Coisson"]["is_chiral_algebra"]

    def test_pinf_is_chiral(self):
        data = pinf_vs_coisson()
        assert data["P_inf_chiral"]["is_chiral_algebra"]

    def test_coisson_no_ope(self):
        data = pinf_vs_coisson()
        assert not data["Coisson"]["has_ope"]

    def test_pinf_has_ope(self):
        data = pinf_vs_coisson()
        assert data["P_inf_chiral"]["has_ope"]

    def test_koszul_property(self):
        data = pinf_vs_coisson()
        assert "chirCom^! = chirLie" in data["P_inf_chiral"]["key_property"]


class TestStarProduct:
    def test_order0(self):
        sp = star_product_expansion(2)
        assert "commutative" in sp[0]

    def test_order1(self):
        sp = star_product_expansion(2)
        assert "Poisson" in sp[1]

    def test_order2(self):
        sp = star_product_expansion(2)
        assert "HH^3" in sp[2] or "second" in sp[2]


class TestObstructions:
    def test_first_order(self):
        obs = deformation_obstructions()
        assert "HH^2" in obs["first_order"]["lives_in"]

    def test_obstruction(self):
        obs = deformation_obstructions()
        assert "HH^3" in obs["obstruction"]["lives_in"]

    def test_curved(self):
        obs = deformation_obstructions()
        assert "center" in obs["curved"]["lives_in"] or "HH^0" in obs["curved"]["lives_in"]


class TestExamples:
    def test_heisenberg(self):
        ex = deformation_examples()
        assert "Heisenberg" in ex["Heisenberg_DQ"]["quantum"]

    def test_lattice(self):
        ex = deformation_examples()
        assert ex["lattice_DQ"]["obstruction_vanishes"]


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_deformation().items():
            assert ok, f"Failed: {name}"
