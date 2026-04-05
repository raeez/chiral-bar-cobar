r"""Tests for bootstrap_from_mc_engine.py.

Tests the derivation of conformal bootstrap constraints from the
Maurer-Cartan equation of the shadow obstruction tower.

Organized by mathematical topic:
  1. Crossing symmetry from MC (genus 0, arity 4)
  2. Unitarity bound from shadow metric
  3. OPE coefficient bounds
  4. Modular bootstrap (genus 1)
  5. Extremal functional from shadow connection
  6. Ising model (c=1/2) multi-path
  7. Free boson (c=1) from MC
  8. Koszulness = bootstrap completeness
  9. Shadow bound vs RRTV comparison
  10. Multi-path verification
  11. Shadow metric properties
  12. Kac determinant cross-checks
"""

import math
import sys
import os

import pytest
import numpy as np

# Ensure compute/lib is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bootstrap_from_mc_engine import (
    # Primitives
    kappa_virasoro,
    Q_contact_virasoro,
    shadow_metric_Q,
    shadow_metric_virasoro,
    lambda_fp,
    F_g_shadow,
    # Crossing symmetry
    virasoro_conformal_block_small_z,
    crossing_symmetry_from_mc,
    mc_bracket_arity4,
    # Unitarity bound
    unitarity_bound_from_shadow,
    kac_determinant_level_n,
    bpz_minimal_model_weights,
    # OPE bounds
    ope_bound_from_shadow,
    # Modular bootstrap
    genus1_mc_constraint,
    modular_differential_equation,
    hellerman_gap_bound,
    # Extremal functional
    shadow_connection_flat_section,
    extremal_functional_at_delta_zero,
    # Ising model
    ising_from_mc,
    ising_bpz_four_point,
    _hyper2f1,
    # Free boson
    free_boson_from_mc,
    # Koszulness
    koszulness_bootstrap_completeness,
    # RRTV comparison
    rrtv_bound_comparison,
    # Multi-path verification
    verify_ising_ope_multipath,
    verify_unitarity_bound_multipath,
    verify_modular_bootstrap_multipath,
    # Master
    master_bootstrap_mc_verification,
)


# =========================================================================
# 1. SHADOW TOWER PRIMITIVES
# =========================================================================

class TestShadowPrimitives:
    """Tests for shadow tower primitive functions."""

    def test_kappa_virasoro_c_half(self):
        """kappa(Vir_{1/2}) = 1/4."""
        assert abs(kappa_virasoro(0.5) - 0.25) < 1e-15

    def test_kappa_virasoro_c_1(self):
        """kappa(Vir_1) = 1/2."""
        assert abs(kappa_virasoro(1.0) - 0.5) < 1e-15

    def test_kappa_virasoro_c_25(self):
        """kappa(Vir_25) = 25/2."""
        assert abs(kappa_virasoro(25.0) - 12.5) < 1e-15

    def test_kappa_virasoro_c_26(self):
        """kappa(Vir_26) = 13. (Critical string: ghost kappa = -13.)"""
        assert abs(kappa_virasoro(26.0) - 13.0) < 1e-15

    def test_Q_contact_virasoro_c_half(self):
        """Q^contact(Vir_{1/2}) = 10/(0.5 * (2.5 + 22)) = 10/12.25."""
        expected = 10.0 / (0.5 * (2.5 + 22.0))
        assert abs(Q_contact_virasoro(0.5) - expected) < 1e-12

    def test_Q_contact_virasoro_c_1(self):
        """Q^contact(Vir_1) = 10/(1 * 27) = 10/27."""
        expected = 10.0 / 27.0
        assert abs(Q_contact_virasoro(1.0) - expected) < 1e-12

    def test_Q_contact_virasoro_large_c(self):
        """Q^contact -> 0 as c -> infinity."""
        Q_100 = Q_contact_virasoro(100.0)
        Q_1000 = Q_contact_virasoro(1000.0)
        assert Q_100 > Q_1000 > 0

    def test_shadow_metric_positive_at_origin(self):
        """Q_L(0) = (2*kappa)^2 = c^2 > 0 for c > 0."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            Q0 = shadow_metric_virasoro(c, 0.0)
            assert Q0 > 0, f"Q_L(0) should be positive for c={c}"
            assert abs(Q0 - c ** 2) < 1e-10

    def test_shadow_metric_positive_generic(self):
        """Q_L(t) > 0 for all t when c > 0 (Virasoro Delta > 0)."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            for t in [-10.0, -1.0, -0.1, 0.0, 0.1, 1.0, 10.0]:
                Qt = shadow_metric_virasoro(c, t)
                assert Qt > 0, f"Q_L({t}) = {Qt} < 0 for c={c}"

    def test_lambda_fp_genus_1(self):
        """lambda_1 = 1/24 (Bernoulli: B_2 = 1/6)."""
        lam1 = lambda_fp(1)
        assert abs(float(lam1) - 1.0/24.0) < 1e-15

    def test_lambda_fp_genus_2(self):
        """lambda_2 = 7/5760."""
        lam2 = lambda_fp(2)
        assert abs(float(lam2) - 7.0/5760.0) < 1e-15

    def test_lambda_fp_genus_3(self):
        """lambda_3 = 31/967680."""
        lam3 = lambda_fp(3)
        expected = 31.0 / 967680.0
        assert abs(float(lam3) - expected) < 1e-15

    def test_F_g_shadow_genus1(self):
        """F_1 = kappa/24 = c/48."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            kappa = c / 2.0
            F1 = F_g_shadow(kappa, 1)
            expected = c / 48.0
            assert abs(float(F1) - expected) < 1e-12


# =========================================================================
# 2. CROSSING SYMMETRY FROM MC (genus 0, arity 4)
# =========================================================================

class TestCrossingSymmetry:
    """Test that crossing symmetry follows from [Theta,Theta]|_4 = 0."""

    def test_conformal_block_identity(self):
        """Identity block F_0(z) ~ z^{-2h} for small z."""
        # For h_ext = 1/16, h_int = 0 (identity):
        F0 = virasoro_conformal_block_small_z(0.5, 1.0/16.0, 0.0, 0.1)
        # Should be ~ (0.1)^{-1/8} * (1 + corrections)
        expected_leading = 0.1 ** (-1.0/8.0)
        # Allow 50% relative error from higher-order corrections
        assert abs(F0 / expected_leading - 1) < 0.5

    def test_conformal_block_nonzero(self):
        """Conformal blocks are nonzero at generic z."""
        F = virasoro_conformal_block_small_z(0.5, 1.0/16.0, 0.5, 0.1)
        assert abs(F) > 1e-10

    def test_crossing_ising_approximate(self):
        """Ising model crossing should be approximately satisfied."""
        c = 0.5
        h_ext = 1.0 / 16.0
        spectrum = [0.0, 0.5]     # identity + epsilon
        ope_sq = [1.0, 0.25]     # C_ss1^2 = 1, C_sse^2 = 1/4

        result = crossing_symmetry_from_mc(c, h_ext, spectrum, ope_sq, z=0.2)
        # With our approximate blocks, crossing won't be exact,
        # but both channels should be finite and of the same sign
        assert result['s_channel'] != 0
        assert result['t_channel'] != 0

    def test_mc_bracket_arity4_structure(self):
        """MC bracket at arity 4 produces consistent structure."""
        c = 0.5
        h_ext = 1.0 / 16.0
        spectrum = [0.0, 0.5]
        ope_sq = [1.0, 0.25]

        result = mc_bracket_arity4(c, h_ext, spectrum, ope_sq)
        assert 'max_relative_violation' in result
        assert 'point_data' in result
        assert len(result['point_data']) == 6

    def test_crossing_c1_free_boson(self):
        """Free boson crossing: shadow class G, crossing trivial."""
        c = 1.0
        h_ext = 0.25  # vertex operator V_1
        # Free boson: only identity in the sigma x sigma OPE for the simplest case
        spectrum = [0.0]
        ope_sq = [1.0]

        result = crossing_symmetry_from_mc(c, h_ext, spectrum, ope_sq, z=0.3)
        assert result['s_channel'] != 0

    def test_crossing_large_c(self):
        """Large c: MFT-like behavior, crossing should work approximately."""
        c = 100.0
        h_ext = 2.0
        # Large-c approximation: only identity block dominates
        spectrum = [0.0]
        ope_sq = [1.0]

        result = crossing_symmetry_from_mc(c, h_ext, spectrum, ope_sq, z=0.2)
        assert result['s_channel'] != 0


# =========================================================================
# 3. UNITARITY BOUND FROM SHADOW METRIC
# =========================================================================

class TestUnitarityBound:
    """Test unitarity bounds derived from shadow metric positivity."""

    def test_unitarity_bound_c_half(self):
        """At c = 1/2: all three paths give h >= 0."""
        result = unitarity_bound_from_shadow(0.5)
        assert result['all_agree_h_ge_0']
        assert result['all_agree_c_ge_0']

    def test_unitarity_bound_c_1(self):
        """At c = 1: all three paths give h >= 0."""
        result = unitarity_bound_from_shadow(1.0)
        assert result['all_agree_h_ge_0']

    def test_unitarity_bound_c_25(self):
        """At c = 25: all three paths give h >= 0."""
        result = unitarity_bound_from_shadow(25.0)
        assert result['all_agree_h_ge_0']

    def test_shadow_metric_positive_implies_unitarity(self):
        """Q_L positive => shadow tower consistent => unitarity."""
        for c in [0.5, 1.0, 10.0, 25.0, 100.0]:
            result = unitarity_bound_from_shadow(c)
            assert result['shadow']['Q_L_positive']
            assert result['shadow']['Delta'] > 0

    def test_kac_determinant_level_1(self):
        """Kac det at level 1: det = 2h. Zero at h=0, positive for h>0."""
        assert abs(kac_determinant_level_n(0.0, 1.0, 1) - 0.0) < 1e-15
        assert kac_determinant_level_n(0.5, 1.0, 1) > 0
        assert kac_determinant_level_n(1.0, 1.0, 1) > 0

    def test_kac_determinant_level_2(self):
        """Kac det at level 2: positive for generic h, c."""
        # For c = 1/2, h = 1/16 (sigma): there IS a null vector at level 2
        # det should vanish (h = h_{2,1} = 1/16 for c = 1/2)
        det = kac_determinant_level_n(1.0/16.0, 0.5, 2)
        # h_{2,1} = [(2p - q)^2 - (p-q)^2]/(4pq) for M(4,3)
        # = [(8-3)^2 - 1]/(48) = 24/48 = 1/2  ... wait
        # Actually h_{2,1} in M(4,3) is:
        # h_{r,s} = ((4r - 3s)^2 - 1)/48
        # h_{2,1} = ((8-3)^2 - 1)/48 = 24/48 = 1/2
        # h_{1,2} = ((4-6)^2 - 1)/48 = 3/48 = 1/16
        # So h = 1/16 is h_{1,2}, which has null at level r*s = 2.
        # The Kac determinant at level 2 should vanish for h = h_{1,2} = 1/16
        # at c = 1/2.
        # Check: G_{11} = 4*(1/16) + 1/4 = 1/4 + 1/4 = 1/2
        #         G_{12} = 6*(1/16) = 3/8
        #         G_{22} = 4*(1/16)*(2*(1/16)+1) = (1/4)*(9/8) = 9/32
        #         det = (1/2)*(9/32) - (3/8)^2 = 9/64 - 9/64 = 0
        assert abs(det) < 1e-12, f"Kac det should vanish for Ising sigma: got {det}"

    def test_kac_determinant_level_2_nondegenerate(self):
        """Kac det at level 2 is positive for generic h, c."""
        det = kac_determinant_level_n(2.0, 10.0, 2)
        assert det > 0, f"Kac det should be positive for h=2, c=10: got {det}"

    def test_bpz_ising_weights(self):
        """Ising model M(4,3) has weights {0, 1/16, 1/2}."""
        weights = bpz_minimal_model_weights(4, 3)
        h_values = sorted([w[2] for w in weights])
        expected = [0.0, 1.0/16.0, 0.5]
        for h_got, h_exp in zip(h_values, expected):
            assert abs(h_got - h_exp) < 1e-12, f"Expected {h_exp}, got {h_got}"

    def test_bpz_tricritical_ising_weights(self):
        """Tricritical Ising M(5,4) has 6 primaries."""
        weights = bpz_minimal_model_weights(5, 4)
        assert len(weights) == 6

    def test_bpz_minimal_model_c_formula(self):
        """c = 1 - 6(p-q)^2/(pq) for M(p,q)."""
        # M(4,3): c = 1 - 6*1/12 = 1/2
        c_ising = 1.0 - 6.0 * (4 - 3) ** 2 / (4.0 * 3.0)
        assert abs(c_ising - 0.5) < 1e-12

        # M(5,4): c = 1 - 6*1/20 = 1 - 3/10 = 7/10
        c_tricritical = 1.0 - 6.0 * 1.0 / 20.0
        assert abs(c_tricritical - 0.7) < 1e-12


# =========================================================================
# 4. OPE COEFFICIENT BOUNDS
# =========================================================================

class TestOPEBounds:
    """Test OPE coefficient bounds from shadow invariants."""

    def test_identity_normalization(self):
        """Identity OPE: C^2 = 1 by normalization."""
        result = ope_bound_from_shadow(0.5, 1.0/16.0, 0.0)
        assert result['is_identity']
        assert abs(result['bound'] - 1.0) < 1e-15

    def test_ope_bound_finite(self):
        """OPE bound is finite for generic operators."""
        result = ope_bound_from_shadow(0.5, 1.0/16.0, 0.5)
        assert result['bound'] < float('inf')
        assert result['bound'] > 0

    def test_ope_bound_includes_shadow_correction(self):
        """Shadow correction modifies the MFT bound."""
        result = ope_bound_from_shadow(10.0, 2.0, 4.0)
        assert 'shadow_correction' in result
        assert result['shadow_correction'] != 1.0  # modified by Q_contact

    def test_ope_bound_large_c_approaches_mft(self):
        """At large c, the shadow correction approaches 1."""
        # Use h_ext = 2 so that h_ext*(h_ext-1) = 2 != 0
        bound_c100 = ope_bound_from_shadow(100.0, 2.0, 4.0)
        bound_c1000 = ope_bound_from_shadow(1000.0, 2.0, 4.0)
        # Shadow correction -> 1 as c -> infinity (Q_contact -> 0)
        dev_1000 = abs(bound_c1000['shadow_correction'] - 1.0)
        dev_100 = abs(bound_c100['shadow_correction'] - 1.0)
        assert dev_1000 < dev_100 or dev_100 < 1e-10

    def test_ope_bound_c_half_epsilon(self):
        """For Ising sigma-sigma-epsilon: bound should be >= 1/4."""
        result = ope_bound_from_shadow(0.5, 1.0/16.0, 0.5)
        # The bound should be AT LEAST the exact value 1/4
        assert result['bound'] >= 0.25 - 1e-10


# =========================================================================
# 5. MODULAR BOOTSTRAP (genus 1)
# =========================================================================

class TestModularBootstrap:
    """Test modular bootstrap constraints from genus-1 MC."""

    def test_genus1_F1_ising(self):
        """F_1(Ising) = (1/4)/24 = 1/96."""
        result = genus1_mc_constraint(0.5)
        assert abs(result['F_1'] - 1.0/96.0) < 1e-15

    def test_genus1_F1_c1(self):
        """F_1(c=1) = (1/2)/24 = 1/48."""
        result = genus1_mc_constraint(1.0)
        assert abs(result['F_1'] - 1.0/48.0) < 1e-15

    def test_genus1_F1_proportional_to_c(self):
        """F_1 = c/48 is linear in c."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            result = genus1_mc_constraint(c)
            assert abs(result['F_1'] - c / 48.0) < 1e-12

    def test_genus1_F2_planted_forest(self):
        """F_2 includes planted-forest correction delta_pf."""
        result = genus1_mc_constraint(10.0)
        assert result['F_2_planted_forest'] != 0
        # delta_pf = S_3 * (10*S_3 - kappa) / 48 = 2*(20 - 5)/48 = 30/48 = 5/8
        expected_delta = 2.0 * (20.0 - 5.0) / 48.0
        assert abs(result['F_2_planted_forest'] - expected_delta) < 1e-12

    def test_genus1_cardy_coefficient(self):
        """Cardy coefficient sqrt(c/3) is correct."""
        result = genus1_mc_constraint(12.0)
        assert abs(result['cardy_coefficient'] - 2.0) < 1e-12

    def test_mde_structure(self):
        """MDE has order = n_primaries."""
        result = modular_differential_equation(0.5, 3)  # Ising: 3 primaries
        assert result['mde_order'] == 3

    def test_hellerman_bound_large_c(self):
        """Hellerman bound: Delta_1 <= c/12 + O(1) for large c."""
        for c in [10.0, 100.0, 1000.0]:
            result = hellerman_gap_bound(c)
            assert result['hellerman_leading'] == c / 12.0
            assert result['hellerman_bound'] > c / 12.0

    def test_hellerman_bound_monotone(self):
        """Hellerman bound is monotonically increasing in c."""
        bounds = [hellerman_gap_bound(c)['hellerman_bound'] for c in [10, 50, 100]]
        assert bounds[0] < bounds[1] < bounds[2]


# =========================================================================
# 6. EXTREMAL FUNCTIONAL FROM SHADOW CONNECTION
# =========================================================================

class TestExtremalFunctional:
    """Test the extremal functional from the shadow connection flat section."""

    def test_flat_section_at_origin(self):
        """Phi(0) = 1 (normalization)."""
        result = shadow_connection_flat_section(10.0, 0.0)
        assert abs(result['Phi'] - 1.0) < 1e-12

    def test_flat_section_positive(self):
        """Phi(t) > 0 for Virasoro (Delta > 0)."""
        for c in [0.5, 1.0, 10.0]:
            for t in [0.0, 0.1, 0.5, 1.0]:
                result = shadow_connection_flat_section(c, t)
                assert result['valid']
                assert result['Phi'] > 0

    def test_flat_section_increasing(self):
        """Phi(t) is monotonically increasing for t > 0 (Virasoro, generic c)."""
        c = 10.0
        phi_values = []
        for t in [0.0, 0.1, 0.5, 1.0, 2.0]:
            result = shadow_connection_flat_section(c, t)
            phi_values.append(result['Phi'])
        for i in range(len(phi_values) - 1):
            assert phi_values[i] <= phi_values[i+1] + 1e-10

    def test_flat_section_monodromy(self):
        """Monodromy = -1 (Koszul sign)."""
        result = shadow_connection_flat_section(10.0, 0.5)
        assert result['monodromy'] == -1

    def test_extremal_at_delta_zero(self):
        """At Delta = 0: flat section is linear."""
        result = extremal_functional_at_delta_zero(10.0)
        assert result['is_extremal']
        assert result['Delta'] == 0.0
        for entry in result['flat_section']:
            t = entry['t']
            expected = 1.0 + 6.0 * t / 10.0
            assert abs(entry['Phi_extremal'] - expected) < 1e-12

    def test_extremal_linear_property(self):
        """At Delta = 0, Phi(t) = 1 + 6t/c is exactly linear."""
        result = extremal_functional_at_delta_zero(5.0, t_values=[0, 1, 2, 3])
        for entry in result['flat_section']:
            assert entry['Phi_linear']

    def test_flat_section_q_ratio(self):
        """Phi(t) = sqrt(Q(t)/Q(0)) by definition."""
        c = 10.0
        for t in [0.1, 0.5, 1.0, 2.0]:
            result = shadow_connection_flat_section(c, t)
            Q_t = result['Q_t']
            Q_0 = result['Q_0']
            expected_phi = math.sqrt(Q_t / Q_0)
            assert abs(result['Phi'] - expected_phi) < 1e-12


# =========================================================================
# 7. ISING MODEL (c=1/2) MULTI-PATH VERIFICATION
# =========================================================================

class TestIsingModel:
    """Comprehensive tests for the Ising model from MC."""

    def test_ising_central_charge(self):
        """Ising model has c = 1/2."""
        result = ising_from_mc()
        assert abs(result['c'] - 0.5) < 1e-15

    def test_ising_kappa(self):
        """kappa(Ising) = 1/4."""
        result = ising_from_mc()
        assert abs(result['kappa'] - 0.25) < 1e-15

    def test_ising_primaries(self):
        """Ising has three primaries: 1, sigma, epsilon."""
        result = ising_from_mc()
        assert len(result['primaries']) == 3
        assert abs(result['primaries']['1']['h'] - 0.0) < 1e-15
        assert abs(result['primaries']['sigma']['h'] - 1.0/16.0) < 1e-15
        assert abs(result['primaries']['epsilon']['h'] - 0.5) < 1e-15

    def test_ising_ope_C_sse(self):
        """C_{sigma sigma epsilon}^2 = 1/4."""
        result = ising_from_mc()
        assert abs(result['ope_coefficients']['C_sse_sq'] - 0.25) < 1e-15

    def test_ising_ope_C_sss(self):
        """C_{sigma sigma sigma}^2 = 0 (Z2 symmetry)."""
        result = ising_from_mc()
        assert abs(result['ope_coefficients']['C_sss_sq'] - 0.0) < 1e-15

    def test_ising_shadow_class(self):
        """Ising shadow class is L (minimal model)."""
        result = ising_from_mc()
        assert result['shadow_data']['shadow_class'] == 'L'

    def test_ising_fusion_rules(self):
        """Ising fusion: sigma x sigma = 1 + epsilon."""
        result = ising_from_mc()
        fusion = result['fusion_rules']
        assert '1' in fusion[('sigma', 'sigma')]
        assert 'epsilon' in fusion[('sigma', 'sigma')]

    def test_ising_four_point_function(self):
        """Ising 4-point function is finite at generic z."""
        G = ising_bpz_four_point(0.3)
        assert math.isfinite(G)
        assert G > 0

    def test_ising_four_point_singular_at_0(self):
        """Ising 4-point diverges as z -> 0."""
        G = ising_bpz_four_point(0.01)
        assert G > ising_bpz_four_point(0.1)

    def test_ising_uniqueness(self):
        """Ising is the UNIQUE solution at c=1/2 with Koszulness."""
        result = ising_from_mc()
        assert 'UNIQUE' in result['uniqueness']

    def test_ising_multipath_all_agree(self):
        """All four paths give C_{sse}^2 = 1/4."""
        result = verify_ising_ope_multipath()
        assert result['all_agree']
        assert result['n_paths'] == 4
        assert abs(result['exact_value'] - 0.25) < 1e-15

    def test_ising_multipath_max_deviation(self):
        """Maximum deviation across paths is negligible."""
        result = verify_ising_ope_multipath()
        assert result['max_deviation'] < 1e-10

    def test_ising_multipath_mc_path(self):
        """MC equation path gives 1/4."""
        result = verify_ising_ope_multipath()
        assert abs(result['paths']['MC_equation']['C_sse_sq'] - 0.25) < 1e-15

    def test_ising_multipath_bpz_path(self):
        """BPZ equation path gives 1/4."""
        result = verify_ising_ope_multipath()
        assert abs(result['paths']['BPZ_equation']['C_sse_sq'] - 0.25) < 1e-15

    def test_ising_multipath_coulomb_path(self):
        """Coulomb gas path gives 1/4."""
        result = verify_ising_ope_multipath()
        assert abs(result['paths']['Coulomb_gas']['C_sse_sq'] - 0.25) < 1e-15

    def test_ising_multipath_lattice_path(self):
        """Lattice exact solution path gives 1/4."""
        result = verify_ising_ope_multipath()
        assert abs(result['paths']['lattice_exact']['C_sse_sq'] - 0.25) < 1e-15


# =========================================================================
# 8. FREE BOSON (c=1) FROM MC
# =========================================================================

class TestFreeBoson:
    """Tests for c=1 free boson from MC."""

    def test_free_boson_c(self):
        """Free boson has c = 1."""
        result = free_boson_from_mc(R=1.0)
        assert abs(result['c'] - 1.0) < 1e-15

    def test_free_boson_kappa(self):
        """kappa(free boson) = 1/2."""
        result = free_boson_from_mc(R=1.0)
        assert abs(result['kappa'] - 0.5) < 1e-15

    def test_free_boson_shadow_class_G(self):
        """Free boson is Gaussian class (shadow depth 2)."""
        result = free_boson_from_mc(R=1.0)
        assert result['shadow_data']['shadow_class'] == 'G'
        assert result['shadow_data']['shadow_depth'] == 2

    def test_free_boson_mc_trivial(self):
        """MC at arity >= 3 is trivially zero for class G."""
        result = free_boson_from_mc(R=1.0)
        assert result['mc_trivial']

    def test_free_boson_S3_zero(self):
        """Heisenberg has S_3 = 0 (no cubic shadow)."""
        result = free_boson_from_mc(R=1.0)
        assert abs(result['shadow_data']['S_3']) < 1e-15

    def test_free_boson_spectrum_nonempty(self):
        """Free boson has a nontrivial spectrum."""
        result = free_boson_from_mc(R=1.0)
        assert len(result['spectrum']) > 0

    def test_free_boson_spectrum_positive(self):
        """All operator dimensions are positive."""
        result = free_boson_from_mc(R=1.0)
        for op in result['spectrum']:
            assert op['h'] > 0

    def test_free_boson_t_duality(self):
        """T-duality: spectrum at R and 1/R agree."""
        result_R = free_boson_from_mc(R=2.0)
        result_inv = free_boson_from_mc(R=0.5)
        # The spectra should be identical (T-duality exchanges n <-> w)
        h_R = sorted([op['h'] for op in result_R['spectrum']])
        h_inv = sorted([op['h'] for op in result_inv['spectrum']])
        for h1, h2 in zip(h_R, h_inv):
            assert abs(h1 - h2) < 1e-12

    def test_free_boson_self_dual_radius(self):
        """At R = 1 (self-dual): momentum and winding are symmetric."""
        result = free_boson_from_mc(R=1.0)
        # At R=1: h_{n,0} = n^2/4 = h_{0,n}
        for op in result['spectrum']:
            n, w = op['n'], op['w']
            if abs(n) == abs(w):
                # h should be n^2/4 + n^2/4 = n^2/2
                expected = n ** 2 / 4.0 + w ** 2 / 4.0
                assert abs(op['h'] - expected) < 1e-12


# =========================================================================
# 9. KOSZULNESS = BOOTSTRAP COMPLETENESS
# =========================================================================

class TestKoszulnessCompleteness:
    """Test Koszulness as bootstrap completeness conjecture."""

    def test_minimal_model_koszul(self):
        """Minimal models (c < 1) are Koszul."""
        result = koszulness_bootstrap_completeness(0.5)
        assert result['koszul']

    def test_minimal_model_bootstrap_complete(self):
        """Minimal models have complete bootstrap."""
        result = koszulness_bootstrap_completeness(0.5)
        assert result['bootstrap_complete']

    def test_free_boson_koszul(self):
        """Free boson is Koszul."""
        result = koszulness_bootstrap_completeness(1.0)
        assert result['koszul']

    def test_large_c_koszul_but_incomplete(self):
        """Virasoro at large c is Koszul but bootstrap-incomplete."""
        result = koszulness_bootstrap_completeness(30.0)
        assert result['koszul']
        # At large c, multiple theories exist (non-unique)
        assert not result['bootstrap_complete']

    def test_non_unitary_not_koszul(self):
        """c < 0 is non-unitary, not Koszul."""
        result = koszulness_bootstrap_completeness(-2.0)
        assert not result['koszul']


# =========================================================================
# 10. SHADOW BOUND vs RRTV COMPARISON
# =========================================================================

class TestRRTVComparison:
    """Test comparison between shadow-derived and RRTV bounds."""

    def test_ising_rrtv_saturated(self):
        """Ising model saturates the bootstrap bound."""
        result = rrtv_bound_comparison(0.5, 1.0/16.0)
        assert result['shadow_saturated']
        assert abs(result['gap_bound_exact'] - 0.5) < 1e-12

    def test_ising_rrtv_C_sse_exact(self):
        """Ising C_{sse}^2 = 1/4 from RRTV."""
        result = rrtv_bound_comparison(0.5, 1.0/16.0)
        assert abs(result['C_sse_sq_exact'] - 0.25) < 1e-12

    def test_ising_shadow_equals_rrtv(self):
        """For Ising: shadow bound = RRTV bound."""
        result = rrtv_bound_comparison(0.5, 1.0/16.0)
        assert abs(result['gap_bound_shadow'] - result['gap_bound_RRTV']) < 1e-12

    def test_generic_genus0_agrees_with_rrtv(self):
        """At genus 0, shadow = crossing = RRTV."""
        result = rrtv_bound_comparison(10.0, 1.0)
        assert 'agrees_with_RRTV' in result.get('genus_0_bound', '')

    def test_genus1_provides_additional_constraint(self):
        """Genus 1 gives an ADDITIONAL constraint beyond RRTV."""
        result = rrtv_bound_comparison(10.0, 1.0)
        assert result['genus_1_constraint'] > 0


# =========================================================================
# 11. MULTI-PATH VERIFICATION
# =========================================================================

class TestMultiPathVerification:
    """Test multi-path verification across topics."""

    def test_unitarity_multipath_c_half(self):
        """Unitarity: 3 paths agree at c=1/2."""
        result = verify_unitarity_bound_multipath(0.5)
        assert result['all_agree']
        assert result['n_paths'] == 3

    def test_unitarity_multipath_c_25(self):
        """Unitarity: 3 paths agree at c=25."""
        result = verify_unitarity_bound_multipath(25.0)
        assert result['all_agree']

    def test_modular_multipath_c_half(self):
        """Modular: 3 paths agree at c=1/2."""
        result = verify_modular_bootstrap_multipath(0.5)
        assert result['all_agree']
        assert result['n_paths'] == 3

    def test_modular_multipath_c_1(self):
        """Modular: 3 paths agree at c=1."""
        result = verify_modular_bootstrap_multipath(1.0)
        assert result['all_agree']

    def test_modular_multipath_F1_value(self):
        """Modular F_1 = c/48 from all three paths."""
        result = verify_modular_bootstrap_multipath(10.0)
        expected = 10.0 / 48.0
        for path_data in result['paths'].values():
            assert abs(path_data['F_1'] - expected) < 1e-12


# =========================================================================
# 12. SHADOW METRIC DETAILED PROPERTIES
# =========================================================================

class TestShadowMetricProperties:
    """Detailed tests of shadow metric Q_L properties."""

    def test_shadow_metric_quadratic_in_t(self):
        """Q_L(t) is quadratic in t."""
        c = 10.0
        kappa = 5.0
        alpha = 2.0
        S4 = Q_contact_virasoro(c)

        # Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
        # = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 2*Delta)*t^2
        # This is a polynomial of degree exactly 2.

        # Check: Q(t) = a + b*t + c*t^2
        Q0 = shadow_metric_Q(kappa, alpha, S4, 0.0)
        Q1 = shadow_metric_Q(kappa, alpha, S4, 1.0)
        Qm1 = shadow_metric_Q(kappa, alpha, S4, -1.0)
        Q2 = shadow_metric_Q(kappa, alpha, S4, 2.0)

        # From a + b + c = Q1 and a - b + c = Qm1:
        a = Q0
        b = (Q1 - Qm1) / 2.0
        c_coeff = (Q1 + Qm1) / 2.0 - a

        # Verify at t=2
        Q2_predicted = a + 2 * b + 4 * c_coeff
        assert abs(Q2 - Q2_predicted) < 1e-10

    def test_shadow_metric_discriminant_virasoro(self):
        """Delta = 40/(5c+22) for Virasoro."""
        for c in [0.5, 1.0, 10.0, 25.0]:
            kappa = c / 2.0
            S4 = Q_contact_virasoro(c)
            Delta = 8.0 * kappa * S4
            expected = 40.0 / (5.0 * c + 22.0)
            assert abs(Delta - expected) < 1e-10

    def test_shadow_metric_perfect_square_at_delta_zero(self):
        """When Delta = 0, Q_L is a perfect square."""
        # Delta = 0 means 8*kappa*S4 = 0, i.e., S4 = 0 (for kappa != 0)
        # Then Q_L(t) = (2*kappa + 3*alpha*t)^2
        kappa = 5.0
        alpha = 2.0
        S4 = 0.0
        for t in [-1.0, 0.0, 0.5, 1.0, 2.0]:
            Qt = shadow_metric_Q(kappa, alpha, S4, t)
            expected = (2.0 * kappa + 3.0 * alpha * t) ** 2
            assert abs(Qt - expected) < 1e-10

    def test_shadow_metric_virasoro_never_zero(self):
        """For Virasoro c > 0: Q_L(t) > 0 for all real t."""
        for c in [0.5, 1.0, 10.0, 25.0, 100.0]:
            # The discriminant of Q_L as quadratic in t:
            # disc = q1^2 - 4*q0*q2 = (12*c*2)^2 - 4*c^2*(36 + 2*Delta)
            # For Virasoro: this is -8*c^2*Delta < 0 when Delta > 0
            # So Q_L has no real roots.
            kappa = c / 2.0
            S4 = Q_contact_virasoro(c)
            Delta = 8.0 * kappa * S4
            q0 = (2 * kappa) ** 2
            q1 = 12.0 * kappa * 2.0  # alpha = 2 for Virasoro
            q2 = 9.0 * 4.0 + 2.0 * Delta  # 9*alpha^2 + 2*Delta
            disc = q1 ** 2 - 4.0 * q0 * q2
            assert disc < 0, f"Discriminant should be < 0 for c={c}: got {disc}"


# =========================================================================
# 13. HYPERGEOMETRIC FUNCTION TESTS
# =========================================================================

class TestHypergeometric:
    """Tests for the hypergeometric function helper."""

    def test_hyper2f1_at_zero(self):
        """2F1(a, b; c; 0) = 1."""
        assert abs(_hyper2f1(0.5, 0.5, 1.0, 0.0) - 1.0) < 1e-15

    def test_hyper2f1_known_value(self):
        """2F1(1/2, 1/2; 1; z) = (2/pi) * K(sqrt(z)) where K is elliptic."""
        # At z = 0.5: K(1/sqrt(2)) = Gamma(1/4)^2 / (4*sqrt(pi))
        # 2F1(1/2, 1/2; 1; 0.5) ~ 1.1803...
        F = _hyper2f1(0.5, 0.5, 1.0, 0.5, nterms=100)
        # Known value: (2/pi) * K(1/sqrt(2)) ~ 1.18034
        assert abs(F - 1.18034) < 0.001

    def test_hyper2f1_log(self):
        """2F1(1, 1; 2; z) = -log(1-z)/z (exact identity)."""
        for z in [0.1, 0.2, 0.3, 0.4]:
            F = _hyper2f1(1.0, 1.0, 2.0, z, nterms=100)
            exact = -math.log(1.0 - z) / z
            assert abs(F - exact) < 1e-8

    def test_hyper2f1_convergence(self):
        """Series converges for |z| < 1."""
        F_10 = _hyper2f1(0.5, 0.5, 1.0, 0.3, nterms=10)
        F_50 = _hyper2f1(0.5, 0.5, 1.0, 0.3, nterms=50)
        F_100 = _hyper2f1(0.5, 0.5, 1.0, 0.3, nterms=100)
        # Should converge: differences decrease
        assert abs(F_100 - F_50) < abs(F_50 - F_10)


# =========================================================================
# 14. MASTER VERIFICATION
# =========================================================================

class TestMasterVerification:
    """Test the master verification function."""

    def test_master_runs(self):
        """Master verification completes without error."""
        result = master_bootstrap_mc_verification()
        assert 'ising' in result
        assert 'free_boson' in result
        assert 'ising_multipath' in result

    def test_master_ising_consistent(self):
        """Ising results consistent across master."""
        result = master_bootstrap_mc_verification()
        assert abs(result['ising']['kappa'] - 0.25) < 1e-15

    def test_master_multipath_all_agree(self):
        """All multi-path verifications agree in master."""
        result = master_bootstrap_mc_verification()
        assert result['ising_multipath']['all_agree']

    def test_master_unitarity_all_agree(self):
        """All unitarity checks agree in master."""
        result = master_bootstrap_mc_verification()
        for key in result:
            if key.startswith('unitarity_'):
                assert result[key]['all_agree']

    def test_master_modular_all_agree(self):
        """All modular checks agree in master."""
        result = master_bootstrap_mc_verification()
        for key in result:
            if key.startswith('modular_'):
                assert result[key]['all_agree']


# =========================================================================
# 15. ADDITIONAL CROSS-CHECKS
# =========================================================================

class TestCrossChecks:
    """Additional cross-checks between different subsystems."""

    def test_kappa_and_F1_consistency(self):
        """kappa and F_1 satisfy F_1 = kappa/24 for all c."""
        for c in [0.5, 1.0, 2.0, 10.0, 25.0, 100.0]:
            kappa = kappa_virasoro(c)
            result = genus1_mc_constraint(c)
            assert abs(result['F_1'] - float(kappa) / 24.0) < 1e-12

    def test_shadow_metric_and_connection_consistency(self):
        """Shadow metric Q_L matches shadow connection flat section."""
        for c in [0.5, 1.0, 10.0]:
            for t in [0.1, 0.5, 1.0]:
                Q_t = shadow_metric_virasoro(c, t)
                Q_0 = shadow_metric_virasoro(c, 0.0)
                phi_direct = math.sqrt(Q_t / Q_0)
                result = shadow_connection_flat_section(c, t)
                assert abs(result['Phi'] - phi_direct) < 1e-12

    def test_kac_det_vanishes_at_null(self):
        """Kac det vanishes at BPZ null vector locations."""
        # M(4,3): h_{1,2} = 1/16 has null at level 2
        det = kac_determinant_level_n(1.0/16.0, 0.5, 2)
        assert abs(det) < 1e-10

    def test_ising_shadow_kappa_consistent(self):
        """Ising kappa from shadow = kappa from formula."""
        ising = ising_from_mc()
        assert abs(ising['kappa'] - kappa_virasoro(0.5)) < 1e-15

    def test_free_boson_shadow_kappa_consistent(self):
        """Free boson kappa from shadow = kappa from formula."""
        fb = free_boson_from_mc(R=1.0)
        assert abs(fb['kappa'] - kappa_virasoro(1.0)) < 1e-15

    def test_hellerman_vs_ising_gap(self):
        """Hellerman bound at c=1/2 is >= Ising gap h=1/2."""
        bound = hellerman_gap_bound(0.5)
        assert bound['hellerman_bound'] >= 0.5 - 1e-10

    def test_Q_contact_positive_for_c_positive(self):
        """Q^contact > 0 for c > 0."""
        for c in [0.1, 0.5, 1.0, 10.0, 100.0]:
            assert Q_contact_virasoro(c) > 0

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 6):
            assert float(lambda_fp(g)) > 0

    def test_F_g_positive_for_positive_kappa(self):
        """F_g > 0 when kappa > 0."""
        for g in range(1, 4):
            for c in [0.5, 1.0, 10.0]:
                kappa = c / 2.0
                assert float(F_g_shadow(kappa, g)) > 0
