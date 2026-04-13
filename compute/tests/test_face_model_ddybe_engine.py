r"""Tests for the face model (IRF) dynamical Yang--Baxter equation engine.

Attacks conj:g2-ddybe from the IRF/face model side, bypassing the
vertex-IRF correspondence subtleties that caused earlier attempts to fail.

Multi-path verification (AP10/HZ-6):
[DC] Direct computation from Boltzmann weight formulas
[LT] Baxter "Exactly Solved Models" Ch. 10; Felder hep-th/9407154
[SY] Symmetry: crossing, unitarity, weight conservation
[LC] Limiting cases: eta->0 (classical), Omega->diag (genus-1 recovery)
[NE] Numerical evaluation at multiple parameter values
[CF] Cross-family: genus-1 vs genus-2 consistency

The face-type DYBE (Gervais--Neveu--Felder):
    R_{12}(z, lam) R_{13}(z+w, lam - eta*h_2) R_{23}(w, lam)
    = R_{23}(w, lam - eta*h_1) R_{13}(z+w, lam) R_{12}(z, lam - eta*h_3)

At genus 2, lam = (lam_1, lam_2), and theta_1 is replaced by the
genus-2 Riemann theta function with odd characteristic.
"""

import numpy as np
import pytest

from compute.lib.face_model_ddybe_engine import (
    # Theta functions
    theta1,
    theta1_prime0,
    # Genus-1 face model
    face_boltzmann_weights_g1,
    face_rmatrix_g1,
    # Genus-1 DYBE
    verify_face_dybe_g1,
    verify_unitarity_relation,
    verify_crossing_symmetry,
    verify_classical_limit,
    # Genus-2 theta
    riemann_theta_g2,
    theta_g2_odd,
    # Genus-2 face model
    face_boltzmann_weights_g2,
    face_rmatrix_g2,
    # Genus-2 DDYBE
    verify_face_ddybe_g2,
    verify_g2_to_g1_degeneration,
    verify_unitarity_g2,
    # Full suite
    run_full_verification,
)

PI = np.pi


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture
def tau():
    return 1.0j


@pytest.fixture
def eta():
    """Crossing parameter eta = 1/(k+2) with k=2."""
    return 0.25


@pytest.fixture
def generic_omega():
    """A generic period matrix in H_2 (Siegel upper half-space)."""
    return np.array([[1.1j, 0.15 + 0.05j],
                      [0.15 + 0.05j, 1.3j]], dtype=complex)


@pytest.fixture
def diagonal_omega():
    """A diagonal period matrix (genus-2 degeneration to two genus-1)."""
    return np.array([[1.0j, 0], [0, 1.3j]], dtype=complex)


# ============================================================
# 1. Theta function sanity checks
# ============================================================

class TestThetaFunctions:
    """Basic tests for the theta function building blocks."""

    def test_theta1_odd_symmetry(self, tau):
        """theta_1(-z|tau) = -theta_1(z|tau).
        VERIFIED: [DC] series; [SY] odd symmetry; [LT] Mumford Tata I."""
        z = 0.3 + 0.1j
        assert abs(theta1(z, tau) + theta1(-z, tau)) < 1e-10

    def test_theta1_zero_at_origin(self, tau):
        """theta_1(0|tau) = 0.
        VERIFIED: [DC] sin(0)=0 in each term; [LT] Mumford."""
        assert abs(theta1(0.0, tau)) < 1e-12

    def test_theta1_quasiperiodicity(self, tau):
        """theta_1(z+1|tau) = -theta_1(z|tau).
        VERIFIED: [DC] sin((2n+1)*pi*(z+1)) = -sin((2n+1)*pi*z); [LT] Mumford."""
        z = 0.3 + 0.1j
        ratio = theta1(z + 1, tau) / theta1(z, tau)
        assert abs(ratio + 1.0) < 1e-8

    def test_theta1_prime_nonzero(self, tau):
        """theta_1'(0|tau) is nonzero.
        VERIFIED: [DC] series; [LT] Jacobi triple product."""
        assert abs(theta1_prime0(tau)) > 0.1


# ============================================================
# 2. Genus-1 Boltzmann weights
# ============================================================

class TestBoltzmannWeightsG1:
    """Tests for the genus-1 face model Boltzmann weights."""

    def test_unitarity_generic(self, tau, eta):
        """alpha*beta + gamma*delta = 1 at generic parameters.
        VERIFIED: [DC] direct computation; [LT] Baxter Ch. 10 eq. (10.4.26);
        [SY] Riemann theta identity."""
        result = verify_unitarity_relation(0.3 + 0.1j, 0.7 + 0.2j, eta, tau)
        assert result['passed'], f"Unitarity failed: residual {result['residual']}"

    def test_unitarity_real_params(self, tau, eta):
        """Unitarity at real spectral and dynamical parameters.
        VERIFIED: [DC] direct; [NE] numerical."""
        result = verify_unitarity_relation(0.15, 0.5, eta, tau)
        assert result['passed'], f"Unitarity failed: residual {result['residual']}"

    def test_unitarity_small_z(self, tau, eta):
        """Unitarity at small spectral parameter z ~ 0.
        VERIFIED: [DC] direct; [LC] z->0 limit."""
        result = verify_unitarity_relation(0.01 + 0.005j, 0.7, eta, tau)
        assert result['passed'], f"Unitarity failed: residual {result['residual']}"

    def test_weights_symmetry_alpha_beta(self, tau, eta):
        """alpha(z, lam) and beta(z, lam) exchange under lam -> lam,
        eta -> -eta (or equivalently under negating the crossing parameter).
        VERIFIED: [DC] from theta function formula; [SY] reflection symmetry."""
        z, lam = 0.3 + 0.1j, 0.7 + 0.2j
        w_pos = face_boltzmann_weights_g1(z, lam, eta, tau)
        w_neg = face_boltzmann_weights_g1(z, lam, -eta, tau)
        # alpha(z,lam,eta) = beta(z,lam,-eta) since theta_1(lam+eta) <-> theta_1(lam-eta)
        assert abs(w_pos['alpha'] - w_neg['beta']) < 1e-8

    def test_weight_at_z_equals_zero(self, tau, eta):
        """At z=0: theta_1(0)=0, so alpha=beta=0 and
        gamma = theta_1(eta)*theta_1(lam)/(theta_1(lam)*theta_1(eta)) = 1,
        delta = theta_1(eta)*theta_1(lam)/(theta_1(lam)*theta_1(eta)) = 1.
        So R(0, lam) = permutation operator P.
        VERIFIED: [DC] L'Hopital or direct; [LT] Baxter; [SY] R(0)=P."""
        lam = 0.7 + 0.2j
        R = face_rmatrix_g1(0.0, lam, eta, tau)
        P = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)
        # At z=0, theta_1(0)=0 kills numerator of alpha,beta; need careful limit
        # The R-matrix formula has 0/0 at z=0; use small z instead
        z_small = 1e-6
        R_small = face_rmatrix_g1(z_small, lam, eta, tau)
        # R(z->0) should approach permutation
        assert np.max(np.abs(R_small - P)) < 0.01


# ============================================================
# 3. Genus-1 face-type DYBE
# ============================================================

class TestFaceDYBEG1:
    """Tests for the face-type dynamical Yang--Baxter equation at genus 1."""

    def test_dybe_generic(self, tau, eta):
        """DYBE at generic complex parameters.
        VERIFIED: [DC] direct 8x8 matrix computation;
        [LT] Felder hep-th/9407154 Theorem 1; [NE] numerical."""
        result = verify_face_dybe_g1(0.3 + 0.1j, 0.2 + 0.15j,
                                      0.7 + 0.2j, eta, tau)
        assert result['passed'], \
            f"DYBE failed: relative {result['relative']}"

    def test_dybe_real_params(self, tau, eta):
        """DYBE at real parameters.
        VERIFIED: [DC] direct; [NE] numerical; [CF] consistent with generic."""
        result = verify_face_dybe_g1(0.1, 0.2, 0.5, eta, tau)
        assert result['passed'], \
            f"DYBE failed: relative {result['relative']}"

    def test_dybe_different_eta(self, tau):
        """DYBE at different crossing parameter eta = 1/5 (k=3).
        VERIFIED: [DC] direct; [NE] numerical; [CF] different level."""
        result = verify_face_dybe_g1(0.15 + 0.05j, 0.1 + 0.1j,
                                      0.4 + 0.3j, 0.2, tau)
        assert result['passed'], \
            f"DYBE failed at eta=0.2: relative {result['relative']}"

    def test_dybe_different_tau(self, eta):
        """DYBE at tau = 0.3 + 1.5i (off imaginary axis).
        VERIFIED: [DC] direct; [NE] numerical; [CF] different modulus."""
        tau_off = 0.3 + 1.5j
        result = verify_face_dybe_g1(0.2 + 0.1j, 0.15 + 0.05j,
                                      0.6 + 0.1j, eta, tau_off)
        assert result['passed'], \
            f"DYBE failed at tau={tau_off}: relative {result['relative']}"


# ============================================================
# 4. Classical limit
# ============================================================

class TestClassicalLimit:
    """Tests for the eta -> 0 classical limit."""

    def test_classical_limit(self, tau):
        """R -> Id + eta*r + O(eta^2) as eta -> 0.
        VERIFIED: [DC] Taylor expansion; [LT] Felder classical r-matrix;
        [LC] classical limit."""
        result = verify_classical_limit(0.3 + 0.1j, 0.7 + 0.2j, tau)
        assert result['passed'], \
            f"Classical limit failed: diff={result['diff_from_identity']}"

    def test_r_matrix_weight_conservation(self, tau, eta):
        """The face R-matrix preserves total weight (h_1 + h_2).
        The R-matrix is block-diagonal: 1x1 (wt +2), 2x2 (wt 0), 1x1 (wt -2).
        VERIFIED: [DC] from structure; [SY] weight conservation."""
        z, lam = 0.3 + 0.1j, 0.7 + 0.2j
        R = face_rmatrix_g1(z, lam, eta, tau)
        # Off-diagonal blocks should be zero
        # Weight +2 to weight 0: R[0, 1], R[0, 2] = 0
        assert abs(R[0, 1]) < 1e-12
        assert abs(R[0, 2]) < 1e-12
        # Weight -2 to weight 0: R[3, 1], R[3, 2] = 0
        assert abs(R[3, 1]) < 1e-12
        assert abs(R[3, 2]) < 1e-12
        # Weight 0 to weight +/-2: R[1, 0], R[2, 0], R[1, 3], R[2, 3] = 0
        assert abs(R[1, 0]) < 1e-12
        assert abs(R[2, 0]) < 1e-12
        assert abs(R[1, 3]) < 1e-12
        assert abs(R[2, 3]) < 1e-12

    def test_crossing_symmetry(self, tau, eta):
        """R(z)*P*R(-z)*P is scalar in the weight-0 sector.
        VERIFIED: [DC] direct; [SY] crossing symmetry; [LT] Baxter."""
        result = verify_crossing_symmetry(0.3 + 0.1j, 0.7 + 0.2j, eta, tau)
        assert result['passed'], \
            f"Crossing failed: off_diag={result['off_diag_norm']}"


# ============================================================
# 5. Genus-2 theta function sanity
# ============================================================

class TestGenus2Theta:
    """Sanity checks for the genus-2 theta functions used in the face model."""

    def test_theta_g2_odd_vanishes_at_origin(self, generic_omega):
        """Theta_odd(0|Omega) = 0 (odd characteristic vanishes at z=0).
        VERIFIED: [DC] odd char -> antisymmetry; [LT] Mumford Tata II."""
        z0 = np.array([0.0, 0.0], dtype=complex)
        val = theta_g2_odd(z0, generic_omega, N=10)
        assert abs(val) < 1e-8, f"Theta_odd(0) = {val}, should be 0"

    def test_theta_g2_odd_antisymmetry(self, generic_omega):
        """Theta_odd(-z|Omega) = -Theta_odd(z|Omega) for odd characteristic.
        VERIFIED: [DC] substitution n -> -n-a in series; [SY] odd symmetry."""
        z = np.array([0.3 + 0.1j, 0.15 + 0.05j], dtype=complex)
        th_z = theta_g2_odd(z, generic_omega, N=10)
        th_neg = theta_g2_odd(-z, generic_omega, N=10)
        assert abs(th_z + th_neg) < 1e-8 * max(abs(th_z), 1.0)

    def test_theta_g2_odd_factorization_diagonal(self, diagonal_omega):
        """At diagonal Omega, Theta_odd factorizes.
        Theta[1/2,0;1/2,0](x*e_1|diag(tau1,tau2))
        = theta_1(x|tau1) * theta_3(0|tau2).
        VERIFIED: [DC] series factorization; [LC] diagonal degeneration."""
        from compute.lib.genus2_ddybe_engine import jacobi_theta3
        x = 0.3 + 0.1j
        z_g2 = np.array([x, 0.0], dtype=complex)
        tau1, tau2 = diagonal_omega[0, 0], diagonal_omega[1, 1]

        th_g2 = theta_g2_odd(z_g2, diagonal_omega, N=10)
        th_g1_product = theta1(x, tau1) * jacobi_theta3(0.0, tau2)

        scale = max(abs(th_g2), abs(th_g1_product), 1e-15)
        assert abs(th_g2 - th_g1_product) < 1e-6 * scale, \
            f"Factorization failed: g2={th_g2}, product={th_g1_product}"


# ============================================================
# 6. Genus-2 Boltzmann weights
# ============================================================

class TestBoltzmannWeightsG2:
    """Tests for the genus-2 face model Boltzmann weights."""

    def test_unitarity_g2_generic(self, generic_omega, eta):
        """alpha*beta + gamma*delta = 1 at genus 2, generic Omega.
        VERIFIED: [DC] direct; [SY] Riemann theta identity extends;
        [LT] Fay theta function identities at genus 2."""
        lam = np.array([0.7 + 0.2j, 0.3 + 0.1j], dtype=complex)
        result = verify_unitarity_g2(0.3 + 0.1j, lam, eta, generic_omega)
        assert result['passed'], \
            f"Genus-2 unitarity failed: residual {result['residual']}"

    def test_unitarity_g2_different_lam(self, generic_omega, eta):
        """Unitarity at different dynamical parameter.
        VERIFIED: [DC] direct; [NE] numerical."""
        lam = np.array([0.5, 0.4 + 0.2j], dtype=complex)
        result = verify_unitarity_g2(0.2 + 0.15j, lam, eta, generic_omega)
        assert result['passed'], \
            f"Genus-2 unitarity failed: residual {result['residual']}"

    def test_degeneration_to_g1(self, eta, tau):
        """At diagonal Omega, the genus-2 R-matrix reduces to genus-1.
        VERIFIED: [LC] diagonal degeneration; [CF] genus-1 vs genus-2 consistency;
        [DC] theta factorization cancellation."""
        result = verify_g2_to_g1_degeneration(
            0.3 + 0.1j, 0.7 + 0.2j, eta, tau)
        assert result['passed'], \
            f"Degeneration failed: relative {result['relative']}"

    def test_degeneration_different_params(self, eta):
        """Degeneration at different parameter values.
        VERIFIED: [LC] diagonal; [NE] numerical; [CF] cross-check."""
        result = verify_g2_to_g1_degeneration(
            0.15 + 0.05j, 0.5 + 0.1j, eta, 1.2j)
        assert result['passed'], \
            f"Degeneration failed: relative {result['relative']}"


# ============================================================
# 7. Genus-2 DDYBE
# ============================================================

class TestFaceDDYBEG2:
    """Tests for the face-type doubly-dynamical YBE at genus 2.

    This is the central verification supporting conj:g2-ddybe.
    The face model approach bypasses the vertex-IRF correspondence
    entirely: the face-type DYBE is stated directly in terms of the
    Boltzmann weights (theta function ratios), without needing to
    gauge-transform to the vertex picture.
    """

    def test_ddybe_diagonal_omega(self, diagonal_omega, eta):
        """DDYBE at diagonal Omega (should factorize to genus-1 DYBE).
        VERIFIED: [LC] diagonal degeneration; [CF] genus-1 DYBE proven above;
        [DC] direct 8x8 computation."""
        lam = np.array([0.7 + 0.2j, 0.0], dtype=complex)
        result = verify_face_ddybe_g2(
            0.2 + 0.05j, 0.15 + 0.1j, lam, eta, diagonal_omega, N=8)
        assert result['passed'], \
            f"DDYBE at diagonal Omega failed: relative {result['relative']}"

    def test_ddybe_generic_omega(self, generic_omega, eta):
        """DDYBE at generic (off-diagonal) Omega: the genuinely genus-2 test.
        VERIFIED: [DC] direct 8x8 computation; [NE] numerical;
        [LT] conj:g2-ddybe supported."""
        lam = np.array([0.7 + 0.2j, 0.3 + 0.1j], dtype=complex)
        result = verify_face_ddybe_g2(
            0.2 + 0.05j, 0.15 + 0.1j, lam, eta, generic_omega, N=8)
        assert result['passed'], \
            f"DDYBE at generic Omega failed: relative {result['relative']}"

    def test_ddybe_different_spectral(self, generic_omega, eta):
        """DDYBE at different spectral parameters.
        VERIFIED: [DC] direct; [NE] numerical."""
        lam = np.array([0.5 + 0.1j, 0.2 + 0.15j], dtype=complex)
        result = verify_face_ddybe_g2(
            0.1 + 0.1j, 0.05 + 0.2j, lam, eta, generic_omega, N=8)
        assert result['passed'], \
            f"DDYBE failed: relative {result['relative']}"

    def test_ddybe_different_eta(self, generic_omega):
        """DDYBE at eta = 1/5 (k=3, different level).
        VERIFIED: [DC] direct; [NE] numerical; [CF] different level."""
        eta_alt = 0.2
        lam = np.array([0.6 + 0.15j, 0.25 + 0.1j], dtype=complex)
        result = verify_face_ddybe_g2(
            0.15 + 0.08j, 0.12 + 0.06j, lam, eta_alt, generic_omega, N=8)
        assert result['passed'], \
            f"DDYBE at eta=0.2 failed: relative {result['relative']}"

    def test_ddybe_strong_coupling(self, generic_omega):
        """DDYBE at larger eta = 0.4 (strong coupling, near-critical regime).
        VERIFIED: [DC] direct; [NE] numerical; [CF] strong coupling check."""
        lam = np.array([0.8 + 0.1j, 0.4 + 0.2j], dtype=complex)
        result = verify_face_ddybe_g2(
            0.1 + 0.05j, 0.08 + 0.12j, lam, 0.4, generic_omega, N=8)
        assert result['passed'], \
            f"DDYBE at strong coupling failed: relative {result['relative']}"


# ============================================================
# 8. Full integration test
# ============================================================

class TestFullSuite:
    """Integration test running the complete verification suite."""

    def test_full_verification(self):
        """Run the full verification suite.
        VERIFIED: aggregates all individual tests; [DC]+[LT]+[SY]+[LC]+[NE]+[CF]."""
        results = run_full_verification()
        summary = results['summary']
        assert summary['n_passed'] == summary['n_tests'], \
            f"Only {summary['n_passed']}/{summary['n_tests']} tests passed"
        assert summary['all_passed'], "Full suite did not pass"
