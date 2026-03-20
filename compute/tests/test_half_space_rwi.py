"""Tests for the half-space reflected weight identity (RWI) module.

Investigates conj:quadratic-rwi and conj:cubic-rwi from Vol II
(affine_half_space_bv.tex).

Ground truth:
  - Jet order <= 1 (affine): PROVED (thm:affine-half-space-bv)
  - Jet order 2 (quadratic): OPEN (conj:quadratic-rwi)
  - Jet order 3 (cubic): OPEN (conj:cubic-rwi)
  - Valence-shift argument: excess = jet_order - 1 per vertex
  - Lollipop-triangle cancellation needed at jet order 3
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.half_space_rwi import (
    PVAGenerator, PVA,
    affine_pva, betagamma_pva, virasoro_pva, w3_pva, free_boson_pva,
    config_space_dim, form_degree, form_degree_excess,
    valence_shift_excess, affine_one_loop_excess, quadratic_one_loop_excess,
    single_insertion_graphs_jet2, delta2_vanishes_by_valence_shift,
    delta2_analysis,
    lollipop_graph, reflected_triangle_graph,
    delta3_graph_analysis, delta3_cancellation_test,
    jet_order_tower, standard_landscape_rwi_analysis,
    kontsevich_weight_mc, rwi_status_summary,
    HalfSpaceGraph,
    bulk_propagator_form, reflected_propagator, self_image_propagator,
)


# ===========================================================================
# PVA framework tests
# ===========================================================================

class TestPVAGenerators:
    def test_heisenberg_generator(self):
        """Free boson J has conformal weight 1."""
        pva = free_boson_pva()
        assert pva.generators[0].weight == Rational(1)
        assert pva.generators[0].name == "J"

    def test_betagamma_weights(self):
        """Beta-gamma generators have complementary weights."""
        pva = betagamma_pva(Rational(1, 2))
        assert pva.generators[0].weight == Rational(1, 2)
        assert pva.generators[1].weight == Rational(1, 2)

    def test_virasoro_weight(self):
        """Virasoro generator L has conformal weight 2."""
        pva = virasoro_pva()
        assert pva.generators[0].weight == Rational(2)

    def test_w3_generators(self):
        """W_3 has two generators: L (weight 2) and W (weight 3)."""
        pva = w3_pva()
        assert len(pva.generators) == 2
        assert pva.generators[0].weight == Rational(2)
        assert pva.generators[1].weight == Rational(3)


class TestPVAJetOrder:
    def test_heisenberg_jet_order_0(self):
        """Heisenberg PVA has jet order 0 (constant brackets)."""
        pva = free_boson_pva()
        assert pva.jet_order == 0

    def test_betagamma_jet_order_0(self):
        """Beta-gamma PVA has jet order 0 (constant brackets)."""
        pva = betagamma_pva()
        assert pva.jet_order == 0

    def test_affine_jet_order_1(self):
        """Affine PVA has jet order 1 (linear in fields)."""
        pva = affine_pva("sl2")
        assert pva.jet_order == 1

    def test_virasoro_jet_order_1(self):
        """Virasoro PVA: jet order 1 in field degree."""
        pva = virasoro_pva()
        assert pva.jet_order == 1

    def test_w3_jet_order_2(self):
        """W_3 PVA has jet order 2 (W-W bracket is quadratic in L)."""
        pva = w3_pva()
        assert pva.jet_order == 2


class TestPVABrackets:
    def test_heisenberg_pole_order(self):
        """Heisenberg has max pole order 1 (simple pole)."""
        pva = free_boson_pva()
        assert pva.max_pole_order == 1

    def test_affine_has_structure_constants(self):
        """Affine sl_2 has nonzero structure constants at pole 0, jet 1."""
        pva = affine_pva("sl2")
        # [e, f] = h: coefficient of h in pi^{02}_{0,1}
        bracket_ef = pva.get_bracket(0, 2, 0, 1)
        assert bracket_ef is not None
        assert bracket_ef[1] == Rational(1)  # h component

    def test_virasoro_central_charge(self):
        """Virasoro has c/12 at pole order 3."""
        c = Symbol('c')
        pva = virasoro_pva(c)
        cc = pva.get_bracket(0, 0, 3, 0)
        assert cc == c / 12


# ===========================================================================
# Configuration space dimension tests
# ===========================================================================

class TestConfigSpaceDim:
    def test_single_bulk_point(self):
        """Single bulk point: dim = 0 (modulo translations+dilation)."""
        assert config_space_dim(1, 0) == 0

    def test_two_bulk_points(self):
        """Two bulk points: dim = 3 (3*2 - 3)."""
        assert config_space_dim(2, 0) == 3

    def test_three_bulk_points(self):
        """Three bulk points: dim = 6."""
        assert config_space_dim(3, 0) == 6

    def test_one_boundary_one_bulk(self):
        """One bulk + one boundary: dim = 2 (3 + 2 - 3)."""
        assert config_space_dim(1, 1) == 2

    def test_two_boundary(self):
        """Two boundary points: dim = 1 (0 + 4 - 3)."""
        assert config_space_dim(0, 2) == 1


# ===========================================================================
# Valence-shift analysis (conj:quadratic-rwi)
# ===========================================================================

class TestValenceShift:
    def test_affine_excess_zero(self):
        """Affine vertex (jet 1): valence-shift excess = 0."""
        assert valence_shift_excess(1) == 0

    def test_quadratic_excess_one(self):
        """Quadratic vertex (jet 2): valence-shift excess = 1."""
        assert valence_shift_excess(2) == 1

    def test_cubic_excess_two(self):
        """Cubic vertex (jet 3): valence-shift excess = 2."""
        assert valence_shift_excess(3) == 2

    def test_constant_excess_minus_one(self):
        """Constant vertex (jet 0): valence-shift excess = -1."""
        assert valence_shift_excess(0) == -1

    def test_general_excess(self):
        """General jet order N: excess = N - 1."""
        for N in range(0, 10):
            assert valence_shift_excess(N) == N - 1


class TestDelta2VanishingByValenceShift:
    def test_heisenberg_trivial(self):
        """Heisenberg: jet order 0, delta_2 = 0 trivially."""
        pva = free_boson_pva()
        result = delta2_vanishes_by_valence_shift(pva)
        assert result['vanishes'] is True

    def test_betagamma_trivial(self):
        """Beta-gamma: jet order 0, delta_2 = 0 trivially."""
        pva = betagamma_pva()
        result = delta2_vanishes_by_valence_shift(pva)
        assert result['vanishes'] is True

    def test_affine_trivial(self):
        """Affine: jet order 1, delta_2 = 0 trivially (no quadratic terms)."""
        pva = affine_pva("sl2")
        result = delta2_vanishes_by_valence_shift(pva)
        assert result['vanishes'] is True


class TestDelta2FullAnalysis:
    def test_virasoro_delta2_vanishes(self):
        """Virasoro: delta_2 vanishes (jet order 1, no quadratic terms)."""
        pva = virasoro_pva()
        result = delta2_analysis(pva)
        assert result['delta2_vanishes'] is True

    def test_w3_delta2_vanishes(self):
        """W_3: delta_2 vanishes (Dolgushev or known quantization)."""
        pva = w3_pva()
        result = delta2_analysis(pva)
        assert result['delta2_vanishes'] is True

    def test_heisenberg_delta2_vanishes(self):
        """Heisenberg: delta_2 vanishes trivially."""
        pva = free_boson_pva()
        result = delta2_analysis(pva)
        assert result['delta2_vanishes'] is True

    def test_affine_delta2_mechanism(self):
        """Affine: delta_2 vanishes by jet order < 2."""
        pva = affine_pva("sl2")
        result = delta2_analysis(pva)
        assert result['delta2_vanishes'] is True
        assert result['mechanism'] == 'valence_shift'

    def test_betagamma_delta2_vanishes(self):
        """Beta-gamma: delta_2 vanishes trivially."""
        pva = betagamma_pva()
        result = delta2_analysis(pva)
        assert result['delta2_vanishes'] is True


# ===========================================================================
# Graph combinatorics for jet order 2
# ===========================================================================

class TestJet2Graphs:
    def test_single_insertion_graph_count(self):
        """At least 3 graph types at jet order 2."""
        graphs = single_insertion_graphs_jet2()
        assert len(graphs) >= 3

    def test_self_loop_excess(self):
        """Quadratic self-loop: form-degree excess > 0 (degree vanishing)."""
        g = single_insertion_graphs_jet2()[0]
        assert g.name == "quad_self_loop"
        excess = form_degree_excess(g)
        # Single bulk vertex: dim = 0, 1 edge: form_degree = 1
        assert excess == 1

    def test_quad_affine_loop(self):
        """Quadratic + affine loop: check excess."""
        g = single_insertion_graphs_jet2()[1]
        assert g.name == "quad_affine_loop"
        excess = form_degree_excess(g)
        # 2 bulk vertices: dim = 3, 2 edges: form_degree = 2
        # excess = 2 - 3 = -1
        assert excess == -1

    def test_total_jet_order(self):
        """Single-insertion graphs have correct total jet order."""
        for g in single_insertion_graphs_jet2():
            # All have at least one vertex with jet order 2
            has_quad = any(v['jet_order'] == 2 for v in g.vertices)
            assert has_quad


# ===========================================================================
# delta_3: cubic correction (conj:cubic-rwi)
# ===========================================================================

class TestDelta3GraphAnalysis:
    def test_lollipop_structure(self):
        """Lollipop graph has correct structure."""
        g = lollipop_graph()
        assert g.n_vertices == 2  # cubic vertex + boundary
        assert any(v['jet_order'] == 3 for v in g.vertices)

    def test_reflected_triangle_structure(self):
        """Reflected triangle has cubic + affine vertices."""
        g = reflected_triangle_graph()
        jet_orders = sorted(v['jet_order'] for v in g.vertices
                           if v['type'] == 'bulk')
        assert 3 in jet_orders
        assert 1 in jet_orders

    def test_cancellation_needed(self):
        """At jet order 3, cancellation is needed (valence shift alone insufficient)."""
        analysis = delta3_graph_analysis()
        assert analysis['cancellation_needed'] is True

    def test_lollipop_excess(self):
        """Lollipop excess computation."""
        analysis = delta3_graph_analysis()
        # Check that lollipop data is populated
        assert 'excess' in analysis['lollipop']

    def test_reflected_triangle_excess(self):
        """Reflected triangle excess computation."""
        analysis = delta3_graph_analysis()
        assert 'excess' in analysis['reflected_triangle']


class TestDelta3Cancellation:
    def test_low_jet_order_trivial(self):
        """PVAs with jet order < 3: delta_3 = 0 trivially."""
        for pva in [free_boson_pva(), betagamma_pva(), affine_pva("sl2")]:
            result = delta3_cancellation_test(pva)
            assert result['trivially_zero'] is True

    def test_virasoro_delta3_trivial(self):
        """Virasoro (jet order 1): delta_3 = 0 trivially."""
        pva = virasoro_pva()
        result = delta3_cancellation_test(pva)
        assert result['trivially_zero'] is True

    def test_w3_delta3_trivial(self):
        """W_3: delta_3 vanishes trivially (jet order 2 < 3)."""
        pva = w3_pva()
        result = delta3_cancellation_test(pva)
        assert result['delta3_vanishes'] is True
        assert result['trivially_zero'] is True


# ===========================================================================
# Jet-order tower analysis
# ===========================================================================

class TestJetOrderTower:
    def test_heisenberg_empty_tower(self):
        """Heisenberg has no corrections (jet order 0)."""
        pva = free_boson_pva()
        result = jet_order_tower(pva)
        assert len(result['tower']) == 0

    def test_affine_empty_tower(self):
        """Affine has no corrections beyond jet order 1."""
        pva = affine_pva("sl2")
        result = jet_order_tower(pva)
        assert len(result['tower']) == 0

    def test_w3_tower_has_order_2(self):
        """W_3 tower includes delta_2."""
        pva = w3_pva()
        result = jet_order_tower(pva)
        assert 2 in result['tower']

    def test_w3_delta2_vanishes_by_valence(self):
        """W_3: delta_2 vanishes by valence-shift excess."""
        pva = w3_pva()
        result = jet_order_tower(pva)
        assert result['tower'][2]['vanishes_by_valence_shift'] is True


# ===========================================================================
# Standard landscape analysis
# ===========================================================================

class TestStandardLandscape:
    def test_all_families_delta2_vanishes(self):
        """delta_2 vanishes for all standard PVA families."""
        results = standard_landscape_rwi_analysis()
        for name, data in results.items():
            assert data['delta2']['delta2_vanishes'] is True, \
                f"delta_2 fails for {name}"

    def test_all_families_delta3_vanishes(self):
        """delta_3 vanishes for all standard PVA families."""
        results = standard_landscape_rwi_analysis()
        for name, data in results.items():
            assert data['delta3']['delta3_vanishes'] is True, \
                f"delta_3 fails for {name}"

    def test_jet_order_classification(self):
        """Standard families have correct jet orders."""
        results = standard_landscape_rwi_analysis()
        assert results['Heisenberg']['jet_order'] == 0
        assert results['betagamma']['jet_order'] == 0
        assert results['affine_sl2']['jet_order'] == 1
        assert results['Virasoro']['jet_order'] == 1
        assert results['W3']['jet_order'] == 2


# ===========================================================================
# Propagator tests
# ===========================================================================

class TestPropagator:
    def test_reflected_propagator_symmetry(self):
        """Reflected propagator at t=0 is 2x the bulk propagator."""
        z1 = 1 + 1j
        z2 = 2 + 0.5j
        # At t1 = t2 = 0 (boundary), the image coincides with the point
        # so K^refl = K + K = 2K... but actually t > 0 for bulk points.
        # Test: K^refl(z,t; z',t) = K(z,t;z',t) + K(z,t;conj(z'),-t)
        t = 0.5
        k_refl = reflected_propagator(z1, t, z2, t)
        k_bulk = bulk_propagator_form(z1, t, z2, t)
        k_image = bulk_propagator_form(z1, t, z2.conjugate(), -t)
        assert abs(k_refl - k_bulk - k_image) < 1e-10

    def test_self_image_diverges_on_real_axis(self):
        """Self-image propagator diverges when z is real (Im(z) = 0)."""
        z = complex(1.0, 0.0)
        result = self_image_propagator(z, 1.0)
        assert result == float('inf')

    def test_self_image_finite_off_real(self):
        """Self-image propagator is finite when Im(z) != 0."""
        z = complex(1.0, 0.5)
        result = self_image_propagator(z, 1.0)
        assert abs(result) < float('inf')


# ===========================================================================
# Monte Carlo weight checks
# ===========================================================================

class TestMCWeights:
    def test_excess_positive_gives_zero(self):
        """Graphs with positive form-degree excess have weight = 0."""
        g = single_insertion_graphs_jet2()[0]  # self-loop, excess > 0
        if form_degree_excess(g) > 0:
            result = kontsevich_weight_mc(g)
            assert result['exact_zero'] is True
            assert result['weight'] == 0.0


# ===========================================================================
# Status and broken reference detection
# ===========================================================================

class TestStatus:
    def test_affine_proved(self):
        """Affine case is proved."""
        status = rwi_status_summary()
        assert 'PROVED' in status['jet_order_1']

    def test_quadratic_open(self):
        """Quadratic case is OPEN."""
        status = rwi_status_summary()
        assert 'OPEN' in status['jet_order_2']

    def test_cubic_open(self):
        """Cubic case is OPEN."""
        status = rwi_status_summary()
        assert 'OPEN' in status['jet_order_3']

    def test_broken_ref_detected(self):
        """Detect the broken reference thm:quadratic-rwi."""
        status = rwi_status_summary()
        assert 'broken_ref' in status
        assert 'thm:quadratic-rwi' in status['broken_ref']

    def test_jet_order_hierarchy(self):
        """Jet order hierarchy: 0 trivial, 1 proved, >=2 open."""
        status = rwi_status_summary()
        assert 'TRIVIAL' in status['jet_order_0']
        assert 'PROVED' in status['jet_order_1']
        assert 'OPEN' in status['jet_order_2']
        assert 'OPEN' in status['jet_order_3']


# ===========================================================================
# Dimensional counting cross-checks
# ===========================================================================

class TestDimensionalCounting:
    def test_affine_one_loop_single_vertex(self):
        """Single affine vertex self-loop: excess = 1 (vanishes)."""
        assert affine_one_loop_excess(1) == 1

    def test_affine_one_loop_two_vertices(self):
        """Two affine vertices in a loop: excess = -1."""
        assert affine_one_loop_excess(2) == -1

    def test_affine_one_loop_three_vertices(self):
        """Three affine vertices in a loop: excess = -3."""
        assert affine_one_loop_excess(3) == -3

    def test_quadratic_one_loop_single(self):
        """Single quadratic vertex self-loop: excess = 2 (vanishes strongly)."""
        assert quadratic_one_loop_excess(0, 1) == 2

    def test_quadratic_one_loop_mixed(self):
        """One quadratic + one affine in loop: excess = 0 (marginal)."""
        assert quadratic_one_loop_excess(1, 1) == 0

    def test_valence_shift_monotone(self):
        """Valence-shift excess increases with jet order."""
        for j in range(1, 10):
            assert valence_shift_excess(j + 1) > valence_shift_excess(j)
