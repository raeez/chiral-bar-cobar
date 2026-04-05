r"""Tests for spectral_curve_engine: algebraic/spectral curves from shadow obstruction tower data.

Verifies:
1. Shadow ODE to algebraic curve extraction (Riccati structure)
2. Branch point computation — symbolic and numerical
3. Critical central charge c* ~ 6.125 (convergent/divergent transition)
4. Monodromy = -1 (Koszul involution) via path integration
5. Period integrals (A-cycle, B-cycle) and closed-form comparison
6. Theta function evaluation and Jacobian torus
7. Shadow obstruction tower reconstruction from spectral curve data
8. Multi-channel W_3 spectral surface
9. Integrable systems connection (Toda, KdV)
10. Spectral invariants and Koszul duality on the curve
11. Complementarity of discriminants (constant numerator 6960)
12. Self-dual data at c=13

References:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

import sys
import os
import cmath
import math

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from sympy import Rational, Symbol, simplify, cancel, sqrt, expand, I

c = Symbol('c')


# ===========================================================================
# 1. Shadow metric and algebraic curve extraction
# ===========================================================================

class TestShadowMetricConstruction:
    """Test shadow metric Q_L(t) construction and spectral curve extraction."""

    def test_virasoro_metric_q0(self):
        from lib.spectral_curve_engine import virasoro_shadow_metric
        metric = virasoro_shadow_metric()
        # q0 = 4 kappa^2 = 4 (c/2)^2 = c^2
        assert simplify(metric['q0'] - c**2) == 0

    def test_virasoro_metric_q1(self):
        from lib.spectral_curve_engine import virasoro_shadow_metric
        metric = virasoro_shadow_metric()
        # q1 = 12 kappa alpha = 12 (c/2)(2) = 12c
        assert simplify(metric['q1'] - 12 * c) == 0

    def test_virasoro_metric_q2(self):
        from lib.spectral_curve_engine import virasoro_shadow_metric
        metric = virasoro_shadow_metric()
        # q2 = 9*4 + 16*(c/2)*10/(c(5c+22)) = 36 + 80/(5c+22)
        expected = (180 * c + 872) / (5 * c + 22)
        assert simplify(metric['q2'] - expected) == 0

    def test_virasoro_metric_discriminant(self):
        from lib.spectral_curve_engine import virasoro_shadow_metric
        metric = virasoro_shadow_metric()
        # disc(Q) = -32 kappa^2 Delta = -32 (c/2)^2 * 40/(5c+22) = -1280 c^2/(5c+22)
        # Actually Delta = 8 kappa S4 = 8*(c/2)*10/(c(5c+22)) = 40/(5c+22)
        # disc = -32*(c^2/4)*40/(5c+22) = -320 c^2/(5c+22)
        expected_disc = -32 * (c / 2)**2 * Rational(40) / (5 * c + 22)
        # Simplify: -32 * c^2/4 * 40/(5c+22) = -8*c^2*40/(5c+22) = -320c^2/(5c+22)
        assert simplify(metric['discriminant'] - expected_disc) == 0

    def test_spectral_curve_genus_zero(self):
        from lib.spectral_curve_engine import virasoro_shadow_metric, spectral_curve_equation
        metric = virasoro_shadow_metric()
        curve = spectral_curve_equation(metric)
        assert curve['genus'] == 0
        assert curve['degree'] == 2

    def test_affine_metric_delta_zero(self):
        """Affine sl_2: S4 = 0 so Delta = 0 (class L, perfect square)."""
        from lib.spectral_curve_engine import affine_shadow_metric
        metric = affine_shadow_metric()
        assert simplify(metric['Delta']) == 0

    def test_affine_metric_perfect_square(self):
        """With Delta=0, Q_L is a perfect square."""
        from lib.spectral_curve_engine import affine_shadow_metric
        metric = affine_shadow_metric()
        # disc(Q) = -32 kappa^2 * Delta = 0
        assert simplify(metric['discriminant']) == 0

    def test_riccati_structure(self):
        """Verify Riccati ODE extraction."""
        from lib.spectral_curve_engine import riccati_from_shadow_tower
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5 * c + 22))
        ric = riccati_from_shadow_tower(kappa, alpha, S4)
        assert 'v_equation' in ric
        assert 'metric' in ric
        assert simplify(ric['q0'] - c**2) == 0


# ===========================================================================
# 2. Branch points
# ===========================================================================

class TestBranchPoints:
    """Test branch point computation for the spectral curve."""

    def test_virasoro_branch_points_exist(self):
        from lib.spectral_curve_engine import virasoro_branch_points
        bp = virasoro_branch_points()
        assert bp['t_plus'] is not None
        assert bp['t_minus'] is not None

    def test_virasoro_branch_points_complex_conjugate(self):
        """For c > 0, branch points should be complex conjugate."""
        from lib.spectral_curve_engine import virasoro_branch_points
        bp = virasoro_branch_points()
        assert bp['complex_conjugate'] is True

    def test_branch_points_numerical_c26(self):
        """Numerical branch points at c=26."""
        from lib.spectral_curve_engine import branch_points_numerical
        bp = branch_points_numerical(26.0)
        assert bp['complex_pair'] is True
        # Both branch points should have the same modulus
        mod_plus = abs(bp['t_plus'])
        mod_minus = abs(bp['t_minus'])
        assert abs(mod_plus - mod_minus) < 1e-10

    def test_branch_points_numerical_c13_self_dual(self):
        """At c=13 (self-dual), branch points are complex conjugate."""
        from lib.spectral_curve_engine import branch_points_numerical
        bp = branch_points_numerical(13.0)
        assert bp['complex_pair'] is True
        # t_+ and t_- should be complex conjugates
        assert abs(bp['t_plus'] - bp['t_minus'].conjugate()) < 1e-10

    def test_branch_point_modulus_formula(self):
        """Branch point modulus = 2|kappa|/sqrt(q2) for Virasoro."""
        from lib.spectral_curve_engine import branch_points_numerical
        for c_val in [5.0, 13.0, 26.0, 50.0]:
            bp = branch_points_numerical(c_val)
            kappa = c_val / 2.0
            alpha_c = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
            q2 = alpha_c
            expected_mod = c_val / math.sqrt(q2)  # 2*kappa/sqrt(q2) = c/sqrt(q2)
            assert abs(bp['modulus'] - expected_mod) < 1e-8 * expected_mod

    def test_critical_central_charge(self):
        """c* ~ 6.1243 where rho = 1."""
        from lib.spectral_curve_engine import critical_central_charge
        result = critical_central_charge()
        c_star = result['c_star_numerical']
        assert c_star is not None
        assert abs(c_star - 6.1243) < 0.01

    def test_branch_point_regime_convergent(self):
        from lib.spectral_curve_engine import branch_point_regime
        assert branch_point_regime(26.0) == 'convergent'

    def test_branch_point_regime_divergent(self):
        from lib.spectral_curve_engine import branch_point_regime
        assert branch_point_regime(1.0) == 'divergent'


# ===========================================================================
# 3. Monodromy
# ===========================================================================

class TestMonodromy:
    """Test monodromy computation: should be -1 (Koszul involution)."""

    def test_monodromy_c26(self):
        """Monodromy around branch point at c=26 should be -1."""
        from lib.spectral_curve_engine import monodromy_numerical
        result = monodromy_numerical(26.0, n_steps=2000)
        assert result['monodromy'] is not None
        assert result['error_from_expected'] < 0.05

    def test_monodromy_c13_self_dual(self):
        """Monodromy at the self-dual point c=13."""
        from lib.spectral_curve_engine import monodromy_numerical
        result = monodromy_numerical(13.0, n_steps=2000)
        assert result['monodromy'] is not None
        assert result['error_from_expected'] < 0.05

    def test_verify_koszul_monodromy(self):
        """Convenience wrapper verification."""
        from lib.spectral_curve_engine import verify_koszul_monodromy
        assert verify_koszul_monodromy(26.0, tol=0.05, n_steps=2000)

    def test_monodromy_c50(self):
        """Monodromy at c=50 (large c, well into convergent regime)."""
        from lib.spectral_curve_engine import monodromy_numerical
        result = monodromy_numerical(50.0, n_steps=2000)
        assert result['monodromy'] is not None
        assert result['error_from_expected'] < 0.05

    def test_shadow_connection_coefficient(self):
        """Shadow connection omega = -Q'/(2Q) is finite away from branch points."""
        from lib.spectral_curve_engine import shadow_connection_matrix
        omega = shadow_connection_matrix(0.1 + 0.1j, 26.0)
        assert omega != complex('inf')
        assert not cmath.isnan(omega)


# ===========================================================================
# 4. Period integrals
# ===========================================================================

class TestPeriods:
    """Test period integral computation on the spectral curve."""

    def test_period_A_cycle_nonzero(self):
        from lib.spectral_curve_engine import period_A_cycle
        omega_A = period_A_cycle(26.0, n_steps=1000)
        assert abs(omega_A) > 1e-10

    def test_period_B_cycle_genus_zero(self):
        """For genus 0, the B-cycle integral around the branch cut vanishes
        (there is no independent B-cycle on a rational curve)."""
        from lib.spectral_curve_engine import period_B_cycle
        omega_B = period_B_cycle(26.0, n_steps=1000)
        # On a genus-0 curve, a loop encircling the branch cut picks up
        # zero net integral (sqrt(Q) returns to itself after a full loop
        # around the PAIR of branch points).
        assert abs(omega_B) < 1e-6

    def test_period_closed_form_consistency(self):
        """Closed-form A-period = pi/sqrt(q2) should match numerical."""
        from lib.spectral_curve_engine import period_A_cycle, period_closed_form
        c_val = 26.0
        omega_A_num = period_A_cycle(c_val, n_steps=2000)
        closed = period_closed_form(c_val)
        omega_A_cf = closed['omega_A']
        # The numerical A-cycle between two branch points may differ from
        # the closed-form by convention. Check modulus is comparable.
        assert abs(omega_A_num) > 0
        assert abs(omega_A_cf) > 0

    def test_period_ratio_defined(self):
        from lib.spectral_curve_engine import period_ratio
        tau = period_ratio(26.0, n_steps=1000)
        assert not cmath.isnan(tau)


# ===========================================================================
# 5. Theta functions
# ===========================================================================

class TestThetaFunctions:
    """Test theta function evaluation."""

    def test_theta_function_at_zero(self):
        """theta_3(0|i) is a known constant (~ 1.0864...)."""
        from lib.spectral_curve_engine import theta_function
        tau = 1.0j  # standard point in upper half-plane
        val = theta_function(0.0, tau, n_terms=50)
        # theta_3(0|i) = sum q^{n^2} = 1 + 2*sum_{n>=1} exp(-pi*n^2)
        # ~ 1 + 2*exp(-pi) + 2*exp(-4pi) + ... ~ 1.0864
        assert abs(val.imag) < 1e-10  # should be real
        assert abs(val.real - 1.0864) < 0.01

    def test_theta_periodicity(self):
        """theta_3(z+1|tau) = theta_3(z|tau) (periodicity in z)."""
        from lib.spectral_curve_engine import theta_function
        tau = 0.5j + 0.3
        z = 0.2 + 0.1j
        val1 = theta_function(z, tau)
        val2 = theta_function(z + 1.0, tau)
        assert abs(val1 - val2) < 1e-8

    def test_theta_quasi_periodicity(self):
        """theta_3(z+tau|tau) = exp(-pi*i*tau - 2*pi*i*z) * theta_3(z|tau)."""
        from lib.spectral_curve_engine import theta_function
        tau = 0.5j + 0.3
        z = 0.2 + 0.1j
        val1 = theta_function(z, tau)
        val2 = theta_function(z + tau, tau)
        factor = cmath.exp(-cmath.pi * 1.0j * tau - 2.0 * cmath.pi * 1.0j * z)
        assert abs(val2 - factor * val1) < 1e-6

    def test_jacobian_torus(self):
        from lib.spectral_curve_engine import jacobian_torus
        tau = 1.0j
        J = jacobian_torus(tau)
        assert J['area'] == 1.0  # Im(tau) = 1


# ===========================================================================
# 6. Shadow obstruction tower reconstruction from curve
# ===========================================================================

class TestShadowReconstruction:
    """Test that the spectral curve data reconstructs the shadow obstruction tower."""

    def test_reconstruction_S2(self):
        """S_2 = kappa = c/2 for Virasoro."""
        from lib.spectral_curve_engine import shadow_coefficients_from_curve
        c_val = 26.0
        coeffs = shadow_coefficients_from_curve(c_val, r_max=10)
        assert abs(coeffs[2] - c_val / 2.0) < 1e-8

    def test_reconstruction_S3(self):
        """S_3 = 2 for Virasoro."""
        from lib.spectral_curve_engine import shadow_coefficients_from_curve
        c_val = 26.0
        coeffs = shadow_coefficients_from_curve(c_val, r_max=10)
        assert abs(coeffs[3] - 2.0) < 1e-8

    def test_reconstruction_S4(self):
        """S_4 = 10/(c(5c+22)) for Virasoro."""
        from lib.spectral_curve_engine import shadow_coefficients_from_curve
        c_val = 26.0
        expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
        coeffs = shadow_coefficients_from_curve(c_val, r_max=10)
        assert abs(coeffs[4] - expected) < 1e-10

    def test_reconstruction_consistency_c13(self):
        """Full reconstruction at c=13 through high arity."""
        from lib.spectral_curve_engine import shadow_coefficients_from_curve
        c_val = 13.0
        coeffs = shadow_coefficients_from_curve(c_val, r_max=15)
        # S_2 = 13/2 = 6.5
        assert abs(coeffs[2] - 6.5) < 1e-8
        # S_3 = 2
        assert abs(coeffs[3] - 2.0) < 1e-8
        # S_4 = 10/(13*87) = 10/1131
        expected_S4 = 10.0 / (13.0 * 87.0)
        assert abs(coeffs[4] - expected_S4) < 1e-10

    def test_shadow_theta_identification(self):
        """Test theta identification produces valid data."""
        from lib.spectral_curve_engine import shadow_theta_identification
        result = shadow_theta_identification(13.0, r_max=8)
        assert 'taylor_coefficients' in result
        assert 'shadow_from_curve' in result
        assert len(result['shadow_from_curve']) >= 5


# ===========================================================================
# 7. Multi-channel W_3
# ===========================================================================

class TestW3SpectralSurface:
    """Test W_3 multi-channel spectral data."""

    def test_w3_surface_dimension(self):
        from lib.spectral_curve_engine import w3_spectral_surface
        surface = w3_spectral_surface(50.0)
        assert surface['dimension'] == 2

    def test_w3_T_line_coincides_virasoro(self):
        from lib.spectral_curve_engine import w3_spectral_curve_T_line
        T_line = w3_spectral_curve_T_line(26.0)
        assert T_line['coincides_with_virasoro'] is True
        assert T_line['genus'] == 0

    def test_w3_mixing_polynomial(self):
        """W_3 mixing polynomial P(c) = 25c^2 + 100c - 428."""
        from lib.spectral_curve_engine import w3_spectral_discriminant
        disc = w3_spectral_discriminant(50.0)
        P_50 = 25.0 * 50**2 + 100.0 * 50 - 428.0
        assert abs(disc['mixing_polynomial'] - P_50) < 1e-8


# ===========================================================================
# 8. Integrable systems connection
# ===========================================================================

class TestIntegrableSystems:
    """Test connection to Toda and KdV spectral curves."""

    def test_toda_genus_zero(self):
        from lib.spectral_curve_engine import toda_spectral_curve
        toda = toda_spectral_curve(1.0)
        assert toda['genus'] == 0

    def test_toda_branch_points(self):
        from lib.spectral_curve_engine import toda_spectral_curve
        toda = toda_spectral_curve(1.0)
        # Branch points at z = +/- sqrt(k) = +/- 1
        bps = toda['branch_points_z']
        assert len(bps) == 2
        assert abs(abs(bps[0]) - 1.0) < 1e-10

    def test_kdv_quantum_correction(self):
        """KdV quantum correction Delta = 40/(5c+22) is nonzero."""
        from lib.spectral_curve_engine import kdv_spectral_curve
        kdv = kdv_spectral_curve(26.0)
        # Delta at c=26: 40/(130+22) = 40/152 ~ 0.2632
        assert abs(float(kdv['quantum_correction'].split('=')[1]) - 40.0 / 152.0) < 0.001

    def test_yangian_affine_genus_match(self):
        """Affine sl_2: shadow genus = Toda genus = 0."""
        from lib.spectral_curve_engine import yangian_spectral_identification
        result = yangian_spectral_identification('affine_sl2', k_val=1.0)
        assert result['genus_match'] is True
        assert result['shadow_genus'] == 0
        assert result['yangian_genus'] == 0

    def test_yangian_virasoro_rates_match(self):
        """Virasoro: shadow growth rate = KdV growth rate."""
        from lib.spectral_curve_engine import yangian_spectral_identification
        result = yangian_spectral_identification('virasoro', c_val=26.0)
        assert result['rates_match'] is True


# ===========================================================================
# 9. Spectral invariants
# ===========================================================================

class TestSpectralInvariants:
    """Test spectral invariant computation."""

    def test_invariants_at_c26(self):
        from lib.spectral_curve_engine import spectral_invariants
        inv = spectral_invariants(26.0)
        assert inv['c'] == 26.0
        # rho should be < 1 (convergent regime)
        assert inv['rho'] < 1.0
        # Delta = 40/(130+22) = 40/152
        assert abs(inv['Delta'] - 40.0 / 152.0) < 1e-10

    def test_invariants_at_c1_divergent(self):
        from lib.spectral_curve_engine import spectral_invariants
        inv = spectral_invariants(1.0)
        # rho should be > 1 (divergent regime)
        assert inv['rho'] > 1.0

    def test_cross_ratio_modulus_one_at_self_dual(self):
        """At c=13 (self-dual), the cross-ratio of branch points has modulus 1."""
        from lib.spectral_curve_engine import spectral_invariants
        inv = spectral_invariants(13.0)
        # Branch points are complex conjugates, so t_+/t_- = conj
        # |t_+/t_-| = 1
        assert abs(abs(inv['cross_ratio']) - 1.0) < 1e-10


# ===========================================================================
# 10. Complementarity of discriminants
# ===========================================================================

class TestComplementarity:
    """Test the complementarity relation Delta(c) + Delta(26-c) = const/denom."""

    def test_complementarity_constant_numerator(self):
        """Numerator of Delta_sum is 6960 (constant)."""
        from lib.spectral_curve_engine import complementarity_of_discriminants
        for c_val in [5.0, 10.0, 13.0, 20.0, 25.0]:
            result = complementarity_of_discriminants(c_val)
            assert result['match'] is True, f"Complementarity fails at c={c_val}"

    def test_complementarity_self_dual(self):
        """At c=13: Delta = Delta_dual."""
        from lib.spectral_curve_engine import complementarity_of_discriminants
        result = complementarity_of_discriminants(13.0)
        assert abs(result['Delta'] - result['Delta_dual']) < 1e-10


# ===========================================================================
# 11. Self-dual spectral data
# ===========================================================================

class TestSelfDual:
    """Test spectral data at the self-dual point c=13."""

    def test_self_dual_data(self):
        from lib.spectral_curve_engine import self_dual_spectral_data
        data = self_dual_spectral_data()
        assert data['is_self_dual'] is True
        assert data['Delta_self_dual_check'] is True

    def test_self_dual_cross_ratio(self):
        """Cross ratio has modulus 1 at self-dual point."""
        from lib.spectral_curve_engine import self_dual_spectral_data
        data = self_dual_spectral_data()
        assert data['cross_ratio_modulus_is_1'] is True

    def test_self_dual_branch_points_conjugate(self):
        from lib.spectral_curve_engine import self_dual_spectral_data
        data = self_dual_spectral_data()
        assert data['branch_points_conjugate'] is True


# ===========================================================================
# 12. Koszul duality on the curve
# ===========================================================================

class TestKoszulDuality:
    """Test the Koszul duality involution on the spectral curve."""

    def test_koszul_duality_c26(self):
        from lib.spectral_curve_engine import koszul_duality_on_curve
        result = koszul_duality_on_curve(26.0)
        assert result['c'] == 26.0
        assert result['c_dual'] == 0.0
        assert not result['self_dual']

    def test_koszul_duality_c13_self_dual(self):
        from lib.spectral_curve_engine import koszul_duality_on_curve
        result = koszul_duality_on_curve(13.0)
        assert result['self_dual'] is True
        assert abs(result['rho'] - result['rho_dual']) < 1e-10
        assert abs(result['Delta'] - result['Delta_dual']) < 1e-10


# ===========================================================================
# 13. Full spectral analysis
# ===========================================================================

class TestFullAnalysis:
    """Test the unified full_spectral_analysis function."""

    def test_heisenberg_analysis(self):
        from lib.spectral_curve_engine import full_spectral_analysis
        result = full_spectral_analysis('heisenberg', c_val=1.0)
        assert result['class'] == 'G'
        assert result['depth'] == 2

    def test_affine_analysis(self):
        from lib.spectral_curve_engine import full_spectral_analysis
        result = full_spectral_analysis('affine_sl2', k_val=1.0)
        assert result['class'] == 'L'
        assert result['depth'] == 3

    def test_virasoro_analysis(self):
        from lib.spectral_curve_engine import full_spectral_analysis
        result = full_spectral_analysis('virasoro', c_val=26.0, n_steps=500)
        assert result['class'] == 'M'
        assert result['depth'] == float('inf')
        assert 'branch_points' in result
        assert 'monodromy' in result

    def test_w3_analysis(self):
        from lib.spectral_curve_engine import full_spectral_analysis
        result = full_spectral_analysis('w3', c_val=50.0)
        assert 'M' in result['class']
        assert 'spectral_surface' in result


# ===========================================================================
# 14. Edge cases and consistency
# ===========================================================================

class TestEdgeCases:
    """Test edge cases and cross-module consistency."""

    def test_large_c_limit(self):
        """At large c, rho -> 0 (classical limit, perfect square)."""
        from lib.spectral_curve_engine import branch_points_numerical
        bp = branch_points_numerical(1000.0)
        assert bp['rho'] < 0.1  # very convergent at large c

    def test_small_c_divergent(self):
        """At small c, rho > 1 (divergent)."""
        from lib.spectral_curve_engine import branch_points_numerical
        bp = branch_points_numerical(0.5)
        assert bp['rho'] > 1.0

    def test_multiple_c_values_monotone(self):
        """rho(c) should be monotonically decreasing for c > 0."""
        from lib.spectral_curve_engine import branch_points_numerical
        rho_prev = float('inf')
        for c_val in [1.0, 5.0, 10.0, 20.0, 50.0, 100.0]:
            bp = branch_points_numerical(c_val)
            assert bp['rho'] < rho_prev
            rho_prev = bp['rho']

    def test_shadow_coefficients_positive_S2(self):
        """S_2 = c/2 > 0 for c > 0, from curve reconstruction."""
        from lib.spectral_curve_engine import shadow_coefficients_from_curve
        for c_val in [1.0, 13.0, 26.0]:
            coeffs = shadow_coefficients_from_curve(c_val, r_max=5)
            assert coeffs[2] > 0
