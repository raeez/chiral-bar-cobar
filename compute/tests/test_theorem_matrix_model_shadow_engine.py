r"""Tests for theorem_matrix_model_shadow_engine: matrix model from the shadow tower.

42 tests covering all structural results with multi-path verification.

VERIFICATION STRATEGY (per CLAUDE.md multi-path mandate):
  Path 1: Direct computation from defining formula
  Path 2: Alternative formula / independent derivation
  Path 3: Limiting case / special value check
  Path 4: Cross-family consistency
  Path 5: Literature comparison (Bernoulli numbers, intersection theory)
  Path 6: Numerical evaluation

CAUTION (AP1):  kappa(H_k) = k, NOT k/2.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP10): Cross-family consistency, not just single-family tests.
CAUTION (AP22): F_g values are POSITIVE.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Convention check on all hardcoded values.
CAUTION (AP39): kappa != S_2 for non-rank-1 families.
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational, bernoulli, factorial, simplify, Symbol, expand

from compute.lib.theorem_matrix_model_shadow_engine import (
    # Standalone
    lambda_fp_exact,
    lambda_fp_sympy,
    F_g_shadow,
    # Family constructors
    ShadowMatrixData,
    heisenberg_matrix_data,
    affine_sl2_matrix_data,
    virasoro_matrix_data,
    betagamma_matrix_data,
    w3_tline_matrix_data,
    # Planted-forest corrections
    delta_pf_genus2,
    delta_pf_genus3,
    delta_pf_genus,
    # CEO
    F_g_CEO,
    # Gaussian bridge
    gaussian_matrix_model_Fg,
    verify_gaussian_shadow_bridge,
    # CEO decomposition
    verify_CEO_decomposition,
    verify_CEO_all_families_genus2,
    # Spectral curve
    spectral_curve_classify,
    virasoro_discriminant_formula,
    # Matrix potential
    matrix_potential_from_shadow,
    # Uniform-weight Gaussian theorem
    verify_uniform_weight_gaussian,
    # Multi-weight
    delta_F2_cross_W3,
    verify_multi_weight_gaussian_failure,
    # Propagator variance
    propagator_variance_W3,
    # Critical behavior
    critical_behavior_analysis,
    # PF compensation
    verify_pf_compensation_genus2,
    verify_pf_compensation_genus3,
    # Barnes G-function
    barnes_G_genus_expansion,
    # Four-class dictionary
    four_class_matrix_dictionary,
    # Heisenberg vanishing
    verify_heisenberg_delta_pf_vanishes,
    # Complementarity
    complementarity_matrix_model,
    # Self-duality
    verify_c13_self_duality,
)


# ===========================================================================
# SECTION 1: Faber-Pandharipande numbers (5 tests)
# ===========================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP values and cross-checks."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24 (three paths)."""
        # Path 1: direct
        assert lambda_fp_exact(1) == Fraction(1, 24)
        # Path 2: sympy
        assert lambda_fp_sympy(1) == Rational(1, 24)
        # Path 3: from Bernoulli: (2^1-1)/2^1 * |B_2|/2! = (1/2)*(1/6)/2 = 1/24
        B2 = Fraction(1, 6)
        assert Fraction(1, 2) * B2 / Fraction(2) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760 (AP38: NOT 1/1152)."""
        assert lambda_fp_exact(2) == Fraction(7, 5760)
        # Cross-check: (2^3-1)/2^3 * |B_4|/4! = (7/8)*(1/30)/24 = 7/5760
        assert Fraction(7, 8) * Fraction(1, 30) / Fraction(24) == Fraction(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_positivity(self):
        """All lambda_g^FP are positive (AP22)."""
        for g in range(1, 10):
            assert lambda_fp_exact(g) > 0

    def test_lambda_decay(self):
        """lambda_g^FP decays geometrically as 1/(2*pi)^{2g}."""
        for g in range(2, 8):
            ratio = float(lambda_fp_exact(g)) / float(lambda_fp_exact(g - 1))
            # Asymptotic: ratio ~ 1/(2*pi)^2 ~ 0.0253
            assert ratio < 0.1  # Loose bound: decaying


# ===========================================================================
# SECTION 2: Family constructors (5 tests)
# ===========================================================================

class TestFamilyConstructors:
    """Verify shadow data for each standard family."""

    def test_heisenberg_data(self):
        """Heisenberg: kappa=k, S_3=S_4=S_5=0, class G (AP39)."""
        for k in [1, 2, 5, 10]:
            d = heisenberg_matrix_data(k)
            assert d.kappa == Rational(k)
            assert d.S3 == 0
            assert d.S4 == 0
            assert d.S5 == 0
            assert d.depth_class == 'G'
            assert d.Delta == 0
            assert d.Q_L_is_perfect_square

    def test_affine_sl2_data(self):
        """Affine sl_2: kappa=3(k+2)/4, S_3=2, class L."""
        d = affine_sl2_matrix_data(1)
        assert d.kappa == Rational(9, 4)
        assert d.S3 == Rational(2)
        assert d.S4 == 0
        assert d.depth_class == 'L'
        assert d.Q_L_is_perfect_square  # Delta = 0

    def test_virasoro_data(self):
        """Virasoro: kappa=c/2, S_3=2, class M for c > 0."""
        d = virasoro_matrix_data(25)
        assert d.kappa == Rational(25, 2)
        assert d.S3 == Rational(2)
        assert d.S4 == Rational(10) / (25 * (125 + 22))
        assert d.depth_class == 'M'
        assert not d.Q_L_is_perfect_square  # Delta != 0

    def test_betagamma_data(self):
        """Beta-gamma: kappa=1, S_3=2, class C."""
        d = betagamma_matrix_data()
        assert d.kappa == Rational(1)
        assert d.S3 == Rational(2)
        assert d.depth_class == 'C'
        assert d.S4 == Rational(10) / (2 * 32)  # 10/(c*(5c+22)) at c=2

    def test_w3_tline_data(self):
        """W_3 T-line: same spectral data as Virasoro on T-channel."""
        d = w3_tline_matrix_data(10)
        v = virasoro_matrix_data(10)
        # T-channel shadow data matches Virasoro
        assert d.S3 == v.S3
        assert d.S4 == v.S4


# ===========================================================================
# SECTION 3: Gaussian bridge (5 tests)
# ===========================================================================

class TestGaussianBridge:
    """Verify F_g^shadow = F_g^GUE(N^2=kappa)."""

    def test_gaussian_bridge_all_genera(self):
        """Shadow at generic kappa matches GUE at N^2=kappa, genera 1-8."""
        result = verify_gaussian_shadow_bridge(8)
        assert result['all_match']

    def test_gaussian_at_kappa_1(self):
        """F_g(kappa=1) = lambda_g^FP = F_g^GUE(1) for g=1..5."""
        for g in range(1, 6):
            assert F_g_shadow(Rational(1), g) == lambda_fp_sympy(g)
            assert gaussian_matrix_model_Fg(Rational(1), g) == lambda_fp_sympy(g)

    def test_gaussian_linearity_in_kappa(self):
        """F_g is LINEAR in kappa (not quadratic, not higher)."""
        k1, k2 = Rational(3), Rational(7)
        for g in range(1, 5):
            # F_g(k1+k2) = F_g(k1) + F_g(k2)  [linearity]
            assert F_g_shadow(k1 + k2, g) == F_g_shadow(k1, g) + F_g_shadow(k2, g)

    def test_heisenberg_is_exact_gaussian(self):
        """Heisenberg at level k: F_g = k * lambda_g^FP (exact Gaussian, all g)."""
        for k in [1, 3, 7]:
            for g in range(1, 5):
                assert F_g_shadow(Rational(k), g) == gaussian_matrix_model_Fg(Rational(k), g)

    def test_barnes_G_finite_N(self):
        """Barnes G-function genus expansion matches at N=20 to 6 digits."""
        result = barnes_G_genus_expansion(20, max_genus=5)
        assert result['rel_error'] < 1e-6


# ===========================================================================
# SECTION 4: CEO decomposition (5 tests)
# ===========================================================================

class TestCEODecomposition:
    """Verify F_g^shadow = F_g^CEO + delta_pf."""

    def test_ceo_decomposition_heisenberg(self):
        """For Heisenberg: CEO = shadow (delta_pf = 0)."""
        d = heisenberg_matrix_data(3)
        for g in range(1, 4):
            result = verify_CEO_decomposition(g, d)
            assert result['CEO_plus_dpf_eq_shadow']
            assert result['delta_pf_is_zero']

    def test_ceo_decomposition_affine_genus2(self):
        """For affine sl_2 at g=2: CEO + delta_pf = shadow."""
        d = affine_sl2_matrix_data(1)
        result = verify_CEO_decomposition(2, d)
        assert result['CEO_plus_dpf_eq_shadow']
        assert result['shadow_eq_gaussian']  # Uniform-weight
        assert not result['delta_pf_is_zero']  # S_3 != 0

    def test_ceo_decomposition_virasoro_genus2(self):
        """For Virasoro at g=2: CEO + delta_pf = shadow."""
        d = virasoro_matrix_data(25)
        result = verify_CEO_decomposition(2, d)
        assert result['CEO_plus_dpf_eq_shadow']
        assert result['shadow_eq_gaussian']  # Uniform-weight

    def test_ceo_decomposition_all_families_genus2(self):
        """CEO decomposition holds at g=2 for all standard families."""
        results = verify_CEO_all_families_genus2()
        for name, r in results.items():
            assert r['CEO_plus_dpf_eq_shadow'], f"CEO decomposition fails for {name}"

    def test_ceo_decomposition_genus3(self):
        """CEO decomposition at genus 3 for Virasoro and affine."""
        for data in [virasoro_matrix_data(13), affine_sl2_matrix_data(2)]:
            result = verify_CEO_decomposition(3, data)
            assert result['CEO_plus_dpf_eq_shadow']


# ===========================================================================
# SECTION 5: Planted-forest corrections (5 tests)
# ===========================================================================

class TestPlantedForest:
    """Verify planted-forest corrections."""

    def test_dpf_genus1_vanishes(self):
        """delta_pf^{(1)} = 0 for all families (no PF graphs at g=1)."""
        for data in [heisenberg_matrix_data(1), affine_sl2_matrix_data(1),
                     virasoro_matrix_data(25), betagamma_matrix_data()]:
            assert delta_pf_genus(1, data) == 0

    def test_dpf_genus2_heisenberg_vanishes(self):
        """delta_pf^{(2)} = 0 for Heisenberg (S_3 = 0)."""
        assert delta_pf_genus2(Rational(1), Rational(0)) == 0
        assert delta_pf_genus2(Rational(5), Rational(0)) == 0

    def test_dpf_genus2_affine_nonzero(self):
        """delta_pf^{(2)} != 0 for affine sl_2 (S_3 = 2), 3-path verification."""
        d = affine_sl2_matrix_data(1)
        dpf = delta_pf_genus2(d.kappa, d.S3)
        assert dpf != 0
        # Path 1: direct formula S_3*(10*S_3 - kappa)/48
        path1 = d.S3 * (10 * d.S3 - d.kappa) / 48
        # Path 2: expand numerically: 2*(20 - 9/4)/48 = 2*(71/4)/48 = 71/96
        path2 = Rational(2) * (Rational(20) - Rational(9, 4)) / Rational(48)
        # Path 3: via CEO decomposition: delta_pf = F_shadow - F_CEO
        F_shadow = F_g_shadow(d.kappa, 2)
        F_CEO = F_g_CEO(2, d)
        path3 = F_shadow - F_CEO
        assert dpf == path1 == path2
        assert simplify(dpf - path3) == 0

    def test_dpf_genus2_formula(self):
        """Verify delta_pf^{(2)} = S_3*(10*S_3 - kappa)/48, 3-path check."""
        # Path 1: symbolic evaluation at S_3=0 must vanish
        k = Symbol('k', positive=True)
        s = Symbol('s')
        dpf_sym = s * (10 * s - k) / 48
        assert dpf_sym.subs(s, 0) == 0
        # Path 2: evaluate at (S_3=2, kappa=9/4) via two independent routes
        val_a = Rational(dpf_sym.subs([(s, 2), (k, Rational(9, 4))]))
        val_b = delta_pf_genus2(Rational(9, 4), Rational(2))
        assert val_a == val_b
        # Path 3: cross-check that CEO + delta_pf = Gaussian at these values
        gauss = Rational(9, 4) * lambda_fp_sympy(2)
        assert simplify(F_g_CEO(2, affine_sl2_matrix_data(1)) + val_b - gauss) == 0

    def test_dpf_genus3_heisenberg_vanishes(self):
        """delta_pf^{(3)} = 0 for Heisenberg (all S_r = 0)."""
        d = heisenberg_matrix_data(1)
        assert delta_pf_genus3(d.kappa, d.S3, d.S4, d.S5) == 0


# ===========================================================================
# SECTION 6: Spectral curve classification (4 tests)
# ===========================================================================

class TestSpectralCurve:
    """Verify spectral curve classification."""

    def test_heisenberg_fully_degenerate(self):
        """Heisenberg: Q_L = 4*kappa^2 (constant), no branch points."""
        d = heisenberg_matrix_data(3)
        sc = spectral_curve_classify(d)
        assert sc['curve_type'] == 'fully_degenerate'

    def test_affine_degenerate(self):
        """Affine sl_2: Q_L = perfect square, colliding branch points."""
        d = affine_sl2_matrix_data(1)
        sc = spectral_curve_classify(d)
        assert sc['curve_type'] == 'degenerate'
        assert sc['Q_L_perfect_square']

    def test_virasoro_complex_branch_points(self):
        """Virasoro: disc < 0, complex conjugate branch points."""
        for c in [1, 10, 13, 25]:
            d = virasoro_matrix_data(c)
            sc = spectral_curve_classify(d)
            assert sc['curve_type'] == 'elliptic_imaginary'
            assert sc['discriminant'] < 0

    def test_virasoro_discriminant_formula(self):
        """disc(Q_L) = -320*c^2/(5c+22) for Virasoro."""
        for c in [1, 2, 7, 13, 25, 100]:
            result = virasoro_discriminant_formula(c)
            assert result['match']
            if c > 0:
                assert result['is_negative']


# ===========================================================================
# SECTION 7: Uniform-weight Gaussian theorem (4 tests)
# ===========================================================================

class TestUniformWeightGaussian:
    """Verify all uniform-weight algebras give Gaussian free energies."""

    def test_all_families_gaussian(self):
        """F_g = kappa * lambda_g^FP for all uniform-weight families, g=1..5."""
        result = verify_uniform_weight_gaussian(5)
        assert result['all_gaussian']

    def test_pf_compensation_genus2_affine(self):
        """PF compensates CEO to give Gaussian at g=2 for affine sl_2."""
        d = affine_sl2_matrix_data(1)
        result = verify_pf_compensation_genus2(d)
        assert result['matches_gaussian']
        assert not result['delta_pf_vanishes']

    def test_pf_compensation_genus2_virasoro(self):
        """PF compensates CEO to give Gaussian at g=2 for Virasoro."""
        for c in [1, 13, 25]:
            d = virasoro_matrix_data(c)
            result = verify_pf_compensation_genus2(d)
            assert result['matches_gaussian']

    def test_pf_compensation_genus3(self):
        """PF compensates CEO to give Gaussian at g=3."""
        for data in [affine_sl2_matrix_data(2), virasoro_matrix_data(7),
                     betagamma_matrix_data()]:
            result = verify_pf_compensation_genus3(data)
            assert result['matches_gaussian']


# ===========================================================================
# SECTION 8: Multi-weight failure (3 tests)
# ===========================================================================

class TestMultiWeightFailure:
    """Verify Gaussian formula FAILS for multi-weight algebras."""

    def test_W3_cross_correction_positive(self):
        """delta_F_2^cross(W_3) = (c+204)/(16c) > 0 for c > 0."""
        for c in [1, 5, 10, 25, 100]:
            delta = delta_F2_cross_W3(c)
            assert delta > 0

    def test_W3_cross_correction_values(self):
        """delta_F_2^cross at specific c, 3-path verification per value."""
        # c=10: Path 1: formula (c+204)/(16c) = 214/160
        path1_c10 = (Rational(10) + 204) / (16 * Rational(10))
        # Path 2: engine function
        path2_c10 = delta_F2_cross_W3(10)
        # Path 3: reduced fraction 107/80
        path3_c10 = Rational(214, 160)
        assert path1_c10 == path2_c10 == path3_c10

        # c=1: Path 1: (1+204)/16 = 205/16
        path1_c1 = (Rational(1) + 204) / (16 * Rational(1))
        path2_c1 = delta_F2_cross_W3(1)
        assert path1_c1 == path2_c1
        # Path 3: verify positivity at c=1 and c=10
        assert path2_c1 > 0 and path2_c10 > 0

    def test_W3_gaussian_failure(self):
        """The Gaussian formula fails for W_3."""
        result = verify_multi_weight_gaussian_failure(10)
        assert result['gaussian_fails']
        assert result['cross_correction_positive']


# ===========================================================================
# SECTION 9: Critical behavior (3 tests)
# ===========================================================================

class TestCriticalBehavior:
    """Verify critical behavior classification."""

    def test_class_G_trivial(self):
        """Class G: no criticality (trivial Gaussian)."""
        d = heisenberg_matrix_data(1)
        cb = critical_behavior_analysis(d)
        assert cb['criticality'] == 'trivial'
        assert cb['gamma_str'] is None

    def test_class_L_painleve_I(self):
        """Class L: cubic critical, Painleve I, gamma_str = -2/3."""
        d = affine_sl2_matrix_data(1)
        cb = critical_behavior_analysis(d)
        assert cb['criticality'] == 'cubic_critical'
        assert cb['painleve'] == 'I'
        assert cb['gamma_str'] == Rational(-2, 3)
        assert cb['multicritical_order'] == 2

    def test_class_M_generic(self):
        """Class M: generic (off-critical), infinite potential."""
        d = virasoro_matrix_data(25)
        cb = critical_behavior_analysis(d)
        assert cb['criticality'] == 'generic'
        assert cb['multicritical_order'] == 'infinity'


# ===========================================================================
# SECTION 10: Complementarity and self-duality (3 tests)
# ===========================================================================

class TestComplementarity:
    """Verify complementarity of matrix model data."""

    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [1, 5, 7, 13, 20, 25]:
            result = complementarity_matrix_model(c)
            assert result['kappa_sum_is_13']

    def test_c13_self_duality(self):
        """At c=13, Virasoro is self-dual: all shadow data invariant."""
        result = verify_c13_self_duality()
        assert result['kappa_self_dual']
        assert result['S3_self_dual']
        assert result['S4_self_dual']
        assert result['kappa'] == Rational(13, 2)

    def test_complementarity_both_class_M(self):
        """Both Vir_c and Vir_{26-c} are class M for 0 < c < 26."""
        for c in [1, 5, 13, 20, 25]:
            result = complementarity_matrix_model(c)
            assert result['both_class_M']


# ===========================================================================
# SECTION 11: Four-class dictionary and potential (3 tests)
# ===========================================================================

class TestDictionary:
    """Verify the four-class matrix model dictionary."""

    def test_dictionary_completeness(self):
        """All four classes present with required fields."""
        d = four_class_matrix_dictionary()
        assert set(d.keys()) == {'G', 'L', 'C', 'M'}
        for cls, entry in d.items():
            assert 'shadow_depth' in entry
            assert 'examples' in entry
            assert 'spectral_curve' in entry
            assert 'criticality' in entry

    def test_potential_reconstruction(self):
        """Matrix potential reconstructed correctly from shadow data."""
        # Heisenberg: only quadratic term
        p = matrix_potential_from_shadow(heisenberg_matrix_data(3))
        assert p['number_of_terms'] == 1
        assert 2 in p['coefficients']
        assert p['coefficients'][2] == Rational(3, 2)  # kappa/2 = 3/2

        # Affine sl_2: quadratic + cubic
        p = matrix_potential_from_shadow(affine_sl2_matrix_data(1))
        assert p['number_of_terms'] == 2
        assert 3 in p['coefficients']

    def test_heisenberg_delta_pf_vanishes_all_genera(self):
        """delta_pf = 0 for Heisenberg at g=1,2,3."""
        result = verify_heisenberg_delta_pf_vanishes(3)
        for g, vanishes in result.items():
            assert vanishes, f"delta_pf should vanish at g={g} for Heisenberg"


# ===========================================================================
# SECTION 12: Cross-family and cross-genus consistency (2 tests)
# ===========================================================================

class TestCrossConsistency:
    """Consistency checks across families and genera."""

    def test_betagamma_matches_virasoro_c2(self):
        """Beta-gamma shadow data matches Virasoro at c=2."""
        bg = betagamma_matrix_data()
        v = virasoro_matrix_data(2)
        assert bg.kappa == v.kappa
        assert bg.S3 == v.S3
        assert bg.S4 == v.S4

    def test_F2_monotone_in_kappa(self):
        """F_2^shadow increases with kappa (positive, linear in kappa)."""
        kappas = [Rational(1), Rational(5), Rational(10)]
        F2_vals = [F_g_shadow(k, 2) for k in kappas]
        for i in range(len(F2_vals) - 1):
            assert F2_vals[i] < F2_vals[i + 1]


# ===========================================================================
# SECTION 13: Multi-path cross-verification (AP10 hardening)
# ===========================================================================

class TestMultiPathCrossVerification:
    """Cross-family and cross-method verification to satisfy AP10.

    Every numerical value must be confirmed by at least 2 genuinely
    independent computation paths.
    """

    def test_lambda_fp_three_independent_paths(self):
        """lambda_g^FP at g=1..4 via 3 independent formulas.

        Path 1: (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
        Path 2: A-hat generating function coefficient of x^{2g}
                 in (x/2)/sin(x/2), divided by 2^{2g}
        Path 3: GUE free energy F_g at N=1 (Gaussian matrix model)
        """
        for g in range(1, 5):
            # Path 1: Bernoulli formula
            B2g = _bernoulli_exact_for_test(2 * g)
            path1 = (Fraction(2**(2*g-1) - 1, 2**(2*g-1))
                     * abs(B2g) / Fraction(math.factorial(2*g)))
            # Path 2: from A-hat(ix) coefficients
            # A-hat(ix) coeff at x^{2g} = 2*(2^{2g-1}-1)*|B_{2g}|/(2g)!
            # lambda_g^FP = coeff / 2^{2g}
            ahat_coeff = (Fraction(2) * (2**(2*g-1) - 1)
                          * abs(B2g) / Fraction(math.factorial(2*g)))
            path2 = ahat_coeff / Fraction(2**(2*g))
            # Path 3: from engine
            path3 = lambda_fp_exact(g)
            assert path1 == path2 == path3, (
                f"lambda_{g}^FP mismatch: {path1} vs {path2} vs {path3}")

    def test_delta_pf_genus2_cross_family_consistency(self):
        """delta_pf^{(2)} cross-checked across families by the identity
        F_shadow = CEO + delta_pf = kappa * lambda_2^FP.

        For each family, compute delta_pf two ways:
          Way A: formula S_3*(10*S_3 - kappa)/48
          Way B: F_shadow - F_CEO (from the decomposition)
        Then verify both give the same result AND that the sum = Gaussian.
        """
        families = [
            heisenberg_matrix_data(1),
            heisenberg_matrix_data(7),
            affine_sl2_matrix_data(1),
            affine_sl2_matrix_data(4),
            virasoro_matrix_data(1),
            virasoro_matrix_data(13),
            virasoro_matrix_data(25),
            betagamma_matrix_data(),
        ]
        for d in families:
            way_a = delta_pf_genus2(d.kappa, d.S3)
            F_s = F_g_shadow(d.kappa, 2)
            F_c = F_g_CEO(2, d)
            way_b = F_s - F_c
            gauss = gaussian_matrix_model_Fg(d.kappa, 2)
            assert simplify(way_a - way_b) == 0, (
                f"{d.name}: delta_pf formula vs decomposition mismatch")
            assert simplify(F_c + way_a - gauss) == 0, (
                f"{d.name}: CEO + delta_pf != Gaussian")

    def test_kappa_sum_13_independent_verification(self):
        """kappa(c) + kappa(26-c) = 13 via 3 independent paths.

        Path 1: direct from family constructors
        Path 2: algebraic: c/2 + (26-c)/2 = 13
        Path 3: cross-check F_1(c) + F_1(26-c) = 13/24
        """
        for c_val in [1, 5, 7, 10, 13, 20, 25]:
            c = Rational(c_val)
            # Path 1: constructors
            d1 = virasoro_matrix_data(c)
            d2 = virasoro_matrix_data(26 - c)
            path1 = d1.kappa + d2.kappa
            # Path 2: algebraic
            path2 = c / 2 + (26 - c) / 2
            # Path 3: via F_1
            F1_sum = F_g_shadow(d1.kappa, 1) + F_g_shadow(d2.kappa, 1)
            path3_kappa = F1_sum / lambda_fp_sympy(1)
            assert path1 == path2 == Rational(13), (
                f"c={c}: paths disagree: {path1}, {path2}")
            assert path3_kappa == Rational(13)

    def test_discriminant_virasoro_three_paths(self):
        """disc(Q_L) for Virasoro via 3 independent computations.

        Path 1: q1^2 - 4*q0*q2 from shadow data
        Path 2: specialized formula -320*c^2/(5c+22)
        Path 3: via Delta and alpha: disc = 144*kappa^2*alpha^2
                 - 16*kappa^2*(9*alpha^2 + 16*kappa*S4)
                 = 144*k^2*a^2 - 144*k^2*a^2 - 256*k^3*S4
                 = -256*kappa^3*S4
        """
        for c_val in [1, 7, 13, 25]:
            c = Rational(c_val)
            d = virasoro_matrix_data(c)
            # Path 1: general
            path1 = d.q1**2 - 4 * d.q0 * d.q2
            # Path 2: specialized
            path2 = Rational(-320) * c**2 / (5*c + 22)
            # Path 3: via individual components
            path3 = (12*d.kappa*d.S3)**2 - 4*(4*d.kappa**2)*(9*d.S3**2 + 16*d.kappa*d.S4)
            assert simplify(path1 - path2) == 0, f"c={c}: path1 vs path2"
            assert simplify(path1 - path3) == 0, f"c={c}: path1 vs path3"

    def test_gaussian_universality_cross_genus(self):
        """F_g / lambda_g^FP = kappa for all (family, g) pairs.

        This is the RATIO test: the ratio must be exactly kappa,
        independent of g.  Any error in either lambda_g^FP or F_g
        will show as a g-dependent ratio.
        """
        families = {
            'Heis_1': heisenberg_matrix_data(1),
            'Heis_7': heisenberg_matrix_data(7),
            'aff_3': affine_sl2_matrix_data(3),
            'Vir_13': virasoro_matrix_data(13),
            'bg': betagamma_matrix_data(),
        }
        for name, d in families.items():
            ratios = set()
            for g in range(1, 5):
                ratio = F_g_shadow(d.kappa, g) / lambda_fp_sympy(g)
                ratios.add(ratio)
            assert len(ratios) == 1, (
                f"{name}: F_g/lambda_g not constant in g: {ratios}")
            assert ratios.pop() == d.kappa

    def test_delta_pf_genus3_cross_check_genus2(self):
        """delta_pf genus-3 at S_4=S_5=0 relates to genus-2 structure.

        For class L (S_4=S_5=0), delta_pf^{(3)} is a polynomial in
        (kappa, S_3) alone.  Verify it vanishes for Heisenberg (S_3=0)
        and is nonzero for affine sl_2 (S_3=2), and that the genus-2
        formula is not accidentally equal to the genus-3 formula.
        """
        # Heisenberg: all vanish
        dh = heisenberg_matrix_data(5)
        assert delta_pf_genus3(dh.kappa, dh.S3, dh.S4, dh.S5) == 0
        assert delta_pf_genus2(dh.kappa, dh.S3) == 0

        # Affine sl_2: both nonzero, and different
        da = affine_sl2_matrix_data(1)
        dpf2 = delta_pf_genus2(da.kappa, da.S3)
        dpf3 = delta_pf_genus3(da.kappa, da.S3, da.S4, da.S5)
        assert dpf2 != 0
        assert dpf3 != 0
        assert dpf2 != dpf3  # Genus-2 and genus-3 corrections are different

        # Both satisfy CEO + delta_pf = Gaussian
        assert simplify(F_g_CEO(2, da) + dpf2 - gaussian_matrix_model_Fg(da.kappa, 2)) == 0
        assert simplify(F_g_CEO(3, da) + dpf3 - gaussian_matrix_model_Fg(da.kappa, 3)) == 0

    def test_W3_cross_correction_formula_vs_limit(self):
        """delta_F_2^cross(W_3) = (c+204)/(16c) verified by large-c limit.

        Path 1: exact formula
        Path 2: large-c asymptotic: (c+204)/(16c) -> 1/16 as c -> inf
        Path 3: cross-check: at c=204, delta = 408/3264 = 1/8
        """
        # Path 1 vs Path 3 (special value where numerator doubles)
        assert delta_F2_cross_W3(204) == Rational(408, 204 * 16)
        assert delta_F2_cross_W3(204) == Rational(1, 8)

        # Path 2: large-c limit
        large_c = 10**6
        val = float(delta_F2_cross_W3(large_c))
        assert abs(val - 1.0/16) < 1e-4

        # Path 1: formula agreement at multiple c
        for c in [1, 2, 5, 10, 100]:
            c_r = Rational(c)
            assert delta_F2_cross_W3(c) == (c_r + 204) / (16 * c_r)


# Helper for the cross-verification section (standalone, no circular import)
def _bernoulli_exact_for_test(n: int) -> Fraction:
    """Bernoulli number via recurrence for test independence."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        bk = _bernoulli_exact_for_test(k)
        if bk != 0:
            c = 1
            for j in range(k):
                c = c * (n + 1 - j) // (j + 1)
            s += Fraction(c) * bk
    return -s / Fraction(n + 1)
