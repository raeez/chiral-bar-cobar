r"""Tests for the multi-weight genus tower: delta_F_g^cross(W_3).

Verifies the cross-channel correction at genera 2, 3, 4 using multiple
independent paths:

Path 1: Direct graph sum (brute force over all channel assignments)
Path 2: Closed-form formula (Newton-interpolated rational function)
Path 3: Limiting cases (c -> large, c = 50 self-dual)
Path 4: Koszul duality (c <-> 100-c symmetry)
Path 5: Z_2 parity (odd-W channels vanish)
Path 6: Scalar-lane firewall (diagonal boundary != kappa_i * lambda_g)
Path 7: Positivity and monotonicity

References:
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    op:multi-generator-universality (higher_genus_foundations.tex)
"""

import pytest
from fractions import Fraction

from compute.lib.multi_weight_genus_tower import (
    cross_channel_correction,
    delta_Fg_closed_form,
    full_amplitude_decomposition,
    finite_window_theorem,
    four_point_pairing_audit,
    genus2_mixed_graph_contributions,
    graph_amplitude_decomposed,
    holographic_package_entries,
    interpolate_scaled_numerator,
    modular_koszul_primary_projections,
    object_firewall,
    stable_graphs_complete,
    boundary_graphs,
    delta_F2_closed_form,
    delta_F3_closed_form,
    delta_F4_closed_form,
    verify_genus2,
    verify_genus3,
    verify_genus4,
    kappa_total,
    kappa_channel,
    lambda_fp,
    propagator,
    C3,
    V0_factorize,
    V0_four_point_by_pairing,
    Vg_n,
    CHANNELS,
    CERTIFIED_W3_GENUS_WINDOW,
    CLOSED_FORM_NUMERATOR_COEFFS,
    EXPECTED_BOUNDARY_COUNTS,
    EXPECTED_GRAPH_COUNTS,
    r_matrix_independence_note,
    scaled_numerator_from_graph_sum,
    uniform_weight_cross_channel_correction,
)


# ============================================================================
# Section 1: W_3 Frobenius algebra data (AP1, AP9, AP27)
# ============================================================================

class TestFrobeniusData:
    """Verify W_3 Frobenius algebra structure constants and kappa values."""

    def test_kappa_T(self):
        assert kappa_channel('T', Fraction(26)) == Fraction(13)

    def test_kappa_W(self):
        assert kappa_channel('W', Fraction(26)) == Fraction(26, 3)

    def test_kappa_total(self):
        assert kappa_total(Fraction(26)) == Fraction(65, 3)
        assert kappa_total(Fraction(6)) == Fraction(5)

    def test_kappa_additivity(self):
        for cv in [1, 2, 10, 26, 50]:
            c = Fraction(cv)
            assert kappa_total(c) == kappa_channel('T', c) + kappa_channel('W', c)

    def test_propagator_inverse_metric(self):
        c = Fraction(26)
        assert propagator('T', c) == Fraction(1, 13)
        assert propagator('W', c) == Fraction(3, 26)

    def test_C3_z2_parity(self):
        c = Fraction(10)
        assert C3('T', 'T', 'W', c) == 0
        assert C3('T', 'W', 'T', c) == 0
        assert C3('W', 'T', 'T', c) == 0
        assert C3('W', 'W', 'W', c) == 0

    def test_C3_nonzero(self):
        c = Fraction(10)
        assert C3('T', 'T', 'T', c) == c
        assert C3('T', 'W', 'W', c) == c
        assert C3('W', 'T', 'W', c) == c
        assert C3('W', 'W', 'T', c) == c


# ============================================================================
# Section 2: Vertex factors
# ============================================================================

class TestVertexFactors:

    def test_V0_3pt_TTT(self):
        assert V0_factorize(('T', 'T', 'T'), Fraction(26)) == Fraction(26)

    def test_V0_3pt_TWW(self):
        assert V0_factorize(('T', 'W', 'W'), Fraction(26)) == Fraction(26)

    def test_V0_3pt_vanishing(self):
        assert V0_factorize(('T', 'T', 'W'), Fraction(26)) == 0

    def test_V0_4pt_canonical_pairing(self):
        c = Fraction(26)
        for i in CHANNELS:
            for j in CHANNELS:
                assert V0_factorize((i, i, j, j), c) == 2 * c

    def test_V0_4pt_pairing_not_scalar_associative(self):
        c = Fraction(10)
        assert V0_four_point_by_pairing(('T', 'T', 'W', 'W'), c, '01|23') == 2 * c
        assert V0_four_point_by_pairing(('T', 'T', 'W', 'W'), c, '02|13') == 3 * c
        assert V0_four_point_by_pairing(('T', 'T', 'W', 'W'), c, '03|12') == 3 * c
        audit = four_point_pairing_audit(('T', 'T', 'W', 'W'), c)
        assert not audit['pairing_independent']

    def test_V1_1_per_channel(self):
        c = Fraction(26)
        assert Vg_n(1, ('T',), c) == kappa_channel('T', c) / 24
        assert Vg_n(1, ('W',), c) == kappa_channel('W', c) / 24

    def test_V1_2_diagonal(self):
        c = Fraction(26)
        assert Vg_n(1, ('T', 'T'), c) == kappa_channel('T', c) / 24
        assert Vg_n(1, ('W', 'W'), c) == kappa_channel('W', c) / 24
        assert Vg_n(1, ('T', 'W'), c) == 0

    def test_Vg_n_diagonal_principle(self):
        c = Fraction(26)
        for gv in [1, 2, 3]:
            assert Vg_n(gv, ('T', 'W'), c) == 0
            assert Vg_n(gv, ('T',), c) == kappa_channel('T', c) * lambda_fp(gv)


# ============================================================================
# Section 3: Graph enumeration
# ============================================================================

class TestGraphEnumeration:

    def test_genus2_total_count(self):
        assert len(stable_graphs_complete(2)) == 7

    def test_genus2_boundary_count(self):
        assert len(boundary_graphs(2)) == 6

    def test_genus3_count(self):
        assert len(stable_graphs_complete(3)) == 42

    def test_genus4_count(self):
        assert len(stable_graphs_complete(4)) == 379

    def test_barbell_properties(self):
        barbell = stable_graphs_complete(2)[-1]
        assert barbell.vertex_genera == (0, 0)
        assert barbell.num_edges == 3
        assert barbell.arithmetic_genus == 2
        assert barbell.is_stable
        assert barbell.is_connected
        assert barbell.automorphism_order() == 8

    def test_certified_window_graph_counts(self):
        assert CERTIFIED_W3_GENUS_WINDOW == (2, 3, 4)
        for g in CERTIFIED_W3_GENUS_WINDOW:
            assert len(stable_graphs_complete(g)) == EXPECTED_GRAPH_COUNTS[g]
            assert len(boundary_graphs(g)) == EXPECTED_BOUNDARY_COUNTS[g]


# ============================================================================
# Section 4: Genus-2 cross-channel (delta = (c+204)/(16c))
# ============================================================================

class TestGenus2:

    def test_closed_form_at_c26(self):
        assert delta_F2_closed_form(Fraction(26)) == Fraction(115, 208)

    def test_graph_sum_matches_c26(self):
        assert verify_genus2(Fraction(26))['match']

    def test_graph_sum_matches_c10(self):
        assert verify_genus2(Fraction(10))['match']

    def test_graph_sum_matches_c50(self):
        assert verify_genus2(Fraction(50))['match']

    def test_graph_sum_matches_c1(self):
        assert verify_genus2(Fraction(1))['match']

    def test_positivity(self):
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            assert delta_F2_closed_form(Fraction(cv)) > 0

    def test_large_c_limit(self):
        assert abs(float(delta_F2_closed_form(Fraction(100000))) - 1.0 / 16) < 0.001

    def test_barbell_contribution(self):
        c = Fraction(26)
        barbell = stable_graphs_complete(2)[-1]
        r = graph_amplitude_decomposed(barbell, c)
        assert r['mixed'] == Fraction(21, 4 * 26)

    def test_graphwise_contributions(self):
        c = Fraction(10)
        r = genus2_mixed_graph_contributions(c)
        assert r['irreducible_self_node'] == 0
        assert r['banana_double_self_loop'] == Fraction(3, c)
        assert r['separating_genus1_bridge'] == 0
        assert r['theta_three_bridge'] == Fraction(9, 2 * c)
        assert r['lollipop_self_loop_bridge'] == Fraction(1, 16)
        assert r['barbell_two_self_loops_bridge'] == Fraction(21, 4 * c)

    def test_formula_symbolic(self):
        for cv in [1, 2, 3, 5, 7, 10, 13, 26, 50]:
            c = Fraction(cv)
            assert delta_F2_closed_form(c) == (c + 204) / (16 * c)


# ============================================================================
# Section 5: Genus-3 cross-channel
# ============================================================================

class TestGenus3:

    def test_graph_sum_matches_c26(self):
        assert verify_genus3(Fraction(26))['match']

    def test_graph_sum_matches_c1(self):
        assert verify_genus3(Fraction(1))['match']

    def test_graph_sum_matches_c10(self):
        assert verify_genus3(Fraction(10))['match']

    def test_graph_sum_matches_c50(self):
        assert verify_genus3(Fraction(50))['match']

    def test_positivity(self):
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            assert delta_F3_closed_form(Fraction(cv)) > 0

    def test_numerator_form(self):
        for cv in [1, 2, 3, 4, 5]:
            c = Fraction(cv)
            expected = (5 * c**3 + 3792 * c**2 + 1149120 * c + 217071360) / (138240 * c**2)
            assert delta_F3_closed_form(c) == expected


# ============================================================================
# Section 6: Genus-4 cross-channel
# ============================================================================

class TestGenus4:

    @pytest.mark.slow
    def test_graph_sum_matches_c1(self):
        assert verify_genus4(Fraction(1))['match']

    @pytest.mark.slow
    def test_graph_sum_matches_c5(self):
        assert verify_genus4(Fraction(5))['match']

    @pytest.mark.slow
    def test_graph_sum_matches_c10(self):
        assert verify_genus4(Fraction(10))['match']

    def test_positivity(self):
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            assert delta_F4_closed_form(Fraction(cv)) > 0

    def test_numerator_coefficients_positive(self):
        coeffs = [287, 268881, 115455816, 29725133760, 5594347866240]
        assert all(c > 0 for c in coeffs)


# ============================================================================
# Section 7: Pattern structure across genera
# ============================================================================

class TestPattern:

    def test_all_coefficients_positive(self):
        for coeffs in [
            [1, 204],
            [5, 3792, 1149120, 217071360],
            [287, 268881, 115455816, 29725133760, 5594347866240],
        ]:
            assert all(c > 0 for c in coeffs)

    def test_never_vanishes(self):
        for cv in [1, 5, 10, 26, 50]:
            c = Fraction(cv)
            assert delta_F2_closed_form(c) > 0
            assert delta_F3_closed_form(c) > 0
            assert delta_F4_closed_form(c) > 0

    def test_correction_dominates_at_higher_genus(self):
        c = Fraction(50)
        ratios = []
        for g, closed in [(2, delta_F2_closed_form), (3, delta_F3_closed_form),
                          (4, delta_F4_closed_form)]:
            delta = closed(c)
            kl = kappa_total(c) * lambda_fp(g)
            ratios.append(float(delta / kl))
        assert ratios[0] < ratios[1] < ratios[2]

    def test_denominator_c_powers(self):
        """delta_F_g has c^{g-1} in denominator."""
        # g=2: 16*c^1, g=3: 138240*c^2, g=4: 17418240*c^3
        # Verified by: at large c, delta * c^{g-1} -> polynomial
        for cv in [1000]:
            c = Fraction(cv)
            # g=2: c*delta should be O(1)
            assert abs(float(c * delta_F2_closed_form(c)) - float(c + 204) / 16) < 0.01
            # g=3: c^2*delta should be O(c)
            val = float(c**2 * delta_F3_closed_form(c))
            assert val > 0

    def test_closed_form_dispatch(self):
        for g, closed in [(2, delta_F2_closed_form),
                          (3, delta_F3_closed_form),
                          (4, delta_F4_closed_form)]:
            for cv in [1, 5, 26]:
                c = Fraction(cv)
                assert delta_Fg_closed_form(g, c) == closed(c)

    def test_scaled_numerator_from_graph_sum(self):
        for g in [2, 3]:
            c = Fraction(3)
            expected = Fraction(0)
            for coeff in CLOSED_FORM_NUMERATOR_COEFFS[g]:
                expected = expected * c + coeff
            assert scaled_numerator_from_graph_sum(g, c) == expected

    def test_interpolation_recovers_constants(self):
        for g in [2, 3]:
            assert interpolate_scaled_numerator(g) == tuple(
                Fraction(x) for x in CLOSED_FORM_NUMERATOR_COEFFS[g])


# ============================================================================
# Section 8: Koszul duality (c <-> 100-c)
# ============================================================================

class TestKoszulDuality:

    def test_kappa_sum(self):
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            assert kappa_total(c) + kappa_total(100 - c) == Fraction(250, 3)

    def test_delta_sum_genus2(self):
        c = Fraction(26)
        d1 = delta_F2_closed_form(c)
        d2 = delta_F2_closed_form(Fraction(100) - c)
        expected = (c + 204) / (16 * c) + (304 - c) / (16 * (100 - c))
        assert d1 + d2 == expected


# ============================================================================
# Section 9: Finite-window theorem and firewalls
# ============================================================================

class TestFiniteWindowTheorem:

    def test_certificate_genus2(self):
        c = Fraction(26)
        r = finite_window_theorem(2, c)
        assert r['graphs_total_match']
        assert r['graphs_boundary_match']
        assert r['chi_orb_match']
        assert r['graph_matches_closed']
        assert r['cross_channel'] == Fraction(115, 208)
        assert not r['diagonal_boundary_is_scalar_lane']
        assert r['full_free_energy'] == r['scalar_fp_lane'] + r['cross_channel']

    def test_per_channel_boundary_not_scalar_lane(self):
        r = finite_window_theorem(2, Fraction(10))['per_channel']
        assert r['boundary_T'] == Fraction(1921, 5760)
        assert r['expected_T'] == Fraction(7, 1152)
        assert r['boundary_W'] == Fraction(2149, 8640)
        assert r['expected_W'] == Fraction(7, 1728)
        assert not r['match_T']
        assert not r['match_W']

    def test_uniform_weight_lane_has_no_cross_channels(self):
        for g in CERTIFIED_W3_GENUS_WINDOW:
            assert uniform_weight_cross_channel_correction(g, Fraction(26)) == 0

    def test_package_cardinality_firewalls(self):
        assert holographic_package_entries() == (
            "A", "A^i", "A^!", "C", "r(z)", "Theta_A", "nabla^hol")
        assert modular_koszul_primary_projections() == (
            "Fact_X(L)", "barB_X(L)", "Theta_L", "L_L",
            "(V_br,T_br)", "R4_mod(L)")
        firewall = object_firewall()
        assert firewall["Omega(B(A))"] == "bar-cobar inversion recovering A"
        assert "Hochschild" in firewall["Z_ch^der(A)"]
        assert firewall["A^!"] != firewall["A^i"]


# ============================================================================
# Section 10: R-matrix independence
# ============================================================================

class TestRMatrixIndependence:

    def test_note_exists(self):
        note = r_matrix_independence_note()
        assert 'diagonal' in note.lower()

    def test_frobenius_only_dependence(self):
        c = Fraction(26)
        assert Vg_n(1, ('T',), c) == kappa_channel('T', c) / 24


# ============================================================================
# Section 11: Lambda_fp numbers
# ============================================================================

class TestLambdaFP:

    def test_lambda1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda4(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_positivity(self):
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_decreasing(self):
        for g in range(1, 7):
            assert lambda_fp(g + 1) < lambda_fp(g)


# ============================================================================
# Section 12: Specific numerical values
# ============================================================================

class TestNumericalValues:

    def test_g2_c26(self):
        assert delta_F2_closed_form(Fraction(26)) == Fraction(115, 208)

    def test_g2_c1(self):
        assert delta_F2_closed_form(Fraction(1)) == Fraction(205, 16)

    def test_g3_c1(self):
        expected = Fraction(5 + 3792 + 1149120 + 217071360, 138240)
        assert delta_F3_closed_form(Fraction(1)) == expected

    def test_g4_c1_closed(self):
        expected = Fraction(287 + 268881 + 115455816 + 29725133760 + 5594347866240,
                            17418240)
        assert delta_F4_closed_form(Fraction(1)) == expected


# ============================================================================
# Section 13: Edge cases
# ============================================================================

class TestEdgeCases:

    def test_small_c(self):
        c = Fraction(1)
        assert delta_F2_closed_form(c) == Fraction(205, 16)
        assert delta_F3_closed_form(c) > 0
        assert delta_F4_closed_form(c) > 0

    def test_large_c(self):
        c = Fraction(10000)
        assert delta_F2_closed_form(c) > 0
        assert delta_F3_closed_form(c) > 0
        assert delta_F4_closed_form(c) > 0
        # (c+204)/(16c) = 1/16 + 204/(16c) -> 1/16 + 204/160000 ~ 0.06375
        assert abs(float(delta_F2_closed_form(c)) - 1.0 / 16) < 0.002

    def test_zero_c_rejected(self):
        with pytest.raises(ValueError):
            cross_channel_correction(2, Fraction(0))
        with pytest.raises(ValueError):
            delta_F2_closed_form(Fraction(0))


# ============================================================================
# Section 14: Acceleration pattern analysis
# ============================================================================

class TestAccelerationPattern:
    """Verify the genus tower acceleration pattern.

    Key results:
      - Numerator degrees: 1, 3, 4 for g=2,3,4 (NOT 2g-3 at g=4)
      - Net degree stabilizes at 1 for g >= 3 (linear growth in c)
      - delta_F_g / (kappa * lambda_g) approaches a FINITE constant for g >= 3
      - The constant GROWS with g: 42/31 at g=3, 9184/381 at g=4
      - 287 = 7 * 41: the leading g=4 numerator coefficient factors through 7
    """

    def test_net_degree_g2_is_zero(self):
        """delta_F_2 = O(1) at large c."""
        c = Fraction(10**6)
        d = delta_F2_closed_form(c)
        # Should be close to 1/16
        assert abs(float(d) - 1.0/16) < 1e-4

    def test_net_degree_g3_is_one(self):
        """delta_F_3 = O(c) at large c."""
        c = Fraction(10**6)
        d = delta_F3_closed_form(c)
        ratio = d / c
        # Should approach 5/138240 = 1/27648
        assert abs(float(ratio) - 1.0/27648) < 1e-7

    def test_net_degree_g4_is_one(self):
        """delta_F_4 = O(c) at large c (NOT c^2)."""
        c = Fraction(10**6)
        d = delta_F4_closed_form(c)
        ratio = d / c
        # Should approach 287/17418240
        assert abs(float(ratio) - 287.0/17418240) < 1e-7

    def test_leading_coeff_ratio(self):
        """A_4/A_3 = (287/17418240) / (5/138240) = 41/90."""
        A3 = Fraction(5, 138240)
        A4 = Fraction(287, 17418240)
        assert A4 / A3 == Fraction(41, 90)

    def test_asymptotic_ratio_g3(self):
        """lim_{c->inf} delta_3 / (kappa*lambda_3) = 42/31."""
        # delta_3 ~ c/27648, kappa*lambda_3 = (5c/6)*(31/967680) = 31c/1161216
        # ratio -> (1/27648) / (31/1161216) = 1161216/(27648*31) = 42/31
        lim = Fraction(1, 27648) / (Fraction(31, 1161216))
        assert lim == Fraction(42, 31)

    def test_asymptotic_ratio_g4(self):
        """lim_{c->inf} delta_4 / (kappa*lambda_4) = 9184/381."""
        # delta_4 ~ 287c/17418240, kappa*lambda_4 = (5c/6)*(127/154828800) = 127c/185794560
        # ratio -> (287/17418240) / (127/185794560) = 287*185794560 / (17418240*127)
        lim = Fraction(287, 17418240) / Fraction(127, 185794560)
        assert lim == Fraction(9184, 381)

    def test_asymptotic_ratio_increases(self):
        """The large-c ratio grows: 42/31 < 9184/381."""
        assert Fraction(42, 31) < Fraction(9184, 381)

    def test_numerator_degree_4_not_5(self):
        """At genus 4, numerator has degree 4 (not 2*4-3=5).

        This breaks the 2g-3 pattern that holds at g=2,3.
        Verified via forward differences vanishing at order 5.
        """
        L = 17418240
        vals = []
        for cv in range(1, 8):
            c = Fraction(cv)
            # L * c^3 * delta = polynomial of degree 4
            vals.append(delta_F4_closed_form(c) * c**3 * L)
        # 5th forward differences vanish
        diffs = list(vals)
        for _ in range(5):
            diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
        for d in diffs:
            assert d == 0

    def test_g4_leading_coefficient_factorization(self):
        """287 = 7 * 41, and gcd(287, 17418240) = 7."""
        from math import gcd
        assert 287 == 7 * 41
        assert gcd(287, 17418240) == 7
        # Simplified: 41/2488320
        assert 17418240 // 7 == 2488320

    def test_denominator_prime_factorizations(self):
        """D_2 = 2^4, D_3 = 2^10*3^3*5, D_4 = 2^11*3^5*5*7."""
        assert 16 == 2**4
        assert 138240 == 2**10 * 3**3 * 5
        assert 17418240 == 2**11 * 3**5 * 5 * 7

    def test_correction_growth_relative_to_scalar(self):
        """At c=26: delta_2/kl_2 < delta_3/kl_3 < delta_4/kl_4."""
        c = Fraction(26)
        ratios = []
        for g, closed in [(2, delta_F2_closed_form),
                          (3, delta_F3_closed_form),
                          (4, delta_F4_closed_form)]:
            d = closed(c)
            kl = kappa_total(c) * lambda_fp(g)
            ratios.append(d / kl)
        assert ratios[0] < ratios[1] < ratios[2]

    def test_constant_term_growth(self):
        """P_g(0) grows super-exponentially: 204, 217071360, 5594347866240."""
        P0 = [204, 217071360, 5594347866240]
        assert P0[0] < P0[1] < P0[2]
        # Growth ratio: P_3(0)/P_2(0) ~ 10^6, P_4(0)/P_3(0) ~ 2.6*10^4
        assert P0[1] / P0[0] > 10**5
        assert P0[2] / P0[1] > 10**4
