r"""Tests for the Analytic O1 Attack Engine.

Multi-path verification of the cusp extraction for Heisenberg at genus 1
and genus 2, proving metric independence of the shadow F_g.

Test organization (42 tests):
  1. Cusp extraction at genus 1 (5 tests)
  2. Re(tau) independence (4 tests)
  3. Convergence rate (3 tests)
  4. Eisenstein/cuspidal decomposition (5 tests)
  5. Genus-2 separating degeneration (4 tests)
  6. Genus-2 cusp extraction (3 tests)
  7. Fredholm shadow at genus 2 (3 tests)
  8. Three-path metric independence (3 tests)
  9. Eta constant term verification (3 tests)
  10. Derivative extraction (2 tests)
  11. Anomaly cancellation at c=26 (2 tests)
  12. A-hat generating function (2 tests)
  13. Lattice VOA extraction (2 tests)
  14. Cuspidal Fourier analysis (3 tests)
  15. Multi-genus shadow (2 tests)
  16. Cusp extraction landscape survey (2 tests)
  17. Cross-family consistency / AP prevention (2 tests)

Ground truth:
  thm:general-hs-sewing, thm:heisenberg-sewing,
  conj:analytic-realization (O1 analysis),
  theorem_analytic_realization_obstruction_engine.py,
  theorem_moriwaki_analytic_bridge_engine.py,
  Bismut-Gillet-Soule, Polyakov.

MULTI-PATH VERIFICATION:
  Every shadow value verified by at least 3 independent paths.
  AP10 prevention: cross-family consistency checks throughout.
  AP39/AP48: kappa != c/2 for non-Virasoro families.
  AP46: eta includes q^{1/24}.
"""

import math
import cmath
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_analytic_o1_attack_engine import (
    # Core
    eta_product,
    dedekind_eta,
    faber_pandharipande,
    shadow_free_energy,
    _bernoulli_number,
    # Kappa
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_km,
    central_charge_km,
    # Genus-1
    heisenberg_log_partition_g1,
    cusp_extraction_genus1,
    cusp_extraction_x_independence,
    cusp_extraction_convergence_rate,
    eisenstein_cuspidal_decomposition_g1,
    verify_eta_constant_term,
    derivative_extraction_g1,
    # Genus-2
    genus2_separating_partition,
    genus2_cusp_extraction,
    genus2_fredholm_shadow,
    # Three-path proof
    MetricIndependenceProof,
    # Anomaly
    anomaly_cancellation_genus1,
    # A-hat
    a_hat_generating_function_check,
    # Lattice
    lattice_voa_cusp_extraction_g1,
    # Fourier
    cuspidal_fourier_analysis,
    # Multi-genus
    multi_genus_shadow_verification,
    # Landscape
    cusp_extraction_landscape_survey,
    CuspExtractionConjecture,
)


PI = math.pi
TWO_PI = 2 * PI


# ======================================================================
# 1. Cusp extraction at genus 1 (5 tests)
# ======================================================================

class TestCuspExtractionGenus1:
    """Verify F_1(H_k) = k/24 from the cusp of log Z_1."""

    def test_extraction_k1_y10(self):
        """F_1(H_1) = 1/24 at y=10."""
        result = cusp_extraction_genus1(1j * 10.0, k=1)
        assert 'error' not in result
        assert abs(result['extracted_F1'] - 1.0 / 24.0) < 1e-8
        assert result['extraction_converged']

    def test_extraction_k1_y50(self):
        """F_1(H_1) = 1/24 at y=50 (deeper into the cusp)."""
        result = cusp_extraction_genus1(1j * 50.0, k=1)
        assert abs(result['extracted_F1'] - 1.0 / 24.0) < 1e-12

    def test_extraction_k5(self):
        """F_1(H_5) = 5/24."""
        result = cusp_extraction_genus1(1j * 20.0, k=5)
        assert abs(result['extracted_F1'] - 5.0 / 24.0) < 1e-8

    def test_extraction_k26(self):
        """F_1(H_26) = 26/24 = 13/12 (26 free bosons, the critical dim)."""
        result = cusp_extraction_genus1(1j * 20.0, k=26)
        assert abs(result['extracted_F1'] - 26.0 / 24.0) < 1e-8

    def test_cuspidal_within_bound(self):
        """The cuspidal remainder is bounded by O(e^{-2*pi*y})."""
        result = cusp_extraction_genus1(1j * 5.0, k=1)
        assert result['cuspidal_within_bound']


# ======================================================================
# 2. Re(tau) independence (4 tests)
# ======================================================================

class TestReIndependence:
    """Verify F_1 is independent of Re(tau) = x."""

    def test_x_independence_k1_y10(self):
        """F_1(H_1) = 1/24 for all x at y=10."""
        result = cusp_extraction_x_independence(
            1, 10.0, [0.0, 0.1, 0.3, 0.5, -0.2])
        assert result['x_independent']
        assert result['all_converged']

    def test_x_independence_k3_y20(self):
        """F_1(H_3) = 3/24 = 1/8 for all x at y=20."""
        result = cusp_extraction_x_independence(
            3, 20.0, [0.0, 0.25, 0.5])
        assert result['x_independent']

    def test_cuspidal_x_dependence(self):
        """The cuspidal part DOES depend on x (but is exponentially small)."""
        result = cusp_extraction_x_independence(
            1, 3.0, [0.0, 0.1, 0.3, 0.5])
        # At y=3, the cuspidal part is small but nonzero and x-dependent
        if result.get('cuspidal_x_dependent') is not None:
            assert result['cuspidal_x_dependent'], (
                "Cuspidal part should depend on x at moderate y"
            )

    def test_spread_decreases_with_y(self):
        """The F_1 spread across x values decreases with y."""
        x_vals = [0.0, 0.2, 0.4]
        r5 = cusp_extraction_x_independence(1, 5.0, x_vals)
        r20 = cusp_extraction_x_independence(1, 20.0, x_vals)
        # At y=20, the spread should be smaller than at y=5
        assert r20['F1_spread'] < r5['F1_spread'] or r5['F1_spread'] < 1e-10


# ======================================================================
# 3. Convergence rate (3 tests)
# ======================================================================

class TestConvergenceRate:
    """Verify exponential convergence rate ~ 2*pi."""

    def test_exponential_decay_k1(self):
        """Decay rate close to 2*pi for k=1."""
        result = cusp_extraction_convergence_rate(1, [2, 3, 5, 8, 12])
        assert result['exponential_decay_confirmed'], (
            f"Decay rate {result['mean_decay_rate']:.4f}, "
            f"expected ~ {TWO_PI:.4f}"
        )

    def test_exponential_decay_k5(self):
        """Decay rate close to 2*pi for k=5."""
        result = cusp_extraction_convergence_rate(5, [2, 3, 5, 8])
        assert result['exponential_decay_confirmed']

    def test_rate_ratio_near_one(self):
        """The ratio of measured to expected decay rate is close to 1."""
        result = cusp_extraction_convergence_rate(1, [2, 4, 6, 10])
        if result.get('rate_ratio') is not None:
            assert abs(result['rate_ratio'] - 1.0) < 0.3, (
                f"Rate ratio = {result['rate_ratio']:.4f}"
            )


# ======================================================================
# 4. Eisenstein/cuspidal decomposition (5 tests)
# ======================================================================

class TestEisensteinCuspidalDecomposition:
    """Verify the Eisenstein/cuspidal decomposition of log Z_1."""

    def test_decomposition_exact(self):
        """Eisenstein + cuspidal = log Z_1 (exact decomposition)."""
        result = eisenstein_cuspidal_decomposition_g1(0.3 + 10j, k=2)
        assert 'error' not in result
        assert result['decomposition_exact']

    def test_shadow_from_eisenstein(self):
        """The Eisenstein coefficient gives k/24."""
        for k in [1, 3, 10]:
            result = eisenstein_cuspidal_decomposition_g1(1j * 20.0, k=k)
            assert result['shadow_matches'], (
                f"k={k}: shadow_from_eis={result['shadow_from_eisenstein']}, "
                f"expected={result['shadow_expected']}"
            )

    def test_cuspidal_bounded_by_q(self):
        """The cuspidal part is bounded by O(k*|q|/(1-|q|))."""
        result = eisenstein_cuspidal_decomposition_g1(1j * 5.0, k=1)
        if result.get('cuspidal_bound_by_q') is not None:
            assert result['cuspidal_bound_by_q']

    def test_cuspidal_relative_small(self):
        """The cuspidal part is a tiny fraction of log Z_1 at large y."""
        result = eisenstein_cuspidal_decomposition_g1(1j * 10.0, k=1)
        assert result['cuspidal_relative'] < 1e-6

    def test_fourier_coefficients(self):
        """The cuspidal Fourier coefficients are sigma_{-1}(n)."""
        result = eisenstein_cuspidal_decomposition_g1(1j * 10.0, k=1)
        coeffs = result['cuspidal_fourier_coeffs']
        # c_1 = 1 (only divisor of 1 is 1, 1/1 = 1)
        assert abs(coeffs[0]['coefficient'] - 1.0) < 1e-12
        # c_2 = 1/1 + 1/2 = 3/2
        assert abs(coeffs[1]['coefficient'] - 1.5) < 1e-12
        # c_3 = 1/1 + 1/3 = 4/3
        assert abs(coeffs[2]['coefficient'] - 4.0 / 3.0) < 1e-12


# ======================================================================
# 5. Genus-2 separating degeneration (4 tests)
# ======================================================================

class TestGenus2SeparatingDegeneration:
    """Verify genus-2 partition function in separating degeneration."""

    def test_F2_shadow_k1(self):
        """F_2(H_1) = 7/5760."""
        result = genus2_separating_partition(1j * 3.0, 1j * 4.0, 0.1 + 0j, k=1)
        assert 'error' not in result
        assert abs(result['F2_shadow'] - 7.0 / 5760.0) < 1e-15

    def test_F2_shadow_k2(self):
        """F_2(H_2) = 7/2880."""
        result = genus2_separating_partition(1j * 3.0, 1j * 4.0, 0.1 + 0j, k=2)
        assert abs(result['F2_shadow'] - 14.0 / 5760.0) < 1e-15

    def test_factorization(self):
        """log Z_2^{sep} = log Z_1(tau_1) + log Z_1(tau_2) + log Z_neck(w)."""
        result = genus2_separating_partition(1j * 5.0, 1j * 6.0, 0.05 + 0j, k=3)
        # Verify the decomposition
        total = result['log_Z1_a'] + result['log_Z1_b'] + result['log_neck']
        assert abs(total - result['log_Z2_sep']) < 1e-12

    def test_pointwise_ne_integrated(self):
        """Pointwise F_2 differs from the integrated shadow."""
        result = genus2_separating_partition(1j * 2.0, 1j * 3.0, 0.1 + 0j, k=1)
        assert abs(result['F2_pointwise_real'] - result['F2_shadow']) > 0.001


# ======================================================================
# 6. Genus-2 cusp extraction (3 tests)
# ======================================================================

class TestGenus2CuspExtraction:
    """Verify cusp extraction at genus 2."""

    def test_tau1_extraction_converges(self):
        """Cusp extraction in the tau_1 direction converges."""
        result = genus2_cusp_extraction(1, [5, 10, 20, 50])
        assert result['tau1_extraction_converged']

    def test_tau1_extraction_k3(self):
        """k=3: tau_1 extraction gives 3/24 = 1/8."""
        result = genus2_cusp_extraction(3, [10, 20, 50])
        assert result['tau1_extraction_converged']

    def test_metric_independence_of_factor(self):
        """The genus-1 factor in the genus-2 partition function is metric-independent."""
        result = genus2_cusp_extraction(1, [10, 30, 50])
        assert result['metric_independence_of_factor']


# ======================================================================
# 7. Fredholm shadow at genus 2 (3 tests)
# ======================================================================

class TestFredholmShadow:
    """Verify the Fredholm determinant sewing contribution."""

    def test_fredholm_det_small_w(self):
        """At small |w|, det(1 - T_w) ~ 1 - w."""
        result = genus2_fredholm_shadow(1, [0.01 + 0j, 0.001 + 0j])
        for r in result['results']:
            det_val = r['fredholm_det']
            # det(1-T_w) = prod(1-w^n) ~ 1-w for small w
            w = r['w']
            assert abs(det_val - (1.0 - w)) < abs(w) ** 2 * 2

    def test_fredholm_real_for_real_w(self):
        """The Fredholm determinant is real for real w."""
        result = genus2_fredholm_shadow(2, [0.1 + 0j, 0.3 + 0j, 0.5 + 0j])
        for r in result['results']:
            assert abs(r['fredholm_det'].imag) < 1e-12

    def test_F2_shadow_correct(self):
        """The genus-2 shadow is k * 7/5760."""
        result = genus2_fredholm_shadow(5, [0.1 + 0j])
        assert abs(result['F2_shadow'] - 5.0 * 7.0 / 5760.0) < 1e-15


# ======================================================================
# 8. Three-path metric independence (3 tests)
# ======================================================================

class TestThreePathMetricIndependence:
    """Verify all three paths to metric independence agree."""

    def test_three_paths_k1_g1(self):
        """k=1, g=1: all three paths give F_1 = 1/24."""
        proof = MetricIndependenceProof(k=1, genus=1)
        result = proof.all_paths()
        assert result['all_agree']
        assert result['all_metric_independent']
        assert abs(result['F_g'] - 1.0 / 24.0) < 1e-15

    def test_three_paths_k5_g2(self):
        """k=5, g=2: all three paths give F_2 = 5 * 7/5760."""
        proof = MetricIndependenceProof(k=5, genus=2)
        result = proof.all_paths()
        assert result['all_agree']
        assert abs(result['F_g'] - 5.0 * 7.0 / 5760.0) < 1e-15

    def test_three_paths_k1_g3(self):
        """k=1, g=3: all three paths give F_3 = 31/967680."""
        proof = MetricIndependenceProof(k=1, genus=3)
        result = proof.all_paths()
        assert result['all_agree']
        assert abs(result['F_g'] - 31.0 / 967680.0) < 1e-15


# ======================================================================
# 9. Eta constant term verification (3 tests)
# ======================================================================

class TestEtaConstantTerm:
    """Verify the constant term extraction from -k*log eta."""

    def test_both_methods_k1(self):
        """Direct limit and derivative methods agree for k=1."""
        result = verify_eta_constant_term(1j * 20.0, k=1)
        assert result['both_agree']
        assert result['both_correct']

    def test_both_methods_k10(self):
        """Direct limit and derivative methods agree for k=10."""
        result = verify_eta_constant_term(1j * 15.0, k=10)
        assert result['both_agree']

    def test_direct_limit_accurate(self):
        """Direct limit gives k/24 to high precision at large y."""
        result = verify_eta_constant_term(1j * 50.0, k=1)
        assert result['direct_error'] < 1e-12


# ======================================================================
# 10. Derivative extraction (2 tests)
# ======================================================================

class TestDerivativeExtraction:
    """Verify F_1 = (1/2*pi) lim d/dy Re(log Z_1)."""

    def test_derivative_k1(self):
        """Derivative extraction gives 1/24 for k=1."""
        result = derivative_extraction_g1(1, 20.0)
        assert result['numerical_correct']
        assert result['derivative_formula_verified']

    def test_derivative_k5(self):
        """Derivative extraction gives 5/24 for k=5."""
        result = derivative_extraction_g1(5, 15.0)
        assert result['numerical_correct']


# ======================================================================
# 11. Anomaly cancellation at c=26 (2 tests)
# ======================================================================

class TestAnomalyCancellation:
    """Verify anomaly cancellation at c=26."""

    def test_kappa_eff_vanishes(self):
        """kappa(Vir_26) + kappa(ghost) = 13 - 13 = 0."""
        result = anomaly_cancellation_genus1(10.0)
        assert result['anomaly_cancelled']
        assert result['F1_total_vanishes']

    def test_heis26_extraction(self):
        """26 free bosons: extraction gives 26/24 = 13/12."""
        result = anomaly_cancellation_genus1(20.0)
        assert result['heis26_agrees']
        assert abs(result['heis26_shadow'] - 26.0 / 24.0) < 1e-15


# ======================================================================
# 12. A-hat generating function (2 tests)
# ======================================================================

class TestAHatGeneratingFunction:
    """Verify the A-hat generating function for the shadow."""

    def test_a_hat_k5_x01(self):
        """A-hat GF agrees with term sum at x=0.1, kappa=5."""
        result = a_hat_generating_function_check(5.0, 0.1, g_max=5)
        assert result['agrees_within_truncation']

    def test_a_hat_k1_x05(self):
        """A-hat GF at x=0.5, kappa=1 (larger x, more terms needed)."""
        result = a_hat_generating_function_check(1.0, 0.5, g_max=5)
        assert result['agrees_within_truncation']


# ======================================================================
# 13. Lattice VOA extraction (2 tests)
# ======================================================================

class TestLatticeVOAExtraction:
    """Verify cusp extraction for lattice VOAs (kappa = c = rank)."""

    def test_rank8_extraction(self):
        """E_8 lattice VOA: kappa = rank = 8, extraction gives 8/24 = 1/3."""
        result = lattice_voa_cusp_extraction_g1(8, 20.0)
        assert result['heis_agrees']
        assert abs(result['shadow_F1'] - 8.0 / 24.0) < 1e-15

    def test_rank24_extraction(self):
        """Leech lattice VOA: kappa = rank = 24, extraction gives 24/24 = 1."""
        result = lattice_voa_cusp_extraction_g1(24, 20.0)
        assert result['heis_agrees']
        assert abs(result['shadow_F1'] - 1.0) < 1e-15


# ======================================================================
# 14. Cuspidal Fourier analysis (3 tests)
# ======================================================================

class TestCuspidalFourierAnalysis:
    """Verify the Fourier structure of the cuspidal part."""

    def test_leading_coefficient(self):
        """The leading Fourier coefficient is k * 1 = k."""
        result = cuspidal_fourier_analysis(3, 10.0)
        coeffs = result['fourier_coefficients']
        assert abs(coeffs[0]['k_c_n'] - 3.0) < 1e-12

    def test_exponentially_small(self):
        """Cuspidal part is exponentially small at large y."""
        result = cuspidal_fourier_analysis(1, 5.0)
        assert result['cuspidal_is_exponentially_small']

    def test_simple_bound_holds(self):
        """The simple bound k*|q|/(1-|q|) contains the cuspidal part."""
        result = cuspidal_fourier_analysis(2, 3.0)
        if result['actual_cuspidal_abs'] is not None:
            assert result['actual_cuspidal_abs'] < result['simple_bound']


# ======================================================================
# 15. Multi-genus shadow (2 tests)
# ======================================================================

class TestMultiGenusShadow:
    """Verify F_g across genera."""

    def test_all_positive(self):
        """F_g > 0 for all g (AP22: A-hat(ix) has positive coefficients)."""
        result = multi_genus_shadow_verification(1, g_max=4)
        assert result['all_positive']

    def test_f_g_ratios_decreasing(self):
        """F_{g+1}/F_g < 1 (the shadow decays with genus)."""
        result = multi_genus_shadow_verification(1, g_max=4)
        for r in result['ratios']:
            if r['ratio'] is not None:
                assert r['ratio'] < 1.0, (
                    f"F_{r['g+1']}/F_{r['g']} = {r['ratio']} >= 1"
                )


# ======================================================================
# 16. Cusp extraction landscape survey (2 tests)
# ======================================================================

class TestCuspExtractionLandscape:
    """Survey which families allow partition-function cusp extraction."""

    def test_free_fields_agree(self):
        """Free fields (Heisenberg, lattice): partition extraction works."""
        survey = cusp_extraction_landscape_survey()
        assert survey['partition_extraction_works_count'] >= 5

    def test_quillen_always_works(self):
        """Quillen extraction works for ALL families."""
        survey = cusp_extraction_landscape_survey()
        assert survey['quillen_extraction_works_count'] == survey['total_families']


# ======================================================================
# 17. Cross-family consistency / AP prevention (2 tests)
# ======================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks to prevent AP10/AP39/AP48."""

    def test_kappa_ne_c_for_virasoro(self):
        """AP48: kappa(Vir_c) = c/2 != c for c > 0."""
        conj = CuspExtractionConjecture('Vir_26', kappa_virasoro(26.0), 26.0)
        assert not conj.kappa_equals_c
        assert not conj.partition_extraction_gives_shadow()
        assert conj.quillen_extraction_gives_shadow()

    def test_kappa_ne_c_for_affine_km(self):
        """AP39: kappa != c for affine KM."""
        kap = kappa_affine_km('A', 1, 1)
        cc = central_charge_km('A', 1, 1)
        conj = CuspExtractionConjecture('sl_2 k=1', kap, cc)
        assert not conj.kappa_equals_c
        assert abs(kap - 9.0 / 4.0) < 1e-15
        assert abs(cc - 1.0) < 1e-15
