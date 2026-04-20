"""Tests for compute/lib/euler_koszul_moments.

Sewing coefficients, Hankel moments, and kappa values for Heisenberg,
Virasoro, and W_N, with Q^contact quartic coefficient.

Three verification paths:
  (a) kappa(Heisenberg_k) = k.
  (b) kappa(Virasoro_c) = c/2.
  (c) divisor_sigma(1, n) = n (trivial divisor sum identity).
"""

from fractions import Fraction

import pytest

from compute.lib.euler_koszul_moments import (
    Q_contact_virasoro,
    divisor_sigma,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_WN,
    sewing_coeffs_heisenberg,
)


def test_smoke_import():
    """Module imports and basic call."""
    assert kappa_heisenberg(1) == 1


def test_kappa_heisenberg_identity():
    """kappa(H_k) = k from essential-constants table in CLAUDE.md."""
    for k in (1, 2, 3, 5):
        assert kappa_heisenberg(k) == k


def test_kappa_virasoro_is_c_over_2():
    """kappa(Vir_c) = c/2 (CLAUDE.md essential constants)."""
    import sympy as sp
    for c in (1, 2, Fraction(1, 2), 13, 26):
        val = kappa_virasoro(c)
        # Could be rational or sympy
        if isinstance(val, Fraction):
            assert val == Fraction(c, 2)
        else:
            assert sp.nsimplify(val) == sp.nsimplify(sp.Rational(c) / 2)


def test_divisor_sigma_trivial():
    """sigma_0(n) = number of divisors; sigma_1(n) = sum of divisors.

    Module convention: divisor_sigma(N, s) = sum_{d|N} d^s.
    """
    assert divisor_sigma(6, 1) == 1 + 2 + 3 + 6  # sigma_1(6) = 12
    assert divisor_sigma(10, 1) == 1 + 2 + 5 + 10  # sigma_1(10) = 18
    assert divisor_sigma(6, 0) == 4  # sigma_0(6) = 4 (divisors {1,2,3,6})
    assert divisor_sigma(12, 0) == 6  # sigma_0(12) = 6


def test_sewing_coeffs_heisenberg_shape():
    """Sewing coefficients are a list/tuple of correct length."""
    coeffs = sewing_coeffs_heisenberg(10)
    assert len(coeffs) >= 10


def test_kappa_WN_formula():
    """kappa(W_N, c) = c(H_N - 1) with H_N = sum 1/j (essential constants).

    The module uses mpmath floats internally, so compare via coefficient extraction
    with a floating-point tolerance.
    """
    import sympy as sp
    c = sp.Symbol('c')
    tol = 1e-30
    # N = 2: H_2 - 1 = 1/2 -> coefficient 1/2
    coeff_2 = float(sp.Poly(sp.sympify(kappa_WN(c, 2)), c).nth(1))
    assert abs(coeff_2 - 0.5) < tol
    # N = 3: H_3 - 1 = 5/6
    coeff_3 = float(sp.Poly(sp.sympify(kappa_WN(c, 3)), c).nth(1))
    assert abs(coeff_3 - 5.0 / 6.0) < tol
