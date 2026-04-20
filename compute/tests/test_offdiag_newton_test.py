"""Tests for compute/lib/offdiag_newton_test.py -- Satake Newton identities.

Non-trivial identities tested:
  (i)   Newton recursion p_r = e1*p_{r-1} - e2*p_{r-2} matches direct alpha^r + beta^r
        for Satake parameters at Ramanujan tau values.
  (ii)  Genus-1 MC equation is tautologous for the 2-variable Satake case:
        no new constraints beyond (e1, e2).
  (iii) Divisor count and sigma_k sanity.
"""

from __future__ import annotations

import math

from compute.lib.offdiag_newton_test import (
    divisor_count,
    genus1_mc_is_newton,
    partitions,
    sigma_k,
)


def test_smoke_sigma_k_small():
    """Smoke: sigma_3(1)=1, sigma_3(2)=1+8=9, sigma_3(3)=1+27=28."""
    assert sigma_k(1, 3) == 1
    assert sigma_k(2, 3) == 9
    assert sigma_k(3, 3) == 28


def test_sigma_k_at_prime():
    """For prime p: sigma_k(p) = 1 + p^k."""
    for p in [2, 3, 5, 7, 11, 13]:
        for k in [1, 2, 3, 5]:
            assert sigma_k(p, k) == 1 + p ** k


def test_divisor_count_small():
    """tau(12) = 6 (divisors 1,2,3,4,6,12). tau(1) = 1."""
    assert divisor_count(1) == 1
    assert divisor_count(12) == 6
    assert divisor_count(7) == 2  # prime


def test_newton_recursion_at_ramanujan_tau_p2():
    """Satake parameters at p=2 (tau(2) = -24): alpha + beta = -24, alpha*beta = 2^11.
    Newton p_r = -24*p_{r-1} - 2^11*p_{r-2} matches direct computation."""
    e1 = -24.0
    e2 = 2 ** 11  # 2048
    result = genus1_mc_is_newton(e1, e2, r_max=10)
    assert result['newton_complete'] is True
    assert result['max_relative_residual'] < 1e-10


def test_newton_recursion_at_ramanujan_tau_p3():
    """Ramanujan tau(3) = 252, e2 = 3^11 = 177147."""
    e1 = 252.0
    e2 = 3 ** 11
    result = genus1_mc_is_newton(e1, e2, r_max=12)
    assert result['newton_complete'] is True


def test_newton_recursion_at_real_roots():
    """e1=5, e2=6: alpha=3, beta=2, p_r = 3^r + 2^r."""
    e1, e2 = 5.0, 6.0
    result = genus1_mc_is_newton(e1, e2, r_max=8)
    # p_0 = 2, p_1 = 5, p_2 = 13 (9+4), p_3 = 35 (27+8), p_4 = 97 (81+16)
    p = result['p_newton']
    assert abs(p[0] - 5) < 1e-9  # p_1
    assert abs(p[1] - 13) < 1e-9  # p_2
    assert abs(p[2] - 35) < 1e-9  # p_3
    assert abs(p[3] - 97) < 1e-9  # p_4


def test_partitions_small():
    """p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7 (integer partition counts)."""
    assert partitions(1) == 1
    assert partitions(2) == 2
    assert partitions(3) == 3
    assert partitions(4) == 5
    assert partitions(5) == 7
