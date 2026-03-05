"""Tests for free fermion bar complex chain-level computations.

Ground truth from manuscript (detailed_computations.tex):
  OPE: (psi_i)_{(0)}psi_j = delta_{ij}|0>  [comp:fermion-two-gen-ope]
  Bar diff: D([psi_i|psi_j]) = delta_{ij}|0>  [comp:fermion-deg2]
  Degree 3: explicit residue examples  [comp:fermion-deg3]
  Signs: desuspension makes generators even  [comp:fermion-deg2-signs]
  Coalgebra: B(F_2) = Sym^c(s^{-1}V-bar)  [prop:fermion-bar-symmetric]
  Koszul dual: F_2^! = Sym^ch(V*)
"""

import pytest
from sympy import Rational

from compute.lib.fermion_bar import (
    fermion_nth_product,
    fermion_all_products,
    fermion_bar_diff_deg2,
    fermion_bar_diff_deg3_example1,
    fermion_bar_diff_deg3_example2,
    fermion_curvature,
    fermion_bar_cohomology_dim,
    desuspension_parity,
    coalgebra_type,
    koszul_dual_type,
    FERMION_DIM_TABLE_WT_HALF,
    FERMION_FORM_DIMS,
    FERMION_DIFF_RANKS,
    verify_fermion_ope,
    verify_fermion_bar_diff,
    verify_fermion_deg3,
    verify_fermion_cohomology,
)


class TestOPE:
    def test_diagonal_simple_pole(self):
        """psi_i_{(0)}psi_i = |0> (simple pole)."""
        assert fermion_nth_product(1, 1, 0)["vac"] == Rational(1)
        assert fermion_nth_product(2, 2, 0)["vac"] == Rational(1)

    def test_off_diagonal_regular(self):
        """psi_1_{(0)}psi_2 = 0 (regular)."""
        assert len(fermion_nth_product(1, 2, 0)) == 0
        assert len(fermion_nth_product(2, 1, 0)) == 0

    def test_no_higher_poles(self):
        for i in [1, 2]:
            for j in [1, 2]:
                for n in [1, 2, 3]:
                    assert len(fermion_nth_product(i, j, n)) == 0


class TestBarDifferential:
    def test_diagonal_vacuum(self):
        """D([psi_i|psi_i]) = |0>."""
        for i in [1, 2]:
            vac, bar1 = fermion_bar_diff_deg2(i, i)
            assert vac["vac"] == Rational(1)
            assert len(bar1) == 0

    def test_off_diagonal_zero(self):
        """D([psi_1|psi_2]) = 0."""
        vac, bar1 = fermion_bar_diff_deg2(1, 2)
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_off_diagonal_zero_reverse(self):
        vac, bar1 = fermion_bar_diff_deg2(2, 1)
        assert len(vac) == 0
        assert len(bar1) == 0


class TestDegree3:
    """Degree 3 iterated residue examples."""

    def test_example1_total(self):
        """D([psi_1|psi_1|psi_2] otimes eta12^eta13) = [psi_2] otimes eta_23."""
        ex = fermion_bar_diff_deg3_example1()
        assert ex["total"] == "[psi_2] otimes eta_23"

    def test_example1_only_D12(self):
        """Only D_{12} contributes (diagonal psi_1-psi_1)."""
        ex = fermion_bar_diff_deg3_example1()
        assert ex["D_12"]["coeff"] == Rational(1)
        assert ex["D_13"]["coeff"] == Rational(0)
        assert ex["D_23"]["coeff"] == Rational(0)

    def test_example2_total(self):
        """D([psi_1|psi_2|psi_1] otimes eta12^eta13) = [psi_2] otimes eta_12."""
        ex = fermion_bar_diff_deg3_example2()
        assert ex["total"] == "[psi_2] otimes eta_12"

    def test_example2_only_D13(self):
        """Only D_{13} contributes (diagonal psi_1-psi_1)."""
        ex = fermion_bar_diff_deg3_example2()
        assert ex["D_12"]["coeff"] == Rational(0)
        assert ex["D_13"]["coeff"] == Rational(1)
        assert ex["D_23"]["coeff"] == Rational(0)


class TestStructure:
    def test_desuspension_even(self):
        """After desuspension, generators are even."""
        assert desuspension_parity() == "even"

    def test_symmetric_coalgebra(self):
        """B(F_2) = Sym^c (not Exterior^c)."""
        assert coalgebra_type() == "symmetric"

    def test_koszul_dual(self):
        """F_2^! = Sym^ch(V*)."""
        assert koszul_dual_type() == "Sym^ch(V*)"


class TestCurvature:
    def test_two_channels(self):
        """Curvature has two components (one per generator)."""
        curv = fermion_curvature()
        assert curv["psi_1"] == Rational(1)
        assert curv["psi_2"] == Rational(1)


class TestBarCohomology:
    @pytest.mark.parametrize("h,expected", [
        (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 7), (7, 11), (8, 15),
    ])
    def test_dims(self, h, expected):
        assert fermion_bar_cohomology_dim(h) == expected


class TestDimTable:
    def test_form_dims(self):
        """Form space dims = (n-1)!."""
        for n in [1, 2, 3, 4, 5]:
            from math import factorial
            assert FERMION_FORM_DIMS[n] == factorial(n - 1)


class TestSelfConsistency:
    def test_ope(self):
        for name, ok in verify_fermion_ope().items():
            assert ok, f"Failed: {name}"

    def test_bar_diff(self):
        for name, ok in verify_fermion_bar_diff().items():
            assert ok, f"Failed: {name}"

    def test_deg3(self):
        for name, ok in verify_fermion_deg3().items():
            assert ok, f"Failed: {name}"

    def test_cohomology(self):
        for name, ok in verify_fermion_cohomology().items():
            assert ok, f"Failed: {name}"
