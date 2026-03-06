"""Tests for compute/lib/bar_modular.py — modular arithmetic infrastructure.

Tests OS algebra dimensions, CE cohomology of sl_3, and sl_3 structure constants.
"""

import pytest
import numpy as np
from math import comb

from compute.lib.bar_modular import (
    nbc_basis,
    os_dimension,
    bar_dimension,
    bracket_mod_p,
    killing_mod_p,
    ce_differential_mod_p,
    matrix_rank_mod_p,
    ce_cohomology_dims_mod_p,
    verify_d_squared_ce,
    DIM_G,
    H1, H2, E1, E2, E3, F1, F2, F3,
)


# ===== Orlik-Solomon / NBC basis =====

class TestNBCBasis:
    """NBC basis dimensions = unsigned Stirling numbers of the first kind."""

    def test_os_degree_0(self):
        """OS^0(n) = 1 for all n >= 1."""
        for n in range(1, 6):
            assert os_dimension(n, 0) == 1

    def test_os_top_degree(self):
        """OS^{n-1}(n) = (n-1)! for the complete graph K_n."""
        expected = {1: 1, 2: 1, 3: 2, 4: 6, 5: 24, 6: 120}
        for n, val in expected.items():
            assert os_dimension(n, n - 1) == val, f"OS^{n-1}({n})"

    def test_os_middle_degrees(self):
        """Spot-check OS^k(n) for small n, k."""
        # OS^1(3) = 3 (three edges, no broken circuit constraint at degree 1)
        assert os_dimension(3, 1) == 3
        # OS^1(4) = 6 = C(4,2) - 4 broken circuits... actually
        # OS^1(n) = C(n,2) - |broken circuits of size 1| = n(n-1)/2
        # No, OS^1(n) for the braid arrangement has dim = C(n,2) at degree 1
        # because broken circuits have size >= 2.
        assert os_dimension(4, 1) == 6
        # OS^2(4) = 11 (unsigned Stirling |s(4,2)| = 11)
        assert os_dimension(4, 2) == 11


# ===== Bar complex dimensions =====

class TestBarDimensions:
    """Bar chain space dimensions = dim(g)^n * OS^{n-1}(n)."""

    def test_bar_degree_1(self):
        assert bar_dimension(1) == 8

    def test_bar_degree_2(self):
        assert bar_dimension(2) == 64

    def test_bar_degree_3(self):
        assert bar_dimension(3) == 8**3 * 2  # 1024

    def test_bar_degree_4(self):
        assert bar_dimension(4) == 8**4 * 6  # 24576


# ===== sl_3 structure constants =====

class TestStructureConstants:
    """Verify sl_3 Lie bracket and Killing form."""

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_bracket_antisymmetry(self, p):
        """[a,b] = -[b,a] for all generators."""
        for a in range(DIM_G):
            for b in range(DIM_G):
                ab = {c: v for c, v in bracket_mod_p(a, b, p)}
                ba = {c: v for c, v in bracket_mod_p(b, a, p)}
                for c in set(list(ab.keys()) + list(ba.keys())):
                    assert (ab.get(c, 0) + ba.get(c, 0)) % p == 0, \
                        f"[{a},{b}] + [{b},{a}] != 0 at gen {c}"

    def test_cartan_on_roots(self):
        """[H1, E1] = 2*E1, [H1, E2] = -E2."""
        terms = bracket_mod_p(H1, E1, 7)
        assert terms == [(E1, 2)]
        terms = bracket_mod_p(H1, E2, 7)
        assert terms == [(E2, 7 - 1)]  # -1 mod 7 = 6

    def test_serre_relation(self):
        """[E1, E2] = E3."""
        terms = bracket_mod_p(E1, E2, 7)
        assert terms == [(E3, 1)]

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_killing_symmetry(self, p):
        """(a,b) = (b,a)."""
        for a in range(DIM_G):
            for b in range(DIM_G):
                assert killing_mod_p(a, b, p) == killing_mod_p(b, a, p)

    def test_killing_values(self):
        """Spot-check Killing form values."""
        assert killing_mod_p(H1, H1, 7) == 2
        assert killing_mod_p(H1, H2, 7) == 7 - 1  # -1 mod 7
        assert killing_mod_p(E1, F1, 7) == 1
        assert killing_mod_p(E1, E1, 7) == 0


# ===== CE differential =====

class TestCEDifferential:
    """Chevalley-Eilenberg differential d^2 = 0 and cohomology."""

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_d_squared_zero(self, p):
        """d^2 = 0 at every degree."""
        for k in range(8):
            assert verify_d_squared_ce(k, p), f"d^2 != 0 at degree {k} mod {p}"

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_ce_dimensions(self, p):
        """Chain space dims = C(8, k)."""
        for k in range(9):
            D = ce_differential_mod_p(k, p) if k <= 8 else None
            if D is not None:
                rows, cols = D.shape
                assert cols == comb(8, k), f"C^{k} dim wrong"
                assert rows == comb(8, k + 1), f"C^{k+1} dim wrong"

    @pytest.mark.parametrize("p", [5, 7, 11])
    def test_ce_cohomology_sl3(self, p):
        """H*(sl_3) = Lambda(x_3, x_5): dims 1,0,0,1,0,1,0,0,1."""
        expected = {0: 1, 1: 0, 2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 0, 8: 1}
        dims = ce_cohomology_dims_mod_p(p, max_degree=8)
        for k, exp in expected.items():
            assert dims[k] == exp, f"H^{k}(sl_3) mod {p}: got {dims[k]}, expected {exp}"


# ===== Gaussian elimination =====

class TestGaussianElimination:
    def test_identity(self):
        M = np.eye(5, dtype=np.int64)
        assert matrix_rank_mod_p(M, 7) == 5

    def test_zero(self):
        M = np.zeros((3, 4), dtype=np.int64)
        assert matrix_rank_mod_p(M, 7) == 0

    def test_rank_deficient(self):
        M = np.array([[1, 2, 3], [2, 4, 6], [1, 0, 1]], dtype=np.int64)
        assert matrix_rank_mod_p(M, 7) == 2

    def test_mod_p_matters(self):
        """Matrix with rank depending on characteristic."""
        # [3, 0; 0, 3] has rank 2 mod 5, rank 0 mod 3
        M = np.array([[3, 0], [0, 3]], dtype=np.int64)
        assert matrix_rank_mod_p(M, 5) == 2
        assert matrix_rank_mod_p(M, 3) == 0
