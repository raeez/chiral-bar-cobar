r"""BTZ 7-loop finite shadow diagnostics.

CERTIFIED SURFACE
=================

This module extends the finite BTZ shadow diagnostic to genus 7.  The
certified lane is the scalar Bernoulli/A-hat component

    F_g^{scalar}(A) = kappa(A) * lambda_g^FP,

with lambda_g^FP the Faber-Pandharipande integral.  For Virasoro, the
implemented full free-energy window is still only genus 2 and genus 3:
those are the local planted-forest corrections recorded in the base
engine.  The genus 6 and genus 7 Virasoro routines below return scalar
components, not certified full Virasoro planted-forest amplitudes.

The BTZ/Cardy wrappers use external 3d-gravity input.  Finite scalar
coefficients do not certify an exact BTZ partition function, an exact
full-Virasoro convergence radius, Borel summability, all-genus planted
forests, or analytic tau-dependence.

SCALAR VALUES
=============

The exact scalar formula is

    lambda_g^FP =
    ((2^{2g-1}-1)/2^{2g-1}) * |B_{2g}| / (2g)!.

Through genus 7:
  lambda_1 = 1/24
  lambda_2 = 7/5760
  lambda_3 = 31/967680
  lambda_4 = 127/154828800
  lambda_5 = 73/3503554560
  lambda_6 = 1414477/2678117105664000
  lambda_7 = 8191/612141052723200

The scalar A-hat generating function is

    sum_{g>=1} lambda_g^FP x^{2g} = (x/2)/sin(x/2) - 1.

This gives the scalar Taylor radius 2*pi.  It is not a radius theorem for
the full Virasoro planted-forest tower or for the full BTZ partition
function.

LOCAL CONSTANTS
===============

The constants are sourced from the local landscape census:

  kappa(Vir_c) = c/2
  kappa(H_k) = k
  kappa(V_k(g)) = dim(g)(k+h^vee)/(2h^vee)
  S_3(Vir_c) = 2
  S_4(Vir_c) = 10/[c(5c+22)]
  S_5(Vir_c) = -48/[c^2(5c+22)]
  r_H(z) = k/z
  r_KM^{coll}(z) = k Omega_tr/z
  r_KZ(z) = Omega/((k+h^vee)z)
  r_Vir(z) = (c/2)/z^3 + 2T/z

OBJECT FIREWALLS
================

A, B(A), A^i, A^!, and Z_ch^der(A) are distinct objects.  Omega(B(A)) = A
is bar-cobar inversion, not Koszul duality.  A^! is the Verdier/continuous
linear-dual branch.  Hochschild cochains describe the bulk/derived centre,
not the Koszul dual.

References:
  BTZ 1992: hep-th/9204099
  Maloney-Witten 2010: 0712.0155
  chapters/examples/landscape_census.tex
  chapters/connections/concordance.tex
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:theorem-d (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

# Import base engine (do NOT duplicate)
from compute.lib.btz_quantum_gravity_engine import (
    SCALAR_BERNOULLI_LANE,
    VIRASORO_FINITE_WINDOW_LANE,
    EXTERNAL_BTZ_INPUT,
    VIRASORO_PLANTED_FOREST_CERTIFIED_MAX_GENUS,
    lambda_fp,
    _bernoulli_2g,
    _factorial_fraction,
    kappa_virasoro,
    kappa_heisenberg,
    kappa_kac_moody,
    virasoro_S3,
    virasoro_S4,
    virasoro_S5,
    F_g_scalar,
    planted_forest_g2,
    planted_forest_g3,
    virasoro_free_energy,
    heisenberg_free_energy,
    bekenstein_hawking_entropy,
    inverse_hawking_temperature,
    shadow_convergence_radius,
    ahat_closed_form,
    scalar_free_energy_sum,
    free_energy_certification,
    borel_summability_status,
)

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2
BTZ_7LOOP_SCALAR_MAX_GENUS = 7


def object_firewall_status() -> Dict[str, Any]:
    """Object-separation firewall for this diagnostic layer."""
    return {
        'distinct_objects': ['A', 'B(A)', 'A^i', 'A^!', 'Z_ch^der(A)'],
        'bar_cobar_inversion': 'Omega(B(A)) = A',
        'koszul_dual_branch': 'A^! is Verdier/continuous-linear dual data',
        'bulk_branch': 'Z_ch^der(A) is Hochschild/derived-centre data',
        'btz_scalar_lane_uses_only': ['kappa(A)', 'lambda_g^FP'],
    }


def seven_loop_certification(algebra: str = 'virasoro',
                             g_max: int = BTZ_7LOOP_SCALAR_MAX_GENUS) -> Dict[str, Any]:
    """Certification split for the finite genus-7 diagnostic."""
    per_genus = {
        g: free_energy_certification(algebra, g)
        for g in range(1, g_max + 1)
    }

    if algebra == 'heisenberg':
        full_certified_through = g_max
    elif algebra == 'virasoro':
        full_certified_through = min(
            g_max, VIRASORO_PLANTED_FOREST_CERTIFIED_MAX_GENUS
        )
    else:
        full_certified_through = 0

    return {
        'scalar_coefficients_certified_through_genus': g_max,
        'finite_window_lane': VIRASORO_FINITE_WINDOW_LANE,
        'full_free_energy_certified_through_genus': full_certified_through,
        'per_genus': per_genus,
        'scalar_convergence_radius': shadow_convergence_radius(SCALAR_BERNOULLI_LANE),
        'full_virasoro_convergence_radius': shadow_convergence_radius('virasoro_full'),
        'borel_status': borel_summability_status(
            'virasoro_full' if algebra == 'virasoro' else algebra
        ),
        'btz_input_status': EXTERNAL_BTZ_INPUT,
        'closed_form_btz_partition_certified': False,
        'analytic_tau_dependence_certified': False,
        'all_genus_planted_forest_certified': algebra == 'heisenberg',
        'object_firewall': object_firewall_status(),
    }


def _dirichlet_eta_even(g: int) -> float:
    r"""Exact Dirichlet eta function at s=2g (even positive integer).

    eta(s) = (1 - 2^{1-s}) * zeta(s)

    For even positive integers:
      zeta(2g) = |B_{2g}| * (2*pi)^{2g} / (2*(2g)!)

    So eta(2g) = (1 - 2^{1-2g}) * |B_{2g}| * (2*pi)^{2g} / (2*(2g)!)
               = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}| * (2*pi)^{2g} / (2*(2g)!)

    This is EXACT (no series truncation).
    """
    B_2g = _bernoulli_2g(g)
    power = 2 ** (2 * g - 1)
    zeta_2g = float(abs(B_2g)) * TWO_PI ** (2 * g) / (2.0 * math.factorial(2 * g))
    return (1.0 - 2.0 ** (1 - 2 * g)) * zeta_2g


# =========================================================================
# Section 1: Extended Faber-Pandharipande data (g=6, g=7)
# =========================================================================

# Exact hardcoded values, independently computed and verified
LAMBDA_FP_6 = Fraction(1414477, 2678117105664000)
LAMBDA_FP_7 = Fraction(8191, 612141052723200)


def verify_lambda_6_from_bernoulli() -> Fraction:
    r"""Independent computation of lambda_6^FP from B_{12}.

    B_{12} = -691/2730
    lambda_6 = (2^{11}-1)/(2^{11}) * |B_{12}|/12!
             = 2047/2048 * 691/2730 / 479001600
             = 1414477/2678117105664000

    Verification path: Bernoulli number formula.
    """
    B12 = _bernoulli_2g(6)  # B_{12} = -691/2730
    power = 2 ** 11  # 2^{2*6-1} = 2^11 = 2048
    num = (power - 1) * abs(B12)
    den = power * _factorial_fraction(12)
    return num / den


def verify_lambda_7_from_bernoulli() -> Fraction:
    r"""Independent computation of lambda_7^FP from B_{14}.

    B_{14} = 7/6
    lambda_7 = (2^{13}-1)/(2^{13}) * |B_{14}|/14!
             = 8191/8192 * 7/6 / 87178291200
             = 8191/612141052723200

    Verification path: Bernoulli number formula.
    """
    B14 = _bernoulli_2g(7)  # B_{14} = 7/6
    power = 2 ** 13  # 2^{2*7-1} = 2^13 = 8192
    num = (power - 1) * abs(B14)
    den = power * _factorial_fraction(14)
    return num / den


def verify_lambda_6_from_ahat(tol: float = 1e-8) -> Dict[str, Any]:
    r"""Verify lambda_6 from the A-hat generating function.

    A-hat(ix) - 1 = (x/2)/sin(x/2) - 1 = sum_{g>=1} lambda_g x^{2g}

    The coefficient of x^{12} is lambda_6.  We use the Taylor series of
    the A-hat function computed via the known Bernoulli recurrence and
    compare with the closed-form residue extraction.

    Since direct floating-point subtraction at small x suffers from
    catastrophic cancellation (the x^2 term dominates), we instead
    verify via the 7-term series sum against the closed form at moderate x.
    """
    # Use a moderate x where the series has converged but the terms
    # are still numerically distinguishable
    x = 1.0
    ahat_closed = (x / 2.0) / math.sin(x / 2.0) - 1.0

    # Sum the 7-term series
    series_7 = sum(float(lambda_fp(g)) * x ** (2 * g) for g in range(1, 8))

    # The difference is the tail from g >= 8
    tail = ahat_closed - series_7

    # The tail should be small: dominated by lambda_8 * x^16
    # lambda_8 ~ lambda_7 / (2*pi)^2 ~ 3.4e-13
    # So tail ~ 3.4e-13 (since x=1)

    # Verify that including lambda_6 improves the fit
    series_5 = sum(float(lambda_fp(g)) * x ** (2 * g) for g in range(1, 6))
    tail_5 = ahat_closed - series_5

    # tail_5 includes g=6,7,8,... while tail includes g=8,...
    # So tail_5 - tail = lambda_6 * x^12 + lambda_7 * x^14
    lambda_6_contribution = float(LAMBDA_FP_6) * x ** 12

    exact = float(LAMBDA_FP_6)
    # Verify that the series-to-closed-form residual shrinks when we add g=6
    improvement_ratio = abs(tail) / abs(tail_5) if tail_5 != 0 else 0

    return {
        'lambda_6_exact': exact,
        'series_7_at_x1': series_7,
        'closed_form_at_x1': ahat_closed,
        'tail_after_7': tail,
        'tail_after_5': tail_5,
        'improvement': improvement_ratio,
        'relative_error': abs(tail) / abs(ahat_closed) if ahat_closed != 0 else 0,
        'match': improvement_ratio < 0.01,  # 7-term series captures > 99%
    }


def verify_lambda_from_generating_function(g_target: int, g_max: int = 10) -> Dict[str, Any]:
    r"""Verify lambda_g by checking the g_max-term series against the closed form.

    The closed form is (x/2)/sin(x/2) - 1.  The g_max-term series is
    sum_{g=1}^{g_max} lambda_g x^{2g}.  We verify that the two agree
    at a moderate x value to high precision (limited by the tail from g > g_max).

    Direct coefficient extraction via subtraction at small x suffers from
    catastrophic cancellation.  Instead, we verify that the series including
    g_target is much closer to the closed form than the series excluding it.

    Verification path: A-hat generating function consistency.
    """
    x = 1.0  # moderate value for numerical stability

    ahat_closed = (x / 2.0) / math.sin(x / 2.0) - 1.0

    # Series including g_target
    series_with = sum(float(lambda_fp(g)) * x ** (2 * g) for g in range(1, g_max + 1))
    # Series excluding g_target
    series_without = sum(float(lambda_fp(g)) * x ** (2 * g) for g in range(1, g_max + 1) if g != g_target)

    err_with = abs(ahat_closed - series_with)
    err_without = abs(ahat_closed - series_without)

    # The contribution of g_target term
    contribution = float(lambda_fp(g_target)) * x ** (2 * g_target)

    # Check that including g_target brings the series closer to closed form
    # by approximately the size of the g_target term
    improvement = err_without - err_with

    lambda_exact = float(lambda_fp(g_target))

    return {
        'g': g_target,
        'lambda_exact': lambda_exact,
        'contribution': contribution,
        'err_with': err_with,
        'err_without': err_without,
        'improvement': improvement,
        'relative_error': abs(improvement - contribution) / contribution if contribution != 0 else 0,
        'match': abs(improvement - contribution) / contribution < 0.01 if contribution > 0 else False,
    }


# =========================================================================
# Section 2: Extended free energies F_6 and F_7
# =========================================================================

def F_6_scalar(kappa) -> Fraction:
    """F_6^{sc} = kappa * lambda_6^FP.

    For Virasoro: F_6(Vir_c) = (c/2) * 1414477/2678117105664000.
    """
    return Fraction(kappa) * LAMBDA_FP_6


def F_7_scalar(kappa) -> Fraction:
    """F_7^{sc} = kappa * lambda_7^FP.

    For Virasoro: F_7(Vir_c) = (c/2) * 8191/612141052723200.
    """
    return Fraction(kappa) * LAMBDA_FP_7


def virasoro_F6(c) -> Fraction:
    """Scalar genus-6 component for Virasoro.

    The full planted-forest genus-6 Virasoro amplitude is not certified in
    this module.
    """
    return F_6_scalar(kappa_virasoro(c))


def virasoro_F7(c) -> Fraction:
    """Scalar genus-7 component for Virasoro.

    The full planted-forest genus-7 Virasoro amplitude is not certified in
    this module.
    """
    return F_7_scalar(kappa_virasoro(c))


def extended_free_energy_table(c, g_max: int = 7,
                                algebra: str = 'virasoro') -> Dict[int, Fraction]:
    """Finite free-energy table through genus g_max.

    Virasoro uses the base-engine certified planted-forest terms at genus 2
    and genus 3.  Genus 4 and above are scalar Bernoulli components unless
    another algebra lane certifies more.
    """
    table = {}
    for g in range(1, g_max + 1):
        if algebra == 'virasoro':
            if g <= 5:
                table[g] = virasoro_free_energy(c, g)
            elif g == 6:
                table[g] = virasoro_F6(c)
            elif g == 7:
                table[g] = virasoro_F7(c)
            else:
                table[g] = F_g_scalar(kappa_virasoro(c), g)
        elif algebra == 'heisenberg':
            if g <= 5:
                table[g] = heisenberg_free_energy(c, g)
            else:
                table[g] = F_g_scalar(Fraction(c), g)
        else:
            kappa = Fraction(c) / Fraction(2)
            table[g] = F_g_scalar(kappa, g)
    return table


# =========================================================================
# Section 3: 7-loop BTZ partition function
# =========================================================================

def shadow_partition_7loop(c, hbar: float = 1.0,
                            algebra: str = 'virasoro') -> float:
    r"""Finite 7-loop shadow diagnostic.

    Z_7^{sh}(c, hbar) = exp(sum_{g=1}^7 hbar^{2g} F_g).
    This finite exponential is always a polynomial-exponential diagnostic.
    The scalar all-genus A-hat lane has Taylor radius 2*pi; this function
    does not certify the full Virasoro or BTZ radius.
    """
    table = extended_free_energy_table(c, g_max=7, algebra=algebra)
    exponent = sum(hbar ** (2 * g) * float(table[g]) for g in range(1, 8))
    return math.exp(exponent)


def shadow_free_energy_7loop(c, hbar: float = 1.0,
                              algebra: str = 'virasoro') -> float:
    """F^{sh} = sum_{g=1}^7 hbar^{2g} F_g = log Z^{sh}."""
    table = extended_free_energy_table(c, g_max=7, algebra=algebra)
    return sum(hbar ** (2 * g) * float(table[g]) for g in range(1, 8))


# =========================================================================
# Section 4: 6-loop and 7-loop entropy corrections
# =========================================================================

def explicit_6loop_correction(c, M) -> Dict[str, Any]:
    r"""Scalar genus-6 correction in the BTZ saddle expansion.

    F_6 = (c/2) * lambda_6^FP = (c/2) * 1414477/2678117105664000
    S_6 = F_6 * (2*pi/S_BH)^{10}
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    F6_sc = float(F_6_scalar(kappa))
    epsilon = TWO_PI / S_BH if S_BH > 0 else 0.0

    return {
        'S_BH': S_BH,
        'F_6_scalar': F6_sc,
        'F_6_exact': F_6_scalar(kappa),
        'S_6': F6_sc * epsilon ** 10 if S_BH > 0 else 0.0,
        'epsilon': epsilon,
        'epsilon_10': epsilon ** 10 if S_BH > 0 else 0.0,
        'certification': free_energy_certification('virasoro', 6),
        'btz_input_status': EXTERNAL_BTZ_INPUT,
        'note': 'scalar genus-6 BTZ saddle diagnostic',
    }


def explicit_7loop_correction(c, M) -> Dict[str, Any]:
    r"""Scalar genus-7 correction in the BTZ saddle expansion.

    F_7 = (c/2) * lambda_7^FP = (c/2) * 8191/612141052723200
    S_7 = F_7 * (2*pi/S_BH)^{12}
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    F7_sc = float(F_7_scalar(kappa))
    epsilon = TWO_PI / S_BH if S_BH > 0 else 0.0

    return {
        'S_BH': S_BH,
        'F_7_scalar': F7_sc,
        'F_7_exact': F_7_scalar(kappa),
        'S_7': F7_sc * epsilon ** 12 if S_BH > 0 else 0.0,
        'epsilon': epsilon,
        'epsilon_12': epsilon ** 12 if S_BH > 0 else 0.0,
        'certification': free_energy_certification('virasoro', 7),
        'btz_input_status': EXTERNAL_BTZ_INPUT,
        'note': 'scalar genus-7 BTZ saddle diagnostic',
    }


def entropy_correction_7loop(c, M, g: int,
                              algebra: str = 'virasoro') -> float:
    r"""Entropy correction S_g at genus g (extended to g=6,7).

    S_1 = -(3/2)*log(S_BH/(2*pi))   [one-loop logarithmic]
    S_g = F_g * epsilon^{2g-2}       [g >= 2]

    where epsilon = 2*pi/S_BH.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return 0.0

    if g == 1:
        return -1.5 * math.log(S_BH / TWO_PI)

    # Get F_g
    table = extended_free_energy_table(c, g_max=max(g, 7), algebra=algebra)
    Fg = float(table.get(g, F_g_scalar(Fraction(c) / 2, g)))

    epsilon = TWO_PI / S_BH
    return Fg * epsilon ** (2 * g - 2)


# =========================================================================
# Section 5: 7-loop entropy diagnostic
# =========================================================================

def entropy_7loop_full(c, M, algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""BTZ entropy diagnostic through 7 loops.

    S(M) = S_BH + sum_{g=1}^7 S_g

    The Cardy/Bekenstein-Hawking input is external.  For Virasoro, the
    genus-6 and genus-7 terms are scalar Bernoulli components, not certified
    full planted-forest corrections.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return {'error': 'S_BH <= 0: below Cardy threshold'}

    F_table = extended_free_energy_table(c, g_max=7, algebra=algebra)
    epsilon = TWO_PI / S_BH
    kappa = float(Fraction(c) / 2) if algebra == 'virasoro' else float(c)

    result = {
        'c': c,
        'M': M,
        'kappa': kappa,
        'S_BH': S_BH,
        'epsilon': epsilon,
        'F_table': {g: float(f) for g, f in F_table.items()},
        'F_table_exact': {g: f for g, f in F_table.items()},
        'btz_input_status': EXTERNAL_BTZ_INPUT,
        'certification': {
            g: free_energy_certification(algebra, g)
            for g in range(1, 8)
        },
        'seven_loop_certification': seven_loop_certification(algebra, 7),
    }

    total = S_BH
    for g in range(1, 8):
        Sg = entropy_correction_7loop(c, M, g, algebra)
        result[f'S_{g}'] = Sg
        total += Sg

    result['S_total'] = total
    result['relative_correction'] = (total - S_BH) / S_BH if S_BH > 0 else 0.0

    # Scalar Bernoulli/A-hat convergence diagnostic.
    result['convergent'] = abs(epsilon) < TWO_PI
    result['scalar_bernoulli_convergent'] = result['convergent']
    result['convergence_certification'] = SCALAR_BERNOULLI_LANE
    result['full_virasoro_convergence_certified'] = False if algebra == 'virasoro' else None
    result['closed_form_btz_partition_certified'] = False
    result['analytic_tau_dependence_certified'] = False
    result['epsilon_over_2pi'] = epsilon / TWO_PI

    # Decay ratios
    decay_ratios = {}
    for g in range(2, 8):
        Fg_prev = float(F_table[g - 1])
        Fg_curr = float(F_table[g])
        if abs(Fg_prev) > 1e-300:
            decay_ratios[f'{g-1}_to_{g}'] = abs(Fg_curr / Fg_prev)
    result['F_decay_ratios'] = decay_ratios

    return result


# =========================================================================
# Section 6: Convergence analysis at 7 loops
# =========================================================================

def convergence_analysis_7loop(c, M, algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""Finite-loop scalar convergence diagnostics at 7 loops.

    The A-hat closed form and radius are certified only on the scalar
    Bernoulli lane.  For Virasoro, planted-forest data beyond genus 3 is not
    certified, so these fields are diagnostics, not a full convergence proof.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return {'error': 'S_BH <= 0'}

    epsilon = TWO_PI / S_BH
    kappa = float(Fraction(c) / 2) if algebra == 'virasoro' else float(c)
    F_table = extended_free_energy_table(c, g_max=7, algebra=algebra)

    # Scalar A-hat radius condition.
    convergent = abs(epsilon) < TWO_PI

    # Decay ratios vs Bernoulli prediction.
    predicted_ratio = 1.0 / TWO_PI_SQ  # ~0.02533
    actual_ratios = []
    for g in range(2, 8):
        r = abs(float(F_table[g]) / float(F_table[g - 1]))
        actual_ratios.append({
            'g': g,
            'actual': r,
            'predicted': predicted_ratio,
            'error': abs(r - predicted_ratio) / predicted_ratio,
        })

    # Partial sums vs scalar closed form.
    closed_form = ahat_closed_form(c, epsilon) if convergent else None
    partial_sums = []
    running = 0.0
    for g in range(1, 8):
        Fg = float(F_table[g])
        running += Fg * epsilon ** (2 * g)
        partial_sums.append({
            'g': g,
            'partial_sum': running,
            'term': Fg * epsilon ** (2 * g),
        })

    # Entropy correction magnitudes.
    corrections = []
    for g in range(1, 8):
        Sg = entropy_correction_7loop(c, M, g, algebra)
        corrections.append({
            'g': g,
            'S_g': Sg,
            '|S_g|': abs(Sg),
            'S_g_over_S_BH': Sg / S_BH,
        })

    # Tail estimate from the scalar asymptotic ratio.  This is not a
    # certified bound for full Virasoro planted-forest corrections.
    if convergent:
        r_asymp = 1.0 / TWO_PI_SQ
        # Estimate F_8 from asymptotic: F_8 ~ F_7 * r_asymp
        F7 = float(F_table[7])
        F8_est = F7 * r_asymp
        tail_bound = abs(F8_est) * abs(epsilon) ** 16 / (1.0 - r_asymp * epsilon ** 2)
    else:
        tail_bound = float('inf')

    return {
        'c': c,
        'M': M,
        'S_BH': S_BH,
        'epsilon': epsilon,
        'epsilon_over_2pi': epsilon / TWO_PI,
        'convergent': convergent,
        'scalar_bernoulli_convergent': convergent,
        'convergence_certification': SCALAR_BERNOULLI_LANE,
        'full_virasoro_convergence_certified': False if algebra == 'virasoro' else None,
        'predicted_ratio': predicted_ratio,
        'actual_ratios': actual_ratios,
        'closed_form': closed_form,
        'closed_form_lane': SCALAR_BERNOULLI_LANE,
        'closed_form_btz_partition_certified': False,
        'partial_sums': partial_sums,
        'corrections': corrections,
        'tail_bound': tail_bound,
        'tail_bound_certified': False,
        'tail_relative': tail_bound / S_BH if S_BH > 0 else 0.0,
    }


def shadow_growth_verification(g_max: int = 7) -> Dict[str, Any]:
    r"""Check finite scalar ratios against the Bernoulli asymptotic.

    The Bernoulli asymptotic gives:
    |B_{2g+2}| / |B_{2g}| * (2g)! / (2g+2)! -> 1/(2*pi)^2

    The finite g <= 7 window is evidence for the scalar lane; it does not
    certify full Virasoro planted-forest asymptotics.
    """
    predicted = 1.0 / TWO_PI_SQ
    ratios = []
    for g in range(1, g_max):
        lfp_g = float(lambda_fp(g))
        lfp_gp1 = float(lambda_fp(g + 1))
        ratio = lfp_gp1 / lfp_g
        ratios.append({
            'g': g,
            'g+1': g + 1,
            'ratio': ratio,
            'predicted': predicted,
            'relative_error': abs(ratio - predicted) / predicted,
        })

    return {
        'predicted_ratio': predicted,
        'ratios': ratios,
        'converging': all(r['relative_error'] < 0.01 for r in ratios[-3:]),
        'lane': SCALAR_BERNOULLI_LANE,
        'finite_loop_diagnostic_only': True,
    }


# =========================================================================
# Section 7: Borel analysis at 7 loops
# =========================================================================

def borel_coefficients_7loop(c, algebra: str = 'virasoro') -> Dict[int, float]:
    r"""Truncated Borel-transform coefficients through 7 loops.

    The Borel transform in the hbar-plane:
      B(zeta) = sum_{g>=1} F_g * zeta^{2g-1} / (2g-1)!

    Coefficients b_g = F_g / (2g-1)!.
    """
    F_table = extended_free_energy_table(c, g_max=7, algebra=algebra)
    coeffs = {}
    for g in range(1, 8):
        Fg = float(F_table[g])
        factorial_2gm1 = math.factorial(2 * g - 1)
        coeffs[g] = Fg / factorial_2gm1
    return coeffs


def borel_transform_evaluate(c, zeta: float,
                              algebra: str = 'virasoro') -> float:
    r"""Evaluate the Borel transform B(zeta) at a point.

    B(zeta) = sum_{g=1}^7 F_g * zeta^{2g-1} / (2g-1)!
    """
    F_table = extended_free_energy_table(c, g_max=7, algebra=algebra)
    total = 0.0
    for g in range(1, 8):
        Fg = float(F_table[g])
        total += Fg * zeta ** (2 * g - 1) / math.factorial(2 * g - 1)
    return total


def borel_singularity_analysis(c, algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""Scalar meromorphic pole diagnostics from finite data.

    The poles of the resummed function (x/2)/sin(x/2) - 1 in the x-plane
    are at x = 2*pi*n.  In the Borel plane (u = hbar^2):
      u_n = (2*pi*n)^2

    Residues at the poles:
      R_n = lim_{x->2*pi*n} (x - 2*pi*n) * (x/2)/sin(x/2)
          = (-1)^n * 2*pi*n * (2*pi*n / 2) / (d/dx sin(x/2)|_{x=2*pi*n})
          = (-1)^n * 2*pi*n * pi*n / (cos(pi*n)/2)
          = (-1)^n * 2*pi^2*n^2 / ((-1)^n/2)
          = 4*pi^2*n^2

    The finite table can test scalar large-order ratios.  It does not prove
    Borel summability for the full Virasoro or BTZ expansion.
    """
    kappa = float(Fraction(c) / 2) if algebra == 'virasoro' else float(c)
    F_table = extended_free_energy_table(c, g_max=7, algebra=algebra)

    # First pole at u_1 = (2*pi)^2
    u_1 = TWO_PI_SQ

    # The coefficient extraction: F_g ~ 2*kappa / (2*pi)^{2g}
    # So F_g * (2*pi)^{2g} / (2*kappa) -> 1
    pole_residue_ratios = []
    for g in range(1, 8):
        Fg = float(F_table[g])
        ratio = Fg * TWO_PI ** (2 * g) / (2.0 * kappa) if kappa != 0 else 0.0
        pole_residue_ratios.append({
            'g': g,
            'F_g * (2pi)^{2g} / (2*kappa)': ratio,
            'deviation_from_1': abs(ratio - 1.0),
        })

    # Scalar Stokes normalization in the hbar-plane.
    stokes_1 = -4.0 * PI ** 2 * kappa

    # Second pole contribution ratio: F_g * (4*pi)^{2g} / (2*kappa) -> 1
    # But the alternating sign means the TOTAL is:
    # F_g = 2*kappa * sum_{n>=1} (-1)^{n+1} / (2*pi*n)^{2g}
    #      = 2*kappa/(2pi)^{2g} * eta(2g)
    # where eta is the Dirichlet eta function
    eta_ratios = []
    for g in range(1, 8):
        Fg = float(F_table[g])
        # eta(2g) = (1 - 2^{1-2g}) * zeta(2g)
        # For large g, eta(2g) -> 1 (since zeta(2g) -> 1, 2^{1-2g} -> 0)
        eta_2g = _dirichlet_eta_even(g)
        F_predicted = 2.0 * kappa / TWO_PI ** (2 * g) * eta_2g
        eta_ratios.append({
            'g': g,
            'F_g_actual': Fg,
            'F_g_predicted': F_predicted,
            'ratio': Fg / F_predicted if F_predicted != 0 else 0.0,
        })

    return {
        'kappa': kappa,
        'first_pole_u': u_1,
        'first_pole_hbar': TWO_PI,
        'stokes_1': stokes_1,
        'stokes_1_status': 'scalar_meromorphic_normalization_only',
        'borel_status': borel_summability_status(
            'virasoro_full' if algebra == 'virasoro' else algebra
        ),
        'borel_summability_certified': False,
        'full_virasoro_borel_singularities_certified': False if algebra == 'virasoro' else None,
        'pole_residue_ratios': pole_residue_ratios,
        'eta_ratios': eta_ratios,
    }


def large_order_relation_check(c, g_max: int = 7,
                                 algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""Check scalar large-order ratios at finite genus.

    The large-order prediction (leading instanton):
      F_g ~ 2*kappa / (2*pi)^{2g}  [leading term]

    The subleading correction from the second instanton:
      F_g ~ 2*kappa / (2*pi)^{2g} * [1 - 1/2^{2g} + 1/3^{2g} - ...]
          = 2*kappa / (2*pi)^{2g} * eta(2g)

    At g=7, eta(14) is already close to 1.  This is a scalar Bernoulli
    diagnostic, not a proof of full Virasoro resurgence.
    """
    kappa = float(Fraction(c) / 2) if algebra == 'virasoro' else float(c)
    F_table = extended_free_energy_table(c, g_max=g_max, algebra=algebra)

    results = []
    for g in range(1, g_max + 1):
        Fg = float(F_table[g])

        # Leading approximation
        F_leading = 2.0 * kappa / TWO_PI ** (2 * g)

        # Full Dirichlet eta approximation
        eta_2g = _dirichlet_eta_even(g)
        F_eta = 2.0 * kappa / TWO_PI ** (2 * g) * eta_2g

        results.append({
            'g': g,
            'F_g': Fg,
            'F_leading': F_leading,
            'F_eta': F_eta,
            'leading_error': abs(Fg - F_leading) / abs(Fg) if Fg != 0 else 0,
            'eta_error': abs(Fg - F_eta) / abs(Fg) if Fg != 0 else 0,
        })

    return {
        'kappa': kappa,
        'c': c,
        'results': results,
        'lane': SCALAR_BERNOULLI_LANE,
        'full_virasoro_resurgence_certified': False if algebra == 'virasoro' else None,
    }


# =========================================================================
# Section 8: Maloney-Witten comparison
# =========================================================================

def maloney_witten_comparison(c, M, g_max: int = 7) -> Dict[str, Any]:
    r"""Compare the finite shadow diagnostic with external MW input.

    MW (0712.0155) sum over SL(2,Z) images:
      Z^MW(tau) = sum_{gamma in SL(2,Z)/Gamma_inf} Z_0(gamma.tau)

    The finite shadow diagnostic is
      Z^sh = exp(sum_{g=1}^7 hbar^{2g} F_g)

    It is a perturbative single-saddle object.  It does not recover the
    exact Maloney-Witten partition function or certify the analytic status of
    the Poincare/Farey sum.  The MW divergence flag below records external
    analytic input, not a conclusion from seven finite coefficients.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return {'error': 'S_BH <= 0'}

    epsilon = TWO_PI / S_BH
    kappa = float(Fraction(c) / 2)

    # Finite single-saddle shadow contribution.
    F_table = extended_free_energy_table(c, g_max=g_max)
    shadow_sum = sum(float(F_table[g]) * epsilon ** (2 * g) for g in range(1, g_max + 1))
    Z_shadow = math.exp(shadow_sum)

    # Closed-form comparison at scalar level
    if abs(epsilon) < TWO_PI:
        Z_closed = math.exp(ahat_closed_form(c, epsilon))
    else:
        Z_closed = None

    # MW non-perturbative: the leading sub-dominant saddle (c_F=1, d=0)
    # contributes ~ exp(-2*pi*c*Im(1/tau)) which is ~ exp(-c/12 * S_BH)
    # for the thermal saddle at beta_H.
    # This is exponentially suppressed for large S_BH.
    np_suppression = math.exp(-float(c) / 12.0 * S_BH) if S_BH < 500 else 0.0

    # Truncation error from stopping at g=7
    F7 = float(F_table[g_max])
    r_asymp = 1.0 / TWO_PI_SQ
    tail_first = abs(F7 * r_asymp) * abs(epsilon) ** (2 * (g_max + 1))

    return {
        'c': c,
        'M': M,
        'S_BH': S_BH,
        'epsilon': epsilon,
        'kappa': kappa,
        # Shadow tower
        'shadow_sum_log': shadow_sum,
        'Z_shadow': Z_shadow,
        'Z_closed_form': Z_closed,
        # MW comparison
        'mw_np_suppression': np_suppression,
        'mw_perturbative_vs_np': abs(shadow_sum) / np_suppression if np_suppression > 1e-300 else float('inf'),
        'mw_divergence_source': 'external_maloney_witten_input',
        'mw_divergence_certified_by_engine': False,
        'closed_form_btz_partition_recovered': False,
        # Error budget
        'truncation_error': tail_first,
        'truncation_relative': tail_first / abs(shadow_sum) if abs(shadow_sum) > 0 else 0.0,
        'shadow_converges': abs(epsilon) < TWO_PI,
        'shadow_convergence_certification': SCALAR_BERNOULLI_LANE,
        'full_virasoro_convergence_certified': False,
        'mw_diverges': True,
    }


# =========================================================================
# Section 9: Special central charges at 7 loops
# =========================================================================

def btz_c1_7loop(M: float = 10.0) -> Dict[str, Any]:
    """BTZ at c=1 (minimal / single free boson) through 7 loops.

    kappa = 1/2.  Smallest nontrivial central charge for Virasoro.
    All corrections are tiny.
    """
    return entropy_7loop_full(1, M, algebra='virasoro')


def btz_c13_7loop(M: float = 10.0) -> Dict[str, Any]:
    """BTZ diagnostic at the c=13 Virasoro scalar fixed point.

    kappa = 13/2.  This does not assert A = A^! or identify the
    Hochschild/derived-centre branch.
    """
    return entropy_7loop_full(13, M, algebra='virasoro')


def btz_c24_7loop(M: float = 10.0) -> Dict[str, Any]:
    """BTZ at c=24 (pure 3D gravity / monster) through 7 loops.

    kappa(Vir_24) = 12.  Identifying this with a full extremal CFT or
    one-loop determinant is external input.
    """
    return entropy_7loop_full(24, M, algebra='virasoro')


def btz_c26_7loop(M: float = 10.0) -> Dict[str, Any]:
    """BTZ at c=26 (critical bosonic string) through 7 loops.

    kappa = 13.  Dual algebra Vir_0 has kappa = 0 (uncurved).
    This scalar complementarity does not identify A^!, B(A), or the
    Hochschild bulk.
    """
    return entropy_7loop_full(26, M, algebra='virasoro')


def special_charges_comparison_7loop(M: float = 10.0) -> Dict[str, Dict[str, Any]]:
    """Compare all special central charges at 7 loops."""
    return {
        'c=1': btz_c1_7loop(M),
        'c=13': btz_c13_7loop(M),
        'c=24': btz_c24_7loop(M),
        'c=26': btz_c26_7loop(M),
    }


# =========================================================================
# Section 10: Complementarity at 7 loops
# =========================================================================

def complementarity_7loop(c, M: float = 10.0) -> Dict[str, Any]:
    r"""Scalar complementarity check through genus 7.

    From kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13,
    the scalar free energies satisfy:

        F_g^{sc}(c) + F_g^{sc}(26-c) = 13 * lambda_g^FP

    This is a LINEAR identity that holds at all genera for the scalar lane.
    Planted-forest corrections break simple additivity at g >= 2.
    """
    c_frac = Fraction(c)
    c_dual = 26 - c_frac

    F_c = extended_free_energy_table(c_frac, g_max=7)
    F_dual = extended_free_energy_table(c_dual, g_max=7)

    results = {}
    for g in range(1, 8):
        Fg_c = F_c[g]
        Fg_dual = F_dual[g]
        Fg_sum = Fg_c + Fg_dual
        Fg_expected_scalar = Fraction(13) * lambda_fp(g)

        results[g] = {
            'F_g_c': float(Fg_c),
            'F_g_dual': float(Fg_dual),
            'sum': float(Fg_sum),
            'expected_scalar_sum': float(Fg_expected_scalar),
            'scalar_match': Fg_sum == Fg_expected_scalar if g >= 4 else None,
            # For g<=3, planted-forest may break simple additivity
        }

    # Entropy complementarity
    S_c = bekenstein_hawking_entropy(float(c), M)
    S_dual = bekenstein_hawking_entropy(float(c_dual), M)

    results['entropy'] = {
        'S_BH_c': S_c,
        'S_BH_dual': S_dual,
        'kappa_sum': float(kappa_virasoro(c_frac) + kappa_virasoro(c_dual)),
        'kappa_sum_expected': 13.0,
    }

    return results


# =========================================================================
# Section 11: Area corrections and Bekenstein-Hawking modifications
# =========================================================================

def area_corrections_7loop(c, M) -> Dict[str, Any]:
    r"""Compute the area (Bekenstein-Hawking) corrections at each loop order.

    In 3D gravity, the BTZ entropy is:
      S_BH = A / (4*G_N) = 2*pi*r_+ / (4*G_N) = 2*pi*sqrt(c*M/6)

    where r_+ is the horizon radius.

    The quantum-corrected entropy defines a quantum-corrected area:
      A_quantum = 4*G_N * S_quantum

    The fractional area correction at each loop order:
      delta_A_g / A = S_g / S_BH
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return {'error': 'S_BH <= 0'}

    result = {
        'c': c,
        'M': M,
        'S_BH': S_BH,
        'A_classical': S_BH,  # In natural units A/(4G) = S
    }

    S_total = S_BH
    for g in range(1, 8):
        Sg = entropy_correction_7loop(c, M, g)
        result[f'delta_S_{g}'] = Sg
        result[f'delta_A_{g}_over_A'] = Sg / S_BH
        S_total += Sg

    result['S_total'] = S_total
    result['A_quantum_over_A_classical'] = S_total / S_BH

    return result


# =========================================================================
# Section 12: Resurgence from 7-loop data
# =========================================================================

def resurgence_from_7loop(c, algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""Extract scalar large-order diagnostics from seven coefficients.

    The key observables:
    1. Scalar pole scale: A_1 = (2*pi)^2
    2. Convention-dependent scalar Stokes normalization: -4*pi^2*kappa
    3. Scalar large-order growth: F_g ~ 2*kappa/(2*pi)^{2g}

    This routine does not certify Borel summability or median resummation
    for the full Virasoro/BTZ expansion.
    """
    kappa = float(Fraction(c) / 2) if algebra == 'virasoro' else float(c)
    F_table = extended_free_energy_table(c, g_max=7, algebra=algebra)

    # Scalar pole scale from the ratio test: A ~ F_g/F_{g+1}.
    action_estimates = []
    for g in range(1, 7):
        Fg = float(F_table[g])
        Fgp1 = float(F_table[g + 1])
        if abs(Fgp1) > 1e-300:
            A_est = abs(Fg / Fgp1) ** (1.0 / 2)  # F_g/F_{g+1} ~ (2*pi)^2 * (g-dependent)
            # Better: the ratio test for Bernoulli gives
            # F_g/F_{g+1} = lambda_g/lambda_{g+1} = (2pi)^2 * correction
            # The correction factor: (2^{2g-1}-1)/(2^{2g+1}-1) * (2g+2)(2g+1) * |B_{2g}|/|B_{2g+2}|
            # Asymptotically this ratio -> (2pi)^2
            action_estimates.append({
                'g': g,
                'F_g/F_{g+1}': Fg / Fgp1,
                'sqrt_ratio': A_est,
                'A_predicted': TWO_PI_SQ,
            })

    # Scalar Stokes normalization.
    stokes_1 = -4.0 * PI ** 2 * kappa

    borel_status = borel_summability_status(
        'virasoro_full' if algebra == 'virasoro' else algebra
    )

    return {
        'kappa': kappa,
        'instanton_action_1': TWO_PI_SQ,
        'stokes_constant_1': stokes_1,
        'stokes_constant_1_status': 'scalar_meromorphic_normalization_only',
        'borel_summable': False,
        'borel_summability_certified': False,
        'borel_status': borel_status,
        'action_estimates': action_estimates,
        'median_resummation': False,
        'median_resummation_certified': False,
        'full_virasoro_resurgence_certified': False if algebra == 'virasoro' else None,
    }


# =========================================================================
# Section 13: Numerical precision diagnostics
# =========================================================================

def precision_diagnostics(c) -> Dict[str, Any]:
    r"""Numerical precision analysis of the 7-loop computation.

    At genus 7, the free energy F_7 ~ 10^{-10} for c ~ 25.
    We need to verify that floating-point arithmetic does not
    introduce significant errors.

    Strategy: compute in exact arithmetic (Fraction) and compare
    with floating-point.
    """
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    results = {}
    for g in range(1, 8):
        # Exact
        Fg_exact = F_g_scalar(kappa, g)
        # Float
        Fg_float = float(kappa) * float(lambda_fp(g))
        # Error
        Fg_exact_float = float(Fg_exact)
        rel_err = abs(Fg_float - Fg_exact_float) / abs(Fg_exact_float) if Fg_exact_float != 0 else 0

        results[g] = {
            'F_g_exact': str(Fg_exact),
            'F_g_float': Fg_float,
            'F_g_exact_float': Fg_exact_float,
            'relative_error': rel_err,
            'exact_bits': Fg_exact.numerator.bit_length() + Fg_exact.denominator.bit_length(),
        }

    return results


def full_7loop_report(c, M, algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""Finite 7-loop BTZ shadow diagnostic report.

    Combines:
    1. Entropy diagnostic through 7 loops
    2. Scalar convergence diagnostics
    3. Scalar Borel-pole diagnostics
    4. Maloney-Witten external comparison
    5. Complementarity check
    6. Area corrections
    7. Resurgence data
    8. Precision diagnostics
    """
    report = {
        'entropy': entropy_7loop_full(c, M, algebra),
        'convergence': convergence_analysis_7loop(c, M, algebra),
        'borel': borel_singularity_analysis(c, algebra),
        'maloney_witten': maloney_witten_comparison(c, M),
        'complementarity': complementarity_7loop(c, M),
        'area_corrections': area_corrections_7loop(c, M),
        'resurgence': resurgence_from_7loop(c, algebra),
        'precision': precision_diagnostics(c),
    }
    return report
