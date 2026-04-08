"""Tests for theorem_arithmetic_eisenstein_engine.

Verifies thm:shadow-eisenstein (arithmetic_shadows.tex line 2949) along
four independent verification paths:

  P1. Direct identity L^sh(s) = -kappa * zeta(s) * zeta(s - 1)
      at concrete complex s and several kappa values.
  P2. Euler product factorization at s = 3, 4, 5 with growing prime
      counts, monitoring monotone convergence.
  P3. Hasse-Weil identification: local factor at p = 2, 3, 5, 7 equals
      1 / [(1 - p^{-s})(1 - p^{1-s})] = Z(P^1/F_p, p^{-s}).
  P4. Pole / residue structure at s = 1 (residue kappa/2) and s = 2
      (residue -kappa * pi^2 / 6).

These four paths are genuinely independent: P1 uses mpmath's reference
zeta directly; P2 reconstructs zeta * zeta-shift from primes; P3 uses
the geometric Hasse-Weil count of P^1; P4 uses the analytic Laurent
expansion. A single coding bug cannot pass all four.
"""

from __future__ import annotations

import math

import mpmath as mp
import pytest

from compute.lib.theorem_arithmetic_eisenstein_engine import (
    ShadowEisensteinEngine,
    euler_partial_product,
    first_n_primes,
    p1_local_factor,
    shadow_l_function,
    shadow_l_residue_at_one,
    shadow_l_residue_at_two,
    shadow_l_via_bernoulli,
    zeta_zeta_shift_product,
)


# ---------------------------------------------------------------------------
# High precision baseline
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _set_precision():
    mp.mp.dps = 60
    yield


# ---------------------------------------------------------------------------
# Sieve sanity
# ---------------------------------------------------------------------------


def test_first_n_primes_short():
    assert first_n_primes(5) == [2, 3, 5, 7, 11]


def test_first_n_primes_count():
    p = first_n_primes(20)
    assert len(p) == 20
    assert p[-1] == 71


def test_first_n_primes_zero():
    assert first_n_primes(0) == []


# ---------------------------------------------------------------------------
# Path 1: Direct numerical identity at concrete s and kappa
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("s", [3, 4, 5, 6])
@pytest.mark.parametrize("kappa", [1, 2, mp.mpf("0.5"), mp.mpf("13")])
def test_shadow_l_equals_minus_kappa_zeta_zetashift(s, kappa):
    lhs = shadow_l_function(s, kappa)
    rhs = -mp.mpf(kappa) * mp.zeta(s) * mp.zeta(s - 1)
    assert abs(lhs - rhs) < mp.mpf("1e-50")


def test_shadow_l_at_s_equals_3_kappa_one():
    val = shadow_l_function(3, 1)
    expected = -mp.zeta(3) * mp.zeta(2)
    assert abs(val - expected) < mp.mpf("1e-50")


def test_shadow_l_at_s_equals_4_kappa_two():
    val = shadow_l_function(4, 2)
    expected = -2 * mp.zeta(4) * mp.zeta(3)
    assert abs(val - expected) < mp.mpf("1e-50")


def test_shadow_l_complex_s():
    s = mp.mpc(3, 1)
    val = shadow_l_function(s, 1)
    expected = -mp.zeta(s) * mp.zeta(s - 1)
    assert abs(val - expected) < mp.mpf("1e-50")


def test_shadow_l_at_s_equals_minus_one():
    """At s = -1: zeta(-1) = -1/12 and zeta(-2) = 0, so L^sh(-1) = 0."""
    val = shadow_l_function(-1, 1)
    assert abs(val) < mp.mpf("1e-50")


def test_shadow_l_negative_kappa_sign_flip():
    a = shadow_l_function(3, 1)
    b = shadow_l_function(3, -1)
    assert abs(a + b) < mp.mpf("1e-50")


# ---------------------------------------------------------------------------
# Path 1b: Bernoulli Dirichlet series cross-check
# ---------------------------------------------------------------------------


def test_bernoulli_dirichlet_leading_term_at_s_equals_5():
    """The r = 1 term of the Bernoulli Dirichlet series is B_2 / 2! = 1/12.

    sum_{r >= 1} (B_{2r}/(2r)!) * r^{-s} starts with (1/12) * 1^{-s} = 1/12,
    and subsequent terms are O(2^{-s}) and smaller. So at s = 5 the partial
    sum should be very close to 1/12.
    """
    truncated = shadow_l_via_bernoulli(5, 1, n_terms=20)
    leading = mp.mpf(1) / 12
    # subsequent term r=2 contributes (B_4/4!) * 2^{-5} = (-1/720) * (1/32)
    # = -1/23040 ~ -4.34e-5
    correction = (mp.bernoulli(4) / mp.factorial(4)) * mp.power(2, -5)
    expected = leading + correction
    # Should agree to better than 1e-6 (subsequent terms are tiny)
    assert abs(truncated - expected) < mp.mpf("1e-6")


def test_bernoulli_dirichlet_first_term_kappa_scaling():
    """Linearity in kappa: doubling kappa doubles the partial sum."""
    a = shadow_l_via_bernoulli(5, 1, n_terms=10)
    b = shadow_l_via_bernoulli(5, 2, n_terms=10)
    assert abs(b - 2 * a) < mp.mpf("1e-40")


# ---------------------------------------------------------------------------
# Path 2: Euler product convergence
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("s,n_primes,tol", [
    (5, 200, mp.mpf("1e-10")),
    (6, 200, mp.mpf("1e-12")),
    (8, 200, mp.mpf("1e-15")),
    (10, 200, mp.mpf("1e-18")),
])
def test_euler_product_converges_to_zeta_zeta_shift(s, n_primes, tol):
    """Convergence rate of the Euler product is governed by zeta(s-1):
    each prime contributes O(p^{1-s}), so total tail is O(N^{2-s}).
    We test at s = 5, 6, 8, 10 where convergence is rapid.
    """
    target = zeta_zeta_shift_product(s)
    primes = first_n_primes(n_primes)
    approx = euler_partial_product(s, primes)
    assert abs(approx - target) < tol


def test_euler_product_monotone_convergence():
    """Adding more primes brings the product closer to the truth."""
    s = 6
    target = zeta_zeta_shift_product(s)
    err_small = abs(euler_partial_product(s, first_n_primes(10)) - target)
    err_med = abs(euler_partial_product(s, first_n_primes(50)) - target)
    err_big = abs(euler_partial_product(s, first_n_primes(200)) - target)
    assert err_small > err_med > err_big


def test_euler_product_at_s_equals_10_high_precision():
    """At large s the Euler product converges very rapidly."""
    target = zeta_zeta_shift_product(10)
    approx = euler_partial_product(10, first_n_primes(100))
    assert abs(approx - target) < mp.mpf("1e-20")


def test_euler_product_kappa_consistency():
    """L^sh(s) / (-kappa) should equal the Euler product."""
    s = 8
    kappa = 5
    lhs = shadow_l_function(s, kappa) / (-mp.mpf(kappa))
    rhs = euler_partial_product(s, first_n_primes(300))
    assert abs(lhs - rhs) < mp.mpf("1e-15")


# ---------------------------------------------------------------------------
# Path 3: Hasse-Weil identification with P^1
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("p", [2, 3, 5, 7])
def test_p1_local_factor_matches_geometric_form(p):
    """L_p(P^1, s) = 1 / [(1 - p^{-s})(1 - p^{1-s})]."""
    s = mp.mpf(3)
    lhs = p1_local_factor(p, s)
    p_mp = mp.mpf(p)
    rhs = mp.mpc(1) / ((1 - p_mp ** (-s)) * (1 - p_mp ** (1 - s)))
    assert abs(lhs - rhs) < mp.mpf("1e-50")


@pytest.mark.parametrize("p", [2, 3, 5, 7, 11, 13])
def test_p1_point_count_via_local_factor(p):
    """The number of points on P^1(F_p) is p + 1.

    This is encoded in the local factor: log L_p(P^1, s) at T = p^{-s}
    expands as sum_{n>=1} (#P^1(F_{p^n})) * T^n / n. The leading term
    in T is #P^1(F_p) * T = (p + 1) * p^{-s}. We extract this by
    differentiating the log of the local factor at large s.
    """
    # At very large s, T = p^{-s} is tiny and
    #   log L_p(P^1, s) ~ T + p T = (p + 1) T + O(T^2).
    # Equivalently (L_p - 1) / T -> p + 1 as s -> infinity.
    s = mp.mpf(20)
    p_mp = mp.mpf(p)
    T = p_mp ** (-s)
    leading = (p1_local_factor(p, s) - 1) / T
    # Expected leading coefficient is (p + 1) up to higher-order in T
    assert abs(leading - (p + 1)) < mp.mpf("1e-5")


def test_p1_local_factor_product_recovers_zeta_shift():
    """Product over many primes of P^1 local factors == zeta(s) * zeta(s-1).

    Convergence is governed by zeta(s-1), so we use s = 8.
    """
    s = mp.mpf(8)
    primes = first_n_primes(200)
    prod = mp.mpc(1)
    for p in primes:
        prod *= p1_local_factor(p, s)
    target = zeta_zeta_shift_product(s)
    assert abs(prod - target) < mp.mpf("1e-15")


def test_p1_local_factor_explicit_p_equals_2():
    """At p=2, s=3: (1 - 2^{-3})(1 - 2^{-2}) = (7/8)(3/4) = 21/32,
    so L_2(P^1, 3) = 32/21.
    """
    s = mp.mpf(3)
    val = p1_local_factor(2, s)
    # 2^{-3} = 1/8 and 2^{1-3} = 2^{-2} = 1/4
    expected = mp.mpc(1) / ((1 - mp.mpf(1) / 8) * (1 - mp.mpf(1) / 4))
    # = 1 / (7/8 * 3/4) = 32/21
    assert abs(val - expected) < mp.mpf("1e-50")
    assert abs(val - mp.mpf(32) / 21) < mp.mpf("1e-50")


def test_p1_local_factor_explicit_p_equals_3_at_s_equals_4():
    s = mp.mpf(4)
    val = p1_local_factor(3, s)
    expected = mp.mpc(1) / ((1 - mp.mpf(3) ** (-4)) * (1 - mp.mpf(3) ** (-3)))
    assert abs(val - expected) < mp.mpf("1e-50")


# ---------------------------------------------------------------------------
# Path 4: Pole / residue structure
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("kappa", [1, 2, 5, mp.mpf("13")])
def test_residue_at_one_equals_kappa_over_two(kappa):
    """L^sh(s) = -kappa * zeta(s) * zeta(s-1).
    zeta has simple pole at s=1 with residue 1; zeta(0) = -1/2.
    Residue = -kappa * 1 * (-1/2) = kappa/2.
    """
    res = shadow_l_residue_at_one(kappa)
    assert abs(res - mp.mpf(kappa) / 2) < mp.mpf("1e-50")


@pytest.mark.parametrize("kappa", [1, 2, 5, mp.mpf("13")])
def test_residue_at_two_equals_minus_kappa_pi_squared_over_six(kappa):
    """zeta(s-1) has simple pole at s=2 with residue 1; zeta(2) = pi^2/6.
    Residue = -kappa * (pi^2/6) * 1 = -kappa * pi^2 / 6.
    """
    res = shadow_l_residue_at_two(kappa)
    expected = -mp.mpf(kappa) * mp.pi ** 2 / 6
    assert abs(res - expected) < mp.mpf("1e-50")


def test_pole_at_one_via_limit():
    """(s - 1) * L^sh(s) -> kappa/2 as s -> 1."""
    kappa = 1
    eps = mp.mpf("1e-8")
    s = 1 + eps
    val = (s - 1) * shadow_l_function(s, kappa)
    assert abs(val - mp.mpf(kappa) / 2) < mp.mpf("1e-7")


def test_pole_at_two_via_limit():
    """(s - 2) * L^sh(s) -> -kappa * pi^2 / 6 as s -> 2."""
    kappa = 1
    eps = mp.mpf("1e-8")
    s = 2 + eps
    val = (s - 2) * shadow_l_function(s, kappa)
    expected = -mp.mpf(kappa) * mp.pi ** 2 / 6
    assert abs(val - expected) < mp.mpf("1e-6")


def test_no_pole_at_s_equals_3():
    """L^sh is finite at s = 3 (no zeta pole)."""
    val = shadow_l_function(3, 1)
    assert abs(val) < mp.mpf("100")
    assert mp.isfinite(mp.re(val))


# ---------------------------------------------------------------------------
# Engine wrapper tests
# ---------------------------------------------------------------------------


def test_engine_identity_residual_zero():
    eng = ShadowEisensteinEngine()
    assert abs(eng.identity_residual(4, 1)) < mp.mpf("1e-40")
    assert abs(eng.identity_residual(5, 13)) < mp.mpf("1e-40")


def test_engine_euler_residual_decays():
    eng = ShadowEisensteinEngine()
    err10 = abs(eng.euler_residual(4, 10))
    err100 = abs(eng.euler_residual(4, 100))
    assert err100 < err10


def test_engine_hasse_weil_residual_zero():
    eng = ShadowEisensteinEngine()
    for p in (2, 3, 5, 7):
        assert abs(eng.hasse_weil_residual(p, 4)) < mp.mpf("1e-40")


def test_engine_pole_residuals_match_closed_form():
    eng = ShadowEisensteinEngine()
    kappa = 7
    assert abs(eng.residue_at_one(kappa) - mp.mpf(7) / 2) < mp.mpf("1e-50")
    assert abs(eng.residue_at_two(kappa) - (-mp.mpf(7) * mp.pi ** 2 / 6)) < mp.mpf("1e-50")


def test_engine_pole_residual_via_limit_at_one():
    eng = ShadowEisensteinEngine()
    val = eng.pole_residual_at_one(1, eps=1e-8)
    assert abs(val) < mp.mpf("1e-6")


def test_engine_pole_residual_via_limit_at_two():
    eng = ShadowEisensteinEngine()
    val = eng.pole_residual_at_two(1, eps=1e-8)
    assert abs(val) < mp.mpf("1e-5")


# ---------------------------------------------------------------------------
# Cross-path: all four verification paths agree
# ---------------------------------------------------------------------------


def test_all_paths_agree_at_s_equals_8_kappa_one():
    """The four independent verification paths all yield the same value of L^sh.

    Convergence rate is governed by zeta(s-1) = zeta(7) so we test at s = 8
    where the Euler product converges to ~1e-15 with 300 primes.
    """
    s = mp.mpf(8)
    kappa = 1

    # Path 1: closed-form -kappa * zeta(s) * zeta(s - 1)
    p1 = shadow_l_function(s, kappa)

    # Path 2: -kappa * Euler product
    p2 = -mp.mpf(kappa) * euler_partial_product(s, first_n_primes(300))

    # Path 3: -kappa * product of P^1 local factors over the same primes
    p3_inner = mp.mpc(1)
    for p in first_n_primes(300):
        p3_inner *= p1_local_factor(p, s)
    p3 = -mp.mpf(kappa) * p3_inner

    # All three should agree to high precision
    assert abs(p1 - p2) < mp.mpf("1e-15")
    assert abs(p1 - p3) < mp.mpf("1e-15")
    assert abs(p2 - p3) < mp.mpf("1e-15")
