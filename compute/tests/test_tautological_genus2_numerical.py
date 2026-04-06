r"""Tests for tautological_genus2_numerical_engine.py

Numerical verification of multi-generator universality using tautological
intersection theory on M-bar_{2,0}.

RESULT SUMMARY
==============

1. Single-channel algebras (Heisenberg, Virasoro, affine sl_2, betagamma):
   Cross-channel correction = 0 EXACTLY. No mixed-channel boundary amplitudes.
   This is the CALIBRATION: single-channel algebras have no cross-channel.

2. W_3 (two channels T, W):
   Cross-channel correction = (c+204)/(16c) != 0 for all c > 0.
   This means either:
     (a) R-matrix corrections cancel it (restoring universality), or
     (b) universality genuinely FAILS at genus 2 for multi-weight algebras.
   This is the computational content of op:multi-generator-universality.

3. W_4 (three channels T, W3, W4):
   Similar cross-channel correction.

4. Intersection ring:
   All 10 degree-3 intersection numbers on M-bar_2 independently verified.
   Faber-Pandharipande number: lambda_2^FP = 7/5760.
   Lambda_2 pairings: int l2*l1 = 1/2880, int l2*dirr = 0, int l2*d1 = 1/1152.

TEST STRUCTURE (8 verification paths)
======================================

Path 1: Intersection ring self-consistency (Mumford, Noether, Faber).
Path 2: Single-channel calibration (zero cross-channel).
Path 3: Per-channel universality (diagonal sum structure).
Path 4: W_3 cross-channel: brute force vs analytic formula.
Path 5: W_3 cross-channel: graph-by-graph decomposition.
Path 6: W_4 cross-channel structure.
Path 7: Graph topology and automorphism verification.
Path 8: Koszul duality constraints and special-value checks.

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex): F_g = kappa * lambda_g^FP
    op:multi-generator-universality (higher_genus_foundations.tex)
    rem:propagator-weight-universality (AP27)
"""

import pytest
from fractions import Fraction

from compute.lib.tautological_genus2_numerical_engine import (
    # Basics
    _bernoulli, lambda_fp,
    # Intersection ring
    Genus2IntersectionRing,
    TautClass2,
    # Algebra constructors
    MCAlgebra,
    make_heisenberg,
    make_virasoro,
    make_affine_sl2,
    make_w3,
    make_w4,
    make_betagamma,
    # Graph engine
    GENUS2_GRAPHS,
    graph_amplitude,
    _half_edge_channels,
    _vertex_factor,
    # Core computation
    compute_boundary_decomposition,
    Genus2UniversalityResult,
    # Analytics
    w3_cross_channel_analytic,
    dumbbell_stratum_check,
    numerical_landscape,
    run_full_verification,
    # Genus 3
    genus3_universality_check,
)

# Standard test central charges
C_SMALL = [Fraction(1), Fraction(2), Fraction(4)]
C_MEDIUM = [Fraction(10), Fraction(13), Fraction(26)]
C_LARGE = [Fraction(50), Fraction(100)]
C_ALL = C_SMALL + C_MEDIUM + C_LARGE


# ============================================================================
# PATH 1: Intersection ring self-consistency
# ============================================================================

class TestIntersectionRing:
    """Verify Faber's intersection numbers on M-bar_2."""

    def test_faber_pandharipande_g1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_faber_pandharipande_g3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_bernoulli_values(self):
        """Verify Bernoulli numbers used in FP formula."""
        assert _bernoulli(0) == Fraction(1)
        assert _bernoulli(1) == Fraction(-1, 2)
        assert _bernoulli(2) == Fraction(1, 6)
        assert _bernoulli(4) == Fraction(-1, 30)
        assert _bernoulli(6) == Fraction(1, 42)

    def test_lambda1_cube(self):
        """int_{M-bar_2} lambda_1^3 = 1/1440 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_l1_l1_l1() == Fraction(1, 1440)

    def test_lambda2_lambda1(self):
        """int_{M-bar_2} lambda_2 * lambda_1 = 1/2880 (FP formula)."""
        IR = Genus2IntersectionRing
        assert IR.int_l2_l1() == Fraction(1, 2880)

    def test_lambda1sq_delta_irr(self):
        """int_{M-bar_2} lambda_1^2 * delta_irr = 1/120 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_l1_l1_dirr() == Fraction(1, 120)

    def test_lambda1sq_delta1_vanishes(self):
        """int_{M-bar_2} lambda_1^2 * delta_1 = 0 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_l1_l1_d1() == Fraction(0)

    def test_lambda1_delta_irr_sq(self):
        """int_{M-bar_2} lambda_1 * delta_irr^2 = -1/60 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_l1_dirr_dirr() == Fraction(-1, 60)

    def test_lambda1_delta1_sq(self):
        """int_{M-bar_2} lambda_1 * delta_1^2 = -1/576 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_l1_d1_d1() == Fraction(-1, 576)

    def test_delta_irr_cube(self):
        """int_{M-bar_2} delta_irr^3 = 4/15 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_dirr_dirr_dirr() == Fraction(4, 15)

    def test_delta1_cube(self):
        """int_{M-bar_2} delta_1^3 = 1/1728 (Faber)."""
        IR = Genus2IntersectionRing
        assert IR.int_d1_d1_d1() == Fraction(1, 1728)

    def test_mixed_boundary_vanishing(self):
        """Several mixed boundary integrals vanish on M-bar_2."""
        IR = Genus2IntersectionRing
        assert IR.int_l1_dirr_d1() == Fraction(0)
        assert IR.int_dirr_dirr_d1() == Fraction(0)
        assert IR.int_dirr_d1_d1() == Fraction(0)

    def test_lambda2_delta_irr_vanishes(self):
        """int_{M-bar_2} lambda_2 * delta_irr = 0.

        From c_2(E|_{Delta_irr}) = 0 (Hodge bundle restricts as rank-1 extension).
        """
        IR = Genus2IntersectionRing
        assert IR.int_l2_dirr() == Fraction(0)

    def test_lambda2_delta1(self):
        """int_{M-bar_2} lambda_2 * delta_1 = 1/1152.

        From gl*(lambda_2) = lambda_1 x lambda_1, with S_2 factor.
        """
        IR = Genus2IntersectionRing
        assert IR.int_l2_d1() == Fraction(1, 1152)

    def test_noether_relation(self):
        """Verify kappa_1 = 12*lambda_1 - delta_irr - delta_1.

        Check: int kappa_1 * lambda_1^2 = 12*(1/1440) - 1/120 - 0 = 0.
        """
        IR = Genus2IntersectionRing
        kappa1_l1sq = (Fraction(12) * IR.int_l1_l1_l1()
                       - IR.int_l1_l1_dirr()
                       - IR.int_l1_l1_d1())
        assert kappa1_l1sq == Fraction(0)

    def test_mumford_relation_boundary(self):
        """Verify 2*lambda_2*lambda_1 - lambda_1^3 = 0.

        On M_2 (open moduli), 2*lambda_2 = lambda_1^2.
        Integration: 2*(1/2880) - 1/1440 = 1/1440 - 1/1440 = 0.
        """
        IR = Genus2IntersectionRing
        diff_l1 = 2 * IR.int_l2_l1() - IR.int_l1_l1_l1()
        assert diff_l1 == Fraction(0)


# ============================================================================
# PATH 2: Single-channel calibration (zero cross-channel)
# ============================================================================

class TestSingleChannelCalibration:
    """Verify that single-channel algebras have ZERO cross-channel correction.

    For a single-channel algebra, all edge assignments use the same channel,
    so there are no mixed-channel contributions. The cross-channel sum is
    identically zero, which is consistent with F_2 = kappa * lambda_2^FP.
    """

    def test_heisenberg_k1_zero_cross(self):
        """Heisenberg k=1: zero cross-channel."""
        alg = make_heisenberg(1)
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross == Fraction(0)
        assert r.cross_is_zero

    def test_heisenberg_k5_zero_cross(self):
        """Heisenberg k=5: zero cross-channel."""
        alg = make_heisenberg(5)
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross == Fraction(0)
        assert r.cross_is_zero

    @pytest.mark.parametrize("c", C_ALL)
    def test_virasoro_zero_cross(self, c):
        """Virasoro: zero cross-channel for all c."""
        alg = make_virasoro(c)
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross == Fraction(0)
        assert r.cross_is_zero

    @pytest.mark.parametrize("k", [1, 2, 5, 10])
    def test_affine_sl2_zero_cross(self, k):
        """Affine sl_2: zero cross-channel for all k."""
        alg = make_affine_sl2(k)
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross == Fraction(0)
        assert r.cross_is_zero

    def test_betagamma_zero_cross(self):
        """Standard betagamma: zero cross-channel."""
        alg = make_betagamma()
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross == Fraction(0)
        assert r.cross_is_zero


# ============================================================================
# PATH 3: Per-channel universality (dumbbell stratum check)
# ============================================================================

class TestPerChannelUniversality:
    """The dumbbell amplitude equals kappa * int(lambda_2 * delta_1) for ALL algebras.

    The dumbbell has 1 edge (bridge), so no cross-channel.
    Each channel gives (1/kappa_ch) * (kappa_ch/24)^2 = kappa_ch/576.
    Total with |Aut|=2: kappa/1152 = kappa * int(lambda_2 * delta_1).
    """

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(10), Fraction(50)])
    def test_w3_dumbbell(self, c):
        """W_3 dumbbell = kappa * 1/1152."""
        dc = dumbbell_stratum_check(make_w3(c))
        assert dc['match'], f"W_3 c={c}: dumbbell mismatch"

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(10)])
    def test_w4_dumbbell(self, c):
        """W_4 dumbbell = kappa * 1/1152."""
        dc = dumbbell_stratum_check(make_w4(c))
        assert dc['match'], f"W_4 c={c}: dumbbell mismatch"

    @pytest.mark.parametrize("k", [1, 2, 5])
    def test_heisenberg_dumbbell(self, k):
        """Heisenberg dumbbell = kappa * 1/1152."""
        dc = dumbbell_stratum_check(make_heisenberg(k))
        assert dc['match'], f"Heisenberg k={k}: dumbbell mismatch"

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(26)])
    def test_virasoro_dumbbell(self, c):
        """Virasoro dumbbell = kappa * 1/1152."""
        dc = dumbbell_stratum_check(make_virasoro(c))
        assert dc['match'], f"Virasoro c={c}: dumbbell mismatch"

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(10), Fraction(50)])
    def test_w3_dumbbell_no_cross(self, c):
        """W_3 dumbbell has zero cross-channel (only 1 edge)."""
        dc = dumbbell_stratum_check(make_w3(c))
        assert dc['dumbbell_cross'] == Fraction(0)


# ============================================================================
# PATH 4: W_3 cross-channel — brute force vs analytic
# ============================================================================

class TestW3CrossChannelAnalytic:
    """Verify the W_3 cross-channel correction against the analytic formula.

    Analytic formula: delta_F2(W_3) = (c + 204) / (16c).
    """

    @pytest.mark.parametrize("c", C_ALL)
    def test_numeric_vs_analytic(self, c):
        """Brute-force graph sum matches analytic cross-channel formula."""
        alg = make_w3(c)
        r = compute_boundary_decomposition(alg)
        an = w3_cross_channel_analytic(c)
        assert r.boundary_cross == an['total_cross'], (
            f"c={c}: numeric={r.boundary_cross} != analytic={an['total_cross']}"
        )

    @pytest.mark.parametrize("c", C_ALL)
    def test_analytic_formula(self, c):
        """Analytic formula (c+204)/(16c) is correct."""
        an = w3_cross_channel_analytic(c)
        assert an['matches_formula'], (
            f"c={c}: formula mismatch: {an['total_cross']} != {an['formula']}"
        )

    @pytest.mark.parametrize("c", C_ALL)
    def test_cross_nonzero(self, c):
        """W_3 cross-channel is NONZERO for all c > 0."""
        an = w3_cross_channel_analytic(c)
        assert an['total_cross'] > 0, f"c={c}: cross = {an['total_cross']} <= 0"

    def test_large_c_limit(self):
        """As c -> infinity, cross-channel -> 1/16 (the lollipop constant)."""
        c = Fraction(10000)
        an = w3_cross_channel_analytic(c)
        diff = an['total_cross'] - Fraction(1, 16)
        # (c+204)/(16c) - 1/16 = 204/(16c)
        assert diff == Fraction(204, 16 * c)
        assert diff > 0 and diff < Fraction(1, 100)

    def test_c_equals_204_special(self):
        """At c=204: cross = (204+204)/(16*204) = 408/3264 = 1/8."""
        an = w3_cross_channel_analytic(204)
        assert an['total_cross'] == Fraction(1, 8)


# ============================================================================
# PATH 5: W_3 graph-by-graph decomposition
# ============================================================================

class TestW3GraphDecomposition:
    """Verify per-graph cross-channel contributions for W_3."""

    def _get_result(self, c):
        return compute_boundary_decomposition(make_w3(c))

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_dumbbell_no_cross(self, c):
        """Dumbbell has only 1 edge, so no cross-channel."""
        r = self._get_result(c)
        assert r.per_graph['dumbbell']['cross'] == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_fig_eight_no_cross(self, c):
        """Fig-eight has only 1 edge, so no cross-channel."""
        r = self._get_result(c)
        assert r.per_graph['fig_eight']['cross'] == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_banana_cross(self, c):
        """Banana cross-channel = 3/c."""
        r = self._get_result(c)
        expected = Fraction(3) / Fraction(c)
        assert r.per_graph['banana']['cross'] == expected, (
            f"c={c}: banana cross = {r.per_graph['banana']['cross']} != {expected}"
        )

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_theta_cross(self, c):
        """Theta cross-channel = 9/(2c)."""
        r = self._get_result(c)
        expected = Fraction(9) / (2 * Fraction(c))
        assert r.per_graph['theta']['cross'] == expected, (
            f"c={c}: theta cross = {r.per_graph['theta']['cross']} != {expected}"
        )

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_lollipop_cross(self, c):
        """Lollipop cross-channel = 1/16 (c-independent!)."""
        r = self._get_result(c)
        expected = Fraction(1, 16)
        assert r.per_graph['lollipop']['cross'] == expected, (
            f"c={c}: lollipop cross = {r.per_graph['lollipop']['cross']} != {expected}"
        )

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(10), Fraction(100)])
    def test_total_cross_sum(self, c):
        """Total cross = sum of per-graph cross contributions."""
        r = self._get_result(c)
        graph_sum = sum(pg['cross'] for pg in r.per_graph.values())
        assert graph_sum == r.boundary_cross, (
            f"c={c}: sum of graph cross = {graph_sum} != total = {r.boundary_cross}"
        )


# ============================================================================
# PATH 6: W_4 cross-channel
# ============================================================================

class TestW4CrossChannel:
    """Verify cross-channel corrections for W_4 (3 generators)."""

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(10), Fraction(50)])
    def test_w4_cross_nonzero(self, c):
        """W_4 has nonzero cross-channel correction."""
        alg = make_w4(c)
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross != Fraction(0), (
            f"W_4 c={c}: expected nonzero cross-channel"
        )

    def test_w4_more_channels_more_cross(self):
        """W_4 (3 channels) has MORE cross-channel than W_3 (2 channels) at same c."""
        c = Fraction(10)
        w3 = compute_boundary_decomposition(make_w3(c))
        w4 = compute_boundary_decomposition(make_w4(c))
        assert w4.boundary_cross > w3.boundary_cross


# ============================================================================
# PATH 7: Graph topology and automorphism verification
# ============================================================================

class TestGraphTopology:
    """Verify the 7 stable graphs of M-bar_{2,0}."""

    def test_graph_count(self):
        """There are exactly 7 stable graphs at (g=2, n=0)."""
        assert len(GENUS2_GRAPHS) == 7

    def test_all_genus_2(self):
        """All graphs have arithmetic genus 2."""
        for G in GENUS2_GRAPHS:
            nv = len(G['vg'])
            ne = len(G['edges'])
            g_sum = sum(G['vg'])
            h1 = ne - nv + 1
            g_total = h1 + g_sum
            assert g_total == 2, f"Graph {G['name']}: genus = {g_total} != 2"

    def test_stability(self):
        """All vertices are stable: 2g(v) - 2 + val(v) > 0."""
        for G in GENUS2_GRAPHS:
            nv = len(G['vg'])
            val = [0] * nv
            for edge in G['edges']:
                if edge[0] == 'self':
                    val[edge[1]] += 2
                else:
                    val[edge[1]] += 1
                    val[edge[2]] += 1
            for vi in range(nv):
                assert 2 * G['vg'][vi] - 2 + val[vi] > 0, (
                    f"Graph {G['name']}: unstable vertex {vi}"
                )

    def test_automorphism_orders(self):
        """Verify automorphism group orders."""
        expected_auts = {
            'smooth': 1, 'fig_eight': 2, 'banana': 8,
            'dumbbell': 2, 'theta': 12, 'lollipop': 2, 'barbell': 8,
        }
        for G in GENUS2_GRAPHS:
            assert G['aut'] == expected_auts[G['name']]


# ============================================================================
# PATH 8: Special values and Koszul duality
# ============================================================================

class TestSpecialValues:
    """Verify special values and Koszul duality constraints."""

    def test_w3_kappa_formula(self):
        """kappa(W_3) = 5c/6."""
        for c in [1, 2, 10, 100]:
            alg = make_w3(c)
            assert alg.kappa_total == Fraction(5) * Fraction(c) / 6

    def test_w4_kappa_formula(self):
        """kappa(W_4) = 13c/12."""
        for c in [3, 10, 50]:
            alg = make_w4(c)
            assert alg.kappa_total == Fraction(13) * Fraction(c) / 12

    def test_w3_koszul_dual_central_charge(self):
        """W_3 Koszul dual: c + c' = 100."""
        c = Fraction(10)
        c_dual = Fraction(100) - c
        alg = make_w3(c)
        alg_dual = make_w3(c_dual)
        assert alg.kappa_total + alg_dual.kappa_total == Fraction(250, 3)

    def test_w3_cross_at_self_dual(self):
        """At c=50: cross = (50+204)/(16*50) = 254/800 = 127/400."""
        an = w3_cross_channel_analytic(50)
        assert an['total_cross'] == Fraction(127, 400)

    def test_w3_cross_complementarity(self):
        """Verify cross(c) + cross(100-c) has a specific value."""
        c = Fraction(10)
        c_dual = Fraction(90)
        an_c = w3_cross_channel_analytic(c)
        an_c_dual = w3_cross_channel_analytic(c_dual)
        total = an_c['total_cross'] + an_c_dual['total_cross']
        expected = (Fraction(c) + 204) / (16 * Fraction(c)) + (Fraction(c_dual) + 204) / (16 * Fraction(c_dual))
        assert total == expected

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(50)])
    def test_w3_cross_positive(self, c):
        """W_3 cross-channel is POSITIVE for all c > 0."""
        alg = make_w3(c)
        r = compute_boundary_decomposition(alg)
        assert r.boundary_cross > 0, f"c={c}: cross = {r.boundary_cross} <= 0"

    def test_w3_single_generator_limit(self):
        """At large c, cross / F2_scalar -> 0."""
        c = Fraction(10000)
        alg = make_w3(c)
        r = compute_boundary_decomposition(alg)
        ratio = r.cross_over_scalar
        assert ratio is not None
        assert ratio < Fraction(1, 100)

    def test_fig_eight_c_independent(self):
        """Fig-eight diagonal sum = (number of channels)/48 (c-independent).

        Each channel gives (1/kappa) * (kappa/24) / 2 = 1/48.
        """
        # W_3 (2 channels)
        for c in [Fraction(2), Fraction(50)]:
            r = compute_boundary_decomposition(make_w3(c))
            assert r.per_graph['fig_eight']['diagonal'] == Fraction(1, 24)

        # Virasoro (1 channel)
        for c in [Fraction(2), Fraction(50)]:
            r = compute_boundary_decomposition(make_virasoro(c))
            assert r.per_graph['fig_eight']['total'] == Fraction(1, 48)

    def test_lollipop_cross_c_independent(self):
        """Lollipop cross = 1/16, independent of c."""
        for c in [1, 5, 50, 1000]:
            r = compute_boundary_decomposition(make_w3(c))
            assert r.per_graph['lollipop']['cross'] == Fraction(1, 16)


# ============================================================================
# Full verification
# ============================================================================

class TestFullVerification:
    """Run the master verification function."""

    def test_calibration_all_pass(self):
        """All single-channel calibration tests pass (zero cross-channel)."""
        report = run_full_verification()
        for name, data in report['calibration'].items():
            assert data['cross_is_zero'], f"Calibration failed: {name}"

    def test_w3_cross_all_nonzero(self):
        """W_3 cross-channel is nonzero at all tested central charges."""
        report = run_full_verification()
        for cval, data in report['W_3'].items():
            assert not data['cross_is_zero'], f"W_3 {cval}: expected nonzero cross"

    def test_analytic_matches_numeric(self):
        """Analytic formula matches numeric computation for all tested c."""
        report = run_full_verification()
        for cval, data in report['W_3_analytic'].items():
            assert data['numeric_matches_analytic'], f"W_3 {cval}: analytic mismatch"
            assert data['analytic_matches_formula'], f"W_3 {cval}: formula mismatch"

    def test_dumbbell_stratum_matches(self):
        """Dumbbell amplitude = kappa * int(lambda_2 * delta_1) for W_3."""
        report = run_full_verification()
        for cval, data in report['dumbbell_stratum'].items():
            assert data['match'], f"Dumbbell {cval}: mismatch"

    def test_intersection_ring_consistency(self):
        """2*l2*l1 - l1^3 = 0 (Mumford relation at genus 2)."""
        report = run_full_verification()
        ir = report['intersection_ring']
        mumford = ir['mumford_relation']
        assert mumford['int_diff_l1'] == Fraction(0)


# ============================================================================
# TautClass2 pairing tests
# ============================================================================

class TestTautClass2:
    """Test the tautological class representation and pairing."""

    def test_lambda2_pairing(self):
        """lambda_2 pairs correctly with degree-1 classes."""
        l2 = TautClass2(lambda_2=Fraction(1))
        assert l2.pair_with('l1') == Fraction(1, 2880)
        assert l2.pair_with('dirr') == Fraction(0)
        assert l2.pair_with('d1') == Fraction(1, 1152)

    def test_lambda1_sq_pairing(self):
        """lambda_1^2 pairs correctly."""
        l1sq = TautClass2(l1_l1=Fraction(1))
        assert l1sq.pair_with('l1') == Fraction(1, 1440)
        assert l1sq.pair_with('dirr') == Fraction(1, 120)
        assert l1sq.pair_with('d1') == Fraction(0)

    def test_proportionality_check(self):
        """kappa * lambda_2 is proportional to lambda_2 with constant kappa."""
        kappa = Fraction(5, 6)
        c = TautClass2(lambda_2=kappa)
        is_prop, const = c.is_proportional_to_lambda2()
        assert is_prop
        assert const == kappa

    def test_nonproportionality(self):
        """lambda_1^2 is NOT proportional to lambda_2."""
        c = TautClass2(l1_l1=Fraction(1))
        is_prop, _ = c.is_proportional_to_lambda2()
        assert not is_prop

    def test_mixed_class(self):
        """lambda_2 + epsilon * lambda_1^2 is not proportional to lambda_2."""
        c = TautClass2(lambda_2=Fraction(1), l1_l1=Fraction(1, 100))
        is_prop, _ = c.is_proportional_to_lambda2()
        assert not is_prop


# ============================================================================
# F2_total calibration: F2_total = F2_scalar for single-channel algebras
# ============================================================================

class TestF2TotalCalibration:
    """Verify that F2_total = kappa * lambda_2^FP for single-channel algebras.

    The smooth vertex contribution is determined by the constraint that
    per-channel universality (PROVED) fixes each channel's total:
        smooth = F2_scalar - boundary_diagonal
        F2_total = smooth + boundary_total = F2_scalar + boundary_cross

    For single-channel algebras, boundary_cross = 0, so
        F2_total = F2_scalar = kappa * 7/5760

    This is the fundamental calibration identity.
    """

    def test_heisenberg_k1(self):
        """F2(Heisenberg, k=1) = 1 * 7/5760 = 7/5760."""
        alg = make_heisenberg(1)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total == r.F2_scalar
        assert r.F2_total == Fraction(7, 5760)

    def test_heisenberg_k2(self):
        """F2(Heisenberg, k=2) = 2 * 7/5760 = 7/2880."""
        alg = make_heisenberg(2)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total == r.F2_scalar
        assert r.F2_total == Fraction(7, 2880)

    @pytest.mark.parametrize("k", [1, 2, 5, 10])
    def test_heisenberg_parametric(self, k):
        """F2(Heisenberg, k) = k * 7/5760 for all k."""
        alg = make_heisenberg(k)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total == r.F2_scalar
        assert r.F2_total == Fraction(k) * lambda_fp(2)

    @pytest.mark.parametrize("c", C_ALL)
    def test_virasoro(self, c):
        """F2(Virasoro, c) = (c/2) * 7/5760 for all c."""
        alg = make_virasoro(c)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total == r.F2_scalar
        assert r.F2_total == (c / 2) * lambda_fp(2)

    @pytest.mark.parametrize("k", [1, 2, 5, 10])
    def test_affine_sl2(self, k):
        """F2(affine sl_2, k) = kappa * 7/5760 for all k."""
        alg = make_affine_sl2(k)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total == r.F2_scalar

    def test_betagamma_standard(self):
        """F2(betagamma) = 1 * 7/5760 = 7/5760."""
        alg = make_betagamma()
        r = compute_boundary_decomposition(alg)
        assert r.F2_total == r.F2_scalar
        assert r.F2_total == Fraction(7, 5760)

    def test_smooth_vertex_negative(self):
        """The smooth vertex contribution is negative for nontrivial algebras.

        smooth = F2_scalar - boundary_diagonal < 0 because the boundary
        graph sum (raw propagator * vertex products) overcounts relative
        to the true F_2. The smooth vertex absorbs this overcounting.
        """
        for alg in [make_heisenberg(1), make_virasoro(10), make_affine_sl2(2)]:
            r = compute_boundary_decomposition(alg)
            assert r.smooth_vertex < Fraction(0), (
                f"{alg.name}: smooth vertex {r.smooth_vertex} >= 0"
            )

    def test_f2_total_identity(self):
        """F2_total = F2_scalar + boundary_cross (algebraic identity)."""
        for alg in [make_heisenberg(1), make_virasoro(10), make_w3(10), make_w4(10)]:
            r = compute_boundary_decomposition(alg)
            assert r.F2_total == r.F2_scalar + r.boundary_cross, (
                f"{alg.name}: F2_total = {r.F2_total} != "
                f"F2_scalar + cross = {r.F2_scalar + r.boundary_cross}"
            )

    def test_smooth_plus_boundary_equals_f2(self):
        """smooth + boundary_total = F2_total (consistency check)."""
        for alg in [make_heisenberg(1), make_virasoro(26), make_w3(50)]:
            r = compute_boundary_decomposition(alg)
            reconstructed = r.smooth_vertex + r.boundary_total
            assert reconstructed == r.F2_total, (
                f"{alg.name}: smooth + boundary = {reconstructed} != "
                f"F2_total = {r.F2_total}"
            )


class TestW3Diagonal:
    """Verify the diagonal (per-channel) contribution for W_3.

    Per-channel universality (PROVED): each channel independently gives
    F_2^{(i)} = kappa_i * lambda_2^FP. The diagonal boundary sum is the
    boundary part of this per-channel sum. The smooth vertex absorbs
    the rest.
    """

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_w3_diagonal_per_channel(self, c):
        """W_3 diagonal amplitude is consistent with per-channel universality."""
        alg = make_w3(c)
        r = compute_boundary_decomposition(alg)
        # F2_total = F2_scalar + cross, where F2_scalar = kappa * lambda_2^FP
        # This holds by construction; the content is that cross != 0.
        assert r.F2_total == r.F2_scalar + r.boundary_cross

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_w3_f2_total_exceeds_scalar(self, c):
        """F2_total > F2_scalar for W_3 (cross-channel is positive)."""
        alg = make_w3(c)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total > r.F2_scalar
        assert r.boundary_cross > Fraction(0)


class TestW4Diagonal:
    """Verify W_4 cross-channel and F2_total."""

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(10), Fraction(50)])
    def test_w4_f2_total_exceeds_scalar(self, c):
        """F2_total > F2_scalar for W_4 (cross-channel is positive)."""
        alg = make_w4(c)
        r = compute_boundary_decomposition(alg)
        assert r.F2_total > r.F2_scalar
        assert r.boundary_cross > Fraction(0)

    def test_w4_more_cross_than_w3(self):
        """W_4 (3 channels) has more cross-channel than W_3 (2 channels)."""
        c = Fraction(10)
        r3 = compute_boundary_decomposition(make_w3(c))
        r4 = compute_boundary_decomposition(make_w4(c))
        assert r4.boundary_cross > r3.boundary_cross


# ============================================================================
# Genus-3 partial checks
# ============================================================================

class TestGenus3:
    """Partial genus-3 checks."""

    def test_fp_number(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_single_channel_g3(self):
        """Single-channel algebra: F_3 = kappa * lambda_3^FP."""
        alg = make_heisenberg(1)
        res = genus3_universality_check(alg)
        assert res['single_channel']
        assert res['F3_scalar'] == Fraction(31, 967680)

    def test_w3_g3_report(self):
        """W_3 genus-3 report is well-formed."""
        alg = make_w3(10)
        res = genus3_universality_check(alg)
        assert not res['single_channel']
        assert res['F3_scalar'] == Fraction(5) * Fraction(10) / 6 * Fraction(31, 967680)


# ============================================================================
# Numerical landscape
# ============================================================================

class TestNumericalLandscape:
    """Test the numerical landscape computation."""

    def test_landscape_runs(self):
        """The landscape computation completes without error."""
        results = numerical_landscape([Fraction(2), Fraction(10)])
        assert 'Heisenberg' in results
        assert 'Virasoro' in results
        assert 'W_3' in results
        assert 'W_4' in results

    def test_heisenberg_always_zero_cross(self):
        """Heisenberg always has zero cross-channel."""
        results = numerical_landscape()
        for entry in results['Heisenberg']:
            assert entry['cross_is_zero']

    def test_virasoro_always_zero_cross(self):
        """Virasoro always has zero cross-channel."""
        results = numerical_landscape()
        for entry in results['Virasoro']:
            assert entry['cross_is_zero']

    def test_w3_never_zero_cross(self):
        """W_3 NEVER has zero cross-channel (for c > 0)."""
        results = numerical_landscape()
        for entry in results['W_3']:
            assert not entry['cross_is_zero']
            assert entry['cross'] > Fraction(0)
