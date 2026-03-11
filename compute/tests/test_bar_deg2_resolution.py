"""Tests resolving rem:bar-deg2-symmetric-square — H^2_{h=2}(bar) = 0, not 6.

The original remark claimed H^2_{h=2} = 6 = binom(4,2) by using:
  (WRONG) B^1_{h=2} = g_2 (dim 3, mode-2 generators only)
  (WRONG) d = Lie bracket [a,b] (0-th product)

Correct:
  B^1_{h=2} = A-bar_2 = g_2 + S^2(g_1) (dim 9)
  d = normally ordered product :ab: ((-1)-th product)
  rank(d) = 9, so H^2_{h=2} = 0

Ground truth:
  H^2(bar, sl_2-hat) = 5, all at weight 3 [comp:sl2-ce-verification]
  H^2_{h=2} = 0 (this computation)
"""

import pytest
import numpy as np
from fractions import Fraction

from compute.lib.bar_deg2_resolution import (
    DIM_G,
    sl2_structure_constants,
    sl2_killing_form,
    abar_weight_basis,
    dim_abar,
    bar_chain_dim,
    bar_differential_weight2,
    bar_differential_weight2_rank,
    h2_weight2,
    weight3_euler_char,
    ce_h2_sl2,
    verify_no_weight2_contribution_to_h2,
)


# ============================================================
# sl_2 data
# ============================================================

class TestSl2Data:
    def test_dim(self):
        assert DIM_G == 3

    def test_structure_constants_antisymmetry(self):
        c = sl2_structure_constants()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    assert c[i, j, k] == -c[j, i, k], \
                        f"Antisymmetry fails at ({i},{j},{k})"

    def test_structure_constants_jacobi(self):
        """Verify Jacobi identity: [e_i, [e_j, e_k]] + cyclic = 0."""
        c = sl2_structure_constants()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # [[e_i, e_j], e_k] = c[i,j,l] c[l,k,m] e_m
                    for m in range(3):
                        val = Fraction(0)
                        for l in range(3):
                            val += c[i, j, l] * c[l, k, m]
                            val += c[j, k, l] * c[l, i, m]
                            val += c[k, i, l] * c[l, j, m]
                        assert val == 0, \
                            f"Jacobi fails at ({i},{j},{k},{m}): {val}"

    def test_killing_form_invariance(self):
        """Verify kap([a,b], c) = kap(a, [b,c])."""
        c = sl2_structure_constants()
        kap = sl2_killing_form()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    lhs = sum(c[i, j, l] * kap[l, k] for l in range(3))
                    rhs = sum(c[j, k, l] * kap[i, l] for l in range(3))
                    assert lhs == rhs, \
                        f"Invariance fails at ({i},{j},{k}): {lhs} != {rhs}"


# ============================================================
# Chain group dimensions
# ============================================================

class TestChainGroups:
    def test_abar_weight1(self):
        """A-bar_1 = g_1 = g, dim = 3."""
        assert dim_abar(1) == 3

    def test_abar_weight2(self):
        """A-bar_2 = g_2 + S^2(g_1), dim = 3 + 6 = 9.

        This is the KEY correction: the original remark used dim 3.
        """
        assert dim_abar(2) == 9
        # Decomposition check
        basis = abar_weight_basis(2)
        mode2 = [b for b in basis if len(b) == 2 and b[1] == "mode2"]
        nop = [b for b in basis if len(b) == 3 and b[2] == "nop"]
        assert len(mode2) == 3, "g_2 should have dim 3"
        assert len(nop) == 6, "S^2(g_1) should have dim 6"
        assert len(mode2) + len(nop) == 9

    def test_abar_weight2_NOT_3(self):
        """Explicitly verify the remark's error: B^1_{h=2} != 3."""
        assert dim_abar(2) != 3, \
            "The old remark used dim 3 (mode-2 only), which was wrong"

    def test_abar_weight3(self):
        """A-bar_3 = g_3 + g_2*g_1 + S^3(g_1), dim = 3 + 9 + 10 = 22."""
        assert dim_abar(3) == 22

    def test_b2_weight2(self):
        """B^2_{h=2} = g tensor g, dim = 9."""
        assert bar_chain_dim(2, 2) == 9

    def test_b1_weight2(self):
        """B^1_{h=2} = A-bar_2, dim = 9."""
        assert bar_chain_dim(1, 2) == 9

    def test_b3_weight2_zero(self):
        """B^3_{h=2} = 0 (three weight-1 factors need weight >= 3)."""
        assert bar_chain_dim(3, 2) == 0

    def test_b2_weight3(self):
        """B^2_{h=3} = A-bar_1 tensor A-bar_2 + A-bar_2 tensor A-bar_1, dim = 54."""
        assert bar_chain_dim(2, 3) == 54

    def test_b3_weight3(self):
        """B^3_{h=3} = g^{tensor 3} / Arnold, dim = 27 * 2 = 54."""
        assert bar_chain_dim(3, 3) == 54


# ============================================================
# Bar differential at weight 2
# ============================================================

class TestBarDifferentialWeight2:
    def test_differential_shape(self):
        """d: B^2_{h=2} -> B^1_{h=2} is 9x9."""
        d = bar_differential_weight2()
        assert d.shape == (9, 9)

    def test_differential_rank_9(self):
        """The bar differential at weight 2 is an ISOMORPHISM (rank 9).

        This is the core computation: the normally ordered product map
        J^a tensor J^b |-> J^a_{-1}J^b_{-1}|0> has full rank.
        """
        rank = bar_differential_weight2_rank()
        assert rank == 9, \
            f"Expected rank 9 (isomorphism), got {rank}"

    def test_h2_weight2_is_zero(self):
        """H^2_{h=2}(bar) = 0, NOT 6.

        This is the main result resolving rem:bar-deg2-symmetric-square.
        """
        assert h2_weight2() == 0

    def test_diagonal_entries(self):
        """Check specific entries of the differential.

        d(e tensor e) = :ee: = J^e_{-1}J^e_{-1}|0>
        This should map to the (0,0) nop basis element (index 3).
        Source index: 0*3+0 = 0. Target index: 3.
        """
        d = bar_differential_weight2()
        # e tensor e -> :ee: at index 3
        assert d[3, 0] == Fraction(1)

    def test_symmetric_pair(self):
        """d(e tensor h) -> :eh: = nop basis (0,1) at index 4."""
        d = bar_differential_weight2()
        # e tensor h: source index 0*3+1 = 1, target index 4 (pair (0,1))
        assert d[4, 1] == Fraction(1)

    def test_antisymmetric_pair(self):
        """d(h tensor e) -> :he: = :eh: + [h,e]_{-2} = :eh: + 2*e_{-2}.

        Source index: 1*3+0 = 3.
        Target: nop(0,1) at index 4 with coeff 1, plus mode2(e) at index 0 with coeff 2.
        """
        d = bar_differential_weight2()
        src = 1 * 3 + 0  # h tensor e
        assert d[4, src] == Fraction(1), "symmetric part of :he:"
        assert d[0, src] == Fraction(2), "[h,e] = 2e contributes to mode-2"

    def test_ef_antisymmetric(self):
        """d(e tensor f) and d(f tensor e) differ by structure constants.

        d(e tensor f) = J^e_{-1}J^f_{-1}|0> -> nop(0,2) at index 5.
        d(f tensor e) = J^f_{-1}J^e_{-1}|0> = :ef: + [f,e]_{-2}
                      = nop(0,2) + (-1)*h_{-2}
        """
        d = bar_differential_weight2()
        # e tensor f: source = 0*3+2 = 2
        assert d[5, 2] == Fraction(1), "e tensor f -> :ef:"

        # f tensor e: source = 2*3+0 = 6
        assert d[5, 6] == Fraction(1), "f tensor e -> :ef: (symmetric part)"
        assert d[1, 6] == Fraction(-1), "[f,e] = -h -> -1 * h_{-2}"

    def test_commutator_produces_mode2(self):
        """The antisymmetric part of d produces mode-2 generators.

        For each pair (a,b) with a > b, the commutator [J^a, J^b]
        contributes f^{ab}_c J^c_{-2} to the mode-2 subspace.
        This is how g_2 is covered by the image of d.
        """
        d = bar_differential_weight2()
        c = sl2_structure_constants()

        # The three antisymmetric directions span g_2 via:
        # J^a_{-1}J^b_{-1} - J^b_{-1}J^a_{-1} = f^{ab}_c J^c_{-2}
        for a in range(DIM_G):
            for b in range(a + 1, DIM_G):
                # d(a tensor b) - d(b tensor a) should give f^{ab}_c in mode-2
                src_ab = a * DIM_G + b
                src_ba = b * DIM_G + a
                for k in range(DIM_G):
                    diff = d[k, src_ab] - d[k, src_ba]
                    # This should be -f^{ab}_c (since f^{ba}_c = -f^{ab}_c)
                    # Actually: d(a,b) puts 1 in nop(a,b), d(b,a) puts 1 in nop(a,b) + f^{ba}_c
                    # So diff = -f^{ba}_c = f^{ab}_c in mode-2 direction k
                    expected = -c[b, a, k]  # = c[a,b,k]
                    assert diff == expected, \
                        f"Commutator check fails at ({a},{b},{k}): {diff} != {expected}"


# ============================================================
# Master verification
# ============================================================

class TestMasterVerification:
    def test_full_resolution(self):
        """Complete verification that H^2_{h=2} = 0."""
        result = verify_no_weight2_contribution_to_h2()
        assert result["dim_B2_h2"] == 9
        assert result["dim_B1_h2"] == 9
        assert result["dim_B3_h2"] == 0
        assert result["differential_rank"] == 9
        assert result["H2_h2"] == 0
        assert result["is_isomorphism"] is True

    def test_consistency_with_ce(self):
        """H^2(bar) = H^2(CE) = 5, all at weight >= 3.

        Since H^2_{h=2} = 0 and H^2_{h=1} = 0 (trivially, B^2_{h=1} = 0),
        all of H^2 = 5 must come from weight >= 3.
        """
        assert h2_weight2() == 0
        assert bar_chain_dim(2, 1) == 0  # B^2_{h=1} = 0
        assert ce_h2_sl2() == 5

    def test_weight3_euler_char(self):
        """chi_3 = dim B^1_3 - dim B^2_3 + dim B^3_3 = 22 - 54 + 54 = 22."""
        assert weight3_euler_char() == 22

    def test_remark_error_diagnosis(self):
        """Explicitly verify what the old remark got wrong.

        Old claim: B^1_{h=2} = g_2, dim = 3 (WRONG, should be 9).
        Old claim: rank(d) = dim[g,g] = 3 (WRONG, rank is 9).
        Old claim: H^2_{h=2} = 9 - 3 = 6 (WRONG, should be 0).
        """
        # The old remark used dim 3 for B^1
        old_B1_dim = 3  # WRONG
        correct_B1_dim = dim_abar(2)  # 9
        assert correct_B1_dim == 9
        assert old_B1_dim != correct_B1_dim

        # The old remark used rank 3 for the differential
        old_rank = 3  # WRONG
        correct_rank = bar_differential_weight2_rank()
        assert correct_rank == 9
        assert old_rank != correct_rank

        # The old remark got H^2 = 6
        old_h2 = 6  # WRONG
        correct_h2 = h2_weight2()
        assert correct_h2 == 0
        assert old_h2 != correct_h2
