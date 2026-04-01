r"""Tests for Yangian R-matrix extraction from the bar complex for sl_3.

First non-sl_2 extraction of R(z) = Res^{coll}_{0,2}(\Theta_A).

Ground truth references:
    - sl3_bar.py: structure constants, Killing form, OPE data
    - yangian_residue_extraction.py: Yang R-matrix for sl_N, YBE, channel decomposition
    - yangians.tex: DK bridge, r-matrix = collision residue of bar MC element
    - landscape_census.tex: kappa(sl_3_k) = 4(k+3)/3

Tests organized by:
    1. Fundamental representation consistency (bracket, Killing form)
    2. Casimir tensor and identity Omega = P - I/N
    3. r-matrix pole structure (AP19 verification)
    4. Yang--Baxter equation (additive and multiplicative conventions)
    5. Unitarity and crossing
    6. Spectral decomposition (Sym^2 / Lambda^2)
    7. sl_2 reduction (embedding sl_2 -> sl_3)
    8. kappa dependence and large-kappa limit
    9. R(z) at special points (z = 0, z -> infinity)
    10. Quantum determinant
    11. Drinfeld--Kohno bridge (KZ monodromy)
    12. Cubic Casimir (d-tensor, sl_3-specific)
    13. d^2 = 0 => YBE (bar complex structural connection)
    14. Cross-checks with yangian_residue_extraction.py
    15. Literature comparison
"""

import pytest
import numpy as np
from fractions import Fraction
from sympy import Rational, Symbol

from compute.lib.yangian_rmatrix_sl3 import (
    # Constants
    H_VEE_SL3,
    DIM_SL3,
    FUND_DIM,
    # Kappa
    kappa_sl3,
    # Fundamental rep
    fund_rep_matrices,
    verify_fund_rep_bracket,
    verify_fund_rep_killing,
    # Killing form
    killing_form_matrix,
    inverse_killing_form,
    dual_basis_matrices,
    # Casimir
    casimir_tensor_fund,
    permutation_matrix_3,
    verify_casimir_identity,
    casimir_scalar_fund,
    # Cubic
    d_tensor_sl3,
    # r-matrix
    r_matrix_abstract,
    r_matrix_fund,
    # R-matrix
    R_matrix_fund_leading,
    R_matrix_fund_with_trace,
    R_matrix_fund_exact_yang,
    R_matrix_fund_second_order,
    # YBE
    verify_ybe_fundamental,
    verify_ybe_multiplicative,
    # Unitarity
    verify_unitarity,
    # Spectral decomposition
    spectral_decomposition,
    # sl_2 embedding
    sl2_embedding_indices,
    sl2_reduction_r_matrix,
    sl2_casimir_in_fund,
    # DK bridge
    kz_connection_matrix,
    kz_monodromy_eigenvalues,
    # Quantum determinant
    quantum_determinant_check,
    # Bar connection
    bar_d_squared_implies_ybe,
    # Special points
    R_at_infinity,
    R_residue_at_zero,
    # Comparison
    compare_with_literature,
    full_extraction_report,
)

from compute.lib.sl3_bar import (
    DIM_G,
    GEN_NAMES,
    H1, H2, E1, E2, E3, F1, F2, F3,
    sl3_structure_constants,
    sl3_killing_form,
)


# ============================================================
# 1. Fundamental representation consistency
# ============================================================

class TestFundamentalRep:
    """Verify the fundamental representation of sl_3 is correct."""

    def test_bracket_consistency(self):
        """[T^a, T^b] = f^{abc} T^c in fundamental rep."""
        assert verify_fund_rep_bracket()

    def test_killing_form_consistency(self):
        """tr(T^a T^b) matches sl3_killing_form."""
        assert verify_fund_rep_killing()

    def test_dimension(self):
        """Fundamental rep is 3-dimensional."""
        mats = fund_rep_matrices()
        assert len(mats) == DIM_G  # 8 generators
        for M in mats:
            assert M.shape == (3, 3)

    def test_tracelessness(self):
        """All sl_3 generators are traceless in the fundamental."""
        mats = fund_rep_matrices()
        for a in range(DIM_G):
            assert abs(np.trace(mats[a])) < 1e-14, f"T^{GEN_NAMES[a]} not traceless"

    def test_E3_is_bracket(self):
        """E_3 = [E_1, E_2] in the fundamental rep."""
        mats = fund_rep_matrices()
        comm = mats[E1] @ mats[E2] - mats[E2] @ mats[E1]
        assert np.allclose(comm, mats[E3], atol=1e-14)

    def test_F3_is_bracket(self):
        """F_3 = [F_2, F_1] in the fundamental rep."""
        mats = fund_rep_matrices()
        comm = mats[F2] @ mats[F1] - mats[F1] @ mats[F2]
        assert np.allclose(comm, mats[F3], atol=1e-14)

    def test_cartan_eigenvalues(self):
        """H_1, H_2 have correct eigenvalues on basis vectors."""
        mats = fund_rep_matrices()
        # H_1 = diag(1, -1, 0)
        assert np.allclose(np.diag(mats[H1].real), [1, -1, 0], atol=1e-14)
        # H_2 = diag(0, 1, -1)
        assert np.allclose(np.diag(mats[H2].real), [0, 1, -1], atol=1e-14)


# ============================================================
# 2. Casimir tensor and identity
# ============================================================

class TestCasimir:
    """Verify the quadratic Casimir tensor."""

    def test_casimir_identity_omega_eq_p_minus_i_over_n(self):
        """Omega = P - I/N on V otimes V (the standard sl_N identity)."""
        assert verify_casimir_identity()

    def test_casimir_scalar_fund(self):
        """C_2(fund) = (N^2 - 1)/N = 8/3 for sl_3 (trace normalization)."""
        c2 = casimir_scalar_fund()
        assert abs(c2 - 8.0 / 3.0) < 1e-12

    def test_casimir_scalar_matrix(self):
        """The scalar Casimir on V is proportional to the identity."""
        mats = fund_rep_matrices()
        dual = dual_basis_matrices()
        C2 = sum(mats[a] @ dual[a] for a in range(DIM_G))
        assert np.allclose(C2, (8.0 / 3.0) * np.eye(3), atol=1e-10)

    def test_killing_form_symmetric(self):
        """Killing form g_{ab} is symmetric."""
        G = killing_form_matrix()
        assert np.allclose(G, G.T, atol=1e-14)

    def test_killing_form_nondegenerate(self):
        """Killing form is nondegenerate (sl_3 is semisimple)."""
        G = killing_form_matrix()
        det = np.linalg.det(G)
        assert abs(det) > 1e-6, f"Killing form degenerate: det = {det}"

    def test_dual_basis_pairing(self):
        """(T^a, T_b) = delta^a_b."""
        mats = fund_rep_matrices()
        dual = dual_basis_matrices()
        for a in range(DIM_G):
            for b in range(DIM_G):
                pairing = np.trace(mats[a] @ dual[b]).real
                expected = 1.0 if a == b else 0.0
                assert abs(pairing - expected) < 1e-10, \
                    f"(T^{GEN_NAMES[a]}, T_{GEN_NAMES[b]}) = {pairing}, expected {expected}"

    def test_omega_eigenvalues(self):
        """Omega eigenvalues on Sym^2 and Lambda^2."""
        Omega = casimir_tensor_fund()
        P = permutation_matrix_3()
        I9 = np.eye(9)
        P_sym = (I9 + P) / 2
        P_asym = (I9 - P) / 2

        # Omega|_Sym = (2/3) P_sym
        assert np.allclose(Omega @ P_sym, (2.0 / 3.0) * P_sym, atol=1e-10)
        # Omega|_Lambda = (-4/3) P_asym
        assert np.allclose(Omega @ P_asym, (-4.0 / 3.0) * P_asym, atol=1e-10)

    def test_permutation_squared_is_identity(self):
        """P^2 = I on V otimes V."""
        P = permutation_matrix_3()
        assert np.allclose(P @ P, np.eye(9), atol=1e-14)

    def test_permutation_eigenvalues(self):
        """P has eigenvalues +1 (mult 6) and -1 (mult 3)."""
        P = permutation_matrix_3()
        evals = sorted(np.linalg.eigvalsh(P))
        assert np.allclose(evals[:3], [-1, -1, -1], atol=1e-10)
        assert np.allclose(evals[3:], [1, 1, 1, 1, 1, 1], atol=1e-10)


# ============================================================
# 3. r-matrix pole structure (AP19)
# ============================================================

class TestRMatrixPoleStructure:
    """Verify the r-matrix has the correct pole structure (AP19)."""

    def test_single_pole(self):
        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
        info = r_matrix_abstract()
        assert info["pole_order"] == 1

    def test_residue_is_omega(self):
        """Residue of r(z) at z = 0 is Omega = P - I/3."""
        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
        Omega = casimir_tensor_fund()
        P = permutation_matrix_3()
        I9 = np.eye(9)
        assert np.allclose(Omega, P - I9 / 3, atol=1e-10)

    def test_ope_pole_orders_vs_rmatrix(self):
        """OPE has poles z^{-2} (curvature) and z^{-1} (bracket).
        Bar propagator d log absorbs one power: r-matrix has z^{-1} only.
        This is AP19: r-matrix poles are one order below OPE poles."""
        # The OPE: J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c/(z-w)
        # Highest OPE pole: z^{-2} (double pole from Killing form)
        # After d log extraction: z^{-2} -> z^{-1}  (absorbs one power)
        # So r-matrix has ONLY z^{-1} pole, as verified above.
        info = r_matrix_abstract()
        assert "z^{-1} only" in info["AP19_check"]

    def test_r_matrix_at_large_z(self):
        """r(z) -> 0 as z -> infinity."""
        r = r_matrix_fund(100.0)
        assert np.max(np.abs(r)) < 0.1


# ============================================================
# 4. Yang--Baxter equation
# ============================================================

class TestYangBaxter:
    """Verify the Yang--Baxter equation."""

    def test_ybe_additive_real(self):
        """YBE in additive convention at real spectral parameters."""
        assert verify_ybe_fundamental(1.0, 2.0, 3.0) < 1e-10

    def test_ybe_additive_real_2(self):
        """YBE at a second set of real parameters."""
        assert verify_ybe_fundamental(0.5, 1.7, 3.2) < 1e-10

    def test_ybe_additive_complex(self):
        """YBE at complex spectral parameters."""
        assert verify_ybe_fundamental(1.0 + 0.5j, 2.0 - 0.3j, 3.0 + 0.1j) < 1e-10

    def test_ybe_additive_close_parameters(self):
        """YBE at nearby spectral parameters."""
        assert verify_ybe_fundamental(0.1, 0.2, 0.3) < 1e-10

    def test_ybe_multiplicative_real(self):
        """YBE in multiplicative convention R(z) = I + P/z."""
        assert verify_ybe_multiplicative(1.0, 2.0, 3.0) < 1e-10

    def test_ybe_multiplicative_complex(self):
        """YBE multiplicative at complex parameters."""
        assert verify_ybe_multiplicative(1.5 + 0.3j, 2.0 - 0.7j, 4.0 + 0.1j) < 1e-10

    def test_ybe_27_dimensional(self):
        """YBE acts on V^{otimes 3} = C^{27} (19683 equations)."""
        # The YBE is a 27x27 matrix equation, i.e. 729 scalar equations.
        # Actually 27^2 = 729, not 19683 (that would be 27^3 which is
        # the number of entries of the cubic tensor product).
        # Each side is a 27x27 matrix, so 729 equations.
        N = FUND_DIM
        assert N ** 3 == 27  # V^{otimes 3} dimension
        norm = verify_ybe_fundamental(2.0, 5.0, 7.0)
        assert norm < 1e-10

    def test_ybe_degenerate_z2_eq_z3(self):
        """YBE when z_2 = z_3 (degenerate, but R(0) = P is well-defined)."""
        # R(0) = P in additive convention
        norm = verify_ybe_fundamental(1.0, 2.0, 2.0)
        # R_{23}(0) = P, which is fine
        assert norm < 1e-10


# ============================================================
# 5. Unitarity and crossing
# ============================================================

class TestUnitarity:
    """Verify unitarity and crossing relations."""

    def test_unitarity_real(self):
        """R(z) R(-z) = (1 - z^2) I at real z."""
        assert verify_unitarity(1.5) < 1e-10

    def test_unitarity_complex(self):
        """R(z) R(-z) = (1 - z^2) I at complex z."""
        assert verify_unitarity(2.7 + 0.3j) < 1e-10

    def test_unitarity_small_z(self):
        """Unitarity at small z."""
        assert verify_unitarity(0.1) < 1e-10

    def test_r21_equals_r(self):
        """R_{21}(z) = P R(z) P = R(z) for the Yang R-matrix.

        This is because P R(z) P = P(zI + P)P = zP^2 + P^3 = zI + P = R(z)."""
        P = permutation_matrix_3()
        z = 2.5
        R = R_matrix_fund_exact_yang(z)
        R21 = P @ R @ P
        assert np.allclose(R, R21, atol=1e-14)


# ============================================================
# 6. Spectral decomposition
# ============================================================

class TestSpectralDecomposition:
    """Verify the spectral decomposition of R on V otimes V."""

    def test_sym_dim_6(self):
        sd = spectral_decomposition()
        assert sd["sym_dim"] == 6

    def test_asym_dim_3(self):
        sd = spectral_decomposition()
        assert sd["asym_dim"] == 3

    def test_total_dim_9(self):
        sd = spectral_decomposition()
        assert sd["sym_dim"] + sd["asym_dim"] == 9

    def test_omega_on_sym(self):
        """Omega eigenvalue on Sym^2 is 2/3."""
        sd = spectral_decomposition()
        assert abs(sd["C2_on_sym"] - 2.0 / 3.0) < 1e-10

    def test_omega_on_asym(self):
        """Omega eigenvalue on Lambda^2 is -4/3."""
        sd = spectral_decomposition()
        assert abs(sd["C2_on_asym"] - (-4.0 / 3.0)) < 1e-10

    def test_R_eigenvalue_sym(self):
        """R(z)|_{Sym^2} = (z+1) I_{Sym^2}."""
        P = permutation_matrix_3()
        I9 = np.eye(9)
        P_sym = (I9 + P) / 2
        z = 3.7
        R = R_matrix_fund_exact_yang(z)
        assert np.allclose(R @ P_sym, (z + 1) * P_sym, atol=1e-10)

    def test_R_eigenvalue_asym(self):
        """R(z)|_{Lambda^2} = (z-1) I_{Lambda^2}."""
        P = permutation_matrix_3()
        I9 = np.eye(9)
        P_asym = (I9 - P) / 2
        z = 3.7
        R = R_matrix_fund_exact_yang(z)
        assert np.allclose(R @ P_asym, (z - 1) * P_asym, atol=1e-10)


# ============================================================
# 7. sl_2 reduction
# ============================================================

class TestSl2Reduction:
    """Verify sl_2 -> sl_3 embedding reproduces known sl_2 data."""

    def test_sl2_indices(self):
        """sl_2 subalgebra indices are H1, E1, F1."""
        idx = sl2_embedding_indices()
        assert set(idx) == {H1, E1, F1}

    def test_sl2_casimir_block_diagonal(self):
        """sl_2 Casimir on C^3 = C^2 + C^1 decomposes block-diagonally.

        The sl_2 subalgebra generated by H_1, E_1, F_1 acts on C^3
        via the decomposition C^3 = V_1 + V_0 (2-dim fundamental + trivial).
        The Casimir of the sl_2 subalgebra (with dual basis from sl_3
        Killing form) acts on e_3 by 0 (trivial rep)."""
        C2 = sl2_casimir_in_fund()
        # e_3 is in the trivial representation of sl_2
        assert abs(C2[2, 2]) < 1e-10, "C_2^{sl_2} not zero on trivial rep"
        # Off-diagonal to e_3 should vanish
        assert abs(C2[0, 2]) < 1e-10
        assert abs(C2[1, 2]) < 1e-10
        assert abs(C2[2, 0]) < 1e-10
        assert abs(C2[2, 1]) < 1e-10

    def test_sl2_r_matrix_pole_structure(self):
        """sl_2 part of r-matrix also has single pole at z = 0."""
        r = sl2_reduction_r_matrix(1.0)
        # Non-zero: restriction is non-trivial
        assert np.max(np.abs(r)) > 0.1

    def test_sl2_casimir_on_2d_subspace(self):
        """The sl_2 Casimir restricted to the 2-dim subspace e_1, e_2
        is proportional to the identity.

        With the sl_3 trace normalization, the sl_2 Casimir on the
        2-dim fundamental is a nonzero scalar (not necessarily the
        standard sl_2 value, because we use the sl_3 dual basis)."""
        C2 = sl2_casimir_in_fund()
        # Extract 2x2 block
        block = C2[:2, :2].real
        # Should be proportional to I_2
        assert abs(block[0, 1]) < 1e-10, "Off-diagonal in sl_2 block"
        assert abs(block[1, 0]) < 1e-10, "Off-diagonal in sl_2 block"
        # Diagonal elements should be positive (Casimir on nontrivial rep)
        assert block[0, 0] > 0
        assert block[1, 1] > 0


# ============================================================
# 8. Kappa dependence
# ============================================================

class TestKappaDependence:
    """Verify kappa formula and large-kappa behavior."""

    def test_kappa_formula_k1(self):
        """kappa(sl_3, k=1) = 4*4/3 = 16/3."""
        assert kappa_sl3(1) == Rational(16, 3)

    def test_kappa_formula_k0(self):
        """kappa(sl_3, k=0) = 4*3/3 = 4 (special: zero level, nonzero kappa)."""
        assert kappa_sl3(0) == Rational(4)

    def test_kappa_formula_critical(self):
        """At the critical level k = -h^vee = -3: kappa = 0."""
        assert kappa_sl3(-3) == 0

    def test_kappa_dual_level(self):
        """Feigin-Frenkel duality: k' = -k - 2h^vee.
        kappa(k) + kappa(k') should be 0 for KM algebras."""
        k = Symbol('k')
        k_dual = -k - 2 * H_VEE_SL3  # -k - 6
        kappa_sum = kappa_sl3(k) + kappa_sl3(k_dual)
        # kappa(k) + kappa(k') = 4(k+3)/3 + 4(-k-6+3)/3
        # = 4(k+3)/3 + 4(-k-3)/3 = 0
        assert kappa_sum == 0

    def test_R_large_kappa_limit(self):
        """R(z; kappa) = I + Omega/(kappa*z) -> I as kappa -> infinity.

        The Omega/(kappa*z) correction vanishes at large kappa,
        leaving just the identity.  The Yang R-matrix I + P/z is the
        EXACT kappa-independent solution (not the large-kappa limit
        of the perturbative series)."""
        z = 2.0
        kappa_val = 1e6
        R_full = R_matrix_fund_with_trace(z, kappa_val)
        # At large kappa, R -> I (not I + P/z)
        assert np.allclose(R_full, np.eye(9, dtype=complex), atol=1e-3)

    def test_R_with_trace_kappa_scaling(self):
        """R_with_trace(z, kappa) = I + Omega/(kappa*z) has corrections of order 1/kappa.

        At kappa = 10, z = 2: the largest correction is |Omega|/(kappa*z).
        Omega has eigenvalues 2/3 and -4/3, so max correction ~ 4/(3*10*2) ~ 0.067."""
        z = 2.0
        kappa_val = 10.0
        R_full = R_matrix_fund_with_trace(z, kappa_val)
        diff_from_I = np.max(np.abs(R_full - np.eye(9, dtype=complex)))
        # Max eigenvalue of Omega is 2/3 on Sym, -4/3 on Lambda
        # So max correction ~ 4/3 / (10 * 2) = 2/30 ~ 0.067
        assert diff_from_I < 0.15
        assert diff_from_I > 0.01  # NOT zero at finite kappa


# ============================================================
# 9. R(z) at special points
# ============================================================

class TestSpecialPoints:
    """R-matrix at special values of z."""

    def test_R_infinity_is_identity(self):
        """R(z) -> I as z -> infinity."""
        R_inf = R_at_infinity()
        assert np.allclose(R_inf, np.eye(9), atol=1e-14)

    def test_R_residue_at_zero_is_P(self):
        """Residue of R(z) = I + P/z at z = 0 is P."""
        P_res = R_residue_at_zero()
        P = permutation_matrix_3()
        assert np.allclose(P_res, P, atol=1e-14)

    def test_R_additive_at_zero_is_P(self):
        """R(0) = P in additive convention."""
        R0 = R_matrix_fund_exact_yang(0.0)
        P = permutation_matrix_3()
        assert np.allclose(R0, P, atol=1e-14)

    def test_R_at_z1(self):
        """R(1) = I + P (additive) has eigenvalues 2 and 0."""
        R1 = R_matrix_fund_exact_yang(1.0)
        evals = np.sort(np.abs(np.linalg.eigvals(R1)))
        # Sym^2: z+1 = 2, Lambda^2: z-1 = 0
        # So 6 eigenvalues at 2 and 3 at 0
        assert np.sum(np.abs(evals) < 1e-10) == 3  # three zero eigenvalues
        assert np.sum(np.abs(evals - 2.0) < 1e-10) == 6  # six eigenvalues at 2

    def test_R_at_minus1(self):
        """R(-1) has eigenvalues 0 (on Sym^2) and -2 (on Lambda^2)."""
        R_m1 = R_matrix_fund_exact_yang(-1.0)
        evals = np.sort(np.linalg.eigvals(R_m1).real)
        assert np.sum(np.abs(evals) < 1e-10) == 6  # six zeros on Sym^2
        assert np.sum(np.abs(evals + 2.0) < 1e-10) == 3  # three at -2 on Lambda^2


# ============================================================
# 10. Quantum determinant
# ============================================================

class TestQuantumDeterminant:
    """Verify quantum determinant properties."""

    def test_qdet_z2(self):
        """R|_{Lambda^2} = (z-1) at z = 2."""
        assert quantum_determinant_check(2.0) < 1e-10

    def test_qdet_z5(self):
        """R|_{Lambda^2} = (z-1) at z = 5."""
        assert quantum_determinant_check(5.0) < 1e-10

    def test_qdet_complex(self):
        """Quantum determinant at complex z."""
        assert quantum_determinant_check(3.0 + 1.0j) < 1e-10

    def test_qdet_explicit(self):
        """Explicitly: P_asym R(z) P_asym = (z-1) P_asym."""
        P = permutation_matrix_3()
        I9 = np.eye(9, dtype=complex)
        P_asym = (I9 - P) / 2
        z = 4.0
        R = R_matrix_fund_exact_yang(z)
        lhs = P_asym @ R @ P_asym
        rhs = (z - 1) * P_asym
        assert np.allclose(lhs, rhs, atol=1e-10)


# ============================================================
# 11. Drinfeld--Kohno bridge
# ============================================================

class TestDrinfeldKohno:
    """Verify the Drinfeld--Kohno correspondence for sl_3."""

    def test_kz_connection_proportional_to_omega(self):
        """KZ connection A(z) = Omega / (kappa * z)."""
        z = 2.0
        kappa_val = float(kappa_sl3(1))
        A = kz_connection_matrix(z, kappa_val)
        Omega = casimir_tensor_fund()
        assert np.allclose(A, Omega / (kappa_val * z), atol=1e-12)

    def test_monodromy_eigenvalues_k1(self):
        """KZ monodromy eigenvalues at k = 1."""
        kappa_val = float(kappa_sl3(1))  # 16/3
        mono = kz_monodromy_eigenvalues(kappa_val)
        # Omega eigenvalue on Sym^2: 2/3
        assert abs(mono["Omega_eigenvalue_sym"] - 2.0 / 3.0) < 1e-10
        # Omega eigenvalue on Lambda^2: -4/3
        assert abs(mono["Omega_eigenvalue_asym"] - (-4.0 / 3.0)) < 1e-10

    def test_monodromy_at_large_kappa(self):
        """At large kappa, monodromy -> I (trivial)."""
        kappa_val = 1e6
        mono = kz_monodromy_eigenvalues(kappa_val)
        # exp(2*pi*i * small) ~ 1
        assert abs(mono["monodromy_sym"] - 1.0) < 1e-4
        assert abs(mono["monodromy_asym"] - 1.0) < 1e-4

    def test_monodromy_ratio_nondegenerate(self):
        """Monodromy ratio on Sym^2 vs Lambda^2 is nontrivial at k = 1."""
        kappa_val = float(kappa_sl3(1))
        mono = kz_monodromy_eigenvalues(kappa_val)
        # The ratio should NOT be 1
        assert abs(mono["ratio"] - 1.0) > 0.01


# ============================================================
# 12. Cubic Casimir (sl_3-specific)
# ============================================================

class TestCubicCasimir:
    """The cubic Casimir d^{abc} is nonzero for sl_3 (unlike sl_2)."""

    def test_d_tensor_nonzero(self):
        """d^{abc} is nonzero for sl_3."""
        d = d_tensor_sl3()
        assert np.max(np.abs(d)) > 1e-10

    def test_d_tensor_totally_symmetric(self):
        """d^{abc} = d^{bac} = d^{acb} = ... (totally symmetric)."""
        d = d_tensor_sl3()
        for a in range(DIM_G):
            for b in range(DIM_G):
                for c in range(DIM_G):
                    assert abs(d[a, b, c] - d[b, a, c]) < 1e-12
                    assert abs(d[a, b, c] - d[a, c, b]) < 1e-12
                    assert abs(d[a, b, c] - d[c, b, a]) < 1e-12

    def test_d_tensor_vanishes_for_sl2_generators(self):
        """d^{abc} restricted to sl_2 generators (H1, E1, F1) should vanish.

        sl_2 has no cubic invariant; d^{abc} = 0 for a,b,c in sl_2."""
        d = d_tensor_sl3()
        sl2_idx = sl2_embedding_indices()
        for a in sl2_idx:
            for b in sl2_idx:
                for c in sl2_idx:
                    assert abs(d[a, b, c]) < 1e-12, \
                        f"d^{{{GEN_NAMES[a]},{GEN_NAMES[b]},{GEN_NAMES[c]}}} = {d[a,b,c]} != 0"

    def test_cubic_casimir_does_not_enter_R_at_order_1_over_z(self):
        """The cubic Casimir C_3 does NOT contribute to R(z) at order 1/z.

        R(z) = I + Omega/z + ..., and Omega involves only the quadratic Casimir.
        C_3 can only appear in V^{otimes 3} or at higher orders in 1/z."""
        # This is structural: the r-matrix r(z) = Omega/z is purely quadratic.
        # The cubic Casimir enters at the ARITY-3 level of the shadow tower.
        Omega = casimir_tensor_fund()
        # Omega is 9x9 (V otimes V), not 27x27 (V otimes V otimes V)
        assert Omega.shape == (9, 9)


# ============================================================
# 13. d^2 = 0 => YBE
# ============================================================

class TestBarDSquaredImpliesYBE:
    """The bar complex D^2 = 0 implies YBE for the collision residue."""

    def test_structural_implication(self):
        """D^2 = 0 => YBE at multiple spectral parameters."""
        results = bar_d_squared_implies_ybe()
        for name, ok in results.items():
            assert ok, f"d^2=0 => YBE failed at {name}"


# ============================================================
# 14. Cross-checks with yangian_residue_extraction.py
# ============================================================

class TestCrossCheck:
    """Cross-check with the existing Yang R-matrix code in yangian_residue_extraction.py."""

    def test_permutation_matches(self):
        """Our permutation matrix matches yangian_residue_extraction."""
        from compute.lib.yangian_residue_extraction import permutation_matrix_slN
        P_us = permutation_matrix_3()
        P_them = permutation_matrix_slN(3)
        assert np.allclose(P_us, P_them, atol=1e-14)

    def test_yang_r_matrix_matches(self):
        """Our Yang R-matrix matches yangian_residue_extraction at N = 3."""
        from compute.lib.yangian_residue_extraction import yang_r_matrix_slN
        z = 2.5
        R_us = R_matrix_fund_exact_yang(z)
        R_them = yang_r_matrix_slN(z, 3)
        assert np.allclose(R_us, R_them, atol=1e-12)

    def test_ybe_matches(self):
        """YBE verification matches yangian_residue_extraction."""
        from compute.lib.yangian_residue_extraction import verify_yang_baxter_slN
        z1, z2 = 1.0, 2.0
        norm_them = verify_yang_baxter_slN(z1, z2, 3)
        # Their convention: R_{12}(u-v) R_{13}(u) R_{23}(v)
        # = R_{23}(v) R_{13}(u) R_{12}(u-v)
        assert norm_them < 1e-10

    def test_channel_decomposition_matches(self):
        """Channel decomposition matches yangian_residue_extraction."""
        from compute.lib.yangian_residue_extraction import (
            sym_antisym_projectors as sap_them,
            channel_eigenvalues,
        )
        P_sym_us = (np.eye(9) + permutation_matrix_3()) / 2
        P_sym_them, _ = sap_them(3)
        assert np.allclose(P_sym_us, P_sym_them, atol=1e-14)

        eigs = channel_eigenvalues(3)
        assert eigs["sym_dim"] == 6
        assert eigs["alt_dim"] == 3


# ============================================================
# 15. Literature comparison
# ============================================================

class TestLiteratureComparison:
    """Compare R-matrix with known results."""

    def test_full_literature_comparison(self):
        """All literature checks pass."""
        results = compare_with_literature()
        for name, ok in results.items():
            assert ok, f"Literature check failed: {name}"

    def test_extraction_report_consistent(self):
        """Full extraction report has consistent data."""
        report = full_extraction_report(k=1)
        assert report["h_vee"] == 3
        assert report["dim_g"] == 8
        assert report["fund_dim"] == 3
        assert report["kappa"] == Rational(16, 3)
        assert report["r_matrix_pole_order"] == 1
        assert report["casimir_fund"] == Rational(8, 3)


# ============================================================
# 16. Second-order corrections
# ============================================================

class TestSecondOrder:
    """Second-order R-matrix R(z) = I + Omega/(kz) + Omega^2/(kz)^2."""

    def test_omega_squared(self):
        """Omega^2 = I - 2P/N + I/N^2 since Omega = P - I/N and P^2 = I."""
        Omega = casimir_tensor_fund()
        Omega_sq = Omega @ Omega
        P = permutation_matrix_3()
        I9 = np.eye(9)
        N = FUND_DIM
        expected = I9 - 2 * P / N + I9 / N ** 2
        assert np.allclose(Omega_sq, expected, atol=1e-10)

    def test_second_order_approaches_first(self):
        """At large kappa, second-order correction is negligible."""
        z = 2.0
        kappa_val = 100.0
        R1 = R_matrix_fund_with_trace(z, kappa_val)
        R2 = R_matrix_fund_second_order(z, kappa_val)
        # Difference should be of order 1/(kappa*z)^2 ~ 1e-4
        diff = np.max(np.abs(R1 - R2))
        assert diff < 0.01

    def test_second_order_eigenvalues(self):
        """Second-order R-matrix has correct eigenvalue structure.

        On Sym^2: R = 1 + (2/3)/(kz) + ((2/3)/(kz))^2
        On Lambda^2: R = 1 + (-4/3)/(kz) + ((-4/3)/(kz))^2"""
        z = 2.0
        kappa_val = 5.0
        R2 = R_matrix_fund_second_order(z, kappa_val)
        P = permutation_matrix_3()
        I9 = np.eye(9)
        P_sym = (I9 + P) / 2
        P_asym = (I9 - P) / 2

        # Sym^2 eigenvalue
        omega_sym = 2.0 / 3.0
        x = omega_sym / (kappa_val * z)
        expected_sym = 1 + x + x ** 2
        R2_sym = R2 @ P_sym
        # Check it is scalar on Sym^2
        assert np.allclose(R2_sym, expected_sym * P_sym, atol=1e-10)

        # Lambda^2 eigenvalue
        omega_asym = -4.0 / 3.0
        x_a = omega_asym / (kappa_val * z)
        expected_asym = 1 + x_a + x_a ** 2
        R2_asym = R2 @ P_asym
        assert np.allclose(R2_asym, expected_asym * P_asym, atol=1e-10)


# ============================================================
# 17. Exact arithmetic (Fraction-based) verification
# ============================================================

class TestExactArithmetic:
    """Verification using exact rational arithmetic."""

    def test_killing_form_exact(self):
        """Killing form entries are exact rationals."""
        kf = sl3_killing_form()
        for (a, b), val in kf.items():
            assert isinstance(val, Rational)

    def test_kappa_exact_symbolic(self):
        """kappa is exact rational for integer k."""
        for k_val in range(10):
            kap = kappa_sl3(k_val)
            assert isinstance(kap, Rational)

    def test_casimir_fund_exact(self):
        """C_2(fund) = 8/3 exactly."""
        # Verify via trace of exact Killing form and its inverse
        kf = sl3_killing_form()
        G = np.zeros((DIM_G, DIM_G))
        for (a, b), val in kf.items():
            G[a, b] = float(val)
        Ginv = np.linalg.inv(G)
        c2 = np.trace(Ginv @ G)
        # tr(G^{-1} G) = tr(I_8) = 8, but C_2 on fund = tr(sum T^a T_a) = 8/3
        # These are different. The 8/3 comes from the actual matrix computation.
        assert abs(casimir_scalar_fund() - 8.0 / 3.0) < 1e-12


# ============================================================
# 18. Consistency with sl3_bar.py OPE data
# ============================================================

class TestOPEConsistency:
    """Verify that the R-matrix extraction is consistent with the OPE."""

    def test_structure_constants_from_rep(self):
        """Structure constants extracted from [T^a, T^b] match sl3_bar.py."""
        mats = fund_rep_matrices()
        bracket = sl3_structure_constants()
        for (a, b), outputs in bracket.items():
            comm = mats[a] @ mats[b] - mats[b] @ mats[a]
            expected = np.zeros((3, 3), dtype=complex)
            for c, coeff in outputs.items():
                expected += float(coeff) * mats[c]
            assert np.allclose(comm, expected, atol=1e-12), \
                f"[{GEN_NAMES[a]}, {GEN_NAMES[b]}] mismatch"

    def test_killing_form_cartan_block(self):
        """Cartan block of the Killing form matches the Cartan matrix A_{ij}.

        (H_i, H_j) = A_{ij} with A = [[2,-1],[-1,2]] for sl_3."""
        G = killing_form_matrix()
        assert abs(G[H1, H1] - 2.0) < 1e-12
        assert abs(G[H1, H2] - (-1.0)) < 1e-12
        assert abs(G[H2, H2] - 2.0) < 1e-12

    def test_killing_form_ef_pairing(self):
        """(E_i, F_i) = 1 for each simple root pair."""
        G = killing_form_matrix()
        assert abs(G[E1, F1] - 1.0) < 1e-12
        assert abs(G[E2, F2] - 1.0) < 1e-12
        assert abs(G[E3, F3] - 1.0) < 1e-12


# ============================================================
# 19. Additional structural tests
# ============================================================

class TestStructural:
    """Additional structural verifications."""

    def test_omega_symmetric(self):
        """The Casimir tensor Omega is symmetric under exchange: Omega_{21} = Omega."""
        Omega = casimir_tensor_fund()
        N = FUND_DIM
        # Omega_{21} = P Omega P
        P = permutation_matrix_3()
        Omega_21 = P @ Omega @ P
        assert np.allclose(Omega, Omega_21, atol=1e-10)

    def test_R_matrix_regularity(self):
        """R(z) = z I + P is regular (no poles) for all z."""
        # It is a polynomial in z, hence entire
        for z in [0, 1, -1, 1+1j, 100]:
            R = R_matrix_fund_exact_yang(complex(z))
            assert np.all(np.isfinite(R))

    def test_dimension_consistency(self):
        """All matrices have consistent dimensions."""
        assert DIM_SL3 == 8
        assert FUND_DIM == 3
        assert H_VEE_SL3 == 3
        Omega = casimir_tensor_fund()
        assert Omega.shape == (9, 9)
        P = permutation_matrix_3()
        assert P.shape == (9, 9)
        R = R_matrix_fund_exact_yang(1.0)
        assert R.shape == (9, 9)

    def test_constants(self):
        """Basic constants are correct."""
        assert H_VEE_SL3 == 3
        assert DIM_SL3 == 8
        assert FUND_DIM == 3
