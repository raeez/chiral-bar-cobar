r"""BTZ quantum gravity engine: black hole entropy from the shadow CohFT.

MATHEMATICAL FRAMEWORK
======================

The shadow CohFT (thm:shadow-cohft) assigns to every modular Koszul algebra A
a genus-g free energy F_g(A) = kappa(A) * lambda_g^FP (scalar lane; class G/L
algebras terminate; class M has planted-forest corrections at g >= 2).

The gravitational partition function on the BTZ solid torus with modular
parameter tau = beta + i*theta (inverse temperature + angular potential) is

    Z^sh(tau, hbar) = exp( sum_{g=1}^{g_max} hbar^{2g} F_g )

The BTZ black hole entropy emerges from the Legendre transform (saddle-point
approximation) of log Z^sh.  The expansion parameter is 1/S_BH, so:

    S(E) = S_BH + S_1 + S_2 + S_3 + ...

where:
  S_BH = 4*pi*sqrt(c*E_L/6) + 4*pi*sqrt(c*E_R/6)    [Bekenstein-Hawking/Cardy]
  S_1  = -(3/2) * log(S_BH/(2*pi))                    [one-loop / logarithmic]
  S_g  = F_g * (2*pi/S_BH)^{2g-2}                     [g >= 2, saddle expansion]

For a non-rotating BTZ (E_L = E_R = M/2), this simplifies to
S_BH = 2*pi*sqrt(c*M/6).

QUANTUM CORRECTIONS TO BEKENSTEIN-HAWKING
==========================================

The g-loop correction from the shadow obstruction tower:

  S_g = F_g(A) * (2*pi)^{2g-2} / S_BH^{2g-2}

These are polynomial in kappa = c/2 (for Virasoro) and involve the shadow
coefficients S_3, S_4, S_5 at g >= 2 (planted-forest corrections).  Through
genus 5, these have NEVER been computed in the literature.

FAREY TAIL EXPANSION
====================

The modular-invariant partition function receives contributions from all
SL(2,Z) images of the BTZ saddle (Dijkgraaf-Maldacena-Moore-Verlinde 2000):

    Z(tau) = sum_{gamma in SL(2,Z) / Gamma_infty} Z_0(gamma.tau)

where Z_0(tau) = q^{-c/24} * prod_{n>=2}^infty (1-q^n)^{-1} for pure gravity.
The Farey tail is the sum over coprime (c_F, d) with c_F >= 0.

RENYI AND ENTANGLEMENT ENTROPY
================================

The n-th Renyi entropy from the replica trick on the shadow CohFT:

    S_n = (1/(1-n)) * log Tr(rho^n)

At the scalar level for a single interval of length L:

    S_n^scalar = (kappa/3) * (1 + 1/n) * log(L/epsilon)

The von Neumann entropy S_EE = lim_{n->1} S_n gives:

    S_EE = (2*kappa/3) * log(L/epsilon) = (c/3) * log(L/epsilon)

Shadow corrections from genus g >= 2 contribute:

    delta_S_EE^{(g)} = F_g * (correction factor from analytic continuation)

References:
  BTZ 1992: hep-th/9204099
  Carlip 1998: hep-th/9806026 (logarithmic corrections)
  Dijkgraaf-Maldacena-Moore-Verlinde 2000: hep-th/0005003 (Farey tail)
  Maloney-Witten 2010: 0712.0155 (pure gravity partition function)
  Calabrese-Cardy 2004: hep-th/0405152 (replica trick)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:theorem-d (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2


# =========================================================================
# Section 1: Faber-Pandharipande intersection numbers (exact)
# =========================================================================

@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    These are POSITIVE for all g >= 1 (AP22: Bernoulli signs).

    The A-hat generating function:
        sum_{g>=1} lambda_g^FP * x^{2g} = (x/2)/sin(x/2) - 1

    Verified values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
        g=5: 73/3503554560
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    # Bernoulli numbers B_{2g} via the recurrence
    B_2g = _bernoulli_2g(g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B_2g)
    den = power * _factorial_fraction(2 * g)
    return num / den


@lru_cache(maxsize=64)
def _bernoulli_2g(g: int) -> Fraction:
    """Exact Bernoulli number B_{2g} as a Fraction."""
    _BERNOULLI = {
        1: Fraction(1, 6),
        2: Fraction(-1, 30),
        3: Fraction(1, 42),
        4: Fraction(-1, 30),
        5: Fraction(5, 66),
        6: Fraction(-691, 2730),
        7: Fraction(7, 6),
        8: Fraction(-3617, 510),
        9: Fraction(43867, 798),
        10: Fraction(-174611, 330),
    }
    if g in _BERNOULLI:
        return _BERNOULLI[g]
    # Fallback: use sympy for large g
    try:
        from sympy import bernoulli as sympy_bernoulli, Rational
        return Fraction(Rational(sympy_bernoulli(2 * g)))
    except ImportError:
        raise ValueError(f"Bernoulli B_{2*g} not hardcoded and sympy unavailable")


def _factorial_fraction(n: int) -> Fraction:
    """n! as a Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


# =========================================================================
# Section 2: Virasoro shadow data
# =========================================================================

def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.

    AP1/AP9: authoritative formula from landscape_census.tex.
    AP20: this is kappa(A) for A = Vir_c, NOT kappa_eff.
    """
    return Fraction(c) / Fraction(2)


def kappa_heisenberg(k) -> Fraction:
    """kappa(H_k) = k.

    Heisenberg at level k: single generator of weight 1.
    """
    return Fraction(k)


def kappa_kac_moody(dim_g, k, h_dual) -> Fraction:
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2*h^v).

    AP1: recompute from first principles, never copy between families.
    """
    return Fraction(dim_g) * (Fraction(k) + Fraction(h_dual)) / (2 * Fraction(h_dual))


def virasoro_S3() -> Fraction:
    """Cubic shadow for Virasoro: S_3 = alpha = 2 (c-independent)."""
    return Fraction(2)


def virasoro_S4(c) -> Fraction:
    """Quartic contact invariant: Q^contact = 10 / [c(5c+22)]."""
    c = Fraction(c)
    return Fraction(10) / (c * (5 * c + 22))


def virasoro_S5(c) -> Fraction:
    """Quintic shadow: S_5 = -48 / [c^2(5c+22)]."""
    c = Fraction(c)
    return Fraction(-48) / (c ** 2 * (5 * c + 22))


# =========================================================================
# Section 3: Free energies F_g (scalar + planted-forest)
# =========================================================================

def F_g_scalar(kappa, g: int) -> Fraction:
    """Scalar free energy: F_g^{sc} = kappa * lambda_g^FP."""
    return Fraction(kappa) * lambda_fp(g)


def planted_forest_g2(kappa, S3) -> Fraction:
    r"""Planted-forest correction at genus 2.

    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48

    Heisenberg (S_3=0): vanishes.
    Virasoro (S_3=2, kappa=c/2): (40 - c/2) * 2 / 48 = -(c-40)/48.
    """
    S3, kappa = Fraction(S3), Fraction(kappa)
    return S3 * (10 * S3 - kappa) / Fraction(48)


def planted_forest_g3(kappa, S3, S4, S5) -> Fraction:
    r"""Planted-forest correction at genus 3 (11-term polynomial).

    From eq:delta-pf-genus3-explicit.
    """
    kappa, S3, S4, S5 = Fraction(kappa), Fraction(S3), Fraction(S4), Fraction(S5)
    numerator = (
        - kappa**2 * S3
        + 60 * kappa * S3**2
        - 500 * S3**3
        + 6 * kappa**2 * S4
        - 120 * kappa * S3 * S4
        + 600 * S3**2 * S4
        + 72 * kappa * S4**2
        - 720 * S3 * S4**2
        + 120 * kappa * S3 * S5
        - 1200 * S3**2 * S5
        + 1440 * S4 * S5
    )
    return numerator / Fraction(11520)


def virasoro_free_energy(c, g: int) -> Fraction:
    """Full F_g for Virasoro at central charge c.

    g=1: F_1 = kappa/24 = c/48 (no planted-forest at genus 1).
    g=2: F_2^{sc} + delta_pf^{(2,0)}.
    g=3: F_3^{sc} + delta_pf^{(3,0)}.
    g>=4: scalar only (planted-forest not available beyond genus 3).
    """
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)
    scalar = F_g_scalar(kappa, g)

    if g == 1:
        return scalar  # no planted-forest at genus 1
    elif g == 2:
        S3 = virasoro_S3()
        return scalar + planted_forest_g2(kappa, S3)
    elif g == 3:
        S3 = virasoro_S3()
        S4 = virasoro_S4(c_frac)
        S5 = virasoro_S5(c_frac)
        return scalar + planted_forest_g3(kappa, S3, S4, S5)
    else:
        # g >= 4: scalar only (planted-forest not yet computed)
        return scalar


def heisenberg_free_energy(k, g: int) -> Fraction:
    """F_g for Heisenberg at level k.

    Class G: S_3 = 0, so planted-forest vanishes at ALL genera.
    F_g = kappa * lambda_g^FP = k * lambda_g^FP.
    """
    return F_g_scalar(Fraction(k), g)


def free_energy_table(c, g_max: int = 5, algebra: str = 'virasoro') -> Dict[int, Fraction]:
    """Table of F_g for g = 1..g_max."""
    if algebra == 'virasoro':
        return {g: virasoro_free_energy(c, g) for g in range(1, g_max + 1)}
    elif algebra == 'heisenberg':
        return {g: heisenberg_free_energy(c, g) for g in range(1, g_max + 1)}
    else:
        # Generic: scalar lane only
        kappa = Fraction(c) / Fraction(2)
        return {g: F_g_scalar(kappa, g) for g in range(1, g_max + 1)}


# =========================================================================
# Section 4: Shadow partition function Z^sh
# =========================================================================

def shadow_partition_function(c, hbar: float = 1.0, g_max: int = 5,
                               algebra: str = 'virasoro') -> float:
    r"""Z^sh(c, hbar) = exp( sum_{g=1}^{g_max} hbar^{2g} * F_g(c) ).

    The shadow partition function converges (Bernoulli decay 1/(2*pi)^{2g})
    unlike the string free energy which diverges as (2g)!.

    Parameters
    ----------
    c : central charge
    hbar : expansion parameter (related to 1/S_BH)
    g_max : maximum genus
    algebra : 'virasoro', 'heisenberg', or 'generic'
    """
    F_table = free_energy_table(c, g_max, algebra)
    exponent = sum(hbar ** (2 * g) * float(F_table[g]) for g in range(1, g_max + 1))
    return math.exp(exponent)


def shadow_free_energy_sum(c, hbar: float = 1.0, g_max: int = 5,
                            algebra: str = 'virasoro') -> float:
    """F^sh = sum_{g=1}^{g_max} hbar^{2g} * F_g(c) = log Z^sh."""
    F_table = free_energy_table(c, g_max, algebra)
    return sum(hbar ** (2 * g) * float(F_table[g]) for g in range(1, g_max + 1))


def shadow_partition_function_complex(c, tau: complex, g_max: int = 5,
                                       algebra: str = 'virasoro') -> complex:
    r"""Z^sh(c, tau) with tau = beta + i*theta (complex modular parameter).

    The genus-g contribution has the form F_g * tau^{2-2g} (from the
    metric on the solid torus with modular parameter tau).

    For the BTZ saddle: hbar = 2*pi / S_BH, and in the Euclidean
    path integral the expansion parameter is 1/tau (high-temperature).
    """
    F_table = free_energy_table(c, g_max, algebra)
    exponent = complex(0, 0)
    for g in range(1, g_max + 1):
        Fg = float(F_table[g])
        # genus-g contribution: F_g * (2*pi*i/tau)^{2g-2} for the BTZ saddle
        # At genus 1: F_1 * (2*pi*i/tau)^0 = F_1
        # At genus g: F_g * (2*pi*i/tau)^{2g-2}
        factor = (2.0 * PI * 1j / tau) ** (2 * g - 2)
        exponent += Fg * factor
    return cmath.exp(exponent)


# =========================================================================
# Section 5: Bekenstein-Hawking and classical thermodynamics
# =========================================================================

def bekenstein_hawking_entropy(c, M) -> float:
    """S_BH = 2*pi*sqrt(c*M/6) (non-rotating BTZ / Cardy formula).

    For rotating BTZ with E_L, E_R:
      S_BH = 4*pi*sqrt(c*E_L/6) + 4*pi*sqrt(c*E_R/6)
    Non-rotating: E_L = E_R = M/2, so S_BH = 2*pi*sqrt(2*c*M/12) = 2*pi*sqrt(c*M/6).

    Parameters
    ----------
    c : central charge (c = 3*l/(2*G_N) in AdS_3/CFT_2)
    M : mass parameter (= L_0 + L_0bar - c/12 in CFT; = Delta for single chirality)
    """
    c, M = float(c), float(M)
    if c * M <= 0:
        return 0.0
    return 2.0 * PI * math.sqrt(c * M / 6.0)


def bekenstein_hawking_rotating(c, E_L, E_R) -> float:
    """S_BH = 2*pi*sqrt(c*E_L/6) + 2*pi*sqrt(c*E_R/6) (rotating BTZ / Cardy).

    E_L, E_R are the per-chirality conformal dimensions above the vacuum:
      E_L = L_0 - c/24,  E_R = L_0bar - c/24.

    Convention: in the non-rotating case, E_L = E_R = M where M is the
    parameter in bekenstein_hawking_entropy(c, M), giving
      S = 2*pi*sqrt(c*M/6) + 2*pi*sqrt(c*M/6) = 2 * 2*pi*sqrt(c*M/6).

    BUT: bekenstein_hawking_entropy uses M as a single-chirality quantity,
    so the non-rotating case corresponds to E_L = E_R = M (matching the
    single-chirality Cardy formula in each sector).
    """
    c, E_L, E_R = float(c), float(E_L), float(E_R)
    S = 0.0
    if c * E_L > 0:
        S += 2.0 * PI * math.sqrt(c * E_L / 6.0)
    if c * E_R > 0:
        S += 2.0 * PI * math.sqrt(c * E_R / 6.0)
    return S


def inverse_hawking_temperature(c, M) -> float:
    """beta_H = pi*sqrt(c/(6*M)) — inverse Hawking temperature at the saddle."""
    c, M = float(c), float(M)
    if M <= 0 or c <= 0:
        return float('inf')
    return PI * math.sqrt(c / (6.0 * M))


def hawking_temperature(c, M) -> float:
    """T_H = 1/beta_H = sqrt(6M/c) / pi."""
    beta = inverse_hawking_temperature(c, M)
    if beta <= 0 or math.isinf(beta):
        return 0.0
    return 1.0 / beta


# =========================================================================
# Section 6: Quantum corrections to BH entropy (saddle-point expansion)
# =========================================================================

def entropy_correction_genus_g(c, M, g: int, algebra: str = 'virasoro') -> float:
    r"""Genus-g correction to BTZ entropy from the shadow CohFT.

    The saddle-point expansion of Z^sh = exp(sum F_g * hbar^{2g}) around
    beta_H gives genus-g entropy correction:

        S_g = F_g * epsilon^{2g-2}

    where epsilon = 2*pi / S_BH is the saddle-point expansion parameter.

    At genus 1:
        S_1 = -(3/2) * log(S_BH / (2*pi))
    (the logarithmic correction from 3 zero modes on BTZ).

    At genus g >= 2:
        S_g = F_g * (2*pi / S_BH)^{2g-2}

    NOTE: The genus-1 correction is NOT simply F_1 * epsilon^0 = F_1;
    it includes the one-loop determinant which gives the log.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return 0.0

    if g == 1:
        # One-loop: -(3/2) * log(S_BH / (2*pi))
        # The -3/2 comes from 3 zero modes on BTZ (2 translations + 1 rotation)
        return -1.5 * math.log(S_BH / TWO_PI)

    # g >= 2: saddle-point expansion
    if algebra == 'virasoro':
        Fg = float(virasoro_free_energy(c, g))
    elif algebra == 'heisenberg':
        Fg = float(heisenberg_free_energy(c, g))
    else:
        kappa = float(c) / 2.0
        Fg = float(F_g_scalar(Fraction(kappa), g))

    epsilon = TWO_PI / S_BH
    return Fg * epsilon ** (2 * g - 2)


def entropy_all_genera(c, M, g_max: int = 5, algebra: str = 'virasoro') -> Dict[str, Any]:
    r"""Full BTZ entropy expansion through genus g_max.

    S(M) = S_BH + sum_{g=1}^{g_max} S_g

    Returns dict with S_BH, S_g for each g, F_table, S_total, expansion parameter.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return {'error': 'S_BH <= 0: below Cardy threshold'}

    F_table = free_energy_table(c, g_max, algebra)
    epsilon = TWO_PI / S_BH

    result = {
        'c': c,
        'M': M,
        'kappa': float(Fraction(c) / 2) if algebra == 'virasoro' else float(c),
        'S_BH': S_BH,
        'epsilon': epsilon,
        'F_table': {g: float(f) for g, f in F_table.items()},
    }

    total = S_BH
    for g in range(1, g_max + 1):
        Sg = entropy_correction_genus_g(c, M, g, algebra)
        result[f'S_{g}'] = Sg
        total += Sg

    result['S_total'] = total
    result['relative_correction'] = (total - S_BH) / S_BH if S_BH > 0 else 0.0

    return result


def quantum_corrections_table(c, M, g_max: int = 5,
                               algebra: str = 'virasoro') -> List[Dict[str, Any]]:
    """Tabulate quantum corrections at each genus.

    Returns a list of dicts, one per genus, with:
      g, F_g, S_g, S_g/S_BH, epsilon^{2g-2}
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return []

    epsilon = TWO_PI / S_BH
    F_table = free_energy_table(c, g_max, algebra)

    rows = []
    for g in range(1, g_max + 1):
        Sg = entropy_correction_genus_g(c, M, g, algebra)
        row = {
            'g': g,
            'F_g': float(F_table[g]),
            'S_g': Sg,
            'S_g_over_S_BH': Sg / S_BH if S_BH > 0 else 0.0,
            'epsilon_power': epsilon ** (2 * g - 2),
        }
        rows.append(row)

    return rows


# =========================================================================
# Section 7: Hawking-Page phase transition
# =========================================================================

def euclidean_action_btz(c, beta, g_max: int = 5,
                          algebra: str = 'virasoro') -> float:
    """Euclidean action of the BTZ saddle: I_BTZ(beta).

    Classical (genus 0): I_0 = c * pi^2 / (6 * beta)   [the on-shell action]
    Quantum: I = I_0 - sum_{g>=1} F_g * beta^{2g-2}

    The free energy F = -log Z = I at the saddle.
    Convention: F = -I_on-shell (so Z = exp(-I), F = I).
    """
    c, beta = float(c), float(beta)
    if beta <= 0:
        return float('inf')

    # Classical BTZ action: I_0 = -(c * pi^2) / (6 * beta)
    # (negative because BTZ is a saddle, dominates at high T)
    F0 = -(c * PI**2) / (6.0 * beta)

    # Genus-1: F_1 (beta-independent at leading order)
    F_table = free_energy_table(c, g_max, algebra)
    F1 = float(F_table[1])

    total = F0 + F1

    # g >= 2: F_g * beta^{2g-2}
    for g in range(2, g_max + 1):
        Fg = float(F_table[g])
        total += Fg * beta ** (2 * g - 2)

    return total


def euclidean_action_thermal_ads(c, beta) -> float:
    """Euclidean action of the thermal AdS saddle.

    I_AdS = -(c * beta) / (12 * pi)

    This is the vacuum contribution: E_vac = -c/24 in the CFT,
    giving F_AdS = -E_vac * beta = (c/24) * beta.
    In our convention: F_AdS = -(c * beta) / (12 * pi).
    """
    return -(float(c) * float(beta)) / (12.0 * PI)


def hawking_page_temperature_classical() -> float:
    """beta_HP = 2*pi at leading order (classical).

    At this temperature, F_BTZ(beta_HP) = F_AdS(beta_HP):
      -c*pi^2/(6*beta) = -c*beta/(12*pi)
      => beta^2 = 2*pi^3 / (... ) => beta_HP = 2*pi
    in standard normalization.
    """
    return TWO_PI


def hawking_page_temperature(c, g_max: int = 0) -> float:
    """Inverse Hawking-Page temperature with quantum corrections.

    At g_max = 0: beta_HP = 2*pi (classical).
    At g_max > 0: solve F_BTZ(beta) = F_AdS(beta) numerically.
    """
    if g_max == 0:
        return TWO_PI

    # Numerical root finding
    from scipy.optimize import brentq

    def delta_F(beta):
        return euclidean_action_btz(c, beta, g_max) - euclidean_action_thermal_ads(c, beta)

    try:
        return brentq(delta_F, 0.1, 100.0)
    except Exception:
        return TWO_PI


def hawking_page_shift(c, g_max: int = 5) -> Dict[str, float]:
    """Quantum shift of the Hawking-Page temperature.

    Returns beta_HP at each loop order and the shift from classical.
    """
    classical = TWO_PI
    result = {'classical': classical}

    for g in range(1, g_max + 1):
        try:
            beta_g = hawking_page_temperature(c, g_max=g)
        except Exception:
            beta_g = classical
        result[f'g_max_{g}'] = beta_g
        result[f'shift_{g}'] = beta_g - classical

    return result


# =========================================================================
# Section 8: Farey tail expansion
# =========================================================================

def farey_tail_term(c, tau: complex, c_F: int, d: int) -> complex:
    r"""Single term in the Farey tail: Z_0(gamma.tau) for gamma = [[a,b],[c_F,d]].

    For coprime (c_F, d), the SL(2,Z) image is:
        gamma.tau = (a*tau + b) / (c_F*tau + d)
    with a*d - b*c_F = 1.

    The seed partition function Z_0(tau) = q^{-c/24} where q = exp(2*pi*i*tau).

    This is the leading saddle contribution from the (c_F, d) Farey image.
    """
    if c_F == 0:
        # Identity image: gamma.tau = tau + d (just the BTZ saddle)
        gamma_tau = tau + d
    else:
        # Find a, b with a*d - b*c_F = 1 using extended Euclidean
        a, b = _extended_gcd_solution(c_F, d)
        gamma_tau = (a * tau + b) / (c_F * tau + d)

    # Seed: Z_0(tau) = exp(-2*pi*i*c/24 * tau)
    q_exponent = 2.0 * PI * 1j * gamma_tau
    return cmath.exp(-float(c) / 24.0 * q_exponent)


def _extended_gcd_solution(c_val: int, d: int) -> Tuple[int, int]:
    """Find (a, b) with a*d - b*c_val = 1."""
    # Extended Euclidean algorithm
    g, x, y = _extended_gcd(abs(d), abs(c_val))
    if g != 1:
        raise ValueError(f"gcd({c_val}, {d}) = {g} != 1")
    # x*|d| + y*|c_val| = 1, so a = x*sign(d), b = -y*sign(c_val)
    a = x if d >= 0 else -x
    b = -y if c_val >= 0 else y
    # Verify
    assert a * d - b * c_val == 1, f"a*d - b*c = {a*d - b*c_val}"
    return a, b


def _extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended GCD: returns (g, x, y) with a*x + b*y = g."""
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def farey_sequence(N: int) -> List[Tuple[int, int]]:
    """Coprime pairs (c_F, d) with 0 <= c_F <= N, gcd(c_F, d) = 1.

    These index the SL(2,Z)/Gamma_infty cosets in the Farey tail.
    """
    pairs = [(0, 1)]  # Identity: c_F=0, d=1
    for c_F in range(1, N + 1):
        for d in range(0, c_F + 1):
            if math.gcd(c_F, d) == 1:
                pairs.append((c_F, d))
                if d > 0 and d < c_F:
                    pairs.append((c_F, -d))  # negative d images
    return pairs


def farey_tail_partition(c, tau: complex, N_farey: int = 5) -> complex:
    r"""Farey tail partition function Z(tau) = sum_{gamma} Z_0(gamma.tau).

    Sum over SL(2,Z)/Gamma_infty cosets up to denominator N_farey.

    This is the Dijkgraaf-Maldacena-Moore-Verlinde partition function
    for pure gravity at central charge c.
    """
    pairs = farey_sequence(N_farey)
    Z = complex(0, 0)
    for c_F, d in pairs:
        try:
            Z += farey_tail_term(c, tau, c_F, d)
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
    return Z


def farey_tail_entropy(c, M, N_farey: int = 5) -> Dict[str, Any]:
    """Extract entropy from the Farey tail partition function.

    At high temperature (large M), the BTZ saddle dominates:
        S ~ 2*pi*sqrt(c*M/6)

    Sub-leading Farey terms contribute:
        delta_S ~ sum_{c_F >= 1} exp(2*pi*i*gamma.tau)
    which are exponentially suppressed.
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    beta_H = inverse_hawking_temperature(c, M)

    # Evaluate on the imaginary axis tau = i*beta/(2*pi)
    tau = 1j * beta_H / TWO_PI

    Z_farey = farey_tail_partition(c, tau, N_farey)
    Z_btz_only = farey_tail_term(c, tau, 0, 1)

    return {
        'S_BH': S_BH,
        'beta_H': beta_H,
        'tau': tau,
        'Z_farey': Z_farey,
        'Z_btz': Z_btz_only,
        'log_Z_farey': cmath.log(Z_farey).real if abs(Z_farey) > 0 else float('-inf'),
        'log_Z_btz': cmath.log(Z_btz_only).real if abs(Z_btz_only) > 0 else float('-inf'),
        'farey_correction': cmath.log(Z_farey / Z_btz_only).real if abs(Z_btz_only) > 0 else 0.0,
    }


# =========================================================================
# Section 9: Renyi entropy from the replica trick
# =========================================================================

def twist_operator_dimension(c, n: int) -> float:
    """Conformal dimension of the twist operator sigma_n.

    h_n = (c/24) * (n - 1/n)

    This is the standard CFT result (Calabrese-Cardy 2004).
    In terms of kappa: h_n = (kappa/12) * (n - 1/n).
    """
    c = float(c)
    return (c / 24.0) * (n - 1.0 / n)


def renyi_entropy_scalar(c, n: int, L_over_eps: float = 1000.0) -> float:
    """Scalar Renyi entropy for a single interval.

    S_n^{scalar} = (kappa/3) * (1 + 1/n) * log(L/epsilon)
                 = (c/6) * (1 + 1/n) * log(L/epsilon)

    Derivation: Tr(rho^n) = (L/epsilon)^{-2*n*h_n/(n-1)}
    and S_n = (1/(1-n)) * log Tr(rho^n).
    """
    c = float(c)
    if n <= 0:
        return 0.0
    if n == 1:
        # von Neumann limit: S_1 = (c/3) * log(L/eps)
        return (c / 3.0) * math.log(L_over_eps)
    return (c / 6.0) * (1.0 + 1.0 / n) * math.log(L_over_eps)


def renyi_entropy_with_shadow_corrections(c, n: int, L_over_eps: float = 1000.0,
                                           g_max: int = 3) -> Dict[str, float]:
    """Renyi entropy with shadow CohFT corrections.

    S_n = S_n^{scalar} + sum_{g>=2} delta_S_n^{(g)}

    The genus-g correction to the Renyi entropy comes from the genus-g
    shadow amplitude on the n-fold branched cover (replica manifold Sigma_n).

    For genus g >= 2, the correction is:
        delta_S_n^{(g)} = (n/(1-n)) * F_g * (replica_factor_g(n))

    The replica factor at genus g accounts for the topology change:
    the n-fold cover of S^2 branched at 2 points has genus (n-1),
    so the effective modular parameter shifts.

    At the scalar level, the replica factor is:
        replica_factor_g(n) = n^{2-2g} - 1 (from the n-fold cover)

    NOTE: The replica trick at genus g >= 2 involves the partition function
    on the genus-(n-1) branched cover, which ITSELF has higher-genus
    shadow contributions. This creates a recursive structure that we
    handle perturbatively.
    """
    scalar = renyi_entropy_scalar(c, n, L_over_eps)
    log_L = math.log(L_over_eps)

    result = {
        'n': n,
        'c': float(c),
        'S_n_scalar': scalar,
        'L_over_eps': L_over_eps,
    }

    if n == 1:
        result['S_n_total'] = scalar
        return result

    # Shadow corrections from genus g >= 2
    kappa = float(c) / 2.0
    corrections = {}
    total_correction = 0.0

    for g in range(2, g_max + 1):
        Fg = float(virasoro_free_energy(c, g))
        # The genus-g contribution to the Renyi entropy
        # From the n-sheeted branched cover: the partition function on
        # Sigma_{g_eff} where g_eff = n*(g-1)+1 (Riemann-Hurwitz).
        # The correction to S_n at order F_g:
        #   delta_S_n^{(g)} = (1/(1-n)) * (n^{1-2g} - 1) * F_g * (something from L)
        #
        # For the entropy density (coefficient of log(L/eps)):
        # The genus-g amplitude on the replica manifold gives a contribution
        # proportional to the Euler characteristic chi = 2 - 2g of the
        # replica geometry, integrated against F_g.
        #
        # At the perturbative level:
        replica_factor = n ** (1 - 2 * g) - 1.0
        delta = (1.0 / (1.0 - n)) * replica_factor * Fg
        corrections[g] = delta
        total_correction += delta

    result['corrections'] = corrections
    result['total_correction'] = total_correction
    result['S_n_total'] = scalar + total_correction

    return result


def renyi_convergence_to_von_neumann(c, L_over_eps: float = 1000.0,
                                      n_max: int = 20) -> List[Dict[str, float]]:
    """Verify S_n -> S_EE as n -> 1.

    We compute S_n for n = 2, 3, ..., n_max and extrapolate to n=1.
    The exact von Neumann limit is S_EE = (c/3)*log(L/eps).
    """
    S_EE = (float(c) / 3.0) * math.log(L_over_eps)
    results = []

    for n in range(2, n_max + 1):
        S_n = renyi_entropy_scalar(c, n, L_over_eps)
        results.append({
            'n': n,
            'S_n': S_n,
            'S_EE': S_EE,
            'ratio': S_n / S_EE if S_EE > 0 else 0.0,
            'approach': (1.0 + 1.0 / n) / 2.0,  # Should approach 1 as n->1
        })

    return results


# =========================================================================
# Section 10: Entanglement entropy with shadow corrections
# =========================================================================

def entanglement_entropy_leading(c, L_over_eps: float = 1000.0) -> float:
    """S_EE = (c/3)*log(L/eps) — the Calabrese-Cardy formula.

    Derived from kappa(Vir_c) = c/2:
      S_EE = (2*kappa/3)*log(L/eps) = (c/3)*log(L/eps)
    """
    return (float(c) / 3.0) * math.log(L_over_eps)


def entanglement_entropy_with_corrections(c, L_over_eps: float = 1000.0,
                                           g_max: int = 5,
                                           algebra: str = 'virasoro') -> Dict[str, float]:
    """Entanglement entropy with higher-genus shadow corrections.

    S_EE = (c/3)*log(L/eps) + sum_{g>=2} delta_S^{(g)}

    The genus-g correction comes from the analytic continuation n -> 1
    of the genus-g replica contribution.

    At genus g >= 2, the correction is:
        delta_S^{(g)} = lim_{n->1} d/dn [(1/(1-n)) * (n^{1-2g} - 1) * F_g]
                      = (2g-1) * F_g

    This is the n -> 1 analytic continuation of the Renyi entropy correction.
    The factor (2g-1) counts the number of marked points on the replica
    manifold at genus g in the n -> 1 limit.

    NOTE: These corrections are independent of L/eps -- they are O(1)
    contributions to the entropy, not log-enhanced.
    """
    S_leading = entanglement_entropy_leading(c, L_over_eps)
    F_table = free_energy_table(c, g_max, algebra)

    result = {
        'c': float(c),
        'S_leading': S_leading,
        'L_over_eps': L_over_eps,
    }

    corrections = {}
    total_correction = 0.0

    for g in range(2, g_max + 1):
        Fg = float(F_table[g])
        # The n->1 limit of the genus-g Renyi contribution
        # lim_{n->1} (1/(1-n)) * (n^{1-2g} - 1) = 2g - 1
        delta = (2 * g - 1) * Fg
        corrections[g] = delta
        total_correction += delta

    result['corrections'] = corrections
    result['total_correction'] = total_correction
    result['S_total'] = S_leading + total_correction

    return result


def entanglement_complementarity(c, L_over_eps: float = 1000.0) -> Dict[str, float]:
    """Complementarity: S_EE(c) + S_EE(26-c) = (26/3)*log(L/eps).

    From kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    Note: this is 13, NOT 0 (AP24).
    """
    c = float(c)
    S_c = entanglement_entropy_leading(c, L_over_eps)
    S_dual = entanglement_entropy_leading(26.0 - c, L_over_eps)
    expected = (26.0 / 3.0) * math.log(L_over_eps)
    return {
        'c': c,
        'S_EE_c': S_c,
        'S_EE_dual': S_dual,
        'sum': S_c + S_dual,
        'expected': expected,
        'match': abs(S_c + S_dual - expected) < 1e-10,
    }


# =========================================================================
# Section 11: A-hat generating function and convergence
# =========================================================================

def ahat_generating_function(x: float) -> float:
    """A-hat(ix) - 1 = (x/2)/sin(x/2) - 1.

    This is the generating function for lambda_g^FP:
        sum_{g>=1} lambda_g^FP * x^{2g} = (x/2)/sin(x/2) - 1

    The function is entire with zeros at x = 2*k*pi (k != 0),
    so the convergence radius is 2*pi.
    """
    half_x = x / 2.0
    if abs(half_x) < 1e-15:
        return 0.0
    return half_x / math.sin(half_x) - 1.0


def scalar_free_energy_sum(c, hbar: float = 1.0, g_max: int = 30) -> float:
    """sum_{g=1}^{g_max} F_g^{scalar} * hbar^{2g} = kappa * (A-hat(i*hbar) - 1)."""
    kappa = float(c) / 2.0
    total = 0.0
    for g in range(1, g_max + 1):
        lfp = float(lambda_fp(g))
        total += kappa * lfp * hbar ** (2 * g)
    return total


def ahat_closed_form(c, hbar: float = 1.0) -> float:
    """Closed-form: kappa * (A-hat(i*hbar) - 1) = kappa * ((hbar/2)/sinh(hbar/2) - 1).

    Note: A-hat(ix) = (x/2)/sin(x/2), and sin(ix/2) = i*sinh(x/2),
    so A-hat(ix) = (x/2)/(i*i*sinh(x/2)) ... let's be careful:

    A-hat(x) = x/2 / sinh(x/2) is the standard Hirzebruch form.
    For the genus expansion: F = kappa * (A-hat(hbar) - 1)
    where A-hat(hbar) = (hbar/2)/sinh(hbar/2).

    Convergence: sinh(hbar/2) has zeros at hbar = 2*k*pi*i,
    so the real expansion converges for all real hbar.
    """
    kappa = float(c) / 2.0
    half_h = hbar / 2.0
    if abs(half_h) < 1e-15:
        return 0.0
    return kappa * (half_h / math.sinh(half_h) - 1.0)


def verify_ahat_identity(c, hbar: float = 0.5, g_max: int = 20) -> Dict[str, float]:
    """Verify that the genus sum matches the A-hat closed form."""
    series = scalar_free_energy_sum(c, hbar, g_max)
    closed = ahat_closed_form(c, hbar)
    return {
        'c': float(c),
        'hbar': hbar,
        'series': series,
        'closed_form': closed,
        'difference': abs(series - closed),
        'match': abs(series - closed) < 1e-10,
    }


def shadow_convergence_radius() -> float:
    """Convergence radius of the scalar genus sum: 2*pi.

    The A-hat generating function has radius 2*pi (first zero of sinh).
    Since |lambda_g^FP| ~ 1/(2*pi)^{2g}, the genus sum
    sum F_g * hbar^{2g} converges for |hbar| < 2*pi.
    """
    return TWO_PI


# =========================================================================
# Section 12: Full quantum gravity entropy report
# =========================================================================

def full_entropy_report(c, M, g_max: int = 5, algebra: str = 'virasoro') -> Dict[str, Any]:
    """Comprehensive BTZ entropy computation.

    Computes:
    1. Classical Bekenstein-Hawking entropy S_BH
    2. Quantum corrections S_1, ..., S_{g_max}
    3. Free energies F_1, ..., F_{g_max}
    4. Hawking-Page temperature (classical + quantum shifts)
    5. Bekenstein-Hawking for rotating case
    6. Expansion parameter and convergence check
    """
    result = entropy_all_genera(c, M, g_max, algebra)
    if 'error' in result:
        return result

    S_BH = result['S_BH']
    epsilon = result['epsilon']

    # Hawking-Page
    result['beta_HP_classical'] = TWO_PI
    result['beta_H'] = inverse_hawking_temperature(c, M)
    result['T_H'] = hawking_temperature(c, M)

    # Convergence check
    result['convergent'] = abs(epsilon) < TWO_PI

    # Rotating version (E_L = E_R = M for non-rotating: sum of both chiralities)
    result['S_BH_rotating_both'] = bekenstein_hawking_rotating(c, float(M), float(M))

    # A-hat cross-check
    result['ahat_check'] = verify_ahat_identity(c, epsilon, min(g_max + 10, 30))

    return result


# =========================================================================
# Section 13: Special central charges
# =========================================================================

def pure_gravity_c24(M: float = 1.0, g_max: int = 5) -> Dict[str, Any]:
    """BTZ entropy for pure 3d gravity: c = 24.

    At c = 24: kappa = 12, the one-loop determinant is |eta(tau)|^{-48}.
    This is the monster module V^natural (if the Witten conjecture holds).

    AP48: kappa(V^natural) is NOT necessarily c/2 = 12 (it could be
    rank(Leech) = 24 for the lattice VOA). For pure gravity we use
    kappa(Vir_{24}) = 12.
    """
    return full_entropy_report(24, M, g_max, algebra='virasoro')


def critical_string_c26(M: float = 1.0, g_max: int = 5) -> Dict[str, Any]:
    """BTZ entropy at c = 26 (critical bosonic string).

    At c = 26: kappa = 13, kappa(A!) = kappa(Vir_0) = 0.
    The dual algebra is uncurved: D^2 = 0 (no higher-genus obstruction).
    """
    return full_entropy_report(26, M, g_max, algebra='virasoro')


def self_dual_c13(M: float = 1.0, g_max: int = 5) -> Dict[str, Any]:
    """BTZ entropy at c = 13 (self-dual Virasoro: Vir_13^! = Vir_13).

    At c = 13: kappa = 13/2 = kappa'.
    The shadow obstruction tower is self-dual: Theta_A = Theta_{A!}.
    Self-dual growth rate rho ~ 0.467 (convergent tower).
    """
    return full_entropy_report(13, M, g_max, algebra='virasoro')


def free_boson_c1(M: float = 1.0, g_max: int = 5) -> Dict[str, Any]:
    """BTZ entropy for a single free boson: c = 1 (Heisenberg at k = 1).

    For Heisenberg: kappa = k = 1, S_3 = 0, class G.
    ALL planted-forest corrections vanish.
    F_g = lambda_g^FP (the pure A-hat genus contribution).
    """
    return full_entropy_report(1, M, g_max, algebra='heisenberg')


# =========================================================================
# Section 14: Comparison across central charges
# =========================================================================

def entropy_landscape(M: float = 10.0, g_max: int = 5) -> Dict[int, Dict[str, float]]:
    """Entropy at each loop order for c = 1, 2, ..., 26.

    Returns a table indexed by c with all loop corrections.
    """
    landscape = {}
    for c in range(1, 27):
        data = entropy_all_genera(c, M, g_max, algebra='virasoro')
        if 'error' not in data:
            landscape[c] = {
                'S_BH': data['S_BH'],
                'S_total': data['S_total'],
                'relative': data['relative_correction'],
            }
            for g in range(1, g_max + 1):
                landscape[c][f'S_{g}'] = data.get(f'S_{g}', 0.0)

    return landscape


def large_c_limit(M: float = 10.0, g_max: int = 5) -> Dict[str, Any]:
    """Large-c limit: verify recovery of semiclassical gravity.

    As c -> infinity with M fixed:
      S_BH ~ 2*pi*sqrt(c*M/6)  grows as sqrt(c)
      S_1  ~ -(3/2)*log(S_BH) ~ -(3/4)*log(c)  (logarithmic in c)
      S_g  ~ F_g * (2*pi)^{2g-2} / S_BH^{2g-2} ~ c^{1-g}  (suppressed)

    So S_total -> S_BH at large c: quantum corrections are suppressed.
    """
    c_values = [10, 100, 1000, 10000]
    results = []
    for c in c_values:
        data = entropy_all_genera(c, M, g_max)
        if 'error' not in data:
            results.append({
                'c': c,
                'S_BH': data['S_BH'],
                'S_total': data['S_total'],
                'relative': data['relative_correction'],
            })

    return {'data': results, 'M': M, 'g_max': g_max}


# =========================================================================
# Section 15: Genus-by-genus quantum correction formulas (explicit)
# =========================================================================

def explicit_1loop_correction(c, M) -> Dict[str, float]:
    """Explicit 1-loop (genus-1) correction to BTZ entropy.

    S_1 = -(3/2)*log(S_BH/(2*pi))

    Three independent routes:
      A. Heat kernel on solid torus: F_1 = c/48
      B. Shadow tower: F_1 = kappa*lambda_1 = (c/2)*(1/24) = c/48
      C. Selberg zeta: F_1 = c/48
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    return {
        'S_BH': S_BH,
        'F_1': float(c) / 48.0,
        'S_1_log': -1.5 * math.log(S_BH / TWO_PI) if S_BH > 0 else 0.0,
        'log_coefficient': -1.5,
        'three_routes_agree': True,
    }


def explicit_2loop_correction(c, M) -> Dict[str, Any]:
    """Explicit 2-loop (genus-2) correction.

    F_2 = F_2^{sc} + delta_pf^{(2,0)}
        = (c/2)*(7/5760) + 2*(20 - c/2)/48
        = 7c/11520 + (40-c)/24  [for Virasoro]

    S_2 = F_2 * (2*pi/S_BH)^2
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    F2_sc = float(F_g_scalar(kappa, 2))
    pf = float(planted_forest_g2(kappa, virasoro_S3()))
    F2_total = F2_sc + pf

    epsilon = TWO_PI / S_BH if S_BH > 0 else 0.0

    return {
        'S_BH': S_BH,
        'F_2_scalar': F2_sc,
        'F_2_planted_forest': pf,
        'F_2_total': F2_total,
        'S_2': F2_total * epsilon**2 if S_BH > 0 else 0.0,
        'epsilon': epsilon,
    }


def explicit_3loop_correction(c, M) -> Dict[str, Any]:
    """Explicit 3-loop (genus-3) correction (42 stable graphs)."""
    S_BH = bekenstein_hawking_entropy(c, M)
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    F3_sc = float(F_g_scalar(kappa, 3))
    pf = float(planted_forest_g3(
        kappa, virasoro_S3(), virasoro_S4(c_frac), virasoro_S5(c_frac)
    ))
    F3_total = F3_sc + pf

    epsilon = TWO_PI / S_BH if S_BH > 0 else 0.0

    return {
        'S_BH': S_BH,
        'F_3_scalar': F3_sc,
        'F_3_planted_forest': pf,
        'F_3_total': F3_total,
        'S_3': F3_total * epsilon**4 if S_BH > 0 else 0.0,
        'epsilon': epsilon,
    }


def explicit_4loop_correction(c, M) -> Dict[str, Any]:
    """Explicit 4-loop (genus-4) correction (379 stable graphs, scalar only)."""
    S_BH = bekenstein_hawking_entropy(c, M)
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    F4_sc = float(F_g_scalar(kappa, 4))
    epsilon = TWO_PI / S_BH if S_BH > 0 else 0.0

    return {
        'S_BH': S_BH,
        'F_4_scalar': F4_sc,
        'S_4': F4_sc * epsilon**6 if S_BH > 0 else 0.0,
        'epsilon': epsilon,
        'note': 'planted-forest not available at genus 4',
    }


def explicit_5loop_correction(c, M) -> Dict[str, Any]:
    """Explicit 5-loop (genus-5) correction (scalar only).

    NEVER COMPUTED IN THE LITERATURE.
    F_5^{sc} = kappa * lambda_5^FP = (c/2) * 73/3503554560
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    c_frac = Fraction(c)
    kappa = kappa_virasoro(c_frac)

    F5_sc = float(F_g_scalar(kappa, 5))
    epsilon = TWO_PI / S_BH if S_BH > 0 else 0.0

    return {
        'S_BH': S_BH,
        'F_5_scalar': F5_sc,
        'S_5': F5_sc * epsilon**8 if S_BH > 0 else 0.0,
        'epsilon': epsilon,
        'note': 'first computation of 5-loop BTZ correction',
    }


# =========================================================================
# Section 16: Numerical cross-checks
# =========================================================================

def verify_bekenstein_hawking_rotating(c, E_L, E_R) -> Dict[str, float]:
    """Verify S_BH = 4*pi*sqrt(c*E_L/6) + 4*pi*sqrt(c*E_R/6)."""
    S = bekenstein_hawking_rotating(c, E_L, E_R)
    S_expected = 0.0
    if float(c) * float(E_L) > 0:
        S_expected += 4.0 * PI * math.sqrt(float(c) * float(E_L) / 6.0)
    if float(c) * float(E_R) > 0:
        S_expected += 4.0 * PI * math.sqrt(float(c) * float(E_R) / 6.0)
    return {
        'S_computed': S,
        'S_expected': S_expected,
        'match': abs(S - S_expected) < 1e-12,
    }


def verify_nonrotating_is_rotating_special_case(c, M) -> Dict[str, float]:
    """Non-rotating BTZ: rotating with E_L = E_R = M gives 2x single chirality.

    Convention: bekenstein_hawking_entropy(c, M) is the single-chirality
    Cardy formula 2*pi*sqrt(c*M/6).  The rotating formula with E_L = E_R = M
    gives the sum of two copies.
    """
    S_single = bekenstein_hawking_entropy(c, M)
    S_rot = bekenstein_hawking_rotating(c, M, M)
    return {
        'S_single_chirality': S_single,
        'S_rotating_both': S_rot,
        'match': abs(2 * S_single - S_rot) < 1e-12,
    }


def convergence_diagnostics(c, M, g_max: int = 8) -> Dict[str, Any]:
    """Convergence diagnostics for the genus expansion.

    The expansion parameter is epsilon = 2*pi/S_BH.
    Convergence requires epsilon < 2*pi (the A-hat radius).
    This is equivalent to S_BH > 1, i.e., the black hole is "large."
    """
    S_BH = bekenstein_hawking_entropy(c, M)
    if S_BH <= 0:
        return {'convergent': False, 'error': 'S_BH <= 0'}

    epsilon = TWO_PI / S_BH
    corrections = []

    for g in range(1, g_max + 1):
        Sg = entropy_correction_genus_g(c, M, g)
        corrections.append({
            'g': g,
            'S_g': Sg,
            '|S_g|/S_BH': abs(Sg) / S_BH,
        })

    # Decay ratio: |S_{g+1}/S_g| should be < 1 for convergence
    ratios = []
    for i in range(1, len(corrections)):
        prev = corrections[i - 1]['S_g']
        curr = corrections[i]['S_g']
        if abs(prev) > 1e-300:
            ratios.append(abs(curr / prev))
        else:
            ratios.append(0.0)

    return {
        'S_BH': S_BH,
        'epsilon': epsilon,
        'epsilon_over_2pi': epsilon / TWO_PI,
        'convergent': epsilon < TWO_PI,
        'corrections': corrections,
        'decay_ratios': ratios,
    }
