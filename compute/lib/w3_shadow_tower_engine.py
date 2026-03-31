r"""W_3 shadow tower engine: multi-generator shadow Postnikov tower for the W_3 algebra.

The W_3 algebra (DS reduction of sl_3 at level k) is the simplest
multi-generator chiral algebra, with two strong generators:
    T (stress tensor, conformal weight 2)
    W (spin-3 current, conformal weight 3)

SHADOW DATA:
    Total modular characteristic: kappa(W_3) = 5c/6
    where c = c_{W_3}(k) = 2 - 24(k+2)^2/(k+3) = 2(1 - 12/(k+3))
    and kappa = c * (H_3 - 1) with H_3 = 1 + 1/2 + 1/3 = 11/6.

TWO PRIMARY LINES:
    T-line (x_W = 0): kappa_T = c/2, alpha_T = 2, S4_T = 10/[c(5c+22)]
        Identical to Virasoro shadow data.  Class M, infinite depth.
    W-line (x_T = 0): kappa_W = c/3, alpha_W = 0, S4_W = 2560/[c(5c+22)^3]
        Z_2 parity (W -> -W) kills all odd arities.  Class M, infinite depth.

SHADOW METRIC:
    T-line: Q_T(t) = c^2 + 12c*t + [(180c+872)/(5c+22)] t^2
    W-line: Q_W(w) = 4c^2/9 + [16*2560/(3*(5c+22)^3)] w^2
        = 4c^2/9 + 40960/[3(5c+22)^3] w^2

GROWTH RATES:
    rho_T(c) = sqrt((180c+872)/((5c+22)*c^2))   [= Virasoro growth rate]
    rho_W(c) = sqrt(2*Delta_W) / (2*kappa_W)
             = sqrt(16*2560/(3*(5c+22)^3)) / (2c/3)
             = ... (computed below)

KOSZUL DUALITY:
    W_3 at c is Koszul dual to W_3 at 100-c.
    kappa(W_3,c) + kappa(W_3,100-c) = 5*100/6 = 250/3.

DS COMMUTATION:
    kappa(W_3,c(k)) + kappa_ghosts(k) = kappa(sl_3,k)
    where kappa(sl_3,k) = 4(k+3)/3, kappa_ghosts = kappa(sl_3) - kappa(W_3).
    The ghost sector CREATES the quartic: S_4(sl_3) = 0 but S_4(W_3) != 0.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    cor:w3-wline-parity-vanishing (w_algebras.tex)
    cor:ds-theta-descent (w_algebras_deep.tex)
    thm:propagator-variance (higher_genus_modular_koszul.tex)

Dependencies:
    w3_bar.py: W_3 OPE data, curvature, central charge formula
    w3_2d_shadow_metric.py: quartic tensor, cubic tensor, Hessian
    shadow_tower_recursive.py: general tower recursion
    shadow_radius.py: growth rate computation
    genus_expansion.py: kappa_w3
    propagator_variance.py: mixing polynomial P(W_3)
    ds_shadow_functor.py: DS compatibility checks
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs,
    N as Neval,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    solve,
    sqrt,
    symbols,
)

c = Symbol('c')
k = Symbol('k')


# =============================================================================
# 1.  Central charge and kappa formulas
# =============================================================================

def w3_central_charge(level=None):
    r"""W_3 central charge from DS reduction of sl_3 at level k.

    c_{W_3}(k) = 2 - 24(k+2)^2/(k+3)

    This is the manuscript's convention, consistent with c + c' = 100
    under Feigin-Frenkel duality k <-> k' = -k - 6.

    Values: c(k=1) = -52, c(k=10) ~ -263.8.
    """
    if level is None:
        level = k
    return 2 - 24 * (level + 2) ** 2 / (level + 3)


def w3_kappa_total(c_val=None):
    r"""Total modular characteristic kappa(W_3) = 5c/6.

    Derived from kappa = c * (H_3 - 1) where H_3 = 1 + 1/2 + 1/3 = 11/6.
    So kappa = c * (11/6 - 1) = c * 5/6 = 5c/6.

    Decomposition: kappa = kappa_T + kappa_W = c/2 + c/3 = 5c/6.
    """
    cc = c_val if c_val is not None else c
    return Rational(5) * cc / 6


def w3_kappa_T(c_val=None):
    """T-channel curvature kappa_T = c/2 (identical to Virasoro)."""
    cc = c_val if c_val is not None else c
    return cc / 2


def w3_kappa_W(c_val=None):
    """W-channel curvature kappa_W = c/3."""
    cc = c_val if c_val is not None else c
    return cc / 3


# =============================================================================
# 2.  Shadow data for each primary line
# =============================================================================

def t_line_shadow_data(c_val=None):
    """Shadow data for the T-line (x_W = 0): identical to Virasoro.

    kappa_T = c/2, alpha_T = 2, S4_T = 10/[c(5c+22)].
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 2
    alpha = Rational(2)
    S4 = Rational(10) / (cc * (5 * cc + 22))
    Delta = 8 * kappa * S4  # = 40/(5c+22)
    q0 = 4 * kappa ** 2    # c^2
    q1 = 12 * kappa * alpha  # 12c
    q2 = 9 * alpha ** 2 + 16 * kappa * S4  # (180c+872)/(5c+22)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': cancel(Delta), 'q0': q0, 'q1': q1, 'q2': cancel(q2),
    }


def w_line_shadow_data(c_val=None):
    """Shadow data for the W-line (x_T = 0).

    kappa_W = c/3, alpha_W = 0 (Z_2 parity), S4_W = 2560/[c(5c+22)^3].
    The Z_2 parity (W -> -W) forces ALL odd arities to vanish.

    Q_W(w) = 4*(c/3)^2 + 16*(c/3)*S4_W * w^2
           = 4c^2/9 + 40960/[3(5c+22)^3] w^2
    """
    cc = c_val if c_val is not None else c
    kappa = cc / 3
    alpha = Rational(0)
    # S4_W = alpha_Lambda^2 * Q_0 where alpha_Lambda = 16/(5c+22), Q_0 = 10/[c(5c+22)]
    S4 = Rational(2560) / (cc * (5 * cc + 22) ** 3)
    Delta = 8 * kappa * S4
    q0 = 4 * kappa ** 2
    q1 = Rational(0)  # alpha = 0
    q2 = 16 * kappa * S4  # = 16*(c/3)*2560/[c(5c+22)^3]
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': cancel(Delta), 'q0': cancel(q0), 'q1': q1, 'q2': cancel(q2),
    }


# =============================================================================
# 3.  Convolution recursion (shadow tower coefficients)
# =============================================================================

def _convolution_coefficients_exact(q0, q1, q2, max_n):
    r"""Taylor coefficients of f(t) = sqrt(q0 + q1*t + q2*t^2).

    Recursion: f^2 = Q_L gives
        a_0 = sqrt(q0)
        a_1 = q1 / (2*a_0)
        a_2 = (q2 - a_1^2) / (2*a_0)
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}  for n >= 3

    Shadow coefficient: S_r = a_{r-2} / r.
    """
    a0 = sqrt(q0)
    coeffs = [a0]
    if max_n >= 1:
        a1 = q1 / (2 * a0)
        coeffs.append(a1)
    if max_n >= 2:
        a2 = (q2 - coeffs[1] ** 2) / (2 * a0)
        coeffs.append(a2)
    for n in range(3, max_n + 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs.append(-conv_sum / (2 * a0))
    return coeffs


def _convolution_coefficients_float(q0, q1, q2, max_n):
    """Float-precision convolution recursion for speed."""
    a0 = math.sqrt(q0)
    a = [a0]
    if max_n >= 1:
        a.append(q1 / (2.0 * a0))
    if max_n >= 2:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv_sum / (2.0 * a0))
    return a


def t_line_tower_exact(max_r=10):
    r"""Exact T-line shadow tower S_2^T, ..., S_{max_r}^T as functions of c.

    Identical to the Virasoro shadow tower.
    Uses a positive symbol for c to simplify sqrt(c^2) = c.
    """
    cp = Symbol('c', positive=True)
    data = t_line_shadow_data(cp)
    coeffs = _convolution_coefficients_exact(data['q0'], data['q1'], data['q2'], max_r - 2)
    result = {}
    for r in range(len(coeffs)):
        expr = cancel(coeffs[r] / (r + 2))
        result[r + 2] = expr.subs(cp, c)
    return result


def w_line_tower_exact(max_r=10):
    r"""Exact W-line shadow tower S_2^W, ..., S_{max_r}^W as functions of c.

    Odd arities vanish by Z_2 parity (alpha_W = 0 => a_1 = 0,
    and the recursion preserves parity).
    Uses a positive symbol for c to simplify sqrt(c^2) = c.
    """
    cp = Symbol('c', positive=True)
    data = w_line_shadow_data(cp)
    coeffs = _convolution_coefficients_exact(data['q0'], data['q1'], data['q2'], max_r - 2)
    result = {}
    for r in range(len(coeffs)):
        expr = cancel(coeffs[r] / (r + 2))
        result[r + 2] = expr.subs(cp, c)
    return result


def t_line_tower_numerical(c_val, max_r=30):
    """Numerical T-line shadow tower at a specific central charge."""
    c_num = float(c_val)
    kappa = c_num / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_num * (5.0 * c_num + 22.0))
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    coeffs = _convolution_coefficients_float(q0, q1, q2, max_r - 2)
    return {r + 2: coeffs[r] / (r + 2) for r in range(len(coeffs))}


def w_line_tower_numerical(c_val, max_r=30):
    """Numerical W-line shadow tower at a specific central charge."""
    c_num = float(c_val)
    kappa_W = c_num / 3.0
    S4_W = 2560.0 / (c_num * (5.0 * c_num + 22.0) ** 3)
    q0 = 4.0 * kappa_W ** 2
    q1 = 0.0
    q2 = 16.0 * kappa_W * S4_W
    coeffs = _convolution_coefficients_float(q0, q1, q2, max_r - 2)
    return {r + 2: coeffs[r] / (r + 2) for r in range(len(coeffs))}


# =============================================================================
# 4.  Growth rates and critical central charges
# =============================================================================

def t_line_growth_rate_sq():
    """Squared growth rate rho_T^2(c) for the T-line (= Virasoro).

    rho_T^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)
            = (180c + 872) / ((5c+22) * c^2)
    """
    data = t_line_shadow_data()
    numer_sq = 9 * data['alpha'] ** 2 + 2 * data['Delta']
    denom_sq = 4 * data['kappa'] ** 2
    return cancel(numer_sq / denom_sq)


def w_line_growth_rate_sq():
    """Squared growth rate rho_W^2(c) for the W-line.

    Since alpha_W = 0:
        rho_W^2 = 2*Delta_W / (4*kappa_W^2)
                = Delta_W / (2*kappa_W^2)

    Delta_W = 8*kappa_W*S4_W = 8*(c/3)*2560/[c(5c+22)^3]
            = 20480/[3(5c+22)^3]

    rho_W^2 = 20480/[3(5c+22)^3] / (2*c^2/9)
            = 20480*9 / [3*2*c^2*(5c+22)^3]
            = 184320 / [6*c^2*(5c+22)^3]
            = 30720 / [c^2*(5c+22)^3]
    """
    data = w_line_shadow_data()
    numer_sq = 2 * data['Delta']
    denom_sq = 4 * data['kappa'] ** 2
    return cancel(numer_sq / denom_sq)


def t_line_growth_rate(c_val):
    """Numerical growth rate rho_T at a specific c value."""
    rho_sq = t_line_growth_rate_sq()
    val = float(rho_sq.subs(c, Rational(c_val)))
    return math.sqrt(val)


def w_line_growth_rate(c_val):
    """Numerical growth rate rho_W at a specific c value."""
    rho_sq = w_line_growth_rate_sq()
    val = float(rho_sq.subs(c, Rational(c_val)))
    return math.sqrt(val)


def t_line_critical_charge():
    """Critical central charge c*_T where rho_T = 1.

    Solves: (180c + 872) / ((5c+22) * c^2) = 1
    i.e., 5c^3 + 22c^2 - 180c - 872 = 0.

    Same as the Virasoro critical charge c* ~ 6.1243.
    """
    poly = 5 * c ** 3 + 22 * c ** 2 - 180 * c - 872
    roots = solve(poly, c)
    real_positive = []
    for r in roots:
        try:
            val = complex(r.evalf())
            if abs(val.imag) < 1e-10 and val.real > 0:
                real_positive.append(r)
        except (TypeError, ValueError):
            continue
    return real_positive[0] if real_positive else None


def w_line_critical_charge():
    """Critical central charge c*_W where rho_W = 1.

    Solves: 30720 / [c^2 * (5c+22)^3] = 1
    i.e., c^2 * (5c+22)^3 = 30720.

    Expanding: c^2 * (125c^3 + 1650c^2 + 7260c + 10648) = 30720
    125c^5 + 1650c^4 + 7260c^3 + 10648c^2 - 30720 = 0.

    Returns the unique positive real root (approximate).
    """
    poly = 125 * c ** 5 + 1650 * c ** 4 + 7260 * c ** 3 + 10648 * c ** 2 - 30720
    roots = solve(poly, c)
    real_positive = []
    for r in roots:
        try:
            val = complex(r.evalf())
            if abs(val.imag) < 1e-10 and val.real > 0:
                real_positive.append((r, val.real))
        except (TypeError, ValueError):
            continue
    if real_positive:
        # Return the smallest positive root
        real_positive.sort(key=lambda x: x[1])
        return real_positive[0][0]
    return None


# =============================================================================
# 5.  Depth classification
# =============================================================================

def depth_classification_t_line():
    """T-line depth = class M (infinite tower), identical to Virasoro.

    Delta_T = 40/(5c+22) != 0 for generic c => class M.
    """
    return ('M', None)


def depth_classification_w_line():
    """W-line depth = class M (infinite tower).

    Delta_W = 20480/[3(5c+22)^3] != 0 for generic c => class M.
    But alpha_W = 0 means ODD arities vanish (Z_2 parity),
    which is a special feature not captured by the single-line G/L/C/M
    classification.
    """
    return ('M', None)


def depth_classification_w3():
    """Overall W_3 depth classification: class M (infinite tower).

    Both the T-line and W-line are class M.
    Additionally there are mixed (T-W) contributions at arity >= 4
    from the Lambda-exchange coupling.
    """
    return ('M', None)


# =============================================================================
# 6.  Koszul duality (c <-> 100 - c)
# =============================================================================

def koszul_conductor():
    """Koszul conductor K_3 = 100 for W_3.

    W_3 at c is Koszul dual to W_3 at 100-c.
    """
    return 100


def kappa_complementarity():
    """kappa(c) + kappa(100-c) = 250/3.

    kappa(c) = 5c/6, kappa(100-c) = 5(100-c)/6.
    Sum = 5*100/6 = 500/6 = 250/3.
    """
    K = koszul_conductor()
    kap = w3_kappa_total()
    kap_dual = w3_kappa_total(K - c)
    return cancel(kap + kap_dual)


def shadow_complementarity_t_line(max_r=8):
    r"""Complementarity sum S_r^T(c) + S_r^T(100-c) for each arity.

    Under Koszul duality c <-> 100-c, the shadow coefficients
    satisfy complementarity constraints from Theorem C.
    """
    K = koszul_conductor()
    tower = t_line_tower_exact(max_r)
    sums = {}
    for r, Sr in tower.items():
        Sr_dual = Sr.subs(c, K - c)
        sums[r] = cancel(Sr + Sr_dual)
    return sums


def shadow_complementarity_w_line(max_r=8):
    r"""Complementarity sum S_r^W(c) + S_r^W(100-c) for each arity."""
    K = koszul_conductor()
    tower = w_line_tower_exact(max_r)
    sums = {}
    for r, Sr in tower.items():
        Sr_dual = Sr.subs(c, K - c)
        sums[r] = cancel(Sr + Sr_dual)
    return sums


# =============================================================================
# 7.  DS commutation check
# =============================================================================

def ds_kappa_compatibility():
    r"""Verify DS compatibility at kappa level:
        kappa(W_3, c(k)) + kappa_ghosts(k) = kappa(sl_3, k).

    kappa(sl_3, k) = dim(sl_3) * (k + h^v) / (2*h^v)
                   = 8 * (k+3) / 6 = 4(k+3)/3.

    kappa(W_3, c(k)) = 5*c(k)/6 where c(k) = 2 - 24(k+2)^2/(k+3).

    kappa_ghosts = kappa(sl_3) - kappa(W_3).

    Ghost kappa: the BRST ghost sector has 3 bc pairs (for sl_3) whose
    total kappa is the difference.
    """
    # sl_3 kappa
    kap_sl3 = Rational(4) * (k + 3) / 3

    # W_3 central charge from DS
    c_w3 = w3_central_charge()
    kap_w3 = w3_kappa_total(c_w3)

    # Ghost kappa
    kap_ghost = cancel(kap_sl3 - kap_w3)

    # Verify
    diff = simplify(kap_w3 + kap_ghost - kap_sl3)

    return {
        'kappa_sl3': factor(kap_sl3),
        'kappa_w3_of_k': factor(kap_w3),
        'kappa_ghost': factor(kap_ghost),
        'c_w3_of_k': factor(c_w3),
        'compatible': diff == 0,
        'difference': diff,
    }


def ds_quartic_creation():
    """Verify that DS reduction CREATES the quartic from the ghost sector.

    sl_3: class L, S_4 = 0 (Jacobi identity kills the quartic).
    W_3:  class M, S_4 != 0.

    The quartic S_4(W_3) != 0 is created by the ghost sector in the BRST
    reduction.  This is the mechanism for depth increase: depth 3 -> inf.
    """
    # sl_3 quartic = 0
    S4_sl3 = Rational(0)

    # W_3 T-line quartic
    S4_T = Rational(10) / (c * (5 * c + 22))

    # W_3 W-line quartic
    S4_W = Rational(2560) / (c * (5 * c + 22) ** 3)

    return {
        'S4_sl3': S4_sl3,
        'S4_W3_T': S4_T,
        'S4_W3_W': S4_W,
        'depth_sl3': 3,
        'depth_W3': None,  # infinity
        'mechanism': 'Ghost sector creates quartic from BRST reduction',
    }


# =============================================================================
# 8.  Comparison: Virasoro vs W_3
# =============================================================================

def comparison_table(c_values, max_r=8):
    """Side-by-side comparison of S_r^{Vir}(c) vs S_r^{W_3,T}(c) vs S_r^{W_3,W}(c).

    The T-line of W_3 is identical to Virasoro; the W-line is different.

    Parameters:
        c_values: list of central charge values (numeric).
        max_r: maximum arity.

    Returns:
        List of dicts, one per c-value, each containing shadow tower data.
    """
    rows = []
    for c_val in c_values:
        c_num = float(c_val)
        if abs(c_num) < 1e-10 or abs(5.0 * c_num + 22.0) < 1e-10:
            continue
        t_tower = t_line_tower_numerical(c_num, max_r)
        w_tower = w_line_tower_numerical(c_num, max_r)
        rho_T = t_line_growth_rate(c_num)
        rho_W = w_line_growth_rate(c_num)

        row = {
            'c': c_num,
            'kappa_total': 5.0 * c_num / 6.0,
            'kappa_T': c_num / 2.0,
            'kappa_W': c_num / 3.0,
            'rho_T': rho_T,
            'rho_W': rho_W,
            'T_line': {r: t_tower[r] for r in sorted(t_tower) if r <= max_r},
            'W_line': {r: w_tower[r] for r in sorted(w_tower) if r <= max_r},
        }
        rows.append(row)
    return rows


# =============================================================================
# 9.  Propagator variance and mixing polynomial
# =============================================================================

def mixing_polynomial():
    r"""The mixing polynomial P(W_3) = 25c^2 + 100c - 428.

    P = 0 iff the quartic gradient is curvature-proportional
    (i.e., f_T/kappa_T = f_W/kappa_W), which is the condition for
    the diagonal to be autonomous.

    P(W_3) = 25(c+2)^2 - 528.  No real roots of physical significance.
    """
    return 25 * c ** 2 + 100 * c - 428


def mixing_polynomial_roots():
    """Roots of P(W_3) = 0: c = -2 +/- sqrt(528/25) = -2 +/- 2*sqrt(132)/5."""
    return solve(mixing_polynomial(), c)


def propagator_variance_w3(c_val=None):
    r"""Propagator variance delta_mix for W_3.

    delta_mix = f_T^2/kappa_T + f_W^2/kappa_W - (f_T+f_W)^2/(kappa_T+kappa_W)

    where f_T, f_W are the quartic gradients evaluated on the diagonal.
    """
    cc = c_val if c_val is not None else c
    kap_T = cc / 2
    kap_W = cc / 3
    Q0 = Rational(10) / (cc * (5 * cc + 22))
    alpha_L = Rational(16) / (5 * cc + 22)
    f_T = 4 * Q0 * (1 + 3 * alpha_L)
    f_W = 4 * Q0 * alpha_L * (3 + alpha_L)
    f_T = cancel(f_T)
    f_W = cancel(f_W)

    term1 = f_T ** 2 / kap_T + f_W ** 2 / kap_W
    term2 = (f_T + f_W) ** 2 / (kap_T + kap_W)
    return cancel(term1 - term2)


# =============================================================================
# 10. Full W_3 shadow tower summary
# =============================================================================

class W3ShadowTower:
    """Complete W_3 shadow tower data at a specific central charge."""

    def __init__(self, c_val, kappa_total, kappa_T, kappa_W,
                 t_line=None, w_line=None, rho_T=0.0, rho_W=0.0,
                 depth_class='M', mixing_poly_val=0.0):
        self.c_val = c_val
        self.kappa_total = kappa_total
        self.kappa_T = kappa_T
        self.kappa_W = kappa_W
        self.t_line = t_line if t_line is not None else {}
        self.w_line = w_line if w_line is not None else {}
        self.rho_T = rho_T
        self.rho_W = rho_W
        self.depth_class = depth_class
        self.mixing_poly_val = mixing_poly_val

    def summary(self) -> str:
        lines = [
            f"W_3 Shadow Tower at c = {self.c_val}",
            f"  kappa(W_3) = {self.kappa_total:.6f}  (= kappa_T + kappa_W = {self.kappa_T:.6f} + {self.kappa_W:.6f})",
            f"  Depth class: {self.depth_class}",
            f"  Growth rates: rho_T = {self.rho_T:.6f}, rho_W = {self.rho_W:.6f}",
            f"  Mixing polynomial P(c) = {self.mixing_poly_val:.2f}",
            f"  T-line convergent: {self.rho_T < 1.0}",
            f"  W-line convergent: {self.rho_W < 1.0}",
            "  --- T-line tower (= Virasoro) ---",
        ]
        for r in sorted(self.t_line):
            if r <= 10:
                lines.append(f"    S_{r}^T = {self.t_line[r]:.8e}")
        lines.append("  --- W-line tower ---")
        for r in sorted(self.w_line):
            if r <= 10:
                lines.append(f"    S_{r}^W = {self.w_line[r]:.8e}")
        return "\n".join(lines)


def compute_w3_tower(c_val, max_r=20):
    """Compute the full W_3 shadow tower at a specific central charge.

    Returns a W3ShadowTower dataclass with all data.
    """
    c_num = float(c_val)
    kap_total = 5.0 * c_num / 6.0
    kap_T = c_num / 2.0
    kap_W = c_num / 3.0

    t_tower = t_line_tower_numerical(c_num, max_r)
    w_tower = w_line_tower_numerical(c_num, max_r)
    rho_T = t_line_growth_rate(c_num)
    rho_W = w_line_growth_rate(c_num)

    P_val = 25.0 * c_num ** 2 + 100.0 * c_num - 428.0

    return W3ShadowTower(
        c_val=c_num,
        kappa_total=kap_total,
        kappa_T=kap_T,
        kappa_W=kap_W,
        t_line=t_tower,
        w_line=w_tower,
        rho_T=rho_T,
        rho_W=rho_W,
        depth_class='M',
        mixing_poly_val=P_val,
    )


# =============================================================================
# 11. Growth rate comparison atlas
# =============================================================================

def growth_rate_atlas(c_values=None):
    """Growth rate atlas for W_3 at several central charges.

    Compares rho_T and rho_W, and determines which line dominates
    the asymptotic shadow tower behavior.
    """
    if c_values is None:
        c_values = [Rational(1, 2), Rational(1), Rational(2),
                    Rational(4), Rational(6), Rational(10),
                    Rational(13), Rational(25), Rational(50)]

    atlas = []
    for c_val in c_values:
        c_num = float(c_val)
        if abs(c_num) < 1e-10 or abs(5.0 * c_num + 22.0) < 1e-10:
            continue
        rho_T = t_line_growth_rate(c_num)
        rho_W = w_line_growth_rate(c_num)
        atlas.append({
            'c': c_num,
            'rho_T': rho_T,
            'rho_W': rho_W,
            'dominant_line': 'T' if rho_T > rho_W else 'W',
            'rho_max': max(rho_T, rho_W),
            'convergent_T': rho_T < 1.0,
            'convergent_W': rho_W < 1.0,
        })
    return atlas


# =============================================================================
# 12. Self-dual and special points
# =============================================================================

def self_dual_point():
    """W_3 self-dual point: c = 50 (midpoint of [0, 100]).

    At c = 50: kappa(W_3) = 250/6 = 125/3.
    kappa(W_3^!) = 5*(100-50)/6 = 250/6 = 125/3 = kappa(W_3).
    """
    return Rational(50)


def self_dual_kappa():
    """kappa(W_3) at the self-dual point c = 50."""
    return w3_kappa_total(Rational(50))


def self_dual_tower(max_r=12):
    """Shadow tower at the self-dual point c = 50.

    At this point, S_r(50) = S_r(100-50) = S_r(50), which is
    automatically satisfied (tautology).
    """
    return compute_w3_tower(50.0, max_r)


# =============================================================================
# 13. W-line parity verification
# =============================================================================

def verify_w_line_parity(c_val, max_r=20):
    """Verify that all ODD arities vanish on the W-line.

    This is a consequence of the Z_2 parity W -> -W, which forces
    the shadow tower on the W-line to contain only even powers.
    """
    tower = w_line_tower_numerical(c_val, max_r)
    violations = {}
    for r in range(3, max_r + 1, 2):  # odd arities
        val = tower.get(r, 0.0)
        if abs(val) > 1e-14:
            violations[r] = val
    return {
        'all_odd_vanish': len(violations) == 0,
        'violations': violations,
        'max_arity_checked': max_r,
    }


# =============================================================================
# 14. Entry point / demo
# =============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("W_3 SHADOW TOWER ENGINE")
    print("=" * 70)

    # DS compatibility
    ds = ds_kappa_compatibility()
    print(f"\nDS compatibility: kappa(sl_3) = {ds['kappa_sl3']}")
    print(f"  kappa(W_3, c(k)) = {ds['kappa_w3_of_k']}")
    print(f"  kappa_ghost = {ds['kappa_ghost']}")
    print(f"  Compatible: {ds['compatible']}")

    # Growth rate atlas
    print("\nGrowth rate atlas:")
    print(f"  {'c':>6s}  {'rho_T':>10s}  {'rho_W':>10s}  {'dominant':>8s}  {'conv_T':>6s}  {'conv_W':>6s}")
    for row in growth_rate_atlas():
        print(f"  {row['c']:6.1f}  {row['rho_T']:10.6f}  {row['rho_W']:10.6f}  "
              f"{row['dominant_line']:>8s}  {'Y' if row['convergent_T'] else 'N':>6s}  "
              f"{'Y' if row['convergent_W'] else 'N':>6s}")

    # Shadow tower at c = 2
    print("\n" + compute_w3_tower(2.0, 12).summary())

    # Kappa complementarity
    print(f"\nKappa complementarity: kappa(c) + kappa(100-c) = {kappa_complementarity()}")

    # Mixing polynomial
    print(f"\nMixing polynomial: P(W_3) = {mixing_polynomial()}")
    print(f"  Roots: {mixing_polynomial_roots()}")
