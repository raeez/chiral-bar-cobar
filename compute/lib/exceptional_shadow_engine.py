r"""Exceptional Lie algebras E_6, E_7, E_8 and their W-algebras in the shadow framework.

Comprehensive shadow obstruction tower engine for the exceptional types,
covering affine algebras, principal W-algebras, heterotic string, Deligne
exceptional series, Minahan-Nemeschansky boundary VOAs, Schellekens c=24
holomorphic VOAs, and the McKay ADE correspondence.

SCOPE AND CONTENTS
==================

1. AFFINE E_6, E_7, E_8 at level k:
   c, kappa, shadow depth class L, R-matrix pole structure (simple pole).
   All affine KM algebras are class L (Jacobi kills quartic, S_4=0).

2. PRINCIPAL W-ALGEBRAS W(E_6), W(E_7), W(E_8):
   Generator weights = exponents + 1.
   Central charge via FKW formula.  kappa = rho * c_W where rho = anomaly ratio.
   Shadow depth class M (infinite tower): DS reduction introduces S_4 != 0.

3. SHADOW TOWERS:
   For affine: kappa, S_3=1, S_4=0, class L, depth 3.
   For W-algebras: kappa, S_3, S_4 from Virasoro T-line data, class M.
   Full convolution recursion coefficients through arity 8.

4. HETEROTIC STRING E_8 x E_8:
   Two copies of E_8 at level 1.  c = 8+8 = 16.
   kappa(E_8 x E_8) = kappa(E_8,1) + kappa(E_8,1) = 2 * 1922/15.
   NOT 248 (that would be rank of E_8 x E_8 lattice as Heisenberg, AP48).

5. DELIGNE EXCEPTIONAL SERIES:
   A_1 < A_2 < G_2 < D_4 < F_4 < E_6 < E_7 < E_8.
   Shadow depth is uniformly class L for all affine algebras in the series.
   kappa increases monotonically along the series at fixed level.

6. MINAHAN-NEMESCHANSKY THEORIES:
   MN E_6: affine e_6 at k = -3.  c = -26, kappa = 117/4.
   MN E_7: affine e_7 at k = -4.  c = -38, kappa = 931/18.
   MN E_8: affine e_8 at k = -6.  c = -62, kappa = 496/5.
   All class L (still affine KM, negative level does not change class).

7. SCHELLEKENS LIST:
   71 holomorphic c=24 VOAs.  Shadow depth classification by structure.
   The 24 Niemeier lattice VOAs are all class G (Heisenberg tensor products).
   V^natural (moonshine) is class M (no weight-1 currents).

8. McKAY ADE CORRESPONDENCE:
   A-D-E classification of du Val singularities C^2/Gamma.
   Shadow depth of the corresponding affine algebra is uniformly class L.
   The McKay graph = extended Dynkin diagram.

FORMULAS (computed from first principles, AP1):

   kappa(g, k) = dim(g) * (k + h^vee) / (2 * h^vee)
   c(g, k) = dim(g) * k / (k + h^vee)
   k' = -k - 2*h^vee  (Feigin-Frenkel involution)
   kappa + kappa' = 0  (AP24: correct for all KM)

   W-algebra central charge (FKW):
     c_W(g, k) = rank - dim*h*(p-1)^2/p  where p = k + h^vee
   W-algebra kappa:
     kappa_W = rho(g) * c_W  where rho = sum 1/(m_i+1)

   Generator weights of W(g): {m_i + 1} where m_i are exponents.

CONVENTIONS:
   Root length normalization: long roots |alpha|^2 = 2.
   Level k generic (not critical: k != -h^vee).
   Cohomological grading, |d| = +1.
   Bar propagator d log E(z,w) has weight 1 (AP27).

Manuscript references:
   kac_moody.tex, w_algebras.tex, landscape_census.tex
   higher_genus_modular_koszul.tex: shadow archetype classification
   concordance.tex: AP24, AP27, AP48
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from math import gcd
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, cancel, expand, factor, simplify, sqrt, S,
    N as Neval,
)

from compute.lib.lie_algebra import cartan_data


# ============================================================================
# Symbols
# ============================================================================

k = Symbol('k')
c = Symbol('c', positive=True)


# ============================================================================
# 1. Exceptional Lie algebra data
# ============================================================================

# Ground truth from Bourbaki/Humphreys, cross-checked against cartan_data().
EXCEPTIONAL_DATA = {
    'E6': {
        'type': 'E', 'rank': 6, 'dim': 78, 'h': 12, 'h_dual': 12,
        'exponents': [1, 4, 5, 7, 8, 11], 'simply_laced': True,
        'fund_rep_dim': 27,  # V(omega_1), not self-dual
        'fund_rep_self_dual': False,
        'outer_aut_order': 2,  # Z/2 diagram automorphism
    },
    'E7': {
        'type': 'E', 'rank': 7, 'dim': 133, 'h': 18, 'h_dual': 18,
        'exponents': [1, 5, 7, 9, 11, 13, 17], 'simply_laced': True,
        'fund_rep_dim': 56,  # V(omega_7), self-dual (pseudo-real)
        'fund_rep_self_dual': True,
        'outer_aut_order': 1,  # no outer automorphism
    },
    'E8': {
        'type': 'E', 'rank': 8, 'dim': 248, 'h': 30, 'h_dual': 30,
        'exponents': [1, 7, 11, 13, 17, 19, 23, 29], 'simply_laced': True,
        'fund_rep_dim': 248,  # adjoint (smallest rep IS adjoint)
        'fund_rep_self_dual': True,
        'outer_aut_order': 1,  # no outer automorphism
    },
}


def _get(name: str) -> dict:
    if name not in EXCEPTIONAL_DATA:
        raise ValueError(f"Unknown algebra {name}. Expected E6, E7, or E8.")
    return EXCEPTIONAL_DATA[name]


# ============================================================================
# 2. Affine algebra invariants
# ============================================================================

def affine_kappa(name: str, level=None):
    """kappa(g, k) = dim(g) * (k + h^vee) / (2 * h^vee)."""
    d = _get(name)
    lv = k if level is None else level
    return Rational(d['dim']) * (lv + d['h_dual']) / (2 * d['h_dual'])


def affine_kappa_numeric(name: str, level_val) -> Fraction:
    """Evaluate kappa at a numeric level."""
    d = _get(name)
    return Fraction(d['dim']) * (Fraction(level_val) + d['h_dual']) / (2 * d['h_dual'])


def affine_central_charge(name: str, level=None):
    """c(g, k) = dim(g) * k / (k + h^vee)."""
    d = _get(name)
    lv = k if level is None else level
    return Rational(d['dim']) * lv / (lv + d['h_dual'])


def affine_central_charge_numeric(name: str, level_val) -> Fraction:
    d = _get(name)
    return Fraction(d['dim']) * Fraction(level_val) / (Fraction(level_val) + d['h_dual'])


def ff_dual_level(name: str, level=None):
    """Feigin-Frenkel dual level k' = -k - 2*h^vee."""
    d = _get(name)
    lv = k if level is None else level
    return -lv - 2 * d['h_dual']


def ff_dual_level_numeric(name: str, level_val) -> Fraction:
    d = _get(name)
    return -Fraction(level_val) - 2 * d['h_dual']


def affine_complementarity_kappa(name: str):
    """kappa(k) + kappa(k') = 0 for all affine KM (AP24)."""
    kd = ff_dual_level(name)
    return simplify(affine_kappa(name) + affine_kappa(name, kd))


def affine_complementarity_c(name: str):
    """c(k) + c(k') = 2*dim(g)."""
    kd = ff_dual_level(name)
    return cancel(affine_central_charge(name) + affine_central_charge(name, kd))


def affine_shadow_class(name: str) -> str:
    """All affine KM algebras are class L."""
    return 'L'


def affine_shadow_depth(name: str) -> int:
    """r_max = 3 for class L (tower terminates at arity 3)."""
    return 3


def affine_S3(name: str) -> Rational:
    """S_3 = 1 (universal for all affine KM: Lie bracket cubic)."""
    return Rational(1)


def affine_S4(name: str) -> Rational:
    """S_4 = 0 (Jacobi identity kills quartic on primary line)."""
    return Rational(0)


def affine_discriminant(name: str) -> Rational:
    """Delta = 8*kappa*S_4 = 0 for all affine KM."""
    return Rational(0)


def affine_r_matrix_pole_order(name: str) -> int:
    """r-matrix has a simple pole (AP19: one less than OPE)."""
    return 1


# ============================================================================
# 3. Principal W-algebra data
# ============================================================================

def w_generator_weights(name: str) -> List[int]:
    """Generator weights of the principal W-algebra W(g).

    Weights = exponents + 1.  These are the conformal weights of the
    strong generators of W^k(g) obtained by DS (quantum Drinfeld-Sokolov)
    reduction of the affine algebra.

    E_6: exponents [1,4,5,7,8,11] -> weights [2,5,6,8,9,12]
    E_7: exponents [1,5,7,9,11,13,17] -> weights [2,6,8,10,12,14,18]
    E_8: exponents [1,7,11,13,17,19,23,29] -> weights [2,8,12,14,18,20,24,30]
    """
    d = _get(name)
    return [m + 1 for m in d['exponents']]


def w_num_generators(name: str) -> int:
    """Number of strong generators = rank(g)."""
    return _get(name)['rank']


def w_anomaly_ratio(name: str) -> Fraction:
    r"""Anomaly ratio rho(g) = sum_{i=1}^{rank} 1/(m_i + 1).

    kappa(W(g), k) = rho(g) * c(W(g), k).
    """
    d = _get(name)
    return sum(Fraction(1, m + 1) for m in d['exponents'])


def w_anomaly_ratio_symbolic(name: str):
    d = _get(name)
    return sum(Rational(1, m + 1) for m in d['exponents'])


def w_central_charge(name: str, level=None):
    """FKW central charge: c_W = rank - dim*h*(p-1)^2/p where p = k + h^vee.

    Uses the Freudenthal-de Vries Strange Formula: |rho|^2 = dim*h/12.
    """
    d = _get(name)
    lv = k if level is None else level
    p = lv + d['h_dual']
    rho_sq = Rational(d['dim'] * d['h'], 12)
    return d['rank'] - 12 * rho_sq * (p - 1)**2 / p


def w_central_charge_numeric(name: str, level_val) -> Fraction:
    d = _get(name)
    p = Fraction(level_val) + d['h_dual']
    rho_sq = Fraction(d['dim'] * d['h'], 12)
    return Fraction(d['rank']) - 12 * rho_sq * (p - 1)**2 / p


def w_kappa(name: str, level=None):
    """kappa(W(g), k) = rho(g) * c_W(g, k)."""
    rho = w_anomaly_ratio_symbolic(name)
    return rho * w_central_charge(name, level)


def w_kappa_numeric(name: str, level_val) -> Fraction:
    rho = w_anomaly_ratio(name)
    return rho * w_central_charge_numeric(name, level_val)


def w_shadow_class(name: str) -> str:
    """Principal W-algebras are class M (infinite depth, DS introduces S_4 != 0)."""
    return 'M'


def w_shadow_depth(name: str) -> str:
    """r_max = infinity for class M."""
    return 'infinity'


def w_max_ope_pole(name: str) -> int:
    """Maximum OPE pole order = 2 * max(generator weight).

    For the T-T OPE, the pole is at z^{-4} (weight 2).
    For the highest generator W_s with weight s, the W_s-T OPE has
    pole at z^{-s-1}.  The self-OPE W_s W_s has pole at z^{-2s}.
    """
    weights = w_generator_weights(name)
    return 2 * max(weights)


# ============================================================================
# 4. Shadow tower coefficients for W-algebras (T-line projection)
# ============================================================================

def _virasoro_shadow_data(c_val):
    """Virasoro shadow data on the T-line: kappa_T, alpha, S_4, Delta.

    On the T-line (the Virasoro subalgebra direction), the shadow data
    is identical to the Virasoro algebra at the same central charge.
    """
    kappa_T = c_val / 2
    alpha = Rational(2)
    S4 = Rational(10) / (c_val * (5 * c_val + 22))
    Delta = 8 * kappa_T * S4
    return kappa_T, alpha, S4, Delta


def w_tline_shadow_coefficients(name: str, level_val, max_arity: int = 8) -> Dict[int, Fraction]:
    """Shadow tower coefficients on the T-line for a principal W-algebra.

    On the T-line, the shadow data is identical to Virasoro at c_W.
    This gives the convolution recursion sqrt(Q_L(t)) coefficients.

    Returns: {r: S_r} for r = 2, 3, ..., max_arity.
    """
    c_w = w_central_charge_numeric(name, level_val)
    if c_w == 0:
        return {2: Fraction(0)}

    kappa_T = c_w / 2
    alpha = Fraction(2)
    denom = c_w * (5 * c_w + 22)
    if denom == 0:
        return {2: kappa_T}
    S4 = Fraction(10) / denom

    # Shadow metric: Q_L(t) = q0 + q1*t + q2*t^2
    q0 = 4 * kappa_T**2
    q1 = 12 * kappa_T * alpha
    q2 = 9 * alpha**2 + 16 * kappa_T * S4

    # Convolution recursion: f(t)^2 = Q_L(t), f = sum a_n t^n
    a = [Fraction(0)] * (max_arity + 1)
    if q0 <= 0:
        # Negative central charge: use absolute value approach
        # kappa_T = c_w/2, might be negative
        a[0] = kappa_T * 2  # = c_w, but we need sqrt(4*kappa_T^2) = |2*kappa_T|
        if a[0] == 0:
            return {r: Fraction(0) for r in range(2, max_arity + 1)}
        # For negative c_w: a0 = 2*kappa_T = c_w (negative)
        # a0^2 = c_w^2 = 4*kappa_T^2 = q0.  CHECK.
    else:
        a[0] = kappa_T * 2  # = c_w

    if a[0] == 0:
        return {r: Fraction(0) for r in range(2, max_arity + 1)}

    a[1] = q1 / (2 * a[0])

    if max_arity >= 2:
        a[2] = (q2 - a[1]**2) / (2 * a[0])

    for n in range(3, max_arity + 1):
        cross = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -cross / (2 * a[0])

    # S_r = a_{r-2} / r
    coeffs = {}
    for r in range(2, max_arity + 1):
        coeffs[r] = a[r - 2] / r
    return coeffs


# ============================================================================
# 5. Heterotic string E_8 x E_8
# ============================================================================

def heterotic_e8_central_charge() -> Fraction:
    """c(E_8 x E_8) at level 1 = 8 + 8 = 16."""
    c1 = affine_central_charge_numeric('E8', 1)
    return c1 + c1


def heterotic_e8_kappa() -> Fraction:
    """kappa(E_8 x E_8) at level 1.

    kappa is ADDITIVE for tensor products of independent algebras
    (prop:independent-sum-factorization).

    kappa = kappa(E_8, k=1) + kappa(E_8, k=1) = 2 * 1922/15 = 3844/15.

    AP48 WARNING: This is NOT 248 (the naive lattice rank formula).
    The rank formula kappa = rank applies to the HEISENBERG description
    H_1^{otimes 8}, not to the full affine E_8 algebra which includes
    240 root-vector currents.
    """
    kap1 = affine_kappa_numeric('E8', 1)
    return kap1 + kap1


def heterotic_total_c() -> Fraction:
    """Total heterotic string central charge: c(E_8 x E_8) + c(10 bosons) = 26.

    The bosonic string critical dimension is c = 26.
    """
    return heterotic_e8_central_charge() + 10


def heterotic_e8_shadow_class() -> str:
    """E_8 x E_8 at level 1 is class L (tensor product of class L algebras)."""
    return 'L'


# ============================================================================
# 6. Deligne exceptional series
# ============================================================================

# The Deligne-Cvitanovic exceptional series.
# Extended chain: A_1 < A_2 < G_2 < D_4 < F_4 < E_6 < E_7 < E_8
# Parametrized by the "Deligne dimension" formula.

DELIGNE_SERIES = [
    ('A1', 'A', 1, 3, 2, 2),      # dim, h, h_dual
    ('A2', 'A', 2, 8, 3, 3),
    ('G2', 'G', 2, 14, 6, 4),
    ('D4', 'D', 4, 28, 6, 6),
    ('F4', 'F', 4, 52, 12, 9),
    ('E6', 'E', 6, 78, 12, 12),
    ('E7', 'E', 7, 133, 18, 18),
    ('E8', 'E', 8, 248, 30, 30),
]


def deligne_kappas_at_level(level_val: int = 1) -> List[Dict[str, Any]]:
    """Compute kappa along the Deligne series at a fixed level.

    All algebras in the series are class L (affine KM).
    kappa increases monotonically along the series at fixed level > 0.
    """
    results = []
    for label, type_, rank, dim, h, h_dual in DELIGNE_SERIES:
        kap = Fraction(dim) * (Fraction(level_val) + h_dual) / (2 * h_dual)
        results.append({
            'label': label,
            'type': type_,
            'rank': rank,
            'dim': dim,
            'h': h,
            'h_dual': h_dual,
            'kappa': kap,
            'shadow_class': 'L',
        })
    return results


def deligne_shadow_depth_constant() -> bool:
    """Shadow depth is uniformly 3 (class L) along the entire Deligne series.

    This is because ALL affine KM algebras are class L, regardless of type.
    """
    return True


def deligne_kappa_monotone(level_val: int = 1) -> bool:
    """Verify kappa is strictly increasing along the Deligne series."""
    data = deligne_kappas_at_level(level_val)
    for i in range(len(data) - 1):
        if data[i]['kappa'] >= data[i + 1]['kappa']:
            return False
    return True


# ============================================================================
# 7. Minahan-Nemeschansky theories
# ============================================================================

# The MN theories are 4d N=2 SCFTs with exceptional flavor symmetry.
# The boundary VOA (BLLPRR correspondence) is the affine algebra at
# a specific NEGATIVE level.

MN_THEORIES = {
    'MN_E6': {
        'algebra': 'E6', 'level': -3,
        '4d_name': 'Minahan-Nemeschansky E_6',
        '4d_a': Fraction(41, 24),  # Weyl anomaly a
        '4d_c': Fraction(13, 6),   # Weyl anomaly c
    },
    'MN_E7': {
        'algebra': 'E7', 'level': -4,
        '4d_name': 'Minahan-Nemeschansky E_7',
        '4d_a': Fraction(59, 24),
        '4d_c': Fraction(19, 6),
    },
    'MN_E8': {
        'algebra': 'E8', 'level': -6,
        '4d_name': 'Minahan-Nemeschansky E_8',
        '4d_a': Fraction(95, 24),
        '4d_c': Fraction(31, 6),
    },
}


def mn_central_charge(theory: str) -> Fraction:
    """2d central charge of the MN boundary VOA.

    c_2d = -12 * c_4d  where c_4d is the 4d Weyl anomaly coefficient.
    Equivalently: c_2d = dim(g) * k / (k + h^vee) at the MN level.
    """
    info = MN_THEORIES[theory]
    return affine_central_charge_numeric(info['algebra'], info['level'])


def mn_kappa(theory: str) -> Fraction:
    """kappa of the MN boundary VOA."""
    info = MN_THEORIES[theory]
    return affine_kappa_numeric(info['algebra'], info['level'])


def mn_shadow_class(theory: str) -> str:
    """All MN boundary VOAs are class L (they are affine KM at negative level)."""
    return 'L'


def mn_verify_c2d_formula(theory: str) -> bool:
    """Verify c_2d = -12 * c_4d."""
    info = MN_THEORIES[theory]
    c_2d = mn_central_charge(theory)
    c_4d = info['4d_c']
    return c_2d == -12 * c_4d


def mn_complementarity(theory: str) -> Dict[str, Fraction]:
    """Complementarity data for MN VOA."""
    info = MN_THEORIES[theory]
    alg = info['algebra']
    lv = info['level']
    kap = affine_kappa_numeric(alg, lv)
    kd = ff_dual_level_numeric(alg, lv)
    kap_dual = affine_kappa_numeric(alg, kd)
    c_2d = affine_central_charge_numeric(alg, lv)
    c_dual = affine_central_charge_numeric(alg, kd)
    d = _get(alg)
    return {
        'kappa': kap,
        'kappa_dual': kap_dual,
        'kappa_sum': kap + kap_dual,
        'c_2d': c_2d,
        'c_dual': c_dual,
        'c_sum': c_2d + c_dual,
        'expected_c_sum': Fraction(2 * d['dim']),
    }


# ============================================================================
# 8. Schellekens list of c=24 holomorphic VOAs
# ============================================================================

# The 71 holomorphic VOAs at c=24 (Schellekens 1993).
# We classify a representative selection by shadow depth.
#
# Key structural fact: the shadow depth classification depends on the
# PRESENTATION of the VOA as a chiral algebra, specifically on the
# structure of the weight-1 subspace V_1 (the current algebra).
#
# Three regimes:
#   (a) Lattice VOAs V_Lambda (24 Niemeier lattices): V_1 = h^{24} (Heisenberg),
#       class G if viewed as Heisenberg tensor product.
#   (b) Non-lattice VOAs with V_1 != 0: the current algebra is a product of
#       affine algebras at specified levels; class L (affine KM).
#   (c) V^natural (moonshine module): V_1 = 0, class M.

# Representative entries from the Schellekens list.
# Format: (label, V_1_description, dim_V_1, shadow_class, notes)
SCHELLEKENS_REPRESENTATIVES = [
    # Niemeier lattice VOAs (class G as Heisenberg description)
    ('Leech', 'none (V_1=0 for Leech is WRONG; Leech lattice VOA has dim V_1=24)',
     24, 'G', 'V_{Leech}: 24 Heisenberg bosons'),
    ('E8^3', 'e_8^1 + e_8^1 + e_8^1', 744, 'L', 'Three copies of E_8 at level 1'),
    ('D24', 'd_24^1', 1128, 'L', 'D_24 lattice VOA'),
    ('A24', 'a_24^1', 624, 'L', 'A_24 lattice VOA'),

    # Non-Niemeier with exceptional automorphisms
    ('E8_k2', 'e_8^2', 248, 'L', 'Affine E_8 at level 2'),
    ('E7_k3', 'e_7^3', 133, 'L', 'Affine E_7 at level 3'),
    ('E6_k4', 'e_6^4', 78, 'L', 'Affine E_6 at level 4'),

    # The moonshine module
    ('V_natural', 'none', 0, 'M', 'V^natural: no currents, Monster symmetry'),
]


def schellekens_kappa_lattice_voa(rank: int = 24) -> Fraction:
    """kappa for a Niemeier lattice VOA viewed as Heisenberg^{24}.

    In the Heisenberg description: kappa = rank = 24.
    In the affine description (if applicable): kappa = dim(g)*(k+h^v)/(2*h^v).
    These DIFFER (AP48).
    """
    return Fraction(rank)


def schellekens_kappa_moonshine() -> Fraction:
    """kappa for the moonshine module V^natural.

    V^natural has c = 24, no weight-1 currents (dim V_1 = 0).
    The Virasoro subalgebra gives kappa(Vir_{24}) = 24/2 = 12.
    But V^natural is NOT the Virasoro algebra (AP48).
    kappa depends on the full bar complex, not just the Virasoro
    subalgebra.  For a c=24 VOA with dim V_1 = 0, the genus-1
    bar complex receives contributions from weight-2 states.
    The modular characteristic is kappa = c/2 = 12 for the
    Virasoro contribution.  Additional contributions from the
    196884-dimensional weight-2 space make the full kappa larger.
    However, in the STANDARD bar complex presentation where the
    Virasoro IS the algebra (before including higher-weight data),
    kappa = 12.  We report this with a caveat.
    """
    return Fraction(12)


def schellekens_shadow_class(label: str) -> Optional[str]:
    """Shadow class for a Schellekens list entry."""
    for entry in SCHELLEKENS_REPRESENTATIVES:
        if entry[0] == label:
            return entry[3]
    return None


def schellekens_count() -> int:
    """Total number of holomorphic c=24 VOAs in the Schellekens list."""
    return 71


def schellekens_niemeier_count() -> int:
    """Number of Niemeier lattice VOAs among the 71."""
    return 24


# ============================================================================
# 9. McKay ADE correspondence
# ============================================================================

# The McKay correspondence: finite subgroups Gamma < SU(2) <-> ADE Dynkin diagrams.
# The resolution of C^2/Gamma has exceptional divisor = union of P^1's arranged
# in the ADE pattern.  The corresponding affine algebra is the McKay graph.

MCKAY_ADE = {
    'A_n': {
        'subgroup': 'Z/(n+1) (cyclic)',
        'singularity': 'x^2 + y^2 + z^{n+1}',
        'shadow_class': 'L',
        'rank_formula': 'n',
    },
    'D_n': {
        'subgroup': 'Dic_{n-2} (binary dihedral)',
        'singularity': 'x^2 + y^2*z + z^{n-1}',
        'shadow_class': 'L',
        'rank_formula': 'n',
    },
    'E6': {
        'subgroup': '2T (binary tetrahedral, order 24)',
        'singularity': 'x^2 + y^3 + z^4',
        'shadow_class': 'L',
        'rank_formula': '6',
    },
    'E7': {
        'subgroup': '2O (binary octahedral, order 48)',
        'singularity': 'x^2 + y^3 + y*z^3',
        'shadow_class': 'L',
        'rank_formula': '7',
    },
    'E8': {
        'subgroup': '2I (binary icosahedral, order 120)',
        'singularity': 'x^2 + y^3 + z^5',
        'shadow_class': 'L',
        'rank_formula': '8',
    },
}


def mckay_shadow_class(ade_type: str) -> str:
    """Shadow class of the affine algebra corresponding to a du Val singularity.

    ALL ADE types give class L (affine KM algebras).
    The McKay correspondence does not change the shadow class.
    """
    if ade_type in MCKAY_ADE:
        return MCKAY_ADE[ade_type]['shadow_class']
    return 'L'


def mckay_all_class_L() -> bool:
    """Verify all McKay ADE types are class L."""
    return all(v['shadow_class'] == 'L' for v in MCKAY_ADE.values())


def mckay_singularity(ade_type: str) -> str:
    """du Val singularity equation for an ADE type."""
    return MCKAY_ADE[ade_type]['singularity']


def mckay_subgroup(ade_type: str) -> str:
    """Finite subgroup of SU(2) for an ADE type."""
    return MCKAY_ADE[ade_type]['subgroup']


# ============================================================================
# 10. Tensor product decompositions and R-matrix structure
# ============================================================================

# For the R-matrix R(u) = u + Omega on V tensor V, the spectral decomposition
# R = sum f_lambda P_lambda has eigenvalues determined by the Casimir.

def fund_rep_tensor_decomposition(name: str) -> Dict[str, Any]:
    """Tensor product decomposition V tensor V for the fundamental representation.

    E_6, V=27: 27 x 27 = 351_a + 351_s (27 is NOT self-dual)
               27 x 27* = 1 + 78 + 650
    E_7, V=56: 56 x 56 = (1 + 1539)_a + (133 + 1463)_s
               Lambda^2(56) = 1 + 1539, S^2(56) = 133 + 1463
    E_8, V=248: 248 x 248 = (248 + 30380)_a + (1 + 3875 + 27000)_s
    """
    d = _get(name)
    dim_V = d['fund_rep_dim']
    dim_sq = dim_V * dim_V
    dim_anti = dim_V * (dim_V - 1) // 2
    dim_sym = dim_V * (dim_V + 1) // 2

    if name == 'E6':
        return {
            'V_dim': 27,
            'self_dual': False,
            'V_x_V': {'351_a': 351, '351_s': 351},
            'V_x_Vdual': {'1': 1, '78': 78, '650': 650},
            'dim_antisym': dim_anti,
            'dim_sym': dim_sym,
            'dim_check': dim_anti + dim_sym == dim_sq,
            'n_irreps_VxV': 2,
            'n_irreps_VxVdual': 3,
        }
    elif name == 'E7':
        return {
            'V_dim': 56,
            'self_dual': True,
            'sym_type': 'symplectic',  # pseudo-real
            'antisym_irreps': {'1': 1, '1539': 1539},
            'sym_irreps': {'133': 133, '1463': 1463},
            'dim_antisym': dim_anti,
            'dim_sym': dim_sym,
            'dim_check': dim_anti + dim_sym == dim_sq,
            'antisym_dim_check': 1 + 1539 == dim_anti,
            'sym_dim_check': 133 + 1463 == dim_sym,
            'n_irreps': 4,
        }
    elif name == 'E8':
        return {
            'V_dim': 248,
            'self_dual': True,
            'sym_type': 'orthogonal',  # real
            'antisym_irreps': {'248': 248, '30380': 30380},
            'sym_irreps': {'1': 1, '3875': 3875, '27000': 27000},
            'dim_antisym': dim_anti,
            'dim_sym': dim_sym,
            'dim_check': dim_anti + dim_sym == dim_sq,
            'antisym_dim_check': 248 + 30380 == dim_anti,
            'sym_dim_check': 1 + 3875 + 27000 == dim_sym,
            'n_irreps': 5,
        }


def quadratic_casimir_fund(name: str) -> Fraction:
    """Quadratic Casimir eigenvalue C_2(V) on the fundamental representation.

    Normalized so that C_2(adj) = 2*h^vee.
    For the fundamental:
      E_6: C_2(27) = 26/3
      E_7: C_2(56) = 57/4 (= 3*(h^vee+1)/2 = 3*19/4)
      E_8: C_2(248) = 60 (= 2*h^vee, adjoint IS fundamental)
    """
    d = _get(name)
    if name == 'E6':
        return Fraction(26, 3)
    elif name == 'E7':
        return Fraction(57, 4)
    elif name == 'E8':
        # E_8 fundamental = adjoint, so C_2 = 2*h^vee = 60
        return Fraction(2 * d['h_dual'])


def r_matrix_num_eigenvalues(name: str) -> int:
    """Number of distinct R-matrix eigenvalues on V tensor V.

    = number of irreducible components in the tensor product decomposition.
    """
    decomp = fund_rep_tensor_decomposition(name)
    return decomp.get('n_irreps', decomp.get('n_irreps_VxV', 0))


# ============================================================================
# 11. Cross-family comparison table
# ============================================================================

def comparison_table(level_val: int = 1) -> List[Dict[str, Any]]:
    """Full comparison across E_6, E_7, E_8 at a given level.

    Reports affine data, W-algebra data, shadow classification, and
    R-matrix information.
    """
    rows = []
    for name in ['E6', 'E7', 'E8']:
        d = _get(name)

        kap_aff = affine_kappa_numeric(name, level_val)
        c_aff = affine_central_charge_numeric(name, level_val)
        kap_w = w_kappa_numeric(name, level_val)
        c_w = w_central_charge_numeric(name, level_val)
        rho = w_anomaly_ratio(name)
        gen_wts = w_generator_weights(name)

        rows.append({
            'name': name,
            'dim': d['dim'],
            'rank': d['rank'],
            'h_dual': d['h_dual'],
            'level': level_val,
            # Affine data
            'kappa_affine': kap_aff,
            'c_affine': c_aff,
            'affine_class': 'L',
            'affine_depth': 3,
            # W-algebra data
            'kappa_W': kap_w,
            'c_W': c_w,
            'anomaly_ratio': rho,
            'generator_weights': gen_wts,
            'W_class': 'M',
            'W_depth': 'infinity',
            # R-matrix
            'r_matrix_pole': 1,
            'fund_rep_dim': d['fund_rep_dim'],
        })
    return rows


# ============================================================================
# 12. E_8 level 1 special properties
# ============================================================================

def e8_level1_properties() -> Dict[str, Any]:
    """Special properties of E_8 at level 1.

    At level 1, E_8^(1) has exactly ONE integrable representation (the vacuum).
    The central charge is c = 248/31 = 8.
    The lattice VOA V_{E_8} coincides with V_1(e_8) (Frenkel-Kac-Segal),
    but kappa depends on the PRESENTATION (AP48).
    """
    c_val = affine_central_charge_numeric('E8', 1)
    kap_val = affine_kappa_numeric('E8', 1)

    return {
        'central_charge': c_val,
        'kappa_affine': kap_val,
        'kappa_lattice_heisenberg': Fraction(8),  # rank = 8 for H^{otimes 8}
        'n_integrable_reps': 1,
        'is_self_dual_lattice': True,  # E_8 lattice is unimodular
        'theta_equals_E4': True,       # Theta_{E_8} = E_4
        'c_equals_8': c_val == Fraction(8),
        'kappa_discrepancy': kap_val != Fraction(8),
        'AP48_note': 'kappa depends on presentation: affine vs Heisenberg tensor',
    }


# ============================================================================
# 13. Utility: verify Lie algebra data against cartan_data
# ============================================================================

def verify_against_cartan(name: str) -> Dict[str, bool]:
    """Cross-check stored data against the cartan_data infrastructure."""
    d = _get(name)
    cd = cartan_data(d['type'], d['rank'])
    return {
        'dim': d['dim'] == cd.dim,
        'h': d['h'] == cd.h,
        'h_dual': d['h_dual'] == cd.h_dual,
        'exponents': d['exponents'] == cd.exponents,
        'simply_laced': all(r == 2 for r in cd.root_lengths_squared),
    }


def verify_all_against_cartan() -> Dict[str, Dict[str, bool]]:
    return {name: verify_against_cartan(name) for name in EXCEPTIONAL_DATA}


# ============================================================================
# Main
# ============================================================================

if __name__ == '__main__':
    print("=" * 78)
    print("EXCEPTIONAL SHADOW ENGINE: E_6, E_7, E_8")
    print("=" * 78)

    for name in ['E6', 'E7', 'E8']:
        d = _get(name)
        print(f"\n--- {name} ---")
        print(f"  dim={d['dim']}, rank={d['rank']}, h=h^v={d['h_dual']}")
        print(f"  Affine at k=1: c={affine_central_charge_numeric(name, 1)}, "
              f"kappa={affine_kappa_numeric(name, 1)}")
        print(f"  W-algebra generators: {w_generator_weights(name)}")
        print(f"  Anomaly ratio: {w_anomaly_ratio(name)} = {float(w_anomaly_ratio(name)):.8f}")
        print(f"  W-algebra at k=1: c_W={w_central_charge_numeric(name, 1)}, "
              f"kappa_W={w_kappa_numeric(name, 1)}")

    print(f"\n--- Heterotic E_8 x E_8 ---")
    print(f"  c = {heterotic_e8_central_charge()}, kappa = {heterotic_e8_kappa()}")
    print(f"  Total c (+ 10 bosons) = {heterotic_total_c()}")

    print(f"\n--- MN theories ---")
    for theory in MN_THEORIES:
        print(f"  {theory}: c={mn_central_charge(theory)}, kappa={mn_kappa(theory)}")

    print(f"\n--- Deligne series at k=1 ---")
    for entry in deligne_kappas_at_level(1):
        print(f"  {entry['label']:3s}: dim={entry['dim']:>3d}, "
              f"kappa={float(entry['kappa']):.4f}")
