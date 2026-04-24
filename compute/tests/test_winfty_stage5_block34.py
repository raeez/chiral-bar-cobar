"""Exact tests for prop:winfty-stage5-block-34."""

from fractions import Fraction

import pytest

from compute.lib.galois_hierarchy_general_engine import g_squared_at
from compute.lib.galois_w4_w5_engine import g345_sq_w5
from compute.lib.w5_full_ope_delta_f2_engine import g345_squared_exact
from compute.lib.w_infinity_dual_candidate import (
    stage5_visible_pairing_normal_form_report,
)
from compute.lib.winfty_stage5_block34 import (
    BLOCK34_CHANNEL,
    SignedQuadraticCoefficient,
    block34_defect,
    ds_block34_coefficient,
    g345_squared,
    residue_block34_coefficient,
    visible_normal_form_values,
    w3_w4_w5_three_point,
    w5_metric,
)


@pytest.mark.parametrize("c", [Fraction(10), Fraction(24), Fraction(26), Fraction(123)])
def test_g345_formula_matches_existing_w5_engines(c):
    """The block-34 engine uses the same bootstrap square as the W5 engines."""

    expected = g345_squared_exact(c)
    assert g345_squared(c) == expected
    assert g345_squared(c) == g345_sq_w5(c)
    assert g345_squared(c) == g_squared_at(3, 4, 5, c)


@pytest.mark.parametrize("c", [Fraction(10), Fraction(24), Fraction(26), Fraction(123)])
def test_residue_metric_contraction_returns_g345(c):
    """<W3 W4 W5>=(c/5)g345 and eta^55=5/c imply C^res=g345."""

    g345 = ds_block34_coefficient(c)
    tensor = w3_w4_w5_three_point(c, g345)
    eta55 = w5_metric(5, c)
    assert tensor.square == eta55 * eta55 * g345.square
    assert residue_block34_coefficient(c).same_as(g345)


@pytest.mark.parametrize("c", [Fraction(10), Fraction(24), Fraction(26), Fraction(123)])
def test_block34_defect_vanishes_with_common_generator_sign(c):
    """The exact equality holds after the W5 sign convention is identified."""

    report = block34_defect(c)
    assert report["channel"] == BLOCK34_CHANNEL
    assert report["same_sign_convention"] is True
    assert report["defect_zero"] is True
    assert report["residue_coefficient"].same_as(report["ds_coefficient"])


def test_block34_detects_opposite_generator_sign():
    """Independent W5 sign choices are the only local sign obstruction."""

    report = block34_defect(Fraction(10), residue_sign=1, ds_sign=-1)
    assert report["same_sign_convention"] is False
    assert report["defect_zero"] is False
    assert report["residue_coefficient"].same_as(
        report["ds_coefficient"].negated()
    )


def test_degenerate_g345_zero_point_has_zero_defect():
    """At c=1/2 the factor 2c-1 kills g345 on both sides."""

    report = block34_defect(Fraction(1, 2))
    assert report["g345_squared"] == 0
    assert report["residue_coefficient"] == SignedQuadraticCoefficient(0, Fraction(0))
    assert report["ds_coefficient"] == SignedQuadraticCoefficient(0, Fraction(0))
    assert report["defect_zero"] is True


def test_visible_normal_form_ratios_match_existing_stage5_packet():
    """The direct g345 value is consistent with the existing stage-5 ratios."""

    c = Fraction(10)
    values = visible_normal_form_values(c)
    normal_form = stage5_visible_pairing_normal_form_report()["channel_normal_form"]

    block34 = values[(3, 4, 5, 2)]
    representative = values[(3, 5, 4, 4)]
    target3 = values[(4, 5, 3, 6)]

    assert block34.square == representative.square * Fraction(25, 16)
    assert block34.sign == -representative.sign
    assert normal_form[(3, 4, 5, 2)]["ratio_to_A5"] == Fraction(-5, 4)

    assert target3.square == representative.square * Fraction(9, 16)
    assert target3.sign == -representative.sign
    assert normal_form[(4, 5, 3, 6)]["ratio_to_A5"] == Fraction(-3, 4)
