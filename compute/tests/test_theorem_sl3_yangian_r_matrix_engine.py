r"""Tests for sl_3 Yangian R-matrix from the ordered bar complex.

First rank-2 computation of the Yangian R-matrix from the monograph's
framework, going beyond the well-studied sl_2 case.

Tests organized by:
    1. Fundamental representation consistency
    2. Adjoint representation consistency
    3. Casimir tensor — fundamental (Omega = P - I/3)
    4. Casimir tensor — adjoint (eigenvalue decomposition)
    5. r-matrix pole structure (AP19)
    6. Yang--Baxter equation (fundamental)
    7. Classical Yang--Baxter equation (both representations)
    8. Infinitesimal braid relations / KZ commutativity (n=3,4)
    9. Verlinde fusion rules (levels 1,2,3)
   10. DNP comparison
   11. sl_2 cross-check (rank-1 reduction)
   12. Spectral decomposition (Sym^2 / Lambda^2)
   13. Kappa formula and modular characteristic
   14. Cross-checks with yangian_rmatrix_sl3.py

Ground truth references:
    - sl3_bar.py: structure constants, Killing form, OPE data.
    - yangian_rmatrix_sl3.py: fundamental Casimir, YBE, spectral decomposition.
    - yangian_residue_extraction.py: Yang R-matrix for sl_N.
    - landscape_census.tex: kappa(sl_3_k) = 4(k+3)/3.
"""

import pytest
import numpy as np
from sympy import Rational, Symbol

from compute.lib.theorem_sl3_yangian_r_matrix_engine import (
    # Constants
    H_VEE, DIM_SL3, FUND_DIM, ADJ_DIM, RANK,
    # Kappa
    kappa_sl3,
    # Representations
    fund_rep_matrices, adjoint_rep_matrices, verify_adjoint_rep_bracket,
    # Killing form
    fund_killing_form_matrix, fund_inverse_killing_form, fund_dual_basis_matrices,
    killing_form_matrix_from_rep,
    # Casimir
    casimir_tensor_fund, casimir_tensor_adj,
    casimir_scalar_fund, casimir_scalar_adj,
    permutation_matrix, verify_casimir_identity_fund,
    adjoint_casimir_eigenvalues,
    # r-matrix
    r_matrix_fund, r_matrix_adj,
    # R-matrix
    R_matrix_yang_fund,
    # YBE / CYBE
    verify_ybe_fund, verify_cybe, verify_casimir_identity,
    # KZ / IBR
    kz_hamiltonian, verify_kz_commutativity,
    # Verlinde
    sl3_integrable_weights, sl3_dim_irrep, sl3_casimir_eigenvalue,
    sl3_tensor_product, verlinde_fusion,
    # DNP
    dnp_r_matrix_genus0, dnp_comparison_report,
    # sl_2
    sl2_yang_r_matrix, sl2_casimir_fund, verify_sl2_casimir_identity, verify_sl2_ybe,
    # Spectral
    spectral_decomposition_fund,
    # Report
    full_report,
)

from compute.lib.sl3_bar import (
    DIM_G, GEN_NAMES,
    H1, H2, E1, E2, E3, F1, F2, F3,
    sl3_structure_constants, sl3_killing_form,
)


# ============================================================
# 1. Fundamental representation consistency
# ============================================================

class TestFundamentalRep:
    """Verify the fundamental representation of sl_3."""

    def test_dimension(self):
        mats = fund_rep_matrices()
        assert len(mats) == 8
        for M in mats:
            assert M.shape == (3, 3)

    def test_tracelessness(self):
        mats = fund_rep_matrices()
        for a in range(DIM_SL3):
            assert abs(np.trace(mats[a])) < 1e-14

    def test_E3_is_bracket(self):
        mats = fund_rep_matrices()
        comm = mats[E1] @ mats[E2] - mats[E2] @ mats[E1]
        assert np.allclose(comm, mats[E3], atol=1e-14)

    def test_F3_is_bracket(self):
        mats = fund_rep_matrices()
        comm = mats[F2] @ mats[F1] - mats[F1] @ mats[F2]
        assert np.allclose(comm, mats[F3], atol=1e-14)

    def test_cartan_eigenvalues(self):
        mats = fund_rep_matrices()
        assert np.allclose(np.diag(mats[H1].real), [1, -1, 0], atol=1e-14)
        assert np.allclose(np.diag(mats[H2].real), [0, 1, -1], atol=1e-14)

    def test_killing_form_symmetric(self):
        G = fund_killing_form_matrix()
        assert np.allclose(G, G.T, atol=1e-14)

    def test_killing_form_nondegenerate(self):
        G = fund_killing_form_matrix()
        assert abs(np.linalg.det(G)) > 1e-6

    def test_killing_form_cartan_block(self):
        """Cartan block = Cartan matrix [[2,-1],[-1,2]]."""
        G = fund_killing_form_matrix()
        assert abs(G[H1, H1] - 2.0) < 1e-12
        assert abs(G[H1, H2] - (-1.0)) < 1e-12
        assert abs(G[H2, H2] - 2.0) < 1e-12

    def test_killing_form_ef_pairing(self):
        """(E_i, F_i) = 1 for each root pair."""
        G = fund_killing_form_matrix()
        assert abs(G[E1, F1] - 1.0) < 1e-12
        assert abs(G[E2, F2] - 1.0) < 1e-12
        assert abs(G[E3, F3] - 1.0) < 1e-12

    def test_dual_basis_pairing(self):
        """tr(T^a T_b) = delta^a_b."""
        mats = fund_rep_matrices()
        dual = fund_dual_basis_matrices()
        for a in range(DIM_SL3):
            for b in range(DIM_SL3):
                pairing = np.trace(mats[a] @ dual[b]).real
                expected = 1.0 if a == b else 0.0
                assert abs(pairing - expected) < 1e-10


# ============================================================
# 2. Adjoint representation consistency
# ============================================================

class TestAdjointRep:
    """Verify the adjoint representation of sl_3."""

    def test_dimension(self):
        mats = adjoint_rep_matrices()
        assert len(mats) == 8
        for M in mats:
            assert M.shape == (8, 8)

    def test_bracket_consistency(self):
        """[ad(T^a), ad(T^b)] = f^{ab}_c ad(T^c) (Jacobi identity)."""
        assert verify_adjoint_rep_bracket()

    def test_adjoint_trace_ratio(self):
        """tr_adj = 2 h^vee * tr_fund = 6 * tr_fund for sl_3."""
        G_fund = fund_killing_form_matrix()
        G_adj = killing_form_matrix_from_rep(adjoint_rep_matrices())
        # Every nonzero entry should have ratio 6
        for a in range(DIM_SL3):
            for b in range(DIM_SL3):
                if abs(G_fund[a, b]) > 0.01:
                    ratio = G_adj[a, b] / G_fund[a, b]
                    assert abs(ratio - 6.0) < 1e-10

    def test_casimir_scalar_adj(self):
        """C_2(adj) = 2N = 6 for sl_3 (fund-trace normalization)."""
        assert abs(casimir_scalar_adj() - 6.0) < 1e-10


# ============================================================
# 3. Casimir tensor — fundamental
# ============================================================

class TestCasimirFund:
    """Quadratic Casimir tensor in the fundamental."""

    def test_omega_eq_p_minus_i_over_3(self):
        """Omega = P - I/3 on C^3 otimes C^3."""
        assert verify_casimir_identity_fund()

    def test_casimir_scalar_fund(self):
        """C_2(fund) = (N^2-1)/N = 8/3 for sl_3."""
        assert abs(casimir_scalar_fund() - 8.0 / 3.0) < 1e-12

    def test_casimir_scalar_matrix(self):
        """C_2 on V is proportional to I_3."""
        mats = fund_rep_matrices()
        dual = fund_dual_basis_matrices()
        C2 = sum(mats[a] @ dual[a] for a in range(DIM_SL3))
        assert np.allclose(C2, (8.0 / 3.0) * np.eye(3), atol=1e-10)

    def test_permutation_squared(self):
        """P^2 = I on C^3 otimes C^3."""
        P = permutation_matrix(FUND_DIM)
        assert np.allclose(P @ P, np.eye(9), atol=1e-14)

    def test_permutation_eigenvalues(self):
        """P has eigenvalues +1 (mult 6) and -1 (mult 3)."""
        P = permutation_matrix(FUND_DIM)
        evals = sorted(np.linalg.eigvalsh(P))
        assert np.allclose(evals[:3], [-1, -1, -1], atol=1e-10)
        assert np.allclose(evals[3:], [1] * 6, atol=1e-10)

    def test_omega_symmetric_under_swap(self):
        """Omega_{21} = P Omega P = Omega (symmetric Casimir)."""
        Omega = casimir_tensor_fund()
        P = permutation_matrix(FUND_DIM)
        Omega_21 = P @ Omega @ P
        assert np.allclose(Omega, Omega_21, atol=1e-10)

    def test_casimir_identity_commutator(self):
        """[Omega_12, Omega_13 + Omega_23] = 0 in the fundamental."""
        Omega = casimir_tensor_fund()
        assert verify_casimir_identity(Omega, FUND_DIM) < 1e-10


# ============================================================
# 4. Casimir tensor — adjoint
# ============================================================

class TestCasimirAdj:
    """Quadratic Casimir tensor in the adjoint."""

    def test_casimir_identity_adj(self):
        """[Omega_12, Omega_13 + Omega_23] = 0 in the adjoint."""
        Omega = casimir_tensor_adj()
        assert verify_casimir_identity(Omega, ADJ_DIM) < 1e-10

    def test_omega_commutes_with_sl3_action(self):
        """Omega^adj commutes with the diagonal sl_3 action (Schur)."""
        Omega = casimir_tensor_adj()
        adj_mats = adjoint_rep_matrices()
        dim = ADJ_DIM
        for c in range(DIM_SL3):
            Delta_c = np.kron(adj_mats[c], np.eye(dim)) + np.kron(np.eye(dim), adj_mats[c])
            comm = Omega @ Delta_c - Delta_c @ Omega
            assert np.linalg.norm(comm) < 1e-8, f"[Omega, Delta({GEN_NAMES[c]})] != 0"

    def test_eigenvalue_singlet(self):
        """Omega^adj eigenvalue on the singlet V_{(0,0)}: -6."""
        Omega = casimir_tensor_adj()
        # Singlet = Killing form vector
        G = fund_killing_form_matrix()
        v = np.zeros(64, dtype=complex)
        for a in range(8):
            for b in range(8):
                v[a * 8 + b] = G[a, b]
        v /= np.linalg.norm(v)
        result = Omega @ v
        eigenvalue = np.dot(v.conj(), result).real
        assert abs(eigenvalue - (-6.0)) < 1e-8

    def test_eigenvalue_decomposition(self):
        """adj x adj = 27 + 10 + 10* + 8 + 8 + 1 with eigenvalues {2,0,-3,-6}."""
        ev = adjoint_casimir_eigenvalues()
        expected_evals = [-6.0, -3.0, 0.0, 2.0]
        expected_mults = [1, 16, 20, 27]
        assert len(ev["eigenvalues"]) == 4
        for e_exp, m_exp, e_got, m_got in zip(
                expected_evals, expected_mults,
                ev["eigenvalues"], ev["multiplicities"]):
            assert abs(e_got - e_exp) < 0.5, f"Expected eigenvalue {e_exp}, got {e_got}"
            assert m_got == m_exp, f"Expected mult {m_exp}, got {m_got}"
        assert ev["total_dim"] == 64


# ============================================================
# 5. r-matrix pole structure (AP19)
# ============================================================

class TestRMatrixPoleStructure:
    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""

    def test_single_pole_fund(self):
        """r(z) = Omega/z has a single pole (AP19)."""
        r = r_matrix_fund(1.0)
        Omega = casimir_tensor_fund()
        assert np.allclose(r, Omega, atol=1e-14)

    def test_r_matrix_at_large_z(self):
        """r(z) -> 0 as z -> infinity."""
        r = r_matrix_fund(100.0)
        assert np.max(np.abs(r)) < 0.1

    def test_residue_is_omega(self):
        """Res_{z=0} r(z) = Omega."""
        Omega = casimir_tensor_fund()
        P = permutation_matrix(FUND_DIM)
        assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)

    def test_adj_r_matrix_structure(self):
        """r^{adj}(z) = Omega^{adj}/z has single pole."""
        r1 = r_matrix_adj(1.0)
        r2 = r_matrix_adj(2.0)
        assert np.allclose(r1, 2.0 * r2, atol=1e-10)


# ============================================================
# 6. Yang--Baxter equation (fundamental)
# ============================================================

class TestYangBaxter:
    """Yang R-matrix R(u) = uI + P satisfies YBE in the fundamental."""

    def test_ybe_real_params(self):
        assert verify_ybe_fund(1.0, 2.0, 3.0) < 1e-10

    def test_ybe_real_params_2(self):
        assert verify_ybe_fund(0.5, 1.7, 3.2) < 1e-10

    def test_ybe_complex_params(self):
        assert verify_ybe_fund(1.0 + 0.5j, 2.0 - 0.3j, 3.0 + 0.1j) < 1e-10

    def test_ybe_close_params(self):
        assert verify_ybe_fund(0.1, 0.2, 0.3) < 1e-10

    def test_R_at_zero_is_P(self):
        """R(0) = P (permutation)."""
        R0 = R_matrix_yang_fund(0.0)
        P = permutation_matrix(FUND_DIM)
        assert np.allclose(R0, P, atol=1e-14)

    def test_R_eigenvalues_at_z1(self):
        """R(1) has eigenvalues 2 (x6) and 0 (x3)."""
        R1 = R_matrix_yang_fund(1.0)
        evals = np.sort(np.abs(np.linalg.eigvals(R1)))
        assert np.sum(np.abs(evals) < 1e-10) == 3
        assert np.sum(np.abs(evals - 2.0) < 1e-10) == 6

    def test_unitarity(self):
        """R(z)R(-z) = (1 - z^2) I."""
        z = 1.5
        R_plus = R_matrix_yang_fund(z)
        R_minus = R_matrix_yang_fund(-z)
        product = R_plus @ R_minus
        expected = (1 - z ** 2) * np.eye(9, dtype=complex)
        assert np.allclose(product, expected, atol=1e-10)


# ============================================================
# 7. Classical Yang--Baxter equation (CYBE)
# ============================================================

class TestCYBE:
    """CYBE for the Casimir r-matrix in fundamental and adjoint."""

    def test_cybe_fund(self):
        Omega = casimir_tensor_fund()
        assert verify_cybe(Omega, FUND_DIM, 1.5, 2.7) < 1e-10

    def test_cybe_fund_complex(self):
        Omega = casimir_tensor_fund()
        assert verify_cybe(Omega, FUND_DIM, 1.0 + 0.5j, 2.0 - 0.3j) < 1e-10

    def test_cybe_adj(self):
        """CYBE in the adjoint representation (64x64 Casimir)."""
        Omega = casimir_tensor_adj()
        assert verify_cybe(Omega, ADJ_DIM, 1.5, 2.7) < 1e-10

    def test_cybe_adj_complex(self):
        Omega = casimir_tensor_adj()
        assert verify_cybe(Omega, ADJ_DIM, 1.0 + 0.5j, 2.0 - 0.3j) < 1e-10


# ============================================================
# 8. KZ commutativity / IBR
# ============================================================

class TestKZCommutativity:
    """Infinitesimal braid relations: [H_i, H_j] = 0."""

    def test_kz_n3_fund(self):
        """KZ commutativity at 3 points, fundamental rep."""
        Omega = casimir_tensor_fund()
        kv = float(kappa_sl3(1))
        norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
        assert norm < 1e-10

    def test_kz_n3_fund_different_z(self):
        """KZ commutativity at 3 points with different spectral params."""
        Omega = casimir_tensor_fund()
        kv = float(kappa_sl3(2))
        norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
        assert norm < 1e-10

    def test_kz_n4_fund(self):
        """KZ commutativity at 4 points, fundamental rep (81-dimensional).

        This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
        Omega = casimir_tensor_fund()
        kv = float(kappa_sl3(1))
        norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
        assert norm < 1e-10

    def test_kz_kappa_independence(self):
        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
        Omega = casimir_tensor_fund()
        for k in [1, 2, 5, 10]:
            kv = float(kappa_sl3(k))
            norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
            assert norm < 1e-10, f"IBR fails at k={k}"


# ============================================================
# 9. Verlinde fusion rules
# ============================================================

class TestVerlindeRules:
    """Verlinde fusion for sl_3 at levels 1, 2, 3."""

    def test_integrable_count_k1(self):
        """Level 1: 3 integrable weights."""
        assert len(sl3_integrable_weights(1)) == 3

    def test_integrable_count_k2(self):
        """Level 2: 6 integrable weights."""
        assert len(sl3_integrable_weights(2)) == 6

    def test_integrable_count_k3(self):
        """Level 3: 10 integrable weights."""
        assert len(sl3_integrable_weights(3)) == 10

    def test_integrable_formula(self):
        """Count = (k+1)(k+2)/2."""
        for k in range(1, 8):
            assert len(sl3_integrable_weights(k)) == (k + 1) * (k + 2) // 2

    def test_dim_fund(self):
        assert sl3_dim_irrep(1, 0) == 3

    def test_dim_antifund(self):
        assert sl3_dim_irrep(0, 1) == 3

    def test_dim_adj(self):
        assert sl3_dim_irrep(1, 1) == 8

    def test_dim_sym2(self):
        assert sl3_dim_irrep(2, 0) == 6

    def test_c2_fund(self):
        assert sl3_casimir_eigenvalue(1, 0) == Rational(8, 3)

    def test_c2_adj(self):
        assert sl3_casimir_eigenvalue(1, 1) == Rational(6)

    def test_c2_trivial(self):
        assert sl3_casimir_eigenvalue(0, 0) == 0

    def test_tensor_product_fund_x_fund(self):
        """3 x 3 = 6 + 3*."""
        decomp = sl3_tensor_product(1, 0, 1, 0)
        assert decomp == {(2, 0): 1, (0, 1): 1}

    def test_tensor_product_fund_x_antifund(self):
        """3 x 3* = 8 + 1."""
        decomp = sl3_tensor_product(1, 0, 0, 1)
        assert decomp == {(1, 1): 1, (0, 0): 1}

    def test_verlinde_k1_fund_x_fund(self):
        """At k=1: 3 x 3 = 3* only (6 is not integrable)."""
        fus = verlinde_fusion(1, (1, 0), (1, 0))
        assert fus == {(0, 1): 1}

    def test_verlinde_k1_fund_x_antifund(self):
        """At k=1: 3 x 3* = 1 only (8 is not integrable)."""
        fus = verlinde_fusion(1, (1, 0), (0, 1))
        assert fus == {(0, 0): 1}

    def test_verlinde_k2_fund_x_fund(self):
        """At k=2: 3 x 3 = 6 + 3* (both integrable)."""
        fus = verlinde_fusion(2, (1, 0), (1, 0))
        assert fus == {(2, 0): 1, (0, 1): 1}

    def test_verlinde_k3_fund_x_fund(self):
        """At k=3: same as k=2 (no new reps appear in 3 x 3)."""
        fus = verlinde_fusion(3, (1, 0), (1, 0))
        assert fus == {(2, 0): 1, (0, 1): 1}

    def test_verlinde_k1_associativity(self):
        """At k=1 with 3 reps {0, 3, 3*}: fusion ring is Z_3."""
        # 3 x 3 = 3*, 3 x 3* = 0, 3* x 3* = 3
        fus_33 = verlinde_fusion(1, (1, 0), (1, 0))
        fus_33s = verlinde_fusion(1, (1, 0), (0, 1))
        fus_3s3s = verlinde_fusion(1, (0, 1), (0, 1))
        assert fus_33 == {(0, 1): 1}     # 3 x 3 = 3*
        assert fus_33s == {(0, 0): 1}    # 3 x 3* = 1
        assert fus_3s3s == {(1, 0): 1}   # 3* x 3* = 3


# ============================================================
# 10. DNP comparison
# ============================================================

class TestDNPComparison:
    """Compare with the Dimofte-Niu-Py dg-shifted Yangian."""

    def test_genus0_agreement(self):
        """r^{MK}(z) = r^{DNP}(z) = Omega/z at genus 0."""
        r_mk = r_matrix_fund(1.5)
        r_dnp = dnp_r_matrix_genus0(1.5)
        assert np.allclose(r_mk, r_dnp, atol=1e-14)

    def test_dnp_report_agreement(self):
        report = dnp_comparison_report(1.5)
        assert report["genus_0_agreement"]

    def test_dnp_cybe_satisfied(self):
        report = dnp_comparison_report(1.5)
        assert report["CYBE_satisfied"]

    def test_dnp_ainfty_trivial_for_km(self):
        """For KM algebras, higher A_infty operations vanish (strict)."""
        report = dnp_comparison_report(1.5)
        assert report["ainfty_ybe_reduces_to_cybe"]


# ============================================================
# 11. sl_2 cross-check
# ============================================================

class TestSl2CrossCheck:
    """sl_2 rank-1 reduction as consistency check."""

    def test_sl2_casimir_identity(self):
        """Omega^{sl_2} = P - I/2 on C^2 x C^2."""
        assert verify_sl2_casimir_identity()

    def test_sl2_ybe(self):
        """YBE for sl_2 Yang R-matrix R(u) = uI + P in C^2."""
        assert verify_sl2_ybe(1.0, 2.0, 3.0) < 1e-10

    def test_sl2_ybe_complex(self):
        assert verify_sl2_ybe(1.0 + 0.5j, 2.0 - 0.3j, 3.0 + 0.1j) < 1e-10

    def test_sl2_unitarity(self):
        """R(z)R(-z) = (1-z^2)I for sl_2."""
        z = 2.0
        R_plus = sl2_yang_r_matrix(z)
        R_minus = sl2_yang_r_matrix(-z)
        product = R_plus @ R_minus
        expected = (1 - z ** 2) * np.eye(4, dtype=complex)
        assert np.allclose(product, expected, atol=1e-10)

    def test_sl2_spectral_decomposition(self):
        """For sl_2: C^2 x C^2 = Sym^2 (dim 3) + Lambda^2 (dim 1)."""
        P = permutation_matrix(2)
        I4 = np.eye(4)
        P_sym = (I4 + P) / 2
        P_asym = (I4 - P) / 2
        assert abs(np.trace(P_sym).real - 3.0) < 1e-10
        assert abs(np.trace(P_asym).real - 1.0) < 1e-10


# ============================================================
# 12. Spectral decomposition (fundamental)
# ============================================================

class TestSpectralDecomposition:
    """Spectral decomposition of R on C^3 x C^3."""

    def test_sym_dim(self):
        sd = spectral_decomposition_fund()
        assert sd["sym_dim"] == 6

    def test_asym_dim(self):
        sd = spectral_decomposition_fund()
        assert sd["asym_dim"] == 3

    def test_omega_on_sym(self):
        """Omega eigenvalue on Sym^2: 2/3."""
        sd = spectral_decomposition_fund()
        assert abs(sd["Omega_eigenvalue_sym"] - 2.0 / 3.0) < 1e-10

    def test_omega_on_asym(self):
        """Omega eigenvalue on Lambda^2: -4/3."""
        sd = spectral_decomposition_fund()
        assert abs(sd["Omega_eigenvalue_asym"] - (-4.0 / 3.0)) < 1e-10

    def test_R_on_sym(self):
        """R(z)|_{Sym^2} = (z+1) I_{Sym^2}."""
        P = permutation_matrix(FUND_DIM)
        P_sym = (np.eye(9) + P) / 2
        z = 3.7
        R = R_matrix_yang_fund(z)
        assert np.allclose(R @ P_sym, (z + 1) * P_sym, atol=1e-10)

    def test_R_on_asym(self):
        """R(z)|_{Lambda^2} = (z-1) I_{Lambda^2}."""
        P = permutation_matrix(FUND_DIM)
        P_asym = (np.eye(9) - P) / 2
        z = 3.7
        R = R_matrix_yang_fund(z)
        assert np.allclose(R @ P_asym, (z - 1) * P_asym, atol=1e-10)


# ============================================================
# 13. Kappa formula and modular characteristic
# ============================================================

class TestKappa:
    """Kappa formula kappa(sl_3_k) = 4(k+3)/3."""

    def test_kappa_k1(self):
        assert kappa_sl3(1) == Rational(16, 3)

    def test_kappa_k0(self):
        assert kappa_sl3(0) == Rational(4)

    def test_kappa_critical(self):
        """At critical level k = -h^vee = -3: kappa = 0."""
        assert kappa_sl3(-3) == 0

    def test_kappa_ff_duality(self):
        """Feigin-Frenkel: kappa(k) + kappa(-k - 2h^vee) = 0."""
        k = Symbol('k')
        k_dual = -k - 2 * H_VEE
        assert kappa_sl3(k) + kappa_sl3(k_dual) == 0

    def test_constants(self):
        assert H_VEE == 3
        assert DIM_SL3 == 8
        assert FUND_DIM == 3
        assert ADJ_DIM == 8
        assert RANK == 2


# ============================================================
# 14. Cross-checks with yangian_rmatrix_sl3.py
# ============================================================

class TestCrossCheck:
    """Cross-check with the existing yangian_rmatrix_sl3.py module."""

    def test_casimir_matches(self):
        """Our Casimir matches yangian_rmatrix_sl3."""
        from compute.lib.yangian_rmatrix_sl3 import (
            casimir_tensor_fund as ctf_old,
        )
        Omega_us = casimir_tensor_fund()
        Omega_them = ctf_old()
        assert np.allclose(Omega_us, Omega_them, atol=1e-14)

    def test_permutation_matches(self):
        """Our permutation matrix matches."""
        from compute.lib.yangian_rmatrix_sl3 import (
            permutation_matrix_3,
        )
        P_us = permutation_matrix(3)
        P_them = permutation_matrix_3()
        assert np.allclose(P_us, P_them, atol=1e-14)

    def test_kappa_matches(self):
        """Our kappa formula matches."""
        from compute.lib.yangian_rmatrix_sl3 import kappa_sl3 as kappa_old
        for k in range(10):
            assert kappa_sl3(k) == kappa_old(k)

    def test_yang_r_matrix_matches(self):
        """Our Yang R-matrix matches at z = 2.5."""
        from compute.lib.yangian_rmatrix_sl3 import (
            R_matrix_fund_exact_yang,
        )
        z = 2.5
        R_us = R_matrix_yang_fund(z)
        R_them = R_matrix_fund_exact_yang(z)
        assert np.allclose(R_us, R_them, atol=1e-12)

    def test_yang_r_matches_residue_extraction(self):
        """Our Yang R-matrix matches yangian_residue_extraction at N=3."""
        from compute.lib.yangian_residue_extraction import yang_r_matrix_slN
        z = 2.5
        R_us = R_matrix_yang_fund(z)
        R_them = yang_r_matrix_slN(z, 3)
        assert np.allclose(R_us, R_them, atol=1e-12)

    def test_full_report_consistent(self):
        """Full report has expected structure and values."""
        rpt = full_report(k=1)
        assert rpt["h_vee"] == 3
        assert rpt["dim_g"] == 8
        assert rpt["rank"] == 2
        assert rpt["kappa"] == Rational(16, 3)
        assert abs(rpt["C2_fund"] - 8.0 / 3.0) < 1e-10
        assert abs(rpt["C2_adj"] - 6.0) < 1e-10
        assert rpt["YBE_fund_norm"] < 1e-10
        assert rpt["CYBE_fund_norm"] < 1e-10
        assert rpt["CYBE_adj_norm"] < 1e-10
        assert rpt["KZ_commutativity_n3"] < 1e-10
        assert rpt["DNP_genus0_agreement"]
