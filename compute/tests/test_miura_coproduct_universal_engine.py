r"""Tests for miura_coproduct_universal_engine.

Module claims (Miura coefficient universality at spins 2, 3, 4):
    Delta_z(W_s) = W_s . 1 + 1 . W_s + c_s * (J . W_{s-1} + W_{s-1} . J)
                   + (lower-spin / composite / spectral corrections)
    c_s = (Psi - 1) / Psi   for s in {2, 3, 4}.

Primary literature anchors:
    Prochazka-Rapcak arXiv:1711.11582 (Miura transform for W_{1+inf}).
    Tsymbaliuk arXiv:1404.5240 (affine Yangian coproduct).
    Drinfeld 1988 (Yangian coproduct formula binom(n-k-1, m-1)).

Verification paths:
    (1) Miura relations: psi_1 = J, psi_2 = T + :J^2:/(2 Psi), etc.
    (2) Drinfeld coproduct formula gives primitive coefficient binom(n-k-1, m-1).
    (3) (Psi - 1)/Psi is stable across s = 2, 3, 4 (universality).
    (4) Limiting cases: Psi -> oo, Psi = 1.
"""

from __future__ import annotations

import pytest

from sympy import (
    Rational,
    Symbol,
    binomial,
    limit,
    oo,
    simplify,
    symbols,
)

from compute.lib.miura_coproduct_universal_engine import (
    cross_spin_table,
    delta_composite_JW,
    delta_composite_TT,
    delta_psi,
    evaluate_cross_coefficient,
    miura_coefficients,
    primary_cross_coefficient,
    verify_classical_limit_coeff,
    verify_conjecture_at_spin,
    verify_free_boson_limit,
)


Psi_sym, z_sym = symbols("Psi z", commutative=True)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def test_smoke_primary_cross_coefficient_runs():
    for s in (2, 3, 4):
        c = primary_cross_coefficient(s)
        assert c is not None


# ---------------------------------------------------------------------------
# (Identity) Drinfeld coproduct: Delta_z(psi_1) = J.1 + 1.J is primitive.
# Drinfeld 1988 formula Delta_z(psi_n) = psi_n . 1 + sum_{k, m} binom(...)
# ---------------------------------------------------------------------------

def test_drinfeld_coproduct_psi1_is_primitive():
    d1 = delta_psi(1)
    assert d1[(1, 0)] == 1  # psi_1 . 1
    assert d1[(0, 1)] == 1  # 1 . psi_1
    # No other terms
    assert set(d1.keys()) == {(1, 0), (0, 1)}


def test_drinfeld_coproduct_psi2_cross_term_binomial():
    d2 = delta_psi(2, z=0)
    # psi_1 . psi_1 entry: binom(2 - 1 - 1, 1 - 1) z^0 = binom(0, 0) = 1
    assert simplify(d2.get((1, 1), 0) - 1) == 0


@pytest.mark.parametrize("n", [2, 3, 4, 5])
def test_drinfeld_cross_coefficient_equals_binom_sm2_sm2(n):
    # psi_{n} cross-term at (k, m) = (1, n-1): coefficient is
    #   binom(n - k - 1, m - 1) z^{n - k - m} = binom(n-2, n-2) = 1
    # (at z = 0 or as the leading-order coefficient).
    dn = delta_psi(n, z=0)
    coeff = dn.get((1, n - 1), 0)
    expected = int(binomial(n - 2, n - 2))
    assert simplify(coeff - expected) == 0


# ---------------------------------------------------------------------------
# (Identity) Miura relations match Prochazka-Rapcak 1711.11582
# ---------------------------------------------------------------------------

def test_miura_psi_2_relation():
    mc = miura_coefficients(2)
    assert mc["T"] == 1
    # :J^2: coefficient = 1 / (2 Psi)
    assert simplify(mc[":J^2:"] - 1 / (2 * Psi_sym)) == 0


def test_miura_psi_3_relation():
    mc = miura_coefficients(3)
    assert mc["W"] == 1
    # :JT: coefficient = 1/Psi, :J^3: coefficient = 1/(6 Psi^2), J'' = 1/(2 Psi)
    assert simplify(mc[":JT:"] - 1 / Psi_sym) == 0
    assert simplify(mc[":J^3:"] - 1 / (6 * Psi_sym ** 2)) == 0


def test_miura_psi_4_includes_J_W_composite():
    mc = miura_coefficients(4)
    assert mc["W_4"] == 1
    # :JW: coefficient = 1/Psi  (this is what carries the universality proof)
    assert simplify(mc[":JW:"] - 1 / Psi_sym) == 0


# ---------------------------------------------------------------------------
# (Identity) :JW: coproduct contributes (J, W) and (W, J) with coefficient 1.
# This is the step that combines with Drinfeld to produce (Psi-1)/Psi.
# ---------------------------------------------------------------------------

def test_delta_JW_produces_J_W_with_coefficient_one():
    d = delta_composite_JW()
    assert simplify(d.get(("J", "W"), 0) - 1) == 0
    assert simplify(d.get(("W", "J"), 0) - 1) == 0


def test_delta_TT_has_no_W_components():
    # :TT: involves only J, T, so cannot produce W on either side.
    # The J.W and W.J coefficients in Delta_z(:TT:) must be zero.
    d = delta_composite_TT()
    assert d == {}


# ---------------------------------------------------------------------------
# (Identity) Universality: c_s = (Psi-1)/Psi for s in {2, 3, 4}.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", [2, 3, 4])
def test_primary_cross_coefficient_equals_psi_minus_one_over_psi(s):
    c = primary_cross_coefficient(s)
    expected = simplify((Psi_sym - 1) / Psi_sym)
    assert simplify(c - expected) == 0, (
        f"primary cross-coefficient at s={s}: {c} != (Psi-1)/Psi"
    )


# ---------------------------------------------------------------------------
# (Limiting case) Classical limit Psi -> oo: c_s -> 1.
# (Limiting case) Free-boson limit Psi = 1: c_s = 0.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", [2, 3, 4])
def test_classical_limit_gives_one(s):
    data = verify_classical_limit_coeff(s)
    assert data["match"] is True, (
        f"classical limit at s={s}: c_s -> {data['c_s_classical']} != 1"
    )
    assert data["expected"] == 1


@pytest.mark.parametrize("s", [2, 3, 4])
def test_free_boson_limit_gives_zero(s):
    data = verify_free_boson_limit(s)
    assert data["match"] is True, (
        f"free-boson limit at s={s}: c_s = {data['c_s']} != 0 at Psi=1"
    )
    assert data["expected"] == 0


# ---------------------------------------------------------------------------
# (Symmetry / cross-spin)  The same universal coefficient at each s.
# ---------------------------------------------------------------------------

def test_cross_spin_table_all_spins_universal():
    data = cross_spin_table()
    # The table is nested: data["table"]["spin_s"] -> {c_s, expected, match}
    assert data["all_match"] is True
    assert data["conjecture_holds_through_spin_4"] is True
    for s in (2, 3, 4):
        entry = data["table"][f"spin_{s}"]
        assert entry["match"] is True, (
            f"spin {s} universality failed: c_s={entry['c_s']}, "
            f"expected={entry['expected']}"
        )
