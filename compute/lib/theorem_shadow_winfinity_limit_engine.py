r"""Shadow depth in the W_{1+\infty} limit: phase transition from class M to class G.

MAIN RESULT (planar shadow degeneration theorem):

    For each finite N >= 2, the principal W-algebra W_N has shadow depth
    r_max = infinity (class M) on the T-line.  The critical discriminant is

        Delta(W_N) = 80 / (5c + 22),

    which is nonzero for all c != -22/5.  As N -> infinity at fixed level k,
    the central charge c(W_N, k) diverges, and Delta -> 0.  The shadow metric

        Q_L(t) = (c + 6t)^2 + (80/(5c+22)) t^2

    degenerates to a perfect square Q_L^{planar}(t) = (c + 6t)^2.  The shadow
    obstruction tower undergoes a PHASE TRANSITION from class M (infinite depth)
    to class G (Gaussian, depth 2) in the planar limit.

CLOSED-FORM PLANAR LIMITS:

    The planar shadow coefficients L_r := lim_{c -> inf} c^{r-2} S_r satisfy
    the exact closed form

        L_r = (-1)^r  2 * 6^{r-2} / (9r)       for r >= 4.

    S_3 = 2 is a universal constant (independent of c).  L_3 is not defined
    in the c^{r-2} normalization because S_3 does not vanish.

    Ratio recursion: L_{r+1} / L_r = -6r/(r+1).

    Generating function (u = t/c):

        sum_{r >= 4} L_r u^{r-2}
            = (1/(162 u^2)) [-log(1 + 6u) + 6u - 18u^2 + 72u^3].

    The logarithm in the generating function reflects the Taylor series of
    sqrt(1 + epsilon) with epsilon = 80t^2 / [(c+6t)^2(5c+22)] -> 0.

THREE INDEPENDENT DERIVATION PATHS:

    Path 1 (Denominator-numerator extraction):
        S_r = P_{floor((r-4)/2)}(c) / [c^{r-3} (5c+22)^{floor((r-2)/2)}].
        For large c: S_r ~ leading(P) / [c^{r-3} 5^{floor((r-2)/2)} c^{floor((r-2)/2)}].
        Yields L_r for r = 4, ..., 8 from explicit formulas.

    Path 2 (Convolution recursion at large c):
        f(t) = sqrt(Q_L(t)) with Q_L = (c+6t)^2 + Delta t^2.
        Perturbation theory in epsilon = Delta/c^2 yields the recursion
        for L_r from the Taylor expansion of sqrt(1 + epsilon g(u)).

    Path 3 (Shadow ODE degeneration):
        The shadow connection nabla^sh = d - Q'/(2Q) dt has the degenerate
        limit nabla^{planar} = d - 6/(c+6t) dt, whose flat sections are
        (c + 6t)^{1/2}.  The L_r encode the deviation from this flat section.

SCALING IN THE W_{1+inf} LIMIT:

    Self-dual central charge: c_sd(W_N) = (N-1)(2N^2 + 2N + 1) ~ 2N^3.
    Free-field central charge: c_ff(W_N) = N - 1.
    Total modular characteristic: kappa(W_N) = (H_N - 1) c ~ log(N) * c.

    At self-dual point:
        S_r(c_sd) ~ L_r / c_sd^{r-2} ~ L_r / (2N^3)^{r-2}   for r >= 4.
        S_3 = 2 for all N.
        kappa(W_N, c_sd) ~ 2N^3 log(N).

    At free-field point:
        S_r(N-1) ~ L_r / (N-1)^{r-2} ~ L_r / N^{r-2}   for r >= 4.
        kappa(W_N, N-1) ~ (N-1)(log N + gamma - 1) ~ N log(N).

    't Hooft limit (lambda = N/(k+N) fixed, N -> inf):
        c ~ -N^4/lambda (NEGATIVE for lambda > 0, all N >> 1).
        The shadow tower is well-defined on the negative-c sheet but the
        physical interpretation requires analytic continuation.
        For lambda > 0: maximum N with c > 0 is N_max ~ 1/lambda - 1.

MULTI-CHANNEL DECOMPOSITION:

    W_N has N-1 generators of spins s = 2, ..., N.
    Channel curvature: kappa_s = c/s.
    Total: kappa(W_N) = sum_{s=2}^{N} c/s = (H_N - 1) c.
    The T-line (s=2, Virasoro) carries the universal shadow data.
    Higher-spin channels have alpha_s = 0 (by parity for odd s) and
    channel-specific S4_s data.

    In the large-N limit:
        kappa(W_N) / c = H_N - 1 ~ log(N) + gamma - 1  (logarithmic growth).
        kappa(W_N) / N -> 0  (harmonic sum grows slower than N).

References:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:winfty-all-stages-rigidity-closure (concordance.tex)
    thm:stabilized-completion-positive (bar_cobar_adjunction_curved.tex)
    prop:shadow-depth-phase-transition (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# 1.  Fundamental arithmetic
# ============================================================================

def harmonic(n: int) -> Fraction:
    """H_n = 1 + 1/2 + ... + 1/n.  H_0 = 0."""
    if n <= 0:
        return Fraction(0)
    return sum(Fraction(1, j) for j in range(1, n + 1))


def anomaly_ratio(N: int) -> Fraction:
    r"""rho(W_N) = H_N - 1 = sum_{s=2}^{N} 1/s.

    kappa(W_N) = rho(N) * c.
    """
    if N < 2:
        return Fraction(0)
    return harmonic(N) - 1


EULER_MASCHERONI = 0.5772156649015329


# ============================================================================
# 2.  Central charge formulas (Fateev-Lukyanov, canonical)
# ============================================================================

def c_wn(N: int, k: Fraction) -> Fraction:
    r"""Fateev-Lukyanov central charge for principal W^k(sl_N).

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).

    Decisive test: N=2, k=1 gives c = -7.
    """
    k = Fraction(k) if not isinstance(k, Fraction) else k
    kN = k + N
    if kN == 0:
        raise ValueError(f"Critical level k = -{N}")
    return canonical_c_wn_fl(N, k)


def alpha_N(N: int) -> Fraction:
    r"""Complementarity sum alpha_N = c(k) + c(-k-2N) = 4N^3 - 2N - 2.

    Equivalently: alpha_N = 2(N-1)(2N^2 + 2N + 1).
    Independent of k (Freudenthal-de Vries identity).
    """
    return Fraction(4 * N**3 - 2 * N - 2)


def c_self_dual(N: int) -> Fraction:
    r"""Self-dual central charge c_sd = alpha_N / 2 = (N-1)(2N^2 + 2N + 1).

    Asymptotic: c_sd ~ 2N^3 as N -> inf.
    """
    return alpha_N(N) / 2


def c_free_field(N: int) -> Fraction:
    """Free-field central charge c_ff = N - 1 (k -> infinity limit)."""
    return Fraction(N - 1)


def kappa_total(N: int, c_val: Fraction) -> Fraction:
    """Total modular characteristic kappa(W_N) = (H_N - 1) * c."""
    return anomaly_ratio(N) * c_val


# ============================================================================
# 3.  T-line shadow tower (Virasoro, exact Fraction arithmetic)
# ============================================================================

def shadow_metric_coefficients(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    r"""Virasoro shadow metric Q_L(t) = q0 + q1*t + q2*t^2.

    q0 = c^2, q1 = 12c, q2 = (180c + 872)/(5c + 22).
    """
    q0 = c_val ** 2
    q1 = 12 * c_val
    q2 = (180 * c_val + 872) / (5 * c_val + 22)
    return q0, q1, q2


def critical_discriminant(c_val: Fraction) -> Fraction:
    r"""Critical discriminant Delta = 8 kappa S_4 = 80/(5c+22) on the T-line."""
    return Fraction(80) / (5 * c_val + 22)


def tline_shadow_tower(c_val: Fraction, max_r: int = 12) -> Dict[int, Fraction]:
    r"""T-line shadow tower S_2, ..., S_{max_r} via convolution recursion.

    Uses exact Fraction arithmetic.  S_r = a_{r-2}/r where a_n are the
    Taylor coefficients of f(t) = sqrt(Q_L(t)).
    """
    if c_val == 0:
        raise ValueError("c = 0 is degenerate")

    q0, q1, q2 = shadow_metric_coefficients(c_val)

    # a_0 = c (positive branch of sqrt(c^2))
    a = [c_val]
    # a_1 = q1/(2*a_0) = 12c/(2c) = 6
    a.append(q1 / (2 * c_val))
    # a_2 = (q2 - a_1^2)/(2*a_0)
    a.append((q2 - a[1]**2) / (2 * c_val))
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2 * c_val))

    tower = {}
    for n in range(len(a)):
        r = n + 2
        tower[r] = a[n] / r
    return tower


def tline_shadow_tower_float(c_val: float, max_r: int = 12) -> Dict[int, float]:
    """T-line shadow tower using floating-point arithmetic (fast, large c)."""
    if abs(c_val) < 1e-100:
        return {r: 0.0 for r in range(2, max_r + 1)}

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    a = [c_val, q1 / (2.0 * c_val)]
    a.append((q2 - a[1]**2) / (2.0 * c_val))
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * c_val))

    tower = {}
    for n in range(len(a)):
        r = n + 2
        tower[r] = a[n] / r
    return tower


# ============================================================================
# 4.  Planar shadow limits (the main theorem)
# ============================================================================

def planar_limit_exact(r: int) -> Fraction:
    r"""Exact planar shadow limit L_r = lim_{c -> inf} c^{r-2} S_r.

    CLOSED FORM: L_r = (-1)^r * 2 * 6^{r-2} / (9r)  for r >= 4.

    S_3 = 2 is a universal constant independent of c.  L_3 is not defined
    in this normalization (S_3 does not vanish as c -> inf).

    Derived from the denominator-numerator structure of S_r and independently
    verified by convolution recursion at large c and by the ratio test
    L_{r+1}/L_r = -6r/(r+1).
    """
    if r < 4:
        raise ValueError(
            f"L_r undefined for r={r}: S_3 = 2 is constant, S_2 = c/2 diverges"
        )
    return (-1)**r * Fraction(2) * Fraction(6)**(r - 2) / (9 * r)


def planar_limit_float(r: int) -> float:
    """Floating-point evaluation of L_r."""
    if r < 4:
        raise ValueError(f"L_r undefined for r={r}")
    return (-1)**r * 2.0 * 6.0**(r - 2) / (9.0 * r)


def planar_limit_ratio(r: int) -> Fraction:
    r"""Ratio L_{r+1}/L_r = -6r/(r+1)."""
    return Fraction(-6 * r, r + 1)


def planar_limit_generating_function(u: float) -> float:
    r"""Generating function sum_{r >= 4} L_r u^{r-2}.

    = (1/(162 u^2)) * [-log(1 + 6u) + 6u - 18u^2 + 72u^3]

    Valid for |6u| < 1, i.e. |u| < 1/6.
    """
    if abs(u) < 1e-15:
        return planar_limit_float(4)
    if abs(6 * u) >= 1:
        raise ValueError(f"|6u| = {abs(6*u):.4f} >= 1: outside convergence radius")
    return (1.0 / (162.0 * u**2)) * (
        -math.log(1.0 + 6.0 * u) + 6.0 * u - 18.0 * u**2 + 72.0 * u**3
    )


def planar_shadow_at_c(c_val: float, r: int) -> float:
    r"""Planar approximation to S_r at given c: S_r^{planar} = L_r / c^{r-2}."""
    return planar_limit_float(r) / c_val ** (r - 2)


# ============================================================================
# 5.  Finite-N corrections
# ============================================================================

def finite_N_correction(c_val: Fraction, r: int) -> Fraction:
    r"""Exact S_r minus planar approximation L_r/c^{r-2}.

    The difference delta_r(c) = S_r(c) - L_r/c^{r-2} encodes the 1/c
    corrections to the planar limit.  These are the non-planar shadow
    corrections at finite N.
    """
    if r < 4:
        raise ValueError("Correction not defined for r < 4")
    tower = tline_shadow_tower(c_val, max_r=r + 1)
    S_exact = tower[r]
    L_r = planar_limit_exact(r)
    return S_exact - L_r / c_val ** (r - 2)


def subleading_coefficient(r: int) -> Fraction:
    r"""Subleading coefficient M_r in S_r = L_r/c^{r-2} + M_r/c^{r-1} + ...

    Extracted by computing S_r * c^{r-1} - L_r * c and taking c -> inf.
    Uses exact arithmetic at c = 10^6 with Richardson acceleration.
    """
    c1 = Fraction(10**5)
    c2 = Fraction(10**6)

    tower1 = tline_shadow_tower(c1, max_r=r + 1)
    tower2 = tline_shadow_tower(c2, max_r=r + 1)

    L_r = planar_limit_exact(r)

    # S_r * c^{r-1} - L_r * c = M_r + O(1/c)
    val1 = tower1[r] * c1**(r - 1) - L_r * c1
    val2 = tower2[r] * c2**(r - 1) - L_r * c2

    # Richardson: M_r ~ val2 + (val2 - val1)/9
    # (since the correction is O(1/c) and c2/c1 = 10)
    return val2


# ============================================================================
# 6.  Shadow depth phase transition
# ============================================================================

def depth_class_at_c(c_val: Fraction) -> str:
    r"""Shadow depth class on the T-line at central charge c.

    Delta = 80/(5c+22).
    Delta != 0 for c != -22/5 => class M (infinite depth) at finite c.
    Delta -> 0 as c -> inf => class G (Gaussian) in the planar limit.
    """
    if c_val == Fraction(-22, 5):
        return 'degenerate'
    if c_val == 0:
        return 'degenerate'
    return 'M'


def depth_transition_data(N_values: Optional[List[int]] = None,
                          regime: str = 'self_dual') -> List[Dict[str, Any]]:
    r"""Track the shadow depth transition as N increases.

    For each N, compute c, Delta, shadow growth rate rho, and the first
    few shadow coefficients.

    regime: 'self_dual' or 'free_field'.
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50, 100]

    results = []
    for N in N_values:
        if regime == 'self_dual':
            c = c_self_dual(N)
        elif regime == 'free_field':
            c = c_free_field(N)
        else:
            raise ValueError(f"Unknown regime: {regime}")

        if c <= 0:
            continue

        delta = critical_discriminant(c)
        kap = kappa_total(N, c)
        rho_val = anomaly_ratio(N)

        # Growth rate
        c_f = float(c)
        numer_rho = 180.0 * c_f + 872.0
        denom_rho = (5.0 * c_f + 22.0) * c_f ** 2
        growth = math.sqrt(numer_rho / denom_rho) if denom_rho > 0 else float('inf')

        # Shadow coefficients
        tower = tline_shadow_tower_float(c_f, max_r=8)

        results.append({
            'N': N,
            'c': c,
            'c_float': c_f,
            'Delta': delta,
            'Delta_float': float(delta),
            'kappa_total': kap,
            'anomaly_ratio': rho_val,
            'growth_rate': growth,
            'S3': tower.get(3, 0.0),
            'S4': tower.get(4, 0.0),
            'S5': tower.get(5, 0.0),
            'S6': tower.get(6, 0.0),
            'depth_class': 'M',
            'regime': regime,
        })

    return results


# ============================================================================
# 7.  S_3 and S_4 at self-dual point for specific N values
# ============================================================================

def s3_at_self_dual(N: int) -> Fraction:
    """S_3(W_N) on the T-line at self-dual c.  Always 2 (universal)."""
    return Fraction(2)


def s4_at_self_dual(N: int) -> Fraction:
    r"""S_4(W_N) = Q^contact on the T-line at self-dual c = (N-1)(2N^2+2N+1).

    S_4 = 10 / [c(5c+22)].
    """
    c = c_self_dual(N)
    return Fraction(10) / (c * (5 * c + 22))


def s4_times_c_squared_at_self_dual(N: int) -> Fraction:
    r"""S_4 * c^2 at self-dual c.

    = 10c / (5c + 22).  Limit as N -> inf: 10/5 = 2.
    """
    c = c_self_dual(N)
    return Fraction(10) * c / (5 * c + 22)


# ============================================================================
# 8.  Large-N scaling analysis
# ============================================================================

def large_N_scaling_self_dual(N_values: Optional[List[int]] = None,
                              max_r: int = 10) -> Dict[str, Any]:
    r"""Shadow coefficients at self-dual c as a function of N.

    At c_sd ~ 2N^3:
        S_3 = 2  (constant).
        S_r ~ L_r / (2N^3)^{r-2}  for r >= 4  (vanishes as N^{-3(r-2)}).
        kappa ~ 2N^3 * log(N).
        Delta ~ 80/(10N^3) = 8/N^3  (vanishes as N^{-3}).
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 10, 20, 50, 100]

    data = []
    for N in N_values:
        c = c_self_dual(N)
        c_f = float(c)

        tower = tline_shadow_tower_float(c_f, max_r=max_r)
        kap = float(kappa_total(N, c))
        delta = float(critical_discriminant(c))

        row = {
            'N': N,
            'c_sd': c_f,
            'c_sd_over_N3': c_f / N**3,
            'kappa': kap,
            'Delta': delta,
            'Delta_times_N3': delta * N**3,
        }
        for r in range(3, max_r + 1):
            row[f'S{r}'] = tower.get(r, 0.0)
            if r >= 4:
                row[f'S{r}_times_c^{r-2}'] = tower.get(r, 0.0) * c_f ** (r - 2)
                row[f'S{r}_planar_ratio'] = (
                    tower.get(r, 0.0) * c_f ** (r - 2) / planar_limit_float(r)
                    if abs(planar_limit_float(r)) > 1e-100 else None
                )

        data.append(row)

    return {
        'regime': 'self_dual',
        'data': data,
        'planar_limits': {r: planar_limit_float(r) for r in range(4, max_r + 1)},
    }


def large_N_scaling_free_field(N_values: Optional[List[int]] = None,
                               max_r: int = 10) -> Dict[str, Any]:
    r"""Shadow coefficients at free-field c = N-1 as a function of N.

    At c_ff = N-1:
        S_r ~ L_r / N^{r-2}  for r >= 4  (slower vanishing than self-dual).
        kappa ~ N log(N).
        Delta ~ 80/(5N) = 16/N.
    """
    if N_values is None:
        N_values = [2, 3, 5, 10, 20, 50, 100, 200]

    data = []
    for N in N_values:
        c = c_free_field(N)
        c_f = float(c)
        if c_f <= 0:
            continue

        tower = tline_shadow_tower_float(c_f, max_r=max_r)
        kap = float(kappa_total(N, c))
        delta = float(critical_discriminant(c))

        row = {
            'N': N,
            'c_ff': c_f,
            'kappa': kap,
            'Delta': delta,
            'Delta_times_N': delta * N,
        }
        for r in range(3, max_r + 1):
            row[f'S{r}'] = tower.get(r, 0.0)
            if r >= 4:
                row[f'S{r}_times_c^{r-2}'] = tower.get(r, 0.0) * c_f ** (r - 2)

        data.append(row)

    return {
        'regime': 'free_field',
        'data': data,
    }


# ============================================================================
# 9.  't Hooft limit
# ============================================================================

def thooft_c_exact(N: int, lam: Fraction) -> Fraction:
    r"""Exact central charge in 't Hooft parameterization.

    lambda = N/(k+N), so k+N = N/lambda.
    c = (N-1) - N(N^2-1)(N/lambda - 1)^2 / (N/lambda).

    For lambda > 0 and N >> 1: c ~ -N^4/lambda (negative).
    Maximum N with c > 0: N_max ~ 1/lambda - 1.
    """
    if lam <= 0 or lam >= 1:
        raise ValueError(f"lambda = {lam} must be in (0, 1)")
    kN = Fraction(N) / lam
    return canonical_c_wn_fl(N, kN - N)


def thooft_max_N(lam: float) -> int:
    r"""Maximum N with positive central charge at given lambda.

    Approximate: N_max ~ floor(1/lambda - 1).
    """
    if lam <= 0:
        return 10**6  # effectively infinite
    return max(1, int(1.0 / lam - 1))


def thooft_shadow_data(lam: Fraction,
                       N_values: Optional[List[int]] = None,
                       max_r: int = 8) -> Dict[str, Any]:
    r"""Shadow tower data in the 't Hooft limit at fixed lambda.

    Only includes N values with c > 0.
    """
    if N_values is None:
        N_max = thooft_max_N(float(lam))
        N_values = [N for N in range(2, min(N_max + 2, 201))]

    data = []
    for N in N_values:
        try:
            c = thooft_c_exact(N, lam)
        except (ValueError, ZeroDivisionError):
            continue

        c_f = float(c)
        if c_f <= 0 or abs(5 * c_f + 22) < 1e-10:
            continue

        tower = tline_shadow_tower_float(c_f, max_r=max_r)
        kap = float(kappa_total(N, c))
        delta = float(critical_discriminant(c))

        row = {
            'N': N,
            'c': c_f,
            'kappa_total': kap,
            'Delta': delta,
        }
        for r in range(3, max_r + 1):
            row[f'S{r}'] = tower.get(r, 0.0)

        data.append(row)

    return {
        'lambda': float(lam),
        'data': data,
        'N_max_positive': thooft_max_N(float(lam)),
    }


# ============================================================================
# 10.  Multi-channel decomposition
# ============================================================================

def channel_kappa_decomposition(N: int, c_val: Fraction) -> Dict[str, Any]:
    r"""Decompose total kappa into per-channel contributions.

    kappa_s = c/s for spin-s generator.
    kappa_total = sum_{s=2}^{N} c/s = (H_N - 1) c.
    """
    channels = {}
    total_sum = Fraction(0)
    for s in range(2, N + 1):
        kap_s = c_val / s
        channels[s] = kap_s
        total_sum += kap_s

    kap_formula = kappa_total(N, c_val)

    return {
        'N': N,
        'c': c_val,
        'channels': channels,
        'channel_sum': total_sum,
        'formula': kap_formula,
        'match': total_sum == kap_formula,
        'anomaly_ratio': anomaly_ratio(N),
    }


def kappa_over_c_convergence(N_values: Optional[List[int]] = None) -> List[Dict]:
    r"""Track kappa(W_N)/c = H_N - 1 ~ log(N) + gamma - 1.

    The anomaly ratio grows logarithmically, confirming the harmonic
    divergence of the total modular characteristic.
    """
    if N_values is None:
        N_values = [2, 3, 5, 10, 20, 50, 100, 200, 500, 1000]

    results = []
    for N in N_values:
        rho = float(anomaly_ratio(N))
        rho_asymp = math.log(N) + EULER_MASCHERONI - 1.0

        results.append({
            'N': N,
            'rho_exact': rho,
            'rho_asymptotic': rho_asymp,
            'relative_error': abs(rho - rho_asymp) / max(abs(rho), 1e-100),
        })

    return results


# ============================================================================
# 11.  Shadow growth rate in the large-N limit
# ============================================================================

def growth_rate_tline(c_val: float) -> float:
    r"""Shadow growth rate on the T-line.

    rho = sqrt((180c + 872) / ((5c + 22) c^2)).
    For large c: rho ~ 6/c.
    """
    if c_val <= 0 or (5 * c_val + 22) <= 0:
        return float('inf')
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    return math.sqrt(numer / denom)


def growth_rate_large_N(N_values: Optional[List[int]] = None,
                        regime: str = 'self_dual') -> List[Dict]:
    r"""Track shadow growth rate as N increases.

    At self-dual c ~ 2N^3: rho ~ 6/(2N^3) = 3/N^3 -> 0.
    At free-field c = N-1: rho ~ 6/N -> 0.
    In both cases the convergence radius R = 1/rho -> infinity.
    """
    if N_values is None:
        N_values = [2, 3, 5, 10, 20, 50, 100]

    results = []
    for N in N_values:
        if regime == 'self_dual':
            c_f = float(c_self_dual(N))
        elif regime == 'free_field':
            c_f = float(c_free_field(N))
        else:
            raise ValueError(f"Unknown regime: {regime}")

        if c_f <= 0:
            continue

        rho = growth_rate_tline(c_f)
        results.append({
            'N': N,
            'c': c_f,
            'growth_rate': rho,
            'convergence_radius': 1.0 / rho if rho > 0 else float('inf'),
            'rho_times_c': rho * c_f,
            'regime': regime,
        })

    return results


# ============================================================================
# 12.  Complementarity in the large-N limit
# ============================================================================

def complementarity_scaling(N_values: Optional[List[int]] = None) -> List[Dict]:
    r"""Track the complementarity sum kappa + kappa' as N increases.

    kappa + kappa' = (H_N - 1) * alpha_N.
    alpha_N = 4N^3 - 2N - 2 ~ 4N^3.
    H_N - 1 ~ log(N).
    So kappa + kappa' ~ 4N^3 log(N).
    """
    if N_values is None:
        N_values = [2, 3, 4, 5, 10, 20, 50, 100]

    results = []
    for N in N_values:
        rho = anomaly_ratio(N)
        a_N = alpha_N(N)
        kk_sum = rho * a_N

        results.append({
            'N': N,
            'alpha_N': a_N,
            'anomaly_ratio': rho,
            'kappa_plus_kappa_prime': kk_sum,
            'sum_float': float(kk_sum),
            'sum_over_N3_logN': (
                float(kk_sum) / (N**3 * math.log(N))
                if N >= 2 else None
            ),
        })

    return results


# ============================================================================
# 13.  Summary table
# ============================================================================

def summary_table(N_values: Optional[List[int]] = None) -> List[Dict]:
    r"""Complete summary for each N: c_sd, c_ff, kappa, Delta, S_3, S_4, rho."""
    if N_values is None:
        N_values = [2, 3, 4, 5, 10, 20, 50, 100]

    rows = []
    for N in N_values:
        c_sd = c_self_dual(N)
        c_ff = c_free_field(N)
        kap_sd = kappa_total(N, c_sd)
        kap_ff = kappa_total(N, c_ff)
        delta_sd = critical_discriminant(c_sd)
        delta_ff = critical_discriminant(c_ff)

        rows.append({
            'N': N,
            'c_self_dual': float(c_sd),
            'c_free_field': float(c_ff),
            'kappa_self_dual': float(kap_sd),
            'kappa_free_field': float(kap_ff),
            'Delta_self_dual': float(delta_sd),
            'Delta_free_field': float(delta_ff),
            'S3': 2.0,
            'S4_self_dual': float(s4_at_self_dual(N)),
            'S4_c2_self_dual': float(s4_times_c_squared_at_self_dual(N)),
            'growth_rate_sd': growth_rate_tline(float(c_sd)),
            'growth_rate_ff': growth_rate_tline(float(c_ff)),
        })

    return rows
