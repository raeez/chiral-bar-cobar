r"""Tests for k3_yangian_wave18_pentagon_coboundary_hbar11_12.

Module claims:
    (1) Padovan dimension d_n (Brown 2011 Ann. Math. 175 Thm 1.1):
        d_0 = 1, d_1 = 0, d_2 = d_3 = d_4 = d_5 = 1, and
        d_n = d_{n-2} + d_{n-3} for n >= 3.  Thus
        d_6, d_7, ..., d_12 = 2, 2, 3, 4, 5, 7, 9.
    (2) Depth-4 irreducible motivic MZV first appears at weight 12
        (Brown 2011 Thm 1.2): zeta(3, 3, 3, 3).  Below weight 12
        every Deligne-basis entry has depth <= 3.
    (3) K3 Borcherds leg Phi_10^{n/2} / eta^{12n} has raw modular
        weight -n (wt(Phi_10) = 10, wt(eta) = 1/2).
    (4) Fake-Monster BKM denominator Phi_12 lives on II_{25,1}
        (signature (25,1)), NOT on Lambda^{2,1}_II (signature (2,1)):
        the two lattices cannot embed compatibly, so the Fake-Monster
        leg is never a K3-BKM leg (Borcherds 1998 Thm 13.1 vs K3 setup).
    (5) Borcherds leg lives on Sp_4(Z) double cover iff n is odd
        (Gritsenko-Nikulin 1998 Sec 4).
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_wave18_pentagon_coboundary_hbar11_12 import (
    borcherds_leg_in_tower_weight,
    borcherds_leg_is_fake_monster,
    borcherds_leg_lives_on_double_cover,
    borcherds_leg_raw_weight,
    depth_4_first_appears_at_weight,
    mzv_basis_weight_11,
    mzv_basis_weight_12,
    padovan_dim,
    phi_11_symbolic,
    phi_12_symbolic,
)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def test_smoke_phi_11_and_phi_12_decompose():
    d11 = phi_11_symbolic()
    d12 = phi_12_symbolic()
    assert d11["weight"] == 11
    assert d12["weight"] == 12


# ---------------------------------------------------------------------------
# (Identity) Brown 2011 Thm 1.1: Padovan recurrence, tabulated values.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 2),
    (7, 2),
    (8, 3),
    (9, 4),
    (10, 5),
    (11, 7),
    (12, 9),
])
def test_padovan_canonical_brown_2011(n, expected):
    assert padovan_dim(n) == expected, (
        f"d_{n} = {padovan_dim(n)} disagrees with Brown 2011 Thm 1.1 "
        f"tabulated value {expected}"
    )


def test_padovan_recurrence_d_n_equals_d_nm2_plus_d_nm3():
    for n in range(6, 20):
        assert padovan_dim(n) == padovan_dim(n - 2) + padovan_dim(n - 3)


# ---------------------------------------------------------------------------
# (Identity) Brown 2011 Thm 1.2: depth-4 first appears at weight 12.
# ---------------------------------------------------------------------------

def test_depth_4_first_appearance_is_weight_12():
    assert depth_4_first_appears_at_weight() == 12
    # Weight-11 basis: 7 entries, max depth = 3 (only zeta(3,3,5) is depth 3)
    b11 = mzv_basis_weight_11()
    assert len(b11) == 7
    d11 = phi_11_symbolic()
    assert d11["depth_max_in_basis"] == 3
    # Weight-12 basis: 9 entries, max depth = 4 (ninth entry zeta(3,3,3,3))
    b12 = mzv_basis_weight_12()
    assert len(b12) == 9
    assert "zeta(3, 3, 3, 3)" in b12
    d12 = phi_12_symbolic()
    assert d12["depth_max_in_basis"] == 4


# ---------------------------------------------------------------------------
# (Identity) Borcherds raw modular weight = -n
#   wt(Phi_10^{n/2} / eta^{12n}) = 10 * (n/2) - (1/2)(12n) = 5n - 6n = -n.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [1, 2, 3, 6, 11, 12])
def test_borcherds_raw_modular_weight_equals_minus_n(n):
    assert borcherds_leg_raw_weight(n) == Fraction(-n, 1)


def test_borcherds_in_tower_weight_equals_5n():
    for n in (0, 1, 5, 11, 12):
        assert borcherds_leg_in_tower_weight(n) == 5 * n


# ---------------------------------------------------------------------------
# (Symmetry) Double-cover lives iff n is odd (half-integer exponent n/2).
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n,odd", [
    (1, True), (2, False), (3, True), (4, False),
    (11, True), (12, False),
])
def test_double_cover_iff_n_odd(n, odd):
    assert borcherds_leg_lives_on_double_cover(n) is odd


# ---------------------------------------------------------------------------
# (Lattice signature) Fake-Monster is never a K3-BKM leg.
# Borcherds 1998 Thm 13.1: Phi_12 on II_{25,1} (signature (25,1)).
# K3-BKM Cartan is Lambda^{2,1}_II (signature (2,1)).  No embedding.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n", [2, 6, 10, 11, 12, 100])
def test_fake_monster_never_a_k3_bkm_leg(n):
    assert borcherds_leg_is_fake_monster(n) is False
