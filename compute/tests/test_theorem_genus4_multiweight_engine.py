r"""Tests for theorem_genus4_multiweight_engine.

Genus-4 multi-weight universality failure: pushing delta_F_g^cross to genus 4.
Multi-path verification per CLAUDE.md mandate.

Multi-path verification:
  Path 1: lambda_4^FP from Akiyama-Tanigawa Bernoulli
  Path 2: lambda_4^FP from standard Bernoulli recurrence
  Path 3: lambda_4^FP from A-hat genus expansion
  Path 4: lambda_4^FP manual derivation from B_8
  Path 5: delta_F_4(W_3) closed-form consistency
  Path 6: delta_F_4(W_3) c-power decomposition
  Path 7: delta_F_4(W_3) positivity (all numerator coefficients positive)
  Path 8: S_6, S_7 three-way cross-verification
  Path 9: Virasoro complementarity at genus 4
  Path 10: W_3 complementarity at genus 4
  Path 11: Depth-class consistency at genus 4
  Path 12: Shadow visibility (S_6, S_7 first at genus 4)
  Path 13: Heisenberg F_4 = k * lambda_4^FP (no corrections)
  Path 14: Cross-genus growth analysis (factorial growth)
  Path 15: Cross-genus lambda_g^FP consistency (g=1..4)
"""

from fractions import Fraction
import pytest

from compute.lib.theorem_genus4_multiweight_engine import (
    # Bernoulli
    _bernoulli,
    _bernoulli_recurrence,
    # Faber-Pandharipande (3 paths)
    lambda_fp,
    lambda_fp_path2,
    lambda_fp_from_ahat,
    # Shadow data
    virasoro_shadow,
    w3_shadow,
    heisenberg_shadow,
    affine_sl2_shadow,
    # Cross-channel corrections
    delta_F2_W3,
    delta_F3_W3,
    delta_F4_W3,
    delta_F4_W3_coefficients,
    delta_F4_W3_from_thm_d_engine,
    delta_F4_W3_decomposition,
    # Free energy decomposition
    genus4_free_energy,
    # A-hat verification
    ahat_verification,
    # Growth analysis
    cross_channel_growth,
    genus4_positivity,
    # Complementarity
    virasoro_complementarity_g4,
    w3_complementarity_g4,
    # Shadow visibility
    shadow_visibility_g4,
    # Depth-class
    depth_class_consistency_g4,
    # S_6, S_7 cross-verification
    virasoro_S6_from_convolution,
    virasoro_S6_from_shadow_metric,
    virasoro_S7_from_convolution,
    virasoro_S7_from_shadow_metric,
    # Comparison table
    genus_comparison_table,
    # Summary
    full_verification_summary,
)


# ============================================================================
# PATH 1-4: lambda_4^FP four-way verification
# ============================================================================

class TestLambda4FP:
    """Four-path verification of lambda_4^FP = 127/154828800."""

    def test_lambda4_fp_value(self):
        """lambda_4^FP = 127/154828800 from Akiyama-Tanigawa."""
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda4_fp_path2(self):
        """lambda_4^FP from standard recurrence matches."""
        assert lambda_fp_path2(4) == Fraction(127, 154828800)

    def test_lambda4_fp_from_ahat(self):
        """lambda_4^FP from A-hat genus expansion matches."""
        assert lambda_fp_from_ahat(4) == Fraction(127, 154828800)

    def test_all_three_paths_agree(self):
        """All three independent paths give the same lambda_4^FP."""
        v1 = lambda_fp(4)
        v2 = lambda_fp_path2(4)
        v3 = lambda_fp_from_ahat(4)
        assert v1 == v2 == v3 == Fraction(127, 154828800)

    def test_bernoulli_B8(self):
        """B_8 = -1/30 (both implementations)."""
        assert _bernoulli(8) == Fraction(-1, 30)
        assert _bernoulli_recurrence(8) == Fraction(-1, 30)

    def test_lambda4_from_B8_manual(self):
        r"""Manual derivation: (2^7-1)/2^7 * |B_8|/8!.

        2^7 = 128, 2^7 - 1 = 127, |B_8| = 1/30, 8! = 40320.
        lambda_4^FP = 127/128 * 1/30 / 40320 = 127/(128*30*40320) = 127/154828800.
        """
        B8 = Fraction(1, 30)
        result = Fraction(127, 128) * B8 / Fraction(40320)
        assert result == Fraction(127, 154828800)

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP positive for g=1..5."""
        for g in range(1, 6):
            assert lambda_fp(g) > 0

    def test_lambda_fp_strictly_decreasing(self):
        """lambda_g^FP is strictly decreasing for g=1..5."""
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_lambda_fp_cross_genus_consistency(self):
        """Cross-check all lambda_g^FP for g=1..4."""
        assert lambda_fp(1) == Fraction(1, 24)
        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp(3) == Fraction(31, 967680)
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_ahat_verification_all_genera(self):
        """A-hat verification passes at all genera 1..5."""
        results = ahat_verification(5)
        for g in range(1, 6):
            assert results[g]['all_agree'], f"A-hat disagreement at g={g}"


# ============================================================================
# PATH 5-7: delta_F_4(W_3) closed-form, decomposition, positivity
# ============================================================================

class TestDeltaF4:
    """Verification of delta_F_4(W_3) closed-form formula."""

    def test_closed_form_c1(self):
        """delta_F_4 at c=1 from closed-form formula."""
        c = Fraction(1)
        num = 287 + 268881 + 115455816 + 29725133760 + 5594347866240
        expected = Fraction(num, 17418240)
        assert delta_F4_W3(c) == expected

    def test_closed_form_c26(self):
        """delta_F_4 at c=26."""
        c = Fraction(26)
        num = (287 * 26**4 + 268881 * 26**3 + 115455816 * 26**2
               + 29725133760 * 26 + 5594347866240)
        den = 17418240 * 26**3
        assert delta_F4_W3(c) == Fraction(num, den)

    def test_engine_matches_closed_c1(self):
        """thm_d_engine formula matches closed-form at c=1."""
        c = Fraction(1)
        assert delta_F4_W3(c) == delta_F4_W3_from_thm_d_engine(c)

    def test_engine_matches_closed_c26(self):
        """thm_d_engine formula matches closed-form at c=26."""
        c = Fraction(26)
        assert delta_F4_W3(c) == delta_F4_W3_from_thm_d_engine(c)

    def test_engine_matches_closed_c50(self):
        """thm_d_engine formula matches closed-form at c=50."""
        c = Fraction(50)
        assert delta_F4_W3(c) == delta_F4_W3_from_thm_d_engine(c)

    def test_engine_matches_closed_c100(self):
        """thm_d_engine formula matches closed-form at c=100."""
        c = Fraction(100)
        assert delta_F4_W3(c) == delta_F4_W3_from_thm_d_engine(c)

    def test_decomposition_matches_formula(self):
        """c-power decomposition sums to the closed-form at c=26."""
        decomp = delta_F4_W3_decomposition(Fraction(26))
        assert decomp['match']

    def test_decomposition_matches_at_multiple_c(self):
        """c-power decomposition matches at multiple c-values."""
        for c_val in [1, 10, 50, 100]:
            decomp = delta_F4_W3_decomposition(Fraction(c_val))
            assert decomp['match'], f"Decomposition mismatch at c={c_val}"

    def test_positivity_all_c(self):
        """delta_F_4 > 0 for all c > 0 (all numerator coefficients positive)."""
        results = genus4_positivity()
        for c_val, is_pos in results.items():
            assert is_pos, f"delta_F_4 not positive at c={c_val}"

    def test_numerator_coefficients_positive(self):
        """All numerator coefficients are positive."""
        coeffs = delta_F4_W3_coefficients()
        assert coeffs['a_4'] > 0
        assert coeffs['a_3'] > 0
        assert coeffs['a_2'] > 0
        assert coeffs['a_1'] > 0
        assert coeffs['a_0'] > 0

    def test_denominator(self):
        """Denominator is 17418240 = 2^11 * 3^5 * 5 * 7."""
        coeffs = delta_F4_W3_coefficients()
        D = coeffs['D']
        assert D == Fraction(17418240)
        # Verify factorization: 2^11 * 3^5 * 5 * 7
        assert 2**11 * 3**5 * 5 * 7 == 17418240

    def test_large_c_leading(self):
        """At large c, delta_F_4 ~ 287c/(17418240) = 41c/2488320."""
        c = Fraction(100000)
        approx = delta_F4_W3(c)
        leading = Fraction(287) * c / 17418240
        ratio = approx / leading
        assert abs(float(ratio) - 1.0) < 0.01


# ============================================================================
# PATH 8: S_6, S_7 three-way cross-verification
# ============================================================================

class TestShadowCoefficients:
    """Three-way verification of Virasoro S_6 and S_7."""

    def test_S6_three_paths_c26(self):
        """S_6 at c=26: shadow dict, convolution, shadow metric all agree."""
        c = Fraction(26)
        vir = virasoro_shadow(c)
        s6_dict = vir['S_6']
        s6_conv = virasoro_S6_from_convolution(c)
        s6_metr = virasoro_S6_from_shadow_metric(c)
        assert s6_dict == s6_conv == s6_metr

    def test_S7_three_paths_c26(self):
        """S_7 at c=26: shadow dict, convolution, shadow metric all agree."""
        c = Fraction(26)
        vir = virasoro_shadow(c)
        s7_dict = vir['S_7']
        s7_conv = virasoro_S7_from_convolution(c)
        s7_metr = virasoro_S7_from_shadow_metric(c)
        assert s7_dict == s7_conv == s7_metr

    def test_S6_three_paths_c1(self):
        """S_6 three-way agreement at c=1."""
        c = Fraction(1)
        vir = virasoro_shadow(c)
        assert vir['S_6'] == virasoro_S6_from_convolution(c)
        assert vir['S_6'] == virasoro_S6_from_shadow_metric(c)

    def test_S7_three_paths_c1(self):
        """S_7 three-way agreement at c=1."""
        c = Fraction(1)
        vir = virasoro_shadow(c)
        assert vir['S_7'] == virasoro_S7_from_convolution(c)
        assert vir['S_7'] == virasoro_S7_from_shadow_metric(c)

    def test_S6_positive(self):
        """S_6 > 0 for all c > 0 (numerator 45c+193 > 0)."""
        for c_val in [1, 10, 26, 50, 100]:
            c = Fraction(c_val)
            assert virasoro_shadow(c)['S_6'] > 0

    def test_S7_negative(self):
        """S_7 < 0 for all c > 0 (prefactor -2880, numerator 15c+61 > 0)."""
        for c_val in [1, 10, 26, 50, 100]:
            c = Fraction(c_val)
            assert virasoro_shadow(c)['S_7'] < 0

    def test_S6_formula_explicit(self):
        """S_6(c=1) = 80*238 / (3*1*729) = 19040/2187."""
        c = Fraction(1)
        expected = Fraction(80) * (45 + 193) / (3 * 1 * (5 + 22) ** 2)
        # 80*238 / (3 * 729) = 19040/2187
        assert expected == Fraction(19040, 2187)
        assert virasoro_shadow(c)['S_6'] == expected

    def test_known_lower_shadows_consistent(self):
        """S_3, S_4, S_5 at c=26 match the known values."""
        c = Fraction(26)
        vir = virasoro_shadow(c)
        assert vir['S_3'] == Fraction(2)
        assert vir['S_4'] == Fraction(10) / (26 * (5 * 26 + 22))
        assert vir['S_5'] == Fraction(-48) / (26 ** 2 * (5 * 26 + 22))


# ============================================================================
# PATH 9-10: Complementarity at genus 4
# ============================================================================

class TestComplementarityG4:
    """Koszul complementarity checks at genus 4."""

    def test_virasoro_scalar_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 at genus 4."""
        result = virasoro_complementarity_g4(Fraction(1))
        assert result['scalar_match']

    def test_virasoro_scalar_complementarity_c13(self):
        """Self-dual point c=13: both kappas equal."""
        result = virasoro_complementarity_g4(Fraction(13))
        assert result['scalar_match']
        assert result['c'] == result['c_dual']

    def test_virasoro_scalar_complementarity_c26(self):
        """c=26: kappa(26) = 13, kappa(0) degenerate -- use c=25 instead."""
        result = virasoro_complementarity_g4(Fraction(25))
        assert result['scalar_match']

    def test_w3_scalar_complementarity(self):
        """W_3 scalar: kappa(c) + kappa(100-c) = 250/3 at genus 4."""
        result = w3_complementarity_g4(Fraction(50))
        assert result['scalar_match']

    def test_w3_cross_channel_dual_pair(self):
        """Cross-channel at c and 100-c: both nonzero and positive."""
        result = w3_complementarity_g4(Fraction(50))
        assert result['cross_c'] > 0
        assert result['cross_dual'] > 0


# ============================================================================
# PATH 11: Depth-class consistency at genus 4
# ============================================================================

class TestDepthClassG4:
    """Depth-class consistency for shadow data at genus 4."""

    def test_class_G_S6_S7_vanish(self):
        """Class G (Heisenberg): S_6 = S_7 = 0."""
        results = depth_class_consistency_g4()
        assert results['G_S6_zero']
        assert results['G_S7_zero']

    def test_class_L_S6_S7_vanish(self):
        """Class L (affine sl_2): S_6 = S_7 = 0."""
        results = depth_class_consistency_g4()
        assert results['L_S6_zero']
        assert results['L_S7_zero']

    def test_class_M_S6_S7_nonzero(self):
        """Class M (Virasoro): S_6 and S_7 both nonzero."""
        results = depth_class_consistency_g4()
        assert results['M_S6_nonzero']
        assert results['M_S7_nonzero']


# ============================================================================
# PATH 12: Shadow visibility at genus 4
# ============================================================================

class TestShadowVisibilityG4:
    """Shadow visibility genus check at genus 4."""

    def test_S6_first_at_g4(self):
        """S_6 is nonzero for Virasoro (first visible at g=4)."""
        results = shadow_visibility_g4()
        assert results['S6_nonzero_virasoro']

    def test_S7_first_at_g4(self):
        """S_7 is nonzero for Virasoro (first visible at g=4)."""
        results = shadow_visibility_g4()
        assert results['S7_nonzero_virasoro']

    def test_S6_S7_zero_for_heisenberg(self):
        """Heisenberg: S_6 = S_7 = 0 (class G, all shadows vanish)."""
        results = shadow_visibility_g4()
        assert results['S6_zero_heisenberg']
        assert results['S7_zero_heisenberg']

    def test_g_min_values(self):
        """g_min(S_6) = 4, g_min(S_7) = 4, g_min(S_8) = 5."""
        results = shadow_visibility_g4()
        assert results['g_min_S6'] == 4
        assert results['g_min_S7'] == 4
        assert results['g_min_S8'] == 5


# ============================================================================
# PATH 13: Heisenberg F_4 = k * lambda_4^FP
# ============================================================================

class TestHeisenbergG4:
    """Heisenberg at genus 4: F_4 = k * lambda_4^FP, no corrections."""

    def test_heisenberg_k1(self):
        """F_4(H_1) = 1 * 127/154828800."""
        result = genus4_free_energy('Heisenberg', Fraction(1))
        assert result['is_uniform_weight']
        assert result['delta_cross'] == 0
        assert result['total_F4'] == Fraction(127, 154828800)

    def test_heisenberg_k_general(self):
        """F_4(H_k) = k * lambda_4^FP for k = 1, 2, 5, 10."""
        fp4 = Fraction(127, 154828800)
        for k_val in [1, 2, 5, 10]:
            k = Fraction(k_val)
            result = genus4_free_energy('Heisenberg', k)
            assert result['total_F4'] == k * fp4, (
                f"Heisenberg at k={k}: F_4 = {result['total_F4']} "
                f"!= k*lambda_4 = {k * fp4}"
            )

    def test_heisenberg_zero_corrections(self):
        """Heisenberg has zero cross-channel correction at all genera 2-4."""
        k = Fraction(1)
        result = genus4_free_energy('Heisenberg', k)
        assert result['delta_cross'] == Fraction(0)
        assert result['scalar_F4'] == result['total_F4']


# ============================================================================
# PATH 14: Cross-genus growth analysis
# ============================================================================

class TestGrowthAnalysis:
    """Cross-genus growth analysis of delta_F_g^cross(W_3)."""

    def test_cross_channel_increasing_with_genus(self):
        """delta_F_{g+1}^cross > delta_F_g^cross for all tested c-values."""
        results = cross_channel_growth()
        for c_val, data in results.items():
            assert data['delta_F3'] > data['delta_F2'], (
                f"At c={c_val}: delta_F_3 <= delta_F_2"
            )
            assert data['delta_F4'] > data['delta_F3'], (
                f"At c={c_val}: delta_F_4 <= delta_F_3"
            )

    def test_cross_over_scalar_ratio_increases(self):
        """Cross-channel/scalar ratio increases with genus at c >= 10."""
        results = cross_channel_growth()
        for c_val in [10, 26, 50, 100]:
            data = results[c_val]
            r2 = data['cross_over_scalar_g2']
            r3 = data['cross_over_scalar_g3']
            r4 = data['cross_over_scalar_g4']
            assert r3 > r2, (
                f"At c={c_val}: cross/scalar ratio should increase g2->g3"
            )
            assert r4 > r3, (
                f"At c={c_val}: cross/scalar ratio should increase g3->g4"
            )

    def test_growth_ratio_data_valid(self):
        """Growth ratios F4/F3 and F3/F2 are well-defined and positive."""
        results = cross_channel_growth()
        for c_val, data in results.items():
            assert data['ratio_F3_F2'] is not None and data['ratio_F3_F2'] > 0
            assert data['ratio_F4_F3'] is not None and data['ratio_F4_F3'] > 0


# ============================================================================
# PATH 15: Cross-genus lambda_g^FP consistency
# ============================================================================

class TestCrossGenusConsistency:
    """Cross-genus consistency of lambda_g^FP and the correction tower."""

    def test_genus2_baseline(self):
        """delta_F_2(W_3) = (c+204)/(16c) at c=50."""
        c = Fraction(50)
        assert delta_F2_W3(c) == Fraction(254, 800)

    def test_genus3_baseline(self):
        """delta_F_3(W_3) from closed-form at c=26."""
        c = Fraction(26)
        num = 5 * 26**3 + 3792 * 26**2 + 1149120 * 26 + 217071360
        expected = Fraction(num, 138240 * 26**2)
        assert delta_F3_W3(c) == expected

    def test_w3_nonuniform_at_all_genera(self):
        """W_3 has nonzero cross-channel at all genera 2, 3, 4."""
        c = Fraction(50)
        assert delta_F2_W3(c) > 0
        assert delta_F3_W3(c) > 0
        assert delta_F4_W3(c) > 0

    def test_comparison_table_valid(self):
        """Genus comparison table produces valid data."""
        table = genus_comparison_table([26, 50])
        for c_val in [26, 50]:
            assert table[c_val]['g2_cross'] > 0
            assert table[c_val]['g3_cross'] > 0
            assert table[c_val]['g4_cross'] > 0
            assert table[c_val]['g4_to_g3_cross_ratio'] is not None

    def test_virasoro_uniform_all_genera(self):
        """Virasoro is uniform-weight: delta_F_g^cross = 0 at all genera."""
        result = genus4_free_energy('Virasoro', Fraction(26))
        assert result['is_uniform_weight']
        assert result['delta_cross'] == 0


# ============================================================================
# Free energy decomposition
# ============================================================================

class TestFreeEnergyDecomposition:
    """Complete genus-4 free energy decomposition for all families."""

    def test_w3_nonuniform(self):
        """W_3 is multi-weight, nonzero cross-channel at genus 4."""
        result = genus4_free_energy('W_3', Fraction(50))
        assert not result['is_uniform_weight']
        assert result['delta_cross'] > 0

    def test_w3_total_F4_positive(self):
        """Total F_4(W_3) is positive for c > 0 (scalar and cross both positive)."""
        for c_val in [1, 10, 26, 50, 100]:
            result = genus4_free_energy('W_3', Fraction(c_val))
            assert result['total_F4'] > 0, f"F_4 not positive at c={c_val}"

    def test_affine_uniform(self):
        """Affine sl_2 is uniform-weight at genus 4."""
        result = genus4_free_energy('affine_sl2', Fraction(1))
        assert result['is_uniform_weight']
        assert result['delta_cross'] == 0


# ============================================================================
# Full verification summary
# ============================================================================

class TestFullVerification:
    """End-to-end verification of all genus-4 computations."""

    def test_full_summary(self):
        """Full verification summary passes all checks."""
        summary = full_verification_summary()
        # lambda_4^FP
        assert summary['lambda_4_FP']['all_agree']
        assert summary['lambda_4_FP']['equals_127_over_154828800']
        # delta_F_4 closed-form vs engine at multiple c
        for c_val in [1, 10, 26, 50]:
            key = f'delta_F4_c{c_val}'
            assert summary[key]['match'], f"Mismatch at c={c_val}"
        # Positivity
        for c_val, pos in summary['positivity'].items():
            assert pos, f"Not positive at c={c_val}"
        # Depth-class
        dc = summary['depth_class']
        assert dc['G_S6_zero']
        assert dc['G_S7_zero']
        assert dc['L_S6_zero']
        assert dc['L_S7_zero']
        assert dc['M_S6_nonzero']
        assert dc['M_S7_nonzero']
        # Shadow visibility
        sv = summary['shadow_visibility']
        assert sv['S6_nonzero_virasoro']
        assert sv['S7_nonzero_virasoro']
        # S_6, S_7 cross-verification
        assert summary['S6_cross']['all_agree']
        assert summary['S7_cross']['all_agree']
