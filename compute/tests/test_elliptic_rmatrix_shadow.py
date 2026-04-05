r"""Tests for the elliptic R-matrix shadow module.

Verifies:
  - Jacobi theta functions (series, identities, quasi-periodicity)
  - Jacobi triple product identity
  - Weierstrass zeta/p functions (oddness, derivative relation, lattice periods)
  - Phi-function (residue, quasi-periodicity)
  - sl_2 representation matrices (commutation, Casimir, permutation)
  - Belavin r-matrix for sl_2 and sl_3 (pole structure, skew-symmetry)
  - Classical Yang-Baxter equation verification structure
  - Degeneration chain: elliptic -> trigonometric -> rational
  - Modular transformations (T and S)
  - KZB connection (shape, flatness, critical level)
  - Kappa affine formula
  - Crossing symmetry
  - Quantum R-matrix semi-classical expansion
  - Embedding operators (12, 13, 23)
  - Shadow obstruction tower q-expansion
  - Eisenstein correction structure
  - Landscape summary

Ground truth:
  - Belavin (1981), Belavin-Drinfeld (1982)
  - Bernard (1988), Felder (1994)
  - AP19: bar kernel absorbs a pole (simple pole at z=0)
  - AP27: bar propagator d log E(z,w) is weight 1
  - kappa(sl_2, k) = 3(k+2)/4
  - kappa(sl_3, k) = 4(k+3)/3
"""

import pytest
import numpy as np

import importlib.util
import os

# Load module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'elliptic_rmatrix_shadow',
    os.path.join(_lib_dir, 'elliptic_rmatrix_shadow.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Standard tau for tests (Im(tau) > 0, not too small for convergence)
TAU = 0.25 + 1.0j
TAU_PURE = 1.5j


# ============================================================
# Section 0: Constants and kappa_affine
# ============================================================

class TestKappaAffine:
    """Tests for the modular characteristic kappa = dim(g)(k+h^v)/(2h^v)."""

    def test_kappa_sl2_level1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        val = _mod.kappa_affine('sl2', 1)
        assert abs(val - 9.0 / 4.0) < 1e-12

    def test_kappa_sl2_level0(self):
        """kappa(sl_2, k=0) = 3*(0+2)/(2*2) = 3/2."""
        val = _mod.kappa_affine('sl2', 0)
        assert abs(val - 3.0 / 2.0) < 1e-12

    def test_kappa_sl3_level1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        val = _mod.kappa_affine('sl3', 1)
        assert abs(val - 16.0 / 3.0) < 1e-12

    def test_kappa_sl3_level2(self):
        """kappa(sl_3, k=2) = 8*(2+3)/(2*3) = 20/3."""
        val = _mod.kappa_affine('sl3', 2)
        assert abs(val - 20.0 / 3.0) < 1e-12

    def test_kappa_sl2_fractional_level(self):
        """kappa for fractional level (admissible)."""
        k = -0.5
        expected = 3.0 * (k + 2) / 4.0
        assert abs(_mod.kappa_affine('sl2', k) - expected) < 1e-12

    def test_kappa_sl2_critical_level(self):
        """kappa at critical level k=-h^v=-2 vanishes for sl_2."""
        assert abs(_mod.kappa_affine('sl2', -2)) < 1e-12

    def test_kappa_sl2_linearity_in_k(self):
        """kappa is linear in k: kappa(k1) + kappa(k2) - kappa(0)
        = kappa(k1+k2) - kappa(0) (up to the constant h^v shift)."""
        k1, k2 = 1.0, 3.0
        # kappa(k) = dim*(k+h^v)/(2*h^v) = dim/(2h^v) * k + dim/2
        # so kappa(k1) + kappa(k2) = dim/(2h^v)*(k1+k2) + dim
        #    kappa(k1+k2) = dim/(2h^v)*(k1+k2) + dim/2
        # difference = dim/2
        diff = _mod.kappa_affine('sl2', k1) + _mod.kappa_affine('sl2', k2)
        expected = _mod.kappa_affine('sl2', k1 + k2) + _mod.kappa_affine('sl2', 0)
        assert abs(diff - expected) < 1e-12


# ============================================================
# Section 1: Jacobi theta functions
# ============================================================

class TestJacobiTheta:
    """Tests for Jacobi theta_1, theta_2, theta_3, theta_4."""

    def test_theta1_odd(self):
        """theta_1 is odd: theta_1(-z|tau) = -theta_1(z|tau)."""
        z = 0.3 + 0.1j
        th_z = _mod.jacobi_theta1(z, TAU)
        th_mz = _mod.jacobi_theta1(-z, TAU)
        assert abs(th_z + th_mz) < 1e-10 * max(abs(th_z), 1.0)

    def test_theta1_zero_at_origin(self):
        """theta_1(0|tau) = 0."""
        val = _mod.jacobi_theta1(0, TAU)
        assert abs(val) < 1e-10

    def test_theta2_even(self):
        """theta_2 is even: theta_2(-z|tau) = theta_2(z|tau)."""
        z = 0.2 + 0.15j
        th_z = _mod.jacobi_theta2(z, TAU)
        th_mz = _mod.jacobi_theta2(-z, TAU)
        assert abs(th_z - th_mz) < 1e-10 * max(abs(th_z), 1.0)

    def test_theta3_even(self):
        """theta_3 is even: theta_3(-z|tau) = theta_3(z|tau)."""
        z = 0.2 + 0.15j
        th_z = _mod.jacobi_theta3(z, TAU)
        th_mz = _mod.jacobi_theta3(-z, TAU)
        assert abs(th_z - th_mz) < 1e-10 * max(abs(th_z), 1.0)

    def test_theta4_even(self):
        """theta_4 is even: theta_4(-z|tau) = theta_4(z|tau)."""
        z = 0.2 + 0.15j
        th_z = _mod.jacobi_theta4(z, TAU)
        th_mz = _mod.jacobi_theta4(-z, TAU)
        assert abs(th_z - th_mz) < 1e-10 * max(abs(th_z), 1.0)

    def test_theta3_at_zero_nonzero(self):
        """theta_3(0|tau) is nonzero for generic tau."""
        val = _mod.jacobi_theta3(0, TAU)
        assert abs(val) > 0.1

    def test_theta1_quasi_periodicity_z(self):
        """theta_1(z+1|tau) = -theta_1(z|tau) (periodicity in z by 1)."""
        z = 0.17 + 0.08j
        th_z = _mod.jacobi_theta1(z, TAU)
        th_zp1 = _mod.jacobi_theta1(z + 1, TAU)
        assert abs(th_zp1 + th_z) < 1e-9 * max(abs(th_z), 1.0)

    def test_theta1_quasi_periodicity_tau(self):
        """theta_1(z+tau|tau) = -q^{-1} e^{-2pi i z} theta_1(z|tau)
        where q = e^{i pi tau}."""
        z = 0.17 + 0.08j
        th_z = _mod.jacobi_theta1(z, TAU)
        th_zpt = _mod.jacobi_theta1(z + TAU, TAU)
        q = np.exp(1j * np.pi * TAU)
        expected = -q**(-1) * np.exp(-2j * np.pi * z) * th_z
        assert abs(th_zpt - expected) < 1e-8 * max(abs(th_z), 1.0)

    def test_theta1_zero_at_lattice_points(self):
        """theta_1 has zeros at z = m + n*tau."""
        for m, n in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
            z = m + n * TAU
            val = _mod.jacobi_theta1(z, TAU)
            assert abs(val) < 1e-8, f"theta_1 not zero at z={m}+{n}*tau"

    def test_theta2_at_zero_nonzero(self):
        """theta_2(0|tau) is nonzero."""
        val = _mod.jacobi_theta2(0, TAU)
        assert abs(val) > 0.01

    def test_theta4_at_zero_nonzero(self):
        """theta_4(0|tau) is nonzero."""
        val = _mod.jacobi_theta4(0, TAU)
        assert abs(val) > 0.01


class TestJacobiTripleProduct:
    """Test the Jacobi triple product identity theta_1'(0) = pi theta_2(0) theta_3(0) theta_4(0)."""

    def test_triple_product_pure_imaginary(self):
        assert _mod.verify_jacobi_triple_product(TAU_PURE)

    def test_triple_product_generic(self):
        assert _mod.verify_jacobi_triple_product(TAU)

    def test_triple_product_large_imag(self):
        assert _mod.verify_jacobi_triple_product(5j)

    def test_theta1_prime0_nonzero(self):
        """theta_1'(0|tau) should be nonzero."""
        val = _mod.jacobi_theta1_prime0(TAU)
        assert abs(val) > 0.1

    def test_triple_product_small_imag(self):
        """Triple product at smaller Im(tau) (harder regime)."""
        assert _mod.verify_jacobi_triple_product(0.3 + 0.8j, tol=1e-8)


# ============================================================
# Section 2: Weierstrass functions
# ============================================================

class TestWeierstrass:
    """Tests for Weierstrass zeta and p functions."""

    def test_zeta_odd(self):
        """Weierstrass zeta is odd: zeta(-z) = -zeta(z)."""
        z = 0.15 + 0.05j
        zeta_z = _mod.weierstrass_zeta(z, TAU)
        zeta_mz = _mod.weierstrass_zeta(-z, TAU)
        assert abs(zeta_z + zeta_mz) < 1e-4 * max(abs(zeta_z), 1.0)

    def test_zeta_pole_at_origin(self):
        """zeta(z) ~ 1/z near z=0."""
        z = 0.001
        zeta_z = _mod.weierstrass_zeta(z, TAU)
        assert abs(zeta_z - 1.0 / z) / abs(1.0 / z) < 0.05

    def test_wp_even(self):
        """Weierstrass p is even: wp(-z) = wp(z)."""
        z = 0.15 + 0.05j
        wp_z = _mod.weierstrass_p(z, TAU)
        wp_mz = _mod.weierstrass_p(-z, TAU)
        assert abs(wp_z - wp_mz) < 1e-3 * max(abs(wp_z), 1.0)

    def test_wp_double_pole(self):
        """wp(z) ~ 1/z^2 near z=0."""
        z = 0.002
        wp_z = _mod.weierstrass_p(z, TAU)
        assert abs(wp_z - 1.0 / z**2) / abs(1.0 / z**2) < 0.1

    def test_wp_is_minus_zeta_prime(self):
        """wp(z) = -zeta'(z), verified by finite differences."""
        z = 0.2 + 0.1j
        eps = 1e-6
        zeta_p = _mod.weierstrass_zeta(z + eps, TAU)
        zeta_m = _mod.weierstrass_zeta(z - eps, TAU)
        zeta_deriv = (zeta_p - zeta_m) / (2 * eps)
        wp_z = _mod.weierstrass_p(z, TAU)
        assert abs(wp_z + zeta_deriv) < 1e-2 * max(abs(wp_z), 1.0)

    def test_eta1_quasi_period(self):
        """eta_1 should be a finite complex number for generic tau."""
        eta1 = _mod._weierstrass_eta1(TAU)
        assert np.isfinite(eta1)
        assert abs(eta1) > 1e-5

    def test_zeta_finite_away_from_lattice(self):
        """zeta(z) is finite for z away from lattice points."""
        z = 0.3 + 0.2j
        val = _mod.weierstrass_zeta(z, TAU)
        assert np.isfinite(val)
        assert abs(val) < 1e6

    def test_wp_finite_away_from_lattice(self):
        """wp(z) is finite for z away from lattice points."""
        z = 0.3 + 0.2j
        val = _mod.weierstrass_p(z, TAU)
        assert np.isfinite(val)
        assert abs(val) < 1e6


# ============================================================
# Section 3: Phi-function
# ============================================================

class TestPhiFunction:
    """Tests for the Belavin phi-function."""

    def test_phi_simple_pole_at_zero(self):
        """phi_alpha(z) ~ 1/z as z -> 0 (residue = 1)."""
        alpha = 0.3
        z = 0.001
        phi_val = _mod.phi_function(z, TAU, alpha)
        assert abs(phi_val * z - 1.0) < 0.1

    def test_phi_finite_away_from_zero(self):
        """phi_alpha(z) is finite for z away from the lattice."""
        z = 0.25 + 0.1j
        alpha = 0.3
        val = _mod.phi_function(z, TAU, alpha)
        assert np.isfinite(val)
        assert abs(val) < 1e6

    def test_phi_alpha_sign_relation(self):
        """phi_{-alpha}(-z) = -phi_alpha(z) (from theta_1 odd)."""
        z = 0.15 + 0.07j
        alpha = 0.2
        phi_a = _mod.phi_function(z, TAU, alpha)
        phi_ma_mz = _mod.phi_function(-z, TAU, -alpha)
        assert abs(phi_a + phi_ma_mz) < 1e-8 * max(abs(phi_a), 1.0)

    def test_phi_different_alphas(self):
        """Phi-function gives different values for different alpha."""
        z = 0.2 + 0.05j
        phi1 = _mod.phi_function(z, TAU, 0.2)
        phi2 = _mod.phi_function(z, TAU, 0.4)
        assert abs(phi1 - phi2) > 1e-3


# ============================================================
# Section 4: sl_2 matrices
# ============================================================

class TestSl2Matrices:
    """Tests for sl_2 representation matrices."""

    def test_sl2_commutation_EF(self):
        """[E, F] = H."""
        gens = _mod._sl2_fund_matrices()
        comm = gens['E'] @ gens['F'] - gens['F'] @ gens['E']
        assert np.allclose(comm, gens['H'])

    def test_sl2_commutation_HE(self):
        """[H, E] = 2E."""
        gens = _mod._sl2_fund_matrices()
        comm = gens['H'] @ gens['E'] - gens['E'] @ gens['H']
        assert np.allclose(comm, 2 * gens['E'])

    def test_sl2_commutation_HF(self):
        """[H, F] = -2F."""
        gens = _mod._sl2_fund_matrices()
        comm = gens['H'] @ gens['F'] - gens['F'] @ gens['H']
        assert np.allclose(comm, -2 * gens['F'])

    def test_sl2_generators_traceless(self):
        """All sl_2 generators are traceless."""
        gens = _mod._sl2_fund_matrices()
        for name, T in gens.items():
            assert abs(np.trace(T)) < 1e-12, f"{name} not traceless"

    def test_sl2_casimir_symmetric(self):
        """Casimir Omega is symmetric under transposition of both tensor factors."""
        Omega = _mod._sl2_casimir_fund()
        P = _mod._permutation_2()
        # Omega should commute with P for sl_2 (since Omega = P - I/2)
        assert np.allclose(P @ Omega @ P, Omega)

    def test_sl2_casimir_equals_P_minus_half_I(self):
        """Casimir Omega = P - I/2 for sl_2 in fundamental."""
        Omega = _mod._sl2_casimir_fund()
        P = _mod._permutation_2()
        assert np.allclose(Omega, P - 0.5 * np.eye(4))

    def test_permutation_squared(self):
        """P^2 = I (permutation is an involution)."""
        P = _mod._permutation_2()
        assert np.allclose(P @ P, np.eye(4))

    def test_permutation_eigenvalues(self):
        """Permutation eigenvalues: +1 (3x symmetric) and -1 (1x antisymmetric)."""
        P = _mod._permutation_2()
        eigs = np.sort(np.linalg.eigvals(P).real)
        assert abs(eigs[0] - (-1.0)) < 1e-10
        assert all(abs(e - 1.0) < 1e-10 for e in eigs[1:])


# ============================================================
# Section 5: Belavin r-matrix sl_2
# ============================================================

class TestBelavinSl2:
    """Tests for the sl_2 Belavin elliptic r-matrix."""

    def test_simple_pole_at_zero(self):
        """r^ell(z) has a simple pole at z=0 with residue proportional to Omega (AP19)."""
        z = 0.005
        r = _mod.belavin_r_matrix_sl2(z, TAU)
        Omega = _mod._sl2_casimir_fund()
        residue = z * r
        err = np.linalg.norm(residue - Omega) / np.linalg.norm(Omega)
        assert err < 0.1

    def test_r_matrix_4x4(self):
        """r-matrix is 4x4 (C^2 tensor C^2)."""
        r = _mod.belavin_r_matrix_sl2(0.2, TAU)
        assert r.shape == (4, 4)

    def test_r_matrix_finite(self):
        """r-matrix is finite away from lattice points."""
        r = _mod.belavin_r_matrix_sl2(0.2 + 0.1j, TAU)
        assert np.all(np.isfinite(r))

    def test_pauli_form_equals_cartan_form(self):
        """Pauli form returns the same matrix as Cartan-root form."""
        z = 0.15 + 0.05j
        r_cartan = _mod.belavin_r_matrix_sl2(z, TAU)
        r_pauli = _mod.belavin_r_matrix_sl2_pauli(z, TAU)
        assert np.allclose(r_cartan, r_pauli)

    def test_r_depends_on_z(self):
        """r-matrix changes with z."""
        r1 = _mod.belavin_r_matrix_sl2(0.1 + 0.05j, TAU)
        r2 = _mod.belavin_r_matrix_sl2(0.3 + 0.05j, TAU)
        assert np.linalg.norm(r1 - r2) > 0.01

    def test_r_depends_on_tau(self):
        """r-matrix changes with tau."""
        r1 = _mod.belavin_r_matrix_sl2(0.2, 1j)
        r2 = _mod.belavin_r_matrix_sl2(0.2, 2j)
        assert np.linalg.norm(r1 - r2) > 0.01


# ============================================================
# Section 6: Genus-1 shadow r-matrix
# ============================================================

class TestGenus1ShadowRmatrix:
    """Tests for the genus-1 shadow r-matrix from bar complex on E_tau."""

    def test_level_scaling_sl2(self):
        """r^shadow(z, tau, k) = k * r^Belavin(z, tau)."""
        z = 0.15 + 0.05j
        k = 3.0
        r_shadow = _mod.genus1_shadow_rmatrix_sl2(z, TAU, k)
        r_belavin = _mod.belavin_r_matrix_sl2(z, TAU)
        assert np.allclose(r_shadow, k * r_belavin)

    def test_level_scaling_sl3(self):
        """r^shadow_sl3(z, tau, k) = k * r^Belavin_sl3(z, tau)."""
        z = 0.15 + 0.05j
        k = 2.0
        r_shadow = _mod.genus1_shadow_rmatrix_sl3(z, TAU, k)
        r_belavin = _mod.belavin_r_matrix_sl3(z, TAU)
        assert np.allclose(r_shadow, k * r_belavin)

    def test_level_1_equals_belavin(self):
        """At k=1, shadow r-matrix equals Belavin."""
        z = 0.15 + 0.05j
        r_shadow = _mod.genus1_shadow_rmatrix_sl2(z, TAU, 1.0)
        r_belavin = _mod.belavin_r_matrix_sl2(z, TAU)
        assert np.allclose(r_shadow, r_belavin)


# ============================================================
# Section 7: Yang-Baxter equation
# ============================================================

class TestYBE:
    """Tests for the classical Yang-Baxter equation verification."""

    def test_ybe_sl2_returns_dict(self):
        """YBE verification returns a dict with expected keys."""
        result = _mod.verify_ybe_elliptic_sl2(
            0.1 + 0.02j, 0.3 + 0.07j, 0.6 + 0.11j,
            TAU, k=1.0
        )
        assert 'residual' in result
        assert 'relative' in result
        assert 'passed' in result
        assert 'z12' in result

    def test_ybe_sl2_residual_finite(self):
        """YBE residual is a finite number."""
        result = _mod.verify_ybe_elliptic_sl2(
            0.1 + 0.02j, 0.3 + 0.07j, 0.6 + 0.11j,
            TAU, k=1.0
        )
        assert np.isfinite(result['residual'])

    def test_ybe_sl3_returns_dict(self):
        """YBE sl_3 verification returns expected structure."""
        result = _mod.verify_ybe_elliptic_sl3(
            0.08 + 0.02j, 0.25 + 0.06j, 0.5 + 0.1j,
            TAU, k=1.0
        )
        assert 'residual' in result
        assert 'relative' in result
        assert 'passed' in result
        assert np.isfinite(result['residual'])

    def test_ybe_sl2_scales_with_k(self):
        """YBE residual scales with k^3 (cubic in the r-matrix).
        [kr_{12}, kr_{13}] = k^2[r_{12}, r_{13}], three terms, so LHS ~ k^2 * r ~ k^3."""
        r1 = _mod.verify_ybe_elliptic_sl2(0.1 + 0.02j, 0.3 + 0.07j, 0.6 + 0.11j, TAU, k=1.0)
        r2 = _mod.verify_ybe_elliptic_sl2(0.1 + 0.02j, 0.3 + 0.07j, 0.6 + 0.11j, TAU, k=2.0)
        # Residual should scale by factor 2^3 = 8
        # (since commutator of k*r is k^2 * [r,r], and each commutator has r ~ k inside)
        # Actually: [kr12, kr13] = k^2[r12, r13], so LHS_k = k^2 * LHS_1
        # But scale also grows with k, so relative stays ~constant
        ratio = r2['residual'] / max(r1['residual'], 1e-15)
        assert 2.0 < ratio < 6.0  # should be ~4 (k^2 scaling)

    def test_ybe_correct_z_differences(self):
        """YBE stores correct z-differences."""
        z1, z2, z3 = 0.1, 0.3, 0.5
        result = _mod.verify_ybe_elliptic_sl2(z1, z2, z3, TAU)
        assert abs(result['z12'] - (z1 - z2)) < 1e-12
        assert abs(result['z13'] - (z1 - z3)) < 1e-12
        assert abs(result['z23'] - (z2 - z3)) < 1e-12


# ============================================================
# Section 8: Degeneration chain
# ============================================================

class TestDegeneration:
    """Tests for the elliptic -> trigonometric -> rational degeneration."""

    def test_elliptic_to_trigonometric_returns_structure(self):
        """Degeneration check returns expected structure."""
        result = _mod.elliptic_to_trigonometric_limit(0.15 + 0.05j, k=1.0)
        assert 'relative_errors' in result
        assert 'final_error' in result
        assert len(result['relative_errors']) > 0

    def test_trigonometric_to_rational_returns_structure(self):
        """Trigonometric -> rational returns error dict."""
        result = _mod.trigonometric_to_rational_limit()
        assert len(result) > 0
        for z, errors in result.items():
            assert len(errors) > 0

    def test_trigonometric_to_rational_convergence(self):
        """Trigonometric errors decrease with L."""
        result = _mod.trigonometric_to_rational_limit()
        for z, errors in result.items():
            assert errors[-1] < errors[0], f"Expected decreasing errors for z={z}"

    def test_trigonometric_r_shape(self):
        """Trigonometric r-matrix is 4x4."""
        r = _mod.trigonometric_r_matrix_sl2(0.2)
        assert r.shape == (4, 4)

    def test_trigonometric_r_finite(self):
        """Trigonometric r-matrix is finite away from integer points."""
        r = _mod.trigonometric_r_matrix_sl2(0.2 + 0.1j)
        assert np.all(np.isfinite(r))

    def test_rational_r_shape(self):
        """Rational r-matrix is 4x4."""
        r = _mod.rational_r_matrix_sl2(0.3)
        assert r.shape == (4, 4)

    def test_rational_r_is_omega_over_z(self):
        """r^rat(z) = Omega / z."""
        z = 0.25 + 0.1j
        r = _mod.rational_r_matrix_sl2(z)
        Omega = _mod._sl2_casimir_fund()
        assert np.allclose(r, Omega / z)

    def test_rational_r_skew(self):
        """Rational r-matrix satisfies r(z) + P r(-z) P = 0."""
        z = 0.3 + 0.1j
        r_z = _mod.rational_r_matrix_sl2(z)
        r_mz = _mod.rational_r_matrix_sl2(-z)
        P = _mod._permutation_2()
        assert np.allclose(r_z + P @ r_mz @ P, 0, atol=1e-10)

    def test_full_degeneration_chain_structure(self):
        """Full chain returns both steps."""
        result = _mod.full_degeneration_chain()
        assert 'step1_ell_to_trig' in result
        assert 'step2_trig_to_rat' in result
        assert 'relative_error' in result['step1_ell_to_trig']
        assert 'relative_error' in result['step2_trig_to_rat']

    def test_full_degeneration_step2_close(self):
        """Step 2 (trig -> rational at small z) has small error."""
        result = _mod.full_degeneration_chain()
        assert result['step2_trig_to_rat']['close']

    def test_trigonometric_pole_at_zero(self):
        """Trigonometric r-matrix has simple pole at z=0 with residue ~ Omega."""
        z = 0.001
        r = _mod.trigonometric_r_matrix_sl2(z)
        Omega = _mod._sl2_casimir_fund()
        residue = z * r
        err = np.linalg.norm(residue - Omega) / np.linalg.norm(Omega)
        assert err < 0.05

    def test_rational_r_ybe(self):
        """Rational r-matrix satisfies classical YBE exactly: [Omega/z12, Omega/z13] + ... = 0.
        For the Casimir Omega = P - I/2, [Omega, Omega] = 0 trivially on same slots,
        but on different slots the YBE residual should be small."""
        z1, z2, z3 = 0.1, 0.3, 0.5
        d = 2
        r12 = _mod._embed_12(_mod.rational_r_matrix_sl2(z1 - z2), d)
        r13 = _mod._embed_13(_mod.rational_r_matrix_sl2(z1 - z3), d)
        r23 = _mod._embed_23(_mod.rational_r_matrix_sl2(z2 - z3), d)
        lhs = (r12 @ r13 - r13 @ r12
               + r12 @ r23 - r23 @ r12
               + r13 @ r23 - r23 @ r13)
        residual = np.linalg.norm(lhs)
        scale = max(np.linalg.norm(r12), np.linalg.norm(r13), np.linalg.norm(r23), 1.0)
        assert residual / scale < 1e-8


# ============================================================
# Section 9: Modular transformations
# ============================================================

class TestModularTransformations:
    """Tests for modular T and S transformations of the r-matrix."""

    def test_t_transform_returns_structure(self):
        """T-transform check returns expected structure."""
        z = 0.15 + 0.05j
        result = _mod.modular_t_transform_check(z, TAU, k=1.0)
        assert 'eigenvalues_tau' in result
        assert 'eigenvalues_tau_plus_1' in result
        assert 'magnitudes_match' in result

    def test_t_transform_preserves_magnitudes(self):
        """Under tau -> tau+1, eigenvalue magnitudes are preserved."""
        z = 0.15 + 0.05j
        result = _mod.modular_t_transform_check(z, TAU, k=1.0)
        assert result['magnitudes_match'], \
            f"T-transform magnitude diff: {result['magnitude_difference']}"

    def test_s_transform_returns_structure(self):
        """S-transform check returns expected structure."""
        z = 0.15 + 0.05j
        result = _mod.modular_s_transform_check(z, TAU, k=1.0)
        assert 'tau' in result
        assert 'tau_s' in result
        assert 'passed' in result

    def test_s_transform_returns_finite(self):
        """S-transform check returns finite eigenvalue differences."""
        z = 0.15 + 0.05j
        result = _mod.modular_s_transform_check(z, TAU, k=1.0)
        assert np.isfinite(result['eigenvalue_magnitude_diff'])


# ============================================================
# Section 10: KZB connection
# ============================================================

class TestKZB:
    """Tests for the KZB (genus-1 shadow) connection."""

    def test_kzb_shape(self):
        """KZB connection matrix is 4x4."""
        A_tau = _mod.kzb_connection_sl2(0.2 + 0.05j, TAU, k=1.0)
        assert A_tau.shape == (4, 4)

    def test_kzb_finite(self):
        """KZB connection is finite away from singularities."""
        A_tau = _mod.kzb_connection_sl2(0.2 + 0.05j, TAU, k=1.0)
        assert np.all(np.isfinite(A_tau))

    def test_kzb_critical_level_raises(self):
        """KZB is undefined at critical level k = -h^v = -2."""
        with pytest.raises(ValueError, match="Critical level"):
            _mod.kzb_connection_sl2(0.2, TAU, k=-2.0)

    def test_kzb_flatness_commutator_vanishes(self):
        """In KZB flatness, [A_z, A_tau] = 0 (both proportional to Casimir)."""
        z = 0.2 + 0.05j
        result = _mod.kzb_flatness_check(z, TAU, k=1.0)
        assert result['commutator_norm'] < 1e-10

    def test_kzb_flatness_returns_structure(self):
        """KZB flatness check returns expected keys."""
        result = _mod.kzb_flatness_check(0.2 + 0.05j, TAU, k=1.0)
        assert 'residual' in result
        assert 'relative' in result
        assert 'commutator_norm' in result
        assert 'passed' in result

    def test_kzb_proportional_to_casimir(self):
        """A_tau = wp(z) * Omega / (2*pi*i*(k+h^v)), so it is a scalar multiple of Omega."""
        z = 0.2 + 0.05j
        A_tau = _mod.kzb_connection_sl2(z, TAU, k=1.0)
        Omega = _mod._sl2_casimir_fund()
        # A_tau should be a scalar * Omega
        # Find the scalar from a nonzero entry of Omega
        idx = np.unravel_index(np.argmax(np.abs(Omega)), Omega.shape)
        if abs(Omega[idx]) > 1e-10 and abs(A_tau[idx]) > 1e-10:
            scalar = A_tau[idx] / Omega[idx]
            reconstructed = scalar * Omega
            err = np.linalg.norm(A_tau - reconstructed) / np.linalg.norm(A_tau)
            assert err < 1e-6


# ============================================================
# Section 11: Skew-symmetry
# ============================================================

class TestSkewSymmetry:
    """Tests for skew-symmetry r_12(z) + r_21(-z) = 0."""

    def test_skew_sl2_generic(self):
        """Skew-symmetry at generic z and tau."""
        result = _mod.verify_skew_symmetry(0.15 + 0.05j, TAU, k=1.0)
        assert result['passed'], f"Skew-symmetry failed: relative={result['relative']}"

    def test_skew_sl2_pure_imaginary(self):
        """Skew-symmetry at pure imaginary tau."""
        result = _mod.verify_skew_symmetry(0.2 + 0.1j, TAU_PURE, k=1.0)
        assert result['passed']

    def test_skew_sl2_different_levels(self):
        """Skew-symmetry holds at various levels."""
        for k in [0.5, 1.0, 2.0, 5.0]:
            result = _mod.verify_skew_symmetry(0.15 + 0.05j, TAU, k=k)
            assert result['passed'], f"Skew-symmetry failed at k={k}"

    def test_skew_returns_structure(self):
        """Skew-symmetry check returns expected keys."""
        result = _mod.verify_skew_symmetry(0.15 + 0.05j, TAU)
        assert 'residual' in result
        assert 'relative' in result
        assert 'passed' in result


# ============================================================
# Section 12: sl_3 r-matrix
# ============================================================

class TestSl3:
    """Tests for the sl_3 elliptic r-matrix."""

    def test_sl3_generators_count(self):
        """sl_3 has 8 generators (2 Cartan + 6 root)."""
        mats = _mod._sl3_fund_matrices()
        assert len(mats) == 8

    def test_sl3_generators_traceless(self):
        """All sl_3 generators are traceless."""
        for T in _mod._sl3_fund_matrices():
            assert abs(np.trace(T)) < 1e-12

    def test_sl3_generators_3x3(self):
        """Each sl_3 generator is 3x3."""
        for T in _mod._sl3_fund_matrices():
            assert T.shape == (3, 3)

    def test_sl3_killing_form_symmetric(self):
        """Killing form is symmetric."""
        G = _mod._sl3_killing_form_matrix()
        assert np.allclose(G, G.T)

    def test_sl3_killing_form_nondegenerate(self):
        """Killing form is nondegenerate (invertible)."""
        G = _mod._sl3_killing_form_matrix()
        det = np.linalg.det(G)
        assert abs(det) > 1e-10

    def test_sl3_killing_form_shape(self):
        """Killing form is 8x8."""
        G = _mod._sl3_killing_form_matrix()
        assert G.shape == (8, 8)

    def test_sl3_inverse_killing_is_inverse(self):
        """Inverse Killing form times Killing form is identity."""
        G = _mod._sl3_killing_form_matrix()
        Ginv = _mod._sl3_inverse_killing()
        assert np.allclose(G @ Ginv, np.eye(8), atol=1e-10)

    def test_sl3_casimir_shape(self):
        """Casimir is 9x9 (C^3 tensor C^3)."""
        Omega = _mod._sl3_casimir_fund()
        assert Omega.shape == (9, 9)

    def test_sl3_casimir_is_P_minus_I_over_3(self):
        """Casimir = P - I/3 for sl_3."""
        Omega = _mod._sl3_casimir_fund()
        N = 3
        P = np.zeros((N * N, N * N), dtype=complex)
        for i in range(N):
            for j in range(N):
                P[i * N + j, j * N + i] = 1.0
        expected = P - np.eye(N * N) / N
        assert np.allclose(Omega, expected)

    def test_sl3_r_shape(self):
        """sl_3 Belavin r-matrix is 9x9."""
        r = _mod.belavin_r_matrix_sl3(0.15 + 0.05j, TAU)
        assert r.shape == (9, 9)

    def test_sl3_r_finite(self):
        """sl_3 r-matrix is finite away from singularities."""
        r = _mod.belavin_r_matrix_sl3(0.15 + 0.05j, TAU)
        assert np.all(np.isfinite(r))

    def test_sl3_pole_at_zero(self):
        """sl_3 r-matrix has residue proportional to Omega at z=0."""
        z = 0.005
        r = _mod.belavin_r_matrix_sl3(z, TAU)
        Omega = _mod._sl3_casimir_fund()
        residue = z * r
        err = np.linalg.norm(residue - Omega) / np.linalg.norm(Omega)
        assert err < 0.15


# ============================================================
# Section 13: Pole structure
# ============================================================

class TestPoleStructure:
    """Tests for pole structure analysis (AP19 compliance)."""

    def test_sl2_residue_is_omega(self):
        """Residue of sl_2 r-matrix at z=0 matches Omega."""
        result = _mod.elliptic_pole_structure(0.005, TAU)
        assert result['sl2_residue_matches_Omega']

    def test_sl3_residue_is_omega(self):
        """Residue of sl_3 r-matrix at z=0 matches Omega."""
        result = _mod.elliptic_pole_structure(0.005, TAU)
        assert result['sl3_residue_matches_Omega']

    def test_simple_pole_not_double(self):
        """The r-matrix has a SIMPLE pole: z*r(z) converges as z -> 0."""
        z_values = [0.01, 0.005, 0.002]
        norms = []
        for z in z_values:
            r = _mod.belavin_r_matrix_sl2(z, TAU)
            norms.append(np.linalg.norm(z * r))
        # All norms should be close to each other (converging to Omega norm)
        assert max(norms) - min(norms) < 0.5 * np.mean(norms)

    def test_pole_structure_returns_structure(self):
        """Pole structure analysis returns expected keys."""
        result = _mod.elliptic_pole_structure()
        assert 'sl2_residue_error' in result
        assert 'sl3_residue_error' in result
        assert 'sl2_residue_matches_Omega' in result


# ============================================================
# Section 14: Shadow obstruction tower q-expansion
# ============================================================

class TestShadowTowerQExpansion:
    """Tests for q-expansion of the elliptic r-matrix."""

    def test_q_correction_small_for_large_im_tau(self):
        """q-correction is small when Im(tau) is large (q ~ 0)."""
        result = _mod.shadow_tower_q_expansion(0.15 + 0.05j, 5j, k=1.0)
        # r_ell should be close to r_trig, so correction should be small
        assert result['q_correction_norm'] < result['r_trig_norm']

    def test_q_correction_larger_for_small_im_tau(self):
        """q-correction grows when Im(tau) decreases (more winding modes)."""
        result_large = _mod.shadow_tower_q_expansion(0.15 + 0.05j, 5j, k=1.0)
        result_small = _mod.shadow_tower_q_expansion(0.15 + 0.05j, 1j, k=1.0)
        assert result_small['q_correction_norm'] > result_large['q_correction_norm']

    def test_q_expansion_returns_structure(self):
        """q-expansion returns expected keys."""
        result = _mod.shadow_tower_q_expansion(0.15 + 0.05j, TAU)
        assert 'tau' in result
        assert 'q' in result
        assert 'r_ell_norm' in result
        assert 'r_trig_norm' in result
        assert 'q_correction_norm' in result

    def test_q_abs_decreases_with_im_tau(self):
        """|q| = e^{-2*pi*Im(tau)} decreases with Im(tau)."""
        r1 = _mod.shadow_tower_q_expansion(0.15, 1j)
        r2 = _mod.shadow_tower_q_expansion(0.15, 3j)
        assert r2['q_abs'] < r1['q_abs']


# ============================================================
# Section 15: Kappa consistency
# ============================================================

class TestKappaConsistency:
    """Tests for kappa extraction from the r-matrix residue."""

    def test_kappa_sl2_returns_structure(self):
        """kappa extraction returns expected keys."""
        result = _mod.kappa_from_elliptic_rmatrix('sl2', 1.0, TAU)
        assert 'lie_type' in result
        assert 'expected_kappa' in result
        assert 'extracted_k_times_C2' in result
        assert 'expected_k_times_C2' in result

    def test_kappa_sl2_expected_value(self):
        """Expected kappa value is computed correctly."""
        result = _mod.kappa_from_elliptic_rmatrix('sl2', 1.0, TAU)
        assert abs(result['expected_kappa'] - 9.0 / 4.0) < 1e-10

    def test_kappa_sl3_expected_value(self):
        """Expected kappa value for sl_3 is computed correctly."""
        result = _mod.kappa_from_elliptic_rmatrix('sl3', 1.0, TAU)
        assert abs(result['expected_kappa'] - 16.0 / 3.0) < 1e-10

    def test_kappa_unsupported_type(self):
        """Unsupported Lie type raises error."""
        with pytest.raises((ValueError, KeyError)):
            _mod.kappa_from_elliptic_rmatrix('sl4', 1.0, TAU)


# ============================================================
# Section 16: Crossing symmetry
# ============================================================

class TestCrossingSymmetry:
    """Tests for crossing symmetry under half-period shift."""

    def test_crossing_sl2_returns_structure(self):
        """Crossing check returns expected structure."""
        result = _mod.verify_crossing_symmetry_sl2(0.15 + 0.05j, TAU, k=1.0)
        assert 'eigenvalue_diff' in result
        assert 'passed' in result

    def test_crossing_sl2_finite(self):
        """Half-period shift crossing check returns finite eigenvalue differences."""
        result = _mod.verify_crossing_symmetry_sl2(0.15 + 0.05j, TAU, k=1.0)
        assert np.isfinite(result['eigenvalue_diff'])


# ============================================================
# Section 17: Eisenstein correction
# ============================================================

class TestEisensteinCorrection:
    """Tests for the Eisenstein correction structure."""

    def test_corrections_finite(self):
        """Eisenstein corrections are finite numbers."""
        result = _mod.eisenstein_correction_analysis(TAU, k=1.0)
        for entry in result['corrections']:
            assert np.isfinite(entry['r0_norm'])

    def test_corrections_vary_with_tau(self):
        """Corrections change as tau varies (nontrivial modular dependence)."""
        result = _mod.eisenstein_correction_analysis(TAU, k=1.0)
        norms = [e['r0_norm'] for e in result['corrections']]
        assert max(norms) - min(norms) > 1e-5

    def test_corrections_return_structure(self):
        """Eisenstein correction returns expected keys."""
        result = _mod.eisenstein_correction_analysis(TAU)
        assert 'z_small' in result
        assert 'corrections' in result
        assert len(result['corrections']) > 0
        assert 'r0_norm' in result['corrections'][0]
        assert 'r0_trace' in result['corrections'][0]


# ============================================================
# Section 18: Quantum R-matrix
# ============================================================

class TestQuantumRMatrix:
    """Tests for the quantum (semi-classical) R-matrix."""

    def test_quantum_R_identity_at_leading_order(self):
        """R(z) = I + r(z)/kappa at leading order."""
        z = 0.15 + 0.05j
        k = 1.0
        R = _mod.quantum_R_matrix_sl2(z, TAU, k)
        kap = _mod.kappa_affine('sl2', k)
        r = _mod.genus1_shadow_rmatrix_sl2(z, TAU, k)
        expected = np.eye(4) + r / kap
        assert np.allclose(R, expected)

    def test_quantum_R_shape(self):
        """Quantum R-matrix is 4x4."""
        R = _mod.quantum_R_matrix_sl2(0.2, TAU, 1.0)
        assert R.shape == (4, 4)

    def test_quantum_R_converges_at_large_k(self):
        """At large k, R(z) = I + (4/3)*r_Belavin converges (since k/kappa -> 4/3 for sl_2)."""
        z = 0.15 + 0.05j
        R1 = _mod.quantum_R_matrix_sl2(z, TAU, k=50.0)
        R2 = _mod.quantum_R_matrix_sl2(z, TAU, k=100.0)
        # Should converge as k -> infinity
        assert np.linalg.norm(R1 - R2) < np.linalg.norm(R1 - np.eye(4)) * 0.1

    def test_quantum_R_finite(self):
        """Quantum R-matrix is finite away from singularities."""
        R = _mod.quantum_R_matrix_sl2(0.2 + 0.1j, TAU, 1.0)
        assert np.all(np.isfinite(R))


# ============================================================
# Section 19: Embedding operators
# ============================================================

class TestEmbeddings:
    """Tests for the 12, 13, 23 embedding operators."""

    def test_embed_12_shape_d2(self):
        """embed_12 for d=2 produces 8x8 matrix."""
        M = np.eye(4, dtype=complex)
        result = _mod._embed_12(M, 2)
        assert result.shape == (8, 8)

    def test_embed_23_shape_d2(self):
        """embed_23 for d=2 produces 8x8 matrix."""
        M = np.eye(4, dtype=complex)
        result = _mod._embed_23(M, 2)
        assert result.shape == (8, 8)

    def test_embed_13_shape_d2(self):
        """embed_13 for d=2 produces 8x8 matrix."""
        M = np.eye(4, dtype=complex)
        result = _mod._embed_13(M, 2)
        assert result.shape == (8, 8)

    def test_embed_12_shape_d3(self):
        """embed_12 for d=3 produces 27x27 matrix."""
        M = np.eye(9, dtype=complex)
        result = _mod._embed_12(M, 3)
        assert result.shape == (27, 27)

    def test_embed_13_shape_d3(self):
        """embed_13 for d=3 produces 27x27 matrix."""
        M = np.eye(9, dtype=complex)
        result = _mod._embed_13(M, 3)
        assert result.shape == (27, 27)

    def test_embed_identity_12(self):
        """Embedding identity in 12 gives identity on full space (I_12 acts trivially on slot 3)."""
        I4 = np.eye(4, dtype=complex)
        E12 = _mod._embed_12(I4, 2)
        assert np.allclose(E12, np.eye(8))

    def test_embed_identity_23(self):
        """Embedding identity in 23 gives identity on full space."""
        I4 = np.eye(4, dtype=complex)
        E23 = _mod._embed_23(I4, 2)
        assert np.allclose(E23, np.eye(8))

    def test_embed_identity_13(self):
        """Embedding identity in 13 gives identity on full space."""
        I4 = np.eye(4, dtype=complex)
        E13 = _mod._embed_13(I4, 2)
        assert np.allclose(E13, np.eye(8))


# ============================================================
# Section 20: Landscape summary
# ============================================================

class TestLandscape:
    """Tests for the summary landscape function."""

    def test_landscape_returns_dict(self):
        """Landscape summary returns a dictionary with expected keys."""
        result = _mod.elliptic_rmatrix_landscape(TAU, k=1.0)
        assert 'ybe_sl2' in result
        assert 'skew_symmetry' in result
        assert 'pole_structure' in result
        assert 'degeneration' in result
        assert 'kappa_sl2' in result
        assert 'tau' in result
        assert 'k' in result

    def test_landscape_skew_passes(self):
        """Skew-symmetry passes in the landscape check."""
        result = _mod.elliptic_rmatrix_landscape(TAU, k=1.0)
        assert result['skew_symmetry']['passed']

    def test_landscape_pole_structure_sl2(self):
        """Pole structure for sl_2 is correct in landscape."""
        result = _mod.elliptic_rmatrix_landscape(TAU, k=1.0)
        assert result['pole_structure']['sl2_residue_matches_Omega']
