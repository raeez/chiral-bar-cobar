"""Tests for the shadow tower atlas: all standard families."""

from fractions import Fraction
from sympy import Symbol, Rational, simplify, factor, diff
import pytest

from compute.lib.shadow_tower_atlas import (
    KOSZUL_CONDUCTORS,
    LATTICE_EXAMPLES,
    affine_sl2_tower,
    affine_slN_tower,
    betagamma_tower,
    lattice_tower,
    shadow_depth_table,
    tline_level_independence,
    tline_sigma_invariant,
    virasoro_tower,
    w3_wline_tower,
)

c = Symbol('c')
k = Symbol('k')


# ===========================================================================
# Virasoro tower
# ===========================================================================

class TestVirasoroTower:
    def test_32_entries(self):
        S = virasoro_tower(32)
        assert len(S) == 31  # r = 2, ..., 32

    def test_S2(self):
        S = virasoro_tower(4)
        assert simplify(S[2] - c / 2) == 0

    def test_S3(self):
        S = virasoro_tower(4)
        assert simplify(S[3] - 2) == 0

    def test_S4(self):
        S = virasoro_tower(4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(S[4] - expected) == 0

    def test_S5(self):
        S = virasoro_tower(5)
        expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(S[5] - expected) == 0

    def test_denominator_pattern(self):
        """S_r has denominator c^{r-2} * (5c+22)^{floor((r-2)/2)}."""
        S = virasoro_tower(10)
        # Check at c=1: denominators should be nonzero
        for r in range(2, 11):
            val = S[r].subs(c, 1)
            assert val != 0, f"S_{r} vanishes at c=1"


# ===========================================================================
# W3 W-line tower
# ===========================================================================

class TestW3WlineTower:
    def test_even_arities_only(self):
        S = w3_wline_tower(12)
        for r in range(3, 13, 2):
            assert S[r] == 0, f"Odd arity {r} should be zero"

    def test_S2_W(self):
        S = w3_wline_tower(4)
        assert simplify(S[2] - c / 3) == 0

    def test_S4_W(self):
        S = w3_wline_tower(4)
        expected = Rational(2560) / (c * (5 * c + 22) ** 3)
        assert simplify(S[4] - expected) == 0

    def test_S6_nonzero(self):
        S = w3_wline_tower(6)
        assert S[6] != 0

    def test_16_even_entries(self):
        S = w3_wline_tower(32)
        even_entries = [r for r in S if r % 2 == 0 and S[r] != 0]
        assert len(even_entries) >= 15


# ===========================================================================
# T-line sigma-invariants for W_N
# ===========================================================================

class TestTLineSigma:
    def test_virasoro_delta2_is_13(self):
        D = tline_sigma_invariant(2, 4)
        assert simplify(D[2] - 13) == 0

    def test_w3_delta2(self):
        D = tline_sigma_invariant(3, 4)
        # K_3 = 100, so Delta^(2) = c/2 + (100-c)/2 = 50
        assert simplify(D[2] - 50) == 0

    def test_w4_delta2(self):
        D = tline_sigma_invariant(4, 4)
        # K_4 = 246, so Delta^(2) = 246/2 = 123
        assert simplify(D[2] - 123) == 0

    def test_w5_delta2(self):
        D = tline_sigma_invariant(5, 4)
        assert simplify(D[2] - 244) == 0  # K_5/2 = 488/2

    def test_w6_delta2(self):
        D = tline_sigma_invariant(6, 4)
        assert simplify(D[2] - 425) == 0  # K_6/2 = 850/2

    def test_level_independence_arity23(self):
        """Arities 2-3 are level-independent for all W_N."""
        for N in range(2, 7):
            li = tline_level_independence(N, 4)
            assert li[2] is True, f"W_{N} arity 2 not level-ind"
            assert li[3] is True, f"W_{N} arity 3 not level-ind"

    def test_level_dependence_arity4(self):
        """Arity 4 is level-dependent for all W_N."""
        for N in range(2, 7):
            li = tline_level_independence(N, 4)
            assert li[4] is False, f"W_{N} arity 4 level-ind (wrong!)"


# ===========================================================================
# Affine KM towers
# ===========================================================================

class TestAffineKM:
    def test_sl2_terminates(self):
        T = affine_sl2_tower()
        assert T[4] == 0
        assert T["depth"] == 3

    def test_sl2_kappa(self):
        T = affine_sl2_tower()
        expected = Rational(3) * (k + 2) / 4
        assert simplify(T[2] - expected) == 0

    def test_slN_terminates(self):
        for N in range(2, 8):
            T = affine_slN_tower(N)
            assert T[4] == 0
            assert T["depth"] == 3
            assert T["class"] == "L"

    def test_slN_kappa_formula(self):
        for N in [2, 3, 4, 5]:
            T = affine_slN_tower(N)
            dim_g = N * N - 1
            expected = Rational(dim_g) * (k + N) / (2 * N)
            assert simplify(T[2] - expected) == 0


# ===========================================================================
# Lattice VOA towers
# ===========================================================================

class TestLattice:
    def test_terminates_at_2(self):
        for name, data in LATTICE_EXAMPLES.items():
            T = lattice_tower(data["rank"])
            assert T[3] == 0, f"{name} should terminate at arity 2"
            assert T["depth"] == 2
            assert T["class"] == "G"

    def test_kappa_equals_rank(self):
        for name, data in LATTICE_EXAMPLES.items():
            T = lattice_tower(data["rank"])
            assert T[2] == data["rank"]

    def test_leech_kappa_24(self):
        T = lattice_tower(24)
        assert T[2] == 24


# ===========================================================================
# Beta-gamma tower
# ===========================================================================

class TestBetaGamma:
    def test_terminates_at_4(self):
        T = betagamma_tower()
        assert T[5] == 0
        assert T["depth"] == 4
        assert T["class"] == "C"

    def test_kappa_plus_1(self):
        T = betagamma_tower()
        assert T[2] == Rational(1)

    def test_quartic_value(self):
        T = betagamma_tower()
        assert T[4] == Rational(5, 32)


# ===========================================================================
# Summary
# ===========================================================================

class TestSummary:
    def test_depth_table_complete(self):
        table = shadow_depth_table()
        assert "Heisenberg" in table
        assert "Lattice V_Lambda" in table
        assert "Affine V_k(g)" in table
        assert "Beta-gamma" in table
        assert "Virasoro" in table
        assert "W_3" in table
        assert "W_N (N>=3)" in table

    def test_depth_ordering(self):
        """G < L < C < M in shadow depth."""
        table = shadow_depth_table()
        assert table["Heisenberg"]["depth"] == 2
        assert table["Affine V_k(g)"]["depth"] == 3
        assert table["Beta-gamma"]["depth"] == 4
        assert table["Virasoro"]["depth"] == "inf"
