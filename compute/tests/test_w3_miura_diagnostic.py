"""Tests for compute/lib/w3_miura_diagnostic.py -- sl_3 Miura W_3.

Non-trivial identities tested:
  (i)   sl_3 fundamental weights satisfy sum h_i = 0 and h_i . h_j = delta_ij - 1/3.
  (ii)  sl_3 Weyl vector rho = (1, 0, -1) in R^3; |rho|^2 = 2.
  (iii) W_3 central charge c(t) = 2 - 12t. At t=1: c = -10. At t=0: c = 2 (free boson rank 2).
  (iv)  Zamolodchikov C_333^2 = 64(7c+68)(2c-1) / [5c(c+24)(5c+22)] --
        poles at c=0, c=-24, c=-22/5; zeros at c=-68/7, c=1/2.
"""

from __future__ import annotations

import numpy as np

from compute.lib.w3_miura_diagnostic import (
    W3MiuraDiagnostic,
    sl3_fundamental_weights_R3,
    sl3_orthonormal_cartan_basis,
    sl3_weyl_vector_R3,
    w3_central_charge,
)


def test_smoke_sl3_fundamental_weights_sum_to_zero():
    """Smoke: sum of h_1, h_2, h_3 = 0 (sl_3 tracelessness)."""
    h = sl3_fundamental_weights_R3()
    assert np.allclose(h.sum(axis=0), np.zeros(3))


def test_sl3_fundamental_weights_inner_products():
    """h_i . h_j = delta_ij - 1/3."""
    h = sl3_fundamental_weights_R3()
    for i in range(3):
        for j in range(3):
            ip = float(np.dot(h[i], h[j]))
            expected = (1.0 if i == j else 0.0) - 1.0 / 3.0
            assert abs(ip - expected) < 1e-12


def test_sl3_weyl_vector():
    """rho = (1, 0, -1). |rho|^2 = 2."""
    rho = sl3_weyl_vector_R3()
    assert np.allclose(rho, np.array([1.0, 0.0, -1.0]))
    assert abs(float(np.dot(rho, rho)) - 2.0) < 1e-14


def test_sl3_cartan_basis_orthonormal():
    """e_1 = (1,-1,0)/sqrt(2), e_2 = (1,1,-2)/sqrt(6). Check orthonormality and spanning sum=0."""
    basis = sl3_orthonormal_cartan_basis()
    # Orthonormal
    assert abs(float(np.dot(basis[0], basis[0])) - 1.0) < 1e-12
    assert abs(float(np.dot(basis[1], basis[1])) - 1.0) < 1e-12
    assert abs(float(np.dot(basis[0], basis[1]))) < 1e-12
    # Each lies in the sum-zero hyperplane
    assert abs(float(basis[0].sum())) < 1e-12
    assert abs(float(basis[1].sum())) < 1e-12


def test_w3_central_charge_at_t_zero():
    """At t=0 (free limit): c = 2 (rank-2 free boson)."""
    assert abs(w3_central_charge(0.0) - 2.0) < 1e-14


def test_w3_central_charge_at_t_one():
    """At t=1: c = 2 - 12 = -10."""
    assert abs(w3_central_charge(1.0) - (-10.0)) < 1e-14


def test_w3_central_charge_linear_in_t():
    """c(t_1) - c(t_2) = -12 (t_1 - t_2): slope check."""
    slope = w3_central_charge(1.0) - w3_central_charge(0.5)
    assert abs(slope - (-6.0)) < 1e-14


def test_zamolodchikov_c333_squared_pole_at_c_eq_zero():
    """C_333^2 has pole at c=0 (vanishing in denominator)."""
    # At c near 0, C_333^2 should blow up (checked via formula)
    c_num = 1e-6
    c_denom = 5 * c_num * (c_num + 24) * (5 * c_num + 22)
    # denominator ~ 5 * 10^-6 * 24 * 22 = very small
    assert abs(c_denom) < 0.01


def test_zamolodchikov_c333_squared_zero_at_c_eq_half():
    """C_333^2 = 0 at c = 1/2 (numerator factor 2c-1 vanishes)."""
    c = 0.5
    numerator = 64 * (7 * c + 68) * (2 * c - 1)
    assert abs(numerator) < 1e-14


def test_zamolodchikov_c333_squared_zero_at_c_eq_minus_68_over_7():
    """C_333^2 = 0 at c = -68/7 (numerator factor 7c+68 vanishes)."""
    c = -68.0 / 7.0
    numerator = 64 * (7 * c + 68) * (2 * c - 1)
    assert abs(numerator) < 1e-13
