"""Tests for BV-BRST formalism module."""

import pytest
from sympy import Rational

from compute.lib.bv_brst import (
    qme_coefficients,
    hcs_coefficients,
    ghost_number_table,
    bar_as_bv,
    bar_curvature_as_anomaly,
    feynman_bar_correspondence,
    verify_bv_brst,
)


class TestQME:
    def test_antibracket_coeff(self):
        """QME has factor 1/2 on antibracket."""
        assert qme_coefficients()["antibracket_coeff"] == Rational(1, 2)

    def test_not_one(self):
        """Common error: using factor 1 instead of 1/2."""
        assert qme_coefficients()["antibracket_coeff"] != 1


class TestHCS:
    def test_cubic_coeff(self):
        """HCS cubic term has coefficient 2/3."""
        assert hcs_coefficients()["cubic_coeff"] == Rational(2, 3)

    def test_not_one_third(self):
        """Common error: using 1/3 instead of 2/3."""
        assert hcs_coefficients()["cubic_coeff"] != Rational(1, 3)


class TestGhostNumber:
    def test_fields(self):
        assert ghost_number_table()["fields"] == 0

    def test_antifields(self):
        assert ghost_number_table()["antifields"] == 1

    def test_brst(self):
        assert ghost_number_table()["BRST_operator"] == 1


class TestBarAsBV:
    def test_differential(self):
        assert "BRST" in bar_as_bv()["bar_differential"]

    def test_curvature(self):
        assert "obstruction" in bar_as_bv()["curvature"]


class TestAnomalies:
    def test_virasoro(self):
        data = bar_curvature_as_anomaly("Virasoro")
        assert "c = 0" in data["anomaly_free_at"]
        assert "c = 26" in data["dual_anomaly_free_at"]

    def test_sl2_critical(self):
        data = bar_curvature_as_anomaly("sl2")
        assert "k = -2" in data["anomaly_free_at"]


class TestFeynman:
    def test_propagator(self):
        corr = feynman_bar_correspondence()
        assert "omega" in corr["propagator"]

    def test_arnold_renorm(self):
        corr = feynman_bar_correspondence()
        assert "Arnold" in corr["renormalization"]


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_bv_brst().items():
            assert ok, f"Failed: {name}"
