r"""Tests for theorem_jt_gravity_shadow_engine: JT gravity vs shadow obstruction tower.

ORGANIZATION
============

Section 1:  Bernoulli / Faber-Pandharipande foundations
Section 2:  Shadow free energies F_g^{shadow}
Section 3:  JT free energies F_g^{JT} (WP volumes)
Section 4:  The ratio R_g = F_g^{JT} / F_g^{shadow}
Section 5:  Genus-1 dictionary (the only simple match)
Section 6:  Spectral curve comparison
Section 7:  Density of states
Section 8:  Trumpet partition functions
Section 9:  c = 26 critical string analysis
Section 10: Schwarzian limit (large c)
Section 11: Matrix model identification
Section 12: Large-g asymptotics
Section 13: Generating functions
Section 14: Structural comparison with certification boundaries
Section 15: Connection via topological recursion
Section 16: Object and analytic firewalls

VERIFICATION PATHS (>= 3 per claim)
====================================

Ratio non-constancy:
  (a) Explicit computation at g = 1, 2, 3
  (b) Lambda vs kappa class comparison (structural argument)
  (c) Large-g asymptotic divergence
  (d) Generating function comparison

Spectral curve non-identification:
  (a) Algebraic degree comparison
  (b) Zero structure comparison
  (c) Small-parameter expansion

Genus-1 match:
  (a) Direct formula verification
  (b) Mumford relation lambda_1 = kappa_1/12
  (c) Intersection number cross-check

CONVENTION CHECKS
=================
The tests keep scalar Bernoulli/A-hat data, finite Virasoro data,
WP/JT sine-curve data, EO recursion input, and external analytic
gravity claims in separate lanes.
"""

import math
import sys
import os
import pytest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_jt_gravity_shadow_engine import (
    CERTIFIED, CONDITIONAL, EXTERNAL_INPUT, FINITE_WINDOW, NON_CERTIFIED,
    object_kernel_firewall, gravity_claim_certification,
    virasoro_shadow_constants,
    # Section 1
    bernoulli_exact, lambda_fp_exact,
    # Section 2
    F_g_shadow, F_g_shadow_virasoro,
    # Section 3
    F_g_JT,
    # Section 4
    ratio_JT_shadow, ratio_JT_shadow_normalized, is_ratio_constant,
    # Section 5
    genus_1_dictionary,
    # Section 6
    shadow_spectral_curve, jt_spectral_curve, spectral_curve_comparison,
    shadow_curve_zeros, jt_curve_zeros,
    # Section 7
    jt_density_of_states, shadow_density_of_states, density_comparison,
    # Section 8
    jt_trumpet, jt_disk, shadow_trumpet_analogue,
    # Section 9
    c26_analysis,
    # Section 10
    schwarzian_limit_ratio,
    # Section 11
    matrix_size_from_kappa,
    # Section 12
    shadow_large_g_asymptotic, asymptotic_ratio,
    # Section 13
    shadow_generating_function, shadow_gf_virasoro,
    # Section 14
    full_structural_comparison, connection_via_topological_recursion,
    # Section 15
    verify_lambda_fp_values, verify_jt_genus1, verify_ratio_g1,
)

PI = math.pi
PI2 = PI * PI


# =========================================================================
# Section 1: Bernoulli / Faber-Pandharipande foundations
# =========================================================================

class TestBernoulliFoundations:
    """Exact Bernoulli numbers and lambda_g^FP."""

    def test_B2(self):
        assert bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_exact(6) == Fraction(1, 42)

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_all_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 12):
            assert lambda_fp_exact(g) > 0

    def test_verify_lambda_fp_values(self):
        """Cross-verify lambda_g^FP at g = 1, 2, 3."""
        results = verify_lambda_fp_values()
        for g, (val, ok) in results.items():
            assert ok, f"lambda_{g}^FP mismatch: {val}"


# =========================================================================
# Section 2: Shadow free energies
# =========================================================================

class TestShadowFreeEnergies:
    """F_g^{shadow}(Vir_c) = (c/2) * lambda_g^FP."""

    def test_F1_virasoro_c26(self):
        """F_1(Vir_26) = 13/24."""
        from sympy import Rational
        f1 = F_g_shadow_virasoro(26, 1)
        assert f1 == Rational(13, 24)

    def test_F2_virasoro_c26(self):
        """F_2(Vir_26) = 13 * 7/5760 = 91/5760."""
        from sympy import Rational
        f2 = F_g_shadow_virasoro(26, 2)
        assert f2 == Rational(91, 5760)

    def test_F_g_positive_all_c(self):
        """F_g > 0 for c > 0."""
        for c in [1, 2, 10, 26, 100]:
            for g in range(1, 6):
                f = F_g_shadow_virasoro(c, g)
                assert float(f) > 0, f"F_{g}(Vir_{c}) = {f} <= 0"

    def test_F_g_linear_in_c(self):
        """F_g(Vir_c) is linear in c."""
        for g in [1, 2, 3]:
            f_at_10 = float(F_g_shadow_virasoro(10, g))
            f_at_20 = float(F_g_shadow_virasoro(20, g))
            f_at_30 = float(F_g_shadow_virasoro(30, g))
            # f(20) = 2*f(10), f(30) = 3*f(10)
            assert abs(f_at_20 / f_at_10 - 2.0) < 1e-12
            assert abs(f_at_30 / f_at_10 - 3.0) < 1e-12


class TestVirasoroShadowConstants:
    """Canonical finite-window Virasoro constants."""

    def test_c26_constants(self):
        """At c=26: kappa=13, S4=5/1976, Delta=5/19."""
        data = virasoro_shadow_constants(26.0)
        assert data['status'] == CERTIFIED
        assert abs(data['kappa'] - 13.0) < 1e-14
        assert abs(data['S3'] - 2.0) < 1e-14
        assert abs(data['S4'] - 5.0 / 1976.0) < 1e-14
        assert abs(data['Delta'] - 5.0 / 19.0) < 1e-14
        assert abs(data['Q_t2_extra_coefficient'] - 10.0 / 19.0) < 1e-14

    def test_singular_central_charges_rejected(self):
        """The canonical rational formulas exclude c=0 and c=-22/5."""
        with pytest.raises(ValueError):
            virasoro_shadow_constants(0.0)
        with pytest.raises(ValueError):
            virasoro_shadow_constants(-22.0 / 5.0)


# =========================================================================
# Section 3: JT free energies (WP volumes)
# =========================================================================

class TestJTFreeEnergies:
    """F_g^{JT} = V_{g,0} (Weil-Petersson volumes)."""

    def test_F1_JT(self):
        """F_1^{JT} = pi^2/12."""
        f1 = F_g_JT(1)
        assert abs(f1 - PI2 / 12.0) < 1e-12

    def test_F2_JT(self):
        """F_2^{JT} = 29*pi^8/552960."""
        f2 = F_g_JT(2)
        expected = 29.0 * PI2**4 / 552960.0
        assert abs(f2 - expected) / abs(expected) < 1e-10

    def test_F_JT_positive(self):
        """All F_g^{JT} > 0 for g = 1..3."""
        for g in range(1, 4):
            assert F_g_JT(g) > 0

    def test_verify_jt_genus1(self):
        """Multi-path verification of F_1^{JT}."""
        v = verify_jt_genus1()
        assert v['all_agree']

    def test_F1_JT_from_intersection(self):
        """F_1^{JT} = 2*pi^2 * <kappa_1>_{1,1} = 2*pi^2/24 = pi^2/12."""
        # <kappa_1>_{1,1} = 1/24 (Witten)
        from_intersection = 2.0 * PI2 * (1.0 / 24.0)
        assert abs(F_g_JT(1) - from_intersection) < 1e-14


# =========================================================================
# Section 4: The ratio R_g
# =========================================================================

class TestRatioNonConstancy:
    """R_g = F_g^{JT} / F_g^{shadow} is not constant in g."""

    def test_ratio_g1_formula(self):
        """R_1(c) = 4*pi^2/c."""
        for c in [10, 26, 50]:
            r = ratio_JT_shadow(c, 1)
            expected = 4.0 * PI2 / c
            assert abs(r - expected) / abs(expected) < 1e-10

    def test_ratio_g1_c26(self):
        """R_1(26) = 4*pi^2/26 = 2*pi^2/13."""
        r = ratio_JT_shadow(26.0, 1)
        expected = 4.0 * PI2 / 26.0
        assert abs(r - expected) < 1e-10

    def test_ratio_varies_with_genus(self):
        """R_g at c = 26 varies with g (central negative result)."""
        ratios = {g: ratio_JT_shadow(26.0, g) for g in range(1, 4)}
        # R_1, R_2, R_3 should not all be equal
        r_vals = list(ratios.values())
        # Check that max/min ratio > 1.05 (at least 5% variation)
        assert max(r_vals) / min(r_vals) > 1.05, \
            f"Ratios too close: {ratios}. Expected variation > 5%."

    def test_is_ratio_constant_returns_false(self):
        """The normalized ratio is not constant."""
        constant, ratios = is_ratio_constant()
        assert not constant, f"Ratio unexpectedly constant: {ratios}"

    def test_ratio_normalized_g1(self):
        """Normalized R_1 = F_1^JT / lambda_1^FP = (pi^2/12)/(1/24) = 2*pi^2."""
        r1 = ratio_JT_shadow_normalized(1)
        assert abs(r1 - 2.0 * PI2) < 1e-10

    def test_ratio_normalized_g2(self):
        """Normalized R_2 = F_2^JT / lambda_2^FP, verify it differs from R_1."""
        r1 = ratio_JT_shadow_normalized(1)
        r2 = ratio_JT_shadow_normalized(2)
        # These should differ
        assert abs(r2 / r1 - 1.0) > 0.01, f"R_1 = {r1}, R_2 = {r2} too close"

    def test_verify_ratio_g1(self):
        """Multi-path verification of R_1."""
        v = verify_ratio_g1(26.0)
        assert v['agree']


# =========================================================================
# Section 5: Genus-1 dictionary
# =========================================================================

class TestGenus1Dictionary:
    """The genus-1 match is exact via Mumford lambda_1 = kappa_1/12."""

    def test_c_match_genus1(self):
        """c where F_1^shadow = F_1^JT is c = 4*pi^2."""
        d = genus_1_dictionary(1.0)  # any c
        assert abs(d['c_match_genus_1'] - 4.0 * PI2) < 1e-10

    def test_scalar_normalization_at_c26(self):
        """At c = 26 the scalar g=1 normalization is 26/(4*pi^2)."""
        d = genus_1_dictionary(26.0)
        expected = 26.0 / (4.0 * PI2)
        assert abs(d['scalar_normalization_to_JT_g1'] - expected) < 1e-10
        assert 0.5 < d['scalar_normalization_to_JT_g1'] < 1.0
        assert d['e_S0_genus_1'] is None
        assert d['e_S0_genus_1_status'] == NON_CERTIFIED
        assert d['jt_genus_weight_determines_S0'] is False

    def test_scalar_normalization_at_cmatch(self):
        """At c = 4*pi^2 the scalar g=1 normalization is one."""
        d = genus_1_dictionary(4.0 * PI2)
        assert abs(d['scalar_normalization_to_JT_g1'] - 1.0) < 1e-10


# =========================================================================
# Section 6: Spectral curve comparison
# =========================================================================

class TestSpectralCurves:
    """Shadow (polynomial) vs JT (transcendental) spectral curves."""

    def test_shadow_curve_at_origin(self):
        """Q_Vir(0) = c^2 (nonzero for c > 0)."""
        for c in [1, 10, 26]:
            Q0 = shadow_spectral_curve(c, 0.0)
            assert abs(Q0 - c * c) < 1e-10

    def test_jt_curve_at_origin(self):
        """JT curve vanishes at x = 0: sin^2(0) = 0."""
        assert abs(jt_spectral_curve(0.0)) < 1e-20

    def test_shadow_curve_no_real_zeros(self):
        """Shadow curve Q_Vir(t) > 0 for all real t when c > 0."""
        for c in [1, 10, 26, 100]:
            zeros = shadow_curve_zeros(c)
            assert len(zeros) == 0, f"Q_Vir has zeros at c = {c}: {zeros}"

    def test_jt_curve_infinitely_many_zeros(self):
        """JT curve has zeros at x = n^2/4."""
        zeros = jt_curve_zeros(10)
        assert len(zeros) == 11
        assert abs(zeros[0]) < 1e-14
        assert abs(zeros[1] - 0.25) < 1e-14
        assert abs(zeros[4] - 4.0) < 1e-14

    def test_shadow_curve_positive_definite(self):
        """Q_Vir(t) > 0 for all real t when c > 0."""
        for c in [1, 26]:
            for t in [-10, -1, 0, 1, 10, 100]:
                assert shadow_spectral_curve(c, t) > 0

    def test_spectral_curve_comparison_structure(self):
        """Structural comparison at c = 26."""
        comp = spectral_curve_comparison(26.0, 1.0)
        assert comp['shadow_degree'] == 2
        assert comp['JT_degree'] == 'transcendental'
        assert comp['same_curve_certified'] is False
        assert comp['comparison_status'] == NON_CERTIFIED


# =========================================================================
# Section 7: Density of states
# =========================================================================

class TestDensityOfStates:
    """JT (sinh) vs shadow (semicircle) densities."""

    def test_jt_rho_at_zero(self):
        """rho_JT(0) = 0."""
        assert abs(jt_density_of_states(0.0)) < 1e-10

    def test_jt_rho_positive(self):
        """rho_JT(E) > 0 for E > 0."""
        for E in [0.01, 0.1, 1.0, 10.0]:
            assert jt_density_of_states(E) > 0

    def test_jt_rho_unbounded(self):
        """rho_JT(E) -> infinity as E -> infinity."""
        assert jt_density_of_states(100.0) > jt_density_of_states(10.0)

    def test_shadow_rho_bounded(self):
        """Shadow density has finite support (semicircle for Gaussian)."""
        c = 26.0
        kappa = c / 2.0
        edge = 4.0 / kappa
        # Inside support: positive
        assert shadow_density_of_states(c, edge / 2.0) > 0
        # Outside support: zero
        assert shadow_density_of_states(c, edge + 0.1) == 0.0

    def test_density_support_difference(self):
        """JT: unbounded support. Shadow: bounded support."""
        c = 26.0
        # JT is nonzero at large E
        assert jt_density_of_states(1000.0) > 0
        # Shadow vanishes at large E
        assert shadow_density_of_states(c, 1000.0) == 0.0


# =========================================================================
# Section 8: Trumpet partition functions
# =========================================================================

class TestTrumpetFunctions:
    """JT trumpet vs shadow trumpet analogue."""

    def test_jt_trumpet_positive(self):
        """JT trumpet > 0 for beta > 0, b >= 0."""
        for beta in [0.1, 1.0, 10.0]:
            for b in [0.0, 1.0, 5.0]:
                assert jt_trumpet(beta, b) > 0

    def test_jt_trumpet_gaussian(self):
        """JT trumpet is a Gaussian in b."""
        beta = 1.0
        t0 = jt_trumpet(beta, 0.0)
        t1 = jt_trumpet(beta, 1.0)
        # Should decay: t1 < t0
        assert t1 < t0

    def test_jt_disk_positive(self):
        """JT disk amplitude > 0."""
        for beta in [0.1, 1.0, 10.0]:
            assert jt_disk(beta) > 0

    def test_shadow_trumpet_analogue_positive(self):
        """Shadow trumpet analogue > 0 for c > 0, small hbar."""
        for c in [1, 10, 26]:
            val = shadow_trumpet_analogue(c, 0.5, 0.0)
            assert val > 0


# =========================================================================
# Section 9: c = 26 critical string
# =========================================================================

class TestC26Analysis:
    """Full analysis at the critical bosonic string point c = 26."""

    def test_c26_kappa(self):
        """kappa(Vir_26) = 13."""
        data = c26_analysis()
        assert data['kappa'] == 13.0
        assert data['constants_status'] == CERTIFIED

    def test_c26_shadow_F1(self):
        """F_1(Vir_26) = 13/24."""
        data = c26_analysis()
        assert abs(data['shadow_energies'][1] - 13.0 / 24.0) < 1e-12

    def test_c26_ratio_not_constant(self):
        """Ratios R_g vary with g at c = 26."""
        data = c26_analysis()
        assert not data['ratio_constant']

    def test_c26_Q_at_origin(self):
        """Q_Vir(0) = 26^2 = 676 at c = 26."""
        data = c26_analysis()
        assert abs(data['Q_at_0'] - 676.0) < 1e-10

    def test_c26_no_shadow_zeros(self):
        """Shadow curve has no real zeros at c = 26."""
        data = c26_analysis()
        assert len(data['shadow_curve_zeros']) == 0


# =========================================================================
# Section 10: Schwarzian limit
# =========================================================================

class TestSchwarzianLimit:
    """Large-c limit comparison with JT."""

    def test_schwarzian_c_dependence(self):
        """F_shadow ~ c (linear), F_JT_weighted ~ 1/c^{2g-2} (polynomial)."""
        for g in [2, 3]:
            d1 = schwarzian_limit_ratio(100.0, g)
            d2 = schwarzian_limit_ratio(200.0, g)
            # F_shadow doubles when c doubles
            assert abs(d2['F_shadow'] / d1['F_shadow'] - 2.0) < 0.01
            # F_JT_weighted scales as (1/c)^{2g-2}, so halves for each power
            ratio_scaling = d2['F_JT_weighted'] / d1['F_JT_weighted']
            expected_scaling = (100.0 / 200.0) ** (2 * g - 2)
            # This should not be 2.0; the c-dependence differs.
            assert abs(ratio_scaling - expected_scaling) / abs(expected_scaling) < 0.01


# =========================================================================
# Section 11: Matrix model identification
# =========================================================================

class TestMatrixModel:
    """Matrix model identification N^2 = kappa."""

    def test_N_squared_equals_kappa(self):
        """N^2 = kappa in the Gaussian identification."""
        mm = matrix_size_from_kappa(13.0)
        assert mm['N_squared'] == 13.0

    def test_N_at_c26(self):
        """N = sqrt(13) ~ 3.606 at c = 26."""
        mm = matrix_size_from_kappa(13.0)
        assert abs(mm['N'] - math.sqrt(13.0)) < 1e-10

    def test_N_not_integer_c26(self):
        """N is not an integer at c = 26."""
        mm = matrix_size_from_kappa(13.0)
        assert not mm['is_integer_N']
        assert mm['double_scaled_JT_limit_certified'] is False

    def test_N_integer_at_kappa_1(self):
        """N = 1 at kappa = 1 (Witten-Kontsevich point)."""
        mm = matrix_size_from_kappa(1.0)
        assert mm['is_integer_N']
        assert abs(mm['N'] - 1.0) < 1e-10


# =========================================================================
# Section 12: Large-g asymptotics
# =========================================================================

class TestLargeGAsymptotics:
    """Shadow decays exponentially; JT grows factorially."""

    def test_shadow_exponential_decay(self):
        """F_g^{shadow} ~ kappa * 2/(2*pi)^{2g} decays geometrically."""
        kappa = 13.0
        for g in [5, 6, 7, 8]:
            f = float(F_g_shadow(kappa, g))
            f_next = float(F_g_shadow(kappa, g + 1))
            # Ratio should be approximately 1/(2*pi)^2 ~ 0.0253
            ratio = f_next / f
            assert 0.001 < ratio < 0.1, f"Ratio F_{g+1}/F_{g} = {ratio}, expected ~0.025"

    def test_shadow_asymptotic_matches(self):
        """The asymptotic formula approximates the exact value at large g."""
        kappa = 13.0
        for g in [8, 10, 12]:
            exact = float(F_g_shadow(kappa, g))
            asymp = shadow_large_g_asymptotic(kappa, g)
            # Should agree to within 10% at g >= 8
            assert abs(exact / asymp - 1.0) < 0.15, \
                f"g={g}: exact={exact}, asymp={asymp}, ratio={exact/asymp}"


# =========================================================================
# Section 13: Generating functions
# =========================================================================

class TestGeneratingFunctions:
    """Shadow GF = kappa * ((hbar/2)/sin(hbar/2) - 1)."""

    def test_gf_at_zero(self):
        """GF(0) = 0."""
        assert abs(shadow_generating_function(13.0, 0.0)) < 1e-14

    def test_gf_small_hbar(self):
        """GF ~ kappa * hbar^2/24 for small hbar."""
        kappa = 13.0
        h = 0.001
        val = shadow_generating_function(kappa, h)
        expected = kappa * h * h / 24.0
        assert abs(val - expected) / abs(expected) < 0.01

    def test_scalar_gf_convergence_radius(self):
        """The scalar A-hat GF has radius 2*pi."""
        kappa = 1.0
        # Well inside: should be finite
        assert math.isfinite(shadow_generating_function(kappa, 5.0))
        # Near pole: should be large
        val_near_pole = shadow_generating_function(kappa, 2.0 * PI - 0.001)
        assert val_near_pole > 100

    def test_gf_virasoro_c26(self):
        """Shadow GF for Vir_26 at hbar = 1."""
        val = shadow_gf_virasoro(26.0, 1.0)
        # = 13 * (0.5/sin(0.5) - 1) = 13 * (0.5/0.4794... - 1) = 13 * (1.0428 - 1) = 13 * 0.0428 ~ 0.556
        assert 0.4 < val < 0.7


# =========================================================================
# Section 14: Full structural comparison
# =========================================================================

class TestFullComparison:
    """Complete structural comparison between shadow and JT."""

    def test_shadow_not_equal_jt(self):
        """The shadow expansion is not equal to JT."""
        comp = full_structural_comparison(26.0)
        assert comp['shadow_equals_JT'] is False

    def test_scalar_shadow_convergent_certified(self):
        """Only the scalar Bernoulli/A-hat convergence is certified here."""
        comp = full_structural_comparison(26.0)
        assert comp['scalar_shadow_convergent'] is True
        assert comp['scalar_shadow_convergence_status'] == CERTIFIED
        assert comp['shadow_convergent'] is True
        assert comp['shadow_convergent_scope'] == 'scalar Bernoulli/A-hat lane only'
        assert comp['exact_scalar_radius_status'] == CERTIFIED

    def test_jt_asymptotic_external_only(self):
        """JT asymptotics are external analytic input, not certified here."""
        comp = full_structural_comparison(26.0)
        assert comp['jt_asymptotic'] is None
        assert comp['jt_asymptotic_status'] == EXTERNAL_INPUT
        assert comp['borel_summability_status'] == NON_CERTIFIED

    def test_shadow_curve_algebraic(self):
        """Shadow spectral curve is algebraic."""
        comp = full_structural_comparison(26.0)
        assert comp['shadow_curve_algebraic'] is True

    def test_jt_curve_transcendental(self):
        """JT spectral curve is transcendental."""
        comp = full_structural_comparison(26.0)
        assert comp['jt_curve_transcendental'] is True

    def test_ratio_not_constant(self):
        """The ratio R_g varies with g."""
        comp = full_structural_comparison(26.0)
        assert comp['ratio_constant'] is False

    def test_no_gravity_overclaims(self):
        """Scalar data has explicit EO, BTZ, and all-genus boundaries."""
        comp = full_structural_comparison(26.0)
        assert comp['full_EO_recursion_certified_from_Q_L'] is False
        assert comp['eo_recursion_from_shadow_curve_status'] == CONDITIONAL
        assert comp['btz_closed_form_recovery_status'] == NON_CERTIFIED
        assert comp['all_genus_3d_partition_theorem_status'] == NON_CERTIFIED
        assert comp['full_jt_partition_from_shadow'] is False


# =========================================================================
# Section 15: Connection via topological recursion
# =========================================================================

class TestTopologicalRecursionConnection:
    """Topological-recursion comparison on different spectral curves."""

    def test_full_eo_not_certified_from_shadow_curve(self):
        """The quadratic shadow curve alone supplies only partial EO data."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['both_from_top_rec'] is None
        assert conn['shadow_EO_status'] == CONDITIONAL
        assert conn['full_EO_recursion_from_shadow_curve'] is False
        assert conn['jt_sine_curve_status'] == EXTERNAL_INPUT
        assert conn['double_scaled_JT_sector_certified'] is False

    def test_different_curves(self):
        """But on different spectral curves."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['same_spectral_curve'] is False

    def test_common_substrate(self):
        """Both live on the same moduli space M_{g,n}."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['common_substrate'] == 'M_{g,n}'

    def test_genus_1_match(self):
        """Genus-1 match is exact (Mumford relation)."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['genus_1_match'] is True
        assert conn['genus_1_match_status'] == CERTIFIED
        assert abs(conn['genus_1_proportionality'] - 4.0 * PI2 / 26.0) < 1e-12

    def test_higher_genus_no_match(self):
        """Higher genus: no simple proportionality."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['higher_genus_match'] is False

    def test_convergence_properties(self):
        """Convergence statements are scoped by lane."""
        conn = connection_via_topological_recursion(26.0)
        assert 'scalar A-hat lane' in conn['shadow_convergence']
        assert 'external WP/JT asymptotic input' in conn['jt_convergence']
        assert conn['borel_summability_status'] == NON_CERTIFIED


# =========================================================================
# Section 16: Object and analytic firewalls
# =========================================================================

class TestFirewalls:
    """Object, kernel, and analytic certification boundaries."""

    def test_object_firewall(self):
        """The five objects remain distinct."""
        fw = object_kernel_firewall()
        assert fw['objects'] == ('A', 'B(A)', 'A^i', 'A^!', 'Z_ch^der(A)')
        assert fw['bar_cobar_inversion'] == 'Omega(B(A)) = A'
        assert fw['bar_cobar_inversion_is_koszul_duality'] is False
        assert 'Verdier' in fw['koszul_dual_branch']
        assert 'Hochschild' in fw['bulk_branch']

    def test_kernel_constants(self):
        """Kernel constants use the local canonical normalizations."""
        kernels = object_kernel_firewall()['kernels']
        assert kernels['affine_raw_trace_form'] == 'k*Omega_tr/z'
        assert kernels['kz_connection'] == 'Omega/((k+h^vee)z)'
        assert kernels['heisenberg'] == 'k/z'
        assert kernels['virasoro'] == '(c/2)/z^3 + 2T/z'

    def test_gravity_certification_map(self):
        """Analytic gravity claims are not inferred from scalar shadows."""
        cert = gravity_claim_certification()
        assert cert['scalar_bernoulli_ahat_lane'] == CERTIFIED
        assert cert['virasoro_shadow_constants'] == CERTIFIED
        assert cert['wp_jt_sine_curve_data'] == EXTERNAL_INPUT
        assert cert['wp_jt_finite_window']['status'] == FINITE_WINDOW
        assert cert['wp_jt_finite_window']['certified_genera'] == (1, 2, 3)
        assert cert['eo_recursion_from_shadow_curve'] == CONDITIONAL
        assert cert['exact_scalar_radius_2pi'] == CERTIFIED
        assert cert['jt_borel_summability'] == NON_CERTIFIED
        assert cert['btz_closed_form_recovery_from_shadow'] == NON_CERTIFIED
        assert cert['full_jt_partition_function_from_shadow'] == NON_CERTIFIED
        assert cert['all_genus_3d_gravity_partition_theorem'] == NON_CERTIFIED
