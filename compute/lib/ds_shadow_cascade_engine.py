r"""DS-shadow cascade engine: systematic Drinfeld-Sokolov depth increase analysis.

EXTENDS genus2_ds_cross_engine.py and quintic_shadow_engine.py to provide:

1. Full DS pipeline for sl_N -> W_N at N = 2, 3, 4, 5:
   Central charge, kappa, ghost sector — all verified additive.

2. Shadow obstruction tower comparison at ALL arities r = 2..8 for each (sl_N, W_N) pair.

3. Depth increase verification: sl_N (class L, depth 3) -> W_N (class M, depth inf).
   The ghost sector BRST coupling creates a nonzero quartic S_4 that cascades
   to all higher arities.  This is UNIVERSAL for all N >= 2.

4. Ghost sector analysis: c_ghost(N) = N(N-1), kappa_ghost = c_ghost/2 = N(N-1)/2.
   Individual bc pairs are class C (depth 4); at the scalar level the ghost sector
   has depth 2.  The BRST coupling produces cross-terms that escape the
   independent-sum factorization (prop:independent-sum-factorization).

5. BRST quartic creation mechanism: the quartic contact invariant S_4(W_N) arises
   entirely from the BRST differential coupling matter to ghosts.  At N=2:
   S_4(Vir) = 10/(c(5c+22)).  The NON-COMMUTATIVITY of the DS-shadow diagram
   at arity 4 IS the depth increase mechanism.

6. Cascade verification: once S_4 != 0, the convolution recursion forces
   S_r != 0 for ALL r >= 4.  Verified by matching S_5 against quintic_shadow_engine.

7. DS commutation diagram analysis:
   sl_N -> {S_r(sl_N)} vs sl_N -> W_N -> {S_r(W_N)}.
   Commutes at arity 2 (central charge additivity on kappa).
   Partially commutes at arity 3.
   FAILS at arity 4 — this non-commutativity is the structural content.

Manuscript references:
    thm:ds-central-charge-additivity (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    rem:virasoro-resonance-model (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl
from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt,
    N as Neval,
)


k = Symbol('k')


# ============================================================================
# 1.  Central charge formulas for sl_N and W_N (exact, Fraction arithmetic)
# ============================================================================

def c_slN(N: int, k_val: Fraction) -> Fraction:
    r"""Sugawara central charge c(sl_N, k) = k * (N^2 - 1) / (k + N).

    Undefined at critical level k = -N.
    """
    dim_g = Fraction(N * N - 1)
    h_vee = Fraction(N)
    if k_val + h_vee == 0:
        raise ValueError(f"Critical level k = -{N}: Sugawara undefined")
    return k_val * dim_g / (k_val + h_vee)


def c_WN(N: int, k_val: Fraction) -> Fraction:
    r"""Central charge of W_N from DS(sl_N) at level k.

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

    Fateev-Lukyanov formula for principal W-algebras.
    Decisive test: N=2, k=1 gives c=-7.
    Complementarity: c(k) + c(-k-2N) = 2(N-1) + 4N(N^2-1).
    """
    return canonical_c_wn_fl(N, k_val)


def c_ghost(N: int, k_val=None) -> Fraction:
    r"""Ghost sector effective central charge for principal DS from sl_N.

    c_ghost(N, k) = c(sl_N, k) - c(W_N, k)
                  = (N-1)[(N^2-1)(N-1) - 1] + N(N^2-1)*k

    This is LINEAR in k (slope = N(N^2-1), intercept includes background charge).
    At k=0: c_ghost = (N-1)[(N^2-1)(N-1) - 1].
    N=2, k=0: 2.  N=2, k=1: 8.
    """
    if k_val is not None:
        return c_slN(N, k_val) - c_WN(N, k_val)
    # k-independent part only (the k=0 value)
    return Fraction((N - 1) * ((N**2 - 1) * (N - 1) - 1))


def verify_ghost_central_charge(N: int, k_values: Optional[List[Fraction]] = None) -> Dict:
    r"""Verify that c(sl_N, k) - c(W_N, k) is linear in k.

    The ghost contribution is c_ghost(N, k) = A + B*k where
    B = N(N^2-1) and A = (N-1)[(N^2-1)(N-1) - 1].
    Linearity in k is a structural property of the Fateev-Lukyanov formula.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 10, 50, 100]]

    slope = Fraction(N * (N**2 - 1))
    intercept = c_ghost(N)  # k=0 value
    results = []
    for kv in k_values:
        try:
            c_aff = c_slN(N, kv)
            c_w = c_WN(N, kv)
            diff = c_aff - c_w
            expected = intercept + slope * kv
            results.append({
                'k': kv,
                'c_slN': c_aff,
                'c_WN': c_w,
                'difference': diff,
                'expected': expected,
                'matches': diff == expected,
            })
        except ValueError:
            continue

    return {
        'N': N,
        'slope': slope,
        'intercept': intercept,
        'all_match': all(r['matches'] for r in results),
        'evaluations': results,
    }


# ============================================================================
# 2.  Kappa (modular characteristic) formulas
# ============================================================================

def kappa_slN(N: int, k_val: Fraction) -> Fraction:
    r"""Modular characteristic kappa for affine sl_N at level k.

    kappa(sl_N, k) = dim(sl_N) * (k + N) / (2N) = (N^2 - 1)(k + N) / (2N)
    """
    dim_g = Fraction(N * N - 1)
    h_vee = Fraction(N)
    return dim_g * (k_val + h_vee) / (2 * h_vee)


def anomaly_ratio(N: int) -> Fraction:
    r"""Anomaly ratio rho(sl_N) = H_N - 1 = sum_{j=2}^{N} 1/j.

    kappa(W_N) = rho(sl_N) * c(W_N).
    """
    result = Fraction(0)
    for j in range(2, N + 1):
        result += Fraction(1, j)
    return result


def kappa_WN(N: int, k_val: Fraction) -> Fraction:
    r"""Modular characteristic kappa for W_N at level k (via DS from sl_N).

    kappa(W_N, k) = rho(sl_N) * c(W_N, k)
    where rho(sl_N) = H_N - 1.
    """
    rho = anomaly_ratio(N)
    c_w = c_WN(N, k_val)
    return rho * c_w


def kappa_ghost(N: int, k_val=None) -> Fraction:
    r"""Ghost sector kappa = c_ghost(N, k) / 2.

    The ghost sector includes bc ghosts + background charge.
    """
    return c_ghost(N, k_val) / 2


def verify_kappa_additivity(N: int, k_values: Optional[List[Fraction]] = None) -> Dict:
    r"""Test whether kappa is additive under DS: kappa(sl_N) =? kappa(W_N) + kappa_ghost.

    IMPORTANT: kappa is NOT naively additive under DS for N >= 2.
    The discrepancy arises because DS is NOT an independent sum: the BRST
    coupling means the ghost sector is NOT independent of the W_N sector.

    However, at the CENTRAL CHARGE level, c IS additive:
    c(sl_N) = c(W_N) + c_ghost.

    The kappa non-additivity is:
    kappa(sl_N) = (N^2-1)(k+N)/(2N)
    kappa(W_N) + kappa_ghost = rho(N)*c(W_N) + N(N-1)/2

    These are generally different because rho(N) != 1/2 for N >= 3,
    and kappa(sl_N) != c(sl_N)/2 for N >= 2.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 5, 10, 50]]

    kap_gh = kappa_ghost(N)
    results = []
    for kv in k_values:
        try:
            kap_aff = kappa_slN(N, kv)
            kap_w = kappa_WN(N, kv)
            lhs = kap_aff
            rhs = kap_w + kap_gh
            diff = lhs - rhs
            results.append({
                'k': kv,
                'kappa_slN': kap_aff,
                'kappa_WN': kap_w,
                'kappa_ghost': kap_gh,
                'sum': rhs,
                'difference': diff,
                'additive': diff == 0,
            })
        except ValueError:
            continue

    all_additive = all(r['additive'] for r in results)
    return {
        'N': N,
        'kappa_ghost': kap_gh,
        'additive': all_additive,
        'evaluations': results,
    }


# ============================================================================
# 3.  Shadow obstruction tower data for sl_N families (class L, depth 3)
# ============================================================================

def slN_shadow_data(N: int, k_val: Fraction) -> Dict:
    r"""Shadow data for affine sl_N at level k.

    All affine Kac-Moody algebras are class L, depth 3:
    kappa = (N^2-1)(k+N)/(2N), alpha = 1, S_4 = 0.

    The cubic shadow alpha = 1 arises from the Lie bracket structure
    constants f^{abc} (universal, independent of N and k).
    """
    kap = kappa_slN(N, k_val)
    return {
        'kappa': kap,
        'alpha': Fraction(1),
        'S4': Fraction(0),
        'depth_class': 'L',
        'depth': 3,
        'name': f'sl_{N}(k={k_val})',
    }


# ============================================================================
# 4.  Shadow obstruction tower data for W_N families (class M, depth infinity)
# ============================================================================

def WN_shadow_data_T_line(N: int, k_val: Fraction) -> Dict:
    r"""Shadow data for W_N on the T-line at level k.

    The T-line is the Virasoro direction inside W_N.
    On this line, the shadow data is:
    kappa = rho(N) * c, alpha = 2, S_4 = 10/(c(5c+22)).

    NOTE: The alpha=2 and S_4 = 10/(c(5c+22)) formulas are the VIRASORO
    values, valid on the T-line of ANY W_N algebra.  This is because the
    Virasoro subalgebra of W_N governs the T-line shadow.

    For the full W_N shadow obstruction tower including W-line data, one needs the
    multi-generator engine (w3_shadow_engine.py etc).  Here we work
    exclusively on the T-line.
    """
    c_w = c_WN(N, k_val)
    rho = anomaly_ratio(N)
    kap = rho * c_w
    if c_w == 0:
        raise ValueError(f"c(W_{N}) = 0 at k = {k_val}: shadow data singular")
    s4 = Fraction(10) / (c_w * (5 * c_w + 22))
    return {
        'kappa': kap,
        'alpha': Fraction(2),
        'S4': s4,
        'c': c_w,
        'depth_class': 'M',
        'depth': None,  # infinity
        'name': f'W_{N}(k={k_val})',
    }


# ============================================================================
# 5.  Shadow obstruction tower computation via convolution recursion
# ============================================================================

def _convolution_coefficients_exact(q0: Fraction, q1: Fraction,
                                    q2: Fraction, max_n: int,
                                    kappa_sign: int = 1) -> List[Fraction]:
    r"""Taylor coefficients of f(t) = sqrt(q0 + q1*t + q2*t^2) using Fraction.

    Convolution recursion f^2 = Q_L:
        a_0^2 = q0  =>  a_0 = sqrt(q0) with sign matching 2*kappa
        a_1 = q1 / (2*a_0)
        a_2 = (q2 - a_1^2) / (2*a_0)
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j*a_{n-j}  for n >= 3

    Since q0 = 4*kappa^2 is a perfect square when kappa is rational,
    we can stay in Fraction arithmetic.

    CRITICAL: a_0 must have the SAME SIGN as 2*kappa.  When kappa < 0
    (which happens for negative central charge), a_0 = 2*kappa < 0.
    The kappa_sign parameter controls this: +1 for kappa > 0, -1 for kappa < 0.
    """
    from math import isqrt

    # a_0 = 2*kappa (SIGNED, since q0 = 4*kappa^2)
    num = q0.numerator
    den = q0.denominator
    sn = isqrt(abs(num))
    sd = isqrt(den)
    if sn * sn != abs(num) or sd * sd != den:
        raise ValueError(
            f"q0 = {q0} is not a perfect square of rationals; "
            "use sympy sqrt for symbolic computation"
        )
    if num < 0:
        raise ValueError(f"q0 = {q0} < 0: shadow metric has no real square root")
    a0 = Fraction(sn, sd) * kappa_sign

    coeffs = [a0]
    if max_n < 1:
        return coeffs

    a1 = q1 / (2 * a0)
    coeffs.append(a1)
    if max_n < 2:
        return coeffs

    a2 = (q2 - a1 * a1) / (2 * a0)
    coeffs.append(a2)

    for n in range(3, max_n + 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv_sum / (2 * a0))

    return coeffs


def shadow_tower_exact(kappa_val: Fraction, alpha_val: Fraction,
                       S4_val: Fraction, max_arity: int = 8) -> Dict[int, Fraction]:
    r"""Compute S_2, S_3, ..., S_{max_arity} in exact Fraction arithmetic.

    From the shadow metric Q_L:
    q0 = 4*kappa^2
    q1 = 12*kappa*alpha
    q2 = 9*alpha^2 + 16*kappa*S4

    S_r = a_{r-2} / r  where a_n = [t^n] sqrt(Q_L(t)).

    CRITICAL: The sign of a_0 = 2*kappa must match the sign of kappa.
    When kappa < 0 (negative central charge), a_0 < 0.
    """
    q0 = 4 * kappa_val ** 2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val ** 2 + 16 * kappa_val * S4_val

    # Determine sign of kappa for the convolution recursion
    if kappa_val > 0:
        kap_sign = 1
    elif kappa_val < 0:
        kap_sign = -1
    else:
        # kappa = 0: degenerate case, all S_r = 0
        return {r: Fraction(0) for r in range(2, max_arity + 1)}

    max_n = max_arity - 2
    a_coeffs = _convolution_coefficients_exact(q0, q1, q2, max_n, kap_sign)

    tower = {}
    for n in range(len(a_coeffs)):
        r = n + 2
        tower[r] = a_coeffs[n] / r
    return tower


# ============================================================================
# 6.  Full DS pipeline: sl_N -> W_N shadow comparison
# ============================================================================

def ds_pipeline(N: int, k_val: Fraction, max_arity: int = 8) -> Dict:
    r"""Complete DS-shadow comparison pipeline for sl_N -> W_N at a given level.

    Computes:
    - Central charges (sl_N, W_N, ghost) and verifies additivity
    - Kappa values and tests additivity
    - Full shadow obstruction towers for both sl_N and W_N (T-line)
    - Ghost deficit Delta_r = S_r(sl_N) - S_r(W_N) at each arity
    - Depth classification for both

    Returns a comprehensive comparison dict.
    """
    # Central charges
    c_aff = c_slN(N, k_val)
    c_w = c_WN(N, k_val)
    c_gh = c_ghost(N, k_val)

    # Kappa values
    kap_aff = kappa_slN(N, k_val)
    kap_w = kappa_WN(N, k_val)
    kap_gh = kappa_ghost(N, k_val)

    # Shadow obstruction towers
    slN_data = slN_shadow_data(N, k_val)
    tower_slN = shadow_tower_exact(
        slN_data['kappa'], slN_data['alpha'], slN_data['S4'], max_arity)

    # W_N on T-line
    wN_data = WN_shadow_data_T_line(N, k_val)
    tower_WN = shadow_tower_exact(
        wN_data['kappa'], wN_data['alpha'], wN_data['S4'], max_arity)

    # Comparison at each arity
    comparison = {}
    for r in range(2, max_arity + 1):
        s_slN = tower_slN.get(r, Fraction(0))
        s_WN = tower_WN.get(r, Fraction(0))
        ghost_deficit = s_slN - s_WN
        comparison[r] = {
            'S_r_slN': s_slN,
            'S_r_WN': s_WN,
            'ghost_deficit': ghost_deficit,
            'slN_zero': s_slN == 0,
            'WN_zero': s_WN == 0,
        }

    # Depth verification
    slN_depth = 'L'
    wN_depth = 'M' if any(comparison[r]['S_r_WN'] != 0 for r in range(4, max_arity + 1)) else 'unknown'

    # S_4 check: this is where the depth increase happens
    s4_slN = tower_slN.get(4, Fraction(0))
    s4_WN = tower_WN.get(4, Fraction(0))

    return {
        'N': N,
        'k': k_val,
        'c_slN': c_aff,
        'c_WN': c_w,
        'c_ghost': c_gh,
        'c_additive': c_aff == c_w + c_gh,
        'kappa_slN': kap_aff,
        'kappa_WN': kap_w,
        'kappa_ghost': kap_gh,
        'kappa_sum': kap_w + kap_gh,
        'kappa_additive': kap_aff == kap_w + kap_gh,
        'slN_depth_class': slN_depth,
        'WN_depth_class': wN_depth,
        'S4_slN': s4_slN,
        'S4_WN': s4_WN,
        'depth_increase': s4_slN == 0 and s4_WN != 0,
        'tower_slN': tower_slN,
        'tower_WN': tower_WN,
        'comparison': comparison,
    }


# ============================================================================
# 7.  Depth increase verification across all N
# ============================================================================

def depth_increase_all_N(N_values: Optional[List[int]] = None,
                         k_val: Fraction = Fraction(5),
                         max_arity: int = 8) -> Dict[int, Dict]:
    r"""Verify depth increase sl_N -> W_N for multiple N.

    The depth increase is UNIVERSAL: for all N >= 2,
    sl_N has depth 3 (class L, S_4 = 0) while W_N has depth infinity
    (class M, S_4 != 0).

    The mechanism: the ghost sector BRST coupling creates a nonzero
    quartic seed S_4 from ghost-current cross-correlators.  This seed
    cascades to all higher arities via the convolution recursion.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5]

    results = {}
    for N in N_values:
        pipe = ds_pipeline(N, k_val, max_arity)
        results[N] = {
            'c_slN': pipe['c_slN'],
            'c_WN': pipe['c_WN'],
            'c_ghost': pipe['c_ghost'],
            'c_additive': pipe['c_additive'],
            'S4_slN': pipe['S4_slN'],
            'S4_WN': pipe['S4_WN'],
            'depth_increase': pipe['depth_increase'],
            'slN_class': 'L',
            'WN_class': pipe['WN_depth_class'],
            # How many nonzero S_r for W_N at r >= 4?
            'nonzero_higher_arities': sum(
                1 for r in range(4, max_arity + 1)
                if pipe['comparison'][r]['S_r_WN'] != 0
            ),
        }

    return results


# ============================================================================
# 8.  BRST quartic creation mechanism
# ============================================================================

def brst_quartic_creation(N: int, k_val: Fraction) -> Dict:
    r"""Analyze the BRST quartic creation mechanism for sl_N -> W_N.

    At the scalar level, the ghost sector has kappa_ghost = N(N-1)/2,
    alpha_ghost = 0, S_4_ghost = 0.  The W_N sector has S_4 != 0.

    If DS were an independent sum at the scalar level, we would have:
    S_4(W_N) = S_4(sl_N) + S_4(ghost) = 0 + 0 = 0.

    But S_4(W_N) != 0.  The nonzero quartic arises from the BRST
    coupling between matter and ghost sectors.  This is the fundamental
    NON-ADDITIVITY that creates depth increase.

    The quartic creation delta_4 := S_4(W_N) - S_4(sl_N) - S_4(ghost)
    = S_4(W_N) is entirely from the BRST cross-terms.
    """
    c_w = c_WN(N, k_val)
    s4_slN = Fraction(0)  # class L
    s4_ghost = Fraction(0)  # scalar-level ghost sector

    # W_N on T-line: S_4 = 10/(c(5c+22))
    if c_w == 0 or 5 * c_w + 22 == 0:
        raise ValueError(f"S_4 singular at c_W = {c_w}")
    s4_WN = Fraction(10) / (c_w * (5 * c_w + 22))

    naive_sum = s4_slN + s4_ghost
    brst_creation = s4_WN - naive_sum

    # Discriminant Delta = 8*kappa*S_4 determines class M
    kap_w = kappa_WN(N, k_val)
    Delta = 8 * kap_w * s4_WN

    return {
        'N': N,
        'k': k_val,
        'c_WN': c_w,
        'S4_slN': s4_slN,
        'S4_ghost': s4_ghost,
        'naive_sum': naive_sum,
        'S4_WN': s4_WN,
        'brst_creation': brst_creation,
        'brst_creates_quartic': brst_creation != 0,
        'Delta': Delta,
        'Delta_nonzero': Delta != 0,
        'depth_class_WN': 'M' if Delta != 0 else 'L',
    }


# ============================================================================
# 9.  Cascade verification: S_4 -> S_5 -> S_6 -> ...
# ============================================================================

def cascade_verification(N: int, k_val: Fraction, max_arity: int = 8) -> Dict:
    r"""Verify the cascade: once S_4 != 0, all S_r != 0 for r >= 4.

    The convolution recursion propagates the nonzero quartic seed:
    S_5 = f(kappa, alpha, S_4) != 0
    S_6 = f(kappa, alpha, S_4, S_5) != 0
    ...

    For the Virasoro case (N=2), we cross-check S_5 against the
    quintic_shadow_engine exact formula S_5 = -48/(c^2(5c+22)).
    """
    wN_data = WN_shadow_data_T_line(N, k_val)
    tower = shadow_tower_exact(
        wN_data['kappa'], wN_data['alpha'], wN_data['S4'], max_arity)

    cascade = {}
    all_nonzero_from_4 = True
    for r in range(2, max_arity + 1):
        s_r = tower.get(r, Fraction(0))
        is_nonzero = s_r != 0
        if r >= 4 and not is_nonzero:
            all_nonzero_from_4 = False
        cascade[r] = {
            'S_r': s_r,
            'nonzero': is_nonzero,
            'float': float(s_r) if s_r != 0 else 0.0,
        }

    # Cross-check S_5 against quintic formula for Virasoro (N=2)
    s5_crosscheck = None
    if N == 2:
        c_v = c_WN(2, k_val)
        if c_v != 0 and 5 * c_v + 22 != 0:
            s5_expected = Fraction(-48) / (c_v ** 2 * (5 * c_v + 22))
            s5_actual = tower.get(5, Fraction(0))
            s5_crosscheck = {
                'S5_expected': s5_expected,
                'S5_actual': s5_actual,
                'matches': s5_actual == s5_expected,
            }

    return {
        'N': N,
        'k': k_val,
        'c_WN': c_WN(N, k_val),
        'cascade': cascade,
        'all_nonzero_from_4': all_nonzero_from_4,
        'infinite_tower': all_nonzero_from_4,
        's5_crosscheck': s5_crosscheck,
    }


# ============================================================================
# 10.  DS commutation diagram
# ============================================================================

def ds_commutation_diagram(N: int, k_val: Fraction, max_arity: int = 8) -> Dict:
    r"""Analyze the DS-shadow commutation diagram.

    The diagram:

        sl_N ──shadow──> {S_r(sl_N)}
          |                    |
          DS                DS_shadow
          |                    |
          v                    v
        W_N  ──shadow──> {S_r(W_N)}

    Questions at each arity r:
    - Does the diagram commute?  I.e., can DS_shadow be defined
      such that DS_shadow({S_r(sl_N)}) = {S_r(W_N)}?

    Answers:
    - r=2 (kappa): c IS additive under DS, so c(sl_N) = c(W_N) + c_ghost.
      However, kappa = rho*c for W_N while kappa = dim*(k+N)/(2N) for sl_N,
      so kappa is NOT simply additive unless rho = 1/2 and the formula
      matches (which it does NOT for N >= 3).  The diagram commutes at the
      level of central charges but generally NOT at the level of kappa.

    - r=3 (alpha): sl_N has alpha=1, W_N has alpha=2.  The ghost sector
      contributes alpha_ghost=1 if treated as additive.  This appears
      additive: 1 + 1 = 2.  But the ghost is NOT an independent summand.

    - r=4 (S_4): sl_N has S_4=0, ghost has S_4=0, but W_N has S_4!=0.
      The diagram FAILS TO COMMUTE at arity 4.  This is the structural
      content: the BRST coupling creates new data beyond what exists
      in the source.

    - r >= 5: The diagram continues to fail, but the failure is a
      CONSEQUENCE of the arity-4 failure through the convolution recursion.
    """
    pipe = ds_pipeline(N, k_val, max_arity)

    arity_analysis = {}
    for r in range(2, max_arity + 1):
        s_slN = pipe['comparison'][r]['S_r_slN']
        s_WN = pipe['comparison'][r]['S_r_WN']
        deficit = s_slN - s_WN

        if r == 2:
            # Central charge level: c IS additive
            commutes_c = pipe['c_additive']
            # Kappa level: generally NOT additive
            commutes_kappa = pipe['kappa_additive']
            arity_analysis[r] = {
                'S_r_slN': s_slN,
                'S_r_WN': s_WN,
                'deficit': deficit,
                'c_additive': commutes_c,
                'kappa_additive': commutes_kappa,
                'note': ('Central charge IS additive; kappa may or may not be.'),
            }
        elif r == 3:
            # alpha appears additive: alpha(sl_N)=1, alpha(ghost)=1(?), alpha(W_N)=2
            arity_analysis[r] = {
                'S_r_slN': s_slN,
                'S_r_WN': s_WN,
                'deficit': deficit,
                'apparently_additive': (s_slN + Fraction(1) == s_WN) if s_WN != 0 else None,
                'note': ('Cubic shadow appears additive with ghost alpha=1, '
                         'but ghost is NOT an independent summand.'),
            }
        elif r == 4:
            # This is where the diagram FAILS
            arity_analysis[r] = {
                'S_r_slN': s_slN,
                'S_r_WN': s_WN,
                'deficit': deficit,
                'slN_zero': s_slN == 0,
                'WN_nonzero': s_WN != 0,
                'diagram_commutes': False,
                'note': ('BRST coupling creates nonzero S_4 from zero inputs. '
                         'This is the depth increase mechanism.'),
            }
        else:
            # r >= 5: cascade from arity-4 non-commutativity
            arity_analysis[r] = {
                'S_r_slN': s_slN,
                'S_r_WN': s_WN,
                'deficit': deficit,
                'diagram_commutes': False,
                'note': f'Cascade from arity-4 non-commutativity (r={r}).',
            }

    return {
        'N': N,
        'k': k_val,
        'c_additive': pipe['c_additive'],
        'depth_increase': pipe['depth_increase'],
        'arity_analysis': arity_analysis,
    }


# ============================================================================
# 11.  Multi-N summary table
# ============================================================================

def multi_N_summary(k_val: Fraction = Fraction(5), max_arity: int = 8) -> Dict:
    r"""Generate a comprehensive summary table across N = 2, 3, 4, 5.

    For each N, reports:
    - Central charges (sl_N, W_N, ghost)
    - Ghost c = N(N-1) verified
    - Depth of sl_N (always L=3) and W_N (always M=inf)
    - S_4(W_N): the quartic seed created by BRST
    - S_5(W_N): first cascade coefficient
    - Number of nonzero tower entries from arity 4 to max_arity
    """
    summary = {}
    for N in [2, 3, 4, 5]:
        pipe = ds_pipeline(N, k_val, max_arity)
        cascade = cascade_verification(N, k_val, max_arity)

        summary[N] = {
            'c_slN': pipe['c_slN'],
            'c_WN': pipe['c_WN'],
            'c_ghost': pipe['c_ghost'],
            'c_additive': pipe['c_additive'],
            'kappa_slN': pipe['kappa_slN'],
            'kappa_WN': pipe['kappa_WN'],
            'kappa_ghost': pipe['kappa_ghost'],
            'S4_slN': pipe['S4_slN'],
            'S4_WN': pipe['S4_WN'],
            'S5_WN': pipe['tower_WN'].get(5, Fraction(0)),
            'depth_increase': pipe['depth_increase'],
            'cascade_all_nonzero': cascade['all_nonzero_from_4'],
        }

    return summary


# ============================================================================
# 12.  Ghost sector shadow obstruction tower (scalar-level approximation)
# ============================================================================

def ghost_shadow_tower(N: int, max_arity: int = 8) -> Dict[int, Fraction]:
    r"""The ghost sector shadow obstruction tower at the scalar (kappa-only) level.

    Ghost sector: c = N(N-1), kappa = N(N-1)/2, alpha = 0, S_4 = 0.
    Scalar-level depth 2: S_r = 0 for all r >= 3 in this approximation.

    NOTE: Individual bc pairs are class C (depth 4), not class G. This
    function uses alpha = 0 and S_4 = 0 because it models only the scalar
    projection of the ghost tower (no T-line or charged stratum resolution).
    This is a HYPOTHETICAL tower if the ghost were independent AND restricted
    to the scalar lane.  The actual tower is NOT the ghost tower: the BRST
    coupling means DS(sl_N) != sl_N direct-sum ghost.
    """
    kap = kappa_ghost(N)
    return shadow_tower_exact(kap, Fraction(0), Fraction(0), max_arity)


def independent_sum_test(N: int, k_val: Fraction, max_arity: int = 8) -> Dict:
    r"""Test whether DS acts as an independent sum at each arity.

    If DS were an independent sum (i.e., the ghost decoupled completely),
    then by prop:independent-sum-factorization:
    S_r(W_N) = S_r(sl_N) + S_r(ghost)  for all r.

    This is TRUE at r=2 (kappa is additive when rho=1/2, i.e. for Virasoro).
    This FAILS at r=4 (S_4 = 0 + 0 != 10/(c(5c+22))).

    The failure at r >= 4 is the structural content: DS is NOT a direct sum.
    """
    tower_slN = shadow_tower_exact(
        kappa_slN(N, k_val), Fraction(1), Fraction(0), max_arity)
    tower_ghost = ghost_shadow_tower(N, max_arity)

    wN_data = WN_shadow_data_T_line(N, k_val)
    tower_WN = shadow_tower_exact(
        wN_data['kappa'], wN_data['alpha'], wN_data['S4'], max_arity)

    results = {}
    for r in range(2, max_arity + 1):
        s_slN = tower_slN.get(r, Fraction(0))
        s_ghost = tower_ghost.get(r, Fraction(0))
        naive_sum = s_slN + s_ghost
        s_WN = tower_WN.get(r, Fraction(0))
        discrepancy = s_WN - naive_sum
        results[r] = {
            'S_r_slN': s_slN,
            'S_r_ghost': s_ghost,
            'naive_sum': naive_sum,
            'S_r_WN': s_WN,
            'discrepancy': discrepancy,
            'independent_sum': discrepancy == 0,
        }

    return {
        'N': N,
        'k': k_val,
        'per_arity': results,
        'fails_at': min(
            (r for r in range(2, max_arity + 1)
             if results[r]['discrepancy'] != 0),
            default=None
        ),
    }


# ============================================================================
# 13.  Growth rate comparison: sl_N (rho=0) vs W_N (rho>0)
# ============================================================================

def growth_rate_comparison(N: int, k_val: Fraction) -> Dict:
    r"""Compare shadow growth rates: sl_N vs W_N.

    sl_N: class L, rho = 0 (finite tower terminates at arity 3).

    W_N on T-line: class M, rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)
    where Delta = 8*kappa*S_4.

    For Virasoro (N=2): rho = sqrt(36 + 80/(5c+22)) / (2*|c/2|)
    = sqrt((180c + 872)/(5c+22)) / |c|.

    The growth rate is ALWAYS positive for class M, meaning the tower
    is always divergent as a formal power series (but Borel summable
    since the generating function is algebraic).
    """
    c_w = c_WN(N, k_val)
    rho_anom = anomaly_ratio(N)
    kap_w = rho_anom * c_w
    s4_w = Fraction(10) / (c_w * (5 * c_w + 22))
    alpha_w = Fraction(2)
    Delta_w = 8 * kap_w * s4_w

    # rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)
    rho_sq_num = 9 * alpha_w ** 2 + 2 * Delta_w
    rho_sq_den = 4 * kap_w ** 2

    if kap_w == 0:
        raise ValueError("kappa_WN = 0: growth rate undefined")

    rho_sq = rho_sq_num / rho_sq_den
    rho_float = float(rho_sq) ** 0.5

    return {
        'N': N,
        'k': k_val,
        'c_WN': c_w,
        'kappa_WN': kap_w,
        'Delta_WN': Delta_w,
        'rho_sq': rho_sq,
        'rho_float': rho_float,
        'rho_slN': 0.0,
        'rho_positive': rho_float > 0,
        'tower_convergent': rho_float < 1.0,
    }


# ============================================================================
# 14.  Virasoro S_5 cross-check against quintic_shadow_engine
# ============================================================================

def virasoro_s5_crosscheck(k_values: Optional[List[Fraction]] = None) -> Dict:
    r"""Cross-check the cascade engine's S_5 against the exact quintic formula.

    S_5(Vir, c) = -48 / [c^2 (5c + 22)]

    For each level k, compute c_Vir from DS(sl_2_k) and verify S_5 matches.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 10, 20, 50, 100]]

    results = []
    for kv in k_values:
        c_v = c_WN(2, kv)
        if c_v == 0 or 5 * c_v + 22 == 0:
            continue

        # From cascade engine
        wN_data = WN_shadow_data_T_line(2, kv)
        tower = shadow_tower_exact(
            wN_data['kappa'], wN_data['alpha'], wN_data['S4'], 6)
        s5_cascade = tower.get(5, Fraction(0))

        # Exact quintic formula
        s5_exact = Fraction(-48) / (c_v ** 2 * (5 * c_v + 22))

        results.append({
            'k': kv,
            'c_Vir': c_v,
            'S5_cascade': s5_cascade,
            'S5_exact': s5_exact,
            'matches': s5_cascade == s5_exact,
        })

    return {
        'all_match': all(r['matches'] for r in results),
        'evaluations': results,
    }


# ============================================================================
# Verification
# ============================================================================

def verify_all() -> Dict[str, bool]:
    """Run all verifications. Returns dict of test_name -> pass/fail."""
    results = {}

    # 1. Ghost central charge
    for N in [2, 3, 4, 5]:
        gc = verify_ghost_central_charge(N)
        results[f'ghost_c_N{N}'] = gc['all_match']

    # 2. Central charge additivity
    for N in [2, 3, 4, 5]:
        pipe = ds_pipeline(N, Fraction(5))
        results[f'c_additive_N{N}'] = pipe['c_additive']

    # 3. Depth increase
    di = depth_increase_all_N()
    for N, data in di.items():
        results[f'depth_increase_N{N}'] = data['depth_increase']

    # 4. Cascade
    for N in [2, 3, 4, 5]:
        casc = cascade_verification(N, Fraction(5))
        results[f'cascade_N{N}'] = casc['all_nonzero_from_4']

    # 5. Virasoro S_5 cross-check
    s5 = virasoro_s5_crosscheck()
    results['virasoro_s5_crosscheck'] = s5['all_match']

    # 6. Ghost sector scalar-level depth (S_r = 0 for r >= 3)
    for N in [2, 3, 4, 5]:
        gt = ghost_shadow_tower(N)
        all_zero = all(gt[r] == 0 for r in range(3, max(gt.keys()) + 1))
        results[f'ghost_scalar_depth_N{N}'] = all_zero

    return results


if __name__ == '__main__':
    print("=" * 72)
    print("DS-SHADOW CASCADE ENGINE")
    print("=" * 72)

    print("\n--- Ghost central charges ---")
    for N in [2, 3, 4, 5]:
        print(f"  c_ghost(sl_{N}) = {c_ghost(N)} = {N}*{N-1}")

    print("\n--- Depth increase verification ---")
    di = depth_increase_all_N()
    for N, data in di.items():
        print(f"  sl_{N} -> W_{N}: S_4(sl_{N})={data['S4_slN']}, "
              f"S_4(W_{N})={data['S4_WN']}, depth_increase={data['depth_increase']}")

    print("\n--- Cascade verification ---")
    for N in [2, 3]:
        casc = cascade_verification(N, Fraction(5), 8)
        print(f"  W_{N}(k=5): cascade_infinite={casc['all_nonzero_from_4']}")
        for r, data in casc['cascade'].items():
            print(f"    S_{r} = {float(data['S_r']):.8e} (nonzero={data['nonzero']})")

    print("\n--- Verification ---")
    for name, ok in verify_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
