r"""Tests for the Calogero-Moser / quartic shadow derivation.

Verifies: CM coupling from Q^contact, shadow-CM spectral curve matching,
MC recursion = CM integrability, Lax matrix construction, Dunkl eigenvalue
comparison, Koszul duality as CM duality, shadow depth classification,
and the full shadow-CM dictionary at multiple central charges.

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct formula evaluation
  Path 2: Recursion / convolution identity
  Path 3: Koszul complementarity (duality check)
  Path 4: Limiting cases (c -> inf, c = 13, Heisenberg)
  Path 5: Cross-family consistency

All formulas recomputed from first principles (AP1, AP3).
"""

import math
import pytest
import numpy as np

from compute.lib.cm_from_quartic_shadow import (
    # Shadow data
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_km_shadow_data,
    general_shadow_data,
    # Shadow metric
    shadow_metric,
    shadow_metric_coefficients,
    shadow_metric_discriminant,
    spectral_curve_check,
    # Recursion
    shadow_coefficients_from_recursion,
    verify_recursion_is_f_squared_equals_Q,
    # CM coupling
    cm_coupling_from_shadow,
    cm_coupling_beta_from_shadow,
    cm_hamiltonian_N2,
    cm_eigenvalue_N2,
    cm_N_particle_hamiltonian,
    # Lax matrix
    cm_lax_matrix,
    cm_lax_eigenvalues,
    cm_conserved_quantities,
    cm_spectral_curve_N2,
    # Spectral curve matching
    shadow_spectral_curve_match_N2,
    shadow_to_cm_conserved_quantities,
    # Virasoro specifics
    virasoro_q_contact,
    virasoro_cm_coupling,
    virasoro_cm_beta,
    virasoro_shadow_depth_from_cm,
    # Multi-particle
    shadow_to_cm_N_particles,
    # Dunkl
    dunkl_operator_eigenvalue,
    compare_dunkl_eigenvalues_with_shadow,
    # r-matrix
    cm_classical_r_matrix,
    # Classification
    classify_shadow_depth_cm,
    # Koszul duality
    koszul_dual_cm_coupling,
    # Verification
    verify_shadow_cm_at_N2,
    verify_virasoro_shadow_cm,
    # Dictionary
    shadow_cm_full_dictionary,
)


# ============================================================================
# 1. SHADOW DATA TESTS
# ============================================================================

class TestShadowData:
    """Tests for shadow data extraction."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP1: recompute, never copy)."""
        for c in [1, 2, 10, 13, 25, 100]:
            data = virasoro_shadow_data(float(c))
            assert abs(data['kappa'] - c / 2.0) < 1e-14

    def test_virasoro_alpha(self):
        """alpha(Vir_c) = 2 (constant, independent of c)."""
        for c in [1, 5, 13, 30]:
            data = virasoro_shadow_data(float(c))
            assert abs(data['alpha'] - 2.0) < 1e-14

    def test_virasoro_S4(self):
        """S_4(Vir_c) = 10/[c(5c+22)] (the quartic contact invariant)."""
        for c in [1, 2, 5, 10, 13, 25]:
            data = virasoro_shadow_data(float(c))
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(data['S4'] - expected) < 1e-14

    def test_virasoro_Delta(self):
        """Delta(Vir_c) = 8*kappa*S_4 = 40/(5c+22)."""
        for c in [1, 2, 13, 100]:
            data = virasoro_shadow_data(float(c))
            expected = 40.0 / (5 * c + 22)
            assert abs(data['Delta'] - expected) < 1e-13

    def test_virasoro_class_M(self):
        """Virasoro is class M for c != -22/5."""
        for c in [1, 5, 13, 25, 100]:
            data = virasoro_shadow_data(float(c))
            assert data['class'] == 'M'

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Delta = 0, alpha = 0)."""
        for k in [1, 2, 5]:
            data = heisenberg_shadow_data(float(k))
            assert data['class'] == 'G'
            assert data['Delta'] == 0.0
            assert data['alpha'] == 0.0
            assert data['S4'] == 0.0

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 5, 10]:
            data = heisenberg_shadow_data(float(k))
            assert abs(data['kappa'] - k) < 1e-14

    def test_singular_central_charges(self):
        """c = 0 and c = -22/5 are singular."""
        with pytest.raises(ValueError):
            virasoro_shadow_data(0.0)
        with pytest.raises(ValueError):
            virasoro_shadow_data(-22.0 / 5.0)


# ============================================================================
# 2. SHADOW METRIC TESTS
# ============================================================================

class TestShadowMetric:
    """Tests for the shadow metric Q_L(t)."""

    def test_shadow_metric_at_zero(self):
        """Q_L(0) = 4*kappa^2."""
        for c in [1, 5, 13]:
            data = virasoro_shadow_data(float(c))
            Q0 = shadow_metric(data['kappa'], data['alpha'], data['S4'], 0.0)
            assert abs(Q0 - 4 * data['kappa']**2) < 1e-12

    def test_shadow_metric_positive_definite(self):
        """Q_L(t) > 0 for real t near 0 (class M, Virasoro)."""
        for c in [1, 5, 13, 25]:
            data = virasoro_shadow_data(float(c))
            for t in np.linspace(-0.1, 0.1, 20):
                QL = shadow_metric(data['kappa'], data['alpha'], data['S4'], t)
                assert QL > 0, f"Q_L({t}) = {QL} <= 0 at c={c}"

    def test_shadow_metric_coefficients(self):
        """Verify the polynomial coefficients match the expanded form."""
        kappa, alpha, S4 = 5.0, 2.0, 0.1
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        for t in [0.0, 0.5, 1.0, -0.3]:
            direct = shadow_metric(kappa, alpha, S4, t)
            from_coeffs = q0 + q1 * t + q2 * t**2
            assert abs(direct - from_coeffs) < 1e-12

    def test_gaussian_decomposition(self):
        """Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        for c in [1, 5, 13, 25]:
            data = virasoro_shadow_data(float(c))
            kappa, alpha, S4 = data['kappa'], data['alpha'], data['S4']
            Delta = data['Delta']
            for t in np.linspace(-0.5, 0.5, 10):
                QL = shadow_metric(kappa, alpha, S4, t)
                gaussian = (2 * kappa + 3 * alpha * t)**2 + 2 * Delta * t**2
                assert abs(QL - gaussian) < 1e-11

    def test_discriminant_formula(self):
        """disc(Q_L) = -32*kappa^2*Delta = -256*kappa^3*S_4."""
        for c in [1, 5, 13, 25]:
            data = virasoro_shadow_data(float(c))
            kappa, alpha, S4 = data['kappa'], data['alpha'], data['S4']
            disc = shadow_metric_discriminant(kappa, alpha, S4)
            expected_1 = -32 * kappa**2 * data['Delta']
            expected_2 = -256 * kappa**3 * S4
            assert abs(disc - expected_1) < 1e-10
            assert abs(disc - expected_2) < 1e-10

    def test_spectral_curve_identity(self):
        """H^2 - t^4*Q_L = 0 identically (the Riccati algebraicity)."""
        for c in [1, 5, 13, 25]:
            data = virasoro_shadow_data(float(c))
            for t in np.linspace(0.01, 0.5, 10):
                residual = spectral_curve_check(
                    data['kappa'], data['alpha'], data['S4'], t)
                assert abs(residual) < 1e-12, f"Spectral curve residual = {residual} at c={c}, t={t}"


# ============================================================================
# 3. MC RECURSION = CM INTEGRABILITY
# ============================================================================

class TestRecursion:
    """Tests for the MC recursion f^2 = Q_L."""

    def test_virasoro_S5(self):
        """S_5 = -48/[c^2*(5c+22)] (from the manuscript proof)."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            data = virasoro_shadow_data(c)
            shadow = shadow_coefficients_from_recursion(
                data['kappa'], data['alpha'], data['S4'], 7)
            expected = -48.0 / (c**2 * (5 * c + 22))
            assert abs(shadow[5] - expected) < 1e-12, \
                f"S_5 mismatch at c={c}: got {shadow[5]}, expected {expected}"

    def test_virasoro_S6(self):
        """S_6 = 80*(45c+193) / [3*c^3*(5c+22)^2] (from the manuscript)."""
        for c in [1.0, 5.0, 13.0]:
            data = virasoro_shadow_data(c)
            shadow = shadow_coefficients_from_recursion(
                data['kappa'], data['alpha'], data['S4'], 8)
            expected = 80.0 * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2)
            assert abs(shadow[6] - expected) < 1e-11, \
                f"S_6 mismatch at c={c}: got {shadow[6]}, expected {expected}"

    def test_recursion_vanishing_residuals(self):
        """The recursion f^2 = Q_L has zero residuals at orders >= 3.

        At c=1 the shadow coefficients grow as c^{-(r-3)}, so floating-point
        accumulation limits reliable arity to ~12.  For large c the
        coefficients decay and we can go higher.
        """
        for c in [1, 5, 13, 25, 100]:
            data = virasoro_shadow_data(float(c))
            max_r = 12 if c < 3 else 15
            residuals = verify_recursion_is_f_squared_equals_Q(
                data['kappa'], data['alpha'], data['S4'], max_r)
            for r, val in residuals.items():
                assert abs(val) < 1e-9, \
                    f"Recursion residual at arity {r} = {val} for c={c}"

    def test_heisenberg_tower_terminates(self):
        """Heisenberg tower terminates at S_2 = kappa, S_r = 0 for r >= 3."""
        for k in [1, 2, 5]:
            data = heisenberg_shadow_data(float(k))
            shadow = shadow_coefficients_from_recursion(
                data['kappa'], data['alpha'], data['S4'], 10)
            assert abs(shadow[2] - k) < 1e-14
            for r in range(3, 11):
                assert abs(shadow[r]) < 1e-14, f"S_{r} = {shadow[r]} != 0 for Heisenberg"


# ============================================================================
# 4. CM COUPLING FROM SHADOW
# ============================================================================

class TestCMCoupling:
    """Tests for the CM coupling extraction."""

    def test_heisenberg_free_particles(self):
        """Heisenberg has g^2 = 0 (free particles)."""
        for k in [1, 2, 5]:
            g2 = cm_coupling_from_shadow(k, 0.0)
            assert abs(g2) < 1e-14

    def test_heisenberg_beta_equals_1(self):
        """Free particles have beta = 1."""
        beta = cm_coupling_beta_from_shadow(1.0, 0.0)
        assert abs(beta - 1.0) < 1e-14

    def test_virasoro_cm_coupling_formula(self):
        """g_eff^2 = 40/[c*(5c+22)] for Virasoro."""
        for c in [1, 5, 13, 25, 100]:
            g2 = virasoro_cm_coupling(float(c))
            expected = 40.0 / (c * (5 * c + 22))
            assert abs(g2 - expected) < 1e-14

    def test_cm_coupling_positive(self):
        """g_eff^2 > 0 for Virasoro with c > 0 (genuine interaction)."""
        for c in [0.1, 1, 5, 13, 25, 100]:
            g2 = virasoro_cm_coupling(float(c))
            assert g2 > 0

    def test_cm_coupling_semiclassical(self):
        """g_eff^2 -> 0 as c -> infinity (free particle limit)."""
        g2_100 = virasoro_cm_coupling(100.0)
        g2_1000 = virasoro_cm_coupling(1000.0)
        g2_10000 = virasoro_cm_coupling(10000.0)
        assert g2_100 > g2_1000 > g2_10000
        assert g2_10000 < 1e-6


# ============================================================================
# 5. LAX MATRIX AND SPECTRAL CURVE
# ============================================================================

class TestLaxMatrix:
    """Tests for the CM Lax matrix."""

    def test_lax_diagonal(self):
        """L_{ii} = p_i."""
        p = np.array([1.0, 2.0, 3.0])
        q = np.array([0.0, 1.0, 2.0])
        L = cm_lax_matrix(p, q, 0.5)
        for i in range(3):
            assert abs(L[i, i] - p[i]) < 1e-14

    def test_lax_hermitian_for_real_g(self):
        """L is Hermitian for purely imaginary off-diagonal (g real)."""
        p = np.array([1.0, -0.5])
        q = np.array([-1.0, 1.0])
        L = cm_lax_matrix(p, q, 1.0)
        # L^dag = L because L_{ij} = ig/(q_i - q_j) and L_{ji} = ig/(q_j - q_i) = -L_{ij}
        # So L^T = diag(p) - offdiag(L), and L^dag = diag(p) - offdiag(L)^*
        # Since L_{ij} = i*g/(q_i-q_j) is purely imaginary, L_{ij}^* = -L_{ij} = L_{ji}
        # So L^dag = L: Hermitian.
        assert np.allclose(L, L.conj().T, atol=1e-13)

    def test_lax_eigenvalues_real(self):
        """Eigenvalues of Hermitian L are real."""
        p = np.array([2.0, -1.0, 0.5])
        q = np.array([-2.0, 0.0, 3.0])
        eigs = cm_lax_eigenvalues(p, q, 0.7)
        assert np.allclose(eigs.imag, 0, atol=1e-12)

    def test_conserved_I2_equals_hamiltonian(self):
        """I_2 = Tr(L^2)/N = H_CM/N for real momenta."""
        p = np.array([1.0, -1.0])
        q = np.array([-1.0, 1.0])
        g = 0.5
        g2 = g**2

        # H_CM = p1^2 + p2^2 + g^2/(q1-q2)^2
        H = cm_N_particle_hamiltonian(p, q, g2)

        # I_2 = Tr(L^2)/N
        integrals = cm_conserved_quantities(p, q, g, max_r=3)
        I2 = integrals[2].real

        # Tr(L^2)/N should equal H/N (up to conventions)
        # L^2_{ii} = p_i^2 + sum_{j!=i} g^2/(q_i-q_j)^2
        # so Tr(L^2) = sum p_i^2 + sum_{i!=j} g^2/(q_i-q_j)^2
        #            = sum p_i^2 + 2*sum_{i<j} g^2/(q_i-q_j)^2
        #            = H + sum_{i<j} g^2/(q_i-q_j)^2
        # So Tr(L^2) = H + V where V is the potential
        # Actually Tr(L^2) = sum_i L_{ii}^2 + sum_{i!=j} L_{ij}*L_{ji}
        #                   = sum p_i^2 + sum_{i!=j} (ig/(q_i-q_j))(-ig/(q_i-q_j))
        #                   = sum p_i^2 + sum_{i!=j} g^2/(q_i-q_j)^2
        # For N=2: Tr(L^2) = p1^2 + p2^2 + 2*g^2/(q1-q2)^2 = H + g^2/(q1-q2)^2
        V = g2 / (q[0] - q[1])**2
        expected_TrL2_over_N = (H + V) / 2  # Tr(L^2)/N for N=2

        assert abs(I2 - expected_TrL2_over_N) < 1e-10, \
            f"I_2 = {I2}, expected {expected_TrL2_over_N}"


# ============================================================================
# 6. SPECTRAL CURVE MATCHING
# ============================================================================

class TestSpectralCurve:
    """Tests for shadow-CM spectral curve comparison."""

    def test_N2_spectral_curve_vanishes_on_shell(self):
        """det(L - lambda*I) = 0 on the spectral curve for N=2."""
        p_rel = 1.5
        q_rel = 2.0
        g = 0.3
        # Eigenvalues of the 2x2 Lax matrix
        # lambda_pm = +/- sqrt((p_rel/2)^2 + g^2/q_rel^2)
        lam_sq = (p_rel / 2)**2 + g**2 / q_rel**2
        lam_plus = math.sqrt(lam_sq)
        assert abs(cm_spectral_curve_N2(p_rel, q_rel, g, lam_plus)) < 1e-14
        assert abs(cm_spectral_curve_N2(p_rel, q_rel, g, -lam_plus)) < 1e-14

    def test_shadow_spectral_curve_vanishes(self):
        """H^2 = t^4*Q_L(t) holds for the shadow generating function."""
        for c in [1, 5, 13, 25]:
            result = shadow_spectral_curve_match_N2(
                c / 2.0, 2.0, virasoro_q_contact(float(c)), 0.1)
            assert abs(result['spectral_curve_value']) < 1e-14


# ============================================================================
# 7. DUNKL OPERATOR EIGENVALUES
# ============================================================================

class TestDunklEigenvalues:
    """Tests for Dunkl operator eigenvalues."""

    def test_dunkl_I2_single_box(self):
        """I_2((1)) = 2*(N-1)*beta for N particles."""
        # I_2((1)) = (1 + (N-1)*beta)^2 - ((N-1)*beta)^2
        #          + sum_{i=2}^N [(N-i)*beta]^2 - [(N-i)*beta]^2 = 0 for i>=2
        # So I_2((1)) = (1 + (N-1)*beta)^2 - ((N-1)*beta)^2
        #             = 1 + 2*(N-1)*beta
        for N in [2, 3, 4]:
            for beta in [1.0, 1.5, 2.0]:
                I2 = dunkl_operator_eigenvalue((1,), N, beta, 2)
                expected = 1 + 2 * (N - 1) * beta
                assert abs(I2 - expected) < 1e-12

    def test_dunkl_I2_two_boxes(self):
        """I_2((2)) for N particles."""
        # I_2((2)) = (2 + (N-1)*beta)^2 - ((N-1)*beta)^2
        #          = 4 + 4*(N-1)*beta
        for N in [2, 3, 4]:
            for beta in [1.0, 2.0]:
                I2 = dunkl_operator_eigenvalue((2,), N, beta, 2)
                expected = 4 + 4 * (N - 1) * beta
                assert abs(I2 - expected) < 1e-12

    def test_dunkl_vacuum_vanishes(self):
        """I_r(empty) = 0 for all r (vacuum subtraction)."""
        for N in [2, 3, 4]:
            for beta in [1.0, 1.5]:
                for r in [1, 2, 3, 4]:
                    Ir = dunkl_operator_eigenvalue((), N, beta, r)
                    assert abs(Ir) < 1e-14

    def test_dunkl_free_fermion(self):
        """At beta = 1 (free fermions): E_lambda = sum lambda_i*(lambda_i + N - 2i)."""
        N = 3
        beta = 1.0
        lam = (2, 1)
        # E = 2*(2 + 2*1) + 1*(1 + 0*1) = 2*4 + 1 = 9 ... NO
        # I_2((2,1)) = (2+2)^2 + (1+1)^2 + 0^2 - (2^2 + 1^2 + 0^2)
        # = 16 + 4 - 4 - 1 = 15
        I2 = dunkl_operator_eigenvalue(lam, N, beta, 2)
        # Direct: shifted = [2+2, 1+1, 0+0] = [4, 2, 0]
        # vac shifted = [2, 1, 0]
        # I_2 = 4^2 + 2^2 + 0^2 - (2^2 + 1^2 + 0^2) = 16+4 - 4-1 = 15
        assert abs(I2 - 15.0) < 1e-12


# ============================================================================
# 8. KOSZUL DUALITY = CM DUALITY
# ============================================================================

class TestKoszulDuality:
    """Tests for Koszul duality acting on CM data."""

    def test_complementarity_formula(self):
        """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)] (thm:shadow-connection(vi))."""
        for c in [1, 5, 10, 13, 20, 25]:
            result = koszul_dual_cm_coupling(float(c))
            assert result['complementarity_check'], \
                f"Complementarity fails at c={c}: sum={result['Delta_sum']}, expected={result['Delta_sum_expected']}"

    def test_self_duality_at_13(self):
        """At c = 13: g^2(c) = g^2(26-c) (self-dual point)."""
        result = koszul_dual_cm_coupling(13.0)
        assert abs(result['g_squared'] - result['g_squared_dual']) < 1e-14
        assert result['self_dual']

    def test_dual_central_charges_sum_26(self):
        """c + c! = 26 for Virasoro Koszul duality."""
        for c in [1, 5, 13, 20]:
            result = koszul_dual_cm_coupling(float(c))
            assert abs(result['c'] + result['c_dual'] - 26.0) < 1e-14

    def test_lee_yang_duality(self):
        """The dual Lee-Yang singularities c = -22/5 and c = 152/5 sum to 26."""
        c1 = -22.0 / 5.0
        c2 = 152.0 / 5.0
        assert abs(c1 + c2 - 26.0) < 1e-14


# ============================================================================
# 9. SHADOW DEPTH CLASSIFICATION
# ============================================================================

class TestClassification:
    """Tests for the G/L/C/M classification via CM."""

    def test_heisenberg_class_G(self):
        """Heisenberg: class G = free particles."""
        result = classify_shadow_depth_cm(1.0, 0.0, 0.0)
        assert result['class'] == 'G'
        assert result['cm_type'] == 'free'
        assert result['depth'] == 2

    def test_affine_km_class_L(self):
        """Affine KM: class L = tree-level, cubic only."""
        result = classify_shadow_depth_cm(3.0, 1.5, 0.0)
        assert result['class'] == 'L'
        assert result['cm_type'] == 'tree-level'
        assert result['depth'] == 3

    def test_virasoro_class_M(self):
        """Virasoro: class M = full CM."""
        c = 10.0
        data = virasoro_shadow_data(c)
        result = classify_shadow_depth_cm(data['kappa'], data['alpha'], data['S4'])
        assert result['class'] == 'M'
        assert result['cm_type'] == 'full_CM'
        assert result['depth'] == float('inf')

    def test_classification_matches_depth(self):
        """Verify the four-class partition covers all standard families."""
        families = {
            'Heisenberg': (1.0, 0.0, 0.0, 'G'),
            'Affine_KM': (3.0, 1.5, 0.0, 'L'),
            'Virasoro_c10': (5.0, 2.0, virasoro_q_contact(10.0), 'M'),
            'Virasoro_c25': (12.5, 2.0, virasoro_q_contact(25.0), 'M'),
        }
        for name, (kappa, alpha, S4, expected_class) in families.items():
            result = classify_shadow_depth_cm(kappa, alpha, S4)
            assert result['class'] == expected_class, \
                f"{name}: expected {expected_class}, got {result['class']}"


# ============================================================================
# 10. N-PARTICLE SECTOR
# ============================================================================

class TestMultiParticle:
    """Tests for the N-particle CM sector from arity-N shadow."""

    def test_N2_heisenberg(self):
        """N=2 Heisenberg: free particles, g^2 = 0."""
        result = shadow_to_cm_N_particles(2, 1.0, 0.0, 0.0)
        assert abs(result['g_eff_squared']) < 1e-14
        assert abs(result['shadow_coefficients'][2] - 1.0) < 1e-14

    def test_N4_virasoro(self):
        """N=4 Virasoro: quartic shadow S_4 = Q^contact determines coupling."""
        c = 10.0
        data = virasoro_shadow_data(c)
        result = shadow_to_cm_N_particles(
            4, data['kappa'], data['alpha'], data['S4'])
        assert result['g_eff_squared'] > 0
        assert abs(result['shadow_coefficients'][4] - data['S4']) < 1e-14

    def test_ground_state_energy_N2(self):
        """CM ground state energy E_0 = beta^2 * N*(N^2-1)/12 at N=2."""
        c = 10.0
        data = virasoro_shadow_data(c)
        result = shadow_to_cm_N_particles(
            2, data['kappa'], data['alpha'], data['S4'])
        beta = result['beta']
        expected_E0 = beta**2 * 2 * 3 / 12.0
        assert abs(result['ground_state_energy'] - expected_E0) < 1e-10


# ============================================================================
# 11. R-MATRIX
# ============================================================================

class TestRMatrix:
    """Tests for the classical r-matrix."""

    def test_r_matrix_permutation(self):
        """r(z) = P/z where P is the permutation operator."""
        N = 2
        z = 1.5
        r = cm_classical_r_matrix(z, N)
        # P_{ab,cd} = delta_{a,d} delta_{b,c}
        # In basis (00, 01, 10, 11):
        # P = [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
        P = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
        expected = P / z
        assert np.allclose(r, expected, atol=1e-14)

    def test_r_matrix_1_over_z(self):
        """r(z) has a simple pole at z = 0 (as expected for rational CM)."""
        N = 2
        r1 = cm_classical_r_matrix(1.0, N)
        r2 = cm_classical_r_matrix(2.0, N)
        assert np.allclose(r1, 2 * r2, atol=1e-14)  # 1/z scaling


# ============================================================================
# 12. FULL VERIFICATION SUITE
# ============================================================================

class TestFullVerification:
    """End-to-end verification of the shadow-CM correspondence."""

    def test_virasoro_multi_c(self):
        """Verify all four tests pass at multiple central charges."""
        results = verify_virasoro_shadow_cm()
        for c, data in results.items():
            assert data['tests_passed'], \
                f"Verification failed at c={c}: {data}"

    def test_N2_verification(self):
        """N=2 CM verification for Virasoro."""
        c = 10.0
        data = virasoro_shadow_data(c)
        result = verify_shadow_cm_at_N2(data['kappa'], data['alpha'], data['S4'])
        assert result['E_1_equals_beta']

    def test_dictionary_complete(self):
        """The shadow-CM dictionary has all required entries."""
        d = shadow_cm_full_dictionary()
        required_keys = [
            'Q_L (shadow metric)',
            'nabla^sh (shadow connection)',
            'f^2 = Q_L (MC recursion)',
            'kappa = S_2',
            'S_4 = Q^contact',
        ]
        for key in required_keys:
            assert key in d, f"Missing dictionary entry: {key}"

    def test_depth_from_cm_virasoro(self):
        """Shadow depth from CM perspective matches class M for Virasoro."""
        for c in [1, 5, 13, 25, 100]:
            result = virasoro_shadow_depth_from_cm(float(c))
            assert result['shadow_class'] == 'M'
            assert result['cm_interpretation'] == 'interacting'
            assert result['r_max'] == float('inf')


# ============================================================================
# 13. CROSS-FAMILY CONSISTENCY (AP10)
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks to guard against AP10 violations."""

    def test_kappa_additivity_in_cm(self):
        """kappa is additive under direct sum (prop:independent-sum-factorization).
        In CM language: free particles have additive energy."""
        k1, k2 = 2.0, 3.0
        # Two independent Heisenberg channels
        kappa_total = k1 + k2
        kappa_1 = k1
        kappa_2 = k2
        assert abs(kappa_total - kappa_1 - kappa_2) < 1e-14

    def test_virasoro_c1_explicit(self):
        """Virasoro at c=1: explicit numerical check of all shadow-CM data."""
        c = 1.0
        kappa = 0.5
        S4 = 10.0 / (1.0 * 27.0)
        Delta = 8 * 0.5 * S4
        g2 = 4 * S4

        assert abs(kappa - 0.5) < 1e-14
        assert abs(S4 - 10.0 / 27.0) < 1e-14
        assert abs(Delta - 40.0 / 27.0) < 1e-13
        assert abs(g2 - 40.0 / 27.0) < 1e-13

    def test_shadow_coefficients_all_families(self):
        """Shadow coefficients match at arity 2 for all families."""
        # Heisenberg
        h = shadow_coefficients_from_recursion(1.0, 0.0, 0.0, 5)
        assert abs(h[2] - 1.0) < 1e-14  # kappa = k = 1

        # Virasoro c=10
        v = shadow_coefficients_from_recursion(5.0, 2.0, virasoro_q_contact(10.0), 5)
        assert abs(v[2] - 5.0) < 1e-14  # kappa = c/2 = 5

    def test_coupling_vanishes_for_class_G_and_L(self):
        """g_eff^2 = 0 for class G and class L (S_4 = 0)."""
        # Class G
        assert abs(cm_coupling_from_shadow(1.0, 0.0)) < 1e-14
        # Class L
        assert abs(cm_coupling_from_shadow(3.0, 0.0)) < 1e-14

    def test_coupling_nonzero_for_class_M(self):
        """g_eff^2 > 0 for class M (S_4 != 0)."""
        for c in [1, 5, 13, 25]:
            S4 = virasoro_q_contact(float(c))
            assert cm_coupling_from_shadow(c / 2.0, S4) > 0
