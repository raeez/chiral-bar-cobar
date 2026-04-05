r"""W_3 shadow obstruction tower: closed-form coefficients S_3 through S_8 on both primary lines.

The W_3 algebra has two generators:
    T (stress tensor, conformal weight 2)
    W (spin-3 current, conformal weight 3)

The shadow obstruction tower lives on the 2-dimensional deformation space
spanned by (eta_T, eta_W).  On each 1-dimensional primary line the
Riccati algebraicity theorem (thm:riccati-algebraicity) applies:
the generating function H(t) = t^2 sqrt(Q_L(t)) is algebraic of degree 2.

TWO PRIMARY LINES:

    T-line (x_W = 0):
        kappa_T = c/2,  alpha_T = S_3 = 2,  S_4 = 10/[c(5c+22)].
        Shadow metric: Q_T(t) = c^2 + 12c t + 4(45c+218)/(5c+22) t^2.
        Discriminant: Delta_T = 40/(5c+22).
        Growth rate: rho_T^2 = 4(45c+218)/[c^2(5c+22)] (= Virasoro).
        Depth class: M (infinite tower, Delta != 0).

    W-line (x_T = 0):
        kappa_W = c/3,  alpha_W = 0 (Z_2 parity),  S_4 = 2560/[c(5c+22)^3].
        Shadow metric: Q_W(w) = 4c^2/9 + 40960/[3(5c+22)^3] w^2.
        Discriminant: Delta_W = 20480/[3(5c+22)^3].
        Growth rate: rho_W^2 = 30720/[c^2(5c+22)^3].
        Depth class: M (infinite tower, but only even arities by parity).

All coefficients are independently computed from the convolution recursion
    a_0 = sqrt(q_0),  a_1 = q_1/(2a_0),  a_2 = (q_2 - a_1^2)/(2a_0),
    a_n = -(1/(2a_0)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3,
and then S_r = a_{r-2} / r.  Results verified against the manuscript table
in comp:w-infty-shadow-tower (w_algebras_deep.tex).

T-line tower (closed forms in c):
    S_2 = c/2
    S_3 = 2
    S_4 = 10 / [c(5c+22)]
    S_5 = -48 / [c^2(5c+22)]
    S_6 = 80(45c+193) / [3 c^3 (5c+22)^2]
    S_7 = -2880(15c+61) / [7 c^4 (5c+22)^2]
    S_8 = 80(2025c^2+16470c+33314) / [c^5 (5c+22)^3]

W-line tower (closed forms in c, odd arities vanish):
    S_2 = c/3
    S_3 = 0
    S_4 = 2560 / [c(5c+22)^3]
    S_5 = 0
    S_6 = -13107200 / [c^3 (5c+22)^6]
    S_7 = 0
    S_8 = 150994944000 / [c^5 (5c+22)^9]

W-line ring structure: S_6 = -2 S_4^2 / c,  S_8 = 9 S_4^3 / c^2.
General W-line closed form:
    S_{2n} = (-1)^n a_n 2560^{n-1} / [c^{2n-3} (5c+22)^{3(n-1)}]
    with a_n = (-12)^n / 54 * binomial(3/2, n).

Manuscript references:
    comp:w-infty-shadow-tower (w_algebras_deep.tex)
    eq:w3-wline-closed-form (w_algebras_deep.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from typing import Any, Dict, Optional

from sympy import (
    Integer,
    N as Neval,
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
# 1.  Shadow data (inputs from OPE)
# =============================================================================

def t_line_data():
    """Shadow data for the T-line (x_W = 0): identical to Virasoro.

    Returns dict with keys: kappa, alpha, S4, Delta, q0, q1, q2, rho_sq.
    """
    kappa = c / 2
    alpha = Integer(2)
    S4 = Rational(10) / (c * (5 * c + 22))
    Delta = 8 * kappa * S4                            # 40/(5c+22)
    q0 = 4 * kappa ** 2                               # c^2
    q1 = 12 * kappa * alpha                           # 12c
    q2 = 9 * alpha ** 2 + 16 * kappa * S4             # 4(45c+218)/(5c+22)
    rho_sq = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2)
    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': cancel(Delta),
        'q0': q0,
        'q1': q1,
        'q2': cancel(q2),
        'rho_sq': cancel(rho_sq),
    }


def w_line_data():
    """Shadow data for the W-line (x_T = 0).

    Z_2 parity (W -> -W) forces alpha_W = 0 and kills all odd arities.

    Returns dict with keys: kappa, alpha, S4, Delta, q0, q1, q2, rho_sq.
    """
    kappa = c / 3
    alpha = Integer(0)
    S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
    Delta = 8 * kappa * S4                            # 20480/[3(5c+22)^3]
    q0 = 4 * kappa ** 2                               # 4c^2/9
    q1 = Integer(0)
    q2 = 16 * kappa * S4                              # 40960/[3(5c+22)^3]
    rho_sq = 2 * Delta / (4 * kappa ** 2)             # 30720/[c^2(5c+22)^3]
    return {
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': cancel(Delta),
        'q0': cancel(q0),
        'q1': q1,
        'q2': cancel(q2),
        'rho_sq': cancel(rho_sq),
    }


# =============================================================================
# 2.  Convolution recursion: Taylor coefficients of sqrt(Q_L)
# =============================================================================

def _sqrt_quadratic_taylor_exact(q0, q1, q2, max_n):
    r"""Taylor coefficients [t^n] sqrt(q0 + q1 t + q2 t^2).

    Recursion from f^2 = Q_L:
        a_0 = sqrt(q0)
        a_1 = q_1 / (2 a_0)
        a_2 = (q_2 - a_1^2) / (2 a_0)
        a_n = -(1/(2 a_0)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3
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
    """Float-precision version for speed at large arity."""
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
# 3.  Exact symbolic towers (main entry points)
# =============================================================================

def t_line_tower_exact(max_r=10):
    r"""Exact T-line shadow obstruction tower {S_r^T : r = 2, ..., max_r} as functions of c.

    Identical to the Virasoro shadow obstruction tower.
    The symbol c is declared positive so that sqrt(c^2) = c.
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


def w_line_tower_exact(max_r=14):
    r"""Exact W-line shadow obstruction tower {S_r^W : r = 2, ..., max_r} as functions of c.

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

def t_line_tower_numerical(c_val, max_r=30):
    """Numerical T-line shadow obstruction tower at a given central charge."""
    c_num = float(c_val)
    kappa = c_num / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_num * (5.0 * c_num + 22.0))
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    a = _sqrt_quadratic_taylor_float(q0, q1, q2, max_r - 2)
    return {n + 2: a[n] / (n + 2) for n in range(len(a))}


def w_line_tower_numerical(c_val, max_r=30):
    """Numerical W-line shadow obstruction tower at a given central charge."""
    c_num = float(c_val)
    kappa_W = c_num / 3.0
    S4_W = 2560.0 / (c_num * (5.0 * c_num + 22.0) ** 3)
    q0 = 4.0 * kappa_W ** 2
    q1 = 0.0
    q2 = 16.0 * kappa_W * S4_W
    a = _sqrt_quadratic_taylor_float(q0, q1, q2, max_r - 2)
    return {n + 2: a[n] / (n + 2) for n in range(len(a))}


# =============================================================================
# 5.  Hardcoded closed forms (independently verified)
# =============================================================================

def t_line_closed_forms():
    r"""Return S_3 through S_8 on the T-line as factored rational functions of c.

    Each coefficient is independently computed from the convolution recursion
    and cross-checked against the manuscript table in comp:w-infty-shadow-tower.
    The T-line is identical to the Virasoro shadow obstruction tower.
    """
    return {
        2: c / 2,
        3: Integer(2),
        4: Rational(10) / (c * (5 * c + 22)),
        5: Rational(-48) / (c ** 2 * (5 * c + 22)),
        6: Rational(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2),
        7: Rational(-2880) * (15 * c + 61) / (7 * c ** 4 * (5 * c + 22) ** 2),
        8: Rational(80) * (2025 * c ** 2 + 16470 * c + 33314)
           / (c ** 5 * (5 * c + 22) ** 3),
    }


def w_line_closed_forms():
    r"""Return S_2 through S_8 on the W-line as rational functions of c.

    Odd arities vanish by Z_2 parity (W -> -W).
    Even arities satisfy the ring relation S_{2n} = ring product in S_4/c.
    """
    return {
        2: c / 3,
        3: Integer(0),
        4: Rational(2560) / (c * (5 * c + 22) ** 3),
        5: Integer(0),
        6: Rational(-13107200) / (c ** 3 * (5 * c + 22) ** 6),
        7: Integer(0),
        8: Rational(150994944000) / (c ** 5 * (5 * c + 22) ** 9),
    }


def w_line_general_term(n):
    r"""Closed-form S_{2n} on the W-line for any n >= 1.

    S_{2n}^{W-line} = (-1)^n  a_n  2560^{n-1} / [c^{2n-3} (5c+22)^{3(n-1)}]
    where a_n = (-12)^n / 54 * binomial(3/2, n).

    Generating function: sum_{n>=2} a_n x^n = x/3 + ((1-12x)^{3/2} - 1)/54.

    This follows from the algebraicity of H(w) = w^2 sqrt(Q_W(w)):
    the shadow metric Q_W(w) = 4c^2/9 + 40960/[3(5c+22)^3] w^2 has
    sqrt(Q_W) expressible via (1-12x)^{3/2} after the substitution
    x = -2560 w^2 / [c^2 (5c+22)^3].
    """
    a_n = Rational((-12) ** n, 54) * binomial(Rational(3, 2), n)
    if n == 1:
        return c / 3
    return (-1) ** n * a_n * 2560 ** (n - 1) / (c ** (2 * n - 3) * (5 * c + 22) ** (3 * (n - 1)))


# =============================================================================
# 6.  W-line ring structure
# =============================================================================

def w_line_ring_relations():
    r"""Verify the ring structure S_{2n} = polynomial in S_4 and 1/c.

    From the manuscript (eq:w3-wline-closed-form):
        S_6 = -2 S_4^2 / c
        S_8 = 9 S_4^3 / c^2
        S_{10} = -54 S_4^4 / c^3    (since a_5 = 54)
        S_{12} = 378 S_4^5 / c^4    (since a_6 = 378)

    General: S_{2n} = (-1)^{n} a_n S_4^{n-1} / c^{n-2}
    where a_n = |(-12)^n / 54 * binom(3/2, n)|.
    """
    S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
    wl = w_line_closed_forms()
    relations = {}
    # S_6 = -2 S_4^2 / c
    S6_from_ring = -2 * S4 ** 2 / c
    relations['S6_ring'] = simplify(wl[6] - S6_from_ring) == 0
    # S_8 = 9 S_4^3 / c^2
    S8_from_ring = 9 * S4 ** 3 / c ** 2
    relations['S8_ring'] = simplify(wl[8] - S8_from_ring) == 0
    return relations


# =============================================================================
# 7.  Discriminants, growth rates, and critical central charges
# =============================================================================

def discriminants():
    """Discriminants for both primary lines.

    Delta = 8 kappa S_4 controls the depth class:
        Delta != 0  =>  class M (infinite tower)
        Delta = 0   =>  class G or L (finite tower)
    """
    return {
        'T_line': Rational(40) / (5 * c + 22),
        'W_line': Rational(20480) / (3 * (5 * c + 22) ** 3),
    }


def growth_rates_squared():
    """Squared growth rates rho^2 for both primary lines.

    rho^2 = (9 alpha^2 + 2 Delta) / (4 kappa^2).
    """
    return {
        'T_line': 4 * (45 * c + 218) / (c ** 2 * (5 * c + 22)),
        'W_line': Rational(30720) / (c ** 2 * (5 * c + 22) ** 3),
    }


def growth_rates_numerical(c_val):
    """Numerical growth rates rho_T and rho_W at a given central charge."""
    c_num = float(c_val)
    rho_T_sq = 4.0 * (45.0 * c_num + 218.0) / (c_num ** 2 * (5.0 * c_num + 22.0))
    rho_W_sq = 30720.0 / (c_num ** 2 * (5.0 * c_num + 22.0) ** 3)
    return {
        'rho_T': math.sqrt(abs(rho_T_sq)),
        'rho_W': math.sqrt(abs(rho_W_sq)),
    }


# =============================================================================
# 8.  Koszul duality (c <-> 100 - c)
# =============================================================================

def koszul_dual_central_charge():
    """W_3 Koszul duality: c -> 100 - c.

    kappa(c) + kappa(100-c) = 5c/6 + 5(100-c)/6 = 250/3.
    """
    return 100 - c


def complementarity_sums(max_r=8):
    """Complementarity sums S_r(c) + S_r(100-c) on both lines."""
    K = 100
    t_tower = t_line_tower_exact(max_r)
    w_tower = w_line_tower_exact(max_r)
    t_sums = {r: cancel(Sr + Sr.subs(c, K - c)) for r, Sr in t_tower.items()}
    w_sums = {r: cancel(Sr + Sr.subs(c, K - c)) for r, Sr in w_tower.items()}
    return {'T_line': t_sums, 'W_line': w_sums}


# =============================================================================
# 9.  Cross-consistency checks
# =============================================================================

def verify_closed_vs_recursive(max_r=8):
    """Verify that hardcoded closed forms match the convolution recursion.

    This is the primary self-consistency check.  Any discrepancy
    would indicate either a typo in the closed forms or a bug
    in the recursion.
    """
    t_rec = t_line_tower_exact(max_r)
    t_closed = t_line_closed_forms()
    w_rec = w_line_tower_exact(max_r)
    w_closed = w_line_closed_forms()

    results = {}
    for r in range(2, max_r + 1):
        if r in t_closed:
            diff_t = simplify(t_rec[r] - t_closed[r])
            results[f'T_line_S{r}'] = diff_t == 0
        if r in w_closed:
            diff_w = simplify(w_rec[r] - w_closed[r])
            results[f'W_line_S{r}'] = diff_w == 0
    return results


def verify_numerical_vs_exact(c_val=25, max_r=8, tol=1e-10):
    """Verify numerical tower matches exact evaluation at a given c."""
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
