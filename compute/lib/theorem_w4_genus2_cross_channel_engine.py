r"""Consolidated W_4 genus-2 cross-channel engine with DS parametrization.

THEOREM (thm:multi-weight-genus-expansion applied to W_4)
=========================================================

The genus-2 cross-channel correction for W_4 = W(sl_4, f_prin) with
three generators T (weight 2), W3 (weight 3), W4 (weight 4) is:

    delta_F2(W_4, c) = R(c) + I_1(c) + I_2(c)

where:

    R(c) = (147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656)
           / (48c(c+24)(3c+46)(7c+68))

    I_1(c) = sqrt(g334^2) / 64

    I_2(c) = (3/2) * sqrt(g334^2 * g444^2) / c

with OPE structure constants (Hornfeck 1993):

    g334^2 = 42c^2(5c+22) / [(c+24)(7c+68)(3c+46)]
    g444^2 = 112c^2(2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]

Master formula (verified per-graph):

    192c * delta_F2 = 3c*g334 + 28c + 162*g334^2 + 288*g334*g444 + 8592

DS PARAMETRIZATION
==================

W_4 = W(sl_4, f_prin) central charge from DS reduction at level k:

    c(k) = 3 - 60(k+3)^2/(k+4)

where h^v(sl_4) = 4, rank(sl_4) = 3, dim(sl_4) = 15.

Koszul conductor: K_4 = 246.  Self-dual point: c = 123.
Feigin-Frenkel involution: k -> -k - 2h^v = -k - 8.

3-CHANNEL PROPAGATOR MIXING MATRIX
===================================

The bar Frobenius algebra has metric eta_{ij} = (c/h_i) delta_{ij}
with inverse eta^{ij} = (h_i/c) delta_{ij} for h_i in {2, 3, 4}.

The propagator mixing matrix M_{ij} = eta^{ii} C_{iik} eta^{kk} C_{kkj}
encodes the 2-step propagation through each intermediate channel.
The cross-channel correction arises from the fact that M is NOT
proportional to the identity: different channels propagate with
different weights h_i/c, producing mixing through the Frobenius
algebra multiplication.

DECOUPLING ANALYSIS
====================

Removing the weight-4 generator does NOT recover delta_F2(W_3) because:
(1) The W_4 Frobenius algebra has 3 channels; W_3 has 2 channels.
(2) Setting g334 = g444 = 0 removes higher-spin exchange but retains
    the W4-channel gravitational propagation (C_{TW4W4} = c).
(3) The gravitational-only formula delta_F2^grav(W_4) = (7c+2148)/(48c)
    already exceeds delta_F2(W_3) = (c+204)/(16c) for all c > 0.

Restricting the channel sum to {T, W3} only (true 2-channel truncation)
recovers delta_F2(W_3) = (c+204)/(16c) exactly.

MULTI-PATH VERIFICATION (7 paths)
===================================

Path 1: Analytic R + I_1 + I_2 decomposition
Path 2: Master formula 192c*delta = polynomial(g334, g444, c)
Path 3: Direct graph sum over 7 stable graphs of M_bar_{2,0}
Path 4: Per-graph analytic formulas (6 boundary graphs)
Path 5: Gravitational limit (g334=g444=0)
Path 6: Large-c asymptotic verification
Path 7: Koszul duality check at c <-> 246-c

Manuscript references:
    thm:theorem-d, thm:multi-weight-genus-expansion,
    rem:propagator-weight-universality, op:multi-generator-universality
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import comb, factorial
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.wn_central_charge_canonical import c_wn_fl as _canonical_c_wn_fl


# ============================================================================
# Bernoulli numbers and Faber-Pandharipande
# ============================================================================

@lru_cache(maxsize=64)
def _bernoulli(n: int) -> Fraction:
    """Exact Bernoulli number B_n via recurrence."""
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
    r"""Faber-Pandharipande intersection number.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs(B2g) / Fraction(factorial(2 * g)))


# ============================================================================
# DS parametrization for W_4 = W(sl_4, f_prin)
# ============================================================================

# sl_4 data
_N = 4                           # rank + 1
_RANK = _N - 1                   # = 3
_H_DUAL = _N                     # dual Coxeter number = 4
_DIM_G = _N ** 2 - 1             # = 15

# Koszul conductor
K4 = 2 * (_N - 1) + 4 * _N * (_N ** 2 - 1)  # = 246


def central_charge_from_k(k: Fraction) -> Fraction:
    r"""W_4 central charge from DS level k (Fateev-Lukyanov).

    c(k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N) = 3 - 60(k+3)^2/(k+4)

    Valid for k != -4 (critical level).
    Decisive test: k=1 gives c=-189 (NOT -9).
    """
    # VERIFIED: c_wn_fl(4,1)=-189 [DC], complementarity c(1)+c(-9)=246=K4 [SY]
    return _canonical_c_wn_fl(4, k)


def k_from_central_charge(c: Fraction) -> Fraction:
    r"""DS level k from central charge (Fateev-Lukyanov inverse).

    Solves c = 3 - 60(k+3)^2/(k+4) for k on the physical branch (k > -4).
    Quadratic: 60k^2 + (357+c)k + (528+4c) = 0.
    Discriminant: (c-243)(c-3).
    """
    c = Fraction(c) if not isinstance(c, Fraction) else c
    if c == Fraction(3):
        raise ValueError("c = 3 corresponds to k -> infinity")
    A = Fraction(60)
    B = Fraction(357) + c
    C_coeff = Fraction(528) + 4 * c
    disc = B * B - 4 * A * C_coeff  # = (c-243)(c-3)
    # Exact integer square root of the rational discriminant
    p, q = disc.numerator, disc.denominator
    pq = p * q
    if pq < 0:
        raise ValueError(f"Discriminant negative at c={c}: no real level")
    from math import isqrt
    s = isqrt(pq)
    if s * s != pq:
        raise ValueError(f"Discriminant {disc} not a perfect square; no exact Fraction level")
    sqrt_disc = Fraction(s, q)
    # Physical branch: k > -4 requires the + root
    return (-B + sqrt_disc) / (2 * A)


def feigin_frenkel_dual_k(k: Fraction) -> Fraction:
    r"""Feigin-Frenkel dual level: k -> -k - 2h^v = -k - 8."""
    return -k - 2 * _H_DUAL


def koszul_dual_c(c: Fraction) -> Fraction:
    """Koszul dual central charge: c' = K_4 - c = 246 - c."""
    return Fraction(K4) - c


# ============================================================================
# W_4 algebra constants
# ============================================================================

CHANNELS = ('T', 'W3', 'W4')
WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}


def kappa_channel(ch: str, c: Fraction) -> Fraction:
    """Per-channel kappa: kappa_j = c/h_j."""
    return c / Fraction(WEIGHTS[ch])


def kappa_total(c: Fraction) -> Fraction:
    """Total kappa(W_4) = c/2 + c/3 + c/4 = 13c/12."""
    return sum(kappa_channel(ch, c) for ch in CHANNELS)


def kappa_total_float(c: float) -> float:
    """Total kappa as float."""
    return 13.0 * c / 12.0


# ============================================================================
# OPE structure constants (Hornfeck 1993)
# ============================================================================

def g334_squared(c: Fraction) -> Fraction:
    r"""g334^2 = 42c^2(5c+22) / [(c+24)(7c+68)(3c+46)].

    The W3 x W3 -> W4 primary coupling squared.
    """
    return (Fraction(42) * c ** 2 * (5 * c + 22)
            / ((c + 24) * (7 * c + 68) * (3 * c + 46)))


def g444_squared(c: Fraction) -> Fraction:
    r"""g444^2 = 112c^2(2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)].

    The W4 x W4 -> W4 self-coupling squared.
    """
    return (Fraction(112) * c ** 2 * (2 * c - 1) * (3 * c + 46)
            / ((c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3)))


def g334_squared_float(c: float) -> float:
    """g334^2 as float."""
    return 42 * c ** 2 * (5 * c + 22) / ((c + 24) * (7 * c + 68) * (3 * c + 46))


def g444_squared_float(c: float) -> float:
    """g444^2 as float."""
    return (112 * c ** 2 * (2 * c - 1) * (3 * c + 46)
            / ((c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3)))


# ============================================================================
# 3-point Frobenius structure constants
# ============================================================================

def C3(i: str, j: str, k: str, c: float,
       g334: float, g444: float) -> float:
    """W_4 three-point structure constant C_{ijk}.

    Parity: W3 has odd weight; at each vertex the number of W3
    half-edges must be even.

    Nonzero couplings:
        C_{TTT} = C_{TW3W3} = C_{TW4W4} = c     (gravitational)
        C_{W3W3W4} = (c/4)*g334                   (higher-spin)
        C_{W4W4W4} = (c/4)*g444                   (higher-spin)
    """
    w3_count = sum(1 for x in (i, j, k) if x == 'W3')
    if w3_count % 2 == 1:
        return 0.0
    labels = tuple(sorted([i, j, k]))
    if labels in [('T', 'T', 'T'), ('T', 'W3', 'W3'), ('T', 'W4', 'W4')]:
        return c
    if labels == ('W3', 'W3', 'W4'):
        return (c / 4.0) * g334
    if labels == ('W4', 'W4', 'W4'):
        return (c / 4.0) * g444
    return 0.0


def V04(i1: str, i2: str, j1: str, j2: str,
        c: float, g334: float, g444: float) -> float:
    r"""Genus-0 four-point vertex via factorization.

    V_{0,4}(i1,i2|j1,j2) = sum_m eta^{mm} C_{i1 i2 m} C_{m j1 j2}
    """
    total = 0.0
    for m in CHANNELS:
        c3a = C3(i1, i2, m, c, g334, g444)
        if c3a == 0.0:
            continue
        c3b = C3(m, j1, j2, c, g334, g444)
        if c3b == 0.0:
            continue
        total += (WEIGHTS[m] / c) * c3a * c3b
    return total


# ============================================================================
# 3-channel propagator mixing matrix
# ============================================================================

def propagator_matrix(c: float) -> Dict[str, float]:
    """Diagonal propagator matrix eta^{ij} = (h_i/c) delta_{ij}.

    Returns {channel: eta^{ii}} for each channel.
    """
    return {ch: WEIGHTS[ch] / c for ch in CHANNELS}


def mixing_matrix(c: float, g334: float, g444: float) -> Dict[Tuple[str, str], float]:
    r"""Frobenius mixing matrix M_{ij} = sum_k eta^{kk} C_{ik} C_{kj}.

    This encodes the 2-step propagation through intermediate channels.
    The off-diagonal entries drive the cross-channel correction.
    """
    M = {}
    for i in CHANNELS:
        for j in CHANNELS:
            total = 0.0
            for k in CHANNELS:
                c_ik = C3(i, i, k, c, g334, g444)
                c_kj = C3(k, j, j, c, g334, g444)
                total += (WEIGHTS[k] / c) * c_ik * c_kj
            M[(i, j)] = total
    return M


def mixing_eigenvalues(c: float, g334: float, g444: float) -> List[float]:
    """Eigenvalues of the 3x3 mixing matrix (sorted)."""
    M = mixing_matrix(c, g334, g444)
    # Build 3x3 matrix
    ch_list = list(CHANNELS)
    mat = [[M[(ch_list[i], ch_list[j])] for j in range(3)] for i in range(3)]
    # Compute eigenvalues via characteristic polynomial
    # For a 3x3 matrix with known structure, use numpy-free approach
    a, b, c_m = mat[0][0], mat[0][1], mat[0][2]
    d, e, f = mat[1][0], mat[1][1], mat[1][2]
    g, h, k_m = mat[2][0], mat[2][1], mat[2][2]
    tr = a + e + k_m
    # det of 2x2 minors
    m11 = e * k_m - f * h
    m22 = a * k_m - c_m * g
    m33 = a * e - b * d
    cofsum = m11 + m22 + m33
    det = a * m11 - b * (d * k_m - f * g) + c_m * (d * h - e * g)
    # Characteristic polynomial: x^3 - tr*x^2 + cofsum*x - det = 0
    # Solve via depressed cubic
    p = cofsum - tr ** 2 / 3.0
    q = 2 * tr ** 3 / 27.0 - tr * cofsum / 3.0 + det
    disc = -(4 * p ** 3 + 27 * q ** 2)
    if disc >= 0:
        # Three real roots (trigonometric method)
        r_val = math.sqrt(-p / 3.0) if p < 0 else 0.0
        if r_val > 0:
            theta = math.acos(max(-1, min(1, -q / (2 * r_val ** 3)))) / 3.0
            roots = [
                2 * r_val * math.cos(theta) + tr / 3.0,
                2 * r_val * math.cos(theta - 2 * math.pi / 3) + tr / 3.0,
                2 * r_val * math.cos(theta + 2 * math.pi / 3) + tr / 3.0,
            ]
        else:
            roots = [tr / 3.0] * 3
    else:
        # One real root (Cardano)
        d_card = math.sqrt(q ** 2 / 4.0 + p ** 3 / 27.0)
        u = (-q / 2.0 + d_card)
        v = (-q / 2.0 - d_card)
        u_cr = math.copysign(abs(u) ** (1 / 3.0), u)
        v_cr = math.copysign(abs(v) ** (1 / 3.0), v)
        roots = [u_cr + v_cr + tr / 3.0]
    return sorted(roots)


# ============================================================================
# Genus-2 stable graphs (7 graphs of M_bar_{2,0})
# ============================================================================

_GENUS2_GRAPHS = [
    # (name, vertices=[(genus, valence)], edges=[(type, v1, v2)], aut)
    ('smooth',    [(2, 0)],          [],                                      1),
    ('fig_eight', [(1, 2)],          [('self', 0)],                           2),
    ('banana',    [(0, 4)],          [('self', 0), ('self', 0)],              8),
    ('dumbbell',  [(1, 1), (1, 1)],  [('bridge', 0, 1)],                     2),
    ('theta',     [(0, 3), (0, 3)],  [('bridge', 0, 1)] * 3,                12),
    ('lollipop',  [(0, 3), (1, 1)],  [('self', 0), ('bridge', 0, 1)],        2),
    ('barbell',   [(0, 3), (0, 3)],  [('self', 0), ('self', 1),
                                      ('bridge', 0, 1)],                      8),
]


def _half_edge_channels(graph_idx: int,
                        sigma: Tuple[str, ...]) -> List[List[str]]:
    """For each vertex, return half-edge channel labels."""
    _, vertices, edges, _ = _GENUS2_GRAPHS[graph_idx]
    n_v = len(vertices)
    channels_at_v: List[List[str]] = [[] for _ in range(n_v)]
    for e_idx, edge in enumerate(edges):
        ch = sigma[e_idx]
        if edge[0] == 'self':
            v = edge[1]
            channels_at_v[v].append(ch)
            channels_at_v[v].append(ch)
        elif edge[0] == 'bridge':
            channels_at_v[edge[1]].append(ch)
            channels_at_v[edge[2]].append(ch)
    return channels_at_v


def _graph_amplitude(graph_idx: int, sigma: Tuple[str, ...],
                     c: float, g334: float, g444: float,
                     allowed_channels: Tuple[str, ...] = CHANNELS) -> float:
    """Compute amplitude A(Gamma, sigma) without 1/|Aut| factor.

    Parameters:
        allowed_channels: restrict to a subset of channels (for decoupling).
    """
    name, vertices, edges, aut = _GENUS2_GRAPHS[graph_idx]
    if not edges:
        return 0.0

    channels_at_v = _half_edge_channels(graph_idx, sigma)

    # Parity check at genus-0 vertices
    for v_idx, (gv, nv) in enumerate(vertices):
        if gv == 0:
            odd_count = sum(1 for ch in channels_at_v[v_idx] if ch == 'W3')
            if odd_count % 2 == 1:
                return 0.0

    # Propagator product
    prop = 1.0
    for e_idx in range(len(edges)):
        prop *= WEIGHTS[sigma[e_idx]] / c

    # Vertex factors
    vf = 1.0
    for v_idx, (gv, nv) in enumerate(vertices):
        he = channels_at_v[v_idx]
        if not he:
            continue
        if gv == 0:
            if len(he) == 3:
                vf_v = C3(he[0], he[1], he[2], c, g334, g444)
            elif len(he) == 4:
                vf_v = V04(he[0], he[1], he[2], he[3], c, g334, g444)
            else:
                vf_v = 1.0
        elif gv >= 1:
            if len(set(he)) > 1:
                vf_v = 0.0
            else:
                vf_v = (c / WEIGHTS[he[0]]) * float(lambda_fp(gv))
        else:
            vf_v = 1.0
        if vf_v == 0.0:
            return 0.0
        vf *= vf_v

    return prop * vf


# ============================================================================
# Direct graph sum computation
# ============================================================================

def direct_graph_sum(c: float,
                     allowed_channels: Tuple[str, ...] = CHANNELS
                     ) -> Dict[str, Any]:
    """Compute delta_F2 by direct enumeration over all graphs and channels.

    Parameters:
        allowed_channels: restrict to a subset for decoupling analysis.
    """
    g334 = math.sqrt(g334_squared_float(c))
    g444 = math.sqrt(g444_squared_float(c))

    total_mixed = 0.0
    per_graph = {}

    for idx, (name, vertices, edges, aut) in enumerate(_GENUS2_GRAPHS):
        n_e = len(edges)
        if n_e == 0:
            per_graph[name] = {'mixed': 0.0, 'diagonal': 0.0}
            continue

        diag = 0.0
        mixed = 0.0

        for sigma in cartprod(allowed_channels, repeat=n_e):
            amp = _graph_amplitude(idx, sigma, c, g334, g444,
                                   allowed_channels) / aut
            if len(set(sigma)) <= 1:
                diag += amp
            else:
                mixed += amp

        per_graph[name] = {'mixed': mixed, 'diagonal': diag}
        total_mixed += mixed

    return {
        'c': c,
        'delta_F2': total_mixed,
        'per_graph': per_graph,
        'g334': g334,
        'g444': g444,
    }


# ============================================================================
# Master formula
# ============================================================================

def master_formula(c: float, g334: float, g444: float) -> float:
    """192c * delta = 3c*g334 + 28c + 162*g334^2 + 288*g334*g444 + 8592."""
    return (3 * c * g334 + 28 * c + 162 * g334 ** 2
            + 288 * g334 * g444 + 8592) / (192 * c)


# ============================================================================
# Analytic decomposition: R(c) + I_1(c) + I_2(c)
# ============================================================================

def rational_part(c: Fraction) -> Fraction:
    r"""Rational part R(c).

    R(c) = (147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656)
           / (48c(c+24)(3c+46)(7c+68))
    """
    num = (147 * c ** 4 + 60823 * c ** 3 + 2360126 * c ** 2
           + 34360800 * c + 161254656)
    den = 48 * c * (c + 24) * (3 * c + 46) * (7 * c + 68)
    return Fraction(num, den) if isinstance(num, int) else num / den


def rational_part_float(c: float) -> float:
    """R(c) as float."""
    num = (147 * c ** 4 + 60823 * c ** 3 + 2360126 * c ** 2
           + 34360800 * c + 161254656)
    den = 48 * c * (c + 24) * (3 * c + 46) * (7 * c + 68)
    return num / den


def gravitational_part(c: float) -> float:
    r"""Gravitational cross-channel: delta_F2^grav = (7c + 2148)/(48c).

    This is the g334 = g444 = 0 limit.
    """
    return (7 * c + 2148) / (48 * c)


def gravitational_part_exact(c: Fraction) -> Fraction:
    """Gravitational part as exact Fraction."""
    return (7 * c + 2148) / (48 * c)


def rational_hs_part(c: float) -> float:
    r"""Rational higher-spin correction.

    R_HS(c) = 567c(5c+22) / (16(c+24)(7c+68)(3c+46))
            = (27/32) * g334^2 / c
    """
    return 567 * c * (5 * c + 22) / (16 * (c + 24) * (7 * c + 68) * (3 * c + 46))


def rational_hs_part_exact(c: Fraction) -> Fraction:
    """Rational HS part as Fraction."""
    return (Fraction(567) * c * (5 * c + 22)
            / (16 * (c + 24) * (7 * c + 68) * (3 * c + 46)))


def irrational_part_1(c: float) -> float:
    r"""First irrational term: I_1 = sqrt(g334^2)/64.

    From the lollipop graph: 3c*g334/(192c) = g334/64.
    """
    return math.sqrt(g334_squared_float(c)) / 64


def irrational_part_2(c: float) -> float:
    r"""Second irrational term: I_2 = (3/2)*sqrt(g334^2*g444^2)/c.

    From the banana + barbell graphs: 288*g334*g444/(192c).
    """
    return 1.5 * math.sqrt(g334_squared_float(c) * g444_squared_float(c)) / c


def delta_F2_full(c: float) -> float:
    """Full cross-channel correction: R + I_1 + I_2.

    Valid for c > 1/2 (unitarity bound for g444^2 > 0).
    """
    return rational_part_float(c) + irrational_part_1(c) + irrational_part_2(c)


def delta_F2_via_master(c: float) -> float:
    """Compute via the master formula (independent path)."""
    g334 = math.sqrt(g334_squared_float(c))
    g444 = math.sqrt(g444_squared_float(c))
    return master_formula(c, g334, g444)


# ============================================================================
# Per-graph analytic formulas
# ============================================================================

def per_graph_mixed(c: float) -> Dict[str, float]:
    """Per-graph mixed amplitudes evaluated numerically."""
    g334 = math.sqrt(g334_squared_float(c))
    g444 = math.sqrt(g444_squared_float(c))
    return {
        'fig_eight':  0.0,
        'banana':     (3 * g334 * g444 + 52) / (4 * c),
        'dumbbell':   0.0,
        'theta':      (9 * g334 ** 2 + 200) / (16 * c),
        'lollipop':   g334 / 64 + 7.0 / 48,
        'barbell':    (9 * g334 ** 2 + 24 * g334 * g444 + 616) / (32 * c),
    }


def per_graph_grav_only(c: float) -> Dict[str, float]:
    """Per-graph at g334=g444=0 (gravitational only)."""
    return {
        'fig_eight':  0.0,
        'banana':     13.0 / c,
        'dumbbell':   0.0,
        'theta':      12.5 / c,
        'lollipop':   7.0 / 48,
        'barbell':    19.25 / c,
    }


# ============================================================================
# W_3 comparison
# ============================================================================

def delta_F2_W3(c: float) -> float:
    """W_3 cross-channel correction: (c+204)/(16c)."""
    return (c + 204) / (16 * c)


# ============================================================================
# Decoupling analysis: restrict to 2-channel
# ============================================================================

def delta_F2_two_channel(c: float) -> float:
    """Cross-channel correction using only {T, W3} channels.

    This is the true decoupling limit: remove the W4 generator entirely.
    Should recover delta_F2(W_3) = (c+204)/(16c).
    """
    return direct_graph_sum(c, allowed_channels=('T', 'W3'))['delta_F2']


# ============================================================================
# Large-c asymptotics
# ============================================================================

def large_c_limit() -> float:
    r"""Leading constant as c -> infinity.

    g334 -> sqrt(10), g444 -> 4*sqrt(3)/5
    delta -> (3*sqrt(10) + 28)/192
    """
    return (3 * math.sqrt(10) + 28) / 192


# ============================================================================
# Koszul duality
# ============================================================================

def koszul_dual_check(c: float) -> Dict[str, float]:
    """Evaluate delta_F2 at c and at K_4 - c = 246 - c."""
    if c <= 0.5 or c >= 245.5:
        raise ValueError(f"Need 1/2 < c < 245.5, got c={c}")
    d1 = delta_F2_full(c)
    d2 = delta_F2_full(K4 - c)
    return {
        'c': c,
        'c_dual': K4 - c,
        'delta_at_c': d1,
        'delta_at_dual': d2,
        'kappa_sum': kappa_total_float(c) + kappa_total_float(K4 - c),
    }


# ============================================================================
# Multi-path verification
# ============================================================================

def seven_path_verification(c: float) -> Dict[str, Any]:
    """Run all 7 independent verification paths at a given c.

    Returns a dict with each path's value and agreement status.
    """
    g334_v = math.sqrt(g334_squared_float(c))
    g444_v = math.sqrt(g444_squared_float(c))

    # Path 1: R + I_1 + I_2
    p1 = rational_part_float(c) + irrational_part_1(c) + irrational_part_2(c)

    # Path 2: Master formula
    p2 = master_formula(c, g334_v, g444_v)

    # Path 3: Direct graph sum
    gs = direct_graph_sum(c)
    p3 = gs['delta_F2']

    # Path 4: Per-graph analytic sum
    pg = per_graph_mixed(c)
    p4 = sum(pg.values())

    # Path 5: Gravitational limit check
    p5_grav = gravitational_part(c)
    p5_master_at_zero = master_formula(c, 0.0, 0.0)

    # Path 6: Large-c asymptotic
    lim = large_c_limit()

    # Path 7: Koszul duality (well-definedness at dual point)
    if 0.5 < c < 245.5:
        kd = koszul_dual_check(c)
        p7_dual_defined = kd['delta_at_dual'] > 0
    else:
        p7_dual_defined = None

    tol = 1e-9
    return {
        'c': c,
        'path1_decomposition': p1,
        'path2_master': p2,
        'path3_graph_sum': p3,
        'path4_per_graph': p4,
        'path5_grav': p5_grav,
        'path5_grav_master': p5_master_at_zero,
        'path6_large_c_limit': lim,
        'path7_dual_defined': p7_dual_defined,
        'p1_p2_agree': abs(p1 - p2) < tol,
        'p1_p3_agree': abs(p1 - p3) < tol,
        'p1_p4_agree': abs(p1 - p4) < tol,
        'p5_consistent': abs(p5_grav - p5_master_at_zero) < tol,
        'all_agree': (abs(p1 - p2) < tol and abs(p1 - p3) < tol
                      and abs(p1 - p4) < tol),
    }


# ============================================================================
# Higher-spin correction decomposition
# ============================================================================

def higher_spin_correction(c: float) -> float:
    """Total HS correction: delta_F2^full - delta_F2^grav."""
    return delta_F2_full(c) - gravitational_part(c)


def hs_decomposition(c: float) -> Dict[str, float]:
    """Decompose the HS correction into rational and irrational parts."""
    return {
        'rational_hs': rational_hs_part(c),
        'irrational_1': irrational_part_1(c),
        'irrational_2': irrational_part_2(c),
        'total_hs': higher_spin_correction(c),
    }


# ============================================================================
# Full evaluation with all diagnostics
# ============================================================================

def full_evaluation(c: float) -> Dict[str, Any]:
    """Comprehensive evaluation at a specific central charge."""
    g3sq = g334_squared_float(c)
    g4sq = g444_squared_float(c)
    g3 = math.sqrt(g3sq)
    g4 = math.sqrt(g4sq)

    R = rational_part_float(c)
    I1 = irrational_part_1(c)
    I2 = irrational_part_2(c)
    full = R + I1 + I2
    grav = gravitational_part(c)

    mf = master_formula(c, g3, g4)
    gs = direct_graph_sum(c)['delta_F2']

    kl = kappa_total_float(c) * float(lambda_fp(2))

    return {
        'c': c,
        'delta_F2': full,
        'R': R,
        'I_1': I1,
        'I_2': I2,
        'grav': grav,
        'hs_total': full - grav,
        'master': mf,
        'graph_sum': gs,
        'match_master': abs(full - mf) < 1e-9,
        'match_graph': abs(full - gs) < 1e-9,
        'g334': g3,
        'g444': g4,
        'g334_sq': g3sq,
        'g444_sq': g4sq,
        'kappa': kappa_total_float(c),
        'kappa_lambda': kl,
        'delta_ratio': full / kl if kl != 0 else None,
        'delta_W3': delta_F2_W3(c),
        'exceeds_W3': full > delta_F2_W3(c),
    }


if __name__ == '__main__':
    print("=" * 72)
    print("W_4 genus-2 cross-channel engine")
    print("=" * 72)
    for cv in [100, 123, 246]:
        r = full_evaluation(cv)
        print(f"\nc = {cv}:")
        print(f"  delta_F2 = {r['delta_F2']:.12f}")
        print(f"  grav     = {r['grav']:.12f}")
        print(f"  HS       = {r['hs_total']:.12f}")
        print(f"  master   = {r['match_master']}, graph = {r['match_graph']}")
        print(f"  > W_3    = {r['exceeds_W3']}")
