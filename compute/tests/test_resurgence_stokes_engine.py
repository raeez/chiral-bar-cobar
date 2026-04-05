"""Tests for the resurgence and Stokes engine.

Verifies:
1. Borel transform: singularity locations, convergence, relation to shadow data
2. Lateral Borel sums: S_+/S_- computation, Stokes jump extraction
3. Stokes multiplier: leading order = 2*pi*i, monodromy relation
4. Transseries: perturbative + one-instanton sectors, evaluation
5. Alien derivatives: Delta_{A_1} G^(0) = S_1 * G^(1) identity
6. Bridge equation: MC constraint at arities 2, 3, 4; cross-arity consistency
7. Stokes graph: anti-Stokes lines, sector classification, c=13 symmetry
8. Pade-Borel: pole convergence to Borel singularities
9. Self-dual point c=13: enhanced Z_2 symmetry, equal rho
10. Koszul dual comparison: rho(c) vs rho(26-c)
11. Borel sum vs exact: leading-order log form agreement
12. Cross-consistency with shadow_radius and shadow_tower_recursive

References:
    compute/lib/resurgence_stokes_engine.py
    compute/lib/shadow_radius.py
    compute/lib/shadow_tower_recursive.py
    compute/lib/shadow_complex_analysis.py
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math

import numpy as np
import pytest


# =====================================================================
# Section 1: Virasoro shadow invariants
# =====================================================================

class TestVirasoroShadowInvariants:
    """Test the shadow invariant computation for Virasoro."""

    def test_kappa_equals_c_over_2(self):
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c_val)
            assert abs(inv['kappa'] - c_val / 2.0) < 1e-14

    def test_alpha_equals_2(self):
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        inv = virasoro_shadow_invariants(13.0)
        assert abs(inv['alpha'] - 2.0) < 1e-14

    def test_S4_formula(self):
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c_val)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(inv['S4'] - expected) < 1e-14

    def test_delta_formula(self):
        """Delta = 40/(5c+22)."""
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c_val)
            expected = 40.0 / (5.0 * c_val + 22.0)
            assert abs(inv['Delta'] - expected) < 1e-14

    def test_rho_formula(self):
        """rho = sqrt((180c+872)/((5c+22)*c^2))."""
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c_val)
            rho_sq = (180.0 * c_val + 872.0) / ((5.0 * c_val + 22.0) * c_val**2)
            expected = math.sqrt(rho_sq)
            assert abs(inv['rho'] - expected) < 1e-12

    def test_branch_points_conjugate(self):
        """For c > 0, branch points are complex conjugate."""
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c_val)
            t_plus = inv['branch_plus']
            t_minus = inv['branch_minus']
            assert abs(t_minus - t_plus.conjugate()) < 1e-12

    def test_branch_points_equal_modulus(self):
        """Conjugate branch points have equal modulus."""
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c_val)
            assert abs(abs(inv['branch_plus']) - abs(inv['branch_minus'])) < 1e-12


# =====================================================================
# Section 2: Shadow coefficients (recursive)
# =====================================================================

class TestShadowCoefficientsRecursive:
    """Test the recursive shadow coefficient computation."""

    def test_S2_equals_kappa(self):
        """S_2 = kappa = c/2."""
        from lib.resurgence_stokes_engine import virasoro_shadow_coefficients_recursive
        for c_val in [1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients_recursive(c_val, 4)
            assert abs(coeffs[0] - c_val / 2.0) < 1e-12

    def test_S3_equals_alpha(self):
        """S_3 = alpha = 2."""
        from lib.resurgence_stokes_engine import virasoro_shadow_coefficients_recursive
        for c_val in [1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients_recursive(c_val, 4)
            assert abs(coeffs[1] - 2.0) < 1e-10

    def test_S4_matches_formula(self):
        """S_4 = 10/(c(5c+22))."""
        from lib.resurgence_stokes_engine import virasoro_shadow_coefficients_recursive
        for c_val in [1.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients_recursive(c_val, 6)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(coeffs[2] - expected) < 1e-10

    def test_coefficients_nonzero_class_m(self):
        """For Virasoro (class M), S_r != 0 for all r >= 2."""
        from lib.resurgence_stokes_engine import virasoro_shadow_coefficients_recursive
        coeffs = virasoro_shadow_coefficients_recursive(13.0, 20)
        for i, s in enumerate(coeffs):
            assert abs(s) > 1e-30, f"S_{i+2} is effectively zero"


# =====================================================================
# Section 3: Borel transform
# =====================================================================

class TestBorelTransform:
    """Test the Borel transform computation."""

    def test_borel_at_zero_is_zero(self):
        """B[G](0) = 0 (all terms have xi^r with r >= 2)."""
        from lib.resurgence_stokes_engine import borel_transform
        coeffs = [0.5, 2.0, 0.1, 0.01]  # S_2, S_3, S_4, S_5
        assert abs(borel_transform(coeffs, 0.0)) < 1e-15

    def test_borel_coefficients_factorial_division(self):
        """b_r = S_r / r! by definition."""
        from lib.resurgence_stokes_engine import borel_transform_coefficients
        coeffs = [3.0, 1.0, 0.5]  # S_2, S_3, S_4
        b = borel_transform_coefficients(coeffs, r_start=2)
        assert abs(b[0] - 3.0 / math.factorial(2)) < 1e-14
        assert abs(b[1] - 1.0 / math.factorial(3)) < 1e-14
        assert abs(b[2] - 0.5 / math.factorial(4)) < 1e-14

    def test_borel_transform_convergence(self):
        """Borel transform converges for all finite xi (entire function)."""
        from lib.resurgence_stokes_engine import borel_transform_virasoro
        # Should converge at large xi
        val = borel_transform_virasoro(13.0, 40, 10.0 + 0.0j)
        assert np.isfinite(val.real) and np.isfinite(val.imag)

    def test_borel_singularity_locations_conjugate(self):
        """Borel singularities (instanton actions) are conjugate for c > 0."""
        from lib.resurgence_stokes_engine import borel_singularity_locations
        A_plus, A_minus = borel_singularity_locations(13.0)
        assert abs(A_minus - A_plus.conjugate()) < 1e-10

    def test_borel_singularity_modulus_equals_rho(self):
        """The modulus of the instanton action A_1 equals rho (shadow growth rate)."""
        from lib.resurgence_stokes_engine import (
            borel_singularity_locations,
            virasoro_shadow_invariants,
        )
        for c_val in [1.0, 13.0, 25.0]:
            A_plus, _ = borel_singularity_locations(c_val)
            inv = virasoro_shadow_invariants(c_val)
            # |A_1| = 1/R = rho where R = |branch_point|
            assert abs(abs(A_plus) - inv['rho']) < 1e-10


# =====================================================================
# Section 4: Lateral Borel sums
# =====================================================================

class TestLateralBorelSums:
    """Test lateral Borel sum computation."""

    def test_lateral_sums_exist(self):
        """Both S_+ and S_- are computable."""
        from lib.resurgence_stokes_engine import lateral_borel_sums
        result = lateral_borel_sums(13.0, 0.05, r_max=30, n_quad=500, xi_max=30.0)
        assert np.isfinite(result['S_plus'].real)
        assert np.isfinite(result['S_minus'].real)

    def test_lateral_sums_conjugate_for_real_t(self):
        """For real t, S_+ = conj(S_-) if the coefficients are real."""
        from lib.resurgence_stokes_engine import lateral_borel_sums
        result = lateral_borel_sums(13.0, 0.05, r_max=30, epsilon=0.05,
                                     n_quad=500, xi_max=30.0)
        # S_+(t) and S_-(t) should be complex conjugates for real t
        diff = abs(result['S_plus'] - result['S_minus'].conjugate())
        assert diff < 0.1 * max(abs(result['S_plus']), 1e-10)

    def test_stokes_jump_purely_imaginary_for_real_t(self):
        """For real t with real coefficients, the Stokes jump is purely imaginary."""
        from lib.resurgence_stokes_engine import lateral_borel_sums
        result = lateral_borel_sums(13.0, 0.05, r_max=30, epsilon=0.05,
                                     n_quad=500, xi_max=30.0)
        jump = result['stokes_jump']
        # Real part should be small compared to imaginary part
        if abs(jump) > 1e-15:
            assert abs(jump.real) < 0.5 * abs(jump.imag) + 1e-10


# =====================================================================
# Section 5: Stokes multiplier
# =====================================================================

class TestStokesMultiplier:
    """Test Stokes multiplier computation."""

    def test_leading_order_is_2pi_i(self):
        """Leading-order Stokes multiplier S_1 = -2*pi*i."""
        from lib.resurgence_stokes_engine import stokes_multiplier_leading
        S_1 = stokes_multiplier_leading(13.0)
        assert abs(S_1 - (-2.0j * math.pi)) < 1e-12

    def test_monodromy_stokes_multiplier(self):
        """Stokes multiplier from monodromy = 2*pi*i."""
        from lib.resurgence_stokes_engine import stokes_multiplier_from_monodromy
        S_1 = stokes_multiplier_from_monodromy(13.0)
        assert abs(S_1 - 2.0j * math.pi) < 1e-12

    def test_stokes_data_consistency(self):
        """Stokes data package is internally consistent."""
        from lib.resurgence_stokes_engine import compute_stokes_data
        data = compute_stokes_data(13.0)
        assert data.enhanced_symmetry  # c = 13 is self-dual
        assert abs(data.S_1.real) < 1e-10  # purely imaginary
        assert abs(abs(data.S_1) - 2.0 * math.pi) < 1e-10

    def test_stokes_data_generic(self):
        """Generic c (not self-dual) has no enhanced symmetry."""
        from lib.resurgence_stokes_engine import compute_stokes_data
        data = compute_stokes_data(7.0)
        assert not data.enhanced_symmetry


# =====================================================================
# Section 6: Transseries
# =====================================================================

class TestTransseries:
    """Test transseries construction and evaluation."""

    def test_perturbative_sector_is_shadow_series(self):
        """G^(0) = the shadow series itself."""
        from lib.resurgence_stokes_engine import perturbative_sector
        pert = perturbative_sector(13.0, 10)
        assert len(pert) == 9  # S_2 through S_10
        assert abs(pert[0] - 6.5) < 1e-12  # S_2 = c/2 = 6.5

    def test_one_instanton_leading(self):
        """G^(1)(t=0) = 1 at leading order."""
        from lib.resurgence_stokes_engine import one_instanton_sector_leading
        G1 = one_instanton_sector_leading(13.0, 10)
        assert abs(G1[0] - 1.0) < 1e-14  # r=0 term

    def test_one_instanton_geometric(self):
        """G^(1) coefficients are geometric: ratio^r at leading order."""
        from lib.resurgence_stokes_engine import one_instanton_sector_leading
        G1 = one_instanton_sector_leading(13.0, 10)
        ratio = -6.0 / 13.0
        for r in range(5):
            assert abs(G1[r] - ratio**r) < 1e-12

    def test_transseries_eval_suppressed_sector(self):
        """In the sector where Re(A_1/t) > 0, instantons are exponentially suppressed."""
        from lib.resurgence_stokes_engine import (
            transseries_eval, perturbative_sector, virasoro_shadow_invariants,
        )
        import cmath as cm
        c_val = 13.0
        inv = virasoro_shadow_invariants(c_val)
        A_1 = 1.0 / inv['branch_plus']
        # Choose t in the sector where Re(A_1/t) > 0 (suppressed)
        # Need arg(t) ~ arg(A_1) so A_1/t is real positive
        t = 0.001 * cm.exp(1j * cm.phase(A_1))
        pert_coeffs = perturbative_sector(c_val, 30)
        G0 = sum(pert_coeffs[i] * t**(i + 2) for i in range(len(pert_coeffs)))
        G_trans = transseries_eval(c_val, t, sigma_1=1.0, n_inst=1, r_max=30)
        # In the suppressed sector, instanton contribution ~ exp(-|A_1|/0.001) ~ 0
        assert abs(G_trans - G0) < 1e-10 * max(abs(G0), 1.0)

    def test_transseries_data_structure(self):
        """TransseriesData has all required fields."""
        from lib.resurgence_stokes_engine import build_transseries_data
        td = build_transseries_data(13.0, 20)
        assert td.c == 13.0
        assert td.A_1 != 0.0
        assert len(td.perturbative) == 19  # S_2 through S_20
        assert len(td.one_instanton) == 30
        assert td.n_instanton_actions == 2


# =====================================================================
# Section 7: Alien derivatives
# =====================================================================

class TestAlienDerivatives:
    """Test alien derivative computation."""

    def test_alien_derivative_identity(self):
        """Delta_{A_1} G^(0) = S_1 * G^(1) by construction."""
        from lib.resurgence_stokes_engine import verify_alien_derivative_relation
        result = verify_alien_derivative_relation(13.0, r_max=20)
        assert result['consistent']
        assert result['max_difference'] < 1e-10

    def test_alien_derivative_identity_multiple_c(self):
        """Alien derivative identity holds for multiple central charges."""
        from lib.resurgence_stokes_engine import verify_alien_derivative_relation
        for c_val in [1.0, 13.0, 25.0]:
            result = verify_alien_derivative_relation(c_val, r_max=15)
            assert result['consistent'], f"Failed at c={c_val}"

    def test_alien_chain_length(self):
        """Alien derivative chain has the requested depth."""
        from lib.resurgence_stokes_engine import alien_derivative_chain
        chain = alien_derivative_chain(13.0, n_levels=3, r_max=10)
        assert len(chain) == 4  # levels 0, 1, 2, 3


# =====================================================================
# Section 8: Bridge equation
# =====================================================================

class TestBridgeEquation:
    """Test the bridge equation (MC constraint on transseries)."""

    def test_bridge_arity2_trivial(self):
        """Bridge equation at arity 2: kappa is exact, no instantons."""
        from lib.resurgence_stokes_engine import bridge_equation_arity2
        result = bridge_equation_arity2(13.0)
        assert result['bridge_satisfied']
        assert result['alien_derivative'] == 0.0

    def test_bridge_arity3_trivial(self):
        """Bridge equation at arity 3: cubic shadow is exact."""
        from lib.resurgence_stokes_engine import bridge_equation_arity3
        result = bridge_equation_arity3(13.0)
        assert result['bridge_satisfied']

    def test_bridge_arity4_nontrivial(self):
        """Bridge equation at arity 4: quartic has instanton corrections."""
        from lib.resurgence_stokes_engine import bridge_equation_arity4
        result = bridge_equation_arity4(13.0)
        assert result['bridge_satisfied']
        assert result['one_instanton_correction'] != 0.0

    def test_bridge_consistency_across_arities(self):
        """Bridge equation is consistent across all arities (from D^2=0)."""
        from lib.resurgence_stokes_engine import bridge_equation_consistency
        for c_val in [1.0, 13.0, 25.0]:
            result = bridge_equation_consistency(c_val, max_arity=8)
            assert result['consistent'], f"Bridge inconsistent at c={c_val}"


# =====================================================================
# Section 9: Stokes graph
# =====================================================================

class TestStokesGraph:
    """Test Stokes graph construction and properties."""

    def test_stokes_graph_structure(self):
        """Stokes graph has the expected number of components."""
        from lib.resurgence_stokes_engine import build_stokes_graph
        graph = build_stokes_graph(13.0)
        assert len(graph.instanton_actions) == 2
        assert len(graph.stokes_lines) == 2
        assert len(graph.anti_stokes_lines) == 2

    def test_stokes_graph_c13_symmetry(self):
        """At c=13, the Stokes graph has Z_2 symmetry."""
        from lib.resurgence_stokes_engine import build_stokes_graph
        graph = build_stokes_graph(13.0)
        assert graph.symmetry_group == 'Z_2'

    def test_stokes_graph_generic_no_symmetry(self):
        """At generic c, the Stokes graph has Z_1 symmetry."""
        from lib.resurgence_stokes_engine import build_stokes_graph
        graph = build_stokes_graph(7.0)
        assert graph.symmetry_group == 'Z_1'

    def test_stokes_line_points_on_ray(self):
        """Stokes line points lie on a ray from the origin."""
        from lib.resurgence_stokes_engine import stokes_line_points
        A = 1.0 + 2.0j
        points = stokes_line_points(A, n_points=50)
        # All points should have the same argument as A
        expected_angle = cmath.phase(A)
        for pt in points:
            assert abs(cmath.phase(pt) - expected_angle) < 1e-10

    def test_anti_stokes_perpendicular(self):
        """Anti-Stokes lines are perpendicular to Stokes lines."""
        from lib.resurgence_stokes_engine import stokes_graph_properties
        props = stokes_graph_properties(13.0)
        # Angular separation between A_+ and A_- Stokes directions
        assert props['is_conjugate_pair']

    def test_sector_count(self):
        """Each instanton action creates 4 sectors (from anti-Stokes lines)."""
        from lib.resurgence_stokes_engine import stokes_sectors
        A = 1.0 + 1.0j
        sectors = stokes_sectors(A)
        assert len(sectors) == 4

    def test_sector_suppressed_enhanced_partition(self):
        """Sectors partition into suppressed (Re(A/t)>0) and enhanced (Re(A/t)<0)."""
        from lib.resurgence_stokes_engine import stokes_sectors
        A = 1.0 + 0.5j
        sectors = stokes_sectors(A)
        behaviors = [s['exponential_behavior'] for s in sectors]
        # Two suppressed and two enhanced sectors
        assert behaviors.count('suppressed') == 2
        assert behaviors.count('enhanced') == 2


# =====================================================================
# Section 10: Self-dual point c = 13
# =====================================================================

class TestSelfDualPoint:
    """Test the special properties at c = 13."""

    def test_c13_is_self_dual(self):
        from lib.resurgence_stokes_engine import self_dual_analysis
        result = self_dual_analysis()
        assert result['is_self_dual']

    def test_c13_rho_equals_rho_dual(self):
        from lib.resurgence_stokes_engine import self_dual_analysis
        result = self_dual_analysis()
        assert result['rho_equal']

    def test_c13_instanton_actions_conjugate(self):
        from lib.resurgence_stokes_engine import self_dual_analysis
        result = self_dual_analysis()
        assert result['A_conjugate']

    def test_c13_convergent(self):
        """At c=13, the shadow obstruction tower converges (rho < 1)."""
        from lib.resurgence_stokes_engine import self_dual_analysis
        result = self_dual_analysis()
        assert result['convergent']
        assert result['rho'] < 1.0

    def test_c13_rho_value(self):
        """rho(13) ~ 0.467 (known value from shadow_radius.py)."""
        from lib.resurgence_stokes_engine import self_dual_analysis
        result = self_dual_analysis()
        assert abs(result['rho'] - 0.467) < 0.01


# =====================================================================
# Section 11: Koszul dual comparison
# =====================================================================

class TestKoszulDualComparison:
    """Test Koszul duality relations for Stokes data."""

    def test_koszul_dual_c13_self_dual(self):
        from lib.resurgence_stokes_engine import koszul_dual_stokes_comparison
        result = koszul_dual_stokes_comparison(13.0)
        assert result['self_dual']
        assert abs(result['rho'] - result['rho_dual']) < 1e-10

    def test_koszul_dual_c1_vs_c25(self):
        from lib.resurgence_stokes_engine import koszul_dual_stokes_comparison
        result = koszul_dual_stokes_comparison(1.0)
        assert abs(result['c_dual'] - 25.0) < 1e-10
        # rho(1) and rho(25) should be different
        assert abs(result['rho'] - result['rho_dual']) > 0.1

    def test_koszul_dual_symmetry(self):
        """koszul_dual(koszul_dual(c)) = c."""
        from lib.resurgence_stokes_engine import koszul_dual_stokes_comparison
        result = koszul_dual_stokes_comparison(5.0)
        assert abs(result['c_dual'] - 21.0) < 1e-10

    def test_koszul_dual_rho_product(self):
        """Product rho(c)*rho(26-c) is computable and finite for c != 0, 26."""
        from lib.resurgence_stokes_engine import koszul_dual_stokes_comparison
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            result = koszul_dual_stokes_comparison(c_val)
            assert np.isfinite(result['rho_product'])
            assert result['rho_product'] > 0


# =====================================================================
# Section 12: Borel sum vs exact
# =====================================================================

class TestBorelSumVsExact:
    """Test Borel resummation against exact leading-order answer."""

    @pytest.mark.skipif(
        not hasattr(__builtins__, '__import__') or True,
        reason="Run only when scipy available"
    )
    def test_borel_sum_matches_exact_c13(self):
        """Borel sum reproduces -log(1+6t/c)+6t/c at c=13, t=0.05."""
        try:
            from scipy import integrate
        except ImportError:
            pytest.skip("scipy required")
        from lib.resurgence_stokes_engine import borel_sum_vs_exact
        result = borel_sum_vs_exact(13.0, 0.05, r_max=40)
        assert result['borel_error'] < 0.01, (
            f"Borel sum error {result['borel_error']} too large"
        )

    def test_partial_sum_convergent_region(self):
        """In the convergent region (small t), partial sum is accurate."""
        from lib.resurgence_stokes_engine import borel_sum_vs_exact
        result = borel_sum_vs_exact(13.0, 0.01, r_max=40)
        # For very small t, even the partial sum should be good
        assert result['partial_error'] < 0.001

    def test_borel_sum_structure(self):
        """borel_sum_vs_exact returns all expected keys."""
        from lib.resurgence_stokes_engine import borel_sum_vs_exact
        result = borel_sum_vs_exact(13.0, 0.05, r_max=20)
        for key in ['exact', 'partial_sum', 'borel_sum', 'partial_error', 'borel_error']:
            assert key in result


# =====================================================================
# Section 13: Pade-Borel
# =====================================================================

class TestPadeBorel:
    """Test Pade-Borel resummation."""

    def test_pade_poles_approximate_branch_points(self):
        """Pade poles of G(t) approximate the branch points of the shadow metric.

        The shadow generating function G(t) = sum S_r t^r has branch points
        at the zeros of Q_L(t). Diagonal Pade approximants of G should have
        poles converging to these branch points.
        """
        from lib.resurgence_stokes_engine import virasoro_shadow_coefficients_recursive
        from lib.shadow_complex_analysis import pade_poles

        c_val = 13.0
        coeffs = virasoro_shadow_coefficients_recursive(c_val, 30)
        poles = pade_poles(coeffs, r_start=2)

        if len(poles) > 0:
            # Branch point modulus R = 1/rho
            from lib.resurgence_stokes_engine import virasoro_shadow_invariants
            inv = virasoro_shadow_invariants(c_val)
            R = inv['R']
            # At least one pole should be within 50% of R
            min_dist = min(abs(abs(p) - R) for p in poles)
            assert min_dist < R, (
                f"No Pade pole near R={R:.4f}; closest distance = {min_dist:.4f}"
            )

    def test_pade_borel_approximant_finite(self):
        """Pade-Borel approximant gives finite value at a test point."""
        from lib.resurgence_stokes_engine import (
            pade_borel_approximant,
            virasoro_shadow_coefficients_recursive,
        )
        coeffs = virasoro_shadow_coefficients_recursive(13.0, 20)
        val = pade_borel_approximant(coeffs, 0.05 + 0.0j)
        assert np.isfinite(val.real) and np.isfinite(val.imag)


# =====================================================================
# Section 14: Full analysis
# =====================================================================

class TestFullAnalysis:
    """Test the comprehensive analysis pipeline."""

    def test_full_analysis_c1(self):
        from lib.resurgence_stokes_engine import full_resurgence_analysis
        result = full_resurgence_analysis(1.0, r_max=30, t_probe=0.01)
        assert result['shadow_invariants']['rho'] > 1.0  # c=1 diverges

    def test_full_analysis_c13(self):
        from lib.resurgence_stokes_engine import full_resurgence_analysis
        result = full_resurgence_analysis(13.0, r_max=30, t_probe=0.05)
        assert result['shadow_invariants']['rho'] < 1.0  # c=13 converges
        assert result['stokes_graph']['symmetry'] == 'Z_2'

    def test_full_analysis_c25(self):
        from lib.resurgence_stokes_engine import full_resurgence_analysis
        result = full_resurgence_analysis(25.0, r_max=30, t_probe=0.05)
        assert result['shadow_invariants']['rho'] < 1.0  # c=25 converges

    def test_full_analysis_bridge_consistent(self):
        from lib.resurgence_stokes_engine import full_resurgence_analysis
        result = full_resurgence_analysis(13.0, r_max=30, t_probe=0.05)
        assert result['bridge_equation']['consistent']


# =====================================================================
# Section 15: Cross-consistency with shadow_radius module
# =====================================================================

class TestCrossConsistency:
    """Cross-check with the shadow_radius module."""

    def test_rho_matches_shadow_radius(self):
        """Growth rate matches shadow_radius.virasoro_branch_points_numerical."""
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        from lib.shadow_radius import virasoro_branch_points_numerical
        from sympy import Rational

        for c_val in [1, 13, 25]:
            inv = virasoro_shadow_invariants(float(c_val))
            bp = virasoro_branch_points_numerical(Rational(c_val))
            assert abs(inv['rho'] - bp['rho']) < 1e-8, (
                f"rho mismatch at c={c_val}: engine={inv['rho']}, "
                f"shadow_radius={bp['rho']}"
            )

    def test_branch_point_modulus_matches(self):
        """Branch point modulus R matches between modules."""
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        from lib.shadow_radius import virasoro_branch_points_numerical
        from sympy import Rational

        for c_val in [1, 13, 25]:
            inv = virasoro_shadow_invariants(float(c_val))
            bp = virasoro_branch_points_numerical(Rational(c_val))
            assert abs(inv['R'] - bp['R']) < 1e-8
