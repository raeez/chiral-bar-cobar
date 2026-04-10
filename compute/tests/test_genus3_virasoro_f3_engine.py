"""Tests for compute/lib/genus3_virasoro_f3_engine.py."""

from fractions import Fraction

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.genus3_virasoro_f3_engine import (
    LAMBDA3_FP,
    UNIFORM_WEIGHT_TAG,
    genus3_stable_graphs,
    genus3_virasoro_f3,
    genus3_virasoro_f3_symbolic,
    genus3_virasoro_graph_contributions,
    is_smooth_genus3_graph,
    lambda3_fp,
    nonzero_graph_contributions,
    total_c_coefficient,
    total_kappa_coefficient,
    verify_genus3_virasoro_f3,
    virasoro_kappa,
    virasoro_r_matrix_data,
    virasoro_scalar_propagator,
)


def test_genus3_enumeration_is_42():
    # VERIFIED: [LT] Faber's genus-3 stable-graph census gives 42 strata; [DC] the live stable_graph_enumeration engine and existing genus-3 graph tests in this repo agree on 42.
    assert len(genus3_stable_graphs()) == 42


def test_only_one_graph_survives_scalar_lane():
    contributions = nonzero_graph_contributions()
    # VERIFIED: [DA] the scalar vacuum coefficient is linear in kappa on the UNIFORM-WEIGHT lane, so only one scalar source can survive; [CF] existing scalar-lane genus-3 engines in this repo isolate the smooth graph as the sole contributor.
    assert len(contributions) == 1
    assert is_smooth_genus3_graph(contributions[0].graph)


def test_boundary_graphs_vanish_on_scalar_lane():
    contributions = genus3_virasoro_graph_contributions()
    boundary_contributions = [
        contribution
        for contribution in contributions
        if not is_smooth_genus3_graph(contribution.graph)
    ]
    assert all(
        contribution.contribution_at_kappa(Fraction(7)) == 0
        for contribution in boundary_contributions
    )


def test_smooth_graph_contribution_matches_lambda3():
    smooth = nonzero_graph_contributions()[0]
    # VERIFIED: [LT] Faber-Pandharipande gives lambda_3^FP = 31/967680; [DC] Bernoulli evaluation (2^5-1)|B_6|/(2^5 6!) with B_6 = 1/42 gives the same value.
    expected_lambda3 = Fraction(31, 967680)
    # VERIFIED: [DC] kappa(Vir_c) = c/2, so the c-coefficient is lambda_3^FP / 2; [CF] the Virasoro scalar genus formula in the repo uses the same normalization.
    expected_c_coeff = Fraction(31, 1935360)
    assert smooth.kappa_coefficient == expected_lambda3
    assert smooth.c_coefficient == expected_c_coeff


def test_total_sum_matches_fraction_formula():
    # VERIFIED: [LT] lambda_3^FP = 31/967680; [DC] kappa(Vir_c) = c/2 implies F_3(Vir_c) = (c/2) * lambda_3^FP = 31c/1935360.
    expected_kappa_coeff = Fraction(31, 967680)
    # VERIFIED: [DC] (1/2) * 31/967680 = 31/1935360; [CF] the uniform-weight scalar-lane formula is linear in c through kappa = c/2.
    expected_c_coeff = Fraction(31, 1935360)
    assert total_kappa_coefficient() == expected_kappa_coeff
    assert total_c_coefficient() == expected_c_coeff
    assert genus3_virasoro_f3(Fraction(1)) == expected_c_coeff
    # VERIFIED: [DC] kappa(Vir_26) = 13, so F_3(Vir_26) = 13 * 31/967680; [LC] c = 26 is the Virasoro complementarity partner of c = 0.
    assert genus3_virasoro_f3(Fraction(26)) == Fraction(13 * 31, 967680)


def test_symbolic_formula_matches_expected():
    c = Symbol("c")
    # VERIFIED: [LT] Faber-Pandharipande gives the lambda_3 factor; [DC] substituting kappa = c/2 gives the exact symbolic coefficient 31/1935360.
    expected = Rational(31, 1935360) * c
    assert simplify(genus3_virasoro_f3_symbolic() - expected) == 0


def test_r_matrix_and_scalar_propagator_data():
    data = virasoro_r_matrix_data()
    assert data["full_formula"] == "(c/2)/z^3 + 2T/z"
    assert data["scalar_projection_formula"] == "(c/2)/z^3"
    # VERIFIED: [DC] kappa(Vir_2) = 1, so the scalar propagator 1/kappa equals 1; [CF] the scalar projection of the Virasoro r-matrix uses the central term only, hence P = 2/c.
    assert virasoro_scalar_propagator(Fraction(2)) == Fraction(1)
    with pytest.raises(ValueError):
        virasoro_scalar_propagator(Fraction(0))


def test_verification_summary_is_consistent():
    summary = verify_genus3_virasoro_f3()
    # VERIFIED: [LT] the genus-3 scalar coefficient is lambda_3^FP = 31/967680; [DC] the c-coefficient is half of that because kappa = c/2.
    assert summary["uniform_weight_tag"] == UNIFORM_WEIGHT_TAG
    assert summary["graph_count"] == 42
    assert summary["nonzero_graph_count"] == 1
    assert summary["lambda3_fp"] == LAMBDA3_FP == lambda3_fp()
    assert summary["match_lambda3"]
    assert summary["match_total"]
    # VERIFIED: [LC] kappa(Vir_0) = 0 forces F_3(Vir_0) = 0; [DC] 0 times any exact rational is 0.
    assert summary["c0_value"] == 0


def test_virasoro_kappa_formula():
    # VERIFIED: [LT] the true formula census gives kappa(Vir_c) = c/2; [CF] W_2 = Virasoro and the W_N formula kappa = c(H_N - 1) reduces to c/2 at N = 2.
    assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)
