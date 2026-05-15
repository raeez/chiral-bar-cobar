r"""Finite-window Virasoro genus coefficients for 3d-gravity diagnostics.

This module computes the scalar Faber-Pandharipande lane and the
currently available Virasoro planted-forest corrections.  It does not
construct the full all-genus 3d gravity partition function.

Exact scalar lane
=================

For g >= 1 the scalar coefficient is

    F_g^{scalar}(Vir_c) = kappa(Vir_c) * lambda_g^{FP},
    kappa(Vir_c) = c/2,
    lambda_g^{FP} = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!.

The ordinary scalar generating function is

    sum_{g >= 1} F_g^{scalar} * hbar^{2g}
        = kappa * ((hbar/2)/sin(hbar/2) - 1),

with scalar-lane radius |hbar| = 2*pi.  This radius is a theorem about
that ordinary scalar power series, not about the full Virasoro
planted-forest series and not about a Borel transform.

Known planted-forest window
===========================

For Virasoro the planted-forest correction is included where the local
canonical engine supplies it:

    g = 1: scalar value, no planted-forest correction;
    g = 2: scalar + delta_pf^{(2,0)};
    g = 3: scalar + delta_pf^{(3,0)};
    g >= 4: scalar component only in this module.

The g >= 4 return values are therefore finite-window scalar components,
not proved full Virasoro coefficients.

Analytic firewall
=================

The Bernoulli scalar coefficients satisfy

    lambda_g^{FP} ~ 2/(2*pi)^{2g},
    |F_{g+1}/F_g| -> 1/(4*pi^2).

This is geometric decay (Gevrey 0).  No Borel summability, all-genus
analytic summation of the full planted-forest series, or BTZ closed
form is asserted here.  The BTZ routine below is only the Cardy /
Bekenstein-Hawking entropy formula

    S_BTZ = 2*pi*sqrt(c*E/6).

Local sources:
  compute/lib/btz_entropy_allgenus.py
  chapters/examples/genus_expansions.tex
  chapters/examples/landscape_census.tex
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List

from sympy import bernoulli, factorial, Rational

# ---------------------------------------------------------------------------
# Import canonical building blocks from btz_entropy_allgenus
# ---------------------------------------------------------------------------

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from btz_entropy_allgenus import (
    lambda_fp,
    lambda_fp_float,
    kappa_virasoro,
    F1_virasoro,
    F2_full,
    F3_full,
)

PI = math.pi
TWO_PI = 2 * PI
FOUR_PI_SQ = 4 * PI ** 2
SCALAR_RADIUS_SCOPE = "scalar ordinary generating function"
SCALAR_GEVREY_CLASS = 0


def scalar_convergence_radius_exact() -> float:
    r"""Exact radius of the scalar ordinary generating function.

    The identity

        sum_{g>=1} lambda_g^{FP} x^{2g} = (x/2)/sin(x/2) - 1

    has first singularities at x = +/- 2*pi.  This is not a statement
    about the full planted-forest Virasoro partition function.
    """
    return TWO_PI


def virasoro_coefficient_scope(g: int) -> Dict[str, Any]:
    r"""Scope of the Virasoro coefficient returned by this module."""
    if g < 0:
        raise ValueError(f"genus must be non-negative, got {g}")
    if g == 0:
        return {
            "genus": g,
            "coefficient": "regularized zero",
            "includes_planted_forest": False,
            "full_virasoro_value_known_here": False,
        }
    if g == 1:
        return {
            "genus": g,
            "coefficient": "scalar exact",
            "includes_planted_forest": False,
            "full_virasoro_value_known_here": True,
        }
    if g in (2, 3):
        return {
            "genus": g,
            "coefficient": "scalar plus computed planted-forest correction",
            "includes_planted_forest": True,
            "full_virasoro_value_known_here": True,
        }
    return {
        "genus": g,
        "coefficient": "scalar component only; planted-forest correction not computed here",
        "includes_planted_forest": False,
        "full_virasoro_value_known_here": False,
    }


# =========================================================================
# Section 1: Exact Bernoulli numbers (independent path for cross-check)
# =========================================================================

@lru_cache(maxsize=64)
def bernoulli_exact(n: int) -> Fraction:
    r"""Return B_n as an exact Fraction.

    Uses sympy for the computation, converts to Fraction for exact arithmetic.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_3 = 0, B_4 = -1/30, ...
    All odd Bernoulli numbers vanish for n >= 3.
    """
    if n < 0:
        raise ValueError(f"Bernoulli number requires n >= 0, got {n}")
    return Fraction(Rational(bernoulli(n)))


# =========================================================================
# Section 2: Lambda_g via independent formula (cross-verification)
# =========================================================================

@lru_cache(maxsize=64)
def lambda_fp_independent(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number, independent computation.

    lambda_g^{FP} = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    This is an independent implementation for cross-verification against
    the canonical lambda_fp from btz_entropy_allgenus.py.

    Exact values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B_2g = bernoulli_exact(2 * g)
    power = 2 ** (2 * g - 1)
    # |B_{2g}| -- Bernoulli numbers alternate sign for even index >= 2
    abs_B_2g = abs(B_2g)
    num = Fraction(power - 1) * abs_B_2g
    den = Fraction(power) * Fraction(int(factorial(2 * g)))
    return num / den


# =========================================================================
# Section 3: Free energies F_g (scalar and known Virasoro window)
# =========================================================================

def free_energy_scalar(g: int, kappa: Fraction) -> Fraction:
    r"""Scalar (uniform-weight) genus-g free energy.

    F_g^{scalar} = kappa * lambda_g^{FP}    for g >= 1
    F_0 = 0  (regularized; the classical action requires separate treatment)

    (UNIFORM-WEIGHT)

    Parameters
    ----------
    g : genus (non-negative integer)
    kappa : the shadow invariant kappa(A) for the chiral algebra A

    Returns
    -------
    F_g as an exact Fraction
    """
    if g < 0:
        raise ValueError(f"genus must be non-negative, got {g}")
    if g == 0:
        return Fraction(0)
    return kappa * lambda_fp(g)


def free_energy_virasoro_known_window(g: int, c) -> Fraction:
    r"""Known Virasoro genus-g coefficient at central charge c.

    Includes planted-forest corrections exactly where this compute
    layer has them (g = 2, 3).  For g >= 4 it returns only the scalar
    component kappa(Vir_c) * lambda_g^{FP}; it is not a full Virasoro
    coefficient at those genera.

    F_1 = kappa/24 = c/48
    F_2 = F_2^{scalar} + delta_pf^{(2,0)}
    F_3 = F_3^{scalar} + delta_pf^{(3,0)}
    F_g = F_g^{scalar} for g >= 4  (scalar component only here)
    """
    c_frac = Fraction(c)
    if g < 0:
        raise ValueError(f"genus must be non-negative, got {g}")
    if g == 0:
        return Fraction(0)
    if g == 1:
        return F1_virasoro(c_frac)
    if g == 2:
        return F2_full(c_frac)
    if g == 3:
        return F3_full(c_frac)
    # g >= 4: scalar only
    return free_energy_scalar(g, kappa_virasoro(c_frac))


def free_energy_full_virasoro(g: int, c) -> Fraction:
    r"""Compatibility wrapper for the known-window Virasoro coefficient.

    The name is exact only for g <= 3 in this module.  For g >= 4 the
    returned value is the scalar component, and
    ``virasoro_coefficient_scope(g)`` records that the full
    planted-forest correction is not computed here.
    """
    return free_energy_virasoro_known_window(g, c)


# =========================================================================
# Section 4: Scalar and known-window coefficient tables
# =========================================================================

def gravity_partition_coefficients_scalar(
    kappa: Fraction, g_max: int = 9
) -> List[Fraction]:
    r"""Scalar free energies F_0, F_1, ..., F_{g_max} as exact Fractions.

    (UNIFORM-WEIGHT)

    Parameters
    ----------
    kappa : shadow invariant
    g_max : maximum genus (inclusive)

    Returns
    -------
    List of length g_max + 1, where entry g is F_g^{scalar}.
    """
    return [free_energy_scalar(g, kappa) for g in range(g_max + 1)]


def gravity_partition_coefficients_virasoro(
    c, g_max: int = 9
) -> List[Fraction]:
    r"""Known-window Virasoro coefficients F_0, ..., F_{g_max}.

    Uses planted-forest corrections at g = 2, 3.  For g >= 4 the list
    contains scalar components only.

    Parameters
    ----------
    c : central charge
    g_max : maximum genus (inclusive)

    Returns
    -------
    List of length g_max + 1, with the scope recorded by
    virasoro_coefficient_scope(g).
    """
    return [free_energy_virasoro_known_window(g, c) for g in range(g_max + 1)]


def partition_function_table(c, g_max: int = 9) -> Dict[str, Any]:
    r"""Finite-window Virasoro coefficient table at central charge c.

    Returns exact scalar coefficients and known-window coefficients.
    """
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)
    scalar_coeffs = gravity_partition_coefficients_scalar(kappa, g_max)
    known_coeffs = gravity_partition_coefficients_virasoro(c_frac, g_max)

    return {
        'c': c_frac,
        'kappa': kappa,
        'g_max': g_max,
        'F_scalar': scalar_coeffs,
        'F_known': known_coeffs,
        'F_scope': [virasoro_coefficient_scope(g) for g in range(g_max + 1)],
        'F_scalar_float': [float(f) for f in scalar_coeffs],
        'F_known_float': [float(f) for f in known_coeffs],
    }


# =========================================================================
# Section 5: Scalar ordinary generating function
# =========================================================================

def generating_function_closed_form(kappa_val: float, hbar: float) -> float:
    r"""Closed form for the scalar ordinary genus generating function.

    sum_{g >= 1} F_g^{scalar} * hbar^{2g} = kappa * [(hbar/2)/sin(hbar/2) - 1]

    Convergent for |hbar| < 2*pi on the scalar lane.  This function
    does not include planted-forest corrections.

    Parameters
    ----------
    kappa_val : kappa(A) as a float
    hbar : formal expansion parameter

    Returns
    -------
    The value of the generating function (without the g=0 term).
    """
    h = float(hbar)
    if abs(h) < 1e-15:
        return 0.0
    half_h = h / 2.0
    # Guard against poles at hbar = 2*pi*n
    sin_val = math.sin(half_h)
    if abs(sin_val) < 1e-15:
        return float('inf')
    return float(kappa_val) * (half_h / sin_val - 1.0)


def generating_function_series(kappa_val: float, hbar: float, g_max: int = 30) -> float:
    r"""Partial sum of the scalar genus expansion.

    sum_{g=1}^{g_max} F_g^{scalar} * hbar^{2g}
    """
    total = 0.0
    kappa_f = float(kappa_val)
    h2 = float(hbar) ** 2
    h2g = h2  # starts at hbar^2
    for g in range(1, g_max + 1):
        total += kappa_f * lambda_fp_float(g) * h2g
        h2g *= h2
    return total


def verify_generating_function(c, hbar: float = 1.0, g_max: int = 30) -> Dict[str, Any]:
    r"""Verify the scalar A-hat generating function identity.

    sum_{g>=1} F_g * hbar^{2g} = kappa * [(hbar/2)/sin(hbar/2) - 1]
    """
    kappa = float(kappa_virasoro(c))
    series = generating_function_series(kappa, hbar, g_max)
    closed = generating_function_closed_form(kappa, hbar)
    return {
        'c': c,
        'kappa': kappa,
        'hbar': hbar,
        'g_max': g_max,
        'series_value': series,
        'closed_form_value': closed,
        'difference': abs(series - closed),
        'match': abs(series - closed) < 1e-10,
        'scope': SCALAR_RADIUS_SCOPE,
        'includes_planted_forest': False,
    }


# =========================================================================
# Section 6: BTZ entropy comparison
# =========================================================================

def btz_entropy(c, E: float) -> float:
    r"""BTZ black hole entropy: S_BTZ = 2*pi*sqrt(c*E/6).

    Parameters
    ----------
    c : central charge
    E : energy (= L_0 - c/24 in CFT language)

    This is the Cardy / Bekenstein-Hawking entropy for the BTZ black hole
    in AdS_3 with c = 3l/(2G_N).
    """
    c_f, E_f = float(c), float(E)
    if c_f * E_f <= 0:
        return 0.0
    return 2 * PI * math.sqrt(c_f * E_f / 6.0)


# =========================================================================
# Section 7: Asymptotic growth rate
# =========================================================================

def asymptotic_ratios(coefficients: List[Fraction], start_g: int = 1) -> List[Dict[str, Any]]:
    r"""Compute consecutive ratios |F_{g+1}/F_g| for scalar diagnostics.

    For the scalar Virasoro genus expansion, the asymptotic behavior is:

        |F_{g+1}/F_g| -> 1/(4*pi^2)    as g -> infinity

    This is geometric decay (Gevrey 0), not factorial growth.

    The normalized ratio:

        R_g = |F_{g+1}/F_g| * (4*pi^2)

    should converge to 1.

    Parameters
    ----------
    coefficients : list of F_g values (index = genus), starting from g=0
    start_g : first genus to include in the ratio analysis

    Returns
    -------
    List of dicts with genus, raw_ratio, normalized_ratio, convergence info.
    """
    ratios = []
    for g in range(max(start_g, 1), len(coefficients) - 1):
        Fg = float(coefficients[g])
        Fg1 = float(coefficients[g + 1])
        if abs(Fg) < 1e-300:
            continue
        raw_ratio = abs(Fg1 / Fg)
        # Predicted asymptotic ratio: |F_{g+1}/F_g| -> 1/(4*pi^2) as g -> inf
        # This is because lambda_fp(g) ~ 2*(1/(4*pi^2))^g (geometric decay
        # from the nearest pole of 1/sin(x/2) at x = 2*pi).
        predicted = 1.0 / FOUR_PI_SQ
        normalized = raw_ratio / predicted if predicted > 0 else float('inf')
        ratios.append({
            'g': g,
            'F_g': Fg,
            'F_{g+1}': Fg1,
            'raw_ratio': raw_ratio,
            'predicted_ratio': predicted,
            'normalized_ratio': normalized,
            'scope': SCALAR_RADIUS_SCOPE,
        })
    return ratios


def convergence_radius_from_ratios(coefficients: List[Fraction]) -> float:
    r"""Finite-window estimate of the scalar radius from coefficient ratios.

    The radius is R = lim 1 / |F_g / F_{g-1}|^{1/2} in the hbar^{2g} variable.

    For the scalar Virasoro expansion, the exact radius is 2*pi from
    the pole of 1/sin at 2*pi.  This function only estimates it from
    the supplied finite window.
    """
    if len(coefficients) < 3:
        return float('inf')
    # Use the last available ratio
    g = len(coefficients) - 2
    Fg = float(coefficients[g])
    Fg1 = float(coefficients[g + 1])
    if abs(Fg1) < 1e-300 or abs(Fg) < 1e-300:
        return float('inf')
    raw_ratio = abs(Fg1 / Fg)
    # The power series is sum F_g * hbar^{2g}, so the radius of convergence
    # in the variable hbar^2 is 1/limsup |F_{g+1}/F_g| = 4*pi^2.
    # The radius in hbar is sqrt(4*pi^2) = 2*pi.
    R_sq = 1.0 / raw_ratio
    return math.sqrt(R_sq) if R_sq > 0 else float('inf')


def btz_growth_comparison(c, g_max: int = 9) -> Dict[str, Any]:
    r"""Scalar Bernoulli growth diagnostics adjacent to the BTZ formula.

    Returns a comparison table with:
    - scalar F_g values;
    - finite-window ratio diagnostics;
    - finite-window radius estimate;
    - exact scalar-lane radius and growth constant.

    It asserts no Borel summability and no closed form for the full
    planted-forest Virasoro partition function.
    """
    kappa = kappa_virasoro(c)
    coeffs = gravity_partition_coefficients_scalar(kappa, g_max)
    ratios = asymptotic_ratios(coeffs, start_g=1)
    R_est = convergence_radius_from_ratios(coeffs)

    return {
        'c': float(Fraction(c)),
        'kappa': float(kappa),
        'g_max': g_max,
        'coefficients': [float(f) for f in coeffs],
        'ratios': ratios,
        'radius_estimate_from_window': R_est,
        'scalar_convergence_radius_exact': scalar_convergence_radius_exact(),
        'radius_relative_error_to_scalar_exact': abs(R_est - TWO_PI) / TWO_PI,
        'scalar_growth_constant_exact': 1.0 / FOUR_PI_SQ,
        'gevrey_class': SCALAR_GEVREY_CLASS,
        'scope': SCALAR_RADIUS_SCOPE,
        'analytic_claims': {
            'full_partition_convergence': False,
            'borel_summability': False,
            'btz_closed_form_from_scalar_series': False,
        },
    }


# =========================================================================
# Section 8: Special central charges
# =========================================================================

def self_dual_c13_table(g_max: int = 9) -> Dict[str, Any]:
    r"""Scalar and known-window coefficient data at c = 13.

    At c = 13: kappa = 13/2 and the same-family complementarity
    partner Vir_{26-13} has kappa = 13/2.
    Complementarity: kappa + kappa' = 13 (census C8).

    The scalar free energies satisfy:
        F_g(c=13) = (13/2) * lambda_g^{FP}

    Complementarity at the scalar level:
        F_g(c) + F_g(26-c) = 13 * lambda_g^{FP}
    At c = 13 this becomes 2 * F_g(13) = 13 * lambda_g^{FP}, i.e.
    F_g(13) = (13/2) * lambda_g^{FP} (tautological check).
    """
    c = Fraction(13)
    table = partition_function_table(c, g_max)
    # Complementarity check
    comp_check = []
    for g in range(1, g_max + 1):
        Fg_13 = table['F_scalar'][g]
        target = Fraction(13) * lambda_fp(g)
        comp_check.append({
            'g': g,
            '2*F_g': 2 * Fg_13,
            '13*lambda_g': target,
            'match': 2 * Fg_13 == target,
        })
    table['complementarity_check'] = comp_check
    table['all_complementarity_hold'] = all(c['match'] for c in comp_check)
    return table


def critical_c26_table(g_max: int = 9) -> Dict[str, Any]:
    r"""Scalar and known-window coefficient data at c = 26.

    At c = 26: kappa = 13, kappa(Vir_0) = 0.
    The same-family scalar complementarity partner has central charge 0.

    Physical significance: the bosonic string has matter c = 26 and
    bc ghost c = -26, giving kappa_eff = kappa(matter) + kappa(ghost) = 13 + (-13) = 0.
    The vanishing of kappa_eff is the condition for anomaly cancellation.

    The free energies at c = 26 are twice those at c = 13:
        F_g(26) = 13 * lambda_g^{FP} = 2 * F_g(13)

    Complementarity:
        F_g(26) + F_g(0) = 13 * lambda_g^{FP} + 0 = 13 * lambda_g^{FP} = F_g(26)
    (trivially satisfied since kappa(Vir_0) = 0).
    """
    c = Fraction(26)
    table = partition_function_table(c, g_max)
    # Check F_g(26) = 2 * F_g(13)
    doubling_check = []
    for g in range(1, g_max + 1):
        Fg_26 = table['F_scalar'][g]
        Fg_13 = free_energy_scalar(g, kappa_virasoro(Fraction(13)))
        doubling_check.append({
            'g': g,
            'F_g_26': Fg_26,
            '2*F_g_13': 2 * Fg_13,
            'match': Fg_26 == 2 * Fg_13,
        })
    table['doubling_check'] = doubling_check
    table['all_doubling_hold'] = all(d['match'] for d in doubling_check)
    return table


# =========================================================================
# Section 9: Comprehensive summary
# =========================================================================

def comprehensive_summary(g_max: int = 9) -> Dict[str, Any]:
    r"""Finite-window summary for c = 13 and c = 26.

    This is the main entry point for the scalar and known planted-forest
    coefficient computation.
    """
    # Use at least 20 terms for the generating function series check
    # to ensure convergence to the 1e-10 threshold.
    gf_terms = max(g_max, 20)
    return {
        'c13': self_dual_c13_table(g_max),
        'c26': critical_c26_table(g_max),
        'scalar_growth_c13': btz_growth_comparison(13, g_max),
        'scalar_growth_c26': btz_growth_comparison(26, g_max),
        'generating_function_c13': verify_generating_function(13, 1.0, gf_terms),
        'generating_function_c26': verify_generating_function(26, 1.0, gf_terms),
    }


# =========================================================================
# Main (for standalone execution)
# =========================================================================

if __name__ == '__main__':
    import json

    print("=" * 72)
    print("Finite-window Virasoro coefficient diagnostics")
    print("=" * 72)

    for c_val in [13, 26]:
        kappa = kappa_virasoro(c_val)
        print(f"\nc = {c_val}, kappa = {kappa} = {float(kappa):.6f}")
        print("-" * 60)

        coeffs = gravity_partition_coefficients_virasoro(c_val, 9)
        print(f"{'g':>3}  {'F_g (known window)':>35}  {'F_g (float)':>18}")
        for g, fg in enumerate(coeffs):
            print(f"{g:>3}  {str(fg):>35}  {float(fg):>18.12e}")

        print(f"\nGenerating function check (hbar=1):")
        gf = verify_generating_function(c_val, 1.0, 30)
        print(f"  Series (30 terms): {gf['series_value']:.15e}")
        print(f"  Closed form:       {gf['closed_form_value']:.15e}")
        print(f"  Difference:        {gf['difference']:.2e}")

        print(f"\nAsymptotic ratios:")
        btz = btz_growth_comparison(c_val, 9)
        for r in btz['ratios']:
            print(f"  g={r['g']:>2}: |F_{{g+1}}/F_g| = {r['raw_ratio']:.6e}, "
                  f"normalized = {r['normalized_ratio']:.6f}")
        print(f"  Window radius estimate: {btz['radius_estimate_from_window']:.6f}")
        print(f"  Scalar exact radius:    {btz['scalar_convergence_radius_exact']:.6f}")

    print("\nBTZ entropy at representative energies:")
    for c_val in [13, 26]:
        for E in [1.0, 10.0, 100.0]:
            S = btz_entropy(c_val, E)
            print(f"  c={c_val}, E={E:>5.0f}: S_BTZ = {S:.6f}")
