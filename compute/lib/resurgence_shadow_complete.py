r"""Complete resurgence analysis of the shadow partition function.

Extends the existing resurgence engines (resurgence_frontier_engine.py,
resurgence_stokes_engine.py) with the GENUS-DIRECTION resurgence of the
shadow partition function Z^sh(A, hbar) = sum_{g>=1} F_g(A) hbar^{2g}.

The existing engines analyze the ARITY-DIRECTION resurgence of the shadow
tower G(t) = sum_{r>=2} S_r t^r.  This module analyzes the complementary
direction: the genus expansion viewed as a formal power series in hbar.

MATHEMATICAL FRAMEWORK
======================

1. BOREL TRANSFORM (genus direction):

   The shadow partition function at the scalar level is

       Z^sh(hbar) = sum_{g>=1} F_g hbar^{2g}

   where F_g = kappa * lambda_g^FP.  The Borel transform in the variable
   u = hbar^2 is:

       B[Z](xi) = sum_{g>=1} F_g xi^{g-1} / Gamma(g)

   Equivalently, in the variable zeta = hbar (as specified in the task):

       B[F](zeta) = sum_{g>=1} F_g zeta^{2g-1} / Gamma(2g)

   For Heisenberg (F_g = kappa * B_{2g} / (2g(2g-2)!)):

       B_{2g} ~ (-1)^{g+1} 2(2g)! / (2pi)^{2g}

   so F_g ~ 2 kappa / (2pi)^{2g} and

       B[F](zeta) ~ kappa * sum 2/(2pi)^{2g} * zeta^{2g-1} / Gamma(2g)

   The Borel series has FINITE radius of convergence 2*pi in zeta,
   with singularities at zeta = +/- 2*pi*i*n (n = 1, 2, 3, ...).

2. BOREL SINGULARITIES:

   The closed form Z^sh = kappa * ((hbar/2)/sin(hbar/2) - 1) has poles
   at hbar = 2*pi*n.  The Borel transform B[Z](xi) in u = hbar^2 has
   singularities corresponding to these poles.  In the zeta = hbar plane,
   the singularities are at zeta = +/- 2*pi*n*i.

   Instanton actions: A_n = 2*pi*n  (for n = 1, 2, 3, ...).

3. STOKES AUTOMORPHISM:

   As arg(hbar) crosses a Stokes ray, the lateral Borel sums jump.
   The Stokes multiplier S_{2*pi*n} at the n-th singularity encodes
   the jump.  From the residue of (hbar/2)/sin(hbar/2) at hbar = 2*pi*n:

       Res = (-1)^n * 2*pi*n

   The Stokes multiplier is S_1 = 2*pi*i * Res = -4*pi^2*i (for n=1).

4. TRANS-SERIES:

   F^full(hbar) = sum_{n>=0} sigma^n exp(-n*A/hbar^2) * sum_g F_g^{(n)} hbar^{2g}

   where A = (2*pi)^2 is the instanton action (squared, since the series
   is in hbar^2).

5. MEDIAN SUMMATION:

   F^med(hbar) = (1/2)(S_+ + S_-) where S_+/- are lateral Borel sums.

6. LARGE-ORDER RELATIONS:

   F_g ~ sum_omega S_omega/(2*pi*i) * A_omega^{-2g} * Gamma(2g) * (1 + ...)

   For Heisenberg: Bernoulli asymptotics should match.

7. PEACOCK PATTERN (Aniceto-Schiappa-Vonk):

   Multi-instanton Stokes constants S_{n,m}.

8. NON-PERTURBATIVE FREE ENERGY from Koszul complementarity:

   F^np(hbar) = F^pert(A, hbar) + exp(-A_inst/hbar^2) * F^pert(A!, hbar') + ...

Manuscript references:
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
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
    kappa_dual: kappa(A!) for Koszul dual
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

    Koszul dual: H_k^! has kappa = -n*k (kappa + kappa' = 0 for
    Heisenberg, AP24 safe).
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
    Koszul dual: Vir_{26-c}, so kappa' = (26-c)/2.
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
    Koszul dual: k' = -k - 2h^v = -k - 4, kappa' = 3*(-k-4+2)/4 = 3*(-k-2)/4 = -kappa.
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


def lambda_fp(g: int) -> float:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.

    Uses mpmath for large g to avoid float overflow in (2g)!.
    """
    if g < 1:
        return 0.0
    try:
        import mpmath
        B2g = abs(mpmath.bernoulli(2 * g))
        prefac = (mpmath.mpf(2) ** (2 * g - 1) - 1) / mpmath.mpf(2) ** (2 * g - 1)
        return float(prefac * B2g / mpmath.factorial(2 * g))
    except ImportError:
        # Fallback: may overflow for large g
        B2g = abs(_bernoulli_number(2 * g))
        prefac = (2 ** (2 * g - 1) - 1) / (2 ** (2 * g - 1))
        return prefac * B2g / math.factorial(2 * g)


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
    r"""Borel transform of the shadow partition function (genus series).

    B[F](zeta) = sum_{g>=1} F_g * zeta^{2g-1} / Gamma(2g)

    where F_g = kappa * lambda_g^FP.

    The Gamma(2g) = (2g-1)! denominates the factorial growth of B_{2g},
    giving the Borel transform finite radius of convergence.

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
    r"""Borel transform in the u = hbar^2 variable.

    B_u[Z](xi) = sum_{g>=1} F_g * xi^{g-1} / Gamma(g)

    This is the natural Borel transform for a series in u = hbar^2.
    Singularities at xi = (2*pi*n)^2 = 4*pi^2*n^2.
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
# Section 3: Borel singularity analysis
# =====================================================================

def borel_singularities_genus(n_max: int = 5) -> List[Dict[str, Any]]:
    r"""Singularities of the Borel transform (genus direction).

    The closed form Z^sh = kappa * ((hbar/2)/sin(hbar/2) - 1) has
    poles at hbar = 2*pi*n (n = +/-1, +/-2, ...).

    In the Borel zeta-plane, these correspond to singularities at
    zeta = 2*pi*n (on the real axis), since the Borel transform
    inherits the pole structure of the resummed function.

    In the u-plane (u = hbar^2), singularities at u = (2*pi*n)^2.

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
        })
    return sings


def borel_radius_genus() -> float:
    r"""Radius of convergence of the Borel transform (genus direction).

    The Borel transform B[F](zeta) has singularities at zeta = 2*pi*n.
    The radius of convergence is the distance to the nearest singularity:
    R_Borel = 2*pi.

    In the u-plane: R_Borel = (2*pi)^2 = 4*pi^2.
    """
    return TWO_PI


def verify_borel_radius_from_coefficients(kappa: float, g_max: int = 50
                                          ) -> Dict[str, Any]:
    r"""Verify the convergence radius of the ORIGINAL genus series in u = hbar^2.

    The series Z(u) = sum_{g>=1} F_g u^g has coefficients F_g ~ 2*kappa / (4*pi^2)^g.
    The ratio |F_{g+1}/F_g| -> 1/(4*pi^2) as g -> infinity, confirming
    the convergence radius in u is R_u = 4*pi^2 = (2*pi)^2.

    Equivalently, the convergence radius in hbar is R_hbar = 2*pi.

    The BOREL transform coefficients b_g = F_g / (g-1)! decay as
    2*kappa / ((4*pi^2)^g * (g-1)!), which makes the Borel transform
    entire.  But the singularities of the Borel-resummed function
    still occur at xi = (2*pi*n)^2 in the u-plane.
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

    # The ratio should converge to 1/(4*pi^2)
    predicted_ratio = 1.0 / FOUR_PI_SQ

    return {
        'predicted_u_radius': FOUR_PI_SQ,
        'predicted_ratio': predicted_ratio,
        'actual_ratios_last_5': ratios[-5:] if len(ratios) >= 5 else ratios,
        'converged': (len(ratios) >= 3 and
                      abs(ratios[-1] - predicted_ratio) / predicted_ratio < 0.05),
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
    r"""Singularity structure of the Heisenberg genus Borel transform.

    Singularities at zeta = 2*pi*n (n = 1, 2, 3, ...) on the real axis.

    The closed form is Z = kappa * ((hbar/2)/sin(hbar/2) - 1).
    The function (hbar/2)/sin(hbar/2) has simple poles at hbar = 2*pi*n
    with residues (-1)^n * 2*pi*n.

    In the Borel plane, these appear as singularities of the Borel
    transform at zeta = 2*pi*n.
    """
    sings = []
    for n in range(1, 6):
        sings.append({
            'n': n,
            'location': 2.0 * PI * n,
            'residue': kappa * (-1) ** n * 2.0 * PI * n,
            'type': 'simple_pole',
        })
    return {
        'kappa': kappa,
        'borel_radius': TWO_PI,
        'singularities': sings,
        'n_singularities': 'infinite (one per integer n >= 1)',
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
    - Distance to nearest singularity
    - Whether convergent (|zeta| < 2*pi)
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
                'within_radius': abs(z) < TWO_PI,
                'dist_to_singularity': dist_to_nearest,
            })
    return results


# =====================================================================
# Section 6: Stokes automorphism (genus direction)
# =====================================================================

def stokes_multiplier_genus_n(kappa: float, n: int) -> complex:
    r"""Stokes multiplier at the n-th singularity (genus direction).

    Working in the u = hbar^2 plane, the function
    Z(u) = kappa * ((sqrt(u)/2)/sin(sqrt(u)/2) - 1) has simple poles
    at u_n = (2*pi*n)^2 with residues R_n = (-1)^n * 8*pi^2*n^2*kappa.

    The Stokes multiplier (in the u-plane Borel) is:

        S_n = 2*pi*i * R_n = 2*pi*i * (-1)^n * 8*pi^2*n^2 * kappa
            = (-1)^n * 16*pi^3*n^2 * kappa * i

    For the Borel transform in the hbar variable (with singularities at
    hbar = 2*pi*n), the Stokes multiplier is:

        S_n^{hbar} = 2*pi*i * Res_{hbar} = 2*pi*i * kappa * (-1)^n * 2*pi*n
                   = (-1)^n * 4*pi^2*n * kappa * i

    We use the hbar-plane convention.
    """
    return kappa * (-1) ** n * FOUR_PI_SQ * n * 1.0j


def stokes_multiplier_genus_leading(kappa: float) -> complex:
    """Leading Stokes multiplier S_1 at zeta = 2*pi."""
    return stokes_multiplier_genus_n(kappa, 1)


def lateral_borel_sum_genus(kappa: float, hbar: complex,
                            epsilon: float = 0.02,
                            g_max: int = 80,
                            n_quad: int = 2000,
                            xi_max: float = 50.0) -> complex:
    r"""Lateral Borel sum of the genus series.

    S_epsilon[Z](hbar) = int_0^{inf * e^{i*epsilon}} B[F](zeta) e^{-zeta/hbar} dzeta / hbar

    More precisely, working in the u = hbar^2 variable:

    S_epsilon[Z](u) = int_0^{inf * e^{i*epsilon}} B_u[Z](xi) e^{-xi/u} dxi / u

    We use the u-plane formulation for numerical stability.
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
    r"""Compute the Stokes jump S_+ - S_- for the genus series.

    Returns both lateral sums and their difference.
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
    }


# =====================================================================
# Section 7: Trans-series (genus direction)
# =====================================================================

@dataclass
class GenusTransseries:
    """Trans-series data for the genus expansion.

    Z^full(hbar) = sum_{n>=0} sigma^n exp(-n * A / hbar^2) * Z^{(n)}(hbar)

    where A = (2*pi)^2 is the instanton action in the u = hbar^2 plane.
    """
    kappa: float
    instanton_action: float  # A = (2*pi)^2
    perturbative: List[float]  # F_g^{(0)} = F_g
    one_instanton: List[float]  # F_g^{(1)}
    two_instanton: List[float]  # F_g^{(2)}
    three_instanton: List[float]  # F_g^{(3)}
    sigma: complex  # trans-series parameter


def build_genus_transseries(kappa: float, g_max: int = 30) -> GenusTransseries:
    r"""Build the trans-series for the genus expansion.

    The perturbative sector is Z^{(0)}(hbar) = sum_{g>=1} F_g hbar^{2g}.

    The one-instanton sector F_g^{(1)} is determined by the large-order
    relation:

        F_g ~ S_1/(2*pi*i) * A^{-2g} * Gamma(2g) * (1 + c_1/(2g) + ...)

    where A = (2*pi)^2, and S_1 is the leading Stokes multiplier.
    Inverting: F_g^{(1)} ~ constant (from the residue structure).

    For the (hbar/2)/sin(hbar/2) closed form:
        Res at hbar = 2*pi gives F_g^{(1)} proportional to 1/(2*pi)^{2g}.
        The one-instanton fluctuation sector is:
        F_g^{(1)} = kappa * (-1) * 2*pi / ((2*pi)^{2g} * (2g-1)!)

    More precisely, expanding around the pole hbar = 2*pi:
        (hbar/2)/sin(hbar/2) = -2*pi/(hbar - 2*pi) + regular

    The one-instanton sector captures the contribution from this pole.
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
    # Let me compute from the large-order relation directly.

    # From the large-order relation for the u = hbar^2 series:
    #   F_g ~ S_1/(2*pi*i) * A^{-g} * Gamma(g) * (1 + corrections)
    # where A = (2*pi)^2.  This gives the ONE-INSTANTON sector as
    #   F_g^{(1)} = 1 (constant, up to normalization).
    # The sigma parameter is S_1 = -4*pi^2*i * kappa.

    # For computational purposes, use the exact structure:
    # Z(u) = kappa * (sqrt(u)/2)/sin(sqrt(u)/2) - kappa
    # Poles at u = (2*pi*n)^2.
    # Near u = (2*pi)^2: Z ~ -2*pi*kappa / (u - (2*pi)^2)^{1/2} * ...
    # Actually the pole of (hbar/2)/sin(hbar/2) at hbar = 2*pi is a SIMPLE pole,
    # so in u = hbar^2 it becomes a BRANCH POINT at u = (2*pi)^2.

    # For the trans-series in hbar, the instanton sector is simpler:
    # F_g^{(1)} captures the correction from the first pole.
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
    )


def transseries_evaluate_genus(ts: GenusTransseries, hbar: complex,
                               n_inst: int = 1) -> complex:
    r"""Evaluate the genus trans-series at hbar.

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
    r"""Exact closed form: Z^sh = kappa * ((hbar/2)/sin(hbar/2) - 1)."""
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
    r"""Median Borel sum of the genus series.

    F^med(hbar) = (1/2)(S_+(hbar) + S_-(hbar))

    where S_+/- are lateral Borel sums above/below the positive real axis.

    For real hbar > 0 within the convergence radius, this gives the
    physical value.

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
# Section 9: Large-order resurgent relations
# =====================================================================

def large_order_prediction(kappa: float, g: int, n_inst: int = 3) -> float:
    r"""Resurgent large-order prediction for F_g.

    F_g ~ sum_{n=1}^{n_inst} S_n/(2*pi*i) * A_n^{-2g} * Gamma(2g) * (1 + ...)

    where A_n = (2*pi*n)^2 (instanton actions in the u-plane)
    and S_n is the Stokes multiplier at the n-th singularity.

    The leading term (n=1):
        F_g ~ S_1/(2*pi*i) * A_1^{-g} * Gamma(g)

    in the u-plane, where A_1 = (2*pi)^2, S_1 = -4*pi^2*i*kappa.

    So F_g ~ (-4*pi^2*i*kappa)/(2*pi*i) * ((2*pi)^2)^{-g} * (g-1)!
           = 2*kappa / (2*pi)^{2g} * (g-1)!/(g-1)!
           Hmm, let me be more careful.

    The series in u = hbar^2 is Z(u) = sum_{g>=1} F_g u^g.
    The Borel transform in u is B(xi) = sum F_g xi^{g-1}/(g-1)!.
    Singularity of B at xi_1 = (2*pi)^2 with residue related to Res_{hbar=2*pi}.

    Large-order from the u-plane Borel:
        F_g / (g-1)! ~ R_1 / xi_1^g  as g -> infty
    where R_1 is the residue of B at xi_1.

    So F_g ~ R_1 * (g-1)! / xi_1^g.

    Now R_1 = lim_{xi->xi_1} (xi-xi_1) * B(xi).
    From Z(u) = kappa * (sqrt(u)/2)/sin(sqrt(u)/2) - kappa, near u = xi_1 = (2*pi)^2:
        sqrt(u) ~ 2*pi + (u - xi_1)/(4*pi), so
        sin(sqrt(u)/2) ~ sin(pi + (u-xi_1)/(8*pi)) ~ -(u-xi_1)/(8*pi).
        (sqrt(u)/2)/sin(sqrt(u)/2) ~ pi / (-(u-xi_1)/(8*pi)) = -8*pi^2 / (u-xi_1).
    So Z(u) ~ -8*pi^2*kappa / (u - xi_1).
    This gives R_1 (residue of B) = -8*pi^2*kappa / ((g-1)! contribution is already factored out)...

    Actually more carefully: if Z(u) has a simple pole at u = xi_1 with residue R,
    then Z(u) ~ R / (u - xi_1), and the Taylor coefficients are
    F_g = -R / xi_1^{g+1} (from geometric series 1/(xi_1 - u) = sum u^g / xi_1^{g+1}).
    Wait: Z(u) = sum F_g u^g, and near the pole,
    Z(u) ~ R/(u - xi_1) = -R/(xi_1 * (1 - u/xi_1)) = -(R/xi_1) * sum (u/xi_1)^g.
    So F_g ~ -R / xi_1^{g+1}.

    With R = -8*pi^2*kappa (from the computation above):
    F_g ~ 8*pi^2*kappa / xi_1^{g+1} = 8*pi^2*kappa / ((2*pi)^2)^{g+1}
        = 8*pi^2*kappa / (4*pi^2)^{g+1} = 2*kappa / (4*pi^2)^g / (4*pi^2)
        Wait, (4*pi^2)^{g+1} = (4*pi^2)^g * 4*pi^2, so
        F_g ~ 8*pi^2*kappa / ((4*pi^2)^g * 4*pi^2) = 2*kappa / (4*pi^2)^g
            = 2*kappa / (2*pi)^{2g}.

    This matches the Bernoulli asymptotics! (As it must.)

    Including subleading poles at u = (2*pi*n)^2:
    F_g ~ sum_{n>=1} 2*kappa / (2*pi*n)^{2g}  (approximately, at large g)
        = 2*kappa * sum_{n>=1} 1/(2*pi*n)^{2g}
        = 2*kappa / (2*pi)^{2g} * sum_{n>=1} 1/n^{2g}
        = 2*kappa / (2*pi)^{2g} * zeta(2g)

    where zeta(2g) -> 1 as g -> infinity. At finite g:
    zeta(2) = pi^2/6, zeta(4) = pi^4/90, ...
    """
    # Large-order prediction including multiple instanton contributions.
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
    r"""Verify the resurgent large-order relation for F_g.

    Compare exact F_g with the large-order prediction from the instanton
    data. For Heisenberg, the Bernoulli asymptotics should match perfectly.
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
    }


# =====================================================================
# Section 10: Peacock pattern (multi-instanton Stokes constants)
# =====================================================================

def peacock_stokes_constant(kappa: float, n: int, m: int) -> complex:
    r"""Peacock pattern Stokes constant S_{n,m}.

    In the Aniceto-Schiappa-Vonk framework, the Stokes constants organize
    into a "peacock" pattern. For the shadow partition function with
    singularities at integer multiples of 2*pi:

    S_{n,m} encodes the Stokes phenomenon between the n-th and m-th
    instanton sectors (m = 0 is perturbative).

    For the genus series with simple-pole singularities:
        S_{n,0} = S_n (standard Stokes multiplier at n-th singularity)
        S_{n,m} = S_{n-m} * (binomial correction)  for the resurgence triangle

    The exact structure for the A-hat generating function:
    Since (hbar/2)/sin(hbar/2) has only SIMPLE poles, the resurgence
    structure is "simple" in the sense that all multi-instanton Stokes
    constants factorize:

        S_{n,m} = kappa * (-1)^{n-m} * 4*pi^2*(n-m) * i * C(n,m)

    where C(n,m) is a combinatorial prefactor.

    For the simplest case (simple-pole asymptotics):
        S_{n,0} = S_n = kappa * (-1)^n * 4*pi^2*n * i
    """
    if n <= m:
        return 0.0 + 0.0j  # only n > m transitions
    # For simple-pole structure, the Stokes constant is determined
    # by the pole at hbar = 2*pi*(n-m)
    return stokes_multiplier_genus_n(kappa, n - m)


def peacock_pattern_table(kappa: float, n_max: int = 5
                          ) -> Dict[Tuple[int, int], complex]:
    r"""Compute the peacock pattern table of Stokes constants.

    Returns dict mapping (n, m) -> S_{n,m} for 0 <= m < n <= n_max.
    """
    table = {}
    for n in range(1, n_max + 1):
        for m in range(0, n):
            table[(n, m)] = peacock_stokes_constant(kappa, n, m)
    return table


def peacock_resurgence_triangle(kappa: float, n_max: int = 4
                                ) -> List[List[complex]]:
    r"""Resurgence triangle: rows n = 1, 2, ..., n_max.

    Row n has entries S_{n,0}, S_{n,1}, ..., S_{n,n-1}.
    This is the shadow partition function's analogue of the
    Aniceto-Schiappa-Vonk peacock pattern.
    """
    triangle = []
    for n in range(1, n_max + 1):
        row = []
        for m in range(0, n):
            row.append(peacock_stokes_constant(kappa, n, m))
        triangle.append(row)
    return triangle


# =====================================================================
# Section 11: Koszul complementarity and non-perturbative structure
# =====================================================================

def koszul_nonperturbative_genus(algebra: AlgebraData, hbar: float,
                                 g_max: int = 30) -> Dict[str, Any]:
    r"""Non-perturbative free energy from Koszul complementarity.

    The non-perturbative completion should involve the Koszul dual A!:

    F^np(hbar) = F^pert(A, hbar) + exp(-A_inst/hbar^2) * F^pert(A!, hbar') + ...

    where A_inst = (2*pi)^2 and the Koszul dual contribution uses
    kappa' = kappa(A!).

    For Virasoro at c = 13 (self-dual: A! = A, kappa' = kappa):
    the instanton is its own dual, giving enhanced symmetry.

    For general Virasoro: kappa' = (26-c)/2, so the non-perturbative
    sector uses the dual central charge.
    """
    kappa = algebra.kappa
    kappa_dual = algebra.kappa_dual

    # Perturbative sector
    Fpert = genus_series_partial_sum(kappa, hbar, g_max) if abs(hbar) < TWO_PI else float('nan')

    # One-instanton sector (using the Koszul dual)
    A_inst = FOUR_PI_SQ
    Fpert_dual = genus_series_partial_sum(kappa_dual, hbar, g_max) if abs(hbar) < TWO_PI else float('nan')

    # Full non-perturbative (leading order)
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
        'exact': exact,
        'is_self_dual': is_self_dual,
    }


def koszul_self_dual_check(c_val: float = 13.0, hbar: float = 1.0,
                           g_max: int = 30) -> Dict[str, Any]:
    r"""Verify enhanced symmetry at the self-dual point c = 13.

    At c = 13: kappa = kappa' = 13/2, so the perturbative and dual
    sectors are identical. The trans-series has Z_2 symmetry:
    the n-th instanton sector equals the (-n)-th sector.
    """
    alg = virasoro_algebra(c_val)
    result = koszul_nonperturbative_genus(alg, hbar, g_max)

    # Self-duality check
    result['kappa_equals_kappa_dual'] = abs(alg.kappa - alg.kappa_dual) < 1e-10
    result['symmetry'] = 'Z_2 enhanced' if result['kappa_equals_kappa_dual'] else 'broken'

    return result


# =====================================================================
# Section 12: Optimal truncation
# =====================================================================

def optimal_truncation_genus(kappa: float, hbar: float) -> Dict[str, Any]:
    r"""Optimal truncation of the genus series.

    The optimal number of terms is N* = floor(A / hbar^2) where
    A = (2*pi)^2 is the nearest instanton action in the u-plane.

    At optimal truncation, the remainder is of order exp(-A/hbar^2),
    which is the leading non-perturbative contribution.
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

    # The minimum error should be near N_eval
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
        'N_star_actual': min_err_N,
        'min_error': min_err,
        'np_suppression': math.exp(-A / u) if u > 1e-15 else 0.0,
        'exact': exact,
        'sums': sums,
    }


# =====================================================================
# Section 13: Full pipeline analysis
# =====================================================================

def full_resurgence_analysis(kappa: float, g_max: int = 30,
                             hbar_values: Optional[List[float]] = None
                             ) -> Dict[str, Any]:
    r"""Complete resurgence analysis of the genus series.

    Combines all components:
    1. Borel transform and singularity structure
    2. Stokes multipliers
    3. Large-order verification
    4. Optimal truncation
    5. Median summation
    6. Trans-series
    7. Peacock pattern
    """
    if hbar_values is None:
        hbar_values = [0.5, 1.0, 2.0, 3.0]

    # 1. Borel structure
    borel_data = {
        'radius': borel_radius_genus(),
        'singularities': borel_singularities_genus(5),
        'ratio_test': verify_borel_radius_from_coefficients(kappa, g_max),
    }

    # 2. Stokes multipliers
    stokes_data = {
        'S_1': stokes_multiplier_genus_leading(kappa),
        'S_2': stokes_multiplier_genus_n(kappa, 2),
        'S_3': stokes_multiplier_genus_n(kappa, 3),
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
        },
        'peacock_triangle': [[complex(s) for s in row] for row in peacock],
    }


# =====================================================================
# Section 14: Cross-family comparison
# =====================================================================

def family_comparison(g_max: int = 20) -> Dict[str, Dict[str, Any]]:
    r"""Compare resurgence properties across algebra families.

    All families share the SAME genus-direction resurgence structure
    (singularities at (2*pi*n)^2 in the u-plane) because the
    Bernoulli/A-hat generating function is universal. Only kappa changes.
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
            'F_1': F_g_scalar(kappa, 1),
            'large_order_error_g20': lo['error_at_gmax'],
        }

    return results
