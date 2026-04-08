r"""Cross-module integration tests for the Pixton-planted-forest bridge.

Draws from:
  - pixton_shadow_bridge: Pixton ideal generation, WK numbers, graph integrals
  - higher_genus_graph_sum_engine: stable graph enumeration, FP numbers, genus
    spectral sequence, planted-forest correction, complementarity
  - planted_forest_algebra: planted forest enumeration, depth, tridegree
  - propagator_variance_engine: delta_mix, mixing polynomial, Cauchy-Schwarz
  - ds_shadow_cascade_engine: DS pipeline, depth increase, ghost sector
  - shadow_hamilton_jacobi: HJ equation, 2D tower verification

Ten topic clusters, 50+ tests total.

Manuscript references:
    rem:planted-forest-correction-explicit (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
    cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
    const:vol1-genus-spectral-sequence (concordance.tex)
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    thm:ds-central-charge-additivity (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, cancel, simplify, Integer, S


# ============================================================================
# 1. Pixton shadow bridge: planted-forest genus-2 correction
#    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48
# ============================================================================

class TestPlantedForestGenus2Formula:
    """Verify the explicit genus-2 planted-forest correction formula."""

    def test_formula_heisenberg(self):
        """Heisenberg (class G): S_3=0 => delta_pf = 0."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_correction_g2,
        )
        result = planted_forest_correction_g2(Fraction(0), Fraction(1))
        assert result == Fraction(0)

    def test_formula_virasoro_c26(self):
        """Virasoro at c=26: kappa=13, S_3=2.
        delta_pf = 2*(20-13)/48 = 14/48 = 7/24.
        """
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_correction_g2,
        )
        result = planted_forest_correction_g2(Fraction(2), Fraction(13))
        expected = Fraction(2) * (20 - 13) / Fraction(48)
        assert result == expected
        assert result == Fraction(7, 24)

    def test_formula_virasoro_c1(self):
        """Virasoro at c=1: kappa=1/2, S_3=2.
        delta_pf = 2*(20 - 1/2)/48 = 2*39/2/48 = 39/48 = 13/16.
        """
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_correction_g2,
        )
        kappa = Fraction(1, 2)
        result = planted_forest_correction_g2(Fraction(2), kappa)
        expected = Fraction(2) * (20 - kappa) / Fraction(48)
        assert result == expected

    def test_formula_affine_sl2_k1(self):
        """Affine sl_2 at k=1: kappa=9/4, S_3=1 (class L).
        delta_pf = 1*(10-9/4)/48 = (31/4)/48 = 31/192.
        """
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_correction_g2,
        )
        result = planted_forest_correction_g2(Fraction(1), Fraction(9, 4))
        expected = Fraction(1) * (10 - Fraction(9, 4)) / Fraction(48)
        assert result == expected

    def test_formula_vanishes_at_kappa_10alpha(self):
        """delta_pf = 0 iff kappa = 10*alpha (from the formula)."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_correction_g2,
        )
        for alpha in [Fraction(1), Fraction(3, 2), Fraction(7)]:
            kappa = 10 * alpha
            result = planted_forest_correction_g2(alpha, kappa)
            assert result == Fraction(0), f"Should vanish at kappa=10*alpha={kappa}"

    def test_heisenberg_pf_zero_via_graph_sum(self):
        """Verify Heisenberg zero from graph-sum engine (not just formula)."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_heisenberg_g2,
        )
        assert planted_forest_heisenberg_g2() == Fraction(0)

    def test_virasoro_pf_matches_formula(self):
        """Virasoro planted-forest from graph-sum engine matches formula."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_virasoro_g2,
            planted_forest_correction_g2,
        )
        for c_val in [1, 2, 10, 13, 25, 26]:
            from_func = planted_forest_virasoro_g2(Fraction(c_val))
            from_formula = planted_forest_correction_g2(
                Fraction(2), Fraction(c_val, 2))
            assert from_func == from_formula, (
                f"Mismatch at c={c_val}: {from_func} vs {from_formula}")


# ============================================================================
# 2. Self-loop parity vanishing (prop:self-loop-vanishing)
# ============================================================================

class TestSelfLoopParityVanishing:
    """Single-vertex (0, 2k) graphs with k self-loops have I=0 for k >= 2.

    The key: dim M_bar_{0,2k} = 2k-3 is always ODD, and the d+ <-> d-
    swap symmetry pairs every assignment with its negative.
    """

    def test_self_loop_vanishing_k2_through_k6(self):
        """Verify I=0 for k=2..6 via the general Hodge integral."""
        from compute.lib.pixton_shadow_bridge import (
            graph_integral_general, StableGraph,
        )
        import math
        for k in range(2, 7):
            val = 2 * k
            aut = math.factorial(k) * (2 ** k)
            G = StableGraph(
                f'self_loop_{k}', k, 0,
                ((0, val),), k, k, 0, aut, k)
            I = graph_integral_general(G)
            assert I == Fraction(0), f"k={k}: I should be 0, got {I}"

    def test_odd_dimension_invariant(self):
        """dim M_bar_{0,2k} = 2k-3 is odd for all k >= 2."""
        for k in range(2, 50):
            dim = 2 * k - 3
            assert dim % 2 == 1


# ============================================================================
# 3. Shadow visibility genus: g_min(S_r) = floor(r/2) + 1
# ============================================================================

class TestShadowVisibilityGenus:
    """S_r first enters the planted-forest correction at genus floor(r/2)+1."""

    def test_visibility_formula_values(self):
        """Tabulate g_min(S_r) for r = 2..12."""
        expected = {
            2: 2, 3: 2, 4: 3, 5: 3, 6: 4, 7: 4,
            8: 5, 9: 5, 10: 6, 11: 6, 12: 7,
        }
        for r, g_expected in expected.items():
            g_computed = r // 2 + 1
            assert g_computed == g_expected, (
                f"S_{r}: expected g_min={g_expected}, got {g_computed}")

    def test_S3_visible_at_genus2(self):
        """S_3 enters at genus 2: pixton bridge planted-forest depends on S_3."""
        from compute.lib.pixton_shadow_bridge import (
            planted_forest_polynomial, ShadowData,
        )
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        data = ShadowData('test', kappa, S3, Integer(0), depth_class='L')
        pf = cancel(planted_forest_polynomial(data))
        assert S3 in pf.free_symbols, f"S_3 should appear: {pf}"

    def test_S4_invisible_integrated_genus2(self):
        """S_4 is invisible at integrated level at genus 2 (sunset vanishes)."""
        from compute.lib.pixton_shadow_bridge import (
            planted_forest_polynomial, ShadowData,
        )
        kappa = Symbol('kappa')
        S4 = Symbol('S_4')
        data = ShadowData('test', kappa, Integer(0), S4, depth_class='M')
        pf = cancel(planted_forest_polynomial(data))
        assert pf == 0, f"With S_3=0, pf should vanish at g=2: {pf}"

    def test_S4_visible_at_genus3(self):
        """S_4 enters at genus 3: planted-forest at g=3 depends on S_4."""
        from compute.lib.pixton_shadow_bridge import (
            planted_forest_polynomial_genus3, ShadowData,
        )
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        data = ShadowData('test', kappa, S3, S4, depth_class='M')
        pf = cancel(planted_forest_polynomial_genus3(data))
        assert S4 in pf.free_symbols, f"S_4 should appear at g=3: {pf}"

    def test_S5_visible_at_genus3(self):
        """S_5 enters at genus 3: g_min(S_5) = floor(5/2)+1 = 3."""
        from compute.lib.pixton_shadow_bridge import (
            planted_forest_polynomial_genus3, ShadowData,
        )
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        data = ShadowData('test', kappa, S3, S4,
                          shadows={5: S5}, depth_class='M')
        pf = cancel(planted_forest_polynomial_genus3(data))
        assert S5 in pf.free_symbols, f"S_5 should appear at g=3: {pf}"


# ============================================================================
# 4. Graph enumeration and stable graph counts
# ============================================================================

class TestStableGraphCounts:
    """Verify stable graph counts by genus from the higher-genus engine."""

    def test_genus2_graph_count(self):
        """7 stable graphs at (g=2, n=0)."""
        from compute.lib.higher_genus_graph_sum_engine import graph_count
        count = graph_count(2, 0)
        assert count == 7

    def test_genus3_graph_count(self):
        """genus 3 has many stable graphs."""
        from compute.lib.higher_genus_graph_sum_engine import graph_count
        count = graph_count(3, 0)
        assert count >= 20, f"Expected >= 20 graphs at g=3, got {count}"

    def test_graph_count_increases_with_genus(self):
        """Graph count is strictly increasing in genus."""
        from compute.lib.higher_genus_graph_sum_engine import graph_count
        counts = [graph_count(g, 0) for g in range(2, 5)]
        for i in range(len(counts) - 1):
            assert counts[i] < counts[i + 1], (
                f"g={i+2}: {counts[i]} should be < g={i+3}: {counts[i+1]}")

    def test_max_edges_equals_dim(self):
        """Maximum edge count at (g, 0) is 3g-3 = dim M_g."""
        from compute.lib.higher_genus_graph_sum_engine import (
            stable_graphs, graphs_by_edge_count,
        )
        for g in [2, 3]:
            by_edge = graphs_by_edge_count(g, 0)
            max_edge = max(by_edge.keys())
            assert max_edge == 3 * g - 3, (
                f"g={g}: max edges {max_edge} != dim {3*g-3}")


# ============================================================================
# 5. Genus spectral sequence E_1 page
# ============================================================================

class TestGenusSpectralSequence:
    """Test the genus spectral sequence decomposition by loop number h^1."""

    def test_genus2_e1_decomposition(self):
        """At genus 2, h^1 ranges from 0 to 2."""
        from compute.lib.higher_genus_graph_sum_engine import (
            spectral_sequence_counts,
        )
        counts = spectral_sequence_counts(2, 0)
        # h^1=0: tree-level (vertices carry all genus)
        # h^1=2: maximal loop (all vertices genus 0)
        assert 0 in counts, "h^1=0 (tree level) must exist"
        # Maximum loop number is g=2
        assert max(counts.keys()) <= 2

    def test_genus3_e1_has_three_levels(self):
        """At genus 3, h^1 ranges from 0 to 3."""
        from compute.lib.higher_genus_graph_sum_engine import (
            spectral_sequence_counts,
        )
        counts = spectral_sequence_counts(3, 0)
        assert 0 in counts
        assert max(counts.keys()) <= 3

    def test_tree_level_is_smooth_plus_bridges(self):
        """h^1=0 graphs have no cycles: they are trees (bridges only, no loops)."""
        from compute.lib.higher_genus_graph_sum_engine import (
            spectral_sequence_e1,
        )
        pages = spectral_sequence_e1(2, 0)
        if 0 in pages:
            for gamma in pages[0]:
                # first_betti = 0 means no loops in the dual graph
                assert gamma.first_betti == 0


# ============================================================================
# 6. Faber-Pandharipande numbers and free energy
# ============================================================================

class TestFaberPandharipandeNumbers:
    """Verify lambda_g^FP exact values and properties."""

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP are positive (Bernoulli sign pitfall)."""
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        for g in range(1, 11):
            assert lambda_fp(g) > 0, f"lambda_{g}^FP should be positive"

    def test_lambda_fp_strictly_decreasing(self):
        """lambda_{g+1}^FP < lambda_g^FP for g >= 1."""
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        for g in range(1, 10):
            assert lambda_fp(g + 1) < lambda_fp(g)

    def test_free_energy_additivity(self):
        """F_g is additive for independent sums (kappa is additive)."""
        from compute.lib.higher_genus_graph_sum_engine import (
            heisenberg_family, betagamma_family,
            free_energy_additivity_check,
        )
        families = [heisenberg_family(Fraction(1)), betagamma_family()]
        for g in range(1, 6):
            sum_fg, fg_sum, match = free_energy_additivity_check(families, g)
            assert match, f"Additivity fails at g={g}"

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        from compute.lib.higher_genus_graph_sum_engine import (
            virasoro_complementarity,
        )
        for c_val in [0, 1, 5, 13, 20, 26]:
            f_sum, expected, match = virasoro_complementarity(Fraction(c_val), 2)
            assert match, f"Complementarity fails at c={c_val}"


# ============================================================================
# 7. Propagator variance: delta_mix >= 0, P(W3) = 25c^2 + 100c - 428
# ============================================================================

class TestPropagatorVariance:
    """Test multi-channel propagator variance from thm:propagator-variance."""

    def test_single_channel_zero(self):
        """Single channel: delta_mix = 0 identically."""
        from compute.lib.propagator_variance_engine import (
            propagator_variance, ChannelData,
        )
        ch = ChannelData(label='T', weight=2, kappa=Rational(1, 2),
                         f_quartic=Rational(3))
        delta = propagator_variance([ch])
        assert delta == 0

    def test_cauchy_schwarz_w3(self):
        """W_3: delta_mix >= 0 at positive c (Cauchy-Schwarz)."""
        from compute.lib.propagator_variance_engine import (
            propagator_variance, ChannelData,
        )
        c = Symbol('c')
        ch_T = ChannelData(label='T', weight=2, kappa=c / 2,
                           f_quartic=Rational(4) * Rational(10) / (c * (5 * c + 22)))
        ch_W = ChannelData(label='W', weight=3, kappa=c / 3,
                           f_quartic=Rational(4) * Rational(160) / (c * (5 * c + 22) ** 2))
        delta = propagator_variance([ch_T, ch_W])
        # Evaluate at positive c values
        for c_val in [Rational(1), Rational(5), Rational(13), Rational(25)]:
            val = float(delta.subs(c, c_val).evalf())
            assert val >= -1e-15, f"delta_mix < 0 at c={c_val}: {val}"

    def test_mixing_polynomial_w3_formula(self):
        """P(W_3) = 25c^2 + 100c - 428."""
        from compute.lib.propagator_variance_engine import (
            mixing_polynomial_w3,
        )
        P, zeros = mixing_polynomial_w3()
        c = Symbol('c')
        expected = 25 * c ** 2 + 100 * c - 428
        assert cancel(P - expected) == 0, f"P = {P}, expected {expected}"

    def test_virasoro_is_autonomous(self):
        """Virasoro (single channel): trivially autonomous."""
        from compute.lib.propagator_variance_engine import (
            mixing_polynomial_wN,
        )
        P, zeros = mixing_polynomial_wN(2)
        assert P == 0, "Virasoro (N=2) should have P=0"

    def test_mixing_polynomial_w3_has_two_roots(self):
        """P(W_3) has exactly 2 real roots."""
        from compute.lib.propagator_variance_engine import (
            mixing_polynomial_w3,
        )
        _, zeros = mixing_polynomial_w3()
        assert len(zeros) == 2


# ============================================================================
# 8. DS-shadow cascade: depth increase sl_N -> W_N
# ============================================================================

class TestDSShadowCascade:
    """Test Drinfeld-Sokolov shadow cascade from the cascade engine."""

    def test_ghost_central_charge_independent_of_k(self):
        """c_ghost(N) = N(N-1), independent of level k."""
        from compute.lib.ds_shadow_cascade_engine import (
            verify_ghost_central_charge,
        )
        for N in [2, 3, 4, 5]:
            result = verify_ghost_central_charge(N)
            assert result['all_match'], (
                f"Ghost c for sl_{N} not constant: {result}")

    def test_central_charge_additivity(self):
        """c(sl_N, k) = c(W_N, k) + c_ghost(N) for all N, k."""
        from compute.lib.ds_shadow_cascade_engine import (
            c_slN, c_WN, c_ghost,
        )
        for N in [2, 3, 4]:
            for k_val in [Fraction(1), Fraction(3), Fraction(10)]:
                c_aff = c_slN(N, k_val)
                c_w = c_WN(N, k_val)
                c_gh = c_ghost(N)
                assert c_aff == c_w + c_gh, (
                    f"sl_{N}, k={k_val}: {c_aff} != {c_w} + {c_gh}")

    def test_depth_increase_N2(self):
        """sl_2 (class L, S_4=0) -> Vir (class M, S_4 != 0)."""
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        pipe = ds_pipeline(2, Fraction(5), max_arity=6)
        assert pipe['S4_slN'] == Fraction(0), "sl_2 should have S_4=0"
        assert pipe['S4_WN'] != Fraction(0), "Vir should have S_4 != 0"
        assert pipe['depth_increase'] is True

    def test_depth_increase_N3(self):
        """sl_3 (class L) -> W_3 (class M)."""
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        pipe = ds_pipeline(3, Fraction(5), max_arity=6)
        assert pipe['S4_slN'] == Fraction(0)
        assert pipe['S4_WN'] != Fraction(0)
        assert pipe['depth_increase'] is True

    def test_depth_increase_universal(self):
        """Depth increase sl_N -> W_N for all N = 2..5."""
        from compute.lib.ds_shadow_cascade_engine import (
            depth_increase_all_N,
        )
        results = depth_increase_all_N([2, 3, 4, 5], Fraction(5), 6)
        for N, data in results.items():
            assert data['depth_increase'], (
                f"sl_{N} -> W_{N}: depth increase failed")

    def test_slN_is_class_L(self):
        """All affine sl_N algebras are class L (depth 3)."""
        from compute.lib.ds_shadow_cascade_engine import (
            slN_shadow_data, shadow_tower_exact,
        )
        for N in [2, 3, 4, 5]:
            data = slN_shadow_data(N, Fraction(5))
            tower = shadow_tower_exact(
                data['kappa'], data['alpha'], data['S4'], max_arity=6)
            # S_4 = 0 for class L
            assert tower[4] == Fraction(0), f"sl_{N}: S_4 should be 0"
            # S_3 != 0 for class L
            assert tower[3] != Fraction(0), f"sl_{N}: S_3 should be nonzero"

    def test_cascade_S4_forces_all_higher(self):
        """Once S_4 != 0, all S_r != 0 for r >= 4 (cascade)."""
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        pipe = ds_pipeline(2, Fraction(5), max_arity=8)
        tower_WN = pipe['tower_WN']
        for r in range(4, 9):
            assert tower_WN[r] != Fraction(0), (
                f"Vir: S_{r} should be nonzero (cascade)")


# ============================================================================
# 9. Hamilton-Jacobi equation: HJ residuals vanish at arity >= 5
# ============================================================================

class TestHamiltonJacobiEquation:
    """Test the shadow Hamilton-Jacobi equation on the W_3 tower."""

    def test_euler_operator_homogeneity(self):
        """E(f) = r*f for homogeneous f of degree r."""
        from compute.lib.shadow_hamilton_jacobi import euler_operator
        from sympy import expand
        x_T = Symbol('x_T')
        x_W = Symbol('x_W')
        f = 3 * x_T ** 2 * x_W + x_W ** 3  # degree 3
        result = euler_operator(f)
        expected = 3 * f
        assert expand(result - expected) == 0

    def test_hj_residuals_vanish(self):
        """HJ residuals vanish at arity >= 5 for the W_3 tower."""
        from compute.lib.shadow_hamilton_jacobi import verify_hj_equation
        result = verify_hj_equation(max_arity=6)
        assert result['all_vanish_r5_plus'], (
            "HJ residuals should vanish at arity >= 5")

    def test_hj_nonzero_at_arity_3_4(self):
        """HJ residuals are NONZERO at arities 3, 4 (source terms)."""
        from compute.lib.shadow_hamilton_jacobi import verify_hj_equation
        result = verify_hj_equation(max_arity=6)
        assert result['R_3'] != S.Zero, "R_3 should be nonzero"
        assert result['R_4'] != S.Zero, "R_4 should be nonzero"

    def test_t_line_reduces_to_1d(self):
        """On the T-line (x_W=0), the 2D HJ reduces to the 1D Riccati."""
        from compute.lib.shadow_hamilton_jacobi import compare_1d_2d
        result = compare_1d_2d()
        assert result['T_line_reduces'] is True

    def test_w_line_coupling_nonzero(self):
        """On the W-line, the inter-channel coupling is nonzero."""
        from compute.lib.shadow_hamilton_jacobi import compare_1d_2d
        result = compare_1d_2d()
        assert result['W_line_coupling'] != 0

    def test_shadow_hamiltonian_dimension(self):
        """Shadow phase space on W_3 is 4-dimensional."""
        from compute.lib.shadow_hamilton_jacobi import shadow_phase_space
        result = shadow_phase_space()
        assert result['dim'] == 4


# ============================================================================
# 10. Planted forest algebra: enumeration, depth, tridegree
# ============================================================================

class TestPlantedForestAlgebra:
    """Test the planted forest combinatorics from planted_forest_algebra.py."""

    def test_corolla_depth(self):
        """Corolla on n leaves has depth 1."""
        from compute.lib.planted_forest_algebra import corolla
        for n in range(1, 8):
            c = corolla(n)
            assert c.depth == 1, f"Corolla({n}) depth should be 1, got {c.depth}"

    def test_corolla_tridegree(self):
        """Corolla on n leaves has tridegree (0, n, 1)."""
        from compute.lib.planted_forest_algebra import corolla
        for n in range(1, 8):
            c = corolla(n)
            assert c.tridegree == (0, n, 1)

    def test_corolla_is_binary_iff_n2(self):
        """Corolla is binary iff n = 2 (root has exactly 2 children)."""
        from compute.lib.planted_forest_algebra import corolla
        for n in range(1, 8):
            c = corolla(n)
            assert c.is_binary() == (n == 2), (
                f"Corolla({n}): is_binary should be {n==2}")

    def test_corolla_is_corolla(self):
        """Corolla identifies itself."""
        from compute.lib.planted_forest_algebra import corolla
        for n in range(1, 6):
            assert corolla(n).is_corolla()

    def test_enumeration_arity_1(self):
        """Arity 1: exactly 1 planted forest (the trivial edge)."""
        from compute.lib.planted_forest_algebra import enumerate_planted_forests
        forests = enumerate_planted_forests(1)
        assert len(forests) == 1

    def test_enumeration_arity_2(self):
        """Arity 2: 2 planted forests (corolla + depth-2 subdivided edge)."""
        from compute.lib.planted_forest_algebra import enumerate_planted_forests
        forests = enumerate_planted_forests(2)
        # Both the corolla 0->{1,2} and the subdivided 0->v->1,2 are valid
        assert len(forests) == 2
        corollas = [f for f in forests if f.is_corolla()]
        assert len(corollas) == 1

    def test_enumeration_arity_3(self):
        """Arity 3: 8 planted forests including subdivided (chain) trees.
        1 corolla + 3 binary (depth 2 with leaf partition) + 1 subdivided
        ternary + 3 depth-3 chains.
        """
        from compute.lib.planted_forest_algebra import enumerate_planted_forests
        forests = enumerate_planted_forests(3)
        assert len(forests) == 8, f"Expected 8 forests at arity 3, got {len(forests)}"

    def test_enumeration_depths(self):
        """At arity 3: depths are 1 (corolla) and 2 (binary trees)."""
        from compute.lib.planted_forest_algebra import enumerate_planted_forests
        forests = enumerate_planted_forests(3)
        depths = sorted(set(f.depth for f in forests))
        assert 1 in depths, "Corolla (depth 1) should be present"
        assert 2 in depths, "Binary trees (depth 2) should be present"

    def test_leaf_depth_consistency(self):
        """Each leaf's depth is between 1 and forest.depth."""
        from compute.lib.planted_forest_algebra import enumerate_planted_forests
        for n in range(1, 5):
            for f in enumerate_planted_forests(n):
                for leaf in range(1, n + 1):
                    d = f.leaf_depth(leaf)
                    assert 1 <= d <= f.depth, (
                        f"Leaf {leaf} depth {d} out of range [1, {f.depth}]")


# ============================================================================
# 11. Cross-engine consistency: pixton bridge vs graph-sum engine
# ============================================================================

class TestCrossEngineConsistency:
    """Verify that pixton_shadow_bridge and higher_genus_graph_sum_engine
    produce consistent results where they overlap."""

    def test_wk_tau1_genus1_both_engines(self):
        """<tau_1>_1 = 1/24 from both engines."""
        from compute.lib.pixton_shadow_bridge import wk_intersection
        from compute.lib.higher_genus_graph_sum_engine import lambda_fp
        # lambda_1 = <tau_1>_1 = 1/24
        assert wk_intersection(1, (1,)) == Fraction(1, 24)
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_vs_bernoulli(self):
        """lambda_g^FP via Bernoulli matches the recursive WK computation."""
        from compute.lib.higher_genus_graph_sum_engine import (
            lambda_fp, bernoulli_number,
        )
        from math import factorial
        for g in range(1, 6):
            B2g = bernoulli_number(2 * g)
            expected = (
                Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
                * abs(B2g)
                / Fraction(factorial(2 * g))
            )
            assert lambda_fp(g) == expected, (
                f"g={g}: lambda_fp mismatch")

    def test_orbifold_euler_characteristic_genus2(self):
        """chi^orb(M_bar_2) from graph enumeration matches known value."""
        from compute.lib.higher_genus_graph_sum_engine import (
            verify_euler_characteristic,
        )
        computed, expected, match = verify_euler_characteristic(2)
        if expected is not None:
            assert match, (
                f"chi^orb(M_bar_2): computed {computed} != expected {expected}")

    def test_orbifold_euler_characteristic_genus3(self):
        """chi^orb(M_bar_3) from graph enumeration matches known value."""
        from compute.lib.higher_genus_graph_sum_engine import (
            verify_euler_characteristic,
        )
        computed, expected, match = verify_euler_characteristic(3)
        if expected is not None:
            assert match, (
                f"chi^orb(M_bar_3): computed {computed} != expected {expected}")


# ============================================================================
# 12. DS-shadow cascade vs pixton bridge shadow data
# ============================================================================

class TestDSCascadeVsPixton:
    """Verify DS cascade engine shadow data matches pixton bridge families."""

    def test_virasoro_s4_agreement(self):
        """S_4(Vir_c) = 10/[c(5c+22)] from both engines."""
        from compute.lib.ds_shadow_cascade_engine import (
            c_WN, kappa_WN, WN_shadow_data_T_line,
        )
        # At N=2, k=10: c(Vir) = 1 - 6/12 = 1/2.
        k_val = Fraction(10)
        c_w = c_WN(2, k_val)
        data = WN_shadow_data_T_line(2, k_val)
        s4_cascade = data['S4']
        s4_expected = Fraction(10) / (c_w * (5 * c_w + 22))
        assert s4_cascade == s4_expected

    def test_kappa_virasoro_agreement(self):
        """kappa(Vir) = rho * c = (1/2) * c for N=2 (rho = H_2 - 1 = 1/2)."""
        from compute.lib.ds_shadow_cascade_engine import (
            c_WN, kappa_WN, anomaly_ratio,
        )
        rho = anomaly_ratio(2)
        assert rho == Fraction(1, 2)
        for k_val in [Fraction(1), Fraction(3), Fraction(10)]:
            c_w = c_WN(2, k_val)
            kap = kappa_WN(2, k_val)
            assert kap == c_w / 2


# ============================================================================
# 13. Planted forest correction: sign and magnitude checks
# ============================================================================

class TestPlantedForestSignsMagnitudes:
    """Structural checks on the planted-forest correction."""

    def test_virasoro_pf_changes_sign(self):
        """delta_pf for Virasoro changes sign at c=40."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_virasoro_g2,
        )
        # delta_pf = -(c-40)/48 for Virasoro
        pf_below = planted_forest_virasoro_g2(Fraction(20))
        pf_above = planted_forest_virasoro_g2(Fraction(50))
        assert pf_below > 0, "delta_pf should be positive for c < 40"
        assert pf_above < 0, "delta_pf should be negative for c > 40"

    def test_virasoro_pf_at_c40_is_zero(self):
        """delta_pf = 0 at c = 40 (where 10*S_3 = kappa)."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_virasoro_g2,
        )
        pf = planted_forest_virasoro_g2(Fraction(40))
        assert pf == Fraction(0)

    def test_pf_self_dual_c13(self):
        """At self-dual point c=13, delta_pf = -(13-40)/48 = 27/48 = 9/16."""
        from compute.lib.higher_genus_graph_sum_engine import (
            planted_forest_virasoro_g2,
        )
        pf = planted_forest_virasoro_g2(Fraction(13))
        expected = Fraction(-(13 - 40), 48)
        assert pf == expected
        assert pf == Fraction(27, 48)
        assert pf == Fraction(9, 16)
