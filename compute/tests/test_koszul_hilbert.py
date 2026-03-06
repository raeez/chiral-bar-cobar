"""Tests for Koszul dual Hilbert series (koszul_hilbert.py).

Verifies:
1. Quadratic dual computation for known algebras
2. Koszul relation H_A(t) * H_{A!}(-t) = 1
3. Riordan and Motzkin recurrence implementations
"""

import pytest
import numpy as np


class TestQuadraticDual:
    """Test quadratic_dual_dims for known algebras."""

    def test_sym_sl2_dual_coalgebra(self):
        """Koszul dual COALGEBRA of Sym(sl₂) = S^n(V*): dims C(n+2,n).

        quadratic_dual_dims computes the coalgebra (subcoalgebra of cofree),
        not the algebra (quotient). For Sym(V) with d=3:
        coalgebra dims = C(n+2,n) = [1, 3, 6, 10, 15, 21, 28]."""
        from compute.lib.koszul_hilbert import sl2_relations, quadratic_dual_dims
        from math import comb
        d, R = sl2_relations()
        dims = quadratic_dual_dims(d, R, 6)
        expected = [comb(n + d - 1, n) for n in range(7)]
        assert dims == expected

    def test_free_algebra_dual(self):
        """Koszul dual of T(V) (no relations): [1, d, 0, 0, ...]."""
        from compute.lib.koszul_hilbert import quadratic_dual_dims
        d = 3
        R = np.zeros((0, d * d))
        dims = quadratic_dual_dims(d, R, 5)
        assert dims == [1, 3, 0, 0, 0, 0]

    def test_sym_d1_dual(self):
        """Koszul dual of Sym(V) with dim V = 1: Λ(V*) = [1, 1, 0, ...]."""
        from compute.lib.koszul_hilbert import quadratic_dual_dims
        d = 1
        # For Sym(V): relations = antisymmetric tensors = {a⊗b - b⊗a} = 0 for d=1
        R = np.zeros((0, 1))
        dims = quadratic_dual_dims(d, R, 4)
        assert dims == [1, 1, 0, 0, 0]

    def test_exterior_dual_coalgebra(self):
        """Koszul dual COALGEBRA of Λ(V) for dim V = 2.

        Λ(V) = T(V)/(S²V). R = S²V, R^⊥ = Λ²(V*).
        Coalgebra: fully antisymmetric tensors = Λ^n(V*).
        For d=2: dims [1, 2, 1, 0, 0, 0]."""
        from compute.lib.koszul_hilbert import quadratic_dual_dims
        d = 2
        R = []
        for i in range(d):
            for j in range(i, d):
                row = np.zeros(d * d)
                row[i * d + j] = 1
                row[j * d + i] += 1
                R.append(row)
        R = np.array(R)
        dims = quadratic_dual_dims(d, R, 5)
        from math import comb
        expected = [comb(d, n) for n in range(6)]
        assert dims == expected


class TestKoszulRelation:
    """Verify H_A(t) * H_{A!}(-t) = 1 for known pairs."""

    def test_sym_exterior_koszul(self):
        """Sym(V) and Λ(V*) satisfy the Koszul relation."""
        from compute.lib.koszul_hilbert import verify_koszul
        # Sym(k²): [1, 2, 3, 4, 5, ...]
        # Λ(k²): [1, 2, 1, 0, 0, ...]
        h_sym = [1, 2, 3, 4, 5, 6]
        h_ext = [1, 2, 1, 0, 0, 0]
        assert verify_koszul(h_sym, h_ext)


class TestRiordanMotzkin:
    """Test Riordan and Motzkin implementations."""

    def test_riordan_known_values(self):
        """Riordan numbers: 1, 0, 1, 1, 3, 6, 15, 36, 91, 232."""
        from compute.lib.koszul_hilbert import riordan
        expected = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232]
        for n, val in enumerate(expected):
            assert riordan(n) == val, f"R({n}) = {riordan(n)}, expected {val}"

    def test_motzkin_known_values(self):
        """Motzkin numbers: 1, 1, 2, 4, 9, 21, 51, 127, 323, 835."""
        from compute.lib.koszul_hilbert import motzkin
        expected = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835]
        for n, val in enumerate(expected):
            assert motzkin(n) == val, f"M({n}) = {motzkin(n)}, expected {val}"

    def test_sl2_bar_cohomology_matches_bar_complex(self):
        """sl₂ bar cohomology from koszul_hilbert matches bar_complex."""
        from compute.lib.koszul_hilbert import sl2_bar_cohomology
        from compute.lib.bar_complex import bar_dim_sl2
        h = sl2_bar_cohomology(10)
        for n in range(1, 11):
            assert h[n] == bar_dim_sl2(n), f"Mismatch at degree {n}"

    def test_virasoro_bar_cohomology_matches_bar_complex(self):
        """Virasoro bar cohomology from koszul_hilbert matches bar_complex."""
        from compute.lib.koszul_hilbert import virasoro_bar_cohomology
        from compute.lib.bar_complex import bar_dim_virasoro
        h = virasoro_bar_cohomology(10)
        for n in range(1, 11):
            assert h[n] == bar_dim_virasoro(n), f"Mismatch at degree {n}"

    def test_riordan_recurrence_identity(self):
        """(n+1)R(n) = (n-1)(2R(n-1) + 3R(n-2))."""
        from compute.lib.koszul_hilbert import riordan
        for n in range(2, 15):
            lhs = (n + 1) * riordan(n)
            rhs = (n - 1) * (2 * riordan(n - 1) + 3 * riordan(n - 2))
            assert lhs == rhs, f"Riordan recurrence fails at n={n}"

    def test_motzkin_recurrence_identity(self):
        """(n+3)M(n+1) = (2n+3)M(n) + 3nM(n-1)."""
        from compute.lib.koszul_hilbert import motzkin
        for n in range(1, 12):
            lhs = (n + 3) * motzkin(n + 1)
            rhs = (2 * n + 3) * motzkin(n) + 3 * n * motzkin(n - 1)
            assert lhs == rhs, f"Motzkin recurrence fails at n={n}"
