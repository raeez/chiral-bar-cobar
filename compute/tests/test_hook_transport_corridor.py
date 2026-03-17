"""Tests for the hook-type transport corridor and reduction graph.

Verifies:
  - thm:hook-transport-corridor: hook-type duality at generic level
  - prop:transport-propagation: duality propagates through Gamma_N
  - conj:type-a-transport-to-transpose: hook transport-closure = Par(N)

References:
  - Fehily (FehilyHook), Genra-Juillard (GenraStages),
    Butson-Nair (ButsonNair), CLNS24, CFLN24
"""

import pytest

from compute.lib.hook_transport_corridor import (
    ReductionGraph,
    verify_transport_propagation,
    verify_transpose_closure_invariance,
)
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    hook_partition,
    is_hook_partition,
    normalize_partition,
    transpose_partition,
)


# ===================================================================
#  Reduction graph: construction
# ===================================================================

class TestReductionGraphConstruction:
    """Basic construction and vertex counts."""

    @pytest.mark.parametrize("N,expected_partitions", [
        (2, 2),    # (2), (1,1)
        (3, 3),    # (3), (2,1), (1,1,1)
        (4, 5),    # (4), (3,1), (2,2), (2,1,1), (1,1,1,1)
        (5, 7),
        (6, 11),
        (7, 15),
        (8, 22),
    ])
    def test_vertex_count(self, N, expected_partitions):
        """Gamma_N has |Par(N)| vertices."""
        G = ReductionGraph.build(N)
        assert len(G.vertices) == expected_partitions

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_vertices_are_all_partitions(self, N):
        """Gamma_N has exactly Par(N) as vertices."""
        G = ReductionGraph.build(N)
        assert G.vertices == frozenset(_partitions_of_n(N))

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_hook_vertex_count(self, N):
        """There are exactly N hook vertices (including principal/trivial)."""
        G = ReductionGraph.build(N)
        assert len(G.hook_vertices()) == N

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7])
    def test_edges_are_symmetric(self, N):
        """Every edge (a,b) has reverse edge (b,a)."""
        G = ReductionGraph.build(N)
        for src, tgt in G.edges:
            assert (tgt, src) in G.edges


# ===================================================================
#  Hook spine connectivity
# ===================================================================

class TestHookSpine:
    """Hook vertices form a connected path (the spine)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8, 10])
    def test_hook_spine_is_path(self, N):
        """Consecutive hooks (N-r,1^r) and (N-r-1,1^{r+1}) are adjacent."""
        G = ReductionGraph.build(N)
        for r in range(N - 1):
            src = hook_partition(N, r)
            tgt = hook_partition(N, r + 1)
            assert (src, tgt) in G.edges

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7])
    def test_principal_to_trivial_path(self, N):
        """A path exists from principal (N) to trivial (1^N)."""
        G = ReductionGraph.build(N)
        principal = hook_partition(N, 0)
        trivial = hook_partition(N, N - 1)
        assert G.path_exists(principal, trivial)


# ===================================================================
#  Transport closure = Par(N) (conj:type-a-transport-to-transpose)
# ===================================================================

class TestTransportClosure:
    """conj:type-a-transport-to-transpose: hook closure = Par(N)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 7, 8])
    def test_hook_transport_closure_covers_all(self, N):
        """Transport-closure of hooks covers all partitions."""
        result = verify_transport_propagation(N)
        assert result['fully_connected'], (
            f"N={N}: transport-closure misses {result['unreached']}"
        )

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7])
    def test_two_row_partitions_reached(self, N):
        """All two-row partitions (a,b) are reached from hooks."""
        G = ReductionGraph.build(N)
        closure = G.hook_transport_closure()
        for lam in G.vertices:
            if len(lam) == 2:
                assert lam in closure, f"Two-row {lam} not in closure"

    def test_n4_two_two_reached(self):
        """(2,2) in sl_4 is reached from hooks."""
        G = ReductionGraph.build(4)
        closure = G.hook_transport_closure()
        assert (2, 2) in closure

    def test_n5_three_two_reached(self):
        """(3,2) in sl_5 is reached from hooks."""
        G = ReductionGraph.build(5)
        closure = G.hook_transport_closure()
        assert (3, 2) in closure

    def test_n6_three_row_partitions_reached(self):
        """Three-row partitions in sl_6 are reached from hooks."""
        G = ReductionGraph.build(6)
        closure = G.hook_transport_closure()
        assert (3, 2, 1) in closure
        assert (2, 2, 2) in closure

    def test_n7_general_partitions_reached(self):
        """General partitions in sl_7 are reached from hooks."""
        G = ReductionGraph.build(7)
        closure = G.hook_transport_closure()
        assert (3, 2, 2) in closure
        assert (3, 2, 1, 1) in closure
        assert (2, 2, 2, 1) in closure


# ===================================================================
#  Transpose closure invariance
# ===================================================================

class TestTransposeInvariance:
    """Transport-closure is closed under partition transpose."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7, 8])
    def test_closure_transpose_invariant(self, N):
        """If lam is in the closure, so is lam^t."""
        assert verify_transpose_closure_invariance(N)


# ===================================================================
#  Transport propagation (prop:transport-propagation)
# ===================================================================

class TestTransportPropagation:
    """prop:transport-propagation: duality propagates from hooks."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_every_non_hook_has_hook_path(self, N):
        """Every non-hook partition is reachable from some hook vertex."""
        G = ReductionGraph.build(N)
        hooks = G.hook_vertices()
        for lam in G.vertices:
            if lam not in hooks:
                # Must be reachable from some hook
                reachable_from_hooks = G.hook_transport_closure()
                assert lam in reachable_from_hooks, (
                    f"Non-hook partition {lam} not reachable from hooks"
                )

    @pytest.mark.parametrize("N", [4, 5, 6])
    def test_transpose_edges_exist_for_reached_pairs(self, N):
        """For reachable non-hook lam, both lam and lam^t are in closure."""
        G = ReductionGraph.build(N)
        closure = G.hook_transport_closure()
        for lam in closure:
            lam_t = transpose_partition(lam)
            assert lam_t in closure, (
                f"Transpose {lam_t} of reachable {lam} not in closure"
            )


# ===================================================================
#  Partition transpose properties
# ===================================================================

class TestPartitionTranspose:
    """Basic partition transpose properties used by the corridor."""

    @pytest.mark.parametrize("N,r", [
        (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1), (4, 2), (4, 3),
        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
    ])
    def test_hook_transpose_is_hook(self, N, r):
        """Transpose of a hook partition is a hook partition."""
        eta = hook_partition(N, r)
        eta_t = transpose_partition(eta)
        assert is_hook_partition(eta_t)
        assert sum(eta_t) == N

    @pytest.mark.parametrize("N,r", [
        (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1), (4, 2), (4, 3),
        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),
    ])
    def test_double_transpose_is_identity(self, N, r):
        """Transpose is an involution."""
        eta = hook_partition(N, r)
        assert transpose_partition(transpose_partition(eta)) == eta

    def test_first_nonselfdual_hook_pair(self):
        """(3,1) <-> (2,1,1) in sl_4 is the first non-self-dual pair."""
        assert transpose_partition((3, 1)) == (2, 1, 1)
        assert (3, 1) != (2, 1, 1)

    def test_self_dual_hook_examples(self):
        """Self-dual hooks: (2,1) in sl_3, (3,1,1) in sl_5."""
        assert transpose_partition((2, 1)) == (2, 1)
        assert transpose_partition((3, 1, 1)) == (3, 1, 1)

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7])
    def test_all_partitions_double_transpose(self, N):
        """Double transpose is identity for all partitions of N."""
        for lam in _partitions_of_n(N):
            assert transpose_partition(transpose_partition(lam)) == lam

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 7])
    def test_transpose_preserves_size(self, N):
        """Transpose preserves partition size."""
        for lam in _partitions_of_n(N):
            assert sum(transpose_partition(lam)) == sum(lam)


# ===================================================================
#  Summary statistics
# ===================================================================

class TestSummaryStatistics:
    """Reduction graph summary statistics."""

    def test_summary_table(self):
        """Generate and verify summary table for N=2..8."""
        from compute.lib.hook_transport_corridor import reduction_graph_summary
        results = reduction_graph_summary(max_N=8)
        for r in results:
            assert r['fully_connected'], (
                f"N={r['N']}: transport-closure incomplete"
            )
            # Transport closure must equal number of partitions
            assert r['transport_closure_size'] == r['num_partitions']
            # Number of hooks = N
            assert r['num_hooks'] == r['N']
