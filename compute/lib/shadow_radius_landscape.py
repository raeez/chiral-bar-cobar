r"""Shadow radius landscape: rho(A) for ALL standard families.

The shadow growth rate rho(A) = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)
controls the convergence/divergence of the shadow tower arity expansion.
For a class M algebra, the shadow coefficients satisfy

    S_r ~ C(A) * rho^r * r^{-5/2} * cos(r*theta + phi)

as r -> infinity (Flajolet-Sedgewick transfer theorem applied to the
algebraic generating function H(t) = t^2 * sqrt(Q_L(t))).

CLASSIFICATION:

  Class G (Gaussian, r_max=2): rho = 0.  Heisenberg, lattice VOAs, free fermion.
    Tower terminates at arity 2 because alpha = 0 and S_4 = 0.

  Class L (Lie/tree, r_max=3): rho = 3|alpha|/(2|kappa|).
    Affine KM: alpha != 0 but S_4 = 0, so Delta = 0 and Q_L is a perfect square.
    Tower terminates at arity 3 by the Jacobi identity.
    The "radius" is nonzero but finite depth.  The tower is polynomial, NOT
    exponentially growing; the formula gives a FINITE radius of convergence
    of the GF but the GF is NOT a series (it's a polynomial).

  Class C (Contact, r_max=4): single-line rho undefined.
    Beta-gamma: on the weight-changing primary line, alpha = 0 and
    the quartic contact lives on a charged stratum.  The single-line
    shadow radius is not applicable (stratum separation).
    We compute the single-line formula formally but flag it as N/A.

  Class M (Mixed, r_max=infinity): rho > 0.
    Virasoro, W_N: infinite tower with genuine exponential growth.
    rho(Vir_c) = sqrt((180c + 872) / ((5c+22)*c^2)).
    For W_N: each primary line (T, W_3, ..., W_N) has its own rho.
    T-line shadow radius = Virasoro radius (identical formula).

CRITICAL CENTRAL CHARGE:
    rho(Vir_{c*}) = 1  where  5c*^3 + 22c*^2 - 180c* - 872 = 0
    c* ~ 6.1243 (unique positive real root).

KOSZUL DUALITY:
    Vir_c <-> Vir_{26-c}:  rho(c) != rho(26-c) in general.
    Self-dual at c = 13: rho(13) = rho(13).

    W_3(c) <-> W_3(100-c): self-dual at c = 50.
    W_4(c) <-> W_4(246-c): self-dual at c = 123.

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-growth-rate (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, Optional, Tuple

from sympy import (
    Abs, N as Neval, Rational, S, Symbol,
    cancel, factor, oo, simplify, solve, sqrt,
)


c = Symbol('c')
k = Symbol('k')
lam = Symbol('lambda')


# ============================================================================
# 1. Universal shadow radius formula
# ============================================================================

def shadow_radius_universal(kappa_val, alpha_val, S4_val):
    r"""Shadow growth rate rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|).

    Here Delta = 8 * kappa * S4 is the critical discriminant.

    Returns symbolic rho (may involve sqrt).
    """
    Delta = 8 * kappa_val * S4_val
    numer_sq = 9 * alpha_val**2 + 2 * Delta
    numer_sq_simplified = simplify(numer_sq)
    if numer_sq_simplified == 0:
        return S.Zero
    return sqrt(numer_sq_simplified) / (2 * Abs(kappa_val))


def shadow_radius_numerical(kappa_val, alpha_val, S4_val):
    r"""Numerical shadow growth rate as a float."""
    rho = shadow_radius_universal(kappa_val, alpha_val, S4_val)
    return float(rho.evalf())


# ============================================================================
# 2. Virasoro shadow radius
# ============================================================================

def virasoro_data(c_val=None):
    r"""Shadow data (kappa, alpha, S4, Delta) for Virasoro.

    kappa = c/2,  alpha = S_3 = 2,  S_4 = 10/[c(5c+22)].
    Delta = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22).
    """
    cv = c if c_val is None else Rational(c_val)
    kappa = cv / 2
    alpha = Rational(2)
    S4 = Rational(10) / (cv * (5 * cv + 22))
    Delta = simplify(8 * kappa * S4)
    return kappa, alpha, S4, Delta


def virasoro_rho_squared(c_val=None):
    r"""rho^2(Vir_c) = (180c + 872) / ((5c+22)*c^2).

    Derivation:
      9*alpha^2 + 2*Delta = 36 + 80/(5c+22) = (180c + 872)/(5c+22)
      4*kappa^2 = c^2
      rho^2 = (180c + 872) / ((5c+22)*c^2)
    """
    cv = c if c_val is None else Rational(c_val)
    return (180 * cv + 872) / ((5 * cv + 22) * cv**2)


def virasoro_rho(c_val=None):
    r"""rho(Vir_c) = sqrt((180c + 872) / ((5c+22)*c^2))."""
    return sqrt(virasoro_rho_squared(c_val))


def virasoro_rho_numerical(c_val):
    r"""Numerical rho for Virasoro at specific central charge.

    Returns float('inf') at c = 0 (kappa = 0, undefined).
    Returns float('inf') at c = -22/5 (pole of S_4).
    """
    cv = Rational(c_val)
    if cv == 0 or 5 * cv + 22 == 0:
        return float('inf')
    rho_sq = virasoro_rho_squared(cv)
    val = float(rho_sq.evalf())
    if val < 0:
        return float('inf')  # should not happen for real c > 0
    return float(sqrt(Rational(val)).evalf()) if val == int(val) else val**0.5


def virasoro_critical_cubic():
    r"""The critical cubic 5c^3 + 22c^2 - 180c - 872 = 0.

    Roots: one positive real root c* ~ 6.1243, two complex.
    At c = c*: rho = 1 exactly.

    Returns (polynomial_expr, roots, c_star_numerical).
    """
    poly = 5 * c**3 + 22 * c**2 - 180 * c - 872
    roots = solve(poly, c)
    c_star = None
    for r in roots:
        val = complex(r.evalf())
        if abs(val.imag) < 1e-10 and val.real > 0:
            c_star = val.real
            break
    return poly, roots, c_star


def virasoro_landscape():
    r"""Complete Virasoro shadow radius landscape at special central charges.

    Returns dict mapping c-value labels to shadow radius data.
    """
    _, _, c_star = virasoro_critical_cubic()

    results = {}
    special = [
        ('1/2', Rational(1, 2)),
        ('1', Rational(1)),
        ('4', Rational(4)),
        ('c*', None),  # critical
        ('13', Rational(13)),
        ('25', Rational(25)),
        ('26', Rational(26)),
    ]

    for label, c_val in special:
        if label == 'c*':
            rho_val = 1.0
            convergent = None  # marginal
            results[label] = {
                'c': c_star,
                'kappa': c_star / 2,
                'rho': rho_val,
                'convergent': 'marginal',
            }
        else:
            kappa, alpha, S4, Delta = virasoro_data(c_val)
            rho = virasoro_rho(c_val)
            rho_float = float(rho.evalf())
            results[label] = {
                'c': float(c_val),
                'kappa': float(kappa),
                'alpha': float(alpha),
                'S4': float(S4.evalf()),
                'Delta': float(Delta.evalf()),
                'rho': rho_float,
                'convergent': rho_float < 1.0,
            }

    return results


# ============================================================================
# 3. W_N shadow radius: T-line and W-line
# ============================================================================

# Koszul conductors: W_N(c) is dual to W_N(K_N - c)
KOSZUL_CONDUCTORS = {
    2: 26,    # Virasoro: c + c' = 26
    3: 100,   # W_3: c + c' = 100
    4: 246,   # W_4: c + c' = 246
    5: 488,   # W_5
    6: 850,   # W_6
}

# Self-dual central charges: c_sd = K_N / 2
SELF_DUAL_CC = {N: Rational(K, 2) for N, K in KOSZUL_CONDUCTORS.items()}


def wn_tline_rho(N, c_val=None):
    r"""T-line shadow radius for W_N = Virasoro shadow radius.

    On the T-line (all W_j modes set to zero, j >= 3), the shadow
    tower is governed purely by the Virasoro OPE of the stress tensor.
    Therefore rho_T(W_N) = rho(Vir_c) identically.
    """
    return virasoro_rho(c_val)


def w3_wline_data(c_val=None):
    r"""W-line shadow data for W_3.

    On the W-line (x_T = 0):
      kappa_W = c/3
      alpha_W = S_3 = 0  (Z_2 parity: W -> -W forces odd-arity vanishing)
      S4_W = 2560/[c(5c+22)^3]  (pure W-channel quartic from Lambda exchange)
      Delta_W = 8 * (c/3) * 2560/[c(5c+22)^3] = 20480/[3(5c+22)^3]
    """
    cv = c if c_val is None else Rational(c_val)
    kappa_W = cv / 3
    alpha_W = S.Zero
    S4_W = Rational(2560) / (cv * (5 * cv + 22)**3)
    Delta_W = simplify(8 * kappa_W * S4_W)
    return kappa_W, alpha_W, S4_W, Delta_W


def w3_wline_rho_squared(c_val=None):
    r"""rho_W^2 for W_3 on the W-line.

    Since alpha_W = 0:
      rho_W^2 = 2*Delta_W / (4*kappa_W^2)
              = 2 * 20480/[3(5c+22)^3] / (4c^2/9)
              = 2 * 20480 * 9 / (3 * (5c+22)^3 * 4 * c^2)
              = 30720 / (c^2 * (5c+22)^3)
    """
    cv = c if c_val is None else Rational(c_val)
    return Rational(30720) / (cv**2 * (5 * cv + 22)**3)


def w3_wline_rho(c_val=None):
    r"""rho_W(W_3) on the W-line."""
    return sqrt(w3_wline_rho_squared(c_val))


def w3_wline_rho_numerical(c_val):
    r"""Numerical W-line rho for W_3."""
    return float(w3_wline_rho(c_val).evalf())


def w3_landscape():
    r"""Complete W_3 shadow radius landscape.

    W_3 has two independent shadow radii:
      rho_T = Virasoro rho (T-line)
      rho_W = W-line rho (even arities only, Z_2 parity)

    The effective shadow radius governing the full 2D tower is
    max(rho_T, rho_W), since the dominant growth comes from whichever
    line contributes the larger exponential rate.

    Self-dual at c = 50 (Koszul conductor K_3 = 100).
    """
    results = {}
    special = [
        ('2', Rational(2)),
        ('50', Rational(50)),   # self-dual
        ('98', Rational(98)),
    ]

    for label, c_val in special:
        rho_T = virasoro_rho_numerical(c_val)
        rho_W = w3_wline_rho_numerical(c_val)
        kappa_total = Rational(5) * c_val / 6
        results[label] = {
            'c': float(c_val),
            'kappa_T': float(c_val) / 2,
            'kappa_W': float(c_val) / 3,
            'kappa_total': float(kappa_total),
            'rho_T': rho_T,
            'rho_W': rho_W,
            'rho_eff': max(rho_T, rho_W),
            'self_dual': label == '50',
        }

    # Generic c
    rho_T_sq = virasoro_rho_squared()
    rho_W_sq = w3_wline_rho_squared()
    results['generic'] = {
        'rho_T_squared': str(cancel(rho_T_sq)),
        'rho_W_squared': str(cancel(rho_W_sq)),
        'kappa_total': '5c/6',
    }

    return results


def w4_wline_data(c_val=None):
    r"""Shadow data for W_4 on the W_3-line and W_4-line.

    W_4 has generators T (weight 2), W_3 (weight 3), W_4 (weight 4).
    Three primary lines: T, W_3, W_4.

    T-line: same as Virasoro.
    W_3-line: Z_2 parity under W_3 -> -W_3 forces odd arities to vanish.
    W_4-line: Z_2 parity under W_4 -> -W_4 (if present) forces structure.

    For the W_3-line of W_4:
      kappa_{W_3} = c/3
      The quartic coefficient involves the geometric progression factor
      alpha = 16/(5c+22) iterated.  For W_4, additional channels open.

    For the W_4-line:
      kappa_{W_4} = c/4
      The quartic involves further factors of alpha = 16/(5c+22).

    NOTE: The W_4-specific quartic data is more complex than W_3.
    The geometric progression in the Lambda-exchange gives:
      Q_{W_j W_j W_j W_j} = 10/[c(5c+22)] * [16/(5c+22)]^{2(j-2)}

    This is the pattern from w3_quartic_tensor: Q_TTTT : Q_TTWW : Q_WWWW
    form a geometric sequence with ratio alpha = 16/(5c+22).
    Extending to W_4:
      Q_{W_4^4} = 10/[c(5c+22)] * [16/(5c+22)]^4 = 10*16^4/[c(5c+22)^5]
    """
    cv = c if c_val is None else Rational(c_val)

    # W_3-line data (same as W_3 algebra W-line)
    kappa_w3 = cv / 3
    alpha_w3 = S.Zero  # Z_2 parity
    S4_w3 = Rational(2560) / (cv * (5 * cv + 22)**3)

    # W_4-line data
    kappa_w4 = cv / 4
    alpha_w4 = S.Zero  # Z_2 parity
    # Quartic from geometric progression: 10 * 16^4 / [c * (5c+22)^5]
    S4_w4 = Rational(10) * Rational(16)**4 / (cv * (5 * cv + 22)**5)

    return {
        'T': virasoro_data(c_val),
        'W_3': (kappa_w3, alpha_w3, S4_w3, 8 * kappa_w3 * S4_w3),
        'W_4': (kappa_w4, alpha_w4, S4_w4, 8 * kappa_w4 * S4_w4),
    }


def w4_channel_rho_squared(c_val=None):
    r"""rho^2 for each channel of W_4.

    T-channel: rho_T^2 = (180c + 872) / ((5c+22)*c^2)  (Virasoro)
    W_3-channel: rho_{W_3}^2 = 30720 / (c^2 * (5c+22)^3)
    W_4-channel: rho_{W_4}^2 = 2*Delta_{W_4} / (4*kappa_{W_4}^2)

    For W_4 channel:
      Delta_{W_4} = 8*(c/4)*10*16^4/[c*(5c+22)^5] = 2*10*16^4/[(5c+22)^5]
                  = 2*655360/[(5c+22)^5] = 1310720/[(5c+22)^5]
      4*kappa_{W_4}^2 = 4*(c/4)^2 = c^2/4
      rho_{W_4}^2 = 2*1310720/[(5c+22)^5] / (c^2/4)
                  = 2*1310720*4 / (c^2*(5c+22)^5)
                  = 10485760 / (c^2*(5c+22)^5)
    """
    cv = c if c_val is None else Rational(c_val)

    rho_T_sq = virasoro_rho_squared(c_val)

    # W_3 channel
    rho_w3_sq = w3_wline_rho_squared(c_val)

    # W_4 channel
    # S4_{W_4} = 10 * 16^4 / [c * (5c+22)^5]  = 655360 / [c * (5c+22)^5]
    # Delta_{W_4} = 8 * (c/4) * S4_{W_4} = 2c * 655360 / [c * (5c+22)^5]
    #             = 1310720 / (5c+22)^5
    # rho^2 = 2*Delta / (4*kappa^2)  since alpha = 0
    #       = 2 * 1310720 / [(5c+22)^5 * c^2/4]
    #       = 10485760 / [c^2 * (5c+22)^5]
    rho_w4_sq = Rational(10485760) / (cv**2 * (5 * cv + 22)**5)

    return {
        'T': rho_T_sq,
        'W_3': rho_w3_sq,
        'W_4': rho_w4_sq,
    }


def w4_landscape(c_val):
    r"""W_4 shadow radius landscape at a specific central charge.

    Self-dual at c = 123 (Koszul conductor K_4 = 246).
    """
    c_v = Rational(c_val)
    rhos = w4_channel_rho_squared(c_v)
    result = {}
    for channel, rho_sq in rhos.items():
        rho_val = float(sqrt(rho_sq).evalf())
        result[channel] = {
            'rho_squared': float(rho_sq.evalf()),
            'rho': rho_val,
            'convergent': rho_val < 1.0,
        }
    result['rho_eff'] = max(r['rho'] for r in result.values())
    return result


# ============================================================================
# 4. W_N general formula
# ============================================================================

def wn_channel_rho_squared(N, j, c_val=None):
    r"""rho^2 for the W_j-channel of W_N (j = 2, ..., N).

    On the W_j line (all other modes zero):
      kappa_j = c/j
      alpha_j = 0  (Z_2 parity: W_j -> -W_j for j >= 3; for j=2: alpha=2)

    For j = 2 (T-line): alpha = 2, S4 = 10/[c(5c+22)]
    For j >= 3: alpha = 0, S4_j = 10*16^{2(j-2)} / [c*(5c+22)^{2j-3}]
      (geometric progression from Lambda exchange)

    rho_j^2 = (9*alpha_j^2 + 2*Delta_j) / (4*kappa_j^2)
    """
    cv = c if c_val is None else Rational(c_val)

    if j < 2 or j > N:
        raise ValueError(f"Channel index j={j} outside range [2, {N}]")

    kappa_j = cv / j

    if j == 2:
        # T-line: alpha = 2, S4 = 10/[c(5c+22)]
        return virasoro_rho_squared(c_val)
    else:
        # W_j line: alpha = 0
        # S4_j = 10 * 16^{2(j-2)} / [c * (5c+22)^{2j-3}]
        # Delta_j = 8 * (c/j) * S4_j = 80 * 16^{2(j-2)} / [j * (5c+22)^{2j-3}]
        # rho_j^2 = 2*Delta_j / (4*kappa_j^2)
        #         = 2 * 80 * 16^{2(j-2)} / [j * (5c+22)^{2j-3} * c^2/j^2]
        #         WAIT: 4*kappa_j^2 = 4*(c/j)^2 = 4c^2/j^2
        #         = 2 * 80 * 16^{2(j-2)} * j^2 / [j * (5c+22)^{2j-3} * 4 * c^2]
        #         = 40 * j * 16^{2(j-2)} / [c^2 * (5c+22)^{2j-3}]
        power = 2 * (j - 2)
        exponent = 2 * j - 3
        numer = 40 * j * Rational(16)**power
        denom = cv**2 * (5 * cv + 22)**exponent
        return numer / denom


def wn_all_channel_rho(N, c_val):
    r"""All channel shadow radii for W_N at specific central charge.

    Returns dict {j: rho_j} for j = 2, ..., N.
    """
    cv = Rational(c_val)
    result = {}
    for j in range(2, N + 1):
        rho_sq = wn_channel_rho_squared(N, j, cv)
        rho_val = float(sqrt(rho_sq).evalf())
        result[j] = rho_val
    return result


def wn_effective_rho(N, c_val):
    r"""Effective shadow radius = max over all channels."""
    channels = wn_all_channel_rho(N, c_val)
    return max(channels.values())


# ============================================================================
# 5. Beta-gamma shadow radius
# ============================================================================

def betagamma_central_charge(lam_val=None):
    r"""c(betagamma) = 2(6*lambda^2 - 6*lambda + 1).

    lambda=0 or 1: c = 2.   lambda=1/2: c = -1.
    """
    lv = lam if lam_val is None else Rational(lam_val)
    return 2 * (6 * lv**2 - 6 * lv + 1)


def betagamma_kappa(lam_val=None):
    r"""kappa(betagamma) = c/2 = 6*lambda^2 - 6*lambda + 1."""
    lv = lam if lam_val is None else Rational(lam_val)
    return 6 * lv**2 - 6 * lv + 1


def betagamma_shadow_data(lam_val=None):
    r"""Shadow data for betagamma on the weight-changing primary line.

    On the weight-changing line:
      kappa = 6*lambda^2 - 6*lambda + 1
      alpha (S_3) = 0  (abelian on 1D weight-shift subspace)
      S_4: the quartic contact lives on the CHARGED stratum, not the
           weight-changing primary line.  On the primary line, S_4 = 0.

    Depth classification: the single-line framework gives class G
    (since alpha = 0 and S_4 = 0 on the primary line).  The actual
    class C comes from the 2D deformation space where the quartic
    contact on the charged stratum has depth 4.

    Therefore the single-line shadow radius on the weight-changing
    line is rho = 0 (the tower terminates on this line).  The
    nontrivial quartic content lives on the charged stratum and
    escapes via stratum separation.

    This function returns the PRIMARY LINE data, where rho = 0.
    """
    kappa = betagamma_kappa(lam_val)
    alpha = S.Zero
    S4 = S.Zero  # on primary line
    Delta = S.Zero
    return kappa, alpha, S4, Delta


def betagamma_landscape():
    r"""Betagamma shadow data at special conformal weights.

    lambda=0: standard betagamma, c=2, kappa=1
    lambda=1/2: symplectic, c=-1, kappa=-1/2
    lambda=1: also standard (same as lambda=0 by symmetry), c=2, kappa=1
    lambda=3/2: c=10, kappa=5
    """
    results = {}
    for label, lam_val in [('0', 0), ('1/2', Rational(1, 2)),
                           ('1', 1), ('3/2', Rational(3, 2))]:
        kappa = betagamma_kappa(lam_val)
        cc = betagamma_central_charge(lam_val)
        results[label] = {
            'lambda': float(Rational(lam_val)),
            'c': float(cc),
            'kappa': float(kappa),
            'alpha': 0,
            'S4_primary_line': 0,
            'Delta_primary_line': 0,
            'rho_primary_line': 0,
            'class': 'C',
            'depth': 4,
            'note': 'Single-line rho = 0 (stratum separation); '
                    'quartic contact on charged stratum',
        }
    return results


# ============================================================================
# 6. Lattice VOAs
# ============================================================================

def lattice_shadow_data(rank):
    r"""Shadow data for lattice VOA V_Lambda of given rank.

    Class G: kappa = rank, alpha = 0, S_4 = 0, Delta = 0, rho = 0.
    Tower terminates at arity 2 (abelian OPE).
    """
    return {
        'rank': rank,
        'kappa': rank,
        'alpha': 0,
        'S4': 0,
        'Delta': 0,
        'rho': 0,
        'class': 'G',
        'depth': 2,
    }


LATTICE_EXAMPLES = {
    'Z': {'rank': 1, 'lattice': 'Z'},
    'Z^2': {'rank': 2, 'lattice': 'Z^2'},
    'A_2': {'rank': 2, 'lattice': 'A_2 root'},
    'D_4': {'rank': 4, 'lattice': 'D_4 root'},
    'E_8': {'rank': 8, 'lattice': 'E_8 root'},
    'Leech': {'rank': 24, 'lattice': 'Leech'},
}


def lattice_landscape():
    r"""Shadow radius data for all standard lattice VOAs."""
    return {name: lattice_shadow_data(info['rank'])
            for name, info in LATTICE_EXAMPLES.items()}


# ============================================================================
# 7. Affine Kac-Moody
# ============================================================================

def affine_shadow_data(lie_type, rank, level_val=None):
    r"""Shadow data for affine KM algebra V_k(g).

    Class L: S_4 = 0 (Jacobi identity), Delta = 0, rho = 0.
    Tower terminates at arity 3.

    kappa(g, k) = dim(g) * (k + h^v) / (2*h^v)

    Standard dimensions and dual Coxeter numbers:
      sl_N: dim = N^2-1, h^v = N
      so_{2n+1}: dim = n(2n+1), h^v = 2n-1
      sp_{2n}: dim = n(2n+1), h^v = n+1
      so_{2n}: dim = n(2n-1), h^v = 2n-2
      E_6: dim = 78, h^v = 12
      E_7: dim = 133, h^v = 18
      E_8: dim = 248, h^v = 30
      F_4: dim = 52, h^v = 9
      G_2: dim = 14, h^v = 4
    """
    LIE_DATA = {
        'A': lambda n: (n * (n + 2), n + 1),     # sl_{n+1}
        'B': lambda n: (n * (2 * n + 1), 2 * n - 1),  # so_{2n+1}
        'C': lambda n: (n * (2 * n + 1), n + 1),      # sp_{2n}
        'D': lambda n: (n * (2 * n - 1), 2 * n - 2),  # so_{2n}
    }

    EXCEPTIONAL = {
        'E6': (78, 12),
        'E7': (133, 18),
        'E8': (248, 30),
        'F4': (52, 9),
        'G2': (14, 4),
    }

    key = f'{lie_type}{rank}'
    if key in EXCEPTIONAL:
        dim_g, h_v = EXCEPTIONAL[key]
    elif lie_type in LIE_DATA:
        dim_g, h_v = LIE_DATA[lie_type](rank)
    else:
        raise ValueError(f"Unknown Lie type {lie_type}{rank}")

    kv = k if level_val is None else Rational(level_val)
    kappa = Rational(dim_g) * (kv + h_v) / (2 * h_v)

    return {
        'lie_type': f'{lie_type}{rank}',
        'dim_g': dim_g,
        'h_v': h_v,
        'kappa': kappa,
        'alpha': 'nonzero (Killing 3-cocycle)',
        'S4': 0,
        'Delta': 0,
        'rho': 0,
        'class': 'L',
        'depth': 3,
    }


def affine_landscape():
    r"""Shadow radius data for standard affine KM families."""
    families = [
        ('A', 1), ('A', 2), ('A', 3), ('A', 4),
        ('B', 2), ('C', 2), ('D', 4),
    ]
    # Add exceptionals as special entries
    exceptionals = ['E6', 'E7', 'E8', 'F4', 'G2']

    results = {}
    for lt, rk in families:
        key = f'{lt}{rk}'
        results[key] = affine_shadow_data(lt, rk)

    for exc in exceptionals:
        lt = exc[0]
        rk = int(exc[1:])
        results[exc] = affine_shadow_data(lt, rk)

    return results


# ============================================================================
# 8. Koszul duality relationships
# ============================================================================

def virasoro_koszul_pair(c_val):
    r"""Koszul pair data for Virasoro: Vir_c <-> Vir_{26-c}.

    rho(c) and rho(26-c): the shadow radii of the algebra and its dual.
    Self-dual at c = 13.
    """
    cv = Rational(c_val)
    c_dual = 26 - cv
    rho = virasoro_rho_numerical(cv)
    rho_dual = virasoro_rho_numerical(c_dual)
    return {
        'c': float(cv),
        'c_dual': float(c_dual),
        'kappa': float(cv) / 2,
        'kappa_dual': float(c_dual) / 2,
        'rho': rho,
        'rho_dual': rho_dual,
        'rho_sum': rho + rho_dual,
        'rho_product': rho * rho_dual,
        'self_dual': abs(rho - rho_dual) < 1e-10,
    }


def w3_koszul_pair(c_val):
    r"""Koszul pair data for W_3: W_3(c) <-> W_3(100-c).

    Self-dual at c = 50.
    """
    cv = Rational(c_val)
    c_dual = 100 - cv

    rho_T = virasoro_rho_numerical(cv)
    rho_T_dual = virasoro_rho_numerical(c_dual)

    rho_W = w3_wline_rho_numerical(cv)
    rho_W_dual = w3_wline_rho_numerical(c_dual)

    return {
        'c': float(cv),
        'c_dual': float(c_dual),
        'rho_T': rho_T,
        'rho_T_dual': rho_T_dual,
        'rho_W': rho_W,
        'rho_W_dual': rho_W_dual,
        'rho_eff': max(rho_T, rho_W),
        'rho_eff_dual': max(rho_T_dual, rho_W_dual),
        'T_self_dual': abs(rho_T - rho_T_dual) < 1e-10,
        'W_self_dual': abs(rho_W - rho_W_dual) < 1e-10,
    }


# ============================================================================
# 9. Complete landscape table
# ============================================================================

def complete_landscape():
    r"""Complete shadow radius landscape for all standard families.

    Returns a structured dictionary with all families, their shadow data,
    and the shadow radius rho.

    Classes:
      G: rho = 0 (tower terminates at arity 2)
      L: rho = 0 (tower terminates at arity 3; GF is polynomial)
      C: rho = 0 on primary line (stratum separation; tower terminates at arity 4)
      M: rho > 0 (infinite tower)
    """
    landscape = {
        'CLASS_G': {
            'description': 'Gaussian (depth 2): rho = 0, tower terminates',
            'families': {
                'Heisenberg': {'kappa': 'k (level)', 'rho': 0},
                'Free_fermion': {'kappa': '1/4', 'rho': 0},
                **{f'Lattice_{name}': {'kappa': info['rank'], 'rho': 0}
                   for name, info in LATTICE_EXAMPLES.items()},
            },
        },
        'CLASS_L': {
            'description': 'Lie/tree (depth 3): rho = 0, tower terminates',
            'families': affine_landscape(),
        },
        'CLASS_C': {
            'description': 'Contact (depth 4): single-line rho = 0 (stratum separation)',
            'families': betagamma_landscape(),
        },
        'CLASS_M': {
            'description': 'Mixed (depth infinity): rho > 0, infinite tower',
            'families': {
                'Virasoro': virasoro_landscape(),
                'W_3': w3_landscape(),
            },
        },
    }
    return landscape


# ============================================================================
# 10. Complementarity analysis: rho(c) + rho(K-c)
# ============================================================================

def virasoro_complementarity_analysis():
    r"""Analysis of rho(c) + rho(26-c) for Virasoro.

    The shadow radii of a Koszul pair (Vir_c, Vir_{26-c}) are NOT
    simply related (not reciprocal, not additive, not multiplicative
    constant).

    Key values:
      c=1:  rho(1) ~ 6.242, rho(25) ~ 0.242
      c=13: rho(13) = rho(13) ~ 0.467 (self-dual)
      c=25: rho(25) ~ 0.242, rho(1) ~ 6.242

    The product rho(c)*rho(26-c) varies with c.
    """
    c_values = [1, 2, 4, 6, 10, 13, 20, 25, 26]
    results = []
    for cv in c_values:
        pair = virasoro_koszul_pair(cv)
        results.append(pair)
    return results


# ============================================================================
# 11. Critical cubic for W_3 and W_4
# ============================================================================

def wn_tline_critical_c(N=None):
    r"""Critical central charge on the T-line where rho_T = 1.

    Since rho_T = rho_Vir = Virasoro shadow radius, the critical central
    charge is the SAME for ALL W_N on the T-line: c* ~ 6.1243.

    This is the root of 5c^3 + 22c^2 - 180c - 872 = 0.
    """
    _, _, c_star = virasoro_critical_cubic()
    return c_star


def w3_wline_critical_c():
    r"""Critical central charge on the W-line of W_3 where rho_W = 1.

    Solve: rho_W^2 = 30720 / (c^2 * (5c+22)^3) = 1
    => c^2 * (5c+22)^3 = 30720

    This is a degree-5 polynomial in c.
    """
    poly = c**2 * (5 * c + 22)**3 - 30720
    roots = solve(poly, c)
    real_positive = []
    for r in roots:
        try:
            val = complex(r.evalf())
            if abs(val.imag) < 1e-10 and val.real > 0:
                real_positive.append(val.real)
        except (TypeError, ValueError):
            continue
    return sorted(real_positive)[0] if real_positive else None


# ============================================================================
# 12. Summary printer
# ============================================================================

def print_landscape_summary():
    r"""Print a complete summary of the shadow radius landscape."""
    print("=" * 75)
    print("SHADOW RADIUS LANDSCAPE: rho(A) FOR ALL STANDARD FAMILIES")
    print("=" * 75)

    # Critical central charge
    _, _, c_star = virasoro_critical_cubic()
    print(f"\nVirasoro critical c*: {c_star:.6f}")
    print(f"  5c^3 + 22c^2 - 180c - 872 = 0")

    # Class G
    print("\n--- CLASS G (Gaussian, depth 2): rho = 0 ---")
    print("  Heisenberg H_k:   kappa = k,       rho = 0")
    print("  Free fermion:     kappa = 1/4,     rho = 0")
    for name, info in LATTICE_EXAMPLES.items():
        print(f"  Lattice V_{name}:  kappa = {info['rank']},       rho = 0")

    # Class L
    print("\n--- CLASS L (Lie/tree, depth 3): rho = 0 ---")
    al = affine_landscape()
    for name, data in sorted(al.items()):
        print(f"  V_k({name}):  dim = {data['dim_g']}, h^v = {data['h_v']}, "
              f"kappa = {data['kappa']},  rho = 0")

    # Class C
    print("\n--- CLASS C (Contact, depth 4): single-line rho = 0 ---")
    bl = betagamma_landscape()
    for label, data in bl.items():
        print(f"  betagamma(lam={label}): c = {data['c']}, kappa = {data['kappa']}, "
              f"rho = 0 (stratum separation)")

    # Class M: Virasoro
    print("\n--- CLASS M (Mixed, depth infinity): rho > 0 ---")
    print("\n  Virasoro Vir_c:")
    print(f"    rho^2 = (180c + 872) / ((5c+22)*c^2)")
    print(f"    Critical c* = {c_star:.6f}")
    vl = virasoro_landscape()
    print(f"    {'c':>8s}  {'kappa':>8s}  {'rho':>10s}  {'conv?':>6s}")
    print(f"    {'---':>8s}  {'---':>8s}  {'---':>10s}  {'---':>6s}")
    for label, data in vl.items():
        rho = data['rho']
        conv = data['convergent']
        if isinstance(conv, str):
            conv_str = conv
        else:
            conv_str = 'YES' if conv else 'NO'
        print(f"    {label:>8s}  {data.get('kappa', ''):>8.3f}  {rho:10.6f}  {conv_str:>6s}")

    # Class M: W_3
    print("\n  W_3:")
    w3l = w3_landscape()
    for label, data in w3l.items():
        if label == 'generic':
            continue
        print(f"    c={label}: rho_T={data['rho_T']:.6f}, "
              f"rho_W={data['rho_W']:.6f}, "
              f"rho_eff={data['rho_eff']:.6f}")

    # Koszul duality
    print("\n--- KOSZUL DUALITY ---")
    print("\n  Virasoro: rho(c) vs rho(26-c)")
    for cv in [1, 4, 13, 25, 26]:
        pair = virasoro_koszul_pair(cv)
        sd = " (self-dual)" if pair['self_dual'] else ""
        print(f"    c={cv:2d}: rho={pair['rho']:.6f}, "
              f"rho!={pair['rho_dual']:.6f}, "
              f"prod={pair['rho_product']:.6f}{sd}")


if __name__ == '__main__':
    print_landscape_summary()
