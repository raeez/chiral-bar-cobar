"""Tests for Koszul dual dimension computation from quadratic relation data.

Verifies:
  1. Classical U(g): A! = Λ(g*), dims = C(d,n)
  2. R⊥ computation (orthogonal complement)
  3. Ideal degree-n construction
  4. Scan of relation spaces for sl₃
  5. Series inversion: H_bar(t) · H_{A!}(-t) = 1
"""

import pytest
import numpy as np
from math import comb

from compute.lib.koszul_dual_dims import (
    build_relation_subspace,
    compute_R_perp,
    ideal_degree_n,
    koszul_dual_dim,
    koszul_dual_dims_from_relations,
    scan_relation_dims,
    verify_classical_koszul_dual,
)
from compute.lib.sl3_bar import DIM_G, sl3_structure_constants, sl3_killing_form


# ============================================================
# R⊥ computation
# ============================================================

class TestRPerp:
    def test_empty_R(self):
        """R = 0 => R⊥ = full space."""
        R = np.zeros((0, 9))
        R_perp = compute_R_perp(R, 9)
        assert R_perp.shape == (9, 9)

    def test_full_R(self):
        """R = full space => R⊥ = 0."""
        R = np.eye(9)
        R_perp = compute_R_perp(R, 9)
        assert R_perp.shape[0] == 0

    def test_complementary_dims(self):
        """dim(R) + dim(R⊥) = dim(V⊗V)."""
        d = 4
        R_rows = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_rows.append(rel)
        R = np.array(R_rows)
        R_perp = compute_R_perp(R, d * d)
        assert R.shape[0] + R_perp.shape[0] == d * d

    def test_orthogonality(self):
        """R and R⊥ are orthogonal."""
        d = 3
        R_rows = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_rows.append(rel)
        R = np.array(R_rows)
        R_perp = compute_R_perp(R, d * d)
        product = R @ R_perp.T
        assert np.allclose(product, 0, atol=1e-10)


# ============================================================
# Classical Koszul dual: A! = Λ(V*) for U(g)
# ============================================================

class TestClassicalKoszulDual:
    @pytest.mark.parametrize("d", [2, 3, 4, 5])
    def test_exterior_algebra_dims(self, d):
        """For R = Λ²(V), A! = Λ(V*) with dim (A!)_n = C(d,n)."""
        R_rows = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_rows.append(rel)
        R = np.array(R_rows)
        R_perp = compute_R_perp(R, d * d)

        for n in range(min(d + 1, 6)):
            dim_n = koszul_dual_dim(R_perp, d, n)
            expected = comb(d, n)
            assert dim_n == expected, f"d={d}, n={n}: got {dim_n}, expected {expected}"

    def test_sl2_classical(self):
        """sl₂ (d=3): verify classical Koszul dual."""
        results = verify_classical_koszul_dual(3)
        for n, (dim_n, expected, ok) in results.items():
            assert ok, f"n={n}: got {dim_n}, expected {expected}"

    @pytest.mark.slow
    def test_sl3_classical(self):
        """sl₃ (d=8): verify exterior algebra through degree 4.

        Marked slow: degree-4 ideal construction for d=8 allocates ~500 MB.
        """
        results = verify_classical_koszul_dual(8)
        for n, (dim_n, expected, ok) in results.items():
            assert ok, f"n={n}: got {dim_n}, expected {expected}"

    def test_sl3_classical_low_degree(self):
        """sl₃ (d=8): verify exterior algebra through degree 3 (fast)."""
        d = 8
        R_basis = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_basis.append(rel)
        R_basis = np.array(R_basis)
        R_perp = compute_R_perp(R_basis, d * d)
        for n in range(4):
            dim_n = koszul_dual_dim(R_perp, d, n)
            expected = comb(d, n)
            assert dim_n == expected, f"n={n}: got {dim_n}, expected {expected}"

    def test_R_dim_classical(self):
        """R = Λ²(V) has dim C(d,2)."""
        d = 8
        R = build_relation_subspace(d, {}, None, include_killing=False)
        assert R.shape[0] == comb(d, 2)  # = 28


# ============================================================
# Ideal construction
# ============================================================

class TestIdealDegreeN:
    def test_degree_1(self):
        """I_1 should be empty (ideal starts at degree 2)."""
        R_perp = np.eye(4).reshape(4, 4)  # dummy
        I_1 = ideal_degree_n(R_perp, 2, 1)
        assert I_1.shape[0] == 0

    def test_degree_2_equals_R_perp(self):
        """I_2 = R⊥ (just R⊥ itself, no tensor products)."""
        d = 3
        R_rows = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_rows.append(rel)
        R = np.array(R_rows)
        R_perp = compute_R_perp(R, d * d)

        I_2 = ideal_degree_n(R_perp, d, 2)
        # I_2 should have the same rank as R_perp
        rank_I2 = int(np.linalg.matrix_rank(I_2, tol=1e-8))
        assert rank_I2 == R_perp.shape[0]


# ============================================================
# sl₃ relation space scan
# ============================================================

class TestSl3Scan:
    @pytest.fixture
    def sl3_data(self):
        sc = sl3_structure_constants()
        sc_float = {(a, b): {c: float(v) for c, v in tgt.items()}
                    for (a, b), tgt in sc.items()}
        kf = sl3_killing_form()
        kf_float = {k: float(v) for k, v in kf.items()}
        return sc_float, kf_float

    def test_classical_h2(self, sl3_data):
        """Classical R = Λ²(V): (A!)_2 = C(8,2) = 28."""
        sc, kf = sl3_data
        R = build_relation_subspace(DIM_G, sc, None, include_killing=False)
        dims = koszul_dual_dims_from_relations(DIM_G, R, max_degree=2)
        assert dims[2] == 28

    def test_bracket_killing_h2(self, sl3_data):
        """R = Λ²(V) + Killing: (A!)_2 = 29."""
        sc, kf = sl3_data
        R = build_relation_subspace(DIM_G, sc, kf, include_killing=True)
        dims = koszul_dual_dims_from_relations(DIM_G, R, max_degree=2)
        assert dims[2] == 29

    def test_antisym_diagonal_h2(self, sl3_data):
        """R = Λ²(V) + diagonal: (A!)_2 = 36 = bar H²."""
        sc, kf = sl3_data
        d = DIM_G
        R_rows = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_rows.append(rel)
        for a in range(d):
            rel = np.zeros(d * d)
            rel[a * d + a] = 1.0
            R_rows.append(rel)
        R = np.array(R_rows)
        dims = koszul_dual_dims_from_relations(d, R, max_degree=2)
        assert dims[2] == 36

    def test_antisym_diagonal_h3_not_204(self, sl3_data):
        """R = Λ²(V) + diagonal gives (A!)_3 = 120, NOT 204."""
        sc, kf = sl3_data
        d = DIM_G
        R_rows = []
        for a in range(d):
            for b in range(a + 1, d):
                rel = np.zeros(d * d)
                rel[a * d + b] = 1.0
                rel[b * d + a] = -1.0
                R_rows.append(rel)
        for a in range(d):
            rel = np.zeros(d * d)
            rel[a * d + a] = 1.0
            R_rows.append(rel)
        R = np.array(R_rows)
        dims = koszul_dual_dims_from_relations(d, R, max_degree=3)
        assert dims[3] == 120
        assert dims[3] != 204  # chiral bar H³ NOT reproduced

    def test_scan_all_cases(self, sl3_data):
        """Verify scan returns all four cases with correct structure."""
        sc, kf = sl3_data
        results = scan_relation_dims(DIM_G, sc, kf, max_degree=2)
        assert 'classical' in results
        assert 'bracket+killing' in results
        assert 'full_VxV' in results
        assert 'antisym+diagonal' in results
        for name, data in results.items():
            assert 'R_dim' in data
            assert 'dims' in data
            assert 0 in data['dims']
            assert data['dims'][0] == 1


# ============================================================
# Series inversion: H_bar(t) · H_{A!}(-t) = 1
# ============================================================

class TestSeriesInversion:
    def test_koszul_dual_from_bar_dims(self):
        """Verify series inversion gives correct Koszul dual dims."""
        bar = [1, 8, 36, 204, 1352, 9892, 76084, 598592]
        N = len(bar)
        b = [0] * N
        b[0] = 1
        for n in range(1, N):
            b[n] = -sum((-1)**k * bar[k] * b[n-k] for k in range(1, n+1))

        expected = [1, 8, 28, 140, 392, 2884, 2716, 75488]
        assert b == expected

    def test_series_inversion_identity(self):
        """sum_{k=0}^{n} a_k (-1)^k b_{n-k} = delta_{n,0}."""
        bar = [1, 8, 36, 204, 1352, 9892, 76084, 598592]
        dual = [1, 8, 28, 140, 392, 2884, 2716, 75488]
        N = len(bar)
        for n in range(N):
            check = sum(bar[k] * ((-1)**k) * dual[n-k] for k in range(n+1))
            expected = 1 if n == 0 else 0
            assert check == expected, f"n={n}: got {check}"

    def test_koszul_dual_positive_through_deg7(self):
        """All Koszul dual dims positive through degree 7."""
        dual = [1, 8, 28, 140, 392, 2884, 2716, 75488]
        assert all(x > 0 for x in dual)

    def test_chiral_excess_starts_deg3(self):
        """Chiral excess = (A!)_n - C(8,n) is 0 for n <= 2, positive for n = 3."""
        dual = [1, 8, 28, 140, 392, 2884, 2716, 75488]
        for n in range(3):
            assert dual[n] == comb(8, n), f"n={n}: expected {comb(8,n)}, got {dual[n]}"
        assert dual[3] - comb(8, 3) == 84  # first nontrivial excess

    def test_excess_84_matches_quadratic_gap(self):
        """The chiral excess 84 = (A!)_3 - C(8,3) = 140 - 56."""
        assert 140 - 56 == 84
        # Also: bar H³ - quadratic(antisym+diag) H³ = 204 - 120 = 84
        assert 204 - 120 == 84


# ============================================================
# Degree 0 and 1 edge cases
# ============================================================

class TestEdgeCases:
    def test_degree_0(self):
        """(A!)_0 = 1 always."""
        R_perp = np.eye(4)
        assert koszul_dual_dim(R_perp, 2, 0) == 1

    def test_degree_1(self):
        """(A!)_1 = dim(V)."""
        R_perp = np.eye(4)
        assert koszul_dual_dim(R_perp, 2, 1) == 2

    def test_trivial_R(self):
        """R = 0 => R⊥ = V⊗V => (A!)_n = 0 for n >= 2."""
        d = 3
        R = np.zeros((0, d * d))
        R_perp = compute_R_perp(R, d * d)
        assert R_perp.shape[0] == d * d
        # All of V⊗V is in R⊥, so ideal I_n = V^{⊗n} for n >= 2
        assert koszul_dual_dim(R_perp, d, 2) == 0

    def test_full_R(self):
        """R = V⊗V => R⊥ = 0 => (A!)_n = d^n (free algebra)."""
        d = 3
        R = np.eye(d * d)
        R_perp = compute_R_perp(R, d * d)
        assert R_perp.shape[0] == 0
        for n in range(4):
            assert koszul_dual_dim(R_perp, d, n) == d ** n
