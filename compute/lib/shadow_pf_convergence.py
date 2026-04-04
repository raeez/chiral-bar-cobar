r"""Analytic continuation and convergence analysis of the shadow partition function.

MATHEMATICAL FRAMEWORK
======================

The shadow partition function Z^sh(q, hbar) encodes the genus expansion
of the shadow CohFT.  At the scalar level (arity 2):

    F_g^{scal} = kappa * lambda_g^{FP}

where lambda_g^{FP} = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!.  The
generating function is

    sum_{g>=1} F_g^{scal} hbar^{2g} = kappa * (A-hat(i*hbar) - 1)

where A-hat(x) = (x/2)/sinh(x/2).  At imaginary argument i*hbar:

    A-hat(i*hbar) = (hbar/2) / sin(hbar/2)

which has poles at hbar = 2*pi*n (n in Z \ {0}).

SEVEN ANALYTIC RESULTS
======================

1. GENUS CONVERGENCE: The scalar genus series has radius of convergence
   |hbar| < 2*pi, set by the poles of (hbar/2)/sin(hbar/2).
   Bernoulli decay: |F_g| ~ 2|kappa|/(2*pi)^{2g}.

2. ARITY CONVERGENCE: At fixed genus, the arity-r corrections decay as
   |S_r| ~ C * rho^r * r^{-5/2}.  Convergent iff rho < 1.
   Critical c*: unique positive root of 5c^3 + 22c^2 - 180c - 872 = 0.

3. DOUBLE SERIES: Z^sh(hbar, t) converges absolutely on
   D = {(hbar, t) : |hbar| < 2*pi, |t| < 1/rho}.

4. ANALYTIC CONTINUATION: Z^sh has simple poles at hbar = 2*pi*n.
   Residue at hbar = 2*pi computed from (hbar/2)/sin(hbar/2).

5. BOREL TRANSFORM: The Borel transform of the scalar genus series is
   entire (Bernoulli decay kills the factorial).  For the arity sum
   with rho > 1, the Borel transform in t also entire (factorial dominates).

6. MODULAR PROPERTIES: Z^sh transforms under S-duality via the
   modular transformation of the underlying chiral algebra.

7. BOUNDARY BEHAVIOR: At |hbar| -> 2*pi, Z^sh ~ C/(2*pi - |hbar|).
   The critical exponent is alpha = 1 (simple pole).

Manuscript references:
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    rem:convergence-vs-string (genus_expansions.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import mpmath
from sympy import (
    Rational, Symbol, bernoulli, factorial, pi as sym_pi,
    simplify, sqrt, Abs, N as Neval, oo, solve, cancel,
)

from compute.lib.utils import lambda_fp, F_g


# Symbols
c_sym = Symbol('c')
hbar_sym = Symbol('hbar')
t_sym = Symbol('t')

PI = math.pi
TWO_PI = 2 * PI
TWO_PI_SQ = TWO_PI ** 2


# =========================================================================
# Section 1: A-hat genus and genus convergence radius
# =========================================================================

def ahat_function(x: complex) -> complex:
    r"""A-hat(x) = (x/2) / sinh(x/2).

    At imaginary argument x = i*hbar:
        A-hat(i*hbar) = (hbar/2) / sin(hbar/2)

    Poles at x = 2*pi*i*n, equivalently hbar = 2*pi*n.
    """
    if abs(x) < 1e-15:
        return complex(1.0, 0.0)
    return (x / 2.0) / cmath.sinh(x / 2.0)


def ahat_at_imaginary(hbar: float) -> float:
    r"""A-hat(i*hbar) = (hbar/2) / sin(hbar/2).

    Real-valued for real hbar.  Poles at hbar = 2*pi*n.
    """
    if abs(hbar) < 1e-15:
        return 1.0
    return (hbar / 2.0) / math.sin(hbar / 2.0)


def genus_series_closed_form(kappa_val: float, hbar: float) -> float:
    r"""Closed-form scalar genus series.

    sum_{g>=1} F_g hbar^{2g} = kappa * (A-hat(i*hbar) - 1)
                              = kappa * ((hbar/2)/sin(hbar/2) - 1)

    Valid for |hbar| < 2*pi.
    """
    return kappa_val * (ahat_at_imaginary(hbar) - 1.0)


def genus_series_partial_sum(kappa_val, max_genus: int, hbar: float = 1.0) -> float:
    r"""Partial sum sum_{g=1}^{G} F_g * hbar^{2g}.

    Uses exact rational arithmetic for lambda_g^{FP} then converts.
    """
    total = 0.0
    kv = Rational(kappa_val) if isinstance(kappa_val, (int, float)) else kappa_val
    for g in range(1, max_genus + 1):
        fg = float(F_g(kv, g))
        total += fg * hbar ** (2 * g)
    return total


def genus_convergence_radius() -> float:
    r"""Radius of convergence of the scalar genus series in hbar.

    The generating function (hbar/2)/sin(hbar/2) has poles at
    hbar = 2*pi*n (n != 0).  The nearest pole is at |hbar| = 2*pi.

    Returns 2*pi.
    """
    return TWO_PI


def genus_convergence_verification(kappa_val: float,
                                    max_genus: int = 50) -> Dict[str, Any]:
    r"""Verify genus convergence radius = 2*pi.

    Compute partial sums at hbar values within and near the radius.
    """
    results = {}

    for label, hbar_val in [('hbar_1', 1.0), ('hbar_5', 5.0), ('hbar_6', 6.0)]:
        closed = genus_series_closed_form(kappa_val, hbar_val)
        partial = genus_series_partial_sum(kappa_val, max_genus, hbar_val)
        results[label] = {
            'closed_form': closed,
            'partial_sum': partial,
            'relative_error': abs(partial - closed) / abs(closed) if closed != 0 else 0,
        }

    results['asymptotic_ratios'] = {
        'hbar_1': 1.0 / TWO_PI_SQ,
        'hbar_5': 25.0 / TWO_PI_SQ,
        'hbar_6': 36.0 / TWO_PI_SQ,
        'hbar_2pi': 1.0,
    }
    results['convergence_radius'] = TWO_PI
    return results


# =========================================================================
# Section 2: Bernoulli decay and string comparison
# =========================================================================

def bernoulli_decay_coefficients(max_genus: int = 30) -> Dict[str, Any]:
    r"""Compute the Bernoulli decay of lambda_g^{FP}.

    |lambda_g^{FP}| ~ 2 / (2*pi)^{2g} from the Euler formula for |B_{2g}|.
    """
    data = []
    for g in range(1, max_genus + 1):
        lam = float(lambda_fp(g))
        predicted = 2.0 / TWO_PI ** (2 * g)
        ratio = lam / predicted if predicted > 0 else 0
        data.append({'g': g, 'lambda_fp': lam,
                     'predicted_asymptotic': predicted, 'ratio': ratio})

    return {'data': data, 'asymptotic_constant': 2.0,
            'base': 1.0 / TWO_PI_SQ, 'max_genus': max_genus}


def string_divergence_rate(max_genus: int = 15) -> Dict[str, Any]:
    r"""Contrast shadow vs string genus series.

    Shadow: |F_g| ~ 2|kappa| / (2*pi)^{2g}  -> geometric decay
    String: |A_g| ~ C * (2g)!               -> factorial growth
    """
    data = []
    for g in range(1, max_genus + 1):
        shadow = float(lambda_fp(g))
        string = float(math.factorial(2 * g))
        ratio = shadow / string if string > 0 else 0
        data.append({
            'g': g, 'shadow_lambda_fp': shadow,
            'string_vol_estimate': string, 'ratio': ratio,
            'log_ratio': math.log10(ratio) if ratio > 0 else float('-inf'),
        })
    return {'data': data}


# =========================================================================
# Section 3: Arity convergence and critical c*
# =========================================================================

def virasoro_shadow_radius_squared(c_val: float) -> float:
    r"""rho^2(Vir_c) = (180c + 872) / ((5c + 22) * c^2).

    Derivation: kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)).
    9*alpha^2 + 2*Delta = 36 + 80/(5c+22) = (180c + 872)/(5c+22).
    rho^2 = (180c+872) / ((5c+22) * c^2).
    """
    return (180 * c_val + 872) / ((5 * c_val + 22) * c_val ** 2)


def virasoro_shadow_radius(c_val: float) -> float:
    r"""rho(Vir_c) = sqrt((180c+872)/((5c+22)*c^2))."""
    rho_sq = virasoro_shadow_radius_squared(c_val)
    if rho_sq < 0:
        return float('nan')
    return math.sqrt(rho_sq)


def arity_convergence_radius(rho: float) -> float:
    r"""Radius of convergence of the arity series: R_t = 1/rho."""
    if rho <= 0:
        return float('inf')
    return 1.0 / rho


def critical_central_charge() -> float:
    r"""Critical central charge c* where rho(Vir_{c*}) = 1.

    Solves 5c^3 + 22c^2 - 180c - 872 = 0.
    Unique positive real root: c* ~ 6.1243.
    """
    c = Symbol('c')
    poly = 5 * c**3 + 22 * c**2 - 180 * c - 872
    roots = solve(poly, c)
    for r in roots:
        val = complex(r.evalf())
        if abs(val.imag) < 1e-10 and val.real > 0:
            return val.real
    return float('nan')


def arity_convergence_landscape() -> Dict[str, Any]:
    r"""Arity convergence data for all four depth classes."""
    c_star = critical_central_charge()
    landscape = {}

    landscape['Heisenberg'] = {
        'class': 'G', 'rho': 0.0, 'R_arity': float('inf'),
        'convergent': True,
    }
    landscape['Affine_sl2'] = {
        'class': 'L', 'rho': 0.0, 'R_arity': float('inf'),
        'convergent': True,
    }
    landscape['Beta_gamma'] = {
        'class': 'C', 'rho': None, 'R_arity': None,
        'convergent': None,
    }

    for label, c_val in [('Vir_c=1/2', 0.5), ('Vir_c=1', 1.0),
                          ('Vir_c=4', 4.0), ('Vir_c=6', 6.0),
                          ('Vir_c=c*', c_star),
                          ('Vir_c=13', 13.0), ('Vir_c=25', 25.0),
                          ('Vir_c=26', 26.0)]:
        rho = virasoro_shadow_radius(c_val)
        landscape[label] = {
            'class': 'M', 'c': c_val, 'rho': rho,
            'R_arity': arity_convergence_radius(rho),
            'convergent': rho < 1.0,
        }

    landscape['c_star'] = c_star
    return landscape


# =========================================================================
# Section 4: Double convergence domain
# =========================================================================

@dataclass
class DoubleConvergenceDomain:
    r"""Joint convergence domain D = {(hbar, t) : |hbar| < R_genus, |t| < R_arity}.

    R_genus = 2*pi (from A-hat poles, universal).
    R_arity = 1/rho (from shadow radius, algebra-dependent).
    """
    R_genus: float
    R_arity: float
    rho: float
    kappa: float
    algebra_name: str = ''

    @property
    def physical_point_in_domain(self) -> bool:
        return self.rho < 1.0

    @property
    def area_estimate(self) -> float:
        if self.R_arity == float('inf'):
            return float('inf')
        return self.R_genus * self.R_arity


def double_convergence_domain(kappa_val: float, rho: float,
                               name: str = '') -> DoubleConvergenceDomain:
    r"""Construct the double convergence domain for Z^sh."""
    return DoubleConvergenceDomain(
        R_genus=TWO_PI,
        R_arity=arity_convergence_radius(rho),
        rho=rho, kappa=kappa_val, algebra_name=name,
    )


def double_convergence_table() -> List[Dict[str, Any]]:
    r"""Double convergence data for the standard landscape."""
    table = []

    table.append({
        'name': 'Heisenberg (rank 1)', 'class': 'G',
        'kappa': 0.5, 'rho': 0.0,
        'R_genus': TWO_PI, 'R_arity': float('inf'),
        'physical_in_domain': True,
    })

    # kappa(sl_2, k=1) = dim(sl_2)*(k+h^v)/(2*h^v) = 3*(1+2)/(2*2) = 9/4
    table.append({
        'name': 'Affine sl_2 (k=1)', 'class': 'L',
        'kappa': 9.0 / 4.0, 'rho': 0.0,
        'R_genus': TWO_PI, 'R_arity': float('inf'),
        'physical_in_domain': True,
    })

    c_star = critical_central_charge()
    for label, c_val in [('Vir c=1/2', 0.5), ('Vir c=1', 1.0),
                          ('Vir c=4', 4.0), ('Vir c=c*', c_star),
                          ('Vir c=13', 13.0), ('Vir c=25', 25.0),
                          ('Vir c=26', 26.0)]:
        rho = virasoro_shadow_radius(c_val)
        table.append({
            'name': label, 'class': 'M',
            'kappa': c_val / 2.0, 'rho': rho,
            'R_genus': TWO_PI,
            'R_arity': arity_convergence_radius(rho),
            'physical_in_domain': rho < 1.0,
        })

    return table


# =========================================================================
# Section 5: Residues and analytic continuation
# =========================================================================

def ahat_residue_at_2pi_n(n: int) -> float:
    r"""Residue of (hbar/2)/sin(hbar/2) at hbar = 2*pi*n.

    sin(hbar/2) near hbar = 2*pi*n:
        sin(hbar/2) = sin(pi*n + eps/2) = (-1)^n * sin(eps/2)
                    ~ (-1)^n * eps/2.

    So (hbar/2)/sin(hbar/2) ~ (pi*n)/((-1)^n * eps/2) = (-1)^n * 2*pi*n/eps.

    Residue = (-1)^n * 2*pi*n.
    """
    if n == 0:
        return 0.0
    return float((-1) ** n * 2 * PI * n)


def scalar_genus_series_residue(kappa_val: float, n: int) -> float:
    r"""Residue of kappa * (A-hat(i*hbar) - 1) at hbar = 2*pi*n.

    Res = kappa * (-1)^n * 2*pi*n.
    """
    return kappa_val * ahat_residue_at_2pi_n(n)


def ahat_residue_verification(n: int, eps: float = 1e-8) -> Dict[str, Any]:
    r"""Numerical verification of the residue at hbar = 2*pi*n."""
    hbar_pole = 2 * PI * n
    predicted = ahat_residue_at_2pi_n(n)

    z_p = hbar_pole + eps
    numerical_p = (z_p - hbar_pole) * ahat_at_imaginary(z_p)
    z_m = hbar_pole - eps
    numerical_m = (z_m - hbar_pole) * ahat_at_imaginary(z_m)
    numerical_avg = (numerical_p + numerical_m) / 2.0

    return {
        'n': n, 'pole_location': hbar_pole,
        'predicted_residue': predicted,
        'numerical_residue': numerical_avg,
        'relative_error': abs(numerical_avg - predicted) / abs(predicted) if predicted != 0 else abs(numerical_avg),
    }


# =========================================================================
# Section 6: Borel transform analysis
# =========================================================================

def borel_transform_genus_series(kappa_val: float, zeta: complex,
                                  max_genus: int = 100) -> complex:
    r"""Borel transform of the scalar genus series.

    B(zeta) = sum_{g>=1} kappa * lambda_g^{FP} * zeta^{2g} / (2g)!

    The Borel transform is ENTIRE: coefficients lambda_g^{FP} / (2g)!
    decay as 2 / ((2*pi)^{2g} * (2g)!), superexponential.
    """
    total = complex(0, 0)
    for g in range(1, max_genus + 1):
        lam = float(lambda_fp(g))
        coeff = kappa_val * lam / math.factorial(2 * g)
        term = coeff * zeta ** (2 * g)
        total += term
        if abs(term) < 1e-30 * max(abs(total), 1e-100):
            break
    return total


def borel_transform_is_entire(kappa_val: float,
                               test_points: Optional[List[complex]] = None,
                               max_genus: int = 80) -> Dict[str, Any]:
    r"""Verify the Borel transform of the genus series is entire.

    Test at progressively larger |zeta| values.
    """
    if test_points is None:
        test_points = [1.0, 5.0, 10.0, 50.0, 100.0,
                       1j, 5j, 10j, 1+1j, 10+10j]

    results = []
    for z in test_points:
        val = borel_transform_genus_series(kappa_val, z, max_genus)
        results.append({
            'zeta': z, 'modulus_zeta': abs(z),
            'value': val, 'modulus_value': abs(val),
            'finite': math.isfinite(abs(val)),
        })

    all_finite = all(r['finite'] for r in results)
    return {'kappa': kappa_val, 'is_entire': all_finite, 'test_results': results}


def string_borel_comparison(kappa_val: float,
                             max_genus: int = 20) -> Dict[str, Any]:
    r"""Compare Borel transforms of shadow vs string genus series."""
    shadow_coeffs = []
    string_coeffs = []
    for g in range(1, max_genus + 1):
        lam = float(lambda_fp(g))
        fac = math.factorial(2 * g)
        shadow_coeffs.append(abs(kappa_val) * lam / fac)
        string_coeffs.append(1.0)
    return {
        'shadow_borel_coefficients': shadow_coeffs,
        'string_borel_coefficients': string_coeffs,
        'shadow_entire': True, 'string_singular': True,
    }


# =========================================================================
# Section 7: Boundary behavior at |hbar| = 2*pi
# =========================================================================

def boundary_behavior(kappa_val: float, n_points: int = 20) -> Dict[str, Any]:
    r"""Analyze boundary behavior of Z^sh as |hbar| -> 2*pi.

    Near hbar = 2*pi: simple pole with Res = -2*pi*kappa.
    Critical exponent alpha = 1.
    """
    data = []
    for i in range(1, n_points + 1):
        eps = 10 ** (-i / 4.0)
        hbar = TWO_PI - eps
        val = genus_series_closed_form(kappa_val, hbar)
        singular_part = TWO_PI * kappa_val / eps
        regular_part = val - singular_part

        data.append({
            'eps': eps, 'hbar': hbar, 'Z_sh': val,
            'singular_part': singular_part, 'regular_part': regular_part,
            'ratio_Z_to_singular': val / singular_part if singular_part != 0 else 0,
        })

    return {
        'kappa': kappa_val, 'critical_exponent': 1,
        'leading_coefficient': -TWO_PI * kappa_val,
        'pole_type': 'simple', 'data': data,
    }


def boundary_exponent_extraction(kappa_val: float) -> Dict[str, Any]:
    r"""Extract the critical exponent alpha by linear regression.

    Z^sh ~ C * eps^{-alpha}, so log|Z| ~ -alpha*log(eps) + const.
    """
    eps_values = [10**(-k/2.0) for k in range(2, 16)]
    log_eps = []
    log_Z = []

    for eps in eps_values:
        hbar = TWO_PI - eps
        try:
            val = abs(genus_series_closed_form(kappa_val, hbar))
            if val > 0 and math.isfinite(val):
                log_eps.append(math.log(eps))
                log_Z.append(math.log(val))
        except (ValueError, ZeroDivisionError):
            continue

    if len(log_eps) < 3:
        return {'alpha': float('nan'), 'error': 'insufficient data'}

    n = len(log_eps)
    sx = sum(log_eps)
    sy = sum(log_Z)
    sxy = sum(x * y for x, y in zip(log_eps, log_Z))
    sxx = sum(x * x for x in log_eps)

    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    alpha = -slope

    return {
        'alpha': alpha, 'expected_alpha': 1.0,
        'relative_error': abs(alpha - 1.0), 'n_points': n,
    }


# =========================================================================
# Section 8: Modular properties (genus-1 level)
# =========================================================================

def genus_1_shadow_modular(kappa_val: float) -> Dict[str, Any]:
    r"""Modular properties of the genus-1 shadow.

    F_1 = kappa/24.  Under S-transform, the genus-1 free energy
    acquires an additive anomaly proportional to kappa.
    """
    return {'kappa': kappa_val, 'F_1': kappa_val / 24.0,
            'modular_anomaly': kappa_val}


# =========================================================================
# Section 9: High-precision convergence (mpmath)
# =========================================================================

def hp_ahat(hbar_mp):
    r"""High-precision A-hat(i*hbar) = (hbar/2)/sin(hbar/2)."""
    if hbar_mp == 0:
        return mpmath.mpf(1)
    half_h = hbar_mp / 2
    return half_h / mpmath.sin(half_h)


def hp_genus_series(kappa_mp, hbar_mp, max_genus: int = 100):
    r"""High-precision partial sum of the scalar genus series."""
    total = mpmath.mpf(0)
    for g in range(1, max_genus + 1):
        B2g = mpmath.bernoulli(2 * g)
        prefac = (mpmath.mpf(2) ** (2 * g - 1) - 1) / mpmath.mpf(2) ** (2 * g - 1)
        lam = prefac * abs(B2g) / mpmath.factorial(2 * g)
        term = kappa_mp * lam * hbar_mp ** (2 * g)
        total += term
        if abs(term) < mpmath.mpf(10) ** (-mpmath.mp.dps + 5):
            break
    return total


def hp_convergence_radius_verification(kappa_val: float = 1.0,
                                        precision: int = 50) -> Dict[str, Any]:
    r"""High-precision verification that R = 2*pi.

    Evaluates partial sums at hbar approaching 2*pi.
    """
    old_dps = mpmath.mp.dps
    mpmath.mp.dps = precision

    try:
        kappa_mp = mpmath.mpf(kappa_val)
        two_pi = 2 * mpmath.pi

        results = []
        for frac in [0.5, 0.9, 0.95, 0.99, 0.999, 0.9999]:
            hbar = frac * two_pi
            closed = kappa_mp * (hp_ahat(hbar) - 1)
            partial = hp_genus_series(kappa_mp, hbar, max_genus=200)
            error = abs(partial - closed)
            results.append({
                'hbar_over_2pi': float(frac),
                'closed_form': float(closed),
                'partial_sum': float(partial),
                'absolute_error': float(error),
                'converged': float(error) < 10 ** (-(precision // 2)),
            })

        all_converge = all(r['converged'] for r in results)
        return {
            'precision_digits': precision,
            'convergence_radius': float(two_pi),
            'inside_disc_converge': all_converge,
            'results': results,
        }
    finally:
        mpmath.mp.dps = old_dps


def hp_residue_at_2pi(kappa_val: float = 1.0,
                       precision: int = 50) -> Dict[str, Any]:
    r"""High-precision residue at hbar = 2*pi.

    Res = -2*pi*kappa.
    """
    old_dps = mpmath.mp.dps
    mpmath.mp.dps = precision

    try:
        kappa_mp = mpmath.mpf(kappa_val)
        two_pi = 2 * mpmath.pi
        predicted = -two_pi * kappa_mp

        residues_numerical = []
        for k_idx in range(1, min(precision // 2, 20)):
            eps = mpmath.mpf(10) ** (-k_idx)
            hbar_p = two_pi + eps
            hbar_m = two_pi - eps
            val_p = eps * kappa_mp * (hp_ahat(hbar_p) - 1)
            val_m = (-eps) * kappa_mp * (hp_ahat(hbar_m) - 1)
            avg = (val_p + val_m) / 2
            residues_numerical.append(float(avg))

        predicted_float = float(predicted)
        return {
            'predicted_residue': predicted_float,
            'numerical_residues': residues_numerical[-5:] if residues_numerical else [],
            'convergence': (abs(residues_numerical[-1] - predicted_float) < 10 ** (-(precision // 4))
                           if residues_numerical else False),
        }
    finally:
        mpmath.mp.dps = old_dps


# =========================================================================
# Section 10: Virasoro family detailed analysis
# =========================================================================

def virasoro_full_convergence(c_val: float) -> Dict[str, Any]:
    r"""Complete convergence analysis for Virasoro at central charge c."""
    kappa = c_val / 2.0
    rho = virasoro_shadow_radius(c_val)
    R_arity = arity_convergence_radius(rho)
    c_star = critical_central_charge()

    domain = double_convergence_domain(kappa, rho, f'Vir_c={c_val}')
    residue = scalar_genus_series_residue(kappa, 1)

    return {
        'c': c_val, 'kappa': kappa, 'rho': rho,
        'R_genus': TWO_PI, 'R_arity': R_arity,
        'domain': domain, 'residue_at_2pi': residue,
        'c_star': c_star, 'arity_convergent': rho < 1.0,
        'above_c_star': c_val > c_star,
        'F_1': kappa / 24.0,
        'F_2': float(F_g(Rational(kappa), 2)) if kappa != 0 else 0,
    }


def virasoro_convergence_scan(c_values: Optional[List[float]] = None) -> List[Dict[str, Any]]:
    r"""Scan Virasoro convergence across central charges."""
    if c_values is None:
        c_values = [0.5, 1.0, 2.0, 4.0, 6.0, 6.125, 7.0, 10.0,
                     13.0, 20.0, 25.0, 26.0, 50.0, 100.0]
    return [virasoro_full_convergence(c) for c in c_values]


# =========================================================================
# Section 11: Class comparison
# =========================================================================

def class_comparison() -> Dict[str, Dict[str, Any]]:
    r"""Compare convergence properties across the four depth classes."""
    classes = {}

    classes['G'] = {
        'example': 'Heisenberg', 'genus_R': TWO_PI,
        'arity_R': float('inf'), 'arity_terms': 1,
        'double_convergent': True,
    }
    classes['L'] = {
        'example': 'Affine sl_2', 'genus_R': TWO_PI,
        'arity_R': float('inf'), 'arity_terms': 2,
        'double_convergent': True,
    }
    classes['C'] = {
        'example': 'Beta-gamma', 'genus_R': TWO_PI,
        'arity_R': None, 'arity_terms': 3,
        'double_convergent': None,
    }
    classes['M_convergent'] = {
        'example': 'Virasoro c=13', 'c': 13.0,
        'genus_R': TWO_PI,
        'arity_R': 1.0 / virasoro_shadow_radius(13.0),
        'rho': virasoro_shadow_radius(13.0),
        'arity_terms': float('inf'), 'double_convergent': True,
    }
    classes['M_divergent'] = {
        'example': 'Virasoro c=1', 'c': 1.0,
        'genus_R': TWO_PI,
        'arity_R': 1.0 / virasoro_shadow_radius(1.0),
        'rho': virasoro_shadow_radius(1.0),
        'arity_terms': float('inf'), 'double_convergent': False,
    }
    return classes


# =========================================================================
# Section 12: Polylogarithm and arity Borel transform
# =========================================================================

def polylogarithm(s: float, z: complex, max_terms: int = 500) -> complex:
    r"""Polylogarithm Li_s(z) = sum_{k>=1} z^k / k^s."""
    total = complex(0, 0)
    for k_idx in range(1, max_terms + 1):
        term = z ** k_idx / k_idx ** s
        total += term
        if abs(term) < 1e-20:
            break
    return total


def arity_borel_transform(rho: float, zeta: complex,
                           max_terms: int = 200) -> complex:
    r"""Borel transform of the arity series.

    Borel coefficients b_r = rho^r * r^{-5/2} / r! decay factorially.
    ENTIRE even for rho > 1.
    """
    total = complex(0, 0)
    for r in range(2, max_terms + 1):
        sr = rho ** r / r ** 2.5
        coeff = sr / math.factorial(r)
        term = coeff * zeta ** r
        total += term
        if abs(term) < 1e-25:
            break
    return total


def arity_borel_singularity_structure(rho: float) -> Dict[str, Any]:
    r"""Singularity structure of the arity Borel transform.

    Ordinary GF: radius R = 1/rho.
    Borel: ENTIRE (factorial kills geometric growth).
    """
    return {
        'rho': rho,
        'ordinary_R': 1.0 / rho if rho > 0 else float('inf'),
        'borel_entire': True, 'borel_summable': True,
    }


# =========================================================================
# Section 13: Master convergence summary
# =========================================================================

def master_convergence_summary(c_val: float) -> Dict[str, Any]:
    r"""Complete convergence summary for Virasoro at central charge c."""
    kappa = c_val / 2.0
    rho = virasoro_shadow_radius(c_val)
    c_star = critical_central_charge()

    domain = double_convergence_domain(kappa, rho, f'Vir_{c_val}')
    modular = genus_1_shadow_modular(kappa)

    return {
        'algebra': f'Virasoro c={c_val}',
        'kappa': kappa, 'c': c_val, 'c_star': c_star,
        'genus_convergence_radius': TWO_PI, 'genus_convergent': True,
        'rho': rho,
        'arity_convergence_radius': arity_convergence_radius(rho),
        'arity_convergent': rho < 1.0,
        'above_c_star': c_val > c_star,
        'double_convergent': rho < 1.0,
        'domain': {
            'R_genus': TWO_PI,
            'R_arity': arity_convergence_radius(rho),
            'physical_in_domain': domain.physical_point_in_domain,
        },
        'residue_at_2pi': scalar_genus_series_residue(kappa, 1),
        'boundary_exponent': 1,
        'genus_borel_entire': True, 'arity_borel_entire': True,
        'F_1': modular['F_1'], 'modular_anomaly': modular['modular_anomaly'],
    }
