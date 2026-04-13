import pytest
from sympy import Rational

from compute.lib.modular_bootstrap_shadow import (
    ising_model_data,
    lambda_fp,
    minimal_model_shadow_check,
    shadow_genus2_constraint,
    shadow_planted_forest_genus2,
    verify_S_squared,
    verify_S_symmetry,
    verify_S_unitarity,
    verlinde_fusion,
    verify_fusion_integrality,
    virasoro_shadow_data,
)


def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
    expected_lambda1 = Rational(1, 24)
    expected_lambda2 = Rational(7, 5760)
    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
    assert lambda_fp(1) == expected_lambda1
    assert lambda_fp(2) == expected_lambda2


def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
    vir13 = virasoro_shadow_data(Rational(13))
    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
    assert vir13["kappa"] == Rational(13, 2)
    assert vir13["S_4"] == Rational(10, 1131)
    assert vir13["Delta"] == Rational(40, 87)

    vir24 = virasoro_shadow_data(Rational(24))
    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
    assert vir24["kappa"] == Rational(12)
    assert vir24["S_4"] == Rational(5, 1704)
    assert vir24["Delta"] == Rational(20, 71)


def test_monster_genus2_constraint_matches_planted_forest_formula():
    kappa = Rational(12)
    cubic = Rational(2)
    expected_delta_pf = Rational(1, 3)
    expected_genus2 = Rational(167, 480)
    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2


def test_ising_modular_data_and_shadow_check_match_known_values():
    ising = ising_model_data()
    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
    assert ising["c"] == Rational(1, 2)
    assert ising["n_primaries"] == 3
    assert verify_S_squared(ising["S"])[0]
    assert verify_S_unitarity(ising["S"])[0]
    assert verify_S_symmetry(ising["S"])

    fusion = verlinde_fusion(ising["S"])
    assert verify_fusion_integrality(fusion)
    assert fusion[1, 1, 0] == pytest.approx(1.0)
    assert fusion[1, 1, 2] == pytest.approx(1.0)
    assert fusion[1, 2, 1] == pytest.approx(1.0)

    check = minimal_model_shadow_check(4, 3)
    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
    assert check["F_1"] == Rational(1, 96)
    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
