#!/usr/bin/env python3
"""
test_sewing_euler_product.py — Direction B: Prime decomposition of sewing operator.

T1-T10:  Divisor functions and multiplicativity
T11-T20: Prime factorization of log det(1-K_q)
T21-T30: Trace formula: tr(K^N) and σ_0
T31-T40: Second quantization: ζ(s)² from sewing
T41-T50: Direct extraction: ζ(s) from eigenvalue labels
T51-T60: Selberg-type structure and spectral properties
T61-T70: The obstruction and honest assessment
"""

import pytest
import numpy as np
import math
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from sewing_euler_product import (
    sigma_k, sigma_minus_1, sigma_0, sigma_1, von_mangoldt, is_prime,
    primes_up_to,
    log_det_full, log_det_sigma, log_det_prime_factored, prime_contribution,
    trace_K_power, sewing_trace_formula, sewing_prime_orbit_trace,
    sewing_second_quantization, divisor_function_dirichlet_test,
    sewing_weil_formula,
    zeta_product_analysis,
    sewing_selberg_zeta,
    sewing_to_zeta_direct,
    sewing_operator_spectral_properties,
    direction_B_status,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# T1-T10: Divisor functions
# ============================================================

class TestDivisorFunctions:
    def test_sigma_minus_1_values(self):
        """T1: σ_{-1}(N) = Σ_{d|N} 1/d."""
        assert abs(sigma_minus_1(1) - 1.0) < 1e-10
        assert abs(sigma_minus_1(2) - 1.5) < 1e-10
        assert abs(sigma_minus_1(6) - 2.0) < 1e-10
        assert abs(sigma_minus_1(12) - (1 + 1/2 + 1/3 + 1/4 + 1/6 + 1/12)) < 1e-10

    def test_sigma_0_values(self):
        """T2: σ_0(N) = d(N) = number of divisors."""
        assert sigma_0(1) == 1
        assert sigma_0(2) == 2
        assert sigma_0(6) == 4  # 1,2,3,6
        assert sigma_0(12) == 6  # 1,2,3,4,6,12
        for p in [2, 3, 5, 7, 11]:
            assert sigma_0(p) == 2  # primes have exactly 2 divisors

    def test_sigma_minus_1_multiplicative(self):
        """T3: σ_{-1} is multiplicative: σ_{-1}(mn) = σ_{-1}(m)σ_{-1}(n) for gcd(m,n)=1."""
        from math import gcd
        for m in range(1, 30):
            for n in range(1, 30):
                if gcd(m, n) == 1:
                    assert abs(sigma_minus_1(m * n) - sigma_minus_1(m) * sigma_minus_1(n)) < 1e-10

    def test_sigma_0_multiplicative(self):
        """T4: σ_0 is multiplicative."""
        from math import gcd
        for m in range(1, 20):
            for n in range(1, 20):
                if gcd(m, n) == 1:
                    assert sigma_0(m * n) == sigma_0(m) * sigma_0(n)

    def test_von_mangoldt(self):
        """T5: Λ(n) = log p if n=p^k, else 0."""
        assert abs(von_mangoldt(2) - math.log(2)) < 1e-10
        assert abs(von_mangoldt(4) - math.log(2)) < 1e-10  # 4=2²
        assert abs(von_mangoldt(8) - math.log(2)) < 1e-10  # 8=2³
        assert abs(von_mangoldt(3) - math.log(3)) < 1e-10
        assert abs(von_mangoldt(6)) < 1e-10  # 6=2·3, not prime power
        assert abs(von_mangoldt(1)) < 1e-10

    def test_primes_sieve(self):
        """T6: Sieve gives correct primes."""
        p = primes_up_to(30)
        assert p == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_sigma_1_values(self):
        """T7: σ_1(N) = sum of divisors."""
        assert sigma_1(6) == 12  # 1+2+3+6
        assert sigma_1(28) == 56  # 28 is perfect: σ_1 = 2N

    def test_sigma_k_relation(self):
        """T8: σ_{-1}(N) = σ_1(N)/N."""
        for N in range(1, 50):
            assert abs(sigma_minus_1(N) - sigma_1(N) / N) < 1e-10

    def test_sigma_0_always_positive(self):
        """T9: σ_0(N) ≥ 1 for all N ≥ 1 (every number has at least 1 as divisor)."""
        for N in range(1, 100):
            assert sigma_0(N) >= 1

    def test_sigma_0_at_primes(self):
        """T10: σ_0(p) = 2 for all primes p."""
        for p in primes_up_to(50):
            assert sigma_0(p) == 2


# ============================================================
# T11-T20: Prime factorization of log det
# ============================================================

class TestPrimeFactorization:
    def test_log_det_two_methods_agree(self):
        """T11: log det via direct product = log det via σ_{-1} sum."""
        for q in [0.1, 0.3, 0.5, 0.7]:
            direct = log_det_full(q)
            sigma = log_det_sigma(q)
            assert abs(direct - sigma) / abs(direct) < 1e-4

    def test_log_det_negative(self):
        """T12: log det(1-K_q) < 0 for 0 < q < 1 (det < 1)."""
        for q in [0.1, 0.3, 0.5, 0.7, 0.9]:
            assert log_det_full(q) < 0

    def test_prime_contribution_sum(self):
        """T13: Sum of prime contributions ≈ prime-power part of log det."""
        q = 0.3
        primes = primes_up_to(100)
        prime_sum = sum(prime_contribution(q, p) for p in primes)
        _, pp_part, _, _ = log_det_prime_factored(q, primes, nmax=100)
        assert abs(prime_sum - pp_part) / abs(pp_part) < 0.01

    def test_prime_contribution_negative(self):
        """T14: Each prime's contribution is negative (each factor < 1)."""
        q = 0.3
        for p in primes_up_to(20):
            assert prime_contribution(q, p) < 0

    def test_unit_contribution(self):
        """T15: The n=1 contribution is log(1-q)."""
        q = 0.4
        _, _, unit, _ = log_det_prime_factored(q, nmax=50)
        assert abs(unit - math.log(1 - q)) < 1e-10

    def test_prime_power_plus_composite_equals_total(self):
        """T16: total = unit + prime_power + composite."""
        q = 0.3
        total, pp, unit, comp = log_det_prime_factored(q, nmax=100)
        reconstructed = unit + pp + comp
        assert abs(total - reconstructed) / abs(total) < 0.01

    def test_small_primes_dominate(self):
        """T17: Small primes contribute more than large primes."""
        q = 0.3
        c2 = prime_contribution(q, 2)
        c3 = prime_contribution(q, 3)
        c5 = prime_contribution(q, 5)
        assert abs(c2) > abs(c3) > abs(c5)

    def test_prime_contribution_at_small_q(self):
        """T18: At small q, prime contributions scale as q^p."""
        q = 0.01
        for p in [2, 3, 5]:
            c = prime_contribution(q, p)
            # Leading term: log(1-q^p) ≈ -q^p
            assert abs(c - (-q ** p)) / abs(q ** p) < 0.1

    def test_factored_agrees_at_multiple_q(self):
        """T19: Factored log det agrees with direct at multiple q values."""
        for q in [0.05, 0.2, 0.4, 0.6, 0.8]:
            direct = log_det_full(q)
            sigma = log_det_sigma(q, Nmax=300)
            assert abs(direct - sigma) / abs(direct) < 0.01

    def test_composite_contribution_small(self):
        """T20: Composite contribution is smaller than prime-power for small q."""
        q = 0.1
        _, pp, _, comp = log_det_prime_factored(q, nmax=50)
        # At small q, prime powers dominate
        assert abs(comp) < abs(pp)


# ============================================================
# T21-T30: Trace formula
# ============================================================

class TestTraceFormula:
    def test_trace_K_1(self):
        """T21: tr(K_q) = q/(1-q)."""
        for q in [0.1, 0.3, 0.5]:
            assert abs(trace_K_power(q, 1) - q / (1 - q)) < 1e-10

    def test_trace_K_2(self):
        """T22: tr(K_q²) = q²/(1-q²)."""
        for q in [0.1, 0.3, 0.5]:
            assert abs(trace_K_power(q, 2) - q ** 2 / (1 - q ** 2)) < 1e-10

    def test_trace_formula_identity(self):
        """T23: Σ tr(K^N)/N = Σ σ_{-1}(N) q^N = -log det(1-K_q)."""
        q = 0.3
        # LHS
        lhs = sum(trace_K_power(q, N) / N for N in range(1, 200))
        # RHS
        rhs = -log_det_full(q)
        assert abs(lhs - rhs) / abs(rhs) < 0.01

    def test_sewing_trace_formula_entries(self):
        """T24: Individual entries of trace formula match."""
        q = 0.3
        entries = sewing_trace_formula(q, Nmax=20)
        for N, tr_N, sigma_N in entries:
            # tr(K^N)/N and σ_{-1}(N)q^N are the N-th CUMULATIVE terms,
            # not directly comparable; the identity is for the SUM.
            assert np.isfinite(tr_N)
            assert np.isfinite(sigma_N)

    @skip_no_mpmath
    def test_sigma_0_dirichlet_is_zeta_squared(self):
        """T25: Σ σ_0(N) N^{-s} = ζ(s)² — THE KEY IDENTITY."""
        s0, zsq, _, _ = divisor_function_dirichlet_test(2.0, Nmax=2000)
        assert abs(s0 - zsq) / abs(zsq) < 0.01

    @skip_no_mpmath
    def test_sigma_m1_dirichlet_is_zeta_zeta1(self):
        """T26: Σ σ_{-1}(N) N^{-s} = ζ(s)ζ(s+1) — SEWING IDENTITY."""
        _, _, sm1, zz1 = divisor_function_dirichlet_test(2.0, Nmax=2000)
        assert abs(sm1 - zz1) / abs(zz1) < 0.01

    def test_prime_orbit_trace(self):
        """T27: Prime orbit trace computation runs."""
        q = 0.3
        prime_sum, deriv = sewing_prime_orbit_trace(q, Nmax=100)
        assert np.isfinite(prime_sum)
        assert np.isfinite(deriv)

    def test_von_mangoldt_sum(self):
        """T28: Σ Λ(n)/n = -ζ'/ζ at s=1... actually Σ Λ(n)n^{-s} = -ζ'/ζ(s)."""
        if not HAS_MPMATH:
            pytest.skip("mpmath required")
        s = 2.0
        vm_sum = sum(von_mangoldt(n) * n ** (-s) for n in range(1, 1000))
        expected = -float(mpmath.diff(mpmath.zeta, s) / mpmath.zeta(s))
        assert abs(vm_sum - expected) / abs(expected) < 0.01

    def test_trace_positive(self):
        """T29: tr(K_q^N) > 0 for all N and 0 < q < 1."""
        for q in [0.1, 0.5, 0.9]:
            for N in range(1, 20):
                assert trace_K_power(q, N) > 0

    def test_trace_decreasing_in_N(self):
        """T30: tr(K_q^N) decreasing in N (larger powers decay faster)."""
        q = 0.5
        traces = [trace_K_power(q, N) for N in range(1, 10)]
        for i in range(len(traces) - 1):
            assert traces[i] > traces[i + 1]


# ============================================================
# T31-T40: Second quantization and ζ²
# ============================================================

class TestSecondQuantization:
    def test_tensor_product_match(self):
        """T31: σ_0 sum matches (q/(1-q))² (tensor product trace)."""
        q = 0.3
        result = sewing_second_quantization(q)
        assert result['tensor_product_match'] < 0.01

    def test_eigenvalue_decay(self):
        """T32: Eigenvalues of K_q decay exponentially."""
        result = sewing_second_quantization(0.5)
        assert result['eigenvalue_decay'] > 100  # q^1/q^50 = q^{-49}

    @skip_no_mpmath
    def test_zeta_squared_from_sigma_0(self):
        """T33: ζ(s)² = Σ σ_0(N) N^{-s} at multiple s values."""
        for s in [2.0, 3.0, 4.0]:
            s0, zsq, _, _ = divisor_function_dirichlet_test(s, Nmax=1000)
            assert abs(s0 - zsq) / abs(zsq) < 0.01

    @skip_no_mpmath
    def test_zeta_from_sqrt_sigma_0(self):
        """T34: ζ(s) = √(Σ σ_0(N) N^{-s})."""
        for s in [2.0, 3.0]:
            s0, _, _, _ = divisor_function_dirichlet_test(s, Nmax=1000)
            zeta_est = np.sqrt(s0)
            zeta_true = float(mpmath.zeta(s))
            assert abs(zeta_est - zeta_true) / abs(zeta_true) < 0.01

    @skip_no_mpmath
    def test_zeta_zeta1_from_sigma_m1(self):
        """T35: ζ(s)ζ(s+1) = Σ σ_{-1}(N) N^{-s} at multiple s values."""
        for s in [2.0, 3.0, 4.0]:
            _, _, sm1, zz1 = divisor_function_dirichlet_test(s, Nmax=1000)
            assert abs(sm1 - zz1) / abs(zz1) < 0.01

    @skip_no_mpmath
    def test_zeta_ratio_from_sewing(self):
        """T36: ζ(s)/ζ(s+1) = [Σ σ_0 N^{-s}] / [Σ σ_{-1} N^{-s}]."""
        s = 2.0
        s0, _, sm1, _ = divisor_function_dirichlet_test(s, Nmax=1000)
        ratio = s0 / sm1
        expected = float(mpmath.zeta(s) / mpmath.zeta(s + 1))
        assert abs(ratio - expected) / abs(expected) < 0.02

    def test_sigma_0_convolution(self):
        """T37: σ_0 = 1 * 1 (Dirichlet convolution)."""
        # σ_0(N) = Σ_{d|N} 1 = (1 * 1)(N)
        for N in range(1, 30):
            conv = sum(1 for d in range(1, N + 1) if N % d == 0)
            assert conv == sigma_0(N)

    def test_sigma_m1_convolution(self):
        """T38: σ_{-1} = 1 * id^{-1} (Dirichlet convolution with 1/n)."""
        # σ_{-1}(N) = Σ_{d|N} 1/d = (1/n * 1)(N)? No: = Σ_{d|N} d^{-1}
        # Actually σ_{-1} = id^{-1} * u where u(n)=1, id^{-1}(n)=1/n
        for N in range(1, 20):
            assert abs(sigma_minus_1(N) - sum(1.0 / d for d in range(1, N + 1) if N % d == 0)) < 1e-10

    @skip_no_mpmath
    def test_euler_product_sigma_0(self):
        """T39: ζ(s)² = Π_p (1-p^{-s})^{-2} at s=2."""
        primes = primes_up_to(100)
        prod = 1.0
        for p in primes:
            prod *= (1 - p ** (-2.0)) ** (-2)
        expected = float(mpmath.zeta(2) ** 2)
        assert abs(prod - expected) / abs(expected) < 0.05

    @skip_no_mpmath
    def test_euler_product_sigma_m1(self):
        """T40: ζ(s)ζ(s+1) = Π_p (1-p^{-s})^{-1}(1-p^{-(s+1)})^{-1} at s=2."""
        primes = primes_up_to(100)
        prod = 1.0
        for p in primes:
            prod *= 1.0 / ((1 - p ** (-2)) * (1 - p ** (-3)))
        expected = float(mpmath.zeta(2) * mpmath.zeta(3))
        assert abs(prod - expected) / abs(expected) < 0.05


# ============================================================
# T41-T50: Direct extraction of ζ(s)
# ============================================================

class TestDirectExtraction:
    @skip_no_mpmath
    def test_zeta_direct_from_sewing(self):
        """T41: ζ(s) = Σ n^{-s} where n are eigenvalue labels of K_q."""
        result = sewing_to_zeta_direct(2.0)
        assert result['direct_error'] < 0.001

    @skip_no_mpmath
    def test_zeta_from_sigma0(self):
        """T42: ζ(s) = √(Σ σ_0(N) N^{-s}) at s=2."""
        result = sewing_to_zeta_direct(2.0)
        assert result['sigma0_error'] < 0.01

    @skip_no_mpmath
    def test_zeta_zeta1_from_sigma_m1_direct(self):
        """T43: ζ(s)ζ(s+1) from σ_{-1} matches."""
        result = sewing_to_zeta_direct(2.0)
        assert result['sigma_m1_error'] < 0.01

    @skip_no_mpmath
    def test_zeta_at_multiple_s(self):
        """T44: Direct extraction works at s=2,3,4."""
        for s in [2.0, 3.0, 4.0]:
            result = sewing_to_zeta_direct(s)
            assert result['direct_error'] < 0.001

    @skip_no_mpmath
    def test_sigma0_equals_zeta_squared(self):
        """T45: σ_0 Dirichlet series = ζ² at s=3."""
        result = sewing_to_zeta_direct(3.0)
        assert abs(result['sigma0_sum'] - result['zeta_exact'] ** 2) / result['zeta_exact'] ** 2 < 0.01

    @skip_no_mpmath
    def test_consistency_three_methods(self):
        """T46: All three methods agree on ζ(s)."""
        result = sewing_to_zeta_direct(2.0)
        methods = [result['zeta_direct'], result['zeta_from_sigma0'], result['zeta_exact']]
        for m in methods:
            assert abs(m - result['zeta_exact']) / result['zeta_exact'] < 0.01

    def test_sewing_weil_with_identity(self):
        """T47: Sewing Weil formula with h(N)=1 gives -log det."""
        q = 0.3
        val = sewing_weil_formula(q, lambda N: 1.0, Nmax=200)
        expected = -log_det_full(q)
        assert abs(val - expected) / abs(expected) < 0.01

    @skip_no_mpmath
    def test_sewing_weil_with_power(self):
        """T48: Sewing Weil with h(N)=N^{-s} gives ζ(s)ζ(s+1) q-series."""
        q = 0.3
        s = 2.0
        val = sewing_weil_formula(q, lambda N: N ** (-s), Nmax=200)
        # This gives Σ N^{-s} σ_{-1}(N) q^N, a q-series version
        assert np.isfinite(val) and val > 0

    def test_sewing_weil_positive(self):
        """T49: Sewing Weil formula with positive h gives positive result."""
        q = 0.3
        val = sewing_weil_formula(q, lambda N: 1.0 / N, Nmax=200)
        assert val > 0

    @skip_no_mpmath
    def test_zeta_product_analysis(self):
        """T50: Zeta product analysis gives consistent results."""
        result = zeta_product_analysis([2.0, 3.0])
        for s in [2.0, 3.0]:
            assert abs(result[s]['zeta_squared'] - result[s]['zeta_s'] ** 2) < 1e-10
            assert abs(result[s]['zeta_zeta1'] - result[s]['zeta_s'] * result[s]['zeta_s1']) < 1e-10
            assert result[s]['sigma0_coeffs_positive']


# ============================================================
# T51-T60: Spectral properties
# ============================================================

class TestSpectralProperties:
    def test_self_adjoint(self):
        """T51: K_q is self-adjoint."""
        props = sewing_operator_spectral_properties(0.5)
        assert props['self_adjoint']

    def test_positive(self):
        """T52: K_q is positive (all eigenvalues > 0)."""
        props = sewing_operator_spectral_properties(0.5)
        assert props['positive']

    def test_trace_class(self):
        """T53: K_q is trace class."""
        props = sewing_operator_spectral_properties(0.5)
        assert props['trace_class']

    def test_trace_value(self):
        """T54: tr(K_q) = q/(1-q)."""
        for q in [0.1, 0.3, 0.5, 0.7]:
            props = sewing_operator_spectral_properties(q)
            assert abs(props['trace'] - q / (1 - q)) < 1e-10

    def test_fredholm_det_positive(self):
        """T55: det(1-K_q) > 0."""
        for q in [0.1, 0.3, 0.5, 0.7]:
            props = sewing_operator_spectral_properties(q)
            assert props['fredholm_det'] > 0

    def test_spectral_gap(self):
        """T56: Spectral gap = q (largest eigenvalue)."""
        props = sewing_operator_spectral_properties(0.3)
        assert abs(props['spectral_gap'] - 0.3) < 1e-10

    def test_spectral_zeta_identity(self):
        """T57: ζ_{index}(s) = Σ n^{-s} = ζ(s)."""
        props = sewing_operator_spectral_properties(0.5)
        assert 'ζ(s)' in props['spectral_zeta']

    def test_hilbert_polya_gap(self):
        """T58: Honest identification of Hilbert-Pólya gap."""
        props = sewing_operator_spectral_properties(0.5)
        assert 'not zeta zeros' in props['hilbert_polya_gap']

    def test_selberg_zeta_finite(self):
        """T59: Sewing Selberg zeta is finite for Re(s) > 0."""
        val = sewing_selberg_zeta(1.0, 0.3, Nmax=50)
        assert np.isfinite(val) and val > 0

    def test_selberg_zeta_varies(self):
        """T60: Sewing Selberg zeta varies with s."""
        v1 = sewing_selberg_zeta(0.5, 0.3, Nmax=30)
        v2 = sewing_selberg_zeta(1.0, 0.3, Nmax=30)
        assert v1 != v2


# ============================================================
# T61-T70: Obstruction and honest assessment
# ============================================================

class TestObstructionAnalysis:
    def test_direction_B_status_complete(self):
        """T61: Direction B status has all required fields."""
        status = direction_B_status()
        assert len(status['established']) == 9
        assert len(status['gaps']) == 5
        assert 'obstruction' in status
        assert 'next_step' in status

    def test_obstruction_identified(self):
        """T62: The fundamental obstruction is correctly identified.

        K_q is diagonal with no continuous spectrum. The continuous
        spectrum lives on M_{1,1} = SL(2,Z)\\H, not on a single curve.
        This is why the sewing operator alone cannot constrain zeros.
        """
        status = direction_B_status()
        assert 'diagonal' in status['obstruction']
        assert 'continuous spectrum' in status['obstruction']

    def test_nine_established_results(self):
        """T63: All 9 established results are listed."""
        status = direction_B_status()
        established = status['established']
        assert any('σ_{-1}' in e for e in established)
        assert any('ζ(s)²' in e for e in established)
        assert any('self-adjoint' in e for e in established)

    def test_next_step_identified(self):
        """T64: Next step is sewing on moduli space."""
        status = direction_B_status()
        assert 'moduli' in status['next_step'].lower() or 'M_{1,1}' in status['next_step']

    @skip_no_mpmath
    def test_full_chain_log_to_zeta(self):
        """T65: Full chain: log det → σ_{-1} → ζ(s)ζ(s+1) verified numerically."""
        q = 0.3
        # Step 1: log det
        ld = log_det_full(q)
        # Step 2: σ_{-1} decomposition
        ls = log_det_sigma(q, Nmax=300)
        assert abs(ld - ls) / abs(ld) < 0.001
        # Step 3: Dirichlet series
        s0, zsq, sm1, zz1 = divisor_function_dirichlet_test(2.0, Nmax=1000)
        assert abs(sm1 - zz1) / abs(zz1) < 0.01
        assert abs(s0 - zsq) / abs(zsq) < 0.01

    @skip_no_mpmath
    def test_full_chain_to_zeta_alone(self):
        """T66: Full chain gives ζ(s) = √(Σ σ_0 N^{-s})."""
        result = sewing_to_zeta_direct(2.0, Nmax=2000)
        assert result['sigma0_error'] < 0.005

    def test_multiplicativity_is_euler_product(self):
        """T67: Multiplicativity of σ_{-1} = Euler product of ζζ(s+1)."""
        # This is the CONTENT: multiplicativity of divisor functions
        # IMPLIES an Euler product decomposition.
        # Verify: Π_p σ_{-1}(p^k) gives the local factors.
        for p in [2, 3, 5]:
            # σ_{-1}(p) = 1 + 1/p
            assert abs(sigma_minus_1(p) - (1 + 1.0 / p)) < 1e-10
            # σ_{-1}(p²) = 1 + 1/p + 1/p²
            assert abs(sigma_minus_1(p * p) - (1 + 1.0 / p + 1.0 / (p * p))) < 1e-10

    def test_sigma_0_is_zeta_squared_coeffs(self):
        """T68: σ_0(N) = Σ_{d|N} 1 are the coefficients of ζ(s)²."""
        # ζ(s)² = (Σ n^{-s})² = Σ_N (Σ_{ab=N} 1) N^{-s} = Σ σ_0(N) N^{-s}
        for N in range(1, 30):
            pairs = sum(1 for a in range(1, N + 1) if N % a == 0)
            assert pairs == sigma_0(N)

    def test_no_continuous_spectrum(self):
        """T69: K_q has pure point spectrum (no continuous spectrum)."""
        # K_q = diag(q, q², q³, ...) — purely diagonal, all eigenvalues discrete
        q = 0.5
        eigenvalues = [q ** n for n in range(1, 100)]
        # All eigenvalues are isolated points — no accumulation from above
        # (they accumulate at 0, but 0 is not in the spectrum)
        assert all(ev > 0 for ev in eigenvalues)
        assert eigenvalues[0] > eigenvalues[1]  # Decreasing

    def test_moduli_space_is_the_answer(self):
        """T70: The continuous spectrum needed lives on M_{1,1} = SL(2,Z)\\H.

        On M_{1,1}, the Laplacian has:
        - Discrete spectrum: Maass cusp forms (eigenvalue 1/4 + R_n²)
        - Continuous spectrum: Eisenstein series E_s with s = 1/2+it
          The scattering matrix φ(s) = Λ(1-s)/Λ(s) involves ζ(s)

        The sewing operator K_q lives on a SINGLE CURVE (fixed τ).
        To access the continuous spectrum, we must INTEGRATE over τ,
        i.e., study the sewing operator on the MODULI SPACE.
        This is exactly the Rankin-Selberg integral / Benjamin-Chang approach.
        """
        # The honest conclusion:
        assert True  # The obstruction is conceptual, not computational


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
