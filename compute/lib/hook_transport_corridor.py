"""Hook-type transport corridor and reduction graph for type-A W-algebras.

Verifies the mathematical content of:
  - thm:hook-transport-corridor (hook-type duality at generic level)
  - prop:transport-propagation (duality propagates through reduction graph)
  - conj:type-a-transport-to-transpose (transport-closure = Par(N))

The reduction graph Gamma_N has vertices = partitions of N, edges =
proved reduction/inverse-reduction functors at generic level.  The hook
vertices form a connected spine.  Transport propagation says: if duality
is verified at all hook vertices and intertwines all edges, then it holds
on the transport-closure.

This module is orbit-combinatorial.  Central charge verification for
specific families is in w_orbit_duality.py and nonprincipal_ds_reduction.py.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, FrozenSet, List, Set, Tuple

from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    _partitions_of_n,
    hook_partition,
    is_hook_partition,
    normalize_partition,
    transpose_partition,
    type_a_orbit_class,
)


# ---------------------------------------------------------------------------
#  Reduction graph Gamma_N
# ---------------------------------------------------------------------------

@dataclass
class ReductionGraph:
    """The reduction graph Gamma_N for type-A W-algebras.

    Vertices: partitions of N.
    Edges: proved reduction/inverse-reduction functors at generic level.

    Edge types (with literature references):
    - Hook spine: (N-r,1^r) <-> (N-r-1,1^{r+1}) [Fehily, inverse reduction]
    - Two-row to hook: (a,b) <-> (a+b-1,1) [Genra-Juillard, reduction by stages]
    - Row-merge: (a,b,c,...) <-> (a+b,c,...) [Butson-Nair, geometric inverse HR]

    This is a conservative lower bound on the actual edge set. The conjecture
    (conj:type-a-transport-to-transpose) asserts that the transport-closure
    of hooks covers all of Par(N).
    """

    N: int
    vertices: FrozenSet[Partition] = field(default_factory=frozenset)
    edges: FrozenSet[Tuple[Partition, Partition]] = field(default_factory=frozenset)

    @classmethod
    def build(cls, N: int) -> "ReductionGraph":
        """Build the reduction graph for sl_N."""
        vertices = frozenset(_partitions_of_n(N))
        edges: Set[Tuple[Partition, Partition]] = set()

        # Hook-to-hook edges: (N-r, 1^r) <-> (N-r-1, 1^{r+1})
        # These are the inverse-reduction functors of Fehily.
        for r in range(N - 1):
            src = hook_partition(N, r)
            if r + 1 <= N - 1:
                tgt = hook_partition(N, r + 1)
                edges.add((src, tgt))
                edges.add((tgt, src))

        # Reduction-by-stages: from two-row partitions to hook type.
        # For (a, b) with a >= b >= 2, there is a proved reduction
        # path (a, b) -> (a+b-1, 1) [GenraStages].
        for lam in vertices:
            if len(lam) == 2 and lam[1] >= 2:
                hook_target = hook_partition(N, lam[1])
                edges.add((lam, hook_target))
                edges.add((hook_target, lam))

        # Row-merge edges: for partitions with 3+ parts, merging the
        # two largest parts gives a reduction edge [ButsonNair].
        for lam in vertices:
            if len(lam) >= 3:
                merged = normalize_partition(
                    (lam[0] + lam[1],) + lam[2:]
                )
                if merged in vertices:
                    edges.add((lam, merged))
                    edges.add((merged, lam))

        return cls(N=N, vertices=vertices, edges=frozenset(edges))

    def hook_vertices(self) -> FrozenSet[Partition]:
        """Return the hook-type vertices (including principal and trivial)."""
        return frozenset(v for v in self.vertices if is_hook_partition(v))

    def transport_closure(self, seeds: FrozenSet[Partition]) -> FrozenSet[Partition]:
        """BFS from seed vertices through edges."""
        visited: Set[Partition] = set(seeds)
        frontier: List[Partition] = list(seeds)
        while frontier:
            current = frontier.pop()
            for src, tgt in self.edges:
                if src == current and tgt not in visited:
                    visited.add(tgt)
                    frontier.append(tgt)
        return frozenset(visited)

    def hook_transport_closure(self) -> FrozenSet[Partition]:
        """Transport-closure starting from hook vertices."""
        return self.transport_closure(self.hook_vertices())

    def is_fully_connected(self) -> bool:
        """Check if the transport-closure of hooks covers all vertices."""
        return self.hook_transport_closure() == self.vertices

    def edge_count(self) -> int:
        """Number of directed edges."""
        return len(self.edges)

    def undirected_edge_count(self) -> int:
        """Number of undirected edges (each pair counted once)."""
        seen = set()
        for a, b in self.edges:
            pair = (min(a, b), max(a, b))
            seen.add(pair)
        return len(seen)

    def neighbors(self, v: Partition) -> FrozenSet[Partition]:
        """Return all neighbors of a vertex."""
        return frozenset(
            tgt for src, tgt in self.edges if src == v
        )

    def path_exists(self, start: Partition, end: Partition) -> bool:
        """Check if a path exists from start to end."""
        return end in self.transport_closure(frozenset({start}))


# ---------------------------------------------------------------------------
#  Transport propagation verification
# ---------------------------------------------------------------------------

def verify_transport_propagation(N: int) -> dict:
    """Verify Proposition prop:transport-propagation for sl_N.

    Returns a dict with:
    - 'N': the rank parameter
    - 'num_partitions': |Par(N)|
    - 'num_hooks': number of hook vertices
    - 'transport_closure_size': size of hook transport-closure
    - 'fully_connected': whether closure = Par(N)
    - 'unreached': set of unreached partitions (if any)
    - 'num_edges': number of undirected edges
    """
    G = ReductionGraph.build(N)
    hooks = G.hook_vertices()
    closure = G.hook_transport_closure()
    unreached = G.vertices - closure

    return {
        'N': N,
        'num_partitions': len(G.vertices),
        'num_hooks': len(hooks),
        'transport_closure_size': len(closure),
        'fully_connected': len(unreached) == 0,
        'unreached': unreached,
        'num_edges': G.undirected_edge_count(),
    }


def verify_transpose_closure_invariance(N: int) -> bool:
    """Check that the transport-closure is closed under partition transpose."""
    G = ReductionGraph.build(N)
    closure = G.hook_transport_closure()
    for lam in closure:
        if transpose_partition(lam) not in closure:
            return False
    return True


def reduction_graph_summary(max_N: int = 10) -> list:
    """Summary table of reduction graphs for N = 2..max_N."""
    results = []
    for N in range(2, max_N + 1):
        results.append(verify_transport_propagation(N))
    return results
