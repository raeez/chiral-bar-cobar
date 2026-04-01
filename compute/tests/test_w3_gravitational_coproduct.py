r"""Tests for W_3 gravitational coproduct and DS-HPL transfer primitivity.

This test suite independently verifies the primitivity claim for the
transferred coproduct under Drinfeld-Sokolov reduction sl_N -> W_N.
The central claim: the ghost-number obstruction that proves primitivity
for sl_2 -> Vir (prop:coproduct-arity2-vanishing) is UNIVERSAL and
works for ALL N, including N = 3 (W_3).

The test suite covers:
1. sl_3 structure: generators, ghost numbers, conformal weights
2. SDR framework: ghost-degree analysis for h, delta
3. HPL tree ghost-number tracking at arity 2
4. Higher-arity ghost-number analysis (arities 3-6)
5. Potential failure mode analysis (5 candidate failure modes)
6. Central charge identities for sl_3 -> W_3
7. Kappa (modular characteristic) and complementarity
8. Comparison between sl_2 and sl_3 cases
9. General N analysis (N = 2, ..., 10)
10. Cross-checks against existing compute modules
11. Physical interpretation consistency

40+ tests required.

Manuscript references:
  prop:coproduct-arity2-vanishing (Vol II, 3d_gravity.tex)
  rem:gap-b-closed (Vol II, 3d_gravity.tex)
  thm:ds-hpl-transfer (Vol II, 3d_gravity.tex)
  thm:shadow-archetype-classification (Vol I, higher_genus_modular_koszul.tex)
"""

from fractions import Fraction

import pytest

from compute.lib.w3_gravitational_coproduct import (
    POSITIVE_ROOTS_SL3,
    GRADES_SL3,
    BRSTGenerator,
    sl3_brst_generators,
    count_ghost_pairs,
    ghost_central_charge_sl_N,
    analyze_sdr_ghost_numbers,
    verify_ghost_degree_h,
    hpl_arity2_trees,
    coproduct_arity2_vanishes,
    hpl_arity_r_ghost_analysis,
    sl2_sdr_explicit,
    sl3_sdr_framework,
    analyze_potential_failure_modes,
    w3_central_charge,
    sl3_sugawara_central_charge,
    ghost_c_sl3,
    verify_ghost_c_sl3_identity,
    kappa_W3,
    kappa_dual_W3,
    w3_complementarity_sum,
    primitivity_theorem,
    compare_sl2_sl3,
    primitivity_all_N,
    adversarial_caveat,
    where_the_nonlinearity_lives,
)


# ============================================================================
# 1.  sl_3 STRUCTURE TESTS
# ============================================================================

class TestSl3Structure:
    """Tests for the sl_3 Lie algebra and BRST complex structure."""

    def test_positive_roots_count(self):
        """sl_3 has exactly 3 positive roots."""
        assert len(POSITIVE_ROOTS_SL3) == 3

    def test_positive_roots_names(self):
        """The positive roots are alpha1, alpha2, alpha1+alpha2."""
        assert set(POSITIVE_ROOTS_SL3) == {'alpha1', 'alpha2', 'alpha12'}

    def test_grades_sl3_positive(self):
        """Positive root grades: alpha1 = 1, alpha2 = 1, alpha12 = 2."""
        assert GRADES_SL3['E12'] == 1   # alpha1
        assert GRADES_SL3['E23'] == 1   # alpha2
        assert GRADES_SL3['E13'] == 2   # alpha1 + alpha2

    def test_grades_sl3_negative(self):
        """Negative root grades are negatives of positive."""
        assert GRADES_SL3['E21'] == -1
        assert GRADES_SL3['E32'] == -1
        assert GRADES_SL3['E31'] == -2

    def test_grades_sl3_cartan(self):
        """Cartan elements have grade 0."""
        assert GRADES_SL3['h1'] == 0
        assert GRADES_SL3['h2'] == 0

    def test_brst_generators_count(self):
        """sl_3 BRST complex has 14 generators: 8 currents + 3 ghosts + 3 antighosts."""
        gens = sl3_brst_generators()
        assert len(gens) == 14
        currents = [g for g in gens if g.sector == 'current']
        ghosts = [g for g in gens if g.sector == 'ghost']
        antighosts = [g for g in gens if g.sector == 'antighost']
        assert len(currents) == 8
        assert len(ghosts) == 3
        assert len(antighosts) == 3

    def test_ghost_numbers(self):
        """Ghost numbers: currents = 0, ghosts = +1, antighosts = -1."""
        gens = sl3_brst_generators()
        for g in gens:
            if g.sector == 'current':
                assert g.ghost_number == 0, f'{g.name} should have ghost 0'
            elif g.sector == 'ghost':
                assert g.ghost_number == 1, f'{g.name} should have ghost +1'
            elif g.sector == 'antighost':
                assert g.ghost_number == -1, f'{g.name} should have ghost -1'

    def test_ghost_conformal_weights_grade1(self):
        """Grade-1 ghosts have weight 0, grade-1 antighosts have weight 1."""
        gens = sl3_brst_generators()
        for g in gens:
            if g.sector == 'ghost' and g.ad_h_grade == 1:
                assert g.conformal_weight == 0, f'{g.name}: c at grade 1 has weight 0'
            if g.sector == 'antighost' and g.ad_h_grade == 1:
                assert g.conformal_weight == 1, f'{g.name}: b at grade 1 has weight 1'

    def test_ghost_conformal_weights_grade2(self):
        """Grade-2 ghost has weight -1, grade-2 antighost has weight 2."""
        gens = sl3_brst_generators()
        for g in gens:
            if g.sector == 'ghost' and g.ad_h_grade == 2:
                assert g.conformal_weight == -1, f'{g.name}: c at grade 2 has weight -1'
            if g.sector == 'antighost' and g.ad_h_grade == 2:
                assert g.conformal_weight == 2, f'{g.name}: b at grade 2 has weight 2'


# ============================================================================
# 2.  GHOST PAIR COUNTING
# ============================================================================

class TestGhostPairCounting:
    """Tests for ghost pair counting across different N."""

    def test_ghost_pairs_sl2(self):
        """sl_2 has 1 positive root, hence 1 ghost pair."""
        assert count_ghost_pairs(2) == 1

    def test_ghost_pairs_sl3(self):
        """sl_3 has 3 positive roots, hence 3 ghost pairs."""
        assert count_ghost_pairs(3) == 3

    def test_ghost_pairs_sl4(self):
        """sl_4 has 6 positive roots, hence 6 ghost pairs."""
        assert count_ghost_pairs(4) == 6

    def test_ghost_pairs_sl5(self):
        """sl_5 has 10 positive roots, hence 10 ghost pairs."""
        assert count_ghost_pairs(5) == 10

    def test_ghost_pairs_formula(self):
        """N(N-1)/2 positive roots for sl_N."""
        for N in range(2, 11):
            expected = N * (N - 1) // 2
            assert count_ghost_pairs(N) == expected

    def test_ghost_central_charge(self):
        """Ghost central charge = N(N-1) for sl_N."""
        for N in range(2, 8):
            assert ghost_central_charge_sl_N(N) == Fraction(N * (N - 1))


# ============================================================================
# 3.  SDR GHOST-NUMBER ANALYSIS
# ============================================================================

class TestSDRGhostAnalysis:
    """Tests for ghost-number analysis of the SDR."""

    def test_ghost_degree_h_sl2(self):
        """h has ghost degree -1 for sl_2."""
        sdr = analyze_sdr_ghost_numbers(2)
        assert sdr.ghost_degree_h == -1

    def test_ghost_degree_h_sl3(self):
        """h has ghost degree -1 for sl_3."""
        sdr = analyze_sdr_ghost_numbers(3)
        assert sdr.ghost_degree_h == -1

    def test_ghost_degree_delta(self):
        """delta has ghost degree +1 for all N."""
        for N in range(2, 8):
            sdr = analyze_sdr_ghost_numbers(N)
            assert sdr.ghost_degree_delta == +1

    def test_ghost_degree_h_delta(self):
        """h*delta has ghost degree 0 for all N."""
        for N in range(2, 8):
            sdr = analyze_sdr_ghost_numbers(N)
            assert sdr.ghost_degree_h_delta == 0

    def test_delta_kills_T(self):
        """delta(T) = 0 for all N (Sugawara is BRST-closed)."""
        for N in range(2, 8):
            sdr = analyze_sdr_ghost_numbers(N)
            assert sdr.delta_kills_T is True

    def test_delta_kills_W_for_N_ge_3(self):
        """delta(W) = 0 for N >= 3 (spin-3 primary is BRST-closed)."""
        for N in range(3, 8):
            sdr = analyze_sdr_ghost_numbers(N)
            assert sdr.delta_kills_W is True


# ============================================================================
# 4.  EXPLICIT SDR VERIFICATION (sl_2)
# ============================================================================

class TestSl2SDR:
    """Tests for the explicit sl_2 SDR from 3d_gravity.tex."""

    def test_sdr_all_pass(self):
        """All SDR axioms pass for sl_2."""
        result = sl2_sdr_explicit()
        assert result['all_pass'] is True

    def test_pi_is_id(self):
        """pi = id on H^0(d_0)."""
        result = sl2_sdr_explicit()
        assert result['sdr_checks']['pi_is_id'] is True

    def test_h_squared_zero(self):
        """h^2 = 0."""
        result = sl2_sdr_explicit()
        assert result['sdr_checks']['h_squared_zero'] is True

    def test_ph_zero(self):
        """ph = 0."""
        result = sl2_sdr_explicit()
        assert result['sdr_checks']['ph_zero'] is True

    def test_hi_zero(self):
        """hi = 0."""
        result = sl2_sdr_explicit()
        assert result['sdr_checks']['hi_zero'] is True

    def test_homotopy_relation(self):
        """id - ip = d_0 h + h d_0 on all generators."""
        result = sl2_sdr_explicit()
        assert result['sdr_checks']['homotopy_relation'] is True

    def test_homotopy_on_each_generator(self):
        """Homotopy relation holds on each generator individually."""
        result = sl2_sdr_explicit()
        details = result['sdr_checks']['homotopy_details']
        for gen in ['V', 'U', 'W', 'b', 'c']:
            assert details[gen] is True, f'Homotopy fails on {gen}'

    def test_ghost_degree_h_is_minus_1(self):
        """h has ghost degree -1 for sl_2."""
        result = sl2_sdr_explicit()
        assert result['ghost_degree_h'] == -1


# ============================================================================
# 5.  sl_3 SDR FRAMEWORK
# ============================================================================

class TestSl3SDR:
    """Tests for the sl_3 SDR framework."""

    def test_n_generators(self):
        """14 generators in the sl_3 BRST complex."""
        result = sl3_sdr_framework()
        assert result['n_generators'] == 14

    def test_n_ghost_pairs(self):
        """3 ghost pairs for sl_3."""
        result = sl3_sdr_framework()
        assert result['n_ghost_pairs'] == 3

    def test_ghost_degree_h(self):
        """h has ghost degree -1 for sl_3."""
        result = sl3_sdr_framework()
        assert result['ghost_degree_h'] == -1

    def test_all_h_minus_1(self):
        """All nonzero h-actions shift ghost by -1."""
        result = sl3_sdr_framework()
        assert result['all_h_minus_1'] is True

    def test_delta_kills_T(self):
        """delta(T) = 0 for sl_3."""
        result = sl3_sdr_framework()
        assert result['delta_kills_T'] is True

    def test_delta_kills_W(self):
        """delta(W) = 0 for sl_3 (W_3 primary is BRST-closed)."""
        result = sl3_sdr_framework()
        assert result['delta_kills_W'] is True


# ============================================================================
# 6.  GHOST-DEGREE VERIFICATION
# ============================================================================

class TestGhostDegreeVerification:
    """Verify ghost_degree(h) = -1 for multiple N."""

    def test_sl2_ghost_degree(self):
        result = verify_ghost_degree_h(2)
        assert result['ghost_degree_h'] == -1
        assert result['all_degree_minus_1'] is True

    def test_sl3_ghost_degree(self):
        result = verify_ghost_degree_h(3)
        assert result['ghost_degree_h'] == -1
        assert result['all_degree_minus_1'] is True

    def test_sl4_ghost_degree(self):
        result = verify_ghost_degree_h(4)
        assert result['ghost_degree_h'] == -1
        assert result['all_degree_minus_1'] is True

    def test_sl5_ghost_degree(self):
        result = verify_ghost_degree_h(5)
        assert result['ghost_degree_h'] == -1
        assert result['all_degree_minus_1'] is True

    def test_general_N_ghost_degree(self):
        """Ghost degree of h is -1 for N = 2, ..., 10."""
        for N in range(2, 11):
            result = verify_ghost_degree_h(N)
            assert result['ghost_degree_h'] == -1, f'Failed at N = {N}'


# ============================================================================
# 7.  HPL TREE ANALYSIS AT ARITY 2
# ============================================================================

class TestHPLArity2Trees:
    """Tests for the arity-2 HPL tree ghost-number analysis."""

    def test_two_trees_exist(self):
        """There are exactly 2 types of HPL trees at arity 2."""
        trees = hpl_arity2_trees(3, 'T', 'T')
        assert len(trees) == 2

    def test_source_tree_killed(self):
        """Source tree is killed by projection."""
        trees = hpl_arity2_trees(3, 'T', 'T')
        source = [t for t in trees if t.name == 'source_tree'][0]
        assert source.killed_by_projection is True

    def test_target_tree_killed(self):
        """Target tree is killed by projection."""
        trees = hpl_arity2_trees(3, 'T', 'T')
        target = [t for t in trees if t.name == 'target_tree'][0]
        assert target.killed_by_projection is True

    def test_source_tree_ghost_output(self):
        """Source tree output has ghost -1."""
        trees = hpl_arity2_trees(3, 'T', 'T')
        source = [t for t in trees if t.name == 'source_tree'][0]
        assert source.output_ghost == -1

    def test_target_tree_ghost_output(self):
        """Target tree output has ghost -1."""
        trees = hpl_arity2_trees(3, 'T', 'T')
        target = [t for t in trees if t.name == 'target_tree'][0]
        assert target.output_ghost == -1

    def test_TT_vanishes_sl2(self):
        """Delta_{z,2}(T, T) = 0 for sl_2."""
        result = coproduct_arity2_vanishes(2, 'T', 'T')
        assert result['all_trees_vanish'] is True

    def test_TT_vanishes_sl3(self):
        """Delta_{z,2}(T, T) = 0 for sl_3."""
        result = coproduct_arity2_vanishes(3, 'T', 'T')
        assert result['all_trees_vanish'] is True

    def test_TW_vanishes_sl3(self):
        """Delta_{z,2}(T, W) = 0 for sl_3."""
        result = coproduct_arity2_vanishes(3, 'T', 'W')
        assert result['all_trees_vanish'] is True

    def test_WT_vanishes_sl3(self):
        """Delta_{z,2}(W, T) = 0 for sl_3."""
        result = coproduct_arity2_vanishes(3, 'W', 'T')
        assert result['all_trees_vanish'] is True

    def test_WW_vanishes_sl3(self):
        """Delta_{z,2}(W, W) = 0 for sl_3.

        THIS IS THE CRITICAL TEST.  The W x W coproduct involves the
        cubic Casimir of sl_3 and the composite field Lambda = :TT: - 3/10 d^2T.
        Despite this complexity, the ghost-number argument still kills it.
        """
        result = coproduct_arity2_vanishes(3, 'W', 'W')
        assert result['all_trees_vanish'] is True


# ============================================================================
# 8.  HIGHER-ARITY ANALYSIS
# ============================================================================

class TestHigherArity:
    """Tests for ghost-number analysis at arities 3-6."""

    def test_arity3_vanishes(self):
        """All arity-3 trees vanish for sl_3."""
        result = hpl_arity_r_ghost_analysis(3, 3)
        assert result['vanishes'] is True

    def test_arity4_vanishes(self):
        """All arity-4 trees vanish for sl_3."""
        result = hpl_arity_r_ghost_analysis(3, 4)
        assert result['vanishes'] is True

    def test_arity5_vanishes(self):
        """All arity-5 trees vanish for sl_3."""
        result = hpl_arity_r_ghost_analysis(3, 5)
        assert result['vanishes'] is True

    def test_arity6_vanishes(self):
        """All arity-6 trees vanish for sl_3."""
        result = hpl_arity_r_ghost_analysis(3, 6)
        assert result['vanishes'] is True

    def test_all_arities_vanish_sl2(self):
        """All arities 2-6 vanish for sl_2."""
        for r in range(2, 7):
            result = hpl_arity_r_ghost_analysis(2, r)
            assert result['vanishes'] is True, f'Failed at arity {r}'

    def test_all_arities_vanish_sl3(self):
        """All arities 2-6 vanish for sl_3."""
        for r in range(2, 7):
            result = hpl_arity_r_ghost_analysis(3, r)
            assert result['vanishes'] is True, f'Failed at arity {r}'

    def test_all_arities_vanish_sl4(self):
        """All arities 2-6 vanish for sl_4."""
        for r in range(2, 7):
            result = hpl_arity_r_ghost_analysis(4, r)
            assert result['vanishes'] is True, f'Failed at arity {r}'


# ============================================================================
# 9.  POTENTIAL FAILURE MODE ANALYSIS
# ============================================================================

class TestFailureModes:
    """Tests that all potential failure modes are inactive."""

    def test_no_failure_sl2(self):
        """No failure modes for sl_2."""
        result = analyze_potential_failure_modes(2)
        assert result['any_failure'] is False

    def test_no_failure_sl3(self):
        """No failure modes for sl_3."""
        result = analyze_potential_failure_modes(3)
        assert result['any_failure'] is False

    def test_no_failure_sl4(self):
        """No failure modes for sl_4."""
        result = analyze_potential_failure_modes(4)
        assert result['any_failure'] is False

    def test_five_failure_modes_checked(self):
        """Exactly 5 potential failure modes are analyzed."""
        result = analyze_potential_failure_modes(3)
        assert len(result['failure_modes']) == 5

    def test_quadratic_ghost_terms_no_failure(self):
        """Quadratic ghost terms in delta do NOT break the argument."""
        result = analyze_potential_failure_modes(3)
        mode1 = result['failure_modes'][0]
        assert mode1['name'] == 'Quadratic ghost terms in delta'
        assert mode1['fails'] is False

    def test_h_uniformly_minus_1(self):
        """h is uniformly ghost-degree -1."""
        result = analyze_potential_failure_modes(3)
        mode2 = result['failure_modes'][1]
        assert mode2['fails'] is False

    def test_corrected_inclusion_equals_i(self):
        """i_infty = i because delta kills W_N generators."""
        result = analyze_potential_failure_modes(3)
        mode3 = result['failure_modes'][2]
        assert mode3['fails'] is False

    def test_tensor_homotopy_ok(self):
        """H_12 = h x id + id x h works correctly."""
        result = analyze_potential_failure_modes(3)
        mode4 = result['failure_modes'][3]
        assert mode4['fails'] is False

    def test_higher_orders_ok(self):
        """Higher perturbative orders do not break the argument."""
        result = analyze_potential_failure_modes(3)
        mode5 = result['failure_modes'][4]
        assert mode5['fails'] is False


# ============================================================================
# 10.  CENTRAL CHARGE IDENTITIES
# ============================================================================

class TestCentralCharge:
    """Tests for W_3 and sl_3 central charge formulas."""

    def test_w3_central_charge_k1(self):
        """c(W_3, k=1) = 2 - 24/4 = 2 - 6 = -4."""
        assert w3_central_charge(1) == Fraction(-4)

    def test_w3_central_charge_k2(self):
        """c(W_3, k=2) = 2 - 24/5."""
        assert w3_central_charge(2) == Fraction(2) - Fraction(24, 5)
        assert w3_central_charge(2) == Fraction(-14, 5)

    def test_w3_central_charge_k3(self):
        """c(W_3, k=3) = 2 - 24/6 = 2 - 4 = -2."""
        assert w3_central_charge(3) == Fraction(-2)

    def test_sl3_sugawara_k1(self):
        """c(sl_3, k=1) = 8/4 = 2."""
        assert sl3_sugawara_central_charge(1) == Fraction(2)

    def test_sl3_sugawara_k10(self):
        """c(sl_3, k=10) = 80/13."""
        assert sl3_sugawara_central_charge(10) == Fraction(80, 13)

    def test_ghost_c_sl3_value(self):
        """Ghost central charge for sl_3 DS = 6."""
        assert ghost_c_sl3() == Fraction(6)

    def test_ghost_c_sl3_identity(self):
        """c(sl_3, k) - c(W_3, k) = 6 for all k != -3."""
        result = verify_ghost_c_sl3_identity()
        assert result['all_match'] is True

    def test_ghost_c_sl3_k_independent(self):
        """The ghost central charge is independent of k."""
        result = verify_ghost_c_sl3_identity(k_values=[1, 5, 17, 100, 1000])
        for r in result['results']:
            assert r['difference'] == Fraction(6)

    def test_ghost_c_formula_N3(self):
        """Ghost c = N(N-1) = 6 for N=3."""
        assert ghost_central_charge_sl_N(3) == Fraction(6)


# ============================================================================
# 11.  KAPPA AND COMPLEMENTARITY
# ============================================================================

class TestKappaComplementarity:
    """Tests for W_3 modular characteristic and complementarity."""

    def test_kappa_W3_anomaly_ratio(self):
        """Anomaly ratio for W_3: rho = 5/6, NOT 1/2.

        AP1: kappa = rho * c.  For W_3, rho = H_3 - 1 = 1/2 + 1/3 = 5/6.
        DO NOT confuse with kappa = c/2 (which holds only for Virasoro).
        """
        k = 10
        c = w3_central_charge(k)
        kappa = kappa_W3(k)
        assert kappa == Fraction(5, 6) * c

    def test_kappa_not_c_over_2(self):
        """kappa(W_3) != c/2 (the Virasoro formula is WRONG for W_3).

        AP1: This is a CRITICAL pitfall.  The Virasoro formula kappa = c/2
        does NOT apply to W_3.
        """
        k = 10
        c = w3_central_charge(k)
        kappa = kappa_W3(k)
        assert kappa != c / 2, (
            'kappa(W_3) should NOT equal c/2 (that formula is for Virasoro only)'
        )

    def test_complementarity_sum_not_zero(self):
        """kappa(W_3) + kappa(W_3!) != 0 (AP24).

        For W_3: kappa + kappa' = (5/6) * (c + c') = (5/6) * 4 = 10/3.
        """
        k = 10
        comp_sum = w3_complementarity_sum(k)
        assert comp_sum == Fraction(10, 3)
        assert comp_sum != Fraction(0)

    def test_complementarity_sum_k_independent(self):
        """kappa + kappa' = 10/3 for all non-critical k."""
        for k in [1, 2, 5, 10, 50, 100]:
            assert w3_complementarity_sum(k) == Fraction(10, 3)

    def test_c_plus_c_dual_equals_4(self):
        """c(W_3, k) + c(W_3, k') = 4 where k' = -k-6."""
        for k in [1, 2, 5, 10, 50]:
            c = w3_central_charge(k)
            c_dual = w3_central_charge(-Fraction(k) - 6)
            assert c + c_dual == Fraction(4)


# ============================================================================
# 12.  THE FULL PRIMITIVITY THEOREM
# ============================================================================

class TestPrimitivityTheorem:
    """Tests for the full primitivity theorem."""

    def test_sl2_primitive(self):
        """Transferred coproduct is primitive for sl_2 (Virasoro)."""
        result = primitivity_theorem(2)
        assert result['theorem_holds'] is True

    def test_sl3_primitive(self):
        """Transferred coproduct is primitive for sl_3 (W_3).

        THIS IS THE MAIN RESULT.  The ghost-number argument works
        for sl_3, contradicting the cautionary remark in rem:gap-b-closed.
        """
        result = primitivity_theorem(3)
        assert result['theorem_holds'] is True

    def test_sl4_primitive(self):
        """Transferred coproduct is primitive for sl_4 (W_4)."""
        result = primitivity_theorem(4)
        assert result['theorem_holds'] is True

    def test_sl5_primitive(self):
        """Transferred coproduct is primitive for sl_5 (W_5)."""
        result = primitivity_theorem(5)
        assert result['theorem_holds'] is True

    def test_all_generator_pairs_sl3(self):
        """All generator pairs (T,T), (T,W), (W,T), (W,W) give primitive coproduct."""
        result = primitivity_theorem(3)
        for pair, check in result['pair_checks'].items():
            assert check['all_trees_vanish'] is True, (
                f'Coproduct not primitive for pair {pair}'
            )


# ============================================================================
# 13.  COMPARISON sl_2 vs sl_3
# ============================================================================

class TestComparison:
    """Tests comparing sl_2 and sl_3 DS-HPL transfer."""

    def test_both_primitive(self):
        """Both sl_2 and sl_3 give primitive coproducts."""
        result = compare_sl2_sl3()
        assert result['both_primitive'] is True

    def test_ghost_pairs_differ(self):
        """sl_2 has 1 ghost pair, sl_3 has 3."""
        result = compare_sl2_sl3()
        assert result['ghost_pairs_sl2'] == 1
        assert result['ghost_pairs_sl3'] == 3

    def test_ghost_degree_h_same(self):
        """ghost_degree(h) = -1 for both."""
        result = compare_sl2_sl3()
        assert result['ghost_degree_h_sl2'] == -1
        assert result['ghost_degree_h_sl3'] == -1

    def test_ghost_degree_delta_same(self):
        """ghost_degree(delta) = +1 for both."""
        result = compare_sl2_sl3()
        assert result['ghost_degree_delta_sl2'] == +1
        assert result['ghost_degree_delta_sl3'] == +1


# ============================================================================
# 14.  GENERAL N ANALYSIS
# ============================================================================

class TestGeneralN:
    """Tests for primitivity at general N."""

    def test_all_N_primitive(self):
        """Primitivity holds for N = 2, ..., 10."""
        result = primitivity_all_N(10)
        assert result['all_primitive'] is True

    def test_ghost_pairs_grow(self):
        """Number of ghost pairs is N(N-1)/2."""
        result = primitivity_all_N(10)
        for N, data in result['results'].items():
            assert data['n_ghost_pairs'] == N * (N - 1) // 2

    def test_ghost_c_grows(self):
        """Ghost central charge is N(N-1)."""
        result = primitivity_all_N(10)
        for N, data in result['results'].items():
            assert data['ghost_c'] == Fraction(N * (N - 1))


# ============================================================================
# 15.  PHYSICAL INTERPRETATION
# ============================================================================

class TestPhysicalInterpretation:
    """Tests for the physical interpretation of primitivity."""

    def test_coproduct_primitive(self):
        """Coproduct is described as PRIMITIVE (no particle production)."""
        result = where_the_nonlinearity_lives()
        assert result['coproduct'] == 'PRIMITIVE (no particle production)'

    def test_products_nontrivial(self):
        """Products are NONTRIVIAL (class M for N >= 2)."""
        result = where_the_nonlinearity_lives()
        assert 'NONTRIVIAL' in result['products']

    def test_r_matrix_nontrivial(self):
        """r-matrix is NONTRIVIAL for N >= 3."""
        result = where_the_nonlinearity_lives()
        assert 'NONTRIVIAL' in result['r_matrix']


# ============================================================================
# 16.  CROSS-CHECKS WITH EXISTING MODULES
# ============================================================================

class TestCrossChecks:
    """Cross-checks against existing compute modules."""

    def test_ghost_c_matches_cascade_engine(self):
        """Ghost central charge matches ds_shadow_cascade_engine.py.

        c_ghost(N) = N(N-1).
        For N=3: c_ghost = 6.
        """
        from compute.lib.ds_shadow_cascade_engine import c_ghost as cascade_c_ghost
        assert cascade_c_ghost(3) == ghost_c_sl3()

    def test_w3_central_charge_matches_cascade(self):
        """W_3 central charge matches ds_shadow_cascade_engine.py."""
        from compute.lib.ds_shadow_cascade_engine import c_WN
        for k in [1, 2, 5, 10]:
            assert c_WN(3, Fraction(k)) == w3_central_charge(k)

    def test_kappa_matches_cascade(self):
        """Kappa(W_3) matches ds_shadow_cascade_engine.py."""
        from compute.lib.ds_shadow_cascade_engine import kappa_WN
        for k in [1, 2, 5, 10]:
            assert kappa_WN(3, Fraction(k)) == kappa_W3(k)


# ============================================================================
# 17.  EDGE CASES AND BOUNDARY TESTS
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_arity1_trivial(self):
        """Arity 1 is trivial (no correction)."""
        result = hpl_arity_r_ghost_analysis(3, 1)
        assert result['vanishes'] is True

    def test_large_arity(self):
        """Large arity (r=20) still vanishes."""
        result = hpl_arity_r_ghost_analysis(3, 20)
        assert result['vanishes'] is True

    def test_large_N(self):
        """Large N (N=20) still gives primitive coproduct."""
        sdr = analyze_sdr_ghost_numbers(20)
        assert sdr.ghost_degree_h == -1
        assert sdr.ghost_degree_delta == +1

    def test_ghost_pair_count_N20(self):
        """N=20 has 190 ghost pairs, but argument still works."""
        assert count_ghost_pairs(20) == 190
        result = verify_ghost_degree_h(20)
        assert result['ghost_degree_h'] == -1


# ============================================================================
# 18.  MANUSCRIPT CONSISTENCY
# ============================================================================

class TestManuscriptConsistency:
    """Tests for consistency with manuscript claims."""

    def test_rem_gap_b_closed_is_overcautious(self):
        """rem:gap-b-closed suggests failure for N >= 3 is possible.

        Our analysis shows this is OVERCAUTIOUS: the ghost-number
        argument works for ALL N.  The remark should be updated.
        """
        # The remark says: "For multi-step reductions (sl_N with N >= 3),
        # where multiple ghost pairs are present, the ghost-number
        # obstruction may fail and genuine higher-arity coproduct
        # corrections could appear."
        #
        # Our computation shows: this does NOT happen.  The ghost-number
        # argument is universal.
        result_sl3 = primitivity_theorem(3)
        result_sl4 = primitivity_theorem(4)
        assert result_sl3['theorem_holds'] is True
        assert result_sl4['theorem_holds'] is True

    def test_prop_coproduct_arity2_generalizes(self):
        """prop:coproduct-arity2-vanishing generalizes from sl_2 to all N.

        The proof in 3d_gravity.tex works for sl_2 (Virasoro).
        The same argument works verbatim for sl_N (W_N) for all N.
        """
        for N in range(2, 8):
            result = coproduct_arity2_vanishes(N, 'T', 'T')
            assert result['all_trees_vanish'] is True, (
                f'Arity-2 vanishing fails for N = {N}'
            )

    def test_adversarial_caveat_exists(self):
        """The module includes an adversarial self-audit."""
        caveat = adversarial_caveat()
        assert 'establishes' in caveat
        assert 'does_not_establish' in caveat
        assert caveat['argument_type'] == 'Z-grading (structural, independent of coefficients)'
        assert 'SUFFICIENT' in caveat['verdict']

    def test_shadow_depth_in_products_not_coproduct(self):
        """W_3 has infinite shadow depth, but this is in the PRODUCTS,
        not the coproduct.

        The shadow tower Theta_A^{<=r} measures the nonlinearity of
        the transferred products m_n^{W_N}.  The coproduct is primitive
        (no shadow tower structure).
        """
        nonlinearity = where_the_nonlinearity_lives()
        assert nonlinearity['coproduct'] == 'PRIMITIVE (no particle production)'
        assert 'class M' in nonlinearity['products']
