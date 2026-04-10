r"""3D gravity partition function Z_{3d}(hbar) from the Virasoro shadow tower.

MATHEMATICAL FRAMEWORK
======================

The 3D gravity partition function is the genus expansion:

    Z_{3d}(hbar) = exp( sum_{g >= 0} F_g * hbar^{2g-2} )

where F_g are the genus-g free energies of the Virasoro shadow tower.

The free energy has a LOGARITHMIC expansion:

    log Z_{3d}(hbar) = F_0 * hbar^{-2} + F_1 * hbar^0 + F_2 * hbar^2 + ...

The F_g are computed from the Faber-Pandharipande intersection numbers:

    F_g^{scalar}(Vir_c) = kappa(Vir_c) * lambda_g^{FP}    for g >= 1

where:
    kappa(Vir_c) = c/2                              (census C2)
    lambda_g^{FP} = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

For Virasoro (class M), there are planted-forest corrections at g >= 2:

    F_g^{full} = F_g^{scalar} + delta_pf^{(g,0)}

GENERATING FUNCTION
===================

The scalar part has a closed-form generating function:

    sum_{g >= 1} F_g^{scalar} * hbar^{2g} = kappa * [(hbar/2)/sin(hbar/2) - 1]

This converges for |hbar| < 2*pi (radius of convergence from the
nearest pole of 1/sin at hbar = 2*pi).

BTZ ASYMPTOTICS
===============

The asymptotic growth of F_g for large g is controlled by the
nearest singularity of the generating function.  Since 1/sin(x/2)
has poles at x = 2*pi*n, the scalar free energies satisfy:

    lambda_g^{FP} ~ 2 * (1/(4*pi^2))^g    as g -> infinity

This is GEOMETRIC decay (the (2g)! in the Bernoulli numerator is
cancelled by the (2g)! in the denominator of lambda_g^{FP}).  Hence the
genus expansion sum F_g * hbar^{2g} is a CONVERGENT series with radius
of convergence 2*pi in hbar (set by the pole of 1/sin at x = 2*pi).

The ratio:

    |F_{g+1}/F_g| -> 1/(4*pi^2) ~ 0.02533    as g -> infinity

The BTZ black hole entropy is related via saddle-point:

    S_BTZ = 2*pi*sqrt(c*E/6)

TWO SPECIAL CENTRAL CHARGES
============================

c = 13  (Virasoro self-dual point):
  kappa = 13/2, kappa' = kappa(Vir_{26-13}) = 13/2
  Complementarity: kappa + kappa' = 13
  Self-dual: F_g(c=13) = F_g(c=13) (tautological, but the planted-forest
  corrections are symmetric under c -> 26-c only at the scalar level)

c = 26  (bosonic string critical dimension):
  kappa = 13
  This is the kappa_eff = 0 point: kappa(matter) + kappa(ghost) = 13 + (-13) = 0
  The dual central charge is c' = 0, and kappa(Vir_0) = 0

References:
  Faber-Pandharipande 1998: lambda_g intersection numbers
  Maloney-Witten 2010: 0712.0155 (pure gravity partition function)
  thm:theorem-d (higher_genus_modular_koszul.tex)
  btz_entropy_allgenus.py (canonical source for lambda_fp, kappa, etc.)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

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
    F2_scalar,
    F2_full,
    F3_scalar,
    F3_full,
    F4_scalar,
    virasoro_S3,
    virasoro_S4,
    virasoro_S5,
    bekenstein_hawking_entropy,
)

PI = math.pi
TWO_PI = 2 * PI
FOUR_PI_SQ = 4 * PI ** 2


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
        g=1: 1/24       # VERIFIED [DC] direct Bernoulli + [LT] Faber-Pandharipande 1998
        g=2: 7/5760     # VERIFIED [DC] direct Bernoulli + [LT] Faber-Pandharipande 1998
        g=3: 31/967680  # VERIFIED [DC] direct Bernoulli + [LT] Mumford 1983
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
# Section 3: Free energies F_g (scalar and full)
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


def free_energy_full_virasoro(g: int, c) -> Fraction:
    r"""Full genus-g free energy for Virasoro at central charge c.

    Includes planted-forest corrections where available (g = 2, 3).
    Falls back to scalar for g = 1 and g >= 4.

    F_1 = kappa/24 = c/48
    F_2 = F_2^{scalar} + delta_pf^{(2,0)}
    F_3 = F_3^{scalar} + delta_pf^{(3,0)}
    F_g = F_g^{scalar} for g >= 4  (planted-forest not yet computed)

    (UNIFORM-WEIGHT for scalar part; ALL-WEIGHT corrections in delta_pf)
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


# =========================================================================
# Section 4: Partition function coefficients
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
    r"""Full Virasoro free energies F_0, F_1, ..., F_{g_max} at central charge c.

    Uses planted-forest corrections at g = 2, 3 where available.

    Parameters
    ----------
    c : central charge
    g_max : maximum genus (inclusive)

    Returns
    -------
    List of length g_max + 1, where entry g is F_g^{full}(Vir_c).
    """
    return [free_energy_full_virasoro(g, c) for g in range(g_max + 1)]


def partition_function_table(c, g_max: int = 9) -> Dict[str, Any]:
    r"""Complete table of Z_{3d} data for Virasoro at central charge c.

    Returns scalar and full coefficients, plus summary data.
    """
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)
    scalar_coeffs = gravity_partition_coefficients_scalar(kappa, g_max)
    full_coeffs = gravity_partition_coefficients_virasoro(c_frac, g_max)

    return {
        'c': c_frac,
        'kappa': kappa,
        'g_max': g_max,
        'F_scalar': scalar_coeffs,
        'F_full': full_coeffs,
        'F_scalar_float': [float(f) for f in scalar_coeffs],
        'F_full_float': [float(f) for f in full_coeffs],
    }


# =========================================================================
# Section 5: Generating function (closed form)
# =========================================================================

def generating_function_closed_form(kappa_val: float, hbar: float) -> float:
    r"""Closed-form generating function for the scalar genus expansion.

    sum_{g >= 1} F_g^{scalar} * hbar^{2g} = kappa * [(hbar/2)/sin(hbar/2) - 1]

    Convergent for |hbar| < 2*pi.

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
    r"""Verify the A-hat generating function identity.

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
    r"""Compute consecutive ratios |F_{g+1}/F_g| and extract growth diagnostics.

    For the scalar Virasoro genus expansion, the asymptotic behavior is:

        |F_{g+1}/F_g| -> 1/(4*pi^2)    as g -> infinity

    This is GEOMETRIC decay (convergent series, Gevrey-0), not factorial
    growth.  The convergence radius of sum F_g * hbar^{2g} is 2*pi, set
    by the nearest pole of 1/sin(x/2).

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
        })
    return ratios


def convergence_radius_from_ratios(coefficients: List[Fraction]) -> float:
    r"""Estimate the convergence radius of sum F_g * hbar^{2g}.

    The radius is R = lim 1 / |F_g / F_{g-1}|^{1/2} in the hbar^{2g} variable.

    For the scalar Virasoro expansion, R = 2*pi (from the pole of 1/sin at 2*pi).

    We estimate R from the last few ratios via:
        R ~ sqrt((2g)(2g-1) / |F_g/F_{g-1}|)
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
    r"""Compare asymptotic growth of F_g with BTZ predictions.

    The BTZ saddle-point predicts that the genus expansion is an asymptotic
    series with coefficients growing like (2g)! / (4*pi^2)^g.

    This is the signature of Gevrey-1 divergence with Borel singularity
    at t = 4*pi^2 (the action of the BTZ instanton).

    The Borel sum recovers the non-perturbative BTZ entropy.

    Returns a comparison table with:
    - Exact F_g values
    - Asymptotic ratios
    - Estimated convergence radius (should approach 2*pi)
    - Comparison with 1/(4*pi^2) growth constant
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
        'convergence_radius_estimated': R_est,
        'convergence_radius_exact': TWO_PI,
        'radius_relative_error': abs(R_est - TWO_PI) / TWO_PI,
        'btz_growth_constant': 1.0 / FOUR_PI_SQ,
    }


# =========================================================================
# Section 8: Special central charges
# =========================================================================

def self_dual_c13_table(g_max: int = 9) -> Dict[str, Any]:
    r"""Partition function data at the self-dual point c = 13.

    At c = 13: kappa = 13/2, kappa' = kappa(Vir_{26-13}) = 13/2.
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
    r"""Partition function data at c = 26 (bosonic string critical dimension).

    At c = 26: kappa = 13, kappa(Vir_0) = 0.
    The dual algebra Vir^! = Vir_{26-c} = Vir_0 has kappa = 0.

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
    r"""Full summary for both c = 13 and c = 26, with BTZ comparison.

    This is the main entry point for the 3D gravity partition function
    computation.
    """
    # Use at least 20 terms for the generating function series check
    # to ensure convergence to the 1e-10 threshold.
    gf_terms = max(g_max, 20)
    return {
        'c13': self_dual_c13_table(g_max),
        'c26': critical_c26_table(g_max),
        'btz_c13': btz_growth_comparison(13, g_max),
        'btz_c26': btz_growth_comparison(26, g_max),
        'generating_function_c13': verify_generating_function(13, 1.0, gf_terms),
        'generating_function_c26': verify_generating_function(26, 1.0, gf_terms),
    }


# =========================================================================
# Main (for standalone execution)
# =========================================================================

if __name__ == '__main__':
    import json

    print("=" * 72)
    print("3D Gravity Partition Function: Virasoro Shadow Tower")
    print("=" * 72)

    for c_val in [13, 26]:
        kappa = kappa_virasoro(c_val)
        print(f"\nc = {c_val}, kappa = {kappa} = {float(kappa):.6f}")
        print("-" * 60)

        coeffs = gravity_partition_coefficients_virasoro(c_val, 9)
        print(f"{'g':>3}  {'F_g (exact)':>35}  {'F_g (float)':>18}")
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
        print(f"  Estimated convergence radius: {btz['convergence_radius_estimated']:.6f}")
        print(f"  Exact convergence radius:     {btz['convergence_radius_exact']:.6f}")

    print("\nBTZ entropy at representative energies:")
    for c_val in [13, 26]:
        for E in [1.0, 10.0, 100.0]:
            S = btz_entropy(c_val, E)
            print(f"  c={c_val}, E={E:>5.0f}: S_BTZ = {S:.6f}")
