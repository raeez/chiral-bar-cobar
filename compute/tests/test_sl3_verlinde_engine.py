"""Tests for compute/lib/sl3_verlinde_engine.

sl_3 Verlinde formula at level k, genus g: dimensions of conformal blocks,
quantum dimensions, and S_{00}^2 identity.

Three verification paths:
  (a) Genus-0 unitarity: trivial rep has quantum dim 1.
  (b) Genus-1 count: dim V_{1,0}(g=1) = number of integrable reps at level k.
  (c) Number of integrable weights at level k: (k+1)(k+2)/2 for sl_3.
"""

from fractions import Fraction

import pytest

from compute.lib.sl3_verlinde_engine import (
    sl3_integrable_weights,
    sl3_num_integrable_reps,
    sl3_verlinde_dimension,
    verify_genus0_unitarity,
    verify_genus1_count,
)


def test_smoke_import():
    """Imports and one numeric Verlinde call."""
    d = sl3_verlinde_dimension(genus=0, level=1)
    assert isinstance(d, int)


def test_num_integrable_reps_formula():
    """Number of integrable sl_3 reps at level k is (k+1)(k+2)/2."""
    for k in range(1, 8):
        n = sl3_num_integrable_reps(k)
        assert n == (k + 1) * (k + 2) // 2, \
            f"sl_3 integrable count at level {k}: expected {(k+1)*(k+2)//2}, got {n}"


def test_integrable_weights_count_matches():
    """Listing integrable weights matches the count."""
    for k in range(1, 6):
        weights = sl3_integrable_weights(k)
        assert len(weights) == sl3_num_integrable_reps(k)


def test_genus0_unitarity():
    """Verlinde at genus 0 with trivial rep insertions gives dim = 1."""
    for k in (1, 2, 3, 4):
        assert verify_genus0_unitarity(k)


def test_genus1_count():
    """dim V_g=1(k) = number of integrable reps."""
    for k in (1, 2, 3, 4):
        assert verify_genus1_count(k)


def test_verlinde_genus1_level1():
    """sl_3 at level 1: 3 integrable reps, so g=1 Verlinde dim = 3."""
    assert sl3_verlinde_dimension(genus=1, level=1) == 3


def test_verlinde_genus1_level2():
    """sl_3 at level 2: (2+1)(2+2)/2 = 6 integrable reps."""
    assert sl3_num_integrable_reps(2) == 6
    assert sl3_verlinde_dimension(genus=1, level=2) == 6
