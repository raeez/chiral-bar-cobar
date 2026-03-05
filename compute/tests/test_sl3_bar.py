"""Tests for sl_3 bar complex chain-level computations.

Ground truth from manuscript (detailed_computations.tex):
  comp:sl3-ope — OPE data for sl_3-hat_k
  comp:sl3-bar — bar differential at degree 2, Serre relations
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.sl3_bar import (
    H1, H2, E1, E2, E3, F1, F2, F3,
    GEN_NAMES, DIM_G, CARTAN,
    sl3_structure_constants,
    sl3_killing_form,
    sl3_nth_product,
    sl3_bar_diff_deg2,
    sl3_bar_diff_examples,
    sl3_curvature,
    sl3_sugawara_c,
    sl3_serre_cycle,
    sl3_serre_vanishes,
    sl3_jacobi_check,
    verify_sl3_bar_diff,
    verify_sl3_serre,
)

k = Symbol('k')


class TestStructureConstants:
    """Verify sl_3 Lie algebra structure."""

    def test_jacobi(self):
        assert sl3_jacobi_check() is True

    def test_cartan_eigenvalues(self):
        """[H_1, E_1] = 2E_1, [H_1, E_2] = -E_2."""
        bracket = sl3_structure_constants()
        assert bracket[(H1, E1)] == {E1: Rational(2)}
        assert bracket[(H1, E2)] == {E2: Rational(-1)}

    def test_simple_brackets(self):
        """[E_1, F_1] = H_1, [E_1, E_2] = E_3."""
        bracket = sl3_structure_constants()
        assert bracket[(E1, F1)] == {H1: Rational(1)}
        assert bracket[(E1, E2)] == {E3: Rational(1)}

    def test_serre_relation(self):
        """[E_1, [E_1, E_2]] = [E_1, E_3] = 0."""
        bracket = sl3_structure_constants()
        assert (E1, E3) not in bracket

    def test_dim(self):
        assert DIM_G == 8

    def test_cartan_matrix(self):
        assert CARTAN[0, 0] == 2
        assert CARTAN[0, 1] == -1


class TestKillingForm:
    def test_cartan_diagonal(self):
        kf = sl3_killing_form()
        assert kf[(H1, H1)] == Rational(2)
        assert kf[(H2, H2)] == Rational(2)

    def test_cartan_off_diagonal(self):
        kf = sl3_killing_form()
        assert kf[(H1, H2)] == Rational(-1)

    def test_root_pairing(self):
        kf = sl3_killing_form()
        assert kf[(E1, F1)] == Rational(1)
        assert kf[(E3, F3)] == Rational(1)


class TestNthProducts:
    def test_HH_double_pole(self):
        """H_1_{(1)}H_1 = 2k (double pole)."""
        result = sl3_nth_product(H1, H1, 1)
        assert result["vac"] == 2 * k

    def test_HH_off_diagonal(self):
        """H_1_{(1)}H_2 = -k."""
        result = sl3_nth_product(H1, H2, 1)
        assert result["vac"] == -k

    def test_EF_double_pole(self):
        """E_1_{(1)}F_1 = k (double pole)."""
        result = sl3_nth_product(E1, F1, 1)
        assert result["vac"] == k

    def test_HE_simple_pole(self):
        """H_1_{(0)}E_1 = 2E_1 (simple pole)."""
        result = sl3_nth_product(H1, E1, 0)
        assert result["E1"] == Rational(2)

    def test_EE_simple_pole(self):
        """E_1_{(0)}E_2 = E_3."""
        result = sl3_nth_product(E1, E2, 0)
        assert result["E3"] == Rational(1)

    def test_no_higher_poles(self):
        """KM algebras have at most double poles."""
        for n in [2, 3]:
            assert len(sl3_nth_product(H1, H1, n)) == 0
            assert len(sl3_nth_product(E1, E2, n)) == 0


class TestBarDifferential:
    """Degree-2 bar differential from comp:sl3-bar."""

    def test_H1_E1(self):
        """d[H_1|E_1] = 2[E_1]."""
        vac, bar1 = sl3_bar_diff_deg2(H1, E1)
        assert len(vac) == 0
        assert bar1["E1"] == Rational(2)

    def test_H1_E2(self):
        """d[H_1|E_2] = -[E_2]."""
        vac, bar1 = sl3_bar_diff_deg2(H1, E2)
        assert len(vac) == 0
        assert bar1["E2"] == Rational(-1)

    def test_E1_E2(self):
        """d[E_1|E_2] = [E_3]."""
        vac, bar1 = sl3_bar_diff_deg2(E1, E2)
        assert len(vac) == 0
        assert bar1["E3"] == Rational(1)

    def test_E1_F1_curvature(self):
        """d[E_1|F_1] = [H_1] + k*|0⟩ (curvature term)."""
        vac, bar1 = sl3_bar_diff_deg2(E1, F1)
        assert vac["vac"] == k
        assert bar1["H1"] == Rational(1)

    def test_E2_F2_curvature(self):
        """d[E_2|F_2] = [H_2] + k*|0⟩."""
        vac, bar1 = sl3_bar_diff_deg2(E2, F2)
        assert vac["vac"] == k
        assert bar1["H2"] == Rational(1)

    def test_E3_F3(self):
        """d[E_3|F_3] = [H_1+H_2] + k*|0⟩."""
        vac, bar1 = sl3_bar_diff_deg2(E3, F3)
        assert vac["vac"] == k
        assert bar1["H1"] == Rational(1)
        assert bar1["H2"] == Rational(1)

    def test_vanishing_pairs(self):
        """d[E_1|E_1] = 0 (no OPE)."""
        vac, bar1 = sl3_bar_diff_deg2(E1, E1)
        assert len(vac) == 0
        assert len(bar1) == 0


class TestCurvature:
    def test_EF_curvatures(self):
        curv = sl3_curvature()
        assert curv[(E1, F1)] == k
        assert curv[(E2, F2)] == k
        assert curv[(E3, F3)] == k

    def test_HH_curvatures(self):
        curv = sl3_curvature()
        assert curv[(H1, H1)] == 2 * k


class TestSugawara:
    def test_formula(self):
        """c = 8k/(k+3)."""
        c_val = sl3_sugawara_c()
        assert c_val == 8 * k / (k + 3)

    def test_large_k(self):
        """c -> 8 as k -> infinity."""
        from sympy import limit, oo
        c_val = sl3_sugawara_c()
        assert limit(c_val, k, oo) == 8

    def test_critical_level(self):
        """c diverges at k = -h^vee = -3."""
        from sympy import limit, oo
        c_val = sl3_sugawara_c()
        assert abs(limit(c_val, k, -3)) == oo


class TestSerre:
    def test_serre_vanishes(self):
        assert sl3_serre_vanishes() is True

    def test_serre_cycle_data(self):
        data = sl3_serre_cycle()
        assert data["type"] == "Serre"
        assert len(data["generators"]) == 3
        assert data["coefficients"] == [Rational(1), Rational(-2), Rational(1)]


class TestSelfConsistency:
    def test_bar_diff(self):
        for name, ok in verify_sl3_bar_diff().items():
            assert ok, f"Failed: {name}"

    def test_serre(self):
        for name, ok in verify_sl3_serre().items():
            assert ok, f"Failed: {name}"
