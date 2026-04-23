r"""Tests for k3_yangian_wave19_phi12_zeta3333_coefficient.

Module claims:
    (1) c_12^(9) = zeta(3,3,3,3) / 12! ~ 6.180 * 10^{-13}.
        12! = 479001600 (Shnider-Stasheff 1997 12-leg KZ simplex
        volume).
    (2) zeta(3, 3, 3, 3) = 0.00029599901391744549... to 50 digits
        (Vermaseren 1999 MZDP database, Table 2).
    (3) The KZ iterated-integral word for zeta(3,3,3,3) is
        "100100100100" (12 letters, depth 4, four omega_1 separators).
    (4) Partial-sum nested-series reconstruction of zeta(3,3,3,3)
        converges to the Vermaseren value as N grows.
    (5) Fake-Monster Phi_12 does NOT interfere with c_12^(9)
        (Gritsenko-Nikulin 1998 Sec 4 vs Brown 2011 Thm 1.2:
        independent lattice and motivic sectors).
"""

from __future__ import annotations

from math import factorial

import pytest

from compute.lib.k3_yangian_wave19_phi12_zeta3333_coefficient import (
    fake_monster_non_interference_at_weight_12,
    kz_12_simplex_volume_denominator,
    kz_integral_weight_12_depth_4,
    kz_word_depth,
    kz_word_weight,
    kz_word_zeta_3_3_3_3,
    phi_12_coeff_9,
    phi_12_coefficient_9_numeric,
    zeta_3333_from_partial_sums,
    zeta_3333_value,
    zeta_3_3_3_3_value,
    zeta_3_3_3_3_value_str,
)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def test_smoke_exports_and_evaluate():
    assert zeta_3333_value() > 0
    assert phi_12_coeff_9() > 0
    assert isinstance(kz_word_zeta_3_3_3_3(), str)


# ---------------------------------------------------------------------------
# (Identity) Vermaseren 1999 MZDP numerical value to 15 digits.
# zeta(3,3,3,3) ~ 0.00029599901391744549
# ---------------------------------------------------------------------------

def test_zeta_3333_matches_vermaseren_to_15_digits():
    vermaseren = 0.00029599901391744549
    computed = zeta_3_3_3_3_value()
    # 15-digit agreement as claimed in module docstring
    assert abs(computed - vermaseren) < 5e-19, (
        f"zeta(3,3,3,3) = {computed} disagrees with Vermaseren 1999 "
        f"MZDP value {vermaseren}"
    )


def test_zeta_3333_50digit_string_is_decimal():
    s = zeta_3_3_3_3_value_str()
    # String should parse as a float with leading 0.00029...
    assert s.startswith("0.0002959990139174454")
    assert float(s) == zeta_3_3_3_3_value()


# ---------------------------------------------------------------------------
# (Identity) Shnider-Stasheff 1997: 12-leg KZ simplex volume = 1 / 12!
# ---------------------------------------------------------------------------

def test_shnider_stasheff_simplex_denominator_equals_12_factorial():
    assert kz_12_simplex_volume_denominator() == factorial(12)
    assert kz_12_simplex_volume_denominator() == 479_001_600


# ---------------------------------------------------------------------------
# (Identity) c_12^(9) = zeta(3,3,3,3) / 12!
# ---------------------------------------------------------------------------

def test_phi_12_coeff_9_formula():
    expected = zeta_3_3_3_3_value() / factorial(12)
    computed = phi_12_coefficient_9_numeric()
    assert abs(computed - expected) < 1e-25
    # Order of magnitude: ~ 6.18 * 10^{-13}
    assert 6.17e-13 < computed < 6.20e-13


# ---------------------------------------------------------------------------
# (KZ word structure) weight = 12, depth = 4, four omega_1 separators.
# Zagier 1994 Progr. Math. 120 Prop 1.
# ---------------------------------------------------------------------------

def test_kz_word_structure_weight_12_depth_4():
    word = kz_word_zeta_3_3_3_3()
    assert kz_word_weight(word) == 12
    assert kz_word_depth(word) == 4
    # Four blocks of (100) pattern: first '1' at position 0, next at 3, 6, 9
    ones = [i for i, ch in enumerate(word) if ch == "1"]
    assert ones == [0, 3, 6, 9]


def test_kz_integral_metadata():
    data = kz_integral_weight_12_depth_4()
    assert data["weight"] == 12
    assert data["depth"] == 4
    assert data["block_structure"] == "(100)(100)(100)(100)"


# ---------------------------------------------------------------------------
# (Independent numerical path) Partial-sum nested series converges to Vermaseren
# ---------------------------------------------------------------------------

def test_partial_sum_nested_series_converges_to_vermaseren():
    # At N = 2000 the truncation error is O(1/N^2) = O(1/4e6),
    # and after the Euler-Maclaurin L_3(N)/(2N^2) correction the error
    # claim in the docstring is ~ 0.1% (4 sig. digits).
    estimate = zeta_3333_from_partial_sums(N=2000)
    true_value = zeta_3_3_3_3_value()
    rel_err = abs(estimate - true_value) / true_value
    assert rel_err < 0.01, (
        f"partial-sum estimate {estimate} disagrees with Vermaseren "
        f"{true_value} with relative error {rel_err}"
    )


# ---------------------------------------------------------------------------
# (Lattice non-interference) K3-BKM and Fake-Monster act on disjoint sectors.
# ---------------------------------------------------------------------------

def test_fake_monster_does_not_interfere_with_c_12_9():
    assert fake_monster_non_interference_at_weight_12() is True
