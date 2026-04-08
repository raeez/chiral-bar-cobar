r"""Shadow arity frontier engine: S_6, S_7, S_8 across the full standard landscape.

CLOSED-FORM RESULTS (Virasoro):

    S_6(c) = 80(45c + 193) / [3 c^3 (5c+22)^2]

    S_7(c) = -2880(15c + 61) / [7 c^4 (5c+22)^2]

    S_8(c) = 80(2025c^2 + 16470c + 33314) / [c^5 (5c+22)^3]

THREE INDEPENDENT DERIVATION PATHS:

    Path 1 (Convolution recursion):
        f(t)^2 = Q_L(t) = c^2 + 12ct + [(180c+872)/(5c+22)]t^2.
        a_0 = c, a_1 = 6, a_n = -(1/2c) sum_{j=1}^{n-1} a_j a_{n-j}.
        S_r = a_{r-2} / r.

    Path 2 (Master equation projection):
        S_r = -(1/(rc)) sum_{3<=j<=k, j+k=r+2} eps(j,k) j k S_j S_k,
        where eps = 1 if j<k, 1/2 if j=k. Initial data: S_2=c/2, S_3=2,
        S_4=10/[c(5c+22)].

    Path 3 (Shadow ODE 3-term recurrence):
        2 Q_L f' = Q_L' f gives the linear recurrence
        2 q_0 (n+1) a_{n+1} = q_1(1-2n) a_n + 2 q_2(2-n) a_{n-1}.

STRUCTURAL THEOREMS:

    Denominator theorem: denom(S_r) = c^{r-3} (5c+22)^{floor((r-2)/2)} times
    a rational constant whose denominator divides r.

    Numerator degree: deg_c(numer(S_r)) = floor((r-4)/2).

    Sign pattern: (-1)^r for r >= 4 at generic c > 0. Phase slips occur at
    large arity for small c (beat period pi/(pi - arg(branch point))).

LANDSCAPE COVERAGE:

    - Virasoro (class M, r_max = infinity): S_6, S_7, S_8 as closed-form
      rational functions of c.
    - Affine sl_2 (class L on Cartan, class M on T-line): S_6, S_7, S_8
      as rational functions of level k via Sugawara substitution c=3k/(k+2).
    - Beta-gamma (class C, r_max = 4): T-line shadow is the Virasoro tower
      at c = 2(6 lam^2 - 6 lam + 1). Global tower terminates at arity 4
      by stratum separation; T-line projection does NOT terminate.
    - Heisenberg (class G, r_max = 2): S_r = 0 for r >= 3.
    - W_3 (class M, 2-channel): full bivariate Sh_r(x_T, x_W) computed
      through arity 8 from the 2D master equation recursion.

References:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    cor:virasoro-quintic-shadow-explicit (w_algebras.tex)
    virasoro_shadow_all_arity.py (canonical computation module)
    w3_full_2d_shadow_tower.py (W_3 bivariate recursion)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union

from sympy import (
    Poly,
    Rational,
    Symbol,
    cancel,
    denom,
    expand,
    factor,
    limit,
    numer,
    oo,
    simplify,
    sqrt,
)

c = Symbol('c')
k = Symbol('k')


# =========================================================================
# 1. Virasoro shadow metric and core data
# =========================================================================

def virasoro_shadow_metric():
    """Q_L(t) = q0 + q1 t + q2 t^2 for Virasoro.

    Q_L = c^2 + 12c t + [(180c+872)/(5c+22)] t^2.
    """
    q0 = c**2
    q1 = 12 * c
    q2 = (180 * c + 872) / (5 * c + 22)
    return q0, q1, q2


def virasoro_kappa():
    """kappa(Vir_c) = c/2."""
    return c / 2


# =========================================================================
# 2. Path 1: Convolution recursion f^2 = Q_L
# =========================================================================

def convolution_coefficients(max_n: int = 20):
    r"""Taylor coefficients a_n of f(t) = sqrt(Q_L(t)) via convolution.

    f^2 = Q_L implies:
        a_0 = c, a_1 = 6,
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3,
        a_2 = (q2 - a_1^2)/(2c).
    """
    q0, q1, q2 = virasoro_shadow_metric()

    a = [None] * (max_n + 1)
    a[0] = c
    if max_n >= 1:
        a[1] = cancel(q1 / (2 * c))  # = 6
    if max_n >= 2:
        a[2] = cancel((q2 - a[1]**2) / (2 * c))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * c))
    return a


def shadow_coefficients_convolution(max_r: int = 20) -> Dict[int, Any]:
    """S_r via convolution: S_r = a_{r-2}/r."""
    a = convolution_coefficients(max_n=max_r - 2)
    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= len(a) - 1 and a[n] is not None:
            result[r] = factor(cancel(a[n] / r))
    return result


# =========================================================================
# 3. Path 2: Master equation recursion
# =========================================================================

def shadow_coefficients_master_eq(max_r: int = 20) -> Dict[int, Any]:
    r"""S_r via the projected MC equation.

    For r >= 5:
        S_r = -(1/(rc)) sum_{3<=j<=k, j+k=r+2} eps(j,k) j k S_j S_k
    where eps = 1 if j < k, 1/2 if j = k.
    Initial data: S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].
    """
    tower = {}
    tower[2] = c / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_r + 1):
        total = Rational(0)
        for j in range(3, r + 1):
            k_val = r + 2 - j
            if k_val < j or k_val < 3:
                continue
            if j not in tower or k_val not in tower:
                continue
            contrib = j * k_val * tower[j] * tower[k_val]
            if j == k_val:
                contrib = contrib / 2
            total += contrib
        tower[r] = cancel(-total / (r * c))

    return tower


# =========================================================================
# 4. Path 3: Shadow ODE 3-term linear recurrence
# =========================================================================

def shadow_coefficients_ode(max_r: int = 20) -> Dict[int, Any]:
    r"""S_r via the shadow ODE 2 Q_L f' = Q_L' f.

    This gives a 3-term linear recurrence for the Taylor coefficients:
        2 q0 (n+1) a_{n+1} = q1 (1-2n) a_n + 2 q2 (2-n) a_{n-1}
    with a_{-1} = 0.  At n = 0 the recurrence gives
    2 q0 a_1 = q1 a_0 + 2 q2 (2) * 0 = q1 a_0, so a_1 = q1 a_0 / (2 q0).
    At n >= 1 we need the a[n-1] term (which is a_0 for n=1), so the
    condition must include n = 1.
    """
    q0, q1, q2 = virasoro_shadow_metric()

    max_n = max_r - 2
    a = [None] * (max_n + 2)
    a[0] = c
    a[1] = cancel(q1 * a[0] / (2 * q0))  # = 6

    for n in range(1, max_n + 1):
        rhs = q1 * (1 - 2 * n) * a[n]
        # At n=1 we need a[0]; at n >= 1 the a[n-1] term is always present.
        rhs += 2 * q2 * (2 - n) * a[n - 1]
        a[n + 1] = cancel(rhs / (2 * q0 * (n + 1)))

    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= len(a) - 1 and a[n] is not None:
            result[r] = factor(cancel(a[n] / r))
    return result


# =========================================================================
# 5. Explicit closed-form formulas
# =========================================================================

def S_explicit(r: int):
    """Explicit closed-form S_r for Virasoro, r = 2, ..., 10."""
    if r == 2:
        return c / 2
    if r == 3:
        return Rational(2)
    if r == 4:
        return Rational(10) / (c * (5 * c + 22))
    if r == 5:
        return Rational(-48) / (c**2 * (5 * c + 22))
    if r == 6:
        return (Rational(80) * (45 * c + 193)
                / (3 * c**3 * (5 * c + 22)**2))
    if r == 7:
        return (Rational(-2880) * (15 * c + 61)
                / (7 * c**4 * (5 * c + 22)**2))
    if r == 8:
        return (Rational(80) * (2025 * c**2 + 16470 * c + 33314)
                / (c**5 * (5 * c + 22)**3))
    if r == 9:
        return (Rational(-1280) * (2025 * c**2 + 15570 * c + 29554)
                / (3 * c**6 * (5 * c + 22)**3))
    if r == 10:
        return (Rational(256) * (91125 * c**3 + 1050975 * c**2
                                 + 3989790 * c + 4969967)
                / (c**7 * (5 * c + 22)**4))
    raise ValueError(f"Explicit formula not implemented for r={r}")


# =========================================================================
# 6. Affine sl_2 shadow tower on the T-line
# =========================================================================

def affine_sl2_central_charge():
    """c(sl_2, k) = 3k/(k+2)."""
    return 3 * k / (k + 2)


def affine_sl2_shadow_coefficient(r: int):
    """S_r for affine sl_2 on the T-line via Sugawara: substitute c=3k/(k+2)."""
    S_vir = S_explicit(r)
    return factor(cancel(S_vir.subs(c, 3 * k / (k + 2))))


def affine_sl2_shadow_tower(max_r: int = 8) -> Dict[int, Any]:
    """Full shadow tower for affine sl_2 on the T-line."""
    return {r: affine_sl2_shadow_coefficient(r) for r in range(2, max_r + 1)}


# =========================================================================
# 7. Beta-gamma shadow data (T-line projection)
# =========================================================================

lam = Symbol('lambda')


def betagamma_central_charge():
    """c(bg, lambda) = 2(6 lambda^2 - 6 lambda + 1)."""
    return 2 * (6 * lam**2 - 6 * lam + 1)


def betagamma_T_line_shadow(r: int):
    """S_r on the T-line of beta-gamma = Virasoro tower at c(bg, lambda).

    The GLOBAL tower terminates at arity 4 by stratum separation,
    but the T-line projection inherits the full Virasoro tower.
    """
    S_vir = S_explicit(r)
    return factor(cancel(S_vir.subs(c, betagamma_central_charge())))


# =========================================================================
# 8. Heisenberg shadow data
# =========================================================================

def heisenberg_shadow_coefficient(r: int, k_val=None):
    """Heisenberg: S_2 = k, S_r = 0 for r >= 3 (class G, abelian)."""
    if r == 2:
        return k if k_val is None else k_val
    return Rational(0)


# =========================================================================
# 9. Denominator pattern analysis
# =========================================================================

def denominator_analysis(max_r: int = 12) -> List[Tuple[int, int, int, bool]]:
    """Verify the denominator theorem: denom(S_r) = c^{r-3} (5c+22)^{floor((r-2)/2)}.

    Returns [(r, pow_c, pow_5c22, matches_prediction)] for r = 4, ..., max_r.
    """
    coeffs = shadow_coefficients_convolution(max_r)
    results = []
    for r in range(4, max_r + 1):
        Sr = cancel(coeffs[r])
        d = denom(Sr)
        d_poly = Poly(d, c)

        pow_c = 0
        rem = d_poly
        while rem.eval(0) == 0:
            pow_c += 1
            rem = Poly(cancel(rem.as_expr() / c), c)

        pow_5c22 = 0
        while rem.eval(Rational(-22, 5)) == 0:
            pow_5c22 += 1
            rem = Poly(cancel(rem.as_expr() / (5 * c + 22)), c)

        pred_c = r - 3
        pred_5c22 = (r - 2) // 2
        results.append((r, pow_c, pow_5c22,
                         pow_c == pred_c and pow_5c22 == pred_5c22))
    return results


def numerator_degree_analysis(max_r: int = 12) -> List[Tuple[int, int, int, bool]]:
    """Verify numerator degree: deg(numer(S_r)) = floor((r-4)/2).

    Returns [(r, actual_deg, predicted_deg, match)] for r = 4, ..., max_r.
    """
    coeffs = shadow_coefficients_convolution(max_r)
    results = []
    for r in range(4, max_r + 1):
        Sr = cancel(coeffs[r])
        n = numer(Sr)
        n_poly = Poly(n, c)
        d = n_poly.total_degree()
        pred = (r - 4) // 2
        results.append((r, d, pred, d == pred))
    return results


# =========================================================================
# 10. Sign pattern and phase analysis
# =========================================================================

def sign_pattern(max_r: int = 20, c_val: float = 1.0) -> List[Tuple[int, int]]:
    """Sign of S_r at a given c value. Expected: (-1)^r for r >= 4."""
    coeffs = shadow_coefficients_convolution(max_r)
    results = []
    for r in range(4, max_r + 1):
        val = float(coeffs[r].subs(c, c_val))
        sgn = 1 if val > 0 else (-1 if val < 0 else 0)
        expected = (-1)**r
        results.append((r, sgn, expected, sgn == expected))
    return results


def branch_point_argument(c_val: float) -> float:
    """Argument (degrees) of the upper-half-plane branch point of Q_L."""
    import cmath
    import math
    q0 = c_val**2
    q1 = 12 * c_val
    q2 = 36 + 80 / (5 * c_val + 22)
    disc = q1**2 - 4 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    root = (-q1 + sqrt_disc) / (2 * q2)
    return math.degrees(cmath.phase(root))


# =========================================================================
# 11. Shadow visibility genus
# =========================================================================

def shadow_visibility_genus(r: int) -> int:
    """g_min(S_r) = floor(r/2) + 1: the first genus at which S_r contributes.

    S_6 first appears at genus 4.
    S_7 first appears at genus 4.
    S_8 first appears at genus 5.
    """
    return r // 2 + 1


# =========================================================================
# 12. Self-duality at c=13
# =========================================================================

def self_duality_check(max_r: int = 10) -> Dict[int, Any]:
    """At c=13, S_r(13) = S_r(26-13) = S_r(13) (tautological self-duality).

    Returns {r: (S_r(13), S_r(13_dual))} where both should be equal.
    """
    coeffs = shadow_coefficients_convolution(max_r)
    results = {}
    for r in range(2, max_r + 1):
        val = coeffs[r].subs(c, 13)
        val_dual = coeffs[r].subs(c, 13)
        results[r] = (cancel(val), cancel(val_dual), cancel(val - val_dual) == 0)
    return results


def koszul_dual_ratio(r: int):
    """S_r(c) / S_r(26-c): the Koszul duality ratio."""
    Sr = S_explicit(r)
    Sr_dual = Sr.subs(c, 26 - c)
    return factor(cancel(Sr / Sr_dual))


# =========================================================================
# 13. Numerical evaluation at special central charges
# =========================================================================

SPECIAL_CENTRAL_CHARGES = {
    'ising': Rational(1, 2),
    'free_boson': Rational(1),
    'tricritical_ising': Rational(7, 10),
    'yang_lee': Rational(-22, 5),
    'self_dual': Rational(13),
    'near_critical': Rational(25),
    'critical_string': Rational(26),
}


def evaluate_landscape(max_r: int = 8) -> Dict[str, Dict[int, float]]:
    """Evaluate S_r across the standard Virasoro landscape."""
    coeffs = shadow_coefficients_convolution(max_r)
    results = {}
    for name, c_val in SPECIAL_CENTRAL_CHARGES.items():
        if c_val == 0 or (5 * c_val + 22) == 0:
            continue
        row = {}
        for r in range(2, max_r + 1):
            row[r] = float(coeffs[r].subs(c, c_val))
        results[name] = row
    return results


# =========================================================================
# 14. General single-line shadow tower (parametric)
# =========================================================================

def general_shadow_metric(kappa_val, alpha_val, S4_val):
    r"""Q_L(t) = (2 kappa + 3 alpha t)^2 + 2 Delta t^2 for general data.

    Delta = 8 kappa S_4. Returns (q0, q1, q2).
    """
    Delta = 8 * kappa_val * S4_val
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta
    return q0, q1, q2


def general_convolution(kappa_val, alpha_val, S4_val,
                        max_n: int = 20):
    """Convolution recursion for a general single-line shadow tower.

    Returns list of Taylor coefficients [a_0, ..., a_{max_n}].
    """
    q0, q1, q2 = general_shadow_metric(kappa_val, alpha_val, S4_val)

    a = [None] * (max_n + 1)
    a[0] = 2 * kappa_val  # sqrt(q0) for positive kappa
    if max_n >= 1:
        a[1] = cancel(q1 / (2 * a[0]))
    if max_n >= 2:
        a[2] = cancel((q2 - a[1]**2) / (2 * a[0]))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * a[0]))
    return a


def general_shadow_coefficients(kappa_val, alpha_val, S4_val,
                                max_r: int = 10) -> Dict[int, Any]:
    """Shadow coefficients for a general single-line tower.

    S_r = a_{r-2}/r where a_n are the Taylor coefficients of sqrt(Q_L).
    """
    a = general_convolution(kappa_val, alpha_val, S4_val,
                            max_n=max_r - 2)
    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= len(a) - 1 and a[n] is not None:
            result[r] = cancel(a[n] / r)
    return result


# =========================================================================
# 15. Fraction-based evaluation for exact arithmetic
# =========================================================================

def virasoro_S_fraction(r: int, c_val: Union[int, Fraction]) -> Fraction:
    """Evaluate S_r(Vir) at an exact rational c value using Fraction arithmetic."""
    c_f = Fraction(c_val) if isinstance(c_val, int) else c_val
    if c_f == 0:
        raise ValueError("c=0 is a pole of S_r for r >= 4")
    if 5 * c_f + 22 == 0:
        raise ValueError("c=-22/5 is a pole of S_r for r >= 4")
    return Fraction(S_explicit(r).subs(c, c_f))


def affine_sl2_S_fraction(r: int, k_val: Union[int, Fraction]) -> Fraction:
    """Evaluate S_r(sl_2, k) at an exact rational level."""
    k_f = Fraction(k_val) if isinstance(k_val, int) else k_val
    c_f = Fraction(3) * k_f / (k_f + 2)
    return virasoro_S_fraction(r, c_f)
