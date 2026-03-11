"""Tests for compute/lib/genus_expansion.py — functions NOT covered by test_genus.py.

test_genus.py already covers:
  kappa_heisenberg, kappa_virasoro, kappa_w3, kappa_sl2, kappa_sl3,
  kappa_g2, kappa_b2, genus_table, complementarity_sum_km

This file covers the remaining public API:
  genus_table_numeric, complementarity_sum_w, convergence_radius,
  ratio_successive, verify_F1, KNOWN_F1
"""

import pytest
from sympy import Rational, Symbol, pi, simplify

from compute.lib.genus_expansion import (
    genus_table_numeric,
    complementarity_sum_w,
    convergence_radius,
    ratio_successive,
    verify_F1,
    KNOWN_F1,
    kappa_heisenberg,
    kappa_sl2,
    genus_table,
)


class TestGenusTableNumeric:
    def test_returns_strings(self):
        """genus_table_numeric returns string representations."""
        table = genus_table_numeric(Rational(1), max_genus=3)
        assert isinstance(table[1], str)
        assert isinstance(table[2], str)
        assert isinstance(table[3], str)

    def test_matches_exact_table(self):
        """Numeric and exact tables encode same values."""
        kappa_val = Rational(3, 2)
        exact = genus_table(kappa_val, max_genus=5)
        numeric = genus_table_numeric(kappa_val, max_genus=5)
        for g in range(1, 6):
            assert str(exact[g]) == numeric[g]

    def test_genus_keys(self):
        """Keys are 1 through max_genus."""
        table = genus_table_numeric(Rational(1), max_genus=4)
        assert set(table.keys()) == {1, 2, 3, 4}


class TestComplementaritySumW:
    def test_virasoro_sum(self):
        """Virasoro W-algebra: kappa + kappa' = 26 * sigma(A1) = 26 * 1/2 = 13."""
        total = complementarity_sum_w("A", 1)
        assert simplify(total - 13) == 0

    def test_w3_sum(self):
        """W_3: kappa + kappa' = 100 * 5/6 = 250/3."""
        total = complementarity_sum_w("A", 2)
        assert simplify(total - Rational(250, 3)) == 0

    def test_w3_level_independent(self):
        """W_3 sum is constant (no k dependence)."""
        total = complementarity_sum_w("A", 2)
        k = Symbol("k")
        # total should not contain k
        assert simplify(total.diff(k)) == 0


class TestConvergenceRadius:
    def test_value(self):
        """Radius of convergence = 2*pi."""
        assert convergence_radius() == 2 * pi


class TestRatioSuccessive:
    def test_kappa1_genus1(self):
        """F_2/F_1 for kappa=1 is lambda_2/lambda_1 = (7/5760)/(1/24) = 7/240."""
        ratio = ratio_successive(Rational(1), 1)
        assert simplify(ratio - Rational(7, 240)) == 0

    def test_kappa_zero_returns_none(self):
        """F_1(0) = 0, so ratio is undefined."""
        result = ratio_successive(Rational(0), 1)
        assert result is None

    def test_ratio_independent_of_kappa(self):
        """F_{g+1}/F_g = lambda_{g+1}/lambda_g, independent of kappa."""
        r1 = ratio_successive(Rational(1), 3)
        r2 = ratio_successive(Rational(5), 3)
        assert simplify(r1 - r2) == 0


class TestVerifyF1:
    def test_heisenberg_pass(self):
        """F_1(H_kappa) = kappa/24."""
        ok, msg = verify_F1("Heisenberg", 1, Rational(1, 24))
        assert ok, msg

    def test_heisenberg_fail(self):
        """Wrong value fails."""
        ok, msg = verify_F1("Heisenberg", 1, Rational(1, 12))
        assert not ok

    def test_sl2_pass(self):
        """F_1(sl_2, k=1) = 3*3/4 * 1/24 = 3/32."""
        expected = Rational(3) * (Rational(1) + 2) / 4 * Rational(1, 24)
        ok, msg = verify_F1("sl2", 1, expected)
        assert ok, msg

    def test_unknown_algebra(self):
        """Unknown algebra returns True (no ground truth to fail against)."""
        ok, msg = verify_F1("FooAlgebra", 0, 999)
        assert ok

    def test_virasoro_pass(self):
        """F_1(Vir, c=2) = 1 * 1/24 = 1/24."""
        ok, msg = verify_F1("Virasoro", 2, Rational(1, 24))
        assert ok, msg


class TestKnownF1Registry:
    def test_all_algebras_present(self):
        """KNOWN_F1 has entries for all standard algebras."""
        expected_keys = {"Heisenberg", "sl2", "sl3", "G2", "B2", "Virasoro", "W3"}
        assert set(KNOWN_F1.keys()) == expected_keys

    def test_all_formulas_callable(self):
        """Each formula in KNOWN_F1 is callable and returns a number."""
        for name, (param_name, formula) in KNOWN_F1.items():
            result = formula(Rational(1))
            assert result is not None
