"""Stable graph enumeration and graph amplitude engine for the modular bar construction.

A **stable graph** Gamma = (V, H, g, iota, sigma) consists of:
  V = vertex set, with genus labeling g: V -> Z>=0
  H = half-edge set
  iota: H -> V assigns each half-edge to a vertex
  sigma: H -> H is an involution (fixed points = legs/marked points, 2-cycles = edges)
  Stability: 2g(v) - 2 + val(v) > 0 for all v in V

The **arithmetic genus** is g(Gamma) = h^1(Gamma) + sum_{v in V} g(v),
where h^1 = |E| - |V| + (number of connected components).

This module provides:
  1. StableGraph dataclass with genus, edge, leg, stability, automorphism computations
  2. Explicit enumerations for small (g, n): genus 0 n=3,4; genus 1 n=0,1; genus 2 n=0
  3. General enumeration for g <= 3, n <= 4
  4. Orbifold Euler characteristic via the graph-vertex-product formula
  5. Graph amplitude evaluation for scalar-level shadow obstruction tower computations

References:
  - Faber, "A conjectural description of the tautological ring" (1999)
  - Harer-Zagier, "The Euler characteristic of the moduli space of curves" (1986)
  - higher_genus_modular_koszul.tex, def:stable-graph-coefficient-algebra
  - concordance.tex, const:vol1-genus-spectral-sequence
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Set
from fractions import Fraction
from itertools import combinations, permutations, product as cartprod
from functools import lru_cache
from math import factorial
from collections import Counter


# ---------------------------------------------------------------------------
# Core dataclass
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class StableGraph:
    """A stable graph (vertex genera, edges, legs).

    Vertices are integers 0..num_vertices-1.
    Edges are pairs (v1, v2) with v1 <= v2 (v1 == v2 for self-loops).
    Legs (marked points) are assigned to vertices: legs[i] = vertex carrying leg i.

    The edge tuple may contain repeated pairs for multi-edges.
    """
    vertex_genera: Tuple[int, ...]        # g(v) for each vertex
    edges: Tuple[Tuple[int, int], ...]    # (v1, v2) pairs, v1 <= v2
    legs: Tuple[int, ...]                 # legs[i] = vertex assignment for marked pt i

    @property
    def num_vertices(self) -> int:
        return len(self.vertex_genera)

    @property
    def num_edges(self) -> int:
        return len(self.edges)

    @property
    def num_legs(self) -> int:
        return len(self.legs)

    @property
    def first_betti(self) -> int:
        """h^1(Gamma) = |E| - |V| + number of connected components.

        For connected graphs: h^1 = |E| - |V| + 1.
        """
        return self.num_edges - self.num_vertices + self._num_connected_components()

    @property
    def arithmetic_genus(self) -> int:
        """g(Gamma) = h^1(Gamma) + sum g(v)."""
        return self.first_betti + sum(self.vertex_genera)

    @property
    def valence(self) -> Tuple[int, ...]:
        """val(v) for each vertex.

        Each edge (v1, v2) contributes:
          - 2 to val(v1) if v1 == v2 (self-loop)
          - 1 to val(v1) and 1 to val(v2) if v1 != v2
        Each leg on v contributes 1 to val(v).
        """
        val = [0] * self.num_vertices
        for v1, v2 in self.edges:
            if v1 == v2:
                val[v1] += 2
            else:
                val[v1] += 1
                val[v2] += 1
        for v in self.legs:
            val[v] += 1
        return tuple(val)

    @property
    def is_stable(self) -> bool:
        """Check 2g(v) - 2 + val(v) > 0 for all vertices."""
        val = self.valence
        for v in range(self.num_vertices):
            if 2 * self.vertex_genera[v] - 2 + val[v] <= 0:
                return False
        return True

    @property
    def is_connected(self) -> bool:
        return self._num_connected_components() == 1

    def _num_connected_components(self) -> int:
        """Count connected components using union-find."""
        if self.num_vertices == 0:
            return 0
        parent = list(range(self.num_vertices))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for v1, v2 in self.edges:
            union(v1, v2)
        return len(set(find(v) for v in range(self.num_vertices)))

    def automorphism_order(self) -> int:
        """Compute |Aut(Gamma)| by brute force for small graphs.

        An automorphism of a stable graph with labeled legs is a pair
        (pi_V, pi_H) where:
          - pi_V: V -> V is a vertex permutation preserving genera
          - pi_H permutes half-edges compatibly with pi_V and sigma
          - All LEGS (marked points) are FIXED

        For practical computation: enumerate vertex permutations preserving
        genera that also preserve the leg assignment. For each such vertex
        permutation, count the number of compatible edge matchings.

        For each vertex permutation pi_V:
          1. Check pi_V fixes all legs: legs[i] must map to legs[i], so
             pi_V(legs[i]) = legs[i] for all i.
          2. The multiset of edges {(pi_V(v1), pi_V(v2))} must equal {(v1, v2)}.
          3. For multi-edges between the same pair, we can permute them: k! ways.
          4. For self-loops, each loop can be "flipped" (swap its half-edges): 2 per loop.
        """
        n = self.num_vertices
        if n > 7:
            raise ValueError("Brute force automorphism too expensive for > 7 vertices")

        # Group vertices by genus for efficient permutation enumeration
        count = 0
        for perm in _genus_preserving_permutations(self.vertex_genera):
            # Check leg compatibility: perm must fix leg assignments
            if not all(perm[self.legs[i]] == self.legs[i] for i in range(self.num_legs)):
                continue

            # Map edges under perm
            mapped_edges = tuple(sorted(
                (min(perm[v1], perm[v2]), max(perm[v1], perm[v2]))
                for v1, v2 in self.edges
            ))
            original_edges = tuple(sorted(self.edges))

            if mapped_edges != original_edges:
                continue

            # Count edge matchings: for each group of identical edges, we
            # can permute them. For self-loops, each loop also has a flip.
            edge_factor = _edge_automorphism_factor(self.edges, perm)
            count += edge_factor

        return count

    def self_loop_count(self, v: int) -> int:
        """Number of self-loops at vertex v."""
        return sum(1 for v1, v2 in self.edges if v1 == v2 == v)

    def edge_multiplicity(self, v1: int, v2: int) -> int:
        """Number of edges between v1 and v2 (with v1 != v2)."""
        a, b = min(v1, v2), max(v1, v2)
        return sum(1 for e in self.edges if e == (a, b))

    def __repr__(self) -> str:
        parts = [f"genera={self.vertex_genera}"]
        if self.edges:
            parts.append(f"edges={self.edges}")
        if self.legs:
            parts.append(f"legs={self.legs}")
        return f"StableGraph({', '.join(parts)})"


# ---------------------------------------------------------------------------
# Permutation helpers
# ---------------------------------------------------------------------------

def _genus_preserving_permutations(genera: Tuple[int, ...]):
    """Yield all permutations of vertices that preserve the genus labeling."""
    n = len(genera)
    # Group vertices by genus
    genus_groups: Dict[int, List[int]] = {}
    for v, g in enumerate(genera):
        genus_groups.setdefault(g, []).append(v)

    # Generate permutations within each genus group
    group_perms = []
    for g in sorted(genus_groups.keys()):
        verts = genus_groups[g]
        group_perms.append((verts, list(permutations(verts))))

    # Take cartesian product of group permutations
    if not group_perms:
        yield tuple(range(n))
        return

    perm_lists = [gp[1] for gp in group_perms]
    vert_lists = [gp[0] for gp in group_perms]

    for combo in cartprod(*perm_lists):
        perm = list(range(n))
        for verts, mapping in zip(vert_lists, combo):
            for src, dst in zip(verts, mapping):
                perm[src] = dst
        yield tuple(perm)


def _edge_automorphism_factor(edges: Tuple[Tuple[int, int], ...],
                              vertex_perm: Tuple[int, ...]) -> int:
    """Count edge-level automorphisms compatible with a vertex permutation.

    Given that vertex_perm maps the edge multiset to itself, count the number
    of ways to match the mapped edges to the original edges, including:
      - Permutations of parallel edges between the same vertex pair
      - Self-loop half-edge flips (each self-loop contributes a factor of 2)
    """
    # Normalize edges under the vertex permutation
    mapped = []
    for v1, v2 in edges:
        a, b = vertex_perm[v1], vertex_perm[v2]
        mapped.append((min(a, b), max(a, b)))

    # Group original edges by their (v1, v2) pair
    original_groups: Dict[Tuple[int, int], int] = Counter(edges)
    mapped_groups: Dict[Tuple[int, int], int] = Counter(mapped)

    # The mapped groups must equal the original groups (already checked by caller)
    if original_groups != mapped_groups:
        return 0

    # For each edge group, the mapped edges must be matched to original edges.
    # For a group of k parallel edges between (a, b):
    #   - k! permutations of the edges
    #   - If a == b (self-loops), each loop can also be flipped: 2^k
    factor = 1
    for (a, b), k in original_groups.items():
        # The vertex perm maps this group to itself (since mapped_groups == original_groups).
        # We need to find how many ways the k mapped edges can be assigned to the k
        # original edges. This depends on whether the vertex perm fixes or swaps a and b.
        #
        # If vertex_perm maps (a,b) to (a,b) [same pair], then any permutation
        # of the k edges works: k! ways.
        # The flip factor for self-loops is independent.
        factor *= factorial(k)
        if a == b:
            factor *= (2 ** k)

    return factor


# ---------------------------------------------------------------------------
# Explicit enumerations for small (g, n)
# ---------------------------------------------------------------------------

def genus0_stable_graphs_n3() -> List[StableGraph]:
    """The 1 genus-0 stable graph with 3 marked points.

    1. Point: 1 vertex g=0, 3 legs. |Aut|=1.
    """
    return [
        StableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0)),
    ]


def genus0_stable_graphs_n4() -> List[StableGraph]:
    """The 4 genus-0 stable graphs with 4 marked points.

    1. Point: 1 vertex g=0, 4 legs. |Aut|=1.
    2. Channel (12|34): 2 vertices g=0, 1 edge. |Aut|=1.
    3. Channel (13|24): 2 vertices g=0, 1 edge. |Aut|=1.
    4. Channel (14|23): 2 vertices g=0, 1 edge. |Aut|=1.
    """
    return [
        StableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0, 0)),
        StableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 0, 1, 1)),
        StableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 1, 0, 1)),
        StableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 1, 1, 0)),
    ]


def genus1_stable_graphs_n0() -> List[StableGraph]:
    """The 2 genus-1 stable graphs with no marked points.

    1. Smooth torus: 1 vertex g=1, no edges. |Aut|=1.
    2. Nodal rational: 1 vertex g=0, 1 self-loop. |Aut|=2.
    """
    return [
        StableGraph(vertex_genera=(1,), edges=(), legs=()),
        StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=()),
    ]


def genus1_stable_graphs_n1() -> List[StableGraph]:
    """The 2 genus-1 stable graphs with 1 marked point.

    1. Smooth: 1 vertex g=1, 1 leg. |Aut|=1.
    2. Self-node: 1 vertex g=0, 1 self-loop, 1 leg. |Aut|=2.
    """
    return [
        StableGraph(vertex_genera=(1,), edges=(), legs=(0,)),
        StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=(0,)),
    ]


def genus1_stable_graphs_n2() -> List[StableGraph]:
    """The 5 genus-1 stable graphs with 2 marked points.

    1. Smooth: 1 vertex g=1, 2 legs. |Aut|=1.
    2. Self-node: 1 vertex g=0, 1 self-loop, 2 legs. |Aut|=2.
    3. Separating: vertex g=1 (val=1) -- edge -- vertex g=0 (2 legs, val=3). |Aut|=1.
    4. Self-loop + bridge: vertex g=0 (self-loop + edge, val=3) --
       vertex g=0 (2 legs + edge, val=3). |Aut|=2.
    5. Double bridge: 2 vertices g=0, 2 parallel edges, 1 leg on each. |Aut|=2.
    """
    return [
        StableGraph(vertex_genera=(1,), edges=(), legs=(0, 0)),
        StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=(0, 0)),
        StableGraph(vertex_genera=(1, 0), edges=((0, 1),), legs=(1, 1)),
        StableGraph(vertex_genera=(0, 0), edges=((0, 0), (0, 1)), legs=(1, 1)),
        StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1)), legs=(0, 1)),
    ]


def genus2_stable_graphs_n0() -> List[StableGraph]:
    """The 7 genus-2 stable graphs with no marked points.

    1. Smooth: 1 vertex g=2, no edges. |Aut|=1.
    2. Irreducible node: 1 vertex g=1, 1 self-loop. |Aut|=2. (Delta_irr at genus 1)
    3. Banana: 1 vertex g=0, 2 self-loops. |Aut|=8.
    4. Separating: 2 vertices g=1,g=1, 1 edge. |Aut|=2. (Delta_1)
    5. Theta: 2 vertices g=0,g=0, 3 parallel edges. |Aut|=12.
    6. Mixed: vertex g=0 (1 self-loop, 1 half-edge) -- edge -- vertex g=1. |Aut|=2.
    7. Barbell: 2 vertices g=0,g=0 each with one self-loop, joined by a bridge.
       |Aut|=8: vertex swap x reversal of self-loop A x reversal of self-loop B
       generate (Z/2)^3.  h^1 = 3 edges - 2 vertices + 1 component = 2;
       sum g = 0; total g = 2.
    """
    return [
        # 1. Smooth genus-2 curve
        StableGraph(vertex_genera=(2,), edges=(), legs=()),
        # 2. Genus-1 vertex with one self-loop: h^1 = 1, sum g = 1, total g = 2
        StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=()),
        # 3. Genus-0 vertex with two self-loops: h^1 = 2, sum g = 0, total g = 2
        StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=()),
        # 4. Two genus-1 vertices, one edge: h^1 = 0, sum g = 2, total g = 2
        StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=()),
        # 5. Two genus-0 vertices, three parallel edges: h^1 = 2, sum g = 0, total g = 2
        StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=()),
        # 6. Genus-0 with self-loop + edge to genus-1: h^1 = 1, sum g = 1, total g = 2
        StableGraph(vertex_genera=(0, 1), edges=((0, 0), (0, 1)), legs=()),
        # 7. Barbell: two genus-0 vertices, each with a self-loop, joined by a bridge
        StableGraph(vertex_genera=(0, 0), edges=((0, 0), (1, 1), (0, 1)), legs=()),
    ]


# ---------------------------------------------------------------------------
# Orbifold Euler characteristic
# ---------------------------------------------------------------------------

@lru_cache(maxsize=128)
def _chi_orb_open(g: int, n: int) -> Fraction:
    """Orbifold Euler characteristic of M_{g,n} (the OPEN moduli space).

    For 2g - 2 + n > 0:
      chi^orb(M_{0,n}) = (-1)^{n-1} (n-3)!  for n >= 3
      chi^orb(M_{1,1}) = -1/12
      chi^orb(M_{g,n}) for g >= 1 uses the Harer-Zagier recursion:
        chi^orb(M_{g,n+1}) = (2g - 2 + n) * chi^orb(M_{g,n})

    and for n = 0, g >= 2:
      chi^orb(M_g) = B_{2g} / (4g(g-1))

    The base cases and the recursion chi(M_{g,n+1}) = (2g-2+n) chi(M_{g,n})
    follow from the forgetful map M_{g,n+1} -> M_{g,n} being a fiber bundle
    with fiber a (2g-2+n)-punctured surface (orbifold Euler char = 2g-2+n-1+1 = ...).
    Actually the recursion is:
      chi(M_{g,n+1}) = (2g - 2 + n) * chi(M_{g,n})
    """
    if 2 * g - 2 + n <= 0:
        raise ValueError(f"Unstable moduli M_{{{g},{n}}}: 2g-2+n = {2*g-2+n} <= 0")

    # Genus 0
    if g == 0:
        if n < 3:
            raise ValueError(f"M_{{0,{n}}} is unstable")
        return Fraction((-1) ** (n - 1) * factorial(n - 3))

    # Genus >= 1, use known base and recursion
    # Base: chi(M_{g,0}) for g >= 2 from Harer-Zagier
    # chi(M_{1,1}) = -1/12
    if g == 1 and n == 1:
        return Fraction(-1, 12)

    if g >= 2 and n == 0:
        return _chi_orb_harer_zagier(g)

    if g == 1 and n == 0:
        raise ValueError("M_{1,0} is unstable (2g-2+n = 0)")

    # Recursion: chi(M_{g,n}) = (2g - 2 + n - 1) * chi(M_{g,n-1})
    return Fraction(2 * g - 2 + n - 1) * _chi_orb_open(g, n - 1)


def _chi_orb_harer_zagier(g: int) -> Fraction:
    """chi^orb(M_g) = B_{2g} / (4g(g-1)) for g >= 2.

    Uses exact Bernoulli numbers via the von Staudt-Clausen theorem.
    """
    B_2g = _bernoulli_exact(2 * g)
    return B_2g / Fraction(4 * g * (g - 1))


@lru_cache(maxsize=64)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n as a Fraction.

    Uses the recursive definition:
      sum_{k=0}^{n} C(n+1, k) B_k = 0  for n >= 1, with B_0 = 1.
    """
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    # Recursion: B_n = -1/(n+1) * sum_{k=0}^{n-1} C(n+1, k) * B_k
    s = Fraction(0)
    for k in range(n):
        bk = _bernoulli_exact(k)
        if bk != 0:
            s += Fraction(_comb(n + 1, k)) * bk
    return -s / Fraction(n + 1)


def _comb(n: int, k: int) -> int:
    """Binomial coefficient C(n, k)."""
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def orbifold_euler_characteristic(graphs: List[StableGraph]) -> Fraction:
    """Compute chi^orb(M_bar_{g,n}) via the graph-vertex-product formula:

      chi^orb(M_bar_{g,n}) = sum_Gamma prod_{v in V(Gamma)} chi^orb(M_{g(v), val(v)})
                                        / |Aut(Gamma)|

    This formula follows from the stratification of M_bar_{g,n} by topological
    type. Each stratum M_Gamma is isomorphic (as an orbifold) to
    prod_v M_{g(v), val(v)} / Aut(Gamma).

    The key consistency checks (all as orbifold Euler characteristics):
      chi^orb(M_bar_{0,3}) = 1
      chi^orb(M_bar_{1,1}) = -1/12 + 1/2 = 5/12
      chi^orb(M_bar_{2,0}) = sum of 6 weighted vertex products
    """
    total = Fraction(0)
    for gamma in graphs:
        val = gamma.valence
        vertex_product = Fraction(1)
        for v in range(gamma.num_vertices):
            vertex_product *= _chi_orb_open(gamma.vertex_genera[v], val[v])
        aut = gamma.automorphism_order()
        total += vertex_product / Fraction(aut)
    return total


def graph_weight(graph: StableGraph) -> Fraction:
    """Compute (-1)^{|E|} / |Aut(Gamma)|.

    This is the combinatorial weight of the graph in various graph-sum formulas.
    """
    sign = (-1) ** graph.num_edges
    return Fraction(sign, graph.automorphism_order())


# ---------------------------------------------------------------------------
# Known orbifold Euler characteristics for validation
# ---------------------------------------------------------------------------

KNOWN_CHI_MBAR: Dict[Tuple[int, int], Fraction] = {
    (0, 3): Fraction(1),
    (0, 4): Fraction(2),         # chi^top(P^1) = 2
    (1, 1): Fraction(5, 12),     # chi^orb = -1/12 + 1/2
}
# chi^orb(M_bar_{2,0}) is computed from the 6-graph sum — see tests.


# ---------------------------------------------------------------------------
# General enumeration engine
# ---------------------------------------------------------------------------

def enumerate_stable_graphs(g: int, n: int) -> List[StableGraph]:
    """Enumerate all connected stable graphs of arithmetic genus g with n marked points.

    Complete and correct for g <= 3, n <= 4 (enumeration by graph topology).
    For efficiency, uses the explicit functions for known (g, n) pairs.
    """
    # Use explicit enumerations where available
    if g == 0 and n == 3:
        return genus0_stable_graphs_n3()
    if g == 0 and n == 4:
        return genus0_stable_graphs_n4()
    if g == 1 and n == 0:
        return genus1_stable_graphs_n0()
    if g == 1 and n == 1:
        return genus1_stable_graphs_n1()
    if g == 1 and n == 2:
        return genus1_stable_graphs_n2()
    if g == 2 and n == 0:
        return genus2_stable_graphs_n0()

    # General enumeration: generate all graph topologies
    if 2 * g - 2 + n <= 0:
        return []  # unstable

    return _enumerate_general(g, n)


def _enumerate_general(g: int, n: int) -> List[StableGraph]:
    """General enumeration of stable graphs by building all possible topologies.

    Strategy: iterate over number of vertices V, then for each V:
      1. Choose genus distribution (g_1, ..., g_V) with sum <= g
      2. The number of edges E is determined: h^1 = g - sum(g_v), so E = h^1 + V - 1
         (for connected graphs: h^1 = E - V + 1)
      3. Build all edge configurations with E edges on V vertices
      4. Distribute n legs across vertices
      5. Filter by stability and connectedness
      6. Deduplicate (up to isomorphism preserving leg labels)
    """
    results = []
    # Maximum number of vertices: at most 2g - 2 + n (from stability:
    # each vertex needs 2g(v)-2+val(v) > 0, and total = 2g-2+n = sum of these)
    max_vertices = max(1, 2 * g - 2 + n)

    seen = set()

    for num_v in range(1, max_vertices + 1):
        # Enumerate genus distributions
        for genera in _genus_distributions(g, num_v):
            sum_gv = sum(genera)
            h1_needed = g - sum_gv
            if h1_needed < 0:
                continue
            num_edges = h1_needed + num_v - 1  # for connected: E = h1 + V - 1

            if num_edges < 0:
                continue

            # Enumerate edge configurations: num_edges edges on num_v vertices
            for edges in _edge_configurations(num_v, num_edges):
                # Enumerate leg distributions: n legs on num_v vertices
                for legs in _leg_distributions(num_v, n):
                    graph = StableGraph(
                        vertex_genera=genera,
                        edges=edges,
                        legs=legs,
                    )
                    if not graph.is_stable:
                        continue
                    if not graph.is_connected:
                        continue
                    if graph.arithmetic_genus != g:
                        continue

                    # Canonical form for deduplication
                    canon = _canonical_form(graph)
                    if canon not in seen:
                        seen.add(canon)
                        results.append(graph)

    return results


def _genus_distributions(total_genus: int, num_vertices: int):
    """Generate all non-increasing tuples of non-negative integers summing to <= total_genus."""
    if num_vertices == 0:
        yield ()
        return
    if num_vertices == 1:
        for g in range(total_genus + 1):
            yield (g,)
        return
    for g in range(total_genus, -1, -1):
        for rest in _genus_distributions(total_genus - g, num_vertices - 1):
            # Ensure non-increasing for canonical ordering
            if rest and rest[0] > g:
                continue
            yield (g,) + rest


def _edge_configurations(num_vertices: int, num_edges: int):
    """Generate all multisets of edges (including self-loops and multi-edges)."""
    # List all possible edge types: (i, j) with 0 <= i <= j < num_vertices
    edge_types = []
    for i in range(num_vertices):
        for j in range(i, num_vertices):
            edge_types.append((i, j))

    yield from _multiset_combinations(edge_types, num_edges)


def _multiset_combinations(items, k, start=0):
    """Generate all multisets of size k from items[start:]."""
    if k == 0:
        yield ()
        return
    for i in range(start, len(items)):
        for rest in _multiset_combinations(items, k - 1, i):
            yield (items[i],) + rest


def _leg_distributions(num_vertices: int, num_legs: int):
    """Generate all ways to assign num_legs labeled legs to num_vertices vertices.

    Each leg is labeled (by its index), so we enumerate all functions
    {0, ..., num_legs-1} -> {0, ..., num_vertices-1}.
    """
    if num_legs == 0:
        yield ()
        return
    for assignment in cartprod(range(num_vertices), repeat=num_legs):
        yield assignment


def _canonical_form(graph: StableGraph) -> Tuple:
    """Compute a canonical form for deduplication.

    Two stable graphs (with labeled legs) are isomorphic if there is a
    vertex permutation that preserves genera, maps edges to edges (as
    multisets), and preserves leg assignments.

    We compute the lexicographically smallest representation over all
    genus-preserving vertex permutations.
    """
    best = None
    for perm in _genus_preserving_permutations(graph.vertex_genera):
        # Map genera
        new_genera = tuple(graph.vertex_genera[perm.index(i)] for i in range(len(perm)))
        # Actually, perm[old] = new, so new_genera[new] = old_genera[old]
        # We want: for new vertex i, its genus is genera[perm^{-1}(i)]
        # Since perm maps old -> new: perm[old] = new
        # So inv_perm[new] = old, meaning genera[inv_perm[new]]
        inv = [0] * len(perm)
        for old, new in enumerate(perm):
            inv[new] = old

        new_genera = tuple(graph.vertex_genera[inv[i]] for i in range(len(perm)))
        new_edges = tuple(sorted(
            (min(perm[v1], perm[v2]), max(perm[v1], perm[v2]))
            for v1, v2 in graph.edges
        ))
        new_legs = tuple(perm[v] for v in graph.legs)

        rep = (new_genera, new_edges, new_legs)
        if best is None or rep < best:
            best = rep

    return best


# ---------------------------------------------------------------------------
# Graph amplitude evaluation
# ---------------------------------------------------------------------------

def graph_amplitude_scalar(graph: StableGraph, kappa: Fraction,
                           dim: int = 1) -> Fraction:
    """Evaluate the scalar graph amplitude ell_Gamma = kappa^{|E|}.

    At the scalar level (Theorem D), each edge contributes a single power
    of the modular characteristic kappa. The full graph amplitude is the
    product of edge contributions divided by the automorphism factor.

    This is the leading term in the shadow obstruction tower expansion. The full
    amplitude involves integration over vertex moduli M_{g(v),val(v)}.
    """
    return kappa ** graph.num_edges


def heisenberg_free_energy(g: int, k: Fraction = Fraction(1),
                           d: int = 1) -> Fraction:
    """F_g(H_k^d) = kappa(H_k^d) * lambda_g^FP.

    For Heisenberg of rank d at level k:
      kappa(H_k^d) = k * d  (trace of the invariant pairing on generators)
      lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    Explicit values:
      F_1(H_k) = k/24,  F_2(H_k) = 7k/5760,  F_3(H_k) = 31k/967680.
    """
    kappa_val = k * d
    return kappa_val * _lambda_fp_exact(g)


def affine_sl2_free_energy(g: int, k: Fraction = Fraction(1)) -> Fraction:
    """F_g(V_k(sl_2)) = kappa(V_k(sl_2)) * lambda_g^FP.

    For the affine Kac-Moody algebra V_k(sl_2):
      kappa(V_k(sl_2)) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k + 2) / 4

    where h^v = 2 is the dual Coxeter number of sl_2. The shifted level
    (k + h^v) appears from the one-loop determinant correction to the
    bare level k.

    Explicit: F_1(V_k(sl_2)) = 3(k+2)/(4*24) = (k + 2)/32.
    """
    dim_g = 3
    h_dual = 2
    # AP128: was dim_g*(k+h)/2, missing h_dual in denominator.
    # Correct: dim_g*(k+h)/(2*h). Verified: k=1 gives 9/4, F_1 = 9/(4*24) = 3/32.
    kappa_val = Fraction(dim_g * (k + h_dual), 2 * h_dual)
    return kappa_val * _lambda_fp_exact(g)


@lru_cache(maxsize=32)
def _lambda_fp_exact(g: int) -> Fraction:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    g=1: (1) * (1/6) / (2 * 2) = 1/24
    g=2: (7) * (1/30) / (8 * 24) = 7/5760
    g=3: (31) * (1/42) / (32 * 720) = 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    abs_B_2g = abs(B_2g)
    numerator = (2 ** (2 * g - 1) - 1) * abs_B_2g
    denominator = Fraction(2 ** (2 * g - 1) * factorial(2 * g))
    return numerator / denominator


def graph_sum_scalar(graphs: List[StableGraph], kappa: Fraction) -> Fraction:
    """Compute the scalar graph sum: sum_Gamma |Aut(Gamma)|^{-1} * ell_Gamma.

    At the scalar level, ell_Gamma = kappa^{|E(Gamma)|}.
    """
    total = Fraction(0)
    for gamma in graphs:
        aut = gamma.automorphism_order()
        amp = kappa ** gamma.num_edges
        total += amp / Fraction(aut)
    return total
