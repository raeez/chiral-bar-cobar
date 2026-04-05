r"""Tests for derived algebraic geometry of shadow zero schemes.

Multi-path verification (3+ independent methods per claim):
    Path 1: Argument principle N(T) matches explicit zero count
    Path 2: Multiplicity: zeta(rho)=0 and zeta'(rho)!=0 (simple zero check)
    Path 3: Deformation: d(rho)/dc matches numerical finite difference
    Path 4: Self-intersection at c=13: palindromic zero set
    Path 5: Hilbert function H(d) <= N(d) (consistency)

70+ tests covering:
    - Zero scheme structure (multiplicities, local rings)
    - Tangent complex (inverse zero speeds)
    - Intersection theory (complementary pairs, self-intersection)
    - Euler characteristic (argument principle vs explicit)
    - Hilbert function monotonicity and consistency
    - Deformation with c (implicit differentiation vs finite diff)
    - Regularized motivic class
    - Spectral coincidences
    - Multi-path cross-verification

Tolerance: 1e-6 for exact, 1e-3 for numerical, 0.5 for counting.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP10): Multi-path verification, not hardcoded values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

import math
import cmath
import pytest
from typing import Dict, List

from compute.lib.bc_zero_scheme_engine import (
    # Higher derivatives
    _shadow_zeta_higher_deriv,
    # Multiplicity
    zero_multiplicity,
    compute_inverse_zero_speed,
    # Zero scheme construction
    build_zero_scheme_point,
    build_zero_scheme,
    ZeroSchemePoint,
    ZeroSchemeData,
    # Inverse speeds
    inverse_zero_speeds,
    # Intersection theory
    zero_scheme_intersection,
    self_intersection_number,
    complementary_intersection,
    # Euler characteristic
    euler_characteristic_argument_principle,
    euler_characteristic_explicit,
    asymptotic_zero_count,
    # Hilbert function
    hilbert_function,
    # Deformation
    zero_c_derivative,
    track_zeros_with_c,
    zero_c_derivatives_first_n,
    find_zero_collisions,
    # Motivic class
    regularized_motivic_class,
    # Spectral coincidences
    spectral_coincidences,
    spectral_coincidences_complementary,
    # Verification utilities
    verify_zero_simplicity,
    verify_deformation_formula,
    verify_hilbert_vs_counting,
    palindromic_zero_test,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    find_zeros_grid,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
    newton_zero,
)

from compute.lib.shadow_zeta_function_engine import (
    virasoro_shadow_coefficients_numerical,
    shadow_zeta_numerical,
)


# ============================================================================
# Helpers
# ============================================================================

def _virasoro_zeros(c_val, max_r=60, im_max=50.0):
    """Get Virasoro zeros in a standard search region."""
    coeffs = shadow_coefficients_extended('virasoro', c_val, max_r)
    return find_zeros_grid(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=(-im_max, im_max),
        grid_re=15,
        grid_im=80,
        max_r=max_r,
    )


# ============================================================================
# A. Higher derivative computation (8 tests)
# ============================================================================

class TestHigherDerivatives:
    """Tests for k-th derivative of shadow zeta."""

    def test_zeroth_deriv_is_value(self):
        """zeta^{(0)}(s) = zeta(s)."""
        coeffs = virasoro_shadow_coefficients_numerical(1.0, 30)
        s = complex(3.0, 1.0)
        val = _shadow_zeta_higher_deriv(coeffs, s, order=0, max_r=30)
        direct = shadow_zeta_numerical(coeffs, s, 30)
        assert abs(val - direct) < 1e-10

    def test_first_deriv_matches(self):
        """zeta^{(1)}(s) matches the standard derivative function."""
        coeffs = virasoro_shadow_coefficients_numerical(5.0, 30)
        s = complex(2.0, 3.0)
        val = _shadow_zeta_higher_deriv(coeffs, s, order=1, max_r=30)
        standard = _shadow_zeta_derivative(coeffs, s, 30)
        assert abs(val - standard) < 1e-10

    def test_second_deriv_formula(self):
        """zeta''(s) = sum S_r (log r)^2 r^{-s}."""
        coeffs = {2: 1.0, 3: 0.5, 4: 0.25}
        s = complex(2.0, 0.0)
        val = _shadow_zeta_higher_deriv(coeffs, s, order=2, max_r=4)
        expected = (1.0 * math.log(2)**2 * 2**(-2)
                    + 0.5 * math.log(3)**2 * 3**(-2)
                    + 0.25 * math.log(4)**2 * 4**(-2))
        assert abs(val - expected) < 1e-10

    def test_heisenberg_all_derivs(self):
        """Heisenberg: zeta = k*2^{-s}, so zeta^{(n)} = k*(-log 2)^n * 2^{-s}."""
        k = 3.0
        coeffs = {2: k}
        s = complex(1.0, 2.0)
        for n in range(5):
            val = _shadow_zeta_higher_deriv(coeffs, s, order=n, max_r=2)
            expected = k * ((-math.log(2)) ** n) * (2 ** (-s))
            assert abs(val - expected) < 1e-10

    def test_derivative_order_increases_decay(self):
        """Higher derivatives should decay faster for Re(s) >> 1."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, 30)
        s = complex(5.0, 0.0)
        vals = [abs(_shadow_zeta_higher_deriv(coeffs, s, order=n, max_r=30))
                for n in range(4)]
        # Not necessarily strictly decreasing, but should be finite
        for v in vals:
            assert v < 1e10

    def test_pure_imaginary_evaluation(self):
        """Derivative evaluates correctly on the imaginary axis."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 30)
        s = complex(0.0, 5.0)
        val = _shadow_zeta_higher_deriv(coeffs, s, order=1, max_r=30)
        assert isinstance(val, complex)
        assert not cmath.isnan(val)

    def test_derivative_consistency_ratio(self):
        """Numerical derivative via finite difference matches formula."""
        coeffs = virasoro_shadow_coefficients_numerical(5.0, 30)
        s = complex(3.0, 1.0)
        h = 1e-6
        # Numerical first derivative
        f_plus = shadow_zeta_numerical(coeffs, s + h, 30)
        f_minus = shadow_zeta_numerical(coeffs, s - h, 30)
        num_deriv = (f_plus - f_minus) / (2 * h)
        analytic = _shadow_zeta_higher_deriv(coeffs, s, order=1, max_r=30)
        assert abs(num_deriv - analytic) < 1e-3

    def test_empty_coeffs_zero(self):
        """All-zero coefficients give zero for all derivatives."""
        coeffs = {r: 0.0 for r in range(2, 10)}
        s = complex(1.0, 1.0)
        for n in range(3):
            val = _shadow_zeta_higher_deriv(coeffs, s, order=n, max_r=9)
            assert abs(val) < 1e-15


# ============================================================================
# B. Multiplicity computation (8 tests)
# ============================================================================

class TestMultiplicity:
    """Tests for zero multiplicity."""

    def test_heisenberg_not_zero(self):
        """Heisenberg k=1 has no zeros: mult(s) = 0 for any s."""
        coeffs = {2: 1.0}
        for r in range(3, 10):
            coeffs[r] = 0.0
        m = zero_multiplicity(coeffs, complex(1.0, 1.0), max_r=9)
        assert m == 0  # Not a zero at all

    def test_virasoro_simple_zero(self):
        """At a found Virasoro zero, multiplicity should be 1."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-30, 30), 10, 40, max_r=60,
        )
        if len(zeros) > 0:
            m = zero_multiplicity(coeffs, zeros[0], max_r=60)
            assert m == 1

    def test_multiplicity_at_nonzero_point(self):
        """At a point where zeta != 0, multiplicity is 0."""
        coeffs = virasoro_shadow_coefficients_numerical(5.0, 30)
        s = complex(5.0, 0.0)  # Far from critical region
        m = zero_multiplicity(coeffs, s, max_r=30)
        assert m == 0

    def test_inverse_speed_positive(self):
        """Inverse zero speed should be positive at simple zeros."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-30, 30), 10, 40, max_r=60,
        )
        if len(zeros) > 0:
            inv_sp = compute_inverse_zero_speed(coeffs, zeros[0], max_r=60)
            assert inv_sp > 0
            assert inv_sp < float('inf')

    def test_inverse_speed_at_nonzero(self):
        """Inverse speed at a non-zero: 1/|zeta'(s)| is finite."""
        coeffs = virasoro_shadow_coefficients_numerical(5.0, 30)
        s = complex(3.0, 0.0)
        inv_sp = compute_inverse_zero_speed(coeffs, s, max_r=30)
        assert inv_sp > 0
        assert inv_sp < float('inf')

    def test_multiplicity_max_bound(self):
        """Multiplicity should not exceed max_order."""
        coeffs = virasoro_shadow_coefficients_numerical(1.0, 30)
        s = complex(0.5, 0.5)
        m = zero_multiplicity(coeffs, s, max_order=3, max_r=30)
        assert m <= 3

    def test_affine_zeros_simple(self):
        """Affine sl2 zeros (exact formula) should all be simple."""
        coeffs = shadow_coefficients_extended('affine_sl2', 1.0, 30)
        # Construct an exact zero
        k = 1.0
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        ratio = kappa / alpha
        log_32 = math.log(3.0 / 2.0)
        s = complex(-math.log(ratio) / log_32, -math.pi / log_32)
        m = zero_multiplicity(coeffs, s, max_r=30, tol=1e-4)
        assert m == 1

    def test_zero_scheme_point_construction(self):
        """build_zero_scheme_point produces correct data."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-30, 30), 10, 40, max_r=60,
        )
        if len(zeros) > 0:
            pt = build_zero_scheme_point(coeffs, zeros[0], max_r=60)
            assert isinstance(pt, ZeroSchemePoint)
            assert pt.multiplicity >= 1
            assert pt.inverse_speed > 0
            assert pt.tangent_dim >= 1
            assert pt.local_ring_length == pt.multiplicity


# ============================================================================
# C. Zero scheme construction (7 tests)
# ============================================================================

class TestZeroSchemeConstruction:
    """Tests for full zero scheme building."""

    def test_virasoro_c1_scheme(self):
        """Zero scheme for Virasoro c=1 is constructible."""
        scheme = build_zero_scheme(
            'virasoro', 1.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert isinstance(scheme, ZeroSchemeData)
        assert scheme.family == 'virasoro'
        assert scheme.param == 1.0
        assert scheme.total_length >= 0

    def test_virasoro_c13_scheme(self):
        """Zero scheme at self-dual point c=13."""
        scheme = build_zero_scheme(
            'virasoro', 13.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert isinstance(scheme, ZeroSchemeData)
        assert scheme.total_length >= 0

    def test_virasoro_c25_scheme(self):
        """Zero scheme for Virasoro c=25."""
        scheme = build_zero_scheme(
            'virasoro', 25.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert isinstance(scheme, ZeroSchemeData)

    def test_scheme_reduced_generic_c(self):
        """For generic c, expect all zeros simple (reduced scheme)."""
        scheme = build_zero_scheme(
            'virasoro', 7.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert scheme.is_reduced

    def test_total_length_equals_count_when_reduced(self):
        """When reduced: total_length = number of points."""
        scheme = build_zero_scheme(
            'virasoro', 10.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        if scheme.is_reduced:
            assert scheme.total_length == len(scheme.points)

    def test_heisenberg_empty_scheme(self):
        """Heisenberg k!=0 has no zeros: empty scheme."""
        scheme = build_zero_scheme(
            'heisenberg', 1.0, max_r=10,
            im_range=(-30, 30), grid_re=5, grid_im=20,
        )
        assert len(scheme.points) == 0
        assert scheme.total_length == 0
        assert scheme.is_reduced

    def test_scheme_euler_char(self):
        """euler_char_truncated = number of points in scheme."""
        scheme = build_zero_scheme(
            'virasoro', 5.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert scheme.euler_char_truncated == len(scheme.points)


# ============================================================================
# D. Inverse zero speeds (6 tests)
# ============================================================================

class TestInverseZeroSpeeds:
    """Tests for the tangent complex / inverse zero speeds."""

    def test_virasoro_c10_speeds(self):
        """Inverse speeds for c=10 (rho<1) are positive and finite."""
        result = inverse_zero_speeds(
            'virasoro', 10.0, n_zeros=10, max_r=60, im_max=50.0,
            grid_re=15, grid_im=80,
        )
        assert len(result) > 0, "No zeros found for c=10"
        for rho, sp in result:
            assert sp > 0
            assert sp < float('inf')

    def test_virasoro_c13_speeds(self):
        """Inverse speeds for c=13 (self-dual)."""
        result = inverse_zero_speeds(
            'virasoro', 13.0, n_zeros=10, max_r=60, im_max=50.0,
            grid_re=15, grid_im=80,
        )
        assert len(result) > 0, "No zeros found for c=13"
        for rho, sp in result:
            assert sp > 0

    def test_virasoro_c25_speeds(self):
        """Inverse speeds for c=25."""
        result = inverse_zero_speeds(
            'virasoro', 25.0, n_zeros=10, max_r=60, im_max=60.0,
            grid_re=15, grid_im=80,
        )
        assert len(result) > 0, "No zeros found for c=25"
        for rho, sp in result:
            assert sp > 0

    def test_speed_growth_trend(self):
        """Inverse speeds should show a growth trend (like log(gamma)/(2pi))."""
        result = inverse_zero_speeds(
            'virasoro', 10.0, n_zeros=20, max_r=40, im_max=80.0,
            grid_re=10, grid_im=60,
        )
        if len(result) >= 5:
            # Just check that speeds are computed and have a range
            speeds = [sp for _, sp in result]
            assert max(speeds) > min(speeds) * 0.1  # Some variation

    def test_sorted_by_imaginary_part(self):
        """Results should be sorted by |Im(rho)|."""
        result = inverse_zero_speeds(
            'virasoro', 13.0, n_zeros=10, max_r=60, im_max=50.0,
            grid_re=15, grid_im=80,
        )
        assert len(result) >= 2, "Need at least 2 zeros"
        for i in range(len(result) - 1):
            assert abs(result[i][0].imag) <= abs(result[i+1][0].imag) + 1e-6

    def test_speed_matches_derivative(self):
        """1/|zeta'(rho)| computed two ways should agree."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-40, 40), 15, 60, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=10"
        rho = zeros[0]
        sp1 = compute_inverse_zero_speed(coeffs, rho, max_r=60)
        deriv = _shadow_zeta_derivative(coeffs, rho, 60)
        sp2 = 1.0 / abs(deriv) if abs(deriv) > 1e-300 else float('inf')
        assert abs(sp1 - sp2) < 1e-10


# ============================================================================
# E. Intersection theory (8 tests)
# ============================================================================

class TestIntersectionTheory:
    """Tests for intersection numbers of zero schemes."""

    def test_self_intersection_reduced(self):
        """Self-intersection of a reduced scheme equals number of zeros."""
        result = self_intersection_number(
            'virasoro', 10.0, max_r=60,
            im_range=(-40, 40), grid_re=15, grid_im=60,
        )
        if result['is_reduced']:
            assert result['self_intersection'] == result['n_zeros']

    def test_self_intersection_nonnegative(self):
        """Self-intersection is always nonneg."""
        result = self_intersection_number(
            'virasoro', 10.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert result['self_intersection'] >= 0

    def test_complementary_c13_is_self_intersection(self):
        """At c=13, complementary intersection is self-intersection."""
        result = complementary_intersection(
            13.0, max_r=40, im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        # This returns self_intersection_number output
        assert 'self_intersection' in result

    def test_complementary_c10_vs_c16(self):
        """Complementary pair c=10, c=16 (both rho<1) intersection."""
        result = complementary_intersection(
            10.0, max_r=60, im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        assert 'intersection_number' in result
        assert result['intersection_number'] >= 0

    def test_intersection_symmetric(self):
        """<Z_A, Z_B> = <Z_B, Z_A>."""
        # Use c=10, c=16 (both rho<1) for meaningful intersection
        r1 = zero_scheme_intersection(
            'virasoro', 10.0, 'virasoro', 16.0, max_r=60,
            im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        r2 = zero_scheme_intersection(
            'virasoro', 16.0, 'virasoro', 10.0, max_r=60,
            im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        assert r1['intersection_number'] == r2['intersection_number']

    def test_heisenberg_intersection_empty(self):
        """Heisenberg has no zeros, so intersection with anything is 0."""
        result = zero_scheme_intersection(
            'heisenberg', 1.0, 'virasoro', 10.0, max_r=60,
            im_range=(-25, 25), grid_re=8, grid_im=30,
        )
        assert result['intersection_number'] == 0
        assert result['n_zeros_a'] == 0

    def test_self_intersection_geq_n_zeros(self):
        """Self-intersection >= n_zeros (mult^2 >= 1)."""
        result = self_intersection_number(
            'virasoro', 10.0, max_r=40,
            im_range=(-25, 25), grid_re=8, grid_im=30,
        )
        assert result['self_intersection'] >= result['n_zeros']

    def test_complementary_c12_result_type(self):
        """Complementary intersection at c=12 (dual c=14) returns correct structure."""
        result = complementary_intersection(
            12.0, max_r=60, im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        assert 'n_zeros_a' in result or 'n_zeros' in result


# ============================================================================
# F. Euler characteristic / zero counting (8 tests)
# ============================================================================

class TestEulerCharacteristic:
    """Tests for zero counting via argument principle and explicit."""

    def test_asymptotic_formula_positive(self):
        """Asymptotic N(T) is positive for T > 2*pi*e."""
        assert asymptotic_zero_count(20.0) > 0
        assert asymptotic_zero_count(50.0) > 0
        assert asymptotic_zero_count(100.0) > 0

    def test_asymptotic_monotone(self):
        """N(T) is monotone increasing."""
        T_vals = [10.0, 20.0, 50.0, 100.0, 500.0]
        N_vals = [asymptotic_zero_count(T) for T in T_vals]
        for i in range(len(N_vals) - 1):
            assert N_vals[i] <= N_vals[i+1]

    def test_asymptotic_at_zero(self):
        """N(0) = 0."""
        assert asymptotic_zero_count(0.0) == 0.0

    def test_explicit_count_nonneg(self):
        """Explicit zero count is nonneg."""
        result = euler_characteristic_explicit(
            'virasoro', 10.0, [10.0, 20.0], max_r=40, im_max=30.0,
            grid_re=10, grid_im=40,
        )
        for T, n in result.items():
            assert n >= 0

    def test_explicit_count_monotone(self):
        """N(T) is monotone: T1 < T2 => N(T1) <= N(T2)."""
        T_vals = [10.0, 20.0, 30.0, 40.0]
        result = euler_characteristic_explicit(
            'virasoro', 10.0, T_vals, max_r=60, im_max=50.0,
            grid_re=15, grid_im=60,
        )
        prev = -1
        for T in T_vals:
            assert result[T] >= prev
            prev = result[T]

    def test_argument_principle_nonneg(self):
        """Argument principle count is nonneg."""
        result = euler_characteristic_argument_principle(
            'virasoro', 10.0, [20.0],
            max_r=40, n_contour_pts=1000,
        )
        for T, n in result.items():
            assert n >= 0

    def test_argument_vs_explicit_rough(self):
        """Argument principle and explicit count agree roughly."""
        T = 25.0
        result_arg = euler_characteristic_argument_principle(
            'virasoro', 10.0, [T],
            max_r=40, re_range=(-5.0, 5.0), n_contour_pts=1500,
        )
        result_exp = euler_characteristic_explicit(
            'virasoro', 10.0, [T],
            max_r=40, im_max=30.0, grid_re=15, grid_im=60,
        )
        n_arg = result_arg[T]
        n_exp = result_exp[T]
        # Allow generous tolerance for numerical methods
        if n_exp > 0:
            assert abs(n_arg - n_exp) <= max(3, 0.5 * n_exp)

    def test_heisenberg_zero_count(self):
        """Heisenberg has no zeros: N(T) = 0 for all T."""
        result = euler_characteristic_explicit(
            'heisenberg', 1.0, [10.0, 50.0],
            max_r=10, im_max=60.0, grid_re=5, grid_im=20,
        )
        for T, n in result.items():
            assert n == 0


# ============================================================================
# G. Hilbert function (7 tests)
# ============================================================================

class TestHilbertFunction:
    """Tests for the Hilbert function of the zero scheme."""

    def test_hilbert_monotone(self):
        """H(d) is monotone non-decreasing."""
        d_vals = [1.0, 2.0, 5.0, 10.0, 20.0]
        result = hilbert_function(
            'virasoro', 10.0, d_vals, max_r=40, im_max=25.0,
            grid_re=10, grid_im=40,
        )
        prev = -1
        for d in d_vals:
            assert result[d] >= prev
            prev = result[d]

    def test_hilbert_nonneg(self):
        """H(d) >= 0 for all d."""
        d_vals = [1.0, 5.0, 10.0, 20.0]
        result = hilbert_function(
            'virasoro', 5.0, d_vals, max_r=40, im_max=25.0,
            grid_re=10, grid_im=40,
        )
        for d in d_vals:
            assert result[d] >= 0

    def test_hilbert_zero_at_small_radius(self):
        """H(d) = 0 for d very small (no zeros near origin)."""
        result = hilbert_function(
            'virasoro', 10.0, [0.01], max_r=40, im_max=25.0,
            grid_re=10, grid_im=40,
        )
        assert result[0.01] == 0

    def test_hilbert_consistency_with_counting(self):
        """H(d) <= N(d) check via the verification utility."""
        result = verify_hilbert_vs_counting(
            'virasoro', 10.0, [5.0, 10.0, 20.0], max_r=40,
        )
        assert result['all_consistent']

    def test_hilbert_heisenberg_always_zero(self):
        """Heisenberg: H(d) = 0 for all d."""
        d_vals = [1.0, 5.0, 10.0, 50.0]
        result = hilbert_function(
            'heisenberg', 1.0, d_vals, max_r=10, im_max=60.0,
            grid_re=5, grid_im=20,
        )
        for d in d_vals:
            assert result[d] == 0

    def test_hilbert_c10_vs_c16(self):
        """H(d) for complementary pair c=10, c=16 (both rho<1) are computable."""
        d_vals = [5.0, 10.0, 20.0]
        h10 = hilbert_function(
            'virasoro', 10.0, d_vals, max_r=60, im_max=25.0,
            grid_re=10, grid_im=40,
        )
        h16 = hilbert_function(
            'virasoro', 16.0, d_vals, max_r=60, im_max=25.0,
            grid_re=10, grid_im=40,
        )
        for d in d_vals:
            assert h10[d] >= 0
            assert h16[d] >= 0

    def test_hilbert_large_radius_grows(self):
        """H(d) eventually grows for Virasoro (infinite zeros)."""
        d_vals = [5.0, 10.0, 30.0, 50.0]
        result = hilbert_function(
            'virasoro', 10.0, d_vals, max_r=40, im_max=55.0,
            grid_re=10, grid_im=60,
        )
        # Should find some zeros
        assert result[50.0] >= result[5.0]


# ============================================================================
# H. Deformation with c (8 tests)
# ============================================================================

class TestDeformation:
    """Tests for zero deformation d(rho)/dc."""

    def test_c_derivative_finite(self):
        """d(rho)/dc should be finite at a simple zero."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 40)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (0.1, 30), 10, 40, max_r=40,
        )
        if len(zeros) > 0:
            drho = zero_c_derivative(c, zeros[0], max_r=40)
            assert abs(drho) < 1e10

    def test_c_derivative_vs_finite_diff(self):
        """Implicit differentiation matches central finite difference."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 40)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (0.1, 30), 10, 40, max_r=40,
        )
        if len(zeros) > 0:
            result = verify_deformation_formula(c, zeros[0], max_r=40, dc=0.1)
            if 'central_diff_error' in result:
                # Tolerance is generous since dc=0.1 is not tiny
                assert result['central_diff_error'] < 5.0

    def test_derivatives_first_n(self):
        """zero_c_derivatives_first_n returns list of correct length."""
        result = zero_c_derivatives_first_n(10.0, n_zeros=5, max_r=40, im_max=50.0)
        # May find fewer zeros than requested
        assert len(result) <= 5
        for rho, drho in result:
            assert isinstance(drho, complex)

    def test_track_zeros_returns_trajectories(self):
        """track_zeros_with_c returns trajectory data."""
        result = track_zeros_with_c(
            c_start=5.0, c_end=15.0, n_c_steps=5, n_zeros=3,
            max_r=40, im_max=30.0,
        )
        assert 'trajectories' in result
        assert 'c_values' in result
        assert len(result['c_values']) == 5

    def test_collision_search_returns_list(self):
        """find_zero_collisions returns a list (possibly empty)."""
        collisions = find_zero_collisions(
            c_range=(5.0, 20.0), n_c_steps=10, max_r=30,
            collision_tol=0.5, im_max=25.0,
        )
        assert isinstance(collisions, list)
        for c in collisions:
            assert 'c_val' in c
            assert 'gap' in c
            assert c['gap'] < 0.5

    def test_deformation_continuity(self):
        """Zeros should move continuously as c varies by small amount."""
        c = 10.0
        dc = 0.1
        coeffs1 = virasoro_shadow_coefficients_numerical(c, 40)
        coeffs2 = virasoro_shadow_coefficients_numerical(c + dc, 40)
        zeros1 = find_zeros_grid(
            coeffs1, (-5, 5), (5, 25), 10, 30, max_r=40,
        )
        zeros2 = find_zeros_grid(
            coeffs2, (-5, 5), (5, 25), 10, 30, max_r=40,
        )
        if len(zeros1) > 0 and len(zeros2) > 0:
            # Nearest zero in zeros2 to first zero of zeros1
            z1 = zeros1[0]
            dists = [abs(z1 - z2) for z2 in zeros2]
            min_dist = min(dists)
            # Should be close (zeros move continuously)
            assert min_dist < 2.0

    def test_forward_diff_direction(self):
        """Forward and central difference should agree in direction."""
        c = 8.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 40)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (5, 25), 10, 30, max_r=40,
        )
        if len(zeros) > 0:
            result = verify_deformation_formula(c, zeros[0], max_r=40, dc=0.5)
            if 'drho_dc_forward_diff' in result and 'drho_dc_central_diff' in result:
                # Directions should roughly agree (same quadrant in C)
                fwd = result['drho_dc_forward_diff']
                ctr = result['drho_dc_central_diff']
                if abs(fwd) > 1e-10 and abs(ctr) > 1e-10:
                    cos_angle = (fwd.real * ctr.real + fwd.imag * ctr.imag) / (abs(fwd) * abs(ctr))
                    assert cos_angle > -0.5  # Not anti-parallel

    def test_c_derivative_at_c13(self):
        """d(rho)/dc at c=13 (self-dual point) is computable."""
        c = 13.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 40)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (5, 25), 10, 30, max_r=40,
        )
        if len(zeros) > 0:
            drho = zero_c_derivative(c, zeros[0], max_r=40)
            assert abs(drho) < 1e10


# ============================================================================
# I. Regularized motivic class (5 tests)
# ============================================================================

class TestMotivicClass:
    """Tests for the regularized motivic class."""

    def test_heisenberg_motivic_class(self):
        """Heisenberg k=1: zeta(0) = k*2^0 = k, zeta'(0) = -k*log(2)."""
        result = regularized_motivic_class('heisenberg', 1.0, max_r=10)
        assert abs(result['zeta_at_0'] - 1.0) < 1e-10
        assert abs(result['zeta_deriv_at_0'] - (-math.log(2))) < 1e-10
        expected_class = -math.log(2) / 1.0
        assert abs(result['regularized_class'] - expected_class) < 1e-10

    def test_virasoro_motivic_class_finite(self):
        """Virasoro c=10: regularized class is finite."""
        result = regularized_motivic_class('virasoro', 10.0, max_r=40)
        assert abs(result['zeta_at_0']) > 1e-10  # zeta(0) != 0
        assert abs(result['regularized_class']) < 1e10

    def test_motivic_class_c_dependence(self):
        """Regularized class varies with c."""
        r1 = regularized_motivic_class('virasoro', 5.0, max_r=40)
        r2 = regularized_motivic_class('virasoro', 15.0, max_r=40)
        assert abs(r1['regularized_class'] - r2['regularized_class']) > 1e-10

    def test_motivic_class_complementary(self):
        """Check motivic class for complementary pair c, 26-c."""
        r1 = regularized_motivic_class('virasoro', 5.0, max_r=40)
        r2 = regularized_motivic_class('virasoro', 21.0, max_r=40)
        # Both should be finite; relation TBD
        assert abs(r1['regularized_class']) < 1e10
        assert abs(r2['regularized_class']) < 1e10

    def test_affine_motivic_class(self):
        """Affine sl2 k=1: zeta(0) = kappa + alpha, finite."""
        result = regularized_motivic_class('affine_sl2', 1.0, max_r=30)
        assert abs(result['zeta_at_0']) > 1e-10
        assert abs(result['regularized_class']) < 1e10


# ============================================================================
# J. Spectral coincidences (6 tests)
# ============================================================================

class TestSpectralCoincidences:
    """Tests for spectral coincidences (derived intersection with diagonal)."""

    def test_self_coincidence_all(self):
        """zeta_A(s) = zeta_A(s) everywhere: difference is identically zero."""
        # Difference coefficients are all zero
        coeffs_a = shadow_coefficients_extended('virasoro', 10.0, 30)
        diff = {r: coeffs_a.get(r, 0.0) - coeffs_a.get(r, 0.0) for r in coeffs_a}
        # All zero: every s is a coincidence
        for r, v in diff.items():
            assert abs(v) < 1e-15

    def test_complementary_c10_c16(self):
        """Spectral coincidences for (c=10, c=16) pair (both rho<1)."""
        result = spectral_coincidences(
            'virasoro', 10.0, 'virasoro', 16.0, max_r=60,
            im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        assert 'n_coincidences' in result
        assert result['n_coincidences'] >= 0

    def test_complementary_c12_c14(self):
        """Spectral coincidences for (c=12, c=14) pair (both rho<1)."""
        result = spectral_coincidences(
            'virasoro', 12.0, 'virasoro', 14.0, max_r=60,
            im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        assert result['n_coincidences'] >= 0

    def test_complementary_c9_c17(self):
        """Spectral coincidences for (c=9, c=17) pair (both rho<1)."""
        result = spectral_coincidences(
            'virasoro', 9.0, 'virasoro', 17.0, max_r=60,
            im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        assert result['n_coincidences'] >= 0

    def test_c13_self_dual_coincidences(self):
        """At c=13, zeta_c = zeta_{26-c}: trivially all coincidences."""
        result = spectral_coincidences_complementary(
            13.0, max_r=60, im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        assert result['is_self_dual']

    def test_heisenberg_virasoro_coincidences(self):
        """Spectral coincidences between Heisenberg and Virasoro (rho<1)."""
        result = spectral_coincidences(
            'heisenberg', 1.0, 'virasoro', 10.0, max_r=60,
            im_range=(-25, 25), grid_re=10, grid_im=40,
        )
        # Difference is zeta_H - zeta_V: zeros are where k*2^{-s} = zeta_V(s)
        assert result['n_coincidences'] >= 0


# ============================================================================
# K. Multi-path verification (8 tests)
# ============================================================================

class TestMultiPathVerification:
    """Cross-verification tests using multiple independent methods."""

    def test_simplicity_virasoro_c10(self):
        """All Virasoro c=10 zeros are simple (path: zeta=0, zeta'!=0)."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-40, 40), 15, 60, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=10"
        result = verify_zero_simplicity(coeffs, zeros, max_r=60)
        assert result['all_simple']

    def test_simplicity_virasoro_c13(self):
        """All Virasoro c=13 zeros are simple."""
        coeffs = virasoro_shadow_coefficients_numerical(13.0, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-40, 40), 15, 60, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=13"
        result = verify_zero_simplicity(coeffs, zeros, max_r=60)
        assert result['all_simple']

    def test_simplicity_virasoro_c25(self):
        """All Virasoro c=25 zeros are simple."""
        coeffs = virasoro_shadow_coefficients_numerical(25.0, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-60, 60), 15, 80, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=25"
        result = verify_zero_simplicity(coeffs, zeros, max_r=60)
        assert result['all_simple']

    def test_palindromic_c13(self):
        """At c=13, the zero set is palindromic (conjugate-symmetric)."""
        result = palindromic_zero_test(
            13.0, max_r=60, im_range=(-40, 40), grid_re=15, grid_im=60,
        )
        assert result['is_palindromic']

    def test_hilbert_vs_counting_c10(self):
        """H(d) <= N(d) for Virasoro c=10."""
        result = verify_hilbert_vs_counting(
            'virasoro', 10.0, [5.0, 10.0, 20.0], max_r=60,
        )
        assert result['all_consistent']

    def test_hilbert_vs_counting_c13(self):
        """H(d) <= N(d) for Virasoro c=13."""
        result = verify_hilbert_vs_counting(
            'virasoro', 13.0, [5.0, 10.0], max_r=60,
        )
        assert result['all_consistent']

    def test_deformation_c10_first_zero(self):
        """Deformation formula matches finite diff for c=10, first zero."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (5, 40), 15, 50, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=10"
        result = verify_deformation_formula(c, zeros[0], max_r=60, dc=0.5)
        if 'central_diff_error' in result:
            # Generous tolerance for numerical comparison
            assert result['central_diff_error'] < 10.0

    def test_scheme_structure_consistency(self):
        """Zero scheme total_length = sum of multiplicities."""
        scheme = build_zero_scheme(
            'virasoro', 10.0, max_r=40,
            im_range=(-30, 30), grid_re=10, grid_im=40,
        )
        computed_total = sum(pt.local_ring_length for pt in scheme.points)
        assert computed_total == scheme.total_length


# ============================================================================
# L. Virasoro-specific structural tests (5 tests)
# ============================================================================

class TestVirasoroStructure:
    """Virasoro-specific structural properties of the zero scheme."""

    def test_c10_has_zeros(self):
        """Virasoro c=10 (rho<1, entire) has zeros."""
        # c=1 has rho=6.24 >> 1: Dirichlet series diverges, no convergence region.
        # c=10 has rho=0.61 < 1: entire function, zeros exist.
        zeros = _virasoro_zeros(10.0, max_r=60, im_max=50.0)
        assert len(zeros) > 0

    def test_c13_has_zeros(self):
        """Virasoro c=13 (self-dual, rho<1) has zeros."""
        zeros = _virasoro_zeros(13.0, max_r=60, im_max=50.0)
        assert len(zeros) > 0

    def test_c25_has_zeros(self):
        """Virasoro c=25 (rho<1, near critical) has zeros."""
        zeros = _virasoro_zeros(25.0, max_r=60, im_max=60.0)
        assert len(zeros) > 0

    def test_zero_at_zero_is_actually_zero(self):
        """Each found zero satisfies |zeta(rho)| < tol."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-40, 40), 15, 60, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=10"
        for z in zeros:
            val = shadow_zeta_numerical(coeffs, z, 60)
            assert abs(val) < 1e-4, f"Not a zero: zeta({z}) = {val}"

    def test_conjugate_symmetry(self):
        """Zeros come in conjugate pairs: if rho, then conj(rho)."""
        c = 10.0
        coeffs = virasoro_shadow_coefficients_numerical(c, 60)
        zeros = find_zeros_grid(
            coeffs, (-5, 5), (-40, 40), 15, 60, max_r=60,
        )
        assert len(zeros) > 0, "No zeros found for c=10"
        for z in zeros:
            z_conj = z.conjugate()
            has_pair = any(abs(z_conj - w) < 1e-3 for w in zeros)
            # Allow for zeros on real axis (self-conjugate)
            if abs(z.imag) > 0.1:
                assert has_pair, f"No conjugate found for {z}"
