r"""Finite diagnostics for Benjamin-Chang scattering poles and shadow data.

The constrained Epstein zeta function epsilon^c_s(A) satisfies the
functional equation

    epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}

with scattering factor

    F_c(s) = Gamma(s)*Gamma(s+c/2-1)*zeta(2s)
             / (pi^{2s-1/2}*Gamma(c/2-s)*Gamma(s-1/2)*zeta(2s-1)).

The denominator zeta(2s-1) gives uncompleted-factor poles at
s = (1+rho_n)/2.  This module evaluates those pole locations and residue
factors, and compares them with the Virasoro scalar shadow tower.  It does
not certify analytic continuation of spectral data off the real line, a
nonperturbative completion, an all-genus partition theorem, or a
reconstruction of zeta zeros from finite shadow data.

Certified scalar facts in this file are limited to the local scalar lane:
kappa(Vir_c)=c/2, S_3=2, S_4=10/[c(5c+22)], Delta=40/(5c+22), the
Virasoro branch-root rho formula, and Heisenberg kappa=rank*level with a
terminating depth-2 tower.  Bernoulli/A-hat genus coefficients are exact
facts in the genus engines and manuscript surfaces, not consequences of the
finite Borel or zeta-zero diagnostics here.

Object firewall:
    A, B(A), A^i, A^!, and Z_ch^der(A) are distinct.  Omega(B(A))=A is
    bar-cobar inversion.  A^! is the Verdier/continuous linear dual branch.
    Z_ch^der(A) is the Hochschild bulk.

Kernel constants, sourced from chapters/examples/landscape_census.tex:
    affine raw collision residue: k*Omega_tr/z
    KZ normalization: Omega/((k+h^vee)z)
    Heisenberg: k/z
    Virasoro: (c/2)/z^3 + 2T/z

Manuscript references:
    eq:constrained-epstein-fe (arithmetic_shadows.tex)
    def:universal-residue-factor (arithmetic_shadows.tex)
    rem:structural-obstruction (arithmetic_shadows.tex)
    rem:shadow-riemann-independence (arithmetic_shadows.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    cor:virasoro-shadow-radius (higher_genus_modular_koszul.tex)
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

STATUS_EXACT_SCALAR = "exact_scalar_fact"
STATUS_FINITE_WINDOW = "finite_window_diagnostic"
STATUS_BOREL_DIAGNOSTIC = "borel_transform_diagnostic"
STATUS_ZETA_EVIDENCE = "zeta_zero_evidence"
STATUS_CONDITIONAL_ANALYTIC = "conditional_analytic_hypothesis"
STATUS_NON_CERTIFIED = "non_certified_diagnostic"

PROHIBITED_PROMOTION_STATUSES = frozenset({
    "proved_nonperturbative_completion",
    "certified_analytic_continuation",
    "all_genus_shadow_partition_theorem",
    "zeta_zero_reconstruction",
    "koszul_duality_from_scalar_data",
})

CONDITIONAL_ANALYTIC_HYPOTHESES = (
    "Borel summability in the requested sector",
    "admissible contour avoiding singular directions",
    "analytic continuation of spectral coefficients off the real line",
    "Stokes constants matched to a proved alien-calculus model",
)

KERNEL_CONSTANTS = {
    "affine_raw_collision": "k*Omega_tr/z",
    "affine_KZ": "Omega/((k+h^vee)z)",
    "heisenberg": "k/z",
    "virasoro": "(c/2)/z^3 + 2T/z",
}

OBJECT_FIREWALLS = {
    "distinct_objects": ("A", "B(A)", "A^i", "A^!", "Z_ch^der(A)"),
    "bar_cobar": "Omega(B(A))=A is bar-cobar inversion",
    "koszul_dual": "A^! is the Verdier/continuous-linear dual branch",
    "bulk": "Z_ch^der(A) is the Hochschild bulk",
}


def diagnostic_scope() -> Dict[str, Any]:
    """Return the certification boundaries enforced by this engine."""
    return {
        "exact_scalar_facts": {
            "virasoro_kappa": "kappa(Vir_c)=c/2",
            "virasoro_S3": "S_3=2",
            "virasoro_S4": "S_4=10/[c(5c+22)]",
            "virasoro_Delta": "Delta=40/(5c+22)",
            "heisenberg_kappa": "kappa(H_k^{rank})=rank*level",
        },
        "exact_genus_facts_not_computed_here": (
            "Bernoulli/A-hat scalar genus coefficients",
        ),
        "finite_window_diagnostics": (
            "truncated shadow coefficients through r_max",
            "finite quadrature of a truncated Borel-Laplace integral",
            "finite Pade poles from a finite coefficient list",
        ),
        "borel_transform_diagnostics": (
            "finite-window Borel transform values",
            "lateral-sum numerical comparison",
            "median average of two finite lateral quadratures",
        ),
        "zeta_zero_evidence": (
            "omega_n=1/s_n for s_n=(1+rho_n)/2",
            "A_c(rho_n)=Res_{s=s_n} F_c(s) in the uncompleted factor",
        ),
        "conditional_analytic_hypotheses": CONDITIONAL_ANALYTIC_HYPOTHESES,
        "prohibited_promotions": tuple(sorted(PROHIBITED_PROMOTION_STATUSES)),
        "object_firewalls": OBJECT_FIREWALLS,
        "kernel_constants": KERNEL_CONSTANTS,
    }


# =====================================================================
# Section 0: Virasoro shadow invariants (self-contained)
# =====================================================================

def virasoro_kappa(c_val: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c_val / 2.0


def virasoro_shadow_invariants(c_val: float) -> Dict[str, Any]:
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
        'certification_status': STATUS_EXACT_SCALAR,
        'source': 'chapters/examples/landscape_census.tex',
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
    r"""Diagnostic Borel-plane location from the n-th zeta zero.

    The scattering factor F_c(s) has poles at s_n = (1+rho_n)/2.
    In the formal 1/s Borel coordinate used here, the corresponding
    location is zeta_n = 2/(1+rho_n) = 1/s_n.

    Under RH: rho_n = 1/2 + i*gamma_n, so
    s_n = 3/4 + i*gamma_n/2 and zeta_n = 2/(3/2 + i*gamma_n).

    This is evidence for where the uncompleted scattering factor places
    singular data.  It is not a reconstruction of zeta zeros from the
    finite shadow tower.
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
            'diagnostic_status': STATUS_ZETA_EVIDENCE,
            'certifies_zeta_zero_reconstruction': False,
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
    r"""Residue diagnostic S_n = Res_{s=s_n} F_c(s).

    This is the residue of the scattering factor at the pole s_n = (1+rho_n)/2.
    The residue equals the universal residue factor A_c(rho_n).

    Interpreting this residue as a Stokes constant for a completed
    alien-calculus model is conditional on additional analytic data.
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
            'diagnostic_status': STATUS_ZETA_EVIDENCE,
            'certifies_alien_calculus': False,
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
    r"""Measure the finite-window decay of |S_n| as a function of gamma_n.

    From Stirling's approximation of the Gamma factors in A_c(rho),
    the leading decay is:
        |A_c(rho)| ~ |gamma_n|^{-(c-1)/2} * |zeta(1+rho_n)| / |zeta'(rho_n)|

    The returned list is a finite-window diagnostic; it is not a theorem
    about all zero ordinates.
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
# Section 4: Lateral Borel diagnostics of the shadow tower
# =====================================================================

def shadow_borel_transform(c_val, xi, r_max=60):
    r"""Finite Borel-transform diagnostic for the shadow tower.

    The returned value is
        sum_{2 <= r <= r_max} S_r xi^r / r!.

    The exact Borel transform of the algebraic Virasoro shadow series is
    expected to be entire from the proved exponential coefficient bound,
    but this routine evaluates only the finite truncation.
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
    r"""Finite lateral Borel-Laplace diagnostic along direction epsilon.

    S_epsilon[G](t) = int_0^{inf*e^{i*eps}} B[G](xi) e^{-xi/t} dxi/t

    The integral is truncated at xi_max and uses the finite Borel
    polynomial through r_max.
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
    r"""Both finite lateral diagnostics and their numerical difference."""
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
        'diagnostic_status': STATUS_BOREL_DIAGNOSTIC,
        'certifies_nonperturbative_completion': False,
        'analytic_continuation_certified': False,
        'conditional_hypotheses': CONDITIONAL_ANALYTIC_HYPOTHESES,
        'r_max': r_max,
        'n_quad': n_quad,
        'xi_max': xi_max,
    }


# =====================================================================
# Section 5: Alien derivatives at zeta-zero singularities
# =====================================================================

def alien_derivative_at_zeta_zero(n, c_val, dps=30):
    r"""Residue proxy at the singularity from the n-th zeta zero.

    In a completed resurgent model, an alien derivative would measure the
    discontinuity of the Borel resummation at omega_n.

    For a simple pole of F_c(s) at s_n = (1+rho_n)/2, the alien
    derivative coefficient would be proportional to the residue A_c(rho_n):

        Delta_{omega_n} epsilon^c = A_c(rho_n) * (shifted epsilon)

    This function returns only that residue coefficient and location.
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
            'diagnostic_status': STATUS_ZETA_EVIDENCE,
            'certifies_alien_calculus': False,
            'certifies_borel_discontinuity': False,
        }


def alien_derivative_spectrum(c_val, n_zeros=10, dps=30):
    """Finite list of residue proxies at zeta-zero singularities."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    return [alien_derivative_at_zeta_zero(n, c_val, dps)
            for n in range(1, n_zeros + 1)]


# =====================================================================
# Section 6: Finite scale comparison for shadow and zeta-zero data
# =====================================================================

@dataclass
class ResurgentBridgeData:
    """Finite comparison data for shadow and zeta-zero diagnostics."""
    c: float
    kappa: float
    rho_shadow: float        # shadow growth rate
    action_shadow: complex   # shadow instanton action A = 1/t_branch
    borel_sings_zeta: List[complex]   # Borel singularities from zeta zeros
    stokes_constants: List[complex]   # S_n = A_c(rho_n)
    gamma_values: List[float]         # imaginary parts of zeta zeros
    diagnostic_status: str = STATUS_FINITE_WINDOW
    certifies_zeta_zero_reconstruction: bool = False
    certifies_all_genus_partition_theorem: bool = False
    conditional_hypotheses: Tuple[str, ...] = field(
        default_factory=lambda: CONDITIONAL_ANALYTIC_HYPOTHESES
    )


def build_resurgent_bridge(c_val, n_zeros=10, dps=30):
    r"""Build finite comparison data between shadow and zeta-zero scales.

    The shadow tower has instanton action A_shadow = 1/t_branch (from Q_L).
    The Benjamin-Chang FE has singularities at omega_n = 2/(1+rho_n).

    The two lists live in different regimes:
    - Shadow tower: scalar arity expansion from sqrt(Q_L).
    - BC singularities: uncompleted scattering-factor residues.

    A theorem identifying these two regimes requires analytic
    continuation and spectral-coefficient hypotheses not supplied by
    finite scalar data.
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
    r"""Compare shadow branch-point scale with zeta-zero pole positions.

    The shadow instanton action |A_shadow| = rho_shadow sets the
    algebraic branch scale in the arity direction.
    The zeta-zero positions |omega_n| ~ 2/gamma_n set the spectral scale.
    """
    bridge = build_resurgent_bridge(c_val, n_zeros, dps)

    data = {
        'c': c_val,
        'shadow_action_modulus': abs(bridge.action_shadow),
        'shadow_rho': bridge.rho_shadow,
        'diagnostic_status': STATUS_FINITE_WINDOW,
        'certifies_zeta_zero_reconstruction': False,
        'certifies_all_genus_partition_theorem': False,
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
    r"""Finite trans-series ansatz data at the scalar self-dual point.

    At c = 13, kappa(Vir_c)=kappa(Vir_{26-c})=13/2 on the Verdier
    scalar Virasoro lane.  General Koszul-duality certification and
    Hochschild-bulk identification require separate data beyond this
    residue ansatz.

    The finite ansatz has the shape:
        epsilon^{13}_s ~ sum_{k>=0} sigma^k e^{-k*A/s} sum_n a_{k,n} s^{-n}

    The returned object records coefficients and residues only.
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
        'diagnostic_status': STATUS_FINITE_WINDOW,
        'certifies_nonperturbative_completion': False,
        'certifies_koszul_duality': False,
    }


def trans_series_evaluate_c13(s_val, sigma=1.0, n_perturbative=40,
                                n_instanton=2, dps=30):
    r"""Evaluate the finite c=13 ansatz at s = s_val.

    The perturbative sector is the shadow tower evaluated at t = 1/s.
    The extra terms are model corrections e^{-A*s} from branch points.
    The legacy key ``full`` denotes this ansatz value, not a certified
    nonperturbative completion.
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
            'diagnostic_status': STATUS_FINITE_WINDOW,
            'full_is_certified_completion': False,
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
        'diagnostic_status': STATUS_FINITE_WINDOW,
        'full_is_certified_completion': False,
    }


# =====================================================================
# Section 8: Median finite diagnostic
# =====================================================================

def median_resummation(c_val, t_val, epsilon=0.02, r_max=60,
                        n_quad=2000, xi_max=80.0):
    r"""Median of two finite lateral Borel diagnostics.

    S_med[G](t) = (S_+[G](t) + S_-[G](t)) / 2

    Agreement with a direct partial sum inside the algebraic convergence
    radius is a finite-window check.  Outside the radius this routine
    reports a numerical diagnostic, not a certified analytic continuation
    or nonperturbative completion.
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
        'diagnostic_status': STATUS_BOREL_DIAGNOSTIC,
        'agreement_status': STATUS_FINITE_WINDOW,
        'certifies_nonperturbative_completion': False,
        'analytic_continuation_certified': False,
        'conditional_hypotheses': CONDITIONAL_ANALYTIC_HYPOTHESES,
    }


def median_vs_direct_comparison(c_val, t_values, r_max=60):
    r"""Compare median diagnostics with partial sums at multiple points.

    For |t| < 1/rho the algebraic Taylor series converges.  For
    |t| > 1/rho the analytic continuation is supplied by the algebraic
    function sqrt(Q_L), not by the median diagnostic.
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
            'diagnostic_status': STATUS_BOREL_DIAGNOSTIC,
            'median_certified_outside_radius': False,
        })

    return {
        'c': c_val,
        'convergence_radius': convergence_radius,
        'rho': rho,
        'results': results,
        'radius_status': STATUS_EXACT_SCALAR,
        'outside_radius_status': STATUS_NON_CERTIFIED,
    }


# =====================================================================
# Section 9: Algebraic sheet and residue comparison
# =====================================================================

def bridge_equation_check(c_val, n=1, dps=30):
    r"""Check algebraic sheet data and the zeta-residue side by side.

    The MC equation D*Theta + (1/2)[Theta, Theta] = 0 constrains the
    shadow tower.  This routine does not prove that the zeta-zero
    residue is an alien derivative of that MC object.

    For the algebraic shadow sheet one can record the formal relation
        Delta_{omega_1} S_r = S_1 * S_r^{(1)}

    and, for sqrt(Q_L),
        S_r^{(1)} = -S_r^{(0)}  (second sheet = minus first sheet)

    The returned zeta residue remains a separate diagnostic.
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
        'diagnostic_status': STATUS_FINITE_WINDOW,
        'certifies_mc_bridge': False,
        'certifies_alien_calculus': False,
    }


# =====================================================================
# Section 10: Heisenberg exact lane
# =====================================================================

def heisenberg_no_stokes(rank=1, level=1.0, r_max=20):
    r"""Compute the exact depth-2 Heisenberg shadow lane.

    Heisenberg is class G (depth 2): the shadow tower terminates at S_2 = kappa.
    The generating function G(t) = kappa*t^2 is a polynomial (exact).
    No shadow Borel singularities or trans-series corrections occur on
    this scalar lane.
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
        'certification_status': STATUS_EXACT_SCALAR,
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
    For |t| > 1/rho: the Taylor series diverges on the class-M scalar
    lane; analytic continuation is supplied by sqrt(Q_L), not by this
    finite sequence.
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
    r"""Compare Richardson extrapolation with the Borel diagnostic.

    Agreement is only finite-window evidence.  It is not an independent
    proof of analytic continuation or a nonperturbative value.
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
        'diagnostic_status': STATUS_FINITE_WINDOW,
        'agreement_is_certification': False,
    }


# =====================================================================
# Section 12: Complementarity at zeta zeros
# =====================================================================

def complementarity_stokes_at_zero(n, c_val, dps=30):
    r"""Compare residue factors for Vir_c and Vir_{26-c} at one zero.

    On the Virasoro scalar Verdier lane one compares:
        A_c(rho) <-> A_{26-c}(rho)

    At c = 13: A_c = A_{26-c} tautologically.  Koszul duality and
    Hochschild-bulk identification require data beyond residue equality.
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
            'duality_status': 'verdier_scalar_partner_diagnostic',
            'certifies_koszul_duality': False,
            'certifies_bulk_identification': False,
        }


def self_dual_stokes_enhancement(n_zeros=5, dps=30):
    r"""Check finite residue agreement at the scalar point c = 13.

    At c = 13:
    - kappa = kappa' = 13/2
    - Stokes constants satisfy A_{13}(rho) = A_{13}(rho) tautologically
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
        'diagnostic_status': STATUS_ZETA_EVIDENCE,
        'certifies_koszul_duality': False,
    }


# =====================================================================
# Section 13: Borel-Pade approximant
# =====================================================================

def borel_pade_approximant(c_val, r_max=40):
    r"""Construct a finite [M/M] Pade approximant of the Borel transform.

    Pade poles from a finite coefficient list are numerical evidence
    only.  They do not certify singularity locations or analytic
    continuation.
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
        'diagnostic_status': STATUS_FINITE_WINDOW,
        'certifies_singularity_locations': False,
    }


# =====================================================================
# Section 14: Full analysis summary
# =====================================================================

def full_bc_resurgence_analysis(c_val, n_zeros=5, r_max=40, dps=30):
    r"""Collect finite diagnostics for the BC scattering and shadow surfaces.
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
        'diagnostic_scope': diagnostic_scope(),
        'certifies_nonperturbative_completion': False,
        'certifies_zeta_zero_reconstruction': False,
        'certifies_all_genus_partition_theorem': False,
    }
