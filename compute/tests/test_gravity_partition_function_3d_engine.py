"""
Tests for finite-window Virasoro coefficient diagnostics.

Tests organized by section:
  1. Bernoulli numbers (independent cross-check)
  2. Lambda_g^{FP} intersection numbers (two independent paths)
  3. Free energies F_g (scalar, exact arithmetic)
  4. Known-window coefficients at c=13 and c=26
  5. Scalar generating function identity
  6. BTZ entropy
  7. Scalar Bernoulli growth rates and radius diagnostics
  8. Complementarity at c=13 (self-dual)
  9. Doubling relation at c=26 (critical string)
 10. Cross-verification with btz_entropy_allgenus
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from gravity_partition_function_3d_engine import (
    # Section 1: Bernoulli
    bernoulli_exact,
    # Section 2: Lambda
    lambda_fp_independent,
    # Section 3: Free energies
    free_energy_scalar,
    free_energy_virasoro_known_window,
    free_energy_full_virasoro,
    # Section 4: Coefficients
    gravity_partition_coefficients_scalar,
    gravity_partition_coefficients_virasoro,
    partition_function_table,
    # Section 5: Generating function
    generating_function_closed_form,
    verify_generating_function,
    # Section 6: BTZ
    btz_entropy,
    # Section 7: Asymptotics
    asymptotic_ratios,
    convergence_radius_from_ratios,
    scalar_convergence_radius_exact,
    btz_growth_comparison,
    virasoro_coefficient_scope,
    # Section 8: c=13
    self_dual_c13_table,
    # Section 9: c=26
    critical_c26_table,
    # Section 10: Summary
    comprehensive_summary,
)

from btz_entropy_allgenus import (
    lambda_fp,
    kappa_virasoro,
    F1_virasoro,
    F2_scalar as btz_F2_scalar,
    F2_full as btz_F2_full,
    F3_full as btz_F3_full,
    free_energy_table as btz_free_energy_table,
)

PI = math.pi


# =========================================================================
# Section 1: Bernoulli numbers
# =========================================================================

class TestBernoulliNumbers:
    """Independent Bernoulli number verification."""

    def test_B0(self):
        assert bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        """The engine follows sympy's Bernoulli convention at n=1."""
        assert bernoulli_exact(1) == Fraction(1, 2)

    def test_B2(self):
        assert bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        assert bernoulli_exact(10) == Fraction(5, 66)

    def test_odd_vanish(self):
        """All odd Bernoulli numbers vanish for n >= 3."""
        for n in [3, 5, 7, 9, 11, 13, 15, 17]:
            assert bernoulli_exact(n) == Fraction(0)

    def test_alternating_sign(self):
        """B_{2k} alternates sign for k >= 1."""
        for k in range(1, 10):
            B = bernoulli_exact(2 * k)
            expected_sign = (-1) ** (k + 1)
            actual_sign = 1 if B > 0 else -1
            assert actual_sign == expected_sign, f"B_{2*k} = {B} has wrong sign"


# =========================================================================
# Section 2: Lambda_g^{FP} intersection numbers
# =========================================================================

class TestLambdaFP:
    """Faber-Pandharipande intersection numbers: two independent computations."""

    def test_lambda1_exact(self):
        assert lambda_fp_independent(1) == Fraction(1, 24)

    def test_lambda2_exact(self):
        assert lambda_fp_independent(2) == Fraction(7, 5760)

    def test_lambda3_exact(self):
        assert lambda_fp_independent(3) == Fraction(31, 967680)

    def test_lambda4_exact(self):
        assert lambda_fp_independent(4) == Fraction(127, 154828800)

    def test_lambda5_exact(self):
        assert lambda_fp_independent(5) == Fraction(73, 3503554560)

    def test_cross_verification_with_canonical(self):
        """Independent implementation matches the canonical lambda_fp."""
        for g in range(1, 11):
            assert lambda_fp_independent(g) == lambda_fp(g), \
                f"Mismatch at g={g}: independent={lambda_fp_independent(g)}, canonical={lambda_fp(g)}"

    def test_all_positive(self):
        """lambda_g^{FP} > 0 for all g >= 1 (Bernoulli sign pitfall)."""
        for g in range(1, 15):
            assert lambda_fp_independent(g) > 0

    def test_strictly_decreasing(self):
        """lambda_g^{FP} is strictly decreasing."""
        for g in range(1, 14):
            assert lambda_fp_independent(g) > lambda_fp_independent(g + 1)

    def test_ahat_expansion_coefficients(self):
        """Verify the Wick-rotated A-hat coefficients.

        A-hat(x) = (x/2)/sinh(x/2) = 1 - lambda_1 * x^2 + lambda_2 * x^4 - ...

        After Wick rotation x -> ix:
        (x/2)/sin(x/2) = 1 + lambda_1 * x^2 + lambda_2 * x^4 + ...
        """
        # Evaluate at x = 0.5 (well within convergence radius 2*pi)
        x = 0.5
        # Closed form
        closed = (x / 2.0) / math.sin(x / 2.0)
        # Series: 1 + sum_{g=1}^{20} lambda_g * x^{2g}
        series = 1.0
        for g in range(1, 21):
            series += float(lambda_fp_independent(g)) * x ** (2 * g)
        assert abs(closed - series) < 1e-12, \
            f"A-hat identity failed: closed={closed}, series={series}"


# =========================================================================
# Section 3: Free energies F_g
# =========================================================================

class TestFreeEnergies:
    """Exact free energy computations."""

    def test_F0_is_zero(self):
        """F_0 = 0 by convention (regularized)."""
        assert free_energy_scalar(0, Fraction(13, 2)) == Fraction(0)

    def test_F1_c13(self):
        kappa = Fraction(13, 2)
        assert free_energy_scalar(1, kappa) == Fraction(13, 48)

    def test_F1_c26(self):
        kappa = Fraction(13)
        assert free_energy_scalar(1, kappa) == Fraction(13, 24)

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all kappa (sanity check)."""
        for c in [1, 2, 13, 24, 26]:
            kappa = kappa_virasoro(c)
            F1 = free_energy_scalar(1, kappa)
            assert F1 == kappa * Fraction(1, 24), f"F_1 != kappa/24 at c={c}"

    def test_F2_c13_scalar(self):
        kappa = Fraction(13, 2)
        expected = Fraction(91, 11520)
        assert free_energy_scalar(2, kappa) == expected

    def test_F2_c26_scalar(self):
        kappa = Fraction(13)
        expected = Fraction(91, 5760)
        assert free_energy_scalar(2, kappa) == expected

    def test_F2_not_wrong_values(self):
        """F_2 uses 7/5760, not neighbouring Bernoulli mistakes."""
        kappa = Fraction(13, 2)
        F2 = free_energy_scalar(2, kappa)
        assert F2 == kappa * Fraction(7, 5760)
        assert F2 != kappa * Fraction(1, 5760)
        assert F2 != kappa * Fraction(7, 2880)

    def test_known_virasoro_F1_matches_scalar(self):
        """At g=1 there is no planted-forest correction."""
        for c in [1, 13, 26]:
            scalar = free_energy_scalar(1, kappa_virasoro(c))
            known = free_energy_virasoro_known_window(1, c)
            assert scalar == known, f"F_1 scalar != known-window value at c={c}"

    def test_known_virasoro_F2_has_correction(self):
        """At g=2, the known Virasoro value differs from scalar for generic c."""
        for c in [1, 13, 26]:
            scalar = free_energy_scalar(2, kappa_virasoro(c))
            known = free_energy_virasoro_known_window(2, c)
            assert scalar != known, f"F_2 planted-forest correction vanished at c={c}"

    def test_known_virasoro_matches_btz_engine(self):
        """Known-window values match the canonical local BTZ engine."""
        for c in [1, 13, 26]:
            assert free_energy_virasoro_known_window(1, c) == F1_virasoro(c)
            assert free_energy_virasoro_known_window(2, c) == btz_F2_full(c)
            assert free_energy_virasoro_known_window(3, c) == btz_F3_full(c)

    def test_full_name_wrapper_is_known_window(self):
        """The compatibility wrapper carries known-window values only."""
        assert free_energy_full_virasoro(4, 13) == free_energy_virasoro_known_window(4, 13)
        assert not virasoro_coefficient_scope(4)['full_virasoro_value_known_here']

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            free_energy_scalar(-1, Fraction(1))
        with pytest.raises(ValueError):
            free_energy_virasoro_known_window(-1, 13)


# =========================================================================
# Section 4: Scalar and known-window coefficient tables
# =========================================================================

class TestPartitionCoefficients:
    """First 10 terms (g=0..9) at c=13 and c=26."""

    def test_c13_first_10_terms(self):
        """Compute and verify first 10 scalar coefficients at c=13."""
        kappa = Fraction(13, 2)
        coeffs = gravity_partition_coefficients_scalar(kappa, 9)
        assert len(coeffs) == 10
        assert coeffs[0] == Fraction(0)
        assert coeffs[1] == Fraction(13, 48)
        assert coeffs[2] == Fraction(91, 11520)
        for g in range(1, 10):
            assert coeffs[g] > 0, f"F_{g} not positive at c=13"

    def test_c26_first_10_terms(self):
        """Compute and verify first 10 scalar coefficients at c=26."""
        kappa = Fraction(13)
        coeffs = gravity_partition_coefficients_scalar(kappa, 9)
        assert len(coeffs) == 10
        assert coeffs[0] == Fraction(0)
        assert coeffs[1] == Fraction(13, 24)
        assert coeffs[2] == Fraction(91, 5760)
        for g in range(1, 10):
            assert coeffs[g] > 0, f"F_{g} not positive at c=26"

    def test_c26_is_double_c13(self):
        """F_g^{scalar}(c=26) = 2 * F_g^{scalar}(c=13) for all g."""
        coeffs_13 = gravity_partition_coefficients_scalar(Fraction(13, 2), 9)
        coeffs_26 = gravity_partition_coefficients_scalar(Fraction(13), 9)
        for g in range(10):
            assert coeffs_26[g] == 2 * coeffs_13[g], \
                f"Doubling relation fails at g={g}"

    def test_virasoro_coefficients_include_planted_forest(self):
        """Known-window Virasoro coefficients include only computed corrections."""
        c13_scalar = gravity_partition_coefficients_scalar(kappa_virasoro(13), 9)
        c13_known = gravity_partition_coefficients_virasoro(13, 9)
        assert c13_scalar[0] == c13_known[0]
        assert c13_scalar[1] == c13_known[1]
        assert c13_scalar[2] != c13_known[2]
        assert virasoro_coefficient_scope(2)['includes_planted_forest']
        assert virasoro_coefficient_scope(3)['includes_planted_forest']
        for g in range(4, 10):
            assert c13_scalar[g] == c13_known[g]
            assert not virasoro_coefficient_scope(g)['full_virasoro_value_known_here']

    def test_partition_function_table_structure(self):
        """partition_function_table returns well-formed dict."""
        table = partition_function_table(13, 9)
        assert table['c'] == Fraction(13)
        assert table['kappa'] == Fraction(13, 2)
        assert table['g_max'] == 9
        assert len(table['F_scalar']) == 10
        assert len(table['F_known']) == 10
        assert len(table['F_scope']) == 10
        assert len(table['F_scalar_float']) == 10
        assert 'F_full' not in table


# =========================================================================
# Section 5: Generating function identity
# =========================================================================

class TestGeneratingFunction:
    """Scalar closed-form vs series comparison."""

    def test_identity_c13_hbar_1(self):
        """Generating function identity at c=13, hbar=1."""
        result = verify_generating_function(13, 1.0, 30)
        assert result['match'], \
            f"GF identity failed: diff={result['difference']:.2e}"

    def test_identity_c26_hbar_1(self):
        """Generating function identity at c=26, hbar=1."""
        result = verify_generating_function(26, 1.0, 30)
        assert result['match'], \
            f"GF identity failed: diff={result['difference']:.2e}"

    def test_identity_multiple_hbar(self):
        """Scalar generating function identity holds at several hbar values."""
        for hbar in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0]:
            result = verify_generating_function(13, hbar, 40)
            assert result['difference'] < 1e-6, \
                f"GF identity failed at hbar={hbar}: diff={result['difference']:.2e}"

    def test_closed_form_at_zero(self):
        """Generating function vanishes at hbar=0."""
        assert generating_function_closed_form(6.5, 0.0) == 0.0

    def test_closed_form_linearity_in_kappa(self):
        """The generating function is linear in kappa."""
        hbar = 1.5
        gf_13 = generating_function_closed_form(6.5, hbar)
        gf_26 = generating_function_closed_form(13.0, hbar)
        assert abs(gf_26 - 2 * gf_13) < 1e-12

    def test_scalar_convergence_radius_2pi(self):
        """The scalar ordinary generating function has radius 2*pi."""
        assert scalar_convergence_radius_exact() == pytest.approx(2 * PI, rel=1e-15)
        hbar_near = 2 * PI - 0.1
        val = generating_function_closed_form(6.5, hbar_near)
        assert val > 10.0

    def test_generating_function_scope_excludes_planted_forest(self):
        """The closed-form identity is scalar-lane only."""
        result = verify_generating_function(13, 1.0, 30)
        assert result['scope'] == 'scalar ordinary generating function'
        assert result['includes_planted_forest'] is False


# =========================================================================
# Section 6: BTZ entropy
# =========================================================================

class TestBTZEntropy:
    """BTZ black hole entropy S = 2*pi*sqrt(c*E/6)."""

    def test_btz_c13_E1(self):
        expected = 2 * PI * math.sqrt(13.0 / 6.0)
        assert abs(btz_entropy(13, 1.0) - expected) < 1e-12

    def test_btz_c26_E1(self):
        expected = 2 * PI * math.sqrt(26.0 / 6.0)
        assert abs(btz_entropy(26, 1.0) - expected) < 1e-12

    def test_btz_c26_E10(self):
        S_E1 = btz_entropy(26, 1.0)
        S_E10 = btz_entropy(26, 10.0)
        assert abs(S_E10 - math.sqrt(10) * S_E1) < 1e-10

    def test_btz_zero_energy(self):
        assert btz_entropy(13, 0.0) == 0.0

    def test_btz_negative_energy(self):
        assert btz_entropy(13, -1.0) == 0.0

    def test_btz_scaling_in_c(self):
        """S_BTZ scales as sqrt(c)."""
        S1 = btz_entropy(13, 5.0)
        S4 = btz_entropy(52, 5.0)
        assert abs(S4 - 2 * S1) < 1e-10


# =========================================================================
# Section 7: Asymptotic growth and convergence
# =========================================================================

class TestAsymptotics:
    """Asymptotic growth rate analysis."""

    def test_ratios_converge_to_bernoulli_decay(self):
        """Normalized ratios R_g = |F_{g+1}/F_g| * 4*pi^2 -> 1 as g -> infinity."""
        kappa = kappa_virasoro(13)
        coeffs = gravity_partition_coefficients_scalar(kappa, 20)
        ratios = asymptotic_ratios(coeffs, start_g=5)
        for r in ratios:
            assert abs(r['normalized_ratio'] - 1.0) < 0.01, \
                f"Normalized ratio at g={r['g']}: {r['normalized_ratio']:.6f}"
            assert r['scope'] == 'scalar ordinary generating function'

    def test_convergence_radius_estimate(self):
        """Finite-window scalar radius estimate approaches 2*pi."""
        kappa = kappa_virasoro(26)
        coeffs = gravity_partition_coefficients_scalar(kappa, 20)
        R_est = convergence_radius_from_ratios(coeffs)
        R_exact = scalar_convergence_radius_exact()
        rel_err = abs(R_est - R_exact) / R_exact
        assert rel_err < 1e-6, \
            f"Convergence radius estimate {R_est:.6f} vs exact {R_exact:.6f}, rel err {rel_err:.2e}"

    def test_btz_growth_comparison_structure(self):
        """Growth diagnostics keep scalar exact data separate from estimates."""
        result = btz_growth_comparison(13, 9)
        assert 'coefficients' in result
        assert 'ratios' in result
        assert len(result['coefficients']) == 10
        assert abs(result['scalar_convergence_radius_exact'] - 2 * PI) < 1e-12
        assert result['scalar_growth_constant_exact'] == pytest.approx(1.0 / (4 * PI ** 2), rel=1e-12)
        assert result['radius_estimate_from_window'] != result['scalar_convergence_radius_exact']
        assert 'convergence_radius_exact' not in result
        assert 'btz_growth_constant' not in result

    def test_growth_diagnostics_make_no_borel_or_full_partition_claims(self):
        """The scalar diagnostic surface forbids analytic overclaim fields."""
        result = btz_growth_comparison(13, 12)
        assert result['gevrey_class'] == 0
        assert result['scope'] == 'scalar ordinary generating function'
        assert result['analytic_claims'] == {
            'full_partition_convergence': False,
            'borel_summability': False,
            'btz_closed_form_from_scalar_series': False,
        }

    def test_growth_constant_1_over_4pi2(self):
        """The growth constant for Bernoulli-type series is 1/(4*pi^2)."""
        growth = 1.0 / (4 * PI ** 2)
        assert abs(growth - 0.025330295910584444) < 1e-15

    def test_geometric_decay(self):
        """F_g decays geometrically: |F_g| ~ C * (1/(4*pi^2))^g (convergent series).

        The (2g)! in the Bernoulli numerator is cancelled by the (2g)! in
        the lambda_fp denominator, leaving geometric decay.
        """
        kappa = kappa_virasoro(13)
        coeffs = gravity_partition_coefficients_scalar(kappa, 15)
        vals = []
        for g in range(5, 15):
            Fg = abs(float(coeffs[g]))
            norm = Fg * (4 * PI ** 2) ** g
            vals.append(norm)
        for i in range(len(vals) - 1):
            ratio = vals[i + 1] / vals[i] if vals[i] > 0 else float('inf')
            assert 0.95 < ratio < 1.05, \
                f"Geometric normalization not constant: ratio={ratio:.4f} at g={i+5}"


# =========================================================================
# Section 8: Self-dual point c=13
# =========================================================================

class TestSelfDualC13:
    """Properties at the Virasoro self-dual point c=13."""

    def test_kappa_c13(self):
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_complementarity_scalar(self):
        """F_g(13) + F_g(13) = 13 * lambda_g (trivially at self-dual point)."""
        table = self_dual_c13_table(9)
        assert table['all_complementarity_hold']

    def test_kappa_plus_kappa_partner(self):
        """kappa(13) + kappa(26-13) = 13 (census C8)."""
        kappa = kappa_virasoro(13)
        kappa_partner = kappa_virasoro(26 - 13)
        assert kappa + kappa_partner == Fraction(13)

    def test_planted_forest_symmetric(self):
        """At c=13, the known genus-2 value equals its complementarity partner."""
        F2_c13 = free_energy_virasoro_known_window(2, 13)
        F2_c13_partner = free_energy_virasoro_known_window(2, 26 - 13)
        assert F2_c13 == F2_c13_partner


# =========================================================================
# Section 9: Critical string dimension c=26
# =========================================================================

class TestCriticalC26:
    """Properties at c=26 (bosonic string critical dimension)."""

    def test_kappa_c26(self):
        assert kappa_virasoro(26) == Fraction(13)

    def test_complementarity_partner_kappa_vanishes(self):
        """kappa(Vir_0) = 0 for the c=26 same-family partner."""
        assert kappa_virasoro(0) == Fraction(0)

    def test_kappa_eff_vanishes(self):
        """kappa(matter) + kappa(ghost) = 13 + (-13) = 0 at c=26."""
        kappa_matter = kappa_virasoro(26)
        kappa_ghost = kappa_virasoro(-26)
        assert kappa_matter + kappa_ghost == Fraction(0)

    def test_doubling_relation(self):
        """F_g(26) = 2 * F_g(13) at the scalar level."""
        table = critical_c26_table(9)
        assert table['all_doubling_hold']

    def test_F1_c26(self):
        """F_1 = 13/24 at c=26."""
        assert free_energy_scalar(1, Fraction(13)) == Fraction(13, 24)

    def test_ten_terms_all_nonzero(self):
        """Known-window values through g=9 are nonzero at c=26."""
        coeffs = gravity_partition_coefficients_virasoro(26, 9)
        for g in range(1, 10):
            assert coeffs[g] != Fraction(0), f"F_{g} = 0 at c=26"


# =========================================================================
# Section 10: Cross-verification with btz_entropy_allgenus
# =========================================================================

class TestCrossVerification:
    """Consistency with the canonical btz_entropy_allgenus engine."""

    def test_F1_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_virasoro_known_window(1, c)
            theirs = F1_virasoro(c)
            assert ours == theirs, f"F_1 mismatch at c={c}"

    def test_F2_scalar_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_scalar(2, kappa_virasoro(c))
            theirs = btz_F2_scalar(c)
            assert ours == theirs, f"F_2 scalar mismatch at c={c}"

    def test_F2_known_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_virasoro_known_window(2, c)
            theirs = btz_F2_full(c)
            assert ours == theirs, f"F_2 known-window mismatch at c={c}"

    def test_F3_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_virasoro_known_window(3, c)
            theirs = btz_F3_full(c)
            assert ours == theirs, f"F_3 known-window mismatch at c={c}"

    def test_free_energy_table_matches(self):
        """Known-window coefficients match the canonical local table."""
        for c in [13, 26]:
            btz_table = btz_free_energy_table(c, 5)
            for g in range(1, 6):
                ours = free_energy_virasoro_known_window(g, c)
                theirs = btz_table[g]
                assert ours == theirs, \
                    f"F_{g} mismatch at c={c}: {ours} vs {theirs}"

    def test_lambda_fp_canonical_vs_independent(self):
        """Our independent lambda_fp matches the canonical one for g=1..15."""
        for g in range(1, 16):
            assert lambda_fp_independent(g) == lambda_fp(g)


# =========================================================================
# Section 11: Comprehensive summary smoke test
# =========================================================================

class TestComprehensiveSummary:
    """Smoke test for the finite-window summary computation."""

    def test_summary_runs(self):
        result = comprehensive_summary(9)
        assert 'c13' in result
        assert 'c26' in result
        assert 'scalar_growth_c13' in result
        assert 'scalar_growth_c26' in result
        assert 'btz_c13' not in result
        assert 'btz_c26' not in result
        assert 'generating_function_c13' in result
        assert result['generating_function_c13']['match']
        assert result['generating_function_c26']['match']

    def test_summary_c13_complementarity(self):
        result = comprehensive_summary(5)
        assert result['c13']['all_complementarity_hold']

    def test_summary_c26_doubling(self):
        result = comprehensive_summary(5)
        assert result['c26']['all_doubling_hold']
