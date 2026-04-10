from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib.modular_shadow_zeta_engine import (
    analyze_growth,
    affine_km_kappa,
    affine_sl2_kappa,
    borel_transform_analysis,
    borel_transform_coefficients,
    evaluate_borel_transform,
    family_zeta_formulas,
    free_energy,
    lambda_fp,
    lambda_fp_eta_numeric,
    lambda_fp_from_sine_series,
    lambda_fp_table,
    pade_evaluate,
    pade_from_series,
    partial_shadow_zeta,
    standard_family_partial_sums,
    virasoro_kappa,
    heisenberg_kappa,
)


def test_lambda_fp_low_genus_exact_values():
    expected_g1 = Fraction(1, 24)  # VERIFIED [DC] Bernoulli/Faber-Pandharipande formula; [LT] compute/lib/genus_expansion.py and chapters/examples/genus_expansions.tex.
    expected_g2 = Fraction(7, 5760)  # VERIFIED [DC] (2^3-1)/2^3 * |B_4| / 4!; [LT] multiple repo tests explicitly mark 1/1152 as the wrong normalization for this lane.
    expected_g3 = Fraction(31, 967680)  # VERIFIED [DC] (2^5-1)/2^5 * |B_6| / 6!; [LT] chapters/examples/genus_expansions.tex and compute/lib/genus_expansion.py.
    assert lambda_fp(1) == expected_g1
    assert lambda_fp(2) == expected_g2
    assert lambda_fp(3) == expected_g3


def test_lambda_fp_exact_methods_agree_through_genus_ten():
    for genus, value in lambda_fp_table(10).items():
        assert lambda_fp_from_sine_series(genus) == value


def test_lambda_fp_eta_numeric_matches_exact_values():
    # VERIFIED [DC] eta(2g) identity from Bernoulli/zeta formula; [NE] direct alternating-series evaluation.
    assert math.isclose(lambda_fp_eta_numeric(1, terms=5000), float(Fraction(1, 24)), rel_tol=0.0, abs_tol=1e-10)
    assert math.isclose(lambda_fp_eta_numeric(2, terms=5000), float(Fraction(7, 5760)), rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(lambda_fp_eta_numeric(3, terms=5000), float(Fraction(31, 967680)), rel_tol=0.0, abs_tol=1e-12)


def test_f1_sanity_checks_for_standard_families():
    heis_kappa = Fraction(1)  # VERIFIED [DC] kappa(H_k)=k at k=1; [LT] CLAUDE C1 and compute/lib/genus_expansion.py.
    vir_kappa = Fraction(25, 2)  # VERIFIED [DC] kappa(Vir_c)=c/2 at c=25; [LT] CLAUDE C2 and compute/lib/genus_expansion.py.
    sl2_kappa = Fraction(9, 4)  # VERIFIED [DC] dim(sl_2)*(k+h^v)/(2h^v)=3*(1+2)/4; [LT] CLAUDE C3 and compute/lib/genus_expansion.py.
    expected_heis_f1 = Fraction(1, 24)  # VERIFIED [DC] F_1=kappa/24 with kappa=1; [CF] Heisenberg specialization of the universal formula.
    expected_vir_f1 = Fraction(25, 48)  # VERIFIED [DC] F_1=(25/2)/24; [CF] Virasoro c=25 specialization of Theorem D.
    expected_sl2_f1 = Fraction(3, 32)  # VERIFIED [DC] F_1=(9/4)/24; [CF] affine sl_2 level-1 specialization of the KM census formula.
    assert heisenberg_kappa(Fraction(1)) == heis_kappa
    assert virasoro_kappa(Fraction(25)) == vir_kappa
    assert affine_km_kappa(level=Fraction(1), dim_g=3, h_dual=2) == sl2_kappa
    assert affine_sl2_kappa(Fraction(1)) == sl2_kappa
    assert free_energy(1, heis_kappa) == expected_heis_f1
    assert free_energy(1, vir_kappa) == expected_vir_f1
    assert free_energy(1, sl2_kappa) == expected_sl2_f1


def test_partial_shadow_zeta_exact_low_genus_values():
    expected = Fraction(25, 48)  # VERIFIED [DC] Z_Vir^{<=1}(0)=F_1(Vir_25); [CF] F_1=(25/2)/24.
    assert partial_shadow_zeta(Fraction(25, 2), s=0, max_genus=1) == expected

    exact_heis = Fraction(1, 24) + Fraction(7, 5760) + Fraction(31, 967680)
    # VERIFIED [DC] sum of exact lambda_1, lambda_2, lambda_3; [CF] H_1 has kappa=1 so F_g=lambda_g.
    assert partial_shadow_zeta(Fraction(1), s=0, max_genus=3) == exact_heis


def test_standard_family_partial_sums_use_correct_prefactors():
    partials = standard_family_partial_sums(s=0, max_genus=1)
    expected_heis = Fraction(1, 24)  # VERIFIED [DC] kappa(H_1)=1 and lambda_1=1/24; [CF] genus-1 Heisenberg specialization.
    expected_vir = Fraction(25, 48)  # VERIFIED [DC] kappa(Vir_25)=25/2 and lambda_1=1/24; [CF] genus-1 Virasoro specialization.
    expected_km = Fraction(3, 32)  # VERIFIED [DC] kappa(sl_2,1)=9/4 and lambda_1=1/24; [CF] genus-1 affine KM specialization.
    assert partials["Heis_k"] == expected_heis
    assert partials["Vir_c"] == expected_vir
    assert partials["KM"] == expected_km


def test_family_formula_strings_match_canonical_kappa_surface():
    formulas = family_zeta_formulas()
    assert formulas["Heis_k"].startswith("Z_H_k(s) = k *")
    assert formulas["Vir_c"].startswith("Z_Vir_c(s) = (c/2) *")
    assert "dim(g)*(k+h^v)/(2*h^v)" in formulas["KM"]


def test_growth_analysis_concludes_entire_dirichlet_series():
    analysis = analyze_growth(max_genus=10)
    assert analysis.growth_kind == "geometric_decay"
    assert math.isinf(analysis.abscissa_of_convergence) and analysis.abscissa_of_convergence < 0
    assert math.isinf(analysis.abscissa_of_absolute_convergence) and analysis.abscissa_of_absolute_convergence < 0
    assert analysis.meromorphic_continuation == "entire"
    assert analysis.pole_structure == tuple()
    assert analysis.ratio_table[-1] < 0.026
    assert math.isclose(analysis.ratio_limit, 1.0 / ((2.0 * math.pi) ** 2), rel_tol=0.0, abs_tol=1e-15)
    assert analysis.scaled_asymptotic_values[-1] > 0.99


def test_borel_transform_coefficients_are_exact():
    kappa = Fraction(25, 2)  # VERIFIED [DC] kappa(Vir_25)=25/2; [LT] census formula kappa(Vir_c)=c/2.
    coefficients = borel_transform_coefficients(kappa, max_genus=3)
    expected_c0 = Fraction(25, 48)  # VERIFIED [DC] F_1 / Gamma(1) = 25/48; [CF] genus-1 Virasoro sanity check.
    expected_c1 = Fraction(35, 2304)  # VERIFIED [DC] F_2 / Gamma(2) = (25/2)*(7/5760); [CF] gamma(2)=1.
    expected_c2 = Fraction(155, 387072)  # VERIFIED [DC] F_3 / Gamma(3) = ((25/2)*(31/967680))/2; [CF] gamma(3)=2.
    assert coefficients == (expected_c0, expected_c1, expected_c2)


def test_borel_transform_evaluation_at_zero_is_f1():
    expected = Fraction(25, 48)  # VERIFIED [DC] B(0)=F_1/Gamma(1); [CF] Virasoro c=25 genus-1 specialization.
    value = evaluate_borel_transform(Fraction(25, 2), t=0.0, max_genus=10)
    assert value == complex(expected)


def test_pade_construction_matches_geometric_series():
    coefficients = [1.0] * 3
    numerator, denominator = pade_from_series(coefficients, 1, 1)
    assert pytest.approx(pade_evaluate(numerator, denominator, 0.5), rel=0.0, abs=1e-12) == 2.0


def test_borel_pade_analysis_finds_no_stable_poles_for_entire_series():
    analysis = borel_transform_analysis(Fraction(25, 2), max_genus=10)
    assert analysis.entire is True
    assert analysis.stable_poles == tuple()
    assert analysis.reports
