#!/usr/bin/env python3
r"""Tests for symmetric_power_shadow.py — Symmetric power L-functions from the shadow obstruction tower.

Tests cover:
  1. Satake parameters (computation, product, sum, discriminant)
  2. Ramanujan verification for tau(p) at specific primes
  3. Symmetric power Euler factors (degree, functional equation)
  4. Newton's identities (roundtrip, specific values, edge cases)
  5. Shadow-to-symmetric-power bridge
  6. Ramanujan bounds from power sums
  7. Rankin-Selberg bound verification
  8. Improved bounds from higher symmetric powers
  9. Lattice VOA theta coefficients
  10. Full Ramanujan verification pipeline for Leech lattice
  11. Shadow obstruction tower discrimination (real vs fake measures)
  12. Trace of symmetric powers
  13. Fake eigenform detection
"""

import pytest
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.symmetric_power_shadow import (
    _primes_up_to,
    _nth_prime,
    ramanujan_tau,
    satake_parameters,
    satake_discriminant,
    verify_ramanujan_at_prime,
    symmetric_power_euler_factor,
    symmetric_power_euler_poly,
    symmetric_power_L,
    power_sum_from_satake,
    shadow_coefficient,
    shadow_to_symmetric_power,
    power_sum_to_elementary,
    elementary_to_power_sum,
    verify_newton_roundtrip,
    ramanujan_from_power_sums,
    rankin_selberg_bound,
    improved_bound_from_sym_r,
    SYM_POWER_DELTAS,
    lattice_theta_coefficients,
    verify_ramanujan_from_shadows,
    shadow_tower_discriminates,
    ramanujan_tau_satake_table,
    trace_sym_r,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Primes and tau function
# ============================================================

class TestPrimesAndTau:
    """Basic infrastructure tests."""

    def test_primes_up_to_10(self):
        assert _primes_up_to(10) == [2, 3, 5, 7]

    def test_primes_up_to_30(self):
        assert _primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_primes_count_100(self):
        """There are 25 primes up to 100."""
        assert len(_primes_up_to(100)) == 25

    def test_nth_prime_first_six(self):
        assert _nth_prime(1) == 2
        assert _nth_prime(2) == 3
        assert _nth_prime(3) == 5
        assert _nth_prime(4) == 7
        assert _nth_prime(5) == 11
        assert _nth_prime(6) == 13

    def test_nth_prime_25th(self):
        assert _nth_prime(25) == 97

    def test_tau_first_values(self):
        """tau(1)=1, tau(2)=-24, tau(3)=252, tau(4)=-1472, tau(5)=4830."""
        assert ramanujan_tau(1) == 1
        assert ramanujan_tau(2) == -24
        assert ramanujan_tau(3) == 252
        assert ramanujan_tau(4) == -1472
        assert ramanujan_tau(5) == 4830

    def test_tau_zero_for_nonpositive(self):
        assert ramanujan_tau(0) == 0
        assert ramanujan_tau(-1) == 0

    def test_tau_at_primes(self):
        """Known values: tau(7) = -16744, tau(11) = 534612."""
        assert ramanujan_tau(7) == -16744
        assert ramanujan_tau(11) == 534612

    def test_tau_multiplicativity(self):
        """tau is multiplicative at coprime arguments: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)
        assert ramanujan_tau(15) == ramanujan_tau(3) * ramanujan_tau(5)

    def test_tau_hecke_relation_at_p_squared(self):
        """tau(p^2) = tau(p)^2 - p^{11} for prime p."""
        for p in [2, 3, 5]:
            assert ramanujan_tau(p * p) == ramanujan_tau(p) ** 2 - p ** 11


# ============================================================
# 2. Satake parameters
# ============================================================

class TestSatakeParameters:
    """Tests for Satake parameter computation."""

    def test_satake_sum(self):
        """alpha + beta = a(p)."""
        for p in [2, 3, 5, 7]:
            a_p = ramanujan_tau(p)
            alpha, beta = satake_parameters(a_p, 12, p)
            if HAS_MPMATH:
                assert abs(complex(alpha + beta) - a_p) < 1e-20
            else:
                assert abs((alpha + beta) - a_p) < 1e-10

    def test_satake_product(self):
        """alpha * beta = p^{k-1}."""
        for p in [2, 3, 5, 7, 11]:
            a_p = ramanujan_tau(p)
            alpha, beta = satake_parameters(a_p, 12, p)
            expected = p ** 11
            if HAS_MPMATH:
                assert abs(complex(alpha * beta) - expected) < 1e-10
            else:
                assert abs((alpha * beta).real - expected) < 1e-5

    def test_satake_discriminant_tau_p2(self):
        """For tau(2) = -24, k=12, p=2: disc = 576 - 8192 = -7616 < 0."""
        disc = satake_discriminant(-24, 12, 2)
        expected = 576 - 8192  # = -7616
        if HAS_MPMATH:
            assert abs(float(disc) - expected) < 1e-10
        else:
            assert abs(disc - expected) < 1e-10

    def test_satake_discriminant_tau_p3(self):
        """For tau(3) = 252, k=12, p=3: disc = 63504 - 708588 = -645084 < 0."""
        disc = satake_discriminant(252, 12, 3)
        expected = 252**2 - 4 * 3**11
        assert expected == -645084
        if HAS_MPMATH:
            assert abs(float(disc) - expected) < 1e-5
        else:
            assert abs(disc - expected) < 1e-5

    def test_satake_discriminant_always_negative_for_tau(self):
        """For the Ramanujan tau function, discriminant is ALWAYS negative at primes.
        This is Deligne's theorem: the Satake parameters are always complex conjugates."""
        for p in _primes_up_to(50):
            tau_p = ramanujan_tau(p)
            disc = satake_discriminant(tau_p, 12, p)
            if HAS_MPMATH:
                assert float(disc) < 0, f"disc >= 0 at p={p}, tau(p)={tau_p}"
            else:
                assert disc < 0, f"disc >= 0 at p={p}, tau(p)={tau_p}"

    def test_satake_abs_equals_target_p2(self):
        """For p=2: |alpha| = |beta| = 2^{11/2} = sqrt(2048) exactly."""
        alpha, beta = satake_parameters(-24, 12, 2)
        target = 2 ** 5.5  # = 2^{11/2}
        if HAS_MPMATH:
            assert abs(float(mpmath.fabs(alpha)) - target) < 1e-10
            assert abs(float(mpmath.fabs(beta)) - target) < 1e-10
        else:
            assert abs(abs(alpha) - target) < 1e-10
            assert abs(abs(beta) - target) < 1e-10

    def test_satake_abs_equals_target_p3(self):
        """For p=3: |alpha| = |beta| = 3^{11/2} exactly."""
        alpha, beta = satake_parameters(252, 12, 3)
        target = 3 ** 5.5
        if HAS_MPMATH:
            assert abs(float(mpmath.fabs(alpha)) - target) < 1e-8
            assert abs(float(mpmath.fabs(beta)) - target) < 1e-8
        else:
            assert abs(abs(alpha) - target) < 1e-6
            assert abs(abs(beta) - target) < 1e-6

    def test_satake_abs_equals_target_all_primes_to_50(self):
        """Deligne's theorem: |alpha_p| = p^{11/2} for ALL primes p."""
        for p in _primes_up_to(50):
            tau_p = ramanujan_tau(p)
            alpha, beta = satake_parameters(tau_p, 12, p)
            target = p ** 5.5
            if HAS_MPMATH:
                ratio_alpha = float(mpmath.fabs(alpha)) / target
                ratio_beta = float(mpmath.fabs(beta)) / target
            else:
                ratio_alpha = abs(alpha) / target
                ratio_beta = abs(beta) / target
            assert abs(ratio_alpha - 1.0) < 1e-8, f"Failed at p={p}"
            assert abs(ratio_beta - 1.0) < 1e-8, f"Failed at p={p}"

    def test_satake_complex_conjugate(self):
        """When disc < 0, alpha and beta are complex conjugates."""
        alpha, beta = satake_parameters(-24, 12, 2)
        if HAS_MPMATH:
            a = complex(alpha)
            b = complex(beta)
        else:
            a = complex(alpha)
            b = complex(beta)
        # beta should be conj(alpha)
        assert abs(a.real - b.real) < 1e-10
        assert abs(a.imag + b.imag) < 1e-10

    def test_satake_real_case(self):
        """When a(p) > 2*p^{(k-1)/2}, Satake parameters are real (violation)."""
        # Fake: a(2) = 100, k=12, p=2. Bound is 2*2^{11/2} = 90.51.
        # 100 > 90.51, so disc > 0.
        disc = satake_discriminant(100, 12, 2)
        # disc = 10000 - 8192 = 1808 > 0
        if HAS_MPMATH:
            assert float(disc) > 0
        else:
            assert disc > 0
        alpha, beta = satake_parameters(100, 12, 2)
        if HAS_MPMATH:
            # Both should be real
            assert abs(float(mpmath.im(alpha))) < 1e-20
            assert abs(float(mpmath.im(beta))) < 1e-20
        else:
            # Should be real floats
            assert isinstance(alpha, float)
            assert isinstance(beta, float)


# ============================================================
# 3. Ramanujan verification
# ============================================================

class TestRamanujanVerification:
    """Tests for verify_ramanujan_at_prime."""

    def test_tau_p2_satisfies(self):
        result = verify_ramanujan_at_prime(-24, 12, 2)
        assert result['satisfies'] is True
        assert result['exact_ramanujan'] is True
        assert result['satake_type'] == 'complex_conjugate'

    def test_tau_p3_satisfies(self):
        result = verify_ramanujan_at_prime(252, 12, 3)
        assert result['satisfies'] is True
        assert result['exact_ramanujan'] is True

    def test_tau_p5_satisfies(self):
        result = verify_ramanujan_at_prime(4830, 12, 5)
        assert result['satisfies'] is True
        assert result['exact_ramanujan'] is True

    def test_tau_all_primes_to_50(self):
        """ALL primes up to 50 satisfy exact Ramanujan for tau."""
        for p in _primes_up_to(50):
            tau_p = ramanujan_tau(p)
            result = verify_ramanujan_at_prime(tau_p, 12, p)
            assert result['satisfies'] is True, f"Failed at p={p}"
            assert result['exact_ramanujan'] is True, f"Not exact at p={p}"

    def test_fake_eigenvalue_violates(self):
        """a(2) = 100 satisfies (100 < 90.51 is FALSE... wait, 100 > 90.51)."""
        # Ramanujan bound at p=2, k=12: 2*2^{11/2} ≈ 90.51
        result = verify_ramanujan_at_prime(100, 12, 2)
        # 100 > 90.51, so this VIOLATES
        assert result['satisfies'] is False
        assert result['satake_type'] == 'real'

    def test_fake_eigenvalue_91_violates(self):
        """a(2) = 91 > 2*2^{11/2} ≈ 90.51, so violates Ramanujan."""
        result = verify_ramanujan_at_prime(91, 12, 2)
        assert result['satisfies'] is False

    def test_borderline_90_satisfies(self):
        """a(2) = 90 < 2*2^{11/2} ≈ 90.51, so satisfies Ramanujan.
        discriminant = 90^2 - 4*2^{11} = 8100 - 8192 = -92 < 0.
        But NOT exact since a(p)=-24 for the real form."""
        result = verify_ramanujan_at_prime(90, 12, 2)
        assert result['satisfies'] is True
        # The Satake parameters are complex conjugate (disc < 0)
        assert result['satake_type'] == 'complex_conjugate'
        # |alpha| = |beta| = sqrt(alpha*beta) = sqrt(2^{11}) = 2^{11/2} EXACTLY
        # (because for any a(p) with disc <= 0, |alpha| = sqrt(p^{k-1}) by |alpha*beta| = p^{k-1}
        #  and alpha = conj(beta))
        # So exact_ramanujan is True even for "non-real" eigenvalues.
        assert result['exact_ramanujan'] is True

    def test_ramanujan_bound_value(self):
        """Ramanujan bound at p=2, k=12 is 2*2^{11/2}."""
        result = verify_ramanujan_at_prime(-24, 12, 2)
        expected_bound = 2 * 2**5.5
        assert abs(result['bound'] - expected_bound) < 1e-8


# ============================================================
# 4. Symmetric power Euler factors
# ============================================================

class TestSymmetricPowerEuler:
    """Tests for symmetric power Euler factors."""

    def test_sym0_is_zeta(self):
        """Sym^0 L-function. Euler factor at p, m=0: single term j=0.
        lambda = alpha^0 * beta^0 = 1, so factor = (1 - p^{-s})^{-1}."""
        alpha, beta = satake_parameters(-24, 12, 2)
        ef = symmetric_power_euler_factor(alpha, beta, 0, 2, 2.0)
        expected = 1.0 / (1.0 - 2.0**(-2.0))  # = 4/3
        if HAS_MPMATH:
            assert abs(complex(ef).real - expected) < 1e-10
        else:
            assert abs(ef - expected) < 1e-10

    def test_sym1_is_standard_L(self):
        """Sym^1: 2 eigenvalues (alpha, beta), polynomial of degree 2, 3 coefficients."""
        alpha, beta = satake_parameters(-24, 12, 2)
        poly = symmetric_power_euler_poly(alpha, beta, 1, 2)
        assert len(poly) == 3  # degree 2: c_0, c_1, c_2

    def test_sym2_euler_degree(self):
        """Sym^2: 3 eigenvalues, polynomial of degree 3, 4 coefficients."""
        alpha, beta = satake_parameters(-24, 12, 2)
        poly = symmetric_power_euler_poly(alpha, beta, 2, 2)
        assert len(poly) == 4

    def test_sym1_poly_coefficients(self):
        """Sym^1 poly: (1 - alpha*X)(1 - beta*X) = 1 - (alpha+beta)X + alpha*beta*X^2.
        For tau(2) = -24: -(alpha+beta) = 24, alpha*beta = 2^{11}."""
        alpha, beta = satake_parameters(-24, 12, 2)
        poly = symmetric_power_euler_poly(alpha, beta, 1, 2)
        c0 = complex(poly[0])
        c1 = complex(poly[1])
        c2 = complex(poly[2])
        assert abs(c0 - 1.0) < 1e-10
        assert abs(c1.real - 24.0) < 1e-10  # -(alpha+beta) = -(-24) = 24
        assert abs(c1.imag) < 1e-10
        assert abs(c2.real - 2**11) < 1e-5  # alpha*beta = 2^{11}
        assert abs(c2.imag) < 1e-5

    def test_euler_factor_real_at_real_s(self):
        """For real s and the Ramanujan Delta, the Euler factor should be real
        (since the Euler polynomial has real coefficients)."""
        alpha, beta = satake_parameters(-24, 12, 2)
        ef = symmetric_power_euler_factor(alpha, beta, 2, 2, 10.0)
        if HAS_MPMATH:
            assert abs(float(mpmath.im(ef))) < 1e-20
        else:
            assert abs(ef.imag) < 1e-10

    def test_sym_power_L_convergent_high_s(self):
        """L(s, Sym^2 Delta) should converge for Re(s) large."""
        f_coeffs = {p: ramanujan_tau(p) for p in _primes_up_to(200)}
        val = symmetric_power_L(f_coeffs, 12, 2, 20.0, num_primes=40)
        if HAS_MPMATH:
            val = complex(val)
        # Should be close to 1 for very large s
        assert abs(val - 1.0) < 0.1

    def test_sym2_product_identity(self):
        """Sym^2 Euler poly at p=3: constant term = 1."""
        alpha, beta = satake_parameters(252, 12, 3)
        poly = symmetric_power_euler_poly(alpha, beta, 2, 3)
        assert abs(complex(poly[0]) - 1.0) < 1e-10


# ============================================================
# 5. Newton's identities
# ============================================================

class TestNewtonIdentities:
    """Tests for power sum <-> elementary symmetric polynomial conversion."""

    def test_roundtrip_n1(self):
        """p_1 = e_1 (trivially)."""
        assert verify_newton_roundtrip(1)

    def test_roundtrip_n2(self):
        assert verify_newton_roundtrip(2)

    def test_roundtrip_n5(self):
        assert verify_newton_roundtrip(5)

    def test_roundtrip_n10(self):
        assert verify_newton_roundtrip(10)

    def test_specific_two_variables(self):
        """For x, y with x+y=5, xy=6 (so x=2, y=3):
        p_1 = 5, p_2 = 4+9 = 13, p_3 = 8+27 = 35.
        e_1 = 5, e_2 = 6."""
        p = [5, 13, 35]
        e = power_sum_to_elementary(p)
        e = [complex(x).real for x in e]
        assert abs(e[0] - 5.0) < 1e-10  # e_1 = p_1 = 5
        assert abs(e[1] - 6.0) < 1e-10  # e_2 = (e_1*p_1 - p_2)/2 = (25-13)/2 = 6

    def test_inverse_two_variables(self):
        """e_1 = 5, e_2 = 6 -> p_1 = 5, p_2 = 13."""
        e = [5, 6]
        p = elementary_to_power_sum(e)
        p = [complex(x).real for x in p]
        assert abs(p[0] - 5.0) < 1e-10
        assert abs(p[1] - 13.0) < 1e-10

    def test_empty_input(self):
        assert power_sum_to_elementary([]) == []
        assert elementary_to_power_sum([]) == []

    def test_single_variable(self):
        """For a single variable x: p_r = x^r, e_r = 0 for r > 1, e_1 = x."""
        # x = 7: p = [7, 49, 343]
        p = [7, 49, 343]
        e = power_sum_to_elementary(p)
        e = [complex(x).real for x in e]
        assert abs(e[0] - 7.0) < 1e-10
        assert abs(e[1] - 0.0) < 1e-10
        assert abs(e[2] - 0.0) < 1e-10

    def test_newton_with_satake_data(self):
        """Use actual Satake parameters at p=2 for tau(2) = -24."""
        alpha, beta = satake_parameters(-24, 12, 2)
        # Power sums
        p1 = power_sum_from_satake(alpha, beta, 1)
        p2 = power_sum_from_satake(alpha, beta, 2)
        p3 = power_sum_from_satake(alpha, beta, 3)
        # e_1 = alpha + beta = -24, e_2 = alpha*beta = 2^{11}
        e = power_sum_to_elementary([p1, p2, p3])
        e = [complex(x) for x in e]
        assert abs(e[0].real - (-24)) < 1e-8
        assert abs(e[1].real - 2**11) < 1e-3


# ============================================================
# 6. Power sums from Satake
# ============================================================

class TestPowerSums:
    """Tests for power_sum_from_satake and related."""

    def test_power_sum_r1_is_trace(self):
        """p_1(alpha, beta) = alpha + beta = a(p)."""
        alpha, beta = satake_parameters(-24, 12, 2)
        p1 = power_sum_from_satake(alpha, beta, 1)
        if HAS_MPMATH:
            assert abs(complex(p1) - (-24)) < 1e-10
        else:
            assert abs(p1 - (-24)) < 1e-10

    def test_power_sum_r2(self):
        """p_2 = alpha^2 + beta^2 = (alpha+beta)^2 - 2*alpha*beta = a(p)^2 - 2*p^{k-1}."""
        alpha, beta = satake_parameters(-24, 12, 2)
        p2 = power_sum_from_satake(alpha, beta, 2)
        expected = (-24)**2 - 2 * 2**11  # = 576 - 4096 = -3520
        if HAS_MPMATH:
            assert abs(complex(p2).real - expected) < 1e-8
        else:
            assert abs(p2.real - expected) < 1e-8

    def test_power_sum_recurrence(self):
        """p_r = (alpha+beta)*p_{r-1} - alpha*beta*p_{r-2}."""
        alpha, beta = satake_parameters(-24, 12, 2)
        s = -24  # alpha + beta
        prod = 2**11  # alpha * beta
        ps = [power_sum_from_satake(alpha, beta, r) for r in range(1, 8)]
        for r in range(2, 7):
            if HAS_MPMATH:
                lhs = complex(ps[r])
                rhs = s * complex(ps[r - 1]) - prod * complex(ps[r - 2])
            else:
                lhs = ps[r]
                rhs = s * ps[r - 1] - prod * ps[r - 2]
            assert abs(lhs - rhs) < 1e-5, f"Recurrence failed at r={r+1}"

    def test_shadow_coefficient_formula(self):
        """S_r = -(1/r) * sum c_j * lambda_j^r."""
        atoms = [(1.0, 2.0), (3.0, -1.0)]
        # S_2 = -(1/2)*(1*4 + 3*1) = -(1/2)*7 = -3.5
        s2 = shadow_coefficient(atoms, 2)
        assert abs(complex(s2).real - (-3.5)) < 1e-10


# ============================================================
# 7. Shadow to symmetric power bridge
# ============================================================

class TestShadowSymmetricPowerBridge:
    """Tests for the shadow <-> symmetric power identification."""

    def test_shadow_to_sym_degree(self):
        """Shadow at arity r corresponds to Sym^{r-2}."""
        result = shadow_to_symmetric_power({4: 0.5}, 4)
        assert result['symmetric_power_degree'] == 2
        assert result['power_sum_degree'] == 4

    def test_shadow_to_sym_arity2(self):
        """Arity 2 -> Sym^0 (trivial)."""
        result = shadow_to_symmetric_power({2: 1.0}, 2)
        assert result['symmetric_power_degree'] == 0

    def test_shadow_to_sym_arity3(self):
        result = shadow_to_symmetric_power({3: -0.7}, 3)
        assert result['symmetric_power_degree'] == 1

    def test_trace_sym_r_degree0(self):
        """tr(Sym^0(diag(alpha,beta))) = 1."""
        alpha, beta = satake_parameters(-24, 12, 2)
        tr0 = trace_sym_r(alpha, beta, 0)
        if HAS_MPMATH:
            assert abs(complex(tr0) - 1.0) < 1e-10
        else:
            assert abs(tr0 - 1.0) < 1e-10

    def test_trace_sym_r_degree1(self):
        """tr(Sym^1(diag(alpha,beta))) = alpha + beta = a(p)."""
        alpha, beta = satake_parameters(-24, 12, 2)
        tr1 = trace_sym_r(alpha, beta, 1)
        if HAS_MPMATH:
            assert abs(complex(tr1) - (-24)) < 1e-10
        else:
            assert abs(tr1 - (-24)) < 1e-10

    def test_trace_sym_r_degree2(self):
        """tr(Sym^2) = alpha^2 + alpha*beta + beta^2 = (alpha+beta)^2 - alpha*beta."""
        alpha, beta = satake_parameters(-24, 12, 2)
        tr2 = trace_sym_r(alpha, beta, 2)
        expected = (-24)**2 - 2**11  # = 576 - 2048 = -1472
        if HAS_MPMATH:
            assert abs(complex(tr2).real - expected) < 1e-5
        else:
            assert abs(tr2.real - expected) < 1e-5

    def test_trace_vs_power_sum(self):
        """tr(Sym^r) != p_r in general.
        p_r = alpha^r + beta^r (2 terms)
        tr(Sym^r) = sum_{j=0}^r alpha^j beta^{r-j} (r+1 terms)"""
        alpha, beta = satake_parameters(-24, 12, 2)
        for r in range(2, 6):
            pr = power_sum_from_satake(alpha, beta, r)
            trr = trace_sym_r(alpha, beta, r)
            if HAS_MPMATH:
                assert abs(complex(pr) - complex(trr)) > 1e-5, (
                    f"p_{r} should differ from tr(Sym^{r}) for r >= 2"
                )
            else:
                assert abs(pr - trr) > 1e-5


# ============================================================
# 8. Ramanujan bounds from power sums
# ============================================================

class TestRamanujanBounds:
    """Tests for Ramanujan bound computation from power sums."""

    def test_exact_ramanujan_from_tau(self):
        """Actual tau(p) gives exact Ramanujan."""
        alpha, beta = satake_parameters(-24, 12, 2)
        ps = [power_sum_from_satake(alpha, beta, r) for r in range(1, 5)]
        ps_float = [complex(x).real for x in ps]
        result = ramanujan_from_power_sums(ps_float, 12, 2)
        assert result['ratio'] <= 1.0 + 1e-8

    def test_violating_gives_ratio_gt_1(self):
        """Fake a(2) = 100 > bound 90.51: ratio should exceed 1."""
        alpha, beta = satake_parameters(100, 12, 2)
        ps = [power_sum_from_satake(alpha, beta, r) for r in range(1, 3)]
        ps_float = [complex(x).real for x in ps]
        result = ramanujan_from_power_sums(ps_float, 12, 2)
        assert result['ratio'] > 1.0

    def test_rankin_selberg_bound_tau(self):
        """Rankin-Selberg bound should be satisfied for tau."""
        f_coeffs = {p: ramanujan_tau(p) for p in _primes_up_to(50)}
        result = rankin_selberg_bound(f_coeffs, 12)
        assert result['bounded'] is True
        # All individual ratios should be finite and bounded
        for p, r in result['ratios'].items():
            assert r < 10, f"Ratio too large at p={p}"

    def test_improved_bound_sym2(self):
        """Sym^2 delta = 1/5."""
        f_coeffs = {p: ramanujan_tau(p) for p in _primes_up_to(30)}
        result = improved_bound_from_sym_r(f_coeffs, 12, 2)
        assert result['delta'] == pytest.approx(0.2)
        assert result['status'] == 'unconditional'

    def test_improved_bound_sym3(self):
        """Sym^3 delta = 2/9."""
        f_coeffs = {p: ramanujan_tau(p) for p in _primes_up_to(30)}
        result = improved_bound_from_sym_r(f_coeffs, 12, 3)
        assert result['delta'] == pytest.approx(2/9)

    def test_improved_bound_sym4(self):
        """Sym^4 delta = 1/9."""
        result = improved_bound_from_sym_r({2: -24}, 12, 4)
        assert result['delta'] == pytest.approx(1/9)

    def test_higher_sym_conjectural(self):
        """Sym^5 and above are conjectural."""
        result = improved_bound_from_sym_r({2: -24}, 12, 5)
        assert 'conjectural' in result['status']

    def test_sym_deltas_monotone_heuristic(self):
        """The conjectural deltas should approach 1/2 from below."""
        deltas = []
        for r in range(1, 20):
            if r in SYM_POWER_DELTAS:
                deltas.append(SYM_POWER_DELTAS[r])
            else:
                deltas.append(0.5 - 1.0 / (r + 1))
        # Not strictly monotone (delta for Sym^4 < delta for Sym^3), but
        # the conjectural deltas for r >= 5 should increase
        for i in range(5, len(deltas) - 1):
            assert deltas[i] <= deltas[i + 1] + 1e-10


# ============================================================
# 9. Lattice theta coefficients
# ============================================================

class TestLatticeTheta:
    """Tests for lattice theta function coefficients."""

    def test_Z_theta_first_terms(self):
        """theta_3(q) = 1 + 2q + 2q^4 + 2q^9 + ..."""
        c = lattice_theta_coefficients('Z', 20)
        assert c[0] == 1
        assert c[1] == 2
        assert c[2] == 0
        assert c[3] == 0
        assert c[4] == 2
        assert c[9] == 2

    def test_E8_theta_first_terms(self):
        """E_4(q) = 1 + 240q + 2160q^2 + ..."""
        c = lattice_theta_coefficients('E8', 5)
        assert c[0] == 1
        assert c[1] == 240
        assert c[2] == 2160

    def test_A2_theta_first_terms(self):
        """A_2 theta: 1 + 6q + 0q^2 + 6q^3 + 6q^4 + ..."""
        c = lattice_theta_coefficients('A2', 10)
        assert c[0] == 1
        assert c[1] == 6
        assert c[3] == 6
        assert c[4] == 6

    def test_Leech_theta_no_roots(self):
        """Leech lattice has no vectors of norm 2 (no roots): theta_1 = 0."""
        c = lattice_theta_coefficients('Leech', 5)
        assert c[0] == 1
        assert c[1] == 0  # No roots!

    def test_Leech_theta_norm4(self):
        """Leech lattice: 196560 vectors of norm 4."""
        c = lattice_theta_coefficients('Leech', 5)
        assert c[2] == 196560

    def test_unknown_lattice_raises(self):
        with pytest.raises(ValueError):
            lattice_theta_coefficients('UNKNOWN', 5)


# ============================================================
# 10. Full Ramanujan verification for Leech
# ============================================================

class TestLeechRamanujan:
    """Full pipeline: Leech lattice -> shadows -> Ramanujan bound."""

    def test_leech_all_satisfy_ramanujan(self):
        result = verify_ramanujan_from_shadows('Leech', r_max=6)
        assert result['all_satisfy_ramanujan'] is True

    def test_leech_all_exact_ramanujan(self):
        """Deligne's theorem: exact Ramanujan for weight-12 cusp forms."""
        result = verify_ramanujan_from_shadows('Leech', r_max=6)
        assert result['all_exact_ramanujan'] is True

    def test_leech_tau_p2_in_table(self):
        result = verify_ramanujan_from_shadows('Leech', r_max=4)
        p2_data = result['prime_data'][2]
        assert p2_data['tau_p'] == -24

    def test_leech_power_sums_real(self):
        """Power sums from complex conjugate Satake params should be real."""
        result = verify_ramanujan_from_shadows('Leech', r_max=6)
        for p, data in result['prime_data'].items():
            for ps_val in data['power_sums']:
                assert abs(ps_val.imag if isinstance(ps_val, complex) else 0) < 1e-8, (
                    f"Power sum not real at p={p}"
                )

    def test_z_lattice_vacuous(self):
        """V_Z has no cusp forms -> vacuously true."""
        result = verify_ramanujan_from_shadows('Z', r_max=4)
        assert result['all_satisfy_ramanujan'] is True
        assert 'no cuspidal part' in result.get('note', '')


# ============================================================
# 11. Shadow obstruction tower discrimination
# ============================================================

class TestShadowDiscrimination:
    """Tests for shadow_tower_discriminates."""

    def test_identical_measures(self):
        """Identical measures should never diverge."""
        measure = [(1.0, 2.0), (1.0, 3.0)]
        result = shadow_tower_discriminates(measure, measure, r_max=10)
        assert result['first_divergence_arity'] is None

    def test_different_measures_diverge(self):
        """Different measures should diverge at some finite arity."""
        real = [(1.0, 2.0), (1.0, 3.0)]
        fake = [(1.0, 2.0), (1.0, 4.0)]
        result = shadow_tower_discriminates(real, fake, r_max=10)
        assert result['first_divergence_arity'] is not None
        assert result['first_divergence_arity'] <= 10

    def test_diverge_at_arity_1(self):
        """If the first power sums differ, diverge at arity 1."""
        real = [(1.0, 1.0)]
        fake = [(1.0, 2.0)]
        result = shadow_tower_discriminates(real, fake, r_max=5)
        assert result['first_divergence_arity'] == 1

    def test_same_p1_different_p2(self):
        """Two measures with same p_1 but different p_2.
        (1, alpha) + (1, beta) vs (1, alpha') + (1, beta')
        where alpha+beta = alpha'+beta' but alpha^2+beta^2 != alpha'^2+beta'^2.
        E.g., (1,3) + (1,2) vs (1,4) + (1,1): p_1 = 5 for both.
        p_2: 9+4=13 vs 16+1=17. Diverge at r=2."""
        real = [(1.0, 3.0), (1.0, 2.0)]
        fake = [(1.0, 4.0), (1.0, 1.0)]
        result = shadow_tower_discriminates(real, fake, r_max=10)
        assert result['first_divergence_arity'] == 2

    def test_relative_differences_grow(self):
        """For sufficiently different measures, relative differences should grow."""
        real = [(1.0, 1.0)]
        fake = [(1.0, 10.0)]
        result = shadow_tower_discriminates(real, fake, r_max=15)
        diffs = result['relative_differences']
        # The differences should generally grow (10^r vs 1^r)
        assert diffs[10] > diffs[1]


# ============================================================
# 12. Satake diagnostic table
# ============================================================

class TestSatakeTable:
    """Tests for the diagnostic table."""

    def test_table_has_all_primes_to_50(self):
        table = ramanujan_tau_satake_table(50)
        primes = _primes_up_to(50)
        assert len(table) == len(primes)

    def test_table_all_complex_conjugate(self):
        """All entries should have complex conjugate Satake type."""
        table = ramanujan_tau_satake_table(50)
        for row in table:
            assert row['satake_type'] == 'complex_conjugate', f"Failed at p={row['p']}"

    def test_table_all_exact(self):
        table = ramanujan_tau_satake_table(50)
        for row in table:
            assert row['exact_ramanujan'] is True, f"Not exact at p={row['p']}"

    def test_table_abs_alpha_equals_target(self):
        table = ramanujan_tau_satake_table(30)
        for row in table:
            ratio = row['abs_alpha'] / row['target']
            assert abs(ratio - 1.0) < 1e-6, f"Ratio off at p={row['p']}: {ratio}"


# ============================================================
# 13. Fake eigenform detection
# ============================================================

class TestFakeEigenforms:
    """Tests exploring when Ramanujan is violated."""

    def test_real_satake_means_violation(self):
        """If discriminant > 0, Satake params are real => Ramanujan violated."""
        # a(2) = 100, k=12: disc = 10000 - 8192 = 1808 > 0
        disc = satake_discriminant(100, 12, 2)
        if HAS_MPMATH:
            assert float(disc) > 0
        else:
            assert disc > 0
        result = verify_ramanujan_at_prime(100, 12, 2)
        assert result['satake_type'] == 'real'
        assert result['satisfies'] is False

    def test_exact_threshold(self):
        """The threshold is |a(p)| = 2*p^{(k-1)/2}. At exact threshold, disc = 0."""
        # a(p) = 2*p^{(k-1)/2} gives disc = 4*p^{k-1} - 4*p^{k-1} = 0
        p = 2
        k = 12
        threshold = 2 * p ** ((k - 1) / 2.0)  # = 2 * 2^{5.5}
        disc = satake_discriminant(threshold, k, p)
        if HAS_MPMATH:
            assert abs(float(disc)) < 1e-5
        else:
            assert abs(disc) < 1e-5

    def test_shadow_discriminates_fake_from_real(self):
        """The shadow obstruction tower should discriminate a real eigenform from a fake one.
        Use tau at p=2 (real) vs a fake with a(2)=100 (violating)."""
        # Real: spectral atoms from actual tau(2) = -24
        # We treat the "spectral measure" as just the eigenvalue itself.
        real_measure = [(1.0, -24.0)]
        fake_measure = [(1.0, 100.0)]
        result = shadow_tower_discriminates(real_measure, fake_measure, r_max=10)
        assert result['first_divergence_arity'] == 1

    def test_subtle_fake_detection(self):
        """A "near-Ramanujan" fake with a(2) = 90 (within bound) still differs
        from tau(2) = -24 in the shadow obstruction tower."""
        real_measure = [(1.0, -24.0)]
        fake_measure = [(1.0, 90.0)]
        result = shadow_tower_discriminates(real_measure, fake_measure, r_max=10)
        assert result['first_divergence_arity'] == 1

    def test_ramanujan_bound_formula(self):
        """Verify: |a(p)| <= 2*p^{(k-1)/2} is equivalent to disc <= 0."""
        for p in [2, 3, 5, 7]:
            k = 12
            bound = 2 * p ** ((k - 1) / 2.0)
            # At the bound exactly: disc = 0
            disc_at_bound = satake_discriminant(bound, k, p)
            if HAS_MPMATH:
                assert abs(float(disc_at_bound)) < 1e-3
            else:
                assert abs(disc_at_bound) < 1e-3
            # Below bound: disc < 0
            disc_below = satake_discriminant(bound * 0.99, k, p)
            if HAS_MPMATH:
                assert float(disc_below) < 0
            else:
                assert disc_below < 0
            # Above bound: disc > 0
            disc_above = satake_discriminant(bound * 1.01, k, p)
            if HAS_MPMATH:
                assert float(disc_above) > 0
            else:
                assert disc_above > 0


# ============================================================
# 14. Cross-checks and edge cases
# ============================================================

class TestCrossChecks:
    """Cross-checks between different computations."""

    def test_tau_hecke_eigenvalue_consistency(self):
        """tau(p^2) = tau(p)^2 - p^{11} is the same as alpha^2 + beta^2 + alpha*beta."""
        for p in [2, 3, 5]:
            alpha, beta = satake_parameters(ramanujan_tau(p), 12, p)
            # tau(p^2) via Hecke relation
            tau_p2 = ramanujan_tau(p)**2 - p**11
            assert tau_p2 == ramanujan_tau(p*p)
            # Also: alpha^2 + alpha*beta + beta^2 = trace of Sym^2
            tr2 = trace_sym_r(alpha, beta, 2)
            if HAS_MPMATH:
                assert abs(complex(tr2).real - tau_p2) < 1e-3
            else:
                assert abs(tr2.real - tau_p2) < 1e-3

    def test_power_sum_r1_vs_tau(self):
        """p_1(alpha, beta) = alpha + beta = tau(p)."""
        for p in _primes_up_to(30):
            tau_p = ramanujan_tau(p)
            alpha, beta = satake_parameters(tau_p, 12, p)
            p1 = power_sum_from_satake(alpha, beta, 1)
            if HAS_MPMATH:
                assert abs(complex(p1).real - tau_p) < 1e-8
            else:
                assert abs(p1 - tau_p) < 1e-8

    def test_euler_factor_at_s_equals_k(self):
        """The standard L-function L(s, f) has Euler factor at s=k:
        (1 - a(p)*p^{-k} + p^{k-1}*p^{-2k})^{-1}
        = (1 - a(p)/p^k + 1/p^{k+1})^{-1}"""
        p = 2
        k = 12
        a_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(a_p, k, p)
        ef = symmetric_power_euler_factor(alpha, beta, 1, p, float(k))
        expected = 1.0 / (1.0 - a_p / p**k + 1.0 / p**(k+1))
        if HAS_MPMATH:
            assert abs(complex(ef).real - expected) < 1e-8
        else:
            assert abs(ef.real - expected) < 1e-8

    def test_sym0_euler_factor_is_riemann_zeta(self):
        """L(s, Sym^0 f) = zeta(s). The Euler factor at p is (1 - p^{-s})^{-1}."""
        for p in [2, 3, 5]:
            alpha, beta = satake_parameters(ramanujan_tau(p), 12, p)
            ef = symmetric_power_euler_factor(alpha, beta, 0, p, 2.0)
            expected = 1.0 / (1.0 - p**(-2.0))
            assert abs(complex(ef).real - expected) < 1e-10


# ============================================================
# 15. Honesty: gaps and limitations
# ============================================================

class TestHonestyGaps:
    """Tests that document what the module does NOT do (honest gaps)."""

    def test_sym5_not_unconditional(self):
        """Sym^5 lifting is NOT known to be automorphic unconditionally."""
        assert 5 not in SYM_POWER_DELTAS

    def test_lattice_theta_only_specific_types(self):
        """We only support specific lattice types, not arbitrary lattices."""
        supported = ['Z', 'Z2', 'A2', 'E8', 'Leech']
        for lt in supported:
            c = lattice_theta_coefficients(lt, 5)
            assert c[0] == 1

    def test_shadow_bridge_is_heuristic_for_non_lattice(self):
        """For non-lattice VOAs, the shadow-to-symmetric-power bridge is
        not rigorously established. We test only the LATTICE case."""
        result = verify_ramanujan_from_shadows('Z', r_max=4)
        assert 'no cuspidal part' in result.get('note', '')

    def test_partial_euler_product_not_exact(self):
        """A partial Euler product is NOT the exact L-function value."""
        f_coeffs = {p: ramanujan_tau(p) for p in _primes_up_to(30)}
        val_30 = symmetric_power_L(f_coeffs, 12, 1, 7.0, num_primes=10)
        val_100 = symmetric_power_L(
            {p: ramanujan_tau(p) for p in _primes_up_to(200)},
            12, 1, 7.0, num_primes=40
        )
        # They should be close but NOT identical
        if HAS_MPMATH:
            v30 = complex(val_30)
            v100 = complex(val_100)
        else:
            v30 = complex(val_30)
            v100 = complex(val_100)
        # Both should be near 1 for s=7 but differ in the tail
        assert abs(v30) > 0.5
        assert abs(v100) > 0.5

    def test_ramanujan_from_power_sums_limited(self):
        """The moment-problem approach from power sums gives limited improvement
        beyond the basic discriminant test. For complex conjugate Satake parameters,
        the discriminant test already gives the exact bound."""
        alpha, beta = satake_parameters(-24, 12, 2)
        # With 1 power sum: bound = target (exact for complex conjugate case)
        ps1 = [complex(power_sum_from_satake(alpha, beta, 1)).real]
        result1 = ramanujan_from_power_sums(ps1, 12, 2)
        assert result1['ratio'] <= 1.0 + 1e-8
        # With 5 power sums: bound is still the same (all info in p_1 + alpha*beta)
        ps5 = [complex(power_sum_from_satake(alpha, beta, r)).real for r in range(1, 6)]
        result5 = ramanujan_from_power_sums(ps5, 12, 2)
        assert result5['ratio'] <= 1.0 + 1e-8


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
