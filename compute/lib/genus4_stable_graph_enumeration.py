r"""Independent genus-4 stable graph enumeration via adjacency-matrix canonical forms.

This module provides a SECOND, independent algorithmic enumeration of
stable graphs, designed to cross-check the count of 379 genus-4 stable
graphs at n=0 (CC7 census claim in higher_genus_modular_koszul.tex).

ALGORITHM (different from stable_graph_enumeration._enumerate_general):

The existing engine in stable_graph_enumeration.py enumerates by:
  - Iterating over genus distributions and edge multisets (as tuples of pairs)
  - Deduplicating via canonical (genera, edge-tuples, legs) triples

This engine uses a fundamentally different representation and canonicalization:
  - Edge configurations are represented as ADJACENCY MATRICES
  - Canonical forms are (genera, adjacency-matrix) pairs under vertex permutation
  - Pruning uses DEGREE CONSTRAINTS from stability (val(v) >= 3 - 2*g(v))
  - Connectivity checking uses union-find (different from BFS in primary engine)

The two engines share the same mathematical definition of stable graph
but differ in data structures, canonical form computation, and enumeration
order. Agreement between them provides strong evidence for correctness.

VERIFIED COUNTS (CC7, AP123, higher_genus_modular_koszul.tex):
  g=1, n=0:   2 stable graphs   (special: 2g-2=0, DM convention)
  g=2, n=0:   7 stable graphs   # AP123: 7 NOT 6
  g=3, n=0:  42 stable graphs
  g=4, n=0: 379 stable graphs   # CC7 census claim

References:
  higher_genus_modular_koszul.tex: sec:genus-4-amplitude
  stable_graph_enumeration.py: enumerate_stable_graphs (cross-check target)
  Faber (1999): "A conjectural description of the tautological ring"
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product as cartprod
from math import factorial
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Genus distributions
# ---------------------------------------------------------------------------

def _genus_distributions(max_genus: int, num_v: int,
                         upper_bound: int = None):
    """Generate all NON-INCREASING tuples of length num_v with
    entries in [0, upper_bound] and sum <= max_genus."""
    if upper_bound is None:
        upper_bound = max_genus
    if num_v == 0:
        if max_genus >= 0:
            yield ()
        return
    if num_v == 1:
        for g in range(min(max_genus, upper_bound), -1, -1):
            yield (g,)
        return
    for g in range(min(max_genus, upper_bound), -1, -1):
        for rest in _genus_distributions(max_genus - g, num_v - 1, g):
            yield (g,) + rest


# ---------------------------------------------------------------------------
# Edge configuration enumeration with stability pruning
# ---------------------------------------------------------------------------

def _min_valence(gv: int) -> int:
    """Minimum valence for a vertex of genus gv to be stable.

    Stability: 2*gv - 2 + val > 0, so val > 2 - 2*gv, i.e. val >= 3 - 2*gv.
    For gv=0: val >= 3. For gv=1: val >= 1. For gv>=2: val >= 0 (auto-stable).
    """
    return max(0, 3 - 2 * gv)


def _enumerate_edge_configs(genera: Tuple[int, ...], num_edges: int):
    """Enumerate adjacency matrices with num_edges edges that could
    yield stable connected graphs.

    Uses degree-constrained enumeration with early pruning:
    1. Compute minimum valence for each vertex from stability.
    2. Assign edges to slots, tracking remaining degree budget.
    3. Prune branches where remaining edges cannot satisfy minimum degrees.
    """
    num_v = len(genera)
    min_vals = [_min_valence(genera[v]) for v in range(num_v)]

    # Edge slots: (i, j) with i <= j
    slots = []
    for i in range(num_v):
        for j in range(i, num_v):
            slots.append((i, j))

    # Current adjacency matrix (mutable during recursion)
    adj = [[0] * num_v for _ in range(num_v)]
    current_val = [0] * num_v

    def _recurse(slot_idx: int, edges_left: int):
        if edges_left == 0:
            # Check all minimum valences satisfied
            for v in range(num_v):
                if current_val[v] < min_vals[v]:
                    return
            yield tuple(tuple(row) for row in adj)
            return
        if slot_idx >= len(slots):
            return

        i, j = slots[slot_idx]
        slots_remaining = len(slots) - slot_idx

        # Pruning: can remaining edges possibly fill minimum degree deficits?
        # Each remaining edge contributes at most 2 to total degree.
        deficit = sum(max(0, min_vals[v] - current_val[v]) for v in range(num_v))
        # Each edge adds 2 to total degree (either 2 for self-loop, or 1+1)
        if 2 * edges_left < deficit:
            return

        # Maximum edges in this slot
        max_here = edges_left

        for k in range(max_here, -1, -1):
            # Assign k edges to slot (i, j)
            if i == j:
                adj[i][i] = k
                current_val[i] += 2 * k
            else:
                adj[i][j] = k
                adj[j][i] = k
                current_val[i] += k
                current_val[j] += k

            yield from _recurse(slot_idx + 1, edges_left - k)

            # Undo
            if i == j:
                current_val[i] -= 2 * k
                adj[i][i] = 0
            else:
                current_val[i] -= k
                current_val[j] -= k
                adj[i][j] = 0
                adj[j][i] = 0

    yield from _recurse(0, num_edges)


# ---------------------------------------------------------------------------
# Connectivity (union-find, different from BFS in primary engine)
# ---------------------------------------------------------------------------

def _is_connected_uf(adj: Tuple[Tuple[int, ...], ...]) -> bool:
    """Check connectivity via union-find (different from primary engine's BFS)."""
    num_v = len(adj)
    if num_v <= 1:
        return True

    parent = list(range(num_v))
    rank = [0] * num_v

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1

    for i in range(num_v):
        if adj[i][i] > 0:
            pass  # self-loops don't affect connectivity
        for j in range(i + 1, num_v):
            if adj[i][j] > 0:
                union(i, j)

    root = find(0)
    return all(find(v) == root for v in range(1, num_v))


# ---------------------------------------------------------------------------
# Valence from adjacency matrix
# ---------------------------------------------------------------------------

def _valence(adj: Tuple[Tuple[int, ...], ...]) -> Tuple[int, ...]:
    """Valence of each vertex. Self-loops contribute 2."""
    num_v = len(adj)
    val = [0] * num_v
    for i in range(num_v):
        val[i] += 2 * adj[i][i]
        for j in range(num_v):
            if j != i:
                val[i] += adj[i][j]
    return tuple(val)


# ---------------------------------------------------------------------------
# Canonical form (adjacency-matrix based)
# ---------------------------------------------------------------------------

def _genus_preserving_perms(genera: Tuple[int, ...]):
    """All vertex permutations preserving the genus labeling."""
    num_v = len(genera)
    by_genus: Dict[int, List[int]] = {}
    for v, g in enumerate(genera):
        by_genus.setdefault(g, []).append(v)

    genus_keys = sorted(by_genus.keys())
    group_data = [
        (by_genus[gk], list(permutations(by_genus[gk])))
        for gk in genus_keys
    ]
    perm_lists = [gd[1] for gd in group_data]
    vert_lists = [gd[0] for gd in group_data]

    for combo in cartprod(*perm_lists):
        perm = list(range(num_v))
        for verts, mapping in zip(vert_lists, combo):
            for old_v, new_v in zip(verts, mapping):
                perm[old_v] = new_v
        yield tuple(perm)


def _canonical_form(adj: Tuple[Tuple[int, ...], ...],
                    genera: Tuple[int, ...]) -> Tuple:
    """Canonical (genera, adjacency-matrix) under vertex permutation.

    Tries all genus-preserving permutations and returns the
    lexicographically smallest representation.
    """
    num_v = len(adj)
    best = None

    for perm in _genus_preserving_perms(genera):
        inv = [0] * num_v
        for old, new in enumerate(perm):
            inv[new] = old
        new_genera = tuple(genera[inv[a]] for a in range(num_v))
        new_adj = tuple(
            tuple(adj[inv[a]][inv[b]] for b in range(num_v))
            for a in range(num_v)
        )
        rep = (new_genera, new_adj)
        if best is None or rep < best:
            best = rep
    return best


# ---------------------------------------------------------------------------
# Automorphism order
# ---------------------------------------------------------------------------

def _automorphism_order(adj: Tuple[Tuple[int, ...], ...],
                        genera: Tuple[int, ...]) -> int:
    """Count automorphisms of (adj, genera).

    Vertex permutations preserving genera and adjacency, times
    edge-level factors (self-loop flips + parallel edge permutations).
    """
    num_v = len(adj)
    count = 0

    for perm in _genus_preserving_perms(genera):
        inv = [0] * num_v
        for old, new in enumerate(perm):
            inv[new] = old

        preserves = True
        for a in range(num_v):
            for b in range(a, num_v):
                if adj[inv[a]][inv[b]] != adj[a][b]:
                    preserves = False
                    break
            if not preserves:
                break
        if not preserves:
            continue

        edge_factor = 1
        for i in range(num_v):
            k = adj[i][i]
            edge_factor *= factorial(k) * (2 ** k)
        for i in range(num_v):
            for j in range(i + 1, num_v):
                edge_factor *= factorial(adj[i][j])
        count += edge_factor

    return count


# ---------------------------------------------------------------------------
# Main enumeration
# ---------------------------------------------------------------------------

def enumerate_stable_graphs_independent(g: int, n: int = 0) -> List[dict]:
    """Enumerate all connected stable graphs of genus g with n=0.

    Returns list of dicts with graph data.
    Independent implementation from stable_graph_enumeration.py.
    """
    if n != 0:
        raise NotImplementedError("Only n=0 supported")
    if 2 * g - 2 <= 0:
        return []

    results = []
    seen = set()
    max_v = 2 * g - 2

    for num_v in range(1, max_v + 1):
        for genera in _genus_distributions(g, num_v):
            sum_gv = sum(genera)
            if sum_gv > g:
                continue
            h1 = g - sum_gv
            num_edges = h1 + num_v - 1
            if num_edges < 0:
                continue

            for adj in _enumerate_edge_configs(genera, num_edges):
                if not _is_connected_uf(adj):
                    continue

                canon = _canonical_form(adj, genera)
                if canon in seen:
                    continue
                seen.add(canon)

                val = _valence(adj)
                aut = _automorphism_order(adj, genera)

                results.append({
                    'genera': genera,
                    'adj': adj,
                    'num_vertices': num_v,
                    'num_edges': num_edges,
                    'h1': h1,
                    'valence': val,
                    'aut_order': aut,
                })

    return results


# ---------------------------------------------------------------------------
# Census functions
# ---------------------------------------------------------------------------

@lru_cache(maxsize=8)
def count_stable_graphs(g: int) -> int:
    """Count stable graphs at genus g, n=0."""
    return len(enumerate_stable_graphs_independent(g))


def count_by_vertices(g: int) -> Dict[int, int]:
    graphs = enumerate_stable_graphs_independent(g)
    return dict(sorted(Counter(gr['num_vertices'] for gr in graphs).items()))


def count_by_edges(g: int) -> Dict[int, int]:
    graphs = enumerate_stable_graphs_independent(g)
    return dict(sorted(Counter(gr['num_edges'] for gr in graphs).items()))


def count_by_loop_number(g: int) -> Dict[int, int]:
    graphs = enumerate_stable_graphs_independent(g)
    return dict(sorted(Counter(gr['h1'] for gr in graphs).items()))


def count_by_ve(g: int) -> Dict[Tuple[int, int], int]:
    graphs = enumerate_stable_graphs_independent(g)
    return dict(sorted(
        Counter((gr['num_vertices'], gr['num_edges']) for gr in graphs).items()
    ))


def automorphism_spectrum(g: int) -> List[int]:
    graphs = enumerate_stable_graphs_independent(g)
    return sorted(gr['aut_order'] for gr in graphs)


def inverse_aut_sum(g: int) -> Fraction:
    graphs = enumerate_stable_graphs_independent(g)
    return sum(Fraction(1, gr['aut_order']) for gr in graphs)


# ---------------------------------------------------------------------------
# Orbifold Euler characteristic
# ---------------------------------------------------------------------------

def _bernoulli(n: int) -> Fraction:
    """Bernoulli number B_n."""
    if n == 0: return Fraction(1)
    if n == 1: return Fraction(-1, 2)
    if n % 2 == 1 and n > 1: return Fraction(0)
    a = [Fraction(1, m + 1) for m in range(n + 1)]
    for j in range(1, n + 1):
        for m in range(n, j - 1, -1):
            a[m] = (m - j + 1) * (a[m] - a[m - 1])
    return a[n]


@lru_cache(maxsize=64)
def _chi_orb_open(g: int, n: int) -> Fraction:
    """chi^orb(M_{g,n})."""
    if 2 * g - 2 + n <= 0:
        raise ValueError(f"Unstable: (g,n)=({g},{n})")
    if g == 0:
        return Fraction((-1) ** (n - 1) * factorial(n - 3))
    if g == 1 and n == 1:
        return Fraction(-1, 12)
    if g >= 2 and n == 0:
        return _bernoulli(2 * g) / Fraction(4 * g * (g - 1))
    return Fraction(2 * g - 2 + n - 1) * _chi_orb_open(g, n - 1)


def orbifold_euler_char(g: int) -> Fraction:
    """chi^orb(M_bar_{g,0}) via graph sum."""
    graphs = enumerate_stable_graphs_independent(g)
    total = Fraction(0)
    for gr in graphs:
        genera = gr['genera']
        val = gr['valence']
        num_v = gr['num_vertices']
        vp = Fraction(1)
        for v in range(num_v):
            vp *= _chi_orb_open(genera[v], val[v])
        total += vp / Fraction(gr['aut_order'])
    return total


# ---------------------------------------------------------------------------
# Cross-check
# ---------------------------------------------------------------------------

def cross_check_with_primary(g: int) -> Dict:
    """Cross-check against the primary engine."""
    from compute.lib.stable_graph_enumeration import enumerate_stable_graphs

    primary = enumerate_stable_graphs(g, 0)
    independent = enumerate_stable_graphs_independent(g)

    pc = len(primary)
    ic = len(independent)

    p_v = dict(sorted(Counter(gr.num_vertices for gr in primary).items()))
    i_v = count_by_vertices(g)
    p_e = dict(sorted(Counter(gr.num_edges for gr in primary).items()))
    i_e = count_by_edges(g)
    p_h = dict(sorted(Counter(gr.first_betti for gr in primary).items()))
    i_h = count_by_loop_number(g)

    return {
        'genus': g,
        'primary_count': pc,
        'independent_count': ic,
        'counts_match': pc == ic,
        'by_vertices_match': p_v == i_v,
        'by_edges_match': p_e == i_e,
        'by_h1_match': p_h == i_h,
        'all_match': pc == ic and p_v == i_v and p_e == i_e and p_h == i_h,
    }
