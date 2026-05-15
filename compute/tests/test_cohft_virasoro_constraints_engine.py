"""Tests for finite scalar shadow certificates and KW reference checks."""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.cohft_virasoro_constraints_engine import (
    descendant_cohft_data_certificate,
    finite_scalar_shadow_tau,
    kernel_constant_certificate,
    lambda_fp,
    lambda_g_integral,
    shadow_free_energy,
    shadow_cohft_virasoro_theorem,
    shadow_equation_classification,
    standard_hierarchy_constraint_status,
    stationary_primary_line_diagnostics,
    virasoro_string_equation,
    wk_intersection,
)


def test_smoke_lambda_fp_g1():
    """lambda_1^FP = 1/24."""
    assert lambda_fp(1) == Fraction(1, 24)


def test_lambda_fp_g2_and_g3():
    """Non-trivial: lambda_2^FP = 7/5760, lambda_3^FP = 31/967680."""
    assert lambda_fp(2) == Fraction(7, 5760)
    assert lambda_fp(3) == Fraction(31, 967680)


def test_lambda_fp_g4():
    """Fourth entry of FP sequence: 127/154828800."""
    assert lambda_fp(4) == Fraction(127, 154828800)


def test_lambda_g_integral_g1():
    """|B_2|/(2*2!) = (1/6)/4 = 1/24."""
    assert lambda_g_integral(1) == Fraction(1, 24)


def test_lambda_g_integral_g2():
    """|B_4|/(4*4!) = (1/30)/96 = 1/2880."""
    assert lambda_g_integral(2) == Fraction(1, 2880)


def test_lambda_fp_ratio_formula():
    """Check lambda_fp(g) / lambda_g_integral(g) = (2^{2g-1} - 1) * 2g / 2^{2g-1}."""
    for g in [1, 2, 3, 4]:
        ratio = lambda_fp(g) / lambda_g_integral(g)
        power = 2 ** (2 * g - 1)
        expected = Fraction(power - 1, power) * 2 * g
        assert ratio == expected


def test_string_axiom_at_g0_n3():
    """Virasoro string equation applied at (g=0,n=3) with trivial insertion tau_0^2."""
    # The string eq reduces (g,n+1,psi_1^0) to (g,n,...); we test that the
    # returned structure is well-formed (not raising) at a simple case.
    result = virasoro_string_equation(genus=0, insertions=(0, 0, 0))
    assert isinstance(result, dict)


def test_wk_base_case():
    """<tau_0^3>_{0,3} = 1 (string/3-pt function base case of WK)."""
    v = wk_intersection(0, (0, 0, 0))
    assert v == Fraction(1, 1)


def test_shadow_free_energy_linear_in_kappa_at_g1():
    """Shadow free energy at g=1 is lambda_1^FP * kappa = kappa/24."""
    f = shadow_free_energy(1, Fraction(2))  # kappa = 2
    assert f == Fraction(2, 24) == Fraction(1, 12)


def test_finite_scalar_tau_has_no_descendant_certificate():
    """The q-series identity is scalar and finite."""
    result = finite_scalar_shadow_tau(Fraction(3, 2), max_genus=3)
    assert result['ring'] == 'Q[kappa][[q]]/(q^4)'
    assert result['log_identity'] == 'log tau_shadow_scal^{<=G} = kappa log tau_KW^{<=G}'
    assert result['shadow_log_coefficients'][2] == Fraction(3, 2) * Fraction(7, 5760)
    assert result['scalar_lane_only']
    assert not result['constructs_descendant_virasoro_constraints']
    assert not result['constructs_full_tau_function']


def test_standard_hierarchy_status_rejects_arbitrary_kappa():
    """For kappa = 1/2 the standard nonlinear residual is exact."""
    status = standard_hierarchy_constraint_status(Fraction(1, 2))
    assert not status['standard_descendant_virasoro_constraints']
    assert not status['standard_kdv_hierarchy']
    assert status['kdv_residual_factor_kappa_1_minus_kappa'] == Fraction(1, 4)


def test_kw_case_is_the_descendant_virasoro_case():
    """Only kappa = 1 certifies the standard KW package."""
    status = standard_hierarchy_constraint_status(Fraction(1))
    assert status['standard_kw_descendant_tau']
    assert status['standard_descendant_virasoro_constraints']
    assert status['standard_kdv_hierarchy']
    assert status['kdv_residual_factor_kappa_1_minus_kappa'] == Fraction(0)


def test_zero_field_exception_is_not_kw_descendant_data():
    """kappa = 0 is only the trivial nonlinear-field exception."""
    status = standard_hierarchy_constraint_status(Fraction(0))
    assert status['trivial_zero_field_exception']
    assert status['standard_kdv_hierarchy']
    assert status['standard_hirota_equations']
    assert not status['standard_descendant_virasoro_constraints']
    assert not status['all_standard_constraints']


def test_shadow_theorem_classifies_kappa_half_as_scalar_only():
    """KW DVV checks may pass while the kappa-scaled scalar lane fails."""
    result = shadow_cohft_virasoro_theorem(Fraction(1, 2), max_g=2, max_n_vir=2)
    assert result['kw_reference_checks_pass']
    assert result['scalar_lane_pass']
    assert not result['standard_descendant_package_pass']
    assert not result['all_pass']


def test_stationary_primary_line_requires_descendant_data():
    """Stationary diagnostics do not construct the hierarchy."""
    result = stationary_primary_line_diagnostics()
    assert result['classes']['M']['depth'] == 'infinity'
    assert not result['constructs_full_hierarchy']
    assert result['requires_descendant_cohft_data']


def test_separately_supplied_descendant_cohft_data_is_explicit():
    """The scalar lane itself never supplies descendant classes."""
    absent = descendant_cohft_data_certificate(False)
    supplied = descendant_cohft_data_certificate(True)
    assert not absent['finite_scalar_lane_supplies_descendants']
    assert not absent['full_virasoro_constraints_available']
    assert supplied['full_virasoro_constraints_available']


def test_kernel_constants_and_object_firewalls_are_sourced():
    """Kernel constants and object separation use local source anchors."""
    cert = kernel_constant_certificate()
    kernels = cert['kernel_constants']
    assert kernels['affine_raw_trace']['formula'] == 'k*Omega_tr/z'
    assert kernels['affine_kz']['formula'] == 'Omega/((k+h^vee)z)'
    assert kernels['heisenberg']['formula'] == 'k/z'
    assert kernels['virasoro']['formula'] == '(c/2)/z^3 + 2*T/z'
    assert any('bar-cobar inversion' in item for item in cert['object_firewalls'])
    assert any('Hochschild/bulk' in item for item in cert['object_firewalls'])


def test_shadow_equation_classification_records_failure_factor():
    """Classification separates scalar identity, KW case, and zero field."""
    result = shadow_equation_classification(Fraction(2, 3), max_genus=3)
    assert result['satisfies']['finite_scalar_coefficient_identity']
    assert not result['satisfies']['standard_descendant_virasoro_constraints']
    assert result['exceptions']['kdv_residual_factor'] == Fraction(2, 9)
