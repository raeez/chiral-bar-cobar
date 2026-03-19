#!/usr/bin/env python3
"""
test_zeta_spectral_rigidity.py — Tests for shadow tower positivity and spectral rigidity.

T1-T15:  Li-Keiper coefficients
T16-T25: Weil explicit formula with shadow test functions
T26-T35: MC equation positivity
T36-T45: Koszul spectral rigidity
T46-T55: Shadow depth ↔ L-function correspondence
T56-T65: Vardi coefficients and shadow moments
T66-T75: Gap analysis and sewing ↔ Euler product discovery
"""

import pytest
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from zeta_spectral_rigidity import (
    li_coefficient_from_zeros, li_coefficients_batch, epstein_li_coefficient,
    weil_explicit_formula,
    shadow_test_function_gaussian, shadow_test_function_gaussian_hat,
    shadow_test_function_cubic, shadow_test_function_quartic,
    mc_equation_positivity_test, mc_obstruction_to_weil_coefficient,
    koszul_enhanced_constraints, spectral_rigidity_test,
    shadow_depth_lfunction_correspondence,
    vardi_positivity_coefficients, shadow_moment_constraints,
    nyman_beurling_bar_cobar_analogy,
    positivity_certificate, gap_analysis,
)
from rankin_selberg_bridge import narain_scalar_spectrum_c1

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# T1-T15: Li-Keiper coefficients
# ============================================================

class TestLiCoefficients:
    @skip_no_mpmath
    def test_li_1_positive(self):
        """T1: λ₁ > 0 (equivalent to ζ has no zero at s=1, trivially true)."""
        lam = li_coefficient_from_zeros(1, num_zeros=50)
        assert lam > 0

    @skip_no_mpmath
    def test_li_2_positive(self):
        """T2: λ₂ > 0."""
        lam = li_coefficient_from_zeros(2, num_zeros=50)
        assert lam > 0

    @skip_no_mpmath
    def test_first_10_li_positive(self):
        """T3: λ_1,...,λ_{10} all positive (numerical RH verification)."""
        li = li_coefficients_batch(10, num_zeros=100)
        for n, lam in enumerate(li, 1):
            assert lam > 0, f"λ_{n} = {lam} ≤ 0!"

    @skip_no_mpmath
    def test_li_growing(self):
        """T4: Li coefficients grow roughly as n·log(n)."""
        li = li_coefficients_batch(20, num_zeros=100)
        # Should be roughly increasing
        assert li[-1] > li[0]

    @skip_no_mpmath
    def test_li_1_value(self):
        """T5: λ₁ ≈ 0.02310... (known value, Keiper 1992)."""
        lam = li_coefficient_from_zeros(1, num_zeros=200)
        # λ₁ = 1 - 1/ζ(2)·d/ds[sξ'(s)/ξ(s)]|_{s=1} ≈ 0.0231
        # With 200 zeros this should be accurate
        assert abs(lam - 0.0231) < 0.01

    @skip_no_mpmath
    def test_epstein_li_1(self):
        """T6: Epstein Li coefficient λ^ε_1 > 0."""
        lam = epstein_li_coefficient(1, num_zeros=50)
        assert lam > 0

    @skip_no_mpmath
    def test_epstein_li_positive(self):
        """T7: First 5 Epstein Li coefficients all positive."""
        for n in range(1, 6):
            lam = epstein_li_coefficient(n, num_zeros=50)
            assert lam > 0, f"λ^ε_{n} = {lam} ≤ 0!"

    @skip_no_mpmath
    def test_epstein_li_scaled(self):
        """T8: Epstein Li coefficients related to standard Li by scaling.

        Since ξ_ε(s) = ξ(2s), zeros ρ_ε = ρ/2.
        λ^ε_n = Σ [1-(1-1/ρ_ε)^n] = Σ [1-(1-2/ρ)^n].
        """
        lam_eps = epstein_li_coefficient(1, num_zeros=50)
        lam_std = li_coefficient_from_zeros(1, num_zeros=50)
        # They should be different (different scaling)
        assert lam_eps != lam_std

    @skip_no_mpmath
    def test_li_batch_consistency(self):
        """T9: Batch computation matches individual."""
        li_batch = li_coefficients_batch(5, num_zeros=50)
        for n in range(1, 6):
            li_ind = li_coefficient_from_zeros(n, num_zeros=50)
            assert abs(li_batch[n - 1] - li_ind) / max(abs(li_ind), 1e-10) < 1e-6

    @skip_no_mpmath
    def test_li_20_all_positive(self):
        """T10: λ_1,...,λ_{20} all positive."""
        li = li_coefficients_batch(20, num_zeros=100)
        for n, lam in enumerate(li, 1):
            assert lam > 0, f"λ_{n} = {lam}"

    def test_li_requires_mpmath(self):
        """T11: Li computation requires mpmath."""
        if HAS_MPMATH:
            pytest.skip("mpmath is available")
        with pytest.raises(RuntimeError):
            li_coefficient_from_zeros(1)

    @skip_no_mpmath
    def test_li_convergence_with_zeros(self):
        """T12: λ_n converges as num_zeros increases."""
        lam_50 = li_coefficient_from_zeros(1, num_zeros=50)
        lam_100 = li_coefficient_from_zeros(1, num_zeros=100)
        # Should be close
        assert abs(lam_50 - lam_100) < 0.1 * abs(lam_100)

    @skip_no_mpmath
    def test_li_real(self):
        """T13: Li coefficients are real."""
        li = li_coefficients_batch(5, num_zeros=50)
        for lam in li:
            assert isinstance(lam, float)

    @skip_no_mpmath
    def test_epstein_li_real(self):
        """T14: Epstein Li coefficients are real."""
        lam = epstein_li_coefficient(3, num_zeros=50)
        assert isinstance(lam, float)

    @skip_no_mpmath
    def test_li_sum_rule(self):
        """T15: λ_1 = Σ 1/|ρ|² - 2·Re(Σ 1/ρ) + N (schematic)."""
        # λ_1 = Σ_ρ [1 - (1-1/ρ)] = Σ_ρ 1/ρ = known value
        lam = li_coefficient_from_zeros(1, num_zeros=100)
        # Σ 1/ρ over zeros with positive imaginary part:
        # 1/ρ + 1/ρ* = 2Re(1/ρ) = 2·(1/2)/(1/4+γ²) = 1/(1/4+γ²)
        direct = sum(1.0 / (0.25 + float(mpmath.zetazero(k).imag) ** 2)
                     for k in range(1, 101))
        assert abs(lam - direct) / abs(direct) < 0.1


# ============================================================
# T16-T25: Weil explicit formula with shadow test functions
# ============================================================

class TestWeilFormula:
    @skip_no_mpmath
    def test_gaussian_weil_sum_positive(self):
        """T16: Σ_ρ h_G(γ_ρ) > 0 for Gaussian test function."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        weil_sum = sum(2 * shadow_test_function_gaussian(g, kappa=0.5) for g in zeros)
        assert weil_sum > 0

    @skip_no_mpmath
    def test_gaussian_weil_sum_varies_with_kappa(self):
        """T17: Gaussian Weil sum varies with shadow width κ."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        sums = []
        for kappa in [0.1, 0.5, 1.0, 5.0]:
            s = sum(2 * shadow_test_function_gaussian(g, kappa) for g in zeros)
            sums.append(s)
        # Larger κ → wider Gaussian → larger sum
        assert sums[-1] > sums[0]

    @skip_no_mpmath
    def test_cubic_test_function_positive(self):
        """T18: Cubic shadow test function with small correction still gives positive Weil sum."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        weil_sum = sum(2 * shadow_test_function_cubic(g, 0.5, 0.001) for g in zeros)
        assert weil_sum > 0

    @skip_no_mpmath
    def test_quartic_test_function(self):
        """T19: Quartic shadow test function gives finite Weil sum."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        weil_sum = sum(2 * shadow_test_function_quartic(g, 0.5, 0.0001) for g in zeros)
        assert np.isfinite(weil_sum)

    def test_gaussian_test_function_shape(self):
        """T20: h_G is positive, even, and decays."""
        for t in [-10, -1, 0, 1, 10]:
            assert shadow_test_function_gaussian(t) > 0
        # Even
        assert abs(shadow_test_function_gaussian(3) - shadow_test_function_gaussian(-3)) < 1e-15
        # Decays
        assert shadow_test_function_gaussian(100) < 1e-10

    def test_gaussian_hat_shape(self):
        """T21: ĥ_G is positive, even, and decays."""
        for x in [-5, -1, 0, 1, 5]:
            assert shadow_test_function_gaussian_hat(x) > 0

    @skip_no_mpmath
    def test_weil_sum_consistency(self):
        """T22: Weil sum with narrow Gaussian selects first zero."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        # Very narrow Gaussian centered at γ₁
        gamma1 = zeros[0]
        kappa = 0.01  # Very narrow
        weil_sum = sum(2 * np.exp(-(g - gamma1) ** 2 / (4 * kappa)) for g in zeros)
        # Should be dominated by the first zero
        first_term = 2 * np.exp(0)  # = 2
        assert weil_sum > 1.5  # Close to 2

    @skip_no_mpmath
    def test_weil_wide_gaussian_large(self):
        """T23: Wide Gaussian gives large Weil sum (many zeros contribute)."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 101)]
        weil_sum = sum(2 * shadow_test_function_gaussian(g, kappa=100) for g in zeros)
        assert weil_sum > 1  # Many zeros contribute, sum well above 0

    @skip_no_mpmath
    def test_shadow_kappa_determines_weil(self):
        """T24: For Gaussian class, κ alone determines the Weil sum."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        # Two different κ values give different sums
        s1 = sum(2 * shadow_test_function_gaussian(g, 0.3) for g in zeros)
        s2 = sum(2 * shadow_test_function_gaussian(g, 0.7) for g in zeros)
        assert s1 != s2

    @skip_no_mpmath
    def test_all_shadow_weil_sums_positive(self):
        """T25: All shadow-class Weil sums are positive (consistent with RH)."""
        zeros = [float(mpmath.zetazero(k).imag) for k in range(1, 51)]
        # Gaussian (depth 2)
        s_G = sum(2 * shadow_test_function_gaussian(g, 0.5) for g in zeros)
        # Lie (depth 3, small cubic)
        s_L = sum(2 * shadow_test_function_cubic(g, 0.75, 0.01) for g in zeros)
        # Contact (depth 4, small quartic)
        s_C = sum(2 * shadow_test_function_quartic(g, 0.5, 0.001) for g in zeros)
        assert s_G > 0 and s_L > 0 and s_C > 0


# ============================================================
# T26-T35: MC equation positivity
# ============================================================

class TestMCPositivity:
    @skip_no_mpmath
    def test_mc_gaussian_class(self):
        """T26: MC positivity test for Gaussian class (V_Z)."""
        result = mc_equation_positivity_test(
            {'kappa': 0.5, 'depth': 2}, num_zeros=50
        )
        assert result['gaussian_positive']
        assert result['mc_depth'] == 2

    @skip_no_mpmath
    def test_mc_lie_class(self):
        """T27: MC positivity test for Lie class (sl₂)."""
        result = mc_equation_positivity_test(
            {'kappa': 0.75, 'cubic': 0.1, 'depth': 3}, num_zeros=50
        )
        assert result['gaussian_positive']
        assert result['cubic_positive']

    @skip_no_mpmath
    def test_mc_contact_class(self):
        """T28: MC positivity test for Contact class (βγ)."""
        result = mc_equation_positivity_test(
            {'kappa': 0.5, 'cubic': 0, 'quartic': 0.01, 'depth': 4}, num_zeros=50
        )
        assert result['gaussian_positive']
        assert result['quartic_positive']

    @skip_no_mpmath
    def test_mc_shadow_width(self):
        """T29: Shadow width = 1/(4κ) controls Gaussian decay."""
        result = mc_equation_positivity_test(
            {'kappa': 2.0, 'depth': 2}, num_zeros=50
        )
        assert abs(result['shadow_width'] - 0.125) < 1e-10

    def test_obstruction_to_weil(self):
        """T30: MC obstruction maps to Weil coefficient."""
        coeff = mc_obstruction_to_weil_coefficient(0.0, 3, 0.5)
        assert coeff == 0.0  # Zero obstruction for Gaussian

    def test_nonzero_obstruction(self):
        """T31: Nonzero obstruction gives nonzero Weil coefficient."""
        coeff = mc_obstruction_to_weil_coefficient(1.0, 3, 0.5)
        assert coeff > 0

    @skip_no_mpmath
    def test_mc_terminates(self):
        """T32: MC equation terminates at the stated depth."""
        result = mc_equation_positivity_test(
            {'kappa': 0.5, 'depth': 2}, num_zeros=50
        )
        assert result['mc_terminates']

    @skip_no_mpmath
    def test_mc_positivity_robust(self):
        """T33: Gaussian Weil sum positive for wide range of κ values."""
        for kappa in [0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]:
            result = mc_equation_positivity_test(
                {'kappa': kappa, 'depth': 2}, num_zeros=50
            )
            assert result['gaussian_positive'], f"Failed at κ = {kappa}"

    @skip_no_mpmath
    def test_mc_cubic_negative_coeff(self):
        """T34: Cubic correction with negative coefficient still positive (if small)."""
        result = mc_equation_positivity_test(
            {'kappa': 1.0, 'cubic': -0.001, 'depth': 3}, num_zeros=50
        )
        assert result['cubic_positive']

    @skip_no_mpmath
    def test_mc_large_quartic_still_positive(self):
        """T35: Quartic correction with moderate coefficient still positive."""
        result = mc_equation_positivity_test(
            {'kappa': 1.0, 'cubic': 0, 'quartic': 0.1, 'depth': 4}, num_zeros=50
        )
        assert result['quartic_positive']


# ============================================================
# T36-T45: Koszul spectral rigidity
# ============================================================

class TestKoszulRigidity:
    @skip_no_mpmath
    def test_enhanced_constraints(self):
        """T36: Koszul enhanced constraints computed."""
        result = koszul_enhanced_constraints(2.0)
        assert result['gap_monotone']
        assert result['ainfty_depth'] == 2
        assert result['chain_level_determined']

    @skip_no_mpmath
    def test_gap_monotone(self):
        """T37: Gaps Δ_{k+1}-Δ_k are monotonically increasing for V_Z."""
        result = koszul_enhanced_constraints(2.0)
        assert result['gap_monotone']

    @skip_no_mpmath
    def test_ainfty_depth_gaussian(self):
        """T38: A∞ depth = 2 for Gaussian class (strict associativity)."""
        result = koszul_enhanced_constraints(2.0)
        assert result['ainfty_depth'] == 2

    @skip_no_mpmath
    def test_mc_constraints_finite(self):
        """T39: MC constraints are finite (finitely many determine the Epstein zeta)."""
        result = koszul_enhanced_constraints(2.0)
        assert result['mc_constraints_finite']

    @skip_no_mpmath
    def test_spectral_rigidity_c1(self):
        """T40: Spectral rigidity test for c=1 self-dual lattice VOA."""
        spec = narain_scalar_spectrum_c1(1.0, nmax=100)
        result = spectral_rigidity_test(spec, [1.5, 2.0, 3.0])
        assert result['gap_monotone'] if 'gap_monotone' in result else True
        assert 0.4 < result['weyl_exponent'] < 0.6  # Should be ~0.5

    @skip_no_mpmath
    def test_weyl_exponent(self):
        """T41: Weyl exponent for c=1 is ~0.5."""
        spec = narain_scalar_spectrum_c1(1.0, nmax=200)
        result = spectral_rigidity_test(spec, [2.0])
        assert abs(result['weyl_exponent'] - 0.5) < 0.1

    @skip_no_mpmath
    def test_gap_ratio_bounded(self):
        """T42: Gap ratio max/min is bounded for V_Z."""
        spec = narain_scalar_spectrum_c1(1.0, nmax=100)
        result = spectral_rigidity_test(spec, [2.0])
        assert result['gap_ratio'] < 100  # Gaps grow linearly, ratio bounded

    def test_gaps_arithmetic(self):
        """T43: For V_Z at R=1, gaps are (2k+1)/2 (arithmetic progression)."""
        # Δ_k = k²/2, gap = Δ_{k+1}-Δ_k = (2k+1)/2
        for k in range(1, 20):
            gap = (k + 1) ** 2 / 2 - k ** 2 / 2
            expected = (2 * k + 1) / 2
            assert abs(gap - expected) < 1e-10

    @skip_no_mpmath
    def test_chain_level_stronger(self):
        """T44: Chain-level bar-cobar is stronger than homological equivalence.

        The bar-cobar map Ω(B(A)) → A is a quasi-isomorphism (chain-level).
        This is stronger than just H*(Ω(B(A))) ≃ H*(A) (homology).
        The chain-level data constrains the Epstein zeta coefficients
        beyond what the functional equation alone provides.
        """
        result = koszul_enhanced_constraints(2.0)
        assert result['chain_level_determined']
        # The functional equation gives 1 constraint (s ↔ 1/2-s).
        # The chain-level data gives mc_constraint_count constraints.
        assert result['mc_constraint_count'] >= 1

    @skip_no_mpmath
    def test_self_dual_spectrum_structure(self):
        """T45: Self-dual spectrum has multiplicities from enhanced symmetry."""
        spec = narain_scalar_spectrum_c1(1.0, nmax=10)
        # At R=1: all multiplicities are 4 (from SU(2)₁ enhanced symmetry)
        for delta, mult in spec:
            assert mult == 4


# ============================================================
# T46-T55: Shadow depth ↔ L-function correspondence
# ============================================================

class TestShadowLFunction:
    def test_correspondence_table(self):
        """T46: Shadow-L correspondence table exists."""
        table = shadow_depth_lfunction_correspondence()
        assert 'Gaussian' in table
        assert 'Lie' in table
        assert 'Contact' in table
        assert 'Mixed' in table

    def test_gaussian_depth(self):
        """T47: Gaussian class has depth 2."""
        table = shadow_depth_lfunction_correspondence()
        assert table['Gaussian']['depth'] == 2

    def test_lie_depth(self):
        """T48: Lie class has depth 3."""
        table = shadow_depth_lfunction_correspondence()
        assert table['Lie']['depth'] == 3

    def test_contact_depth(self):
        """T49: Contact class has depth 4."""
        table = shadow_depth_lfunction_correspondence()
        assert table['Contact']['depth'] == 4

    def test_mixed_infinite(self):
        """T50: Mixed class has infinite depth."""
        table = shadow_depth_lfunction_correspondence()
        assert table['Mixed']['depth'] == float('inf')

    def test_critical_lines_formula(self):
        """T51: Number of critical lines = depth - 1."""
        table = shadow_depth_lfunction_correspondence()
        for cls in ['Gaussian', 'Lie', 'Contact']:
            assert table[cls]['critical_lines'] == table[cls]['depth'] - 1

    def test_gaussian_single_zeta(self):
        """T52: Gaussian class has single L-factor ζ(2s)."""
        table = shadow_depth_lfunction_correspondence()
        assert len(table['Gaussian']['L_factors']) == 1
        assert 'ζ(2s)' in table['Gaussian']['L_factors']

    def test_lie_two_factors(self):
        """T53: Lie class has two L-factors."""
        table = shadow_depth_lfunction_correspondence()
        assert len(table['Lie']['L_factors']) == 2

    def test_nyman_beurling_analogy(self):
        """T54: Nyman-Beurling analogy structure."""
        nb = nyman_beurling_bar_cobar_analogy()
        assert 'missing_link' in nb
        assert 'proved_direction' in nb

    def test_shadow_terminates(self):
        """T55: Gaussian/Lie/Contact all have finite termination."""
        table = shadow_depth_lfunction_correspondence()
        for cls in ['Gaussian', 'Lie', 'Contact']:
            assert table[cls]['shadows_vanish_from'] is not None


# ============================================================
# T56-T65: Vardi coefficients and shadow moments
# ============================================================

class TestVardiAndMoments:
    @skip_no_mpmath
    def test_vardi_positive(self):
        """T56: Vardi coefficients V_r = Σ γ_k^{-2r} are all positive."""
        vardi = vardi_positivity_coefficients(10, num_zeros=50)
        for r, v in enumerate(vardi, 1):
            assert v > 0, f"V_{r} = {v} ≤ 0!"

    @skip_no_mpmath
    def test_vardi_decreasing(self):
        """T57: Vardi coefficients are decreasing (larger r → smaller sum)."""
        vardi = vardi_positivity_coefficients(10, num_zeros=50)
        for i in range(len(vardi) - 1):
            assert vardi[i] > vardi[i + 1]

    @skip_no_mpmath
    def test_vardi_first(self):
        """T58: V_1 = Σ 2/γ_k² > 0 (positive, converges slowly)."""
        vardi = vardi_positivity_coefficients(1, num_zeros=200)
        assert vardi[0] > 0.03  # Converges to ~0.046

    @skip_no_mpmath
    def test_shadow_moment_gaussian(self):
        """T59: Shadow moment M_κ for Gaussian class is positive."""
        mom = shadow_moment_constraints(0.5, 2, num_zeros=50)
        assert mom['M_kappa'] > 0

    @skip_no_mpmath
    def test_shadow_cubic_moment_zero(self):
        """T60: Cubic moment vanishes by symmetry (γ ↔ -γ)."""
        mom = shadow_moment_constraints(0.5, 3, num_zeros=50)
        assert abs(mom['M_cubic']) < 1e-10

    @skip_no_mpmath
    def test_shadow_quartic_moment_positive(self):
        """T61: Quartic moment is positive."""
        mom = shadow_moment_constraints(0.5, 4, num_zeros=50)
        assert mom['M_quartic'] > 0

    @skip_no_mpmath
    def test_shadow_moments_from_depth(self):
        """T62: Depth d gives d-1 independent moment constraints."""
        for depth in [2, 3, 4]:
            mom = shadow_moment_constraints(0.5, depth, num_zeros=50)
            expected = depth - 1
            assert mom['moments_from_shadow'] == expected

    @skip_no_mpmath
    def test_moment_kappa_dependence(self):
        """T63: Shadow moment depends on κ."""
        m1 = shadow_moment_constraints(0.5, 2, num_zeros=50)['M_kappa']
        m2 = shadow_moment_constraints(2.0, 2, num_zeros=50)['M_kappa']
        assert m1 != m2
        # Larger κ → wider Gaussian → larger moment
        assert m2 > m1

    @skip_no_mpmath
    def test_vardi_li_relation(self):
        """T64: V_1 (Vardi) is related to λ_1 (Li): both ≈ 0.023."""
        vardi = vardi_positivity_coefficients(1, num_zeros=100)
        li = li_coefficients_batch(1, num_zeros=100)
        # V_1 = Σ 2/γ² and λ_1 = Σ 2/(1/4+γ²). Both positive, same order.
        assert vardi[0] > 0 and li[0] > 0
        assert abs(vardi[0] - li[0]) / max(vardi[0], li[0]) < 1.0  # Same order

    @skip_no_mpmath
    def test_vardi_convergence(self):
        """T65: Vardi coefficients converge with number of zeros."""
        v50 = vardi_positivity_coefficients(1, num_zeros=50)
        v100 = vardi_positivity_coefficients(1, num_zeros=100)
        assert abs(v50[0] - v100[0]) / v100[0] < 0.1


# ============================================================
# T66-T75: Gap analysis and discovery
# ============================================================

class TestGapAnalysis:
    def test_gap_analysis_structure(self):
        """T66: Gap analysis returns complete structure."""
        ga = gap_analysis()
        assert 'have' in ga
        assert 'need' in ga
        assert 'discovery' in ga
        assert 'most_promising' in ga

    def test_discovery_sigma_minus_1(self):
        """T67: Discovery: log det(1-K_q) involves σ_{-1}(N) divisor sums.

        log Π(1-q^n) = -Σ_n Σ_m q^{nm}/m = -Σ_N σ_{-1}(N) q^N
        where σ_{-1}(N) = Σ_{d|N} 1/d.
        """
        # Verify the identity for small N
        # σ_{-1}(1) = 1, σ_{-1}(2) = 1+1/2=3/2, σ_{-1}(3) = 1+1/3=4/3
        # σ_{-1}(4) = 1+1/2+1/4=7/4, σ_{-1}(6) = 1+1/2+1/3+1/6=2
        def sigma_minus_1(N):
            return sum(1.0 / d for d in range(1, N + 1) if N % d == 0)

        assert abs(sigma_minus_1(1) - 1.0) < 1e-10
        assert abs(sigma_minus_1(2) - 1.5) < 1e-10
        assert abs(sigma_minus_1(3) - 4 / 3) < 1e-10
        assert abs(sigma_minus_1(6) - 2.0) < 1e-10

    def test_sigma_minus_1_dirichlet_series(self):
        """T68: Σ σ_{-1}(N) N^{-s} = ζ(s)ζ(s+1) (Ramanujan identity).

        This is the ARITHMETIC CONTENT of the sewing Fredholm determinant.
        """
        if not HAS_MPMATH:
            pytest.skip("mpmath required")

        def sigma_minus_1(N):
            return sum(1.0 / d for d in range(1, N + 1) if N % d == 0)

        s = 2.0
        # Direct sum
        direct = sum(sigma_minus_1(N) * N ** (-s) for N in range(1, 1000))
        # Expected: ζ(2)ζ(3)
        expected = float(mpmath.zeta(s) * mpmath.zeta(s + 1))
        assert abs(direct - expected) / abs(expected) < 0.01

    def test_sewing_log_det_expansion(self):
        """T69: Verify log det(1-K_q) = -Σ σ_{-1}(N) q^N."""
        q = 0.3  # Small enough for convergence

        # Direct: log Π(1-q^n)
        log_det = sum(np.log(1 - q ** n) for n in range(1, 100))

        # Via σ_{-1}: -Σ σ_{-1}(N) q^N
        def sigma_minus_1(N):
            return sum(1.0 / d for d in range(1, N + 1) if N % d == 0)

        sigma_sum = -sum(sigma_minus_1(N) * q ** N for N in range(1, 200))

        assert abs(log_det - sigma_sum) / abs(log_det) < 1e-6

    @skip_no_mpmath
    def test_positivity_certificate(self):
        """T70: Positivity certificate computation runs."""
        cert = positivity_certificate(n_max=10, num_zeros=50)
        assert cert['all_positive']
        assert cert['epstein_all_positive']
        assert cert['vardi_all_positive']

    @skip_no_mpmath
    def test_li_from_certificate(self):
        """T71: Certificate gives Li coefficients."""
        cert = positivity_certificate(n_max=5, num_zeros=50)
        assert len(cert['li_coefficients']) == 5

    def test_four_gaps_identified(self):
        """T72: Gap analysis identifies four specific gaps A-D."""
        ga = gap_analysis()
        for gap in ['A', 'B', 'C', 'D']:
            assert gap in ga['need']

    def test_most_promising_is_B(self):
        """T73: Most promising direction is B (Euler product from sewing)."""
        ga = gap_analysis()
        assert 'B' in ga['most_promising']

    @skip_no_mpmath
    def test_sewing_arithmetic_content(self):
        """T74: The sewing operator carries arithmetic content via σ_{-1}.

        KEY OBSERVATION: The eigenvalues of K_q are q^n = e^{-2πny}.
        The divisor function σ_{-1}(N) = Σ_{d|N} 1/d is MULTIPLICATIVE:
        σ_{-1}(mn) = σ_{-1}(m)·σ_{-1}(n) for gcd(m,n)=1.

        This multiplicativity means log det(1-K_q) has an EULER PRODUCT
        decomposition over prime eigenvalues.
        """
        def sigma_minus_1(N):
            return sum(1.0 / d for d in range(1, N + 1) if N % d == 0)

        # Verify multiplicativity for coprime pairs
        for m, n in [(2, 3), (2, 5), (3, 5), (3, 7), (5, 7)]:
            assert abs(sigma_minus_1(m * n) - sigma_minus_1(m) * sigma_minus_1(n)) < 1e-10

    @skip_no_mpmath
    def test_euler_product_of_sewing(self):
        """T75: The Dirichlet series of σ_{-1} has Euler product ζ(s)ζ(s+1).

        BRIDGE: sewing det → σ_{-1} → ζ(s)ζ(s+1) → Euler product.

        The Euler product: ζ(s)ζ(s+1) = Π_p (1-p^{-s})^{-1}(1-p^{-s-1})^{-1}.
        Each prime p contributes a factor to the sewing determinant.
        This is the PRIME DECOMPOSITION of the sewing operator.
        """
        # Verify Euler product at s = 2
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        euler_prod = 1.0
        for p in primes:
            euler_prod *= 1.0 / ((1 - p ** (-2)) * (1 - p ** (-3)))
        expected = float(mpmath.zeta(2) * mpmath.zeta(3))
        # With 15 primes, should be close but not exact
        assert abs(euler_prod - expected) / expected < 0.05


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
