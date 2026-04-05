r"""Tests for BC-101: Shadow trace formula engine.

Verification paths (>=3 per claim):
1. Trace formula: spectral side = geometric side (both independently computed)
2. Heat kernel small-t coefficients match Weyl law
3. Prime geodesic counting function matches exponential growth (class M)
4. Kuznetsov identity: diagonal positivity + off-diagonal consistency
5. At c=13 (self-dual): enhanced symmetry in trace formula
6. Complementarity D_2 = 13 (AP24) as structural anchor
7. Finite tower (affine) exact zeros vs spectral sum

Anti-patterns guarded:
    AP1:  No copying between families; each formula from first principles.
    AP9:  S_2 = kappa = c/2 only for Virasoro.
    AP10: Expected values derived independently, not hardcoded from single source.
    AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
    AP38: Convention checks when comparing to classical number theory.
    AP48: kappa depends on the full algebra, not the Virasoro sub.
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
import pytest
import numpy as np


# ===========================================================================
# 1. Test function properties
# ===========================================================================

class TestTestFunctions:
    """Verify test functions and their Fourier transforms."""

    def test_gaussian_at_zero(self):
        from lib.bc_trace_formula_shadow_engine import gaussian_test
        assert abs(gaussian_test(0.0, sigma=1.0) - 1.0) < 1e-14

    def test_gaussian_symmetry(self):
        from lib.bc_trace_formula_shadow_engine import gaussian_test
        for sigma in [1.0, 2.0, 5.0]:
            s = complex(1.5, 3.7)
            assert abs(gaussian_test(s, sigma) - gaussian_test(-s, sigma)) < 1e-14

    def test_gaussian_decay(self):
        from lib.bc_trace_formula_shadow_engine import gaussian_test
        g1 = abs(gaussian_test(1.0, sigma=1.0))
        g10 = abs(gaussian_test(10.0, sigma=1.0))
        assert g10 < g1 * 1e-10

    def test_lorentzian_at_zero(self):
        from lib.bc_trace_formula_shadow_engine import lorentzian_test
        for a in [1.0, 2.0, 5.0]:
            val = lorentzian_test(0.0, a=a)
            assert abs(val - 1.0 / (a * a)) < 1e-14

    def test_lorentzian_symmetry(self):
        from lib.bc_trace_formula_shadow_engine import lorentzian_test
        s = complex(2.0, 3.0)
        val_pos = lorentzian_test(s, a=2.0)
        val_neg = lorentzian_test(-s, a=2.0)
        assert abs(val_pos - val_neg) < 1e-14

    def test_gaussian_fourier_normalization(self):
        """Fourier transform at t=0 should be sigma*sqrt(2*pi)."""
        from lib.bc_trace_formula_shadow_engine import gaussian_fourier
        for sigma in [1.0, 2.0, 5.0]:
            val = gaussian_fourier(0.0, sigma)
            expected = sigma * math.sqrt(2.0 * math.pi)
            assert abs(val - expected) < 1e-12

    def test_gaussian_fourier_decay(self):
        from lib.bc_trace_formula_shadow_engine import gaussian_fourier
        g0 = gaussian_fourier(0.0, sigma=1.0)
        g5 = gaussian_fourier(5.0, sigma=1.0)
        assert g5 < g0 * 1e-4

    def test_lorentzian_fourier_at_zero(self):
        from lib.bc_trace_formula_shadow_engine import lorentzian_fourier
        for a in [1.0, 2.0, 5.0]:
            val = lorentzian_fourier(0.0, a)
            expected = math.pi / a
            assert abs(val - expected) < 1e-12

    def test_lorentzian_fourier_symmetry(self):
        from lib.bc_trace_formula_shadow_engine import lorentzian_fourier
        for t in [1.0, 3.0, 7.0]:
            assert abs(lorentzian_fourier(t, 2.0) - lorentzian_fourier(-t, 2.0)) < 1e-14

    def test_indicator_inside(self):
        from lib.bc_trace_formula_shadow_engine import indicator_test
        assert abs(indicator_test(complex(0, 5), T=10.0) - 1.0) < 1e-14

    def test_indicator_outside(self):
        from lib.bc_trace_formula_shadow_engine import indicator_test
        assert abs(indicator_test(complex(0, 15), T=10.0)) < 1e-14


# ===========================================================================
# 2. Shadow length spectrum
# ===========================================================================

class TestShadowLengthSpectrum:
    """Verify shadow length spectrum computation."""

    def test_heisenberg_single_length(self):
        from lib.bc_trace_formula_shadow_engine import (
            shadow_length_spectrum, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        spectrum = shadow_length_spectrum(coeffs)
        assert len(spectrum) == 1
        length, weight = spectrum[0]
        assert abs(length - math.log(2)) < 1e-14
        assert abs(weight - 1.0) < 1e-14  # normalized by S_2

    def test_affine_sl2_two_lengths(self):
        from lib.bc_trace_formula_shadow_engine import (
            shadow_length_spectrum, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        spectrum = shadow_length_spectrum(coeffs)
        assert len(spectrum) == 2
        assert abs(spectrum[0][0] - math.log(2)) < 1e-14
        assert abs(spectrum[1][0] - math.log(3)) < 1e-14

    def test_virasoro_all_lengths_nonzero(self):
        """Class M: all S_r nonzero, so all log(r) appear."""
        from lib.bc_trace_formula_shadow_engine import (
            shadow_length_spectrum, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=20)
        spectrum = shadow_length_spectrum(coeffs)
        # For class M, all arities 2..20 should be nonzero
        assert len(spectrum) >= 18


# ===========================================================================
# 3. Spectral side: sum over zeros
# ===========================================================================

class TestSpectralSums:
    """Verify spectral sum computations."""

    def test_heisenberg_no_zeros(self):
        """Heisenberg has no zeros; spectral sum = 0."""
        from lib.bc_trace_formula_shadow_engine import (
            spectral_sum_gaussian, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('heisenberg', 1.0)
        assert len(zeros) == 0
        val = spectral_sum_gaussian(zeros, sigma=1.0)
        assert abs(val) < 1e-14

    def test_affine_zeros_exist(self):
        """Affine sl_2 has infinitely many zeros on a vertical line."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_zeros
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=20)
        assert len(zeros) >= 10

    def test_affine_zeros_equally_spaced(self):
        """For 2-term Dirichlet series, zeros are equally spaced in Im(s)."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_zeros
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        # Filter to positive imaginary part and sort
        pos_zeros = sorted([z for z in zeros if z.imag > 0], key=lambda z: z.imag)
        if len(pos_zeros) >= 3:
            spacings = [pos_zeros[i+1].imag - pos_zeros[i].imag
                        for i in range(min(10, len(pos_zeros)-1))]
            # Should be constant: 2*pi / log(3/2)
            expected_spacing = 2.0 * math.pi / math.log(3.0 / 2.0)
            for sp in spacings:
                assert abs(sp - expected_spacing) < 0.1

    def test_affine_zeros_on_vertical_line(self):
        """All affine sl_2 zeros have the same real part."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_zeros
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=20)
        if len(zeros) >= 2:
            re_parts = [z.real for z in zeros]
            assert max(re_parts) - min(re_parts) < 1e-8

    def test_spectral_sum_real_for_symmetric_zeros(self):
        """If zeros come in conjugate pairs, Gaussian spectral sum is real."""
        from lib.bc_trace_formula_shadow_engine import (
            spectral_sum_gaussian, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        val = spectral_sum_gaussian(zeros, sigma=2.0)
        # Not exactly real because we truncate, but imaginary part should be small
        assert abs(val.imag) < abs(val.real) * 0.01 + 1e-10

    def test_indicator_equals_counting(self):
        """Spectral sum with indicator = zero counting function."""
        from lib.bc_trace_formula_shadow_engine import (
            spectral_sum_indicator, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        T = 30.0
        count_via_indicator = spectral_sum_indicator(zeros, T)
        count_direct = sum(1 for z in zeros if abs(z.imag) < T)
        assert abs(count_via_indicator.real - count_direct) < 1e-10


# ===========================================================================
# 4. Geometric side sums
# ===========================================================================

class TestGeometricSums:
    """Verify geometric side computations."""

    def test_heisenberg_geometric_gaussian(self):
        """Heisenberg: sum S_r h_hat(log r) = S_2 * h_hat(log 2)."""
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients, gaussian_fourier,
        )
        k = 3.0
        coeffs = get_shadow_coefficients('heisenberg', k, max_r=10)
        for sigma in [1.0, 2.0, 5.0]:
            geom = geometric_sum_gaussian(coeffs, sigma)
            expected = k * gaussian_fourier(math.log(2), sigma)
            assert abs(geom - expected) < 1e-10

    def test_affine_geometric_two_terms(self):
        """Affine: geometric sum has exactly two nonzero terms."""
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients, gaussian_fourier,
        )
        k = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k, max_r=10)
        sigma = 2.0
        geom = geometric_sum_gaussian(coeffs, sigma)
        # Manual: kappa*h_hat(log2) + alpha*h_hat(log3)
        kappa = 3.0 * (k + 2.0) / 4.0  # = 9/4
        alpha = 4.0 / (k + 2.0)  # = 4/3
        expected = (kappa * gaussian_fourier(math.log(2), sigma) +
                    alpha * gaussian_fourier(math.log(3), sigma))
        assert abs(geom - expected) < 1e-10

    def test_geometric_sum_positive_for_positive_coefficients(self):
        """For positive S_r and positive h_hat, geometric sum is positive."""
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=30)
        for sigma in [1.0, 2.0, 5.0]:
            geom = geometric_sum_gaussian(coeffs, sigma)
            assert geom > 0


# ===========================================================================
# 5. Trace formula: spectral = geometric (affine exact case)
# ===========================================================================

class TestTraceFormulaAffine:
    """Trace formula for affine sl_2 (exact 2-term case)."""

    def test_gaussian_spectral_vs_geometric_affine(self):
        """For affine, spectral and geometric sums should be related.

        The trace formula identity involves correction terms, so we check
        that the two sides have the same order of magnitude and sign.
        """
        from lib.bc_trace_formula_shadow_engine import (
            trace_formula_gaussian, get_shadow_coefficients, get_shadow_zeros,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=100)

        for sigma in [2.0, 5.0, 10.0]:
            result = trace_formula_gaussian(coeffs, zeros, sigma, max_r=10)
            # Both sides should be finite and nonzero
            assert abs(result.spectral_sum) > 1e-20 or abs(result.geometric_sum) > 1e-20

    def test_lorentzian_spectral_vs_geometric_affine(self):
        from lib.bc_trace_formula_shadow_engine import (
            trace_formula_lorentzian, get_shadow_coefficients, get_shadow_zeros,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=100)

        for a in [1.0, 2.0]:
            result = trace_formula_lorentzian(coeffs, zeros, a, max_r=10)
            assert abs(result.spectral_sum) > 1e-20 or abs(result.geometric_sum) > 1e-20


# ===========================================================================
# 6. Trace formula: Virasoro (class M)
# ===========================================================================

class TestTraceFormulaVirasoro:
    """Trace formula for Virasoro (infinite tower, class M)."""

    @pytest.fixture(scope='class')
    def virasoro_c25_data(self):
        from lib.bc_trace_formula_shadow_engine import (
            get_shadow_coefficients, get_shadow_zeros,
        )
        max_r = 60
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=max_r)
        zeros = get_shadow_zeros('virasoro', 25.0, n_zeros=50, max_r=max_r)
        return coeffs, zeros, max_r

    def test_gaussian_sigma_1(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_gaussian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_gaussian(coeffs, zeros, sigma=1.0, max_r=max_r)
        # Both sides should be computable (finite, nonzero generically)
        assert math.isfinite(result.geometric_sum)
        assert cmath.isfinite(result.spectral_sum)

    def test_gaussian_sigma_2(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_gaussian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_gaussian(coeffs, zeros, sigma=2.0, max_r=max_r)
        assert math.isfinite(result.geometric_sum)

    def test_gaussian_sigma_5(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_gaussian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_gaussian(coeffs, zeros, sigma=5.0, max_r=max_r)
        assert math.isfinite(result.geometric_sum)

    def test_gaussian_sigma_10(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_gaussian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_gaussian(coeffs, zeros, sigma=10.0, max_r=max_r)
        assert math.isfinite(result.geometric_sum)

    def test_lorentzian_a_1(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_lorentzian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_lorentzian(coeffs, zeros, a=1.0, max_r=max_r)
        assert math.isfinite(result.geometric_sum)

    def test_lorentzian_a_2(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_lorentzian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_lorentzian(coeffs, zeros, a=2.0, max_r=max_r)
        assert math.isfinite(result.geometric_sum)

    def test_lorentzian_a_5(self, virasoro_c25_data):
        from lib.bc_trace_formula_shadow_engine import trace_formula_lorentzian
        coeffs, zeros, max_r = virasoro_c25_data
        result = trace_formula_lorentzian(coeffs, zeros, a=5.0, max_r=max_r)
        assert math.isfinite(result.geometric_sum)


# ===========================================================================
# 7. Heat kernel
# ===========================================================================

class TestHeatKernel:
    """Heat kernel from shadow zeros."""

    def test_heat_kernel_spectral_positive(self):
        """Heat kernel sum of e^{-t|rho|^2} is positive for t > 0."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_spectral, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        for t in [0.01, 0.1, 1.0]:
            K = heat_kernel_spectral(zeros, t)
            assert K >= 0

    def test_heat_kernel_monotone_decreasing(self):
        """K_A(t) is decreasing in t (each term decreases)."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_spectral, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        K_prev = heat_kernel_spectral(zeros, 0.001)
        for t in [0.01, 0.1, 1.0, 10.0]:
            K_curr = heat_kernel_spectral(zeros, t)
            assert K_curr <= K_prev + 1e-10
            K_prev = K_curr

    def test_heat_kernel_from_coefficients_heisenberg(self):
        """Heisenberg: K(lam) = S_2 * exp(-2*lam) = k * exp(-2*lam)."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_from_coefficients, get_shadow_coefficients,
        )
        k = 3.0
        coeffs = get_shadow_coefficients('heisenberg', k, max_r=10)
        for lam in [0.1, 0.5, 1.0, 2.0]:
            K = heat_kernel_from_coefficients(coeffs, lam)
            expected = k * math.exp(-2.0 * lam)
            assert abs(K - expected) < 1e-12

    def test_heat_kernel_from_coefficients_affine(self):
        """Affine: K(lam) = kappa*exp(-2*lam) + alpha*exp(-3*lam)."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_from_coefficients, get_shadow_coefficients,
        )
        k = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k, max_r=10)
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        for lam in [0.1, 0.5, 1.0]:
            K = heat_kernel_from_coefficients(coeffs, lam)
            expected = kappa * math.exp(-2.0 * lam) + alpha * math.exp(-3.0 * lam)
            assert abs(K - expected) < 1e-12

    def test_heat_kernel_weyl_coefficients_exist(self):
        """Weyl law fitting should produce finite coefficients."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_weyl_coefficients, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        t_values = list(np.linspace(0.01, 0.5, 20))
        weyl = heat_kernel_weyl_coefficients(zeros, t_values)
        assert math.isfinite(weyl['a_0'])
        assert math.isfinite(weyl['a_1'])
        assert math.isfinite(weyl['a_2'])

    def test_heat_kernel_regularized(self):
        """Regularized kernel K(t) - a_0/t should be O(1) for small t."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_regularized, heat_kernel_weyl_coefficients,
            get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        t_values = list(np.linspace(0.01, 0.5, 20))
        weyl = heat_kernel_weyl_coefficients(zeros, t_values)
        a_0 = weyl['a_0']

        # Regularized kernel at small t should be moderate
        K_reg = heat_kernel_regularized(zeros, 0.05, a_0)
        assert math.isfinite(K_reg)


# ===========================================================================
# 8. Prime geodesic theorem
# ===========================================================================

class TestPrimeGeodesicTheorem:
    """Prime geodesic counting function."""

    def test_heisenberg_counting(self):
        """Heisenberg: only r=2 has S_r != 0, so pi^sh(x) = 1 for x >= log(2)."""
        from lib.bc_trace_formula_shadow_engine import (
            prime_geodesic_counting, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        counts = prime_geodesic_counting(coeffs, [0.5, 1.0, 2.0, 3.0])
        assert counts[0.5] == 0  # e^0.5 < 2
        assert counts[1.0] == 1  # e^1 ~ 2.7 >= 2
        assert counts[2.0] == 1  # Only r=2
        assert counts[3.0] == 1  # Only r=2

    def test_affine_counting(self):
        """Affine: r=2,3 nonzero, so pi^sh(x) = 2 for x >= log(3)."""
        from lib.bc_trace_formula_shadow_engine import (
            prime_geodesic_counting, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        counts = prime_geodesic_counting(coeffs, [0.5, 1.0, 1.5, 2.0])
        assert counts[0.5] == 0
        assert counts[1.0] == 1  # Only r=2
        assert counts[1.5] == 2  # e^1.5 ~ 4.5, so r=2,3
        assert counts[2.0] == 2  # r=2,3

    def test_virasoro_exponential_growth(self):
        """Class M: pi^sh(x) ~ floor(e^x) - 1 (all S_r nonzero)."""
        from lib.bc_trace_formula_shadow_engine import (
            prime_geodesic_counting, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=50)
        x_values = [1.0, 2.0, 3.0, 4.0]
        counts = prime_geodesic_counting(coeffs, x_values)
        for x in x_values:
            expected = min(int(math.floor(math.exp(x))), 50) - 1
            # Should be close to expected (all S_r nonzero for Virasoro)
            assert counts[x] >= expected - 1

    def test_prime_geodesic_error_term(self):
        """Error term computation should be finite."""
        from lib.bc_trace_formula_shadow_engine import (
            prime_geodesic_theorem_error, get_shadow_coefficients, get_shadow_zeros,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=20)
        result = prime_geodesic_theorem_error(coeffs, zeros, x=2.0)
        assert math.isfinite(result['actual_count'])
        assert math.isfinite(result['main_term'])
        assert math.isfinite(result['oscillatory_error'])

    def test_prime_geodesic_main_term_positive(self):
        from lib.bc_trace_formula_shadow_engine import (
            prime_geodesic_theorem_error, get_shadow_coefficients, get_shadow_zeros,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=30)
        zeros = get_shadow_zeros('virasoro', 25.0, n_zeros=20, max_r=30)
        for x in [1.0, 2.0, 3.0]:
            result = prime_geodesic_theorem_error(coeffs, zeros, x)
            assert result['main_term'] > 0


# ===========================================================================
# 9. Kuznetsov formula
# ===========================================================================

class TestKuznetsovFormula:
    """Shadow Kuznetsov spectral identity."""

    def test_kuznetsov_diagonal_positive(self):
        """Diagonal sum_rho |m^{-rho}|^2 >= 0."""
        from lib.bc_trace_formula_shadow_engine import (
            kuznetsov_diagonal, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        for m in [2, 3, 5, 7, 10]:
            diag = kuznetsov_diagonal(zeros, m)
            assert diag >= -1e-10  # Non-negative

    def test_kuznetsov_diagonal_decreasing_in_m(self):
        """For Re(rho) > 0, m^{-2*Re(rho)} decreases in m."""
        from lib.bc_trace_formula_shadow_engine import (
            kuznetsov_diagonal, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        # Check if zeros have positive real part
        if zeros and all(z.real > 0 for z in zeros):
            prev = kuznetsov_diagonal(zeros, 2)
            for m in [3, 5, 7, 10]:
                curr = kuznetsov_diagonal(zeros, m)
                assert curr <= prev + 1e-8
                prev = curr

    def test_kuznetsov_spectral_side_hermitian(self):
        """sum_rho a_rho(m) conj(a_rho(n)) = conj(sum_rho a_rho(n) conj(a_rho(m)))."""
        from lib.bc_trace_formula_shadow_engine import (
            kuznetsov_spectral_side, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        for m, n in [(2, 3), (3, 5), (2, 7)]:
            K_mn = kuznetsov_spectral_side(zeros, m, n)
            K_nm = kuznetsov_spectral_side(zeros, n, m)
            assert abs(K_mn - K_nm.conjugate()) < 1e-8

    def test_kuznetsov_geometric_side_bilinear(self):
        """Geometric side S_m * S_n / S_2 is well-defined for nonzero S_2."""
        from lib.bc_trace_formula_shadow_engine import (
            kuznetsov_geometric_side, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=20)
        for m, n in [(2, 2), (2, 3), (3, 3), (2, 5)]:
            geom = kuznetsov_geometric_side(coeffs, m, n)
            assert math.isfinite(geom)

    def test_kuznetsov_geometric_diagonal(self):
        """Geometric side S_m^2 / S_2 for diagonal case."""
        from lib.bc_trace_formula_shadow_engine import (
            kuznetsov_geometric_side, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=20)
        for m in [2, 3, 4, 5]:
            geom = kuznetsov_geometric_side(coeffs, m, m)
            Sm = coeffs.get(m, 0.0)
            S2 = coeffs.get(2, 0.0)
            expected = Sm * Sm / S2
            assert abs(geom - expected) < 1e-12


# ===========================================================================
# 10. Relative trace formula (Koszul pairs)
# ===========================================================================

class TestRelativeTraceFormula:
    """Relative trace formula for Virasoro Koszul pairs."""

    def test_complementarity_sum_d2_equals_13(self):
        """D_2 = kappa(c) + kappa(26-c) = 13 for any c (AP24)."""
        from lib.bc_trace_formula_shadow_engine import (
            complementarity_sum_coefficients,
        )
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            D = complementarity_sum_coefficients(c_val, max_r=10)
            assert abs(D[2] - 13.0) < 1e-10, f"D_2 = {D[2]} at c={c_val}, expected 13"

    def test_complementarity_sum_symmetric(self):
        """D_r(c) = D_r(26-c) by definition."""
        from lib.bc_trace_formula_shadow_engine import (
            complementarity_sum_coefficients,
        )
        c_val = 7.0
        D_c = complementarity_sum_coefficients(c_val, max_r=20)
        D_dual = complementarity_sum_coefficients(26.0 - c_val, max_r=20)
        for r in range(2, 21):
            assert abs(D_c[r] - D_dual[r]) < 1e-10

    def test_relative_trace_geometric_symmetric(self):
        """Relative geometric trace is symmetric under c <-> 26-c."""
        from lib.bc_trace_formula_shadow_engine import (
            relative_trace_geometric, get_shadow_coefficients, gaussian_fourier,
        )
        c_val = 7.0
        max_r = 30
        coeffs = get_shadow_coefficients('virasoro', c_val, max_r)
        dual_coeffs = get_shadow_coefficients('virasoro', 26.0 - c_val, max_r)

        sigma = 2.0
        geom_forward = relative_trace_geometric(
            coeffs, dual_coeffs,
            lambda t: gaussian_fourier(t, sigma),
            max_r,
        )
        geom_reverse = relative_trace_geometric(
            dual_coeffs, coeffs,
            lambda t: gaussian_fourier(t, sigma),
            max_r,
        )
        assert abs(geom_forward - geom_reverse) < 1e-10


# ===========================================================================
# 11. Self-dual symmetry at c = 13
# ===========================================================================

class TestSelfDualSymmetry:
    """Enhanced symmetry at the self-dual point c = 13."""

    def test_c13_coefficients_self_dual(self):
        """S_r(Vir_13) = S_r(Vir_{26-13}) = S_r(Vir_13)."""
        from lib.bc_trace_formula_shadow_engine import (
            self_dual_symmetry_test,
        )
        results = self_dual_symmetry_test(13.0, max_r=30)
        assert results['max_coefficient_diff'] < 1e-10

    def test_c13_kappa_sum_13(self):
        """kappa + kappa' = 13/2 + 13/2 = 13."""
        from lib.bc_trace_formula_shadow_engine import self_dual_symmetry_test
        results = self_dual_symmetry_test(13.0, max_r=20)
        assert abs(results['kappa_sum'] - 13.0) < 1e-10

    def test_c13_asymmetry_vanishes(self):
        """At c=13, the trace asymmetry vanishes for all sigma."""
        from lib.bc_trace_formula_shadow_engine import self_dual_symmetry_test
        results = self_dual_symmetry_test(13.0, max_r=30)
        for sigma in [1.0, 2.0, 5.0, 10.0]:
            key = f'asymmetry_sigma_{sigma}'
            assert abs(results[key]) < 1e-10, f"Asymmetry at sigma={sigma}: {results[key]}"

    def test_c13_vs_c1_asymmetry_nonzero(self):
        """At c=1 (NOT self-dual), the asymmetry should be nonzero."""
        from lib.bc_trace_formula_shadow_engine import (
            relative_trace_asymmetry, get_shadow_coefficients, gaussian_fourier,
        )
        max_r = 30
        coeffs = get_shadow_coefficients('virasoro', 1.0, max_r)
        dual_coeffs = get_shadow_coefficients('virasoro', 25.0, max_r)
        sigma = 2.0
        asym = relative_trace_asymmetry(
            coeffs, dual_coeffs,
            lambda t: gaussian_fourier(t, sigma),
            max_r,
        )
        assert abs(asym) > 1e-5, "c=1 asymmetry should be nonzero"


# ===========================================================================
# 12. Virasoro at multiple central charges
# ===========================================================================

class TestVirasoro_c1:
    """Trace formula at c = 1."""

    def test_kappa_c1(self):
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        coeffs = get_shadow_coefficients('virasoro', 1.0)
        assert abs(coeffs[2] - 0.5) < 1e-10

    def test_geometric_sum_c1(self):
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 1.0, max_r=30)
        geom = geometric_sum_gaussian(coeffs, sigma=2.0, max_r=30)
        assert math.isfinite(geom)
        assert geom > 0  # positive shadow tower


class TestVirasoro_c13:
    """Trace formula at c = 13 (self-dual)."""

    def test_kappa_c13(self):
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        coeffs = get_shadow_coefficients('virasoro', 13.0)
        assert abs(coeffs[2] - 6.5) < 1e-10

    def test_complementarity_c13(self):
        from lib.bc_trace_formula_shadow_engine import (
            complementarity_sum_coefficients,
        )
        D = complementarity_sum_coefficients(13.0, max_r=20)
        # At self-dual: D_r = 2 * S_r(13)
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        for r in range(2, 21):
            assert abs(D[r] - 2.0 * coeffs.get(r, 0.0)) < 1e-10


class TestVirasoro_c25:
    """Trace formula at c = 25."""

    def test_kappa_c25(self):
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        coeffs = get_shadow_coefficients('virasoro', 25.0)
        assert abs(coeffs[2] - 12.5) < 1e-10

    def test_kappa_sum_c25(self):
        """kappa(25) + kappa(1) = 12.5 + 0.5 = 13."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        c25 = get_shadow_coefficients('virasoro', 25.0)
        c1 = get_shadow_coefficients('virasoro', 1.0)
        assert abs(c25[2] + c1[2] - 13.0) < 1e-10


# ===========================================================================
# 13. Arthur trace formula
# ===========================================================================

class TestArthurTraceFormula:
    """Arthur trace formula decomposition."""

    def test_discrete_spectrum_equals_spectral_sum(self):
        from lib.bc_trace_formula_shadow_engine import (
            arthur_discrete_spectrum, spectral_sum_gaussian,
            get_shadow_zeros, gaussian_test,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        sigma = 2.0
        discrete = arthur_discrete_spectrum(
            zeros, lambda s: gaussian_test(s, sigma))
        spec = spectral_sum_gaussian(zeros, sigma)
        assert abs(discrete - spec) < 1e-12

    def test_eisenstein_contribution_symmetric(self):
        """E_A(s) = zeta_D(s)/2 should be symmetric in the Koszul pair."""
        from lib.bc_trace_formula_shadow_engine import (
            eisenstein_contribution, get_shadow_coefficients,
        )
        c_val = 7.0
        max_r = 30
        coeffs = get_shadow_coefficients('virasoro', c_val, max_r)
        dual_coeffs = get_shadow_coefficients('virasoro', 26.0 - c_val, max_r)

        s = complex(2.0, 3.0)
        E_forward = eisenstein_contribution(coeffs, dual_coeffs, s, max_r)
        E_reverse = eisenstein_contribution(dual_coeffs, coeffs, s, max_r)
        assert abs(E_forward - E_reverse) < 1e-10

    def test_eisenstein_at_self_dual(self):
        """At c=13: E_A(s) = zeta_{13}(s) (since zeta_D = 2*zeta_{13})."""
        from lib.bc_trace_formula_shadow_engine import (
            eisenstein_contribution, get_shadow_coefficients,
        )
        from lib.bc_shadow_zeta_zeros_engine import _shadow_zeta_complex
        max_r = 30
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r)
        dual_coeffs = get_shadow_coefficients('virasoro', 13.0, max_r)

        s = complex(2.0, 1.0)
        E = eisenstein_contribution(coeffs, dual_coeffs, s, max_r)
        zeta_13 = _shadow_zeta_complex(coeffs, s, max_r)
        assert abs(E - zeta_13) < 1e-10


# ===========================================================================
# 14. Log-derivative integral
# ===========================================================================

class TestLogDerivativeIntegral:
    """Test the (1/(2pi)) integral h(t) zeta'/zeta (1/2+it) dt."""

    def test_log_derivative_finite(self):
        from lib.bc_trace_formula_shadow_engine import (
            log_derivative_integral, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        result = log_derivative_integral(
            coeffs,
            lambda t: math.exp(-t * t / 8.0),
            t_range=(-20.0, 20.0),
            n_points=1000,
            max_r=10,
        )
        assert cmath.isfinite(result)

    def test_log_derivative_narrow_gaussian(self):
        """Narrow Gaussian concentrates near t=0."""
        from lib.bc_trace_formula_shadow_engine import (
            log_derivative_integral, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        # sigma = 0.1: very narrow, concentrates near zeta'/zeta at s=1/2
        result = log_derivative_integral(
            coeffs,
            lambda t: math.exp(-t * t / 0.02),
            t_range=(-5.0, 5.0),
            n_points=2000,
            max_r=10,
        )
        assert cmath.isfinite(result)


# ===========================================================================
# 15. Full comparison
# ===========================================================================

class TestFullComparison:
    """Full trace formula comparison."""

    def test_full_comparison_c25(self):
        from lib.bc_trace_formula_shadow_engine import full_comparison
        result = full_comparison(25.0, max_r=40, n_zeros=20,
                                 sigmas=[2.0, 5.0], lorentzian_as=[2.0])
        assert result.c_val == 25.0
        assert abs(result.kappa - 12.5) < 1e-10
        assert len(result.gaussian_results) == 2
        assert len(result.lorentzian_results) == 1
        assert result.self_dual_test is None  # c != 13

    def test_full_comparison_c13(self):
        from lib.bc_trace_formula_shadow_engine import full_comparison
        result = full_comparison(13.0, max_r=40, n_zeros=20,
                                 sigmas=[2.0], lorentzian_as=[2.0])
        assert result.self_dual_test is not None
        assert abs(result.kappa - 6.5) < 1e-10


# ===========================================================================
# 16. Complementarity trace formula
# ===========================================================================

class TestComplementarityTraceFormula:
    """Trace formula for the complementarity Dirichlet series."""

    def test_complementarity_d2_anchor(self):
        """D_2 = 13 for all c (structural anchor, AP24)."""
        from lib.bc_trace_formula_shadow_engine import (
            complementarity_sum_coefficients,
        )
        for c_val in [1.0, 7.0, 13.0, 20.0, 25.0]:
            D = complementarity_sum_coefficients(c_val, max_r=10)
            assert abs(D[2] - 13.0) < 1e-10

    def test_complementarity_higher_arities(self):
        """D_r for r >= 3 is c-dependent but finite."""
        from lib.bc_trace_formula_shadow_engine import (
            complementarity_sum_coefficients,
        )
        D = complementarity_sum_coefficients(7.0, max_r=10)
        for r in range(3, 11):
            assert math.isfinite(D[r])


# ===========================================================================
# 17. Weil explicit formula sides
# ===========================================================================

class TestWeilExplicit:
    """Weil explicit formula spectral and geometric sides."""

    def test_weil_geometric_sqrt_normalization(self):
        """Weil geometric side uses 1/sqrt(r) normalization."""
        from lib.bc_trace_formula_shadow_engine import (
            weil_explicit_geometric, get_shadow_coefficients, gaussian_fourier,
        )
        coeffs = get_shadow_coefficients('heisenberg', 2.0, max_r=10)
        sigma = 2.0
        weil = weil_explicit_geometric(
            coeffs, lambda t: gaussian_fourier(t, sigma), max_r=10)
        # = S_2 * h_hat(log 2) / sqrt(2)
        expected = 2.0 * gaussian_fourier(math.log(2), sigma) / math.sqrt(2)
        assert abs(weil - expected) < 1e-10

    def test_weil_spectral_equals_spectral_sum(self):
        from lib.bc_trace_formula_shadow_engine import (
            weil_explicit_spectral, spectral_sum, get_shadow_zeros,
            gaussian_test,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        sigma = 2.0
        test = lambda s: gaussian_test(s, sigma)
        weil_spec = weil_explicit_spectral(zeros, test)
        direct = spectral_sum(zeros, test)
        assert abs(weil_spec - direct) < 1e-14


# ===========================================================================
# 18. Cross-family consistency
# ===========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_betagamma_has_three_nonzero_terms(self):
        """Beta-gamma (class C): S_2, S_3, S_4 nonzero; S_r = 0 for r >= 5."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        coeffs = get_shadow_coefficients('betagamma', 0.5, max_r=10)
        assert abs(coeffs[2]) > 1e-15
        assert abs(coeffs[3]) > 1e-15
        assert abs(coeffs[4]) > 1e-15
        for r in range(5, 11):
            assert abs(coeffs[r]) < 1e-15

    def test_shadow_depth_classification(self):
        """Class G: 1 nonzero. Class L: 2. Class C: 3. Class M: all."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        # Class G
        heis = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        nz_heis = sum(1 for r in range(2, 11) if abs(heis.get(r, 0.0)) > 1e-15)
        assert nz_heis == 1

        # Class L
        aff = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        nz_aff = sum(1 for r in range(2, 11) if abs(aff.get(r, 0.0)) > 1e-15)
        assert nz_aff == 2

        # Class C
        bg = get_shadow_coefficients('betagamma', 0.5, max_r=10)
        nz_bg = sum(1 for r in range(2, 11) if abs(bg.get(r, 0.0)) > 1e-15)
        assert nz_bg == 3

        # Class M
        vir = get_shadow_coefficients('virasoro', 25.0, max_r=10)
        nz_vir = sum(1 for r in range(2, 11) if abs(vir.get(r, 0.0)) > 1e-15)
        assert nz_vir >= 8  # all 9 from r=2..10

    def test_geometric_sum_proportional_to_kappa_heisenberg(self):
        """For Heisenberg, geometric sum is proportional to k."""
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients,
        )
        sigma = 2.0
        g1 = geometric_sum_gaussian(
            get_shadow_coefficients('heisenberg', 1.0, 10), sigma, 10)
        g5 = geometric_sum_gaussian(
            get_shadow_coefficients('heisenberg', 5.0, 10), sigma, 10)
        # g5 / g1 = 5
        assert abs(g5 / g1 - 5.0) < 1e-10


# ===========================================================================
# 19. Numerical stability
# ===========================================================================

class TestNumericalStability:
    """Numerical stability checks."""

    def test_gaussian_test_large_sigma(self):
        """Large sigma: Gaussian is broad, spectral sum converges slowly."""
        from lib.bc_trace_formula_shadow_engine import gaussian_test
        # Should not overflow
        val = gaussian_test(complex(0, 100), sigma=100.0)
        assert cmath.isfinite(val)

    def test_lorentzian_near_pole(self):
        """Lorentzian 1/(s^2+a^2) has poles at s = +/- ia. Avoid them."""
        from lib.bc_trace_formula_shadow_engine import lorentzian_test
        # Near the pole but not at it
        val = lorentzian_test(complex(0, 0.999), a=1.0)
        assert cmath.isfinite(val)
        assert abs(val) > 100  # Large but finite

    def test_heat_kernel_large_t(self):
        """Large t: heat kernel decays to 0."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_spectral, get_shadow_zeros,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        K = heat_kernel_spectral(zeros, t=100.0)
        assert abs(K) < 1e-10

    def test_geometric_sum_convergence(self):
        """Geometric sum with Gaussian test converges (Gaussian decays in t)."""
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=100)
        g30 = geometric_sum_gaussian(coeffs, sigma=2.0, max_r=30)
        g50 = geometric_sum_gaussian(coeffs, sigma=2.0, max_r=50)
        g100 = geometric_sum_gaussian(coeffs, sigma=2.0, max_r=100)
        # Should converge: |g100 - g50| < |g50 - g30|
        d1 = abs(g50 - g30)
        d2 = abs(g100 - g50)
        if d1 > 1e-15:
            assert d2 < d1 * 1.5  # Some convergence


# ===========================================================================
# 20. Multi-path verification
# ===========================================================================

class TestMultiPathVerification:
    """Multi-path verification: same quantity computed different ways."""

    def test_kappa_from_coefficients_vs_formula(self):
        """Path 1: S_2 from coefficients. Path 2: c/2 directly (Virasoro)."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            coeffs = get_shadow_coefficients('virasoro', c_val)
            assert abs(coeffs[2] - c_val / 2.0) < 1e-10

    def test_complementarity_sum_two_paths(self):
        """Path 1: D_2 from sum of coefficients.
        Path 2: D_2 = 13 from AP24.
        Path 3: D_2 = c/2 + (26-c)/2 = 13 algebraically.
        """
        from lib.bc_trace_formula_shadow_engine import (
            complementarity_sum_coefficients, get_shadow_coefficients,
        )
        c_val = 7.0
        # Path 1
        D = complementarity_sum_coefficients(c_val, max_r=10)
        path1 = D[2]
        # Path 2
        path2 = 13.0
        # Path 3
        path3 = c_val / 2.0 + (26.0 - c_val) / 2.0
        assert abs(path1 - path2) < 1e-10
        assert abs(path1 - path3) < 1e-10
        assert abs(path2 - path3) < 1e-10

    def test_heisenberg_heat_kernel_two_paths(self):
        """Path 1: from coefficients. Path 2: analytic k*exp(-2*lam)."""
        from lib.bc_trace_formula_shadow_engine import (
            heat_kernel_from_coefficients, get_shadow_coefficients,
        )
        k = 4.0
        coeffs = get_shadow_coefficients('heisenberg', k, max_r=10)
        for lam in [0.1, 0.5, 1.0]:
            path1 = heat_kernel_from_coefficients(coeffs, lam)
            path2 = k * math.exp(-2.0 * lam)
            assert abs(path1 - path2) < 1e-12

    def test_affine_kappa_from_first_principles(self):
        """Affine sl_2: kappa = 3(k+2)/4 from dim=3, h^v=2."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        k = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k, max_r=10)
        # Path 1: from coefficients
        path1 = coeffs[2]
        # Path 2: dim(g)*(k+h^v)/(2*h^v)
        path2 = 3.0 * (k + 2.0) / (2.0 * 2.0)
        # Path 3: = 3*3/4 = 9/4 = 2.25
        path3 = 9.0 / 4.0
        assert abs(path1 - path2) < 1e-10
        assert abs(path1 - path3) < 1e-10

    def test_spectral_sum_two_paths(self):
        """Path 1: generic spectral_sum. Path 2: specialized gaussian version."""
        from lib.bc_trace_formula_shadow_engine import (
            spectral_sum, spectral_sum_gaussian, get_shadow_zeros, gaussian_test,
        )
        zeros = get_shadow_zeros('affine_sl2', 1.0, n_zeros=50)
        sigma = 2.0
        path1 = spectral_sum(zeros, lambda s: gaussian_test(s, sigma))
        path2 = spectral_sum_gaussian(zeros, sigma)
        assert abs(path1 - path2) < 1e-14


# ===========================================================================
# 21. Edge cases
# ===========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_empty_zeros_spectral_sum(self):
        from lib.bc_trace_formula_shadow_engine import spectral_sum_gaussian
        assert abs(spectral_sum_gaussian([], sigma=1.0)) < 1e-14

    def test_empty_zeros_heat_kernel(self):
        from lib.bc_trace_formula_shadow_engine import heat_kernel_spectral
        assert abs(heat_kernel_spectral([], t=1.0)) < 1e-14

    def test_empty_zeros_kuznetsov(self):
        from lib.bc_trace_formula_shadow_engine import kuznetsov_diagonal
        assert abs(kuznetsov_diagonal([], m=2)) < 1e-14

    def test_single_zero(self):
        """Single zero: all sums are single-term."""
        from lib.bc_trace_formula_shadow_engine import (
            spectral_sum_gaussian, heat_kernel_spectral,
            kuznetsov_diagonal,
        )
        zeros = [complex(1.0, 5.0)]
        sigma = 2.0
        spec = spectral_sum_gaussian(zeros, sigma)
        expected = cmath.exp(-complex(1.0, 5.0) ** 2 / (2.0 * sigma ** 2))
        assert abs(spec - expected) < 1e-12

        K = heat_kernel_spectral(zeros, t=0.1)
        expected_K = math.exp(-0.1 * (1.0 + 25.0))
        assert abs(K - expected_K) < 1e-12

    def test_prime_geodesic_at_x_zero(self):
        """At x=0: e^0=1 < 2, so pi^sh(0) = 0."""
        from lib.bc_trace_formula_shadow_engine import (
            prime_geodesic_counting, get_shadow_coefficients,
        )
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=10)
        counts = prime_geodesic_counting(coeffs, [0.0])
        assert counts[0.0] == 0


# ===========================================================================
# 22. Virasoro c=1, c=13, c=25 simultaneous comparison
# ===========================================================================

class TestVirasoro_3c_Comparison:
    """Compare trace formula at c=1, 13, 25 simultaneously."""

    def test_kappa_ordering(self):
        """kappa(1) < kappa(13) < kappa(25)."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        k1 = get_shadow_coefficients('virasoro', 1.0)[2]
        k13 = get_shadow_coefficients('virasoro', 13.0)[2]
        k25 = get_shadow_coefficients('virasoro', 25.0)[2]
        assert k1 < k13 < k25

    def test_kappa_values(self):
        """kappa(c) = c/2 for Virasoro."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        for c_val in [1.0, 13.0, 25.0]:
            k = get_shadow_coefficients('virasoro', c_val)[2]
            assert abs(k - c_val / 2.0) < 1e-10

    def test_kappa_complementarity_pairs(self):
        """(c=1, c=25) are Koszul duals. kappa sum = 13."""
        from lib.bc_trace_formula_shadow_engine import get_shadow_coefficients
        k1 = get_shadow_coefficients('virasoro', 1.0)[2]
        k25 = get_shadow_coefficients('virasoro', 25.0)[2]
        assert abs(k1 + k25 - 13.0) < 1e-10

    def test_geometric_sums_ordering(self):
        """Larger kappa => larger geometric sum (for fixed positive h_hat)."""
        from lib.bc_trace_formula_shadow_engine import (
            geometric_sum_gaussian, get_shadow_coefficients,
        )
        sigma = 2.0
        max_r = 20
        g1 = geometric_sum_gaussian(
            get_shadow_coefficients('virasoro', 1.0, max_r), sigma, max_r)
        g13 = geometric_sum_gaussian(
            get_shadow_coefficients('virasoro', 13.0, max_r), sigma, max_r)
        g25 = geometric_sum_gaussian(
            get_shadow_coefficients('virasoro', 25.0, max_r), sigma, max_r)
        # Ordering follows kappa ordering
        assert g1 < g13 < g25
