"""Tests for compute/lib/genus3_f3_stable_graph_engine.py.

Multi-path verification of F_3(Vir_c) = (c/2) * 31/967680 from the 42
stable graphs at (g=3, n=0).
"""

from fractions import Fraction

import pytest

from compute.lib.genus3_f3_stable_graph_engine import (
    CHI_ORB_MBAR3,
    GRAPH_COUNT_G3,
    LAMBDA3_FP,
    UNIFORM_WEIGHT_TAG,
    VIRASORO_F3_OVER_C,
    VIRASORO_KAPPA_OVER_C,
    GraphContribution,
    chi_orb_mbar3_from_graphs,
    genus3_stable_graphs,
    graph_contributions_chi_orb,
    lambda3_fp_ahat,
    lambda3_fp_bernoulli,
    lambda_fp_table,
    spectral_decomposition,
    verify_f3_genus3,
    virasoro_f3,
    virasoro_kappa,
)


class TestGraphEnumeration:
    """Tests for the 42 stable graphs at (g=3, n=0)."""

    def test_graph_count_is_42(self):
        # VERIFIED: [LT] Faber (1999) census of stable graphs at g=3
        # VERIFIED: [DC] stable_graph_enumeration.py general enumerator
        assert len(genus3_stable_graphs()) == 42

    def test_all_graphs_have_genus_3(self):
        for G in genus3_stable_graphs():
            assert G.arithmetic_genus == 3

    def test_all_graphs_are_stable(self):
        for G in genus3_stable_graphs():
            assert G.is_stable

    def test_all_graphs_are_connected(self):
        for G in genus3_stable_graphs():
            assert G.is_connected

    def test_smooth_graph_exists(self):
        """Exactly one smooth graph: 1 vertex, genus 3, no edges."""
        smooth = [G for G in genus3_stable_graphs()
                  if G.vertex_genera == (3,) and G.num_edges == 0]
        assert len(smooth) == 1

    def test_max_edges_is_6(self):
        """Maximum edge count at (g=3, n=0) is 3g-3 = 6."""
        max_e = max(G.num_edges for G in genus3_stable_graphs())
        # VERIFIED: [DA] dim M-bar_3 = 3*3-3 = 6
        # VERIFIED: [DC] trivalent graphs have 6 edges
        assert max_e == 6


class TestSpectralDecomposition:
    """Tests for the loop-number decomposition of the 42 graphs."""

    def test_spectral_counts(self):
        spectral = spectral_decomposition()
        # VERIFIED: [DC] direct enumeration from stable_graph_enumeration.py
        # VERIFIED: [LT] Faber (1999) Table 2
        expected = {0: 4, 1: 9, 2: 14, 3: 15}
        actual = {h1: d['count'] for h1, d in spectral.items()}
        assert actual == expected
        assert sum(expected.values()) == 42

    def test_spectral_sum_is_chi_orb(self):
        spectral = spectral_decomposition()
        total = sum(d['chi_sum'] for d in spectral.values())
        assert total == CHI_ORB_MBAR3


class TestLambda3FP:
    """Tests for lambda_3^FP = 31/967680 via independent paths."""

    def test_bernoulli_formula(self):
        # VERIFIED: [DC] (2^5-1)|B_6|/(2^5 * 6!) = 31*(1/42)/(32*720)
        # VERIFIED: [LT] Faber-Pandharipande (2003), Table 1
        assert lambda3_fp_bernoulli() == Fraction(31, 967680)

    def test_ahat_generating_function(self):
        # VERIFIED: [DC] coeff of t^6 in (t/2)/sin(t/2) - 1
        # VERIFIED: [CF] matches Bernoulli path
        assert lambda3_fp_ahat() == Fraction(31, 967680)

    def test_two_paths_agree(self):
        assert lambda3_fp_bernoulli() == lambda3_fp_ahat()


class TestChiOrbMbar3:
    """Tests for chi^orb(M-bar_3) from the 42-graph vertex-product sum."""

    def test_chi_orb_exact_value(self):
        # VERIFIED: [DC] 42-graph vertex-product sum
        # VERIFIED: [LT] Bini-Harer (2011), Table of chi^orb values
        assert chi_orb_mbar3_from_graphs() == Fraction(-12419, 90720)

    def test_all_42_graphs_contribute(self):
        contribs = graph_contributions_chi_orb()
        assert len(contribs) == 42

    def test_smooth_graph_contribution(self):
        """The smooth graph contributes chi^orb(M_3) = B_6/(4*3*2) = 1/1008."""
        contribs = graph_contributions_chi_orb()
        smooth = [c for c in contribs
                  if c.vertex_genera == (3,) and c.num_edges == 0]
        assert len(smooth) == 1
        # VERIFIED: [DC] chi^orb(M_3) = B_6/(4*3*2) = (1/42)/24 = 1/1008
        # VERIFIED: [LT] Harer-Zagier (1986)
        assert smooth[0].weighted_contribution == Fraction(1, 1008)

    def test_trivalent_graphs_count(self):
        """5 trivalent (all genus-0) graphs at h^1=3, all with val=(3,3,3,3)."""
        contribs = graph_contributions_chi_orb()
        trivalent = [c for c in contribs
                     if all(v == 3 for v in c.valences)
                     and all(g == 0 for g in c.vertex_genera)]
        assert len(trivalent) == 5

    def test_aut_orders_positive(self):
        for c in graph_contributions_chi_orb():
            assert c.aut_order >= 1


class TestCrossGenusConsistency:
    """Tests for lambda_g^FP at g=1,2,3 from the same framework."""

    def test_lambda1_fp(self):
        # VERIFIED: [DC] (2^1-1)|B_2|/(2^1 * 2!) = (1/6)/4 = 1/24
        # VERIFIED: [LT] Mumford (1983)
        table = lambda_fp_table()
        assert table[1] == Fraction(1, 24)

    def test_lambda2_fp(self):
        # VERIFIED: [DC] (2^3-1)|B_4|/(2^3 * 4!) = 7*(1/30)/(8*24) = 7/5760
        # VERIFIED: [LT] Faber-Pandharipande (1998) + Getzler (1998)
        table = lambda_fp_table()
        assert table[2] == Fraction(7, 5760)

    def test_lambda3_fp(self):
        # VERIFIED: [DC] Bernoulli formula
        # VERIFIED: [CF] A-hat generating function
        table = lambda_fp_table()
        assert table[3] == Fraction(31, 967680)

    def test_ratio_growth(self):
        """lambda_{g+1}/lambda_g grows like (2g+1)(2g)/(4 pi^2)."""
        table = lambda_fp_table()
        ratio_12 = table[2] / table[1]
        ratio_23 = table[3] / table[2]
        # VERIFIED: [DC] ratio_12 = (7/5760)/(1/24) = 7/240
        # VERIFIED: [DA] expected ~ 3*2/(4*pi^2) ~ 0.152, actual = 7/240 ~ 0.029
        #   (small g, asymptotic not yet accurate)
        assert ratio_12 == Fraction(7, 240)
        assert ratio_23 == Fraction(31 * 5760, 967680 * 7)


class TestVirasoroF3:
    """Tests for F_3(Vir_c) = (c/2) * 31/967680."""

    def test_kappa_virasoro(self):
        # VERIFIED: [LT] landscape_census.tex C2: kappa(Vir_c) = c/2
        # VERIFIED: [CF] W_2 = Vir, kappa(W_2) = c*(H_2-1) = c/2
        assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)
        assert virasoro_kappa(Fraction(0)) == Fraction(0)
        assert virasoro_kappa(Fraction(26)) == Fraction(13)

    def test_f3_at_c0(self):
        # VERIFIED: [LC] kappa(Vir_0) = 0 forces F_3 = 0
        # VERIFIED: [DC] 0 * lambda_3^FP = 0
        assert virasoro_f3(Fraction(0)) == Fraction(0)

    def test_f3_at_c1(self):
        # VERIFIED: [DC] (1/2) * 31/967680 = 31/1935360
        # VERIFIED: [CF] matches VIRASORO_F3_OVER_C constant
        assert virasoro_f3(Fraction(1)) == Fraction(31, 1935360)

    def test_f3_at_c13(self):
        """c=13 is the Virasoro self-dual point."""
        # VERIFIED: [DC] (13/2) * 31/967680 = 403/1935360
        # VERIFIED: [LT] c=13 is self-dual (C8)
        assert virasoro_f3(Fraction(13)) == Fraction(13, 2) * LAMBDA3_FP

    def test_f3_at_c26(self):
        # VERIFIED: [DC] 13 * 31/967680 = 403/967680
        # VERIFIED: [LC] c=26 is the string ghost cancellation point
        assert virasoro_f3(Fraction(26)) == Fraction(13 * 31, 967680)

    def test_f3_linearity_in_c(self):
        """F_3 is linear in c (consequence of uniform-weight scalar lane)."""
        for c_val in [Fraction(1), Fraction(7), Fraction(13), Fraction(26)]:
            assert virasoro_f3(c_val) == c_val * VIRASORO_F3_OVER_C


class TestComprehensiveVerification:
    """Tests for the full multi-path verification summary."""

    def test_all_paths_consistent(self):
        result = verify_f3_genus3()
        assert result['all_paths_consistent']

    def test_graph_count_in_summary(self):
        result = verify_f3_genus3()
        assert result['graph_count'] == 42
        assert result['graph_count_match']

    def test_bernoulli_in_summary(self):
        result = verify_f3_genus3()
        assert result['lambda3_bernoulli'] == LAMBDA3_FP
        assert result['lambda3_bernoulli_match']

    def test_ahat_in_summary(self):
        result = verify_f3_genus3()
        assert result['lambda3_ahat'] == LAMBDA3_FP
        assert result['lambda3_ahat_match']

    def test_chi_orb_in_summary(self):
        result = verify_f3_genus3()
        assert result['chi_orb_mbar3'] == CHI_ORB_MBAR3
        assert result['chi_orb_match']

    def test_spectral_counts_in_summary(self):
        result = verify_f3_genus3()
        assert result['spectral_counts'] == {0: 4, 1: 9, 2: 14, 3: 15}
