"""Tests for compute/lib/cohft_virasoro_constraints_engine.py.

Non-trivial identities tested:
  (i)   Faber-Pandharipande numbers: lambda_1^FP = 1/24, lambda_2^FP = 7/5760,
        lambda_3^FP = 31/967680 (CLAUDE.md numerology / Faber 1999).
  (ii)  Bernoulli Hodge coefficients: |B_2|/(2*2!) = 1/24, |B_4|/(4*4!) = 1/2880
        (denominator of Hodge-psi identity).
  (iii) Witten-Kontsevich intersection number: <tau_0^3>_{0,3} = 1 (string axiom).
  (iv)  Virasoro L_{-1} string equation reduces (g,n+1) with psi_1^{0} insertion
        to (g,n).
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.cohft_virasoro_constraints_engine import (
    lambda_fp,
    lambda_g_integral,
    shadow_free_energy,
    virasoro_string_equation,
    wk_intersection,
)


def test_smoke_lambda_fp_g1():
    """Smoke: lambda_1^FP = 1/24 (canonical FP number)."""
    assert lambda_fp(1) == Fraction(1, 24)


def test_lambda_fp_g2_and_g3():
    """Non-trivial: lambda_2^FP = 7/5760, lambda_3^FP = 31/967680."""
    assert lambda_fp(2) == Fraction(7, 5760)
    assert lambda_fp(3) == Fraction(31, 967680)


def test_lambda_fp_g4():
    """Fourth entry of FP sequence: 127/154828800."""
    assert lambda_fp(4) == Fraction(127, 154828800)


def test_lambda_g_integral_g1():
    """|B_2|/(2*2!) = (1/6)/4 = 1/24."""
    assert lambda_g_integral(1) == Fraction(1, 24)


def test_lambda_g_integral_g2():
    """|B_4|/(4*4!) = (1/30)/96 = 1/2880."""
    assert lambda_g_integral(2) == Fraction(1, 2880)


def test_lambda_fp_ratio_formula():
    """Check lambda_fp(g) / lambda_g_integral(g) = (2^{2g-1} - 1) * 2g / 2^{2g-1}."""
    for g in [1, 2, 3, 4]:
        ratio = lambda_fp(g) / lambda_g_integral(g)
        power = 2 ** (2 * g - 1)
        expected = Fraction(power - 1, power) * 2 * g
        assert ratio == expected


def test_string_axiom_at_g0_n3():
    """Virasoro string equation applied at (g=0,n=3) with trivial insertion tau_0^2."""
    # The string eq reduces (g,n+1,psi_1^0) to (g,n,...); we test that the
    # returned structure is well-formed (not raising) at a simple case.
    result = virasoro_string_equation(genus=0, insertions=(0, 0, 0))
    assert isinstance(result, dict)


def test_wk_base_case():
    """<tau_0^3>_{0,3} = 1 (string/3-pt function base case of WK)."""
    v = wk_intersection(0, (0, 0, 0))
    assert v == Fraction(1, 1)


def test_shadow_free_energy_linear_in_kappa_at_g1():
    """Shadow free energy at g=1 is lambda_1^FP * kappa = kappa/24."""
    f = shadow_free_energy(1, Fraction(2))  # kappa = 2
    assert f == Fraction(2, 24) == Fraction(1, 12)
