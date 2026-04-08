r"""Exact full-OPE cross-channel correction delta_F2(W_4, c).

THEOREM (first exact full-OPE cross-channel computation for W_4)
================================================================

The genus-2 cross-channel correction for the W_4 = W(sl_4, f_prin) algebra
with ALL higher-spin exchange channels included is:

    delta_F2^full(W_4, c) = R(c) + I_1(c) + I_2(c)

where:

    R(c) = (147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656)
           / (48c(c+24)(3c+46)(7c+68))

    I_1(c) = c * sqrt(42(5c+22)) / (64 * sqrt((c+24)(7c+68)(3c+46)))

    I_2(c) = 42c * sqrt(6(2c-1)(5c+22))
             / ((c+24)(7c+68) * sqrt((5c+3)(10c+197)))

The result decomposes into:

    GRAVITATIONAL part:  (7c + 2148) / (48c)
    RATIONAL HS part:    567c(5c+22) / (16(c+24)(7c+68)(3c+46))
    IRRATIONAL part:     I_1(c) + I_2(c)

DERIVATION
==========

Master formula (verified by independent per-graph symbolic computation):

    192c * delta_F2 = 3c*g334 + 28c + 162*g334^2 + 288*g334*g444 + 8592

where g334, g444 are the W_4 OPE structure constants (Hornfeck 1993):

    g334^2 = 42c^2(5c+22) / [(c+24)(7c+68)(3c+46)]
    g444^2 = 112c^2(2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]

Substituting g334^2 and g444^2 (rational in c):
- Terms with even powers of g334, g444 yield R(c)
- The term 3c*g334 yields I_1(c) = sqrt(g334^2)/64 * (3c/(3c)) ...
  More precisely: 3c*g334/(192c) = g334/64 = sqrt(g334^2)/64 = I_1
- The term 288*g334*g444 yields I_2(c) = (3/2)*sqrt(g334^2*g444^2)/c

The rational part further decomposes:
    R(c) = (7c + 2148)/(48c) + 567c(5c+22)/(16(c+24)(7c+68)(3c+46))
         = gravitational   +   rational higher-spin correction

PER-GRAPH CONTRIBUTIONS (mixed-channel amplitudes)
===================================================

    fig-eight:  0                   (single edge, no mixing)
    banana:     (3*g334*g444 + 52) / (4c)
    dumbbell:   0                   (single edge, no mixing)
    theta:      (9*g334^2 + 200) / (16c)
    lollipop:   g334/64 + 7/48
    barbell:    (9*g334^2 + 24*g334*g444 + 616) / (32c)

Sum: (3c*g334 + 28c + 162*g334^2 + 288*g334*g444 + 8592) / (192c)

W_4 FROBENIUS ALGEBRA
======================

Generators: T (weight 2), W3 (weight 3), W4 (weight 4)
Metric: eta_{TT} = c/2, eta_{W3W3} = c/3, eta_{W4W4} = c/4
Propagator: eta^{TT} = 2/c, eta^{W3W3} = 3/c, eta^{W4W4} = 4/c
kappa(W_4) = c/2 + c/3 + c/4 = 13c/12

3-point structure constants:
    C_{TTT} = C_{TW3W3} = C_{TW4W4} = c     (gravitational)
    C_{W3W3W4} = (c/4)*g334                   (W4-exchange)
    C_{W4W4W4} = (c/4)*g444                   (W4 self-coupling)
    C_{TTW3} = C_{TTW4} = C_{W3W3W3} = 0     (parity/OPE)

Z_2 parity: W3 has odd weight, T and W4 have even weight.
At every genus-0 vertex, the number of W3 half-edges must be even.

VERIFICATION PATHS
==================

1. Direct per-graph symbolic computation (sympy, independent derivation)
2. Float graph sum via w4_genus2_cross_channel.py (verified at 10+ c values)
3. Per-graph analytic formulas (each of 6 boundary graphs verified independently)
4. Gravitational limit (g334=g444=0): recovers (7c+2148)/(48c) exactly
5. Large-c limit: delta -> (3*sqrt(10) + 28)/192 + O(1/c) ~ 0.1952
6. Koszul duality: checked at c <-> 246-c (no anomaly expected; verified)
7. Comparison with W_3: delta_F2(W_4) > delta_F2(W_3) = (c+204)/(16c) for all c > 1/2

References:
    thm:theorem-d, op:multi-generator-universality,
    thm:multi-weight-genus-expansion, rem:propagator-weight-universality,
    Hornfeck (1993), Blumenhagen-Eholzer-Honecker-Hornfeck-Hubel (1996)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import comb, factorial
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# Bernoulli numbers and Faber-Pandharipande
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
    r"""Faber-Pandharipande number: (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!"""
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs(B2g) / Fraction(factorial(2 * g)))


# ============================================================================
# W_4 algebra constants
# ============================================================================

CHANNELS = ('T', 'W3', 'W4')
WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}
K4 = 246  # Koszul conductor for sl_4


def kappa_channel(ch: str, c: float) -> float:
    """Per-channel kappa_j = c/j."""
    return c / WEIGHTS[ch]


def kappa_total(c: float) -> float:
    """kappa(W_4) = 13c/12."""
    return 13 * c / 12


# ============================================================================
# OPE structure constants squared (Hornfeck 1993) — RATIONAL in c
# ============================================================================

def g334_squared_exact(c: Fraction) -> Fraction:
    r"""g334^2 = 42c^2(5c+22)/[(c+24)(7c+68)(3c+46)].

    The W3 x W3 -> W4 OPE coupling squared.
    """
    return (Fraction(42) * c**2 * (5 * c + 22)
            / ((c + 24) * (7 * c + 68) * (3 * c + 46)))


def g444_squared_exact(c: Fraction) -> Fraction:
    r"""g444^2 = 112c^2(2c-1)(3c+46)/[(c+24)(7c+68)(10c+197)(5c+3)].

    The W4 x W4 -> W4 self-coupling squared.
    """
    return (Fraction(112) * c**2 * (2 * c - 1) * (3 * c + 46)
            / ((c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3)))


def g334_squared_float(c: float) -> float:
    """g334^2 as float."""
    return 42 * c**2 * (5*c + 22) / ((c + 24) * (7*c + 68) * (3*c + 46))


def g444_squared_float(c: float) -> float:
    """g444^2 as float."""
    return (112 * c**2 * (2*c - 1) * (3*c + 46)
            / ((c + 24) * (7*c + 68) * (10*c + 197) * (5*c + 3)))


# ============================================================================
# The master formula: 192c * delta = 3c*g334 + 28c + 162*g334^2 + 288*g334*g444 + 8592
# ============================================================================

def _master_formula_float(c: float, g334: float, g444: float) -> float:
    """Evaluate delta_F2 from the master formula with given OPE couplings."""
    return (3*c*g334 + 28*c + 162*g334**2 + 288*g334*g444 + 8592) / (192*c)


# ============================================================================
# Three-part decomposition: R(c) + I_1(c) + I_2(c)
# ============================================================================

def rational_part_exact(c: Fraction) -> Fraction:
    r"""Rational part R(c) of delta_F2^full.

    R(c) = (147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656)
           / (48c(c+24)(3c+46)(7c+68))

    This equals grav(c) + rational_hs(c).
    """
    num = (147 * c**4 + 60823 * c**3 + 2360126 * c**2
           + 34360800 * c + 161254656)
    den = 48 * c * (c + 24) * (3 * c + 46) * (7 * c + 68)
    return Fraction(num, den) if isinstance(num, int) else num / den


def rational_part_float(c: float) -> float:
    """Rational part R(c) as float."""
    num = 147*c**4 + 60823*c**3 + 2360126*c**2 + 34360800*c + 161254656
    den = 48*c*(c + 24)*(3*c + 46)*(7*c + 68)
    return num / den


def gravitational_part(c: float) -> float:
    r"""Gravitational-only cross-channel correction.

    delta_F2^grav(W_4, c) = (7c + 2148) / (48c)

    This is the g334=g444=0 limit. Depends only on the
    number of channels and their conformal weights, not on
    OPE structure constants.
    """
    return (7*c + 2148) / (48*c)


def gravitational_part_exact(c: Fraction) -> Fraction:
    """Gravitational part as exact Fraction."""
    return (7 * c + 2148) / (48 * c)


def rational_hs_part_exact(c: Fraction) -> Fraction:
    r"""Rational higher-spin correction.

    R_HS(c) = 567c(5c+22) / (16(c+24)(7c+68)(3c+46))
            = (27/32) * g334^2 / c

    This is the even-power-of-g334 contribution from the OPE.
    It equals (162*g334^2)/(192c) = (27/32)*g334^2/c.
    """
    return (Fraction(567) * c * (5 * c + 22)
            / (16 * (c + 24) * (7 * c + 68) * (3 * c + 46)))


def rational_hs_part_float(c: float) -> float:
    """Rational HS correction as float."""
    return 567*c*(5*c + 22) / (16*(c + 24)*(7*c + 68)*(3*c + 46))


def irrational_part_1(c: float) -> float:
    r"""First irrational term.

    I_1(c) = c * sqrt(42(5c+22)) / (64 * sqrt((c+24)(7c+68)(3c+46)))
           = sqrt(g334^2) / 64

    From the 3c*g334 term in the master formula: 3c*g334/(192c) = g334/64.
    This is the lollipop graph's irrational contribution.
    """
    g334_sq = g334_squared_float(c)
    return math.sqrt(g334_sq) / 64


def irrational_part_2(c: float) -> float:
    r"""Second irrational term.

    I_2(c) = 42c * sqrt(6(2c-1)(5c+22))
             / ((c+24)(7c+68) * sqrt((5c+3)(10c+197)))
           = (3/2) * sqrt(g334^2 * g444^2) / c

    From the 288*g334*g444 term: 288*g334*g444/(192c) = (3/2)*g334*g444/c.
    This combines contributions from the banana and barbell graphs.
    """
    g334_sq = g334_squared_float(c)
    g444_sq = g444_squared_float(c)
    return 1.5 * math.sqrt(g334_sq * g444_sq) / c


def delta_F2_full(c: float) -> float:
    r"""The FULL cross-channel correction delta_F2(W_4, c).

    delta_F2^full = R(c) + I_1(c) + I_2(c)

    Valid for c > 1/2 (unitarity bound for g444^2 > 0).
    """
    return rational_part_float(c) + irrational_part_1(c) + irrational_part_2(c)


def delta_F2_full_via_master(c: float) -> float:
    """Compute delta_F2 via the master formula (independent path)."""
    g334 = math.sqrt(g334_squared_float(c))
    g444 = math.sqrt(g444_squared_float(c))
    return _master_formula_float(c, g334, g444)


def higher_spin_correction(c: float) -> float:
    """Total higher-spin correction: delta_F2^full - delta_F2^grav."""
    return delta_F2_full(c) - gravitational_part(c)


def higher_spin_correction_decomposed(c: float) -> Dict[str, float]:
    """Decompose the higher-spin correction into rational and irrational parts."""
    return {
        'rational_hs': rational_hs_part_float(c),
        'irrational_1': irrational_part_1(c),
        'irrational_2': irrational_part_2(c),
        'total_hs': higher_spin_correction(c),
    }


# ============================================================================
# Per-graph analytic formulas
# ============================================================================

def per_graph_mixed_symbolic() -> Dict[str, str]:
    """Analytic formulas for each boundary graph's mixed amplitude.

    These are polynomials in (g334, g444) with rational-in-c coefficients,
    derived by independent symbolic computation.
    """
    return {
        'fig_eight':  '0',
        'banana':     '(3*g334*g444 + 52) / (4c)',
        'dumbbell':   '0',
        'theta':      '(9*g334^2 + 200) / (16c)',
        'lollipop':   'g334/64 + 7/48',
        'barbell':    '(9*g334^2 + 24*g334*g444 + 616) / (32c)',
    }


def per_graph_mixed_float(c: float) -> Dict[str, float]:
    """Per-graph mixed amplitudes evaluated numerically."""
    g334 = math.sqrt(g334_squared_float(c))
    g444 = math.sqrt(g444_squared_float(c))
    return {
        'fig_eight':  0.0,
        'banana':     (3*g334*g444 + 52) / (4*c),
        'dumbbell':   0.0,
        'theta':      (9*g334**2 + 200) / (16*c),
        'lollipop':   g334/64 + 7.0/48,
        'barbell':    (9*g334**2 + 24*g334*g444 + 616) / (32*c),
    }


def per_graph_grav_only(c: float) -> Dict[str, float]:
    """Per-graph mixed amplitudes at g334=g444=0 (gravitational only)."""
    return {
        'fig_eight':  0.0,
        'banana':     52 / (4*c),       # = 13/c
        'dumbbell':   0.0,
        'theta':      200 / (16*c),     # = 25/(2c)
        'lollipop':   7.0/48,
        'barbell':    616 / (32*c),     # = 77/(4c)
    }


def verify_per_graph_sum(c: float) -> Dict[str, Any]:
    """Verify that per-graph contributions sum to the total."""
    pg = per_graph_mixed_float(c)
    graph_sum = sum(pg.values())
    total = delta_F2_full(c)
    return {
        'per_graph': pg,
        'graph_sum': graph_sum,
        'total': total,
        'match': abs(graph_sum - total) < 1e-10,
    }


# ============================================================================
# Large-c asymptotics
# ============================================================================

def large_c_limit() -> float:
    r"""Leading constant as c -> infinity.

    g334^2 -> 42*5/7*3 = 210/21 = 10
    g444^2 -> 112*2*3/(7*10*5) = 672/350 = 48/25

    g334 -> sqrt(10), g444 -> sqrt(48/25) = 4*sqrt(3)/5

    192c * delta -> 3c*sqrt(10) + 28c + 162*10 + 288*sqrt(10)*4*sqrt(3)/5 + 8592
    The leading (O(c)) terms: 3*sqrt(10) + 28
    So delta -> (3*sqrt(10) + 28) / 192

    Return this value.
    """
    return (3*math.sqrt(10) + 28) / 192


def large_c_subleading() -> Dict[str, float]:
    r"""Large-c expansion: delta = A + B/c + O(1/c^2).

    Leading: A = (3*sqrt(10) + 28) / 192
    Subleading: B = (162*10 + 288*sqrt(10)*4*sqrt(3)/5 + 8592) / 192
              = (1620 + 1152*sqrt(30)/5 + 8592) / 192
              = (10212 + 1152*sqrt(30)/5) / 192
    """
    A = (3*math.sqrt(10) + 28) / 192
    B = (162*10 + 288*math.sqrt(10)*4*math.sqrt(3)/5 + 8592) / 192
    return {'A': A, 'B': B}


# ============================================================================
# Koszul duality: c <-> 246 - c
# ============================================================================

def koszul_dual_check(c: float) -> Dict[str, float]:
    """Evaluate delta_F2 at c and at 246-c.

    At the self-dual point c=123, the function should be well-defined.
    kappa(c) + kappa(246-c) = 13*246/12 = 533/2.
    """
    if c <= 0.5 or c >= 245.5:
        raise ValueError(f"Need 1/2 < c < 245.5, got c={c}")
    d1 = delta_F2_full(c)
    d2 = delta_F2_full(K4 - c)
    return {
        'c': c,
        'c_dual': K4 - c,
        'delta_at_c': d1,
        'delta_at_dual': d2,
        'delta_sum': d1 + d2,
        'kappa_sum': kappa_total(c) + kappa_total(K4 - c),
        'kappa_sum_expected': 13*246/12,
    }


# ============================================================================
# Comparison with W_3
# ============================================================================

def delta_F2_W3(c: float) -> float:
    """W_3 cross-channel correction: (c+204)/(16c)."""
    return (c + 204) / (16*c)


def w3_w4_comparison(c: float) -> Dict[str, float]:
    """Compare W_3 and W_4 cross-channel corrections."""
    w3 = delta_F2_W3(c)
    w4 = delta_F2_full(c)
    return {
        'c': c,
        'delta_W3': w3,
        'delta_W4': w4,
        'ratio': w4 / w3 if w3 != 0 else float('inf'),
        'excess': w4 - w3,
    }


# ============================================================================
# Direct graph sum verification (independent computation)
# ============================================================================

def _C3(i: str, j: str, k: str, c: float,
        g334: float, g444: float) -> float:
    """W_4 three-point structure constant."""
    odd_count = sum(1 for x in [i, j, k] if x == 'W3')
    if odd_count % 2 == 1:
        return 0.0
    labels = tuple(sorted([i, j, k]))
    if labels in [('T', 'T', 'T'), ('T', 'W3', 'W3'), ('T', 'W4', 'W4')]:
        return c
    if labels == ('T', 'T', 'W4'):
        return 0.0
    if labels == ('W3', 'W3', 'W4'):
        return (c / 4) * g334
    if labels == ('W4', 'W4', 'W4'):
        return (c / 4) * g444
    return 0.0


def _V04(i1: str, i2: str, j1: str, j2: str,
         c: float, g334: float, g444: float) -> float:
    """Genus-0 four-point vertex via factorization."""
    total = 0.0
    for m in CHANNELS:
        c3a = _C3(i1, i2, m, c, g334, g444)
        if c3a == 0.0:
            continue
        c3b = _C3(m, j1, j2, c, g334, g444)
        if c3b == 0.0:
            continue
        total += (WEIGHTS[m] / c) * c3a * c3b
    return total


# Genus-2 stable graphs (7 graphs)
_GENUS2_GRAPHS = [
    # (name, vertices=[(genus, valence)], edges=[(type, v1, v2)], aut)
    ('smooth',    [(2, 0)],          [],                                     1),
    ('fig_eight', [(1, 2)],          [('self', 0)],                          2),
    ('banana',    [(0, 4)],          [('self', 0), ('self', 0)],             8),
    ('dumbbell',  [(1, 1), (1, 1)],  [('bridge', 0, 1)],                    2),
    ('theta',     [(0, 3), (0, 3)],  [('bridge', 0, 1)]*3,                 12),
    ('lollipop',  [(0, 3), (1, 1)],  [('self', 0), ('bridge', 0, 1)],       2),
    ('barbell',   [(0, 3), (0, 3)],  [('self', 0), ('self', 1),
                                      ('bridge', 0, 1)],                     8),
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
                     c: float, g334: float, g444: float) -> float:
    """Compute amplitude A(Gamma, sigma) without 1/|Aut| factor."""
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
                vf_v = _C3(he[0], he[1], he[2], c, g334, g444)
            elif len(he) == 4:
                vf_v = _V04(he[0], he[1], he[2], he[3], c, g334, g444)
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


def direct_graph_sum(c: float) -> Dict[str, Any]:
    """Compute delta_F2 by direct enumeration over all graphs and channels.

    This is the independent verification path: no analytic formulas used.
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

        for sigma in cartprod(CHANNELS, repeat=n_e):
            amp = _graph_amplitude(idx, sigma, c, g334, g444) / aut
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
# Full evaluation with all diagnostics
# ============================================================================

def full_evaluation(c: float) -> Dict[str, Any]:
    """Complete evaluation with all paths, decompositions, and comparisons."""
    g334_sq = g334_squared_float(c)
    g444_sq = g444_squared_float(c)
    g334 = math.sqrt(g334_sq)
    g444 = math.sqrt(g444_sq)

    R = rational_part_float(c)
    I1 = irrational_part_1(c)
    I2 = irrational_part_2(c)
    full = R + I1 + I2
    grav = gravitational_part(c)
    hs_rat = rational_hs_part_float(c)

    # Independent verification paths
    master = _master_formula_float(c, g334, g444)
    graph = direct_graph_sum(c)['delta_F2']

    kl = kappa_total(c) * float(lambda_fp(2))

    return {
        'c': c,
        'delta_F2_full': full,
        'R': R,
        'I_1': I1,
        'I_2': I2,
        'grav': grav,
        'hs_rational': hs_rat,
        'hs_irrational': I1 + I2,
        'hs_total': full - grav,
        'master_formula': master,
        'graph_sum': graph,
        'match_master': abs(full - master) < 1e-10,
        'match_graph': abs(full - graph) < 1e-10,
        'g334': g334,
        'g444': g444,
        'g334_sq': g334_sq,
        'g444_sq': g444_sq,
        'kappa': kappa_total(c),
        'kappa_lambda': kl,
        'delta_ratio': full / kl if kl != 0 else None,
        'delta_W3': delta_F2_W3(c),
        'exceeds_W3': full > delta_F2_W3(c),
    }


# ============================================================================
# Numerical table
# ============================================================================

def numerical_table(c_values: Optional[List[float]] = None) -> List[Dict[str, Any]]:
    """Evaluate delta_F2^full at a range of central charges."""
    if c_values is None:
        c_values = [1, 2, 4, 10, 26, 50, 100, 123, 200, 246]
    results = []
    for cv in c_values:
        if cv <= 0.5:
            continue
        r = full_evaluation(cv)
        results.append(r)
    return results


if __name__ == '__main__':
    print("=" * 72)
    print("Exact full-OPE delta_F2(W_4, c)")
    print("=" * 72)
    print()
    print("FORMULA:")
    print("  delta = R(c) + I_1(c) + I_2(c)")
    print()
    print("  R(c) = (147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656)")
    print("         / (48c(c+24)(3c+46)(7c+68))")
    print()
    print("  I_1(c) = c*sqrt(42(5c+22)) / (64*sqrt((c+24)(7c+68)(3c+46)))")
    print()
    print("  I_2(c) = 42c*sqrt(6(2c-1)(5c+22))")
    print("           / ((c+24)(7c+68)*sqrt((5c+3)(10c+197)))")
    print()

    for cv in [10, 50, 100, 123, 246]:
        r = full_evaluation(cv)
        print(f"c = {cv}:")
        print(f"  full   = {r['delta_F2_full']:.12f}")
        print(f"  grav   = {r['grav']:.12f}")
        print(f"  HS     = {r['hs_total']:.12f} ({100*r['hs_total']/r['grav']:.1f}% of grav)")
        print(f"  match  = master:{r['match_master']}, graph:{r['match_graph']}")
        print()
