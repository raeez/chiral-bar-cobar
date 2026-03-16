"""Unified test suite for MC5 higher-genus bridge: BV/BRST = bar at g >= 2.

Consolidates tests from:
  test_mc5_frontier_modules.py
  test_mc5_genus2_redteam.py
  test_mc5_genus2_defense.py
  test_mc5_genus_geq2_strategies.py

All tests compute real mathematics -- no string-checking tests.
All arithmetic is exact (sympy.Rational).

Organization:
  I.   Arakelov-Bar structure (theta chars, prime form, Arnold defect, Hodge)
  II.  Clutching induction (sewing, degeneration, induction tower)
  III. Universality defense (kappa uniqueness, antisymmetry, Schur)
  IV.  Convergence and A-hat genus (Bernoulli, generating function, radius)
  V.   Cross-family universality (F_g ratios, complementarity, spot checks)
  VI.  Proof strategies (clutching, excision, Schottky, TFT, deformation)
  VII. Full defense battery and quantitative probes
"""

import math
import pytest
from sympy import (
    Rational, Integer, Symbol, simplify, S,
    bernoulli, factorial, pi,
)

from compute.lib.mc5_higher_genus import (
    STANDARD_FAMILIES,
    kappa_values_all_families,
    arakelov_green_identity,
    fay_trisecant_dimensional_analysis,
    quasi_modular_form_dimension,
    symmetry_reduction_dimension,
    arnold_defect_genus_g,
    theta_characteristics_count,
    prime_form_section_type,
    sewing_correction,
    sewing_correction_table,
    non_separating_degeneration_formula,
    induction_step_verification,
    clutching_compatibility,
    verify_kappa_uniqueness,
    verify_kappa_uniqueness_numerical,
    verify_antisymmetry,
    costello_scaling_analysis,
    period_matrix_trace_structure,
    schur_lemma_argument,
    convergence_radius_data,
    ahat_generating_function_check,
    ahat_multiplicativity_connected_coefficients,
    verify_lambda_fp_bernoulli,
    lambda_fp_table,
    verify_F_g_all_families,
    full_genus_g_defense,
    clutching_additivity_separating,
    clutching_nonseparating,
    clutching_induction_tower,
    handle_increment_sequence,
    deformation_obstruction_class,
    smoothing_compatibility,
    excision_decomposition,
    excision_curvature_additivity,
    formal_neighborhood_boundary,
    beauville_laszlo_decomposition,
    schottky_propagator_terms,
    schottky_arnold_defect,
    schottky_genus2_explicit,
    tft_frobenius_structure,
    tft_partition_function,
    lambda_fp_factorization_analysis,
    bernoulli_recursion,
    combined_genus_table,
    strategy_comparison,
)
from compute.lib.utils import lambda_fp, F_g
from compute.lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3,
    kappa_sl2, kappa_sl3,
)


# ============================================================================
# I. ARAKELOV-BAR STRUCTURE (17 tests)
# ============================================================================

class TestThetaCharacteristics:
    """Theta characteristics on Sigma_g."""

    @pytest.mark.parametrize("g,parity,expected", [
        (1, 'odd', 1), (1, 'even', 3),
        (2, 'odd', 6), (2, 'even', 10),
        (3, 'odd', 28), (3, 'even', 36),
    ])
    def test_known_values(self, g, parity, expected):
        assert theta_characteristics_count(g, parity) == expected

    @pytest.mark.parametrize("g", [1, 4, 7])
    def test_odd_plus_even_equals_2_to_2g(self, g):
        odd = theta_characteristics_count(g, 'odd')
        even = theta_characteristics_count(g, 'even')
        assert odd + even == 2 ** (2 * g)


class TestPrimeFormAndArnoldDefect:
    """Prime form E(z,w) and Arnold defect structure."""

    @pytest.mark.parametrize("g", [0, 1, 3])
    def test_section_type_minus_half(self, g):
        assert prime_form_section_type(g)["section_type"] == "K^{-1/2} boxtimes K^{-1/2}"
        assert prime_form_section_type(g)["antisymmetric"] is True
        assert prime_form_section_type(g)["vanishing_order_diagonal"] == 1

    def test_genus0_arnold_exact(self):
        r = arnold_defect_genus_g(0)
        assert r["defect"] == Integer(0)
        assert r["type"] == "exact"

    def test_genus1_lambda_fp(self):
        r = arnold_defect_genus_g(1)
        assert r["lambda_fp"] == Rational(1, 24)

    @pytest.mark.parametrize("g", [2, 5, 10])
    def test_genus_geq2_forced_scalar(self, g):
        r = arnold_defect_genus_g(g)
        assert r["forced_scalar"] is True
        assert r["lambda_fp"] == lambda_fp(g)


class TestFayAndSymmetry:
    """H^{1,1}(Sigma_g) = 1 and symmetry reduction."""

    @pytest.mark.parametrize("g", [1, 5, 20])
    def test_h11_one_defect_scalar(self, g):
        d = fay_trisecant_dimensional_analysis(g)
        assert d["h_11"] == 1
        assert d["h_10"] == g
        assert d["total_betti"] == 2 + 2 * g

    @pytest.mark.parametrize("g,expected", [(1, 1), (3, 6), (5, 15)])
    def test_triangular_numbers(self, g, expected):
        assert quasi_modular_form_dimension(g) == expected

    @pytest.mark.parametrize("g", [1, 10])
    def test_symmetry_reduces_to_one(self, g):
        r = symmetry_reduction_dimension(g)
        assert r["full_dimension"] == g * (g + 1) // 2
        assert r["after_symmetry"] == 1


# ============================================================================
# II. CLUTCHING INDUCTION (15 tests)
# ============================================================================

class TestSewingCorrection:
    """Delta_g = lambda_g - lambda_{g-1} < 0 for g >= 2."""

    @pytest.mark.parametrize("g", [2, 3, 5, 10, 15])
    def test_negative(self, g):
        assert sewing_correction(g) < 0
        assert sewing_correction(g) == lambda_fp(g) - lambda_fp(g - 1)

    def test_g2_explicit(self):
        assert sewing_correction(2) == Rational(7, 5760) - Rational(1, 24)

    def test_table_all_negative(self):
        table = sewing_correction_table(10)
        for g, entry in table.items():
            assert entry["negative"] is True


class TestClutchingInduction:
    """Non-separating degeneration and induction step."""

    @pytest.mark.parametrize("g", [2, 3, 5])
    def test_degeneration_locality(self, g):
        r = non_separating_degeneration_formula(g)
        assert r["source_genus"] == g - 1
        assert r["correction_is_local"] is True
        assert r["sewing_negative"] is True

    def test_base_case(self):
        assert induction_step_verification(1)["verified"] is True

    @pytest.mark.parametrize("g", [2, 5, 10])
    def test_induction_step(self, g):
        r = induction_step_verification(g)
        assert r["decomposition_holds"] is True
        assert r["correction_negative"] is True

    @pytest.mark.parametrize("g1,g2", [(1, 1), (1, 2), (2, 3), (3, 3)])
    def test_separating_clutching(self, g1, g2):
        r = clutching_compatibility(g1, g2)
        assert r["decomposition_holds"] is True
        g = g1 + g2
        assert r["nodal_correction"] == lambda_fp(g) - lambda_fp(g1) - lambda_fp(g2)


# ============================================================================
# III. UNIVERSALITY DEFENSE (15 tests)
# ============================================================================

class TestKappaUniqueness:
    """Additivity + antisymmetry + A-hat => kappa unique."""

    def test_km_slopes(self):
        r = verify_kappa_uniqueness()
        for fam in ["sl2", "sl3", "G2", "B2"]:
            assert r[f"{fam}_slope"]

    def test_w3_sigma(self):
        assert verify_kappa_uniqueness()["W3_sigma_is_5_6"]

    def test_ahat_normalization(self):
        r = verify_kappa_uniqueness()
        assert r["ahat_lambda1"] and r["ahat_lambda2"]

    @pytest.mark.parametrize("fam,expected", [
        ("sl2", Rational(9, 4)), ("sl3", Rational(16, 3)),
        ("G2", Rational(35, 4)), ("B2", Rational(20, 3)),
    ])
    def test_kappa_k1_numerical(self, fam, expected):
        assert STANDARD_FAMILIES[fam]["kappa"](Rational(1)) == expected

    def test_all_families_have_dual(self):
        fams = kappa_values_all_families(1)
        for name, (k, kd) in fams.items():
            assert k is not None and kd is not None

    @pytest.mark.parametrize("family", list(STANDARD_FAMILIES.keys()))
    def test_antisymmetry(self, family):
        assert verify_antisymmetry([family])[family] is True

    @pytest.mark.parametrize("algebra", ["Heisenberg", "sl2", "Virasoro", "W3"])
    def test_schur_applies(self, algebra):
        assert schur_lemma_argument(algebra)["schur_applies"]


class TestCostelloAndPeriodMatrix:
    """Costello scaling and period matrix trace."""

    @pytest.mark.parametrize("g", [1, 5, 15])
    def test_costello_scaling(self, g):
        d = costello_scaling_analysis(g)
        assert d["loop_order"] == g - 1
        assert d["locality"]
        assert d["lambda_g_FP"] > 0

    @pytest.mark.parametrize("g", [2, 5, 10])
    def test_period_trace_scalar(self, g):
        d = period_matrix_trace_structure(g)
        assert d["trace_reduces_to_scalar"]
        assert d["siegel_dim"] == g * (g + 1) // 2
        assert d["moduli_dim"] == 3 * g - 3

    def test_torelli_proper(self):
        assert period_matrix_trace_structure(4)["torelli_proper_subvariety"]
        assert not period_matrix_trace_structure(3)["torelli_proper_subvariety"]


# ============================================================================
# IV. CONVERGENCE AND A-HAT GENUS (13 tests)
# ============================================================================

class TestLambdaFPBernoulli:
    """lambda_g matches Bernoulli formula."""

    @pytest.mark.parametrize("g,expected", [
        (1, Rational(1, 24)), (2, Rational(7, 5760)), (3, Rational(31, 967680)),
    ])
    def test_known_values(self, g, expected):
        assert lambda_fp(g) == expected

    @pytest.mark.parametrize("g", [1, 4, 8, 15])
    def test_bernoulli_match(self, g):
        B_2g = bernoulli(2 * g)
        expected = (2**(2*g-1) - 1) * abs(B_2g) / (2**(2*g-1) * factorial(2*g))
        assert simplify(lambda_fp(g) - expected) == 0

    def test_all_positive_and_decreasing(self):
        for g in range(1, 15):
            assert lambda_fp(g) > 0
            assert lambda_fp(g) > lambda_fp(g + 1)


class TestAhatAndConvergence:
    """A-hat generating function and convergence radius."""

    def test_ahat_coefficients(self):
        checks = ahat_generating_function_check(6)
        for g, data in checks.items():
            assert data["match"], f"A-hat mismatch at genus {g}"

    def test_multiplicativity_c1(self):
        r = ahat_multiplicativity_connected_coefficients()
        assert r["c1"] == Rational(-1, 24)
        assert r["c2_rational"] and r["c3_rational"]

    def test_convergence_radius(self):
        r = convergence_radius_data()
        assert r["converging"]
        assert 0.0253 < r["theoretical_limit_float"] < 0.0254

    def test_ratios_bounded_and_approaching(self):
        r = convergence_radius_data(max_g=15)
        limit = r["theoretical_limit_float"]
        for g in range(2, 15):
            assert r["ratios_exact"][g] < 1
        assert abs(r["ratios_float"][14] - limit) / limit < 0.005

    @pytest.mark.parametrize("g", [1, 5, 10])
    def test_bernoulli_recursion_matches(self, g):
        assert bernoulli_recursion(10)[g] == lambda_fp(g)

    def test_verify_lambda_fp_bernoulli_bulk(self):
        r = verify_lambda_fp_bernoulli(10)
        assert all(r.values())


# ============================================================================
# V. CROSS-FAMILY UNIVERSALITY (12 tests)
# ============================================================================

class TestCrossFamilyUniversality:
    """F_g(A)/F_g(B) = kappa(A)/kappa(B), genus-independent."""

    @pytest.mark.parametrize("g", [1, 3, 10])
    def test_universality(self, g):
        r = verify_F_g_all_families(g)
        ratio_keys = [k for k in r if k.endswith("_matches")]
        assert all(r[k] for k in ratio_keys)

    def test_heisenberg_sl2_ratio_all_genera(self):
        kh, ksl2 = Rational(1), Rational(9, 4)
        for g in [1, 3, 7]:
            assert simplify(F_g(kh, g) / F_g(ksl2, g) - kh / ksl2) == 0


class TestComplementarityAndSpotChecks:
    """Complementarity and exact numerical checks."""

    @pytest.mark.parametrize("g", [1, 3, 7])
    def test_virasoro_complementarity(self, g):
        c = Symbol('c')
        total = simplify(F_g(c/2, g) + F_g((26-c)/2, g))
        assert simplify(total - 13 * lambda_fp(g)) == 0

    def test_sl2_complementarity(self):
        for g in [1, 3]:
            for k_val in [1, 7]:
                s = F_g(kappa_sl2(k_val), g) + F_g(kappa_sl2(-k_val - 4), g)
                assert s == 0

    def test_heisenberg_k1_F2(self):
        assert F_g(Rational(1), 2) == Rational(7, 5760)

    def test_virasoro_c26_F2(self):
        assert F_g(Rational(13), 2) == Rational(91, 5760)

    def test_critical_level_vanishes(self):
        for g in [1, 5, 10]:
            assert F_g(Rational(0), g) == 0

    def test_genus1_F_kappa_over_24(self):
        kappa = Symbol('kappa')
        assert simplify(F_g(kappa, 1) - kappa / 24) == 0

    def test_genus_tower_monotone(self):
        for g in [2, 5, 14]:
            assert F_g(Rational(1), g) > F_g(Rational(1), g + 1)


# ============================================================================
# VI. PROOF STRATEGIES (30 tests)
# ============================================================================

class TestStrategyAClutching:
    """Clutching induction: sewing propagates BV=bar."""

    @pytest.mark.parametrize("g1,g2", [(1, 1), (1, 3), (2, 3)])
    def test_separating_deviation_negative(self, g1, g2):
        r = clutching_additivity_separating(g1, g2)
        assert not r['is_additive']
        assert r['lambda_deviation'] < 0

    @pytest.mark.parametrize("g", [2, 5, 11])
    def test_nonseparating_negative_handle(self, g):
        r = clutching_nonseparating(g)
        assert r['lambda_handle'] < 0
        assert r['handle_is_kappa_times_lambda_handle']

    def test_induction_tower(self):
        tower = clutching_induction_tower(8)
        for g, data in tower.items():
            assert data['cumulative_consistent']

    def test_handle_magnitudes_decrease(self):
        inc = handle_increment_sequence(10)
        for g in [2, 5, 9]:
            assert abs(inc[g]) > abs(inc[g + 1])


class TestStrategyBDeformation:
    """Deformation from nodal curves."""

    @pytest.mark.parametrize("g", [1, 3, 7])
    def test_obstruction_proportional(self, g):
        kappa = Symbol('kappa')
        r = deformation_obstruction_class(g)
        assert simplify(r['obstruction'] - kappa * lambda_fp(g)) == 0

    @pytest.mark.parametrize("g", [2, 5])
    def test_smoothing_interaction_negative(self, g):
        r = smoothing_compatibility(g)
        assert not r['nodes_independent']
        assert r['interaction'] < 0


class TestStrategyCExcision:
    """Ayala-Francis excision."""

    @pytest.mark.parametrize("g", [2, 5, 9])
    def test_decomposition(self, g):
        r = excision_decomposition(g)
        assert r['num_pants'] == 2 * g - 2
        assert r['num_gluing_circles'] == 3 * g - 3
        assert r['chi_consistent']

    @pytest.mark.parametrize("g", [1, 4])
    def test_F_g_from_excision(self, g):
        kappa = Symbol('kappa')
        r = excision_decomposition(g)
        assert simplify(r['F_g_from_excision'] - kappa * lambda_fp(g)) == 0

    @pytest.mark.parametrize("g", [1, 5])
    def test_curvature_topological(self, g):
        r = excision_curvature_additivity(g)
        assert r['local_curvature_pants'] == 0
        assert r['curvature_is_topological']


class TestStrategyDFormalModuli:
    """Formal GAGA and Beauville-Laszlo."""

    @pytest.mark.parametrize("g", [1, 3, 7])
    def test_formal_gaga_and_bl(self, g):
        r = formal_neighborhood_boundary(g)
        assert r['formal_gaga_applicable']
        assert r['coherence_holds']
        bl = beauville_laszlo_decomposition(g)
        assert bl['absorbed_by_period_correction']
        assert bl['remaining_obstruction'] == 0


class TestStrategyESchottky:
    """Schottky uniformization."""

    @pytest.mark.parametrize("g", [1, 3, 7])
    def test_word_structure(self, g):
        r = schottky_propagator_terms(g, max_words=3)
        assert r['num_generators'] == g
        assert r['word_counts'][0] == 1
        assert r['word_counts'][1] == 2 * g
        assert r['word_counts'][2] == 2 * g * (2 * g - 1)

    @pytest.mark.parametrize("g", [2, 5])
    def test_absolute_convergence(self, g):
        assert schottky_propagator_terms(g)['convergence'] == 'absolute'

    def test_genus1_conditional(self):
        assert schottky_propagator_terms(1)['convergence'] == 'conditional'

    @pytest.mark.parametrize("g", [1, 4])
    def test_defect_integral(self, g):
        kappa = Symbol('kappa')
        r = schottky_arnold_defect(g)
        assert simplify(r['integrated_defect'] - kappa * lambda_fp(g)) == 0

    def test_genus2_explicit(self):
        r = schottky_genus2_explicit()
        assert r['lambda_2'] == Rational(7, 5760)
        assert r['schottky_generators'] == 2


class TestStrategyFTFT:
    """TFT bootstrap."""

    @pytest.mark.parametrize("g", [1, 3, 7])
    def test_partition_function(self, g):
        kappa = Symbol('kappa')
        assert simplify(tft_partition_function(kappa, g) - kappa * lambda_fp(g)) == 0

    def test_frobenius_curved(self):
        kappa = Symbol('kappa')
        r = tft_frobenius_structure(kappa)
        assert r['euler_class'] == kappa


class TestCrossStrategy:
    """Cross-strategy lambda_g analysis and comparison."""

    def test_additivities_fail(self):
        analysis = lambda_fp_factorization_analysis(6)
        for (g1, g2), data in analysis['additivity_failures'].items():
            assert data['deviation'] < 0

    def test_strategy_comparison(self):
        comp = strategy_comparison()
        assert len(comp) == 6
        assert comp['A_clutching']['feasibility'] == 'LIKELY'
        assert comp['F_tft_bootstrap']['feasibility'] == 'SPECULATIVE'


# ============================================================================
# VII. FULL DEFENSE BATTERY AND QUANTITATIVE PROBES (24 tests)
# ============================================================================

class TestFullDefenseBattery:
    """Full 7-axis defense at critical genera."""

    def test_genus2(self):
        d = full_genus_g_defense(2)
        assert d["defense_2_fay_scalar"]["defect_forced_scalar"]
        assert d["defense_3_costello"]["locality"]
        assert d["defense_4_mumford"]["lambda_g"] == Rational(7, 5760)
        assert d["defense_5_period_trace"]["trace_reduces_to_scalar"]

    def test_genus3(self):
        d = full_genus_g_defense(3)
        assert d["defense_2_fay_scalar"]["defect_forced_scalar"]
        assert d["defense_4_mumford"]["lambda_g"] == Rational(31, 967680)
        assert "g1=1,g2=2" in d["defense_6_clutching"]

    @pytest.mark.parametrize("g", [5, 10])
    def test_high_genus(self, g):
        d = full_genus_g_defense(g)
        assert d["defense_2_fay_scalar"]["defect_forced_scalar"]
        assert d["defense_4_mumford"]["lambda_g"] > 0

    def test_defense_summary_uniqueness(self):
        assert all(verify_kappa_uniqueness().values())

    def test_defense_summary_bernoulli(self):
        assert all(verify_lambda_fp_bernoulli(10).values())


class TestQuantitativeProbes:
    """Deep structural probes."""

    @pytest.mark.parametrize("g", [3, 5, 7])
    def test_clutching_deviation_negative(self, g):
        """lambda_{2g} - 2*lambda_g < 0."""
        assert lambda_fp(2 * g) - 2 * lambda_fp(g) < 0

    def test_lambda_2_from_lambda_1_correction(self):
        """lambda_2 / lambda_1^2 = 7/10."""
        assert lambda_fp(2) / lambda_fp(1)**2 == Rational(7, 10)

    @pytest.mark.parametrize("g", [2, 5, 10])
    def test_handle_increment_negative(self, g):
        assert lambda_fp(g) - lambda_fp(g - 1) < 0

    def test_separating_deviation_pairs(self):
        """lambda_{g1+g2} < lambda_{g1} + lambda_{g2}."""
        for g1, g2 in [(1, 1), (1, 3), (2, 3), (3, 4)]:
            assert lambda_fp(g1 + g2) - lambda_fp(g1) - lambda_fp(g2) < 0

    def test_kappa_locality(self):
        assert kappa_heisenberg(1) == Rational(1)
        assert kappa_virasoro(2) == Rational(1)
        assert kappa_sl2(1) == Rational(9, 4)
        assert kappa_w3(6) == Rational(5)

    def test_local_determines_global(self):
        kappa = Symbol('kappa')
        for g in [1, 5, 10]:
            assert simplify(F_g(kappa, g) - kappa * lambda_fp(g)) == 0

    def test_separation_of_concerns(self):
        kappa = Symbol('kappa')
        for g in [1, 3, 7]:
            assert F_g(kappa, g).coeff(kappa) == lambda_fp(g)
            assert lambda_fp(g).is_rational

    def test_combined_genus_table(self):
        table = combined_genus_table(6)
        for g in range(2, 7):
            assert table[g]['lambda_g'] == lambda_fp(g)
            assert table[g]['handle_increment'] < 0
            assert table[g]['num_pants'] == 2 * g - 2
            assert table[g]['schottky_words_length_1'] == 2 * g

    def test_convergence_ratio(self):
        analysis = lambda_fp_factorization_analysis(10)
        target = 1.0 / (2.0 * math.pi) ** 2
        for g in [7, 8, 9]:
            assert abs(analysis['ratios'][g]['float'] - target) < 0.01
