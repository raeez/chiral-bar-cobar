"""Tests for compute/lib/wp_triplet_shadow_engine.py -- W(p,1) triplet shadow.

Non-trivial identities tested:
  (i)   c_{p,1} = 1 - 6(p-1)^2/p (Kausch 1991; triplet central charge).
        At p=2: c = 1 - 6 = -5 wait actually 1-6(1)^2/2 = 1-3 = -2. CORRECT.
        At p=3: c = 1 - 24/3 = 1-8 = -7.
  (ii)  kappa_triplet = c/2 (Virasoro-sector extraction, AP48-compliant).
  (iii) Triplet multiplicity: W^a at weight 2p-1 with sl_2 multiplicity 3.
"""

from __future__ import annotations

from sympy import Rational, Symbol

import pytest

from compute.lib.wp_triplet_shadow_engine import (
    central_charge_triplet,
    generator_weights,
    kappa_triplet_virasoro,
    norm_T,
    norm_W_triplet,
    wwLambda_coupling,
)


def test_smoke_central_charge_p2():
    """Smoke: c_{p=2,1} = 1 - 6*1/2 = -2 (Kausch triplet)."""
    assert central_charge_triplet(2) == Rational(-2)


def test_central_charge_p3():
    """c_{p=3,1} = 1 - 24/3 = -7."""
    assert central_charge_triplet(3) == Rational(-7)


def test_central_charge_p5():
    """c_{p=5,1} = 1 - 6*16/5 = (5-96)/5 = -91/5."""
    assert central_charge_triplet(5) == Rational(-91, 5)


def test_central_charge_rejects_p_below_2():
    """p=1 is unphysical (would give c=1, free boson; triplet theory defined for p>=2)."""
    with pytest.raises(ValueError):
        central_charge_triplet(1)


def test_kappa_triplet_is_c_over_2():
    """kappa = c/2 via Virasoro sub-VOA extraction."""
    for p in [2, 3, 5, 7]:
        c = central_charge_triplet(p)
        assert kappa_triplet_virasoro(p) == c / 2


def test_kappa_triplet_p2_equals_minus_one():
    """At p=2: kappa = -2/2 = -1."""
    assert kappa_triplet_virasoro(2) == Rational(-1)


def test_generator_weights_T_W_structure():
    """T at weight 2 (mult 1); W at weight 2p-1 (mult 3 = sl_2 triplet)."""
    for p in [2, 3, 4, 5]:
        gw = generator_weights(p)
        assert gw['T'] == (2, 1)
        assert gw['W_triplet'] == (2 * p - 1, 3)


def test_norm_T_is_c_over_2():
    """<T|T> = c/2 (BPZ normalization, symbolic)."""
    c = Symbol('c')
    n = norm_T()
    assert n == c / 2


def test_norm_W_triplet_is_inverse_h_W():
    """W^a two-point norm per sl_2-singlet line = 1/h_W = 1/(2p-1)."""
    for p in [2, 3, 5]:
        n = norm_W_triplet(p)
        assert n == Rational(1, 2 * p - 1)


def test_wwLambda_coupling_p2_matches_kausch():
    """At p=2: alpha_W = 16/(5c+22) [Kausch 1991]. At c=-2: 5c+22=12."""
    c = Symbol('c')
    coupling = wwLambda_coupling(2)
    expected = Rational(16) / (5 * c + 22)
    assert coupling == expected
    # Specialize to c=-2: coupling = 16/12 = 4/3
    val = coupling.subs(c, Rational(-2))
    assert val == Rational(4, 3)
