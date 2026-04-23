r"""Tests for miura_universality_proof_engine.

Module claims (thm:miura-cross-universality):
    coeff_{J tensor W_{s-1} + W_{s-1} tensor J}(Delta_z(W_s)) = (Psi-1)/Psi
for all s >= 2.

This is verified via three channels:
    (DC)  Direct Drinfeld coefficient from Delta_z(psi_s) at (psi_1, psi_{s-1}).
    (LT)  Fateev-Lukyanov Miura factorization: one distinguished J insertion
          in the single-J sector of the elementary-symmetric Miura product.
    (LC)  Limiting cases: Psi -> infinity gives 1 (classical);
          Psi = 1 gives 0 (free boson).

Verification paths:
    (1) Drinfeld coproduct: binom(n-k-1, m-1) at k=1, m=s-1 gives
        binom(s-2, s-2) = 1 for the psi_1 tensor psi_{s-1} cross-term.
    (2) Single-J Miura sector: every ordered term has coefficient exactly 1/Psi.
    (3) Total = Drinfeld - Miura single-J = 1 - 1/Psi = (Psi-1)/Psi.
    (4) Psi -> oo gives (Psi-1)/Psi -> 1 (classical limit).
    (5) Psi = 1 gives 0 (free-boson degeneration).
"""

from __future__ import annotations

import pytest

from sympy import (
    Rational,
    Symbol,
    limit,
    oo,
    simplify,
    symbols,
)

from compute.lib.miura_universality_proof_engine import (
    SPINS_TO_TEST,
    combined_cross_coefficient,
    delta_psi,
    drinfeld_cross_term_data,
    lower_miura_noncontribution_data,
    miura_sector_expression,
    run_assertions,
    single_j_miura_channel_data,
    verify_spin,
)


Psi_sym = Symbol("Psi", commutative=True)


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

def test_smoke_verify_spin_runs_at_s_2():
    result = verify_spin(2)
    assert "drinfeld" in result
    assert "miura" in result
    assert "combined" in result


# ---------------------------------------------------------------------------
# (Identity) Drinfeld coproduct binomial: binom(s-2, s-2) = 1
# This gives the psi_1 tensor psi_{s-1} cross-coefficient exactly 1.
# Primary: Drinfeld 1988 (Yangians), Tsymbaliuk arXiv:1404.5240.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", [2, 3, 4, 5, 6])
def test_drinfeld_cross_coefficient_equals_one(s):
    data = drinfeld_cross_term_data(s)
    assert simplify(data["left_cross_coefficient"] - 1) == 0, (
        f"Drinfeld left cross-coefficient at s={s}: "
        f"{data['left_cross_coefficient']}"
    )
    assert simplify(data["right_cross_coefficient"] - 1) == 0


# ---------------------------------------------------------------------------
# (Identity) Miura single-J sector: every ordered term has coefficient 1/Psi
# Fateev-Lukyanov: one distinguished J insertion, (s-1) P-slots for W_{s-1}.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", [2, 3, 4, 5, 6])
def test_miura_single_j_ordered_coefficient_is_one_over_psi(s):
    data = single_j_miura_channel_data(s)
    assert simplify(data["ordered_channel_coefficient"] - 1 / Psi_sym) == 0
    # Exactly s ordered terms (one per choice of J-slot)
    assert data["number_of_ordered_terms"] == s


# ---------------------------------------------------------------------------
# (Identity) Total cross coefficient equals (Psi-1)/Psi at every spin
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", list(SPINS_TO_TEST))
def test_total_cross_coefficient_equals_psi_minus_one_over_psi(s):
    data = combined_cross_coefficient(s)
    expected = simplify((Psi_sym - 1) / Psi_sym)
    assert simplify(data["total"] - expected) == 0, (
        f"total cross-coefficient at s={s}: "
        f"{data['total']} != {expected}"
    )


# ---------------------------------------------------------------------------
# (Limiting case) Psi -> infinity: classical limit, (Psi-1)/Psi -> 1
# (Limiting case) Psi = 1: free-boson degeneration, (Psi-1)/Psi = 0
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", [2, 3, 4])
def test_classical_and_free_boson_limits(s):
    result = verify_spin(s)
    assert simplify(result["classical_limit"] - 1) == 0, (
        f"classical (Psi -> oo) limit at s={s}: {result['classical_limit']}"
    )
    assert simplify(result["free_boson_value"]) == 0, (
        f"free-boson (Psi = 1) value at s={s}: {result['free_boson_value']}"
    )


# ---------------------------------------------------------------------------
# (Symmetry / non-interference) Lower Miura sectors (k >= 2) have W-spin
# support <= s-2 and cannot hit the J tensor W_{s-1} channel on either side.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("s", [3, 4, 5])
def test_lower_miura_sectors_do_not_hit_target_channel(s):
    lower = lower_miura_noncontribution_data(s)
    # For each k >= 2, the Miura sector :J^k . W_{s-k}: has W-spin = s-k <= s-2
    for item in lower:
        assert item["hits_target_channel"] is False, (
            f"lower Miura sector at s={s}, k={item['k']} hits target channel"
        )


# ---------------------------------------------------------------------------
# (Consolidated) run_assertions passes at all tested spins
# ---------------------------------------------------------------------------

def test_run_assertions_all_spins_pass():
    results = run_assertions()
    assert set(results.keys()) == set(SPINS_TO_TEST)
