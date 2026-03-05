"""Tests for toroidal/elliptic bar complex."""

import pytest
from sympy import pi, Symbol

from compute.lib.toroidal_bar import (
    eisenstein_q_expansion,
    zeta_laurent_coefficients,
    elliptic_bar_diff_deg,
    elliptic_curvature,
    elliptic_vs_rational,
    bar_decomposition_by_weight,
    fay_d_squared_zero,
    verify_toroidal,
)


class TestEisenstein:
    def test_e2_coeffs(self):
        coeffs = eisenstein_q_expansion(2, 4)
        assert coeffs[0] == 1
        assert coeffs[1] == -24
        assert coeffs[2] == -72
        assert coeffs[3] == -96

    def test_e4_coeffs(self):
        coeffs = eisenstein_q_expansion(4, 3)
        assert coeffs[0] == 1
        assert coeffs[1] == 240

    def test_e6_coeffs(self):
        coeffs = eisenstein_q_expansion(6, 3)
        assert coeffs[0] == 1
        assert coeffs[1] == -504


class TestZetaLaurent:
    def test_leading_term(self):
        zl = zeta_laurent_coefficients()
        assert zl[-1]["coeff"] == 1

    def test_e2_term(self):
        zl = zeta_laurent_coefficients()
        assert zl[1]["eisenstein"] == "E_2"

    def test_e4_term(self):
        zl = zeta_laurent_coefficients()
        assert zl[3]["eisenstein"] == "E_4"


class TestBarDifferential:
    def test_deg1_zero(self):
        d1 = elliptic_bar_diff_deg(1)
        assert d1["rational"] == 0
        assert d1["elliptic"] == 0

    def test_deg2_quasi_modular(self):
        d2 = elliptic_bar_diff_deg(2)
        assert d2["quasi_modular"]
        assert d2["modular_weight"] == 2

    def test_deg3_modular(self):
        d3 = elliptic_bar_diff_deg(3)
        assert not d3["quasi_modular"]
        assert d3["modular_weight"] == 4

    def test_deg4_weight(self):
        d4 = elliptic_bar_diff_deg(4)
        assert d4["modular_weight"] == 6

    def test_rational_always_zero(self):
        for n in range(1, 6):
            assert elliptic_bar_diff_deg(n)["rational"] == 0


class TestCurvature:
    def test_nome_expansion(self):
        curv = elliptic_curvature()
        assert curv["nome_expansion_first_terms"][0] == 1
        assert curv["nome_expansion_first_terms"][1] == -24


class TestDecomposition:
    def test_deg2(self):
        d = bar_decomposition_by_weight(2)
        assert d["n_components"] == 2

    def test_deg3(self):
        d = bar_decomposition_by_weight(3)
        assert d["n_components"] == 3
        assert d["max_modular_weight"] == 4

    def test_deg5(self):
        d = bar_decomposition_by_weight(5)
        assert d["n_components"] == 5
        assert d["max_modular_weight"] == 8


class TestFay:
    def test_d_squared(self):
        fay = fay_d_squared_zero()
        assert "d^2 = 0" in fay["role"]
        assert "Arnold" in fay["rational_analog"]


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_toroidal().items():
            assert ok, f"Failed: {name}"
