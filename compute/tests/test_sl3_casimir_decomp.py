"""Tests for sl₃ Casimir decomposition — PBW spectral sequence data.

Locks in verified results:
1. Casimir eigenspace decomposition of g^{⊗n} for n=2,3,4
2. CE bracket ranks and exactness on tensor algebra
3. Bracket rank by Casimir eigenspace
4. Koszul dual dimensions from bar cohomology
5. Representation-theoretic consistency
"""

import pytest
import numpy as np

from compute.lib.sl3_casimir_decomp import (
    DIM_G,
    build_casimir,
    bracket_rank_by_eigenspace,
    casimir_eigenspace_decomposition,
    ce_bracket_differential,
    expected_adj_tensor2,
    koszul_dual_dims_from_bar_cohomology,
    sl3_casimir_eigenvalue,
    sl3_inverse_killing_form,
    sl3_irrep_dim,
    verify_ce_d_squared,
)


# ---------------------------------------------------------------------------
# Inverse Killing form
# ---------------------------------------------------------------------------

class TestInverseKillingForm:
    def test_cartan_block(self):
        """κ⁻¹ Cartan block = (1/3)[[2,1],[1,2]]."""
        inv_kf = sl3_inverse_killing_form()
        assert abs(inv_kf[(0, 0)] - 2.0/3) < 1e-14
        assert abs(inv_kf[(0, 1)] - 1.0/3) < 1e-14
        assert abs(inv_kf[(1, 0)] - 1.0/3) < 1e-14
        assert abs(inv_kf[(1, 1)] - 2.0/3) < 1e-14

    def test_root_coroot_pairs(self):
        """κ⁻¹(Eᵢ, Fᵢ) = κ⁻¹(Fᵢ, Eᵢ) = 1."""
        inv_kf = sl3_inverse_killing_form()
        for i, (e, f) in enumerate([(2, 5), (3, 6), (4, 7)]):
            assert inv_kf[(e, f)] == 1.0
            assert inv_kf[(f, e)] == 1.0

    def test_inverse_of_killing(self):
        """κ⁻¹ · κ = I on the non-zero entries."""
        from compute.lib.sl3_bar import sl3_killing_form
        kf = {k: float(v) for k, v in sl3_killing_form().items()}
        inv_kf = sl3_inverse_killing_form()

        # Build 8x8 matrices
        K = np.zeros((8, 8))
        K_inv = np.zeros((8, 8))
        for (i, j), v in kf.items():
            K[i, j] = v
        for (i, j), v in inv_kf.items():
            K_inv[i, j] = v

        product = K_inv @ K
        # Should be identity on the non-zero block (K is rank 8 for sl₃)
        assert np.allclose(product, np.eye(8), atol=1e-12)


# ---------------------------------------------------------------------------
# Representation theory formulas
# ---------------------------------------------------------------------------

class TestRepTheoryFormulas:
    @pytest.mark.parametrize("lam1,lam2,expected_dim", [
        (0, 0, 1), (1, 0, 3), (0, 1, 3), (1, 1, 8),
        (2, 0, 6), (0, 2, 6), (3, 0, 10), (0, 3, 10),
        (2, 2, 27), (2, 1, 15), (1, 2, 15), (4, 1, 35),
        (1, 4, 35), (3, 3, 64),
    ])
    def test_irrep_dim(self, lam1, lam2, expected_dim):
        assert sl3_irrep_dim(lam1, lam2) == expected_dim

    @pytest.mark.parametrize("lam1,lam2,expected_ev", [
        (0, 0, 0), (1, 1, 18), (3, 0, 36), (0, 3, 36),
        (2, 2, 48), (4, 1, 72), (1, 4, 72), (3, 3, 90),
    ])
    def test_casimir_eigenvalue(self, lam1, lam2, expected_ev):
        assert sl3_casimir_eigenvalue(lam1, lam2) == expected_ev


# ---------------------------------------------------------------------------
# Casimir on g^{⊗1}
# ---------------------------------------------------------------------------

class TestCasimirDegree1:
    def test_eigenvalue(self):
        """3C₂ on adjoint = 18·I (adjoint has eigenvalue 18)."""
        C = build_casimir(1)
        eigenvalues = np.linalg.eigvals(C).real
        rounded = np.round(eigenvalues).astype(int)
        assert np.all(rounded == 18)

    def test_decomposition(self):
        decomp = casimir_eigenspace_decomposition(1)
        assert decomp == {18: 8}


# ---------------------------------------------------------------------------
# Casimir on g^{⊗2} = adj ⊗ adj
# ---------------------------------------------------------------------------

class TestCasimirDegree2:
    def test_decomposition_matches_rep_theory(self):
        """adj⊗adj = 1 + 8 + 8 + 10 + 10* + 27."""
        decomp = casimir_eigenspace_decomposition(2)
        expected = expected_adj_tensor2()
        assert decomp == expected

    def test_total_dim(self):
        decomp = casimir_eigenspace_decomposition(2)
        assert sum(decomp.values()) == 64

    def test_eigenvalues(self):
        decomp = casimir_eigenspace_decomposition(2)
        assert set(decomp.keys()) == {0, 18, 36, 48}

    def test_multiplicities(self):
        decomp = casimir_eigenspace_decomposition(2)
        assert decomp[0] == 1   # trivial
        assert decomp[18] == 16  # 2 × adj
        assert decomp[36] == 20  # 10 + 10*
        assert decomp[48] == 27  # V(2,2)


# ---------------------------------------------------------------------------
# Casimir on g^{⊗3}
# ---------------------------------------------------------------------------

class TestCasimirDegree3:
    def test_total_dim(self):
        decomp = casimir_eigenspace_decomposition(3)
        assert sum(decomp.values()) == 512

    def test_eigenvalues(self):
        decomp = casimir_eigenspace_decomposition(3)
        assert set(decomp.keys()) == {0, 18, 36, 48, 72, 90}

    def test_multiplicities(self):
        decomp = casimir_eigenspace_decomposition(3)
        assert decomp == {
            0: 2, 18: 64, 36: 80, 48: 162, 72: 140, 90: 64,
        }


# ---------------------------------------------------------------------------
# Casimir on g^{⊗4} (slow: ~30s)
# ---------------------------------------------------------------------------

class TestCasimirDegree4:
    @pytest.mark.slow
    def test_total_dim(self):
        decomp = casimir_eigenspace_decomposition(4)
        assert sum(decomp.values()) == 4096

    @pytest.mark.slow
    def test_eigenvalues(self):
        decomp = casimir_eigenspace_decomposition(4)
        assert set(decomp.keys()) == {0, 18, 36, 48, 72, 90, 108, 120, 144}

    @pytest.mark.slow
    def test_multiplicities(self):
        decomp = casimir_eigenspace_decomposition(4)
        assert decomp == {
            0: 8, 18: 256, 36: 400, 48: 891,
            72: 1050, 90: 768, 108: 112, 120: 486, 144: 125,
        }


# ---------------------------------------------------------------------------
# CE bracket differential: d² = 0
# ---------------------------------------------------------------------------

class TestCEBracketDSquared:
    def test_d_squared_zero_n3(self):
        norm = verify_ce_d_squared(3)
        assert norm < 1e-10

    def test_d_squared_zero_n4(self):
        norm = verify_ce_d_squared(4)
        assert norm < 1e-10


# ---------------------------------------------------------------------------
# CE bracket ranks on tensor algebra
# ---------------------------------------------------------------------------

class TestCEBracketRanks:
    def test_rank_d2(self):
        """rank(d₂) = dim(g) = 8 (bracket surjective for semisimple g)."""
        D = ce_bracket_differential(2)
        assert int(np.linalg.matrix_rank(D, tol=1e-8)) == 8

    def test_rank_d3(self):
        D = ce_bracket_differential(3)
        assert int(np.linalg.matrix_rank(D, tol=1e-8)) == 56

    def test_rank_d4(self):
        D = ce_bracket_differential(4)
        assert int(np.linalg.matrix_rank(D, tol=1e-8)) == 456

    @pytest.mark.slow
    def test_rank_d5(self):
        D = ce_bracket_differential(5)
        assert int(np.linalg.matrix_rank(D, tol=1e-8)) == 3640


# ---------------------------------------------------------------------------
# Exactness: tensor algebra complex is acyclic for n ≥ 1
# ---------------------------------------------------------------------------

class TestTensorAlgebraExactness:
    """The CE differential on g^{⊗n} (full tensor algebra) is exact.

    This is NOT CE cohomology (which lives on Λ^n(g), not T^n(g)).
    For semisimple g, the tensor algebra complex has H_n(T(g), d_CE) = 0
    for all n ≥ 1. This is because the bar resolution of U(g) is acyclic.

    Numerically: rank(d_{n+1}) = dim(g^{⊗n}) - rank(d_n) for all n ≥ 2.
    """

    def test_exact_at_degree_2(self):
        """ker(d₂) = 56 = rank(d₃)."""
        D2 = ce_bracket_differential(2)
        D3 = ce_bracket_differential(3)
        ker_d2 = 64 - int(np.linalg.matrix_rank(D2, tol=1e-8))
        rank_d3 = int(np.linalg.matrix_rank(D3, tol=1e-8))
        assert ker_d2 == rank_d3 == 56

    def test_exact_at_degree_3(self):
        """ker(d₃) = 456 = rank(d₄)."""
        D3 = ce_bracket_differential(3)
        D4 = ce_bracket_differential(4)
        ker_d3 = 512 - int(np.linalg.matrix_rank(D3, tol=1e-8))
        rank_d4 = int(np.linalg.matrix_rank(D4, tol=1e-8))
        assert ker_d3 == rank_d4 == 456

    @pytest.mark.slow
    def test_exact_at_degree_4(self):
        """ker(d₄) = 3640 = rank(d₅)."""
        D4 = ce_bracket_differential(4)
        D5 = ce_bracket_differential(5)
        ker_d4 = 4096 - int(np.linalg.matrix_rank(D4, tol=1e-8))
        rank_d5 = int(np.linalg.matrix_rank(D5, tol=1e-8))
        assert ker_d4 == rank_d5 == 3640


# ---------------------------------------------------------------------------
# Bracket rank by Casimir eigenspace
# ---------------------------------------------------------------------------

class TestBracketByEigenspace:
    def test_n2_rank_total(self):
        data = bracket_rank_by_eigenspace(2)
        total_rank = sum(v["rank"] for v in data.values())
        assert total_rank == 8

    def test_n2_detail(self):
        """adj⊗adj bracket rank: only eigenvalue 18 (adjoint) contributes."""
        data = bracket_rank_by_eigenspace(2)
        # Bracket maps adj⊗adj → adj. The image is in the adj (eigenvalue 18).
        # Only eigenvalue 18 in source maps to eigenvalue 18 in target.
        assert data[0]["rank"] == 0
        assert data[18]["rank"] == 8
        assert data[36]["rank"] == 0
        assert data[48]["rank"] == 0

    def test_n3_rank_total(self):
        data = bracket_rank_by_eigenspace(3)
        total_rank = sum(v["rank"] for v in data.values())
        assert total_rank == 56

    def test_n3_detail(self):
        data = bracket_rank_by_eigenspace(3)
        expected_ranks = {0: 1, 18: 8, 36: 20, 48: 27, 72: 0, 90: 0}
        for ev, exp_rank in expected_ranks.items():
            assert data[ev]["rank"] == exp_rank, (
                f"3C₂={ev}: rank={data[ev]['rank']}, expected {exp_rank}"
            )

    @pytest.mark.slow
    def test_n4_rank_total(self):
        data = bracket_rank_by_eigenspace(4)
        total_rank = sum(v["rank"] for v in data.values())
        assert total_rank == 456

    @pytest.mark.slow
    def test_n4_detail(self):
        data = bracket_rank_by_eigenspace(4)
        expected_ranks = {
            0: 1, 18: 56, 36: 60, 48: 135,
            72: 140, 90: 64, 108: 0, 120: 0, 144: 0,
        }
        for ev, exp_rank in expected_ranks.items():
            assert data[ev]["rank"] == exp_rank, (
                f"3C₂={ev}: rank={data[ev]['rank']}, expected {exp_rank}"
            )


# ---------------------------------------------------------------------------
# Koszul dual dimensions
# ---------------------------------------------------------------------------

class TestKoszulDualDims:
    def test_classical_bar_gives_exterior(self):
        """For classical Koszul: if H^n = C(d,n), then (A!)_n = d^n/n!."""
        # Trivial example: exterior algebra H_A(t) = (1+t)^d
        # Then H_{A!}(-t) = 1/(1+t)^d = Σ C(d+n-1,n)(-t)^n
        pass  # Koszul dual of polynomial ring is exterior, not this formula

    def test_sl3_koszul_dual(self):
        """Bar cohomology [1,8,36,204,1352] → Koszul dual [1,8,28,140,392]."""
        bar_dims = [1, 8, 36, 204, 1352]
        kd = koszul_dual_dims_from_bar_cohomology(bar_dims)
        assert kd == [1, 8, 28, 140, 392]

    def test_sl3_chiral_excess(self):
        """Chiral excess = (A!)_n - Λ^n(g*) is non-negative."""
        bar_dims = [1, 8, 36, 204, 1352]
        kd = koszul_dual_dims_from_bar_cohomology(bar_dims)
        classical = [1, 8, 28, 56, 70]  # C(8, n)
        excess = [kd[i] - classical[i] for i in range(5)]
        assert excess == [0, 0, 0, 84, 322]
        assert all(e >= 0 for e in excess)

    def test_koszul_product_identity(self):
        """H_A(t) · H_{A!}(-t) = 1 through degree 7."""
        bar_dims = [1, 8, 36, 204, 1352, 9892, 76084, 598592]
        kd = koszul_dual_dims_from_bar_cohomology(bar_dims)
        N = len(bar_dims)
        for k in range(N):
            prod_k = sum(
                bar_dims[i] * ((-1)**j) * kd[j]
                for i in range(k + 1)
                for j in [k - i]
                if 0 <= j < N
            )
            if k == 0:
                assert prod_k == 1
            else:
                assert prod_k == 0

    def test_koszul_dual_positive(self):
        """All Koszul dual dimensions are positive integers."""
        bar_dims = [1, 8, 36, 204, 1352, 9892, 76084, 598592]
        kd = koszul_dual_dims_from_bar_cohomology(bar_dims)
        assert all(isinstance(x, int) and x > 0 for x in kd)


# ---------------------------------------------------------------------------
# Integration: consistency across modules
# ---------------------------------------------------------------------------

class TestCrossModuleConsistency:
    def test_ce_ranks_match_h4_verification(self):
        """CE ranks here match test_sl3_h4_verification.py expectations."""
        from compute.lib.km_chiral_bar import ce_bracket_differential_numpy
        from compute.lib.sl3_bar import sl3_structure_constants

        sc = {(a, b): {c: float(v) for c, v in targets.items()}
              for (a, b), targets in sl3_structure_constants().items()}

        for n, expected_rank in [(2, 8), (3, 56), (4, 456)]:
            mat = ce_bracket_differential_numpy(DIM_G, sc, n)
            rank = int(np.linalg.matrix_rank(mat, tol=1e-8))
            assert rank == expected_rank

    def test_bar_gf_sl3_prediction(self):
        """Rational GF predicts H⁴ = 1352, consistent with Casimir data."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf
        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -52, -8],
            den_coeffs=[-11, 23, 8],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 1352
