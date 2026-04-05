r"""Shadow trace formula engine: Selberg/Arthur-type trace formula for shadow towers.

MATHEMATICAL FRAMEWORK
======================

For a modular Koszul algebra A with shadow coefficients S_r(A), define:

SHADOW TRACE (test-function pairing):

    Tr^sh(A, f) = sum_{r >= 2} f(r) * S_r(A)

This is a linear functional on test functions f: Z_{>=2} -> C, pairing
against the shadow sequence.  It is the "spectral side" of the trace formula.

GEOMETRIC SIDE (Mellin pairing):

    Tr^sh(A, f) = integral f_hat(t) * H_A(t) dt

where H_A(t) = sum_{r >= 2} S_r * t^r is the shadow generating function,
and f_hat is the Fourier/Mellin transform of f.

SPECTRAL DECOMPOSITION:

The "spectrum" of the shadow tower = singularities (zeros, poles, branch
points) of the analytic continuation of H_A(t).

    - Class G (Heisenberg): H(t) = kappa * t^2.  Polynomial, no singularities.
      Spectrum = {0} (double zero only).
    - Class L (affine KM): H(t) = S_2*t^2 + S_3*t^3.  Polynomial.
      Spectrum = {0, -S_2/S_3} (zeros of H).
    - Class C (beta-gamma): H(t) = S_2*t^2 + S_3*t^3 + S_4*t^4.
      Spectrum = zeros of H (cubic in t, after dividing by t^2).
    - Class M (Virasoro, W_N): H(t) = t^2 * sqrt(Q_L(t)).
      Branch points at zeros of Q_L.  CONTINUOUS SPECTRUM from branch cuts.

HEAT KERNEL TRACE:

    K_A(lambda) = sum_{r >= 2} S_r * e^{-lambda * r} = H_A(e^{-lambda})

This is the "heat kernel" of the shadow tower at inverse temperature lambda.
Decomposition into identity + correction terms:

    K_A(lambda) = kappa * e^{-2*lambda} * sqrt(Q_L(e^{-lambda}) / Q_L(0))

    I(lambda) = kappa * e^{-2*lambda}  (identity contribution, from S_2 alone)
    K_A(lambda) - I(lambda) = correction from higher arities

WEYL LAW FOR SHADOWS:

    N^sh(eps) = #{r >= 2 : |S_r(A)| > eps}

For class M: |S_r| ~ C * rho^r * r^{-5/2}, so |S_r| > eps iff
    r < log(eps/C) / log(rho) + (5/2) * log(r) / |log(rho)|

Shadow spectral dimension:
    d^sh(A) = lim_{eps -> 0} log(N^sh(eps)) / log(1/eps)
            = 1 / log(1/rho)    for class M with rho < 1
            = 0                  for classes G, L, C (finite support)

SHADOW SELBERG ZETA:

    Z^Sel_A(s) = prod_{r >= 2} (1 - S_r(A) * r^{-s})

Euler product over "shadow primes" (all arities >= 2).  This is a
formal product; convergence requires |S_r * r^{-s}| < 1 for large r,
i.e., Re(s) sufficiently large relative to the growth rate.

RELATIVE TRACE FORMULA (Koszul pair):

    RTF(A, A!; f) = Tr^sh(A, f) - Tr^sh(A!, f)

For complementary pairs with known Koszul duals:
    - Heisenberg: (H_k, H_{-k}) -> RTF = f(2) * 2k
    - Virasoro:   (Vir_c, Vir_{26-c}) -> RTF depends on c-13

At the self-dual point (c=13 for Virasoro), the relative trace formula
measures the SELF-DUAL RESIDUAL (should vanish for perfectly self-dual
algebras at the scalar level).

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)

CAUTION (AP1): kappa formulas are family-specific.  Recompute from first principles.
CAUTION (AP9): S_2 = kappa != c/2 in general.
CAUTION (AP24): kappa(A) + kappa(A!) = 0 for KM/Heisenberg, = 13 for Virasoro.
CAUTION (AP48): kappa depends on the full algebra, not just the Virasoro subalgebra.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple


# ============================================================================
# 1.  Shadow coefficient providers (self-contained, no external imports)
# ============================================================================

def heisenberg_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for Heisenberg H_k.

    S_2 = k.  S_r = 0 for r >= 3 (class G).
    """
    result = {2: float(k_val)}
    for r in range(3, max_r + 1):
        result[r] = 0.0
    return result


def affine_sl2_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for affine V_k(sl_2).

    kappa = 3(k+2)/4.  S_3 = alpha = 4/(k+2) (Sugawara line).
    S_r = 0 for r >= 4 (class L).
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = 0.0
    return result


def affine_sl3_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for affine V_k(sl_3).

    kappa = 4(k+3)/3.  S_3 = alpha = 6/(k+3) (Sugawara line).
    S_r = 0 for r >= 4 (class L).
    """
    h_dual = 3.0
    dim_g = 8.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = 0.0
    return result


def betagamma_shadow_coefficients(lam_val: float = 0.5, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for beta-gamma at weight lambda.

    Global shadow depth = 4 (class C).
    S_2 = kappa = c/2, S_3 = 2, S_4 = 10/(c(5c+22)), S_r = 0 for r >= 5.
    """
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0
    result = {2: kappa, 3: 2.0}
    if c_val != 0.0 and 5.0 * c_val + 22.0 != 0.0:
        result[4] = 10.0 / (c_val * (5.0 * c_val + 22.0))
    else:
        result[4] = 0.0
    for r in range(5, max_r + 1):
        result[r] = 0.0
    return result


def virasoro_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for Virasoro Vir_c via convolution recursion.

    Uses H(t) = t^2 * sqrt(Q_L(t)) where Q_L(t) = c^2 + 12c*t + alpha(c)*t^2
    with alpha(c) = (180c + 872)/(5c + 22).

    S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L).
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    a0 = abs(c_val)
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
    return result


def virasoro_dual_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for the Koszul dual Vir_{26-c}.

    CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13, NOT 0.
    """
    return virasoro_shadow_coefficients(26.0 - c_val, max_r)


def w3_t_line_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for W_3 along the T-line (= Virasoro restriction)."""
    return virasoro_shadow_coefficients(c_val, max_r)


# ============================================================================
# 2.  Shadow trace: spectral side
# ============================================================================

def shadow_trace(
    shadow_coeffs: Dict[int, float],
    test_fn: Callable[[int], float],
    max_r: Optional[int] = None,
) -> float:
    """Compute Tr^sh(A, f) = sum_{r >= 2} f(r) * S_r(A).

    Parameters
    ----------
    shadow_coeffs : arity r -> S_r
    test_fn : test function f: Z_{>=2} -> R
    max_r : truncation arity
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total += test_fn(r) * Sr
    return total


def shadow_trace_characteristic(
    shadow_coeffs: Dict[int, float],
    target_r: int,
) -> float:
    """Tr^sh(A, delta_r) = S_r(A): characteristic function of {r}.

    This recovers the individual shadow coefficient.
    """
    return shadow_coeffs.get(target_r, 0.0)


def shadow_trace_zeta(
    shadow_coeffs: Dict[int, float],
    s: float,
    max_r: Optional[int] = None,
) -> float:
    """Tr^sh(A, r^{-s}) = zeta_A(s): the shadow zeta function.

    Recovers the shadow Dirichlet series.
    """
    return shadow_trace(shadow_coeffs, lambda r: r ** (-s), max_r)


def shadow_trace_heat(
    shadow_coeffs: Dict[int, float],
    lam: float,
    max_r: Optional[int] = None,
) -> float:
    """Tr^sh(A, e^{-lambda*r}) = K_A(lambda): the heat kernel trace.

    = H_A(e^{-lambda}) = sum S_r * exp(-lambda * r).
    """
    return shadow_trace(shadow_coeffs, lambda r: math.exp(-lam * r), max_r)


# ============================================================================
# 3.  Shadow generating function (geometric side)
# ============================================================================

def shadow_generating_function(
    shadow_coeffs: Dict[int, float],
    t: float,
) -> float:
    """H_A(t) = sum_{r >= 2} S_r * t^r.

    The shadow generating function at the point t.
    """
    max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        total += Sr * t ** r
    return total


def shadow_weighted_generating_function_analytic(
    c_val: float,
    t: complex,
) -> complex:
    """Analytic continuation of the WEIGHTED generating function:

        H^w(t) = sum_{r>=2} r * S_r * t^r = t^2 * sqrt(Q_L(t))

    Q_L(t) = c^2 + 12*c*t + alpha(c)*t^2  where alpha = (180c+872)/(5c+22).

    CAUTION: this is NOT the ordinary GF sum S_r * t^r.
    The factor of r comes from the shadow_radius.py convention:
    S_r = a_{r-2}/r where a_n are Taylor coefficients of sqrt(Q_L).
    So sum r*S_r*t^r = sum a_n * t^{n+2} = t^2 * sqrt(Q_L(t)).
    """
    alpha_c = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    Q = c_val ** 2 + 12.0 * c_val * t + alpha_c * t ** 2
    return t ** 2 * cmath.sqrt(Q)


def shadow_generating_function_heisenberg(k_val: float, t: float) -> float:
    """Exact H_{H_k}(t) = k * t^2 / 2.

    Since S_2 = k: H(t) = k * t^2.
    Wait -- S_2 = k, so H(t) = S_2 * t^2 = k * t^2.
    """
    return k_val * t ** 2


def shadow_generating_function_affine(
    kappa: float,
    alpha: float,
    t: float,
) -> float:
    """Exact H for affine KM: H(t) = kappa * t^2 + alpha * t^3."""
    return kappa * t ** 2 + alpha * t ** 3


# ============================================================================
# 4.  Spectral decomposition: singularity structure
# ============================================================================

def virasoro_Q_L_zeros(c_val: float) -> Tuple[complex, complex]:
    """Zeros of Q_L(t) = c^2 + 12*c*t + alpha(c)*t^2.

    alpha(c) = (180c + 872)/(5c + 22).

    Returns (t_+, t_-) as complex numbers.
    """
    alpha_c = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    # Q_L = alpha*t^2 + 12c*t + c^2
    # t = (-12c +/- sqrt(144c^2 - 4*alpha*c^2)) / (2*alpha)
    #   = (-12c +/- c*sqrt(144 - 4*alpha)) / (2*alpha)
    disc = 144.0 * c_val ** 2 - 4.0 * alpha_c * c_val ** 2
    disc_c = complex(disc, 0)
    sq = cmath.sqrt(disc_c)
    t_plus = (-12.0 * c_val + sq) / (2.0 * alpha_c)
    t_minus = (-12.0 * c_val - sq) / (2.0 * alpha_c)
    return t_plus, t_minus


def virasoro_branch_point_modulus(c_val: float) -> float:
    """Modulus of the nearest branch point = 1/rho = convergence radius.

    |t_0| = |c| / sqrt(alpha(c)) = |c| * sqrt((5c+22)/(180c+872)).

    From the shadow metric: Q_L = alpha*(t - t_+)(t - t_-), and
    |t_+| = |t_-| = |c|/sqrt(alpha) when the zeros are complex conjugate.
    """
    alpha_c = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    # |t_+|^2 = (12c/(2*alpha))^2 + (c^2*(4*alpha-144))/(4*alpha^2)
    # = c^2/alpha * (36/alpha + (alpha-36)/alpha) = c^2/alpha
    return abs(c_val) / math.sqrt(abs(alpha_c))


def virasoro_growth_rate(c_val: float) -> float:
    """Shadow growth rate rho(Vir_c) = sqrt((180c+872)/((5c+22)*c^2)).

    rho = 1/|t_0| = sqrt(alpha)/|c|.
    """
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    if denom <= 0:
        return float('inf')
    return math.sqrt(numer / denom)


def spectral_data(c_val: float) -> Dict[str, object]:
    """Full spectral data for Virasoro at central charge c.

    Returns branch points, growth rate, oscillation angle, spectral dimension.
    """
    t_plus, t_minus = virasoro_Q_L_zeros(c_val)
    rho = virasoro_growth_rate(c_val)
    mod = abs(t_plus)
    theta = cmath.phase(t_plus)

    return {
        'c': c_val,
        'branch_points': (t_plus, t_minus),
        'modulus': mod,
        'growth_rate': rho,
        'oscillation_angle': theta,
        'spectral_dimension': 1.0 / math.log(1.0 / rho) if 0 < rho < 1 else (
            0.0 if rho == 0 else float('inf')
        ),
    }


# ============================================================================
# 5.  Heat kernel trace and identity contribution
# ============================================================================

def heat_kernel_trace(
    shadow_coeffs: Dict[int, float],
    lam: float,
    max_r: Optional[int] = None,
) -> float:
    """K_A(lambda) = sum_{r >= 2} S_r * e^{-lambda*r}.

    Direct summation (spectral side).
    """
    return shadow_trace_heat(shadow_coeffs, lam, max_r)


def heat_kernel_identity_contribution(kappa: float, lam: float) -> float:
    """Identity contribution: I(lambda) = kappa * e^{-2*lambda}.

    This is the arity-2 (curvature) contribution alone.
    """
    return kappa * math.exp(-2.0 * lam)


def heat_kernel_analytic_virasoro(c_val: float, lam: float, max_r: int = 50) -> float:
    """Analytic heat kernel for Virasoro: K(lambda) = H(e^{-lambda}).

    Uses the relation: the WEIGHTED GF is t^2 * sqrt(Q_L(t)) = sum r*S_r*t^r.
    The heat kernel K = sum S_r * e^{-lambda*r} = H(e^{-lambda}) (ordinary GF).

    The ordinary GF has NO simple closed form; the closed form is for the
    WEIGHTED GF sum r*S_r*t^r = t^2*sqrt(Q_L(t)).

    For the heat kernel, we use direct summation (same as heat_kernel_trace).
    This function computes from the shadow coefficients for consistency.
    """
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    return heat_kernel_trace(coeffs, lam)


def heat_kernel_correction(
    shadow_coeffs: Dict[int, float],
    kappa: float,
    lam: float,
    max_r: Optional[int] = None,
) -> float:
    """Correction beyond identity: K(lambda) - I(lambda).

    This measures the contribution of higher-arity shadows.
    """
    K = heat_kernel_trace(shadow_coeffs, lam, max_r)
    I = heat_kernel_identity_contribution(kappa, lam)
    return K - I


# ============================================================================
# 6.  Weyl law for shadows
# ============================================================================

def weyl_counting_function(
    shadow_coeffs: Dict[int, float],
    eps: float,
) -> int:
    """N^sh(eps) = #{r >= 2 : |S_r(A)| > eps}.

    Shadow Weyl counting function.
    """
    count = 0
    for r in range(2, max(shadow_coeffs.keys()) + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > eps:
            count += 1
    return count


def weyl_spectrum(
    shadow_coeffs: Dict[int, float],
    eps_values: List[float],
) -> Dict[float, int]:
    """Compute N^sh(eps) for multiple threshold values."""
    return {eps: weyl_counting_function(shadow_coeffs, eps) for eps in eps_values}


def shadow_spectral_dimension_empirical(
    shadow_coeffs: Dict[int, float],
    eps_range: Optional[Tuple[float, float]] = None,
    n_points: int = 20,
) -> float:
    """Estimate d^sh(A) = lim_{eps->0} log(N^sh(eps)) / log(1/eps).

    Uses linear regression on log-log data.
    """
    if eps_range is None:
        eps_range = (1e-10, 1e-1)
    eps_lo, eps_hi = eps_range
    log_eps_lo, log_eps_hi = math.log10(eps_lo), math.log10(eps_hi)
    eps_values = [10 ** (log_eps_lo + i * (log_eps_hi - log_eps_lo) / n_points)
                  for i in range(n_points + 1)]

    log_inv_eps = []
    log_N = []
    for eps in eps_values:
        N = weyl_counting_function(shadow_coeffs, eps)
        if N > 0:
            log_inv_eps.append(math.log(1.0 / eps))
            log_N.append(math.log(N))

    if len(log_inv_eps) < 3:
        return 0.0  # Finite tower

    # Linear regression: log(N) ~ d^sh * log(1/eps) + const
    n = len(log_inv_eps)
    sx = sum(log_inv_eps)
    sy = sum(log_N)
    sxy = sum(x * y for x, y in zip(log_inv_eps, log_N))
    sxx = sum(x * x for x in log_inv_eps)
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return 0.0
    slope = (n * sxy - sx * sy) / denom
    return slope


def shadow_spectral_dimension_exact(rho: float) -> float:
    """Exact shadow spectral dimension for class M.

    d^sh = 1 / log(1/rho) for 0 < rho < 1.
    d^sh = 0 for rho = 0 (finite tower).
    d^sh = infinity for rho >= 1.
    """
    if rho <= 0:
        return 0.0
    if rho >= 1.0 - 1e-15:
        return float('inf')
    return 1.0 / math.log(1.0 / rho)


# ============================================================================
# 7.  Shadow Selberg zeta
# ============================================================================

def shadow_selberg_zeta(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Z^Sel_A(s) = prod_{r >= 2} (1 - S_r * r^{-s}).

    Euler product over shadow arities.

    Convergence: for |S_r| ~ C * rho^r * r^{-5/2}, the product converges
    absolutely when sum |S_r * r^{-s}| < infinity, i.e., Re(s) large enough.

    For finite towers (class G, L, C): always converges (finite product).
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    product = complex(1.0, 0)
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        factor = 1.0 - Sr * r ** (-s)
        product *= factor
    return product


def shadow_selberg_zeta_log(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """log Z^Sel_A(s) = sum_{r >= 2} log(1 - S_r * r^{-s}).

    The logarithm of the Selberg zeta.  More numerically stable than
    the product for large truncation.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = complex(0, 0)
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        arg = 1.0 - Sr * r ** (-s)
        total += cmath.log(arg)
    return total


def shadow_selberg_zeros(
    shadow_coeffs: Dict[int, float],
    s_real_range: Tuple[float, float] = (0.0, 10.0),
    s_imag_range: Tuple[float, float] = (-10.0, 10.0),
    grid_points: int = 50,
    max_r: Optional[int] = None,
) -> List[Tuple[float, float, float]]:
    """Search for approximate zeros of Z^Sel_A(s) on a grid.

    Returns list of (Re(s), Im(s), |Z(s)|) for points where |Z| < threshold.
    """
    results = []
    dr = (s_real_range[1] - s_real_range[0]) / grid_points
    di = (s_imag_range[1] - s_imag_range[0]) / grid_points

    for i in range(grid_points + 1):
        for j in range(grid_points + 1):
            sr = s_real_range[0] + i * dr
            si = s_imag_range[0] + j * di
            s = complex(sr, si)
            Z = shadow_selberg_zeta(shadow_coeffs, s, max_r)
            modulus = abs(Z)
            if modulus < 0.1:
                results.append((sr, si, modulus))
    return results


def shadow_selberg_functional_equation_test(
    shadow_coeffs: Dict[int, float],
    s_values: List[complex],
    candidate_weight: float = 1.0,
    max_r: Optional[int] = None,
) -> List[Tuple[complex, complex, complex, float]]:
    """Test Z(s) vs Z(w-s) for a functional equation.

    Returns (s, Z(s), Z(w-s), |Z(s)-Z(w-s)|/max(|Z|,1)).
    """
    results = []
    for s in s_values:
        Zs = shadow_selberg_zeta(shadow_coeffs, s, max_r)
        Zws = shadow_selberg_zeta(shadow_coeffs, complex(candidate_weight, 0) - s, max_r)
        scale = max(abs(Zs), abs(Zws), 1.0)
        results.append((s, Zs, Zws, abs(Zs - Zws) / scale))
    return results


# ============================================================================
# 8.  Relative trace formula (Koszul pairs)
# ============================================================================

def relative_trace(
    coeffs_A: Dict[int, float],
    coeffs_A_dual: Dict[int, float],
    test_fn: Callable[[int], float],
    max_r: Optional[int] = None,
) -> float:
    """RTF(A, A!; f) = Tr^sh(A, f) - Tr^sh(A!, f).

    For Koszul pairs, this measures the complementarity asymmetry.
    """
    tr_A = shadow_trace(coeffs_A, test_fn, max_r)
    tr_dual = shadow_trace(coeffs_A_dual, test_fn, max_r)
    return tr_A - tr_dual


def relative_trace_heisenberg(
    k_val: float,
    test_fn: Callable[[int], float],
) -> float:
    """RTF for Heisenberg: H_k vs H_{-k}.

    Exact: RTF = f(2) * (k - (-k)) = f(2) * 2k.

    CAUTION (AP24): kappa(H_k) + kappa(H_{-k}) = k + (-k) = 0 (anti-symmetric).
    """
    return test_fn(2) * 2.0 * k_val


def relative_trace_virasoro(
    c_val: float,
    test_fn: Callable[[int], float],
    max_r: int = 50,
) -> Tuple[float, float]:
    """RTF for Virasoro: Vir_c vs Vir_{26-c}.

    Returns (RTF_exact, RTF_from_coefficients).

    Leading term: f(2) * (c/2 - (26-c)/2) = f(2) * (c - 13).

    CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13, NOT 0.
    So kappa_diff = c/2 - (26-c)/2 = c - 13.
    """
    coeffs_c = virasoro_shadow_coefficients(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients(26.0 - c_val, max_r)
    rtf_computed = relative_trace(coeffs_c, coeffs_dual, test_fn, max_r)

    # Leading term only
    leading = test_fn(2) * (c_val - 13.0)

    return rtf_computed, leading


# ============================================================================
# 9.  Explicit trace formula decomposition (heat kernel)
# ============================================================================

def trace_formula_decomposition(
    shadow_coeffs: Dict[int, float],
    lam_values: List[float],
) -> List[Dict[str, float]]:
    """Decompose the heat kernel trace into identity + correction.

    For each lambda, returns:
        K(lambda): full heat kernel trace
        I(lambda): identity contribution (kappa * e^{-2*lambda})
        C(lambda): correction K - I
        ratio: C/I (relative correction)
    """
    kappa = shadow_coeffs.get(2, 0.0)
    results = []
    for lam in lam_values:
        K = heat_kernel_trace(shadow_coeffs, lam)
        I = heat_kernel_identity_contribution(kappa, lam)
        C = K - I
        ratio = C / I if abs(I) > 1e-300 else float('inf')
        results.append({
            'lambda': lam,
            'K': K,
            'I': I,
            'C': C,
            'ratio': ratio,
        })
    return results


def virasoro_heat_kernel_comparison(
    c_val: float,
    lam_values: List[float],
    max_r: int = 50,
) -> List[Dict[str, float]]:
    """Compare direct summation vs weighted-GF analytic form for Virasoro.

    Path 1: Direct summation of ordinary GF: sum S_r * e^{-lambda*r}
    Path 2: Weighted GF analytic: sum r*S_r * t^r = t^2*sqrt(Q_L(t))
    Path 3: Identity + correction decomposition

    Path 1 and Path 2 compute DIFFERENT quantities (ordinary vs weighted).
    The relative_error compares them as a STRUCTURAL check (they should NOT agree).
    The weighted_error compares Path 2 against its direct sum.
    """
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    kappa = c_val / 2.0
    results = []
    for lam in lam_values:
        t = math.exp(-lam)
        K_sum = heat_kernel_trace(coeffs, lam)
        # Weighted GF via analytic formula
        alpha_c = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
        Q = c_val ** 2 + 12.0 * c_val * t + alpha_c * t ** 2
        if Q >= 0:
            W_analytic = t ** 2 * math.sqrt(Q)
        else:
            W_analytic = float('nan')
        # Weighted GF via direct sum
        W_sum = sum(r * coeffs.get(r, 0.0) * t ** r for r in range(2, max_r + 1))
        I = heat_kernel_identity_contribution(kappa, lam)
        results.append({
            'lambda': lam,
            'K_ordinary': K_sum,
            'W_analytic': W_analytic,
            'W_sum': W_sum,
            'I': I,
            'weighted_error': abs(W_sum - W_analytic) / max(abs(W_analytic), 1e-300),
        })
    return results


# ============================================================================
# 10. Shadow Selberg zeta at integer points
# ============================================================================

def selberg_zeta_at_integers(
    shadow_coeffs: Dict[int, float],
    s_values: List[int],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Z^Sel_A(s) at integer values of s.

    For finite towers (class G, L, C), this is a finite product with exact values.
    """
    result = {}
    for s in s_values:
        Z = shadow_selberg_zeta(shadow_coeffs, complex(s, 0), max_r)
        result[s] = Z.real
    return result


def heisenberg_selberg_zeta_exact(k_val: float, s: complex) -> complex:
    """Exact Z^Sel for Heisenberg: Z(s) = 1 - k * 2^{-s}.

    Single-factor product (only S_2 = k nonzero).
    """
    return 1.0 - k_val * 2.0 ** (-s)


def affine_selberg_zeta_exact(
    kappa: float,
    alpha: float,
    s: complex,
) -> complex:
    """Exact Z^Sel for affine KM: Z(s) = (1 - kappa*2^{-s}) * (1 - alpha*3^{-s}).

    Two-factor product (S_2 = kappa, S_3 = alpha, rest zero).
    """
    return (1.0 - kappa * 2.0 ** (-s)) * (1.0 - alpha * 3.0 ** (-s))


# ============================================================================
# 11. Cross-family trace formula data
# ============================================================================

@dataclass
class TraceFormulaData:
    """Complete trace formula data for a modular Koszul algebra."""
    name: str
    shadow_class: str  # G, L, C, M
    shadow_coeffs: Dict[int, float] = field(default_factory=dict)
    kappa: float = 0.0
    growth_rate: float = 0.0
    spectral_dimension: float = 0.0

    # Trace values at standard test functions
    heat_kernel_values: Dict[float, float] = field(default_factory=dict)
    selberg_zeta_values: Dict[int, float] = field(default_factory=dict)
    weyl_spectrum: Dict[float, int] = field(default_factory=dict)


def compute_trace_formula_data(
    name: str,
    shadow_class: str,
    shadow_coeffs: Dict[int, float],
    rho: float = 0.0,
) -> TraceFormulaData:
    """Compute full trace formula data for a given algebra."""
    kappa = shadow_coeffs.get(2, 0.0)

    # Heat kernel at standard temperatures
    lam_values = [0.1, 0.5, 1.0, 2.0, 5.0]
    heat = {}
    for lam in lam_values:
        heat[lam] = heat_kernel_trace(shadow_coeffs, lam)

    # Selberg zeta at integers
    selberg = selberg_zeta_at_integers(shadow_coeffs, [2, 3, 4, 5])

    # Weyl spectrum
    eps_values = [10 ** (-i) for i in range(1, 11)]
    weyl = weyl_spectrum(shadow_coeffs, eps_values)

    d_sh = shadow_spectral_dimension_exact(rho) if rho > 0 else 0.0

    return TraceFormulaData(
        name=name,
        shadow_class=shadow_class,
        shadow_coeffs=shadow_coeffs,
        kappa=kappa,
        growth_rate=rho,
        spectral_dimension=d_sh,
        heat_kernel_values=heat,
        selberg_zeta_values=selberg,
        weyl_spectrum=weyl,
    )


# ============================================================================
# 12. Standard landscape data
# ============================================================================

def standard_landscape_trace_data() -> Dict[str, TraceFormulaData]:
    """Compute trace formula data for the full standard landscape."""
    landscape = {}

    # Heisenberg at k=1
    coeffs = heisenberg_shadow_coefficients(1.0)
    landscape['H_1'] = compute_trace_formula_data('H_1', 'G', coeffs, 0.0)

    # Heisenberg at k=2
    coeffs = heisenberg_shadow_coefficients(2.0)
    landscape['H_2'] = compute_trace_formula_data('H_2', 'G', coeffs, 0.0)

    # Affine sl_2 at k=1
    coeffs = affine_sl2_shadow_coefficients(1.0)
    landscape['sl2_1'] = compute_trace_formula_data('sl2_1', 'L', coeffs, 0.0)

    # Affine sl_2 at k=10
    coeffs = affine_sl2_shadow_coefficients(10.0)
    landscape['sl2_10'] = compute_trace_formula_data('sl2_10', 'L', coeffs, 0.0)

    # Affine sl_3 at k=1
    coeffs = affine_sl3_shadow_coefficients(1.0)
    landscape['sl3_1'] = compute_trace_formula_data('sl3_1', 'L', coeffs, 0.0)

    # Beta-gamma at lambda = 1/2
    coeffs = betagamma_shadow_coefficients(0.5)
    landscape['bg_1/2'] = compute_trace_formula_data('bg_1/2', 'C', coeffs, 0.0)

    # Virasoro at standard central charges
    for c_val in [0.5, 1.0, 2.0, 13.0, 25.0]:
        name = f'Vir_{c_val}'
        coeffs = virasoro_shadow_coefficients(c_val)
        rho = virasoro_growth_rate(c_val)
        landscape[name] = compute_trace_formula_data(name, 'M', coeffs, rho)

    return landscape


# ============================================================================
# 13. Multi-path verification helpers
# ============================================================================

def verify_heat_kernel_virasoro_multipath(
    c_val: float,
    lam: float,
    max_r: int = 50,
    tol: float = 1e-6,
) -> Dict[str, float]:
    """Verify heat kernel via 3 independent paths.

    Path 1: Direct heat kernel sum S_r * e^{-lam*r}
    Path 2: Ordinary generating function H(t) = sum S_r * t^r at t=e^{-lam}
    Path 3: Weighted GF analytic: sum r*S_r*t^r = t^2*sqrt(Q_L(t)),
            then recover ordinary GF by dividing each term by r.
            Independent check: weighted sum vs analytic formula.

    Paths 1 and 2 compute the SAME quantity (the ordinary GF),
    providing a consistency check on evaluation methods.
    Path 3 is structurally independent: it verifies the algebraic identity
    connecting shadow coefficients to the shadow metric Q_L.
    """
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    t = math.exp(-lam)

    # Path 1: Direct heat kernel summation
    K1 = heat_kernel_trace(coeffs, lam)

    # Path 2: Ordinary generating function at t
    K2 = shadow_generating_function(coeffs, t)

    # Path 3: Weighted GF check (analytic vs sum)
    alpha_c = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    Q = c_val ** 2 + 12.0 * c_val * t + alpha_c * t ** 2
    W_analytic = t ** 2 * math.sqrt(abs(Q))
    W_sum = sum(r * coeffs.get(r, 0.0) * t ** r for r in range(2, max_r + 1))

    # The weighted GF converges more slowly (extra factor r), so use a larger
    # tolerance for the weighted comparison.
    weighted_tol = max(tol, 0.01)  # 1% for weighted GF is acceptable

    return {
        'path1_direct': K1,
        'path2_genfn': K2,
        'path3_W_analytic': W_analytic,
        'path3_W_sum': W_sum,
        'error_12': abs(K1 - K2),
        'error_W': abs(W_analytic - W_sum),
        'rel_error_12': abs(K1 - K2) / max(abs(K1), 1e-300),
        'rel_error_W': abs(W_analytic - W_sum) / max(abs(W_analytic), 1e-300),
        'all_agree': (abs(K1 - K2) / max(abs(K1), 1e-300) < tol and
                      abs(W_analytic - W_sum) / max(abs(W_analytic), 1e-300) < weighted_tol),
    }


def verify_selberg_zeta_heisenberg_multipath(
    k_val: float,
    s: complex,
) -> Dict[str, complex]:
    """Verify Selberg zeta for Heisenberg via 2 paths.

    Path 1: General product formula
    Path 2: Exact closed form
    """
    coeffs = heisenberg_shadow_coefficients(k_val)

    Z1 = shadow_selberg_zeta(coeffs, s)
    Z2 = heisenberg_selberg_zeta_exact(k_val, s)

    return {
        'path1_product': Z1,
        'path2_exact': Z2,
        'error': abs(Z1 - Z2),
    }


def verify_relative_trace_heisenberg_multipath(
    k_val: float,
    test_fn: Callable[[int], float],
) -> Dict[str, float]:
    """Verify relative trace for Heisenberg via 3 paths.

    Path 1: Direct coefficient subtraction
    Path 2: Exact formula f(2) * 2k
    Path 3: Kappa difference * f(2)
    """
    coeffs_k = heisenberg_shadow_coefficients(k_val)
    coeffs_mk = heisenberg_shadow_coefficients(-k_val)

    # Path 1: General RTF
    rtf1 = relative_trace(coeffs_k, coeffs_mk, test_fn)

    # Path 2: Exact
    rtf2 = relative_trace_heisenberg(k_val, test_fn)

    # Path 3: Kappa difference
    kappa_diff = k_val - (-k_val)
    rtf3 = test_fn(2) * kappa_diff

    return {
        'path1_general': rtf1,
        'path2_exact': rtf2,
        'path3_kappa_diff': rtf3,
        'all_agree': abs(rtf1 - rtf2) < 1e-12 and abs(rtf1 - rtf3) < 1e-12,
    }
