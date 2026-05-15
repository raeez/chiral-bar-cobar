r"""Scalar shadow genus convergence and Borel diagnostics.

Audit surface for the label ``thm:shadow-borel-summability``.

    This module certifies only the scalar Virasoro/Faber-Pandharipande
    coefficient sector where F_g = kappa * lambda_g^FP.  The ordinary scalar
    genus series F(x) = sum_{g >= 1} F_g x^{2g} converges for |x| < 2*pi.
    That scalar fact is not a proof of analytic continuation, a
    nonperturbative completion, BTZ/JT recovery, or any all-genus
    multi-weight partition theorem.

    Precisely:

    (i) CONVERGENCE REGION (c > c* ~ 6.125):
        The shadow obstruction tower series sum S_r t^r CONVERGES absolutely
        for |t| < 1/rho(c) > 1. The generating function H(t) = t^2 sqrt(Q_L(t))
        is algebraic of degree 2.

    (ii) DIVERGENCE REGION (c < c*):
        The series diverges geometrically with growth rate rho(c) > 1.
        The growth is GEVREY-0 (sub-factorial): |S_r| / r! -> 0.
        This is strictly milder than the Gevrey-1 (factorial) divergence
        of the string genus expansion.

    (iii) ORDINARY GENUS GENERATING FUNCTION:
        The ordinary generating function
            G[F](xi) = sum_{g >= 1} F_g xi^{2g}
        has the closed form:
            G[F](xi) = kappa * (xi / (2 sin(xi/2)) - 1).
        It is meromorphic with simple poles at xi = 2*pi*n,
        n in Z \ {0}.  These are poles of G[F], not singularities of
        the true Borel transform.

    (iv) TRUE BOREL TRANSFORMS:
        In the variable t = x^2,
            B_t[F](s) = sum_{g >= 1} F_g s^g/g!
        is entire.  The even transform
            B_even[F](xi) = sum_{g >= 1} F_g xi^{2g}/(2g)!
        is also entire.  There are no Borel-plane poles at xi = 2*pi*n.

    (v) CONDITIONAL LAPLACE RECONSTRUCTION:
        The standard Borel-Laplace integral in t reconstructs the convergent
        analytic sum in its disk of convergence.  Since B_t[F] is entire in
        this scalar sector, the paired lateral integrals have zero mathematical
        jump in any common convergence sector.  This is conditional on the
        exact scalar coefficient formula and does not certify the full shadow
        obstruction tower.

PROOF STRATEGY:
    (a) The closed form G[F](xi) = kappa * (xi/(2 sin(xi/2)) - 1) is verified
        by checking that its Taylor expansion matches F_g = kappa * lambda_g^FP
        term by term using the identity lambda_g^FP = (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!).
    (b) The meromorphic structure of G[F] gives ordinary pole residues
        Res_{xi=2*pi*n} G[F](xi) = (-1)^n * 2*pi*n * kappa.
    (c) Dividing the already geometric coefficients by g! or (2g)! makes the
        corresponding Borel transforms entire.
    (d) The coefficient ratio F_{g-1}/F_g tends to (2*pi)^2.

MULTI-WEIGHT EXTENSION (W_3, W_N):
    Not implemented here.  This engine proves the scalar sector and exposes
    the exact proof obligation for cross-channel corrections: their own
    coefficient growth must be computed before any Borel or pole statement is
    asserted.

COMPARISON WITH STRING GENUS EXPANSION:
    String:  F_g^{string} ~ (2g)! * A^{-2g}  (Gevrey-1, factorial divergence)
    Shadow:  S_r ~ rho^r * r^{-5/2}           (Gevrey-0, geometric divergence)

    This engine verifies the growth-class separation.  It does not compute
    the Borel singularity set of the full string genus expansion, and it does
    not infer string/nonperturbative Borel summability from scalar shadow data.

References:
    thm:shadow-growth-rate (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    prop:universal-instanton-action (higher_genus_modular_koszul.tex)
    rem:shadow-borel-summability (higher_genus_modular_koszul.tex)
    theorem_shadow_s11_s15_engine.py (growth rate data)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# 0. Scope and certification firewalls
# ============================================================================

def object_and_kernel_firewalls() -> Dict[str, Any]:
    r"""Canonical object and kernel separations used by this diagnostic engine.

    Sources:
        CLAUDE.md "Essential constants" and "Five objects, never conflate";
        chapters/examples/landscape_census.tex, standard-family constants.
    """
    return {
        'objects_distinct': {
            'A': 'chiral algebra',
            'B(A)': 'bar coalgebra T^c(s^{-1} Abar)',
            'A^i': 'bar cohomology / dual coalgebra branch',
            'A^!': 'Verdier or continuous-linear dual algebra branch',
            'Z_ch^der(A)': 'derived chiral centre / Hochschild bulk branch',
        },
        'bar_cobar_inversion': 'Omega(B(A)) = A',
        'bar_cobar_inversion_is_koszul_duality': False,
        'koszul_dual_branch': 'A^! is Verdier/continuous-linear dual, not Omega(B(A))',
        'bulk_branch': 'Z_ch^der(A) is Hochschild bulk, not Koszul duality',
        'kernel_constants': {
            'affine_collision_trace_form': 'r^{KM}(z) = k*Omega_tr/z',
            'affine_kz_normalization': 'r_KZ(z) = Omega/((k+h^vee)z)',
            'heisenberg_collision': 'r^{Heis}(z) = k/z',
            'virasoro_collision': 'r^{Vir}(z) = (c/2)/z^3 + 2T/z',
        },
        'holographic_package_entries': (
            'A', 'A^i', 'A^!', 'C', 'r(z)', 'Theta_A', 'nabla^hol',
        ),
        'modular_koszul_compute_package_projections': (
            'Fact_X(L)', 'barB_X(L)', 'Theta_L', 'L_L',
            '(V_br,T_br)', 'R4_mod(L)',
        ),
        'scalar_projection_is_full_maurer_cartan_data': False,
    }


def analytic_certification_firewall() -> Dict[str, Any]:
    r"""Status split for scalar coefficients, diagnostics, and analytic claims."""
    return {
        'scalar_coefficient_series': {
            'status': 'certified_exact',
            'formula': 'F_g = kappa * lambda_g^FP',
            'scope': 'uniform-weight scalar lane; Virasoro has no cross-channel term',
        },
        'ordinary_scalar_singularities': {
            'status': 'certified_exact',
            'formula': 'G[F](xi) = kappa*(xi/(2*sin(xi/2)) - 1)',
            'singularities': 'simple poles at xi = 2*pi*n, n != 0',
            'are_true_borel_singularities': False,
        },
        'true_borel_transforms': {
            'status': 'certified_for_scalar_coefficients',
            't_transform': 'B_t[F](s) = sum F_g s^g/g! is entire',
            'even_transform': 'B_even[F](xi) = sum F_g xi^(2g)/(2g)! is entire',
            'singularity_set': (),
        },
        'ordinary_t_plane_singularities': {
            'status': 'certified_exact_for_reconstructed_scalar_sum',
            'formula': 't = (2*pi*n)^2 for n != 0',
            'nearest_positive': '(2*pi)^2',
            'are_true_borel_singularities': False,
        },
        'shadow_radius_diagnostic': {
            'status': 'asymptotic_diagnostic',
            'formula': 'rho(c) = sqrt((180c+872)/((5c+22)c^2))',
            'certifies_borel_summability': False,
            'certifies_analytic_continuation': False,
        },
        'pade_darboux_diagnostics': {
            'status': 'diagnostic_only',
            'certifies_ecalle_stokes_data': False,
            'certifies_alien_calculus': False,
        },
        'scalar_projection': {
            'status': 'projection_only',
            'certifies_full_maurer_cartan_data': False,
            'certifies_full_shadow_tower': False,
        },
        'finite_windows': {
            'status': 'diagnostic_only',
            'certifies_borel_summability': False,
            'certifies_nonperturbative_completion': False,
        },
        'conditional_laplace_reconstruction': {
            'status': 'conditional_scalar_statement',
            'requires': 'exact scalar coefficient formula and a convergent Laplace sector',
            'certifies_full_shadow_tower': False,
        },
        'multiweight_extension': {
            'status': 'not_certified_here',
            'missing_input': 'growth and singularity analysis of delta F_g^cross',
        },
        'nonperturbative_completion': {'status': 'not_certified_here'},
        'btz_jt_recovery': {'status': 'not_certified_here'},
        'ecalle_stokes_alien_calculus': {'status': 'not_certified_here'},
        'all_genus_virasoro_or_multiweight_partition_theorem': {
            'status': 'not_certified_here',
        },
        'object_firewalls': object_and_kernel_firewalls(),
    }


# ============================================================================
# 1. Exact arithmetic primitives
# ============================================================================

@lru_cache(maxsize=256)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n via recursion (memoized)."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n >= 3:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        s += Fraction(math.comb(n + 1, k)) * _bernoulli_exact(k)
    return -s / (n + 1)


def _lambda_fp_exact(g: int) -> Fraction:
    r"""Faber-Pandharipande: lambda_g^FP = (2^{2g-1}-1)|B_{2g}| / (2^{2g-1}(2g)!).

    g=1: 1/24.  g=2: 7/5760.  g=3: 31/967680.
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    B2g = _bernoulli_exact(2 * g)
    abs_B2g = abs(B2g)
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs_B2g / Fraction(math.factorial(2 * g))


# ============================================================================
# 1. Shadow metric and branch points (from S11-S15 engine)
# ============================================================================

def virasoro_shadow_metric_coeffs(c_val: float) -> Tuple[float, float, float]:
    """Q_L(t) = q0 + q1*t + q2*t^2 where q0=c^2, q1=12c, q2=(180c+872)/(5c+22)."""
    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    return q0, q1, q2


def virasoro_shadow_metric_coeffs_exact(c_frac: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Exact Virasoro metric coefficients in the trace-form convention."""
    q0 = c_frac ** 2
    q1 = 12 * c_frac
    q2 = Fraction(180 * c_frac + 872, 5 * c_frac + 22)
    return q0, q1, q2


def shadow_metric_branch_points(c_val: float) -> Tuple[complex, complex]:
    """Zeros of Q_L(t) = q0 + q1*t + q2*t^2. Always a conjugate pair for c > 0."""
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    disc = q1 ** 2 - 4.0 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)
    return t_plus, t_minus


def growth_rate(c_val: float) -> float:
    """Growth rate rho(c) = 1/|t_*| where t_* is the nearest branch point."""
    t_plus, t_minus = shadow_metric_branch_points(c_val)
    return 1.0 / min(abs(t_plus), abs(t_minus))


def growth_rate_squared_exact(c_frac: Fraction) -> Fraction:
    r"""Exact Virasoro growth-rate square rho(c)^2 = q2/q0."""
    q0, _, q2 = virasoro_shadow_metric_coeffs_exact(c_frac)
    return q2 / q0


def convergence_radius_shadow(c_val: float) -> float:
    """Convergence radius R = |t_*| of the shadow Taylor series sum S_r t^r."""
    t_plus, t_minus = shadow_metric_branch_points(c_val)
    return min(abs(t_plus), abs(t_minus))


def critical_central_charge() -> float:
    """c* ~ 6.12537: unique positive root of 5c^3 + 22c^2 - 180c - 872 = 0.

    At c = c*: rho = 1 (marginal convergence).
    For c > c*: rho < 1 (convergence).
    For c < c*: rho > 1 (divergence).
    """
    # Newton's method on p(c) = 5c^3 + 22c^2 - 180c - 872
    x = 6.0
    for _ in range(50):
        p = 5.0 * x ** 3 + 22.0 * x ** 2 - 180.0 * x - 872.0
        dp = 15.0 * x ** 2 + 44.0 * x - 180.0
        if abs(dp) < 1e-30:
            break
        x -= p / dp
        if abs(p) < 1e-14:
            break
    return x


# ============================================================================
# 2. Shadow coefficients S_r via convolution recursion
# ============================================================================

def shadow_coefficients_numerical(c_val: float, max_r: int = 30) -> Dict[int, float]:
    """S_r for Virasoro at numerical c, via convolution recursion.

    f(t) = sqrt(Q_L(t)), f^2 = Q_L.
    a_0 = c, a_1 = 6, a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j} for n >= 3.
    S_r = a_{r-2} / r.
    """
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    max_n = max_r - 2
    a = [0.0] * (max_n + 1)
    a[0] = c_val
    if max_n >= 1:
        a[1] = q1 / (2.0 * c_val)  # = 6
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * c_val)
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2.0 * c_val)

    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= max_n:
            result[r] = a[n] / r
    return result


def shadow_coefficients_exact(c_frac: Fraction, max_r: int = 30) -> Dict[int, Fraction]:
    """S_r for Virasoro at exact rational c."""
    q0 = c_frac ** 2
    q1 = 12 * c_frac
    q2 = Fraction(180 * c_frac + 872, 5 * c_frac + 22)
    max_n = max_r - 2
    a = [Fraction(0)] * (max_n + 1)
    a[0] = c_frac
    if max_n >= 1:
        a[1] = q1 / (2 * c_frac)
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * c_frac)
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2 * c_frac)

    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= max_n:
            result[r] = a[n] / Fraction(r)
    return result


# ============================================================================
# 3. Genus expansion F_g = kappa * lambda_g^FP
# ============================================================================

def kappa_virasoro(c_val: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c_val / 2.0


def F_g_virasoro(g: int, c_val: float) -> float:
    """Genus-g free energy F_g = kappa * lambda_g^FP for Virasoro."""
    return kappa_virasoro(c_val) * float(_lambda_fp_exact(g))


def F_g_exact(g: int, c_frac: Fraction) -> Fraction:
    """Exact genus-g free energy for Virasoro."""
    return c_frac / 2 * _lambda_fp_exact(g)


# ============================================================================
# 4. Ordinary genus generating function and true Borel transforms
# ============================================================================

def genus_generating_function(xi: complex, kappa: float) -> complex:
    r"""Closed-form generating function of the genus expansion.

    G[F](xi) := sum_{g>=1} F_g * xi^{2g} = kappa * (xi / (2 sin(xi/2)) - 1)

    DERIVATION:
        The identity z/(2 sin(z/2)) = sum_{n>=0} (2^{2n-1}-1)|B_{2n}| z^{2n}/(2n)!
        (with the n=0 term equal to 1) gives, after subtracting 1:

        xi/(2 sin(xi/2)) - 1 = sum_{g>=1} (2^{2g-1}-1)|B_{2g}| xi^{2g} / (2g)!
                              = sum_{g>=1} lambda_g^FP * xi^{2g}

        Therefore G[F](xi) = kappa * (xi/(2 sin(xi/2)) - 1).

    The function xi/(2 sin(xi/2)) is meromorphic with simple poles at
    xi = 2*pi*n for n in Z \ {0}.  These are singularities of the ordinary
    generating function.

    RELATION TO BOREL TRANSFORM:
        The Borel transform B[F](xi) = sum F_g xi^{2g} / (2g)! is different:
        it divides each term by an ADDITIONAL (2g)!. The generating function
        G[F] is meromorphic, while this even Borel transform is entire.
    """
    xi = complex(xi)
    if abs(xi) < 1e-15:
        return kappa * xi ** 2 / 24.0
    half = xi / 2.0
    sin_half = cmath.sin(half)
    if abs(sin_half) < 1e-30:
        return complex(float('inf'))
    return kappa * (xi / (2.0 * sin_half) - 1.0)


def genus_generating_function_series(xi: complex, kappa: float, g_max: int = 60) -> complex:
    r"""Generating function via truncated series (independent verification).

    G[F](xi) = sum_{g=1}^{g_max} F_g * xi^{2g}
             = sum_{g=1}^{g_max} kappa * lambda_g^FP * xi^{2g}
    """
    xi = complex(xi)
    result = 0j
    for g in range(1, g_max + 1):
        lfp = float(_lambda_fp_exact(g))
        term = kappa * lfp * xi ** (2 * g)
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_transform_even_series(xi: complex, kappa: float, g_max: int = 80) -> complex:
    r"""Even Borel transform via truncated series.

    B_even[F](xi) = sum_{g=1}^{g_max} F_g * xi^{2g} / (2g)!
                  = sum_{g=1}^{g_max} kappa * lambda_g^FP * xi^{2g} / (2g)!

    Since F_g is geometric in g, the extra (2g)! denominator makes this
    transform entire.  In particular it is finite at xi = 2*pi*n, where the
    ordinary generating function G[F] has poles.
    """
    xi = complex(xi)
    result = 0j
    for g in range(1, g_max + 1):
        lfp = float(_lambda_fp_exact(g))
        term = kappa * lfp * xi ** (2 * g) / math.factorial(2 * g)
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_transform_t_series(s: complex, kappa: float, g_max: int = 80) -> complex:
    r"""Standard Borel transform in t = x^2.

    For f(t) = sum_{g>=1} F_g t^g, the standard Borel transform is

        B_t[f](s) = sum_{g>=1} F_g s^g/g!.

    The coefficients F_g = kappa*lambda_g^FP are geometric with radius
    (2*pi)^2 in the t-plane, hence B_t[f] is entire.
    """
    s = complex(s)
    result = 0j
    for g in range(1, g_max + 1):
        lfp = float(_lambda_fp_exact(g))
        term = kappa * lfp * s ** g / math.factorial(g)
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_transform_series(xi: complex, kappa: float, g_max: int = 80) -> complex:
    r"""Compatibility wrapper for the even Borel transform.

    Use ``borel_transform_t_series`` for the standard Borel transform in
    t = x^2.  This wrapper is not the meromorphic closed form G[F].
    """
    return borel_transform_even_series(xi, kappa, g_max=g_max)


# ============================================================================
# 5. Convergence verification: partial sums of sum S_r t^r
# ============================================================================

def partial_sum_shadow(c_val: float, t: float, max_r: int = 30) -> List[Tuple[int, float]]:
    """Partial sums of sum_{r=2}^{R} S_r(c) * t^r, for studying convergence.

    Returns [(R, partial_sum_R)] for R = 2, 3, ..., max_r.
    """
    coeffs = shadow_coefficients_numerical(c_val, max_r)
    partial = 0.0
    results = []
    for r in range(2, max_r + 1):
        if r in coeffs:
            partial += coeffs[r] * t ** r
            results.append((r, partial))
    return results


def convergence_test_at_c(c_val: float, max_r: int = 25) -> Dict[str, Any]:
    """Test convergence of sum S_r t^r at t=1 for given c.

    For c > c* ~ 6.125: rho(c) < 1, so the series at t=1 converges.
    For c < c*: rho(c) > 1, so the series at t=1 diverges.
    """
    rho = growth_rate(c_val)
    coeffs = shadow_coefficients_numerical(c_val, max_r)

    # Partial sums at t=1
    partial = 0.0
    sums = []
    for r in range(2, max_r + 1):
        if r in coeffs:
            partial += coeffs[r]
            sums.append((r, partial))

    # Check convergence: ratio |S_{r+1}/S_r| should approach rho
    ratios = []
    for r in range(4, max_r):
        if r in coeffs and r + 1 in coeffs and abs(coeffs[r]) > 1e-50:
            ratios.append((r, abs(coeffs[r + 1] / coeffs[r])))

    # True function value: H(1) = sqrt(Q_L(1)) where Q_L(t) = c^2 + 12c*t + q2*t^2
    q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)
    Q_at_1 = q0 + q1 + q2
    H_at_1 = math.sqrt(Q_at_1) if Q_at_1 > 0 else float('nan')

    converges = rho < 1.0

    return {
        'c': c_val,
        'rho': rho,
        'converges': converges,
        'partial_sums': sums,
        'ratio_test': ratios,
        'true_value_sqrt_QL': H_at_1,
        'last_partial_sum': sums[-1][1] if sums else None,
    }


def verify_convergence_at_c(c_val: float, max_r: int = 25) -> bool:
    """Verify: for c > c*, last few partial sums are close to the true value."""
    result = convergence_test_at_c(c_val, max_r)
    if not result['converges']:
        return False
    # The partial sums of S_r * 1^r should approach sqrt(Q_L(1)) - c
    # because H(t) = t^2 * sqrt(Q_L(t)) and sum S_r t^r = (H(t) - c*t^2 - 6*t^3)/...
    # More precisely: sqrt(Q_L(t)) = sum a_n t^n, and S_r = a_{r-2}/r.
    # So sum_{r=2}^R S_r = sum_{r=2}^R a_{r-2}/r.
    # This differs from H(1).
    # The correct comparison: check that partial sums stabilize.
    sums = result['partial_sums']
    if len(sums) < 5:
        return False
    last5 = [s[1] for s in sums[-5:]]
    spread = max(last5) - min(last5)
    scale = max(abs(last5[-1]), 1e-10)
    return spread / scale < 0.01  # Within 1% variation


# ============================================================================
# 6. Gevrey-0 verification
# ============================================================================

def gevrey_class_test(c_val: float, max_r: int = 25) -> Dict[str, Any]:
    r"""Verify Gevrey-0 growth: |S_r| / r! -> 0 as r -> infinity.

    Gevrey-0 means the growth is sub-factorial. Specifically, for the shadow:
        |S_r| ~ C * rho^r * r^{-5/2}
    so |S_r| / r! ~ C * rho^r / (r! * r^{5/2}) -> 0 super-exponentially.

    For comparison, Gevrey-1 (string genus expansion) has
        |a_g| ~ C * A^{-2g} * (2g)!
    so |a_g| / (2g)! -> const != 0.
    """
    coeffs = shadow_coefficients_numerical(c_val, max_r)
    rho = growth_rate(c_val)

    gevrey_ratios = []
    for r in range(4, max_r + 1):
        if r in coeffs:
            Sr = abs(coeffs[r])
            if Sr > 0:
                ratio = Sr / math.factorial(r)
                gevrey_ratios.append((r, ratio))

    # Also test the rescaled ratio |S_r| / rho^r * r^{5/2} -> C (constant)
    darboux_ratios = []
    for r in range(4, max_r + 1):
        if r in coeffs:
            Sr = abs(coeffs[r])
            if Sr > 0 and rho > 0:
                rescaled = Sr / (rho ** r) * r ** 2.5
                darboux_ratios.append((r, rescaled))

    is_gevrey_0 = all(gevrey_ratios[i][1] > gevrey_ratios[i + 1][1]
                      for i in range(len(gevrey_ratios) - 1)
                      if i >= 2)  # skip first few due to initial transient

    return {
        'c': c_val,
        'rho': rho,
        'gevrey_ratios': gevrey_ratios,
        'darboux_ratios': darboux_ratios,
        'is_gevrey_0': is_gevrey_0,
    }


# ============================================================================
# 7. Borel-Laplace integral (numerical)
# ============================================================================

def borel_laplace_integral(x_sq: float, kappa: float,
                           theta: float = 0.0,
                           n_points: int = 2000,
                           xi_max: float = 50.0) -> complex:
    r"""Numerical standard Borel-Laplace integral in t = x^2.

    For f(t) = sum_{g>=1} F_g t^g and t = x^2, use

        S_theta[f](t) = integral_0^{exp(i*theta)*inf}
                        B_t[f](s) * exp(-s/t) ds/t.

    Here B_t[f](s) = sum F_g s^g/g! is entire.  For the positive real
    t used by the tests, the integral converges when
    Re(exp(i*theta)/t) is larger than the exponential type 1/(2*pi)^2.

    The ``xi_max`` parameter is the finite cutoff in the standard Borel
    variable s; the name remains for caller compatibility.

    Parameters:
        x_sq: the value of x^2 (positive real)
        kappa: the modular characteristic kappa(A)
        theta: direction angle in the s-Borel plane
        n_points: quadrature points
        xi_max: upper integration limit

    Returns the truncated Borel-Laplace sum.
    """
    if x_sq <= 0:
        raise ValueError("x^2 must be positive")
    dt = xi_max / n_points
    direction = cmath.exp(1j * theta)
    result = 0j

    for i in range(1, n_points + 1):
        u = (i - 0.5) * dt
        s = u * direction
        try:
            b_val = borel_transform_t_series(s, kappa)
            exponential = cmath.exp(-s / x_sq)
            integrand = b_val * exponential * direction / x_sq
            result += integrand * dt
        except (OverflowError, ZeroDivisionError):
            continue

    return result


def lateral_borel_sums(x_sq: float, kappa: float,
                       epsilon: float = 0.05,
                       n_points: int = 3000,
                       xi_max: float = 60.0) -> Dict[str, complex]:
    r"""Compute paired lateral Borel-Laplace integrals.

    In this scalar sector the true Borel transform is entire.  Therefore the
    mathematical lateral jump is zero whenever the contour rotation remains
    in a convergent sector.
    """
    s_plus = borel_laplace_integral(x_sq, kappa, theta=epsilon,
                                    n_points=n_points, xi_max=xi_max)
    s_minus = borel_laplace_integral(x_sq, kappa, theta=-epsilon,
                                     n_points=n_points, xi_max=xi_max)
    return {
        'S_plus': s_plus,
        'S_minus': s_minus,
        'discontinuity': s_plus - s_minus,
        'mean_borel_sum': (s_plus + s_minus) / 2.0,
    }


# ============================================================================
# 8. Ordinary generating-function pole residues
# ============================================================================

def ordinary_genus_pole_residue(n: int, kappa: float) -> float:
    r"""Residue of G[F](xi) at xi = 2*pi*n.

    G[F](xi) = kappa * (xi / (2 sin(xi/2)) - 1)
    has simple poles at xi = 2*pi*n with:

        Res_{xi=2*pi*n} = kappa * lim_{xi -> 2*pi*n} (xi - 2*pi*n) * xi / (2 sin(xi/2))

    Near xi = 2*pi*n: sin(xi/2) ~ (-1)^n * (xi - 2*pi*n)/2
    so xi/(2 sin(xi/2)) ~ 2*pi*n / ((-1)^n * (xi - 2*pi*n))

    Residue = kappa * (-1)^n * 2*pi*n.

    Verified by L'Hopital: sin(xi/2) = sin(pi*n + (xi-2*pi*n)/2) = (-1)^n sin((xi-2*pi*n)/2)
    ~ (-1)^n (xi-2*pi*n)/2. So xi/(2*sin(xi/2)) ~ xi/((-1)^n*(xi-2*pi*n))
    and (xi-2*pi*n) * xi/(2*sin(xi/2)) -> (-1)^n * 2*pi*n.
    """
    return kappa * ((-1) ** n) * 2.0 * math.pi * n


def ordinary_genus_pole_circulation(n: int, kappa: float) -> complex:
    r"""Pole circulation 2*pi*i * Res_{xi=2*pi*n} G[F](xi).

    This is an ordinary contour integral around a pole of G[F].  It is not a
    lateral-jump constant for the true Borel transform, which is entire here.
    """
    return 2.0j * math.pi * ordinary_genus_pole_residue(n, kappa)


def scalar_genus_singularity_audit(kappa: float, n: int = 1) -> Dict[str, Any]:
    r"""Separate ordinary poles, reconstructed-sum singularities, and Borel data.

    The scalar closed form has ordinary poles in the xi-plane.  The analytic
    sum in the variable t = xi^2 has singularities at t = (2*pi*n)^2.  The
    true Borel transforms obtained by dividing by g! or (2g)! are entire.
    Consequently ordinary residues are not Stokes constants for this scalar
    Borel transform, and no alien calculus data is certified here.
    """
    if n == 0:
        raise ValueError("n must be nonzero")
    xi0 = 2.0 * math.pi * n
    t0 = xi0 ** 2
    residue = ordinary_genus_pole_residue(n, kappa)

    return {
        'kappa': kappa,
        'n': n,
        'ordinary_xi_plane': {
            'function': 'G[F](xi) = kappa*(xi/(2*sin(xi/2)) - 1)',
            'pole': xi0,
            'residue': residue,
            'circulation': 2.0j * math.pi * residue,
        },
        'ordinary_t_plane': {
            'variable': 't = xi^2',
            'singularity': t0,
            'nearest_positive_singularity': INSTANTON_ACTION if abs(n) == 1 else None,
            'are_borel_plane_singularities': False,
        },
        'true_borel_t_plane': {
            'transform': 'B_t[F](s) = sum F_g s^g/g!',
            'singularity_set': (),
            'entire': True,
        },
        'true_borel_even_plane': {
            'transform': 'B_even[F](xi) = sum F_g xi^(2g)/(2g)!',
            'singularity_set': (),
            'entire': True,
        },
        'ordinary_residue_is_stokes_constant': False,
        'ecalle_stokes_alien_calculus_certified': False,
        'scalar_projection_certifies_full_maurer_cartan_data': False,
    }


# ============================================================================
# 9. Lateral Borel-Laplace jump diagnostic
# ============================================================================

def lateral_borel_jump_diagnostic(x_sq: float, kappa: float,
                                  epsilon: float = 0.03,
                                  n_points: int = 4000,
                                  xi_max: float = 80.0) -> Dict[str, Any]:
    r"""Measure the paired lateral Borel-Laplace difference.

    The scalar sector has an entire true Borel transform, so the mathematical
    jump is zero in any common convergence sector.  This diagnostic records
    the numerical difference between the two truncated quadratures.
    """
    lateral = lateral_borel_sums(x_sq, kappa, epsilon=epsilon,
                                 n_points=n_points, xi_max=xi_max)
    disc = lateral['discontinuity']

    leading_jump = 0j

    return {
        'x_sq': x_sq,
        'kappa': kappa,
        'discontinuity': disc,
        'leading_prediction': leading_jump,
        'ratio_numerical_to_predicted': None,
        'disc_abs': abs(disc),
        'leading_abs': 0.0,
        'instanton_action': INSTANTON_ACTION,
        'ordinary_pole_circulation': ordinary_genus_pole_circulation(1, kappa),
    }


# ============================================================================
# 10. Borel analyticity verification
# ============================================================================

def genus_generating_function_analyticity_strip(kappa: float,
                                                im_range: float = 1.0,
                                                re_range: Tuple[float, float] = (0.1, 6.0),
                                                n_points: int = 200) -> Dict[str, Any]:
    r"""Sample the ordinary function G[F](xi) away from its poles.

    The exact closed form proves analyticity away from xi = 2*pi*n.  This
    helper is only a finite numerical regularity diagnostic in the strip
    |Im(xi)| < im_range,
    Re(xi) in [re_range[0], re_range[1]], away from xi = 2*pi.

    The ordinary generating function G[F](xi) = kappa*(xi/(2*sin(xi/2)) - 1) is analytic
    everywhere except at the poles xi = 2*pi*n. In the strip between
    0 and 2*pi, it should be well-behaved.

    We verify this by checking:
    1. The function is finite at all sample points
    """
    re_vals = [re_range[0] + i * (re_range[1] - re_range[0]) / n_points
               for i in range(n_points + 1)]

    evaluations = []
    max_val = 0.0
    min_dist_to_pole = float('inf')

    for re in re_vals:
        for im_sign in [1.0, -1.0]:
            im = im_sign * im_range * 0.5
            xi = complex(re, im)
            dist = abs(xi - 2.0 * math.pi)
            min_dist_to_pole = min(min_dist_to_pole, dist)
            try:
                val = genus_generating_function(xi, kappa)
                evaluations.append((re, im, abs(val)))
                max_val = max(max_val, abs(val))
            except (OverflowError, ZeroDivisionError):
                evaluations.append((re, im, float('inf')))

    all_finite = all(e[2] < 1e10 for e in evaluations)

    return {
        'strip_width': im_range,
        're_range': re_range,
        'n_evaluations': len(evaluations),
        'all_finite': all_finite,
        'max_abs_value': max_val,
        'min_dist_to_pole': min_dist_to_pole,
    }


def borel_analyticity_strip(kappa: float,
                            im_range: float = 1.0,
                            re_range: Tuple[float, float] = (0.1, 6.0),
                            n_points: int = 200) -> Dict[str, Any]:
    r"""Compatibility wrapper for G[F] strip analyticity.

    The true Borel transforms are entire; this helper samples the ordinary
    generating function away from its poles.
    """
    return genus_generating_function_analyticity_strip(kappa, im_range, re_range, n_points)


# ============================================================================
# 11. Closed-form vs series verification
# ============================================================================

def verify_generating_function_vs_series(kappa: float, xi_test_points: Optional[List[complex]] = None,
                                          g_max: int = 80) -> List[Tuple[complex, float]]:
    r"""Verify G[F]_closed(xi) = G[F]_series(xi) at test points.

    The closed form kappa * (xi/(2*sin(xi/2)) - 1) must agree with the
    truncated series sum_{g=1}^{g_max} kappa * lambda_g^FP * xi^{2g}
    for |xi| < 2*pi (inside the convergence disk).

    Returns [(xi, |closed - series|)] for each test point.
    """
    if xi_test_points is None:
        xi_test_points = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0,
                          1.0 + 1.0j, 2.0 - 0.5j, 3.0 + 0.3j]
    results = []
    for xi in xi_test_points:
        xi = complex(xi)
        closed = genus_generating_function(xi, kappa)
        series = genus_generating_function_series(xi, kappa, g_max)
        diff = abs(closed - series)
        results.append((xi, diff))
    return results


# ============================================================================
# 12. Instanton action verification
# ============================================================================

INSTANTON_ACTION = (2.0 * math.pi) ** 2  # A = (2*pi)^2 ~ 39.478


def verify_instanton_action(c_val: float, g_max: int = 12) -> Dict[str, Any]:
    r"""Verify the t-plane radius A = (2*pi)^2 from the large-genus ratio.

    For F_g = kappa * lambda_g^FP with lambda_g^FP ~ 2/(2*pi)^{2g}
    at large g (from Bernoulli asymptotics |B_{2g}| ~ 2*(2g)!/(2*pi)^{2g}),
    the ratio F_{g-1}/F_g approaches (2*pi)^2.

    This number is the first ordinary-generating-function singular radius in
    t = x^2.  It is not a pole of the true Borel transform.
    """
    kappa = kappa_virasoro(c_val)
    estimates = []
    for g in range(2, g_max + 1):
        fg = F_g_virasoro(g, c_val)
        fg_prev = F_g_virasoro(g - 1, c_val)
        if abs(fg) > 1e-100:
            A_est = abs(fg_prev / fg)
            estimates.append((g, A_est))

    return {
        'c': c_val,
        'kappa': kappa,
        'estimates': estimates,
        'target_A': INSTANTON_ACTION,
        'best_estimate': estimates[-1][1] if estimates else None,
        'relative_error': abs(estimates[-1][1] - INSTANTON_ACTION) / INSTANTON_ACTION if estimates else None,
    }


# ============================================================================
# 13. Discriminant and oscillatory structure
# ============================================================================

def shadow_discriminant(c_val: float) -> float:
    """Discriminant of Q_L(t): disc = q1^2 - 4*q0*q2 = -320c^2/(5c+22).

    Always negative for c > 0, so branch points are complex conjugate.
    """
    return -320.0 * c_val ** 2 / (5.0 * c_val + 22.0)


def oscillatory_parameters(c_val: float) -> Dict[str, float]:
    """Oscillatory parameters from the complex branch points.

    The branch points t_* and t_*bar produce oscillatory factors in S_r:
        S_r ~ C * rho^r * r^{-5/2} * cos(r * theta + phi)
    where theta = pi - |arg(t_*)| is the oscillation frequency.
    """
    t_plus, _ = shadow_metric_branch_points(c_val)
    rho = 1.0 / abs(t_plus)
    arg_t = cmath.phase(t_plus)
    theta = math.pi - abs(arg_t)  # oscillation angle
    beat_period = math.pi / theta if abs(theta) > 1e-10 else float('inf')
    return {
        'rho': rho,
        'arg_t_star': math.degrees(arg_t),
        'theta_oscillation': theta,
        'beat_period': beat_period,
        'c': c_val,
    }


# ============================================================================
# 14. Scalar Borel diagnostics data package
# ============================================================================

def borel_summability_data(c_val: float, max_r: int = 25, g_max: int = 10
                           ) -> Dict[str, Any]:
    """Scalar Borel diagnostic data at a given c.

    The function name is retained for caller compatibility.  The payload
    deliberately distinguishes certified scalar facts from non-certified
    analytic claims.  It does not certify full Borel summability of the
    shadow obstruction tower from a finite coefficient window.

    Collects:
    - Growth rate rho and convergence radius R = 1/rho
    - Gevrey class diagnostic for the shadow tower coefficients
    - Branch point locations and oscillatory parameters
    - t-plane radius from the scalar genus coefficients
    - ordinary generating-function pole circulation
    - G[F] analyticity in the strip [0, 2*pi)
    """
    kappa = kappa_virasoro(c_val)
    rho = growth_rate(c_val)
    c_star = critical_central_charge()
    t_plus, t_minus = shadow_metric_branch_points(c_val)
    certification = analytic_certification_firewall()

    return {
        'c': c_val,
        'kappa': kappa,
        'rho': rho,
        'convergence_radius': 1.0 / rho,
        'c_star': c_star,
        'converges_at_t1': rho < 1.0,
        'branch_points': (t_plus, t_minus),
        'discriminant': shadow_discriminant(c_val),
        'instanton_action': INSTANTON_ACTION,
        'ordinary_pole_residue_n1': ordinary_genus_pole_residue(1, kappa),
        'ordinary_pole_circulation_n1': ordinary_genus_pole_circulation(1, kappa),
        'ordinary_t_plane_nearest_singularity': INSTANTON_ACTION,
        'true_borel_singularity_set': (),
        'true_borel_transform_entire': True,
        'lateral_jump_expected': 0j,
        'gevrey_class': 0,
        'certification': certification,
        'scalar_borel_summability_certified': True,
        'scalar_borel_summability_scope': 'Borel-Laplace reconstruction of the convergent scalar series',
        'bare_shadow_borel_summability_certified': False,
        'finite_window_certifies_summability': False,
        'pade_darboux_certifies_stokes_data': False,
        'ecalle_stokes_data_certified': False,
        'full_maurer_cartan_data_certified': False,
        'global_resurgence_certified': False,
        'analytic_continuation_certified': False,
        'nonperturbative_completion_certified': False,
        'btz_jt_recovery_certified': False,
        'multiweight_extension_certified': False,
        'all_genus_partition_theorem_certified': False,
    }


# ============================================================================
# 15. Comparison: shadow vs string Borel structure
# ============================================================================

def shadow_vs_string_comparison(c_val: float, g_max: int = 15) -> Dict[str, Any]:
    r"""Compare Borel structure of shadow vs string genus expansion.

    Scalar shadow: F_g^{sh} = kappa * lambda_g^FP ~ kappa * 2/(2*pi)^{2g}
        Growth: GEOMETRIC (Gevrey-0).  The ordinary series is convergent
        for |x| < 2*pi; the true Borel transforms are entire.

    String: F_g^{str} ~ (2g)! * A^{-2g}
        Growth: FACTORIAL (Gevrey-1) in this toy comparison sequence.

    This function verifies coefficient-growth separation only.  It does not
    decide the Borel singularity geometry of the full string expansion, and
    it does not certify the full shadow obstruction tower as Borel summable.
    """
    kappa = kappa_virasoro(c_val)

    shadow_coeffs = []
    string_coeffs = []
    ratios = []

    for g in range(1, g_max + 1):
        f_shadow = F_g_virasoro(g, c_val)
        # String approximation: F_g^{string} ~ (2g-2)! * A^{-(2g-2)}
        # (using the convention that the string genus expansion is sum F_g x^{2g-2})
        f_string = math.factorial(2 * g - 2) / INSTANTON_ACTION ** (g - 1)

        shadow_coeffs.append((g, abs(f_shadow)))
        string_coeffs.append((g, abs(f_string)))
        if abs(f_shadow) > 1e-100:
            ratios.append((g, abs(f_string / f_shadow)))

    return {
        'c': c_val,
        'kappa': kappa,
        'shadow_coefficients': shadow_coeffs,
        'string_coefficients': string_coeffs,
        'string_to_shadow_ratio': ratios,
        'shadow_gevrey': 0,
        'string_gevrey': 1,
        'shadow_borel_summable': None,
        'shadow_borel_summable_scope': 'not a bare global certificate',
        'scalar_borel_summability_certified': True,
        'shadow_series_convergent': True,
        'string_borel_summable_on_real_axis': None,
        'string_borel_geometry_certified': False,
    }
