r"""
genus1_graph_weight_engine.py — Stable graph enumeration and weight bounds
at genus 1 for the shadow-level multiplicativity theorem.

KEY THEOREM (thm:shadow-multiplicativity-low-arity):
  At genus 1 and arity r <= 5, the genus-1 shadow projection
  Sh_r^{(1)}(Theta_A; tau) has modular weight <= 2r <= 10 < 12.
  Since dim S_k(SL(2,Z)) = 0 for k < 12 (no cusp forms), each
  graph amplitude is a polynomial in the Hecke eigenforms E_4, E_6.
  The moment L-function M_r(s) is therefore a polynomial in
  zeta(s) and its shifts, hence has an Euler product.
  Shadow-level multiplicativity holds automatically at arities 2-5.

The weight bound follows from:
  - Each edge of a stable graph on (1, r) contributes weight 2
    (from the genus-1 propagator P(tau) of modular weight 2)
  - For a stable graph Gamma at (1, r) with all vertices at genus 0:
    |E(Gamma)| = |V(Gamma)| (since h^1 = 1)
  - Stability (n_v >= 3) implies |V| <= r
  - Hence weight = 2|E| = 2|V| <= 2r

For r = 6: weight can reach 12, and the Ramanujan cusp form Delta
first appears. The MC recursion constraint at this arity determines
the Delta coefficient.

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial, gcd
from typing import Any, Dict, List, Optional, Set, Tuple


# ===========================================================================
# Stable graph data structure
# ===========================================================================

@dataclass(frozen=True)
class StableGraph:
    """A stable graph at (g, n).

    Vertices are labeled by (genus, valence) pairs.
    Edges connect pairs of half-edges.
    Legs are external half-edges.

    Stability: 2g_v - 2 + n_v > 0 for each vertex v.
    Genus formula: h^1(Gamma) + sum g_v = g.
    """
    genus: int                          # total genus g
    num_legs: int                       # number of external legs = n
    vertex_genera: Tuple[int, ...]      # genus of each vertex
    vertex_valences: Tuple[int, ...]    # total half-edges at each vertex
    num_edges: int                      # number of internal edges
    num_vertices: int                   # |V|
    loop_number: int                    # h^1 = |E| - |V| + connected components
    description: str = ""

    @property
    def modular_weight(self) -> int:
        """Modular weight = 2 * num_edges (each edge contributes weight 2)."""
        return 2 * self.num_edges

    @property
    def is_stable(self) -> bool:
        """Check stability: 2g_v - 2 + n_v > 0 for each vertex."""
        for gv, nv in zip(self.vertex_genera, self.vertex_valences):
            if 2 * gv - 2 + nv <= 0:
                return False
        return True

    @property
    def genus_check(self) -> bool:
        """Verify genus formula: h^1 + sum g_v = g."""
        return self.loop_number + sum(self.vertex_genera) == self.genus

    def vertex_factor_indices(self) -> List[int]:
        """Shadow coefficient indices S_{n_v} for each vertex.

        For a vertex at genus 0 with total valence n_v (including edges
        and legs), the vertex factor is S_{n_v} if all half-edges are
        "shadow-type". For genus-1 vertices, the factor involves
        intersection numbers on M-bar_{1, n_v}.
        """
        return list(self.vertex_valences)


# ===========================================================================
# Stable graph enumeration at genus 1
# ===========================================================================

def enumerate_genus1_graphs(n_legs: int) -> List[StableGraph]:
    """Enumerate all stable graph topologies at (g=1, n=n_legs).

    Strategy: partition genus 1 between loop number h^1 and vertex genera.
    For each (h^1, {g_v}): enumerate vertex valences consistent with
    stability and the handshake lemma.

    Returns: list of StableGraph objects (not canonicalized by automorphism).
    """
    graphs = []

    # Case 1: h^1 = 1, all vertices at genus 0
    # |E| = |V|, sum n_v = 2|E| + n_legs = 2|V| + n_legs
    # Stability: n_v >= 3 for each genus-0 vertex
    _enumerate_h1_1(n_legs, graphs)

    # Case 2: h^1 = 0, exactly one vertex at genus 1, rest at genus 0
    # Tree graph: |E| = |V| - 1
    # The genus-1 vertex needs n_v >= 1 (stability: 2*1-2+n_v > 0 => n_v >= 1)
    # Genus-0 vertices need n_v >= 3
    _enumerate_h1_0(n_legs, graphs)

    return graphs


def _enumerate_h1_1(n_legs: int, graphs: List[StableGraph]):
    """Enumerate graphs with h^1 = 1 (one loop), all vertices at genus 0.

    For |V| vertices: |E| = |V|, valence sum = 2|V| + n_legs.
    Each vertex has valence >= 3 (genus-0 stability).
    """
    # Maximum vertices: each has valence >= 3, so 3|V| <= 2|V| + n_legs => |V| <= n_legs
    # Minimum vertices: 1 (self-loop vertex, valence = 2 + n_legs, need >= 3 => n_legs >= 1)
    # For n_legs = 0: need valence >= 3, but self-loop gives valence 2. Not stable!
    # So minimum vertices depends on n_legs.

    max_v = max(n_legs, 1)  # at most n_legs vertices

    for nv in range(1, max_v + 1):
        # Number of edges = nv (for h^1 = 1)
        ne = nv
        # Total half-edges = 2*ne + n_legs = 2*nv + n_legs
        total_halfedges = 2 * nv + n_legs
        # Need to partition total_halfedges among nv vertices, each >= 3
        _enumerate_valence_partitions(
            n_vertices=nv,
            total_valence=total_halfedges,
            min_valence=3,
            genus=1,
            n_legs=n_legs,
            vertex_genera=tuple([0] * nv),
            num_edges=ne,
            loop_number=1,
            graphs=graphs,
            desc_prefix=f"h1=1,V={nv},E={ne}"
        )


def _enumerate_h1_0(n_legs: int, graphs: List[StableGraph]):
    """Enumerate graphs with h^1 = 0 (tree), one genus-1 vertex.

    Tree: |E| = |V| - 1.
    One vertex at genus 1 (valence >= 1), rest at genus 0 (valence >= 3).
    """
    # Single genus-1 vertex, no edges, no genus-0 vertices
    if n_legs >= 1:  # stability: 2*1-2+n_legs > 0 => n_legs >= 1
        graphs.append(StableGraph(
            genus=1, num_legs=n_legs,
            vertex_genera=(1,),
            vertex_valences=(n_legs,),
            num_edges=0, num_vertices=1, loop_number=0,
            description=f"h1=0,V=1,E=0,g1_vertex"
        ))

    # One genus-1 vertex + genus-0 vertices connected by a tree
    for nv in range(2, n_legs + 2):  # total vertices
        ne = nv - 1  # tree
        total_halfedges = 2 * ne + n_legs

        # Distribute valences: genus-1 vertex gets >= 1, genus-0 get >= 3
        # Try all positions for the genus-1 vertex
        for g1_pos in range(nv):
            min_valences = [3] * nv
            min_valences[g1_pos] = 1  # genus-1 vertex

            genera = [0] * nv
            genera[g1_pos] = 1

            _enumerate_valence_partitions(
                n_vertices=nv,
                total_valence=total_halfedges,
                min_valence=None,  # handled by min_valences
                genus=1,
                n_legs=n_legs,
                vertex_genera=tuple(genera),
                num_edges=ne,
                loop_number=0,
                graphs=graphs,
                desc_prefix=f"h1=0,V={nv},E={ne},g1@{g1_pos}",
                min_valences=min_valences,
            )


def _enumerate_valence_partitions(
    n_vertices: int,
    total_valence: int,
    min_valence: Optional[int],
    genus: int,
    n_legs: int,
    vertex_genera: Tuple[int, ...],
    num_edges: int,
    loop_number: int,
    graphs: List[StableGraph],
    desc_prefix: str,
    min_valences: Optional[List[int]] = None,
):
    """Enumerate ordered partitions of total_valence into n_vertices parts.

    Each part >= min_valence (or per-vertex minimum from min_valences).
    We enumerate SORTED partitions to avoid overcounting symmetric cases.
    """
    if min_valences is None:
        min_valences = [min_valence] * n_vertices

    partitions = _partitions(total_valence, n_vertices, min_valences)

    for p in partitions:
        valences = tuple(p)
        g = StableGraph(
            genus=genus,
            num_legs=n_legs,
            vertex_genera=vertex_genera,
            vertex_valences=valences,
            num_edges=num_edges,
            num_vertices=n_vertices,
            loop_number=loop_number,
            description=f"{desc_prefix},val={valences}",
        )
        if g.is_stable and g.genus_check:
            graphs.append(g)


def _partitions(
    total: int,
    num_parts: int,
    min_vals: List[int],
) -> List[List[int]]:
    """Generate all ordered partitions of total into num_parts parts.

    Part i >= min_vals[i]. Uses recursive generation.
    Returns sorted partitions to reduce overcounting.
    """
    if num_parts == 0:
        return [[]] if total == 0 else []

    if num_parts == 1:
        if total >= min_vals[0]:
            return [[total]]
        return []

    result = []
    for v in range(min_vals[0], total - sum(min_vals[1:]) + 1):
        for rest in _partitions(total - v, num_parts - 1, min_vals[1:]):
            result.append([v] + rest)

    return result


# ===========================================================================
# Weight bound analysis
# ===========================================================================

def weight_bound_analysis(max_legs: int = 7) -> Dict[int, Dict[str, Any]]:
    """Analyze modular weight bounds for genus-1 graphs at each arity.

    Returns {n_legs: {max_weight, min_weight, num_graphs, graphs, ...}}
    """
    results = {}

    for n in range(0, max_legs + 1):
        graphs = enumerate_genus1_graphs(n)
        if not graphs:
            results[n] = {
                'num_graphs': 0,
                'max_weight': 0,
                'min_weight': 0,
                'weights': [],
                'weight_bound_2r': True,
                'below_cusp_threshold': True,
            }
            continue

        weights = [g.modular_weight for g in graphs]
        max_w = max(weights)
        min_w = min(weights)

        results[n] = {
            'num_graphs': len(graphs),
            'max_weight': max_w,
            'min_weight': min_w,
            'weights': sorted(set(weights)),
            'weight_bound_2r': max_w <= 2 * n,
            'below_cusp_threshold': max_w < 12,
            'graphs': graphs,
        }

    return results


def cusp_form_dimension(k: int) -> int:
    """Dimension of the space of cusp forms S_k(SL(2,Z)).

    For k < 12 or k odd: dim = 0.
    For k = 12: dim = 1 (Ramanujan Delta).
    General formula: dim S_k = floor(k/12) - 1 if k = 2 mod 12,
                              floor(k/12) otherwise (for even k >= 12).
    """
    if k < 12 or k % 2 != 0:
        return 0
    if k == 12:
        return 1
    # General: dim M_k - 1 (subtracting the Eisenstein series)
    # dim M_k = floor(k/12) + 1 if k != 2 mod 12, floor(k/12) if k = 2 mod 12
    if k % 12 == 2:
        return k // 12 - 1
    return k // 12


def modular_form_dimension(k: int) -> int:
    """Dimension of the space of modular forms M_k(SL(2,Z))."""
    if k < 0 or k % 2 != 0:
        return 0
    if k == 0:
        return 1
    if k == 2:
        return 0  # no holomorphic weight-2 forms for SL(2,Z)
    if k % 12 == 2:
        return k // 12
    return k // 12 + 1


def shadow_multiplicativity_theorem_data(max_arity: int = 7) -> Dict[str, Any]:
    """Generate all data for the shadow multiplicativity theorem.

    Returns:
    - Weight bounds at each arity
    - Cusp form dimensions at each weight
    - Critical arity where cusp forms first appear
    - Hecke eigenform decomposition status at each weight
    """
    wb = weight_bound_analysis(max_arity)

    data: Dict[str, Any] = {
        'arity_data': {},
        'critical_arity': None,
        'automatic_multiplicativity_range': [],
    }

    for r in range(0, max_arity + 1):
        if r not in wb:
            continue
        wd = wb[r]
        max_w = wd['max_weight']
        cusp_dim = cusp_form_dimension(max_w) if max_w > 0 else 0
        mf_dim = modular_form_dimension(max_w) if max_w > 0 else 0

        entry = {
            'max_weight': max_w,
            'num_graphs': wd['num_graphs'],
            'weight_bound_2r': wd['weight_bound_2r'],
            'cusp_form_dim': cusp_dim,
            'modular_form_dim': mf_dim,
            'below_cusp_threshold': max_w < 12,
            'automatic_multiplicativity': max_w < 12 and wd['num_graphs'] > 0,
        }
        data['arity_data'][r] = entry

        if entry['automatic_multiplicativity']:
            data['automatic_multiplicativity_range'].append(r)

        if cusp_dim > 0 and data['critical_arity'] is None:
            data['critical_arity'] = r

    return data
