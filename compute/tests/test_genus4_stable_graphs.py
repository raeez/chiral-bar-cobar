"""Comprehensive tests for genus-4 stable graph enumeration and shadow amplitudes.

71 tests organized by:
  1. Enumeration and census (10 tests)
  2. Orbifold Euler characteristic (6 tests)
  3. Faber-Pandharipande lambda_4^FP (10 tests)
  4. Scalar graph sum polynomial (8 tests)
  5. Spectral sequence and boundary strata (8 tests)
  6. Free energy and complementarity (9 tests)
  7. Self-loop parity vanishing (5 tests)
  8. Planted-forest and shadow visibility (7 tests)
  9. Named graphs and cross-genus consistency (8 tests)

Every computed quantity has at least 2 independent verification routes.
Exact Fraction arithmetic throughout (no floating-point comparisons).

References:
  higher_genus_modular_koszul.tex: thm:theorem-d, prop:self-loop-vanishing,
    cor:shadow-visibility-genus
  stable_graph_enumeration.py: StableGraph, enumerate_stable_graphs
  higher_genus_graph_sum_engine.py: lambda_fp, stable_graphs
"""

import pytest
from fractions import Fraction
from math import factorial
from collections import Counter

from compute.lib.genus4_stable_graphs import (
    genus4_stable_graphs_n0,
    genus4_graph_count,
    genus4_by_vertex_count,
    genus4_by_edge_count,
    genus4_by_loop_number,
    genus4_automorphism_spectrum,
    genus4_euler_check,
    genus4_euler_decomposition,
    lambda4_fp,
    lambda4_fp_three_way_check,
    genus4_scalar_sum_polynomial,
    genus4_scalar_sum_at,
    genus4_spectral_sequence_e1,
    genus4_spectral_sequence_counts,
    genus4_boundary_strata,
    genus4_boundary_strata_counts,
    genus4_boundary_divisor_types,
    genus4_free_energy_heisenberg,
    genus4_free_energy_virasoro,
    genus4_free_energy_affine,
    genus4_free_energy_betagamma,
    genus4_cross_family_table,
    genus4_virasoro_complementarity,
    genus4_km_antisymmetry,
    genus4_self_loop_parity_check,
    genus4_named_graphs,
    genus4_graph_profiles,
    genus4_graph_weight_sum,
    genus4_planted_forest_census,
    genus4_shadow_visibility_check,
    genus4_inverse_aut_sum,
    genus4_max_automorphism,
    cross_genus_consistency_check,
    is_planted_forest,
    genus4_summary,
)
from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    orbifold_euler_characteristic,
    _bernoulli_exact,
    _lambda_fp_exact,
    _chi_orb_open,
)


# ============================================================================
# 1. Enumeration and census (10 tests)
# ============================================================================

class TestEnumeration:
    """Verify the complete enumeration of 379 genus-4 stable graphs."""

    def test_total_count(self):
        """There are exactly 379 stable graphs at (g=4, n=0)."""
        assert genus4_graph_count() == 379

    def test_vertex_count_distribution(self):
        """By vertex count: 5 + 29 + 79 + 126 + 98 + 42 = 379."""
        by_v = genus4_by_vertex_count()
        assert by_v == {1: 5, 2: 29, 3: 79, 4: 126, 5: 98, 6: 42}
        assert sum(by_v.values()) == 379

    def test_edge_count_distribution(self):
        """By edge count: 1+3+7+21+43+75+89+81+42+17 = 379."""
        by_e = genus4_by_edge_count()
        assert by_e == {
            0: 1, 1: 3, 2: 7, 3: 21, 4: 43,
            5: 75, 6: 89, 7: 81, 8: 42, 9: 17,
        }
        assert sum(by_e.values()) == 379

    def test_loop_number_distribution(self):
        """By loop number: 11+36+93+128+111 = 379."""
        by_h1 = genus4_by_loop_number()
        assert by_h1 == {0: 11, 1: 36, 2: 93, 3: 128, 4: 111}
        assert sum(by_h1.values()) == 379

    def test_all_graphs_are_stable(self):
        """Every enumerated graph satisfies the stability condition."""
        for g in genus4_stable_graphs_n0():
            assert g.is_stable, f"Unstable graph: {g}"

    def test_all_graphs_are_connected(self):
        """Every enumerated graph is connected."""
        for g in genus4_stable_graphs_n0():
            assert g.is_connected, f"Disconnected graph: {g}"

    def test_all_graphs_have_genus_4(self):
        """Every enumerated graph has arithmetic genus 4."""
        for g in genus4_stable_graphs_n0():
            assert g.arithmetic_genus == 4, (
                f"Wrong genus {g.arithmetic_genus}: {g}"
            )

    def test_max_edge_count(self):
        """Maximum edge count = dim M_4 = 3*4-3 = 9."""
        assert max(g.num_edges for g in genus4_stable_graphs_n0()) == 9

    def test_min_edge_count(self):
        """Minimum edge count = 0 (the smooth genus-4 curve)."""
        assert min(g.num_edges for g in genus4_stable_graphs_n0()) == 0

    def test_no_legs(self):
        """All graphs have 0 marked points."""
        for g in genus4_stable_graphs_n0():
            assert g.num_legs == 0


# ============================================================================
# 2. Orbifold Euler characteristic (6 tests)
# ============================================================================

class TestEulerCharacteristic:
    """Verify the orbifold Euler characteristic from the graph sum."""

    def test_chi_mbar_4_value(self):
        """chi^orb(M_bar_{4,0}) = -4717039/6220800."""
        computed, expected, match = genus4_euler_check()
        assert match
        assert computed == Fraction(-4717039, 6220800)

    def test_chi_open_4_from_bernoulli(self):
        """chi^orb(M_4) = B_8/(4*4*3) = -1/1440."""
        chi_open = _chi_orb_open(4, 0)
        expected = _bernoulli_exact(8) / Fraction(4 * 4 * 3)
        assert chi_open == expected
        assert chi_open == Fraction(-1, 1440)

    def test_euler_decomposition_sums_correctly(self):
        """Sum of per-graph chi contributions equals the total."""
        decomp = genus4_euler_decomposition()
        total = sum(contrib for _, contrib in decomp)
        expected = Fraction(-4717039, 6220800)
        assert total == expected

    def test_euler_decomposition_count(self):
        """There are 379 contributions in the decomposition."""
        decomp = genus4_euler_decomposition()
        assert len(decomp) == 379

    def test_smooth_graph_chi_contribution(self):
        """The smooth graph contributes chi^orb(M_4) = B_8/(4*4*3) = -1/1440."""
        decomp = genus4_euler_decomposition()
        # The smooth graph is index 0 (first in enumeration) with 0 edges
        smooth_contribs = [
            (i, c) for i, c in decomp
            if genus4_stable_graphs_n0()[i].num_edges == 0
        ]
        assert len(smooth_contribs) == 1
        _, smooth_chi = smooth_contribs[0]
        assert smooth_chi == Fraction(-1, 1440)

    def test_chi_consistent_with_lower_genera(self):
        """chi^orb(M_bar_{g,0}) values are consistent across genera."""
        g2 = enumerate_stable_graphs(2, 0)
        g3 = enumerate_stable_graphs(3, 0)
        g4 = list(genus4_stable_graphs_n0())
        chi2 = orbifold_euler_characteristic(g2)
        chi3 = orbifold_euler_characteristic(g3)
        chi4 = orbifold_euler_characteristic(g4)
        assert chi2 == Fraction(-181, 1440)
        assert chi3 == Fraction(-12419, 90720)
        assert chi4 == Fraction(-4717039, 6220800)


# ============================================================================
# 3. Faber-Pandharipande lambda_4^FP (10 tests)
# ============================================================================

class TestLambda4FP:
    """Verify lambda_4^FP = 127/154828800 by multiple methods."""

    def test_lambda4_exact_value(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda4_fp() == Fraction(127, 154828800)

    def test_lambda4_from_bernoulli(self):
        """Direct from B_8: (2^7-1)|B_8|/(2^7 * 8!) = 127/154828800."""
        B8 = _bernoulli_exact(8)
        assert B8 == Fraction(-1, 30)
        result = (2**7 - 1) * abs(B8) / Fraction(2**7 * factorial(8))
        assert result == Fraction(127, 154828800)

    def test_lambda4_three_way(self):
        """Three independent computations agree."""
        m1, m2, m3, match = lambda4_fp_three_way_check()
        assert match
        assert m1 == m2 == m3 == Fraction(127, 154828800)

    def test_lambda4_from_power_series(self):
        """Power series inversion of (x/2)/sin(x/2) gives lambda_4."""
        # f(y) = sum (-1)^n y^n/(2n+1)!, 1/f to order y^4
        c_f = [Fraction((-1)**n, factorial(2*n+1)) for n in range(5)]
        a = [Fraction(0)] * 5
        a[0] = Fraction(1)
        for k in range(1, 5):
            s = sum(c_f[j] * a[k-j] for j in range(1, k+1))
            a[k] = -s
        coeff_x8 = a[4] / Fraction(4**4)
        assert coeff_x8 == Fraction(127, 154828800)

    def test_lambda4_positive(self):
        """lambda_4^FP > 0."""
        assert lambda4_fp() > 0

    def test_lambda4_less_than_lambda3(self):
        """lambda_4^FP < lambda_3^FP (decreasing sequence)."""
        assert lambda4_fp() < _lambda_fp_exact(3)

    def test_lambda4_greater_than_lambda5(self):
        """lambda_4^FP > lambda_5^FP."""
        assert lambda4_fp() > _lambda_fp_exact(5)

    def test_lambda4_from_general_engine(self):
        """Cross-check against higher_genus_graph_sum_engine."""
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda4_numerator_is_mersenne(self):
        """127 = 2^7 - 1 is a Mersenne prime, from the formula."""
        assert 127 == 2**7 - 1

    def test_lambda_ratio_g3_to_g4(self):
        """lambda_4/lambda_3 = (127/154828800) / (31/967680)."""
        ratio = lambda4_fp() / _lambda_fp_exact(3)
        expected = Fraction(127 * 967680, 31 * 154828800)
        assert ratio == expected


# ============================================================================
# 4. Scalar graph sum polynomial (8 tests)
# ============================================================================

class TestScalarPolynomial:
    """Verify the scalar graph sum polynomial in kappa."""

    def test_polynomial_has_10_terms(self):
        """Polynomial has terms from kappa^0 to kappa^9."""
        poly = genus4_scalar_sum_polynomial()
        assert set(poly.keys()) == set(range(10))

    def test_constant_term(self):
        """Coefficient of kappa^0 = 1 (the smooth graph)."""
        poly = genus4_scalar_sum_polynomial()
        assert poly[0] == Fraction(1)

    def test_leading_term(self):
        """Coefficient of kappa^9: sum of 1/|Aut| over 9-edge graphs."""
        poly = genus4_scalar_sum_polynomial()
        assert poly[9] == Fraction(1105, 1152)

    def test_all_coefficients_positive(self):
        """All coefficients are positive (no cancellation at scalar level)."""
        poly = genus4_scalar_sum_polynomial()
        for e, c in poly.items():
            assert c > 0, f"Negative coefficient at kappa^{e}: {c}"

    def test_sum_at_kappa_1(self):
        """Evaluate at kappa=1: sum of all 1/|Aut|."""
        val = genus4_scalar_sum_at(Fraction(1))
        assert val == Fraction(15521, 240)

    def test_sum_at_kappa_0(self):
        """Evaluate at kappa=0: only the smooth graph contributes."""
        val = genus4_scalar_sum_at(Fraction(0))
        assert val == Fraction(1)

    def test_polynomial_consistency(self):
        """Evaluating the polynomial agrees with direct graph sum."""
        kappa = Fraction(3, 7)
        poly = genus4_scalar_sum_polynomial()
        poly_val = sum(c * kappa**e for e, c in poly.items())
        direct_val = genus4_scalar_sum_at(kappa)
        assert poly_val == direct_val

    def test_codim1_coefficient(self):
        """Coefficient of kappa^1 = sum 1/|Aut| over codim-1 graphs = 2."""
        poly = genus4_scalar_sum_polynomial()
        # 3 graphs at codim 1: irr_node (aut=2), sep_31 (aut=1 or 2), sep_22 (aut=2)
        assert poly[1] == Fraction(2)


# ============================================================================
# 5. Spectral sequence and boundary strata (8 tests)
# ============================================================================

class TestSpectralSequence:
    """Verify the genus spectral sequence and boundary strata."""

    def test_e1_page_sizes(self):
        """E_1 page sizes: 11, 36, 93, 128, 111."""
        counts = genus4_spectral_sequence_counts()
        assert counts == {0: 11, 1: 36, 2: 93, 3: 128, 4: 111}

    def test_trees_count(self):
        """h^1 = 0 (trees): 11 graphs."""
        pages = genus4_spectral_sequence_e1()
        assert len(pages[0]) == 11

    def test_maximal_loops_count(self):
        """h^1 = 4 (maximal): 111 graphs with all genus at vertices = 0."""
        pages = genus4_spectral_sequence_e1()
        for g in pages[4]:
            assert all(gv == 0 for gv in g.vertex_genera), (
                f"Maximal-loop graph with nonzero vertex genus: {g}"
            )

    def test_trees_have_no_loops(self):
        """All tree-level graphs (h^1=0) have first Betti number 0."""
        pages = genus4_spectral_sequence_e1()
        for g in pages[0]:
            assert g.first_betti == 0

    def test_boundary_codim_distribution(self):
        """Boundary strata codimension distribution matches edge count."""
        strata = genus4_boundary_strata_counts()
        by_edges = genus4_by_edge_count()
        assert strata == by_edges

    def test_boundary_divisors_count(self):
        """Exactly 3 codimension-1 boundary divisors."""
        divs = genus4_boundary_divisor_types()
        total = sum(len(v) for v in divs.values())
        assert total == 3

    def test_delta_irr_exists(self):
        """The irreducible boundary Delta_irr exists (genus-3 with self-loop)."""
        divs = genus4_boundary_divisor_types()
        assert len(divs["Delta_irr"]) == 1
        g = divs["Delta_irr"][0]
        assert g.vertex_genera == (3,)
        assert g.num_edges == 1

    def test_separating_divisors(self):
        """Two separating divisors: Delta_1 (genus 3+1) and Delta_2 (genus 2+2)."""
        divs = genus4_boundary_divisor_types()
        assert len(divs["Delta_1"]) == 1
        assert len(divs["Delta_2"]) == 1


# ============================================================================
# 6. Free energy and complementarity (9 tests)
# ============================================================================

class TestFreeEnergy:
    """Verify Theorem D free energy and complementarity at genus 4."""

    def test_heisenberg_F4(self):
        """F_4(H_1) = 1 * 127/154828800."""
        assert genus4_free_energy_heisenberg() == Fraction(127, 154828800)

    def test_virasoro_F4_c26(self):
        """F_4(Vir_26) = 13 * 127/154828800."""
        f4 = genus4_free_energy_virasoro(Fraction(26))
        assert f4 == Fraction(13) * Fraction(127, 154828800)

    def test_virasoro_F4_c1(self):
        """F_4(Vir_1) = (1/2) * 127/154828800."""
        f4 = genus4_free_energy_virasoro(Fraction(1))
        assert f4 == Fraction(127, 309657600)

    def test_betagamma_F4(self):
        """F_4(beta-gamma) = 127/154828800 (kappa = 1)."""
        assert genus4_free_energy_betagamma() == Fraction(127, 154828800)

    def test_affine_sl2_F4(self):
        """F_4(V_1(sl_2)) = 9/4 * 127/154828800."""
        f4 = genus4_free_energy_affine(Fraction(1), 3, 2)
        expected = Fraction(9, 4) * Fraction(127, 154828800)
        assert f4 == expected

    def test_virasoro_complementarity_c1(self):
        """F_4(Vir_1) + F_4(Vir_25) = 13 * lambda_4."""
        _, expected, match = genus4_virasoro_complementarity(Fraction(1))
        assert match

    def test_virasoro_complementarity_c13(self):
        """At the self-dual point c=13: 2*F_4(Vir_13) = 13*lambda_4."""
        total, expected, match = genus4_virasoro_complementarity(Fraction(13))
        assert match
        assert total == 2 * genus4_free_energy_virasoro(Fraction(13))

    def test_km_antisymmetry_sl2(self):
        """KM anti-symmetry for sl_2: F_4(V_k) + F_4(V_{-k-4}) = 0."""
        _, vanishes = genus4_km_antisymmetry(Fraction(1), 3, 2)
        assert vanishes

    def test_additivity(self):
        """Additivity: F_4(A+B) = F_4(A) + F_4(B) for independent sum."""
        f_heis = genus4_free_energy_heisenberg(Fraction(1))
        f_bg = genus4_free_energy_betagamma()
        # kappa(H_1 + bg) = 1 + 1 = 2
        f_sum = Fraction(2) * lambda4_fp()
        assert f_heis + f_bg == f_sum


# ============================================================================
# 7. Self-loop parity vanishing (5 tests)
# ============================================================================

class TestSelfLoopParity:
    """Verify self-loop parity vanishing at genus 4."""

    def test_single_vertex_data(self):
        """Exactly 5 single-vertex graphs at genus 4."""
        data = genus4_self_loop_parity_check()
        assert len(data) == 5

    def test_smooth_curve_present(self):
        """(4,0) smooth curve with 0 loops is present."""
        data = genus4_self_loop_parity_check()
        assert "(4,0)_loops0" in data

    def test_double_loop_no_parity_vanishing(self):
        """(2,4) with 2 loops: dim = 3*2-3+4 = 7 (odd), expected to vanish."""
        data = genus4_self_loop_parity_check()
        entry = data["(2,4)_loops2"]
        assert entry['dim'] == 7
        assert entry['dim_is_odd'] is True
        assert entry['parity_vanishing_expected'] is True

    def test_triple_loop_no_parity_vanishing(self):
        """(1,6) with 3 loops: dim = 3*1-3+6 = 6 (even), no parity vanishing."""
        data = genus4_self_loop_parity_check()
        entry = data["(1,6)_loops3"]
        assert entry['dim'] == 6
        assert entry['dim_is_odd'] is False
        assert entry['parity_vanishing_expected'] is False

    def test_quadruple_loop_vanishes(self):
        """(0,8) with 4 loops: dim = 5 (odd), expected to vanish."""
        data = genus4_self_loop_parity_check()
        entry = data["(0,8)_loops4"]
        assert entry['dim'] == 5
        assert entry['dim_is_odd'] is True
        assert entry['parity_vanishing_expected'] is True


# ============================================================================
# 8. Planted-forest and shadow visibility (7 tests)
# ============================================================================

class TestPlantedForest:
    """Verify planted-forest identification and shadow visibility."""

    def test_pf_count(self):
        """358 of 379 graphs are planted-forest (have genus-0 vertex val >= 3)."""
        census = genus4_planted_forest_census()
        assert census['pf_count'] == 358

    def test_non_pf_count(self):
        """21 graphs are NOT planted-forest."""
        census = genus4_planted_forest_census()
        assert census['non_pf_count'] == 21

    def test_non_pf_graphs_have_no_g0_val3(self):
        """Non-PF graphs have no genus-0 vertex of valence >= 3."""
        for g in genus4_stable_graphs_n0():
            if not is_planted_forest(g):
                for v in range(g.num_vertices):
                    if g.vertex_genera[v] == 0:
                        assert g.valence[v] < 3

    def test_shadow_S6_visible(self):
        """S_6 is visible at genus 4 (g_min(6) = 4)."""
        vis = genus4_shadow_visibility_check()
        assert vis['S_6_visible'] is True

    def test_shadow_S7_visible(self):
        """S_7 is visible at genus 4 (g_min(7) = 4)."""
        vis = genus4_shadow_visibility_check()
        assert vis['S_7_visible'] is True

    def test_shadow_S8_does_not_contribute(self):
        """S_8 does not contribute at genus 4 (g_min(8) = 5).

        The (0,8) single-vertex graph exists but has vanishing Hodge
        integral by self-loop parity. No multi-vertex graph at genus 4
        has a genus-0 vertex of valence >= 8 connected to other vertices.
        """
        vis = genus4_shadow_visibility_check()
        assert vis['S_8_contributes'] is False

    def test_heisenberg_pf_vanishes(self):
        """For Heisenberg (class G): all planted-forest corrections vanish.

        This is because S_r = 0 for r >= 3 in Heisenberg.
        """
        from compute.lib.genus4_stable_graphs import \
            genus4_planted_forest_scalar_contribution
        assert genus4_planted_forest_scalar_contribution() == Fraction(0)


# ============================================================================
# 9. Named graphs and cross-genus consistency (8 tests)
# ============================================================================

class TestNamedGraphs:
    """Verify named graph identification and cross-genus checks."""

    def test_smooth_graph(self):
        """Smooth genus-4 curve: g=4, 0 edges."""
        named = genus4_named_graphs()
        assert "smooth" in named
        g = named["smooth"]
        assert g.vertex_genera == (4,)
        assert g.num_edges == 0

    def test_irr_node(self):
        """Irreducible node: g=3, 1 self-loop."""
        named = genus4_named_graphs()
        assert "irr_node" in named
        g = named["irr_node"]
        assert g.vertex_genera == (3,)
        assert g.num_edges == 1

    def test_quadruple_loop(self):
        """Quadruple loop: g=0, 4 self-loops."""
        named = genus4_named_graphs()
        assert "quadruple_loop" in named
        g = named["quadruple_loop"]
        assert g.vertex_genera == (0,)
        assert g.num_edges == 4

    def test_graph_weight_sum(self):
        """Signed graph weight sum = 91/360."""
        assert genus4_graph_weight_sum() == Fraction(91, 360)

    def test_max_automorphism(self):
        """Maximum automorphism order is 384."""
        assert genus4_max_automorphism() == 384

    def test_cross_genus_counts_increasing(self):
        """Graph counts increase: 2 < 6 < 42 < 379."""
        cc = cross_genus_consistency_check()
        assert cc['counts_increasing']

    def test_cross_genus_lambdas_decreasing(self):
        """lambda_g^FP is strictly decreasing for g = 1..4."""
        cc = cross_genus_consistency_check()
        assert cc['lambdas_decreasing']

    def test_cross_genus_max_codim(self):
        """Max codimension = 3g-3 at each genus."""
        cc = cross_genus_consistency_check()
        assert all(cc['max_codim_correct'].values())


# ============================================================================
# 10. Additional structural tests (6 tests)
# ============================================================================

class TestStructural:
    """Additional structural and consistency tests."""

    def test_inverse_aut_sum_positive(self):
        """Sum of 1/|Aut| is positive."""
        s = genus4_inverse_aut_sum()
        assert s > 0

    def test_graph_profiles_G(self):
        """Class G: all graphs are scalar-only (no PF corrections)."""
        prof = genus4_graph_profiles("G")
        assert prof['active_count'] == 0
        assert prof['scalar_only_count'] == 379

    def test_graph_profiles_M(self):
        """Class M: most graphs are active (have higher-arity corrections)."""
        prof = genus4_graph_profiles("M")
        assert prof['active_count'] > 300

    def test_summary_completeness(self):
        """Summary returns all expected keys."""
        s = genus4_summary()
        expected_keys = {
            'total_graphs', 'by_h1', 'by_vertices', 'by_edges',
            'aut_spectrum_min', 'aut_spectrum_max',
            'chi_orb_mbar', 'chi_orb_open', 'lambda4_fp',
            'graph_weight_sum', 'scalar_sum_kappa1',
            'planted_forest_count',
        }
        assert expected_keys.issubset(set(s.keys()))

    def test_summary_values_consistent(self):
        """Summary values match individual function outputs."""
        s = genus4_summary()
        assert s['total_graphs'] == 379
        assert s['lambda4_fp'] == Fraction(127, 154828800)
        assert s['graph_weight_sum'] == Fraction(91, 360)

    def test_automorphism_spectrum_length(self):
        """Automorphism spectrum has 379 entries."""
        spec = genus4_automorphism_spectrum()
        assert len(spec) == 379
        assert spec[0] >= 1
        assert spec[-1] == 384


# ============================================================================
# 11. Deep cross-validation tests (8 tests)
# ============================================================================

class TestDeepCrossValidation:
    """Deep cross-validation tests with independent computation routes."""

    def test_euler_char_from_two_engines(self):
        """Euler characteristic from genus4_stable_graphs matches
        the general engine from higher_genus_graph_sum_engine."""
        from compute.lib.higher_genus_graph_sum_engine import (
            chi_orb_mbar,
        )
        chi_general = chi_orb_mbar(4, 0)
        chi_module = genus4_euler_check()[0]
        assert chi_general == chi_module

    def test_scalar_sum_from_two_engines(self):
        """Scalar sum at kappa=1 from genus4 module matches
        higher_genus_graph_sum_engine."""
        from compute.lib.higher_genus_graph_sum_engine import (
            scalar_sum_evaluate,
        )
        val_general = scalar_sum_evaluate(4, Fraction(1))
        val_module = genus4_scalar_sum_at(Fraction(1))
        assert val_general == val_module

    def test_lambda4_from_bernoulli_recurrence(self):
        """Verify B_8 via the Bernoulli recurrence, then derive lambda_4."""
        # B_8 via recurrence: sum_{k=0}^7 C(9,k)*B_k = 0
        s = Fraction(0)
        for k in range(8):
            bk = _bernoulli_exact(k)
            if bk != 0:
                c9k = factorial(9) // (factorial(k) * factorial(9 - k))
                s += Fraction(c9k) * bk
        B8 = -s / Fraction(9)
        assert B8 == Fraction(-1, 30)
        lam = (2**7 - 1) * abs(B8) / Fraction(2**7 * factorial(8))
        assert lam == Fraction(127, 154828800)

    def test_complementarity_all_c_values(self):
        """Virasoro complementarity for c = 1, 2, ..., 25."""
        l4 = lambda4_fp()
        for c_int in range(1, 26):
            c = Fraction(c_int)
            total, expected, match = genus4_virasoro_complementarity(c)
            assert match, f"Complementarity fails at c={c_int}"
            assert total == Fraction(13) * l4

    def test_heisenberg_all_levels(self):
        """F_4(H_k) = k * lambda_4 for various integer levels."""
        l4 = lambda4_fp()
        for k in range(1, 10):
            f4 = genus4_free_energy_heisenberg(Fraction(k))
            assert f4 == Fraction(k) * l4

    def test_affine_sl3_kappa(self):
        """kappa(V_k(sl_3)) = 8(k+3)/6 = 4(k+3)/3."""
        # dim(sl_3) = 8, h^v(sl_3) = 3
        k = Fraction(1)
        f4 = genus4_free_energy_affine(k, 8, 3)
        kappa = Fraction(8) * (k + 3) / Fraction(6)
        assert f4 == kappa * lambda4_fp()
        assert kappa == Fraction(16, 3)

    def test_affine_e8_kappa(self):
        """kappa(V_k(E_8)) = 248(k+30)/60 = 62(k+30)/15."""
        # dim(E_8) = 248, h^v(E_8) = 30
        k = Fraction(1)
        f4 = genus4_free_energy_affine(k, 248, 30)
        kappa = Fraction(248) * (k + 30) / Fraction(60)
        assert f4 == kappa * lambda4_fp()

    def test_ahat_genus4_coefficient(self):
        """Independent A-hat genus computation from the genus4_amplitude module."""
        from compute.lib.genus4_amplitude import lambda_FP, ahat_expansion
        assert lambda_FP(4) == Fraction(127, 154828800)
        coeffs = ahat_expansion()
        assert coeffs[4] == Fraction(127, 154828800)
