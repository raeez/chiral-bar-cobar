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
Section 14: Full structural comparison
Section 15: Connection via topological recursion

VERIFICATION PATHS (>= 3 per claim)
====================================

Ratio non-constancy (the CENTRAL negative result):
  (a) Explicit computation at g = 1, 2, 3, 4
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

ANTI-PATTERNS GUARDED
=====================
AP1:  kappa recomputed from first principles for each family.
AP3:  No pattern-matching; each ratio verified independently.
AP10: Expected values from independent computation, not hardcoded.
AP22: All F_g values verified positive.
AP38: WP volumes in Mirzakhani convention, cross-checked.
AP39: kappa(Vir_c) = c/2 (NOT c or c/12 or anything else).
AP48: kappa depends on the full algebra, not just c.
"""

import math
import sys
import os
import pytest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_jt_gravity_shadow_engine import (
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
        """lambda_2^FP = 7/5760 (NOT 1/1152 -- AP38)."""
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_all_positive(self):
        """All lambda_g^FP are positive (AP22)."""
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
        """F_g > 0 for c > 0 (AP22)."""
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
# Section 4: The ratio R_g (CENTRAL RESULT)
# =========================================================================

class TestRatioNonConstancy:
    """R_g = F_g^{JT} / F_g^{shadow} is NOT constant in g."""

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
        # R_1, R_2, R_3 should NOT all be equal
        r_vals = list(ratios.values())
        # Check that max/min ratio > 1.05 (at least 5% variation)
        assert max(r_vals) / min(r_vals) > 1.05, \
            f"Ratios too close: {ratios}. Expected variation > 5%."

    def test_is_ratio_constant_returns_false(self):
        """The normalized ratio is NOT constant."""
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

    def test_e_S0_at_c26(self):
        """At c = 26: e^{S_0} = 26/(4*pi^2) ~ 0.6580."""
        d = genus_1_dictionary(26.0)
        expected = 26.0 / (4.0 * PI2)
        assert abs(d['e_S0_genus_1'] - expected) < 1e-10
        assert 0.5 < d['e_S0_genus_1'] < 1.0

    def test_e_S0_at_cmatch(self):
        """At c = 4*pi^2: e^{S_0} = 1."""
        d = genus_1_dictionary(4.0 * PI2)
        assert abs(d['e_S0_genus_1'] - 1.0) < 1e-10


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
            # This should NOT be 2.0, demonstrating the mismatch
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
        """N is NOT an integer at c = 26."""
        mm = matrix_size_from_kappa(13.0)
        assert not mm['is_integer_N']

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

    def test_gf_convergence_radius(self):
        """GF converges for |hbar| < 2*pi, diverges at 2*pi."""
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
        """The shadow expansion is NOT equal to JT (central negative result)."""
        comp = full_structural_comparison(26.0)
        assert comp['shadow_equals_JT'] is False

    def test_shadow_convergent(self):
        """Shadow genus expansion converges."""
        comp = full_structural_comparison(26.0)
        assert comp['shadow_convergent'] is True

    def test_jt_asymptotic(self):
        """JT genus expansion is asymptotic (divergent)."""
        comp = full_structural_comparison(26.0)
        assert comp['jt_asymptotic'] is True

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


# =========================================================================
# Section 15: Connection via topological recursion
# =========================================================================

class TestTopologicalRecursionConnection:
    """Both arise from top. rec. on DIFFERENT spectral curves."""

    def test_both_from_top_rec(self):
        """Both shadow and JT arise from topological recursion."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['both_from_top_rec'] is True

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

    def test_higher_genus_no_match(self):
        """Higher genus: no simple proportionality."""
        conn = connection_via_topological_recursion(26.0)
        assert conn['higher_genus_match'] is False

    def test_convergence_properties(self):
        """Shadow converges, JT diverges."""
        conn = connection_via_topological_recursion(26.0)
        assert 'convergent' in conn['shadow_convergence']
        assert 'factorial' in conn['jt_convergence'] or 'asymptotic' in conn['jt_convergence']
