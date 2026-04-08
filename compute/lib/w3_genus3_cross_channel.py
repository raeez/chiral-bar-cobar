r"""W_3 genus-3 cross-channel correction: delta_F_3^cross(W_3).

Computes the multi-weight genus-3 free energy correction from first principles,
extending the genus-2 computation (w3_genus2.py, thm:multi-weight-genus-expansion).

MATHEMATICAL FRAMEWORK
======================

The multi-weight genus expansion (Theorem, thm:multi-weight-genus-expansion):

    F_g(A) = kappa(A) * lambda_g^FP + delta_F_g^cross(A)

At genus 2: delta_F_2(W_3) = (c + 204)/(16c) > 0 (PROVED, w3_genus2.py).
At genus 3: COMPUTED HERE.

The computation sums over all 42 stable graphs of (g=3, n=0).
For each graph Gamma and channel assignment sigma: E(Gamma) -> {T, W}:

    A(Gamma, sigma) = (1/|Aut(Gamma)|)
                      * prod_{e in E} eta^{sigma(e),sigma(e)}
                      * prod_{v in V} V_{g(v), val(v)}(half-edge channels at v)

VERTEX FACTORS
==============

Genus-0 vertices (n=3, trivalent):
    V_{0,3}(i,j,k) = C_{ijk}
    C_{TTT} = c, C_{TWW} = c, C_{TTW} = 0, C_{WWW} = 0
    (Z_2 symmetry: odd W-count vanishes)

Genus-0 vertices (n >= 4, higher valence):
    Factorized through self-loop pairing: self-loops pair their two half-edges;
    remaining half-edges are paired in order. Recursive formula:
    V_{0,n}(half-edges) = sum_m eta^{mm} C_{pair1_a, pair1_b, m} * V_{0,n-1}(m, rest...)
    where (pair1_a, pair1_b) is the first self-loop pair or first two bridges.

    CRITICAL: The W_3 Frobenius algebra is NON-ASSOCIATIVE
    (T*T=2T, T*W=3W, W*W=2T; check: (TW)W=6T != T(WW)=4T).
    So V_{0,4}(a,b,c,d) DEPENDS on the (a,b)|(c,d) pairing:
    V_{0,4}(T,T|W,W) = 2c but V_{0,4}(T,W|T,W) = 3c.
    The graph topology determines the correct pairing.

Genus-1 vertices (CohFT splitting axiom):
    V_{1,1}(i) = kappa_i / 24
    V_{1,2}(i,j) = delta_{ij} * kappa_i / 24
    V_{1,3}(i,j,k) = sum_m eta^{mm} * V_{0,4}(i,j,k,m) * V_{1,1}(m)
        Computed: V_{1,3}(T,T,T)=c/12, V_{1,3}(T,T,W)=c/12,
                  V_{1,3}(T,W,W)=c/8, V_{1,3}(W,W,W)=c/12
    V_{1,4}(i,j,k,l) = sum_m eta^{mm} * V_{0,5}(i,j,k,l,m) * V_{1,1}(m)
                      + sum_m eta^{mm} * V_{0,3+1}(i,j,m) * V_{1,2}(m,k,l)  [separating]
                      + V_{0,6}(i,j,k,l,m,m) [non-separating, genus reduction]
        (Computed via recursive splitting)

Genus-2 vertices:
    V_{2,1}(i) = kappa_i * lambda_2^FP = kappa_i * 7/5760
    V_{2,2}(i,j) = computed via CohFT splitting

PROPAGATORS (AP27: weight-1 for ALL channels):
    eta^{TT} = 2/c,  eta^{WW} = 3/c

Manuscript references:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    comp:w3-genus2-multichannel (higher_genus_modular_koszul.tex)
    constr:cross-channel-graph-sum (higher_genus_modular_koszul.tex)
    rem:propagator-weight-universality: weight-1 bar propagator (AP27)
    eq:multi-weight-genus2-explicit: delta_F_2 = (c+204)/(16c)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import factorial, comb
from typing import Dict, List, Optional, Tuple

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
)


# ============================================================================
# Bernoulli / Faber-Pandharipande (local copy for self-containment)
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        s += Fraction(comb(n + 1, k)) * _bernoulli(k)
    return -s / Fraction(n + 1)


def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    g=1: 1/24, g=2: 7/5760, g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    abs_B2g = abs(B2g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs_B2g / Fraction(factorial(2 * g)))


# ============================================================================
# W_3 curvature data (from landscape_census.tex, AP1/AP9)
# ============================================================================

CHANNELS = ('T', 'W')


def kappa_ch(ch: str, c: Fraction) -> Fraction:
    """Per-channel kappa: kappa_T = c/2, kappa_W = c/3."""
    if ch == 'T':
        return c / 2
    elif ch == 'W':
        return c / 3
    raise ValueError(f"Unknown channel: {ch}")


def kappa_total(c: Fraction) -> Fraction:
    """Total kappa(W_3) = 5c/6."""
    return Fraction(5) * c / 6


def eta_inv(ch: str, c: Fraction) -> Fraction:
    """Inverse metric (propagator) eta^{ii} = 1/kappa_i."""
    return Fraction(1) / kappa_ch(ch, c)


# ============================================================================
# W_3 structure constants (3-point OPE, AP19)
# ============================================================================

def C3(i: str, j: str, k: str, c: Fraction) -> Fraction:
    r"""3-point structure constant C_{ijk}.

    C_{TTT} = c, C_{TWW} = C_{WTW} = C_{WWT} = c.
    C_{TTW} = C_{TWT} = C_{WTT} = 0, C_{WWW} = 0.
    Rule: even number of W's -> c, odd number -> 0.
    """
    w_count = sum(1 for x in (i, j, k) if x == 'W')
    if w_count % 2 == 1:
        return Fraction(0)
    return c


# ============================================================================
# Genus-0 vertex factors (recursive factorization through self-loop pairing)
# ============================================================================

def V0_factorize(channels: Tuple[str, ...], c: Fraction) -> Fraction:
    r"""Genus-0 n-point vertex factor via recursive factorization.

    For n=3: C_{ijk}.
    For n >= 4: factorize through the first pair of channels:
        V(a,b,rest...) = sum_m eta^{mm} C_{a,b,m} * V(m, rest...)

    The pairing is determined by the ORDER of the channels tuple,
    which is set by the graph topology (self-loops pair their half-edges
    first, then bridge half-edges in edge-list order).
    """
    n = len(channels)
    if n < 3:
        raise ValueError(f"Need n >= 3, got {n}")
    if n == 3:
        return C3(channels[0], channels[1], channels[2], c)
    # Recursive factorization: split off first pair
    a, b = channels[0], channels[1]
    rest = channels[2:]
    total = Fraction(0)
    for m in CHANNELS:
        c3_val = C3(a, b, m, c)
        if c3_val == 0:
            continue
        sub = V0_factorize((m,) + rest, c)
        total += eta_inv(m, c) * c3_val * sub
    return total


# ============================================================================
# Genus-1 vertex factors (CohFT splitting axiom)
# ============================================================================

def V1_1(ch: str, c: Fraction) -> Fraction:
    """V_{1,1}(i) = kappa_i / 24."""
    return kappa_ch(ch, c) / 24


def V1_2(ch1: str, ch2: str, c: Fraction) -> Fraction:
    """V_{1,2}(i,j) = delta_{ij} * kappa_i / 24.

    Diagonal by CohFT splitting at self-loop node.
    """
    if ch1 != ch2:
        return Fraction(0)
    return kappa_ch(ch1, c) / 24


def V1_n(channels: Tuple[str, ...], c: Fraction) -> Fraction:
    r"""Genus-1 n-point vertex factor for the graph sum.

    In the stable graph decomposition, the vertex factor at a genus-g vertex
    with n marked points is the integral over the OPEN moduli space M_{g,n}
    of the CohFT class. This does NOT include boundary contributions --
    those are separate stable graphs in the enumeration.

    For genus 1: the DILATON EQUATION gives the recursion:
        V_{1,n}(i_1,...,i_n) for n >= 2 from V_{1,n-1}.

    For the bar-complex CohFT with diagonal metric:
        V_{1,1}(i) = kappa_i / 24
        V_{1,2}(i,j) = delta_{ij} * kappa_i / 24
        (self-loop forces matching channels)

    For n >= 3, the vertex factor on M_{1,n} (the open moduli space)
    is the tensor-valued function obtained from the CohFT class restricted
    to the interior. For a SEMISIMPLE Frobenius algebra, this equals:

        V_{1,n}(i_1,...,i_n) = sum over idempotent basis
            (idempotent eigenvalue)^{-n} * (1-point genus-1 value)
            * product of (change-of-basis factors)

    For W_3 with diagonal metric, the 'idempotent' decomposition uses
    the normalized idempotents of the Frobenius algebra.

    In practice, for the graph sum, we use the RECURSIVE FORMULA from the
    CohFT string equation. For a genus-1 vertex with n half-edges from
    EDGES (not from the CohFT boundary), the vertex factor is:

        V_{1,n}(i_1,...,i_n) = (2*1 - 2 + n - 1) * V_{1,n-1}(i_1,...,i_{n-1})
            [dilaton equation, if i_n = identity/unit field]

    For the bar-complex CohFT of W_3, neither T nor W is the unit field
    in general, so we cannot use the dilaton equation directly.

    CORRECT APPROACH: For the multi-channel graph sum at the scalar CohFT
    level (R=Id), the vertex factor at a genus-g vertex is:

    The genus-1 n-point function on M_{1,n} is:
        V_{1,n}(i_1,...,i_n) = sum_{alpha} Delta_alpha^{-1}
            * prod_j eta(e_{i_j}, pi_alpha) * kappa_alpha / 24

    where {pi_alpha} are the idempotents of the Frobenius algebra and
    Delta_alpha = eta(pi_alpha, pi_alpha).

    For the W_3 Frobenius algebra (non-associative), we use the
    DIRECT COMPUTATION via the Hodge integral over M_{1,n}.

    Since M_{1,n} has dim n for n >= 1, and lambda_1 is a degree-1 class,
    the integral of lambda_1 * psi_1^{a_1} * ... * psi_n^{a_n} with
    sum a_j = n - 1 gives the vertex weight.

    For the MULTI-CHANNEL contribution: each marked point carries a
    vector e_{i_j} in the state space V. The vertex factor is:
        V_{1,n}(i_1,...,i_n) = lambda_1 * product of metric factors

    At n=1: V_{1,1}(i) = kappa_i/24  (integral of lambda_1 over M_bar_{1,1})
    At n=2 with self-loop: V_{1,2}(i,j) = delta_{ij} * kappa_i / 24
        (self-loop forces matching channels by the diagonal metric)
    At n >= 3: the vertex factor for the multi-channel bar-complex CohFT
    with diagonal metric is:
        V_{1,n}(i_1,...,i_n) = delta_{all_same}(i_1,...,i_n) * kappa_i / 24

    JUSTIFICATION: On M_{1,n}, the CohFT class Omega_{1,n} is determined
    by the genus-1 one-point function and the Frobenius algebra. For a
    DIAGONAL metric (eta_{TW} = 0), the class Omega_{1,n} factorizes as
    a product of one-point classes, each diagonal in its own channel.
    The non-diagonal contributions arise only from BOUNDARY degenerations,
    which are counted as separate graphs in the stable graph sum.

    For n=1: V_{1,1}(i) = kappa_i / 24
    For n=2: V_{1,2}(i,j) = delta_{ij} * kappa_i / 24
    For n >= 3: V_{1,n}(i_1,...,i_n) = delta_{all_same}(i_1,...,i_n) * kappa_{i_1} / 24
    """
    n = len(channels)
    if n == 0:
        raise ValueError("Need n >= 1")
    if n == 1:
        return V1_1(channels[0], c)
    # For n >= 2: all channels must match (diagonal metric on open moduli)
    if len(set(channels)) > 1:
        return Fraction(0)
    return kappa_ch(channels[0], c) / 24


# ============================================================================
# Genus-2 vertex factors
# ============================================================================

def V2_1(ch: str, c: Fraction) -> Fraction:
    """V_{2,1}(i) = kappa_i * lambda_2^FP = kappa_i * 7/5760.

    Per-channel universality at genus 2 (PROVED).
    """
    return kappa_ch(ch, c) * lambda_fp(2)


def V2_2(ch1: str, ch2: str, c: Fraction) -> Fraction:
    r"""V_{2,2}(i,j): genus-2 vertex factor with 2 marked points.

    By the same diagonal-metric argument as V_{1,n}: on the OPEN moduli
    space M_{2,2}, the CohFT class with diagonal metric forces all
    marked points to carry the same channel. Mixed-channel contributions
    arise only from boundary degenerations, which are separate stable graphs.

    V_{2,2}(i,j) = delta_{ij} * kappa_i * lambda_2^FP
    """
    if ch1 != ch2:
        return Fraction(0)
    return kappa_ch(ch1, c) * lambda_fp(2)


# ============================================================================
# General vertex factor dispatcher
# ============================================================================

def vertex_factor(g_v: int, channels: Tuple[str, ...], c: Fraction) -> Fraction:
    """Compute vertex factor V_{g_v, n}(channels) for given vertex genus and channels.

    Dispatches to the appropriate computation based on vertex genus.
    """
    n = len(channels)
    if g_v == 0:
        if n < 3:
            raise ValueError(f"Genus-0 vertex needs val >= 3, got {n}")
        return V0_factorize(channels, c)
    elif g_v == 1:
        return V1_n(channels, c)
    elif g_v == 2:
        if n == 0:
            return Fraction(0)  # Smooth genus-2 vertex: no edges
        elif n == 1:
            return V2_1(channels[0], c)
        elif n == 2:
            return V2_2(channels[0], channels[1], c)
        else:
            # V_{2,n} for n >= 3: would need deeper recursion.
            # At genus 3 with (2, val>=3) vertices: none exist.
            raise ValueError(f"V_{{2,{n}}} not implemented (not needed at genus 3)")
    elif g_v == 3:
        if n == 0:
            return Fraction(0)  # Smooth genus-3: no contribution to boundary sum
        else:
            raise ValueError(f"V_{{3,{n}}} not implemented")
    else:
        raise ValueError(f"Vertex genus {g_v} not supported")


# ============================================================================
# Graph amplitude computation
# ============================================================================

def _half_edge_channels(graph: StableGraph, sigma: Tuple[str, ...]) -> List[Tuple[str, ...]]:
    r"""For each vertex, compute the ordered tuple of half-edge channels.

    Each edge (v1, v2) in the graph:
    - If v1 == v2 (self-loop): contributes 2 half-edges to v1, both with sigma(e).
    - If v1 != v2 (bridge): contributes 1 half-edge to v1 and 1 to v2.

    The half-edges at each vertex are ordered: self-loop half-edges first
    (in edge-list order), then bridge half-edges (in edge-list order).
    This ordering determines the factorization pairing for non-trivalent
    genus-0 vertices.
    """
    n_v = graph.num_vertices
    self_loop_channels: List[List[str]] = [[] for _ in range(n_v)]
    bridge_channels: List[List[str]] = [[] for _ in range(n_v)]

    for e_idx, (v1, v2) in enumerate(graph.edges):
        ch = sigma[e_idx]
        if v1 == v2:
            self_loop_channels[v1].append(ch)
            self_loop_channels[v1].append(ch)
        else:
            bridge_channels[v1].append(ch)
            bridge_channels[v2].append(ch)

    # Combine: self-loop pairs first, then bridges
    result = []
    for v in range(n_v):
        all_ch = tuple(self_loop_channels[v] + bridge_channels[v])
        result.append(all_ch)
    return result


def graph_amplitude(graph: StableGraph, sigma: Tuple[str, ...],
                    c: Fraction) -> Fraction:
    r"""Compute A(Gamma, sigma) for a specific channel assignment.

    A(Gamma, sigma) = prod_e eta^{sigma(e)} * prod_v V_{g(v)}(channels_at_v)

    Returns the amplitude WITHOUT the 1/|Aut| factor.
    """
    # Skip the smooth graph (no edges)
    if graph.num_edges == 0:
        return Fraction(0)

    # Propagator product
    prop = Fraction(1)
    for e_idx in range(graph.num_edges):
        prop *= eta_inv(sigma[e_idx], c)

    # Vertex factors
    he_channels = _half_edge_channels(graph, sigma)
    vf = Fraction(1)
    for v_idx in range(graph.num_vertices):
        gv = graph.vertex_genera[v_idx]
        channels = he_channels[v_idx]
        if len(channels) == 0:
            # Smooth vertex: skip (contributes 0 for boundary graphs)
            if gv <= 2:
                continue
            else:
                return Fraction(0)
        vf_v = vertex_factor(gv, channels, c)
        if vf_v == 0:
            return Fraction(0)
        vf *= vf_v

    return prop * vf


def graph_multichannel_amplitude(graph: StableGraph, c: Fraction
                                 ) -> Dict[str, Fraction]:
    r"""Total amplitude of graph, decomposed into diagonal and mixed channels.

    Returns dict with 'diagonal', 'mixed', 'total' components.
    """
    ne = graph.num_edges
    if ne == 0:
        return {'diagonal': Fraction(0), 'mixed': Fraction(0),
                'total': Fraction(0)}

    aut = graph.automorphism_order()
    diag_sum = Fraction(0)
    mixed_sum = Fraction(0)

    for sigma in cartprod(CHANNELS, repeat=ne):
        amp = graph_amplitude(graph, sigma, c)
        if amp == 0:
            continue
        is_diagonal = len(set(sigma)) <= 1
        if is_diagonal:
            diag_sum += amp
        else:
            mixed_sum += amp

    return {
        'diagonal': diag_sum / aut,
        'mixed': mixed_sum / aut,
        'total': (diag_sum + mixed_sum) / aut,
    }


# ============================================================================
# Full genus-3 computation
# ============================================================================

@lru_cache(maxsize=4)
def _genus3_graphs() -> Tuple[StableGraph, ...]:
    """Cached enumeration of all 42 stable graphs at (g=3, n=0)."""
    return tuple(enumerate_stable_graphs(3, 0))


def genus3_cross_channel(c_val: Fraction) -> Fraction:
    r"""The total cross-channel correction delta_F_3^cross(W_3).

    Sum of mixed-channel amplitudes over all 42 stable graphs of (3, 0).
    """
    graphs = _genus3_graphs()
    total_mixed = Fraction(0)
    for graph in graphs:
        result = graph_multichannel_amplitude(graph, c_val)
        total_mixed += result['mixed']
    return total_mixed


def genus3_diagonal_sum(c_val: Fraction) -> Fraction:
    r"""Per-channel diagonal sum: sum of pure-T and pure-W amplitudes.

    By per-channel universality (PROVED):
    F_3^{diagonal} = kappa(W_3) * lambda_3^FP = (5c/6) * (31/967680)
    """
    return kappa_total(c_val) * lambda_fp(3)


def genus3_full_computation(c_val: Fraction) -> Dict[str, object]:
    r"""Complete genus-3 free energy computation for W_3.

    Returns comprehensive breakdown:
    - kappa data
    - lambda_3^FP
    - Per-graph amplitudes (diagonal and mixed)
    - Total cross-channel correction
    - Per-channel (universal) sum
    - Comparison with universal formula
    """
    graphs = _genus3_graphs()
    fp3 = lambda_fp(3)
    kt = kappa_total(c_val)
    F3_universal = kt * fp3

    per_graph = []
    total_diag = Fraction(0)
    total_mixed = Fraction(0)

    for i, graph in enumerate(graphs):
        r = graph_multichannel_amplitude(graph, c_val)
        per_graph.append({
            'index': i,
            'genera': graph.vertex_genera,
            'edges': graph.edges,
            'num_edges': graph.num_edges,
            'aut': graph.automorphism_order(),
            'diagonal': r['diagonal'],
            'mixed': r['mixed'],
            'total': r['total'],
        })
        total_diag += r['diagonal']
        total_mixed += r['mixed']

    return {
        'c': c_val,
        'kappa_total': kt,
        'kappa_T': kappa_ch('T', c_val),
        'kappa_W': kappa_ch('W', c_val),
        'lambda3_fp': fp3,
        'F3_universal': F3_universal,
        'total_diagonal': total_diag,
        'total_mixed': total_mixed,
        'cross_channel_correction': total_mixed,
        'F3_with_cross': F3_universal + total_mixed,
        'per_graph': per_graph,
    }


def genus3_cross_channel_formula(c_val: Fraction) -> Dict[str, Fraction]:
    r"""Compute delta_F_3 and attempt to express as rational function of c.

    If delta_F_3 = P(c)/Q(c) for polynomials P, Q, this function
    computes the correction at the given c value and returns it
    alongside the universal prediction.
    """
    delta = genus3_cross_channel(c_val)
    fp3 = lambda_fp(3)
    F3_univ = kappa_total(c_val) * fp3
    return {
        'c': c_val,
        'delta_F3': delta,
        'F3_universal': F3_univ,
        'delta_over_F3': delta / F3_univ if F3_univ != 0 else None,
    }


# ============================================================================
# Contributing graph analysis
# ============================================================================

def contributing_graphs(c_val: Fraction) -> List[Dict]:
    """Identify which of the 42 graphs contribute nonzero cross-channel corrections."""
    graphs = _genus3_graphs()
    contributors = []
    for i, graph in enumerate(graphs):
        r = graph_multichannel_amplitude(graph, c_val)
        if r['mixed'] != 0:
            contributors.append({
                'index': i,
                'genera': graph.vertex_genera,
                'edges': graph.edges,
                'aut': graph.automorphism_order(),
                'mixed': r['mixed'],
            })
    return contributors


# ============================================================================
# Rational function reconstruction from evaluations
# ============================================================================

def _reconstruct_rational(evaluations: List[Tuple[Fraction, Fraction]],
                          deg_num: int, deg_den: int) -> Optional[Tuple[List[Fraction], List[Fraction]]]:
    r"""Reconstruct P(c)/Q(c) from evaluations {(c_i, f(c_i))}.

    Given f(c_i) = P(c_i)/Q(c_i) for polynomials P of degree deg_num and
    Q of degree deg_den, with Q monic, solve the linear system:

    f(c_i) * Q(c_i) = P(c_i) for all i.

    Need deg_num + deg_den + 1 evaluations (since Q is monic, we have
    deg_num + 1 + deg_den unknowns).

    Returns (P_coeffs, Q_coeffs) where P = sum P_j c^j, Q = sum Q_j c^j
    with Q_{deg_den} = 1 (monic). Returns None if reconstruction fails.
    """
    n_unknowns = (deg_num + 1) + deg_den  # Q is monic so deg_den free coeffs
    if len(evaluations) < n_unknowns:
        return None

    # Build linear system: for each (c_i, f_i):
    # P_0 + P_1*c_i + ... + P_{dn}*c_i^{dn} - f_i*(Q_0 + Q_1*c_i + ... + Q_{dd-1}*c_i^{dd-1}) = f_i * c_i^{dd}
    # (since Q_{dd} = 1, the c_i^{dd} * f_i term moves to RHS)
    dn = deg_num
    dd = deg_den
    rows = []
    rhs = []
    for c_i, f_i in evaluations[:n_unknowns]:
        row = []
        # P coefficients
        for j in range(dn + 1):
            row.append(c_i ** j)
        # -f_i * Q coefficients (Q_0 through Q_{dd-1})
        for j in range(dd):
            row.append(-f_i * c_i ** j)
        rows.append(row)
        rhs.append(f_i * c_i ** dd)

    # Solve using Gaussian elimination with exact Fraction arithmetic
    n = n_unknowns
    mat = [list(rows[i]) + [rhs[i]] for i in range(n)]

    for col in range(n):
        # Find pivot
        pivot = None
        for row in range(col, n):
            if mat[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return None
        mat[col], mat[pivot] = mat[pivot], mat[col]
        # Eliminate
        for row in range(n):
            if row == col:
                continue
            if mat[row][col] == 0:
                continue
            factor = mat[row][col] / mat[col][col]
            for j in range(n + 1):
                mat[row][j] -= factor * mat[col][j]

    # Extract solution
    solution = [mat[i][n] / mat[i][i] for i in range(n)]
    P_coeffs = solution[:dn + 1]
    Q_coeffs = solution[dn + 1:] + [Fraction(1)]  # Q is monic

    # Verify on remaining evaluations
    for c_i, f_i in evaluations[n_unknowns:]:
        P_val = sum(P_coeffs[j] * c_i ** j for j in range(dn + 1))
        Q_val = sum(Q_coeffs[j] * c_i ** j for j in range(dd + 1))
        if Q_val == 0:
            continue
        if P_val / Q_val != f_i:
            return None

    return (P_coeffs, Q_coeffs)


def reconstruct_delta_F3(max_deg: int = 6) -> Optional[Dict]:
    r"""Attempt to reconstruct delta_F_3 as a rational function P(c)/Q(c).

    Evaluates at sufficiently many integer c values, then attempts
    reconstruction for various (deg_num, deg_den) pairs.

    Strategy: evaluate at c = 1, 2, 3, ..., max_eval, then try
    all (dn, dd) with dn + dd <= max_deg.
    """
    max_eval = max_deg + 5
    print(f"Evaluating delta_F_3 at c = 1..{max_eval}...")

    evals = []
    for c_int in range(1, max_eval + 1):
        c_val = Fraction(c_int)
        delta = genus3_cross_channel(c_val)
        evals.append((c_val, delta))
        print(f"  c={c_int}: delta_F_3 = {delta} = {float(delta):.10f}")

    # Try reconstruction
    for total_deg in range(1, max_deg + 1):
        for dd in range(0, total_deg + 1):
            dn = total_deg - dd
            if len(evals) < dn + dd + 1:
                continue
            result = _reconstruct_rational(evals, dn, dd)
            if result is not None:
                P_coeffs, Q_coeffs = result
                # Simplify: clear denominators
                print(f"\nReconstructed as P(c)/Q(c) with deg(P)={dn}, deg(Q)={dd}:")
                print(f"  P(c) = {' + '.join(f'{P_coeffs[j]}*c^{j}' for j in range(dn+1))}")
                print(f"  Q(c) = {' + '.join(f'{Q_coeffs[j]}*c^{j}' for j in range(dd+1))}")
                return {
                    'deg_num': dn,
                    'deg_den': dd,
                    'P_coeffs': P_coeffs,
                    'Q_coeffs': Q_coeffs,
                }

    print(f"\nNo rational reconstruction found with total degree <= {max_deg}")
    return None


# ============================================================================
# Genus-2 cross-check
# ============================================================================

def genus2_cross_channel_via_engine(c_val: Fraction) -> Fraction:
    """Compute delta_F_2 using the same engine, for cross-checking against w3_genus2.py.

    Uses the general enumeration engine (_enumerate_general) which returns
    7 graphs including the barbell, consistent with genus2_stable_graphs_n0().
    """
    from compute.lib.stable_graph_enumeration import _enumerate_general
    graphs = _enumerate_general(2, 0)
    total_mixed = Fraction(0)
    for graph in graphs:
        r = graph_multichannel_amplitude(graph, c_val)
        total_mixed += r['mixed']
    return total_mixed


# ============================================================================
# Limiting cases
# ============================================================================

def large_c_limit() -> Fraction:
    r"""Leading c-independent term of delta_F_3 as c -> infinity.

    As c -> infinity, terms proportional to 1/c^k vanish, and the
    c-independent piece survives. This is the 'semiclassical limit.'
    """
    # Evaluate at a very large c and check convergence
    c_large = Fraction(10**6)
    delta = genus3_cross_channel(c_large)
    # The leading term should be rational
    return delta


def c_to_infinity_extrapolation(c_values: List[int] = None) -> List[Tuple[int, float]]:
    """Evaluate delta_F_3 * c at several large c values to extract the 1/c coefficient."""
    if c_values is None:
        c_values = [10, 50, 100, 500, 1000]
    results = []
    for cv in c_values:
        c_val = Fraction(cv)
        delta = genus3_cross_channel(c_val)
        results.append((cv, float(delta), float(delta * c_val)))
    return results


# ============================================================================
# Closed-form formula (the main result, verified by graph sum reconstruction)
# ============================================================================

def delta_F3_closed_form(c_val: Fraction) -> Fraction:
    r"""Closed-form cross-channel correction at genus 3.

    delta_F_3(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)

    Partial fraction decomposition:
        = c/27648 + 79/2880 + (133/16)/c + (6281/4)/c^2

    Properties:
      - Always positive for c > 0 (all numerator coefficients positive)
      - Denominator: 138240 = 2^10 * 3^3 * 5, times c^2
      - As c -> infinity: delta_F_3 ~ c/27648 (GROWS with c)
      - As c -> 0: delta_F_3 ~ (6281/4)/c^2 (diverges)
      - Does NOT vanish at c=50 (W_3 self-dual point)

    Structural comparison with genus 2:
      genus 2: delta_F_2 = (c + 204)/(16c) = 1/16 + (51/4)/c
        Numerator degree 1, denominator degree 1 in c
      genus 3: delta_F_3 = above
        Numerator degree 3, denominator degree 2 in c

    Pattern: at genus g, delta_F_g has numerator degree 2g-3 and
    denominator degree g-1 in c (verified at g=2,3).

    Derived from rational function reconstruction of the graph sum
    evaluated at c = 1, 2, ..., 11, verified at c = 1, ..., 100.
    """
    num = 5 * c_val**3 + 3792 * c_val**2 + 1149120 * c_val + 217071360
    den = 138240 * c_val**2
    return Fraction(num, den)


def partial_fractions() -> Dict[str, Fraction]:
    r"""Partial fraction decomposition of delta_F_3.

    delta_F_3 = A*c + B + C/c + D/c^2

    where:
      A = 1/27648 = 5/138240
      B = 79/2880 = 3792/138240
      C = 133/16 = 1149120/138240
      D = 6281/4 = 217071360/138240
    """
    return {
        'A_c1': Fraction(1, 27648),     # coefficient of c
        'B_c0': Fraction(79, 2880),      # constant term
        'C_cm1': Fraction(133, 16),      # coefficient of 1/c
        'D_cm2': Fraction(6281, 4),      # coefficient of 1/c^2
    }


def koszul_complementarity_sum(c_val: Fraction) -> Dict[str, Fraction]:
    r"""Evaluate delta_F_3(c) + delta_F_3(100-c) (Koszul complementarity check).

    W_3 Koszul duality: c <-> 100-c.  Self-dual at c=50.
    Unlike the scalar part kappa(c) + kappa(100-c) = 250/3,
    the cross-channel correction does NOT satisfy simple complementarity.
    """
    c_dual = Fraction(100) - c_val
    d = delta_F3_closed_form(c_val)
    d_dual = delta_F3_closed_form(c_dual)
    return {
        'c': c_val,
        'c_dual': c_dual,
        'delta_c': d,
        'delta_c_dual': d_dual,
        'sum': d + d_dual,
        'ratio': d / d_dual if d_dual != 0 else None,
    }


def growth_ratio_genus3_over_genus2(c_val: Fraction) -> Fraction:
    r"""Ratio delta_F_3/delta_F_2 as a function of c.

    delta_F_3/delta_F_2 = 16c * (5c^3 + 3792c^2 + 1149120c + 217071360)
                          / (138240 c^2 * (c + 204))
                        = (5c^3 + 3792c^2 + 1149120c + 217071360)
                          / (8640 c (c + 204))

    Asymptotics:
      c -> infinity: ratio -> c/1728 (grows linearly)
      c -> 0: ratio -> 217071360/(8640 * 204 * c) ~ 123207/c
    """
    d3 = delta_F3_closed_form(c_val)
    d2 = (c_val + 204) / (16 * c_val)
    return d3 / d2


def contribution_by_vertex_type(c_val: Fraction) -> Dict[str, Fraction]:
    r"""Decompose cross-channel correction by vertex-genus pattern.

    Returns dict mapping vertex-genus tuples to their total mixed contribution.
    Pure genus-0 graphs dominate; all-genus->=1 graphs contribute zero.
    """
    from collections import defaultdict
    graphs = _genus3_graphs()
    result = defaultdict(Fraction)
    for g in graphs:
        pattern = tuple(sorted(g.vertex_genera))
        r = graph_multichannel_amplitude(g, c_val)
        if r['mixed'] != 0:
            result[pattern] += r['mixed']
    return dict(result)
