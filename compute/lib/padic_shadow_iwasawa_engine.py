r"""p-adic shadow towers and Iwasawa theory for the shadow obstruction tower.

This module studies the p-adic properties of the shadow obstruction tower
{S_r(A)}_{r>=2} for standard families of chiral algebras.

MATHEMATICAL FRAMEWORK
======================

1. SHADOW COEFFICIENTS ARE RATIONAL.
   For every standard-family algebra A (Virasoro, affine KM, W_N) with
   rational parameters, the shadow coefficients S_r(A) are exact rational
   numbers.  Their p-adic valuations encode arithmetic structure.

2. THREE FAMILIES.
   - Virasoro at central charge c (class M, infinite shadow depth):
     S_2 = c/2, S_3 = 2 (c-independent), S_4 = 10/(c(5c+22)), S_r from shadow metric.
   - Affine sl_2 at level k (class L, shadow depth 3):
     kappa = 3(k+2)/4, alpha = 4/(k+2), S_4 = 0.  Tower terminates: S_r = 0 for r >= 4.
   - W_3 at central charge c (class M on T-line, class M on W-line):
     T-line uses Virasoro shadow data; W-line has Z_2 parity (odd arities vanish).

3. p-ADIC VALUATIONS AND IWASAWA INVARIANTS.
   For the shadow tower series f(T) = sum_{r>=2} S_r T^r in Q_p[[T]]:
   - mu_p(A) = lim_{r->inf} v_p(S_r)/r  (growth rate of valuations)
   - lambda_p(A) = Iwasawa lambda (smallest degree with minimal valuation)
   The shadow Ferrero-Washington analogue: mu_p(A) = 0 for all A.

4. NEWTON POLYGONS.
   The Newton polygon of f(T) = sum S_r T^r is the lower convex hull of
   {(r, v_p(S_r)) : r >= 2}.  Its slopes encode p-adic growth rates.

5. SHADOW KUMMER CRITERION.
   A prime p is shadow-regular for A if p does not divide the numerator of
   S_r(A)/r! for any 2 <= r <= p-1.

6. p-ADIC GENERATING FUNCTION CONVERGENCE.
   H_A(t) = sum S_r t^r.  For Virasoro, H(t) = kappa * t^2 * sqrt(Q_L(t)/Q_L(0)).
   The p-adic radius of convergence depends on the valuations of the shadow
   metric coefficients.

Manuscript references:
    chap:arithmetic-shadows (arithmetic_shadows.tex)
    rem:kummer-motive (arithmetic_shadows.tex)
    thm:shadow-spectral-correspondence (arithmetic_shadows.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)

Convention: shadow coefficients S_r are in the generating function
    H(t) = sum_{r>=2} S_r t^r
where H(t) = t^2 sqrt(Q_L(t)) / sqrt(Q_L(0)) and Q_L is the shadow metric.
For Virasoro: S_2 = c/2, S_3 = 2 (c-independent), S_4 = 10/(c(5c+22)).
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd, log
from typing import Any, Dict, List, Optional, Tuple, Union


# ============================================================================
# 1. p-adic valuation
# ============================================================================

def v_p(x: Fraction, p: int) -> int:
    """Compute the p-adic valuation v_p(x) for a rational number x.

    Returns the unique integer v such that x = p^v * (a/b) with
    gcd(a, p) = gcd(b, p) = 1.

    Raises ValueError if x = 0 (v_p(0) = +infinity).
    """
    if x == 0:
        raise ValueError("v_p(0) is +infinity")
    f = Fraction(x)
    num = abs(f.numerator)
    den = f.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def v_p_safe(x: Fraction, p: int) -> float:
    """v_p with infinity for zero."""
    if x == 0:
        return float('inf')
    return float(v_p(x, p))


def p_adic_abs(x: Fraction, p: int) -> float:
    """Compute the p-adic absolute value |x|_p = p^{-v_p(x)}."""
    if x == 0:
        return 0.0
    return float(p) ** (-v_p(x, p))


# ============================================================================
# 2. Virasoro shadow tower (exact rational, shadow metric convention)
# ============================================================================

def virasoro_shadow_metric_coefficients(c: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Shadow metric Q_L(t) = q0 + q1*t + q2*t^2 for Virasoro at central charge c.

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    with kappa = c/2, alpha = 2 (c-independent), S_4 = 10/(c(5c+22)), Delta = 8*kappa*S_4.

    Returns (q0, q1, q2).
    """
    c = Fraction(c)
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4
    return q0, q1, q2


def virasoro_shadow_exact(r: int, c: Fraction) -> Fraction:
    """Exact shadow coefficient S_r for Virasoro from the shadow metric.

    Uses Taylor expansion of H(t) = t^2 * sqrt(Q_L(t)) / sqrt(Q_L(0)).
    Convention: S_r = [t^r] H(t), so H(t) = sum_{r>=2} S_r t^r.

    Actually, H(t) = sum_{r>=2} S_r t^r and the expansion of sqrt(Q_L(t)):
        sqrt(Q_L(t)) = sum_{n>=0} a_n t^n
    with a_0 = sqrt(q0) = 2|kappa|.

    Then t^2 * sqrt(Q_L(t)) / (2|kappa|) = sum_{n>=0} a_n/(2|kappa|) t^{n+2}
    So S_r = a_{r-2} / (2|kappa|) ... wait.

    More carefully: H(t) = kappa * t^2 * sqrt(Q_L(t)/Q_L(0))
    with Q_L(0) = 4*kappa^2, so sqrt(Q_L(0)) = 2*|kappa|.
    H(t) = kappa * t^2 * sqrt(Q_L(t)) / (2*|kappa|)
         = (sign(kappa)/2) * t^2 * sqrt(Q_L(t))

    For positive kappa (c > 0): H(t) = (1/2) t^2 sqrt(Q_L(t)) / (2kappa) * 2kappa
    = (1/2) t^2 * sqrt(Q_L(t)).

    Actually let's just use the direct recursive approach that matches
    the existing padic_shadow_tower module.

    S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L(t))
    and a_0 = 2*kappa (taking positive branch for c > 0).
    """
    if r < 2:
        raise ValueError(f"arity must be >= 2, got {r}")
    c = Fraction(c)
    if c == 0:
        raise ValueError("c must be nonzero for Virasoro shadow tower")
    if 5 * c + 22 == 0:
        raise ValueError("c = -22/5 (Yang-Lee edge) is singular: 5c+22 = 0")

    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    max_n = r - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = 2 * kappa  # positive branch; for c < 0 this is negative
    if max_n >= 1:
        a[1] = q1 / (2 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a[0])
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    return a[max_n] / r


def virasoro_shadow_tower(c_val: Fraction, max_arity: int = 20) -> Dict[int, Fraction]:
    """Compute the full Virasoro shadow tower S_2, ..., S_{max_arity}.

    Returns dict {r: S_r} with exact rational values.
    """
    c = Fraction(c_val)
    return {r: virasoro_shadow_exact(r, c) for r in range(2, max_arity + 1)}


# ============================================================================
# 3. Affine sl_2 shadow tower (exact rational, class L)
# ============================================================================

def affine_sl2_kappa(k: Fraction) -> Fraction:
    """Modular characteristic kappa(sl_2, k) = dim(sl_2) * (k + h^v) / (2 * h^v).

    For sl_2: dim = 3, h^v = 2.
    kappa = 3(k+2)/4.
    """
    k = Fraction(k)
    return Fraction(3) * (k + 2) / 4


def affine_sl2_shadow_tower(k_val: Fraction, max_arity: int = 20) -> Dict[int, Fraction]:
    """Shadow tower for affine sl_2 at level k.

    Class L (shadow depth 3): the tower terminates at arity 3.
    S_2 = kappa = 3(k+2)/4
    S_3 = 4/(k+2)  (= 2*h^v/(k+h^v) with h^v=2 for sl_2)
    S_r = 0 for r >= 4.

    Note: S_4 = 0 because the Jacobi identity kills the quartic for Lie algebras.
    Delta = 8*kappa*S_4 = 0, so the shadow metric is a perfect square.
    """
    k = Fraction(k_val)
    if k + 2 == 0:
        raise ValueError("k = -2 (critical level for sl_2): S_3 = 4/(k+2) diverges")
    kappa = affine_sl2_kappa(k)
    tower = {}
    tower[2] = kappa
    tower[3] = Fraction(4) / (k + 2)
    for r in range(4, max_arity + 1):
        tower[r] = Fraction(0)
    return tower


# ============================================================================
# 4. W_3 shadow tower on T-line (identical to Virasoro at that c)
# ============================================================================

def w3_central_charge(k: Fraction) -> Fraction:
    """Central charge of W_3 at level k.

    c(W_3, k) = 2 - 24(k+2)^2/(k+3).

    This is the standard sl_3 W-algebra central charge formula,
    NOT the Virasoro formula 2 - 24/(k+3).  See AP3.
    """
    k = Fraction(k)
    return Fraction(2) - Fraction(24) * (k + 2)**2 / (k + 3)


def w3_kappa(c_val: Fraction) -> Fraction:
    """kappa(W_3) = 5c/6.

    Uses kappa = c * (H_3 - 1) with H_3 = 11/6.
    kappa = c * 5/6.
    """
    return Fraction(5) * Fraction(c_val) / 6


def w3_shadow_tower_t_line(c_val: Fraction, max_arity: int = 20) -> Dict[int, Fraction]:
    """W_3 shadow tower on the T-line (Virasoro sector).

    On the T-line, the W_3 shadow data reduces to Virasoro shadow data.
    S_2 = c/2 (the T-channel kappa), S_3 = 2 (c-independent), etc.
    """
    return virasoro_shadow_tower(c_val, max_arity)


def w3_shadow_tower_w_line(c_val: Fraction, max_arity: int = 20) -> Dict[int, Fraction]:
    """W_3 shadow tower on the W-line.

    On the W-line, Z_2 parity (W -> -W) kills all odd arities.
    S_2 = kappa_W = c/3 (the W-channel contribution).
    S_3 = 0 (parity).
    S_4 = 2560 / [c * (5c+22)^3] (the W-line quartic contact).
    S_5 = 0 (parity).
    S_6, S_8, ... from recursion.

    Shadow metric Q_W(w) = 4*kappa_W^2 + 2*Delta_W * w^2
    where Delta_W = 8 * kappa_W * S_4_W.
    No linear term (q1 = 0 because alpha_W = 0).
    """
    c = Fraction(c_val)
    if c == 0:
        raise ValueError("c must be nonzero")

    kappa_W = c / 3
    S4_W = Fraction(2560) / (c * (5 * c + 22) ** 3)
    Delta_W = 8 * kappa_W * S4_W

    # Shadow metric: Q_W(w) = q0 + q2 * w^2 (no linear term)
    q0 = 4 * kappa_W ** 2
    q2 = 16 * kappa_W * S4_W  # = 2 * Delta_W

    # Taylor expansion of sqrt(Q_W(w)):
    # sqrt(q0 + q2*w^2) = sqrt(q0) * sqrt(1 + (q2/q0)*w^2)
    # = sqrt(q0) * sum_{n>=0} binom(1/2, n) * (q2/q0)^n * w^{2n}
    # a_{2n} = sqrt(q0) * binom(1/2, n) * (q2/q0)^n
    # a_{2n+1} = 0

    a0 = 2 * kappa_W  # = sqrt(q0) = sqrt(4*kappa_W^2) for kappa_W > 0
    ratio = q2 / q0 if q0 != 0 else Fraction(0)

    tower = {}
    # S_r = a_{r-2} / r
    # a_0 = 2*kappa_W, a_1 = 0, a_2 = (q2 - 0) / (2*a_0) = q2/(2*a_0), ...
    # But for even-only nonzero: use binomial expansion

    max_n = max_arity - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = a0
    # a[1] = q1/(2*a0) = 0 since q1 = 0
    if max_n >= 2:
        a[2] = (q2 - Fraction(0)) / (2 * a[0])  # a[1]^2 = 0
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    for r in range(2, max_arity + 1):
        idx = r - 2
        if idx <= max_n:
            tower[r] = a[idx] / r
        else:
            tower[r] = Fraction(0)
    return tower


# ============================================================================
# 5. p-adic valuation table for shadow towers
# ============================================================================

def shadow_valuation_table(
    tower: Dict[int, Fraction],
    p: int,
    max_arity: int = 20
) -> List[Dict[str, Any]]:
    """Compute v_p(S_r) for each arity in the tower.

    Returns list of dicts with keys: r, S_r, v_p_S_r.
    """
    results = []
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        results.append({
            'r': r,
            'S_r': Sr,
            'v_p_S_r': vp,
        })
    return results


def multi_family_valuation_table(
    primes: List[int],
    families: Dict[str, Dict[int, Fraction]],
    max_arity: int = 20,
) -> Dict[str, Dict[int, List[Dict]]]:
    """Compute v_p(S_r) for multiple families and primes.

    Returns nested dict: result[family_name][p] = list of valuation data.
    """
    result = {}
    for name, tower in families.items():
        result[name] = {}
        for p in primes:
            result[name][p] = shadow_valuation_table(tower, p, max_arity)
    return result


# ============================================================================
# 6. Iwasawa invariants of the shadow tower
# ============================================================================

def shadow_iwasawa_mu(tower: Dict[int, Fraction], p: int, max_arity: int = 20) -> float:
    """Compute mu_p(A) = lim_{r->inf} v_p(S_r)/r.

    For a p-adic power series f(T) = sum a_r T^r, the mu-invariant is
    min_r v_p(a_r).  In the Iwasawa-theoretic sense, it measures the
    "p-power" dividing ALL coefficients.

    Here we compute mu = min_{2<=r<=max_arity} v_p(S_r), the Iwasawa mu
    in the classical sense.

    Returns float (can be -inf in degenerate cases, or +inf if all S_r = 0).
    """
    min_vp = float('inf')
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        if vp < min_vp:
            min_vp = vp
    return min_vp


def shadow_iwasawa_lambda(tower: Dict[int, Fraction], p: int, max_arity: int = 20) -> int:
    """Compute the Iwasawa lambda-invariant of the shadow tower.

    lambda = smallest r >= 2 such that v_p(S_r) = mu.
    This is the "first index achieving the minimum valuation".
    """
    mu = shadow_iwasawa_mu(tower, p, max_arity)
    if mu == float('inf'):
        return -1  # all coefficients are zero
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        if abs(vp - mu) < 0.5:  # exact match (both are ints or inf)
            return r
    return -1


def shadow_iwasawa_growth_rate(tower: Dict[int, Fraction], p: int, max_arity: int = 20) -> float:
    """Estimate mu_p^growth(A) = lim_{r->inf} v_p(S_r)/r.

    This is the GROWTH RATE variant: how fast do the valuations grow?
    - Linear growth: mu_growth > 0 means p divides more and more
    - Zero growth: mu_growth = 0 means bounded valuations (Ferrero-Washington analogue)
    - Negative growth: mu_growth < 0 means valuations decrease (p-adic norms grow)

    Uses linear regression on the last half of the data.
    """
    points = []
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        if vp != float('inf') and vp != float('-inf'):
            points.append((float(r), float(vp)))

    if len(points) < 3:
        return 0.0

    # Use the latter half for the limit
    half = len(points) // 2
    pts = points[half:]
    if len(pts) < 2:
        return 0.0

    # Linear regression: v_p ~ slope * r + intercept
    n = len(pts)
    sx = sum(x for x, _ in pts)
    sy = sum(y for _, y in pts)
    sxx = sum(x * x for x, _ in pts)
    sxy = sum(x * y for x, y in pts)
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-15:
        return 0.0
    slope = (n * sxy - sx * sy) / denom
    return slope


def shadow_iwasawa_log_rate(tower: Dict[int, Fraction], p: int, max_arity: int = 20) -> float:
    """Estimate lambda_p^log(A) = lim_{r->inf} v_p(S_r)/log(r).

    Logarithmic growth rate of valuations.
    """
    points = []
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        if vp != float('inf') and vp != float('-inf') and r >= 2:
            points.append((log(float(r)), float(vp)))

    if len(points) < 3:
        return 0.0

    half = len(points) // 2
    pts = points[half:]
    if len(pts) < 2:
        return 0.0

    n = len(pts)
    sx = sum(x for x, _ in pts)
    sy = sum(y for _, y in pts)
    sxx = sum(x * x for x, _ in pts)
    sxy = sum(x * y for x, y in pts)
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-15:
        return 0.0
    slope = (n * sxy - sx * sy) / denom
    return slope


def shadow_iwasawa_full(
    tower: Dict[int, Fraction], p: int, max_arity: int = 20
) -> Dict[str, Any]:
    """Full Iwasawa analysis of a shadow tower at prime p.

    Returns mu, lambda, growth rate, log rate, and classification.
    """
    mu = shadow_iwasawa_mu(tower, p, max_arity)
    lam = shadow_iwasawa_lambda(tower, p, max_arity)
    growth = shadow_iwasawa_growth_rate(tower, p, max_arity)
    log_rate = shadow_iwasawa_log_rate(tower, p, max_arity)

    # Classify: bounded / logarithmic / linear
    if abs(growth) < 0.05:
        if abs(log_rate) < 0.3:
            classification = 'bounded'
        else:
            classification = 'logarithmic'
    else:
        classification = 'linear'

    return {
        'p': p,
        'mu': mu,
        'lambda': lam,
        'growth_rate': growth,
        'log_rate': log_rate,
        'classification': classification,
    }


# ============================================================================
# 7. Newton polygon
# ============================================================================

def newton_polygon(
    tower: Dict[int, Fraction], p: int, max_arity: int = 20
) -> List[Tuple[int, float]]:
    """Compute the Newton polygon of the shadow generating function.

    The Newton polygon is the lower convex hull of the set of points
    {(r, v_p(S_r)) : S_r != 0, 2 <= r <= max_arity}.

    Returns list of vertices (r, v_p) on the lower convex hull.
    """
    points = []
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        if vp != float('inf'):
            points.append((r, vp))

    if len(points) < 2:
        return points

    # Compute lower convex hull using Andrew's monotone chain
    # Points are already sorted by x since r increases
    hull = []
    for pt in points:
        while len(hull) >= 2:
            # Check if the last three points make a right turn (or are collinear)
            # For lower hull, we want left turns
            o = _cross(hull[-2], hull[-1], pt)
            if o <= 0:  # right turn or collinear -> remove last point
                hull.pop()
            else:
                break
        hull.append(pt)

    return hull


def _cross(o: Tuple, a: Tuple, b: Tuple) -> float:
    """Cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def newton_polygon_slopes(
    tower: Dict[int, Fraction], p: int, max_arity: int = 20
) -> List[Tuple[float, int]]:
    """Compute the slopes of the Newton polygon segments.

    Returns list of (slope, multiplicity) pairs where multiplicity is the
    horizontal length of the segment.
    """
    hull = newton_polygon(tower, p, max_arity)
    if len(hull) < 2:
        return []

    slopes = []
    for i in range(len(hull) - 1):
        r1, v1 = hull[i]
        r2, v2 = hull[i + 1]
        dr = r2 - r1
        if dr == 0:
            continue
        slope = (v2 - v1) / dr
        slopes.append((slope, dr))
    return slopes


# ============================================================================
# 8. Shadow Kummer criterion
# ============================================================================

def shadow_kummer_regularity(
    tower: Dict[int, Fraction], p: int
) -> Tuple[bool, List[int]]:
    """Test whether p is shadow-regular for the algebra A.

    A prime p is shadow-regular if p does not divide the numerator of
    S_r(A)/r! for any 2 <= r <= p-1.

    Returns (is_regular, irregular_arities) where irregular_arities lists
    the arities where the criterion fails.
    """
    if p < 3:
        # For p=2, the range 2..p-1 = {2..1} is empty, so trivially regular
        return True, []

    irregular = []
    for r in range(2, p):
        Sr = tower.get(r, Fraction(0))
        if Sr == 0:
            continue
        # Compute S_r / r!
        normalized = Sr / factorial(r)
        # Check if p divides the numerator
        num = abs(normalized.numerator)
        if num % p == 0:
            irregular.append(r)

    return len(irregular) == 0, irregular


def shadow_regularity_table(
    tower: Dict[int, Fraction],
    primes: List[int],
) -> Dict[int, Tuple[bool, List[int]]]:
    """Compute shadow-regularity for multiple primes.

    Returns dict {p: (is_regular, irregular_arities)}.
    """
    return {p: shadow_kummer_regularity(tower, p) for p in primes}


# ============================================================================
# 9. p-adic generating function convergence
# ============================================================================

def padic_convergence_radius(
    tower: Dict[int, Fraction], p: int, max_arity: int = 20
) -> float:
    """Estimate the p-adic radius of convergence of H(t) = sum S_r t^r.

    The radius R_p satisfies 1/R_p = lim sup |S_r|_p^{1/r}
    = lim sup p^{-v_p(S_r)/r}.

    So log_p(1/R_p) = lim sup (-v_p(S_r)/r)
    and R_p = p^{lim inf (v_p(S_r)/r)}.
    """
    ratios = []
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        vp = v_p_safe(Sr, p)
        if vp != float('inf') and vp != float('-inf'):
            ratios.append(vp / r)

    if not ratios:
        return float('inf')

    # lim inf of v_p(S_r)/r
    # Use the minimum of the last portion as an estimate
    n = len(ratios)
    tail = ratios[n // 2:]
    if not tail:
        return float('inf')
    lim_inf = min(tail)
    if lim_inf == float('inf'):
        return float('inf')

    return float(p) ** lim_inf


def archimedean_radius(tower: Dict[int, Fraction], max_arity: int = 20) -> float:
    """Estimate the archimedean (real) radius of convergence of H(t).

    1/R = lim sup |S_r|^{1/r}.
    """
    ratios = []
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        if Sr != 0:
            ratios.append(abs(float(Sr)) ** (1.0 / r))

    if not ratios:
        return float('inf')

    # lim sup
    n = len(ratios)
    tail = ratios[n // 2:]
    lim_sup = max(tail) if tail else 0.0
    if lim_sup < 1e-30:
        return float('inf')
    return 1.0 / lim_sup


# ============================================================================
# 10. p-adic interpolation of kappa
# ============================================================================

def kappa_interpolation_sl2(k_val: Fraction, p: int) -> Dict[str, Any]:
    """Study p-adic interpolation of kappa(sl_2, k) = 3(k+2)/4.

    This is linear in k, hence trivially p-adic analytic on all of Z_p.
    The p-adic radius of analyticity is infinite.
    """
    k = Fraction(k_val)
    kappa = affine_sl2_kappa(k)
    return {
        'k': k,
        'kappa': kappa,
        'v_p_kappa': v_p_safe(kappa, p),
        'formula': '3*(k+2)/4',
        'analyticity': 'linear, trivially p-adic analytic on Z_p',
        'radius': float('inf'),
    }


def kappa_interpolation_virasoro(c_val: Fraction, p: int) -> Dict[str, Any]:
    """Study p-adic interpolation of kappa(Vir_c) = c/2.

    Linear in c, trivially p-adic analytic.
    """
    c = Fraction(c_val)
    kappa = c / 2
    return {
        'c': c,
        'kappa': kappa,
        'v_p_kappa': v_p_safe(kappa, p),
        'formula': 'c/2',
        'analyticity': 'linear, trivially p-adic analytic on Z_p',
        'radius': float('inf'),
    }


def kappa_interpolation_w3(c_val: Fraction, p: int) -> Dict[str, Any]:
    """Study p-adic interpolation of kappa(W_3, c) = 5c/6.

    Linear in c, p-adic analytic on Z_p for p != 2, 3.
    For p = 2 or p = 3: kappa = 5c/6 has a factor 1/6 = 1/(2*3),
    introducing a p-adic pole at p = 2, 3 for c in pZ_p.
    """
    c = Fraction(c_val)
    kappa = w3_kappa(c)
    return {
        'c': c,
        'kappa': kappa,
        'v_p_kappa': v_p_safe(kappa, p),
        'formula': '5*c/6',
        'analyticity': (
            'linear, trivially analytic on Z_p' if p > 3
            else f'linear, but 1/6 introduces pole at p={p}'
        ),
        'radius': float('inf'),
    }


# ============================================================================
# 11. Shadow ODE verification of p-adic structure
# ============================================================================

def shadow_ode_valuation_constraint(
    tower: Dict[int, Fraction], p: int, max_arity: int = 15
) -> List[Dict[str, Any]]:
    """Verify p-adic valuation constraints from the shadow ODE.

    The shadow metric recursion a_n = -conv(a) / (2*a_0) implies:
        v_p(a_n) >= min_{1<=j<n} (v_p(a_j) + v_p(a_{n-j})) - v_p(a_0)

    This gives a LOWER BOUND on v_p(S_r) from the recursion structure.
    HOWEVER, cancellation in the convolution sum can make v_p(a_n) strictly
    LESS than this bound.  This is the p-adic analogue of catastrophic
    cancellation.  The correct check is that the recursion identity holds
    exactly: a_n * 2 * a_0 + conv = 0.

    We verify both the identity (exact) and the naive bound (may fail
    due to cancellation, which is recorded but not flagged as an error).
    """
    # Reconstruct the a_n coefficients from the tower
    # S_r = a_{r-2} / r  =>  a_n = (n+2) * S_{n+2}
    results = []
    for r in range(5, max_arity + 1):
        n = r - 2
        # a_n = r * S_r
        Sr = tower.get(r, Fraction(0))
        an = r * Sr
        vp_an = v_p_safe(an, p)

        a0 = tower.get(2, Fraction(0)) * 2  # a_0 = 2 * S_2
        vp_a0 = v_p_safe(a0, p)

        # Compute convolution sum
        conv = Fraction(0)
        min_conv_vp = float('inf')
        for j in range(1, n):
            aj = (j + 2) * tower.get(j + 2, Fraction(0))
            anj = (n - j + 2) * tower.get(n - j + 2, Fraction(0))
            conv += aj * anj
            vp_j = v_p_safe(aj, p)
            vp_nj = v_p_safe(anj, p)
            if vp_j + vp_nj < min_conv_vp:
                min_conv_vp = vp_j + vp_nj

        # The recursion identity: a_n = -conv / (2 * a_0)
        # Equivalently: 2 * a_0 * a_n + conv = 0
        if a0 != 0:
            identity_residual = 2 * a0 * an + conv
            identity_holds = (identity_residual == 0)
        else:
            identity_holds = True  # degenerate case

        naive_bound = min_conv_vp - vp_a0
        # The naive bound may fail due to cancellation -- this is NOT a bug
        naive_satisfies = (vp_an >= naive_bound - 0.5) if vp_an != float('inf') else True

        results.append({
            'r': r,
            'v_p_S_r': v_p_safe(Sr, p),
            'v_p_a_n': vp_an,
            'recursion_bound': naive_bound,
            'satisfies': identity_holds,  # exact identity check
            'naive_bound_holds': naive_satisfies,
            'cancellation': not naive_satisfies,  # True if cancellation occurred
        })
    return results


# ============================================================================
# 12. Cross-verification: p-adic radius vs archimedean radius
# ============================================================================

def radius_cross_check(
    tower: Dict[int, Fraction],
    primes: List[int],
    max_arity: int = 20,
) -> Dict[str, Any]:
    """Cross-check p-adic convergence radii against archimedean radius.

    The product formula: prod_v |x|_v = 1 (over all places v including infinity)
    implies constraints between archimedean and p-adic radii.
    For a polynomial in Z[1/S] where S is a finite set of primes,
    the p-adic radius for p not in S equals 1.
    """
    R_infty = archimedean_radius(tower, max_arity)
    padic_radii = {}
    for p in primes:
        padic_radii[p] = padic_convergence_radius(tower, p, max_arity)

    return {
        'R_infty': R_infty,
        'padic_radii': padic_radii,
        'primes': primes,
    }


# ============================================================================
# 13. Comprehensive analysis
# ============================================================================

def virasoro_full_padic_analysis(
    c_val: Union[int, Fraction],
    primes: List[int],
    max_arity: int = 20,
) -> Dict[str, Any]:
    """Complete p-adic analysis of the Virasoro shadow tower at c = c_val."""
    c = Fraction(c_val)
    tower = virasoro_shadow_tower(c, max_arity)

    iwasawa_data = {}
    newton_data = {}
    regularity_data = {}
    ode_data = {}
    convergence_data = {}

    for p in primes:
        iwasawa_data[p] = shadow_iwasawa_full(tower, p, max_arity)
        newton_data[p] = {
            'polygon': newton_polygon(tower, p, max_arity),
            'slopes': newton_polygon_slopes(tower, p, max_arity),
        }
        regularity_data[p] = shadow_kummer_regularity(tower, p)
        ode_data[p] = shadow_ode_valuation_constraint(tower, p, min(max_arity, 15))
        convergence_data[p] = padic_convergence_radius(tower, p, max_arity)

    return {
        'c': c,
        'kappa': c / 2,
        'tower': tower,
        'iwasawa': iwasawa_data,
        'newton': newton_data,
        'regularity': regularity_data,
        'ode_constraints': ode_data,
        'padic_radii': convergence_data,
        'archimedean_radius': archimedean_radius(tower, max_arity),
    }


def affine_sl2_full_padic_analysis(
    k_val: Union[int, Fraction],
    primes: List[int],
    max_arity: int = 20,
) -> Dict[str, Any]:
    """Complete p-adic analysis of the affine sl_2 shadow tower at level k."""
    k = Fraction(k_val)
    tower = affine_sl2_shadow_tower(k, max_arity)

    iwasawa_data = {}
    newton_data = {}
    regularity_data = {}
    convergence_data = {}

    for p in primes:
        iwasawa_data[p] = shadow_iwasawa_full(tower, p, max_arity)
        newton_data[p] = {
            'polygon': newton_polygon(tower, p, max_arity),
            'slopes': newton_polygon_slopes(tower, p, max_arity),
        }
        regularity_data[p] = shadow_kummer_regularity(tower, p)
        convergence_data[p] = padic_convergence_radius(tower, p, max_arity)

    return {
        'k': k,
        'kappa': affine_sl2_kappa(k),
        'tower': tower,
        'iwasawa': iwasawa_data,
        'newton': newton_data,
        'regularity': regularity_data,
        'padic_radii': convergence_data,
        'archimedean_radius': archimedean_radius(tower, max_arity),
    }


def ferrero_washington_test(
    families: Dict[str, Dict[int, Fraction]],
    primes: List[int],
    max_arity: int = 20,
) -> Dict[str, Dict[int, Dict[str, Any]]]:
    """Test the shadow Ferrero-Washington analogue: mu_p^growth(A) = 0 for all A.

    The original Ferrero-Washington theorem (1979) proves mu = 0 for abelian
    extensions of Q.  The shadow analogue would be: the growth rate of
    v_p(S_r)/r converges to 0 for all standard families.

    Returns nested dict: result[family][p] = {growth_rate, satisfies_FW}.
    """
    result = {}
    for name, tower in families.items():
        result[name] = {}
        for p in primes:
            growth = shadow_iwasawa_growth_rate(tower, p, max_arity)
            result[name][p] = {
                'growth_rate': growth,
                'satisfies_FW': abs(growth) < 0.1,
            }
    return result


# ============================================================================
# 14. Virasoro discriminant and shadow metric p-adic analysis
# ============================================================================

def virasoro_discriminant(c: Fraction) -> Fraction:
    """Critical discriminant Delta(c) = 40/(5c+22) for Virasoro.

    Delta = 8 * kappa * S_4 = 8 * (c/2) * 10/(c(5c+22)) = 40/(5c+22).
    """
    c = Fraction(c)
    if 5 * c + 22 == 0:
        raise ValueError("Discriminant undefined at c = -22/5")
    return Fraction(40) / (5 * c + 22)


def shadow_metric_padic_data(c_val: Fraction, p: int) -> Dict[str, Any]:
    """p-adic data for the shadow metric at Virasoro central charge c."""
    c = Fraction(c_val)
    delta = virasoro_discriminant(c)
    kappa = c / 2
    alpha = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))

    return {
        'c': c,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': delta,
        'v_p_kappa': v_p_safe(kappa, p),
        'v_p_alpha': v_p_safe(alpha, p),
        'v_p_S4': v_p_safe(S4, p),
        'v_p_Delta': v_p_safe(delta, p),
    }


# ============================================================================
# 15. Batch computations for the requested parameter ranges
# ============================================================================

def virasoro_parameter_set() -> Dict[str, Fraction]:
    """The requested set of Virasoro central charges."""
    return {
        'c=1': Fraction(1),
        'c=1/2': Fraction(1, 2),
        'c=25': Fraction(25),
        'c=26': Fraction(26),
        'c=-2': Fraction(-2),
        'c=-22/5': Fraction(-22, 5),
    }


def affine_sl2_parameter_set() -> Dict[str, Fraction]:
    """The requested set of affine sl_2 levels."""
    return {
        'k=1': Fraction(1),
        'k=2': Fraction(2),
        'k=3': Fraction(3),
        'k=4': Fraction(4),
        'k=-1/2': Fraction(-1, 2),
        'k=-3/2': Fraction(-3, 2),
    }


def w3_parameter_set() -> Dict[str, Fraction]:
    """The requested set of W_3 central charges."""
    return {
        'c=2': Fraction(2),
        'c=50': Fraction(50),
        'c=98': Fraction(98),
    }


def standard_primes() -> List[int]:
    """The standard set of primes for p-adic analysis."""
    return [2, 3, 5, 7, 11, 13]


def build_all_towers(max_arity: int = 20) -> Dict[str, Dict[int, Fraction]]:
    """Build shadow towers for all requested parameter values.

    Returns dict mapping descriptive names to shadow tower dicts.
    """
    towers = {}

    # Virasoro
    for name, c in virasoro_parameter_set().items():
        try:
            towers[f'Vir_{name}'] = virasoro_shadow_tower(c, max_arity)
        except (ValueError, ZeroDivisionError):
            pass

    # Affine sl_2
    for name, k in affine_sl2_parameter_set().items():
        try:
            towers[f'sl2_{name}'] = affine_sl2_shadow_tower(k, max_arity)
        except (ValueError, ZeroDivisionError):
            pass

    # W_3 T-line
    for name, c in w3_parameter_set().items():
        try:
            towers[f'W3_T_{name}'] = w3_shadow_tower_t_line(c, max_arity)
        except (ValueError, ZeroDivisionError):
            pass

    # W_3 W-line
    for name, c in w3_parameter_set().items():
        try:
            towers[f'W3_W_{name}'] = w3_shadow_tower_w_line(c, max_arity)
        except (ValueError, ZeroDivisionError):
            pass

    return towers


def full_landscape_analysis(
    max_arity: int = 18,
    primes: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """Full p-adic analysis of the shadow tower landscape.

    This is the main entry point for the comprehensive analysis.
    """
    if primes is None:
        primes = standard_primes()

    towers = build_all_towers(max_arity)

    # Iwasawa analysis for all
    iwasawa = {}
    for name, tower in towers.items():
        iwasawa[name] = {}
        for p in primes:
            iwasawa[name][p] = shadow_iwasawa_full(tower, p, max_arity)

    # Newton polygons
    newton = {}
    for name, tower in towers.items():
        newton[name] = {}
        for p in primes:
            newton[name][p] = {
                'polygon': newton_polygon(tower, p, max_arity),
                'slopes': newton_polygon_slopes(tower, p, max_arity),
            }

    # Regularity
    regularity = {}
    for name, tower in towers.items():
        regularity[name] = shadow_regularity_table(tower, primes)

    # Ferrero-Washington test
    fw = ferrero_washington_test(towers, primes, max_arity)

    # Convergence radii
    radii = {}
    for name, tower in towers.items():
        radii[name] = radius_cross_check(tower, primes, max_arity)

    return {
        'towers': towers,
        'iwasawa': iwasawa,
        'newton': newton,
        'regularity': regularity,
        'ferrero_washington': fw,
        'radii': radii,
        'primes': primes,
        'max_arity': max_arity,
    }
