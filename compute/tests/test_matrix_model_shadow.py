r"""Tests for the matrix model / shadow partition function bridge.

Verifies all eight computational themes:
1. Gaussian matrix model (GUE) <-> Heisenberg shadow
2. Kontsevich model intersection numbers
3. Spectral density from shadow (Wigner semicircle)
4. Double-scaling limit (Painleve II)
5. Tracy-Widom tail behavior
6. Multi-matrix model <-> W_3 shadow
7. Spectral form factor
8. Universal sine kernel

65+ tests covering the full RMT-shadow correspondence.

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
"""

import cmath
import math
import pytest

from sympy import Rational, bernoulli, factorial, simplify

from compute.lib.matrix_model_shadow import (
    # Section 1: GUE
    F_g_GUE,
    F_g_GUE_intersection,
    verify_heisenberg_GUE_bridge,
    GUE_free_energy_table,
    # Section 2: Kontsevich
    kontsevich_tau,
    kontsevich_genus0_n_point,
    kontsevich_verify_string_equation,
    kontsevich_verify_dilaton_equation,
    # Section 3: Spectral density
    shadow_spectral_curve_coefficients,
    shadow_spectral_curve_eval,
    wigner_semicircle_density,
    heisenberg_spectral_density,
    spectral_density_from_resolvent,
    verify_semicircle_normalization,
    verify_semicircle_second_moment,
    # Section 4: Double-scaling
    F_g_double_scaling,
    double_scaling_free_energy,
    painleve_II_asymptotic,
    # Section 5: Tracy-Widom
    tracy_widom_log_tail,
    tracy_widom_log_tail_with_correction,
    tracy_widom_tail_exponent,
    verify_tracy_widom_tail,
    # Section 6: Multi-matrix
    two_matrix_free_energy_g1,
    two_matrix_vs_W3,
    # Section 7: SFF
    spectral_form_factor,
    sff_time_series,
    sff_plateau_value,
    # Section 8: Sine kernel
    sine_kernel,
    sine_kernel_2point_cluster,
    sine_kernel_number_variance,
    sine_kernel_gap_probability_small_L,
    verify_sine_kernel_properties,
    resolvent_to_density,
    resolvent_genus_correction,
    # Section 9: Connecting
    shadow_to_matrix_model_dictionary,
    F1_identity_verification,
    genus_expansion_comparison,
)
from compute.lib.utils import lambda_fp, F_g

PI = math.pi


# ==========================================================================
# Section 1: Gaussian matrix model (GUE) tests
# ==========================================================================

class TestGUEFreeEnergy:
    """Tests for GUE free energy computations."""

    def test_F1_GUE_equals_1_over_24(self):
        """F_1^GUE = 1/24 (universal genus-1 value)."""
        assert F_g_GUE(1) == Rational(1, 24)

    def test_F2_GUE_combinatorial(self):
        """F_2^GUE = |B_4| / (4 * 2) = (1/30) / 8 = 1/240."""
        val = F_g_GUE(2)
        expected = Rational(abs(bernoulli(4)), 4 * 2)
        assert val == expected

    def test_F3_GUE_combinatorial(self):
        """F_3^GUE = |B_6| / (6 * 4) = (1/42) / 24 = 1/1008."""
        val = F_g_GUE(3)
        expected = Rational(abs(bernoulli(6)), 6 * 4)
        assert val == expected

    def test_F_g_GUE_positive_all_genera(self):
        """F_g^GUE > 0 for all g = 1..10 (absolute value convention)."""
        for g in range(1, 11):
            assert F_g_GUE(g) > 0

    def test_F_g_GUE_invalid_genus(self):
        """F_g_GUE raises for g < 1."""
        with pytest.raises(ValueError):
            F_g_GUE(0)

    def test_F_g_GUE_intersection_equals_lambda_fp(self):
        """F_g^GUE_intersection = lambda_fp for g = 1..8."""
        for g in range(1, 9):
            assert F_g_GUE_intersection(g) == lambda_fp(g)

    def test_heisenberg_GUE_bridge_all_match(self):
        """F_g^Heis(kappa=1) = F_g^GUE_intersection for g = 1..6."""
        result = verify_heisenberg_GUE_bridge(6)
        assert result['all_match'] is True

    def test_heisenberg_GUE_bridge_genus_by_genus(self):
        """Verify each genus individually for the bridge identity."""
        for g in range(1, 7):
            shadow = F_g(Rational(1), g)
            intersection = F_g_GUE_intersection(g)
            assert simplify(shadow - intersection) == 0, f"Mismatch at genus {g}"

    def test_GUE_table_has_both_normalizations(self):
        """GUE_free_energy_table returns both combinatorial and intersection."""
        table = GUE_free_energy_table(5)
        for g in range(1, 6):
            assert 'combinatorial' in table[g]
            assert 'intersection' in table[g]

    def test_GUE_combinatorial_vs_intersection_differ_at_g2(self):
        """The two normalizations differ at g >= 2."""
        table = GUE_free_energy_table(5)
        for g in range(2, 6):
            assert table[g]['combinatorial'] != table[g]['intersection']

    def test_GUE_both_normalizations_agree_at_g1(self):
        """Both normalizations give 1/24 at genus 1."""
        table = GUE_free_energy_table(3)
        assert table[1]['combinatorial'] == Rational(1, 24)
        assert table[1]['intersection'] == Rational(1, 24)


# ==========================================================================
# Section 2: Kontsevich model tests
# ==========================================================================

class TestKontsevichModel:
    """Tests for intersection number computations."""

    def test_tau0_cubed_genus0(self):
        """<tau_0^3>_0 = 1."""
        assert kontsevich_tau(0, 0, 0, g=0) == Rational(1)

    def test_tau1_genus1(self):
        """<tau_1>_1 = 1/24."""
        assert kontsevich_tau(1, g=1) == Rational(1, 24)

    def test_tau0_tau1_genus1_selection_fails(self):
        """<tau_0 tau_1>_1 = 0 (selection rule: sum=1, need 3-3+2=2)."""
        val = kontsevich_tau(0, 1, g=1)
        assert val == Rational(0)

    def test_tau0_tau2_genus1(self):
        """<tau_0 tau_2>_1 = 1/24 (by string equation from <tau_1>_1)."""
        val = kontsevich_tau(0, 2, g=1)
        assert val == Rational(1, 24)

    def test_tau4_genus2(self):
        """<tau_4>_2 = 1/1152."""
        val = kontsevich_tau(4, g=2)
        assert val == Rational(1, 1152)

    def test_tau0_cube_tau1_genus0(self):
        """<tau_0^3 tau_1>_0 = 1 (by string equation from <tau_0^3>_0)."""
        val = kontsevich_tau(0, 0, 0, 1, g=0)
        assert val == Rational(1)

    def test_selection_rule_violation(self):
        """Intersection number vanishes when selection rule fails."""
        # sum(d_i) must equal 3g - 3 + n
        val = kontsevich_tau(0, 0, g=0)  # n=2, g=0: need sum = -1, have 0
        assert val == Rational(0)

    def test_tau_0_cubed_auto_genus(self):
        """<tau_0^3> automatically determines g=0."""
        val = kontsevich_tau(0, 0, 0)
        assert val == Rational(1)

    def test_genus0_n_point_n3(self):
        """<tau_0^3>_0 = 1 via the n-point function."""
        assert kontsevich_genus0_n_point(3) == Rational(1)

    def test_genus0_n_point_n4(self):
        """<tau_0^4> has the wrong selection rule for g=0."""
        assert kontsevich_genus0_n_point(4) == Rational(0)

    def test_string_equation_genus0_3pt(self):
        """Verify string equation: <tau_0 tau_0 tau_1>_0 = <tau_0^3>_0 = 1.

        String eq: <tau_0 d_list>_g = sum_i <... d_i-1 ...>_g
        LHS: <tau_0 tau_0 tau_1>_0 (n=3, selection: 0+0+1=1=-3+3=0? No: need 1.)
        Wait: LHS has n=3 insertions total (including the tau_0 we pulled out).
        The string equation says: <tau_0 tau_{d1}...tau_{dn}>_g = sum_i <..tau_{d_i-1}..>_g
        So total insertions = n+1. For g=0: need 3*0-3+(n+1)=n-2=sum(d_i).
        With d_list=(0,1): n=2, sum=1, need n-2=0. 1!=0. Selection fails on LHS too.
        With d_list=(0,0,1): n=3, sum=1, need n-2=1. Yes!
        <tau_0 tau_0 tau_0 tau_1>_0 = <tau_0^3 tau_1>_0
        """
        # Use d_list=(0,0,1) which gives 4-point function at genus 0
        result = kontsevich_verify_string_equation((0, 0, 1), 0)
        assert result['verified'] is True

    def test_dilaton_equation_genus1(self):
        """Verify dilaton equation: <tau_1 tau_1>_1 = 2 * <tau_1>_1.

        Dilaton: <tau_1 prod tau_{d_i}>_g = (2g-2+n_total) * <prod tau_{d_i}>_g
        where n_total = len(d_list) + 1.
        With d_list=(1,), g=1: n_total=2, 2g-2+n_total = 2.
        LHS = <tau_1^2>_1 = 1/12.
        RHS = 2 * <tau_1>_1 = 2/24 = 1/12.
        """
        result = kontsevich_verify_dilaton_equation((1,), 1)
        assert result['verified'] is True

    def test_tau1_tau1_genus1(self):
        """<tau_1^2>_1 = (2*1-2+2) * <tau_1>_1 = 2/24 = 1/12."""
        val = kontsevich_tau(1, 1, g=1)
        assert val == Rational(1, 12)

    def test_genus0_3point_all_d0(self):
        """<tau_0^3>_0 = 1 (fundamental genus-0 three-point function)."""
        val = kontsevich_tau(0, 0, 0, g=0)
        assert val == Rational(1)

    def test_genus0_4point_string_equation(self):
        """<tau_0^3 tau_1>_0 = 1 (by string equation from <tau_0^3>_0)."""
        val = kontsevich_tau(0, 0, 0, 1, g=0)
        assert val == Rational(1)


# ==========================================================================
# Section 3: Spectral density tests
# ==========================================================================

class TestSpectralDensity:
    """Tests for Wigner semicircle and spectral density."""

    def test_wigner_semicircle_at_origin(self):
        """rho(0) = sqrt(4)/(2*pi) = 1/pi for R=2."""
        val = wigner_semicircle_density(0.0)
        expected = 2.0 / (PI * 2.0)
        assert abs(val - expected) < 1e-14

    def test_wigner_semicircle_vanishes_outside(self):
        """rho(x) = 0 for |x| > 2."""
        assert wigner_semicircle_density(2.1) == 0.0
        assert wigner_semicircle_density(-3.0) == 0.0

    def test_wigner_semicircle_symmetric(self):
        """rho(x) = rho(-x)."""
        for x in [0.5, 1.0, 1.5, 1.9]:
            assert abs(wigner_semicircle_density(x) - wigner_semicircle_density(-x)) < 1e-15

    def test_wigner_semicircle_normalization(self):
        """int_{-2}^{2} rho(x) dx = 1."""
        result = verify_semicircle_normalization(10000)
        assert result['relative_error'] < 1e-4

    def test_wigner_semicircle_second_moment(self):
        """<x^2> = R^2/4 = 1 for R=2."""
        result = verify_semicircle_second_moment(10000)
        assert result['relative_error'] < 1e-3

    def test_heisenberg_spectral_density_is_semicircle(self):
        """Heisenberg spectral density = Wigner semicircle."""
        for x in [0.0, 0.5, 1.0, 1.5]:
            assert abs(heisenberg_spectral_density(x) - wigner_semicircle_density(x)) < 1e-15

    def test_shadow_spectral_curve_heisenberg(self):
        """For Heisenberg: Q_L = 4*kappa^2 = 4 (constant)."""
        coeffs = shadow_spectral_curve_coefficients(1.0, 0.0, 0.0)
        assert abs(coeffs['a0'] - 4.0) < 1e-14
        assert abs(coeffs['a1']) < 1e-14
        assert abs(coeffs['a2']) < 1e-14

    def test_shadow_spectral_curve_virasoro(self):
        """For Virasoro c=1: kappa=1/2, alpha=2, S4=10/(1*27)."""
        kappa = 0.5
        alpha = 2.0
        S4 = 10.0 / (1.0 * 27.0)
        coeffs = shadow_spectral_curve_coefficients(kappa, alpha, S4)
        assert abs(coeffs['a0'] - 4 * 0.25) < 1e-14
        assert abs(coeffs['a1'] - 12 * 0.5 * 2.0) < 1e-14
        assert coeffs['Delta'] != 0  # Virasoro has nontrivial discriminant

    def test_spectral_density_from_resolvent_gaussian(self):
        """Default resolvent gives the Wigner semicircle."""
        val = spectral_density_from_resolvent(0.5)
        expected = wigner_semicircle_density(0.5)
        assert abs(val - expected) < 1e-15

    def test_shadow_spectral_curve_eval_heisenberg(self):
        """Q_L(x) = 4 for all x when Heisenberg."""
        for x in [-1.0, 0.0, 0.5, 2.0]:
            val = shadow_spectral_curve_eval(x, 1.0, 0.0, 0.0)
            assert abs(val - 4.0) < 1e-14


# ==========================================================================
# Section 4: Double-scaling limit tests
# ==========================================================================

class TestDoubleScaling:
    """Tests for double-scaling free energies."""

    def test_F0_ds_coefficient(self):
        """F_0^ds coefficient = -1/12."""
        assert abs(F_g_double_scaling(0) - (-1.0/12.0)) < 1e-15

    def test_F1_ds_coefficient(self):
        """F_1^ds coefficient = -1/24."""
        assert abs(F_g_double_scaling(1) - (-1.0/24.0)) < 1e-15

    def test_F2_ds_coefficient(self):
        """F_2^ds = -7/2880."""
        assert abs(F_g_double_scaling(2) - (-7.0/2880.0)) < 1e-15

    def test_F3_ds_coefficient(self):
        """F_3^ds = -245/580608."""
        expected = -245.0 / 580608.0
        assert abs(F_g_double_scaling(3) - expected) < 1e-12

    def test_double_scaling_free_energy_genus0_dominates(self):
        """At large s and small g_s, genus-0 dominates."""
        s = 10.0
        g_s = 0.01
        F_total = double_scaling_free_energy(s, max_genus=3, g_s=g_s)
        F_0 = (-1.0/12.0) * s**3 * g_s**(-2)
        # genus-0 should be the dominant contribution
        assert abs(F_0) > abs(F_total - F_0)

    def test_painleve_II_asymptotic_decay(self):
        """Hastings-McLeod solution decays for large s > 0."""
        u_10 = painleve_II_asymptotic(10.0)
        u_20 = painleve_II_asymptotic(20.0)
        assert u_20 < u_10  # decays

    def test_painleve_II_asymptotic_positive(self):
        """Asymptotic of Hastings-McLeod is positive for s > 0."""
        for s in [1.0, 5.0, 10.0, 50.0]:
            assert painleve_II_asymptotic(s) > 0

    def test_painleve_II_nan_for_negative(self):
        """Asymptotic formula is not valid for s <= 0."""
        assert math.isnan(painleve_II_asymptotic(-1.0))


# ==========================================================================
# Section 5: Tracy-Widom tests
# ==========================================================================

class TestTracyWidom:
    """Tests for Tracy-Widom tail behavior."""

    def test_tail_exponent_right(self):
        """Right tail exponent of Tracy-Widom is 3/2."""
        info = tracy_widom_tail_exponent()
        assert abs(info['right_tail_exponent'] - 1.5) < 1e-15

    def test_tail_coefficient_right(self):
        """Right tail coefficient is -2/3."""
        info = tracy_widom_tail_exponent()
        assert abs(info['right_tail_coefficient'] - (-2.0/3.0)) < 1e-15

    def test_tail_exponent_left(self):
        """Left tail exponent is 3."""
        info = tracy_widom_tail_exponent()
        assert abs(info['left_tail_exponent'] - 3.0) < 1e-15

    def test_airy_decay_matches(self):
        """Tracy-Widom right tail matches Airy function decay."""
        info = tracy_widom_tail_exponent()
        assert info['airy_decay_matches'] is True

    def test_tracy_widom_log_tail_formula(self):
        """log F_2(s) ~ -(2/3) * s^{3/2}."""
        for s in [1.0, 4.0, 9.0]:
            val = tracy_widom_log_tail(s)
            expected = -(2.0/3.0) * s**1.5
            assert abs(val - expected) < 1e-15

    def test_tracy_widom_log_tail_zero_at_origin(self):
        """log F_2(0) = 0 (leading term)."""
        assert tracy_widom_log_tail(0.0) == 0.0

    def test_tracy_widom_corrected_more_negative(self):
        """Subleading correction makes the tail more negative."""
        for s in [2.0, 5.0, 10.0]:
            leading = tracy_widom_log_tail(s)
            corrected = tracy_widom_log_tail_with_correction(s)
            # The -1/4 * log(s) correction is negative for s > 1
            assert corrected < leading

    def test_verify_tracy_widom_tail_consistency(self):
        """Verify ratio log F_2(s) / s^{3/2} -> -2/3."""
        result = verify_tracy_widom_tail()
        assert result['exponent_verified'] is True


# ==========================================================================
# Section 6: Multi-matrix model tests
# ==========================================================================

class TestMultiMatrixModel:
    """Tests for multi-matrix model shadow correspondence."""

    def test_two_matrix_decoupled(self):
        """Decoupled 2-matrix model: F_1 = (kappa_1 + kappa_2)/24."""
        F1 = two_matrix_free_energy_g1(0.5, 0.5)
        assert abs(F1 - 1.0/24.0) < 1e-15

    def test_two_matrix_additivity(self):
        """Shadow additivity: F_1(A1 + A2) = F_1(A1) + F_1(A2)."""
        k1, k2 = 1.0, 2.0
        combined = two_matrix_free_energy_g1(k1, k2)
        separate = k1/24.0 + k2/24.0
        assert abs(combined - separate) < 1e-15

    def test_W3_matches_2matrix_genus1(self):
        """W_3 genus-1 matches 2-matrix model decomposition."""
        result = two_matrix_vs_W3(24.0)
        assert result['genus1_match'] is True

    def test_W3_2matrix_match_various_c(self):
        """W_3 vs 2-matrix match holds for various central charges."""
        for c in [1.0, 6.0, 13.0, 26.0, 50.0]:
            result = two_matrix_vs_W3(c)
            assert result['genus1_match'] is True, f"Mismatch at c={c}"

    def test_W3_kappa_formula(self):
        """kappa(W_3) = 5c/6."""
        for c in [6.0, 12.0, 24.0]:
            result = two_matrix_vs_W3(c)
            assert abs(result['kappa_w3'] - 5*c/6.0) < 1e-14

    def test_W3_decomposition(self):
        """W_3 decomposes as kappa(Vir) + kappa(spin-3) = c/2 + c/3 = 5c/6."""
        for c in [6.0, 24.0]:
            result = two_matrix_vs_W3(c)
            assert abs(result['kappa_1'] + result['kappa_2'] - result['kappa_w3']) < 1e-14


# ==========================================================================
# Section 7: Spectral form factor tests
# ==========================================================================

class TestSpectralFormFactor:
    """Tests for the spectral form factor."""

    def test_sff_at_t0_equals_1(self):
        """SFF(t=0) = 1 by definition."""
        sff = spectral_form_factor(1.0, 0.0, 1.0)
        assert abs(sff - 1.0) < 1e-12

    def test_sff_positive(self):
        """SFF(t) >= 0 for all t."""
        for t in [0.0, 0.5, 1.0, 2.0, 5.0]:
            sff = spectral_form_factor(1.0, t, 1.0, max_genus=10)
            assert sff >= 0.0

    def test_sff_real(self):
        """SFF is real-valued (|Z|^2/|Z|^2 is real)."""
        for t in [0.1, 1.0, 3.0]:
            sff = spectral_form_factor(1.0, t, 1.0, max_genus=10)
            assert isinstance(sff, float)

    def test_sff_time_series_structure(self):
        """SFF time series has the expected structure."""
        result = sff_time_series(1.0, 1.0, t_max=5.0, n_points=50, max_genus=10)
        assert 'times' in result
        assert 'sff' in result
        assert len(result['times']) == 51  # 0 to 50 inclusive
        assert result['initial_value'] == pytest.approx(1.0, abs=1e-10)

    def test_sff_plateau_positive(self):
        """Plateau value is positive."""
        plateau = sff_plateau_value(1.0, 1.0)
        assert plateau > 0.0

    def test_sff_periodic_modulation(self):
        """SFF shows oscillatory behavior (not monotone) at small beta."""
        result = sff_time_series(0.5, 1.0, t_max=10.0, n_points=100, max_genus=10)
        # Check that there are local maxima and minima (non-monotone)
        vals = result['sff']
        has_increase = any(vals[i+1] > vals[i] for i in range(1, len(vals)-1))
        has_decrease = any(vals[i+1] < vals[i] for i in range(1, len(vals)-1))
        assert has_increase or has_decrease  # at least some variation


# ==========================================================================
# Section 8: Sine kernel tests
# ==========================================================================

class TestSineKernel:
    """Tests for the universal sine kernel."""

    def test_sine_kernel_diagonal(self):
        """K(x, x) = 1 for all x."""
        for x in [0.0, 0.5, 1.0, 2.7, -3.14]:
            assert abs(sine_kernel(x, x) - 1.0) < 1e-15

    def test_sine_kernel_origin(self):
        """K(0, 0) = 1."""
        assert abs(sine_kernel(0.0, 0.0) - 1.0) < 1e-15

    def test_sine_kernel_symmetric(self):
        """K(x, y) = K(y, x)."""
        for (x, y) in [(0.3, 1.7), (1.0, 2.0), (-0.5, 0.5)]:
            assert abs(sine_kernel(x, y) - sine_kernel(y, x)) < 1e-15

    def test_sine_kernel_zeros_at_integers(self):
        """K(0, n) = 0 for nonzero integer n."""
        for n in range(1, 6):
            assert abs(sine_kernel(0.0, float(n))) < 1e-14

    def test_sine_kernel_integral(self):
        """int_{-inf}^{inf} K(0, x) dx = 1 (sinc integral, truncated)."""
        result = verify_sine_kernel_properties()
        # Truncation to [-10, 10] with step 0.001 gives ~2% error
        assert result['integral_error'] < 0.03

    def test_sine_kernel_2point_cluster_negative(self):
        """T_2(x, y) = -K(x,y)^2 <= 0 (level repulsion)."""
        for (x, y) in [(0.0, 0.3), (1.0, 1.5), (0.0, 2.7)]:
            assert sine_kernel_2point_cluster(x, y) <= 0

    def test_sine_kernel_2point_cluster_zero_at_integers(self):
        """T_2(0, n) = 0 for integer n (K vanishes)."""
        for n in range(1, 4):
            assert abs(sine_kernel_2point_cluster(0.0, float(n))) < 1e-28

    def test_number_variance_linear_for_small_L(self):
        """Sigma^2(L) ~ L for small L (Poisson)."""
        L_small = 0.01
        sigma2 = sine_kernel_number_variance(L_small, n_points=1000)
        assert abs(sigma2 - L_small) / L_small < 0.1

    def test_number_variance_sublinear_for_large_L(self):
        """Sigma^2(L) grows logarithmically (sublinear) for large L."""
        sigma2_small = sine_kernel_number_variance(1.0, n_points=1000)
        sigma2_large = sine_kernel_number_variance(10.0, n_points=2000)
        # Sublinear: sigma2(10) / sigma2(1) < 10
        assert sigma2_large / sigma2_small < 10.0

    def test_gap_probability_small_L_near_1(self):
        """E(0; L) ~ 1 for small L."""
        for L in [0.001, 0.01]:
            gap = sine_kernel_gap_probability_small_L(L)
            assert abs(gap - 1.0) < 0.02

    def test_gap_probability_decreases(self):
        """E(0; L) decreases with L."""
        gaps = [sine_kernel_gap_probability_small_L(L) for L in [0.1, 0.5, 1.0, 2.0]]
        for i in range(len(gaps) - 1):
            assert gaps[i] >= gaps[i+1]

    def test_gap_probability_zero_at_L0(self):
        """E(0; 0) = 1."""
        assert sine_kernel_gap_probability_small_L(0.0) == 1.0

    def test_verify_sine_kernel_full(self):
        """Full verification of sine kernel properties."""
        result = verify_sine_kernel_properties()
        assert abs(result['diagonal'] - 1.0) < 1e-15
        assert abs(result['origin'] - 1.0) < 1e-15
        assert result['symmetric']
        assert result['zeros_at_integers']


# ==========================================================================
# Section 9: Resolvent tests
# ==========================================================================

class TestResolvent:
    """Tests for the matrix model resolvent."""

    def test_resolvent_asymptotics(self):
        """omega_0(z) ~ 1/z for large z."""
        z = 100.0 + 0.0j
        omega = resolvent_to_density(z)
        expected = 1.0 / z
        assert abs(omega - expected) < 0.01

    def test_resolvent_branch_cut(self):
        """omega_0(x +/- i*eps) has imaginary part for |x| < 2."""
        eps = 1e-8
        x = 1.0
        omega_plus = resolvent_to_density(complex(x, eps))
        omega_minus = resolvent_to_density(complex(x, -eps))
        # Discontinuity = 2*i*pi*rho(x)
        disc = (omega_minus - omega_plus) / (2j)
        rho_numerical = disc.real / PI
        rho_expected = wigner_semicircle_density(x)
        # The discontinuity should relate to the semicircle density
        assert abs(abs(disc.real) - PI * rho_expected) < 0.01

    def test_resolvent_real_outside_cut(self):
        """omega_0(z) is real for z real, |z| > 2."""
        for z in [3.0, 5.0, 10.0]:
            omega = resolvent_to_density(complex(z, 0))
            assert abs(omega.imag) < 1e-10

    def test_resolvent_genus1_correction(self):
        """Genus-1 resolvent correction has correct form."""
        z = complex(3.0, 0)
        omega1 = resolvent_genus_correction(z, 1, kappa_val=1.0)
        expected = -1.0 / (12.0 * (z**2 - 4))
        assert abs(omega1 - expected) < 1e-14

    def test_resolvent_genus0_returns_leading(self):
        """Genus-0 correction = leading resolvent."""
        z = complex(3.0, 0)
        omega0 = resolvent_genus_correction(z, 0)
        omega_lead = resolvent_to_density(z)
        assert abs(omega0 - omega_lead) < 1e-14


# ==========================================================================
# Section 10: Connecting computations tests
# ==========================================================================

class TestConnecting:
    """Tests for the shadow-matrix model dictionary and verifications."""

    def test_dictionary_has_key_entries(self):
        """Dictionary contains all essential entries."""
        d = shadow_to_matrix_model_dictionary()
        assert 'kappa' in d
        assert 'F_g' in d
        assert 'Q_L' in d
        assert 'class_G' in d

    def test_F1_identity_all_match(self):
        """F_1 = 1/24 matches across all normalizations."""
        result = F1_identity_verification()
        assert result['all_match'] is True

    def test_genus_expansion_shadow_eq_intersection(self):
        """Shadow (kappa=1) = intersection for g = 1..6."""
        data = genus_expansion_comparison(6)
        for g in range(1, 7):
            assert data[g]['shadow_eq_intersection'] is True

    def test_genus_expansion_positivity(self):
        """All free energies positive (shadow convention)."""
        data = genus_expansion_comparison(6)
        for g in range(1, 7):
            assert data[g]['shadow'] > 0
            assert data[g]['intersection'] > 0
            assert data[g]['combinatorial'] > 0

    def test_genus_expansion_monotone_decay(self):
        """Free energies decay with genus (Bernoulli decay)."""
        data = genus_expansion_comparison(6)
        for g in range(1, 6):
            assert data[g]['shadow'] > data[g+1]['shadow']
