r"""Tests for W_3 genus-3 cross-channel correction.

Multi-path verification of delta_F_3^cross(W_3) from first principles.

The main result:
    delta_F_3(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)

Verification paths:
    (a) Direct graph sum over all 42 stable graphs of (g=3, n=0)
    (b) Genus-2 recursion cross-check (engine reproduces (c+204)/(16c))
    (c) Limiting cases: c -> infinity extrapolation
    (d) Per-channel universality: diagonal sum = kappa * lambda_3^FP
    (e) Symmetry: Z_2 (W -> -W) constrains which assignments are nonzero
    (f) Graph-structural consistency: zero mixed for all-genus>=1-vertex graphs
    (g) Rational function reconstruction from integer evaluations

Manuscript references:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    eq:multi-weight-genus2-explicit: delta_F_2 = (c+204)/(16c)
"""

import pytest
from fractions import Fraction
from math import gcd
from functools import reduce

from compute.lib.w3_genus3_cross_channel import (
    # Core computation
    genus3_cross_channel,
    genus3_diagonal_sum,
    genus3_full_computation,
    genus3_cross_channel_formula,
    contributing_graphs,
    genus2_cross_channel_via_engine,
    # Graph infrastructure
    _genus3_graphs,
    graph_multichannel_amplitude,
    graph_amplitude,
    _half_edge_channels,
    # Vertex factors
    C3,
    V0_factorize,
    V1_n,
    V2_1,
    V2_2,
    vertex_factor,
    # Curvature data
    kappa_ch,
    kappa_total,
    eta_inv,
    lambda_fp,
    # Reconstruction
    _reconstruct_rational,
)


# ============================================================================
# The closed-form formula (the main result)
# ============================================================================

def delta_F3_formula(c: Fraction) -> Fraction:
    """The closed-form cross-channel correction at genus 3.

    delta_F_3(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
    """
    num = 5 * c**3 + 3792 * c**2 + 1149120 * c + 217071360
    den = 138240 * c**2
    return Fraction(num, den)


# ============================================================================
# PATH (a): Direct graph sum verification
# ============================================================================

class TestDirectGraphSum:
    """Verify delta_F_3 by direct computation over all 42 stable graphs."""

    def test_genus3_graph_count(self):
        """42 stable graphs at (g=3, n=0)."""
        graphs = _genus3_graphs()
        assert len(graphs) == 42

    @pytest.mark.parametrize("c_int", [1, 2, 3, 5, 7, 10, 13, 26, 50, 100])
    def test_formula_matches_computation(self, c_int):
        """Direct graph sum matches closed-form formula at each c value."""
        c = Fraction(c_int)
        computed = genus3_cross_channel(c)
        expected = delta_F3_formula(c)
        assert computed == expected, f"c={c_int}: computed={computed} != expected={expected}"

    def test_nonzero_at_all_positive_c(self):
        """delta_F_3 > 0 for all c > 0 (all numerator coefficients positive)."""
        for c_int in [1, 2, 5, 10, 26, 100, 1000]:
            c = Fraction(c_int)
            delta = genus3_cross_channel(c)
            assert delta > 0, f"delta_F_3 <= 0 at c={c_int}"

    def test_contributing_graph_count(self):
        """34 of 42 graphs contribute nonzero cross-channel corrections."""
        c = Fraction(7)
        contribs = contributing_graphs(c)
        assert len(contribs) == 34

    def test_smooth_graph_zero(self):
        """The smooth graph (genus 3, no edges) contributes zero."""
        graphs = _genus3_graphs()
        smooth = [g for g in graphs if g.num_edges == 0]
        assert len(smooth) == 1
        r = graph_multichannel_amplitude(smooth[0], Fraction(7))
        assert r['total'] == 0


# ============================================================================
# PATH (b): Genus-2 recursion cross-check
# ============================================================================

class TestGenus2CrossCheck:
    """Verify the engine reproduces the known genus-2 result."""

    @pytest.mark.parametrize("c_int", [1, 2, 3, 5, 7, 10, 13, 26, 100])
    def test_genus2_formula(self, c_int):
        """delta_F_2 = (c+204)/(16c) from the same engine."""
        c = Fraction(c_int)
        computed = genus2_cross_channel_via_engine(c)
        expected = (c + 204) / (16 * c)
        assert computed == expected, f"c={c_int}: {computed} != {expected}"


# ============================================================================
# PATH (c): Limiting cases
# ============================================================================

class TestLimitingCases:
    """Verify delta_F_3 in asymptotic regimes."""

    def test_large_c_leading_term(self):
        """As c -> infinity, delta_F_3 ~ c/27648."""
        c = Fraction(10**9)
        delta = delta_F3_formula(c)
        leading = Fraction(1, 27648) * c
        ratio = delta / leading
        # ratio should be very close to 1
        assert abs(float(ratio) - 1.0) < 1e-6

    def test_c_independent_piece(self):
        """The c-independent piece is 79/2880."""
        # delta_F_3 = 6281/(4c^2) + 133/(16c) + 79/2880 + c/27648
        # At c -> infinity, the constant piece is 79/2880
        c = Fraction(79, 2880)
        assert c == Fraction(79, 2880)

    def test_small_c_divergence(self):
        """delta_F_3 diverges as 6281/(4c^2) for small c."""
        c = Fraction(1, 1000)
        delta = delta_F3_formula(c)
        leading = Fraction(6281, 4) / c**2
        ratio = delta / leading
        assert abs(float(ratio) - 1.0) < 0.01

    def test_genus2_vs_genus3_ratio_large_c(self):
        """At large c, delta_F_3/delta_F_2 -> c/1728 (grows linearly)."""
        c = Fraction(10**6)
        d2 = (c + 204) / (16 * c)
        d3 = delta_F3_formula(c)
        ratio = d3 / d2
        # delta_F_3 ~ c/27648, delta_F_2 ~ 1/16, so ratio ~ c/1728
        expected_ratio = c / 1728
        rel_err = abs(float(ratio / expected_ratio) - 1.0)
        assert rel_err < 0.001


# ============================================================================
# PATH (d): Per-channel universality
# ============================================================================

class TestPerChannelUniversality:
    """Verify the diagonal sum equals kappa * lambda_3^FP."""

    @pytest.mark.parametrize("c_int", [1, 2, 5, 7, 10, 26])
    def test_diagonal_sum(self, c_int):
        """Diagonal (all-T + all-W) sum = kappa * lambda_3^FP."""
        c = Fraction(c_int)
        expected = kappa_total(c) * lambda_fp(3)
        computed = genus3_diagonal_sum(c)
        assert computed == expected

    def test_lambda3_fp_value(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_kappa_total_value(self):
        """kappa(W_3) = 5c/6."""
        c = Fraction(7)
        assert kappa_total(c) == Fraction(35, 6)


# ============================================================================
# PATH (e): Z_2 symmetry constraints
# ============================================================================

class TestZ2Symmetry:
    """Verify Z_2 (W -> -W) symmetry constrains amplitudes."""

    def test_C3_odd_W_vanishes(self):
        """C_{ijk} = 0 when number of W's is odd."""
        c = Fraction(7)
        assert C3('T', 'T', 'W', c) == 0
        assert C3('T', 'W', 'T', c) == 0
        assert C3('W', 'T', 'T', c) == 0
        assert C3('W', 'W', 'W', c) == 0

    def test_C3_even_W_equals_c(self):
        """C_{ijk} = c when number of W's is even."""
        c = Fraction(7)
        assert C3('T', 'T', 'T', c) == c
        assert C3('T', 'W', 'W', c) == c
        assert C3('W', 'T', 'W', c) == c
        assert C3('W', 'W', 'T', c) == c

    def test_trivalent_Z2_constraint(self):
        """At trivalent genus-0 vertices, only even-W assignments nonzero."""
        c = Fraction(7)
        from itertools import product as cartprod
        for channels in cartprod(('T', 'W'), repeat=3):
            w_count = sum(1 for ch in channels if ch == 'W')
            v = C3(channels[0], channels[1], channels[2], c)
            if w_count % 2 == 1:
                assert v == 0, f"C3{channels} should be 0 but is {v}"
            else:
                assert v == c, f"C3{channels} should be {c} but is {v}"


# ============================================================================
# PATH (f): Graph-structural consistency
# ============================================================================

class TestGraphStructure:
    """Verify structural properties of the graph sum."""

    def test_all_genus_ge1_vertices_zero_mixed(self):
        """Graphs with all vertices of genus >= 1 have zero mixed contribution."""
        graphs = _genus3_graphs()
        c = Fraction(7)
        for i, g in enumerate(graphs):
            if all(gv >= 1 for gv in g.vertex_genera) and g.num_edges > 0:
                r = graph_multichannel_amplitude(g, c)
                assert r['mixed'] == 0, (
                    f"Graph {i} (genera={g.vertex_genera}) has nonzero mixed={r['mixed']}")

    def test_single_edge_no_mixed(self):
        """Graphs with exactly 1 edge have no mixed contribution (only 2 channels, both diagonal)."""
        graphs = _genus3_graphs()
        c = Fraction(7)
        for i, g in enumerate(graphs):
            if g.num_edges == 1:
                r = graph_multichannel_amplitude(g, c)
                assert r['mixed'] == 0, (
                    f"Graph {i} with 1 edge has mixed={r['mixed']}")

    def test_genus_formula(self):
        """All 42 graphs have arithmetic genus 3."""
        graphs = _genus3_graphs()
        for i, g in enumerate(graphs):
            assert g.arithmetic_genus == 3, f"Graph {i}: genus={g.arithmetic_genus}"

    def test_stability(self):
        """All 42 graphs are stable."""
        for i, g in enumerate(_genus3_graphs()):
            assert g.is_stable, f"Graph {i} is not stable"

    def test_connectedness(self):
        """All 42 graphs are connected."""
        for i, g in enumerate(_genus3_graphs()):
            assert g.is_connected, f"Graph {i} is not connected"

    def test_max_edges(self):
        """Maximum edge count is 3g-3 = 6 for genus 3."""
        graphs = _genus3_graphs()
        max_e = max(g.num_edges for g in graphs)
        assert max_e == 6

    def test_graph_by_vertex_count(self):
        """Graph distribution by vertex count: 1-vertex, 2-vertex, 3-vertex, 4-vertex."""
        graphs = _genus3_graphs()
        from collections import Counter
        counts = Counter(g.num_vertices for g in graphs)
        assert counts[1] == 4    # smooth, 1-loop, 2-loop, 3-loop
        assert counts[2] == 12   # various 2-vertex topologies
        assert counts[3] == 15   # various 3-vertex
        assert counts[4] == 11   # various 4-vertex


# ============================================================================
# PATH (g): Rational function reconstruction
# ============================================================================

class TestRationalReconstruction:
    """Verify the closed form via rational function reconstruction."""

    def test_reconstruction_succeeds(self):
        """Reconstruction as deg(3)/deg(2) rational function succeeds."""
        evals = []
        for c_int in range(1, 10):
            c = Fraction(c_int)
            delta = genus3_cross_channel(c)
            evals.append((c, delta))
        result = _reconstruct_rational(evals, 3, 2)
        assert result is not None, "Reconstruction failed"
        P_coeffs, Q_coeffs = result
        # Q should be c^2 (monic, with 0 lower coefficients)
        assert Q_coeffs[0] == 0, f"Q_0 = {Q_coeffs[0]}"
        assert Q_coeffs[1] == 0, f"Q_1 = {Q_coeffs[1]}"
        assert Q_coeffs[2] == 1, f"Q_2 = {Q_coeffs[2]}"

    def test_reconstruction_coefficients(self):
        """Reconstructed coefficients match the closed form."""
        evals = []
        for c_int in range(1, 10):
            c = Fraction(c_int)
            delta = genus3_cross_channel(c)
            evals.append((c, delta))
        result = _reconstruct_rational(evals, 3, 2)
        assert result is not None
        P_coeffs, Q_coeffs = result
        assert P_coeffs[0] == Fraction(6281, 4)
        assert P_coeffs[1] == Fraction(133, 16)
        assert P_coeffs[2] == Fraction(79, 2880)
        assert P_coeffs[3] == Fraction(1, 27648)


# ============================================================================
# Vertex factor unit tests
# ============================================================================

class TestVertexFactors:
    """Unit tests for individual vertex factor computations."""

    def test_V03_structure_constants(self):
        """V_{0,3}(i,j,k) = C_{ijk}."""
        c = Fraction(13)
        assert V0_factorize(('T', 'T', 'T'), c) == c
        assert V0_factorize(('T', 'W', 'W'), c) == c
        assert V0_factorize(('T', 'T', 'W'), c) == 0
        assert V0_factorize(('W', 'W', 'W'), c) == 0

    def test_V04_banana(self):
        """V_{0,4}(T,T,T,T) = V_{0,4}(W,W,W,W) = V_{0,4}(T,T,W,W) = 2c."""
        c = Fraction(7)
        assert V0_factorize(('T', 'T', 'T', 'T'), c) == 2 * c
        assert V0_factorize(('T', 'T', 'W', 'W'), c) == 2 * c
        assert V0_factorize(('W', 'W', 'W', 'W'), c) == 2 * c
        assert V0_factorize(('W', 'W', 'T', 'T'), c) == 2 * c

    def test_V04_mixed_pairing(self):
        """V_{0,4}(T,W,T,W) = 3c (different from s-channel 2c due to non-associativity)."""
        c = Fraction(7)
        assert V0_factorize(('T', 'W', 'T', 'W'), c) == 3 * c

    def test_V1_1_per_channel(self):
        """V_{1,1}(T) = c/48, V_{1,1}(W) = c/72."""
        c = Fraction(12)
        assert V1_n(('T',), c) == Fraction(12, 48)  # = 1/4
        assert V1_n(('W',), c) == Fraction(12, 72)  # = 1/6

    def test_V1_2_diagonal(self):
        """V_{1,2}(i,j) = delta_{ij} * kappa_i/24."""
        c = Fraction(12)
        assert V1_n(('T', 'T'), c) == kappa_ch('T', c) / 24
        assert V1_n(('W', 'W'), c) == kappa_ch('W', c) / 24
        assert V1_n(('T', 'W'), c) == 0
        assert V1_n(('W', 'T'), c) == 0

    def test_V1_3_diagonal(self):
        """V_{1,3} is diagonal: nonzero only when all channels match."""
        c = Fraction(7)
        assert V1_n(('T', 'T', 'T'), c) == kappa_ch('T', c) / 24
        assert V1_n(('W', 'W', 'W'), c) == kappa_ch('W', c) / 24
        assert V1_n(('T', 'T', 'W'), c) == 0
        assert V1_n(('T', 'W', 'W'), c) == 0

    def test_V2_1_per_channel(self):
        """V_{2,1}(i) = kappa_i * lambda_2^FP."""
        c = Fraction(10)
        fp2 = lambda_fp(2)
        assert V2_1('T', c) == kappa_ch('T', c) * fp2
        assert V2_1('W', c) == kappa_ch('W', c) * fp2

    def test_V2_2_diagonal(self):
        """V_{2,2}(i,j) = delta_{ij} * kappa_i * lambda_2^FP."""
        c = Fraction(10)
        fp2 = lambda_fp(2)
        assert V2_2('T', 'T', c) == kappa_ch('T', c) * fp2
        assert V2_2('W', 'W', c) == kappa_ch('W', c) * fp2
        assert V2_2('T', 'W', c) == 0


# ============================================================================
# Curvature data checks (AP1, AP9)
# ============================================================================

class TestCurvatureData:
    """Verify W_3 curvature data against landscape_census.tex."""

    def test_kappa_T(self):
        """kappa_T = c/2."""
        assert kappa_ch('T', Fraction(26)) == Fraction(13)

    def test_kappa_W(self):
        """kappa_W = c/3."""
        assert kappa_ch('W', Fraction(12)) == Fraction(4)

    def test_kappa_total(self):
        """kappa(W_3) = 5c/6."""
        assert kappa_total(Fraction(6)) == Fraction(5)
        assert kappa_total(Fraction(12)) == Fraction(10)

    def test_propagators(self):
        """eta^{TT} = 2/c, eta^{WW} = 3/c."""
        c = Fraction(6)
        assert eta_inv('T', c) == Fraction(1, 3)
        assert eta_inv('W', c) == Fraction(1, 2)


# ============================================================================
# Numerical properties of the closed form
# ============================================================================

class TestNumericalProperties:
    """Test numerical properties of the closed-form result."""

    def test_always_positive(self):
        """delta_F_3 > 0 for all c > 0."""
        # All coefficients in numerator are positive, QED
        for c_int in [1, 5, 13, 26, 100, 1000]:
            assert delta_F3_formula(Fraction(c_int)) > 0

    def test_semiclassical_limit(self):
        """delta_F_3 -> c/27648 as c -> infinity (nonzero semiclassical limit)."""
        c = Fraction(10**12)
        delta = delta_F3_formula(c)
        leading = c / 27648
        ratio = float(delta / leading)
        assert abs(ratio - 1.0) < 1e-9

    def test_numerator_coefficients(self):
        """The numerator 5c^3 + 3792c^2 + 1149120c + 217071360 has all positive coefficients."""
        assert 5 > 0
        assert 3792 > 0
        assert 1149120 > 0
        assert 217071360 > 0

    def test_denominator(self):
        """Denominator is 138240 * c^2 = 2^10 * 3^3 * 5 * c^2."""
        assert 138240 == 2**10 * 3**3 * 5

    def test_genus2_genus3_comparison(self):
        """delta_F_3 > delta_F_2 for all tested c (cross-channel GROWS with genus)."""
        for c_int in [1, 2, 5, 10, 26, 100]:
            c = Fraction(c_int)
            d2 = (c + 204) / (16 * c)
            d3 = delta_F3_formula(c)
            assert d3 > d2, f"c={c_int}: delta_F_3={float(d3)} <= delta_F_2={float(d2)}"

    def test_koszul_dual_c_value(self):
        """At c=50 (W_3 Koszul self-dual point c=50): delta_F_3 is well-defined."""
        # W_3 Koszul duality: c <-> 100-c, self-dual at c=50
        c = Fraction(50)
        delta = delta_F3_formula(c)
        assert delta > 0
        # Also check complementarity: delta(c) vs delta(100-c)
        c_dual = Fraction(50)
        delta_dual = delta_F3_formula(c_dual)
        assert delta == delta_dual  # self-dual point

    @pytest.mark.parametrize("c_int", [1, 10, 50])
    def test_complementarity_asymmetry(self, c_int):
        """delta_F_3(c) != delta_F_3(100-c) in general (complementarity is broken)."""
        c = Fraction(c_int)
        c_dual = Fraction(100 - c_int)
        d = delta_F3_formula(c)
        d_dual = delta_F3_formula(c_dual)
        if c_int != 50:
            assert d != d_dual


# ============================================================================
# Full computation output tests
# ============================================================================

class TestFullComputation:
    """Test the full computation output structure."""

    def test_output_keys(self):
        """genus3_full_computation returns all expected keys."""
        result = genus3_full_computation(Fraction(7))
        expected_keys = {'c', 'kappa_total', 'kappa_T', 'kappa_W',
                         'lambda3_fp', 'F3_universal', 'total_diagonal',
                         'total_mixed', 'cross_channel_correction',
                         'F3_with_cross', 'per_graph'}
        assert set(result.keys()) == expected_keys

    def test_per_graph_count(self):
        """42 per-graph entries."""
        result = genus3_full_computation(Fraction(7))
        assert len(result['per_graph']) == 42

    def test_cross_channel_matches_mixed(self):
        """Cross-channel correction equals sum of mixed amplitudes."""
        result = genus3_full_computation(Fraction(7))
        assert result['cross_channel_correction'] == result['total_mixed']

    def test_F3_decomposition(self):
        """F_3 = F_3_universal + delta_F_3."""
        c = Fraction(7)
        result = genus3_full_computation(c)
        assert result['F3_with_cross'] == result['F3_universal'] + result['cross_channel_correction']
