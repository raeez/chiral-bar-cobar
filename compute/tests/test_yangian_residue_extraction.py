"""Tests for MC4 Yangian auxiliary-kernel residue extraction.

Verifies the identity K^line_{1,2}(N) = K^RTT_{1,2}(N) for N = 2, 3, 4
via the three-layer reduction:
  Layer 1: Residue at collision gives P (permutation)
  Layer 2: Channel decomposition into Sym^2(V) and Lambda^2(V)
  Layer 3: Single-line identification on e_1 x e_2

Also verifies:
  - Yang R-matrix R(u) = u*I + P: Yang-Baxter, unitarity, spectral decomposition
  - Kernel dimensions: dim K = N(N-1)/2 for N = 2, 3, 4
  - K^line = K^RTT for N = 2 (proved), N = 3, 4 (evidence)
  - Exact (sympy) kernel computation for N = 2, 3
  - Connection to bar complex: bar-side kernel = Lambda^2(V)

Ground truth:
  - yangians.tex: sec:yangian-rep-bar
  - concordance.tex: MC4 status
  - yangian_residue.py: three-layer verification (58 tests, complementary)
"""

import pytest
import numpy as np

from compute.lib.yangian_residue_extraction import (
    # Core R-matrix
    permutation_matrix_slN,
    yang_r_matrix_slN,
    yang_r_matrix_slN_sympy,
    verify_yang_baxter_slN,
    verify_r_matrix_unitarity,
    # L-operator
    l_operator,
    normalized_line_operator,
    l_operator_residue,
    normalized_line_operator_residue,
    additive_to_normalized_line_operator,
    additive_normalization_bridge,
    l_operator_residue_sympy,
    # Channels
    sym_antisym_projectors,
    channel_eigenvalues,
    verify_channel_decomposition,
    # Kernels
    kernel_line_12,
    kernel_rtt_12,
    verify_auxiliary_kernel_identity,
    # Tensor-power propagation
    embed_two_factor_operator,
    fundamental_monodromy_operator,
    tensor_power_rtt_defect,
    complete_homogeneous_scalar,
    fundamental_line_series_coefficients,
    fundamental_line_series_coefficients_closed_form,
    fundamental_line_series_support_terms,
    boundary_strip_coefficient,
    boundary_strip_coefficient_closed_form,
    boundary_strip_packet,
    boundary_strip_packet_closed_form,
    boundary_strip_top_support_from_support_terms,
    boundary_strip_top_support_closed_form_operator,
    # Three-layer reduction
    three_layer_reduction,
    # Residue on e_1 x e_2
    mixed_tensor_residue_e1e2,
    # Spectral decomposition
    r_matrix_spectral_decomposition,
    # Bar complex connection
    bar_side_line_operator,
    rtt_boundary_kernel,
    # Exact
    kernel_line_12_exact,
    # Higher-rank data
    sl2_residue_data,
    sl3_residue_data,
    sl4_residue_data,
    # Full suite
    verify_all,
)


# ============================================================================
# R-matrix basic properties
# ============================================================================

class TestPermutationMatrix:
    """P on C^N x C^N: P^2 = I, Tr(P) = N, P swaps tensor factors."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_P_squared_is_identity(self, N):
        P = permutation_matrix_slN(N)
        assert np.allclose(P @ P, np.eye(N * N))

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_P_trace(self, N):
        P = permutation_matrix_slN(N)
        assert abs(np.trace(P) - N) < 1e-10

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_P_is_symmetric(self, N):
        P = permutation_matrix_slN(N)
        assert np.allclose(P, P.T)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_P_eigenvalues(self, N):
        """P has eigenvalue +1 (mult N(N+1)/2) and -1 (mult N(N-1)/2)."""
        P = permutation_matrix_slN(N)
        eigs = np.linalg.eigvalsh(P)
        n_plus = int(np.sum(np.abs(eigs - 1) < 1e-10))
        n_minus = int(np.sum(np.abs(eigs + 1) < 1e-10))
        assert n_plus == N * (N + 1) // 2
        assert n_minus == N * (N - 1) // 2

    def test_P_swaps_basis_vectors(self):
        """P(e_i x e_j) = e_j x e_i for all i, j."""
        N = 3
        P = permutation_matrix_slN(N)
        for i in range(N):
            for j in range(N):
                v = np.zeros(N * N)
                v[i * N + j] = 1.0
                Pv = P @ v
                expected = np.zeros(N * N)
                expected[j * N + i] = 1.0
                assert np.allclose(Pv, expected), \
                    f"P(e_{i} x e_{j}) != e_{j} x e_{i}"


class TestYangRMatrix:
    """R(u) = u*I + P: Yang-Baxter, unitarity, spectral decomposition."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_R_at_zero_is_P(self, N):
        """R(0) = P."""
        R = yang_r_matrix_slN(0, N)
        P = permutation_matrix_slN(N)
        assert np.allclose(R, P)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_R_large_u_approaches_uI(self, N):
        """R(u) ~ u*I for large u."""
        u = 1e8
        R = yang_r_matrix_slN(u, N)
        assert np.allclose(R / u, np.eye(N * N), atol=1e-6)

    @pytest.mark.parametrize("N,u,v", [
        (2, 2.3, 1.7),
        (2, 0.5, -1.3),
        (3, 3.7, 0.1),
        (3, 1.0, 2.0),
        (4, 2.0, 1.0),
    ])
    def test_yang_baxter_equation(self, N, u, v):
        """R12(u-v) R13(u) R23(v) = R23(v) R13(u) R12(u-v)."""
        err = verify_yang_baxter_slN(u, v, N)
        assert err < 1e-10, f"YBE error = {err} for N={N}, u={u}, v={v}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_unitarity(self, N):
        """R(u) R(-u) = (1 - u^2) I."""
        for u in [1.5, 2.7, 0.3]:
            err = verify_r_matrix_unitarity(u, N)
            assert err < 1e-10, f"Unitarity error = {err} for N={N}, u={u}"

    @pytest.mark.parametrize("N", [2, 3])
    def test_spectral_decomposition(self, N):
        """R(u) = (u+1) P_sym + (u-1) P_asym."""
        for u in [0.5, 2.0, -1.5]:
            sd = r_matrix_spectral_decomposition(u, N)
            assert sd["spectral_matches_direct"]
            assert sd["sym_eigenvalue"] == u + 1
            assert sd["asym_eigenvalue"] == u - 1

    @pytest.mark.parametrize("N", [2, 3])
    def test_R_determinant(self, N):
        """det R(u) = (u+1)^{N(N+1)/2} (u-1)^{N(N-1)/2}."""
        u = 2.5
        R = yang_r_matrix_slN(u, N)
        det_actual = np.linalg.det(R)
        det_expected = (u + 1) ** (N * (N + 1) // 2) * (u - 1) ** (N * (N - 1) // 2)
        assert abs(det_actual - det_expected) / abs(det_expected) < 1e-10

    @pytest.mark.parametrize("N", [2, 3])
    def test_sympy_matches_numpy(self, N):
        """Sympy R-matrix matches numpy at a numerical point."""
        from sympy import Symbol
        u_sym = Symbol('u')
        R_sym = yang_r_matrix_slN_sympy(u_sym, N)
        R_num_sym = np.array(R_sym.subs(u_sym, 2.5).tolist(), dtype=float)
        R_num = yang_r_matrix_slN(2.5, N).real
        assert np.allclose(R_num_sym, R_num)


# ============================================================================
# L-operator and residue
# ============================================================================

class TestLOperator:
    """L_a(u) = R(u-a) = (u-a)*I + P."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_L_at_collision_is_P(self, N):
        """L_a(a) = P (collision residue)."""
        for a in [0.0, 1.0, 2.5]:
            L = l_operator(a, a, N)
            P = permutation_matrix_slN(N)
            assert np.allclose(L, P), f"L_a(a) != P for a={a}, N={N}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_residue_function(self, N):
        """l_operator_residue returns P."""
        for a in [0.0, 1.5]:
            res = l_operator_residue(a, N)
            P = permutation_matrix_slN(N)
            assert np.allclose(res, P)

    @pytest.mark.parametrize("N", [2, 3])
    def test_residue_sympy(self, N):
        """Exact residue matches numpy."""
        P_sym = l_operator_residue_sympy(N)
        P_num = l_operator_residue(0, N)
        P_sym_num = np.array(P_sym.tolist(), dtype=float)
        assert np.allclose(P_sym_num, P_num)

    def test_L_away_from_collision(self):
        """L_a(u) for u != a is (u-a)*I + P, not just P."""
        N = 2
        u, a = 3.0, 1.0
        L = l_operator(u, a, N)
        P = permutation_matrix_slN(N)
        expected = (u - a) * np.eye(N * N) + P
        assert np.allclose(L, expected)


class TestTensorPowerPropagation:
    """Verify low-rank RTT propagation on short tensor powers."""

    @pytest.mark.parametrize("N,eval_points", [
        (2, [0.0, 1.0, 2.0]),
        (3, [0.0, 1.25, 2.5]),
        (4, [0.0, 1.5, 2.75]),
    ])
    def test_monodromy_shape(self, N, eval_points):
        total_dim = N ** (len(eval_points) + 2)
        T1 = fundamental_monodromy_operator(1.7, eval_points, N, auxiliary_slot=0)
        T2 = fundamental_monodromy_operator(-0.4, eval_points, N, auxiliary_slot=1)
        assert T1.shape == (total_dim, total_dim)
        assert T2.shape == (total_dim, total_dim)

    @pytest.mark.parametrize("N,eval_points", [
        (2, [0.0, 1.0]),
        (3, [0.0, 1.25, 2.5]),
        (4, [0.0, 1.5, 2.75]),
    ])
    def test_embedded_rmatrix_is_involutive_at_zero(self, N, eval_points):
        total_factors = len(eval_points) + 2
        P12 = embed_two_factor_operator(
            permutation_matrix_slN(N), 0, 1, total_factors, N
        )
        total_dim = N ** total_factors
        assert np.allclose(P12 @ P12, np.eye(total_dim))

    @pytest.mark.parametrize("N,eval_points,u,v", [
        (2, [0.0, 1.0], 1.7, -0.4),
        (2, [0.0, 1.0, 2.0], 1.7, -0.4),
        (3, [0.0, 1.25], 2.1, 0.3),
        (3, [0.0, 1.25, 2.5], 2.1, 0.3),
        (4, [0.0, 1.5], 1.4, -0.6),
        (4, [0.0, 1.5, 2.75], 1.4, -0.6),
    ])
    def test_tensor_power_rtt_defect_vanishes(self, N, eval_points, u, v):
        defect = tensor_power_rtt_defect(u, v, eval_points, N)
        assert defect["frobenius_norm"] < 1e-10
        assert defect["max_entry"] < 1e-10


class TestBoundaryStripPacket:
    """Verify the first low-stage boundary-strip coefficients on tensor powers."""

    @pytest.mark.parametrize("N,eval_points,stage", [
        (2, [0.0, 1.0], 4),
        (2, [0.0, 1.0, 2.0], 4),
        (3, [0.0, 1.25], 4),
        (3, [0.0, 1.25, 2.5], 4),
        (4, [0.0, 1.5], 4),
        (4, [0.0, 1.5, 2.75], 4),
    ])
    def test_boundary_strip_packet_vanishes(self, N, eval_points, stage):
        packet = boundary_strip_packet(eval_points, N, stage)
        assert packet["all_zero"]
        for _, data in packet["packet"].items():
            assert data["frobenius_norm"] < 1e-10
            assert data["max_entry"] < 1e-10

    @pytest.mark.parametrize("N,eval_points,max_degree", [
        (2, [0.0, 1.0], 3),
        (3, [0.0, 1.25], 3),
    ])
    def test_line_series_starts_with_identity(self, N, eval_points, max_degree):
        coeffs = fundamental_line_series_coefficients(
            eval_points, N, max_degree, auxiliary_slot=0
        )
        total_dim = N ** (len(eval_points) + 2)
        assert np.allclose(coeffs[0], np.eye(total_dim))

    @pytest.mark.parametrize("N,eval_points,boundary_index", [
        (2, [0.0, 1.0], 0),
        (3, [0.0, 1.25, 2.5], 1),
        (4, [0.0, 1.5, 2.75], 2),
    ])
    def test_boundary_strip_single_coefficient_vanishes(self, N, eval_points, boundary_index):
        coeff = boundary_strip_coefficient(
            eval_points, N, boundary_index, max_degree=boundary_index + 2
        )
        assert np.linalg.norm(coeff) < 1e-10


class TestFundamentalSeriesClosedForm:
    """Match the closed-form monodromy coefficients with the iterative expansion."""

    @pytest.mark.parametrize("values,degree,expected", [
        ([2.0], 0, 1.0),
        ([2.0], 2, 4.0),
        ([2.0, 3.0], 1, 5.0),
        ([2.0, 3.0], 2, 19.0),
    ])
    def test_complete_homogeneous_scalar(self, values, degree, expected):
        assert complete_homogeneous_scalar(values, degree) == pytest.approx(expected)

    @pytest.mark.parametrize("N,eval_points,max_degree,auxiliary_slot", [
        (2, [0.0, 1.0], 4, 0),
        (2, [0.0, 1.0], 4, 1),
        (3, [0.0, 1.25, 2.5], 4, 0),
        (3, [0.0, 1.25, 2.5], 4, 1),
    ])
    def test_closed_form_matches_iterative_series(self, N, eval_points, max_degree, auxiliary_slot):
        iterative = fundamental_line_series_coefficients(
            eval_points, N, max_degree, auxiliary_slot
        )
        closed_form = fundamental_line_series_coefficients_closed_form(
            eval_points, N, max_degree, auxiliary_slot
        )
        assert len(iterative) == len(closed_form)
        for iterative_coeff, closed_form_coeff in zip(iterative, closed_form):
            assert np.allclose(iterative_coeff, closed_form_coeff)


class TestClosedFormBoundaryStrip:
    """Use the closed-form monodromy expansion on the next boundary packet."""

    @pytest.mark.parametrize("N,eval_points,boundary_index", [
        (2, [0.0, 1.0], 4),
        (3, [0.0, 1.25, 2.5], 3),
        (4, [0.0, 1.5, 2.75], 2),
    ])
    def test_closed_form_matches_iterative_boundary_coefficient(self, N, eval_points, boundary_index):
        iterative = boundary_strip_coefficient(
            eval_points, N, boundary_index, max_degree=boundary_index + 2
        )
        closed_form = boundary_strip_coefficient_closed_form(
            eval_points, N, boundary_index
        )
        assert np.allclose(iterative, closed_form)

    @pytest.mark.parametrize("N,eval_points,stage", [
        (2, [0.0, 1.0], 6),
        (2, [0.0, 1.0, 2.0], 6),
        (3, [0.0, 1.25], 6),
        (3, [0.0, 1.25, 2.5], 6),
        (4, [0.0, 1.5], 6),
        (4, [0.0, 1.5, 2.75], 6),
    ])
    def test_closed_form_stage6_packet_vanishes(self, N, eval_points, stage):
        packet = boundary_strip_packet_closed_form(eval_points, N, stage)
        assert packet["all_zero"]
        for _, data in packet["packet"].items():
            assert data["frobenius_norm"] < 1e-10
            assert data["max_entry"] < 1e-10

    @pytest.mark.parametrize("N,eval_points,stage", [
        (2, [0.3, 1.7, 4.1], 6),
        (3, [-0.5, 0.8, 2.2], 6),
        (4, [0.25, 1.1, 3.6], 6),
    ])
    def test_closed_form_stage6_packet_vanishes_for_alternate_generic_points(self, N, eval_points, stage):
        packet = boundary_strip_packet_closed_form(eval_points, N, stage)
        assert packet["all_zero"]
        for _, data in packet["packet"].items():
            assert data["frobenius_norm"] < 1e-9
            assert data["max_entry"] < 1e-9


class TestTopSupportFormula:
    """Verify the closed-form top-support operator on the top packet."""

    @pytest.mark.parametrize("N,eval_points,boundary_index", [
        (2, [0.0], 0),
        (2, [0.0, 1.0], 1),
        (2, [0.0, 1.0, 2.0], 2),
        (3, [0.0], 0),
        (3, [0.0, 1.25], 1),
        (3, [0.0, 1.25, 2.5], 2),
    ])
    def test_top_support_closed_form_matches_support_enumeration(self, N, eval_points, boundary_index):
        from_support_terms = boundary_strip_top_support_from_support_terms(
            eval_points, N, boundary_index
        )
        closed_form = boundary_strip_top_support_closed_form_operator(
            N, boundary_index
        )
        assert np.allclose(from_support_terms, closed_form)

    @pytest.mark.parametrize("N,eval_points_a,eval_points_b,boundary_index", [
        (2, [0.0, 1.0, 2.0], [0.3, 1.7, 4.1], 2),
        (3, [0.0, 1.25, 2.5], [-0.5, 0.8, 2.2], 2),
    ])
    def test_top_support_is_independent_of_generic_points(self, N, eval_points_a, eval_points_b, boundary_index):
        top_a = boundary_strip_top_support_from_support_terms(
            eval_points_a, N, boundary_index
        )
        top_b = boundary_strip_top_support_from_support_terms(
            eval_points_b, N, boundary_index
        )
        assert np.allclose(top_a, top_b)


class TestNormalizationBridge:
    """Bridge the additive collision-value package to the normalized residue package."""

    @pytest.mark.parametrize("N,u,a", [
        (2, 3.5, 1.0),
        (3, 2.25, -0.5),
        (4, 5.0, 1.75),
    ])
    def test_additive_division_gives_normalized_kernel(self, N, u, a):
        normalized_from_add = additive_to_normalized_line_operator(u, a, N)
        normalized_expected = normalized_line_operator(u, a, N, hbar=-1.0)
        assert np.allclose(normalized_from_add, normalized_expected)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_collision_value_matches_normalized_residue(self, N):
        collision_value = l_operator_residue(0.0, N)
        normalized_residue = normalized_line_operator_residue(N, hbar=-1.0)
        assert np.allclose(collision_value, normalized_residue)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_bridge_helper(self, N):
        bridge = additive_normalization_bridge(3.5, 1.25, N)
        assert bridge["matrix_bridge_holds"]
        assert bridge["collision_value_matches_normalized_residue"]


# ============================================================================
# Channel decomposition
# ============================================================================

class TestChannelDecomposition:
    """Sym^2(V) and Lambda^2(V) projectors and eigenvalues."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_projectors_sum_to_identity(self, N):
        P_sym, P_asym = sym_antisym_projectors(N)
        assert np.allclose(P_sym + P_asym, np.eye(N * N))

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_projectors_idempotent(self, N):
        P_sym, P_asym = sym_antisym_projectors(N)
        assert np.allclose(P_sym @ P_sym, P_sym)
        assert np.allclose(P_asym @ P_asym, P_asym)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_projectors_orthogonal(self, N):
        P_sym, P_asym = sym_antisym_projectors(N)
        assert np.allclose(P_sym @ P_asym, np.zeros((N * N, N * N)))

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_channel_eigenvalues(self, N):
        data = channel_eigenvalues(N)
        assert data["sym_eigenvalue"] == +1
        assert data["alt_eigenvalue"] == -1
        assert data["sym_dim"] == N * (N + 1) // 2
        assert data["alt_dim"] == N * (N - 1) // 2
        assert data["sym_dim"] + data["alt_dim"] == N * N

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_full_channel_verification(self, N):
        results = verify_channel_decomposition(N)
        for key, val in results.items():
            assert val, f"Channel check failed: {key} for N={N}"


# ============================================================================
# Kernel dimensions for N = 2, 3, 4
# ============================================================================

class TestKernelDimensions:
    """dim K = N(N-1)/2 for N = 2, 3, 4."""

    @pytest.mark.parametrize("N,expected_dim", [
        (2, 1),
        (3, 3),
        (4, 6),
        (5, 10),
    ])
    def test_kernel_line_dim(self, N, expected_dim):
        """K^line_{1,2}(N) has dimension N(N-1)/2."""
        result = kernel_line_12(N)
        assert result["asym_kernel_dim"] == expected_dim
        assert result["asym_correct"]

    @pytest.mark.parametrize("N,expected_dim", [
        (2, 1),
        (3, 3),
        (4, 6),
    ])
    def test_kernel_rtt_dim(self, N, expected_dim):
        """K^RTT_{1,2}(N) has dimension N(N-1)/2."""
        result = kernel_rtt_12(N)
        assert result["rtt_kernel_dim"] == expected_dim
        assert result["correct"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_symmetric_kernel_dim(self, N):
        """Symmetric kernel (P = +1) has dimension N(N+1)/2."""
        result = kernel_line_12(N)
        assert result["sym_kernel_dim"] == N * (N + 1) // 2
        assert result["sym_correct"]


# ============================================================================
# K^line = K^RTT identity
# ============================================================================

class TestAuxiliaryKernelIdentity:
    """K^line_{1,2}(N) = K^RTT_{1,2}(N) for N = 2, 3, 4."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_dimension_match(self, N):
        """dim K^line = dim K^RTT."""
        result = verify_auxiliary_kernel_identity(N)
        assert result["dim_match"]
        assert result["K_line_dim"] == result["K_rtt_dim"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_subspace_match(self, N):
        """K^line and K^RTT span the same subspace (Lambda^2(V))."""
        result = verify_auxiliary_kernel_identity(N)
        assert result["subspace_match"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_identity_holds(self, N):
        """Full identity K^line = K^RTT."""
        result = verify_auxiliary_kernel_identity(N)
        assert result["identity_holds"]

    def test_sl2_kernel_is_1d(self):
        """For sl_2: K = C^1 (singlet)."""
        result = verify_auxiliary_kernel_identity(2)
        assert result["K_line_dim"] == 1
        assert result["K_rtt_dim"] == 1
        assert result["expected_dim"] == 1

    def test_sl3_kernel_is_3d(self):
        """For sl_3: K = C^3 (adjoint of SL(2) subgroup)."""
        result = verify_auxiliary_kernel_identity(3)
        assert result["K_line_dim"] == 3
        assert result["K_rtt_dim"] == 3

    def test_sl4_kernel_is_6d(self):
        """For sl_4: K = C^6 (antisymmetric tensor)."""
        result = verify_auxiliary_kernel_identity(4)
        assert result["K_line_dim"] == 6
        assert result["K_rtt_dim"] == 6


# ============================================================================
# Three-layer reduction verification
# ============================================================================

class TestThreeLayerReduction:
    """Three-layer reduction: residue -> channels -> single line."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_all_layers_pass(self, N):
        result = three_layer_reduction(N)
        assert result["all_layers_pass"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_layer1_permutation(self, N):
        """Layer 1: L_a(a) = P is a permutation (P^2 = I)."""
        result = three_layer_reduction(N)
        assert result["layer_1"]["is_permutation"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_layer2_eigenvalues(self, N):
        """Layer 2: P = +1 on Sym^2, P = -1 on Lambda^2."""
        result = three_layer_reduction(N)
        assert result["layer_2"]["sym_eigenvalue_correct"]
        assert result["layer_2"]["asym_eigenvalue_correct"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_layer2_dimensions(self, N):
        """Layer 2: correct dimensions of Sym^2 and Lambda^2."""
        result = three_layer_reduction(N)
        assert result["layer_2"]["sym_dim"] == N * (N + 1) // 2
        assert result["layer_2"]["asym_dim"] == N * (N - 1) // 2

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_layer3_swap(self, N):
        """Layer 3: P(e_1 x e_2) = e_2 x e_1."""
        result = three_layer_reduction(N)
        assert result["layer_3"]["P_e1e2_equals_e2e1"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_layer3_antisymmetric_in_kernel(self, N):
        """Layer 3: e_1 x e_2 - e_2 x e_1 lies in ker(P + I)."""
        result = three_layer_reduction(N)
        assert result["layer_3"]["antisymmetric_in_kernel"]


# ============================================================================
# Single residue on e_1 x e_2
# ============================================================================

class TestMixedTensorResidue:
    """The single residue computation on e_1 x e_2 that determines everything."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_swap_correct(self, N):
        """P(e_1 x e_2) = e_2 x e_1."""
        result = mixed_tensor_residue_e1e2(N)
        assert result["swap_correct"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_antisymmetric_eigenvector(self, N):
        """w = e_1 x e_2 - e_2 x e_1 is -1 eigenvector of P."""
        result = mixed_tensor_residue_e1e2(N)
        assert result["w_is_eigenvector_minus1"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_in_kernel_P_plus_I(self, N):
        """w = e_1 x e_2 - e_2 x e_1 lies in ker(P + I)."""
        result = mixed_tensor_residue_e1e2(N)
        assert result["w_in_kernel_P_plus_I"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_w_norm(self, N):
        """||w|| = sqrt(2)."""
        result = mixed_tensor_residue_e1e2(N)
        assert abs(result["w_norm"] - np.sqrt(2)) < 1e-10

    def test_sl2_unique_antisymmetric(self):
        """For sl_2, w = e_1 x e_2 - e_2 x e_1 spans all of Lambda^2(C^2)."""
        # Lambda^2(C^2) is 1-dimensional
        result = mixed_tensor_residue_e1e2(2)
        assert result["swap_correct"]
        # No higher pairs for N=2
        assert len(result["higher_pairs"]) == 0

    @pytest.mark.parametrize("N", [3, 4])
    def test_higher_pairs(self, N):
        """For N >= 3, higher pairs e_1 x e_j - e_j x e_1 also work."""
        result = mixed_tensor_residue_e1e2(N)
        for pair_key, pair_data in result["higher_pairs"].items():
            assert pair_data["is_eigenvector"], \
                f"{pair_key} is not -1 eigenvector for N={N}"
            assert pair_data["in_kernel"], \
                f"{pair_key} is not in ker(P+I) for N={N}"


# ============================================================================
# Exact (sympy) kernel computation
# ============================================================================

class TestExactKernel:
    """Exact kernel computation using sympy for rigorous verification."""

    @pytest.mark.parametrize("N", [2, 3])
    def test_kernel_dimension(self, N):
        result = kernel_line_12_exact(N)
        assert result["kernel_dim"] == N * (N - 1) // 2
        assert result["correct"]

    @pytest.mark.parametrize("N", [2, 3])
    def test_all_antisymmetric(self, N):
        """All kernel vectors are antisymmetric (P*v = -v)."""
        result = kernel_line_12_exact(N)
        assert result["all_antisymmetric"]

    def test_sl2_exact_kernel_is_singlet(self):
        """For sl_2: exact kernel is 1-dimensional."""
        result = kernel_line_12_exact(2)
        assert result["kernel_dim"] == 1
        # The kernel vector should be proportional to (0, 1, -1, 0)
        v = result["kernel_vectors"][0]
        # Check it is antisymmetric: v[1] = -v[2] and v[0] = v[3] = 0
        v_list = [float(x) for x in v]
        assert abs(v_list[0]) < 1e-10 or abs(v_list[3]) < 1e-10
        assert abs(v_list[1] + v_list[2]) < 1e-10

    def test_sl3_exact_kernel_is_3d(self):
        """For sl_3: exact kernel is 3-dimensional."""
        result = kernel_line_12_exact(3)
        assert result["kernel_dim"] == 3

    @pytest.mark.parametrize("N", [2, 3])
    def test_canonical_basis_matches(self, N):
        """Canonical basis {e_i x e_j - e_j x e_i : i < j} has correct count."""
        result = kernel_line_12_exact(N)
        assert len(result["canonical_basis"]) == N * (N - 1) // 2


# ============================================================================
# Higher-rank specializations
# ============================================================================

class TestSl2Residue:
    """sl_2 (N=2): dim K = 1 (singlet)."""

    def test_dimensions(self):
        data = sl2_residue_data()
        assert data["V_dim"] == 2
        assert data["VxV_dim"] == 4
        assert data["sym_dim"] == 3
        assert data["asym_dim"] == 1
        assert data["kernel_dim"] == 1

    def test_eigenvalue(self):
        data = sl2_residue_data()
        assert data["w_eigenvalue"] == -1

    def test_identity_holds(self):
        data = sl2_residue_data()
        assert data["identity_holds"]

    def test_antisymmetric_generator(self):
        data = sl2_residue_data()
        w = np.array(data["asym_generator"])
        # w = [0, 1, -1, 0] = e_1 x e_2 - e_2 x e_1
        assert abs(w[0]) < 1e-10
        assert abs(w[3]) < 1e-10
        assert abs(w[1] + w[2]) < 1e-10  # antisymmetric

    def test_P_on_antisymmetric_generator(self):
        data = sl2_residue_data()
        w = np.array(data["asym_generator"])
        Pw = np.array(data["P_on_w"])
        assert np.allclose(Pw, -w)


class TestSl3Residue:
    """sl_3 (N=3): dim K = 3."""

    def test_dimensions(self):
        data = sl3_residue_data()
        assert data["V_dim"] == 3
        assert data["VxV_dim"] == 9
        assert data["sym_dim"] == 6
        assert data["asym_dim"] == 3
        assert data["kernel_dim"] == 3

    def test_all_eigenvectors(self):
        data = sl3_residue_data()
        assert data["all_eigenvectors"]

    def test_identity_holds(self):
        data = sl3_residue_data()
        assert data["identity_holds"]

    def test_three_generators(self):
        data = sl3_residue_data()
        assert len(data["asym_generators"]) == 3


class TestSl4Residue:
    """sl_4 (N=4): dim K = 6."""

    def test_dimensions(self):
        data = sl4_residue_data()
        assert data["V_dim"] == 4
        assert data["VxV_dim"] == 16
        assert data["sym_dim"] == 10
        assert data["asym_dim"] == 6
        assert data["kernel_dim"] == 6

    def test_all_eigenvectors(self):
        data = sl4_residue_data()
        assert data["all_eigenvectors"]

    def test_identity_holds(self):
        data = sl4_residue_data()
        assert data["identity_holds"]

    def test_six_generators(self):
        data = sl4_residue_data()
        assert data["num_generators"] == 6


# ============================================================================
# Bar complex connection
# ============================================================================

class TestBarComplexConnection:
    """Connection between the bar-side line operator and RTT kernel."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_bar_kernel_is_Lambda2(self, N):
        result = bar_side_line_operator(N, mode_level=3)
        assert result["bar_kernel_equals_Lambda2"]
        assert result["collision_residue_is_P"]
        assert result["bar_rtt_match"]

    @pytest.mark.parametrize("N", [2, 3])
    def test_bar_kernel_dim(self, N):
        result = bar_side_line_operator(N, mode_level=3)
        assert result["bar_kernel_dim"] == N * (N - 1) // 2

    def test_bar_mode_count(self):
        """Mode level N gives N+1 modes and N^2*(N+1) total generators."""
        N = 2
        mode_level = 3
        result = bar_side_line_operator(N, mode_level)
        assert result["num_modes"] == mode_level + 1
        assert result["total_generators"] == (mode_level + 1) * N * N

    @pytest.mark.parametrize("N", [2, 3])
    def test_rtt_boundary_kernel(self, N):
        """RTT boundary defect is nonzero (captures truncation kernel)."""
        result = rtt_boundary_kernel(N, mode_level=2, a=1.0)
        # There should be nonzero defects at boundary
        assert result["num_defects"] > 0
        assert result["max_defect_norm"] > 0


# ============================================================================
# Consistency with yangian_residue.py (the existing module)
# ============================================================================

class TestConsistencyWithExisting:
    """Cross-check against yangian_residue.py (which uses R = I - P/u convention)."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_permutation_matrices_agree(self, N):
        """Both modules produce the same permutation matrix."""
        from compute.lib.yangian_residue import permutation_matrix as perm_old
        P_old = perm_old(N)
        P_new = permutation_matrix_slN(N)
        assert np.allclose(P_old, P_new)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_kernel_dimensions_agree(self, N):
        """Both modules give the same antisymmetric kernel dimension."""
        from compute.lib.yangian_residue import alt_dim
        old_dim = alt_dim(N)
        new_result = kernel_line_12(N)
        assert new_result["asym_kernel_dim"] == old_dim

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_normalized_kernels_agree(self, N):
        """The normalized bridge matches the original simple-pole module exactly."""
        from compute.lib.yangian_residue import (
            evaluation_line_operator as normalized_old,
            residue_at_a as residue_old,
        )
        u, a = 3.0, 1.25
        old_line = normalized_old(N, u, a, hbar=1.0)
        new_line = normalized_line_operator(u, a, N, hbar=1.0)
        assert np.allclose(old_line, new_line)
        assert np.allclose(residue_old(N, hbar=1.0), normalized_line_operator_residue(N))


# ============================================================================
# Full verification suite
# ============================================================================

class TestFullSuite:
    """Run the complete verification suite."""

    def test_verify_all_N2_to_N4(self):
        """All checks pass for N = 2, 3, 4."""
        results = verify_all(max_N=4)
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_all_count(self):
        """Correct number of checks."""
        results = verify_all(max_N=4)
        # 3 values of N (2,3,4) x 8 checks + 2 exact checks = 26
        assert len(results) >= 26


# ============================================================================
# Edge cases and structural tests
# ============================================================================

class TestStructural:
    """Structural and edge-case tests."""

    def test_kernel_N1_trivial(self):
        """For N=1, Lambda^2(C^1) = 0 (no antisymmetric tensors)."""
        # N=1: V x V = C^1, P = [1], ker(P + I) = 0
        P = permutation_matrix_slN(1)
        assert np.allclose(P, np.array([[1.0]]))
        # P + I = [[2]], kernel is trivial
        kernel_mat = P + np.eye(1)
        assert np.linalg.matrix_rank(kernel_mat) == 1  # full rank, no kernel

    def test_R_matrix_singular_at_u_minus1(self):
        """R(u) = u*I + P is singular at u = -1 (symmetric channel zero)."""
        for N in [2, 3]:
            R = yang_r_matrix_slN(-1, N)
            det = np.linalg.det(R)
            assert abs(det) < 1e-10, f"R(-1) should be singular for N={N}"

    def test_R_matrix_singular_at_u_plus1(self):
        """R(u) is singular at u = +1 (antisymmetric channel zero)."""
        for N in [2, 3]:
            R = yang_r_matrix_slN(1, N)
            det = np.linalg.det(R)
            assert abs(det) < 1e-10, f"R(1) should be singular for N={N}"

    def test_R_matrix_nonsingular_generic(self):
        """R(u) is nonsingular for generic u (u != pm 1)."""
        for N in [2, 3]:
            R = yang_r_matrix_slN(2.5, N)
            det = np.linalg.det(R)
            assert abs(det) > 1e-5, f"R(2.5) should be nonsingular for N={N}"

    def test_antisymmetric_vectors_linearly_independent(self):
        """The N(N-1)/2 antisymmetric basis vectors are linearly independent."""
        for N in [2, 3, 4]:
            vectors = []
            for i in range(N):
                for j in range(i + 1, N):
                    v = np.zeros(N * N)
                    v[i * N + j] = 1
                    v[j * N + i] = -1
                    vectors.append(v)
            M = np.array(vectors)
            rank = np.linalg.matrix_rank(M)
            assert rank == N * (N - 1) // 2

    def test_symmetric_and_antisymmetric_orthogonal(self):
        """Sym^2 and Lambda^2 basis vectors are orthogonal."""
        N = 3
        # A symmetric vector: e_1 x e_2 + e_2 x e_1
        v_sym = np.zeros(N * N)
        v_sym[0 * N + 1] = 1
        v_sym[1 * N + 0] = 1
        # An antisymmetric vector: e_1 x e_2 - e_2 x e_1
        v_asym = np.zeros(N * N)
        v_asym[0 * N + 1] = 1
        v_asym[1 * N + 0] = -1
        assert abs(np.dot(v_sym, v_asym)) < 1e-10
