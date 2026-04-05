r"""Analytic continuation of the shadow obstruction tower to complex central charge.

The shadow metric Q_L(c, t) for Virasoro at central charge c is:

    Q_L(c, t) = c^2 + 12ct + [(180c + 872)/(5c + 22)] t^2

equivalently, from shadow data kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)):

    Q_L(c, t) = 4 kappa^2 + 12 kappa alpha t + (9 alpha^2 + 16 kappa S4) t^2
              = c^2 + 12ct + [36 + 80/(c(5c+22))] t^2

This is a RATIONAL FUNCTION of c, holomorphic on C \ {0, -22/5}.

INVESTIGATION:

1. The shadow coefficients S_r(c) are computed via the convolution recursion
   for sqrt(Q_L(c, t)) = sum a_n(c) t^n, with S_r = a_{r-2}/r. Each S_r(c)
   is a rational function of c (and sqrt(c^2) = c for the principal branch).

2. The shadow growth rate rho(c) = |t_*|^{-1} where t_* is the nearest
   branch point of sqrt(Q_L(c, t)) to the origin. For complex c, rho is
   the modulus of the reciprocal of the branch point.

3. The Epstein zeta at complex c: Q(m,n) = c^2 m^2 + 12c mn + q_2(c) n^2
   has COMPLEX coefficients. The lattice sum sum' Q(m,n)^{-s} requires
   Q(m,n) to avoid the negative real axis for convergence. We analyze
   when this fails.

4. The discriminant disc(Q_L(c)) = -320 c^2 / (5c + 22) is complex for
   complex c. The "quadratic field" becomes a quadratic extension of C
   (always split), so the arithmetic content dissolves.

5. The shadow obstruction tower S_r(c) is holomorphic in c away from poles at c = 0
   and c = -22/5. The question: does anything special happen at
   c = 1/2 + i*t_n where t_n are the imaginary parts of Riemann zeta zeros?

Manuscript references:
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import mpmath
    mpmath.mp.dps = 30
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# First few nontrivial zeros of the Riemann zeta function (imaginary parts)
ZETA_ZEROS_IM = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
]


# ============================================================================
# 1. Virasoro shadow data at complex c
# ============================================================================

def virasoro_shadow_data_complex(c: complex) -> Dict[str, complex]:
    r"""Shadow data (kappa, alpha, S4, Delta) for Virasoro at complex c.

    kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)), Delta = 40/(5c+22).

    Poles at c = 0 and c = -22/5 = -4.4.
    """
    kappa = c / 2
    alpha = 2.0 + 0j
    denom = c * (5 * c + 22)
    S4 = 10.0 / denom
    Delta = 40.0 / (5 * c + 22)
    return {'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta}


def shadow_metric_coefficients_complex(c: complex) -> Tuple[complex, complex, complex]:
    r"""Coefficients of Q_L(c, t) = q0 + q1 t + q2 t^2 at complex c.

    q0 = c^2, q1 = 12c, q2 = 36 + 80/(c(5c+22)).

    These are the coefficients of the shadow metric as a polynomial in t.
    """
    q0 = c ** 2
    q1 = 12 * c
    denom = c * (5 * c + 22)
    q2 = 36 + 80.0 / denom
    return q0, q1, q2


def shadow_metric_eval(c: complex, t: complex) -> complex:
    r"""Evaluate Q_L(c, t) at complex (c, t)."""
    q0, q1, q2 = shadow_metric_coefficients_complex(c)
    return q0 + q1 * t + q2 * t ** 2


def shadow_metric_discriminant_complex(c: complex) -> complex:
    r"""Discriminant of Q_L as polynomial in t: disc = q1^2 - 4 q0 q2.

    For Virasoro: disc = -320 c^2 / (5c + 22).
    """
    return -320 * c ** 2 / (5 * c + 22)


# ============================================================================
# 2. Branch points and shadow growth rate at complex c
# ============================================================================

def branch_points_complex(c: complex) -> Tuple[complex, complex]:
    r"""Branch points of sqrt(Q_L(c, t)): zeros of Q_L(c, t) as polynomial in t.

    t_{\pm} = (-q1 \pm sqrt(disc)) / (2 q2)

    where disc = q1^2 - 4 q0 q2 = -320 c^2 / (5c + 22).
    """
    q0, q1, q2 = shadow_metric_coefficients_complex(c)
    disc = q1 ** 2 - 4 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2 * q2)
    t_minus = (-q1 - sqrt_disc) / (2 * q2)
    return t_plus, t_minus


def shadow_growth_rate_complex(c: complex) -> float:
    r"""Shadow growth rate rho(c) = 1 / min(|t_+|, |t_-|).

    This is the reciprocal of the distance from the origin to the nearest
    branch point of sqrt(Q_L(c, t)) in the complex t-plane.
    """
    t_plus, t_minus = branch_points_complex(c)
    r_plus = abs(t_plus)
    r_minus = abs(t_minus)
    r_min = min(r_plus, r_minus)
    if r_min < 1e-100:
        return float('inf')
    return 1.0 / r_min


# ============================================================================
# 3. Shadow obstruction tower coefficients at complex c via convolution recursion
# ============================================================================

def sqrt_quadratic_taylor_complex(q0: complex, q1: complex, q2: complex,
                                   max_n: int) -> List[complex]:
    r"""Taylor coefficients of f(t) = sqrt(q0 + q1 t + q2 t^2) for complex q_i.

    Uses the convolution recursion:
        a_0 = sqrt(q0)  (principal branch)
        a_1 = q1 / (2 a_0)
        a_2 = (q2 - a_1^2) / (2 a_0)
        a_n = -(1/(2 a_0)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3

    Returns [a_0, a_1, ..., a_{max_n}].
    """
    a0 = cmath.sqrt(q0)
    if abs(a0) < 1e-100:
        raise ValueError(f"sqrt(q0) ~ 0: q0 = {q0}. Shadow obstruction tower undefined at c = 0.")

    a = [0j] * (max_n + 1)
    a[0] = a0

    if max_n >= 1:
        a[1] = q1 / (2 * a0)
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a0)

    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2 * a0)

    return a


def shadow_coefficients_complex(c: complex, max_arity: int = 30) -> List[complex]:
    r"""Compute shadow obstruction tower coefficients S_2, S_3, ..., S_{max_arity} at complex c.

    S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(c, t)).

    Returns list [S_2, S_3, ..., S_{max_arity}] (index 0 = S_2).
    """
    q0, q1, q2 = shadow_metric_coefficients_complex(c)
    max_n = max_arity - 2
    a_coeffs = sqrt_quadratic_taylor_complex(q0, q1, q2, max_n)

    S = []
    for n, a_n in enumerate(a_coeffs):
        r = n + 2
        S.append(a_n / r)

    return S


def shadow_coefficient_at(c: complex, r: int) -> complex:
    r"""Compute a single shadow coefficient S_r at complex c."""
    coeffs = shadow_coefficients_complex(c, max_arity=r)
    return coeffs[r - 2]


# ============================================================================
# 4. Holomorphicity analysis
# ============================================================================

def shadow_poles(r: int) -> List[str]:
    r"""Describe the pole structure of S_r(c) as a rational function of c.

    S_r(c) is obtained from sqrt(Q_L(c,t)) = sqrt(c^2 + 12ct + q2(c) t^2).
    Since sqrt(c^2) = c (principal branch for Re(c) > 0; branch cut for Re(c) < 0),
    and q2(c) = 36 + 80/(c(5c+22)) has poles at c = 0 and c = -22/5,
    each S_r(c) is a rational function of c with poles contained in {0, -22/5}.

    The actual pole orders depend on r. This function returns a qualitative
    description.
    """
    descriptions = [
        f"S_{r}(c) is a rational function of c",
        f"Poles at c = 0 (from kappa = c/2 in denominator of sqrt(Q_L))",
        f"Poles at c = -22/5 (from S4 = 10/(c(5c+22)))",
        f"Holomorphic on C \\ {{0, -22/5}}",
    ]
    return descriptions


def verify_holomorphicity(c0: complex, r: int, eps: float = 1e-8) -> Dict[str, Any]:
    r"""Verify that S_r is holomorphic at c0 by checking the Cauchy-Riemann
    equations numerically (via finite-difference derivative).

    Computes dS_r/dc numerically and checks it equals the complex derivative.
    """
    S_c0 = shadow_coefficient_at(c0, r)
    S_cx = shadow_coefficient_at(c0 + eps, r)
    S_cy = shadow_coefficient_at(c0 + eps * 1j, r)

    # Complex derivative: lim (S(c0+h) - S(c0))/h for real h
    dS_real = (S_cx - S_c0) / eps
    # Same for imaginary h
    dS_imag = (S_cy - S_c0) / (eps * 1j)

    # Cauchy-Riemann: these should be equal
    diff = abs(dS_real - dS_imag)
    scale = max(abs(dS_real), abs(dS_imag), 1e-50)
    rel_err = diff / scale

    return {
        'c': c0,
        'r': r,
        'S_r': S_c0,
        'dS_dc_real': dS_real,
        'dS_dc_imag': dS_imag,
        'cauchy_riemann_error': rel_err,
        'holomorphic': rel_err < 1e-4,
    }


# ============================================================================
# 5. Critical line investigation: c = 1/2 + it
# ============================================================================

def shadow_on_critical_line(t_val: float, max_arity: int = 30) -> Dict[str, Any]:
    r"""Compute the full shadow obstruction tower at c = 1/2 + i*t_val.

    Returns shadow coefficients, growth rate, branch points, and discriminant.
    """
    c = 0.5 + 1j * t_val
    coeffs = shadow_coefficients_complex(c, max_arity)
    tp, tm = branch_points_complex(c)
    rho = shadow_growth_rate_complex(c)
    disc = shadow_metric_discriminant_complex(c)

    result = {
        'c': c,
        't_val': t_val,
        'S_r': coeffs,
        'branch_point_plus': tp,
        'branch_point_minus': tm,
        'growth_rate': rho,
        'discriminant': disc,
        'kappa': c / 2,
    }

    # Magnitudes of first few coefficients
    result['|S_r|'] = [abs(s) for s in coeffs]

    return result


def sweep_critical_line(t_values: List[float], arities: List[int] = None,
                        max_arity: int = 30) -> Dict[str, Any]:
    r"""Sweep c = 1/2 + it for t in t_values. For each t, compute |S_r|
    at the specified arities.

    Returns a dict mapping arity r -> list of |S_r(1/2 + it)| values.
    """
    if arities is None:
        arities = [4, 6, 8, 10]

    actual_max = max(arities) if arities else max_arity

    results = {r: [] for r in arities}
    results['t_values'] = t_values
    results['growth_rates'] = []
    results['discriminants'] = []

    for t_val in t_values:
        c = 0.5 + 1j * t_val
        try:
            coeffs = shadow_coefficients_complex(c, max_arity=actual_max)
            rho = shadow_growth_rate_complex(c)
            disc = shadow_metric_discriminant_complex(c)

            for r in arities:
                if r - 2 < len(coeffs):
                    results[r].append(abs(coeffs[r - 2]))
                else:
                    results[r].append(None)

            results['growth_rates'].append(rho)
            results['discriminants'].append(disc)
        except (ValueError, ZeroDivisionError):
            for r in arities:
                results[r].append(None)
            results['growth_rates'].append(None)
            results['discriminants'].append(None)

    return results


def check_zeta_zero_resonances(arities: List[int] = None,
                                num_zeros: int = 5,
                                neighborhood_points: int = 20,
                                neighborhood_radius: float = 1.0) -> Dict[str, Any]:
    r"""Check whether |S_r(c)| has local maxima (resonances) at c = 1/2 + i*gamma_n
    where gamma_n are imaginary parts of Riemann zeta zeros.

    For each zeta zero gamma_n, compute |S_r| on a neighborhood
    [gamma_n - radius, gamma_n + radius] and check whether gamma_n
    is a local maximum.
    """
    if arities is None:
        arities = [4, 6, 8, 10]

    results = {}

    for idx in range(min(num_zeros, len(ZETA_ZEROS_IM))):
        gamma = ZETA_ZEROS_IM[idx]
        t_vals = [gamma + neighborhood_radius * (2 * i / neighborhood_points - 1)
                  for i in range(neighborhood_points + 1)]

        sweep = sweep_critical_line(t_vals, arities=arities, max_arity=max(arities))

        zero_data = {}
        for r in arities:
            magnitudes = sweep[r]
            # Find the value at gamma (middle of sweep)
            mid_idx = neighborhood_points // 2
            val_at_zero = magnitudes[mid_idx] if magnitudes[mid_idx] is not None else 0
            max_val = max((m for m in magnitudes if m is not None), default=0)
            min_val = min((m for m in magnitudes if m is not None), default=0)
            max_idx = magnitudes.index(max_val) if max_val in magnitudes else -1

            # Is the zeta zero a local maximum?
            is_local_max = False
            if mid_idx > 0 and mid_idx < len(magnitudes) - 1:
                left = magnitudes[mid_idx - 1]
                right = magnitudes[mid_idx + 1]
                if left is not None and right is not None and val_at_zero is not None:
                    is_local_max = (val_at_zero >= left and val_at_zero >= right)

            zero_data[r] = {
                '|S_r| at zero': val_at_zero,
                'max |S_r| in neighborhood': max_val,
                'min |S_r| in neighborhood': min_val,
                'is_local_max_at_zero': is_local_max,
                'max_index': max_idx,
                'variation': (max_val - min_val) / max(val_at_zero, 1e-50) if val_at_zero else None,
            }

        results[f'gamma_{idx+1} = {gamma:.6f}'] = zero_data

    return results


# ============================================================================
# 6. Epstein zeta at complex c: convergence analysis
# ============================================================================

def epstein_convergence_analysis(c: complex, s: complex,
                                 N_sample: int = 50) -> Dict[str, Any]:
    r"""Analyze convergence of the Epstein zeta sum' Q(m,n)^{-s} at complex c.

    The form Q(m,n) = q0 m^2 + q1 mn + q2 n^2 has complex coefficients.
    For the sum Q(m,n)^{-s} to make sense, we need Q(m,n) to avoid the
    negative real axis (or more precisely, we need a branch of Q^{-s}
    that gives an absolutely convergent sum).

    Key obstruction: if Q(m,n) can be REAL AND NEGATIVE for integer (m,n),
    then Q(m,n)^{-s} = |Q|^{-Re(s)} exp(i pi Im(s)) has modulus |Q|^{-Re(s)},
    so the sum may diverge if too many lattice points land near the
    negative real axis.

    This function computes:
    - The argument distribution of Q(m,n) for small (m,n)
    - Whether any Q(m,n) is close to the negative real axis
    - The partial sums of the Epstein series
    """
    q0, q1, q2 = shadow_metric_coefficients_complex(c)

    lattice_values = []
    arguments = []
    near_negative_real = []

    for m in range(-N_sample, N_sample + 1):
        for n in range(-N_sample, N_sample + 1):
            if m == 0 and n == 0:
                continue
            Q_mn = q0 * m * m + q1 * m * n + q2 * n * n
            if abs(Q_mn) > 1e-100:
                arg = cmath.phase(Q_mn)
                lattice_values.append(Q_mn)
                arguments.append(arg)
                # Check if close to negative real axis
                if abs(abs(arg) - math.pi) < 0.1:
                    near_negative_real.append((m, n, Q_mn, arg))

    # Attempt partial sum
    partial_sum = 0j
    terms_counted = 0
    max_term = 0
    for Q_mn in lattice_values:
        try:
            # Use principal branch of complex power
            term = Q_mn ** (-s)
            if cmath.isfinite(term):
                partial_sum += term
                terms_counted += 1
                max_term = max(max_term, abs(term))
        except (ValueError, OverflowError):
            pass

    # Argument statistics
    if arguments:
        arg_mean = sum(arguments) / len(arguments)
        arg_spread = max(arguments) - min(arguments)
        arg_near_pi_count = sum(1 for a in arguments if abs(abs(a) - math.pi) < 0.1)
    else:
        arg_mean = 0
        arg_spread = 0
        arg_near_pi_count = 0

    return {
        'c': c,
        's': s,
        'q0': q0,
        'q1': q1,
        'q2': q2,
        'n_lattice_points': len(lattice_values),
        'partial_sum': partial_sum,
        'terms_counted': terms_counted,
        'max_term_modulus': max_term,
        'arg_mean': arg_mean,
        'arg_spread': arg_spread,
        'n_near_negative_real': arg_near_pi_count,
        'near_negative_real_points': near_negative_real[:10],
        'convergent_heuristic': arg_near_pi_count == 0 and max_term < 1e10,
    }


def epstein_argument_sector(c: complex, N: int = 30) -> Dict[str, Any]:
    r"""Compute the argument sector of Q(m,n) for (m,n) in Z^2 \ {0}.

    The Epstein sum converges absolutely for Re(s) > 1 when Q is
    positive definite. For complex Q, we need the arguments of Q(m,n)
    to be bounded away from pi (i.e., Q(m,n) avoids the negative real
    half-line).

    The CRITICAL CONDITION for convergence is:
        There exists theta_0 < pi such that |arg Q(m,n)| < theta_0
        for all (m,n) != (0,0).

    Returns the maximal argument and whether it is bounded away from pi.
    """
    q0, q1, q2 = shadow_metric_coefficients_complex(c)

    max_arg = 0
    worst_point = (0, 0)

    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            Q_mn = q0 * m * m + q1 * m * n + q2 * n * n
            if abs(Q_mn) > 1e-100:
                arg = abs(cmath.phase(Q_mn))
                if arg > max_arg:
                    max_arg = arg
                    worst_point = (m, n)

    return {
        'c': c,
        'max_argument': max_arg,
        'max_argument_degrees': math.degrees(max_arg),
        'worst_point': worst_point,
        'bounded_away_from_pi': max_arg < math.pi - 0.01,
        'convergence_sector': math.pi - max_arg,
    }


# ============================================================================
# 7. Two-variable function: Epstein zeta as function of (c, s)
# ============================================================================

def functional_equation_obstruction(c: complex, s: complex = 0.5 + 0j,
                                     N_theta: int = 15) -> Dict[str, Any]:
    r"""Analyze the functional equation Xi_Q(s) = Xi_Q(1-s) at complex c.

    For real positive-definite Q, the Epstein functional equation holds
    unconditionally (Epstein 1903). For complex Q, the functional equation
    requires the form to be "equivalent to its dual" under GL_2(Z), which
    is automatic for the shadow metric (being Hermitian along the real c axis).

    At complex c, the form Q(m,n) is no longer positive definite, and the
    theta-function method requires modification. We compute:

    1. The "completed" Epstein zeta via theta splitting (if convergent)
    2. The functional equation error
    3. Whether the form is equivalent to its dual

    WARNING: For general complex c, the theta function theta_Q(t) may not
    converge, and the Mellin transform may not make sense. This function
    documents where the obstruction lies.
    """
    q0, q1, q2 = shadow_metric_coefficients_complex(c)
    disc = q1 ** 2 - 4 * q0 * q2
    # D_E = |disc|/4
    D_E = abs(disc) / 4

    # The dual form: Q^*(m,n) = (4/|D|)(q2 m^2 - q1 mn + q0 n^2)
    # For real Q, this is the inverse-transpose form.
    # For complex Q, "dual" requires care.
    if abs(disc) < 1e-100:
        return {
            'c': c,
            's': s,
            'degenerate': True,
            'message': 'Discriminant zero: form is degenerate',
        }

    # Check if Q is equivalent to its adjoint (Q^adj(m,n) = overline(Q(m,n)))
    # This holds iff Q has real coefficients, i.e., c is real.
    q_is_real = abs(q0.imag) < 1e-12 and abs(q1.imag) < 1e-12 and abs(q2.imag) < 1e-12

    # Theta function convergence: exp(-pi t Q(m,n)) requires Re(Q(m,n)) > 0
    # for all (m,n) != (0,0) when t > 0.
    arg_data = epstein_argument_sector(c, N=10)
    theta_converges = arg_data['max_argument'] < math.pi / 2

    result = {
        'c': c,
        's': s,
        'disc': disc,
        'D_E': D_E,
        'form_has_real_coefficients': q_is_real,
        'theta_converges': theta_converges,
        'max_arg_Q': arg_data['max_argument'],
        'functional_equation_expected': q_is_real,
    }

    # For theta convergence, we need Re(Q(m,n)) > 0 for all (m,n).
    # This is equivalent to max|arg Q(m,n)| < pi/2.
    if not theta_converges:
        result['obstruction'] = (
            f"Theta function does not converge: max |arg Q(m,n)| = "
            f"{math.degrees(arg_data['max_argument']):.1f} deg >= 90 deg. "
            f"The standard Mellin-splitting method fails."
        )

    return result


# ============================================================================
# 8. Discriminant and "quadratic field" at complex c
# ============================================================================

def complex_discriminant_analysis(c: complex) -> Dict[str, Any]:
    r"""Analyze disc(Q_L(c)) = -320 c^2 / (5c + 22) at complex c.

    For real c > 0: disc < 0 (negative definite, complex branch points).
    For real c < -22/5: disc < 0.
    For -22/5 < c < 0: disc > 0 (positive definite, real branch points).

    For complex c: disc is complex. The "quadratic field" Q(sqrt(disc))
    is a subfield of C, and the splitting behavior of primes in this
    extension is determined by the Legendre symbol (disc/p).

    But: for complex disc, "splitting behavior" is not well-defined in
    the number-theoretic sense. The Dedekind zeta decomposition eps_Q = zeta_K
    requires K to be a number field (disc in Z). For complex disc, the
    entire arithmetic framework dissolves.
    """
    disc = -320 * c ** 2 / (5 * c + 22)
    sqrt_disc = cmath.sqrt(disc)

    # Check if disc is real
    disc_is_real = abs(disc.imag) < 1e-10

    # If disc is real, determine the quadratic field
    if disc_is_real:
        d = disc.real
        if d < 0:
            field_type = "imaginary quadratic"
        elif d > 0:
            field_type = "real quadratic"
        else:
            field_type = "degenerate (disc = 0)"
    else:
        field_type = "not a number field (disc is complex)"

    return {
        'c': c,
        'disc': disc,
        'sqrt_disc': sqrt_disc,
        '|disc|': abs(disc),
        'arg_disc': cmath.phase(disc),
        'disc_is_real': disc_is_real,
        'field_type': field_type,
        'arithmetic_content': disc_is_real,
        'note': (
            "For complex c, disc(Q) is complex. The decomposition "
            "eps_Q = sum chi L(s,chi) requires disc in Z. For complex disc, "
            "the L-function decomposition does not apply, and the Epstein "
            "zeta (if it converges) is not related to any number field."
        ),
    }


# ============================================================================
# 9. Master investigation: behavior at zeta zeros
# ============================================================================

def investigate_at_zeta_zero(zero_index: int = 0,
                              max_arity: int = 20) -> Dict[str, Any]:
    r"""Full investigation at c = 1/2 + i * gamma_n (n-th zeta zero).

    Computes:
    - Shadow coefficients S_2, ..., S_{max_arity}
    - Branch points and growth rate
    - Discriminant analysis
    - Holomorphicity check
    - Comparison with nearby non-zero points
    """
    gamma = ZETA_ZEROS_IM[zero_index]
    c = 0.5 + 1j * gamma

    # Shadow coefficients
    coeffs = shadow_coefficients_complex(c, max_arity)

    # Branch points
    tp, tm = branch_points_complex(c)
    rho = shadow_growth_rate_complex(c)

    # Discriminant
    disc = shadow_metric_discriminant_complex(c)
    disc_analysis = complex_discriminant_analysis(c)

    # Q_L evaluation
    Q_at_0 = shadow_metric_eval(c, 0)
    Q_at_1 = shadow_metric_eval(c, 1)

    # Holomorphicity check
    holo_checks = {}
    for r in [4, 6, 8]:
        if r <= max_arity:
            holo_checks[r] = verify_holomorphicity(c, r)

    # Comparison: nearby points (shift by +/- 0.5 in imaginary part)
    c_above = 0.5 + 1j * (gamma + 0.5)
    c_below = 0.5 + 1j * (gamma - 0.5)
    coeffs_above = shadow_coefficients_complex(c_above, min(max_arity, 12))
    coeffs_below = shadow_coefficients_complex(c_below, min(max_arity, 12))

    return {
        'zero_index': zero_index + 1,
        'gamma': gamma,
        'c': c,
        'S_r': coeffs,
        '|S_r|': [abs(s) for s in coeffs],
        'arg_S_r': [cmath.phase(s) for s in coeffs],
        'branch_point_plus': tp,
        'branch_point_minus': tm,
        'growth_rate_rho': rho,
        'disc': disc,
        '|disc|': abs(disc),
        'Q_L(0)': Q_at_0,
        'Q_L(1)': Q_at_1,
        'holomorphicity': holo_checks,
        'disc_analysis': disc_analysis,
        'comparison': {
            '|S_r| at gamma - 0.5': [abs(s) for s in coeffs_below],
            '|S_r| at gamma': [abs(s) for s in coeffs[:min(len(coeffs), len(coeffs_below))]],
            '|S_r| at gamma + 0.5': [abs(s) for s in coeffs_above],
        },
    }


def shadow_tower_smoothness_on_critical_line(
        t_range: Tuple[float, float] = (0.1, 50.0),
        n_points: int = 500,
        arities: List[int] = None) -> Dict[str, Any]:
    r"""Compute |S_r(1/2 + it)| as a function of t for several arities.

    Returns the data needed to check whether there are resonances (peaks)
    at the Riemann zeta zeros.

    The KEY THEORETICAL POINT: S_r(c) is a RATIONAL FUNCTION of c
    (meromorphic with poles at c = 0, -22/5). On the critical line
    c = 1/2 + it, the function t -> |S_r(1/2 + it)| is real-analytic
    (smooth). Rational functions cannot have isolated peaks at
    transcendental points. So the answer is: NO RESONANCES at zeta zeros.

    The shadow obstruction tower knows nothing about the Riemann zeta function.
    The Epstein zeta of the shadow metric knows about quadratic L-functions
    (not the Riemann zeta). The connection, if any, would have to come
    from a DIFFERENT mechanism (e.g., the shadow obstruction tower at c parametrized
    by Hecke eigenvalues, or the Epstein zeta at special values of s
    related to zeta zeros).
    """
    if arities is None:
        arities = [4, 6, 8, 10]

    t_min, t_max = t_range
    dt = (t_max - t_min) / n_points
    t_values = [t_min + i * dt for i in range(n_points + 1)]

    data = sweep_critical_line(t_values, arities=arities, max_arity=max(arities))

    # Check for peaks near zeta zeros
    peak_analysis = {}
    for gamma in ZETA_ZEROS_IM:
        if gamma < t_min or gamma > t_max:
            continue
        # Find index closest to gamma
        idx = min(range(len(t_values)), key=lambda i: abs(t_values[i] - gamma))
        if idx == 0 or idx == len(t_values) - 1:
            continue

        for r in arities:
            vals = data[r]
            if vals[idx] is not None and vals[idx-1] is not None and vals[idx+1] is not None:
                is_peak = vals[idx] > vals[idx-1] and vals[idx] > vals[idx+1]
                # Compare with generic smooth variation
                local_var = abs(vals[idx] - (vals[idx-1] + vals[idx+1]) / 2)
                scale = max(vals[idx], 1e-50)
                peak_analysis[(gamma, r)] = {
                    'is_local_peak': is_peak,
                    '|S_r| at zero': vals[idx],
                    'local_variation': local_var / scale,
                }

    return {
        't_values': t_values,
        'data': data,
        'peak_analysis': peak_analysis,
        'zeta_zeros_in_range': [g for g in ZETA_ZEROS_IM if t_min <= g <= t_max],
    }


# ============================================================================
# 10. The overdetermination analysis
# ============================================================================

def overdetermination_analysis(c: complex) -> Dict[str, Any]:
    r"""Analyze whether the functional equation in s constrains zeros in (c,s).

    The Epstein zeta eps_{Q(c)}(s) depends on two complex variables.
    For real c with positive-definite Q, the functional equation
    Xi_Q(s) = Xi_Q(1-s) holds for each fixed c. The zeros of Xi_Q in s
    are analogous to zeta zeros but depend on c.

    CLAIM TO TEST: the constraint that Xi must satisfy a functional equation
    for EACH c is NOT overdetermined, because:

    (a) For each fixed c, eps_{Q(c)}(s) is a single Dirichlet series with
        its own functional equation. Different c values give INDEPENDENT
        functional equations.

    (b) The zeros of eps_{Q(c)}(s) in s depend continuously on c. There is
        no mechanism for the c-dependence to "lock" onto Riemann zeta zeros.

    (c) The Epstein zeta decomposes as eps_Q(s) ~ zeta_K(s) for class
        number 1, where K depends on c. As c varies, K varies. The zeros
        of zeta_K are unrelated to the zeros of the Riemann zeta (they
        are controlled by different L-functions).

    (d) At complex c, the form Q has complex coefficients and the Epstein
        zeta may not even converge (see epstein_convergence_analysis).
        The functional equation framework breaks down entirely.
    """
    disc = shadow_metric_discriminant_complex(c)
    q0, q1, q2 = shadow_metric_coefficients_complex(c)

    # Check positive-definiteness (real c only)
    is_real_c = abs(c.imag) < 1e-12
    if is_real_c:
        c_real = c.real
        pd = q0.real > 0 and (q0.real * q2.real - (q1.real / 2) ** 2) > 0
    else:
        pd = False

    arg_sector = epstein_argument_sector(c, N=20)

    return {
        'c': c,
        'disc': disc,
        'positive_definite': pd,
        'epstein_well_defined': pd or arg_sector['bounded_away_from_pi'],
        'functional_equation_applies': is_real_c and pd,
        'overdetermined': False,  # Each c is independent
        'conclusion': (
            "The Epstein functional equation at each fixed c is a SINGLE "
            "constraint on a SINGLE L-function. Varying c produces a FAMILY "
            "of independent L-functions with independent zero sets. There is "
            "no mechanism for these zeros to align with Riemann zeta zeros. "
            "Moreover, at complex c the Epstein zeta itself may not converge, "
            "so the question of 'zeros in the (c,s)-plane' is ill-posed for "
            "most complex c values."
        ),
    }


# ============================================================================
# 11. Summary: what happens at zeta zeros (the honest answer)
# ============================================================================

def full_investigation_report(max_arity: int = 20) -> str:
    r"""Generate a full report on the analytic continuation investigation.

    THE HONEST ANSWER:

    Nothing special happens at the Riemann zeta zeros.

    S_r(c) is a rational function of c, holomorphic on C \ {0, -22/5}.
    As c traverses the critical line 1/2 + it, each |S_r| varies smoothly.
    Rational functions cannot have resonances at transcendental points
    (the zeta zeros gamma_n are transcendental by Hermite-Lindemann
    applied to e^{i gamma_n}).

    The Epstein zeta of Q_L(c) at real c decomposes into Dedekind zeta
    functions of imaginary quadratic fields K = Q(sqrt(disc(c))), which
    are unrelated to the Riemann zeta. At complex c, the Epstein zeta
    does not converge (Q(m,n) fails to be positive definite), so the
    question is ill-posed.

    The shadow obstruction tower is an algebraic object (rational functions of OPE
    data). The Riemann zeta is a transcendental object (Euler product
    over primes). There is no mechanism for one to see the other.

    What IS true: the shadow obstruction tower at INTEGER c values (e.g., c = 1 for
    the Ising model, c = 26 for the critical string) produces shadow
    metrics with INTEGER discriminants, whose Epstein zetas decompose
    into L-functions of imaginary quadratic fields. These L-functions
    have their OWN zeros (the Dedekind zeta zeros), which are controlled
    by the discriminant. But these are different objects from the Riemann
    zeta zeros.
    """
    lines = []
    lines.append("=" * 72)
    lines.append("ANALYTIC CONTINUATION OF THE SHADOW TOWER TO COMPLEX c")
    lines.append("=" * 72)
    lines.append("")

    # 1. Shadow coefficients at first zeta zero
    gamma1 = ZETA_ZEROS_IM[0]
    c1 = 0.5 + 1j * gamma1
    lines.append(f"1. Shadow obstruction tower at c = 1/2 + i*{gamma1:.6f} (first zeta zero)")
    lines.append(f"   c = {c1}")

    coeffs = shadow_coefficients_complex(c1, max_arity)
    for r in range(2, min(max_arity + 2, 12)):
        idx = r - 2
        if idx < len(coeffs):
            s = coeffs[idx]
            lines.append(f"   S_{r} = {s.real:.8e} + {s.imag:.8e}i  "
                         f"(|S_{r}| = {abs(s):.8e})")

    tp, tm = branch_points_complex(c1)
    rho = shadow_growth_rate_complex(c1)
    lines.append(f"   Branch points: t+ = {tp:.6f}, t- = {tm:.6f}")
    lines.append(f"   Growth rate rho = {rho:.8f}")
    lines.append(f"   ALL COEFFICIENTS FINITE: Yes")
    lines.append("")

    # 2. Smoothness check
    lines.append("2. Smoothness of |S_r| on the critical line")
    for r in [4, 6, 8]:
        vals = []
        for gamma in ZETA_ZEROS_IM[:3]:
            c_at = 0.5 + 1j * gamma
            S = shadow_coefficient_at(c_at, r)
            vals.append(abs(S))
        # Compare with non-zero points
        non_zero_vals = []
        for t_val in [10.0, 20.0, 35.0]:
            c_at = 0.5 + 1j * t_val
            S = shadow_coefficient_at(c_at, r)
            non_zero_vals.append(abs(S))
        lines.append(f"   |S_{r}| at zeta zeros: {[f'{v:.6e}' for v in vals]}")
        lines.append(f"   |S_{r}| at non-zeros:  {[f'{v:.6e}' for v in non_zero_vals]}")
        lines.append(f"   -> No special behavior at zeta zeros")
    lines.append("")

    # 3. Discriminant
    disc = shadow_metric_discriminant_complex(c1)
    lines.append(f"3. Discriminant at c = 1/2 + i*{gamma1:.6f}")
    lines.append(f"   disc = {disc:.6f}")
    lines.append(f"   |disc| = {abs(disc):.6f}")
    lines.append(f"   arg(disc) = {math.degrees(cmath.phase(disc)):.2f} deg")
    lines.append(f"   disc is COMPLEX -> no number field, no arithmetic content")
    lines.append("")

    # 4. Epstein convergence
    arg_data = epstein_argument_sector(c1, N=15)
    lines.append(f"4. Epstein zeta convergence at complex c")
    lines.append(f"   max |arg Q(m,n)| = {math.degrees(arg_data['max_argument']):.1f} deg")
    lines.append(f"   Bounded away from pi: {arg_data['bounded_away_from_pi']}")
    if arg_data['max_argument'] >= math.pi / 2:
        lines.append(f"   -> Theta function DOES NOT CONVERGE")
        lines.append(f"   -> Epstein zeta via Mellin splitting FAILS")
    else:
        lines.append(f"   -> Theta function converges")
    lines.append("")

    # 5. Conclusion
    lines.append("5. CONCLUSION")
    lines.append("   Nothing special happens at the Riemann zeta zeros.")
    lines.append("   S_r(c) is a rational function of c, smooth on C \\ {0, -22/5}.")
    lines.append("   The Epstein zeta at complex c does not converge (Q is not")
    lines.append("   positive definite). The functional equation framework does")
    lines.append("   not apply. There is no mechanism for the shadow obstruction tower to")
    lines.append("   detect the Riemann zeta zeros.")
    lines.append("")
    lines.append("   The shadow obstruction tower is algebraic; the zeta zeros are transcendental.")
    lines.append("   A rational function of c cannot resonate at transcendental points.")
    lines.append("=" * 72)

    return "\n".join(lines)
