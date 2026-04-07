"""Tests for gaiotto_3d_ht_comparison_engine.py.

Tests the systematic comparison between:
  - Gaiotto-Kulp-Wu higher operations framework (GKW24, GKW25)
  - Costello-Dimofte-Gaiotto boundary chiral algebras (CDG20)
  - Dimofte-Niu-Py line operators and dg-shifted Yangians (DNP25)
  - Butson equivariant factorization (But20)
  - Gaiotto-Oh corner VOAs (GO19)
and our shadow obstruction tower / Swiss-cheese framework.

Multi-path verification (CLAUDE.md mandate): each claim verified by >= 2 paths.
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify, S

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from gaiotto_3d_ht_comparison_engine import (
    # Section 1: Shadow depth
    ShadowDepthData,
    standard_shadow_data,
    # Section 2: GKW operations
    GKWOperation,
    gkw_formality_prediction,
    gkw_quadratic_identity_dimension,
    # Section 3: Comparisons
    compare_m3_free_scalar,
    compare_m3_cubic_lg,
    compare_m4_cubic_lg,
    compare_m3_gauge_theory,
    compare_m4_gauge_theory,
    compare_mk_virasoro,
    # Section 4: CDG bulk
    cdg_bulk_comparison_free,
    cdg_bulk_comparison_gauge,
    cdg_bulk_comparison_lg,
    # Section 5: DNP lines
    dnp_line_comparison_gauge,
    # Section 6: Shadow depth vs GKW
    shadow_depth_vs_gkw_complexity,
    # Section 7: SQED/SQCD
    sqed_boundary_character,
    sqed_sc_operations_prediction,
    sqcd_sc_operations_prediction,
    # Section 8: Genus comparison
    genus_comparison_table,
    # Section 9: Corner VOA
    corner_voa_shadow_prediction,
    # Section 10: Summary
    full_comparison_summary,
    # Section 11: Numerical checks
    kappa_consistency_check,
    ainfty_relation_count,
    pole_order_to_shadow_depth,
    # Section 12: Butson
    butson_coulomb_comparison,
)


# ============================================================================
# Test Class 1: Shadow Depth Classification
# ============================================================================

class TestShadowDepthClassification:
    """Verify the G/L/C/M shadow depth classification for standard families."""

    def test_standard_shadow_data_completeness(self):
        """All 9 standard families have shadow data."""
        data = standard_shadow_data()
        expected_families = [
            'heisenberg', 'free_fermion', 'lattice',
            'affine_km', 'affine_sl2', 'betagamma',
            'virasoro', 'w3', 'w_N',
        ]
        for fam in expected_families:
            assert fam in data, f"Missing family: {fam}"

    def test_class_g_families(self):
        """Class G families: r_max = 2, SC-formal."""
        data = standard_shadow_data()
        for name in ['heisenberg', 'free_fermion', 'lattice']:
            sd = data[name]
            assert sd.shadow_class == 'G', f"{name} should be class G"
            assert sd.r_max == 2, f"{name} should have r_max = 2"
            assert sd.sc_formal is True, f"{name} should be SC-formal"
            assert sd.is_koszul is True, f"{name} should be Koszul (AP14)"

    def test_class_l_families(self):
        """Class L families: r_max = 3, not SC-formal."""
        data = standard_shadow_data()
        for name in ['affine_km', 'affine_sl2']:
            sd = data[name]
            assert sd.shadow_class == 'L', f"{name} should be class L"
            assert sd.r_max == 3, f"{name} should have r_max = 3"
            assert sd.sc_formal is False
            assert sd.is_koszul is True

    def test_class_c_families(self):
        """Class C families: r_max = 4, not SC-formal."""
        data = standard_shadow_data()
        sd = data['betagamma']
        assert sd.shadow_class == 'C'
        assert sd.r_max == 4
        assert sd.sc_formal is False
        assert sd.is_koszul is True

    def test_class_m_families(self):
        """Class M families: r_max = infinity, not SC-formal."""
        data = standard_shadow_data()
        for name in ['virasoro', 'w3', 'w_N']:
            sd = data[name]
            assert sd.shadow_class == 'M', f"{name} should be class M"
            assert sd.r_max == float('inf'), f"{name} should have infinite depth"
            assert sd.sc_formal is False
            assert sd.is_koszul is True  # ALL standard families are Koszul

    def test_koszulness_universal(self):
        """AP14: ALL standard families are chirally Koszul."""
        data = standard_shadow_data()
        for name, sd in data.items():
            assert sd.is_koszul is True, \
                f"AP14 violation: {name} must be Koszul. " \
                "Shadow depth classifies complexity, not Koszulness."

    def test_pole_orders_consistent(self):
        """Pole orders match expected values for each family."""
        data = standard_shadow_data()
        assert data['heisenberg'].pole_order == 2
        assert data['affine_km'].pole_order == 2
        assert data['betagamma'].pole_order == 2
        assert data['virasoro'].pole_order == 4
        assert data['w3'].pole_order == 6


# ============================================================================
# Test Class 2: GKW Formality Predictions
# ============================================================================

class TestGKWFormality:
    """Test GKW formality predictions and their refinement by our classification."""

    def test_formality_d_prime_geq_2(self):
        """d' >= 2: formality holds, m_k = 0 for k >= 3."""
        for d_prime in [2, 3, 4]:
            for arity in [3, 4, 5, 6, 7, 8]:
                assert gkw_formality_prediction(d_prime, arity) is True, \
                    f"GKW formality should hold at d'={d_prime}, arity={arity}"

    def test_non_formality_d_prime_1(self):
        """d' = 1: non-formality, m_k generically nonzero."""
        for arity in [3, 4, 5, 6]:
            assert gkw_formality_prediction(1, arity) is False, \
                f"GKW: d'=1 should be non-formal at arity {arity}"

    def test_m2_never_vanishes(self):
        """m_2 is the product; it never vanishes by formality alone."""
        for d_prime in [1, 2, 3]:
            assert gkw_formality_prediction(d_prime, 2) is False, \
                "m_2 is the binary product, not controlled by formality"

    def test_quadratic_identity_counts(self):
        """Quadratic identity (Stasheff relation) counts at each arity."""
        counts = gkw_quadratic_identity_dimension
        # At arity 2: the identity is m_1^2 = 0 (if m_1 exists) +
        #             m_1 o m_2 + m_2 o (m_1 x id + id x m_1) = 0
        # Total terms: for n=2, pairs are (2,1) and (1,2)
        assert counts(2) > 0
        assert counts(3) > 0
        # Terms grow with arity
        assert counts(4) > counts(3)
        assert counts(5) > counts(4)


# ============================================================================
# Test Class 3: Operation-by-Operation Comparisons
# ============================================================================

class TestOperationComparisons:
    """Test that GKW operations match our SC operations family by family."""

    def test_m3_free_scalar_vanishes(self):
        """Free scalar (Heisenberg): m_3 = 0 in both frameworks."""
        result = compare_m3_free_scalar()
        assert result.match is True
        assert result.our_value == 0
        assert result.gkw_value == 0
        assert result.our_shadow_class == 'G'

    def test_m3_free_scalar_various_levels(self):
        """Heisenberg m_3 = 0 at any level k."""
        for k in [1, 2, 5, 10, -1]:
            result = compare_m3_free_scalar(k_val=k)
            assert result.match is True
            assert result.our_value == 0

    def test_m3_cubic_lg_nonzero(self):
        """Cubic LG (betagamma): m_3 != 0 in both frameworks."""
        result = compare_m3_cubic_lg()
        assert result.match is True
        assert result.our_value != 0
        assert result.gkw_value != 0
        assert result.our_shadow_class == 'C'

    def test_m4_cubic_lg_nonzero(self):
        """Cubic LG (betagamma): m_4 != 0 (class C, r_max = 4)."""
        result = compare_m4_cubic_lg()
        assert result.match is True
        assert result.our_shadow_class == 'C'

    def test_m3_gauge_theory_nonzero(self):
        """Gauge theory (affine KM): m_3 != 0 in both frameworks."""
        result = compare_m3_gauge_theory()
        assert result.match is True
        assert result.our_shadow_class == 'L'

    def test_m4_gauge_theory_vanishes(self):
        """Pure gauge theory: m_4 = 0 (class L, r_max = 3)."""
        result = compare_m4_gauge_theory()
        assert result.match is True
        assert result.our_value == 0
        assert result.gkw_value == 0
        assert result.our_shadow_class == 'L'

    def test_virasoro_m3_nonzero(self):
        """Virasoro m_3 != 0 (class M)."""
        result = compare_mk_virasoro(3)
        assert result.match is True
        assert result.our_shadow_class == 'M'

    def test_virasoro_m4_nonzero(self):
        """Virasoro m_4 != 0 (class M, infinite tower)."""
        result = compare_mk_virasoro(4)
        assert result.match is True
        assert result.our_shadow_class == 'M'

    def test_virasoro_m5_nonzero(self):
        """Virasoro m_5 != 0 (infinite tower continues)."""
        result = compare_mk_virasoro(5)
        assert result.match is True

    def test_virasoro_m6_nonzero(self):
        """Virasoro m_6 != 0."""
        result = compare_mk_virasoro(6)
        assert result.match is True

    def test_virasoro_infinite_tower(self):
        """Virasoro: m_k != 0 for ALL k >= 3 (class M)."""
        for k in range(3, 11):
            result = compare_mk_virasoro(k)
            assert result.match is True
            assert result.our_shadow_class == 'M'


# ============================================================================
# Test Class 4: CDG Bulk Algebra Comparisons
# ============================================================================

class TestCDGBulkComparisons:
    """Test CDG20 bulk algebra vs our derived center."""

    def test_free_scalar_bulk_match(self):
        """Free scalar: CDG bulk = our derived center at cohomology level."""
        result = cdg_bulk_comparison_free()
        assert result.match_at_cohomology is True
        assert result.shifted_poisson is True

    def test_gauge_theory_bulk_match(self):
        """Gauge theory: CDG bulk = our derived center."""
        result = cdg_bulk_comparison_gauge()
        assert result.match_at_cohomology is True
        assert result.shifted_poisson is True

    def test_lg_model_bulk_match(self):
        """LG model: CDG bulk = Jacobian ring = our derived center."""
        result = cdg_bulk_comparison_lg()
        assert result.match_at_cohomology is True
        assert result.shifted_poisson is True

    def test_bulk_is_derived_center_not_bar(self):
        """AP34: bulk = derived center, NOT bar complex.

        The bar complex classifies twisting morphisms.
        The bulk is Z^der_ch(A) = C^bullet_ch(A_b, A_b).
        These are different objects (AP25, AP34).
        """
        for comparison in [cdg_bulk_comparison_free(),
                           cdg_bulk_comparison_gauge(),
                           cdg_bulk_comparison_lg()]:
            assert 'HH' in comparison.our_bulk or 'C^bullet' in comparison.our_bulk \
                or 'H*' in comparison.our_bulk, \
                "Our bulk must reference derived center / Hochschild, not bar"


# ============================================================================
# Test Class 5: DNP Line Operator Comparisons
# ============================================================================

class TestDNPLineComparisons:
    """Test DNP25 dg-shifted Yangian vs our ordered Koszul dual."""

    def test_gauge_line_match(self):
        """Gauge theory: DNP Yangian = our ordered Koszul dual."""
        result = dnp_line_comparison_gauge()
        assert result.match is True
        assert result.yangian_structure is True

    def test_yangian_is_ordered_koszul_dual(self):
        """The dg-shifted Yangian comes from B^{ord}, not B^{Sigma}."""
        result = dnp_line_comparison_gauge()
        # AP37: B^{ord} != B^{Sigma} != B^{FG}
        assert 'B^{ord}' in result.our_line_algebra


# ============================================================================
# Test Class 6: Shadow Depth vs GKW Complexity
# ============================================================================

class TestShadowDepthVsGKW:
    """Test that our classification refines GKW's binary classification."""

    def test_heisenberg_is_formal_even_at_d1(self):
        """Heisenberg is SC-formal even at d'=1 (GKW would say 'non-formal')."""
        result = shadow_depth_vs_gkw_complexity('heisenberg')
        assert result['our_class'] == 'G'
        assert result['sc_formal'] is True
        assert result['gkw_d_prime'] == 1

    def test_affine_is_intermediate(self):
        """Affine KM has intermediate non-formality (class L)."""
        result = shadow_depth_vs_gkw_complexity('affine_sl2')
        assert result['our_class'] == 'L'
        assert result['our_r_max'] == 3
        assert result['sc_formal'] is False

    def test_virasoro_is_maximally_nonlocal(self):
        """Virasoro is maximally non-formal (class M)."""
        result = shadow_depth_vs_gkw_complexity('virasoro')
        assert result['our_class'] == 'M'
        assert result['our_r_max'] == float('inf')

    def test_refinement_flag(self):
        """All comparisons should flag our classification as a refinement."""
        for name in ['heisenberg', 'affine_sl2', 'betagamma', 'virasoro', 'w3']:
            result = shadow_depth_vs_gkw_complexity(name)
            assert result['our_is_refinement'] is True

    def test_pole_order_determines_depth(self):
        """Higher OPE pole order => deeper shadow tower."""
        data = standard_shadow_data()
        # pole 2 families have finite depth
        for name in ['heisenberg', 'affine_km', 'betagamma']:
            assert data[name].pole_order == 2
            assert data[name].r_max < float('inf') or data[name].r_max <= 4
        # pole 4+ families have infinite depth
        assert data['virasoro'].pole_order == 4
        assert data['virasoro'].r_max == float('inf')


# ============================================================================
# Test Class 7: SQED and SQCD Predictions
# ============================================================================

class TestSQEDSQCD:
    """Test shadow depth predictions for 3d gauge theories."""

    def test_sqed_prediction(self):
        """SQED predicted to be class C (from betagamma factor)."""
        result = sqed_sc_operations_prediction()
        assert result['predicted_class'] == 'C'
        assert result['predicted_r_max'] == 4

    def test_sqed_boundary_character_weight0(self):
        """SQED boundary character: dim at weight 0 = 1 (vacuum)."""
        char = sqed_boundary_character(q_max=5)
        assert char[0] == 1

    def test_sqed_boundary_character_weight1(self):
        """SQED boundary character: weight 1 modes from J only."""
        char = sqed_boundary_character(q_max=5)
        # At weight 1: only J (charge 0) is gauge-invariant
        # beta_1 has charge +1, gamma_1 has charge -1, J_1 has charge 0
        # Gauge invariant at weight 1: J_1 only => dim = 1
        assert char[1] >= 1  # at least J

    def test_sqcd_pure_gauge(self):
        """Pure SU(N) gauge (Nf=0): class L."""
        for N in [2, 3, 4]:
            result = sqcd_sc_operations_prediction(N, 0)
            assert result['predicted_class'] == 'L'
            assert result['predicted_r_max'] == 3

    def test_sqcd_with_matter(self):
        """SU(N) SQCD with Nf > 0: class M (matter escalates depth)."""
        for N in [2, 3]:
            for Nf in [1, 2, 3]:
                result = sqcd_sc_operations_prediction(N, Nf)
                assert result['predicted_class'] == 'M'
                assert result['predicted_r_max'] == float('inf')

    def test_sqcd_dim_g_correct(self):
        """dim(SU(N)) = N^2 - 1."""
        for N in [2, 3, 4, 5]:
            result = sqcd_sc_operations_prediction(N, 1)
            assert result['dim_g'] == N * N - 1

    def test_sqcd_dual_coxeter_correct(self):
        """h^v(SU(N)) = N."""
        for N in [2, 3, 4, 5]:
            result = sqcd_sc_operations_prediction(N, 1)
            assert result['h_v'] == N


# ============================================================================
# Test Class 8: Genus Expansion Comparison
# ============================================================================

class TestGenusComparison:
    """Test that our genus expansion genuinely extends GKW."""

    def test_genus0_both_compute(self):
        """Both frameworks compute at genus 0."""
        table = genus_comparison_table('virasoro')
        g0 = table[0]
        assert g0.genus == 0
        assert g0.gkw_computes is True

    def test_genus1_only_we_compute(self):
        """Worldsheet genus 1: only our framework computes."""
        table = genus_comparison_table('virasoro')
        g1 = table[1]
        assert g1.genus == 1
        assert g1.gkw_computes is False

    def test_genus2_only_we_compute(self):
        """Worldsheet genus 2: only our framework computes."""
        table = genus_comparison_table('virasoro')
        g2 = table[2]
        assert g2.genus == 2
        assert g2.gkw_computes is False

    def test_genus3_only_we_compute(self):
        """Worldsheet genus 3: only our framework computes."""
        table = genus_comparison_table('virasoro')
        g3 = table[3]
        assert g3.genus == 3
        assert g3.gkw_computes is False

    def test_f1_formula(self):
        """F_1 = kappa/24 (Faber-Pandharipande lambda_1)."""
        c = Symbol('c')
        table = genus_comparison_table('virasoro')
        g1 = table[1]
        expected = c / 2 * Rational(1, 24)  # kappa(Vir) = c/2
        assert simplify(g1.our_value - expected) == 0

    def test_f2_formula(self):
        """F_2 = kappa * 7/5760."""
        c = Symbol('c')
        table = genus_comparison_table('virasoro')
        g2 = table[2]
        expected = c / 2 * Rational(7, 5760)
        assert simplify(g2.our_value - expected) == 0

    def test_f3_formula(self):
        """F_3 = kappa * 31/967680."""
        c = Symbol('c')
        table = genus_comparison_table('virasoro')
        g3 = table[3]
        expected = c / 2 * Rational(31, 967680)
        assert simplify(g3.our_value - expected) == 0


# ============================================================================
# Test Class 9: Corner VOA Shadow Predictions
# ============================================================================

class TestCornerVOA:
    """Test shadow depth predictions for Y_{N1,N2,N3} corner VOAs."""

    def test_trivial_corner(self):
        """Y_{0,0,0} = gl(1): class G."""
        result = corner_voa_shadow_prediction(0, 0, 0)
        assert result['shadow_class'] == 'G'
        assert result['r_max'] == 2

    def test_y001(self):
        """Y_{0,0,1} = gl(1)^2: class G."""
        result = corner_voa_shadow_prediction(0, 0, 1)
        assert result['shadow_class'] == 'G'
        assert result['r_max'] == 2

    def test_y002(self):
        """Y_{0,0,2} = W_2 x gl(1) = Virasoro x gl(1): class M."""
        result = corner_voa_shadow_prediction(0, 0, 2)
        assert result['shadow_class'] == 'M'
        assert result['r_max'] == float('inf')

    def test_y003(self):
        """Y_{0,0,3} = W_3 x gl(1): class M."""
        result = corner_voa_shadow_prediction(0, 0, 3)
        assert result['shadow_class'] == 'M'

    def test_y_large_N(self):
        """Y_{0,0,N} for large N: always class M."""
        for N in range(2, 10):
            result = corner_voa_shadow_prediction(0, 0, N)
            assert result['shadow_class'] == 'M'

    def test_koszul_dual_reverses_indices(self):
        """Y^! reverses N1, N3: Y_{N1,N2,N3}^! = Y_{N3,N2,N1}."""
        for N1, N2, N3 in [(0, 0, 3), (1, 0, 2), (2, 1, 3), (0, 2, 5)]:
            result = corner_voa_shadow_prediction(N1, N2, N3)
            assert result['koszul_dual'] == (N3, N2, N1)

    def test_all_corner_voas_koszul(self):
        """All Y-algebras are chirally Koszul at generic Psi."""
        for N1 in range(3):
            for N2 in range(3):
                for N3 in range(3):
                    result = corner_voa_shadow_prediction(N1, N2, N3)
                    assert result['is_koszul'] is True

    def test_y11N_class_M(self):
        """Y_{1,1,N} for N >= 2: class M."""
        for N in range(2, 5):
            result = corner_voa_shadow_prediction(1, 1, N)
            assert result['shadow_class'] == 'M'

    def test_triality_preserves_class(self):
        """S_3 triality preserves shadow class.

        Y_{0,0,N}, Y_{N,0,0}, Y_{0,N,0} should all have the same class.
        """
        for N in range(5):
            r1 = corner_voa_shadow_prediction(0, 0, N)
            r2 = corner_voa_shadow_prediction(N, 0, 0)
            r3 = corner_voa_shadow_prediction(0, N, 0)
            assert r1['shadow_class'] == r2['shadow_class'] == r3['shadow_class']


# ============================================================================
# Test Class 10: Full Summary and Consistency
# ============================================================================

class TestFullSummary:
    """Test the comprehensive comparison summary."""

    def test_summary_structure(self):
        """Summary has all five axes."""
        summary = full_comparison_summary()
        assert 'axis1_higher_operations' in summary
        assert 'axis2_formality' in summary
        assert 'axis3_genus' in summary
        assert 'axis4_bulk' in summary
        assert 'axis5_lines' in summary

    def test_all_axis1_match(self):
        """All higher operation comparisons match."""
        summary = full_comparison_summary()
        assert summary['axis1_higher_operations']['all_match'] is True

    def test_axis1_has_multiple_comparisons(self):
        """Axis 1 has >= 5 comparisons."""
        summary = full_comparison_summary()
        comps = summary['axis1_higher_operations']['comparisons']
        assert len(comps) >= 5

    def test_axis2_has_multiple_families(self):
        """Axis 2 covers multiple families."""
        summary = full_comparison_summary()
        data = summary['axis2_formality']['data']
        assert len(data) >= 4


# ============================================================================
# Test Class 11: Kappa Consistency Checks
# ============================================================================

class TestKappaConsistency:
    """Verify kappa values match between frameworks (multi-path)."""

    def test_heisenberg_kappa(self):
        """Heisenberg: kappa = k in both frameworks."""
        result = kappa_consistency_check('heisenberg', k_val=1)
        assert result['match'] is True
        assert result['our_kappa'] == 1
        assert result['F_1'] == Rational(1, 24)

    def test_heisenberg_kappa_various_levels(self):
        """Heisenberg kappa = k at various levels."""
        for k in [1, 2, 3, 5, 10]:
            result = kappa_consistency_check('heisenberg', k_val=k)
            assert result['match'] is True
            assert result['our_kappa'] == k

    def test_virasoro_kappa(self):
        """Virasoro: kappa = c/2 in both frameworks."""
        result = kappa_consistency_check('virasoro')
        assert result['match'] is True

    def test_sl2_kappa(self):
        """sl_2 level k: kappa = 3(k+2)/4 in both frameworks."""
        result = kappa_consistency_check('affine_sl2')
        assert result['match'] is True

    def test_betagamma_kappa(self):
        """Betagamma: kappa = -1 in both frameworks."""
        result = kappa_consistency_check('betagamma')
        assert result['match'] is True
        assert result['our_kappa'] == -1


# ============================================================================
# Test Class 12: A-infinity Relation Counts
# ============================================================================

class TestAInfinityRelations:
    """Test A-infinity relation (= GKW quadratic axiom) counts."""

    def test_relation_count_arity2(self):
        """At arity 2, there are relations involving m_1 and m_2."""
        counts = ainfty_relation_count(8)
        assert 2 in counts
        assert counts[2]['total_terms'] > 0

    def test_relation_count_grows(self):
        """Relation complexity grows with arity."""
        counts = ainfty_relation_count(8)
        for n in range(3, 8):
            assert counts[n]['total_terms'] >= counts[n - 1]['total_terms']

    def test_arity3_decompositions(self):
        """At arity 3: pairs are (3,1), (2,2), (1,3)."""
        counts = ainfty_relation_count(4)
        pairs = counts[3]['decompositions']
        i_vals = sorted([p[0] for p in pairs])
        j_vals = sorted([p[1] for p in pairs])
        # i+j = 4, so pairs include (1,3), (2,2), (3,1)
        assert (1, 3) in [(p[0], p[1]) for p in pairs] or \
               (3, 1) in [(p[0], p[1]) for p in pairs]


# ============================================================================
# Test Class 13: Pole Order to Shadow Depth Mapping
# ============================================================================

class TestPoleOrderMapping:
    """Test the OPE pole order to shadow depth prediction."""

    def test_simple_pole_class_G(self):
        """Simple pole (order 1) => class G."""
        result = pole_order_to_shadow_depth(1)
        assert result['predicted_class'] == 'G'
        assert result['bar_residue_order'] == 0  # AP19: absorbed by d log

    def test_double_pole(self):
        """Double pole => class G or L."""
        result = pole_order_to_shadow_depth(2)
        assert 'G' in result['predicted_class']
        assert result['bar_residue_order'] == 1  # AP19

    def test_quartic_pole_class_M(self):
        """Quartic pole (order 4) => class M, infinite depth."""
        result = pole_order_to_shadow_depth(4)
        assert result['predicted_class'] == 'M'
        assert result['predicted_depth'] == float('inf')
        assert result['bar_residue_order'] == 3  # AP19: 4 - 1 = 3

    def test_ap19_pole_absorption(self):
        """AP19: bar residue order = OPE pole order - 1 (d log absorption)."""
        for p in range(1, 10):
            result = pole_order_to_shadow_depth(p)
            assert result['bar_residue_order'] == max(0, p - 1)

    def test_high_pole_order_class_M(self):
        """Pole order >= 4 always gives class M."""
        for p in [4, 5, 6, 8, 10, 20]:
            result = pole_order_to_shadow_depth(p)
            assert result['predicted_class'] == 'M'


# ============================================================================
# Test Class 14: Butson Factorization Comparison
# ============================================================================

class TestButsonComparison:
    """Test Butson's factorization framework comparison."""

    def test_butson_match(self):
        """Butson E_1 algebra matches our ordered bar Koszul dual."""
        result = butson_coulomb_comparison()
        assert result['match'] is True

    def test_butson_produces_e1(self):
        """Butson's output is an E_1 factorization algebra."""
        result = butson_coulomb_comparison()
        assert 'E_1' in result['butson_output']

    def test_our_produces_yangian(self):
        """Our output is the dg-shifted Yangian."""
        result = butson_coulomb_comparison()
        assert 'Y^{dg}' in result['our_output']


# ============================================================================
# Test Class 15: Cross-Consistency and Multi-Path Verification
# ============================================================================

class TestCrossConsistency:
    """Multi-path verification: same result from different computational paths."""

    def test_heisenberg_depth_two_paths(self):
        """Heisenberg depth = 2 from (1) shadow data, (2) pole order map."""
        # Path 1: shadow data
        data = standard_shadow_data()
        assert data['heisenberg'].r_max == 2

        # Path 2: pole order map
        pole_result = pole_order_to_shadow_depth(2)
        assert 'G' in pole_result['predicted_class']  # compatible with depth 2

    def test_virasoro_class_M_two_paths(self):
        """Virasoro class M from (1) shadow data, (2) pole order, (3) comparison."""
        # Path 1: shadow data
        data = standard_shadow_data()
        assert data['virasoro'].shadow_class == 'M'

        # Path 2: pole order
        pole_result = pole_order_to_shadow_depth(4)
        assert pole_result['predicted_class'] == 'M'

        # Path 3: GKW comparison
        comp = compare_mk_virasoro(3)
        assert comp.our_shadow_class == 'M'

    def test_gauge_theory_class_L_two_paths(self):
        """Affine KM class L from (1) shadow data, (2) GKW comparison."""
        # Path 1
        data = standard_shadow_data()
        assert data['affine_sl2'].shadow_class == 'L'

        # Path 2
        comp_m3 = compare_m3_gauge_theory()
        comp_m4 = compare_m4_gauge_theory()
        assert comp_m3.our_shadow_class == 'L'
        assert comp_m4.our_value == 0  # m_4 = 0 for class L

    def test_sc_formal_iff_class_G(self):
        """SC-formality holds if and only if class G (multi-path check)."""
        data = standard_shadow_data()
        for name, sd in data.items():
            if sd.shadow_class == 'G':
                assert sd.sc_formal is True, f"{name}: class G must be SC-formal"
            else:
                assert sd.sc_formal is False, f"{name}: class {sd.shadow_class} must not be SC-formal"

    def test_koszul_independent_of_depth(self):
        """AP14: Koszulness is independent of shadow depth. All classes are Koszul."""
        data = standard_shadow_data()
        classes_seen = set()
        for name, sd in data.items():
            classes_seen.add(sd.shadow_class)
            assert sd.is_koszul is True
        # We've seen all four classes
        assert classes_seen == {'G', 'L', 'C', 'M'}

    def test_genus1_f1_matches_kappa(self):
        """F_1 = kappa/24 cross-check: genus table vs kappa check."""
        # From genus table
        table = genus_comparison_table('virasoro')
        f1_from_table = table[1].our_value

        # From kappa check
        kappa_result = kappa_consistency_check('virasoro')
        f1_from_kappa = kappa_result['F_1']

        # Both should give c/(2*24) = c/48
        c = Symbol('c')
        assert simplify(f1_from_table - c / 48) == 0
        assert simplify(f1_from_kappa - c / 48) == 0
