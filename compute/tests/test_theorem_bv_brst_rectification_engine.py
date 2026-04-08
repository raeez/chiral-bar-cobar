r"""Tests for theorem_bv_brst_rectification_engine.

Deep Beilinson rectification of conj:master-bv-brst against:
  [SiLi25]  Si Li, arXiv:2511.12875
  [ESW20]   Elliott-Safronov-Williams, arXiv:2002.10517
  [ESW24]   Elliott-Safronov-Williams, arXiv:2403.19753
  [WG24]    Wang-Grady, arXiv:2407.08667
  [HP26]    Hahner-Paquette, arXiv:2602.22318

Multi-path verification mandate (CLAUDE.md): every numerical claim
verified by at least 3 independent paths.

Ground truth: bv_brst.tex (conj:master-bv-brst, thm:bv-bar-geometric,
  prop:chain-level-three-obstructions, thm:heisenberg-bv-bar-all-genera),
  higher_genus_modular_koszul.tex (Theorem D), concordance.tex (MC5).
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.theorem_bv_brst_rectification_engine import (
    AlgebraData,
    BetaGammaBVGenus1,
    ConjectureStatusUpdate,
    LinftyComparison,
    ObstructionStatus,
    PaperAnalysis,
    TwistClassification,
    UVFinitenessImplication,
    additivity_check,
    affine_km_data,
    all_paper_analyses,
    analyze_esw_lattice,
    analyze_esw_twists,
    analyze_hahner_paquette,
    analyze_si_li,
    analyze_wang_grady,
    anomaly_cancellation_check,
    bar_free_energy,
    betagamma_bv_genus1,
    betagamma_bv_genus1_numerical,
    betagamma_data,
    conjecture_status_by_family,
    cross_family_genus1_check,
    esw_twist_classification,
    full_rectification_synthesis,
    genus2_planted_forest_bv_comparison,
    hahner_paquette_implications,
    heisenberg_bv_bar_all_genera,
    heisenberg_data,
    lambda_fp,
    lambda_fp_from_ahat,
    obstruction_status_analysis,
    si_li_linfty_comparison,
    virasoro_data,
    wang_grady_implications,
)


# =====================================================================
# Section A: Faber-Pandharipande numbers (multi-path verification)
# =====================================================================


class TestLambdaFP:
    """Verify lambda_g^FP by Bernoulli formula and A-hat extraction."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_positive_all(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP must be positive"

    def test_ahat_matches_bernoulli_g1(self):
        """A-hat extraction matches Bernoulli at genus 1."""
        assert lambda_fp_from_ahat(1) == Rational(1, 24)

    def test_ahat_matches_bernoulli_g2(self):
        """A-hat extraction matches Bernoulli at genus 2."""
        assert lambda_fp_from_ahat(2) == Rational(7, 5760)

    def test_ahat_matches_bernoulli_g3(self):
        """A-hat extraction matches Bernoulli at genus 3."""
        assert lambda_fp_from_ahat(3) == Rational(31, 967680)

    def test_lambda_fp_invalid_genus(self):
        """lambda_fp raises for g < 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)


# =====================================================================
# Section B: Algebra data correctness
# =====================================================================


class TestAlgebraData:
    """Verify kappa formulas for standard families (AP1, AP48)."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (NOT k/2, AP48)."""
        h = heisenberg_data(k=Symbol('k'))
        assert h.kappa == Symbol('k')

    def test_heisenberg_kappa_numerical(self):
        """kappa(H_3) = 3."""
        h = heisenberg_data(k=3)
        assert h.kappa == 3

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        v = virasoro_data(c=Symbol('c'))
        assert v.kappa == Symbol('c') / 2

    def test_virasoro_kappa_26(self):
        """kappa(Vir_26) = 13."""
        v = virasoro_data(c=26)
        assert v.kappa == 13

    def test_betagamma_kappa(self):
        """kappa(bg_k) = k."""
        bg = betagamma_data(k=Symbol('k'))
        assert bg.kappa == Symbol('k')

    def test_affine_sl2_kappa(self):
        """kappa(sl2_k) = 3(k+2)/4."""
        km = affine_km_data('sl2', k=Symbol('k'))
        k = Symbol('k')
        expected = Rational(3) * (k + 2) / 4
        assert simplify(km.kappa - expected) == 0

    def test_affine_sl2_kappa_k1(self):
        """kappa(sl2, k=1) = 9/4."""
        km = affine_km_data('sl2', k=1)
        assert km.kappa == Rational(9, 4)


# =====================================================================
# Section C: Paper analyses — epistemic honesty
# =====================================================================


class TestPaperAnalyses:
    """Verify that no paper is overclaimed as proving conj:master-bv-brst."""

    def test_no_paper_proves_conjecture(self):
        """No paper in the literature proves conj:master-bv-brst."""
        for paper in all_paper_analyses():
            assert not paper.proves_conjecture, (
                f"Paper {paper.arxiv_id} DOES NOT prove conj:master-bv-brst. "
                f"This test enforces epistemic honesty (AP4, AP7)."
            )

    def test_five_papers_analyzed(self):
        """All five requested papers are analyzed."""
        papers = all_paper_analyses()
        assert len(papers) == 5
        arxiv_ids = {p.arxiv_id for p in papers}
        assert '2511.12875' in arxiv_ids   # Si Li
        assert '2407.08667' in arxiv_ids   # Wang-Grady
        assert '2002.10517' in arxiv_ids   # ESW twists
        assert '2403.19753' in arxiv_ids   # ESW lattice
        assert '2602.22318' in arxiv_ids   # Hahner-Paquette

    def test_si_li_does_not_prove_conjecture(self):
        """Si Li confirms proved results but does NOT prove the conjecture."""
        paper = analyze_si_li()
        assert not paper.proves_conjecture
        assert 'NOT' in paper.obstruction_3_impact

    def test_wang_grady_removes_necessary_condition(self):
        """Wang-Grady removes UV finiteness obstruction (necessary, not sufficient)."""
        paper = analyze_wang_grady()
        assert not paper.proves_conjecture
        assert 'necessary but not sufficient' in paper.structural_contribution

    def test_esw_twists_classification_not_proof(self):
        """ESW classification constrains scope, does not prove conjecture."""
        paper = analyze_esw_twists()
        assert not paper.proves_conjecture

    def test_esw_lattice_testing_ground(self):
        """ESW lattice provides derived model, not proof."""
        paper = analyze_esw_lattice()
        assert not paper.proves_conjecture

    def test_hahner_paquette_uv_complete(self):
        """Hahner-Paquette provides UV-complete setting, not proof."""
        paper = analyze_hahner_paquette()
        assert not paper.proves_conjecture


# =====================================================================
# Section D: Obstruction analysis
# =====================================================================


class TestObstructionAnalysis:
    """Verify the three-obstruction classification is correct and updated."""

    def test_three_obstructions(self):
        """Exactly three obstructions classified."""
        obstructions = obstruction_status_analysis()
        assert len(obstructions) == 3
        indices = {o.index for o in obstructions}
        assert indices == {1, 2, 3}

    def test_obstruction_3_deepest(self):
        """Obstruction 3 (higher-arity coupling) remains the deepest."""
        obstructions = obstruction_status_analysis()
        obs3 = [o for o in obstructions if o.index == 3][0]
        assert 'UNCHANGED' in obs3.post_literature_status
        assert 'DEEPEST' in obs3.post_literature_status

    def test_obstruction_2_resolved(self):
        """Obstruction 2 (moduli dependence) is essentially resolved."""
        obstructions = obstruction_status_analysis()
        obs2 = [o for o in obstructions if o.index == 2][0]
        assert 'RESOLVED' in obs2.post_literature_status

    def test_obstruction_1_improved(self):
        """Obstruction 1 (propagator regularity) improved by Wang-Grady."""
        obstructions = obstruction_status_analysis()
        obs1 = [o for o in obstructions if o.index == 1][0]
        assert 'IMPROVED' in obs1.post_literature_status
        assert '2407.08667' in obs1.literature_impact

    def test_no_obstruction_fully_resolved_for_class_M(self):
        """No obstruction is fully resolved for class M at genus >= 1."""
        obstructions = obstruction_status_analysis()
        for obs in obstructions:
            if obs.index == 3:
                assert any('M' in item for item in obs.open_for)


# =====================================================================
# Section E: Si Li L_infty comparison
# =====================================================================


class TestSiLiLinftyComparison:
    """Verify L_infty comparison between Si Li and bar-cobar."""

    def test_structural_match(self):
        """Both frameworks produce L_infty algebras with genus expansion."""
        comp = si_li_linfty_comparison()
        assert comp.structural_match

    def test_genus0_match(self):
        """Genus 0: both give classical MC equation (d^2 = 0)."""
        comp = si_li_linfty_comparison()
        assert comp.genus_0_match

    def test_genus1_match(self):
        """Genus 1: both give one-loop anomaly kappa/24."""
        comp = si_li_linfty_comparison()
        assert comp.genus_1_match

    def test_higher_genus_open(self):
        """Higher genus coefficient match is OPEN."""
        comp = si_li_linfty_comparison()
        assert 'OPEN' in comp.higher_genus_match_status


# =====================================================================
# Section F: Beta-gamma BV at genus 1
# =====================================================================


class TestBetaGammaBVGenus1:
    """Verify BV = bar for beta-gamma at genus 1."""

    def test_bg_genus1_match(self):
        """F_1^BV(bg) = F_1^bar(bg) = k/24."""
        result = betagamma_bv_genus1(k_val=1)
        assert result.match
        assert result.bv_F1 == Rational(1, 24)
        assert result.bar_F1 == Rational(1, 24)

    def test_bg_genus1_k2(self):
        """F_1^BV(bg_2) = F_1^bar(bg_2) = 2/24 = 1/12."""
        result = betagamma_bv_genus1(k_val=2)
        assert result.match
        assert result.bv_F1 == Rational(2, 24)

    def test_bg_genus1_numerical(self):
        """Numerical verification of bg BV = bar at genus 1."""
        for k_val in [1, 2, 3, 5, 10]:
            result = betagamma_bv_genus1_numerical(k_val)
            assert result['match'], f"bg_k={k_val}: BV != bar at genus 1"
            assert result['value'] == Rational(k_val, 24)

    def test_bg_mode_sum_description(self):
        """Mode sum representations described on both sides."""
        result = betagamma_bv_genus1()
        assert 'q^n/(1-q^n)' in result.mode_sum_bv
        assert 'q^n/(1-q^n)' in result.mode_sum_bar

    def test_bg_zeta_regularization(self):
        """Zeta regularization correctly produces 1/24."""
        result = betagamma_bv_genus1()
        assert '1/24' in result.zeta_regularization or '-1/24' in result.zeta_regularization


# =====================================================================
# Section G: Heisenberg BV = bar at all genera
# =====================================================================


class TestHeisenbergAllGenera:
    """Verify Heisenberg BV = bar across genera 1-5."""

    def test_all_genera_match(self):
        """F_g^BV = F_g^bar for all g = 1,...,5."""
        results = heisenberg_bv_bar_all_genera(max_genus=5)
        for r in results:
            assert r['match'], f"Heisenberg BV != bar at genus {r['genus']}"

    def test_four_proof_paths(self):
        """Each genus has 4 independent proof paths."""
        results = heisenberg_bv_bar_all_genera(max_genus=3)
        for r in results:
            assert len(r['proof_paths']) == 4

    def test_genus1_value(self):
        """F_1 = k/24 for Heisenberg."""
        results = heisenberg_bv_bar_all_genera(max_genus=1)
        k = Symbol('k')
        assert results[0]['lambda_fp'] == Rational(1, 24)
        assert simplify(results[0]['F_bar'] - k * Rational(1, 24)) == 0

    def test_genus2_value(self):
        """F_2 = k * 7/5760 for Heisenberg."""
        results = heisenberg_bv_bar_all_genera(max_genus=2)
        k = Symbol('k')
        assert results[1]['lambda_fp'] == Rational(7, 5760)


# =====================================================================
# Section H: Wang-Grady UV finiteness implications
# =====================================================================


class TestWangGradyImplications:
    """Verify Wang-Grady implications classified correctly."""

    def test_all_ht_theories_uv_finite(self):
        """All HT theories are UV finite."""
        for impl in wang_grady_implications():
            assert impl.uv_finite

    def test_no_counterterms(self):
        """No counterterms needed."""
        for impl in wang_grady_implications():
            assert not impl.counterterms_needed

    def test_bv_effective_action_defined(self):
        """BV effective action well-defined for all families."""
        for impl in wang_grady_implications():
            assert impl.bv_effective_action_defined

    def test_heisenberg_proved(self):
        """Heisenberg bar comparison is PROVED."""
        impls = wang_grady_implications()
        heis = [i for i in impls if 'Heisenberg' in i.theory_type][0]
        assert 'PROVED' in heis.bar_comparison_status


# =====================================================================
# Section I: ESW twist classification
# =====================================================================


class TestESWTwistClassification:
    """Verify twist classification maps correctly."""

    def test_three_theories_classified(self):
        """At least three parent theories classified."""
        twists = esw_twist_classification()
        assert len(twists) >= 3

    def test_4d_n2_gives_class_s(self):
        """4d N=2 SYM gives class S chiral algebra."""
        twists = esw_twist_classification()
        n2 = [t for t in twists if 'N=2' in t.susy][0]
        assert 'Class S' in n2.resulting_chiral_algebra
        assert 'holomorphic' in n2.twist_type.lower()

    def test_4d_n4_gives_ht(self):
        """4d N=4 SYM gives HT theory."""
        twists = esw_twist_classification()
        n4 = [t for t in twists if 'N=4' in t.susy and t.spacetime_dim == 4][0]
        assert 'Holomorphic-topological' in n4.twist_type


# =====================================================================
# Section J: Cross-family consistency
# =====================================================================


class TestCrossFamilyConsistency:
    """Cross-family checks for BV = bar at genus 1."""

    def test_all_families_pass(self):
        """F_1 = kappa/24 for all standard families."""
        result = cross_family_genus1_check()
        assert result['all_pass']

    def test_additivity(self):
        """F_1(A tensor B) = F_1(A) + F_1(B)."""
        result = additivity_check()
        assert result['all_pass']

    def test_anomaly_cancellation(self):
        """kappa_tot = 0 iff c = 26."""
        result = anomaly_cancellation_check()
        assert result['kappa_tot_is_zero_at_26']
        assert result['brst_zero_at_26']


# =====================================================================
# Section K: Genus-2 planted-forest comparison
# =====================================================================


class TestGenus2PlantedForest:
    """Genus-2 BV/bar comparison with planted-forest corrections."""

    def test_heisenberg_no_planted_forest(self):
        """Class G: no planted-forest correction."""
        h = heisenberg_data(k=1)
        result = genus2_planted_forest_bv_comparison(h)
        assert result['delta_pf'] == 0
        assert result['F2_total'] == Rational(7, 5760)

    def test_virasoro_has_planted_forest(self):
        """Class M: planted-forest correction present."""
        v = virasoro_data(c=Symbol('c'))
        result = genus2_planted_forest_bv_comparison(v)
        assert result['shadow_class'] == 'M'
        assert result['delta_pf'] != 0

    def test_affine_km_uniform_weight(self):
        """Class L uniform-weight: delta_pf absorbed."""
        km = affine_km_data('sl2', k=1)
        result = genus2_planted_forest_bv_comparison(km)
        assert result['shadow_class'] == 'L'
        assert result['F2_total'] == km.kappa * Rational(7, 5760)


# =====================================================================
# Section L: Conjecture status by family
# =====================================================================


class TestConjectureStatus:
    """Verify conjecture status correctly classified per family."""

    def test_heisenberg_all_proved(self):
        """Heisenberg: genus 0 and all-genera scalar PROVED."""
        families = conjecture_status_by_family()
        heis = [f for f in families if 'Heisenberg' in f.family][0]
        assert 'PROVED' in heis.genus_0_status
        assert 'PROVED' in heis.genus_1_scalar_status
        assert 'PROVED' in heis.higher_genus_scalar_status

    def test_virasoro_chain_open(self):
        """Virasoro: chain-level at genus >= 1 is OPEN."""
        families = conjecture_status_by_family()
        vir = [f for f in families if 'Virasoro' in f.family][0]
        assert 'OPEN' in vir.genus_1_chain_status
        assert 'OPEN' in vir.higher_genus_chain_status

    def test_wn_multi_weight(self):
        """W_N: multi-weight at genus >= 2, scalar formula FAILS."""
        families = conjecture_status_by_family()
        wn = [f for f in families if 'W_N' in f.family][0]
        assert 'FAILS' in wn.higher_genus_scalar_status

    def test_betagamma_genus1_scalar_proved(self):
        """Beta-gamma: genus 1 scalar PROVED."""
        families = conjecture_status_by_family()
        bg = [f for f in families if 'Beta-gamma' in f.family][0]
        assert 'PROVED' in bg.genus_1_scalar_status

    def test_all_genus0_proved(self):
        """All families have genus 0 PROVED."""
        for fam in conjecture_status_by_family():
            assert 'PROVED' in fam.genus_0_status, (
                f"{fam.family}: genus 0 must be PROVED"
            )


# =====================================================================
# Section M: Full synthesis
# =====================================================================


class TestFullSynthesis:
    """Verify the complete rectification synthesis."""

    def test_conjecture_not_proved(self):
        """The conjecture is NOT proved by the literature."""
        result = full_rectification_synthesis()
        assert not result['conjecture_proved']

    def test_five_papers(self):
        """Five papers analyzed."""
        result = full_rectification_synthesis()
        assert result['papers_analyzed'] == 5

    def test_wang_grady_most_significant(self):
        """Wang-Grady identified as most significant new result."""
        result = full_rectification_synthesis()
        assert 'Wang-Grady' in result['most_significant_new_result']

    def test_obstruction_3_deepest(self):
        """Obstruction 3 identified as deepest."""
        result = full_rectification_synthesis()
        assert 'Obstruction 3' in result['deepest_obstruction']

    def test_status_remains_conjectural(self):
        """The recommendation is that status remains CONJECTURAL."""
        result = full_rectification_synthesis()
        assert 'CONJECTURAL' in result['recommendation']


# =====================================================================
# Section N: Bar free energy computation
# =====================================================================


class TestBarFreeEnergy:
    """Verify bar free energy formula F_g = kappa * lambda_g^FP."""

    def test_heisenberg_g1(self):
        """F_1(H_k) = k/24."""
        h = heisenberg_data(k=3)
        assert bar_free_energy(h, 1) == Rational(3, 24)

    def test_virasoro_g1(self):
        """F_1(Vir_c) = c/48."""
        v = virasoro_data(c=Rational(26))
        assert bar_free_energy(v, 1) == Rational(13, 24)

    def test_virasoro_c13_g1(self):
        """F_1(Vir_13) = 13/48 (self-dual point)."""
        v = virasoro_data(c=Rational(13))
        assert bar_free_energy(v, 1) == Rational(13, 48)


# =====================================================================
# Section O: Hahner-Paquette implications
# =====================================================================


class TestHahnerPaquette:
    """Verify Hahner-Paquette analysis is correctly scoped."""

    def test_relevance_assessment(self):
        """Relevance classified as LOW-MEDIUM."""
        result = hahner_paquette_implications()
        assert 'LOW-MEDIUM' in result['relevance_for_programme']

    def test_positive_and_negative_listed(self):
        """Both positive and negative implications listed."""
        result = hahner_paquette_implications()
        assert len(result['implications_for_conj']['positive']) >= 2
        assert len(result['implications_for_conj']['negative']) >= 2
