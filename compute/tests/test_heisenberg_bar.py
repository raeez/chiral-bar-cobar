"""Tests for Heisenberg bar complex chain-level computations.

Ground truth from manuscript (detailed_computations.tex):
  OPE: a_{(1)}a = kappa (double pole), a_{(0)}a = 0 (no simple pole)
  Bar diff: D(aa) = kappa|0> (pure vacuum)
  Maximal-form cycles: d=0 for degree >= 3  [prop:heisenberg-maximal-form-cycles]
  Bar cohomology: p(n) = partition function  [KNOWN_BAR_DIMS]
  Curvature: m_0 = kappa
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.heisenberg_bar import (
    heisenberg_nth_products,
    heisenberg_nth_product,
    heisenberg_bar_diff_deg2,
    heisenberg_bar_diff_maximal_form,
    heisenberg_vacuum_dim,
    heisenberg_bar_chain_dim,
    heisenberg_bar_cohomology_dim,
    heisenberg_curvature,
    partition_number,
    verify_heisenberg_bar_diff,
    verify_maximal_form_cycles,
    verify_bar_cohomology_dims,
    verify_partition_values,
)

kappa = Symbol('kappa')


class TestNthProducts:
    def test_double_pole(self):
        """a_{(1)}a = kappa."""
        assert heisenberg_nth_product(1)["vac"] == kappa

    def test_no_simple_pole(self):
        """a_{(0)}a = 0 (KEY structural feature)."""
        assert len(heisenberg_nth_product(0)) == 0

    def test_no_higher_poles(self):
        for n in [2, 3, 4]:
            assert len(heisenberg_nth_product(n)) == 0


class TestBarDifferential:
    def test_vacuum(self):
        """D(a otimes a otimes eta) = kappa|0>."""
        vac, bar1 = heisenberg_bar_diff_deg2()
        assert vac["vac"] == kappa

    def test_no_bar1(self):
        """No bar^1 component (no simple pole)."""
        _, bar1 = heisenberg_bar_diff_deg2()
        assert len(bar1) == 0


class TestMaximalFormCycles:
    """All maximal-form elements are cycles at degree >= 3."""

    @pytest.mark.parametrize("n", [3, 4, 5, 6, 7, 8])
    def test_cycle(self, n):
        assert heisenberg_bar_diff_maximal_form(n) is True

    def test_not_cycle_deg2(self):
        assert heisenberg_bar_diff_maximal_form(2) is False


class TestVacuumModule:
    @pytest.mark.parametrize("w", [1, 2, 3, 5, 10])
    def test_dim_1(self, w):
        """dim V-bar_n = 1 for n >= 1."""
        assert heisenberg_vacuum_dim(w) == 1

    def test_dim_0(self):
        assert heisenberg_vacuum_dim(0) == 0


class TestPartitionFunction:
    @pytest.mark.parametrize("n,expected", [
        (0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 7),
        (6, 11), (7, 15), (8, 22), (9, 30), (10, 42),
    ])
    def test_values(self, n, expected):
        assert partition_number(n) == expected


class TestBarCohomology:
    """Bar cohomology dims from Master Table (by conformal weight)."""

    @pytest.mark.parametrize("h,expected", [
        (1, 1), (2, 1), (3, 1), (4, 2), (5, 3), (6, 5), (7, 7), (8, 11),
    ])
    def test_dims(self, h, expected):
        assert heisenberg_bar_cohomology_dim(h) == expected


class TestChainDims:
    """Chain group dimensions: C(h-1, n-1) * (n-1)!."""

    def test_deg1(self):
        """B^1_h = 1 for all h >= 1."""
        for h in range(1, 10):
            assert heisenberg_bar_chain_dim(1, h) == 1

    def test_deg2_h2(self):
        """B^2_2 = C(1,1) * 1 = 1."""
        assert heisenberg_bar_chain_dim(2, 2) == 1

    def test_deg2_h3(self):
        """B^2_3 = C(2,1) * 1 = 2."""
        assert heisenberg_bar_chain_dim(2, 3) == 2

    def test_deg3_h3(self):
        """B^3_3 = C(2,2) * 2 = 2."""
        assert heisenberg_bar_chain_dim(3, 3) == 2

    def test_below_diagonal(self):
        assert heisenberg_bar_chain_dim(3, 2) == 0
        assert heisenberg_bar_chain_dim(5, 4) == 0


class TestCurvature:
    def test_value(self):
        assert heisenberg_curvature() == kappa

    def test_matches_double_pole(self):
        assert heisenberg_nth_product(1)["vac"] == heisenberg_curvature()


class TestSelfConsistency:
    def test_bar_diff(self):
        for name, ok in verify_heisenberg_bar_diff().items():
            assert ok, f"Failed: {name}"

    def test_maximal_form(self):
        for name, ok in verify_maximal_form_cycles().items():
            assert ok, f"Failed: {name}"

    def test_cohomology(self):
        for name, ok in verify_bar_cohomology_dims().items():
            assert ok, f"Failed: {name}"

    def test_partitions(self):
        for name, ok in verify_partition_values().items():
            assert ok, f"Failed: {name}"
