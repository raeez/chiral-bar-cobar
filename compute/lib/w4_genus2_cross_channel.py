r"""W₄ genus-2 cross-channel correction: the first 3-channel computation.

Computes delta_F2(W_4) -- the genus-2 cross-channel correction for the W_4
algebra, the first algebra with THREE independent propagator channels (T, W3, W4).

MATHEMATICAL FRAMEWORK
======================

The W_4 = W(sl_4, f_prin) algebra has three strong generators:
    T   (conformal weight 2, Virasoro stress tensor)
    W3  (conformal weight 3, spin-3 current)
    W4  (conformal weight 4, spin-4 current)

Modular characteristic (AP1, landscape_census.tex):
    kappa_T  = c/2,  kappa_{W3} = c/3,  kappa_{W4} = c/4
    kappa(W_4) = c*(H_4 - 1) = 13c/12

Koszul duality: W_4 at c <-> W_4 at (246 - c).
Self-dual point: c = 123.

PARITY SELECTION RULE
=====================
Z_2 symmetry: W3 -> -W3 (odd weight), T -> +T, W4 -> +W4 (even weight).
At every vertex, the number of W3 half-edges must be even.

FROBENIUS ALGEBRA
=================

Multiplication table c_{ij}^k (from the bar r-matrix, AP19):
    T*T   = 2T
    T*W3  = 3W3
    T*W4  = 4W4
    W3*W3 = 2T + g334*W4
    W3*W4 = -(3/4)*g334*W3    (metric adjoint, w4_ds_ope_extraction.py)
    W4*W4 = 2T + g444*W4

Three-point structure constants C_{ijk} = eta_{kk} * c_{ij}^k:
    C_{TTT}    = c       C_{TW3W3}  = c       C_{TW4W4}  = c
    C_{W3W3W4} = (c/4)*g334
    C_{W4W4W4} = (c/4)*g444
    All others with odd W3-count vanish.

OPE STRUCTURE CONSTANTS (Hornfeck 1993, w4_ds_ope_extraction.py):
    g334^2 = 42*c^2*(5c+22) / [(c+24)(7c+68)(3c+46)]
    g444^2 = 112*c^2*(2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]

RESULT
======
The cross-channel correction decomposes as:

    delta_F2(W_4) = R(c) + I(c)

where R(c) is a rational function (depending on g334^2) and I(c) is an
irrational function (depending on sqrt(g334^2) and sqrt(g334^2*g444^2)):

    R(c) = [147*c^4 + 60823*c^3 + 2360126*c^2 + 34360800*c + 161254656]
            / [48*c*(c+24)(3c+46)(7c+68)]

    I(c) = sqrt(g334^2)/64 + (3/2)*sqrt(g334^2*g444^2)/c

The irrational part arises from the lollipop graph (sqrt(g334^2) term)
and the banana + barbell graphs (sqrt(g334^2*g444^2) term). It represents
a genuinely NEW structure not present in the W_3 computation.

Per-graph breakdown (mixed-channel amplitudes):
    fig-eight:  0
    banana:     13/c + (3/4)*sqrt(g334^2*g444^2)/c
    dumbbell:   0
    theta:      [3045c^3 + 107158c^2 + 1575200c + 7507200] / [8c(c+24)(3c+46)(7c+68)]
    lollipop:   7/48 + sqrt(g334^2)/64
    barbell:    7*[1059c^3 + 45914c^2 + 693088c + 3303168] / [16c(c+24)(3c+46)(7c+68)]
                + (3/4)*sqrt(g334^2*g444^2)/c

Large-c asymptotics:
    delta_F2 -> (3*sqrt(10) + 28)/192 + O(1/c)  (approx 0.1952)
    Compare W_3: delta_F2 -> 1/16 = 0.0625

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    thm:multi-weight-genus-expansion, rem:propagator-weight-universality,
    w4_ds_ope_extraction.py
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartprod
from math import comb, factorial
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt,
    together,
)


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
    r"""Faber-Pandharipande number lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!"""
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B2g = _bernoulli(2 * g)
    abs_B2g = abs(B2g)
    return (Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            * abs_B2g / Fraction(factorial(2 * g)))


# ============================================================================
# W_4 algebra data
# ============================================================================

CHANNELS = ['T', 'W3', 'W4']
WEIGHTS = {'T': 2, 'W3': 3, 'W4': 4}
K4 = 246  # Complementarity sum for sl_4: c + c' = 246


def kappa_channel(ch: str, c_val: float) -> float:
    """Per-channel kappa: kappa_j = c/j."""
    return c_val / WEIGHTS[ch]


def kappa_total_val(c_val: float) -> float:
    """Total kappa(W_4) = 13c/12."""
    return sum(kappa_channel(ch, c_val) for ch in CHANNELS)


# ============================================================================
# OPE structure constants (Hornfeck 1993)
# ============================================================================

c_sym = Symbol('c', positive=True)


def g334_squared(c_val=None):
    r"""g334^2 = 42*c^2*(5c+22) / [(c+24)(7c+68)(3c+46)].

    The W3 x W3 -> W4 primary coupling squared.
    """
    cc = c_val if c_val is not None else c_sym
    return 42 * cc**2 * (5 * cc + 22) / ((cc + 24) * (7 * cc + 68) * (3 * cc + 46))


def g444_squared(c_val=None):
    r"""g444^2 = 112*c^2*(2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)].

    The W4 x W4 -> W4 self-coupling squared.
    """
    cc = c_val if c_val is not None else c_sym
    return (112 * cc**2 * (2 * cc - 1) * (3 * cc + 46)
            / ((cc + 24) * (7 * cc + 68) * (10 * cc + 197) * (5 * cc + 3)))


def g334_g444_product_squared(c_val=None):
    r"""(g334*g444)^2 = g334^2 * g444^2 (rational in c)."""
    cc = c_val if c_val is not None else c_sym
    return cancel(g334_squared(cc) * g444_squared(cc))


# ============================================================================
# Frobenius algebra: 3-point functions
# ============================================================================

def C3_generic(i: str, j: str, k: str, cc, g334, g444):
    """3-point structure constant C_{ijk} with symbolic OPE coefficients.

    Parameters:
        cc: central charge (number or symbol)
        g334: W3*W3->W4 coupling (signed, number or symbol)
        g444: W4*W4->W4 self-coupling (signed, number or symbol)
    """
    labels = tuple(sorted([i, j, k]))
    w3_count = sum(1 for x in (i, j, k) if x == 'W3')
    if w3_count % 2 == 1:
        return 0
    if labels in [('T', 'T', 'T'), ('T', 'W3', 'W3'), ('T', 'W4', 'W4')]:
        return cc
    if labels == ('W3', 'W3', 'W4'):
        return (cc / 4) * g334
    if labels == ('W4', 'W4', 'W4'):
        return (cc / 4) * g444
    return 0


def V04_generic(i1, i2, j1, j2, cc, g334, g444):
    r"""Genus-0 4-point vertex V_{0,4}(i1,i2|j1,j2) = sum_m eta^{mm} C_{i1 i2 m} C_{m j1 j2}.

    For W_4: V = 2c + (c/4)*c_{i1i2}^{W4}*c_{j1j2}^{W4}
    where the W4 intermediate channel gives a c-dependent correction
    beyond the universal T-exchange value of 2c.
    """
    total = 0
    for m in CHANNELS:
        w = WEIGHTS[m]
        eta_inv = w / cc  # eta^{mm} = weight/c
        total += eta_inv * C3_generic(i1, i2, m, cc, g334, g444) * C3_generic(m, j1, j2, cc, g334, g444)
    return total


# ============================================================================
# Genus-2 stable graph data (7 graphs at g=2, n=0)
# ============================================================================

GENUS2_GRAPHS = [
    {'name': 'smooth',    'vertices': [(2, 0)],          'edges': [],                                              'aut': 1},
    {'name': 'fig_eight', 'vertices': [(1, 2)],          'edges': [('self', 0)],                                   'aut': 2},
    {'name': 'banana',    'vertices': [(0, 4)],          'edges': [('self', 0), ('self', 0)],                      'aut': 8},
    {'name': 'dumbbell',  'vertices': [(1, 1), (1, 1)],  'edges': [('bridge', 0, 1)],                             'aut': 2},
    {'name': 'theta',     'vertices': [(0, 3), (0, 3)],  'edges': [('bridge', 0, 1)] * 3,                         'aut': 12},
    {'name': 'lollipop',  'vertices': [(0, 3), (1, 1)],  'edges': [('self', 0), ('bridge', 0, 1)],                'aut': 2},
    {'name': 'barbell',   'vertices': [(0, 3), (0, 3)],  'edges': [('self', 0), ('self', 1), ('bridge', 0, 1)],   'aut': 8},
]


def _half_edge_channels(graph_idx: int, sigma: Tuple[str, ...]) -> List[List[str]]:
    """For each vertex, return the list of half-edge channels."""
    G = GENUS2_GRAPHS[graph_idx]
    n_v = len(G['vertices'])
    channels_at_v: List[List[str]] = [[] for _ in range(n_v)]
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


# ============================================================================
# Graph amplitude computation (generic, works with float or sympy)
# ============================================================================

def graph_amplitude_generic(graph_idx: int, sigma: Tuple[str, ...],
                            cc, g334_val, g444_val):
    """Compute the amplitude A(Gamma, sigma) WITHOUT the 1/|Aut| factor.

    Works with any numeric type (float, Fraction, sympy expression).
    Returns 0 if any vertex violates Z_2 parity.
    """
    G = GENUS2_GRAPHS[graph_idx]
    if G['name'] == 'smooth':
        return 0

    channels_at_v = _half_edge_channels(graph_idx, sigma)

    # Parity check
    for v_idx, (gv, nv) in enumerate(G['vertices']):
        w3c = sum(1 for ch in channels_at_v[v_idx] if ch == 'W3')
        if w3c % 2 == 1:
            return 0

    # Propagator product
    prop_product = 1
    for edge_idx in range(len(G['edges'])):
        ch = sigma[edge_idx]
        prop_product *= WEIGHTS[ch] / cc

    # Vertex factors
    vertex_product = 1
    for v_idx, (gv, nv) in enumerate(G['vertices']):
        he_ch = channels_at_v[v_idx]
        if gv == 0:
            if len(he_ch) == 3:
                vf = C3_generic(he_ch[0], he_ch[1], he_ch[2], cc, g334_val, g444_val)
            elif len(he_ch) == 4:
                vf = V04_generic(he_ch[0], he_ch[1], he_ch[2], he_ch[3],
                                 cc, g334_val, g444_val)
            else:
                vf = 1
        elif gv == 1:
            if len(he_ch) == 1:
                vf = (cc / WEIGHTS[he_ch[0]]) / 24
            elif len(he_ch) == 2:
                if he_ch[0] != he_ch[1]:
                    vf = 0
                else:
                    vf = (cc / WEIGHTS[he_ch[0]]) / 24
            else:
                vf = 0
        else:
            vf = 1  # smooth vertex

        vertex_product *= vf

    return prop_product * vertex_product


def graph_decomposition_generic(graph_idx: int, cc, g334_val, g444_val):
    """Decompose graph amplitude into diagonal and mixed parts."""
    G = GENUS2_GRAPHS[graph_idx]
    n_edges = len(G['edges'])
    aut = G['aut']

    if n_edges == 0:
        return {'diagonal': 0, 'mixed': 0, 'total': 0}

    diagonal = 0
    mixed = 0

    for sigma in cartprod(CHANNELS, repeat=n_edges):
        amp = graph_amplitude_generic(graph_idx, sigma, cc, g334_val, g444_val) / aut
        if len(set(sigma)) <= 1:
            diagonal += amp
        else:
            mixed += amp

    return {'diagonal': diagonal, 'mixed': mixed, 'total': diagonal + mixed}


# ============================================================================
# Symbolic computation (sympy, exact rational functions of c)
# ============================================================================

def compute_delta_F2_symbolic():
    r"""Compute delta_F2(W_4) symbolically with g334, g444 as parameters.

    Returns the cross-channel correction as a polynomial in g334, g444
    with rational-function-of-c coefficients.
    """
    cc = Symbol('c', positive=True)
    g3 = Symbol('g334')
    g4 = Symbol('g444')

    total_mixed = Rational(0)
    per_graph = {}

    for idx, G in enumerate(GENUS2_GRAPHS):
        decomp = graph_decomposition_generic(idx, cc, g3, g4)
        m = cancel(decomp['mixed'])
        per_graph[G['name']] = m
        total_mixed += m

    total_mixed = cancel(total_mixed)
    return {
        'per_graph': per_graph,
        'total_mixed': total_mixed,
        'c': cc,
        'g334': g3,
        'g444': g4,
    }


# Cache the symbolic result
_SYMBOLIC_RESULT = None

def _get_symbolic():
    global _SYMBOLIC_RESULT
    if _SYMBOLIC_RESULT is None:
        _SYMBOLIC_RESULT = compute_delta_F2_symbolic()
    return _SYMBOLIC_RESULT


# ============================================================================
# Numerical evaluation (floating point)
# ============================================================================

def evaluate_at(c_val: float) -> Dict[str, Any]:
    r"""Evaluate delta_F2(W_4) numerically at a specific central charge.

    Requires c > 1/2 for c444^2 > 0 (unitary regime).
    """
    if c_val <= 0.5:
        raise ValueError(f"Requires c > 1/2 for unitarity, got c = {c_val}")

    # OPE data
    c334_sq_v = float(g334_squared(c_val))
    c444_sq_v = float(g444_squared(c_val))
    g334_v = math.sqrt(c334_sq_v)
    g444_v = math.sqrt(c444_sq_v)

    # Per-graph mixed amplitudes
    per_graph = {}
    total_mixed = 0.0

    for idx, G in enumerate(GENUS2_GRAPHS):
        decomp = graph_decomposition_generic(idx, c_val, g334_v, g444_v)
        per_graph[G['name']] = {
            'diagonal': decomp['diagonal'],
            'mixed': decomp['mixed'],
            'total': decomp['total'],
        }
        total_mixed += decomp['mixed']

    kappa_tot = 13 * c_val / 12
    F2_scalar = kappa_tot * float(lambda_fp(2))

    # Rational/irrational decomposition
    rat_part = float(_rational_part_sym().subs(c_sym, c_val))
    irr_part = total_mixed - rat_part

    return {
        'c': c_val,
        'delta_F2': total_mixed,
        'rational_part': rat_part,
        'irrational_part': irr_part,
        'F2_scalar': F2_scalar,
        'delta_ratio': total_mixed / F2_scalar if F2_scalar != 0 else None,
        'kappa_total': kappa_tot,
        'g334': g334_v,
        'g444': g444_v,
        'g334_sq': c334_sq_v,
        'g444_sq': c444_sq_v,
        'per_graph': per_graph,
    }


# ============================================================================
# Closed-form rational part
# ============================================================================

@lru_cache(maxsize=1)
def _rational_part_sym():
    r"""Rational part of delta_F2: substitute g334^2 -> c334_sq, g444 -> 0 in odd terms.

    R(c) = [147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656]
           / [48c(c+24)(3c+46)(7c+68)]
    """
    cc = c_sym
    c334_sq = g334_squared(cc)
    return cancel((28 * cc + 162 * c334_sq + 8592) / (192 * cc))


def rational_part(c_val=None):
    r"""Rational part of delta_F2(W_4).

    R(c) = (147c^4 + 60823c^3 + 2360126c^2 + 34360800c + 161254656)
           / (48c(c+24)(3c+46)(7c+68))
    """
    expr = _rational_part_sym()
    if c_val is not None:
        return float(expr.subs(c_sym, c_val))
    return expr


def irrational_part_numerical(c_val: float) -> float:
    r"""Irrational part of delta_F2(W_4) evaluated numerically.

    I(c) = sqrt(g334^2)/64 + (3/2)*sqrt(g334^2*g444^2)/c
    """
    c334_sq_v = float(g334_squared(c_val))
    c444_sq_v = float(g444_squared(c_val))
    g334_v = math.sqrt(c334_sq_v)
    g444_v = math.sqrt(c444_sq_v)
    return g334_v / 64 + 1.5 * g334_v * g444_v / c_val


# ============================================================================
# Per-graph analytic formulas
# ============================================================================

def per_graph_mixed_formulas():
    r"""Analytic formulas for per-graph cross-channel corrections.

    All boundary graphs with nonzero mixed amplitudes:

    banana:   13/c + (3/4)*sqrt(g334^2*g444^2)/c
    theta:    [3045c^3 + 107158c^2 + 1575200c + 7507200] / [8c(c+24)(3c+46)(7c+68)]
    lollipop: 7/48 + sqrt(g334^2)/64
    barbell:  7*[1059c^3 + 45914c^2 + 693088c + 3303168] / [16c(c+24)(3c+46)(7c+68)]
              + (3/4)*sqrt(g334^2*g444^2)/c
    """
    cc = c_sym
    D = (cc + 24) * (3 * cc + 46) * (7 * cc + 68)
    return {
        'fig_eight': Rational(0),
        'banana_rational': Rational(13) / cc,
        'banana_irrational_coeff': Rational(3, 4) / cc,  # times sqrt(g334^2*g444^2)
        'dumbbell': Rational(0),
        'theta': cancel((3045 * cc**3 + 107158 * cc**2 + 1575200 * cc + 7507200) / (8 * cc * D)),
        'lollipop_rational': Rational(7, 48),
        'lollipop_irrational_coeff': Rational(1, 64),  # times sqrt(g334^2)
        'barbell_rational': cancel(7 * (1059 * cc**3 + 45914 * cc**2 + 693088 * cc + 3303168) / (16 * cc * D)),
        'barbell_irrational_coeff': Rational(3, 4) / cc,  # times sqrt(g334^2*g444^2)
    }


# ============================================================================
# Comparison with W_3
# ============================================================================

def delta_F2_w3(c_val=None):
    r"""W_3 cross-channel correction: (c+204)/(16c)."""
    if c_val is not None:
        return (c_val + 204) / (16 * c_val)
    return (c_sym + 204) / (16 * c_sym)


def w3_comparison_table(c_values=None):
    r"""Compare delta_F2 for W_3 and W_4 at various central charges."""
    if c_values is None:
        c_values = [1, 2, 4, 10, 26, 50, 100, 123, 246]
    rows = []
    for cv in c_values:
        w3 = delta_F2_w3(cv)
        w4_data = evaluate_at(cv)
        rows.append({
            'c': cv,
            'delta_W3': w3,
            'delta_W4': w4_data['delta_F2'],
            'ratio_W4_W3': w4_data['delta_F2'] / w3 if w3 != 0 else None,
        })
    return rows


# ============================================================================
# Koszul duality check
# ============================================================================

def koszul_duality_check(c_val: float):
    r"""Check delta_F2 under Koszul duality c <-> 246 - c.

    At the self-dual point c = 123, delta_F2 should have extremal properties.
    """
    d1 = evaluate_at(c_val)
    d2 = evaluate_at(K4 - c_val)
    return {
        'c': c_val,
        'c_dual': K4 - c_val,
        'delta_at_c': d1['delta_F2'],
        'delta_at_dual': d2['delta_F2'],
        'sum': d1['delta_F2'] + d2['delta_F2'],
        'self_dual_point': K4 / 2,
    }


# ============================================================================
# Propagator variance for W_4
# ============================================================================

def propagator_variance_w4(c_val: float) -> float:
    r"""Propagator variance for the 3-channel W_4 system.

    delta = sum_i f_i^2/kappa_i - (sum_i f_i)^2 / (sum_i kappa_i)

    Requires the quartic gradient f_i on each primary line.
    For the T-line: f_T is known (Virasoro quartic contact).
    For the W3-line and W4-line: requires full multi-variable quartic data.

    This returns the T-line contribution only (lower bound on full variance).
    """
    # T-line quartic data (same as Virasoro)
    kappa_T = c_val / 2
    Q_T = 10 / (c_val * (5 * c_val + 22))
    f_T = 4 * Q_T * (1 + 3 * 2)  # alpha_T = 2 for Virasoro
    # Simplified: f_T = 200*(c+14)/[c*(5c+22)^2] from w3 module
    # But for a lower bound, use just the T-channel contribution
    # This is a placeholder; full computation requires the multi-variable shadow
    return float('nan')  # Not yet computed


# ============================================================================
# Numerical table
# ============================================================================

def numerical_table(c_values=None) -> List[Dict[str, Any]]:
    """Evaluate delta_F2(W_4) at a range of central charges."""
    if c_values is None:
        c_values = [1, 2, 4, 10, 26, 50, 100, 123, 246, 1000]
    return [evaluate_at(cv) for cv in c_values]
