"""Tests for Koszul pair verification.

Ground truth from CLAUDE.md critical pitfalls and manuscript.
"""

import pytest
from sympy import Symbol

from compute.lib.koszul_pairs import (
    KOSZUL_PAIRS,
    COMMON_ERRORS,
    ff_dual_level,
    ff_shift_sl2,
    ff_shift_sl3,
    check_involution,
    complementarity_sum_ds,
    verify_ff_duality,
    verify_koszul_pairs,
    verify_common_errors,
)

k = Symbol('k')


class TestFFDuality:
    def test_sl2_shift(self):
        """sl_2: k' = -k - 2*2 = -k - 4."""
        assert ff_shift_sl2(k) == -k - 4

    def test_sl3_shift(self):
        """sl_3: k' = -k - 2*3 = -k - 6."""
        assert ff_shift_sl3(k) == -k - 6

    def test_sl2_involution(self):
        """(k')' = k for sl_2."""
        assert ff_shift_sl2(ff_shift_sl2(k)) == k

    def test_sl3_involution(self):
        """(k')' = k for sl_3."""
        assert ff_shift_sl3(ff_shift_sl3(k)) == k

    def test_general_formula(self):
        """k' = -k - 2h^vee."""
        assert ff_dual_level(k, 2) == -k - 4
        assert ff_dual_level(k, 3) == -k - 6

    def test_critical_level_self_dual(self):
        """At critical level k = -h^vee: k' = h^vee - 2h^vee = -h^vee = k."""
        # sl_2: k = -2, k' = -(-2) - 4 = 2 - 4 = -2 ✓
        assert ff_shift_sl2(-2) == -2
        # sl_3: k = -3, k' = 3 - 6 = -3 ✓
        assert ff_shift_sl3(-3) == -3


class TestKoszulPairs:
    def test_heisenberg_not_self_dual(self):
        """CRITICAL: Heisenberg is NOT self-dual."""
        assert KOSZUL_PAIRS["Heisenberg_Symch"]["self_dual"] is False

    def test_betagamma_bc_involution(self):
        """(betagamma)^! = bc and (bc)^! = betagamma."""
        assert check_involution("beta_gamma_bc") is True

    def test_com_lie_involution(self):
        """(Com^!)^! = Lie^! = Com."""
        assert check_involution("Com_Lie") is True

    def test_com_dual_is_lie(self):
        assert KOSZUL_PAIRS["Com_Lie"]["A_dual"] == "Lie"

    def test_sym_dual_is_lambda(self):
        assert KOSZUL_PAIRS["Sym_Lambda"]["A_dual"] == "Lambda"


class TestCommonErrors:
    def test_all_flagged(self):
        for name, data in COMMON_ERRORS.items():
            assert "WRONG" in data["truth"], f"Error {name} not properly flagged"

    def test_heisenberg_error(self):
        assert "Sym^ch" in COMMON_ERRORS["Heisenberg_self_dual"]["truth"]

    def test_bosonization_error(self):
        assert "bosonization" in COMMON_ERRORS["bosonization_is_koszul"]["claim"]


class TestComplementarity:
    def test_sl2_virasoro(self):
        """sl_2 -> Virasoro: c + c' = 26."""
        assert complementarity_sum_ds("Virasoro") == 26

    def test_sl3_w3(self):
        """sl_3 -> W_3: c + c' = 100."""
        assert complementarity_sum_ds("W3") == 100


class TestSelfConsistency:
    def test_ff(self):
        for name, ok in verify_ff_duality().items():
            assert ok, f"Failed: {name}"

    def test_pairs(self):
        for name, ok in verify_koszul_pairs().items():
            assert ok, f"Failed: {name}"

    def test_errors(self):
        for name, ok in verify_common_errors().items():
            assert ok, f"Failed: {name}"
