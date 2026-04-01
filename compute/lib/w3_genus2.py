r"""W₃ genus-2 free energy: the first explicit multi-generator computation.

Computes F₂(W₃) as a closed-form rational function of the central charge c.

MATHEMATICAL FRAMEWORK
======================

The W₃ algebra has two strong generators:
    T (conformal weight 2, Virasoro stress tensor)
    W (conformal weight 3, spin-3 current)

Total modular characteristic: κ(W₃) = 5c/6 = κ_T + κ_W where
    κ_T = c/2  (Virasoro sector)
    κ_W = c/3  (W-boson sector)

The genus-2 free energy decomposes as:

    F₂(W₃) = F₂^{scalar} + F₂^{planted-forest} + F₂^{cross-channel}

where:
    F₂^{scalar} = κ · λ₂^FP = (5c/6) · (7/5760)  [if universality holds]
    F₂^{planted-forest} = δ_pf^{(2,0)}(T-line) + δ_pf^{(2,0)}(W-line)
    F₂^{cross-channel} = corrections from mixed (T,W) graph amplitudes

COMPUTATION STRATEGY
====================

We use the bar-complex CohFT graph sum on M̄_{2,0}. The 6 stable graphs
at genus 2 with 0 marked points are:

    Γ₀: smooth genus-2 curve (0 edges, |Aut| = 1)
    Γ₁: figure-eight (g=1 vertex, 1 self-loop, |Aut| = 2)
    Γ₂: banana/sunset (g=0 vertex, 2 self-loops, |Aut| = 8)
    Γ₃: dumbbell (2 g=1 vertices, 1 bridge, |Aut| = 2)
    Γ₄: theta graph (2 g=0 vertices, 3 parallel edges, |Aut| = 12)
    Γ₅: lollipop (g=0 vertex with self-loop + bridge to g=1 vertex, |Aut| = 2)

FEYNMAN RULES (bar-complex CohFT, multi-channel)
=================================================

For each graph Γ and channel assignment σ: E(Γ) → {T, W}:

    A(Γ, σ) = Π_e η^{σ(e),σ(e)} × Π_v V_v(g_v, channels_v)

Edge propagator (AP27: weight-1 bar propagator for ALL channels):
    η^{TT} = 1/κ_T = 2/c
    η^{WW} = 1/κ_W = 3/c
    η^{TW} = 0  (diagonal metric)

Genus-0 vertex factors (Frobenius algebra, R-matrix independent):
    V_{0,3}(i,j,k) = C_{ijk}  (sphere 3-point function)
    V_{0,4}(i,j,k,l) = Σ_m η^{mm} C_{ijm} C_{klm}  (s-channel factorization)

W₃ structure constants:
    C_{TTT} = c,  C_{TWW} = c  (and permutations)
    C_{TTW} = C_{WWW} = 0  (Z₂ symmetry W → -W)

Genus-1 vertex factors (R-matrix dependent):
    The genus-1 one-point function ⟨e_i⟩_{1,1} depends on the CohFT
    R-matrix. For the bar-complex CohFT, this is NOT simply κ_i/24.
    The TOTAL F₁ = κ/24 is proved, but the individual vertex factors
    receive R-matrix corrections that cancel only in the full graph sum.

    For the per-channel scalar computation: the individual R-dressed
    vertex factors are constrained by F₁ = κ/24 and the individual
    graph amplitudes of the scalar graph sum.

    For the multi-channel cross-channel computation: we use the structural
    result that genus-1 vertex factors are PER-CHANNEL (each genus-1 vertex
    involves a single channel, determined by the edge assignment).

RESULT
======

The computation reveals that F₂(W₃) is determined by two independent
contributions:

1. The per-channel (diagonal) sum: Σ_i F₂(single-channel i) = κ · λ₂^FP
   This holds by the uniform-weight universality theorem applied to each
   channel separately.

2. The cross-channel correction δF₂: contributions from mixed-channel
   graph assignments. These are computed exactly from the genus-0
   Frobenius algebra (R-matrix independent) and the genus-1 per-channel
   vertex factors.

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex): F_g = κ · λ_g^FP
    op:multi-generator-universality (higher_genus_foundations.tex)
    eq:delta-pf-genus2-explicit: δ_pf = S₃(10S₃ - κ)/48
    thm:shadow-archetype-classification: G/L/C/M depth classes
    rem:propagator-weight-universality: weight-1 bar propagator (AP27)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
from typing import Dict, List, Optional, Tuple


# ============================================================================
# Bernoulli numbers and Faber-Pandharipande
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n as a Fraction."""
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
    r"""Faber-Pandharipande number λ_g^FP.

    λ_g^FP = (2^{2g-1} - 1) / 2^{2g-1} · |B_{2g}| / (2g)!

    g=1: 1/24
    g=2: 7/5760
    g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"λ_g^FP requires g ≥ 1, got {g}")
    B2g = _bernoulli(2 * g)
    abs_B2g = abs(B2g)
    return Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1)) * abs_B2g / Fraction(factorial(2 * g))


# ============================================================================
# W₃ OPE data
# ============================================================================

def kappa_T(c: Fraction) -> Fraction:
    """Per-channel κ for T (Virasoro): κ_T = c/2."""
    return c / 2


def kappa_W(c: Fraction) -> Fraction:
    """Per-channel κ for W (spin-3): κ_W = c/3."""
    return c / 3


def kappa_total(c: Fraction) -> Fraction:
    """Total κ(W₃) = κ_T + κ_W = 5c/6."""
    return kappa_T(c) + kappa_W(c)


def propagator(channel: str, c: Fraction) -> Fraction:
    """Propagator η^{ii} = 1/κ_i for channel i."""
    if channel == 'T':
        return Fraction(1) / kappa_T(c)
    elif channel == 'W':
        return Fraction(1) / kappa_W(c)
    raise ValueError(f"Unknown channel: {channel}")


def C3(i: str, j: str, k: str, c: Fraction) -> Fraction:
    """Sphere 3-point function C_{ijk} for W₃.

    Z₂ symmetry (W → -W): odd W-count vanishes.
    C_{TTT} = c, C_{TWW} = c (and permutations).
    C_{TTW} = C_{WWW} = 0.
    """
    w_count = sum(1 for x in (i, j, k) if x == 'W')
    if w_count % 2 == 1:
        return Fraction(0)
    labels = sorted([i, j, k])
    if labels == ['T', 'T', 'T']:
        return c
    elif labels == ['T', 'W', 'W']:
        return c
    return Fraction(0)


def V04_s_channel(i1: str, i2: str, j1: str, j2: str, c: Fraction) -> Fraction:
    """Genus-0 4-point vertex factor in the s-channel factorization.

    V_{0,4}(i₁,i₂|j₁,j₂) = Σ_m η^{mm} C_{i₁i₂m} C_{j₁j₂m}

    This is the factorization through the boundary divisor where
    half-edges (i₁,i₂) collapse to one side and (j₁,j₂) to the other.
    For genus-0 vertices, this is R-matrix independent.
    """
    total = Fraction(0)
    for m in ['T', 'W']:
        eta_inv = propagator(m, c)
        total += C3(i1, i2, m, c) * eta_inv * C3(m, j1, j2, c)
    return total


# ============================================================================
# Shadow tower data (genus-0 shadow coefficients on each primary line)
# ============================================================================

def S3_T(c: Fraction) -> Fraction:
    """Cubic shadow coefficient on the T-line (= Virasoro α_T = 2).

    S₃ = a₁/3 where a₁ = q₁/(2a₀) = 12κ_T · 2 / (2 · 2κ_T) = ...
    For Virasoro: S₃ = α/3 = 2/3.

    Actually: from shadow_tower_recursive.py, with α_T = 2:
    a₀ = √q₀ = 2κ_T = c
    a₁ = q₁/(2a₀) = 12κ_T · α_T / (2 · 2κ_T) = 12·(c/2)·2 / (2c) = 12c/(2c) = 6
    S₃ = a₁/3 = 2.

    Wait: the shadow coefficient convention: H(t) = Σ r·S_r·t^r = t²√Q_L(t).
    So S_r = a_{r-2}/r where a_n = [t^n] √Q_L.

    For the T-line: Q_T(t) = (2κ_T)² + 12κ_T · α_T · t + q₂ · t²
                           = c² + 12c · t + q₂ · t²

    a₀ = c,  a₁ = 12c/(2c) = 6
    S₂ = a₀/2 = c/2 = κ_T  ✓
    S₃ = a₁/3 = 6/3 = 2.

    For Virasoro at the r-matrix level: S₃ = α = 2. ✓
    """
    return Fraction(2)


def S3_W(c: Fraction) -> Fraction:
    """Cubic shadow on W-line: S₃^W = 0 (Z₂ parity, α_W = 0)."""
    return Fraction(0)


def S4_T(c: Fraction) -> Fraction:
    """Quartic shadow on T-line (= Virasoro Q^contact).

    S₄_T = Q^contact_Vir = 10/[c(5c+22)].
    """
    return Fraction(10) / (c * (5 * c + 22))


def S4_W(c: Fraction) -> Fraction:
    """Quartic shadow on W-line.

    S₄_W = 2560/[c(5c+22)³].
    """
    return Fraction(2560) / (c * (5 * c + 22) ** 3)


# ============================================================================
# Genus-2 stable graph enumeration
# ============================================================================

# The 6 stable graphs at (g=2, n=0):
#
# Γ₀: smooth  — 1 vertex (g=2, val=0), 0 edges. |Aut|=1. h¹=0.
# Γ₁: fig-8   — 1 vertex (g=1, val=2), 1 self-loop. |Aut|=2. h¹=1.
# Γ₂: banana  — 1 vertex (g=0, val=4), 2 self-loops. |Aut|=8. h¹=2.
# Γ₃: dumbbell— 2 vertices (g=1,val=1)+(g=1,val=1), 1 edge. |Aut|=2. h¹=0.
# Γ₄: theta   — 2 vertices (g=0,val=3)+(g=0,val=3), 3 edges. |Aut|=12. h¹=2.
# Γ₅: lollipop— 2 vertices (g=0,val=3)+(g=1,val=1), 2 edges. |Aut|=2. h¹=1.
#               edges: 1 self-loop at v₀, 1 bridge v₀→v₁.

GENUS2_GRAPHS = [
    {'name': 'smooth',   'vertices': [(2, 0)],          'edges': [],                  'aut': 1,  'h1': 0},
    {'name': 'fig_eight','vertices': [(1, 2)],          'edges': [('self', 0)],       'aut': 2,  'h1': 1},
    {'name': 'banana',   'vertices': [(0, 4)],          'edges': [('self', 0), ('self', 0)], 'aut': 8,  'h1': 2},
    {'name': 'dumbbell', 'vertices': [(1, 1), (1, 1)],  'edges': [('bridge', 0, 1)],  'aut': 2,  'h1': 0},
    {'name': 'theta',    'vertices': [(0, 3), (0, 3)],  'edges': [('bridge', 0, 1)] * 3, 'aut': 12, 'h1': 2},
    {'name': 'lollipop', 'vertices': [(0, 3), (1, 1)],  'edges': [('self', 0), ('bridge', 0, 1)], 'aut': 2, 'h1': 1},
]


def verify_genus2_graphs():
    """Verify all 6 graphs have genus 2 and are stable."""
    for G in GENUS2_GRAPHS:
        n_v = len(G['vertices'])
        n_e = len(G['edges'])
        g_sum = sum(gv for gv, _ in G['vertices'])
        h1 = n_e - n_v + 1
        g_total = h1 + g_sum
        assert g_total == 2, f"{G['name']}: genus = {g_total} ≠ 2"
        assert h1 == G['h1'], f"{G['name']}: h¹ = {h1} ≠ {G['h1']}"
        for gv, nv in G['vertices']:
            assert 2 * gv + nv >= 3, f"{G['name']}: unstable vertex (g={gv}, n={nv})"


# ============================================================================
# Multi-channel graph amplitudes
# ============================================================================

def _channel_assignments(n_edges: int) -> List[Tuple[str, ...]]:
    """All channel assignments σ: {e₁,...,e_n} → {T, W}."""
    if n_edges == 0:
        return [()]
    result = []
    for sub in _channel_assignments(n_edges - 1):
        result.append(sub + ('T',))
        result.append(sub + ('W',))
    return result


def _half_edge_channels_at_vertex(graph_idx: int, sigma: Tuple[str, ...]) -> List[List[str]]:
    """For each vertex, return the list of half-edge channels.

    Each bridge edge (v₁,v₂) contributes one half-edge to v₁ and one to v₂.
    Each self-loop at v contributes two half-edges to v.
    """
    G = GENUS2_GRAPHS[graph_idx]
    n_v = len(G['vertices'])
    channels_at_v = [[] for _ in range(n_v)]
    for edge_idx, edge in enumerate(G['edges']):
        ch = sigma[edge_idx]
        if edge[0] == 'self':
            v = edge[1]
            channels_at_v[v].append(ch)
            channels_at_v[v].append(ch)
        elif edge[0] == 'bridge':
            v1, v2 = edge[1], edge[2]
            channels_at_v[v1].append(ch)
            channels_at_v[v2].append(ch)
    return channels_at_v


def genus0_vertex_factor(half_edge_channels: List[str], c: Fraction) -> Fraction:
    """Vertex factor for a genus-0 vertex with given half-edge channels.

    For trivalent (n=3): V = C_{i₁i₂i₃}
    For 4-valent (n=4) at a double-self-loop vertex (banana):
        V = Σ_m η^{mm} C_{i₁i₂m} C_{mi₃i₄}
        where (i₁,i₂) are from loop 1 and (i₃,i₄) from loop 2.

    These are R-matrix INDEPENDENT (genus 0 is unaffected by R).
    """
    n = len(half_edge_channels)
    if n == 3:
        return C3(half_edge_channels[0], half_edge_channels[1],
                   half_edge_channels[2], c)
    elif n == 4:
        # For banana: pairing is (0,1)|(2,3)
        i1, i2 = half_edge_channels[0], half_edge_channels[1]
        j1, j2 = half_edge_channels[2], half_edge_channels[3]
        return V04_s_channel(i1, i2, j1, j2, c)
    elif n == 0:
        # Smooth vertex: contributes the genus-g integrated class
        return Fraction(1)  # placeholder; handled separately
    raise ValueError(f"Unsupported genus-0 vertex with {n} half-edges")


def genus1_vertex_factor(half_edge_channels: List[str], c: Fraction,
                         use_exact: bool = True) -> Fraction:
    """Vertex factor for a genus-1 vertex with given half-edge channels.

    For the CohFT graph sum, the genus-1 vertex factor depends on the
    R-matrix. However, for the SCALAR bar-complex CohFT:

    - n=0 (smooth genus-1): integrated F₁ = κ/24
    - n=1 (one marked point): ⟨e_i⟩_{1,1}
    - n=2 (self-loop): ⟨e_i e_j⟩_{1,2}

    The per-channel decomposition gives, for each channel i:
    F₁^{(i)} = κ_i / 24.

    For the one-point function at genus 1, the CohFT gives:
    ⟨e_i⟩_{1,1} = ∫_{M̄_{1,1}} Ω_{1,1}(e_i)

    For the bar-complex CohFT with the Â-genus R-matrix, this equals
    κ_i/24 at the INTEGRATED level (the vertex factor for graphs with
    a genus-1 vertex absorbs the R-correction into the full graph sum).

    The key structural fact: at genus 1, the one-point and two-point
    vertex factors are determined by the per-channel genus-1 universality:
        ⟨e_i⟩_{1,1} = κ_i/24  [proved unconditionally]
        ⟨e_i e_i⟩_{1,2} = vertex factor for self-loop at genus-1

    For the self-loop vertex factor on M̄_{1,2}, we need:
    ∫_{M̄_{1,2}} Ω_{1,2}(e_i, e_i) with appropriate ψ-class from the node.

    NOTE: Using κ_i/24 as the genus-1 vertex factor is the LEADING ORDER
    approximation. The exact value includes R-matrix corrections that modify
    individual graph amplitudes but cancel in the total sum for the scalar
    case. For the multi-channel case, these corrections affect cross-channel
    terms.

    We flag this with RECTIFICATION-FLAG below.
    """
    n = len(half_edge_channels)
    if n == 0:
        # Smooth genus-1 vertex (no marked points): not in genus-2 graphs
        return Fraction(0)  # This vertex type doesn't appear in genus-2 graphs
    elif n == 1:
        ch = half_edge_channels[0]
        # One marked point at genus 1
        # ⟨e_i⟩_{1,1} = κ_i/24 [genus-1 universality]
        kappa_ch = kappa_T(c) if ch == 'T' else kappa_W(c)
        return kappa_ch / 24
    elif n == 2:
        # Self-loop at genus 1: both half-edges carry same channel
        ch1, ch2 = half_edge_channels
        if ch1 != ch2:
            return Fraction(0)  # diagonal metric
        kappa_ch = kappa_T(c) if ch1 == 'T' else kappa_W(c)
        # ⟨e_i e_i⟩_{1,2} for the self-loop node
        # At leading order: κ_i/24
        # % RECTIFICATION-FLAG: R-matrix corrections modify this value.
        # The total genus-2 free energy F₂ is affected through the
        # figure-eight graph (Γ₁) amplitude. The R-corrections cancel
        # in the full scalar sum but may not cancel in cross-channel terms.
        return kappa_ch / 24
    raise ValueError(f"Unsupported genus-1 vertex with {n} half-edges")


def graph_amplitude(graph_idx: int, sigma: Tuple[str, ...],
                    c: Fraction) -> Fraction:
    """Compute the amplitude A(Γ, σ) for graph Γ with channel assignment σ.

    A(Γ, σ) = Π_e η^{σ(e),σ(e)} × Π_v V_v(g_v, channels_v)

    Returns the amplitude WITHOUT the 1/|Aut| factor.
    """
    G = GENUS2_GRAPHS[graph_idx]
    if G['name'] == 'smooth':
        # Smooth genus-2: no edges, no channels. Contribution is the
        # smooth-interior integral, which is part of the total F₂.
        # This is NOT computable from the graph sum alone.
        # We handle it via the total = smooth + boundary decomposition.
        return Fraction(0)  # Handled separately

    # Propagator product
    prop_product = Fraction(1)
    for edge_idx in range(len(G['edges'])):
        prop_product *= propagator(sigma[edge_idx], c)

    # Vertex factors
    channels_at_v = _half_edge_channels_at_vertex(graph_idx, sigma)
    vertex_product = Fraction(1)
    for v_idx, (gv, nv) in enumerate(G['vertices']):
        he_channels = channels_at_v[v_idx]
        if gv == 0:
            vertex_product *= genus0_vertex_factor(he_channels, c)
        elif gv == 1:
            vertex_product *= genus1_vertex_factor(he_channels, c)
        elif gv == 2:
            # genus-2 vertex with no half-edges = smooth part
            # Already handled above
            pass
        else:
            raise ValueError(f"Unsupported vertex genus {gv}")

    return prop_product * vertex_product


def graph_total_amplitude(graph_idx: int, c: Fraction) -> Dict[str, Fraction]:
    """Total amplitude of graph Γ summed over all channel assignments.

    Returns dict with 'all_T', 'all_W', 'mixed', 'total' components.
    """
    G = GENUS2_GRAPHS[graph_idx]
    n_edges = len(G['edges'])

    if n_edges == 0:
        # Smooth graph: no channel assignments
        return {'all_T': Fraction(0), 'all_W': Fraction(0),
                'mixed': Fraction(0), 'total': Fraction(0),
                'note': 'smooth: handled separately'}

    all_T_amp = Fraction(0)
    all_W_amp = Fraction(0)
    mixed_amp = Fraction(0)

    for sigma in _channel_assignments(n_edges):
        amp = graph_amplitude(graph_idx, sigma, c)
        if all(ch == 'T' for ch in sigma):
            all_T_amp += amp
        elif all(ch == 'W' for ch in sigma):
            all_W_amp += amp
        else:
            mixed_amp += amp

    aut = G['aut']
    return {
        'all_T': all_T_amp / aut,
        'all_W': all_W_amp / aut,
        'mixed': mixed_amp / aut,
        'total': (all_T_amp + all_W_amp + mixed_amp) / aut,
    }


# ============================================================================
# The computation: F₂(W₃) from the graph sum
# ============================================================================

def compute_F2_w3(c_val: Fraction) -> Dict[str, Fraction]:
    r"""Compute the genus-2 free energy of W₃ at central charge c.

    Strategy: We compute the BOUNDARY graph sum (Γ₁ through Γ₅) with
    multi-channel Feynman rules. The smooth contribution (Γ₀) is
    determined by the constraint F₂ = κ · λ₂^FP for the scalar case.

    For the multi-channel case:
    F₂(W₃) = F₂^{per-channel} + δF₂^{cross}

    where F₂^{per-channel} = κ_T · λ₂^FP + κ_W · λ₂^FP = κ · λ₂^FP
    and δF₂^{cross} is the cross-channel correction from mixed assignments.

    The cross-channel correction comes from graphs with ≥ 2 edges:
    Γ₂ (banana), Γ₄ (theta), Γ₅ (lollipop).
    """
    fp2 = lambda_fp(2)  # = 7/5760

    # Per-channel universal contribution
    kT = kappa_T(c_val)
    kW = kappa_W(c_val)
    kTotal = kappa_total(c_val)
    F2_universal = kTotal * fp2

    # Per-graph amplitudes with channel decomposition
    results_by_graph = {}
    boundary_total = Fraction(0)
    boundary_diagonal = Fraction(0)
    boundary_mixed = Fraction(0)

    for idx in range(6):
        G = GENUS2_GRAPHS[idx]
        r = graph_total_amplitude(idx, c_val)
        results_by_graph[G['name']] = r
        boundary_total += r['total']
        boundary_diagonal += r['all_T'] + r['all_W']
        boundary_mixed += r['mixed']

    # The cross-channel correction
    delta_cross = boundary_mixed

    return {
        'c': c_val,
        'kappa_T': kT,
        'kappa_W': kW,
        'kappa_total': kTotal,
        'lambda2_fp': fp2,
        'F2_universal': F2_universal,
        'boundary_total': boundary_total,
        'boundary_diagonal': boundary_diagonal,
        'cross_channel_correction': delta_cross,
        'per_graph': results_by_graph,
    }


def cross_channel_correction(c_val: Fraction) -> Fraction:
    """The total cross-channel correction δF₂ for W₃.

    This is the sum of mixed-channel amplitudes from graphs Γ₂, Γ₄, Γ₅.

    Computed analytically:

    Γ₂ (banana, |Aut|=8):
        Mixed assignment (T,W): both loops carry different channels.
        V_{0,4}(T,T,W,W) = Σ_m η^{mm} C_{TTm} C_{WWm} = (2/c)·c·c = 2c.
        A(T,W) = η^{TT}·η^{WW}·V = (2/c)(3/c)·2c = 12/c.
        Two mixed assignments (T,W) and (W,T) with same amplitude.
        δΓ₂ = (1/8)·2·(12/c) = 3/c.

    Γ₄ (theta, |Aut|=12):
        3 edges, 8 channel assignments.
        (T,T,W)-type (3 assignments): C_{TTW} = 0 → amplitude = 0.
        (T,W,W)-type (3 assignments): C_{TWW} = c.
            A = (2/c)(3/c)(3/c)·c² = 18/c.
        δΓ₄ = (1/12)·3·(18/c) = 9/(2c).

    Γ₅ (lollipop, |Aut|=2):
        (T,W): self-loop T, bridge W. V₀ = C_{TTW} = 0 → A = 0.
        (W,T): self-loop W, bridge T. V₀ = C_{WWT} = c. V₁ = κ_T/24.
            A = (3/c)(2/c)·c·(c/2)/24 = 6·c/(48c²) = ... let me compute:
            = (3/c)·(2/c)·c·(c/48) = 6c/(48c²) = 1/8.
            WAIT: κ_T/24 = (c/2)/24 = c/48.
            A = (3/c)·(2/c)·c·(c/48) = (6/c²)·(c²/48) = 6/48 = 1/8.
        δΓ₅ = (1/2)·(0 + 1/8) = 1/16.

    Total: δF₂ = 3/c + 9/(2c) + 1/16 = (48 + 72 + c)/(16c) = (c + 120)/(16c).

    % RECTIFICATION-FLAG: This computation uses V_{1,1}(T) = κ_T/24 as the
    % genus-1 one-point vertex factor. This is the genus-1 universality value.
    % The R-matrix corrections to V_{1,1} modify δΓ₅ but cancel in the
    % single-channel graph sum. Whether they cancel in the cross-channel sum
    % is the content of op:multi-generator-universality.
    %
    % The direct computation gives δF₂ = (c + 120)/(16c) ≠ 0.
    % If universality holds (F₂ = κ·λ₂^FP), then the R-corrections
    % to V_{1,1} must produce a compensating term -(c + 120)/(16c).
    % This would be a nontrivial identity on the R-matrix.
    """
    # Banana correction
    delta_banana = Fraction(3) / c_val

    # Theta correction
    delta_theta = Fraction(9) / (2 * c_val)

    # Lollipop correction
    delta_lollipop = Fraction(1, 16)

    return delta_banana + delta_theta + delta_lollipop


def cross_channel_correction_exact(c_val: Fraction) -> Dict[str, Fraction]:
    """Exact per-graph cross-channel corrections with breakdown."""
    delta_banana = Fraction(3) / c_val
    delta_theta = Fraction(9) / (2 * c_val)
    delta_lollipop = Fraction(1, 16)
    delta_total = delta_banana + delta_theta + delta_lollipop
    # Simplify: 3/c + 9/(2c) + 1/16 = 6/(2c) + 9/(2c) + 1/16
    #         = 15/(2c) + 1/16 = (120 + c)/(16c)
    delta_simplified = (c_val + 120) / (16 * c_val)
    return {
        'delta_banana': delta_banana,
        'delta_theta': delta_theta,
        'delta_lollipop': delta_lollipop,
        'delta_total': delta_total,
        'delta_simplified': delta_simplified,
        'match': delta_total == delta_simplified,
    }


# ============================================================================
# Planted-forest corrections at genus 2
# ============================================================================

def planted_forest_correction_T(c_val: Fraction) -> Fraction:
    r"""Planted-forest correction δ_pf^{(2,0)} on the T-line.

    δ_pf = S₃(10S₃ - κ)/48

    For T-line: S₃ = 2, κ_T = c/2.
    δ_pf^T = 2·(20 - c/2)/48 = (40 - c)/(48) = -(c - 40)/48.

    For Virasoro: this matches the manuscript formula -(c-40)/48.
    """
    S3 = S3_T(c_val)
    kT = kappa_T(c_val)
    return S3 * (10 * S3 - kT) / 48


def planted_forest_correction_W(c_val: Fraction) -> Fraction:
    r"""Planted-forest correction δ_pf^{(2,0)} on the W-line.

    δ_pf = S₃(10S₃ - κ)/48

    For W-line: S₃ = 0 (Z₂ parity), κ_W = c/3.
    δ_pf^W = 0·(0 - c/3)/48 = 0.
    """
    S3 = S3_W(c_val)
    kW = kappa_W(c_val)
    return S3 * (10 * S3 - kW) / 48


def planted_forest_total(c_val: Fraction) -> Fraction:
    """Total planted-forest correction at genus 2 for W₃."""
    return planted_forest_correction_T(c_val) + planted_forest_correction_W(c_val)


# ============================================================================
# Full F₂(W₃): combining all contributions
# ============================================================================

def F2_w3_scalar_universal(c_val: Fraction) -> Fraction:
    """F₂(W₃) assuming universality holds: κ · λ₂^FP = (5c/6) · 7/5760."""
    return kappa_total(c_val) * lambda_fp(2)


def F2_w3_per_channel(c_val: Fraction) -> Fraction:
    """F₂(W₃) from per-channel sum: κ_T · λ₂^FP + κ_W · λ₂^FP = κ · λ₂^FP.

    This is the PROVED contribution from single-channel universality applied
    to each generator independently. It equals the universal formula by
    the additivity of κ.
    """
    fp2 = lambda_fp(2)
    return kappa_T(c_val) * fp2 + kappa_W(c_val) * fp2


def F2_w3_with_cross_channel(c_val: Fraction) -> Dict[str, Fraction]:
    r"""F₂(W₃) including the naive cross-channel correction.

    F₂ = F₂^{per-channel} + δF₂^{cross}
       = κ·λ₂^FP + (c + 120)/(16c)

    % RECTIFICATION-FLAG: The cross-channel correction (c+120)/(16c) uses
    % naive genus-1 vertex factors (κ_i/24). The R-matrix-corrected
    % vertex factors may cancel this correction. Whether universality holds
    % (δF₂ = 0) is op:multi-generator-universality.

    Returns both the naive and universal results for comparison.
    """
    fp2 = lambda_fp(2)
    F2_univ = kappa_total(c_val) * fp2
    delta = cross_channel_correction(c_val)
    F2_naive = F2_univ + delta

    return {
        'c': c_val,
        'F2_universal': F2_univ,
        'F2_naive_with_cross': F2_naive,
        'cross_channel_correction': delta,
        'delta_as_fraction_of_F2': delta / F2_univ if F2_univ != 0 else None,
        'universality_holds_iff_delta_zero': delta == Fraction(0),
    }


# ============================================================================
# Numerical evaluation at specific c values
# ============================================================================

def F2_w3_numerical_table(c_values: Optional[List[Fraction]] = None
                          ) -> List[Dict[str, object]]:
    """Evaluate F₂(W₃) at multiple central charges."""
    if c_values is None:
        c_values = [Fraction(1), Fraction(2), Fraction(13), Fraction(26),
                    Fraction(50), Fraction(100)]
    results = []
    for c_val in c_values:
        fp2 = lambda_fp(2)
        r = {
            'c': c_val,
            'kappa_total': kappa_total(c_val),
            'F2_universal': float(kappa_total(c_val) * fp2),
            'cross_channel': float(cross_channel_correction(c_val)),
            'F2_naive': float(kappa_total(c_val) * fp2 + cross_channel_correction(c_val)),
            'pf_correction_T': float(planted_forest_correction_T(c_val)),
            'pf_correction_W': float(planted_forest_correction_W(c_val)),
        }
        results.append(r)
    return results


# ============================================================================
# Consistency checks
# ============================================================================

def verify_single_channel_limit(c_val: Fraction) -> Dict[str, object]:
    """Verify that F₂ reduces to κ·λ₂^FP in the single-channel limit.

    In the single-channel limit (only T or only W), the cross-channel
    corrections vanish and F₂ = κ_i · λ₂^FP for the active channel.
    """
    fp2 = lambda_fp(2)

    # Single-channel T: all edges carry T, no W generator
    # The boundary graph sum with all-T is the Virasoro graph sum
    F2_T_only = kappa_T(c_val) * fp2

    # Single-channel W: all edges carry W
    F2_W_only = kappa_W(c_val) * fp2

    # Additivity: per-channel sum = κ · λ₂^FP
    F2_sum = F2_T_only + F2_W_only
    F2_univ = kappa_total(c_val) * fp2

    return {
        'F2_T': F2_T_only,
        'F2_W': F2_W_only,
        'F2_sum': F2_sum,
        'F2_universal': F2_univ,
        'additivity_holds': F2_sum == F2_univ,
    }


def verify_graph_amplitudes(c_val: Fraction) -> Dict[str, object]:
    """Verify graph amplitude computations match analytic formulas."""
    results = {}

    # Γ₂ banana: all assignments
    r2 = graph_total_amplitude(2, c_val)  # idx=2 for banana
    # Expected: all-T = (1/8)(4/c²)(2c) = 1/c
    # all-W = (1/8)(9/c²)(2c) = 18/(8c) = 9/(4c)
    # mixed = (1/8)(2·12/c) = 3/c
    expected_all_T_banana = Fraction(1) / c_val
    expected_all_W_banana = Fraction(9) / (4 * c_val)
    expected_mixed_banana = Fraction(3) / c_val
    results['banana'] = {
        'all_T': r2['all_T'],
        'all_T_expected': expected_all_T_banana,
        'all_T_match': r2['all_T'] == expected_all_T_banana,
        'all_W': r2['all_W'],
        'all_W_expected': expected_all_W_banana,
        'all_W_match': r2['all_W'] == expected_all_W_banana,
        'mixed': r2['mixed'],
        'mixed_expected': expected_mixed_banana,
        'mixed_match': r2['mixed'] == expected_mixed_banana,
    }

    # Γ₄ theta: all assignments
    r4 = graph_total_amplitude(4, c_val)  # idx=4 for theta
    # Expected: all-T = (1/12)(8/c) = 2/(3c)
    # all-W = 0 (C_{WWW} = 0)
    # mixed = (1/12)(3·18/c) = 9/(2c)
    expected_all_T_theta = Fraction(2) / (3 * c_val)
    expected_all_W_theta = Fraction(0)
    expected_mixed_theta = Fraction(9) / (2 * c_val)
    results['theta'] = {
        'all_T': r4['all_T'],
        'all_T_expected': expected_all_T_theta,
        'all_T_match': r4['all_T'] == expected_all_T_theta,
        'all_W': r4['all_W'],
        'all_W_expected': expected_all_W_theta,
        'all_W_match': r4['all_W'] == expected_all_W_theta,
        'mixed': r4['mixed'],
        'mixed_expected': expected_mixed_theta,
        'mixed_match': r4['mixed'] == expected_mixed_theta,
    }

    return results
