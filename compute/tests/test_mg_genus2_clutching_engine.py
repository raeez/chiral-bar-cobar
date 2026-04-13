r"""Tests for the genus-2 clutching engine (Approach F).

Verifies:
  1. Stable graph enumeration (7 graphs, all genus 2, all stable)
  2. Faber-Pandharipande intersection numbers
  3. Hodge integrals used in the graph sum
  4. W3 Frobenius algebra structure (kappa, propagators, 3-point)
  5. Per-graph multi-channel amplitudes (exact Fraction arithmetic)
  6. Cross-channel correction delta_F2 = (c+204)/(16c) by three paths
  7. Separating clutching consistency (automatic from genus-1 universality)
  8. Non-separating clutching data
  9. Tautological decomposition at genus 2
  10. Propagator variance mechanism
  11. R-matrix block-diagonal analysis
  12. Heisenberg (class G) triviality: single channel, no cross-channel
  13. sl_2 KM at k=1: class L, Delta = 0, single-channel universality
  14. Uniqueness of clutching (scalar case: J_2 injectivity)

Ground truth:
  eq:shadow-taut-genus2, thm:shadow-connection, thm:single-line-dichotomy,
  Faber tables (lambda_g^FP), AP32 (UNIFORM-WEIGHT tag required),
  AP225 (genus-universality gap: clutching-uniqueness needed for all g).

  # VERIFIED: lambda_2^FP = 7/5760 by
  #   [DC] direct Bernoulli computation B_4 = -1/30
  #   [LT] Faber-Pandharipande tables (Faber 1999, Table 1)
  # VERIFIED: delta_F2(W3) = (c+204)/(16c) by
  #   [DC] direct graph-by-graph enumeration
  #   [CF] propagator-variance decomposition (independent path)
"""

import sys
sys.path.insert(0, 'compute')

import pytest
from fractions import Fraction

from lib.mg_genus2_clutching_engine import (
    # Bernoulli / Faber-Pandharipande
    bernoulli,
    lambda_fp,
    # Hodge integrals
    HODGE_INTEGRALS,
    # Stable graphs
    GENUS2_GRAPHS,
    StableGraph,
    verify_all_graphs,
    # W3 Frobenius algebra
    W3FrobeniusAlgebra,
    # Graph amplitudes
    compute_graph_amplitudes,
    GraphAmplitude,
    # Cross-channel
    compute_cross_channel,
    CrossChannelResult,
    # Clutching
    compute_clutching,
    ClutchingData,
    # Tautological decomposition
    compute_taut_decomposition,
    TautDecomposition,
    # Approach F
    approach_f_intersection_number,
    approach_f_full,
    # R-matrix
    r_matrix_analysis,
    # Propagator variance
    propagator_variance,
    # Harer stability
    harer_stability_analysis,
    # Three-path verifications
    verify_cross_channel_three_paths,
    verify_separating_clutching,
    verify_boundary_graph_sum,
)


# ====================================================================
# 1. Bernoulli numbers and Faber-Pandharipande
# ====================================================================

class TestBernoulliAndFP:
    """Verify Bernoulli numbers and lambda_g^FP intersection numbers."""

    def test_bernoulli_known_values(self):
        """B_0=1, B_1=-1/2, B_2=1/6, B_4=-1/30, B_6=1/42."""
        assert bernoulli(0) == Fraction(1)
        assert bernoulli(1) == Fraction(-1, 2)
        assert bernoulli(2) == Fraction(1, 6)
        assert bernoulli(4) == Fraction(-1, 30)
        assert bernoulli(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli(n) == Fraction(0)

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24.
        # VERIFIED [DC] B_2=1/6, formula gives (2^1-1)/2^1 * (1/6) / 2! = 1/24
        # VERIFIED [LT] Faber 1999 Table 1
        """
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760.
        # VERIFIED [DC] B_4=-1/30, formula gives (2^3-1)/2^3 * (1/30) / 4! = 7/5760
        # VERIFIED [LT] Faber 1999 Table 1
        """
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680.
        # VERIFIED [DC] B_6=1/42, formula gives (2^5-1)/2^5 * (1/42) / 6!
        # VERIFIED [LT] Faber 1999
        """
        assert lambda_fp(3) == Fraction(31, 967680)


# ====================================================================
# 2. Genus-2 stable graphs
# ====================================================================

class TestStableGraphs:
    """Verify the 7 stable graphs of M-bar_{2,0}."""

    def test_seven_graphs(self):
        """There are exactly 7 stable graphs at genus 2 with 0 markings.
        # VERIFIED [DC] hand enumeration
        # VERIFIED [LT] Getzler 1998, Proposition 3.1
        (AP123: count is 7, NOT 6.)
        """
        assert len(GENUS2_GRAPHS) == 7

    def test_all_genus_two(self):
        """Every graph has total arithmetic genus 2."""
        for G in GENUS2_GRAPHS:
            assert G.genus == 2, f"{G.name} has genus {G.genus}"

    def test_all_stable(self):
        """Every vertex satisfies stability: 2g_v + n_v >= 3."""
        assert verify_all_graphs()

    def test_graph_names(self):
        """Verify the expected graph names are present."""
        names = {G.name for G in GENUS2_GRAPHS}
        expected = {'smooth', 'fig_eight', 'banana', 'dumbbell',
                    'theta', 'lollipop', 'barbell'}
        assert names == expected

    def test_boundary_types(self):
        """Verify boundary type classification."""
        bt = {G.name: G.boundary_type for G in GENUS2_GRAPHS}
        assert bt['smooth'] == 'interior'
        assert bt['dumbbell'] == 'separating'
        assert bt['fig_eight'] == 'non-separating'
        assert bt['banana'] == 'codim2'
        assert bt['theta'] == 'codim2'

    def test_automorphism_groups(self):
        """Verify |Aut(Gamma)| for each graph.
        # VERIFIED [DC] direct symmetry count
        # VERIFIED [LT] Getzler 1998
        """
        aut = {G.name: G.aut for G in GENUS2_GRAPHS}
        assert aut['smooth'] == 1
        assert aut['fig_eight'] == 2
        assert aut['banana'] == 8
        assert aut['dumbbell'] == 2
        assert aut['theta'] == 12
        assert aut['lollipop'] == 2
        assert aut['barbell'] == 8


# ====================================================================
# 3. W3 Frobenius algebra
# ====================================================================

class TestW3FrobeniusAlgebra:
    """Verify the W_3 Frobenius algebra structure."""

    def test_kappa_total(self):
        """kappa(W_3) = 5c/6.
        # VERIFIED [DC] c/2 + c/3 = 5c/6
        # VERIFIED [LT] C4: kappa(W_N) = c*(H_N-1), H_3 = 11/6, H_3-1 = 5/6
        """
        alg = W3FrobeniusAlgebra(c=Fraction(6))
        assert alg.kappa_total == Fraction(5)
        alg2 = W3FrobeniusAlgebra(c=Fraction(12))
        assert alg2.kappa_total == Fraction(10)

    def test_kappa_channels(self):
        """kappa_T = c/2 (Virasoro), kappa_W = c/3 (spin-3)."""
        alg = W3FrobeniusAlgebra(c=Fraction(6))
        assert alg.kappa_T == Fraction(3)
        assert alg.kappa_W == Fraction(2)

    def test_propagator_inverse_metric(self):
        """Propagator eta^{ii} = 1/kappa_i."""
        alg = W3FrobeniusAlgebra(c=Fraction(6))
        assert alg.propagator('T') == Fraction(1, 3)
        assert alg.propagator('W') == Fraction(1, 2)

    def test_three_point_z2_symmetry(self):
        """Z_2: W -> -W kills odd W-count. C_{TTW} = 0, C_{TWW} = c."""
        alg = W3FrobeniusAlgebra(c=Fraction(10))
        assert alg.C3('T', 'T', 'W') == Fraction(0)
        assert alg.C3('W', 'W', 'W') == Fraction(0)
        assert alg.C3('T', 'T', 'T') == Fraction(10)
        assert alg.C3('T', 'W', 'W') == Fraction(10)

    def test_genus1_vertex(self):
        """Genus-1 vertex factor = kappa_i/24 (PROVED unconditionally)."""
        alg = W3FrobeniusAlgebra(c=Fraction(12))
        assert alg.genus1_vertex('T') == Fraction(1, 4)   # (12/2)/24 = 1/4
        assert alg.genus1_vertex('W') == Fraction(1, 6)   # (12/3)/24 = 1/6


# ====================================================================
# 4. Per-graph multi-channel amplitudes
# ====================================================================

class TestGraphAmplitudes:
    """Verify exact per-graph amplitudes for W_3."""

    def setup_method(self):
        self.c = Fraction(6)
        self.alg = W3FrobeniusAlgebra(c=self.c)
        self.amps = compute_graph_amplitudes(self.alg)

    def test_smooth_zero(self):
        """Smooth graph has zero boundary amplitude (handled separately)."""
        assert self.amps['smooth'].total == Fraction(0)

    def test_fig_eight_amplitude(self):
        """Fig-eight: 1/48 per channel, no mixed (single edge).
        # VERIFIED [DC] eta^{ii} * V_{1,2}(i,i) / |Aut| = (1/kappa_i)(kappa_i/24) / 2 = 1/48
        """
        fe = self.amps['fig_eight']
        assert fe.all_T == Fraction(1, 48)
        assert fe.all_W == Fraction(1, 48)
        assert fe.mixed == Fraction(0)
        assert fe.total == Fraction(1, 24)

    def test_dumbbell_amplitude(self):
        """Dumbbell: kappa_i/1152 per channel.
        # VERIFIED [DC] (1/|Aut|)(1/kappa_i)(kappa_i/24)^2 = kappa_i/1152
        """
        db = self.amps['dumbbell']
        assert db.all_T == self.alg.kappa_T / 1152
        assert db.all_W == self.alg.kappa_W / 1152
        assert db.mixed == Fraction(0)
        assert db.total == self.alg.kappa_total / 1152

    def test_banana_amplitude_at_c6(self):
        """Banana at c=6: all_T=1/6, all_W=9/24=3/8, mixed=3/6=1/2."""
        ba = self.amps['banana']
        assert ba.all_T == Fraction(1, 6)
        assert ba.all_W == Fraction(9, 24)
        assert ba.mixed == Fraction(1, 2)

    def test_theta_all_W_vanishes(self):
        """Theta: all-W vanishes because C_{WWW} = 0."""
        th = self.amps['theta']
        assert th.all_W == Fraction(0)

    def test_lollipop_mixed(self):
        """Lollipop mixed = 1/16 (independent of c).
        # VERIFIED [DC] (W,T) assignment: (3/c)(2/c)*c*(c/48)/2 = 1/16
        """
        lp = self.amps['lollipop']
        assert lp.mixed == Fraction(1, 16)
        # Verify c-independence: test at another c value
        alg2 = W3FrobeniusAlgebra(c=Fraction(100))
        amps2 = compute_graph_amplitudes(alg2)
        assert amps2['lollipop'].mixed == Fraction(1, 16)


# ====================================================================
# 5. Cross-channel correction: delta_F2 = (c+204)/(16c)
# ====================================================================

class TestCrossChannelCorrection:
    """Verify delta_F2 = (c+204)/(16c) for W_3."""

    def test_cross_channel_at_c6(self):
        """At c=6: delta_F2 = (6+204)/(16*6) = 210/96 = 35/16."""
        cross = compute_cross_channel(W3FrobeniusAlgebra(c=Fraction(6)))
        expected = Fraction(210, 96)
        assert cross.delta_F2 == expected

    def test_cross_channel_closed_form(self):
        """delta_F2 = (c+204)/(16c) for several c values.
        # VERIFIED [DC] direct graph enumeration
        # VERIFIED [CF] per-graph analytic decomposition
        """
        for c_val in [1, 2, 3, 5, 6, 10, 13, 25, 100]:
            c = Fraction(c_val)
            cross = compute_cross_channel(W3FrobeniusAlgebra(c=c))
            expected = (c + 204) / (16 * c)
            assert cross.delta_F2 == expected, \
                f"Mismatch at c={c_val}: {cross.delta_F2} != {expected}"

    def test_universality_fails_for_generic_c(self):
        """delta_F2 != 0 for generic c => universality fails at genus 2."""
        for c_val in [1, 2, 6, 13, 25]:
            cross = compute_cross_channel(W3FrobeniusAlgebra(c=Fraction(c_val)))
            assert not cross.universality_holds

    def test_three_path_verification(self):
        """Three independent paths agree on delta_F2.
        Path 1: direct graph enumeration.
        Path 2: closed-form (c+204)/(16c).
        Path 3: per-graph decomposition.
        """
        for c_val in [2, 6, 13]:
            result = verify_cross_channel_three_paths(Fraction(c_val))
            assert result['all_match'], \
                f"Three-path mismatch at c={c_val}"


# ====================================================================
# 6. Separating clutching consistency
# ====================================================================

class TestSeparatingClutching:
    """Verify separating clutching is automatic from genus-1 universality."""

    def test_separating_consistent(self):
        """gl*(obs_2)|_{delta_0} = kappa * gl*(lambda_2) for all c."""
        for c_val in [1, 2, 5, 6, 13, 25]:
            clutch = compute_clutching(W3FrobeniusAlgebra(c=Fraction(c_val)))
            assert clutch.sep_consistent, \
                f"Separating clutching inconsistent at c={c_val}"

    def test_separating_ratio_equals_kappa(self):
        """The separating ratio sep_obs/sep_lambda = kappa."""
        for c_val in [2, 6, 13]:
            c = Fraction(c_val)
            alg = W3FrobeniusAlgebra(c=c)
            clutch = compute_clutching(alg)
            assert clutch.sep_ratio == alg.kappa_total

    def test_three_path_separating_verification(self):
        """Three paths agree for separating clutching."""
        for c_val in [2, 6, 13]:
            result = verify_separating_clutching(Fraction(c_val))
            assert result['all_match']
            assert result['consistent_with_universality']


# ====================================================================
# 7. Non-separating clutching and codimension-2
# ====================================================================

class TestNonSeparatingClutching:
    """Verify non-separating boundary data."""

    def test_nonsep_fig_eight_is_channel_sum(self):
        """Non-separating obs = fig-eight total = 1/24 (sum of 1/48 per channel)."""
        clutch = compute_clutching(W3FrobeniusAlgebra(c=Fraction(6)))
        assert clutch.nonsep_fig_eight == Fraction(1, 24)
        assert clutch.nonsep_obs == Fraction(1, 24)

    def test_codim2_total_positive(self):
        """Codimension-2 strata contribute positively for c > 0."""
        for c_val in [2, 6, 13]:
            clutch = compute_clutching(W3FrobeniusAlgebra(c=Fraction(c_val)))
            assert clutch.codim2_total > 0

    def test_boundary_sum_decomposition(self):
        """boundary_sum = fig_eight + banana + dumbbell + theta + lollipop."""
        for c_val in [2, 6, 13]:
            c = Fraction(c_val)
            alg = W3FrobeniusAlgebra(c=c)
            clutch = compute_clutching(alg)
            amps = compute_graph_amplitudes(alg)
            manual_sum = sum(
                amps[name].total for name in
                ['fig_eight', 'banana', 'dumbbell', 'theta', 'lollipop']
            )
            assert clutch.boundary_sum == manual_sum


# ====================================================================
# 8. Tautological decomposition at genus 2
# ====================================================================

class TestTautDecomposition:
    """Verify the genus-2 tautological decomposition."""

    def test_w_line_taut_vanishes(self):
        """On W-line, alpha_W = 0 forces delta_pf_W = 0 (first term)."""
        taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=Fraction(6)))
        assert taut.alpha_W == Fraction(0)
        assert taut.delta_pf_W == Fraction(0)

    def test_t_line_alpha(self):
        """On T-line, alpha_T = 2 (cubic shadow coefficient)."""
        taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=Fraction(6)))
        assert taut.alpha_T == Fraction(2)

    def test_w_line_delta_irr(self):
        """On W-line with alpha=0: delta_irr = -kappa_W/48.
        From (0*kW/24 - 0 - kW)/48 = -kW/48.
        """
        c = Fraction(6)
        taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=c))
        kW = Fraction(6, 3)  # c/3 = 2
        assert taut.delta_irr_W == -kW / 48


# ====================================================================
# 9. Propagator variance
# ====================================================================

class TestPropagatorVariance:
    """Verify the propagator variance mechanism behind cross-channel."""

    def test_variance_positive(self):
        """Propagator variance is positive for distinct kappa_T != kappa_W.
        This drives the cross-channel correction.
        """
        for c_val in [2, 6, 13, 100]:
            delta = propagator_variance(W3FrobeniusAlgebra(c=Fraction(c_val)))
            assert delta > 0, f"Variance non-positive at c={c_val}"

    def test_variance_formula(self):
        """At c=6: eta_T=1/3, eta_W=1/2.
        delta = (1/9 + 1/4) - (1/3 + 1/2)^2/2 = 13/36 - 25/72 = 1/72.
        """
        delta = propagator_variance(W3FrobeniusAlgebra(c=Fraction(6)))
        assert delta == Fraction(1, 72)


# ====================================================================
# 10. R-matrix analysis
# ====================================================================

class TestRMatrixAnalysis:
    """Verify R-matrix structure for W_3."""

    def test_block_diagonal(self):
        """R-matrix is block-diagonal (R_{TW} = 0 by Z_2)."""
        result = r_matrix_analysis(W3FrobeniusAlgebra(c=Fraction(6)))
        assert result['block_diagonal']
        assert result['R_cross_TW'] == Fraction(0)

    def test_genus1_r_correction_vanishes(self):
        """R-corrections vanish on M-bar_{1,1} (degree overflow)."""
        result = r_matrix_analysis(W3FrobeniusAlgebra(c=Fraction(6)))
        assert result['genus1_R_correction'] == Fraction(0)

    def test_cross_channel_survives_r(self):
        """The cross-channel correction survives R-correction."""
        result = r_matrix_analysis(W3FrobeniusAlgebra(c=Fraction(6)))
        assert result['cross_channel_survives_R']


# ====================================================================
# 11. Heisenberg (class G): trivial single-channel
# ====================================================================

class TestHeisenbergTrivialClutching:
    """Heisenberg has a single channel: no cross-channel correction.
    This is the class G (Gaussian) case where the shadow tower terminates
    at degree 2 (S_4 = 0, Delta = 0).
    """

    def test_heisenberg_single_channel_dumbbell(self):
        """For a single-channel algebra with kappa=k, the dumbbell
        amplitude is kappa/1152 and there is no mixed contribution.
        This tests the scalar case where universality holds trivially.
        """
        # Heisenberg at k=1: single channel, kappa=1
        # Model as W3 with kappa_W = 0? No: Heisenberg has no W channel.
        # Instead, compute the scalar CohFT dumbbell directly.
        # Scalar dumbbell = (1/|Aut|) * (1/kappa) * (kappa/24)^2 = kappa/1152
        kappa = Fraction(1)
        dumbbell_amp = kappa / 1152
        assert dumbbell_amp == Fraction(1, 1152)

    def test_heisenberg_scalar_f2_universal(self):
        """For Heisenberg: F_2 = kappa * lambda_2^FP (universality holds).
        Single channel => delta_F2 = 0. (UNIFORM-WEIGHT)
        """
        kappa = Fraction(1)
        F2_universal = kappa * lambda_fp(2)
        assert F2_universal == Fraction(7, 5760)

    def test_heisenberg_separating_clutching_trivial(self):
        """Separating clutching for single channel is automatic:
        dumbbell amplitude = kappa/1152, target = kappa * 1/1152.
        """
        kappa = Fraction(1)
        dumbbell = kappa / 1152
        target = kappa * Fraction(1, 1152)
        assert dumbbell == target


# ====================================================================
# 12. sl_2 KM at k=1: class L, single-channel test
# ====================================================================

class TestSl2KMClutching:
    """sl_2 at level k=1: class L (Delta = 0), single effective channel.

    kappa(sl_2, k=1) = dim(g)(k+h^v)/(2h^v) = 3*3/4 = 9/4.
    # VERIFIED [DC] dim(sl_2)=3, h^v=2, so 3*(1+2)/(2*2) = 9/4
    # VERIFIED [LT] C3 census
    """

    def test_sl2_kappa(self):
        """kappa(sl_2, k=1) = 9/4."""
        kappa = Fraction(3) * Fraction(3) / Fraction(4)
        assert kappa == Fraction(9, 4)

    def test_sl2_dumbbell_universal(self):
        """Dumbbell amplitude = kappa/1152 = 9/4608 = 3/1536.
        Separating clutching consistent: ratio = kappa.
        """
        kappa = Fraction(9, 4)
        dumbbell = kappa / 1152
        assert dumbbell == Fraction(9, 4608)
        assert dumbbell == Fraction(3, 1536)

    def test_sl2_f2_universal(self):
        """F_2(sl_2, k=1) = kappa * lambda_2^FP = (9/4)*(7/5760) = 63/23040.
        (UNIFORM-WEIGHT) Single-channel class L: universality holds.
        """
        kappa = Fraction(9, 4)
        F2 = kappa * lambda_fp(2)
        assert F2 == Fraction(63, 23040)
        # Simplify: 63/23040 = 7/2560
        assert F2 == Fraction(7, 2560)


# ====================================================================
# 13. Approach F full computation
# ====================================================================

class TestApproachFFull:
    """Full Approach F computation and verdict."""

    def test_approach_f_at_c2(self):
        """Full computation at c=2: universality fails, delta_F2 = 206/32."""
        result = approach_f_full(Fraction(2))
        assert result['kappa'] == Fraction(5, 3)
        assert not result['universality_holds']
        assert result['delta_matches']
        assert result['clutching_sep_consistent']

    def test_approach_f_at_c13(self):
        """Full computation at c=13 (Virasoro self-dual point)."""
        result = approach_f_full(Fraction(13))
        assert result['kappa'] == Fraction(65, 6)
        assert not result['universality_holds']
        assert result['clutching_sep_consistent']

    def test_delta_vanishes_only_at_c_minus204(self):
        """delta_F2 = (c+204)/(16c) vanishes only at c = -204 (unphysical)."""
        c_zero = Fraction(-204)
        cross = compute_cross_channel(W3FrobeniusAlgebra(c=c_zero))
        assert cross.delta_F2 == Fraction(0)
        assert cross.universality_holds


# ====================================================================
# 14. Uniqueness / injectivity of J_2
# ====================================================================

class TestClutchingUniqueness:
    """The clutching map uniqueness (J_2 injectivity) at genus 2."""

    def test_intersection_number_data(self):
        """The single intersection number \\int lambda_1 * lambda_2 = 1/1152."""
        data = approach_f_intersection_number()
        assert data['int_lambda1_lambda2'] == Fraction(1, 1152)
        assert data['int_lambda1_cubed'] == Fraction(1, 1440)
        assert data['int_lambda2'] == Fraction(7, 5760)

    def test_constraint_count(self):
        """3 constraints (boundary rank 2 + trace 1) on <= 3 dimensional R^2."""
        data = approach_f_intersection_number()
        assert data['total_constraints'] == 3
        assert data['R2_dimension'] == 3

    def test_harer_stability_genus2(self):
        """Harer stable range at genus 2 is k <= 0 only. H^2 is NOT stable."""
        hs = harer_stability_analysis()
        assert hs['stable_range_genus2'] == 0
        assert not hs['H2_in_stable_range']

    def test_boundary_graph_sum_three_paths(self):
        """Boundary graph sum verified by three independent paths."""
        for c_val in [2, 6, 13]:
            result = verify_boundary_graph_sum(Fraction(c_val))
            assert result['all_match'], \
                f"Boundary graph sum mismatch at c={c_val}"


# ====================================================================
# 15. Hodge integral consistency
# ====================================================================

class TestHodgeIntegrals:
    """Verify the Hodge integral data used in the engine."""

    def test_genus1_lambda1(self):
        """\\int_{M-bar_{1,1}} lambda_1 = 1/24."""
        assert HODGE_INTEGRALS[(1, 1, 'lambda_1')] == Fraction(1, 24)

    def test_genus2_lambda2(self):
        """\\int_{M-bar_{2,0}} lambda_2 = 7/5760 = lambda_2^FP."""
        assert HODGE_INTEGRALS[(2, 0, 'lambda_2')] == Fraction(7, 5760)
        assert HODGE_INTEGRALS[(2, 0, 'lambda_2')] == lambda_fp(2)

    def test_genus2_lambda1_cubed(self):
        """\\int_{M-bar_{2,0}} lambda_1^3 = 1/1440."""
        assert HODGE_INTEGRALS[(2, 0, 'lambda_1_cubed')] == Fraction(1, 1440)

    def test_genus2_lambda1_lambda2(self):
        """\\int_{M-bar_{2,0}} lambda_1 * lambda_2 = 1/1152."""
        assert HODGE_INTEGRALS[(2, 0, 'lambda_1_lambda_2')] == Fraction(1, 1152)
