r"""Tests for mc_crossing_theorem_engine.

Module claims (thm:thqg-VII-crossing-from-mc):
    The (g, n) = (0, 4) projection of the Maurer-Cartan equation
        D Theta + (1/2) [Theta, Theta] = 0
    is equivalent to crossing symmetry of the 4-point function.

Numerical deliverable: Q^contact(Vir_c) = 10 / [c * (5c + 22)].
Poles at c = 0 and c = -22/5.

Primary literature:
    Belavin-Polyakov-Zamolodchikov 1984 (Virasoro TT OPE).
    Zamolodchikov 1986 (:TT: - (3/10) d^2 T quasi-primary at level 4).
    Costello arXiv:2412.17168 (OPE associativity => all loop amplitudes).

Verification paths:
    (1) kappa(Vir_c) = c / 2 (AP1 Virasoro formula).
    (2) Virasoro level-4 Gram matrix determinant = c^2 (5c + 22) / 2.
    (3) Zamolodchikov quasi-primary Lambda = L_{-2}^2 |0> - (3/5) L_{-4} |0>
        with <Lambda|Lambda> = c(5c+22)/10.
    (4) Q^contact = 1 / <Lambda|Lambda> = 10 / [c(5c+22)].
    (5) Limiting cases: Ising c=1/2, free boson c=1, critical string c=26.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from sympy import (
    Rational,
    Symbol,
    expand,
    factor,
    simplify,
    symbols,
)

from compute.lib.mc_crossing_theorem_engine import (
    Q_contact_virasoro,
    c_sym,
    ising_crossing_from_mc,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_wn,
    mbar04_boundary_structure,
    mc_direct_expansion_genus0_arity4,
    virasoro_level4_gram_matrix,
    virasoro_ope_modes,
    virasoro_quasi_primary_lambda,
)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def test_smoke_module_runs_at_c_26():
    result = mc_direct_expansion_genus0_arity4(Rational(26))
    assert "Q_contact_from_mc" in result


# ---------------------------------------------------------------------------
# (Identity, AP1) kappa formulas are family-specific.
#   kappa(Vir_c)   = c / 2
#   kappa(H_k)     = k
#   kappa(V_k sl_2)= 3 (k + 2) / 4
#   kappa(W_N, c)  = c (H_N - 1)
# ---------------------------------------------------------------------------

def test_kappa_virasoro_is_c_over_2():
    assert kappa_virasoro(Rational(26)) == Rational(13)
    assert kappa_virasoro(Rational(1)) == Rational(1, 2)
    assert kappa_virasoro(Rational(-22, 5)) == Rational(-11, 5)


def test_kappa_heisenberg_is_k():
    assert kappa_heisenberg(3) == 3
    assert kappa_heisenberg(Rational(5, 2)) == Rational(5, 2)


def test_kappa_affine_sl2_is_3_k_plus_2_over_4():
    # V_1 sl_2: kappa = 3 * (1 + 2) / 4 = 9/4
    assert kappa_affine_sl2(1) == Rational(9, 4)
    # V_k=0: kappa = 3 * 2 / 4 = 3/2 (the "almost trivial" level)
    assert kappa_affine_sl2(0) == Rational(3, 2)


def test_kappa_wn_equals_c_times_H_N_minus_1():
    # H_3 - 1 = (1/2 + 1/3) = 5/6
    assert kappa_wn(3, Rational(6)) == Rational(5)  # 6 * 5/6 = 5
    # W_1 has trivial kappa = 0
    assert kappa_wn(1, Rational(10)) == Rational(0)


# ---------------------------------------------------------------------------
# (Identity) Virasoro level-4 Gram matrix (BPZ 1984; Zamolodchikov 1986)
#   G_{11} = <0| L_4 L_{-4} |0> = 5c
#   G_{12} = <0| L_4 L_{-2}^2 |0> = 3c
#   G_{22} = <0| L_2^2 L_{-2}^2 |0> = c(c+8)/2
#   det G = c^2 (5c + 22) / 2
# ---------------------------------------------------------------------------

def test_virasoro_level4_gram_matrix_entries():
    g = virasoro_level4_gram_matrix(c_sym)
    assert simplify(g["G11"] - 5 * c_sym) == 0
    assert simplify(g["G12"] - 3 * c_sym) == 0
    assert simplify(g["G22"] - c_sym * (c_sym + 8) / 2) == 0


def test_virasoro_level4_gram_determinant():
    g = virasoro_level4_gram_matrix(c_sym)
    expected = c_sym ** 2 * (5 * c_sym + 22) / 2
    assert simplify(g["determinant"] - expected) == 0


# ---------------------------------------------------------------------------
# (Identity) Zamolodchikov quasi-primary Lambda = :TT: - (3/10) d^2 T
# <Lambda | Lambda> = c(5c+22)/10  (constitutional cache entry from CLAUDE.md)
# ---------------------------------------------------------------------------

def test_zamolodchikov_quasi_primary_norm_equals_c_5c_plus_22_over_10():
    data = virasoro_quasi_primary_lambda(c_sym)
    expected = c_sym * (5 * c_sym + 22) / 10
    assert simplify(data["norm_Lambda"] - expected) == 0
    # L_1 annihilation is exact (a_state = 3/5):
    assert data["L1_check"] is True
    assert data["a_state"] == Rational(3, 5)
    assert data["a_field"] == Rational(3, 10)


# ---------------------------------------------------------------------------
# (Identity) Q^contact = 10 / [c (5c + 22)] (Virasoro)
# This is the reciprocal of <Lambda|Lambda> / 1 = c(5c+22)/10.
# ---------------------------------------------------------------------------

def test_q_contact_virasoro_equals_ten_over_c_times_5c_plus_22():
    # Rational input: exact Sympy
    q = Q_contact_virasoro(Rational(26))
    assert simplify(q - Rational(10, 26 * (5 * 26 + 22))) == 0  # 10/(26*152) = 10/3952


def test_q_contact_virasoro_symbolic_form():
    result = mc_direct_expansion_genus0_arity4(Rational(26))
    assert result["mc_derivation_consistent"] is True


@pytest.mark.parametrize("c_int", [1, 26, 2, 12])
def test_q_contact_equals_reciprocal_of_lambda_norm(c_int):
    # Q^contact = 1 / <Lambda | Lambda> with normalisation <Lambda|Lambda> = c(5c+22)/10
    c = Rational(c_int)
    q = Q_contact_virasoro(c)
    lambda_norm = c * (5 * c + 22) / 10
    product = simplify(q * lambda_norm)
    assert product == 1, (
        f"Q^contact({c}) * <Lambda|Lambda> = {product} != 1 "
        f"(violates the contact / Zamolodchikov norm reciprocity)"
    )


# ---------------------------------------------------------------------------
# (Symmetry) Mbar_{0,4} = P^1 with three boundary divisors.
# [D_s] + [D_t] + [D_u] = 0 is the topological origin of crossing.
# ---------------------------------------------------------------------------

def test_mbar04_has_three_boundary_divisors():
    data = mbar04_boundary_structure()
    assert data["moduli_space"] == "M-bar_{0,4} = P^1"
    assert data["dimension"] == 1
    assert set(data["boundary_divisors"].keys()) == {"D_s", "D_t", "D_u"}


# ---------------------------------------------------------------------------
# (Limiting case) Ising at c = 1/2: Q^contact = 10 / [(1/2)(5/2 + 22)] = 10/(1/2 * 49/2)
#  = 10 * 4 / 49 = 40/49
# ---------------------------------------------------------------------------

def test_q_contact_at_ising_c_one_half():
    c = Rational(1, 2)
    q = Q_contact_virasoro(c)
    expected = Rational(10) / (c * (5 * c + 22))  # 10 / (1/2 * 49/2) = 10 * 4/49 = 40/49
    assert simplify(q - expected) == 0
    assert simplify(q - Rational(40, 49)) == 0


# ---------------------------------------------------------------------------
# (TT OPE mode data) T_{(3)} T = c / 2 (quartic pole)
# ---------------------------------------------------------------------------

def test_virasoro_tt_ope_modes():
    modes = virasoro_ope_modes(Rational(26))
    assert modes["T_(3)_T"] == Rational(13)   # c/2 at c=26
    assert modes["T_(2)_T"] == Rational(0)
    # Lambda-bracket: (c/12) * lambda^3 + 2T * lambda + dT
    assert modes["lambda_bracket_coeff_3"] == Rational(26, 12)
