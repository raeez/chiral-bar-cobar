"""Tests for MC4 Yangian residue extraction and three-layer verification.

Verifies:
  - Permutation matrix P and Yang R-matrix R(u) = Id - hbar*P/u
  - Three-layer reduction (residue, channel, single-line) for M=2,3,4
  - Yang-Baxter equation
  - L-mode structure in evaluation representation
  - RTT truncation defect: interior zero, boundary nonzero
  - Defect scaling and algebraic structure
"""

import pytest
import numpy as np

from compute.lib.yangian_residue import (
    permutation_matrix,
    yang_r_matrix,
    sym_antisym_projectors,
    sym_dim,
    alt_dim,
    evaluation_line_operator,
    evaluation_L_mode,
    residue_at_a,
    e_tensor,
    verify_residue_reduction,
    verify_channel_reduction,
    verify_single_line_reduction,
    verify_all_reductions,
    verify_rll_relation,
    verify_rtt_l_modes,
    verify_rtt_truncation,
    rtt_mode_defect,
    rtt_mode_defect_norm,
    _eval_T_ij_mode,
    truncated_rtt_defect_eval,
    verify_mc4_yangian,
)


# ===== Permutation matrix =====

class TestPermutationMatrix:
    def test_P_squared_is_identity(self):
        """P^2 = Id on V tensor V."""
        for M in [2, 3, 4]:
            P = permutation_matrix(M)
            assert np.allclose(P @ P, np.eye(M * M))

    def test_P_eigenvalues(self):
        """P has eigenvalues +1 (dim M(M+1)/2) and -1 (dim M(M-1)/2)."""
        for M in [2, 3, 4]:
            P = permutation_matrix(M)
            eigs = np.linalg.eigvalsh(P)
            n_plus = np.sum(np.abs(eigs - 1) < 1e-10)
            n_minus = np.sum(np.abs(eigs + 1) < 1e-10)
            assert n_plus == sym_dim(M)
            assert n_minus == alt_dim(M)

    def test_P_trace(self):
        """Tr(P) = M (trace over V tensor V)."""
        for M in [2, 3, 4]:
            P = permutation_matrix(M)
            assert abs(np.trace(P) - M) < 1e-10

    def test_P_swaps_tensor(self):
        """P(e_i tensor e_j) = e_j tensor e_i."""
        M = 3
        P = permutation_matrix(M)
        for i in range(M):
            for j in range(M):
                v = e_tensor(M, i, j)
                Pv = P @ v
                expected = e_tensor(M, j, i)
                assert np.allclose(Pv, expected)


# ===== Yang R-matrix =====

class TestYangRMatrix:
    def test_R_at_infinity(self):
        """R(u) -> Id as u -> infinity."""
        for M in [2, 3]:
            R = yang_r_matrix(M, 1e10)
            assert np.allclose(R, np.eye(M * M), atol=1e-8)

    def test_R_residue_at_zero(self):
        """Res_{u=0} R(u) = -hbar*P."""
        for M in [2, 3]:
            P = permutation_matrix(M)
            eps = 1e-10
            R_near = yang_r_matrix(M, eps)
            res = eps * (R_near - np.eye(M * M))
            assert np.allclose(res, -P, atol=1e-6)

    def test_R_unitarity(self):
        """R(u)R(-u) = (1 - hbar^2/u^2) * Id (unitarity)."""
        for M in [2, 3]:
            u = 3.7
            R_plus = yang_r_matrix(M, u)
            R_minus = yang_r_matrix(M, -u)
            product = R_plus @ R_minus
            expected = (1 - 1.0 / u ** 2) * np.eye(M * M)
            assert np.allclose(product, expected)


# ===== Projectors =====

class TestProjectors:
    def test_projector_sum(self):
        """P_sym + P_alt = Id."""
        for M in [2, 3, 4]:
            P_sym, P_alt = sym_antisym_projectors(M)
            assert np.allclose(P_sym + P_alt, np.eye(M * M))

    def test_projector_idempotent(self):
        """P_sym^2 = P_sym, P_alt^2 = P_alt."""
        for M in [2, 3]:
            P_sym, P_alt = sym_antisym_projectors(M)
            assert np.allclose(P_sym @ P_sym, P_sym)
            assert np.allclose(P_alt @ P_alt, P_alt)

    def test_projector_orthogonal(self):
        """P_sym * P_alt = 0."""
        for M in [2, 3]:
            P_sym, P_alt = sym_antisym_projectors(M)
            assert np.allclose(P_sym @ P_alt, np.zeros((M * M, M * M)))

    def test_projector_ranks(self):
        """rank(P_sym) = M(M+1)/2, rank(P_alt) = M(M-1)/2."""
        for M in [2, 3, 4]:
            P_sym, P_alt = sym_antisym_projectors(M)
            assert abs(np.trace(P_sym) - sym_dim(M)) < 1e-10
            assert abs(np.trace(P_alt) - alt_dim(M)) < 1e-10


# ===== Three-layer reduction =====

class TestResidueReduction:
    """Layer 1: Res_{u=a} L_a(u) = -hbar*P (cor:dg-shifted-rtt-typea-residue-reduction)."""

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_residue_equals_minus_hbar_P(self, M):
        results = verify_residue_reduction(M)
        assert results["Xi_equals_minus_hbar_P"]

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_numeric_residue(self, M):
        results = verify_residue_reduction(M)
        for key, val in results.items():
            if key.startswith("numeric_residue"):
                assert val, f"{key} failed for M={M}"


class TestChannelReduction:
    """Layer 2: Xi|_{Sym^2} = -hbar, Xi|_{Lambda^2} = +hbar."""

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_sym_eigenvalue(self, M):
        results = verify_channel_reduction(M)
        assert results["Xi_sym_check"]
        assert results["Xi_sym_eigenvalue"] == -1.0

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_alt_eigenvalue(self, M):
        results = verify_channel_reduction(M)
        assert results["Xi_alt_check"]
        assert results["Xi_alt_eigenvalue"] == 1.0


class TestSingleLineReduction:
    """Layer 3: Xi(e1 x e2) = -hbar(e2 x e1)."""

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_single_line(self, M):
        results = verify_single_line_reduction(M)
        assert results["match"]

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_inverse_direction(self, M):
        results = verify_single_line_reduction(M)
        assert results["Xi(e2xe1)_equals_minus_hbar_e1xe2"]

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_diagonal_symmetric(self, M):
        results = verify_single_line_reduction(M)
        assert results["Xi(e1xe1)_equals_minus_hbar_e1xe1"]


# ===== Yang-Baxter equation =====

class TestYangBaxter:
    """R12(u-v) R13(u-a) R23(v-a) = R23(v-a) R13(u-a) R12(u-v)."""

    @pytest.mark.parametrize("M", [2, 3])
    def test_ybe_generic_params(self, M):
        result = verify_rll_relation(M, 3.7, 1.2, 0.5)
        assert result["ybe_holds"]
        assert result["max_diff"] < 1e-12

    @pytest.mark.parametrize("M", [2, 3])
    def test_ybe_different_params(self, M):
        result = verify_rll_relation(M, 5.1, 2.3, 0.7)
        assert result["ybe_holds"]

    def test_ybe_sl4(self):
        result = verify_rll_relation(4, 4.0, 2.0, 1.0)
        assert result["ybe_holds"]


# ===== L-mode structure =====

class TestLModes:
    def test_L0_is_identity(self):
        """L^{(0)} = Id_{M^2}."""
        for M in [2, 3]:
            L0 = evaluation_L_mode(M, 0, 1.5)
            assert np.allclose(L0, np.eye(M * M))

    def test_Lr_proportional_to_P(self):
        """L^{(r)} = -hbar*a^{r-1}*P for r >= 1."""
        M, a = 2, 2.0
        P = permutation_matrix(M)
        for r in range(1, 5):
            Lr = evaluation_L_mode(M, r, a)
            expected = -(a ** (r - 1)) * P
            assert np.allclose(Lr, expected)

    @pytest.mark.parametrize("M", [2, 3])
    def test_mode_reconstruction(self, M):
        """sum L^{(r)} u^{-r} approximates L(u) = Id - P/(u-a)."""
        result = verify_rtt_l_modes(M, 5, 1.0)
        assert result["mode_structure_correct"]
        assert result["error_within_bound"]


# ===== RTT truncation defect =====

class TestRTTTruncation:
    @pytest.mark.parametrize("M", [2, 3])
    def test_interior_zero(self, M):
        """RTT defect is zero for interior modes (r < N and s < N)."""
        result = verify_rtt_truncation(M, 3, a=1.5)
        assert result["interior_zero"]

    @pytest.mark.parametrize("M", [2, 3])
    def test_boundary_nonzero(self, M):
        """RTT defect is nonzero at boundary modes."""
        result = verify_rtt_truncation(M, 3, a=1.5)
        assert result["boundary_nonzero"]

    def test_defect_scaling(self):
        """Defect at (N, s) scales as a^{N+s-1}."""
        M, N = 2, 3
        a1, a2 = 1.5, 3.0
        s = 1
        norm1 = rtt_mode_defect_norm(M, N, a1, N, s)
        norm2 = rtt_mode_defect_norm(M, N, a2, N, s)
        # Both nonzero
        assert norm1 > 0
        assert norm2 > 0
        # Ratio should be (a2/a1)^{N+s-1} = 2^3 = 8
        ratio = norm2 / norm1
        expected_ratio = (a2 / a1) ** (N + s - 1)
        assert abs(ratio - expected_ratio) < 1e-8

    def test_defect_symmetry(self):
        """Defect norm at (r, s) relates to (s, r) by symmetry."""
        M, N, a = 2, 3, 1.5
        # The defect at (N, 1) and (1, N) should have the same norm
        norm_Ns = rtt_mode_defect_norm(M, N, a, N, 1)
        norm_sN = rtt_mode_defect_norm(M, N, a, 1, N)
        assert abs(norm_Ns - norm_sN) < 1e-10


# ===== Evaluation T-mode structure =====

class TestEvalTMode:
    def test_T0_diagonal(self):
        """T_{ij}^{(0)} = delta_{ij} * Id_M."""
        M = 3
        for i in range(M):
            for j in range(M):
                T = _eval_T_ij_mode(M, i, j, 0, 5, 1.0)
                expected = float(i == j) * np.eye(M)
                assert np.allclose(T, expected)

    def test_T_mode_structure(self):
        """T_{ij}^{(r)} = -hbar*a^{r-1}*E_{ji} for r >= 1."""
        M, a = 2, 2.0
        for r in range(1, 4):
            T = _eval_T_ij_mode(M, 0, 1, r, 5, a)
            # E_{ji} = E_{10}: 1 at position (1, 0)
            expected = np.zeros((M, M))
            expected[1, 0] = -(a ** (r - 1))
            assert np.allclose(T, expected)

    def test_T_truncated_zero(self):
        """T_{ij}^{(r)} = 0 for r > N."""
        M, N = 2, 3
        T = _eval_T_ij_mode(M, 0, 1, N + 1, N, 1.0)
        assert np.allclose(T, np.zeros((M, M)))


# ===== Dimensions =====

class TestDimensions:
    @pytest.mark.parametrize("M,expected_sym,expected_alt", [
        (2, 3, 1), (3, 6, 3), (4, 10, 6),
    ])
    def test_sym_alt_dims(self, M, expected_sym, expected_alt):
        assert sym_dim(M) == expected_sym
        assert alt_dim(M) == expected_alt
        assert sym_dim(M) + alt_dim(M) == M * M


# ===== Full MC4 verification =====

class TestMC4Full:
    def test_verify_mc4_yangian(self):
        """Full MC4 verification passes for M = 2, 3, 4."""
        results = verify_mc4_yangian()
        for M in [2, 3, 4]:
            r = results[f"sl_{M}"]
            r1 = r["reduction_1_residue"]
            r2 = r["reduction_2_channels"]
            r3 = r["reduction_3_single_line"]
            assert r1["Xi_equals_minus_hbar_P"]
            assert r2["Xi_sym_check"]
            assert r2["Xi_alt_check"]
            assert r3["match"]

    def test_ybe_in_full_verification(self):
        """YBE passes in full MC4 verification."""
        results = verify_mc4_yangian()
        for M in [2, 3]:
            assert results[f"ybe_sl_{M}"]["ybe_holds"]

    def test_l_modes_in_full_verification(self):
        """L-mode structure correct in full MC4 verification."""
        results = verify_mc4_yangian()
        for M in [2, 3]:
            assert results[f"l_modes_sl_{M}"]["mode_structure_correct"]


# ===== Specific defect values =====

class TestDefectValues:
    def test_sl2_N2_specific(self):
        """sl_2, N=2, a=1: defect at (2,1) with (i,j,k,l)=(0,1,1,0)."""
        M, N, a = 2, 2, 1.0
        D = rtt_mode_defect(M, N, a, 0, 1, 1, 0, N, 1)
        # D = -hbar^2 * a^{N+s-1} * (delta_{il}E_{jk} - delta_{jk}E_{li})
        # (i,j,k,l) = (0,1,1,0): delta_{00}=1, E_{11}; delta_{11}=1, E_{00}
        # D = -a^2 * (E_{11} - E_{00})
        expected = np.array([[-(-1.0), 0], [0, -(1.0)]])  # [[1,0],[0,-1]]
        assert np.allclose(D, expected)

    def test_defect_zero_interior(self):
        """Defect at interior mode (r=1, s=1) is zero for N=3."""
        M, N, a = 2, 3, 1.5
        for i in range(M):
            for j in range(M):
                for k in range(M):
                    for l in range(M):
                        D = rtt_mode_defect(M, N, a, i, j, k, l, 1, 1)
                        assert np.allclose(D, np.zeros((M, M))), \
                            f"Nonzero interior defect at ({i},{j},{k},{l})"
