from fractions import Fraction

from compute.lib.cohft_string_genus2_engine import (
    FrobeniusData,
    full_string_equation_verification_genus2,
    lambda_fp,
    string_equation_general_genus,
    verify_string_equation_genus2_se2,
)


def test_rank_one_frobenius_data_tracks_unit_presence():
    heisenberg = FrobeniusData.heisenberg(Fraction(2))
    virasoro = FrobeniusData.virasoro(Fraction(26))

    assert heisenberg.has_unit is False
    assert virasoro.has_unit is True
    assert virasoro.unit_coeff == Fraction(13, 2)


def test_genus2_string_equation_prediction_matches_faber_pandharipande():
    se2 = verify_string_equation_genus2_se2()
    assert lambda_fp(2) == Fraction(7, 5760)
    assert se2["prediction_per_kappa"] == Fraction(7, 2880)
    assert se2["passes"] is True


def test_full_genus2_check_and_general_genus_projection_formula():
    genus3 = string_equation_general_genus(3)
    result = full_string_equation_verification_genus2()

    assert result["all_pass"] is True
    assert genus3["se2_per_kappa"] == Fraction(31, 241920)
    assert genus3["se3_vanishes"] is True
