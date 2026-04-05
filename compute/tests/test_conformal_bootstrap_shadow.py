"""Tests for conformal bootstrap from shadow obstruction tower constraints.

Covers all seven components of the shadow-augmented conformal bootstrap:
  1. Ising modular bootstrap with shadow (kappa=1/4, F_1=1/96)
  2. Crossing symmetry + shadow obstruction tower constraints
  3. Multi-genus shadow bootstrap tightening (c=1)
  4. Cardy formula corrections from shadow obstruction tower
  5. Hellerman bound with shadow augmentation
  6. Sphere packing consistency (E8 c=8, Leech c=24)
  7. OPE coefficient bounds for Ising

60+ tests, all using exact arithmetic where possible.

AP1: kappa(Vir_c) = c/2 (Virasoro formula, not KM).
AP15: genus-1 propagator is E_2* (quasi-modular).
AP24: kappa + kappa' = 13 for Virasoro (NOT zero).
"""

from __future__ import annotations

import math
import sys

import numpy as np
import pytest
from sympy import Rational, N as Neval

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from conformal_bootstrap_shadow import (
    # Shadow primitives
    kappa_virasoro,
    lambda_fp,
    F_g_shadow,
    Q_contact_virasoro,
    shadow_planted_forest_genus2,
    virasoro_shadow_data,
    # 1. Ising modular bootstrap
    ising_partition_function_q_expansion,
    ising_S_matrix,
    ising_T_matrix,
    ising_modular_relations,
    ising_verlinde_fusion,
    ising_shadow_spectrum,
    # 2. Crossing + shadow
    conformal_block_scalar_approx,
    crossing_constraint_functional,
    shadow_crossing_bound,
    gap_vs_c_allowed_region,
    # 3. Multi-genus
    genus_g_shadow_constraint,
    multi_genus_shadow_bounds,
    shadow_bootstrap_c1_multigenus,
    # 4. Cardy
    cardy_leading,
    cardy_subleading_coefficients,
    cardy_corrected,
    cardy_shadow_comparison,
    # 5. Hellerman
    hellerman_bound_standard,
    hellerman_bound_shadow_augmented,
    hellerman_shadow_comparison,
    # 6. Sphere packing
    e8_lattice_shadow_data,
    leech_lattice_shadow_data,
    sphere_packing_shadow_consistency,
    # 7. OPE bounds
    ising_ope_coefficients_exact,
    ising_ope_shadow_constraint,
    ope_shadow_allowed_region,
    # 8. Master
    full_shadow_bootstrap_analysis,
)


# ============================================================================
# 1. Shadow obstruction tower primitives
# ============================================================================

class TestShadowPrimitives:
    """Verify exact shadow obstruction tower data."""

    def test_kappa_virasoro_half(self):
        """kappa(Vir_{1/2}) = 1/4."""
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)

    def test_kappa_virasoro_integer(self):
        """kappa(Vir_c) = c/2 for integer c."""
        for c in [1, 2, 8, 24, 26]:
            assert kappa_virasoro(c) == Rational(c, 2)

    def test_kappa_virasoro_float(self):
        """kappa for float input."""
        assert abs(kappa_virasoro(1.0) - 0.5) < 1e-15

    def test_lambda_fp_genus1(self):
        """lambda_1 = 1/24 (Bernoulli B_2 = 1/6)."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_fp_invalid(self):
        """lambda_fp raises for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_F_g_genus1_virasoro(self):
        """F_1(Vir_c) = c/48."""
        c = Rational(1, 2)
        assert F_g_shadow(kappa_virasoro(c), 1) == c / 48

    def test_Q_contact_ising(self):
        """Q^contact(Vir_{1/2}) = 10/[(1/2)(49/2)] = 40/49."""
        assert Q_contact_virasoro(Rational(1, 2)) == Rational(40, 49)

    def test_Q_contact_c26(self):
        """Q^contact(Vir_26) = 10/(26*152) = 5/1976."""
        assert Q_contact_virasoro(26) == Rational(10, 26 * 152)

    def test_planted_forest_genus2_heisenberg(self):
        """delta_pf^{(2,0)} = 0 for Heisenberg (S_3 = 0, kappa = k)."""
        assert shadow_planted_forest_genus2(1.0, 0.0) == 0.0

    def test_planted_forest_genus2_virasoro(self):
        """delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48 for Virasoro."""
        kappa = Rational(1, 4)
        S_3 = Rational(2)
        expected = S_3 * (10 * S_3 - kappa) / 48
        assert shadow_planted_forest_genus2(kappa, S_3) == expected

    def test_virasoro_shadow_data_ising(self):
        """Full shadow data for c=1/2."""
        data = virasoro_shadow_data(Rational(1, 2))
        assert data['c'] == Rational(1, 2)
        assert data['kappa'] == Rational(1, 4)
        assert data['S_3'] == Rational(2)
        assert data['shadow_class'] == 'M'


# ============================================================================
# 2. Ising modular bootstrap with shadow
# ============================================================================

class TestIsingModularBootstrap:
    """Ising model (c=1/2) modular bootstrap + shadow."""

    def test_ising_central_charge(self):
        data = ising_partition_function_q_expansion()
        assert data['c'] == Rational(1, 2)

    def test_ising_kappa(self):
        data = ising_partition_function_q_expansion()
        assert data['kappa'] == Rational(1, 4)

    def test_ising_F1(self):
        """F_1 = kappa/24 = 1/96."""
        data = ising_partition_function_q_expansion()
        assert data['F_1'] == Rational(1, 96)

    def test_ising_three_primaries(self):
        data = ising_partition_function_q_expansion()
        assert data['n_primaries'] == 3

    def test_ising_identity_weight(self):
        data = ising_partition_function_q_expansion()
        assert data['primaries']['identity']['h'] == 0

    def test_ising_sigma_weight(self):
        data = ising_partition_function_q_expansion()
        assert data['primaries']['sigma']['h'] == Rational(1, 16)

    def test_ising_epsilon_weight(self):
        data = ising_partition_function_q_expansion()
        assert data['primaries']['epsilon']['h'] == Rational(1, 2)

    def test_ising_diagonal_invariant(self):
        data = ising_partition_function_q_expansion()
        assert data['diagonal'] is True

    def test_ising_S_matrix_shape(self):
        S = ising_S_matrix()
        assert S.shape == (3, 3)

    def test_ising_S_squared_is_identity(self):
        """S^2 = C = I for Ising (all self-conjugate)."""
        S = ising_S_matrix()
        S2 = S @ S
        assert np.allclose(S2, np.eye(3), atol=1e-10)

    def test_ising_ST_cubed_is_identity(self):
        """(ST)^3 = I."""
        S = ising_S_matrix()
        T = ising_T_matrix()
        ST = S @ T
        ST3 = ST @ ST @ ST
        assert np.allclose(ST3, np.eye(3), atol=1e-10)

    def test_ising_S_unitary(self):
        """S S^dag = I."""
        S = ising_S_matrix()
        assert np.allclose(S @ S.T, np.eye(3), atol=1e-10)

    def test_ising_S_symmetric(self):
        """S = S^T."""
        S = ising_S_matrix()
        assert np.allclose(S, S.T, atol=1e-10)

    def test_ising_modular_relations_all_pass(self):
        rels = ising_modular_relations()
        assert rels['S_squared_is_identity']
        assert rels['ST_cubed_is_identity']
        assert rels['S_unitary']
        assert rels['S_symmetric']

    def test_ising_verlinde_fusion_integrality(self):
        """Verlinde fusion coefficients are non-negative integers."""
        N = ising_verlinde_fusion()
        rounded = np.round(N)
        assert np.allclose(N, rounded, atol=1e-8)
        assert np.all(rounded >= -1e-8)

    def test_ising_sigma_sigma_fusion(self):
        """sigma x sigma = 1 + epsilon."""
        N = ising_verlinde_fusion()
        # sigma = index 1, identity = 0, epsilon = 2
        assert abs(N[1, 1, 0] - 1.0) < 1e-8  # sigma x sigma -> 1
        assert abs(N[1, 1, 2] - 1.0) < 1e-8  # sigma x sigma -> epsilon

    def test_ising_epsilon_epsilon_fusion(self):
        """epsilon x epsilon = 1."""
        N = ising_verlinde_fusion()
        assert abs(N[2, 2, 0] - 1.0) < 1e-8

    def test_ising_shadow_spectrum_consistency(self):
        """Shadow data consistent with known spectrum."""
        spec = ising_shadow_spectrum()
        assert spec['shadow_consistent']
        assert spec['Delta_gap'] == Rational(1, 16)


# ============================================================================
# 3. Crossing symmetry + shadow
# ============================================================================

class TestCrossingShadow:
    """Crossing symmetry augmented by shadow obstruction tower."""

    def test_conformal_block_positive_for_positive_z(self):
        """Conformal block is positive for z in (0,1)."""
        val = conformal_block_scalar_approx(0.5, 2.0, 0.3)
        assert val > 0

    def test_conformal_block_zero_at_boundary(self):
        """Block vanishes at z=0 and z=1."""
        assert conformal_block_scalar_approx(0.5, 2.0, 0.0) == 0.0
        assert conformal_block_scalar_approx(0.5, 2.0, 1.0) == 0.0

    def test_crossing_functional_finite(self):
        """Crossing constraint evaluates to finite value."""
        val = crossing_constraint_functional(1.0, 0.5, z=0.5)
        assert np.isfinite(val)

    def test_shadow_crossing_bound_tighter(self):
        """Shadow-augmented bound is tighter than crossing alone."""
        result = shadow_crossing_bound(10.0, 5.0, Q_contact_virasoro(10.0))
        # The shadow_bound should be less than or equal to crossing_bound
        assert result['shadow_bound'] <= result['crossing_bound']

    def test_shadow_crossing_bound_positive(self):
        """The shadow-augmented bound is still positive."""
        result = shadow_crossing_bound(10.0, 5.0, float(Q_contact_virasoro(10.0)))
        assert result['shadow_bound'] > 0

    def test_gap_vs_c_region_shape(self):
        """Gap vs c region has correct structure."""
        region = gap_vs_c_allowed_region(n_points=10)
        assert len(region['c_values']) == 10
        assert len(region['crossing_upper']) == 10
        assert len(region['shadow_upper']) == 10

    def test_shadow_upper_below_crossing(self):
        """Shadow upper bound <= crossing upper bound at each c."""
        region = gap_vs_c_allowed_region(c_values=[5.0, 10.0, 20.0, 50.0])
        for s, c_val in zip(region['shadow_upper'], region['crossing_upper']):
            assert s <= c_val + 1e-10  # shadow is tighter or equal


# ============================================================================
# 4. Multi-genus shadow bootstrap
# ============================================================================

class TestMultiGenusBootstrap:
    """Shadow bootstrap tightening with increasing genus."""

    def test_genus_constraint_positive(self):
        """F_g > 0 for c > 0."""
        for g in [1, 2, 3]:
            assert genus_g_shadow_constraint(1.0, g) > 0

    def test_genus_constraint_bernoulli_decay(self):
        """|F_g| decays with genus (Bernoulli decay)."""
        F1 = genus_g_shadow_constraint(1.0, 1)
        F2 = genus_g_shadow_constraint(1.0, 2)
        F3 = genus_g_shadow_constraint(1.0, 3)
        assert abs(F1) > abs(F2) > abs(F3)

    def test_multi_genus_bounds_tighten(self):
        """Bounds tighten with each additional genus."""
        result = multi_genus_shadow_bounds(10.0, max_genus=3)
        assert result['bounds_tighten']

    def test_multi_genus_c1_gap_within_bounds(self):
        """c=1 actual gap within all multi-genus bounds."""
        result = shadow_bootstrap_c1_multigenus()
        assert result['gap_within_bound_g1']
        assert result['gap_within_bound_g2']
        assert result['gap_within_bound_g3']

    def test_multi_genus_c1_actual_gap(self):
        """c=1 free boson gap = 1/2."""
        result = shadow_bootstrap_c1_multigenus()
        assert result['actual_gap'] == 0.5

    def test_genus2_planted_forest_nonzero(self):
        """Planted-forest correction nonzero for Virasoro."""
        result = multi_genus_shadow_bounds(10.0, max_genus=3)
        assert result['delta_pf_genus2'] != 0.0

    def test_cumulative_info_increases(self):
        """Cumulative information increases with genus."""
        result = multi_genus_shadow_bounds(10.0, max_genus=3)
        assert result['cumulative_info'] > result['info_1']

    def test_F1_exact_c1(self):
        """F_1 = 1/48 at c=1."""
        result = multi_genus_shadow_bounds(1.0)
        assert abs(result['F_1'] - 1.0 / 48.0) < 1e-15


# ============================================================================
# 5. Cardy formula corrections
# ============================================================================

class TestCardyCorrections:
    """Cardy formula with shadow-derived subleading corrections."""

    def test_cardy_leading_positive(self):
        """Leading Cardy density is positive for Delta > 0, c > 0."""
        assert cardy_leading(1.0, 10.0) > 0

    def test_cardy_leading_grows_with_Delta(self):
        """Cardy density grows exponentially with Delta."""
        rho1 = cardy_leading(1.0, 10.0)
        rho2 = cardy_leading(1.0, 20.0)
        assert rho2 > rho1

    def test_cardy_leading_grows_with_c(self):
        """Cardy density grows with central charge."""
        rho1 = cardy_leading(1.0, 10.0)
        rho2 = cardy_leading(2.0, 10.0)
        assert rho2 > rho1

    def test_cardy_leading_zero_for_nonpositive(self):
        """Cardy density is zero for Delta <= 0 or c <= 0."""
        assert cardy_leading(1.0, 0.0) == 0.0
        assert cardy_leading(0.0, 10.0) == 0.0
        assert cardy_leading(-1.0, 10.0) == 0.0

    def test_cardy_c1_coefficient(self):
        """c_1 is nonzero for c != 1 (corrections nontrivial)."""
        coeffs = cardy_subleading_coefficients(10.0)
        assert abs(coeffs['c1']) > 0

    def test_cardy_c1_vanishes_at_c1(self):
        """c_1 = 0 at c = 1 (by the (c-1) factor)."""
        coeffs = cardy_subleading_coefficients(1.0)
        assert abs(coeffs['c1']) < 1e-10

    def test_cardy_c2_finite(self):
        """c_2 is finite for c > 0."""
        coeffs = cardy_subleading_coefficients(10.0)
        assert np.isfinite(coeffs['c2'])

    def test_cardy_corrected_close_to_leading_at_large_Delta(self):
        """Corrections are small at large Delta."""
        c = 10.0
        Delta = 1000.0
        rho_leading = cardy_leading(c, Delta) * Delta ** (-0.75)
        rho_corrected = cardy_corrected(c, Delta, n_corrections=2)
        # The relative correction should be small
        if rho_leading > 0:
            rel = abs(rho_corrected - rho_leading) / rho_leading
            assert rel < 0.1  # less than 10% correction at Delta = 1000

    def test_cardy_comparison_corrections_decrease(self):
        """Relative corrections decrease with increasing Delta."""
        result = cardy_shadow_comparison(10.0)
        assert result['corrections_decrease_with_Delta']

    def test_cardy_coefficients_kappa(self):
        """Cardy coefficients store correct kappa."""
        coeffs = cardy_subleading_coefficients(10.0)
        assert abs(coeffs['kappa'] - 5.0) < 1e-15

    def test_cardy_coefficients_F1(self):
        """F_1 in Cardy data matches kappa/24."""
        coeffs = cardy_subleading_coefficients(10.0)
        assert abs(coeffs['F_1'] - 5.0 / 24.0) < 1e-15


# ============================================================================
# 6. Hellerman bound with shadow
# ============================================================================

class TestHellermanShadow:
    """Hellerman bound augmented by shadow obstruction tower."""

    def test_hellerman_standard_formula(self):
        """Standard Hellerman: Delta <= c/12 + 0.4736 for c > 1."""
        assert abs(hellerman_bound_standard(12.0) - (1.0 + 0.4736)) < 1e-10

    def test_hellerman_not_applicable_small_c(self):
        """Hellerman bound is inf for c <= 1."""
        assert hellerman_bound_standard(0.5) == float('inf')

    def test_shadow_augmented_tighter(self):
        """Shadow-augmented bound is strictly tighter than standard for c > 1."""
        for c_val in [2.0, 5.0, 10.0, 50.0, 100.0]:
            result = hellerman_bound_shadow_augmented(c_val)
            assert result['bound_is_tighter']

    def test_shadow_augmented_positive(self):
        """Shadow-augmented bound is positive for c > 1."""
        for c_val in [2.0, 10.0, 100.0]:
            result = hellerman_bound_shadow_augmented(c_val)
            assert result['shadow_augmented'] > 0

    def test_shadow_improvement_positive(self):
        """Shadow improvement is positive for c > 1."""
        result = hellerman_bound_shadow_augmented(10.0)
        assert result['improvement'] > 0

    def test_hellerman_comparison_list(self):
        """Comparison returns results for all c values."""
        results = hellerman_shadow_comparison([5.0, 10.0, 50.0])
        assert len(results) == 3
        for r in results:
            assert 'hellerman' in r
            assert 'shadow_augmented' in r

    def test_hellerman_shadow_at_c26(self):
        """At c=26 (critical string): bound ~ 26/12 + O(1) ~ 2.64."""
        result = hellerman_bound_shadow_augmented(26.0)
        assert 2.0 < result['shadow_augmented'] < 3.0


# ============================================================================
# 7. Sphere packing consistency
# ============================================================================

class TestSpherePacking:
    """Sphere packing from shadow obstruction tower: E8 (c=8) and Leech (c=24)."""

    def test_e8_central_charge(self):
        data = e8_lattice_shadow_data()
        assert data['c'] == 8

    def test_e8_kappa(self):
        data = e8_lattice_shadow_data()
        assert data['kappa'] == 4.0

    def test_e8_gap(self):
        """E8 lattice gap Delta = 1 (root vectors at norm 2)."""
        data = e8_lattice_shadow_data()
        assert data['Delta_gap'] == 1.0

    def test_e8_240_roots(self):
        data = e8_lattice_shadow_data()
        assert data['n_roots'] == 240

    def test_e8_gap_within_hellerman(self):
        """E8 gap satisfies Hellerman bound."""
        data = e8_lattice_shadow_data()
        assert data['gap_within_hellerman']

    def test_e8_gap_within_shadow_bound(self):
        """E8 gap satisfies shadow-augmented bound."""
        data = e8_lattice_shadow_data()
        assert data['gap_within_shadow_bound']

    def test_leech_central_charge(self):
        data = leech_lattice_shadow_data()
        assert data['c'] == 24

    def test_leech_kappa(self):
        data = leech_lattice_shadow_data()
        assert data['kappa'] == 12.0

    def test_leech_gap(self):
        """Leech lattice gap Delta = 2 (NO roots, shortest vectors at norm 4)."""
        data = leech_lattice_shadow_data()
        assert data['Delta_gap'] == 2.0

    def test_leech_no_roots(self):
        """Leech lattice has no roots (key packing property)."""
        data = leech_lattice_shadow_data()
        assert data['no_roots']
        assert data['theta_coefficients'][1] == 0

    def test_leech_kissing_number(self):
        """Leech kissing number = 196560."""
        data = leech_lattice_shadow_data()
        assert data['kissing_number'] == 196560

    def test_leech_gap_within_hellerman(self):
        data = leech_lattice_shadow_data()
        assert data['gap_within_hellerman']

    def test_leech_gap_within_shadow_bound(self):
        data = leech_lattice_shadow_data()
        assert data['gap_within_shadow_bound']

    def test_sphere_packing_both_consistent(self):
        """Both E8 and Leech are consistent with shadow constraints."""
        result = sphere_packing_shadow_consistency()
        assert result['both_consistent']

    def test_e8_saturation_ratio(self):
        """E8 is close to saturating the bound (near optimal)."""
        result = sphere_packing_shadow_consistency()
        assert result['e8_saturation_ratio'] > 0.5  # at least 50% of bound

    def test_leech_saturation_ratio(self):
        """Leech is close to saturating the bound."""
        result = sphere_packing_shadow_consistency()
        assert result['leech_saturation_ratio'] > 0.5


# ============================================================================
# 8. OPE coefficient bounds
# ============================================================================

class TestOPEBounds:
    """OPE coefficient bounds from shadow obstruction tower."""

    def test_ising_C_sigma_sigma_epsilon_exact(self):
        """C_{sigma sigma epsilon}^2 = 1/4 (BPZ exact)."""
        ope = ising_ope_coefficients_exact()
        assert ope['C_sigma_sigma_epsilon_sq'] == Rational(1, 4)

    def test_ising_Z2_selection_rules(self):
        """Z_2 selection rules: C_{sss} = 0, C_{eee} = 0."""
        ope = ising_ope_coefficients_exact()
        assert ope['C_sigma_sigma_sigma'] == 0
        assert ope['C_epsilon_epsilon_epsilon'] == 0

    def test_ising_ope_within_shadow_bounds(self):
        """Exact C_{sse}^2 = 1/4 is within shadow-constrained range."""
        result = ising_ope_shadow_constraint()
        assert result['exact_within_shadow']

    def test_shadow_narrows_ope_range(self):
        """Shadow constraints narrow the OPE allowed range."""
        result = ising_ope_shadow_constraint()
        assert result['shadow_narrows_range']

    def test_shadow_narrowing_factor_positive(self):
        """Narrowing factor > 1 (shadow is strictly tighter)."""
        result = ising_ope_shadow_constraint()
        assert result['narrowing_factor'] > 1.0

    def test_ope_region_general_c(self):
        """OPE allowed region has correct structure at general c."""
        for c_val in [1.0, 5.0, 10.0]:
            result = ope_shadow_allowed_region(c_val)
            assert result['shadow_narrows']

    def test_ope_region_shadow_range_nonempty(self):
        """Shadow-constrained range is nonempty."""
        result = ope_shadow_allowed_region(10.0)
        lo, hi = result['C_leading_sq_shadow_range']
        assert hi > lo


# ============================================================================
# 9. Master analysis and cross-checks
# ============================================================================

class TestMasterAnalysis:
    """Full shadow bootstrap analysis: integration tests."""

    def test_master_ising(self):
        """Master analysis at c=1/2 (Ising)."""
        result = full_shadow_bootstrap_analysis(Rational(1, 2))
        assert result['c'] == Rational(1, 2)
        assert 'shadow_data' in result
        assert 'cardy_coefficients' in result

    def test_master_c1(self):
        """Master analysis at c=1."""
        result = full_shadow_bootstrap_analysis(1.0)
        assert result['c'] == 1.0

    def test_master_c26(self):
        """Master analysis at c=26 (critical string)."""
        result = full_shadow_bootstrap_analysis(26.0)
        assert result['c'] == 26.0
        assert result['shadow_data']['kappa'] == 13.0

    def test_kappa_additivity_check(self):
        """AP24 check: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, not 0."""
        for c_val in [Rational(1, 2), 1, 10, 13]:
            k1 = kappa_virasoro(c_val)
            k2 = kappa_virasoro(26 - c_val)
            # AP24: the sum is 13 for Virasoro (NOT zero)
            assert k1 + k2 == 13

    def test_self_dual_point(self):
        """Virasoro self-dual at c=13: kappa(13) = kappa(26-13) = 13/2."""
        assert kappa_virasoro(13) == Rational(13, 2)
        assert kappa_virasoro(26 - 13) == Rational(13, 2)

    def test_shadow_class_M_for_all_virasoro(self):
        """All Virasoro algebras have shadow class M (infinite tower)."""
        for c_val in [Rational(1, 2), 1, 10, 26]:
            data = virasoro_shadow_data(c_val)
            assert data['shadow_class'] == 'M'

    def test_F1_is_kappa_over_24(self):
        """F_1 = kappa/24 universally."""
        for c_val in [1, 10, 26]:
            data = virasoro_shadow_data(c_val)
            assert data['F_1'] == data['kappa'] / 24

    def test_Q_contact_decreases_with_c(self):
        """Q^contact = 10/[c(5c+22)] decreases with c for c > 0."""
        q1 = float(Q_contact_virasoro(1))
        q10 = float(Q_contact_virasoro(10))
        q100 = float(Q_contact_virasoro(100))
        assert q1 > q10 > q100

    def test_genus_hierarchy(self):
        """F_1 > F_2 > F_3 (Bernoulli decay) at fixed c."""
        c = 10
        data = virasoro_shadow_data(c)
        assert float(data['F_1']) > float(data['F_2']) > float(data['F_3'])
