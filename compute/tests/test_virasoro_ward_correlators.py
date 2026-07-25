r"""Exact checks for the Virasoro sphere Ward recursion through arity six.

The independent oracle is the free-boson realization
``T=(1/2):J^2:`` at ``c=1``.  It enumerates every perfect matching of the
``2n`` current insertions, discards self-contractions at each normal-ordered
vertex, and evaluates the remaining contractions over the rationals.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterator

import pytest
import sympy as sp

from compute.lib.virasoro_ward_correlators import (
    CENTRAL_CHARGE,
    ResidueProjectionRequired,
    cycle_connected_correlator,
    evaluate_connected_correlator,
    evaluate_cycle_expansion,
    evaluate_ward_correlator,
    require_residue_projection,
    standard_points,
    virasoro_connected_correlator,
    virasoro_ward_correlator,
    ward_recursion_terms,
)


FULL_C_ONE_AT_CONSECUTIVE_POINTS = {
    # Exact free-boson matching sums at z_i=i, divided by 2^n.
    2: sp.Rational(1, 2),
    3: sp.Rational(1, 4),
    4: sp.Rational(36049, 82944),
    5: sp.Rational(2443325, 5971968),
    6: sp.Rational(90812103752809, 174142586880000),
}

CONNECTED_C_ONE_AT_CONSECUTIVE_POINTS = {
    # Möbius inversion of the preceding exact moment values.
    2: sp.Rational(1, 2),
    3: sp.Rational(1, 4),
    4: sp.Rational(13, 72),
    5: sp.Rational(775, 5184),
    6: sp.Rational(49705, 373248),
}


def _perfect_matchings(items: tuple[tuple[int, int], ...]) -> Iterator[tuple]:
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        partner = items[index]
        remaining = items[1:index] + items[index + 1 :]
        for matching in _perfect_matchings(remaining):
            yield ((first, partner),) + matching


def _free_boson_wick_value(coordinates: tuple[int, ...]) -> Fraction:
    """Direct Wick sum for ``T=(1/2):J^2:`` and ``<JJ>=z_ij^-2``."""

    half_edges = tuple(
        (vertex, leg)
        for vertex in range(len(coordinates))
        for leg in range(2)
    )
    total = Fraction(0)
    for matching in _perfect_matchings(half_edges):
        if any(left[0] == right[0] for left, right in matching):
            continue
        contribution = Fraction(1)
        for left, right in matching:
            separation = coordinates[left[0]] - coordinates[right[0]]
            contribution *= Fraction(1, separation**2)
        total += contribution
    return total / 2 ** len(coordinates)


def _substitute(
    expression: sp.Expr,
    points: tuple[sp.Symbol, ...],
    coordinates: tuple[int, ...],
    central_charge: object,
) -> sp.Expr:
    substitutions = dict(zip(points, map(sp.Integer, coordinates)))
    substitutions[CENTRAL_CHARGE] = sp.sympify(central_charge)
    return sp.cancel(expression.subs(substitutions))


def test_vacuum_initial_conditions():
    assert virasoro_ward_correlator((), CENTRAL_CHARGE) == 1
    assert virasoro_ward_correlator(standard_points(1), CENTRAL_CHARGE) == 0


def test_two_point_function_symbolically():
    z1, z2 = standard_points(2)
    expected = CENTRAL_CHARGE / (2 * (z1 - z2) ** 4)
    assert sp.cancel(
        virasoro_ward_correlator((z1, z2), CENTRAL_CHARGE) - expected
    ) == 0


def test_three_point_function_symbolically():
    z1, z2, z3 = standard_points(3)
    expected = CENTRAL_CHARGE / (
        (z1 - z2) ** 2 * (z1 - z3) ** 2 * (z2 - z3) ** 2
    )
    assert sp.cancel(
        virasoro_ward_correlator((z1, z2, z3), CENTRAL_CHARGE) - expected
    ) == 0


def test_all_three_ward_contributions_at_four_points():
    points = standard_points(4)
    terms = ward_recursion_terms(points, CENTRAL_CHARGE)
    coordinates = (0, 1, 2, 3)

    assert _substitute(terms.central, points, coordinates, 1) == sp.Rational(
        21073, 82944
    )
    assert _substitute(
        terms.stress_exchange, points, coordinates, 1
    ) == sp.Rational(49, 72)
    assert _substitute(terms.derivative, points, coordinates, 1) == sp.Rational(
        -1, 2
    )
    assert sp.cancel(terms.total - virasoro_ward_correlator(points)) == 0


@pytest.mark.parametrize("arity", range(2, 7))
def test_exact_rational_values(arity: int):
    coordinates = tuple(range(arity))
    assert (
        evaluate_ward_correlator(coordinates, 1)
        == FULL_C_ONE_AT_CONSECUTIVE_POINTS[arity]
    )
    assert (
        evaluate_connected_correlator(coordinates, 1)
        == CONNECTED_C_ONE_AT_CONSECUTIVE_POINTS[arity]
    )


@pytest.mark.parametrize("arity", range(2, 7))
def test_free_boson_wick_oracle(arity: int):
    coordinates = tuple(range(arity))
    ward_value = evaluate_ward_correlator(coordinates, 1)
    wick_value = _free_boson_wick_value(coordinates)
    assert ward_value == sp.Rational(wick_value.numerator, wick_value.denominator)


@pytest.mark.parametrize("arity", range(2, 7))
def test_cycle_expansion_oracle_at_rational_c(arity: int):
    coordinates = tuple(index * index + 2 * index + 1 for index in range(arity))
    central_charge = sp.Rational(7, 5)
    assert evaluate_ward_correlator(
        coordinates, central_charge
    ) == evaluate_cycle_expansion(coordinates, central_charge)


@pytest.mark.parametrize("arity", range(2, 7))
def test_mobius_connected_correlator_matches_cycle_formula(arity: int):
    points = standard_points(arity)
    coordinates = tuple(range(arity))
    central_charge = sp.Rational(7, 5)
    mobius = _substitute(
        virasoro_connected_correlator(points),
        points,
        coordinates,
        central_charge,
    )
    cycles = _substitute(
        cycle_connected_correlator(points),
        points,
        coordinates,
        central_charge,
    )
    assert mobius == cycles


@pytest.mark.parametrize("arity", range(2, 7))
def test_permutation_symmetry(arity: int):
    coordinates = tuple(index * index + index + 1 for index in range(arity))
    central_charge = sp.Rational(11, 7)
    reference = evaluate_ward_correlator(coordinates, central_charge)
    for index in range(arity - 1):
        permuted = list(coordinates)
        permuted[index], permuted[index + 1] = (
            permuted[index + 1],
            permuted[index],
        )
        assert evaluate_ward_correlator(permuted, central_charge) == reference


@pytest.mark.parametrize("arity", range(2, 7))
def test_conformal_homogeneity(arity: int):
    coordinates = tuple(index * index + 2 * index + 1 for index in range(arity))
    central_charge = sp.Rational(5, 3)
    scale = sp.Integer(3)
    original = evaluate_ward_correlator(coordinates, central_charge)
    scaled = evaluate_ward_correlator(
        tuple(scale * coordinate for coordinate in coordinates),
        central_charge,
    )
    assert scaled == original / scale ** (2 * arity)


@pytest.mark.parametrize("arity", range(2, 7))
def test_translation_invariance(arity: int):
    coordinates = tuple(index * index + 2 * index + 1 for index in range(arity))
    translated = tuple(coordinate + 17 for coordinate in coordinates)
    central_charge = sp.Rational(5, 3)
    assert evaluate_ward_correlator(
        translated, central_charge
    ) == evaluate_ward_correlator(coordinates, central_charge)


def test_scalar_projection_obligation_names_the_missing_data():
    with pytest.raises(ResidueProjectionRequired) as error:
        require_residue_projection(6)
    message = str(error.value)
    assert "H_res(Vir_c; X)" in message
    assert "Arnold" in message
    assert "residue projection" in message
    assert "C_6^rel" in message
    assert "R_6^Ricc" in message
