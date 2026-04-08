r"""Delta_F_4 engine: genus-4 cross-channel correction for W_N algebras.

MATHEMATICAL PROBLEM
====================

The full genus expansion for a multi-weight modular Koszul algebra is:

    F_g(A) = kappa(A) * lambda_g^FP + delta_F_g^cross(A)

For UNIFORM-WEIGHT algebras, delta_F_g^cross = 0 (PROVED).
For MULTI-WEIGHT algebras like W_N (N >= 3), delta_F_g^cross != 0.

This engine computes delta_F_4^{grav}(W_N, c) for arbitrary N and c by:
  1. Enumerating all 379 stable graphs of M_bar_{4,0} (378 boundary)
  2. For each graph, summing over channel assignments {2, 3, ..., N}^{|E|}
  3. Computing graph amplitudes using the gravitational Frobenius algebra
  4. Extracting the mixed (cross-channel) contribution
  5. Fitting the polynomial structure in c and N via interpolation

GRAVITATIONAL FROBENIUS ALGEBRA FOR W_N
========================================

Channels: T (weight 2), W_3 (weight 3), ..., W_N (weight N)
Metric: eta_{jj} = c/j  (diagonal)
Propagator: eta^{jj} = j/c  (AP27: bar propagator is weight 1)
3-point: C_{2,2,2} = c; C_{2,j,j} = c for j >= 3; all others = 0
Higher-genus vertex: V_{g,n}(j,...,j) = (c/j) * lambda_g^FP (diagonal)
Higher-genus mixed vertex: V_{g,n}(mixed channels) = 0

KEY OPTIMIZATION: The 3-point coupling structure severely constrains
which channel assignments give nonzero amplitudes:
  - At every genus-0 vertex, the channels form a valid factorization
    through TTT and TW_jW_j couplings only.
  - At every genus >= 1 vertex, all half-edges carry the same channel.
  - This allows aggressive pruning of the channel assignment space.

POWER SUM STRUCTURE
===================

The W_N correction factors through symmetric functions of generator
weights {2, 3, ..., N}. The power sums S_k = sum_{j=2}^{N} j^k
appear naturally in the graph sum:

  S_0 = N - 1  (number of generators)
  S_1 = H(N) - 1 = sum_{j=2}^N 1/j  (harmonic, but wait: S_1 = 2+3+...+N)
  S_k = 2^k + 3^k + ... + N^k

Actually, the propagator j/c and metric c/j produce power sums:
  sum_j (j/c)^a * (c/j)^b = c^{b-a} * sum_j j^{a-b} = c^{b-a} * S_{a-b}

DEGREE PATTERN (from genus 2, 3, 4 for W_3)
=============================================

For W_3: delta_F_g = P_g(c) / (D_g * c^{g-1})

  g=2: P_2 = c + 204,  D_2 = 16
  g=3: P_3 = 5c^3 + 3792c^2 + 1149120c + 217071360,  D_3 = 138240
  g=4: P_4 = 287c^4 + 268881c^3 + 115455816c^2
            + 29725133760c + 5594347866240,  D_4 = 17418240

Pattern: d_g = g for g >= 3, net degree e_g = 1 (linear in c at large c).

For general W_N:
  delta_F_g(W_N, c) = sum_{k=0}^{g-1} A_{g,k}(N) / c^k

  where A_{g,k}(N) are polynomials in N.

At genus 4:
  delta_F_4(W_N, c) = E_4(N)*c + D_4(N) + C_4(N)/c + B_4(N)/c^2 + A_4(N)/c^3

MATRIX MODEL IDENTIFICATION
=============================

At genus 2: A_2(N) = (2*S_1^2 + S_2 - 12) / 4 where S_k are power sums
of weights {2,...,N}. A Penner-type matrix model with potential
V(x) = -sum_{j=2}^{N} log(1 - x/j) generates these power sums.

References:
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    op:multi-generator-universality (higher_genus_foundations.tex, RESOLVED NEGATIVELY)
    theorem_delta_f3_universal_engine.py (genus-3 template)
    rectification_delta_f2_verify_engine.py (genus-2 template)
    stable_graph_enumeration.py (StableGraph)
    AP27: bar propagator d log E(z,w) has weight 1
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import factorial, gcd
from typing import Dict, List, Optional, Tuple

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
)


# ============================================================================
# Section 1: Exact arithmetic primitives (independent implementations)
# ============================================================================

@lru_cache(maxsize=64)
def bernoulli_number(n: int) -> Fraction:
    """Exact Bernoulli number B_n via Akiyama-Tanigawa algorithm."""
    if n < 0:
        raise ValueError(f"Bernoulli number requires n >= 0, got {n}")
    a = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        a[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


@lru_cache(maxsize=32)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number at genus g.

    lambda_g^FP = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

    Verified values:
      g=1: 1/24
      g=2: 7/5760
      g=3: 31/967680
      g=4: 127/154828800
    """
    if g < 1:
        raise ValueError(f"lambda_FP requires g >= 1, got {g}")
    B2g = bernoulli_number(2 * g)
    abs_B2g = abs(B2g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs_B2g / Fraction(factorial(2 * g))


def power_sum(k: int, N: int) -> Fraction:
    """Power sum S_k(N) = sum_{j=2}^{N} j^k.

    These are the power-sum symmetric functions of the weight set {2,...,N}.
    """
    return sum(Fraction(j) ** k for j in range(2, N + 1))


# ============================================================================
# Section 2: Gravitational Frobenius algebra for W_N
# ============================================================================

def grav_C3(i: int, j: int, k: int, c: Fraction) -> Fraction:
    """Gravitational 3-point structure constant C^{grav}_{ijk}.

    Non-vanishing couplings:
      C_{2,2,2} = c        (TTT)
      C_{2,j,j} = c        (T W_j W_j) for j >= 3
    All others vanish.

    Parity selection: odd-weight channel count must be even.
    """
    odd_count = sum(1 for w in (i, j, k) if w % 2 == 1)
    if odd_count % 2 == 1:
        return Fraction(0)
    triple = tuple(sorted((i, j, k)))
    if triple == (2, 2, 2):
        return c
    if triple[0] == 2 and triple[1] == triple[2] and triple[1] >= 3:
        return c
    return Fraction(0)


def grav_propagator(weight: int, c: Fraction) -> Fraction:
    """Inverse metric eta^{jj} = j/c (AP27)."""
    return Fraction(weight) / c


def grav_kappa_channel(weight: int, c: Fraction) -> Fraction:
    """Per-channel modular characteristic kappa_j = c/j."""
    return c / Fraction(weight)


def grav_kappa_total(N: int, c: Fraction) -> Fraction:
    """Total kappa(W_N) = sum_{j=2}^{N} c/j = c * (H_N - 1)."""
    return sum(c / Fraction(j) for j in range(2, N + 1))


# ============================================================================
# Section 3: Vertex factors
# ============================================================================

def grav_V0_factorize(channels: Tuple[int, ...], c: Fraction,
                      all_weights: Tuple[int, ...]) -> Fraction:
    r"""Genus-0 n-point vertex factor via recursive factorization.

    V_0(a, b, rest...) = sum_m eta^{mm} * C_{a,b,m} * V_0(m, rest...)
    Base case n=3: V_0(a,b,c) = C_{abc}.
    """
    n = len(channels)
    if n < 3:
        raise ValueError(f"Genus-0 vertex needs n >= 3, got {n}")
    if n == 3:
        return grav_C3(channels[0], channels[1], channels[2], c)

    a, b = channels[0], channels[1]
    rest = channels[2:]
    total = Fraction(0)
    for m in all_weights:
        c3 = grav_C3(a, b, m, c)
        if c3 == 0:
            continue
        sub_val = grav_V0_factorize((m,) + rest, c, all_weights)
        if sub_val == 0:
            continue
        total += grav_propagator(m, c) * c3 * sub_val
    return total


def grav_vertex_factor(gv: int, channels: Tuple[int, ...], c: Fraction,
                       all_weights: Tuple[int, ...]) -> Fraction:
    """Vertex factor V_{g,n}(channels).

    g >= 1: diagonal principle (all channels must match).
      V_{g,n}(j,...,j) = kappa_j * lambda_g^FP = (c/j) * lambda_g
      V_{g,n}(mixed) = 0

    g = 0: recursive Frobenius factorization.
    """
    n = len(channels)
    if n == 0:
        return Fraction(0)
    if gv == 0:
        if n < 3:
            raise ValueError(f"Genus-0 vertex needs n >= 3, got {n}")
        return grav_V0_factorize(channels, c, all_weights)
    else:
        if len(set(channels)) > 1:
            return Fraction(0)
        return grav_kappa_channel(channels[0], c) * lambda_fp(gv)


# ============================================================================
# Section 4: Half-edge channel routing
# ============================================================================

def half_edge_channels(graph: StableGraph, sigma: Tuple[int, ...]
                       ) -> List[Tuple[int, ...]]:
    """Compute per-vertex half-edge channel assignments.

    Self-loop half-edges come FIRST (both carry the same channel),
    then bridge half-edges, in edge-list order. This ordering matches
    the authority engine (multi_weight_genus_tower.py) and matters for
    the recursive V0_factorize which pairs channels sequentially.
    """
    nv = graph.num_vertices
    self_loop_chs: List[List[int]] = [[] for _ in range(nv)]
    bridge_chs: List[List[int]] = [[] for _ in range(nv)]
    for e_idx, (v1, v2) in enumerate(graph.edges):
        ch = sigma[e_idx]
        if v1 == v2:
            self_loop_chs[v1].append(ch)
            self_loop_chs[v1].append(ch)
        else:
            bridge_chs[v1].append(ch)
            bridge_chs[v2].append(ch)
    return [tuple(self_loop_chs[v] + bridge_chs[v]) for v in range(nv)]


# ============================================================================
# Section 5: Graph amplitude computation
# ============================================================================

def graph_amplitude_raw(graph: StableGraph, sigma: Tuple[int, ...],
                        c: Fraction, all_weights: Tuple[int, ...]) -> Fraction:
    """Raw amplitude A(Gamma, sigma) WITHOUT the 1/|Aut| factor."""
    ne = graph.num_edges
    if ne == 0:
        return Fraction(0)

    he_chs = half_edge_channels(graph, sigma)

    # Propagator product
    prop = Fraction(1)
    for e_idx in range(ne):
        prop *= grav_propagator(sigma[e_idx], c)

    # Vertex factors
    vf = Fraction(1)
    for v_idx in range(graph.num_vertices):
        gv = graph.vertex_genera[v_idx]
        chs = he_chs[v_idx]
        if len(chs) == 0:
            continue
        vf_v = grav_vertex_factor(gv, chs, c, all_weights)
        if vf_v == 0:
            return Fraction(0)
        vf *= vf_v

    return prop * vf


def graph_amplitude_decomposed(graph: StableGraph, c: Fraction,
                               all_weights: Tuple[int, ...]
                               ) -> Dict[str, Fraction]:
    """Sum amplitude over all channel assignments, split diagonal/mixed.

    Divides by |Aut(Gamma)|.
    """
    ne = graph.num_edges
    if ne == 0:
        return {'diagonal': Fraction(0), 'mixed': Fraction(0),
                'total': Fraction(0)}

    aut = graph.automorphism_order()
    diag = Fraction(0)
    mixed = Fraction(0)

    for sigma in cartprod(all_weights, repeat=ne):
        amp = graph_amplitude_raw(graph, sigma, c, all_weights)
        if amp == 0:
            continue
        if len(set(sigma)) <= 1:
            diag += amp
        else:
            mixed += amp

    return {
        'diagonal': diag / aut,
        'mixed': mixed / aut,
        'total': (diag + mixed) / aut,
    }


# ============================================================================
# Section 6: Fast graph amplitude with structural pre-filtering
# ============================================================================

def _precompute_graph_structure(graph: StableGraph):
    """Pre-analyze a graph for fast channel assignment filtering.

    Returns:
        vertex_edge_map: for each vertex, list of (edge_idx, is_self_loop) pairs
        higher_genus_vertices: set of vertex indices with g >= 1
        genus0_vertices: set of vertex indices with g == 0
    """
    nv = graph.num_vertices
    vertex_edges = [[] for _ in range(nv)]  # (edge_idx, is_self_loop)

    for e_idx, (v1, v2) in enumerate(graph.edges):
        if v1 == v2:
            vertex_edges[v1].append((e_idx, True))
        else:
            vertex_edges[v1].append((e_idx, False))
            vertex_edges[v2].append((e_idx, False))

    hg_verts = {v for v in range(nv) if graph.vertex_genera[v] >= 1}
    g0_verts = {v for v in range(nv) if graph.vertex_genera[v] == 0}

    return vertex_edges, hg_verts, g0_verts


def _check_vertex_parity(graph: StableGraph, sigma: Tuple[int, ...],
                         vertex_edges, g0_verts) -> bool:
    """Fast check: at each genus-0 vertex, each non-T channel appears even times.

    This is a necessary condition for nonzero amplitude from the gravitational
    Frobenius algebra. The 3-point couplings C_{i,j,k} are nonzero only for
    (2,2,2) and (2,j,j), so non-T channels must pair up at each vertex.
    """
    for v in g0_verts:
        counts = {}
        for e_idx, is_self_loop in vertex_edges[v]:
            ch = sigma[e_idx]
            if ch != 2:
                mult = 2 if is_self_loop else 1
                counts[ch] = counts.get(ch, 0) + mult
        for ch, cnt in counts.items():
            if cnt % 2 != 0:
                return False
    return True


def _check_hg_vertex_diag(graph: StableGraph, sigma: Tuple[int, ...],
                          vertex_edges, hg_verts) -> bool:
    """Fast check: at each higher-genus vertex, all incident edges same channel."""
    for v in hg_verts:
        channels_at_v = set()
        for e_idx, is_self_loop in vertex_edges[v]:
            channels_at_v.add(sigma[e_idx])
        if len(channels_at_v) > 1:
            return False
    return True


def graph_amplitude_fast(graph: StableGraph, c: Fraction,
                         all_weights: Tuple[int, ...]) -> Dict[str, Fraction]:
    """Fast amplitude computation with structural pre-filtering.

    Uses two pre-filters before computing the expensive vertex factors:
    1. Higher-genus diagonality: all edges at g>=1 vertices must match
    2. Genus-0 parity: each non-T channel appears even times at g=0 vertices

    These filters eliminate ~90% of channel assignments before any Fraction
    arithmetic.
    """
    ne = graph.num_edges
    if ne == 0:
        return {'diagonal': Fraction(0), 'mixed': Fraction(0),
                'total': Fraction(0)}

    vertex_edges, hg_verts, g0_verts = _precompute_graph_structure(graph)
    aut = graph.automorphism_order()
    diag = Fraction(0)
    mixed = Fraction(0)

    for sigma in cartprod(all_weights, repeat=ne):
        # Fast integer checks before expensive Fraction computation
        if hg_verts and not _check_hg_vertex_diag(graph, sigma, vertex_edges, hg_verts):
            continue
        if g0_verts and not _check_vertex_parity(graph, sigma, vertex_edges, g0_verts):
            continue

        amp = graph_amplitude_raw(graph, sigma, c, all_weights)
        if amp == 0:
            continue
        if len(set(sigma)) <= 1:
            diag += amp
        else:
            mixed += amp

    return {
        'diagonal': diag / aut,
        'mixed': mixed / aut,
        'total': (diag + mixed) / aut,
    }


# ============================================================================
# Section 7: Genus-4 stable graph enumeration
# ============================================================================

@lru_cache(maxsize=1)
def genus4_graphs() -> Tuple[StableGraph, ...]:
    """All 379 stable graphs of M_bar_{4,0}."""
    return tuple(enumerate_stable_graphs(4, 0))


def genus4_boundary_graphs() -> List[StableGraph]:
    """The 378 boundary stable graphs (edges >= 1)."""
    return [g for g in genus4_graphs() if g.num_edges > 0]


# ============================================================================
# Section 8: Core delta_F_4 computation
# ============================================================================

def delta_F4_grav_graph_sum(N: int, c: Fraction) -> Fraction:
    """Compute delta_F_4^{grav}(W_N, c) by summing over all 378 boundary graphs.

    Args:
        N: rank of W_N algebra (channels are {2, 3, ..., N})
        c: central charge (Fraction)

    Returns:
        delta_F_4^{grav}(W_N, c) as exact Fraction
    """
    if N < 2:
        raise ValueError(f"Need N >= 2, got {N}")
    if N == 2:
        # Virasoro: uniform weight, delta = 0
        return Fraction(0)

    all_weights = tuple(range(2, N + 1))
    graphs = genus4_boundary_graphs()

    total_mixed = Fraction(0)
    for graph in graphs:
        decomp = graph_amplitude_fast(graph, c, all_weights)
        total_mixed += decomp['mixed']

    return total_mixed


def delta_F4_per_graph(N: int, c: Fraction) -> List[Dict]:
    """Per-graph decomposition of delta_F_4^{grav}(W_N, c).

    Returns a list of dicts with graph info and amplitude decomposition.
    """
    all_weights = tuple(range(2, N + 1))
    graphs = genus4_boundary_graphs()

    result = []
    for i, graph in enumerate(graphs):
        decomp = graph_amplitude_fast(graph, c, all_weights)
        decomp['index'] = i
        decomp['genera'] = graph.vertex_genera
        decomp['edges'] = graph.num_edges
        decomp['aut'] = graph.automorphism_order()
        decomp['vertices'] = graph.num_vertices
        result.append(decomp)

    return result


# ============================================================================
# Section 9: Genus-2 and genus-3 for cross-validation
# ============================================================================

def delta_F2_grav_graph_sum(N: int, c: Fraction) -> Fraction:
    """Compute delta_F_2^{grav}(W_N, c) via genus-2 graph sum.

    Uses the 7 stable graphs of M_bar_{2,0}.
    """
    if N == 2:
        return Fraction(0)
    all_weights = tuple(range(2, N + 1))
    graphs = list(enumerate_stable_graphs(2, 0))
    # Add barbell if not present (the general enumerator may miss it)
    barbell = StableGraph(
        vertex_genera=(0, 0),
        edges=((0, 0), (0, 1), (1, 1)),
        legs=(),
    )
    # Check if barbell is already there by canonical form
    has_barbell = any(
        g.vertex_genera == (0, 0) and len(g.edges) == 3
        and sum(1 for e in g.edges if e[0] == e[1]) == 2
        for g in graphs
    )
    if not has_barbell:
        graphs.append(barbell)

    total_mixed = Fraction(0)
    for graph in graphs:
        if graph.num_edges == 0:
            continue
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        total_mixed += decomp['mixed']
    return total_mixed


def delta_F3_grav_graph_sum(N: int, c: Fraction) -> Fraction:
    """Compute delta_F_3^{grav}(W_N, c) via genus-3 graph sum."""
    if N == 2:
        return Fraction(0)
    all_weights = tuple(range(2, N + 1))
    graphs = enumerate_stable_graphs(3, 0)

    total_mixed = Fraction(0)
    for graph in graphs:
        if graph.num_edges == 0:
            continue
        decomp = graph_amplitude_decomposed(graph, c, all_weights)
        total_mixed += decomp['mixed']
    return total_mixed


# ============================================================================
# Section 10: Newton interpolation for c-polynomial extraction
# ============================================================================

def newton_interpolate(values: Dict[Fraction, Fraction],
                       degree: int) -> List[Fraction]:
    """Lagrange interpolation: fit polynomial of given degree to (x, f(x)) data.

    Input: values = {x_i: f(x_i)} with len >= degree + 1.
    Output: coefficients [a_d, a_{d-1}, ..., a_0] of a_d*x^d + ... + a_0.

    Uses the Vandermonde system.
    """
    points = sorted(values.keys())
    if len(points) < degree + 1:
        raise ValueError(f"Need {degree + 1} points, got {len(points)}")

    # Use first degree+1 points
    xs = points[:degree + 1]
    fs = [values[x] for x in xs]

    # Build Vandermonde matrix and solve via Gaussian elimination
    n = degree + 1
    # Augmented matrix: row i = [x_i^d, x_i^{d-1}, ..., x_i^0, f_i]
    mat = []
    for i in range(n):
        row = [xs[i] ** (degree - j) for j in range(n)] + [fs[i]]
        mat.append(row)

    # Gaussian elimination
    for col in range(n):
        # Find pivot
        pivot_row = None
        for row in range(col, n):
            if mat[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            raise ValueError("Singular Vandermonde matrix")
        mat[col], mat[pivot_row] = mat[pivot_row], mat[col]

        # Eliminate below
        for row in range(col + 1, n):
            if mat[row][col] != 0:
                factor = mat[row][col] / mat[col][col]
                for j in range(col, n + 1):
                    mat[row][j] -= factor * mat[col][j]

    # Back substitution
    coeffs = [Fraction(0)] * n
    for row in range(n - 1, -1, -1):
        val = mat[row][n]
        for j in range(row + 1, n):
            val -= mat[row][j] * coeffs[j]
        coeffs[row] = val / mat[row][row]

    return coeffs


def extract_c_polynomial_genus4(N: int, num_points: int = 7) -> Dict:
    """Extract the c-polynomial structure of delta_F_4(W_N, c).

    delta_F_4(W_N, c) = E*c + D + C/c + B/c^2 + A/c^3

    where E, D, C, B, A depend on N.

    We compute delta_F_4 at num_points values of c and fit.
    The polynomial in x = 1/c has degree g-1 = 3 with net degree 1,
    so in c we have terms from c^1 down to c^{-3}: 5 coefficients.

    Returns dict with 'E', 'D', 'C', 'B', 'A' and verification data.
    """
    # Compute at several c values
    c_values = [Fraction(k) for k in range(1, num_points + 1)]
    raw_values = {}
    for cv in c_values:
        raw_values[cv] = delta_F4_grav_graph_sum(N, cv)

    # The function delta_F_4(c) = E*c + D + C/c + B/c^2 + A/c^3
    # Substitute x = 1/c: delta_F_4 = E/x + D + C*x + B*x^2 + A*x^3
    # Multiply by x: x * delta_F_4 = E + D*x + C*x^2 + B*x^3 + A*x^4
    # This is a degree-4 polynomial in x = 1/c.

    # Alternatively: delta_F_4(c) * c^3 = E*c^4 + D*c^3 + C*c^2 + B*c + A
    # This is a degree-4 polynomial in c.
    # Interpolate P(c) = delta_F_4(c) * c^3 as a polynomial of degree 4 in c.

    poly_values = {}
    for cv in c_values:
        poly_values[cv] = raw_values[cv] * cv ** 3

    # Interpolate: P(c) = E*c^4 + D*c^3 + C*c^2 + B*c + A
    # Need 5 points minimum. Use all available for overdetermination.
    coeffs = newton_interpolate(poly_values, 4)
    E, D, C, B, A = coeffs  # from highest to lowest power

    # Verify: check at additional c values
    verification = {}
    for cv in c_values:
        predicted = E * cv**4 + D * cv**3 + C * cv**2 + B * cv + A
        actual_poly = raw_values[cv] * cv**3
        verification[int(cv)] = {
            'predicted': predicted,
            'actual': actual_poly,
            'match': predicted == actual_poly,
        }

    return {
        'N': N,
        'E': E,  # coefficient of c (leading at large c)
        'D': D,  # constant term
        'C': C,  # coefficient of 1/c
        'B': B,  # coefficient of 1/c^2
        'A': A,  # coefficient of 1/c^3
        'raw_values': raw_values,
        'verification': verification,
        'all_verified': all(v['match'] for v in verification.values()),
    }


# ============================================================================
# Section 11: Lagrange interpolation in N
# ============================================================================

def lagrange_interpolate_N(values: Dict[int, Fraction],
                           max_degree: int) -> List[Fraction]:
    """Fit a polynomial in N to data {N_i: f(N_i)}.

    Returns coefficients [a_d, ..., a_0] of a_d*N^d + ... + a_0.
    Tries degrees from 0 up to max_degree; returns the lowest degree
    that fits all data points exactly.
    """
    ns = sorted(values.keys())
    fs = [values[n] for n in ns]

    for deg in range(min(max_degree + 1, len(ns))):
        frac_values = {Fraction(n): f for n, f in zip(ns, fs)}
        try:
            coeffs = newton_interpolate(frac_values, deg)
        except (ValueError, ZeroDivisionError):
            continue

        # Verify at all points
        all_match = True
        for n, f in zip(ns, fs):
            val = sum(coeffs[i] * Fraction(n) ** (deg - i) for i in range(deg + 1))
            if val != f:
                all_match = False
                break
        if all_match:
            return coeffs

    # Fall back to max degree fit
    frac_values = {Fraction(n): f for n, f in zip(ns, fs)}
    return newton_interpolate(frac_values, min(max_degree, len(ns) - 1))


def extract_N_polynomials(c_poly_data: Dict[int, Dict],
                          max_N_degree: int = 10) -> Dict:
    """From c-polynomial coefficients at several N values, extract N-polynomials.

    Input: c_poly_data = {N: {E, D, C, B, A}} for several N values.
    Output: polynomial formulas for E(N), D(N), C(N), B(N), A(N).
    """
    labels = ['E', 'D', 'C', 'B', 'A']
    result = {}

    for label in labels:
        values = {N: data[label] for N, data in c_poly_data.items()}

        # All should vanish at N=2 (Virasoro is uniform weight)
        if 2 in values:
            assert values[2] == 0, f"{label}(N=2) = {values[2]} != 0"

        coeffs = lagrange_interpolate_N(values, max_N_degree)
        degree = len(coeffs) - 1

        # Verify
        verified = {}
        for N, expected in values.items():
            computed = sum(coeffs[i] * Fraction(N) ** (degree - i)
                          for i in range(degree + 1))
            verified[N] = {'expected': expected, 'computed': computed,
                           'match': computed == expected}

        result[label] = {
            'degree': degree,
            'coefficients': coeffs,
            'formula_string': _poly_string(coeffs, 'N'),
            'verified': verified,
            'all_match': all(v['match'] for v in verified.values()),
        }

    return result


def _poly_string(coeffs: List[Fraction], var: str) -> str:
    """Format a polynomial as a human-readable string."""
    degree = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        if c == 0:
            continue
        power = degree - i
        if power == 0:
            terms.append(str(c))
        elif power == 1:
            if c == 1:
                terms.append(var)
            elif c == -1:
                terms.append(f'-{var}')
            else:
                terms.append(f'{c}*{var}')
        else:
            if c == 1:
                terms.append(f'{var}^{power}')
            elif c == -1:
                terms.append(f'-{var}^{power}')
            else:
                terms.append(f'{c}*{var}^{power}')
    return ' + '.join(terms) if terms else '0'


# ============================================================================
# Section 12: Known closed-form formulas for cross-validation
# ============================================================================

def delta_F2_closed_form_W3(c: Fraction) -> Fraction:
    """Known: delta_F_2(W_3, c) = (c + 204) / (16c)."""
    return (c + 204) / (16 * c)


def delta_F3_closed_form_W3(c: Fraction) -> Fraction:
    """Known: delta_F_3(W_3, c)."""
    return (5 * c**3 + 3792 * c**2 + 1149120 * c + 217071360) / (138240 * c**2)


def delta_F4_closed_form_W3(c: Fraction) -> Fraction:
    """Known: delta_F_4(W_3, c)."""
    return (287 * c**4 + 268881 * c**3 + 115455816 * c**2
            + 29725133760 * c + 5594347866240) / (17418240 * c**3)


# ============================================================================
# Section 13: Matrix model identification (Penner model)
# ============================================================================

def penner_potential_coefficients(N: int, max_order: int = 6) -> List[Fraction]:
    r"""Coefficients of the Penner potential V(x) = -sum_{j=2}^{N} log(1 - x/j).

    Taylor expansion: V(x) = sum_{k=1}^{inf} (1/k) * S_{-k}(N) * x^k
    where S_{-k}(N) = sum_{j=2}^{N} j^{-k}.

    Actually V(x) = sum_{j=2}^{N} sum_{k>=1} x^k / (k * j^k)
                  = sum_{k>=1} (x^k / k) * sum_{j=2}^{N} j^{-k}
                  = sum_{k>=1} (x^k / k) * H_k^{(N)}

    where H_k^{(N)} = sum_{j=2}^{N} 1/j^k (partial harmonic-like sums).

    Returns [V_1, V_2, ..., V_{max_order}] = coefficients of x, x^2, ..., x^{max_order}.
    """
    coeffs = []
    for k in range(1, max_order + 1):
        Hk = sum(Fraction(1, j**k) for j in range(2, N + 1))
        coeffs.append(Hk / k)
    return coeffs


def penner_free_energy_genus2(N: int) -> Dict[str, Fraction]:
    r"""Genus-2 free energy of the Penner matrix model with eigenvalues at {2,...,N}.

    The Penner model for a matrix M with potential
      V(M) = -sum_{j=2}^{N} Tr log(I - M/j)
    has eigenvalue density supported near x=0 (weak coupling).

    At genus 2, the free energy involves the moments
      m_k = (1/N_eff) * sum_{j=2}^{N} j^{-k}  (where N_eff = N-1 = number of eigenvalues)

    The genus-2 free energy of a one-cut matrix model is:
      F_2 = (1/240) * [5*m_2^2 + 4*m_2*m_4/(m_2) + ...] (Eynard formula)

    This is a HEURISTIC computation. The comparison with delta_F_2 tests
    whether the Penner model reproduces the W_N correction.

    For now, compute the power sums and report them.
    """
    S = {}
    for k in range(-4, 5):
        S[k] = sum(Fraction(j) ** k for j in range(2, N + 1))

    # From the delta_F_2 engine:
    # delta_F_2(W_N, c) = B_2(N) + A_2(N)/c
    # where B_2(N) = (N-2)(N+3)/96  and  A_2(N) = (N-2)(3N^3+14N^2+22N+33)/24

    B2_formula = Fraction(N - 2) * Fraction(N + 3) / 96
    A2_formula = Fraction(N - 2) * (3 * N**3 + 14 * N**2 + 22 * N + 33) / 24

    # Express in terms of power sums S_k = 2^k + ... + N^k
    # S_1 = 2 + 3 + ... + N = N(N+1)/2 - 1
    # S_2 = 2^2 + 3^2 + ... + N^2 = N(N+1)(2N+1)/6 - 1
    # S_0 = N - 1

    S0 = Fraction(N - 1)
    S1 = Fraction(N * (N + 1), 2) - 1
    S2 = Fraction(N * (N + 1) * (2 * N + 1), 6) - 1

    # Test: can A_2 be expressed as a polynomial in S_k?
    # A_2 = (N-2)(3N^3+14N^2+22N+33)/24
    # Try: A_2 = alpha * S_1^2 + beta * S_2 + gamma * S_0 + delta

    # The actual formula from the delta_F_2 engine (for W_3 -> N=3):
    # delta_F_2(W_3,c) = (c+204)/(16c) = 1/16 + 204/(16c) = 1/16 + 51/(4c)
    # At N=3: B_2 = 1*6/96 = 1/16. Check.
    #         A_2 = 1*(81+126+66+33)/24 = 306/24 = 51/4. Check.

    # Power sums for N=3: S_1=5, S_2=13, S_0=2
    # S_1^2=25, S_2=13
    # 2*S_1^2 + S_2 - 12 = 50+13-12 = 51. So A_2 = 51/4 = (2*25+13-12)/4.
    # General: A_2 = (2*S_1^2 + S_2 - 12) / 4?

    A2_power_sum = (2 * S1**2 + S2 - 12) / 4

    return {
        'N': N,
        'B2_formula': B2_formula,
        'A2_formula': A2_formula,
        'S0': S0,
        'S1': S1,
        'S2': S2,
        'A2_from_power_sums': A2_power_sum,
        'A2_match': A2_formula == A2_power_sum,
    }


# ============================================================================
# Section 14: Full pipeline: compute, extract, identify
# ============================================================================

def full_pipeline(N_values: Tuple[int, ...] = (2, 3, 4, 5),
                  c_points: int = 7) -> Dict:
    """Run the full delta_F_4 pipeline for given N values.

    1. Compute delta_F_4(W_N, c) at c = 1, ..., c_points for each N
    2. Extract c-polynomial coefficients E, D, C, B, A for each N
    3. Fit N-polynomials to each coefficient
    4. Verify at all data points

    Returns complete results dictionary.
    """
    c_poly_data = {}
    for N in N_values:
        c_poly_data[N] = extract_c_polynomial_genus4(N, num_points=c_points)

    N_polys = extract_N_polynomials(c_poly_data)

    return {
        'c_polynomial_data': c_poly_data,
        'N_polynomials': N_polys,
        'N_values': N_values,
    }


# ============================================================================
# Section 15: Degree pattern verification
# ============================================================================

def verify_degree_pattern_genus4(N: int) -> Dict:
    """Verify that delta_F_4 has the expected degree pattern.

    Expected: delta_F_4(W_N, c) = E*c + D + C/c + B/c^2 + A/c^3
    i.e., numerator degree = 4, denominator = c^3, net degree = 1.
    """
    result = extract_c_polynomial_genus4(N)

    # Check: polynomial is exactly degree 4 in c
    # (when multiplied by c^3)
    # This means: c^5 coefficient is zero (no c^2 term in delta_F_4)
    # Verify by checking that degree-5 interpolation gives 0 leading coeff

    c_values = [Fraction(k) for k in range(1, 8)]
    poly5_values = {}
    for cv in c_values:
        poly5_values[cv] = result['raw_values'][cv] * cv**3

    try:
        coeffs5 = newton_interpolate(poly5_values, 5)
        leading_is_zero = (coeffs5[0] == 0)
    except (ValueError, ZeroDivisionError):
        leading_is_zero = None

    return {
        'N': N,
        'E': result['E'],
        'D': result['D'],
        'C': result['C'],
        'B': result['B'],
        'A': result['A'],
        'all_c_verified': result['all_verified'],
        'degree_5_leading_zero': leading_is_zero,
        'matches_pattern': result['all_verified'] and (leading_is_zero is True),
    }


# ============================================================================
# Section 16: Cross-genus consistency checks
# ============================================================================

def cross_genus_check_W3(c: Fraction) -> Dict:
    """Verify delta_F_g(W_3, c) at g = 2, 3, 4 against closed forms."""
    results = {}

    # Genus 2
    computed_2 = delta_F2_grav_graph_sum(3, c)
    closed_2 = delta_F2_closed_form_W3(c)
    results['g2'] = {
        'computed': computed_2,
        'closed_form': closed_2,
        'match': computed_2 == closed_2,
    }

    # Genus 3
    computed_3 = delta_F3_grav_graph_sum(3, c)
    closed_3 = delta_F3_closed_form_W3(c)
    results['g3'] = {
        'computed': computed_3,
        'closed_form': closed_3,
        'match': computed_3 == closed_3,
    }

    # Genus 4
    computed_4 = delta_F4_grav_graph_sum(3, c)
    closed_4 = delta_F4_closed_form_W3(c)
    results['g4'] = {
        'computed': computed_4,
        'closed_form': closed_4,
        'match': computed_4 == closed_4,
    }

    return results


def virasoro_vanishing_check(g: int, c: Fraction) -> Dict:
    """Verify delta_F_g(W_2, c) = 0 (Virasoro is uniform weight)."""
    if g == 2:
        val = delta_F2_grav_graph_sum(2, c)
    elif g == 3:
        val = delta_F3_grav_graph_sum(2, c)
    elif g == 4:
        val = delta_F4_grav_graph_sum(2, c)
    else:
        raise ValueError(f"Only g=2,3,4 supported, got {g}")

    return {
        'genus': g,
        'c': c,
        'value': val,
        'is_zero': val == 0,
    }
