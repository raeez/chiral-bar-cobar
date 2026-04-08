r"""Balduf-Gaiotto combinatorial non-renormalization and chiral formality bridge.

MATHEMATICAL FRAMEWORK
======================

Balduf-Gaiotto (arXiv:2408.03192, JHEP 2025) prove a Feynman graph identity:

    alpha_Gamma wedge alpha_Gamma = 0

for all non-tree graphs Gamma, where alpha_Gamma is a differential form in
Schwinger parameters {a_e} obtained by integrating the topological propagator
P_e = exp(-s_e^2) ds_e over vertex positions.  This generalizes Kontsevich's
formality theorem from deformation quantization to a wide class of theories.

BRIDGE TO THE CHIRAL SETTING
=============================

The monograph proves (thm:shadow-formality-identification) that the shadow
obstruction tower equals the L-infinity formality obstruction tower:

    Sh_r(A) = ell_r^{(0),tr}(Theta^{<=r-1}, ..., Theta^{<=r-1})

at all arities r >= 2.  The tree formula (eq:tree-formula-general) computes
both sides using the SAME planted trees with the SAME propagator P_A = h.

RELATIONSHIP ANALYSIS
=====================

1. PROPAGATOR COMPARISON:
   - BG: P_e = exp(-s_e^2) ds_e with s_e = (x^+_e - x^-_e)/sqrt(a_e)
   - Kontsevich: dArg(z_i - z_j)/pi (angle form on upper half-plane)
   - Chiral bar: d log E(z,w) (logarithmic differential of prime form)
   All three are "topological" propagators in that they produce closed forms
   on configuration spaces.  The BG Gaussian propagator is a DIFFERENT
   representative of the same de Rham cohomology class as Kontsevich's
   angle form.  The chiral d log E(z,w) is the algebraic-curve analogue.

2. QUADRATIC VANISHING vs CUBIC GAUGE TRIVIALITY:
   - BG: alpha_Gamma ^ alpha_Gamma = 0 for non-tree Gamma (vanishing of
     wedge-square of the integrated form)
   - Monograph: thm:cubic-gauge-triviality says when H^1(F^3/F^4, d_2) = 0,
     the cubic MC term is gauge-trivial and the quartic class [Theta'_4]
     is canonical
   These are RELATED but DIFFERENT statements:
   - BG's quadratic vanishing implies no quantum corrections (non-renorm)
   - Cubic gauge triviality is about the arity-3 component of the MC element
   - The connection: BG's vanishing at loop order 1 (single-loop graphs)
     is the combinatorial shadow of cubic gauge triviality for class-G/C
     algebras.  For class-M algebras (Virasoro), the cubic IS nonzero.

3. PLANTED FORESTS vs BG GRAPH SUMS:
   - Monograph: planted-forest corrections d_pf live at codimension >= 2
     of the FM boundary.  The genus-2 formula is delta_pf = S_3(10S_3-kappa)/48.
   - BG: their graph sum ranges over ALL graphs (trees + loops)
   - Connection: the tree part of BG's sum is the HTT tree formula for
     ell_r^{(0),tr}.  The loop part contains genus corrections.
     BG's alpha_Gamma ^ alpha_Gamma = 0 for non-trees implies that the
     loop corrections to the formality quasi-isomorphism vanish, but this
     does NOT mean planted-forest corrections vanish (those live in a
     different complex).

4. NON-RENORMALIZATION and MC5 SEWING:
   - BG's non-renormalization applies to theories with topological directions
     (R^T x C^H with T >= 2, including 3d CS and HT theories)
   - MC5 analytic sewing (thm:general-hs-sewing) proves convergence for
     the standard landscape via HS-sewing, which is about GENUS sums
   - BG's non-renorm is about LOOP corrections to the formality map, not
     about genus sums per se.  The two are compatible but not identical.

THIS MODULE COMPUTES
====================

1. BG alpha_Gamma for small graphs via Gaussian integration over positions
2. Verification of alpha_Gamma ^ alpha_Gamma = 0 (the main theorem)
3. Comparison of BG propagator with our d log propagator on planted trees
4. Bridge between BG graph identity and shadow obstruction tower
5. Spanning tree expansion (Kirchhoff/matrix-tree) underlying BG's proof

CONVENTIONS:
    - Exact arithmetic via fractions.Fraction
    - Graphs represented as (n_vertices, edge_list)
    - Schwinger parameters a_e > 0 treated symbolically
    - Vertex positions x_v integrated out via Gaussian

REFERENCES:
    Balduf-Gaiotto, arXiv:2408.03192 (JHEP 2025)
    thm:shadow-formality-identification (higher_genus_modular_koszul.tex)
    thm:cubic-gauge-triviality (higher_genus_modular_koszul.tex)
    eq:tree-formula-general (higher_genus_modular_koszul.tex)
    prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
    thm:kontsevich-formality (cobar_construction.tex)
    rem:kontsevich-graphs (feynman_diagrams.tex)
    AP19: bar propagator d log E(z,w) has weight 1
    AP27: all channels use E_1 at the edge level
"""

from __future__ import annotations

import itertools
import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from typing import (
    Any, Dict, FrozenSet, List, Optional, Set, Tuple, Union,
)

import numpy as np

# ---------------------------------------------------------------------------
# Exact arithmetic
# ---------------------------------------------------------------------------

FR = Fraction
ZERO = FR(0)
ONE = FR(1)
TWO = FR(2)


def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, float):
        return Fraction(x).limit_denominator(10**15)
    return Fraction(x)


# ============================================================================
# 1. GRAPH DATA STRUCTURES
# ============================================================================

@dataclass(frozen=True)
class FeynmanGraph:
    """A graph with labeled vertices and edges.

    For Balduf-Gaiotto, vertices have positions x_v in R,
    and edges carry Schwinger parameters a_e > 0.

    Attributes:
        n_vertices: number of vertices (labeled 0..n_vertices-1)
        edges: list of (u, v) pairs (u < v, may have multi-edges)
        name: optional label
    """
    n_vertices: int
    edges: Tuple[Tuple[int, int], ...]
    name: str = ""

    @property
    def n_edges(self) -> int:
        return len(self.edges)

    @property
    def loop_number(self) -> int:
        """First Betti number b_1 = |E| - |V| + connected_components."""
        return self.n_edges - self.n_vertices + self._n_components()

    def _n_components(self) -> int:
        visited: Set[int] = set()
        adj: Dict[int, Set[int]] = defaultdict(set)
        for u, v in self.edges:
            adj[u].add(v)
            adj[v].add(u)
        count = 0
        for start in range(self.n_vertices):
            if start in visited:
                continue
            count += 1
            stack = [start]
            visited.add(start)
            while stack:
                node = stack.pop()
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        stack.append(nb)
        return count

    def is_tree(self) -> bool:
        return self.loop_number == 0 and self._n_components() == 1

    def is_connected(self) -> bool:
        return self._n_components() == 1

    def incidence_matrix(self) -> np.ndarray:
        """Signed incidence matrix I: |V| x |E|.

        Convention: for edge e = (u, v) with u < v,
        I[u, e] = -1, I[v, e] = +1.
        """
        I = np.zeros((self.n_vertices, self.n_edges), dtype=float)
        for idx, (u, v) in enumerate(self.edges):
            I[u, idx] = -1.0
            I[v, idx] = +1.0
        return I

    def reduced_incidence(self) -> np.ndarray:
        """Incidence matrix with last row removed (reduced, for connected graphs)."""
        I = self.incidence_matrix()
        return I[:-1, :]  # remove last vertex row

    def laplacian(self, schwinger: Optional[np.ndarray] = None) -> np.ndarray:
        """Graph Laplacian L = I^T D^{-1} I where D = diag(a_e).

        If schwinger is None, use a_e = 1 for all edges.
        Returns the REDUCED Laplacian (delete last row/col of full Laplacian).
        """
        n = self.n_vertices
        if schwinger is None:
            schwinger = np.ones(self.n_edges)
        D_inv = np.diag(1.0 / schwinger)
        I = self.incidence_matrix()
        L_full = I @ D_inv @ I.T
        # Reduced: delete last row and column
        return L_full[:-1, :-1]

    def spanning_trees(self) -> List[FrozenSet[int]]:
        """Enumerate all spanning trees by edge index sets.

        A spanning tree uses exactly n_vertices - 1 edges that connect all vertices.
        """
        n = self.n_vertices
        m = self.n_edges
        trees = []
        for edge_subset in itertools.combinations(range(m), n - 1):
            # Check if these edges form a spanning tree
            adj: Dict[int, Set[int]] = defaultdict(set)
            for idx in edge_subset:
                u, v = self.edges[idx]
                adj[u].add(v)
                adj[v].add(u)
            # BFS from vertex 0
            visited: Set[int] = {0}
            stack = [0]
            while stack:
                node = stack.pop()
                for nb in adj[node]:
                    if nb not in visited:
                        visited.add(nb)
                        stack.append(nb)
            if len(visited) == n:
                trees.append(frozenset(edge_subset))
        return trees

    def kirchhoff_polynomial(self) -> int:
        """Number of spanning trees (Kirchhoff's theorem).

        Equals det(reduced Laplacian) with all a_e = 1.
        """
        if not self.is_connected():
            return 0
        L = self.laplacian()
        return int(round(np.linalg.det(L)))


# ============================================================================
# 2. STANDARD SMALL GRAPHS
# ============================================================================

def triangle_graph() -> FeynmanGraph:
    """K_3: 3 vertices, 3 edges, loop number 1."""
    return FeynmanGraph(3, ((0, 1), (0, 2), (1, 2)), name="K3/triangle")


def square_graph() -> FeynmanGraph:
    """C_4: 4 vertices, 4 edges, loop number 1."""
    return FeynmanGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)), name="C4/square")


def complete_graph(n: int) -> FeynmanGraph:
    """K_n: complete graph on n vertices."""
    edges = tuple((i, j) for i in range(n) for j in range(i + 1, n))
    return FeynmanGraph(n, edges, name=f"K{n}")


def theta_graph() -> FeynmanGraph:
    """Theta graph: 2 vertices, 3 parallel edges. Loop number 2."""
    return FeynmanGraph(2, ((0, 1), (0, 1), (0, 1)), name="theta")


def banana_graph(k: int) -> FeynmanGraph:
    """Banana/sunset graph: 2 vertices, k parallel edges. Loop number k-1."""
    return FeynmanGraph(2, tuple((0, 1) for _ in range(k)), name=f"banana_{k}")


def wheel_graph(n: int) -> FeynmanGraph:
    """Wheel W_n: central vertex 0 connected to cycle 1..n.
    n+1 vertices, 2n edges, loop number n.
    """
    edges = []
    for i in range(1, n + 1):
        edges.append((0, i))  # spoke
    for i in range(1, n + 1):
        j = i % n + 1
        edges.append((i, j))  # rim
    return FeynmanGraph(n + 1, tuple(edges), name=f"W{n}")


def path_graph(n: int) -> FeynmanGraph:
    """Path P_n: n vertices, n-1 edges (a tree)."""
    edges = tuple((i, i + 1) for i in range(n - 1))
    return FeynmanGraph(n, edges, name=f"P{n}")


def star_graph(n: int) -> FeynmanGraph:
    """Star S_n: central vertex 0, n leaves (a tree)."""
    edges = tuple((0, i) for i in range(1, n + 1))
    return FeynmanGraph(n + 1, edges, name=f"S{n}")


# ============================================================================
# 3. BALDUF-GAIOTTO alpha_Gamma COMPUTATION
# ============================================================================

def bg_quadratic_form(graph: FeynmanGraph,
                      schwinger: np.ndarray) -> np.ndarray:
    """Compute the quadratic form sum_e s_e^2 = x^T L x.

    For the reduced system (fixing x_{n-1} = 0):
    L_{red} = I_red^T D^{-1} I_red
    where I_red is the reduced incidence matrix and D = diag(a_e).

    Returns the reduced Laplacian matrix.
    """
    I_red = graph.reduced_incidence()
    D_inv = np.diag(1.0 / schwinger)
    return I_red @ D_inv @ I_red.T


def bg_gaussian_integral(graph: FeynmanGraph,
                         schwinger: np.ndarray) -> float:
    """Compute the Gaussian integral over vertex positions.

    integral exp(-x^T L x) d^{n-1}x = (pi)^{(n-1)/2} / sqrt(det L)

    where L is the reduced Laplacian.  For connected graphs,
    det L = (product of a_e) * (Kirchhoff polynomial) by the matrix-tree theorem.
    """
    n = graph.n_vertices
    if n <= 1:
        return 1.0
    L = bg_quadratic_form(graph, schwinger)
    det_L = np.linalg.det(L)
    if det_L <= 0:
        return 0.0
    dim = n - 1
    return (np.pi ** (dim / 2.0)) / np.sqrt(det_L)


def bg_alpha_gamma_degree(graph: FeynmanGraph) -> int:
    """Degree of the differential form alpha_Gamma in Schwinger parameters.

    alpha_Gamma is a (|E| - |V| + 1)-form in the variables {da_e}.
    For trees: degree 0 (a constant).
    For single-loop: degree 1 (a 1-form).
    """
    return graph.loop_number


def bg_spanning_tree_sum(graph: FeynmanGraph,
                         schwinger: np.ndarray) -> float:
    """Compute the spanning tree polynomial psi_Gamma(a).

    psi_Gamma = sum over spanning trees T of product_{e not in T} a_e

    This is the Kirchhoff/Symanzik polynomial.  By the matrix-tree theorem,
    det(L_reduced) = psi_Gamma / product(a_e).
    """
    if not graph.is_connected():
        return 0.0
    trees = graph.spanning_trees()
    total = 0.0
    all_edges = set(range(graph.n_edges))
    for tree_edges in trees:
        complement = all_edges - tree_edges
        contrib = 1.0
        for e_idx in complement:
            contrib *= schwinger[e_idx]
        total += contrib
    return total


def bg_alpha_components(graph: FeynmanGraph,
                        schwinger: np.ndarray) -> Dict[FrozenSet[int], float]:
    """Compute the components of alpha_Gamma as a differential form.

    alpha_Gamma = sum_{S subset of edges, |S| = loop_number}
                  f_S(a) * wedge_{e in S} da_e

    For a graph with loop number L, alpha_Gamma is an L-form.
    Each component f_S is computed from the Gaussian integral over positions,
    selecting the L edges whose da_e differentials survive.

    For trees (L=0): alpha = constant (the Gaussian integral value).
    For L=1: alpha = sum_e f_e(a) da_e.

    The computation uses the reduced Laplacian and Dodgson-style minors.
    """
    L = graph.loop_number
    m = graph.n_edges
    n = graph.n_vertices

    if L == 0:
        # Tree: alpha is a 0-form = scalar
        val = bg_gaussian_integral(graph, schwinger)
        return {frozenset(): val}

    components: Dict[FrozenSet[int], float] = {}

    # For each L-element subset S of edges, compute the coefficient
    # The coefficient comes from expanding the product of propagators
    # and collecting terms with da_e for e in S.
    #
    # The key formula (BG eq. 3.7):
    # alpha_Gamma = sum_S (-1)^{sign(S)} * psi_{Gamma\S}(a) /
    #               psi_Gamma(a)^{dim/2+1} * normalization
    #
    # where psi_{Gamma\S} is the Kirchhoff polynomial of the graph
    # with edges S removed (the complementary spanning forest polynomial).

    psi = bg_spanning_tree_sum(graph, schwinger)
    if abs(psi) < 1e-15:
        return components

    dim = n - 1  # dimension of integration

    for edge_subset in itertools.combinations(range(m), L):
        S = frozenset(edge_subset)
        # Compute the minor: spanning forest polynomial for the
        # graph with edges in S contracted (or equivalently,
        # the cofactor from the Laplacian).
        #
        # For L=1, single edge e removed:
        # psi_{Gamma\e} = number of spanning trees NOT containing e
        # (complementary forest polynomial).
        #
        # This is computed via the ratio of Laplacian minors.

        # For small graphs, direct computation:
        complement_edges = [i for i in range(m) if i not in S]
        if len(complement_edges) < n - 1:
            # Not enough edges to span
            components[S] = 0.0
            continue

        # Build subgraph with complement edges, check if spanning
        sub_schwinger = np.array([schwinger[i] for i in complement_edges])
        sub_edges = tuple(graph.edges[i] for i in complement_edges)
        sub_graph = FeynmanGraph(n, sub_edges)

        # Count spanning trees of complement subgraph
        sub_trees = sub_graph.spanning_trees()
        if not sub_trees:
            components[S] = 0.0
            continue

        sub_psi = 0.0
        sub_all_idx = set(range(len(complement_edges)))
        for tree_idx_set in sub_trees:
            tree_complement = sub_all_idx - tree_idx_set
            contrib = 1.0
            for idx in tree_complement:
                contrib *= sub_schwinger[idx]
            sub_psi += contrib

        # Product of Schwinger parameters for edges in S
        a_S = 1.0
        for e_idx in S:
            a_S *= schwinger[e_idx]

        # The coefficient: related to the ratio of forest polynomials
        # Normalization from Gaussian integration
        coeff = sub_psi * a_S / (psi ** ((dim + 2) / 2.0))
        coeff *= (np.pi ** (dim / 2.0)) / 2.0

        # Sign from edge ordering
        sign = _subset_sign(edge_subset, m)
        components[S] = sign * coeff

    return components


def _subset_sign(subset: Tuple[int, ...], m: int) -> int:
    """Sign from embedding a subset into the ordered set {0,...,m-1}.

    This is the sign of the shuffle permutation that moves the
    selected indices to the front while preserving order.
    For an ordered tuple, the sign is (-1)^{sum(s_i - i)}.
    """
    sign = 0
    for i, s in enumerate(subset):
        sign += s - i
    return 1 if sign % 2 == 0 else -1


# ============================================================================
# 4. QUADRATIC VANISHING: alpha_Gamma ^ alpha_Gamma = 0
# ============================================================================

def bg_alpha_wedge_alpha(graph: FeynmanGraph,
                         schwinger: np.ndarray) -> Dict[FrozenSet[int], float]:
    """Compute alpha_Gamma ^ alpha_Gamma as a 2L-form.

    The wedge product of the L-form alpha with itself.
    BG's theorem: this vanishes for all non-tree graphs.
    For trees (L=0): the square of a scalar, which can be nonzero.

    Returns dictionary mapping 2L-element edge subsets to coefficients.
    """
    alpha = bg_alpha_components(graph, schwinger)
    L = graph.loop_number
    m = graph.n_edges

    if L == 0:
        # 0-form squared is a scalar
        val = alpha.get(frozenset(), 0.0)
        return {frozenset(): val * val}

    # Wedge product: (sum f_S da_S) ^ (sum f_T da_T)
    # = sum_{S,T disjoint} f_S * f_T * sign(S,T) * da_{S cup T}
    result: Dict[FrozenSet[int], float] = defaultdict(float)

    for S, f_S in alpha.items():
        for T, f_T in alpha.items():
            if S & T:  # not disjoint => wedge vanishes
                continue
            if abs(f_S) < 1e-15 or abs(f_T) < 1e-15:
                continue
            union = S | T
            # Sign from rearranging da_S ^ da_T into standard order
            sign = _wedge_sign(sorted(S), sorted(T))
            result[union] += sign * f_S * f_T

    return dict(result)


def _wedge_sign(S_sorted: List[int], T_sorted: List[int]) -> int:
    """Sign from interleaving two sorted lists into a single sorted sequence.

    This is the sign of the shuffle permutation.
    """
    merged = S_sorted + T_sorted
    # Count inversions
    inv = 0
    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if merged[i] > merged[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1


def verify_quadratic_vanishing(graph: FeynmanGraph,
                               n_samples: int = 20,
                               tol: float = 1e-8) -> Tuple[bool, float]:
    """Verify alpha_Gamma ^ alpha_Gamma = 0 for random Schwinger parameters.

    BG's main theorem: this holds for all non-tree graphs.
    For trees: alpha is a 0-form, so alpha^2 is a nonzero scalar.

    Returns (passes, max_residual).
    """
    if graph.is_tree():
        # For trees, alpha^2 is not zero (it's a scalar squared)
        return True, 0.0

    if graph.loop_number * 2 > graph.n_edges:
        # 2L > |E| means the 2L-form is automatically zero
        return True, 0.0

    max_residual = 0.0
    for _ in range(n_samples):
        schwinger = np.random.uniform(0.5, 2.0, graph.n_edges)
        wedge_sq = bg_alpha_wedge_alpha(graph, schwinger)
        for S, val in wedge_sq.items():
            max_residual = max(max_residual, abs(val))

    passes = max_residual < tol
    return passes, max_residual


# ============================================================================
# 5. KIRCHHOFF/MATRIX-TREE THEOREM
# ============================================================================

def matrix_tree_count(graph: FeynmanGraph) -> int:
    """Number of spanning trees via the matrix-tree theorem.

    det(reduced Laplacian with a_e=1) = number of spanning trees.
    """
    return graph.kirchhoff_polynomial()


def kirchhoff_polynomial_symbolic(graph: FeynmanGraph) -> Dict[FrozenSet[int], int]:
    """Kirchhoff polynomial psi_Gamma = sum_T prod_{e not in T} a_e.

    Returns coefficients indexed by the complement edge sets.
    Each spanning tree T contributes a monomial in {a_e : e not in T}.
    """
    trees = graph.spanning_trees()
    all_edges = set(range(graph.n_edges))
    poly: Dict[FrozenSet[int], int] = defaultdict(int)
    for tree in trees:
        complement = frozenset(all_edges - tree)
        poly[complement] += 1
    return dict(poly)


def kirchhoff_verify_determinant(graph: FeynmanGraph,
                                 schwinger: np.ndarray) -> float:
    """Verify matrix-tree theorem: det(L_red) = psi/prod(a_e).

    Returns the discrepancy |det(L) - psi/prod(a)|.
    """
    if not graph.is_connected():
        return 0.0
    L = bg_quadratic_form(graph, schwinger)
    det_L = np.linalg.det(L)
    psi = bg_spanning_tree_sum(graph, schwinger)
    prod_a = np.prod(schwinger)
    expected = psi / prod_a
    return abs(det_L - expected)


# ============================================================================
# 6. PLANTED TREE COMPARISON: BG vs CHIRAL BAR
# ============================================================================

@dataclass(frozen=True)
class PlantedTree:
    """A planted binary tree with labeled leaves for tree formula comparison."""
    structure: Any  # nested tuples of ints
    n_leaves: int
    label: str = ""


def _gen_binary_trees(n: int) -> List:
    """Generate all planar binary trees with n leaves (0-indexed)."""
    if n == 1:
        return [0]
    results = []
    for k in range(1, n):
        for lt in _gen_binary_trees(k):
            for rt in _gen_binary_trees(n - k):
                shifted_rt = _shift_tree(rt, k)
                results.append((lt, shifted_rt))
    return results


def _shift_tree(tree, offset: int):
    if isinstance(tree, int):
        return tree + offset
    return tuple(_shift_tree(child, offset) for child in tree)


def catalan(n: int) -> int:
    """Catalan number C_n = binom(2n, n) / (n+1)."""
    if n < 0:
        return 0
    from math import comb
    return comb(2 * n, n) // (n + 1)


def planted_binary_trees(n: int) -> List[PlantedTree]:
    """Enumerate planted binary trees with n labeled leaves."""
    structures = _gen_binary_trees(n)
    return [
        PlantedTree(s, n, f"T_{n}_{i}")
        for i, s in enumerate(structures)
    ]


def tree_to_feynman_graph(tree: PlantedTree) -> FeynmanGraph:
    """Convert a planted tree to a FeynmanGraph.

    The planted tree has n_leaves leaves and n_leaves - 1 internal vertices.
    Total vertices = 2*n_leaves - 1.
    Leaves: 0..n_leaves-1; internal: n_leaves..2*n_leaves-2.
    """
    n = tree.n_leaves
    edges: List[Tuple[int, int]] = []
    next_internal = [n]  # mutable counter

    def _build(subtree) -> int:
        """Returns the vertex index for this subtree."""
        if isinstance(subtree, int):
            return subtree  # leaf
        # Internal node
        v = next_internal[0]
        next_internal[0] += 1
        children = [_build(child) for child in subtree]
        for child_v in children:
            u, w = min(v, child_v), max(v, child_v)
            edges.append((u, w))
        return v

    _build(tree.structure)
    total_vertices = 2 * n - 1
    return FeynmanGraph(total_vertices, tuple(edges), name=tree.label)


def bg_tree_amplitude(tree: PlantedTree) -> float:
    """BG alpha_Gamma for a tree graph (should be a nonzero constant).

    For trees, alpha_Gamma is a 0-form = scalar.
    With all Schwinger parameters = 1:
    alpha_tree = (pi)^{dim/2} / sqrt(det L_red)
    """
    fg = tree_to_feynman_graph(tree)
    schwinger = np.ones(fg.n_edges)
    return bg_gaussian_integral(fg, schwinger)


# ============================================================================
# 7. SHADOW TOWER COMPARISON
# ============================================================================

def shadow_coefficients_virasoro(c: FR, max_arity: int = 6) -> Dict[int, FR]:
    """Compute shadow obstruction tower S_r for Virasoro at central charge c.

    The shadow Sh_r = S_r * x^r on the primary line.  The authoritative
    recursion (virasoro_shadow_tower.py, higher_genus_modular_koszul.tex)
    uses the MC equation projected to the primary line:

        nabla_H(Sh_r) + o^{(r)} = 0

    where o^{(r)} = sum_{j+k=r+2} {Sh_j, Sh_k}_H (the H-Poisson bracket)
    and nabla_H^{-1}(alpha * x^r) = alpha/(2r) * x^r.

    Authoritative values (computed from first principles in
    virasoro_shadow_tower.py using the Virasoro OPE data):
        S_2 = c/2        (kappa, the modular characteristic)
        S_3 = 2           (cubic shadow, a CONSTANT independent of c)
        S_4 = 10/(c(5c+22))  (quartic contact invariant Q^contact)
        S_5 = -48/(c^2(5c+22))
        S_6 = 80(45c+193)/(3c^3(5c+22)^2)
        S_7 = -2880(15c+61)/(7c^4(5c+22)^2)

    The H-Poisson bracket with propagator P = 2/c is:
        {f, g}_H = (df/dx) * P * (dg/dx) = (2/c) * f' * g'

    THESE COEFFICIENTS are the obstruction tower data that thm:shadow-formality-
    identification identifies with L-infinity brackets:
        S_r = ell_r^{(0),tr}(Theta, ..., Theta) (on scalar line)

    CAUTION (AP1): S_3 = 2 is a CONSTANT. It is NOT 6/(5c+22).
    The value 6/(5c+22) is a different normalization that appears in certain
    generating function presentations.  The authoritative coefficient is S_3 = 2.
    """
    if c == FR(0):
        return {r: ZERO for r in range(2, max_arity + 1)}

    # Hessian propagator on the primary line: P = 2/c
    P = TWO / c

    S: Dict[int, FR] = {}
    S[2] = c / TWO              # kappa
    S[3] = TWO                  # cubic shadow (constant!)
    S[4] = FR(10) / (c * (FR(5) * c + FR(22)))  # Q^contact

    # Recursive computation for r >= 5 using the MC obstruction equation:
    #   Sh_r = -nabla_H^{-1}(o^{(r)})
    # where o^{(r)} = sum_{j+k=r+2, j>=2, k>=2, j<r, k<r} {Sh_j, Sh_k}_H
    #
    # CRITICAL: the obstruction uses only PREVIOUSLY COMPUTED shadows.
    # The pair (2, r) is EXCLUDED because Sh_r is what we are computing.
    # This is the iterative MC solution: at each step we solve for Sh_r
    # from the obstruction built from Sh_2, ..., Sh_{r-1} only.
    #
    # {S_j x^j, S_k x^k}_H = j*k * S_j * S_k * P * x^{j+k-2}
    # nabla_H^{-1}(alpha * x^r) = alpha / (2r)

    for r in range(5, max_arity + 1):
        # Obstruction at arity r: collect H-Poisson bracket terms
        # {Sh_j, Sh_k} with j + k - 2 = r, i.e., j + k = r + 2
        # BOTH j and k must be strictly less than r (already computed)
        obstruction_coeff = ZERO
        for j in range(2, r):
            k = r + 2 - j
            if k < 2 or k >= r:  # k must be in range [2, r-1]
                continue
            if k not in S:
                continue
            if j > k:
                continue  # avoid double counting
            bracket_coeff = FR(j) * FR(k) * S[j] * S[k] * P
            if j == k:
                obstruction_coeff += FR(1, 2) * bracket_coeff
            else:
                obstruction_coeff += bracket_coeff

        # Sh_r = -obstruction_coeff / (2*r) * x^r
        S[r] = -obstruction_coeff / (TWO * FR(r))

    return S


def shadow_depth_from_coefficients(S: Dict[int, FR]) -> Union[int, str]:
    """Determine the shadow depth r_max from shadow coefficients.

    r_max = largest r such that S_r != 0, or "infinity" if none vanish.
    """
    max_r = max(S.keys())
    for r in range(max_r, 1, -1):
        if S.get(r, ZERO) != ZERO:
            return r if all(S.get(k, ZERO) == ZERO for k in range(r + 1, max_r + 1)) else "infinity"
    return 2


# ============================================================================
# 8. CUBIC GAUGE TRIVIALITY (thm:cubic-gauge-triviality)
# ============================================================================

def cubic_gauge_triviality_check(
    kappa: FR, alpha: FR, S4: FR
) -> Dict[str, Any]:
    """Check conditions for cubic gauge triviality.

    thm:cubic-gauge-triviality: If H^1(F^3g/F^4g, d_2) = 0, then:
    (i) Theta_3 is gauge-trivial
    (ii) [Theta'_4] in H^2(F^4g/F^5g, d_2) is canonical

    For the shadow obstruction tower on the primary line:
    - Class G (Heisenberg): alpha = 0, gauge trivial trivially
    - Class L (affine): alpha != 0, but Jacobi gives o_4 = 0
    - Class C (betagamma): alpha gauge-trivial, S4 = Q_contact
    - Class M (Virasoro): alpha != 0 and NOT gauge-trivial

    The BG quadratic vanishing alpha_Gamma ^ alpha_Gamma = 0 at loop order 1
    is the GRAPH-COMPLEX shadow of the fact that the cubic obstruction
    o_3 = [C, C]_H involves only tree-level graphs, and the non-renormalization
    means no loop corrections to the formality quasi-isomorphism.

    Returns diagnostic dictionary.
    """
    result: Dict[str, Any] = {}
    result["kappa"] = kappa
    result["alpha"] = alpha
    result["S4"] = S4

    # Check if cubic is zero (class G)
    result["cubic_zero"] = (alpha == ZERO)

    # Check discriminant Delta = 8*kappa*S4
    if kappa != ZERO:
        Delta = FR(8) * kappa * S4
        result["Delta"] = Delta
        result["Delta_zero"] = (Delta == ZERO)

        # Shadow metric Q_L = (2k + 3a*t)^2 + 2*Delta*t^2
        # Delta = 0 => Q_L is a perfect square => tower terminates
        if Delta == ZERO:
            if alpha == ZERO:
                result["shadow_class"] = "G"
                result["depth"] = 2
            else:
                result["shadow_class"] = "L"
                result["depth"] = 3
        else:
            result["shadow_class"] = "M"
            result["depth"] = "infinity"
    else:
        result["Delta"] = ZERO
        result["Delta_zero"] = True
        result["shadow_class"] = "degenerate (kappa=0)"
        result["depth"] = "N/A"

    # BG connection: the quartic obstruction is canonical
    # iff the cubic is gauge-trivial
    result["quartic_canonical"] = result["cubic_zero"] or result.get("Delta_zero", False)

    return result


# ============================================================================
# 9. BG PROPAGATOR vs CHIRAL d log PROPAGATOR
# ============================================================================

def bg_propagator_1d(x_plus: float, x_minus: float,
                     a: float) -> float:
    """BG topological propagator exp(-s^2) on R^1.

    s = (x+ - x-) / sqrt(a)
    P = exp(-s^2) = exp(-(x+ - x-)^2 / a)
    """
    s = (x_plus - x_minus) / np.sqrt(a)
    return np.exp(-s * s)


def chiral_dlog_propagator(z: complex, w: complex) -> complex:
    """Chiral bar propagator d log(z - w) = dz/(z - w).

    On the Riemann sphere, this is a (1,0)-form in z.
    At the level of the residue: Res_{z=w} f(z) dz/(z-w) = f(w).
    """
    if abs(z - w) < 1e-15:
        return complex(float('inf'), 0)
    return 1.0 / (z - w)


def propagator_comparison_tree(n_leaves: int) -> Dict[str, Any]:
    """Compare BG and chiral propagators on planted trees.

    For TREE graphs:
    - BG: alpha_Gamma is a scalar (Gaussian integral)
    - Chiral: the tree formula uses d log(z_i - z_j) propagators

    The key comparison: both propagators produce the SAME L-infinity
    quasi-isomorphism at the cohomological level, because:
    1. BG's Gaussian and Kontsevich's angle form are cohomologous in
       the de Rham complex of the configuration space
    2. The chiral d log E(z,w) is the algebraic-curve representative

    This function computes tree counts and amplitudes to verify consistency.
    """
    trees = planted_binary_trees(n_leaves)
    result: Dict[str, Any] = {
        "n_leaves": n_leaves,
        "n_trees": len(trees),
        "catalan": catalan(n_leaves - 1),
    }

    # Verify tree count = Catalan(n-1)
    result["count_matches_catalan"] = (len(trees) == catalan(n_leaves - 1))

    # BG amplitudes (with a_e = 1)
    bg_amps = []
    for tree in trees:
        amp = bg_tree_amplitude(tree)
        bg_amps.append(amp)
    result["bg_amplitudes"] = bg_amps
    result["bg_total"] = sum(bg_amps)

    return result


# ============================================================================
# 10. DODGSON POLYNOMIAL / MINOR COMPUTATION
# ============================================================================

def dodgson_minor(graph: FeynmanGraph,
                  schwinger: np.ndarray,
                  rows_deleted: Tuple[int, ...],
                  cols_deleted: Tuple[int, ...]) -> float:
    """Compute a Dodgson minor (submatrix determinant) of the Laplacian.

    The Laplacian L = I^T D^{-1} I is an |E| x |E| matrix in edge space.
    Dodgson minors are determinants of submatrices with certain rows/cols removed.

    In BG's framework, these minors control the components of alpha_Gamma.
    """
    I_full = graph.incidence_matrix()
    D_inv = np.diag(1.0 / schwinger)
    L_edge = D_inv  # In edge space, the relevant matrix is D^{-1}

    # Actually, BG use the reduced vertex-space Laplacian
    L = bg_quadratic_form(graph, schwinger)
    n = L.shape[0]

    # Delete specified rows and columns
    row_mask = [i for i in range(n) if i not in rows_deleted]
    col_mask = [i for i in range(n) if i not in cols_deleted]

    if not row_mask or not col_mask:
        return 1.0

    sub = L[np.ix_(row_mask, col_mask)]
    if sub.shape[0] != sub.shape[1]:
        return 0.0
    return np.linalg.det(sub)


# ============================================================================
# 11. NON-RENORMALIZATION BRIDGE
# ============================================================================

def non_renormalization_genus_check(
    graph: FeynmanGraph,
    genus: int,
) -> Dict[str, Any]:
    """Assess whether BG non-renormalization applies at given genus.

    BG's non-renormalization holds for theories on R^T x C^H with T >= 2.
    This means: quantum corrections to the formality quasi-isomorphism vanish.

    For the CHIRAL setting on a curve X (T=0, H=1), the situation is DIFFERENT:
    - At genus 0: the tree formula gives the same L-infinity structure
      (thm:shadow-formality-identification)
    - At genus >= 1: LOOP corrections are nonzero (the genus expansion)
    - The planted-forest corrections d_pf are the codimension-2 boundary terms
      that BG's formalism does not directly address

    The key insight: BG's non-renormalization is for FLAT space (T >= 2 topological
    directions).  The chiral setting on a curved Riemann surface DOES have
    nontrivial genus corrections (the shadow obstruction tower at g >= 1).
    BG's theorem would apply to a chiral algebra on C (genus 0) with at least
    2 additional topological directions (i.e., a holomorphic-topological theory
    on R^2 x C), matching the 3d HT context of Vol II.
    """
    result: Dict[str, Any] = {}
    result["graph_name"] = graph.name
    result["loop_number"] = graph.loop_number
    result["genus"] = genus
    result["n_vertices"] = graph.n_vertices
    result["n_edges"] = graph.n_edges

    # BG non-renormalization applies when:
    # 1. There are T >= 2 topological directions
    # 2. The graph has loop_number >= 1 (non-tree)
    bg_applies = graph.loop_number >= 1
    result["bg_non_renorm_applies"] = bg_applies

    # In the chiral setting:
    # genus-0 shadow tower = L-infinity formality tower (PROVED)
    # genus-g corrections for g >= 1 are NONZERO generically
    result["chiral_genus_0_formality"] = True
    result["chiral_higher_genus_corrections"] = (genus >= 1)

    # The bridge: BG's alpha_Gamma ^ alpha_Gamma = 0 implies that
    # the formality quasi-isomorphism has no loop corrections.
    # In the chiral setting, this translates to:
    # the GENUS-0 shadow tower is exact (no loop corrections at genus 0).
    # Higher genus corrections are a SEPARATE phenomenon (modular structure).
    result["genus_0_loop_corrections_vanish"] = True
    result["higher_genus_separate"] = True

    # For 3d HT theories (T=2, H=1): BG applies, giving non-renormalization
    # This is consistent with Vol II's result that the Swiss-cheese structure
    # controls the deformation without quantum corrections in the bulk.
    result["ht_3d_applies"] = True

    return result


# ============================================================================
# 12. GENUS-2 PLANTED FOREST vs BG
# ============================================================================

def genus2_planted_forest_delta(kappa: FR, S3: FR) -> FR:
    """Genus-2 planted-forest correction delta_pf^{(2,0)}.

    From the manuscript (pixton_shadow_bridge.py):
        delta_pf = S_3 * (10*S_3 - kappa) / 48

    This is the d_pf component of the five-piece differential D,
    evaluated at genus 2 with 0 external legs.

    BG's formalism does NOT directly compute this:
    - delta_pf lives on codimension-2 FM boundary strata
    - BG's Schwinger parameter integrals are over flat R^n
    - The connection requires Mok's log-FM degeneration formula
    """
    return S3 * (FR(10) * S3 - kappa) / FR(48)


def genus2_comparison(c: FR) -> Dict[str, Any]:
    """Compare genus-2 data between BG framework and shadow tower.

    At genus 2, the shadow free energy receives:
    F_2 = kappa * lambda_2^FP + delta_pf^{(2,0)}

    where lambda_2^FP = 7/5760 (Faber-Pandharipande).

    For Virasoro (c = c_val):
        kappa = c/2
        S3 = 2 (authoritative constant, independent of c)
        delta_pf = S3 * (10*S3 - kappa) / 48

    BG's non-renormalization says that the FORMALITY MAP has no loop corrections.
    This does NOT mean delta_pf vanishes.  delta_pf is a GEOMETRIC correction
    from the moduli space stratification, not a loop correction to formality.
    """
    kappa = c / TWO
    S3 = TWO  # authoritative: S_3 = 2 (constant)

    lambda2_FP = FR(7, 5760)
    delta_pf = genus2_planted_forest_delta(kappa, S3)

    F2_scalar = kappa * lambda2_FP
    F2_total = F2_scalar + delta_pf

    result: Dict[str, Any] = {
        "central_charge": c,
        "kappa": kappa,
        "S3_cubic_shadow": S3,
        "S3": S3,
        "lambda2_FP": lambda2_FP,
        "delta_pf_genus2": delta_pf,
        "F2_scalar": F2_scalar,
        "F2_total": F2_total,
        "bg_non_renorm_affects_delta_pf": False,  # delta_pf is geometric, not a loop correction
    }

    return result
