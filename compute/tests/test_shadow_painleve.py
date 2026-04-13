# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import pytest

from compute.lib.shadow_painleve import (
    classify_singularities,
    fuchsian_type,
    heisenberg_shadow_params,
    jmu_tau_from_connection,
    painleve_type,
    painleve_type_multichannel,
    schwarzian_potential_numeric,
    shadow_metric_coefficients,
    shadow_metric_discriminant,
    singularity_count,
    virasoro_shadow_params,
)


def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
    kappa, alpha, delta = 2, 3, 5
    expected_coeffs = (16, 72, 91)
    expected_discriminant = -640
    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant


def test_schwarzian_potential_numeric_matches_origin_value():
    value = schwarzian_potential_numeric(2, 3, 5, 0)
    expected = 5.0 / 8.0
    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
    assert value == pytest.approx(expected)


def test_delta_zero_classification_is_trivial():
    params = heisenberg_shadow_params(2)
    singularities = classify_singularities(*params)
    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
    assert singularities[0].type == "ordinary"
    assert not singularities[0].is_finite
    assert singularity_count(*params) == {
        "regular": 0,
        "irregular": 0,
        "ordinary": 1,
        "apparent": 0,
    }
    assert fuchsian_type(*params) == "trivial"
    assert painleve_type(*params) == "trivial"


def test_virasoro_shadow_params_match_self_dual_c13_values():
    kappa, alpha, delta = virasoro_shadow_params(13)
    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
    assert kappa == pytest.approx(6.5)
    assert alpha == pytest.approx(2.0)
    assert delta == pytest.approx(40.0 / 87.0)


def test_multichannel_and_tau_normalization_smoke_checks():
    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)
