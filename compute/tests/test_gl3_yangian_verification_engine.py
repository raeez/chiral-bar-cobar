r"""Tests for the gl_3 Yangian verification engine.

Complete N=3 worked verification of thm:glN-chiral-qg:
    1. The explicit 9x9 Yang R-matrix.
    2. Yang-Baxter equation at 6+ parameter sets.
    3. RTT gives the sl_3 Yangian relations.
    4. Quantum determinant for 3x3.

Ground truth references:
    - Molev, "Yangians and Classical Lie Algebras", AMS 2007.
    - Chari-Pressley, "A Guide to Quantum Groups", Cambridge 1994.
    - VERIFIED: R(u) = u I + Psi P satisfies YBE (textbook, Molev Ch. 1) [LT].
    - VERIFIED: qdet T(u) central in Y(gl_3) (Molev Thm 1.11.2) [LT].
    - VERIFIED: [t^{(1)}_{ij}, t^{(1)}_{kl}] = Psi(delta_{kj} t^{(1)}_{il}
                - delta_{il} t^{(1)}_{kj}) (gl_3 Lie bracket) [DC] + [LT].
    - VERIFIED: P eigenvalues +1 (6-fold) and -1 (3-fold) by
                dim Sym^2(C^3)=6, dim Alt^2(C^3)=3 [DC] + [DA].
    - VERIFIED: R(u)R(-u) = (Psi^2 - u^2)I (direct computation) [DC].
    - VERIFIED: Explicit 9x9 matrix entries by hand [DC].
"""

import pytest
import numpy as np

from compute.lib.gl3_yangian_verification_engine import (
    # Fundamental operators
    permutation_matrix_gl3,
    identity_9,
    # R-matrices
    yang_r_matrix_gl3,
    yang_r_matrix_gl3_explicit_entries,
    classical_r_matrix_gl3,
    # YBE
    verify_ybe_gl3,
    # RTT
    verify_rtt_gl3,
    verify_rtt_nontrivial_gl3,
    rtt_level1_commutator_gl3,
    # Quantum determinant
    quantum_determinant_gl3,
    quantum_determinant_gl3_6terms,
    verify_qdet_scalar_gl3,
    verify_qdet_two_methods_gl3,
    qdet_classical_limit_gl3,
    qdet_explicit_value_gl3,
    # R-matrix properties
    verify_r_matrix_properties_gl3,
    # Spectral decomposition
    spectral_decomposition_gl3,
    # Drinfeld coproduct
    drinfeld_coproduct_gl3,
    verify_coproduct_coassociativity_gl3,
    # Explicit entries
    explicit_R_matrix_gl3_Psi1_u2,
    explicit_P_matrix_gl3,
    # Full suite
    full_gl3_verification,
)


# ============================================================
# Section 1: Explicit 9x9 permutation matrix
# ============================================================

class TestPermutationMatrixGL3:
    """Test the 9x9 permutation matrix P on C^3 tensor C^3."""

    def test_P_squared_is_identity(self):
        """P^2 = I_9."""
        # VERIFIED: P is an involution [DC] + definition [LT]
        P = permutation_matrix_gl3()
        I9 = identity_9()
        assert np.allclose(P @ P, I9), "P^2 != I_9"

    def test_P_trace_equals_3(self):
        """Tr(P) = N = 3."""
        # VERIFIED: Tr(P) = sum delta_{ii} = N [DC] + Molev [LT]
        P = permutation_matrix_gl3()
        assert abs(np.trace(P) - 3.0) < 1e-12, f"Tr(P) = {np.trace(P)}, expected 3"

    def test_P_eigenvalues(self):
        """P eigenvalues: +1 (6-fold, Sym^2 C^3) and -1 (3-fold, Alt^2 C^3)."""
        # VERIFIED: dim Sym^2(C^3) = 3*4/2 = 6, dim Alt^2(C^3) = 3*2/2 = 3 [DC] + [DA]
        P = permutation_matrix_gl3()
        evals = np.sort(np.real(np.linalg.eigvals(P)))
        expected = np.sort([-1.0] * 3 + [1.0] * 6)
        assert np.allclose(evals, expected), f"Eigenvalues: {evals}"

    def test_P_is_symmetric(self):
        """P is a symmetric matrix: P = P^T."""
        # VERIFIED: P_{(ij),(kl)} = delta_{il}delta_{jk} = P_{(kl),(ij)} [DC]
        P = permutation_matrix_gl3()
        assert np.allclose(P, P.T), "P is not symmetric"

    def test_P_explicit_entries(self):
        """Check P against the explicit 9x9 matrix."""
        # VERIFIED: hand-computed entry by entry [DC]
        P_computed, P_expected = explicit_P_matrix_gl3()
        assert np.allclose(P_computed, P_expected), (
            f"P mismatch:\n{P_computed}\nvs expected:\n{P_expected}"
        )

    def test_P_swap_specific_vectors(self):
        """P(e_1 tensor e_2) = e_2 tensor e_1."""
        # VERIFIED: definition P(e_i tensor e_j) = e_j tensor e_i [DC]
        P = permutation_matrix_gl3()
        # e_1 tensor e_2 = basis vector index 0*3+1 = 1
        v = np.zeros(9, dtype=complex)
        v[1] = 1.0  # e_1 tensor e_2
        Pv = P @ v
        expected = np.zeros(9, dtype=complex)
        expected[3] = 1.0  # e_2 tensor e_1 = index 1*3+0 = 3
        assert np.allclose(Pv, expected), f"P(e1 tensor e2) = {Pv}"


# ============================================================
# Section 2: Explicit 9x9 R-matrix
# ============================================================

class TestRMatrixGL3:
    """Test the explicit 9x9 Yang R-matrix for gl_3."""

    def test_R_explicit_Psi1_u2(self):
        """R(2) at Psi=1: explicit 9x9 matrix."""
        # VERIFIED: R = 2I + P, hand-computed [DC]
        R_computed, R_expected = explicit_R_matrix_gl3_Psi1_u2()
        assert np.allclose(R_computed, R_expected), (
            f"R(2) mismatch:\nComputed:\n{np.real(R_computed)}\n"
            f"Expected:\n{np.real(R_expected)}"
        )

    def test_R_diagonal_entries(self):
        """R_{(ij),(ij)} = u + Psi delta_{ij}."""
        # VERIFIED: (uI + Psi P)_{(ij),(ij)} = u + Psi P_{(ij),(ij)} = u + Psi delta_{ij} [DC]
        Psi = 1.5
        u = 2.7
        R = yang_r_matrix_gl3(Psi, u)
        for i in range(3):
            for j in range(3):
                idx = i * 3 + j
                expected = u + Psi if i == j else u
                assert abs(R[idx, idx] - expected) < 1e-12, (
                    f"R[({i}{j}),({i}{j})] = {R[idx,idx]}, expected {expected}"
                )

    def test_R_off_diagonal_swap_entries(self):
        """R_{(ij),(ji)} = Psi for i != j."""
        # VERIFIED: P_{(ij),(ji)} = delta_{ii} delta_{jj} = 1 for all i,j [DC]
        Psi = 2.3
        u = 1.1
        R = yang_r_matrix_gl3(Psi, u)
        for i in range(3):
            for j in range(3):
                if i != j:
                    row = i * 3 + j
                    col = j * 3 + i
                    assert abs(R[row, col] - Psi) < 1e-12, (
                        f"R[({i}{j}),({j}{i})] = {R[row,col]}, expected {Psi}"
                    )

    def test_two_constructions_agree(self):
        """Matrix-based and entry-by-entry constructions of R agree."""
        # VERIFIED: two independent implementations [DC]
        Psi = 1.7 + 0.3j
        u = 2.5 - 0.4j
        R1 = yang_r_matrix_gl3(Psi, u)
        R2 = yang_r_matrix_gl3_explicit_entries(Psi, u)
        assert np.allclose(R1, R2), "Two R-matrix constructions disagree"

    def test_AP126_R_matrix(self):
        """AP126: at Psi=0, R(u) = u I_9."""
        # VERIFIED: Psi=0 -> Psi P = 0, so R = uI [DC] + AP126 [LT]
        u = 3.0 + 1.0j
        R = yang_r_matrix_gl3(0.0, u)
        assert np.allclose(R, u * identity_9()), "AP126 fails: R(u)|_{Psi=0} != u I"

    def test_AP126_classical_r(self):
        """AP126: at Psi=0, classical r-matrix = 0."""
        # VERIFIED: r(z) = Psi P/z -> 0 at Psi=0 [DC] + AP126 [LT]
        r = classical_r_matrix_gl3(0.0, 1.0)
        assert np.allclose(r, 0.0), "AP126 fails: r|_{Psi=0} != 0"

    def test_unitarity(self):
        """R(u) R(-u) = (Psi^2 - u^2) I_9."""
        # VERIFIED: (uI+Psi P)(-uI+Psi P) = Psi^2 P^2 - u^2 I = (Psi^2-u^2)I [DC] + Molev [LT]
        Psi = 1.0
        u = 2.5 + 0.3j
        R_u = yang_r_matrix_gl3(Psi, u)
        R_neg_u = yang_r_matrix_gl3(Psi, -u)
        product = R_u @ R_neg_u
        expected = (Psi**2 - u**2) * identity_9()
        assert np.allclose(product, expected), "Unitarity R(u)R(-u) != (Psi^2-u^2)I"

    def test_unitarity_specific_numerical(self):
        """Unitarity at Psi=2, u=3: Psi^2-u^2 = 4-9 = -5."""
        # VERIFIED: direct arithmetic [DC] + [NE]
        Psi = 2.0
        u = 3.0
        R_u = yang_r_matrix_gl3(Psi, u)
        R_neg_u = yang_r_matrix_gl3(Psi, -u)
        product = R_u @ R_neg_u
        expected = -5.0 * identity_9()
        assert np.allclose(product, expected), "R(3)R(-3) != -5 I at Psi=2"

    def test_R_at_zero(self):
        """R(0) = Psi P."""
        # VERIFIED: R(0) = 0*I + Psi*P = Psi*P [DC]
        Psi = 1.5
        R = yang_r_matrix_gl3(Psi, 0.0)
        expected = Psi * permutation_matrix_gl3()
        assert np.allclose(R, expected), "R(0) != Psi P"


# ============================================================
# Section 3: Yang-Baxter equation (6+ parameter sets)
# ============================================================

class TestYBEGL3:
    """Verify the Yang-Baxter equation for the 9x9 gl_3 R-matrix."""

    def test_ybe_generic_complex(self):
        """YBE at generic complex spectral parameters."""
        # VERIFIED: textbook [LT] + numerical [NE]
        result = verify_ybe_gl3(1.0, u=3.7+0.3j, v=1.3+0.7j)
        assert result['passes'], f"YBE fails: diff={result['max_diff']}"

    def test_ybe_real_parameters(self):
        """YBE at real spectral parameters."""
        # VERIFIED: [NE] + consistency with complex test [CF]
        result = verify_ybe_gl3(1.0, u=5.0, v=2.0)
        assert result['passes'], f"YBE fails (real): diff={result['max_diff']}"

    def test_ybe_large_spectral(self):
        """YBE at large spectral parameters."""
        # VERIFIED: [NE], R(u) ~ u I dominates; still exact [DC]
        result = verify_ybe_gl3(1.0, u=100.0+3.0j, v=50.0-7.0j)
        assert result['passes'], f"YBE fails (large): diff={result['max_diff']}"

    def test_ybe_small_spectral(self):
        """YBE at small spectral parameters (near the pole)."""
        # VERIFIED: [NE]
        result = verify_ybe_gl3(1.0, u=0.1+0.05j, v=0.03-0.02j)
        assert result['passes'], f"YBE fails (small): diff={result['max_diff']}"

    def test_ybe_Psi_2(self):
        """YBE at Psi=2."""
        # VERIFIED: YBE holds for all Psi [LT] + [NE]
        result = verify_ybe_gl3(2.0, u=4.1+0.2j, v=1.7+0.5j)
        assert result['passes'], f"YBE fails (Psi=2): diff={result['max_diff']}"

    def test_ybe_Psi_half(self):
        """YBE at Psi=0.5."""
        # VERIFIED: [NE]
        result = verify_ybe_gl3(0.5, u=3.0+1.0j, v=1.0-0.5j)
        assert result['passes'], f"YBE fails (Psi=0.5): diff={result['max_diff']}"

    def test_ybe_Psi_0(self):
        """YBE at Psi=0: R = uI, trivially satisfied."""
        # VERIFIED: R=uI commutes with everything [DC] + AP126 [LT]
        result = verify_ybe_gl3(0.0, u=3.0, v=1.0)
        assert result['passes'], f"YBE fails (Psi=0): diff={result['max_diff']}"

    def test_ybe_Psi_negative(self):
        """YBE at negative Psi."""
        # VERIFIED: R(u) = uI + Psi P algebraic in Psi; YBE polynomial identity [DC]
        result = verify_ybe_gl3(-1.5, u=4.0+0.1j, v=2.0-0.3j)
        assert result['passes'], f"YBE fails (Psi<0): diff={result['max_diff']}"

    def test_ybe_Psi_complex(self):
        """YBE at complex Psi."""
        # VERIFIED: YBE is a polynomial identity in Psi; holds for all complex Psi [DC]
        result = verify_ybe_gl3(1.0+0.5j, u=3.0+0.2j, v=1.5-0.1j)
        assert result['passes'], f"YBE fails (complex Psi): diff={result['max_diff']}"


# ============================================================
# Section 4: RTT relation
# ============================================================

class TestRTTGL3:
    """Verify the RTT relation for gl_3."""

    def test_rtt_generic(self):
        """RTT at generic parameters."""
        # VERIFIED: RTT for eval L-op = YBE with shift [DC] + Molev [LT]
        result = verify_rtt_gl3(1.0, u=3.7+0.3j, v=1.3+0.7j)
        assert result['passes'], f"RTT fails: diff={result['max_diff']}"

    def test_rtt_real_parameters(self):
        """RTT at real parameters."""
        # VERIFIED: [NE] + consistency [CF]
        result = verify_rtt_gl3(2.0, u=5.0, v=2.0)
        assert result['passes'], f"RTT fails (real): diff={result['max_diff']}"

    def test_rtt_different_eval_point(self):
        """RTT with non-zero evaluation point a."""
        # VERIFIED: [NE]
        result = verify_rtt_gl3(1.0, u=4.0+0.5j, v=2.0-0.3j, a=1.5)
        assert result['passes'], f"RTT fails (a=1.5): diff={result['max_diff']}"

    def test_rtt_nontrivial(self):
        """RTT is NON-TRIVIAL: [R_{12}, L_{13}] != 0 for N=3."""
        # VERIFIED: P is non-scalar for N=3 [DC] + [DA]
        result = verify_rtt_nontrivial_gl3(1.0)
        assert result['is_nontrivial'], "RTT should be nontrivial for N=3"

    def test_level1_commutation_Psi1(self):
        """Level-1 RTT gives gl_3 Lie bracket at Psi=1.

        [t_{ij}^{(1)}, t_{kl}^{(1)}] = Psi(delta_{il} t_{kj}^{(1)} - delta_{kj} t_{il}^{(1)})
        In eval rep with t_{ij}^{(1)} = Psi E_{ji}, this reduces to the gl_3 bracket.
        """
        # VERIFIED: direct computation in eval rep [DC] + Molev [LT]
        result = rtt_level1_commutator_gl3(Psi=1.0)
        assert result['passes'], (
            f"Level-1 commutator fails at Psi=1: max_error={result['max_error']}"
        )
        assert result['num_checks'] == 81, f"Expected 81 checks, got {result['num_checks']}"

    def test_level1_commutation_Psi2(self):
        """Level-1 RTT gives scaled gl_3 bracket at Psi=2."""
        # VERIFIED: scaling by Psi is consistent [DC]
        result = rtt_level1_commutator_gl3(Psi=2.0)
        assert result['passes'], (
            f"Level-1 commutator fails at Psi=2: max_error={result['max_error']}"
        )


# ============================================================
# Section 5: Quantum determinant for gl_3
# ============================================================

class TestQuantumDeterminantGL3:
    """Test the quantum determinant for 3x3."""

    def test_qdet_is_scalar(self):
        """qdet T(u) is proportional to I_3 (central in Y(gl_3))."""
        # VERIFIED: Molev Thm 1.11.2 [LT] + numerical [NE]
        result = verify_qdet_scalar_gl3(1.0, u=3.5+0.2j)
        assert result['is_scalar'], (
            f"qdet not scalar: deviation={result['deviation_from_scalar']}"
        )

    def test_qdet_scalar_Psi_half(self):
        """qdet is scalar at Psi=0.5."""
        # VERIFIED: centrality holds for all Psi [LT] + [NE]
        result = verify_qdet_scalar_gl3(0.5, u=4.0+0.1j)
        assert result['is_scalar'], (
            f"qdet not scalar (Psi=0.5): deviation={result['deviation_from_scalar']}"
        )

    def test_qdet_scalar_Psi_2(self):
        """qdet is scalar at Psi=2."""
        # VERIFIED: [NE]
        result = verify_qdet_scalar_gl3(2.0, u=5.0-0.3j)
        assert result['is_scalar'], (
            f"qdet not scalar (Psi=2): deviation={result['deviation_from_scalar']}"
        )

    def test_qdet_two_methods_agree(self):
        """Loop-based qdet and explicit 6-term formula agree."""
        # VERIFIED: two independent implementations [DC]
        result = verify_qdet_two_methods_gl3(1.0, u=3.5+0.2j)
        assert result['passes'], (
            f"Two qdet methods disagree: diff={result['max_diff']}"
        )

    def test_qdet_two_methods_Psi2(self):
        """Two qdet methods agree at Psi=2."""
        # VERIFIED: [DC]
        # u=5.0 avoids the pole at u-2*Psi-a = 5-4-0 = 1 != 0
        result = verify_qdet_two_methods_gl3(2.0, u=5.0+0.3j)
        assert result['passes'], (
            f"Two qdet methods disagree (Psi=2): diff={result['max_diff']}"
        )

    def test_qdet_classical_limit(self):
        """At Psi=0, qdet T(u) = det(I_3) = I_3."""
        # VERIFIED: Psi=0 -> T = I, so det = 1 [DC] + [LC]
        result = qdet_classical_limit_gl3(u=5.0)
        assert result['passes'], (
            f"Classical limit fails: deviation={result['deviation_from_I']}"
        )

    def test_qdet_6terms_explicit(self):
        """Verify 6-term formula gives scalar operator."""
        # VERIFIED: Molev Thm 1.11.2 [LT] + [DC]
        Psi = 1.5
        u = 4.0 + 0.2j
        qdet = quantum_determinant_gl3_6terms(Psi, u)
        trace = np.trace(qdet)
        scalar = trace / 3.0
        deviation = float(np.max(np.abs(qdet - scalar * np.eye(3, dtype=complex))))
        assert deviation < 1e-8, f"6-term qdet not scalar: deviation={deviation}"

    def test_qdet_value_at_Psi1_u5(self):
        """Cross-check qdet scalar value at specific parameters.

        At Psi=1, u=5, a=0: the scalar value of qdet should be consistent
        between the two methods.
        """
        # VERIFIED: [DC] + [NE]
        Psi = 1.0
        u = 5.0
        val_loop = qdet_explicit_value_gl3(Psi, u)
        qdet_6 = quantum_determinant_gl3_6terms(Psi, u)
        val_6term = complex(np.trace(qdet_6) / 3.0)
        assert abs(val_loop - val_6term) < 1e-10, (
            f"qdet values differ: loop={val_loop}, 6term={val_6term}"
        )


# ============================================================
# Section 6: Spectral decomposition
# ============================================================

class TestSpectralDecompositionGL3:
    """Test the spectral decomposition R(u) = (u+Psi) Proj_Sym + (u-Psi) Proj_Alt."""

    def test_projector_ranks(self):
        """Proj_Sym has rank 6, Proj_Alt has rank 3."""
        # VERIFIED: dim Sym^2(C^3) = 6, dim Alt^2(C^3) = 3 [DC] + [DA]
        result = spectral_decomposition_gl3(1.0, 2.0)
        assert result['rank_sym'] == 6, f"rank_sym = {result['rank_sym']}"
        assert result['rank_alt'] == 3, f"rank_alt = {result['rank_alt']}"

    def test_projectors_idempotent(self):
        """Proj_Sym^2 = Proj_Sym, Proj_Alt^2 = Proj_Alt."""
        # VERIFIED: (I+P)/2 and (I-P)/2 are projectors since P^2=I [DC]
        result = spectral_decomposition_gl3(1.0, 2.0)
        assert result['proj_sym_idempotent']
        assert result['proj_alt_idempotent']

    def test_projectors_orthogonal(self):
        """Proj_Sym Proj_Alt = 0."""
        # VERIFIED: (I+P)(I-P) = I - P^2 = 0 [DC]
        result = spectral_decomposition_gl3(1.0, 2.0)
        assert result['projectors_orthogonal']

    def test_R_spectral_decomposition(self):
        """R(u) = (u+Psi) Proj_Sym + (u-Psi) Proj_Alt."""
        # VERIFIED: expand using P = Proj_Sym - Proj_Alt [DC]
        result = spectral_decomposition_gl3(1.5, 2.5+0.3j)
        assert result['R_decomposition_ok'], (
            f"Spectral decomposition fails: deviation={result['R_decomposition_deviation']}"
        )


# ============================================================
# Section 7: Drinfeld coproduct for gl_3
# ============================================================

class TestDrinfeldCoproductGL3:
    """Test the Drinfeld coproduct Delta_z(T(u)) = T(u) . T(u-z)."""

    def test_coproduct_identity_at_zero_order(self):
        """With T^{(1)} = 0: Delta_z(I) = I."""
        # VERIFIED: I . I = I [DC]
        T1 = np.zeros((3, 3), dtype=complex)
        result = drinfeld_coproduct_gl3(5.0, 1.0, T1, T1)
        assert np.allclose(result, np.eye(3)), "Delta_z(I) != I"

    def test_coproduct_matrix_multiplication(self):
        """Delta_z(T(u)) = T(u) . T(u-z) for random T^{(1)}."""
        # VERIFIED: definition of Drinfeld coproduct [DC] + Molev [LT]
        rng = np.random.default_rng(137)
        T1_L = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        T1_R = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        u = 5.0
        z = 1.0
        result = drinfeld_coproduct_gl3(u, z, T1_L, T1_R)
        T_u = np.eye(3) + T1_L / u
        T_uz = np.eye(3) + T1_R / (u - z)
        expected = T_u @ T_uz
        assert np.allclose(result, expected), "Coproduct != T(u) . T(u-z)"

    def test_coassociativity_at_equal_z(self):
        """At z1=z2, the two triple products agree."""
        # VERIFIED: T(u-z1) = T(u-z2) when z1=z2 [DC]
        rng = np.random.default_rng(42)
        T1 = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        result = verify_coproduct_coassociativity_gl3(5.0, 1.0, 1.0, T1)
        assert result['agrees_when_z_equal'], "Should agree at z1=z2"


# ============================================================
# Section 8: R-matrix properties (comprehensive)
# ============================================================

class TestRMatrixPropertiesGL3:
    """Comprehensive verification of gl_3 R-matrix properties."""

    def test_all_properties(self):
        """Run the full property check."""
        # VERIFIED: all properties at N=3 [DC] + [LT] + [NE]
        result = verify_r_matrix_properties_gl3(1.0, 2.5+0.3j)
        assert result['P_squared_ok'], "P^2 != I"
        assert result['trace_P_ok'], "Tr(P) != 3"
        assert result['eigenvalues_ok'], "P eigenvalues wrong"
        assert result['unitarity_ok'], "Unitarity fails"
        assert result['R_at_zero_ok'], "R(0) != Psi P"
        assert result['AP126_ok'], "AP126 fails"
        assert result['AP126_classical_ok'], "AP126 classical fails"
        assert result['two_methods_ok'], "Two R constructions disagree"


# ============================================================
# Section 9: Full verification suite
# ============================================================

class TestFullGL3Verification:
    """Run the complete gl_3 verification."""

    def test_full_Psi1(self):
        """Full verification at Psi=1."""
        # VERIFIED: all [DC] + [LT] + [NE]
        result = full_gl3_verification(Psi=1.0)
        assert result['all_pass'], f"Full verification fails at Psi=1"

    def test_full_Psi_half(self):
        """Full verification at Psi=0.5."""
        # VERIFIED: [NE]
        result = full_gl3_verification(Psi=0.5)
        assert result['all_pass'], f"Full verification fails at Psi=0.5"

    def test_full_Psi2(self):
        """Full verification at Psi=2."""
        # VERIFIED: [NE]
        result = full_gl3_verification(Psi=2.0)
        assert result['all_pass'], f"Full verification fails at Psi=2"


# ============================================================
# Section 10: Cross-checks with glN engine
# ============================================================

class TestCrossChecksGL3:
    """Cross-checks between gl_3-specific and general glN engine."""

    def test_R_matches_glN_engine(self):
        """gl_3-specific R-matrix matches the glN engine at N=3."""
        # VERIFIED: same formula, independent construction [DC]
        from compute.lib.glN_affine_yangian_chiral_qg_engine import (
            yang_r_matrix_additive,
        )
        Psi = 1.7 + 0.2j
        u = 3.0 - 0.5j
        R_gl3 = yang_r_matrix_gl3(Psi, u)
        R_glN = yang_r_matrix_additive(3, Psi, u)
        assert np.allclose(R_gl3, R_glN), "gl_3 R != glN R at N=3"

    def test_P_matches_glN_engine(self):
        """gl_3-specific P matches the glN engine at N=3."""
        # VERIFIED: [DC]
        from compute.lib.glN_affine_yangian_chiral_qg_engine import (
            permutation_operator,
        )
        P_gl3 = permutation_matrix_gl3()
        P_glN = permutation_operator(3)
        assert np.allclose(P_gl3, P_glN), "gl_3 P != glN P at N=3"

    def test_qdet_matches_glN_engine(self):
        """gl_3-specific qdet matches the glN engine at N=3."""
        # VERIFIED: [DC]
        from compute.lib.glN_affine_yangian_chiral_qg_engine import (
            quantum_determinant_eval,
        )
        Psi = 1.0
        u = 4.0 + 0.2j
        a = 0.0
        qdet_gl3 = quantum_determinant_gl3(Psi, u, a)
        qdet_glN = quantum_determinant_eval(3, Psi, u, a)
        assert np.allclose(qdet_gl3, qdet_glN), "gl_3 qdet != glN qdet at N=3"

    def test_ybe_matches_glN_engine(self):
        """gl_3-specific YBE matches the glN engine."""
        # VERIFIED: [DC]
        from compute.lib.glN_affine_yangian_chiral_qg_engine import (
            verify_yang_baxter,
        )
        Psi = 1.0
        u = 3.7 + 0.3j
        v = 1.3 + 0.7j
        result_gl3 = verify_ybe_gl3(Psi, u, v)
        result_glN = verify_yang_baxter(3, Psi, u, v)
        assert result_gl3['passes'] and result_glN['passes']
