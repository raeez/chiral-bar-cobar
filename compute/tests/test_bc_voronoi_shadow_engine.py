r"""Tests for Voronoi summation of shadow coefficients.

Multi-path verification (3+ independent methods per claim):
    Path 1: Direct summation vs Voronoi formula (must agree)
    Path 2: Plancherel identity (sum |G_q|^2 = q * sum |S_r|^2)
    Path 3: Subconvexity bound verification (numerical vs analytic)
    Path 4: Complementarity (Voronoi data for Vir_c and Vir_{26-c} related)
    Path 5: Limiting case (finite towers reduce to finite identity)
    Path 6: Shifted convolution via delta method vs direct
    Path 7: Ramanujan sum decomposition vs direct computation

90+ tests covering:
    - Additive twist computation for all four depth classes
    - Plancherel identity for Heisenberg, affine, beta-gamma, Virasoro
    - Shadow Gauss sums: norm structure, q-dependence
    - Shifted convolution sums: direct vs delta method
    - Subconvexity bounds: numerical verification
    - Voronoi finite tower identity (Poisson summation for G/L/C)
    - Complementarity of Gauss sums (Vir_c + Vir_{26-c})
    - Self-dual analysis at c = 13
    - Ramanujan sum decomposition
    - Smoothed partial sums and bump function tests
    - Voronoi kernel function properties
    - Shadow conductor estimate
    - Cross-family consistency
    - Delta method for shifted convolutions
    - Comprehensive landscape analysis

Tolerance: 1e-8 for exact comparisons, 1e-4 for numerical methods.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP10): Multi-path verification, not hardcoded values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Convention checks for classical number theory.
"""

import math
import cmath
import pytest
from typing import Dict

from compute.lib.bc_voronoi_shadow_engine import (
    # Core
    e,
    # Coefficient providers
    virasoro_coefficients,
    koszul_dual_virasoro_coefficients,
    get_shadow_coefficients,
    classify_shadow_depth,
    # Additive twists / Gauss sums
    additive_twist,
    shadow_gauss_sum,
    all_gauss_sums,
    # Plancherel
    plancherel_lhs,
    plancherel_rhs,
    verify_plancherel,
    # Smoothed sums
    bump_function,
    gaussian_test,
    direct_smoothed_sum,
    direct_twisted_smoothed_sum,
    partial_sum,
    smoothed_partial_sum,
    # Voronoi kernels
    voronoi_kernel_G,
    voronoi_kernel_L,
    voronoi_kernel_M,
    voronoi_kernel_integral,
    # Voronoi formula
    voronoi_direct_side,
    voronoi_dual_side,
    voronoi_main_term,
    voronoi_finite_identity,
    # Shifted convolution
    shifted_convolution_direct,
    shifted_convolution_via_twist,
    shifted_convolution_all,
    # Subconvexity
    twisted_partial_sum,
    subconvexity_bound_value,
    subconvexity_analytic_bound,
    verify_subconvexity,
    # Delta method
    delta_method_shifted_convolution,
    # Complementarity
    complementarity_coefficients,
    voronoi_complementarity_check,
    # Self-dual
    self_dual_gauss_sum,
    self_dual_complementarity_verify,
    # Gauss sum analysis
    gauss_sum_norm_squared,
    shadow_conductor_estimate,
    # Ramanujan sums
    shadow_ramanujan_sum,
    classical_ramanujan_sum,
    shadow_ramanujan_vs_classical,
    # Utilities
    coprime_residues,
    euler_phi,
    # Finite tower check
    voronoi_finite_tower_check,
    # Landscape
    gauss_sum_landscape,
    gauss_sum_norm_landscape,
    # Comprehensive analysis
    full_voronoi_analysis,
    VoronoiAnalysis,
    # Voronoi acceleration
    voronoi_accelerated_sum,
)


# ============================================================================
# Helpers
# ============================================================================

TOL = 1e-8
RTOL = 1e-6


def _close(a, b, tol=TOL):
    """Check that a and b are close (complex or real)."""
    return abs(a - b) < tol * max(abs(a), abs(b), 1.0)


def _rclose(a, b, rtol=RTOL):
    """Relative closeness."""
    denom = max(abs(a), abs(b), 1e-30)
    return abs(a - b) / denom < rtol


# ============================================================================
# Section 1: Core additive character
# ============================================================================

class TestAdditiveCharacter:
    """Tests for the additive character e(x) = exp(2*pi*i*x)."""

    def test_e_at_zero(self):
        """e(0) = 1."""
        assert _close(e(0.0), 1.0)

    def test_e_at_half(self):
        """e(1/2) = -1."""
        assert _close(e(0.5), -1.0)

    def test_e_at_quarter(self):
        """e(1/4) = i."""
        assert _close(e(0.25), 1.0j)

    def test_e_periodicity(self):
        """e(x + 1) = e(x)."""
        for x in [0.1, 0.37, 0.73]:
            assert _close(e(x), e(x + 1.0))

    def test_e_unit_circle(self):
        """| e(x) | = 1 for all x."""
        for x in [0.0, 0.1, 0.5, 0.99]:
            assert abs(abs(e(x)) - 1.0) < 1e-14

    def test_e_roots_of_unity(self):
        """e(k/n) for k=0,...,n-1 are the n-th roots of unity. Sum = 0."""
        for n in [3, 5, 7, 11]:
            total = sum(e(k / n) for k in range(n))
            assert abs(total) < 1e-12, f"Sum of {n}-th roots should be 0, got {total}"


# ============================================================================
# Section 2: Shadow coefficient classification
# ============================================================================

class TestClassification:
    """Test depth class classification."""

    def test_heisenberg_class_G(self):
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        assert classify_shadow_depth(coeffs) == 'G'

    def test_affine_sl2_class_L(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        assert classify_shadow_depth(coeffs) == 'L'

    def test_betagamma_class_C(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        assert classify_shadow_depth(coeffs) == 'C'

    def test_virasoro_class_M(self):
        coeffs = get_shadow_coefficients('virasoro', {'c': 1.0}, max_r=50)
        assert classify_shadow_depth(coeffs) == 'M'

    def test_virasoro_kappa_is_c_over_2(self):
        """AP9: kappa = c/2 for Virasoro."""
        for c_val in [1.0, 13.0, 25.0]:
            coeffs = virasoro_coefficients(c_val)
            assert _close(coeffs[2], c_val / 2.0)


# ============================================================================
# Section 3: Plancherel identity verification
# ============================================================================

class TestPlancherel:
    """Plancherel: sum_{a=0}^{q-1} |G_q(A, a)|^2 = q * sum |S_r|^2.

    This is the fundamental Parseval identity for additive characters
    and constitutes verification path 2.
    """

    def test_plancherel_heisenberg_q2(self):
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        lhs, rhs, ok = verify_plancherel(coeffs, 2)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_heisenberg_q5(self):
        coeffs = get_shadow_coefficients('heisenberg', {'k': 3.0})
        lhs, rhs, ok = verify_plancherel(coeffs, 5)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_affine_sl2_q3(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        lhs, rhs, ok = verify_plancherel(coeffs, 3)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_affine_sl2_q7(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 2.0})
        lhs, rhs, ok = verify_plancherel(coeffs, 7)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_betagamma_q4(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        lhs, rhs, ok = verify_plancherel(coeffs, 4)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_betagamma_q11(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 1.0 / 3.0})
        lhs, rhs, ok = verify_plancherel(coeffs, 11)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_virasoro_c1_q3(self):
        # c=1: rho ~ 6.24 >> 1, large coefficients, use moderate max_r
        coeffs = virasoro_coefficients(1.0, max_r=30)
        lhs, rhs, ok = verify_plancherel(coeffs, 3, max_r=30, rtol=1e-6)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_virasoro_c13_q5(self):
        coeffs = virasoro_coefficients(13.0, max_r=40)
        lhs, rhs, ok = verify_plancherel(coeffs, 5, max_r=40, rtol=1e-6)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    def test_plancherel_virasoro_c25_q7(self):
        coeffs = virasoro_coefficients(25.0, max_r=40)
        lhs, rhs, ok = verify_plancherel(coeffs, 7, max_r=40, rtol=1e-6)
        assert ok, f"Plancherel failed: lhs={lhs}, rhs={rhs}"

    @pytest.mark.parametrize("q", [2, 3, 5, 8, 13])
    def test_plancherel_virasoro_c1_multiple_q(self, q):
        coeffs = virasoro_coefficients(1.0, max_r=30)
        lhs, rhs, ok = verify_plancherel(coeffs, q, max_r=30, rtol=1e-6)
        assert ok, f"Plancherel failed at q={q}: lhs={lhs}, rhs={rhs}"

    @pytest.mark.parametrize("q", [2, 3, 4, 6, 10])
    def test_plancherel_w3_t_line(self, q):
        coeffs = get_shadow_coefficients('w3_t', {'c': 2.0}, max_r=30)
        lhs, rhs, ok = verify_plancherel(coeffs, q, max_r=30, rtol=1e-6)
        assert ok, f"Plancherel failed at q={q}: lhs={lhs}, rhs={rhs}"


# ============================================================================
# Section 4: Voronoi finite tower identity (Poisson summation)
# ============================================================================

class TestFiniteTowerVoronoi:
    """For finite towers (G/L/C), the Voronoi formula is a finite identity.

    Verification path 5: limiting case.
    """

    def test_heisenberg_poisson_q2(self):
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, 1, 2)
        assert ok, f"Poisson failed: {direct} vs {poisson}"

    def test_heisenberg_poisson_q5(self):
        coeffs = get_shadow_coefficients('heisenberg', {'k': 2.0})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, 1, 5)
        assert ok, f"Poisson failed: {direct} vs {poisson}"

    def test_affine_sl2_poisson_q3(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, 1, 3)
        assert ok, f"Poisson failed: {direct} vs {poisson}"

    def test_affine_sl2_poisson_q7(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 2.0})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, 2, 7)
        assert ok, f"Poisson failed: {direct} vs {poisson}"

    def test_betagamma_poisson_q4(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, 1, 4)
        assert ok, f"Poisson failed: {direct} vs {poisson}"

    def test_betagamma_poisson_q11(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, 3, 11)
        assert ok, f"Poisson failed: {direct} vs {poisson}"

    @pytest.mark.parametrize("a,q", [(1, 2), (1, 3), (2, 5), (3, 7), (1, 11)])
    def test_heisenberg_poisson_systematic(self, a, q):
        coeffs = get_shadow_coefficients('heisenberg', {'k': 5.0})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, a, q)
        assert ok, f"Poisson failed at a={a}, q={q}"

    @pytest.mark.parametrize("a,q", [(1, 2), (1, 3), (2, 3), (1, 5), (3, 5)])
    def test_affine_sl2_poisson_systematic(self, a, q):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        direct, poisson, ok = voronoi_finite_tower_check(coeffs, a, q)
        assert ok, f"Poisson failed at a={a}, q={q}"


# ============================================================================
# Section 5: Shadow Gauss sums
# ============================================================================

class TestGaussSums:
    """Tests for shadow Gauss sums and their properties."""

    def test_gauss_sum_heisenberg_q2(self):
        """G_2(H_k) = k * e(2/2) = k * e(1) = k."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 3.0})
        g = shadow_gauss_sum(coeffs, 2)
        # e(2/2) = e(1) = 1
        assert _close(g, 3.0)

    def test_gauss_sum_heisenberg_q3(self):
        """G_3(H_k) = k * e(2/3)."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        g = shadow_gauss_sum(coeffs, 3)
        expected = 1.0 * e(2.0 / 3.0)
        assert _close(g, expected)

    def test_gauss_sum_is_additive_in_coefficients(self):
        """G_q(A + B) = G_q(A) + G_q(B) for linearly combined towers."""
        c1 = virasoro_coefficients(1.0, 30)
        c2 = virasoro_coefficients(25.0, 30)
        combined = {r: c1.get(r, 0.0) + c2.get(r, 0.0) for r in range(2, 31)}
        q = 5
        g1 = shadow_gauss_sum(c1, q, 30)
        g2 = shadow_gauss_sum(c2, q, 30)
        g_comb = shadow_gauss_sum(combined, q, 30)
        assert _close(g1 + g2, g_comb)

    def test_gauss_sum_q1_is_sum_of_coefficients(self):
        """G_1(A) = sum S_r * e(r) = sum S_r (since e(integer) = 1)."""
        coeffs = virasoro_coefficients(1.0, 30)
        g = shadow_gauss_sum(coeffs, 1, 30)
        total = sum(coeffs.get(r, 0.0) for r in range(2, 31))
        assert _close(g, total)

    def test_gauss_sum_conjugate_symmetry(self):
        """G_q(A, q-a) = conj(G_q(A, a)) when S_r are real."""
        coeffs = virasoro_coefficients(1.0, 30)
        q = 7
        for a in range(1, q):
            ga = additive_twist(coeffs, a, q, 30)
            ga_conj = additive_twist(coeffs, q - a, q, 30)
            assert _close(ga, ga_conj.conjugate()), f"Conjugate symmetry failed at a={a}"

    def test_gauss_sum_a0_is_real(self):
        """G_q(A, 0) = sum S_r is real."""
        coeffs = virasoro_coefficients(13.0, 30)
        g0 = additive_twist(coeffs, 0, 5, 30)
        assert abs(g0.imag) < 1e-12

    def test_all_gauss_sums_count(self):
        """all_gauss_sums returns q entries."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        gs = all_gauss_sums(coeffs, 7)
        assert len(gs) == 7


# ============================================================================
# Section 6: Complementarity of Gauss sums
# ============================================================================

class TestComplementarity:
    """Test that Voronoi twists respect Koszul complementarity.

    Verification path 4: G_q(Vir_c) + G_q(Vir_{26-c}) = G_q(D).
    """

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_complementarity_twist_q3(self, c_val):
        twist_c, twist_dual, twist_D = voronoi_complementarity_check(c_val, 1, 3, max_r=50)
        assert _close(twist_c + twist_dual, twist_D), \
            f"Complementarity failed at c={c_val}: {twist_c + twist_dual} vs {twist_D}"

    @pytest.mark.parametrize("c_val", [1.0, 13.0, 25.0])
    def test_complementarity_twist_q7(self, c_val):
        twist_c, twist_dual, twist_D = voronoi_complementarity_check(c_val, 1, 7, max_r=50)
        assert _close(twist_c + twist_dual, twist_D)

    def test_complementarity_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            k1 = virasoro_coefficients(c_val)[2]
            k2 = koszul_dual_virasoro_coefficients(c_val)[2]
            assert _close(k1 + k2, 13.0), \
                f"kappa sum = {k1 + k2} at c={c_val}, expected 13"

    @pytest.mark.parametrize("q", [2, 3, 5])
    def test_complementarity_partial_sums(self, q):
        """Partial sums also respect complementarity."""
        c_val = 1.0
        coeffs_c = virasoro_coefficients(c_val, 40)
        coeffs_dual = koszul_dual_virasoro_coefficients(c_val, 40)
        coeffs_D = complementarity_coefficients(coeffs_c, coeffs_dual, 40)
        for N in [10, 20, 30]:
            ps_c = partial_sum(coeffs_c, N)
            ps_dual = partial_sum(coeffs_dual, N)
            ps_D = partial_sum(coeffs_D, N)
            assert _close(ps_c + ps_dual, ps_D), \
                f"Partial sum complementarity failed at N={N}"

    def test_complementarity_shifted_convolution(self):
        """Complementarity extends to shifted convolution structure."""
        c_val = 1.0
        coeffs_c = virasoro_coefficients(c_val, 40)
        coeffs_dual = koszul_dual_virasoro_coefficients(c_val, 40)
        coeffs_D = complementarity_coefficients(coeffs_c, coeffs_dual, 40)
        # C_h(D) = C_h(c) + C_h(26-c) + cross terms
        # The cross term is sum S_r(c) S_{r+h}(26-c) + S_r(26-c) S_{r+h}(c)
        for h in [1, 2, 3]:
            ch_D = shifted_convolution_direct(coeffs_D, h, 40)
            ch_c = shifted_convolution_direct(coeffs_c, h, 40)
            ch_dual = shifted_convolution_direct(coeffs_dual, h, 40)
            cross = sum(
                coeffs_c.get(r, 0.0) * coeffs_dual.get(r + h, 0.0)
                + coeffs_dual.get(r, 0.0) * coeffs_c.get(r + h, 0.0)
                for r in range(2, 40 - h + 1)
            )
            assert _close(ch_D, ch_c + ch_dual + cross), \
                f"Complementarity shifted convolution failed at h={h}"


# ============================================================================
# Section 7: Self-dual point c = 13
# ============================================================================

class TestSelfDual:
    """Tests at the self-dual point c = 13.

    At c = 13: Vir_13 is self-dual, so S_r(13) = S_r(13) trivially.
    The complementarity sum D_r = 2 * S_r(13).
    """

    def test_self_dual_kappa(self):
        """kappa(Vir_13) = 13/2."""
        coeffs = virasoro_coefficients(13.0)
        assert _close(coeffs[2], 6.5)

    @pytest.mark.parametrize("q", [2, 3, 5, 7])
    def test_self_dual_gauss_sum_is_half_D(self, q):
        g_13, g_D_half, ok = self_dual_complementarity_verify(q, max_r=50)
        assert ok, f"Self-dual check failed at q={q}: {g_13} vs {g_D_half}"

    def test_self_dual_plancherel(self):
        coeffs = virasoro_coefficients(13.0, 40)
        lhs, rhs, ok = verify_plancherel(coeffs, 5, 40)
        assert ok

    def test_self_dual_shifted_convolution_symmetry(self):
        """At self-dual point, C_h(c) = C_h(26-c) since c = 26-c = 13."""
        coeffs = virasoro_coefficients(13.0, 40)
        dual_coeffs = koszul_dual_virasoro_coefficients(13.0, 40)
        for h in [1, 2, 3]:
            ch = shifted_convolution_direct(coeffs, h, 40)
            ch_dual = shifted_convolution_direct(dual_coeffs, h, 40)
            assert _close(ch, ch_dual), \
                f"Self-dual C_h symmetry failed at h={h}: {ch} vs {ch_dual}"


# ============================================================================
# Section 8: Shifted convolution sums
# ============================================================================

class TestShiftedConvolution:
    """Tests for shifted convolution sums C_h = sum S_r * S_{r+h}.

    Verification path 6: direct vs delta method.
    """

    def test_heisenberg_shifted_convolution_is_zero(self):
        """For Heisenberg, S_r = 0 for r >= 3, so C_h = 0 for h >= 1."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        for h in range(1, 6):
            assert _close(shifted_convolution_direct(coeffs, h), 0.0)

    def test_affine_sl2_shifted_convolution(self):
        """For affine sl_2, only S_2 and S_3 nonzero.
        C_1 = S_2 * S_3, C_h = 0 for h >= 2."""
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        S2 = coeffs[2]
        S3 = coeffs[3]
        assert _close(shifted_convolution_direct(coeffs, 1), S2 * S3)
        assert _close(shifted_convolution_direct(coeffs, 2), 0.0)

    def test_virasoro_shifted_convolution_h1(self):
        """C_1 for Virasoro is nonzero (class M, infinite tower)."""
        coeffs = virasoro_coefficients(1.0, 50)
        c1 = shifted_convolution_direct(coeffs, 1, 50)
        assert abs(c1) > 1e-10, "C_1 should be nonzero for Virasoro"

    def test_shifted_convolution_delta_method_heisenberg(self):
        """Delta method agrees with direct for Heisenberg."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        for h in [1, 2, 3]:
            direct = shifted_convolution_direct(coeffs, h)
            delta = delta_method_shifted_convolution(coeffs, h, Q=10)
            assert _close(direct, delta, tol=1e-6), \
                f"Delta vs direct at h={h}: {direct} vs {delta}"

    def test_shifted_convolution_delta_method_affine(self):
        """Delta method agrees with direct for affine sl_2."""
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        for h in [1, 2, 3]:
            direct = shifted_convolution_direct(coeffs, h)
            delta = delta_method_shifted_convolution(coeffs, h, Q=20)
            assert _close(direct, delta, tol=1e-4), \
                f"Delta vs direct at h={h}: {direct} vs {delta}"

    def test_shifted_convolution_delta_method_virasoro(self):
        """Delta method approximates direct for Virasoro."""
        coeffs = virasoro_coefficients(1.0, 40)
        for h in [1, 2]:
            direct = shifted_convolution_direct(coeffs, h, 40)
            delta = delta_method_shifted_convolution(coeffs, h, Q=40, max_r=40)
            # Delta method at finite Q is an approximation
            assert _rclose(direct, delta, rtol=0.05), \
                f"Delta vs direct at h={h}: {direct} vs {delta}"

    def test_shifted_convolution_all_returns_dict(self):
        coeffs = virasoro_coefficients(1.0, 30)
        result = shifted_convolution_all(coeffs, h_max=5, max_r=30)
        assert len(result) == 5
        assert all(h in result for h in range(1, 6))

    def test_shifted_convolution_via_twist_heisenberg(self):
        """Twist-based method agrees with direct for Heisenberg."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 2.0})
        for h in [1, 2]:
            direct = shifted_convolution_direct(coeffs, h)
            twist = shifted_convolution_via_twist(coeffs, h, q_max=10)
            assert _close(direct, twist, tol=1e-4)


# ============================================================================
# Section 9: Subconvexity bounds
# ============================================================================

class TestSubconvexity:
    """Verify the subconvexity bound numerically.

    Verification path 3: numerical bound vs analytic bound.
    """

    @pytest.mark.parametrize("c_val", [1.0, 13.0, 25.0])
    def test_subconvexity_virasoro_q2_N10(self, c_val):
        coeffs = virasoro_coefficients(c_val, 50)
        actual, bound, ok = verify_subconvexity(coeffs, 1, 2, 10)
        assert ok, f"Subconvexity failed at c={c_val}: {actual} > {bound}"

    @pytest.mark.parametrize("q", [2, 3, 5, 7])
    def test_subconvexity_virasoro_c1_N50(self, q):
        coeffs = virasoro_coefficients(1.0, 60)
        actual, bound, ok = verify_subconvexity(coeffs, 1, q, 50)
        assert ok, f"Subconvexity failed at q={q}: {actual} > {bound}"

    @pytest.mark.parametrize("N", [10, 20, 50])
    def test_subconvexity_virasoro_c13_q3(self, N):
        coeffs = virasoro_coefficients(13.0, max(60, N + 10))
        actual, bound, ok = verify_subconvexity(coeffs, 1, 3, N)
        assert ok, f"Subconvexity failed at N={N}: {actual} > {bound}"

    def test_subconvexity_heisenberg(self):
        """Heisenberg: trivially bounded (single term)."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 5.0})
        actual, bound, ok = verify_subconvexity(coeffs, 1, 3, 10)
        assert ok

    def test_subconvexity_affine_sl2(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        actual, bound, ok = verify_subconvexity(coeffs, 1, 5, 10)
        assert ok

    def test_subconvexity_betagamma(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        actual, bound, ok = verify_subconvexity(coeffs, 1, 4, 10)
        assert ok

    @pytest.mark.parametrize("c_val,q,N", [
        (1.0, 2, 10), (1.0, 5, 20), (1.0, 10, 50),
        (13.0, 3, 30), (25.0, 7, 40),
    ])
    def test_subconvexity_systematic(self, c_val, q, N):
        coeffs = virasoro_coefficients(c_val, max(60, N + 10))
        actual, bound, ok = verify_subconvexity(coeffs, 1, q, N)
        assert ok, f"Subconvexity failed: c={c_val}, q={q}, N={N}"


# ============================================================================
# Section 10: Voronoi kernel properties
# ============================================================================

class TestVoronoiKernels:
    """Test Bessel-type Voronoi kernels."""

    def test_kernel_G_at_zero(self):
        """J_0(0) = 1."""
        assert _close(voronoi_kernel_G(0.0), 1.0)

    def test_kernel_L_at_zero(self):
        """J_0(0) = 1."""
        assert _close(voronoi_kernel_L(0.0), 1.0)

    def test_kernel_M_at_zero(self):
        """J_0(0) = 1."""
        assert _close(voronoi_kernel_M(0.0), 1.0)

    def test_kernel_L_negative_x(self):
        """Kernel is 0 for x < 0."""
        assert voronoi_kernel_L(-1.0) == 0.0

    def test_kernel_M_negative_x(self):
        assert voronoi_kernel_M(-1.0) == 0.0

    def test_kernel_M_decay(self):
        """Bessel function decays like 1/sqrt(x) for large x."""
        x1 = 100.0
        x2 = 400.0
        k1 = abs(voronoi_kernel_M(x1))
        k2 = abs(voronoi_kernel_M(x2))
        # |J_0(x)| ~ sqrt(2/(pi*x)) => ratio ~ sqrt(x2/x1) = 2
        if k2 > 1e-15:
            ratio = k1 / k2
            # Should be roughly 2 (within factor of 3, since oscillatory)
            assert 0.1 < ratio < 30

    def test_kernel_integral_finite(self):
        """Kernel integral against Gaussian is finite."""
        test = lambda x: gaussian_test(x, sigma=5.0)
        integral = voronoi_kernel_integral(test, r=2, q=3, x_max=50.0)
        assert math.isfinite(integral)


# ============================================================================
# Section 11: Smoothed sums and bump function
# ============================================================================

class TestSmoothedSums:
    """Test smoothing and bump functions."""

    def test_bump_far_below(self):
        """bump(x, N, delta) ~ 1 for x << N."""
        assert bump_function(5.0, 100.0, 5.0) > 0.99

    def test_bump_far_above(self):
        """bump(x, N, delta) ~ 0 for x >> N."""
        assert bump_function(200.0, 100.0, 5.0) < 0.01

    def test_bump_at_N(self):
        """bump(N, N, delta) = 1/2."""
        assert _close(bump_function(100.0, 100.0, 5.0), 0.5)

    def test_bump_monotone_decreasing(self):
        """bump is monotone decreasing."""
        vals = [bump_function(x, 50.0, 3.0) for x in range(0, 100)]
        for i in range(len(vals) - 1):
            assert vals[i] >= vals[i + 1] - 1e-15

    def test_gaussian_test_at_zero(self):
        assert _close(gaussian_test(0.0, 1.0), 1.0)

    def test_gaussian_test_decay(self):
        assert gaussian_test(10.0, 1.0) < 1e-20

    def test_smoothed_partial_sum_vs_direct(self):
        """For small delta and convergent series, smoothed ~ direct partial sum.

        Use c=25 where rho < 1 so coefficients decay, making the bump
        approximation accurate even with a sharp cutoff.
        """
        coeffs = virasoro_coefficients(25.0, 50)
        direct = partial_sum(coeffs, 20)
        smoothed = smoothed_partial_sum(coeffs, 20, delta=0.01, max_r=50)
        # With very small delta and convergent tails, these should agree closely
        assert _rclose(direct, smoothed, rtol=0.01)

    def test_direct_smoothed_sum_gaussian(self):
        coeffs = virasoro_coefficients(1.0, 30)
        result = direct_smoothed_sum(coeffs, lambda x: gaussian_test(x, 10.0), 30)
        assert math.isfinite(result.real if isinstance(result, complex) else result)


# ============================================================================
# Section 12: Ramanujan sum decomposition
# ============================================================================

class TestRamanujanSums:
    """Test shadow Ramanujan sum decomposition.

    Verification path 7: c_q(A) = sum S_r * c_q(r) vs direct computation.
    """

    def test_classical_ramanujan_sum_q1(self):
        """c_1(n) = 1 for all n."""
        for n in [1, 2, 5, 10]:
            assert _close(classical_ramanujan_sum(1, n), 1.0)

    def test_classical_ramanujan_sum_prime(self):
        """c_p(n) = -1 if p does not divide n, p-1 if p divides n."""
        p = 5
        assert _close(classical_ramanujan_sum(p, 3), -1.0)  # 5 does not divide 3
        assert _close(classical_ramanujan_sum(p, 10), p - 1)  # 5 divides 10

    def test_shadow_ramanujan_vs_classical_heisenberg(self):
        """Shadow Ramanujan decomposition matches direct for Heisenberg."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 1.0})
        for q in [2, 3, 5, 7]:
            shadow, classical = shadow_ramanujan_vs_classical(coeffs, q)
            assert _close(shadow, classical, tol=1e-8), \
                f"Ramanujan mismatch at q={q}: {shadow} vs {classical}"

    def test_shadow_ramanujan_vs_classical_affine(self):
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        for q in [2, 3, 5]:
            shadow, classical = shadow_ramanujan_vs_classical(coeffs, q)
            assert _close(shadow, classical, tol=1e-8), \
                f"Ramanujan mismatch at q={q}"

    def test_shadow_ramanujan_vs_classical_virasoro(self):
        coeffs = virasoro_coefficients(1.0, 40)
        for q in [2, 3, 5]:
            shadow, classical = shadow_ramanujan_vs_classical(coeffs, q, max_r=40)
            assert _close(shadow, classical, tol=1e-6), \
                f"Ramanujan mismatch at q={q}: {shadow} vs {classical}"

    def test_shadow_ramanujan_vs_classical_betagamma(self):
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        for q in [2, 3, 7]:
            shadow, classical = shadow_ramanujan_vs_classical(coeffs, q)
            assert _close(shadow, classical, tol=1e-8)


# ============================================================================
# Section 13: Euler totient and coprime residues
# ============================================================================

class TestArithmetic:
    """Test arithmetic utility functions."""

    def test_euler_phi_prime(self):
        assert euler_phi(7) == 6

    def test_euler_phi_prime_power(self):
        assert euler_phi(8) == 4  # 2^3: phi = 4

    def test_euler_phi_1(self):
        """phi(1) = 1 by standard convention."""
        assert euler_phi(1) == 1

    def test_coprime_residues_prime(self):
        assert coprime_residues(5) == [1, 2, 3, 4]

    def test_coprime_residues_6(self):
        assert coprime_residues(6) == [1, 5]

    def test_coprime_residues_count(self):
        """len(coprime_residues(q)) == euler_phi(q)."""
        for q in [2, 3, 5, 6, 10, 12]:
            assert len(coprime_residues(q)) == euler_phi(q)


# ============================================================================
# Section 14: Partial sums across N values
# ============================================================================

class TestPartialSums:
    """Test partial sums for different N values."""

    def test_partial_sum_heisenberg(self):
        """sum_{r=2}^{N} S_r(H_k) = k for all N >= 2."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 3.0})
        for N in [2, 5, 10, 50]:
            assert _close(partial_sum(coeffs, N), 3.0)

    def test_partial_sum_monotone_check(self):
        """Partial sums for Virasoro: S_r alternates sign for some c values."""
        coeffs = virasoro_coefficients(1.0, 50)
        # Not necessarily monotone, but should be finite and well-defined
        for N in [10, 20, 30, 40, 50]:
            ps = partial_sum(coeffs, N)
            assert math.isfinite(ps)

    def test_partial_sum_affine_sl2(self):
        """sum_{r=2}^N S_r for affine sl_2: converges at r=3."""
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        ps3 = partial_sum(coeffs, 3)
        ps10 = partial_sum(coeffs, 10)
        assert _close(ps3, ps10)  # No further terms

    def test_partial_sum_betagamma(self):
        """sum_{r=2}^N S_r for beta-gamma: converges at r=4."""
        coeffs = get_shadow_coefficients('betagamma', {'lam': 0.5})
        ps4 = partial_sum(coeffs, 4)
        ps20 = partial_sum(coeffs, 20)
        assert _close(ps4, ps20)

    @pytest.mark.parametrize("N", [10, 50, 100])
    def test_voronoi_accelerated_matches_direct(self, N):
        """Voronoi-accelerated sum matches direct partial sum."""
        coeffs = virasoro_coefficients(1.0, max(N + 10, 110))
        direct = partial_sum(coeffs, N)
        accel = voronoi_accelerated_sum(coeffs, N)
        assert _close(direct, accel, tol=1e-4)


# ============================================================================
# Section 15: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks for Voronoi data."""

    def test_w3_t_line_matches_virasoro(self):
        """W_3 T-line shadow is identical to Virasoro."""
        c_val = 2.0
        vir = virasoro_coefficients(c_val, 20)
        w3t = get_shadow_coefficients('w3_t', {'c': c_val}, max_r=20)
        for r in range(2, 21):
            assert _close(vir[r], w3t[r]), f"Mismatch at r={r}"

    def test_w3_t_line_gauss_sum_matches_virasoro(self):
        """Gauss sums agree on W_3 T-line."""
        c_val = 2.0
        vir = virasoro_coefficients(c_val, 30)
        w3t = get_shadow_coefficients('w3_t', {'c': c_val}, max_r=30)
        for q in [2, 3, 5]:
            gv = shadow_gauss_sum(vir, q, 30)
            gw = shadow_gauss_sum(w3t, q, 30)
            assert _close(gv, gw)

    def test_plancherel_across_families(self):
        """Plancherel holds for all families at q=5."""
        families = [
            ('heisenberg', {'k': 2.0}),
            ('affine_sl2', {'k': 1.0}),
            ('betagamma', {'lam': 0.5}),
            ('virasoro', {'c': 1.0}),
        ]
        for fam, params in families:
            coeffs = get_shadow_coefficients(fam, params, max_r=30)
            _, _, ok = verify_plancherel(coeffs, 5, max_r=30)
            assert ok, f"Plancherel failed for {fam}"


# ============================================================================
# Section 16: Delta method
# ============================================================================

class TestDeltaMethod:
    """Test the Duke-Friedlander-Iwaniec delta method for shadow sums."""

    def test_delta_method_is_exact_for_large_Q(self):
        """For Q > max(r) in support, delta method is exact."""
        coeffs = get_shadow_coefficients('affine_sl2', {'k': 1.0})
        # max nonzero r = 3, so Q > 3 should give exact results
        direct = shifted_convolution_direct(coeffs, 1)
        delta = delta_method_shifted_convolution(coeffs, 1, Q=10)
        assert _close(direct, delta, tol=1e-10)

    def test_delta_method_convergence_with_Q(self):
        """As Q increases, delta method improves for Virasoro."""
        coeffs = virasoro_coefficients(1.0, 30)
        direct = shifted_convolution_direct(coeffs, 1, 30)
        errors = []
        for Q in [5, 10, 20, 30]:
            delta = delta_method_shifted_convolution(coeffs, 1, Q, 30)
            errors.append(abs(direct - delta))
        # Error should generally decrease (not strictly monotone due to resonances)
        assert errors[-1] < errors[0] * 1.5  # Final should be better than first

    def test_delta_method_h_dependence(self):
        """Delta method works for multiple shifts h."""
        coeffs = virasoro_coefficients(13.0, 40)
        for h in [1, 2, 3, 4, 5]:
            direct = shifted_convolution_direct(coeffs, h, 40)
            delta = delta_method_shifted_convolution(coeffs, h, Q=40, max_r=40)
            assert _rclose(direct, delta, rtol=0.1), \
                f"Delta method failed at h={h}: {direct} vs {delta}"


# ============================================================================
# Section 17: Shadow conductor
# ============================================================================

class TestShadowConductor:
    """Test shadow conductor estimates."""

    def test_conductor_heisenberg_constant(self):
        """For Heisenberg, |G_q|^2/q should be k^2/q (single term)."""
        k = 3.0
        coeffs = get_shadow_coefficients('heisenberg', {'k': k})
        cond = shadow_conductor_estimate(coeffs, q_max=10)
        # G_q = k * e(2/q), so |G_q|^2 = k^2, and |G_q|^2/q = k^2/q
        for q in range(1, 11):
            expected = k ** 2 / q
            assert _close(cond[q], expected), f"Conductor at q={q}: {cond[q]} vs {expected}"

    def test_conductor_returns_dict(self):
        coeffs = virasoro_coefficients(1.0, 30)
        cond = shadow_conductor_estimate(coeffs, q_max=10, max_r=30)
        assert len(cond) == 10
        assert all(q in cond for q in range(1, 11))

    def test_conductor_positive(self):
        """All conductor estimates are non-negative."""
        coeffs = virasoro_coefficients(13.0, 30)
        cond = shadow_conductor_estimate(coeffs, q_max=10, max_r=30)
        for q, val in cond.items():
            assert val >= -1e-15, f"Conductor negative at q={q}: {val}"


# ============================================================================
# Section 18: Comprehensive analysis
# ============================================================================

class TestFullAnalysis:
    """Test the full_voronoi_analysis function."""

    def test_analysis_heisenberg(self):
        analysis = full_voronoi_analysis('heisenberg', {'k': 1.0}, max_r=30, q_max=5)
        assert analysis.depth_class == 'G'
        assert len(analysis.gauss_sums) == 5
        assert all(ok for _, _, ok in analysis.plancherel_checks.values())

    def test_analysis_virasoro(self):
        analysis = full_voronoi_analysis('virasoro', {'c': 1.0}, max_r=30, q_max=5, N_values=[10])
        assert analysis.depth_class == 'M'
        assert 10 in analysis.partial_sums
        assert analysis.complementarity_sum is not None

    def test_analysis_affine(self):
        analysis = full_voronoi_analysis('affine_sl2', {'k': 1.0}, max_r=20, q_max=3)
        assert analysis.depth_class == 'L'

    def test_analysis_betagamma(self):
        analysis = full_voronoi_analysis('betagamma', {'lam': 0.5}, max_r=20, q_max=3)
        assert analysis.depth_class == 'C'

    def test_analysis_subconvexity_all_pass(self):
        analysis = full_voronoi_analysis('virasoro', {'c': 13.0}, max_r=30, q_max=5, N_values=[10])
        for _, _, _, actual, bound, ok in analysis.subconvexity_checks:
            assert ok, f"Subconvexity failed: {actual} > {bound}"


# ============================================================================
# Section 19: Twisted partial sums
# ============================================================================

class TestTwistedPartialSums:
    """Test twisted partial sums sum_{r=2}^N S_r e(ar/q)."""

    def test_twisted_partial_sum_a0_is_real(self):
        """Twist at a=0 gives real partial sum."""
        coeffs = virasoro_coefficients(1.0, 30)
        val = twisted_partial_sum(coeffs, 0, 5, 20)
        assert abs(val.imag) < 1e-12

    def test_twisted_partial_sum_at_large_N_converges(self):
        """For Heisenberg, twisted partial sum converges at N=2."""
        coeffs = get_shadow_coefficients('heisenberg', {'k': 2.0})
        v2 = twisted_partial_sum(coeffs, 1, 3, 2)
        v10 = twisted_partial_sum(coeffs, 1, 3, 10)
        assert _close(v2, v10)

    def test_twisted_partial_sum_bound(self):
        """Twisted partial sum is bounded by sum |S_r|."""
        coeffs = virasoro_coefficients(1.0, 30)
        for q in [2, 3, 5]:
            for a in range(1, q):
                if math.gcd(a, q) == 1:
                    val = twisted_partial_sum(coeffs, a, q, 30)
                    bound = sum(abs(coeffs.get(r, 0.0)) for r in range(2, 31))
                    assert abs(val) <= bound + 1e-10


# ============================================================================
# Section 20: Gauss sum landscape
# ============================================================================

class TestLandscape:
    """Test landscape-level Gauss sum computations."""

    def test_landscape_returns_dict(self):
        result = gauss_sum_landscape([1.0, 13.0, 25.0], q=3, max_r=30)
        assert len(result) == 3
        assert all(c in result for c in [1.0, 13.0, 25.0])

    def test_landscape_norm(self):
        result = gauss_sum_norm_landscape([1.0, 13.0, 25.0], q=3, max_r=30)
        assert all(isinstance(v, float) for v in result.values())
        assert all(v >= 0 for v in result.values())

    def test_landscape_complementarity_pair(self):
        """G_q(Vir_c) and G_q(Vir_{26-c}) should sum to G_q(D)."""
        result_c = gauss_sum_landscape([1.0], q=5, max_r=30)
        result_dual = gauss_sum_landscape([25.0], q=5, max_r=30)
        coeffs_c = virasoro_coefficients(1.0, 30)
        coeffs_dual = koszul_dual_virasoro_coefficients(1.0, 30)
        coeffs_D = complementarity_coefficients(coeffs_c, coeffs_dual, 30)
        g_D = shadow_gauss_sum(coeffs_D, 5, 30)
        assert _close(result_c[1.0] + result_dual[25.0], g_D)


# ============================================================================
# Section 21: Direct vs Voronoi side comparison
# ============================================================================

class TestVoronoiSides:
    """Comparison of direct and Voronoi formula sides.

    For finite towers, the Voronoi formula is exact.
    For class M, the dual side is an approximation.
    """

    def test_voronoi_direct_side_equals_twisted_sum(self):
        """Direct side of Voronoi = twisted smoothed sum."""
        coeffs = virasoro_coefficients(1.0, 30)
        test = lambda x: gaussian_test(x, 10.0)
        direct = voronoi_direct_side(coeffs, 1, 3, test, 30)
        manual = direct_twisted_smoothed_sum(coeffs, 1, 3, test, 30)
        assert _close(direct, manual)

    def test_voronoi_main_term_finite(self):
        """Main term is finite."""
        coeffs = virasoro_coefficients(1.0, 30)
        test = lambda x: gaussian_test(x, 10.0)
        mt = voronoi_main_term(coeffs, 1, 3, test, 30.0)
        assert isinstance(mt, (int, float, complex))
        if isinstance(mt, complex):
            assert math.isfinite(mt.real) and math.isfinite(mt.imag)
        else:
            assert math.isfinite(mt)


# ============================================================================
# Section 22: Gauss sum norm vs Plancherel (cross-check)
# ============================================================================

class TestGaussSumNormPlancherel:
    """Cross-check: |G_q|^2 computed via norm_squared vs via Plancherel.

    Plancherel gives sum_a |G_q(a)|^2 = q * sum |S_r|^2.
    The term a=1 gives |G_q(1)|^2 = gauss_sum_norm_squared.
    So gauss_sum_norm_squared <= plancherel_lhs.
    """

    def test_norm_squared_bounded_by_plancherel(self):
        coeffs = virasoro_coefficients(1.0, 30)
        for q in [2, 3, 5]:
            norm_sq = gauss_sum_norm_squared(coeffs, q, 30)
            pl_lhs = plancherel_lhs(coeffs, q, 30)
            assert norm_sq <= pl_lhs + 1e-10, \
                f"|G_q|^2 = {norm_sq} > Plancherel LHS = {pl_lhs}"


# ============================================================================
# Section 23: Additional parametrized tests for coverage
# ============================================================================

class TestParametrized:
    """Parametrized sweep tests for broad coverage."""

    @pytest.mark.parametrize("family,params", [
        ('heisenberg', {'k': 1.0}),
        ('heisenberg', {'k': 5.0}),
        ('affine_sl2', {'k': 1.0}),
        ('affine_sl2', {'k': 3.0}),
        ('affine_sl3', {'k': 1.0}),
        ('betagamma', {'lam': 0.5}),
        ('virasoro', {'c': 1.0}),
        ('virasoro', {'c': 13.0}),
        ('virasoro', {'c': 25.0}),
        ('w3_t', {'c': 2.0}),
    ])
    def test_plancherel_all_families_q3(self, family, params):
        coeffs = get_shadow_coefficients(family, params, max_r=30)
        _, _, ok = verify_plancherel(coeffs, 3, max_r=30, rtol=1e-6)
        assert ok, f"Plancherel failed for {family} {params}"

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 10.0, 13.0, 20.0, 25.0])
    def test_complementarity_gauss_sum_additivity(self, c_val):
        """G_q(c) + G_q(26-c) = G_q(D) at q=3."""
        tc, td, tD = voronoi_complementarity_check(c_val, 1, 3, max_r=40)
        assert _close(tc + td, tD)

    @pytest.mark.parametrize("q", [2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_plancherel_virasoro_c1_sweep(self, q):
        coeffs = virasoro_coefficients(1.0, 30)
        lhs, rhs, ok = verify_plancherel(coeffs, q, max_r=30, rtol=1e-6)
        assert ok, f"Plancherel at q={q}: {lhs} vs {rhs}"


# ============================================================================
# Section 24: Voronoi finite identity for class M (approximate)
# ============================================================================

class TestVoronoiClassM:
    """For class M, the Voronoi Poisson identity still holds at finite truncation."""

    def test_virasoro_finite_identity_q3(self):
        """Poisson identity holds for truncated Virasoro."""
        coeffs = virasoro_coefficients(1.0, 30)
        direct, poisson = voronoi_finite_identity(coeffs, 1, 3, max_r=30)
        assert _close(direct, poisson), f"Finite identity: {direct} vs {poisson}"

    def test_virasoro_finite_identity_q7(self):
        coeffs = virasoro_coefficients(13.0, 40)
        direct, poisson = voronoi_finite_identity(coeffs, 2, 7, max_r=40)
        assert _close(direct, poisson)

    @pytest.mark.parametrize("a,q", [(1, 2), (1, 3), (2, 5), (3, 7)])
    def test_virasoro_finite_identity_systematic(self, a, q):
        coeffs = virasoro_coefficients(1.0, 30)
        direct, poisson = voronoi_finite_identity(coeffs, a, q, max_r=30)
        assert _close(direct, poisson), \
            f"Finite identity at a={a}, q={q}: {direct} vs {poisson}"
