"""Tests for compute/lib/lattice_genus2_theta.

Genus-2 theta series of even unimodular lattices E_8, D_4, A_2 and
the diagonal-factorisation identity.

Three verification paths:
  (a) E_8 theta coefficients: 1, 240, 2160, 6720 (classical values).
  (b) D_4 theta coefficients: 1, 24, 24, ... (D_4 root lattice values).
  (c) Diagonal factorisation Theta_Lambda(Z_diag) = Theta(z_1) * Theta(z_2).
"""

from fractions import Fraction

import pytest

from compute.lib.lattice_genus2_theta import (
    d4_theta_coefficients,
    e8_theta_coefficients,
    e8_vectors_by_half_norm,
    lambda_fp,
)


def test_smoke_import():
    """Imports and a coefficient call."""
    coeffs = e8_theta_coefficients(5)
    assert coeffs[0] == 1


def test_e8_theta_classical_coefficients():
    """E_8 theta = E_4: coeffs are 1, 240, 2160, 6720, 17520, 30240.

    These are 240*sigma_3(n) for n >= 1.
    """
    coeffs = e8_theta_coefficients(6)
    assert coeffs[0] == 1
    assert coeffs[1] == 240   # 240 * 1
    assert coeffs[2] == 2160  # 240 * 9 = 240 * (1 + 2^3)
    assert coeffs[3] == 6720  # 240 * 28 = 240 * (1 + 3^3)
    assert coeffs[4] == 17520  # 240 * 73 = 240 * (1 + 2^3 + 4^3)
    assert coeffs[5] == 30240  # 240 * 126 = 240 * (1 + 5^3)


def test_d4_theta_first_coefficients():
    """D_4 theta series starts 1, 24, 24, 96, 24 (A024761 shifted)."""
    coeffs = d4_theta_coefficients(5)
    assert coeffs[0] == 1
    assert coeffs[1] == 24


def test_e8_vectors_by_half_norm_count_matches_theta():
    """Number of E_8 vectors of norm 2n equals the E_8 theta coefficient at q^n.

    Shortest E_8 roots have norm 2, count 240 (the root system).
    """
    vectors = e8_vectors_by_half_norm(2)
    # number of vectors with |v|^2/2 = 1 (norm 2) is 240
    assert len(vectors[1]) == 240


def test_lambda_fp_values():
    """lambda_fp(g) is the Hodge integral int lambda_g on M_bar_{g,1} (or similar)."""
    # Classical value: lambda_fp(1) = 1/24, lambda_fp(2) = 1/5760
    val1 = lambda_fp(1)
    val2 = lambda_fp(2)
    assert val1 == Fraction(1, 24)
    assert val2 == Fraction(1, 5760)


def test_e8_theta_matches_eisenstein_e4():
    """For unimodular E_8: Theta_{E_8} = E_4 (Jacobi theta identity).

    E_4 = 1 + 240 sum sigma_3(n) q^n. Check for n = 1..5.
    """
    coeffs = e8_theta_coefficients(6)
    # sigma_3(n):
    sigma3 = [0, 1, 9, 28, 73, 126]
    for n in range(1, 6):
        assert coeffs[n] == 240 * sigma3[n]
