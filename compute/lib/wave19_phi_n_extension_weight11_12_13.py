"""Motivic weight data at orders eleven, twelve, and thirteen.

The Hoffman words in the alphabet {2,3} give dimensions 9, 12, and 16.
At weight twelve the repeated period zeta(3,3,3,3) obeys the exact
Newton identity and has zero primitive projection.  These arithmetic
facts specify inputs to an associator comparison.  The order-n cyclic
operation additionally requires a represented KZ word, a
word-to-cochain map, a solution of the Maurer--Cartan equation, and
the relevant comparison homotopies.
"""

from __future__ import annotations

from math import factorial
from typing import Dict, Iterable, Tuple

from compute.lib.k3_yangian_wave18_pentagon_coboundary_hbar11_12 import (
    hoffman_words,
    kz_normalization_status,
    mzv_basis,
    padovan_dim,
    zeta3333_status,
)


SUPPORTED_WEIGHTS: Tuple[int, ...] = (11, 12, 13)


def motivic_dimension_table(
    start: int = 0, stop: int = 13
) -> Dict[int, int]:
    """Return the Hoffman dimensions on an inclusive weight interval."""
    if start < 0:
        raise ValueError("start must be nonnegative")
    if stop < start:
        raise ValueError("stop must be at least start")
    return {weight: padovan_dim(weight) for weight in range(start, stop + 1)}


def weight_order_status(weight: int) -> Dict[str, object]:
    """Return exact arithmetic and explicit chain-level obligations."""
    if weight < 0:
        raise ValueError("weight must be nonnegative")

    repeated = zeta3333_status() if weight == 12 else None
    return {
        "weight": weight,
        "hoffman_words": hoffman_words(weight),
        "hoffman_basis": mzv_basis(weight),
        "motivic_dimension": padovan_dim(weight),
        "simplex_denominator": factorial(weight),
        "kz_normalization": kz_normalization_status(weight),
        "zeta3333": repeated,
        "associator_chosen": False,
        "represented_kz_word_constructed": False,
        "word_to_cochain_map_constructed": False,
        "cyclic_cochain_constructed": False,
        "rotation_equation_verified": False,
        "maurer_cartan_equation_verified": False,
        "phi_n_constructed": False,
        "status": "exact motivic arithmetic; cyclic comparison open",
    }


def weight_extension_status(
    weights: Iterable[int] = SUPPORTED_WEIGHTS,
) -> Dict[int, Dict[str, object]]:
    """Return the status at each requested weight."""
    return {weight: weight_order_status(weight) for weight in weights}


def run_tests() -> Dict[str, bool]:
    """Run internal exact checks."""
    table = motivic_dimension_table(0, 13)
    statuses = weight_extension_status()
    return {
        "dimension_11": table[11] == 9,
        "dimension_12": table[12] == 12,
        "dimension_13": table[13] == 16,
        "recurrence_11": table[11] == table[9] + table[8],
        "recurrence_12": table[12] == table[10] + table[9],
        "recurrence_13": table[13] == table[11] + table[10],
        "hoffman_word_counts": all(
            len(statuses[weight]["hoffman_words"])
            == statuses[weight]["motivic_dimension"]
            for weight in SUPPORTED_WEIGHTS
        ),
        "zeta3333_product_sector": (
            statuses[12]["zeta3333"]["primitive_projection"] == 0
        ),
        "weight_11_phi_open": statuses[11]["phi_n_constructed"] is False,
        "weight_12_phi_open": statuses[12]["phi_n_constructed"] is False,
        "weight_13_phi_open": statuses[13]["phi_n_constructed"] is False,
    }


if __name__ == "__main__":
    checks = run_tests()
    for name, passed in checks.items():
        print(f"{name}: {passed}")
    if not all(checks.values()):
        raise SystemExit(1)
