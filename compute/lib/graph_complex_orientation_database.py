"""
Graph complex orientation database for Kontsevich graph complex GC_n.

Complete enumeration of connected multigraphs with minimum vertex valence >= 3,
organized by loop number (first Betti number b_1 = |E| - |V| + 1).

For each graph, the database records:
  - Automorphism group |Aut(Gamma)|
  - Half-edge decomposition: each edge e = (h_e^+, h_e^-)
  - Canonical orientation (reference edge ordering)
  - Edge contraction differential with signs
  - Verification that d^2 = 0

GRAPH COMPLEX DIFFERENTIAL (edge-oriented, standard GC_n):
  Orientation = ordering of edges, modulo even permutations.
  d(Gamma) = sum_k (-1)^k Gamma/e_k
  d^2 = 0: contracting e_i then e_j cancels with e_j then e_i.

MULTIGRAPH CONVENTIONS:
  - Self-loops allowed (each contributes 2 to vertex valence)
  - Multi-edges allowed
  - Contracting a non-loop edge KEEPS resulting self-loops
  - Contracting a self-loop removes it
  - |Aut(G)| = (vertex perms preserving edge multiset)
                * product of (multiplicity!) for each parallel edge family
"""

from itertools import permutations
from itertools import combinations_with_replacement
from collections import defaultdict, Counter
from fractions import Fraction
import math

try:
    import networkx as nx
    _HAS_NX = True
except ImportError:
    _HAS_NX = False


# ============================================================
# Core data structure
# ============================================================

class Graph:
    """
    A connected multigraph for the Kontsevich graph complex.

    Edges stored as (v1, v2) with v1 <= v2.
    Half-edges: edge i has h^+ = 2i at v1, h^- = 2i+1 at v2.
    """

    def __init__(self, vertices, edges, name=None):
        self.vertices = sorted(vertices)
        self.edges = [(min(a, b), max(a, b)) for (a, b) in edges]
        self.name = name
        self._setup_half_edges()
        self._canonical = None
        self._aut_count = None

    def _setup_half_edges(self):
        self.half_edges = {}
        self.vertex_half_edges = defaultdict(list)
        for i, (v1, v2) in enumerate(self.edges):
            self.half_edges[i] = (2 * i, 2 * i + 1)
            self.vertex_half_edges[v1].append(2 * i)
            self.vertex_half_edges[v2].append(2 * i + 1)

    @property
    def num_vertices(self):
        return len(self.vertices)

    @property
    def num_edges(self):
        return len(self.edges)

    @property
    def loop_number(self):
        return self.num_edges - self.num_vertices + 1

    def valence(self, v):
        count = 0
        for (v1, v2) in self.edges:
            if v1 == v:
                count += 1
            if v2 == v:
                count += 1
        return count

    def min_valence(self):
        if not self.vertices:
            return 0
        return min(self.valence(v) for v in self.vertices)

    def is_connected(self):
        if len(self.vertices) <= 1:
            return True
        adj = defaultdict(set)
        for (v1, v2) in self.edges:
            adj[v1].add(v2)
            adj[v2].add(v1)
        visited = {self.vertices[0]}
        queue = [self.vertices[0]]
        while queue:
            v = queue.pop()
            for w in adj[v]:
                if w not in visited:
                    visited.add(w)
                    queue.append(w)
        return len(visited) == len(self.vertices)

    def degree_sequence(self):
        return tuple(sorted(self.valence(v) for v in self.vertices))

    def _edge_multiset_under(self, label_map):
        out = []
        for (v1, v2) in self.edges:
            a, b = label_map[v1], label_map[v2]
            out.append((min(a, b), max(a, b)))
        return tuple(sorted(out))

    def _color_refinement(self):
        """
        1-WL color refinement: iteratively refine vertex colors based on
        multiset of neighbor colors until stable. Returns a partition of
        vertices into equivalence classes.

        This is O(V * E * iterations) where iterations <= V.
        """
        n = len(self.vertices)
        # Build adjacency with multiplicities
        adj_multi = defaultdict(list)  # v -> list of neighbors (with repeats)
        self_loop_count = defaultdict(int)
        for (v1, v2) in self.edges:
            if v1 == v2:
                self_loop_count[v1] += 1
            else:
                adj_multi[v1].append(v2)
                adj_multi[v2].append(v1)

        # Initial color: (valence, self_loop_count)
        color = {}
        for v in self.vertices:
            color[v] = (self.valence(v), self_loop_count[v])

        for _ in range(n):
            new_color = {}
            for v in self.vertices:
                neighbor_colors = tuple(sorted(color[w] for w in adj_multi[v]))
                new_color[v] = (color[v], neighbor_colors)
            # Re-encode as integers for efficiency
            palette = {}
            idx = 0
            final = {}
            for v in self.vertices:
                key = new_color[v]
                if key not in palette:
                    palette[key] = idx
                    idx += 1
                final[v] = palette[key]
            if final == color:
                break
            color = final

        # Partition into classes
        classes = defaultdict(list)
        for v in self.vertices:
            classes[color[v]].append(v)
        return dict(classes)

    def _wl_certificate(self):
        """
        Fast Weisfeiler-Leman certificate for cheap isomorphism rejection.
        NOT a complete invariant -- graphs with same certificate MAY be
        non-isomorphic. But graphs with different certificates are
        definitely non-isomorphic.
        """
        classes = self._color_refinement()
        # Certificate: sorted tuple of (class_color, class_size)
        return tuple(sorted((c, len(vs)) for c, vs in classes.items()))

    def canonical_form(self):
        """
        Canonical form: lex-min edge multiset over all vertex relabelings.

        Uses color refinement to prune: only permutations that map
        each equivalence class to itself need be tried.

        For the canonical form to be correct, we need the FULL V!
        search, but color refinement reduces it to product of class_size!
        when the classes are well-separated. The key insight: an isomorphism
        MUST map each color class to a class of the same color. Since colors
        are canonical (same algorithm on both graphs), we try all mappings
        of class-to-class (for same-colored classes of the same size) and
        within each mapping, all vertex permutations.

        For self-canonical-form (single graph), the partition is into
        orbits of the automorphism group (or a refinement thereof).
        Any relabeling that achieves the lex-min must map each class
        to the same class. So we just try all permutations within classes,
        with all possible inter-class label assignments.
        """
        if self._canonical is not None:
            return self._canonical
        n = len(self.vertices)
        if n == 0:
            self._canonical = (0, ())
            return self._canonical

        # For small graphs (V <= 8), just brute force all permutations.
        # The color refinement overhead is not worth it for V <= 6,
        # and for V=7,8 we need a smarter approach anyway.
        if n <= 8:
            best = None
            for perm in permutations(range(n)):
                label_map = {self.vertices[i]: perm[i] for i in range(n)}
                key = self._edge_multiset_under(label_map)
                if best is None or key < best:
                    best = key
            self._canonical = (n, best)
            return self._canonical

        # For larger graphs, would need nauty. Not needed for loop <= 5.
        raise NotImplementedError(f"canonical_form not implemented for V={n} > 8")

    def is_isomorphic_to(self, other):
        if self.num_vertices != other.num_vertices:
            return False
        if self.num_edges != other.num_edges:
            return False
        if self.degree_sequence() != other.degree_sequence():
            return False
        return self.canonical_form() == other.canonical_form()

    def automorphism_count(self):
        """
        |Aut(G)| = sum over vertex perms preserving edge multiset
                   of product of (multiplicity!) per edge type.
        """
        if self._aut_count is not None:
            return self._aut_count
        n = len(self.vertices)
        edge_ms = tuple(sorted(self.edges))
        count = 0
        for perm in permutations(range(n)):
            label_map = {self.vertices[i]: perm[i] for i in range(n)}
            new_edges = []
            for (v1, v2) in self.edges:
                a, b = label_map[v1], label_map[v2]
                new_edges.append((min(a, b), max(a, b)))
            if tuple(sorted(new_edges)) == edge_ms:
                ct = Counter(new_edges)
                ep = 1
                for k in ct.values():
                    ep *= math.factorial(k)
                count += ep
        self._aut_count = count
        return count

    def contract_edge(self, edge_idx):
        """
        Contract edge. Self-loop: just remove. Non-loop: merge vertices,
        keep resulting self-loops.
        """
        v1, v2 = self.edges[edge_idx]
        if v1 == v2:
            new_edges = [e for i, e in enumerate(self.edges) if i != edge_idx]
            return Graph(list(self.vertices), new_edges)
        keep, remove = min(v1, v2), max(v1, v2)
        new_vertices = [v for v in self.vertices if v != remove]
        new_edges = []
        for i, (a, b) in enumerate(self.edges):
            if i == edge_idx:
                continue
            a2 = keep if a == remove else a
            b2 = keep if b == remove else b
            new_edges.append((a2, b2))
        if not new_vertices:
            return None
        return Graph(new_vertices, new_edges)

    def num_self_loops(self):
        return sum(1 for (a, b) in self.edges if a == b)

    def num_multi_edge_pairs(self):
        return sum(max(0, v - 1) for v in Counter(self.edges).values())

    def __repr__(self):
        nm = f" ({self.name})" if self.name else ""
        return f"Graph{nm}: V={self.vertices}, E={self.edges}, loop={self.loop_number}"

    def to_nx(self):
        """Convert to networkx MultiGraph for fast isomorphism."""
        if not _HAS_NX:
            raise ImportError("networkx required")
        G = nx.MultiGraph()
        G.add_nodes_from(self.vertices)
        G.add_edges_from(self.edges)
        return G

    def is_isomorphic_nx(self, other):
        """Fast isomorphism check via networkx VF2."""
        if not _HAS_NX:
            return self.is_isomorphic_to(other)
        if self.num_vertices != other.num_vertices:
            return False
        if self.num_edges != other.num_edges:
            return False
        if self.degree_sequence() != other.degree_sequence():
            return False
        return nx.is_isomorphic(self.to_nx(), other.to_nx())

    def __eq__(self, other):
        if not isinstance(other, Graph):
            return False
        return self.canonical_form() == other.canonical_form()

    def __hash__(self):
        return hash(self.canonical_form())


# ============================================================
# Optimized enumeration with recursive pruning
# ============================================================

def _enumerate_recursive(n_verts, n_edges_remaining, slots, slot_idx,
                         current_edges, degrees, min_val, results_raw):
    """
    Recursive enumeration of multigraphs with pruning.

    Generates edge multisets by choosing edges from slots[slot_idx:]
    in non-decreasing order (to avoid duplicates).

    Prunes when:
    - Remaining edges can't bring all vertices to min_valence
    - Any vertex already exceeds the max possible degree
    """
    if n_edges_remaining == 0:
        # Check min_valence
        if all(d >= min_val for d in degrees):
            results_raw.append(list(current_edges))
        return

    if slot_idx >= len(slots):
        return

    # Pruning: compute the maximum possible degree increase
    # Each remaining edge increases total degree by 2.
    # Deficit = sum of max(0, min_val - degrees[v]) for all v.
    deficit = sum(max(0, min_val - d) for d in degrees)
    if deficit > 2 * n_edges_remaining:
        return

    # For each remaining slot, try adding 0 to n_edges_remaining copies
    s = slots[slot_idx]
    v1, v2 = s

    # Maximum copies of this slot: limited by remaining edges
    max_copies = n_edges_remaining

    for copies in range(0, max_copies + 1):
        if copies > 0:
            current_edges.append(s)
            if v1 == v2:
                degrees[v1] += 2
            else:
                degrees[v1] += 1
                degrees[v2] += 1

        _enumerate_recursive(n_verts, n_edges_remaining - copies,
                             slots, slot_idx + 1,
                             current_edges, degrees, min_val, results_raw)

    # Undo all additions
    for _ in range(max_copies):
        if current_edges and current_edges[-1] == s:
            current_edges.pop()
            if v1 == v2:
                degrees[v1] -= 2
            else:
                degrees[v1] -= 1
                degrees[v2] -= 1


def enumerate_connected_graphs(num_vertices, num_edges, min_valence=3):
    """
    All non-isomorphic connected multigraphs with given V, E, min_valence.
    Uses recursive enumeration with degree-based pruning, then
    WL-certificate grouping for fast isomorphism dedup.
    """
    vertices = list(range(num_vertices))
    slots = [(i, j) for i in range(num_vertices)
             for j in range(i, num_vertices)]

    # Recursive generation
    results_raw = []
    degrees = [0] * num_vertices
    _enumerate_recursive(num_vertices, num_edges, slots, 0,
                         [], degrees, min_valence, results_raw)

    # Filter: connectivity check, then isomorphism dedup.
    connected = []
    for edge_list in results_raw:
        g = Graph(vertices, edge_list)
        if g.is_connected():
            connected.append(g)

    # Dedup by isomorphism.
    # Strategy: group by degree sequence (coarse invariant), then
    # use networkx VF2 (fast for multigraphs) within each group.
    # For small V (<= 7), canonical form is also fast enough.
    results = []
    if _HAS_NX and num_vertices >= 5:
        # Group by degree sequence + edge multiplicity profile
        deg_groups = defaultdict(list)
        for g in connected:
            key = (g.degree_sequence(),
                   tuple(sorted(Counter(g.edges).values())))
            deg_groups[key].append(g)

        for key, group in deg_groups.items():
            representatives = []
            for g in group:
                g_nx = g.to_nx()
                is_dup = False
                for rep, rep_nx in representatives:
                    if nx.is_isomorphic(g_nx, rep_nx):
                        is_dup = True
                        break
                if not is_dup:
                    representatives.append((g, g_nx))
            results.extend(rep for rep, _ in representatives)
    else:
        # For small V, canonical form is fine
        seen = set()
        for g in connected:
            cf = g.canonical_form()
            if cf not in seen:
                seen.add(cf)
                results.append(g)

    return results


def enumerate_by_loop_number(max_loop, min_valence=3):
    """
    All non-isomorphic connected multigraphs with min_valence >= 3,
    organized by loop number b_1 = |E| - |V| + 1.

    Vertex bound: V <= 2(b_1 - 1) for min_valence = 3.
    """
    if min_valence < 3:
        raise ValueError("min_valence must be >= 3")
    result = {}
    for loop in range(1, max_loop + 1):
        graphs = []
        max_V = max(1, 2 * (loop - 1))
        for V in range(1, max_V + 1):
            E = V + loop - 1
            if 2 * E < min_valence * V:
                continue
            graphs.extend(enumerate_connected_graphs(V, E, min_valence))
        seen = set()
        unique = []
        for g in graphs:
            cf = g.canonical_form()
            if cf not in seen:
                seen.add(cf)
                unique.append(g)
        result[loop] = unique
    return result


# ============================================================
# Edge-oriented graph complex differential
# ============================================================

def contraction_sign(edge_idx):
    """Sign (-1)^k for contracting edge at position k."""
    return (-1) ** edge_idx


def check_d_squared(graph):
    """
    Verify d^2 = 0 for a graph in the edge-oriented graph complex.

    d(Gamma) = sum_k (-1)^k Gamma/e_k

    Returns (is_zero, all_contribs, nonzero_contribs).
    """
    g = graph
    m = g.num_edges
    contributions = defaultdict(lambda: Fraction(0))

    for i in range(m):
        g1 = g.contract_edge(i)
        if g1 is None:
            continue
        sign_i = contraction_sign(i)

        for j in range(g1.num_edges):
            g2 = g1.contract_edge(j)
            if g2 is None:
                continue
            if not g2.is_connected():
                continue
            sign_j = contraction_sign(j)
            key = g2.canonical_form()
            contributions[key] += Fraction(sign_i * sign_j)

    nonzero = {k: v for k, v in contributions.items() if v != 0}
    return len(nonzero) == 0, dict(contributions), dict(nonzero)


# ============================================================
# d^2 verification across all loops
# ============================================================

def verify_d_squared(max_loop=4, verbose=False):
    """
    Verify d^2 = 0 for all graphs up to max_loop.
    Returns dict: loop -> report dict.
    """
    database = build_database(max_loop, verbose=verbose)
    report = {}

    for loop_num in sorted(database.keys()):
        entries = database[loop_num]
        graphs = [e['graph'] for e in entries]

        if not graphs:
            report[loop_num] = {
                'num_graphs': 0,
                'd2_zero': True,
                'failures': [],
            }
            continue

        failures = []
        for i, g in enumerate(graphs):
            ok, _, nz = check_d_squared(g)
            if not ok:
                failures.append({
                    'graph_idx': i, 'graph': g,
                    'nonzero_terms': len(nz), 'details': nz,
                })

        report[loop_num] = {
            'num_graphs': len(graphs),
            'd2_zero': len(failures) == 0,
            'failures': failures,
        }

        if verbose:
            tag = "PASS" if not failures else f"FAIL({len(failures)})"
            print(f"  d^2 at loop {loop_num}: {tag}")

    return report


# ============================================================
# Named graphs
# ============================================================

def double_banana():
    """V=1, E=2: single vertex, 2 self-loops. Loop 2."""
    return Graph([0], [(0, 0), (0, 0)], name="double_banana")


def dumbbell():
    """V=2, E=3: two self-loops connected by a bridge. Loop 2."""
    return Graph([0, 1], [(0, 0), (0, 1), (1, 1)], name="dumbbell")


def theta():
    """V=2, E=3: three parallel edges. Loop 2."""
    return Graph([0, 1], [(0, 1), (0, 1), (0, 1)], name="theta")


def triple_banana():
    """V=1, E=3: single vertex, 3 self-loops. Loop 3."""
    return Graph([0], [(0, 0), (0, 0), (0, 0)], name="triple_banana")


def k4():
    """Complete graph K_4: V=4, E=6. Loop 3."""
    edges = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    return Graph(list(range(4)), edges, name="K4")


def k33():
    """Complete bipartite K_{3,3}: V=6, E=9. Loop 4."""
    edges = [(i, 3 + j) for i in range(3) for j in range(3)]
    return Graph(list(range(6)), edges, name="K33")


def petersen():
    """Petersen graph: V=10, E=15. Loop 6."""
    outer = [(i, (i + 1) % 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    spokes = [(i, 5 + i) for i in range(5)]
    return Graph(list(range(10)), outer + inner + spokes, name="Petersen")


# ============================================================
# Database builder
# ============================================================

def build_database(max_loop=5, min_valence=3, verbose=False):
    """
    Build the complete orientation database up to max_loop.
    Returns dict: loop_number -> list of entry dicts.
    """
    if verbose:
        print(f"Enumerating: min_valence={min_valence}, max_loop={max_loop}")

    all_graphs = enumerate_by_loop_number(max_loop, min_valence)
    database = {}

    for loop_num in sorted(all_graphs.keys()):
        graphs = all_graphs[loop_num]
        entries = []
        for idx, g in enumerate(graphs):
            aut = g.automorphism_count()
            he_data = {}
            for e_idx, (hp, hm) in g.half_edges.items():
                v1, v2 = g.edges[e_idx]
                he_data[e_idx] = {
                    'h_plus': hp, 'h_minus': hm,
                    'v1': v1, 'v2': v2,
                    'is_self_loop': v1 == v2,
                }
            vhe = {v: list(g.vertex_half_edges[v]) for v in g.vertices}
            nsl = g.num_self_loops()
            nme = g.num_multi_edge_pairs()

            entry = {
                'graph': g,
                'index': idx,
                'name': g.name,
                'vertices': g.num_vertices,
                'edges': g.num_edges,
                'loop': g.loop_number,
                'automorphisms': aut,
                'degree_sequence': g.degree_sequence(),
                'half_edge_data': he_data,
                'vertex_half_edges': vhe,
                'canonical_form': g.canonical_form(),
                'edge_list': list(g.edges),
                'num_self_loops': nsl,
                'num_multi_edges': nme,
            }
            entries.append(entry)

            if verbose:
                sl_s = f", sl={nsl}" if nsl else ""
                me_s = f", me={nme}" if nme else ""
                print(f"  L{loop_num} #{idx}: V={g.num_vertices} E={g.num_edges} "
                      f"|Aut|={aut} deg={g.degree_sequence()}{sl_s}{me_s}")

        database[loop_num] = entries
        if verbose:
            print(f"  Loop {loop_num} total: {len(entries)} graphs")

    return database


# ============================================================
# Euler characteristic
# ============================================================

def euler_characteristic(max_loop=5):
    """
    chi = sum_Gamma (-1)^{|E|} / |Aut(Gamma)| at each loop number.
    Related to chi(Out(F_n)) by Kontsevich's theorem.
    """
    database = build_database(max_loop)
    result = {}
    for loop_num, entries in sorted(database.items()):
        chi = Fraction(0)
        for e in entries:
            chi += Fraction((-1) ** e['edges'], e['automorphisms'])
        result[loop_num] = chi
    return result


# ============================================================
# Graph count table
# ============================================================

def graph_count_table(max_loop=5, min_valence=3):
    """Summary table of graph counts at each loop number."""
    database = build_database(max_loop, min_valence)
    table = {}
    for loop_num, entries in sorted(database.items()):
        if entries:
            table[loop_num] = {
                'count': len(entries),
                'V_range': (min(e['vertices'] for e in entries),
                            max(e['vertices'] for e in entries)),
                'E_range': (min(e['edges'] for e in entries),
                            max(e['edges'] for e in entries)),
                'simple_count': sum(1 for e in entries
                                    if e['num_self_loops'] == 0
                                    and e['num_multi_edges'] == 0),
            }
        else:
            table[loop_num] = {'count': 0, 'V_range': None,
                               'E_range': None, 'simple_count': 0}
    return table


# ============================================================
# Differential matrix
# ============================================================

def differential_targets(graph, min_valence=3):
    """
    Compute d(graph) as a list of (sign, contracted_graph) pairs,
    filtering to valid graph complex elements.
    """
    results = []
    for e_idx in range(graph.num_edges):
        c = graph.contract_edge(e_idx)
        if c is None:
            continue
        if not c.is_connected():
            continue
        if c.min_valence() < min_valence:
            continue
        results.append((contraction_sign(e_idx), c))
    return results


# ============================================================
# Pretty printer
# ============================================================

def print_database_summary(max_loop=5):
    """Print comprehensive summary."""
    database = build_database(max_loop)
    total = 0

    for loop_num in sorted(database.keys()):
        entries = database[loop_num]
        total += len(entries)
        print(f"\n{'=' * 65}")
        print(f"LOOP {loop_num}: {len(entries)} graphs")
        print(f"{'=' * 65}")
        for e in entries:
            tags = []
            if e['num_self_loops']:
                tags.append(f"{e['num_self_loops']}sl")
            if e['num_multi_edges']:
                tags.append(f"{e['num_multi_edges']}me")
            tag_str = f" [{','.join(tags)}]" if tags else ""
            print(f"  #{e['index']:3d}: V={e['vertices']} E={e['edges']} "
                  f"|Aut|={e['automorphisms']:>4d} "
                  f"deg={e['degree_sequence']}{tag_str}")

    print(f"\n{'=' * 65}")
    print(f"TOTAL: {total} graphs through loop {max_loop}")

    table = graph_count_table(max_loop)
    print(f"\nCOUNT TABLE:")
    print(f"  {'Loop':>4s}  {'Total':>5s}  {'Simple':>6s}  {'V range':>8s}  {'E range':>8s}")
    for loop_num, info in sorted(table.items()):
        if info['count'] > 0:
            print(f"  {loop_num:4d}  {info['count']:5d}  {info['simple_count']:6d}  "
                  f"{str(info['V_range']):>8s}  {str(info['E_range']):>8s}")
        else:
            print(f"  {loop_num:4d}      0      -         -         -")

    # d^2 check
    check_max = min(max_loop, 4)
    print(f"\nd^2 = 0 VERIFICATION (loops 1-{check_max}):")
    report = verify_d_squared(check_max)
    for loop_num in sorted(report.keys()):
        r = report[loop_num]
        if r['num_graphs'] == 0:
            print(f"  Loop {loop_num}: 0 graphs (vacuous)")
            continue
        tag = "PASS" if r['d2_zero'] else f"FAIL({len(r['failures'])})"
        print(f"  Loop {loop_num}: {r['num_graphs']:3d} graphs  d^2=0: {tag}")

    # Euler characteristic
    print(f"\nEULER CHARACTERISTIC chi = sum (-1)^|E| / |Aut|:")
    chi = euler_characteristic(max_loop)
    for loop_num, val in sorted(chi.items()):
        print(f"  Loop {loop_num}: {val} = {float(val):.8f}")


if __name__ == '__main__':
    print_database_summary(4)
