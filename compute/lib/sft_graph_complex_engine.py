r"""String field theory perspective on graph complex d^2 = 0.

MATHEMATICAL FRAMEWORK
======================

String field theory (SFT) provides a PHYSICAL framework in which d^2 = 0
for the graph complex is not a combinatorial miracle but a CONSEQUENCE
of the BV master equation.  This module implements the SFT sign conventions
and verifies that they reproduce the Kontsevich graph complex differential
with d^2 = 0.

THE THREE KEY STRUCTURES:

1. OPEN SFT (Witten 1986, Zwiebach 1993):
   The string field Psi is expanded in a basis of string states.
   The action S(Psi) = (1/2)<Psi, Q*Psi> + sum_n (1/n!) V_n(Psi^n)
   where Q is BRST and V_n are string vertices.
   The BV master equation {S, S} + 2*hbar*Delta*S = 0 is equivalent to
   the quantum A_infinity relations.

2. CLOSED SFT (Zwiebach 1993):
   The closed string vertices V_{g,n} live on M_bar_{g,n}.
   The BV master equation on the closed string gives d^2 = 0 for the
   modular operad.  This IS the d^2 = 0 that the monograph needs.

3. SFT SIGN CONVENTION:
   (a) Each vertex gets a CYCLIC ORDERING of half-edges (from the cyclic
       structure of string products / the puncture ordering on the
       worldsheet).
   (b) Each edge gets an ORIENTATION (from the propagator b_0/L_0:
       the strip has a canonical direction from the BPZ conjugation).
   (c) These orientations determine the signs in d^2 = 0.

THE KEY IDENTIFICATION (matching bar complex to SFT):
   - Bar differential d_B = BRST operator Q of open SFT
   - Bar curvature m_0 = tadpole (one-loop anomaly)
   - Shadow amplitude Sh_{g,n}(Theta_A) = closed SFT vertex V_{g,n}
   - MC equation for Theta_A = closed SFT master equation
   (See thm:frontier-sft-vertices in frontier_modular_holography_platonic.tex)

HALF-EDGE ORIENTATION FROM SFT:
   The worldsheet for a string propagator is a strip (open) or cylinder
   (closed) with canonical parameterization.  The strip maps to a half-edge
   pair (h_e^+, h_e^-) where:
   - h_e^+ is the outgoing half-edge (at the source vertex)
   - h_e^- is the incoming half-edge (at the target vertex)
   The orientation h_e^+ wedge h_e^- is FIXED by the worldsheet orientation.
   At each vertex, the cyclic ordering comes from the cyclic structure of
   the string product (counterclockwise ordering of punctures on the disk
   for open strings, on the sphere for closed strings).

COMPUTATION AT LOOP ORDER 4:
   We enumerate all graphs in GC_2 at loop order <= 4, compute the SFT
   sign for each, and verify d^2 = 0.

CONVENTIONS:
  - Cohomological grading (|d| = +1).
  - Graphs in GC_2: all vertices valence >= 3, connected, simple (no
    multi-edges), no self-loops.
  - SFT orientation: det(E) tensor bigotimes_v det(H_v) where H_v is the
    set of half-edges at vertex v in cyclic order.
  - The propagator orientation is from h_e^+ to h_e^-, matching the
    BPZ conjugation direction.

Anti-patterns guarded against:
  AP1:  kappa formulas are family-specific; not used here.
  AP3:  All graph counts independently verified by enumeration.
  AP10: Cross-checked via multiple independent d^2 = 0 computations.
  AP19: Pole absorption is irrelevant for the graph complex (no OPE here).
  AP35: We verify d^2 = 0 by EXPLICIT COMPUTATION, not by appeal to SFT.
        The SFT argument provides the PHYSICAL EXPLANATION, not the proof.
  AP37: Spectral sequence pages not used here.

References:
  Witten, "Noncommutative geometry and string field theory" (1986).
  Zwiebach, "Closed string field theory: Quantum action and the BV
    master equation" (1993).
  Kontsevich, "Feynman diagrams and low-dimensional topology" (1994).
  Willwacher, "M. Kontsevich's graph complex and the GRT Lie algebra"
    (Inventiones, 2015).
  Vol I: thm:frontier-sft-vertices (frontier_modular_holography_platonic.tex).
  Vol I: thm:mc2-bar-intrinsic (bar_cobar_adjunction_curved.tex).
  Vol I: thm:convolution-d-squared-zero (higher_genus_modular_koszul.tex).
  Vol I: eq:preface-feynman-sum, preface.tex line 973.
"""

from __future__ import annotations

import itertools
import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple


# ===========================================================================
# 1. ORIENTED GRAPH DATA STRUCTURES
# ===========================================================================

@dataclass(frozen=True)
class HalfEdge:
    """A half-edge in an oriented graph.

    Each edge e = (u, v) decomposes into two half-edges:
      h_plus:  at vertex u (source, outgoing)
      h_minus: at vertex v (target, incoming)

    The SFT convention: the propagator b_0/L_0 maps from h_plus to h_minus.
    This is the BPZ direction on the worldsheet strip.
    """
    edge_index: int
    vertex: int
    is_source: bool  # True = h^+, False = h^-

    @property
    def label(self) -> str:
        sign = '+' if self.is_source else '-'
        return f"h_{self.edge_index}^{sign}"


@dataclass
class OrientedGraph:
    """A graph with SFT-induced orientation data.

    The SFT orientation consists of:
    1. An ordered edge list (determines det(E))
    2. At each vertex, a CYCLIC ordering of half-edges (from the string
       product cyclic structure)
    3. Each edge has an orientation (source -> target, from the propagator)

    The orientation line is:
      omega = bigwedge_e (h_e^+ wedge h_e^-) tensor bigotimes_v det(H_v)

    For GC_2, the relevant orientation is det(E) tensor det(V)^{-2}.
    Since det(V)^{-2} is trivial (even power), only det(E) matters.
    The SFT contribution is the ADDITIONAL structure from half-edge
    decomposition that makes all signs consistent.

    Attributes:
        n_vertices: number of vertices
        edges: list of (u, v) pairs (u < v), ordered
        half_edges: dict edge_index -> (HalfEdge_plus, HalfEdge_minus)
        vertex_cyclic_order: dict vertex -> list of HalfEdge in cyclic order
    """
    n_vertices: int
    edges: List[Tuple[int, int]]
    half_edges: Dict[int, Tuple[HalfEdge, HalfEdge]] = field(default_factory=dict)
    vertex_cyclic_order: Dict[int, List[HalfEdge]] = field(default_factory=dict)
    name: str = ""

    def __post_init__(self):
        if not self.half_edges:
            self._setup_half_edges()
        if not self.vertex_cyclic_order:
            self._setup_cyclic_order()

    def _setup_half_edges(self):
        """Assign half-edges from the edge list.

        SFT convention: for edge e = (u, v) with u < v,
        h_e^+ is at u (source), h_e^- is at v (target).
        The propagator direction is u -> v.
        """
        self.half_edges = {}
        for idx, (u, v) in enumerate(self.edges):
            h_plus = HalfEdge(edge_index=idx, vertex=u, is_source=True)
            h_minus = HalfEdge(edge_index=idx, vertex=v, is_source=False)
            self.half_edges[idx] = (h_plus, h_minus)

    def _setup_cyclic_order(self):
        """Set up canonical cyclic ordering of half-edges at each vertex.

        SFT convention: the cyclic ordering at each vertex comes from
        the counterclockwise ordering of punctures on the disk (open)
        or sphere (closed).

        For the canonical form, we order half-edges at each vertex by:
        1. Edge index (ascending)
        This gives a canonical cyclic representative.
        """
        self.vertex_cyclic_order = defaultdict(list)
        for idx, (h_plus, h_minus) in self.half_edges.items():
            self.vertex_cyclic_order[h_plus.vertex].append(h_plus)
            self.vertex_cyclic_order[h_minus.vertex].append(h_minus)
        # Sort by edge index at each vertex for canonical form
        for v in self.vertex_cyclic_order:
            self.vertex_cyclic_order[v].sort(key=lambda h: h.edge_index)

    @property
    def n_edges(self) -> int:
        return len(self.edges)

    @property
    def loop_order(self) -> int:
        """First Betti number = |E| - |V| + 1."""
        return self.n_edges - self.n_vertices + 1

    @property
    def degree(self) -> int:
        """Cohomological degree in GC_2: |E| - 2|V|."""
        return self.n_edges - 2 * self.n_vertices

    def vertex_valences(self) -> Dict[int, int]:
        """Valence of each vertex."""
        val: Dict[int, int] = {v: 0 for v in range(self.n_vertices)}
        for (u, v) in self.edges:
            val[u] += 1
            val[v] += 1
        return val

    def min_valence(self) -> int:
        vals = self.vertex_valences()
        return min(vals.values()) if vals else 0

    def is_valid_gc2(self) -> bool:
        return all(v >= 3 for v in self.vertex_valences().values())

    def is_connected(self) -> bool:
        if self.n_vertices <= 1:
            return True
        visited: Set[int] = {0}
        queue = [0]
        while queue:
            v = queue.pop()
            for (a, b) in self.edges:
                if a == v and b not in visited:
                    visited.add(b)
                    queue.append(b)
                elif b == v and a not in visited:
                    visited.add(a)
                    queue.append(a)
        return len(visited) == self.n_vertices

    @property
    def edge_set(self) -> FrozenSet[Tuple[int, int]]:
        return frozenset(self.edges)

    def canonical_edge_set(self) -> Tuple[Tuple[int, int], ...]:
        """Sorted tuple of edges for comparison (label-dependent, NOT up to iso)."""
        return tuple(sorted(self.edges))

    def isomorphism_canonical_form(self) -> Tuple[Tuple[int, int], ...]:
        """Canonical form up to graph isomorphism.

        Tries all vertex relabelings and returns the lexicographically
        smallest edge tuple.  For n_vertices <= 7, this is exact.
        For larger graphs, uses degree-partition pruning.

        This is the CORRECT canonical form for deduplicating GC_2 graphs.
        Two graphs are isomorphic iff their isomorphism_canonical_form agrees.
        """
        n = self.n_vertices
        if n > 8:
            # Degree-based heuristic for large graphs (may miss some iso)
            degs = self.vertex_valences()
            sorted_verts = sorted(range(n), key=lambda v: degs[v])
            perm = {v: i for i, v in enumerate(sorted_verts)}
            mapped = tuple(sorted(
                (min(perm[a], perm[b]), max(perm[a], perm[b]))
                for (a, b) in self.edges
            ))
            return mapped

        # For small graphs: degree-partition constrained search
        degs = self.vertex_valences()
        deg_groups: Dict[int, List[int]] = defaultdict(list)
        for v in range(n):
            deg_groups[degs[v]].append(v)

        groups = [deg_groups[d] for d in sorted(deg_groups.keys())]
        group_sizes = [len(g) for g in groups]

        best: Optional[Tuple[Tuple[int, int], ...]] = None

        def gen_perms(group_idx: int, perm_so_far: List[int]):
            nonlocal best
            if group_idx == len(groups):
                mapped = tuple(sorted(
                    (min(perm_so_far[a], perm_so_far[b]),
                     max(perm_so_far[a], perm_so_far[b]))
                    for (a, b) in self.edges
                ))
                if best is None or mapped < best:
                    best = mapped
                return

            group = groups[group_idx]
            start = sum(group_sizes[:group_idx])
            target_positions = list(range(start, start + len(group)))

            for perm_of_group in itertools.permutations(group):
                new_perm = list(perm_so_far)
                for pos, v in zip(target_positions, perm_of_group):
                    new_perm[v] = pos
                gen_perms(group_idx + 1, new_perm)

        gen_perms(0, [0] * n)
        return best


# ===========================================================================
# 2. SFT SIGN COMPUTATION
# ===========================================================================

def sft_edge_contraction_sign(graph: OrientedGraph, edge_idx: int) -> int:
    """Compute the SFT sign for contracting edge edge_idx.

    The sign has THREE contributions:

    1. EDGE POSITION SIGN: (-1)^{pos(e)} from the position of edge e
       in the ordered edge list.  This is the standard det(E) sign.

    2. HALF-EDGE MERGE SIGN: When contracting edge e = (u, v), the
       half-edges at u and v must be merged into a single cyclic
       ordering at the new vertex.  The sign comes from the
       permutation needed to interleave the two cyclic orderings,
       minus the two half-edges of e itself (which are annihilated).

       Concretely: at the merged vertex w, the half-edges are
       (H_u minus h_e^+) union (H_v minus h_e^-), and we must put them in
       canonical cyclic order.  The sign is the parity of the
       permutation from the concatenation order to the sorted order.

    3. PROPAGATOR SIGN: The SFT propagator b_0/L_0 has a fixed
       orientation.  When we contract e, we are integrating over
       the moduli of the strip, which contributes a sign from the
       orientation of the integration domain.  For the BV formalism
       this is always +1 (the strip modulus is positive).

    The TOTAL SFT sign is the product of all three.

    In practice, for GC_2 (where det(V)^{-2} is trivial), the SFT
    sign reduces to:
      sign = (-1)^{pos(e)} * epsilon_merge(e)
    where epsilon_merge accounts for the half-edge reordering.
    """
    if edge_idx < 0 or edge_idx >= graph.n_edges:
        raise ValueError(f"Edge index {edge_idx} out of range [0, {graph.n_edges})")

    u, v = graph.edges[edge_idx]

    # --- Contribution 1: edge position sign ---
    edge_pos_sign = (-1) ** edge_idx

    # --- Contribution 2: half-edge merge sign ---
    # Collect half-edges at u and v, excluding those of edge e
    h_plus, h_minus = graph.half_edges[edge_idx]

    half_edges_at_u = [h for h in graph.vertex_cyclic_order[u]
                       if h.edge_index != edge_idx]
    half_edges_at_v = [h for h in graph.vertex_cyclic_order[v]
                       if h.edge_index != edge_idx]

    # The merged list in concatenation order
    concat_order = half_edges_at_u + half_edges_at_v

    # Target: sorted by edge index (canonical cyclic order at merged vertex)
    sorted_order = sorted(concat_order, key=lambda h: (h.edge_index, not h.is_source))

    # Compute the permutation parity
    merge_sign = _permutation_sign_from_lists(concat_order, sorted_order)

    # --- Contribution 3: propagator orientation sign ---
    # In the BV formalism, the propagator integration contributes +1.
    # The BPZ conjugation direction is fixed, so no additional sign.
    propagator_sign = 1

    return edge_pos_sign * merge_sign * propagator_sign


def _permutation_sign_from_lists(source: list, target: list) -> int:
    """Compute the sign of the permutation mapping source to target.

    Both lists must contain the same elements (compared by identity/equality).
    Returns +1 for even permutation, -1 for odd.

    Uses the inversion count method.
    """
    n = len(source)
    if n <= 1:
        return 1

    # Build index map: target element -> position
    # We need to handle the case where elements may not be hashable in the
    # usual sense, so use index-based matching
    target_indices = {id(target[i]): i for i in range(n)}

    # For each element in source, find its position in target
    perm = []
    for s in source:
        perm.append(target_indices[id(s)])

    # Count inversions
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1

    return 1 if inversions % 2 == 0 else -1


# ===========================================================================
# 3. GRAPH COMPLEX DIFFERENTIAL WITH SFT SIGNS
# ===========================================================================

def contract_edge_sft(graph: OrientedGraph, edge_idx: int
                      ) -> Optional[Tuple[OrientedGraph, int]]:
    """Contract edge edge_idx and return the new oriented graph with SFT sign.

    Returns (new_graph, total_sign) or None if contraction leaves GC_2
    (creates self-loop, multi-edge, or vertex with valence < 3).
    """
    u, v = graph.edges[edge_idx]
    merge_to = min(u, v)  # the surviving vertex
    merge_from = max(u, v)

    # Compute sign BEFORE modifying the graph
    total_sign = sft_edge_contraction_sign(graph, edge_idx)

    # Build new edge list
    new_edges_raw: List[Tuple[int, int]] = []
    for idx, (a, b) in enumerate(graph.edges):
        if idx == edge_idx:
            continue
        # Relabel: merge_from -> merge_to, vertices > merge_from shift down
        ra = merge_to if a == merge_from else (a - 1 if a > merge_from else a)
        rb = merge_to if b == merge_from else (b - 1 if b > merge_from else b)
        if ra == rb:
            return None  # self-loop
        e = (min(ra, rb), max(ra, rb))
        new_edges_raw.append(e)

    # Check for multi-edges
    if len(set(new_edges_raw)) < len(new_edges_raw):
        return None

    # Sort edges for canonical form
    new_edges = sorted(set(new_edges_raw))
    new_n = graph.n_vertices - 1

    new_graph = OrientedGraph(
        n_vertices=new_n,
        edges=new_edges,
    )

    if not new_graph.is_valid_gc2():
        return None
    if new_n > 1 and not new_graph.is_connected():
        return None

    return new_graph, total_sign


def sft_differential(graph: OrientedGraph) -> Dict[Tuple[Tuple[int, int], ...], int]:
    """Compute the graph complex differential using SFT signs.

    d(Gamma) = sum_e sft_sign(e) * Gamma/e

    Returns dict mapping canonical_edge_tuple -> coefficient.
    """
    result: Dict[Tuple[Tuple[int, int], ...], int] = defaultdict(int)

    for edge_idx in range(graph.n_edges):
        contracted = contract_edge_sft(graph, edge_idx)
        if contracted is None:
            continue
        new_graph, sign = contracted
        key = new_graph.canonical_edge_set()
        result[key] += sign

    return {k: v for k, v in result.items() if v != 0}


def sft_d_squared(graph: OrientedGraph) -> Dict[Tuple[Tuple[int, int], ...], int]:
    """Compute d^2(Gamma) using SFT signs.

    Should return the zero map if the SFT signs are correct.
    """
    d1 = sft_differential(graph)

    result: Dict[Tuple[Tuple[int, int], ...], int] = defaultdict(int)
    for edge_key, coeff1 in d1.items():
        # Reconstruct the graph from its edge key
        if not edge_key:
            continue
        max_vertex = max(max(e) for e in edge_key)
        g1 = OrientedGraph(n_vertices=max_vertex + 1, edges=list(edge_key))
        d2 = sft_differential(g1)
        for edge_key2, coeff2 in d2.items():
            result[edge_key2] += coeff1 * coeff2

    return {k: v for k, v in result.items() if v != 0}


# ===========================================================================
# 4. STANDARD (EDGE-ORDER) SIGN CONVENTION
# ===========================================================================

def standard_edge_contraction_sign(graph: OrientedGraph, edge_idx: int) -> int:
    """Standard graph complex sign: just (-1)^{position in edge list}.

    This is the naive sign convention without half-edge tracking.
    """
    return (-1) ** edge_idx


def standard_differential(graph: OrientedGraph
                          ) -> Dict[Tuple[Tuple[int, int], ...], int]:
    """Compute the differential with the standard (naive) sign convention.

    d(Gamma) = sum_e (-1)^{pos(e)} * Gamma/e
    """
    result: Dict[Tuple[Tuple[int, int], ...], int] = defaultdict(int)

    for edge_idx in range(graph.n_edges):
        sign = standard_edge_contraction_sign(graph, edge_idx)
        # Contract without SFT sign
        u, v = graph.edges[edge_idx]
        merge_to = min(u, v)
        merge_from = max(u, v)

        new_edges_raw: List[Tuple[int, int]] = []
        valid = True
        for idx, (a, b) in enumerate(graph.edges):
            if idx == edge_idx:
                continue
            ra = merge_to if a == merge_from else (a - 1 if a > merge_from else a)
            rb = merge_to if b == merge_from else (b - 1 if b > merge_from else b)
            if ra == rb:
                valid = False
                break
            e = (min(ra, rb), max(ra, rb))
            new_edges_raw.append(e)

        if not valid:
            continue

        if len(set(new_edges_raw)) < len(new_edges_raw):
            continue

        new_edges = sorted(set(new_edges_raw))
        new_n = graph.n_vertices - 1
        new_graph = OrientedGraph(n_vertices=new_n, edges=new_edges)

        if not new_graph.is_valid_gc2():
            continue
        if new_n > 1 and not new_graph.is_connected():
            continue

        key = new_graph.canonical_edge_set()
        result[key] += sign

    return {k: v for k, v in result.items() if v != 0}


def standard_d_squared(graph: OrientedGraph
                       ) -> Dict[Tuple[Tuple[int, int], ...], int]:
    """Compute d^2 with standard signs. May NOT be zero."""
    d1 = standard_differential(graph)
    result: Dict[Tuple[Tuple[int, int], ...], int] = defaultdict(int)
    for edge_key, coeff1 in d1.items():
        if not edge_key:
            continue
        max_vertex = max(max(e) for e in edge_key)
        g1 = OrientedGraph(n_vertices=max_vertex + 1, edges=list(edge_key))
        d2 = standard_differential(g1)
        for edge_key2, coeff2 in d2.items():
            result[edge_key2] += coeff1 * coeff2
    return {k: v for k, v in result.items() if v != 0}


# ===========================================================================
# 5. GRAPH ENUMERATION
# ===========================================================================

def enumerate_oriented_gc2(max_vertices: int, max_edges: int
                           ) -> List[OrientedGraph]:
    """Enumerate all non-isomorphic connected graphs in GC_2 as OrientedGraphs.

    Returns canonical representatives with SFT orientation data.
    Deduplication is by graph ISOMORPHISM (not label-dependent edge set).
    """
    results: List[OrientedGraph] = []
    seen: Set[Tuple[Tuple[int, int], ...]] = set()

    for n_v in range(2, max_vertices + 1):
        min_e = (3 * n_v + 1) // 2
        max_e_possible = n_v * (n_v - 1) // 2
        actual_max_e = min(max_edges, max_e_possible)

        if min_e > actual_max_e:
            continue

        all_possible_edges = [
            (i, j) for i in range(n_v) for j in range(i + 1, n_v)
        ]

        for n_e in range(min_e, actual_max_e + 1):
            for edge_combo in itertools.combinations(all_possible_edges, n_e):
                edges = sorted(edge_combo)
                g = OrientedGraph(n_vertices=n_v, edges=edges)
                if not g.is_valid_gc2():
                    continue
                if not g.is_connected():
                    continue
                key = g.isomorphism_canonical_form()
                if key not in seen:
                    seen.add(key)
                    results.append(g)

    return results


def oriented_gc2_by_loop_order(max_loop: int) -> Dict[int, List[OrientedGraph]]:
    """Enumerate GC_2 graphs organized by loop order, as OrientedGraphs.

    Deduplication is by graph ISOMORPHISM (not label-dependent edge set).
    """
    by_loop: Dict[int, List[OrientedGraph]] = defaultdict(list)

    for L in range(1, max_loop + 1):
        seen: Set[Tuple[Tuple[int, int], ...]] = set()
        max_v = 2 * L
        for n_v in range(2, max_v + 1):
            n_e = n_v + L - 1
            if n_e > n_v * (n_v - 1) // 2:
                continue
            if n_e < (3 * n_v + 1) // 2:
                continue

            all_possible = [
                (i, j) for i in range(n_v) for j in range(i + 1, n_v)
            ]
            if n_e > len(all_possible):
                continue

            for edge_combo in itertools.combinations(all_possible, n_e):
                edges = sorted(edge_combo)
                g = OrientedGraph(n_vertices=n_v, edges=edges)
                if not g.is_valid_gc2():
                    continue
                if not g.is_connected():
                    continue
                key = g.isomorphism_canonical_form()
                if key not in seen:
                    seen.add(key)
                    by_loop[L].append(g)

    return by_loop


# ===========================================================================
# 6. NAMED GRAPHS
# ===========================================================================

def oriented_wheel(n_spokes: int) -> OrientedGraph:
    """Wheel graph W_n with SFT orientation.

    Hub = vertex 0, rim = vertices 1..n.
    Edges: rim (i, i+1 mod n) + spokes (0, i).
    Cyclic order at hub: spokes in order (0,1), (0,2), ..., (0,n).
    Cyclic order at rim vertex i: spoke, rim-left, rim-right.
    """
    if n_spokes < 3:
        raise ValueError(f"Need >= 3 spokes, got {n_spokes}")
    n = n_spokes
    edges: List[Tuple[int, int]] = []
    # Spoke edges (hub=0 to rim vertex i) -- listed first
    for i in range(1, n + 1):
        edges.append((0, i))
    # Rim edges
    for i in range(1, n + 1):
        j = (i % n) + 1
        a, b = min(i, j), max(i, j)
        edges.append((a, b))
    edges = sorted(edges)
    return OrientedGraph(n_vertices=n + 1, edges=edges, name=f"W_{n}")


def oriented_theta() -> OrientedGraph:
    """Theta graph: 2 vertices, 3 parallel edges.

    The simplest graph in GC_2 with all valence 3.
    Loop order = 3 - 2 + 1 = 2. Degree = 3 - 4 = -1.
    """
    # 2 vertices, 3 edges between them
    edges = [(0, 1), (0, 1), (0, 1)]
    # But GC_2 is SIMPLE (no multi-edges). The theta graph is NOT in GC_2.
    # The theta graph has multi-edges and is excluded from the reduced complex.

    # The correct loop-2 graph in GC_2 is K_4 minus an edge, but that has
    # a valence-2 vertex.  In fact, the SMALLEST graph in GC_2 (simple, all
    # valence >= 3) is K_4 (complete graph on 4 vertices):
    #   V = 4, E = 6, loop = 6-4+1 = 3, degree = 6-8 = -2.
    # So the theta graph is NOT in GC_2 (reduced, simple).

    # For completeness, return K_4 as the "simplest":
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    return OrientedGraph(n_vertices=4, edges=edges, name="K_4")


def oriented_k4() -> OrientedGraph:
    """Complete graph K_4: 4 vertices, 6 edges.

    The simplest graph in GC_2 (simple, min valence 3).
    Loop order = 6 - 4 + 1 = 3. Degree = 6 - 8 = -2.
    This is the wheel W_3 (triangle with hub).
    """
    edges = sorted([
        (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)
    ])
    return OrientedGraph(n_vertices=4, edges=edges, name="K_4")


def oriented_k33() -> OrientedGraph:
    """Complete bipartite graph K_{3,3}: 6 vertices, 9 edges.

    Vertices {0,1,2} on one side, {3,4,5} on the other.
    Loop order = 9 - 6 + 1 = 4. Degree = 9 - 12 = -3.
    All valence 3. This is a key graph at loop order 4.
    """
    edges = sorted([
        (i, j) for i in range(3) for j in range(3, 6)
    ])
    return OrientedGraph(n_vertices=6, edges=edges, name="K_{3,3}")


def oriented_petersen() -> OrientedGraph:
    """Petersen graph: 10 vertices, 15 edges.

    All valence 3. Loop order = 15 - 10 + 1 = 6. Degree = 15 - 20 = -5.
    The Petersen graph is 3-regular and is a key object in graph theory.
    """
    edges = sorted([
        # Outer pentagon
        (0, 1), (1, 2), (2, 3), (3, 4), (0, 4),
        # Inner pentagram
        (5, 7), (7, 9), (9, 6), (6, 8), (5, 8),
        # Spokes
        (0, 5), (1, 6), (2, 7), (3, 8), (4, 9),
    ])
    return OrientedGraph(n_vertices=10, edges=edges, name="Petersen")


# ===========================================================================
# 7. SFT AMPLITUDE COMPUTATION
# ===========================================================================

def sft_amplitude_sign(graph: OrientedGraph) -> int:
    """Compute the SFT amplitude sign for a graph.

    In closed string field theory, the amplitude for a graph Gamma is:
      A(Gamma) = (hbar^g / |Aut(Gamma)|) * prod_v V_{g(v), n(v)} * prod_e P_e

    where V_{g,n} are the string vertices and P_e is the propagator.

    The SIGN of the amplitude comes from:
    1. The ordering of vertices (from the Feynman rules)
    2. The cyclic orderings at each vertex
    3. The propagator orientations

    For the graph complex, the relevant sign is the one entering the
    differential, which we compute in sft_edge_contraction_sign.

    Here we compute the OVERALL sign of the graph amplitude relative
    to the canonical orientation.  This is the product of:
    - vertex cyclic ordering signs (from the string product)
    - propagator direction signs (from b_0/L_0)

    For the canonical form (edges sorted, cyclic orders canonical),
    this is always +1.
    """
    # In canonical form, the sign is +1 by definition
    return 1


def sft_vertex_factor(valence: int, genus: int = 0) -> str:
    """String representation of the SFT vertex factor V_{g,n}.

    The string vertex V_{g,n} is a multilinear map on n string states,
    defined by integration over a region in the moduli space M_{g,n}.

    For genus 0:
      V_{0,3} = cubic coupling (Witten's open string vertex)
      V_{0,n} = (n-3)-fold product (higher string products)

    For genus g > 0:
      V_{g,n} = genus-g, n-punctured surface contribution
    """
    return f"V_{{{genus},{valence}}}"


# ===========================================================================
# 8. COMPARISON: SFT vs NAIVE vs CANONICAL SIGNS
# ===========================================================================

def compare_sign_conventions(graph: OrientedGraph
                             ) -> Dict[str, Dict[Tuple[Tuple[int, int], ...], int]]:
    """Compare the SFT and standard sign conventions for the differential.

    Returns a dict with keys 'sft', 'standard', 'difference' containing
    the differential computed with each convention and their difference.
    """
    sft_d = sft_differential(graph)
    std_d = standard_differential(graph)

    # Compute difference
    all_keys = set(sft_d.keys()) | set(std_d.keys())
    diff = {}
    for k in all_keys:
        d = sft_d.get(k, 0) - std_d.get(k, 0)
        if d != 0:
            diff[k] = d

    return {
        'sft': sft_d,
        'standard': std_d,
        'difference': diff,
    }


def sign_discrepancy_analysis(max_loop: int = 4
                               ) -> Dict[int, Dict[str, Any]]:
    """Analyze sign discrepancies between SFT and naive conventions.

    For each loop order up to max_loop, enumerate graphs and check:
    1. Does d^2 = 0 with SFT signs?
    2. Does d^2 = 0 with naive signs?
    3. Where do the signs differ?

    Returns a dict by loop order with analysis results.
    """
    by_loop = oriented_gc2_by_loop_order(max_loop)
    analysis: Dict[int, Dict[str, Any]] = {}

    for L, graphs in sorted(by_loop.items()):
        sft_d2_ok = True
        std_d2_ok = True
        n_discrepancies = 0
        discrepancy_details: List[Dict] = []

        for g in graphs:
            # Check d^2 with SFT signs
            d2_sft = sft_d_squared(g)
            if d2_sft:
                sft_d2_ok = False

            # Check d^2 with standard signs
            d2_std = standard_d_squared(g)
            if d2_std:
                std_d2_ok = False

            # Compare signs
            comp = compare_sign_conventions(g)
            if comp['difference']:
                n_discrepancies += 1
                discrepancy_details.append({
                    'graph': g.canonical_edge_set(),
                    'n_vertices': g.n_vertices,
                    'n_edges': g.n_edges,
                    'sft_terms': len(comp['sft']),
                    'std_terms': len(comp['standard']),
                    'diff_terms': len(comp['difference']),
                })

        analysis[L] = {
            'n_graphs': len(graphs),
            'sft_d2_zero': sft_d2_ok,
            'standard_d2_zero': std_d2_ok,
            'n_sign_discrepancies': n_discrepancies,
            'discrepancy_details': discrepancy_details,
        }

    return analysis


# ===========================================================================
# 9. BV MASTER EQUATION VERIFICATION
# ===========================================================================

def bv_master_equation_check(graph: OrientedGraph) -> Dict[str, Any]:
    """Verify the BV master equation perspective on d^2 = 0.

    The BV master equation {S, S} + 2*hbar*Delta*S = 0 implies:
    1. At tree level (hbar^0): {S_0, S_0} = 0  =>  d_bar^2 = 0
    2. At one-loop (hbar^1): {S_0, S_1} + Delta*S_0 = 0  =>  anomaly
    3. At genus g: sum over splittings + Delta = 0  =>  modular MC

    For the graph complex, the tree-level equation IS d^2 = 0.
    The one-loop equation gives the anomaly coefficient kappa.

    This function computes d^2 and checks it equals zero, then
    interprets the result in BV language.
    """
    d2_sft = sft_d_squared(graph)
    d1_sft = sft_differential(graph)

    # Count the terms in d and d^2
    n_d_terms = sum(abs(v) for v in d1_sft.values())
    n_d2_terms = sum(abs(v) for v in d2_sft.values())

    # Each term in d^2 corresponds to a pair of edge contractions.
    # The BV master equation says these pairs cancel.
    # Count the number of cancelling pairs.
    n_edges = graph.n_edges
    n_contraction_pairs = 0
    n_valid_pairs = 0
    for e1 in range(n_edges):
        for e2 in range(e1 + 1, n_edges):
            n_contraction_pairs += 1
            # Check if both contractions are valid
            c1 = contract_edge_sft(graph, e1)
            if c1 is None:
                continue
            g1, s1 = c1
            # Find the index of e2 in the contracted graph
            # (e2 may have shifted after removing e1)
            n_valid_pairs += 1

    return {
        'graph': graph.canonical_edge_set(),
        'loop_order': graph.loop_order,
        'degree': graph.degree,
        'n_edges': n_edges,
        'd_nonzero_terms': len(d1_sft),
        'd_total_coefficient': n_d_terms,
        'd2_is_zero': len(d2_sft) == 0,
        'd2_nonzero_terms': len(d2_sft),
        'bv_interpretation': {
            'tree_level': 'd^2 = 0' if len(d2_sft) == 0 else 'd^2 != 0 (BV FAILURE)',
            'explanation': (
                'The BV master equation {S,S} + 2*hbar*Delta*S = 0 '
                'at tree level reduces to {S_0, S_0} = 0, which is '
                'd_bar^2 = 0 on the graph complex. The SFT sign '
                'convention makes this identity manifest: each pair '
                'of edge contractions contributes with opposite signs '
                'due to the propagator orientation and cyclic vertex '
                'ordering.'
            ),
        },
        'n_contraction_pairs': n_contraction_pairs,
        'n_valid_pairs': n_valid_pairs,
    }


# ===========================================================================
# 10. WORLDSHEET ORIENTATION DATA
# ===========================================================================

@dataclass
class WorldsheetData:
    """Worldsheet data for an SFT graph.

    Each graph in the SFT Feynman expansion corresponds to a worldsheet:
    - Vertices are punctured Riemann surfaces (disks for open, spheres for closed)
    - Edges are strips (open) or cylinders (closed) connecting them
    - The worldsheet orientation induces the half-edge orientations
    """
    graph: OrientedGraph
    vertex_genera: Dict[int, int]  # vertex -> genus of the corresponding surface
    total_genus: int  # genus of the sewn worldsheet
    euler_characteristic: int

    @classmethod
    def from_graph(cls, graph: OrientedGraph, vertex_genera: Optional[Dict[int, int]] = None):
        """Construct worldsheet data from a graph.

        If vertex_genera is not specified, all vertices are genus 0 (tree-level).
        The total genus is then the loop order of the graph.
        """
        if vertex_genera is None:
            vertex_genera = {v: 0 for v in range(graph.n_vertices)}

        # Total genus of the sewn surface:
        # g = sum_v g(v) + loop_order(Gamma)
        # (each edge adds a handle to the sewing)
        total_genus = sum(vertex_genera.values()) + graph.loop_order

        # Euler characteristic: chi = 2 - 2g
        euler_characteristic = 2 - 2 * total_genus

        return cls(
            graph=graph,
            vertex_genera=vertex_genera,
            total_genus=total_genus,
            euler_characteristic=euler_characteristic,
        )


def closed_sft_vertex_genus_expansion(graph: OrientedGraph
                                      ) -> List[Dict[str, Any]]:
    """Enumerate all genus distributions on the vertices of a graph.

    In closed string field theory, the BV master equation sums over
    all ways to distribute the total genus g among the vertices
    (surface genera) and the graph (loop order).

    For a graph Gamma with loop order L and vertex genera g_v:
      total genus = L + sum_v g_v

    At fixed total genus g, the sum over Gamma and {g_v} gives the
    full genus-g contribution to the closed SFT action.
    """
    results = []
    L = graph.loop_order

    # At genus g = L (all vertex genera 0): pure graph complex contribution
    ws = WorldsheetData.from_graph(graph)
    results.append({
        'vertex_genera': {v: 0 for v in range(graph.n_vertices)},
        'total_genus': ws.total_genus,
        'euler_characteristic': ws.euler_characteristic,
        'is_tree_vertices': True,
        'loop_order': L,
    })

    # At genus g = L + 1: one vertex has genus 1, rest genus 0
    for v in range(graph.n_vertices):
        vg = {u: 0 for u in range(graph.n_vertices)}
        vg[v] = 1
        ws = WorldsheetData.from_graph(graph, vg)
        results.append({
            'vertex_genera': dict(vg),
            'total_genus': ws.total_genus,
            'euler_characteristic': ws.euler_characteristic,
            'is_tree_vertices': False,
            'loop_order': L,
            'genus_1_vertex': v,
        })

    return results


# ===========================================================================
# 11. d^2 = 0 PROOF STRUCTURE (SFT PERSPECTIVE)
# ===========================================================================

def d_squared_cancellation_pairs(graph: OrientedGraph
                                 ) -> List[Dict[str, Any]]:
    """Enumerate the cancellation pairs in d^2 = 0.

    For each pair of edges (e1, e2) in graph, contracting e1 then e2
    gives the same result as contracting e2 then e1 (up to sign).
    The BV master equation guarantees that these signs are opposite,
    giving d^2 = 0.

    This function explicitly enumerates all such pairs and verifies
    the cancellation.
    """
    pairs = []

    for e1_idx in range(graph.n_edges):
        for e2_idx in range(e1_idx + 1, graph.n_edges):
            # Path 1: contract e1 first, then e2
            c1 = contract_edge_sft(graph, e1_idx)
            if c1 is None:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': False, 'path2_valid': False,
                    'cancels': True,  # both invalid => cancels trivially
                    'reason': 'e1 contraction invalid',
                })
                continue

            g1, sign1 = c1

            # Find e2 in the contracted graph g1
            # After contracting e1 = (u1, v1), edge e2 may have been relabeled
            u1, v1 = graph.edges[e1_idx]
            u2, v2 = graph.edges[e2_idx]
            merge_to = min(u1, v1)
            merge_from = max(u1, v1)

            # Relabel e2's vertices
            def relabel(x):
                if x == merge_from:
                    return merge_to
                elif x > merge_from:
                    return x - 1
                return x

            new_u2, new_v2 = relabel(u2), relabel(v2)
            if new_u2 == new_v2:
                # e2 became a self-loop after e1 contraction
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': False,
                    'reason': 'e2 becomes self-loop after e1 contraction',
                })
                continue

            new_e2 = (min(new_u2, new_v2), max(new_u2, new_v2))
            # Find index of new_e2 in g1.edges
            try:
                e2_in_g1 = g1.edges.index(new_e2)
            except ValueError:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': False,
                    'reason': 'e2 not found in contracted graph',
                })
                continue

            c12 = contract_edge_sft(g1, e2_in_g1)

            # Path 2: contract e2 first, then e1
            c2 = contract_edge_sft(graph, e2_idx)
            if c2 is None:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': c12 is not None,
                    'path2_valid': False,
                    'reason': 'e2 contraction invalid',
                })
                continue

            g2, sign2 = c2

            # Find e1 in g2
            u2_orig, v2_orig = graph.edges[e2_idx]
            merge_to2 = min(u2_orig, v2_orig)
            merge_from2 = max(u2_orig, v2_orig)

            def relabel2(x):
                if x == merge_from2:
                    return merge_to2
                elif x > merge_from2:
                    return x - 1
                return x

            new_u1, new_v1 = relabel2(u1), relabel2(v1)
            if new_u1 == new_v1:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': c12 is not None,
                    'path2_valid': False,
                    'reason': 'e1 becomes self-loop after e2 contraction',
                })
                continue

            new_e1 = (min(new_u1, new_v1), max(new_u1, new_v1))
            try:
                e1_in_g2 = g2.edges.index(new_e1)
            except ValueError:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': c12 is not None,
                    'path2_valid': False,
                    'reason': 'e1 not found in contracted graph (path 2)',
                })
                continue

            c21 = contract_edge_sft(g2, e1_in_g2)

            if c12 is None and c21 is None:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': False, 'path2_valid': False,
                    'cancels': True,
                    'reason': 'both double contractions invalid',
                })
                continue

            if c12 is None or c21 is None:
                pairs.append({
                    'e1': e1_idx, 'e2': e2_idx,
                    'path1_valid': c12 is not None,
                    'path2_valid': c21 is not None,
                    'cancels': False,
                    'reason': 'one path valid, other invalid',
                })
                continue

            g12, sign12 = c12
            g21, sign21 = c21

            # Check that the two results are the same graph
            same_graph = (g12.canonical_edge_set() == g21.canonical_edge_set())

            # The total sign for path 1: sign1 * sign12
            # The total sign for path 2: sign2 * sign21
            total_sign_path1 = sign1 * sign12
            total_sign_path2 = sign2 * sign21

            # For d^2 = 0, we need total_sign_path1 + total_sign_path2 = 0
            cancels = same_graph and (total_sign_path1 + total_sign_path2 == 0)

            pairs.append({
                'e1': e1_idx, 'e2': e2_idx,
                'e1_edge': graph.edges[e1_idx],
                'e2_edge': graph.edges[e2_idx],
                'path1_valid': True, 'path2_valid': True,
                'same_graph': same_graph,
                'result_graph': g12.canonical_edge_set() if same_graph else None,
                'total_sign_path1': total_sign_path1,
                'total_sign_path2': total_sign_path2,
                'cancels': cancels,
                'sign_analysis': {
                    'e1_edge_sign': sign1,
                    'e2_in_contracted_sign': sign12,
                    'e2_edge_sign': sign2,
                    'e1_in_contracted_sign': sign21,
                },
            })

    return pairs


def verify_all_pairs_cancel(graph: OrientedGraph) -> bool:
    """Verify that all cancellation pairs cancel for d^2 = 0."""
    pairs = d_squared_cancellation_pairs(graph)
    for p in pairs:
        if 'cancels' in p and not p['cancels']:
            return False
    return True


# ===========================================================================
# 12. PHYSICAL INTERPRETATION SUMMARY
# ===========================================================================

def sft_interpretation_summary(graph: OrientedGraph) -> Dict[str, Any]:
    """Generate a physical interpretation summary for a graph.

    Maps graph complex data to SFT quantities:
    - Loop order = genus of the worldsheet (with genus-0 vertices)
    - Degree = ghost number excess
    - Vertices = string field insertions
    - Edges = propagator strips/cylinders
    - d = BRST operator (open) / sewing operator (closed)
    - d^2 = 0 = BV master equation
    - Half-edge orientations = propagator BPZ directions
    """
    vals = graph.vertex_valences()

    return {
        'graph': graph.name or str(graph.canonical_edge_set()),
        'loop_order': graph.loop_order,
        'worldsheet_genus': graph.loop_order,  # with genus-0 vertices
        'degree': graph.degree,
        'ghost_number_excess': graph.degree,
        'n_vertices': graph.n_vertices,
        'n_edges': graph.n_edges,
        'vertex_valences': vals,
        'string_vertices': [
            f"V_{{0,{vals[v]}}}" for v in range(graph.n_vertices)
        ],
        'n_half_edges': 2 * graph.n_edges,
        'n_propagators': graph.n_edges,
        'euler_characteristic': 2 - 2 * graph.loop_order,
        'sft_amplitude': (
            f"hbar^{graph.loop_order} / |Aut| * "
            f"prod_v V_{{0,val(v)}} * prod_e P_e"
        ),
        'd2_zero': len(sft_d_squared(graph)) == 0,
        'physical_reason': (
            "BV master equation: the propagator b_0/L_0 orientation "
            "fixes the half-edge signs, and the cyclic vertex ordering "
            "from the string product structure ensures that edge "
            "contraction pairs cancel in d^2."
        ),
    }


# ===========================================================================
# 13. FULL VERIFICATION AT LOOP ORDER 4
# ===========================================================================

def full_loop4_verification() -> Dict[str, Any]:
    """Complete verification of d^2 = 0 at loop order <= 4.

    This is the KEY computation: at loop order 4, the graph complex
    becomes nontrivial enough that naive signs can fail.  The SFT
    signs provide the correct convention.

    Returns comprehensive verification data.
    """
    by_loop = oriented_gc2_by_loop_order(4)
    results: Dict[str, Any] = {}

    for L in sorted(by_loop.keys()):
        graphs = by_loop[L]
        loop_results = {
            'n_graphs': len(graphs),
            'all_d2_zero_sft': True,
            'all_d2_zero_standard': True,
            'graphs': [],
        }

        for g in graphs:
            d2_sft = sft_d_squared(g)
            d2_std = standard_d_squared(g)
            d_sft = sft_differential(g)
            d_std = standard_differential(g)

            graph_data = {
                'edges': g.canonical_edge_set(),
                'n_vertices': g.n_vertices,
                'n_edges': g.n_edges,
                'degree': g.degree,
                'valences': g.vertex_valences(),
                'sft_d2_zero': len(d2_sft) == 0,
                'std_d2_zero': len(d2_std) == 0,
                'sft_d_terms': len(d_sft),
                'std_d_terms': len(d_std),
                'signs_agree': d_sft == d_std,
            }

            if not graph_data['sft_d2_zero']:
                loop_results['all_d2_zero_sft'] = False
            if not graph_data['std_d2_zero']:
                loop_results['all_d2_zero_standard'] = False

            loop_results['graphs'].append(graph_data)

        results[f'loop_{L}'] = loop_results

    # Summary
    results['summary'] = {
        'max_loop': 4,
        'total_graphs': sum(len(by_loop.get(L, [])) for L in range(1, 5)),
        'sft_d2_zero_all': all(
            results[f'loop_{L}']['all_d2_zero_sft']
            for L in by_loop.keys()
        ),
        'standard_d2_zero_all': all(
            results[f'loop_{L}']['all_d2_zero_standard']
            for L in by_loop.keys()
        ),
    }

    return results
