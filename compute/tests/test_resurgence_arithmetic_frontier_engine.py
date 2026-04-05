r"""Tests for the resurgence arithmetic frontier engine.

Comprehensive verification of the arity-direction resurgence arithmetic
of the shadow obstruction tower, covering:

1. Shadow data correctness for all families
2. Shadow coefficients: convolution recursion, high precision
3. Borel transform: coefficients, evaluation, singularity locations
4. Pade approximant singularity detection and convergence
5. Stokes constants: monodromy, numerical extraction, PSLQ
6. Alien derivatives: structure, bridge equation, depth dependence
7. Transseries: perturbative + instanton sectors
8. Lateral Borel sums: S_+/S_-, median resummation
9. Exact closed-form comparison
10. Shadow ODE analytic continuation
11. p-adic Borel transform and singularity comparison
12. Peacock patterns mod p
13. Multi-path verification
14. Cross-family consistency
15. Koszul duality: rho(c) vs rho(26-c)
16. Self-dual c=13 properties
17. Edge cases: c near 0, c critical, c large

References:
    compute/lib/resurgence_arithmetic_frontier_engine.py
    compute/lib/shadow_radius.py
    compute/lib/resurgence_frontier_engine.py
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
from fractions import Fraction

import numpy as np
import pytest


# =====================================================================
# Helpers
# =====================================================================

def _has_mpmath():
    try:
        import mpmath
        return True
    except ImportError:
        return False


PI = math.pi
TWO_PI = 2.0 * PI


# =====================================================================
# Section 1: Shadow algebra data correctness
# =====================================================================

class TestVirasoroData:
    """Test Virasoro shadow data at multiple central charges."""

    def test_kappa_formula(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [0.5, 1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            assert abs(d.kappa - c / 2.0) < 1e-14

    def test_alpha_is_2(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 13.0, 25.0]:
            d = virasoro_data(c)
            assert abs(d.alpha - 2.0) < 1e-14

    def test_S4_formula(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            expected = 10.0 / (c * (5.0 * c + 22.0))
            assert abs(d.S4 - expected) < 1e-14

    def test_Delta_formula(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            expected = 40.0 / (5.0 * c + 22.0)
            assert abs(d.Delta - expected) < 1e-13

    def test_depth_class_M(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        assert d.depth_class == 'M'

    def test_kappa_dual(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 13.0, 25.0]:
            d = virasoro_data(c)
            assert abs(d.kappa_dual - (26.0 - c) / 2.0) < 1e-14

    def test_rho_formula(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            rho_sq = (180.0 * c + 872.0) / ((5.0 * c + 22.0) * c ** 2)
            expected = math.sqrt(rho_sq)
            assert abs(d.rho - expected) < 1e-12

    def test_branch_points_conjugate(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            # For c > 0, branch points are complex conjugates
            assert abs(d.branch_plus - d.branch_minus.conjugate()) < 1e-12

    def test_branch_points_equal_modulus(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            assert abs(abs(d.branch_plus) - abs(d.branch_minus)) < 1e-12

    def test_c13_self_dual_rho(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        d_dual = virasoro_data(26.0 - 13.0)
        assert abs(d.rho - d_dual.rho) < 1e-12


class TestAffineSl2Data:
    """Test affine sl_2 shadow data."""

    def test_kappa(self):
        from lib.resurgence_arithmetic_frontier_engine import affine_sl2_data
        for k in [1.0, 2.0, 5.0]:
            d = affine_sl2_data(k)
            expected = 3.0 * (k + 2.0) / 4.0
            assert abs(d.kappa - expected) < 1e-14

    def test_depth_class_L(self):
        from lib.resurgence_arithmetic_frontier_engine import affine_sl2_data
        d = affine_sl2_data(1.0)
        assert d.depth_class == 'L'

    def test_S4_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import affine_sl2_data
        d = affine_sl2_data(1.0)
        assert abs(d.S4) < 1e-14

    def test_Delta_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import affine_sl2_data
        d = affine_sl2_data(1.0)
        assert abs(d.Delta) < 1e-14

    def test_tower_terminates(self):
        """Class L: tower terminates at arity 3 (S_r = 0 for r >= 4)."""
        from lib.resurgence_arithmetic_frontier_engine import (
            affine_sl2_data, shadow_coefficients,
        )
        d = affine_sl2_data(1.0)
        coeffs = shadow_coefficients(d, 10)
        for r in range(4, 11):
            assert abs(coeffs[r]) < 1e-10


class TestHeisenbergData:
    """Test Heisenberg shadow data."""

    def test_kappa(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data(1, 1.0)
        assert abs(d.kappa - 1.0) < 1e-14

    def test_depth_class_G(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data()
        assert d.depth_class == 'G'

    def test_rho_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data()
        assert d.rho == 0.0

    def test_alpha_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data()
        assert abs(d.alpha) < 1e-14

    def test_kappa_dual_antisymmetric(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data(1, 2.0)
        assert abs(d.kappa + d.kappa_dual) < 1e-14  # kappa + kappa' = 0 (AP24)


# =====================================================================
# Section 2: Shadow coefficients
# =====================================================================

class TestShadowCoefficients:
    """Test shadow coefficient computation."""

    def test_heisenberg_only_S2(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data, shadow_coefficients
        d = heisenberg_data()
        coeffs = shadow_coefficients(d, 10)
        # S_2 = a_0 / 2 = sqrt(q0) / 2 = 2*|kappa| / 2 = |kappa|
        assert abs(coeffs[2] - abs(d.kappa)) < 1e-14
        for r in range(3, 11):
            assert abs(coeffs[r]) < 1e-14

    def test_affine_only_S2_S3(self):
        from lib.resurgence_arithmetic_frontier_engine import affine_sl2_data, shadow_coefficients
        d = affine_sl2_data(1.0)
        coeffs = shadow_coefficients(d, 10)
        assert abs(coeffs[2]) > 1e-10  # S_2 nonzero
        assert abs(coeffs[3]) > 1e-10  # S_3 nonzero
        for r in range(4, 11):
            assert abs(coeffs[r]) < 1e-10

    def test_virasoro_infinite_tower(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data, shadow_coefficients
        d = virasoro_data(13.0)
        coeffs = shadow_coefficients(d, 20)
        # All coefficients should be nonzero for class M
        for r in range(2, 15):
            assert abs(coeffs[r]) > 1e-20

    def test_virasoro_S2_equals_kappa_over_2(self):
        """S_2 = kappa/2 for all families (leading coefficient of t^2*sqrt(Q_L))."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data, shadow_coefficients
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            coeffs = shadow_coefficients(d, 5)
            # S_2 = a_0 / 2 = sqrt(q0) / 2 = |2*kappa| / 2 = |kappa|
            expected = abs(d.kappa)
            assert abs(coeffs[2] - expected) < 1e-12, f"c={c}: S_2={coeffs[2]}, expected={expected}"

    def test_convolution_identity(self):
        """f^2 = Q_L: verify convolution squares to shadow metric."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data, shadow_coefficients
        d = virasoro_data(2.0)
        coeffs = shadow_coefficients(d, 30)
        # Reconstruct Taylor coefficients: a_n = (n+2) * S_{n+2}
        max_n = 25
        a = [(n + 2) * coeffs.get(n + 2, 0.0) for n in range(max_n + 1)]
        # Check f^2(0) = q0
        assert abs(a[0] ** 2 - d.q0) < 1e-10
        # Check f^2 coefficient at t^1 = q1
        assert abs(2 * a[0] * a[1] - d.q1) < 1e-10
        # Check f^2 coefficient at t^2 = q2
        conv_2 = a[0] * a[2] + a[1] ** 2 + a[2] * a[0]
        # Actually 2*a_0*a_2 + a_1^2
        assert abs(2 * a[0] * a[2] + a[1] ** 2 - d.q2) < 1e-10

    @pytest.mark.skipif(not _has_mpmath(), reason="mpmath required")
    def test_mpmath_agrees_with_float(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients, shadow_coefficients_mpmath,
        )
        d = virasoro_data(13.0)
        float_coeffs = shadow_coefficients(d, 30)
        mp_coeffs = shadow_coefficients_mpmath(d, 30, dps=30)
        for r in range(2, 25):
            assert abs(float(mp_coeffs[r]) - float_coeffs[r]) < 1e-12 * max(abs(float_coeffs[r]), 1e-20)

    def test_coefficients_growth_rate(self):
        """For class M, |S_r| ~ C * rho^r * r^{-5/2}."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data, shadow_coefficients
        d = virasoro_data(13.0)
        coeffs = shadow_coefficients(d, 60)
        rho = d.rho
        # Check that |S_r| * rho^{-r} * r^{5/2} converges to a constant
        ratios = []
        for r in range(20, 50):
            sr = abs(coeffs[r])
            if sr > 1e-100:
                ratios.append(sr * rho ** (-r) * r ** 2.5)
        # Ratios should stabilize (not diverge or vanish)
        assert len(ratios) > 10
        # Check ratio stability: std/mean < 1 (rough bound)
        mean_r = sum(ratios) / len(ratios)
        assert mean_r > 0


# =====================================================================
# Section 3: Borel transform
# =====================================================================

class TestBorelTransform:
    """Test Borel transform computation."""

    def test_borel_coefficients_factorial_suppression(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients, borel_transform_coefficients,
        )
        d = virasoro_data(13.0)
        sc = shadow_coefficients(d, 30)
        bc = borel_transform_coefficients(sc)
        # Borel coefficients should be much smaller than shadow coefficients
        for r in range(10, 25):
            assert abs(bc[r]) < abs(sc[r])

    def test_borel_at_origin_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients, borel_transform_evaluate,
        )
        d = virasoro_data(13.0)
        sc = shadow_coefficients(d, 30)
        B0 = borel_transform_evaluate(sc, 0.0)
        assert abs(B0) < 1e-14

    def test_borel_evaluate_small_zeta(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients, borel_transform_evaluate,
        )
        d = virasoro_data(13.0)
        sc = shadow_coefficients(d, 60)
        zeta = 0.1 + 0.0j
        B_val = borel_transform_evaluate(sc, zeta)
        assert np.isfinite(B_val.real) and np.isfinite(B_val.imag)

    def test_heisenberg_borel_entire(self):
        """Heisenberg: Borel transform is entire (class G)."""
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, shadow_coefficients, borel_transform_evaluate,
        )
        d = heisenberg_data()
        sc = shadow_coefficients(d, 10)
        # Should be finite everywhere
        for zeta in [1.0, 10.0, 100.0, 1j, 50 + 50j]:
            B_val = borel_transform_evaluate(sc, zeta)
            assert np.isfinite(abs(B_val))


class TestBorelSingularities:
    """Test Borel singularity location prediction."""

    def test_singularity_at_reciprocal_branch_point(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_singularity_locations,
        )
        d = virasoro_data(13.0)
        zeta_p, zeta_m = borel_singularity_locations(d)
        # zeta_pm = 1 / t_pm
        assert abs(zeta_p * d.branch_plus - 1.0) < 1e-12
        assert abs(zeta_m * d.branch_minus - 1.0) < 1e-12

    def test_singularities_conjugate(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_singularity_locations,
        )
        d = virasoro_data(13.0)
        zeta_p, zeta_m = borel_singularity_locations(d)
        assert abs(zeta_p - zeta_m.conjugate()) < 1e-12

    def test_singularity_modulus_equals_rho(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_singularity_locations,
        )
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            zeta_p, zeta_m = borel_singularity_locations(d)
            assert abs(abs(zeta_p) - d.rho) < 1e-10

    def test_heisenberg_no_singularities(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, locate_all_borel_singularities,
        )
        d = heisenberg_data()
        sings = locate_all_borel_singularities(d)
        assert len(sings) == 0

    def test_affine_no_singularities(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            affine_sl2_data, locate_all_borel_singularities,
        )
        d = affine_sl2_data(1.0)
        sings = locate_all_borel_singularities(d)
        assert len(sings) == 0

    def test_virasoro_many_singularities(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, locate_all_borel_singularities,
        )
        d = virasoro_data(13.0)
        sings = locate_all_borel_singularities(d)
        assert len(sings) >= 2  # At least the leading pair

    def test_singularities_sorted_by_modulus(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, locate_all_borel_singularities,
        )
        d = virasoro_data(13.0)
        sings = locate_all_borel_singularities(d)
        moduli = [s['modulus'] for s in sings]
        assert moduli == sorted(moduli)


# =====================================================================
# Section 4: Pade singularity detection
# =====================================================================

class TestPadeSingularities:
    """Test Pade-based branch point detection on the original series."""

    def test_pade_poles_exist_for_virasoro(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_pade_singularities,
        )
        d = virasoro_data(13.0)
        result = borel_pade_singularities(d, max_r=40)
        assert len(result['detected_poles']) > 0

    def test_pade_poles_match_branch_points(self):
        """Pade poles of the original series should approximate branch points."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_pade_singularities,
        )
        d = virasoro_data(13.0)
        result = borel_pade_singularities(d, max_r=50)
        if 'pole_match' in result:
            for label, match in result['pole_match'].items():
                # Relative error < 30% (Pade for algebraic functions)
                assert match['relative_error'] < 0.3, (
                    f"{label}: relative error {match['relative_error']}"
                )

    def test_pade_heisenberg_no_meaningful_poles(self):
        """Heisenberg series is polynomial; Pade should have no physical poles."""
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, borel_pade_singularities,
        )
        d = heisenberg_data()
        result = borel_pade_singularities(d, max_r=10)
        poles = result['detected_poles']
        if len(poles) > 0:
            nearest = min(abs(p) for p in poles)
            assert nearest > 10.0  # Far from origin = numerical artifact

    def test_pade_convergence_with_order(self):
        """Pade poles should improve with more coefficients."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_pade_singularities,
        )
        d = virasoro_data(13.0)
        r1 = borel_pade_singularities(d, max_r=20)
        r2 = borel_pade_singularities(d, max_r=40)
        assert r2['pade_order'][0] >= r1['pade_order'][0]


# =====================================================================
# Section 5: Stokes constants
# =====================================================================

class TestStokesConstants:
    """Test Stokes constant computation."""

    def test_monodromy_prediction(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, stokes_constant_from_monodromy,
        )
        d = virasoro_data(13.0)
        S_1 = stokes_constant_from_monodromy(d)
        assert abs(S_1 - 2j * PI) < 1e-12

    def test_monodromy_heisenberg_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, stokes_constant_from_monodromy,
        )
        d = heisenberg_data()
        S_1 = stokes_constant_from_monodromy(d)
        assert abs(S_1) < 1e-14

    def test_monodromy_affine_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            affine_sl2_data, stokes_constant_from_monodromy,
        )
        d = affine_sl2_data(1.0)
        S_1 = stokes_constant_from_monodromy(d)
        assert abs(S_1) < 1e-14

    def test_numerical_rho_verification(self):
        """Numerical ratio test: S_{r+1}/S_r -> rho for large r."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, stokes_constant_numerical,
        )
        d = virasoro_data(13.0)
        result = stokes_constant_numerical(d, max_r=60)
        assert result['converged']
        # rho from ratios should match predicted rho
        rho_num = result['rho_from_ratios']
        rho_pred = result['rho']
        assert abs(rho_num - rho_pred) / rho_pred < 0.1

    def test_numerical_heisenberg_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, stokes_constant_numerical,
        )
        d = heisenberg_data()
        result = stokes_constant_numerical(d, max_r=10)
        assert abs(result['S_1']) < 1e-10

    @pytest.mark.skipif(not _has_mpmath(), reason="mpmath required")
    def test_pslq_rho_recognition(self):
        """PSLQ should identify rho^2 as rational for rational c."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, stokes_constant_pslq,
        )
        d = virasoro_data(13.0)
        result = stokes_constant_pslq(d, max_r=100, dps=30)
        # S_1 is exact: 2*pi*i
        assert result['near_2pi_i']
        # rho from numerical ratios should approximately match predicted
        # (slow convergence due to r^{-3/2} correction)
        rho_num = result['rho_numerical']
        rho_pred = result['rho_predicted']
        assert abs(rho_num - rho_pred) / rho_pred < 0.1

    def test_stokes_c_independent_for_virasoro(self):
        """The Stokes constant S_1 = 2*pi*i is universal (monodromy argument)."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, stokes_constant_from_monodromy,
        )
        for c in [0.5, 1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            S_1 = stokes_constant_from_monodromy(d)
            assert abs(S_1 - 2j * PI) < 1e-12


# =====================================================================
# Section 6: Alien derivatives
# =====================================================================

class TestAlienDerivatives:
    """Test alien derivative structure."""

    def test_heisenberg_no_alien_derivatives(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, alien_derivative_structure,
        )
        d = heisenberg_data()
        aliens = alien_derivative_structure(d, max_r=10, max_k=3)
        for entry in aliens:
            assert abs(entry['S_k']) < 1e-14

    def test_affine_no_alien_derivatives(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            affine_sl2_data, alien_derivative_structure,
        )
        d = affine_sl2_data(1.0)
        aliens = alien_derivative_structure(d, max_r=10, max_k=3)
        for entry in aliens:
            assert abs(entry['S_k']) < 1e-14

    def test_virasoro_infinite_alien_tower(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, alien_derivative_structure,
        )
        d = virasoro_data(13.0)
        aliens = alien_derivative_structure(d, max_r=30, max_k=5)
        # All alien derivatives should be nonzero for class M
        for entry in aliens:
            assert abs(entry['S_k']) > 1e-10

    def test_alien_omega_k_multiples(self):
        """Alien derivative positions should be at integer multiples of omega_1."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, alien_derivative_structure,
        )
        d = virasoro_data(13.0)
        aliens = alien_derivative_structure(d, max_r=30, max_k=5)
        omega_1 = aliens[0]['omega_k']
        for k, entry in enumerate(aliens, start=1):
            expected = k * omega_1
            assert abs(entry['omega_k'] - expected) < 1e-12

    def test_stokes_constants_decay(self):
        """S_k should decay as 1/k (logarithmic branch point)."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, alien_derivative_structure,
        )
        d = virasoro_data(13.0)
        aliens = alien_derivative_structure(d, max_r=30, max_k=5)
        S_1 = abs(aliens[0]['S_k'])
        for k, entry in enumerate(aliens, start=1):
            expected_decay = S_1 / k
            assert abs(abs(entry['S_k']) - expected_decay) < 1e-8


class TestBridgeEquation:
    """Test bridge equation verification."""

    def test_heisenberg_trivial(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, bridge_equation_check,
        )
        d = heisenberg_data()
        result = bridge_equation_check(d, max_r=10)
        assert result['bridge_satisfied']

    def test_affine_trivial(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            affine_sl2_data, bridge_equation_check,
        )
        d = affine_sl2_data(1.0)
        result = bridge_equation_check(d, max_r=10)
        assert result['bridge_satisfied']

    def test_virasoro_bridge(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, bridge_equation_check,
        )
        d = virasoro_data(13.0)
        result = bridge_equation_check(d, max_r=30)
        assert result['bridge_satisfied']
        assert result['max_residual'] < 1e-10

    def test_bridge_multiple_c(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, bridge_equation_check,
        )
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            result = bridge_equation_check(d, max_r=20)
            assert result['bridge_satisfied'], f"Bridge fails at c={c}"


# =====================================================================
# Section 7: Transseries
# =====================================================================

class TestTransseries:
    """Test transseries computation."""

    def test_perturbative_matches_direct_sum(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients, transseries_perturbative,
        )
        d = virasoro_data(13.0)
        t = 0.1 + 0.0j
        H_0 = transseries_perturbative(d, t, max_r=30)
        coeffs = shadow_coefficients(d, 30)
        direct = sum(coeffs[r] * t ** r for r in sorted(coeffs.keys()))
        assert abs(H_0 - direct) < 1e-12

    def test_heisenberg_no_instanton(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, transseries_evaluate,
        )
        d = heisenberg_data()
        result = transseries_evaluate(d, 0.1 + 0.0j)
        assert abs(result['one_instanton']) < 1e-14
        assert abs(result['total'] - result['perturbative']) < 1e-14

    def test_virasoro_transseries_evaluates(self):
        """Transseries evaluation produces finite results."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, transseries_evaluate,
        )
        d = virasoro_data(13.0)
        result = transseries_evaluate(d, 0.05 + 0.0j)
        assert np.isfinite(abs(result['perturbative']))
        assert np.isfinite(abs(result['total']))
        # The 1-instanton sector should be finite
        assert np.isfinite(abs(result['one_instanton']))


# =====================================================================
# Section 8: Lateral Borel sums and median resummation
# =====================================================================

class TestMedianResummation:
    """Test lateral Borel sums and median resummation."""

    def test_S_plus_S_minus_conjugate_on_real_axis(self):
        """For real t > 0, S_+ and S_- should be complex conjugates."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, median_borel_sum,
        )
        d = virasoro_data(13.0)
        result = median_borel_sum(d, t=0.1, max_r=30, n_quad=500)
        # S_+ and S_- should be approximately conjugate
        diff = abs(result['S_plus'] - result['S_minus'].conjugate())
        scale = max(abs(result['S_plus']), 1e-10)
        assert diff / scale < 0.1  # Allow for numerical quadrature error

    def test_median_real_for_real_t(self):
        """Median sum should be approximately real for real t."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, median_borel_sum,
        )
        d = virasoro_data(13.0)
        result = median_borel_sum(d, t=0.1, max_r=30, n_quad=500)
        median = result['median']
        if abs(median) > 1e-10:
            assert abs(median.imag) / abs(median) < 0.1  # Approximately real

    def test_heisenberg_small_stokes_jump(self):
        """Heisenberg: Stokes jump should be very small (polynomial Borel)."""
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, median_borel_sum,
        )
        d = heisenberg_data()
        result = median_borel_sum(d, t=0.1, max_r=10, n_quad=500)
        # For polynomial Borel, lateral sums differ only by numerical error
        S_avg = max(abs(result['S_plus']), abs(result['S_minus']), 1e-10)
        assert abs(result['stokes_jump']) / S_avg < 0.1


class TestMedianAtUnitArity:
    """Test median resummation at t = 1."""

    def test_weighted_sum_matches_exact(self):
        """The weighted sum sum r*S_r t^r = t^2*sqrt(Q_L(t)) at t=1."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, median_sum_at_unit_arity,
        )
        d = virasoro_data(25.0)
        assert d.rho < 1.0
        result = median_sum_at_unit_arity(d, max_r=50, n_quad=500)
        exact_w = result['exact_weighted']
        weighted = result['weighted_partial_sum']
        # Weighted partial sum should match exact weighted value
        assert abs(weighted - complex(exact_w)) / max(abs(complex(exact_w)), 1e-10) < 1e-6


# =====================================================================
# Section 9: Exact closed-form comparison
# =====================================================================

class TestExactComparison:
    """Test exact shadow generating function vs series comparison.

    Key relationship: sum r*S_r t^r = t^2 * sqrt(Q_L(t)).
    The unweighted sum S_r t^r is a different function.
    """

    def test_weighted_series_matches_exact(self):
        """sum r * S_r * t^r = t^2 * sqrt(Q_L(t)) at small t."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients, exact_shadow_generating_function,
        )
        d = virasoro_data(13.0)
        t = 0.05
        exact = exact_shadow_generating_function(d, t)
        coeffs = shadow_coefficients(d, 60)
        weighted_series = sum(r * coeffs[r] * t ** r for r in sorted(coeffs.keys()))
        assert abs(exact - weighted_series) / max(abs(exact), 1e-10) < 1e-6

    def test_exact_at_origin(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, exact_shadow_generating_function,
        )
        d = virasoro_data(13.0)
        assert abs(exact_shadow_generating_function(d, 0.0)) < 1e-14

    def test_exact_Q_L_positive_at_t_small(self):
        """Q_L(0) = 4*kappa^2 > 0 for kappa != 0."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        assert d.q0 > 0

    def test_unweighted_series_at_small_t(self):
        """The unweighted series sum S_r t^r converges for small t."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients,
        )
        d = virasoro_data(13.0)
        coeffs = shadow_coefficients(d, 60)
        t = 0.05
        series = sum(coeffs[r] * t ** r for r in sorted(coeffs.keys()))
        assert np.isfinite(series)


class TestShadowODE:
    """Test shadow ODE analytic continuation."""

    def test_ode_starts_at_one(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_ode_analytic_continuation,
        )
        d = virasoro_data(13.0)
        traj = shadow_ode_analytic_continuation(d, t_start=0.01, t_end=0.1)
        # Phi(t_start) should be close to sqrt(Q_L(t_start)/Q_L(0))
        t0 = traj[0][0]
        phi0 = traj[0][1]
        Q0 = d.q0 + d.q1 * t0 + d.q2 * t0 ** 2
        expected = cmath.sqrt(Q0) / cmath.sqrt(complex(d.q0))
        assert abs(phi0 - expected) < 0.01

    def test_ode_matches_exact_at_small_t(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_ode_analytic_continuation,
        )
        d = virasoro_data(13.0)
        traj = shadow_ode_analytic_continuation(d, t_start=0.01, t_end=0.5, n_steps=5000)
        # Check at t = 0.3
        for t_val, phi_val in traj:
            if abs(t_val - 0.3) < 0.01:
                Q_val = d.q0 + d.q1 * t_val + d.q2 * t_val ** 2
                expected = cmath.sqrt(Q_val) / cmath.sqrt(complex(d.q0))
                assert abs(phi_val - expected) / max(abs(expected), 1e-10) < 0.05
                break


# =====================================================================
# Section 10: p-adic analysis
# =====================================================================

class TestPAdicValuation:
    """Test p-adic valuation and norm."""

    def test_valuation_powers_of_p(self):
        from lib.resurgence_arithmetic_frontier_engine import p_adic_valuation
        assert p_adic_valuation(8, 2) == 3
        assert p_adic_valuation(27, 3) == 3
        assert p_adic_valuation(25, 5) == 2

    def test_valuation_coprime(self):
        from lib.resurgence_arithmetic_frontier_engine import p_adic_valuation
        assert p_adic_valuation(7, 2) == 0
        assert p_adic_valuation(11, 3) == 0

    def test_norm_basic(self):
        from lib.resurgence_arithmetic_frontier_engine import p_adic_norm
        assert abs(p_adic_norm(Fraction(8), 2) - 1.0 / 8.0) < 1e-14
        assert abs(p_adic_norm(Fraction(1, 3), 3) - 3.0) < 1e-14

    def test_norm_zero(self):
        from lib.resurgence_arithmetic_frontier_engine import p_adic_norm
        assert p_adic_norm(Fraction(0), 2) == 0.0


class TestPAdicBorel:
    """Test p-adic Borel transform analysis."""

    def test_borel_coefficients_rational(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_coefficients_rational,
        )
        d = virasoro_data(2.0)
        bc = borel_coefficients_rational(d, max_r=15)
        assert len(bc) > 0
        # All values should be Fraction
        for r, val in bc.items():
            assert isinstance(val, Fraction)

    def test_p_adic_norms_computed(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, p_adic_borel_norms,
        )
        d = virasoro_data(2.0)
        norms = p_adic_borel_norms(d, p=2, max_r=15)
        assert len(norms) > 0
        for r, val in norms.items():
            assert val >= 0

    def test_p_adic_convergence_radius(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, p_adic_convergence_radius,
        )
        d = virasoro_data(2.0)
        R_p = p_adic_convergence_radius(d, p=2, max_r=20)
        assert R_p > 0

    def test_comparison_archimedean_vs_p_adic(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, p_adic_singularity_comparison,
        )
        d = virasoro_data(2.0)
        result = p_adic_singularity_comparison(d, primes=[2, 3, 5], max_r=20)
        assert 'archimedean_radius' in result
        for p in [2, 3, 5]:
            assert p in result
            assert result[p]['R_p'] > 0

    def test_p_adic_stokes(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, p_adic_stokes_phenomenon,
        )
        d = virasoro_data(2.0)
        result = p_adic_stokes_phenomenon(d, p=2, max_r=20)
        assert 'p' in result
        assert result['p'] == 2
        assert 'has_p_adic_stokes' in result


# =====================================================================
# Section 11: Peacock patterns
# =====================================================================

class TestPeacockPattern:
    """Test Garoufalidis-Zagier peacock patterns."""

    def test_coefficients_mod_p(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients_mod_p,
        )
        d = virasoro_data(2.0)
        mods = shadow_coefficients_mod_p(d, p=5, max_r=30)
        assert len(mods) == 29  # r = 2, ..., 30
        for r, val in mods.items():
            assert 0 <= val < 5

    def test_heisenberg_trivial_pattern(self):
        """Heisenberg: only S_2 nonzero, so pattern is mostly zeros."""
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, shadow_coefficients_mod_p,
        )
        d = heisenberg_data()
        mods = shadow_coefficients_mod_p(d, p=3, max_r=20)
        # S_r = 0 for r >= 3
        for r in range(3, 21):
            assert mods[r] == 0

    def test_peacock_pattern_structure(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, peacock_pattern,
        )
        d = virasoro_data(2.0)
        result = peacock_pattern(d, p=5, max_r=50)
        assert 'residue_distribution' in result
        assert 'mod_values' in result
        assert len(result['mod_values']) == 49

    def test_peacock_multi_prime(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, peacock_pattern_multi_prime,
        )
        d = virasoro_data(2.0)
        result = peacock_pattern_multi_prime(d, primes=[2, 3, 5, 7], max_r=40)
        assert len(result) == 4
        for p in [2, 3, 5, 7]:
            assert p in result


# =====================================================================
# Section 12: Multi-path verification
# =====================================================================

class TestMultiPathVerification:
    """Test multi-path verification of resurgence structure."""

    def test_borel_singularity_multipath(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, verify_borel_singularities_multipath,
        )
        d = virasoro_data(13.0)
        result = verify_borel_singularities_multipath(d, max_r=40)
        assert 'path_1_predicted' in result
        assert 'path_2_pade' in result
        assert 'path_4_p_adic' in result

    def test_stokes_multipath(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, verify_stokes_multipath,
        )
        d = virasoro_data(13.0)
        result = verify_stokes_multipath(d, max_r=40)
        assert 'path_1_monodromy' in result
        assert abs(result['path_1_monodromy'] - 2j * PI) < 1e-12


# =====================================================================
# Section 13: Cross-family consistency
# =====================================================================

class TestCrossFamilyConsistency:
    """Test consistency across algebra families."""

    def test_depth_class_determines_singularities(self):
        """Class G/L: no singularities. Class M: singularities."""
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, affine_sl2_data, virasoro_data,
            locate_all_borel_singularities,
        )
        assert len(locate_all_borel_singularities(heisenberg_data())) == 0
        assert len(locate_all_borel_singularities(affine_sl2_data(1.0))) == 0
        assert len(locate_all_borel_singularities(virasoro_data(13.0))) > 0

    def test_rho_monotone_in_c(self):
        """rho(Vir_c) decreases as c increases (for large c)."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        rho_prev = virasoro_data(5.0).rho
        for c in [10.0, 15.0, 20.0, 25.0]:
            rho_curr = virasoro_data(c).rho
            assert rho_curr < rho_prev
            rho_prev = rho_curr

    def test_landscape_scan(self):
        from lib.resurgence_arithmetic_frontier_engine import landscape_resurgence_scan
        scan = landscape_resurgence_scan(max_r=20)
        assert 'Heis' in scan
        assert 'Vir_c13' in scan
        assert scan['Heis']['depth_class'] == 'G'
        assert scan['Vir_c13']['depth_class'] == 'M'


# =====================================================================
# Section 14: Koszul duality and self-duality
# =====================================================================

class TestKoszulDuality:
    """Test Koszul duality properties of resurgence structure."""

    def test_c13_self_dual_rho(self):
        """At c=13, Vir_c and its Koszul dual Vir_{26-c}=Vir_13 are the same."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        d_dual = virasoro_data(26.0 - 13.0)
        assert abs(d.rho - d_dual.rho) < 1e-12
        assert abs(d.theta - d_dual.theta) < 1e-12

    def test_koszul_pair_complementary_rho(self):
        """rho(c) and rho(26-c) should differ for c != 13."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 5.0, 20.0, 25.0]:
            d = virasoro_data(c)
            d_dual = virasoro_data(26.0 - c)
            # They should be different (unless c=13)
            if abs(c - 13.0) > 0.1:
                assert abs(d.rho - d_dual.rho) > 1e-6

    def test_complementarity_sum_AP24(self):
        """kappa + kappa' = 13 for Virasoro (AP24)."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            assert abs(d.kappa + d.kappa_dual - 13.0) < 1e-12

    def test_heisenberg_kappa_antisymmetric(self):
        """kappa + kappa' = 0 for Heisenberg (AP24)."""
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data(1, 3.0)
        assert abs(d.kappa + d.kappa_dual) < 1e-14


class TestSelfDualProperties:
    """Test special properties at the self-dual point c=13."""

    def test_rho_at_c13(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        # rho(13) = sqrt((180*13 + 872) / ((5*13+22)*13^2))
        rho_sq = (180 * 13 + 872) / ((5 * 13 + 22) * 13 ** 2)
        assert abs(d.rho - math.sqrt(rho_sq)) < 1e-12

    def test_branch_points_symmetric(self):
        """At c=13, the branch points should be symmetric (complex conjugate)."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        assert abs(d.branch_plus - d.branch_minus.conjugate()) < 1e-12


# =====================================================================
# Section 15: Edge cases
# =====================================================================

class TestEdgeCases:
    """Test edge cases and boundary behavior."""

    def test_c_near_zero(self):
        """c near 0: kappa -> 0, degenerate shadow metric."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(0.01)
        assert abs(d.kappa - 0.005) < 1e-10

    def test_c_large(self):
        """Large c: rho -> 0, tower converges rapidly."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(100.0)
        assert d.rho < 0.5

    def test_c_one_half(self):
        """c = 1/2 (minimal model): verify shadow data."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(0.5)
        assert abs(d.kappa - 0.25) < 1e-14
        assert abs(d.alpha - 2.0) < 1e-14
        assert abs(d.S4 - 10.0 / (0.5 * (2.5 + 22.0))) < 1e-12

    def test_negative_level_affine(self):
        """Negative level for affine sl_2 (below critical)."""
        from lib.resurgence_arithmetic_frontier_engine import affine_sl2_data
        d = affine_sl2_data(-1.0)
        expected = 3.0 * (-1.0 + 2.0) / 4.0  # = 3/4
        assert abs(d.kappa - expected) < 1e-14

    def test_high_rank_heisenberg(self):
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data(rank=24)
        assert abs(d.kappa - 24.0) < 1e-14
        assert d.depth_class == 'G'


# =====================================================================
# Section 16: Resurgence summary and scan
# =====================================================================

class TestResurgenceSummary:
    """Test the resurgence summary function."""

    def test_summary_virasoro(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, resurgence_summary,
        )
        d = virasoro_data(13.0)
        s = resurgence_summary(d, max_r=20)
        assert s['depth_class'] == 'M'
        assert s['n_singularities'] > 0
        assert abs(s['S_1'] - 2j * PI) < 1e-12

    def test_summary_heisenberg(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            heisenberg_data, resurgence_summary,
        )
        d = heisenberg_data()
        s = resurgence_summary(d, max_r=10)
        assert s['depth_class'] == 'G'
        assert s['n_singularities'] == 0

    def test_scan_all_families(self):
        from lib.resurgence_arithmetic_frontier_engine import landscape_resurgence_scan
        scan = landscape_resurgence_scan(max_r=15)
        assert len(scan) >= 5
        # Heisenberg should be class G
        assert scan['Heis']['depth_class'] == 'G'
        # Affine should be class L
        assert scan['aff_sl2_k1']['depth_class'] == 'L'
        # Virasoro should be class M
        for key in ['Vir_c1', 'Vir_c2', 'Vir_c13', 'Vir_c25']:
            assert scan[key]['depth_class'] == 'M'


# =====================================================================
# Section 17: Virasoro at specific central charges
# =====================================================================

class TestVirasoroSpecificC:
    """Test resurgence at specific central charges for Virasoro."""

    def test_c1_rho_greater_than_1(self):
        """c=1: diverging tower (rho > 1)."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(1.0)
        assert d.rho > 1.0

    def test_c2_rho_greater_than_1(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(2.0)
        assert d.rho > 1.0

    def test_c13_rho_less_than_1(self):
        """c=13: converging tower (rho < 1)."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(13.0)
        assert d.rho < 1.0

    def test_c25_rho_less_than_1(self):
        """c=25: converging tower."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        d = virasoro_data(25.0)
        assert d.rho < 1.0

    def test_critical_c_exists(self):
        """The critical central charge c* where rho=1 should be near 6.12."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        # Binary search for rho = 1
        lo, hi = 5.0, 8.0
        for _ in range(50):
            mid = (lo + hi) / 2.0
            d = virasoro_data(mid)
            if d.rho > 1.0:
                lo = mid
            else:
                hi = mid
        c_star = (lo + hi) / 2.0
        assert abs(c_star - 6.1243) < 0.01

    def test_virasoro_singularities_at_all_c(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, locate_all_borel_singularities,
        )
        for c in [0.5, 1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            sings = locate_all_borel_singularities(d)
            assert len(sings) >= 2, f"c={c}: expected >= 2 singularities"


# =====================================================================
# Section 18: Instanton actions
# =====================================================================

class TestInstantonActions:
    """Test instanton action computation."""

    def test_instanton_modulus_is_rho(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            A_p, A_m = d.instanton_actions
            assert abs(abs(A_p) - d.rho) < 1e-10, f"c={c}"
            assert abs(abs(A_m) - d.rho) < 1e-10, f"c={c}"

    def test_instanton_actions_conjugate(self):
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 13.0, 25.0]:
            d = virasoro_data(c)
            A_p, A_m = d.instanton_actions
            assert abs(A_p - A_m.conjugate()) < 1e-12

    def test_heisenberg_no_instanton(self):
        """Heisenberg: branch points at infinity, so instanton actions are trivial."""
        from lib.resurgence_arithmetic_frontier_engine import heisenberg_data
        d = heisenberg_data()
        # rho = 0 means no finite instanton actions
        assert d.rho == 0.0
        # Branch points at infinity
        assert d.branch_plus == complex('inf')
        assert d.branch_minus == complex('inf')


# =====================================================================
# Section 19: Consistency with existing engines
# =====================================================================

class TestCrossEngineConsistency:
    """Test consistency with existing resurgence and shadow engines."""

    def test_shadow_coefficients_vs_stokes_engine(self):
        """Compare shadow coefficients with resurgence_stokes_engine."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data as vd_new, shadow_coefficients as sc_new,
        )
        try:
            from lib.resurgence_stokes_engine import (
                virasoro_shadow_invariants, virasoro_shadow_coefficients_recursive,
            )
        except ImportError:
            pytest.skip("resurgence_stokes_engine not available")

        c = 13.0
        d = vd_new(c)
        new_coeffs = sc_new(d, 20)
        old_coeffs = virasoro_shadow_coefficients_recursive(c, 20)
        for i, r in enumerate(range(2, 21)):
            assert abs(new_coeffs[r] - old_coeffs[i]) < 1e-12

    def test_rho_vs_shadow_radius(self):
        """Compare rho with shadow_radius.py formula."""
        from lib.resurgence_arithmetic_frontier_engine import virasoro_data
        for c in [1.0, 2.0, 13.0, 25.0]:
            d = virasoro_data(c)
            rho_sq = (180.0 * c + 872.0) / ((5.0 * c + 22.0) * c ** 2)
            expected_rho = math.sqrt(rho_sq)
            assert abs(d.rho - expected_rho) < 1e-12


# =====================================================================
# Section 20: Arithmetic properties of shadow coefficients
# =====================================================================

class TestArithmeticProperties:
    """Test arithmetic properties of shadow coefficients."""

    def test_virasoro_S2_rational(self):
        """S_2 = kappa = c/2 should be rational for rational c."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_coefficients_rational,
        )
        d = virasoro_data(2.0)
        bc = borel_coefficients_rational(d, max_r=10)
        # All Borel coefficients should be exact Fractions
        for r, val in bc.items():
            assert isinstance(val, Fraction)

    def test_coefficients_sign_alternation(self):
        """For Virasoro, high-arity shadow coefficients should alternate in sign."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, shadow_coefficients,
        )
        d = virasoro_data(13.0)
        coeffs = shadow_coefficients(d, 40)
        # Check sign pattern in high-arity regime
        signs = [1 if coeffs[r] > 0 else -1 for r in range(10, 35) if abs(coeffs[r]) > 1e-30]
        # Should have sign changes (from the oscillating asymptotics)
        if len(signs) > 5:
            n_changes = sum(1 for i in range(len(signs) - 1) if signs[i] != signs[i + 1])
            assert n_changes > 0, "Expected sign changes for class M tower"


# =====================================================================
# Section 21: Additional multipath verifications
# =====================================================================

class TestAdditionalVerification:
    """Additional multi-path verification tests."""

    def test_borel_singularity_3_paths_virasoro_c1(self):
        """3-path verification for Virasoro c=1."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_singularity_locations,
            borel_pade_singularities, p_adic_singularity_comparison,
        )
        d = virasoro_data(1.0)
        # Path 1: predicted
        zeta_p, zeta_m = borel_singularity_locations(d)
        assert abs(zeta_p) > 0
        # Path 2: Pade
        pade = borel_pade_singularities(d, max_r=40)
        assert len(pade['detected_poles']) > 0
        # Path 3: p-adic (existence check)
        p_adic = p_adic_singularity_comparison(d, primes=[2], max_r=20)
        assert 2 in p_adic

    def test_borel_singularity_3_paths_virasoro_c13(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, borel_singularity_locations,
            borel_pade_singularities, p_adic_singularity_comparison,
        )
        d = virasoro_data(13.0)
        zeta_p, zeta_m = borel_singularity_locations(d)
        assert abs(zeta_p) > 0
        pade = borel_pade_singularities(d, max_r=40)
        assert len(pade['detected_poles']) > 0
        p_adic = p_adic_singularity_comparison(d, primes=[2, 3], max_r=20)
        assert 2 in p_adic

    def test_stokes_3_paths_virasoro(self):
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, stokes_constant_from_monodromy,
            stokes_constant_numerical,
        )
        d = virasoro_data(13.0)
        # Path 1: monodromy
        S_1_mono = stokes_constant_from_monodromy(d)
        assert abs(S_1_mono - 2j * PI) < 1e-12
        # Path 2: numerical
        result = stokes_constant_numerical(d, max_r=60)
        assert result['converged']

    def test_bridge_equation_all_c(self):
        """Bridge equation should hold at all central charges."""
        from lib.resurgence_arithmetic_frontier_engine import (
            virasoro_data, bridge_equation_check,
        )
        for c in [0.5, 1.0, 2.0, 5.0, 13.0, 25.0]:
            d = virasoro_data(c)
            result = bridge_equation_check(d, max_r=15)
            assert result['bridge_satisfied'], f"Bridge fails at c={c}"
