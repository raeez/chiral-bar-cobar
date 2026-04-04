r"""Tests for KZ conformal blocks engine.

Verifies:
  1. Representation theory data (dimensions, central charges, characters)
  2. 4-point conformal blocks (hypergeometric solutions, KZ ODE verification)
  3. Monodromy representation (braiding eigenvalues, braid relations, F-matrix)
  4. Genus-1 KZB connection (E_2, Hitchin, characters)
  5. Quantum KZ (trigonometric R-matrix, QYBE, shift equations)
  6. WZNW partition function (Verlinde formula, modular invariance)
  7. sl_3 KZ (Casimir, IBR, connection)
  8. Comparison tables (cross-level, cross-rank)

All tests are computed from first principles.  Hardcoded expected values
are independently verified.  Cross-family consistency checks (AP10)
are preferred over single-point tests.

References:
  Knizhnik-Zamolodchikov, Nucl. Phys. B 247 (1984) 83-103
  Etingof-Frenkel-Kirillov, Lectures on Rep. Theory and KZ Equations
  thm:yangian-shadow-theorem (concordance.tex)
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np
import pytest

from compute.lib.kz_conformal_blocks import (
    _hypergeometric_2f1,
    _pochhammer,
    braiding_eigenvalues_sl2,
    comparison_table,
    eisenstein_e2,
    four_point_hypergeometric_params,
    kz_4point_conformal_blocks,
    kz_4point_solutions_fundamental,
    kz_parameter,
    kzb_connection_1point,
    kzb_npoint_connection,
    monodromy_around_one,
    monodromy_around_zero,
    monodromy_matrices_4point,
    qkz_shift_equation,
    shadow_kz_identification_table,
    sl2_central_charge,
    sl2_character,
    sl2_conformal_dimension,
    sl2_fusion_rules,
    sl2_integrable_reps,
    sl2_kappa_km,
    sl2_modular_s_matrix,
    sl3_casimir_eigenvalues,
    sl3_casimir_fundamental,
    sl3_generators_fundamental,
    sl3_kz_connection,
    sl3_verify_ibr,
    trigonometric_r_matrix_sl2,
    verify_character_kzb,
    verify_kz_ode_4point,
    verify_qybe_trigonometric,
    weierstrass_p,
    wznw_dimension_of_blocks,
    wznw_genus1_partition,
    wznw_partition_function,
)


# =========================================================================
# 1. Representation theory data
# =========================================================================

class TestRepresentationTheory:
    """Tests for sl_2 WZW representation theory data."""

    def test_conformal_dimension_vacuum(self):
        """Delta_0 = 0 for the vacuum at any level."""
        for k in [1, 2, 3, 4, 10]:
            assert abs(sl2_conformal_dimension(0, k)) < 1e-15

    def test_conformal_dimension_fundamental(self):
        """Delta_{1/2} = 3/(4(k+2)) for the fundamental."""
        for k in [1, 2, 3, 4]:
            expected = 3.0 / (4.0 * (k + 2))
            assert abs(sl2_conformal_dimension(0.5, k) - expected) < 1e-15

    def test_conformal_dimension_adjoint(self):
        """Delta_1 = 2/(k+2) for the adjoint."""
        for k in [2, 3, 4, 5]:
            expected = 2.0 / (k + 2)
            assert abs(sl2_conformal_dimension(1, k) - expected) < 1e-15

    def test_central_charge_values(self):
        """c(sl_2, k) = 3k/(k+2): known values at small k."""
        assert abs(sl2_central_charge(1) - 1.0) < 1e-14        # c = 1
        assert abs(sl2_central_charge(2) - 1.5) < 1e-14        # c = 3/2
        assert abs(sl2_central_charge(4) - 2.0) < 1e-14        # c = 2
        assert abs(sl2_central_charge(10) - 2.5) < 1e-14       # c = 5/2

    def test_central_charge_monotone(self):
        """c(k) is strictly increasing and bounded by 3."""
        c_prev = 0
        for k in range(1, 20):
            c_k = sl2_central_charge(k)
            assert c_k > c_prev
            assert c_k < 3.0
            c_prev = c_k

    def test_kappa_km_formula(self):
        """kappa(KM) = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4."""
        for k in [1, 2, 3, 4, 5]:
            expected = 3.0 * (k + 2) / 4.0
            assert abs(sl2_kappa_km(k) - expected) < 1e-14

    def test_kappa_not_c_over_2(self):
        """kappa(KM) is NOT c/2 in general (AP20)."""
        for k in [1, 2, 3, 4]:
            kappa = sl2_kappa_km(k)
            c_half = sl2_central_charge(k) / 2.0
            # These should be DIFFERENT:
            assert abs(kappa - c_half) > 0.1

    def test_integrable_reps(self):
        """Number of integrable reps at level k is k+1."""
        for k in [1, 2, 3, 4, 5]:
            reps = sl2_integrable_reps(k)
            assert len(reps) == k + 1
            assert reps[0] == 0.0
            assert reps[-1] == k / 2.0

    def test_kz_parameter(self):
        """h = 1/(k+h^v) for various Lie types."""
        assert abs(kz_parameter(1, 'sl2') - 1.0/3) < 1e-14
        assert abs(kz_parameter(2, 'sl2') - 0.25) < 1e-14
        assert abs(kz_parameter(1, 'sl3') - 0.25) < 1e-14


# =========================================================================
# 2. Modular S-matrix and fusion rules
# =========================================================================

class TestSMatrixFusion:
    """Tests for the modular S-matrix and Verlinde fusion rules."""

    def test_s_matrix_unitarity(self):
        """S is unitary: S S^dagger = Id."""
        for k in [1, 2, 3, 4]:
            S = sl2_modular_s_matrix(k)
            SSdag = S @ S.T  # S is real for sl_2
            eye = np.eye(k + 1)
            assert np.max(np.abs(SSdag - eye)) < 1e-12

    def test_s_matrix_symmetry(self):
        """S is symmetric: S_{l1, l2} = S_{l2, l1}."""
        for k in [1, 2, 3, 4]:
            S = sl2_modular_s_matrix(k)
            assert np.max(np.abs(S - S.T)) < 1e-14

    def test_s_matrix_involution(self):
        """S^2 = Id for sl_2 (all representations are self-conjugate).

        For sl_2, the charge conjugation matrix C_{l, l'} = delta_{l, k-l}
        equals the identity because the S-matrix satisfies S_{l, k-l} = S_{l, l}
        (self-conjugacy of SU(2) representations).  Hence S^2 = C = Id.
        """
        for k in [1, 2, 3, 4]:
            S = sl2_modular_s_matrix(k)
            S2 = S @ S
            eye = np.eye(k + 1)
            assert np.max(np.abs(S2 - eye)) < 1e-12

    def test_fusion_rules_k1(self):
        """At k=1: 1 x 1 = 0 (only the singlet channel)."""
        N = sl2_fusion_rules(1)
        assert N[1, 1, 0] == 1
        # No triplet (l=2 does not exist at k=1)
        assert N.shape == (2, 2, 2)

    def test_fusion_rules_k2(self):
        """At k=2: 1 x 1 = 0 + 2."""
        N = sl2_fusion_rules(2)
        assert N[1, 1, 0] == 1
        assert N[1, 1, 2] == 1

    def test_fusion_associativity(self):
        """Fusion is associative: sum_m N_{ab}^m N_{mc}^d = sum_m N_{ac}^m N_{bm}^d."""
        for k in [2, 3, 4]:
            N = sl2_fusion_rules(k)
            n = k + 1
            for a, b, c, d in [(1, 1, 1, 1), (0, 1, 1, 0), (1, 2, 1, 0)]:
                if max(a, b, c, d) >= n:
                    continue
                lhs = sum(N[a, b, m] * N[m, c, d] for m in range(n))
                rhs = sum(N[a, c, m] * N[b, m, d] for m in range(n))
                assert abs(lhs - rhs) < 0.5  # integer, so this is exact

    def test_vacuum_is_identity(self):
        """N_{0, l}^m = delta_{l,m}: vacuum is the fusion identity."""
        for k in [1, 2, 3, 4]:
            N = sl2_fusion_rules(k)
            for l in range(k + 1):
                for m in range(k + 1):
                    expected = 1 if l == m else 0
                    assert N[0, l, m] == expected


# =========================================================================
# 3. Hypergeometric utility
# =========================================================================

class TestHypergeometric:
    """Tests for the _2F_1 implementation."""

    def test_2f1_at_zero(self):
        """_2F_1(a, b; c; 0) = 1 for any a, b, c."""
        assert abs(_hypergeometric_2f1(0.5, 1.0, 1.5, 0.0) - 1.0) < 1e-14

    def test_2f1_geometric(self):
        """_2F_1(1, 1; 1; z) = 1/(1-z) for |z| < 1 (geometric series)."""
        for z in [0.1, 0.3, 0.5, 0.7, 0.9]:
            computed = _hypergeometric_2f1(1, 1, 1, z, n_terms=500)
            expected = 1.0 / (1 - z)
            # Slow convergence near z=1, so allow some tolerance
            assert abs(computed - expected) / abs(expected) < 1e-4

    def test_2f1_log(self):
        """_2F_1(1, 1; 2; z) = -log(1-z)/z."""
        for z in [0.1, 0.3, 0.5]:
            computed = _hypergeometric_2f1(1, 1, 2, z)
            expected = -np.log(1 - z) / z
            assert abs(computed - expected) < 1e-10

    def test_2f1_gauss_evaluation(self):
        """Gauss's formula: _2F_1(a, b; c; 1) = Gamma(c)Gamma(c-a-b)/(Gamma(c-a)Gamma(c-b))
        when Re(c-a-b) > 0."""
        a, b, c = 0.3, 0.4, 1.5
        from scipy.special import gamma
        expected = gamma(c) * gamma(c - a - b) / (gamma(c - a) * gamma(c - b))
        computed = _hypergeometric_2f1(a, b, c, 0.999, n_terms=500)
        assert abs(computed - expected) / abs(expected) < 1e-2

    def test_pochhammer_values(self):
        """Pochhammer (a)_n = a(a+1)...(a+n-1)."""
        assert abs(_pochhammer(1, 0) - 1) < 1e-14
        assert abs(_pochhammer(1, 3) - 6) < 1e-14  # 1*2*3
        assert abs(_pochhammer(0.5, 2) - 0.75) < 1e-14  # 0.5 * 1.5


# =========================================================================
# 4. Four-point conformal blocks
# =========================================================================

class TestFourPointBlocks:
    """Tests for 4-point KZ conformal blocks for sl_2 fundamental."""

    def test_hypergeometric_params_all_fundamental(self):
        """Verify hypergeometric parameters for all-fundamental external."""
        for k in [1, 2, 3, 4]:
            params = four_point_hypergeometric_params(
                (0.5, 0.5, 0.5, 0.5), 0.0, k)
            h = 1.0 / (k + 2)
            assert params['all_fundamental']
            assert abs(params['a'] - (-h)) < 1e-14
            assert abs(params['b'] - (1 - h)) < 1e-14
            assert abs(params['c'] - (1 - 2*h)) < 1e-14

    def test_solutions_at_small_z(self):
        """f_singlet(z) -> 1 and f_triplet(z) -> z^{2h} as z -> 0."""
        for k in [1, 2, 3, 4]:
            z = 0.001
            sol = kz_4point_solutions_fundamental(k, z)
            h = 1.0 / (k + 2)
            # f_singlet(z) ~ 1 + O(z)
            assert abs(sol['f_singlet'] - 1.0) < 0.01
            # f_triplet(z) ~ z^{2h}
            expected = z ** (2 * h)
            assert abs(sol['f_triplet'] / expected - 1.0) < 0.01

    def test_solutions_nonzero(self):
        """Both solutions are nonzero at generic z."""
        for k in [1, 2, 3, 4]:
            sol = kz_4point_solutions_fundamental(k, 0.3)
            assert abs(sol['f_singlet']) > 1e-10
            assert abs(sol['f_triplet']) > 1e-10

    def test_kz_ode_singlet(self):
        """The singlet solution satisfies the hypergeometric ODE."""
        for k in [2, 3, 4]:
            result = verify_kz_ode_4point(k, 0.3 + 0.1j, eps=1e-5)
            assert result['singlet']['satisfies_ode'], (
                f"k={k}: singlet residual = {result['singlet']['abs_residual']}")

    def test_linear_independence(self):
        """The two solutions are linearly independent (nonzero Wronskian)."""
        for k in [2, 3, 4]:
            z_vals = [0.2 + 0.1j, 0.4 + 0.05j, 0.6 - 0.1j]
            result = kz_4point_conformal_blocks(k, z_vals)
            assert result['linearly_independent']

    def test_solutions_real_on_real_axis(self):
        """Solutions are real for real z in (0, 1)."""
        for k in [2, 3, 4]:
            sol = kz_4point_solutions_fundamental(k, 0.4)
            assert abs(sol['f_singlet'].imag) < 1e-12
            assert abs(sol['f_triplet'].imag) < 1e-12


# =========================================================================
# 5. Braiding and monodromy
# =========================================================================

class TestBraidingMonodromy:
    """Tests for braiding eigenvalues and monodromy matrices."""

    def test_braiding_eigenvalue_ratio(self):
        """R_triplet / R_singlet = -q^2 where q = exp(pi i/(k+2))."""
        for k in [1, 2, 3, 4, 5]:
            eigs = braiding_eigenvalues_sl2(k)
            q = eigs['q']
            expected_ratio = -q**2
            assert abs(eigs['R_ratio'] - expected_ratio) < 1e-12

    def test_braiding_eigenvalues_k1(self):
        """At k=1: R_0 = -exp(-pi i/2), R_1 = exp(pi i/6)."""
        eigs = braiding_eigenvalues_sl2(1)
        # R_0 = -exp(-3 pi i / (2*3)) = -exp(-pi i / 2) = -(-i) = i...
        # Actually: -exp(-3*pi*i/6) = -exp(-pi*i/2) = -(cos(-pi/2)+i*sin(-pi/2)) = -(0-i) = i
        R0_expected = -np.exp(-3j * np.pi / 6)
        R1_expected = np.exp(1j * np.pi / 6)
        assert abs(eigs['R_singlet'] - R0_expected) < 1e-12
        assert abs(eigs['R_triplet'] - R1_expected) < 1e-12

    def test_braiding_eigenvalues_k2(self):
        """At k=2: q = exp(pi i / 4)."""
        eigs = braiding_eigenvalues_sl2(2)
        q = np.exp(1j * np.pi / 4)
        assert abs(eigs['q'] - q) < 1e-12

    def test_R_singlet_includes_sign(self):
        """R_singlet = -q^{-3/2}: includes (-1) sign from antisymmetric CG coupling."""
        for k in [1, 2, 3, 4]:
            eigs = braiding_eigenvalues_sl2(k)
            q = eigs['q']
            # R_singlet = -q^{-3/2}
            expected = -q**(-1.5)
            assert abs(eigs['R_singlet'] - expected) < 1e-12

    def test_R_triplet_no_sign(self):
        """R_triplet = q^{1/2}: no sign for symmetric CG coupling."""
        for k in [1, 2, 3, 4]:
            eigs = braiding_eigenvalues_sl2(k)
            q = eigs['q']
            expected = q**0.5
            assert abs(eigs['R_triplet'] - expected) < 1e-12

    def test_monodromy_4point_exists(self):
        """Monodromy computation completes for k = 1, 2, 3, 4."""
        for k in [1, 2, 3, 4]:
            data = monodromy_matrices_4point(k)
            assert data['block_dim'] >= 1

    def test_braid_relation_4point(self):
        """B_s B_t B_s = B_t B_s B_t for k >= 2 (2-dimensional block space)."""
        for k in [2, 3, 4]:
            data = monodromy_matrices_4point(k)
            assert data['block_dim'] == 2
            assert data['braid_relation_holds'], (
                f"k={k}: braid error = {data['braid_relation_error']}")

    def test_monodromy_zero_diagonal(self):
        """Monodromy around z=0 is diagonal in the s-channel basis."""
        for k in [1, 2, 3, 4]:
            data = monodromy_around_zero(k)
            assert data['is_diagonal']
            assert abs(data['eigenvalues'][0] - 1.0) < 1e-12

    def test_monodromy_zero_triplet_phase(self):
        """Monodromy phase for triplet: e^{4 pi i / (k+2)}."""
        for k in [1, 2, 3, 4]:
            data = monodromy_around_zero(k)
            expected = np.exp(4j * np.pi / (k + 2))
            assert abs(data['triplet_phase'] - expected) < 1e-12

    def test_f_matrix_unitarity(self):
        """The F-matrix (fusion matrix) is unitary for k >= 2."""
        for k in [2, 3, 4, 5]:
            data = monodromy_matrices_4point(k)
            F = data['F_matrix']
            FdagF = np.conj(F.T) @ F
            eye = np.eye(F.shape[0])
            assert np.max(np.abs(FdagF - eye)) < 1e-10


# =========================================================================
# 6. Genus-1 KZB
# =========================================================================

class TestKZB:
    """Tests for the KZB connection and genus-1 blocks."""

    def test_eisenstein_e2_basic(self):
        """E_2(i) is a known value: E_2(i) = 3/pi (approximately)."""
        tau = 1j  # tau = i (square torus)
        E2 = eisenstein_e2(tau, n_terms=200)
        # E_2(i) = 3/pi = 0.9549...
        expected = 3.0 / np.pi
        assert abs(E2 - expected) < 0.01

    def test_eisenstein_e2_q_expansion(self):
        """E_2 starts with 1 - 24q for small q."""
        tau = 2j  # large Im(tau), small q
        q = np.exp(-4 * np.pi)  # very small
        E2 = eisenstein_e2(tau, n_terms=10)
        # E_2 ~ 1 - 24q + O(q^2), and q ~ 3.5e-6, so E_2 ~ 1
        assert abs(E2 - 1.0) < 1e-4

    def test_kzb_connection_returns_data(self):
        """KZB connection computation returns expected fields."""
        result = kzb_connection_1point(1, 0.5j + 0.3)
        assert 'E2' in result
        assert 'kzb_coefficient' in result
        assert 'kappa_km' in result
        assert result['genus'] == 1

    def test_kzb_kappa_vs_shadow(self):
        """KZB and shadow connection use the same kappa at genus 1."""
        for k in [1, 2, 3, 4]:
            result = kzb_connection_1point(k, 1j)
            # The shadow connection at genus 1 uses kappa_km
            assert abs(result['kappa_km'] - sl2_kappa_km(k)) < 1e-12

    def test_kzb_npoint_returns_wp(self):
        """KZB n-point connection involves Weierstrass p."""
        z_pts = [0.1 + 0.2j, 0.4 + 0.1j]
        result = kzb_npoint_connection(1, z_pts, 1j)
        assert len(result['A_scalars']) == 2
        assert result['genus'] == 1

    def test_weierstrass_p_pole(self):
        """wp(z) ~ 1/z^2 near z = 0."""
        tau = 1j
        z = 0.001 + 0.001j
        wp_val = weierstrass_p(z, tau, n_terms=3)
        expected = 1.0 / z**2
        assert abs(wp_val / expected - 1.0) < 0.1

    def test_character_vacuum_leading(self):
        """chi_0(tau) ~ q^{-c/24} (1 + O(q)) at large Im(tau).

        For the vacuum module (l=0), Delta_0 = 0, so the leading term is
        q^{-c/24}.  The ratio chi_0 / q^{-c/24} -> 1 as Im(tau) -> infty.
        """
        for k in [1, 2, 3]:
            tau = 3j  # large imaginary part
            chi = sl2_character(0, k, tau, n_terms=30)
            c = sl2_central_charge(k)
            q = np.exp(2j * np.pi * tau)
            expected_leading = q ** (-c / 24)
            ratio = chi / expected_leading
            # At Im(tau) = 3, q is very small, so ratio ~ 1
            assert abs(ratio - 1.0) < 0.01, (
                f"k={k}: ratio = {ratio}, expected ~ 1")

    def test_character_kzb_leading_order(self):
        """q d/dq chi_l ~ (Delta_l - c/24) chi_l at leading order."""
        for k in [1, 2, 3]:
            result = verify_character_kzb(k, 0, 3j, eps=1e-5)
            expected = result['expected_ratio']
            if abs(result['chi']) > 1e-10:
                assert abs(result['ratio'] - expected) / max(abs(expected), 1e-10) < 0.01


# =========================================================================
# 7. Quantum KZ
# =========================================================================

class TestQuantumKZ:
    """Tests for quantum KZ equations and trigonometric R-matrices."""

    def test_r_matrix_invertible(self):
        """The trigonometric R-matrix is invertible at generic u."""
        for k in [1, 2, 3, 4]:
            u = 0.5 + 0.2j
            R = trigonometric_r_matrix_sl2(u, k)
            det = np.linalg.det(R)
            assert abs(det) > 1e-10

    def test_r_matrix_initial_condition(self):
        """R(0) = sin(eta) * P (proportional to permutation).

        At u = 0: a(0) = sin(eta), b(0) = 0, c = sin(eta).
        So R(0) = sin(eta) * [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]] = sin(eta) * P.
        """
        for k in [2, 3, 4]:
            eta = np.pi / (k + 2)
            R = trigonometric_r_matrix_sl2(0, k)
            P = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)
            assert np.max(np.abs(R - np.sin(eta) * P)) < 1e-12

    def test_qybe_k1(self):
        """QYBE holds for k=1."""
        result = verify_qybe_trigonometric(1, 0.3 + 0.1j, 0.7 - 0.2j)
        assert result['qybe_satisfied'], f"QYBE error: {result['qybe_error']}"

    def test_qybe_k2(self):
        """QYBE holds for k=2."""
        result = verify_qybe_trigonometric(2, 0.4 + 0.15j, 0.8 - 0.1j)
        assert result['qybe_satisfied'], f"QYBE error: {result['qybe_error']}"

    def test_qybe_k3(self):
        """QYBE holds for k=3."""
        result = verify_qybe_trigonometric(3, 0.2 + 0.3j, 0.6 - 0.4j)
        assert result['qybe_satisfied'], f"QYBE error: {result['qybe_error']}"

    def test_qybe_k4(self):
        """QYBE holds for k=4."""
        result = verify_qybe_trigonometric(4, 0.5, 1.0)
        assert result['qybe_satisfied'], f"QYBE error: {result['qybe_error']}"

    def test_qybe_multiple_spectral_params(self):
        """QYBE holds at multiple random spectral parameter values."""
        rng = np.random.RandomState(42)
        for k in [2, 3]:
            for _ in range(5):
                u = rng.randn() + 1j * rng.randn()
                v = rng.randn() + 1j * rng.randn()
                result = verify_qybe_trigonometric(k, u, v)
                assert result['qybe_satisfied'], (
                    f"k={k}, u={u}, v={v}: error={result['qybe_error']}")

    def test_r_matrix_p_symmetry(self):
        """P R(u) P = R(u): the R-matrix is symmetric under P conjugation.

        Our R-matrix has the form [[a,0,0,0],[0,b,c,0],[0,c,b,0],[0,0,0,a]]
        which is symmetric under the permutation P, since swapping the two
        tensor factors leaves the matrix invariant.
        """
        P = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)
        for k in [2, 3]:
            u = 0.5 + 0.3j
            R = trigonometric_r_matrix_sl2(u, k)
            PRP = P @ R @ P
            assert np.max(np.abs(PRP - R)) < 1e-10

    def test_qkz_shift_returns_matrix(self):
        """qKZ shift equation returns a transport matrix."""
        z_pts = [1.0 + 0.5j, 2.0 - 0.3j]
        result = qkz_shift_equation(2, z_pts, 0)
        T = result['transport_matrix']
        assert T.shape == (4, 4)
        assert abs(np.linalg.det(T)) > 1e-10


# =========================================================================
# 8. WZNW partition function
# =========================================================================

class TestWZNWPartition:
    """Tests for the WZNW partition function."""

    def test_genus0_is_one(self):
        """Z(Sigma_0) = 1 (sphere partition function)."""
        for k in [1, 2, 3, 4]:
            Z = wznw_partition_function(k, 0)
            assert abs(Z['Z_WZNW'] - 1.0) < 1e-12

    def test_genus1_dimension(self):
        """dim V(Sigma_1) = k+1 (number of integrable reps)."""
        for k in [1, 2, 3, 4, 5]:
            Z = wznw_partition_function(k, 1)
            assert abs(Z['Z_WZNW'] - (k + 1)) < 1e-12

    def test_genus2_positive(self):
        """Z(Sigma_2) > 0 for all k >= 1."""
        for k in [1, 2, 3, 4, 5]:
            Z = wznw_partition_function(k, 2)
            assert Z['Z_WZNW'] > 0

    def test_genus2_k1(self):
        """Z(Sigma_2, sl_2, k=1) = S_{00}^{-2} + S_{01}^{-2}.

        S_{00} = sqrt(2/3) sin(pi/3) = sqrt(2/3) * sqrt(3)/2 = sqrt(1/2) = 1/sqrt(2)
        S_{01} = sqrt(2/3) sin(2*pi/3) = sqrt(2/3) * sqrt(3)/2 = 1/sqrt(2)

        So Z = 2 + 2 = 4.  Wait, let me recompute.

        S = sqrt(2/3) * [[sin(pi/3), sin(2pi/3)], [sin(2pi/3), sin(4pi/3)]]
          = sqrt(2/3) * [[sqrt(3)/2, sqrt(3)/2], [sqrt(3)/2, -sqrt(3)/2]]

        S_{00} = sqrt(2/3) * sqrt(3)/2 = sqrt(6)/2 / sqrt(3) = 1/sqrt(2)...
        Let me just compute: sqrt(2/3) * sin(pi/3) = sqrt(2/3) * sqrt(3)/2 = sqrt(2)*sqrt(3)/(2*sqrt(3)) = sqrt(2)/2
        Hmm: sqrt(2/3) = sqrt(2)/sqrt(3). And sin(pi/3) = sqrt(3)/2.
        So S_{00} = sqrt(2)/sqrt(3) * sqrt(3)/2 = sqrt(2)/2 = 1/sqrt(2).
        And S_{01} = sqrt(2)/sqrt(3) * sin(2*pi/3) = sqrt(2)/sqrt(3) * sqrt(3)/2 = 1/sqrt(2).

        Z(g=2) = S_{00}^{-2} + S_{01}^{-2} = 2 + 2 = 4.
        """
        Z = wznw_partition_function(1, 2)
        assert abs(Z['Z_WZNW'] - 4.0) < 1e-10

    def test_genus3_k1(self):
        """Z(Sigma_3, sl_2, k=1) = S_{00}^{-4} + S_{01}^{-4} = 4 + 4 = 8."""
        Z = wznw_partition_function(1, 3)
        assert abs(Z['Z_WZNW'] - 8.0) < 1e-10

    def test_verlinde_block_dimension(self):
        """dim V(Sigma_0, 4pt fundamental) matches Verlinde formula."""
        for k in [2, 3, 4]:
            dim = wznw_dimension_of_blocks(k, 0, 4, [1, 1, 1, 1])
            # For k >= 2: dim = 2 (singlet + triplet channels)
            assert dim == 2

    def test_verlinde_3point(self):
        """dim V(Sigma_0, 3pt) = N_{l1, l2, l3} (fusion coefficient)."""
        for k in [2, 3]:
            # 3 fundamentals: N_{1,1,0} = 1
            dim = wznw_dimension_of_blocks(k, 0, 3, [1, 1, 0])
            assert dim == 1
            # 3 fundamentals: N_{1,1,2} = 1
            dim = wznw_dimension_of_blocks(k, 0, 3, [1, 1, 2])
            assert dim == 1

    def test_genus1_partition_modular(self):
        """Z(tau) is approximately constant under tau -> tau + 1."""
        k = 1
        tau = 0.3 + 1j
        Z1 = wznw_genus1_partition(k, tau, n_terms=30)['Z']
        Z2 = wznw_genus1_partition(k, tau + 1, n_terms=30)['Z']
        # Z should be modular invariant: Z(tau + 1) = Z(tau)
        assert abs(Z1 - Z2) / max(abs(Z1), 1e-10) < 0.01


# =========================================================================
# 9. sl_3 KZ equations
# =========================================================================

class TestSL3KZ:
    """Tests for sl_3 KZ equations."""

    def test_sl3_generators_commutation(self):
        """Verify [E_1, F_1] = H_1 and [E_1, E_2] = E_3."""
        gens = sl3_generators_fundamental()
        # [E1, F1] = H1
        comm_EF = gens['E1'] @ gens['F1'] - gens['F1'] @ gens['E1']
        assert np.max(np.abs(comm_EF - gens['H1'])) < 1e-14

        # [E1, E2] = E3
        comm_EE = gens['E1'] @ gens['E2'] - gens['E2'] @ gens['E1']
        assert np.max(np.abs(comm_EE - gens['E3'])) < 1e-14

    def test_sl3_generators_traceless(self):
        """All generators are traceless."""
        gens = sl3_generators_fundamental()
        for name, g in gens.items():
            assert abs(np.trace(g)) < 1e-14, f"{name} not traceless"

    def test_sl3_casimir_eigenvalues(self):
        """Omega eigenvalues on C^3 x C^3: 2/3 (dim 6, Sym^2) and -4/3 (dim 3, wedge^2).

        With our normalization (Killing form = trace in fundamental):
          C_2(fundamental) = 8/3
          Omega = (C_total - C_1 - C_2)/2
          On Sym^2 (dim 6): C_2 = 20/3, so Omega = (20/3 - 16/3)/2 = 2/3
          On wedge^2 (dim 3): C_2 = 8/3, so Omega = (8/3 - 16/3)/2 = -4/3
        """
        result = sl3_casimir_eigenvalues()
        eigs = result['eigenvalues']
        assert len(eigs) == 2
        eig_vals = sorted(eigs.keys())
        assert abs(eig_vals[0] - (-4.0/3)) < 1e-8
        assert abs(eig_vals[1] - (2.0/3)) < 1e-8
        assert eigs[eig_vals[0]] == 3  # antisymmetric (wedge^2)
        assert eigs[eig_vals[1]] == 6  # symmetric (sym^2)

    def test_sl3_casimir_trace(self):
        """Tr(Omega) on C^3 x C^3 = 6*(1/3) + 3*(-2/3) = 2 - 2 = 0."""
        result = sl3_casimir_eigenvalues()
        assert abs(result['Omega_trace']) < 1e-10

    def test_sl3_ibr(self):
        """Infinitesimal braid relation [Omega_{12}, Omega_{13} + Omega_{23}] = 0."""
        result = sl3_verify_ibr()
        assert result['ibr_satisfied'], f"IBR error: {result['ibr_error']}"

    def test_sl3_kz_connection_size(self):
        """KZ connection matrices have correct size for n points."""
        for n in [2, 3]:
            z_pts = [0.5 + 0.1j * i for i in range(n)]
            A_mats = sl3_kz_connection(1, z_pts)
            expected_dim = 3 ** n
            assert len(A_mats) == n
            for A in A_mats:
                assert A.shape == (expected_dim, expected_dim)

    def test_sl3_kz_sum_zero(self):
        """sum_i A_i = 0 (translation invariance of KZ)."""
        z_pts = [0.5 + 0.1j, 1.0 + 0.3j, 2.0 - 0.2j]
        A_mats = sl3_kz_connection(1, z_pts)
        A_sum = sum(A_mats)
        assert np.max(np.abs(A_sum)) < 1e-10

    def test_sl3_kz_antisymmetry(self):
        """A_i is proportional to Omega_{ij}/(z_i - z_j), which changes sign under i<->j."""
        z_pts = [0.5, 1.5]
        A_mats = sl3_kz_connection(1, z_pts)
        # For 2 points: A_1 + A_2 = 0
        assert np.max(np.abs(A_mats[0] + A_mats[1])) < 1e-10


# =========================================================================
# 10. Comparison and identification tables
# =========================================================================

class TestComparisonTables:
    """Tests for cross-level and cross-family comparison tables."""

    def test_comparison_table_completeness(self):
        """Comparison table has entries for all requested levels."""
        table = comparison_table([1, 2, 3, 4])
        assert len(table) == 4
        for entry in table:
            assert 'k' in entry
            assert 'c' in entry
            assert 'kappa_KM' in entry

    def test_comparison_table_consistency(self):
        """Cross-check: c, kappa, h are consistent across table entries."""
        table = comparison_table([1, 2, 3, 4])
        for entry in table:
            k = entry['k']
            assert abs(entry['c'] - 3.0 * k / (k + 2)) < 1e-12
            assert abs(entry['kappa_KM'] - 3.0 * (k + 2) / 4) < 1e-12
            assert abs(entry['h_KZ'] - 1.0 / (k + 2)) < 1e-12

    def test_identification_table_entries(self):
        """Shadow-KZ identification table has expected entries."""
        table = shadow_kz_identification_table()
        assert len(table) >= 5  # 4 sl_2 levels + 1 sl_3
        for entry in table:
            assert 'family' in entry
            assert 'identification' in entry
            assert 'PROVED' in entry['identification']

    def test_c_monotone_in_table(self):
        """Central charge increases with level in the table."""
        table = comparison_table([1, 2, 3, 4, 5])
        for i in range(len(table) - 1):
            assert table[i]['c'] < table[i+1]['c']

    def test_fusion_in_table(self):
        """Fusion rules 1 x 1 in the table are correct."""
        table = comparison_table([1, 2, 3])
        # k=1: 1 x 1 = 0 only
        assert table[0]['fusion_1x1'] == {0: 1}
        # k=2: 1 x 1 = 0 + 2
        assert table[1]['fusion_1x1'] == {0: 1, 2: 1}
        # k=3: 1 x 1 = 0 + 2
        assert table[2]['fusion_1x1'] == {0: 1, 2: 1}


# =========================================================================
# 11. Cross-consistency checks (AP10)
# =========================================================================

class TestCrossConsistency:
    """Cross-family and cross-level consistency tests (AP10 safeguard)."""

    def test_c_from_kappa(self):
        """Central charge c and kappa are related but NOT by c = 2*kappa for KM."""
        for k in [1, 2, 3, 4, 5]:
            c = sl2_central_charge(k)
            kappa = sl2_kappa_km(k)
            # The relation is: c = k * dim / (k + h^v) and kappa = dim*(k+h^v)/(2*h^v)
            # So c * kappa = k * dim^2 / (2 * h^v) = k * 9 / 4
            assert abs(c * kappa - 9.0 * k / 4.0) < 1e-12

    def test_conformal_dim_from_casimir(self):
        """Delta_j = C_2(j) / (2(k+h^v)) where C_2(j) = j(j+1)*2 = 2j(j+1).

        Actually: Delta_j = j(j+1)/(k+2) and the quadratic Casimir
        eigenvalue in our normalization is C_2(V_j) = j(j+1).
        So Delta_j = C_2 / (k+h^v) = j(j+1)/(k+2).
        """
        for k in [1, 2, 3, 4]:
            for j in [0, 0.5, 1.0]:
                if j > k / 2.0:
                    continue
                Delta = sl2_conformal_dimension(j, k)
                C2 = j * (j + 1)  # Casimir eigenvalue
                expected = C2 / (k + 2)
                assert abs(Delta - expected) < 1e-14

    def test_s_matrix_verlinde_self_consistency(self):
        """Verlinde dimension of genus-0 0-point = 1 from S-matrix."""
        for k in [1, 2, 3, 4]:
            dim = wznw_dimension_of_blocks(k, 0, 0)
            assert dim == 1

    def test_braiding_and_monodromy_compatible(self):
        """Braiding eigenvalues appear as diagonal entries of B_s."""
        for k in [2, 3, 4]:
            eigs = braiding_eigenvalues_sl2(k)
            data = monodromy_matrices_4point(k)
            B_s = data['B_s_channel']
            # B_s is diagonal with the braiding eigenvalues
            assert abs(B_s[0, 0] - eigs['R_singlet']) < 1e-10
            assert abs(B_s[1, 1] - eigs['R_triplet']) < 1e-10

    def test_kz_sum_zero_sl2(self):
        """sum_i A_i = 0 for the sl_2 KZ connection (translation invariance)."""
        from compute.lib.kz_shadow_connection import kz_connection_matrix
        for k in [1, 2, 3]:
            z_pts = [0.5 + 0.1j, 1.0 + 0.3j, 2.0 - 0.2j]
            A_mats = kz_connection_matrix('sl2', Fraction(k), z_pts, rep_dim=2)
            A_sum = sum(A_mats)
            assert np.max(np.abs(A_sum)) < 1e-10

    def test_genus_tower_monotonicity(self):
        """Z(Sigma_g, k) grows with genus for fixed k."""
        for k in [1, 2, 3]:
            Z_prev = 0
            for g in [2, 3, 4, 5]:
                Z_g = wznw_partition_function(k, g)['Z_WZNW']
                assert Z_g > Z_prev, f"k={k}, g={g}: Z not monotone"
                Z_prev = Z_g

    def test_sl2_sl3_kz_parameter_ratio(self):
        """h(sl_2, k) / h(sl_3, k) = (k+3)/(k+2)."""
        for k in [1, 2, 3, 4]:
            h2 = kz_parameter(k, 'sl2')
            h3 = kz_parameter(k, 'sl3')
            expected_ratio = (k + 3.0) / (k + 2.0)
            assert abs(h2 / h3 - expected_ratio) < 1e-12


# =========================================================================
# 12. Integration with existing shadow connection code
# =========================================================================

class TestShadowIntegration:
    """Tests verifying compatibility with existing shadow connection module."""

    def test_kappa_km_matches_shadow_module(self):
        """kappa(KM) from this module matches kz_shadow_connection."""
        from compute.lib.kz_shadow_connection import casimir_element
        for k in [1, 2, 3, 4]:
            cas = casimir_element('sl2')
            h_v = cas['dual_coxeter']
            dim_g = cas['dim']
            kappa_from_shadow = dim_g * (k + h_v) / (2.0 * h_v)
            kappa_from_blocks = sl2_kappa_km(k)
            assert abs(kappa_from_shadow - kappa_from_blocks) < 1e-12

    def test_casimir_eigenvalues_match(self):
        """Casimir eigenvalues from kz_shadow_connection are twice our convention.

        The existing module uses the full Casimir: Omega eigenvalues -3/2 (singlet)
        and 1/2 (triplet).  Our braiding formulas use Delta_j - 2*Delta_ext
        which gives the same structure up to normalization.  The key point:
        both modules agree that the singlet-to-triplet ratio is 3:1.
        """
        from compute.lib.kz_shadow_connection import casimir_eigenvalue_on_VV
        result_shadow = casimir_eigenvalue_on_VV('sl2', rep_dim=2)
        eigs_shadow = result_shadow['eigenvalues']
        shadow_eigs_sorted = sorted(eigs_shadow.keys())
        # Check absolute values from existing module
        assert abs(shadow_eigs_sorted[0] - (-1.5)) < 1e-8
        assert abs(shadow_eigs_sorted[1] - 0.5) < 1e-8
        # The eigenvalue ratio matches our convention:
        # (-1.5) / 0.5 = -3, and (-3/4) / (1/4) = -3.  Consistent.
        assert abs(shadow_eigs_sorted[0] / shadow_eigs_sorted[1] + 3.0) < 1e-8

    def test_arnold_relation_consistency(self):
        """Arnold relation from kz_shadow_connection passes."""
        from compute.lib.kz_shadow_connection import arnold_relation_verify
        result = arnold_relation_verify()
        assert result['symbolic_zero']
        assert result['numerical_passes']


# =========================================================================
# 13. Edge cases and robustness
# =========================================================================

class TestEdgeCases:
    """Edge case tests for robustness."""

    def test_k1_minimal(self):
        """k=1 is the minimal level: 2 reps, c=1, smallest nontrivial model."""
        assert len(sl2_integrable_reps(1)) == 2
        assert abs(sl2_central_charge(1) - 1.0) < 1e-14

    def test_large_k_semiclassical(self):
        """At large k, c -> 3, Delta -> 0, kappa = 3(k+2)/4."""
        k = 100
        assert abs(sl2_central_charge(k) - 3.0) < 0.06
        assert abs(sl2_conformal_dimension(0.5, k)) < 0.01
        # kappa = 3(k+2)/4 exactly, not approximately 3k/4
        assert abs(sl2_kappa_km(k) - 3.0 * (k + 2) / 4.0) < 1e-10

    def test_s_matrix_large_k(self):
        """S-matrix at large k: S_{0,l} ~ sqrt(2/K) sin(pi(l+1)/K) for K=k+2."""
        k = 10
        S = sl2_modular_s_matrix(k)
        for l in range(k + 1):
            expected = np.sqrt(2.0 / (k + 2)) * np.sin(np.pi * (l + 1) / (k + 2))
            assert abs(S[0, l] - expected) < 1e-12

    def test_hypergeometric_small_z(self):
        """Solutions are well-behaved for z near 0."""
        for k in [1, 2, 3]:
            sol = kz_4point_solutions_fundamental(k, 0.001)
            assert np.isfinite(sol['f_singlet'])
            assert np.isfinite(sol['f_triplet'])

    def test_no_nans(self):
        """No NaNs appear in standard computations."""
        for k in [1, 2, 3, 4]:
            sol = kz_4point_solutions_fundamental(k, 0.3 + 0.1j)
            assert not np.isnan(sol['f_singlet'])
            assert not np.isnan(sol['f_triplet'])

            eigs = braiding_eigenvalues_sl2(k)
            assert not np.isnan(abs(eigs['R_singlet']))

            Z = wznw_partition_function(k, 2)
            assert not np.isnan(Z['Z_WZNW'])
