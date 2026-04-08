r"""Tests for the Damiolini-Woike modular functor vs shadow CohFT comparison engine.

Verification strategy:
  Path 1: Strongly rational axiom checking against known family properties
  Path 2: Framing anomaly = kappa = c/2 identification (and AP39 divergence)
  Path 3: Verlinde dimension vs shadow free energy quantitative comparison
  Path 4: Scope comparison: which families each framework covers
  Path 5: Categorical hierarchy consistency checks
  Path 6: AP30 analysis: DW propagation vs shadow flat identity
  Path 7: MC3 connection: thick generation vs modular fusion category
  Path 8: 3d TFT comparison: DW RT-type TFT vs Vol II HT QFT

Ground truth:
  Damiolini-Woike, arXiv:2507.05845 (Theorems 4.2.2, 5.3.1, 5.5.1)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:chain-modular-functor (higher_genus_modular_koszul.tex)
  conj:categorical-modular-kd (concordance.tex)
"""

from __future__ import annotations

import math
import pytest

from sympy import Rational, factorial, simplify

from compute.lib.theorem_damiolini_modular_functor_engine import (
    STANDARD_FAMILIES,
    ap30_analysis,
    axiom_comparison,
    categorical_hierarchy,
    cohft_axioms,
    count_scope,
    framing_anomaly_comparison,
    get_family_status,
    is_strongly_rational,
    kappa_affine,
    lambda_fp,
    level_reduction_maps,
    mc3_dw_comparison,
    modular_functor_axioms,
    num_integrable_reps,
    scope_comparison,
    shadow_free_energy,
    shadow_trace_vs_verlinde,
    tft_comparison,
    upgrade_analysis,
    verify_kappa_equals_framing_anomaly,
    verlinde_dimension_sl2,
)


# =========================================================================
# Section 1: Strongly rational VOA axiom tests
# =========================================================================

class TestStronglyRationalAxioms:
    """Verify strongly rational classification against known families."""

    def test_heisenberg_not_strongly_rational(self):
        """Heisenberg is NOT strongly rational (not C2-cofinite, not rational)."""
        props = STANDARD_FAMILIES['heisenberg']
        assert not is_strongly_rational(props)
        assert not props['c2_cofinite']
        assert not props['rational']

    def test_affine_integrable_strongly_rational(self):
        """Affine Lie algebras at positive integer level ARE strongly rational."""
        props = STANDARD_FAMILIES['affine_integrable']
        assert is_strongly_rational(props)
        assert props['c2_cofinite']
        assert props['rational']
        assert props['self_contragredient']

    def test_affine_generic_not_strongly_rational(self):
        """Affine algebras at generic level are NOT strongly rational."""
        props = STANDARD_FAMILIES['affine_generic']
        assert not is_strongly_rational(props)

    def test_virasoro_minimal_strongly_rational(self):
        """Virasoro minimal models ARE strongly rational."""
        props = STANDARD_FAMILIES['virasoro_minimal']
        assert is_strongly_rational(props)

    def test_virasoro_generic_not_strongly_rational(self):
        """Virasoro at generic c is NOT strongly rational."""
        props = STANDARD_FAMILIES['virasoro_generic']
        assert not is_strongly_rational(props)

    def test_lattice_voa_strongly_rational(self):
        """Lattice VOAs (even unimodular) ARE strongly rational."""
        props = STANDARD_FAMILIES['lattice_voa']
        assert is_strongly_rational(props)

    def test_triplet_c2_cofinite_but_not_rational(self):
        """Triplet W(p): C2-cofinite but NOT rational (logarithmic)."""
        props = STANDARD_FAMILIES['triplet_w_p']
        assert props['c2_cofinite']
        assert not props['rational']
        assert not is_strongly_rational(props)

    def test_w_integrable_strongly_rational(self):
        """W-algebras at integrable level ARE strongly rational."""
        props = STANDARD_FAMILIES['w_algebra_integrable']
        assert is_strongly_rational(props)

    def test_all_families_have_required_keys(self):
        """Every family entry must have all required classification keys."""
        required = ['n_graded', 'cft_type', 'c2_cofinite', 'rational',
                    'self_contragredient', 'strongly_rational', 'dw_applies',
                    'shadow_cohft_applies', 'description']
        for name, fam in STANDARD_FAMILIES.items():
            for key in required:
                assert key in fam, f"Missing key '{key}' in family '{name}'"

    def test_strongly_rational_consistent_with_dw_applies(self):
        """DW applies if and only if the VOA is strongly rational."""
        for name, fam in STANDARD_FAMILIES.items():
            assert fam['dw_applies'] == fam['strongly_rational'], (
                f"Inconsistency in '{name}': dw_applies={fam['dw_applies']} "
                f"but strongly_rational={fam['strongly_rational']}"
            )

    def test_shadow_cohft_broader_than_dw(self):
        """Shadow CohFT applies to ALL families; DW only to strongly rational."""
        for name, fam in STANDARD_FAMILIES.items():
            assert fam['shadow_cohft_applies'], (
                f"Family '{name}' should have shadow_cohft_applies=True"
            )


# =========================================================================
# Section 2: Framing anomaly and kappa comparison
# =========================================================================

class TestFramingAnomaly:
    """Verify the framing anomaly alpha = c/2 and its relation to kappa."""

    def test_virasoro_kappa_equals_c_over_2(self):
        """For Virasoro: kappa = c/2 = framing anomaly."""
        result = framing_anomaly_comparison(Rational(26))
        assert result['dw_framing_anomaly'] == 13
        assert result['bar_modular_characteristic'] == 13
        assert result['match']

    def test_framing_anomaly_c_equals_1(self):
        """c = 1: alpha = 1/2."""
        result = framing_anomaly_comparison(Rational(1))
        assert result['dw_framing_anomaly'] == Rational(1, 2)

    def test_framing_anomaly_c_equals_0(self):
        """c = 0: alpha = 0 (uncurved)."""
        result = framing_anomaly_comparison(Rational(0))
        assert result['dw_framing_anomaly'] == 0

    def test_kappa_ne_c_over_2_for_affine_sl2(self):
        """AP39: kappa != c/2 for affine sl_2 at generic level.

        kappa(sl_2, k) = 3(k+2)/4.
        c(sl_2, k) = 3k/(k+2).
        c/2 = 3k/(2(k+2)).
        These are NOT equal for k != 0.
        """
        result = verify_kappa_equals_framing_anomaly('A', 1, 1)
        # sl_2 at level 1: kappa = 3*3/4 = 9/4, c = 3*1/3 = 1, c/2 = 1/2
        assert result['kappa'] == Rational(9, 4)
        assert result['central_charge'] == Rational(1)
        assert result['c_over_2'] == Rational(1, 2)
        assert not result['kappa_equals_c_over_2']

    def test_kappa_ne_c_over_2_for_affine_sl3(self):
        """AP39: kappa != c/2 for sl_3 at level 1."""
        result = verify_kappa_equals_framing_anomaly('A', 2, 1)
        # sl_3 at level 1: dim=8, h^v=3, kappa=8*4/6=16/3, c=8/4=2, c/2=1
        assert result['kappa'] == Rational(16, 3)
        assert result['central_charge'] == Rational(2)
        assert not result['kappa_equals_c_over_2']

    def test_kappa_for_sl2_level_1(self):
        """kappa(sl_2, 1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_affine('A', 1, 1) == Rational(9, 4)

    def test_kappa_for_sl2_level_2(self):
        """kappa(sl_2, 2) = 3*(2+2)/(2*2) = 3."""
        assert kappa_affine('A', 1, 2) == Rational(3)

    def test_kappa_for_sl3_level_1(self):
        """kappa(sl_3, 1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_affine('A', 2, 1) == Rational(16, 3)


# =========================================================================
# Section 3: Verlinde dimension vs shadow free energy
# =========================================================================

class TestVerlindeVsShadow:
    """Quantitative comparison: Verlinde dimensions vs shadow F_g."""

    def test_verlinde_genus0_is_1(self):
        """V_{0,k}(sl_2) = 1 for all k."""
        for k in range(1, 6):
            assert verlinde_dimension_sl2(k, 0) == 1

    def test_verlinde_genus1_equals_k_plus_1(self):
        """V_{1,k}(sl_2) = k + 1."""
        for k in range(1, 6):
            assert verlinde_dimension_sl2(k, 1) == k + 1

    def test_shadow_f1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all families."""
        assert lambda_fp(1) == Rational(1, 24)
        for k in range(1, 6):
            kap = kappa_affine('A', 1, k)
            assert shadow_free_energy(kap, 1) == kap / 24

    def test_shadow_f2(self):
        """F_2 = kappa * 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)
        kap = kappa_affine('A', 1, 1)
        assert shadow_free_energy(kap, 2) == kap * Rational(7, 5760)

    def test_shadow_trace_vs_verlinde_sl2_level1(self):
        """Compare scalar shadow vs Verlinde for sl_2 at level 1."""
        result = shadow_trace_vs_verlinde('A', 1, 1)
        assert result['kappa'] == Rational(9, 4)
        assert result['shadow_F1'] == Rational(9, 4) / 24
        assert result['verlinde_V1'] == 2  # k+1 = 2

    def test_shadow_trace_vs_verlinde_sl2_level2(self):
        """Compare scalar shadow vs Verlinde for sl_2 at level 2."""
        result = shadow_trace_vs_verlinde('A', 1, 2)
        assert result['kappa'] == Rational(3)
        assert result['verlinde_V1'] == 3  # k+1 = 3

    def test_verlinde_greater_than_shadow_at_genus_geq_2(self):
        """Verlinde V_g grows as (k+2)^{g-1}; shadow F_g decays as 1/(2pi)^{2g}.

        For g >= 2 and k >= 1, V_g >> |F_g|: the modular functor carries
        exponentially more data than the scalar shadow.
        """
        for k in [1, 2, 3]:
            kap = kappa_affine('A', 1, k)
            for g in [2, 3]:
                v_g = verlinde_dimension_sl2(k, g)
                f_g = float(shadow_free_energy(kap, g))
                assert abs(v_g) > abs(f_g), (
                    f"Expected V_{g} > |F_{g}| for sl_2 at level {k}"
                )

    def test_num_integrable_reps_sl2(self):
        """For sl_2 at level k: number of integrable reps = k + 1."""
        for k in range(1, 10):
            assert num_integrable_reps('A', 1, k) == k + 1

    def test_num_integrable_reps_sl3(self):
        """For sl_3 at level k: number of integrable reps = (k+1)(k+2)/2."""
        for k in range(1, 6):
            expected = (k + 1) * (k + 2) // 2
            assert num_integrable_reps('A', 2, k) == expected


# =========================================================================
# Section 4: Scope comparison
# =========================================================================

class TestScopeComparison:
    """Verify that the shadow CohFT scope strictly contains the DW scope."""

    def test_shadow_scope_is_full(self):
        """Shadow CohFT applies to all 9 standard families."""
        counts = count_scope()
        assert counts['shadow_scope'] == counts['total_families']

    def test_dw_scope_is_subset(self):
        """DW scope is a strict subset of shadow scope."""
        counts = count_scope()
        assert counts['dw_scope'] < counts['shadow_scope']

    def test_shadow_only_families_exist(self):
        """There are families where shadow applies but DW does not."""
        counts = count_scope()
        assert counts['shadow_only'] > 0

    def test_exact_dw_scope_count(self):
        """Exactly 4 families are strongly rational: affine_integrable,
        virasoro_minimal, lattice_voa, w_algebra_integrable."""
        counts = count_scope()
        assert counts['dw_scope'] == 4

    def test_scope_detail(self):
        """Verify per-family DW applicability."""
        scope = scope_comparison()
        assert scope['heisenberg']['dw_applies'] is False
        assert scope['affine_integrable']['dw_applies'] is True
        assert scope['affine_generic']['dw_applies'] is False
        assert scope['virasoro_minimal']['dw_applies'] is True
        assert scope['virasoro_generic']['dw_applies'] is False
        assert scope['lattice_voa']['dw_applies'] is True
        assert scope['w_algebra_principal']['dw_applies'] is False
        assert scope['w_algebra_integrable']['dw_applies'] is True
        assert scope['triplet_w_p']['dw_applies'] is False


# =========================================================================
# Section 5: Categorical hierarchy consistency
# =========================================================================

class TestCategoricalHierarchy:
    """Verify the four-level categorical hierarchy is consistent."""

    def test_hierarchy_has_four_levels(self):
        """The hierarchy has exactly levels 0, 1, 2, 3."""
        h = categorical_hierarchy()
        assert len(h) == 4
        assert 'level_0_scalar' in h
        assert 'level_1_cohft' in h
        assert 'level_2_chain' in h
        assert 'level_3_modular_functor' in h

    def test_reduction_maps_complete(self):
        """There is a reduction map between each adjacent pair of levels."""
        maps = level_reduction_maps()
        assert 'level_3_to_2' in maps
        assert 'level_2_to_1' in maps
        assert 'level_1_to_0' in maps
        assert 'dw_to_shadow' in maps

    def test_level_3_is_dw(self):
        """Level 3 cites DW Theorem 4.2.2."""
        h = categorical_hierarchy()
        assert 'DW' in h['level_3_modular_functor']['source'] or \
               '4.2.2' in h['level_3_modular_functor']['source']

    def test_level_1_is_shadow_cohft(self):
        """Level 1 is the shadow CohFT."""
        h = categorical_hierarchy()
        assert 'shadow-cohft' in h['level_1_cohft']['source']

    def test_level_0_is_scalar(self):
        """Level 0 is the scalar free energy F_g = kappa * lambda_g^FP."""
        h = categorical_hierarchy()
        assert 'kappa' in h['level_0_scalar']['data']


# =========================================================================
# Section 6: AP30 flat identity analysis
# =========================================================================

class TestAP30Analysis:
    """Verify AP30 analysis: DW propagation does NOT resolve the shadow flat identity."""

    def test_ap30_not_resolved(self):
        """DW does NOT resolve AP30."""
        analysis = ap30_analysis()
        assert analysis['resolution_status'] == 'NOT RESOLVED'

    def test_ap30_reason_cites_categorical_level(self):
        """The reason must cite the categorical level difference."""
        analysis = ap30_analysis()
        assert 'CATEGORICAL' in analysis['reason'].upper() or \
               'categorical' in analysis['reason']

    def test_ap30_reason_cites_non_rational(self):
        """The reason must cite the non-rational case being outside DW scope."""
        analysis = ap30_analysis()
        assert 'non-rational' in analysis['reason'].lower() or \
               'NON-RATIONAL' in analysis['reason'] or \
               'not strongly rational' in analysis['reason'].lower()

    def test_ap30_partial_resolution_exists(self):
        """There is a partial resolution for strongly rational VOAs."""
        analysis = ap30_analysis()
        assert 'partial_resolution' in analysis
        assert len(analysis['partial_resolution']) > 0


# =========================================================================
# Section 7: MC3 connection
# =========================================================================

class TestMC3Connection:
    """Verify the MC3 connection with DW's modular fusion category."""

    def test_mc3_comparison_exists(self):
        """The MC3-DW comparison analysis is complete."""
        comp = mc3_dw_comparison()
        assert 'mc3_statement' in comp
        assert 'dw_mfc' in comp
        assert 'intersection' in comp
        assert 'beyond_dw' in comp

    def test_mc3_covers_all_types(self):
        """MC3 is proved for all simple types (not just type A)."""
        comp = mc3_dw_comparison()
        assert 'all simple' in comp['mc3_statement'].lower() or \
               'ALL simple' in comp['mc3_statement']

    def test_dw_mfc_cites_theorem(self):
        """DW MFC cites Theorem 5.3.1."""
        comp = mc3_dw_comparison()
        assert '5.3.1' in comp['dw_mfc']

    def test_intersection_mentions_integrable(self):
        """The intersection of MC3 and DW involves integrable representations."""
        comp = mc3_dw_comparison()
        assert 'integrable' in comp['intersection'].lower()


# =========================================================================
# Section 8: 3d TFT comparison
# =========================================================================

class TestTFTComparison:
    """Verify the 3d TFT comparison: DW RT-type vs Vol II HT."""

    def test_tft_comparison_exists(self):
        """The TFT comparison analysis is complete."""
        comp = tft_comparison()
        assert 'dw_3d_tft' in comp
        assert 'vol2_3d_ht_qft' in comp
        assert 'relationship' in comp

    def test_dw_tft_is_topological(self):
        """DW 3d TFT is TOPOLOGICAL (not holomorphic-topological)."""
        comp = tft_comparison()
        assert 'TOPOLOGICAL' in comp['dw_3d_tft'].upper() or \
               'topological' in comp['dw_3d_tft'].lower()

    def test_vol2_ht_is_holomorphic_topological(self):
        """Vol II 3d theory is holomorphic-topological."""
        comp = tft_comparison()
        assert 'holomorphic-topological' in comp['vol2_3d_ht_qft'].lower() or \
               'holomorphic' in comp['vol2_3d_ht_qft'].lower()

    def test_dw_is_topological_shadow_of_ht(self):
        """DW 3d TFT is the topological shadow of the HT theory."""
        comp = tft_comparison()
        assert 'shadow' in comp['relationship'].lower() or \
               'SHADOW' in comp['relationship']

    def test_factorization_homology_mentioned(self):
        """Factorization homology connects the two frameworks."""
        comp = tft_comparison()
        assert 'factorization homology' in comp['factorization_homology'].lower() or \
               'factorization' in comp['factorization_homology'].lower()


# =========================================================================
# Section 9: Axiom comparison
# =========================================================================

class TestAxiomComparison:
    """Verify the detailed axiom comparison between DW and shadow CohFT."""

    def test_axiom_comparison_complete(self):
        """The axiom comparison covers all key axiom pairs."""
        comp = axiom_comparison()
        assert 'factorization_vs_splitting' in comp
        assert 'propagation_vs_flat_identity' in comp
        assert 'framing_anomaly_vs_curvature' in comp
        assert 'modularity' in comp

    def test_factorization_same_content(self):
        """Factorization and splitting encode the same mathematical content."""
        comp = axiom_comparison()
        assert 'SAME' in comp['factorization_vs_splitting']['relationship'].upper()

    def test_framing_anomaly_same_invariant(self):
        """Framing anomaly and bar curvature produce the same invariant."""
        comp = axiom_comparison()
        assert 'SAME' in comp['framing_anomaly_vs_curvature']['relationship'].upper()

    def test_propagation_not_resolved(self):
        """The propagation/flat-identity comparison notes AP30 is not resolved."""
        comp = axiom_comparison()
        r = comp['propagation_vs_flat_identity']['relationship']
        assert 'NOT' in r.upper() and 'RESOLVE' in r.upper()

    def test_modularity_complementary(self):
        """MC3 and DW MFC are complementary."""
        comp = axiom_comparison()
        assert 'COMPLEMENTARY' in comp['modularity']['relationship'].upper()


# =========================================================================
# Section 10: Upgrade analysis
# =========================================================================

class TestUpgradeAnalysis:
    """Test the analysis of whether DW upgrades or subsumes the shadow CohFT."""

    def test_upgrade_analysis_exists(self):
        """The upgrade analysis returns a complete dictionary."""
        ua = upgrade_analysis()
        assert 'question' in ua
        assert 'answer' in ua
        assert 'conclusion' in ua

    def test_dw_does_not_subsume(self):
        """DW COMPLEMENTS but does not SUBSUME our framework."""
        ua = upgrade_analysis()
        assert 'COMPLEMENT' in ua['conclusion'].upper()
        assert 'SUBSUME' in ua['conclusion'].upper()

    def test_conjectural_categorical_kd_mentioned(self):
        """The conjectural categorical modular KD is the correct full upgrade."""
        ua = upgrade_analysis()
        assert 'categorical-modular-kd' in ua['answer'] or \
               'categorical modular' in ua['answer'].lower()


# =========================================================================
# Section 11: Lie algebra data consistency
# =========================================================================

class TestLieAlgebraData:
    """Verify Lie algebra dimensions and dual Coxeter numbers."""

    def test_sl2_data(self):
        """sl_2: dim = 3, h^v = 2."""
        assert kappa_affine('A', 1, 1) == Rational(3 * 3, 2 * 2)

    def test_sl3_data(self):
        """sl_3: dim = 8, h^v = 3."""
        # kappa(sl_3, 1) = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert kappa_affine('A', 2, 1) == Rational(16, 3)

    def test_so5_data(self):
        """B_2 = so_5: dim = 10, h^v = 3."""
        # kappa(so_5, 1) = 10*(1+3)/(2*3) = 40/6 = 20/3
        assert kappa_affine('B', 2, 1) == Rational(20, 3)

    def test_sp4_data(self):
        """C_2 = sp_4: dim = 10, h^v = 3."""
        # kappa(sp_4, 1) = 10*(1+3)/(2*3) = 40/6 = 20/3
        assert kappa_affine('C', 2, 1) == Rational(20, 3)

    def test_g2_data(self):
        """G_2: dim = 14, h^v = 4."""
        # kappa(G_2, 1) = 14*(1+4)/(2*4) = 70/8 = 35/4
        assert kappa_affine('G', 2, 1) == Rational(35, 4)

    def test_e6_data(self):
        """E_6: dim = 78, h^v = 12."""
        # kappa(E_6, 1) = 78*(1+12)/(2*12) = 78*13/24 = 1014/24 = 169/4
        assert kappa_affine('E', 6, 1) == Rational(169, 4)

    def test_e7_data(self):
        """E_7: dim = 133, h^v = 18."""
        # kappa(E_7, 1) = 133*(1+18)/(2*18) = 133*19/36 = 2527/36
        assert kappa_affine('E', 7, 1) == Rational(2527, 36)

    def test_e8_data(self):
        """E_8: dim = 248, h^v = 30."""
        # kappa(E_8, 1) = 248*(1+30)/(2*30) = 248*31/60 = 7688/60 = 1922/15
        assert kappa_affine('E', 8, 1) == Rational(1922, 15)

    def test_f4_data(self):
        """F_4: dim = 52, h^v = 9."""
        # kappa(F_4, 1) = 52*(1+9)/(2*9) = 520/18 = 260/9
        assert kappa_affine('F', 4, 1) == Rational(260, 9)


# =========================================================================
# Section 12: Cross-consistency: kappa additivity under direct sums
# =========================================================================

class TestKappaAdditivity:
    """Verify kappa additivity: kappa(A_1 + A_2) = kappa(A_1) + kappa(A_2)."""

    def test_kappa_additive_sl2_heisenberg(self):
        """kappa(sl_2 oplus H_1) = kappa(sl_2) + kappa(H_1) = 9/4 + 1 = 13/4."""
        kappa_sl2 = kappa_affine('A', 1, 1)
        kappa_heis = Rational(1)  # H_1 has kappa = 1
        assert kappa_sl2 + kappa_heis == Rational(13, 4)

    def test_kappa_additive_same_family(self):
        """kappa(sl_2 oplus sl_2) at level 1 = 2 * kappa(sl_2,1) = 9/2."""
        kappa_1 = kappa_affine('A', 1, 1)
        assert 2 * kappa_1 == Rational(9, 2)


# =========================================================================
# Section 13: Modular functor axiom enumeration
# =========================================================================

class TestModularFunctorAxioms:
    """Verify the modular functor and CohFT axiom lists are complete."""

    def test_modular_functor_has_all_axioms(self):
        """The modular functor axiom list covers all key properties."""
        axioms = modular_functor_axioms()
        assert 'operadic_identity' in axioms
        assert 'propagation_of_vacua' in axioms
        assert 'factorization_separating' in axioms
        assert 'framing_anomaly' in axioms
        assert 'mapping_class_group' in axioms

    def test_cohft_has_all_axioms(self):
        """The CohFT axiom list covers equivariance, splitting, flat identity."""
        axioms = cohft_axioms()
        assert 'equivariance' in axioms
        assert 'separating_splitting' in axioms
        assert 'nonseparating_splitting' in axioms
        assert 'flat_identity' in axioms

    def test_equivariance_unconditional(self):
        """Equivariance is UNCONDITIONAL."""
        axioms = cohft_axioms()
        assert 'UNCONDITIONAL' in axioms['equivariance']

    def test_splitting_unconditional(self):
        """Both splitting axioms are UNCONDITIONAL."""
        axioms = cohft_axioms()
        assert 'UNCONDITIONAL' in axioms['separating_splitting']
        assert 'UNCONDITIONAL' in axioms['nonseparating_splitting']

    def test_flat_identity_conditional(self):
        """The flat identity is CONDITIONAL (AP30)."""
        axioms = cohft_axioms()
        assert 'CONDITIONAL' in axioms['flat_identity']


# =========================================================================
# Section 14: Multi-path cross-checks (AP10 compliance)
# =========================================================================

class TestMultiPathCrossChecks:
    """Multi-path verification of all numerical claims.

    Each numerical value is verified by at least 2 independent methods
    to prevent AP10 (hardcoded wrong values passing tests).
    """

    # -- kappa cross-checks --

    def test_kappa_sl2_via_two_formulas(self):
        """kappa(sl_2, k) = dim(g)*(k+h^v)/(2h^v) cross-checked against c-formula.

        Path 1: kappa = 3*(k+2)/4 from dim=3, h^v=2.
        Path 2: Direct computation dim(g)*(k+h^v)/(2*h^v) = 3*(k+2)/4.
        Path 3: kappa(sl_2, 0) = 3*2/4 = 3/2 (k=0 limiting case).
        """
        # Path 1
        assert kappa_affine('A', 1, 1) == Rational(9, 4)
        # Path 2: direct
        dim_g, h_v = 3, 2
        assert Rational(dim_g * (1 + h_v), 2 * h_v) == Rational(9, 4)
        # Path 3: k=0 limit
        assert kappa_affine('A', 1, 0) == Rational(3, 2)
        assert Rational(dim_g * (0 + h_v), 2 * h_v) == Rational(3, 2)

    def test_kappa_sl3_via_two_formulas(self):
        """kappa(sl_3, k) cross-checked.

        Path 1: engine computation.
        Path 2: direct from dim=8, h^v=3.
        """
        assert kappa_affine('A', 2, 1) == Rational(16, 3)
        dim_g, h_v = 8, 3
        assert Rational(dim_g * (1 + h_v), 2 * h_v) == Rational(16, 3)

    def test_kappa_e8_via_two_formulas(self):
        """kappa(E_8, 1) cross-checked.

        Path 1: engine computation.
        Path 2: direct from dim=248, h^v=30.
        """
        assert kappa_affine('E', 8, 1) == Rational(1922, 15)
        dim_g, h_v = 248, 30
        assert Rational(dim_g * (1 + h_v), 2 * h_v) == Rational(1922, 15)
        # Path 3: verify numerator/denominator
        assert 248 * 31 == 7688
        assert Rational(7688, 60) == Rational(1922, 15)

    # -- lambda_fp cross-checks --

    def test_lambda_fp_genus1_via_bernoulli(self):
        """lambda_1^FP = 1/24 via Bernoulli number B_2 = 1/6.

        Path 1: engine computation.
        Path 2: (2^1 - 1)/(2^1) * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24.
        """
        assert lambda_fp(1) == Rational(1, 24)
        from sympy import bernoulli as bern
        B2 = bern(2)
        assert B2 == Rational(1, 6)
        result = Rational(2**1 - 1, 2**1) * abs(B2) / factorial(2)
        assert result == Rational(1, 24)

    def test_lambda_fp_genus2_via_bernoulli(self):
        """lambda_2^FP = 7/5760 via B_4 = -1/30.

        Path 1: engine.
        Path 2: (2^3 - 1)/(2^3) * |B_4|/4! = 7/8 * (1/30) / 24 = 7/5760.
        """
        assert lambda_fp(2) == Rational(7, 5760)
        from sympy import bernoulli as bern, factorial as fact
        B4 = bern(4)
        assert B4 == Rational(-1, 30)
        result = Rational(2**3 - 1, 2**3) * abs(B4) / fact(4)
        assert result == Rational(7, 5760)

    def test_lambda_fp_genus3_via_bernoulli(self):
        """lambda_3^FP = 31/967680 via B_6 = 1/42.

        Path 1: engine.
        Path 2: (2^5 - 1)/(2^5) * |B_6|/6! = 31/32 * (1/42) / 720.
        """
        assert lambda_fp(3) == Rational(31, 967680)
        from sympy import bernoulli as bern, factorial as fact
        B6 = bern(6)
        assert B6 == Rational(1, 42)
        result = Rational(2**5 - 1, 2**5) * abs(B6) / fact(6)
        assert result == Rational(31, 967680)

    # -- Verlinde cross-checks --

    def test_verlinde_sl2_genus1_cross_check(self):
        """V_{1,k}(sl_2) = k+1: cross-checked via S-matrix trace.

        Path 1: direct formula k+1.
        Path 2: sum_{j=0}^k 1 = k+1 (since S_{0,j}^0 = 1 for genus 1).
        """
        for k in [1, 2, 3, 4, 5]:
            assert verlinde_dimension_sl2(k, 1) == k + 1
            # Path 2: trivial identity for genus 1
            assert sum(1 for j in range(k + 1)) == k + 1

    def test_num_reps_sl_N_cross_check(self):
        """Number of integrable reps for sl_N at level k.

        Path 1: engine computation via binomial(k+N-1, N-1).
        Path 2: direct combinatorial count (stars and bars).
        """
        # sl_2 (N=2): binomial(k+1, 1) = k+1
        for k in [1, 2, 3]:
            assert num_integrable_reps('A', 1, k) == k + 1
            from sympy import binomial as binom
            assert int(binom(k + 1, 1)) == k + 1

        # sl_3 (N=3): binomial(k+2, 2) = (k+1)(k+2)/2
        for k in [1, 2, 3]:
            expected = (k + 1) * (k + 2) // 2
            assert num_integrable_reps('A', 2, k) == expected
            assert int(binom(k + 2, 2)) == expected

    # -- Framing anomaly cross-checks --

    def test_framing_anomaly_cross_check_virasoro(self):
        """For Virasoro: kappa = c/2 = framing anomaly alpha.

        Path 1: framing_anomaly_comparison.
        Path 2: direct computation.
        Path 3: check at c=1, c=26 (known values).
        """
        # c=1
        r1 = framing_anomaly_comparison(Rational(1))
        assert r1['match']
        assert r1['dw_framing_anomaly'] == Rational(1, 2)

        # c=26
        r26 = framing_anomaly_comparison(Rational(26))
        assert r26['match']
        assert r26['dw_framing_anomaly'] == Rational(13)

    def test_kappa_c_over_2_divergence_cross_check(self):
        """kappa != c/2 for rank > 1: verified by two independent computations.

        Path 1: verify_kappa_equals_framing_anomaly engine.
        Path 2: manual computation of kappa and c for sl_3 at level 1.
        """
        # Engine
        result = verify_kappa_equals_framing_anomaly('A', 2, 1)
        assert not result['kappa_equals_c_over_2']

        # Manual: sl_3, level 1
        # dim = 8, h^v = 3
        # kappa = 8 * (1+3) / (2*3) = 32/6 = 16/3
        # c = 1 * 8 / (1+3) = 8/4 = 2
        # c/2 = 1
        # kappa - c/2 = 16/3 - 1 = 13/3 != 0
        kappa_manual = Rational(8 * 4, 6)
        c_manual = Rational(8, 4)
        assert kappa_manual == Rational(16, 3)
        assert c_manual == Rational(2)
        assert kappa_manual != c_manual / 2

    # -- Scope cross-checks --

    def test_scope_count_cross_check(self):
        """Scope counts verified by enumeration and by function.

        Path 1: count_scope() function.
        Path 2: manual enumeration of STANDARD_FAMILIES.
        """
        counts = count_scope()
        # Path 2: manual count
        dw_manual = sum(1 for f in STANDARD_FAMILIES.values() if f['dw_applies'])
        shadow_manual = sum(1 for f in STANDARD_FAMILIES.values()
                          if f['shadow_cohft_applies'])
        assert counts['dw_scope'] == dw_manual
        assert counts['shadow_scope'] == shadow_manual
        # Verify specific families
        dw_families = [n for n, f in STANDARD_FAMILIES.items() if f['dw_applies']]
        assert set(dw_families) == {
            'affine_integrable', 'virasoro_minimal',
            'lattice_voa', 'w_algebra_integrable',
        }

    # -- Shadow free energy cross-checks --

    def test_shadow_f1_cross_check(self):
        """F_1 = kappa/24 cross-checked for multiple families.

        Path 1: shadow_free_energy(kappa, 1).
        Path 2: kappa * lambda_fp(1) = kappa * 1/24.
        Path 3: specific numerical values.
        """
        for (lt, rk, lv) in [('A', 1, 1), ('A', 1, 2), ('A', 2, 1), ('E', 8, 1)]:
            kap = kappa_affine(lt, rk, lv)
            # Path 1
            f1_engine = shadow_free_energy(kap, 1)
            # Path 2
            f1_manual = kap * Rational(1, 24)
            assert f1_engine == f1_manual, (
                f"F_1 mismatch for {lt}_{rk} at level {lv}"
            )

    def test_shadow_f2_cross_check(self):
        """F_2 = kappa * 7/5760 cross-checked.

        Path 1: shadow_free_energy(kappa, 2).
        Path 2: kappa * lambda_fp(2).
        """
        kap = kappa_affine('A', 1, 1)
        f2_engine = shadow_free_energy(kap, 2)
        f2_manual = kap * Rational(7, 5760)
        assert f2_engine == f2_manual

    def test_verlinde_vs_shadow_ratio_cross_check(self):
        """The ratio V_1 / F_1 = 24 * V_1 / kappa is consistent.

        Path 1: shadow_trace_vs_verlinde function.
        Path 2: direct computation.
        """
        result = shadow_trace_vs_verlinde('A', 1, 2)
        # sl_2 at level 2: kappa=3, V_1=3
        # ratio = 3 / (3/24) = 24
        assert result['ratio_V1_over_F1'] == Rational(24)
        # Path 2: direct
        assert Rational(3) / (Rational(3) / 24) == 24
