"""
Tests for the Kontsevich graph complex orientation database.

Tests are organized by:
  1. Graph construction and basic invariants
  2. Automorphism group computation
  3. Graph enumeration and counts
  4. Edge contraction
  5. d^2 = 0 verification (the critical test)
  6. Euler characteristic
  7. Cross-checks and consistency
"""

import pytest
from fractions import Fraction
from collections import Counter

from compute.lib.graph_complex_orientation_database import (
    Graph,
    double_banana, dumbbell, theta, triple_banana, k4, k33, petersen,
    enumerate_connected_graphs, enumerate_by_loop_number,
    build_database, graph_count_table,
    contraction_sign, check_d_squared, verify_d_squared,
    differential_targets,
    euler_characteristic,
)


# ============================================================
# 1. Graph construction and basic invariants
# ============================================================

class TestGraphBasics:
    """Test Graph construction, loop number, valence, connectivity."""

    def test_theta_graph_invariants(self):
        g = theta()
        assert g.num_vertices == 2
        assert g.num_edges == 3
        assert g.loop_number == 2  # 3 - 2 + 1
        assert g.valence(0) == 3
        assert g.valence(1) == 3
        assert g.degree_sequence() == (3, 3)
        assert g.is_connected()
        assert g.min_valence() == 3

    def test_dumbbell_invariants(self):
        g = dumbbell()
        assert g.num_vertices == 2
        assert g.num_edges == 3
        assert g.loop_number == 2
        assert g.valence(0) == 3  # self-loop (2) + bridge (1)
        assert g.valence(1) == 3
        assert g.is_connected()

    def test_double_banana_invariants(self):
        g = double_banana()
        assert g.num_vertices == 1
        assert g.num_edges == 2
        assert g.loop_number == 2  # 2 - 1 + 1
        assert g.valence(0) == 4  # two self-loops, each contributing 2
        assert g.is_connected()

    def test_k4_invariants(self):
        g = k4()
        assert g.num_vertices == 4
        assert g.num_edges == 6
        assert g.loop_number == 3  # 6 - 4 + 1
        assert g.degree_sequence() == (3, 3, 3, 3)
        assert g.is_connected()
        assert g.num_self_loops() == 0
        assert g.num_multi_edge_pairs() == 0

    def test_k33_invariants(self):
        g = k33()
        assert g.num_vertices == 6
        assert g.num_edges == 9
        assert g.loop_number == 4  # 9 - 6 + 1
        assert g.degree_sequence() == (3, 3, 3, 3, 3, 3)
        assert g.is_connected()

    def test_petersen_invariants(self):
        g = petersen()
        assert g.num_vertices == 10
        assert g.num_edges == 15
        assert g.loop_number == 6  # 15 - 10 + 1
        assert g.degree_sequence() == (3,) * 10
        assert g.is_connected()

    def test_triple_banana_invariants(self):
        g = triple_banana()
        assert g.num_vertices == 1
        assert g.num_edges == 3
        assert g.loop_number == 3
        assert g.valence(0) == 6

    def test_disconnected_graph(self):
        """Two isolated edges: not connected."""
        g = Graph([0, 1, 2, 3], [(0, 1), (2, 3)])
        assert not g.is_connected()

    def test_self_loop_count(self):
        g = Graph([0, 1], [(0, 0), (0, 0), (0, 1)])
        assert g.num_self_loops() == 2
        assert g.num_multi_edge_pairs() == 1  # two (0,0) edges

    def test_loop_number_formula(self):
        """b_1 = E - V + 1 for connected graphs."""
        for named in [theta(), dumbbell(), double_banana(), k4(), k33()]:
            E = named.num_edges
            V = named.num_vertices
            assert named.loop_number == E - V + 1


# ============================================================
# 2. Automorphism groups
# ============================================================

class TestAutomorphisms:
    """Test automorphism group computation."""

    def test_theta_aut(self):
        """theta: S_3 (edge perms) x Z/2 (vertex swap) = 12."""
        assert theta().automorphism_count() == 12

    def test_dumbbell_aut(self):
        """dumbbell: Z/2 (swap vertices, which swaps the two self-loops)."""
        assert dumbbell().automorphism_count() == 2

    def test_double_banana_aut(self):
        """double banana: 1 vertex, 2 identical self-loops -> 2! = 2."""
        assert double_banana().automorphism_count() == 2

    def test_k4_aut(self):
        """K_4: S_4 acting on vertices, no multi-edges -> 24."""
        assert k4().automorphism_count() == 24

    def test_k33_aut(self):
        """K_{3,3}: (S_3 x S_3) x Z/2 = 72."""
        assert k33().automorphism_count() == 72

    def test_petersen_aut(self):
        """Petersen graph: |Aut| = 120 = S_5."""
        assert petersen().automorphism_count() == 120

    def test_triple_banana_aut(self):
        """V=1, 3 self-loops: 3! = 6."""
        assert triple_banana().automorphism_count() == 6

    def test_single_edge_graph(self):
        """Single edge between 2 vertices: |Aut| = 2 (swap vertices)."""
        g = Graph([0, 1], [(0, 1)])
        assert g.automorphism_count() == 2

    def test_triangle_aut(self):
        """Triangle C_3: |Aut| = 6 = D_3."""
        g = Graph([0, 1, 2], [(0, 1), (1, 2), (0, 2)])
        assert g.automorphism_count() == 6


# ============================================================
# 3. Isomorphism and canonical forms
# ============================================================

class TestIsomorphism:
    """Test canonical forms and isomorphism detection."""

    def test_theta_not_iso_dumbbell(self):
        """theta and dumbbell are NOT isomorphic (different edge structure)."""
        assert not theta().is_isomorphic_to(dumbbell())

    def test_relabeled_k4(self):
        """K_4 with relabeled vertices is isomorphic to K_4."""
        g1 = k4()
        # Relabel: 0->3, 1->2, 2->1, 3->0
        edges = [(3 - a, 3 - b) for (a, b) in g1.edges]
        g2 = Graph([0, 1, 2, 3], edges)
        assert g1.is_isomorphic_to(g2)

    def test_canonical_form_invariant(self):
        """Canonical form is the same for isomorphic graphs."""
        g1 = Graph([0, 1, 2], [(0, 1), (1, 2), (0, 2)])
        g2 = Graph([10, 20, 30], [(10, 20), (20, 30), (10, 30)])
        assert g1.canonical_form() == g2.canonical_form()

    def test_self_isomorphism(self):
        for g in [theta(), dumbbell(), double_banana(), k4()]:
            assert g.is_isomorphic_to(g)

    def test_different_loop_not_iso(self):
        """Graphs with different loop numbers can't be isomorphic."""
        assert not theta().is_isomorphic_to(k4())


# ============================================================
# 4. Edge contraction
# ============================================================

class TestContraction:
    """Test edge contraction behavior."""

    def test_self_loop_contraction(self):
        """Contracting a self-loop just removes it."""
        g = Graph([0], [(0, 0), (0, 0)])
        c = g.contract_edge(0)
        assert c.num_vertices == 1
        assert c.num_edges == 1
        assert c.edges == [(0, 0)]

    def test_bridge_contraction_creates_self_loops(self):
        """Contracting the bridge in theta merges vertices;
        the other 2 parallel edges become self-loops."""
        g = theta()  # edges: [(0,1), (0,1), (0,1)]
        c = g.contract_edge(0)
        assert c.num_vertices == 1
        assert c.num_edges == 2
        # Both remaining edges become self-loops at the merged vertex
        for (a, b) in c.edges:
            assert a == b

    def test_contraction_preserves_loop_number_for_nonloop(self):
        """Contracting a non-loop edge: V decreases by 1, E decreases by 1,
        so loop number is unchanged."""
        g = k4()
        c = g.contract_edge(0)
        assert c.loop_number == g.loop_number

    def test_contraction_decreases_loop_for_selfloop(self):
        """Contracting a self-loop: V unchanged, E decreases by 1,
        so loop number decreases by 1."""
        g = double_banana()  # loop 2
        c = g.contract_edge(0)
        assert c.loop_number == g.loop_number - 1

    def test_dumbbell_contraction_bridge(self):
        """Contracting the bridge in the dumbbell."""
        g = dumbbell()  # edges: [(0,0), (0,1), (1,1)]
        c = g.contract_edge(1)  # contract bridge (0,1)
        assert c.num_vertices == 1
        # The two self-loops remain, plus no new self-loops from bridge
        assert c.num_edges == 2

    def test_k4_contraction_gives_triangle_with_double_edge(self):
        """Contracting one edge of K_4 gives a graph with V=3."""
        g = k4()
        c = g.contract_edge(0)
        assert c.num_vertices == 3
        assert c.num_edges == 5  # 6 - 1 = 5


# ============================================================
# 5. Graph enumeration and counts
# ============================================================

class TestEnumeration:
    """Test graph enumeration counts."""

    def test_loop_1_empty(self):
        """No graphs at loop 1 with min_valence >= 3."""
        db = enumerate_by_loop_number(1, min_valence=3)
        assert len(db[1]) == 0

    def test_loop_2_count(self):
        """Loop 2: exactly 3 graphs (double_banana, dumbbell, theta)."""
        db = enumerate_by_loop_number(2, min_valence=3)
        assert len(db[2]) == 3

    def test_loop_2_contains_theta(self):
        """theta should be among the loop 2 graphs."""
        db = enumerate_by_loop_number(2)
        t = theta()
        found = any(g.is_isomorphic_to(t) for g in db[2])
        assert found

    def test_loop_2_contains_dumbbell(self):
        """dumbbell should be among the loop 2 graphs."""
        db = enumerate_by_loop_number(2)
        d = dumbbell()
        found = any(g.is_isomorphic_to(d) for g in db[2])
        assert found

    def test_loop_2_contains_double_banana(self):
        """double_banana should be among the loop 2 graphs."""
        db = enumerate_by_loop_number(2)
        b = double_banana()
        found = any(g.is_isomorphic_to(b) for g in db[2])
        assert found

    def test_loop_3_count(self):
        """Loop 3: 15 graphs."""
        db = enumerate_by_loop_number(3)
        assert len(db[3]) == 15

    def test_loop_3_contains_k4(self):
        """K_4 has loop 3 and should appear."""
        db = enumerate_by_loop_number(3)
        k = k4()
        found = any(g.is_isomorphic_to(k) for g in db[3])
        assert found

    def test_loop_4_count(self):
        """Loop 4: 111 graphs."""
        db = enumerate_by_loop_number(4)
        assert len(db[4]) == 111

    def test_loop_4_contains_k33(self):
        """K_{3,3} has loop 4 and should appear."""
        db = enumerate_by_loop_number(4)
        k = k33()
        found = any(g.is_isomorphic_to(k) for g in db[4])
        assert found

    def test_enumeration_no_duplicates(self):
        """No two graphs in the enumeration are isomorphic."""
        db = enumerate_by_loop_number(3)
        for loop_num, graphs in db.items():
            canonicals = [g.canonical_form() for g in graphs]
            assert len(canonicals) == len(set(canonicals)), \
                f"Duplicate at loop {loop_num}"

    def test_all_graphs_connected(self):
        """Every enumerated graph is connected."""
        db = enumerate_by_loop_number(3)
        for loop_num, graphs in db.items():
            for g in graphs:
                assert g.is_connected(), f"Disconnected at loop {loop_num}"

    def test_all_graphs_min_valence_3(self):
        """Every enumerated graph has min valence >= 3."""
        db = enumerate_by_loop_number(3)
        for loop_num, graphs in db.items():
            for g in graphs:
                assert g.min_valence() >= 3, f"Low valence at loop {loop_num}"

    def test_loop_2_vertex_distribution(self):
        """Loop 2 graphs: 1 with V=1 (double banana), 2 with V=2."""
        db = enumerate_by_loop_number(2)
        v_counts = Counter(g.num_vertices for g in db[2])
        assert v_counts[1] == 1
        assert v_counts[2] == 2


# ============================================================
# 6. d^2 = 0 verification
# ============================================================

class TestDSquared:
    """Test d^2 = 0 in the edge-oriented graph complex."""

    def test_d_squared_theta(self):
        ok, _, nz = check_d_squared(theta())
        assert ok, f"d^2 != 0 for theta: {nz}"

    def test_d_squared_dumbbell(self):
        ok, _, nz = check_d_squared(dumbbell())
        assert ok, f"d^2 != 0 for dumbbell: {nz}"

    def test_d_squared_double_banana(self):
        ok, _, nz = check_d_squared(double_banana())
        assert ok, f"d^2 != 0 for double_banana: {nz}"

    def test_d_squared_k4(self):
        ok, _, nz = check_d_squared(k4())
        assert ok, f"d^2 != 0 for K4: {nz}"

    def test_d_squared_triple_banana(self):
        ok, _, nz = check_d_squared(triple_banana())
        assert ok, f"d^2 != 0 for triple_banana: {nz}"

    def test_d_squared_k33(self):
        ok, _, nz = check_d_squared(k33())
        assert ok, f"d^2 != 0 for K33: {nz}"

    def test_d_squared_all_loop_2(self):
        """d^2 = 0 for all 3 graphs at loop 2."""
        db = build_database(2)
        for e in db[2]:
            ok, _, nz = check_d_squared(e['graph'])
            assert ok, f"d^2 != 0: graph #{e['index']}"

    def test_d_squared_all_loop_3(self):
        """d^2 = 0 for all 15 graphs at loop 3."""
        db = build_database(3)
        for e in db[3]:
            ok, _, nz = check_d_squared(e['graph'])
            assert ok, f"d^2 != 0: graph #{e['index']}"

    def test_d_squared_all_loop_4(self):
        """d^2 = 0 for all 111 graphs at loop 4."""
        db = build_database(4)
        for e in db[4]:
            ok, _, nz = check_d_squared(e['graph'])
            assert ok, f"d^2 != 0: graph #{e['index']}"

    def test_contraction_sign_alternating(self):
        """Signs alternate: (-1)^0, (-1)^1, (-1)^2, ..."""
        for k in range(10):
            assert contraction_sign(k) == (-1) ** k

    def test_verify_d_squared_report(self):
        """verify_d_squared returns correct report structure."""
        report = verify_d_squared(3)
        assert 1 in report
        assert 2 in report
        assert 3 in report
        assert report[1]['num_graphs'] == 0
        assert report[1]['d2_zero'] is True
        assert report[2]['num_graphs'] == 3
        assert report[2]['d2_zero'] is True
        assert report[3]['num_graphs'] == 15
        assert report[3]['d2_zero'] is True


# ============================================================
# 7. Euler characteristic
# ============================================================

class TestEulerCharacteristic:
    """Test Euler characteristic computation."""

    def test_euler_char_loop_1(self):
        """chi at loop 1 = 0 (no graphs)."""
        chi = euler_characteristic(1)
        assert chi[1] == 0

    def test_euler_char_loop_2(self):
        """chi at loop 2 = sum (-1)^E / |Aut| for 3 graphs.

        double_banana: E=2, |Aut|=2 -> (+1)/2 = 1/2
        dumbbell: E=3, |Aut|=2 -> (-1)/2 = -1/2
        theta: E=3, |Aut|=12 -> (-1)/12
        Total: 1/2 - 1/2 - 1/12 = -1/12
        """
        chi = euler_characteristic(2)
        assert chi[2] == Fraction(-1, 12)

    def test_euler_char_rational(self):
        """Euler characteristic is rational at each loop."""
        chi = euler_characteristic(4)
        for loop_num, val in chi.items():
            assert isinstance(val, Fraction)


# ============================================================
# 8. Differential targets
# ============================================================

class TestDifferentialTargets:
    """Test that differential_targets computes correct boundary."""

    def test_theta_differential(self):
        """Theta graph has 3 edges; contracting any gives a V=1 graph
        with 2 self-loops (the double banana)."""
        g = theta()
        targets = differential_targets(g)
        # All 3 contractions produce the same graph type
        assert len(targets) == 3
        for sign, c in targets:
            assert c.num_vertices == 1
            assert c.num_edges == 2

    def test_double_banana_differential(self):
        """Double banana: 2 self-loops. Contracting each gives V=1, E=1
        (single self-loop, valence 2 < 3). So differential is 0."""
        g = double_banana()
        targets = differential_targets(g, min_valence=3)
        assert len(targets) == 0

    def test_k4_differential_target_count(self):
        """K_4 has 6 edges, each contractible to a valid graph."""
        g = k4()
        targets = differential_targets(g)
        # All 6 contractions produce connected graphs with min val >= 3
        assert len(targets) == 6


# ============================================================
# 9. Half-edge data
# ============================================================

class TestHalfEdges:
    """Test half-edge decomposition."""

    def test_half_edge_count(self):
        """Each edge contributes exactly 2 half-edges."""
        for g in [theta(), dumbbell(), k4()]:
            total_he = sum(len(hes) for hes in g.vertex_half_edges.values())
            assert total_he == 2 * g.num_edges

    def test_half_edge_labels_unique(self):
        """All half-edge labels are distinct."""
        for g in [theta(), dumbbell(), k4(), double_banana()]:
            all_labels = []
            for hes in g.vertex_half_edges.values():
                all_labels.extend(hes)
            assert len(all_labels) == len(set(all_labels))

    def test_self_loop_half_edges_same_vertex(self):
        """For a self-loop (v,v), both half-edges are at vertex v."""
        g = double_banana()
        for e_idx, (hp, hm) in g.half_edges.items():
            v1, v2 = g.edges[e_idx]
            assert v1 == v2 == 0
            assert hp in g.vertex_half_edges[0]
            assert hm in g.vertex_half_edges[0]


# ============================================================
# 10. Database structure
# ============================================================

class TestDatabase:
    """Test database builder output structure."""

    def test_database_keys(self):
        db = build_database(3)
        assert set(db.keys()) == {1, 2, 3}

    def test_entry_fields(self):
        db = build_database(2)
        for e in db[2]:
            assert 'graph' in e
            assert 'index' in e
            assert 'vertices' in e
            assert 'edges' in e
            assert 'loop' in e
            assert 'automorphisms' in e
            assert 'degree_sequence' in e
            assert 'half_edge_data' in e
            assert 'vertex_half_edges' in e
            assert 'canonical_form' in e
            assert 'edge_list' in e
            assert 'num_self_loops' in e
            assert 'num_multi_edges' in e

    def test_loop_consistency(self):
        """Every entry's loop number matches its database key."""
        db = build_database(4)
        for loop_num, entries in db.items():
            for e in entries:
                assert e['loop'] == loop_num

    def test_automorphism_consistency(self):
        """Database automorphism matches graph computation."""
        db = build_database(3)
        for loop_num, entries in db.items():
            for e in entries:
                assert e['automorphisms'] == e['graph'].automorphism_count()


# ============================================================
# 11. Count table
# ============================================================

class TestCountTable:
    """Test graph_count_table output."""

    def test_count_table_values(self):
        table = graph_count_table(4)
        assert table[1]['count'] == 0
        assert table[2]['count'] == 3
        assert table[3]['count'] == 15
        assert table[4]['count'] == 111

    def test_simple_graph_counts(self):
        """Count of simple graphs (no self-loops, no multi-edges)."""
        table = graph_count_table(3)
        # Loop 2: only theta is simple? No: theta has multi-edges.
        # Actually: double_banana has self-loops, dumbbell has self-loops,
        # theta has multi-edges. So 0 simple at loop 2.
        assert table[2]['simple_count'] == 0
        # Loop 3: K_4 is simple. Check how many others.
        assert table[3]['simple_count'] >= 1


# ============================================================
# 12. Cross-checks and consistency
# ============================================================

class TestCrossChecks:
    """Cross-consistency checks."""

    def test_valence_sum_equals_twice_edges(self):
        """For any graph: sum of valences = 2 * |E|."""
        db = build_database(4)
        for loop_num, entries in db.items():
            for e in entries:
                g = e['graph']
                total_val = sum(g.valence(v) for v in g.vertices)
                assert total_val == 2 * g.num_edges

    def test_self_loop_multi_edge_classification(self):
        """Every loop-2 graph is accounted for: 1 double_banana +
        1 dumbbell + 1 theta = 3."""
        db = build_database(2)
        entries = db[2]
        sl_counts = [e['num_self_loops'] for e in entries]
        # double_banana: 2 self-loops; dumbbell: 2 self-loops; theta: 0
        assert sorted(sl_counts) == [0, 2, 2]

    def test_contraction_target_in_database(self):
        """For any graph at loop L, contracting an edge that produces a
        valid graph should yield a graph isomorphic to one in the
        database at loop L (non-loop edge) or loop L-1 (self-loop)."""
        db = build_database(3)
        for loop_num in [2, 3]:
            for e in db[loop_num]:
                g = e['graph']
                for sign, c in differential_targets(g):
                    c_loop = c.loop_number
                    # Find it in the database
                    assert c_loop in db, f"Target loop {c_loop} not in db"
                    found = any(c.is_isomorphic_to(dg) for dg in
                                [ee['graph'] for ee in db[c_loop]])
                    assert found, (
                        f"Contraction target not found in database: "
                        f"loop {c_loop}, {c}")

    def test_euler_char_loop2_independent(self):
        """Verify chi(loop 2) by direct computation from database."""
        db = build_database(2)
        chi = Fraction(0)
        for e in db[2]:
            chi += Fraction((-1) ** e['edges'], e['automorphisms'])
        # double_banana: (-1)^2 / 2 = 1/2
        # dumbbell: (-1)^3 / 2 = -1/2
        # theta: (-1)^3 / 12 = -1/12
        # Total: 1/2 - 1/2 - 1/12 = -1/12
        assert chi == Fraction(-1, 12)

    def test_burnside_counting(self):
        """Burnside check: sum of 1/|Aut(G)| over all G at loop L
        should give a positive rational number (no direct formula to
        check against, but it shouldn't be negative or zero for L >= 2)."""
        db = build_database(4)
        for loop_num in [2, 3, 4]:
            total = sum(Fraction(1, e['automorphisms']) for e in db[loop_num])
            assert total > 0


# ============================================================
# 13. Stress tests (marked slow)
# ============================================================

class TestStress:
    """Heavier tests for thoroughness."""

    def test_d_squared_all_loop_4_individually(self):
        """Individually verify d^2 = 0 for each loop-4 graph."""
        db = build_database(4)
        for e in db[4]:
            g = e['graph']
            ok, _, nz = check_d_squared(g)
            assert ok, (
                f"d^2 != 0 for loop-4 graph #{e['index']}: "
                f"V={g.num_vertices}, E={g.num_edges}, "
                f"deg={g.degree_sequence()}, nonzero={nz}")

    def test_loop_3_simple_subcount(self):
        """At loop 3, exactly 1 simple graph (K_4)."""
        db = build_database(3)
        simple = [e for e in db[3]
                  if e['num_self_loops'] == 0 and e['num_multi_edges'] == 0]
        assert len(simple) == 1
        # And it should be K_4
        assert simple[0]['graph'].is_isomorphic_to(k4())

    def test_loop_4_trivalent_count(self):
        """At loop 4, count graphs where ALL vertices are trivalent."""
        db = build_database(4)
        trivalent = [e for e in db[4]
                     if all(d == 3 for d in e['degree_sequence'])]
        # These are the (3-regular multigraphs at loop 4).
        # At loop 4 with all val=3: 2E = 3V, E = V + 3,
        # so 2(V+3) = 3V => V = 6, E = 9.
        for e in trivalent:
            assert e['vertices'] == 6
            assert e['edges'] == 9

    def test_enumeration_stability(self):
        """Running enumeration twice gives the same count."""
        db1 = enumerate_by_loop_number(3)
        db2 = enumerate_by_loop_number(3)
        for loop in [1, 2, 3]:
            assert len(db1[loop]) == len(db2[loop])
