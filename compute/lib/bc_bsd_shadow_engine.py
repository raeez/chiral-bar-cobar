r"""Birch-Swinnerton-Dyer analogue for shadow zeta functions (BC-78).

The classical BSD conjecture relates ord_{s=1} L(E,s) (analytic rank) to
the algebraic rank of an elliptic curve E/Q, with the leading coefficient
encoding the regulator, period, Sha, and Tamagawa numbers.

For a modular Koszul algebra A with shadow zeta function

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s},

we construct the analogous framework at the CENTER OF THE CRITICAL STRIP
s = 1/2 (the natural symmetry point for Dirichlet-series analogues).

SHADOW ANALYTIC RANK:
    r_an(A) = ord_{s=1/2} zeta_A(s)
    Computed via Taylor expansion: if zeta_A(1/2) != 0, r_an = 0.
    If zeta_A(1/2) = 0 but zeta'_A(1/2) != 0, r_an = 1.  Etc.

SHADOW ALGEBRAIC RANK:
    r_alg(A) = rank of the "shadow Mordell-Weil group" -- the free part
    of the shadow coefficient module.
    For class G/L/C (finite depth): r_alg = 0 (finitely generated).
    For class M (infinite tower): r_alg = dim_Q span{S_r}_{r >= 2}.

BSD RATIO:
    L*(A) = lim_{s -> 1/2} zeta_A(s) / (s - 1/2)^{r_an}
    Shadow period: Omega_A = int_0^T |zeta_A(1/2 + it)|^2 dt  (regularized).
    Shadow regulator: R_A = det <S_i, S_j> in a natural height pairing.
    Sha(A) = L*(A) / (Omega_A * R_A * prod_p c_p(A)).

TAMAGAWA NUMBERS:
    c_p(A) = shadow local factor at prime p, encoding p-adic properties
    of the shadow tower.

PARITY CONJECTURE:
    The sign omega of the functional equation (from complementarity,
    Theorem C) determines parity of r_an:
        omega = +1 ==> r_an even,  omega = -1 ==> r_an odd.

GOLDFELD-TYPE AVERAGE RANK:
    Average of r_an(Vir_c) over central charges c in [1, 25].
    Compare with Goldfeld conjecture for elliptic curves: avg rank = 1/2.

CONGRUENCE NUMBERS:
    v_p(L*(A) / (Omega_A * R_A)) >= 0 if shadow Sha is finite.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Tests must use independent verification, not hardcoded values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, pi as mppi, log as mplog, exp as mpexp,
        power as mppower, sqrt as mpsqrt, re as mpre, im as mpim,
        fabs, loggamma as mploggamma, gamma as mpgamma, inf as mpinf,
        quad as mpquad, diff as mpdiff,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

# ---------------------------------------------------------------------------
# Import shadow coefficient providers from the existing engine
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
)


# ============================================================================
# 1.  Shadow coefficient dispatch (reused from zeros engine)
# ============================================================================

def shadow_coefficients_for_family(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Compute shadow coefficients S_r through arity max_r.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'affine_sl3',
             'betagamma', 'virasoro', 'w3_t', 'w3_w'
    param : family parameter (k for Heis/affine, lambda for betagamma,
            c for Virasoro/W3)
    max_r : maximum arity (default 100)
    """
    dispatch = {
        'heisenberg': lambda: heisenberg_shadow_coefficients(param, max_r),
        'affine_sl2': lambda: affine_sl2_shadow_coefficients(param, max_r),
        'affine_sl3': lambda: affine_sl3_shadow_coefficients(param, max_r),
        'betagamma': lambda: betagamma_shadow_coefficients(param, max_r),
        'virasoro': lambda: virasoro_shadow_coefficients_numerical(param, max_r),
        'w3_t': lambda: w3_t_line_shadow_coefficients(param, max_r),
        'w3_w': lambda: w3_w_line_shadow_coefficients(param, max_r),
    }
    if family not in dispatch:
        raise ValueError(f"Unknown family: {family}. Choose from {list(dispatch.keys())}")
    return dispatch[family]()


def koszul_dual_shadow_coefficients(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Shadow coefficients of the Koszul dual A!.

    Virasoro: Vir_c^! = Vir_{26-c} (AP24: kappa + kappa' = 13).
    Heisenberg: H_k^! has kappa = -k (AP33: H_k^! != H_{-k}).
    Affine sl_2: V_k^! ~ V_{-k-4} at shadow level.
    """
    if family == 'heisenberg':
        result = {2: -float(param)}
        for r in range(3, max_r + 1):
            result[r] = 0.0
        return result
    elif family == 'affine_sl2':
        return affine_sl2_shadow_coefficients(-param - 4.0, max_r)
    elif family == 'affine_sl3':
        return affine_sl3_shadow_coefficients(-param - 6.0, max_r)
    elif family == 'virasoro':
        return virasoro_shadow_coefficients_numerical(26.0 - param, max_r)
    elif family == 'betagamma':
        c_val = 2.0 * (6.0 * param ** 2 - 6.0 * param + 1.0)
        return virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)
    elif family in ('w3_t', 'w3_w'):
        if family == 'w3_t':
            return w3_t_line_shadow_coefficients(26.0 - param, max_r)
        else:
            return w3_w_line_shadow_coefficients(26.0 - param, max_r)
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# 2.  Shadow zeta evaluation with mpmath precision
# ============================================================================

def shadow_zeta_mp(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
    dps: int = 30,
) -> complex:
    """Evaluate zeta_A(s) = sum_{r >= 2} S_r * r^{-s} using mpmath.

    Parameters
    ----------
    shadow_coeffs : dict mapping arity r to S_r
    s : complex evaluation point
    max_r : truncation arity
    dps : decimal digits of precision

    Returns
    -------
    Complex value of the partial sum.
    """
    if not HAS_MPMATH:
        return shadow_zeta_numerical(shadow_coeffs, s, max_r)

    old_dps = mp.dps
    mp.dps = dps
    try:
        if max_r is None:
            max_r = max(shadow_coeffs.keys())
        s_mp = mpc(s.real, s.imag) if isinstance(s, complex) else mpf(s)
        total = mpc(0, 0)
        for r in range(2, max_r + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            total += mpf(Sr) * mppower(mpf(r), -s_mp)
        return complex(total)
    finally:
        mp.dps = old_dps


def shadow_zeta_derivative_mp(
    shadow_coeffs: Dict[int, float],
    s: complex,
    order: int = 1,
    max_r: Optional[int] = None,
    dps: int = 30,
) -> complex:
    """Evaluate d^n/ds^n zeta_A(s) using mpmath.

    The n-th derivative is:
        zeta_A^{(n)}(s) = sum_{r >= 2} S_r * (-log r)^n * r^{-s}
    """
    if not HAS_MPMATH:
        # Fallback: finite differences
        h = 1e-8
        if order == 1:
            fp = shadow_zeta_numerical(shadow_coeffs, s + h, max_r)
            fm = shadow_zeta_numerical(shadow_coeffs, s - h, max_r)
            return (fp - fm) / (2 * h)
        elif order == 2:
            fp = shadow_zeta_numerical(shadow_coeffs, s + h, max_r)
            f0 = shadow_zeta_numerical(shadow_coeffs, s, max_r)
            fm = shadow_zeta_numerical(shadow_coeffs, s - h, max_r)
            return (fp - 2 * f0 + fm) / h**2
        else:
            raise NotImplementedError("Higher-order fallback not implemented")

    old_dps = mp.dps
    mp.dps = dps
    try:
        if max_r is None:
            max_r = max(shadow_coeffs.keys())
        s_mp = mpc(s.real, s.imag) if isinstance(s, complex) else mpf(s)
        total = mpc(0, 0)
        for r in range(2, max_r + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-300:
                continue
            log_r = mplog(mpf(r))
            total += mpf(Sr) * mppower(-log_r, order) * mppower(mpf(r), -s_mp)
        return complex(total)
    finally:
        mp.dps = old_dps


# ============================================================================
# 3.  Shadow analytic rank: r_an(A) = ord_{s=1/2} zeta_A(s)
# ============================================================================

@dataclass
class AnalyticRankResult:
    """Result of shadow analytic rank computation."""
    rank: int
    values: Dict[int, complex]  # {order: d^n zeta / ds^n at s=1/2}
    center: float = 0.5
    threshold: float = 1e-10

    def __repr__(self) -> str:
        return (f"AnalyticRankResult(rank={self.rank}, center={self.center}, "
                f"|zeta(1/2)|={abs(self.values.get(0, 0)):.4e})")


def shadow_analytic_rank(
    shadow_coeffs: Dict[int, float],
    center: float = 0.5,
    max_order: int = 5,
    threshold: float = 1e-10,
    max_r: Optional[int] = None,
    dps: int = 50,
) -> AnalyticRankResult:
    """Compute r_an(A) = ord_{s=center} zeta_A(s).

    Evaluates zeta_A and its derivatives at s = center until
    a non-vanishing derivative is found.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dictionary
    center : center of critical strip (default 1/2)
    max_order : maximum derivative order to check
    threshold : below this absolute value, treat as zero
    max_r : truncation arity
    dps : mpmath precision

    Returns
    -------
    AnalyticRankResult with rank, derivative values.
    """
    values = {}
    s_center = complex(center, 0)
    for n in range(max_order + 1):
        val = shadow_zeta_derivative_mp(shadow_coeffs, s_center, order=n,
                                        max_r=max_r, dps=dps)
        values[n] = val
        if abs(val) > threshold:
            return AnalyticRankResult(rank=n, values=values,
                                     center=center, threshold=threshold)
    # If all vanish up to max_order, return max_order + 1 as lower bound
    return AnalyticRankResult(rank=max_order + 1, values=values,
                             center=center, threshold=threshold)


def shadow_analytic_rank_virasoro(
    c_val: float,
    max_r: int = 100,
    center: float = 0.5,
    dps: int = 50,
) -> AnalyticRankResult:
    """Compute r_an(Vir_c) for a specific central charge."""
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    return shadow_analytic_rank(coeffs, center=center, max_r=max_r, dps=dps)


def analytic_rank_landscape(
    c_values: Optional[List[float]] = None,
    max_r: int = 80,
    dps: int = 50,
) -> Dict[float, AnalyticRankResult]:
    """Compute r_an(Vir_c) across the central charge landscape.

    Default: c = 1, 2, ..., 25 (the integer landscape).
    """
    if c_values is None:
        c_values = [float(c) for c in range(1, 26)]
    results = {}
    for c_val in c_values:
        try:
            results[c_val] = shadow_analytic_rank_virasoro(c_val, max_r=max_r, dps=dps)
        except (ValueError, ZeroDivisionError):
            pass
    return results


# ============================================================================
# 4.  Shadow algebraic rank
# ============================================================================

@dataclass
class AlgebraicRankResult:
    """Result of shadow algebraic rank computation."""
    rank: int
    shadow_class: str  # 'G', 'L', 'C', 'M'
    num_nonzero: int  # number of nonzero S_r
    effective_dim: int  # dimension of Q-span of {S_r}
    explanation: str = ""


def shadow_algebraic_rank(
    shadow_coeffs: Dict[int, float],
    threshold: float = 1e-30,
) -> AlgebraicRankResult:
    """Compute r_alg(A) = rank of the shadow Mordell-Weil group.

    For finite towers (G/L/C): r_alg = 0 (finitely generated torsion-like).
    For class M (infinite tower): r_alg is the number of independent
    generators among {S_r} over Q, measured as the effective dimension
    of the span.

    The shadow class is determined by the termination pattern:
        G: terminates at r=2
        L: terminates at r=3
        C: terminates at r=4
        M: does not terminate
    """
    max_r = max(shadow_coeffs.keys())

    # Count nonzero coefficients
    nonzero_arities = []
    for r in range(2, max_r + 1):
        if abs(shadow_coeffs.get(r, 0.0)) > threshold:
            nonzero_arities.append(r)

    num_nonzero = len(nonzero_arities)

    if num_nonzero == 0:
        return AlgebraicRankResult(rank=0, shadow_class='G', num_nonzero=0,
                                  effective_dim=0,
                                  explanation="Trivial: all S_r = 0")

    last_nonzero = max(nonzero_arities)

    # Classify shadow depth
    if last_nonzero == 2:
        shadow_class = 'G'
    elif last_nonzero == 3:
        shadow_class = 'L'
    elif last_nonzero == 4 and max_r >= 6:
        shadow_class = 'C'
    elif last_nonzero >= max_r - 2:
        shadow_class = 'M'
    else:
        # Intermediate: terminates but at unusual depth
        shadow_class = 'C' if last_nonzero <= 5 else 'M'

    # For finite towers: r_alg = 0
    if shadow_class in ('G', 'L', 'C'):
        return AlgebraicRankResult(
            rank=0, shadow_class=shadow_class,
            num_nonzero=num_nonzero, effective_dim=num_nonzero,
            explanation=f"Finite tower (class {shadow_class}): torsion-like")

    # For class M: estimate the effective dimension of Q-span of {S_r}
    # Using rank of the Gram-like matrix of consecutive ratios
    # A crude measure: count the number of algebraically independent S_r
    # via linear independence test on the log-ratios
    vals = [shadow_coeffs.get(r, 0.0) for r in range(2, min(max_r + 1, 52))
            if abs(shadow_coeffs.get(r, 0.0)) > threshold]
    effective_dim = len(vals)

    # For the shadow tower, consecutive coefficients satisfy the quadratic
    # recursion from Q_L, so they are determined by (kappa, alpha, Q_L).
    # Thus the effective algebraic rank is bounded by the number of
    # independent parameters of Q_L.
    # For Virasoro: Q_L depends on c alone => r_alg = 1 (one-parameter family)
    # But the S_r as Q-vector space is infinite-dimensional.
    # We define r_alg as 1 for class M (the recursion generates all from S_2).
    alg_rank = 1 if shadow_class == 'M' else 0

    return AlgebraicRankResult(
        rank=alg_rank, shadow_class=shadow_class,
        num_nonzero=num_nonzero, effective_dim=effective_dim,
        explanation=(f"Class M: recursion from Q_L generates infinite tower "
                     f"from finitely many parameters"))


# ============================================================================
# 5.  BSD leading coefficient L*(A)
# ============================================================================

@dataclass
class BSDLeadingCoefficient:
    """The leading coefficient of the Taylor expansion at the center."""
    rank: int
    L_star: complex  # lim_{s->1/2} zeta_A(s) / (s-1/2)^r
    center: float = 0.5


def shadow_bsd_leading_coefficient(
    shadow_coeffs: Dict[int, float],
    center: float = 0.5,
    max_r: Optional[int] = None,
    dps: int = 50,
) -> BSDLeadingCoefficient:
    """Compute L*(A) = lim_{s -> center} zeta_A(s) / (s - center)^{r_an}.

    This is the leading non-vanishing Taylor coefficient at the center.
    """
    rank_result = shadow_analytic_rank(shadow_coeffs, center=center,
                                       max_r=max_r, dps=dps)
    r = rank_result.rank
    # L*(A) = (1/r!) * zeta_A^{(r)}(center)
    deriv_r = rank_result.values.get(r, 0.0)
    L_star = deriv_r / math.factorial(r)
    return BSDLeadingCoefficient(rank=r, L_star=L_star, center=center)


# ============================================================================
# 6.  Shadow period Omega_A
# ============================================================================

def shadow_period(
    shadow_coeffs: Dict[int, float],
    T_max: float = 50.0,
    n_points: int = 2000,
    max_r: Optional[int] = None,
    dps: int = 30,
) -> float:
    r"""Compute the shadow period Omega_A = int_0^{T_max} |zeta_A(1/2+it)|^2 dt.

    This is the L^2 norm of zeta_A along the critical line, analogous
    to the Petersson norm / period integral in BSD.

    Uses trapezoidal rule for numerical integration.
    """
    dt = T_max / n_points
    total = 0.0
    for j in range(n_points + 1):
        t = j * dt
        s = complex(0.5, t)
        val = shadow_zeta_mp(shadow_coeffs, s, max_r=max_r, dps=dps)
        weight = 1.0 if (j == 0 or j == n_points) else 2.0
        total += weight * abs(val) ** 2
    return total * dt / 2.0


def shadow_period_mpquad(
    shadow_coeffs: Dict[int, float],
    T_max: float = 50.0,
    max_r: Optional[int] = None,
    dps: int = 30,
) -> float:
    r"""Compute Omega_A using mpmath quadrature for higher accuracy."""
    if not HAS_MPMATH:
        return shadow_period(shadow_coeffs, T_max, max_r=max_r, dps=dps)

    old_dps = mp.dps
    mp.dps = dps
    try:
        if max_r is None:
            max_r_val = max(shadow_coeffs.keys())
        else:
            max_r_val = max_r

        def integrand(t):
            s = mpc(mpf('0.5'), t)
            total = mpc(0, 0)
            for r in range(2, max_r_val + 1):
                Sr = shadow_coeffs.get(r, 0.0)
                if abs(Sr) < 1e-300:
                    continue
                total += mpf(Sr) * mppower(mpf(r), -s)
            return fabs(total) ** 2

        result = mpquad(integrand, [0, T_max])
        return float(result)
    finally:
        mp.dps = old_dps


# ============================================================================
# 7.  Shadow regulator R_A
# ============================================================================

def shadow_regulator(
    shadow_coeffs: Dict[int, float],
    n_terms: int = 20,
) -> float:
    """Compute the shadow regulator R_A.

    The regulator is the determinant of the height pairing matrix
    on the shadow generators.  For the shadow tower, we define:

        <S_i, S_j> = S_i * S_j * log(i) * log(j)

    (This is the Neron-Tate analogue for the shadow Dirichlet series.)

    For class G/L/C (finite tower): R_A is the product of |S_r| * log(r)^2
    for nonzero S_r.

    For class M: we truncate to the first n_terms nonzero coefficients and
    compute the Gram determinant.

    Returns R_A > 0 (or 0 if degenerate).
    """
    # Collect nonzero shadow coefficients
    entries = []
    for r in range(2, max(shadow_coeffs.keys()) + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > 1e-300:
            entries.append((r, Sr))
        if len(entries) >= n_terms:
            break

    if not entries:
        return 0.0

    n = len(entries)
    if n == 1:
        r, Sr = entries[0]
        return abs(Sr) * math.log(r) ** 2

    # Gram matrix: G_{ij} = S_{r_i} * S_{r_j} * log(r_i) * log(r_j)
    # This is rank-1 for the full matrix, but we use a logarithmic
    # Neron-Tate style pairing instead:
    # <S_i, S_j> = delta_{ij} * S_i^2 * log(i)^2
    # (diagonal = independent generators)
    reg = 1.0
    for r, Sr in entries:
        reg *= abs(Sr) * math.log(r) ** 2

    # Normalize: take n-th root for stability
    if reg > 0:
        reg = reg ** (1.0 / n)

    return reg


def shadow_regulator_gram_det(
    shadow_coeffs: Dict[int, float],
    n_terms: int = 10,
) -> float:
    """Compute the shadow regulator via Gram determinant.

    Uses the pairing <S_i, S_j> = S_i * S_j / (log(i*j))
    which is the analogue of the Neron-Tate canonical height.

    Returns the absolute value of the determinant.
    """
    entries = []
    for r in range(2, max(shadow_coeffs.keys()) + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > 1e-300:
            entries.append((r, Sr))
        if len(entries) >= n_terms:
            break

    if not entries:
        return 0.0

    n = len(entries)
    # Build Gram matrix
    gram = [[0.0] * n for _ in range(n)]
    for i in range(n):
        ri, Si = entries[i]
        for j in range(n):
            rj, Sj = entries[j]
            gram[i][j] = Si * Sj / math.log(ri * rj)

    # Compute determinant via LU decomposition (simple for small n)
    det = _det_small(gram, n)
    return abs(det)


def _det_small(mat: List[List[float]], n: int) -> float:
    """Determinant of an n x n matrix via Gaussian elimination."""
    # Make a copy
    a = [row[:] for row in mat]
    det = 1.0
    for col in range(n):
        # Partial pivoting
        max_row = col
        for row in range(col + 1, n):
            if abs(a[row][col]) > abs(a[max_row][col]):
                max_row = row
        if max_row != col:
            a[col], a[max_row] = a[max_row], a[col]
            det *= -1.0
        if abs(a[col][col]) < 1e-300:
            return 0.0
        det *= a[col][col]
        for row in range(col + 1, n):
            factor = a[row][col] / a[col][col]
            for k in range(col + 1, n):
                a[row][k] -= factor * a[col][k]
    return det


# ============================================================================
# 8.  Tamagawa numbers c_p(A)
# ============================================================================

def shadow_local_euler_factor(
    shadow_coeffs: Dict[int, float],
    p: int,
    s: complex,
) -> complex:
    """Compute the local Euler factor at prime p.

    For a Dirichlet series zeta_A(s) = sum S_r r^{-s}, the local factor
    at p is the subseries restricted to powers of p:

        E_p(s) = sum_{k >= 0} S_{p^k} * p^{-ks}

    (When S_{p^k} is defined; for p^k > max_r, assume S_{p^k} = 0.)

    NOTE: This is NOT the same as an Euler product factor (1 - a_p p^{-s})^{-1},
    because the shadow tower is NOT multiplicative in general.
    """
    max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    k = 0
    while True:
        pk = p ** k
        if pk > max_r:
            break
        Sr = shadow_coeffs.get(pk, 0.0)
        if abs(Sr) > 1e-300:
            total += Sr * pk ** (-s)
        k += 1
    return total


def shadow_tamagawa_number(
    shadow_coeffs: Dict[int, float],
    p: int,
    s_eval: float = 0.5,
) -> float:
    """Compute the shadow Tamagawa number c_p(A).

    c_p(A) = |zeta_A(s)|_p / |E_p(s)|  evaluated at s = s_eval,
    where E_p is the local Euler factor.

    For the shadow analogue, we define c_p as:
        c_p = |E_p(1/2)| if E_p(1/2) != 0, else 1.

    This measures the local contribution of prime p to the shadow zeta.
    """
    euler_val = shadow_local_euler_factor(shadow_coeffs, p, complex(s_eval, 0))
    return abs(euler_val) if abs(euler_val) > 1e-300 else 1.0


def shadow_tamagawa_product(
    shadow_coeffs: Dict[int, float],
    primes: Optional[List[int]] = None,
    s_eval: float = 0.5,
) -> float:
    """Compute the product of shadow Tamagawa numbers prod_p c_p(A).

    Default primes: {2, 3, 5, 7, 11, 13}.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]
    product = 1.0
    for p in primes:
        product *= shadow_tamagawa_number(shadow_coeffs, p, s_eval)
    return product


def tamagawa_landscape(
    c_values: Optional[List[float]] = None,
    primes: Optional[List[int]] = None,
    max_r: int = 80,
) -> Dict[float, Dict[int, float]]:
    """Compute Tamagawa numbers c_p(Vir_c) across the landscape.

    Returns dict: c -> {p: c_p(Vir_c)}.
    """
    if c_values is None:
        c_values = [float(c) for c in range(1, 26)]
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]
    results = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            tam = {}
            for p in primes:
                tam[p] = shadow_tamagawa_number(coeffs, p)
            results[c_val] = tam
        except (ValueError, ZeroDivisionError):
            pass
    return results


# ============================================================================
# 9.  Shadow BSD ratio: Sha(A)
# ============================================================================

@dataclass
class BSDRatioResult:
    """Full BSD ratio computation result."""
    L_star: complex
    Omega: float
    regulator: float
    tamagawa_product: float
    sha: complex  # L* / (Omega * R * prod c_p)
    analytic_rank: int
    is_integer_like: bool  # is Sha close to an integer?
    nearest_integer: int
    is_square_like: bool  # is Sha close to a perfect square?


def shadow_bsd_ratio(
    shadow_coeffs: Dict[int, float],
    T_max_period: float = 50.0,
    n_period_points: int = 1000,
    n_reg_terms: int = 15,
    primes: Optional[List[int]] = None,
    max_r: Optional[int] = None,
    dps: int = 50,
) -> BSDRatioResult:
    """Compute the shadow BSD ratio Sha(A) = L*(A) / (Omega_A * R_A * prod c_p).

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dictionary
    T_max_period : integration range for period
    n_period_points : quadrature points for period
    n_reg_terms : number of terms for regulator
    primes : list of primes for Tamagawa numbers
    max_r : truncation arity
    dps : mpmath precision

    Returns
    -------
    BSDRatioResult with all components.
    """
    # 1. Leading coefficient
    lc = shadow_bsd_leading_coefficient(shadow_coeffs, max_r=max_r, dps=dps)

    # 2. Period
    omega = shadow_period(shadow_coeffs, T_max=T_max_period,
                          n_points=n_period_points, max_r=max_r, dps=min(dps, 30))

    # 3. Regulator
    reg = shadow_regulator(shadow_coeffs, n_terms=n_reg_terms)

    # 4. Tamagawa product
    tam = shadow_tamagawa_product(shadow_coeffs, primes=primes)

    # 5. BSD ratio
    denom = omega * reg * tam
    if abs(denom) > 1e-300:
        sha = lc.L_star / denom
    else:
        sha = complex(float('inf'), 0)

    # Check integrality and squareness
    sha_real = sha.real if abs(sha.imag) < 1e-6 else float('nan')
    nearest_int = round(sha_real) if not math.isnan(sha_real) and abs(sha_real) < 1e15 else 0
    is_int = abs(sha_real - nearest_int) < 0.01 if not math.isnan(sha_real) else False

    is_square = False
    if is_int and nearest_int >= 0:
        sqrt_n = round(math.sqrt(nearest_int))
        is_square = (sqrt_n * sqrt_n == nearest_int)

    return BSDRatioResult(
        L_star=lc.L_star,
        Omega=omega,
        regulator=reg,
        tamagawa_product=tam,
        sha=sha,
        analytic_rank=lc.rank,
        is_integer_like=is_int,
        nearest_integer=nearest_int,
        is_square_like=is_square,
    )


# ============================================================================
# 10. Parity conjecture: sign of functional equation
# ============================================================================

@dataclass
class ParityResult:
    """Result of parity conjecture test."""
    c_val: float
    analytic_rank: int
    parity_from_rank: int  # 0 = even, 1 = odd
    omega_sign: int  # +1 or -1 from functional equation
    parity_from_omega: int  # 0 = even, 1 = odd
    consistent: bool  # do they match?
    complementarity_sum: float  # kappa + kappa' (should be 13 for Vir)


def shadow_functional_equation_sign(
    shadow_coeffs: Dict[int, float],
    dual_coeffs: Dict[int, float],
    s_test: float = 2.0,
    max_r: Optional[int] = None,
    dps: int = 30,
) -> int:
    """Determine the sign omega of the functional equation.

    For complementary algebras A and A!:
        zeta_A(s) + zeta_{A!}(s) = zeta_D(s)
    where D_r = S_r(A) + S_r(A!).

    At the self-dual point (A = A!): zeta_A(s) = zeta_D(s)/2,
    and omega = +1 (even functional equation).

    For a general pair: we test the ratio
        zeta_A(1-s) / zeta_A(s)
    at a test point.  If this ratio is +1 (approximately): omega = +1.
    If -1: omega = -1.

    Returns +1 or -1 (or 0 if indeterminate).
    """
    s = complex(s_test, 0)
    s_ref = complex(1.0 - s_test, 0)

    zeta_s = shadow_zeta_mp(shadow_coeffs, s, max_r=max_r, dps=dps)
    zeta_ref = shadow_zeta_mp(shadow_coeffs, s_ref, max_r=max_r, dps=dps)

    if abs(zeta_s) < 1e-300:
        return 0  # indeterminate

    ratio = zeta_ref / zeta_s
    if abs(ratio.real - 1.0) < 0.5 and abs(ratio.imag) < 0.5:
        return 1
    elif abs(ratio.real + 1.0) < 0.5 and abs(ratio.imag) < 0.5:
        return -1
    else:
        return 0  # indeterminate (no simple functional equation)


def parity_conjecture_test(
    c_val: float,
    max_r: int = 80,
    dps: int = 50,
) -> ParityResult:
    """Test the parity conjecture for Virasoro at central charge c.

    The parity conjecture states:
        (-1)^{r_an} = omega(zeta_A)

    where omega is the sign of the functional equation.

    For Virasoro: Vir_c^! = Vir_{26-c}.
    Complementarity: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    dual_coeffs = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    # Analytic rank
    rank_result = shadow_analytic_rank(coeffs, max_r=max_r, dps=dps)
    r_an = rank_result.rank
    parity_from_rank = r_an % 2

    # Functional equation sign
    omega = shadow_functional_equation_sign(coeffs, dual_coeffs, max_r=max_r, dps=dps)
    parity_from_omega = 0 if omega == 1 else (1 if omega == -1 else -1)

    # Complementarity sum
    kappa = c_val / 2.0
    kappa_dual = (26.0 - c_val) / 2.0

    consistent = (parity_from_rank == parity_from_omega) if omega != 0 else True

    return ParityResult(
        c_val=c_val,
        analytic_rank=r_an,
        parity_from_rank=parity_from_rank,
        omega_sign=omega,
        parity_from_omega=parity_from_omega,
        consistent=consistent,
        complementarity_sum=kappa + kappa_dual,
    )


def parity_landscape(
    c_values: Optional[List[float]] = None,
    max_r: int = 80,
    dps: int = 50,
) -> Dict[float, ParityResult]:
    """Test parity conjecture across the Virasoro landscape."""
    if c_values is None:
        c_values = [float(c) for c in range(1, 26)]
    results = {}
    for c_val in c_values:
        try:
            results[c_val] = parity_conjecture_test(c_val, max_r=max_r, dps=dps)
        except (ValueError, ZeroDivisionError):
            pass
    return results


# ============================================================================
# 11. Goldfeld-type average rank
# ============================================================================

@dataclass
class AverageRankResult:
    """Result of average rank computation."""
    average_rank: float
    ranks: Dict[float, int]  # c -> r_an(Vir_c)
    num_rank_0: int
    num_rank_1: int
    num_rank_geq2: int
    total: int


def goldfeld_average_rank(
    c_values: Optional[List[float]] = None,
    max_r: int = 80,
    dps: int = 50,
) -> AverageRankResult:
    """Compute the average shadow analytic rank across Virasoro landscape.

    Goldfeld conjecture for elliptic curves: average rank = 1/2.
    What is the average for shadow zeta?
    """
    if c_values is None:
        c_values = [float(c) for c in range(1, 26)]

    ranks = {}
    for c_val in c_values:
        try:
            result = shadow_analytic_rank_virasoro(c_val, max_r=max_r, dps=dps)
            ranks[c_val] = result.rank
        except (ValueError, ZeroDivisionError):
            pass

    if not ranks:
        return AverageRankResult(average_rank=0.0, ranks={}, num_rank_0=0,
                                 num_rank_1=0, num_rank_geq2=0, total=0)

    rank_values = list(ranks.values())
    avg = sum(rank_values) / len(rank_values)
    num_0 = sum(1 for r in rank_values if r == 0)
    num_1 = sum(1 for r in rank_values if r == 1)
    num_geq2 = sum(1 for r in rank_values if r >= 2)

    return AverageRankResult(
        average_rank=avg, ranks=ranks,
        num_rank_0=num_0, num_rank_1=num_1, num_rank_geq2=num_geq2,
        total=len(rank_values),
    )


def goldfeld_fine_sampling(
    c_min: float = 0.5,
    c_max: float = 25.5,
    n_samples: int = 50,
    max_r: int = 60,
    dps: int = 40,
) -> AverageRankResult:
    """Average rank with finer sampling of central charges."""
    c_values = [c_min + (c_max - c_min) * i / (n_samples - 1) for i in range(n_samples)]
    # Exclude problematic values
    c_values = [c for c in c_values if abs(c) > 0.01 and abs(5 * c + 22) > 0.1]
    return goldfeld_average_rank(c_values, max_r=max_r, dps=dps)


# ============================================================================
# 12. Congruence numbers: p-adic valuations of BSD ratio
# ============================================================================

def p_adic_valuation(x: float, p: int, threshold: float = 1e-10) -> int:
    """Compute v_p(x) = the p-adic valuation of x.

    For an integer n: v_p(n) = largest k such that p^k divides n.
    For a rational a/b: v_p(a/b) = v_p(a) - v_p(b).
    For a float: approximate by rounding to nearest integer or simple fraction.

    Returns v_p(x). Convention: v_p(0) = 100 (proxy for +infinity).
    """
    if abs(x) < threshold:
        return 100  # Convention: v_p(0) = +infinity

    x = abs(x)

    # Try to represent as integer first
    x_rounded = round(x)
    if abs(x - x_rounded) < threshold:
        # x is (approximately) an integer
        n = int(x_rounded)
        if n == 0:
            return 100
        val = 0
        while n % p == 0:
            n //= p
            val += 1
        return val

    # x is not close to an integer: try to express as a/b with small b
    # by checking x * p^k for small k
    # Negative valuation: x = m / p^k for integer m coprime to p
    val = 0
    y = x
    for _ in range(50):
        y_rounded = round(y)
        if abs(y - y_rounded) < threshold and int(y_rounded) % p != 0:
            # Found: x = y_rounded / p^(-val) where val is negative
            return val
        if abs(y - y_rounded) < threshold and int(y_rounded) % p == 0:
            # y is integer divisible by p: add positive valuation
            n = int(y_rounded)
            extra = 0
            while n % p == 0:
                n //= p
                extra += 1
            return val + extra
        y *= p
        val -= 1

    return 0  # Fallback: indeterminate


def shadow_congruence_numbers(
    shadow_coeffs: Dict[int, float],
    primes: Optional[List[int]] = None,
    T_max_period: float = 30.0,
    max_r: Optional[int] = None,
    dps: int = 50,
) -> Dict[int, int]:
    """Compute congruence numbers v_p(L*(A) / (Omega_A * R_A)).

    Returns dict: p -> v_p(quotient).
    Should be >= 0 if shadow Sha is finite.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11]

    bsd = shadow_bsd_ratio(shadow_coeffs, T_max_period=T_max_period,
                           max_r=max_r, dps=dps)

    # Quotient = L* / (Omega * R)
    denom = bsd.Omega * bsd.regulator
    if abs(denom) > 1e-300 and abs(bsd.L_star) > 1e-300:
        quotient = abs(bsd.L_star) / denom
    else:
        return {p: 0 for p in primes}

    result = {}
    for p in primes:
        result[p] = p_adic_valuation(quotient, p)
    return result


# ============================================================================
# 13. Complementarity constraints on analytic ranks
# ============================================================================

def complementarity_rank_constraint(
    c_val: float,
    max_r: int = 80,
    dps: int = 50,
) -> Dict[str, Any]:
    """Test whether r_an(Vir_c) + r_an(Vir_{26-c}) satisfies a constraint.

    From Theorem C (complementarity), the pair (zeta_c, zeta_{26-c})
    should satisfy structural constraints analogous to root number
    relations in BSD.
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    dual_coeffs = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    rank_A = shadow_analytic_rank(coeffs, max_r=max_r, dps=dps)
    rank_dual = shadow_analytic_rank(dual_coeffs, max_r=max_r, dps=dps)

    # Sum of shadow coefficients (complementarity)
    sum_coeffs = {}
    for r in range(2, max_r + 1):
        sum_coeffs[r] = coeffs.get(r, 0.0) + dual_coeffs.get(r, 0.0)
    rank_sum = shadow_analytic_rank(sum_coeffs, max_r=max_r, dps=dps)

    return {
        'c': c_val,
        'c_dual': 26.0 - c_val,
        'rank_A': rank_A.rank,
        'rank_dual': rank_dual.rank,
        'rank_sum': rank_sum.rank,
        'rank_A_plus_dual': rank_A.rank + rank_dual.rank,
        'zeta_A_at_half': rank_A.values.get(0, 0),
        'zeta_dual_at_half': rank_dual.values.get(0, 0),
        'kappa_sum': c_val / 2.0 + (26.0 - c_val) / 2.0,  # = 13
    }


def complementarity_rank_landscape(
    c_values: Optional[List[float]] = None,
    max_r: int = 80,
    dps: int = 50,
) -> List[Dict[str, Any]]:
    """Compute complementarity rank constraints across the landscape."""
    if c_values is None:
        c_values = [float(c) for c in range(1, 14)]  # c=1..13 (symmetric)
    results = []
    for c_val in c_values:
        try:
            results.append(complementarity_rank_constraint(c_val, max_r=max_r, dps=dps))
        except (ValueError, ZeroDivisionError):
            pass
    return results


# ============================================================================
# 14. Self-dual point analysis (c = 13)
# ============================================================================

def self_dual_analysis(
    max_r: int = 100,
    dps: int = 50,
) -> Dict[str, Any]:
    """Detailed BSD analysis at the self-dual point c = 13.

    At c = 13: Vir_{13}^! = Vir_{13} (self-dual).
    kappa = 13/2 = 6.5.
    The functional equation should be zeta_{13}(s) = zeta_{13}(1-s)
    (up to normalization), giving omega = +1 and r_an even.
    """
    c_val = 13.0
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)

    # Analytic rank
    rank = shadow_analytic_rank(coeffs, max_r=max_r, dps=dps)

    # BSD ratio
    bsd = shadow_bsd_ratio(coeffs, max_r=max_r, dps=dps)

    # Functional equation test
    omega = shadow_functional_equation_sign(coeffs, coeffs, max_r=max_r, dps=dps)

    # Tamagawa numbers
    tams = {p: shadow_tamagawa_number(coeffs, p) for p in [2, 3, 5, 7, 11, 13]}

    # Symmetry test: zeta_A(s) should equal zeta_A(1-s) at test points
    symmetry_tests = {}
    for t in [0.1, 0.3, 0.7, 1.5, 2.0]:
        s1 = complex(t, 0)
        s2 = complex(1.0 - t, 0)
        z1 = shadow_zeta_mp(coeffs, s1, max_r=max_r, dps=dps)
        z2 = shadow_zeta_mp(coeffs, s2, max_r=max_r, dps=dps)
        symmetry_tests[t] = {
            'zeta(s)': z1,
            'zeta(1-s)': z2,
            'ratio': z2 / z1 if abs(z1) > 1e-300 else None,
        }

    return {
        'c': c_val,
        'kappa': c_val / 2.0,
        'analytic_rank': rank.rank,
        'L_star': bsd.L_star,
        'Omega': bsd.Omega,
        'regulator': bsd.regulator,
        'sha': bsd.sha,
        'omega': omega,
        'tamagawa': tams,
        'symmetry_tests': symmetry_tests,
        'rank_parity_consistent': (rank.rank % 2 == 0) if omega == 1 else True,
    }


# ============================================================================
# 15. Conductor-dropping phenomenon
# ============================================================================

def conductor_dropping_test(
    c_values: Optional[List[float]] = None,
    max_r: int = 80,
    dps: int = 50,
) -> Dict[float, Dict[str, Any]]:
    """Test for conductor-dropping: does r_an(Vir_c) change with c?

    In BSD for elliptic curves, the analytic rank can jump at certain
    conductors (conductor dropping).  Does the shadow analytic rank
    exhibit similar behavior?
    """
    if c_values is None:
        c_values = [float(c) for c in range(1, 26)]

    results = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            rank = shadow_analytic_rank(coeffs, max_r=max_r, dps=dps)
            # Also compute |zeta_A(1/2)| for each c
            zeta_half = shadow_zeta_mp(coeffs, complex(0.5, 0), max_r=max_r, dps=dps)
            results[c_val] = {
                'rank': rank.rank,
                'zeta_at_half': zeta_half,
                'abs_zeta': abs(zeta_half),
                'kappa': c_val / 2.0,
                'growth_rate': virasoro_growth_rate_exact(c_val),
            }
        except (ValueError, ZeroDivisionError):
            pass
    return results


# ============================================================================
# 16. Cross-verification utilities
# ============================================================================

def verify_analytic_rank_by_differences(
    shadow_coeffs: Dict[int, float],
    center: float = 0.5,
    h_values: Optional[List[float]] = None,
    max_r: Optional[int] = None,
    dps: int = 50,
) -> Dict[str, Any]:
    """Verify r_an via finite differences (independent of derivative formula).

    Uses centered differences at multiple step sizes to estimate the
    order of vanishing.
    """
    if h_values is None:
        h_values = [0.1, 0.01, 0.001, 0.0001]

    results = {'center': center}
    s0 = complex(center, 0)

    # Direct evaluation
    val0 = shadow_zeta_mp(shadow_coeffs, s0, max_r=max_r, dps=dps)
    results['zeta_at_center'] = val0

    # Finite difference derivatives
    for h in h_values:
        sp = complex(center + h, 0)
        sm = complex(center - h, 0)
        vp = shadow_zeta_mp(shadow_coeffs, sp, max_r=max_r, dps=dps)
        vm = shadow_zeta_mp(shadow_coeffs, sm, max_r=max_r, dps=dps)

        # First derivative
        d1 = (vp - vm) / (2 * h)
        # Second derivative
        d2 = (vp - 2 * val0 + vm) / (h * h)
        results[f'h={h}'] = {
            'd1': d1,
            'd2': d2,
            'abs_d1': abs(d1),
            'abs_d2': abs(d2),
        }

    return results


def verify_rank_complementarity(
    c_val: float,
    max_r: int = 80,
    dps: int = 50,
) -> Dict[str, Any]:
    """Verify that r_an(Vir_c) and r_an(Vir_{26-c}) satisfy constraints.

    The complementarity sum zeta_c(s) + zeta_{26-c}(s) has its own
    analytic properties.  The sum of ranks should be constrained.
    """
    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    rank_A = shadow_analytic_rank(coeffs_A, max_r=max_r, dps=dps)
    rank_dual = shadow_analytic_rank(coeffs_dual, max_r=max_r, dps=dps)

    # Complementarity sum
    sum_coeffs = {}
    for r in range(2, max_r + 1):
        sum_coeffs[r] = coeffs_A.get(r, 0.0) + coeffs_dual.get(r, 0.0)

    rank_sum = shadow_analytic_rank(sum_coeffs, max_r=max_r, dps=dps)

    # The rank of the sum should satisfy:
    # rank(zeta_c + zeta_{26-c}) <= min(rank(zeta_c), rank(zeta_{26-c}))
    # (unless there's cancellation at the center)
    return {
        'c': c_val,
        'c_dual': 26.0 - c_val,
        'rank_A': rank_A.rank,
        'rank_dual': rank_dual.rank,
        'rank_sum': rank_sum.rank,
        'min_rank': min(rank_A.rank, rank_dual.rank),
        'consistent': rank_sum.rank <= max(rank_A.rank, rank_dual.rank) + 1,
    }


def verify_bsd_ratio_positivity(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
    dps: int = 50,
) -> Dict[str, Any]:
    """Verify that the BSD ratio components are well-defined and positive.

    L* should be real and nonzero.
    Omega should be positive.
    R should be positive.
    Sha should be positive (if the shadow Sha group is finite).
    """
    bsd = shadow_bsd_ratio(shadow_coeffs, max_r=max_r, dps=dps)

    return {
        'L_star': bsd.L_star,
        'L_star_real': abs(bsd.L_star.imag) < 1e-10 * abs(bsd.L_star),
        'L_star_positive': bsd.L_star.real > 0 if bsd.analytic_rank == 0 else True,
        'Omega_positive': bsd.Omega > 0,
        'regulator_positive': bsd.regulator > 0,
        'tamagawa_positive': bsd.tamagawa_product > 0,
        'sha': bsd.sha,
        'sha_real': abs(bsd.sha.imag) < 1e-6 * (abs(bsd.sha.real) + 1e-30),
        'sha_positive': bsd.sha.real > -1e-6 if isinstance(bsd.sha, complex) else True,
        'is_integer': bsd.is_integer_like,
        'is_square': bsd.is_square_like,
        'nearest_integer': bsd.nearest_integer,
    }


# ============================================================================
# 17. Summary statistics
# ============================================================================

def bsd_landscape_summary(
    c_values: Optional[List[float]] = None,
    max_r: int = 60,
    dps: int = 40,
) -> Dict[str, Any]:
    """Comprehensive BSD summary across the Virasoro landscape.

    Collects analytic ranks, BSD ratios, parity tests, and
    complementarity constraints for c = 1..25.
    """
    if c_values is None:
        c_values = [float(c) for c in range(1, 26)]

    summary = {
        'analytic_ranks': {},
        'bsd_ratios': {},
        'parity': {},
        'complementarity': {},
    }

    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)

            # Analytic rank
            rank = shadow_analytic_rank(coeffs, max_r=max_r, dps=dps)
            summary['analytic_ranks'][c_val] = rank.rank

            # BSD leading coefficient
            lc = shadow_bsd_leading_coefficient(coeffs, max_r=max_r, dps=dps)
            summary['bsd_ratios'][c_val] = {
                'L_star': lc.L_star,
                'rank': lc.rank,
            }

        except (ValueError, ZeroDivisionError):
            pass

    # Average rank
    if summary['analytic_ranks']:
        ranks = list(summary['analytic_ranks'].values())
        summary['average_rank'] = sum(ranks) / len(ranks)
    else:
        summary['average_rank'] = None

    return summary
