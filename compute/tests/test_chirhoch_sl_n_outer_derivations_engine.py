r"""Tests for chirhoch_sl_n_outer_derivations_engine.py.

Verifies the affine sl_N FR4 surface

    dim ChirHoch^1(V_k(sl_N)) = dim(sl_N) = N^2 - 1

for N = 2, ..., 8 at generic level.
"""

from compute.lib.chirhoch_sl_n_outer_derivations_engine import (
    compute_chirhoch1_affine_sl_n,
    verify_fr4_conjecture,
)


def test_chirhoch1_affine_sl2():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 3
    assert compute_chirhoch1_affine_sl_n(2) == expected
    assert verify_fr4_conjecture()[2] == (expected, expected, True)


def test_chirhoch1_affine_sl3():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 8
    assert compute_chirhoch1_affine_sl_n(3) == expected
    assert verify_fr4_conjecture()[3] == (expected, expected, True)


def test_chirhoch1_affine_sl4():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 15
    assert compute_chirhoch1_affine_sl_n(4) == expected
    assert verify_fr4_conjecture()[4] == (expected, expected, True)


def test_chirhoch1_affine_sl5():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 24
    assert compute_chirhoch1_affine_sl_n(5) == expected
    assert verify_fr4_conjecture()[5] == (expected, expected, True)


def test_chirhoch1_affine_sl6():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 35
    assert compute_chirhoch1_affine_sl_n(6) == expected
    assert verify_fr4_conjecture()[6] == (expected, expected, True)


def test_chirhoch1_affine_sl7():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 48
    assert compute_chirhoch1_affine_sl_n(7) == expected
    assert verify_fr4_conjecture()[7] == (expected, expected, True)


def test_chirhoch1_affine_sl8():
    # VERIFIED [DC] dim(sl_N)=N^2-1 [LT] Frenkel-Ben-Zvi: HH^1(V_k(g))=g as g-module
    expected = 63
    assert compute_chirhoch1_affine_sl_n(8) == expected
    assert verify_fr4_conjecture()[8] == (expected, expected, True)
