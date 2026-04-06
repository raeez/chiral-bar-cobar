r"""Tests for the shadow-Siegel bridge engine.

Organized into 16 sections:
  1.  Three genus-2 objects (categorical distinction)
  2.  Shadow amplitude F_g multi-path verification
  3.  Faber-Pandharipande lambda_g values
  4.  Kappa values and AP20/AP48 verification
  5.  Torelli bridge data
  6.  Schottky obstruction table
  7.  Schottky codimension formula verification
  8.  Shadow as integration over moduli
  9.  Lambda_2 intersection number
  10. BKM shadow dictionary
  11. Dictionary entry verification
  12. Second-quantization bridge
  13. DMVV coefficient analysis
  14. Genus-2 integration measure
  15. Mumford relations
  16. Full bridge summary and cross-verification

Multi-path verification: >= 3 independent paths per numerical result.
Total: >= 110 tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_shadow_siegel_bridge_engine import (
    # Core functions
    bernoulli_number,
    lambda_fp,
    lambda_fp_via_ahat,
    # Constants
    KAPPA_CHIRAL,
    KAPPA_BPS,
    CHI_K3,
    WEIGHT_PHI10,
    DIM_C_K3E,
    # Section 1: Three objects
    GenusGShadowAmplitude,
    shadow_amplitude,
    compute_F_g_three_paths,
    # Section 2: Siegel form
    SiegelFormData,
    siegel_form_dimensions,
    phi_10_uniqueness,
    # Section 3: Partition function
    GenusGPartitionFunction,
    three_objects_genus_2,
    # Section 4: Torelli
    TorelliBridgeData,
    torelli_bridge,
    torelli_bridge_table,
    # Section 5: Schottky
    schottky_codimension,
    schottky_obstruction_table,
    schottky_growth_rate,
    # Section 6: Integration
    shadow_as_integration,
    lambda_2_intersection_number,
    # Section 7: Dictionary
    BKMShadowDictionaryEntry,
    bkm_shadow_dictionary,
    verify_dictionary_entries,
    # Section 8: Second quantization
    second_quantization_bridge,
    dmvv_coefficient_analysis,
    # Section 9: Integration measure
    genus_2_integration_measure,
    # Section 10: Mumford
    mumford_relations_genus_2,
    # Section 11: Summary
    genus_g_shadow_siegel_summary,
    # Section 12: Verification
    verify_F_2_five_paths,
    verify_schottky_codimension_formula,
    verify_kappa_ratio_not_universal,
    # Section 13: Cross-verification
    cross_verify_with_siegel_engine,
    full_bridge_summary,
)

F = Fraction


# ============================================================================
# SECTION 1: Three genus-2 objects (categorical distinction)
# ============================================================================

class TestThreeGenus2Objects:
    """The three distinct objects at genus 2."""

    def test_three_objects_returns_all_three(self):
        """All three objects are present in the result."""
        result = three_objects_genus_2()
        assert 'object_a' in result
        assert 'object_b' in result
        assert 'object_c' in result

    def test_object_a_is_number(self):
        """Object (a) F_2 is a number (Fraction), not a function."""
        result = three_objects_genus_2()
        assert isinstance(result['object_a']['value'], Fraction)
        assert result['object_a']['type'] == 'NUMBER (Fraction)'

    def test_object_a_value(self):
        """F_2 = 3 * 7/5760 = 7/1920."""
        result = three_objects_genus_2()
        assert result['object_a']['value'] == F(7, 1920)

    def test_object_b_is_function(self):
        """Object (b) Phi_10 is a function on H_2."""
        result = three_objects_genus_2()
        assert 'FUNCTION' in result['object_b']['type']
        assert result['object_b']['dim_domain'] == 3

    def test_object_b_weight(self):
        """Phi_10 has weight 10."""
        result = three_objects_genus_2()
        assert result['object_b']['weight'] == 10

    def test_object_c_is_section(self):
        """Object (c) Z_2 is a section of a line bundle on M_2."""
        result = three_objects_genus_2()
        assert 'SECTION' in result['object_c']['type']

    def test_object_c_topological_limit(self):
        """The topological limit of Z_2 is F_2."""
        result = three_objects_genus_2()
        assert result['object_c']['topological_limit'] == F(7, 1920)

    def test_categorical_distinction(self):
        """All three objects are categorically different."""
        result = three_objects_genus_2()
        types = {
            result['object_a']['type'],
            result['object_b']['type'],
            result['object_c']['type'],
        }
        # All three types should be distinct
        assert len(types) == 3

    def test_kappa_chiral_vs_bps(self):
        """Object (a) uses kappa_ch = 3; object (b) uses kappa_BPS = 5."""
        result = three_objects_genus_2()
        assert result['object_a']['kappa'] == F(3)
        assert result['object_b']['kappa_associated'] == F(5)


# ============================================================================
# SECTION 2: Shadow amplitude F_g multi-path verification
# ============================================================================

class TestShadowAmplitudeFg:
    """F_g = kappa * lambda_g^FP via multiple paths."""

    def test_F1_exact(self):
        """F_1 = 3 * 1/24 = 1/8."""
        amp = shadow_amplitude(1)
        assert amp.F_g == F(1, 8)

    def test_F2_exact(self):
        """F_2 = 3 * 7/5760 = 7/1920."""
        amp = shadow_amplitude(2)
        assert amp.F_g == F(7, 1920)

    def test_F3_exact(self):
        """F_3 = 3 * 31/967680 = 31/322560."""
        amp = shadow_amplitude(3)
        assert amp.F_g == F(31, 322560)

    def test_F4_exact(self):
        """F_4 = 3 * 127/154828800 = 127/51609600."""
        amp = shadow_amplitude(4)
        assert amp.F_g == F(127, 51609600)

    def test_F5_exact(self):
        """F_5 = 3 * 73/3503554560 = 73/1167851520."""
        amp = shadow_amplitude(5)
        assert amp.F_g == F(73, 1167851520)

    def test_three_paths_agree_g1(self):
        """Three paths agree for F_1."""
        result = compute_F_g_three_paths(1)
        assert result['all_agree']

    def test_three_paths_agree_g2(self):
        """Three paths agree for F_2."""
        result = compute_F_g_three_paths(2)
        assert result['all_agree']

    def test_three_paths_agree_g3(self):
        """Three paths agree for F_3."""
        result = compute_F_g_three_paths(3)
        assert result['all_agree']

    def test_three_paths_agree_g5(self):
        """Three paths agree for F_5."""
        result = compute_F_g_three_paths(5)
        assert result['all_agree']

    def test_five_paths_F2(self):
        """Five independent paths give F_2 = 7/1920."""
        result = verify_F_2_five_paths()
        assert result['all_correct']
        assert result['F_2'] == F(7, 1920)

    def test_five_paths_all_agree(self):
        """All five paths give the same F_2."""
        result = verify_F_2_five_paths()
        vals = [
            result['path_1_direct'],
            result['path_2_ahat'],
            result['path_3_bernoulli'],
            result['path_4_additive'],
            result['path_5_cy_dim'],
        ]
        assert len(set(vals)) == 1

    def test_F_g_positive_all_genera(self):
        """F_g > 0 for all g >= 1 (shadow amplitudes are positive)."""
        for g in range(1, 11):
            amp = shadow_amplitude(g)
            assert amp.F_g > 0, f"F_{g} should be positive"

    def test_F_g_decreasing(self):
        """F_g is strictly decreasing in g."""
        for g in range(1, 10):
            assert shadow_amplitude(g).F_g > shadow_amplitude(g + 1).F_g


# ============================================================================
# SECTION 3: Faber-Pandharipande lambda_g values
# ============================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP intersection numbers."""

    def test_lambda_1(self):
        assert lambda_fp(1) == F(1, 24)

    def test_lambda_2(self):
        assert lambda_fp(2) == F(7, 5760)

    def test_lambda_3(self):
        assert lambda_fp(3) == F(31, 967680)

    def test_lambda_4(self):
        assert lambda_fp(4) == F(127, 154828800)

    def test_lambda_5(self):
        assert lambda_fp(5) == F(73, 3503554560)

    def test_lambda_via_ahat_agrees(self):
        """lambda_fp and lambda_fp_via_ahat give identical results."""
        for g in range(1, 8):
            assert lambda_fp(g) == lambda_fp_via_ahat(g), f"Mismatch at g={g}"

    def test_lambda_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 11):
            assert lambda_fp(g) > 0

    def test_lambda_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        for g in range(1, 10):
            assert lambda_fp(g) > lambda_fp(g + 1)


# ============================================================================
# SECTION 4: Kappa values and AP20/AP48 verification
# ============================================================================

class TestKappaValues:
    """Verify the two distinct kappa values (AP20, AP48)."""

    def test_kappa_chiral_is_3(self):
        assert KAPPA_CHIRAL == F(3)

    def test_kappa_bps_is_5(self):
        assert KAPPA_BPS == F(5)

    def test_kappa_not_equal(self):
        """kappa_ch != kappa_BPS (AP20: different objects)."""
        assert KAPPA_CHIRAL != KAPPA_BPS

    def test_kappa_ratio(self):
        """kappa_BPS / kappa_ch = 5/3."""
        assert KAPPA_BPS / KAPPA_CHIRAL == F(5, 3)

    def test_kappa_bps_from_chi(self):
        """kappa_BPS = chi(K3)/4 - 1 = 24/4 - 1 = 5."""
        assert KAPPA_BPS == F(CHI_K3, 4) - 1

    def test_weight_phi10_from_kappa_bps(self):
        """Weight of Phi_10 = 2 * kappa_BPS = 10."""
        assert WEIGHT_PHI10 == 2 * int(KAPPA_BPS)

    def test_kappa_not_c_over_2(self):
        """kappa(K3 x E) = 3 != c/2 = 3/2 (AP48)."""
        # For CY: c = dim_C = 3, but kappa = dim_C = 3 (NOT c/2 = 3/2)
        c = DIM_C_K3E
        assert KAPPA_CHIRAL == F(c)
        assert KAPPA_CHIRAL != F(c, 2)

    def test_kappa_ratio_not_universal(self):
        """The ratio 5/3 is NOT universal (depends on chi(K3))."""
        result = verify_kappa_ratio_not_universal()
        assert result['ratio_is_universal'] is False


# ============================================================================
# SECTION 5: Torelli bridge data
# ============================================================================

class TestTorelliBridge:
    """Test the Torelli bridge at each genus."""

    def test_genus_1_isomorphism(self):
        tb = TorelliBridgeData(genus=1)
        assert tb.is_isomorphism
        assert tb.dim_M_g == 1
        assert tb.dim_A_g == 1
        assert tb.codimension == 0

    def test_genus_2_birational(self):
        tb = TorelliBridgeData(genus=2)
        assert tb.is_birational
        assert tb.dim_M_g == 3
        assert tb.dim_A_g == 3
        assert tb.codimension == 0

    def test_genus_3_injective_codim_0(self):
        tb = TorelliBridgeData(genus=3)
        assert tb.is_injective
        assert not tb.has_schottky_obstruction
        assert tb.dim_M_g == 6
        assert tb.dim_A_g == 6
        assert tb.codimension == 0

    def test_genus_4_first_schottky(self):
        tb = TorelliBridgeData(genus=4)
        assert tb.has_schottky_obstruction
        assert tb.dim_M_g == 9
        assert tb.dim_A_g == 10
        assert tb.codimension == 1

    def test_genus_5_codim_3(self):
        tb = TorelliBridgeData(genus=5)
        assert tb.codimension == 3

    def test_torelli_always_injective(self):
        for g in range(1, 11):
            assert TorelliBridgeData(genus=g).is_injective

    def test_schottky_starts_at_4(self):
        for g in range(1, 4):
            assert not TorelliBridgeData(genus=g).has_schottky_obstruction
        for g in range(4, 11):
            assert TorelliBridgeData(genus=g).has_schottky_obstruction

    def test_torelli_bridge_table(self):
        """Table has entries for all genera."""
        table = torelli_bridge_table(10)
        assert len(table) == 10
        for g in range(1, 11):
            assert g in table

    def test_genus_2_phi10_pullback_exists(self):
        result = torelli_bridge(2)
        assert 'phi10_pullback' in result

    def test_genus_4_schottky_form_weight(self):
        result = torelli_bridge(4)
        assert result.get('schottky_form_weight') == 8


# ============================================================================
# SECTION 6: Schottky obstruction table
# ============================================================================

class TestSchottkyObstruction:
    """Test the Schottky obstruction."""

    def test_codim_g1(self):
        assert schottky_codimension(1) == 0

    def test_codim_g2(self):
        assert schottky_codimension(2) == 0

    def test_codim_g3(self):
        assert schottky_codimension(3) == 0

    def test_codim_g4(self):
        assert schottky_codimension(4) == 1

    def test_codim_g5(self):
        assert schottky_codimension(5) == 3

    def test_codim_g6(self):
        assert schottky_codimension(6) == 6

    def test_codim_g7(self):
        assert schottky_codimension(7) == 10

    def test_codim_g8(self):
        assert schottky_codimension(8) == 15

    def test_codim_g9(self):
        assert schottky_codimension(9) == 21

    def test_codim_g10(self):
        assert schottky_codimension(10) == 28

    def test_obstruction_table_complete(self):
        table = schottky_obstruction_table(10)
        for g in range(1, 11):
            assert g in table
            assert table[g]['formula_matches']


# ============================================================================
# SECTION 7: Schottky codimension formula verification
# ============================================================================

class TestSchottkyFormula:
    """Verify codim = (g-2)(g-3)/2 via two independent paths."""

    def test_formula_all_genera(self):
        """Both formulas agree for g = 1, ..., 15."""
        results = verify_schottky_codimension_formula()
        for g, agree in results.items():
            assert agree, f"Formula mismatch at g={g}"

    def test_formula_is_quadratic(self):
        """codim(g) = (g^2 - 5g + 6)/2 for g >= 2."""
        for g in range(2, 16):
            codim = schottky_codimension(g)
            expected = (g * g - 5 * g + 6) // 2
            assert codim == expected, f"Quadratic formula mismatch at g={g}"

    def test_codim_nonnegative(self):
        """Codimension is non-negative for all g."""
        for g in range(1, 21):
            assert schottky_codimension(g) >= 0

    def test_codim_zero_iff_g_le_3(self):
        """Codimension = 0 iff g <= 3."""
        for g in range(1, 21):
            if g <= 3:
                assert schottky_codimension(g) == 0
            else:
                assert schottky_codimension(g) > 0

    def test_growth_rate_approaches_1(self):
        """codim/dim_A_g -> 1 as g -> infinity.

        The ratio (g-2)(g-3) / (g(g+1)) converges to 1 slowly:
          g=10: 0.509, g=20: 0.729, g=50: 0.885, g=100: 0.941.
        """
        data = schottky_growth_rate()
        # At g=20: ratio > 0.7
        ratio_20 = data[20]['ratio_numerical']
        assert ratio_20 > 0.7, f"Ratio at g=20 should be > 0.7, got {ratio_20}"
        # Ratio is increasing toward 1
        assert data[20]['ratio_numerical'] > data[10]['ratio_numerical']

    def test_growth_rate_monotone(self):
        """The ratio codim/dim_A is increasing for g >= 4."""
        data = schottky_growth_rate()
        for g in range(5, 20):
            assert data[g]['ratio_numerical'] >= data[g - 1]['ratio_numerical']


# ============================================================================
# SECTION 8: Shadow as integration over moduli
# ============================================================================

class TestShadowAsIntegration:
    """F_g as an integral over M-bar_g."""

    def test_F_g_is_topological(self):
        for g in range(1, 6):
            result = shadow_as_integration(g)
            assert result['is_topological']
            assert not result['depends_on_moduli']

    def test_integration_type(self):
        result = shadow_as_integration(2)
        assert 'tautological' in result['integration_type']

    def test_genus_1_eta_connection(self):
        result = shadow_as_integration(1)
        assert 'eta' in result.get('eta_connection', '')

    def test_genus_2_siegel_connection(self):
        result = shadow_as_integration(2)
        assert 'Phi_10' in result.get('siegel_connection', '') or \
               'siegel' in result.get('siegel_connection', '').lower()

    def test_genus_4_schottky_gap(self):
        result = shadow_as_integration(4)
        assert 'schottky_gap' in result


# ============================================================================
# SECTION 9: Lambda_2 intersection number
# ============================================================================

class TestLambda2Intersection:
    """Lambda_2 as intersection number on M-bar_2."""

    def test_lambda_2_FP_value(self):
        result = lambda_2_intersection_number()
        assert result['lambda_2_FP'] == F(7, 5760)

    def test_three_paths_agree(self):
        result = lambda_2_intersection_number()
        assert result['all_agree']

    def test_known_intersection_lambda1_cubed(self):
        """int_{M-bar_2} lambda_1^3 = 1/240 (Faber)."""
        result = lambda_2_intersection_number()
        assert result['int_lambda1_cubed_M2bar'] == F(1, 240)

    def test_known_intersection_lambda1_lambda2(self):
        """int_{M-bar_2} lambda_1 * lambda_2 = 1/1152 (Faber)."""
        result = lambda_2_intersection_number()
        assert result['int_lambda1_lambda2_M2bar'] == F(1, 1152)

    def test_B4_value(self):
        """B_4 = -1/30."""
        result = lambda_2_intersection_number()
        assert result['B_4'] == F(-1, 30)


# ============================================================================
# SECTION 10: BKM shadow dictionary
# ============================================================================

class TestBKMShadowDictionary:
    """Test the BKM-shadow dictionary."""

    def test_dictionary_has_all_entries(self):
        entries = bkm_shadow_dictionary()
        expected_keys = {'kappa', 'F_1', 'F_2', 'F_g', 'shadow_depth', 'complementarity'}
        assert expected_keys.issubset(set(entries.keys()))

    def test_all_entries_verified(self):
        entries = bkm_shadow_dictionary()
        for key, entry in entries.items():
            assert entry.verified, f"Entry {key} not verified"

    def test_kappa_entry_values(self):
        entries = bkm_shadow_dictionary()
        kappa = entries['kappa']
        assert kappa.shadow_value == F(3)
        assert kappa.bkm_value == F(5)

    def test_F1_entry(self):
        entries = bkm_shadow_dictionary()
        f1 = entries['F_1']
        assert f1.shadow_value == F(1, 8)
        assert f1.bkm_value == F(1, 8)  # Exact match at genus 1

    def test_F2_entry(self):
        entries = bkm_shadow_dictionary()
        f2 = entries['F_2']
        assert f2.shadow_value == F(7, 1920)
        assert f2.bkm_value == F(7, 1920)


# ============================================================================
# SECTION 11: Dictionary entry verification
# ============================================================================

class TestDictionaryVerification:
    """Independent verification of dictionary entries."""

    def test_verify_all_entries(self):
        results = verify_dictionary_entries()
        for key, ok in results.items():
            assert ok, f"Verification failed for {key}"

    def test_kappa_ratio_verified(self):
        results = verify_dictionary_entries()
        assert results['kappa_ratio']

    def test_F1_value_verified(self):
        results = verify_dictionary_entries()
        assert results['F_1_value']

    def test_F2_value_verified(self):
        results = verify_dictionary_entries()
        assert results['F_2_value']

    def test_chi_K3_verified(self):
        results = verify_dictionary_entries()
        assert results['chi_K3']

    def test_kappa_bps_from_chi_verified(self):
        results = verify_dictionary_entries()
        assert results['kappa_BPS_from_chi']

    def test_eta_power_verified(self):
        results = verify_dictionary_entries()
        assert results['eta_power']


# ============================================================================
# SECTION 12: Second-quantization bridge
# ============================================================================

class TestSecondQuantizationBridge:
    """Test the first-quantized vs second-quantized bridge."""

    def test_kappa_values(self):
        result = second_quantization_bridge()
        assert result['kappa_chiral'] == F(3)
        assert result['kappa_bps'] == F(5)

    def test_ratio(self):
        result = second_quantization_bridge()
        assert result['ratio'] == F(5, 3)

    def test_ratio_not_universal(self):
        result = second_quantization_bridge()
        assert result['ratio_is_universal'] is False

    def test_operations_not_in_shadow(self):
        """Three operations separate shadow from BPS."""
        result = second_quantization_bridge()
        ops = result['operations_not_in_shadow']
        assert len(ops) == 3
        assert any('Sym' in op or 'symmetric' in op.lower() for op in ops)
        assert any('DMVV' in op for op in ops)
        assert any('Borcherds' in op for op in ops)

    def test_shadow_values_correct(self):
        result = second_quantization_bridge()
        assert result['F_g_shadow'][1]['value'] == F(1, 8)
        assert result['F_g_shadow'][2]['value'] == F(7, 1920)


# ============================================================================
# SECTION 13: DMVV coefficient analysis
# ============================================================================

class TestDMVVAnalysis:
    """Test DMVV symmetric product analysis."""

    def test_chi_K3(self):
        result = dmvv_coefficient_analysis()
        assert result['chi_K3'] == 24

    def test_chi_y_K3(self):
        """chi_y(K3) = 2."""
        result = dmvv_coefficient_analysis()
        assert result['chi_y_K3'] == 2

    def test_sym0_is_1(self):
        result = dmvv_coefficient_analysis()
        assert result['symmetric_product_data'][0]['chi_top'] == 1

    def test_sym1_is_24(self):
        result = dmvv_coefficient_analysis()
        assert result['symmetric_product_data'][1]['chi_top'] == 24

    def test_sym2_is_300(self):
        """chi(Sym^2(K3)) = (24^2 + 24)/2 = 300."""
        result = dmvv_coefficient_analysis()
        assert result['symmetric_product_data'][2]['chi_top'] == 300

    def test_sym3_value(self):
        """chi(Sym^3(K3)) = (24^3 + 3*24^2 + 2*24)/6 = 2600."""
        chi = 24
        expected = (chi ** 3 + 3 * chi ** 2 + 2 * chi) // 6
        assert expected == 2600
        result = dmvv_coefficient_analysis()
        assert result['symmetric_product_data'][3]['chi_top'] == 2600

    def test_sym_N_via_binomial(self):
        """chi(Sym^N(K3)) = C(23+N, N) for chi = 24."""
        result = dmvv_coefficient_analysis()
        for N in range(6):
            expected = math.comb(23 + N, N)
            assert result['symmetric_product_data'][N]['chi_top'] == expected

    def test_sym_growth(self):
        """chi(Sym^N) grows with N."""
        result = dmvv_coefficient_analysis()
        data = result['symmetric_product_data']
        for N in range(1, 5):
            assert data[N]['chi_top'] < data[N + 1]['chi_top']


# ============================================================================
# SECTION 14: Genus-2 integration measure
# ============================================================================

class TestGenus2IntegrationMeasure:
    """Test the integration measure analysis."""

    def test_question_is_ill_posed(self):
        result = genus_2_integration_measure()
        assert result['question_is_ill_posed']

    def test_F2_value(self):
        result = genus_2_integration_measure()
        assert result['F_2'] == F(7, 1920)

    def test_intersection_numbers(self):
        result = genus_2_integration_measure()
        assert result['known_intersection_numbers']['lambda_1_cubed'] == F(1, 240)
        assert result['known_intersection_numbers']['lambda_1_lambda_2'] == F(1, 1152)


# ============================================================================
# SECTION 15: Mumford relations
# ============================================================================

class TestMumfordRelations:
    """Test Mumford relation data at genus 2."""

    def test_hodge_rank(self):
        result = mumford_relations_genus_2()
        assert result['hodge_bundle_rank'] == 2

    def test_lambda_2_FP(self):
        result = mumford_relations_genus_2()
        assert result['lambda_2_FP'] == F(7, 5760)

    def test_F_2(self):
        result = mumford_relations_genus_2()
        assert result['F_2'] == F(7, 1920)

    def test_intersection_lambda1_cubed(self):
        result = mumford_relations_genus_2()
        assert result['intersection_numbers']['lambda_1^3'] == F(1, 240)

    def test_intersection_lambda1_lambda2(self):
        result = mumford_relations_genus_2()
        assert result['intersection_numbers']['lambda_1 * lambda_2'] == F(1, 1152)


# ============================================================================
# SECTION 16: Full bridge summary and cross-verification
# ============================================================================

class TestFullBridgeSummary:
    """Test the complete bridge summary."""

    def test_definitive_answer(self):
        result = full_bridge_summary()
        assert 'NOT' in result['definitive_answer']

    def test_four_reasons(self):
        result = full_bridge_summary()
        assert 'reason_categorical' in result
        assert 'reason_kappa' in result
        assert 'reason_quantization' in result
        assert 'reason_genus' in result

    def test_bridge_genus_1(self):
        result = full_bridge_summary()
        assert result['bridge_genus_1']['F_1'] == F(1, 8)
        assert result['bridge_genus_1']['eta_power'] == -6

    def test_bridge_genus_2(self):
        result = full_bridge_summary()
        assert result['bridge_genus_2']['F_2'] == F(7, 1920)

    def test_schottky_table(self):
        result = full_bridge_summary()
        st = result['schottky_table']
        assert st[1] == 0
        assert st[2] == 0
        assert st[3] == 0
        assert st[4] == 1
        assert st[10] == 28

    def test_cross_verify_all_agree(self):
        result = cross_verify_with_siegel_engine()
        assert result['all_agree']

    def test_cross_verify_F_values(self):
        result = cross_verify_with_siegel_engine()
        assert result['F_values'][1] == F(1, 8)
        assert result['F_values'][2] == F(7, 1920)
        assert result['F_values'][3] == F(31, 322560)


class TestSiegelFormDimensions:
    """Test Siegel modular form dimension data."""

    def test_first_cusp_form_weight_10(self):
        dims = siegel_form_dimensions()
        # No cusp forms below weight 10
        for k in range(0, 10, 2):
            assert dims[k]['dim_S_k'] == 0

    def test_dim_S_10_is_1(self):
        dims = siegel_form_dimensions()
        assert dims[10]['dim_S_k'] == 1

    def test_phi_10_unique(self):
        result = phi_10_uniqueness()
        assert result['unique']
        assert result['dim_S_10'] == 1


class TestSiegelFormDataclass:
    """Test the SiegelFormData dataclass."""

    def test_weight(self):
        sf = SiegelFormData()
        assert sf.weight == 10

    def test_degree(self):
        sf = SiegelFormData()
        assert sf.degree == 2

    def test_dim_domain(self):
        sf = SiegelFormData()
        assert sf.dim_domain == 3  # g(g+1)/2 = 3

    def test_is_cusp(self):
        sf = SiegelFormData()
        assert sf.is_cusp_form

    def test_kappa_bps(self):
        sf = SiegelFormData()
        assert sf.kappa_bps == F(5)


class TestGenusGSummary:
    """Test the genus-g summary function."""

    def test_genus_1_exact(self):
        s = genus_g_shadow_siegel_summary(1)
        assert s['bridge_quality'] == 'exact'
        assert s['shadow_amplitude']['F_g'] == F(1, 8)

    def test_genus_2_birational(self):
        s = genus_g_shadow_siegel_summary(2)
        assert s['bridge_quality'] == 'birational'
        assert s['shadow_amplitude']['F_g'] == F(7, 1920)

    def test_genus_3_open_dense(self):
        s = genus_g_shadow_siegel_summary(3)
        assert s['bridge_quality'] == 'open dense'

    def test_genus_4_schottky(self):
        s = genus_g_shadow_siegel_summary(4)
        assert 'Schottky' in s['bridge_quality']
        assert s['torelli']['codim'] == 1

    def test_genus_10_large_codim(self):
        s = genus_g_shadow_siegel_summary(10)
        assert s['torelli']['codim'] == 28


class TestPartitionFunction:
    """Test GenusGPartitionFunction."""

    def test_genus_1_eta_power(self):
        pf = GenusGPartitionFunction(genus=1)
        assert pf.genus_1_eta_power() == -6

    def test_shadow_amplitude_genus_2(self):
        pf = GenusGPartitionFunction(genus=2)
        assert pf.shadow_amplitude == F(7, 1920)

    def test_description_genus_1(self):
        pf = GenusGPartitionFunction(genus=1)
        desc = pf.description()
        assert 'eta' in desc
        assert '-6' in desc

    def test_description_genus_2(self):
        pf = GenusGPartitionFunction(genus=2)
        desc = pf.description()
        assert 'Phi_10' in desc or 'DVV' in desc


class TestBernoulliNumbers:
    """Cross-verify Bernoulli numbers used throughout."""

    def test_B0(self):
        assert bernoulli_number(0) == F(1)

    def test_B1(self):
        assert bernoulli_number(1) == F(-1, 2)

    def test_B2(self):
        assert bernoulli_number(2) == F(1, 6)

    def test_B4(self):
        assert bernoulli_number(4) == F(-1, 30)

    def test_B6(self):
        assert bernoulli_number(6) == F(1, 42)

    def test_B8(self):
        assert bernoulli_number(8) == F(-1, 30)

    def test_B10(self):
        assert bernoulli_number(10) == F(5, 66)

    def test_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == F(0)
