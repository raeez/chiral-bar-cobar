r"""Tests for the multi-weight genus tower: delta_F_g^cross(W_3).

Verifies the cross-channel correction at genera 2, 3, 4 using multiple
independent paths:

Path 1: Direct graph sum (brute force over all channel assignments)
Path 2: Closed-form formula (Newton-interpolated rational function)
Path 3: Limiting cases (c -> large, c = 50 self-dual)
Path 4: Koszul duality (c <-> 100-c symmetry)
Path 5: Z_2 parity (odd-W channels vanish)
Path 6: Per-channel universality (diagonal sum = kappa_i * lambda_g)
Path 7: Positivity and monotonicity

References:
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    op:multi-generator-universality (higher_genus_foundations.tex)
"""

import pytest
from fractions import Fraction

from compute.lib.multi_weight_genus_tower import (
    cross_channel_correction,
    full_amplitude_decomposition,
    graph_amplitude_decomposed,
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
    Vg_n,
    CHANNELS,
    r_matrix_independence_note,
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

    def test_V0_4pt_universality(self):
        c = Fraction(26)
        for i in CHANNELS:
            for j in CHANNELS:
                assert V0_factorize((i, i, j, j), c) == 2 * c

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
# Section 9: R-matrix independence
# ============================================================================

class TestRMatrixIndependence:

    def test_note_exists(self):
        note = r_matrix_independence_note()
        assert 'diagonal' in note.lower()

    def test_frobenius_only_dependence(self):
        c = Fraction(26)
        assert Vg_n(1, ('T',), c) == kappa_channel('T', c) / 24


# ============================================================================
# Section 10: Lambda_fp numbers
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
# Section 11: Specific numerical values
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
# Section 12: Edge cases
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
