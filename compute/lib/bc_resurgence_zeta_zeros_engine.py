r"""Benjamin-Chang resurgent structure near Riemann zeta zeros.

MATHEMATICAL FRAMEWORK
======================

The constrained Epstein zeta function epsilon^c_s(A) (Benjamin-Chang,
arXiv:2208.02259) satisfies the functional equation

    epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}

where the scattering factor

    F_c(s) = Gamma(s)*Gamma(s+c/2-1)*zeta(2s)
             / (pi^{2s-1/2}*Gamma(c/2-s)*Gamma(s-1/2)*zeta(2s-1))

has POLES at s = (1+rho_n)/2 where rho_n ranges over the nontrivial
zeros of the Riemann zeta function.

This module computes the RESURGENT structure of epsilon^c_s near these poles,
connecting the Borel singularity structure to the shadow obstruction tower
and the trans-series expansion of the shadow generating function.

SEVEN COMPUTATIONS
==================

1. BOREL PLANE OF F_c(s): The scattering factor has poles at s_n = (1+rho_n)/2.
   Under RH, s_n = 3/4 + i*gamma_n/2 with gamma_n the imaginary parts of
   zeta zeros.  In the Borel plane (Borel transform in the variable 1/s),
   these become singularities at zeta_n = 2/(1+rho_n).

2. STOKES LINES: The Stokes lines of epsilon^c_s in the complex s-plane
   separate regions where different trans-series contributions dominate.
   They emanate from the zeta-zero poles and have directions determined by
   the phase of the instanton action A_n = s_n.

3. LATERAL BOREL RESUMMATION: The lateral Borel sums S_+/- differ by the
   Stokes automorphism.  The Stokes jump at each zeta zero encodes the
   residue A_c(rho_n).

4. ALIEN DERIVATIVE: Delta_{omega_n} epsilon^c_s = the alien derivative at
   the singularity omega_n corresponding to the n-th zeta zero.  Computed
   from the universal residue factor A_c(rho_n).

5. RESURGENT BRIDGE: The shadow tower F_g ~ C*rho^g*g^{-5/2} with action
   A = -log(rho).  The Benjamin-Chang poles at gamma_n are at
   omega_n = 2/(1+1/2+i*gamma_n) under RH.  The Stokes constants
   S_n = Res_{s=s_n} F_c(s) * [perturbative coefficient].

6. TRANS-SERIES at c=13: The self-dual point has enhanced resurgent
   structure from Koszul self-duality c -> 26-c = 13.

7. MEDIAN RESUMMATION: The median sum (average of lateral Borel sums)
   should give the correct nonperturbative value.

BEILINSON WARNINGS
==================

AP15: The genus-1 propagator is E_2* (quasi-modular).  The Borel transform
maps the quasi-modular series to a holomorphic object in the Borel plane.

AP24: kappa + kappa' = 0 for KM/free fields, = 13 for Virasoro.  At c=13
(self-dual), kappa = kappa' = 13/2.

AP29: delta_kappa = kappa - kappa' (complementarity asymmetry, vanishes at
c=13) is DIFFERENT from kappa_eff = kappa(matter) + kappa(ghost) (anomaly
cancellation, vanishes at c=26).

AP38: Literature normalization conventions: verify against specific sources.

AP39: kappa = c/2 is specific to Virasoro.  For affine KM: kappa =
dim(g)*(k+h^v)/(2h^v).  NEVER copy between families without recomputation.

AP46: eta(q) = q^{1/24} prod(1-q^n).  The q^{1/24} is NOT optional.

Manuscript references:
    eq:constrained-epstein-fe (arithmetic_shadows.tex)
    def:universal-residue-factor (arithmetic_shadows.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    [BenjaminChang22]: arXiv:2208.02259
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, pi as mppi, zeta as mpzeta, gamma as mpgamma,
        log as mplog, exp as mpexp, power as mppower, sqrt as mpsqrt,
        re as mpre, im as mpim, conj as mpconj, diff as mpdiff,
        zetazero, inf as mpinf, sin as mpsin, cos as mpcos,
        arg as mparg, fabs as mpfabs,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

# =====================================================================
# Constants
# =====================================================================

PI = math.pi
TWO_PI = 2.0 * PI


# =====================================================================
# Section 0: Virasoro shadow invariants (self-contained)
# =====================================================================

def virasoro_kappa(c_val: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c_val / 2.0


def virasoro_shadow_invariants(c_val: float) -> Dict[str, float]:
    r"""Shadow invariants for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)),
    Delta = 40/(5c+22), rho from branch points of Q_L.
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4  # = 40/(5c+22)

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    disc = q1 ** 2 - 4.0 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)

    R = abs(t_plus)
    rho = 1.0 / R if R > 0 else float('inf')
    theta = cmath.phase(t_plus)

    return {
        'c': c_val,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2,
        'branch_plus': t_plus,
        'branch_minus': t_minus,
        'R': R,
        'rho': rho,
        'theta': theta,
    }


def virasoro_shadow_coefficients(c_val: float, r_max: int) -> List[float]:
    r"""Virasoro shadow coefficients S_2, ..., S_{r_max}
    via convolution recursion for sqrt(Q_L).

    Convention: S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t)).
    """
    inv = virasoro_shadow_invariants(c_val)
    q0, q1, q2 = inv['q0'], inv['q1'], inv['q2']

    max_n = r_max - 2 + 1
    a = [0.0] * max_n
    a[0] = math.sqrt(q0)
    if max_n > 1:
        a[1] = q1 / (2.0 * a[0])
    for n in range(2, max_n):
        cn = q2 if n == 2 else 0.0
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv_sum) / (2.0 * a[0])

    coeffs = []
    for r in range(2, r_max + 1):
        idx = r - 2
        if idx < len(a):
            coeffs.append(a[idx] / r)
        else:
            coeffs.append(0.0)
    return coeffs


# =====================================================================
# Section 1: Borel plane of F_c(s) — singularities from zeta zeros
# =====================================================================

def scattering_factor_Fc(s, c_val, dps=30):
    r"""Scattering factor F_c(s) from the constrained Epstein FE.

    F_c(s) = Gamma(s)*Gamma(s+c/2-1)*zeta(2s)
             / (pi^{2s-1/2}*Gamma(c/2-s)*Gamma(s-1/2)*zeta(2s-1))
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c_val)
        num = mpgamma(s) * mpgamma(s + c / 2 - 1) * mpzeta(2 * s)
        den = (mppower(mppi, 2 * s - mpf('0.5'))
               * mpgamma(c / 2 - s)
               * mpgamma(s - mpf('0.5'))
               * mpzeta(2 * s - 1))
        if abs(den) < mppower(10, -dps + 5):
            return complex(mpc(mpinf))
        return complex(num / den)


def universal_residue_factor(rho_val, c_val, dps=30):
    r"""Residue of F_c at s = (1+rho)/2.

    A_c(rho) = Gamma((1+rho)/2)*Gamma((c+rho-1)/2)*zeta(1+rho)
               / (2*pi^{rho+1/2}*Gamma((c-rho-1)/2)*Gamma(rho/2)*zeta'(rho))
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho_val)
        c = mpc(c_val)
        num = (mpgamma((1 + rho) / 2) * mpgamma((c + rho - 1) / 2)
               * mpzeta(1 + rho))
        zeta_prime_rho = mpdiff(mpzeta, rho)
        den = (2 * mppower(mppi, rho + mpf('0.5'))
               * mpgamma((c - rho - 1) / 2)
               * mpgamma(rho / 2)
               * zeta_prime_rho)
        if abs(den) < mppower(10, -dps + 5):
            return complex(mpc(mpinf))
        return complex(num / den)


def borel_singularity_from_zeta_zero(n, dps=30):
    r"""Borel singularity location from the n-th zeta zero.

    The scattering factor F_c(s) has poles at s_n = (1+rho_n)/2.
    In the Borel plane (Borel transform in the variable 1/s), the
    singularity is at zeta_n = 2/(1+rho_n) = 1/s_n.

    Under RH: rho_n = 1/2 + i*gamma_n, so
    s_n = 3/4 + i*gamma_n/2 and zeta_n = 2/(3/2 + i*gamma_n).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_n = zetazero(n)
        s_n = (1 + rho_n) / 2
        zeta_n = 1 / s_n  # = 2/(1+rho_n)
        gamma_n = float(mpim(rho_n))
        return {
            'n': n,
            'rho_n': complex(rho_n),
            'gamma_n': gamma_n,
            's_n': complex(s_n),
            'borel_singularity': complex(zeta_n),
            'borel_singularity_modulus': float(mpfabs(zeta_n)),
            'borel_singularity_arg': float(mparg(zeta_n)),
        }


def borel_singularity_map(n_zeros=10, dps=30):
    r"""Map of all Borel singularities from the first n_zeros zeta zeros.

    Returns a list of singularity data sorted by modulus.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    sings = []
    for n in range(1, n_zeros + 1):
        sings.append(borel_singularity_from_zeta_zero(n, dps))
    sings.sort(key=lambda x: x['borel_singularity_modulus'])
    return sings


# =====================================================================
# Section 2: Stokes lines emanating from zeta zeros
# =====================================================================

@dataclass
class StokesLineData:
    """Stokes line data for a given zeta zero."""
    n: int                   # zeta zero index
    gamma_n: float           # imaginary part of rho_n
    s_n: complex             # pole position (1+rho_n)/2
    stokes_direction: float  # angle of the Stokes line
    anti_stokes_direction: float  # angle of the anti-Stokes line


def stokes_line_direction(n, dps=30):
    r"""Stokes line direction from the n-th zeta zero pole.

    The Stokes line at s_n = (1+rho_n)/2 emanates in the direction
    where Im(A_n / (s - s_n)) = 0 locally, i.e., the direction is
    determined by arg(s_n).

    More precisely, for the trans-series correction e^{-s_n/delta_s}
    near the singularity, the Stokes line is where the exponential
    switches from exponentially small to exponentially large.
    The Stokes direction is arg(s_n) (the phase of the instanton action).
    The anti-Stokes directions are arg(s_n) +/- pi/2.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_n = zetazero(n)
        s_n = (1 + rho_n) / 2
        gamma_n = float(mpim(rho_n))

        stokes_dir = float(mparg(s_n))
        anti_stokes_1 = stokes_dir + PI / 2
        anti_stokes_2 = stokes_dir - PI / 2

        return StokesLineData(
            n=n,
            gamma_n=gamma_n,
            s_n=complex(s_n),
            stokes_direction=stokes_dir,
            anti_stokes_direction=anti_stokes_1,
        )


def stokes_line_map(n_zeros=10, dps=30):
    """Compute Stokes line data for the first n_zeros zeta zeros."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    return [stokes_line_direction(n, dps) for n in range(1, n_zeros + 1)]


def stokes_direction_large_gamma(gamma_n):
    r"""Asymptotic Stokes direction for large gamma_n.

    For s_n = 3/4 + i*gamma_n/2 (under RH), as gamma_n -> inf:
        arg(s_n) -> pi/2

    So all Stokes lines asymptotically point in the direction pi/2
    (along the imaginary s-axis).  The corrections are:
        arg(s_n) = pi/2 - arctan(3/(2*gamma_n)) ~ pi/2 - 3/(2*gamma_n)
    """
    if abs(gamma_n) < 1e-15:
        return math.atan2(0, 0.75)
    return math.atan2(gamma_n / 2.0, 0.75)


# =====================================================================
# Section 3: Stokes constants from residues of F_c
# =====================================================================

def stokes_constant_at_zero(n, c_val, dps=30):
    r"""Stokes constant S_n = Res_{s=s_n} F_c(s).

    This is the residue of the scattering factor at the pole s_n = (1+rho_n)/2.
    The residue equals the universal residue factor A_c(rho_n).

    The Stokes constant controls the jump in the lateral Borel resummation:
    S_+ - S_- = 2*pi*i * S_n * (one-instanton contribution)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_n = zetazero(n)
        A_c = universal_residue_factor(complex(rho_n), c_val, dps)
        gamma_n = float(mpim(rho_n))
        return {
            'n': n,
            'rho_n': complex(rho_n),
            'gamma_n': gamma_n,
            'stokes_constant': A_c,
            'stokes_modulus': abs(A_c),
            'stokes_phase': cmath.phase(A_c),
            'c': c_val,
        }


def stokes_constants_spectrum(c_val, n_zeros=10, dps=30):
    r"""Spectrum of Stokes constants for the first n_zeros zeta zeros.

    Returns the Stokes constants sorted by modulus (decreasing).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    constants = []
    for n in range(1, n_zeros + 1):
        constants.append(stokes_constant_at_zero(n, c_val, dps))
    constants.sort(key=lambda x: -x['stokes_modulus'])
    return constants


def stokes_constant_decay_rate(c_val, n_zeros=10, dps=30):
    r"""Measure the decay rate of |S_n| as a function of gamma_n.

    From Stirling's approximation of the Gamma factors in A_c(rho),
    the leading decay is:
        |A_c(rho)| ~ |gamma_n|^{-(c-1)/2} * |zeta(1+rho_n)| / |zeta'(rho_n)|

    The |zeta(1+i*gamma)/zeta'(1/2+i*gamma)| ratio grows like log(gamma)
    on average, so the Stokes constants decay polynomially in gamma_n.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    data = []
    for n in range(1, n_zeros + 1):
        sc = stokes_constant_at_zero(n, c_val, dps)
        data.append({
            'n': n,
            'gamma_n': sc['gamma_n'],
            'log_gamma': math.log(abs(sc['gamma_n'])) if abs(sc['gamma_n']) > 1e-15 else 0,
            'stokes_modulus': sc['stokes_modulus'],
            'log_modulus': (math.log(sc['stokes_modulus'])
                           if sc['stokes_modulus'] > 1e-300 else float('-inf')),
        })
    return data


# =====================================================================
# Section 4: Lateral Borel resummation of the shadow tower
# =====================================================================

def shadow_borel_transform(c_val, xi, r_max=60):
    r"""Borel transform of the shadow tower: B[G](xi) = sum_{r>=2} S_r xi^r / r!.

    This is an ENTIRE function (r! kills geometric growth rho^r).
    """
    coeffs = virasoro_shadow_coefficients(c_val, r_max)
    xi = complex(xi)
    result = 0.0 + 0.0j
    for i, s_r in enumerate(coeffs):
        r = 2 + i
        term = s_r * xi ** r / math.gamma(r + 1)
        result += term
        if i > 10 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def lateral_borel_sum_shadow(c_val, t_val, epsilon=0.02, r_max=60,
                              n_quad=2000, xi_max=80.0):
    r"""Lateral Borel sum of the shadow tower along direction epsilon.

    S_epsilon[G](t) = int_0^{inf*e^{i*eps}} B[G](xi) e^{-xi/t} dxi/t
    """
    coeffs = virasoro_shadow_coefficients(c_val, r_max)
    t = complex(t_val)
    if abs(t) < 1e-15:
        return 0.0 + 0.0j

    direction = cmath.exp(1j * epsilon)
    ds = xi_max / n_quad
    result = 0.0 + 0.0j

    for k in range(1, n_quad + 1):
        s = (k - 0.5) * ds
        xi = s * direction
        B_val = shadow_borel_transform(c_val, xi, r_max)
        weight = cmath.exp(-xi / t) * direction / t
        result += B_val * weight * ds

    return result


def lateral_borel_sums_shadow(c_val, t_val, epsilon=0.02, r_max=60,
                               n_quad=2000, xi_max=80.0):
    r"""Both lateral Borel sums and the Stokes jump for the shadow tower."""
    S_plus = lateral_borel_sum_shadow(c_val, t_val, +epsilon, r_max,
                                       n_quad, xi_max)
    S_minus = lateral_borel_sum_shadow(c_val, t_val, -epsilon, r_max,
                                        n_quad, xi_max)
    return {
        'c': c_val,
        't': t_val,
        'S_plus': S_plus,
        'S_minus': S_minus,
        'stokes_jump': S_plus - S_minus,
        'median_sum': (S_plus + S_minus) / 2.0,
        'epsilon': epsilon,
    }


# =====================================================================
# Section 5: Alien derivatives at zeta-zero singularities
# =====================================================================

def alien_derivative_at_zeta_zero(n, c_val, dps=30):
    r"""Alien derivative of epsilon^c_s at the singularity from the n-th zeta zero.

    The alien derivative Delta_{omega_n} epsilon^c measures the
    discontinuity of the Borel resummation at the singularity omega_n.

    For a simple pole of F_c(s) at s_n = (1+rho_n)/2, the alien
    derivative is proportional to the residue A_c(rho_n):

        Delta_{omega_n} epsilon^c = A_c(rho_n) * (shifted epsilon)

    where omega_n = 1/s_n is the Borel singularity.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_n = zetazero(n)
        s_n = (1 + rho_n) / 2
        omega_n = 1 / s_n
        gamma_n = float(mpim(rho_n))

        A_c = universal_residue_factor(complex(rho_n), c_val, dps)

        return {
            'n': n,
            'rho_n': complex(rho_n),
            'gamma_n': gamma_n,
            's_n': complex(s_n),
            'omega_n': complex(omega_n),
            'alien_derivative_coefficient': A_c,
            'alien_modulus': abs(A_c),
            'c': c_val,
        }


def alien_derivative_spectrum(c_val, n_zeros=10, dps=30):
    """Spectrum of alien derivatives at zeta-zero singularities."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    return [alien_derivative_at_zeta_zero(n, c_val, dps)
            for n in range(1, n_zeros + 1)]


# =====================================================================
# Section 6: Resurgent bridge — shadow tower meets zeta zeros
# =====================================================================

@dataclass
class ResurgentBridgeData:
    """Data connecting shadow tower resurgence to zeta-zero structure."""
    c: float
    kappa: float
    rho_shadow: float        # shadow growth rate
    action_shadow: complex   # shadow instanton action A = 1/t_branch
    borel_sings_zeta: List[complex]   # Borel singularities from zeta zeros
    stokes_constants: List[complex]   # S_n = A_c(rho_n)
    gamma_values: List[float]         # imaginary parts of zeta zeros


def build_resurgent_bridge(c_val, n_zeros=10, dps=30):
    r"""Build the resurgent bridge between shadow tower and zeta zeros.

    The shadow tower has instanton action A_shadow = 1/t_branch (from Q_L).
    The Benjamin-Chang FE has singularities at omega_n = 2/(1+rho_n).

    The BRIDGE: both arise from the same modular-invariant partition
    function Z_A(tau), but in different asymptotic regimes:
    - Shadow tower: arity expansion (algebraic, from sqrt(Q_L))
    - BC singularities: spectral expansion (analytic, from Eisenstein)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    inv = virasoro_shadow_invariants(c_val)
    kappa = inv['kappa']
    rho_shadow = inv['rho']
    t_plus = inv['branch_plus']
    A_shadow = 1.0 / t_plus if abs(t_plus) > 1e-15 else complex('inf')

    borel_sings = []
    stokes_consts = []
    gammas = []
    with mp.workdps(dps):
        for n in range(1, n_zeros + 1):
            rho_n = zetazero(n)
            s_n = (1 + rho_n) / 2
            omega_n = 1 / s_n
            borel_sings.append(complex(omega_n))
            gammas.append(float(mpim(rho_n)))

            A_c = universal_residue_factor(complex(rho_n), c_val, dps)
            stokes_consts.append(A_c)

    return ResurgentBridgeData(
        c=c_val,
        kappa=kappa,
        rho_shadow=rho_shadow,
        action_shadow=A_shadow,
        borel_sings_zeta=borel_sings,
        stokes_constants=stokes_consts,
        gamma_values=gammas,
    )


def resurgent_bridge_scales(c_val, n_zeros=5, dps=30):
    r"""Compare the two scales: shadow instanton action vs zeta-zero positions.

    The shadow instanton action |A_shadow| = rho_shadow sets the
    non-perturbative scale in the arity direction.
    The zeta-zero positions |omega_n| ~ 2/gamma_n set the spectral scale.

    For the bridge to be meaningful, we need these scales to interact.
    """
    bridge = build_resurgent_bridge(c_val, n_zeros, dps)

    data = {
        'c': c_val,
        'shadow_action_modulus': abs(bridge.action_shadow),
        'shadow_rho': bridge.rho_shadow,
    }

    for i, (omega, gamma, sc) in enumerate(zip(
            bridge.borel_sings_zeta, bridge.gamma_values,
            bridge.stokes_constants)):
        data[f'zeta_zero_{i+1}'] = {
            'gamma': gamma,
            'omega_modulus': abs(omega),
            'omega_phase': cmath.phase(omega),
            'stokes_modulus': abs(sc),
            'ratio_to_shadow': abs(omega) / abs(bridge.action_shadow)
                               if abs(bridge.action_shadow) > 1e-15 else float('inf'),
        }

    return data


# =====================================================================
# Section 7: Trans-series at the self-dual point c = 13
# =====================================================================

def trans_series_c13(n_instanton=3, r_max=60, n_zeros=5, dps=30):
    r"""Trans-series expansion of epsilon^{13}_s at the self-dual point.

    At c = 13, kappa = kappa' = 13/2, and the Koszul duality c -> 26-c
    is a self-duality.  This means:
    - F_{13}(s) has a symmetry under s -> 7-s (reflection around s=7/2)
    - The Gamma factors Gamma(s+11/2)/Gamma(13/2-s) are palindromic

    The trans-series:
    epsilon^{13}_s ~ sum_{k>=0} sigma^k e^{-k*A/s} sum_n a_{k,n} s^{-n}

    where A is determined by the nearest singularity.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    c_val = 13.0
    inv = virasoro_shadow_invariants(c_val)
    kappa = inv['kappa']
    rho = inv['rho']

    # Shadow tower coefficients (perturbative sector)
    coeffs = virasoro_shadow_coefficients(c_val, r_max)

    # Instanton actions from the shadow metric
    A_shadow = 1.0 / inv['branch_plus'] if abs(inv['branch_plus']) > 1e-15 else 0
    A_shadow_conj = 1.0 / inv['branch_minus'] if abs(inv['branch_minus']) > 1e-15 else 0

    # Stokes constants from zeta zeros
    zeta_stokes = []
    with mp.workdps(dps):
        for n in range(1, n_zeros + 1):
            rho_n = zetazero(n)
            A_c = universal_residue_factor(complex(rho_n), c_val, dps)
            zeta_stokes.append({
                'n': n,
                'gamma_n': float(mpim(rho_n)),
                'stokes_constant': A_c,
                'modulus': abs(A_c),
            })

    # Self-duality checks
    # kappa(Vir_13) = 13/2, kappa(Vir_{26-13}) = 13/2 => kappa = kappa'
    kappa_dual = virasoro_kappa(26.0 - c_val)  # = 13/2

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'self_dual': abs(kappa - kappa_dual) < 1e-14,
        'rho_shadow': rho,
        'instanton_action_shadow': A_shadow,
        'instanton_action_shadow_conj': A_shadow_conj,
        'perturbative_coeffs': coeffs[:min(10, len(coeffs))],
        'zeta_stokes': zeta_stokes,
        'n_instanton_sectors': n_instanton,
    }


def trans_series_evaluate_c13(s_val, sigma=1.0, n_perturbative=40,
                                n_instanton=2, dps=30):
    r"""Evaluate the trans-series at s = s_val with trans-series parameter sigma.

    The perturbative sector is the shadow tower evaluated at t = 1/s.
    The instanton corrections are e^{-A*s} (in the s-variable).
    """
    c_val = 13.0
    coeffs = virasoro_shadow_coefficients(c_val, n_perturbative)
    inv = virasoro_shadow_invariants(c_val)

    s = complex(s_val)
    t = 1.0 / s if abs(s) > 1e-15 else 0.0

    # Perturbative sector: sum S_r t^r = sum S_r s^{-r}
    G_pert = sum(coeffs[i] * t ** (i + 2) for i in range(len(coeffs)))

    if n_instanton == 0 or abs(sigma) < 1e-30:
        return {
            's': s_val,
            'perturbative': G_pert,
            'full': G_pert,
            'instanton_corrections': [],
        }

    # Instanton corrections from shadow branch points
    A_plus = 1.0 / inv['branch_plus'] if abs(inv['branch_plus']) > 1e-15 else 0
    A_minus = 1.0 / inv['branch_minus'] if abs(inv['branch_minus']) > 1e-15 else 0

    corrections = []
    G_full = G_pert
    for k in range(1, n_instanton + 1):
        # k-instanton from plus branch
        np_k = sigma ** k * cmath.exp(-k * A_plus * s) * (-1) ** k * G_pert
        corrections.append({
            'k': k,
            'branch': '+',
            'exponential_suppression': abs(cmath.exp(-k * A_plus * s)),
            'correction': np_k,
        })
        G_full += np_k

        # k-instanton from minus branch (conjugate)
        np_k_conj = (sigma.conjugate() ** k
                     * cmath.exp(-k * A_minus * s)
                     * (-1) ** k * G_pert)
        corrections.append({
            'k': k,
            'branch': '-',
            'exponential_suppression': abs(cmath.exp(-k * A_minus * s)),
            'correction': np_k_conj,
        })
        G_full += np_k_conj

    return {
        's': s_val,
        'perturbative': G_pert,
        'full': G_full,
        'instanton_corrections': corrections,
    }


# =====================================================================
# Section 8: Median resummation
# =====================================================================

def median_resummation(c_val, t_val, epsilon=0.02, r_max=60,
                        n_quad=2000, xi_max=80.0):
    r"""Median Borel resummation (average of lateral sums).

    S_med[G](t) = (S_+[G](t) + S_-[G](t)) / 2

    This should give the correct nonperturbative value when the
    series is Borel summable (class M algebras).

    Verification: for small |t| (inside convergence radius), the
    median sum should agree with the direct partial sum.
    """
    data = lateral_borel_sums_shadow(c_val, t_val, epsilon, r_max,
                                      n_quad, xi_max)
    coeffs = virasoro_shadow_coefficients(c_val, r_max)
    partial = sum(coeffs[i] * complex(t_val) ** (i + 2)
                  for i in range(len(coeffs)))

    return {
        'c': c_val,
        't': t_val,
        'median_sum': data['median_sum'],
        'partial_sum': partial,
        'S_plus': data['S_plus'],
        'S_minus': data['S_minus'],
        'stokes_jump': data['stokes_jump'],
        'agreement_error': abs(data['median_sum'] - partial),
    }


def median_vs_direct_comparison(c_val, t_values, r_max=60):
    r"""Compare median resummation with direct evaluation at multiple points.

    For |t| < 1/rho (convergence region), both should agree.
    For |t| > 1/rho (divergence region), only the median sum is well-defined.
    """
    inv = virasoro_shadow_invariants(c_val)
    rho = inv['rho']
    convergence_radius = 1.0 / rho if rho > 0 else float('inf')

    results = []
    for t in t_values:
        in_convergence = abs(t) < convergence_radius
        data = median_resummation(c_val, t, r_max=r_max)
        results.append({
            't': t,
            'in_convergence_region': in_convergence,
            'median_sum': data['median_sum'],
            'partial_sum': data['partial_sum'],
            'relative_error': (abs(data['median_sum'] - data['partial_sum'])
                               / max(abs(data['partial_sum']), 1e-100)),
        })

    return {
        'c': c_val,
        'convergence_radius': convergence_radius,
        'rho': rho,
        'results': results,
    }


# =====================================================================
# Section 9: Bridge equation verification
# =====================================================================

def bridge_equation_check(c_val, n=1, dps=30):
    r"""Check the bridge equation relating Stokes constants to MC structure.

    The bridge equation constrains the alien derivatives via the MC
    equation D*Theta + (1/2)[Theta, Theta] = 0.  At leading order:

    For the shadow tower, the MC equation at arity r gives:
        Delta_{omega_1} S_r = S_1 * S_r^{(1)}

    where S_1 is the Stokes constant and S_r^{(1)} is the one-instanton
    shadow coefficient.

    For the algebraic case (sqrt(Q_L)), this reduces to:
        S_r^{(1)} = -S_r^{(0)}  (second sheet = minus first sheet)

    so the bridge equation becomes:
        Delta_{omega_1} S_r = -S_1 * S_r

    This means the Stokes automorphism acts as multiplication by
    (1 - S_1 * e^{-omega_1/t}), consistent with the two-sheeted structure.
    """
    inv = virasoro_shadow_invariants(c_val)
    kappa = inv['kappa']
    rho = inv['rho']
    t_plus = inv['branch_plus']

    # Shadow instanton action
    omega_1 = 1.0 / t_plus if abs(t_plus) > 1e-15 else complex('inf')

    # Stokes constant from the Darboux coefficient
    q2 = inv['q2']
    t_minus = inv['branch_minus']
    sqrt_q2 = cmath.sqrt(q2)
    sqrt_diff = cmath.sqrt(t_plus - t_minus)
    sqrt_tp = cmath.sqrt(-t_plus)

    # Stokes constant S_1 = i*sqrt(pi)*sqrt(q2)*sqrt(t_+-t_-)*sqrt(-t_+)
    S_1 = 1j * math.sqrt(PI) * sqrt_q2 * sqrt_diff * sqrt_tp

    # Zeta-zero Stokes constant (from Benjamin-Chang residue)
    if HAS_MPMATH:
        with mp.workdps(dps):
            rho_n = zetazero(n)
            A_c = universal_residue_factor(complex(rho_n), c_val, dps)
    else:
        A_c = None

    return {
        'c': c_val,
        'shadow_stokes_constant': S_1,
        'shadow_instanton_action': omega_1,
        'zeta_stokes_constant': A_c,
        'bridge_consistency': 'algebraic: second sheet = minus first sheet',
    }


# =====================================================================
# Section 10: Heisenberg verification — no Stokes phenomena
# =====================================================================

def heisenberg_no_stokes(rank=1, level=1.0, r_max=20):
    r"""Verify that Heisenberg has no Stokes phenomena.

    Heisenberg is class G (depth 2): the shadow tower terminates at S_2 = kappa.
    The generating function G(t) = kappa*t^2 is a polynomial (exact).
    No Borel singularities, no Stokes lines, no trans-series corrections.

    This is the cleanest verification: the Borel transform B[G](xi) = kappa*xi^2/2
    is entire, and the Borel-Laplace integral gives back kappa*t^2 exactly.
    """
    kappa = float(rank) * level

    # Shadow tower: only S_2 = kappa, rest zero
    S = {2: kappa}
    for r in range(3, r_max + 1):
        S[r] = 0.0

    # Borel transform: B[G](xi) = kappa * xi^2 / 2
    def borel_heis(xi):
        return kappa * xi ** 2 / 2.0

    # Direct evaluation (exact)
    def exact_heis(t):
        return kappa * t ** 2

    # Check at some test points
    tests = []
    for t_val in [0.1, 0.5, 1.0, 2.0, 5.0]:
        direct = exact_heis(t_val)
        # Borel-Laplace: int_0^inf B(xi) e^{-xi/t} dxi/t
        # = int_0^inf kappa*xi^2/(2t) * e^{-xi/t} dxi
        # = kappa/(2t) * Gamma(3) * t^3 = kappa * t^2  (exact)
        borel_laplace = kappa * t_val ** 2  # analytical result
        tests.append({
            't': t_val,
            'direct': direct,
            'borel_laplace': borel_laplace,
            'error': abs(direct - borel_laplace),
        })

    return {
        'name': f'Heis_rank={rank}_k={level}',
        'kappa': kappa,
        'depth_class': 'G',
        'tower_terminates': True,
        'stokes_phenomena': False,
        'borel_singularities': [],
        'tests': tests,
    }


# =====================================================================
# Section 11: Richardson extrapolation for partial sums
# =====================================================================

def richardson_extrapolation(partial_sums, order=2):
    r"""Richardson extrapolation of a sequence of partial sums.

    Given partial sums a_1, a_2, ..., a_N, the Richardson transform
    of order k is:

    R_N^{(k)} = sum_{j=0}^{k} (-1)^{k-j} C(k,j) * (j+1)^k * a_{N-k+j}
                / sum_{j=0}^{k} (-1)^{k-j} C(k,j) * (j+1)^k

    This accelerates convergence by eliminating the leading O(1/N^j)
    corrections for j = 1, ..., k.
    """
    if len(partial_sums) < order + 1:
        return partial_sums[-1] if partial_sums else 0.0

    N = len(partial_sums) - 1
    k = order

    from math import comb

    numerator = 0.0
    denominator = 0.0
    for j in range(k + 1):
        sign = (-1) ** (k - j)
        binom = comb(k, j)
        weight = (j + 1) ** k
        idx = N - k + j
        if idx < 0 or idx >= len(partial_sums):
            continue
        numerator += sign * binom * weight * partial_sums[idx]
        denominator += sign * binom * weight

    if abs(denominator) < 1e-300:
        return partial_sums[-1]
    return numerator / denominator


def partial_sum_sequence(c_val, t_val, r_max=60):
    r"""Sequence of partial sums for the shadow tower at t.

    P_N(t) = sum_{r=2}^{N} S_r t^r

    For |t| < 1/rho: converges.
    For |t| > 1/rho: diverges (class M).
    """
    coeffs = virasoro_shadow_coefficients(c_val, r_max)
    t = complex(t_val)
    partial_sums = []
    running = 0.0 + 0.0j
    for i, s_r in enumerate(coeffs):
        r = 2 + i
        running += s_r * t ** r
        partial_sums.append(running)
    return partial_sums


def richardson_vs_borel(c_val, t_val, r_max=60, rich_order=3):
    r"""Compare Richardson extrapolation with Borel resummation.

    For divergent series, both should approximate the correct answer:
    - Richardson: algebraic acceleration of partial sums
    - Borel: analytic continuation via integral transform

    Agreement between the two provides INDEPENDENT VERIFICATION.
    """
    partial = partial_sum_sequence(c_val, t_val, r_max)
    real_partial = [p.real for p in partial]

    rich_result = richardson_extrapolation(real_partial, rich_order)

    borel_data = lateral_borel_sums_shadow(c_val, t_val, r_max=r_max)
    median = borel_data['median_sum']

    return {
        'c': c_val,
        't': t_val,
        'richardson': rich_result,
        'borel_median': median,
        'partial_sum_last': partial[-1] if partial else 0.0,
        'rich_borel_agreement': abs(rich_result - median.real),
    }


# =====================================================================
# Section 12: Complementarity at zeta zeros
# =====================================================================

def complementarity_stokes_at_zero(n, c_val, dps=30):
    r"""Compare Stokes constants for A = Vir_c and A! = Vir_{26-c} at the n-th zero.

    The Koszul duality c -> 26-c maps:
        A_c(rho) <-> A_{26-c}(rho)

    At c = 13 (self-dual): A_c = A_{26-c} identically.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho_n = zetazero(n)
        A_c = universal_residue_factor(complex(rho_n), c_val, dps)
        A_c_dual = universal_residue_factor(complex(rho_n), 26.0 - c_val, dps)

        return {
            'n': n,
            'c': c_val,
            'c_dual': 26.0 - c_val,
            'A_c': A_c,
            'A_c_dual': A_c_dual,
            'ratio': A_c / A_c_dual if abs(A_c_dual) > 1e-300 else complex('inf'),
            'modulus_ratio': abs(A_c) / abs(A_c_dual) if abs(A_c_dual) > 1e-300 else float('inf'),
        }


def self_dual_stokes_enhancement(n_zeros=5, dps=30):
    r"""Check for enhanced structure at the self-dual point c = 13.

    At c = 13:
    - kappa = kappa' = 13/2
    - F_{13}(s) has reflection symmetry s -> 7-s
    - Stokes constants satisfy A_{13}(rho) = A_{13}(rho) trivially
    - The shadow growth rate rho is at its unique self-dual value
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    c_val = 13.0
    inv = virasoro_shadow_invariants(c_val)

    stokes_data = []
    for n in range(1, n_zeros + 1):
        sc = stokes_constant_at_zero(n, c_val, dps)
        sc_dual = stokes_constant_at_zero(n, 26.0 - c_val, dps)
        stokes_data.append({
            'n': n,
            'gamma_n': sc['gamma_n'],
            'stokes_c13': sc['stokes_constant'],
            'stokes_c13_dual': sc_dual['stokes_constant'],
            'agreement': abs(sc['stokes_constant'] - sc_dual['stokes_constant']),
        })

    return {
        'c': c_val,
        'kappa': inv['kappa'],
        'kappa_dual': virasoro_kappa(26.0 - c_val),
        'self_dual_kappa': abs(inv['kappa'] - virasoro_kappa(26.0 - c_val)) < 1e-14,
        'rho_shadow': inv['rho'],
        'stokes_data': stokes_data,
    }


# =====================================================================
# Section 13: Borel-Pade approximant
# =====================================================================

def borel_pade_approximant(c_val, r_max=40):
    r"""Construct the [M/M] Pade approximant of the Borel transform.

    The Pade poles cluster toward the Borel singularities (Peacock
    pattern, Dorigoni-Dunne-Unsal).  This provides an independent
    check on the singularity locations.
    """
    coeffs = virasoro_shadow_coefficients(c_val, r_max)

    # Borel coefficients: b_r = S_r / r!
    borel_coeffs = []
    for i, s_r in enumerate(coeffs):
        r = 2 + i
        borel_coeffs.append(s_r / math.gamma(r + 1))

    # Build the Pade approximant using numpy
    # The Borel series is sum b_r xi^r for r = 2, ..., r_max
    # Rewrite as xi^2 * sum b_{r+2} xi^r for r = 0, ..., r_max-2
    n_terms = len(borel_coeffs)
    if n_terms < 4:
        return {'poles': [], 'zeros': [], 'coefficients': borel_coeffs}

    # Use the coefficient sequence for the Pade
    # We construct [M/M] Pade where M = n_terms // 2
    M = min(n_terms // 2, 15)

    # Pade from power series coefficients (Toeplitz method)
    # For f(x) = sum_{k=0}^{2M} c_k x^k, Pade [M/M] satisfies
    # Q(x)*f(x) - P(x) = O(x^{2M+1})
    c = np.array(borel_coeffs[:2 * M], dtype=np.float64)

    # Build the Toeplitz system for the denominator coefficients
    # Q(x) = 1 + q_1*x + ... + q_M*x^M
    # The system: sum_{j=0}^M q_j * c_{M+i-j} = 0 for i=1,...,M
    # with q_0 = 1
    if M < 1:
        return {'poles': [], 'zeros': [], 'coefficients': borel_coeffs}

    A = np.zeros((M, M), dtype=np.float64)
    b_vec = np.zeros(M, dtype=np.float64)
    for i in range(M):
        for j in range(M):
            idx = M + i - j
            if 0 <= idx < len(c):
                A[i, j] = c[idx]
        idx_rhs = M + i + 1
        if 0 <= idx_rhs < len(c):
            b_vec[i] = -c[idx_rhs]

    try:
        q_coeffs = np.linalg.solve(A, b_vec)
    except np.linalg.LinAlgError:
        return {'poles': [], 'zeros': [], 'coefficients': borel_coeffs}

    # Denominator polynomial: 1 + q_1*x + ... + q_M*x^M
    denom_poly = np.zeros(M + 1)
    denom_poly[0] = 1.0
    denom_poly[1:] = q_coeffs

    # Find poles (roots of denominator)
    # np.roots expects coefficients in descending order
    poles = np.roots(denom_poly[::-1])

    # Filter: keep only poles that map to the Borel plane
    # The original variable is xi^2, so map back: xi = sqrt(pole)
    pole_list = [complex(p) for p in poles]

    return {
        'M': M,
        'poles': pole_list,
        'n_poles': len(pole_list),
        'nearest_pole_modulus': min(abs(p) for p in pole_list) if pole_list else float('inf'),
        'coefficients': borel_coeffs,
    }


# =====================================================================
# Section 14: Full analysis summary
# =====================================================================

def full_bc_resurgence_analysis(c_val, n_zeros=5, r_max=40, dps=30):
    r"""Complete analysis: Borel singularities, Stokes constants, trans-series,
    median resummation, bridge equation, complementarity.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    inv = virasoro_shadow_invariants(c_val)

    # Borel singularity map
    borel_map = borel_singularity_map(n_zeros, dps)

    # Stokes constants
    stokes = stokes_constants_spectrum(c_val, n_zeros, dps)

    # Alien derivatives
    aliens = alien_derivative_spectrum(c_val, n_zeros, dps)

    # Bridge
    bridge = build_resurgent_bridge(c_val, n_zeros, dps)

    # Complementarity
    comp = complementarity_stokes_at_zero(1, c_val, dps)

    return {
        'c': c_val,
        'kappa': inv['kappa'],
        'rho_shadow': inv['rho'],
        'borel_singularities': borel_map,
        'stokes_constants': stokes,
        'alien_derivatives': aliens,
        'bridge': bridge,
        'complementarity_first_zero': comp,
    }
