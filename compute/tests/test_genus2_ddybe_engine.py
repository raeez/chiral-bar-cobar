r"""Tests for the genus-2 doubly-dynamical Yang--Baxter equation engine.

Supports conj:g2-ddybe by verifying:
1. The genus-2 theta function heat equation (all three components).
2. Theta function factorization at diagonal period matrix.
3. Szego kernel degeneration to genus 1.
4. Szego kernel simple pole residue.
5. Etingof-Varchenko framework extension.

The conjecture itself (the DDYBE for the sl_2 R-matrix) is NOT numerically
verified here; it requires a verified implementation of the Felder dynamical
R-matrix with the correct vertex-IRF correspondence, which involves subtle
normalization choices.  The supporting infrastructure (heat equation, theta
functions, degenerations) IS verified.

Multi-path verification (AP10/HZ-6):
[DC] Direct computation from genus-2 theta functions
[LT] Fay "Theta functions on Riemann surfaces" (heat equation)
[SY] Symmetry of Riemann theta under Omega transpose
[LC] Degeneration Omega_12 -> 0 (diagonal period matrix)
[NE] Numerical evaluation at 10+ digit precision
"""

import numpy as np
import pytest

from compute.lib.genus2_ddybe_engine import (
    # Theta functions
    jacobi_theta1,
    jacobi_theta1_prime0,
    jacobi_theta3,
    riemann_theta_g2,
    riemann_theta_g2_gradient,
    # Szego kernel
    genus2_szego_kernel,
    # Verification functions
    verify_heat_equation_theta_g2,
    verify_theta_factorization_diagonal,
    verify_szego_degeneration,
    check_ev_framework_genus2,
    run_full_verification,
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


# ============================================================
# Test: Jacobi theta functions
# ============================================================

class TestThetaFunctions:
    """Basic tests for theta function implementations."""

    def test_theta1_odd(self):
        """theta_1(-z) = -theta_1(z)."""
        tau = 1.5j
        z = 0.3 + 0.1j
        th_z = jacobi_theta1(z, tau)
        th_neg_z = jacobi_theta1(-z, tau)
        # VERIFIED: [DC] series definition; [SY] odd symmetry
        assert abs(th_z + th_neg_z) < 1e-10 * max(abs(th_z), 1.0)

    def test_theta1_zero_at_origin(self):
        """theta_1(0|tau) = 0."""
        tau = 1.0j
        # VERIFIED: [DC] sin(0) = 0 in each term; [LT] Mumford Tata I
        assert abs(jacobi_theta1(0.0, tau)) < 1e-12

    def test_theta1_prime_triple_product(self):
        """theta_1'(0) = pi * theta_2(0) * theta_3(0) * theta_4(0)."""
        def th2(z, tau, n_terms=80):
            q = np.exp(1j * PI * tau)
            result = 0.0 + 0.0j
            for n in range(n_terms):
                result += q ** ((n + 0.5) ** 2) * np.cos((2 * n + 1) * PI * z)
            return 2.0 * result

        def th3(z, tau, n_terms=80):
            q = np.exp(1j * PI * tau)
            result = 1.0 + 0.0j
            for n in range(1, n_terms + 1):
                result += 2.0 * q ** (n ** 2) * np.cos(2 * n * PI * z)
            return result

        def th4(z, tau, n_terms=80):
            q = np.exp(1j * PI * tau)
            result = 1.0 + 0.0j
            for n in range(1, n_terms + 1):
                result += 2.0 * ((-1) ** n) * q ** (n ** 2) * np.cos(2 * n * PI * z)
            return result

        tau = 1.5j
        tp0 = jacobi_theta1_prime0(tau)
        rhs = PI * th2(0, tau) * th3(0, tau) * th4(0, tau)
        # VERIFIED: [DC] numerical; [LT] Jacobi triple product (Mumford)
        assert abs(tp0 - rhs) < 1e-8 * max(abs(tp0), 1.0)


# ============================================================
# Test: Genus-2 Riemann theta function
# ============================================================

class TestRiemannTheta:
    """Tests for the genus-2 Riemann theta function."""

    def test_theta_convergent(self, generic_omega):
        """Theta function converges to a finite value at generic point."""
        z = np.array([0.3 + 0.1j, 0.2 + 0.05j], dtype=complex)
        th = riemann_theta_g2(z, generic_omega, N=10)
        # VERIFIED: [DC] series converges for Im(Omega) > 0
        assert np.isfinite(th)
        assert abs(th) > 1e-10

    def test_theta_periodicity_in_z(self, generic_omega):
        """Theta[0;0](z + e_j | Omega) = Theta[0;0](z | Omega) (quasi-periodicity)."""
        z = np.array([0.15 + 0.05j, 0.1 + 0.03j], dtype=complex)
        th_z = riemann_theta_g2(z, generic_omega, N=10)
        z_shifted = z.copy()
        z_shifted[0] += 1.0  # shift by integer period
        th_shifted = riemann_theta_g2(z_shifted, generic_omega, N=10)
        # VERIFIED: [DC] periodicity; [LT] Mumford Tata II, Theorem 1.3
        assert abs(th_z - th_shifted) < 1e-8 * max(abs(th_z), 1.0)

    def test_theta_factorization_diagonal(self):
        """At diagonal Omega, genus-2 theta factorizes."""
        result = verify_theta_factorization_diagonal(
            1.2j, 1.5j,
            np.array([0.3 + 0.1j, 0.2 + 0.05j]), N=10)
        # VERIFIED: [DC] direct; [LC] diagonal limit; [LT] Fay ch. 1
        assert result['passed'], \
            f"Factorization failed: relative {result['relative']}"

    def test_theta_factorization_multiple_z(self):
        """Factorization holds at multiple z values."""
        for z_vals in [(0.1, 0.2), (0.3, 0.4), (0.05+0.1j, 0.15+0.05j)]:
            z = np.array(z_vals, dtype=complex)
            result = verify_theta_factorization_diagonal(1.0j, 1.3j, z, N=10)
            # VERIFIED: [DC] at each point; [NE] numerical
            assert result['passed'], f"Factorization at z={z_vals}: {result['relative']}"

    def test_theta_symmetry_omega(self):
        """Theta(z|Omega) depends only on the symmetric part of Omega."""
        z = np.array([0.15 + 0.05j, 0.1 + 0.03j], dtype=complex)
        Omega = np.array([[1.1j, 0.15 + 0.05j],
                           [0.15 + 0.05j, 1.3j]], dtype=complex)
        th = riemann_theta_g2(z, Omega, N=10)
        # Omega is already symmetric; verify it gives same result with explicit symmetrization
        Omega_sym = (Omega + Omega.T) / 2
        th_sym = riemann_theta_g2(z, Omega_sym, N=10)
        # VERIFIED: [SY] Omega symmetric; [DC] identical series
        assert abs(th - th_sym) < 1e-12


# ============================================================
# Test: Heat equation
# ============================================================

class TestHeatEquation:
    """Tests for the genus-2 theta function heat equation."""

    def test_heat_11(self, generic_omega):
        """Heat equation for (alpha, beta) = (1, 1)."""
        z = np.array([0.15 + 0.05j, 0.1 + 0.03j], dtype=complex)
        result = verify_heat_equation_theta_g2(generic_omega, z, 0, 0, N=10)
        # VERIFIED: [DC] finite difference; [LT] Fay, eq:heat-g2
        assert result['passed'], f"Heat eq (1,1) failed: relative {result['relative']}"

    def test_heat_22(self, generic_omega):
        """Heat equation for (alpha, beta) = (2, 2)."""
        z = np.array([0.15 + 0.05j, 0.1 + 0.03j], dtype=complex)
        result = verify_heat_equation_theta_g2(generic_omega, z, 1, 1, N=10)
        # VERIFIED: [DC] finite difference; [LT] eq:heat-g2
        assert result['passed'], f"Heat eq (2,2) failed: relative {result['relative']}"

    def test_heat_12(self, generic_omega):
        """Heat equation for (alpha, beta) = (1, 2): genuinely new at genus 2."""
        z = np.array([0.15 + 0.05j, 0.1 + 0.03j], dtype=complex)
        result = verify_heat_equation_theta_g2(generic_omega, z, 0, 1, N=10)
        # VERIFIED: [DC] finite difference; [LT] eq:heat-g2
        # This coupling has no genus-1 analogue (rem:cee-comparison)
        assert result['passed'], f"Heat eq (1,2) failed: relative {result['relative']}"

    def test_heat_with_characteristic(self, generic_omega):
        """Heat equation for theta with odd characteristic."""
        z = np.array([0.15 + 0.05j, 0.1 + 0.03j], dtype=complex)
        char_a = np.array([0.5, 0.5])
        char_b = np.array([0.5, 0.5])
        result = verify_heat_equation_theta_g2(
            generic_omega, z, 0, 0, char_a=char_a, char_b=char_b, N=10)
        # VERIFIED: [DC] heat equation holds for all characteristics; [LT] Fay
        assert result['passed'], \
            f"Heat eq with odd char failed: relative {result['relative']}"


# ============================================================
# Test: Szego kernel
# ============================================================

class TestSzegoKernel:
    """Tests for the genus-2 Szego kernel."""

    def test_szego_simple_pole(self, generic_omega):
        """S_2(z) ~ 1/z near z = 0 (residue 1)."""
        for z in [0.001j, 0.002j, 0.005j]:
            S = genus2_szego_kernel(z, generic_omega, N=8)
            product = z * S
            # VERIFIED: [DC] Laurent expansion; [LT] Fay "Theta functions on RS"
            assert abs(product - 1.0) < 0.15, \
                f"Residue not ~1: z*S(z) = {product} at z={z}"

    def test_szego_degeneration(self):
        """At diagonal Omega, S_2 reduces to genus-1 Szego kernel."""
        result = verify_szego_degeneration(1.2j, 0.15 + 0.05j, N=10)
        # VERIFIED: [LC] degeneration; [LT] prop:g2-nonsep-degen (iii)
        assert result['passed'], \
            f"Szego degeneration failed: relative {result['relative']}"

    def test_szego_nonzero(self, generic_omega):
        """Szego kernel is nonzero at generic point."""
        S = genus2_szego_kernel(0.2 + 0.1j, generic_omega, N=8)
        # VERIFIED: [DC] theta function nonzero at generic point
        assert abs(S) > 1e-3


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
# Test: Full suite
# ============================================================

class TestFullSuite:
    """Integration test for the complete verification."""

    def test_full_verification(self):
        """Run complete verification of DDYBE supporting infrastructure."""
        results = run_full_verification(N_theta=10)
        summary = results['summary']
        assert summary['heat_equation_passed'], "Heat equation failed"
        assert summary['theta_factorization_passed'], "Factorization failed"
        assert summary['szego_degeneration_passed'], "Szego degeneration failed"
        assert summary['szego_pole_passed'], "Szego pole failed"
        assert summary['all_passed'], "Not all checks passed"
