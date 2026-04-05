r"""Ihara zeta function of the bar graph complex and spectral analysis.

The bar construction B(A) has an associated graph complex whose vertices at genus g
are the stable graphs Gamma of type (g, n).  The Ihara zeta function of a finite
graph G is

    zeta_G(u) = prod_{[p]} (1 - u^{|p|})^{-1}

where the product is over equivalence classes of primitive (backtrackless, tailless)
closed paths [p] of length |p|.

HASHIMOTO-BASS DETERMINANT FORMULA (three-term, for multigraphs with self-loops):

For a finite connected graph G = (V, E) (possibly with self-loops and multi-edges),
define the oriented edge set E_or with 2|E| oriented edges (each undirected edge gives
two orientations; each self-loop also gives two orientations). The Hashimoto (edge
adjacency) matrix T is the |E_or| x |E_or| matrix with

    T_{e, f} = 1  if terminal(e) = origin(f) and f != bar(e)

where bar(e) is the reverse of e.  Then:

    zeta_G(u)^{-1} = det(I - u * T)

The Bass three-term determinant identity gives (for simple graphs without self-loops):

    det(I - u * T) = (1 - u^2)^{r-1} * det(I - u*A + u^2*(D - I))

where A is the adjacency matrix, D = diag(deg(v)), and r = |E| - |V| + 1 is the
cyclomatic number.  For MULTIGRAPHS with self-loops, the three-term formula needs
modification: A_{ij} counts the number of edges between i and j (including self-loops
counted twice on the diagonal), and D_{ii} = sum_j A_{ij} = degree including 2 per
self-loop.

CAUTION: For stable graphs, self-loops are ubiquitous (e.g., the genus-1 nodal curve
is a genus-0 vertex with one self-loop).  The adjacency matrix for multigraphs with
self-loops is:

    A_{ii} = 2 * (number of self-loops at i)
    A_{ij} = number of edges between i and j,  i != j

and the degree D_{ii} = val(i) where val counts each self-loop twice and each
non-self-loop edge once per endpoint.

BAR GRAPH ZETA:

    Z^{bar}_g(u) = sum_Gamma |Aut(Gamma)|^{-1} * zeta_Gamma(u)

is the automorphism-weighted sum of Ihara zeta functions over all stable graphs
at genus g (n = 0 for vacuum amplitudes).

TOTAL BAR ZETA:

    Z^{bar}(u, q) = sum_g Z^{bar}_g(u) * q^g

is the generating function in the genus variable.

RAMANUJAN PROPERTY: A (q+1)-regular graph is Ramanujan if every nontrivial
eigenvalue lambda of its adjacency matrix satisfies |lambda| <= 2*sqrt(q).
For non-regular graphs, the analog is that the spectral radius of A restricted
to the orthogonal complement of the constant eigenspace should be bounded by
2*sqrt(d_max - 1) where d_max is the maximum degree.

PLANTED FOREST IHARA: The planted-forest subcomplex consists of graphs with
at least one genus-0 vertex of valence >= 3 (carrying higher L_infinity operations).
The planted-forest Ihara zeta restricts the graph sum to this subcomplex.

References:
  - Ihara, "On discrete subgroups of the two by two projective linear group over
    p-adic fields" (1966)
  - Bass, "The Ihara-Selberg zeta function of a tree lattice" (1992)
  - Hashimoto, "Zeta functions of finite graphs and representations of p-adic groups"
    (1989)
  - Terras, "Zeta Functions of Graphs: A Stroll through the Garden" (2011)
  - Stark-Terras, "Zeta functions of finite graphs and coverings" (1996, 2000)
  - higher_genus_modular_koszul.tex: def:stable-graph-coefficient-algebra
  - concordance.tex: const:vol1-genus-spectral-sequence

CONVENTIONS:
  - u is the spectral parameter for the Ihara zeta.
  - q is the genus-counting parameter for the bar generating function.
  - All computations use exact arithmetic (Fraction) where possible.
  - Floating-point only for zero-finding (Newton/bisection).

VERIFICATION PATHS (Multi-Path Mandate):
  1. Direct cycle enumeration (definition)
  2. Hashimoto-Bass determinant formula
  3. Known results for cycle graphs: zeta_{C_n}(u) = (1 - u^n)^{-1}
  4. Euler product comparison with Dirichlet series
"""

from __future__ import annotations

import math
import cmath
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

import numpy as np
from numpy.polynomial import polynomial as P

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    genus1_stable_graphs_n0,
    genus2_stable_graphs_n0,
)


# ===========================================================================
# 1.  ADJACENCY AND DEGREE MATRICES FOR STABLE GRAPHS
# ===========================================================================

def adjacency_matrix(graph: StableGraph) -> np.ndarray:
    """Compute the adjacency matrix of a stable graph (multigraph with self-loops).

    Convention for multigraphs:
      A_{ii} = 2 * (number of self-loops at vertex i)
      A_{ij} = number of edges between vertices i and j, for i != j

    This matches the standard graph theory convention where each self-loop
    contributes 2 to the degree of the vertex (since both half-edges are
    at the same vertex).
    """
    n = graph.num_vertices
    A = np.zeros((n, n), dtype=int)
    for v1, v2 in graph.edges:
        if v1 == v2:
            A[v1, v1] += 2  # self-loop contributes 2
        else:
            A[v1, v2] += 1
            A[v2, v1] += 1
    return A


def degree_matrix(graph: StableGraph) -> np.ndarray:
    """Compute the degree matrix D = diag(deg(v)).

    For multigraphs, deg(v) = number of half-edges at v (from edges only,
    NOT including legs/marked points).  Each self-loop contributes 2 to degree.
    """
    n = graph.num_vertices
    A = adjacency_matrix(graph)
    D = np.diag(np.sum(A, axis=1))
    return D


def edge_degree_vector(graph: StableGraph) -> np.ndarray:
    """Return the vector of vertex degrees (from edges only)."""
    A = adjacency_matrix(graph)
    return np.sum(A, axis=1)


# ===========================================================================
# 2.  HASHIMOTO (EDGE ADJACENCY) MATRIX
# ===========================================================================

def oriented_edge_list(graph: StableGraph) -> List[Tuple[int, int, int, int]]:
    """Return the list of oriented edges (origin, terminus, edge_index, direction).

    Each undirected edge {v1, v2} (including self-loops where v1 = v2)
    produces two oriented edges distinguished by direction 0 and 1:
      (v1, v2, i, 0)  and  (v2, v1, i, 1)

    For self-loops v1 = v2, both oriented edges have the same origin
    and terminus, but they are distinct objects (the two half-edges of
    the loop, distinguished by direction).  The reverse of (v, v, i, 0)
    is (v, v, i, 1), NOT itself.

    Returns a list of (origin, terminus, edge_index, direction) 4-tuples.
    """
    oriented = []
    for idx, (v1, v2) in enumerate(graph.edges):
        oriented.append((v1, v2, idx, 0))
        oriented.append((v2, v1, idx, 1))
    return oriented


def hashimoto_matrix(graph: StableGraph) -> np.ndarray:
    """Compute the Hashimoto (edge adjacency) matrix T.

    T is a 2|E| x 2|E| matrix indexed by oriented edges.
    T_{e, f} = 1 if terminal(e) = origin(f) and f != bar(e),
    where bar(e) is the reverse of e (same edge, opposite direction).

    The reverse of oriented edge (o, t, idx, d) is (t, o, idx, 1-d).
    For self-loops (v, v, idx, 0), the reverse is (v, v, idx, 1).

    The Ihara zeta function satisfies:
        zeta_G(u)^{-1} = det(I - u * T)
    """
    edges_or = oriented_edge_list(graph)
    m = len(edges_or)
    T = np.zeros((m, m), dtype=int)

    for i, (o_i, t_i, idx_i, d_i) in enumerate(edges_or):
        for j, (o_j, t_j, idx_j, d_j) in enumerate(edges_or):
            # terminal of e_i = origin of e_j, and e_j is not the reverse of e_i
            if t_i == o_j:
                # bar(e_i) has edge_index = idx_i and direction = 1 - d_i
                is_reverse = (idx_j == idx_i and d_j == 1 - d_i)
                if not is_reverse:
                    T[i, j] = 1

    return T


# ===========================================================================
# 3.  IHARA ZETA FUNCTION
# ===========================================================================

def ihara_zeta_reciprocal_hashimoto(graph: StableGraph, u: complex) -> complex:
    """Compute zeta_G(u)^{-1} = det(I - u * T) via the Hashimoto matrix.

    This is the DEFINITION-LEVEL computation (verification path 2).
    """
    T = hashimoto_matrix(graph)
    m = T.shape[0]
    if m == 0:
        # No edges => zeta = 1 (empty product), so reciprocal = 1
        return complex(1.0)
    M = np.eye(m, dtype=complex) - u * T.astype(complex)
    return np.linalg.det(M)


def ihara_zeta_reciprocal_bass(graph: StableGraph, u: complex) -> complex:
    """Compute zeta_G(u)^{-1} via the Bass three-term determinant formula.

    For a multigraph (possibly with self-loops):

        zeta_G(u)^{-1} = (1 - u^2)^{r-1} * det(I - u*A + u^2*(D - I))

    where:
      A = adjacency matrix (multigraph convention: A_{ii} = 2*self-loops)
      D = degree matrix (D_{ii} = sum_j A_{ij})
      r = |E| - |V| + 1 = cyclomatic number (for connected graphs)
      I = identity matrix

    For disconnected graphs (which should not occur for stable graphs),
    r = |E| - |V| + (number of components).

    This is verification path 2 (alternative formula).
    """
    n = graph.num_vertices
    if n == 0:
        return complex(1.0)

    A = adjacency_matrix(graph).astype(complex)
    D = degree_matrix(graph).astype(complex)
    I_n = np.eye(n, dtype=complex)

    r = graph.first_betti

    # Three-term determinant
    M = I_n - u * A + u**2 * (D - I_n)
    det_M = np.linalg.det(M)

    # Bass formula: zeta^{-1} = (1-u^2)^{r-1} * det(I - uA + u^2(D-I))
    # For trees (r=0): factor = (1-u^2)^{-1}, and det should be (1-u^2), giving 1.
    factor = (1.0 - u**2) ** (r - 1)

    return factor * det_M


def ihara_zeta_reciprocal_poly_coeffs(graph: StableGraph) -> np.ndarray:
    """Compute the polynomial coefficients of zeta_G(u)^{-1} = det(I - u*T).

    Returns coefficients [c_0, c_1, ..., c_m] of the polynomial
    p(u) = c_0 + c_1*u + ... + c_m*u^m  where p(u) = det(I - u*T).

    Uses the characteristic polynomial of T:
        det(I - u*T) = det(-T) * det(-T^{-1} + u*I) ... NO, this is fragile.

    Instead, we expand det(I - u*T) directly by computing det(I - u*T) at
    enough points and interpolating, OR by using the coefficient formula.

    For numerical stability, we evaluate at roots of unity and use DFT.
    """
    T = hashimoto_matrix(graph)
    m = T.shape[0]
    if m == 0:
        return np.array([1.0])

    # Evaluate at m+1 points on the unit circle
    n_pts = m + 1
    vals = np.zeros(n_pts, dtype=complex)
    for k in range(n_pts):
        u = np.exp(2j * np.pi * k / n_pts) * 0.5  # scale to avoid singularities
        M = np.eye(m, dtype=complex) - u * T.astype(complex)
        vals[k] = np.linalg.det(M)

    # Lagrange interpolation (or use numpy's polyfit)
    points = [0.5 * np.exp(2j * np.pi * k / n_pts) for k in range(n_pts)]
    # Use Vandermonde
    V = np.vander(points, increasing=True)
    coeffs = np.linalg.solve(V, vals)

    # Round near-integer coefficients
    coeffs_real = np.real(coeffs)
    coeffs_rounded = np.round(coeffs_real).astype(int)
    # Verify
    if np.max(np.abs(coeffs_real - coeffs_rounded)) < 1e-6:
        return coeffs_rounded.astype(float)
    return coeffs_real


def ihara_zeta_value(graph: StableGraph, u: complex) -> complex:
    """Compute zeta_G(u) = 1 / det(I - u*T).

    Uses the Hashimoto matrix for the primary computation.
    """
    recip = ihara_zeta_reciprocal_hashimoto(graph, u)
    if abs(recip) < 1e-15:
        return complex(float('inf'))
    return 1.0 / recip


# ===========================================================================
# 4.  BASS THREE-TERM POLYNOMIAL (EXACT, FOR SPECTRUM ANALYSIS)
# ===========================================================================

def bass_polynomial_matrix(graph: StableGraph) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (A, D, I) for the Bass three-term formula.

    The Bass polynomial is det(I - u*A + u^2*(D - I)) as a function of u.
    """
    n = graph.num_vertices
    A = adjacency_matrix(graph).astype(float)
    D = degree_matrix(graph).astype(float)
    I_n = np.eye(n, dtype=float)
    return A, D, I_n


def bass_determinant_at_u(graph: StableGraph, u: complex) -> complex:
    """Evaluate det(I - u*A + u^2*(D - I)) at a given u."""
    n = graph.num_vertices
    if n == 0:
        return complex(1.0)
    A, D, I_n = bass_polynomial_matrix(graph)
    M = I_n - u * A + u**2 * (D - I_n)
    return np.linalg.det(M)


# ===========================================================================
# 5.  SPECTRUM AND RAMANUJAN PROPERTY
# ===========================================================================

def adjacency_spectrum(graph: StableGraph) -> np.ndarray:
    """Eigenvalues of the adjacency matrix, sorted by decreasing real part."""
    A = adjacency_matrix(graph).astype(float)
    if A.shape[0] == 0:
        return np.array([])
    evals = np.linalg.eigvalsh(A)
    return np.sort(evals)[::-1]


def max_degree(graph: StableGraph) -> int:
    """Maximum vertex degree (from edges only, each self-loop counts 2)."""
    A = adjacency_matrix(graph)
    if A.shape[0] == 0:
        return 0
    return int(np.max(np.sum(A, axis=1)))


def is_regular(graph: StableGraph) -> bool:
    """Check if the graph is regular (all vertices have the same degree)."""
    degs = edge_degree_vector(graph)
    if len(degs) == 0:
        return True
    return np.all(degs == degs[0])


def ramanujan_bound(graph: StableGraph) -> float:
    """The Ramanujan bound 2*sqrt(d_max - 1) for the spectral gap.

    For a (q+1)-regular graph, the Ramanujan bound is 2*sqrt(q).
    For non-regular graphs, we use 2*sqrt(d_max - 1) as a generalization.
    """
    d = max_degree(graph)
    if d <= 1:
        return 0.0
    return 2.0 * math.sqrt(d - 1)


def is_ramanujan(graph: StableGraph) -> bool:
    """Check the Ramanujan property for a graph.

    A connected (q+1)-regular graph is Ramanujan if all nontrivial eigenvalues
    lambda of A satisfy |lambda| <= 2*sqrt(q).

    For non-regular graphs or graphs with self-loops, we check whether all
    eigenvalues except the largest satisfy |lambda| <= 2*sqrt(d_max - 1).

    For a single-vertex graph with self-loops, the eigenvalue is 2*loops.
    The trivial eigenvalue is the largest; there are no nontrivial ones
    when |V| = 1.  Convention: single-vertex graphs are Ramanujan.
    """
    spec = adjacency_spectrum(graph)
    if len(spec) <= 1:
        return True  # Single-vertex or empty: vacuously Ramanujan

    d = max_degree(graph)
    if d <= 1:
        return True

    bound = 2.0 * math.sqrt(d - 1)
    # Nontrivial eigenvalues: all except the largest
    nontrivial = spec[1:]
    return bool(np.all(np.abs(nontrivial) <= bound + 1e-10))


def spectral_gap(graph: StableGraph) -> float:
    """The spectral gap: lambda_1 - max(|lambda_2|, |lambda_n|).

    For a connected graph, lambda_1 = max eigenvalue, and the spectral gap
    measures how far the nontrivial eigenvalues are from lambda_1.

    Returns lambda_1 - max nontrivial |eigenvalue|.
    """
    spec = adjacency_spectrum(graph)
    if len(spec) <= 1:
        return float('inf')
    return float(spec[0] - max(abs(spec[1]), abs(spec[-1])))


# ===========================================================================
# 6.  BAR GRAPH ZETA FUNCTIONS (WEIGHTED SUMS)
# ===========================================================================

def bar_graph_zeta_g(g: int, u: complex, n: int = 0) -> complex:
    """Compute the bar graph zeta at genus g:

        Z^{bar}_g(u) = sum_Gamma |Aut(Gamma)|^{-1} * zeta_Gamma(u)

    where the sum is over all stable graphs Gamma of type (g, n).

    Note: for (g,n) = (1,0), 2g-2+n = 0 which fails the strict stability
    condition, but M_bar_{1,0} exists as a DM stack and the bar construction
    does produce genus-1 contributions.  We allow this case.
    """
    graphs = enumerate_stable_graphs(g, n)
    if not graphs:
        return complex(0.0)

    total = complex(0.0)
    for gamma in graphs:
        aut = gamma.automorphism_order()
        zeta_val = ihara_zeta_value(gamma, u)
        total += zeta_val / aut
    return total


def bar_graph_zeta_reciprocal_g(g: int, u: complex, n: int = 0) -> complex:
    """Compute the reciprocal bar graph zeta at genus g.

    This is NOT 1/Z^{bar}_g(u) but rather

        Z^{bar,rec}_g(u) = sum_Gamma |Aut(Gamma)|^{-1} * zeta_Gamma(u)^{-1}

    i.e., the weighted sum of the reciprocal zetas (which are polynomials).
    This is more natural for spectral analysis.
    """
    graphs = enumerate_stable_graphs(g, n)
    if not graphs:
        return complex(0.0)
    total = complex(0.0)
    for gamma in graphs:
        aut = gamma.automorphism_order()
        recip = ihara_zeta_reciprocal_hashimoto(gamma, u)
        total += recip / aut
    return total


def total_bar_zeta(u: complex, q: complex, max_genus: int = 4) -> complex:
    """Compute the total bar zeta function:

        Z^{bar}(u, q) = sum_{g=1}^{max_genus} Z^{bar}_g(u) * q^g

    Note: genus 0 with n=0 is unstable (2*0 - 2 + 0 = -2 < 0), so the
    sum starts at g=1.
    """
    total = complex(0.0)
    for g in range(1, max_genus + 1):
        z_g = bar_graph_zeta_g(g, u)
        total += z_g * q**g
    return total


# ===========================================================================
# 7.  ZERO-FINDING FOR BAR GRAPH ZETAS
# ===========================================================================

def find_ihara_zeros(graph: StableGraph, n_sample: int = 1000,
                     r_max: float = 2.0) -> List[complex]:
    """Find approximate zeros of zeta_Gamma(u)^{-1} = det(I - u*T).

    These are the poles of zeta_Gamma(u), i.e., eigenvalues of T^{-1}
    (reciprocals of eigenvalues of T).

    For a graph with 2|E| oriented edges, T is 2|E| x 2|E|.
    The eigenvalues of T determine the zeros of det(I - uT):
        det(I - uT) = 0  iff  u = 1/lambda for some eigenvalue lambda of T.

    Returns eigenvalues 1/lambda_i for nonzero eigenvalues lambda_i of T.
    """
    T = hashimoto_matrix(graph)
    m = T.shape[0]
    if m == 0:
        return []

    evals = np.linalg.eigvals(T.astype(complex))
    zeros = []
    for lam in evals:
        if abs(lam) > 1e-12:
            z = 1.0 / lam
            if abs(z) <= r_max:
                zeros.append(z)
    return sorted(zeros, key=lambda z: abs(z))


def bar_zeta_zeros_genus(g: int, n_grid: int = 200,
                         r_max: float = 2.0) -> List[complex]:
    """Find approximate zeros of Z^{bar}_g(u) in the disk |u| <= r_max.

    Uses a grid search followed by Newton refinement.  The bar graph zeta
    is a sum of rational functions, so its zeros are found numerically.

    Returns a list of approximate zeros sorted by modulus.
    """
    # Grid search on a polar grid
    candidates = []
    for r_idx in range(1, n_grid + 1):
        r = r_max * r_idx / n_grid
        for theta_idx in range(4 * n_grid):
            theta = 2 * math.pi * theta_idx / (4 * n_grid)
            u = r * cmath.exp(1j * theta)
            val = bar_graph_zeta_g(g, u)
            if abs(val) > 1e10:  # Near a pole
                continue
            candidates.append((u, val))

    # Find sign/phase changes (approximate zero crossings)
    zeros = []
    # Use Newton's method from points where |Z| is small
    small_pts = sorted(candidates, key=lambda x: abs(x[1]))[:20]
    for u0, _ in small_pts:
        z = _newton_bar_zeta(g, u0, max_iter=50)
        if z is not None and abs(z) <= r_max:
            # Check it's actually a zero
            val = bar_graph_zeta_g(g, z)
            if abs(val) < 1e-6:
                # Deduplicate
                is_dup = False
                for existing in zeros:
                    if abs(z - existing) < 1e-6:
                        is_dup = True
                        break
                if not is_dup:
                    zeros.append(z)

    return sorted(zeros, key=lambda z: abs(z))


def _newton_bar_zeta(g: int, u0: complex, max_iter: int = 50,
                     tol: float = 1e-12) -> Optional[complex]:
    """Newton's method for finding zeros of Z^{bar}_g(u)."""
    u = u0
    h = 1e-8
    for _ in range(max_iter):
        val = bar_graph_zeta_g(g, u)
        if abs(val) < tol:
            return u
        # Numerical derivative
        val_h = bar_graph_zeta_g(g, u + h)
        deriv = (val_h - val) / h
        if abs(deriv) < 1e-15:
            return None
        u = u - val / deriv
    return u if abs(bar_graph_zeta_g(g, u)) < 1e-6 else None


# ===========================================================================
# 8.  PLANTED FOREST IHARA ZETA
# ===========================================================================

def is_planted_forest_graph(graph: StableGraph) -> bool:
    """Check if a stable graph belongs to the planted-forest subcomplex.

    A graph is in the planted-forest subcomplex if it has at least one
    genus-0 vertex of valence >= 3 (carrying a higher L_infinity operation).

    Trees (h^1 = 0) with genus-0 vertices of valence >= 3 are planted forests.
    Graphs with loops where at least one genus-0 vertex has val >= 3 also qualify.

    The smooth curve (single vertex of high genus, no edges) is NOT a planted
    forest graph.
    """
    val = graph.valence
    for v in range(graph.num_vertices):
        if graph.vertex_genera[v] == 0 and val[v] >= 3:
            return True
    return False


def planted_forest_zeta_g(g: int, u: complex, n: int = 0) -> complex:
    """Compute the planted-forest Ihara zeta at genus g.

    Z^{pf}_g(u) = sum_{Gamma in PF} |Aut(Gamma)|^{-1} * zeta_Gamma(u)

    where PF is the set of planted-forest stable graphs at genus g.
    """
    graphs = enumerate_stable_graphs(g, n)
    if not graphs:
        return complex(0.0)
    total = complex(0.0)
    for gamma in graphs:
        if not is_planted_forest_graph(gamma):
            continue
        aut = gamma.automorphism_order()
        zeta_val = ihara_zeta_value(gamma, u)
        total += zeta_val / aut
    return total


def non_planted_forest_zeta_g(g: int, u: complex, n: int = 0) -> complex:
    """The complement: graphs NOT in the planted-forest subcomplex."""
    return bar_graph_zeta_g(g, u, n) - planted_forest_zeta_g(g, u, n)


# ===========================================================================
# 9.  CYCLE ENUMERATION (DIRECT VERIFICATION PATH)
# ===========================================================================

def enumerate_prime_cycles(graph: StableGraph, max_length: int = 10) -> List[Tuple[int, ...]]:
    """Enumerate all prime (backtrackless, tailless) cycles up to length max_length.

    A prime cycle is a closed walk on oriented edges that:
      1. Never backtracks: consecutive edges e, f satisfy f != bar(e)
      2. Is not a power of a shorter cycle
      3. Is considered up to cyclic permutation (equivalence class)

    For verification against the Ihara product formula.

    Returns a list of cycles, each represented as a tuple of oriented edge indices.
    """
    edges_or = oriented_edge_list(graph)
    m = len(edges_or)
    if m == 0:
        return []

    # Build adjacency for oriented edges (same as Hashimoto)
    adj = [[] for _ in range(m)]
    for i, (o_i, t_i, idx_i, d_i) in enumerate(edges_or):
        for j, (o_j, t_j, idx_j, d_j) in enumerate(edges_or):
            if t_i == o_j:
                is_reverse = (idx_j == idx_i and d_j == 1 - d_i)
                if not is_reverse:
                    adj[i].append(j)

    # Find all backtrackless closed walks up to max_length
    all_cycles = []
    for length in range(1, max_length + 1):
        for start in range(m):
            _dfs_cycles(adj, start, [start], length, all_cycles)

    # Filter to prime cycles (not powers of shorter) and take cyclic equivalence classes
    prime_cycles = []
    seen = set()
    for cycle in all_cycles:
        # Normalize: take the lexicographically smallest cyclic rotation
        normalized = _normalize_cycle(cycle)
        if normalized in seen:
            continue
        # Check if it's a power of a shorter cycle
        if _is_prime_cycle(normalized):
            seen.add(normalized)
            prime_cycles.append(normalized)

    return prime_cycles


def _dfs_cycles(adj, start, path, target_length, result):
    """DFS to find all backtrackless closed walks of exactly target_length."""
    if len(path) == target_length:
        # Check if we can close the walk
        last = path[-1]
        if start in adj[last]:
            result.append(tuple(path))
        return
    last = path[-1]
    for nxt in adj[last]:
        path.append(nxt)
        _dfs_cycles(adj, start, path, target_length, result)
        path.pop()


def _normalize_cycle(cycle: Tuple[int, ...]) -> Tuple[int, ...]:
    """Return the lexicographically smallest cyclic rotation."""
    n = len(cycle)
    best = cycle
    for i in range(1, n):
        rotated = cycle[i:] + cycle[:i]
        if rotated < best:
            best = rotated
    return best


def _is_prime_cycle(cycle: Tuple[int, ...]) -> bool:
    """Check if a cycle is primitive (not a power of a shorter cycle)."""
    n = len(cycle)
    for d in range(1, n):
        if n % d == 0:
            # Check if cycle = (cycle[:d])^{n/d}
            base = cycle[:d]
            is_power = True
            for k in range(1, n // d):
                if cycle[k*d:(k+1)*d] != base:
                    is_power = False
                    break
            if is_power and d < n:
                return False
    return True


def ihara_from_cycles(graph: StableGraph, u: complex,
                      max_length: int = 10) -> complex:
    """Compute zeta_G(u) from the cycle product definition (verification path 1).

    zeta_G(u) = prod_{[p] prime} (1 - u^{|p|})^{-1}

    This is the DEFINITION-LEVEL computation, limited to cycles up to max_length.
    It provides only a partial product but should agree with the determinant
    formula at small |u|.
    """
    cycles = enumerate_prime_cycles(graph, max_length)
    product = complex(1.0)
    for cycle in cycles:
        length = len(cycle)
        product *= (1.0 - u**length)
    return 1.0 / product if abs(product) > 1e-15 else complex(float('inf'))


# ===========================================================================
# 10. SPECTRAL ANALYSIS AND RAMANUJAN STATISTICS
# ===========================================================================

def ramanujan_statistics(g: int, n: int = 0) -> Dict:
    """Compute Ramanujan property statistics for all stable graphs at genus g.

    Returns:
        {
            'total': number of graphs,
            'ramanujan_count': number satisfying the Ramanujan bound,
            'ramanujan_fraction': fraction,
            'max_nontrivial_eigenvalue': largest |nontrivial eigenvalue| across all graphs,
            'min_spectral_gap': smallest spectral gap,
            'spectrum_data': list of (graph_index, is_ramanujan, max_nontrivial, gap)
        }
    """
    graphs = enumerate_stable_graphs(g, n)
    total = len(graphs)
    ram_count = 0
    max_nontrivial = 0.0
    min_gap = float('inf')
    data = []

    for idx, gamma in enumerate(graphs):
        is_ram = is_ramanujan(gamma)
        if is_ram:
            ram_count += 1

        spec = adjacency_spectrum(gamma)
        if len(spec) > 1:
            nt_max = max(abs(spec[1]), abs(spec[-1]))
            gap = spec[0] - nt_max
        else:
            nt_max = 0.0
            gap = float('inf')

        max_nontrivial = max(max_nontrivial, nt_max)
        min_gap = min(min_gap, gap)
        data.append((idx, is_ram, nt_max, gap))

    return {
        'total': total,
        'ramanujan_count': ram_count,
        'ramanujan_fraction': Fraction(ram_count, total) if total > 0 else Fraction(0),
        'max_nontrivial_eigenvalue': max_nontrivial,
        'min_spectral_gap': min_gap,
        'spectrum_data': data,
    }


def spectral_radius_distribution(g: int, n: int = 0) -> List[float]:
    """Return the sorted list of largest eigenvalues across all stable graphs at genus g."""
    graphs = enumerate_stable_graphs(g, n)
    radii = []
    for gamma in graphs:
        spec = adjacency_spectrum(gamma)
        if len(spec) > 0:
            radii.append(float(spec[0]))
        else:
            radii.append(0.0)
    return sorted(radii)


def nontrivial_spectral_radii(g: int, n: int = 0) -> List[float]:
    """Return sorted list of max |nontrivial eigenvalue| for all stable graphs at genus g."""
    graphs = enumerate_stable_graphs(g, n)
    radii = []
    for gamma in graphs:
        spec = adjacency_spectrum(gamma)
        if len(spec) > 1:
            radii.append(max(abs(spec[1]), abs(spec[-1])))
        else:
            radii.append(0.0)
    return sorted(radii)


# ===========================================================================
# 11. IHARA ZETA FOR SPECIFIC KNOWN GRAPHS (VERIFICATION)
# ===========================================================================

def cycle_graph_zeta_reciprocal(n: int, u: complex) -> complex:
    """The Ihara zeta of the cycle graph C_n (n-gon).

    Known result: zeta_{C_n}(u)^{-1} = (1 - u^n)^2 * (1 - u^2)^{-1}

    Wait -- let me recompute.  For the n-cycle:
      - |V| = n, |E| = n, r = n - n + 1 = 1
      - A is the circulant matrix with eigenvalues 2*cos(2*pi*k/n) for k=0,...,n-1
      - D = 2*I (each vertex has degree 2)
      - Bass: det(I - uA + u^2*(2I - I)) = det(I - uA + u^2*I)
              = prod_k (1 - 2*cos(2*pi*k/n)*u + u^2)
              = prod_k ((1 - e^{2*pi*i*k/n}*u)(1 - e^{-2*pi*i*k/n}*u))
              = (1 - u^n)^2
      - (1-u^2)^{r-1} = (1-u^2)^0 = 1
      - So zeta_{C_n}(u)^{-1} = (1 - u^n)^2

    But also from the cycle product: there are two prime cycles of length n
    (one in each direction), giving:

        zeta_{C_n}(u) = (1 - u^n)^{-2}

    Actually wait.  For the n-cycle (n >= 3):
      - The two prime cycles of length n are the two traversals.
      - There are no shorter prime cycles (backtrackless requires n >= 3).
      - So zeta_{C_n}(u) = (1 - u^n)^{-2} for n >= 3.

    For n = 1 (single vertex with self-loop): special case.
    For n = 2 (two vertices with 2 edges = double edge):
      - 2 prime cycles of length 2 => zeta = (1 - u^2)^{-2}
      - But also need to check: is the single edge a "cycle" of length 2?
        No, for a single edge between v1, v2 there are no backtrackless cycles.
        For a double edge, the cycle v1->v2->v1 using different edges IS backtrackless.

    So: zeta_{C_n}(u)^{-1} = (1 - u^n)^2 for n >= 3.
    """
    return (1.0 - u**n) ** 2


def make_cycle_stable_graph(n: int) -> StableGraph:
    """Create a stable graph representing the n-cycle.

    For n >= 3: n genus-0 vertices, n edges forming a cycle, and we need
    stability: val(v) = 2 but 2*0 - 2 + 2 = 0, NOT > 0.
    So a pure n-cycle with genus-0 vertices is NOT stable.

    For the bar complex, the relevant cycle-like graphs are:
      - genus 1, n=0: single vertex genus-1 (no edges) or genus-0 with self-loop
      - The "theta graph" at genus 2: two vertices with 3 parallel edges

    This function creates the cycle as a (non-stable) graph for testing purposes.
    For a stable version, we need to add marked points or use genus-1 vertices.
    """
    if n < 1:
        raise ValueError(f"Cycle graph requires n >= 1, got {n}")
    # n vertices genus 0, edges forming a cycle
    edges = tuple((i, (i + 1) % n) if i < (i + 1) % n else ((i + 1) % n, i)
                  for i in range(n))
    genera = (0,) * n
    # Add 1 leg per vertex for stability (2*0 - 2 + 3 = 1 > 0)
    legs = tuple(range(n))
    return StableGraph(vertex_genera=genera, edges=edges, legs=legs)


def bouquet_graph_zeta_reciprocal(k: int, u: complex) -> complex:
    """Ihara zeta reciprocal for the bouquet graph B_k (single vertex, k self-loops).

    For the bouquet B_k:
      - |V| = 1, |E| = k, r = k - 1 + 1 = k
      - A = (2k,) (1x1 matrix), D = (2k,) (each self-loop contributes 2 to degree)
      - Bass: (1-u^2)^{k-1} * det(I - 2k*u + u^2*(2k - 1))
            = (1-u^2)^{k-1} * (1 - 2k*u + (2k-1)*u^2)
      - Hashimoto: T is 2k x 2k.  The oriented edges from the single vertex
        go to the single vertex, with the no-backtrack constraint.

    For k = 1 (single self-loop = genus-1 nodal curve):
      - Bass: (1-u^2)^0 * (1 - 2u + u^2) = (1-u)^2
      - So zeta_{B_1}(u)^{-1} = (1-u)^2, hence zeta_{B_1}(u) = (1-u)^{-2}
      - Cycle product: one prime cycle of length 1 in each direction
        => zeta = (1-u)^{-2}.  Check: the self-loop gives TWO oriented edges.
        The backtrackless walk of length 1: start at edge e, next must not be bar(e).
        For B_1 with 2 oriented edges {e, bar(e)}: from e, the only neighbor is
        bar(e), which IS bar(e). So there are NO backtrackless closed walks!
        Wait -- that means the Hashimoto matrix has all zeros for k=1...

    Let me reconsider. For B_1 (single self-loop on one vertex):
      - Oriented edges: e = (0 -> 0, edge 0, forward), bar(e) = (0 -> 0, edge 0, backward)
      - From e: terminal(e) = 0 = origin(bar(e)), but bar(e) IS the reverse of e.
        No other edges. So T = [[0,0],[0,0]]. det(I - uT) = 1.
      - So zeta_{B_1}(u)^{-1} = 1, meaning zeta_{B_1}(u) = 1.

    But the Bass formula gives (1-u)^2 ... This is the well-known discrepancy
    for graphs with degree < 2 vertices.  The Bass formula assumes minimum
    degree >= 2.  For the bouquet B_1, each "vertex" has degree 2 (the self-loop
    contributes 2), so Bass should apply.

    Actually, let me reconsider the Hashimoto matrix for B_1 more carefully.
    The oriented edges are e_+ and e_- (the two orientations of the self-loop).
    terminal(e_+) = 0, origin(e_-) = 0, and e_- IS bar(e_+).
    terminal(e_-) = 0, origin(e_+) = 0, and e_+ IS bar(e_-).
    So T = [[0, 0], [0, 0]].  det(I - uT) = 1.

    For B_2 (two self-loops):
    Oriented edges: e1+, e1-, e2+, e2-.
    From e1+: terminal = 0. Neighbors at 0: e1+, e1-, e2+, e2-.
    Exclude bar(e1+) = e1-. So T[e1+, e1+] = 1, T[e1+, e2+] = 1, T[e1+, e2-] = 1.
    The Hashimoto matrix is 4x4.

    The Bass formula for B_2:
      (1-u^2)^1 * (1 - 4u + 3u^2)
      = (1-u^2)(1 - 4u + 3u^2)
      = (1-u)(1+u)(1-u)(1-3u)
      = (1-u)^2(1+u)(1-3u)

    This should equal det(I - uT) for the Hashimoto matrix of B_2.

    For general bouquet B_k (k self-loops), degree = 2k:
      Bass: (1-u^2)^{k-1} * (1 - 2ku + (2k-1)u^2)
    """
    k_val = k
    if k_val == 0:
        return complex(1.0)
    # Bass formula
    bass_det = 1.0 - 2 * k_val * u + (2 * k_val - 1) * u**2
    factor = (1.0 - u**2) ** (k_val - 1)
    return factor * bass_det


# ===========================================================================
# 12. GENUS-SPECIFIC IHARA ZETA COMPUTATIONS
# ===========================================================================

def genus1_ihara_data() -> List[Dict]:
    """Ihara zeta data for all genus-1 stable graphs (n=0).

    The two genus-1 graphs:
      1. Smooth torus: 1 vertex g=1, no edges. |Aut|=1.
         No edges => T is empty, zeta = 1.
      2. Nodal rational: 1 vertex g=0, 1 self-loop. |Aut|=2.
         Single self-loop => T is 2x2 all zeros (as above), zeta = 1.

    So Z^{bar}_1(u) = 1/1 + 1/2 = 3/2 for all u.
    This is a CONSTANT function of u.
    """
    graphs = genus1_stable_graphs_n0()
    data = []
    for idx, gamma in enumerate(graphs):
        T = hashimoto_matrix(gamma)
        spec = adjacency_spectrum(gamma)
        data.append({
            'index': idx,
            'graph': gamma,
            'hashimoto_size': T.shape[0],
            'hashimoto_rank': int(np.linalg.matrix_rank(T)) if T.shape[0] > 0 else 0,
            'adjacency_spectrum': spec.tolist(),
            'is_ramanujan': is_ramanujan(gamma),
            'automorphism_order': gamma.automorphism_order(),
        })
    return data


def genus2_ihara_data() -> List[Dict]:
    """Ihara zeta data for all genus-2 stable graphs (n=0).

    The 6 genus-2 graphs and their Ihara zetas (computed via Hashimoto/Bass):

    1. Smooth (g=2, no edges): zeta = 1, |Aut| = 1
    2. Irr node (g=1, 1 self-loop): T=2x2 zeros, zeta = 1, |Aut| = 2
    3. Banana (g=0, 2 self-loops): T=4x4, nontrivial, |Aut| = 8
    4. Separating (g=1+g=1, 1 edge): T=2x2, nontrivial, |Aut| = 2
    5. Theta (g=0+g=0, 3 edges): T=6x6, nontrivial, |Aut| = 12
    6. Mixed (g=0 self-loop + g=1, 1 edge): T=4x4, |Aut| = 2
    """
    graphs = genus2_stable_graphs_n0()
    data = []
    for idx, gamma in enumerate(graphs):
        T = hashimoto_matrix(gamma)
        spec = adjacency_spectrum(gamma)
        data.append({
            'index': idx,
            'graph': gamma,
            'num_edges': gamma.num_edges,
            'num_vertices': gamma.num_vertices,
            'hashimoto_size': T.shape[0],
            'adjacency_spectrum': spec.tolist(),
            'is_ramanujan': is_ramanujan(gamma),
            'automorphism_order': gamma.automorphism_order(),
            'first_betti': gamma.first_betti,
        })
    return data


# ===========================================================================
# 13. IHARA ZETA POLES AND THE UNIT CIRCLE APPROACH
# ===========================================================================

def ihara_pole_radii(g: int, n: int = 0) -> List[float]:
    """Compute |pole| for all poles of the Ihara zeta for each stable graph at genus g.

    The poles of zeta_Gamma(u) are the zeros of det(I - uT), which are the
    reciprocals of the nonzero eigenvalues of T.

    Returns a sorted list of all pole radii across all stable graphs at genus g.
    """
    graphs = enumerate_stable_graphs(g, n)
    radii = []
    for gamma in graphs:
        T = hashimoto_matrix(gamma)
        if T.shape[0] == 0:
            continue
        evals = np.linalg.eigvals(T.astype(complex))
        for lam in evals:
            if abs(lam) > 1e-12:
                radii.append(abs(1.0 / lam))
    return sorted(radii)


def min_pole_radius(g: int, n: int = 0) -> float:
    """The smallest pole radius across all stable graphs at genus g.

    If this approaches 1 as g -> infinity, poles approach the unit circle
    (analogous to RH for the Ihara zeta of Ramanujan graphs).
    """
    radii = ihara_pole_radii(g, n)
    return min(radii) if radii else float('inf')


def unit_circle_approach_data(max_genus: int = 4) -> Dict[int, float]:
    """For each genus g, compute the minimum Ihara pole radius.

    Track whether the poles approach the unit circle as g grows.
    """
    data = {}
    for g in range(1, max_genus + 1):
        data[g] = min_pole_radius(g)
    return data


# ===========================================================================
# 14. WEIGHTED IHARA INVARIANTS FOR THE BAR COMPLEX
# ===========================================================================

def bar_weighted_hashimoto_trace(g: int, power: int = 1,
                                 n: int = 0) -> complex:
    """Compute the bar-weighted trace:

        sum_Gamma |Aut(Gamma)|^{-1} * Tr(T_Gamma^power)

    This is related to the number of closed backtrackless walks of length
    'power' in the graph, weighted by the automorphism factor.

    The coefficient of u^k in the Taylor expansion of
    -d/du log zeta_G(u) = sum_{k>=1} N_k u^{k-1}
    counts the number of closed backtrackless walks of length k.
    """
    graphs = enumerate_stable_graphs(g, n)
    total = complex(0.0)
    for gamma in graphs:
        T = hashimoto_matrix(gamma)
        if T.shape[0] == 0:
            continue
        aut = gamma.automorphism_order()
        T_power = np.linalg.matrix_power(T.astype(complex), power)
        tr = np.trace(T_power)
        total += tr / aut
    return total


def bar_weighted_closed_walks(g: int, max_length: int = 10,
                              n: int = 0) -> List[complex]:
    """Compute N_k = bar-weighted number of closed backtrackless walks of length k.

    Returns [N_1, N_2, ..., N_{max_length}].
    """
    return [bar_weighted_hashimoto_trace(g, k, n) for k in range(1, max_length + 1)]


# ===========================================================================
# 15. SUMMARY FUNCTIONS
# ===========================================================================

def full_ihara_analysis(g: int, n: int = 0) -> Dict:
    """Complete Ihara zeta analysis for a given genus.

    Returns a dictionary with:
      - graph_count: number of stable graphs
      - per_graph: list of per-graph data (spectrum, poles, Ramanujan, etc.)
      - bar_zeta_at_half: Z^{bar}_g(1/2)
      - ramanujan_stats: Ramanujan property statistics
      - min_pole_radius: smallest Ihara pole radius
      - planted_forest_count: number of planted-forest graphs
      - closed_walk_counts: bar-weighted closed walk counts N_1, ..., N_6
    """
    graphs = enumerate_stable_graphs(g, n)

    per_graph = []
    pf_count = 0
    for idx, gamma in enumerate(graphs):
        T = hashimoto_matrix(gamma)
        spec = adjacency_spectrum(gamma)
        poles = find_ihara_zeros(gamma)
        is_pf = is_planted_forest_graph(gamma)
        if is_pf:
            pf_count += 1

        per_graph.append({
            'index': idx,
            'vertices': gamma.num_vertices,
            'edges': gamma.num_edges,
            'first_betti': gamma.first_betti,
            'hashimoto_size': T.shape[0],
            'adjacency_spectrum': spec.tolist(),
            'num_poles': len(poles),
            'min_pole_radius': min(abs(p) for p in poles) if poles else float('inf'),
            'is_ramanujan': is_ramanujan(gamma),
            'is_planted_forest': is_pf,
            'automorphism_order': gamma.automorphism_order(),
        })

    ram_stats = ramanujan_statistics(g, n)

    return {
        'genus': g,
        'n_marked': n,
        'graph_count': len(graphs),
        'per_graph': per_graph,
        'bar_zeta_at_half': bar_graph_zeta_g(g, 0.5),
        'ramanujan_stats': ram_stats,
        'min_pole_radius': min_pole_radius(g, n),
        'planted_forest_count': pf_count,
        'closed_walk_counts': bar_weighted_closed_walks(g, 6, n),
    }
