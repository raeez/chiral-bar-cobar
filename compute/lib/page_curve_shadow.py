r"""Page curve and island formula from modular Koszul duality.

MATHEMATICAL FRAMEWORK
======================

The Page curve describes the von Neumann entropy of Hawking radiation
as a function of time.  In the modular Koszul framework, the Page
transition is a direct consequence of COMPLEMENTARITY (Theorem C):
the Koszul duality A <-> A! exchanges the dominant saddle at the
Page time.

For the Virasoro algebra at central charge c:
  - Matter side: kappa(Vir_c) = c/2
  - Radiation (Koszul dual) side: kappa(Vir_{26-c}) = (26-c)/2
  - The Koszul dual central charge c' = 26 - c.

The complementarity sum kappa + kappa' = 13 (AP24: NOT zero for
Virasoro) provides the total Bekenstein-Hawking entropy.

CENTRAL RESULTS
===============

1. HAWKING PHASE (t < t_P):
   S_rad(t) = (c/6) * t
   From kappa = c/2 and the entanglement growth rate (c/6) per unit time.

2. ISLAND PHASE (t > t_P):
   S_rad(t) = S_BH - ((26-c)/6) * (t - t_P)
   Uses the Koszul dual kappa' = (26-c)/2.

3. PAGE TIME:
   t_P = 3 * S_BH / 13
   From the crossing condition S_Hawking(t_P) = S_island(t_P).

4. PAGE CURVE:
   S_Page(t) = min(S_Hawking(t), S_island(t))
   This min is the genus-1 projection of the complementarity formula
   (Theorem C): Q_g(A) + Q_g(A!) = H*(M_g, Z(A)).

5. GENERALIZED ENTROPY (island formula):
   S_gen = (Area)/(4 G_N) + S_bulk = kappa * lambda_1 + S_bulk
   The island appears when the bar complex B(A!) dominates B(A).

6. QUANTUM CORRECTIONS at genus g >= 2:
   delta_S_Page^{(g)} from F_g(A) = kappa * lambda_g^FP.
   The quantum Page curve includes subleading 1/S_BH^{2g-2} corrections.

7. REPLICA WORMHOLES:
   The connected contribution to Tr(rho^n) involves the shadow
   amplitude at genus g * n.  Renyi entropy S_n at each genus,
   with the von Neumann limit n -> 1.

8. SELF-DUAL POINT c = 13:
   kappa = kappa' = 13/2.  The Page time is exactly half the
   evaporation time.  Perfect A <-> A! symmetry.

MATHEMATICAL INTEGRITY NOTES
=============================

- The time parameter t is dimensionless (measured in units of the
  scrambling time).  The physical Page time depends on c, S_BH,
  and the black hole mass.

- S_BH is an input (the initial Bekenstein-Hawking entropy), NOT
  derived from the shadow obstruction tower.  The shadow obstruction tower provides the
  QUANTUM CORRECTIONS to S_BH, not S_BH itself.

- The "island formula" language is adopted from Penington (1905.08255)
  and AEMM (1908.10996, 1911.11977).  In the present framework, the
  island is the region where the Koszul dual bar complex B(A!)
  provides the dominant contribution.

- The entanglement wedge boundary is determined by the quantum
  extremal surface (QES) condition, which in the shadow framework
  is a Ward identity of the shadow connection (nabla^sh).

- AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
- AP8: Virasoro self-dual at c = 13, NOT c = 26.
- AP20: kappa(A) is an invariant of A; kappa_eff = kappa(matter) + kappa(ghost)
  is a different object.  We use kappa(A) throughout.

References:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
  Page 1993 (hep-th/9306083): average entropy of a subsystem
  Penington 2019 (1905.08255): entanglement wedge reconstruction
  AEMM 2019 (1908.10996, 1911.11977): island formula
  Calabrese-Cardy 2005 (hep-th/0503001): entanglement evolution
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand, factor,
    factorial, log, oo, pi, S, simplify, sqrt, symbols,
)

# ---------------------------------------------------------------------------
# Imports from existing engines
# ---------------------------------------------------------------------------

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_wN,
    von_neumann_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
    shadow_depth_class,
    shadow_radius_virasoro,
    entanglement_correction_bound,
    renyi_entropy_scalar,
)

from compute.lib.complementarity_landscape import (
    complementarity_sum_wn,
)


# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
t_sym = Symbol('t', nonnegative=True)


# =========================================================================
# Section 1: Koszul dual data
# =========================================================================

def kappa_dual_virasoro(c_val) -> Rational:
    r"""Koszul dual modular characteristic for Virasoro.

    kappa(Vir_{26-c}) = (26 - c) / 2.

    The Koszul duality is c -> 26 - c (Feigin-Frenkel for Virasoro).

    >>> kappa_dual_virasoro(Rational(1))
    25/2
    >>> kappa_dual_virasoro(Rational(13))
    13/2
    >>> kappa_dual_virasoro(Rational(26))
    0
    """
    c_val = Rational(c_val)
    return Rational(26 - c_val, 2)


def complementarity_sum_virasoro(c_val) -> Rational:
    r"""Complementarity sum kappa(c) + kappa(26-c) = 13.

    This is a CONSTANT independent of c (AP24).
    For Virasoro: c/2 + (26-c)/2 = 13.

    >>> complementarity_sum_virasoro(Rational(1))
    13
    >>> complementarity_sum_virasoro(Rational(13))
    13
    >>> complementarity_sum_virasoro(Rational(25))
    13
    """
    return kappa_virasoro(c_val) + kappa_dual_virasoro(c_val)


def dual_central_charge(c_val) -> Rational:
    r"""Koszul dual central charge for Virasoro: c' = 26 - c.

    >>> dual_central_charge(Rational(1))
    25
    >>> dual_central_charge(Rational(13))
    13
    """
    return Rational(26) - Rational(c_val)


# =========================================================================
# Section 2: Hawking phase and growth rates
# =========================================================================

def hawking_rate(c_val) -> Rational:
    r"""Hawking radiation entropy growth rate.

    dS_rad/dt = c / 6  (in units where t is dimensionless scrambling time).

    This is the Calabrese-Cardy growth rate for entanglement after a
    local quench, reinterpreted as Hawking radiation production.

    The factor c/6 = kappa/3 comes from the twist operator dimension
    at n = 1:  d/dn [h_n]|_{n=1} = c/12, and the Renyi derivative gives
    the coefficient c/6 in the linear growth regime.

    >>> hawking_rate(Rational(6))
    1
    >>> hawking_rate(Rational(12))
    2
    >>> hawking_rate(Rational(1))
    1/6
    """
    return Rational(c_val, 6)


def island_rate(c_val) -> Rational:
    r"""Island phase entropy decrease rate.

    dS_rad/dt = -(26 - c) / 6   (decreasing after Page time).

    Uses the Koszul dual kappa' = (26 - c)/2 in the island formula.

    >>> island_rate(Rational(1))
    -25/6
    >>> island_rate(Rational(13))
    -13/6
    >>> island_rate(Rational(25))
    -1/6
    """
    return -Rational(26 - Rational(c_val), 6)


def hawking_entropy(c_val, t, S_BH=None) -> Rational:
    r"""Hawking phase radiation entropy.

    S_Hawking(t) = (c/6) * t

    Valid for t < t_P.  If S_BH is provided, caps at S_BH.

    >>> hawking_entropy(Rational(6), Rational(3))
    3
    >>> hawking_entropy(Rational(12), Rational(1))
    2
    """
    c_val = Rational(c_val)
    t = Rational(t)
    result = Rational(c_val, 6) * t
    if S_BH is not None:
        S_BH = Rational(S_BH)
        result = min(result, S_BH)
    return result


def island_entropy(c_val, t, S_BH) -> Rational:
    r"""Island phase radiation entropy (Koszul model).

    In the Koszul-dual Page curve model, the island channel uses the
    dual rate kappa' = (26 - c)/2, giving:

      S_island(t) = S_BH - ((26 - c) / 6) * t

    This equals the Hawking entropy S_hawk(t) = (c/6)*t at the Koszul
    Page time t_P = 3*S_BH/13, where both equal c*S_BH/26.

    The key identity: the crossing time is c-independent because
    kappa + kappa' = 13 (AP24 for Virasoro).

    >>> S_BH = Rational(26)
    >>> t_P = page_time_koszul(Rational(6), S_BH)
    >>> island_entropy(Rational(6), t_P, S_BH) == hawking_entropy(Rational(6), t_P)
    True
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)
    return S_BH - Rational(26 - c_val, 6) * t


# =========================================================================
# Section 3: Page time
# =========================================================================

def page_time(c_val, S_BH) -> Rational:
    r"""Page time: when the Hawking curve crosses the island curve.

    At t_P:
      S_Hawking(t_P) = S_island(t_P)
      (c/6) * t_P = S_BH - ((26-c)/6) * (t_P - t_P) = S_BH - 0

    Wait, that is wrong.  Let us derive carefully.

    The island entropy at time t is modeled as the total BH entropy
    minus the entropy of radiation already emitted by the island channel:

      S_island(t) = S_BH - ((26-c)/6) * t   ... NO.

    The correct setup: the Hawking computation gives S_rad growing as
    (c/6)*t.  The island computation gives S_rad = S_BH - S_remaining,
    where S_remaining is the entropy still in the black hole.  If the
    BH loses entropy at rate (26-c)/6 from the dual perspective:

      S_island(t) = S_BH - ((26-c)/6) * (t - 0)  ?

    This is not right either.  The standard Page curve setup:

    - S_Hawking(t) = (c/6) * t      [linearly growing, Hawking computation]
    - S_island(t) = S_BH - (c/6) * t  [the unitary bound: total entropy
      minus what the radiation already has]

    In the STANDARD information paradox, the island entropy uses the
    SAME rate c/6 but subtracted from S_BH.  The Koszul duality
    interpretation modifies this: the island uses kappa' = (26-c)/2
    instead of kappa = c/2.  But the simplest and most physically
    correct model is:

    - No-island (Hawking): S_Hawking(t) = (c/6) * t
    - With island: S_island(t) = S_BH - (c/6) * t

    The crossing gives t_P = 3 * S_BH / c.

    For the Koszul-dual interpretation where the island channel uses
    the dual rate:
    - S_island(t) = S_BH - ((26-c)/6) * t

    The crossing gives (c/6)*t_P = S_BH - ((26-c)/6)*t_P
    => (c + 26 - c)/6 * t_P = S_BH
    => t_P = 6 * S_BH / 26 = 3 * S_BH / 13.

    We implement BOTH models:
    - page_time: the standard Page curve (same rate both sides)
    - page_time_koszul: the Koszul-dual model (different rates)

    This function returns the STANDARD Page time: t_P = 3 * S_BH / c.

    >>> page_time(Rational(6), Rational(13))
    13/2
    >>> page_time(Rational(13), Rational(13))
    3
    >>> page_time(Rational(26), Rational(13))
    3/2
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    if c_val == 0:
        raise ValueError("c = 0: no Hawking radiation")
    return 3 * S_BH / c_val


def page_time_koszul(c_val, S_BH) -> Rational:
    r"""Koszul-dual Page time.

    The Hawking channel uses kappa = c/2, the island channel uses
    kappa' = (26 - c)/2.  At the crossing:

      (c/6) * t_P = S_BH - ((26 - c)/6) * t_P
      => (c + 26 - c)/6 * t_P = S_BH
      => t_P = 6 * S_BH / 26 = 3 * S_BH / 13

    This is INDEPENDENT of c (the complementarity sum kappa + kappa' = 13
    absorbs the c dependence).

    At the self-dual point c = 13: the standard and Koszul Page times
    coincide: 3 * S_BH / 13.

    >>> page_time_koszul(Rational(6), Rational(13))
    3
    >>> page_time_koszul(Rational(1), Rational(13))
    3
    >>> page_time_koszul(Rational(25), Rational(13))
    3
    >>> page_time_koszul(Rational(13), Rational(13))
    3
    """
    S_BH = Rational(S_BH)
    return 3 * S_BH / 13


def evaporation_time(c_val, S_BH) -> Rational:
    r"""Total evaporation time: when S_Hawking(t) = S_BH.

    t_evap = 6 * S_BH / c.

    >>> evaporation_time(Rational(6), Rational(13))
    13
    >>> evaporation_time(Rational(13), Rational(13))
    6
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    if c_val == 0:
        raise ValueError("c = 0: no evaporation")
    return 6 * S_BH / c_val


def page_time_fraction(c_val) -> Rational:
    r"""Ratio t_P / t_evap for the standard Page curve.

    t_P / t_evap = (3*S_BH/c) / (6*S_BH/c) = 1/2.

    The Page time is always exactly half the evaporation time
    in the standard model (same rate for both channels).

    >>> page_time_fraction(Rational(6))
    1/2
    >>> page_time_fraction(Rational(13))
    1/2
    """
    return Rational(1, 2)


def page_time_fraction_koszul(c_val) -> Rational:
    r"""Ratio t_P / t_evap for the Koszul model.

    t_P_K = 3 * S_BH / 13.
    t_evap = 6 * S_BH / c.
    Ratio = (3/13) / (6/c) = c / 26.

    At c = 13: ratio = 1/2 (agrees with standard).
    At c < 13: ratio < 1/2 (Page time earlier — radiation dominates).
    At c > 13: ratio > 1/2 (Page time later — BH dominates).

    >>> page_time_fraction_koszul(Rational(13))
    1/2
    >>> page_time_fraction_koszul(Rational(26))
    1
    >>> page_time_fraction_koszul(Rational(1))
    1/26
    """
    return Rational(c_val, 26)


# =========================================================================
# Section 4: Page curve (full trajectory)
# =========================================================================

def page_curve_value(c_val, t, S_BH) -> Rational:
    r"""The Page curve: S_Page(t) = min(S_Hawking(t), S_island(t)).

    Standard model (same rate both channels):
      S_Hawking(t) = (c/6) * t
      S_island(t) = S_BH - (c/6) * t
      S_Page(t) = min of the two.

    >>> S_BH = Rational(13)
    >>> page_curve_value(Rational(6), Rational(0), S_BH)
    0
    >>> page_curve_value(Rational(6), Rational(100), S_BH)  # past evaporation
    0
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)
    S_hawk = Rational(c_val, 6) * t
    S_island = S_BH - Rational(c_val, 6) * t
    # Physical constraint: entropy is non-negative
    S_hawk = max(S_hawk, Rational(0))
    S_island = max(S_island, Rational(0))
    return min(S_hawk, S_island)


def page_curve_koszul(c_val, t, S_BH) -> Dict[str, Any]:
    r"""Koszul-dual Page curve with full phase information.

    Hawking channel: S_H(t) = (c/6) * t      [uses kappa = c/2]
    Island channel:  S_I(t) = S_BH - ((26-c)/6) * t  [uses kappa' = (26-c)/2]

    The crossing point is at t_P = 3 * S_BH / 13 (c-independent).

    Returns dict with:
      S_hawking, S_island, S_page (the min), phase, t_page.

    >>> data = page_curve_koszul(Rational(13), Rational(3), Rational(13))
    >>> data['phase']
    'page_point'
    >>> data['S_page']
    13/2
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)

    S_hawk = Rational(c_val, 6) * t
    S_island = S_BH - Rational(26 - c_val, 6) * t

    # Clamp to physical range
    S_hawk = max(S_hawk, Rational(0))
    S_island = max(S_island, Rational(0))

    t_P = page_time_koszul(c_val, S_BH)

    if t < t_P:
        phase = 'hawking'
        S_page = S_hawk
    elif t > t_P:
        phase = 'island'
        S_page = S_island
    else:
        phase = 'page_point'
        S_page = S_hawk  # they agree at crossing

    return {
        'S_hawking': S_hawk,
        'S_island': S_island,
        'S_page': S_page,
        'phase': phase,
        't_page': t_P,
        'c': c_val,
        'c_dual': 26 - c_val,
    }


def page_entropy_at_transition(c_val, S_BH) -> Rational:
    r"""Entropy at the Page time.

    Standard model: S_Page(t_P) = S_BH / 2.
    Koszul model: S_Page(t_P) = (c/6) * (3*S_BH/13) = c*S_BH / 26.

    >>> page_entropy_at_transition(Rational(13), Rational(26))
    13
    >>> page_entropy_at_transition(Rational(6), Rational(26))
    6
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    t_P = page_time_koszul(c_val, S_BH)
    return Rational(c_val, 6) * t_P


def page_entropy_fraction(c_val) -> Rational:
    r"""Ratio S_Page(t_P) / S_BH for the Koszul model.

    S_Page(t_P) / S_BH = c / 26.

    At c = 13: 1/2 (Page's original result for equal-size subsystems).
    At c < 13: < 1/2 (the matter algebra has less entropy).
    At c > 13: > 1/2 (the matter algebra has more entropy).

    >>> page_entropy_fraction(Rational(13))
    1/2
    >>> page_entropy_fraction(Rational(26))
    1
    >>> page_entropy_fraction(Rational(1))
    1/26
    """
    return Rational(c_val, 26)


# =========================================================================
# Section 5: Page curve trajectory (sampled)
# =========================================================================

def page_curve_trajectory(c_val, S_BH, n_points=20) -> List[Dict[str, Any]]:
    r"""Sample the Koszul Page curve at n_points evenly spaced times.

    Returns list of dicts with t, S_hawking, S_island, S_page, phase.

    >>> traj = page_curve_trajectory(Rational(13), Rational(13), n_points=5)
    >>> len(traj) == 5
    True
    >>> traj[0]['S_page'] == 0
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    # Sample from t = 0 to t = 6*S_BH/(26-c) (when island hits zero),
    # or t_evap = 6*S_BH/c (when hawking hits S_BH), whichever is larger.
    c_dual = 26 - c_val
    if c_dual > 0:
        t_max_island = 6 * S_BH / c_dual
    else:
        t_max_island = 6 * S_BH  # large fallback
    t_max = max(evaporation_time(c_val, S_BH), t_max_island)

    trajectory = []
    for i in range(n_points):
        t_frac = Rational(i, n_points - 1) if n_points > 1 else Rational(0)
        t_val = t_frac * t_max
        data = page_curve_koszul(c_val, t_val, S_BH)
        data['t'] = t_val
        trajectory.append(data)
    return trajectory


# =========================================================================
# Section 6: Generalized entropy (island formula)
# =========================================================================

def generalized_entropy(kappa_val, area_over_4G, S_bulk) -> Rational:
    r"""Generalized entropy: S_gen = Area/(4G_N) + S_bulk.

    In the modular Koszul framework:
      Area/(4G_N) = kappa * lambda_1 * (geometric factor)

    At the scalar level, kappa * lambda_1 = kappa / 24 = F_1.

    For a black hole of initial entropy S_BH:
      S_gen = S_BH + S_bulk    (no-island saddle)
      S_gen = S_BH^{island} + S_bulk^{island}  (island saddle)

    Here we just compute the sum.

    >>> generalized_entropy(Rational(13, 2), Rational(10), Rational(3))
    13
    """
    return Rational(area_over_4G) + Rational(S_bulk)


def island_dominance_condition(kappa_val, kappa_dual, t, S_BH) -> Dict[str, Any]:
    r"""Determine whether the island saddle dominates.

    No-island: S_gen^{no-island} = (2*kappa/3) * t  [Hawking growth]
    Island: S_gen^{island} = S_BH - (2*kappa'/3) * t

    The island dominates when S_gen^{island} < S_gen^{no-island},
    i.e., when t > t_P = 3*S_BH/(kappa + kappa').

    For Virasoro: kappa + kappa' = 13, so t_P = 3*S_BH/13.

    >>> data = island_dominance_condition(Rational(13,2), Rational(13,2), Rational(4), Rational(13))
    >>> data['island_dominates']
    True
    """
    kappa_val = Rational(kappa_val)
    kappa_dual = Rational(kappa_dual)
    t = Rational(t)
    S_BH = Rational(S_BH)

    S_no_island = (2 * kappa_val / 3) * t
    S_island = S_BH - (2 * kappa_dual / 3) * t

    kappa_sum = kappa_val + kappa_dual
    if kappa_sum > 0:
        t_P = 3 * S_BH / kappa_sum
    else:
        t_P = Rational(0)

    return {
        'S_no_island': S_no_island,
        'S_island': max(S_island, Rational(0)),
        'S_gen': min(S_no_island, max(S_island, Rational(0))),
        'island_dominates': t > t_P,
        't_page': t_P,
        'kappa_sum': kappa_sum,
    }


# =========================================================================
# Section 7: Quantum corrections to the Page curve
# =========================================================================

def quantum_page_correction_genus(c_val, g: int) -> Rational:
    r"""Genus-g quantum correction to the Page curve.

    delta_S^{(g)} = F_g(A) - F_g(A!)
                  = kappa * lambda_g^FP - kappa' * lambda_g^FP
                  = (kappa - kappa') * lambda_g^FP
                  = (c - 13) * lambda_g^FP

    This vanishes at the self-dual point c = 13.

    At genus 1: delta_S^{(1)} = (c - 13) / 24.
    At genus 2: delta_S^{(2)} = 7 * (c - 13) / 5760.

    >>> quantum_page_correction_genus(Rational(13), 1)
    0
    >>> quantum_page_correction_genus(Rational(14), 1)
    1/24
    >>> quantum_page_correction_genus(Rational(12), 1)
    -1/24
    """
    c_val = Rational(c_val)
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_dual_virasoro(c_val)
    return (kappa - kappa_dual) * faber_pandharipande(g)


def quantum_page_curve_value(c_val, t, S_BH, max_genus=3) -> Dict[str, Any]:
    r"""Page curve with quantum corrections through genus max_genus.

    The quantum-corrected Page curve includes subleading terms:

    S_Page^{quantum}(t) = S_Page^{classical}(t) + sum_{g=1}^{max_genus} delta^{(g)}

    where delta^{(g)} is the genus-g correction.

    The corrections are in units of 1/S_BH^{2g-2} relative to the
    classical term, so they are perturbatively small for large S_BH.

    Returns dict with classical and corrected values.

    >>> data = quantum_page_curve_value(Rational(13), Rational(3), Rational(13))
    >>> data['total_correction']
    0
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)

    classical = page_curve_koszul(c_val, t, S_BH)
    corrections = {}
    total_corr = Rational(0)
    for g in range(1, max_genus + 1):
        corr_g = quantum_page_correction_genus(c_val, g)
        corrections[g] = corr_g
        total_corr += corr_g

    return {
        'classical': classical['S_page'],
        'corrections': corrections,
        'total_correction': total_corr,
        'quantum_page': classical['S_page'] + total_corr,
        'phase': classical['phase'],
    }


def complementarity_correction_sum(c_val, g: int) -> Rational:
    r"""Complementarity identity for quantum corrections.

    F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g^FP.

    This is Theorem C at the scalar level, at genus g.

    >>> complementarity_correction_sum(Rational(1), 1)
    13/24
    >>> complementarity_correction_sum(Rational(13), 1)
    13/24
    >>> complementarity_correction_sum(Rational(25), 2) == Rational(13) * faber_pandharipande(2)
    True
    """
    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_dual_virasoro(c_val)
    return (kappa + kappa_d) * faber_pandharipande(g)


# =========================================================================
# Section 8: Replica wormholes
# =========================================================================

def replica_partition_function_genus(kappa_val, n: int, g: int) -> Rational:
    r"""Genus-g contribution to Tr(rho^n).

    The replica partition function Z_n at genus g is:
      Z_n^{(g)} proportional to exp(-n * F_g(A))

    The genus-g Renyi entropy gets a contribution:
      delta_S_n^{(g)} = (1/(1-n)) * n * F_g(A) * (1 - 1/n^{2g})

    At the scalar level: F_g = kappa * lambda_g^FP.

    For g = 1: F_1 = kappa / 24.

    We return the exponent n * F_g(A).

    >>> replica_partition_function_genus(Rational(13, 2), 2, 1)
    13/24
    >>> replica_partition_function_genus(Rational(1, 2), 3, 1)
    1/16
    """
    kappa_val = Rational(kappa_val)
    n = Rational(n)
    return n * scalar_free_energy(kappa_val, g)


def renyi_entropy_genus_correction(kappa_val, n: int, g: int) -> Rational:
    r"""Genus-g correction to the Renyi entropy S_n.

    The full Renyi entropy is:
      S_n = S_n^{scalar} + sum_{g >= 1} delta_S_n^{(g)}

    The genus-g correction to the Renyi entropy arises from the
    genus-g free energy and its replica scaling:

      delta_S_n^{(g)} = (n/(n-1)) * F_g * (1 - 1/n^{2g})  for n != 1.

    At genus 1: delta_S_n^{(1)} = (n/(n-1)) * (kappa/24) * (1 - 1/n^2)
              = (kappa/24) * (n+1)/n * (1/1)  ... let me be careful.

    Actually: (n/(n-1)) * (1 - 1/n^2) = (n/(n-1)) * (n^2-1)/n^2
            = (n/(n-1)) * (n-1)(n+1)/n^2 = (n+1)/n.

    So delta_S_n^{(1)} = (kappa/24) * (n+1)/n.

    In the von Neumann limit n -> 1: delta_S_1^{(1)} = kappa/12.

    >>> renyi_entropy_genus_correction(Rational(1), 2, 1)
    1/16
    """
    kappa_val = Rational(kappa_val)
    n_val = Rational(n)
    F_g = scalar_free_energy(kappa_val, g)
    if n_val == 1:
        raise ValueError("Use von Neumann formula for n = 1")
    factor = (n_val / (n_val - 1)) * (1 - 1 / n_val**(2 * g))
    return F_g * factor


def von_neumann_genus_correction(kappa_val, g: int) -> Rational:
    r"""Von Neumann (n -> 1) limit of the genus-g correction.

    lim_{n -> 1} delta_S_n^{(g)} = 2g * F_g(A).

    Derivation: as n -> 1, (n/(n-1))(1 - 1/n^{2g}) ~ 2g.
    (L'Hopital: d/dn [1 - n^{-2g}] / d/dn [1 - 1/n] at n=1
     = 2g * n^{-2g-1} / n^{-2} = 2g.)

    At genus 1: 2 * F_1 = 2 * kappa/24 = kappa/12.
    At genus 2: 4 * F_2 = 4 * 7*kappa/5760 = 7*kappa/1440.

    >>> von_neumann_genus_correction(Rational(1), 1)
    1/12
    >>> von_neumann_genus_correction(Rational(13, 2), 1)
    13/24
    """
    kappa_val = Rational(kappa_val)
    F_g = scalar_free_energy(kappa_val, g)
    return 2 * g * F_g


def replica_wormhole_connected(kappa_val, n: int, g: int) -> Rational:
    r"""Connected replica wormhole contribution at genus g.

    The connected n-replica wormhole at genus g contributes to
    Tr(rho^n) a factor proportional to:

      W_{g,n}^{conn} = kappa * lambda_g^FP * n

    This is the simplest (genus-g, n-replica) connected amplitude.
    The full amplitude includes disconnected contributions
    (products of lower-genus wormholes).

    >>> replica_wormhole_connected(Rational(13, 2), 2, 1)
    13/24
    >>> replica_wormhole_connected(Rational(1), 3, 2)
    7/1920
    """
    kappa_val = Rational(kappa_val)
    n = Rational(n)
    return kappa_val * faber_pandharipande(g) * n


# =========================================================================
# Section 9: Entanglement wedge from Koszul duality
# =========================================================================

def entanglement_wedge_boundary(c_val, t, S_BH) -> Dict[str, Any]:
    r"""Entanglement wedge boundary as a function of time.

    In the bar-cobar framework, the entanglement wedge is the spacetime
    region where B(A) dominates over B(A!).  The boundary of this region
    moves as the Page transition progresses.

    Before the Page time: the wedge is empty (no island).
    After the Page time: the wedge appears and grows.

    The wedge radius (in units of the AdS radius) is:

      r_wedge(t) = 0                    for t < t_P
      r_wedge(t) = sqrt(1 - S_BH(t)/S_BH(0))  for t > t_P

    where S_BH(t) is the remaining BH entropy at time t.

    For the Koszul model:
      S_BH(t) = S_BH - (c/6)*t  (the BH loses entropy at the Hawking rate).

    >>> data = entanglement_wedge_boundary(Rational(13), Rational(0), Rational(13))
    >>> data['has_island']
    False
    """
    c_val = Rational(c_val)
    t = Rational(t)
    S_BH = Rational(S_BH)
    t_P = page_time_koszul(c_val, S_BH)

    if t <= t_P:
        return {
            'has_island': False,
            'r_wedge': Rational(0),
            'S_remaining': S_BH - Rational(c_val, 6) * t,
            't_page': t_P,
        }

    S_remaining = S_BH - Rational(c_val, 6) * t
    S_remaining = max(S_remaining, Rational(0))

    if S_BH > 0:
        fraction_evaporated = 1 - float(S_remaining) / float(S_BH)
        r_wedge = math.sqrt(max(fraction_evaporated, 0.0))
    else:
        r_wedge = 0.0

    return {
        'has_island': True,
        'r_wedge': r_wedge,
        'S_remaining': S_remaining,
        'fraction_evaporated': Rational(S_BH - S_remaining, S_BH) if S_BH > 0 else Rational(0),
        't_page': t_P,
    }


# =========================================================================
# Section 10: Self-dual analysis at c = 13
# =========================================================================

def self_dual_page_analysis(S_BH) -> Dict[str, Any]:
    r"""Complete Page curve analysis at the self-dual point c = 13.

    At c = 13: Vir_13^! = Vir_13 (AP8: self-dual at c = 13, NOT c = 26).
    kappa = kappa' = 13/2.

    Consequences:
    - Page time = half of evaporation time.
    - S_Page(t_P) = S_BH/2 (Page's original result).
    - ALL quantum corrections vanish: F_g(A) - F_g(A!) = 0 for all g.
    - The Page curve is exactly symmetric under time reversal about t_P.

    >>> data = self_dual_page_analysis(Rational(26))
    >>> data['page_entropy']
    13
    >>> data['total_quantum_correction']
    0
    """
    S_BH = Rational(S_BH)
    c_val = Rational(13)
    kappa = kappa_virasoro(c_val)
    t_P = page_time_koszul(c_val, S_BH)
    t_evap = evaporation_time(c_val, S_BH)

    corrections = {}
    total_corr = Rational(0)
    for g in range(1, 6):
        corr = quantum_page_correction_genus(c_val, g)
        corrections[g] = corr
        total_corr += corr

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa,
        'self_dual': True,
        'S_BH': S_BH,
        't_page': t_P,
        't_evap': t_evap,
        'page_entropy': page_entropy_at_transition(c_val, S_BH),
        'page_fraction': page_entropy_fraction(c_val),
        'corrections': corrections,
        'total_quantum_correction': total_corr,
        'symmetry': 'exact time-reversal symmetry about t_P',
    }


# =========================================================================
# Section 11: Multi-central-charge census
# =========================================================================

def page_curve_census(S_BH, c_values=None) -> List[Dict[str, Any]]:
    r"""Page curve data for multiple central charge values.

    Default census values: c = 1, 6, 12, 13, 24, 25.

    >>> census = page_curve_census(Rational(13))
    >>> len(census) >= 6
    True
    >>> any(d['c'] == 13 for d in census)
    True
    """
    S_BH = Rational(S_BH)
    if c_values is None:
        c_values = [Rational(1), Rational(6), Rational(12),
                    Rational(13), Rational(24), Rational(25)]

    results = []
    for c_val in c_values:
        c_val = Rational(c_val)
        kappa = kappa_virasoro(c_val)
        kappa_d = kappa_dual_virasoro(c_val)
        t_P = page_time_koszul(c_val, S_BH)
        t_evap = evaporation_time(c_val, S_BH)
        S_page = page_entropy_at_transition(c_val, S_BH)

        results.append({
            'c': c_val,
            'c_dual': 26 - c_val,
            'kappa': kappa,
            'kappa_dual': kappa_d,
            'kappa_sum': kappa + kappa_d,
            't_page': t_P,
            't_evap': t_evap,
            'page_fraction': page_time_fraction_koszul(c_val),
            'S_page': S_page,
            'S_page_over_S_BH': page_entropy_fraction(c_val),
            'self_dual': (c_val == 13),
            'quantum_correction_g1': quantum_page_correction_genus(c_val, 1),
        })
    return results


# =========================================================================
# Section 12: Consistency checks
# =========================================================================

def verify_page_curve_complementarity(c_val, S_BH) -> Dict[str, bool]:
    r"""Verify all complementarity constraints on the Page curve.

    1. kappa + kappa' = 13
    2. S_Hawking(t_P) = S_island(t_P)  at the Koszul Page time
    3. F_g(c) + F_g(26-c) = 13 * lambda_g^FP for g = 1, ..., 5
    4. Quantum corrections vanish at c = 13

    >>> checks = verify_page_curve_complementarity(Rational(6), Rational(13))
    >>> all(checks.values())
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)

    # Check 1: kappa sum
    kappa_sum_ok = complementarity_sum_virasoro(c_val) == 13

    # Check 2: crossing at t_P
    t_P = page_time_koszul(c_val, S_BH)
    S_hawk_tP = Rational(c_val, 6) * t_P
    S_island_tP = S_BH - Rational(26 - c_val, 6) * t_P
    crossing_ok = (S_hawk_tP == S_island_tP)

    # Check 3: complementarity at each genus
    genus_ok = True
    for g in range(1, 6):
        lhs = complementarity_correction_sum(c_val, g)
        rhs = Rational(13) * faber_pandharipande(g)
        if lhs != rhs:
            genus_ok = False

    # Check 4: self-dual corrections vanish
    selfdual_ok = all(
        quantum_page_correction_genus(Rational(13), g) == 0
        for g in range(1, 6)
    )

    return {
        'kappa_sum': kappa_sum_ok,
        'crossing': crossing_ok,
        'genus_complementarity': genus_ok,
        'self_dual_corrections_vanish': selfdual_ok,
    }


def verify_page_curve_monotonicity(c_val, S_BH) -> bool:
    r"""Verify that the Page curve is monotonically increasing then decreasing.

    The Page curve S_Page(t) should:
    - Increase linearly from 0 to S_BH/2 for t in [0, t_P]
    - Decrease linearly from S_BH/2 back to 0 for t in [t_P, t_evap]

    (In the standard model.  In the Koszul model the peak is at
    c * S_BH / 26, not S_BH / 2, unless c = 13.)

    >>> verify_page_curve_monotonicity(Rational(6), Rational(13))
    True
    >>> verify_page_curve_monotonicity(Rational(13), Rational(26))
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)

    # Sample 10 points and check monotonicity
    t_P = page_time_koszul(c_val, S_BH)
    t_max = max(evaporation_time(c_val, S_BH),
                6 * S_BH / (26 - c_val) if c_val < 26 else 6 * S_BH)

    # Before Page time: increasing
    for i in range(5):
        t1 = Rational(i, 5) * t_P
        t2 = Rational(i + 1, 5) * t_P
        d1 = page_curve_koszul(c_val, t1, S_BH)
        d2 = page_curve_koszul(c_val, t2, S_BH)
        if d2['S_page'] < d1['S_page']:
            return False

    # After Page time: decreasing
    for i in range(5):
        t1 = t_P + Rational(i, 5) * (t_max - t_P)
        t2 = t_P + Rational(i + 1, 5) * (t_max - t_P)
        d1 = page_curve_koszul(c_val, t1, S_BH)
        d2 = page_curve_koszul(c_val, t2, S_BH)
        if d2['S_page'] > d1['S_page']:
            return False

    return True


# =========================================================================
# Section 13: Scrambling time and information retrieval
# =========================================================================

def scrambling_time(c_val, S_BH) -> float:
    r"""Scrambling time: t_scr ~ (6/c) * log(S_BH).

    The scrambling time is the time for a perturbation to become
    thermalized across the black hole.  In the shadow framework,
    it corresponds to the time for the bar complex to fully mix.

    In the Page curve model where the Hawking rate is c/6 per unit time,
    the inverse temperature is beta ~ 6/c (in these time units), so:
      t_scr ~ beta * log(S_BH) / (2*pi) ~ (6/c) * log(S_BH)

    This is O(log S_BH), parametrically smaller than the Page time
    t_P = 3*S_BH/13 which is O(S_BH).

    >>> t = scrambling_time(Rational(13), Rational(1000))
    >>> t > 0
    True
    >>> t < float(page_time_koszul(Rational(13), Rational(1000)))
    True
    """
    c_val = float(c_val)
    S_BH = float(S_BH)
    if c_val <= 0 or S_BH <= 0:
        return float('inf')
    return (6.0 / c_val) * math.log(S_BH)


def information_retrieval_time(c_val, S_BH) -> Rational:
    r"""Time after the Page time at which information starts to be retrievable.

    In the Hayden-Preskill protocol, information thrown into the BH
    after the Page time is retrievable after one scrambling time.

    For our purposes, this is t_P + delta, where delta is small
    relative to t_P.  We return t_P as the leading-order answer.

    >>> information_retrieval_time(Rational(13), Rational(13))
    3
    """
    return page_time_koszul(Rational(c_val), Rational(S_BH))


# =========================================================================
# Section 14: Shadow depth effects on the Page curve
# =========================================================================

def page_curve_shadow_class_analysis(c_val, S_BH) -> Dict[str, Any]:
    r"""Analyze how shadow depth affects the Page curve.

    Class G (Gaussian): Page curve is exact at the scalar level.
    Class L (Lie): one cubic correction.
    Class C (Contact): two corrections (cubic + quartic).
    Class M (Mixed): infinite tower of corrections.

    For Virasoro (always class M), the corrections converge when
    the shadow radius rho < 1, i.e., c > c* ~ 6.125.

    >>> data = page_curve_shadow_class_analysis(Rational(13), Rational(13))
    >>> data['shadow_class']
    'M'
    >>> data['corrections_converge']
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)
    rho = shadow_radius_virasoro(float(c_val))
    converges = rho < 1.0

    # Correction bounds at each arity
    correction_bounds = {}
    for r in range(3, 8):
        correction_bounds[r] = entanglement_correction_bound(rho, r)

    return {
        'c': c_val,
        'shadow_class': 'M',  # Virasoro is always class M
        'shadow_radius': rho,
        'corrections_converge': converges,
        'correction_bounds': correction_bounds,
        'page_time': page_time_koszul(c_val, S_BH),
        'quantum_corrections': {
            g: quantum_page_correction_genus(c_val, g)
            for g in range(1, 4)
        },
    }


# =========================================================================
# Section 15: Full Page curve analysis
# =========================================================================

def full_page_analysis(c_val, S_BH, max_genus=4) -> Dict[str, Any]:
    r"""Complete Page curve analysis for Virasoro at central charge c.

    Returns comprehensive data including:
    - Koszul dual data
    - Page time (standard and Koszul)
    - Entanglement at Page time
    - Quantum corrections through genus max_genus
    - Complementarity verification
    - Shadow depth analysis

    >>> data = full_page_analysis(Rational(13), Rational(26))
    >>> data['self_dual']
    True
    >>> data['complementarity_verified']
    True
    """
    c_val = Rational(c_val)
    S_BH = Rational(S_BH)

    kappa = kappa_virasoro(c_val)
    kappa_d = kappa_dual_virasoro(c_val)

    t_P_std = page_time(c_val, S_BH)
    t_P_K = page_time_koszul(c_val, S_BH)
    t_evap = evaporation_time(c_val, S_BH)

    corrections = {}
    total_corr = Rational(0)
    for g in range(1, max_genus + 1):
        corr = quantum_page_correction_genus(c_val, g)
        corrections[g] = corr
        total_corr += corr

    comp_checks = verify_page_curve_complementarity(c_val, S_BH)

    return {
        'c': c_val,
        'c_dual': 26 - c_val,
        'kappa': kappa,
        'kappa_dual': kappa_d,
        'kappa_sum': kappa + kappa_d,
        'self_dual': (c_val == 13),
        'S_BH': S_BH,
        't_page_standard': t_P_std,
        't_page_koszul': t_P_K,
        't_evaporation': t_evap,
        'page_fraction_koszul': page_time_fraction_koszul(c_val),
        'S_at_page': page_entropy_at_transition(c_val, S_BH),
        'S_at_page_fraction': page_entropy_fraction(c_val),
        'hawking_rate': hawking_rate(c_val),
        'island_rate': island_rate(c_val),
        'quantum_corrections': corrections,
        'total_quantum_correction': total_corr,
        'complementarity_verified': all(comp_checks.values()),
        'complementarity_details': comp_checks,
        'shadow_radius': shadow_radius_virasoro(float(c_val)),
        'shadow_class': 'M',
    }
