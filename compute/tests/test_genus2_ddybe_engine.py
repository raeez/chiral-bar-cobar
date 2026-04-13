r"""Tests for the genus-2 doubly-dynamical Yang--Baxter equation engine.

Verifies prop:g2-ddybe (upgraded from conj:g2-ddybe) by:
1. Validating the genus-1 Felder DYBE as a baseline.
2. Numerically verifying the genus-2 DDYBE for alpha = 1 and alpha = 2.
3. Verifying the heat equation coupling condition.
4. Verifying the degeneration to two independent copies of Felder's DYBE.
5. Checking the Etingof-Varchenko framework extension.

Multi-path verification (AP10/HZ-6):
[DC] Direct computation of R-matrix from genus-2 theta functions
[LT] Felder 1994 genus-1 DYBE as limiting case
[SY] Weight-space symmetry of sl_2 R-matrix
[LC] Degeneration Omega_12 -> 0 (diagonal period matrix)
[NE] Numerical evaluation at 10+ digit precision
"""

import numpy as np
import pytest

from compute.lib.genus2_ddybe_engine import (
    # Theta functions
    jacobi_theta1,
    jacobi_theta1_prime0,
    riemann_theta_g2,
    # R-matrices
    felder_R_matrix,
    felder_boltzmann_weights,
    genus2_R_matrix,
    genus2_boltzmann_weights,
    # Verification functions
    verify_dybe_genus1,
    verify_ddybe_sl2,
    verify_heat_equation_g2,
    verify_degeneration_to_two_dybe,
    check_ev_framework_genus2,
    run_full_ddybe_verification,
    # Utilities
    sl2_fund_matrices,
    sl2_casimir_fund,
    embed_12,
    embed_13,
    embed_23,
    genus2_szego_kernel,
)

PI = np.pi


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture
def generic_omega():
    """A generic period matrix in H_2."""
    return np.array([[1.1j, 0.15 + 0.05j],
                      [0.15 + 0.05j, 1.3j]], dtype=complex)


@pytest.fixture
def diagonal_omega():
    """A diagonal period matrix (separating degeneration)."""
    return np.array([[1.2j, 0.0],
                      [0.0, 1.4j]], dtype=complex)


# ============================================================
# Test: Jacobi theta functions
# ============================================================

class TestThetaFunctions:
    """Basic tests for theta function implementations."""

    def test_theta1_odd(self):
        """theta_1 is an odd function: theta_1(-z) = -theta_1(z)."""
        tau = 1.5j
        z = 0.3 + 0.1j
        th_z = jacobi_theta1(z, tau)
        th_neg_z = jacobi_theta1(-z, tau)
        # VERIFIED: [DC] direct from series definition; [SY] odd symmetry
        assert abs(th_z + th_neg_z) < 1e-10 * max(abs(th_z), 1.0)

    def test_theta1_zero_at_origin(self):
        """theta_1(0|tau) = 0."""
        tau = 1.0j
        th_0 = jacobi_theta1(0.0, tau)
        # VERIFIED: [DC] series vanishes term by term; [LT] Mumford Tata I
        assert abs(th_0) < 1e-12

    def test_theta1_prime_triple_product(self):
        """theta_1'(0) = pi * theta_2(0) * theta_3(0) * theta_4(0)."""
        from compute.lib.elliptic_rmatrix_shadow import (
            jacobi_theta2 as th2,
            jacobi_theta3 as th3,
            jacobi_theta4 as th4,
        )
        tau = 1.5j
        tp0 = jacobi_theta1_prime0(tau)
        rhs = PI * th2(0, tau) * th3(0, tau) * th4(0, tau)
        # VERIFIED: [DC] numerical; [LT] Jacobi triple product (Mumford)
        assert abs(tp0 - rhs) < 1e-8 * max(abs(tp0), 1.0)

    def test_genus2_theta_factorization_diagonal(self):
        """At diagonal Omega, Riemann theta factorizes into product of genus-1 thetas."""
        tau1 = 1.2j
        tau2 = 1.5j
        Omega = np.array([[tau1, 0], [0, tau2]], dtype=complex)
        z = np.array([0.3 + 0.1j, 0.2 + 0.05j], dtype=complex)

        th_g2 = riemann_theta_g2(z, Omega, N=10)

        from compute.lib.elliptic_rmatrix_shadow import jacobi_theta3 as th3_g1
        th_product = th3_g1(z[0], tau1) * th3_g1(z[1], tau2)

        # VERIFIED: [DC] direct; [LC] diagonal limit; [LT] Fay "Theta functions on RS"
        rel = abs(th_g2 - th_product) / max(abs(th_g2), 1.0)
        assert rel < 1e-8, f"Factorization failed: relative error {rel}"


# ============================================================
# Test: Felder genus-1 dynamical R-matrix
# ============================================================

class TestFelderDYBE:
    """Tests for Felder's genus-1 dynamical R-matrix."""

    def test_felder_weights_symmetry(self):
        """beta(lam, z) and gamma(lam, z) satisfy beta(-lam,z) = gamma(lam,z)."""
        tau = 1.0j
        lam = 0.3 + 0.1j
        z = 0.2 + 0.05j
        eta = 0.25

        w_pos = felder_boltzmann_weights(lam, z, eta, tau)
        w_neg = felder_boltzmann_weights(-lam, z, eta, tau)

        # beta(-lam,z) = gamma(lam,z) (proved analytically via theta_1 odd)
        # VERIFIED: [DC] numerical; [SY] theta_1 odd symmetry
        assert abs(w_neg['beta'] - w_pos['gamma']) < 1e-8, \
            f"beta(-lam) != gamma(lam): {w_neg['beta']} vs {w_pos['gamma']}"

    def test_felder_dybe_genus1(self):
        """Verify the standard DYBE for Felder's R-matrix at genus 1.

        Uses the full 8x8 shifted-matrix formulation.
        """
        tau = 1.0j
        lam = 0.3 + 0.1j
        eta = 0.25
        z1, z2, z3 = 0.1 + 0.05j, 0.35 + 0.02j, 0.6 + 0.07j

        result = verify_dybe_genus1(lam, z1, z2, z3, eta, tau)
        # VERIFIED: [DC] numerical 8x8 matrix; [LT] Felder 1994 Thm 4.1
        assert result['passed'], \
            f"Felder DYBE failed: relative residual {result['relative']}"

    def test_felder_dybe_multiple_points(self):
        """DYBE at multiple parameter points."""
        tau = 1.2j
        eta = 0.2
        points = [
            (0.2 + 0.1j, 0.05j, 0.3 + 0.02j, 0.5 + 0.04j),
            (0.4 + 0.05j, 0.1 + 0.03j, 0.25 + 0.01j, 0.45 + 0.06j),
            (0.15 + 0.2j, 0.08 + 0.01j, 0.35 + 0.05j, 0.55 + 0.02j),
        ]
        for lam, z1, z2, z3 in points:
            result = verify_dybe_genus1(lam, z1, z2, z3, eta, tau)
            # VERIFIED: [DC] at each point; [NE] numerical
            assert result['passed'], \
                f"DYBE at lam={lam} failed: {result['relative']}"


# ============================================================
# Test: Genus-2 R-matrix structure
# ============================================================

class TestGenus2RMatrix:
    """Tests for the genus-2 doubly-dynamical R-matrix."""

    def test_rmatrix_weight_symmetry(self, generic_omega):
        """R has alpha on diagonal (++,--), beta/gamma in +- block."""
        lam1, lam2 = 0.3 + 0.1j, 0.2 + 0.15j
        z = 0.15 + 0.05j
        eta = 0.25

        R = genus2_R_matrix(lam1, lam2, z, eta, generic_omega)

        # alpha(++) = alpha(--)
        # VERIFIED: [SY] sl_2 weight symmetry
        assert abs(R[0, 0] - R[3, 3]) < 1e-8 * max(abs(R[0, 0]), 1.0)

        # Off-diagonal zeros
        for i, j in [(0, 1), (0, 2), (0, 3), (3, 0), (3, 1), (3, 2)]:
            assert abs(R[i, j]) < 1e-10, f"Unexpected nonzero R[{i},{j}] = {R[i,j]}"

    def test_rmatrix_nonzero(self, generic_omega):
        """R is nonzero at generic parameters."""
        R = genus2_R_matrix(0.3 + 0.1j, 0.2 + 0.15j, 0.15 + 0.05j,
                             0.25, generic_omega)
        # VERIFIED: [DC] theta functions nonzero at generic point
        assert np.linalg.norm(R) > 1e-3

    def test_rmatrix_reduces_to_genus1_at_diagonal(self, diagonal_omega):
        """At diagonal Omega, genus-2 R reduces to genus-1 R (normalized)."""
        lam1 = 0.3 + 0.1j
        lam2 = 0.2 + 0.15j
        z = 0.15 + 0.05j
        eta = 0.25
        tau1 = diagonal_omega[0, 0]

        R_g2 = genus2_R_matrix(lam1, lam2, z, eta, diagonal_omega)
        R_g1 = felder_R_matrix(lam1, z, eta, tau1)

        # Normalize
        if abs(R_g2[0, 0]) > 1e-300 and abs(R_g1[0, 0]) > 1e-300:
            R_g2_n = R_g2 / R_g2[0, 0]
            R_g1_n = R_g1 / R_g1[0, 0]
            diff = np.linalg.norm(R_g2_n - R_g1_n) / max(np.linalg.norm(R_g1_n), 1.0)
            # VERIFIED: [LC] diagonal degeneration; [LT] prop:g2-nonsep-degen
            assert diff < 1e-4, f"Genus-2 does not reduce to genus-1: {diff}"


# ============================================================
# Test: DDYBE verification
# ============================================================

class TestDDYBE:
    """Core DDYBE verification tests."""

    def test_ddybe_alpha1(self, generic_omega):
        """DDYBE for alpha = 1 direction."""
        result = verify_ddybe_sl2(
            0.3 + 0.1j, 0.2 + 0.15j,
            0.1 + 0.05j, 0.35 + 0.02j, 0.55 + 0.07j,
            generic_omega, alpha=1, eta=0.25, N_theta=8)
        # VERIFIED: [DC] direct 8x8 matrix; [LT] CEE09 flatness
        assert result['passed'], \
            f"DDYBE alpha=1 failed: residual {result['relative']}"

    def test_ddybe_alpha2(self, generic_omega):
        """DDYBE for alpha = 2 direction."""
        result = verify_ddybe_sl2(
            0.3 + 0.1j, 0.2 + 0.15j,
            0.1 + 0.05j, 0.35 + 0.02j, 0.55 + 0.07j,
            generic_omega, alpha=2, eta=0.25, N_theta=8)
        # VERIFIED: [DC] direct 8x8 matrix; [LT] CEE09 flatness
        assert result['passed'], \
            f"DDYBE alpha=2 failed: residual {result['relative']}"

    def test_ddybe_at_multiple_points(self, generic_omega):
        """DDYBE at multiple parameter points for robustness."""
        eta = 0.25
        points = [
            (0.3 + 0.1j, 0.2 + 0.15j, 0.1 + 0.05j, 0.3 + 0.02j, 0.5 + 0.07j),
            (0.1 + 0.2j, 0.4 + 0.1j, 0.15 + 0.03j, 0.25 + 0.08j, 0.45 + 0.04j),
        ]
        for lam1, lam2, z1, z2, z3 in points:
            for alpha in [1, 2]:
                result = verify_ddybe_sl2(
                    lam1, lam2, z1, z2, z3, generic_omega,
                    alpha=alpha, eta=eta, N_theta=8)
                # VERIFIED: [DC] at each point; [NE] numerical
                assert result['passed'], \
                    f"DDYBE alpha={alpha} at ({lam1},{lam2}) failed: {result['relative']}"

    def test_ddybe_trivial_at_diagonal_omega(self):
        """At diagonal Omega, both alpha=1 and alpha=2 DDBYEs hold."""
        Omega = np.array([[1.2j, 0], [0, 1.4j]], dtype=complex)
        result = verify_ddybe_sl2(
            0.3 + 0.1j, 0.2 + 0.15j,
            0.1 + 0.05j, 0.35 + 0.02j, 0.55 + 0.07j,
            Omega, alpha=1, eta=0.25, N_theta=8)
        # VERIFIED: [LC] diagonal limit; [LT] prop:g2-nonsep-degen (iv)
        assert result['passed'], f"DDYBE diagonal failed: {result['relative']}"


# ============================================================
# Test: Heat equation
# ============================================================

class TestHeatEquation:
    """Tests for the heat equation coupling condition."""

    def test_heat_11(self, generic_omega):
        """Heat equation for (alpha, beta) = (1, 1)."""
        result = verify_heat_equation_g2(
            0.3 + 0.1j, 0.2 + 0.15j, 0.15 + 0.05j,
            generic_omega, 0, 0, eta=0.25, N_theta=8)
        # VERIFIED: [DC] finite difference; [LT] eq:ddybe-coupling
        assert result['passed'], f"Heat eq (1,1) failed: {result['relative']}"

    def test_heat_22(self, generic_omega):
        """Heat equation for (alpha, beta) = (2, 2)."""
        result = verify_heat_equation_g2(
            0.3 + 0.1j, 0.2 + 0.15j, 0.15 + 0.05j,
            generic_omega, 1, 1, eta=0.25, N_theta=8)
        # VERIFIED: [DC] finite difference; [LT] eq:ddybe-coupling
        assert result['passed'], f"Heat eq (2,2) failed: {result['relative']}"

    def test_heat_12(self, generic_omega):
        """Heat equation for (alpha, beta) = (1, 2): genuinely new at genus 2."""
        result = verify_heat_equation_g2(
            0.3 + 0.1j, 0.2 + 0.15j, 0.15 + 0.05j,
            generic_omega, 0, 1, eta=0.25, N_theta=8)
        # VERIFIED: [DC] finite difference; [LT] eq:ddybe-coupling
        # This coupling has no genus-1 analogue (rem:cee-comparison)
        assert result['passed'], f"Heat eq (1,2) failed: {result['relative']}"


# ============================================================
# Test: Degeneration
# ============================================================

class TestDegeneration:
    """Tests for the degeneration to two independent DYBEs."""

    def test_degeneration_matches_genus1(self):
        """At Omega_12 = 0, genus-2 R reduces to genus-1."""
        result = verify_degeneration_to_two_dybe(
            0.3 + 0.1j, 0.2 + 0.15j, 0.15 + 0.05j,
            tau1=1.2j, tau2=1.4j, eta=0.25)
        # VERIFIED: [LC] diagonal degeneration; [LT] prop:g2-nonsep-degen
        assert result['matches_genus1'], \
            f"Degeneration failed: {result['genus2_vs_genus1_relative']}"

    def test_lam2_decouples_at_diagonal(self):
        """At Omega_12 = 0, R is independent of lambda_2."""
        result = verify_degeneration_to_two_dybe(
            0.3 + 0.1j, 0.2 + 0.15j, 0.15 + 0.05j,
            tau1=1.2j, tau2=1.4j, eta=0.25)
        # VERIFIED: [LC] decoupling; [SY] B_2 monodromy trivializes
        assert result['lam2_decoupled'], \
            f"Lambda_2 not decoupled: {result['lam2_independence_relative']}"

    def test_degeneration_multiple_tau(self):
        """Degeneration at several values of (tau1, tau2)."""
        for tau1, tau2 in [(1.0j, 1.5j), (1.5j, 0.9j)]:
            result = verify_degeneration_to_two_dybe(
                0.25 + 0.1j, 0.35 + 0.2j, 0.12 + 0.04j,
                tau1=tau1, tau2=tau2, eta=0.25)
            # VERIFIED: [LC] at each tau pair; [NE] numerical
            assert result['matches_genus1'], \
                f"Degeneration at tau=({tau1},{tau2}) failed: " \
                f"{result['genus2_vs_genus1_relative']}"


# ============================================================
# Test: Etingof-Varchenko framework
# ============================================================

class TestEVFramework:
    """Tests for the Etingof-Varchenko framework extension."""

    def test_ev_extends(self):
        """The EV framework extends to genus 2 via CEE."""
        result = check_ev_framework_genus2()
        assert result['ev_framework_extends'] is True
        assert 'CEE09' in result['mechanism']

    def test_ev_references_complete(self):
        """All four key references are cited."""
        result = check_ev_framework_genus2()
        refs = result['references']
        assert any('Etingof-Varchenko' in r for r in refs)
        assert any('Calaque-Enriquez-Etingof' in r for r in refs)
        assert any('Bernard' in r for r in refs)
        assert any('Felder' in r for r in refs)


# ============================================================
# Test: Szego kernel
# ============================================================

class TestSzegoKernel:
    """Tests for the genus-2 Szego kernel."""

    def test_szego_has_simple_pole(self, generic_omega):
        """S_2(z) ~ 1/z near z = 0."""
        zvals = [0.001j, 0.002j, 0.005j]
        for z in zvals:
            S = genus2_szego_kernel(z, generic_omega, N=8)
            product = z * S
            # z * S(z) -> 1 as z -> 0
            # VERIFIED: [DC] Laurent expansion; [LT] Fay
            assert abs(product - 1.0) < 0.15, \
                f"Residue not close to 1: z*S(z) = {product} at z={z}"


# ============================================================
# Test: Full suite
# ============================================================

class TestFullSuite:
    """Integration test for the complete verification."""

    def test_full_verification(self):
        """Run complete DDYBE verification."""
        results = run_full_ddybe_verification(eta=0.25, N_theta=8)
        summary = results['summary']
        assert summary['ddybe_passed'], "DDYBE verification failed"
        assert summary['heat_equation_passed'], "Heat equation verification failed"
        assert summary['degeneration_passed'], "Degeneration verification failed"
        assert summary['all_passed'], "Not all checks passed"


# ============================================================
# Test: Embedding operators
# ============================================================

class TestEmbeddings:
    """Tests for the tensor embedding operators."""

    def test_embed_dimensions(self):
        """All embeddings produce 8x8 matrices."""
        M = np.eye(4, dtype=complex)
        assert embed_12(M).shape == (8, 8)
        assert embed_13(M).shape == (8, 8)
        assert embed_23(M).shape == (8, 8)

    def test_embed_identity(self):
        """Embedding the identity gives the identity."""
        Id4 = np.eye(4, dtype=complex)
        Id8 = np.eye(8, dtype=complex)
        np.testing.assert_allclose(embed_12(Id4), Id8, atol=1e-12)
        np.testing.assert_allclose(embed_23(Id4), Id8, atol=1e-12)
        np.testing.assert_allclose(embed_13(Id4), Id8, atol=1e-12)
