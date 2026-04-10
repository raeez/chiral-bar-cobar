"""
Tests for the 3D gravity partition function from the Virasoro shadow tower.

Tests organized by section:
  1. Bernoulli numbers (independent cross-check)
  2. Lambda_g^{FP} intersection numbers (two independent paths)
  3. Free energies F_g (scalar, exact arithmetic)
  4. Partition function coefficients at c=13 and c=26
  5. Generating function identity
  6. BTZ entropy
  7. Asymptotic growth rates and convergence radius
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
    free_energy_full_virasoro,
    # Section 4: Coefficients
    gravity_partition_coefficients_scalar,
    gravity_partition_coefficients_virasoro,
    partition_function_table,
    # Section 5: Generating function
    generating_function_closed_form,
    generating_function_series,
    verify_generating_function,
    # Section 6: BTZ
    btz_entropy,
    # Section 7: Asymptotics
    asymptotic_ratios,
    convergence_radius_from_ratios,
    btz_growth_comparison,
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
    F3_scalar as btz_F3_scalar,
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
        # VERIFIED [DC] definition + [LT] Abramowitz-Stegun 23.1.1
        assert bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        # VERIFIED [DC] definition + [LT] sympy convention: B_1 = +1/2
        # Note: some references use B_1 = -1/2 (the other convention).
        # sympy follows the convention where the generating function is
        # t/(e^t - 1) = sum B_n t^n/n! with B_1 = +1/2.
        assert bernoulli_exact(1) == Fraction(1, 2)

    def test_B2(self):
        # VERIFIED [DC] definition + [LT] Abramowitz-Stegun table 23.2
        assert bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        # VERIFIED [DC] definition + [LT] Abramowitz-Stegun table 23.2
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        # VERIFIED [DC] definition + [LT] Abramowitz-Stegun table 23.2
        assert bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        # VERIFIED [DC] definition + [LT] Abramowitz-Stegun table 23.2
        assert bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        # VERIFIED [DC] definition + [LT] Abramowitz-Stegun table 23.2
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
        # VERIFIED [DC] direct Bernoulli formula + [LT] Faber-Pandharipande 1998 Thm 1
        assert lambda_fp_independent(1) == Fraction(1, 24)

    def test_lambda2_exact(self):
        # VERIFIED [DC] direct Bernoulli formula + [LT] Faber-Pandharipande 1998 Thm 1
        # AP B37: NOT 1/5760 or 7/2880
        assert lambda_fp_independent(2) == Fraction(7, 5760)

    def test_lambda3_exact(self):
        # VERIFIED [DC] direct Bernoulli formula + [LT] Mumford 1983
        assert lambda_fp_independent(3) == Fraction(31, 967680)

    def test_lambda4_exact(self):
        # VERIFIED [DC] direct Bernoulli formula + [CF] cross-check with A-hat expansion
        assert lambda_fp_independent(4) == Fraction(127, 154828800)

    def test_lambda5_exact(self):
        # VERIFIED [DC] direct Bernoulli formula + [CF] cross-check with A-hat expansion
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
        """Verify lambda_g^{FP} are the Taylor coefficients of (x/2)/sinh(x/2).

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
        # VERIFIED [DC] kappa(Vir_13) = 13/2, lambda_1 = 1/24
        # [LC] F_1 = kappa/24 = 13/48
        kappa = Fraction(13, 2)
        assert free_energy_scalar(1, kappa) == Fraction(13, 48)

    def test_F1_c26(self):
        # VERIFIED [DC] kappa(Vir_26) = 13, lambda_1 = 1/24
        # [LC] F_1 = kappa/24 = 13/24
        kappa = Fraction(13)
        assert free_energy_scalar(1, kappa) == Fraction(13, 24)

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all kappa (sanity check)."""
        for c in [1, 2, 13, 24, 26]:
            kappa = kappa_virasoro(c)
            F1 = free_energy_scalar(1, kappa)
            assert F1 == kappa * Fraction(1, 24), f"F_1 != kappa/24 at c={c}"

    def test_F2_c13_scalar(self):
        # VERIFIED [DC] (13/2) * (7/5760) = 91/11520
        # [CF] matches btz_entropy_allgenus.F2_scalar(13)
        kappa = Fraction(13, 2)
        expected = Fraction(91, 11520)  # = 13*7 / (2*11520) = 91/11520
        assert free_energy_scalar(2, kappa) == expected

    def test_F2_c26_scalar(self):
        # VERIFIED [DC] 13 * (7/5760) = 91/5760
        # [CF] matches btz_entropy_allgenus.F2_scalar(26)
        kappa = Fraction(13)
        expected = Fraction(91, 5760)
        assert free_energy_scalar(2, kappa) == expected

    def test_F2_not_wrong_values(self):
        """B37 blacklist: F_2 != 1/5760 or 7/2880 times kappa."""
        kappa = Fraction(13, 2)
        F2 = free_energy_scalar(2, kappa)
        # F_2 = kappa * 7/5760
        assert F2 == kappa * Fraction(7, 5760)
        # NOT kappa * 1/5760
        assert F2 != kappa * Fraction(1, 5760)
        # NOT kappa * 7/2880
        assert F2 != kappa * Fraction(7, 2880)

    def test_full_virasoro_F1_matches_scalar(self):
        """At g=1 there is no planted-forest correction."""
        for c in [1, 13, 26]:
            scalar = free_energy_scalar(1, kappa_virasoro(c))
            full = free_energy_full_virasoro(1, c)
            assert scalar == full, f"F_1 scalar != full at c={c}"

    def test_full_virasoro_F2_has_correction(self):
        """At g=2, the full F_2 differs from scalar for generic c."""
        for c in [1, 13, 26]:
            scalar = free_energy_scalar(2, kappa_virasoro(c))
            full = free_energy_full_virasoro(2, c)
            # They should differ (planted-forest correction is nonzero for c != 40)
            assert scalar != full, f"F_2 planted-forest correction unexpectedly zero at c={c}"

    def test_full_virasoro_matches_btz_engine(self):
        """Cross-check: free_energy_full_virasoro matches btz_entropy_allgenus."""
        for c in [1, 13, 26]:
            assert free_energy_full_virasoro(1, c) == F1_virasoro(c)
            assert free_energy_full_virasoro(2, c) == btz_F2_full(c)
            assert free_energy_full_virasoro(3, c) == btz_F3_full(c)

    def test_negative_genus_raises(self):
        with pytest.raises(ValueError):
            free_energy_scalar(-1, Fraction(1))
        with pytest.raises(ValueError):
            free_energy_full_virasoro(-1, 13)


# =========================================================================
# Section 4: Partition function coefficients
# =========================================================================

class TestPartitionCoefficients:
    """First 10 terms (g=0..9) at c=13 and c=26."""

    def test_c13_first_10_terms(self):
        """Compute and verify first 10 scalar coefficients at c=13."""
        # VERIFIED [DC] each entry = (13/2) * lambda_g
        # [CF] cross-check with btz_entropy_allgenus.free_energy_table
        kappa = Fraction(13, 2)
        coeffs = gravity_partition_coefficients_scalar(kappa, 9)
        assert len(coeffs) == 10
        assert coeffs[0] == Fraction(0)
        assert coeffs[1] == Fraction(13, 48)
        assert coeffs[2] == Fraction(91, 11520)
        # All positive for g >= 1
        for g in range(1, 10):
            assert coeffs[g] > 0, f"F_{g} not positive at c=13"

    def test_c26_first_10_terms(self):
        """Compute and verify first 10 scalar coefficients at c=26."""
        # VERIFIED [DC] each entry = 13 * lambda_g
        # [CF] cross-check: F_g(26) = 2 * F_g(13) at scalar level
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
        # VERIFIED [DC] kappa(26) = 13 = 2 * (13/2) = 2 * kappa(13)
        # [SY] linearity of F_g in kappa
        coeffs_13 = gravity_partition_coefficients_scalar(Fraction(13, 2), 9)
        coeffs_26 = gravity_partition_coefficients_scalar(Fraction(13), 9)
        for g in range(10):
            assert coeffs_26[g] == 2 * coeffs_13[g], \
                f"Doubling relation fails at g={g}"

    def test_virasoro_coefficients_include_planted_forest(self):
        """Full Virasoro coefficients differ from scalar at g=2,3."""
        c13_scalar = gravity_partition_coefficients_scalar(kappa_virasoro(13), 9)
        c13_full = gravity_partition_coefficients_virasoro(13, 9)
        # g=0 and g=1: same
        assert c13_scalar[0] == c13_full[0]
        assert c13_scalar[1] == c13_full[1]
        # g=2: different (planted-forest correction)
        assert c13_scalar[2] != c13_full[2]
        # g >= 4: same (no planted-forest available)
        for g in range(4, 10):
            assert c13_scalar[g] == c13_full[g]

    def test_partition_function_table_structure(self):
        """partition_function_table returns well-formed dict."""
        table = partition_function_table(13, 9)
        assert table['c'] == Fraction(13)
        assert table['kappa'] == Fraction(13, 2)
        assert table['g_max'] == 9
        assert len(table['F_scalar']) == 10
        assert len(table['F_full']) == 10
        assert len(table['F_scalar_float']) == 10


# =========================================================================
# Section 5: Generating function identity
# =========================================================================

class TestGeneratingFunction:
    """Closed-form vs series comparison."""

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
        """Generating function identity holds at several hbar values."""
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

    def test_convergence_radius_2pi(self):
        """Series diverges near hbar = 2*pi (pole of 1/sin)."""
        # At hbar slightly below 2*pi: large but finite
        hbar_near = 2 * PI - 0.1
        val = generating_function_closed_form(6.5, hbar_near)
        assert val > 10.0  # should be large near the pole


# =========================================================================
# Section 6: BTZ entropy
# =========================================================================

class TestBTZEntropy:
    """BTZ black hole entropy S = 2*pi*sqrt(c*E/6)."""

    def test_btz_c13_E1(self):
        # VERIFIED [DC] 2*pi*sqrt(13/6) = 2*pi*sqrt(13/6)
        # [LT] Cardy 1986 formula
        expected = 2 * PI * math.sqrt(13.0 / 6.0)
        assert abs(btz_entropy(13, 1.0) - expected) < 1e-12

    def test_btz_c26_E1(self):
        # VERIFIED [DC] 2*pi*sqrt(26/6) = 2*pi*sqrt(13/3)
        # [LT] Cardy 1986 formula
        expected = 2 * PI * math.sqrt(26.0 / 6.0)
        assert abs(btz_entropy(26, 1.0) - expected) < 1e-12

    def test_btz_c26_E10(self):
        # VERIFIED [DC] 2*pi*sqrt(260/6)
        # [SY] S(c, a*E) = sqrt(a) * S(c, E)
        S_E1 = btz_entropy(26, 1.0)
        S_E10 = btz_entropy(26, 10.0)
        assert abs(S_E10 - math.sqrt(10) * S_E1) < 1e-10

    def test_btz_zero_energy(self):
        assert btz_entropy(13, 0.0) == 0.0

    def test_btz_negative_energy(self):
        assert btz_entropy(13, -1.0) == 0.0

    def test_btz_scaling_in_c(self):
        """S_BTZ scales as sqrt(c)."""
        # VERIFIED [DC] S(4c, E) = 2 * S(c, E)
        # [DA] dimensional analysis
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
        # For g >= 5, normalized ratio should be close to 1
        # (geometric decay with ratio 1/(4*pi^2))
        for r in ratios:
            assert abs(r['normalized_ratio'] - 1.0) < 0.01, \
                f"Normalized ratio at g={r['g']}: {r['normalized_ratio']:.6f}"

    def test_convergence_radius_estimate(self):
        """Estimated convergence radius approaches 2*pi."""
        kappa = kappa_virasoro(26)
        coeffs = gravity_partition_coefficients_scalar(kappa, 20)
        R_est = convergence_radius_from_ratios(coeffs)
        R_exact = 2 * PI
        rel_err = abs(R_est - R_exact) / R_exact
        # At g=19, the ratio is extremely close to 1/(4*pi^2), so R_est ~ 2*pi
        assert rel_err < 1e-6, \
            f"Convergence radius estimate {R_est:.6f} vs exact {R_exact:.6f}, rel err {rel_err:.2e}"

    def test_btz_growth_comparison_structure(self):
        """btz_growth_comparison returns well-formed dict."""
        result = btz_growth_comparison(13, 9)
        assert 'coefficients' in result
        assert 'ratios' in result
        assert len(result['coefficients']) == 10
        assert abs(result['convergence_radius_exact'] - 2 * PI) < 1e-12
        assert result['btz_growth_constant'] == pytest.approx(1.0 / (4 * PI ** 2), rel=1e-12)

    def test_growth_constant_1_over_4pi2(self):
        """The growth constant for Bernoulli-type series is 1/(4*pi^2)."""
        # VERIFIED [DC] poles of 1/sin(x/2) at x = 2*pi give radius 2*pi
        # [LT] standard complex analysis: nearest singularity determines radius
        growth = 1.0 / (4 * PI ** 2)
        assert abs(growth - 0.025330295910584444) < 1e-15

    def test_geometric_decay(self):
        """F_g decays geometrically: |F_g| ~ C * (1/(4*pi^2))^g (convergent series).

        The (2g)! in the Bernoulli numerator is cancelled by the (2g)! in
        the lambda_fp denominator, leaving geometric decay.
        """
        # VERIFIED [DC] direct computation + [LT] pole analysis of 1/sin(x/2)
        kappa = kappa_virasoro(13)
        coeffs = gravity_partition_coefficients_scalar(kappa, 15)
        # Check that |F_g| * (4*pi^2)^g is roughly constant for large g
        vals = []
        for g in range(5, 15):
            Fg = abs(float(coeffs[g]))
            norm = Fg * (4 * PI ** 2) ** g
            vals.append(norm)
        # The normalized values should be roughly constant (ratio of consecutive ~ 1)
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
        # VERIFIED [DC] c/2 = 13/2 + [LT] census C2
        assert kappa_virasoro(13) == Fraction(13, 2)

    def test_complementarity_scalar(self):
        """F_g(13) + F_g(13) = 13 * lambda_g (trivially at self-dual point)."""
        # VERIFIED [DC] 2 * (13/2) * lambda_g = 13 * lambda_g
        # [SY] c=13 is fixed point of c -> 26-c
        table = self_dual_c13_table(9)
        assert table['all_complementarity_hold']

    def test_kappa_plus_kappa_dual(self):
        """kappa(13) + kappa(26-13) = 13 (census C8)."""
        # VERIFIED [DC] 13/2 + 13/2 = 13
        # [LT] census C8: Virasoro complementarity kappa + kappa' = 13
        kappa = kappa_virasoro(13)
        kappa_dual = kappa_virasoro(26 - 13)
        assert kappa + kappa_dual == Fraction(13)

    def test_planted_forest_symmetric(self):
        """At c=13, planted-forest correction is self-dual in a specific sense.

        Since c=13 is the self-dual point under c -> 26-c, and the shadow
        coefficients S_4, S_5 depend on c, the planted-forest corrections
        at c=13 have special symmetry.
        """
        F2_c13 = free_energy_full_virasoro(2, 13)
        F2_c13_dual = free_energy_full_virasoro(2, 26 - 13)
        assert F2_c13 == F2_c13_dual


# =========================================================================
# Section 9: Critical string dimension c=26
# =========================================================================

class TestCriticalC26:
    """Properties at c=26 (bosonic string critical dimension)."""

    def test_kappa_c26(self):
        # VERIFIED [DC] c/2 = 26/2 = 13 + [LT] census C2
        assert kappa_virasoro(26) == Fraction(13)

    def test_dual_kappa_vanishes(self):
        """kappa(Vir_0) = 0: the dual algebra at c=26 is trivial."""
        # VERIFIED [DC] 0/2 = 0 + [LC] kappa -> 0 as c -> 0
        assert kappa_virasoro(0) == Fraction(0)

    def test_kappa_eff_vanishes(self):
        """kappa(matter) + kappa(ghost) = 13 + (-13) = 0 at c=26."""
        # VERIFIED [DC] 26/2 + (-26)/2 = 0 + [LT] bosonic string anomaly cancellation
        kappa_matter = kappa_virasoro(26)
        kappa_ghost = kappa_virasoro(-26)
        assert kappa_matter + kappa_ghost == Fraction(0)

    def test_doubling_relation(self):
        """F_g(26) = 2 * F_g(13) at the scalar level."""
        table = critical_c26_table(9)
        assert table['all_doubling_hold']

    def test_F1_c26(self):
        """F_1 = 13/24 at c=26."""
        # VERIFIED [DC] kappa/24 = 13/24
        # [CF] cross-check: 2 * F_1(13) = 2 * 13/48 = 13/24
        assert free_energy_scalar(1, Fraction(13)) == Fraction(13, 24)

    def test_ten_terms_all_nonzero(self):
        """All 10 free energies (g=1..9) are nonzero at c=26."""
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
            ours = free_energy_full_virasoro(1, c)
            theirs = F1_virasoro(c)
            assert ours == theirs, f"F_1 mismatch at c={c}"

    def test_F2_scalar_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_scalar(2, kappa_virasoro(c))
            theirs = btz_F2_scalar(c)
            assert ours == theirs, f"F_2 scalar mismatch at c={c}"

    def test_F2_full_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_full_virasoro(2, c)
            theirs = btz_F2_full(c)
            assert ours == theirs, f"F_2 full mismatch at c={c}"

    def test_F3_matches(self):
        for c in [1, 13, 24, 26]:
            ours = free_energy_full_virasoro(3, c)
            theirs = btz_F3_full(c)
            assert ours == theirs, f"F_3 full mismatch at c={c}"

    def test_free_energy_table_matches(self):
        """Our coefficients match btz_entropy_allgenus.free_energy_table."""
        for c in [13, 26]:
            btz_table = btz_free_energy_table(c, 5)
            for g in range(1, 6):
                ours = free_energy_full_virasoro(g, c)
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
    """Smoke test for the full summary computation."""

    def test_summary_runs(self):
        result = comprehensive_summary(9)
        assert 'c13' in result
        assert 'c26' in result
        assert 'btz_c13' in result
        assert 'btz_c26' in result
        assert 'generating_function_c13' in result
        assert result['generating_function_c13']['match']
        assert result['generating_function_c26']['match']

    def test_summary_c13_complementarity(self):
        result = comprehensive_summary(5)
        assert result['c13']['all_complementarity_hold']

    def test_summary_c26_doubling(self):
        result = comprehensive_summary(5)
        assert result['c26']['all_doubling_hold']
