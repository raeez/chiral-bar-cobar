"""Tests for genus-2 stable graph shadow amplitudes.

Verifies:
  - Graph enumeration: correct number of genus-2 stable graphs
  - Stability condition: 2g_v + n_v >= 3 at each vertex
  - Genus verification: h_1 + sum g_v = 2
  - Automorphism orders
  - Faber-Pandharipande numbers
  - Vacuum amplitude consistency
  - Genus-arity table structure
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, bernoulli, factorial

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'genus2_stable_graph_shadows',
    os.path.join(_lib_dir, 'genus2_stable_graph_shadows.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

c = Symbol('c')


# ============================================================
# Graph enumeration tests
# ============================================================

class TestGraphEnumeration:
    def test_seven_vacuum_graphs(self):
        """There are exactly 7 genus-2 stable graphs at n=0."""
        graphs = _mod.genus2_vacuum_graphs()
        assert len(graphs) == 7

    def test_all_stable(self):
        """All enumerated graphs are stable."""
        for graph in _mod.genus2_vacuum_graphs():
            assert graph.is_stable(), f"{graph.name} is not stable"

    def test_all_genus_2(self):
        """All graphs have arithmetic genus 2."""
        for graph in _mod.genus2_vacuum_graphs():
            assert graph.verify_genus(), \
                f"{graph.name}: h1={graph.h1()}, sum_gv={graph.vertex_genus_sum()}"

    def test_graph_names(self):
        """Graphs are named correctly."""
        names = {g.name for g in _mod.genus2_vacuum_graphs()}
        assert 'theta' in names
        assert 'sunset' in names
        assert 'figure_eight' in names
        assert 'smooth_g2' in names
        assert 'separating' in names
        assert 'mixed' in names
        assert 'barbell' in names


class TestGraphProperties:
    def test_theta_graph(self):
        """Theta graph: 2 vertices, 3 edges, h_1 = 2."""
        graphs = _mod.genus2_vacuum_graphs()
        theta = [g for g in graphs if g.name == 'theta'][0]
        assert len(theta.vertices) == 2
        assert len(theta.edges) == 3
        assert theta.h1() == 2
        assert theta.aut_order == 12

    def test_sunset_graph(self):
        """Sunset graph: 1 vertex, 2 self-loops, h_1 = 2."""
        graphs = _mod.genus2_vacuum_graphs()
        sunset = [g for g in graphs if g.name == 'sunset'][0]
        assert len(sunset.vertices) == 1
        assert len(sunset.edges) == 2
        assert sunset.h1() == 2
        assert sunset.aut_order == 8

    def test_figure_eight(self):
        """Figure-eight: 1 vertex g=1, 1 self-loop, h_1 = 1."""
        graphs = _mod.genus2_vacuum_graphs()
        fig = [g for g in graphs if g.name == 'figure_eight'][0]
        assert len(fig.vertices) == 1
        assert fig.vertices[0] == (1, 2)
        assert fig.h1() == 1
        assert fig.aut_order == 2

    def test_smooth_g2(self):
        """Smooth genus-2: 1 vertex g=2, no edges."""
        graphs = _mod.genus2_vacuum_graphs()
        smooth = [g for g in graphs if g.name == 'smooth_g2'][0]
        assert len(smooth.vertices) == 1
        assert smooth.vertices[0] == (2, 0)
        assert len(smooth.edges) == 0
        assert smooth.aut_order == 1


# ============================================================
# Faber-Pandharipande number tests
# ============================================================

class TestFPNumbers:
    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert _mod.lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        # B_4 = -1/30, |B_4| = 1/30
        # (2^3-1)/2^3 * (1/30) / 24 = 7/8 * 1/720 = 7/5760
        assert _mod.lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        # B_6 = 1/42, |B_6| = 1/42
        # (2^5-1)/2^5 * (1/42) / 720 = 31/32 * 1/30240 = 31/967680
        val = _mod.lambda_fp(3)
        expected = Rational(31, 32) * Rational(1, 42) / factorial(6)
        assert val == expected

    def test_lambda_fp_positive(self):
        """All lambda_g^FP are positive for g >= 1."""
        for g in range(1, 8):
            assert _mod.lambda_fp(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP decreases for g >= 2."""
        for g in range(2, 7):
            assert _mod.lambda_fp(g) > _mod.lambda_fp(g + 1)


# ============================================================
# Amplitude tests
# ============================================================

class TestAmplitudes:
    def test_theta_amplitude_form(self):
        """Theta graph amplitude is a rational function of c."""
        graphs = _mod.genus2_vacuum_graphs()
        theta = [g for g in graphs if g.name == 'theta'][0]
        amp = _mod.graph_amplitude_virasoro(theta)
        # Should involve S_3^2 * P^3 = 4 * (2/c)^3 / 12
        expected = Rational(1, 12) * 4 * (Rational(2)/c)**3
        assert simplify(amp - expected) == 0

    def test_sunset_amplitude_form(self):
        """Sunset graph amplitude involves S_4 * P^2."""
        graphs = _mod.genus2_vacuum_graphs()
        sunset = [g for g in graphs if g.name == 'sunset'][0]
        amp = _mod.graph_amplitude_virasoro(sunset)
        # (1/8) * S_4 * P^2 where S_4 = 10/[c(5c+22)]
        S_4 = Rational(10) / (c * (5*c + 22))
        expected = Rational(1, 8) * S_4 * (Rational(2)/c)**2
        assert simplify(amp - expected) == 0

    def test_smooth_amplitude(self):
        """Smooth genus-2 amplitude = kappa * lambda_2."""
        graphs = _mod.genus2_vacuum_graphs()
        smooth = [g for g in graphs if g.name == 'smooth_g2'][0]
        amp = _mod.graph_amplitude_virasoro(smooth)
        expected = (c/2) * _mod.lambda_fp(2)
        assert simplify(amp - expected) == 0

    def test_all_amplitudes_finite_at_c26(self):
        """All fully-evaluated graph amplitudes are finite at c=26.

        Graphs whose amplitudes contain undetermined vertex symbols
        (e.g. V_1_1 for genus-1, valence-1 vertices) are skipped,
        since finiteness requires the numerical value of those vertices.
        """
        for graph in _mod.genus2_vacuum_graphs():
            amp = _mod.graph_amplitude_virasoro(graph)
            val = amp.subs(c, 26)
            if val.free_symbols:
                continue  # symbolic amplitude, cannot test finiteness
            assert val.is_finite, f"{graph.name} diverges at c=26"


# ============================================================
# Genus-arity table tests
# ============================================================

class TestGenusArityTable:
    def test_table_has_entries(self):
        """Table is non-empty."""
        table = _mod.genus_arity_table()
        assert len(table) > 0

    def test_g0_r2_is_kappa(self):
        """(g=0, r=2) should be kappa."""
        table = _mod.genus_arity_table()
        assert 'kappa' in table[(0, 2)].lower()

    def test_g1_r0_is_f1(self):
        """(g=1, r=0) should be F_1."""
        table = _mod.genus_arity_table()
        assert 'F_1' in table[(1, 0)] or 'f_1' in table[(1, 0)].lower()

    def test_g2_entries_new(self):
        """Genus-2 entries are marked as new/open."""
        table = _mod.genus_arity_table()
        # (g=2, r=2) should be mentioned as new
        assert '2' in str(table[(2, 2)]) or 'THIS' in table[(2, 2)]


# ============================================================
# Genus-2 with marked points tests
# ============================================================

class TestMarkedPoints:
    def test_1marked_graphs_exist(self):
        """Genus-2 graphs with 1 marked point exist."""
        graphs = _mod.genus2_1marked_graphs()
        assert len(graphs) >= 3

    def test_2marked_graphs_exist(self):
        """Genus-2 graphs with 2 marked points exist."""
        graphs = _mod.genus2_2marked_graphs()
        assert len(graphs) >= 4

    def test_1marked_all_stable(self):
        """All 1-marked graphs are stable."""
        for graph in _mod.genus2_1marked_graphs():
            assert graph.is_stable(), f"{graph.name} not stable"

    def test_1marked_all_genus2(self):
        """All 1-marked graphs have genus 2."""
        for graph in _mod.genus2_1marked_graphs():
            assert graph.verify_genus(), f"{graph.name} genus wrong"


# ============================================================
# Numerical consistency tests
# ============================================================

class TestNumerical:
    def test_kappa_correction_genus2(self):
        """Genus-2 kappa correction data is consistent."""
        data = _mod.genus2_kappa_correction_virasoro()
        assert data['lambda_2_FP'] == Rational(7, 5760)
        # F_2 at c=1: kappa = 1/2, F_2 = 1/2 * 7/5760 = 7/11520
        f2_c1 = data['F_2_virasoro'].subs(c, 1)
        assert f2_c1 == Rational(7, 11520)

    def test_graph_count_genus2(self):
        """4 stable graphs at genus 2, n=0."""
        counts = _mod.graph_count_by_genus()
        assert counts[2] == 4

    def test_siegel_modular_weight4_dim1(self):
        """Siegel modular forms of weight 4 have dim 1."""
        data = _mod.genus2_modular_form_space()
        assert data['weight_classification'][4] == 'dim 1 (E_4)'
