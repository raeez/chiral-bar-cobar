r"""Scalar genus diagnostics for the shadow partition function.

This module works only in the scalar Faber--Pandharipande lane

    Z^sh_A(hbar) = sum_{g>=1} F_g(A) hbar^{2g},
    F_g(A) = kappa(A) lambda_g^FP.

Certified exact facts:

* ``lambda_g^FP`` is the Faber--Pandharipande number
  ``((2**(2*g-1)-1)/2**(2*g-1))*abs(B_{2*g})/(2*g)!``.
* The scalar generating function is
  ``kappa*((hbar/2)/sin(hbar/2) - 1)``.
* The scalar meromorphic continuation has simple poles at
  ``hbar = 2*pi*n`` with residue ``kappa*(-1)**n*2*pi*n``.
* The scalar power series has radius ``2*pi`` in ``hbar`` and
  ``(2*pi)**2`` in ``u = hbar**2``.

Certified negative fact:

* The factorial-divided Borel transforms implemented here are entire.
  The A-hat poles are singularities of the scalar closed form, not
  singularities detected from these Borel transforms.

Consequently, Stokes constants, median summation, trans-series sectors,
Peacock tables, and non-perturbative completions returned by this file
are diagnostics or analytic-resurgence hypotheses.  They are not
certificates of Borel summability, unique analytic continuation,
BTZ/JT recovery, all-genus Virasoro partition theorems, or
multiweight partition theorems.

Local sources:
    chapters/connections/concordance.tex:6473-6683
    chapters/connections/concordance.tex:10065-10074
    chapters/examples/landscape_census.tex:142-185, 834-881
    compute/lib/shadow_pf_convergence.py
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from functools import lru_cache
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    from scipy import integrate as scipy_integrate
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

# =====================================================================
# Constants
# =====================================================================

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2
FOUR_PI_SQ = (2.0 * PI) ** 2

CERTIFIED_EXACT = 'certified_exact'
FINITE_WINDOW_DIAGNOSTIC = 'finite_window_diagnostic'
ASYMPTOTIC_ESTIMATE = 'asymptotic_estimate'
BOREL_TRANSFORM_DIAGNOSTIC = 'borel_transform_entire_diagnostic'
ANALYTIC_RESURGENCE_HYPOTHESIS = 'analytic_resurgence_hypothesis'

KERNEL_NORMALIZATIONS = {
    # Local sources: CLAUDE.md:280-291; landscape_census.tex:180-185, 834-881.
    'affine_raw_collision': 'k*Omega_tr/z',
    'affine_KZ': 'Omega/((k+h_vee)z)',
    'heisenberg': 'k/z',
    'virasoro': '(c/2)/z^3 + 2T/z',
}

OBJECT_FIREWALLS = {
    'A': 'chiral algebra',
    'B(A)': 'bar coalgebra T^c(s^{-1}Abar)',
    'A^i': 'bar cohomology dual coalgebra H^*B(A)',
    'A^!': 'Verdier/continuous-linear dual algebra branch',
    'Z_ch^der(A)': 'derived centre/bulk Hochschild branch',
    'bar_cobar': 'Omega(B(A))=A is inversion, not Koszul duality',
}


# =====================================================================
# Section 0: Algebra data
# =====================================================================

@dataclass
class AlgebraData:
    """Algebra data for genus-direction resurgence analysis.

    kappa: modular characteristic kappa(A)
    name: human-readable identifier
    c: central charge (if applicable)
    family: 'Heisenberg', 'Virasoro', 'Affine', 'W3', etc.
    kappa_dual: scalar kappa on the Verdier/continuous-linear dual branch A!
    """
    name: str
    kappa: float
    family: str = ''
    c: float = 0.0
    kappa_dual: float = 0.0


def heisenberg_algebra(rank: int = 1, level: float = 1.0) -> AlgebraData:
    """Heisenberg at rank n, level k.

    kappa(H_k) = k for rank-1 Heisenberg at level k.
    For rank-n at level k: kappa = n * k (additive over rank,
    linear in level).  Central charge c = n (rank-independent of level).

    The scalar Verdier-dual branch has kappa = -n*k.
    """
    kappa = float(rank) * float(level)
    return AlgebraData(
        name=f'Heis_rank={rank}_level={level}',
        kappa=kappa,
        family='Heisenberg',
        c=float(rank),
        kappa_dual=-kappa,
    )


def virasoro_algebra(c_val: float) -> AlgebraData:
    """Virasoro at central charge c.

    kappa(Vir_c) = c/2.
    The scalar Verdier-dual branch has central charge 26-c, so
    kappa' = (26-c)/2.
    """
    kappa = c_val / 2.0
    kappa_dual = (26.0 - c_val) / 2.0
    return AlgebraData(
        name=f'Vir_c={c_val}',
        kappa=kappa,
        family='Virasoro',
        c=c_val,
        kappa_dual=kappa_dual,
    )


def affine_sl2_algebra(k: float) -> AlgebraData:
    """Affine sl_2 at level k.

    kappa = dim(g) * (k + h^v) / (2 h^v) = 3*(k+2)/4 for sl_2.
    The scalar dual-level branch uses k' = -k - 2h^v = -k - 4, hence
    kappa' = 3*(-k-4+2)/4 = -kappa.
    """
    kappa = 3.0 * (k + 2.0) / 4.0
    kappa_dual = -kappa
    return AlgebraData(
        name=f'aff_sl2_k={k}',
        kappa=kappa,
        family='Affine',
        c=3.0 * k / (k + 2.0) if abs(k + 2.0) > 1e-15 else float('nan'),
        kappa_dual=kappa_dual,
    )


# =====================================================================
# Section 1: Faber-Pandharipande coefficients and free energy
# =====================================================================

def _bernoulli_number(n: int) -> float:
    """Bernoulli number B_n (standard convention: B_1 = -1/2)."""
    # Use mpmath for reliability at high index
    try:
        import mpmath
        return float(mpmath.bernoulli(n))
    except ImportError:
        # Fallback to sympy
        from sympy import bernoulli as sym_bernoulli
        return float(sym_bernoulli(n))


@lru_cache(maxsize=None)
def bernoulli_number_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n with B_1 = -1/2."""
    if n < 0:
        raise ValueError("Bernoulli index must be nonnegative")
    values = [Fraction(1)]
    for m in range(1, n + 1):
        total = sum(Fraction(math.comb(m + 1, k)) * values[k]
                    for k in range(m))
        values.append(-total / Fraction(m + 1))
    return values[n]


@lru_cache(maxsize=None)
def lambda_fp_exact(g: int) -> Fraction:
    """Exact Faber--Pandharipande number lambda_g^FP."""
    if g < 1:
        return Fraction(0)
    prefac = Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
    return prefac * abs(bernoulli_number_exact(2 * g)) / math.factorial(2 * g)


def lambda_fp(g: int) -> float:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        return 0.0
    return float(lambda_fp_exact(g))


def F_g_scalar(kappa: float, g: int) -> float:
    """Genus-g scalar free energy: F_g(A) = kappa(A) * lambda_g^FP."""
    return kappa * lambda_fp(g)


def F_g_array(kappa: float, g_max: int) -> List[float]:
    """Array of F_g for g = 1, ..., g_max."""
    return [F_g_scalar(kappa, g) for g in range(1, g_max + 1)]


# =====================================================================
# Section 2: Borel transform of the genus series
# =====================================================================

def borel_transform_genus(kappa: float, zeta: complex,
                          g_max: int = 100) -> complex:
    r"""Factorial-divided diagnostic transform in the hbar variable.

    B[F](zeta) = sum_{g>=1} F_g * zeta^{2g-1} / Gamma(2g)

    where F_g = kappa * lambda_g^FP.

    Since lambda_g^FP has geometric, not factorial, growth, the
    additional Gamma(2g) divisor makes this transform entire.  It does
    not certify Borel singularities or Stokes jumps.

    Parameters
    ----------
    kappa : float
        Modular characteristic.
    zeta : complex
        Borel plane variable.
    g_max : int
        Maximum genus for summation.

    Returns
    -------
    complex
        B[F](zeta).
    """
    zeta = complex(zeta)
    result = 0.0 + 0.0j
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_2g = math.gamma(2 * g)  # = (2g-1)!
        term = Fg * zeta ** (2 * g - 1) / gamma_2g
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_coefficients_genus(kappa: float, g_max: int = 50
                             ) -> List[Tuple[int, float]]:
    r"""Borel transform coefficients for the genus series.

    Returns list of (2g-1, F_g / Gamma(2g)) pairs.
    """
    coeffs = []
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_2g = math.gamma(2 * g)
        coeffs.append((2 * g - 1, Fg / gamma_2g))
    return coeffs


def borel_transform_u_plane(kappa: float, xi: complex,
                            g_max: int = 100) -> complex:
    r"""Factorial-divided diagnostic transform in u = hbar^2.

    B_u[Z](xi) = sum_{g>=1} F_g * xi^{g-1} / Gamma(g)

    This entire transform is useful as a numerical diagnostic.  The
    poles at xi = (2*pi*n)^2 belong to the scalar closed form in the
    u-plane, not to this factorial-divided transform.
    """
    xi = complex(xi)
    result = 0.0 + 0.0j
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_g = math.gamma(g)  # = (g-1)!
        term = Fg * xi ** (g - 1) / gamma_g
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


# =====================================================================
# Section 3: Scalar poles and Borel diagnostics
# =====================================================================

def scalar_genus_radius_hbar() -> float:
    r"""Exact radius of the scalar genus series in hbar."""
    return TWO_PI


def scalar_genus_radius_u() -> float:
    r"""Exact radius of the scalar genus series in u = hbar^2."""
    return FOUR_PI_SQ

def borel_singularities_genus(n_max: int = 5) -> List[Dict[str, Any]]:
    r"""Poles of the scalar A-hat closed form.

    The closed form Z^sh = kappa * ((hbar/2)/sin(hbar/2) - 1) has
    poles at hbar = 2*pi*n (n = +/-1, +/-2, ...).

    This compatibility function keeps the historical name, but the
    returned points are scalar meromorphic singularities.  The
    factorial-divided Borel transforms in this module are entire.

    Returns list of singularity data.
    """
    sings = []
    for n in range(1, n_max + 1):
        A_n = 2.0 * PI * n
        sings.append({
            'n': n,
            'zeta_location': A_n,
            'u_location': A_n ** 2,
            'instanton_action_zeta': A_n,
            'instanton_action_u': A_n ** 2,
            'type': 'simple_pole',
            'residue_of_ahat': (-1) ** n * TWO_PI * n,
            'object': 'scalar_ahat_closed_form',
            'certification': CERTIFIED_EXACT,
            'borel_transform_singularity': False,
        })
    return sings


def borel_radius_genus() -> float:
    r"""Radius of the factorial-divided Borel transform.

    The transform is entire, so the radius is infinite.  Use
    scalar_genus_radius_hbar() for the exact 2*pi radius of the scalar
    A-hat power series.
    """
    return math.inf


def verify_borel_radius_from_coefficients(kappa: float, g_max: int = 50
                                          ) -> Dict[str, Any]:
    r"""Finite-window estimate for the scalar genus radius in u = hbar^2.

    The series Z(u) = sum_{g>=1} F_g u^g has coefficients F_g ~ 2*kappa / (4*pi^2)^g.
    The ratio |F_{g+1}/F_g| -> 1/(4*pi^2) as g -> infinity, confirming
    the convergence radius in u is R_u = 4*pi^2 = (2*pi)^2.

    Equivalently, the convergence radius in hbar is R_hbar = 2*pi.

    The BOREL transform coefficients b_g = F_g / (g-1)! decay as
    2*kappa / ((4*pi^2)^g * (g-1)!), which makes the Borel transform
    entire.  The scalar closed form still has poles at
    xi = (2*pi*n)^2 in the u-plane.
    """
    # Original series coefficients F_g
    Fg_values = []
    for g in range(1, g_max + 1):
        Fg_values.append(abs(F_g_scalar(kappa, g)))

    # Ratios of consecutive F_g
    ratios = []
    for i in range(1, len(Fg_values)):
        if Fg_values[i - 1] > 1e-100:
            ratios.append(Fg_values[i] / Fg_values[i - 1])

    # The ratio converges to 1/(4*pi^2) for nonzero kappa.
    predicted_ratio = 1.0 / FOUR_PI_SQ

    return {
        'predicted_u_radius': FOUR_PI_SQ,
        'predicted_hbar_radius': TWO_PI,
        'borel_transform_radius': math.inf,
        'predicted_ratio': predicted_ratio,
        'actual_ratios_last_5': ratios[-5:] if len(ratios) >= 5 else ratios,
        'converged': (len(ratios) >= 3 and
                      abs(ratios[-1] - predicted_ratio) / predicted_ratio < 0.05),
        'certification': FINITE_WINDOW_DIAGNOSTIC,
    }


# =====================================================================
# Section 4: Heisenberg exact Borel analysis
# =====================================================================

def heisenberg_borel_coefficients(kappa: float, g_max: int = 30
                                  ) -> List[Dict[str, float]]:
    r"""Borel transform coefficients for Heisenberg.

    F_g = kappa * B_{2g} * (2^{2g-1}-1) / (2^{2g-1} * (2g)!)

    Borel coefficient in zeta-plane:
        b_g = F_g / Gamma(2g) = F_g / (2g-1)!

    Using B_{2g} ~ (-1)^{g+1} 2(2g)! / (2*pi)^{2g}:
        F_g ~ 2*kappa / (2*pi)^{2g}  (leading order)
        b_g ~ 2*kappa / ((2*pi)^{2g} * (2g-1)!)
    """
    coeffs = []
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_2g = math.gamma(2 * g)
        bg = Fg / gamma_2g
        coeffs.append({
            'g': g,
            'F_g': Fg,
            'borel_coeff': bg,
            'zeta_power': 2 * g - 1,
        })
    return coeffs


def heisenberg_borel_singularity_structure(kappa: float) -> Dict[str, Any]:
    r"""Scalar A-hat pole structure for the Heisenberg genus series.

    Singularities at zeta = 2*pi*n (n = 1, 2, 3, ...) on the real axis.

    The closed form is Z = kappa * ((hbar/2)/sin(hbar/2) - 1).
    The function (hbar/2)/sin(hbar/2) has simple poles at hbar = 2*pi*n
    with residues (-1)^n * 2*pi*n.

    The factorial-divided Borel transform is entire; these are not
    certified Borel singularities.
    """
    sings = []
    for n in range(1, 6):
        sings.append({
            'n': n,
            'location': 2.0 * PI * n,
            'residue': kappa * (-1) ** n * 2.0 * PI * n,
            'type': 'simple_pole',
            'object': 'scalar_ahat_closed_form',
        })
    return {
        'kappa': kappa,
        'borel_radius': math.inf,
        'scalar_hbar_radius': TWO_PI,
        'singularities': sings,
        'n_singularities': 'infinite (one per integer n >= 1)',
        'certification': CERTIFIED_EXACT,
    }


# =====================================================================
# Section 5: Virasoro Borel analysis (genus direction)
# =====================================================================

def virasoro_borel_genus(c_val: float, zeta: complex,
                         g_max: int = 80) -> complex:
    r"""Borel transform of the Virasoro genus series at central charge c.

    B[F](zeta) = sum_{g>=1} F_g^{Vir}(c) * zeta^{2g-1} / Gamma(2g)

    At the scalar level: F_g^{Vir}(c) = (c/2) * lambda_g^FP.
    """
    kappa = c_val / 2.0
    return borel_transform_genus(kappa, zeta, g_max)


def virasoro_borel_scan(c_values: Optional[List[float]] = None,
                        zeta_values: Optional[List[complex]] = None,
                        g_max: int = 80) -> List[Dict[str, Any]]:
    r"""Scan the Virasoro Borel transform at multiple c and zeta values.

    Computes B[F](zeta) for each (c, zeta) pair and records:
    - The value B[F](zeta)
    - Whether the point lies inside the scalar A-hat disk
    - The transform's entire-function certification
    """
    if c_values is None:
        c_values = [0.5, 1.0, 6.0, 13.0, 25.0, 26.0]
    if zeta_values is None:
        zeta_values = [1.0, 3.0, 5.0, 6.0, 2.0 * PI - 0.1,
                       1.0j, 3.0j, 1.0 + 1.0j]

    results = []
    for c in c_values:
        kappa = c / 2.0
        for z in zeta_values:
            val = borel_transform_genus(kappa, z, g_max)
            dist_to_nearest = TWO_PI - abs(z) if abs(z) < TWO_PI else 0.0
            results.append({
                'c': c,
                'kappa': kappa,
                'zeta': z,
                'modulus_zeta': abs(z),
                'borel_value': val,
                'modulus_borel': abs(val),
                'within_radius': True,
                'within_scalar_genus_radius': abs(z) < TWO_PI,
                'dist_to_scalar_pole_radius': dist_to_nearest,
                'borel_certification': BOREL_TRANSFORM_DIAGNOSTIC,
            })
    return results


# =====================================================================
# Section 6: Formal residue multipliers (not Borel-certified Stokes data)
# =====================================================================

def stokes_multiplier_genus_n(kappa: float, n: int) -> complex:
    r"""Formal residue multiplier at the n-th scalar A-hat pole.

    Working in the u = hbar^2 plane, the function
    Z(u) = kappa * ((sqrt(u)/2)/sin(sqrt(u)/2) - 1) has simple poles
    at u_n = (2*pi*n)^2 with residues R_n = (-1)^n * 8*pi^2*n^2*kappa.

    The formal multiplier obtained from the u-plane residue is:

        S_n = 2*pi*i * R_n = 2*pi*i * (-1)^n * 8*pi^2*n^2 * kappa
            = (-1)^n * 16*pi^3*n^2 * kappa * i

    For the hbar-plane scalar pole residue this gives:

        S_n^{hbar} = 2*pi*i * Res_{hbar} = 2*pi*i * kappa * (-1)^n * 2*pi*n
                   = (-1)^n * 4*pi^2*n * kappa * i

    We return the hbar-plane residue convention.  This is not promoted
    to a certified Stokes constant because the factorial-divided Borel
    transforms implemented here are entire.
    """
    return kappa * (-1) ** n * FOUR_PI_SQ * n * 1.0j


def stokes_multiplier_genus_leading(kappa: float) -> complex:
    """Leading formal residue multiplier at hbar = 2*pi."""
    return stokes_multiplier_genus_n(kappa, 1)


def lateral_borel_sum_genus(kappa: float, hbar: complex,
                            epsilon: float = 0.02,
                            g_max: int = 80,
                            n_quad: int = 2000,
                            xi_max: float = 50.0) -> complex:
    r"""Numerical ray integral of the entire u-plane diagnostic transform.

    S_epsilon[Z](hbar) = int_0^{inf * e^{i*epsilon}} B[F](zeta) e^{-zeta/hbar} dzeta / hbar

    More precisely, working in the u = hbar^2 variable:

    S_epsilon[Z](u) = int_0^{inf * e^{i*epsilon}} B_u[Z](xi) e^{-xi/u} dxi / u

    We use the u-plane formulation for numerical stability.  Since
    B_u is entire in this scalar lane, this integral is a diagnostic
    and does not by itself certify Stokes jumps or Borel summability.
    """
    u = complex(hbar) ** 2
    if abs(u) < 1e-15:
        return 0.0 + 0.0j

    direction = cmath.exp(1j * epsilon)
    ds = xi_max / n_quad
    result = 0.0 + 0.0j

    for k in range(1, n_quad + 1):
        s = (k - 0.5) * ds
        xi = s * direction
        B_val = borel_transform_u_plane(kappa, xi, g_max)
        weight = cmath.exp(-xi / u) * direction / u
        result += B_val * weight * ds

    return result


def stokes_jump_genus(kappa: float, hbar: complex,
                      epsilon: float = 0.02,
                      g_max: int = 80,
                      n_quad: int = 2000,
                      xi_max: float = 50.0) -> Dict[str, Any]:
    r"""Compute the numerical ray-integral difference S_+ - S_-.

    Returns both ray integrals and their difference.  This is a finite
    numerical diagnostic, not a proof of a Stokes automorphism.
    """
    S_plus = lateral_borel_sum_genus(kappa, hbar, +epsilon, g_max, n_quad, xi_max)
    S_minus = lateral_borel_sum_genus(kappa, hbar, -epsilon, g_max, n_quad, xi_max)
    jump = S_plus - S_minus

    return {
        'kappa': kappa,
        'hbar': hbar,
        'S_plus': S_plus,
        'S_minus': S_minus,
        'stokes_jump': jump,
        'epsilon': epsilon,
        'certification': BOREL_TRANSFORM_DIAGNOSTIC,
    }


# =====================================================================
# Section 7: Trans-series (genus direction)
# =====================================================================

@dataclass
class GenusTransseries:
    """Diagnostic trans-series data for the scalar genus expansion.

    Z^full(hbar) = sum_{n>=0} sigma^n exp(-n * A / hbar^2) * Z^{(n)}(hbar)

    where A = (2*pi)^2 is the nearest scalar pole location in the
    u = hbar^2 plane.  These sectors are hypotheses, not certified
    non-perturbative completions.
    """
    kappa: float
    instanton_action: float  # A = (2*pi)^2
    perturbative: List[float]  # F_g^{(0)} = F_g
    one_instanton: List[float]  # F_g^{(1)}
    two_instanton: List[float]  # F_g^{(2)}
    three_instanton: List[float]  # F_g^{(3)}
    sigma: complex  # trans-series parameter
    certification: str = ANALYTIC_RESURGENCE_HYPOTHESIS


def build_genus_transseries(kappa: float, g_max: int = 30) -> GenusTransseries:
    r"""Build a diagnostic trans-series model for the genus expansion.

    The perturbative sector is Z^{(0)}(hbar) = sum_{g>=1} F_g hbar^{2g}.

    The one-instanton sector F_g^{(1)} is estimated from the nearest
    scalar pole at A = (2*pi)^2 in the u-plane.

    For the (hbar/2)/sin(hbar/2) closed form:
        Res at hbar = 2*pi gives F_g^{(1)} proportional to 1/(2*pi)^{2g}.
        The model one-instanton fluctuation sector is proportional to
        (2*pi)^{-2g}.

    More precisely, expanding around the pole hbar = 2*pi:
        (hbar/2)/sin(hbar/2) = -2*pi/(hbar - 2*pi) + regular

    The one-instanton sector is a model for the contribution from this
    pole.  The scalar data alone do not certify an analytic
    non-perturbative completion.
    """
    # Perturbative sector
    pert = F_g_array(kappa, g_max)

    # One-instanton sector (from the residue at hbar = 2*pi)
    # The residue of kappa * (hbar/2)/sin(hbar/2) at hbar = 2*pi is
    # kappa * (-1)^1 * 2*pi = -2*pi*kappa.
    # The one-instanton coefficients are the Taylor coefficients of
    # kappa * (-2*pi) / (hbar - 2*pi) = -2*pi*kappa / (hbar - 2*pi)
    # expanded around hbar = 0, contributing at order hbar^{2g}:
    # The g-th coefficient from the geometric series 1/(2*pi - hbar) = sum (hbar/2*pi)^n / (2*pi)
    # gives F_g^{(1)} = -kappa * (1/(2*pi))^{2g}
    # But more carefully: the residue contribution to F_g is
    # -Res * A^{-(2g)} where A = (2*pi)^2 (the u-plane instanton action).
    # So F_g^{(1)} = (-1) * (-2*pi*kappa) * ((2*pi)^2)^{-g} / ... (normalization)
    # From the formal large-order relation for the u = hbar^2 series:
    #   F_g ~ S_1/(2*pi*i) * A^{-g} * Gamma(g) * (1 + corrections)
    # where A = (2*pi)^2.  This gives the ONE-INSTANTON sector as
    #   F_g^{(1)} = 1 (constant, up to normalization).
    # The sigma parameter is S_1 = -4*pi^2*i * kappa.

    # For diagnostics, use the exact scalar pole locations:
    # Z(u) = kappa * (sqrt(u)/2)/sin(sqrt(u)/2) - kappa
    # Poles at u = (2*pi*n)^2.
    # Near u = (2*pi)^2: Z ~ -2*pi*kappa / (u - (2*pi)^2)^{1/2} * ...
    # Actually the pole of (hbar/2)/sin(hbar/2) at hbar = 2*pi is a SIMPLE pole,
    # so in u = hbar^2 it becomes a BRANCH POINT at u = (2*pi)^2.

    # For the trans-series model in hbar, F_g^{(1)} records the first
    # scalar pole contribution.
    # At leading order: F_g^{(1)} = (-1)^{g+1} * 2 * kappa / (2*pi)^{2g}
    # (from the Bernoulli large-order relation, matching the leading asymptotic).

    inst1 = []
    for g in range(1, g_max + 1):
        # The one-instanton coefficient from the n=1 pole
        # Using the large-order/dispersion relation structure
        fg1 = (-1) ** (g + 1) * 2.0 * kappa / TWO_PI ** (2 * g)
        inst1.append(fg1)

    # Two-instanton sector (from the n=2 pole)
    inst2 = []
    for g in range(1, g_max + 1):
        fg2 = (-1) ** g * 2.0 * kappa / (2.0 * TWO_PI) ** (2 * g)
        inst2.append(fg2)

    # Three-instanton sector (from the n=3 pole)
    inst3 = []
    for g in range(1, g_max + 1):
        fg3 = (-1) ** (g + 1) * 2.0 * kappa / (3.0 * TWO_PI) ** (2 * g)
        inst3.append(fg3)

    sigma = stokes_multiplier_genus_leading(kappa)

    return GenusTransseries(
        kappa=kappa,
        instanton_action=FOUR_PI_SQ,
        perturbative=pert,
        one_instanton=inst1,
        two_instanton=inst2,
        three_instanton=inst3,
        sigma=sigma,
        certification=ANALYTIC_RESURGENCE_HYPOTHESIS,
    )


def transseries_evaluate_genus(ts: GenusTransseries, hbar: complex,
                               n_inst: int = 1) -> complex:
    r"""Evaluate the diagnostic genus trans-series at hbar.

    Z^full(hbar) = Z^{(0)}(hbar) + sigma * exp(-A/hbar^2) * Z^{(1)}(hbar) + ...

    where A = (2*pi)^2, Z^{(0)} is the perturbative sum.
    """
    hbar = complex(hbar)
    if abs(hbar) < 1e-15:
        return 0.0 + 0.0j

    u = hbar ** 2

    # Perturbative sector
    Z0 = sum(ts.perturbative[g - 1] * hbar ** (2 * g)
             for g in range(1, len(ts.perturbative) + 1))

    result = Z0

    if n_inst >= 1 and ts.one_instanton:
        A = ts.instanton_action
        Z1 = sum(ts.one_instanton[g - 1] * hbar ** (2 * g)
                 for g in range(1, len(ts.one_instanton) + 1))
        result += ts.sigma * cmath.exp(-A / u) * Z1

    if n_inst >= 2 and ts.two_instanton:
        A2 = 4.0 * ts.instanton_action  # = (2*2*pi)^2 = 4*(2*pi)^2
        Z2 = sum(ts.two_instanton[g - 1] * hbar ** (2 * g)
                 for g in range(1, len(ts.two_instanton) + 1))
        result += ts.sigma ** 2 / 2.0 * cmath.exp(-A2 / u) * Z2

    return result


# =====================================================================
# Section 8: Median Borel summation
# =====================================================================

def ahat_at_imaginary(hbar: float) -> float:
    r"""A-hat(i*hbar) = (hbar/2)/sin(hbar/2).

    The closed form of the scalar genus series generating function.
    Poles at hbar = 2*pi*n.
    """
    if abs(hbar) < 1e-15:
        return 1.0
    return (hbar / 2.0) / math.sin(hbar / 2.0)


def genus_series_closed_form(kappa: float, hbar: float) -> float:
    r"""Exact scalar closed form inside the disk |hbar| < 2*pi."""
    return kappa * (ahat_at_imaginary(hbar) - 1.0)


def genus_series_partial_sum(kappa: float, hbar: float,
                             g_max: int = 50) -> float:
    r"""Partial sum of the genus series."""
    total = 0.0
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        total += Fg * hbar ** (2 * g)
    return total


def median_borel_sum_genus(kappa: float, hbar: float,
                           epsilon: float = 0.02,
                           g_max: int = 80,
                           n_quad: int = 2000,
                           xi_max: float = 50.0) -> Dict[str, Any]:
    r"""Median of two numerical ray integrals.

    F^med(hbar) = (1/2)(S_+(hbar) + S_-(hbar))

    where S_+/- are lateral Borel sums above/below the positive real axis.

    For real hbar > 0 inside the scalar convergence disk, the exact
    scalar value is supplied separately by the closed form.  The median
    below is a numerical diagnostic, not a physical-value certificate.

    Compare with:
    a. Pade approximants of the series
    b. Direct partial sum
    c. Exact closed form (where available)
    """
    hbar_c = complex(hbar)

    # Lateral sums
    S_plus = lateral_borel_sum_genus(kappa, hbar_c, +epsilon, g_max, n_quad, xi_max)
    S_minus = lateral_borel_sum_genus(kappa, hbar_c, -epsilon, g_max, n_quad, xi_max)
    median = (S_plus + S_minus) / 2.0

    # Partial sum
    partial = genus_series_partial_sum(kappa, hbar, g_max)

    # Exact (if available: |hbar| < 2*pi)
    exact = None
    if abs(hbar) < TWO_PI - 0.01:
        exact = genus_series_closed_form(kappa, hbar)

    # Pade approximant
    pade_val = pade_genus_series(kappa, hbar, g_max)

    return {
        'kappa': kappa,
        'hbar': hbar,
        'median_sum': median.real,
        'S_plus': S_plus,
        'S_minus': S_minus,
        'partial_sum': partial,
        'exact': exact,
        'pade': pade_val,
        'median_vs_exact': abs(median.real - exact) if exact is not None else None,
        'partial_vs_exact': abs(partial - exact) if exact is not None else None,
        'pade_vs_exact': abs(pade_val - exact) if exact is not None else None,
        'certification': BOREL_TRANSFORM_DIAGNOSTIC,
    }


def pade_genus_series(kappa: float, hbar: float, g_max: int = 30) -> float:
    r"""Pade approximant [N/N] of the genus series.

    Construct from the partial sums.
    """
    # Coefficients of the power series in u = hbar^2
    coeffs = [0.0]  # c_0 = 0 (no constant term in Z = sum F_g u^g)
    for g in range(1, g_max + 1):
        coeffs.append(F_g_scalar(kappa, g))

    n_coeffs = len(coeffs)
    N = (n_coeffs - 1) // 2

    if N < 1:
        return genus_series_partial_sum(kappa, hbar, g_max)

    # Build Pade [N/N] in u = hbar^2
    u = hbar ** 2

    # Set up the system for denominator coefficients q_1, ..., q_N
    # From: sum_{j=0}^N q_j c_{N+1+i-j} = 0, i = 0,...,N-1, q_0 = 1
    mat = np.zeros((N, N))
    rhs = np.zeros(N)
    for i in range(N):
        for j in range(N):
            idx = N + 1 + i - (j + 1)
            if 0 <= idx < len(coeffs):
                mat[i, j] = coeffs[idx]
        idx_r = N + 1 + i
        if 0 <= idx_r < len(coeffs):
            rhs[i] = -coeffs[idx_r]

    try:
        q_vec = np.linalg.solve(mat, rhs)
    except np.linalg.LinAlgError:
        return genus_series_partial_sum(kappa, hbar, g_max)

    Q_coeffs = np.concatenate(([1.0], q_vec))

    # Numerator: p_k = sum_{j=0}^{min(k,N)} q_j * c_{k-j}
    P_coeffs = np.zeros(N + 1)
    for k in range(N + 1):
        for j in range(min(k, N) + 1):
            if k - j < len(coeffs):
                P_coeffs[k] += Q_coeffs[j] * coeffs[k - j]

    # Evaluate P(u) / Q(u)
    P_val = sum(P_coeffs[k] * u ** k for k in range(len(P_coeffs)))
    Q_val = sum(Q_coeffs[k] * u ** k for k in range(len(Q_coeffs)))

    if abs(Q_val) < 1e-100:
        return genus_series_partial_sum(kappa, hbar, g_max)

    return float((P_val / Q_val).real) if isinstance(P_val / Q_val, complex) else float(P_val / Q_val)


# =====================================================================
# Section 9: Scalar pole coefficient asymptotics
# =====================================================================

def large_order_prediction(kappa: float, g: int, n_inst: int = 3) -> float:
    r"""Finite-pole asymptotic prediction for F_g.

    This computes the contribution of the first ``n_inst`` scalar A-hat
    poles to the coefficient of u^g in the meromorphic closed form.
    It is an asymptotic estimate, not a certified resurgence
    large-order theorem.

    The series in u = hbar^2 is Z(u) = sum_{g>=1} F_g u^g.
    From Z(u) = kappa * (sqrt(u)/2)/sin(sqrt(u)/2) - kappa, near u = xi_1 = (2*pi)^2:
        sqrt(u) ~ 2*pi + (u - xi_1)/(4*pi), so
        sin(sqrt(u)/2) ~ sin(pi + (u-xi_1)/(8*pi)) ~ -(u-xi_1)/(8*pi).
        (sqrt(u)/2)/sin(sqrt(u)/2) ~ pi / (-(u-xi_1)/(8*pi)) = -8*pi^2 / (u-xi_1).
    So Z(u) ~ -8*pi^2*kappa / (u - xi_1).

    If Z(u) has a simple pole at u = xi_1 with residue R, then
    Z(u) ~ R / (u - xi_1), and the Taylor coefficients are
    F_g = -R / xi_1^{g+1} (from geometric series 1/(xi_1 - u) = sum u^g / xi_1^{g+1}).
    Since Z(u) = sum F_g u^g, near the pole
    Z(u) ~ R/(u - xi_1) = -R/(xi_1 * (1 - u/xi_1)) = -(R/xi_1) * sum (u/xi_1)^g.
    So F_g ~ -R / xi_1^{g+1}.

    With R = -8*pi^2*kappa (from the computation above):
    F_g ~ 8*pi^2*kappa / xi_1^{g+1} = 8*pi^2*kappa / ((2*pi)^2)^{g+1}
        F_g ~ 8*pi^2*kappa / ((4*pi^2)^g * 4*pi^2) = 2*kappa / (4*pi^2)^g
            = 2*kappa / (2*pi)^{2g}.

    This matches the Bernoulli asymptotics.

    Including subleading poles at u = (2*pi*n)^2:
    F_g ~ sum_{n>=1} 2*kappa / (2*pi*n)^{2g}  (approximately, at large g)
        = 2*kappa * sum_{n>=1} 1/(2*pi*n)^{2g}
        = 2*kappa / (2*pi)^{2g} * sum_{n>=1} 1/n^{2g}
        = 2*kappa / (2*pi)^{2g} * zeta(2g)

    where zeta(2g) -> 1 as g -> infinity. At finite g:
    zeta(2) = pi^2/6, zeta(4) = pi^4/90, ...
    """
    # Asymptotic coefficient prediction including multiple scalar poles.
    #
    # Z(u) = kappa * ((sqrt(u)/2)/sin(sqrt(u)/2) - 1) has simple poles
    # at u_n = (2*pi*n)^2 for n = 1, 2, 3, ...
    #
    # Near u_n: sqrt(u)/2 ~ pi*n + (u-u_n)/(8*pi*n), so
    # sin(sqrt(u)/2) = (-1)^n * sin((u-u_n)/(8*pi*n)) ~ (-1)^n * (u-u_n)/(8*pi*n).
    # Thus (sqrt(u)/2)/sin(sqrt(u)/2) ~ pi*n / ((-1)^n * (u-u_n)/(8*pi*n))
    #     = (-1)^n * 8*pi^2*n^2 / (u-u_n).
    #
    # Residue: R_n = (-1)^n * 8*pi^2*n^2 * kappa.
    #
    # From 1/(u_n - u) = (1/u_n) * sum_{g>=0} (u/u_n)^g,
    # the contribution of the n-th pole to F_g is:
    #   -R_n / u_n^{g+1} = (-1)^{n+1} * 8*pi^2*n^2*kappa / u_n^{g+1}
    #   = (-1)^{n+1} * 8*pi^2*n^2*kappa / ((2*pi*n)^{2g+2})
    #   = (-1)^{n+1} * 2*kappa / ((2*pi)^{2g} * n^{2g})
    #
    result = 0.0
    for n in range(1, n_inst + 1):
        u_n = (TWO_PI * n) ** 2
        R_n = (-1) ** n * 8.0 * PI ** 2 * n ** 2 * kappa
        contrib = -R_n / u_n ** (g + 1)
        result += contrib
    return result


def large_order_verification(kappa: float, g_max: int = 20,
                             n_inst: int = 3) -> Dict[str, Any]:
    r"""Compare exact coefficients with the finite-pole asymptotic estimate.

    This is finite-window evidence for the Bernoulli/A-hat pole
    asymptotics, not a proof of a Stokes structure.
    """
    results = []
    for g in range(1, g_max + 1):
        Fg_exact = F_g_scalar(kappa, g)
        Fg_predicted = large_order_prediction(kappa, g, n_inst)
        rel_err = abs(Fg_exact - Fg_predicted) / abs(Fg_exact) if abs(Fg_exact) > 1e-100 else 0.0
        results.append({
            'g': g,
            'F_g_exact': Fg_exact,
            'F_g_predicted': Fg_predicted,
            'relative_error': rel_err,
        })

    # Check convergence of relative error to zero
    last_errors = [r['relative_error'] for r in results[-5:]]
    improving = all(last_errors[i] >= last_errors[i + 1] for i in range(len(last_errors) - 1)) if len(last_errors) > 1 else True

    return {
        'kappa': kappa,
        'n_instanton_sectors': n_inst,
        'g_max': g_max,
        'results': results,
        'last_5_errors': last_errors,
        'errors_decreasing': improving,
        'error_at_gmax': results[-1]['relative_error'] if results else None,
        'certification': FINITE_WINDOW_DIAGNOSTIC,
    }


# =====================================================================
# Section 10: Formal Peacock-table diagnostics
# =====================================================================

def peacock_stokes_constant(kappa: float, n: int, m: int) -> complex:
    r"""Formal Peacock-table entry S_{n,m}.

    For the A-hat generating function, the scalar closed form has only
    simple poles.  The factorized table below records the formal residue
    pattern one would use under an analytic-resurgence hypothesis:

        S_{n,m} = kappa * (-1)^{n-m} * 4*pi^2*(n-m) * i * C(n,m)

    where C(n,m) is a combinatorial prefactor.

    For the simple-pole residue model:
        S_{n,0} = S_n = kappa * (-1)^n * 4*pi^2*n * i

    The scalar coefficient data do not certify the Aniceto--Schiappa--
    Vonk Peacock structure.
    """
    if n <= m:
        return 0.0 + 0.0j  # only n > m transitions
    # For simple-pole structure, the Stokes constant is determined
    # by the pole at hbar = 2*pi*(n-m)
    return stokes_multiplier_genus_n(kappa, n - m)


def peacock_pattern_table(kappa: float, n_max: int = 5
                          ) -> Dict[Tuple[int, int], complex]:
    r"""Compute the formal Peacock residue table.

    Returns dict mapping (n, m) -> S_{n,m} for 0 <= m < n <= n_max.
    """
    table = {}
    for n in range(1, n_max + 1):
        for m in range(0, n):
            table[(n, m)] = peacock_stokes_constant(kappa, n, m)
    return table


def peacock_resurgence_triangle(kappa: float, n_max: int = 4
                                ) -> List[List[complex]]:
    r"""Formal residue triangle: rows n = 1, 2, ..., n_max.

    Row n has entries S_{n,0}, S_{n,1}, ..., S_{n,n-1}.
    This is a diagnostic analogue of the Aniceto--Schiappa--Vonk
    Peacock pattern, not a certified resurgence theorem.
    """
    triangle = []
    for n in range(1, n_max + 1):
        row = []
        for m in range(0, n):
            row.append(peacock_stokes_constant(kappa, n, m))
        triangle.append(row)
    return triangle


# =====================================================================
# Section 11: Verdier-branch complementarity diagnostics
# =====================================================================

def koszul_nonperturbative_genus(algebra: AlgebraData, hbar: float,
                                 g_max: int = 30) -> Dict[str, Any]:
    r"""Diagnostic non-perturbative ansatz using the A! scalar branch.

    A possible analytic-resurgence ansatz may involve the Verdier/
    continuous-linear dual branch A!:

    F^np(hbar) = F^pert(A, hbar) + exp(-A_inst/hbar^2) * F^pert(A!, hbar') + ...

    where A_inst = (2*pi)^2 and the dual-branch contribution uses
    kappa' = kappa(A!).

    This function does not identify A!, B(A), A^i, or the Hochschild
    bulk Z_ch^der(A).  It does not certify a non-perturbative
    completion.

    For general Virasoro, the scalar dual branch has
    kappa' = (26-c)/2.
    """
    kappa = algebra.kappa
    kappa_dual = algebra.kappa_dual

    # Perturbative sector
    Fpert = genus_series_partial_sum(kappa, hbar, g_max) if abs(hbar) < TWO_PI else float('nan')

    # One-instanton diagnostic sector using the Verdier dual branch.
    A_inst = FOUR_PI_SQ
    Fpert_dual = genus_series_partial_sum(kappa_dual, hbar, g_max) if abs(hbar) < TWO_PI else float('nan')

    # Leading non-perturbative diagnostic ansatz.
    u = hbar ** 2
    exp_factor = math.exp(-A_inst / u) if abs(u) > 1e-15 and A_inst / u < 500 else 0.0

    F_np = Fpert + exp_factor * Fpert_dual if not math.isnan(Fpert) and not math.isnan(Fpert_dual) else float('nan')

    # Exact (within convergence radius)
    exact = genus_series_closed_form(kappa, hbar) if abs(hbar) < TWO_PI - 0.01 else None

    # Is self-dual?
    is_self_dual = abs(kappa - kappa_dual) < 0.01

    return {
        'algebra': algebra.name,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'hbar': hbar,
        'F_perturbative': Fpert,
        'F_perturbative_dual': Fpert_dual,
        'instanton_action': A_inst,
        'exp_suppression': exp_factor,
        'F_nonperturbative': F_np,
        'F_nonperturbative_diagnostic': F_np,
        'exact': exact,
        'is_self_dual': is_self_dual,
        'dual_branch': 'A^! Verdier/continuous-linear dual branch',
        'certification': ANALYTIC_RESURGENCE_HYPOTHESIS,
        'object_firewall': OBJECT_FIREWALLS,
    }


def koszul_self_dual_check(c_val: float = 13.0, hbar: float = 1.0,
                           g_max: int = 30) -> Dict[str, Any]:
    r"""Check the scalar Verdier-branch fixed point c = 13.

    At c = 13: kappa = kappa' = 13/2, so the two scalar branches have
    identical perturbative coefficients.  This does not prove a
    trans-series symmetry.
    """
    alg = virasoro_algebra(c_val)
    result = koszul_nonperturbative_genus(alg, hbar, g_max)

    # Self-duality check
    result['kappa_equals_kappa_dual'] = abs(alg.kappa - alg.kappa_dual) < 1e-10
    result['symmetry'] = ('scalar branch fixed point'
                          if result['kappa_equals_kappa_dual']
                          else 'scalar branches distinct')

    return result


# =====================================================================
# Section 12: Optimal truncation
# =====================================================================

def optimal_truncation_genus(kappa: float, hbar: float) -> Dict[str, Any]:
    r"""Finite-window truncation diagnostic for the convergent genus series.

    The scalar genus series is convergent for |hbar| < 2*pi.  Thus the
    asymptotic formula N* = floor(A / hbar^2), A=(2*pi)^2, is only a
    diagnostic scale inherited from the nearest scalar pole; it is not
    an optimal truncation theorem.

    The returned minimum is computed only in the displayed finite
    window.
    """
    A = FOUR_PI_SQ
    u = hbar ** 2
    N_star = int(A / u) if u > 1e-15 else 1000

    # Cap at 80 for practical computation (beyond that, terms are negligible)
    N_eval = min(N_star, 80)

    # Compute partial sums at N_eval and nearby
    sums = {}
    exact = genus_series_closed_form(kappa, hbar) if abs(hbar) < TWO_PI - 0.01 else None
    for N in range(max(1, N_eval - 3), N_eval + 4):
        partial = genus_series_partial_sum(kappa, hbar, N)
        err = abs(partial - exact) if exact is not None else None
        sums[N] = {'partial_sum': partial, 'error': err}

    # Search for the minimum error in the displayed finite window.
    min_err_N = None
    min_err = float('inf')
    for N, data in sums.items():
        if data['error'] is not None and data['error'] < min_err:
            min_err = data['error']
            min_err_N = N

    return {
        'kappa': kappa,
        'hbar': hbar,
        'instanton_action': A,
        'N_star_predicted': N_star,
        'N_star_asymptotic_diagnostic': N_star,
        'N_star_actual': min_err_N,
        'min_error': min_err,
        'np_suppression': math.exp(-A / u) if u > 1e-15 else 0.0,
        'exact': exact,
        'sums': sums,
        'certification': FINITE_WINDOW_DIAGNOSTIC,
    }


# =====================================================================
# Section 13: Full pipeline analysis
# =====================================================================

def claim_certification_summary() -> Dict[str, str]:
    """Certification map for the scalar genus diagnostics in this file."""
    return {
        'scalar_ahat_closed_form': CERTIFIED_EXACT,
        'lambda_fp_bernoulli_coefficients': CERTIFIED_EXACT,
        'scalar_hbar_radius_2pi': CERTIFIED_EXACT,
        'scalar_u_radius_4pi2': CERTIFIED_EXACT,
        'borel_transform_entire': CERTIFIED_EXACT,
        'coefficient_ratio_radius': FINITE_WINDOW_DIAGNOSTIC,
        'finite_pole_asymptotics': ASYMPTOTIC_ESTIMATE,
        'formal_stokes_multipliers': ANALYTIC_RESURGENCE_HYPOTHESIS,
        'median_borel_summation': BOREL_TRANSFORM_DIAGNOSTIC,
        'transseries_sectors': ANALYTIC_RESURGENCE_HYPOTHESIS,
        'peacock_pattern': ANALYTIC_RESURGENCE_HYPOTHESIS,
        'nonperturbative_completion': ANALYTIC_RESURGENCE_HYPOTHESIS,
        'arity_radius': 'not_computed_here',
        'BTZ_JT_recovery': 'not_certified_here',
        'all_genus_multiweight_partition_theorem': 'not_certified_here',
    }


def full_resurgence_analysis(kappa: float, g_max: int = 30,
                             hbar_values: Optional[List[float]] = None
                             ) -> Dict[str, Any]:
    r"""Scalar genus diagnostic bundle.

    Combines all components:
    1. Entire Borel-transform diagnostic and scalar pole structure
    2. Formal residue multipliers
    3. Finite-pole coefficient asymptotics
    4. Truncation diagnostics
    5. Median ray-integral diagnostics
    6. Hypothetical trans-series sectors
    7. Formal Peacock table
    """
    if hbar_values is None:
        hbar_values = [0.5, 1.0, 2.0, 3.0]

    # 1. Borel structure
    borel_data = {
        'radius': borel_radius_genus(),
        'scalar_hbar_radius': scalar_genus_radius_hbar(),
        'scalar_u_radius': scalar_genus_radius_u(),
        'singularities': borel_singularities_genus(5),
        'ratio_test': verify_borel_radius_from_coefficients(kappa, g_max),
        'certification': BOREL_TRANSFORM_DIAGNOSTIC,
    }

    # 2. Stokes multipliers
    stokes_data = {
        'S_1': stokes_multiplier_genus_leading(kappa),
        'S_2': stokes_multiplier_genus_n(kappa, 2),
        'S_3': stokes_multiplier_genus_n(kappa, 3),
        'certification': ANALYTIC_RESURGENCE_HYPOTHESIS,
    }

    # 3. Large-order
    large_order = large_order_verification(kappa, g_max, n_inst=3)

    # 4. Optimal truncation at hbar = 1
    optimal = optimal_truncation_genus(kappa, 1.0)

    # 5. Trans-series
    ts = build_genus_transseries(kappa, g_max)

    # 6. Peacock pattern
    peacock = peacock_resurgence_triangle(kappa, 4)

    return {
        'kappa': kappa,
        'borel': borel_data,
        'stokes': stokes_data,
        'large_order': large_order,
        'optimal_truncation': optimal,
        'transseries': {
            'instanton_action': ts.instanton_action,
            'sigma': ts.sigma,
            'certification': ts.certification,
        },
        'peacock_triangle': [[complex(s) for s in row] for row in peacock],
        'certification_summary': claim_certification_summary(),
        'object_firewall': OBJECT_FIREWALLS,
        'kernel_normalizations': KERNEL_NORMALIZATIONS,
    }


# =====================================================================
# Section 14: Cross-family comparison
# =====================================================================

def family_comparison(g_max: int = 20) -> Dict[str, Dict[str, Any]]:
    r"""Compare scalar A-hat/Bernoulli diagnostics across families.

    In this scalar lane, the Faber--Pandharipande factor is universal
    and only kappa changes.  This is not an operator-level all-genus
    Virasoro theorem and not a multiweight partition theorem.
    """
    families = {
        'Heisenberg_rank1': {'kappa': 1.0, 'c': 1.0},
        'Heisenberg_rank2': {'kappa': 2.0, 'c': 2.0},
        'Virasoro_c=1': {'kappa': 0.5, 'c': 1.0},
        'Virasoro_c=13': {'kappa': 6.5, 'c': 13.0},
        'Virasoro_c=25': {'kappa': 12.5, 'c': 25.0},
        'Virasoro_c=26': {'kappa': 13.0, 'c': 26.0},
        'Affine_sl2_k1': {'kappa': 2.25, 'c': 1.0},
    }

    results = {}
    for name, data in families.items():
        kappa = data['kappa']
        lo = large_order_verification(kappa, g_max, n_inst=3)

        results[name] = {
            'kappa': kappa,
            'instanton_action': FOUR_PI_SQ,
            'S_1': stokes_multiplier_genus_leading(kappa),
            'borel_radius': borel_radius_genus(),
            'scalar_hbar_radius': scalar_genus_radius_hbar(),
            'scalar_u_radius': scalar_genus_radius_u(),
            'F_1': F_g_scalar(kappa, 1),
            'large_order_error_g20': lo['error_at_gmax'],
            'certification': FINITE_WINDOW_DIAGNOSTIC,
            'not_certified': [
                'all-genus Virasoro partition theorem',
                'multiweight partition theorem',
                'BTZ/JT recovery',
            ],
        }

    return results
