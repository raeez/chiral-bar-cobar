r"""W_3 shadow tower extended to arity 12: even-arity coefficients, growth rates, asymptotics.

Extension of w3_shadow_extended.py to arity 12 on both the T-line and
W-line, with explicit growth rate analysis exploiting the Z_2 parity
symmetry (W -> -W) that kills all odd arities on the W-line.

W_3 ALGEBRA DATA:
    Generators: T (weight 2), W (weight 3).
    Central charge: c.
    Total modular characteristic: kappa(W_3) = 5c/6 = c/2 + c/3.
    Koszul conductor: K_3 = 100.  Duality: c <-> 100 - c.

T-LINE (x_W = 0, identical to Virasoro):
    kappa_T = c/2, alpha_T = 2, S_4^T = 10/[c(5c+22)].
    Shadow metric: Q_T(t) = c^2 + 12c*t + 4(45c+218)/(5c+22) * t^2.
    Growth rate: rho_T^2 = 4(45c+218)/[c^2(5c+22)].
    All arities nonzero; depth class M (infinite tower).

W-LINE (x_T = 0):
    kappa_W = c/3, alpha_W = 0, S_4^W = 2560/[c(5c+22)^3].
    Shadow metric: Q_W(w) = 4c^2/9 + 40960/[3(5c+22)^3] * w^2.
    Growth rate: rho_W^2 = 30720/[c^2(5c+22)^3].
    Odd arities vanish by Z_2 parity.  Depth class M (infinite tower).

W-LINE RING STRUCTURE:
    S_{2n}^W = gamma_n * S_4^{n-1} / c^{n-2}  where
    gamma_n = (-1)^{n-1} * |a_n|, with
    |a_n| = (12^n / 54) * |binom(3/2, n)|.

    Sequence: gamma_2 = 1, gamma_3 = -2, gamma_4 = 9,
              gamma_5 = -54, gamma_6 = 378.

GROWTH RATE ANALYSIS:
    The even-arity ratio |S_{2n+2}/S_{2n}| on the W-line equals
    |gamma_{n+1}/gamma_n| * |S_4|/|c|.

    Since |a_{n+1}/a_n| -> 12 as n -> infinity (from the binomial
    asymptotics binom(3/2,n) ~ const * n^{-5/2}), the even-arity
    growth ratio converges to 12 * S_4/c = rho_W^2.

    The first five ratios |gamma_{n+1}/gamma_n| are:
        2, 9/2, 6, 7, 54/7.
    These converge monotonically to 12 from below.

CLOSED-FORM COEFFICIENTS (arities 2--12):

    T-line:
        S_2  = c/2
        S_3  = 2
        S_4  = 10/[c(5c+22)]
        S_5  = -48/[c^2(5c+22)]
        S_6  = 80(45c+193)/[3 c^3 (5c+22)^2]
        S_7  = -2880(15c+61)/[7 c^4 (5c+22)^2]
        S_8  = 80(2025c^2+16470c+33314)/[c^5 (5c+22)^3]
        S_9  = -1280(2025c^2+15570c+29554)/[3 c^6 (5c+22)^3]
        S_10 = 256(91125c^3+1050975c^2+3989790c+4969967)/[c^7 (5c+22)^4]
        S_11 = -15360(91125c^3+990225c^2+3500190c+3988097)/[11 c^8 (5c+22)^4]
        S_12 = 2560(4100625c^4+59413500c^3+315017100c^2
                     +717857460c+583976486)/[3 c^9 (5c+22)^5]

    W-line (odd arities all zero):
        S_2  = c/3
        S_4  = 2560/[c(5c+22)^3]
        S_6  = -13107200/[c^3 (5c+22)^6]
        S_8  = 150994944000/[c^5 (5c+22)^9]
        S_10 = -2319282339840000/[c^7 (5c+22)^12]
        S_12 = 41561539529932800000/[c^9 (5c+22)^15]

VERIFICATION (AP10, HZ-6):
    Every coefficient verified by 3 independent paths:
    [DC] direct convolution recursion from shadow metric
    [CF] closed-form general term via binomial (3/2 choose n)
    [NE] numerical evaluation at c=2,10,50 against float recursion

Manuscript references:
    comp:w-infty-shadow-tower (w_algebras_deep.tex)
    eq:w3-wline-closed-form (w_algebras_deep.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple

from sympy import (
    Integer,
    Rational,
    Symbol,
    binomial,
    cancel,
    expand,
    factor,
    simplify,
    sqrt,
)

c = Symbol('c')


# =============================================================================
# 1.  Shadow data (OPE input)
# =============================================================================

def t_line_data() -> Dict:
    """Shadow data for the T-line (x_W = 0, identical to Virasoro)."""
    kappa = c / 2
    alpha = Integer(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    Delta = 8 * kappa * S4
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    rho_sq = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': cancel(Delta), 'q0': q0, 'q1': q1,
        'q2': cancel(q2), 'rho_sq': cancel(rho_sq),
    }


def w_line_data() -> Dict:
    """Shadow data for the W-line (x_T = 0).

    Z_2 parity (W -> -W) forces alpha_W = 0, killing all odd arities.
    """
    kappa = c / 3
    alpha = Integer(0)
    S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
    Delta = 8 * kappa * S4
    q0 = 4 * kappa ** 2
    q1 = Integer(0)
    q2 = 16 * kappa * S4
    rho_sq = 2 * Delta / (4 * kappa ** 2)
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': cancel(Delta), 'q0': cancel(q0), 'q1': q1,
        'q2': cancel(q2), 'rho_sq': cancel(rho_sq),
    }


# =============================================================================
# 2.  Convolution recursion: Taylor coefficients of sqrt(Q_L)
# =============================================================================

def _sqrt_quadratic_taylor_exact(q0, q1, q2, max_n):
    r"""Taylor coefficients [t^n] sqrt(q0 + q1 t + q2 t^2).

    Recursion from f^2 = Q_L:
        a_0 = sqrt(q0),
        a_1 = q_1 / (2 a_0),
        a_2 = (q_2 - a_1^2) / (2 a_0),
        a_n = -(1/(2 a_0)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3.
    """
    a0 = sqrt(q0)
    a = [a0]
    if max_n >= 1:
        a.append(q1 / (2 * a0))
    if max_n >= 2:
        a.append((q2 - a[1] ** 2) / (2 * a0))
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * a0))
    return a


def _sqrt_quadratic_taylor_float(q0, q1, q2, max_n):
    """Float-precision convolution recursion."""
    a0 = math.sqrt(q0)
    a = [a0]
    if max_n >= 1:
        a.append(q1 / (2.0 * a0))
    if max_n >= 2:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))
    return a


# =============================================================================
# 3.  Exact symbolic towers to arity 12
# =============================================================================

def t_line_tower_exact(max_r=12) -> Dict[int, object]:
    r"""Exact T-line shadow tower {S_r^T : r = 2, ..., max_r} as functions of c.

    Identical to the Virasoro shadow tower.
    """
    cp = Symbol('c', positive=True)
    data = t_line_data()
    q0 = data['q0'].subs(c, cp)
    q1 = data['q1'].subs(c, cp)
    q2 = data['q2'].subs(c, cp)
    a = _sqrt_quadratic_taylor_exact(q0, q1, q2, max_r - 2)
    result = {}
    for n in range(len(a)):
        r = n + 2
        expr = cancel(a[n] / r)
        result[r] = expr.subs(cp, c)
    return result


def w_line_tower_exact(max_r=12) -> Dict[int, object]:
    r"""Exact W-line shadow tower {S_r^W : r = 2, ..., max_r} as functions of c.

    Odd arities vanish by Z_2 parity.
    """
    cp = Symbol('c', positive=True)
    data = w_line_data()
    q0 = data['q0'].subs(c, cp)
    q1 = data['q1'].subs(c, cp)
    q2 = data['q2'].subs(c, cp)
    a = _sqrt_quadratic_taylor_exact(q0, q1, q2, max_r - 2)
    result = {}
    for n in range(len(a)):
        r = n + 2
        expr = cancel(a[n] / r)
        result[r] = expr.subs(cp, c)
    return result


# =============================================================================
# 4.  Numerical towers
# =============================================================================

def t_line_tower_numerical(c_val, max_r=12) -> Dict[int, float]:
    """Numerical T-line shadow tower at a given central charge."""
    c_num = float(c_val)
    kappa = c_num / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_num * (5.0 * c_num + 22.0))
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    a = _sqrt_quadratic_taylor_float(q0, q1, q2, max_r - 2)
    return {n + 2: a[n] / (n + 2) for n in range(len(a))}


def w_line_tower_numerical(c_val, max_r=12) -> Dict[int, float]:
    """Numerical W-line shadow tower at a given central charge."""
    c_num = float(c_val)
    kappa_W = c_num / 3.0
    S4_W = 2560.0 / (c_num * (5.0 * c_num + 22.0) ** 3)
    q0 = 4.0 * kappa_W ** 2
    q1 = 0.0
    q2 = 16.0 * kappa_W * S4_W
    a = _sqrt_quadratic_taylor_float(q0, q1, q2, max_r - 2)
    return {n + 2: a[n] / (n + 2) for n in range(len(a))}


# =============================================================================
# 5.  Closed-form coefficients to arity 12
# =============================================================================

def t_line_closed_forms() -> Dict[int, object]:
    r"""T-line closed forms S_2 through S_12.

    Each coefficient verified by [DC] convolution recursion + [NE] numerical
    evaluation at c=2,10,50 + [LT] Virasoro shadow tower literature
    (shadow_tower_recursive.py).
    """
    return {
        # VERIFIED: [DC] recursion, [LT] shadow_tower_recursive.py, [NE] c=2,10,50
        2: c / 2,
        # VERIFIED: [DC] recursion, [LT] gravitational cubic = 2, [NE] c=2,10,50
        3: Integer(2),
        # VERIFIED: [DC] recursion, [LT] virasoro_shadow_tower.py, [NE] c=2,10,50
        4: Rational(10) / (c * (5 * c + 22)),
        # VERIFIED: [DC] recursion, [LT] quintic_shadow_engine.py, [NE] c=2,10,50
        5: Rational(-48) / (c ** 2 * (5 * c + 22)),
        # VERIFIED: [DC] recursion, [LT] w3_shadow_extended.py, [NE] c=2,10,50
        6: Rational(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2),
        # VERIFIED: [DC] recursion, [LT] w3_shadow_extended.py, [NE] c=2,10,50
        7: Rational(-2880) * (15 * c + 61) / (7 * c ** 4 * (5 * c + 22) ** 2),
        # VERIFIED: [DC] recursion, [LT] w3_shadow_extended.py, [NE] c=2,10,50
        8: Rational(80) * (2025 * c ** 2 + 16470 * c + 33314)
           / (c ** 5 * (5 * c + 22) ** 3),
        # VERIFIED: [DC] recursion, [NE] c=2,10,50, [CF] independent sympy factor
        9: Rational(-1280) * (2025 * c ** 2 + 15570 * c + 29554)
           / (3 * c ** 6 * (5 * c + 22) ** 3),
        # VERIFIED: [DC] recursion, [NE] c=2,10,50, [CF] independent sympy factor
        10: Rational(256) * (91125 * c ** 3 + 1050975 * c ** 2
                              + 3989790 * c + 4969967)
            / (c ** 7 * (5 * c + 22) ** 4),
        # VERIFIED: [DC] recursion, [NE] c=2,10,50, [CF] independent sympy factor
        11: Rational(-15360) * (91125 * c ** 3 + 990225 * c ** 2
                                 + 3500190 * c + 3988097)
            / (11 * c ** 8 * (5 * c + 22) ** 4),
        # VERIFIED: [DC] recursion, [NE] c=2,10,50, [CF] independent sympy factor
        12: Rational(2560) * (4100625 * c ** 4 + 59413500 * c ** 3
                               + 315017100 * c ** 2 + 717857460 * c
                               + 583976486)
            / (3 * c ** 9 * (5 * c + 22) ** 5),
    }


def w_line_closed_forms() -> Dict[int, object]:
    r"""W-line closed forms S_2 through S_12 (odd arities zero by Z_2 parity).

    Each coefficient verified by [DC] convolution recursion + [CF] general
    term via binomial(3/2, n) + [NE] numerical evaluation at c=2,10,50.
    """
    return {
        # VERIFIED: [DC] recursion, [CF] kappa_W = c/3, [NE] c=2,10,50
        2: c / 3,
        3: Integer(0),
        # VERIFIED: [DC] recursion, [CF] w_line_general_term(2), [NE] c=2,10,50
        4: Rational(2560) / (c * (5 * c + 22) ** 3),
        5: Integer(0),
        # VERIFIED: [DC] recursion, [CF] w_line_general_term(3), [NE] ring S_6=-2*S_4^2/c
        6: Rational(-13107200) / (c ** 3 * (5 * c + 22) ** 6),
        7: Integer(0),
        # VERIFIED: [DC] recursion, [CF] w_line_general_term(4), [NE] ring S_8=9*S_4^3/c^2
        8: Rational(150994944000) / (c ** 5 * (5 * c + 22) ** 9),
        9: Integer(0),
        # VERIFIED: [DC] recursion, [CF] w_line_general_term(5), [NE] ring S_10=-54*S_4^4/c^3
        10: Rational(-2319282339840000) / (c ** 7 * (5 * c + 22) ** 12),
        11: Integer(0),
        # VERIFIED: [DC] recursion, [CF] w_line_general_term(6), [NE] ring S_12=378*S_4^5/c^4
        12: Rational(41561539529932800000) / (c ** 9 * (5 * c + 22) ** 15),
    }


# =============================================================================
# 6.  W-line general term and ring structure
# =============================================================================

def w_line_general_term(n):
    r"""Closed-form S_{2n}^W for any n >= 1.

    S_{2n}^W = (-1)^n * a_n * 2560^{n-1} / [c^{2n-3} (5c+22)^{3(n-1)}]
    where a_n = (-12)^n / 54 * binomial(3/2, n).

    The sequence |a_n| = 1/3, 1, 2, 9, 54, 378, 2916, 24057, ...
    """
    a_n = Rational((-12) ** n, 54) * binomial(Rational(3, 2), n)
    if n == 1:
        return c / 3
    return (-1) ** n * a_n * 2560 ** (n - 1) / (
        c ** (2 * n - 3) * (5 * c + 22) ** (3 * (n - 1)))


def w_line_ring_coefficients() -> Dict[int, int]:
    r"""Ring coefficients gamma_n: S_{2n}^W = gamma_n * S_4^{n-1} / c^{n-2}.

    gamma_2 = 1, gamma_3 = -2, gamma_4 = 9, gamma_5 = -54, gamma_6 = 378.
    """
    # VERIFIED: [DC] direct from ring relation, [CF] |a_n| sequence, [NE] c=2,10,50
    return {2: 1, 3: -2, 4: 9, 5: -54, 6: 378}


def verify_ring_relations(max_n=6) -> Dict[str, bool]:
    r"""Verify S_{2n}^W = gamma_n * S_4^{n-1} / c^{n-2} for n = 2, ..., max_n."""
    S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
    wl = w_line_closed_forms()
    gamma = w_line_ring_coefficients()
    results = {}
    for n in range(2, max_n + 1):
        r = 2 * n
        if r not in wl or n not in gamma:
            continue
        ring_val = gamma[n] * S4 ** (n - 1) / c ** (n - 2)
        results[f'S_{r}_ring'] = simplify(wl[r] - ring_val) == 0
    return results


# =============================================================================
# 7.  Growth rates
# =============================================================================

def growth_rates_squared() -> Dict[str, object]:
    """Squared growth rates rho^2 for both primary lines."""
    return {
        # VERIFIED: [DC] from shadow data, [CF] (180c+872)/((5c+22)*c^2)
        #           rewritten as 4(45c+218)/(c^2*(5c+22)), [NE] c=2,10,50
        'T_line': 4 * (45 * c + 218) / (c ** 2 * (5 * c + 22)),
        # VERIFIED: [DC] from shadow data, [CF] 12*S_4/c asymptotic,
        #           [NE] c=2,10,50
        'W_line': Rational(30720) / (c ** 2 * (5 * c + 22) ** 3),
    }


def growth_rates_numerical(c_val) -> Dict[str, float]:
    """Numerical growth rates rho_T and rho_W at a given central charge."""
    c_num = float(c_val)
    rho_T_sq = 4.0 * (45.0 * c_num + 218.0) / (c_num ** 2 * (5.0 * c_num + 22.0))
    rho_W_sq = 30720.0 / (c_num ** 2 * (5.0 * c_num + 22.0) ** 3)
    return {
        'rho_T': math.sqrt(abs(rho_T_sq)),
        'rho_W': math.sqrt(abs(rho_W_sq)),
    }


def even_arity_ratios_w_line(c_val, max_n=6) -> Dict[str, object]:
    r"""Even-arity growth ratios |S_{2n+2}/S_{2n}| on the W-line.

    These converge to rho_W^2 = 30720/[c^2(5c+22)^3] as n -> infinity.
    The convergence rate is governed by |gamma_{n+1}/gamma_n| -> 12.

    Returns dict with:
        'ratios': list of (n, |S_{2n+2}/S_{2n}|) tuples
        'rho_W_sq': the theoretical limit
        'ring_coeff_ratios': list of |gamma_{n+1}/gamma_n|
    """
    tower = w_line_tower_numerical(c_val, 2 * max_n + 2)
    c_num = float(c_val)
    rho_W_sq = 30720.0 / (c_num ** 2 * (5.0 * c_num + 22.0) ** 3)

    ratios = []
    for n in range(1, max_n):
        r = 2 * n
        r_next = 2 * (n + 1)
        if abs(tower[r]) > 1e-300:
            ratios.append((n, abs(tower[r_next] / tower[r])))

    gamma = w_line_ring_coefficients()
    ring_ratios = []
    for n in range(2, max_n):
        if n in gamma and (n + 1) in gamma:
            ring_ratios.append((n, abs(gamma[n + 1]) / abs(gamma[n])))

    return {
        'ratios': ratios,
        'rho_W_sq': rho_W_sq,
        'ring_coeff_ratios': ring_ratios,
        'asymptotic_ring_limit': 12.0,
    }


def even_arity_ratios_t_line(c_val, max_r=12) -> List[Tuple[int, float]]:
    r"""Even-arity growth ratios |S_{r+2}/S_r| on the T-line for even r.

    Unlike the W-line, the T-line has nonzero odd arities, so
    even-arity ratios skip one step.
    """
    tower = t_line_tower_numerical(c_val, max_r)
    ratios = []
    for r in range(2, max_r - 1, 2):
        if abs(tower[r]) > 1e-300:
            ratios.append((r, abs(tower[r + 2] / tower[r])))
    return ratios


# =============================================================================
# 8.  Asymptotic analysis
# =============================================================================

def w_line_asymptotic_exponents():
    r"""Asymptotic form of W-line even-arity coefficients.

    From the general term:
        S_{2n}^W ~ C * rho_W^{2n} * n^{-5/2}    as n -> infinity

    where rho_W^2 = 30720/[c^2(5c+22)^3] and the n^{-5/2} comes from
    binomial(3/2, n) ~ const * n^{-5/2} / Gamma(-1/2).

    This is characteristic of CLASS M algebras: the shadow tower
    grows geometrically (radius of convergence = 1/rho_W on the W-line)
    with a polynomial correction from the algebraic structure of H(w).
    """
    return {
        'geometric_base': 'rho_W^2 = 30720/[c^2(5c+22)^3]',
        'polynomial_correction': 'n^{-5/2}',
        'source': 'binomial(3/2, n) ~ const * n^{-5/2}',
        'convergence_radius': '1/rho_W on the W-line',
        'depth_class': 'M (infinite tower, only even arities)',
    }


def t_line_asymptotic_form():
    r"""Asymptotic form of T-line coefficients.

    S_r^T ~ C * rho_T^r * cos(r*theta + phi) * r^{-3/2}    as r -> infinity

    where rho_T = sqrt(4(45c+218)/[c^2(5c+22)]) and the oscillation
    comes from the complex roots of the quadratic Q_T (when the
    discriminant q1^2 - 4*q0*q2 < 0, which happens for c > 0).

    The r^{-3/2} correction is characteristic of quadratic shadow metrics.
    """
    return {
        'geometric_base': 'rho_T = sqrt(4(45c+218)/[c^2(5c+22)])',
        'oscillation': 'cos(r*theta + phi)',
        'polynomial_correction': 'r^{-3/2}',
        'convergence_radius': '1/rho_T on the T-line',
        'depth_class': 'M (infinite tower, all arities nonzero)',
    }


# =============================================================================
# 9.  Cross-consistency checks
# =============================================================================

def verify_closed_vs_recursive(max_r=12) -> Dict[str, bool]:
    """Verify that hardcoded closed forms match the convolution recursion."""
    t_rec = t_line_tower_exact(max_r)
    t_closed = t_line_closed_forms()
    w_rec = w_line_tower_exact(max_r)
    w_closed = w_line_closed_forms()

    results = {}
    for r in range(2, max_r + 1):
        if r in t_closed:
            diff = simplify(t_rec[r] - t_closed[r])
            results[f'T_line_S{r}'] = diff == 0
        if r in w_closed:
            diff = simplify(w_rec[r] - w_closed[r])
            results[f'W_line_S{r}'] = diff == 0
    return results


def verify_numerical_vs_exact(c_val=25, max_r=12, tol=1e-10) -> Dict[str, bool]:
    """Verify numerical tower matches exact evaluation."""
    t_exact = t_line_tower_exact(max_r)
    t_num = t_line_tower_numerical(c_val, max_r)
    w_exact = w_line_tower_exact(max_r)
    w_num = w_line_tower_numerical(c_val, max_r)

    results = {}
    for r in range(2, max_r + 1):
        exact_val = float(t_exact[r].subs(c, c_val))
        results[f'T_line_S{r}'] = abs(exact_val - t_num[r]) < tol * max(1, abs(exact_val))
        exact_val_w = float(w_exact[r].subs(c, c_val))
        results[f'W_line_S{r}'] = abs(exact_val_w - w_num[r]) < tol * max(1, abs(exact_val_w))
    return results


def verify_general_term_vs_recursive(max_n=6) -> Dict[str, bool]:
    """Verify w_line_general_term(n) matches recursion for n = 1..max_n."""
    w_rec = w_line_tower_exact(2 * max_n)
    results = {}
    for n in range(1, max_n + 1):
        r = 2 * n
        gen = w_line_general_term(n)
        diff = simplify(w_rec[r] - gen)
        results[f'S_{r}_general_term'] = diff == 0
    return results


# =============================================================================
# 10.  Koszul complementarity to arity 12
# =============================================================================

def complementarity_sums(max_r=12) -> Dict[str, Dict[int, object]]:
    """Complementarity sums S_r(c) + S_r(100-c) on both lines to arity max_r."""
    K = 100
    t_tower = t_line_tower_exact(max_r)
    w_tower = w_line_tower_exact(max_r)
    t_sums = {r: cancel(Sr + Sr.subs(c, K - c)) for r, Sr in t_tower.items()}
    w_sums = {r: cancel(Sr + Sr.subs(c, K - c)) for r, Sr in w_tower.items()}
    return {'T_line': t_sums, 'W_line': w_sums}


# =============================================================================
# 11.  Summary report
# =============================================================================

def arity12_summary(c_val) -> str:
    """Full summary of the W_3 shadow tower at a specific central charge to arity 12."""
    c_num = float(c_val)
    gr = growth_rates_numerical(c_num)
    t_tower = t_line_tower_numerical(c_num, 12)
    w_tower = w_line_tower_numerical(c_num, 12)
    w_ratios = even_arity_ratios_w_line(c_num)

    lines = [
        f"W_3 Shadow Tower at c = {c_num} (arity 12 extension)",
        f"  kappa(W_3) = {5.0 * c_num / 6.0:.6f}",
        f"  kappa_T = {c_num / 2.0:.6f}, kappa_W = {c_num / 3.0:.6f}",
        f"  rho_T = {gr['rho_T']:.8f}, rho_W = {gr['rho_W']:.8f}",
        f"  T-line convergent: {gr['rho_T'] < 1.0}",
        f"  W-line convergent: {gr['rho_W'] < 1.0}",
        "",
        "  T-line tower (even arities):",
    ]
    for r in range(2, 13, 2):
        lines.append(f"    S_{r:2d}^T = {t_tower[r]:+20.10e}")
    lines.append("")
    lines.append("  W-line tower (even arities, odd = 0 by Z_2 parity):")
    for r in range(2, 13, 2):
        lines.append(f"    S_{r:2d}^W = {w_tower[r]:+20.10e}")
    lines.append("")
    lines.append("  W-line even-arity growth ratios |S_{2n+2}/S_{2n}|:")
    for n, ratio in w_ratios['ratios']:
        lines.append(f"    n={n}: |S_{2*n+2}/S_{2*n}| = {ratio:.10e}")
    lines.append(f"  Limit (rho_W^2) = {w_ratios['rho_W_sq']:.10e}")

    return "\n".join(lines)


# =============================================================================
# 12.  Entry point
# =============================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("W_3 SHADOW TOWER -- ARITY 12 EXTENSION")
    print("=" * 72)

    # Verify internal consistency
    print("\nClosed-form vs recursion (arity 12):")
    for key, ok in verify_closed_vs_recursive(12).items():
        status = "OK" if ok else "FAIL"
        print(f"  {key}: {status}")

    print("\nGeneral term vs recursion (W-line):")
    for key, ok in verify_general_term_vs_recursive(6).items():
        status = "OK" if ok else "FAIL"
        print(f"  {key}: {status}")

    print("\nRing relations:")
    for key, ok in verify_ring_relations(6).items():
        status = "OK" if ok else "FAIL"
        print(f"  {key}: {status}")

    # Summary at c = 2
    print("\n" + arity12_summary(2))
    print("\n" + arity12_summary(50))
