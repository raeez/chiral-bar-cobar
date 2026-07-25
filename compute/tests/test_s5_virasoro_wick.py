r"""Virasoro algebra checks retained beside the Ward correlator engine."""

from __future__ import annotations

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.s5_virasoro_wick import (
    ResidueProjectionRequired,
    bpz_ope_coefficients,
    bpz_three_point_function,
    g5_connected_ward_correlator,
    g6_connected_ward_correlator,
    lambda_channel_combinatorial_weight,
    s3_from_three_point_arnold_residue,
    s5_times_level5_gram_determinant,
    s5_via_lambda_channel,
    s5_virasoro_closed_form,
    s5_virasoro_recursion,
    s5_virasoro_wick,
    s5_weighted_riccati_candidate,
    verify_lambda_norm_symbolic,
    virasoro_level4_gram_determinant,
    virasoro_level4_gram_matrix,
    virasoro_level4_gram_matrix_from_commutators,
    virasoro_level5_gram_determinant,
    virasoro_level5_gram_matrix,
    virasoro_vacuum_expectation,
    zamolodchikov_lambda_norm,
)
from compute.lib.virasoro_ward_correlators import standard_points


@pytest.mark.parametrize(
    "central_charge",
    [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(24)],
)
def test_singular_ope_coefficients(central_charge: Fraction):
    coefficients = bpz_ope_coefficients(central_charge)
    assert coefficients == {
        4: central_charge / 2,
        2: Fraction(2),
        1: Fraction(1),
    }


def test_level_four_gram_matrix_and_schur_complement():
    c = sp.Symbol("c")
    gram = virasoro_level4_gram_matrix(c)
    assert gram == sp.Matrix(
        [[5 * c, 3 * c], [3 * c, c * (c + 8) / 2]]
    )
    assert sp.factor(virasoro_level4_gram_determinant(c)) == (
        c**2 * (5 * c + 22) / 2
    )
    determinant, schur = verify_lambda_norm_symbolic()
    assert sp.factor(determinant - c**2 * (5 * c + 22) / 2) == 0
    assert sp.factor(schur - c * (5 * c + 22) / 10) == 0


@pytest.mark.parametrize(
    "central_charge",
    [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(24)],
)
def test_lambda_norm_exact(central_charge: Fraction):
    expected = central_charge * (5 * central_charge + 22) / 10
    assert zamolodchikov_lambda_norm(central_charge) == expected


def test_three_point_function_is_generated_by_ward_recursion():
    c = sp.Symbol("c")
    z1, z2, z3 = standard_points(3)
    expected = c / (
        (z1 - z2) ** 2 * (z1 - z3) ** 2 * (z2 - z3) ** 2
    )
    assert sp.cancel(bpz_three_point_function() - expected) == 0


def test_connected_five_and_six_point_values():
    points5 = standard_points(5)
    value5 = sp.cancel(
        g5_connected_ward_correlator(1).subs(dict(zip(points5, range(5))))
    )
    assert value5 == sp.Rational(775, 5184)

    points6 = standard_points(6)
    value6 = sp.cancel(
        g6_connected_ward_correlator(1).subs(dict(zip(points6, range(6))))
    )
    assert value6 == sp.Rational(49705, 373248)


@pytest.mark.parametrize(
    "function, arguments",
    [
        (s3_from_three_point_arnold_residue, (Fraction(1),)),
        (lambda_channel_combinatorial_weight, ()),
        (s5_via_lambda_channel, (Fraction(1),)),
        (s5_virasoro_wick, (Fraction(1),)),
    ],
)
def test_scalar_extractions_request_residue_data(function, arguments):
    with pytest.raises(ResidueProjectionRequired) as error:
        function(*arguments)
    assert "residue projection" in str(error.value)


@pytest.mark.parametrize(
    "central_charge",
    [
        Fraction(1, 2),
        Fraction(7, 10),
        Fraction(4, 5),
        Fraction(1),
        Fraction(2),
        Fraction(24),
    ],
)
def test_weighted_riccati_candidate_matches_its_recurrence(
    central_charge: Fraction,
):
    candidate = s5_weighted_riccati_candidate(central_charge)
    assert s5_virasoro_recursion(central_charge) == candidate
    assert s5_virasoro_closed_form(central_charge) == candidate


def test_weighted_riccati_pole_at_the_level_four_null_locus():
    with pytest.raises(ZeroDivisionError):
        s5_weighted_riccati_candidate(Fraction(-22, 5))


def test_vacuum_expectation_engine_elementary_values():
    c = sp.Symbol("c")
    # <0|L_2 L_{-2}|0> = c/2, <0|L_3 L_{-3}|0> = 2c, <0|L_5 L_{-5}|0> = 10c
    assert sp.simplify(virasoro_vacuum_expectation((2, -2), c) - c / 2) == 0
    assert sp.simplify(virasoro_vacuum_expectation((3, -3), c) - 2 * c) == 0
    assert sp.simplify(virasoro_vacuum_expectation((5, -5), c) - 10 * c) == 0
    # annihilation on the ket and the bra
    assert virasoro_vacuum_expectation((-2, 2), c) == 0
    assert virasoro_vacuum_expectation((0,), c) == 0


def test_level_four_gram_matrix_recomputed_from_commutators():
    c = sp.Symbol("c")
    engine = virasoro_level4_gram_matrix_from_commutators(c)
    closed = virasoro_level4_gram_matrix(c)
    assert sp.simplify(engine - closed) == sp.zeros(2, 2)


def test_level_five_gram_matrix_from_commutators():
    c = sp.Symbol("c")
    gram = virasoro_level5_gram_matrix(c)
    expected = sp.Matrix([[10 * c, 4 * c], [4 * c, c * (c + 6)]])
    assert sp.simplify(gram - expected) == sp.zeros(2, 2)
    assert sp.factor(
        virasoro_level5_gram_determinant(c) - 2 * c**2 * (5 * c + 22)
    ) == 0


@pytest.mark.parametrize(
    "central_charge",
    [
        Fraction(1, 2),
        Fraction(7, 10),
        Fraction(1),
        Fraction(2),
        Fraction(24),
        Fraction(-218, 45),
    ],
)
def test_s5_inverse_gram_shape(central_charge: Fraction):
    # S_5^Ricc * det G_5 = -96: the level-five analogue of the level-four
    # identity S_4 = 1/<Lambda|Lambda>.  A shape check, not a derivation.
    assert s5_times_level5_gram_determinant(central_charge) == Fraction(-96)
