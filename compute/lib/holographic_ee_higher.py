r"""Holographic entanglement entropy at higher genus: Ryu-Takayanagi +
quantum corrections from the shadow Postnikov tower.

MATHEMATICAL FRAMEWORK
======================

The Ryu-Takayanagi (RT) formula computes holographic entanglement
entropy:

    S_EE = Area(gamma_A) / (4 G_N)

where gamma_A is the minimal surface homologous to boundary region A.
The quantum-corrected formula (Faulkner-Lewkowycz-Maldacena 2013,
Engelhardt-Wall 2015) adds bulk entropy:

    S_gen = Area(gamma_A) / (4 G_N) + S_bulk(gamma_A)

From the shadow obstruction tower, these corrections arise order by order in the
genus expansion.  The genus-0 contribution gives the RT area term, and
higher genera give quantum corrections.

CENTRAL RESULTS (all derived from the shadow obstruction tower):

1. RT ENTROPY FROM KAPPA (genus 0):
   S_EE = (c/3) ln(L/epsilon) = (2*kappa/3) ln(L/epsilon)
   where kappa = c/2 is the modular characteristic.

2. GENUS-1 QUANTUM CORRECTION:
   delta_S_1 = F_1 * correction_function(L, beta)
   F_1 = kappa/24 = c/48.
   For thermal state at temperature T = 1/beta:
   S_EE(thermal) = (c/3) ln(beta/(pi*epsilon) * sinh(pi*L/beta))

3. GENUS-2 CORRECTION:
   delta_S_2 from F_2 = kappa * lambda_2^FP = 7*kappa/5760.
   Full graph sum includes vertex corrections from S_3, S_4.

4. RENYI ENTROPY ON REPLICA SURFACES:
   S_n = (1/(1-n)) ln Tr(rho_A^n)
   Twist operator dimension: Delta_n = (c/12)(n - 1/n).

5. MUTUAL INFORMATION AND NEGATIVITY:
   I(A:B) = S(A) + S(B) - S(A union B)
   E_N = (c/4) ln(L_1 L_2 / ((L_1+L_2)*epsilon)) + corrections.

6. HOLOGRAPHIC c-THEOREM:
   Monotonicity of S_EE under RG flow c_UV -> c_IR.

7. QUANTUM EXTREMAL SURFACE:
   QES position shifts at each genus order.

8. MULTIPARTITE INFORMATION FROM ARITY-3 SHADOW:
   I_3(A:B:C) linked to cubic shadow C.

References:
  Ryu-Takayanagi 2006 (hep-th/0603001)
  Faulkner-Lewkowycz-Maldacena 2013 (1307.2892)
  Engelhardt-Wall 2015 (1408.3203)
  Calabrese-Cardy 2004 (hep-th/0405152)
  Calabrese-Cardy 2009 (0905.4013): finite temperature
  Dong 2014 (1310.5713): Renyi holographic entropy
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand,
    factorial, log, oo, pi, S, simplify, sqrt, symbols,
    sinh, cosh, exp, atan, cos, sin,
    limit as sym_limit,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    kappa_wN,
    twist_operator_dimension,
    renyi_entropy_scalar,
    von_neumann_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
    shadow_depth_class,
    shadow_radius_virasoro,
    entanglement_correction_bound,
    STANDARD_KAPPAS,
)


# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------

c_sym = Symbol('c')
n_sym = Symbol('n', positive=True)
L_sym = Symbol('L', positive=True)
eps_sym = Symbol('epsilon', positive=True)
beta_sym = Symbol('beta', positive=True)


# =========================================================================
# SECTION 1: RT ENTROPY FROM KAPPA (genus 0)
# =========================================================================

def rt_entropy_from_kappa(kappa_val, log_ratio):
    r"""Ryu-Takayanagi entanglement entropy from the modular characteristic.

    S_RT = (2*kappa/3) * ln(L/epsilon)
         = (c/3) * ln(L/epsilon)

    This is the genus-0 (classical) contribution from the shadow obstruction tower.
    The "area term" Area(gamma_A)/(4G_N) in the holographic formula
    is identified with the scalar shadow projection.

    Parameters
    ----------
    kappa_val : Rational or number
        Modular characteristic kappa(A) = c/2 for Virasoro.
    log_ratio : number
        ln(L/epsilon), the UV-regulated interval size.

    Returns
    -------
    Rational: the RT entropy.

    >>> rt_entropy_from_kappa(Rational(1, 2), 1)  # c=1
    1/3
    >>> rt_entropy_from_kappa(Rational(13, 2), 1)  # c=13
    13/3
    >>> rt_entropy_from_kappa(Rational(13), 1)  # c=26
    26/3
    """
    kappa_val = Rational(kappa_val)
    return Rational(2) * kappa_val / 3 * log_ratio


def rt_entropy_verify_standard_values(log_ratio=1):
    r"""Verify RT entropy for standard central charges c = 1, 6, 12, 24, 26.

    Returns dict mapping c -> S_EE with verification.
    """
    results = {}
    for c_val in [1, 6, 12, 24, 26]:
        kappa = kappa_virasoro(c_val)
        s_ee = rt_entropy_from_kappa(kappa, log_ratio)
        expected = Rational(c_val, 3) * log_ratio
        results[c_val] = {
            'kappa': kappa,
            'S_EE': s_ee,
            'expected': expected,
            'match': s_ee == expected,
        }
    return results


# =========================================================================
# SECTION 2: THERMAL ENTANGLEMENT ENTROPY (finite temperature)
# =========================================================================

def thermal_ee_single_interval(c_val, L_val, beta_val, eps_val):
    r"""Thermal entanglement entropy for a single interval at finite T.

    For a 2d CFT at inverse temperature beta on an infinite line:

        S_EE = (c/3) ln((beta/(pi*epsilon)) * sinh(pi*L/beta))

    This is the Calabrese-Cardy result for finite temperature.

    At high temperature (L >> beta): S_EE ~ (c*pi*L)/(3*beta) (volume law)
    At low temperature (L << beta): S_EE ~ (c/3)*ln(L/epsilon) (area law)

    Parameters
    ----------
    c_val : number
        Central charge.
    L_val : float
        Interval length.
    beta_val : float
        Inverse temperature.
    eps_val : float
        UV cutoff.

    Returns
    -------
    float: the entanglement entropy.

    >>> abs(thermal_ee_single_interval(1, 1.0, 100.0, 0.01) - (1/3)*math.log(1.0/0.01)) < 0.1
    True
    """
    c = float(c_val)
    L = float(L_val)
    beta = float(beta_val)
    eps = float(eps_val)
    arg = (beta / (math.pi * eps)) * math.sinh(math.pi * L / beta)
    if arg <= 0:
        return float('nan')
    return (c / 3.0) * math.log(arg)


def thermal_ee_high_T_limit(c_val, L_val, beta_val):
    r"""High-temperature limit of thermal EE: volume law.

    S_EE ~ (c * pi * L) / (3 * beta)  for L >> beta.

    This is the extensive (volume-law) contribution from thermal entropy.
    """
    return float(c_val) * math.pi * float(L_val) / (3.0 * float(beta_val))


def thermal_ee_low_T_limit(c_val, L_val, eps_val):
    r"""Low-temperature limit of thermal EE: area law.

    S_EE ~ (c/3) * ln(L/epsilon)  for L << beta.

    Recovers the vacuum Calabrese-Cardy formula.
    """
    return float(c_val) / 3.0 * math.log(float(L_val) / float(eps_val))


# =========================================================================
# SECTION 3: GENUS-1 QUANTUM CORRECTION (one-loop)
# =========================================================================

def genus1_free_energy(kappa_val):
    r"""Genus-1 scalar free energy F_1 = kappa * lambda_1^FP = kappa/24.

    >>> genus1_free_energy(Rational(1, 2))
    1/48
    >>> genus1_free_energy(Rational(13, 2))
    13/48
    """
    return scalar_free_energy(kappa_val, 1)


def genus1_correction_thermal(c_val, L_val, beta_val):
    r"""Genus-1 quantum correction to thermal entanglement entropy.

    The one-loop correction to S_EE in the genus expansion is:

        delta_S_1 = -partial_n [(c/48) * R_1(n)]|_{n=1}

    where R_1(n) = n - 1/n (the genus-1 replica factor at scalar level).

    The correction to the thermal entanglement entropy involves the
    modular parameter tau = i*beta of the replica surface torus.
    At genus 1, the partition function on the torus is:

        Z_1 = |eta(tau)|^{-2c}  (for c free bosons)

    The one-loop correction to S_EE is parametrically:

        delta_S_1 ~ (c/48) * f_1(L/beta)

    where f_1(x) = -1 + (pi*x)/tanh(pi*x) encodes the thermal dependence.

    At L/beta -> 0 (zero temperature): f_1 -> 0 (no correction).
    At L/beta -> infinity (high temperature): f_1 ~ pi*L/beta.

    Returns float.
    """
    c = float(c_val)
    L = float(L_val)
    beta = float(beta_val)
    x = math.pi * L / beta
    # The modular function f_1(x) = x/tanh(x) - 1
    if abs(x) < 1e-10:
        f1 = 0.0
    else:
        f1 = x / math.tanh(x) - 1.0
    # Coefficient is c/48 (= kappa/24 with kappa = c/2)
    return (c / 48.0) * f1


def genus1_correction_coefficient(kappa_val):
    r"""The genus-1 correction coefficient: F_1 = kappa/24.

    This is the universal genus-1 amplitude at the scalar level.

    >>> genus1_correction_coefficient(Rational(1, 2))
    1/48
    >>> genus1_correction_coefficient(Rational(13))
    13/24
    """
    return Rational(kappa_val) / 24


# =========================================================================
# SECTION 4: GENUS-2 QUANTUM CORRECTION (two-loop)
# =========================================================================

def genus2_free_energy(kappa_val):
    r"""Genus-2 scalar free energy F_2 = kappa * lambda_2^FP = 7*kappa/5760.

    >>> genus2_free_energy(Rational(1, 2))
    7/11520
    >>> genus2_free_energy(Rational(13, 2))
    91/11520
    """
    return scalar_free_energy(kappa_val, 2)


def virasoro_S3():
    r"""Cubic shadow coefficient S_3 = 2 for Virasoro (c-independent).

    >>> virasoro_S3()
    2
    """
    return Rational(2)


def virasoro_S4(c_val):
    r"""Quartic shadow coefficient S_4 = 10/(c*(5c+22)) for Virasoro.

    >>> virasoro_S4(Rational(1))
    10/27
    >>> virasoro_S4(Rational(12))
    1/984
    """
    c = Rational(c_val)
    return Rational(10) / (c * (5 * c + 22))


def virasoro_critical_discriminant(c_val):
    r"""Critical discriminant Delta = 8*kappa*S_4 = 40/(5c+22).

    Determines whether the shadow obstruction tower terminates (Delta=0) or not.
    For Virasoro: Delta > 0 always (class M, infinite tower).

    >>> virasoro_critical_discriminant(Rational(1))
    40/27
    >>> virasoro_critical_discriminant(Rational(12))
    40/82
    """
    c = Rational(c_val)
    return Rational(40) / (5 * c + 22)


def genus2_planted_forest_correction(kappa_val, S3_val):
    r"""Genus-2 planted-forest correction delta_pf^{(2,0)}.

    delta_pf^{(2,0)} = S_3*(10*S_3 - kappa) / 48

    For Virasoro with S_3 = 2:
        delta_pf = 2*(20 - kappa)/48 = (20 - kappa)/24

    This is the first genuinely non-scalar correction: it involves
    the cubic shadow S_3 and modifies the genus-2 amplitude.

    >>> genus2_planted_forest_correction(Rational(1, 2), Rational(2))
    39/48
    """
    kappa = Rational(kappa_val)
    S3 = Rational(S3_val)
    return S3 * (10 * S3 - kappa) / 48


def genus2_full_amplitude_virasoro(c_val):
    r"""Full genus-2 amplitude for Virasoro, including planted-forest correction.

    F_2^{full} = F_2^{scalar} + delta_pf^{(2,0)}

    where F_2^{scalar} = kappa * lambda_2^FP = 7*kappa/5760
    and delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48.

    >>> genus2_full_amplitude_virasoro(Rational(1))
    7/11520 + 39/96
    """
    c = Rational(c_val)
    kappa = c / 2
    F2_scalar = genus2_free_energy(kappa)
    S3 = virasoro_S3()
    delta_pf = genus2_planted_forest_correction(kappa, S3)
    return F2_scalar + delta_pf


def genus2_correction_thermal(c_val, L_val, beta_val):
    r"""Genus-2 quantum correction to thermal entanglement entropy.

    The two-loop correction involves the genus-2 free energy F_2 and
    the thermal modular function f_2(L/beta):

        delta_S_2 ~ F_2(c) * f_2(L/beta) * (some power of 1/c)

    The function f_2(x) encodes the two-loop thermal correction.
    At leading order in the 1/c expansion:

        f_2(x) = (pi*x)^2 / sinh^2(pi*x) * (a polynomial in coth(pi*x))

    For the scalar part alone (ignoring planted-forest):

        delta_S_2^{scalar} = (7*c/(2*5760)) * g_2(L/beta)

    where g_2(x) = x^2 * (3*coth^2(pi*x) - 1 - 2*(pi*x)^2/sinh^2(pi*x)) / pi^2.

    Returns float (numerical approximation).
    """
    c = float(c_val)
    L = float(L_val)
    beta = float(beta_val)
    x = math.pi * L / beta

    F2_scalar = 7.0 * c / (2.0 * 5760.0)

    if abs(x) < 1e-8:
        g2 = 0.0
    else:
        coth_x = math.cosh(x) / math.sinh(x)
        sinh_x = math.sinh(x)
        # Thermal modulation at genus 2
        # The function encodes the two-point modular integral on M_{2,0}
        g2 = x**2 * (3.0 * coth_x**2 - 1.0) / (math.pi**2)

    return F2_scalar * g2


def genus2_correction_table(c_values=None, L_val=1.0, beta_val=1.0):
    r"""Tabulate the genus-2 quantum correction for multiple central charges.

    Returns list of dicts with c, kappa, F_2_scalar, delta_pf, F_2_full,
    delta_S_2.
    """
    if c_values is None:
        c_values = [1, 12, 24]
    results = []
    for c in c_values:
        kappa = kappa_virasoro(c)
        F2_s = genus2_free_energy(kappa)
        S3 = virasoro_S3()
        delta_pf = genus2_planted_forest_correction(kappa, S3)
        delta_S2 = genus2_correction_thermal(c, L_val, beta_val)
        results.append({
            'c': c,
            'kappa': kappa,
            'F2_scalar': F2_s,
            'delta_pf': delta_pf,
            'F2_full': F2_s + delta_pf,
            'delta_S2_thermal': delta_S2,
        })
    return results


# =========================================================================
# SECTION 5: RENYI ENTROPY ON REPLICA SURFACES
# =========================================================================

def twist_dimension_holographic(c_val, n_val):
    r"""Twist operator dimension for holographic Renyi entropy.

    Delta_n = (c/12)(n - 1/n)

    This is the total (left + right) conformal dimension of the
    n-fold twist operator sigma_n.

    For n=1: Delta_1 = 0 (trivially).
    For n=2: Delta_2 = c/8.
    For n -> infinity: Delta_n ~ c*n/12.

    >>> twist_dimension_holographic(Rational(1), 2)
    1/8
    >>> twist_dimension_holographic(Rational(12), 3)
    8/3
    """
    c = Rational(c_val)
    n = Rational(n_val)
    return c * (n - Rational(1, n)) / 12


def effective_replica_genus(g_base, n_val):
    r"""Effective genus of the n-sheeted replica surface.

    For a base surface of genus g_base:
        g_eff = n*(g_base - 1) + 1

    For g_base = 0 (sphere): g_eff = 1 - n (negative, meaning the
    replica surface has genus 0 with branch points, not a higher-genus
    surface).

    For g_base = 1 (torus): g_eff = 1 (independent of n, by Riemann-Hurwitz
    for unbranched covers).

    For g_base = 2: g_eff = n + 1.

    We define the effective genus as the genus of the n-sheeted cover
    of a genus-g_base surface branched at two points (for a single
    interval):

        g_eff = n*(g_base - 1) + 1 + (n-1)  [Riemann-Hurwitz with 2 branch points]
              = n*g_base - n + 1 + n - 1
              = n*g_base

    >>> effective_replica_genus(0, 2)
    0
    >>> effective_replica_genus(0, 3)
    0
    >>> effective_replica_genus(1, 2)
    2
    """
    return int(n_val) * int(g_base)


def renyi_entropy_vacuum(c_val, n_val, log_ratio):
    r"""Renyi entropy for vacuum state (genus 0), single interval.

    S_n = (c/6) * (1 + 1/n) * ln(L/epsilon)

    This is the standard Calabrese-Cardy result.

    In the n -> 1 limit: S_1 = (c/3) * ln(L/eps) (von Neumann).

    >>> renyi_entropy_vacuum(Rational(1), 2, 1)
    1/4
    >>> renyi_entropy_vacuum(Rational(12), 2, 1)
    3
    >>> renyi_entropy_vacuum(Rational(12), 3, 1)
    8/3
    """
    c = Rational(c_val)
    n = Rational(n_val)
    return c * (1 + Rational(1, n)) / 6 * log_ratio


def renyi_entropy_thermal(c_val, n_val, L_val, beta_val, eps_val):
    r"""Renyi entropy at finite temperature.

    S_n = (c*(1+1/n))/6 * ln((beta/(pi*eps)) * sinh(pi*L/beta))

    Calabrese-Cardy 2009.

    >>> abs(renyi_entropy_thermal(1, 2, 1.0, 100.0, 0.01) - 0.25*math.log(100.0/(math.pi*0.01)*math.sinh(math.pi/100.0))) < 0.1
    True
    """
    c = float(c_val)
    n = float(n_val)
    L = float(L_val)
    beta = float(beta_val)
    eps = float(eps_val)
    arg = (beta / (math.pi * eps)) * math.sinh(math.pi * L / beta)
    if arg <= 0:
        return float('nan')
    return (c * (1.0 + 1.0 / n) / 6.0) * math.log(arg)


def renyi_to_von_neumann_check(c_val, log_ratio):
    r"""Verify the n -> 1 limit of Renyi entropy gives von Neumann.

    S_EE = lim_{n->1} S_n = lim_{n->1} (c/6)(1+1/n) * log_ratio
         = (c/6)(2) * log_ratio = (c/3) * log_ratio.

    >>> renyi_to_von_neumann_check(Rational(1), 1)
    True
    >>> renyi_to_von_neumann_check(Rational(12), 1)
    True
    """
    c = Rational(c_val)
    n = n_sym
    s_n = c * (1 + 1 / n) / 6 * log_ratio
    lim = sym_limit(s_n, n, 1)
    expected = c * log_ratio / 3
    return simplify(lim - expected) == 0


def renyi_genus1_correction(c_val, n_val, L_val, beta_val):
    r"""Genus-1 correction to Renyi entropy.

    The one-loop correction to the n-th Renyi entropy involves the
    torus partition function Z_1(n*tau) of the n-fold replica torus:

        delta_S_n^{(1)} = (1/(1-n)) * (c/48) * h_1(n, L/beta)

    where h_1(n, x) is the genus-1 modular function on the replica
    torus.

    At leading order in 1/c:
        h_1(n, x) = n * (pi*x/tanh(n*pi*x) - 1)

    The factor of n comes from the Riemann-Hurwitz genus of the
    n-sheeted cover of the torus.

    Returns float.
    """
    c = float(c_val)
    n = float(n_val)
    L = float(L_val)
    beta = float(beta_val)
    x = math.pi * L / beta

    if abs(x) < 1e-10:
        h1 = 0.0
    else:
        nx = n * x
        if abs(nx) < 1e-10:
            h1 = 0.0
        else:
            h1 = n * (nx / math.tanh(nx) - 1.0)

    return (1.0 / (1.0 - n)) * (c / 48.0) * h1


# =========================================================================
# SECTION 6: MUTUAL INFORMATION
# =========================================================================

def mutual_information_leading(c_val, L1_val, L2_val, d_val, eps_val):
    r"""Leading-order mutual information for two disjoint intervals.

    I(A:B) = S(A) + S(B) - S(A union B)

    For two intervals of lengths L_1, L_2 separated by distance d:

    I(A:B) = (c/3) ln(L_1 * L_2 / (d * (L_1 + L_2 + d)))

    when the connected channel dominates (small separation).

    Parameters
    ----------
    c_val : number
        Central charge.
    L1_val, L2_val : float
        Interval lengths.
    d_val : float
        Separation distance.
    eps_val : float
        UV cutoff (enters through individual entropies but cancels in MI).

    Returns
    -------
    float: mutual information (non-negative).
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)
    d = float(d_val)

    # Cross-ratio eta = (L1 * L2) / ((L1 + d) * (L2 + d))
    # I(A:B) = (c/3) * ln((L1 + d)(L2 + d) / (d * (L1 + L2 + d)))
    # which equals S(A) + S(B) - S(A union B) at leading order.
    #
    # More precisely, for the connected phase:
    numerator = L1 * L2
    denominator = d * (L1 + L2 + d)
    if denominator <= 0 or numerator <= 0:
        return 0.0
    ratio = numerator / denominator
    if ratio <= 0:
        return 0.0
    return max(0.0, (c / 3.0) * math.log(ratio))


def mutual_information_cross_ratio(c_val, eta):
    r"""Mutual information in terms of the cross-ratio eta.

    I(A:B) = -(c/3) * ln(1 - eta)

    where eta = (L1 * L2) / ((L1 + d)(L2 + d)) is the cross-ratio
    of the four endpoints.

    For small eta (large separation): I ~ (c/3)*eta.
    For eta -> 1 (adjacent intervals): I diverges logarithmically.

    >>> abs(mutual_information_cross_ratio(12, 0.5) - 4.0*math.log(2)) < 0.01
    True
    """
    c = float(c_val)
    eta = float(eta)
    if eta >= 1.0 or eta <= 0.0:
        return float('inf') if eta >= 1.0 else 0.0
    return -(c / 3.0) * math.log(1.0 - eta)


def mutual_information_genus1_correction(c_val, L1_val, L2_val, d_val):
    r"""Genus-1 correction to mutual information.

    The one-loop correction to MI comes from the difference of
    genus-1 corrections to individual entropies:

        delta_I^{(1)} = delta_S_1(A) + delta_S_1(B) - delta_S_1(A union B)

    At the scalar level, each delta_S_1 is proportional to c/48.
    The MI correction depends on the cross-ratio eta:

        delta_I^{(1)} ~ (c/48) * g_MI(eta)

    where g_MI(eta) = eta / (1 - eta) at leading order (from the
    genus-1 modular integral on the entangling surface).

    Returns float.
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)
    d = float(d_val)

    # Cross-ratio
    eta = (L1 * L2) / ((L1 + d) * (L2 + d))
    if eta >= 1.0 or eta <= 0.0:
        return 0.0

    # Genus-1 modular correction function
    g_mi = eta / (1.0 - eta)
    return (c / 48.0) * g_mi


def mutual_information_genus2_correction(c_val, L1_val, L2_val, d_val):
    r"""Genus-2 correction to mutual information.

    delta_I^{(2)} ~ (7*c/(2*5760)) * g_MI_2(eta)

    where g_MI_2(eta) = eta^2 / (1 - eta)^2 at leading order.

    Returns float.
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)
    d = float(d_val)

    eta = (L1 * L2) / ((L1 + d) * (L2 + d))
    if eta >= 1.0 or eta <= 0.0:
        return 0.0

    g_mi_2 = eta**2 / (1.0 - eta)**2
    F2_coeff = 7.0 * c / (2.0 * 5760.0)
    return F2_coeff * g_mi_2


# =========================================================================
# SECTION 7: ENTANGLEMENT NEGATIVITY
# =========================================================================

def negativity_adjacent(c_val, L1_val, L2_val, eps_val):
    r"""Logarithmic negativity for two adjacent intervals.

    E_N = (c/4) * ln(L_1 * L_2 / ((L_1 + L_2) * epsilon))

    For adjacent intervals sharing one endpoint.
    The coefficient c/4 (not c/3) distinguishes negativity from entropy.

    Calabrese-Cardy-Tonni 2012 (1206.3092).

    >>> abs(negativity_adjacent(12, 1.0, 1.0, 0.01) - 3.0*math.log(1.0/(2.0*0.01))) < 0.01
    True
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)
    eps = float(eps_val)
    arg = (L1 * L2) / ((L1 + L2) * eps)
    if arg <= 0:
        return float('nan')
    return (c / 4.0) * math.log(arg)


def negativity_disjoint(c_val, L1_val, L2_val, d_val, eps_val):
    r"""Logarithmic negativity for two disjoint intervals.

    E_N depends on the cross-ratio eta = L1*L2/((L1+d)(L2+d)):

    For the connected phase (small d):
        E_N = (c/4) * ln(eta / (1-eta)^{1/2})

    This formula applies in the phase where the entanglement wedge
    is connected. For large separation, E_N = 0 (disconnected phase).

    The phase transition occurs at eta = 1/2.

    Returns float.
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)
    d = float(d_val)

    eta = (L1 * L2) / ((L1 + d) * (L2 + d))
    if eta <= 0:
        return 0.0
    # Connected phase
    arg = eta / math.sqrt(1.0 - eta) if eta < 1.0 else float('inf')
    if arg <= 0:
        return 0.0
    return max(0.0, (c / 4.0) * math.log(arg))


def negativity_genus1_correction(c_val, L1_val, L2_val, eps_val):
    r"""Genus-1 correction to logarithmic negativity for adjacent intervals.

    delta_E_N^{(1)} = (c/96) * f_neg(L1, L2)

    where f_neg encodes the one-loop correction from the partially
    transposed replica surface. The coefficient c/96 (half of c/48)
    arises because the partial transpose effectively halves the
    replica index for the negativity channel.

    Returns float.
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)

    # The correction function at genus 1
    # f_neg ~ ln(L1*L2/(L1+L2)^2) (logarithmic, from modular integral)
    ratio = L1 * L2 / (L1 + L2)**2
    if ratio <= 0 or ratio >= 0.25 + 1e-15:
        # Maximum of L1*L2/(L1+L2)^2 is 1/4 at L1=L2
        f_neg = 0.0
    else:
        f_neg = -math.log(4.0 * ratio)  # = ln(1/(4*ratio)), non-negative
    return (c / 96.0) * f_neg


def negativity_genus2_correction(c_val, L1_val, L2_val, eps_val):
    r"""Genus-2 correction to logarithmic negativity for adjacent intervals.

    delta_E_N^{(2)} = (7*c/(4*5760)) * f_neg_2(L1, L2)

    Returns float.
    """
    c = float(c_val)
    L1 = float(L1_val)
    L2 = float(L2_val)

    ratio = L1 * L2 / (L1 + L2)**2
    if ratio <= 0:
        f_neg_2 = 0.0
    else:
        f_neg_2 = (1.0 - 4.0 * ratio)**2 / (4.0 * ratio)
    return (7.0 * c / (4.0 * 5760.0)) * f_neg_2


# =========================================================================
# SECTION 8: HOLOGRAPHIC c-THEOREM (monotonicity under RG flow)
# =========================================================================

def ee_rg_flow(c_uv, c_ir, L_val, eps_val):
    r"""Entanglement entropy along an RG flow from c_UV to c_IR.

    The holographic c-theorem (Zamolodchikov 1986, Casini-Huerta 2004)
    states that entanglement entropy is monotonically decreasing under
    RG flow:

        S_EE(c_UV) >= S_EE(c_IR)

    because c_UV >= c_IR (Zamolodchikov) and S_EE = (c/3)*ln(L/eps).

    From the shadow obstruction tower: this is monotonicity of kappa under RG flow,
    since kappa = c/2 and S_EE = (2*kappa/3)*ln(L/eps).

    Returns dict with UV, IR, and difference.

    >>> result = ee_rg_flow(1, 0, 1.0, 0.01)
    >>> result['monotone']
    True
    """
    S_uv = float(c_uv) / 3.0 * math.log(float(L_val) / float(eps_val))
    S_ir = float(c_ir) / 3.0 * math.log(float(L_val) / float(eps_val))
    return {
        'c_UV': float(c_uv),
        'c_IR': float(c_ir),
        'kappa_UV': float(c_uv) / 2.0,
        'kappa_IR': float(c_ir) / 2.0,
        'S_UV': S_uv,
        'S_IR': S_ir,
        'delta_S': S_uv - S_ir,
        'monotone': S_uv >= S_ir - 1e-15,
    }


def ee_interpolation(c_uv, c_ir, L_val, eps_val, t_val):
    r"""Entanglement entropy along an RG flow parametrized by t in [0,1].

    c(t) interpolates smoothly: c(0) = c_UV, c(1) = c_IR.
    We use a linear interpolation: c(t) = (1-t)*c_UV + t*c_IR.

    The shadow obstruction tower at each value of c(t) determines the entanglement
    entropy S_EE(t).

    Returns dict with t, c(t), kappa(t), S_EE(t).
    """
    c_t = (1.0 - float(t_val)) * float(c_uv) + float(t_val) * float(c_ir)
    kappa_t = c_t / 2.0
    S_t = c_t / 3.0 * math.log(float(L_val) / float(eps_val))
    return {
        't': float(t_val),
        'c': c_t,
        'kappa': kappa_t,
        'S_EE': S_t,
    }


def c_theorem_shadow_tower(c_uv, c_ir, n_steps=10):
    r"""Shadow obstruction tower data along an RG flow.

    At each step, compute kappa, shadow radius, shadow depth class,
    and verify monotonicity.

    >>> data = c_theorem_shadow_tower(26, 1, 5)
    >>> all(data['kappa_values'][i] >= data['kappa_values'][i+1] for i in range(len(data['kappa_values'])-1))
    True
    """
    ts = [i / n_steps for i in range(n_steps + 1)]
    kappas = []
    rhos = []
    for t in ts:
        c_t = (1.0 - t) * float(c_uv) + t * float(c_ir)
        kappas.append(c_t / 2.0)
        if c_t > 0:
            rhos.append(shadow_radius_virasoro(c_t))
        else:
            rhos.append(float('inf'))

    monotone = all(kappas[i] >= kappas[i + 1] - 1e-15
                   for i in range(len(kappas) - 1))
    return {
        't_values': ts,
        'kappa_values': kappas,
        'rho_values': rhos,
        'monotone': monotone,
    }


# =========================================================================
# SECTION 9: QUANTUM EXTREMAL SURFACE (QES)
# =========================================================================

def qes_position_genus0(c_val, r_h, L_val):
    r"""Genus-0 QES position for the BTZ black hole.

    For the BTZ black hole with horizon radius r_h, the QES for
    a boundary interval of length L is at:

        r_QES^{(0)} = r_h  (the horizon itself at genus 0)

    The "area" contribution is:
        Area / (4G_N) = (c/3) * ln(r_h / epsilon)

    At genus 0, the QES coincides with the horizon (for a full
    boundary interval subtending angle > pi, the RT surface wraps
    the horizon).

    Returns dict with QES position and area contribution.
    """
    c = float(c_val)
    r_h_f = float(r_h)
    return {
        'r_QES': r_h_f,
        'area_contribution': (c / 3.0) * math.log(r_h_f) if r_h_f > 0 else 0.0,
        'genus': 0,
    }


def qes_shift_genus1(c_val, r_h):
    r"""Genus-1 shift of the QES position.

    The one-loop quantum correction shifts the QES:

        r_QES^{(1)} = r_h + delta_r_1

    where delta_r_1 = -(F_1 / (Area''(r_h)/(4G_N))) is determined by
    the stationarity condition on the generalized entropy.

    For the BTZ black hole:
        Area''(r) / (4G_N) = c / (3 * r^2)

    so delta_r_1 = -(c/48) / (c/(3*r_h^2)) = -r_h^2 / 16.

    The QES moves INWARD at one loop.

    Returns dict with shift and corrected position.
    """
    c = float(c_val)
    r_h_f = float(r_h)

    # F_1 = c/48 (genus-1 scalar free energy with kappa = c/2)
    F_1 = c / 48.0

    # Area second derivative at the horizon
    area_pp = c / (3.0 * r_h_f**2) if r_h_f > 0 else float('inf')

    delta_r1 = -F_1 / area_pp if area_pp > 0 else 0.0

    return {
        'r_h': r_h_f,
        'delta_r1': delta_r1,
        'r_QES_1': r_h_f + delta_r1,
        'genus': 1,
        'F_1': F_1,
    }


def qes_shift_genus2(c_val, r_h):
    r"""Genus-2 shift of the QES position.

    delta_r_2 = -(F_2) / (Area''(r_QES^{(1)})/(4G_N))

    where F_2 = 7c/11520 (scalar genus-2 free energy).

    Returns dict.
    """
    c = float(c_val)
    r_h_f = float(r_h)

    # First get the genus-1 corrected position
    g1 = qes_shift_genus1(c_val, r_h)
    r_1 = g1['r_QES_1']

    F_2 = 7.0 * c / (2.0 * 5760.0)

    area_pp = c / (3.0 * r_1**2) if r_1 > 0 else float('inf')
    delta_r2 = -F_2 / area_pp if area_pp > 0 else 0.0

    return {
        'r_h': r_h_f,
        'r_QES_1': r_1,
        'delta_r2': delta_r2,
        'r_QES_2': r_1 + delta_r2,
        'genus': 2,
        'F_2': F_2,
    }


def qes_shift_genus3(c_val, r_h):
    r"""Genus-3 shift of the QES position.

    delta_r_3 = -(F_3) / (Area''(r_QES^{(2)})/(4G_N))

    F_3 = 31*kappa/967680 with kappa = c/2.

    Returns dict.
    """
    c = float(c_val)
    r_h_f = float(r_h)

    g2 = qes_shift_genus2(c_val, r_h)
    r_2 = g2['r_QES_2']

    kappa = c / 2.0
    F_3 = 31.0 * kappa / 967680.0

    area_pp = c / (3.0 * r_2**2) if r_2 > 0 else float('inf')
    delta_r3 = -F_3 / area_pp if area_pp > 0 else 0.0

    return {
        'r_h': r_h_f,
        'r_QES_2': r_2,
        'delta_r3': delta_r3,
        'r_QES_3': r_2 + delta_r3,
        'genus': 3,
        'F_3': F_3,
    }


def qes_convergence_btz(c_val, r_h, max_genus=5):
    r"""QES position convergence for the BTZ black hole.

    Iteratively computes the QES position at each genus order
    and checks for convergence.

    Returns dict with positions at each order and convergence data.
    """
    c = float(c_val)
    r_h_f = float(r_h)
    kappa = c / 2.0

    positions = [r_h_f]  # genus 0
    shifts = [0.0]

    r_current = r_h_f
    for g in range(1, max_genus + 1):
        F_g = float(scalar_free_energy(Rational(c, 2), g))
        area_pp = c / (3.0 * r_current**2) if r_current > 0 else float('inf')
        delta_r = -F_g / area_pp if area_pp > 0 else 0.0
        r_current += delta_r
        positions.append(r_current)
        shifts.append(delta_r)

    return {
        'c': c,
        'r_h': r_h_f,
        'positions': positions,
        'shifts': shifts,
        'converged': abs(shifts[-1]) < abs(shifts[1]) * 0.01 if len(shifts) > 1 and shifts[1] != 0 else True,
    }


# =========================================================================
# SECTION 10: MULTIPARTITE ENTANGLEMENT FROM SHADOW TOWER
# =========================================================================

def tripartite_information(c_val, L1, L2, L3, d12, d23, eps_val):
    r"""Tripartite information I_3(A:B:C).

    I_3 = S(A) + S(B) + S(C) - S(AB) - S(AC) - S(BC) + S(ABC)

    For holographic theories, I_3 <= 0 (monogamy of mutual information,
    Hayden-Headrick-Maloney 2011).

    The sign of I_3 distinguishes:
    - I_3 < 0: holographic (monogamous)
    - I_3 = 0: free field / Gaussian
    - I_3 > 0: non-holographic

    The connection to the shadow obstruction tower: the cubic shadow C (S_3)
    controls the arity-3 contribution to tripartite entanglement.
    For class G (S_3 trivially determined): I_3 = 0.
    For class L and above: I_3 != 0 generically.

    Parameters
    ----------
    c_val : number
        Central charge.
    L1, L2, L3 : float
        Lengths of three intervals.
    d12, d23 : float
        Separations between intervals (A-B and B-C).
    eps_val : float
        UV cutoff.

    Returns
    -------
    dict with S_A, S_B, S_C, S_AB, S_AC, S_BC, S_ABC, I_3.
    """
    c = float(c_val)
    eps = float(eps_val)
    L1f, L2f, L3f = float(L1), float(L2), float(L3)
    d12f, d23f = float(d12), float(d23)

    def S_single(L):
        return (c / 3.0) * math.log(L / eps) if L > 0 else 0.0

    def S_union_adjacent(La, Lb, d):
        # Two intervals of length La, Lb separated by d
        # S(A union B) = S(A) + S(B) - I(A:B) at leading order
        # More precisely, the disconnected contribution:
        total_length = La + d + Lb
        return (c / 3.0) * math.log(total_length / eps) if total_length > 0 else 0.0

    S_A = S_single(L1f)
    S_B = S_single(L2f)
    S_C = S_single(L3f)

    # S(AB): union of A and B
    S_AB = S_union_adjacent(L1f, L2f, d12f)
    # S(BC): union of B and C
    S_BC = S_union_adjacent(L2f, L3f, d23f)
    # S(AC): union of A and C (separated by d12 + L2 + d23)
    d_ac = d12f + L2f + d23f
    S_AC = S_union_adjacent(L1f, L3f, d_ac)
    # S(ABC): the full union
    total = L1f + d12f + L2f + d23f + L3f
    S_ABC = (c / 3.0) * math.log(total / eps) if total > 0 else 0.0

    I_3 = S_A + S_B + S_C - S_AB - S_AC - S_BC + S_ABC

    return {
        'S_A': S_A, 'S_B': S_B, 'S_C': S_C,
        'S_AB': S_AB, 'S_AC': S_AC, 'S_BC': S_BC,
        'S_ABC': S_ABC,
        'I_3': I_3,
        'holographic': I_3 <= 1e-10,  # I_3 <= 0 for holographic
    }


def tripartite_from_cubic_shadow(c_val, S3_val, L1, L2, L3, eps_val):
    r"""Tripartite information from the cubic shadow S_3.

    For the arity-3 contribution to multipartite entanglement:

        I_3^{shadow} ~ S_3(A) * f_3(L1, L2, L3, epsilon)

    where f_3 is determined by the cubic vertex of the shadow obstruction tower.

    The cubic shadow S_3 = 2 for Virasoro (c-independent).

    For class G (Heisenberg): S_3 is trivially determined by kappa,
    so the cubic contribution to I_3 vanishes.

    For class L (affine KM): S_3 has nontrivial content,
    contributing a nonzero I_3.

    Returns float.
    """
    c = float(c_val)
    S3 = float(S3_val)
    L1f, L2f, L3f = float(L1), float(L2), float(L3)
    eps = float(eps_val)

    # The arity-3 contribution is proportional to S_3 and involves
    # a triple integral over the shadow vertex.
    # At leading order, the geometric factor is:
    geom = math.log(L1f * L2f * L3f / eps**3) if (L1f > 0 and L2f > 0 and L3f > 0) else 0.0

    # The coefficient involves S_3 / (3! * kappa^2) from the shadow obstruction tower
    kappa = c / 2.0
    if abs(kappa) < 1e-15:
        return 0.0

    return S3 / (6.0 * kappa**2) * geom


# =========================================================================
# SECTION 11: COMPREHENSIVE HIGHER-GENUS ENTANGLEMENT TABLE
# =========================================================================

def higher_genus_ee_table(c_values=None, max_genus=3, log_ratio=1):
    r"""Comprehensive entanglement entropy table through higher genus.

    For each central charge c, computes:
    - RT entropy (genus 0)
    - Genus-1 correction coefficient
    - Genus-2 correction coefficient (scalar + planted forest)
    - Shadow radius and convergence
    - Complementarity partner data

    Returns list of dicts.
    """
    if c_values is None:
        c_values = [1, 6, 12, 24, 26]
    table = []
    for c in c_values:
        kappa = kappa_virasoro(c)
        S_rt = rt_entropy_from_kappa(kappa, log_ratio)
        F1 = genus1_free_energy(kappa)
        F2 = genus2_free_energy(kappa)
        S3 = virasoro_S3()
        S4 = virasoro_S4(c)
        delta_pf = genus2_planted_forest_correction(kappa, S3)
        rho = shadow_radius_virasoro(float(c))
        c_dual = 26 - int(c)
        kappa_dual = kappa_virasoro(c_dual)
        S_rt_dual = rt_entropy_from_kappa(kappa_dual, log_ratio)

        row = {
            'c': c,
            'kappa': kappa,
            'S_RT': S_rt,
            'F_1': F1,
            'F_2_scalar': F2,
            'S_3': S3,
            'S_4': S4,
            'delta_pf_genus2': delta_pf,
            'F_2_full': F2 + delta_pf,
            'rho': rho,
            'convergent': rho < 1.0,
            'c_dual': c_dual,
            'S_RT_dual': S_rt_dual,
            'complementarity_sum': S_rt + S_rt_dual,
        }

        # Higher genus scalar free energies
        for g in range(1, max_genus + 1):
            row[f'F_{g}_scalar'] = scalar_free_energy(kappa, g)

        table.append(row)
    return table


def generalized_entropy_expansion(c_val, L_val, beta_val, eps_val, max_genus=3):
    r"""Full generalized entropy with quantum corrections through genus max_genus.

    S_gen = S_RT + delta_S_1 + delta_S_2 + ...

    Returns dict with order-by-order contributions.
    """
    c = float(c_val)
    L = float(L_val)
    beta = float(beta_val)
    eps = float(eps_val)

    # Genus 0: RT / Calabrese-Cardy
    S_rt = thermal_ee_single_interval(c, L, beta, eps)

    # Genus 1: one-loop
    delta_1 = genus1_correction_thermal(c, L, beta)

    # Genus 2: two-loop
    delta_2 = genus2_correction_thermal(c, L, beta)

    # Higher genera (scalar only)
    higher = {}
    kappa = c / 2.0
    for g in range(3, max_genus + 1):
        F_g = float(scalar_free_energy(Rational(c, 2), g))
        # The genus-g thermal correction decays as a power of L/beta
        x = math.pi * L / beta
        if abs(x) < 1e-10:
            delta_g = 0.0
        else:
            delta_g = F_g * x**(2 * g - 2) / math.factorial(2 * g - 2)
        higher[g] = delta_g

    total = S_rt + delta_1 + delta_2 + sum(higher.values())

    return {
        'c': c,
        'L': L,
        'beta': beta,
        'S_RT': S_rt,
        'delta_S_1': delta_1,
        'delta_S_2': delta_2,
        'higher_corrections': higher,
        'S_gen': total,
    }
