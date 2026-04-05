r"""bc_stark_shadow_engine.py -- Stark-type conjectures for shadow zeta functions.

BC-77: Stark regulators, class number formulae, BSD-type central values,
and Gross-Zagier height pairings for shadow zeta functions of modular
Koszul algebras.

MATHEMATICAL CONTENT
====================

Stark's conjecture: the leading Taylor coefficient of an L-function at
s=0 is (up to an algebraic factor) a regulator -- a determinant of
logarithms of algebraic units.  For the shadow zeta function

    zeta_A(s) = sum_{r >= 2} S_r(A) r^{-s}

we develop the analogous programme.

=== 1. TAYLOR EXPANSION AT s=0 ===

zeta_A^{(k)}(0) = sum_{r >= 2} S_r (-log r)^k

For class G/L/C (finite shadow towers), these are finite sums and
manifestly algebraic in the OPE data.  For class M (Virasoro, W_N),
|S_r| ~ C rho^r r^{-5/2} with rho < 1, so the series converges
absolutely (in fact exponentially) for all k >= 0.

=== 2. ORDER OF VANISHING ===

r_A = ord_{s=0} zeta_A(s).

Since class M shadow zeta functions are entire (rho < 1 implies
sigma_c = -infinity), s=0 is an ordinary point and r_A is the
multiplicity of s=0 as a zero of the entire function zeta_A(s).

For Heisenberg H_k: zeta(s) = k 2^{-s}, so zeta(0) = k != 0, r_A = 0.
For affine sl_2 at level k: zeta(0) = kappa + alpha != 0 generically, r_A = 0.

=== 3. SHADOW REGULATOR ===

R_A = lim_{s -> 0} zeta_A(s) / s^{r_A}.

This is the "leading coefficient" at s=0 -- the shadow analogue of the
Stark regulator.  We compute R_A to high precision and use PSLQ/LLL
to test for algebraic relations with pi, log(2), log(3), zeta(2), zeta(3).

=== 4. SHADOW CLASS NUMBER FORMULA ===

At s=1, the classical Dedekind zeta formula is:
    zeta_K(s) ~ h R w^{-1} |d_K|^{-1/2}

Shadow analogue:
    zeta_A(1) = sum_{r >= 2} S_r / r

Converges since |S_r| ~ rho^r.  Complementarity at s=1:
    zeta_A(1) + zeta_{A!}(1) for Koszul dual pairs.

=== 5. BSD-TYPE CENTRAL VALUE ===

zeta_A(1/2) = sum_{r >= 2} S_r r^{-1/2}

We test whether zeta_A(1/2) = 0 for some c ("shadow analytic rank >= 1"),
and whether sgn(zeta_A(1/2)) correlates with algebraic invariants.

=== 6. GROSS-ZAGIER TYPE ===

zeta'_A(1/2) = -sum_{r >= 2} S_r log(r) r^{-1/2}

Test for a "shadow height pairing" h_A such that
    zeta'_A(1/2) = const * h_A.

=== 7. SPECIAL VALUES AT NEGATIVE INTEGERS ===

zeta_A(-n) = sum_{r >= 2} S_r r^n

The shadow analogues of Bernoulli numbers.  For class M these are
convergent infinite series (rho < 1).

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    prop:shadow-periods (arithmetic_shadows.tex)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
CAUTION (AP38): All numerical values computed from first principles.
CAUTION (AP10): Multi-path verification required -- never trust a single
    computation path.
"""

from __future__ import annotations

import math
from typing import Any, Callable, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# 0. Shadow coefficient providers (adapted from shadow_zeta_function_engine)
# ---------------------------------------------------------------------------

def heisenberg_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for Heisenberg H_k.

    S_2 = k (modular characteristic kappa = k).
    S_r = 0 for r >= 3 (class G).
    """
    result = {r: 0.0 for r in range(2, max_r + 1)}
    result[2] = float(k_val)
    return result


def affine_sl2_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for affine V_k(sl_2).

    kappa = dim(sl_2) * (k + h^v) / (2 h^v) = 3(k+2)/4.
    S_3 = alpha = 2 h^v / (k + h^v) = 4/(k+2).
    S_r = 0 for r >= 4 (class L).
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {r: 0.0 for r in range(2, max_r + 1)}
    result[2] = kappa
    result[3] = alpha
    return result


def virasoro_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for Virasoro Vir_c via sqrt(Q_L) Taylor expansion.

    Uses H(t) = t^2 sqrt(Q_L(t)) with Q_L(t) = c^2 + 12c t + alpha(c) t^2
    where alpha(c) = (180c + 872)/(5c + 22).

    S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L).

    CAUTION: c = 0 and 5c + 22 = 0 are poles.
    """
    if abs(c_val) < 1e-15 or abs(5.0 * c_val + 22.0) < 1e-15:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    # Taylor coefficients of sqrt(Q_L(t)) = sum a_n t^n
    # sqrt(q0 + q1 t + q2 t^2) = a0 + a1 t + a2 t^2 + ...
    a0 = abs(c_val)  # sqrt(c^2) = |c|

    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2.0 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))

    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))

    result = {}
    for n in range(len(a)):
        r = n + 2
        result[r] = a[n] / float(r)

    # Fill remaining with zeros
    for r in range(len(a) + 2, max_r + 1):
        result[r] = 0.0

    return result


def betagamma_shadow_coefficients(lam_val: float = 0.5, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for beta-gamma at weight lambda.

    c = 2(6 lambda^2 - 6 lambda + 1), kappa = c/2.
    S_3 = 2, S_4 = 10/(c(5c+22)), S_r = 0 for r >= 5 (class C).
    """
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0

    result = {r: 0.0 for r in range(2, max_r + 1)}
    result[2] = kappa
    result[3] = 2.0
    if abs(c_val) > 1e-15 and abs(5.0 * c_val + 22.0) > 1e-15:
        result[4] = 10.0 / (c_val * (5.0 * c_val + 22.0))
    return result


# ---------------------------------------------------------------------------
# 1. Taylor expansion at s=0
# ---------------------------------------------------------------------------

def shadow_zeta_taylor_at_zero(
    shadow_coeffs: Dict[int, float],
    max_deriv: int = 10,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Compute zeta_A^{(k)}(0) for k = 0, 1, ..., max_deriv.

    zeta_A^{(k)}(0) = sum_{r >= 2} S_r (-log r)^k

    Returns dict {k: zeta_A^{(k)}(0)}.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    results = {}
    for k in range(max_deriv + 1):
        total = 0.0
        for r in range(2, max_r + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            total += Sr * (-math.log(r)) ** k
        results[k] = total
    return results


def shadow_zeta_taylor_at_zero_hp(
    shadow_coeffs: Dict[int, float],
    max_deriv: int = 10,
    max_r: Optional[int] = None,
    dps: int = 50,
) -> Dict[int, Any]:
    """High-precision Taylor coefficients using mpmath.

    Returns dict {k: mpf value at dps precision}.
    """
    try:
        import mpmath
    except ImportError:
        raise ImportError("mpmath required for high-precision computation")

    mpmath.mp.dps = dps
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    results = {}
    for k in range(max_deriv + 1):
        total = mpmath.mpf(0)
        for r in range(2, max_r + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            total += mpmath.mpf(Sr) * (-mpmath.log(r)) ** k
        results[k] = total
    return results


# ---------------------------------------------------------------------------
# 2. Order of vanishing at s=0
# ---------------------------------------------------------------------------

def order_of_vanishing_at_zero(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
    tol: float = 1e-12,
) -> int:
    """Compute r_A = ord_{s=0} zeta_A(s).

    Since zeta_A is entire for class M (rho < 1), r_A is the multiplicity
    of s=0 as a zero.  We compute via Taylor coefficients: r_A = min{k :
    zeta_A^{(k)}(0) != 0}.

    Note zeta_A^{(k)}(0) / k! is the Taylor coefficient of s^k.
    """
    taylor = shadow_zeta_taylor_at_zero(shadow_coeffs, max_deriv=20, max_r=max_r)
    for k in range(21):
        if abs(taylor[k]) > tol:
            return k
    return 20  # Should not happen for nontrivial algebras


# ---------------------------------------------------------------------------
# 3. Shadow regulator
# ---------------------------------------------------------------------------

def shadow_regulator(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
    tol: float = 1e-12,
) -> Tuple[float, int]:
    """Compute the shadow regulator R_A = lim_{s->0} zeta_A(s) / s^{r_A}.

    Returns (R_A, r_A) where r_A is the order of vanishing.

    R_A = zeta_A^{(r_A)}(0) / r_A!
    """
    taylor = shadow_zeta_taylor_at_zero(shadow_coeffs, max_deriv=20, max_r=max_r)
    r_A = 0
    for k in range(21):
        if abs(taylor[k]) > tol:
            r_A = k
            break
    else:
        return (0.0, 20)

    R_A = taylor[r_A] / math.factorial(r_A)
    return (R_A, r_A)


def shadow_regulator_hp(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
    dps: int = 50,
) -> Tuple[Any, int]:
    """High-precision shadow regulator using mpmath.

    Returns (R_A as mpf, r_A).
    """
    try:
        import mpmath
    except ImportError:
        raise ImportError("mpmath required")

    mpmath.mp.dps = dps
    taylor = shadow_zeta_taylor_at_zero_hp(shadow_coeffs, max_deriv=20, max_r=max_r, dps=dps)

    r_A = 0
    for k in range(21):
        if abs(float(taylor[k])) > 10 ** (-(dps - 5)):
            r_A = k
            break
    else:
        return (mpmath.mpf(0), 20)

    R_A = taylor[r_A] / mpmath.factorial(r_A)
    return (R_A, r_A)


# ---------------------------------------------------------------------------
# 4. Shadow zeta evaluation at arbitrary s
# ---------------------------------------------------------------------------

def shadow_zeta_eval(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate zeta_A(s) = sum_{r >= 2} S_r r^{-s} by direct summation.

    For entire shadow zeta (rho < 1), this converges for all s.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * r ** (-s)
    return total


def shadow_zeta_eval_real(
    shadow_coeffs: Dict[int, float],
    s: float,
    max_r: Optional[int] = None,
) -> float:
    """Evaluate zeta_A(s) for real s."""
    val = shadow_zeta_eval(shadow_coeffs, complex(s, 0), max_r)
    return val.real


# ---------------------------------------------------------------------------
# 5. Shadow class number formula: zeta_A(1)
# ---------------------------------------------------------------------------

def shadow_class_number(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> float:
    """Compute the "shadow class number" zeta_A(1) = sum S_r / r.

    Converges since |S_r| ~ rho^r with rho < 1.
    """
    return shadow_zeta_eval_real(shadow_coeffs, 1.0, max_r)


def shadow_class_number_complementarity(
    shadow_coeffs_A: Dict[int, float],
    shadow_coeffs_A_dual: Dict[int, float],
    max_r: Optional[int] = None,
) -> Tuple[float, float, float]:
    """Compute zeta_A(1) + zeta_{A!}(1) for a Koszul dual pair.

    Returns (zeta_A(1), zeta_{A!}(1), sum).
    """
    z_A = shadow_class_number(shadow_coeffs_A, max_r)
    z_Ad = shadow_class_number(shadow_coeffs_A_dual, max_r)
    return (z_A, z_Ad, z_A + z_Ad)


# ---------------------------------------------------------------------------
# 6. BSD-type central value: zeta_A(1/2)
# ---------------------------------------------------------------------------

def shadow_central_value(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> float:
    """Compute zeta_A(1/2) = sum S_r / sqrt(r).

    The shadow analogue of the BSD central value.
    """
    return shadow_zeta_eval_real(shadow_coeffs, 0.5, max_r)


def shadow_central_derivative(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> float:
    """Compute zeta'_A(1/2) = -sum S_r log(r) / sqrt(r).

    The shadow analogue of a Gross-Zagier derivative.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * (-math.log(r)) / math.sqrt(r)
    return total


# ---------------------------------------------------------------------------
# 7. Special values at negative integers
# ---------------------------------------------------------------------------

def shadow_zeta_negative_integers(
    shadow_coeffs: Dict[int, float],
    max_n: int = 5,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Compute zeta_A(-n) = sum S_r r^n for n = 0, 1, ..., max_n.

    These are the shadow analogues of Bernoulli special values.
    For class M, convergent since |S_r| ~ rho^r with rho < 1.

    Returns dict {-n: zeta_A(-n)} for n = 0..max_n.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    results = {}
    for n in range(max_n + 1):
        total = 0.0
        for r in range(2, max_r + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            total += Sr * (r ** n)
        results[-n] = total
    return results


def shadow_zeta_positive_integers(
    shadow_coeffs: Dict[int, float],
    max_n: int = 10,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Compute zeta_A(n) = sum S_r r^{-n} for n = 1, 2, ..., max_n.

    Returns dict {n: zeta_A(n)}.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    results = {}
    for n in range(1, max_n + 1):
        results[n] = shadow_zeta_eval_real(shadow_coeffs, float(n), max_r)
    return results


# ---------------------------------------------------------------------------
# 8. Full special values table
# ---------------------------------------------------------------------------

def shadow_zeta_special_values_table(
    shadow_coeffs: Dict[int, float],
    s_range: Optional[List[int]] = None,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Compute zeta_A(n) for n in s_range (default: -5..10).

    Returns dict {n: zeta_A(n)}.
    """
    if s_range is None:
        s_range = list(range(-5, 11))

    results = {}
    for n in s_range:
        results[n] = shadow_zeta_eval_real(shadow_coeffs, float(n), max_r)
    return results


# ---------------------------------------------------------------------------
# 9. Finite-difference verification of Taylor coefficients
# ---------------------------------------------------------------------------

def shadow_zeta_taylor_finite_diff(
    shadow_coeffs: Dict[int, float],
    k: int,
    h: float = 1e-4,
    max_r: Optional[int] = None,
) -> float:
    """Verify zeta_A^{(k)}(0) by central finite differences.

    Uses the stencil for the k-th derivative at s=0 with step h.
    This provides an INDEPENDENT verification of the Taylor expansion.
    """
    if k == 0:
        return shadow_zeta_eval_real(shadow_coeffs, 0.0, max_r)
    elif k == 1:
        fp = shadow_zeta_eval_real(shadow_coeffs, h, max_r)
        fm = shadow_zeta_eval_real(shadow_coeffs, -h, max_r)
        return (fp - fm) / (2.0 * h)
    elif k == 2:
        fp = shadow_zeta_eval_real(shadow_coeffs, h, max_r)
        f0 = shadow_zeta_eval_real(shadow_coeffs, 0.0, max_r)
        fm = shadow_zeta_eval_real(shadow_coeffs, -h, max_r)
        return (fp - 2 * f0 + fm) / (h ** 2)
    elif k == 3:
        fp2 = shadow_zeta_eval_real(shadow_coeffs, 2 * h, max_r)
        fp1 = shadow_zeta_eval_real(shadow_coeffs, h, max_r)
        fm1 = shadow_zeta_eval_real(shadow_coeffs, -h, max_r)
        fm2 = shadow_zeta_eval_real(shadow_coeffs, -2 * h, max_r)
        return (fp2 - 2 * fp1 + 2 * fm1 - fm2) / (2 * h ** 3)
    elif k == 4:
        fp2 = shadow_zeta_eval_real(shadow_coeffs, 2 * h, max_r)
        fp1 = shadow_zeta_eval_real(shadow_coeffs, h, max_r)
        f0 = shadow_zeta_eval_real(shadow_coeffs, 0.0, max_r)
        fm1 = shadow_zeta_eval_real(shadow_coeffs, -h, max_r)
        fm2 = shadow_zeta_eval_real(shadow_coeffs, -2 * h, max_r)
        return (fp2 - 4 * fp1 + 6 * f0 - 4 * fm1 + fm2) / (h ** 4)
    else:
        # General central difference via Richardson-like approach
        # Use higher-order stencil for k-th derivative
        # Fallback: use binomial coefficients for central difference
        coeffs_stencil = _central_diff_coeffs(k)
        total = 0.0
        for j, c_j in coeffs_stencil:
            total += c_j * shadow_zeta_eval_real(shadow_coeffs, j * h, max_r)
        return total / (h ** k)


def _central_diff_coeffs(k: int) -> List[Tuple[int, float]]:
    """Central difference stencil coefficients for the k-th derivative.

    Returns list of (offset, coefficient) pairs.
    Uses the standard recursive formula for central differences.
    """
    # For k-th derivative, use 2*ceil(k/2)+1 point stencil
    # via binomial expansion of the central difference operator
    n = k + 2  # number of points on each side
    points = list(range(-n, n + 1))

    # Solve the Vandermonde system for k-th derivative
    import numpy as np  # type: ignore
    N = len(points)
    V = np.zeros((N, N))
    for i, p in enumerate(points):
        for j in range(N):
            V[i, j] = p ** j
    rhs = np.zeros(N)
    rhs[k] = math.factorial(k)

    try:
        coeffs = np.linalg.solve(V.T, rhs)
    except np.linalg.LinAlgError:
        # Fallback: simple forward difference
        return [(j, (-1.0) ** (k - j) * math.comb(k, j)) for j in range(k + 1)]

    result = []
    for i, p in enumerate(points):
        if abs(coeffs[i]) > 1e-15:
            result.append((p, float(coeffs[i])))
    return result


# ---------------------------------------------------------------------------
# 10. Convergence rate analysis
# ---------------------------------------------------------------------------

def convergence_analysis(
    shadow_coeffs: Dict[int, float],
    s: float,
    checkpoints: Optional[List[int]] = None,
) -> List[Tuple[int, float, float]]:
    """Analyze convergence of the partial sums of zeta_A(s).

    Returns list of (N, partial_sum_N, |term_N|) showing how quickly
    the series converges.
    """
    if checkpoints is None:
        max_r = max(shadow_coeffs.keys())
        checkpoints = [5, 10, 15, 20, 25, 30, 40, max_r]
        checkpoints = [n for n in checkpoints if n <= max_r]

    results = []
    partial = 0.0
    last_cp = 1
    for cp in checkpoints:
        for r in range(max(2, last_cp + 1), cp + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) > 1e-300:
                partial += Sr * r ** (-s)
        last_cp = cp
        Sr_cp = shadow_coeffs.get(cp, 0.0)
        term_size = abs(Sr_cp * cp ** (-s)) if abs(Sr_cp) > 1e-300 else 0.0
        results.append((cp, partial, term_size))

    return results


# ---------------------------------------------------------------------------
# 11. PSLQ / algebraic relation detection
# ---------------------------------------------------------------------------

def detect_algebraic_relations(
    value: float,
    constants: Optional[List[Tuple[str, float]]] = None,
    tol: float = 1e-10,
) -> Optional[Dict[str, Any]]:
    """Test whether `value` is a rational linear combination of standard
    mathematical constants.

    Uses mpmath.identify() for algebraic recognition, and a manual
    PSLQ-like search over the given basis.

    Returns dict with 'identified' string if found, else None.
    """
    try:
        import mpmath
    except ImportError:
        return None

    mpmath.mp.dps = 30
    x = mpmath.mpf(value)

    # Try mpmath.identify
    result = mpmath.identify(x, tol=tol)
    if result:
        return {'identified': result, 'value': float(x)}

    # Manual check against standard constants
    if constants is None:
        constants = [
            ('1', 1.0),
            ('pi', float(mpmath.pi)),
            ('pi^2', float(mpmath.pi ** 2)),
            ('log(2)', float(mpmath.log(2))),
            ('log(3)', float(mpmath.log(3))),
            ('zeta(2)', float(mpmath.pi ** 2 / 6)),
            ('zeta(3)', float(mpmath.zeta(3))),
            ('euler_gamma', float(mpmath.euler)),
        ]

    # Check if value is a simple rational multiple of any constant
    for name, c_val in constants:
        if abs(c_val) < 1e-30:
            continue
        ratio = value / c_val
        # Check if ratio is close to a simple rational p/q
        for q in range(1, 100):
            p = round(ratio * q)
            if abs(ratio - p / q) < tol:
                return {
                    'identified': f'{p}/{q} * {name}',
                    'value': float(x),
                    'p': p,
                    'q': q,
                    'constant': name,
                }

    return None


# ---------------------------------------------------------------------------
# 12. Complementarity at special values
# ---------------------------------------------------------------------------

def complementarity_at_s(
    c_val: float,
    s_val: float,
    max_r: int = 50,
) -> Dict[str, float]:
    """Compute zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) for complementarity test.

    For Virasoro: A = Vir_c, A! = Vir_{26-c}.
    kappa(A) + kappa(A!) = c/2 + (26-c)/2 = 13 (AP24).

    Returns dict with zeta_A, zeta_Ad, sum, and the S_2 sum.
    """
    coeffs_A = virasoro_shadow_coefficients(c_val, max_r)
    coeffs_Ad = virasoro_shadow_coefficients(26.0 - c_val, max_r)

    z_A = shadow_zeta_eval_real(coeffs_A, s_val, max_r)
    z_Ad = shadow_zeta_eval_real(coeffs_Ad, s_val, max_r)

    return {
        'zeta_A': z_A,
        'zeta_Ad': z_Ad,
        'sum': z_A + z_Ad,
        'kappa_A': c_val / 2.0,
        'kappa_Ad': (26.0 - c_val) / 2.0,
        'kappa_sum': 13.0,
        'c': c_val,
        's': s_val,
    }


def complementarity_special_values_sweep(
    c_values: List[float],
    s_values: List[float],
    max_r: int = 50,
) -> List[Dict[str, float]]:
    """Sweep complementarity over multiple c and s values."""
    results = []
    for c_val in c_values:
        for s_val in s_values:
            try:
                results.append(complementarity_at_s(c_val, s_val, max_r))
            except (ValueError, ZeroDivisionError):
                pass
    return results


# ---------------------------------------------------------------------------
# 13. Gross-Zagier type: shadow height pairing
# ---------------------------------------------------------------------------

def shadow_height_pairing_candidate(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[str, float]:
    """Compute candidate shadow height pairing from zeta'_A(1/2).

    We test whether zeta'_A(1/2) = const * ||Theta_A||^2 where
    ||Theta_A||^2 is a natural "norm" on the MC element.

    Natural candidates for ||Theta_A||^2:
    - sum S_r^2 (L^2 norm of shadow sequence)
    - sum S_r^2 / r (weighted L^2)
    - kappa^2 (leading term squared)

    Returns dict with computed values and ratios.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    zeta_prime_half = shadow_central_derivative(shadow_coeffs, max_r)
    kappa = shadow_coeffs.get(2, 0.0)

    l2_norm = sum(shadow_coeffs.get(r, 0.0) ** 2 for r in range(2, max_r + 1))
    weighted_l2 = sum(shadow_coeffs.get(r, 0.0) ** 2 / r for r in range(2, max_r + 1))

    result = {
        'zeta_prime_half': zeta_prime_half,
        'kappa': kappa,
        'kappa_squared': kappa ** 2,
        'l2_norm': l2_norm,
        'weighted_l2': weighted_l2,
    }

    if abs(kappa ** 2) > 1e-30:
        result['ratio_kappa2'] = zeta_prime_half / (kappa ** 2)
    if abs(l2_norm) > 1e-30:
        result['ratio_l2'] = zeta_prime_half / l2_norm
    if abs(weighted_l2) > 1e-30:
        result['ratio_wl2'] = zeta_prime_half / weighted_l2

    return result


# ---------------------------------------------------------------------------
# 14. Rationality tests for special values at negative integers
# ---------------------------------------------------------------------------

def rationality_test_negative_integers(
    shadow_coeffs: Dict[int, float],
    max_n: int = 5,
    max_r: Optional[int] = None,
    tol: float = 1e-8,
) -> Dict[int, Dict[str, Any]]:
    """Test whether zeta_A(-n) is rational for n = 0, 1, ..., max_n.

    The "shadow Klingen-Siegel" question: are these special values rational?

    For class G/L/C (finite towers): zeta_A(-n) is a FINITE sum of S_r r^n,
    and if S_r are rational then zeta_A(-n) is manifestly rational.

    For class M: infinite series. Rationality is a nontrivial constraint.

    Returns dict {-n: {'value': ..., 'is_rational': ..., 'fraction': ...}}.
    """
    neg_vals = shadow_zeta_negative_integers(shadow_coeffs, max_n, max_r)

    results = {}
    for n in range(max_n + 1):
        val = neg_vals[-n]
        info: Dict[str, Any] = {'value': val}

        # Test if val is close to a rational p/q with small denominator
        is_rational = False
        for q in range(1, 1000):
            p = round(val * q)
            if abs(val - p / q) < tol:
                is_rational = True
                info['is_rational'] = True
                info['p'] = p
                info['q'] = q
                info['fraction'] = f'{p}/{q}'
                break

        if not is_rational:
            info['is_rational'] = False
            info['fraction'] = None

        results[-n] = info

    return results


# ---------------------------------------------------------------------------
# 15. Landscape sweep: compute all Stark data for a family
# ---------------------------------------------------------------------------

def virasoro_stark_landscape(
    c_values: List[float],
    max_r: int = 50,
) -> List[Dict[str, Any]]:
    """Compute all Stark-type data for Virasoro at each c value.

    Returns list of dicts with Taylor coefficients, regulator, class number,
    central value, central derivative, and special values.
    """
    results = []
    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients(c_val, max_r)
        except ValueError:
            continue

        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=10, max_r=max_r)
        R_A, r_A = shadow_regulator(coeffs, max_r=max_r)

        entry = {
            'c': c_val,
            'kappa': c_val / 2.0,
            'order_of_vanishing': r_A,
            'regulator': R_A,
            'zeta_0': taylor[0],
            'zeta_prime_0': taylor[1],
            'zeta_double_prime_0': taylor[2],
            'class_number': shadow_class_number(coeffs, max_r),
            'central_value': shadow_central_value(coeffs, max_r),
            'central_derivative': shadow_central_derivative(coeffs, max_r),
        }

        # Special values at integers
        for n in range(-5, 11):
            entry[f'zeta_{n}'] = shadow_zeta_eval_real(coeffs, float(n), max_r)

        results.append(entry)

    return results


def affine_sl2_stark_landscape(
    k_values: List[float],
    max_r: int = 50,
) -> List[Dict[str, Any]]:
    """Compute Stark data for affine sl_2 at each level k."""
    results = []
    for k_val in k_values:
        if k_val <= -2.0:
            continue  # skip critical level
        coeffs = affine_sl2_shadow_coefficients(k_val, max_r)
        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5, max_r=max_r)
        R_A, r_A = shadow_regulator(coeffs, max_r=max_r)

        entry = {
            'k': k_val,
            'kappa': 3.0 * (k_val + 2.0) / 4.0,
            'alpha': 4.0 / (k_val + 2.0),
            'order_of_vanishing': r_A,
            'regulator': R_A,
            'zeta_0': taylor[0],
            'zeta_prime_0': taylor[1],
            'class_number': shadow_class_number(coeffs, max_r),
            'central_value': shadow_central_value(coeffs, max_r),
        }
        results.append(entry)

    return results


# ---------------------------------------------------------------------------
# 16. Virasoro shadow growth rate (for convergence verification)
# ---------------------------------------------------------------------------

def virasoro_shadow_growth_rate(c_val: float) -> float:
    """Exact shadow growth rate rho(Vir_c).

    From thm:shadow-radius:
    rho = |t_*|^{-1} where t_* is the nearest root of Q_L(t) = 0.

    Q_L(t) = c^2 + 12c t + alpha(c) t^2, alpha = (180c+872)/(5c+22).
    Discriminant = (12c)^2 - 4 c^2 alpha = 144c^2 - 4c^2 (180c+872)/(5c+22).

    For the growth rate of S_r coefficients:
    rho = smallest |root of Q_L|^{-1} if roots are finite.
    """
    if abs(c_val) < 1e-15:
        return float('inf')

    alpha = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    # Roots of c^2 + 12c t + alpha t^2 = 0
    # alpha t^2 + 12c t + c^2 = 0
    # t = (-12c +/- sqrt(144c^2 - 4 alpha c^2)) / (2 alpha)
    disc = 144.0 * c_val ** 2 - 4.0 * alpha * c_val ** 2
    if abs(alpha) < 1e-15:
        return 0.0
    if disc < 0:
        # Complex roots
        re_part = -12.0 * c_val / (2.0 * alpha)
        im_part = math.sqrt(-disc) / (2.0 * abs(alpha))
        modulus = math.sqrt(re_part ** 2 + im_part ** 2)
        if modulus < 1e-15:
            return float('inf')
        return 1.0 / modulus
    else:
        sq = math.sqrt(disc)
        t1 = (-12.0 * c_val + sq) / (2.0 * alpha)
        t2 = (-12.0 * c_val - sq) / (2.0 * alpha)
        min_mod = min(abs(t1), abs(t2))
        if min_mod < 1e-15:
            return float('inf')
        return 1.0 / min_mod


# ---------------------------------------------------------------------------
# 17. W_3 shadow coefficients on T-line
# ---------------------------------------------------------------------------

def w3_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for W_3 along the T-line (Virasoro restriction).

    On the T-line, kappa_T = c/2, S_3 = 2, S_4 = 10/(c(5c+22)).
    The T-line shadow tower is identical to Virasoro.
    """
    return virasoro_shadow_coefficients(c_val, max_r)
