r"""Tests for the shadow partition function convergence atlas.

Comprehensive verification of convergence radii for ALL standard families:

1. GENUS CONVERGENCE: R_genus = 2*pi (universal)
2. ARITY CONVERGENCE: R_arity = 1/rho (family-dependent)
3. DOUBLE CONVERGENCE DOMAIN: D(A) = B(0, R_genus) x B(0, R_arity)
4. SHADOW GROWTH RATE ATLAS: rho(A) for every standard family
5. PERTURBATIVE vs NON-PERTURBATIVE: shadow (convergent) vs string (divergent)
6. BOREL SUMMABILITY: shadow Borel transform is entire
7. PHASE TRANSITION: c < c* divergent, c > c* convergent
8. ANALYTIC CONTINUATION: complex hbar, Lorentzian evaluation

60+ tests covering the full convergence landscape.

Manuscript references:
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    prop:genus-expansion-convergence (genus_expansions.tex)
    rem:convergence-vs-string (genus_expansions.tex)
    def:shadow-growth-rate (higher_genus_modular_koszul.tex)
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import math
import cmath
import pytest

from sympy import Rational

from compute.lib.shadow_pf_convergence_atlas import (
    # Kappa values
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_affine_slN,
    kappa_affine_general,
    kappa_wN,
    # Shadow radii
    virasoro_rho_squared,
    virasoro_rho,
    w3_wline_rho_squared,
    w3_rho_effective,
    wN_channel_rho,
    wN_rho_effective,
    critical_central_charge,
    # Genus convergence
    genus_convergence_radius,
    genus_series_closed_form,
    genus_series_partial_sum,
    # Arity convergence
    arity_convergence_radius,
    # Atlas
    shadow_growth_rate_atlas,
    FamilyConvergenceData,
    family_convergence,
    # Double convergence
    DoubleConvergenceDomain,
    double_convergence_domain,
    double_convergence_domains_table,
    # Comparison
    shadow_vs_string_comparison,
    borel_comparison,
    # Phase transition
    phase_transition_scan,
    # Analytic continuation
    analytic_continuation_complex_hbar,
    lorentzian_evaluation,
    # Koszul
    koszul_convergence_comparison,
    # Free field limit
    affine_sl2_free_field_limit,
    # Tables
    full_convergence_table,
    virasoro_convergence_scan,
    # Bound
    polylogarithm_5_2,
    double_convergence_bound,
    # Bernoulli
    bernoulli_decay_table,
    genus_ratio_table,
    # Constants
    TWO_PI,
    TWO_PI_SQ,
    PI,
)

from compute.lib.utils import lambda_fp


# ============================================================================
# Class 1: Kappa values for all families
# ============================================================================

class TestKappaValues:
    """Test kappa(A) for all standard families."""

    def test_kappa_heisenberg_rank1(self):
        """kappa(H, rank 1) = 1/2."""
        assert abs(kappa_heisenberg(1) - 0.5) < 1e-14

    def test_kappa_heisenberg_rank8(self):
        """kappa(H, rank 8) = 4."""
        assert abs(kappa_heisenberg(8) - 4.0) < 1e-14

    def test_kappa_virasoro_c1(self):
        """kappa(Vir, c=1) = 1/2."""
        assert abs(kappa_virasoro(1.0) - 0.5) < 1e-14

    def test_kappa_virasoro_c26(self):
        """kappa(Vir, c=26) = 13."""
        assert abs(kappa_virasoro(26.0) - 13.0) < 1e-14

    def test_kappa_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4."""
        assert abs(kappa_affine_sl2(1) - 9.0 / 4.0) < 1e-14

    def test_kappa_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/6 = 16/3."""
        assert abs(kappa_affine_slN(3, 1) - 16.0 / 3.0) < 1e-12

    def test_kappa_wN_virasoro(self):
        """kappa(W_2, c) = kappa(Vir, c) = c/2."""
        for c_val in [1.0, 13.0, 26.0]:
            assert abs(kappa_wN(2, c_val) - c_val / 2.0) < 1e-14

    def test_kappa_w3(self):
        """kappa(W_3, c) = c/2 + c/3 = 5c/6."""
        for c_val in [6.0, 50.0, 100.0]:
            assert abs(kappa_wN(3, c_val) - 5.0 * c_val / 6.0) < 1e-12

    def test_kappa_w4(self):
        """kappa(W_4, c) = c/2 + c/3 + c/4 = 13c/12."""
        assert abs(kappa_wN(4, 12.0) - 13.0) < 1e-12

    def test_kappa_affine_E8_k1(self):
        """kappa(E_8, k=1) = 248*(1+30)/(2*30) = 248*31/60."""
        expected = 248.0 * 31.0 / 60.0
        assert abs(kappa_affine_general(248, 1, 30) - expected) < 1e-10


# ============================================================================
# Class 2: Shadow growth rate rho
# ============================================================================

class TestShadowRadius:
    """Test shadow growth rate rho(A) for all families."""

    def test_virasoro_rho_c13(self):
        """rho(Vir, c=13) ~ 0.467 (self-dual)."""
        rho = virasoro_rho(13.0)
        assert abs(rho - 0.467) < 0.01

    def test_virasoro_rho_c26(self):
        """rho(Vir, c=26) ~ 0.234."""
        rho = virasoro_rho(26.0)
        assert abs(rho - 0.234) < 0.01

    def test_virasoro_rho_c_half(self):
        """rho(Vir, c=1/2) > 1 (divergent, below c*)."""
        rho = virasoro_rho(0.5)
        assert rho > 1.0

    def test_virasoro_rho_c1(self):
        """rho(Vir, c=1) > 1 (divergent, below c*)."""
        rho = virasoro_rho(1.0)
        assert rho > 1.0

    def test_virasoro_rho_monotone_decreasing(self):
        """rho(Vir_c) is decreasing for c > c* (approaching free field)."""
        c_star = critical_central_charge()
        rho_prev = virasoro_rho(c_star + 1.0)
        for c_val in [10.0, 13.0, 20.0, 26.0, 50.0]:
            rho_curr = virasoro_rho(c_val)
            assert rho_curr < rho_prev or abs(rho_curr - rho_prev) < 1e-10
            rho_prev = rho_curr

    def test_critical_central_charge(self):
        """c* ~ 6.125 where rho(Vir_{c*}) = 1."""
        c_star = critical_central_charge()
        assert abs(c_star - 6.125) < 0.01
        # Verify rho = 1 at c*
        rho = virasoro_rho(c_star)
        assert abs(rho - 1.0) < 1e-6

    def test_w3_wline_rho_at_c50(self):
        """W_3 W-line rho at c=50 (self-dual) is small."""
        rho_W = math.sqrt(w3_wline_rho_squared(50.0))
        assert rho_W < 1.0  # convergent
        assert rho_W < virasoro_rho(50.0)  # W-line rho < T-line rho at large c

    def test_w3_effective_rho_is_max(self):
        """Effective rho = max(rho_T, rho_W)."""
        c_val = 50.0
        rho_eff = w3_rho_effective(c_val)
        rho_T = virasoro_rho(c_val)
        rho_W = math.sqrt(w3_wline_rho_squared(c_val))
        assert abs(rho_eff - max(rho_T, rho_W)) < 1e-14

    def test_wN_channel_T_equals_virasoro(self):
        """T-channel rho for any W_N equals Virasoro rho."""
        for c_val in [10.0, 50.0, 100.0]:
            for N in [3, 4, 5]:
                assert abs(wN_channel_rho(N, 2, c_val) - virasoro_rho(c_val)) < 1e-14

    def test_wN_higher_channels_smaller_at_large_c(self):
        """Higher W_j channels have smaller rho at large c."""
        c_val = 100.0
        rho_T = wN_channel_rho(4, 2, c_val)
        rho_W3 = wN_channel_rho(4, 3, c_val)
        rho_W4 = wN_channel_rho(4, 4, c_val)
        # At large c, higher channels decay faster
        assert rho_W3 < rho_T
        assert rho_W4 < rho_W3

    def test_virasoro_rho_squared_formula(self):
        """Verify rho^2 = (180c + 872) / ((5c+22)*c^2)."""
        for c_val in [1.0, 5.0, 13.0, 26.0]:
            rho_sq = virasoro_rho_squared(c_val)
            expected = (180 * c_val + 872) / ((5 * c_val + 22) * c_val ** 2)
            assert abs(rho_sq - expected) < 1e-12


# ============================================================================
# Class 3: Genus convergence radius
# ============================================================================

class TestGenusConvergence:
    """Test the universal genus convergence radius R_genus = 2*pi."""

    def test_convergence_radius_value(self):
        """R_genus = 2*pi ~ 6.2832."""
        assert abs(genus_convergence_radius() - TWO_PI) < 1e-10

    def test_closed_form_at_hbar_1(self):
        """Closed form agrees with partial sum at hbar = 1."""
        kappa = 1.0
        closed = genus_series_closed_form(kappa, 1.0)
        partial = genus_series_partial_sum(kappa, 50, 1.0)
        assert abs(partial - closed) / abs(closed) < 1e-10

    def test_closed_form_at_hbar_5(self):
        """Convergence at hbar = 5 (inside disc, slow)."""
        kappa = 0.5
        closed = genus_series_closed_form(kappa, 5.0)
        partial = genus_series_partial_sum(kappa, 80, 5.0)
        assert abs(partial - closed) / abs(closed) < 1e-3

    def test_divergence_at_hbar_2pi(self):
        """Series diverges at hbar = 2*pi (pole)."""
        # At hbar = 2*pi, sin(pi) = 0 -> pole
        # Approaching from below should give large values
        kappa = 1.0
        val = genus_series_closed_form(kappa, TWO_PI - 0.001)
        assert abs(val) > 100  # should be very large

    def test_genus_convergence_radius_is_universal(self):
        """R_genus = 2*pi regardless of kappa."""
        # R_genus comes from the poles of (hbar/2)/sin(hbar/2),
        # independent of the multiplicative factor kappa.
        assert genus_convergence_radius() == TWO_PI


# ============================================================================
# Class 4: Arity convergence radius
# ============================================================================

class TestArityConvergence:
    """Test arity convergence radius R_arity = 1/rho."""

    def test_arity_radius_class_G(self):
        """Class G (rho=0): R_arity = infinity."""
        assert arity_convergence_radius(0.0) == float('inf')

    def test_arity_radius_class_L(self):
        """Class L (rho=0): R_arity = infinity."""
        assert arity_convergence_radius(0.0) == float('inf')

    def test_arity_radius_virasoro_c13(self):
        """Virasoro c=13: R_arity ~ 2.14."""
        rho = virasoro_rho(13.0)
        R = arity_convergence_radius(rho)
        assert abs(R - 1.0 / rho) < 1e-10
        assert R > 1.0  # convergent since rho < 1

    def test_arity_radius_virasoro_c1(self):
        """Virasoro c=1: R_arity < 1 (divergent)."""
        rho = virasoro_rho(1.0)
        R = arity_convergence_radius(rho)
        assert R < 1.0  # divergent since rho > 1


# ============================================================================
# Class 5: Full atlas
# ============================================================================

class TestShadowGrowthRateAtlas:
    """Test the complete shadow growth rate atlas."""

    def test_atlas_contains_all_classes(self):
        """Atlas contains representatives of all four depth classes."""
        atlas = shadow_growth_rate_atlas()
        classes = {d.depth_class for d in atlas.values()}
        assert 'G' in classes
        assert 'L' in classes
        assert 'C' in classes
        assert 'M' in classes

    def test_atlas_class_G_rho_zero(self):
        """All class G families have rho = 0."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if data.depth_class == 'G':
                assert data.rho == 0.0, f"{key}: expected rho=0, got {data.rho}"

    def test_atlas_class_L_rho_zero(self):
        """All class L families have rho = 0."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if data.depth_class == 'L':
                assert data.rho == 0.0, f"{key}: expected rho=0, got {data.rho}"

    def test_atlas_class_M_rho_positive(self):
        """All class M families have rho > 0."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if data.depth_class == 'M':
                assert data.rho > 0.0, f"{key}: expected rho > 0, got {data.rho}"

    def test_atlas_R_genus_universal(self):
        """R_genus = 2*pi for ALL families."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            assert abs(data.R_genus - TWO_PI) < 1e-10, \
                f"{key}: R_genus = {data.R_genus}"

    def test_atlas_genus_convergent_always(self):
        """genus_convergent = True for ALL families."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            assert data.genus_convergent, f"{key}: genus not convergent"

    def test_atlas_double_convergent_when_rho_small(self):
        """double_convergent iff rho < 1."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if data.rho < 1.0:
                assert data.double_convergent, \
                    f"{key}: rho={data.rho} < 1 but not double convergent"
            elif data.rho > 1.0:
                assert not data.double_convergent, \
                    f"{key}: rho={data.rho} > 1 but marked double convergent"

    def test_atlas_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all families."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            assert abs(data.F1 - data.kappa / 24.0) < 1e-14, \
                f"{key}: F1={data.F1} != kappa/24={data.kappa/24.0}"

    def test_atlas_exceptional_types(self):
        """Exceptional affine types G2, F4, E6, E7, E8 are all class L."""
        atlas = shadow_growth_rate_atlas()
        for lie_type in ['G2', 'F4', 'E6', 'E7', 'E8']:
            key = f'{lie_type}_k1'
            assert key in atlas, f"Missing {key}"
            assert atlas[key].depth_class == 'L'
            assert atlas[key].rho == 0.0

    def test_atlas_non_simply_laced(self):
        """Non-simply-laced types B2, C2, B3, C3 are all class L."""
        atlas = shadow_growth_rate_atlas()
        for lie_type in ['B2', 'C2', 'B3', 'C3']:
            key = f'{lie_type}_k1'
            assert key in atlas, f"Missing {key}"
            assert atlas[key].depth_class == 'L'

    def test_atlas_virasoro_self_dual(self):
        """Virasoro c=13 is self-dual: rho(13) = rho(13)."""
        atlas = shadow_growth_rate_atlas()
        data = atlas['Vir_c=13']
        assert abs(data.parameters['c'] - 13.0) < 1e-10

    def test_atlas_has_correct_count(self):
        """Atlas has a reasonable number of entries (30+)."""
        atlas = shadow_growth_rate_atlas()
        assert len(atlas) >= 30


# ============================================================================
# Class 6: Double convergence domain
# ============================================================================

class TestDoubleConvergenceDomain:
    """Test the double convergence domain D(A)."""

    def test_domain_heisenberg(self):
        """Heisenberg: D = {|hbar| < 2*pi} x C (infinite arity radius)."""
        dom = double_convergence_domain(0.5, 0.0, 'Heisenberg')
        assert dom.R_genus == TWO_PI
        assert dom.R_arity == float('inf')
        assert dom.is_convergent

    def test_domain_virasoro_c13(self):
        """Virasoro c=13: finite R_arity."""
        rho = virasoro_rho(13.0)
        dom = double_convergence_domain(6.5, rho, 'Vir_13')
        assert abs(dom.R_genus - TWO_PI) < 1e-10
        assert dom.R_arity > 1.0
        assert dom.is_convergent

    def test_domain_virasoro_c1_divergent(self):
        """Virasoro c=1: divergent arity."""
        rho = virasoro_rho(1.0)
        dom = double_convergence_domain(0.5, rho, 'Vir_1')
        assert not dom.is_convergent

    def test_domains_table_entries(self):
        """Double convergence domains table has correct families."""
        table = double_convergence_domains_table()
        names = {entry['name'] for entry in table}
        assert 'Vir c=13' in names
        assert 'Vir c=26' in names
        assert 'W_3 c=50' in names
        assert 'sl_2 k=1' in names

    def test_domains_table_sl2_infinite_arity(self):
        """All sl_2 entries have R_arity = infinity."""
        table = double_convergence_domains_table()
        for entry in table:
            if 'sl_2' in entry['name']:
                assert entry['R_arity'] == float('inf')
                assert entry['rho'] == 0.0
                assert entry['double_convergent']


# ============================================================================
# Class 7: Shadow vs string comparison
# ============================================================================

class TestShadowVsString:
    """Test the shadow vs string perturbative comparison."""

    def test_ratio_decreases_monotonically(self):
        """F_g^{sh} / F_g^{str} decreases with g."""
        result = shadow_vs_string_comparison(1.0, max_genus=10)
        ratios = [d['ratio'] for d in result['data']]
        for i in range(1, len(ratios)):
            assert ratios[i] < ratios[i - 1]

    def test_factorial_decay_confirmed(self):
        """The ratio decays faster than geometrically."""
        result = shadow_vs_string_comparison(1.0, max_genus=10)
        assert result['factorial_decay_confirmed']

    def test_log_ratio_drops_fast(self):
        """log10 of the ratio drops fast with g."""
        result = shadow_vs_string_comparison(1.0, max_genus=10)
        log_ratios = [d['log10_ratio'] for d in result['data']]
        # Each genus adds roughly -log10((2*pi)^2 * (2g)*(2g-1)) ~ -2 to -4
        assert log_ratios[-1] < -15  # very small by g=10

    def test_shadow_convergent_string_divergent(self):
        """Shadow terms decrease, string terms increase."""
        result = shadow_vs_string_comparison(1.0, max_genus=8)
        shadow = [d['F_g_shadow'] for d in result['data']]
        string = [d['F_g_string'] for d in result['data']]
        # Shadow decreases after g=1
        for i in range(2, len(shadow)):
            assert shadow[i] < shadow[i - 1]
        # String increases monotonically
        for i in range(1, len(string)):
            assert string[i] > string[i - 1]


# ============================================================================
# Class 8: Borel comparison
# ============================================================================

class TestBorelComparison:
    """Test Borel summability comparison."""

    def test_borel_transform_finite(self):
        """Shadow Borel transform is finite at all test points."""
        result = borel_comparison(1.0, [0.1, 0.5, 1.0, 2.0])
        for entry in result['results']:
            if not math.isnan(entry.get('Z_sh_exact', float('nan'))):
                assert entry['borel_finite']

    def test_exact_matches_partial_at_small_hbar(self):
        """Closed form matches partial sum at small hbar."""
        result = borel_comparison(1.0, [0.1, 0.5])
        for entry in result['results']:
            if entry.get('relative_error') is not None:
                assert entry['relative_error'] < 1e-8


# ============================================================================
# Class 9: Phase transition
# ============================================================================

class TestPhaseTransition:
    """Test the phase transition at c = c* ~ 6.125."""

    def test_phase_transition_location(self):
        """c* is near 6.125."""
        result = phase_transition_scan()
        assert abs(result['c_star'] - 6.125) < 0.01

    def test_divergent_below_c_star(self):
        """All c < c* have phase = 'divergent'."""
        result = phase_transition_scan([0.5, 1.0, 2.0, 4.0, 5.0])
        for entry in result['scan']:
            assert entry['phase'] == 'divergent', \
                f"c={entry['c']}: expected divergent, got {entry['phase']}"

    def test_convergent_above_c_star(self):
        """All c > c* have phase = 'convergent'."""
        result = phase_transition_scan([7.0, 10.0, 13.0, 26.0])
        for entry in result['scan']:
            assert entry['phase'] == 'convergent', \
                f"c={entry['c']}: expected convergent, got {entry['phase']}"

    def test_marginal_at_c_star(self):
        """At c = c*, the phase is marginal (rho = 1)."""
        c_star = critical_central_charge()
        result = phase_transition_scan([c_star])
        entry = result['scan'][0]
        assert entry['phase'] == 'marginal'

    def test_all_unitary_minimal_models_divergent(self):
        """Unitary minimal models (c < 1) have rho > 1."""
        # c = 1/2 (Ising), c = 7/10 (tri-critical Ising), c = 4/5 (3-state Potts)
        for c_val in [0.5, 0.7, 0.8]:
            rho = virasoro_rho(c_val)
            assert rho > 1.0, f"c={c_val}: rho={rho} should be > 1"


# ============================================================================
# Class 10: Analytic continuation
# ============================================================================

class TestAnalyticContinuation:
    """Test analytic continuation to complex hbar."""

    def test_complex_hbar_inside_disc(self):
        """Z^sh at complex hbar inside disc is finite and consistent."""
        results = analytic_continuation_complex_hbar(1.0, [1.0 + 1.0j, 0.5 - 0.5j])
        for entry in results:
            assert entry['inside_disc']
            assert entry['finite']
            # Closed form and partial sum should agree
            assert entry['relative_error'] < 1e-6

    def test_purely_imaginary_hbar(self):
        """At hbar = 2i (purely imaginary), Z^sh is finite."""
        results = analytic_continuation_complex_hbar(1.0, [2.0j])
        assert results[0]['finite']
        assert results[0]['inside_disc']

    def test_negative_real_hbar(self):
        """At hbar = -1 (negative real), Z^sh is finite."""
        results = analytic_continuation_complex_hbar(1.0, [-1.0 + 0j])
        assert results[0]['finite']
        assert results[0]['inside_disc']

    def test_symmetry_conjugate(self):
        """Z^sh(conj(hbar)) = conj(Z^sh(hbar)) since kappa is real."""
        kappa = 1.0
        hbar = 1.0 + 2.0j
        results = analytic_continuation_complex_hbar(kappa, [hbar, hbar.conjugate()])
        Z1 = results[0]['Z_closed']
        Z2 = results[1]['Z_closed']
        assert abs(Z1.conjugate() - Z2) < 1e-10

    def test_even_function(self):
        """Z^sh(hbar) = Z^sh(-hbar) (even function of hbar)."""
        kappa = 1.0
        hbar = 1.5 + 0.5j
        results = analytic_continuation_complex_hbar(kappa, [hbar, -hbar])
        Z_plus = results[0]['Z_closed']
        Z_minus = results[1]['Z_closed']
        assert abs(Z_plus - Z_minus) < 1e-10


# ============================================================================
# Class 11: Lorentzian evaluation
# ============================================================================

class TestLorentzian:
    """Test Lorentzian (imaginary hbar) evaluation."""

    def test_lorentzian_is_real(self):
        """Z^sh(i*beta) is real for all real beta."""
        results = lorentzian_evaluation(1.0)
        for entry in results:
            assert entry['is_real']

    def test_lorentzian_finite_for_all_beta(self):
        """Z^sh(i*beta) is finite for all real beta > 0."""
        results = lorentzian_evaluation(1.0, [0.1, 1.0, 10.0, 100.0])
        for entry in results:
            assert entry['is_finite']

    def test_lorentzian_negative_for_positive_kappa(self):
        """Z^sh(i*beta) < 0 for kappa > 0 and beta > 0.

        Since (beta/2)/sinh(beta/2) < 1 for beta > 0,
        and kappa > 0, we get kappa * (f(beta) - 1) < 0.
        """
        results = lorentzian_evaluation(1.0, [0.1, 1.0, 5.0, 10.0])
        for entry in results:
            assert entry['sign'] == 'negative'

    def test_lorentzian_approaches_minus_kappa_at_large_beta(self):
        """Z^sh(i*beta) -> -kappa as beta -> infinity.

        (beta/2)/sinh(beta/2) -> 0, so Z^sh -> kappa*(0 - 1) = -kappa.
        """
        results = lorentzian_evaluation(1.0, [100.0, 1000.0])
        for entry in results:
            assert abs(entry['Z_sh'] - (-1.0)) < 0.01


# ============================================================================
# Class 12: Koszul duality comparison
# ============================================================================

class TestKoszulDuality:
    """Test Koszul duality and convergence."""

    def test_kappa_sum_equals_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            result = koszul_convergence_comparison(c_val)
            assert abs(result['kappa_sum'] - 13.0) < 1e-10

    def test_self_dual_at_c13(self):
        """rho(13) = rho(13): self-dual."""
        result = koszul_convergence_comparison(13.0)
        assert result['self_dual']
        assert abs(result['rho'] - result['rho_dual']) < 1e-10

    def test_not_self_dual_away_from_c13(self):
        """rho(c) != rho(26-c) for c != 13."""
        for c_val in [1.0, 5.0, 20.0, 25.0]:
            result = koszul_convergence_comparison(c_val)
            assert not result['self_dual']
            assert abs(result['rho'] - result['rho_dual']) > 0.01

    def test_rho_product_not_constant(self):
        """rho(c) * rho(26-c) is NOT constant (not reciprocal)."""
        products = []
        for c_val in [1.0, 5.0, 10.0, 13.0, 25.0]:
            result = koszul_convergence_comparison(c_val)
            products.append(result['rho_product'])
        # Products should vary
        assert max(products) - min(products) > 0.01


# ============================================================================
# Class 13: Affine free field limit
# ============================================================================

class TestFreeFieldLimit:
    """Test sl_2 convergence as k -> infinity."""

    def test_all_class_L(self):
        """sl_2 is class L at ALL levels."""
        results = affine_sl2_free_field_limit()
        for entry in results:
            assert entry['depth_class'] == 'L'
            assert entry['rho'] == 0.0

    def test_kappa_grows_with_k(self):
        """kappa(sl_2, k) grows linearly with k.

        kappa = 3(k+2)/4 so kappa/k = 3/4 + 3/(2k) -> 3/4 as k -> inf.
        """
        results = affine_sl2_free_field_limit([1, 10, 100, 1000])
        for entry in results:
            # kappa = 3(k+2)/4 = 3k/4 + 3/2 so kappa/k = 3/4 + 3/(2k)
            expected_ratio = 0.75 + 1.5 / entry['k']
            assert abs(entry['kappa_over_k'] - expected_ratio) < 1e-10

    def test_R_arity_always_infinite(self):
        """R_arity = infinity for ALL levels (class L, rho = 0)."""
        results = affine_sl2_free_field_limit([1, 10, 100])
        for entry in results:
            assert entry['R_arity'] == float('inf')


# ============================================================================
# Class 14: Convergence tables
# ============================================================================

class TestConvergenceTables:
    """Test the master convergence tables."""

    def test_full_table_nonempty(self):
        """Full convergence table is nonempty."""
        table = full_convergence_table()
        assert len(table) > 0

    def test_full_table_all_R_genus_2pi(self):
        """All entries have R_genus = 2*pi."""
        table = full_convergence_table()
        for entry in table:
            assert abs(entry['R_genus'] - TWO_PI) < 1e-10

    def test_virasoro_scan_covers_c_star(self):
        """Virasoro scan includes c* and both phases."""
        scan = virasoro_convergence_scan()
        convergent_count = sum(1 for s in scan if s['arity_convergent'])
        divergent_count = sum(1 for s in scan if not s['arity_convergent'])
        assert convergent_count > 0
        assert divergent_count > 0


# ============================================================================
# Class 15: Double convergence bound
# ============================================================================

class TestDoubleConvergenceBound:
    """Test the analytic bound on |Z^sh|."""

    def test_polylog_at_zero(self):
        """Li_{5/2}(0) = 0."""
        assert abs(polylogarithm_5_2(0.0)) < 1e-14

    def test_polylog_at_half(self):
        """Li_{5/2}(1/2) ~ 0.508..."""
        val = polylogarithm_5_2(0.5)
        assert 0.5 < val < 0.6

    def test_polylog_diverges_above_1(self):
        """Li_{5/2}(rho) = infinity for rho > 1."""
        assert polylogarithm_5_2(1.5) == float('inf')

    def test_bound_positive(self):
        """The double convergence bound is positive for kappa > 0."""
        result = double_convergence_bound(1.0, 0.5)
        assert result['bound'] > 0
        assert result['convergent']

    def test_bound_divergent_at_rho_gt_1(self):
        """The bound is not finite for rho > 1."""
        result = double_convergence_bound(1.0, 1.5)
        assert not result['convergent']

    def test_bound_zero_rho_finite(self):
        """For class G/L (rho = 0): bound is finite."""
        result = double_convergence_bound(1.0, 0.0)
        assert result['convergent']
        assert result['bound'] > 0
        assert math.isfinite(result['bound'])


# ============================================================================
# Class 16: Bernoulli decay
# ============================================================================

class TestBernoulliDecay:
    """Test the Bernoulli decay of lambda_g^FP."""

    def test_decay_ratio_approaches_target(self):
        """lambda_g^FP / (2/(2*pi)^{2g}) -> 1."""
        data = bernoulli_decay_table(20)
        # At g=20 the ratio should be very close to 1
        assert abs(data[-1]['ratio'] - 1.0) < 0.01

    def test_genus_ratio_approaches_target(self):
        """lambda_{g+1}/lambda_g -> 1/(2*pi)^2 ~ 0.0253."""
        data = genus_ratio_table(20)
        target = 1.0 / TWO_PI_SQ
        # At g=20, the ratio should be very close
        assert abs(data[-1]['ratio'] - target) / target < 0.01

    def test_bernoulli_table_positive(self):
        """All lambda_g^FP > 0."""
        data = bernoulli_decay_table(15)
        for entry in data:
            assert entry['lambda_fp'] > 0

    def test_bernoulli_table_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        data = bernoulli_decay_table(15)
        for i in range(1, len(data)):
            assert data[i]['lambda_fp'] < data[i - 1]['lambda_fp']


# ============================================================================
# Class 17: Cross-family consistency checks (AP10)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks to catch AP10 violations.

    These are structural checks that hold universally, not just for
    individual families.  They catch hardcoded-wrong-expected-value bugs.
    """

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_{n1} + H_{n2}) = kappa(H_{n1}) + kappa(H_{n2}).

        Independent sum factorization (prop:independent-sum-factorization).
        """
        for n1 in [1, 2, 4]:
            for n2 in [1, 3, 8]:
                assert abs(kappa_heisenberg(n1 + n2)
                           - kappa_heisenberg(n1) - kappa_heisenberg(n2)) < 1e-14

    def test_rho_zero_implies_infinite_R_arity(self):
        """rho = 0 => R_arity = infinity, for every family in the atlas."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if data.rho == 0.0:
                assert data.R_arity == float('inf'), \
                    f"{key}: rho=0 but R_arity={data.R_arity}"

    def test_R_arity_is_reciprocal_of_rho(self):
        """R_arity = 1/rho for all class M families."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if data.depth_class == 'M' and data.rho > 0:
                assert abs(data.R_arity - 1.0 / data.rho) < 1e-10, \
                    f"{key}: R_arity={data.R_arity} != 1/rho=1/{data.rho}"

    def test_genus_convergence_independent_of_family(self):
        """R_genus = 2*pi for every single family."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            assert abs(data.R_genus - TWO_PI) < 1e-10, \
                f"{key}: R_genus={data.R_genus}"

    def test_virasoro_kappa_equals_c_over_2(self):
        """kappa(Vir_c) = c/2 for all c in the atlas."""
        atlas = shadow_growth_rate_atlas()
        for key, data in atlas.items():
            if key.startswith('Vir_c=') and 'c' in data.parameters:
                c_val = data.parameters['c']
                assert abs(data.kappa - c_val / 2.0) < 1e-10, \
                    f"{key}: kappa={data.kappa} != c/2={c_val/2}"

    def test_virasoro_rho_at_c_star_is_one(self):
        """rho(Vir_{c*}) = 1 exactly."""
        c_star = critical_central_charge()
        rho = virasoro_rho(c_star)
        assert abs(rho - 1.0) < 1e-6


# ============================================================================
# Class 18: Specific numerical values (independent verification)
# ============================================================================

class TestSpecificNumericalValues:
    """Verify specific numerical values from independent computation.

    These are computed from first principles, not copied from the atlas.
    """

    def test_virasoro_rho_c26_exact(self):
        """rho^2(Vir_{c=26}) = (180*26 + 872)/((5*26+22)*26^2)
        = (4680 + 872) / (152 * 676) = 5552 / 102752."""
        rho_sq = 5552.0 / 102752.0
        assert abs(virasoro_rho_squared(26.0) - rho_sq) < 1e-12
        assert abs(virasoro_rho(26.0) - math.sqrt(rho_sq)) < 1e-10

    def test_virasoro_rho_c13_exact(self):
        """rho^2(Vir_{c=13}) = (180*13 + 872)/((5*13+22)*13^2)
        = (2340 + 872) / (87 * 169) = 3212 / 14703."""
        rho_sq = 3212.0 / 14703.0
        assert abs(virasoro_rho_squared(13.0) - rho_sq) < 1e-12

    def test_w3_wline_rho_c50_exact(self):
        """rho_W^2(W_3, c=50) = 30720 / (50^2 * (5*50+22)^3)
        = 30720 / (2500 * 272^3)."""
        rho_sq = 30720.0 / (2500.0 * 272.0 ** 3)
        assert abs(w3_wline_rho_squared(50.0) - rho_sq) < 1e-12

    def test_kappa_E8_k1_exact(self):
        """kappa(E_8, k=1) = 248 * (1+30) / (2*30) = 248*31/60 = 7688/60."""
        expected = 7688.0 / 60.0
        assert abs(kappa_affine_general(248, 1, 30) - expected) < 1e-10

    def test_kappa_sl2_k1_exact(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert abs(kappa_affine_sl2(1) - 2.25) < 1e-14

    def test_F1_heisenberg_rank1(self):
        """F_1(Heisenberg, rank 1) = (1/2)/24 = 1/48."""
        assert abs(kappa_heisenberg(1) / 24.0 - 1.0 / 48.0) < 1e-14

    def test_genus_series_at_hbar_1(self):
        """Closed form at hbar=1: kappa * (0.5/sin(0.5) - 1)."""
        kappa = 1.0
        expected = kappa * (0.5 / math.sin(0.5) - 1.0)
        assert abs(genus_series_closed_form(kappa, 1.0) - expected) < 1e-14

    def test_critical_cubic_polynomial(self):
        """5*c*^3 + 22*c*^2 - 180*c* - 872 = 0 at c*."""
        c_star = critical_central_charge()
        poly_val = 5 * c_star ** 3 + 22 * c_star ** 2 - 180 * c_star - 872
        assert abs(poly_val) < 1e-6
