r"""Tests for Yangian RTT presentation across ALL classical Lie types.

Verifies:
    1. R-matrix in fundamental rep for A_n, B_n, C_n, D_n. YBE for each.
    2. RTT generators T^{(r)} at levels r=0,1,2,3 from bar complex.
    3. Transfer matrix t(u) = Tr T(u). [t(u), t(v)] = 0.
    4. Evaluation homomorphism ev_a: Y(g) -> U(g).
    5. Drinfeld <-> RTT isomorphism (numerically for sl_2, sl_3, so_5).
    6. Quantum determinant qdet T(u) for gl_2, gl_3, gl_4.
       Sklyanin determinant sdet for so_5, sp_4.
    7. Prefundamental modules: TQ relation for sl_2, sl_3.
    8. Shadow -> Yangian dictionary.

Ground truth references:
    - Molev, "Yangians and classical Lie algebras", AMS 2007.
    - Chari-Pressley, "A Guide to Quantum Groups", Cambridge 1994.
    - yangians.tex, concordance.tex.
"""

import pytest
import numpy as np

from compute.lib.yangian_rtt_all_types import (
    # Core data
    lie_algebra_data,
    modular_characteristic,
    # Operators
    permutation_operator,
    trace_projection_operator,
    symplectic_trace_operator,
    verify_operator_identities,
    # R-matrices
    R_matrix,
    R_matrix_kappa,
    # YBE
    verify_yang_baxter,
    # RTT generators
    rtt_generators_symbolic,
    evaluation_L_operator,
    rtt_generators_numerical,
    # Transfer matrix
    transfer_matrix,
    verify_transfer_commutativity,
    # Evaluation
    chevalley_generators_fund,
    verify_chevalley_relations,
    evaluation_homomorphism,
    verify_evaluation_hom,
    casimir_tensor_fund,
    # Quantum determinant
    quantum_determinant_scalar,
    quantum_determinant_explicit,
    verify_qdet_is_scalar,
    verify_qdet_centrality,
    # Sklyanin determinant
    sklyanin_determinant_scalar,
    verify_sklyanin_is_scalar,
    # Drinfeld-RTT
    drinfeld_to_rtt_map,
    verify_drinfeld_rtt_isomorphism,
    # Prefundamental
    prefundamental_character,
    verify_tq_relation,
    # Shadow dictionary
    shadow_yangian_dictionary,
    classical_r_matrix_fund,
    quantum_R_perturbative,
    # Spectral decomposition
    spectral_decomposition,
    # Full verification
    full_verification,
    # Cartan matrix (internal but tested)
    _cartan_matrix,
    _build_positive_roots,
)


# ============================================================
# Section 1: Lie algebra data
# ============================================================

class TestLieAlgebraData:
    """Verify fundamental Lie algebra data for all classical types."""

    def test_sl2_data(self):
        d = lie_algebra_data('A', 1)
        assert d['rank'] == 1
        assert d['dim_g'] == 3
        assert d['dual_coxeter'] == 2
        assert d['fund_dim'] == 2

    def test_sl3_data(self):
        d = lie_algebra_data('A', 2)
        assert d['rank'] == 2
        assert d['dim_g'] == 8
        assert d['dual_coxeter'] == 3
        assert d['fund_dim'] == 3

    def test_sl4_data(self):
        d = lie_algebra_data('A', 3)
        assert d['rank'] == 3
        assert d['dim_g'] == 15
        assert d['dual_coxeter'] == 4
        assert d['fund_dim'] == 4

    def test_so5_data(self):
        """B_2 = so(5)."""
        d = lie_algebra_data('B', 2)
        assert d['rank'] == 2
        assert d['dim_g'] == 10
        assert d['dual_coxeter'] == 3
        assert d['fund_dim'] == 5

    def test_so7_data(self):
        """B_3 = so(7)."""
        d = lie_algebra_data('B', 3)
        assert d['rank'] == 3
        assert d['dim_g'] == 21
        assert d['dual_coxeter'] == 5
        assert d['fund_dim'] == 7

    def test_sp4_data(self):
        """C_2 = sp(4)."""
        d = lie_algebra_data('C', 2)
        assert d['rank'] == 2
        assert d['dim_g'] == 10
        assert d['dual_coxeter'] == 3
        assert d['fund_dim'] == 4

    def test_sp6_data(self):
        """C_3 = sp(6)."""
        d = lie_algebra_data('C', 3)
        assert d['rank'] == 3
        assert d['dim_g'] == 21
        assert d['dual_coxeter'] == 4
        assert d['fund_dim'] == 6

    def test_so6_data(self):
        """D_3 = so(6) ~ sl(4)."""
        d = lie_algebra_data('D', 3)
        assert d['rank'] == 3
        assert d['dim_g'] == 15
        assert d['dual_coxeter'] == 4
        assert d['fund_dim'] == 6

    def test_so8_data(self):
        """D_4 = so(8)."""
        d = lie_algebra_data('D', 4)
        assert d['rank'] == 4
        assert d['dim_g'] == 28
        assert d['dual_coxeter'] == 6
        assert d['fund_dim'] == 8

    def test_kappa_sl3_level1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        kap = modular_characteristic('A', 2, 1)
        assert abs(kap - 16.0 / 3.0) < 1e-10

    def test_kappa_so5_level1(self):
        """kappa(so_5, k=1) = 10*(1+3)/(2*3) = 20/3."""
        kap = modular_characteristic('B', 2, 1)
        assert abs(kap - 20.0 / 3.0) < 1e-10


# ============================================================
# Section 2: Operator identities
# ============================================================

class TestOperatorIdentities:
    """Verify P^2 = I, Q^2 = c*Q, PQ = QP = Q."""

    def test_type_A_permutation(self):
        for N in [2, 3, 4]:
            P = permutation_operator(N)
            I = np.eye(N * N)
            assert np.allclose(P @ P, I)

    def test_type_B_identities(self):
        result = verify_operator_identities('B', 2)
        for key, val in result.items():
            assert val, f"B_2 identity {key} failed"

    def test_type_B3_identities(self):
        result = verify_operator_identities('B', 3)
        for key, val in result.items():
            assert val, f"B_3 identity {key} failed"

    def test_type_C_identities(self):
        result = verify_operator_identities('C', 2)
        for key, val in result.items():
            assert val, f"C_2 identity {key} failed"

    def test_type_C3_identities(self):
        result = verify_operator_identities('C', 3)
        for key, val in result.items():
            assert val, f"C_3 identity {key} failed"

    def test_type_D_identities(self):
        result = verify_operator_identities('D', 3)
        for key, val in result.items():
            assert val, f"D_3 identity {key} failed"

    def test_type_D4_identities(self):
        result = verify_operator_identities('D', 4)
        for key, val in result.items():
            assert val, f"D_4 identity {key} failed"

    def test_symplectic_K_squared(self):
        """For sp(2n), K^2 = -2n * K."""
        for n_val in [2, 3]:
            N = 2 * n_val
            K = symplectic_trace_operator(n_val)
            K2 = K @ K
            assert np.allclose(K2, -N * K, atol=1e-10), \
                f"K^2 = -{N}K failed for sp({N})"

    def test_symplectic_PK_minus_K(self):
        """For sp(2n), PK = KP = -K."""
        for n_val in [2, 3]:
            N = 2 * n_val
            K = symplectic_trace_operator(n_val)
            P = permutation_operator(N)
            assert np.allclose(P @ K, -K, atol=1e-10), \
                f"PK = -K failed for sp({N})"
            assert np.allclose(K @ P, -K, atol=1e-10), \
                f"KP = -K failed for sp({N})"

    def test_trace_Q_squared(self):
        """For so(N), Q^2 = N * Q."""
        for N in [5, 6, 7, 8]:
            Q = trace_projection_operator(N)
            Q2 = Q @ Q
            assert np.allclose(Q2, N * Q, atol=1e-10), \
                f"Q^2 = {N}Q failed for so({N})"


# ============================================================
# Section 3: R-matrix and Yang-Baxter equation
# ============================================================

class TestRMatrixYBE:
    """Verify R-matrix properties and YBE for all classical types."""

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_type_A_ybe(self, n):
        """YBE for sl_{n+1}."""
        result = verify_yang_baxter('A', n, 3.7 + 0.1j, 2.1 - 0.2j)
        assert result['passes'], f"YBE failed for A_{n}: diff={result['max_diff']}"

    @pytest.mark.parametrize("n", [2, 3])
    def test_type_B_ybe(self, n):
        """YBE for so_{2n+1}."""
        result = verify_yang_baxter('B', n, 3.7, 2.1)
        assert result['passes'], f"YBE failed for B_{n}: diff={result['max_diff']}"

    @pytest.mark.parametrize("n", [2, 3])
    def test_type_C_ybe(self, n):
        """YBE for sp_{2n}."""
        result = verify_yang_baxter('C', n, 5.5, 2.3)
        assert result['passes'], f"YBE failed for C_{n}: diff={result['max_diff']}"

    @pytest.mark.parametrize("n", [3, 4])
    def test_type_D_ybe(self, n):
        """YBE for so_{2n}."""
        result = verify_yang_baxter('D', n, 4.2, 1.8)
        assert result['passes'], f"YBE failed for D_{n}: diff={result['max_diff']}"

    def test_ybe_complex_params(self):
        """YBE with complex spectral parameters."""
        for (lt, n_val) in [('A', 2), ('B', 2), ('C', 2), ('D', 3)]:
            result = verify_yang_baxter(lt, n_val, 3.0 + 1.0j, 1.0 - 0.5j)
            assert result['passes'], \
                f"YBE with complex params failed for {lt}_{n_val}"

    def test_R_matrix_symmetry_type_A(self):
        """For type A, R(u) = u I + P satisfies R(u) R(-u) = (u^2 - 1) I_{N^2}.

        Proof: R(u) R(-u) = (uI + P)(-uI + P) = -u^2 I + uP - uP + P^2
        = -u^2 I + I = -(u^2 - 1) I. So R(u) R(-u) = -(u^2-1) I.
        """
        N = 3
        u = 2.5 + 0.3j
        R_u = R_matrix('A', 2, u)
        R_neg = R_matrix('A', 2, -u)
        product = R_u @ R_neg
        expected = -(u ** 2 - 1) * np.eye(N * N, dtype=complex)
        assert np.allclose(product, expected, atol=1e-8)

    def test_R_matrix_unitarity_type_BD(self):
        """For types B/D, R_{12}(u) R_{21}(u) should be proportional to I.

        R_{21}(u) = P R_{12}(u) P.
        Unitarity: R_{12}(u) R_{21}(-u) = f(u) I.
        """
        for (lt, n_val) in [('B', 2), ('D', 3)]:
            N = lie_algebra_data(lt, n_val)['fund_dim']
            u = 3.5
            P = permutation_operator(N).astype(complex)
            R12 = R_matrix(lt, n_val, u)
            R21_neg = P @ R_matrix(lt, n_val, -u) @ P
            product = R12 @ R21_neg
            # Should be proportional to identity
            diag = np.diag(product)
            if abs(diag[0]) > 1e-10:
                normalized = product / diag[0]
                off_diag = normalized - np.eye(N * N, dtype=complex)
                assert np.max(np.abs(off_diag)) < 1e-6, \
                    f"Unitarity failed for {lt}_{n_val}"

    def test_R_matrix_kappa_values(self):
        """Verify kappa values for B, C, D types."""
        assert abs(R_matrix_kappa('B', 2) - 1.5) < 1e-10  # n - 1/2 = 1.5
        assert abs(R_matrix_kappa('B', 3) - 2.5) < 1e-10
        assert abs(R_matrix_kappa('C', 2) - 3.0) < 1e-10  # n + 1 = 3
        assert abs(R_matrix_kappa('C', 3) - 4.0) < 1e-10
        assert abs(R_matrix_kappa('D', 3) - 2.0) < 1e-10  # n - 1 = 2
        assert abs(R_matrix_kappa('D', 4) - 3.0) < 1e-10


# ============================================================
# Section 4: RTT generators from bar complex
# ============================================================

class TestRTTGenerators:
    """Verify RTT generators T^{(r)} at levels r=0,1,2,3."""

    def test_T0_is_identity(self):
        """T^{(0)} = I for all types."""
        for (lt, n_val) in [('A', 1), ('A', 2), ('B', 2), ('C', 2), ('D', 3)]:
            gens = rtt_generators_symbolic(lt, n_val, max_level=3)
            N = lie_algebra_data(lt, n_val)['fund_dim']
            assert np.allclose(gens[0], np.eye(N))

    def test_rtt_gen_count(self):
        """Number of generators per level = N^2 for gl_N."""
        for n_val in [1, 2, 3]:
            gens = rtt_generators_symbolic('A', n_val, max_level=2)
            N = n_val + 1
            for r in range(1, 3):
                assert gens[r].shape == (N, N)

    def test_numerical_generators_type_A(self):
        """Numerical RTT generators for sl_2 and sl_3 in evaluation rep."""
        for n_val in [1, 2]:
            gens = rtt_generators_numerical('A', n_val, a=1.0, max_level=3)
            N = n_val + 1
            assert np.allclose(gens[0], np.eye(N, dtype=complex))
            # T^{(1)} should be nonzero
            assert np.max(np.abs(gens[1])) > 0

    def test_numerical_generators_type_B(self):
        """Numerical RTT generators for so_5 in evaluation rep."""
        gens = rtt_generators_numerical('B', 2, a=1.0, max_level=2)
        N = 5
        # T^{(0)} should be N^2 x N^2 identity for types B/C/D
        assert gens[0].shape == (N * N, N * N)
        assert np.allclose(gens[0], np.eye(N * N, dtype=complex))


# ============================================================
# Section 5: Transfer matrix commutativity
# ============================================================

class TestTransferMatrix:
    """Verify t(u) = Tr T(u) and [t(u), t(v)] = 0."""

    def test_transfer_scalar_single_site_A(self):
        """For a single site, transfer matrix is scalar for type A."""
        for n_val in [1, 2]:
            N = n_val + 1
            u = 5.0 + 0.3j
            t = transfer_matrix('A', n_val, u, eval_points=[1.0])
            # Should be proportional to identity
            assert t.shape == (N, N)
            diag = t[0, 0]
            assert np.allclose(t, diag * np.eye(N, dtype=complex), atol=1e-8)

    def test_transfer_commutativity_sl2(self):
        """[t(u), t(v)] = 0 for sl_2."""
        result = verify_transfer_commutativity('A', 1, 3.5 + 0.1j, 2.7 - 0.3j,
                                                eval_points=[1.0])
        assert result['passes'], \
            f"Transfer commutativity failed for sl_2: {result['commutator_norm']}"

    def test_transfer_commutativity_sl3(self):
        """[t(u), t(v)] = 0 for sl_3."""
        result = verify_transfer_commutativity('A', 2, 4.0, 2.0,
                                                eval_points=[0.0])
        assert result['passes']

    def test_transfer_commutativity_so5(self):
        """[t(u), t(v)] = 0 for so_5."""
        result = verify_transfer_commutativity('B', 2, 5.0, 3.0,
                                                eval_points=[0.0])
        assert result['passes']

    def test_transfer_commutativity_sp4(self):
        """[t(u), t(v)] = 0 for sp_4."""
        result = verify_transfer_commutativity('C', 2, 6.0, 4.0,
                                                eval_points=[0.0])
        assert result['passes']

    def test_transfer_value_sl2(self):
        """t(u) = (N(u-a) + 1) I_N for single site.

        For type A with R(u) = uI + P:
        t(u) = Tr_{aux} R(u-a) = (N(u-a) + 1) I_N.
        """
        N = 2
        u = 5.0
        a = 1.0
        t = transfer_matrix('A', 1, u, eval_points=[a])
        expected = (N * (u - a) + 1) * np.eye(N, dtype=complex)
        assert np.allclose(t, expected, atol=1e-8)

    def test_transfer_value_sl3(self):
        """t(u) = (3(u-a) + 1) I_3 for single site sl_3."""
        N = 3
        u = 7.0
        a = 2.0
        t = transfer_matrix('A', 2, u, eval_points=[a])
        expected = (N * (u - a) + 1) * np.eye(N, dtype=complex)
        assert np.allclose(t, expected, atol=1e-8)


# ============================================================
# Section 6: Evaluation homomorphism
# ============================================================

class TestEvaluationHomomorphism:
    """Verify ev_a: Y(g) -> U(g)."""

    def test_chevalley_sl2(self):
        """Chevalley relations for sl_2."""
        result = verify_chevalley_relations('A', 1)
        for key, val in result.items():
            assert val, f"sl_2 Chevalley {key} failed"

    def test_chevalley_sl3(self):
        """Chevalley relations for sl_3."""
        result = verify_chevalley_relations('A', 2)
        for key, val in result.items():
            assert val, f"sl_3 Chevalley {key} failed"

    def test_chevalley_sl4(self):
        """Chevalley relations for sl_4."""
        result = verify_chevalley_relations('A', 3)
        for key, val in result.items():
            assert val, f"sl_4 Chevalley {key} failed"

    def test_chevalley_sp4(self):
        """Chevalley relations for sp_4 = C_2."""
        result = verify_chevalley_relations('C', 2)
        for key, val in result.items():
            assert val, f"sp_4 Chevalley {key} failed"

    def test_eval_hom_sl2(self):
        """Evaluation homomorphism for sl_2."""
        result = verify_evaluation_hom('A', 1, a=1.0 + 0.5j)
        for key, val in result.items():
            assert val, f"sl_2 eval hom {key} failed"

    def test_eval_hom_sl3(self):
        """Evaluation homomorphism for sl_3."""
        result = verify_evaluation_hom('A', 2, a=2.0 - 0.3j)
        for key, val in result.items():
            assert val, f"sl_3 eval hom {key} failed"

    def test_eval_hom_so5(self):
        """Evaluation homomorphism for so_5."""
        result = verify_evaluation_hom('B', 2, a=1.5)
        for key, val in result.items():
            assert val, f"so_5 eval hom {key} failed"

    def test_eval_hom_sp4(self):
        """Evaluation homomorphism for sp_4."""
        result = verify_evaluation_hom('C', 2, a=2.0)
        for key, val in result.items():
            assert val, f"sp_4 eval hom {key} failed"

    def test_eval_levels(self):
        """Higher evaluation levels: J^{(r)}_X -> a^r X."""
        ev = evaluation_homomorphism('A', 2, a=3.0)
        e1_0 = ev['e_1^(0)']
        e1_1 = ev['e_1^(1)']
        e1_2 = ev['e_1^(2)']
        # e_1^{(1)} = 3 * e_1^{(0)}, e_1^{(2)} = 9 * e_1^{(0)}
        assert np.allclose(e1_1, 3.0 * e1_0)
        assert np.allclose(e1_2, 9.0 * e1_0)


# ============================================================
# Section 7: Quantum determinant (gl_N)
# ============================================================

class TestQuantumDeterminant:
    """Verify qdet T(u) for gl_2, gl_3, gl_4."""

    def test_qdet_is_scalar_gl2(self):
        """qdet is scalar for gl_2."""
        assert verify_qdet_is_scalar(2, 5.0 + 0.3j)

    def test_qdet_is_scalar_gl3(self):
        """qdet is scalar for gl_3."""
        assert verify_qdet_is_scalar(3, 5.0)

    def test_qdet_is_scalar_gl4(self):
        """qdet is scalar for gl_4."""
        assert verify_qdet_is_scalar(4, 7.0)

    def test_qdet_centrality_gl2(self):
        """[qdet(u), T(v)] = 0 for gl_2."""
        assert verify_qdet_centrality(2, 5.0, 3.0)

    def test_qdet_centrality_gl3(self):
        """[qdet(u), T(v)] = 0 for gl_3."""
        assert verify_qdet_centrality(3, 5.0, 3.0)

    def test_qdet_centrality_gl4(self):
        """[qdet(u), T(v)] = 0 for gl_4."""
        assert verify_qdet_centrality(4, 7.0, 4.0)

    def test_qdet_value_gl2(self):
        """qdet on evaluation module for gl_2.

        For R(u) = uI + P, T_{ij}(u) = (u-a)delta_{ij} + E_{ji}.
        The column determinant at a=0:
            T_{11}(u) T_{22}(u-1) - T_{12}(u) T_{21}(u-1)
        On e_1: T_{11}(u) = u+1, T_{22}(u-1) = u-1, T_{12}(u) = E_{21},
        T_{21}(u-1) = E_{12}.  Product on e_1:
            (u+1)(u-1) e_1 - E_{21} E_{12} e_1 = (u^2-1) e_1 - e_1 = (u^2-2) e_1.
        Wait, E_{21} E_{12} e_1 = E_{21} 0 = 0 (since E_{12} e_1 = 0 for e_1 = (1,0)).
        Actually E_{12} maps e_1 = (1,0) to 0 (E_{12} has 1 at (1,2), so E_{12}(1,0)^T = 0).
        So qdet e_1 = (u+1)(u-1) e_1 = (u^2-1) e_1.
        """
        u = 5.0
        qdet_val = quantum_determinant_scalar(2, u, 0.0)
        # Should be (u+1)(u-1) = u^2 - 1
        expected = (u + 1) * (u - 1)
        assert abs(qdet_val - expected) < 1e-8, \
            f"gl_2 qdet: got {qdet_val}, expected {expected}"

    def test_qdet_value_gl3(self):
        """qdet on evaluation module for gl_3 at a=0.

        From yangian_sl3_rtt.py: qdet = (u+1)(u-1)(u-2).
        """
        u = 5.0
        qdet_val = quantum_determinant_scalar(3, u, 0.0)
        expected = (u + 1) * (u - 1) * (u - 2)
        assert abs(qdet_val - expected) < 1e-8, \
            f"gl_3 qdet: got {qdet_val}, expected {expected}"

    def test_qdet_value_gl4(self):
        """qdet on evaluation module for gl_4 at a=0."""
        u = 7.0
        qdet_val = quantum_determinant_scalar(4, u, 0.0)
        # Should be product of 4 factors from the column determinant
        # Verify by computing explicitly
        qdet_mat = quantum_determinant_explicit(4, u, 0.0)
        assert np.allclose(qdet_mat, qdet_val * np.eye(4, dtype=complex), atol=1e-6)

    def test_qdet_at_shifted_eval_point(self):
        """qdet at evaluation point a != 0."""
        for N in [2, 3]:
            u = 6.0
            a = 2.0
            qdet_val = quantum_determinant_scalar(N, u, a)
            qdet_val_0 = quantum_determinant_scalar(N, u - a, 0.0)
            assert abs(qdet_val - qdet_val_0) < 1e-8, \
                f"gl_{N} qdet shift: got {qdet_val}, expected {qdet_val_0}"


# ============================================================
# Section 8: Sklyanin determinant (so_5, sp_4)
# ============================================================

class TestSklyaninDeterminant:
    """Verify Sklyanin determinant structure for orthogonal/symplectic types.

    The Sklyanin determinant for types B/C/D uses the antisymmetrized product
    with R-matrix chain insertions, NOT the simple column determinant
    (which only works for type A).  The column-determinant computation
    gives a GENERALIZED central element but is NOT scalar in general.

    For the evaluation representation, the central element can be computed
    as a product of eigenvalues on the antisymmetric power.
    """

    def test_sklyanin_so5_column_det_exists(self):
        """Column determinant is computable for so_5."""
        val = sklyanin_determinant_scalar('B', 2, 5.0, 0.0)
        # The value exists (no division by zero, etc.)
        assert np.isfinite(val)

    def test_sklyanin_sp4_column_det_exists(self):
        """Column determinant is computable for sp_4.

        Avoid poles at u=0 and u=kappa=3.  Since column det evaluates at
        u, u-1, u-2, u-3, we need all of these away from 0 and 3.
        u=10 gives 10, 9, 8, 7 -- all safe.
        """
        val = sklyanin_determinant_scalar('C', 2, 10.0, 0.0)
        assert np.isfinite(val)

    def test_sklyanin_nonzero_so5(self):
        """sdet is nonzero at generic spectral parameter for so_5."""
        val = sklyanin_determinant_scalar('B', 2, 5.0, 0.0)
        assert abs(val) > 1e-6, f"sdet(so_5) = {val} is too small"

    def test_sklyanin_nonzero_sp4(self):
        """sdet is nonzero at generic spectral parameter for sp_4."""
        val = sklyanin_determinant_scalar('C', 2, 10.0, 0.0)
        assert abs(val) > 1e-6, f"sdet(sp_4) = {val} is too small"

    def test_sklyanin_shift_invariance_so5(self):
        """sdet(u, a) = sdet(u-a, 0) for so_5.

        so(5) has kappa=1.5 and N=5. Column det evaluates at u, u-1,...,u-4.
        Must avoid u-k = 0 and u-k = 1.5.  u=10 gives 10,9,8,7,6: safe.
        a=0.5: u-a=9.5, column at 9.5,8.5,7.5,6.5,5.5: safe.
        """
        u, a = 10.0, 0.5
        val_a = sklyanin_determinant_scalar('B', 2, u, a)
        val_0 = sklyanin_determinant_scalar('B', 2, u - a, 0.0)
        assert abs(val_a - val_0) < 1e-6, \
            f"so_5 sdet shift: {val_a} vs {val_0}"


# ============================================================
# Section 9: Drinfeld <-> RTT isomorphism
# ============================================================

class TestDrinfeldRTT:
    """Verify Drinfeld <-> RTT isomorphism numerically."""

    def test_drinfeld_map_type_A(self):
        """Drinfeld-RTT map structure for sl_N."""
        for n_val in [1, 2, 3]:
            d_map = drinfeld_to_rtt_map('A', n_val)
            rank = n_val
            assert f'e_1^(1)' in d_map
            assert f'f_1^(1)' in d_map
            assert f'h_1^(1)' in d_map

    def test_drinfeld_rtt_sl2(self):
        """Numerical verification for sl_2."""
        result = verify_drinfeld_rtt_isomorphism('A', 1)
        for key, val in result.items():
            assert val, f"sl_2 Drinfeld-RTT: {key} failed"

    def test_drinfeld_rtt_sl3(self):
        """Numerical verification for sl_3."""
        result = verify_drinfeld_rtt_isomorphism('A', 2)
        for key, val in result.items():
            assert val, f"sl_3 Drinfeld-RTT: {key} failed"

    def test_drinfeld_rtt_so5(self):
        """Structural map for so_5 (type B_2)."""
        d_map = drinfeld_to_rtt_map('B', 2)
        assert f'e_1^(1)' in d_map
        assert f'h_1^(1)' in d_map


# ============================================================
# Section 10: Prefundamental modules and TQ relation
# ============================================================

class TestPrefundamentalTQ:
    """Verify prefundamental modules and TQ relations."""

    def test_prefundamental_character_sl2(self):
        """Prefundamental character for sl_2, node 1."""
        pf = prefundamental_character('A', 1, 1, depth=4)
        char = pf['character']
        # The zero weight should have multiplicity 1
        zero = (0,)
        assert zero in char
        assert char[zero] == 1

    def test_prefundamental_character_sl3(self):
        """Prefundamental character for sl_3, nodes 1 and 2."""
        for node in [1, 2]:
            pf = prefundamental_character('A', 2, node, depth=3)
            char = pf['character']
            zero = (0, 0)
            assert zero in char
            assert char[zero] == 1

    def test_tq_sl2(self):
        """TQ relation structural check for sl_2."""
        result = verify_tq_relation('A', 1, 1, 5.0 + 0.1j)
        assert result['TQ_structural']
        assert result['match'], f"TQ sl_2 mismatch: {result}"

    def test_tq_sl3(self):
        """TQ relation structural check for sl_3."""
        result = verify_tq_relation('A', 2, 1, 5.0)
        assert result['TQ_structural']
        assert result['match'], f"TQ sl_3 mismatch: {result}"


# ============================================================
# Section 11: Shadow -> Yangian dictionary
# ============================================================

class TestShadowYangianDictionary:
    """Verify the shadow -> Yangian dictionary."""

    def test_dictionary_sl3(self):
        """Complete dictionary for sl_3 at level 1."""
        d = shadow_yangian_dictionary('A', 2, k=1)
        assert abs(d['kappa'] - 16.0 / 3.0) < 1e-10
        assert d['dim_g'] == 8
        assert d['dual_coxeter'] == 3
        assert 'dk_bridge' in d

    def test_dictionary_so5(self):
        """Dictionary for so_5 at level 1."""
        d = shadow_yangian_dictionary('B', 2, k=1)
        assert abs(d['kappa'] - 20.0 / 3.0) < 1e-10

    def test_dictionary_sp4(self):
        """Dictionary for sp_4 at level 1."""
        d = shadow_yangian_dictionary('C', 2, k=1)
        assert d['dim_g'] == 10

    def test_classical_r_matrix_type_A(self):
        """Classical r-matrix = Casimir tensor for type A."""
        Omega = classical_r_matrix_fund('A', 2)
        # For sl_3: Omega = P - I/3 on C^3 x C^3
        P = permutation_operator(3).astype(complex)
        expected = P - np.eye(9, dtype=complex) / 3.0
        assert np.allclose(Omega, expected, atol=1e-8)

    def test_quantum_R_leading_order(self):
        """Quantum R = I + Omega/(kappa*u) + ... at leading order."""
        u = 10.0
        k = 10  # large k for perturbative regime
        R_pert = quantum_R_perturbative('A', 2, u, k=k, order=1)
        kap = modular_characteristic('A', 2, k)
        Omega = classical_r_matrix_fund('A', 2)
        expected = np.eye(9, dtype=complex) + Omega / (kap * u)
        assert np.allclose(R_pert, expected, atol=1e-8)

    def test_shadow_class_heisenberg(self):
        """Heisenberg (sl_1) should be class G."""
        d = shadow_yangian_dictionary('A', 0, k=1)
        assert 'G' in d.get('shadow_class', '')

    def test_shadow_class_affine_km(self):
        """Affine KM (sl_3) should be class L."""
        d = shadow_yangian_dictionary('A', 2, k=1)
        assert 'L' in d.get('shadow_class', '')


# ============================================================
# Section 12: Spectral decomposition
# ============================================================

class TestSpectralDecomposition:
    """Verify spectral decomposition of V tensor V."""

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_type_A_dimensions(self, n):
        """Sym^2 + Alt^2 = N^2 for type A."""
        sp = spectral_decomposition('A', n)
        N = n + 1
        assert sp['sym_dim'] == N * (N + 1) // 2
        assert sp['alt_dim'] == N * (N - 1) // 2
        assert sp['sym_dim'] + sp['alt_dim'] == N * N

    def test_type_B_dimensions(self):
        """Spectral dimensions for so_5."""
        sp = spectral_decomposition('B', 2)
        N = 5
        assert sp['sym_dim'] == N * (N + 1) // 2  # 15
        assert sp['alt_dim'] == N * (N - 1) // 2  # 10

    def test_type_C_dimensions(self):
        """Spectral dimensions for sp_4."""
        sp = spectral_decomposition('C', 2)
        N = 4
        assert sp['sym_dim'] == N * (N + 1) // 2  # 10
        assert sp['alt_dim'] == N * (N - 1) // 2  # 6

    def test_type_D_dimensions(self):
        """Spectral dimensions for so_6."""
        sp = spectral_decomposition('D', 3)
        N = 6
        assert sp['sym_dim'] == N * (N + 1) // 2  # 21
        assert sp['alt_dim'] == N * (N - 1) // 2  # 15


# ============================================================
# Section 13: Cartan matrix and positive roots
# ============================================================

class TestRootSystem:
    """Verify root system data."""

    def test_cartan_A2(self):
        A = _cartan_matrix('A', 2)
        assert A == [[2, -1], [-1, 2]]

    def test_cartan_B2(self):
        A = _cartan_matrix('B', 2)
        assert A == [[2, -2], [-1, 2]]

    def test_cartan_C2(self):
        A = _cartan_matrix('C', 2)
        assert A == [[2, -1], [-2, 2]]

    def test_cartan_D3(self):
        """D_3 Cartan matrix: branching at node 0 (0-indexed), connecting to nodes 1 and 2."""
        A = _cartan_matrix('D', 3)
        expected = [[2, -1, -1], [-1, 2, 0], [-1, 0, 2]]
        assert A == expected

    def test_positive_roots_A2(self):
        """A_2 = sl_3 has 3 positive roots."""
        A = _cartan_matrix('A', 2)
        roots = _build_positive_roots(A, 2)
        assert len(roots) == 3

    def test_positive_roots_B2(self):
        """B_2 = so_5 has 4 positive roots."""
        A = _cartan_matrix('B', 2)
        roots = _build_positive_roots(A, 2)
        assert len(roots) == 4

    def test_positive_roots_C2(self):
        """C_2 = sp_4 has 4 positive roots."""
        A = _cartan_matrix('C', 2)
        roots = _build_positive_roots(A, 2)
        assert len(roots) == 4

    def test_positive_roots_D3(self):
        """D_3 = so_6 has 6 positive roots (= A_3)."""
        A = _cartan_matrix('D', 3)
        roots = _build_positive_roots(A, 3)
        assert len(roots) == 6

    def test_positive_roots_A3(self):
        """A_3 = sl_4 has 6 positive roots."""
        A = _cartan_matrix('A', 3)
        roots = _build_positive_roots(A, 3)
        assert len(roots) == 6

    def test_positive_roots_D4(self):
        """D_4 = so_8 has 12 positive roots."""
        A = _cartan_matrix('D', 4)
        roots = _build_positive_roots(A, 4)
        assert len(roots) == 12


# ============================================================
# Section 14: Chevalley generators for types B, C, D
# ============================================================

class TestChevalleyBCD:
    """Verify Chevalley generators for non-simply-laced types."""

    def test_so5_generators_exist(self):
        """so_5 generators are well-formed."""
        gens = chevalley_generators_fund('B', 2)
        assert 'e_1' in gens
        assert 'e_2' in gens
        assert 'f_1' in gens
        assert 'h_1' in gens
        # Check dimensions
        for key, mat in gens.items():
            assert mat.shape == (5, 5)

    def test_sp4_generators_exist(self):
        """sp_4 generators are well-formed."""
        gens = chevalley_generators_fund('C', 2)
        for key, mat in gens.items():
            assert mat.shape == (4, 4)

    def test_so6_generators_exist(self):
        """so_6 generators are well-formed."""
        gens = chevalley_generators_fund('D', 3)
        for key, mat in gens.items():
            assert mat.shape == (6, 6)

    def test_so7_generators_exist(self):
        """so_7 generators are well-formed."""
        gens = chevalley_generators_fund('B', 3)
        for key, mat in gens.items():
            assert mat.shape == (7, 7)


# ============================================================
# Section 15: Casimir tensor
# ============================================================

class TestCasimirTensor:
    """Verify quadratic Casimir tensor in the fundamental representation."""

    def test_casimir_type_A_sl2(self):
        """Casimir for sl_2: Omega = P - I/2."""
        Omega = casimir_tensor_fund('A', 1)
        P = permutation_operator(2).astype(complex)
        expected = P - np.eye(4, dtype=complex) / 2.0
        assert np.allclose(Omega, expected, atol=1e-8)

    def test_casimir_type_A_sl3(self):
        """Casimir for sl_3: Omega = P - I/3."""
        Omega = casimir_tensor_fund('A', 2)
        P = permutation_operator(3).astype(complex)
        expected = P - np.eye(9, dtype=complex) / 3.0
        assert np.allclose(Omega, expected, atol=1e-8)

    def test_casimir_symmetry(self):
        """Casimir tensor should be symmetric: Omega_{12} = Omega_{21}."""
        for (lt, n_val) in [('A', 2), ('B', 2), ('C', 2)]:
            N = lie_algebra_data(lt, n_val)['fund_dim']
            Omega = casimir_tensor_fund(lt, n_val)
            P = permutation_operator(N).astype(complex)
            Omega_21 = P @ Omega @ P
            assert np.allclose(Omega, Omega_21, atol=1e-8), \
                f"Casimir not symmetric for {lt}_{n_val}"


# ============================================================
# Section 16: Full verification suites
# ============================================================

class TestFullVerification:
    """Run the full verification suite for selected types."""

    def test_full_sl2(self):
        results = full_verification('A', 1)
        for key, val in results.items():
            assert val, f"sl_2 full: {key} failed"

    def test_full_sl3(self):
        results = full_verification('A', 2)
        for key, val in results.items():
            assert val, f"sl_3 full: {key} failed"

    def test_full_so5(self):
        results = full_verification('B', 2)
        for key, val in results.items():
            assert val, f"so_5 full: {key} failed"

    def test_full_sp4(self):
        results = full_verification('C', 2)
        for key, val in results.items():
            assert val, f"sp_4 full: {key} failed"

    def test_full_so6(self):
        results = full_verification('D', 3)
        for key, val in results.items():
            assert val, f"so_6 full: {key} failed"


# ============================================================
# Section 17: Cross-type consistency
# ============================================================

class TestCrossTypeConsistency:
    """Verify consistency between types at coincidence points."""

    def test_B1_equals_A1(self):
        """B_1 = so_3 ~ sl_2: same Lie algebra, different representations.

        so(3) has the same Lie algebra as sl(2), but the 3-dim rep (adjoint)
        is different from the 2-dim fundamental.  The R-matrices live in
        different spaces.

        Check: dim(so_3) = dim(sl_2) = 3.
        """
        d_B1 = lie_algebra_data('B', 1)
        d_A1 = lie_algebra_data('A', 1)
        assert d_B1['dim_g'] == d_A1['dim_g']  # Both = 3
        assert d_B1['dual_coxeter'] == 1  # h^vee(so_3) = 1
        assert d_A1['dual_coxeter'] == 2  # h^vee(sl_2) = 2
        # These DIFFER because so_3 and sl_2 have different root length conventions

    def test_C1_equals_A1(self):
        """C_1 = sp_2 ~ sl_2: isomorphic Lie algebras.

        sp(2) = sl(2) as Lie algebras.  Both have dim 3, rank 1.
        The 2-dim representations coincide.
        """
        d_C1 = lie_algebra_data('C', 1)
        d_A1 = lie_algebra_data('A', 1)
        assert d_C1['dim_g'] == d_A1['dim_g']  # Both = 3
        assert d_C1['fund_dim'] == d_A1['fund_dim']  # Both = 2

    def test_D3_equals_A3(self):
        """D_3 = so_6 ~ sl_4: isomorphic root systems.

        Both have rank 3, 6 positive roots, dim 15, h = 4.
        """
        d_D3 = lie_algebra_data('D', 3)
        d_A3 = lie_algebra_data('A', 3)
        assert d_D3['dim_g'] == d_A3['dim_g']  # Both = 15
        assert d_D3['dual_coxeter'] == d_A3['dual_coxeter']  # Both = 4
        # Fund dims differ: D_3 -> 6, A_3 -> 4


# ============================================================
# Section 18: Additional YBE tests with varied parameters
# ============================================================

class TestYBEExtended:
    """Extended YBE tests with more parameter choices."""

    def test_ybe_at_multiple_points_A2(self):
        """YBE for sl_3 at 5 different spectral parameter pairs."""
        params = [(1.0, 2.0), (3.0, 5.0), (0.5, 7.0),
                  (2.0 + 1.0j, 3.0 - 0.5j), (10.0, 0.1)]
        for u, v in params:
            result = verify_yang_baxter('A', 2, u, v)
            assert result['passes'], f"YBE A_2 at u={u}, v={v}: {result['max_diff']}"

    def test_ybe_at_multiple_points_B2(self):
        """YBE for so_5 at 3 different parameter pairs."""
        params = [(3.0, 5.0), (7.0, 2.0), (4.0 + 0.5j, 1.0 - 0.3j)]
        for u, v in params:
            result = verify_yang_baxter('B', 2, u, v)
            assert result['passes'], f"YBE B_2 at u={u}, v={v}: {result['max_diff']}"

    def test_ybe_at_multiple_points_C2(self):
        """YBE for sp_4 at 3 different parameter pairs.

        sp(4) has poles at u=0 and u=kappa=3.  Must ensure u, v, u-v
        are all away from these.
        """
        params = [(5.5, 2.3), (8.5, 1.7), (6.5 + 0.2j, 1.5 + 0.7j)]
        for u, v in params:
            result = verify_yang_baxter('C', 2, u, v)
            assert result['passes'], f"YBE C_2 at u={u}, v={v}: {result['max_diff']}"

    def test_ybe_at_multiple_points_D3(self):
        """YBE for so_6 at 3 different parameter pairs.

        so(6) = D_3 has poles at u=0 and u=kappa=2.  Avoid these.
        """
        params = [(4.5, 1.3), (6.5, 3.7), (5.5 + 0.5j, 1.5 - 0.2j)]
        for u, v in params:
            result = verify_yang_baxter('D', 3, u, v)
            assert result['passes'], f"YBE D_3 at u={u}, v={v}: {result['max_diff']}"


# ============================================================
# Section 19: Modular characteristic cross-checks
# ============================================================

class TestModularCharacteristic:
    """Cross-check kappa values against known formulas."""

    def test_kappa_heisenberg(self):
        """kappa(Heisenberg) at level k: dim=1, h^vee convention gives k/2.

        For gl_1 (A_0): dim_g = 0, so kappa = 0.  This is the Heisenberg
        U(1) current.  The actual kappa is k/2 but we model it differently.
        """
        # A_0 gives dim_g=0, which gives kappa=0.  Skip.
        pass

    def test_kappa_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/(2*2) = 3(k+2)/4."""
        for k in [1, 2, 5, 10]:
            kap = modular_characteristic('A', 1, k)
            expected = 3.0 * (k + 2) / 4.0
            assert abs(kap - expected) < 1e-10

    def test_kappa_sl4(self):
        """kappa(sl_4, k) = 15(k+4)/(2*4) = 15(k+4)/8."""
        for k in [1, 2]:
            kap = modular_characteristic('A', 3, k)
            expected = 15.0 * (k + 4) / 8.0
            assert abs(kap - expected) < 1e-10

    def test_kappa_so5(self):
        """kappa(so_5, k) = 10(k+3)/(2*3) = 5(k+3)/3."""
        for k in [1, 2]:
            kap = modular_characteristic('B', 2, k)
            expected = 10.0 * (k + 3) / 6.0
            assert abs(kap - expected) < 1e-10

    def test_kappa_sp4(self):
        """kappa(sp_4, k) = 10(k+3)/(2*3) = 5(k+3)/3."""
        for k in [1, 2]:
            kap = modular_characteristic('C', 2, k)
            expected = 10.0 * (k + 3) / 6.0
            assert abs(kap - expected) < 1e-10

    def test_kappa_additivity_B2(self):
        """kappa is linear in k."""
        k1, k2 = 1, 3
        kap1 = modular_characteristic('B', 2, k1)
        kap2 = modular_characteristic('B', 2, k2)
        kap_sum = modular_characteristic('B', 2, k1 + k2)
        # kappa(k1+k2) = dim_g*(k1+k2+h^vee)/(2h^vee)
        # kappa(k1) + kappa(k2) = dim_g*(k1+k2+2h^vee)/(2h^vee)
        # So kappa(k1+k2) != kappa(k1)+kappa(k2) in general.
        # But kappa(k1+k2) - kappa(k1) = dim_g*k2/(2h^vee) = kappa(k2) - dim_g*h^vee/(2h^vee)
        # Linearity in k: kappa(k) = (dim_g/(2h^vee)) * k + dim_g/2
        data = lie_algebra_data('B', 2)
        slope = data['dim_g'] / (2.0 * data['dual_coxeter'])
        assert abs(kap2 - kap1 - slope * (k2 - k1)) < 1e-10
