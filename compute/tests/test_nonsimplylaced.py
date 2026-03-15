"""Tests for non-simply-laced (B_2 and G_2) bar complexes.

Ground truth from CLAUDE.md and manuscript.
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.nonsimplylaced_bar import (
    b2_data, b2_central_charge, b2_ff_dual, b2_kappa,
    b2_complementarity_sum, b2_bar_generators, b2_curvature,
    g2_data, g2_central_charge, g2_ff_dual, g2_kappa,
    g2_complementarity_sum, g2_bar_generators, g2_curvature,
    periodicity_coxeter, periodicity_vs_dual_coxeter,
    verify_nonsimplylaced_all,
)

k = Symbol('k')


class TestB2Data:
    def test_dim(self):
        assert b2_data()["dim"] == 10

    def test_h_vs_hdual(self):
        d = b2_data()
        assert d["h"] == 4
        assert d["h_dual"] == 3
        assert d["h"] != d["h_dual"]

    def test_positive_roots(self):
        assert b2_data()["n_positive_roots"] == 4

    def test_generators(self):
        g = b2_bar_generators()
        assert g["total"] == 10
        assert g["cartan"] == 2


class TestB2Formulas:
    def test_central_charge(self):
        assert b2_central_charge(k) == 10 * k / (k + 3)

    def test_ff_dual(self):
        assert b2_ff_dual(k) == -k - 6

    def test_ff_involution(self):
        assert b2_ff_dual(b2_ff_dual(k)) == k

    def test_kappa(self):
        assert b2_kappa(k) == Rational(5) * (k + 3) / 3

    def test_complementarity(self):
        assert b2_complementarity_sum() == 20

    def test_curvature_critical(self):
        """At k = -h^vee = -3: curvature vanishes."""
        assert b2_curvature(-3) == 0


class TestG2Data:
    def test_dim(self):
        assert g2_data()["dim"] == 14

    def test_h_vs_hdual(self):
        d = g2_data()
        assert d["h"] == 6
        assert d["h_dual"] == 4
        assert d["h"] != d["h_dual"]

    def test_positive_roots(self):
        assert g2_data()["n_positive_roots"] == 6

    def test_generators(self):
        g = g2_bar_generators()
        assert g["total"] == 14
        assert g["cartan"] == 2


class TestG2Formulas:
    def test_central_charge(self):
        assert g2_central_charge(k) == 14 * k / (k + 4)

    def test_ff_dual(self):
        assert g2_ff_dual(k) == -k - 8

    def test_ff_involution(self):
        assert g2_ff_dual(g2_ff_dual(k)) == k

    def test_kappa(self):
        assert g2_kappa(k) == Rational(7) * (k + 4) / 4

    def test_complementarity(self):
        assert g2_complementarity_sum() == 28

    def test_curvature_critical(self):
        """At k = -h^vee = -4: curvature vanishes."""
        assert g2_curvature(-4) == 0


class TestPeriodicity:
    def test_b2_period(self):
        """B_2 period = 2h = 8, NOT 2h^vee = 6."""
        assert periodicity_coxeter("B", 2) == 8

    def test_g2_period(self):
        """G_2 period = 2h = 12, NOT 2h^vee = 8."""
        assert periodicity_coxeter("G", 2) == 12

    def test_a2_simply_laced(self):
        p = periodicity_vs_dual_coxeter("A", 2)
        assert p["simply_laced"]
        assert p["h"] == p["h_dual"] == 3

    def test_b2_not_simply_laced(self):
        p = periodicity_vs_dual_coxeter("B", 2)
        assert not p["simply_laced"]

    def test_g2_not_simply_laced(self):
        p = periodicity_vs_dual_coxeter("G", 2)
        assert not p["simply_laced"]


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_nonsimplylaced_all().items():
            assert ok, f"Failed: {name}"
