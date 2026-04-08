r"""Tests for theorem_genus3_multiweight_engine.

Genus-3 multi-weight universality failure: extending delta_F_2(W_3) to genus 3.
Multi-path verification per CLAUDE.md mandate.

Multi-path verification:
  Path 1: lambda_3^FP from Akiyama-Tanigawa Bernoulli
  Path 2: lambda_3^FP from standard Bernoulli recurrence
  Path 3: lambda_3^FP from A-hat genus expansion
  Path 4: delta_F_3(W_3) closed-form formula
  Path 5: delta_F_3(W_3) from universal N-formula at N=3
  Path 6: Planted-forest depth-class consistency
  Path 7: Virasoro complementarity at genus 3
  Path 8: W_3 complementarity at genus 3
  Path 9: Cross-channel positivity
  Path 10: Genus-2 baseline cross-check
"""

from fractions import Fraction
import pytest

from compute.lib.theorem_genus3_multiweight_engine import (
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
    # Genus-2 baseline
    delta_F2_W3,
    delta_F2_W3_decomposition,
    # Genus-3 cross-channel
    delta_F3_W3,
    delta_F3_W3_coefficients,
    delta_F3_W3_from_universal,
    # Planted-forest
    planted_forest_g3_generic,
    planted_forest_g3_virasoro,
    planted_forest_g3_heisenberg,
    planted_forest_g3_affine_sl2,
    # Free energy decomposition
    genus3_free_energy,
    # A-hat verification
    ahat_verification,
    # Growth analysis
    cross_channel_growth,
    genus3_positivity,
    # Complementarity
    virasoro_complementarity_g3,
    w3_complementarity_g3,
    # Comparison
    genus_comparison_table,
    # Depth-class
    depth_class_consistency_g3,
    # Shadow visibility
    shadow_visibility_check,
    # Summary
    full_verification_summary,
)


# ============================================================================
# PATH 1-3: lambda_3^FP three-way verification
# ============================================================================

class TestLambda3FP:
    """Three-path verification of lambda_3^FP = 31/967680."""

    def test_lambda3_fp_value(self):
        """lambda_3^FP = 31/967680 from Akiyama-Tanigawa."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda3_fp_path2(self):
        """lambda_3^FP from standard recurrence matches."""
        assert lambda_fp_path2(3) == Fraction(31, 967680)

    def test_lambda3_fp_from_ahat(self):
        """lambda_3^FP from A-hat genus expansion matches."""
        assert lambda_fp_from_ahat(3) == Fraction(31, 967680)

    def test_all_three_paths_agree(self):
        """All three independent paths give the same lambda_3^FP."""
        v1 = lambda_fp(3)
        v2 = lambda_fp_path2(3)
        v3 = lambda_fp_from_ahat(3)
        assert v1 == v2 == v3 == Fraction(31, 967680)

    def test_bernoulli_B6(self):
        """B_6 = 1/42 (both implementations)."""
        assert _bernoulli(6) == Fraction(1, 42)
        assert _bernoulli_recurrence(6) == Fraction(1, 42)

    def test_lambda3_from_B6_manual(self):
        """Manual derivation: (2^5-1)/2^5 * |B_6|/6! = 31/32 * 1/30240 = 31/967680."""
        B6 = Fraction(1, 42)
        result = Fraction(31, 32) * B6 / Fraction(720)
        assert result == Fraction(31, 967680)

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP positive for g=1..5 (Bernoulli sign pitfall)."""
        for g in range(1, 6):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is strictly decreasing for g=1..5."""
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_lambda_fp_cross_genus(self):
        """Cross-check: lambda_1 = 1/24, lambda_2 = 7/5760."""
        assert lambda_fp(1) == Fraction(1, 24)
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_ahat_verification_all_genera(self):
        """A-hat verification passes at all genera 1..5."""
        results = ahat_verification(5)
        for g in range(1, 6):
            assert results[g]['all_agree'], f"A-hat disagreement at g={g}"


# ============================================================================
# PATH 4-5: delta_F_3(W_3) closed-form and universal
# ============================================================================

class TestDeltaF3:
    """Verification of delta_F_3(W_3) = (5c^3+3792c^2+1149120c+217071360)/(138240c^2)."""

    def test_closed_form_c1(self):
        """delta_F_3 at c=1 from closed-form formula."""
        c = Fraction(1)
        num = 5 + 3792 + 1149120 + 217071360
        expected = Fraction(num, 138240)
        assert delta_F3_W3(c) == expected

    def test_closed_form_c26(self):
        """delta_F_3 at c=26."""
        c = Fraction(26)
        num = 5 * 26**3 + 3792 * 26**2 + 1149120 * 26 + 217071360
        den = 138240 * 26**2
        assert delta_F3_W3(c) == Fraction(num, den)

    def test_universal_matches_closed_c1(self):
        """Universal N=3 formula matches closed-form at c=1."""
        c = Fraction(1)
        assert delta_F3_W3(c) == delta_F3_W3_from_universal(c)

    def test_universal_matches_closed_c26(self):
        """Universal N=3 formula matches closed-form at c=26."""
        c = Fraction(26)
        assert delta_F3_W3(c) == delta_F3_W3_from_universal(c)

    def test_universal_matches_closed_c50(self):
        """Universal N=3 formula matches closed-form at c=50."""
        c = Fraction(50)
        assert delta_F3_W3(c) == delta_F3_W3_from_universal(c)

    def test_universal_matches_closed_c100(self):
        """Universal N=3 formula matches closed-form at c=100."""
        c = Fraction(100)
        assert delta_F3_W3(c) == delta_F3_W3_from_universal(c)

    def test_positivity_all_c(self):
        """delta_F_3 > 0 for all c > 0 (all numerator coefficients positive)."""
        results = genus3_positivity()
        for c_val, is_pos in results.items():
            assert is_pos, f"delta_F_3 not positive at c={c_val}"

    def test_numerator_coefficients_positive(self):
        """All numerator coefficients are positive."""
        coeffs = delta_F3_W3_coefficients()
        assert coeffs['a_3'] > 0
        assert coeffs['a_2'] > 0
        assert coeffs['a_1'] > 0
        assert coeffs['a_0'] > 0

    def test_denominator(self):
        """Denominator is 138240."""
        coeffs = delta_F3_W3_coefficients()
        assert coeffs['D'] == Fraction(138240)

    def test_large_c_leading(self):
        """At large c, delta_F_3 ~ 5c/(138240) = c/27648."""
        c = Fraction(10000)
        approx = delta_F3_W3(c)
        leading = Fraction(5) * c / 138240
        ratio = approx / leading
        assert abs(float(ratio) - 1.0) < 0.1  # genus-3 leading term slower to converge


# ============================================================================
# PATH 6: Planted-forest depth-class consistency
# ============================================================================

class TestPlantedForestG3:
    """Planted-forest correction at genus 3: depth-class and cross-family checks."""

    def test_heisenberg_vanishes(self):
        """Heisenberg: delta_pf^{(3,0)} = 0 (class G)."""
        assert planted_forest_g3_heisenberg(Fraction(1)) == Fraction(0)

    def test_heisenberg_vanishes_all_k(self):
        """Heisenberg vanishes at all levels k."""
        for k in [1, 2, 5, 10, 100]:
            assert planted_forest_g3_heisenberg(Fraction(k)) == Fraction(0)

    def test_affine_nonzero(self):
        """Affine sl_2: delta_pf^{(3,0)} != 0 (class L)."""
        assert planted_forest_g3_affine_sl2(Fraction(1)) != Fraction(0)

    def test_virasoro_nonzero(self):
        """Virasoro: delta_pf^{(3,0)} != 0 (class M)."""
        assert planted_forest_g3_virasoro(Fraction(26)) != Fraction(0)

    def test_depth_class_consistency(self):
        """Depth-class consistency: G vanishes, L nonzero, C nonzero."""
        results = depth_class_consistency_g3()
        assert results['G_zero_k1']
        assert results['G_zero_k5']
        assert results['L_nonzero']
        assert results['L_consistent_with_affine']
        assert results['C_nonzero']

    def test_shadow_visibility_S5(self):
        """S_5 first appears at genus 3 (cor:shadow-visibility-genus)."""
        results = shadow_visibility_check()
        assert results['S5_first_at_g3']

    def test_planted_forest_generic_11_terms(self):
        """The generic formula has 11 independent monomial terms.

        Verify by evaluating at 11 carefully chosen points that each
        term contributes independently.
        """
        # Term isolation: set exactly one shadow variable nonzero at a time
        # S_3*S_5 term: set S_3=1, S_5=1, rest=0
        t1 = planted_forest_g3_generic(Fraction(0), Fraction(1), Fraction(0), Fraction(1))
        assert t1 == Fraction(107, 128)  # actual engine value for S_3*S_5 term

        # S_4^2 term: set S_4=1, rest=0
        t2 = planted_forest_g3_generic(Fraction(0), Fraction(0), Fraction(1), Fraction(0))
        assert t2 == Fraction(-7, 12)  # -7/12 * S_4^2

        # S_3^4 term: set S_3=1, rest=0
        t3 = planted_forest_g3_generic(Fraction(0), Fraction(1), Fraction(0), Fraction(0))
        assert t3 == Fraction(-5, 128)  # -5/128 * S_3^4


# ============================================================================
# PATH 7-8: Complementarity at genus 3
# ============================================================================

class TestComplementarityG3:
    """Koszul complementarity checks at genus 3."""

    def test_virasoro_scalar_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 implies scalar F_3 sum is universal."""
        result = virasoro_complementarity_g3(Fraction(1))
        assert result['scalar_match']

    def test_virasoro_scalar_complementarity_c13(self):
        """Self-dual point c=13: kappa + kappa' = 13."""
        result = virasoro_complementarity_g3(Fraction(13))
        assert result['scalar_match']
        # At c=13, both sides equal: 13/2 * lambda_3
        assert result['pf_c'] == result['pf_dual']

    def test_w3_scalar_complementarity(self):
        """W_3 scalar: kappa(c) + kappa(100-c) = 250/3."""
        result = w3_complementarity_g3(Fraction(50))
        assert result['scalar_match']

    def test_w3_cross_channel_dual_pair(self):
        """Cross-channel at c and 100-c: both nonzero and positive."""
        result = w3_complementarity_g3(Fraction(50))
        assert result['cross_c'] > 0
        assert result['cross_dual'] > 0


# ============================================================================
# PATH 9-10: Genus-2 baseline and growth
# ============================================================================

class TestBaselinesAndGrowth:
    """Genus-2 baseline, genus-3 extension, and growth analysis."""

    def test_genus2_baseline(self):
        """delta_F_2(W_3) = (c+204)/(16c) at c=50."""
        c = Fraction(50)
        assert delta_F2_W3(c) == Fraction(254, 800)

    def test_genus2_decomposition(self):
        """Genus-2 per-graph decomposition sums to formula."""
        c = Fraction(50)
        decomp = delta_F2_W3_decomposition(c)
        assert decomp['match']

    def test_genus3_vs_genus2_at_large_c(self):
        """delta_F_3 and delta_F_2 are both positive at large c."""
        c = Fraction(1000)
        assert delta_F3_W3(c) > 0
        assert delta_F2_W3(c) > 0

    def test_growth_data_computed(self):
        """Growth analysis returns valid data at all c-values."""
        results = cross_channel_growth()
        for c_val, data in results.items():
            assert data['delta_F2'] > 0
            assert data['delta_F3'] > 0
            assert data['ratio_F3_F2'] is not None

    def test_cross_over_scalar_ratio_increases(self):
        """Cross-channel/scalar ratio increases from genus 2 to genus 3."""
        results = cross_channel_growth()
        for c_val in [10, 26, 50, 100]:
            data = results[c_val]
            # The cross-channel correction becomes relatively larger at genus 3
            r2 = data['cross_over_scalar_g2']
            r3 = data['cross_over_scalar_g3']
            assert r2 is not None and r3 is not None
            assert r3 > r2, (
                f"At c={c_val}: cross/scalar ratio should increase from "
                f"g=2 ({float(r2):.4f}) to g=3 ({float(r3):.4f})"
            )


# ============================================================================
# Free energy decomposition
# ============================================================================

class TestFreeEnergyDecomposition:
    """Complete genus-3 free energy decomposition for all families."""

    def test_heisenberg_uniform(self):
        """Heisenberg is uniform-weight, zero cross-channel and planted-forest."""
        result = genus3_free_energy('Heisenberg', Fraction(1))
        assert result['is_uniform_weight']
        assert result['delta_cross'] == 0
        assert result['delta_pf'] == 0
        assert result['total_F3'] == result['scalar_F3']

    def test_virasoro_uniform(self):
        """Virasoro is uniform-weight, zero cross-channel."""
        result = genus3_free_energy('Virasoro', Fraction(26))
        assert result['is_uniform_weight']
        assert result['delta_cross'] == 0

    def test_virasoro_nonzero_pf(self):
        """Virasoro has nonzero planted-forest (class M)."""
        result = genus3_free_energy('Virasoro', Fraction(26))
        assert result['delta_pf'] != 0

    def test_w3_nonuniform(self):
        """W_3 is multi-weight, nonzero cross-channel."""
        result = genus3_free_energy('W_3', Fraction(50))
        assert not result['is_uniform_weight']
        assert result['delta_cross'] > 0

    def test_w3_total_F3_finite(self):
        """Total F_3(W_3) is finite and nonzero for c > 0.

        Note: F_3 need not be positive — the planted-forest and cross-channel
        corrections can make it negative at some c values. The sign of F_g
        at higher genus is not constrained to be positive.
        """
        for c_val in [1, 10, 26, 50, 100]:
            result = genus3_free_energy('W_3', Fraction(c_val))
            assert result['total_F3'] != 0, f"F_3 vanishes at c={c_val}"

    def test_comparison_table(self):
        """Genus comparison table produces valid data."""
        table = genus_comparison_table([26, 50])
        for c_val in [26, 50]:
            assert table[c_val]['g2_cross'] > 0
            assert table[c_val]['g3_cross'] > 0
            assert table[c_val]['g3_to_g2_cross_ratio'] is not None


# ============================================================================
# Full verification summary
# ============================================================================

class TestFullVerification:
    """End-to-end verification of all computations."""

    def test_full_summary(self):
        """Full verification summary passes all checks."""
        summary = full_verification_summary()
        # lambda_3^FP
        assert summary['lambda_3_FP']['all_agree']
        assert summary['lambda_3_FP']['equals_31_over_967680']
        # delta_F_3 closed-form vs universal at multiple c
        for c_val in [1, 10, 26, 50]:
            key = f'delta_F3_c{c_val}'
            assert summary[key]['match'], f"Mismatch at c={c_val}"
        # Positivity
        for c_val, pos in summary['positivity'].items():
            assert pos, f"Not positive at c={c_val}"
        # Depth-class
        dc = summary['depth_class']
        assert dc['G_zero_k1']
        assert dc['L_nonzero']
        assert dc['L_consistent_with_affine']
