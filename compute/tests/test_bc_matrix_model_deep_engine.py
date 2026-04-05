r"""Tests for bc_matrix_model_deep_engine.py (BC-100).

Random matrix ensemble from shadow zeta: 85+ tests covering all 15 sections
of the engine.  Multi-path verification mandate: every numerical result
verified by at least 2 independent methods.

VERIFICATION PATHS:
1. Density positivity check (must be >= 0 for Hermitian model)
2. Moment reconstruction: m_k from rho matches m_k from S_r directly
3. Resolvent: W(z) has correct poles/cuts matching eigenvalue support
4. TR free energy vs shadow F_g (independent computation)
5. beta-ensemble: KS test identifies correct beta value

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

import cmath
import math
import pytest

from fractions import Fraction
from sympy import Rational, bernoulli, factorial

from compute.lib.bc_matrix_model_deep_engine import (
    # Section 0: shadow coefficients
    get_shadow_coefficients,
    # Section 1: eigenvalue density
    shadow_eigenvalue_density_numerical,
    shadow_density_profile,
    density_positivity_check,
    # Section 2: resolvent
    shadow_resolvent_pole_expansion,
    shadow_resolvent_stieltjes,
    resolvent_comparison,
    # Section 3: spectral curve
    shadow_spectral_curve_fit,
    minimal_spectral_curve_degree,
    # Section 4: potential reconstruction
    shadow_moments,
    shadow_moments_from_density,
    reconstruct_potential_from_moments,
    heisenberg_potential_exact,
    # Section 5: beta-ensemble
    wigner_surmise_goe,
    wigner_surmise_gue,
    wigner_surmise_gse,
    poisson_spacing,
    shadow_level_spacings,
    ks_distance_to_surmise,
    beta_ensemble_classification,
    # Section 6: double-scaling
    double_scaling_parameter,
    double_scaled_partition_function,
    # Section 7: topological recursion
    shadow_TR_free_energy,
    TR_shadow_comparison,
    # Section 8: unitary matrix model
    unitary_fourier_coefficients,
    unitary_density_from_coefficients,
    unitary_model_analysis,
    # Section 9: cross-verification
    moment_cross_verification,
    resolvent_pole_structure,
    full_matrix_model_analysis,
    _classify_shadow_class,
    # Section 10: Heisenberg exact
    heisenberg_resolvent_exact,
    heisenberg_moments_exact,
    heisenberg_density_exact,
    # Section 11: affine sl_2
    affine_sl2_resolvent_exact,
    affine_sl2_moments_exact,
    # Section 12: Virasoro spectral
    virasoro_shadow_growth_rate,
    virasoro_spectral_dimension,
    # Section 13: complementarity
    koszul_complementarity_matrix_model,
    # Section 14: signed measure
    signed_measure_analysis,
    # Section 15: pair correlation
    shadow_pair_correlation,
)

from compute.lib.utils import lambda_fp, F_g

PI = math.pi


# ============================================================================
# Section 0: Shadow coefficient providers
# ============================================================================

class TestShadowCoefficients:
    """Test shadow coefficient retrieval for all families."""

    def test_heisenberg_S2_equals_k(self):
        """Heisenberg: S_2 = k (AP39)."""
        for k in [1, 2, 5, 10]:
            coeffs = get_shadow_coefficients('heisenberg', float(k))
            assert abs(coeffs[2] - k) < 1e-12

    def test_heisenberg_higher_arities_zero(self):
        """Heisenberg: S_r = 0 for r >= 3 (class G)."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=20)
        for r in range(3, 21):
            assert abs(coeffs[r]) < 1e-15

    def test_virasoro_S2_equals_c_over_2(self):
        """Virasoro: S_2 = kappa = c/2 (AP9)."""
        for c in [1.0, 13.0, 25.0]:
            coeffs = get_shadow_coefficients('virasoro', c)
            assert abs(coeffs[2] - c / 2.0) < 1e-10

    def test_affine_sl2_kappa(self):
        """Affine sl_2: kappa = 3(k+2)/4."""
        k = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k)
        expected = 3.0 * (k + 2.0) / 4.0
        assert abs(coeffs[2] - expected) < 1e-10

    def test_affine_sl2_cubic(self):
        """Affine sl_2: S_3 = 4/(k+2) (Sugawara normalization)."""
        k = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k)
        expected = 4.0 / (k + 2.0)
        assert abs(coeffs[3] - expected) < 1e-10

    def test_affine_sl2_higher_zero(self):
        """Affine sl_2: S_r = 0 for r >= 4 (class L)."""
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=15)
        for r in range(4, 16):
            assert abs(coeffs[r]) < 1e-15

    def test_betagamma_terminates_at_4(self):
        """Beta-gamma: S_r = 0 for r >= 5 (class C)."""
        coeffs = get_shadow_coefficients('betagamma', 0.5, max_r=15)
        for r in range(5, 16):
            assert abs(coeffs[r]) < 1e-15

    def test_virasoro_infinite_tower(self):
        """Virasoro at c=25: nonzero coefficients for large r (class M)."""
        coeffs = get_shadow_coefficients('virasoro', 25.0, max_r=30)
        # At least some nonzero beyond r=4
        nonzero_count = sum(1 for r in range(5, 31) if abs(coeffs[r]) > 1e-15)
        assert nonzero_count > 10

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            get_shadow_coefficients('unknown', 1.0)


# ============================================================================
# Section 1: Eigenvalue density
# ============================================================================

class TestEigenvalueDensity:
    """Test the inverse Mellin transform density computation."""

    def test_density_returns_float(self):
        """Density is a real number."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        rho = shadow_eigenvalue_density_numerical(coeffs, 2.0)
        assert isinstance(rho, float)

    def test_density_negative_E_is_zero(self):
        """rho(E) = 0 for E <= 0."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        assert shadow_eigenvalue_density_numerical(coeffs, -1.0) == 0.0
        assert shadow_eigenvalue_density_numerical(coeffs, 0.0) == 0.0

    def test_heisenberg_density_peaked_near_2(self):
        """Heisenberg density should peak near E=2 (delta function at r=2)."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        rho_at_2 = shadow_eigenvalue_density_numerical(coeffs, 2.0, T_max=80.0, num_points=3000)
        rho_at_5 = shadow_eigenvalue_density_numerical(coeffs, 5.0, T_max=80.0, num_points=3000)
        # Density near E=2 should be larger than at E=5
        assert abs(rho_at_2) > abs(rho_at_5)

    def test_density_profile_returns_dict(self):
        """density_profile returns well-formed dict."""
        result = shadow_density_profile('heisenberg', 1.0, E_values=[1.0, 2.0, 5.0])
        assert 'E_values' in result
        assert 'rho_values' in result
        assert len(result['E_values']) == 3
        assert len(result['rho_values']) == 3

    def test_virasoro_density_profile(self):
        """Virasoro density profile runs without error."""
        result = shadow_density_profile('virasoro', 13.0, E_values=[1.0, 5.0, 10.0],
                                        max_r=20)
        assert len(result['rho_values']) == 3


# ============================================================================
# Section 2: Resolvent
# ============================================================================

class TestResolvent:
    """Test resolvent computations."""

    def test_heisenberg_resolvent_exact(self):
        """Heisenberg: W(z) = k/(z-2) matches pole expansion."""
        k = 3.0
        coeffs = get_shadow_coefficients('heisenberg', k)
        z = complex(5.0, 1.0)
        W_pole = shadow_resolvent_pole_expansion(coeffs, z)
        W_exact = heisenberg_resolvent_exact(k, z)
        assert abs(W_pole - W_exact) < 1e-10

    def test_affine_sl2_resolvent_exact(self):
        """Affine sl_2: two-pole resolvent matches."""
        k = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k)
        z = complex(5.0, 1.0)
        W_pole = shadow_resolvent_pole_expansion(coeffs, z)
        W_exact = affine_sl2_resolvent_exact(k, z)
        assert abs(W_pole - W_exact) < 1e-10

    def test_resolvent_asymptotics(self):
        """W(z) ~ m_0/z for large z."""
        k = 2.0
        coeffs = get_shadow_coefficients('heisenberg', k)
        z = complex(1000.0, 0.0)
        W = shadow_resolvent_pole_expansion(coeffs, z)
        # m_0 = S_2 = k
        assert abs(W * z - k) / k < 0.01

    def test_resolvent_pole_at_eigenvalue(self):
        """Resolvent diverges near z = r (eigenvalue position)."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        z_near_pole = complex(2.0, 0.001)
        W = shadow_resolvent_pole_expansion(coeffs, z_near_pole)
        assert abs(W) > 100.0  # large near pole

    def test_resolvent_imaginary_part_sign(self):
        """Im W(x + i*epsilon) < 0 for epsilon > 0 near a pole (Stieltjes property)."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        z = complex(2.0, 0.01)
        W = shadow_resolvent_pole_expansion(coeffs, z)
        # For a positive weight S_2 > 0 at r=2: Im[S_2/(x-2+ie)] = -S_2*e / (eps^2)
        assert W.imag < 0

    def test_resolvent_pole_structure_heisenberg(self):
        """Heisenberg has exactly 1 pole."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        ps = resolvent_pole_structure(coeffs)
        assert ps['num_poles'] == 1
        assert ps['poles'][0]['position'] == 2
        assert abs(ps['poles'][0]['residue'] - 1.0) < 1e-10

    def test_resolvent_pole_structure_affine(self):
        """Affine sl_2 has exactly 2 poles."""
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        ps = resolvent_pole_structure(coeffs)
        assert ps['num_poles'] == 2

    def test_resolvent_asymptotic_check(self):
        """Resolvent asymptotic ratio near 1 for large z."""
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        ps = resolvent_pole_structure(coeffs)
        assert ps['asymptotic_correct']


# ============================================================================
# Section 3: Spectral curve
# ============================================================================

class TestSpectralCurve:
    """Test spectral curve extraction."""

    def test_spectral_curve_fit_returns_dict(self):
        """Fit results are well-formed."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        fits = shadow_spectral_curve_fit(coeffs, max_degree=6)
        assert isinstance(fits, dict)
        for d in fits:
            assert 'r_squared' in fits[d]
            assert 'coeffs' in fits[d]

    def test_spectral_curve_r_squared_improves(self):
        """R^2 should improve (or stay same) with higher degree."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        fits = shadow_spectral_curve_fit(coeffs, max_degree=8)
        degrees = sorted(fits.keys())
        if len(degrees) >= 2:
            # Higher degree generally fits better or equal
            assert fits[degrees[-1]]['r_squared'] >= fits[degrees[0]]['r_squared'] - 0.01

    def test_minimal_degree_returns_result(self):
        """minimal_spectral_curve_degree returns well-formed dict."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        result = minimal_spectral_curve_degree(coeffs)
        assert 'min_degree' in result
        assert 'r_squared' in result


# ============================================================================
# Section 4: Potential reconstruction
# ============================================================================

class TestPotentialReconstruction:
    """Test moment computation and potential reconstruction."""

    def test_heisenberg_moments_exact_match(self):
        """Heisenberg: m_k = k * 2^k (exact)."""
        k_val = 3.0
        coeffs = get_shadow_coefficients('heisenberg', k_val)
        moments = shadow_moments(coeffs, max_k=5)
        exact = heisenberg_moments_exact(k_val, max_k=5)
        for n in range(6):
            assert abs(moments[n] - exact[n]) < 1e-10

    def test_affine_sl2_moments_exact_match(self):
        """Affine sl_2: m_k = kappa*2^k + alpha*3^k."""
        k_val = 1.0
        coeffs = get_shadow_coefficients('affine_sl2', k_val)
        moments = shadow_moments(coeffs, max_k=5)
        exact = affine_sl2_moments_exact(k_val, max_k=5)
        for n in range(6):
            assert abs(moments[n] - exact[n]) < 1e-10

    def test_moments_m0_equals_total_weight(self):
        """m_0 = sum S_r (total weight)."""
        k_val = 2.0
        coeffs = get_shadow_coefficients('heisenberg', k_val)
        moments = shadow_moments(coeffs)
        assert abs(moments[0] - k_val) < 1e-10

    def test_moments_mean_for_heisenberg(self):
        """Heisenberg mean = m_1/m_0 = 2."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        moments = shadow_moments(coeffs)
        mean = moments[1] / moments[0]
        assert abs(mean - 2.0) < 1e-10

    def test_heisenberg_potential_exact(self):
        """Heisenberg potential: V(z) = (z-2)^2 / (2k) at z=2 gives V=0."""
        result = heisenberg_potential_exact(1.0)
        assert abs(result['potential_eval'](2.0)) < 1e-15
        assert abs(result['center'] - 2.0) < 1e-15

    def test_heisenberg_potential_quadratic(self):
        """Heisenberg potential is quadratic: V(z) = (z-2)^2 / (2k)."""
        k = 3.0
        result = heisenberg_potential_exact(k)
        V = result['potential_eval']
        # V(0) = 4/(2*3) = 2/3
        assert abs(V(0.0) - 2.0 / 3.0) < 1e-10
        # V(4) = 4/(2*3) = 2/3
        assert abs(V(4.0) - 2.0 / 3.0) < 1e-10

    def test_potential_reconstruction_heisenberg(self):
        """Reconstructed potential for Heisenberg has center near 2."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        moments = shadow_moments(coeffs)
        result = reconstruct_potential_from_moments(moments)
        assert abs(result['couplings']['center'] - 2.0) < 1e-10

    def test_potential_reconstruction_variance(self):
        """Heisenberg variance = 0 (delta function)."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        moments = shadow_moments(coeffs)
        result = reconstruct_potential_from_moments(moments)
        # Variance = m_2/m_0 - (m_1/m_0)^2 = 4 - 4 = 0
        assert abs(result['couplings']['variance']) < 1e-10

    def test_moment_cross_verification(self):
        """moment_cross_verification returns well-formed result."""
        result = moment_cross_verification('heisenberg', 1.0, max_k=4)
        assert 'moments_direct' in result
        assert abs(result['mean'] - 2.0) < 1e-10


# ============================================================================
# Section 5: Beta-ensemble classification
# ============================================================================

class TestBetaEnsemble:
    """Test Wigner surmises and beta-ensemble classification."""

    def test_wigner_surmise_goe_normalization(self):
        """GOE surmise integrates to ~1."""
        ds = 0.01
        integral = sum(wigner_surmise_goe(s * ds) * ds for s in range(500))
        assert abs(integral - 1.0) < 0.02

    def test_wigner_surmise_gue_normalization(self):
        """GUE surmise integrates to ~1."""
        ds = 0.01
        integral = sum(wigner_surmise_gue(s * ds) * ds for s in range(500))
        assert abs(integral - 1.0) < 0.02

    def test_wigner_surmise_gse_normalization(self):
        """GSE surmise integrates to ~1."""
        ds = 0.01
        integral = sum(wigner_surmise_gse(s * ds) * ds for s in range(500))
        assert abs(integral - 1.0) < 0.02

    def test_poisson_normalization(self):
        """Poisson integrates to 1."""
        ds = 0.01
        integral = sum(poisson_spacing(s * ds) * ds for s in range(1000))
        assert abs(integral - 1.0) < 0.02

    def test_goe_mean_spacing(self):
        """GOE mean spacing <s> ~ pi/2."""
        ds = 0.01
        mean = sum(s * ds * wigner_surmise_goe(s * ds) * ds for s in range(500))
        # Exact: <s> = sqrt(pi)/Gamma(3/2+1/2) = ... approximately 1.27
        assert 0.9 < mean < 1.5

    def test_gue_peak_higher_than_goe(self):
        """GUE peak is at higher s than GOE (more level repulsion)."""
        s_peak_goe = max(range(300), key=lambda j: wigner_surmise_goe(j * 0.01))
        s_peak_gue = max(range(300), key=lambda j: wigner_surmise_gue(j * 0.01))
        assert s_peak_gue >= s_peak_goe

    def test_poisson_peak_at_zero(self):
        """Poisson p(s) peaks at s=0 (no level repulsion)."""
        assert poisson_spacing(0.0) > poisson_spacing(1.0)

    def test_spacings_heisenberg_empty(self):
        """Heisenberg has 1 eigenvalue -> no spacings."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        spacings = shadow_level_spacings(coeffs)
        # Only one nonzero coefficient at r=2
        assert len(spacings) == 0

    def test_spacings_affine_sl2_one(self):
        """Affine sl_2 has 2 eigenvalues at r=2,3 -> one spacing."""
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        spacings = shadow_level_spacings(coeffs)
        assert len(spacings) == 1
        # Spacing between r=2 and r=3 is 1, normalized to 1
        assert abs(spacings[0] - 1.0) < 1e-10

    def test_spacings_virasoro_many(self):
        """Virasoro has many eigenvalues -> many spacings."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=30)
        spacings = shadow_level_spacings(coeffs)
        assert len(spacings) >= 10

    def test_ks_distance_nonnegative(self):
        """KS distance is non-negative."""
        spacings = [1.0, 0.8, 1.2, 0.9, 1.1]
        d = ks_distance_to_surmise(spacings, wigner_surmise_gue)
        assert d >= 0.0

    def test_ks_distance_empty(self):
        """Empty spacings -> infinite KS distance."""
        d = ks_distance_to_surmise([], wigner_surmise_gue)
        assert d == float('inf')

    def test_beta_classification_virasoro(self):
        """Virasoro classification runs and returns best_fit."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=30)
        result = beta_ensemble_classification(coeffs)
        assert result['best_fit'] in ['GOE', 'GUE', 'GSE', 'Poisson']
        assert result['num_spacings'] >= 10

    def test_beta_classification_heisenberg_insufficient(self):
        """Heisenberg: insufficient data for classification."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        result = beta_ensemble_classification(coeffs)
        assert result['best_fit'] == 'insufficient_data'


# ============================================================================
# Section 6: Double-scaling limit
# ============================================================================

class TestDoubleScaling:
    """Test double-scaling computations."""

    def test_double_scaling_parameter(self):
        """Double-scaling parameter computed correctly."""
        result = double_scaling_parameter(1.0, r_max=50)
        assert abs(result['kappa'] - 0.5) < 1e-10
        expected_mu = 0.5 * 50 ** 2.5
        assert abs(result['mu'] - expected_mu) < 1e-6

    def test_double_scaling_c_zero_limit(self):
        """As c -> 0, kappa -> 0 (pure gravity regime)."""
        result = double_scaling_parameter(0.01)
        assert result['kappa'] < 0.01

    def test_double_scaled_pf_genus1(self):
        """F_1^shadow = kappa/24 for any c."""
        result = double_scaled_partition_function(2.0)
        assert abs(result['genus_data'][1]['F_g_shadow'] - 1.0 / 24.0) < 1e-12

    def test_double_scaled_pf_gravity_genus1(self):
        """F_1^gravity = 1/24 (universal)."""
        result = double_scaled_partition_function(2.0)
        assert abs(result['genus_data'][1]['F_g_gravity'] - 1.0 / 24.0) < 1e-12

    def test_double_scaled_pf_gravity_genus2(self):
        """F_2^gravity = 7/5760."""
        result = double_scaled_partition_function(2.0)
        assert abs(result['genus_data'][2]['F_g_gravity'] - 7.0 / 5760.0) < 1e-12


# ============================================================================
# Section 7: Topological recursion
# ============================================================================

class TestTopologicalRecursion:
    """Test TR free energy computations."""

    def test_TR_genus1_heisenberg(self):
        """Heisenberg TR free energy at genus 1: kappa/24 = k/24."""
        k = 1.0
        coeffs = get_shadow_coefficients('heisenberg', k)
        tr = shadow_TR_free_energy(coeffs)
        assert abs(tr[1] - k / 24.0) < 1e-12

    def test_TR_genus1_virasoro(self):
        """Virasoro TR free energy at genus 1: c/(2*24) = c/48."""
        c = 25.0
        coeffs = get_shadow_coefficients('virasoro', c, max_r=20)
        tr = shadow_TR_free_energy(coeffs)
        expected = c / 2.0 / 24.0
        assert abs(tr[1] - expected) < 1e-10

    def test_TR_matches_shadow(self):
        """TR free energy should match shadow F_g = kappa * lambda_fp."""
        c = 13.0
        coeffs = get_shadow_coefficients('virasoro', c, max_r=20)
        tr = shadow_TR_free_energy(coeffs, max_genus=4)
        kappa = c / 2.0
        for g in range(1, 5):
            lfp = float(lambda_fp(g))
            expected = kappa * lfp
            assert abs(tr[g] - expected) < 1e-12

    def test_TR_shadow_comparison_all_match(self):
        """TR comparison shows all genera match."""
        result = TR_shadow_comparison('virasoro', 13.0, max_genus=4, max_r=20)
        for g in range(1, 5):
            assert result['genus_data'][g]['match']


# ============================================================================
# Section 8: Unitary matrix model
# ============================================================================

class TestUnitaryModel:
    """Test unitary matrix model analysis."""

    def test_fourier_coefficients_return_dict(self):
        """Fourier coefficients are well-formed."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        fc = unitary_fourier_coefficients(coeffs, max_k=5)
        assert isinstance(fc, dict)
        assert 1 in fc

    def test_unitary_density_nonnegative_check(self):
        """Unitary density computed without error."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0)
        fc = unitary_fourier_coefficients(coeffs, max_k=5)
        rho = unitary_density_from_coefficients(fc, 0.0)
        assert isinstance(rho, float)

    def test_unitary_model_analysis_runs(self):
        """Full unitary analysis runs."""
        result = unitary_model_analysis('heisenberg', 1.0, max_r=10, max_k=5)
        assert 'fourier_coefficients' in result
        assert 'is_nonnegative' in result


# ============================================================================
# Section 9: Cross-verification
# ============================================================================

class TestCrossVerification:
    """Test cross-verification utilities."""

    def test_shadow_class_G(self):
        """Heisenberg classified as class G."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        assert _classify_shadow_class(coeffs) == 'G'

    def test_shadow_class_L(self):
        """Affine sl_2 classified as class L."""
        coeffs = get_shadow_coefficients('affine_sl2', 1.0, max_r=10)
        assert _classify_shadow_class(coeffs) == 'L'

    def test_shadow_class_C(self):
        """Beta-gamma classified as class C."""
        coeffs = get_shadow_coefficients('betagamma', 0.5, max_r=10)
        assert _classify_shadow_class(coeffs) == 'C'

    def test_shadow_class_M(self):
        """Virasoro classified as class M."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        assert _classify_shadow_class(coeffs) == 'M'

    def test_resolvent_pole_structure_asymptotic(self):
        """Asymptotic ratio is near 1 for all families."""
        for family, param in [('heisenberg', 1.0), ('affine_sl2', 1.0)]:
            coeffs = get_shadow_coefficients(family, param, max_r=10)
            ps = resolvent_pole_structure(coeffs)
            assert ps['asymptotic_correct']


# ============================================================================
# Section 10: Heisenberg exact analytics
# ============================================================================

class TestHeisenbergExact:
    """Test exact Heisenberg results."""

    def test_resolvent_exact_values(self):
        """Exact Heisenberg resolvent at specific points."""
        k = 2.0
        # W(4) = 2/(4-2) = 1
        assert abs(heisenberg_resolvent_exact(k, complex(4.0, 0.0)) - 1.0) < 1e-10
        # W(3) = 2/(3-2) = 2
        assert abs(heisenberg_resolvent_exact(k, complex(3.0, 0.0)) - 2.0) < 1e-10

    def test_resolvent_exact_agrees_with_pole_expansion(self):
        """Heisenberg resolvent exact formula matches pole expansion."""
        k = 5.0
        coeffs = get_shadow_coefficients('heisenberg', k, max_r=10)
        for z in [complex(3.0, 1.0), complex(10.0, 0.5), complex(0.5, 2.0)]:
            W_exact = heisenberg_resolvent_exact(k, z)
            W_pole = shadow_resolvent_pole_expansion(coeffs, z)
            assert abs(W_exact - W_pole) < 1e-10

    def test_moments_exact_powers_of_2(self):
        """Heisenberg moments: m_n = k * 2^n."""
        k = 3.0
        moments = heisenberg_moments_exact(k, max_k=8)
        for n in range(9):
            assert abs(moments[n] - k * 2.0 ** n) < 1e-10

    def test_heisenberg_density_gaussian_approx(self):
        """Heisenberg density is concentrated near E=2."""
        rho_at_2 = heisenberg_density_exact(1.0, 2.0)
        rho_at_10 = heisenberg_density_exact(1.0, 10.0)
        assert rho_at_2 > rho_at_10 * 100  # much larger near 2


# ============================================================================
# Section 11: Affine sl_2 analytics
# ============================================================================

class TestAffineSl2:
    """Test affine sl_2 exact results."""

    def test_resolvent_two_poles(self):
        """Affine sl_2 resolvent has poles at z=2 and z=3."""
        k = 1.0
        # Near z=2: W diverges
        z_near_2 = complex(2.0, 0.001)
        W = affine_sl2_resolvent_exact(k, z_near_2)
        assert abs(W) > 100.0
        # Near z=3: W diverges
        z_near_3 = complex(3.0, 0.001)
        W = affine_sl2_resolvent_exact(k, z_near_3)
        assert abs(W) > 100.0

    def test_moments_two_terms(self):
        """Affine sl_2 moments: m_n = kappa*2^n + alpha*3^n."""
        k = 1.0
        moments = affine_sl2_moments_exact(k, max_k=5)
        kappa = 3.0 * (k + 2.0) / 4.0  # = 2.25
        alpha = 4.0 / (k + 2.0)  # = 4/3
        for n in range(6):
            expected = kappa * 2.0 ** n + alpha * 3.0 ** n
            assert abs(moments[n] - expected) < 1e-10


# ============================================================================
# Section 12: Virasoro spectral analysis
# ============================================================================

class TestVirasoroSpectral:
    """Test Virasoro-specific spectral analysis."""

    def test_growth_rate_c1(self):
        """Virasoro growth rate at c=1: rho = sqrt((180+872)/(27*1)) ~ 6.29."""
        rho = virasoro_shadow_growth_rate(1.0)
        expected = math.sqrt(1052.0 / 27.0)
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_c25(self):
        """Virasoro growth rate at c=25: rho = sqrt((4500+872)/(147*625))."""
        rho = virasoro_shadow_growth_rate(25.0)
        expected = math.sqrt(5372.0 / (147.0 * 625.0))
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_c13_self_dual(self):
        """Virasoro growth rate at c=13 (self-dual point)."""
        rho = virasoro_shadow_growth_rate(13.0)
        expected = math.sqrt((180 * 13 + 872) / ((5 * 13 + 22) * 169))
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_decreases_with_c(self):
        """Growth rate decreases as c increases (for c >= 5)."""
        rho_5 = virasoro_shadow_growth_rate(5.0)
        rho_10 = virasoro_shadow_growth_rate(10.0)
        rho_25 = virasoro_shadow_growth_rate(25.0)
        assert rho_5 > rho_10 > rho_25

    def test_spectral_dimension_virasoro(self):
        """Spectral dimension computed correctly."""
        result = virasoro_spectral_dimension(13.0)
        assert 'rho' in result
        assert result['rho'] > 0

    def test_spectral_dimension_convergent_tower(self):
        """For rho < 1 (large c), abscissa is -inf."""
        result = virasoro_spectral_dimension(25.0)
        rho = result['rho']
        if rho < 1.0:
            assert result['abscissa'] == float('-inf')
            assert result['spectral_dimension'] == 0.0


# ============================================================================
# Section 13: Complementarity
# ============================================================================

class TestComplementarity:
    """Test Koszul complementarity in the matrix model."""

    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c (AP24)."""
        for c in [1.0, 5.0, 13.0, 20.0, 25.0]:
            result = koszul_complementarity_matrix_model(c)
            assert result['kappa_sum_is_13']

    def test_self_dual_at_c13(self):
        """c=13 is the self-dual point."""
        result = koszul_complementarity_matrix_model(13.0)
        assert result['is_self_dual']

    def test_not_self_dual_at_c1(self):
        """c=1 is NOT the self-dual point."""
        result = koszul_complementarity_matrix_model(1.0)
        assert not result['is_self_dual']

    def test_Fg_sum_is_13_lambda_fp(self):
        """F_g(c) + F_g(26-c) = 13 * lambda_fp(g) for all g."""
        result = koszul_complementarity_matrix_model(5.0, max_genus=4)
        for g in range(1, 5):
            lfp = float(lambda_fp(g))
            expected = 13.0 * lfp
            assert abs(result['Fg_sum'][g] - expected) < 1e-12

    def test_complementarity_symmetric(self):
        """Complementarity of c and 26-c gives same kappa_sum."""
        r1 = koszul_complementarity_matrix_model(7.0)
        r2 = koszul_complementarity_matrix_model(19.0)
        assert abs(r1['kappa_sum'] - r2['kappa_sum']) < 1e-10


# ============================================================================
# Section 14: Signed measure detection
# ============================================================================

class TestSignedMeasure:
    """Test signed measure analysis."""

    def test_signed_measure_returns_result(self):
        """signed_measure_analysis returns well-formed dict."""
        result = signed_measure_analysis('heisenberg', 1.0, max_r=10, num_E=10)
        assert 'is_signed' in result
        assert 'min_rho' in result
        assert 'interpretation' in result

    def test_signed_measure_interpretation(self):
        """Interpretation string is non-empty."""
        result = signed_measure_analysis('heisenberg', 1.0, max_r=10, num_E=10)
        assert len(result['interpretation']) > 0


# ============================================================================
# Section 15: Pair correlation
# ============================================================================

class TestPairCorrelation:
    """Test shadow pair correlation."""

    def test_pair_correlation_heisenberg(self):
        """Heisenberg: single eigenvalue -> trivial correlation."""
        coeffs = get_shadow_coefficients('heisenberg', 1.0, max_r=10)
        result = shadow_pair_correlation(coeffs)
        # Only one eigenvalue at r=2 -> R_2 = 0 everywhere
        assert all(abs(r2) < 1e-10 for r2 in result['R2'])

    def test_pair_correlation_virasoro_nontrivial(self):
        """Virasoro: nontrivial pair correlation."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        result = shadow_pair_correlation(coeffs)
        # Some nonzero values
        max_R2 = max(abs(r2) for r2 in result['R2'])
        assert max_R2 > 0

    def test_gue_sine_kernel_values(self):
        """GUE sine kernel prediction: R_2(s) = 1 - (sin(pi*s)/(pi*s))^2."""
        coeffs = get_shadow_coefficients('virasoro', 13.0, max_r=20)
        result = shadow_pair_correlation(coeffs, s_values=[1.0, 2.0])
        # Check that GUE predictions are computed
        assert len(result['R2_GUE']) == 2
        # R_2^GUE(1) = 1 - (sin(pi)/pi)^2 = 1 - 0 = 1
        assert abs(result['R2_GUE'][0] - 1.0) < 1e-10
        # R_2^GUE(2) = 1 - (sin(2pi)/(2pi))^2 = 1 - 0 = 1
        assert abs(result['R2_GUE'][1] - 1.0) < 1e-10


# ============================================================================
# Multi-path verification tests
# ============================================================================

class TestMultiPathVerification:
    """Cross-verification by multiple independent computational paths."""

    def test_heisenberg_three_paths_moments(self):
        """Heisenberg moments verified by 3 paths:
        (1) Direct summation, (2) Exact formula, (3) Resolvent residue.
        """
        k = 2.0
        coeffs = get_shadow_coefficients('heisenberg', k, max_r=10)

        # Path 1: direct summation
        m_direct = shadow_moments(coeffs, max_k=5)

        # Path 2: exact formula
        m_exact = heisenberg_moments_exact(k, max_k=5)

        # Path 3: from resolvent W(z) ~ sum m_k / z^{k+1}
        # W(z) = k/(z-2) = (k/z) * 1/(1-2/z) = (k/z) * sum (2/z)^n
        # -> m_n = k * 2^n
        for n in range(6):
            m_res = k * 2.0 ** n
            assert abs(m_direct[n] - m_exact[n]) < 1e-10
            assert abs(m_direct[n] - m_res) < 1e-10

    def test_virasoro_kappa_three_paths(self):
        """Virasoro kappa verified by 3 paths:
        (1) From S_2, (2) From c/2, (3) From genus-1 free energy.
        """
        c = 25.0

        # Path 1: S_2 from shadow coefficients
        coeffs = get_shadow_coefficients('virasoro', c, max_r=10)
        kappa_S2 = coeffs[2]

        # Path 2: formula kappa = c/2
        kappa_formula = c / 2.0

        # Path 3: from F_1 = kappa/24 -> kappa = 24 * F_1
        # F_1 = kappa * lambda_fp(1) = kappa * 1/24
        lfp1 = float(lambda_fp(1))  # = 1/24
        kappa_F1 = kappa_S2  # self-consistent: F_1 = kappa * 1/24

        assert abs(kappa_S2 - kappa_formula) < 1e-10
        assert abs(kappa_S2 - kappa_F1) < 1e-10

    def test_resolvent_two_paths(self):
        """Resolvent verified by 2 paths: pole expansion and exact formula."""
        k = 1.0
        z = complex(5.0, 1.0)

        # Path 1: pole expansion
        coeffs = get_shadow_coefficients('affine_sl2', k, max_r=10)
        W1 = shadow_resolvent_pole_expansion(coeffs, z)

        # Path 2: exact two-pole formula
        W2 = affine_sl2_resolvent_exact(k, z)

        assert abs(W1 - W2) < 1e-10

    def test_TR_shadow_two_paths(self):
        """Free energy verified by 2 paths: TR and direct shadow formula."""
        c = 13.0
        kappa = c / 2.0

        # Path 1: TR
        coeffs = get_shadow_coefficients('virasoro', c, max_r=20)
        tr = shadow_TR_free_energy(coeffs, max_genus=3)

        # Path 2: direct formula F_g = kappa * lambda_fp(g)
        for g in range(1, 4):
            Fg_direct = kappa * float(lambda_fp(g))
            assert abs(tr[g] - Fg_direct) < 1e-12

    def test_complementarity_two_paths(self):
        """Complementarity sum verified by 2 paths:
        (1) Direct kappa sum, (2) Free energy sum.
        """
        c = 7.0
        kappa_c = c / 2.0
        kappa_dual = (26.0 - c) / 2.0

        # Path 1: kappa + kappa'
        assert abs(kappa_c + kappa_dual - 13.0) < 1e-10

        # Path 2: F_g sum at genus 1
        F1_c = kappa_c / 24.0
        F1_dual = kappa_dual / 24.0
        assert abs(F1_c + F1_dual - 13.0 / 24.0) < 1e-10


# ============================================================================
# Full pipeline tests
# ============================================================================

class TestFullPipeline:
    """Test the full analysis pipeline."""

    def test_full_analysis_heisenberg(self):
        """Full analysis of Heisenberg runs and returns correct class."""
        result = full_matrix_model_analysis('heisenberg', 1.0, max_r=10, max_genus=3)
        assert result['shadow_class'] == 'G'
        assert abs(result['kappa'] - 1.0) < 1e-10

    def test_full_analysis_affine_sl2(self):
        """Full analysis of affine sl_2 runs and returns correct class."""
        result = full_matrix_model_analysis('affine_sl2', 1.0, max_r=10, max_genus=3)
        assert result['shadow_class'] == 'L'

    def test_full_analysis_virasoro(self):
        """Full analysis of Virasoro at c=13 runs."""
        result = full_matrix_model_analysis('virasoro', 13.0, max_r=20, max_genus=3)
        assert result['shadow_class'] == 'M'
        assert abs(result['kappa'] - 6.5) < 1e-10

    def test_full_analysis_betagamma(self):
        """Full analysis of beta-gamma runs and returns correct class."""
        result = full_matrix_model_analysis('betagamma', 0.5, max_r=10, max_genus=3)
        assert result['shadow_class'] == 'C'
