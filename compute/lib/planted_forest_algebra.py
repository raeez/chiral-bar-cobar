r"""Planted forest coefficient algebra G_pf — the combinatorial heart of the
modular convolution algebra.

A **planted forest** on n leaves is a rooted tree with:
  - One distinguished root vertex (vertex 0)
  - n labeled leaves {1, ..., n}
  - Internal vertices (neither root nor leaf) with valence >= 2
  - Each internal vertex has a "parent edge" (towards root) and >= 1 "child edges"

The composition law on G_pf comes from grafting + residue:
  F_1 circ_i F_2 grafts F_2 at the i-th leaf of F_1, producing a forest
  on (n_1 + n_2 - 1) leaves.  The coefficient encodes the residue
  correspondence on log FM boundary strata.

The chain differential d_pf contracts internal edges:
  d_pf(F) = Sum_{e in internal edges} +/- F/e

The depth filtration stratifies the shadow tower:
  d = longest root-to-leaf path length

The tridegree of a planted forest is (g, n, d) where:
  g = loop genus = 0 for trees (no cycles)
  n = number of leaves
  d = depth

KEY ENUMERATIVE FACTS:
  At each arity n, the number of labeled rooted trees on n+1 vertices
  (root=0, leaves=1..n) is (n+1)^{n-1} by Cayley's formula.
  But we enumerate ALL rooted trees, not just binary ones:
    n=1: 1 tree  (root -- leaf 1)
    n=2: 1 tree  (root with children 1, 2)
    n=3: 4 trees (3 binary + 1 ternary)
    n=4: 26 trees
    n=5: 236 trees

  Planar planted forests (remembering left-right order) at arity n are
  counted by the Catalan number C_{n-1} for binary trees, and by the
  super-Catalan / Schroder numbers for general trees.

ASSOCIAHEDRON CONNECTION:
  At genus 0, the binary planted forests are dual to faces of K_n.
  The full planted forest complex (including non-binary trees) is the
  chain complex of the Stasheff associahedron viewed as a CW complex
  where k-ary vertices correspond to (k-2)-dimensional cells.

References:
  - higher_genus_modular_koszul.tex: def:planted-forest-coefficient-algebra
  - bar_cobar_adjunction_inversion.tex: bar complex, planted forests
  - concordance.tex: const:vol1-graphwise-log-fm-cocomposition
  - Mok25: log FM tropicalization
  - Stasheff 1963: associahedra
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import permutations, product as cartprod
from math import factorial, comb
from typing import Dict, FrozenSet, List, Optional, Set, Tuple


# =========================================================================
# Core data structure: PlantedForest
# =========================================================================

@dataclass(frozen=True)
class PlantedForest:
    """A planted forest (rooted tree) with labeled leaves.

    Vertices are integers: 0 = root, 1..n = leaves, n+1.. = internal.
    Edges are frozensets of (parent, child) pairs, oriented root-to-leaf.

    Attributes:
        n_leaves: number of labeled leaves (arity)
        edges: tuple of (parent, child) pairs, sorted
        internal_vertices: frozenset of non-root, non-leaf vertices

    Convention: edges are directed FROM root TOWARDS leaves.
    Edge (u, v) means u is the parent and v is the child.
    """
    n_leaves: int
    edges: Tuple[Tuple[int, int], ...]  # (parent, child) pairs
    internal_vertices: FrozenSet[int] = frozenset()

    @property
    def vertices(self) -> FrozenSet[int]:
        """All vertices: root + leaves + internal."""
        return frozenset({0}) | frozenset(range(1, self.n_leaves + 1)) | self.internal_vertices

    @property
    def leaf_set(self) -> FrozenSet[int]:
        return frozenset(range(1, self.n_leaves + 1))

    @property
    def num_edges(self) -> int:
        return len(self.edges)

    @property
    def num_internal_edges(self) -> int:
        """Number of edges between non-leaf vertices.

        An internal edge connects two non-leaf vertices (root or internal).
        """
        leaves = self.leaf_set
        return sum(1 for (u, v) in self.edges if v not in leaves)

    @property
    def num_vertices(self) -> int:
        return len(self.vertices)

    @property
    def depth(self) -> int:
        """Longest root-to-leaf path length (= log boundary depth d)."""
        children = defaultdict(list)
        for u, v in self.edges:
            children[u].append(v)

        def _depth(v):
            if v in self.leaf_set:
                return 0
            if not children[v]:
                return 0
            return 1 + max(_depth(c) for c in children[v])

        return _depth(0)

    @property
    def tridegree(self) -> Tuple[int, int, int]:
        """Tridegree (g, n, d) = (loop genus, arity, depth)."""
        return (0, self.n_leaves, self.depth)

    def children_of(self, v: int) -> List[int]:
        """Return children of vertex v."""
        return [c for (u, c) in self.edges if u == v]

    def parent_of(self, v: int) -> Optional[int]:
        """Return parent of vertex v, or None if v is root."""
        if v == 0:
            return None
        for (u, c) in self.edges:
            if c == v:
                return u
        return None

    def valence(self, v: int) -> int:
        """Valence of vertex v in the tree.

        Root: out-degree only.
        Internal: in-degree (1) + out-degree.
        Leaf: in-degree (1) only.
        """
        out = sum(1 for (u, c) in self.edges if u == v)
        inp = sum(1 for (u, c) in self.edges if c == v)
        return out + inp

    def root_valence(self) -> int:
        """Number of children of the root."""
        return len(self.children_of(0))

    def is_binary(self) -> bool:
        """Check if every internal vertex (including root) has exactly 2 children."""
        for v in self.vertices:
            if v in self.leaf_set:
                continue
            children = self.children_of(v)
            if len(children) != 2:
                return False
        return True

    def is_corolla(self) -> bool:
        """Check if all leaves are children of the root (single-vertex tree)."""
        return all(u == 0 for (u, v) in self.edges)

    def leaf_depth(self, leaf: int) -> int:
        """Distance from root to a specific leaf."""
        v = leaf
        d = 0
        while v != 0:
            v = self.parent_of(v)
            d += 1
            if v is None:
                raise ValueError(f"Leaf {leaf} not connected to root")
        return d

    def internal_edge_list(self) -> List[Tuple[int, int]]:
        """List edges that connect two non-leaf vertices."""
        leaves = self.leaf_set
        return [(u, v) for (u, v) in self.edges if v not in leaves]

    def canonical_key(self) -> Tuple:
        """Canonical form for comparison and hashing.

        We canonicalize by sorting edges and using a standard representation.
        """
        return (self.n_leaves, tuple(sorted(self.edges)), tuple(sorted(self.internal_vertices)))

    def __eq__(self, other):
        if not isinstance(other, PlantedForest):
            return NotImplemented
        return self.canonical_key() == other.canonical_key()

    def __hash__(self):
        return hash(self.canonical_key())

    def __repr__(self):
        if self.is_corolla():
            return f"Corolla({self.n_leaves})"
        return f"PlantedForest(n={self.n_leaves}, edges={self.edges})"


# =========================================================================
# Construction helpers
# =========================================================================

def corolla(n: int) -> PlantedForest:
    """The corolla on n leaves: root vertex with n leaf children.

    This is the unique tree of depth 1 = the single-vertex tree.
    """
    edges = tuple((0, i) for i in range(1, n + 1))
    return PlantedForest(n_leaves=n, edges=edges)


def binary_tree(left_leaves: Tuple[int, ...], right_leaves: Tuple[int, ...],
                n: int, next_internal: int) -> Tuple[PlantedForest, int]:
    """Build a binary tree at the root with given leaf partitions.

    This is a helper for building trees recursively.
    Returns the tree and the next available internal vertex label.
    """
    edges = []
    internal = set()
    nxt = next_internal

    def _build(parent, leaves, nxt_id):
        if len(leaves) == 1:
            edges.append((parent, leaves[0]))
            return nxt_id
        if len(leaves) == 0:
            return nxt_id
        # Create an internal vertex
        v = nxt_id
        nxt_id += 1
        internal.add(v)
        edges.append((parent, v))
        # Split: first leaf on left, rest recursively
        edges.append((v, leaves[0]))
        for lf in leaves[1:]:
            edges.append((v, lf))
        return nxt_id

    # Build left subtree under root
    if len(left_leaves) == 1:
        edges.append((0, left_leaves[0]))
    else:
        nxt = _build(0, left_leaves, nxt)

    if len(right_leaves) == 1:
        edges.append((0, right_leaves[0]))
    else:
        nxt = _build(0, right_leaves, nxt)

    return PlantedForest(n_leaves=n, edges=tuple(sorted(edges)),
                         internal_vertices=frozenset(internal)), nxt


# =========================================================================
# Enumeration of planted forests (rooted labeled trees)
# =========================================================================

def _enumerate_rooted_trees_recursive(
    parent: int,
    available_leaves: List[int],
    next_internal: int,
    n_total: int,
) -> List[Tuple[List[Tuple[int, int]], Set[int], int]]:
    """Recursively enumerate all rooted trees.

    Returns list of (edge_list, internal_vertex_set, next_internal).
    parent: the vertex whose subtree we are building.
    available_leaves: leaves that must appear in this subtree.
    """
    if not available_leaves:
        return [([], set(), next_internal)]

    if len(available_leaves) == 1:
        # Single leaf, attach directly to parent
        return [( [(parent, available_leaves[0])], set(), next_internal)]

    results = []

    # For the parent vertex, choose how many children it has (1 to len(available_leaves))
    # and partition the available_leaves among them.
    # A child is either a leaf or an internal vertex leading to a subtree.
    #
    # We enumerate all set partitions of available_leaves into >= 1 non-empty subsets.
    # For each subset: if size 1, the child is a leaf; if size > 1, the child is
    # an internal vertex whose subtree contains those leaves.
    #
    # BUT: we must avoid generating isomorphic trees.
    # Two children of the same vertex are interchangeable (unordered children),
    # so we need to enumerate UNORDERED set partitions.

    for partition in _set_partitions(available_leaves):
        # Each block in the partition is a set of leaves for one child subtree
        # For symmetry, skip if the parent has only one child that is internal
        # with the same leaves (this would just be an unnecessary vertex)
        if len(partition) == 1:
            # Single child with all leaves: this child must be internal
            # with all the leaves below it
            v = next_internal
            child_results = _enumerate_rooted_trees_recursive(
                v, available_leaves, next_internal + 1, n_total
            )
            for child_edges, child_internal, child_next in child_results:
                edges = [(parent, v)] + child_edges
                internal = child_internal | {v}
                results.append((edges, internal, child_next))
            continue

        # Multiple children
        # Each block becomes a subtree
        # Blocks of size 1: leaf directly attached
        # Blocks of size > 1: internal vertex created
        block_options = []
        nxt = next_internal
        for block in partition:
            if len(block) == 1:
                # Leaf child
                block_options.append([
                    ([(parent, block[0])], set(), nxt)
                ])
            else:
                # Internal vertex child
                v = nxt
                nxt_after = nxt + 1
                child_trees = _enumerate_rooted_trees_recursive(
                    v, block, nxt_after, n_total
                )
                opts = []
                for child_edges, child_internal, child_next in child_trees:
                    edges = [(parent, v)] + child_edges
                    internal = child_internal | {v}
                    opts.append((edges, internal, child_next))
                block_options.append(opts)
                # Update nxt to account for vertices used
                # Actually, we need a cleaner approach to vertex numbering

        # The recursive approach with shared vertex numbering is complex.
        # Use a different strategy: build trees canonically then relabel.
        pass

    return results


def _set_partitions(lst: List[int]) -> List[List[List[int]]]:
    """Enumerate all set partitions of lst into non-empty subsets.

    Returns list of partitions, each partition is a list of blocks (sorted lists).
    """
    if not lst:
        return [[]]
    if len(lst) == 1:
        return [[[lst[0]]]]

    first = lst[0]
    rest = lst[1:]
    result = []

    for partition in _set_partitions(rest):
        # Option 1: first element forms its own singleton block
        result.append([[first]] + partition)

        # Option 2: first element joins one of the existing blocks
        for i in range(len(partition)):
            new_partition = [b[:] for b in partition]
            new_partition[i] = sorted([first] + new_partition[i])
            # Canonicalize: sort blocks by their smallest element
            new_partition.sort(key=lambda b: b[0])
            result.append(new_partition)

    return result


def enumerate_planted_forests(n: int) -> List[PlantedForest]:
    """Enumerate all planted forests (rooted labeled trees) on n leaves.

    A planted forest on leaves {1,...,n} is a rooted tree with root 0
    and leaves 1,...,n.  Internal vertices are labeled n+1, n+2, ...

    The count is (n+1)^{n-1} by Cayley's formula for rooted labeled trees
    on {0, 1, ..., n} with root 0.  BUT this counts trees where internal
    vertices are also labeled; we want trees up to relabeling of internal
    vertices.

    Actually: we want rooted trees with the ROOT fixed at 0, LEAVES fixed
    at {1,...,n}, and INTERNAL vertices unlabeled (identified up to
    tree isomorphism preserving root and leaf labels).

    Strategy: Build by recursive decomposition.  At the root, choose a
    partition of leaves into children subtrees.  Recurse for each subtree
    with an internal vertex as its local root.
    """
    if n <= 0:
        return []
    if n == 1:
        # Single tree: root -- leaf 1
        return [corolla(1)]

    # Build trees by choosing the structure at the root.
    # The root has k >= 1 children.
    # Each child is either a leaf or an internal vertex leading to a subtree.
    # The leaves are partitioned among the subtrees.

    return _enumerate_from_root(n)


def _enumerate_from_root(n: int) -> List[PlantedForest]:
    """Enumerate rooted trees with root=0, leaves={1,...,n}.

    Uses canonical tree representation to avoid duplicates.
    """
    leaves = list(range(1, n + 1))
    seen = set()
    results = []

    for partition in _ordered_set_partitions_for_trees(leaves):
        # Each block in the partition is a set of leaves that share
        # a child subtree of the root.
        # For blocks of size 1: the leaf is directly a child of root.
        # For blocks of size > 1: an internal vertex is a child of root,
        #   and the block's leaves hang below it (recursively).

        # Build the tree from this partition
        trees_from_partition = _build_trees_from_root_partition(partition, n)
        for tree in trees_from_partition:
            key = tree.canonical_key()
            if key not in seen:
                seen.add(key)
                results.append(tree)

    return results


def _ordered_set_partitions_for_trees(leaves: List[int]) -> List[List[List[int]]]:
    """Generate unordered set partitions into non-empty blocks.

    Each partition represents a way to distribute leaves among the root's
    child subtrees.  Blocks of size 1 are leaves; blocks of size >= 2
    require internal vertices.

    We canonicalize by sorting blocks by their smallest element.
    """
    return _set_partitions(leaves)


def _build_trees_from_root_partition(
    partition: List[List[int]], n: int
) -> List[PlantedForest]:
    """Build all trees from a given root partition.

    partition: list of blocks, each block is a sorted list of leaf labels.
    For each block of size 1: a direct root-to-leaf edge.
    For each block of size >= 2: create an internal vertex as child of root,
        then recursively build the subtree for that block.
    """
    # Collect the subtree options for each block
    block_tree_options = []
    for block in partition:
        if len(block) == 1:
            # Direct leaf
            block_tree_options.append([('leaf', block[0])])
        else:
            # Need to enumerate subtrees for this block
            subtrees = _enumerate_subtrees(block)
            block_tree_options.append(subtrees)

    # Take cartesian product of options across blocks
    results = []
    for combo in cartprod(*block_tree_options):
        edges = []
        internal = set()
        next_id = n + 1  # internal vertices start after leaves

        for item in combo:
            if item[0] == 'leaf':
                edges.append((0, item[1]))
            else:
                # item = ('subtree', sub_edges, sub_internal_offsets)
                _, sub_edges_template, sub_internal_count = item
                # Allocate internal vertices
                base = next_id
                next_id += sub_internal_count

                # The subtree template uses internal vertices 0, 1, ...
                # Map: template internal 0 -> base, 1 -> base+1, etc.
                # Template root (internal 0) is a child of the actual root.
                root_internal = base
                edges.append((0, root_internal))
                internal.add(root_internal)

                for (tu, tv, is_leaf_v) in sub_edges_template:
                    actual_u = base + tu if tu >= 0 else tu  # negative = leaf label
                    actual_v = tv if is_leaf_v else base + tv
                    if not is_leaf_v:
                        internal.add(actual_v)
                    edges.append((actual_u, actual_v))

        tree = PlantedForest(
            n_leaves=n,
            edges=tuple(sorted(edges)),
            internal_vertices=frozenset(internal),
        )
        results.append(tree)

    return results


def _enumerate_subtrees(leaves: List[int]) -> List[Tuple]:
    """Enumerate subtree structures for a block of leaves.

    Returns list of ('subtree', edge_template, num_internal_vertices).
    The edge_template uses:
      - Internal vertices numbered 0, 1, ...
      - Leaves by their actual label
    Edges are (parent_internal_idx, child, is_child_leaf).
    Internal vertex 0 is always the subtree root.
    """
    if len(leaves) <= 1:
        raise ValueError("Subtrees need at least 2 leaves")

    # Recursively enumerate: the subtree root has k >= 2 children
    # (otherwise it's a redundant pass-through vertex).
    # Each child is either a leaf or a sub-internal vertex.
    results = []

    # Partition leaves among children of the subtree root (vertex 0)
    for partition in _set_partitions(leaves):
        if len(partition) < 2:
            # Must have >= 2 children (otherwise subtree root is redundant)
            continue

        # For each block, recurse
        block_options = []
        for block in partition:
            if len(block) == 1:
                block_options.append([('leaf', block[0])])
            else:
                sub_results = _enumerate_subtrees(block)
                block_options.append(sub_results)

        for combo in cartprod(*block_options):
            edges = []
            num_internal = 1  # vertex 0 = subtree root

            for item in combo:
                if item[0] == 'leaf':
                    edges.append((0, item[1], True))
                else:
                    _, sub_edges, sub_count = item
                    # Offset sub-internal vertices
                    offset = num_internal
                    edges.append((0, offset, False))  # root -> sub-root

                    for (su, sv, is_leaf) in sub_edges:
                        actual_u = su + offset
                        actual_v = sv if is_leaf else sv + offset
                        edges.append((actual_u, actual_v, is_leaf))

                    num_internal += sub_count

            results.append(('subtree', edges, num_internal))

    return results


# =========================================================================
# Cayley count verification
# =========================================================================

def cayley_count(n: int) -> int:
    """Number of labeled rooted trees on vertices {0, 1, ..., n} with root 0.

    By Cayley's formula: (n+1)^{n-1}.
    This counts trees where ALL vertices are distinguishable.
    """
    if n <= 0:
        return 1
    return (n + 1) ** (n - 1)


def planted_forest_count_expected(n: int) -> int:
    """Expected number of planted forests on n leaves (unordered, leaf-labeled).

    These are rooted trees with root 0 and labeled leaves 1..n,
    where internal vertices are unlabeled (up to isomorphism preserving
    root + leaf labels).

    n=1: 1
    n=2: 1 (corolla)
    n=3: 4 (3 binary + 1 ternary)
    n=4: 26
    n=5: 236
    n=6: 2752

    These are the Cayley numbers for rooted labeled forests, equivalent
    to the number of ways to build a rooted tree whose leaves are labeled
    1..n and whose internal vertices can be anything.

    Sequence: this is A000169(n) = n^{n-1} for labeled rooted trees on n nodes,
    but our setting is different (leaves labeled, internals unlabeled).

    Actually: our forests have root=0 (fixed, not a leaf) and leaves 1..n (fixed).
    The number of such trees is given by the recursive formula counting
    rooted trees with n labeled leaves modulo relabeling of internal vertices.
    This equals the number of total partitions / arrangements counted by:

    a(n) = sum over rooted tree shapes T with n leaves of
           (n! / |Aut_leaf(T)|) where Aut_leaf preserves root and leaf labels.

    For n=1: 1
    For n=2: 1 (corolla)
    For n=3: 4 = C(3,2) * 1 (3 binary arrangements) + 1 (ternary corolla)
    For n=4: 26 (verified by explicit enumeration)
    """
    known = {1: 1, 2: 1, 3: 4, 4: 26, 5: 236, 6: 2752}
    if n in known:
        return known[n]
    return -1  # Unknown


# =========================================================================
# Automorphism group computation
# =========================================================================

def automorphism_order(forest: PlantedForest) -> int:
    """Compute |Aut(F)| for a planted forest F.

    An automorphism of a planted forest must:
    - Fix the root (vertex 0)
    - Fix all leaf labels (leaves 1..n are labeled)
    - Permute internal vertices compatibly with the tree structure

    For a rooted tree with labeled leaves, the automorphism group is
    the product over all internal vertices v of S_{k(v)} where k(v) is
    the number of children of v that have ISOMORPHIC subtrees.

    More precisely: at each internal vertex v, the children's subtrees
    form a multiset; Aut permutes identical subtrees.
    """
    return _compute_aut(forest, 0)


def _subtree_signature(forest: PlantedForest, v: int) -> Tuple:
    """Compute a canonical signature for the subtree rooted at v.

    The signature uniquely identifies the isomorphism class of the subtree
    (preserving leaf labels within it).
    """
    if v in forest.leaf_set:
        return ('leaf', v)

    children = forest.children_of(v)
    child_sigs = tuple(sorted(_subtree_signature(forest, c) for c in children))
    return ('node', child_sigs)


def _compute_aut(forest: PlantedForest, v: int) -> int:
    """Compute |Aut| of the subtree at v, fixing root and leaves."""
    if v in forest.leaf_set:
        return 1

    children = forest.children_of(v)
    if not children:
        return 1

    # Compute signatures of children's subtrees
    child_sigs = [_subtree_signature(forest, c) for c in children]

    # Group identical subtrees
    sig_counts = Counter(child_sigs)

    # Aut = product of (k! for each group of k identical subtrees)
    #        * product of (Aut of each child subtree)
    result = 1
    for sig, count in sig_counts.items():
        result *= factorial(count)

    for c in children:
        result *= _compute_aut(forest, c)

    return result


# =========================================================================
# Composition law: grafting + residue
# =========================================================================

def graft(F1: PlantedForest, F2: PlantedForest, leaf_index: int) -> PlantedForest:
    """Graft F2 at the leaf_index-th leaf of F1.

    The i-th leaf of F1 is replaced by the root of F2, and F2's leaves
    become new leaves of the result.  The resulting forest has
    n1 + n2 - 1 leaves.

    Leaf relabeling: leaves of F1 that are < leaf_index keep their labels.
    F2's leaves get labels [leaf_index, ..., leaf_index + n2 - 1].
    F1's leaves > leaf_index get shifted by (n2 - 1).

    This is the geometric content of the operadic composition in G_pf:
    the grafting corresponds to inserting a boundary stratum at the
    collision point specified by leaf_index.
    """
    if leaf_index < 1 or leaf_index > F1.n_leaves:
        raise ValueError(f"leaf_index {leaf_index} out of range [1, {F1.n_leaves}]")

    n1 = F1.n_leaves
    n2 = F2.n_leaves
    n_new = n1 + n2 - 1

    # Build a relabeling map for F1's vertices
    # Root stays 0
    # Leaves: leaf_index is removed (grafted);
    #   leaves < leaf_index keep labels;
    #   leaves > leaf_index shift by (n2 - 1)
    # Internal vertices get new labels starting from n_new + 1
    f1_internal_map = {}
    next_internal = n_new + 1
    for v in sorted(F1.internal_vertices):
        f1_internal_map[v] = next_internal
        next_internal += 1

    def relabel_f1(v):
        if v == 0:
            return 0
        if v in F1.internal_vertices:
            return f1_internal_map[v]
        # v is a leaf
        if v < leaf_index:
            return v
        if v == leaf_index:
            raise ValueError("Should not relabel the grafted leaf")
        # v > leaf_index
        return v + n2 - 1

    # Build a relabeling map for F2's vertices
    # F2's root (0) maps to the graft point
    # F2's leaves map to [leaf_index, ..., leaf_index + n2 - 1]
    # F2's internal vertices get new labels
    f2_internal_map = {}
    for v in sorted(F2.internal_vertices):
        f2_internal_map[v] = next_internal
        next_internal += 1

    # The graft point: the parent of leaf_index in F1 connects to
    # what F2's root connects to.
    graft_point_parent = F1.parent_of(leaf_index)

    def relabel_f2_vertex(v):
        if v == 0:
            return None  # root of F2 is absorbed
        if v in F2.internal_vertices:
            return f2_internal_map[v]
        # v is a leaf of F2 (1..n2)
        return leaf_index + v - 1

    # Build edges of the grafted tree
    new_edges = []
    new_internal = set()

    # Edges from F1, skipping edges to the grafted leaf
    for (u, v) in F1.edges:
        if v == leaf_index:
            # This edge is replaced: parent of leaf_index in F1
            # now connects to F2's root's children
            continue
        new_u = relabel_f1(u)
        new_v = relabel_f1(v)
        new_edges.append((new_u, new_v))
        if new_v > n_new:
            new_internal.add(new_v)
        if new_u > n_new:
            new_internal.add(new_u)

    # The parent of leaf_index in F1 connects to F2's root's children
    # If F2's root has children c1, c2, ..., then:
    # - parent(leaf_index) -> relabel_f2(ci) for each child ci of F2's root
    # BUT this makes parent(leaf_index) absorb F2's root.
    # That changes the tree topology (increasing valence of parent).
    #
    # Actually, for the OPERAD composition:
    # We should keep F2's root as an internal vertex connecting
    # parent(leaf_index) to F2's children.
    # This way the grafting preserves the tree structure.

    # F2's root becomes an internal vertex in the grafted tree
    # It sits between graft_point_parent and F2's children.
    f2_root_new = next_internal
    next_internal += 1
    new_internal.add(f2_root_new)

    # Edge from F1's parent of leaf_index to F2's root
    graft_parent = relabel_f1(graft_point_parent) if graft_point_parent is not None else 0
    new_edges.append((graft_parent, f2_root_new))

    # Edges from F2 (replacing F2's root=0 with f2_root_new)
    for (u, v) in F2.edges:
        new_u = f2_root_new if u == 0 else relabel_f2_vertex(u)
        new_v = relabel_f2_vertex(v)
        if new_u is None or new_v is None:
            raise ValueError("Failed to relabel F2 vertex")
        new_edges.append((new_u, new_v))
        if new_v > n_new:
            new_internal.add(new_v)
        if new_u > n_new:
            new_internal.add(new_u)

    # Remove root from internal if present
    new_internal.discard(0)
    # Remove leaves from internal
    for i in range(1, n_new + 1):
        new_internal.discard(i)

    return PlantedForest(
        n_leaves=n_new,
        edges=tuple(sorted(new_edges)),
        internal_vertices=frozenset(new_internal),
    )


def composition_coefficient(F1: PlantedForest, F2: PlantedForest,
                            leaf_index: int) -> Fraction:
    """Coefficient of the composition F1 circ_i F2 in G_pf.

    The basic coefficient for grafting is 1 (just tree insertion).
    The log FM residue correction introduces multinomial factors
    for non-binary vertices:

    For a vertex of valence k created by grafting, the residue
    weight is 1/(k-1)! from the normal-crossing factor of the
    log FM stratum.

    In the simplest case (both trees binary, grafting doesn't create
    non-binary vertices): coefficient = 1.

    For higher valence: coefficient = product over affected vertices v of
    1 / (symmetry factor at v).
    """
    # For the basic operadic composition, the coefficient is 1.
    # The residue correspondence correction is higher-order and
    # involves the explicit stratum geometry.
    #
    # At the combinatorial level of the coefficient algebra,
    # the composition is simply grafting with coefficient 1.
    return Fraction(1)


# =========================================================================
# Differential: edge contraction
# =========================================================================

def contract_internal_edge(forest: PlantedForest, edge: Tuple[int, int]) -> PlantedForest:
    """Contract an internal edge (u, v) where v is NOT a leaf.

    Contracting edge (u, v) merges v into u:
    - All children of v become children of u
    - v is removed from internal vertices
    - The edge (u, v) is removed
    """
    u, v = edge
    if v in forest.leaf_set:
        raise ValueError(f"Cannot contract edge to leaf {v}")
    if edge not in forest.edges:
        raise ValueError(f"Edge {edge} not in forest")

    new_edges = []
    for (a, b) in forest.edges:
        if (a, b) == edge:
            continue  # remove the contracted edge
        # Replace v with u everywhere
        new_a = u if a == v else a
        new_b = u if b == v else b
        new_edges.append((new_a, new_b))

    # Remove v from internal vertices
    new_internal = forest.internal_vertices - {v}

    # Need to relabel internal vertices to keep them contiguous
    # Actually, we just remove v; the labels may have gaps but that's fine
    # for our canonical key comparison.

    return PlantedForest(
        n_leaves=forest.n_leaves,
        edges=tuple(sorted(new_edges)),
        internal_vertices=frozenset(new_internal),
    )


def chain_differential(forest: PlantedForest) -> Dict[PlantedForest, Fraction]:
    """Compute d_pf(F) = Sum_{e internal} (-1)^{sigma(e)} F/e.

    The sign sigma(e) is the position of the edge in a fixed ordering
    of internal edges (ordered by parent vertex, then child vertex).

    Returns a dictionary {contracted_forest: coefficient}.
    """
    internal_edges = forest.internal_edge_list()
    if not internal_edges:
        return {}

    result = defaultdict(Fraction)
    for idx, edge in enumerate(sorted(internal_edges)):
        sign = Fraction((-1) ** idx)
        contracted = contract_internal_edge(forest, edge)
        result[contracted] += sign

    return dict(result)


def verify_d_squared_zero(n: int) -> Dict:
    """Verify d_pf^2 = 0 on all planted forests at arity n.

    d^2 = 0 follows from the CW chain complex structure: each
    codimension-2 cell appears as a boundary of exactly two
    codimension-1 cells with opposite signs.
    """
    forests = enumerate_planted_forests(n)
    all_pass = True
    failures = []

    for f in forests:
        # Compute d(f)
        df = chain_differential(f)
        if not df:
            continue

        # Compute d(d(f)) = d^2(f)
        d2f = defaultdict(Fraction)
        for contracted, coeff in df.items():
            d_contracted = chain_differential(contracted)
            for cc, cc_coeff in d_contracted.items():
                d2f[cc] += coeff * cc_coeff

        # Check all coefficients are zero
        nonzero = {k: v for k, v in d2f.items() if v != Fraction(0)}
        if nonzero:
            all_pass = False
            failures.append(f)

    return {
        "n": n,
        "num_forests": len(forests),
        "d_squared_zero": all_pass,
        "num_failures": len(failures),
    }


# =========================================================================
# Depth filtration and genus spectral sequence E_1 page
# =========================================================================

def forests_by_depth(n: int) -> Dict[int, List[PlantedForest]]:
    """Partition planted forests at arity n by depth d.

    depth 1 = corollas (single-vertex trees)
    depth 2 = trees with one level of internal vertices
    etc.
    """
    forests = enumerate_planted_forests(n)
    by_depth = defaultdict(list)
    for f in forests:
        by_depth[f.depth].append(f)
    return dict(by_depth)


def e1_page(n: int, max_depth: int = 5) -> Dict[int, int]:
    """E_1 page of the genus spectral sequence at arity n.

    E_1^{d, n} = number of arity-n forests at depth d.

    d=1: corollas (always 1)
    d=2: trees where all internal vertices are children of root
    d=k: trees with maximum root-to-leaf path of length k
    """
    by_depth = forests_by_depth(n)
    return {d: len(forests) for d, forests in by_depth.items() if d <= max_depth}


def depth_differential(n: int) -> Dict[int, Dict[PlantedForest, Dict[PlantedForest, Fraction]]]:
    """Differential d_1 on the E_1 page: edge contraction grouped by depth.

    The differential maps depth d to depth d-1 (contracting an edge
    reduces the maximum path length).
    """
    forests = enumerate_planted_forests(n)
    by_depth = defaultdict(list)
    for f in forests:
        by_depth[f.depth].append(f)

    diff_by_depth = {}
    for d, d_forests in by_depth.items():
        diff_at_d = {}
        for f in d_forests:
            df = chain_differential(f)
            if df:
                diff_at_d[f] = df
        diff_by_depth[d] = diff_at_d

    return diff_by_depth


# =========================================================================
# Associahedron connection
# =========================================================================

def binary_forests(n: int) -> List[PlantedForest]:
    """All binary planted forests at arity n.

    A binary forest has every non-leaf vertex with exactly 2 children.
    The count equals the Catalan number C_{n-1}.
    """
    forests = enumerate_planted_forests(n)
    return [f for f in forests if f.is_binary()]


def catalan(n: int) -> int:
    """Catalan number C_n = binom(2n, n) / (n+1)."""
    if n < 0:
        return 0
    return comb(2 * n, n) // (n + 1)


def verify_binary_count(n: int) -> Dict:
    """Verify that binary forests at arity n = Catalan C_{n-1}."""
    bf = binary_forests(n)
    expected = catalan(n - 1)
    return {
        "n": n,
        "binary_count": len(bf),
        "catalan": expected,
        "match": len(bf) == expected,
    }


# =========================================================================
# Shadow tower connection
# =========================================================================

def shadow_coefficient(forest: PlantedForest) -> Fraction:
    """Combinatorial coefficient 1/|Aut(F)| for the forest F in a graph sum.

    The shadow at arity r is:
      Sh_r = Sum_{forests F with r leaves} (1/|Aut(F)|) * (vertex_weights) * (edge_propagators)

    This function returns just the combinatorial prefactor.
    """
    return Fraction(1, automorphism_order(forest))


def shadow_sum_coefficients(n: int) -> Fraction:
    """Sum of 1/|Aut(F)| over all planted forests at arity n.

    This is a basic consistency check: the sum should equal
    n^{n-1} / n! (by Cayley's formula divided by n! for the
    internal vertex relabeling quotient)... actually this needs
    more careful analysis.
    """
    forests = enumerate_planted_forests(n)
    return sum(Fraction(1, automorphism_order(f)) for f in forests)


def shadow_at_arity(
    n: int,
    family: str,
    kappa_val: Fraction = Fraction(1),
    alpha_val: Fraction = Fraction(0),
) -> Fraction:
    """Compute the shadow tower coefficient Sh_n for a given family.

    The shadow at arity n sums over all planted forests F with n leaves:
      Sh_n = Sum_F (1/|Aut(F)|) * prod_{v internal} (vertex weight) * prod_{e} (propagator)

    For the Gaussian class (Heisenberg):
      Only the corolla contributes (vertex weight = kappa for the corolla,
      all other forests have vertex weight = 0 because higher-valence
      vertices involve higher OPE poles that vanish for abelian algebras).

    For the Lie class (affine):
      Corolla + binary trees with 3-valent root contribute.
      3-valent vertex weight = alpha (cubic shadow parameter).

    For deeper classes: all forests contribute with appropriate vertex weights.

    This simplified version uses:
      vertex weight at valence k = alpha^{k-2} (the k-point OPE coefficient)
      propagator per edge = 1/kappa

    Parameters:
      n: arity
      family: 'gaussian', 'lie', 'contact', 'mixed'
      kappa_val: curvature
      alpha_val: cubic shadow parameter
    """
    if kappa_val == 0:
        return Fraction(0)

    forests = enumerate_planted_forests(n)
    total = Fraction(0)
    propagator = Fraction(1, 1) / kappa_val

    for f in forests:
        # Automorphism weight
        aut = automorphism_order(f)
        coeff = Fraction(1, aut)

        # Vertex weights
        vertex_weight = Fraction(1)
        for v in f.vertices:
            if v in f.leaf_set:
                continue
            k = len(f.children_of(v))  # number of children
            if k < 2:
                continue
            if family == 'gaussian' and k > 2:
                vertex_weight = Fraction(0)
                break
            if family == 'lie' and k > 3:
                vertex_weight = Fraction(0)
                break
            if k == 2:
                vertex_weight *= kappa_val
            elif k == 3:
                vertex_weight *= alpha_val
            else:
                # Higher valence: use alpha^{k-2} as a proxy
                vertex_weight *= alpha_val ** (k - 2)

        if vertex_weight == Fraction(0):
            continue

        # Edge propagator: each internal edge contributes 1/kappa
        n_int_edges = f.num_internal_edges
        edge_weight = propagator ** n_int_edges

        total += coeff * vertex_weight * edge_weight

    return total


# =========================================================================
# Summary statistics
# =========================================================================

def forest_statistics(n: int) -> Dict:
    """Comprehensive statistics for planted forests at arity n."""
    forests = enumerate_planted_forests(n)
    by_depth = forests_by_depth(n)
    bf = [f for f in forests if f.is_binary()]
    corollas = [f for f in forests if f.is_corolla()]

    depth_dist = {d: len(fs) for d, fs in sorted(by_depth.items())}
    aut_dist = Counter(automorphism_order(f) for f in forests)
    aut_sum = sum(Fraction(1, automorphism_order(f)) for f in forests)

    return {
        "n": n,
        "total_forests": len(forests),
        "expected_count": planted_forest_count_expected(n),
        "count_matches": len(forests) == planted_forest_count_expected(n),
        "binary_count": len(bf),
        "catalan": catalan(n - 1),
        "binary_matches_catalan": len(bf) == catalan(n - 1),
        "corolla_count": len(corollas),
        "depth_distribution": depth_dist,
        "automorphism_distribution": dict(aut_dist),
        "aut_reciprocal_sum": aut_sum,
    }
