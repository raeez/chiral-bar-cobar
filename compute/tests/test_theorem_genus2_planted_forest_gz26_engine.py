r"""Tests for theorem_genus2_planted_forest_gz26_engine.

Cross-checks genus-2 planted-forest corrections against GZ26 non-planar
sphere algebra predictions. Multi-path verification per CLAUDE.md mandate.

Multi-path verification:
  Path 1: lambda_2^FP from Bernoulli recurrence
  Path 2: lambda_2^FP from A-hat genus expansion
  Path 3: lambda_2^FP from direct Bernoulli evaluation
  Path 4: delta_pf from planted-forest formula
  Path 5: delta_pf from direct closed-form (Virasoro)
  Path 6: delta_F_2^cross from graph decomposition
  Path 7: delta_F_2^cross from closed-form formula
  Path 8: Propagator variance from Cauchy-Schwarz formula
  Path 9: Propagator variance from direct closed-form
  Path 10: Banana graph S_4 sensitivity
  Path 11: GZ26 genus-0 -> genus-2 consistency
  Path 12: Koszul complementarity at genus 2
  Path 13: Cross-family consistency
"""

from fractions import Fraction
import pytest

from compute.lib.theorem_genus2_planted_forest_gz26_engine import (
    # Bernoulli and Faber-Pandharipande
    _bernoulli,
    lambda_fp,
    lambda_fp_from_ahat,
    lambda_fp_from_bernoulli_direct,
    # Shadow data
    heisenberg_shadow,
    affine_sl2_shadow,
    virasoro_shadow,
    w3_shadow,
    betagamma_shadow,
    # Planted-forest corrections
    planted_forest_g2,
    planted_forest_g2_heisenberg,
    planted_forest_g2_affine_sl2,
    planted_forest_g2_virasoro,
    planted_forest_g2_virasoro_direct,
    # Cross-channel corrections
    w3_cross_channel_correction,
    w3_cross_channel_decomposition,
    w3_full_F2,
    # Propagator variance
    propagator_variance,
    w3_propagator_variance,
    w3_propagator_variance_direct,
    # Banana graph
    banana_dF2_dS4,
    banana_contribution_virasoro,
    # GZ26 consistency
    gz26_shadow_to_planted_forest,
    gz26_consistency_table,
    # Free energy
    genus2_free_energy,
    virasoro_F2_total,
    # Complementarity
    virasoro_complementarity_g2,
    w3_complementarity_g2,
    # Cross-checks
    uniform_weight_cross_check,
    additivity_check_g2,
    full_verification_summary,
)


# ============================================================================
# PATH 1-3: lambda_2^FP three-way verification
# ============================================================================

class TestLambdaFP:
    """Three-path verification of the Faber-Pandharipande number lambda_2^FP."""

    def test_lambda2_fp_value(self):
        """lambda_2^FP = 7/5760 (NOT 1/1152 -- AP38!)."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda2_fp_from_ahat(self):
        """lambda_2^FP from A-hat genus expansion matches Bernoulli."""
        assert lambda_fp_from_ahat(2) == Fraction(7, 5760)

    def test_lambda2_fp_from_direct(self):
        """lambda_2^FP from direct Bernoulli evaluation."""
        assert lambda_fp_from_bernoulli_direct(2) == Fraction(7, 5760)

    def test_all_three_paths_agree(self):
        """All three paths give the same lambda_2^FP."""
        v1 = lambda_fp(2)
        v2 = lambda_fp_from_ahat(2)
        v3 = lambda_fp_from_bernoulli_direct(2)
        assert v1 == v2 == v3

    def test_lambda1_fp_value(self):
        """lambda_1^FP = 1/24 (cross-check)."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda3_fp_value(self):
        """lambda_3^FP = 31/967680 (cross-check)."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda2_from_bernoulli_B4(self):
        """Verify from B_4 = -1/30 directly.

        lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 * 1/24 = 7/5760.
        """
        B4 = _bernoulli(4)
        assert B4 == Fraction(-1, 30)
        result = Fraction(7, 8) * abs(B4) / Fraction(24)
        assert result == Fraction(7, 5760)

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP are positive (Bernoulli sign, critical pitfall)."""
        for g in range(1, 6):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        for g in range(1, 5):
            assert lambda_fp(g) > lambda_fp(g + 1)


# ============================================================================
# PATH 4-5: Planted-forest corrections
# ============================================================================

class TestPlantedForest:
    """Planted-forest correction delta_pf^{(2,0)} for all families."""

    def test_heisenberg_vanishes(self):
        """Heisenberg: delta_pf = 0 (class G, S_3 = 0)."""
        assert planted_forest_g2_heisenberg() == Fraction(0)

    def test_heisenberg_vanishes_all_k(self):
        """Heisenberg vanishes at all levels k."""
        for k in [1, 2, 5, 10, 100]:
            assert planted_forest_g2_heisenberg(Fraction(k)) == Fraction(0)

    def test_virasoro_c26(self):
        """Virasoro at c=26: delta_pf = -(26-40)/48 = 14/48 = 7/24."""
        result = planted_forest_g2_virasoro(Fraction(26))
        assert result == Fraction(7, 24)

    def test_virasoro_c26_direct(self):
        """Virasoro at c=26 via direct formula matches."""
        formula = planted_forest_g2_virasoro(Fraction(26))
        direct = planted_forest_g2_virasoro_direct(Fraction(26))
        assert formula == direct

    def test_virasoro_c13(self):
        """Virasoro at c=13 (self-dual point): delta_pf = 27/48 = 9/16."""
        result = planted_forest_g2_virasoro(Fraction(13))
        expected = -(Fraction(13) - 40) / 48
        assert result == expected
        assert result == Fraction(27, 48)
        assert result == Fraction(9, 16)

    def test_virasoro_c40_vanishes(self):
        """Virasoro at c=40: delta_pf = 0 (special zero)."""
        result = planted_forest_g2_virasoro(Fraction(40))
        assert result == Fraction(0)

    def test_virasoro_formula_vs_direct(self):
        """Formula and direct agree at multiple c values."""
        for c_val in [1, 2, 5, 13, 26, 40, 50, 100]:
            c = Fraction(c_val)
            assert planted_forest_g2_virasoro(c) == planted_forest_g2_virasoro_direct(c)

    def test_affine_sl2_k1(self):
        """Affine sl_2 at k=1: S_3 = 4/3, kappa = 9/4.

        delta_pf = (4/3)(10*4/3 - 9/4)/48
                 = (4/3)(40/3 - 9/4)/48
                 = (4/3)((160-27)/12)/48
                 = (4/3)(133/12)/48
                 = 532/(3*12*48)
                 = 532/1728
                 = 133/432
        """
        result = planted_forest_g2_affine_sl2(Fraction(1))
        expected = Fraction(133, 432)
        assert result == expected

    def test_affine_sl2_k1_from_raw(self):
        """Cross-check affine sl_2 k=1 from raw formula."""
        S_3 = Fraction(4, 3)
        kappa = Fraction(9, 4)
        raw = planted_forest_g2(S_3, kappa)
        assert raw == Fraction(133, 432)

    def test_affine_sl2_nonzero(self):
        """Affine sl_2 planted-forest is nonzero (class L, S_3 != 0)."""
        for k in [1, 3, 5, 10]:
            kf = Fraction(k)
            result = planted_forest_g2_affine_sl2(kf)
            assert result != Fraction(0), f"Should be nonzero at k={k}"

    def test_betagamma_vanishes(self):
        """Beta-gamma: delta_pf = 0 (S_3 = 0 despite class C)."""
        sd = betagamma_shadow()
        result = planted_forest_g2(sd['S_3'], sd['kappa'])
        assert result == Fraction(0)


# ============================================================================
# PATH 6-7: W_3 cross-channel correction
# ============================================================================

class TestW3CrossChannel:
    """Cross-channel correction delta_F_2(W_3) = (c+204)/(16c)."""

    def test_w3_formula_c50(self):
        """W_3 at c=50: delta_F_2 = (50+204)/(16*50) = 254/800 = 127/400."""
        result = w3_cross_channel_correction(Fraction(50))
        assert result == Fraction(254, 800)
        assert result == Fraction(127, 400)

    def test_w3_formula_c1(self):
        """W_3 at c=1: delta_F_2 = 205/16."""
        result = w3_cross_channel_correction(Fraction(1))
        assert result == Fraction(205, 16)

    def test_w3_decomposition_matches_formula(self):
        """Graph decomposition matches closed-form formula."""
        for c_val in [1, 10, 13, 26, 50, 100]:
            c = Fraction(c_val)
            decomp = w3_cross_channel_decomposition(c)
            assert decomp['match'], f"Mismatch at c={c_val}"

    def test_w3_decomposition_banana(self):
        """Banana graph mixed contribution = 3/c."""
        c = Fraction(50)
        decomp = w3_cross_channel_decomposition(c)
        assert decomp['banana'] == Fraction(3, 50)

    def test_w3_decomposition_theta(self):
        """Theta graph mixed contribution = 9/(2c)."""
        c = Fraction(50)
        decomp = w3_cross_channel_decomposition(c)
        assert decomp['theta'] == Fraction(9, 100)

    def test_w3_decomposition_lollipop(self):
        """Lollipop mixed contribution = 1/16 (c-independent!)."""
        for c_val in [1, 50, 100]:
            c = Fraction(c_val)
            decomp = w3_cross_channel_decomposition(c)
            assert decomp['lollipop'] == Fraction(1, 16)

    def test_w3_decomposition_barbell(self):
        """Barbell mixed contribution = 21/(4c)."""
        c = Fraction(50)
        decomp = w3_cross_channel_decomposition(c)
        assert decomp['barbell'] == Fraction(21, 200)

    def test_w3_decomposition_single_edge_zero(self):
        """Fig-eight and dumbbell have zero mixed (single-edge graphs)."""
        c = Fraction(50)
        decomp = w3_cross_channel_decomposition(c)
        assert decomp['fig_eight'] == Fraction(0)
        assert decomp['dumbbell'] == Fraction(0)

    def test_w3_large_c_asymptotics(self):
        """delta_F_2(W_3) -> 1/16 as c -> infinity."""
        # (c+204)/(16c) = 1/16 + 204/(16c) -> 1/16
        c = Fraction(10**6)
        result = w3_cross_channel_correction(c)
        # Should be very close to 1/16
        diff = abs(result - Fraction(1, 16))
        assert diff < Fraction(1, 1000)

    def test_w3_cross_channel_positive(self):
        """delta_F_2(W_3) > 0 for all c > 0."""
        for c_val in [1, 2, 5, 13, 26, 50, 100, 1000]:
            c = Fraction(c_val)
            result = w3_cross_channel_correction(c)
            assert result > 0, f"Should be positive at c={c_val}"

    def test_w3_universality_fails(self):
        """F_2(W_3) != kappa(W_3) * lambda_2^FP (multi-weight!)."""
        for c_val in [1, 13, 26, 50]:
            c = Fraction(c_val)
            kappa = Fraction(5) * c / 6
            scalar = kappa * lambda_fp(2)
            total = w3_full_F2(c)
            assert total != scalar, f"W_3 at c={c_val}: universality should fail"


# ============================================================================
# PATH 8-9: Propagator variance
# ============================================================================

class TestPropagatorVariance:
    """Propagator variance delta_mix for multi-weight algebras."""

    def test_w3_variance_formula(self):
        """W_3 propagator variance = c/5 via Cauchy-Schwarz formula."""
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            result = w3_propagator_variance(c)
            assert result == c / 5

    def test_w3_variance_direct_matches(self):
        """Cauchy-Schwarz and direct formula agree."""
        for c_val in [1, 10, 50, 100]:
            c = Fraction(c_val)
            assert w3_propagator_variance(c) == w3_propagator_variance_direct(c)

    def test_w3_variance_nonnegative(self):
        """Propagator variance is non-negative (Cauchy-Schwarz guarantee)."""
        for c_val in [1, 5, 13, 26, 50]:
            c = Fraction(c_val)
            assert w3_propagator_variance(c) >= 0

    def test_single_channel_variance_vanishes(self):
        """Single-channel algebra has zero propagator variance."""
        # Single channel: one kappa, one f
        kappas = [Fraction(13)]
        f_values = [Fraction(26)]
        result = propagator_variance(kappas, f_values)
        assert result == Fraction(0)

    def test_uniform_f_variance(self):
        """If all f_i are equal, variance simplifies but need not vanish."""
        # Two channels, equal f but different kappa
        kappas = [Fraction(1, 2), Fraction(1, 3)]
        f_values = [Fraction(1), Fraction(1)]
        result = propagator_variance(kappas, f_values)
        # = 1/(1/2) + 1/(1/3) - (2)^2/(5/6) = 2 + 3 - 24/5 = 25/5 - 24/5 = 1/5
        assert result == Fraction(1, 5)


# ============================================================================
# PATH 10: Banana graph S_4 sensitivity
# ============================================================================

class TestBananaGraph:
    """Banana graph contribution and S_4 sensitivity."""

    def test_banana_dF2_dS4_virasoro(self):
        """dF_2/dS_4 = 1/(8*kappa^2) for Virasoro at c=26.

        kappa = 13, so dF_2/dS_4 = 1/(8*169) = 1/1352.
        """
        kappa = Fraction(13)
        result = banana_dF2_dS4(kappa)
        assert result == Fraction(1, 1352)

    def test_banana_dF2_dS4_formula(self):
        """dF_2/dS_4 = 1/(8*kappa^2) at several kappa values."""
        for k in [1, 2, 5, 13]:
            kappa = Fraction(k)
            result = banana_dF2_dS4(kappa)
            assert result == Fraction(1, 8 * k**2)

    def test_banana_virasoro_contribution(self):
        """Banana contribution for Virasoro at c=26.

        S_4 = 10/(26*152) = 10/3952 = 5/1976.
        banana = S_4/(8*kappa^2) = (5/1976)/(8*169) = 5/(1976*1352) = 5/2671552.
        """
        c = Fraction(26)
        result = banana_contribution_virasoro(c)
        kappa = c / 2
        S_4 = Fraction(10) / (c * (5 * c + 22))
        expected = S_4 / (8 * kappa**2)
        assert result == expected


# ============================================================================
# PATH 11: GZ26 consistency
# ============================================================================

class TestGZ26Consistency:
    """GZ26 genus-0 shadow data -> genus-2 planted-forest consistency."""

    def test_gz26_heisenberg(self):
        """GZ26 for Heisenberg: genus-0 S_3=0 correctly predicts delta_pf=0."""
        gz = gz26_shadow_to_planted_forest(Fraction(0), Fraction(1))
        assert gz['delta_pf'] == Fraction(0)

    def test_gz26_virasoro_c26(self):
        """GZ26 for Virasoro c=26: genus-0 S_3=2 predicts delta_pf=7/24."""
        gz = gz26_shadow_to_planted_forest(Fraction(2), Fraction(13))
        assert gz['delta_pf'] == Fraction(7, 24)

    def test_gz26_affine_sl2_k1(self):
        """GZ26 for affine sl_2 k=1: S_3=4/3 predicts delta_pf=133/432."""
        gz = gz26_shadow_to_planted_forest(Fraction(4, 3), Fraction(9, 4))
        assert gz['delta_pf'] == Fraction(133, 432)

    def test_gz26_consistency_table_all_match(self):
        """Full GZ26 consistency table: all entries match."""
        table = gz26_consistency_table()
        for family, data in table.items():
            assert data['match'], f"GZ26 mismatch for {family}"

    def test_gz26_hamiltonian_order(self):
        """GZ26 Hamiltonian order: 1 for class G, 3 for class L/M."""
        gz_heis = gz26_shadow_to_planted_forest(Fraction(0), Fraction(1))
        assert gz_heis['gz26_H_order'] == 1  # class G: only quadratic

        gz_vir = gz26_shadow_to_planted_forest(Fraction(2), Fraction(13))
        assert gz_vir['gz26_H_order'] == 3  # class M: cubic term present


# ============================================================================
# PATH 12: Koszul complementarity
# ============================================================================

class TestComplementarity:
    """Koszul complementarity checks at genus 2."""

    def test_virasoro_scalar_complementarity(self):
        """Vir_c + Vir_{26-c}: scalar sum = 13 * lambda_2^FP."""
        for c_val in [1, 5, 13, 25]:
            c = Fraction(c_val)
            result = virasoro_complementarity_g2(c)
            assert result['scalar_match']

    def test_virasoro_pf_complementarity_sum(self):
        """delta_pf(c) + delta_pf(26-c) = 9/8 for Virasoro.

        -(c-40)/48 + -(26-c-40)/48 = -(c-40-(c-66))/48... let me recompute.
        delta_pf(c) = -(c-40)/48
        delta_pf(26-c) = -((26-c)-40)/48 = -(26-c-40)/48 = -(-c-14)/48 = (c+14)/48
        Sum = -(c-40)/48 + (c+14)/48 = (-c+40+c+14)/48 = 54/48 = 9/8.
        """
        for c_val in [1, 5, 13, 25]:
            c = Fraction(c_val)
            result = virasoro_complementarity_g2(c)
            assert result['pf_match'], f"PF complementarity fails at c={c_val}"
            assert result['pf_sum'] == Fraction(9, 8)

    def test_virasoro_c13_selfdual_pf(self):
        """At self-dual point c=13: delta_pf(13) = delta_pf(13) (trivially)."""
        result = virasoro_complementarity_g2(Fraction(13))
        pf_13 = planted_forest_g2_virasoro(Fraction(13))
        assert 2 * pf_13 == Fraction(9, 8)
        assert pf_13 == Fraction(9, 16)

    def test_w3_scalar_complementarity(self):
        """W_3 at c + W_3 at 100-c: scalar sum = (250/3) * lambda_2^FP."""
        for c_val in [10, 50, 80]:
            c = Fraction(c_val)
            result = w3_complementarity_g2(c)
            assert result['scalar_match'], f"W_3 scalar compl fails at c={c_val}"


# ============================================================================
# PATH 13: Cross-family consistency
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_uniform_weight_check(self):
        """All uniform-weight families: verify delta_pf computed correctly."""
        results = uniform_weight_cross_check()
        # Heisenberg: all should be zero
        for k in [1, 2, 5, 10]:
            key = f'Heisenberg_k{k}'
            assert results[key]['is_zero'], f"Heisenberg k={k} should have delta_pf=0"

    def test_virasoro_c40_special(self):
        """Virasoro at c=40: unique zero of delta_pf."""
        results = uniform_weight_cross_check()
        assert results['Virasoro_c40']['is_zero']

    def test_virasoro_nonzero_generic(self):
        """Virasoro at generic c != 40: delta_pf != 0."""
        results = uniform_weight_cross_check()
        for c_val in [1, 13, 26]:
            assert not results[f'Virasoro_c{c_val}']['is_zero']

    def test_affine_sl2_nonzero(self):
        """Affine sl_2: delta_pf != 0 (class L, S_3 != 0)."""
        results = uniform_weight_cross_check()
        for k in [1, 3, 10]:
            assert not results[f'affine_sl2_k{k}']['is_zero']

    def test_additivity_g2(self):
        """Scalar sector additivity at genus 2."""
        result = additivity_check_g2()
        assert result['heisenberg_additivity']
        assert result['virasoro_complementarity']

    def test_genus2_free_energy_virasoro(self):
        """Full genus-2 decomposition for Virasoro."""
        result = genus2_free_energy('Virasoro', Fraction(26))
        assert result['kappa'] == Fraction(13)
        assert result['lambda_2_FP'] == Fraction(7, 5760)
        assert result['delta_cross'] == Fraction(0)
        assert result['is_uniform_weight']

    def test_genus2_free_energy_w3(self):
        """Full genus-2 decomposition for W_3."""
        c = Fraction(50)
        result = genus2_free_energy('W_3', c)
        assert result['kappa'] == Fraction(5) * c / 6
        assert result['delta_cross'] == w3_cross_channel_correction(c)
        assert not result['is_uniform_weight']

    def test_virasoro_F2_total_c26(self):
        """Total F_2 for Virasoro at c=26.

        scalar = 13 * 7/5760 = 91/5760
        delta_pf = 7/24 = 1680/5760
        total = 1771/5760
        """
        result = virasoro_F2_total(Fraction(26))
        scalar = Fraction(13) * Fraction(7, 5760)
        pf = Fraction(7, 24)
        expected = scalar + pf
        assert result == expected

    def test_virasoro_F2_total_c1(self):
        """Total F_2 for Virasoro at c=1.

        scalar = (1/2)(7/5760) = 7/11520
        delta_pf = -(1-40)/48 = 39/48 = 13/16
        """
        c = Fraction(1)
        result = virasoro_F2_total(c)
        scalar = Fraction(1, 2) * Fraction(7, 5760)
        pf = Fraction(13, 16)
        assert result == scalar + pf


# ============================================================================
# Integration: Full verification summary
# ============================================================================

class TestFullVerification:
    """Integration tests using the full verification summary."""

    def test_summary_lambda2_agreement(self):
        """Full summary: all three lambda_2^FP paths agree."""
        summary = full_verification_summary([26])
        assert summary['lambda_2_FP']['all_agree']

    def test_summary_propagator_variance(self):
        """Full summary: propagator variance formula vs direct agree."""
        summary = full_verification_summary([26, 50])
        for c_val in [26, 50]:
            assert summary[f'prop_variance_c{c_val}']['match']

    def test_summary_gz26_consistency(self):
        """Full summary: GZ26 consistency entries all match."""
        summary = full_verification_summary([26])
        gz = summary['gz26_consistency']
        for family, data in gz.items():
            assert data['match'], f"GZ26 mismatch: {family}"


# ============================================================================
# Shadow data validation
# ============================================================================

class TestShadowData:
    """Validate shadow data for all standard families."""

    def test_heisenberg_kappa(self):
        """Heisenberg kappa = k (AP1/AP9)."""
        for k in [1, 2, 5]:
            sd = heisenberg_shadow(Fraction(k))
            assert sd['kappa'] == Fraction(k)

    def test_virasoro_kappa(self):
        """Virasoro kappa = c/2 (AP1/AP9)."""
        for c_val in [1, 13, 26]:
            sd = virasoro_shadow(Fraction(c_val))
            assert sd['kappa'] == Fraction(c_val, 2)

    def test_affine_sl2_kappa(self):
        """Affine sl_2 kappa = 3(k+2)/4 (AP1/AP9)."""
        sd = affine_sl2_shadow(Fraction(1))
        assert sd['kappa'] == Fraction(9, 4)

        sd = affine_sl2_shadow(Fraction(2))
        assert sd['kappa'] == Fraction(3)

    def test_virasoro_S3(self):
        """Virasoro S_3 = 2 (cubic shadow from T_{(1)}T = 2T)."""
        sd = virasoro_shadow(Fraction(26))
        assert sd['S_3'] == Fraction(2)

    def test_affine_sl2_S3(self):
        """Affine sl_2 S_3 = 4/(k+2)."""
        sd = affine_sl2_shadow(Fraction(1))
        assert sd['S_3'] == Fraction(4, 3)

        sd = affine_sl2_shadow(Fraction(2))
        assert sd['S_3'] == Fraction(1)

    def test_virasoro_S4(self):
        """Virasoro S_4 = Q^contact = 10/[c(5c+22)]."""
        sd = virasoro_shadow(Fraction(26))
        assert sd['S_4'] == Fraction(10, 26 * 152)

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (all higher shadows vanish)."""
        sd = heisenberg_shadow()
        assert sd['class'] == 'G'
        assert sd['S_3'] == 0
        assert sd['S_4'] == 0

    def test_affine_sl2_class_L(self):
        """Affine sl_2 is class L (S_3 != 0, S_4 = 0)."""
        sd = affine_sl2_shadow()
        assert sd['class'] == 'L'
        assert sd['S_3'] != 0
        assert sd['S_4'] == 0

    def test_virasoro_class_M(self):
        """Virasoro is class M (S_3 != 0, S_4 != 0)."""
        sd = virasoro_shadow(Fraction(26))
        assert sd['class'] == 'M'
        assert sd['S_3'] != 0
        assert sd['S_4'] != 0

    def test_w3_kappa_total(self):
        """W_3 total kappa = 5c/6."""
        c = Fraction(50)
        sd = w3_shadow(c)
        assert sd['kappa_total'] == Fraction(5) * c / 6

    def test_w3_kappa_decomposition(self):
        """W_3 kappa_T + kappa_W = kappa_total."""
        c = Fraction(50)
        sd = w3_shadow(c)
        assert sd['kappa_T'] + sd['kappa_W'] == sd['kappa_total']

    def test_affine_critical_level_raises(self):
        """Affine sl_2 at critical level k=-2 raises error."""
        with pytest.raises(ValueError, match="critical level"):
            affine_sl2_shadow(Fraction(-2))

    def test_virasoro_c0_raises(self):
        """Virasoro at c=0 raises error."""
        with pytest.raises(ValueError, match="c = 0"):
            virasoro_shadow(Fraction(0))
