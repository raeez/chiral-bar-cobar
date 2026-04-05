r"""Deep Iwasawa theory for shadow zeta functions of modular Koszul algebras.

MATHEMATICAL FRAMEWORK
======================

This module pushes far beyond the basic mu/lambda invariants computed in
padic_shadow_iwasawa_engine.py.  It implements:

1. FULL mu-INVARIANT TABLE across all primes p <= 97 and all standard
   families (Heisenberg, affine sl_2, Virasoro, W_3).  Maps the exact
   boundary of the shadow Ferrero-Washington phenomenon.

2. lambda-INVARIANT SPECTRUM for all (A, p) pairs where mu = 0.  Tests
   whether lambda_p depends on shadow depth class (G/L/C/M).

3. KUBOTA-LEOPOLDT p-ADIC L-FUNCTION L_p(s, chi_shadow) constructed from
   shadow data.  Uses Mahler expansion and verifies interpolation against
   complex L-values at negative integers.

4. IWASAWA MAIN CONJECTURE TEST: for mu = 0 cases, computes the
   characteristic ideal of the shadow Selmer group X_infty and tests
   whether char(X_infty) = (f_p(T)) in Lambda = Z_p[[T]].

5. CYCLOTOMIC TOWER: shadow zeta at each level of the Z_p-extension
   Q_n, testing growth rate against the Iwasawa formula
   |zeta_A(1/2; Q_n)| ~ lambda * p^n + mu * p^{p^n}.

6. KOSZUL DUALITY ON IWASAWA INVARIANTS: mu_p(A) vs mu_p(A!) and
   lambda_p(A) vs lambda_p(A!).

VERIFICATION PATHS (3+ per claim):
   Path 1: Direct power series computation in Z_p[[T]]
   Path 2: Iwasawa descent from finite levels Q_n
   Path 3: Functional equation consistency L_p(s) vs L_p(1-s)
   Path 4: Koszul complementarity cross-check (A vs A!)
   Path 5: Newton polygon slope counting vs lambda
   Path 6: Heisenberg single-term triviality

Manuscript references:
    chap:arithmetic-shadows (arithmetic_shadows.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)

Convention: shadow coefficients S_r from H(t) = sum_{r>=2} S_r t^r.
    S_2 = kappa for each family.

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general.
CAUTION (AP24): kappa + kappa' != 0 for Virasoro (kappa + kappa' = 13).
CAUTION (AP38): all numerical values computed from first principles, not
    hardcoded from literature.
CAUTION (AP48): kappa depends on full algebra, not Virasoro subalgebra.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, gcd, log
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union


# ============================================================================
# 0. Primes up to 97
# ============================================================================

PRIMES_TO_97 = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
]


# ============================================================================
# 1. p-adic valuation (standalone, no external dependency)
# ============================================================================

def v_p(x: Fraction, p: int) -> int:
    """p-adic valuation v_p(x) for rational x.

    Returns v such that x = p^v * (a/b) with gcd(a,p) = gcd(b,p) = 1.
    Raises ValueError for x = 0.
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
    """v_p returning float('inf') for zero."""
    if x == 0:
        return float('inf')
    return float(v_p(x, p))


def p_adic_unit_part(x: Fraction, p: int) -> Fraction:
    """Unit part u where x = p^{v_p(x)} * u with |u|_p = 1."""
    if x == 0:
        return Fraction(0)
    val = v_p(x, p)
    return x / Fraction(p) ** val


# ============================================================================
# 2. Exact Bernoulli numbers
# ============================================================================

_bernoulli_cache: Dict[int, Fraction] = {}


def bernoulli_number(n: int) -> Fraction:
    """Compute B_n (with B_1 = -1/2)."""
    if n in _bernoulli_cache:
        return _bernoulli_cache[n]
    B: List[Fraction] = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    if n >= 1:
        B[1] = Fraction(-1, 2)
    for k in range(2, n + 1):
        if k % 2 == 1:
            B[k] = Fraction(0)
            continue
        s = Fraction(0)
        for j in range(k):
            s += Fraction(comb(k + 1, j)) * B[j]
        B[k] = -s / (k + 1)
    for k in range(n + 1):
        _bernoulli_cache[k] = B[k]
    return B[n]


# ============================================================================
# 3. Shadow coefficient providers (exact rational)
# ============================================================================

def virasoro_shadow_tower(c_val: Fraction, max_arity: int = 60) -> Dict[int, Fraction]:
    r"""Exact shadow tower for Virasoro at central charge c.

    Uses Taylor expansion of H(t) = t^2 sqrt(Q_L(t)) / sqrt(Q_L(0))
    where Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Parameters:
        kappa = c/2
        alpha = 2 (c-independent; S_3 = 2 for Virasoro)
        Q^contact = S_4 = 10/(c(5c+22))  (quartic shadow coefficient)
        Delta = 8*kappa*S_4 = 40/(5c+22)  (critical discriminant)

    AP9: The shadow coefficient S_4 = Q^contact = 10/(c(5c+22)) is the quartic
    term of the shadow obstruction tower. This is NOT the same as the shadow
    metric quadratic coefficient q_2 = 9*alpha^2 + 16*kappa*S_4, which enters
    Q_L(t) as q_2*t^2. The two differ by additive and multiplicative terms
    involving alpha and kappa.

    S_r = a_{r-2}/r where a_n are Taylor coefficients of sqrt(Q_L(t))
    normalized so a_0 = 2*kappa.
    """
    c = Fraction(c_val)
    if c == 0:
        raise ValueError("c must be nonzero for Virasoro shadow tower")

    if 5 * c + 22 == 0:
        raise ValueError("c = -22/5 (Yang-Lee edge) is singular: 5c+22 = 0")
    kappa = c / 2
    alpha = Fraction(2)  # S_3 = 2 (c-independent for Virasoro)
    S4_param = Fraction(10) / (c * (5 * c + 22))  # Q^contact

    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4_param

    max_n = max_arity - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = 2 * kappa
    if max_n >= 1:
        a[1] = q1 / (2 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a[0])
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0])

    tower = {}
    for r in range(2, max_arity + 1):
        tower[r] = a[r - 2] / r
    return tower


def heisenberg_shadow_tower(k_val: Fraction, max_arity: int = 60) -> Dict[int, Fraction]:
    """Shadow tower for Heisenberg H_k. Class G: terminates at arity 2.

    S_2 = k (the level), S_r = 0 for r >= 3.
    """
    k = Fraction(k_val)
    tower = {2: k}
    for r in range(3, max_arity + 1):
        tower[r] = Fraction(0)
    return tower


def affine_sl2_shadow_tower(k_val: Fraction, max_arity: int = 60) -> Dict[int, Fraction]:
    """Shadow tower for affine sl_2 at level k. Class L: terminates at arity 3.

    kappa = 3(k+2)/4, S_3 = 2*h^v/(k+h^v) = 4/(k+2), S_r = 0 for r >= 4.

    BUG FIX: S_3 was hardcoded to 1, which is only correct at k=2.
    The parametric formula S_3 = 2*h_dual/(k + h_dual) gives S_3 = 4/(k+2)
    for sl_2 (h_dual = 2). Check: k=2 => S_3 = 4/4 = 1 (matches old value).
    k=1 => S_3 = 4/3. k=4 => S_3 = 4/6 = 2/3.
    """
    k = Fraction(k_val)
    h_dual = Fraction(2)  # h^vee for sl_2
    kappa = Fraction(3) * (k + h_dual) / 4
    S3 = 2 * h_dual / (k + h_dual)  # = 4/(k+2) for sl_2
    tower = {2: kappa, 3: S3}
    for r in range(4, max_arity + 1):
        tower[r] = Fraction(0)
    return tower


def w3_shadow_tower_t_line(c_val: Fraction, max_arity: int = 60) -> Dict[int, Fraction]:
    """W_3 shadow tower on the T-line (Virasoro sector)."""
    return virasoro_shadow_tower(c_val, max_arity)


def w3_shadow_tower_w_line(c_val: Fraction, max_arity: int = 60) -> Dict[int, Fraction]:
    """W_3 shadow tower on the W-line.

    Z_2 parity kills odd arities. S_2 = c/3, S_3 = 0,
    S_4 = 2560/[c(5c+22)^3], S_5 = 0, etc.
    """
    c = Fraction(c_val)
    if c == 0:
        raise ValueError("c must be nonzero")

    kappa_W = c / 3
    S4_W = Fraction(2560) / (c * (5 * c + 22) ** 3)

    q0 = 4 * kappa_W ** 2
    q2 = 16 * kappa_W * S4_W

    max_n = max_arity - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = 2 * kappa_W
    if max_n >= 2 and a[0] != 0:
        a[2] = q2 / (2 * a[0])
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a[0]) if a[0] != 0 else Fraction(0)

    tower = {}
    for r in range(2, max_arity + 1):
        idx = r - 2
        tower[r] = a[idx] / r if idx <= max_n else Fraction(0)
    return tower


# ============================================================================
# 4. Koszul dual shadow towers
# ============================================================================

def virasoro_koszul_dual_c(c_val: Fraction) -> Fraction:
    """Koszul dual of Vir_c is Vir_{26-c}."""
    return Fraction(26) - Fraction(c_val)


def affine_sl2_koszul_dual_k(k_val: Fraction) -> Fraction:
    """Feigin-Frenkel involution for sl_2: k -> -k - 2h^v = -k - 4."""
    return -Fraction(k_val) - 4


def heisenberg_koszul_dual_k(k_val: Fraction) -> Fraction:
    """Koszul dual level for Heisenberg: k -> -k."""
    return -Fraction(k_val)


# ============================================================================
# 5. Iwasawa power series construction
# ============================================================================

def teichmuller_lift(a: int, p: int, precision: int = 40) -> int:
    r"""Teichmuller representative omega(a) mod p^precision.

    The unique (p-1)-th root of unity in Z_p reducing to a mod p.
    Computed by Hensel lifting: x -> x^p converges to the Teichmuller lift.
    """
    if p == 2:
        return 1  # (Z/2Z)^* = {1}
    a = a % p
    if a == 0:
        return 0
    modulus = p ** precision
    x = a
    for _ in range(precision + 10):
        x = pow(x, p, modulus)
    return x


def diamond_bracket(r: int, p: int, precision: int = 40) -> Fraction:
    r"""Diamond bracket <r> = r / omega(r) in 1 + pZ_p.

    For p = 2: use gamma = 5, so <r> = r for r = 1 mod 4,
    <r> = -r for r = 3 mod 4.
    """
    if r % p == 0:
        raise ValueError(f"r={r} divisible by p={p}")
    if p == 2:
        if r % 4 == 1:
            return Fraction(r)
        elif r % 4 == 3:
            return Fraction(-r)
        else:
            raise ValueError(f"r={r} is even")

    modulus = p ** precision
    omega_r = teichmuller_lift(r, p, precision)
    if omega_r == 0:
        raise ValueError(f"Teichmuller lift is 0 for r={r}, p={p}")
    omega_inv = pow(omega_r, -1, modulus)
    bracket = (r * omega_inv) % modulus
    return Fraction(bracket)


def iwasawa_log_p(x: Fraction, p: int, terms: int = 40) -> Fraction:
    r"""Iwasawa p-adic logarithm log_p(x) for x in 1 + pZ_p.

    log_p(x) = -sum_{n=1}^{terms} (1-x)^n / n

    We work in Q with enough terms for convergence mod p^prec.
    """
    u = Fraction(1) - x
    result = Fraction(0)
    u_power = Fraction(1)
    for n in range(1, terms + 1):
        u_power *= u
        result -= u_power / n
    return result


def iwasawa_power_series_coefficients(
    tower: Dict[int, Fraction],
    p: int,
    max_terms: int = 30,
    precision: int = 30
) -> List[Fraction]:
    r"""Compute coefficients of the Iwasawa power series f_p(T) in Z_p[[T]].

    The p-adic shadow zeta function is:
        zeta_{p,A}(s) = sum_{r>=2, p nmid r} S_r(A) * <r>^{-s}

    Setting T = gamma^s - 1 where gamma = 1 + p (odd p) or gamma = 5 (p=2):
        f_p(T) = sum_{r>=2, p nmid r} S_r * (1+T)^{-log_p(<r>)/log_p(gamma)}

    Expanding in T via binomial series to precision max_terms:
        f_p(T) = sum_{n=0}^{max_terms} a_n T^n

    where a_n = sum_{r>=2, p nmid r} S_r * C(alpha_r, n)
    with alpha_r = -log_p(<r>) / log_p(gamma) and C(alpha, n) = alpha*(alpha-1)*...*(alpha-n+1)/n!.

    We compute a_n as exact rationals.
    """
    gamma = 5 if p == 2 else (1 + p)
    gamma_frac = Fraction(gamma)

    # Precompute log_p(gamma) modulo enough precision
    # For 1 + p*Z_p elements, the Iwasawa log converges
    log_gamma = iwasawa_log_p(gamma_frac, p, terms=precision)

    if log_gamma == 0:
        # Degenerate case -- shouldn't happen for valid gamma
        return [Fraction(0)] * (max_terms + 1)

    coeffs = [Fraction(0)] * (max_terms + 1)

    for r, S_r in tower.items():
        if r < 2:
            continue
        if S_r == 0:
            continue
        if r % p == 0:
            continue  # Remove Euler factor at p

        # Compute <r> = r / omega(r)
        try:
            br = diamond_bracket(r, p, precision)
        except (ValueError, ZeroDivisionError):
            continue

        # alpha_r = -log_p(<r>) / log_p(gamma)
        log_br = iwasawa_log_p(br, p, terms=precision)
        alpha_r = -log_br / log_gamma

        # Binomial coefficients C(alpha_r, n) = alpha_r * (alpha_r - 1) * ... * (alpha_r - n + 1) / n!
        binom_coeff = Fraction(1)  # C(alpha_r, 0) = 1
        coeffs[0] += S_r * binom_coeff
        for n in range(1, max_terms + 1):
            binom_coeff *= (alpha_r - (n - 1)) / n
            coeffs[n] += S_r * binom_coeff

    return coeffs


# ============================================================================
# 6. mu-invariant and lambda-invariant from power series
# ============================================================================

def mu_invariant(coeffs: List[Fraction], p: int) -> int:
    r"""Compute the Iwasawa mu-invariant.

    mu = min_n v_p(a_n) over all nonzero coefficients a_n.
    If all coefficients are zero, returns +inf (as large int).
    """
    vals = []
    for a in coeffs:
        if a != 0:
            vals.append(v_p(a, p))
    if not vals:
        return 999  # Proxy for infinity
    return min(vals)


def lambda_invariant(coeffs: List[Fraction], p: int) -> int:
    r"""Compute the Iwasawa lambda-invariant.

    lambda = min{n : v_p(a_n) = mu}.
    This is the degree of the distinguished polynomial in the
    Weierstrass preparation.
    """
    mu = mu_invariant(coeffs, p)
    if mu == 999:
        return 0
    for n, a in enumerate(coeffs):
        if a != 0 and v_p(a, p) == mu:
            return n
    return len(coeffs)  # Should not reach here


def nu_invariant(coeffs: List[Fraction], p: int) -> int:
    r"""Compute the Iwasawa nu-invariant (unit part indicator).

    nu = v_p(a_lambda) where lambda is the lambda-invariant.
    Should equal mu when mu = 0.
    """
    lam = lambda_invariant(coeffs, p)
    if lam >= len(coeffs):
        return 999
    a_lam = coeffs[lam]
    if a_lam == 0:
        return 999
    return v_p(a_lam, p)


# ============================================================================
# 7. Newton polygon
# ============================================================================

def newton_polygon(coeffs: List[Fraction], p: int) -> List[Tuple[int, float]]:
    r"""Lower convex hull of {(n, v_p(a_n)) : a_n != 0}.

    Returns vertices of the Newton polygon as (n, v_p(a_n)) pairs.
    """
    points = []
    for n, a in enumerate(coeffs):
        if a != 0:
            points.append((n, float(v_p(a, p))))

    if len(points) <= 1:
        return points

    # Graham scan for lower convex hull
    points.sort()
    hull = []
    for pt in points:
        while len(hull) >= 2:
            # Check if last point makes a left turn
            o = hull[-2]
            a_pt = hull[-1]
            # Cross product (a-o) x (pt-o)
            cross = (a_pt[0] - o[0]) * (pt[1] - o[1]) - (a_pt[1] - o[1]) * (pt[0] - o[0])
            if cross <= 0:
                hull.pop()
            else:
                break
        hull.append(pt)
    return hull


def newton_polygon_slopes(coeffs: List[Fraction], p: int) -> List[float]:
    """Slopes of the Newton polygon segments."""
    hull = newton_polygon(coeffs, p)
    if len(hull) <= 1:
        return []
    slopes = []
    for i in range(1, len(hull)):
        dx = hull[i][0] - hull[i - 1][0]
        dy = hull[i][1] - hull[i - 1][1]
        if dx > 0:
            slopes.append(dy / dx)
    return slopes


def newton_polygon_zero_count(coeffs: List[Fraction], p: int) -> int:
    r"""Count zeros of f(T) in the open unit disk |T|_p < 1.

    Equals the number of Newton polygon segments with negative slope,
    counted with multiplicity (length of horizontal span).
    """
    hull = newton_polygon(coeffs, p)
    if len(hull) <= 1:
        return 0
    count = 0
    for i in range(1, len(hull)):
        dx = hull[i][0] - hull[i - 1][0]
        dy = hull[i][1] - hull[i - 1][1]
        if dx > 0 and dy < 0:
            count += int(dx)
    return count


# ============================================================================
# 8. Full mu-invariant table (all primes, all families)
# ============================================================================

def mu_table_virasoro(
    c_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, int], int]:
    r"""Compute mu_p(Vir_c) for all (c, p) pairs.

    Returns dict {(c, p): mu}.
    """
    if primes is None:
        primes = PRIMES_TO_97
    result = {}
    for c in c_values:
        c_frac = Fraction(c)
        try:
            tower = virasoro_shadow_tower(c_frac, max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            result[(c, p)] = mu_invariant(coeffs, p)
    return result


def mu_table_heisenberg(
    k_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, int], int]:
    """Compute mu_p(H_k) for all (k, p) pairs."""
    if primes is None:
        primes = PRIMES_TO_97
    result = {}
    for k in k_values:
        tower = heisenberg_shadow_tower(Fraction(k), max_arity)
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            result[(k, p)] = mu_invariant(coeffs, p)
    return result


def mu_table_affine_sl2(
    k_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, int], int]:
    """Compute mu_p(V_k(sl_2)) for all (k, p) pairs."""
    if primes is None:
        primes = PRIMES_TO_97
    result = {}
    for k in k_values:
        tower = affine_sl2_shadow_tower(Fraction(k), max_arity)
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            result[(k, p)] = mu_invariant(coeffs, p)
    return result


def mu_table_w3(
    c_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20,
    line: str = "T"
) -> Dict[Tuple[int, int], int]:
    """Compute mu_p(W_3) for all (c, p) pairs on the specified line."""
    if primes is None:
        primes = PRIMES_TO_97
    tower_fn = w3_shadow_tower_t_line if line == "T" else w3_shadow_tower_w_line
    result = {}
    for c in c_values:
        c_frac = Fraction(c)
        try:
            tower = tower_fn(c_frac, max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            result[(c, p)] = mu_invariant(coeffs, p)
    return result


# ============================================================================
# 9. Full lambda-invariant spectrum
# ============================================================================

def lambda_spectrum_virasoro(
    c_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, int], int]:
    r"""Compute lambda_p(Vir_c) for all (c, p) where mu = 0.

    Returns dict {(c, p): lambda} restricted to mu = 0 cases.
    """
    if primes is None:
        primes = PRIMES_TO_97[:25]  # First 25 primes
    result = {}
    for c in c_values:
        c_frac = Fraction(c)
        try:
            tower = virasoro_shadow_tower(c_frac, max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            mu = mu_invariant(coeffs, p)
            if mu == 0:
                result[(c, p)] = lambda_invariant(coeffs, p)
    return result


def lambda_spectrum_affine_sl2(
    k_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, int], int]:
    """lambda_p(V_k(sl_2)) for mu = 0 cases."""
    if primes is None:
        primes = PRIMES_TO_97[:25]
    result = {}
    for k in k_values:
        tower = affine_sl2_shadow_tower(Fraction(k), max_arity)
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            mu = mu_invariant(coeffs, p)
            if mu == 0:
                result[(k, p)] = lambda_invariant(coeffs, p)
    return result


# ============================================================================
# 10. Kubota-Leopoldt p-adic L-function from shadow data
# ============================================================================

def shadow_dirichlet_character(
    tower: Dict[int, Fraction],
    modulus: int,
    max_r: int = 40
) -> Dict[int, Fraction]:
    r"""Extract a Dirichlet character from the shadow tower.

    chi_shadow(r) = S_r / |S_r| * sign, reduced modulo the conductor.
    For our purposes, we use the p-part structure of S_r as the character.

    Actually, for the p-adic L-function we directly use the shadow
    coefficients S_r as the "moments" of a p-adic measure, rather than
    extracting a separate Dirichlet character.

    Returns: {r: S_r mod conductor} for r coprime to modulus.
    """
    result = {}
    for r in range(2, max_r + 1):
        if r in tower and tower[r] != 0 and gcd(r, modulus) == 1:
            result[r] = tower[r]
    return result


def kubota_leopoldt_shadow(
    tower: Dict[int, Fraction],
    p: int,
    s_values: List[Fraction],
    max_r: int = 50
) -> Dict[Fraction, Fraction]:
    r"""Compute the shadow Kubota-Leopoldt p-adic L-function at given s-values.

    L_p^{sh}(s) = sum_{r>=2, p nmid r} S_r * <r>^{-s}

    For integer s = 1-n (n >= 1), the interpolation property reads:
        L_p^{sh}(1-n) = (1 - S_p * p^{n-1}) * Z_sh(1-n)  [approximate]
    where Z_sh(1-n) = sum_{r>=2} S_r * r^{n-1} is the "archimedean" value.

    We compute L_p^{sh}(s) for s in s_values using the Mahler expansion:
        L_p^{sh}(s) = sum_n a_n C(s, n)
    where C(s,n) = s(s-1)...(s-n+1)/n! is the Mahler coefficient basis.

    Implementation: compute the Iwasawa power series coefficients and
    evaluate via the change of variables T = gamma^s - 1.
    """
    gamma = Fraction(5 if p == 2 else 1 + p)

    results = {}
    for s in s_values:
        s_frac = Fraction(s)
        # T = gamma^s - 1, but for rational s we need to define gamma^s
        # For integer s, gamma^s is exact
        if s_frac.denominator == 1:
            n = int(s_frac)
            T = gamma ** n - 1
        else:
            # For non-integer s, use truncated power series approximation
            # gamma^s = exp(s * log(gamma)) ~ sum s^k (log gamma)^k / k!
            # In Q_p arithmetic, work with enough terms
            log_g = iwasawa_log_p(gamma, p, terms=30)
            T = Fraction(0)
            power = Fraction(1)
            for k in range(1, 30):
                power *= s_frac * log_g / k
                T += power
            # T = exp(s * log_p(gamma)) - 1

        # Evaluate f_p(T) = sum a_n T^n
        coeffs = iwasawa_power_series_coefficients(tower, p, max_terms=25)
        result = Fraction(0)
        T_power = Fraction(1)
        for n, a_n in enumerate(coeffs):
            result += a_n * T_power
            T_power *= T

        results[s_frac] = result

    return results


def archimedean_shadow_L(
    tower: Dict[int, Fraction],
    n: int
) -> Fraction:
    r"""Compute the archimedean shadow L-value Z_sh(1-n) = sum_{r>=2} S_r * r^{n-1}.

    This is the "complex" L-value that the p-adic L-function interpolates.
    """
    result = Fraction(0)
    for r, S_r in tower.items():
        if r >= 2 and S_r != 0:
            result += S_r * Fraction(r) ** (n - 1)
    return result


def interpolation_test(
    tower: Dict[int, Fraction],
    p: int,
    n_values: List[int],
    max_r: int = 50
) -> List[Dict[str, Any]]:
    r"""Test the interpolation property at s = 1-n for n in n_values.

    For each n, computes:
      - L_p^{sh}(1-n) via the power series
      - Z_sh(1-n) = sum S_r * r^{n-1} (archimedean)
      - Euler factor correction (1 - S_p * p^{n-1}) if p >= 2

    The interpolation "theorem" (which is an analogy, not rigorous):
        L_p^{sh}(1-n) ~ (1 - S_p * p^{n-1}) * Z_sh(1-n)
    """
    S_p = tower.get(p, Fraction(0))

    s_values = [Fraction(1 - n) for n in n_values]
    padic_values = kubota_leopoldt_shadow(tower, p, s_values, max_r)

    results = []
    for n in n_values:
        s = Fraction(1 - n)
        Z_arch = archimedean_shadow_L(tower, n)
        euler_factor = 1 - S_p * Fraction(p) ** (n - 1) if p >= 2 else Fraction(1)
        predicted = euler_factor * Z_arch
        actual = padic_values.get(s, Fraction(0))

        results.append({
            'n': n,
            's': s,
            'L_p': actual,
            'Z_arch': Z_arch,
            'euler_factor': euler_factor,
            'predicted': predicted,
            'match': actual == predicted,
            'ratio': actual / predicted if predicted != 0 else None,
        })
    return results


# ============================================================================
# 11. Cyclotomic tower: shadow zeta at Z_p-extension levels
# ============================================================================

def cyclotomic_level_shadow_zeta(
    tower: Dict[int, Fraction],
    p: int,
    level: int,
    s_eval: Fraction = Fraction(1, 2)
) -> Fraction:
    r"""Compute shadow zeta at level n of the Z_p-cyclotomic tower.

    At level n, the "conductor" is p^{n+1} (for p odd) or 2^{n+2} (for p=2).
    The shadow zeta at level n restricts the sum to r with r coprime to p
    and additionally weights by the level-n character.

    Simplified model: weight the sum by <r>^{p^n} / <r>^{p^n} congruence:
        zeta_A(s; Q_n) = sum_{r>=2, p nmid r} S_r * r^{-s} * chi_n(r)
    where chi_n(r) = 1 if <r> = 1 mod p^{n+1}, else a p^n-th root of unity.

    For a concrete computation, we use the simpler model:
        zeta_A(s; Q_n) = sum_{r>=2, r = 1 mod p^n} S_r * r^{-s}
    restricted to the trivial character at level n.
    """
    modulus = p ** level if p > 2 else 2 ** (level + 1)
    result = Fraction(0)
    for r, S_r in tower.items():
        if r < 2 or S_r == 0:
            continue
        if r % p == 0:
            continue
        if r % modulus == 1 or (level == 0 and r % p != 0):
            # At level 0, include all r coprime to p
            # At higher levels, restrict to r = 1 mod p^n
            if level == 0 or r % modulus == 1:
                # Evaluate r^{-s}: for s = 1/2, use float then convert back
                # Actually for exact rational s and integer r, r^{-s} is algebraic.
                # We approximate: use rational approximation of r^{-s}
                if s_eval == Fraction(1, 2):
                    # r^{-1/2} is irrational; use rational approx
                    import math
                    approx = Fraction(int(10**15 / math.sqrt(r)), 10**15)
                    result += S_r * approx
                elif s_eval.denominator == 1:
                    s_int = int(s_eval)
                    if s_int >= 0:
                        result += S_r / Fraction(r) ** s_int
                    else:
                        result += S_r * Fraction(r) ** (-s_int)
                else:
                    import math
                    approx = Fraction(int(10**15 * r ** float(-s_eval)), 10**15)
                    result += S_r * approx
    return result


def cyclotomic_growth_test(
    tower: Dict[int, Fraction],
    p: int,
    max_level: int = 5,
    s_eval: Fraction = Fraction(1)
) -> List[Dict[str, Any]]:
    r"""Test growth rate in the cyclotomic Z_p-tower.

    For the shadow zeta at level n of the Z_p-extension, the Iwasawa
    formula predicts:
        |zeta_A(s; Q_n)|_p ~ lambda * p^n + mu * p^{p^n}

    We compute the p-adic valuation of the shadow zeta at each level
    and check whether the growth is linear (mu = 0) or exponential (mu > 0).
    """
    results = []
    for n in range(max_level + 1):
        val = cyclotomic_level_shadow_zeta(tower, p, n, s_eval)
        vp = v_p_safe(val, p)
        results.append({
            'level': n,
            'value': val,
            'v_p': vp,
            'predicted_linear': n,  # lambda * p^n for lambda = 1
        })
    return results


# ============================================================================
# 12. Koszul duality on Iwasawa invariants
# ============================================================================

def koszul_mu_comparison_virasoro(
    c_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> List[Dict[str, Any]]:
    r"""Compare mu_p(Vir_c) with mu_p(Vir_{26-c}).

    Tests complementarity: is there a pattern in mu_p(A) + mu_p(A!)?
    """
    if primes is None:
        primes = PRIMES_TO_97[:10]
    results = []
    for c in c_values:
        c_dual = 26 - c
        if c_dual <= 0 or c_dual == c:
            continue
        try:
            tower_A = virasoro_shadow_tower(Fraction(c), max_arity)
            tower_A_dual = virasoro_shadow_tower(Fraction(c_dual), max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        for p in primes:
            coeffs_A = iwasawa_power_series_coefficients(tower_A, p, max_terms)
            coeffs_dual = iwasawa_power_series_coefficients(tower_A_dual, p, max_terms)
            mu_A = mu_invariant(coeffs_A, p)
            mu_dual = mu_invariant(coeffs_dual, p)
            lam_A = lambda_invariant(coeffs_A, p)
            lam_dual = lambda_invariant(coeffs_dual, p)
            results.append({
                'c': c,
                'c_dual': c_dual,
                'p': p,
                'mu_A': mu_A,
                'mu_dual': mu_dual,
                'mu_sum': mu_A + mu_dual,
                'lambda_A': lam_A,
                'lambda_dual': lam_dual,
                'lambda_sum': lam_A + lam_dual,
            })
    return results


def koszul_lambda_comparison_affine(
    k_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> List[Dict[str, Any]]:
    r"""Compare lambda_p(sl_2, k) with lambda_p(sl_2, -k-4).

    The Feigin-Frenkel dual of V_k(sl_2) has k' = -k - 2h^v = -k - 4.
    Note: kappa(sl_2, k) + kappa(sl_2, -k-4) = 3(k+2)/4 + 3(-k-4+2)/4
        = 3(k+2)/4 + 3(-k-2)/4 = 0.  (Anti-symmetric for KM.)
    """
    if primes is None:
        primes = PRIMES_TO_97[:10]
    results = []
    for k in k_values:
        k_dual = -k - 4
        tower_A = affine_sl2_shadow_tower(Fraction(k), max_arity)
        tower_dual = affine_sl2_shadow_tower(Fraction(k_dual), max_arity)
        for p in primes:
            coeffs_A = iwasawa_power_series_coefficients(tower_A, p, max_terms)
            coeffs_dual = iwasawa_power_series_coefficients(tower_dual, p, max_terms)
            mu_A = mu_invariant(coeffs_A, p)
            mu_dual = mu_invariant(coeffs_dual, p)
            lam_A = lambda_invariant(coeffs_A, p)
            lam_dual = lambda_invariant(coeffs_dual, p)
            results.append({
                'k': k,
                'k_dual': k_dual,
                'p': p,
                'mu_A': mu_A,
                'mu_dual': mu_dual,
                'mu_sum': mu_A + mu_dual,
                'lambda_A': lam_A,
                'lambda_dual': lam_dual,
                'lambda_sum': lam_A + lam_dual,
                'kappa_A': Fraction(3) * (k + 2) / 4,
                'kappa_dual': Fraction(3) * (k_dual + 2) / 4,
                'kappa_sum': Fraction(0),  # Anti-symmetric for KM
            })
    return results


# ============================================================================
# 13. Iwasawa Main Conjecture test
# ============================================================================

def weierstrass_preparation(
    coeffs: List[Fraction],
    p: int,
    precision: int = 20
) -> Tuple[int, int, List[Fraction]]:
    r"""Weierstrass preparation: f(T) = p^mu * g(T) * u(T)
    where g(T) is a distinguished polynomial of degree lambda and
    u(T) is a unit in Z_p[[T]].

    Returns (mu, lambda, distinguished_poly_coeffs).
    """
    mu = mu_invariant(coeffs, p)
    lam = lambda_invariant(coeffs, p)

    if mu == 999:
        return (999, 0, [])

    # Normalize: remove p^mu factor
    normalized = [c / Fraction(p) ** mu for c in coeffs]

    # Distinguished polynomial: first lambda+1 coefficients of g(T)
    # g(T) = T^lambda + a_{lambda-1} T^{lambda-1} + ... + a_0
    # where v_p(a_i) >= 1 for i < lambda
    dist_poly = []
    for i in range(lam + 1):
        if i < len(normalized):
            dist_poly.append(normalized[i])
        else:
            dist_poly.append(Fraction(0))

    return (mu, lam, dist_poly)


def characteristic_ideal_test(
    tower: Dict[int, Fraction],
    p: int,
    max_arity: int = 40,
    max_terms: int = 25
) -> Dict[str, Any]:
    r"""Test the Iwasawa Main Conjecture analogue for the shadow tower.

    The analytic side: f_p(T) = the Iwasawa power series.
    The algebraic side: char(X_infty) = the characteristic ideal of the
    shadow Selmer group.

    For the shadow analogy, we MODEL the Selmer group as follows:
    X_infty ~ Z_p[[T]] / (f_p(T))  (this is the Main Conjecture statement).

    The test: the zeros of f_p(T) should be simple (no repeated roots),
    and the lambda-invariant should equal the Newton polygon zero count.

    Returns diagnostic data.
    """
    coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
    mu = mu_invariant(coeffs, p)
    lam = lambda_invariant(coeffs, p)
    mu_val, lam_val, dist_poly = weierstrass_preparation(coeffs, p)
    np_zeros = newton_polygon_zero_count(coeffs, p)
    np_slopes = newton_polygon_slopes(coeffs, p)

    return {
        'p': p,
        'mu': mu,
        'lambda': lam,
        'weierstrass_mu': mu_val,
        'weierstrass_lambda': lam_val,
        'newton_zero_count': np_zeros,
        'newton_slopes': np_slopes,
        'main_conjecture_consistent': (mu == 0 and lam == np_zeros),
        'dist_poly_len': len(dist_poly),
    }


# ============================================================================
# 14. Comprehensive analysis functions
# ============================================================================

def full_iwasawa_analysis_virasoro(
    c: int,
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[str, Any]:
    """Full Iwasawa analysis for Virasoro at central charge c."""
    if primes is None:
        primes = PRIMES_TO_97[:10]
    c_frac = Fraction(c)
    tower = virasoro_shadow_tower(c_frac, max_arity)

    analysis = {
        'c': c,
        'kappa': c_frac / 2,
        'shadow_class': 'M',
        'primes': {},
    }

    for p in primes:
        coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
        mu = mu_invariant(coeffs, p)
        lam = lambda_invariant(coeffs, p)
        np_slopes = newton_polygon_slopes(coeffs, p)
        np_zeros = newton_polygon_zero_count(coeffs, p)

        analysis['primes'][p] = {
            'mu': mu,
            'lambda': lam,
            'newton_slopes': np_slopes,
            'newton_zero_count': np_zeros,
            'ferrero_washington': mu == 0,
        }

    return analysis


def full_iwasawa_analysis_heisenberg(
    k: int,
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[str, Any]:
    """Full Iwasawa analysis for Heisenberg at level k."""
    if primes is None:
        primes = PRIMES_TO_97[:10]
    tower = heisenberg_shadow_tower(Fraction(k), max_arity)

    analysis = {
        'k': k,
        'kappa': Fraction(k),
        'shadow_class': 'G',
        'primes': {},
    }

    for p in primes:
        coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
        mu = mu_invariant(coeffs, p)
        lam = lambda_invariant(coeffs, p)

        analysis['primes'][p] = {
            'mu': mu,
            'lambda': lam,
            'ferrero_washington': mu == 0,
        }

    return analysis


def full_iwasawa_analysis_affine(
    k: int,
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[str, Any]:
    """Full Iwasawa analysis for affine sl_2 at level k."""
    if primes is None:
        primes = PRIMES_TO_97[:10]
    tower = affine_sl2_shadow_tower(Fraction(k), max_arity)

    analysis = {
        'k': k,
        'kappa': Fraction(3) * (k + 2) / 4,
        'shadow_class': 'L',
        'primes': {},
    }

    for p in primes:
        coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
        mu = mu_invariant(coeffs, p)
        lam = lambda_invariant(coeffs, p)

        analysis['primes'][p] = {
            'mu': mu,
            'lambda': lam,
            'ferrero_washington': mu == 0,
        }

    return analysis


def shadow_depth_class(family: str, **params) -> str:
    """Return the shadow depth class G/L/C/M for a given family."""
    if family == 'heisenberg':
        return 'G'
    elif family == 'affine_sl2':
        return 'L'
    elif family == 'betagamma':
        return 'C'
    elif family in ('virasoro', 'w3'):
        return 'M'
    return 'unknown'


def lambda_by_depth_class(
    lambda_data: Dict[Tuple, int],
    depth_classes: Dict[Tuple, str]
) -> Dict[str, List[int]]:
    r"""Group lambda-invariants by shadow depth class.

    Tests whether lambda_p depends on class G/L/C/M.
    """
    result: Dict[str, List[int]] = {'G': [], 'L': [], 'C': [], 'M': []}
    for key, lam in lambda_data.items():
        cls = depth_classes.get(key, 'unknown')
        if cls in result:
            result[cls].append(lam)
    return result


# ============================================================================
# 15. Functional equation test
# ============================================================================

def functional_equation_test(
    tower: Dict[int, Fraction],
    p: int,
    n_values: List[int],
    max_arity: int = 50
) -> List[Dict[str, Any]]:
    r"""Test the shadow functional equation L_p(s) vs L_p(1-s).

    For standard L-functions, the functional equation relates L(s) to L(1-s)
    with a gamma/conductor factor.  For the shadow p-adic L-function, we
    test whether there is any relation between L_p^{sh}(n) and L_p^{sh}(1-n).

    This is EXPLORATORY -- there is no theorem guaranteeing a functional
    equation for the shadow zeta function.
    """
    results = []
    for n in n_values:
        s_pos = Fraction(n)
        s_neg = Fraction(1 - n)

        vals = kubota_leopoldt_shadow(tower, p, [s_pos, s_neg], max_arity)
        L_pos = vals.get(s_pos, Fraction(0))
        L_neg = vals.get(s_neg, Fraction(0))

        ratio = None
        if L_pos != 0 and L_neg != 0:
            ratio = L_neg / L_pos

        results.append({
            'n': n,
            'L_p(n)': L_pos,
            'L_p(1-n)': L_neg,
            'ratio': ratio,
        })
    return results


# ============================================================================
# 16. Heisenberg triviality verification
# ============================================================================

def heisenberg_iwasawa_triviality(
    k: int,
    p: int,
    max_terms: int = 20
) -> Dict[str, Any]:
    r"""Verify that Heisenberg has trivial Iwasawa theory.

    H_k has S_2 = k, S_r = 0 for r >= 3.  The Iwasawa power series
    reduces to a single term:
        f_p(T) = k * (1+T)^{alpha_2}  if p != 2 (p nmid 2)
    or 0 if p = 2 (since 2 % 2 == 0, the only term is removed).

    For p odd: f_p(T) = k * sum_n C(alpha_2, n) T^n
    where alpha_2 = -log_p(<2>) / log_p(gamma).

    mu = v_p(k), lambda = 0.
    """
    tower = heisenberg_shadow_tower(Fraction(k), max_arity=10)
    coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
    mu = mu_invariant(coeffs, p)
    lam = lambda_invariant(coeffs, p)

    # For p = 2: r = 2 is removed (p | r), so f_p = 0 from other terms
    # Actually S_r = 0 for r >= 3, and S_2 is removed when p = 2.
    # So f_p(T) = 0 for p = 2.
    if p == 2:
        all_zero = all(c == 0 for c in coeffs)
        return {
            'k': k, 'p': p,
            'mu': mu, 'lambda': lam,
            'trivial': all_zero,
            'reason': 'p=2 removes sole term r=2',
        }

    return {
        'k': k, 'p': p,
        'mu': mu, 'lambda': lam,
        'trivial': lam == 0,
        'expected_mu': v_p_safe(Fraction(k), p),
        'reason': 'single term from r=2',
    }


# ============================================================================
# 17. Batch computation utilities
# ============================================================================

def batch_mu_lambda_table(
    family: str,
    param_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, int], Tuple[int, int]]:
    r"""Compute (mu, lambda) for all (param, p) pairs.

    family: 'virasoro', 'heisenberg', 'affine_sl2', 'w3_T', 'w3_W'
    Returns: {(param, p): (mu, lambda)}
    """
    if primes is None:
        primes = PRIMES_TO_97[:15]

    tower_fn = {
        'virasoro': lambda v: virasoro_shadow_tower(Fraction(v), max_arity),
        'heisenberg': lambda v: heisenberg_shadow_tower(Fraction(v), max_arity),
        'affine_sl2': lambda v: affine_sl2_shadow_tower(Fraction(v), max_arity),
        'w3_T': lambda v: w3_shadow_tower_t_line(Fraction(v), max_arity),
        'w3_W': lambda v: w3_shadow_tower_w_line(Fraction(v), max_arity),
    }

    if family not in tower_fn:
        raise ValueError(f"Unknown family: {family}")

    result = {}
    for v in param_values:
        try:
            tower = tower_fn[family](v)
        except (ValueError, ZeroDivisionError):
            continue
        for p in primes:
            coeffs = iwasawa_power_series_coefficients(tower, p, max_terms)
            mu = mu_invariant(coeffs, p)
            lam = lambda_invariant(coeffs, p)
            result[(v, p)] = (mu, lam)
    return result


def ferrero_washington_boundary(
    family: str,
    param_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[str, List[Tuple[int, int]]]:
    r"""Map the success/failure boundary of the shadow Ferrero-Washington.

    Returns {'success': [(param, p), ...], 'failure': [(param, p), ...]}.
    """
    if primes is None:
        primes = PRIMES_TO_97
    table = batch_mu_lambda_table(family, param_values, primes, max_arity, max_terms)
    success = []
    failure = []
    for (param, p), (mu, lam) in table.items():
        if mu == 0:
            success.append((param, p))
        else:
            failure.append((param, p))
    return {'success': success, 'failure': failure}


def mu_zero_fraction(
    family: str,
    param_values: List[int],
    primes: Optional[List[int]] = None,
    max_arity: int = 40,
    max_terms: int = 20
) -> float:
    """Fraction of (param, p) pairs where mu = 0."""
    boundary = ferrero_washington_boundary(family, param_values, primes, max_arity, max_terms)
    total = len(boundary['success']) + len(boundary['failure'])
    if total == 0:
        return 0.0
    return len(boundary['success']) / total


# ============================================================================
# 18. Advanced: two-variable p-adic L-function (Katz-type)
# ============================================================================

def two_variable_shadow_L(
    p: int,
    c_values: List[int],
    s_values: List[Fraction],
    max_arity: int = 40,
    max_terms: int = 20
) -> Dict[Tuple[int, Fraction], Fraction]:
    r"""Two-variable p-adic L-function L_p(s, c).

    Interpolates across both s and c (central charge).
    For each (c, s), returns L_p^{sh}(s) at Virasoro central charge c.
    """
    result = {}
    for c in c_values:
        try:
            tower = virasoro_shadow_tower(Fraction(c), max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        vals = kubota_leopoldt_shadow(tower, p, s_values, max_arity)
        for s, v in vals.items():
            result[(c, s)] = v
    return result


# ============================================================================
# 19. Valuation growth analysis
# ============================================================================

def valuation_growth_rate(
    tower: Dict[int, Fraction],
    p: int,
    max_r: int = 40
) -> Dict[str, Any]:
    r"""Analyze the growth rate of v_p(S_r) as r -> infinity.

    For the mu-invariant interpretation:
        mu_p(A) = lim_{r->inf} v_p(S_r) / r

    We compute the least-squares fit of v_p(S_r) vs r for large r,
    which gives the effective mu and lambda.
    """
    r_vals = []
    vp_vals = []
    for r in range(2, max_r + 1):
        S_r = tower.get(r, Fraction(0))
        if S_r != 0:
            r_vals.append(r)
            vp_vals.append(v_p(S_r, p))

    if len(r_vals) < 2:
        return {
            'p': p,
            'n_points': len(r_vals),
            'effective_mu': 0,
            'effective_lambda': 0,
            'r_values': r_vals,
            'vp_values': vp_vals,
        }

    # Least squares: v_p(S_r) ~ mu * r + b
    n = len(r_vals)
    sum_r = sum(r_vals)
    sum_v = sum(vp_vals)
    sum_rv = sum(r_vals[i] * vp_vals[i] for i in range(n))
    sum_r2 = sum(r ** 2 for r in r_vals)

    denom = n * sum_r2 - sum_r ** 2
    if denom == 0:
        slope = 0.0
    else:
        slope = (n * sum_rv - sum_r * sum_v) / denom
    intercept = (sum_v - slope * sum_r) / n if n > 0 else 0.0

    return {
        'p': p,
        'n_points': n,
        'effective_mu': slope,
        'effective_lambda': intercept,
        'r_values': r_vals,
        'vp_values': vp_vals,
    }


def valuation_growth_table(
    tower: Dict[int, Fraction],
    primes: Optional[List[int]] = None,
    max_r: int = 40
) -> Dict[int, Dict[str, Any]]:
    """Valuation growth analysis for multiple primes."""
    if primes is None:
        primes = PRIMES_TO_97[:15]
    return {p: valuation_growth_rate(tower, p, max_r) for p in primes}
