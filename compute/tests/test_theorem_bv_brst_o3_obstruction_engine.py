r"""Tests for theorem_bv_brst_o3_obstruction_engine: O3 harmonic-propagator obstruction.

OBSTRUCTION O3 (prop:chain-level-three-obstructions, item (3)):
  The deepest obstruction to conj:master-bv-brst. The BV Laplacian
  contracts through the FULL propagator P = P_bar + P_harm; the bar
  differential uses only P_bar. The discrepancy delta_4^harm from
  P_harm coupling to interaction vertices is the content of O3.

TEST STRUCTURE (multi-path verification, 3+ independent paths):

  Section A: Core data types and algebra classification
  Section B: Harmonic propagator structure
  Section C: Coupling analysis (pole-order threshold)
  Section D: Betagamma three-mechanism proof (class C)
  Section E: Virasoro contrast (class M)
  Section F: Mode-level verification
  Section G: Free energy comparisons (genus 1 and 2)
  Section H: Consistency checks (additivity, complementarity)
  Section I: Genus-2 extension
  Section J: Coderived reformulation
  Section K: Full synthesis and cross-class comparison
"""

import pytest
from sympy import (
    Integer, Rational, Symbol, simplify, pi, Abs, bernoulli, factorial,
    expand,
)

from compute.lib.theorem_bv_brst_o3_obstruction_engine import (
    AlgebraO3Data,
    HarmonicDiscrepancy,
    HarmonicPropagator,
    ModeLevelComparison,
    QuarticVertexDecomposition,
    affine_km_o3,
    betagamma_o3,
    betagamma_quartic_vertex_decomposition,
    bg_genus1_bv_bar_comparison,
    bg_genus2_bv_bar_comparison,
    coderived_reformulation,
    consistency_check_additivity,
    consistency_check_complementarity,
    full_o3_synthesis,
    genus2_o3_analysis,
    harmonic_coupling_to_vertex,
    harmonic_discrepancy_genus1,
    harmonic_propagator_genus1,
    harmonic_propagator_genus_g,
    heisenberg_o3,
    lambda_fp,
    mode_level_comparison_bg_genus1,
    mode_level_comparison_vir_genus1,
    o3_landscape,
    pole_order_threshold,
    virasoro_o3,
    virasoro_quartic_vertex_decomposition,
)


# =====================================================================
# Section A: Core data types and algebra classification
# =====================================================================


class TestAlgebraO3Data:
    """Verify algebra data construction for O3 analysis."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G with shadow depth 2."""
        h = heisenberg_o3(Integer(1))
        assert h.shadow_class == 'G'
        assert h.shadow_depth == 2
        assert h.kappa == 1
        assert h.has_quartic_vertex is False
        assert h.q_contact == 0
        assert h.fundamental_max_pole == 1

    def test_affine_km_class_L(self):
        """Affine KM is class L with shadow depth 3."""
        km = affine_km_o3('sl2', Integer(1))
        assert km.shadow_class == 'L'
        assert km.shadow_depth == 3
        assert km.has_quartic_vertex is False
        assert km.q_contact == 0
        assert km.fundamental_structure_constants is True
        # kappa(sl2, k=1) = 3*(1+2)/(2*2) = 9/4
        assert km.kappa == Rational(9, 4)

    def test_betagamma_class_C(self):
        """Betagamma is class C with shadow depth 4."""
        bg = betagamma_o3(Integer(1))
        assert bg.shadow_class == 'C'
        assert bg.shadow_depth == 4
        assert bg.has_quartic_vertex is True
        assert bg.q_contact == 0  # Q^contact = 0 on fundamental channel
        assert bg.fundamental_max_pole == 1  # simple pole only
        # c = 2(6-6+1) = 2, kappa = 1
        assert bg.central_charge == 2
        assert bg.kappa == 1

    def test_virasoro_class_M(self):
        """Virasoro is class M with shadow depth infinity."""
        v = virasoro_o3(Integer(26))
        assert v.shadow_class == 'M'
        assert v.shadow_depth == 1000
        assert v.has_quartic_vertex is True
        assert v.fundamental_max_pole == 4
        # kappa(Vir_26) = 13
        assert v.kappa == 13
        # Q^contact(26) = 10/(26*(5*26+22)) = 10/(26*152) = 10/3952 = 5/1976
        assert v.q_contact == Rational(10, 3952)

    def test_betagamma_at_weight_half(self):
        """Betagamma at lambda=1/2: c = -1, kappa = -1/2."""
        bg = betagamma_o3(Rational(1, 2))
        # c = 2*(6/4 - 3 + 1) = 2*(-1/2) = -1
        assert bg.central_charge == -1
        assert bg.kappa == Rational(-1, 2)
        assert bg.shadow_class == 'C'

    def test_virasoro_q_contact_formula(self):
        """Q^contact(Vir_c) = 10/(c*(5c+22)) for specific c values."""
        # c = 1: Q = 10/(1*27) = 10/27
        v1 = virasoro_o3(Integer(1))
        assert v1.q_contact == Rational(10, 27)
        # c = 2: Q = 10/(2*32) = 10/64 = 5/32
        v2 = virasoro_o3(Integer(2))
        assert v2.q_contact == Rational(10, 64)


# =====================================================================
# Section B: Harmonic propagator structure
# =====================================================================


class TestHarmonicPropagator:
    """Verify harmonic propagator properties."""

    def test_genus1_dim(self):
        """At genus 1, harmonic space has dimension 1."""
        p = harmonic_propagator_genus1()
        assert p.genus == 1
        assert p.dim_harmonic == 1

    def test_genus1_no_poles(self):
        """P_harm at genus 1 has no poles (smooth on E_tau)."""
        p = harmonic_propagator_genus1()
        assert p.has_poles is False
        assert p.is_meromorphic is False

    def test_genus1_im_tau(self):
        """P_harm at genus 1 depends on Im(tau) (non-holomorphic)."""
        p = harmonic_propagator_genus1()
        assert p.im_tau_dependence is True

    def test_genus_g_dim(self):
        """At genus g, harmonic space has dimension g."""
        for g in range(1, 6):
            p = harmonic_propagator_genus_g(g)
            assert p.dim_harmonic == g
            assert p.has_poles is False

    def test_genus0_error(self):
        """Genus 0 should raise an error (no harmonic propagator)."""
        with pytest.raises(ValueError):
            harmonic_propagator_genus_g(0)


# =====================================================================
# Section C: Coupling analysis (pole-order threshold)
# =====================================================================


class TestHarmonicCoupling:
    """Verify P_harm coupling to vertices by class."""

    def test_heisenberg_arity3_no_coupling(self):
        """Heisenberg: no cubic vertex (depth 2 < 3), coupling vanishes."""
        h = heisenberg_o3(Integer(1))
        result = harmonic_coupling_to_vertex(h, arity=3)
        assert result['coupling_vanishes'] is True
        # Heisenberg has shadow depth 2, so no arity-3 vertex exists
        assert result['vertex_exists'] is False

    def test_heisenberg_arity4_no_coupling(self):
        """Heisenberg: no quartic vertex."""
        h = heisenberg_o3(Integer(1))
        result = harmonic_coupling_to_vertex(h, arity=4)
        assert result['coupling_vanishes'] is True

    def test_affine_km_arity3_jacobi(self):
        """Affine KM: cubic vertex exists, Jacobi kills harmonic coupling."""
        km = affine_km_o3('sl2', Integer(1))
        result = harmonic_coupling_to_vertex(km, arity=3)
        assert result['vertex_exists'] is True
        assert result['coupling_vanishes'] is True
        assert 'Jacobi' in result['reason']

    def test_affine_km_arity4_no_vertex(self):
        """Affine KM: no quartic vertex (depth 3 < 4)."""
        km = affine_km_o3('sl2', Integer(1))
        result = harmonic_coupling_to_vertex(km, arity=4)
        assert result['vertex_exists'] is False
        assert result['coupling_vanishes'] is True

    def test_betagamma_arity4_vanishes(self):
        """Betagamma: quartic vertex exists but coupling vanishes."""
        bg = betagamma_o3(Integer(1))
        result = harmonic_coupling_to_vertex(bg, arity=4)
        assert result['vertex_exists'] is True
        assert result['coupling_vanishes'] is True
        assert 'simple poles' in result['reason']

    def test_virasoro_arity4_nonvanishing(self):
        """Virasoro: quartic vertex couples to P_harm (O3 genuine)."""
        v = virasoro_o3(Integer(26))
        result = harmonic_coupling_to_vertex(v, arity=4)
        assert result['vertex_exists'] is True
        assert result['coupling_vanishes'] is False
        assert 'genuine' in result['reason'].lower() or 'Class M' in result['reason']

    def test_pole_order_threshold_value(self):
        """The pole-order threshold is 2."""
        threshold = pole_order_threshold()
        assert threshold['threshold'] == 2
        assert threshold['simple_pole_coupling'] == 0


# =====================================================================
# Section D: Betagamma three-mechanism proof (class C)
# =====================================================================


class TestBetagammaThreeMechanisms:
    """Verify the three-mechanism proof that O3 vanishes for class C."""

    def test_vertex_factorization(self):
        """Betagamma quartic vertex factorizes into simple-pole channels."""
        decomp = betagamma_quartic_vertex_decomposition()
        assert decomp.fundamental_factorization is True
        assert decomp.each_factor_max_pole == 1
        assert decomp.composite_max_pole == 4  # T(z)T(w) has 4th order

    def test_harmonic_coupling_vanishes(self):
        """The quartic harmonic coupling VANISHES for betagamma."""
        decomp = betagamma_quartic_vertex_decomposition()
        assert 'VANISHES' in decomp.harmonic_coupling_result

    def test_discrepancy_genus1_zero(self):
        """delta_4^harm = 0 for betagamma at genus 1."""
        bg = betagamma_o3(Integer(1))
        disc = harmonic_discrepancy_genus1(bg)
        assert disc.is_zero is True
        assert disc.delta_value == 0
        assert disc.is_coboundary is True

    def test_mechanism_contains_all_three(self):
        """The mechanism description mentions all three arguments."""
        bg = betagamma_o3(Integer(1))
        disc = harmonic_discrepancy_genus1(bg)
        assert 'simple pole' in disc.mechanism.lower() or 'Fundamental OPE' in disc.mechanism
        assert 'Hodge' in disc.mechanism or 'type' in disc.mechanism
        assert 'separation' in disc.mechanism.lower() or 'composite' in disc.mechanism.lower()

    def test_q_contact_fundamental_channel_zero(self):
        """Q^contact on the fundamental (weight-changing) channel is zero."""
        bg = betagamma_o3(Integer(1))
        assert bg.q_contact == 0

    def test_fundamental_ope_simple_pole(self):
        """beta(z)gamma(w) ~ 1/(z-w) is a simple pole (order 1)."""
        bg = betagamma_o3(Integer(1))
        assert bg.fundamental_max_pole == 1

    def test_no_structure_constants(self):
        """Betagamma has no Lie algebra structure constants f^{abc}."""
        bg = betagamma_o3(Integer(1))
        assert bg.fundamental_structure_constants is False


# =====================================================================
# Section E: Virasoro contrast (class M)
# =====================================================================


class TestVirasoroContrast:
    """Verify that O3 is genuinely nonvanishing for class M."""

    def test_virasoro_vertex_does_not_factorize(self):
        """Virasoro quartic vertex does NOT factorize into simple poles."""
        decomp = virasoro_quartic_vertex_decomposition()
        assert decomp.fundamental_factorization is False
        assert decomp.each_factor_max_pole == 4

    def test_virasoro_harmonic_coupling_nonvanishing(self):
        """Virasoro quartic harmonic coupling is NONVANISHING."""
        decomp = virasoro_quartic_vertex_decomposition()
        assert 'NONVANISHING' in decomp.harmonic_coupling_result

    def test_discrepancy_genus1_nonzero(self):
        """delta_4^harm != 0 for Virasoro at genus 1."""
        v = virasoro_o3(Integer(26))
        disc = harmonic_discrepancy_genus1(v)
        assert disc.is_zero is False
        assert disc.is_coboundary is False

    def test_discrepancy_not_coboundary(self):
        """The Virasoro discrepancy contains 1/Im(tau), not holomorphic."""
        v = virasoro_o3(Integer(26))
        disc = harmonic_discrepancy_genus1(v)
        assert disc.is_coboundary is False
        # The mechanism should mention non-holomorphic or Im(tau)
        assert 'non-holomorphic' in disc.mechanism.lower() or 'coderived' in disc.mechanism.lower()

    def test_virasoro_fundamental_pole_order_4(self):
        """Virasoro self-OPE T(z)T(w) has pole order 4."""
        v = virasoro_o3(Integer(26))
        assert v.fundamental_max_pole == 4

    def test_discrepancy_proportional_to_q_contact(self):
        """delta_4^harm is proportional to Q^contact for class M."""
        v = virasoro_o3(Integer(1))
        disc = harmonic_discrepancy_genus1(v)
        # delta_value = Q^contact * kappa * pi / Im(tau)
        # Q^contact(1) = 10/27, kappa(1) = 1/2
        # delta = 10/27 * 1/2 * pi / y = 5*pi / (27*y)
        y = Symbol('y', positive=True)
        expected_proportional = Rational(10, 27) * Rational(1, 2) * pi / y
        assert simplify(disc.delta_value - expected_proportional) == 0


# =====================================================================
# Section F: Mode-level verification
# =====================================================================


class TestModeLevelComparison:
    """Verify mode-level BV/bar comparison at arity 4."""

    def test_bg_modes_match_at_nonzero(self):
        """Betagamma: nonzero modes match between BV and bar."""
        comp = mode_level_comparison_bg_genus1()
        assert comp.match_at_nonzero_modes is True

    def test_bg_zero_mode_discrepancy_zero(self):
        """Betagamma: zero-mode quartic discrepancy is zero."""
        comp = mode_level_comparison_bg_genus1()
        assert comp.zero_mode_discrepancy == 0

    def test_vir_modes_match_at_nonzero(self):
        """Virasoro: nonzero modes match between BV and bar."""
        comp = mode_level_comparison_vir_genus1()
        assert comp.match_at_nonzero_modes is True

    def test_vir_zero_mode_discrepancy_nonzero(self):
        """Virasoro: zero-mode quartic discrepancy is nonzero."""
        comp = mode_level_comparison_vir_genus1()
        # Should be Q^contact / Im(tau), symbolically nonzero
        assert comp.zero_mode_discrepancy != 0


# =====================================================================
# Section G: Free energy comparisons
# =====================================================================


class TestFreeEnergyComparisons:
    """Verify BV = bar free energies for betagamma."""

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_bg_genus1_match(self):
        """BV and bar free energies match at genus 1 for betagamma."""
        result = bg_genus1_bv_bar_comparison(k_val=1)
        assert result['match'] is True
        assert result['F1_bar'] == Rational(1, 24)
        assert result['F1_bv'] == Rational(1, 24)
        assert result['arity_4_discrepancy'] == 0

    def test_bg_genus1_k2(self):
        """BV = bar at genus 1 for betagamma with k=2 pairs."""
        result = bg_genus1_bv_bar_comparison(k_val=2)
        assert result['match'] is True
        assert result['F1_bar'] == Rational(2, 24)

    def test_bg_genus2_delta_pf_zero(self):
        """Planted-forest correction is zero for betagamma (S_3 = 0)."""
        result = bg_genus2_bv_bar_comparison(k_val=1)
        assert result['delta_pf_is_zero'] is True
        assert result['delta_pf'] == 0

    def test_bg_genus2_free_energy(self):
        """F_2^bar = kappa * lambda_2^FP for betagamma."""
        result = bg_genus2_bv_bar_comparison(k_val=1)
        expected = Rational(7, 5760)
        assert result['F2_bar'] == expected

    def test_bg_genus1_three_paths(self):
        """Three independent verification paths for F_1(bg)."""
        result = bg_genus1_bv_bar_comparison(k_val=1)
        paths = result['verification_paths']
        assert paths['quillen_anomaly'] == Rational(1, 24)
        assert paths['bar_sewing'] == Rational(1, 24)
        assert paths['eisenstein'] == Rational(1, 24)


# =====================================================================
# Section H: Consistency checks
# =====================================================================


class TestConsistencyChecks:
    """Verify additivity and complementarity of delta_4^harm."""

    def test_additivity_h_tensor_bg(self):
        """delta(H tensor bg) = delta(H) + delta(bg) = 0 + 0 = 0."""
        result = consistency_check_additivity()
        assert result['H_tensor_bg']['additive'] is True
        assert result['H_tensor_bg']['delta_sum'] == 0

    def test_additivity_all_additive(self):
        """Additivity holds for all tested tensor products."""
        result = consistency_check_additivity()
        for key in result:
            assert result[key]['additive'] is True

    def test_complementarity_at_c13(self):
        """At c=13 (self-dual): delta(13) + delta(13) = 2*delta(13)."""
        result = consistency_check_complementarity()
        # At c=13: the sum should be a definite rational number
        val_13 = result['at_c_13']
        # 870 / (87 * 87) = 870/7569 = 10/87
        assert simplify(val_13 - Rational(10, 87)) == 0

    def test_complementarity_symmetric(self):
        """The complementarity sum is symmetric around c=13."""
        result = consistency_check_complementarity()
        assert result['symmetric_around_13'] is True


# =====================================================================
# Section I: Genus-2 extension
# =====================================================================


class TestGenus2Extension:
    """Verify O3 analysis extends to genus 2."""

    def test_heisenberg_genus2_no_obstruction(self):
        """Heisenberg: no O3 at genus 2."""
        h = heisenberg_o3(Integer(1))
        g2 = genus2_o3_analysis(h)
        assert g2.new_obstruction is False
        assert g2.dim_harmonic == 2

    def test_betagamma_genus2_no_obstruction(self):
        """Betagamma: O3 vanishes at genus 2 (same three mechanisms)."""
        bg = betagamma_o3(Integer(1))
        g2 = genus2_o3_analysis(bg)
        assert g2.new_obstruction is False
        assert 'ZERO' in g2.discrepancy_status

    def test_virasoro_genus2_has_obstruction(self):
        """Virasoro: O3 is nonzero at genus 2 with richer structure."""
        v = virasoro_o3(Integer(26))
        g2 = genus2_o3_analysis(v)
        assert g2.new_obstruction is True
        assert g2.harmonic_coupling_channels == 3
        assert 'period matrix' in g2.discrepancy_status.lower()


# =====================================================================
# Section J: Coderived reformulation
# =====================================================================


class TestCoderivedReformulation:
    """Verify the coderived reformulation absorbs O3 for class M."""

    def test_ordinary_chain_level_class_M_fails(self):
        """Ordinary chain-level BV = bar FAILS for class M."""
        result = coderived_reformulation()
        assert 'bar' in result['ordinary_chain_level']['class_M'].lower()
        # The status should indicate failure at ordinary level
        assert '!=' in result['ordinary_chain_level']['class_M']

    def test_coderived_class_M_consistent(self):
        """In D^co, class M is CONSISTENT."""
        result = coderived_reformulation()
        assert 'CONSISTENT' in result['coderived_level']['class_M']

    def test_coderived_classes_GLC_proved(self):
        """In D^co, classes G, L, C are PROVED."""
        result = coderived_reformulation()
        assert 'proved' in result['coderived_level']['class_G'].lower()
        assert 'proved' in result['coderived_level']['class_L'].lower()
        assert 'proved' in result['coderived_level']['class_C'].lower()

    def test_discrepancy_proportional_to_curvature(self):
        """The O3 discrepancy is proportional to the curvature m_0."""
        result = coderived_reformulation()
        assert 'curvature' in result['key_observation'].lower()
        assert 'm_0' in result['proportionality']


# =====================================================================
# Section K: Full synthesis and cross-class comparison
# =====================================================================


class TestFullSynthesis:
    """Verify the complete O3 landscape and synthesis."""

    def test_landscape_has_all_classes(self):
        """The landscape covers classes G, L, C, M."""
        results = o3_landscape()
        classes = {r['class'] for r in results}
        assert classes == {'G', 'L', 'C', 'M'}

    def test_landscape_genus1_zeros(self):
        """Classes G, L, C all have delta_4^harm = 0 at genus 1."""
        results = o3_landscape()
        for r in results:
            if r['class'] in ('G', 'L', 'C'):
                assert r['genus1_zero'] is True, f"{r['name']} should have zero discrepancy"

    def test_landscape_genus1_class_M_nonzero(self):
        """Class M has delta_4^harm != 0 at genus 1."""
        results = o3_landscape()
        for r in results:
            if r['class'] == 'M':
                assert r['genus1_zero'] is False, f"{r['name']} should have nonzero discrepancy"

    def test_full_synthesis_runs(self):
        """The full synthesis completes without error."""
        result = full_o3_synthesis()
        assert 'landscape' in result
        assert 'summary' in result
        assert 'key_insight' in result

    def test_synthesis_summary_correct(self):
        """The synthesis summary is consistent with individual results."""
        result = full_o3_synthesis()
        summary = result['summary']
        assert 'absent' in summary['class_G'].lower()
        assert 'killed' in summary['class_L'].lower() or 'jacobi' in summary['class_L'].lower()
        assert 'vanish' in summary['class_C'].lower()
        assert 'genuine' in summary['class_M'].lower()

    def test_pole_order_threshold_classification(self):
        """Pole-order classification matches shadow class."""
        threshold = pole_order_threshold()
        cls = threshold['classification']
        assert cls['G']['max_fundamental_pole'] == 1
        assert cls['L']['max_fundamental_pole'] == 1
        assert cls['C']['max_fundamental_pole'] == 1
        assert cls['M']['max_fundamental_pole'] == 4
        # All classes with fundamental pole 1 have o3 resolved
        for c in ('G', 'L', 'C'):
            assert 'absent' in cls[c]['o3_status'] or 'killed' in cls[c]['o3_status'] or 'zero' in cls[c]['o3_status']

    def test_betagamma_genus1_and_genus2_consistent(self):
        """Betagamma O3 = 0 at both genus 1 and genus 2."""
        result = full_o3_synthesis()
        assert result['betagamma_genus1']['arity_4_discrepancy'] == 0
        assert result['betagamma_genus2']['arity_4_harmonic_discrepancy_genus2'] == 0

    def test_key_insight_mentions_pole_threshold(self):
        """Key insight identifies the pole-order threshold."""
        result = full_o3_synthesis()
        assert 'pole' in result['key_insight'].lower()
        assert 'threshold' in result['key_insight'].lower() or 'order' in result['key_insight'].lower()
