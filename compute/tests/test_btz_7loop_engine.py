r"""Tests for BTZ 7-loop quantum gravity engine.

Tests organized by section:
  1.  Extended Faber-Pandharipande (lambda_6, lambda_7) — exact arithmetic
  2.  Multi-path verification of lambda_6 and lambda_7
  3.  Free energies F_6, F_7 (exact and numerical)
  4.  7-loop partition function and free energy sum
  5.  6-loop and 7-loop explicit entropy corrections
  6.  Full 7-loop entropy expansion
  7.  Convergence analysis at 7 loops
  8.  Shadow growth rate verification
  9.  Borel transform analysis
  10. Large-order / Dingle-Berry relations
  11. Maloney-Witten comparison
  12. Special central charges (c=1, 13, 24, 26) at 7 loops
  13. Complementarity at 7 loops
  14. Area corrections
  15. Resurgence from 7-loop data
  16. Numerical precision diagnostics
  17. Cross-checks with base engine
  18. Multi-path verification synthesis
"""

import pytest
from fractions import Fraction
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from btz_7loop_engine import (
    # Section 1
    LAMBDA_FP_6, LAMBDA_FP_7,
    verify_lambda_6_from_bernoulli, verify_lambda_7_from_bernoulli,
    verify_lambda_6_from_ahat, verify_lambda_from_generating_function,
    # Section 2
    F_6_scalar, F_7_scalar, virasoro_F6, virasoro_F7,
    extended_free_energy_table,
    # Section 3
    shadow_partition_7loop, shadow_free_energy_7loop,
    # Section 4
    explicit_6loop_correction, explicit_7loop_correction,
    entropy_correction_7loop,
    # Section 5
    entropy_7loop_full,
    # Section 6
    convergence_analysis_7loop, shadow_growth_verification,
    # Section 7
    borel_coefficients_7loop, borel_transform_evaluate,
    borel_singularity_analysis, large_order_relation_check,
    # Section 8
    maloney_witten_comparison,
    # Section 9
    btz_c1_7loop, btz_c13_7loop, btz_c24_7loop, btz_c26_7loop,
    special_charges_comparison_7loop,
    # Section 10
    complementarity_7loop,
    # Section 11
    area_corrections_7loop,
    # Section 12
    resurgence_from_7loop,
    # Section 13
    precision_diagnostics,
    # Section 14
    full_7loop_report,
)

from btz_quantum_gravity_engine import (
    lambda_fp,
    _bernoulli_2g,
    _factorial_fraction,
    kappa_virasoro,
    kappa_heisenberg,
    F_g_scalar,
    virasoro_free_energy,
    heisenberg_free_energy,
    bekenstein_hawking_entropy,
    ahat_closed_form,
    scalar_free_energy_sum,
    shadow_convergence_radius,
)

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2


# =========================================================================
# Section 1: Extended Faber-Pandharipande (exact arithmetic)
# =========================================================================

class TestLambdaFP6:
    """Exact lambda_6^FP = 1414477/2678117105664000."""

    def test_exact_value(self):
        assert LAMBDA_FP_6 == Fraction(1414477, 2678117105664000)

    def test_matches_lambda_fp_function(self):
        """lambda_fp(6) from the base engine should match our hardcoded value."""
        assert lambda_fp(6) == LAMBDA_FP_6

    def test_from_bernoulli(self):
        """Independent computation from B_12 = -691/2730."""
        assert verify_lambda_6_from_bernoulli() == LAMBDA_FP_6

    def test_bernoulli_components(self):
        """Verify the components: B_12, 2^11, 12!."""
        B12 = _bernoulli_2g(6)
        assert B12 == Fraction(-691, 2730)
        assert abs(B12) == Fraction(691, 2730)
        assert _factorial_fraction(12) == Fraction(479001600)
        # (2^11 - 1) / 2^11 = 2047/2048
        assert (2 ** 11 - 1) == 2047
        # lambda_6 = 2047/2048 * 691/2730 / 479001600
        expected = Fraction(2047, 2048) * Fraction(691, 2730) / Fraction(479001600)
        assert expected == LAMBDA_FP_6

    def test_positive(self):
        """lambda_6^FP > 0 (AP22: all Bernoulli contributions are positive)."""
        assert LAMBDA_FP_6 > 0

    def test_numerical_value(self):
        """Numerical value ~ 5.28e-10."""
        val = float(LAMBDA_FP_6)
        assert abs(val - 5.281609967721337e-10) < 1e-22


class TestLambdaFP7:
    """Exact lambda_7^FP = 8191/612141052723200."""

    def test_exact_value(self):
        assert LAMBDA_FP_7 == Fraction(8191, 612141052723200)

    def test_matches_lambda_fp_function(self):
        assert lambda_fp(7) == LAMBDA_FP_7

    def test_from_bernoulli(self):
        """Independent computation from B_14 = 7/6."""
        assert verify_lambda_7_from_bernoulli() == LAMBDA_FP_7

    def test_bernoulli_components(self):
        """Verify: B_14 = 7/6, 2^13, 14!."""
        B14 = _bernoulli_2g(7)
        assert B14 == Fraction(7, 6)
        assert _factorial_fraction(14) == Fraction(87178291200)
        # (2^13 - 1) / 2^13 = 8191/8192
        expected = Fraction(8191, 8192) * Fraction(7, 6) / Fraction(87178291200)
        assert expected == LAMBDA_FP_7

    def test_positive(self):
        assert LAMBDA_FP_7 > 0

    def test_numerical_value(self):
        val = float(LAMBDA_FP_7)
        assert abs(val - 1.338090292026833e-11) < 1e-23


# =========================================================================
# Section 2: Multi-path verification of lambda_6, lambda_7
# =========================================================================

class TestMultiPathLambda:
    """Multi-path verification: Bernoulli, A-hat GF, generating function extraction."""

    def test_lambda_6_bernoulli_path(self):
        """Path 1: Bernoulli number formula."""
        assert verify_lambda_6_from_bernoulli() == LAMBDA_FP_6

    def test_lambda_7_bernoulli_path(self):
        assert verify_lambda_7_from_bernoulli() == LAMBDA_FP_7

    def test_lambda_6_ahat_path(self):
        """Path 2: A-hat generating function — 7-term series captures > 99%."""
        data = verify_lambda_6_from_ahat()
        assert data['match'], f"7-term series does not improve sufficiently: ratio={data['improvement']}"

    def test_lambda_6_gf_extraction(self):
        """Path 2b: Generating function extraction for lambda_6."""
        data = verify_lambda_from_generating_function(6)
        assert data['match']

    def test_lambda_7_gf_extraction(self):
        """Path 2b: Generating function extraction for lambda_7."""
        data = verify_lambda_from_generating_function(7)
        assert data['match']

    def test_lambda_6_decay_rate_path(self):
        """Path 3: Decay ratio lambda_6/lambda_5 ~ 1/(2*pi)^2."""
        ratio = float(LAMBDA_FP_6) / float(lambda_fp(5))
        predicted = 1.0 / TWO_PI_SQ
        assert abs(ratio - predicted) / predicted < 0.005  # Within 0.5%

    def test_lambda_7_decay_rate_path(self):
        """Path 3: Decay ratio lambda_7/lambda_6 ~ 1/(2*pi)^2."""
        ratio = float(LAMBDA_FP_7) / float(LAMBDA_FP_6)
        predicted = 1.0 / TWO_PI_SQ
        assert abs(ratio - predicted) / predicted < 0.005

    def test_lambda_6_series_convergence_path(self):
        """Path 4: Series sum through g=6 matches closed form."""
        hbar = 0.5
        c = 24
        kappa = 12.0
        series = sum(kappa * float(lambda_fp(g)) * hbar ** (2 * g) for g in range(1, 7))
        closed = ahat_closed_form(c, hbar)
        # The series through g=6 should be very close
        error = abs(series - closed)
        # Remaining tail: kappa * lambda_7 * hbar^14 + ...
        tail_bound = kappa * float(LAMBDA_FP_7) * hbar ** 14 / (1.0 - 1.0 / TWO_PI_SQ * hbar ** 2)
        assert error < 2 * tail_bound  # Error bounded by twice the tail

    def test_all_lambda_positive(self):
        """All lambda_g^FP are positive for g=1..7."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_lambda_monotone_decreasing(self):
        """lambda_{g+1} < lambda_g for all g=1..6."""
        for g in range(1, 7):
            assert lambda_fp(g + 1) < lambda_fp(g)


# =========================================================================
# Section 3: Free energies F_6, F_7
# =========================================================================

class TestFreeEnergies67:
    """Free energies at genus 6 and 7."""

    def test_F6_scalar_c24(self):
        """F_6^{sc}(Vir_24) = 12 * lambda_6^FP."""
        F6 = F_6_scalar(Fraction(12))
        expected = Fraction(12) * LAMBDA_FP_6
        assert F6 == expected

    def test_F7_scalar_c24(self):
        """F_7^{sc}(Vir_24) = 12 * lambda_7^FP."""
        F7 = F_7_scalar(Fraction(12))
        expected = Fraction(12) * LAMBDA_FP_7
        assert F7 == expected

    def test_F6_c26(self):
        """F_6(Vir_26) = 13 * lambda_6^FP."""
        F6 = virasoro_F6(26)
        expected = Fraction(13) * LAMBDA_FP_6
        assert F6 == expected

    def test_F7_c26(self):
        """F_7(Vir_26) = 13 * lambda_7^FP."""
        F7 = virasoro_F7(26)
        expected = Fraction(13) * LAMBDA_FP_7
        assert F7 == expected

    def test_F6_c13(self):
        """F_6(Vir_13) = (13/2) * lambda_6^FP."""
        F6 = virasoro_F6(13)
        expected = Fraction(13, 2) * LAMBDA_FP_6
        assert F6 == expected

    def test_F7_c1(self):
        """F_7(Vir_1) = (1/2) * lambda_7^FP."""
        F7 = virasoro_F7(1)
        expected = Fraction(1, 2) * LAMBDA_FP_7
        assert F7 == expected

    def test_F6_linear_in_kappa(self):
        """F_6 is linear in kappa (exact arithmetic)."""
        assert F_6_scalar(Fraction(5)) == 5 * F_6_scalar(Fraction(1))

    def test_F7_linear_in_kappa(self):
        """F_7 is linear in kappa (exact arithmetic)."""
        assert F_7_scalar(Fraction(3)) == 3 * F_7_scalar(Fraction(1))

    def test_F6_positive(self):
        """F_6 > 0 for positive kappa (from positive lambda_6)."""
        for kappa in [1, 5, 12, 13]:
            assert F_6_scalar(Fraction(kappa)) > 0

    def test_F7_positive(self):
        for kappa in [1, 5, 12, 13]:
            assert F_7_scalar(Fraction(kappa)) > 0

    def test_F6_smaller_than_F5(self):
        """F_6 < F_5 (monotone decrease from Bernoulli decay)."""
        for c in [1, 13, 24, 26]:
            F5 = float(virasoro_free_energy(c, 5))
            F6 = float(virasoro_F6(c))
            # F_5 is scalar only at genus 5, F_6 is scalar only at genus 6
            # Both use the same kappa, so comparison is valid
            assert F6 < F5

    def test_F7_smaller_than_F6(self):
        for c in [1, 13, 24, 26]:
            F6 = float(virasoro_F6(c))
            F7 = float(virasoro_F7(c))
            assert F7 < F6

    def test_extended_table_length(self):
        table = extended_free_energy_table(24, g_max=7)
        assert len(table) == 7

    def test_extended_table_matches_base_g1_to_5(self):
        """Extended table g=1..5 matches base engine."""
        for c in [1, 13, 24, 26]:
            ext = extended_free_energy_table(c, g_max=7)
            for g in range(1, 6):
                assert ext[g] == virasoro_free_energy(c, g)

    def test_extended_table_g6_g7(self):
        """Extended table g=6,7 matches standalone functions."""
        for c in [1, 13, 24, 26]:
            ext = extended_free_energy_table(c, g_max=7)
            assert ext[6] == virasoro_F6(c)
            assert ext[7] == virasoro_F7(c)

    def test_heisenberg_extended_table(self):
        """Heisenberg: all scalar, no planted-forest at any genus."""
        k = 3
        ext = extended_free_energy_table(k, g_max=7, algebra='heisenberg')
        for g in range(1, 8):
            assert ext[g] == F_g_scalar(Fraction(k), g)


# =========================================================================
# Section 4: 7-loop partition function
# =========================================================================

class TestPartitionFunction7Loop:
    """Z^sh at 7 loops."""

    def test_Z_at_hbar_zero(self):
        """Z^sh(hbar=0) = 1."""
        Z = shadow_partition_7loop(24, hbar=0.0)
        assert abs(Z - 1.0) < 1e-14

    def test_Z_positive(self):
        Z = shadow_partition_7loop(24, hbar=0.5)
        assert Z > 0

    def test_Z_increases_with_hbar(self):
        """Z increases with hbar (F_g > 0)."""
        Z1 = shadow_partition_7loop(24, hbar=0.1)
        Z2 = shadow_partition_7loop(24, hbar=0.5)
        assert Z2 > Z1

    def test_log_Z_equals_free_energy(self):
        hbar = 0.3
        Z = shadow_partition_7loop(24, hbar=hbar)
        F = shadow_free_energy_7loop(24, hbar=hbar)
        assert abs(math.log(Z) - F) < 1e-12

    def test_7loop_scalar_closer_to_closed_form_than_5loop(self):
        """7-loop SCALAR truncation is closer to A-hat closed form than 5-loop scalar.

        The A-hat closed form is the SCALAR generating function.  Virasoro includes
        planted-forest corrections at g=2,3 that shift away from the scalar closed form.
        Compare scalar-only series to see the improved truncation.
        """
        c = 24
        hbar = 1.0
        kappa = 12.0
        F_5_scalar = sum(kappa * float(lambda_fp(g)) * hbar ** (2 * g) for g in range(1, 6))
        F_7_scalar = sum(kappa * float(lambda_fp(g)) * hbar ** (2 * g) for g in range(1, 8))
        closed = ahat_closed_form(c, hbar)
        assert abs(F_7_scalar - closed) < abs(F_5_scalar - closed)

    def test_series_matches_closed_form_high_precision(self):
        """At hbar=0.5, 7 terms give < 10^{-12} error to closed form."""
        c = 26
        hbar = 0.5
        F_7 = shadow_free_energy_7loop(c, hbar=hbar)
        closed = ahat_closed_form(c, hbar)
        # The scalar closed form uses only scalar part; compare accordingly
        kappa = 13.0
        F_scalar = sum(kappa * float(lambda_fp(g)) * hbar ** (2 * g) for g in range(1, 8))
        closed_scalar = kappa * ((hbar / 2.0) / math.sin(hbar / 2.0) - 1.0)
        assert abs(F_scalar - closed_scalar) < 1e-12

    def test_Z_increases_with_c(self):
        """Larger c gives larger Z at fixed hbar."""
        hbar = 0.3
        Z1 = shadow_partition_7loop(1, hbar=hbar)
        Z24 = shadow_partition_7loop(24, hbar=hbar)
        assert Z24 > Z1


# =========================================================================
# Section 5: 6-loop and 7-loop explicit corrections
# =========================================================================

class TestExplicit6Loop:
    """First-ever 6-loop BTZ correction."""

    def test_F6_c24_positive(self):
        data = explicit_6loop_correction(24, 10)
        assert data['F_6_scalar'] > 0

    def test_S6_scaling(self):
        """S_6 = F_6 * epsilon^10."""
        c, M = 24, 100
        data = explicit_6loop_correction(c, M)
        S_BH = bekenstein_hawking_entropy(c, M)
        epsilon = TWO_PI / S_BH
        expected = data['F_6_scalar'] * epsilon ** 10
        assert abs(data['S_6'] - expected) < 1e-30

    def test_S6_small_relative_to_S_BH(self):
        """6-loop correction is tiny for macroscopic BH."""
        c, M = 24, 100
        data = explicit_6loop_correction(c, M)
        S_BH = bekenstein_hawking_entropy(c, M)
        assert abs(data['S_6']) / S_BH < 1e-10

    def test_6loop_exact_fraction(self):
        data = explicit_6loop_correction(24, 10)
        F6_exact = data['F_6_exact']
        assert isinstance(F6_exact, Fraction)
        assert F6_exact == Fraction(12) * LAMBDA_FP_6

    def test_note_says_first(self):
        data = explicit_6loop_correction(24, 10)
        assert 'first' in data['note'].lower()


class TestExplicit7Loop:
    """First-ever 7-loop BTZ correction."""

    def test_F7_c24_positive(self):
        data = explicit_7loop_correction(24, 10)
        assert data['F_7_scalar'] > 0

    def test_S7_scaling(self):
        """S_7 = F_7 * epsilon^12."""
        c, M = 24, 100
        data = explicit_7loop_correction(c, M)
        S_BH = bekenstein_hawking_entropy(c, M)
        epsilon = TWO_PI / S_BH
        expected = data['F_7_scalar'] * epsilon ** 12
        assert abs(data['S_7'] - expected) < 1e-35

    def test_S7_smaller_than_S6(self):
        """7-loop correction < 6-loop correction."""
        c, M = 24, 100
        d6 = explicit_6loop_correction(c, M)
        d7 = explicit_7loop_correction(c, M)
        assert abs(d7['S_7']) < abs(d6['S_6'])

    def test_7loop_exact_fraction(self):
        data = explicit_7loop_correction(26, 10)
        F7_exact = data['F_7_exact']
        assert F7_exact == Fraction(13) * LAMBDA_FP_7


class TestEntropyCorrection7Loop:
    """entropy_correction_7loop for all genera 1..7."""

    def test_genus_1_log_correction(self):
        """S_1 = -(3/2)*log(S_BH/(2*pi))."""
        c, M = 24, 10
        S_BH = bekenstein_hawking_entropy(c, M)
        S_1 = entropy_correction_7loop(c, M, 1)
        expected = -1.5 * math.log(S_BH / TWO_PI)
        assert abs(S_1 - expected) < 1e-12

    def test_genus_2_matches_base(self):
        """S_2 from 7-loop engine matches base engine."""
        c, M = 24, 100
        from btz_quantum_gravity_engine import entropy_correction_genus_g
        S2_base = entropy_correction_genus_g(c, M, 2)
        S2_ext = entropy_correction_7loop(c, M, 2)
        assert abs(S2_base - S2_ext) < 1e-14

    def test_genus_6(self):
        """S_6 = F_6 * epsilon^10."""
        c, M = 24, 100
        S6 = entropy_correction_7loop(c, M, 6)
        S_BH = bekenstein_hawking_entropy(c, M)
        epsilon = TWO_PI / S_BH
        F6 = float(virasoro_F6(c))
        assert abs(S6 - F6 * epsilon ** 10) < 1e-30

    def test_genus_7(self):
        """S_7 = F_7 * epsilon^12."""
        c, M = 26, 100
        S7 = entropy_correction_7loop(c, M, 7)
        S_BH = bekenstein_hawking_entropy(c, M)
        epsilon = TWO_PI / S_BH
        F7 = float(virasoro_F7(c))
        assert abs(S7 - F7 * epsilon ** 12) < 1e-32

    def test_monotone_decrease_g2_to_g7(self):
        """Corrections decrease monotonically |S_g| > |S_{g+1}| for g >= 2."""
        c, M = 24, 100
        for g in range(2, 7):
            Sg = abs(entropy_correction_7loop(c, M, g))
            Sgp1 = abs(entropy_correction_7loop(c, M, g + 1))
            assert Sg > Sgp1, f"|S_{g}| should be > |S_{g+1}|"


# =========================================================================
# Section 6: Full 7-loop entropy expansion
# =========================================================================

class TestFull7LoopEntropy:
    """Full expansion S = S_BH + sum_{g=1}^7 S_g."""

    def test_all_keys_present(self):
        data = entropy_7loop_full(24, 10)
        assert 'S_BH' in data
        assert 'S_1' in data
        assert 'S_6' in data
        assert 'S_7' in data
        assert 'S_total' in data
        assert 'F_table' in data
        assert 'convergent' in data

    def test_total_equals_sum(self):
        data = entropy_7loop_full(24, 10)
        total = data['S_BH']
        for g in range(1, 8):
            total += data[f'S_{g}']
        assert abs(data['S_total'] - total) < 1e-10

    def test_7_loop_close_to_5_loop(self):
        """Adding 6th and 7th loops barely changes the total."""
        c, M = 24, 100
        from btz_quantum_gravity_engine import entropy_all_genera
        data_5 = entropy_all_genera(c, M, g_max=5)
        data_7 = entropy_7loop_full(c, M)
        # The additional corrections should be tiny
        diff = abs(data_7['S_total'] - data_5['S_total'])
        assert diff < 1e-8 * data_5['S_BH']

    def test_F_table_has_7_entries(self):
        data = entropy_7loop_full(24, 10)
        assert len(data['F_table']) == 7

    def test_convergent_for_large_M(self):
        data = entropy_7loop_full(24, 1000)
        assert data['convergent']

    def test_decay_ratios_present(self):
        data = entropy_7loop_full(24, 10)
        assert 'F_decay_ratios' in data
        assert len(data['F_decay_ratios']) >= 5


# =========================================================================
# Section 7: Convergence analysis
# =========================================================================

class TestConvergenceAnalysis:
    """Comprehensive convergence analysis at 7 loops."""

    def test_convergent_condition(self):
        data = convergence_analysis_7loop(24, 100)
        assert data['convergent']
        assert data['epsilon_over_2pi'] < 1.0

    def test_decay_ratios_approach_prediction(self):
        """Actual ratios approach 1/(2*pi)^2."""
        data = convergence_analysis_7loop(24, 100)
        predicted = data['predicted_ratio']
        # Last 3 ratios should be within 1% of prediction
        for r in data['actual_ratios'][-3:]:
            assert r['error'] < 0.01, f"Ratio at g={r['g']} too far from prediction"

    def test_partial_sums_converge(self):
        """Partial sums get progressively closer together."""
        data = convergence_analysis_7loop(24, 100)
        sums = data['partial_sums']
        for i in range(1, len(sums)):
            assert abs(sums[i]['term']) < abs(sums[i - 1]['term'])

    def test_tail_bound_small(self):
        """Truncation error bound is very small for large S_BH."""
        data = convergence_analysis_7loop(24, 1000)
        assert data['tail_relative'] < 1e-20

    def test_corrections_monotonically_decrease(self):
        """Entropy corrections decrease in absolute value for g >= 2."""
        data = convergence_analysis_7loop(24, 100)
        corrs = data['corrections']
        for i in range(2, len(corrs)):
            assert abs(corrs[i]['S_g']) < abs(corrs[i - 1]['S_g'])


# =========================================================================
# Section 8: Shadow growth rate verification
# =========================================================================

class TestShadowGrowthRate:
    """Verify lambda_{g+1}/lambda_g -> 1/(2*pi)^2."""

    def test_growth_verification_output(self):
        data = shadow_growth_verification(7)
        assert 'ratios' in data
        assert len(data['ratios']) == 6  # g=1..6

    def test_converging_at_high_g(self):
        data = shadow_growth_verification(7)
        assert data['converging']

    def test_all_ratios_positive(self):
        data = shadow_growth_verification(7)
        for r in data['ratios']:
            assert r['ratio'] > 0

    def test_ratios_decrease_toward_limit(self):
        """Ratios approach 1/(2*pi)^2 from above."""
        data = shadow_growth_verification(7)
        predicted = data['predicted_ratio']
        errors = [r['relative_error'] for r in data['ratios']]
        # Errors should generally decrease
        assert errors[-1] < errors[0]


# =========================================================================
# Section 9: Borel transform analysis
# =========================================================================

class TestBorelTransform:
    """Borel transform and singularity structure."""

    def test_borel_coefficients_scalar_all_positive(self):
        """Borel coefficients b_g = F_g/(2g-1)! all positive for scalar (Heisenberg).

        For Virasoro, the planted-forest correction can make F_3 negative at c=24.
        The SCALAR coefficients (from Bernoulli decay) are always positive.
        """
        coeffs = borel_coefficients_7loop(1, algebra='heisenberg')
        for g, bg in coeffs.items():
            assert bg > 0, f"Scalar Borel coefficient at g={g} should be positive"

    def test_borel_coefficients_scalar_decrease(self):
        """|b_{g+1}| < |b_g| (super-exponential decay) for scalar."""
        coeffs = borel_coefficients_7loop(1, algebra='heisenberg')
        for g in range(1, 7):
            assert abs(coeffs[g + 1]) < abs(coeffs[g])

    def test_borel_at_zero(self):
        """B(0) = 0."""
        assert abs(borel_transform_evaluate(24, 0.0)) < 1e-14

    def test_borel_small_zeta(self):
        """B(zeta) ~ F_1 * zeta for small zeta."""
        zeta = 0.01
        B = borel_transform_evaluate(24, zeta)
        F1 = float(virasoro_free_energy(24, 1))
        assert abs(B - F1 * zeta) / abs(F1 * zeta) < 0.01

    def test_first_pole_location(self):
        """First Borel singularity at zeta = 2*pi."""
        data = borel_singularity_analysis(24)
        assert abs(data['first_pole_hbar'] - TWO_PI) < 1e-12

    def test_stokes_constant_proportional_to_kappa(self):
        """S_1 = -4*pi^2*kappa."""
        for c in [1, 13, 24, 26]:
            data = borel_singularity_analysis(c)
            kappa = float(kappa_virasoro(c))
            expected = -4.0 * PI ** 2 * kappa
            assert abs(data['stokes_1'] - expected) < 1e-10

    def test_pole_residue_converges_to_1(self):
        """F_g * (2*pi)^{2g} / (2*kappa) -> 1 as g -> infinity."""
        data = borel_singularity_analysis(26)
        ratios = data['pole_residue_ratios']
        # At g=7, should be close to 1
        assert ratios[-1]['deviation_from_1'] < 0.01

    def test_eta_ratios_close_to_1_scalar(self):
        """F_g matches the Dirichlet eta prediction for scalar (Heisenberg).

        The eta formula applies to the SCALAR free energies only.  Virasoro
        includes planted-forest corrections at g=2,3 that break the formula.
        For Heisenberg (class G, S_3=0), all F_g are scalar, and the eta
        prediction is exact.
        """
        data = borel_singularity_analysis(1, algebra='heisenberg')
        for entry in data['eta_ratios']:
            assert abs(entry['ratio'] - 1.0) < 1e-8, \
                f"Eta ratio at g={entry['g']} deviates: {entry['ratio']}"

    def test_eta_ratios_virasoro_g4_plus(self):
        """For Virasoro at g >= 4 (scalar-only), eta formula applies."""
        data = borel_singularity_analysis(24)
        for entry in data['eta_ratios']:
            if entry['g'] >= 4:
                assert abs(entry['ratio'] - 1.0) < 1e-8, \
                    f"Eta ratio at g={entry['g']} deviates"


# =========================================================================
# Section 10: Large-order / Dingle-Berry
# =========================================================================

class TestLargeOrderRelation:
    """Dingle-Berry large-order prediction at 7 loops."""

    def test_eta_formula_at_g7(self):
        """F_7 = 2*kappa/(2*pi)^{14} * eta(14) to high precision."""
        data = large_order_relation_check(26, g_max=7)
        result_g7 = data['results'][6]  # g=7 is index 6
        assert result_g7['eta_error'] < 1e-10

    def test_leading_approximation_improves(self):
        """Leading instanton approximation improves with g."""
        data = large_order_relation_check(24, g_max=7)
        errors = [r['leading_error'] for r in data['results']]
        # Later genera should have smaller leading errors
        assert errors[-1] < errors[0]

    def test_eta_approximation_virasoro_g_ge_4(self):
        """Dirichlet eta matches F_g for Virasoro at g >= 4 (scalar-only genera).

        At g=2,3 the Virasoro planted-forest correction breaks the eta formula.
        At g >= 4, the formula is exact (scalar lane).
        """
        data = large_order_relation_check(26, g_max=7)
        for r in data['results']:
            if r['g'] >= 4:
                assert r['eta_error'] < 1e-8, f"Eta error too large at g={r['g']}"

    def test_large_order_for_heisenberg(self):
        """Large-order relation holds for Heisenberg at ALL genera (class G, no planted forest)."""
        data = large_order_relation_check(1, g_max=7, algebra='heisenberg')
        for r in data['results']:
            assert r['eta_error'] < 1e-8, f"Eta error at g={r['g']}: {r['eta_error']}"


# =========================================================================
# Section 11: Maloney-Witten comparison
# =========================================================================

class TestMaloneyWittenComparison:
    """Shadow tower vs Maloney-Witten."""

    def test_shadow_converges(self):
        data = maloney_witten_comparison(24, 100)
        assert data['shadow_converges']

    def test_mw_diverges(self):
        data = maloney_witten_comparison(24, 100)
        assert data['mw_diverges']

    def test_truncation_error_small(self):
        """7-loop truncation error is small compared to the shadow sum."""
        data = maloney_witten_comparison(24, 100)
        assert data['truncation_relative'] < 1e-6

    def test_np_exponentially_suppressed(self):
        """Non-perturbative MW corrections are exponentially small for large M."""
        data = maloney_witten_comparison(24, 100)
        assert data['mw_np_suppression'] < 1e-100

    def test_Z_shadow_close_to_closed_form(self):
        """Shadow Z close to closed-form A-hat partition function.

        For Virasoro, planted-forest corrections at g=2,3 cause a small
        discrepancy with the scalar A-hat closed form.  For Heisenberg
        (class G, no planted forest), the match is exact.
        """
        # Virasoro: planted-forest shifts by O(S_3) ~ O(1)
        data = maloney_witten_comparison(26, 100)
        if data['Z_closed_form'] is not None:
            rel = abs(data['Z_shadow'] - data['Z_closed_form']) / data['Z_closed_form']
            assert rel < 1e-4  # planted-forest causes ~10^{-5} relative shift

        # Heisenberg: exact match (no planted forest)
        from btz_7loop_engine import extended_free_energy_table
        kappa = 1.0
        S_BH = bekenstein_hawking_entropy(1, 100)
        eps = TWO_PI / S_BH
        F_sum = sum(float(F_g_scalar(Fraction(1), g)) * eps ** (2 * g) for g in range(1, 8))
        closed = kappa * ((eps / 2.0) / math.sin(eps / 2.0) - 1.0)
        assert abs(F_sum - closed) < 1e-12

    def test_c26_shadow_sum(self):
        """At c=26, M=10: shadow free energy is finite and positive."""
        data = maloney_witten_comparison(26, 10)
        assert data['shadow_sum_log'] > 0
        assert math.isfinite(data['shadow_sum_log'])


# =========================================================================
# Section 12: Special central charges at 7 loops
# =========================================================================

class TestSpecialCharges7Loop:
    """c=1, 13, 24, 26 at 7 loops."""

    def test_c1_kappa(self):
        data = btz_c1_7loop(M=10)
        assert abs(data['kappa'] - 0.5) < 1e-12

    def test_c13_self_dual(self):
        """c=13: kappa = 13/2."""
        data = btz_c13_7loop(M=10)
        assert abs(data['kappa'] - 6.5) < 1e-12

    def test_c24_kappa(self):
        data = btz_c24_7loop(M=10)
        assert abs(data['kappa'] - 12.0) < 1e-12

    def test_c26_kappa(self):
        data = btz_c26_7loop(M=10)
        assert abs(data['kappa'] - 13.0) < 1e-12

    def test_all_7_loops_present(self):
        """All special charges have 7 F_g entries."""
        for func in [btz_c1_7loop, btz_c13_7loop, btz_c24_7loop, btz_c26_7loop]:
            data = func(M=10)
            assert len(data['F_table']) == 7

    def test_all_positive_entropy(self):
        """Total entropy positive for M > 0."""
        for func in [btz_c1_7loop, btz_c13_7loop, btz_c24_7loop, btz_c26_7loop]:
            data = func(M=10)
            assert data['S_total'] > 0

    def test_c26_F7_exact(self):
        """F_7(Vir_26) = 13 * 8191/612141052723200 exact."""
        data = btz_c26_7loop(M=10)
        F7_exact = Fraction(13) * LAMBDA_FP_7
        assert abs(data['F_table'][7] - float(F7_exact)) < 1e-22

    def test_c24_F6_exact(self):
        """F_6(Vir_24) = 12 * 1414477/2678117105664000."""
        data = btz_c24_7loop(M=10)
        F6_exact = Fraction(12) * LAMBDA_FP_6
        assert abs(data['F_table'][6] - float(F6_exact)) < 1e-20

    def test_special_charges_comparison(self):
        data = special_charges_comparison_7loop(M=10)
        assert 'c=1' in data
        assert 'c=26' in data

    def test_larger_c_gives_larger_scalar_corrections(self):
        """F_g^{scalar} increases with c (via kappa = c/2) at scalar-only genera.

        At g=2,3 the planted-forest can reverse the ordering (the planted-forest
        for small c is proportionally larger because S_3 is c-independent while
        kappa is small).  At g >= 4, the corrections are purely scalar and
        monotone in kappa.
        """
        data = special_charges_comparison_7loop(M=10)
        for g in [4, 5, 6, 7]:  # scalar-only genera
            F_c1 = data['c=1']['F_table'][g]
            F_c26 = data['c=26']['F_table'][g]
            assert F_c26 > F_c1, f"F_{g}(c=26) should be > F_{g}(c=1)"


# =========================================================================
# Section 13: Complementarity at 7 loops
# =========================================================================

class TestComplementarity7Loop:
    """F_g(c) + F_g(26-c) checks at 7 loops."""

    def test_scalar_sum_g6(self):
        """F_6^{sc}(c) + F_6^{sc}(26-c) = 13 * lambda_6."""
        data = complementarity_7loop(12)
        assert data[6]['scalar_match']

    def test_scalar_sum_g7(self):
        """F_7^{sc}(c) + F_7^{sc}(26-c) = 13 * lambda_7."""
        data = complementarity_7loop(12)
        assert data[7]['scalar_match']

    def test_scalar_sum_multiple_c(self):
        """Scalar complementarity for several c values at g=6,7."""
        for c in [1, 5, 10, 13, 20, 25]:
            data = complementarity_7loop(c)
            for g in [4, 5, 6, 7]:  # g >= 4 is scalar-only
                assert data[g]['scalar_match'], \
                    f"Scalar complementarity fails at c={c}, g={g}"

    def test_kappa_sum_is_13(self):
        """kappa(c) + kappa(26-c) = 13 for all c."""
        for c in range(1, 26):
            data = complementarity_7loop(c)
            assert abs(data['entropy']['kappa_sum'] - 13.0) < 1e-12

    def test_self_dual_c13(self):
        """At c=13: F_g(13) = F_g(13), so sum = 2*F_g(13) = 13*lambda_g."""
        data = complementarity_7loop(13)
        for g in [6, 7]:
            Fg = data[g]['F_g_c']
            assert abs(2 * Fg - data[g]['expected_scalar_sum']) < 1e-20


# =========================================================================
# Section 14: Area corrections
# =========================================================================

class TestAreaCorrections:
    """Bekenstein-Hawking area modifications at each loop order."""

    def test_all_corrections_present(self):
        data = area_corrections_7loop(24, 100)
        for g in range(1, 8):
            assert f'delta_S_{g}' in data
            assert f'delta_A_{g}_over_A' in data

    def test_area_corrections_decrease(self):
        """Higher-loop area corrections are smaller in absolute value."""
        data = area_corrections_7loop(24, 100)
        for g in range(2, 7):
            assert abs(data[f'delta_A_{g}_over_A']) > abs(data[f'delta_A_{g+1}_over_A'])

    def test_quantum_area_close_to_classical(self):
        """Quantum-corrected area is close to classical for large M.

        The one-loop log correction is -(3/2)*log(S_BH/(2*pi)) which is
        non-negligible even at M=1000 for c=24.  Use M=10000 for <1%.
        """
        data = area_corrections_7loop(24, 10000)
        ratio = data['A_quantum_over_A_classical']
        assert abs(ratio - 1.0) < 0.01

    def test_6loop_area_correction_c26(self):
        """Explicit check: delta_A_6/A at c=26, M=100."""
        data = area_corrections_7loop(26, 100)
        # S_6 / S_BH should be extremely small
        assert abs(data['delta_A_6_over_A']) < 1e-10

    def test_7loop_area_correction_c26(self):
        data = area_corrections_7loop(26, 100)
        assert abs(data['delta_A_7_over_A']) < 1e-12


# =========================================================================
# Section 15: Resurgence from 7-loop data
# =========================================================================

class TestResurgence7Loop:
    """Resurgence analysis from 7-loop data."""

    def test_instanton_action(self):
        data = resurgence_from_7loop(24)
        assert abs(data['instanton_action_1'] - TWO_PI_SQ) < 1e-10

    def test_stokes_constant_c26(self):
        """S_1 = -4*pi^2*13 for c=26."""
        data = resurgence_from_7loop(26)
        expected = -4.0 * PI ** 2 * 13.0
        assert abs(data['stokes_constant_1'] - expected) < 1e-8

    def test_borel_summable(self):
        data = resurgence_from_7loop(24)
        assert data['borel_summable']

    def test_median_resummation(self):
        data = resurgence_from_7loop(24)
        assert data['median_resummation']

    def test_action_estimates_converge(self):
        """Instanton action estimates from ratio test converge."""
        data = resurgence_from_7loop(26)
        estimates = data['action_estimates']
        # Later estimates should be closer to (2*pi)^2
        for est in estimates[-3:]:
            ratio = est['F_g/F_{g+1}']
            assert abs(ratio - TWO_PI_SQ) / TWO_PI_SQ < 0.1

    def test_stokes_proportional_to_kappa(self):
        """Stokes constant scales linearly with kappa."""
        data_c1 = resurgence_from_7loop(1)
        data_c26 = resurgence_from_7loop(26)
        ratio = data_c26['stokes_constant_1'] / data_c1['stokes_constant_1']
        kappa_ratio = 13.0 / 0.5
        assert abs(ratio - kappa_ratio) < 1e-6


# =========================================================================
# Section 16: Numerical precision
# =========================================================================

class TestPrecision:
    """Numerical precision diagnostics."""

    def test_exact_vs_float_g6(self):
        data = precision_diagnostics(24)
        assert data[6]['relative_error'] < 1e-14

    def test_exact_vs_float_g7(self):
        data = precision_diagnostics(24)
        assert data[7]['relative_error'] < 1e-14

    def test_exact_vs_float_all_genera(self):
        data = precision_diagnostics(26)
        for g in range(1, 8):
            assert data[g]['relative_error'] < 1e-12

    def test_bit_length_reasonable(self):
        """Exact fractions do not have absurdly large numerator/denominator."""
        data = precision_diagnostics(24)
        for g in range(1, 8):
            assert data[g]['exact_bits'] < 200  # Reasonable bit complexity


# =========================================================================
# Section 17: Cross-checks with base engine
# =========================================================================

class TestCrossChecksWithBase:
    """Consistency between 7-loop engine and base BTZ engine."""

    def test_F1_through_F5_match(self):
        """F_1..F_5 from extended table match base engine exactly."""
        for c in [1, 13, 24, 26]:
            ext = extended_free_energy_table(c, g_max=7)
            for g in range(1, 6):
                assert ext[g] == virasoro_free_energy(c, g), \
                    f"Mismatch at c={c}, g={g}"

    def test_lambda_fp_6_matches_base(self):
        """lambda_fp(6) from base engine matches our LAMBDA_FP_6."""
        assert lambda_fp(6) == LAMBDA_FP_6

    def test_lambda_fp_7_matches_base(self):
        assert lambda_fp(7) == LAMBDA_FP_7

    def test_kappa_consistent(self):
        """kappa values used in 7-loop engine match base."""
        for c in [1, 13, 24, 26]:
            data = entropy_7loop_full(c, 10)
            assert abs(data['kappa'] - float(kappa_virasoro(c))) < 1e-12

    def test_S_BH_consistent(self):
        """S_BH from 7-loop engine matches base."""
        from btz_quantum_gravity_engine import entropy_all_genera
        for c in [1, 13, 24, 26]:
            d7 = entropy_7loop_full(c, 10)
            d5 = entropy_all_genera(c, 10, g_max=5)
            assert abs(d7['S_BH'] - d5['S_BH']) < 1e-12

    def test_entropy_corrections_g1_g5_match(self):
        """Entropy corrections g=1..5 match between engines."""
        from btz_quantum_gravity_engine import entropy_correction_genus_g
        c, M = 24, 100
        for g in range(1, 6):
            S_base = entropy_correction_genus_g(c, M, g)
            S_7loop = entropy_correction_7loop(c, M, g)
            assert abs(S_base - S_7loop) < 1e-14

    def test_convergence_radius_consistent(self):
        """Convergence radius 2*pi matches base engine."""
        assert abs(shadow_convergence_radius() - TWO_PI) < 1e-12

    def test_heisenberg_no_planted_forest(self):
        """Heisenberg: all genera are scalar-only, matching base."""
        k = 5
        ext = extended_free_energy_table(k, g_max=7, algebra='heisenberg')
        for g in range(1, 8):
            F_scalar = F_g_scalar(Fraction(k), g)
            assert ext[g] == F_scalar


# =========================================================================
# Section 18: Multi-path verification synthesis
# =========================================================================

class TestMultiPathSynthesis:
    """Synthesis: verify key results via >= 3 independent paths."""

    def test_F6_c26_three_paths(self):
        """F_6(Vir_26) verified by 3 paths.

        Path 1: Bernoulli formula (exact arithmetic)
        Path 2: Dirichlet eta large-order relation (exact)
        Path 3: Decay ratio prediction from asymptotic analysis
        """
        # Path 1: Bernoulli
        F6_bernoulli = Fraction(13) * verify_lambda_6_from_bernoulli()
        F6_exact = float(F6_bernoulli)

        # Path 2: Dirichlet eta relation: F_g = 2*kappa/(2*pi)^{2g} * eta(2g)
        from btz_7loop_engine import _dirichlet_eta_even
        kappa = 13.0
        eta_12 = _dirichlet_eta_even(6)
        F6_eta = 2.0 * kappa / TWO_PI ** 12 * eta_12
        assert abs(F6_eta - F6_exact) / F6_exact < 1e-10

        # Path 3: Decay ratio
        F5 = float(Fraction(13) * lambda_fp(5))
        F6_decay = F5 / TWO_PI_SQ  # leading-order prediction
        # The decay prediction is asymptotic; at g=6 it's within ~0.5%
        assert abs(F6_decay - F6_exact) / F6_exact < 0.03

    def test_F7_c26_three_paths(self):
        """F_7(Vir_26) verified by 3 paths."""
        # Path 1: Bernoulli
        F7_bernoulli = float(Fraction(13) * verify_lambda_7_from_bernoulli())
        # Path 2: large-order relation (Dirichlet eta)
        kappa = 13.0
        from btz_7loop_engine import _dirichlet_eta_even
        eta_14 = _dirichlet_eta_even(7)
        F7_eta = 2.0 * kappa / TWO_PI ** 14 * eta_14
        assert abs(F7_eta - F7_bernoulli) / F7_bernoulli < 1e-8

        # Path 3: Decay ratio from F_6
        F6 = float(Fraction(13) * LAMBDA_FP_6)
        F7_decay = F6 / TWO_PI_SQ
        assert abs(F7_decay - F7_bernoulli) / F7_bernoulli < 0.03

    def test_entropy_S7_three_paths(self):
        """S_7 at c=26, M=100 verified by 3 paths.

        Path 1: Direct computation S_7 = F_7 * epsilon^12
        Path 2: Dirichlet eta: F_7 = 2*kappa/(2*pi)^{14} * eta(14)
        Path 3: Bernoulli formula: F_7 = kappa * lambda_7^FP
        """
        c, M = 26, 100
        S_BH = bekenstein_hawking_entropy(c, M)
        epsilon = TWO_PI / S_BH
        kappa = 13.0

        # Path 1: direct
        F7_direct = float(Fraction(13) * LAMBDA_FP_7)
        S7_direct = F7_direct * epsilon ** 12

        # Path 2: Dirichlet eta (exact at even integers)
        from btz_7loop_engine import _dirichlet_eta_even
        eta_14 = _dirichlet_eta_even(7)
        F7_eta = 2.0 * kappa / TWO_PI ** 14 * eta_14
        S7_eta = F7_eta * epsilon ** 12
        assert abs(S7_eta - S7_direct) / abs(S7_direct) < 1e-8

        # Path 3: Bernoulli (independent computation)
        F7_bernoulli = float(verify_lambda_7_from_bernoulli()) * kappa
        S7_bernoulli = F7_bernoulli * epsilon ** 12
        assert abs(S7_bernoulli - S7_direct) / abs(S7_direct) < 1e-12

    def test_convergence_three_paths(self):
        """Convergence verified by 3 paths.

        Path 1: F_g decay rate < 1
        Path 2: A-hat radius condition |hbar| < 2*pi
        Path 3: Tail bound from geometric series
        """
        c, M = 24, 100
        data = convergence_analysis_7loop(c, M)

        # Path 1: decay ratios
        for r in data['actual_ratios'][-3:]:
            assert r['actual'] < 1.0

        # Path 2: epsilon < 2*pi
        assert data['epsilon'] < TWO_PI

        # Path 3: tail bound
        assert data['tail_bound'] < 1e-15

    def test_complementarity_three_paths(self):
        """Complementarity F_g(c) + F_g(26-c) = 13*lambda_g at g=6,7.

        Path 1: Direct computation of sums
        Path 2: From linearity of F_g in kappa
        Path 3: From kappa(c) + kappa(26-c) = 13
        """
        c = 10
        c_dual = 16

        for g in [6, 7]:
            # Path 1: direct
            F_c = float(F_g_scalar(kappa_virasoro(c), g))
            F_dual = float(F_g_scalar(kappa_virasoro(c_dual), g))
            sum_direct = F_c + F_dual

            # Path 2: linearity
            kappa_c = float(kappa_virasoro(c))
            kappa_dual = float(kappa_virasoro(c_dual))
            lfp = float(lambda_fp(g))
            sum_linear = (kappa_c + kappa_dual) * lfp

            # Path 3: kappa sum = 13
            sum_kappa = 13.0 * lfp

            assert abs(sum_direct - sum_kappa) < 1e-20
            assert abs(sum_linear - sum_kappa) < 1e-20


# =========================================================================
# Additional robustness tests
# =========================================================================

class TestRobustness:
    """Edge cases and robustness."""

    def test_zero_mass(self):
        """M=0: S_BH = 0, corrections should handle gracefully."""
        data = entropy_7loop_full(24, 0)
        assert 'error' in data

    def test_negative_mass(self):
        """M<0: should return error."""
        data = entropy_7loop_full(24, -1)
        assert 'error' in data

    def test_c_equals_zero(self):
        """c=0: kappa=0, all F_g = 0."""
        for g in range(1, 8):
            assert F_g_scalar(Fraction(0), g) == Fraction(0)

    def test_very_large_c(self):
        """Large c: computations remain finite."""
        data = entropy_7loop_full(10000, 100)
        assert math.isfinite(data['S_total'])
        assert data['S_total'] > 0

    def test_very_large_M(self):
        """Large M: expansion parameter is small, corrections tiny."""
        data = entropy_7loop_full(24, 1e6)
        assert data['convergent']
        assert abs(data['relative_correction']) < 1e-3

    def test_full_report_runs(self):
        """Full 7-loop report runs without error."""
        report = full_7loop_report(24, 10)
        assert 'entropy' in report
        assert 'convergence' in report
        assert 'borel' in report
        assert 'maloney_witten' in report
        assert 'resurgence' in report
        assert 'precision' in report

    def test_heisenberg_7loop(self):
        """Heisenberg at 7 loops: scalar only, all consistent."""
        k = 3
        table = extended_free_energy_table(k, g_max=7, algebra='heisenberg')
        for g in range(1, 8):
            expected = F_g_scalar(Fraction(k), g)
            assert table[g] == expected


class TestDecayRateNumerics:
    """Detailed numerical verification of decay rates."""

    def test_ratio_g5_to_g6(self):
        """lambda_6/lambda_5 numerical value."""
        ratio = float(LAMBDA_FP_6) / float(lambda_fp(5))
        assert abs(ratio - 0.025349) < 0.0001

    def test_ratio_g6_to_g7(self):
        """lambda_7/lambda_6 numerical value."""
        ratio = float(LAMBDA_FP_7) / float(LAMBDA_FP_6)
        assert abs(ratio - 0.025335) < 0.0001

    def test_ratio_monotonically_approaches_limit(self):
        """lambda_{g+1}/lambda_g monotonically approaches 1/(2*pi)^2."""
        predicted = 1.0 / TWO_PI_SQ
        ratios = []
        for g in range(1, 7):
            r = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            ratios.append(r)
        # Errors from predicted should decrease
        errors = [abs(r - predicted) for r in ratios]
        for i in range(1, len(errors)):
            assert errors[i] <= errors[i - 1] * 1.1  # Allow small noise


class TestNumericalValues:
    """Hard-coded numerical verification of key values."""

    def test_F6_c24_numerical(self):
        """F_6(Vir_24) ~ 6.338e-9."""
        F6 = float(virasoro_F6(24))
        assert abs(F6 - 6.337932e-9) < 1e-14

    def test_F7_c24_numerical(self):
        """F_7(Vir_24) ~ 1.606e-10."""
        F7 = float(virasoro_F7(24))
        assert abs(F7 - 1.605708e-10) < 1e-16

    def test_F6_c26_numerical(self):
        """F_6(Vir_26) ~ 6.866e-9."""
        F6 = float(virasoro_F6(26))
        assert abs(F6 - 6.866093e-9) < 1e-14

    def test_F7_c26_numerical(self):
        """F_7(Vir_26) ~ 1.740e-10."""
        F7 = float(virasoro_F7(26))
        assert abs(F7 - 1.739517e-10) < 1e-16

    def test_F6_c13_numerical(self):
        """F_6(Vir_13) ~ 3.433e-9."""
        F6 = float(virasoro_F6(13))
        assert abs(F6 - 3.433046e-9) < 1e-14

    def test_F7_c13_numerical(self):
        """F_7(Vir_13) ~ 8.698e-11."""
        F7 = float(virasoro_F7(13))
        assert abs(F7 - 8.697587e-11) < 1e-16

    def test_F6_c1_numerical(self):
        """F_6(Vir_1) ~ 2.641e-10."""
        F6 = float(virasoro_F6(1))
        assert abs(F6 - 2.640805e-10) < 1e-16

    def test_F7_c1_numerical(self):
        """F_7(Vir_1) ~ 6.690e-12."""
        F7 = float(virasoro_F7(1))
        assert abs(F7 - 6.690451e-12) < 1e-18

    def test_S7_c26_M100(self):
        """S_7 at c=26, M=100: explicit numerical check."""
        c, M = 26, 100
        S_BH = bekenstein_hawking_entropy(c, M)
        epsilon = TWO_PI / S_BH
        F7 = float(virasoro_F7(c))
        S7 = F7 * epsilon ** 12
        # Just verify it's extremely small
        assert abs(S7) < 1e-20
        assert S7 > 0

    def test_borel_coefficient_b7_c26(self):
        """b_7 = F_7 / 13! for c=26."""
        F7 = float(Fraction(13) * LAMBDA_FP_7)
        b7 = F7 / math.factorial(13)
        assert abs(b7 - 2.7935e-20) < 1e-23
