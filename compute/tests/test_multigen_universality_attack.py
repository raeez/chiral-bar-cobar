"""Tests for compute/lib/multigen_universality_attack.py -- W_3 shadow data.

Non-trivial identities tested:
  (i)   W_3 kappas: kappa_T = c/2, kappa_W = c/3, total = 5c/6.
  (ii)  Cubic shadow: coefficient of x_T*x_W^2 is 3 (from W_3 x W_3 OPE structure).
  (iii) Virasoro shadow S_4 = 10/[c(5c+22)] (Zamolodchikov Lambda contact).
  (iv)  Quartic shadow block structure: Q_TT, Q_TW, Q_WW scaling with (5c+22)^k.
"""

from __future__ import annotations

from fractions import Fraction

from compute.lib.multigen_universality_attack import (
    lambda_fp,
    virasoro_shadow_data,
    w3_cubic_shadows,
    w3_kappas,
    w3_quartic_shadows,
)


def test_smoke_w3_kappas_decomposition():
    """Smoke: W_3 kappas split as T-channel c/2 plus W-channel c/3 = 5c/6."""
    c = Fraction(3)
    k = w3_kappas(c)
    assert k['T'] == Fraction(3, 2)
    assert k['W'] == Fraction(1, 1)
    assert k['total'] == Fraction(5, 2)


def test_w3_kappa_total_equals_T_plus_W():
    """For any c: kappa_total = kappa_T + kappa_W = 5c/6."""
    for c in [Fraction(1), Fraction(2), Fraction(-22, 5), Fraction(7)]:
        k = w3_kappas(c)
        assert k['T'] + k['W'] == k['total']
        assert k['total'] == 5 * c / 6


def test_w3_cubic_shadow_z2_symmetry_vanishing():
    """Z_2 parity W -> -W forces odd-W-count shadows to vanish:
    S_3(TTW) = 0 and S_3(WWW) = 0."""
    c = Fraction(1)
    s3 = w3_cubic_shadows(c)
    assert s3['TTW'] == Fraction(0)
    assert s3['WWW'] == Fraction(0)


def test_w3_cubic_shadow_values():
    """Non-vanishing cubic shadows: TTT coefficient = 2, TWW coefficient = 3."""
    s3 = w3_cubic_shadows(Fraction(1))
    assert s3['TTT'] == Fraction(2)
    assert s3['TWW'] == Fraction(3)


def test_w3_quartic_Q_TT_is_Zamolodchikov():
    """Q_TT = 10 / [c(5c+22)] -- Virasoro sector quartic contact."""
    c = Fraction(3)
    s4 = w3_quartic_shadows(c)
    expected = Fraction(10, 3 * (5 * 3 + 22))
    assert s4['TTTT'] == expected


def test_w3_quartic_Q_TW_scales_by_5c_plus_22():
    """Q_TW / Q_TT = 16/(5c+22) (one extra factor of (5c+22))."""
    c = Fraction(7)
    s4 = w3_quartic_shadows(c)
    ratio = s4['TTWW'] / s4['TTTT']
    expected_ratio = Fraction(16, 5 * 7 + 22)
    assert ratio == expected_ratio


def test_w3_quartic_Q_WW_scales_by_5c_plus_22_squared():
    """Q_WW / Q_TT = 256/(5c+22)^2 (two extra factors)."""
    c = Fraction(5)
    s4 = w3_quartic_shadows(c)
    ratio = s4['WWWW'] / s4['TTTT']
    expected_ratio = Fraction(256, (5 * 5 + 22) ** 2)
    assert ratio == expected_ratio


def test_virasoro_shadow_data_at_unit_c():
    """Virasoro at c=1: kappa=1/2, alpha=2 (c-independent), S_4 = 10/27."""
    d = virasoro_shadow_data(Fraction(1))
    assert d['kappa'] == Fraction(1, 2)
    assert d['alpha'] == Fraction(2)
    assert d['S4'] == Fraction(10, 27)


def test_lambda_fp_g1_canonical():
    """Faber-Pandharipande g=1: lambda_1^FP = 1/24."""
    assert lambda_fp(1) == Fraction(1, 24)
