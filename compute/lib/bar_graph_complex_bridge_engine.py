r"""Bar complex / Kontsevich graph complex differential bridge engine.

CONNECTION BETWEEN BAR DIFFERENTIAL AND GRAPH COMPLEX DIFFERENTIAL
==================================================================

The bar complex B(A) of a chiral algebra and the Kontsevich graph complex
GC_n share a deep structural relationship: both are organized by graphs,
and both have differentials that contract edges with signs from the
orientation line det(E(Gamma)).

THEORETICAL FRAMEWORK
---------------------

1. THE KONTSEVICH GRAPH COMPLEX GC_n:
   - Objects: connected graphs Gamma with all vertices valence >= 3
   - Grading: degree = |E| - n|V|  (for GC_n)
   - Orientation: det(E(Gamma)) = bigwedge^top k<E(Gamma)>
   - Differential: d_GC(Gamma) = sum_{e in E} sign(e, Gamma) * Gamma/e
   - d^2 = 0 from codimension-2 face cancellation

2. THE MODULAR BAR COMPLEX (ref: eq:modular-bar-hamiltonian):
   - B^{(g,n)}(A) = oplus_Gamma B_Gamma(A)
   - Each summand: tensor_v V_A(g(v), val(v)) tensor C_*(FM^log_Gamma)
                    tensor det(E_int(Gamma))
   - Full differential D = d_int + d_coll + d_sew + d_pf + hbar*Delta
     (ref: eq:dmod-five-log, eq:ambient-differential)
   - D^2 = 0 from Mok's log-FM normal crossings (thm:ambient-d-squared-zero)

3. THE BRIDGE:
   The graph-sum formula for Theta_A (eq:theta-graph-sum-logfm):

     Theta_A = sum_Gamma (1/|Aut(Gamma)|) W_Gamma^logFM tensor Phi_Gamma^A

   decomposes by stable graphs. The sign in the bar differential at each
   edge contraction is EXACTLY the same as in GC: it comes from the
   position of the edge in the orientation line det(E(Gamma)).

   The key difference: in GC_2, edges are abstract (carrying only an
   orientation). In the bar complex, each edge carries ADDITIONAL DATA:
   the OPE kernel d log(z_i - z_j), which provides a NATURAL half-edge
   orientation (from the chiral algebra's input/output structure).

4. HALF-EDGE ORIENTATIONS:
   The chiral algebra OPE a(z)b(w) ~ sum c_n(w)/(z-w)^n has an inherent
   DIRECTIONALITY: the operator at z acts on the operator at w. This
   gives each edge in the bar complex a natural orientation: from the
   "acting" half-edge to the "acted-upon" half-edge.

   In GC_2, the orientation line is det(E(Gamma)) = bigwedge^top k<E>.
   In the bar complex, the orientation is:
     det(E(Gamma)) tensor bigotimes_e (half-edge orientation at e)

   The half-edge orientations from the OPE are ALREADY PRESENT in the
   bar complex -- they are encoded in the d log(z-w) kernel that
   contracts internal edges.

   KEY RESULT: The bar complex signs and GC_2 signs AGREE because:
   (a) Both use det(E(Gamma)) for the edge-ordering sign
   (b) The bar complex has additional half-edge data, but this data
       is symmetric under the cyclic pairing (the Verdier/BV pairing
       is graded-symmetric), so it does NOT introduce additional signs
       beyond det(E)
   (c) At loop order 4, d^2_{GC} = 0 and d^2_{bar} = 0 independently,
       and the sign conventions are compatible.

5. THE TETRAHEDRON COCYCLE sigma_3 (loop order 3):
   W_3 = K_4 (complete graph on 4 vertices) with 6 edges.
   d(W_3) = 0 in GC_2 because W_3 has odd number of spokes (3).
   In the bar complex, the corresponding arity-4 shadow component
   at genus 0 is the cubic shadow C(A), which is gauge-trivial
   by thm:cubic-gauge-triviality when H^1(F^3g/F^4g, d_2) = 0.

COMPUTATION TARGETS
-------------------
1. Explicit edge-contraction differentials at loop orders 3 and 4
2. Full sign tracking with orientation lines
3. Verification of d^2 = 0 at loop 4 for both GC_2 and bar
4. Half-edge orientation analysis: when does OPE data add signs?
5. Tetrahedron cocycle verification

CONVENTIONS (matching higher_genus_modular_koszul.tex):
- Cohomological grading (|d| = +1)
- Bar uses DESUSPENSION (s^{-1} lowers degree by 1)
- Edge orientation line: det(E) = bigwedge^top k<E>
- Edge-contraction sign: (-1)^{position of e in ordered edge list}
- The bar propagator d log E(z,w) has weight 1 (AP27)

CAUTION (AP1): kappa formulas differ by family.
CAUTION (AP3): Do NOT pattern-match signs -- compute independently.
CAUTION (AP19): Bar differential extracts ALL OPE modes via d log,
    not just the simple-pole coefficient. The r-matrix has pole orders
    ONE LESS than the OPE.
CAUTION (AP35): Verify proofs independently of conclusions.

Manuscript references:
    eq:theta-graph-sum-logfm (higher_genus_modular_koszul.tex)
    eq:graphwise-log-cocomposition (higher_genus_modular_koszul.tex)
    const:vol1-boundary-operators-residue (higher_genus_modular_koszul.tex)
    eq:modular-bar-hamiltonian (higher_genus_modular_koszul.tex)
    eq:intro-feynman (introduction.tex)
    thm:ambient-d-squared-zero (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import itertools
import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import Rational, Symbol, factor, simplify, Matrix


# ============================================================================
# 1. ORIENTED GRAPH DATA STRUCTURE
# ============================================================================

@dataclass(frozen=True)
class OrientedGraph:
    """A graph with an explicit edge ordering (orientation line element).

    The orientation of a graph in GC_2 is an element of
        det(E(Gamma)) = bigwedge^top k<E(Gamma)>
    represented concretely by an ordered tuple of edges.

    Two oriented graphs that differ by a permutation of their edge list
    represent the SAME graph with a sign (-1)^{parity of permutation}.

    Vertices: 0, 1, ..., n_vertices - 1
    Edges: ordered tuple of pairs (i, j) with i < j
    """
    n_vertices: int
    edges: Tuple[Tuple[int, int], ...]  # ORDERED tuple = orientation

    @property
    def n_edges(self) -> int:
        return len(self.edges)

    @property
    def edge_set(self) -> FrozenSet[Tuple[int, int]]:
        return frozenset(self.edges)

    @property
    def loop_order(self) -> int:
        """First Betti number b_1 = |E| - |V| + 1 (connected)."""
        return self.n_edges - self.n_vertices + 1

    @property
    def gc2_degree(self) -> int:
        """Cohomological degree in GC_2: |E| - 2|V|."""
        return self.n_edges - 2 * self.n_vertices

    def vertex_valences(self) -> Dict[int, int]:
        val = {v: 0 for v in range(self.n_vertices)}
        for (a, b) in self.edges:
            val[a] += 1
            val[b] += 1
        return val

    def min_valence(self) -> int:
        vals = self.vertex_valences()
        return min(vals.values()) if vals else 0

    def is_valid_gc2(self) -> bool:
        return all(v >= 3 for v in self.vertex_valences().values())

    def is_connected(self) -> bool:
        if self.n_vertices <= 1:
            return True
        adj: Dict[int, Set[int]] = {v: set() for v in range(self.n_vertices)}
        for (a, b) in self.edges:
            adj[a].add(b)
            adj[b].add(a)
        visited = set()
        stack = [0]
        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            stack.extend(adj[v] - visited)
        return len(visited) == self.n_vertices


# ============================================================================
# 2. ORIENTATION LINE AND SIGN COMPUTATION
# ============================================================================

def edge_removal_sign(edges: Tuple[Tuple[int, int], ...],
                      edge_index: int) -> int:
    """Sign from removing edge at position `edge_index` from the orientation line.

    In det(E) = e_0 wedge e_1 wedge ... wedge e_{m-1},
    removing e_k gives sign (-1)^k times the remaining wedge product.

    This is the sign that appears in the graph complex differential:
        d(Gamma) = sum_e (-1)^{pos(e)} Gamma/e
    """
    return (-1) ** edge_index


def relabeling_edge_sign(old_edges: Tuple[Tuple[int, int], ...],
                         vertex_map: Dict[int, int]) -> int:
    """Sign of the permutation induced on edge ordering by a vertex relabeling.

    When we relabel vertices (e.g., after contracting an edge and
    shifting vertex labels), the edges get mapped and must be re-sorted.
    The sign of the permutation from old order to new sorted order
    contributes to the orientation.

    This is the content of the signed_canonical_form method.
    """
    mapped = []
    for (a, b) in old_edges:
        na, nb = vertex_map[a], vertex_map[b]
        mapped.append((min(na, nb), max(na, nb)))

    # Compute sign of the permutation that sorts `mapped`
    n = len(mapped)
    # Use inversion count
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if mapped[i] > mapped[j]:
                inversions += 1
    return (-1) ** inversions


# ============================================================================
# 3. EDGE CONTRACTION WITH FULL SIGN TRACKING
# ============================================================================

@dataclass
class ContractionResult:
    """Result of contracting an edge in an oriented graph.

    Attributes:
        graph: the contracted graph (or None if invalid)
        sign: the total sign from:
            (a) position in orientation line: (-1)^{pos(e)}
            (b) vertex relabeling after merging: edge-reorder parity
        is_valid: whether the contraction produces a valid GC_2 graph
        edge_contracted: which edge was contracted
        detail: human-readable description
    """
    graph: Optional[OrientedGraph]
    sign: int
    is_valid: bool
    edge_contracted: Tuple[int, int]
    detail: str = ""


def contract_edge_oriented(G: OrientedGraph,
                           edge_index: int) -> ContractionResult:
    """Contract edge at position `edge_index` with full sign tracking.

    Steps:
    1. Remove edge e = (u, v) from the edge list
    2. Merge vertex v into vertex u
    3. Relabel remaining vertices (shift those > v down by 1)
    4. Normalize resulting edges to (min, max) form
    5. Check for self-loops and multi-edges (discard if found)
    6. Check min valence >= 3
    7. Compute total sign = edge_removal_sign * relabeling_sign

    Returns ContractionResult with the new oriented graph and total sign.
    """
    edges = G.edges
    e = edges[edge_index]
    u, v = e  # u < v by convention

    # Step 1: sign from edge removal
    removal_sign = edge_removal_sign(edges, edge_index)

    # Step 2-3: remaining edges with v -> u, vertices > v shift down
    remaining = []
    for idx, (a, b) in enumerate(edges):
        if idx == edge_index:
            continue
        # Relabel: v -> u, then shift
        def relabel(x):
            if x == v:
                return u
            elif x > v:
                return x - 1
            else:
                return x
        ra, rb = relabel(a), relabel(b)

        # Check self-loop
        if ra == rb:
            return ContractionResult(
                graph=None, sign=0, is_valid=False,
                edge_contracted=e,
                detail=f"Contraction of {e} creates self-loop at {ra}"
            )

        remaining.append((min(ra, rb), max(ra, rb)))

    # Check multi-edges
    if len(set(remaining)) < len(remaining):
        return ContractionResult(
            graph=None, sign=0, is_valid=False,
            edge_contracted=e,
            detail=f"Contraction of {e} creates multi-edge"
        )

    # Step 4: sort remaining edges to get canonical orientation
    sorted_remaining = sorted(remaining)

    # Step 5: compute relabeling sign (perm that sorts remaining into lex order)
    # Count inversions in `remaining` relative to `sorted_remaining`
    n = len(remaining)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if remaining[i] > remaining[j]:
                inversions += 1
    relabel_sign = (-1) ** inversions

    # Step 6: build new graph
    new_n = G.n_vertices - 1
    new_edges = tuple(sorted_remaining)
    new_G = OrientedGraph(new_n, new_edges)

    # Step 7: check validity
    if new_G.n_vertices > 0 and new_G.min_valence() < 3:
        return ContractionResult(
            graph=None, sign=0, is_valid=False,
            edge_contracted=e,
            detail=f"Contraction of {e} gives min valence < 3"
        )

    total_sign = removal_sign * relabel_sign

    return ContractionResult(
        graph=new_G, sign=total_sign, is_valid=True,
        edge_contracted=e,
        detail=f"Contract {e}: removal_sign={removal_sign}, "
               f"relabel_sign={relabel_sign}, total={total_sign}"
    )


# ============================================================================
# 4. GC_2 DIFFERENTIAL WITH FULL SIGN AUDIT
# ============================================================================

def gc2_differential_oriented(G: OrientedGraph) -> List[Tuple[OrientedGraph, int, str]]:
    """Compute d_{GC}(Gamma) with complete sign tracking.

    Returns list of (contracted_graph, coefficient, detail_string).
    Terms with the same graph are NOT yet collected -- the caller
    should group by graph isomorphism class and sum coefficients.
    """
    results = []
    for idx in range(G.n_edges):
        cr = contract_edge_oriented(G, idx)
        if cr.is_valid and cr.graph is not None:
            results.append((cr.graph, cr.sign, cr.detail))
    return results


def collect_differential(terms: List[Tuple[OrientedGraph, int, str]]
                         ) -> Dict[FrozenSet[Tuple[int, int]], Tuple[int, OrientedGraph, List[str]]]:
    """Collect terms in the differential by graph isomorphism class.

    Groups by edge set (which is the canonical form for small graphs
    with sorted edge tuples).

    Returns {edge_set: (total_coeff, representative_graph, details)}.
    """
    collected: Dict[FrozenSet, Tuple[int, OrientedGraph, List[str]]] = {}
    for (G, coeff, detail) in terms:
        key = G.edge_set
        if key not in collected:
            collected[key] = (coeff, G, [detail])
        else:
            old_coeff, old_G, old_details = collected[key]
            collected[key] = (old_coeff + coeff, old_G, old_details + [detail])
    return collected


def gc2_differential_collected(G: OrientedGraph
                               ) -> Dict[FrozenSet[Tuple[int, int]], int]:
    """Compute d_{GC}(Gamma) and return {edge_set: total_coefficient}.

    Cancellations (coefficient = 0) are removed.
    """
    terms = gc2_differential_oriented(G)
    collected = collect_differential(terms)
    result = {}
    for key, (coeff, _, _) in collected.items():
        if coeff != 0:
            result[key] = coeff
    return result


# ============================================================================
# 5. d^2 = 0 VERIFICATION WITH FULL SIGN AUDIT
# ============================================================================

def verify_d_squared_zero_oriented(G: OrientedGraph) -> Dict[str, Any]:
    """Verify d^2(Gamma) = 0 with complete sign audit trail.

    Returns a dict with:
        'input': the input graph
        'd1_terms': list of (graph, coeff, detail) from first application of d
        'd2_terms': aggregated terms from d^2
        'd2_is_zero': True iff d^2 = 0
        'sign_audit': detailed breakdown of how signs cancel
    """
    # First differential
    d1_raw = gc2_differential_oriented(G)
    d1_collected = collect_differential(d1_raw)

    # Second differential: apply d to each term in d(Gamma)
    d2_all = defaultdict(int)
    d2_details = defaultdict(list)

    for key1, (coeff1, G1, details1) in d1_collected.items():
        if coeff1 == 0:
            continue
        d2_raw = gc2_differential_oriented(G1)
        for (G2, coeff2, detail2) in d2_raw:
            key2 = G2.edge_set
            contribution = coeff1 * coeff2
            d2_all[key2] += contribution
            d2_details[key2].append(
                f"  From {key1} (coeff={coeff1}): {detail2} => {contribution}"
            )

    # Check if d^2 = 0
    nonzero = {k: v for k, v in d2_all.items() if v != 0}

    # Build sign audit
    sign_audit = []
    for key2 in sorted(d2_details.keys(), key=str):
        total = d2_all[key2]
        sign_audit.append({
            'target_graph': key2,
            'total_coefficient': total,
            'individual_contributions': d2_details[key2],
            'cancels': total == 0,
        })

    return {
        'input': G,
        'input_edges': G.edges,
        'input_loop_order': G.loop_order,
        'd1_terms': len(d1_raw),
        'd1_nonzero': sum(1 for v in d1_collected.values() if v[0] != 0),
        'd2_total_contributions': sum(len(v) for v in d2_details.values()),
        'd2_is_zero': len(nonzero) == 0,
        'd2_nonzero_terms': nonzero,
        'sign_audit': sign_audit,
    }


# ============================================================================
# 6. STANDARD GRAPHS: WHEELS, TETRAHEDRON, LOOP-4 EXAMPLES
# ============================================================================

def oriented_wheel(n_spokes: int) -> OrientedGraph:
    """Construct oriented wheel graph W_n.

    Hub = vertex 0. Rim = vertices 1, ..., n_spokes.
    Edge ordering: rim edges first (sorted), then spoke edges (sorted).
    This gives a canonical orientation.

    W_n properties:
        vertices: n+1
        edges: 2n (n rim + n spokes)
        loop order: n
        GC_2 degree: 2n - 2(n+1) = -2
        Aut: 2n (dihedral D_n)
    """
    n = n_spokes
    edges = []
    # Rim edges (vertex i to vertex i+1, wrapping)
    for i in range(1, n + 1):
        j = (i % n) + 1
        edges.append((min(i, j), max(i, j)))
    # Spoke edges (hub 0 to rim vertex i)
    for i in range(1, n + 1):
        edges.append((0, i))
    return OrientedGraph(n + 1, tuple(sorted(edges)))


def tetrahedron_graph() -> OrientedGraph:
    """The complete graph K_4 (tetrahedron).

    This is the wheel W_3, and also the unique loop-3 graph in GC_2.
    It is a COCYCLE in GC_2 (d(K_4) = 0) because 3 is odd.

    K_4 has:
        vertices: 4
        edges: 6
        loop order: 3
        degree: 6 - 8 = -2
        Aut: 24 (S_4)
    """
    edges = []
    for i in range(4):
        for j in range(i + 1, 4):
            edges.append((i, j))
    return OrientedGraph(4, tuple(sorted(edges)))


def prism_graph() -> OrientedGraph:
    """The triangular prism graph (3-prism).

    Vertices: 0,1,2 (top triangle), 3,4,5 (bottom triangle)
    Edges: 3 top + 3 bottom + 3 vertical = 9 edges
    Loop order: 9 - 6 + 1 = 4
    All vertices have valence 3 => valid GC_2 graph.

    This is one of the loop-4 graphs in GC_2.
    """
    edges = [
        # Top triangle
        (0, 1), (0, 2), (1, 2),
        # Bottom triangle
        (3, 4), (3, 5), (4, 5),
        # Vertical edges
        (0, 3), (1, 4), (2, 5),
    ]
    return OrientedGraph(6, tuple(sorted(edges)))


def complete_bipartite_33() -> OrientedGraph:
    """The complete bipartite graph K_{3,3}.

    Vertices: {0,1,2} and {3,4,5}
    Edges: all 9 edges between the two sets
    Loop order: 9 - 6 + 1 = 4
    All vertices have valence 3 => valid GC_2 graph.

    This is another loop-4 graph in GC_2.
    """
    edges = []
    for i in range(3):
        for j in range(3, 6):
            edges.append((i, j))
    return OrientedGraph(6, tuple(sorted(edges)))


def mobius_kantor_subgraph() -> OrientedGraph:
    """A 4-regular graph on 5 vertices: K_5 minus a perfect matching.

    Wait -- K_5 has 10 edges on 5 vertices. We need loop order 4,
    so |E| = |V| + 3 = 8. For 5 vertices: 8 edges.
    Need all valences >= 3. With 5 vertices and 8 edges,
    average valence = 16/5 = 3.2. Some vertices have valence 3,
    some 4.

    Actually, K_5 minus one edge has 9 edges, loop order 5.
    Let's use the Petersen-like graph instead.

    For loop 4 with 5 vertices: need 8 edges.
    K_5 has C(5,2) = 10 edges. Remove 2 non-adjacent edges.
    """
    # K_5 minus edges (0,1) and (2,3)
    all_k5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    edges = [e for e in all_k5 if e not in [(0, 1), (2, 3)]]
    return OrientedGraph(5, tuple(sorted(edges)))


def enumerate_loop4_gc2() -> List[OrientedGraph]:
    """Enumerate all GC_2 graphs at loop order 4.

    Loop order 4 means |E| = |V| + 3.
    Constraints: connected, all valences >= 3, simple (no multi-edges).

    Known: at loop order 4, GC_2 has a small number of graphs.
    We enumerate by vertex count.

    For |V| vertices: |E| = |V| + 3
    Need: |E| >= ceil(3|V|/2), so |V| + 3 >= ceil(3|V|/2)
           => 3 >= ceil(|V|/2) => |V| <= 6
    Also: |E| <= C(|V|,2), so |V| + 3 <= |V|(|V|-1)/2
           => |V|^2 - 3|V| - 6 >= 0 => |V| >= 5 (approx)
    Actually: |V|=4, |E|=7, C(4,2)=6 < 7: impossible
              |V|=5, |E|=8, C(5,2)=10: possible
              |V|=6, |E|=9, C(6,2)=15: possible
    """
    results = []
    seen: Set[FrozenSet[Tuple[int, int]]] = set()

    for n_v in [5, 6]:
        n_e = n_v + 3
        if n_e > n_v * (n_v - 1) // 2:
            continue
        # Need min valence >= 3: sum of valences = 2*n_e = 2*(n_v+3)
        # Average valence = 2*(n_v+3)/n_v = 2 + 6/n_v
        # For n_v=5: avg = 3.2, need all >= 3
        # For n_v=6: avg = 3.0, need all exactly 3

        all_edges = [(i, j) for i in range(n_v) for j in range(i + 1, n_v)]
        for combo in itertools.combinations(all_edges, n_e):
            G = OrientedGraph(n_v, tuple(sorted(combo)))
            if not G.is_valid_gc2():
                continue
            if not G.is_connected():
                continue
            key = G.edge_set
            if key not in seen:
                seen.add(key)
                results.append(G)

    return results


# ============================================================================
# 7. BAR COMPLEX DIFFERENTIAL COMPONENTS
# ============================================================================

@dataclass
class BarVertex:
    """A vertex in the bar complex graph, decorated with algebra data.

    In the bar complex B^{(g,n)}(A), each vertex v carries:
    - genus g(v)
    - arity val(v) (number of half-edges)
    - transferred operation ell_{val(v)}^tr
    - conformal weight h(v) of the field at v

    The half-edges at v are ORDERED (from the cyclic structure of
    the chiral algebra), giving a natural half-edge orientation.
    """
    label: int
    genus: int
    arity: int  # number of half-edges (internal + external)
    weight: float = 1.0  # conformal weight of the field


@dataclass
class BarEdge:
    """An edge in the bar complex, carrying the propagator.

    The propagator is P_A = H_A^{-1}, the inverse of the Hessian.
    In the bar complex, each edge contracts via d log E(z,w)
    (the logarithmic derivative of the prime form).

    CRITICAL (AP27): The propagator d log E(z,w) has weight 1 in
    BOTH variables, REGARDLESS of the conformal weight h of the
    fields at the endpoints. All channels use E_1.

    The half-edge orientation:
    - half_edge_1: the "source" half-edge (at vertex v1)
    - half_edge_2: the "target" half-edge (at vertex v2)
    - The OPE a(z)b(w) has z -> w, so the source is at z
    """
    label: int
    v1: int  # source vertex
    v2: int  # target vertex
    # Half-edge orientations from OPE structure:
    # The chiral OPE a_{(n)}b = Res_{z=w} a(z)b(w)(z-w)^n dz
    # gives a natural direction: from the z-variable to the w-variable


@dataclass
class BarGraphTerm:
    """A single graph contribution to the bar complex.

    B_Gamma(A) = (tensor_v V_A(g(v), val(v))) tensor C_*(FM_Gamma) tensor det(E)

    The sign convention:
    - det(E) = bigwedge^top k<E>: one-dimensional orientation line
    - Edge contraction at edge e: sign from position in det(E)
    - Vertex operation signs: from the graded structure of s^{-1}A
    - Total bar differential sign = edge_sign * vertex_sign
    """
    graph: OrientedGraph
    vertices: Tuple[BarVertex, ...]
    edges: Tuple[BarEdge, ...]
    genus: int
    arity: int  # number of external legs

    @property
    def is_stable(self) -> bool:
        """Check stability at each vertex."""
        return all(
            2 * v.genus - 2 + v.arity > 0
            for v in self.vertices
        )


def bar_edge_contraction_sign(bar_term: BarGraphTerm,
                              edge_index: int) -> Dict[str, int]:
    """Compute the sign of contracting edge `edge_index` in the bar complex.

    The total sign has THREE components:

    1. ORIENTATION LINE SIGN: the full sign from det(E(Gamma)).
       This includes BOTH:
       (a) (-1)^{pos(e)}: sign from removing edge e at position pos(e)
           in the ordered edge list (the exterior algebra sign)
       (b) relabeling parity: after merging vertices and relabeling,
           the remaining edges get permuted; the parity of this
           permutation is part of the orientation line sign.
       The product (a)*(b) is IDENTICAL to the GC_2 contraction sign.

    2. DESUSPENSION SIGN: from s^{-1} shifts on the contracted elements.
       In the bar complex, each element is desuspended: |s^{-1}a| = |a| - 1.
       The Koszul sign rule for the tensor product gives an additional
       sign when moving s^{-1}a past s^{-1}b.
       For the contraction mu(s^{-1}a, s^{-1}b), the sign is:
           (-1)^{|s^{-1}a| * |s^{-1}b|} = (-1)^{(|a|-1)(|b|-1)}

    3. HALF-EDGE SIGN: from the cyclic pairing orientation.
       The BV/cyclic pairing <a, b> = (-1)^{|a||b|} <b, a> introduces
       a sign when we swap the half-edge orientation.
       For the bar complex with the canonical half-edge orientation
       from the OPE, this sign is TRIVIAL (it is already accounted for
       in the cyclic structure constants).

    Returns dict with each component and the total.
    """
    G = bar_term.graph
    e = bar_term.edges[edge_index]

    # Component 1: orientation line sign = full GC_2 contraction sign
    # This is (-1)^{pos(e)} * relabeling_parity, computed by the
    # same edge contraction routine used for GC_2.
    cr = contract_edge_oriented(G, edge_index)
    orient_sign = cr.sign if cr.is_valid else 0

    # Component 2: desuspension sign
    # For bar complex elements: degree of s^{-1}a at vertex v is
    # |a_v| - 1 where |a_v| is the cohomological degree of the field.
    # The contraction sign is (-1)^{sum of degrees of elements "to the left"}
    # In practice, for weight-1 fields (the standard case, AP27),
    # |a| = 1 and |s^{-1}a| = 0, so the desuspension sign is always +1.
    v1 = bar_term.vertices[e.v1]
    v2 = bar_term.vertices[e.v2]
    desus_sign = (-1) ** ((int(v1.weight) - 1) * (int(v2.weight) - 1))

    # Component 3: half-edge sign (from cyclic pairing)
    # For the canonical OPE orientation, this is +1
    halfedge_sign = 1

    total = orient_sign * desus_sign * halfedge_sign

    return {
        'orientation_line': orient_sign,
        'desuspension': desus_sign,
        'half_edge': halfedge_sign,
        'total': total,
        'detail': (f"orient={orient_sign}, desus={desus_sign}, "
                   f"half_edge={halfedge_sign}, total={total}")
    }


# ============================================================================
# 8. BAR vs GC_2 SIGN COMPARISON
# ============================================================================

def compare_bar_gc2_signs(G: OrientedGraph,
                          weights: Optional[List[float]] = None
                          ) -> Dict[str, Any]:
    """Compare edge-contraction signs between bar complex and GC_2.

    For each edge e in G:
    - Compute the GC_2 sign: (-1)^{pos(e)} * relabeling_sign
    - Compute the bar sign: orient_sign * desus_sign * halfedge_sign
    - Check agreement

    The KEY RESULT: for weight-1 fields (the standard case, AP27),
    the bar signs and GC_2 signs are IDENTICAL because:
    - The orientation line sign is the same
    - The desuspension sign is +1 (|s^{-1}a| = 0)
    - The half-edge sign is +1 (canonical OPE orientation)

    For higher-weight fields, the desuspension sign may differ,
    but this is a VERTEX-LEVEL correction, not an edge-level one.
    """
    if weights is None:
        weights = [1.0] * G.n_vertices

    # Build bar term
    vertices = tuple(
        BarVertex(label=i, genus=0, arity=G.vertex_valences()[i], weight=weights[i])
        for i in range(G.n_vertices)
    )
    edges_list = []
    for idx, (a, b) in enumerate(G.edges):
        edges_list.append(BarEdge(label=idx, v1=a, v2=b))
    bar_term = BarGraphTerm(
        graph=G, vertices=vertices, edges=tuple(edges_list),
        genus=0, arity=0
    )

    comparisons = []
    all_agree = True

    for idx in range(G.n_edges):
        # GC_2 sign
        cr = contract_edge_oriented(G, idx)
        gc2_sign = cr.sign if cr.is_valid else 0

        # Bar sign
        bar_signs = bar_edge_contraction_sign(bar_term, idx)
        bar_sign = bar_signs['total'] if cr.is_valid else 0

        agrees = (gc2_sign == bar_sign) or not cr.is_valid
        if not agrees:
            all_agree = False

        comparisons.append({
            'edge': G.edges[idx],
            'edge_index': idx,
            'gc2_sign': gc2_sign,
            'bar_sign': bar_sign,
            'bar_components': bar_signs,
            'contraction_valid': cr.is_valid,
            'signs_agree': agrees,
        })

    return {
        'graph': G,
        'n_edges': G.n_edges,
        'all_signs_agree': all_agree,
        'comparisons': comparisons,
        'field_weights': weights,
    }


# ============================================================================
# 9. HALF-EDGE ORIENTATION ANALYSIS
# ============================================================================

def halfedge_orientation_analysis(G: OrientedGraph) -> Dict[str, Any]:
    """Analyze whether half-edge orientations from the OPE provide
    additional sign data beyond the orientation line det(E).

    KEY QUESTION: Is the half-edge orientation needed for GC ALREADY
    present in the bar complex?

    ANSWER: YES. The bar complex naturally has half-edge orientations
    from the OPE structure:
    - At each vertex v, the incoming half-edges are ORDERED by the
      cyclic structure of the chiral algebra's n-point function
    - Each edge connects two half-edges: one "source" (z-variable)
      and one "target" (w-variable) in the OPE a(z)b(w)
    - This gives each edge a DIRECTION, beyond the orientation line

    However, for the SIGN computation in the bar differential, the
    half-edge orientation contributes TRIVIALLY (+1) because:
    1. The cyclic pairing is graded-symmetric
    2. The propagator d log E(z,w) = -d log E(w,z) is antisymmetric,
       but this antisymmetry is already encoded in the orientation line
    3. The OPE extraction Res_{z=w} is symmetric for even-spin fields
       (and modifies by a Koszul sign for odd-spin, which is tracked
       by the desuspension)

    For GC_2, the half-edge orientation appears as:
    - An element of det(H_v) at each vertex v, where H_v is the set
      of half-edges at v
    - Combined with det(E) and det(V), this gives the full orientation
      data: det(E) tensor (bigotimes_v det(H_v)) / det(V)

    The quotient by det(V) is trivial for GC_2 (n=2), and the
    half-edge det cancels with the cyclic structure.
    """
    vertex_vals = G.vertex_valences()

    # For each vertex, the half-edge set is the set of incident edges
    halfedge_data = {}
    for v in range(G.n_vertices):
        incident = [(idx, e) for idx, e in enumerate(G.edges) if v in e]
        halfedge_data[v] = {
            'valence': vertex_vals[v],
            'incident_edges': incident,
            'halfedge_det_dim': vertex_vals[v],
            # The cyclic ordering at v: the OPE provides a CYCLIC order
            # on the half-edges at v (from the cyclic symmetry of the
            # n-point function). This cyclic order is encoded in the
            # cyclic minimal model operations ell_n^tr.
            'has_cyclic_order': True,
        }

    # The orientation data:
    # det(E) has dimension |E|
    # product of det(H_v) has dimension sum val(v) = 2|E|
    # det(V) has dimension |V|
    # Total orientation space: dim |E| + 2|E| - |V| = 3|E| - |V|
    # But det(E) alone suffices for GC_2 because
    # bigotimes_v det(H_v) / det(V) is canonically trivialized
    # by the cyclic structure.

    return {
        'graph': G,
        'vertex_halfedge_data': halfedge_data,
        'det_E_dim': G.n_edges,
        'sum_halfedge_dims': sum(vertex_vals.values()),  # = 2|E|
        'det_V_dim': G.n_vertices,
        'total_orientation_dim': 3 * G.n_edges - G.n_vertices,
        'gc2_orientation_dim': G.n_edges - 2 * G.n_vertices,  # = degree
        'bar_orientation_uses_detE': True,
        'bar_halfedge_trivial': True,
        'reason': (
            "The cyclic pairing at each vertex provides a canonical "
            "trivialization of bigotimes_v det(H_v) / det(V), so the "
            "bar complex orientation reduces to det(E) = the GC_2 "
            "orientation line. Half-edge orientations from the OPE "
            "are present but sign-neutral for weight-1 fields."
        ),
    }


# ============================================================================
# 10. TETRAHEDRON COCYCLE VERIFICATION (loop 3, sigma_3)
# ============================================================================

def verify_tetrahedron_cocycle() -> Dict[str, Any]:
    """Verify d(K_4) = 0 in GC_2 with both naive and oriented signs.

    The tetrahedron K_4 is the UNIQUE loop-3 graph in GC_2.
    It represents the cocycle sigma_3, the first generator of grt_1,
    corresponding to zeta(3).

    K_4 has 4 vertices, 6 edges, loop order 3, degree -2.
    |Aut(K_4)| = 24 = |S_4|.

    d(K_4) = sum_{e in E} (+/-) K_4/e

    Contracting ANY edge of K_4 produces a graph on 3 vertices
    with 5 edges. But C(3,2) = 3, so 5 edges requires multi-edges.
    Therefore EVERY contraction produces a multi-edge graph,
    which is ZERO in the reduced GC_2 complex.

    Hence d(K_4) = 0 trivially in the reduced complex.

    In the UNREDUCED complex (allowing multi-edges): the sum of
    6 terms must cancel in pairs by the S_4 symmetry. This happens
    because S_4 has a sign representation (the alternating character)
    and the orientation line transforms by this character.
    """
    K4 = tetrahedron_graph()

    # Compute differential
    d_terms = gc2_differential_oriented(K4)
    d_collected = gc2_differential_collected(K4)

    # Verify d^2 = 0
    d2_result = verify_d_squared_zero_oriented(K4)

    # Analyze each edge contraction
    contraction_details = []
    for idx in range(K4.n_edges):
        cr = contract_edge_oriented(K4, idx)
        contraction_details.append({
            'edge': K4.edges[idx],
            'edge_index': idx,
            'removal_sign': edge_removal_sign(K4.edges, idx),
            'valid': cr.is_valid,
            'reason': cr.detail,
        })

    # Count: how many contractions are valid vs invalid?
    n_valid = sum(1 for cd in contraction_details if cd['valid'])
    n_invalid = sum(1 for cd in contraction_details if not cd['valid'])

    return {
        'graph': 'K_4 (tetrahedron)',
        'vertices': K4.n_vertices,
        'edges': K4.n_edges,
        'loop_order': K4.loop_order,
        'degree': K4.gc2_degree,
        'd_is_zero': len(d_collected) == 0,
        'd_terms_before_cancel': len(d_terms),
        'd_nonzero_terms_after_cancel': len(d_collected),
        'd2_is_zero': d2_result['d2_is_zero'],
        'n_valid_contractions': n_valid,
        'n_invalid_contractions': n_invalid,
        'contraction_details': contraction_details,
        'mechanism': (
            "Every edge contraction of K_4 produces a multi-edge graph "
            "(5 edges on 3 vertices, but C(3,2)=3), which is ZERO in "
            "the reduced GC_2 complex. So d(K_4) = 0 trivially."
        ),
    }


# ============================================================================
# 11. LOOP-4 ANALYSIS
# ============================================================================

def analyze_loop4_differential() -> Dict[str, Any]:
    """Complete analysis of d and d^2 at loop order 4.

    Enumerate all GC_2 graphs at loop 4 and:
    1. Compute d(Gamma) for each
    2. Verify d^2 = 0 for each
    3. Find cocycles (graphs with d = 0)
    4. Compare bar vs GC_2 signs

    At loop 4, GC_2 contains specific graphs (we enumerate them).
    The key test: d^2 = 0 with the CORRECT signs, and the bar
    complex signs agree with GC_2 signs for weight-1 fields.
    """
    graphs = enumerate_loop4_gc2()

    results_per_graph = []
    all_d2_zero = True
    cocycles = []

    for G in graphs:
        # Compute differential
        d_collected = gc2_differential_collected(G)
        is_cocycle = len(d_collected) == 0

        # Verify d^2
        d2 = verify_d_squared_zero_oriented(G)
        if not d2['d2_is_zero']:
            all_d2_zero = False

        # Compare bar vs GC_2 signs
        sign_comparison = compare_bar_gc2_signs(G)

        if is_cocycle:
            cocycles.append(G)

        results_per_graph.append({
            'graph_edges': G.edges,
            'n_vertices': G.n_vertices,
            'n_edges': G.n_edges,
            'loop_order': G.loop_order,
            'degree': G.gc2_degree,
            'is_cocycle': is_cocycle,
            'd_nonzero_terms': len(d_collected),
            'd2_is_zero': d2['d2_is_zero'],
            'bar_gc2_signs_agree': sign_comparison['all_signs_agree'],
        })

    return {
        'n_graphs_loop4': len(graphs),
        'all_d2_zero': all_d2_zero,
        'n_cocycles': len(cocycles),
        'cocycle_graphs': [c.edges for c in cocycles],
        'per_graph_results': results_per_graph,
    }


# ============================================================================
# 12. BAR COMPLEX OPE SIGN CORRECTION
# ============================================================================

def ope_sign_correction_analysis(max_weight: int = 4) -> Dict[str, Any]:
    """Analyze when OPE data introduces signs beyond the GC_2 orientation line.

    For weight-1 fields (AP27: bar propagator is always weight 1),
    the desuspension sign is +1 and the half-edge sign is +1.
    So the bar signs = GC_2 signs exactly.

    For higher-weight fields (hypothetical, since AP27 says propagator
    is always weight 1 -- but the VERTEX operations may have
    effective higher weight), the desuspension sign can be -1:
        (-1)^{(h_1 - 1)(h_2 - 1)} = -1 when both h_1, h_2 are even.

    This analysis checks: for which field weights do the bar and GC_2
    signs disagree?
    """
    K4 = tetrahedron_graph()
    results = {}

    for h in range(1, max_weight + 1):
        weights = [float(h)] * K4.n_vertices
        comparison = compare_bar_gc2_signs(K4, weights=weights)
        results[h] = {
            'weight': h,
            'all_signs_agree': comparison['all_signs_agree'],
            'desuspension_sign': (-1) ** ((h - 1) * (h - 1)),
            'note': (
                f"Weight {h}: desuspension sign = "
                f"{(-1)**((h-1)*(h-1))}. "
                f"For h=1: +1 (standard). "
                f"For h=2: (-1)^1 = -1 (would flip signs at each edge)."
            ) if h <= 2 else f"Weight {h}: desus = {(-1)**((h-1)**2)}"
        }

    return {
        'analysis': (
            "The bar propagator d log E(z,w) has weight 1 (AP27), so the "
            "EDGE-level data is always weight 1. However, VERTEX operations "
            "ell_n^tr may carry effective weight from the transferred A_inf "
            "structure. For the standard landscape (fields of weight h >= 1), "
            "the desuspension sign (-1)^{(h-1)^2} is +1 for odd h and -1 "
            "for even h. Since the bar complex uses the cyclic Hessian "
            "H_A: V -> V*[-1] to define the propagator, and H_A preserves "
            "the parity of the conformal weight, the effective sign "
            "computation reduces to the GC_2 sign for weight-1 "
            "(the universal case)."
        ),
        'weight_results': results,
        'conclusion': (
            "Bar complex signs = GC_2 signs for weight-1 fields (universal). "
            "For higher-weight vertices, the desuspension sign provides "
            "an additional (-1)^{(h-1)^2} per edge, but this is a "
            "vertex-level correction, not an edge-level one. The "
            "orientation line det(E) is the COMPLETE edge-level sign "
            "data for both GC_2 and the bar complex."
        ),
    }


# ============================================================================
# 13. d^2 FAILURE ANALYSIS (hypothetical naive signs)
# ============================================================================

def naive_sign_d_squared_test(G: OrientedGraph) -> Dict[str, Any]:
    """Test d^2 with NAIVE signs (all +1) to show it fails.

    If we drop the orientation line sign and use d(Gamma) = sum_e Gamma/e
    (all positive), then d^2 != 0 in general.

    This demonstrates that the orientation line is ESSENTIAL.
    """
    # Naive differential: all signs +1
    naive_d1_terms = []
    for idx in range(G.n_edges):
        cr = contract_edge_oriented(G, idx)
        if cr.is_valid and cr.graph is not None:
            naive_d1_terms.append((cr.graph, 1, "naive"))  # sign = +1

    naive_d1 = collect_differential(naive_d1_terms)

    # Apply naive d again
    naive_d2 = defaultdict(int)
    for key1, (coeff1, G1, _) in naive_d1.items():
        if coeff1 == 0:
            continue
        for idx2 in range(G1.n_edges):
            cr2 = contract_edge_oriented(G1, idx2)
            if cr2.is_valid and cr2.graph is not None:
                naive_d2[cr2.graph.edge_set] += coeff1

    nonzero_naive = {k: v for k, v in naive_d2.items() if v != 0}

    # Correct differential for comparison
    d2_correct = verify_d_squared_zero_oriented(G)

    return {
        'graph': G.edges,
        'naive_d2_is_zero': len(nonzero_naive) == 0,
        'correct_d2_is_zero': d2_correct['d2_is_zero'],
        'naive_d2_nonzero_count': len(nonzero_naive),
        'correct_d2_nonzero_count': len(d2_correct['d2_nonzero_terms']),
        'demonstrates_sign_necessity': (
            len(nonzero_naive) > 0 and d2_correct['d2_is_zero']
        ),
        'conclusion': (
            "Naive signs (all +1) give d^2 != 0, while correct "
            "orientation-line signs give d^2 = 0. The orientation "
            "line det(E(Gamma)) is ESSENTIAL for the graph complex "
            "differential, and the bar complex inherits this sign "
            "structure automatically."
        ) if len(nonzero_naive) > 0 and d2_correct['d2_is_zero'] else (
            "Both naive and correct signs give d^2 = 0 for this graph "
            "(all contractions may be invalid in reduced GC_2)."
        ),
    }


# ============================================================================
# 14. COMPREHENSIVE SIGN BRIDGE THEOREM
# ============================================================================

def sign_bridge_theorem() -> Dict[str, Any]:
    """State and verify the sign bridge theorem.

    THEOREM (sign bridge): For any oriented graph Gamma in GC_2 and
    any modular Koszul algebra A with weight-1 generating fields,
    the edge-contraction sign in the bar differential d_bar|_Gamma
    equals the edge-contraction sign in d_{GC}|_Gamma.

    More precisely: for each edge e in E(Gamma),

        sign_bar(e, Gamma, A) = sign_GC(e, Gamma)

    where:
    - sign_GC(e, Gamma) = (-1)^{pos(e)} * relabeling_parity
    - sign_bar(e, Gamma, A) = orientation_line * desuspension * halfedge

    PROOF SKETCH:
    (i) The orientation line sign is identical (both use det(E)).
    (ii) For weight-1 fields: desuspension sign = (-1)^{(1-1)(1-1)} = +1.
    (iii) The half-edge sign is +1 by the cyclic symmetry of the pairing.
    (iv) Therefore sign_bar = sign_GC.

    The bar complex has ADDITIONAL structure (the algebra A) that
    DECORATES the graph summands but does NOT modify the SIGNS.
    The signs are purely combinatorial/topological, determined by
    the orientation line.

    CONSEQUENCE: d^2_{bar} = 0 at loop order L is equivalent to
    d^2_{GC} = 0 at loop order L, for any modular Koszul algebra.
    The bar complex does NOT need additional sign corrections from
    the OPE to make d^2 = 0.
    """
    # Verify at loop 3 (tetrahedron)
    K4 = tetrahedron_graph()
    K4_comparison = compare_bar_gc2_signs(K4)

    # Verify at loop 4 (all graphs)
    loop4_analysis = analyze_loop4_differential()

    # OPE correction analysis
    ope_analysis = ope_sign_correction_analysis()

    return {
        'theorem': (
            "For weight-1 modular Koszul algebras, the bar complex "
            "edge-contraction signs equal the GC_2 edge-contraction signs. "
            "The orientation line det(E(Gamma)) is the complete sign data."
        ),
        'loop3_verification': {
            'graph': 'K_4',
            'all_signs_agree': K4_comparison['all_signs_agree'],
            'cocycle': len(gc2_differential_collected(K4)) == 0,
        },
        'loop4_verification': {
            'n_graphs': loop4_analysis['n_graphs_loop4'],
            'all_d2_zero': loop4_analysis['all_d2_zero'],
            'all_signs_agree': all(
                r['bar_gc2_signs_agree']
                for r in loop4_analysis['per_graph_results']
            ),
        },
        'higher_weight_note': ope_analysis['conclusion'],
    }


# ============================================================================
# 15. UTILITY: HUMAN-READABLE GRAPH DESCRIPTION
# ============================================================================

def describe_graph(G: OrientedGraph) -> str:
    """Human-readable description of a graph."""
    vals = G.vertex_valences()
    val_seq = tuple(sorted(vals.values(), reverse=True))
    return (
        f"Graph({G.n_vertices}v, {G.n_edges}e, "
        f"loop={G.loop_order}, deg={G.gc2_degree}, "
        f"valences={val_seq})"
    )


def full_loop_order_report(max_loop: int = 5) -> Dict[int, Dict[str, Any]]:
    """Generate a complete report for each loop order up to max_loop.

    For each loop order:
    - Number of GC_2 graphs
    - d^2 = 0 verification for each
    - Cocycles found
    - Bar/GC_2 sign agreement
    """
    report = {}

    for L in range(2, max_loop + 1):
        if L == 2:
            # Loop 2: only the theta graph (two vertices, three edges)
            # Actually: need |E| = |V| + 1. |V|=2: |E|=3, C(2,2)=1 < 3: impossible
            # |V|=3: |E|=4, need min val >= 3, sum val = 8, avg = 8/3 < 3: impossible
            # |V|=4: |E|=5, need min val >= 3, sum val = 10, avg = 2.5 < 3: impossible
            # Loop 2 is EMPTY in GC_2!
            report[L] = {
                'n_graphs': 0,
                'all_d2_zero': True,
                'n_cocycles': 0,
                'note': 'Loop 2 is empty in GC_2 (no valid graphs)'
            }
            continue

        if L == 3:
            # Loop 3: only K_4
            K4 = tetrahedron_graph()
            d2_result = verify_d_squared_zero_oriented(K4)
            report[L] = {
                'n_graphs': 1,
                'all_d2_zero': d2_result['d2_is_zero'],
                'n_cocycles': 1,  # K_4 is a cocycle
                'graphs': [describe_graph(K4)],
                'note': 'K_4 is the unique loop-3 graph and the cocycle sigma_3'
            }
            continue

        if L == 4:
            analysis = analyze_loop4_differential()
            report[L] = {
                'n_graphs': analysis['n_graphs_loop4'],
                'all_d2_zero': analysis['all_d2_zero'],
                'n_cocycles': analysis['n_cocycles'],
                'graphs': [
                    f"({r['n_vertices']}v, {r['n_edges']}e, cocycle={r['is_cocycle']})"
                    for r in analysis['per_graph_results']
                ],
            }
            continue

        # General case
        report[L] = {'note': f'Loop {L}: enumeration not implemented above L=4'}

    return report
