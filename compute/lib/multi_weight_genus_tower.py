r"""Multi-weight genus tower: delta_F_g^cross(W_3) for g = 2, 3, 4.

MATHEMATICAL PROBLEM
====================

This module certifies the finite-window W_3 two-channel boundary graph
functional at genera g = 2, 3, 4 and nonzero central charge c:

    F_g(A) = kappa(A) * lambda_g^FP + delta_F_g^cross(A)

The scalar Faber-Pandharipande lane is kappa(A) * lambda_g^FP.  The
diagonal boundary graph diagnostic is not substituted for that scalar lane.
For W_3, the mixed-channel correction is already nonzero at genus 2.

This module computes delta_F_g^cross(W_3) for g = 2, 3, 4 by:
  1. Enumerating all stable graphs of M_bar_{g,0}
  2. For each graph, summing over all channel assignments {T, W}^{|E|}
  3. Computing the graph amplitude using W_3 Frobenius data
  4. Extracting the mixed (cross-channel) contribution

The certified genus window is g = 2, 3, 4.  The engine deliberately does
not claim a genus-5 closed formula.

RESULTS
=======

g=2: delta_F_2 = (c + 204) / (16c)
g=3: delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
g=4: delta_F_4 = (287c^4 + 268881c^3 + 115455816c^2 + 29725133760c
                  + 5594347866240) / (17418240 c^3)

Pattern: delta_F_g = P_{d_g}(c) / (D_g * c^{g-1})
  where P has positive coefficients and d_g = deg(P_g):
    d_2 = 1 = 2*2-3, d_3 = 3 = 2*3-3, d_4 = 4 < 2*4-3 = 5.
  Net degree d_g - (g-1): 0 at g=2, 1 at g=3 and g=4.
  Large-c asymptotics: delta_F_g ~ A_g * c for g >= 3 (LINEAR growth).
  The ratio delta_F_g / (kappa*lambda_g) approaches a FINITE NONZERO constant
  as c -> infinity for g >= 3:
    g=3: ratio -> 42/31 ~ 1.35
    g=4: ratio -> 9184/381 ~ 24.1
  The cross-channel correction is comparable to (g=3) or dominates (g=4)
  the scalar part kappa*lambda_g at large c.

Denominators: D_2 = 16 = 2^4, D_3 = 138240 = 2^10*3^3*5,
  D_4 = 17418240 = 2^11*3^5*5*7.

R-MATRIX INPUT: this finite graph functional uses only the W_3 Frobenius
data below and stable-graph combinatorics.  Since T and W have distinct
conformal weights h=2 and h=3, no off-diagonal channel-mixing R-matrix input
appears in this window.

W_3 FROBENIUS DATA
==================

Generators: T (weight 2, Virasoro), W (weight 3, spin-3 current)

Metric (diagonal): eta_{TT} = kappa_T = c/2, eta_{WW} = kappa_W = c/3
Propagator (AP27): eta^{TT} = 2/c, eta^{WW} = 3/c
3-point: C_{TTT} = c, C_{TWW} = c (even W-count); C_{TTW} = C_{WWW} = 0
kappa(W_3) = 5c/6.  Koszul dual: c <-> 100-c, so kappa + kappa' = 250/3.

VERTEX FACTOR RULE
==================

In this finite-window model, the higher-genus open vertex is diagonal:

    V_{g,n}(i_1,...,i_n) = delta_{all_same}(i_1,...,i_n) * kappa_i * lambda_g^FP
        for g >= 1, n >= 1

    V_{0,n}(i_1,...,i_n) computed via recursive factorization through C_{ijk}
        for g = 0, n >= 3

The genus-0 W_3 channel algebra is not crossing invariant in this truncated
two-channel presentation: V_0(T,T|W,W) = 2c while V_0(T,W|T,W) = 3c.
The stable-graph topology fixes the half-edge pairing.  Replacing it by a
scalar or pairing-averaged Faber-Pandharipande lane is a different claim.

References:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    op:multi-generator-universality (higher_genus_foundations.tex)
    rem:propagator-weight-universality (AP27)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from typing import Dict, List, Optional, Tuple

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    genus2_stable_graphs_n0,
    orbifold_euler_characteristic,
    _bernoulli_exact,
    _lambda_fp_exact,
)


CERTIFIED_W3_GENUS_WINDOW: Tuple[int, ...] = (2, 3, 4)

EXPECTED_GRAPH_COUNTS: Dict[int, int] = {2: 7, 3: 42, 4: 379}
EXPECTED_BOUNDARY_COUNTS: Dict[int, int] = {2: 6, 3: 41, 4: 378}
EXPECTED_CHI_ORB: Dict[int, Fraction] = {
    2: Fraction(-1, 1440),
    3: Fraction(-12419, 90720),
    4: Fraction(-4717039, 6220800),
}

CLOSED_FORM_NUMERATOR_COEFFS: Dict[int, Tuple[int, ...]] = {
    2: (1, 204),
    3: (5, 3792, 1149120, 217071360),
    4: (287, 268881, 115455816, 29725133760, 5594347866240),
}
CLOSED_FORM_DENOMINATORS: Dict[int, int] = {
    2: 16,
    3: 138240,
    4: 17418240,
}

FOUR_POINT_PAIRINGS: Dict[str, Tuple[Tuple[int, int], Tuple[int, int]]] = {
    '01|23': ((0, 1), (2, 3)),
    '02|13': ((0, 2), (1, 3)),
    '03|12': ((0, 3), (1, 2)),
}

HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)

MODULAR_KOSZUL_PRIMARY_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br,T_br)",
    "R4_mod(L)",
)

OBJECT_FIREWALL: Dict[str, str] = {
    "A": "input chiral algebra",
    "B(A)": "ordered bar coalgebra before cohomology",
    "A^i": "bar cohomology coalgebra H^*(B(A))",
    "A^!": "Verdier/continuous-linear dual branch",
    "Omega(B(A))": "bar-cobar inversion recovering A",
    "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild/derived-centre bulk",
}


def _require_nonzero_c(c: Fraction) -> Fraction:
    """Normalize c and reject the degenerate W_3 metric."""
    c = Fraction(c)
    if c == 0:
        raise ValueError("W_3 graph amplitudes require nonzero central charge c")
    return c


def _eval_polynomial_desc(coeffs: Tuple[int, ...], x: Fraction) -> Fraction:
    """Evaluate a polynomial whose coefficients are ordered high to low."""
    value = Fraction(0)
    for coeff in coeffs:
        value = value * x + coeff
    return value


def holographic_package_entries() -> Tuple[str, ...]:
    """Seven entries of the holographic package H(A)."""
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_primary_projections() -> Tuple[str, ...]:
    """Six projections of the compute-side modular Koszul package."""
    return MODULAR_KOSZUL_PRIMARY_PROJECTIONS


def object_firewall() -> Dict[str, str]:
    """Typed roles for bar, Verdier dual, inversion, and Hochschild bulk."""
    return dict(OBJECT_FIREWALL)


# ============================================================================
# Faber-Pandharipande numbers
# ============================================================================

@lru_cache(maxsize=32)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    return _lambda_fp_exact(g)


# ============================================================================
# W_3 Frobenius algebra
# ============================================================================

CHANNELS = ('T', 'W')


def kappa_channel(ch: str, c: Fraction) -> Fraction:
    """Per-channel modular characteristic: kappa_T = c/2, kappa_W = c/3."""
    if ch == 'T':
        return c / 2
    elif ch == 'W':
        return c / 3
    raise ValueError(f"Unknown channel: {ch}")


def kappa_total(c: Fraction) -> Fraction:
    """Total kappa(W_3) = 5c/6."""
    return Fraction(5) * c / 6


def propagator(ch: str, c: Fraction) -> Fraction:
    """Inverse metric eta^{ii} = 1/kappa_i."""
    c = _require_nonzero_c(c)
    return Fraction(1) / kappa_channel(ch, c)


def C3(i: str, j: str, k: str, c: Fraction) -> Fraction:
    """3-point structure constant C_{ijk}.

    Z_2 parity: even W-count gives c, odd gives 0.
    C_{TTT} = c, C_{TWW} = c; C_{TTW} = C_{WWW} = 0.
    """
    w_count = sum(1 for x in (i, j, k) if x == 'W')
    if w_count % 2 == 1:
        return Fraction(0)
    return c


# ============================================================================
# Genus-0 vertex factor: recursive factorization
# ============================================================================

@lru_cache(maxsize=None)
def V0_factorize(channels: Tuple[str, ...], c: Fraction) -> Fraction:
    r"""Genus-0 n-point vertex factor via recursive factorization.

    V(a,b,rest...) = sum_m eta^{mm} C_{a,b,m} * V(m, rest...)

    The pairing is determined by the order of the channels tuple,
    set by the graph topology (self-loop half-edges first, then bridges).
    """
    n = len(channels)
    if n < 3:
        raise ValueError(f"Need n >= 3, got {n}")
    if n == 3:
        return C3(channels[0], channels[1], channels[2], c)
    a, b = channels[0], channels[1]
    rest = channels[2:]
    total = Fraction(0)
    for m in CHANNELS:
        c3_val = C3(a, b, m, c)
        if c3_val == 0:
            continue
        sub = V0_factorize((m,) + rest, c)
        total += propagator(m, c) * c3_val * sub
    return total


def V0_four_point_by_pairing(channels: Tuple[str, str, str, str],
                             c: Fraction,
                             pairing: str = '01|23') -> Fraction:
    r"""Genus-0 four-point vertex for a specified binary pairing.

    The three pairings are ``01|23``, ``02|13``, and ``03|12``.  This is
    the explicit firewall against replacing W_3 multi-weight data by an
    associative scalar lane: for (T,T,W,W), ``01|23`` gives 2c while the
    two crossed pairings give 3c.
    """
    c = _require_nonzero_c(c)
    if pairing not in FOUR_POINT_PAIRINGS:
        raise ValueError(f"Unknown four-point pairing: {pairing}")
    (a_idx, b_idx), (d_idx, e_idx) = FOUR_POINT_PAIRINGS[pairing]
    total = Fraction(0)
    for m in CHANNELS:
        left = C3(channels[a_idx], channels[b_idx], m, c)
        if left == 0:
            continue
        right = C3(m, channels[d_idx], channels[e_idx], c)
        if right == 0:
            continue
        total += propagator(m, c) * left * right
    return total


def four_point_pairing_audit(channels: Tuple[str, str, str, str],
                             c: Fraction) -> Dict[str, object]:
    """Evaluate all three genus-0 four-point pairings exactly."""
    values = {
        pairing: V0_four_point_by_pairing(channels, c, pairing)
        for pairing in FOUR_POINT_PAIRINGS
    }
    return {
        'channels': channels,
        'values': values,
        'pairing_independent': len(set(values.values())) == 1,
    }


# ============================================================================
# Higher-genus vertex factors (diagonal metric principle)
# ============================================================================

def Vg_n(gv: int, channels: Tuple[str, ...], c: Fraction) -> Fraction:
    r"""Vertex factor V_{g,n}(channels) for genus g >= 1.

    In the finite-window diagonal open-vertex rule:

        V_{g,n}(i_1,...,i_n) = delta_{all_same} * kappa_i * lambda_g^FP

    For n = 0 (smooth vertex): returns 0 (excluded from boundary sum;
    the smooth scalar FP lane is tracked separately as kappa_total*lambda_g).

    For n >= 1: diagonal in all channels.
    """
    n = len(channels)
    if n == 0:
        return Fraction(0)
    # All channels must match (diagonal metric on open moduli)
    if len(set(channels)) > 1:
        return Fraction(0)
    return kappa_channel(channels[0], c) * lambda_fp(gv)


# ============================================================================
# General vertex factor dispatcher
# ============================================================================

def vertex_factor(gv: int, channels: Tuple[str, ...], c: Fraction) -> Fraction:
    """Compute vertex factor V_{g_v, n}(channels).

    genus 0: recursive factorization through C_{ijk}
    genus >= 1: diagonal metric principle
    """
    n = len(channels)
    if gv == 0:
        if n < 3:
            raise ValueError(f"Genus-0 vertex needs val >= 3, got {n}")
        return V0_factorize(channels, c)
    else:
        return Vg_n(gv, channels, c)


# ============================================================================
# Half-edge channel routing
# ============================================================================

def half_edge_channels(graph: StableGraph, sigma: Tuple[str, ...]) -> List[Tuple[str, ...]]:
    """For each vertex, compute ordered tuple of half-edge channel labels.

    Self-loop half-edges come first (both carry the same channel),
    then bridge half-edges, in edge-list order.
    """
    nv = graph.num_vertices
    self_loop_chs: List[List[str]] = [[] for _ in range(nv)]
    bridge_chs: List[List[str]] = [[] for _ in range(nv)]

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
# Graph amplitude computation
# ============================================================================

def graph_amplitude_single(graph: StableGraph, sigma: Tuple[str, ...],
                           c: Fraction) -> Fraction:
    """Compute A(Gamma, sigma) for a specific channel assignment.

    Returns the amplitude WITHOUT the 1/|Aut| factor.
    Returns 0 if any vertex factor vanishes.
    """
    return _graph_amplitude_single_cached(graph, tuple(sigma), _require_nonzero_c(c))


@lru_cache(maxsize=None)
def _graph_amplitude_single_cached(graph: StableGraph, sigma: Tuple[str, ...],
                                   c: Fraction) -> Fraction:
    """Compute A(Gamma, sigma) for a specific channel assignment.

    Returns the amplitude WITHOUT the 1/|Aut| factor.
    Returns 0 if any vertex factor vanishes.
    """
    if graph.num_edges == 0:
        return Fraction(0)

    # Propagator product
    prop = Fraction(1)
    for e_idx in range(graph.num_edges):
        prop *= propagator(sigma[e_idx], c)

    # Vertex factors
    he_chs = half_edge_channels(graph, sigma)
    vf = Fraction(1)
    for v_idx in range(graph.num_vertices):
        gv = graph.vertex_genera[v_idx]
        chs = he_chs[v_idx]
        if len(chs) == 0:
            # Smooth vertex: no contribution from boundary sum
            continue
        vf_v = vertex_factor(gv, chs, c)
        if vf_v == 0:
            return Fraction(0)
        vf *= vf_v

    return prop * vf


def graph_amplitude_decomposed(graph: StableGraph, c: Fraction
                               ) -> Dict[str, Fraction]:
    """Sum amplitude over all channel assignments, decomposed.

    Returns {diagonal, mixed, total}, all divided by |Aut(Gamma)|.
    """
    diag, mixed, total = _graph_amplitude_decomposed_cached(
        graph, _require_nonzero_c(c))
    return {
        'diagonal': diag,
        'mixed': mixed,
        'total': total,
    }


@lru_cache(maxsize=None)
def _graph_amplitude_decomposed_cached(graph: StableGraph,
                                       c: Fraction
                                       ) -> Tuple[Fraction, Fraction, Fraction]:
    """Cached tuple form for graph_amplitude_decomposed."""
    ne = graph.num_edges
    if ne == 0:
        return Fraction(0), Fraction(0), Fraction(0)

    aut = graph.automorphism_order()
    diag = Fraction(0)
    mixed = Fraction(0)

    for sigma in cartprod(CHANNELS, repeat=ne):
        amp = graph_amplitude_single(graph, sigma, c)
        if amp == 0:
            continue
        if len(set(sigma)) <= 1:
            diag += amp
        else:
            mixed += amp

    diag_aut = diag / aut
    mixed_aut = mixed / aut
    return diag_aut, mixed_aut, diag_aut + mixed_aut


# ============================================================================
# Stable graph enumeration (complete, including barbell at g=2)
# ============================================================================

@lru_cache(maxsize=16)
def stable_graphs_complete(g: int) -> Tuple[StableGraph, ...]:
    """Complete enumeration of stable graphs of M_bar_{g,0}.

    At genus 2, genus2_stable_graphs_n0() returns all 7 graphs
    (including the barbell). For other genera, use the general enumerator.
    """
    if g == 2:
        return tuple(genus2_stable_graphs_n0())
    return tuple(enumerate_stable_graphs(g, 0))


def boundary_graphs(g: int) -> List[StableGraph]:
    """Return only boundary graphs (those with at least one edge)."""
    return [gr for gr in stable_graphs_complete(g) if gr.num_edges > 0]


# ============================================================================
# Cross-channel correction at each genus
# ============================================================================

@lru_cache(maxsize=None)
def cross_channel_correction(g: int, c: Fraction) -> Fraction:
    """Compute delta_F_g^cross(W_3) at genus g and central charge c.

    delta_F_g^cross = sum over boundary graphs of mixed-channel amplitudes.
    """
    c = _require_nonzero_c(c)
    total_mixed = Fraction(0)
    for gr in boundary_graphs(g):
        r = graph_amplitude_decomposed(gr, c)
        total_mixed += r['mixed']
    return total_mixed


def full_amplitude_decomposition(g: int, c: Fraction) -> Dict[str, object]:
    """Full decomposition of F_g(W_3) into per-channel and cross-channel parts.

    Returns diagnostic information about the boundary computation.  The
    diagonal term is a boundary diagnostic, not the scalar FP lane.
    """
    c = _require_nonzero_c(c)
    bnd_graphs = boundary_graphs(g)

    diag = Fraction(0)
    mixed = Fraction(0)
    per_graph = []

    for i, gr in enumerate(bnd_graphs):
        r = graph_amplitude_decomposed(gr, c)
        diag += r['diagonal']
        mixed += r['mixed']
        per_graph.append({
            'index': i,
            'genera': gr.vertex_genera,
            'edges': len(gr.edges),
            'aut': gr.automorphism_order(),
            'diagonal': r['diagonal'],
            'mixed': r['mixed'],
            'total': r['total'],
        })

    return {
        'genus': g,
        'c': c,
        'graphs_total': len(stable_graphs_complete(g)),
        'graphs_boundary': len(bnd_graphs),
        'diagonal': diag,
        'mixed': mixed,
        'scalar_fp_lane': kappa_total(c) * lambda_fp(g),
        'kappa_lambda': kappa_total(c) * lambda_fp(g),
        'per_graph': per_graph,
    }


# ============================================================================
# Genus tower computation
# ============================================================================

def genus_tower(c: Fraction, max_genus: int = 4) -> Dict[int, Dict[str, object]]:
    """Compute the multi-weight genus tower delta_F_g^cross for g = 2..max_genus."""
    c = _require_nonzero_c(c)
    return {g: full_amplitude_decomposition(g, c) for g in range(2, max_genus + 1)}


def cross_channel_tower(c: Fraction, max_genus: int = 4) -> Dict[int, Fraction]:
    """Extract just the cross-channel corrections delta_F_g^cross."""
    c = _require_nonzero_c(c)
    return {g: cross_channel_correction(g, c) for g in range(2, max_genus + 1)}


# ============================================================================
# Closed-form formulas (derived from graph sum computation)
# ============================================================================

def delta_F2_closed_form(c: Fraction) -> Fraction:
    """Closed form: delta_F_2(W_3) = (c + 204) / (16c)."""
    return delta_Fg_closed_form(2, c)


def delta_F3_closed_form(c: Fraction) -> Fraction:
    """Closed form: delta_F_3(W_3) = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2).

    Derived from the 42-graph sum via Newton interpolation.
    Verified at c = 1, 2, 4, 10, 26, 50.
    """
    return delta_Fg_closed_form(3, c)


def delta_F4_closed_form(c: Fraction) -> Fraction:
    r"""Closed form: delta_F_4(W_3).

    Numerator: 287c^4 + 268881c^3 + 115455816c^2 + 29725133760c + 5594347866240
    Denominator: 17418240 c^3

    Derived from the 379-graph sum via Newton interpolation (degree 4 polynomial
    in the numerator, confirmed by forward differences vanishing at order 5).
    Verified at c = 1, 2, ..., 20 (all 20 integer points match graph sum).

    Denominator constant: 17418240 = 2^11 * 3^5 * 5 * 7.
    Leading coefficient: 287/17418240 = 41/2488320 (since gcd(287,17418240) = 7).
    Large-c asymptotics: delta_F_4 ~ (41/2488320) * c (linear growth, same as g=3).
    """
    return delta_Fg_closed_form(4, c)


def delta_Fg_closed_form(g: int, c: Fraction) -> Fraction:
    """Closed form P_g(c)/(D_g c^{g-1}) in the certified window g=2,3,4."""
    c = _require_nonzero_c(c)
    if g not in CERTIFIED_W3_GENUS_WINDOW:
        raise ValueError(f"Certified W_3 closed forms only for g={CERTIFIED_W3_GENUS_WINDOW}")
    numerator = _eval_polynomial_desc(CLOSED_FORM_NUMERATOR_COEFFS[g], c)
    denominator = CLOSED_FORM_DENOMINATORS[g] * c ** (g - 1)
    return numerator / denominator


def scaled_numerator_from_graph_sum(g: int, c: Fraction) -> Fraction:
    """Return D_g c^{g-1} delta_F_g^cross(c) from the direct graph sum."""
    c = _require_nonzero_c(c)
    if g not in CERTIFIED_W3_GENUS_WINDOW:
        raise ValueError(f"Certified W_3 scaled numerators only for g={CERTIFIED_W3_GENUS_WINDOW}")
    return cross_channel_correction(g, c) * CLOSED_FORM_DENOMINATORS[g] * c ** (g - 1)


def _poly_add_asc(p: List[Fraction], q: List[Fraction]) -> List[Fraction]:
    n = max(len(p), len(q))
    out = [Fraction(0)] * n
    for i in range(n):
        if i < len(p):
            out[i] += p[i]
        if i < len(q):
            out[i] += q[i]
    return out


def _poly_mul_asc(p: List[Fraction], q: List[Fraction]) -> List[Fraction]:
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def interpolate_scaled_numerator(g: int,
                                 c_values: Optional[Tuple[Fraction, ...]] = None
                                 ) -> Tuple[Fraction, ...]:
    """Interpolate P_g(c) from exact graph sums.

    Returns coefficients ordered high-to-low.  This is an exact oracle for
    the hardcoded constants, because the inputs are the direct stable-graph
    sums rather than the closed-form functions.
    """
    if g not in CERTIFIED_W3_GENUS_WINDOW:
        raise ValueError(f"Certified W_3 interpolation only for g={CERTIFIED_W3_GENUS_WINDOW}")
    degree = len(CLOSED_FORM_NUMERATOR_COEFFS[g]) - 1
    if c_values is None:
        c_values = tuple(Fraction(i) for i in range(1, degree + 2))
    if len(c_values) != degree + 1:
        raise ValueError(f"Need {degree + 1} interpolation points for genus {g}")

    points = [
        (_require_nonzero_c(c), scaled_numerator_from_graph_sum(g, c))
        for c in c_values
    ]
    poly = [Fraction(0)]
    for i, (x_i, y_i) in enumerate(points):
        basis = [Fraction(1)]
        denom = Fraction(1)
        for j, (x_j, _) in enumerate(points):
            if i == j:
                continue
            basis = _poly_mul_asc(basis, [-x_j, Fraction(1)])
            denom *= x_i - x_j
        poly = _poly_add_asc(poly, [coef * y_i / denom for coef in basis])
    return tuple(reversed(poly))


# ============================================================================
# Verification functions
# ============================================================================

def verify_genus2(c: Fraction) -> Dict[str, object]:
    """Verify delta_F2 from graph sum matches closed form."""
    c = _require_nonzero_c(c)
    computed = cross_channel_correction(2, c)
    closed = delta_F2_closed_form(c)
    return {
        'c': c,
        'computed': computed,
        'closed_form': closed,
        'match': computed == closed,
    }


def verify_genus3(c: Fraction) -> Dict[str, object]:
    """Verify delta_F3 from graph sum matches closed form."""
    c = _require_nonzero_c(c)
    computed = cross_channel_correction(3, c)
    closed = delta_F3_closed_form(c)
    return {
        'c': c,
        'computed': computed,
        'closed_form': closed,
        'match': computed == closed,
    }


def verify_genus4(c: Fraction) -> Dict[str, object]:
    """Verify delta_F4 from graph sum matches closed form."""
    c = _require_nonzero_c(c)
    computed = cross_channel_correction(4, c)
    closed = delta_F4_closed_form(c)
    return {
        'c': c,
        'computed': computed,
        'closed_form': closed,
        'match': computed == closed,
    }


def per_channel_check(g: int, c: Fraction) -> Dict[str, object]:
    """Compare diagonal boundary diagnostics with scalar FP channel lanes.

    The all-i boundary sum is not asserted to equal kappa_i * lambda_g^FP.
    Equality flags are returned explicitly to block accidental collapse of
    the boundary diagnostic onto the scalar lane.
    """
    c = _require_nonzero_c(c)
    fpg = lambda_fp(g)
    diag_T = Fraction(0)
    diag_W = Fraction(0)

    for gr in boundary_graphs(g):
        ne = gr.num_edges
        if ne == 0:
            continue
        aut = gr.automorphism_order()
        # All-T assignment
        sigma_T = tuple(['T'] * ne)
        amp_T = graph_amplitude_single(gr, sigma_T, c)
        diag_T += amp_T / aut
        # All-W assignment
        sigma_W = tuple(['W'] * ne)
        amp_W = graph_amplitude_single(gr, sigma_W, c)
        diag_W += amp_W / aut

    expected_T = kappa_channel('T', c) * fpg
    expected_W = kappa_channel('W', c) * fpg
    return {
        'boundary_T': diag_T,
        'boundary_W': diag_W,
        'expected_T': expected_T,
        'expected_W': expected_W,
        'kappa_T_lambda': expected_T,
        'kappa_W_lambda': expected_W,
        'match_T': diag_T == expected_T,
        'match_W': diag_W == expected_W,
        'diagonal_boundary': diag_T + diag_W,
        'scalar_fp_lane': kappa_total(c) * fpg,
        'diagonal_boundary_is_scalar_lane': (diag_T + diag_W) == kappa_total(c) * fpg,
    }


def koszul_duality_check(g: int, c: Fraction) -> Dict[str, object]:
    """Koszul duality: W_3 at c <-> W_3 at 100-c.

    kappa(c) + kappa(100-c) = 250/3.
    """
    c = _require_nonzero_c(c)
    c_dual = Fraction(100) - c
    if c_dual <= 0:
        return {'c': c, 'c_dual': c_dual, 'note': 'dual has c <= 0'}

    delta_c = cross_channel_correction(g, c)
    delta_dual = cross_channel_correction(g, c_dual)

    return {
        'c': c,
        'c_dual': c_dual,
        'kappa_sum': kappa_total(c) + kappa_total(c_dual),
        'kappa_sum_expected': Fraction(250, 3),
        'delta_c': delta_c,
        'delta_dual': delta_dual,
        'delta_sum': delta_c + delta_dual,
    }


def chi_orb_check(g: int) -> Dict[str, object]:
    """Verify orbifold Euler characteristic from graph enumeration.

    At genus 2, the complete 7-graph enumeration (including barbell) gives
    chi^orb(M-bar_{2,0}) = -1/1440.
    """
    graphs = list(stable_graphs_complete(g))
    try:
        chi = orbifold_euler_characteristic(graphs)
    except ValueError:
        chi = None

    return {
        'genus': g,
        'graph_count': len(graphs),
        'chi_computed': chi,
        'chi_expected': EXPECTED_CHI_ORB.get(g),
        'match': chi == EXPECTED_CHI_ORB.get(g),
    }


def genus2_mixed_graph_contributions(c: Fraction) -> Dict[str, Fraction]:
    """Graph-by-graph genus-2 mixed terms with automorphism factors included."""
    c = _require_nonzero_c(c)
    names = (
        'irreducible_self_node',
        'banana_double_self_loop',
        'separating_genus1_bridge',
        'theta_three_bridge',
        'lollipop_self_loop_bridge',
        'barbell_two_self_loops_bridge',
    )
    return {
        name: graph_amplitude_decomposed(graph, c)['mixed']
        for name, graph in zip(names, boundary_graphs(2))
    }


def uniform_weight_cross_channel_correction(g: int, c: Fraction) -> Fraction:
    """One-channel scalar lane has no mixed channel assignments."""
    _require_nonzero_c(c)
    if g < 1:
        raise ValueError(f"Genus must be positive, got {g}")
    return Fraction(0)


def finite_window_theorem(g: int, c: Fraction) -> Dict[str, object]:
    """Exact certificate for the W_3 finite graph window g = 2, 3, 4."""
    c = _require_nonzero_c(c)
    if g not in CERTIFIED_W3_GENUS_WINDOW:
        raise ValueError(f"Certified W_3 finite window is {CERTIFIED_W3_GENUS_WINDOW}")
    decomp = full_amplitude_decomposition(g, c)
    chi = chi_orb_check(g)
    direct = decomp['mixed']
    closed = delta_Fg_closed_form(g, c)
    scalar_lane = kappa_total(c) * lambda_fp(g)
    per_channel = per_channel_check(g, c)
    return {
        'genus': g,
        'c': c,
        'certified_genus_window': CERTIFIED_W3_GENUS_WINDOW,
        'graphs_total': len(stable_graphs_complete(g)),
        'graphs_total_expected': EXPECTED_GRAPH_COUNTS[g],
        'graphs_total_match': len(stable_graphs_complete(g)) == EXPECTED_GRAPH_COUNTS[g],
        'graphs_boundary': len(boundary_graphs(g)),
        'graphs_boundary_expected': EXPECTED_BOUNDARY_COUNTS[g],
        'graphs_boundary_match': len(boundary_graphs(g)) == EXPECTED_BOUNDARY_COUNTS[g],
        'chi_orb': chi['chi_computed'],
        'chi_orb_expected': chi['chi_expected'],
        'chi_orb_match': chi['match'],
        'lambda_fp': lambda_fp(g),
        'scalar_fp_lane': scalar_lane,
        'cross_channel': direct,
        'cross_channel_closed': closed,
        'graph_matches_closed': direct == closed,
        'full_free_energy': scalar_lane + direct,
        'diagonal_boundary_diagnostic': decomp['diagonal'],
        'diagonal_boundary_is_scalar_lane': per_channel['diagonal_boundary_is_scalar_lane'],
        'per_channel': per_channel,
        'holographic_package_entries': holographic_package_entries(),
        'modular_koszul_primary_projections': modular_koszul_primary_projections(),
        'object_firewall': object_firewall(),
    }


# ============================================================================
# R-matrix independence
# ============================================================================

def r_matrix_independence_note() -> str:
    """The finite-window graph functional has no off-diagonal R input.

    T and W have different conformal weights (h=2 and h=3), so R does not
    mix channels in this two-channel window. The correction computed here is
    determined by the Frobenius data and graph combinatorics.
    """
    return (
        "In the certified W_3 finite window, delta_F_g^cross uses no off-diagonal "
        "R-matrix input: T and W have different conformal weights h=2 and h=3."
    )


# ============================================================================
# Pattern analysis
# ============================================================================

def analyze_denominator_structure(max_genus: int = 4) -> Dict[int, Dict[str, object]]:
    """Analyze the rational function structure of delta_F_g at each genus.

    Uses Newton interpolation to find the closed-form rational function.
    """
    results = {}
    for g in range(2, max_genus + 1):
        # Collect data at integer c values
        data = {}
        n_points = 2 * (2 * g - 3) + 5  # enough for interpolation
        for cv in range(1, n_points + 1):
            delta = cross_channel_correction(g, Fraction(cv))
            data[cv] = delta

        # Check: c^{g-1} * delta should be polynomial
        # Compute c^{g-1} * delta values
        scaled = {cv: delta * Fraction(cv) ** (g - 1) for cv, delta in data.items()}

        # Find common denominator
        from math import lcm
        from functools import reduce
        denoms = [scaled[cv].denominator for cv in sorted(scaled)]
        L = reduce(lcm, denoms)
        int_vals = [int(scaled[cv] * L) for cv in sorted(scaled)]

        # Forward differences to find polynomial degree
        diffs = [list(int_vals)]
        poly_degree = None
        for order in range(1, len(int_vals)):
            new_diffs = [diffs[-1][i + 1] - diffs[-1][i] for i in range(len(diffs[-1]) - 1)]
            diffs.append(new_diffs)
            if all(d == 0 for d in new_diffs):
                poly_degree = order - 1
                break

        results[g] = {
            'denom_c_power': g - 1,
            'numerator_degree': poly_degree,
            'denom_constant': L,
            'pattern_2g_minus_3': (poly_degree == 2 * g - 3 if poly_degree else None),
            'newton_coefficients': [d[0] for d in diffs[:poly_degree + 1]] if poly_degree else None,
        }
    return results


if __name__ == '__main__':
    import sys

    print("=" * 70)
    print("Multi-weight genus tower: delta_F_g^cross(W_3)")
    print("=" * 70)
    print()

    c = Fraction(26)
    print(f"Central charge c = {c}")
    print(f"kappa(W_3) = {kappa_total(c)} = {float(kappa_total(c)):.4f}")
    print()

    for g in range(2, 5):
        print(f"--- Genus {g} ---")
        dec = full_amplitude_decomposition(g, c)
        print(f"  Graphs: {dec['graphs_total']} total, {dec['graphs_boundary']} boundary")
        print(f"  Mixed (cross-channel): {dec['mixed']} = {float(dec['mixed']):.10f}")
        print(f"  kappa * lambda_{g}: {dec['kappa_lambda']} = {float(dec['kappa_lambda']):.10f}")
        print()

    print("Closed-form verification:")
    print(f"  g=2: match = {verify_genus2(c)['match']}")
    print(f"  g=3: match = {verify_genus3(c)['match']}")
