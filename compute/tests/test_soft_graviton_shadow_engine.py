"""Tests for the soft graviton shadow engine.

The oracle in this file is independent of the engine implementation:
    - the engine uses the convolution recursion for sqrt(Q_L);
    - these tests use a direct SymPy Taylor expansion of sqrt(Q_L).

The local normalization is:
    a_r(c) = S_r(c), where S_r(z; c) = a_r(c) / z^r + O(z^{-(r-1)}).
"""

from __future__ import annotations

import pytest
import sympy as sp

from compute.lib.soft_graviton_shadow_engine import (
    CENTRAL_CHARGE,
    QUADRATIC_CASIMIR,
    STRESS_TENSOR_ZERO_MODE,
    compare_with_weinberg_soft_theorems,
    soft_graviton_coefficient,
    soft_graviton_coefficients,
    soft_graviton_expansion,
    soft_graviton_operator_data,
)


T = sp.Symbol("t")
Z = sp.Symbol("z")


def _independent_series_coefficients(c_value: sp.Expr, max_arity: int = 7) -> dict[int, sp.Expr]:
    """Independent oracle from the direct Taylor series of sqrt(Q_L(t))."""

    c_expr = sp.sympify(c_value)
    q_l = (c_expr + 6 * T) ** 2 + sp.Rational(80, 1) * T**2 / (5 * c_expr + 22)
    sqrt_series = sp.series(sp.sqrt(q_l), T, 0, max_arity - 1).removeO()
    return {
        arity: sp.factor(sp.cancel(sqrt_series.coeff(T, arity - 2) / arity))
        for arity in range(2, max_arity + 1)
    }


REFERENCE_CASES = [
    (
        sp.Integer(1),
        sp.Rational(1, 2),
        sp.Integer(2),
        sp.Rational(10, 27),
    ),  # VERIFIED: [DC] direct substitution into a_2=c/2, a_3=2, a_4=10/[c(5c+22)]; [CF] agrees with the local Virasoro T-line shadow formulas already used in the repo.
    (
        sp.Integer(13),
        sp.Rational(13, 2),
        sp.Integer(2),
        sp.Rational(10, 1131),
    ),  # VERIFIED: [DC] direct substitution into the closed formulas; [LC] a_3 stays c-independent while a_4 remains positive and small at the self-dual point c=13.
    (
        sp.Integer(26),
        sp.Integer(13),
        sp.Integer(2),
        sp.Rational(5, 1976),
    ),  # VERIFIED: [DC] direct substitution into the closed formulas; [CF] matches the critical-string T-line normalization already used in the local celestial and soft-theorem surfaces.
]


def test_symbolic_low_arity_formulas():
    coeffs = soft_graviton_coefficients(max_arity=4)

    assert sp.simplify(coeffs[2] - CENTRAL_CHARGE / 2) == 0
    assert sp.simplify(coeffs[3] - 2) == 0
    assert sp.simplify(coeffs[4] - sp.Rational(10, 1) / (CENTRAL_CHARGE * (5 * CENTRAL_CHARGE + 22))) == 0


def test_requested_arity_window_is_present():
    coeffs = soft_graviton_coefficients(max_arity=7)

    assert sorted(coeffs) == [2, 3, 4, 5, 6, 7]


@pytest.mark.parametrize("c_value", [sp.Integer(1), sp.Integer(13), sp.Integer(26)])
def test_coefficients_through_seven_match_independent_series(c_value: sp.Expr):
    actual = soft_graviton_coefficients(max_arity=7, central_charge=c_value)
    expected = _independent_series_coefficients(c_value, max_arity=7)

    for arity in range(2, 8):
        assert sp.simplify(actual[arity] - expected[arity]) == 0


@pytest.mark.parametrize(("c_value", "expected_a2", "expected_a3", "expected_a4"), REFERENCE_CASES)
def test_explicit_a2_a3_a4_values(c_value: sp.Expr, expected_a2: sp.Expr, expected_a3: sp.Expr, expected_a4: sp.Expr):
    assert sp.simplify(soft_graviton_coefficient(2, c_value) - expected_a2) == 0
    assert sp.simplify(soft_graviton_coefficient(3, c_value) - expected_a3) == 0
    assert sp.simplify(soft_graviton_coefficient(4, c_value) - expected_a4) == 0


def test_soft_expansion_uses_requested_pole_orders():
    expansion = sp.expand(soft_graviton_expansion(max_arity=4, soft_coordinate=Z))

    expected = (
        CENTRAL_CHARGE / (2 * Z**2)
        + sp.Integer(2) / Z**3
        + sp.Rational(10, 1) / (CENTRAL_CHARGE * (5 * CENTRAL_CHARGE + 22) * Z**4)
    )
    assert sp.simplify(expansion - expected) == 0


def test_operator_dressing_tracks_expected_channels():
    operator_data = soft_graviton_operator_data(max_arity=7, central_charge=26)

    assert operator_data[2].operator == 1
    assert operator_data[2].pole_order == 2
    assert operator_data[3].operator == STRESS_TENSOR_ZERO_MODE
    assert operator_data[3].pole_order == 3
    assert operator_data[4].operator == QUADRATIC_CASIMIR
    assert operator_data[4].pole_order == 4


def test_soft_theorem_structure_report_matches_expectations():
    comparison = compare_with_weinberg_soft_theorems(26)

    assert comparison[2].matches_expected_structure is True
    assert sp.simplify(comparison[2].scalar_prefactor - 13) == 0
    assert comparison[2].coefficient_is_universal is False

    assert comparison[3].matches_expected_structure is True
    assert comparison[3].operator == STRESS_TENSOR_ZERO_MODE
    assert sp.simplify(comparison[3].scalar_prefactor - 2) == 0
    assert comparison[3].coefficient_is_universal is True

    assert comparison[4].matches_expected_structure is True
    assert comparison[4].operator == QUADRATIC_CASIMIR
    assert sp.simplify(comparison[4].scalar_prefactor - sp.Rational(5, 1976)) == 0
    assert comparison[4].coefficient_is_universal is False
