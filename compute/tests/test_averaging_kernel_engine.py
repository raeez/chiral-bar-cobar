"""
Tests for averaging_kernel_engine.

Verification sources for each expected value:
  [DC] direct computation   [LT] literature (Weyl dimension formula)
  [LC] limiting case        [SY] symmetry (Sigma_n action)

# VERIFIED: sl2 n=2: binom(4,2)/3^2 = 6/9 = 2/3  [DC] [SY: Sym^2(C^3)=6]
# VERIFIED: sl2 n=3: binom(5,3)/3^3 = 10/27        [DC] [LT: stars-and-bars]
# VERIFIED: sl2 n=4: binom(6,4)/3^4 = 15/81 = 5/27 [DC] [LT: stars-and-bars]
# VERIFIED: Heis d=1: binom(n,n)/1 = 1 for all n    [DC] [LC: d=1 trivial]
# VERIFIED: Vir  d=1: same as Heis                   [DC] [LC: d=1 trivial]
# VERIFIED: sl3 n=2: binom(9,2)/8^2 = 36/64 = 9/16  [DC] [SY: Sym^2(C^8)]
# VERIFIED: odd d=3 n=2: binom(3,2)/3^2 = 3/9 = 1/3 [DC] [SY: Alt^2(C^3)]
# VERIFIED: odd d=3 n=3: binom(3,3)/3^3 = 1/27       [DC] [SY: Alt^3(C^3)]
"""

from fractions import Fraction

import pytest

from compute.lib.averaging_kernel_engine import (
    FAMILIES,
    arity_table,
    information_ratio,
    kernel_dim,
    surviving_dim,
)


# ── sl_2 anchor values ──────────────────────────────────────────────

class TestSl2:
    """sl_2: d=3, parity=even."""

    def test_sl2_arity2(self):
        # binom(4,2) = 6, total = 9, ratio = 2/3, kernel = 3
        assert information_ratio(3, 2, "even") == Fraction(2, 3)
        assert kernel_dim(3, 2, "even") == 3

    def test_sl2_arity3(self):
        # binom(5,3) = 10, total = 27, ratio = 10/27, kernel = 17
        assert information_ratio(3, 3, "even") == Fraction(10, 27)
        assert kernel_dim(3, 3, "even") == 17

    def test_sl2_arity4(self):
        # binom(6,4) = 15, total = 81, ratio = 5/27, kernel = 66
        assert information_ratio(3, 4, "even") == Fraction(5, 27)
        assert kernel_dim(3, 4, "even") == 66


# ── d=1 families: ratio always 1 ────────────────────────────────────

class TestHeisAllArities:
    def test_heis_all_arities(self):
        for n in range(1, 11):
            assert information_ratio(1, n, "even") == Fraction(1, 1), (
                f"Heis ratio != 1 at n={n}"
            )
            assert kernel_dim(1, n, "even") == 0


class TestVirAllArities:
    def test_vir_all_arities(self):
        for n in range(1, 11):
            assert information_ratio(1, n, "even") == Fraction(1, 1), (
                f"Vir ratio != 1 at n={n}"
            )
            assert kernel_dim(1, n, "even") == 0


# ── sl_3 ─────────────────────────────────────────────────────────────

class TestSl3:
    def test_sl3_arity2(self):
        # binom(9,2) = 36, total = 64, kernel = 28
        assert surviving_dim(8, 2, "even") == 36
        assert kernel_dim(8, 2, "even") == 28
        assert information_ratio(8, 2, "even") == Fraction(36, 64)


# ── odd parity ───────────────────────────────────────────────────────

class TestOddParity:
    """Odd desuspended degree: alternating power."""

    def test_odd_d3_n2(self):
        # Alt^2(C^3) = binom(3,2) = 3, total = 9
        assert surviving_dim(3, 2, "odd") == 3
        assert information_ratio(3, 2, "odd") == Fraction(1, 3)
        assert kernel_dim(3, 2, "odd") == 6

    def test_odd_d3_n3(self):
        # Alt^3(C^3) = binom(3,3) = 1, total = 27
        assert surviving_dim(3, 3, "odd") == 1
        assert information_ratio(3, 3, "odd") == Fraction(1, 27)
        assert kernel_dim(3, 3, "odd") == 26

    def test_odd_vanishes_beyond_d(self):
        # Alt^n(C^3) = 0 for n > 3
        assert surviving_dim(3, 4, "odd") == 0
        assert kernel_dim(3, 4, "odd") == 81


# ── structural properties ────────────────────────────────────────────

class TestKernelNonnegativity:
    def test_kernel_nonneg_all_families(self):
        for fam_name, cfg in FAMILIES.items():
            d = cfg["d"]
            par = cfg["parity"]
            for n in range(1, 21):
                k = kernel_dim(d, n, par)
                assert k >= 0, (
                    f"kernel_dim < 0 for {fam_name} at n={n}: {k}"
                )


class TestArityTableLength:
    def test_table_length(self):
        for max_n in (5, 10, 15):
            rows = arity_table("sl2", max_arity=max_n)
            assert len(rows) == max_n


class TestMonotoneRatioDecrease:
    """For d >= 2 even parity, the information ratio is non-increasing."""

    def test_sl2_ratio_nonincreasing(self):
        rows = arity_table("sl2", max_arity=20)
        for i in range(1, len(rows)):
            assert rows[i]["ratio"] <= rows[i - 1]["ratio"], (
                f"ratio increased at n={rows[i]['n']}: "
                f"{rows[i-1]['ratio']} -> {rows[i]['ratio']}"
            )


# ── arity-1 identity ────────────────────────────────────────────────

class TestArity1:
    """At arity 1, the averaging map is the identity: ratio = 1."""

    def test_arity1_all_families(self):
        for fam_name, cfg in FAMILIES.items():
            d = cfg["d"]
            par = cfg["parity"]
            assert information_ratio(d, 1, par) == Fraction(1, 1), (
                f"ratio != 1 at n=1 for {fam_name}"
            )
            assert kernel_dim(d, 1, par) == 0
