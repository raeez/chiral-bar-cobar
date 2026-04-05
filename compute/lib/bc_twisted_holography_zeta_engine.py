r"""Twisted holographic partition functions at Riemann zeta zero parameters.

MATHEMATICAL FRAMEWORK
======================

This module computes standard holographic quantities — boundary partition
functions, bulk shadows, BTZ thermodynamics, Chern-Simons partition functions,
anomaly polynomials, and open/closed annulus amplitudes — evaluated at spectral
parameters determined by the nontrivial zeros rho_n of the Riemann zeta function.

EPISTEMIC STATUS (AP42)
=======================

The evaluation of holographic quantities at zeta-zero parameters is EXPLORATORY
NUMEROLOGY, not established mathematics or physics.  There is no published theorem
or physical principle that relates the nontrivial zeros of zeta(s) to holographic
modular parameters.  The mapping tau_n = i*(1 + rho_n)/(4*pi) is an ANSATZ with
no derivation.  The Selberg zeta for the BTZ quotient Gamma\H^3 is DISTINCT from
the Riemann zeta (see bc_btz_spectral_zeta_engine.py for the precise relation).

What IS mathematically rigorous in this module:
  - Boundary partition functions Z_partial(tau) = Tr(q^{L_0 - c/24})
  - Bulk shadow free energies F_g from the proved shadow CohFT (thm:shadow-cohft)
  - BTZ thermodynamics and Cardy formula (AP20: kappa(A), not kappa_eff)
  - Chern-Simons partition function on the solid torus at integer/rational level
  - Anomaly polynomials I_8 as topological invariants
  - Annulus trace = kappa * lambda_1 at genus 1 (proved, thm:annulus-trace)
  - Open/closed duality: derived center Z^der_ch(A) (thm:thqg-swiss-cheese)

What is NUMEROLOGICAL / CONJECTURAL:
  - The mapping from zeta zeros to modular parameters
  - Any claimed "coincidence" between zeta-zero evaluations and physical quantities
  - The term "Benjamin-Chang programme" does not correspond to a published programme

CONVENTIONS
===========

  - kappa(Vir_c) = c/2 (AP1, AP9, AP20)
  - kappa_eff = kappa(matter) + kappa(ghost), vanishes at c=26 (AP29)
  - delta_kappa = kappa - kappa' (complementarity asymmetry), vanishes at c=13 (AP29)
  - The bar propagator is d log E(z,w), weight 1 in both variables (AP27)
  - r-matrix pole order = OPE pole order - 1 (AP19)
  - Dedekind eta: eta(q) = q^{1/24} * prod(1-q^n) (AP46)
  - COHOMOLOGICAL grading, bar uses DESUSPENSION (AP45)
  - Z_partial(tau) = Tr(q^{L_0-c/24}) with q = e^{2*pi*i*tau}

FAMILIES
========

  Heisenberg H_k:  kappa = k,  c = 1 (at level k=1, convention-dependent)
  Affine KM V_k(g): kappa = dim(g)*(k+h^v)/(2*h^v), c = k*dim(g)/(k+h^v)
  Virasoro Vir_c:  kappa = c/2
  W_N at level k:  kappa = c*(H_N - 1)

References:
    BTZ 1992: hep-th/9204099
    Cardy 1986: the Cardy formula for asymptotic density of states
    Witten 1989: CS and the Jones polynomial
    Dijkgraaf-Maldacena-Moore-Verlinde 2000: hep-th/0005003 (Farey tail)
    Costello-Paquette 2022: celestial holography from twisted holography
    Strominger 2014: BMS supertranslations and celestial holography
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
    thm:annulus-trace (thqg_open_closed_realization.tex)
    thm:thqg-swiss-cheese (thqg_open_closed_realization.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple


# ===========================================================================
# Constants
# ===========================================================================

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2
EULER_GAMMA = 0.5772156649015329  # Euler-Mascheroni constant

# First 30 nontrivial zeros of the Riemann zeta function (imaginary parts).
# These are the positive imaginary parts rho_n such that zeta(1/2 + i*rho_n) = 0.
# Source: LMFDB / Odlyzko tables, verified to 10+ digits.
RIEMANN_ZETA_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081607,
    67.079810529494174,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492980517050,
    87.425274613125196,
    88.809111207634465,
    92.491899270558484,
    94.651344040519838,
    95.870634228245309,
    98.831194218193692,
    101.31785100573139,
]


# ===========================================================================
# Section 1: Modular characteristics (exact arithmetic)
# ===========================================================================

def kappa_virasoro(c) -> Fraction:
    """kappa(Vir_c) = c/2.

    AP1/AP9: authoritative formula.
    AP20: this is kappa(A) for A = Vir_c, NOT kappa_eff.
    """
    return Fraction(c) / Fraction(2)


def kappa_heisenberg(k) -> Fraction:
    """kappa(H_k) = k.

    Single generator of weight 1 at level k.
    """
    return Fraction(k)


def kappa_kac_moody(dim_g: int, k, h_dual) -> Fraction:
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2*h^v).

    AP1: recomputed from first principles for each family.
    """
    return Fraction(dim_g) * (Fraction(k) + Fraction(h_dual)) / (2 * Fraction(h_dual))


def kappa_wn(c, N: int) -> Fraction:
    """kappa(W_N) = c * (H_N - 1) where H_N = sum_{j=1}^N 1/j.

    AP1/AP9: distinct from c/2 for N >= 3.
    """
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    return Fraction(c) * (H_N - 1)


def central_charge_km(dim_g: int, k, h_dual) -> Fraction:
    """Central charge c(V_k(g)) = k * dim(g) / (k + h^v)."""
    return Fraction(k) * Fraction(dim_g) / (Fraction(k) + Fraction(h_dual))


def kappa_ghost() -> Fraction:
    """kappa(bc ghosts) = -13.

    The bc ghost system for the bosonic string has c_ghost = -26,
    so kappa(ghost) = c_ghost/2 = -13.  (Treated as Virasoro at c=-26.)
    """
    return Fraction(-13)


def kappa_eff(kappa_matter: Fraction) -> Fraction:
    """Effective curvature kappa_eff = kappa(matter) + kappa(ghost).

    AP29: this is DISTINCT from delta_kappa = kappa - kappa'.
    Vanishes at c_matter = 26 (bosonic string critical dimension).
    """
    return kappa_matter + kappa_ghost()


def delta_kappa(kappa_A: Fraction, kappa_A_dual: Fraction) -> Fraction:
    """Complementarity asymmetry delta_kappa = kappa(A) - kappa(A!).

    AP29: DISTINCT from kappa_eff.
    For KM/free fields: delta_kappa = 2*kappa(A) (since kappa+kappa'=0).
    For Virasoro: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, so
      delta_kappa = c/2 - (26-c)/2 = c - 13.
    """
    return kappa_A - kappa_A_dual


# ===========================================================================
# Section 2: Faber-Pandharipande intersection numbers
# ===========================================================================

@lru_cache(maxsize=64)
def _bernoulli_2g(g: int) -> Fraction:
    """Exact Bernoulli number B_{2g}."""
    _TABLE = {
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
    if g in _TABLE:
        return _TABLE[g]
    try:
        from sympy import bernoulli as sympy_bernoulli, Rational
        return Fraction(Rational(sympy_bernoulli(2 * g)))
    except ImportError:
        raise ValueError(f"B_{{{2*g}}} not hardcoded and sympy unavailable")


def _factorial_fraction(n: int) -> Fraction:
    """n! as exact Fraction."""
    result = Fraction(1)
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    These are POSITIVE for all g >= 1 (AP22: Bernoulli signs).

    Verified values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B_2g = _bernoulli_2g(g)
    power = 2 ** (2 * g - 1)
    num = (power - 1) * abs(B_2g)
    den = power * _factorial_fraction(2 * g)
    return num / den


# ===========================================================================
# Section 3: Zeta-zero to modular parameter mapping (NUMEROLOGICAL)
# ===========================================================================

def zeta_zero(n: int) -> float:
    """Return the n-th nontrivial zero imaginary part rho_n (1-indexed).

    These are the positive imaginary parts of the nontrivial zeros of
    the Riemann zeta function: zeta(1/2 + i*rho_n) = 0.
    """
    if n < 1 or n > len(RIEMANN_ZETA_ZEROS):
        raise ValueError(
            f"Zeta zero index must be in [1, {len(RIEMANN_ZETA_ZEROS)}], got {n}"
        )
    return RIEMANN_ZETA_ZEROS[n - 1]


def modular_parameter_from_zeta_zero(n: int) -> complex:
    r"""Map zeta zero rho_n to modular parameter tau_n.

    NUMEROLOGICAL ANSATZ (no physical derivation):
        tau_n = i * (1 + rho_n) / (4*pi)

    This places tau in the upper half-plane (Im(tau) > 0) for rho_n > 0.
    The nome is q_n = e^{2*pi*i*tau_n} = e^{-(1+rho_n)/2}.

    NOTE: This mapping is ARBITRARY.  It is chosen so that |q_n| < 1
    (ensuring convergence of q-series) and so that larger rho_n gives
    smaller |q_n| (stronger convergence).
    """
    rho_n = zeta_zero(n)
    return 1j * (1.0 + rho_n) / (4.0 * PI)


def nome_from_zeta_zero(n: int) -> complex:
    r"""Nome q_n = e^{2*pi*i*tau_n} at the n-th zeta zero parameter.

    q_n = e^{-(1 + rho_n)/2}.

    Since rho_1 ~ 14.13, we have |q_1| ~ e^{-7.57} ~ 5.2e-4.
    The q-series converges extremely rapidly at all zeta zero parameters.
    """
    rho_n = zeta_zero(n)
    return cmath.exp(-(1.0 + rho_n) / 2.0)


def spectral_parameter_from_zeta_zero(n: int) -> complex:
    r"""Spectral parameter s_n = (1 + i*rho_n)/2 on the critical line.

    This is the standard parameterization of the critical strip:
    the n-th zero is at s = 1/2 + i*rho_n, so s_n = (1 + i*rho_n)/2
    is the ACTUAL location of the zero.
    """
    rho_n = zeta_zero(n)
    return complex(0.5, rho_n)


def mellin_parameter_from_zeta_zero(n: int) -> complex:
    r"""Mellin/conformal dimension Delta_n = (1 + i*rho_n)/2.

    In celestial holography, the Mellin transform of a bulk scattering
    amplitude has conformal dimension Delta.  Setting Delta to the spectral
    parameter s_n gives the celestial OPE coefficient at the zeta zero.

    NOTE: This identification is FORMAL.  Celestial conformal dimensions are
    real for physical operators; complex Delta corresponds to principal-series
    representations (which DO appear in the celestial basis, cf. Pasterski-
    Shao-Strominger).  But the claim that zeta zeros have special significance
    for celestial amplitudes is UNPROVED.
    """
    return spectral_parameter_from_zeta_zero(n)


# ===========================================================================
# Section 4: Boundary partition functions
# ===========================================================================

def dedekind_eta(tau: complex, n_max: int = 200) -> complex:
    r"""Dedekind eta function: eta(tau) = q^{1/24} * prod_{n>=1} (1 - q^n).

    AP46: the q^{1/24} prefactor is NOT optional.

    Parameters
    ----------
    tau : complex
        Modular parameter with Im(tau) > 0.
    n_max : int
        Product truncation (200 terms gives machine precision for |q| < 0.9).
    """
    if tau.imag <= 0:
        raise ValueError(f"Need Im(tau) > 0, got Im(tau) = {tau.imag}")
    q = cmath.exp(2.0 * PI * 1j * tau)
    # q^{1/24}
    prefactor = cmath.exp(2.0 * PI * 1j * tau / 24.0)
    product = complex(1.0, 0.0)
    q_power = q
    for _ in range(1, n_max + 1):
        product *= (1.0 - q_power)
        q_power *= q
    return prefactor * product


def boundary_partition_virasoro(tau: complex, c: float = 26.0,
                                 n_max: int = 200) -> complex:
    r"""Boundary partition function Z_partial(tau) for the Virasoro algebra.

    Z(tau) = Tr(q^{L_0 - c/24}) = q^{-c/24} / prod_{n>=1}(1 - q^n)
           = q^{-c/24} / (eta(tau) * q^{-1/24})
           = q^{(-c+1)/24} / eta(tau)     ... NO:

    Careful (AP46): eta(tau) = q^{1/24} prod(1-q^n).
    So prod(1-q^n) = eta(tau) / q^{1/24} = eta(tau) * q^{-1/24}.

    For pure Virasoro (single copy, no fermions):
        Z(tau) = q^{-c/24} * prod_{n>=2} (1-q^n)^{-1}
               = q^{-c/24} * (1-q)^{-1} ... NO.

    Standard: Z(tau) = q^{(1-c)/24} / eta(tau) for the Virasoro module
    generated by L_{-n} for n >= 2 on the vacuum.  But the FULL partition
    function of the Verma module at generic c is:

        Z(tau) = q^{-c/24} / prod_{n>=1}(1-q^n) = q^{-c/24} / (eta/q^{1/24})
               = q^{(-c+1)/24} / eta(tau)

    We compute directly for numerical stability.
    """
    if tau.imag <= 0:
        raise ValueError(f"Need Im(tau) > 0, got Im(tau) = {tau.imag}")
    q = cmath.exp(2.0 * PI * 1j * tau)
    # q^{-c/24}
    vacuum_factor = cmath.exp(-2.0 * PI * 1j * tau * c / 24.0)
    # 1 / prod_{n>=1}(1-q^n)
    product = complex(1.0, 0.0)
    q_power = q
    for n in range(1, n_max + 1):
        product *= (1.0 - q_power)
        q_power *= q
    return vacuum_factor / product


def boundary_partition_heisenberg(tau: complex, k: float = 1.0,
                                   n_max: int = 200) -> complex:
    r"""Boundary partition function for the Heisenberg algebra at level k.

    Single free boson: Z(tau) = q^{-1/24} / prod_{n>=1}(1-q^n) = 1/eta(tau).

    For the rank-r Heisenberg (r free bosons):
        Z(tau) = 1 / eta(tau)^r

    Here we compute for a single boson (rank 1).  The central charge is 1.
    """
    eta_val = dedekind_eta(tau, n_max)
    if abs(eta_val) < 1e-300:
        return complex(float('inf'), 0)
    return 1.0 / eta_val


def boundary_partition_km(tau: complex, dim_g: int, k: int, h_dual: int,
                           n_max: int = 200) -> complex:
    r"""Boundary partition function for affine KM at level k.

    For V_k(g), the vacuum character is:
        chi_0(tau) = q^{-c/24} * prod_{n>=1} (1-q^n)^{-dim(g)}
                   = q^{-c/24} / eta(tau)^{dim(g)} * q^{dim(g)/24}
                   = q^{(-c+dim(g))/24} / eta(tau)^{dim(g)}

    where c = k*dim(g)/(k+h^v).

    This is the CHARACTER of the vacuum module, not the full partition
    function (which would sum over all integrable modules).
    """
    c = float(k) * dim_g / (float(k) + float(h_dual))
    q = cmath.exp(2.0 * PI * 1j * tau)
    vacuum_factor = cmath.exp(-2.0 * PI * 1j * tau * c / 24.0)
    product = complex(1.0, 0.0)
    q_power = q
    for n in range(1, n_max + 1):
        product *= (1.0 - q_power) ** dim_g
        q_power *= q
    return vacuum_factor / product


# ===========================================================================
# Section 5: Boundary partition at zeta-zero parameters
# ===========================================================================

def boundary_Z_at_zeta_zero(n: int, c: float = 26.0,
                             algebra: str = 'virasoro',
                             **kwargs) -> complex:
    r"""Evaluate the boundary partition function at the n-th zeta zero parameter.

    tau_n = i*(1+rho_n)/(4*pi)  [NUMEROLOGICAL ANSATZ]

    Returns Z_partial(tau_n) for the specified algebra.
    """
    tau = modular_parameter_from_zeta_zero(n)
    if algebra == 'virasoro':
        return boundary_partition_virasoro(tau, c=c)
    elif algebra == 'heisenberg':
        return boundary_partition_heisenberg(tau)
    elif algebra == 'kac_moody':
        dim_g = kwargs.get('dim_g', 3)
        k = kwargs.get('k', 1)
        h_dual = kwargs.get('h_dual', 2)
        return boundary_partition_km(tau, dim_g, k, h_dual)
    else:
        raise ValueError(f"Unknown algebra: {algebra}")


def boundary_Z_table(c: float = 26.0, n_max: int = 10,
                      algebra: str = 'virasoro',
                      **kwargs) -> Dict[int, complex]:
    """Table of Z_partial(tau_n) for n = 1..n_max."""
    return {
        n: boundary_Z_at_zeta_zero(n, c=c, algebra=algebra, **kwargs)
        for n in range(1, n_max + 1)
    }


# ===========================================================================
# Section 6: Bulk shadow at zeta-zero parameters
# ===========================================================================

def bulk_shadow_Fg(kappa_val: Fraction, g: int) -> Fraction:
    r"""Scalar free energy F_g = kappa * lambda_g^FP.

    This is the SCALAR LANE contribution (proved for uniform-weight
    algebras at all genera; genus 1 unconditional for all families).

    AP31: F_g depends on kappa, not the full Theta_A.  Higher-arity
    corrections exist for class M algebras at g >= 2.
    """
    return Fraction(kappa_val) * lambda_fp(g)


def bulk_shadow_effective(c_matter: float, g: int) -> float:
    r"""Effective bulk shadow: F_g^{eff} = kappa_eff * lambda_g^FP.

    AP29: kappa_eff = kappa(matter) + kappa(ghost) = c/2 - 13.
    At c=26: kappa_eff = 0, so ALL scalar free energies vanish.
    This is the anomaly cancellation condition for the bosonic string.
    """
    kappa_m = kappa_virasoro(Fraction(c_matter))
    kappa_e = kappa_eff(kappa_m)
    return float(kappa_e * lambda_fp(g))


def bulk_shadow_table(c_matter: float, g_max: int = 5) -> Dict[str, Any]:
    r"""Table of bulk shadow data.

    Returns both the matter and effective (matter+ghost) free energies.
    """
    kappa_m = kappa_virasoro(Fraction(c_matter))
    kappa_e = kappa_eff(kappa_m)

    matter = {g: float(bulk_shadow_Fg(kappa_m, g)) for g in range(1, g_max + 1)}
    effective = {g: float(bulk_shadow_Fg(kappa_e, g)) for g in range(1, g_max + 1)}

    return {
        'c_matter': c_matter,
        'kappa_matter': float(kappa_m),
        'kappa_ghost': float(kappa_ghost()),
        'kappa_eff': float(kappa_e),
        'F_g_matter': matter,
        'F_g_effective': effective,
        'anomaly_cancelled': (kappa_e == 0),
    }


# ===========================================================================
# Section 7: Twisted partition function (refined index)
# ===========================================================================

def twisted_partition_virasoro(tau: complex, z: complex, c: float = 26.0,
                                J_max: int = 50, n_max: int = 200) -> complex:
    r"""Twisted partition function Z(tau, z) = Tr(q^{L_0-c/24} y^{J_0}).

    For a Virasoro algebra, there is no conserved U(1) current J_0 unless
    we add one (e.g., spectral flow or a free boson).  For the Heisenberg
    extension of Virasoro (free boson + Virasoro), we have J_0 = a_0
    (zero mode of the free boson).  The twisted partition function is:

        Z(tau, z) = q^{-c/24} * y^0 * prod_{n>=1} (1-q^n)^{-1}
                  * sum_m y^m q^{m^2/(2k)}    [Heisenberg zero-mode sum]

    For the pure Virasoro without a conserved current, Z(tau, z) degenerates
    to Z(tau, 0) = Z(tau).  We compute the HEISENBERG-EXTENDED version.

    Parameters
    ----------
    tau : complex with Im(tau) > 0
    z : complex (the twist parameter; y = e^{2*pi*i*z})
    c : central charge
    J_max : truncation for zero-mode sum
    n_max : product truncation
    """
    if tau.imag <= 0:
        raise ValueError(f"Need Im(tau) > 0, got {tau.imag}")

    q = cmath.exp(2.0 * PI * 1j * tau)
    y = cmath.exp(2.0 * PI * 1j * z)

    # Vacuum factor
    vacuum = cmath.exp(-2.0 * PI * 1j * tau * c / 24.0)

    # Oscillator product: prod_{n>=1} (1-q^n)^{-1}
    product = complex(1.0, 0.0)
    q_power = q
    for _ in range(1, n_max + 1):
        product *= (1.0 - q_power)
        q_power *= q
    oscillator = 1.0 / product

    # Zero-mode sum: sum_{m=-J_max}^{J_max} y^m q^{m^2/2}
    # (k=1 Heisenberg; for general k, replace m^2/2 -> m^2/(2k))
    # Compute via log to avoid overflow: y^m * q^{m^2/2} = exp(m*log(y) + m^2*pi*i*tau)
    log_y = cmath.log(y) if abs(y) > 1e-300 else complex(-1e300, 0)
    zero_mode_sum = complex(0.0, 0.0)
    for m in range(-J_max, J_max + 1):
        log_term = m * log_y + PI * 1j * tau * m * m
        # Skip terms with extremely large negative real part (underflow)
        if log_term.real > -500:
            zero_mode_sum += cmath.exp(log_term)

    return vacuum * oscillator * zero_mode_sum


def twisted_Z_at_zeta_zero(n: int, c: float = 26.0,
                             z_mode: str = 'half_rho') -> complex:
    r"""Twisted partition function at zeta-zero parameters.

    Parameters
    ----------
    n : zeta zero index (1-indexed)
    c : central charge
    z_mode : how to set the twist parameter z
        'half_rho': z = rho_n / 2  (NUMEROLOGICAL)
        'spectral': z = s_n / 2 = (1 + i*rho_n) / 4  (NUMEROLOGICAL)
        'zero': z = 0 (reduces to untwisted partition function)
    """
    tau = modular_parameter_from_zeta_zero(n)
    rho_n = zeta_zero(n)

    if z_mode == 'half_rho':
        z = complex(0, rho_n / 2.0)
    elif z_mode == 'spectral':
        z = complex(0.25, rho_n / 4.0)
    elif z_mode == 'zero':
        z = complex(0, 0)
    else:
        raise ValueError(f"Unknown z_mode: {z_mode}")

    return twisted_partition_virasoro(tau, z, c=c)


# ===========================================================================
# Section 8: Celestial OPE at zeta-zero Mellin parameters
# ===========================================================================

def celestial_soft_factor(Delta: complex, spin: int = 2) -> complex:
    r"""Leading celestial soft factor S^{(0)} at conformal dimension Delta.

    For spin-s conformal primary operators on the celestial sphere,
    the leading soft theorem (Strominger 2014) gives:

        S^{(0)}_{s}(Delta) = 1 / (Delta - 1)     [supertranslation, s=0]
        S^{(1)}_{s}(Delta) = 1 / (Delta - 1)^2   [superrotation, s=1]

    For graviton scattering (s=2), the Weinberg soft factor is:
        S_0^grav(Delta) = kappa / (Delta - 1)

    where kappa here is the gravitational coupling (NOT the modular
    characteristic of the manuscript; regrettable notational collision).

    We compute with the coupling set to 1 (normalized soft factor).

    Parameters
    ----------
    Delta : complex conformal dimension (Mellin parameter)
    spin : spin of the soft particle (0, 1, or 2)
    """
    if abs(Delta - 1.0) < 1e-15:
        return complex(float('inf'), 0)
    if spin == 0:
        return 1.0 / (Delta - 1.0)
    elif spin == 1:
        return 1.0 / (Delta - 1.0) ** 2
    elif spin == 2:
        return 1.0 / (Delta - 1.0)
    else:
        # General spin: S^{(0)} ~ 1/(Delta - 1 + s - 2)
        return 1.0 / (Delta - 1.0 + spin - 2.0)


def celestial_collinear_kernel(Delta_1: complex, Delta_2: complex,
                                spin_1: int = 2, spin_2: int = 2) -> complex:
    r"""Celestial collinear splitting kernel B(Delta_1, Delta_2).

    For two gravitons with celestial dimensions Delta_1, Delta_2, the
    collinear limit gives a kernel proportional to the Beta function:

        B(Delta_1, Delta_2) = Gamma(Delta_1) * Gamma(Delta_2) / Gamma(Delta_1 + Delta_2)

    This is the celestial OPE coefficient in the collinear limit.

    We use the Gamma function from cmath (via the reflection formula for
    complex arguments).
    """
    try:
        import scipy.special as sp
        g1 = sp.gamma(complex(Delta_1))
        g2 = sp.gamma(complex(Delta_2))
        g12 = sp.gamma(complex(Delta_1 + Delta_2))
        if abs(g12) < 1e-300:
            return complex(float('inf'), 0)
        return g1 * g2 / g12
    except ImportError:
        # Fallback: use Stirling for large |Delta|
        # For small Delta, use the recurrence Gamma(z+1) = z*Gamma(z)
        return _gamma_ratio_fallback(Delta_1, Delta_2)


def _gamma_ratio_fallback(a: complex, b: complex) -> complex:
    """Fallback Beta(a,b) = Gamma(a)*Gamma(b)/Gamma(a+b) via Stirling."""
    # Stirling: log Gamma(z) ~ z*log(z) - z - 0.5*log(z) + 0.5*log(2*pi)
    def log_stirling(z):
        z = complex(z)
        return z * cmath.log(z) - z - 0.5 * cmath.log(z) + 0.5 * math.log(TWO_PI)

    log_beta = log_stirling(a) + log_stirling(b) - log_stirling(a + b)
    return cmath.exp(log_beta)


def celestial_at_zeta_zero(n: int, spin: int = 2) -> Dict[str, complex]:
    r"""Celestial soft factor and collinear kernel at zeta-zero parameter.

    Delta_n = (1 + i*rho_n)/2  (the spectral parameter on the critical line).

    NOTE (AP42): this evaluation has no established physical meaning.
    The celestial conformal dimension for physical gravitons is REAL.
    Complex Delta corresponds to principal-series representations.
    """
    Delta = mellin_parameter_from_zeta_zero(n)
    rho_n = zeta_zero(n)

    soft = celestial_soft_factor(Delta, spin)
    collinear = celestial_collinear_kernel(Delta, Delta, spin, spin)

    return {
        'n': n,
        'rho_n': rho_n,
        'Delta': Delta,
        'soft_factor': soft,
        'collinear_kernel': collinear,
        'abs_soft': abs(soft),
        'abs_collinear': abs(collinear),
    }


# ===========================================================================
# Section 9: BTZ black hole at zeta-zero parameters
# ===========================================================================

def btz_at_zeta_zero(n: int, c: float = 26.0) -> Dict[str, Any]:
    r"""BTZ black hole thermodynamics at zeta-zero modular parameter.

    The BTZ modular parameter tau = i*beta/(2*pi) where beta = 1/T_H.
    From tau_n = i*(1+rho_n)/(4*pi), we read off:
        beta_n = (1+rho_n)/2
        T_H_n = 2/(1+rho_n)

    The Bekenstein-Hawking entropy at this temperature:
        S_BH = pi^2 * c * T_H / 3 = 2*pi^2*c / (3*(1+rho_n))

    The Cardy formula (matching CFT counting):
        S_Cardy = (pi^2/3) * c * T   (high-T)
    """
    rho_n = zeta_zero(n)
    tau_n = modular_parameter_from_zeta_zero(n)

    beta_n = (1.0 + rho_n) / 2.0
    T_H_n = 1.0 / beta_n

    # Bekenstein-Hawking / Cardy entropy
    # S = pi^2 * c * T / 3 = pi^2 * c / (3 * beta)
    S_BH = PI ** 2 * c / (3.0 * beta_n)

    # Nome
    q_n = nome_from_zeta_zero(n)

    # Tachyon mass at c=26: m^2 = -1/alpha' = -4 in conventions where alpha'=1/2
    # The tachyon vertex operator has dimension h = alpha' m^2 / 4 + 1 = 0
    # at the mass shell.  At the BTZ temperature T_H:
    # The thermal mass correction: m_eff^2 = m^2 + pi^2 * T_H^2 * (c-2)/6
    # For c=26: m_eff^2 = -4 + pi^2 * T_H^2 * 4 = -4 + 4*pi^2/(beta^2)
    alpha_prime = 0.5  # alpha' = 1/2 convention
    m_sq_tachyon = -4.0  # in alpha' = 1/2 units
    if c == 26.0:
        thermal_mass_sq = m_sq_tachyon + 4.0 * PI ** 2 / (beta_n ** 2)
        hagedorn_beta = PI * math.sqrt(2.0 * alpha_prime * (c - 2.0))
        tachyon_condensed = (beta_n < hagedorn_beta)
    else:
        thermal_mass_sq = None
        hagedorn_beta = None
        tachyon_condensed = None

    # One-loop correction: S_1 = -(3/2) * log(S_BH/(2*pi))
    if S_BH > 0:
        S_1_loop = -1.5 * math.log(S_BH / TWO_PI)
    else:
        S_1_loop = 0.0

    return {
        'n': n,
        'rho_n': rho_n,
        'tau_n': tau_n,
        'beta_n': beta_n,
        'T_H': T_H_n,
        'S_BH': S_BH,
        'S_1_loop': S_1_loop,
        'q_n': q_n,
        'abs_q': abs(q_n),
        'c': c,
        'thermal_mass_sq': thermal_mass_sq,
        'hagedorn_beta': hagedorn_beta,
        'tachyon_condensed': tachyon_condensed,
    }


def cardy_entropy(c: float, Delta: float) -> float:
    r"""Cardy formula: S = 2*pi*sqrt(c*Delta/6).

    This is the asymptotic (high-energy) entropy for a 2d CFT of central
    charge c at conformal dimension Delta >> c/24.
    """
    if c * Delta <= 0:
        return 0.0
    return 2.0 * PI * math.sqrt(c * Delta / 6.0)


def cardy_matches_btz(c: float, beta: float, tol: float = 1e-10) -> bool:
    r"""Verify that Cardy entropy matches BTZ entropy at inverse temperature beta.

    The BTZ entropy S_BH = pi^2*c/(3*beta).
    The Cardy entropy at energy E = pi^2*c/(6*beta^2) is
        S_Cardy = 2*pi*sqrt(c*E/6) = 2*pi*sqrt(c * pi^2*c/(36*beta^2))
                = 2*pi^2*c / (6*beta) ... NO.

    Let me be careful.  In the canonical ensemble at temperature T = 1/beta:
        E = (pi^2 / 6) * c * T^2 = (pi^2 * c) / (6 * beta^2)
        S = beta * E + log Z ~ (pi^2 / 3) * c * T = (pi^2 * c) / (3 * beta)

    The Cardy formula in the microcanonical ensemble:
        S(E) = 2*pi*sqrt(c*E/6) = 2*pi*sqrt(c * (pi^2*c)/(36*beta^2))
             = 2*pi * pi*sqrt(c^2/(36)) / beta
             = 2*pi^2*c / (6*beta)
             = pi^2*c / (3*beta)

    Yes, they match: S_BH = S_Cardy = pi^2*c/(3*beta).
    """
    S_btz = PI ** 2 * c / (3.0 * beta)
    E = PI ** 2 * c / (6.0 * beta ** 2)
    S_cardy = cardy_entropy(c, E)
    return abs(S_btz - S_cardy) < tol * max(abs(S_btz), 1.0)


# ===========================================================================
# Section 10: Anomaly polynomial
# ===========================================================================

def anomaly_polynomial_I4(c: float, p1: float = 1.0) -> float:
    r"""Gravitational anomaly 4-form I_4 for a 2d CFT.

    I_4 = (c/24) * p_1(R)

    where p_1(R) = -(1/(8*pi^2)) * Tr(R^2) is the first Pontryagin class.
    This is the gravitational anomaly that obstructs coupling to curved
    backgrounds.

    At c=26: I_4 = 26/24 * p_1 = 13/12 * p_1.
    At c=0: I_4 = 0 (no gravitational anomaly for topological theory).

    Parameters
    ----------
    c : central charge
    p1 : value of p_1(R) (set to 1 for the coefficient)
    """
    return c * p1 / 24.0


def anomaly_polynomial_I8(c: float, p1: float = 1.0,
                           p2: float = 0.0) -> float:
    r"""Anomaly 8-form I_8 for a holographic system.

    For a 6d (2,0) SCFT (relevant for M5-branes), the anomaly polynomial is:
        I_8 = (1/48) * [p_2(R) - (1/4)*(p_1(R))^2 + (1/4)*p_1(R)*p_1(N)]

    For the HT (holomorphic-topological) system at central charge c:
    the coefficient of p_2 is determined by the a-anomaly, and p_1^2
    by the c-anomaly.  In 2d, I_8 reduces to products of I_4 by factorization.

    At the EXPLORATORY level: we evaluate I_8 with curvature parameter
    scaled by rho_n (zeta zero).  This has NO established physical meaning.

    Parameters
    ----------
    c : central charge (determines the anomaly coefficients)
    p1 : first Pontryagin class value
    p2 : second Pontryagin class value
    """
    # For 2d holographic system: I_8 factorizes as products of 4-forms
    # I_8 = c_1 * p_2 + c_2 * p_1^2
    # where c_1 = c^2/576, c_2 = -c^2/2304 (from squaring I_4)
    c1_coeff = c ** 2 / 576.0
    c2_coeff = -c ** 2 / 2304.0
    return c1_coeff * p2 + c2_coeff * p1 ** 2


def anomaly_at_zeta_zero(n: int, c: float = 26.0) -> Dict[str, float]:
    r"""Anomaly polynomial evaluated with rho_n-scaled curvature.

    NUMEROLOGICAL: sets p_1 = rho_n * omega (no physical justification).
    """
    rho_n = zeta_zero(n)
    I4 = anomaly_polynomial_I4(c, p1=rho_n)
    I8 = anomaly_polynomial_I8(c, p1=rho_n, p2=rho_n ** 2)
    return {
        'n': n,
        'rho_n': rho_n,
        'I4': I4,
        'I8': I8,
        'c': c,
    }


# ===========================================================================
# Section 11: 3D holomorphic Chern-Simons
# ===========================================================================

def cs_partition_solid_torus(k: int, rank: int = 1,
                              tau: Optional[complex] = None) -> complex:
    r"""Chern-Simons partition function on the solid torus S^1 x D^2.

    For U(1) CS at level k (integer):
        Z_{CS}(S^1 x D^2; k) = 1/sqrt(k)

    For SU(2) CS at level k:
        Z_{CS}(S^1 x D^2; k) = sqrt(2/(k+2)) * sin(pi/(k+2))

    For general SU(N) at level k, the partition function on the solid torus
    (with trivial boundary condition = vacuum representation) is:

        Z = (vol(G) / (k+h^v)^{dim(G)/2}) * prod_{alpha > 0}
            2*sin(pi*<alpha, rho>/(k+h^v))

    For U(1): this simplifies to 1/sqrt(k).

    Parameters
    ----------
    k : Chern-Simons level (must be positive integer for well-defined theory)
    rank : 1 for U(1), 2 for SU(2), etc.
    tau : optional modular parameter (for the solid torus with complex structure)
    """
    if k <= 0:
        raise ValueError(f"CS level must be positive integer, got k={k}")

    if rank == 1:
        # U(1) at level k
        Z = 1.0 / math.sqrt(float(k))
    elif rank == 2:
        # SU(2) at level k: Z = sqrt(2/(k+2)) * sin(pi/(k+2))
        kp = float(k) + 2.0
        Z = math.sqrt(2.0 / kp) * math.sin(PI / kp)
    else:
        # General rank: use the Weyl volume formula
        # Z ~ k^{-dim(G)/2} * (volume factor)
        # For SU(N): dim = N^2-1, h^v = N
        N = rank
        dim_g = N ** 2 - 1
        h_dual = N
        kp = float(k) + h_dual
        Z = kp ** (-dim_g / 2.0)
        # Weyl denominator product (simplified)
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                Z *= 2.0 * math.sin(PI * (j - i) / kp)
    return complex(Z, 0.0)


def cs_at_zeta_zero(n: int, rank: int = 2) -> Dict[str, Any]:
    r"""CS partition function at level k_n derived from zeta zero.

    NUMEROLOGICAL ANSATZ: k_n = round((1+rho_n)/2).
    CS level must be a positive integer, so we round to the nearest integer.

    For rho_1 ~ 14.13: k_1 ~ round(7.57) = 8.
    For rho_2 ~ 21.02: k_2 ~ round(11.01) = 11.
    """
    rho_n = zeta_zero(n)
    k_float = (1.0 + rho_n) / 2.0
    k_int = max(1, round(k_float))

    Z = cs_partition_solid_torus(k_int, rank)

    return {
        'n': n,
        'rho_n': rho_n,
        'k_float': k_float,
        'k_int': k_int,
        'rank': rank,
        'Z_CS': Z,
        'abs_Z': abs(Z),
    }


# ===========================================================================
# Section 12: Open/closed duality at zeta-zero parameters
# ===========================================================================

def annulus_trace_genus1(kappa_val) -> Fraction:
    r"""Annulus trace at genus 1: Tr_A = kappa * lambda_1 = kappa/24.

    PROVED (thm:annulus-trace): the annulus trace Tr_A in HH_*(A)
    at genus 1 is kappa(A) * lambda_1^FP.

    AP34: This is the FIRST modular shadow of the open sector.
    It is NOT the derived center (which is the universal bulk).
    """
    return Fraction(kappa_val) * lambda_fp(1)


def derived_center_dimension(algebra: str = 'heisenberg',
                              weight_max: int = 4) -> Dict[int, int]:
    r"""Dimensions of the chiral derived center Z^der_ch(A) by weight.

    The derived center (Hochschild cohomology of A) has:
        H^0 = center Z(A)
        H^1 = outer derivations
        H^2 = first-order deformations

    For Heisenberg at weight w:
        dim H^0(w) = 1 for all w >= 0 (generated by 1, J, J^2, ...)
        dim H^1(w) = 1 for w >= 1 (derivation J_{-w})
        dim H^2(w) = 0 for w <= 1; dim H^2(2) = 1 (the level deformation)

    For Virasoro at weight w:
        dim H^0(w) = p(w) (partitions, Verma module)
        dim H^1(0) = 0, dim H^1(2) = 1 (the T-derivation)
        dim H^2(0) = 1 (the central extension c)

    These are SIMPLIFIED (weight-truncated) computations.
    The full derived center requires the entire chiral Hochschild complex.
    """
    dims: Dict[int, int] = {}
    if algebra == 'heisenberg':
        for w in range(weight_max + 1):
            dims[w] = 1  # H^0 only, simplified
    elif algebra == 'virasoro':
        # Partition function of Verma module (H^0 contribution)
        for w in range(weight_max + 1):
            dims[w] = _partition_count(w)
    else:
        for w in range(weight_max + 1):
            dims[w] = 1
    return dims


def _partition_count(n: int) -> int:
    """Integer partition count p(n)."""
    if n < 0:
        return 0
    if n <= 1:
        return 1
    # Dynamic programming
    p = [0] * (n + 1)
    p[0] = 1
    for k in range(1, n + 1):
        for j in range(k, n + 1):
            p[j] += p[j - k]
    return p[n]


def open_closed_at_zeta_zero(n: int, c: float = 26.0) -> Dict[str, Any]:
    r"""Open/closed data at zeta-zero parameters.

    Returns:
        - Annulus trace (genus-1 open-to-closed map)
        - Boundary partition function
        - Complementarity data (c vs 26-c)
    """
    rho_n = zeta_zero(n)
    tau_n = modular_parameter_from_zeta_zero(n)

    kappa_A = kappa_virasoro(Fraction(c))
    kappa_A_dual = kappa_virasoro(Fraction(26) - Fraction(c))

    annulus = annulus_trace_genus1(kappa_A)
    annulus_dual = annulus_trace_genus1(kappa_A_dual)

    # Complementarity sum (AP24)
    # For Virasoro: kappa + kappa' = c/2 + (26-c)/2 = 13
    kappa_sum = kappa_A + kappa_A_dual

    Z_boundary = boundary_partition_virasoro(tau_n, c=c)
    Z_boundary_dual = boundary_partition_virasoro(tau_n, c=26.0 - c)

    return {
        'n': n,
        'rho_n': rho_n,
        'tau_n': tau_n,
        'c': c,
        'c_dual': 26.0 - c,
        'kappa': float(kappa_A),
        'kappa_dual': float(kappa_A_dual),
        'kappa_sum': float(kappa_sum),
        'kappa_sum_exact': kappa_sum,  # Should be 13 for Virasoro (AP24)
        'annulus_trace': float(annulus),
        'annulus_trace_dual': float(annulus_dual),
        'Z_boundary': Z_boundary,
        'Z_boundary_dual': Z_boundary_dual,
        'abs_Z_boundary': abs(Z_boundary),
        'abs_Z_boundary_dual': abs(Z_boundary_dual),
    }


# ===========================================================================
# Section 13: Complementarity and holographic dictionary
# ===========================================================================

def complementarity_check(c: float) -> Dict[str, Any]:
    r"""Complementarity data for the Koszul pair (Vir_c, Vir_{26-c}).

    AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.
    NOT zero (except at c=13 where kappa = kappa' = 13/2).

    AP29: delta_kappa = kappa - kappa' = c/2 - (26-c)/2 = c - 13.
    kappa_eff = kappa(matter) + kappa(ghost) = c/2 - 13 = (c-26)/2.

    At c=13: delta_kappa = 0 (self-dual point).
    At c=26: kappa_eff = 0 (anomaly cancellation, critical string).
    These are DIFFERENT conditions at DIFFERENT central charges (AP29).
    """
    kappa_A = kappa_virasoro(Fraction(c))
    kappa_A_dual = kappa_virasoro(Fraction(26) - Fraction(c))

    return {
        'c': c,
        'c_dual': 26.0 - float(c),
        'kappa': float(kappa_A),
        'kappa_dual': float(kappa_A_dual),
        'kappa_sum': float(kappa_A + kappa_A_dual),
        'delta_kappa': float(kappa_A - kappa_A_dual),
        'kappa_eff': float(kappa_eff(kappa_A)),
        'is_self_dual': (c == 13),
        'is_critical': (c == 26),
        'complementarity_holds': (kappa_A + kappa_A_dual == Fraction(13)),
    }


def holographic_dictionary_entry(c: float, n: int) -> Dict[str, Any]:
    r"""Full holographic dictionary entry at zeta zero n for central charge c.

    Compiles:
      - Boundary: Z_partial, kappa, annulus trace
      - Bulk: shadow F_g, kappa_eff, BTZ data
      - Complementarity: c vs 26-c
      - Celestial: soft factor at Delta_n
      - CS: partition function at k_n
      - Anomaly: I_4, I_8
    """
    boundary = open_closed_at_zeta_zero(n, c)
    bulk = bulk_shadow_table(c)
    btz = btz_at_zeta_zero(n, c)
    celestial = celestial_at_zeta_zero(n)
    cs = cs_at_zeta_zero(n)
    anomaly = anomaly_at_zeta_zero(n, c)
    comp = complementarity_check(c)

    return {
        'boundary': boundary,
        'bulk': bulk,
        'btz': btz,
        'celestial': celestial,
        'cs': cs,
        'anomaly': anomaly,
        'complementarity': comp,
    }


# ===========================================================================
# Section 14: Shadow partition function at zeta-zero temperature
# ===========================================================================

def shadow_partition_at_zeta_zero(n: int, c: float = 26.0,
                                   g_max: int = 5,
                                   use_effective: bool = False) -> Dict[str, Any]:
    r"""Shadow partition function Z^sh evaluated at zeta-zero BTZ temperature.

    Z^sh = exp(sum_{g=1}^{g_max} hbar^{2g} F_g)

    where hbar = 2*pi / S_BH (inverse Bekenstein-Hawking entropy).

    Parameters
    ----------
    n : zeta zero index
    c : central charge
    g_max : maximum genus in the shadow expansion
    use_effective : if True, use kappa_eff instead of kappa(A)
    """
    btz = btz_at_zeta_zero(n, c)
    S_BH = btz['S_BH']

    if S_BH <= 0:
        return {'error': 'S_BH <= 0', 'n': n, 'c': c}

    hbar = TWO_PI / S_BH

    if use_effective:
        kappa_val = kappa_eff(kappa_virasoro(Fraction(c)))
    else:
        kappa_val = kappa_virasoro(Fraction(c))

    F_table = {}
    exponent = 0.0
    for g in range(1, g_max + 1):
        Fg = float(Fraction(kappa_val) * lambda_fp(g))
        F_table[g] = Fg
        exponent += hbar ** (2 * g) * Fg

    Z_sh = math.exp(exponent)

    return {
        'n': n,
        'c': c,
        'rho_n': btz['rho_n'],
        'S_BH': S_BH,
        'hbar': hbar,
        'kappa': float(kappa_val),
        'F_g': F_table,
        'exponent': exponent,
        'Z_sh': Z_sh,
        'g_max': g_max,
    }


# ===========================================================================
# Section 15: Summary and cross-verification
# ===========================================================================

def cardy_btz_consistency(c: float, n_zeros: int = 10) -> List[Dict[str, Any]]:
    r"""Verify Cardy-BTZ consistency at each zeta-zero parameter.

    At each temperature T_n = 2/(1+rho_n):
      - S_BH = pi^2*c/(3*beta_n) from the BTZ geometry
      - S_Cardy = 2*pi*sqrt(c*E_n/6) from the Cardy formula with E_n = pi^2*c/(6*beta_n^2)
      - These must agree (proved identity, not numerological)

    This is a MATHEMATICAL CONSISTENCY CHECK of the formulas, not a
    physical prediction about zeta zeros.
    """
    results = []
    for n in range(1, n_zeros + 1):
        btz = btz_at_zeta_zero(n, c)
        beta = btz['beta_n']
        S_BH = btz['S_BH']

        E_n = PI ** 2 * c / (6.0 * beta ** 2)
        S_Cardy = cardy_entropy(c, E_n)

        match = abs(S_BH - S_Cardy) < 1e-10 * max(abs(S_BH), 1.0)

        results.append({
            'n': n,
            'rho_n': btz['rho_n'],
            'beta': beta,
            'S_BH': S_BH,
            'S_Cardy': S_Cardy,
            'match': match,
            'relative_error': abs(S_BH - S_Cardy) / max(abs(S_BH), 1e-300),
        })
    return results


def tachyon_mass_at_zeta_zeros(n_max: int = 10) -> List[Dict[str, Any]]:
    r"""Tachyon effective mass at zeta-zero BTZ temperatures (c=26 only).

    The bosonic string tachyon has m^2 = -4/alpha' = -4 (alpha'=1/2).
    The thermal mass shift: m_eff^2 = m^2 + (4*pi^2/beta^2).

    The Hagedorn temperature: beta_H = pi*sqrt(2*alpha'*(c-2)) = pi*sqrt(24) ~ 15.4.
    For beta < beta_H: tachyon condensation occurs (m_eff^2 > 0 not sufficient
    to prevent instability; the Hagedorn temperature is the real criterion).
    """
    results = []
    alpha_prime = 0.5
    m_sq = -4.0  # m^2 = -4/alpha' with alpha'=1/2 gives m^2 = -4 in these units
    hagedorn_beta = PI * math.sqrt(2.0 * alpha_prime * 24.0)  # c-2 = 24 for c=26

    for n in range(1, n_max + 1):
        btz = btz_at_zeta_zero(n, c=26.0)
        beta = btz['beta_n']
        m_eff_sq = m_sq + 4.0 * PI ** 2 / (beta ** 2)

        results.append({
            'n': n,
            'rho_n': btz['rho_n'],
            'beta': beta,
            'hagedorn_beta': hagedorn_beta,
            'm_sq_bare': m_sq,
            'm_eff_sq': m_eff_sq,
            'tachyonic': (m_eff_sq < 0),
            'below_hagedorn': (beta < hagedorn_beta),
        })
    return results


def full_holographic_scan(c: float = 26.0, n_max: int = 10,
                           g_max: int = 5) -> Dict[str, Any]:
    r"""Full scan of holographic data at zeta-zero parameters.

    Returns a comprehensive dictionary with all computations.

    DISCLAIMER: The zeta-zero evaluations are NUMEROLOGICAL.  The
    mathematically rigorous content is the formulas themselves (partition
    functions, Cardy, BTZ, shadows, CS), not their evaluation at
    zeta-zero parameters.
    """
    boundary_table = boundary_Z_table(c, n_max)
    shadow_table = {
        n: shadow_partition_at_zeta_zero(n, c, g_max)
        for n in range(1, n_max + 1)
    }
    btz_table = {n: btz_at_zeta_zero(n, c) for n in range(1, n_max + 1)}
    cs_table = {n: cs_at_zeta_zero(n) for n in range(1, n_max + 1)}
    consistency = cardy_btz_consistency(c, n_max)
    comp = complementarity_check(c)

    return {
        'c': c,
        'n_max': n_max,
        'g_max': g_max,
        'boundary': boundary_table,
        'shadow': shadow_table,
        'btz': btz_table,
        'cs': cs_table,
        'cardy_consistency': consistency,
        'complementarity': comp,
    }
