"""Tests for true_formula_census_verifier.py.

Each canonical census entry C01-C10 must pass exactly as written, and the
known anti-pattern variants must fail at the named audit points.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import pytest


LIB_DIR = Path(__file__).resolve().parent.parent / "lib"
if str(LIB_DIR) not in sys.path:
    sys.path.insert(0, str(LIB_DIR))

import true_formula_census_verifier as verifier


@pytest.mark.parametrize(
    "check_name",
    [
        "C01",
        "C02",
        "C03",
        "C04",
        "C05",
        "C06",
        "C07",
        "C08",
        "C09",
        "C10",
    ],
)
def test_canonical_check_passes(check_name: str) -> None:
    """Every canonical census check must pass with computed == expected."""
    result = getattr(verifier, f"verify_{check_name}")()
    assert result["passed"] is True
    assert result["computed"] == result["expected"]


def test_kappa_from_rmatrix_rejects_bare_omega_over_z() -> None:
    """AP126/AP141: bare Omega/z without a level prefix is rejected."""
    with pytest.raises(ValueError, match="AP126/AP141"):
        verifier.kappa_from_rmatrix(None, Fraction(3, 2))


def test_w_n_h_n_minus_1_variant_fails() -> None:
    """AP136: H_{N-1} does not reproduce the canonical W_N coefficient."""
    wrong = verifier.harmonic_number(2)
    canonical = verifier.kappa_w_n(3, 1)
    assert wrong != canonical
    assert wrong == Fraction(3, 2)
    assert canonical == Fraction(5, 6)


def test_e8_bogus_dimension_injection_fails_membership_check() -> None:
    """Wave 10-8 bogus 779247 is not a fundamental E_8 dimension."""
    bogus_dimensions = (
        248,
        3875,
        30380,
        147250,
        779247,
        2450240,
        6696000,
        146325270,
    )
    assert verifier.validate_e8_fundamental_dimensions(bogus_dimensions) is False


def test_bc_reciprocal_swap_formula_fails_at_lambda_2() -> None:
    """AP129: the reciprocal-swap variant does not return the ghost value -26."""
    lam = Fraction(2)
    wrong = 1 - Fraction(3, (2 * lam - 1) ** 2)
    canonical = verifier.central_charge_bc(lam)
    assert wrong != canonical
    assert wrong != Fraction(-26)
    assert canonical == Fraction(-26)


def test_virasoro_complementarity_26_fails() -> None:
    """AP24: Virasoro complementarity is 13, not the raw critical dimension 26."""
    complementarity_sum = (
        verifier.kappa_virasoro(25)
        + verifier.kappa_virasoro(verifier.virasoro_dual_c(25))
    )
    assert complementarity_sum != Fraction(26)
    assert complementarity_sum == Fraction(13)
