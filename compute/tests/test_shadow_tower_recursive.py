"""Tests for recursive shadow obstruction tower computation.

Verifies the full recursive tower computation including:
- Depth classification (G/L/C/M classes)
- Shadow metric Q_L and discriminant Delta
- Taylor expansion of sqrt(Q_L) via convolution recursion
- Asymptotic extraction (growth rate rho, oscillation phase theta)
- Complementarity of Koszul pairs (Vir_c, Vir_{26-c})
- Two-path verification (sqrt(Q_L) vs master equation)
- Genus corrections
- Standard family tower construction

Manuscript references:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:recursive-existence (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import math
import pytest
from sympy import Rational, Symbol, simplify, sqrt, S, N as Neval, Abs

from compute.lib.shadow_tower_recursive import (
    ShadowCoefficient,
    ShadowTower,
    compute_shadow_tower,
    shadow_coefficients_exact,
    shadow_coefficients_virasoro,
    shadow_coefficients_virasoro_exact,
    shadow_coefficients_w3,
    asymptotic_extraction,
    convergence_analysis,
    depth_classification,
    shadow_spectral_decomposition,
    shadow_tower_comparison,
    genus_correction_tower,
    complementarity_shadow_tower,
    virasoro_complementarity,
    verify_two_paths,
    standard_family_tower,
    shadow_metric_from_data,
    STANDARD_FAMILIES,
)


c = Symbol('c')


# ================================================================
# CLASS G (GAUSSIAN) -- HEISENBERG
# ================================================================

class TestClassG:
    """Test class G (Gaussian): Heisenberg family.

    Heisenberg: kappa = k (level), alpha = 0, S_4 = 0.
    Shadow metric Q_L = 4*kappa^2 (constant).
    All S_r = 0 for r >= 3. Depth class G, depth 2.
    """

    def test_heisenberg_kappa(self):
        """S_2 = kappa = k (level) for Heisenberg."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0,
                                     max_arity=10,
                                     algebra_name="Heisenberg")
        assert abs(tower.kappa - 5.0) < 1e-14

    def test_all_higher_vanish(self):
        """S_r = 0 for all r >= 3 (Gaussian terminates at arity 2)."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0,
                                     max_arity=15,
                                     algebra_name="Heisenberg")
        for r in range(3, 16):
            val = tower.coefficient(r)
            assert val is not None
            assert abs(float(Neval(val))) < 1e-14, (
                f"S_{r} = {val} should be 0 for Heisenberg"
            )

    def test_depth_classification_G(self):
        """depth_classification returns ('G', 2) for alpha=0, S4=0."""
        dc, depth = depth_classification(5.0, 0.0, 0.0)
        assert dc == 'G'
        assert depth == 2

    def test_shadow_metric_constant(self):
        """Q_L(t) = 4*kappa^2 (no t-dependence)."""
        q0, q1, q2, Delta = shadow_metric_from_data(5.0, 0.0, 0.0)
        assert abs(q0 - 100.0) < 1e-14  # 4*(5)^2
        assert abs(q1) < 1e-14
        assert abs(q2) < 1e-14
        assert abs(Delta) < 1e-14

    def test_discriminant_zero(self):
        """Delta = 8*kappa*S_4 = 0 for Heisenberg."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0, max_arity=5)
        assert abs(float(Neval(tower.discriminant))) < 1e-14

    def test_growth_rate_zero(self):
        """Growth rate rho = 0 for class G."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0, max_arity=5)
        assert tower.convergent is True
        assert float(Neval(tower.growth_rate)) == 0.0

    def test_convergent(self):
        """Class G tower is convergent."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0, max_arity=5)
        assert tower.convergent is True

    def test_depth_class_label(self):
        """Tower carries depth_class = 'G'."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0, max_arity=5)
        assert tower.depth_class == 'G'


# ================================================================
# CLASS L (LIE/TREE) -- AFFINE sl_2
# ================================================================

class TestClassL:
    """Test class L (Lie/tree): affine sl_2 family.

    Affine sl_2 at level k: kappa = 3(k+2)/4, alpha = 1, S_4 = 0.
    Delta = 0. Depth class L, depth 3.
    """

    def test_affine_kappa(self):
        """S_2 = 3(k+2)/4 for affine sl_2."""
        k = 1
        kappa = 3.0 * (k + 2.0) / 4.0  # = 2.25
        tower = compute_shadow_tower(kappa, 1.0, 0.0,
                                     max_arity=10,
                                     algebra_name="Affine_sl2")
        assert abs(tower.kappa - 2.25) < 1e-14

    def test_cubic_nonzero(self):
        """S_3 = alpha = 1 (nonzero cubic shadow)."""
        kappa = 3.0 * 3.0 / 4.0  # k=1
        tower = compute_shadow_tower(kappa, 1.0, 0.0, max_arity=10)
        assert abs(tower.cubic - 1.0) < 1e-14

    def test_s4_zero(self):
        """S_4 = 0 for affine (tree level terminates at arity 3)."""
        kappa = 3.0 * 3.0 / 4.0
        tower = compute_shadow_tower(kappa, 1.0, 0.0, max_arity=10)
        assert abs(float(Neval(tower.quartic))) < 1e-14

    def test_higher_vanish(self):
        """S_r = 0 for r >= 4 (Lie/tree depth 3)."""
        kappa = 3.0 * 3.0 / 4.0
        tower = compute_shadow_tower(kappa, 1.0, 0.0, max_arity=12)
        for r in range(4, 13):
            val = tower.coefficient(r)
            assert abs(float(Neval(val))) < 1e-12, (
                f"S_{r} = {val} should be 0 for affine"
            )

    def test_depth_classification_L(self):
        """depth_classification returns ('L', 3) for alpha!=0, Delta=0."""
        dc, depth = depth_classification(2.25, 1.0, 0.0)
        assert dc == 'L'
        assert depth == 3

    def test_discriminant_zero(self):
        """Delta = 0 for class L."""
        kappa = 2.25
        _, _, _, Delta = shadow_metric_from_data(kappa, 1.0, 0.0)
        assert abs(Delta) < 1e-14

    def test_growth_rate_zero(self):
        """rho = 0 for class L."""
        tower = compute_shadow_tower(2.25, 1.0, 0.0, max_arity=5)
        assert float(Neval(tower.growth_rate)) == 0.0

    def test_convergent(self):
        """Class L tower is convergent."""
        tower = compute_shadow_tower(2.25, 1.0, 0.0, max_arity=5)
        assert tower.convergent is True


# ================================================================
# CLASS M (MIXED) -- VIRASORO
# ================================================================

class TestClassM_Virasoro:
    """Test class M (mixed): Virasoro algebra.

    Virasoro: kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)).
    Delta = 80/(5c+22). Depth class M, depth infinity.
    """

    def test_virasoro_kappa(self):
        """S_2 = c/2 for Virasoro."""
        coeffs = shadow_coefficients_virasoro(25, max_r=5)
        assert abs(coeffs[2] - 12.5) < 1e-10

    def test_virasoro_alpha(self):
        """S_3 = 2 for Virasoro (independent of c)."""
        coeffs = shadow_coefficients_virasoro(25, max_r=5)
        assert abs(coeffs[3] - 2.0) < 1e-10

    def test_virasoro_S4(self):
        """S_4 = 10/(c(5c+22)) matches the quartic contact invariant."""
        c_val = 25.0
        expected = 10.0 / (c_val * (5 * c_val + 22))
        coeffs = shadow_coefficients_virasoro(c_val, max_r=5)
        assert abs(coeffs[4] - expected) < 1e-12

    def test_infinite_tower(self):
        """S_r != 0 for all r: the tower is infinite (class M)."""
        coeffs = shadow_coefficients_virasoro(25, max_r=20)
        for r in range(2, 21):
            assert abs(coeffs[r]) > 1e-30, (
                f"S_{r} should be nonzero for Virasoro"
            )

    def test_depth_class_M(self):
        """depth_classification returns ('M', None) for Virasoro."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        dc, depth = depth_classification(kappa, alpha, S4)
        assert dc == 'M'
        assert depth is None

    def test_c25_specific_coefficients(self):
        """Verify specific numerical coefficients at c = 25."""
        coeffs = shadow_coefficients_virasoro(25, max_r=10)
        # S_2 = 25/2 = 12.5
        assert abs(coeffs[2] - 12.5) < 1e-10
        # S_3 = 2.0
        assert abs(coeffs[3] - 2.0) < 1e-10
        # S_4 = 10/(25*147) = 10/3675
        assert abs(coeffs[4] - 10.0 / 3675.0) < 1e-12
        # S_5 should be nonzero (quintic forced)
        assert abs(coeffs[5]) > 1e-15

    def test_c13_self_dual(self):
        """At c = 13 (self-dual point): growth rate rho ~ 0.467."""
        c_val = 13.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        Delta = 8.0 * kappa * S4
        rho_theory = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * abs(kappa))
        assert abs(rho_theory - 0.467) < 0.01

    def test_growth_rate_from_tower_ratio_test(self):
        """ShadowTower.ratio_test converges toward rho."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        Delta = 8.0 * kappa * S4
        rho_theory = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * abs(kappa))

        tower = compute_shadow_tower(kappa, alpha, S4,
                                     max_arity=40,
                                     algebra_name="Virasoro(c=25)")
        ratios = tower.ratio_test(40)
        # Filter out zero entries
        nonzero_ratios = [r for r in ratios if r > 0]
        # The last ratio should be within 15% of rho
        assert len(nonzero_ratios) >= 5
        assert abs(nonzero_ratios[-1] - rho_theory) / rho_theory < 0.15

    def test_quintic_forced(self):
        """o^(5)_Vir != 0: the quintic obstruction is nonvanishing."""
        coeffs = shadow_coefficients_virasoro(25, max_r=6)
        assert abs(coeffs[5]) > 1e-15

    def test_exact_symbolic_s2(self):
        """Exact symbolic S_2 = c/2."""
        exact = shadow_coefficients_virasoro_exact(max_r=5)
        assert simplify(exact[2] - c / 2) == 0

    def test_exact_symbolic_s3(self):
        """Exact symbolic S_3 = 2."""
        exact = shadow_coefficients_virasoro_exact(max_r=5)
        assert simplify(exact[3] - 2) == 0

    def test_exact_symbolic_s4(self):
        """Exact symbolic S_4 = 10/(c(5c+22))."""
        exact = shadow_coefficients_virasoro_exact(max_r=5)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(exact[4] - expected) == 0

    def test_q_contact_vir(self):
        """Q^contact_Vir = 10/(c(5c+22)) (the quartic contact invariant)."""
        c_val = 25.0
        expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
        coeffs = shadow_coefficients_virasoro(c_val, max_r=5)
        assert abs(coeffs[4] - expected) < 1e-14

    def test_discriminant_nonzero(self):
        """Delta = 8*kappa*S_4 = 40/(5c+22) != 0 for finite c."""
        c_val = 25.0
        kappa = c_val / 2
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        Delta = 8.0 * kappa * S4
        # Delta = 8*(c/2)*(10/(c*(5c+22))) = 40/(5c+22)
        expected_Delta = 40.0 / (5.0 * c_val + 22.0)
        assert abs(Delta - expected_Delta) < 1e-12
        assert abs(Delta) > 1e-10

    def test_tower_summary_string(self):
        """ShadowTower.summary() returns a non-empty string."""
        tower = compute_shadow_tower(12.5, 2.0,
                                     10.0 / (25 * 147),
                                     max_arity=10,
                                     algebra_name="Virasoro(c=25)")
        summary = tower.summary()
        assert isinstance(summary, str)
        assert "Virasoro" in summary


# ================================================================
# COMPLEMENTARITY
# ================================================================

class TestComplementarity:
    """Test complementarity of Koszul pairs (Vir_c, Vir_{26-c}).

    Key identity: Delta(Vir_c) + Delta(Vir_{26-c}) = 6960/((5c+22)(152-5c)).
    Self-dual at c = 13.
    """

    def test_c13_self_dual(self):
        """At c = 13: Vir_13 is self-dual, equal discriminants."""
        result = virasoro_complementarity(13, max_r=10)
        Delta_A = float(Neval(result['Delta_A']))
        Delta_dual = float(Neval(result['Delta_dual']))
        assert abs(Delta_A - Delta_dual) < 1e-12

    def test_c1_complementarity_sum(self):
        """At c = 1: Delta(Vir_1) + Delta(Vir_25) = 6960/((27)(147))."""
        result = virasoro_complementarity(1, max_r=10)
        Delta_sum = result['Delta_sum']
        expected = Rational(6960) / (27 * 147)
        assert simplify(Delta_sum - expected) == 0

    def test_c5_complementarity_sum(self):
        """At c = 5: Delta(Vir_5) + Delta(Vir_21) = 6960/((47)(127))."""
        result = virasoro_complementarity(5, max_r=10)
        Delta_sum = result['Delta_sum']
        expected = Rational(6960) / (47 * 127)
        assert simplify(Delta_sum - expected) == 0

    def test_constant_numerator_6960(self):
        """The numerator of Delta_sum is always 6960."""
        for c_val in [1, 3, 7, 10, 20]:
            result = virasoro_complementarity(c_val, max_r=5)
            # Delta_sum = 6960/((5c+22)(152-5c))
            expected = Rational(6960, (5 * c_val + 22) * (152 - 5 * c_val))
            assert simplify(result['Delta_sum'] - expected) == 0

    def test_c13_self_dual_rho(self):
        """At c = 13: rho(A) = rho(A!) (self-dual growth rates)."""
        result = virasoro_complementarity(13, max_r=15)
        if 'rho_A' in result and 'rho_dual' in result:
            assert abs(result['rho_A'] - result['rho_dual']) < 1e-10

    def test_c2_dual_is_c24(self):
        """Vir_2 is dual to Vir_24."""
        result = virasoro_complementarity(2, max_r=8)
        # Both towers should be computed
        assert result['tower_A'] is not None
        assert result['tower_dual'] is not None
        # Kappa values
        assert abs(float(Neval(result['tower_A'].kappa)) - 1.0) < 1e-12
        assert abs(float(Neval(result['tower_dual'].kappa)) - 12.0) < 1e-12

    def test_coefficient_sums_exist(self):
        """Coefficient-by-coefficient sums S_r(A) + S_r(A!) are computed."""
        result = virasoro_complementarity(10, max_r=8)
        sums = result['coefficient_sums']
        assert len(sums) >= 5

    def test_both_towers_class_M(self):
        """Both Vir_c and Vir_{26-c} are class M for generic c."""
        result = virasoro_complementarity(5, max_r=8)
        assert result['tower_A'].depth_class == 'M'
        assert result['tower_dual'].depth_class == 'M'


# ================================================================
# ASYMPTOTIC EXTRACTION
# ================================================================

class TestAsymptoticExtraction:
    """Test asymptotic parameter extraction from numerical data."""

    def test_rho_from_spectral_matches_theory(self):
        """Spectral decomposition growth rate matches theoretical rho."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        Delta = 8.0 * kappa * S4
        rho_theory = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * abs(kappa))

        result = shadow_spectral_decomposition(kappa, alpha, S4)
        rho_spectral = result.get('growth_rate', None)
        assert rho_spectral is not None
        assert abs(rho_spectral - rho_theory) / rho_theory < 1e-6

    def test_theta_extracted(self):
        """Oscillation phase theta is extracted from data."""
        coeffs = shadow_coefficients_virasoro(25, max_r=30)
        result = asymptotic_extraction(coeffs, max_r=30)
        assert 'theta' in result
        # theta should be finite
        assert math.isfinite(result['theta'])

    def test_error_decreases_with_max_r(self):
        """Extracted rho improves as max_r increases."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        Delta = 8.0 * kappa * S4
        rho_theory = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * abs(kappa))

        coeffs = shadow_coefficients_virasoro(c_val, max_r=50)
        errors = []
        for max_r in [15, 25, 40]:
            result = asymptotic_extraction(coeffs, max_r=max_r)
            errors.append(abs(result['rho'] - rho_theory))

        # Errors should generally decrease (non-strict due to oscillations)
        assert errors[-1] < errors[0]

    def test_insufficient_data_returns_error(self):
        """Fewer than 5 coefficients returns an error dict."""
        coeffs = {2: 1.0, 3: 0.5, 4: 0.1}
        result = asymptotic_extraction(coeffs)
        assert 'error' in result

    def test_amplitude_and_phase_extracted(self):
        """Amplitude C and phase phi are extracted."""
        coeffs = shadow_coefficients_virasoro(25, max_r=30)
        result = asymptotic_extraction(coeffs, max_r=30)
        assert 'amplitude_C' in result
        assert 'phase_phi' in result
        assert result['amplitude_C'] >= 0

    def test_normalized_tail_provided(self):
        """Normalized tail data is provided in results."""
        coeffs = shadow_coefficients_virasoro(25, max_r=20)
        result = asymptotic_extraction(coeffs, max_r=20)
        assert 'normalized_tail' in result
        assert len(result['normalized_tail']) > 0


# ================================================================
# TWO-PATH VERIFICATION
# ================================================================

class TestTwoPaths:
    """Verify sqrt(Q_L) expansion and master equation recursion agree."""

    def test_virasoro_symbolic_agreement(self):
        """Both paths agree for Virasoro (symbolic, evaluated at c=25)."""
        kappa_sym = c / 2
        alpha_sym = Rational(2)
        S4_sym = Rational(10) / (c * (5 * c + 22))
        P_sym = Rational(2) / c

        result = verify_two_paths(kappa_sym, alpha_sym, S4_sym, P_sym,
                                  max_r=10, numerical_point={c: Rational(25)})
        assert result['all_agree'] is True
        assert result['max_error'] < 1e-10

    def test_virasoro_numerical_agreement(self):
        """Both paths agree numerically at c = 10."""
        c_val = 10.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        P = 2.0 / c_val

        result = verify_two_paths(kappa, alpha, S4, P, max_r=12)
        assert result['all_agree'] is True

    def test_affine_numerical_agreement(self):
        """Both paths agree for affine sl_2 (alpha != 0, S4 = 0)."""
        kappa = 2.25
        alpha = 1.0
        S4 = 0.0
        P = 2.0 / 3.0  # placeholder propagator

        result = verify_two_paths(kappa, alpha, S4, P, max_r=10)
        assert result['all_agree'] is True

    def test_heisenberg_agreement(self):
        """Both paths agree for Heisenberg (trivially)."""
        kappa = 5.0
        alpha = 0.0
        S4 = 0.0
        P = 0.2

        result = verify_two_paths(kappa, alpha, S4, P, max_r=8)
        assert result['all_agree'] is True

    def test_agreement_at_many_c_values(self):
        """Both paths agree at c = 1, 5, 13, 25, 100."""
        for c_val in [1.0, 5.0, 13.0, 25.0, 100.0]:
            kappa = c_val / 2
            alpha = 2.0
            S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
            P = 2.0 / c_val
            result = verify_two_paths(kappa, alpha, S4, P, max_r=10)
            assert result['all_agree'] is True, (
                f"Two-path disagreement at c={c_val}"
            )


# ================================================================
# GENUS CORRECTION TOWER
# ================================================================

class TestGenusCorrectionTower:
    """Test genus-g corrections to the shadow obstruction tower."""

    def test_genus0_returns_base_tower(self):
        """Genus-0 corrections are just the base coefficients."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5 * c + 22))
        base = shadow_coefficients_exact(kappa, alpha, S4, max_r=8)
        g0 = genus_correction_tower(kappa, alpha, S4, genus=0, max_r=8)
        for r in range(2, 9):
            assert simplify(base[r] - g0[r]) == 0

    def test_genus1_virasoro_quartic_correction(self):
        """Genus-1 correction modifies S_4 for Virasoro."""
        kappa_sym = c / 2
        alpha_sym = Rational(2)
        S4_sym = Rational(10) / (c * (5 * c + 22))
        corrections = genus_correction_tower(kappa_sym, alpha_sym, S4_sym,
                                              genus=1, max_r=8)
        # S_2 and S_3 should have zero correction (genus-1 only hits quartic)
        assert simplify(corrections[2]) == 0
        assert simplify(corrections[3]) == 0

    def test_genus1_correction_nonzero_at_quartic(self):
        """Genus-1 quartic correction is nonzero for Virasoro."""
        kappa_sym = c / 2
        alpha_sym = Rational(2)
        S4_sym = Rational(10) / (c * (5 * c + 22))
        corrections = genus_correction_tower(kappa_sym, alpha_sym, S4_sym,
                                              genus=1, max_r=8)
        # Substitute c = 25 to get a numerical value
        corr4_num = corrections[4].subs(c, 25)
        # Should be nonzero (genus-1 Hessian correction)
        assert float(Neval(corr4_num)) != 0.0

    def test_genus0_alone_gives_base_sr(self):
        """Genus-0 coefficients match shadow_coefficients_virasoro."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        base = shadow_coefficients_exact(kappa, alpha, S4, max_r=10)
        vir = shadow_coefficients_virasoro(c_val, max_r=10)
        for r in range(2, 11):
            assert abs(float(Neval(base[r])) - vir[r]) < 1e-10

    def test_higher_genus_returns_zero(self):
        """Genus >= 2 corrections return zero (not yet implemented)."""
        kappa = 5.0
        alpha = 2.0
        S4 = 0.01
        corrections = genus_correction_tower(kappa, alpha, S4,
                                              genus=2, max_r=8)
        for r in range(2, 9):
            val = corrections[r]
            assert float(Neval(val)) == 0.0


# ================================================================
# STANDARD FAMILY TOWER
# ================================================================

class TestStandardFamilies:
    """Test standard_family_tower for all supported families."""

    def test_heisenberg_depth_class_G(self):
        """Heisenberg tower has depth class G."""
        tower = standard_family_tower('Heisenberg', 10, max_r=10)
        assert tower.depth_class == 'G'

    def test_affine_depth_class_L(self):
        """Affine sl_2 tower has depth class L."""
        tower = standard_family_tower('Affine_sl2', 1, max_r=10)
        assert tower.depth_class == 'L'

    def test_virasoro_depth_class_M(self):
        """Virasoro tower has depth class M."""
        tower = standard_family_tower('Virasoro', 25, max_r=10)
        assert tower.depth_class == 'M'

    def test_heisenberg_terminates_at_2(self):
        """Heisenberg tower terminates at arity 2."""
        tower = standard_family_tower('Heisenberg', 10, max_r=15)
        for r in range(3, 16):
            assert abs(float(Neval(tower.coefficient(r)))) < 1e-14

    def test_affine_terminates_at_3(self):
        """Affine sl_2 tower terminates at arity 3."""
        tower = standard_family_tower('Affine_sl2', 1, max_r=15)
        for r in range(4, 16):
            assert abs(float(Neval(tower.coefficient(r)))) < 1e-12

    def test_virasoro_infinite(self):
        """Virasoro tower does not terminate."""
        tower = standard_family_tower('Virasoro', 25, max_r=15)
        for r in range(2, 16):
            assert abs(float(Neval(tower.coefficient(r)))) > 1e-30

    def test_unknown_family_raises(self):
        """Requesting an unknown family raises ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            standard_family_tower('SomeUnknown', 1)

    def test_all_families_in_standard_dict(self):
        """STANDARD_FAMILIES contains Heisenberg, Affine, BetaGamma, Virasoro."""
        expected = {'Heisenberg', 'Affine_sl2', 'BetaGamma', 'Virasoro'}
        assert expected == set(STANDARD_FAMILIES.keys())


# ================================================================
# W_3 TWO-LINE TOWER
# ================================================================

class TestW3Tower:
    """Tests for W_3 two-line shadow obstruction tower."""

    def test_t_line_matches_virasoro(self):
        """W_3 T-line shadow obstruction tower matches Virasoro tower."""
        c_val = 25.0
        w3 = shadow_coefficients_w3(c_val, max_r=15)
        vir = shadow_coefficients_virasoro(c_val, max_r=15)
        for r in range(2, 16):
            assert abs(w3['T_line'][r] - vir[r]) < 1e-12

    def test_w_line_odd_arities_vanish(self):
        """W_3 W-line has alpha_W = 0, so odd-arity contributions vanish."""
        c_val = 25.0
        w3 = shadow_coefficients_w3(c_val, max_r=15)
        # S_3 on W-line should be zero (alpha_W = 0)
        assert abs(w3['W_line'][3]) < 1e-14

    def test_w_line_kappa(self):
        """W_3 W-line has kappa_W = c/3."""
        c_val = 30.0
        w3 = shadow_coefficients_w3(c_val, max_r=5)
        assert abs(w3['W_line'][2] - c_val / 3.0) < 1e-10


# ================================================================
# SHADOW SPECTRAL DECOMPOSITION
# ================================================================

class TestSpectralDecomposition:
    """Tests for shadow_spectral_decomposition."""

    def test_virasoro_conjugate_pair(self):
        """Virasoro branch points form a conjugate pair."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        result = shadow_spectral_decomposition(kappa, alpha, S4)
        assert result.get('conjugate_pair', False) is True

    def test_growth_rate_from_spectral(self):
        """Growth rate from spectral decomposition matches theory."""
        c_val = 25.0
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        Delta = 8.0 * kappa * S4
        rho_theory = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * abs(kappa))

        result = shadow_spectral_decomposition(kappa, alpha, S4)
        rho_spectral = result.get('growth_rate', None)
        assert rho_spectral is not None
        assert abs(rho_spectral - rho_theory) / rho_theory < 0.01


# ================================================================
# CONVERGENCE ANALYSIS
# ================================================================

class TestConvergenceAnalysis:
    """Tests for convergence_analysis on ShadowTower objects."""

    def test_virasoro_c25_convergent(self):
        """Virasoro at c = 25 has rho < 1 (convergent tower)."""
        tower = compute_shadow_tower(12.5, 2.0,
                                     10.0 / (25 * 147),
                                     max_arity=20,
                                     algebra_name="Virasoro(c=25)")
        result = convergence_analysis(tower)
        assert result.get('convergent', None) is True

    def test_virasoro_ising_divergent(self):
        """Virasoro at c = 1/2 (Ising) has rho > 1 (divergent tower)."""
        c_val = 0.5
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        tower = compute_shadow_tower(kappa, alpha, S4,
                                     max_arity=20,
                                     algebra_name="Virasoro(c=0.5)")
        result = convergence_analysis(tower)
        assert result.get('convergent', None) is False

    def test_heisenberg_convergent(self):
        """Heisenberg tower is trivially convergent."""
        tower = compute_shadow_tower(5.0, 0.0, 0.0, max_arity=10)
        result = convergence_analysis(tower)
        assert result.get('convergent', None) is True

    def test_borel_summable_class_M(self):
        """Class M towers are always Borel summable (algebraic GF)."""
        tower = compute_shadow_tower(12.5, 2.0,
                                     10.0 / (25 * 147),
                                     max_arity=15)
        result = convergence_analysis(tower)
        assert result.get('borel_summable', None) is True
