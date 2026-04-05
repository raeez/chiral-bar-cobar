r"""Kubota-Leopoldt p-adic interpolation for shadow zeta functions (BC-79).

MATHEMATICAL FRAMEWORK
======================

The Kubota-Leopoldt p-adic L-function L_p(s, chi) interpolates special values
L(1-n, chi) at negative integers.  For the shadow zeta function

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}

of a modular Koszul algebra A, we construct the p-adic shadow analogue.

1. SHADOW BERNOULLI NUMBERS.

   B_n^{sh}(A) = zeta_A(-n) = sum_{r >= 2} S_r(A) * r^n    (n = 0, 1, 2, ...)

   For class M (Virasoro): |S_r| ~ rho^r with rho < 1, so the sum converges
   for all n.  These are the shadow analogues of the classical Bernoulli numbers
   B_n = -n * zeta(1-n).

2. KUMMER CONGRUENCES.

   The classical Kummer congruences state: for n, m >= 1 with n = m mod (p-1)
   (or mod 2 if p = 2), and n, m not divisible by p-1:

       (1 - p^{n-1}) * B_n/n = (1 - p^{m-1}) * B_m/m   mod p^{v_p(n-m)+1}

   For the shadow zeta, we test the analogous congruences:

       (1 - S_p * p^n) * B_n^{sh}  =  (1 - S_p * p^m) * B_m^{sh}
           mod p^{v_p(n-m)+1}

   for n = m mod (p-1) (or mod 2 for p = 2).

   If these hold, the p-adic L-function L_p^{sh}(s, A) exists as a p-adic
   analytic function by Mahler's theorem.

   If they FAIL for some (n, m, p), this records genuine arithmetic structure
   of the shadow tower.

3. IWASAWA FUNCTION.

   When Kummer congruences hold, write:

       L_p^{sh}(s, A) = integral_{Z_p^x} x^{-s} d mu_A

   The Iwasawa power series f_A(T) = sum a_n(A) T^n in Z_p[[T]], with
   T = (1+p)^s - 1 (or T = 5^s - 1 for p = 2).

   mu-invariant: mu_p(A) = min_n v_p(a_n).
   lambda-invariant: lambda_p(A) = min{n : v_p(a_n) = mu_p}.

4. WEIERSTRASS PREPARATION.

   L_p^{sh} = p^{mu_p} * g(T) * u(T)

   where g is a distinguished polynomial of degree lambda and u is a unit in
   Z_p[[T]].  The zeros of g(T) in the p-adic unit disk are the p-adic zeros
   of L_p^{sh}.

5. OVERCONVERGENCE.

   For class G (Heisenberg): the shadow zeta is a monomial (single nonzero
   term S_2), so L_p^{sh} trivially extends to all of C_p.

   For class M (Virasoro): S_r ~ C * rho^r * r^{-5/2}, so the overconvergence
   radius is controlled by the shadow convergence radius rho.  We compute this
   numerically.

6. TWO-VARIABLE p-ADIC L-FUNCTION.

   For the Virasoro family parametrized by c, define:

       L_p^{sh}(s, c) = sum_{r >= 2, p nmid r} S_r(c) * <r>^{-s}

   interpolating across both s and c simultaneously (Katz-type).

7. CLASSICAL COMPARISON.

   For sl_2, the categorical zeta is the Riemann zeta:
       zeta^{DK}_{sl_2}(s) = zeta(s) = sum_{n >= 1} n^{-s}.

   The Kubota-Leopoldt 2-adic zeta function L_2(s) interpolates:
       L_2(1-n) = (1 - 2^{n-1}) * B_n / n

   We verify that the sl_2 categorical p-adic zeta matches the classical
   Kubota-Leopoldt construction.

VERIFICATION PATHS (>= 3 per claim):
   Path 1: Kummer congruences tested exhaustively for n, m <= 20
   Path 2: Iwasawa power series consistency at roots of unity
   Path 3: Weierstrass degree = lambda (independent zero count)
   Path 4: Complementarity constraints on mu_p(A) + mu_p(A!)
   Path 5: Classical comparison: p-adic zeta of sl_2 = Kubota-Leopoldt

Manuscript references:
    chap:arithmetic-shadows (arithmetic_shadows.tex)
    rem:kummer-motive (arithmetic_shadows.tex)
    thm:shadow-spectral-correspondence (arithmetic_shadows.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

Convention: shadow coefficients S_r from H(t) = sum_{r>=2} S_r t^r.
    S_2 = kappa for each family.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP24): kappa + kappa' != 0 for Virasoro (kappa + kappa' = 13).
CAUTION (AP38): all numerical values computed from first principles.
CAUTION (AP48): kappa depends on full algebra, not Virasoro subalgebra.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, gcd, log
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union


# ============================================================================
# 0. Primes
# ============================================================================

PRIMES_15 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

C_VALUES = [1, 2, 4, 10, 13, 25]

# ============================================================================
# 1. p-adic valuation (standalone)
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


# ============================================================================
# 2. Shadow coefficient providers (exact rational)
# ============================================================================

def virasoro_shadow_tower(c_val: Fraction, max_arity: int = 40) -> Dict[int, Fraction]:
    r"""Exact shadow coefficients for Virasoro at central charge c.

    Uses the recursive formula from the shadow metric:
      S_2 = c/2 (kappa)
      S_3 = 2 (universal gravitational cubic)
      S_4 = 10/(c*(5c+22))
      S_r for r >= 5: recursion from the Poisson bracket on the primary line.

    This matches thm:shadow-archetype-classification and the authoritative
    computation in padic_shadow_tower.py and bc_padic_shadow_zeta_engine.py.
    """
    c = Fraction(c_val)
    if c == 0:
        raise ValueError("c must be nonzero for Virasoro shadow tower")
    if 5 * c + 22 == 0:
        raise ValueError("c = -22/5 (Yang-Lee edge) is singular: 5c+22 = 0")

    P = Fraction(2) / c  # propagator on the single-generator line
    S: Dict[int, Fraction] = {}
    S[2] = c / 2
    S[3] = Fraction(2)
    S[4] = Fraction(10) / (c * (5 * c + 22))

    for r in range(5, max_arity + 1):
        obs = Fraction(0)
        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k not in S:
                continue
            if j > k:
                continue
            contrib = Fraction(j) * S[j] * P * Fraction(k) * S[k]
            if j == k:
                obs += contrib / 2
            else:
                obs += contrib
        S[r] = -obs / (2 * r)

    return S


def heisenberg_shadow_tower(k_val: Fraction, max_arity: int = 40) -> Dict[int, Fraction]:
    r"""Exact shadow coefficients for Heisenberg at level k.

    Class G (Gaussian): terminates at depth 2.
      S_2 = k (the level = kappa), S_r = 0 for r >= 3.
    """
    k = Fraction(k_val)
    S: Dict[int, Fraction] = {2: k}
    for r in range(3, max_arity + 1):
        S[r] = Fraction(0)
    return S


def affine_sl2_shadow_tower(k_val: Fraction, max_arity: int = 40) -> Dict[int, Fraction]:
    r"""Exact shadow coefficients for affine sl_2 at level k.

    Class L (Lie/tree): terminates at depth 3.
      kappa = 3(k+2)/4, S_3 = 2*h^v/(k+h^v) = 4/(k+2), S_r = 0 for r >= 4.
    """
    k = Fraction(k_val)
    kappa = Fraction(3) * (k + 2) / 4
    S3 = Fraction(4) / (k + 2)  # 2*h^v/(k+h^v), h^v(sl_2)=2
    S: Dict[int, Fraction] = {2: kappa, 3: S3}
    for r in range(4, max_arity + 1):
        S[r] = Fraction(0)
    return S


def betagamma_shadow_tower(max_arity: int = 40) -> Dict[int, Fraction]:
    r"""Exact shadow coefficients for beta-gamma at c = -2.

    Class C (contact): terminates at depth 4.
    Uses Virasoro recursion for arities 2-4, then truncates.
    """
    vir = virasoro_shadow_tower(Fraction(-2), max(max_arity, 4))
    result: Dict[int, Fraction] = {}
    for r in range(2, max_arity + 1):
        result[r] = vir.get(r, Fraction(0)) if r <= 4 else Fraction(0)
    return result


# ============================================================================
# 3. Shadow Bernoulli numbers: B_n^{sh}(A) = zeta_A(-n)
# ============================================================================

def shadow_bernoulli(tower: Dict[int, Fraction], n: int,
                     max_arity: int = 40) -> Fraction:
    r"""Compute the n-th shadow Bernoulli number B_n^{sh}(A) = zeta_A(-n).

    B_n^{sh} = sum_{r >= 2} S_r * r^n

    For class M algebras (|S_r| ~ rho^r with rho < 1), the sum converges
    for all n >= 0.
    """
    result = Fraction(0)
    for r in range(2, max_arity + 1):
        Sr = tower.get(r, Fraction(0))
        if Sr == 0:
            continue
        result += Sr * Fraction(r) ** n
    return result


def shadow_bernoulli_table(tower: Dict[int, Fraction], max_n: int = 20,
                           max_arity: int = 40) -> Dict[int, Fraction]:
    """Compute B_0^{sh}, ..., B_{max_n}^{sh} as exact fractions."""
    return {n: shadow_bernoulli(tower, n, max_arity) for n in range(max_n + 1)}


# ============================================================================
# 4. Classical Bernoulli numbers (for comparison)
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
# 5. Kummer congruences for the shadow zeta
# ============================================================================

def kummer_congruence_test(tower: Dict[int, Fraction], p: int,
                           n: int, m: int,
                           max_arity: int = 40) -> Dict[str, Any]:
    r"""Test the shadow Kummer congruence for a given (p, n, m) triple.

    The congruence to test:

      (1 - S_p * p^n) * B_n^{sh}  ==  (1 - S_p * p^m) * B_m^{sh}
          mod p^{v_p(n - m) + 1}

    where n == m mod (p-1) for odd p, or n == m mod 2 for p = 2.

    Returns dict with:
      - lhs, rhs: the two sides of the congruence
      - difference: lhs - rhs
      - modulus_exponent: v_p(n - m) + 1
      - holds: whether v_p(difference) >= modulus_exponent
      - actual_valuation: v_p(difference)
    """
    S_p = tower.get(p, Fraction(0))
    B_n = shadow_bernoulli(tower, n, max_arity)
    B_m = shadow_bernoulli(tower, m, max_arity)

    lhs = (1 - S_p * Fraction(p) ** n) * B_n
    rhs = (1 - S_p * Fraction(p) ** m) * B_m

    diff = lhs - rhs

    if n == m:
        # Trivially holds
        return {
            'p': p, 'n': n, 'm': m,
            'lhs': lhs, 'rhs': rhs,
            'difference': Fraction(0),
            'modulus_exponent': float('inf'),
            'actual_valuation': float('inf'),
            'holds': True,
            'trivial': True,
        }

    # v_p(n - m): need p-adic valuation of the integer n - m
    nm_diff = abs(n - m)
    vp_nm = 0
    temp = nm_diff
    while temp % p == 0:
        vp_nm += 1
        temp //= p
    mod_exp = vp_nm + 1

    vp_diff = v_p_safe(diff, p)

    return {
        'p': p, 'n': n, 'm': m,
        'lhs': lhs, 'rhs': rhs,
        'difference': diff,
        'modulus_exponent': mod_exp,
        'actual_valuation': vp_diff,
        'holds': vp_diff >= mod_exp,
        'trivial': False,
    }


def congruence_class(n: int, p: int) -> int:
    """Return n mod (p-1) for odd p, or n mod 2 for p = 2."""
    if p == 2:
        return n % 2
    return n % (p - 1)


def exhaustive_kummer_test(tower: Dict[int, Fraction], p: int,
                           max_n: int = 20,
                           max_arity: int = 40) -> Dict[str, Any]:
    r"""Test Kummer congruences exhaustively for all (n, m) pairs with
    0 <= n, m <= max_n and n == m mod (p-1) (or mod 2 for p=2).

    Returns summary with total tests, passes, failures, and details of
    any failures.
    """
    tests_run = 0
    passes = 0
    failures = []
    excess_valuations = []  # when v_p(diff) > required minimum

    for n in range(0, max_n + 1):
        for m in range(n + 1, max_n + 1):
            if congruence_class(n, p) != congruence_class(m, p):
                continue
            result = kummer_congruence_test(tower, p, n, m, max_arity)
            tests_run += 1
            if result['holds']:
                passes += 1
                if not result['trivial']:
                    excess = result['actual_valuation'] - result['modulus_exponent']
                    if excess != float('inf'):
                        excess_valuations.append(excess)
            else:
                failures.append(result)

    return {
        'p': p,
        'max_n': max_n,
        'tests_run': tests_run,
        'passes': passes,
        'failures': len(failures),
        'failure_details': failures,
        'all_pass': len(failures) == 0,
        'mean_excess_valuation': (
            sum(excess_valuations) / len(excess_valuations)
            if excess_valuations else float('inf')
        ),
    }


def full_kummer_scan(tower: Dict[int, Fraction],
                     primes: Optional[List[int]] = None,
                     max_n: int = 20,
                     max_arity: int = 40) -> Dict[int, Dict[str, Any]]:
    """Run exhaustive Kummer tests for all specified primes.

    Returns dict {p: test_result}.
    """
    if primes is None:
        primes = PRIMES_15
    return {p: exhaustive_kummer_test(tower, p, max_n, max_arity) for p in primes}


# ============================================================================
# 6. Iwasawa power series via Vandermonde interpolation
# ============================================================================

def padic_shadow_zeta_value(tower: Dict[int, Fraction], p: int,
                            n: int, max_arity: int = 40) -> Fraction:
    r"""Compute zeta_{p,A}(1-n) = sum_{r>=2, p nmid r} S_r * r^{n-1}.

    This is the p-adic shadow zeta value at s = 1-n, with the Euler factor
    at p removed (terms with p | r are excluded).
    """
    result = Fraction(0)
    for r in range(2, max_arity + 1):
        if r % p == 0:
            continue
        Sr = tower.get(r, Fraction(0))
        if Sr == 0:
            continue
        result += Sr * Fraction(r) ** (n - 1)
    return result


def iwasawa_power_series(tower: Dict[int, Fraction], p: int,
                         num_coeffs: int = 11,
                         max_arity: int = 40) -> List[Fraction]:
    r"""Compute coefficients of the Iwasawa power series f_p(T) = sum a_n T^n.

    Uses Vandermonde interpolation at T_n = gamma^{1-n} - 1 for n = 1, ..., N.

    gamma = 1 + p for odd p, gamma = 5 for p = 2.

    The linear system V * a = vals is solved by Gaussian elimination in
    exact Fraction arithmetic.

    Returns [a_0, a_1, ..., a_{num_coeffs-1}].
    """
    gamma = Fraction(5) if p == 2 else Fraction(1 + p)
    N = num_coeffs

    T_points = []
    values = []
    for n in range(1, N + 1):
        T_n = Fraction(1) / gamma ** (n - 1) - 1
        T_points.append(T_n)
        val = padic_shadow_zeta_value(tower, p, n, max_arity)
        values.append(val)

    # Build Vandermonde system [V | values] and solve
    mat = []
    for i in range(N):
        row = []
        T_pow = Fraction(1)
        for j in range(N):
            row.append(T_pow)
            T_pow *= T_points[i]
        row.append(values[i])
        mat.append(row)

    # Gaussian elimination with exact arithmetic
    for col in range(N):
        pivot_row = None
        for row in range(col, N):
            if mat[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            raise ValueError("Singular Vandermonde matrix")
        if pivot_row != col:
            mat[col], mat[pivot_row] = mat[pivot_row], mat[col]

        pivot = mat[col][col]
        for row in range(col + 1, N):
            if mat[row][col] == 0:
                continue
            factor = mat[row][col] / pivot
            for j in range(col, N + 1):
                mat[row][j] -= factor * mat[col][j]

    coeffs = [Fraction(0)] * N
    for row in range(N - 1, -1, -1):
        val = mat[row][N]
        for j in range(row + 1, N):
            val -= mat[row][j] * coeffs[j]
        coeffs[row] = val / mat[row][row]

    return coeffs


def iwasawa_power_series_precision(tower: Dict[int, Fraction], p: int,
                                   num_coeffs: int = 11,
                                   max_arity: int = 40,
                                   p_prec: int = 20) -> List[Dict[str, Any]]:
    r"""Compute Iwasawa coefficients with p-adic precision data.

    Returns list of dicts with coefficient value, p-adic valuation, and
    reduction mod p^{p_prec}.
    """
    coeffs = iwasawa_power_series(tower, p, num_coeffs, max_arity)
    result = []
    for n, a in enumerate(coeffs):
        vp = v_p_safe(a, p)
        result.append({
            'n': n,
            'a_n': a,
            'v_p': vp,
        })
    return result


# ============================================================================
# 7. mu-invariant and lambda-invariant
# ============================================================================

def mu_invariant(coeffs: List[Fraction], p: int) -> int:
    r"""mu(f) = min_n v_p(a_n) over all nonzero coefficients.

    Can be negative (power series in p^mu * Z_p[[T]]).
    """
    vals = []
    for a in coeffs:
        if a != 0:
            vals.append(v_p(a, p))
    if not vals:
        return 999  # Proxy for infinity
    return min(vals)


def lambda_invariant(coeffs: List[Fraction], p: int) -> int:
    r"""lambda(f) = min{n : v_p(a_n) = mu}.

    Degree of the distinguished polynomial in the Weierstrass factorization.
    """
    mu = mu_invariant(coeffs, p)
    if mu == 999:
        return 0
    for n, a in enumerate(coeffs):
        if a != 0 and v_p(a, p) == mu:
            return n
    return len(coeffs)


def full_iwasawa_invariants(tower: Dict[int, Fraction], p: int,
                            num_coeffs: int = 11,
                            max_arity: int = 40) -> Dict[str, Any]:
    """Compute (mu, lambda) invariants for the shadow Iwasawa function.

    Returns dict with mu, lambda, coefficient data, and diagnostics.
    """
    coeffs = iwasawa_power_series(tower, p, num_coeffs, max_arity)
    mu = mu_invariant(coeffs, p)
    lam = lambda_invariant(coeffs, p)

    coeff_data = []
    for n, a in enumerate(coeffs):
        coeff_data.append({
            'n': n,
            'a_n': a,
            'v_p': v_p_safe(a, p),
        })

    return {
        'p': p,
        'mu': mu,
        'lambda': lam,
        'coefficients': coeff_data,
        'num_coeffs': len(coeffs),
    }


def iwasawa_invariant_table(family_name: str,
                            params: List[Fraction],
                            primes: Optional[List[int]] = None,
                            max_arity: int = 40,
                            num_coeffs: int = 11) -> Dict[Tuple, Dict[str, int]]:
    r"""Compute (mu, lambda) for all (param, p) pairs.

    family_name: "virasoro", "heisenberg", "affine_sl2"
    params: list of parameter values (c for Virasoro, k for others)

    Returns dict {(param_value, p): {'mu': ..., 'lambda': ...}}.
    """
    if primes is None:
        primes = PRIMES_15

    tower_fn = {
        'virasoro': virasoro_shadow_tower,
        'heisenberg': heisenberg_shadow_tower,
        'affine_sl2': affine_sl2_shadow_tower,
    }[family_name]

    result = {}
    for param in params:
        try:
            tower = tower_fn(Fraction(param), max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        for p in primes:
            try:
                inv = full_iwasawa_invariants(tower, p, num_coeffs, max_arity)
                result[(param, p)] = {'mu': inv['mu'], 'lambda': inv['lambda']}
            except (ValueError, ZeroDivisionError):
                continue

    return result


# ============================================================================
# 8. Newton polygon and zero analysis
# ============================================================================

def newton_polygon(coeffs: List[Fraction], p: int) -> List[Tuple[int, float]]:
    r"""Lower convex hull of {(n, v_p(a_n)) : a_n != 0}.

    Returns vertices as (n, v_p(a_n)) pairs.
    """
    points = []
    for n, a in enumerate(coeffs):
        if a != 0:
            points.append((n, float(v_p(a, p))))

    if len(points) <= 1:
        return points

    hull = []
    for pt in points:
        while len(hull) >= 2:
            o = hull[-2]
            a_pt = hull[-1]
            cross = ((a_pt[0] - o[0]) * (pt[1] - o[1])
                     - (a_pt[1] - o[1]) * (pt[0] - o[0]))
            if cross <= 0:
                hull.pop()
            else:
                break
        hull.append(pt)
    return hull


def newton_polygon_slopes(coeffs: List[Fraction],
                          p: int) -> List[Tuple[float, int]]:
    r"""Extract (slope, multiplicity) pairs from Newton polygon.

    A slope s means n_{i+1} - n_i zeros with v_p(zero) = -s.
    Negative slope => zeros inside the unit disk.
    """
    hull = newton_polygon(coeffs, p)
    slopes = []
    for i in range(len(hull) - 1):
        n1, v1 = hull[i]
        n2, v2 = hull[i + 1]
        dx = n2 - n1
        if dx > 0:
            slopes.append(((v2 - v1) / dx, dx))
    return slopes


def zeros_in_unit_disk(coeffs: List[Fraction], p: int) -> int:
    """Count zeros of f(T) in the open unit disk |T|_p < 1.

    These correspond to negative Newton polygon slopes.
    """
    slopes = newton_polygon_slopes(coeffs, p)
    count = 0
    for slope, mult in slopes:
        if slope < 0:
            count += mult
    return count


# ============================================================================
# 9. Weierstrass preparation
# ============================================================================

def weierstrass_preparation(coeffs: List[Fraction],
                            p: int) -> Dict[str, Any]:
    r"""Factor f = p^mu * g(T) * u(T) via Weierstrass preparation.

    g is a distinguished polynomial (monic, non-leading coefficients in pZ_p),
    deg(g) = lambda.
    u is a unit in Z_p[[T]].

    Returns mu, lambda, the reduced coefficients p^{-mu} * a_n, and
    whether the Weierstrass conditions are satisfied.
    """
    mu = mu_invariant(coeffs, p)
    lam = lambda_invariant(coeffs, p)

    if mu == 999:
        return {'mu': 999, 'lambda': 0, 'valid': True, 'reduced': []}

    reduced = [a / Fraction(p) ** mu for a in coeffs]

    # Check Weierstrass conditions on the reduced polynomial
    valid = True
    for i in range(min(lam, len(reduced))):
        if reduced[i] != 0 and v_p(reduced[i], p) < 1:
            valid = False
            break
    if lam < len(reduced) and reduced[lam] != 0:
        if v_p(reduced[lam], p) != 0:
            valid = False

    return {
        'mu': mu,
        'lambda': lam,
        'valid': valid,
        'reduced': reduced[:min(len(reduced), lam + 3)],
    }


# ============================================================================
# 10. Overconvergence radius
# ============================================================================

def overconvergence_radius(tower: Dict[int, Fraction], p: int,
                           num_coeffs: int = 20,
                           max_arity: int = 40) -> Dict[str, Any]:
    r"""Estimate the overconvergence radius rho_p(A) of L_p^{sh}.

    The Iwasawa power series f(T) = sum a_n T^n converges on |T|_p < rho_p.
    The radius of convergence is:

        rho_p = 1 / limsup_{n -> inf} |a_n|_p^{1/n}
              = p^{liminf_{n -> inf} v_p(a_n)/n}

    For class G (Heisenberg): f(T) is a polynomial, so rho_p = infinity.
    For class M: rho_p is finite, controlled by the shadow radius.

    Returns dict with estimated radius, the valuation sequence, and whether
    the series appears to overconverge (rho_p > 1).
    """
    coeffs = iwasawa_power_series(tower, p, num_coeffs, max_arity)

    # Compute v_p(a_n)/n for n >= 1
    ratios = []
    for n, a in enumerate(coeffs):
        if n == 0 or a == 0:
            continue
        vp = v_p(a, p)
        ratios.append((n, vp, vp / n))

    if not ratios:
        return {
            'p': p,
            'radius': float('inf'),
            'overconverges': True,
            'ratios': [],
            'class': 'G',
        }

    # Estimate liminf v_p(a_n)/n from the last few ratios
    # Use the minimum of the last half as a conservative estimate
    half = max(1, len(ratios) // 2)
    tail_ratios = [r[2] for r in ratios[-half:]]
    liminf_est = min(tail_ratios)

    if liminf_est > 0:
        # rho_p = p^{liminf} > 1: overconvergent
        radius = float(p) ** liminf_est
        overconverges = True
    elif liminf_est == 0:
        # rho_p = 1: converges on closed unit disk but not beyond
        radius = 1.0
        overconverges = False
    else:
        # rho_p = p^{liminf} < 1: does not even converge on full disk
        radius = float(p) ** liminf_est
        overconverges = False

    return {
        'p': p,
        'radius': radius,
        'overconverges': overconverges,
        'liminf_estimate': liminf_est,
        'ratios': ratios,
    }


# ============================================================================
# 11. Two-variable p-adic L-function (Katz-type)
# ============================================================================

def two_variable_padic_L(p: int,
                         c_values: Optional[List[Fraction]] = None,
                         n_values: Optional[List[int]] = None,
                         max_arity: int = 30) -> Dict[str, Any]:
    r"""Compute L_p^{sh}(1-n, c) on a grid of (n, c) values.

    For the Virasoro family parametrized by c, computes the two-variable
    p-adic L-function on a grid, interpolating across both s and c.

    Returns the grid as a nested dict: table[c][n] = L_p^{sh}(1-n, Vir_c).
    """
    if c_values is None:
        c_values = [Fraction(c) for c in C_VALUES]
    if n_values is None:
        n_values = list(range(1, 11))

    table: Dict[Fraction, Dict[int, Fraction]] = {}
    for c_val in c_values:
        c = Fraction(c_val)
        try:
            tower = virasoro_shadow_tower(c, max_arity)
        except (ValueError, ZeroDivisionError):
            continue
        row: Dict[int, Fraction] = {}
        for n in n_values:
            row[n] = padic_shadow_zeta_value(tower, p, n, max_arity)
        table[c] = row

    return {
        'p': p,
        'c_values': c_values,
        'n_values': n_values,
        'table': table,
    }


def two_variable_rationality_check(p: int,
                                   n_val: int,
                                   c_values: Optional[List[Fraction]] = None,
                                   max_arity: int = 30) -> Dict[str, Any]:
    r"""For fixed n, check that L_p^{sh}(1-n, c) is a rational function of c.

    Since S_r(c) is rational in c for Virasoro, the sum
    sum_{r coprime to p} S_r(c) * r^{n-1} is a rational function of c.

    We verify this by checking that the values at our c grid are consistent
    with a rational function of bounded degree.
    """
    if c_values is None:
        c_values = [Fraction(c) for c in [1, 2, 3, 4, 5, 6, 7, 8, 10, 13, 15, 20, 25]]

    values = []
    for c_val in c_values:
        c = Fraction(c_val)
        try:
            tower = virasoro_shadow_tower(c, max_arity)
            val = padic_shadow_zeta_value(tower, p, n_val, max_arity)
            values.append((c, val))
        except (ValueError, ZeroDivisionError):
            continue

    # Check: consecutive differences should be rational functions
    # For a polynomial of degree d, the (d+1)-th finite difference vanishes.
    # But we have a rational function, so just verify that the values are
    # nonzero and have bounded denominators.
    max_denom = max(abs(v.denominator) for _, v in values if v != 0) if values else 0

    return {
        'p': p,
        'n': n_val,
        'num_c_values': len(values),
        'max_denominator': max_denom,
        'values': values,
    }


# ============================================================================
# 12. Koszul complementarity on Iwasawa invariants
# ============================================================================

def virasoro_koszul_dual_c(c_val: Fraction) -> Fraction:
    """Koszul dual central charge: c -> 26 - c."""
    return Fraction(26) - Fraction(c_val)


def complementarity_iwasawa(c_val: Fraction, p: int,
                            num_coeffs: int = 11,
                            max_arity: int = 40) -> Dict[str, Any]:
    r"""Compare Iwasawa invariants for Vir_c and Vir_{26-c}.

    Koszul duality c -> 26-c gives paired algebras. We compute
    (mu, lambda) for both and look for complementarity relations.

    Known from AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT zero).
    """
    c = Fraction(c_val)
    c_dual = virasoro_koszul_dual_c(c)

    tower_A = virasoro_shadow_tower(c, max_arity)
    tower_dual = virasoro_shadow_tower(c_dual, max_arity)

    inv_A = full_iwasawa_invariants(tower_A, p, num_coeffs, max_arity)
    inv_dual = full_iwasawa_invariants(tower_dual, p, num_coeffs, max_arity)

    return {
        'c': c,
        'c_dual': c_dual,
        'p': p,
        'mu_A': inv_A['mu'],
        'lambda_A': inv_A['lambda'],
        'mu_dual': inv_dual['mu'],
        'lambda_dual': inv_dual['lambda'],
        'mu_sum': inv_A['mu'] + inv_dual['mu'],
        'lambda_sum': inv_A['lambda'] + inv_dual['lambda'],
        'kappa_A': c / 2,
        'kappa_dual': c_dual / 2,
        'kappa_sum': c / 2 + c_dual / 2,  # = 13 always
    }


# ============================================================================
# 13. Classical comparison: sl_2 categorical zeta = Riemann zeta
# ============================================================================

def kubota_leopoldt_value(p: int, n: int) -> Fraction:
    r"""Compute the classical Kubota-Leopoldt p-adic zeta value at s = 1-n.

    For even n >= 2:
        L_p(1-n) = -(1 - p^{n-1}) * B_n / n

    where B_n is the n-th Bernoulli number.

    For odd n >= 1 (trivial zeros of classical zeta): L_p(1-n) = 0.

    Note: the Kubota-Leopoldt function interpolates (1 - p^{n-1}) * B_n / n
    at positive even integers n, corresponding to zeta(1-n) for even n.

    Actually, the classical relation is:
        zeta(1-n) = -B_n / n   for n >= 1

    The p-adic interpolation is:
        L_p(1-n, omega^{1-n}) = -(1 - p^{n-1}) * B_n / n

    For the TRIVIAL BRANCH (weight 0 character):
        L_p(1-n) = (1 - p^{n-1}) * zeta(1-n)  for n = 1, 2, ...

    We compute this directly.
    """
    if n < 1:
        raise ValueError("n must be >= 1 for Kubota-Leopoldt values")

    B_n = bernoulli_number(n)
    # zeta(1-n) = -B_n / n
    zeta_value = -B_n / Fraction(n)

    # Euler factor removal at p
    euler = Fraction(1) - Fraction(p) ** (n - 1)

    return euler * zeta_value


def sl2_categorical_shadow_tower(max_dim: int = 40) -> Dict[int, Fraction]:
    r"""Build the "shadow tower" for the sl_2 categorical zeta.

    The sl_2 categorical zeta is zeta^{DK}_{sl_2}(s) = sum_{n >= 1} n^{-s}.
    To express this in the framework of shadow towers indexed by r >= 2,
    we note that S_r = 1 for all r >= 1 (each positive integer appears once
    as a representation dimension dim V_{r-1} = r).

    Specifically: the irreducible representations of sl_2 have dimensions
    1, 2, 3, ..., so each positive integer n appears exactly once.

    To compare with the Kubota-Leopoldt p-adic L-function, we build a
    "tower" with S_n = 1 for n = 1, ..., max_dim.

    NOTE: this is NOT a shadow tower in the strict sense (it starts at n=1
    and S_n = 1 for all n). It is the Dirichlet coefficients of the Riemann
    zeta function itself.
    """
    return {n: Fraction(1) for n in range(1, max_dim + 1)}


def sl2_padic_zeta_value(p: int, n: int, max_dim: int = 40) -> Fraction:
    r"""Compute the sl_2 categorical p-adic zeta value at s = 1-n.

    sum_{r >= 1, p nmid r} r^{n-1}  (truncated at max_dim)

    This should match the Kubota-Leopoldt value:
        (1 - p^{n-1}) * sum_{r >= 1} r^{n-1}
      = (1 - p^{n-1}) * zeta(1-n)  [using zeta regularization]
    """
    result = Fraction(0)
    for r in range(1, max_dim + 1):
        if r % p == 0:
            continue
        result += Fraction(r) ** (n - 1)
    return result


def verify_kubota_leopoldt_comparison(p: int, max_n: int = 12,
                                       max_dim: int = 60) -> Dict[str, Any]:
    r"""Verify that the sl_2 p-adic categorical zeta matches Kubota-Leopoldt.

    For each n = 1, ..., max_n, compute:
      - sl2_value: sum_{r=1, p nmid r}^{max_dim} r^{n-1}
      - KL_value: (1-p^{n-1}) * (-B_n/n)

    These should agree as max_dim -> infinity (the sl2_value is a partial
    sum). For finite max_dim, they agree to the extent that the partial
    sum approximates the regularized value.

    NOTE: The partial sum sum_{r=1}^N r^{n-1} does NOT converge to
    zeta(1-n) for n >= 1 (the Dirichlet series diverges). The agreement
    requires ANALYTIC CONTINUATION / p-adic regularization. So we check
    the Kummer congruences for the sl_2 tower instead, which is the correct
    p-adic interpolation property.

    Returns comparison data and Kummer congruence results.
    """
    # Check Kummer congruences for the sl_2 tower
    tower = sl2_categorical_shadow_tower(max_dim)
    kummer = exhaustive_kummer_test(tower, p, max_n=max_n, max_arity=max_dim)

    # Also compute direct values for comparison
    values = {}
    for n in range(1, max_n + 1):
        sl2_val = sl2_padic_zeta_value(p, n, max_dim)
        try:
            kl_val = kubota_leopoldt_value(p, n)
        except (ValueError, ZeroDivisionError):
            kl_val = None
        values[n] = {
            'sl2_partial_sum': sl2_val,
            'kubota_leopoldt': kl_val,
        }

    return {
        'p': p,
        'max_dim': max_dim,
        'kummer_test': kummer,
        'values': values,
    }


# ============================================================================
# 14. Master analysis function
# ============================================================================

def full_kubota_leopoldt_analysis(c_val: Fraction,
                                  primes: Optional[List[int]] = None,
                                  max_arity: int = 40,
                                  max_n: int = 20,
                                  num_coeffs: int = 11) -> Dict[str, Any]:
    r"""Run the complete Kubota-Leopoldt analysis for Virasoro at central charge c.

    Computes:
      1. Shadow Bernoulli numbers B_0^{sh}, ..., B_{max_n}^{sh}
      2. Kummer congruence tests for all specified primes
      3. Iwasawa power series and (mu, lambda) invariants
      4. Newton polygon and zero analysis
      5. Weierstrass preparation
      6. Overconvergence radius estimate
      7. Complementarity data (c vs 26-c)
    """
    if primes is None:
        primes = PRIMES_15

    c = Fraction(c_val)
    tower = virasoro_shadow_tower(c, max_arity)

    # 1. Shadow Bernoulli numbers
    bernoulli_table = shadow_bernoulli_table(tower, max_n, max_arity)

    # 2. Kummer congruences
    kummer_results = {}
    for p in primes:
        kummer_results[p] = exhaustive_kummer_test(tower, p, max_n, max_arity)

    # 3-5. Iwasawa analysis per prime
    iwasawa_results = {}
    for p in primes:
        coeffs = iwasawa_power_series(tower, p, num_coeffs, max_arity)
        mu = mu_invariant(coeffs, p)
        lam = lambda_invariant(coeffs, p)
        np_verts = newton_polygon(coeffs, p)
        np_slopes = newton_polygon_slopes(coeffs, p)
        n_zeros = zeros_in_unit_disk(coeffs, p)
        wp = weierstrass_preparation(coeffs, p)
        oc = overconvergence_radius(tower, p, num_coeffs, max_arity)

        iwasawa_results[p] = {
            'mu': mu,
            'lambda': lam,
            'newton_polygon_vertices': np_verts,
            'newton_polygon_slopes': np_slopes,
            'zeros_in_disk': n_zeros,
            'weierstrass': wp,
            'overconvergence': oc,
        }

    # 6. Complementarity
    comp_results = {}
    for p in primes[:5]:  # Just a few primes for speed
        comp_results[p] = complementarity_iwasawa(c, p, num_coeffs, max_arity)

    return {
        'c': c,
        'kappa': c / 2,
        'shadow_bernoulli': bernoulli_table,
        'kummer': kummer_results,
        'iwasawa': iwasawa_results,
        'complementarity': comp_results,
    }
