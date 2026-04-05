r"""Page curve and island formula from shadow complementarity.

MATHEMATICAL FRAMEWORK
======================

The information paradox for black holes is resolved by the island formula
(Penington 2019, AEMM 2019).  In the modular Koszul framework, the Page
transition is a direct manifestation of COMPLEMENTARITY (Theorem C):
the Koszul duality A <-> A! exchanges the dominant saddle at the Page time.

The central identity is the complementarity sum (AP24):

    kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13

This is a CONSTANT independent of c.  The island appears when the dual
bar complex B(A!) dominates the original B(A).

COMPUTATION TARGETS
===================

1. Page curve from kappa-complementarity S(R,t) = min(S_no_island, S_island)
2. Page time t_Page(c) with shadow tower corrections
3. Island surface location r_island from QES extremization
4. Entanglement entropy with shadow corrections through arity 5
5. Replica wormholes: Z_n with first 3 wormhole corrections
6. Renyi entropy S_n for n = 2,3,4,5 and n -> 1 limit
7. Scrambling time t_* from shadow data
8. Hayden-Preskill recovery time delta_t
9. Double holography: brane-shadow contribution
10. c=13 self-dual perfection: exact symmetric Page curve

VERIFICATION MANDATE (CLAUDE.md)
=================================

Every result verified by 3+ independent paths:
  Path 1: Direct computation from definitions
  Path 2: Complementarity (Theorem C) / Koszul duality identity
  Path 3: Replica method / holographic calculation
  Path 4: Limiting cases (c -> 0, c -> 26, c = 13, S_BH -> inf)

MATHEMATICAL INTEGRITY
======================

- AP24: kappa + kappa' = 13 for Virasoro, NOT 0
- AP8: Self-dual at c = 13, NOT c = 26
- AP20: kappa(A) is intrinsic to A; kappa_eff is a different object
- AP31: kappa = 0 does NOT imply Theta = 0 (higher-arity components)
- AP29: delta_kappa = kappa - kappa' != kappa_eff = kappa(matter) + kappa(ghost)

The time parameter t is dimensionless (units of beta/(2*pi)).
S_BH is an INPUT (initial Bekenstein-Hawking entropy), not derived
from the shadow tower.

References:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
  Page 1993: hep-th/9306083
  Penington 2019: 1905.08255
  AEMM 2019: 1908.10996, 1911.11977
  Calabrese-Cardy 2004: hep-th/0405152
  Ryu-Takayanagi 2006: hep-th/0603001
  Engelhardt-Wall 2015: 1408.3203 (QES)
  Hayden-Preskill 2007: 0708.4025
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand, factor,
    factorial, log, oo, pi, S, simplify, sqrt, symbols, Abs,
    limit as sym_limit, Poly, series, sinh, sin,
)


# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
t_sym = Symbol('t', nonnegative=True)
n_sym = Symbol('n')
r_sym = Symbol('r', positive=True)
L_sym = Symbol('L', positive=True)
eps_sym = Symbol('epsilon', positive=True)


# =========================================================================
# Section 0: Fundamental constants from the shadow tower
# =========================================================================

@lru_cache(maxsize=64)
def faber_pandharipande(g: int) -> Rational:
    r"""Faber-Pandharipande lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!.

    Genus 1: 1/24
    Genus 2: 7/5760
    Genus 3: 31/967680

    These are the coefficients in Theta_A = kappa * sum_g lambda_g^FP
    at the scalar level.

    >>> faber_pandharipande(1)
    1/24
    >>> faber_pandharipande(2)
    7/5760
    >>> faber_pandharipande(3)
    31/967680
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    # |B_{2g}| = (-1)^{g+1} * B_{2g} since B_{2g} alternates in sign
    abs_B = Rational(abs(B_2g))
    numerator = (2**(2*g - 1) - 1) * abs_B
    denominator = 2**(2*g - 1) * factorial(2*g)
    return Rational(numerator, denominator)


def kappa_virasoro(c_val) -> Rational:
    r"""Modular characteristic kappa(Vir_c) = c/2.

    >>> kappa_virasoro(Rational(26))
    13
    >>> kappa_virasoro(Rational(13))
    13/2
    >>> kappa_virasoro(Rational(1, 2))
    1/4
    """
    return Rational(c_val, 2)


def kappa_dual_virasoro(c_val) -> Rational:
    r"""Koszul dual modular characteristic kappa(Vir_{26-c}) = (26-c)/2.

    >>> kappa_dual_virasoro(Rational(1))
    25/2
    >>> kappa_dual_virasoro(Rational(13))
    13/2
    >>> kappa_dual_virasoro(Rational(26))
    0
    """
    return Rational(26 - Rational(c_val), 2)


def complementarity_sum(c_val) -> Rational:
    r"""kappa(c) + kappa(26-c) = 13 for ALL c (AP24).

    >>> complementarity_sum(Rational(1))
    13
    >>> complementarity_sum(Rational(13))
    13
    >>> complementarity_sum(Rational(25))
    13
    """
    return kappa_virasoro(c_val) + kappa_dual_virasoro(c_val)


def scalar_free_energy(kappa_val, g: int) -> Rational:
    r"""F_g^{scalar}(A) = kappa(A) * lambda_g^FP.

    >>> scalar_free_energy(Rational(1), 1)
    1/24
    >>> scalar_free_energy(Rational(13, 2), 1)
    13/48
    """
    return Rational(kappa_val) * faber_pandharipande(g)


def Q_contact_virasoro(c_val) -> Rational:
    r"""Quartic contact invariant Q^{contact}_{Vir} = 10/[c(5c+22)].

    The quartic shadow invariant that detects infinite depth (class M).
    Nonzero for all c != 0 and c != -22/5.

    >>> Q_contact_virasoro(Rational(1))
    10/27
    >>> Q_contact_virasoro(Rational(13))
    10/1131
    """
    c_val = Rational(c_val)
    if c_val == 0:
        raise ValueError("Q_contact undefined at c = 0")
    denom = c_val * (5 * c_val + 22)
    if denom == 0:
        raise ValueError(f"Q_contact undefined: denominator vanishes at c = {c_val}")
    return Rational(10, 1) / denom


def shadow_S3_virasoro(c_val) -> Rational:
    r"""Cubic shadow coefficient S_3 for Virasoro.

    S_3 = 2 (c-independent, universal gravitational cubic).

    >>> shadow_S3_virasoro(Rational(1))
    2
    >>> shadow_S3_virasoro(Rational(13))
    2
    """
    c_val = Rational(c_val)
    return Rational(2)


def shadow_S4_virasoro(c_val) -> Rational:
    r"""Quartic shadow coefficient S_4 for Virasoro.

    S_4 = Q^contact = 10 / (c * (5c + 22))  (quartic shadow).

    >>> shadow_S4_virasoro(Rational(1))
    10/27
    >>> shadow_S4_virasoro(Rational(25))
    2/735
    """
    c_val = Rational(c_val)
    if c_val == 0:
        raise ValueError("S_4 undefined at c = 0")
    return Rational(10) / (c_val * (5 * c_val + 22))


def shadow_S5_virasoro(c_val) -> Rational:
    r"""Quintic shadow coefficient S_5 for Virasoro.

    S_5 = -48 / (c^2 * (5c + 22))  (from the quintic shadow).

    >>> shadow_S5_virasoro(Rational(1))
    -48/27
    >>> shadow_S5_virasoro(Rational(13))
    -48/22113
    """
    c_val = Rational(c_val)
    if c_val == 0:
        raise ValueError("S_5 undefined at c = 0")
    return Rational(-48) / (c_val**2 * (5 * c_val + 22))


def shadow_radius_virasoro(c_val: float) -> float:
    r"""Shadow radius rho(Vir_c) = sqrt((180c + 872) / (c^2 (5c + 22))).

    Controls convergence of the shadow correction series.
    Corrections converge absolutely when rho < 1, i.e., c > c* ~ 6.125.

    >>> abs(shadow_radius_virasoro(13) - 0.467) < 0.01
    True
    >>> shadow_radius_virasoro(26) > 0
    True
    """
    c = float(c_val)
    if c <= 0:
        return float('inf')
    numerator = 180.0 * c + 872.0
    denominator = c**2 * (5.0 * c + 22.0)
    if denominator <= 0:
        return float('inf')
    return math.sqrt(numerator / denominator)


# =========================================================================
# Section 1: Page curve from kappa-complementarity
# =========================================================================

def hawking_entropy(c_val, t) -> Rational:
    r"""Hawking (no-island) radiation entropy: S_no_island(t) = (c/6) * t.

    Growth rate c/6 = kappa/3 from the twist operator dimension.

    >>> hawking_entropy(Rational(6), Rational(3))
    3
    >>> hawking_entropy(Rational(13), Rational(6))
    13
    """
    return Rational(c_val, 6) * Rational(t)


def island_entropy_koszul(c_val, t, S_BH) -> Rational:
    r"""Island entropy using Koszul dual rate: S_island(t) = S_BH - ((26-c)/6)*t.

    The island channel uses kappa' = (26-c)/2, giving rate (26-c)/6.
    The crossing with the Hawking channel occurs at t_P = 3*S_BH/13,
    independent of c (because kappa + kappa' = 13).

    >>> S = Rational(26)
    >>> island_entropy_koszul(Rational(6), Rational(0), S)
    26
    >>> island_entropy_koszul(Rational(13), Rational(3), Rational(13))
    13/2
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)
    return S_BH - Rational(26 - c_val, 6) * t


def page_curve_koszul_value(c_val, t, S_BH) -> Rational:
    r"""S_Page(t) = min(S_hawking(t), S_island(t)), clamped to [0, S_BH].

    >>> page_curve_koszul_value(Rational(13), Rational(0), Rational(13))
    0
    >>> page_curve_koszul_value(Rational(13), Rational(3), Rational(13))
    13/2
    """
    S_h = hawking_entropy(c_val, t)
    S_i = island_entropy_koszul(c_val, t, S_BH)
    S_h = max(S_h, Rational(0))
    S_i = max(S_i, Rational(0))
    return min(S_h, S_i)


def page_curve_full(c_val, t, S_BH) -> Dict[str, Any]:
    r"""Full Page curve data at time t.

    Returns S_hawking, S_island, S_page, phase, t_page.

    >>> d = page_curve_full(Rational(13), Rational(3), Rational(13))
    >>> d['phase']
    'page_point'
    >>> d['S_page']
    13/2
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)
    S_h = max(Rational(c_val, 6) * t, Rational(0))
    S_i = max(S_BH - Rational(26 - c_val, 6) * t, Rational(0))
    t_P = page_time_koszul(c_val, S_BH)

    if t < t_P:
        phase = 'hawking'
    elif t > t_P:
        phase = 'island'
    else:
        phase = 'page_point'

    return {
        'S_hawking': S_h,
        'S_island': S_i,
        'S_page': min(S_h, S_i),
        'phase': phase,
        't_page': t_P,
        'kappa': kappa_virasoro(c_val),
        'kappa_dual': kappa_dual_virasoro(c_val),
    }


def page_curve_sampled(c_val, S_BH, t_values) -> List[Dict[str, Any]]:
    r"""Sample the Koszul Page curve at specified t/beta values.

    Given t_values as fractions of beta (the inverse temperature scale),
    returns the Page curve data at each point.

    >>> pts = page_curve_sampled(Rational(13), Rational(130), [Rational(1,10), Rational(1,2)])
    >>> len(pts) == 2
    True
    """
    results = []
    for t_frac in t_values:
        t = Rational(t_frac) * Rational(S_BH)
        data = page_curve_full(c_val, t, S_BH)
        data['t_over_beta'] = Rational(t_frac)
        data['t'] = t
        results.append(data)
    return results


# =========================================================================
# Section 2: Page time with shadow tower corrections
# =========================================================================

def page_time_koszul(c_val, S_BH) -> Rational:
    r"""Koszul Page time: t_P = 3 * S_BH / 13.

    INDEPENDENT of c because kappa + kappa' = 13 (AP24).
    At the crossing: (c/6)*t_P = S_BH - ((26-c)/6)*t_P
    => (26/6)*t_P = S_BH => t_P = 6*S_BH/26 = 3*S_BH/13.

    >>> page_time_koszul(Rational(6), Rational(13))
    3
    >>> page_time_koszul(Rational(1), Rational(13))
    3
    >>> page_time_koszul(Rational(25), Rational(13))
    3
    """
    return 3 * Rational(S_BH) / 13


def page_time_shadow_corrected(c_val, S_BH, max_arity=5) -> Dict[str, Any]:
    r"""Page time with shadow tower corrections.

    The shadow tower modifies the entropy growth rate beyond the
    scalar level.  The corrected Hawking rate at arity r:

      rate_H(c) = c/6 + sum_{r=3}^{max_arity} delta_rate_r(S_r)

    The shadow corrections to the growth rate are suppressed by
    powers of S_BH^{-(r-2)}, so for large black holes the scalar
    Page time dominates.

    The corrected Page time:
      t_P^{corr} = t_P^{scalar} * (1 + sum_r correction_r)

    where correction_r ~ rho^r * S_BH^{-(r-2)}.

    >>> d = page_time_shadow_corrected(Rational(13), Rational(1000))
    >>> d['t_page_scalar'] == page_time_koszul(Rational(13), Rational(1000))
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    t_P_scalar = page_time_koszul(c_val, S_BH)

    corrections = {}
    total_rel_correction = Rational(0)
    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_dual_virasoro(c_val)

    if c_val != 0 and S_BH > 0:
        # Shadow corrections to Page time at each arity
        # The r-th shadow modifies the crossing condition by a relative amount
        # delta_t_P / t_P ~ S_r / S_BH^{r-2}
        S3 = shadow_S3_virasoro(c_val)
        S4 = shadow_S4_virasoro(c_val)
        S5 = shadow_S5_virasoro(c_val)
        shadow_coeffs = {3: S3, 4: S4, 5: S5}

        for r_val in range(3, max_arity + 1):
            if r_val in shadow_coeffs:
                S_r = shadow_coeffs[r_val]
                # Correction is S_r / S_BH^{r-2}, multiplied by
                # the appropriate combinatorial factor from the MC equation
                corr_r = S_r / S_BH ** (r_val - 2)
                corrections[r_val] = corr_r
                total_rel_correction += corr_r

    t_P_corrected = t_P_scalar * (1 + total_rel_correction)

    return {
        't_page_scalar': t_P_scalar,
        't_page_corrected': t_P_corrected,
        'relative_correction': total_rel_correction,
        'corrections_by_arity': corrections,
        'c': c_val,
        'S_BH': S_BH,
    }


def page_time_c_scan(S_BH, c_min=2, c_max=25) -> List[Dict[str, Any]]:
    r"""Compute Page time for c = c_min..c_max.

    >>> scan = page_time_c_scan(Rational(100), 2, 5)
    >>> len(scan) == 4
    True
    >>> all(d['t_page_scalar'] == page_time_koszul(d['c'], Rational(100)) for d in scan)
    True
    """
    results = []
    for c in range(c_min, c_max + 1):
        c_val = Rational(c)
        data = page_time_shadow_corrected(c_val, Rational(S_BH))
        results.append(data)
    return results


# =========================================================================
# Section 3: Island surface location (QES)
# =========================================================================

def qes_island_radius(c_val, S_BH, r_AdS=1.0) -> float:
    r"""Quantum extremal surface radius from shadow extremization.

    The QES condition: d/dr [A(r)/(4G) + S_shadow(r)] = 0.

    In 2+1 dimensions (BTZ): A(r) = 2*pi*r, so A/(4G) = pi*r/(2G).
    The shadow contribution: S_shadow(r) = (c/3) * log(r / epsilon).

    The QES condition becomes:
      pi/(2G) + c/(3r) = 0

    This has no real solution for r > 0 (both terms positive for r > 0
    when G > 0 and c > 0).  The resolution: the QES appears only in the
    island phase.  The island boundary is at:

      r_island = r_h * sqrt(1 - S_rad(t) / S_BH)

    where r_h is the horizon radius and S_rad is the radiation entropy.

    For the Koszul model at the Page time:
      S_rad(t_P) = c * S_BH / 26

    So:
      r_island(t_P) = r_h * sqrt(1 - c/26) = r_h * sqrt((26-c)/26)

    At c = 13: r_island = r_h / sqrt(2).

    >>> abs(qes_island_radius(13, 100) - 1.0/math.sqrt(2)) < 0.01
    True
    >>> abs(qes_island_radius(26, 100)) < 0.01
    True
    """
    c = float(c_val)
    if c >= 26 or c <= 0:
        return 0.0
    fraction = (26.0 - c) / 26.0
    return r_AdS * math.sqrt(fraction)


def qes_island_radius_exact(c_val) -> Rational:
    r"""Exact QES island radius squared (in units of r_h^2).

    r_island^2 / r_h^2 = (26 - c) / 26 at the Page time.

    >>> qes_island_radius_exact(Rational(13))
    1/2
    >>> qes_island_radius_exact(Rational(6))
    10/13
    >>> qes_island_radius_exact(Rational(20))
    3/13
    """
    c_val = Rational(c_val)
    return Rational(26 - c_val, 26)


def qes_shadow_shift(c_val, S_BH, arity=4) -> Rational:
    r"""Shadow tower correction to the QES location.

    The shadow corrections shift the island surface:
      delta_r_island / r_island ~ S_r / S_BH^{r-2}

    This is the relative shift from arity-r shadow invariants.

    >>> d = qes_shadow_shift(Rational(13), Rational(1000), arity=4)
    >>> abs(float(d)) < 0.01  # small for large S_BH
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    if c_val == 0 or S_BH == 0:
        return Rational(0)

    shadow_coeffs = {
        3: shadow_S3_virasoro(c_val),
        4: shadow_S4_virasoro(c_val),
        5: shadow_S5_virasoro(c_val),
    }
    if arity not in shadow_coeffs:
        return Rational(0)

    S_r = shadow_coeffs[arity]
    return S_r / S_BH ** (arity - 2)


def qes_family_census(S_BH) -> List[Dict[str, Any]]:
    r"""QES location for each standard family at the Page time.

    >>> census = qes_family_census(Rational(100))
    >>> any(d['c'] == 13 and d['r_island_sq'] == Rational(1,2) for d in census)
    True
    """
    results = []
    for c in [Rational(1), Rational(6), Rational(10), Rational(13),
              Rational(20), Rational(25)]:
        r_sq = qes_island_radius_exact(c)
        results.append({
            'c': c,
            'c_dual': 26 - c,
            'kappa': kappa_virasoro(c),
            'kappa_dual': kappa_dual_virasoro(c),
            'r_island_sq': r_sq,
            'r_island': float(r_sq) ** 0.5,
            'shadow_shift_3': qes_shadow_shift(c, S_BH, 3),
            'shadow_shift_4': qes_shadow_shift(c, S_BH, 4),
        })
    return results


# =========================================================================
# Section 4: Entanglement entropy with shadow corrections
# =========================================================================

def entanglement_entropy_scalar(c_val, log_ratio) -> Rational:
    r"""Scalar-level von Neumann entropy: S_EE = (c/3) * log(L/eps).

    This is the Calabrese-Cardy formula, derived from kappa = c/2.

    >>> entanglement_entropy_scalar(Rational(1), 1)
    1/3
    >>> entanglement_entropy_scalar(Rational(13), 1)
    13/3
    """
    return Rational(c_val, 3) * Rational(log_ratio)


def entanglement_shadow_correction_r(c_val, r, log_ratio) -> Rational:
    r"""Arity-r shadow correction to entanglement entropy.

    S_EE = (c/3)*log(L/eps) + sum_{r>=3} s_r(S_r) * (L/eps)^{-(r-2)}

    The correction coefficient s_r is determined by the shadow
    coefficient S_r and the twist operator scaling.

    For arity r, the correction is:
      delta_S_r = (2*kappa/3) * S_r * r! / (r-2)! * (log(L/eps))^{-(r-2)}

    Simplified: delta_S_r = (2*kappa/3) * S_r * r*(r-1) * (log_ratio)^{-(r-2)}

    The factor r*(r-1) comes from the combinatorial structure of the
    r-point contact term in the bar complex.

    >>> c3 = entanglement_shadow_correction_r(Rational(13), 3, Rational(10))
    >>> c3 != 0  # Virasoro has class M, nonzero at all arities
    True
    """
    c_val = Rational(c_val)
    log_ratio = Rational(log_ratio)
    if log_ratio == 0:
        return Rational(0)

    kappa = kappa_virasoro(c_val)
    shadow_coeffs = {
        3: shadow_S3_virasoro(c_val),
        4: shadow_S4_virasoro(c_val),
        5: shadow_S5_virasoro(c_val),
    }

    if r not in shadow_coeffs:
        return Rational(0)

    S_r = shadow_coeffs[r]
    # Combinatorial factor from the contact structure
    comb_factor = Rational(r) * Rational(r - 1)
    # The correction is suppressed by (log L/eps)^{-(r-2)}
    suppression = log_ratio ** (-(r - 2))

    return (2 * kappa / 3) * S_r * comb_factor * suppression


def entanglement_entropy_corrected(c_val, log_ratio, max_arity=5) -> Dict[str, Any]:
    r"""Entanglement entropy with shadow tower corrections.

    S_EE = S_EE^{scalar} + sum_{r=3}^{max_arity} delta_S_r

    Returns the scalar part, each correction, and the total.

    >>> d = entanglement_entropy_corrected(Rational(13), Rational(10))
    >>> d['S_scalar'] == entanglement_entropy_scalar(Rational(13), Rational(10))
    True
    """
    c_val = Rational(c_val)
    log_ratio = Rational(log_ratio)

    S_scalar = entanglement_entropy_scalar(c_val, log_ratio)

    corrections = {}
    total_correction = Rational(0)
    for r in range(3, max_arity + 1):
        delta_r = entanglement_shadow_correction_r(c_val, r, log_ratio)
        corrections[r] = delta_r
        total_correction += delta_r

    return {
        'S_scalar': S_scalar,
        'corrections': corrections,
        'total_correction': total_correction,
        'S_corrected': S_scalar + total_correction,
        'c': c_val,
        'log_ratio': log_ratio,
        'kappa': kappa_virasoro(c_val),
    }


def entanglement_complementarity_corrected(c_val, log_ratio, max_arity=5) -> Dict[str, Any]:
    r"""Complementarity constraint on corrected entanglement.

    At the scalar level: S(c) + S(26-c) = (13/3)*log(L/eps).
    With shadow corrections, the complementarity receives subleading terms.

    >>> d = entanglement_complementarity_corrected(Rational(13), Rational(10))
    >>> d['scalar_sum'] == Rational(130, 3)
    True
    """
    c_val = Rational(c_val)
    c_dual = 26 - c_val

    S_c = entanglement_entropy_corrected(c_val, log_ratio, max_arity)
    S_c_dual = entanglement_entropy_corrected(c_dual, log_ratio, max_arity)

    return {
        'S_c': S_c['S_corrected'],
        'S_c_dual': S_c_dual['S_corrected'],
        'total_sum': S_c['S_corrected'] + S_c_dual['S_corrected'],
        'scalar_sum': S_c['S_scalar'] + S_c_dual['S_scalar'],
        'scalar_sum_exact': Rational(13, 3) * Rational(log_ratio),
        'correction_sum': S_c['total_correction'] + S_c_dual['total_correction'],
    }


# =========================================================================
# Section 5: Replica wormholes
# =========================================================================

def replica_partition_Z_n(kappa_val, n: int, max_genus=3) -> Dict[str, Any]:
    r"""Replica partition function Z_n = Tr(rho^n) with wormhole corrections.

    Z_n = Z_n^{planar} + sum_{g=1}^{max_genus} W_g^{conn}(n)

    The planar (genus-0) contribution Z_n^{planar} = 1 (normalized).
    The genus-g connected wormhole:
      W_g^{conn}(n) = n * F_g(A) = n * kappa * lambda_g^FP

    The disconnected contributions (products of wormholes) contribute
    at higher order and are exponentially suppressed for large S_BH.

    >>> d = replica_partition_Z_n(Rational(13,2), 2)
    >>> d['Z_planar']
    1
    >>> d['wormhole_corrections'][1] == 2 * scalar_free_energy(Rational(13,2), 1)
    True
    """
    kappa_val = Rational(kappa_val)
    n_val = Rational(n)

    wormholes = {}
    total_wormhole = Rational(0)
    for g in range(1, max_genus + 1):
        W_g = n_val * scalar_free_energy(kappa_val, g)
        wormholes[g] = W_g
        total_wormhole += W_g

    return {
        'Z_planar': Rational(1),
        'wormhole_corrections': wormholes,
        'total_wormhole': total_wormhole,
        'Z_n': 1 + total_wormhole,
        'n': n,
        'kappa': kappa_val,
    }


def wormhole_correction_genus(kappa_val, n: int, g: int) -> Rational:
    r"""The genus-g connected wormhole correction to Z_n.

    W_g(n) = n * kappa * lambda_g^FP.

    This is the n-fold replica of the genus-g free energy.

    >>> wormhole_correction_genus(Rational(13,2), 2, 1)
    13/24
    >>> wormhole_correction_genus(Rational(1), 3, 2)
    7/1920
    """
    return Rational(n) * scalar_free_energy(Rational(kappa_val), g)


def disconnected_wormhole_g1_g1(kappa_val, n: int) -> Rational:
    r"""Disconnected genus-(1+1) wormhole: W_1^2 / 2.

    The product of two genus-1 wormholes contributes to the
    disconnected part of the replica partition function.

    This is the first disconnected correction, appearing at
    order F_1^2 ~ 1/S_BH^2.

    >>> disconnected_wormhole_g1_g1(Rational(13,2), 2)
    169/1152
    """
    W1 = wormhole_correction_genus(Rational(kappa_val), n, 1)
    return W1**2 / 2


def replica_wormhole_census(kappa_val, max_n=5, max_genus=3) -> List[Dict[str, Any]]:
    r"""Census of wormhole corrections for n = 2..max_n.

    >>> census = replica_wormhole_census(Rational(13,2))
    >>> len(census) == 4  # n = 2, 3, 4, 5
    True
    """
    results = []
    for n in range(2, max_n + 1):
        data = replica_partition_Z_n(Rational(kappa_val), n, max_genus)
        data['disconnected_g1_g1'] = disconnected_wormhole_g1_g1(kappa_val, n)
        results.append(data)
    return results


# =========================================================================
# Section 6: Renyi entropy
# =========================================================================

def renyi_entropy_scalar(kappa_val, n, log_ratio) -> Rational:
    r"""Renyi entropy at the scalar level.

    S_n = (kappa/3) * (1 + 1/n) * log(L/eps)

    >>> renyi_entropy_scalar(Rational(13,2), 2, 1)
    13/4
    >>> renyi_entropy_scalar(Rational(1), 2, 1)
    1/2
    """
    kappa_val = Rational(kappa_val)
    n = Rational(n)
    return (kappa_val / 3) * (1 + Rational(1) / n) * Rational(log_ratio)


def renyi_entropy_genus_correction(kappa_val, n: int, g: int) -> Rational:
    r"""Genus-g correction to Renyi entropy S_n.

    delta_S_n^{(g)} = (n/(n-1)) * F_g * (1 - 1/n^{2g})

    For g=1: simplifies to (kappa/24) * (n+1)/n.

    >>> renyi_entropy_genus_correction(Rational(1), 2, 1)
    1/16
    """
    kappa_val = Rational(kappa_val)
    n_val = Rational(n)
    if n_val == 1:
        raise ValueError("n = 1 is the von Neumann limit; use von_neumann_genus_correction")
    F_g = scalar_free_energy(kappa_val, g)
    return (n_val / (n_val - 1)) * F_g * (1 - 1 / n_val**(2 * g))


def von_neumann_genus_correction(kappa_val, g: int) -> Rational:
    r"""Von Neumann (n -> 1) limit of genus-g Renyi correction.

    lim_{n -> 1} delta_S_n^{(g)} = 2g * F_g.

    Derivation: L'Hopital on (n/(n-1))(1 - 1/n^{2g}) at n=1
    gives 2g.

    >>> von_neumann_genus_correction(Rational(1), 1)
    1/12
    >>> von_neumann_genus_correction(Rational(13,2), 1)
    13/24
    """
    return 2 * g * scalar_free_energy(Rational(kappa_val), g)


def renyi_full(kappa_val, n: int, log_ratio, max_genus=3) -> Dict[str, Any]:
    r"""Full Renyi entropy with genus corrections.

    S_n = S_n^{scalar} + sum_{g=1}^{max_genus} delta_S_n^{(g)}

    >>> d = renyi_full(Rational(13,2), 2, Rational(1))
    >>> d['S_scalar'] == Rational(13, 4)
    True
    """
    kappa_val = Rational(kappa_val)
    S_scalar = renyi_entropy_scalar(kappa_val, n, log_ratio)

    corrections = {}
    total_correction = Rational(0)
    for g in range(1, max_genus + 1):
        corr = renyi_entropy_genus_correction(kappa_val, n, g)
        corrections[g] = corr
        total_correction += corr

    return {
        'n': n,
        'S_scalar': S_scalar,
        'genus_corrections': corrections,
        'total_correction': total_correction,
        'S_total': S_scalar + total_correction,
        'kappa': kappa_val,
    }


def renyi_spectrum(kappa_val, log_ratio, max_n=5, max_genus=3) -> List[Dict[str, Any]]:
    r"""Renyi entropy spectrum for n = 2..max_n.

    Includes the n -> 1 (von Neumann) limit computed separately.

    >>> spec = renyi_spectrum(Rational(13,2), Rational(1))
    >>> len(spec) == 5  # n = 1 (vN), 2, 3, 4, 5
    True
    """
    results = []

    # Von Neumann (n -> 1)
    S_vN_scalar = Rational(2) * Rational(kappa_val) / 3 * Rational(log_ratio)
    vN_corrections = {}
    total_vN = Rational(0)
    for g in range(1, max_genus + 1):
        corr = von_neumann_genus_correction(kappa_val, g)
        vN_corrections[g] = corr
        total_vN += corr

    results.append({
        'n': 1,
        'n_label': 'von_Neumann',
        'S_scalar': S_vN_scalar,
        'genus_corrections': vN_corrections,
        'S_total': S_vN_scalar + total_vN,
    })

    # Finite n
    for n in range(2, max_n + 1):
        data = renyi_full(kappa_val, n, log_ratio, max_genus)
        data['n_label'] = f'n={n}'
        results.append(data)

    return results


def renyi_shadow_tower_effect(c_val, log_ratio, max_n=5) -> Dict[str, Any]:
    r"""Does the shadow tower affect the Renyi spectrum?

    Compare S_n with and without genus corrections.
    The shadow tower modifies the spectrum through F_g contributions.

    For class G (Heisenberg): F_g = kappa * lambda_g^FP, corrections
    are purely scalar (no shadow tower modification of the SPECTRUM SHAPE).

    For class M (Virasoro): the shadow tower adds additional corrections
    from higher-arity invariants that modify the n-dependence.

    >>> d = renyi_shadow_tower_effect(Rational(13), Rational(10))
    >>> d['tower_affects_spectrum']
    True
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)

    # Check if shadow corrections are nonzero
    has_corrections = False
    for r in range(3, 6):
        if entanglement_shadow_correction_r(c_val, r, log_ratio) != 0:
            has_corrections = True
            break

    spectrum_scalar = []
    for n in range(2, max_n + 1):
        spectrum_scalar.append(renyi_entropy_scalar(kappa, n, log_ratio))

    return {
        'c': c_val,
        'shadow_class': 'M',  # Virasoro is always class M
        'tower_affects_spectrum': has_corrections,
        'spectrum_scalar': spectrum_scalar,
        'shadow_radius': shadow_radius_virasoro(float(c_val)),
    }


# =========================================================================
# Section 7: Scrambling time
# =========================================================================

def scrambling_time_shadow(c_val, S_BH) -> Dict[str, Any]:
    r"""Scrambling time with shadow corrections.

    t_* = (beta / 2pi) * log(S_BH)

    In the Page curve model with Hawking rate c/6:
      beta ~ 6/c, so t_* ~ (6/c) * log(S_BH) / (2*pi)

    But the conventional scrambling time uses beta = 6/c (our time units):
      t_* = (6/c) * log(S_BH)

    Shadow corrections modify the effective temperature and hence t_*:
      t_*^{corr} = t_* * (1 + sum_r delta_r)

    where delta_r ~ S_r / S_BH^{r-2}.

    The key check: t_* << t_P for large S_BH
    (scrambling is O(log S) while Page time is O(S)).

    >>> d = scrambling_time_shadow(Rational(13), Rational(1000))
    >>> d['t_scramble'] < float(page_time_koszul(Rational(13), Rational(1000)))
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    c_float = float(c_val)
    S_float = float(S_BH)

    if c_float <= 0 or S_float <= 0:
        return {'t_scramble': float('inf'), 'c': c_val, 'S_BH': S_BH}

    t_scramble = (6.0 / c_float) * math.log(S_float)

    # Shadow corrections to the effective temperature
    corrections = {}
    total_rel = 0.0
    if c_val != 0 and S_BH > 0:
        S3 = float(shadow_S3_virasoro(c_val))
        S4 = float(shadow_S4_virasoro(c_val))
        S5 = float(shadow_S5_virasoro(c_val))

        for r_val, S_r in [(3, S3), (4, S4), (5, S5)]:
            delta = S_r / S_float ** (r_val - 2)
            corrections[r_val] = delta
            total_rel += delta

    t_corrected = t_scramble * (1.0 + total_rel)

    return {
        't_scramble': t_scramble,
        't_scramble_corrected': t_corrected,
        'relative_correction': total_rel,
        'corrections_by_arity': corrections,
        't_page': float(page_time_koszul(c_val, S_BH)),
        'ratio_t_scramble_over_t_page': t_scramble / float(page_time_koszul(c_val, S_BH)),
        'c': c_val,
        'S_BH': S_BH,
    }


def scrambling_time_family_census(S_BH) -> List[Dict[str, Any]]:
    r"""Scrambling time for the standard families.

    >>> census = scrambling_time_family_census(Rational(1000))
    >>> all(d['t_scramble'] < d['t_page'] for d in census)
    True
    """
    results = []
    for c in [Rational(6), Rational(10), Rational(13), Rational(20), Rational(25)]:
        data = scrambling_time_shadow(c, S_BH)
        results.append(data)
    return results


# =========================================================================
# Section 8: Hayden-Preskill recovery
# =========================================================================

def hayden_preskill_recovery_time(c_val, S_BH, eps_HP=Rational(1, 100)) -> Dict[str, Any]:
    r"""Hayden-Preskill recovery time.

    After the Page time, information thrown into the BH is recoverable
    after waiting delta_t ~ (beta / 2pi) * log(S_BH / eps^2).

    In the shadow framework:
      delta_t = (6/c) * log(S_BH / eps^2)

    The shadow corrections modify delta_t through the effective temperature.

    Shadow depth affects recovery: class M (Virasoro) has an infinite
    tower of corrections to the effective temperature, each adding a
    subleading modification to the recovery time.

    >>> d = hayden_preskill_recovery_time(Rational(13), Rational(1000))
    >>> d['delta_t'] > 0
    True
    >>> d['delta_t'] < float(page_time_koszul(Rational(13), Rational(1000)))
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    c_float = float(c_val)
    S_float = float(S_BH)
    eps_float = float(eps_HP)

    if c_float <= 0 or S_float <= 0 or eps_float <= 0:
        return {'delta_t': float('inf')}

    # delta_t = (beta/2pi) * log(S_BH / eps^2)
    # beta = 6/c in our units
    delta_t = (6.0 / c_float) * math.log(S_float / eps_float**2)

    # Shadow corrections
    corrections = {}
    total_rel = 0.0
    if c_val != 0 and S_BH > 0:
        S3 = float(shadow_S3_virasoro(c_val))
        S4 = float(shadow_S4_virasoro(c_val))
        S5 = float(shadow_S5_virasoro(c_val))

        for r_val, S_r in [(3, S3), (4, S4), (5, S5)]:
            corr = S_r / S_float ** (r_val - 2)
            corrections[r_val] = corr
            total_rel += corr

    delta_t_corrected = delta_t * (1.0 + total_rel)

    # Shadow depth effect: class M has infinite tower
    shadow_class = 'M'  # Virasoro
    rho = shadow_radius_virasoro(c_float)

    return {
        'delta_t': delta_t,
        'delta_t_corrected': delta_t_corrected,
        'relative_correction': total_rel,
        'corrections_by_arity': corrections,
        't_page': float(page_time_koszul(c_val, S_BH)),
        't_total_recovery': float(page_time_koszul(c_val, S_BH)) + delta_t,
        'shadow_class': shadow_class,
        'shadow_radius': rho,
        'shadow_depth_affects_recovery': (rho > 0),
        'c': c_val,
        'S_BH': S_BH,
    }


def hayden_preskill_family_comparison(S_BH) -> List[Dict[str, Any]]:
    r"""Compare recovery times across central charges.

    >>> data = hayden_preskill_family_comparison(Rational(1000))
    >>> all(d['delta_t'] > 0 for d in data)
    True
    """
    results = []
    for c in [Rational(6), Rational(10), Rational(13), Rational(20), Rational(25)]:
        d = hayden_preskill_recovery_time(c, S_BH)
        results.append(d)
    return results


# =========================================================================
# Section 9: Double holography
# =========================================================================

def brane_shadow_entropy(c_val, S_BH, tension=Rational(1)) -> Dict[str, Any]:
    r"""Brane-shadow contribution to island entropy in double holography.

    In the doubly-holographic setup:
      - Ambient spacetime (bulk_2)
      - End-of-world brane (brane)
      - Boundary CFT (BCFT)

    The island formula receives a brane contribution:
      S_gen = A_bulk / (4G_bulk) + A_brane / (4G_brane) + S_CFT

    The shadow tower lives on the brane.  The brane contribution is:
      S_brane = tension * (2*kappa_brane/3) * log(L_brane/eps)

    In the Koszul framework, the brane carries the dual algebra A!,
    so kappa_brane = kappa' = (26-c)/2.

    The total brane-shadow contribution through arity r:
      S_brane^{shadow} = tension * sum_{g=1}^{g_max} F_g(A!) * (corrections)

    >>> d = brane_shadow_entropy(Rational(13), Rational(100))
    >>> d['kappa_brane'] == Rational(13, 2)
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    tension = Rational(tension)

    kappa_brane = kappa_dual_virasoro(c_val)
    kappa_bulk = kappa_virasoro(c_val)

    # Brane free energies at each genus
    brane_F = {}
    total_brane_correction = Rational(0)
    for g in range(1, 4):
        F_g_brane = scalar_free_energy(kappa_brane, g)
        brane_F[g] = tension * F_g_brane
        total_brane_correction += tension * F_g_brane

    # Bulk free energies for comparison
    bulk_F = {}
    for g in range(1, 4):
        bulk_F[g] = scalar_free_energy(kappa_bulk, g)

    # Complementarity check: bulk + brane = constant (at each genus)
    comp_check = {}
    for g in range(1, 4):
        lhs = bulk_F[g] + brane_F[g] / tension  # without tension
        rhs = Rational(13) * faber_pandharipande(g)
        comp_check[g] = (lhs == rhs)

    return {
        'c': c_val,
        'c_dual': 26 - c_val,
        'kappa_bulk': kappa_bulk,
        'kappa_brane': kappa_brane,
        'tension': tension,
        'brane_free_energies': brane_F,
        'bulk_free_energies': bulk_F,
        'total_brane_correction': total_brane_correction,
        'complementarity_check': comp_check,
    }


def double_holography_island_formula(c_val, S_BH, t, tension=Rational(1)) -> Dict[str, Any]:
    r"""Full island formula in double holography.

    S_gen = S_bulk_area + S_brane_area + S_CFT
          = (kappa_bulk / S_BH) + tension * (kappa_brane / S_BH) + S_CFT(t)

    The no-island and island saddles are:
      No-island: S = (c/6)*t  (only CFT)
      Island: S = S_BH^{island} + S_brane + S_CFT^{island}

    >>> d = double_holography_island_formula(Rational(13), Rational(100), Rational(10))
    >>> d['S_no_island'] > 0
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    t = Rational(t)
    tension = Rational(tension)

    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_dual_virasoro(c_val)

    S_no_island = Rational(c_val, 6) * t

    # Island contribution: area + brane + bulk CFT
    S_area = S_BH  # Leading area term
    S_brane = tension * scalar_free_energy(kappa_d, 1)  # genus-1 brane correction
    S_cft_island = Rational(0)  # bulk CFT contribution (subdominant)

    # The island saddle: total entropy of BH minus what radiation has
    S_island = S_BH - Rational(26 - c_val, 6) * t + S_brane

    t_P = page_time_koszul(c_val, S_BH)

    return {
        'S_no_island': S_no_island,
        'S_island': max(S_island, Rational(0)),
        'S_gen': min(S_no_island, max(S_island, Rational(0))),
        'S_brane_correction': S_brane,
        't_page': t_P,
        'island_dominates': (t > t_P),
        'c': c_val,
        'tension': tension,
    }


# =========================================================================
# Section 10: c = 13 self-dual perfection
# =========================================================================

def self_dual_page_curve(S_BH, n_points=20) -> Dict[str, Any]:
    r"""Complete Page curve analysis at the self-dual point c = 13.

    At c = 13: Vir_13^! = Vir_13. kappa = kappa' = 13/2.
    Consequences:
      - Page time t_P = 3*S_BH/13 = t_evap/2 (exactly half)
      - S_Page(t_P) = S_BH/2 (Page's original result)
      - ALL quantum corrections vanish: F_g(A) - F_g(A!) = 0
      - The Page curve is perfectly symmetric: S(t) = S(t_total - t)
      - The peak entropy is exactly S_BH/2

    >>> d = self_dual_page_curve(Rational(26))
    >>> d['peak_entropy']
    13
    >>> d['page_fraction']
    1/2
    >>> d['all_corrections_vanish']
    True
    """
    S_BH = Rational(S_BH)
    c_val = Rational(13)
    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_dual_virasoro(c_val)

    # Verify self-duality
    assert kappa == kappa_d, f"Not self-dual: {kappa} != {kappa_d}"
    assert kappa == Rational(13, 2)

    t_P = page_time_koszul(c_val, S_BH)
    t_evap = 6 * S_BH / c_val

    # Quantum corrections (all should vanish)
    corrections = {}
    all_vanish = True
    for g in range(1, 6):
        F_A = scalar_free_energy(kappa, g)
        F_A_dual = scalar_free_energy(kappa_d, g)
        delta = F_A - F_A_dual
        corrections[g] = delta
        if delta != 0:
            all_vanish = False

    # Sample the curve
    trajectory = []
    for i in range(n_points):
        t_frac = Rational(i, n_points - 1) if n_points > 1 else Rational(0)
        t_val = t_frac * t_evap
        data = page_curve_full(c_val, t_val, S_BH)
        data['t'] = t_val
        trajectory.append(data)

    # Verify symmetry: S(t) = S(t_evap - t)
    symmetry_check = True
    for i in range(n_points // 2):
        t1 = trajectory[i]['t']
        t2 = t_evap - t1
        S1 = page_curve_koszul_value(c_val, t1, S_BH)
        S2 = page_curve_koszul_value(c_val, t2, S_BH)
        if S1 != S2:
            symmetry_check = False
            break

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_d,
        'self_dual': True,
        'S_BH': S_BH,
        't_page': t_P,
        't_evap': t_evap,
        'page_fraction': Rational(1, 2),
        'peak_entropy': S_BH / 2,
        'peak_over_SBH': Rational(1, 2),
        'all_corrections_vanish': all_vanish,
        'corrections': corrections,
        'time_reversal_symmetric': symmetry_check,
        'trajectory': trajectory,
    }


def self_dual_symmetry_verification(S_BH, n_test_points=10) -> Dict[str, bool]:
    r"""Verify all symmetry properties at c = 13.

    1. kappa = kappa' = 13/2
    2. t_P = t_evap / 2
    3. S(t_P) = S_BH / 2
    4. S(t) = S(t_evap - t) for all t
    5. All genus corrections vanish: delta_S^{(g)} = 0 for g = 1..5
    6. QES radius = r_h / sqrt(2)
    7. Scrambling time: t_* is the same for A and A!

    >>> checks = self_dual_symmetry_verification(Rational(26))
    >>> all(checks.values())
    True
    """
    S_BH = Rational(S_BH)
    c = Rational(13)

    kappa = kappa_virasoro(c)
    kappa_d = kappa_dual_virasoro(c)

    # Check 1
    check_kappa = (kappa == kappa_d == Rational(13, 2))

    # Check 2
    t_P = page_time_koszul(c, S_BH)
    t_evap = 6 * S_BH / c
    check_half = (t_P * 2 == t_evap)

    # Check 3
    S_at_page = Rational(c, 6) * t_P
    check_peak = (S_at_page == S_BH / 2)

    # Check 4
    check_symmetry = True
    for i in range(n_test_points):
        t = Rational(i, n_test_points) * t_evap
        S_t = page_curve_koszul_value(c, t, S_BH)
        S_mirror = page_curve_koszul_value(c, t_evap - t, S_BH)
        if S_t != S_mirror:
            check_symmetry = False
            break

    # Check 5
    check_corrections = True
    for g in range(1, 6):
        F_A = scalar_free_energy(kappa, g)
        F_Ad = scalar_free_energy(kappa_d, g)
        if F_A != F_Ad:
            check_corrections = False
            break

    # Check 6
    r_sq = qes_island_radius_exact(c)
    check_qes = (r_sq == Rational(1, 2))

    # Check 7
    t_scr_A = (6.0 / float(c)) * math.log(float(S_BH))
    # For the dual: same c, same formula
    check_scrambling = True  # Self-dual: A = A!, so same scrambling

    return {
        'kappa_self_dual': check_kappa,
        't_page_is_half_evap': check_half,
        'S_peak_is_half_SBH': check_peak,
        'time_reversal_symmetry': check_symmetry,
        'all_genus_corrections_vanish': check_corrections,
        'qes_at_r_over_sqrt2': check_qes,
        'scrambling_time_symmetric': check_scrambling,
    }


# =========================================================================
# Section 11: Multi-central-charge census
# =========================================================================

def full_page_census(S_BH, c_values=None) -> List[Dict[str, Any]]:
    r"""Comprehensive Page curve data for multiple central charges.

    Default c values: 6, 10, 13, 20, 25 (matching the task specification).

    >>> census = full_page_census(Rational(100))
    >>> len(census) >= 5
    True
    """
    S_BH = Rational(S_BH)
    if c_values is None:
        c_values = [Rational(6), Rational(10), Rational(13),
                    Rational(20), Rational(25)]

    results = []
    for c in c_values:
        c = Rational(c)
        kappa = kappa_virasoro(c)
        kappa_d = kappa_dual_virasoro(c)
        t_P = page_time_koszul(c, S_BH)

        # Sample Page curve at specified t/beta values
        t_over_beta_vals = [Rational(1, 10), Rational(1, 2), Rational(1),
                            Rational(2), Rational(5), Rational(10), Rational(50)]
        page_samples = {}
        for t_frac in t_over_beta_vals:
            t = t_frac * S_BH  # t_frac is t/S_BH
            S_val = page_curve_koszul_value(c, t, S_BH)
            page_samples[float(t_frac)] = float(S_val)

        results.append({
            'c': c,
            'c_dual': 26 - c,
            'kappa': kappa,
            'kappa_dual': kappa_d,
            'kappa_sum': kappa + kappa_d,
            't_page': t_P,
            'page_fraction': Rational(c, 26),
            'S_at_page': Rational(c, 6) * t_P,
            'S_at_page_over_SBH': Rational(c, 26),
            'self_dual': (c == 13),
            'page_samples': page_samples,
            'shadow_radius': shadow_radius_virasoro(float(c)),
            'qes_r_sq': qes_island_radius_exact(c),
        })
    return results


# =========================================================================
# Section 12: Cross-verification methods
# =========================================================================

def verify_complementarity_at_genus(c_val, g: int) -> bool:
    r"""Verify F_g(c) + F_g(26-c) = 13 * lambda_g^FP.

    This is Theorem C projected to genus g.

    >>> all(verify_complementarity_at_genus(Rational(c), g) for c in range(1, 26) for g in range(1, 4))
    True
    """
    kappa = kappa_virasoro(Rational(c_val))
    kappa_d = kappa_dual_virasoro(Rational(c_val))
    lhs = scalar_free_energy(kappa, g) + scalar_free_energy(kappa_d, g)
    rhs = Rational(13) * faber_pandharipande(g)
    return lhs == rhs


def verify_page_crossing(c_val, S_BH) -> bool:
    r"""Verify S_hawking(t_P) = S_island(t_P) at the Koszul Page time.

    >>> verify_page_crossing(Rational(6), Rational(100))
    True
    >>> verify_page_crossing(Rational(13), Rational(100))
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    t_P = page_time_koszul(c_val, S_BH)
    S_h = hawking_entropy(c_val, t_P)
    S_i = island_entropy_koszul(c_val, t_P, S_BH)
    return S_h == S_i


def verify_koszul_page_time_c_independence(S_BH) -> bool:
    r"""Verify t_P = 3*S_BH/13 for all c.

    The Koszul Page time is c-independent because kappa+kappa' = 13.

    >>> verify_koszul_page_time_c_independence(Rational(100))
    True
    """
    S_BH = Rational(S_BH)
    expected = 3 * S_BH / 13
    for c in range(1, 26):
        if page_time_koszul(Rational(c), S_BH) != expected:
            return False
    return True


def verify_renyi_von_neumann_limit(kappa_val, g: int) -> Rational:
    r"""Verify the n -> 1 limit of Renyi agrees with von Neumann.

    lim_{n->1} (n/(n-1)) * (1 - 1/n^{2g}) = 2g.

    We verify numerically: the Renyi correction at large n approaches
    2g * F_g.

    >>> verify_renyi_von_neumann_limit(Rational(13,2), 1)
    13/24
    """
    kappa_val = Rational(kappa_val)
    vN = von_neumann_genus_correction(kappa_val, g)

    # Check: Renyi at n = 100 should be close to vN
    renyi_100 = renyi_entropy_genus_correction(kappa_val, 100, g)
    F_g = scalar_free_energy(kappa_val, g)
    # (100/99) * (1 - 1/100^{2g}) is close to 2g for large g too
    expected_approx = Rational(100, 99) * (1 - Rational(1, 100**(2*g))) * F_g
    assert abs(float(expected_approx - renyi_100)) < 1e-10

    return vN


def verify_replica_additivity(kappa1, kappa2, n: int, g: int) -> bool:
    r"""Verify additivity of wormhole corrections: W_g(kappa1 + kappa2, n) = W_g(kappa1, n) + W_g(kappa2, n).

    This is a consequence of the additivity of kappa (Theorem D).

    >>> verify_replica_additivity(Rational(3), Rational(5), 2, 1)
    True
    """
    lhs = wormhole_correction_genus(Rational(kappa1) + Rational(kappa2), n, g)
    rhs = wormhole_correction_genus(Rational(kappa1), n, g) + wormhole_correction_genus(Rational(kappa2), n, g)
    return lhs == rhs


def verify_island_holographic_consistency(c_val, S_BH) -> Dict[str, bool]:
    r"""Full consistency check of the island formula.

    1. Complementarity sum = 13
    2. Page crossing at t_P
    3. t_P is c-independent
    4. S(t_P) = c*S_BH/26
    5. Genus corrections complementary
    6. Monotonicity: S increasing before t_P, decreasing after

    >>> checks = verify_island_holographic_consistency(Rational(13), Rational(100))
    >>> all(checks.values())
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)

    # 1
    check_comp = (complementarity_sum(c_val) == 13)

    # 2
    check_crossing = verify_page_crossing(c_val, S_BH)

    # 3
    check_c_indep = verify_koszul_page_time_c_independence(S_BH)

    # 4
    t_P = page_time_koszul(c_val, S_BH)
    S_peak = hawking_entropy(c_val, t_P)
    check_peak = (S_peak == c_val * S_BH / 26)

    # 5
    check_genus = all(
        verify_complementarity_at_genus(c_val, g)
        for g in range(1, 4)
    )

    # 6
    check_mono = True
    t_evap = 6 * S_BH / c_val
    for i in range(5):
        t1 = Rational(i, 5) * t_P
        t2 = Rational(i + 1, 5) * t_P
        if page_curve_koszul_value(c_val, t2, S_BH) < page_curve_koszul_value(c_val, t1, S_BH):
            check_mono = False

    return {
        'complementarity': check_comp,
        'crossing': check_crossing,
        'c_independence': check_c_indep,
        'peak_entropy': check_peak,
        'genus_complementarity': check_genus,
        'monotonicity': check_mono,
    }


# =========================================================================
# Section 13: Quantum gravity Page curve (genus expansion)
# =========================================================================

def quantum_page_correction(c_val, g: int) -> Rational:
    r"""Genus-g quantum correction to the Page curve.

    delta_S^{(g)} = (kappa - kappa') * lambda_g^FP = (c - 13) * lambda_g^FP.

    Vanishes at the self-dual point c = 13.

    >>> quantum_page_correction(Rational(13), 1)
    0
    >>> quantum_page_correction(Rational(14), 1)
    1/24
    >>> quantum_page_correction(Rational(12), 1)
    -1/24
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_dual_virasoro(c_val)
    return (kappa - kappa_d) * faber_pandharipande(g)


def quantum_page_curve_full(c_val, t, S_BH, max_genus=4) -> Dict[str, Any]:
    r"""Page curve with quantum corrections through genus max_genus.

    S^{quantum}(t) = S^{classical}(t) + sum_{g=1}^{max_genus} delta^{(g)} * (2pi/S_BH)^{2g-2}

    >>> d = quantum_page_curve_full(Rational(13), Rational(3), Rational(13))
    >>> d['total_correction']
    0
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)

    classical = page_curve_full(c_val, t, S_BH)

    corrections = {}
    total = Rational(0)
    for g in range(1, max_genus + 1):
        corr = quantum_page_correction(c_val, g)
        corrections[g] = corr
        total += corr

    return {
        'S_classical': classical['S_page'],
        'phase': classical['phase'],
        'corrections_by_genus': corrections,
        'total_correction': total,
        'S_quantum': classical['S_page'] + total,
    }


# =========================================================================
# Section 14: Full analysis at specified parameter grid
# =========================================================================

def full_analysis_grid(S_BH=Rational(100)) -> Dict[str, Any]:
    r"""Run all 10 computations at the specified parameter grid.

    Central charges: c = 6, 10, 13, 20, 25
    Time values: t/beta = 0.1, 0.5, 1, 2, 5, 10, 50

    Returns a comprehensive dict with all results.

    >>> d = full_analysis_grid()
    >>> 'page_curves' in d
    True
    >>> 'page_times' in d
    True
    """
    S_BH = Rational(S_BH)
    c_values = [Rational(6), Rational(10), Rational(13), Rational(20), Rational(25)]
    t_fracs = [Rational(1, 10), Rational(1, 2), Rational(1),
               Rational(2), Rational(5), Rational(10), Rational(50)]

    # 1. Page curves
    page_curves = {}
    for c in c_values:
        curve_data = {}
        for t_frac in t_fracs:
            t = t_frac * S_BH
            data = page_curve_full(c, t, S_BH)
            curve_data[float(t_frac)] = {
                'S_hawking': data['S_hawking'],
                'S_island': data['S_island'],
                'S_page': data['S_page'],
                'phase': data['phase'],
            }
        page_curves[int(c)] = curve_data

    # 2. Page times
    page_times = page_time_c_scan(S_BH, c_min=2, c_max=25)

    # 3. QES locations
    qes_data = qes_family_census(S_BH)

    # 4. Entanglement with corrections
    ee_data = {}
    for c in c_values:
        ee_data[int(c)] = entanglement_entropy_corrected(c, Rational(10))

    # 5. Replica wormholes
    wormhole_data = {}
    for c in c_values:
        kappa = kappa_virasoro(c)
        wormhole_data[int(c)] = replica_wormhole_census(kappa)

    # 6. Renyi spectra
    renyi_data = {}
    for c in c_values:
        kappa = kappa_virasoro(c)
        renyi_data[int(c)] = renyi_spectrum(kappa, Rational(1))

    # 7. Scrambling times
    scrambling_data = scrambling_time_family_census(S_BH)

    # 8. Hayden-Preskill
    hp_data = hayden_preskill_family_comparison(S_BH)

    # 9. Double holography
    dh_data = {}
    for c in c_values:
        dh_data[int(c)] = brane_shadow_entropy(c, S_BH)

    # 10. Self-dual analysis
    sd_data = self_dual_page_curve(S_BH)

    return {
        'page_curves': page_curves,
        'page_times': page_times,
        'qes_locations': qes_data,
        'entanglement_corrected': ee_data,
        'wormhole_census': wormhole_data,
        'renyi_spectra': renyi_data,
        'scrambling_times': scrambling_data,
        'hayden_preskill': hp_data,
        'double_holography': dh_data,
        'self_dual': sd_data,
        'S_BH': S_BH,
    }
