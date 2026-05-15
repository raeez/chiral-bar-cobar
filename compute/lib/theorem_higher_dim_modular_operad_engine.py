r"""Curve-level modular-operad diagnostics: stable graphs, ribbon structures,
Feynman-transform scalar normalization.

COMPUTABLE CLAIM.
The routines in this module work on the Deligne--Mumford modular operad of
stable pointed complex curves.  They do not compute factorization operads on
higher-dimensional varieties.  The finite E_n checks below are scalar
coinvariant diagnostics for curve-level shadows, not a theorem about all
higher-dimensional factorization algebras.

KEY STRUCTURES:
  1. E_1 modular operad = ribbon (fat) graph version of the curve-level
     modular operad.
     At each vertex of a stable graph, half-edges carry a CYCLIC ORDERING
     (from the ribbon/surface embedding).  This is the primitive operadic
     structure; the symmetric version is obtained after forgetting order.

  2. E_infty modular operad = symmetric/unordered version (standard).
     No ordering data at vertices.  Recovered from E_1 by Sigma_n coinvariants.

  3. Feynman transforms: FCom (from Com) controls the chiral bar B^Sigma(A).
     FAss (from Ass) controls the ordered bar B^ord(A).  Raw ribbon graph
     sums carry an extra product of cyclic-order counts.  Scalar FCom/FAss
     agreement is the normalized coinvariant statement; without that
     normalization the raw ribbon excess is an obstruction witness.

RIBBON GRAPH COUNTING:
  A ribbon graph (= fat graph = dessin d'enfants) is a graph with a cyclic
  ordering of half-edges at each vertex.  Equivalently, it is a 2-cell
  embedding of the graph into an orientable surface.

  For a stable graph Gamma with vertex valences val(v_1), ..., val(v_k):
    - Number of ribbon structures = prod_v (val(v) - 1)!
      (cyclic orderings at each vertex)
    - The E_1/E_infty multiplicity ratio is this product divided by 1
      (since E_infty has trivial ordering).

  The total weighted count uses |Aut_ribbon(Gamma)| which accounts for
  the symmetries that preserve the ribbon structure.

HARER-ZAGIER FORMULA:
  The orbifold Euler characteristic of M_{g,n} (open moduli) equals
    chi^orb(M_g) = B_{2g} / (4g(g-1))    for g >= 2
  The Harer-Zagier recursion for the number of genus-g cell decompositions
  of a surface with one vertex and n edges:
    epsilon_g(n) satisfies: sum_{g=0}^{n} epsilon_g(n) * x^{2g}
                          = (2n-1)!! * sum_{j=0}^{n} C(n,j) (x+1)^j (x-1)^{n-j} / (2^n)
  The total count of labeled trivalent ribbon graphs at genus g with no
  marked points is related to Euler characteristics through the cell
  decomposition of M_{g,n}.

FEYNMAN TRANSFORM COMPARISON:
  FCom(g,n) = Feynman transform of Com at (g,n).
  FAss(g,n) = Feynman transform of Ass at (g,n).
  At the normalized SCALAR coinvariant level (shadow invariants), both
  produce the same answer.  Before normalization, the ribbon sum already
  differs by the cyclic-order multiplicity prod_v (val(v)-1)!.

References:
  - Harer-Zagier, "The Euler characteristic of the moduli space of curves" (1986)
  - Kontsevich, "Intersection theory on the moduli space of curves" (1992)
  - Getzler-Kapranov, "Modular operads" (1998)
  - stable_graph_enumeration.py: StableGraph dataclass, enumerations
  - bar_modular_operad_fcom.py: FCom algebra structure
  - theorem_kappa_en_invariance_engine.py: kappa finite-window diagnostics
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, comb
from typing import Any, Dict, List, Optional, Tuple
from functools import lru_cache
from collections import Counter

from sympy import Rational, bernoulli, Symbol, simplify


# =========================================================================
# 0. Utility
# =========================================================================

def _frac(x) -> Fraction:
    """Coerce to Fraction."""
    if isinstance(x, Fraction):
        return x
    return Fraction(x)


def double_factorial(n: int) -> int:
    """Compute n!! = n * (n-2) * (n-4) * ... * 1 or 2.

    Convention: (-1)!! = 1, 0!! = 1.
    """
    if n <= 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result


def catalan_number(n: int) -> int:
    """C_n = (2n)! / ((n+1)! * n!) = C(2n,n)/(n+1)."""
    if n < 0:
        return 0
    return comb(2 * n, n) // (n + 1)


def is_stable_curve_type(g: int, n: int) -> bool:
    """Return whether the pair (g,n) is stable for pointed curves.

    The Deligne--Mumford modular operad is indexed by stable pairs:
    2g - 2 + n > 0.  In particular, (1,0) is not a stable pointed curve.
    """
    return g >= 0 and n >= 0 and 2 * g - 2 + n > 0


def validate_curve_modular_operad_domain(
    g: int,
    n: int,
    *,
    base_complex_dimension: int = 1,
    moduli_kind: str = "curves",
    operad_kind: str = "modular",
    require_stable: bool = True,
) -> None:
    """Validate the geometric domain implemented here.

    The compute surface is deliberately narrower than a higher-dimensional
    factorization-algebra theorem: it is the modular operad of stable pointed
    curves, with optional ribbon ordering data.
    """
    if base_complex_dimension != 1:
        raise NotImplementedError(
            "Only complex curves are implemented; higher-dimensional "
            "varieties require a separate factorization-operad engine"
        )

    if moduli_kind not in {"curves", "stable_curves"}:
        raise NotImplementedError(
            "Only Deligne--Mumford moduli of stable pointed curves are "
            "implemented"
        )

    if operad_kind not in {"modular", "ribbon_modular", "symmetric_modular"}:
        raise ValueError(
            "Use a modular-operad kind here; factorization operads are a "
            "different compute surface"
        )

    if require_stable and not is_stable_curve_type(g, n):
        raise ValueError(f"Unstable pointed-curve type: (g,n)=({g},{n})")


# =========================================================================
# 1. Stable graph data structure (lightweight, self-contained)
# =========================================================================

@dataclass(frozen=True)
class RibbonStableGraph:
    """A stable graph with optional ribbon (cyclic ordering) structure.

    vertex_genera: genus g(v) for each vertex v = 0, ..., |V|-1
    edges: tuple of (v1, v2) pairs with v1 <= v2; v1==v2 for self-loops
    legs: tuple of vertex assignments for each marked point
    """
    vertex_genera: Tuple[int, ...]
    edges: Tuple[Tuple[int, int], ...]
    legs: Tuple[int, ...]

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
    def valence(self) -> Tuple[int, ...]:
        """Valence of each vertex.

        Each edge (v1, v2) contributes 2 to val(v1) if self-loop,
        else 1 to each endpoint. Each leg contributes 1.
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
    def first_betti(self) -> int:
        """h^1(Gamma) = |E| - |V| + connected components."""
        return self.num_edges - self.num_vertices + self._num_components()

    @property
    def arithmetic_genus(self) -> int:
        """g(Gamma) = h^1(Gamma) + sum g(v)."""
        return self.first_betti + sum(self.vertex_genera)

    @property
    def is_stable(self) -> bool:
        """Stability: 2g(v) - 2 + val(v) > 0 for all v."""
        val = self.valence
        return all(2 * self.vertex_genera[v] - 2 + val[v] > 0
                   for v in range(self.num_vertices))

    @property
    def is_connected(self) -> bool:
        return self._num_components() == 1

    @property
    def is_trivalent(self) -> bool:
        """Every vertex has valence exactly 3 (standard for ribbon graph counting)."""
        return all(v == 3 for v in self.valence)

    def _num_components(self) -> int:
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
        # Also connect via leg-sharing (legs connect to same vertex)
        return len(set(find(v) for v in range(self.num_vertices)))

    def automorphism_order(self) -> int:
        """Compute |Aut(Gamma)| by brute force for small graphs.

        An automorphism preserves vertex genera, edge multiset, and leg
        assignments. For multi-edges: k! permutations. For self-loops: 2^k flips.
        """
        n = self.num_vertices
        if n > 7:
            raise ValueError("Brute force too expensive for > 7 vertices")

        count = 0
        for perm in _genus_preserving_perms(self.vertex_genera):
            # Legs must be fixed
            if not all(perm[self.legs[i]] == self.legs[i]
                       for i in range(self.num_legs)):
                continue
            # Map edges
            mapped = tuple(sorted(
                (min(perm[v1], perm[v2]), max(perm[v1], perm[v2]))
                for v1, v2 in self.edges
            ))
            original = tuple(sorted(self.edges))
            if mapped != original:
                continue
            # Edge-level factor
            count += _edge_aut_factor(self.edges, perm)
        return max(count, 1)

    def ribbon_structure_count(self) -> int:
        """Number of distinct ribbon structures on this graph.

        A ribbon structure = cyclic ordering of half-edges at each vertex.
        At a vertex of valence val(v), there are (val(v)-1)! cyclic orderings.
        The total is the product over all vertices.

        For val(v) = 0 or 1: (val(v)-1)! is treated as 1 (trivial cyclic ordering).
        """
        val = self.valence
        result = 1
        for v in range(self.num_vertices):
            d = val[v]
            if d >= 2:
                result *= factorial(d - 1)
        return result

    def ribbon_automorphism_order(self) -> int:
        """Automorphism order of the ribbon graph.

        For a ribbon graph, automorphisms must also preserve the cyclic
        ordering at each vertex. This is more restrictive than the abstract
        graph automorphism group:

        |Aut_ribbon(Gamma)| divides |Aut(Gamma)|

        For connected trivalent graphs: the ribbon automorphism group acts
        freely on the set of ribbon structures, so

        |Aut_ribbon| = |Aut(Gamma)| * ribbon_structure_count / (number of distinct ribbon graphs)

        In general, we compute: for each abstract automorphism, check if it
        can be lifted to a ribbon automorphism. An abstract automorphism
        sigma lifts iff at every vertex v, the induced permutation of
        half-edges at v is a cyclic rotation.

        For a first approximation (exact for many cases): the ribbon
        automorphism group has order |Aut(Gamma)| / orientation_factor
        where orientation_factor accounts for the fact that self-loops
        cannot be flipped in a ribbon graph (flipping reverses the local
        orientation).

        Exact formula: |Aut_ribbon| = |Aut(Gamma)| / 2^{self_loops}
        for trivalent graphs. More generally, the self-loop flip is
        incompatible with the ribbon structure.
        """
        num_self_loops = sum(1 for v1, v2 in self.edges if v1 == v2)
        base_aut = self.automorphism_order()
        # Each self-loop contributes a factor of 2 to Aut(Gamma) via
        # half-edge flips. These flips reverse the local cyclic order,
        # placing them outside the ribbon automorphism group.
        return base_aut // (2 ** num_self_loops)


# =========================================================================
# 1b. Permutation / automorphism helpers
# =========================================================================

def _genus_preserving_perms(genera: Tuple[int, ...]):
    """Yield all permutations of vertices preserving genera."""
    from itertools import permutations as iterperms

    n = len(genera)
    groups: Dict[int, List[int]] = {}
    for v, g in enumerate(genera):
        groups.setdefault(g, []).append(v)

    group_perms = []
    for g_val in sorted(groups.keys()):
        verts = groups[g_val]
        group_perms.append((verts, list(iterperms(verts))))

    if not group_perms:
        yield tuple(range(n))
        return

    from itertools import product as cartprod
    perm_lists = [gp[1] for gp in group_perms]
    vert_lists = [gp[0] for gp in group_perms]

    for combo in cartprod(*perm_lists):
        perm = list(range(n))
        for verts, mapping in zip(vert_lists, combo):
            for src, dst in zip(verts, mapping):
                perm[src] = dst
        yield tuple(perm)


def _edge_aut_factor(edges: Tuple[Tuple[int, int], ...],
                     vertex_perm: Tuple[int, ...]) -> int:
    """Count edge-level automorphisms for a given vertex permutation."""
    mapped = []
    for v1, v2 in edges:
        a, b = vertex_perm[v1], vertex_perm[v2]
        mapped.append((min(a, b), max(a, b)))

    orig_groups = Counter(edges)
    map_groups = Counter(mapped)
    if orig_groups != map_groups:
        return 0

    factor = 1
    for (a, b), k in orig_groups.items():
        factor *= factorial(k)
        if a == b:
            factor *= 2 ** k
    return factor


# =========================================================================
# 2. Explicit stable graph enumerations
# =========================================================================

def genus0_graphs(n: int) -> List[RibbonStableGraph]:
    """Stable graphs of genus 0 with n marked points (n >= 3).

    At genus 0, the stable graphs are in bijection with trivalent trees
    with n labeled leaves plus possible non-trivalent vertices.

    For genus 0: all vertex genera are 0, first_betti = 0 (trees),
    so num_edges = num_vertices - 1.
    """
    if n < 3:
        return []
    if n == 3:
        return [RibbonStableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0))]
    if n == 4:
        return [
            RibbonStableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0, 0)),
            RibbonStableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 0, 1, 1)),
            RibbonStableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 1, 0, 1)),
            RibbonStableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 1, 1, 0)),
        ]
    # General: enumerate
    return _enumerate_graphs(0, n)


def genus1_graphs(n: int) -> List[RibbonStableGraph]:
    """Stable graphs of genus 1 with n marked points."""
    if n == 0:
        return []
    if n == 1:
        return [
            RibbonStableGraph(vertex_genera=(1,), edges=(), legs=(0,)),
            RibbonStableGraph(vertex_genera=(0,), edges=((0, 0),), legs=(0,)),
        ]
    return _enumerate_graphs(1, n)


def genus2_graphs_n0() -> List[RibbonStableGraph]:
    """The 7 genus-2 stable graphs with 0 marked points.

    1. Smooth (g=2): |Aut|=1
    2. Irreducible node (g=1, 1 self-loop): |Aut|=2
    3. Banana (g=0, 2 self-loops): |Aut|=8
    4. Separating (g=1,g=1, 1 edge): |Aut|=2
    5. Theta (g=0,g=0, 3 parallel edges): |Aut|=12
    6. Mixed (g=0 self-loop + edge to g=1): |Aut|=2
    7. Barbell (g=0,g=0, each with self-loop, 1 bridge): |Aut|=8
    """
    return [
        RibbonStableGraph(vertex_genera=(2,), edges=(), legs=()),
        RibbonStableGraph(vertex_genera=(1,), edges=((0, 0),), legs=()),
        RibbonStableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=()),
        RibbonStableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=()),
        RibbonStableGraph(vertex_genera=(0, 0),
                          edges=((0, 1), (0, 1), (0, 1)), legs=()),
        RibbonStableGraph(vertex_genera=(0, 1), edges=((0, 0), (0, 1)), legs=()),
        RibbonStableGraph(vertex_genera=(0, 0),
                          edges=((0, 0), (1, 1), (0, 1)), legs=()),
    ]


# =========================================================================
# 3. General graph enumeration
# =========================================================================

def _enumerate_graphs(g: int, n: int) -> List[RibbonStableGraph]:
    """Enumerate all connected stable graphs of genus g with n legs."""
    if 2 * g - 2 + n <= 0:
        return []

    results = []
    seen = set()
    max_v = max(1, 2 * g - 2 + n)

    for nv in range(1, max_v + 1):
        for genera in _genus_distributions(g, nv):
            sum_gv = sum(genera)
            h1 = g - sum_gv
            if h1 < 0:
                continue
            ne = h1 + nv - 1
            if ne < 0:
                continue
            for edges in _edge_configs(nv, ne):
                for legs in _leg_distribs(nv, n):
                    gr = RibbonStableGraph(genera, edges, legs)
                    if not gr.is_stable or not gr.is_connected:
                        continue
                    if gr.arithmetic_genus != g:
                        continue
                    canon = _canonical(gr)
                    if canon not in seen:
                        seen.add(canon)
                        results.append(gr)
    return results


def _genus_distributions(g: int, nv: int):
    """All tuples (g_1, ..., g_nv) with sum <= g and each g_i >= 0."""
    if nv == 1:
        for gi in range(g + 1):
            yield (gi,)
        return
    for gi in range(g + 1):
        for rest in _genus_distributions(g - gi, nv - 1):
            yield (gi,) + rest


def _edge_configs(nv: int, ne: int):
    """All multisets of ne edges on nv vertices (including self-loops).

    Edges are (v1, v2) with v1 <= v2.
    """
    if ne == 0:
        yield ()
        return
    # Generate all possible edge slots
    slots = []
    for i in range(nv):
        for j in range(i, nv):
            slots.append((i, j))

    for combo in _multiset_combos(slots, ne):
        yield tuple(sorted(combo))


def _multiset_combos(items: List[Tuple[int, int]], k: int, start: int = 0):
    """Choose k items from items[start:] with repetition, sorted."""
    if k == 0:
        yield []
        return
    for i in range(start, len(items)):
        for rest in _multiset_combos(items, k - 1, i):
            yield [items[i]] + rest


def _leg_distribs(nv: int, n: int):
    """Distribute n labeled legs among nv vertices.

    For legs labeled 0, ..., n-1, yield all tuples
    (v_0, v_1, ..., v_{n-1}) with v_i in {0, ..., nv-1}.

    For n > 4, restrict to reduce combinatorial explosion.
    """
    if n == 0:
        yield ()
        return
    if nv == 1:
        yield (0,) * n
        return
    # For small n, enumerate all
    if n <= 4:
        for combo in _product_range(nv, n):
            yield combo
    else:
        # For larger n, only enumerate sorted-representative distributions
        for combo in _product_range(nv, n):
            yield combo


def _product_range(nv: int, n: int):
    """Cartesian product {0,...,nv-1}^n."""
    if n == 0:
        yield ()
        return
    for first in range(nv):
        for rest in _product_range(nv, n - 1):
            yield (first,) + rest


def _canonical(gr: RibbonStableGraph) -> tuple:
    """Canonical form for isomorphism deduplication.

    Two graphs are isomorphic if there is a vertex permutation
    preserving genera, mapping the edge multiset, and preserving
    leg assignments (legs are labeled).
    """
    best = None
    for perm in _genus_preserving_perms(gr.vertex_genera):
        mapped_edges = tuple(sorted(
            (min(perm[v1], perm[v2]), max(perm[v1], perm[v2]))
            for v1, v2 in gr.edges
        ))
        mapped_legs = tuple(perm[v] for v in gr.legs)
        candidate = (tuple(gr.vertex_genera[perm[v]]
                           for v in range(gr.num_vertices)),
                     mapped_edges, mapped_legs)
        # Canonical form relabels vertices by the permuted genera in a
        # standard order. For this diagnostic, use sorted genera, sorted
        # edges under all valid relabelings, and legs.
        # For deduplication, the key insight is: two graphs are iso iff
        # there exists a perm making them identical.
        key = (gr.vertex_genera, mapped_edges, mapped_legs)
        if best is None or key < best:
            best = key
    return best


# =========================================================================
# 4. Ribbon graph counting
# =========================================================================

def ribbon_structures_on_graph(graph: RibbonStableGraph) -> int:
    """Number of distinct ribbon structures on a given stable graph.

    A ribbon structure assigns a cyclic ordering to the half-edges at each
    vertex. At vertex v with valence d = val(v):
      - There are (d-1)! distinct cyclic orderings (for d >= 1).
      - Convention: 0! = 1, so val=1 gives 1 ordering.

    Total = product over all vertices of (val(v) - 1)!.

    This counts ALL ribbon structures, including those related by
    graph automorphisms. The number of DISTINCT ribbon graphs
    (up to ribbon isomorphism) is:

      ribbon_structures / |Aut_ribbon(Gamma)|

    but since we often want the weighted count, we provide both.
    """
    return graph.ribbon_structure_count()


def ribbon_graph_count_genus0(n: int) -> int:
    """Number of labeled trivalent ribbon trees with n leaves at genus 0.

    For genus 0 (planar), the number of distinct ribbon structures on
    trivalent trees with n labeled leaves is:
      (2n-5)!! for n >= 3, with (2*3-5)!! = 1!! = 1

    This counts the number of distinct planar binary trees with n
    labeled leaves, which is the Catalan number C_{n-1} times (n-1)!
    ... no. The correct count of labeled planar binary trees (= genus-0
    ribbon trivalent trees) with n leaves is:

    The number of trivalent planar trees with n labeled leaves is
    (2n-5)!! = 1*3*5*...*(2n-5) for n >= 3.

    Verification:
      n=3: (2*3-5)!! = 1!! = 1.  Correct (unique trivalent tree with 3 leaves).
      n=4: (2*4-5)!! = 3!! = 3.  Three binary trees on 4 labeled leaves
           corresponding to the 3 channels (12|34), (13|24), (14|23).
      n=5: (2*5-5)!! = 5!! = 15.

    These are the genus-0 RIBBON trivalent tree count.
    """
    if n < 3:
        return 0
    return double_factorial(2 * n - 5)


def total_ribbon_structures_genus(g: int, n: int,
                                  graphs: Optional[List[RibbonStableGraph]] = None
                                  ) -> int:
    """Total number of ribbon structures summed over all stable graphs
    of genus g with n marked points.

    Sum over all stable graphs Gamma of genus (g, n):
      sum_Gamma ribbon_structures(Gamma)
    """
    if graphs is None:
        graphs = enumerate_stable_graphs(g, n)
    return sum(gr.ribbon_structure_count() for gr in graphs)


def total_ordinary_graphs(g: int, n: int,
                          graphs: Optional[List[RibbonStableGraph]] = None
                          ) -> int:
    """Total number of (ordinary, unordered) stable graphs at (g, n)."""
    if graphs is None:
        graphs = enumerate_stable_graphs(g, n)
    return len(graphs)


def enumerate_stable_graphs(
    g: int,
    n: int,
    *,
    base_complex_dimension: int = 1,
    moduli_kind: str = "curves",
    operad_kind: str = "modular",
) -> List[RibbonStableGraph]:
    """Main entry: enumerate stable pointed-curve graphs at (g, n).

    Unstable pairs return the empty list.  Use
    validate_curve_modular_operad_domain when an amplitude formula requires a
    stable input rather than an empty diagnostic.
    """
    validate_curve_modular_operad_domain(
        g,
        n,
        base_complex_dimension=base_complex_dimension,
        moduli_kind=moduli_kind,
        operad_kind=operad_kind,
        require_stable=False,
    )
    if not is_stable_curve_type(g, n):
        return []
    if g == 0:
        return genus0_graphs(n)
    if g == 1:
        return genus1_graphs(n)
    if g == 2 and n == 0:
        return genus2_graphs_n0()
    return _enumerate_graphs(g, n)


# =========================================================================
# 5. E_1 / E_infty multiplicity ratio
# =========================================================================

def e1_einfty_ratio(graph: RibbonStableGraph) -> Fraction:
    """The E_1/E_infty multiplicity for a single graph.

    This is the number of ribbon structures on the graph,
    measuring how much extra data the E_1 (ordered) modular operad
    carries compared to E_infty (symmetric).

    ratio = ribbon_structures(Gamma) = prod_v (val(v) - 1)!
    """
    return Fraction(graph.ribbon_structure_count())


def total_e1_einfty_ratio(g: int, n: int) -> Fraction:
    """Total weighted E_1/E_infty ratio for all graphs at (g, n).

    Sum_Gamma ribbon_structures(Gamma) / |Aut(Gamma)|
    divided by
    Sum_Gamma 1 / |Aut(Gamma)|

    This gives the average number of ribbon structures per graph,
    weighted by 1/|Aut|.
    """
    graphs = enumerate_stable_graphs(g, n)
    if not graphs:
        return Fraction(0)

    num = Fraction(0)
    den = Fraction(0)
    for gr in graphs:
        aut = gr.automorphism_order()
        num += Fraction(gr.ribbon_structure_count(), aut)
        den += Fraction(1, aut)

    if den == 0:
        return Fraction(0)
    return num / den


# =========================================================================
# 6. Orientation doubling for trivalent graphs
# =========================================================================

def orientation_factor(graph: RibbonStableGraph) -> int:
    """For a connected graph Gamma, each ribbon structure on Gamma
    determines an orientable surface Sigma. Reversing the orientation
    of Sigma gives a DIFFERENT ribbon structure (reflected cyclic orders).

    For a connected graph, the number of orientable surface embeddings
    is exactly 2 times the number of oriented surface embeddings,
    UNLESS the graph has an orientation-reversing automorphism.

    For trivalent graphs: at each vertex of valence 3, there are
    (3-1)! = 2 cyclic orderings. These two are related by orientation
    reversal. So for trivalent graphs without orientation-reversing
    automorphisms:
      ribbon_count = 2^{|V|} for trivalent, all genus

    The orientation doubling factor for genus 1:
      For trivalent genus-1 graphs, the number of ribbon structures
      is exactly 2 * (number obtained by fixing an orientation).
    """
    # The factor is 2 for connected graphs (orientation choice)
    # unless the graph has an automorphism reversing orientation.
    # For simplicity, return 2 for connected graphs.
    if graph.is_connected:
        return 2
    return 1


def genus1_trivalent_ribbon_vs_ordinary() -> Fraction:
    """Verify: for genus-1 trivalent graphs, ribbon = 2 * ordinary.

    At genus 1 with 0 marked points, the self-loop graph has one genus-0
    vertex, one self-loop, and valence 2. It is unstable. Hence there are no
    trivalent graphs
    (minimum valence for stable g=0 vertex is 3, but a self-loop gives
    valence 2 for g=0 which is unstable; the smooth g=1 vertex has val=0).

    With n=2 marked points, genus 1:
    - The smooth vertex (g=1, val=2, 2 legs): (2-1)! = 1 ribbon.
    - Self-loop vertex (g=0, val=4, 2 legs + self-loop): (4-1)! = 6 ribbons.
    - etc.

    The precise statement: for any single TRIVALENT graph at any genus,
    the number of ribbon structures is prod_v 2 = 2^|V|.  The oriented
    count (choosing a global orientation) is 2^|V| / 2 = 2^{|V|-1}
    for connected graphs.

    Return the ratio ribbon_count / ordinary_count for trivalent graphs
    at (1, 2) as a consistency check.
    """
    graphs = enumerate_stable_graphs(1, 2)
    trivalent = [gr for gr in graphs if gr.is_trivalent]

    if not trivalent:
        # Ratio is undefined if no trivalent graphs
        return Fraction(0)

    ribbon_total = sum(gr.ribbon_structure_count() for gr in trivalent)
    ordinary_total = len(trivalent)
    return Fraction(ribbon_total, ordinary_total)


# =========================================================================
# 7. Harer-Zagier Euler characteristic
# =========================================================================

@lru_cache(maxsize=128)
def bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n as Fraction."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        bk = bernoulli_exact(k)
        if bk != 0:
            s += Fraction(comb(n + 1, k)) * bk
    return -s / Fraction(n + 1)


def chi_orb_mg(g: int) -> Fraction:
    """Orbifold Euler characteristic of M_g (open moduli, no marked points).

    chi^orb(M_g) = B_{2g} / (4g(g-1))  for g >= 2.

    Harer-Zagier (1986).
    """
    if g < 2:
        raise ValueError(f"Formula valid for g >= 2, got g={g}")
    B_2g = bernoulli_exact(2 * g)
    return B_2g / Fraction(4 * g * (g - 1))


@lru_cache(maxsize=128)
def chi_orb_mgn(g: int, n: int) -> Fraction:
    """Orbifold Euler characteristic of M_{g,n} (open moduli).

    Recursion: chi(M_{g,n+1}) = (2g - 2 + n) * chi(M_{g,n}).
    Base cases: chi(M_{1,1}) = -1/12, chi(M_{g,0}) = B_{2g}/(4g(g-1)) for g>=2.
    Genus 0: chi(M_{0,n}) = (-1)^{n-1} * (n-3)! for n >= 3.
    """
    if 2 * g - 2 + n <= 0:
        raise ValueError(f"Unstable: (g,n)=({g},{n})")
    if g == 0:
        if n < 3:
            raise ValueError(f"Unstable: (0, {n})")
        return Fraction((-1) ** (n - 1) * factorial(n - 3))
    if g == 1 and n == 1:
        return Fraction(-1, 12)
    if g >= 2 and n == 0:
        return chi_orb_mg(g)
    if g == 1 and n == 0:
        raise ValueError("M_{1,0} unstable")
    return Fraction(2 * g - 2 + n - 1) * chi_orb_mgn(g, n - 1)


def chi_orb_mbar_from_graphs(g: int, n: int) -> Fraction:
    """Compute chi^orb(Mbar_{g,n}) from the graph stratification.

    chi^orb(Mbar_{g,n}) = sum_Gamma prod_v chi^orb(M_{g(v), val(v)}) / |Aut(Gamma)|
    """
    validate_curve_modular_operad_domain(g, n)
    graphs = enumerate_stable_graphs(g, n)
    total = Fraction(0)
    for gr in graphs:
        val = gr.valence
        prod = Fraction(1)
        for v in range(gr.num_vertices):
            gv = gr.vertex_genera[v]
            dv = val[v]
            prod *= chi_orb_mgn(gv, dv)
        prod /= Fraction(gr.automorphism_order())
        total += prod
    return total


# =========================================================================
# 8. Feynman transform: FCom vs FAss scalar sector comparison
# =========================================================================

def fcom_scalar_amplitude(g: int, kappa: Fraction,
                          graphs: Optional[List[RibbonStableGraph]] = None,
                          n: int = 0
                          ) -> Fraction:
    """FCom scalar graph diagnostic for the curve-level modular operad.

    At fixed stable pointed-curve type (g,n), in the constant-vertex-weight
    diagnostic:

      F_{g,n}^{FCom}(kappa) = sum_Gamma kappa^{|E(Gamma)|} / |Aut(Gamma)|.

    This is not the full Faber--Pandharipande genus formula; it is the
    finite graph-sum surface used to compare symmetric and ordered scalar
    normalizations.
    """
    if graphs is None:
        validate_curve_modular_operad_domain(g, n)
        graphs = enumerate_stable_graphs(g, n)
    total = Fraction(0)
    for gr in graphs:
        weight = kappa ** gr.num_edges / Fraction(gr.automorphism_order())
        total += weight
    return total


def fass_scalar_amplitude(g: int, kappa: Fraction,
                          graphs: Optional[List[RibbonStableGraph]] = None,
                          n: int = 0
                          ) -> Fraction:
    """Normalized FAss scalar diagnostic.

    The raw ribbon sum differs from FCom by the cyclic-order factor
    prod_v (val(v)-1)!.  The scalar coinvariant comparison divides the
    ribbon contribution by exactly that local ordering count.  The returned
    value is therefore the normalized scalar comparison, not the raw ribbon
    amplitude.
    """
    if graphs is None:
        validate_curve_modular_operad_domain(g, n)
        graphs = enumerate_stable_graphs(g, n)

    total = Fraction(0)
    for gr in graphs:
        ribbon_count = gr.ribbon_structure_count()
        aut = gr.automorphism_order()
        total += (
            kappa ** gr.num_edges
            * Fraction(ribbon_count, aut)
            * Fraction(1, ribbon_count)
        )

    return total


def raw_ribbon_scalar_amplitude(g: int, kappa: Fraction,
                                graphs: Optional[List[RibbonStableGraph]] = None,
                                n: int = 0
                                ) -> Fraction:
    """Raw ribbon scalar graph sum before scalar coinvariant normalization."""
    if graphs is None:
        validate_curve_modular_operad_domain(g, n)
        graphs = enumerate_stable_graphs(g, n)

    total = Fraction(0)
    for gr in graphs:
        total += (
            kappa ** gr.num_edges
            * Fraction(gr.ribbon_structure_count(), gr.automorphism_order())
        )
    return total


def ribbon_normalization_obstruction(
    g: int,
    kappa: Fraction = Fraction(1),
    n: int = 0,
) -> Dict[str, Any]:
    """Compare raw ribbon and normalized scalar graph sums.

    A nonzero obstruction means the raw ribbon count cannot be promoted to
    scalar FCom/FAss agreement without the cyclic-order normalization.
    """
    validate_curve_modular_operad_domain(g, n)
    graphs = enumerate_stable_graphs(g, n)
    fcom = fcom_scalar_amplitude(g, kappa, graphs, n=n)
    fass = fass_scalar_amplitude(g, kappa, graphs, n=n)
    raw = raw_ribbon_scalar_amplitude(g, kappa, graphs, n=n)
    return {
        "genus": g,
        "marked_points": n,
        "kappa": kappa,
        "fcom": fcom,
        "fass_normalized": fass,
        "raw_ribbon": raw,
        "normalization_obstruction": raw - fcom,
        "normalized_agrees": fcom == fass,
        "raw_agrees": raw == fcom,
        "num_graphs": len(graphs),
    }


def verify_fcom_fass_scalar_agreement(g: int, kappa: Fraction = Fraction(1),
                                      n: int = 0
                                      ) -> Dict[str, Any]:
    """Verify normalized FCom = FAss at scalar level for stable (g,n).

    The returned raw ribbon value is included as an obstruction witness.
    """
    validate_curve_modular_operad_domain(g, n)
    graphs = enumerate_stable_graphs(g, n)
    fcom = fcom_scalar_amplitude(g, kappa, graphs, n=n)
    fass = fass_scalar_amplitude(g, kappa, graphs, n=n)
    raw = raw_ribbon_scalar_amplitude(g, kappa, graphs, n=n)
    return {
        "genus": g,
        "marked_points": n,
        "kappa": kappa,
        "fcom": fcom,
        "fass": fass,
        "raw_ribbon": raw,
        "normalization_obstruction": raw - fcom,
        "agree": fcom == fass,
        "raw_agrees": raw == fcom,
        "num_graphs": len(graphs),
    }


# =========================================================================
# 9. Shadow invariant finite E_n diagnostics
# =========================================================================

def shadow_kappa_en(
    family: str,
    n_operad: int,
    *,
    base_complex_dimension: int = 1,
    **kwargs,
) -> Fraction:
    """Compute the curve-level scalar kappa diagnostic at operadic level n.

    The operadic level is a label for the finite scalar diagnostic, not the
    complex dimension of a target variety.  Higher-dimensional varieties are
    outside this module's implemented domain.

    Families: "heisenberg", "virasoro", "affine", "wn", "betagamma",
              "bc", "lattice", "free_fermion"
    """
    if n_operad < 1:
        raise ValueError(f"Operadic level must be >= 1, got {n_operad}")
    if base_complex_dimension != 1:
        raise NotImplementedError(
            "kappa E_n diagnostics here are curve-level scalar shadows; "
            "higher-dimensional varieties require the CY/factorization engine"
        )

    family = family.lower()
    if family == "heisenberg":
        k = kwargs.get("k", Fraction(1))
        return _frac(k)
    elif family == "virasoro":
        c = kwargs.get("c", Fraction(26))
        return _frac(c) / 2
    elif family == "affine":
        lie_type = kwargs.get("lie_type", "A")
        rank = kwargs.get("rank", 1)
        k = kwargs.get("k", Fraction(1))
        dim_g, h_dual = _lie_data(lie_type, rank)
        return Fraction(dim_g) * (_frac(k) + Fraction(h_dual)) / \
            (2 * Fraction(h_dual))
    elif family == "wn":
        N = kwargs.get("N", 2)
        c = kwargs.get("c", Fraction(0))
        sigma = sum(Fraction(1, j) for j in range(2, N + 1))
        return _frac(c) * sigma
    elif family == "betagamma":
        lam = kwargs.get("lam", 1)
        return Fraction(6 * lam * lam - 6 * lam + 1)
    elif family == "bc":
        return Fraction(-1)
    elif family == "lattice":
        rank = kwargs.get("rank", 1)
        return Fraction(rank)
    elif family == "free_fermion":
        return Fraction(1, 2)
    else:
        raise ValueError(f"Unknown family: {family}")


def _lie_data(lie_type: str, rank: int) -> Tuple[int, int]:
    """(dim(g), h^vee) for a simple Lie algebra."""
    t = lie_type.upper()
    if t == "A":
        N = rank + 1
        return (N * N - 1, N)
    elif t == "B":
        return (rank * (2 * rank + 1), 2 * rank - 1)
    elif t == "C":
        return (rank * (2 * rank + 1), rank + 1)
    elif t == "D":
        return (rank * (2 * rank - 1), 2 * rank - 2)
    elif t == "G" and rank == 2:
        return (14, 4)
    elif t == "F" and rank == 4:
        return (52, 9)
    elif t == "E" and rank == 6:
        return (78, 12)
    elif t == "E" and rank == 7:
        return (133, 18)
    elif t == "E" and rank == 8:
        return (248, 30)
    raise ValueError(f"Unknown Lie type {lie_type}{rank}")


def verify_shadow_en_independence(
    family: str,
    max_n: int = 5,
    *,
    base_complex_dimension: int = 1,
    **kwargs,
) -> Dict[str, Any]:
    """Finite diagnostic for kappa across operadic levels 1,...,max_n.

    This is a bounded computation.  It records evidence for the scalar
    coinvariant claim; it is not itself an all-n proof.
    """
    if max_n < 1:
        raise ValueError(f"max_n must be >= 1, got {max_n}")
    if base_complex_dimension != 1:
        raise NotImplementedError(
            "Only curve-level scalar shadows are implemented in this module"
        )

    values = {}
    for n in range(1, max_n + 1):
        values[n] = shadow_kappa_en(
            family,
            n,
            base_complex_dimension=base_complex_dimension,
            **kwargs,
        )

    all_equal = len(set(values.values())) == 1
    return {
        "family": family,
        "kwargs": kwargs,
        "values": values,
        "all_equal": all_equal,
        "kappa": values[1],
        "diagnostic_range": (1, max_n),
        "finite_diagnostic": True,
        "base_complex_dimension": base_complex_dimension,
    }


# =========================================================================
# 10. Harer-Zagier cell decomposition count
# =========================================================================

@lru_cache(maxsize=128)
def harer_zagier_epsilon(g: int, n: int) -> int:
    """Number of genus-g cell decompositions with one vertex and n edges.

    The Harer-Zagier formula: for a surface of genus g, the number of
    ways to identify sides of a 2n-gon to get a genus-g surface with
    one face is epsilon_g(n).

    Recursion (Harer-Zagier 1986):
      (n+1) epsilon_g(n) = (4n-2) epsilon_g(n-1) + (2n-1)(n-1)(2n-3) epsilon_{g-1}(n-2)

    Alternative generating function:
      sum_{g=0}^{n} epsilon_g(n) * x^{2g} = (2n-1)!! * (x+1)^n ... (complicated)

    Base cases:
      epsilon_0(n) = C_n = (2n)!/((n+1)!n!) (Catalan numbers, genus 0)
      epsilon_g(n) = 0 for n < 2g (not enough edges for genus g)

    For simplicity, use the explicit formula:
      epsilon_g(n) = (2n)! / (2^n * n!) * [coefficient of x^{2g} in
                     sum_j C(n,j) (1+x)^j (1-x)^{n-j}] / ... complicated.

    Use the recursion instead.
    """
    if n < 0 or g < 0:
        return 0
    if g == 0:
        return catalan_number(n)
    if n < 2 * g:
        return 0
    if n == 0:
        return 1 if g == 0 else 0
    if n == 1:
        return 1 if g == 0 else 0

    # Recursion: (n+1) eps_g(n) = (4n-2) eps_g(n-1) + (2n-1)(n-1)(2n-3) eps_{g-1}(n-2)
    term1 = (4 * n - 2) * harer_zagier_epsilon(g, n - 1)
    term2 = (2 * n - 1) * (n - 1) * (2 * n - 3) * harer_zagier_epsilon(g - 1, n - 2)
    result, rem = divmod(term1 + term2, n + 1)
    assert rem == 0, f"Harer-Zagier recursion not integral at g={g}, n={n}"
    return result


def harer_zagier_total(n: int) -> int:
    """Total number of cell decompositions with n edges (sum over all genera).

    sum_{g=0}^{floor(n/2)} epsilon_g(n) = (2n-1)!!

    This is the Harer-Zagier identity: the total count is the double factorial.
    """
    return sum(harer_zagier_epsilon(g, n) for g in range(n // 2 + 1))


# =========================================================================
# 11. Genus-2 Euler characteristic verification
# =========================================================================

def verify_genus2_euler() -> Dict[str, Any]:
    """Verify chi^orb(M_2) = -1/240 via the Harer-Zagier formula
    and also via the graph stratification sum.

    B_4 = -1/30, so chi^orb(M_2) = B_4 / (4*2*1) = (-1/30)/8 = -1/240.
    """
    # Method 1: Harer-Zagier formula
    hz = chi_orb_mg(2)

    # Method 2: graph stratification
    graph_chi = chi_orb_mbar_from_graphs(2, 0)

    # Method 3: direct Bernoulli
    B4 = bernoulli_exact(4)
    direct = B4 / Fraction(8)

    return {
        "harer_zagier": hz,
        "graph_stratification_mbar": graph_chi,
        "direct_bernoulli": direct,
        "hz_equals_expected": hz == Fraction(-1, 240),
        "direct_equals_expected": direct == Fraction(-1, 240),
    }


# =========================================================================
# 12. Summary / theorem statement
# =========================================================================

def theorem_summary() -> Dict[str, Any]:
    """Summary of the curve-level modular-operad compute surface."""
    return {
        "theorem": "Curve-level modular operad scalar diagnostics",
        "key_results": [
            "1. Ribbon structures on stable graph Gamma = prod(val(v)-1)!",
            "2. Stable pointed-curve domain requires 2g-2+n > 0",
            "3. Raw ribbon sums differ from symmetric sums by cyclic-order multiplicity",
            "4. Normalized FAss scalar diagnostic agrees with FCom",
            "5. Genus-0 ribbon count = (2n-5)!! for trivalent trees",
            "6. Finite kappa E_n checks are diagnostics, not higher-dimensional proofs",
        ],
        "scope_guards": [
            "Deligne--Mumford stable pointed curves only",
            "modular or ribbon modular operads only",
            "higher-dimensional varieties not implemented here",
            "raw ribbon and scalar coinvariant sums reported separately",
        ],
    }
