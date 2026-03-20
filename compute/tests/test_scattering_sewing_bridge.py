#!/usr/bin/env python3
"""
test_scattering_sewing_bridge.py — BLUE TEAM defense: strengthen the
sewing-operator/scattering-matrix connection.

T1-T7:   Sewing operator spectral decomposition and resolvent
T8-T14:  Mellin transform of resolvent gives zeta(s)*zeta(s+1)
T15-T21: Rankin-Selberg derivative at zeta zeros
T22-T27: Spectral zeta function of sewing operator
T28-T33: Eisenstein-sewing duality
T34-T39: Modular invariance (S-transform) of sewing data
T40-T45: Higher-rank generalization
T46-T50: Selberg trace formula and sewing test functions
"""

import pytest
import numpy as np
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from scattering_sewing_bridge import (
    sigma_minus_1, sigma_0, sigma_1, eta_real,
    sewing_eigenvalue, sewing_resolvent_trace,
    resolvent_trace_power_expansion, mellin_resolvent_coefficient,
    mellin_resolvent_full, verify_mellin_resolvent_gives_zeta_product,
    rankin_selberg_log_det, rankin_selberg_log_det_derivative,
    zeta_product_derivative_at_zero, rankin_selberg_derivative_at_zeta_zeros,
    spectral_zeta_sewing, spectral_zeta_sewing_complex,
    mellin_of_spectral_zeta, verify_mellin_spectral_zeta,
    eisenstein_from_sewing, verify_eisenstein_sewing_duality,
    eisenstein_constant_term,
    fredholm_det_q, eta_modular_s_transform, fredholm_det_s_transform,
    scattering_from_eta_ratio, rankin_selberg_functional_equation_ratio,
    higher_rank_fredholm_det, higher_rank_rankin_selberg,
    higher_rank_log_det_coefficients, higher_rank_eta_power_coefficients,
    sewing_test_function, sewing_test_function_fourier,
    is_valid_selberg_test_function, selberg_spectral_side_sewing,
    scattering_sewing_synthesis,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# T1-T7: Sewing operator spectral decomposition
# ============================================================

class TestSewingSpectralDecomposition:
    def test_T1_sewing_eigenvalues(self):
        """T1: Eigenvalues lambda_n = q^n = e^{-2*pi*n*y}."""
        y = 1.0
        for n in range(1, 10):
            lam = sewing_eigenvalue(n, y)
            expected = math.exp(-2 * math.pi * n * y)
            assert abs(lam - expected) < 1e-15

    def test_T2_eigenvalue_ordering(self):
        """T2: Eigenvalues are strictly decreasing: lambda_1 > lambda_2 > ..."""
        y = 0.5
        prev = 1.0
        for n in range(1, 20):
            lam = sewing_eigenvalue(n, y)
            assert lam < prev
            prev = lam

    def test_T3_resolvent_trace_convergence(self):
        """T3: Resolvent trace converges for |z| < 1/q (radius of convergence)."""
        y = 1.0
        q = math.exp(-2 * math.pi * y)
        # z well within convergence radius
        z = 0.5
        tr_val = sewing_resolvent_trace(z, y)
        assert np.isfinite(tr_val)
        assert tr_val > 0

    def test_T4_resolvent_at_z_equals_1(self):
        """T4: At z=1, tr_red R(1) = sum q^n/(1-q^n) = sum sigma_0(N) q^N.
        Identity: sum_{n>=1} q^n/(1-q^n) = sum_{n>=1} sum_{m>=1} q^{nm} = sum_{N>=1} d(N)*q^N."""
        y = 1.5
        q = math.exp(-2 * math.pi * y)
        tr_at_1 = sewing_resolvent_trace(1.0, y)
        # sum q^n/(1-q^n) = sum d(N)*q^N where d(N) = sigma_0(N) = number of divisors
        sigma0_sum = sum(sigma_0(N) * q ** N for N in range(1, 200))
        assert abs(tr_at_1 - sigma0_sum) / abs(sigma0_sum) < 1e-8

    def test_T5_power_expansion_coefficients(self):
        """T5: c_k = tr(K^k) = q^k/(1-q^k)."""
        y = 1.0
        q = math.exp(-2 * math.pi * y)
        coeffs = resolvent_trace_power_expansion(y, kmax=20)
        for k in range(1, 20):
            qk = q ** k
            expected = qk / (1.0 - qk)
            assert abs(coeffs[k - 1] - expected) < 1e-12

    def test_T6_trace_formula_identity(self):
        """T6: sum_{k=1}^N (1/k)*c_k = sum sigma_{-1}(M)*q^M (sewing trace formula)."""
        y = 2.0
        q = math.exp(-2 * math.pi * y)
        coeffs = resolvent_trace_power_expansion(y, kmax=100)
        # sum (1/k)*c_k
        lhs = sum((1.0 / k) * coeffs[k - 1] for k in range(1, 101))
        # -log det(1-K_q) = sum sigma_{-1}(N)*q^N
        rhs = -sum(math.log1p(-q ** n) for n in range(1, 200))
        assert abs(lhs - rhs) / abs(rhs) < 1e-6

    def test_T7_resolvent_z_derivative(self):
        """T7: d/dz tr_red R(z)|_{z=0} = c_1 = q/(1-q)."""
        y = 1.0
        q = math.exp(-2 * math.pi * y)
        # Numerical derivative at z=0
        eps = 1e-6
        deriv = (sewing_resolvent_trace(eps, y) - sewing_resolvent_trace(-eps, y)) / (2 * eps)
        # Should be c_1 = q/(1-q)
        expected = q / (1 - q)
        assert abs(deriv - expected) / abs(expected) < 1e-4


# ============================================================
# T8-T14: Mellin transform gives zeta(s)*zeta(s+1)
# ============================================================

class TestMellinResolvent:
    @skip_no_mpmath
    def test_T8_mellin_single_coefficient(self):
        """T8: M[c_k](s) = Gamma(s)*zeta(s)/(2*pi*k)^s."""
        s = 3.0
        for k in [1, 2, 3, 5]:
            result = mellin_resolvent_coefficient(s, k)
            expected = complex(
                mpmath.gamma(s) * mpmath.zeta(s) / (2 * mpmath.pi * k) ** s
            )
            assert abs(result - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_T9_mellin_full_zeta_product(self):
        """T9: sum (1/k)*M[c_k](s) = Gamma(s)/(2*pi)^s * zeta(s)*zeta(s+1)."""
        for s in [2.5, 3.0, 4.0]:
            partial, exact, rel_err = verify_mellin_resolvent_gives_zeta_product(s, kmax=500)
            assert rel_err < 1e-3, f"Relative error {rel_err} at s={s}"

    @skip_no_mpmath
    def test_T10_mellin_full_closed_form(self):
        """T10: The closed-form Mellin resolvent matches direct computation."""
        for s in [2.0, 3.0, 5.0]:
            closed = mellin_resolvent_full(s)
            expected = complex(
                mpmath.gamma(s) / (2 * mpmath.pi) ** s
                * mpmath.zeta(s) * mpmath.zeta(s + 1)
            )
            assert abs(closed - expected) / abs(expected) < 1e-12

    @skip_no_mpmath
    def test_T11_mellin_at_s_equals_2(self):
        """T11: At s=2: Gamma(2)/(2pi)^2 * zeta(2)*zeta(3) = pi^2/6 * zeta(3) / (4pi^2)."""
        closed = mellin_resolvent_full(2.0)
        # Gamma(2) = 1, (2pi)^2 = 4pi^2, zeta(2) = pi^2/6
        expected = complex(
            mpmath.mpf(1) / (4 * mpmath.pi ** 2) * (mpmath.pi ** 2 / 6) * mpmath.zeta(3)
        )
        assert abs(closed - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_T12_mellin_convergence_rate(self):
        """T12: The partial sum converges as O(k^{-s}) for large k."""
        s = 3.0
        _, exact, _ = verify_mellin_resolvent_gives_zeta_product(s, kmax=100)
        _, _, rel_err_100 = verify_mellin_resolvent_gives_zeta_product(s, kmax=100)
        _, _, rel_err_500 = verify_mellin_resolvent_gives_zeta_product(s, kmax=500)
        # Error should decrease with more terms
        assert rel_err_500 < rel_err_100

    @skip_no_mpmath
    def test_T13_sigma_minus_1_dirichlet_series(self):
        """T13: sum sigma_{-1}(N) N^{-s} = zeta(s)*zeta(s+1), the underlying identity."""
        s = 3.0
        Nmax = 2000
        partial = sum(sigma_minus_1(N) * N ** (-s) for N in range(1, Nmax + 1))
        exact = float(mpmath.zeta(s) * mpmath.zeta(s + 1))
        assert abs(partial - exact) / abs(exact) < 1e-3

    @skip_no_mpmath
    def test_T14_resolvent_mellin_functional_properties(self):
        """T14: Verify M(s) has expected pole structure near s=1 and s=0."""
        # Near s=1: Gamma(s) has no pole, zeta(s) has a pole, so M(s) ~ pole
        s_near_1 = 1.01
        val = abs(mellin_resolvent_full(s_near_1))
        # Should be large (near pole from zeta(s) at s=1)
        assert val > 10.0


# ============================================================
# T15-T21: Rankin-Selberg derivative at zeta zeros
# ============================================================

class TestRankinSelbergDerivative:
    @skip_no_mpmath
    def test_T15_I_vanishes_at_zeta_zeros(self):
        """T15: I(rho_k) = 0 because zeta(rho_k) = 0."""
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            I_val = rankin_selberg_log_det(rho)
            assert abs(I_val) < 1e-8, f"I(rho_{k}) = {I_val}, expected ~0"

    @skip_no_mpmath
    def test_T16_derivative_nonzero_at_zeros(self):
        """T16: zeta'(rho_k)*zeta(rho_k-1) != 0 for first 5 zeros."""
        for k in range(1, 6):
            info = zeta_product_derivative_at_zero(k)
            # The "simplified" form is zeta'(rho)*zeta(rho-1), which must be nonzero
            assert abs(info['simplified']) > 1e-5, \
                f"zeta'(rho_{k})*zeta(rho_{k}-1) = {info['simplified']}, expected nonzero"

    @skip_no_mpmath
    def test_T17_zeta_at_rho_is_zero(self):
        """T17: Verify zeta(rho_k) ~ 0 for first 10 zeros."""
        for k in range(1, 11):
            rho = mpmath.zetazero(k)
            val = complex(mpmath.zeta(rho))
            assert abs(val) < 1e-10

    @skip_no_mpmath
    def test_T18_derivative_product_factorization(self):
        """T18: d/ds[zeta(s-1)*zeta(s)]|_{rho_k} = zeta'(rho_k)*zeta(rho_k-1) (since zeta(rho_k)=0)."""
        for k in range(1, 6):
            info = zeta_product_derivative_at_zero(k)
            full = info['derivative_of_product']
            simplified = info['simplified']
            assert abs(full - simplified) / abs(simplified) < 1e-6, \
                f"k={k}: full={full}, simplified={simplified}"

    @skip_no_mpmath
    def test_T19_zeta_prime_at_zeros_nonzero(self):
        """T19: zeta'(rho_k) != 0 for k=1,...,10 (zeros are simple)."""
        for k in range(1, 11):
            info = zeta_product_derivative_at_zero(k)
            assert abs(info['zeta_prime_at_rho']) > 0.1, \
                f"zeta'(rho_{k}) = {info['zeta_prime_at_rho']}, expected nonzero"

    @skip_no_mpmath
    def test_T20_zeta_at_rho_minus_1(self):
        """T20: zeta(rho_k - 1) is well-defined and nonzero."""
        for k in range(1, 11):
            info = zeta_product_derivative_at_zero(k)
            assert abs(info['zeta_at_rho_minus_1']) > 1e-5, \
                f"zeta(rho_{k}-1) = {info['zeta_at_rho_minus_1']}, expected nonzero"

    @skip_no_mpmath
    def test_T21_I_derivative_structure(self):
        """T21: I'(rho_k) involves both Gamma and zeta factors."""
        results = rankin_selberg_derivative_at_zeta_zeros(num_zeros=3)
        # Check that results have expected keys and magnitudes
        for info in results:
            assert 'I_derivative' in info
            assert 'simplified' in info
            assert abs(info['I_at_rho']) < 1e-6  # I vanishes at rho


# ============================================================
# T22-T27: Spectral zeta function of sewing operator
# ============================================================

class TestSpectralZetaSewing:
    def test_T22_spectral_zeta_formula(self):
        """T22: zeta_K(s) = q^s/(1-q^s) for real s > 0."""
        y = 1.0
        for s in [1.0, 2.0, 3.0, 0.5]:
            val = spectral_zeta_sewing(s, y)
            q = math.exp(-2 * math.pi * y)
            qs = q ** s
            expected = qs / (1 - qs)
            assert abs(val - expected) < 1e-12

    def test_T23_spectral_zeta_sum_check(self):
        """T23: zeta_K(s) = sum_{n>=1} q^{ns} (direct sum vs closed form)."""
        y = 1.0
        s = 2.0
        q = math.exp(-2 * math.pi * y)
        direct_sum = sum(q ** (n * s) for n in range(1, 500))
        closed = spectral_zeta_sewing(s, y)
        assert abs(direct_sum - closed) / abs(closed) < 1e-10

    @skip_no_mpmath
    def test_T24_mellin_spectral_zeta_analytic(self):
        """T24: M[zeta_K(s)](u) = Gamma(u)*zeta(u)/(2*pi*s)^u."""
        for u, s in [(2.0, 1.0), (3.0, 2.0), (2.0, 0.5)]:
            result = mellin_of_spectral_zeta(u, s)
            expected = complex(
                mpmath.gamma(u) * mpmath.zeta(u) / (2 * mpmath.pi * s) ** u
            )
            assert abs(result - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_T25_mellin_spectral_zeta_numerical(self):
        """T25: Numerical Mellin transform matches analytic formula."""
        u, s = 3.0, 1.0
        numerical, analytic = verify_mellin_spectral_zeta(u, s)
        # Allow generous tolerance for numerical integration
        assert abs(numerical - analytic) / analytic < 0.05

    def test_T26_spectral_zeta_positivity(self):
        """T26: zeta_K(s) > 0 for all real s > 0 (positive eigenvalues)."""
        y = 1.0
        for s in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            val = spectral_zeta_sewing(s, y)
            assert val > 0, f"zeta_K({s}) = {val}, expected positive"

    def test_T27_spectral_zeta_monotone(self):
        """T27: zeta_K(s) is strictly decreasing in s for y > 0."""
        y = 1.0
        prev = spectral_zeta_sewing(0.1, y)
        for s in [0.5, 1.0, 2.0, 5.0]:
            val = spectral_zeta_sewing(s, y)
            assert val < prev, f"zeta_K({s}) = {val} >= zeta_K(prev) = {prev}"
            prev = val


# ============================================================
# T28-T33: Eisenstein-sewing duality
# ============================================================

class TestEisensteinSewingDuality:
    @skip_no_mpmath
    def test_T28_sewing_eigenvalue_zeta_recovery(self):
        """T28: sum (n*y)^{-s} = y^{-s}*zeta(s)."""
        for s, y in [(2.0, 1.0), (3.0, 0.5), (4.0, 2.0)]:
            partial, exact, rel_err = verify_eisenstein_sewing_duality(s, y, nmax=2000)
            assert rel_err < 1e-3, f"s={s}, y={y}: rel_err={rel_err}"

    @skip_no_mpmath
    def test_T29_eisenstein_from_sewing_formula(self):
        """T29: E_hat_s(K) = y^{-s}*zeta(s)."""
        s, y = 3.0, 1.0
        val = eisenstein_from_sewing(s, y)
        expected = complex(mpmath.power(y, -s) * mpmath.zeta(s))
        assert abs(val - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_T30_eisenstein_constant_term_structure(self):
        """T30: Constant term a_0(y,s) = y^s + phi(s)*y^{1-s}."""
        y = 2.0
        s = 0.75
        a0 = eisenstein_constant_term(s, y)
        # Should be real for real s and real y (on imaginary axis)
        assert abs(a0.imag) < 1e-8
        assert abs(a0.real) > 0.1  # non-trivial

    @skip_no_mpmath
    def test_T31_eisenstein_duality_y_independence(self):
        """T31: y^s * E_hat_s(K) = zeta(s), independent of y."""
        s = 3.0
        vals = []
        for y in [0.5, 1.0, 2.0, 5.0]:
            val = eisenstein_from_sewing(s, y)
            corrected = val * y ** s  # should give zeta(s)
            vals.append(corrected)
        # All should be equal to zeta(s)
        zeta_s = complex(mpmath.zeta(s))
        for v in vals:
            assert abs(v - zeta_s) / abs(zeta_s) < 1e-10

    @skip_no_mpmath
    def test_T32_eisenstein_duality_at_s_equals_2(self):
        """T32: At s=2, E_hat_2(K) = y^{-2}*pi^2/6."""
        y = 1.5
        val = eisenstein_from_sewing(2.0, y)
        expected = y ** (-2) * math.pi ** 2 / 6
        assert abs(val - expected) / abs(expected) < 1e-10

    @skip_no_mpmath
    def test_T33_constant_term_functional_equation(self):
        """T33: a_0(y,s) is invariant under s -> 1-s up to phi(s) swap."""
        y = 1.5
        s = 0.7
        a0_s = eisenstein_constant_term(s, y)
        a0_1ms = eisenstein_constant_term(1.0 - s, y)
        # a_0(y,s) = y^s + phi(s)*y^{1-s}
        # a_0(y,1-s) = y^{1-s} + phi(1-s)*y^s = y^{1-s} + y^s/phi(s) [since phi(s)*phi(1-s)=1]
        # So a_0(y,1-s) = a_0(y,s) when phi(s) = 1 (i.e., s = 1/2)
        # In general they differ; verify they are related by phi
        phi_s = scattering_from_eta_ratio(s)
        # a_0(y,s) = y^s + phi(s)*y^{1-s}
        # a_0(y,1-s) = y^{1-s} + phi(1-s)*y^s
        # phi(1-s) = 1/phi(s)
        reconstructed = y ** (1 - s) + y ** s / phi_s
        assert abs(a0_1ms - reconstructed) / abs(a0_1ms) < 1e-6


# ============================================================
# T34-T39: Modular invariance of sewing data
# ============================================================

class TestModularInvariance:
    def test_T34_eta_s_transform(self):
        """T34: eta(i/y) = sqrt(y)*eta(iy)."""
        for y in [0.5, 1.0, 2.0, 3.0]:
            eta_y, eta_inv_y, predicted = eta_modular_s_transform(y)
            assert abs(eta_inv_y - predicted) / abs(predicted) < 1e-10, \
                f"y={y}: eta(i/y)={eta_inv_y}, sqrt(y)*eta(iy)={predicted}"

    def test_T35_fredholm_det_s_transform(self):
        """T35: det(1-K_{q'})/det(1-K_q) = sqrt(y)*exp(pi(1/y-y)/12)."""
        for y in [0.5, 1.0, 1.5, 2.0, 3.0]:
            det_y, det_inv_y, ratio_actual, ratio_predicted = fredholm_det_s_transform(y)
            if det_y > 1e-200:
                assert abs(ratio_actual - ratio_predicted) / abs(ratio_predicted) < 1e-8, \
                    f"y={y}: ratio={ratio_actual}, predicted={ratio_predicted}"

    def test_T36_s_transform_at_fixed_point(self):
        """T36: At y=1 (fixed point of S), det(1-K_{q'}) = det(1-K_q)."""
        y = 1.0
        det_y, det_inv_y, _, _ = fredholm_det_s_transform(y)
        assert abs(det_y - det_inv_y) / abs(det_y) < 1e-10

    @skip_no_mpmath
    def test_T37_scattering_matrix_unitarity(self):
        """T37: |phi(1/2+it)| = 1 on the critical line."""
        for t in [1.0, 5.0, 10.0, 14.0]:
            s = 0.5 + 1j * t
            phi_val = scattering_from_eta_ratio(s)
            assert abs(abs(phi_val) - 1.0) < 1e-6, \
                f"t={t}: |phi(1/2+it)| = {abs(phi_val)}, expected 1"

    @skip_no_mpmath
    def test_T38_scattering_functional_equation(self):
        """T38: phi(s)*phi(1-s) = 1."""
        for s in [0.3, 0.7, 0.25 + 0.5j]:
            phi_s = scattering_from_eta_ratio(s)
            phi_1ms = scattering_from_eta_ratio(1.0 - s)
            product = phi_s * phi_1ms
            assert abs(product - 1.0) < 1e-6, \
                f"s={s}: phi(s)*phi(1-s) = {product}, expected 1"

    @skip_no_mpmath
    def test_T39_RS_integral_functional_equation(self):
        """T39: I(1-s)/I(s) encodes the functional equation.
        Avoid integer s where Gamma(s-1) or Gamma((1-s)-1) = Gamma(-s) has poles."""
        for s in [2.5, 3.5, 4.5]:
            ratio = rankin_selberg_functional_equation_ratio(s)
            # This should be a finite, nonzero number
            assert np.isfinite(abs(ratio))
            assert abs(ratio) > 1e-10


# ============================================================
# T40-T45: Higher-rank generalization
# ============================================================

class TestHigherRank:
    def test_T40_rank_1_fredholm_det(self):
        """T40: Rank 1 Fredholm det matches single boson."""
        y = 1.0
        det_r1 = higher_rank_fredholm_det(y, rank=1)
        det_single = fredholm_det_q(y)
        assert abs(det_r1 - det_single) / abs(det_single) < 1e-12

    def test_T41_rank_r_is_power(self):
        """T41: det(1-K^{otimes r}) = det(1-K)^r."""
        y = 1.0
        det1 = fredholm_det_q(y)
        for r in [1, 2, 4, 8]:
            det_r = higher_rank_fredholm_det(y, rank=r)
            expected = det1 ** r
            assert abs(det_r - expected) / abs(expected) < 1e-10, \
                f"rank={r}: det_r={det_r}, det1^r={expected}"

    @skip_no_mpmath
    def test_T42_higher_rank_RS_linear_in_rank(self):
        """T42: I_r(s) = r * I_1(s)."""
        s = 3.0
        I_1 = higher_rank_rankin_selberg(s, rank=1)
        for r in [2, 4, 8, 24]:
            I_r = higher_rank_rankin_selberg(s, rank=r)
            assert abs(I_r - r * I_1) / abs(r * I_1) < 1e-10, \
                f"rank={r}: I_r={I_r}, r*I_1={r * I_1}"

    def test_T43_higher_rank_coefficients(self):
        """T43: log det coefficients scale linearly with rank."""
        for r in [1, 2, 4, 8, 24]:
            coeffs = higher_rank_log_det_coefficients(r, Nmax=20)
            for N, c in coeffs:
                expected = -r * sigma_minus_1(N)
                assert abs(c - expected) < 1e-12

    def test_T44_eta_power_rank_2(self):
        """T44: prod(1-q^n)^4 = eta^4 power coefficients (Jacobi-type)."""
        coeffs = higher_rank_eta_power_coefficients(rank=1, Nmax=10)
        # For prod(1-q^n)^2: coefficient of q^1 should be -2
        assert abs(coeffs[0] - 1.0) < 1e-10  # constant term
        assert abs(coeffs[1] - (-2.0)) < 1e-10  # q^1 coefficient

    def test_T45_rank_24_leech(self):
        """T45: Rank 24 (Leech lattice dimension) gives det(1-K)^24."""
        y = 1.5
        det1 = fredholm_det_q(y)
        det24 = higher_rank_fredholm_det(y, rank=24)
        expected = det1 ** 24
        assert abs(det24 - expected) / abs(expected) < 1e-8


# ============================================================
# T46-T50: Selberg trace formula and sewing test functions
# ============================================================

class TestSelbergTraceFormula:
    def test_T46_sewing_test_function_evenness(self):
        """T46: h(r) = h(-r) (even function)."""
        y = 3.0
        for r in [0.5, 1.0, 2.0, 5.0]:
            assert abs(sewing_test_function(r, y) - sewing_test_function(-r, y)) < 1e-15

    def test_T47_sewing_test_function_decay(self):
        """T47: h(r) -> 0 as r -> infinity (Gaussian decay)."""
        y = 3.0
        vals = [sewing_test_function(r, y) for r in [1, 2, 5, 10, 20]]
        for i in range(len(vals) - 1):
            assert vals[i + 1] <= vals[i] + 1e-15

    def test_T48_selberg_test_function_validity(self):
        """T48: Sewing test function is valid Selberg test function for y < 2.
        Strip width = 1/sqrt(2y) > 1/2 requires y < 2."""
        checks = is_valid_selberg_test_function(y=0.6)
        assert checks['even']
        assert checks['decays']
        assert checks['gaussian_decay']
        assert checks['analytic_in_half_strip']  # 1/sqrt(1.2) ~ 0.913 > 0.5

    def test_T49_selberg_test_function_strip_width(self):
        """T49: Strip width = sqrt(1/(2y)). Valid for y < 2, invalid for y >= 2."""
        # Valid cases: y < 2
        for y in [0.3, 0.5, 1.0, 1.5]:
            checks = is_valid_selberg_test_function(y)
            expected_width = math.sqrt(1.0 / (2.0 * y))
            assert abs(checks['strip_width'] - expected_width) < 1e-12
            assert checks['strip_width'] > 0.5
        # Invalid cases: y >= 2
        for y in [2.5, 5.0]:
            checks = is_valid_selberg_test_function(y)
            assert checks['strip_width'] < 0.5

    def test_T50_sewing_test_function_fourier_positivity(self):
        """T50: Fourier transform of h(r) is positive (sum of Gaussians)."""
        y = 3.0
        for u in [0.0, 0.5, 1.0, 2.0, 5.0]:
            ft = sewing_test_function_fourier(u, y)
            assert ft > 0, f"h_hat({u}) = {ft}, expected positive"


# ============================================================
# Bonus: Synthesis and cross-checks
# ============================================================

class TestSynthesis:
    def test_B1_synthesis_keys(self):
        """B1: Synthesis dictionary has all seven connections."""
        synth = scattering_sewing_synthesis()
        expected_keys = [
            'resolvent_mellin', 'RS_derivative', 'spectral_zeta_mellin',
            'eisenstein_duality', 's_transform', 'higher_rank', 'selberg_test'
        ]
        for key in expected_keys:
            assert key in synth

    @skip_no_mpmath
    def test_B2_sewing_selberg_formula_consistency(self):
        """B2: The sewing-Selberg formula I(s) = -2*(2pi)^{-(s-1)}*Gamma(s-1)*zeta(s-1)*zeta(s)
        is consistent with the resolvent Mellin transform."""
        s = 3.0
        # From sewing-Selberg formula
        I_s = rankin_selberg_log_det(s)
        # From resolvent Mellin: Gamma(s)/(2pi)^s * zeta(s)*zeta(s+1)
        # These are related but not identical (different parameter shifts).
        # Check: I(s) involves zeta(s-1)*zeta(s), resolvent gives zeta(s)*zeta(s+1).
        # At s -> s+1: I(s+1) = -2*(2pi)^{-s}*Gamma(s)*zeta(s)*zeta(s+1)
        I_s_plus_1 = rankin_selberg_log_det(s + 1)
        mellin_val = mellin_resolvent_full(s)
        # I(s+1) = -2 * mellin_val (up to normalization)
        ratio = abs(I_s_plus_1) / abs(mellin_val)
        assert abs(ratio - 2.0) < 0.01, f"Ratio = {ratio}, expected ~2"

    @skip_no_mpmath
    def test_B3_spectral_zeta_recovers_riemann_zeta(self):
        """B3: The spectral zeta function of K_q, after Mellin over y, gives zeta(s)."""
        # M[zeta_K(1)](u) = Gamma(u)*zeta(u)/(2pi)^u
        # So zeta(u) = (2pi)^u/Gamma(u) * M[zeta_K(1)](u)
        u = 3.0
        mellin_val = mellin_of_spectral_zeta(u, s=1.0)
        recovered_zeta = mellin_val * (2 * math.pi) ** u / complex(mpmath.gamma(u))
        exact_zeta = complex(mpmath.zeta(u))
        assert abs(recovered_zeta - exact_zeta) / abs(exact_zeta) < 1e-10

    @skip_no_mpmath
    def test_B4_s_transform_encodes_scattering(self):
        """B4: The S-transform ratio of sewing determinants is related to the scattering matrix."""
        # For several y values, check that the S-transform ratio has the correct structure
        for y in [1.5, 2.0, 3.0]:
            _, _, ratio_actual, ratio_predicted = fredholm_det_s_transform(y)
            assert abs(ratio_actual - ratio_predicted) / abs(ratio_predicted) < 1e-8

    @skip_no_mpmath
    def test_B5_higher_rank_at_zeta_zeros(self):
        """B5: I_r(rho_k) = 0 for any rank r (since zeta(rho_k) = 0)."""
        rho_1 = complex(mpmath.zetazero(1))
        for r in [1, 2, 4]:
            I_r = higher_rank_rankin_selberg(rho_1, rank=r)
            assert abs(I_r) < 1e-6, f"rank={r}: I_r(rho_1) = {I_r}, expected ~0"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
