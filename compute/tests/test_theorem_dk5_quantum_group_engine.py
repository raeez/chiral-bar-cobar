r"""Tests for DK-5: Full quantum group U_q(sl_2) from bar-cobar data.

Multi-path verification covering:
  V1. Yang R-matrix construction and Yang-Baxter equation
  V2. Quantum Casimir from partial trace of R_{12} R_{21}
  V3. RTT relations for the evaluation monodromy matrix
  V4. Hopf algebra axioms (coassociativity, counit, antipode)
  V5. Clebsch-Gordan from R-matrix eigendecomposition
  V6. Coproduct reconstruction via FRT (DK-5 core)
  V7. Strong unitarity and crossing symmetry
  V8. Verlinde truncation at roots of unity
  V9. DK-5 gap analysis and summary
"""

import math
import cmath

import numpy as np
import pytest
from numpy import linalg as la

from compute.lib.theorem_dk5_quantum_group_engine import (
    permutation_operator,
    partial_trace_1,
    partial_trace_2,
    yang_r_matrix_sl2,
    yang_r_matrix_inverse_sl2,
    verify_ybe_sl2,
    quantum_casimir_from_r_matrix,
    monodromy_matrix_sl2,
    verify_rtt_relation,
    build_hopf_sl2,
    verify_hopf_axioms,
    r_matrix_eigendecomposition,
    clebsch_gordan_from_r_matrix,
    coproduct_from_r_matrix,
    dk5_gap_analysis,
    verify_strong_unitarity,
    verify_crossing_symmetry,
    quantum_dimension,
    verlinde_truncation,
)


TOL = 1e-10


# =====================================================================
# V1.  Yang R-matrix basics
# =====================================================================

class TestYangRMatrixBasics:
    """Verify Yang R-matrix construction and fundamental properties."""

    def test_permutation_operator_square(self):
        """P^2 = I (involution)."""
        P = permutation_operator(2)
        assert la.norm(P @ P - np.eye(4, dtype=complex)) < TOL

    def test_permutation_operator_trace(self):
        """tr(P) = d for C^d tensor C^d."""
        for d in [2, 3, 4]:
            P = permutation_operator(d)
            assert abs(np.trace(P) - d) < TOL

    def test_permutation_operator_eigenvalues(self):
        """P on C^2 x C^2 has eigenvalues +1 (x3) and -1 (x1)."""
        P = permutation_operator(2)
        eigs = sorted(np.real(la.eigvals(P)))
        assert abs(eigs[0] - (-1.0)) < TOL
        assert all(abs(e - 1.0) < TOL for e in eigs[1:])

    def test_r_matrix_at_zero(self):
        """R(0) = hbar P (reduces to permutation times hbar)."""
        hbar = 1.0
        R = yang_r_matrix_sl2(0, hbar)
        P = permutation_operator(2)
        assert la.norm(R - hbar * P) < TOL

    def test_r_matrix_classical_limit(self):
        """At hbar -> 0, R(u) -> u I (trivial braiding)."""
        R = yang_r_matrix_sl2(3.0, 1e-14)
        assert la.norm(R - 3.0 * np.eye(4, dtype=complex)) < 1e-12

    def test_r_matrix_eigenvalues(self):
        """R(u) has eigenvalues u+hbar (x3) and u-hbar (x1)."""
        u, hbar = 2.0, 1.0
        R = yang_r_matrix_sl2(u, hbar)
        eigs = sorted(np.real(la.eigvals(R)))
        assert abs(eigs[0] - (u - hbar)) < TOL
        assert all(abs(e - (u + hbar)) < TOL for e in eigs[1:])

    def test_partial_trace_identity(self):
        """tr_2(I_4) = 2 I_2."""
        I4 = np.eye(4, dtype=complex)
        result = partial_trace_2(I4, 2)
        assert la.norm(result - 2 * np.eye(2, dtype=complex)) < TOL

    def test_partial_trace_permutation(self):
        """tr_2(P) = I_2 for C^2 x C^2."""
        P = permutation_operator(2)
        result = partial_trace_2(P, 2)
        assert la.norm(result - np.eye(2, dtype=complex)) < TOL


# =====================================================================
# V2.  Yang-Baxter equation
# =====================================================================

class TestYangBaxterEquation:
    """Verify R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)."""

    @pytest.mark.parametrize("u,v", [
        (1.0, 2.0), (3.5, -1.2), (0.1, 0.7), (2.0+1j, 1.0-0.5j),
    ])
    def test_ybe_various_parameters(self, u, v):
        result = verify_ybe_sl2(u, v, hbar=1.0)
        assert result['ybe_holds'], f"YBE failed at u={u}, v={v}: residual={result['residual_norm']}"

    def test_ybe_complex_hbar(self):
        """YBE holds for complex hbar."""
        result = verify_ybe_sl2(1.0, 2.0, hbar=0.5 + 0.3j)
        assert result['ybe_holds']

    def test_ybe_large_parameters(self):
        """YBE holds for large spectral parameters."""
        result = verify_ybe_sl2(100.0, -50.0, hbar=1.0)
        assert result['ybe_holds']


# =====================================================================
# V3.  Quantum Casimir
# =====================================================================

class TestQuantumCasimir:
    """Verify C_q = tr_2(R_{12} R_{21}) is scalar."""

    def test_casimir_is_scalar(self):
        result = quantum_casimir_from_r_matrix(1.0, 1.0)
        assert result['is_scalar']

    def test_casimir_analytic_formula(self):
        """C_q = (2u^2 + 2hbar^2 + 2u*hbar) I_2."""
        for u, hbar in [(1.0, 1.0), (2.0, 0.5), (3.0, 2.0), (0.5+1j, 1.0)]:
            result = quantum_casimir_from_r_matrix(u, hbar)
            assert result['analytic_matches'], (
                f"Casimir mismatch at u={u}, hbar={hbar}: "
                f"got {result['scalar_value']}, expected {result['analytic_value']}"
            )

    def test_casimir_classical_limit(self):
        """At hbar=0, C_q = 2u^2 I (no quantum correction)."""
        u = 3.0
        result = quantum_casimir_from_r_matrix(u, 1e-14)
        assert abs(result['scalar_value'] - 2 * u ** 2) < 1e-10


# =====================================================================
# V4.  RTT relations
# =====================================================================

class TestRTTRelations:
    """Verify R T_1 T_2 = T_2 T_1 R."""

    def test_rtt_single_evaluation(self):
        """RTT for T(u) = R(u) (single evaluation point)."""
        result = verify_rtt_relation(1.0, 2.0, hbar=1.0)
        assert result['rtt_holds']

    def test_rtt_composite_monodromy(self):
        """RTT for composite T with two evaluation points."""
        params = {'eval_points': [0.5, 1.5]}
        result = verify_rtt_relation(3.0, 1.0, hbar=1.0, params=params)
        assert result['rtt_holds']

    def test_rtt_three_evaluation_points(self):
        """RTT for composite T with three evaluation points."""
        params = {'eval_points': [0.2, 0.8, 1.4]}
        result = verify_rtt_relation(2.5, 0.5, hbar=1.0, params=params)
        assert result['rtt_holds']


# =====================================================================
# V5.  Hopf algebra axioms
# =====================================================================

class TestHopfAlgebra:
    """Verify all Hopf algebra axioms for U_q(sl_2)."""

    @pytest.mark.parametrize("hbar", [0.3, 0.5, 1.0, 0.1+0.2j])
    def test_hopf_axioms_various_q(self, hbar):
        result = verify_hopf_axioms(hbar)
        assert result['all_pass'], f"Hopf axioms failed at hbar={hbar}: {result}"

    def test_algebra_relations(self):
        """[E,F] = (K-K^{-1})/(q-q^{-1}), KEK^{-1} = q^2 E, KFK^{-1} = q^{-2} F."""
        result = verify_hopf_axioms(0.3)
        assert result['algebra_EF']
        assert result['algebra_KEK']
        assert result['algebra_KFK']

    def test_coassociativity(self):
        """(Delta tensor id) Delta = (id tensor Delta) Delta on K."""
        result = verify_hopf_axioms(0.5)
        assert result['coassoc_K']

    def test_antipode_on_generators(self):
        """m(S tensor id) Delta(x) = epsilon(x) I for x = E, F, K."""
        result = verify_hopf_axioms(0.7)
        assert result['antipode_E']
        assert result['antipode_F']
        assert result['antipode_K']
        assert result['antipode_K_right']

    def test_antipode_explicit_formulas(self):
        """S(E) = -EK^{-1}, S(F) = -KF, S(K) = K^{-1}."""
        h = build_hopf_sl2(0.4)
        assert la.norm(h.S_E - (-h.E @ h.K_inv)) < TOL
        assert la.norm(h.S_F - (-h.K @ h.F)) < TOL
        assert la.norm(h.S_K - h.K_inv) < TOL

    def test_counit_values(self):
        """epsilon(E) = 0, epsilon(F) = 0, epsilon(K) = 1."""
        h = build_hopf_sl2(0.3)
        assert abs(h.epsilon_E) < TOL
        assert abs(h.epsilon_F) < TOL
        assert abs(h.epsilon_K - 1.0) < TOL


# =====================================================================
# V6.  Clebsch-Gordan from R-matrix
# =====================================================================

class TestClebschGordan:
    """Verify CG decomposition from R-matrix eigenstructure."""

    def test_fund_tensor_fund_dimensions(self):
        """V_{1/2} x V_{1/2} = V_1 (dim 3) + V_0 (dim 1)."""
        decomp = r_matrix_eigendecomposition(1.0, 1.0)
        assert decomp['rank_symmetric'] == 3
        assert decomp['rank_antisymmetric'] == 1
        assert decomp['cg_dimensions_correct']

    def test_projectors_sum_to_identity(self):
        decomp = r_matrix_eigendecomposition(1.0, 1.0)
        assert decomp['projectors_sum_to_identity']

    def test_projectors_orthogonal(self):
        decomp = r_matrix_eigendecomposition(1.0, 1.0)
        assert decomp['projectors_orthogonal']

    def test_reconstruction_from_projectors(self):
        """R = (u+hbar) P_sym + (u-hbar) P_anti."""
        decomp = r_matrix_eigendecomposition(2.0, 0.5)
        assert decomp['reconstruction_from_projectors']

    def test_cg_comparison(self):
        """CG coefficients from R-matrix match standard sl_2."""
        cg = clebsch_gordan_from_r_matrix(0.5, 0.5, hbar=0.3)
        assert cg['cg_decomposition_correct']
        assert cg['channels'] == [0, 1]
        assert cg['dimensions'] == [1, 3]

    def test_casimir_differences(self):
        """C_2(1) - 2*C_2(1/2) = 1/2, C_2(0) - 2*C_2(1/2) = -3/2."""
        cg = clebsch_gordan_from_r_matrix(0.5, 0.5, hbar=0.3)
        assert abs(cg['casimir_J1'] - 0.5) < TOL
        assert abs(cg['casimir_J0'] - (-1.5)) < TOL
        assert abs(cg['casimir_difference'] - 2.0) < TOL


# =====================================================================
# V7.  Coproduct reconstruction (DK-5 core)
# =====================================================================

class TestCoproductReconstruction:
    """Verify FRT coproduct reconstruction from R-matrix."""

    @pytest.mark.parametrize("hbar", [0.3, 0.5, 1.0, 0.2+0.1j])
    def test_frt_coproduct_all_pass(self, hbar):
        result = coproduct_from_r_matrix(hbar)
        assert result['all_pass'], f"FRT failed at hbar={hbar}: {result}"

    def test_delta_algebra_map(self):
        """Delta is an algebra homomorphism: Delta(xy) = Delta(x) Delta(y)."""
        result = coproduct_from_r_matrix(0.3)
        assert result['delta_is_algebra_map_EF']
        assert result['delta_is_algebra_map_KEK']
        assert result['delta_is_algebra_map_KFK']

    def test_coassociativity_E(self):
        """(Delta tensor id) Delta(E) = (id tensor Delta) Delta(E)."""
        result = coproduct_from_r_matrix(0.5)
        assert result['coassociativity_E']


# =====================================================================
# V8.  Strong unitarity and crossing
# =====================================================================

class TestUnitarityAndCrossing:
    """Verify strong unitarity R(u) R_{21}(-u) = f(u) I."""

    @pytest.mark.parametrize("u", [1.0, 2.5, 0.3+1j])
    def test_strong_unitarity(self, u):
        result = verify_strong_unitarity(u, hbar=1.0)
        assert result['strong_unitarity_holds']

    def test_strong_unitarity_scalar(self):
        """f(u) = hbar^2 - u^2."""
        u, hbar = 2.0, 1.5
        result = verify_strong_unitarity(u, hbar)
        expected = hbar ** 2 - u ** 2
        assert abs(result['scalar_function'] - expected) < TOL

    def test_r_matrix_inverse(self):
        """R(u)^{-1} = R(-u) / (hbar^2 - u^2)."""
        u, hbar = 1.5, 1.0
        R = yang_r_matrix_sl2(u, hbar)
        R_inv = yang_r_matrix_inverse_sl2(u, hbar)
        assert la.norm(R @ R_inv - np.eye(4, dtype=complex)) < TOL

    def test_crossing_symmetry(self):
        """Crossing: R(u)^{t2} R(-u-N*hbar)^{t2} = -u(u+N*hbar) I for sl_2."""
        result = verify_crossing_symmetry(1.0, 1.0)
        assert result['crossing_product_is_scalar'], (
            f"Crossing not scalar: off_diag={result['off_diagonal_norm']}"
        )
        assert result['scalar_matches_analytic']

    def test_crossing_symmetry_various(self):
        """Crossing holds for various u, hbar."""
        for u, hbar in [(2.0, 0.5), (0.3, 1.5), (1.0 + 0.5j, 1.0)]:
            result = verify_crossing_symmetry(u, hbar)
            assert result['crossing_product_is_scalar'], f"Failed at u={u}, hbar={hbar}"
            assert result['scalar_matches_analytic']


# =====================================================================
# V9.  Verlinde truncation
# =====================================================================

class TestVerlindetruncation:
    """Verify quantum dimension vanishing at roots of unity."""

    def test_level_1_truncation(self):
        """Level k=1: j_max = 1/2, only V_0 and V_{1/2}."""
        result = verlinde_truncation(1)
        assert result['j_max'] == 0.5
        assert result['num_irreps'] == 2

    def test_level_2_truncation(self):
        """Level k=2: j_max = 1, reps V_0, V_{1/2}, V_1."""
        result = verlinde_truncation(2)
        assert result['j_max'] == 1.0
        assert result['num_irreps'] == 3

    def test_quantum_dim_classical_limit(self):
        """At q -> 1, dim_q(V_j) -> 2j+1."""
        q = np.exp(1e-14 * 1j)
        for two_j in range(0, 6):
            j = two_j / 2.0
            d = quantum_dimension(j, q)
            assert abs(d - (2 * j + 1)) < 1e-8

    def test_truncation_dimension_vanishes(self):
        """At level k with q=exp(pi i/(k+h^v)), dim_q vanishes at j=(k+1)/2.

        [2j+1]_q = 0 when 2j+1 = k+h^v = k+2, i.e. j = (k+1)/2.
        This is the first spin ABOVE the Verlinde range j <= k/2.
        """
        for k in [1, 2, 3, 4]:
            h_dual = 2
            q = np.exp(1j * math.pi / (k + h_dual))
            j_trunc = (k + 1) / 2.0  # first disallowed spin
            d = quantum_dimension(j_trunc, q)
            assert abs(d) < 1e-8, f"Truncation failed at k={k}: dim_q(V_{j_trunc}) = {d}"


# =====================================================================
# V10.  DK-5 gap analysis (the main theorem)
# =====================================================================

class TestDK5GapAnalysis:
    """Verify the DK-5 gap closes for sl_2 at generic q."""

    def test_dk5_closes(self):
        result = dk5_gap_analysis(hbar=0.3)
        assert result['dk5_closes_for_sl2']

    def test_r_matrix_separates_irreps(self):
        result = dk5_gap_analysis(hbar=0.5)
        assert result['r_matrix_separates_irreps']

    def test_generators_visible(self):
        result = dk5_gap_analysis(hbar=0.3)
        assert result['generators_visible_in_fund']
        assert result['generator_count'] == 3

    def test_deformation_obstruction_vanishes(self):
        """H^2(U_q(sl_2), k) = 0 at generic q."""
        result = dk5_gap_analysis(hbar=0.3)
        assert result['deformation_obstruction_vanishes']

    def test_frt_reconstruction_in_gap_analysis(self):
        result = dk5_gap_analysis(hbar=0.5)
        assert result['frt_reconstruction_works']

    def test_hom_dimension(self):
        """dim Hom(V x V, V x V) = 2 (from 2 irreducible summands)."""
        result = dk5_gap_analysis(hbar=0.3)
        assert result['hom_dimension'] == 2

    def test_dk5_various_hbar(self):
        """DK-5 closes for various values of hbar."""
        for hbar in [0.1, 0.3, 0.7, 1.0, 1.5]:
            result = dk5_gap_analysis(hbar=hbar)
            assert result['dk5_closes_for_sl2'], f"DK-5 failed at hbar={hbar}"
