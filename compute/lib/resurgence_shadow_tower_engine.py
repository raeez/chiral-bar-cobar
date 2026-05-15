r"""Scalar A-hat diagnostics for the shadow obstruction tower.

Certified scalar lane.  On the proved uniform-weight scalar lane,

    F_g(A) = kappa(A) * lambda_g^FP,
    lambda_g^FP = ((2**(2*g-1) - 1) / 2**(2*g-1)) * |B_{2g}| / (2g)!,
    sum_{g>=1} lambda_g^FP hbar^{2g} = (hbar/2)/sin(hbar/2) - 1.

Consequences certified by the local manuscript and compute surfaces:

* the scalar hbar-series has radius 2*pi;
* the scalar u = hbar^2 series has radius (2*pi)^2;
* the closed A-hat function has simple hbar-poles at hbar = 2*pi*n;
* the hbar-pole residue is (-1)^n * 2*pi*n;
* the u-plane residue is kappa * (-1)^n * 8*pi^2*n^2.

What is not certified here.  Scalar coefficients, finite Pade windows, and
finite arity-shadow windows do not by themselves prove Borel summability,
median resummation, a Stokes automorphism, alien derivatives, a unique
nonperturbative completion, or a Koszul-dual bulk sector.  Functions retaining
legacy names such as ``stokes_multiplier_n`` or ``median_borel_sum`` therefore
return formal diagnostics or analytic hypotheses, not promoted theorems.

Local formula anchors:
    chapters/theory/higher_genus_modular_koszul.tex:4253-4277
    chapters/examples/landscape_census.tex:134-185
    chapters/examples/landscape_census.tex:4984-5030
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    from scipy import integrate as scipy_integrate
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

# =====================================================================
# Constants and certification labels
# =====================================================================

PI = math.pi
TWO_PI = 2.0 * PI
TWO_PI_SQ = TWO_PI ** 2       # ~ 39.478
FOUR_PI_SQ = (2.0 * PI) ** 2  # same as TWO_PI_SQ = (2*pi)^2
SCALAR_HBAR_RADIUS = TWO_PI
SCALAR_U_RADIUS = FOUR_PI_SQ
SCALAR_FIRST_U_POLE = FOUR_PI_SQ
INSTANTON_ACTION = SCALAR_FIRST_U_POLE  # legacy formal name, not a certificate
BOREL_RADIUS = math.inf                 # scalar Borel transforms below are entire
BOREL_U_RADIUS = math.inf

CERTIFIED_SCALAR_AHAT = "certified_scalar_ahat_bernoulli"
FINITE_WINDOW_DIAGNOSTIC = "finite_window_diagnostic"
ARITY_RADIUS_DIAGNOSTIC = "arity_radius_diagnostic"
ANALYTIC_HYPOTHESIS = "analytic_resurgence_hypothesis_not_certified"

SCALAR_AHAT_SOURCE = "chapters/theory/higher_genus_modular_koszul.tex:4253-4277"
STANDARD_CONSTANTS_SOURCE = "chapters/examples/landscape_census.tex:134-185"
FP_COEFFICIENT_SOURCE = "chapters/examples/landscape_census.tex:4984-5030"

# Bernoulli numbers (precomputed for speed, using standard convention B_1 = -1/2)
_BERNOULLI_CACHE: Dict[int, float] = {}


def _bernoulli_number(n: int) -> float:
    """Bernoulli number B_n with caching."""
    if n in _BERNOULLI_CACHE:
        return _BERNOULLI_CACHE[n]
    try:
        import mpmath
        val = float(mpmath.bernoulli(n))
    except ImportError:
        from sympy import bernoulli as sym_bernoulli
        val = float(sym_bernoulli(n))
    _BERNOULLI_CACHE[n] = val
    return val


# =====================================================================
# Section 0: Algebra data and fundamental invariants
# =====================================================================

def certification_report() -> Dict[str, Any]:
    """Certification boundaries for this scalar diagnostic engine."""
    return {
        'exact_scalar_ahat_coefficients': True,
        'scalar_hbar_radius_certified': SCALAR_HBAR_RADIUS,
        'scalar_u_radius_certified': SCALAR_U_RADIUS,
        'borel_transform_radius_certified': BOREL_RADIUS,
        'borel_summability_certified': False,
        'median_resummation_certified': False,
        'stokes_automorphism_certified': False,
        'alien_derivatives_certified': False,
        'nonperturbative_completion_certified': False,
        'unique_continuation_from_finite_data_certified': False,
        'exact_sources': (
            SCALAR_AHAT_SOURCE,
            STANDARD_CONSTANTS_SOURCE,
            FP_COEFFICIENT_SOURCE,
        ),
    }


def object_firewall() -> Dict[str, str]:
    """Canonical separation of algebra, bar, Verdier dual, and bulk objects."""
    return {
        'A': 'algebra',
        'B(A)': 'bar coalgebra T^c(s^{-1} Abar)',
        'Omega(B(A))': 'bar-cobar inversion of A, not Koszul duality',
        'A^i': 'bar cohomology coalgebra H^* B(A)',
        'A^!': 'Verdier/continuous-linear dual algebra branch',
        'Z_ch^der(A)': 'Hochschild derived centre/bulk, not Koszul dual',
    }


def kernel_constant_firewall() -> Dict[str, str]:
    """Kernel normalizations from the local standard-family constants."""
    return {
        'source': STANDARD_CONSTANTS_SOURCE,
        'heisenberg_collision': 'k/z',
        'affine_raw_trace_form': 'k*Omega_tr/z',
        'affine_kz': 'Omega/((k+h^vee)z), Omega=2*h^vee*Omega_tr',
        'virasoro_collision': '(c/2)/z^3 + 2T/z',
    }


def kappa_virasoro(c: float) -> float:
    """kappa(Vir_c) = c/2."""
    return c / 2.0


def kappa_heisenberg(k: float = 1.0, rank: int = 1) -> float:
    """kappa(H_k) = k for rank-1 Heisenberg at level k."""
    return float(rank) * float(k)


def kappa_affine_sl2(k: float) -> float:
    """kappa for affine sl_2 at level k: dim(g)*(k+h^v)/(2*h^v) = 3*(k+2)/4."""
    return 3.0 * (k + 2.0) / 4.0


def lambda_fp(g: int) -> float:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        return 0.0
    try:
        import mpmath
        B2g = abs(mpmath.bernoulli(2 * g))
        prefac = (mpmath.mpf(2) ** (2 * g - 1) - 1) / mpmath.mpf(2) ** (2 * g - 1)
        return float(prefac * B2g / mpmath.factorial(2 * g))
    except ImportError:
        B2g = abs(_bernoulli_number(2 * g))
        prefac = (2 ** (2 * g - 1) - 1) / (2 ** (2 * g - 1))
        return prefac * B2g / math.factorial(2 * g)


def F_g_scalar(kappa: float, g: int) -> float:
    """Genus-g scalar free energy: F_g(A) = kappa(A) * lambda_g^FP."""
    return kappa * lambda_fp(g)


# =====================================================================
# Section 1: Borel transform of the genus expansion
# =====================================================================

def borel_transform_genus(kappa: float, t: complex,
                          g_max: int = 100) -> complex:
    r"""Diagnostic Borel transform of the scalar genus series.

    B(t) = sum_{g>=1} F_g * t^{2g-1} / (2g-1)!

    where F_g = kappa * lambda_g^FP.

    The scalar coefficients already decay geometrically:
    lambda_g^FP = 2*eta(2g)/(2*pi)^{2g}.  Dividing by Gamma(2g)
    makes this diagnostic transform entire.  The finite scalar radius
    2*pi belongs to the original A-hat hbar-series, not to this Borel
    transform.

    Parameters
    ----------
    kappa : float
        Modular characteristic kappa(A).
    t : complex
        Borel-plane variable.
    g_max : int
        Maximum genus for summation.

    Returns
    -------
    complex
        B(t) evaluated at the given point.
    """
    t = complex(t)
    result = 0.0 + 0.0j
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_2g = math.gamma(2 * g)  # Gamma(2g) = (2g-1)!
        term = Fg * t ** (2 * g - 1) / gamma_2g
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_transform_u_plane(kappa: float, xi: complex,
                            g_max: int = 100) -> complex:
    r"""Diagnostic Borel transform in the u = hbar^2 variable.

    B_u(xi) = sum_{g>=1} F_g * xi^{g-1} / (g-1)!

    This transform is entire for the certified scalar A-hat series.  The
    points xi = (2*pi*n)^2 are the poles of the closed scalar u-function,
    not certified Borel singularities of this transform.
    """
    xi = complex(xi)
    result = 0.0 + 0.0j
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_g = math.gamma(g)  # (g-1)!
        term = Fg * xi ** (g - 1) / gamma_g
        result += term
        if g > 5 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_coefficients(kappa: float, g_max: int = 50
                       ) -> List[Dict[str, float]]:
    r"""Borel transform coefficients b_g = F_g / (2g-1)!.

    Returns list of {g, F_g, borel_coeff, power} dicts.
    """
    coeffs = []
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        gamma_2g = math.gamma(2 * g)
        bg = Fg / gamma_2g
        coeffs.append({
            'g': g,
            'F_g': Fg,
            'borel_coeff': bg,
            'power': 2 * g - 1,
        })
    return coeffs


# =====================================================================
# Section 2: Singularity structure of B(t)
# =====================================================================

@dataclass
class BorelSingularity:
    """Legacy name for an exact A-hat pole datum."""
    n: int                # index (n = 1, 2, 3, ...)
    location_hbar: complex  # location in hbar-plane
    location_u: float       # location in u = hbar^2 plane
    instanton_action: float  # legacy name for the scalar u-pole A_n
    singularity_type: str   # 'simple_pole'
    residue: float          # residue at the pole
    certification: str = CERTIFIED_SCALAR_AHAT
    borel_singularity_certified: bool = False


def borel_singularity_locations(n_max: int = 5) -> List[BorelSingularity]:
    r"""Exact pole structure of the scalar A-hat closed form.

    The closed form Z^sh = kappa * ((hbar/2)/sin(hbar/2) - 1) has
    simple poles at hbar = 2*pi*n for n = +/-1, +/-2, ...

    In the u = hbar^2 plane: singularities at u = (2*pi*n)^2.

    Residue of (hbar/2)/sin(hbar/2) at hbar = 2*pi*n:
    Near hbar = 2*pi*n: sin(hbar/2) = sin(pi*n + (hbar-2*pi*n)/2)
                       = (-1)^n * sin((hbar-2*pi*n)/2)
                       ~ (-1)^n * (hbar-2*pi*n)/2.
    So (hbar/2)/sin(hbar/2) ~ pi*n / ((-1)^n * (hbar-2*pi*n)/2)
                             = (-1)^n * 2*pi*n / (hbar-2*pi*n).
    Residue = (-1)^n * 2*pi*n.  The legacy function name does not certify
    a singularity of the diagnostic Borel transforms above.
    """
    sings = []
    for n in range(1, n_max + 1):
        location_hbar = 2.0 * PI * n
        sings.append(BorelSingularity(
            n=n,
            location_hbar=location_hbar,
            location_u=location_hbar ** 2,
            instanton_action=(TWO_PI * n) ** 2,
            singularity_type='simple_pole',
            residue=(-1) ** n * TWO_PI * n,
        ))
    return sings


def nearest_borel_singularity() -> BorelSingularity:
    """Nearest exact scalar A-hat pole, retained under a legacy name."""
    return borel_singularity_locations(1)[0]


def verify_borel_radius_from_coefficients(kappa: float, g_max: int = 50
                                          ) -> Dict[str, Any]:
    r"""Verify the scalar A-hat radius from coefficient ratios.

    The diagnostic Borel coefficients b_g = F_g / (2g-1)! make B(t)
    entire.  The finite radius recovered here is the radius of the
    original scalar A-hat series in u = hbar^2:

        |F_{g+1}/F_g| -> 1/(4*pi^2).

    Convergence radius in u: R_u = (2*pi)^2.
    Convergence radius in hbar: R_hbar = 2*pi.
    """
    ratios = []
    prev = None
    for g in range(1, g_max + 1):
        Fg = abs(F_g_scalar(kappa, g))
        if prev is not None and prev > 1e-100:
            ratios.append(Fg / prev)
        prev = Fg

    predicted_ratio = 1.0 / FOUR_PI_SQ
    last_5 = ratios[-5:] if len(ratios) >= 5 else ratios

    return {
        'predicted_u_radius': SCALAR_U_RADIUS,
        'predicted_hbar_radius': SCALAR_HBAR_RADIUS,
        'borel_transform_radius': BOREL_RADIUS,
        'predicted_ratio': predicted_ratio,
        'actual_ratios_last_5': last_5,
        'converged': (len(last_5) >= 3 and
                      abs(last_5[-1] - predicted_ratio) / predicted_ratio < 0.05),
        'certification': CERTIFIED_SCALAR_AHAT,
        'borel_summability_certified': False,
        'analytic_continuation_from_finite_data_certified': False,
    }


# =====================================================================
# Section 3: Formal residue multipliers
# =====================================================================

def stokes_multiplier_n(kappa: float, n: int) -> complex:
    r"""Formal residue multiplier at the n-th scalar A-hat pole.

    From the residue of (hbar/2)/sin(hbar/2) at hbar = 2*pi*n:
        Res = (-1)^n * 2*pi*n.

    Under an additional analytic-resurgence hypothesis one may package
    the residue in the hbar-plane convention:
        S_n = 2*pi*i * kappa * Res = 2*pi*i * kappa * (-1)^n * 2*pi*n
            = (-1)^n * 4*pi^2*n * kappa * i.

    This function returns that formal multiplier.  It does not certify a
    Stokes automorphism or a Borel singularity.
    """
    return kappa * (-1) ** n * FOUR_PI_SQ * n * 1.0j


def stokes_multiplier_leading(kappa: float) -> complex:
    r"""Formal leading residue multiplier S_1 = -4*pi^2*kappa*i."""
    return stokes_multiplier_n(kappa, 1)


def stokes_discontinuity_u_plane(kappa: float, u: complex,
                                 n_inst: int = 3) -> complex:
    r"""Formal Stokes-discontinuity ansatz in the u = hbar^2 plane.

    Disc(Z)(u) = S_+ Z(u) - S_- Z(u) = sum_{n>=1} S_n * exp(-A_n/u) * Z^{(n)}(u)

    At leading formal one-pole order:
        Disc ~ S_1 * exp(-A/u) * Z^{(1)}(u)

    where A = (2*pi)^2 and Z^{(1)} is a hypothesized one-pole
    fluctuation.  The scalar A-hat coefficients do not certify this
    discontinuity.
    """
    u = complex(u)
    if abs(u) < 1e-15:
        return 0.0 + 0.0j

    result = 0.0 + 0.0j
    for n in range(1, n_inst + 1):
        A_n = FOUR_PI_SQ * n ** 2
        S_n = stokes_multiplier_n(kappa, n)
        exp_factor = cmath.exp(-A_n / u)
        result += S_n * exp_factor
    return result


# =====================================================================
# Section 4: Alien derivatives
# =====================================================================

def alien_derivative_perturbative(kappa: float, n: int = 1) -> complex:
    r"""Formal alien-derivative value under an analytic hypothesis.

    Delta_{A_n} F^{(0)} = S_n * F^{(n)}

    where S_n is the formal residue multiplier and F^{(n)} is the
    hypothesized n-pole sector.

    This engine does not construct Ecalle alien derivations.  The return
    value is the formal residue multiplier used for diagnostics.
    """
    return stokes_multiplier_n(kappa, n)


def alien_derivative_chain(kappa: float, max_level: int = 4
                           ) -> List[Dict[str, Any]]:
    r"""Formal chain of iterated alien derivatives.

    Delta_{A_1}^0 F^{(0)} = F^{(0)}  (identity)
    Delta_{A_1}^1 F^{(0)} = S_1 * F^{(1)}
    Delta_{A_1}^2 F^{(0)} = S_1^2 * F^{(2)}  (for simple resurgent structure)

    The factorization Delta^k = S_1^k is recorded as an analytic
    resurgence hypothesis, not as a certified consequence of scalar
    coefficients.
    """
    S_1 = stokes_multiplier_leading(kappa)
    chain = []
    for k in range(max_level + 1):
        chain.append({
            'level': k,
            'alien_derivative': S_1 ** k,
            'instanton_weight': cmath.exp(-k * FOUR_PI_SQ),  # legacy key at u = 1
            'certification': ANALYTIC_HYPOTHESIS,
            'alien_derivative_certified': False,
            'interpretation': (
                'perturbative' if k == 0 else
                f'{k}-pole formal sector'
            ),
        })
    return chain


def verify_alien_derivative_resurgence(kappa: float, g_max: int = 30
                                       ) -> Dict[str, Any]:
    r"""Compare exact scalar coefficients with their leading pole asymptotic.

    The large-order relation for the u-plane series:
        F_g ~ sum_{n>=1} (-R_n / u_n^{g+1})

    where R_n = (-1)^n * 8*pi^2*n^2*kappa is the residue of Z(u) at u_n = (2*pi*n)^2.

    From the leading (n=1) contribution:
        F_g ~ 2*kappa / (2*pi)^{2g}

    The ratio F_g / (2*kappa / (2*pi)^{2g}) approaches 1.  This is an
    asymptotic statement about the exact A-hat pole expansion, not a
    verification of alien derivatives.
    """
    ratios = []
    for g in range(1, g_max + 1):
        Fg = F_g_scalar(kappa, g)
        predicted = 2.0 * kappa / TWO_PI ** (2 * g)
        if abs(predicted) > 1e-100:
            ratios.append(Fg / predicted)

    return {
        'kappa': kappa,
        'ratios': ratios,
        'ratio_at_g10': ratios[9] if len(ratios) >= 10 else None,
        'ratio_at_g20': ratios[19] if len(ratios) >= 20 else None,
        'approaching_1': (len(ratios) >= 15 and
                          abs(ratios[-1] - 1.0) < abs(ratios[5] - 1.0)),
        'certification': CERTIFIED_SCALAR_AHAT,
        'alien_derivative_certified': False,
    }


# =====================================================================
# Section 5: Trans-series
# =====================================================================

@dataclass
class TransseriesData:
    """Formal trans-series ansatz for the scalar diagnostic.

    Z^full(hbar) = sum_{n>=0} sigma^n * exp(-n*A/hbar^2) * Z^{(n)}(hbar)

    where:
        A = (2*pi)^2 is the first scalar u-plane A-hat pole
        Z^{(0)} is the perturbative series (shadow genus expansion)
        Z^{(n)} is a hypothesized n-pole fluctuation sector
        sigma is the formal residue multiplier
    """
    kappa: float
    instanton_action: float          # legacy key: first scalar u-pole
    perturbative: List[float]        # F_g^{(0)} for g = 1, 2, ...
    one_instanton: List[float]       # F_g^{(1)} for g = 1, 2, ...
    two_instanton: List[float]       # F_g^{(2)} for g = 1, 2, ...
    sigma: complex                   # trans-series parameter
    certification: str = ANALYTIC_HYPOTHESIS
    completion_certified: bool = False


def one_instanton_coefficients(kappa: float, g_max: int = 30) -> List[float]:
    r"""Formal one-pole fluctuation coefficients F_g^{(1)}.

    From the pole structure of (hbar/2)/sin(hbar/2) at hbar = 2*pi,
    the first formal sector records the n=1 pole contribution.

    Using the dispersion relation / large-order structure:
        F_g^{(1)} = (-1)^{g+1} * 2*kappa / (2*pi)^{2g}

    This matches the leading Bernoulli asymptotic of F_g.  It does not
    certify a nonperturbative sector.
    """
    coeffs = []
    for g in range(1, g_max + 1):
        fg1 = (-1) ** (g + 1) * 2.0 * kappa / TWO_PI ** (2 * g)
        coeffs.append(fg1)
    return coeffs


def two_instanton_coefficients(kappa: float, g_max: int = 30) -> List[float]:
    r"""Formal two-pole fluctuation coefficients F_g^{(2)}.

    From the n=2 pole at hbar = 4*pi:
        F_g^{(2)} = (-1)^g * 2*kappa / (4*pi)^{2g}
    """
    coeffs = []
    for g in range(1, g_max + 1):
        fg2 = (-1) ** g * 2.0 * kappa / (2.0 * TWO_PI) ** (2 * g)
        coeffs.append(fg2)
    return coeffs


def build_transseries(kappa: float, g_max: int = 30) -> TransseriesData:
    """Build formal trans-series diagnostic data."""
    pert = [F_g_scalar(kappa, g) for g in range(1, g_max + 1)]
    inst1 = one_instanton_coefficients(kappa, g_max)
    inst2 = two_instanton_coefficients(kappa, g_max)
    sigma = stokes_multiplier_leading(kappa)

    return TransseriesData(
        kappa=kappa,
        instanton_action=INSTANTON_ACTION,
        perturbative=pert,
        one_instanton=inst1,
        two_instanton=inst2,
        sigma=sigma,
    )


def transseries_evaluate(ts: TransseriesData, hbar: complex,
                         n_inst: int = 2) -> complex:
    r"""Evaluate the formal trans-series ansatz at hbar.

    Z^full(hbar) = Z^{(0)}(hbar)
                   + sigma * exp(-A/hbar^2) * Z^{(1)}(hbar)
                   + sigma^2/2 * exp(-2A/hbar^2) * Z^{(2)}(hbar) + ...
    """
    hbar = complex(hbar)
    if abs(hbar) < 1e-15:
        return 0.0 + 0.0j

    u = hbar ** 2

    # Perturbative sector
    Z0 = sum(ts.perturbative[g - 1] * hbar ** (2 * g)
             for g in range(1, len(ts.perturbative) + 1))

    result = Z0

    if n_inst >= 1 and ts.one_instanton:
        A = ts.instanton_action
        Z1 = sum(ts.one_instanton[g - 1] * hbar ** (2 * g)
                 for g in range(1, len(ts.one_instanton) + 1))
        result += ts.sigma * cmath.exp(-A / u) * Z1

    if n_inst >= 2 and ts.two_instanton:
        A2 = 4.0 * ts.instanton_action  # (2*2*pi)^2 = 4*(2*pi)^2
        Z2 = sum(ts.two_instanton[g - 1] * hbar ** (2 * g)
                 for g in range(1, len(ts.two_instanton) + 1))
        result += ts.sigma ** 2 / 2.0 * cmath.exp(-A2 / u) * Z2

    return result


# =====================================================================
# Section 6: Formal one-pole correction
# =====================================================================

def one_instanton_correction(kappa: float, hbar: float, g_max: int = 30
                             ) -> Dict[str, Any]:
    r"""Formal one-pole correction to the scalar series.

    F^{(1)}(hbar) = sum_{g>=1} F_g^{(1)} * hbar^{2g}

    weighted by exp(-A/hbar^2) where A = (2*pi)^2.

    The diagnostic exponential is small for small hbar.  The scalar A-hat
    computation alone does not certify an instanton sector.
    """
    inst1_coeffs = one_instanton_coefficients(kappa, g_max)
    Z1 = sum(inst1_coeffs[g - 1] * hbar ** (2 * g)
             for g in range(1, len(inst1_coeffs) + 1))

    u = hbar ** 2
    exp_supp = math.exp(-INSTANTON_ACTION / u) if u > 1e-15 else 0.0

    S_1 = stokes_multiplier_leading(kappa)

    return {
        'kappa': kappa,
        'hbar': hbar,
        'instanton_action': INSTANTON_ACTION,
        'exp_suppression': exp_supp,
        'Z1_perturbative': Z1,
        'one_instanton_contrib': S_1 * exp_supp * Z1,
        'certification': ANALYTIC_HYPOTHESIS,
        'nonperturbative_sector_certified': False,
        'relative_to_perturbative': (
            abs(S_1 * exp_supp * Z1) / abs(sum(
                F_g_scalar(kappa, g) * hbar ** (2 * g)
                for g in range(1, g_max + 1)
            )) if abs(sum(F_g_scalar(kappa, g) * hbar ** (2 * g)
                         for g in range(1, g_max + 1))) > 1e-100 else 0.0
        ),
    }


# =====================================================================
# Section 7: Median resummation
# =====================================================================

def ahat_generating_function(hbar: float) -> float:
    r"""Ahat(i*hbar) = (hbar/2)/sin(hbar/2).

    The exact generating function of the shadow genus expansion.
    Simple poles at hbar = 2*pi*n for n = +/-1, +/-2, ...
    """
    if abs(hbar) < 1e-15:
        return 1.0
    return (hbar / 2.0) / math.sin(hbar / 2.0)


def genus_series_closed_form(kappa: float, hbar: float) -> float:
    r"""Exact scalar closed form: Z^sh = kappa*((hbar/2)/sin(hbar/2)-1)."""
    return kappa * (ahat_generating_function(hbar) - 1.0)


def genus_series_partial_sum(kappa: float, hbar: float,
                             g_max: int = 50) -> float:
    r"""Partial sum of the genus series: sum_{g=1}^{g_max} F_g * hbar^{2g}."""
    total = 0.0
    for g in range(1, g_max + 1):
        total += F_g_scalar(kappa, g) * hbar ** (2 * g)
    return total


def lateral_borel_sum(kappa: float, hbar: complex,
                      epsilon: float = 0.02,
                      g_max: int = 80,
                      n_quad: int = 2000,
                      xi_max: float = 50.0) -> complex:
    r"""Numerical lateral-Borel diagnostic for the genus series.

    Working in the u = hbar^2 plane:
        S_epsilon[Z](u) = int_0^{infty * e^{i*epsilon}} B_u(xi) e^{-xi/u} dxi/u

    epsilon > 0: S_+ (above the real axis)
    epsilon < 0: S_- (below the real axis)

    This quadrature does not certify Borel summability or a Stokes jump.
    """
    u = complex(hbar) ** 2
    if abs(u) < 1e-15:
        return 0.0 + 0.0j

    direction = cmath.exp(1j * epsilon)
    ds = xi_max / n_quad
    result = 0.0 + 0.0j

    for k in range(1, n_quad + 1):
        s = (k - 0.5) * ds
        xi = s * direction
        B_val = borel_transform_u_plane(kappa, xi, g_max)
        weight = cmath.exp(-xi / u) * direction / u
        result += B_val * weight * ds

    return result


def median_borel_sum(kappa: float, hbar: float,
                     epsilon: float = 0.02,
                     g_max: int = 80,
                     n_quad: int = 2000,
                     xi_max: float = 50.0) -> Dict[str, Any]:
    r"""Median-style numerical diagnostic for the scalar series.

    F^med(hbar) = (S_+(hbar) + S_-(hbar)) / 2

    The returned value is a finite quadrature diagnostic.  It is not a
    certificate of median resummation, Stokes ambiguity cancellation, or
    unique nonperturbative completion.  The exact scalar comparison, when
    present, comes from the A-hat closed form.
    """
    hbar_c = complex(hbar)

    S_plus = lateral_borel_sum(kappa, hbar_c, +epsilon, g_max, n_quad, xi_max)
    S_minus = lateral_borel_sum(kappa, hbar_c, -epsilon, g_max, n_quad, xi_max)
    median = (S_plus + S_minus) / 2.0

    # Comparison values
    partial = genus_series_partial_sum(kappa, hbar, g_max)
    exact = None
    if abs(hbar) < TWO_PI - 0.01:
        exact = genus_series_closed_form(kappa, hbar)

    return {
        'kappa': kappa,
        'hbar': hbar,
        'median_sum': median.real,
        'S_plus': S_plus,
        'S_minus': S_minus,
        'stokes_jump': S_plus - S_minus,
        'partial_sum': partial,
        'exact': exact,
        'median_vs_exact': abs(median.real - exact) if exact is not None else None,
        'certification': FINITE_WINDOW_DIAGNOSTIC,
        'median_resummation_certified': False,
        'unique_analytic_continuation_certified': False,
    }


# =====================================================================
# Section 8: Finite-window Pade diagnostics
# =====================================================================

def pade_approximant_genus(kappa: float, hbar: float,
                           g_max: int = 20) -> float:
    r"""Pade [N/N] approximant of the genus series in u = hbar^2.

    Constructs the diagonal Pade approximant of
        Z(u) = sum_{g>=1} F_g u^g
    and evaluates at u = hbar^2.

    The Pade approximant is a finite-window probe of the A-hat pole
    structure.  It does not certify analytic continuation; the exact
    meromorphic continuation is supplied only by the closed A-hat formula.
    """
    # Coefficients of Z(u) = c_0 + c_1*u + c_2*u^2 + ...
    # c_0 = 0, c_g = F_g for g >= 1
    coeffs = [0.0]
    for g in range(1, g_max + 1):
        coeffs.append(F_g_scalar(kappa, g))

    n_coeffs = len(coeffs)
    N = (n_coeffs - 1) // 2
    if N < 1:
        return genus_series_partial_sum(kappa, hbar, g_max)

    u = hbar ** 2

    # Solve for Pade denominator q_1, ..., q_N
    mat = np.zeros((N, N))
    rhs = np.zeros(N)
    for i in range(N):
        for j in range(N):
            idx = N + 1 + i - (j + 1)
            if 0 <= idx < len(coeffs):
                mat[i, j] = coeffs[idx]
        idx_r = N + 1 + i
        if 0 <= idx_r < len(coeffs):
            rhs[i] = -coeffs[idx_r]

    try:
        q_vec = np.linalg.solve(mat, rhs)
    except np.linalg.LinAlgError:
        return genus_series_partial_sum(kappa, hbar, g_max)

    Q_coeffs = np.concatenate(([1.0], q_vec))

    # Numerator p_0, ..., p_N
    P_coeffs = np.zeros(N + 1)
    for k in range(N + 1):
        for j in range(min(k, N) + 1):
            if k - j < len(coeffs):
                P_coeffs[k] += Q_coeffs[j] * coeffs[k - j]

    # Evaluate P(u)/Q(u)
    P_val = sum(P_coeffs[k] * u ** k for k in range(len(P_coeffs)))
    Q_val = sum(Q_coeffs[k] * u ** k for k in range(len(Q_coeffs)))

    if abs(Q_val) < 1e-100:
        return genus_series_partial_sum(kappa, hbar, g_max)

    result = P_val / Q_val
    return float(result.real) if isinstance(result, complex) else float(result)


def pade_poles_genus(kappa: float, g_max: int = 20) -> np.ndarray:
    r"""Find poles of the Pade approximant in the u = hbar^2 plane.

    These approximate the scalar A-hat poles at u = (2*pi*n)^2.
    The nearest pole should converge to (2*pi)^2 ~ 39.48.
    """
    coeffs = [0.0]
    for g in range(1, g_max + 1):
        coeffs.append(F_g_scalar(kappa, g))

    n_coeffs = len(coeffs)
    N = (n_coeffs - 1) // 2
    if N < 1:
        return np.array([])

    mat = np.zeros((N, N))
    rhs = np.zeros(N)
    for i in range(N):
        for j in range(N):
            idx = N + 1 + i - (j + 1)
            if 0 <= idx < len(coeffs):
                mat[i, j] = coeffs[idx]
        idx_r = N + 1 + i
        if 0 <= idx_r < len(coeffs):
            rhs[i] = -coeffs[idx_r]

    try:
        q_vec = np.linalg.solve(mat, rhs)
    except np.linalg.LinAlgError:
        return np.array([])

    # Poles = roots of Q(u) = 1 + q_1*u + ... + q_N*u^N
    poly_coeffs = list(reversed([1.0] + list(q_vec)))
    return np.roots(poly_coeffs)


def borel_pade_virasoro(c_val: float, g_max: int = 20) -> Dict[str, Any]:
    r"""Finite-window Pade analysis for Virasoro at central charge c.

    Computes:
    1. Pade poles (should converge to (2*pi*n)^2)
    2. Pade values at several hbar values vs exact
    3. Quality of approximation

    This is diagnostic data, not a proof of Borel summability or analytic
    continuation from finite coefficients.
    """
    kappa = kappa_virasoro(c_val)
    poles = pade_poles_genus(kappa, g_max)

    # Filter real positive poles (physical)
    real_pos_poles = sorted([p.real for p in poles
                            if abs(p.imag) < abs(p.real) * 0.1 and p.real > 0])

    # Nearest pole should approximate (2*pi)^2
    nearest_pole = real_pos_poles[0] if real_pos_poles else None
    pole_error = abs(nearest_pole - FOUR_PI_SQ) / FOUR_PI_SQ if nearest_pole else None

    # Compare Pade vs exact at several hbar values
    comparisons = []
    for hbar in [0.5, 1.0, 2.0, 3.0, 5.0]:
        pade_val = pade_approximant_genus(kappa, hbar, g_max)
        exact_val = genus_series_closed_form(kappa, hbar) if hbar < TWO_PI - 0.01 else None
        partial_val = genus_series_partial_sum(kappa, hbar, g_max)
        comparisons.append({
            'hbar': hbar,
            'pade': pade_val,
            'exact': exact_val,
            'partial': partial_val,
            'pade_error': abs(pade_val - exact_val) / abs(exact_val) if exact_val and abs(exact_val) > 1e-15 else None,
        })

    return {
        'c': c_val,
        'kappa': kappa,
        'g_max': g_max,
        'poles': poles,
        'real_positive_poles': real_pos_poles,
        'nearest_pole': nearest_pole,
        'nearest_pole_error': pole_error,
        'expected_nearest': FOUR_PI_SQ,
        'comparisons': comparisons,
        'certification': FINITE_WINDOW_DIAGNOSTIC,
        'analytic_continuation_certified': False,
        'borel_summability_certified': False,
    }


# =====================================================================
# Section 9: Bridge equation and MC equation connection
# =====================================================================

def bridge_equation_arity_r(kappa: float, r: int) -> Dict[str, Any]:
    r"""Finite-arity bridge-equation diagnostic.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 projected to arity r
    gives a constraint on the shadow coefficient S_r.

    A full Ecalle bridge equation would relate an alien derivative of
    Theta_r to a Stokes automorphism:
        Delta_{A_1} Theta^{(0)}_r = S_1 * Theta^{(1)}_r

    At arity 2: Theta_2 = kappa = c/2, exact, so Delta kappa = 0.
    At arity 3: alpha = 2, exact, so Delta alpha = 0.
    At arity 4: S_4 = 10/(c(5c+22)), c-dependent.

    This function records the finite shadow data and the formal bridge
    shape.  It does not certify alien derivatives or Stokes automorphisms.
    """
    S_1 = stokes_multiplier_leading(kappa)

    if r == 2:
        return {
            'arity': 2,
            'shadow_coeff': kappa,
            'alien_derivative': 0.0,
            'bridge_satisfied': None,
            'finite_shadow_exact': True,
            'analytic_bridge_certified': False,
            'interpretation': 'kappa is exact on the scalar shadow lane',
        }
    elif r == 3:
        return {
            'arity': 3,
            'shadow_coeff': 2.0,  # alpha = 2 for Virasoro
            'alien_derivative': 0.0,
            'bridge_satisfied': None,
            'finite_shadow_exact': True,
            'analytic_bridge_certified': False,
            'interpretation': 'cubic shadow is exact on the Virasoro lane',
        }
    else:
        return {
            'arity': r,
            'shadow_coeff': 'S_' + str(r),
            'alien_derivative': 'S_1 * S_' + str(r) + '^{(1)}',
            'bridge_satisfied': None,
            'finite_shadow_exact': False,
            'analytic_bridge_certified': False,
            'interpretation': (
                f'bridge equation at arity {r} is a formal analytic '
                f'hypothesis beyond the finite scalar data'
            ),
        }


def bridge_equation_mc_consistency(kappa: float) -> Dict[str, Any]:
    r"""Record the MC-to-bridge hypothesis boundary.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 implies:
    1. D^2 = 0 at all levels
    2. A bridge theorem would require an alien derivative Delta commuting
       with D in the chosen analytic category
    3. Under that extra hypothesis, if Theta satisfies MC, then the trans-series
       Theta^full = Theta^{(0)} + sigma*e^{-A/hbar^2}*Theta^{(1)} + ...
       also satisfies MC, provided the Theta^{(n)} satisfy the
       LINEARIZED MC equation around Theta^{(0)}.

    The scalar engine does not supply the analytic category or Delta.
    """
    S_1 = stokes_multiplier_leading(kappa)

    return {
        'kappa': kappa,
        'S_1': S_1,
        'instanton_action': INSTANTON_ACTION,
        'mc_equation': 'D*Theta + (1/2)[Theta,Theta] = 0',
        'bridge_equation': 'Delta_{A} Theta = S_1 * Theta^{(1)}',
        'analytic_bridge_certified': False,
        'certification': ANALYTIC_HYPOTHESIS,
        'consistency_proof': None,
        'diagnostic_note': (
            'The MC equation is exact in its lane.  Alien derivatives, '
            'Stokes automorphisms, and trans-series MC lifts require an '
            'additional analytic resurgence theorem not supplied here.'
        ),
        'arity_2_bridge': bridge_equation_arity_r(kappa, 2),
        'arity_3_bridge': bridge_equation_arity_r(kappa, 3),
        'arity_4_bridge': bridge_equation_arity_r(kappa, 4),
    }


# =====================================================================
# Section 10: Resurgent structure of Q^contact and higher shadows
# =====================================================================

def virasoro_shadow_invariants(c_val: float) -> Dict[str, float]:
    r"""Fundamental shadow invariants for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)),
    Delta = 40/(5c+22), rho, theta from branch points of Q_L.
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4  # = 40/(5c+22)

    # Shadow metric coefficients Q_L(t) = q0 + q1*t + q2*t^2
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    # Branch points (zeros of Q_L)
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


def arity_shadow_coefficients_recursive(c_val: float, r_max: int = 30
                                        ) -> List[float]:
    r"""Virasoro shadow coefficients S_2, ..., S_{r_max} via f^2 = Q_L.

    The shadow generating function H(t) = t^2 * sqrt(Q_L(t)) gives
    S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(t)).
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


def arity_borel_transform(c_val: float, xi: complex, r_max: int = 60
                          ) -> complex:
    r"""Finite-window Borel diagnostic for the arity-direction shadow series.

    B^arity(xi) = sum_{r>=2} S_r * xi^r / r!

    This is the arity-direction Borel transform, complementary to the
    genus-direction transform in Section 1.

    For the quadratic Q_L model, geometric coefficient growth would make
    the factorially normalized transform entire.  A finite window does not
    certify this analytic statement.
    """
    coeffs = arity_shadow_coefficients_recursive(c_val, r_max)
    xi = complex(xi)
    result = 0.0 + 0.0j
    for i, s_r in enumerate(coeffs):
        r = 2 + i
        term = s_r * xi ** r / math.gamma(r + 1)
        result += term
        if i > 10 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def qcontact_resurgence(c_val: float) -> Dict[str, Any]:
    r"""Arity-radius diagnostic for Q^contact_Vir = 10/(c(5c+22)).

    Q^contact is the quartic shadow coefficient (arity 4).  Its c-dependence
    has poles at c = 0 and c = -22/5.

    The arity expansion G(t) = sum S_r t^r has branch points at the zeros
    of the quadratic shadow metric model
    Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    For Virasoro: Delta = 40/(5c+22) > 0 for c > 0, so Q_L is irreducible
    (class M) and the shadow tower has infinite depth.  The radius, Borel,
    and Stokes fields returned here are diagnostics or hypotheses unless an
    all-arity analytic theorem is supplied separately.
    """
    inv = virasoro_shadow_invariants(c_val)
    kappa = inv['kappa']
    S4 = inv['S4']
    Delta = inv['Delta']
    rho = inv['rho']

    # Arity convergence radius
    R_arity = 1.0 / rho if rho > 0 else float('inf')

    arity_borel_entire_diagnostic = True
    S_1_arity_hypothesis = 2.0j * PI

    return {
        'c': c_val,
        'Q_contact': S4,
        'Delta': Delta,
        'shadow_depth': 'infinite' if Delta != 0 else 'finite',
        'rho': rho,
        'arity_convergence_radius': R_arity,
        'arity_radius_certification': ARITY_RADIUS_DIAGNOSTIC,
        'arity_radius_certified_from_finite_window': False,
        'arity_borel_entire': None,
        'arity_borel_entire_diagnostic': arity_borel_entire_diagnostic,
        'arity_borel_entire_certified': False,
        'arity_stokes_constant': None,
        'arity_stokes_constant_hypothesis': S_1_arity_hypothesis,
        'arity_stokes_constant_certified': False,
        'branch_points': (inv['branch_plus'], inv['branch_minus']),
        'depth_class': 'M' if Delta != 0 else 'G_or_L',
    }


def higher_shadow_resurgence(c_val: float, r_max: int = 20
                             ) -> Dict[str, Any]:
    r"""Asymptotic diagnostics for higher shadow coefficients S_r.

    For Virasoro, the leading asymptotics are:
        S_r ~ (2/r) * (-3)^{r-4} * (2/c)^{r-2}  for r >= 4.

    The growth rate rho = 6/|c| (at leading order in 1/c) gives the
    convergence radius R = |c|/6 of the shadow generating function.

    The growth rate from the quadratic shadow metric branch points gives
    model corrections to this leading-order formula.  Finite windows do not
    certify all-arity analytic continuation or resurgence.
    """
    coeffs = arity_shadow_coefficients_recursive(c_val, r_max)
    inv = virasoro_shadow_invariants(c_val)
    rho = inv['rho']

    # Check growth rate: |S_r|^{1/r} should approach rho
    growth_rates = []
    for i in range(len(coeffs)):
        r = i + 2
        s_r = abs(coeffs[i])
        if s_r > 1e-100 and r >= 4:
            growth_rates.append(s_r ** (1.0 / r))

    # Leading-order comparison: S_r vs (2/r)*(-3)^{r-4}*(2/c)^{r-2}
    leading_ratios = []
    for i in range(len(coeffs)):
        r = i + 2
        if r >= 4:
            leading = (2.0 / r) * (-3.0) ** (r - 4) * (2.0 / c_val) ** (r - 2)
            if abs(leading) > 1e-100:
                leading_ratios.append(coeffs[i] / leading)

    return {
        'c': c_val,
        'rho_exact': rho,
        'rho_leading': 6.0 / abs(c_val),
        'growth_rates': growth_rates[-5:] if growth_rates else [],
        'leading_ratios': leading_ratios[-5:] if leading_ratios else [],
        'r_max': r_max,
        'convergence_radius': 1.0 / rho if rho > 0 else float('inf'),
        'certification': ARITY_RADIUS_DIAGNOSTIC,
        'finite_window_only': True,
        'all_arity_resurgence_certified': False,
    }


# =====================================================================
# Section 11: Large-order relations
# =====================================================================

def large_order_prediction(kappa: float, g: int, n_inst: int = 3) -> float:
    r"""Finite-pole asymptotic estimate for F_g.

    Z(u) = kappa * ((sqrt(u)/2)/sin(sqrt(u)/2) - 1) has simple poles
    at u_n = (2*pi*n)^2 with residues R_n = (-1)^n * 8*pi^2*n^2*kappa.

    The contribution of the n-th A-hat pole to F_g is:
        -R_n / u_n^{g+1} = (-1)^{n+1} * 2*kappa / ((2*pi)^{2g} * n^{2g})

    Total: F_g ~ 2*kappa / (2*pi)^{2g} * sum_{n>=1} (-1)^{n+1} / n^{2g}
             = 2*kappa / (2*pi)^{2g} * (1 - 1/2^{2g} + 1/3^{2g} - ...)
             = 2*kappa / (2*pi)^{2g} * eta(2g)

    where eta is the Dirichlet eta function.  The finite ``n_inst`` cutoff
    is an asymptotic pole-window estimate, not instanton data.
    """
    result = 0.0
    for n in range(1, n_inst + 1):
        u_n = (TWO_PI * n) ** 2
        R_n = (-1) ** n * 8.0 * PI ** 2 * n ** 2 * kappa
        contrib = -R_n / u_n ** (g + 1)
        result += contrib
    return result


def large_order_verification(kappa: float, g_max: int = 20,
                             n_inst: int = 5) -> Dict[str, Any]:
    r"""Compare exact F_g with the finite-pole asymptotic estimate.

    Compare exact F_g (from Bernoulli numbers) with the large-order
    prediction from A-hat pole data.  For large g, the agreement improves
    as more poles are included.
    """
    results = []
    for g in range(1, g_max + 1):
        Fg_exact = F_g_scalar(kappa, g)
        Fg_predicted = large_order_prediction(kappa, g, n_inst)
        rel_err = (abs(Fg_exact - Fg_predicted) / abs(Fg_exact)
                   if abs(Fg_exact) > 1e-100 else 0.0)
        results.append({
            'g': g,
            'F_g_exact': Fg_exact,
            'F_g_predicted': Fg_predicted,
            'relative_error': rel_err,
        })

    return {
        'kappa': kappa,
        'n_instanton_sectors': n_inst,
        'results': results,
        'error_at_g5': results[4]['relative_error'] if len(results) >= 5 else None,
        'error_at_g15': results[14]['relative_error'] if len(results) >= 15 else None,
        'certification': CERTIFIED_SCALAR_AHAT,
        'nonperturbative_completion_certified': False,
    }


# =====================================================================
# Section 12: Verdier scalar complementarity diagnostic
# =====================================================================

def koszul_complementarity_np(c_val: float, hbar: float,
                              g_max: int = 30) -> Dict[str, Any]:
    r"""Verdier scalar complementarity diagnostic for Virasoro.

    For Virasoro at c: kappa = c/2, kappa' = (26-c)/2.

    The optional diagnostic combination:
        F^np = F^pert(A) + exp(-A/hbar^2) * F^pert(A!) + ...

    is not certified as a nonperturbative completion.  A, B(A), A^i,
    A^!, and Z_ch^der(A) remain distinct: Omega(B(A)) = A is bar-cobar
    inversion; A^! is the Verdier/continuous-linear dual branch; the
    Hochschild bulk is not Koszul dual.
    """
    kappa = kappa_virasoro(c_val)
    kappa_dual = kappa_virasoro(26.0 - c_val)  # Verdier scalar branch for Vir

    Fpert = genus_series_partial_sum(kappa, hbar, g_max) if abs(hbar) < TWO_PI else float('nan')
    Fpert_dual = genus_series_partial_sum(kappa_dual, hbar, g_max) if abs(hbar) < TWO_PI else float('nan')

    u = hbar ** 2
    exp_factor = math.exp(-INSTANTON_ACTION / u) if u > 1e-15 and INSTANTON_ACTION / u < 500 else 0.0

    F_np = Fpert + exp_factor * Fpert_dual if not (math.isnan(Fpert) or math.isnan(Fpert_dual)) else float('nan')

    exact = genus_series_closed_form(kappa, hbar) if abs(hbar) < TWO_PI - 0.01 else None

    is_self_dual = abs(c_val - 13.0) < 0.01

    return {
        'c': c_val,
        'kappa': kappa,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa + kappa_dual,
        'hbar': hbar,
        'F_pert': Fpert,
        'F_pert_dual': Fpert_dual,
        'exp_suppression': exp_factor,
        'F_np': F_np,
        'F_np_certification': FINITE_WINDOW_DIAGNOSTIC,
        'nonperturbative_completion_certified': False,
        'dual_branch': 'Verdier scalar branch A^!, not bar-cobar inversion and not Hochschild bulk',
        'object_firewall': object_firewall(),
        'exact': exact,
        'is_self_dual': is_self_dual,
    }


# =====================================================================
# Section 13: Gevrey analysis and optimal truncation
# =====================================================================

def gevrey_order(kappa: float, g_max: int = 30) -> Dict[str, Any]:
    r"""Determine the Gevrey order of the genus series.

    A series sum a_g u^g is Gevrey-s if |a_g| <= C * A^g * (g!)^s.

    For the shadow partition function:
        F_g ~ 2*kappa / (2*pi)^{2g}  (no factorial growth!)

    This means the scalar series is Gevrey-0: convergent within its
    A-hat radius.
    The (2g)! from the Bernoulli numbers is cancelled by the (2g)! in
    the denominator of lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!.

    This statement is only about the scalar shadow lane.  It does not make
    claims about a full Weil-Petersson genus expansion.

    The shadow partition function's Gevrey-0 nature is a CONSEQUENCE of
    the algebraic structure (Ahat generating function).
    """
    # Check growth: is |F_g| bounded by C * A^g (Gevrey-0)?
    ratios = []
    for g in range(2, g_max + 1):
        Fg = abs(F_g_scalar(kappa, g))
        Fg_prev = abs(F_g_scalar(kappa, g - 1))
        if Fg_prev > 1e-100:
            ratios.append(Fg / Fg_prev)

    # For Gevrey-0: ratios should approach a constant (= 1/A = 1/(4*pi^2))
    predicted = 1.0 / FOUR_PI_SQ

    # For Gevrey-1: ratios should grow like g
    # ratio_g / g should approach a constant
    gevrey1_test = [ratios[i] / (i + 2) for i in range(len(ratios))]

    return {
        'kappa': kappa,
        'gevrey_order': 0,
        'predicted_ratio': predicted,
        'actual_ratios_last_5': ratios[-5:] if ratios else [],
        'ratio_converges': (len(ratios) >= 5 and
                            abs(ratios[-1] - predicted) / predicted < 0.05),
        'gevrey1_test_last_5': gevrey1_test[-5:] if gevrey1_test else [],
        'interpretation': (
            'Gevrey-0: the shadow series is convergent within the radius '
            '|hbar| < 2*pi. The factorial growth of B_{2g} is exactly '
            'cancelled by the (2g)! in the FP denominator. The series '
            'therefore needs no Borel-summability certificate on this '
            'scalar lane.'
        ),
        'borel_summability_certified': False,
    }


def optimal_truncation(kappa: float, hbar: float) -> Dict[str, Any]:
    r"""Truncation diagnostic for the scalar genus series.

    For |hbar| < 2*pi the scalar A-hat series converges.  For
    |hbar| >= 2*pi this routine does not certify an optimal truncation
    theorem; it only returns the legacy geometric scale A/hbar^2 as a
    diagnostic.
    """
    u = hbar ** 2
    A = INSTANTON_ACTION
    N_star = int(A / u) if u > 0 else float('inf')

    # Compute partial sums at various truncation orders
    partials = []
    running_sum = 0.0
    for g in range(1, max(2 * N_star, 30) + 1):
        Fg = F_g_scalar(kappa, g)
        running_sum += Fg * hbar ** (2 * g)
        partials.append((g, running_sum))

    # Find the truncation that minimizes |partial - exact| (if exact available)
    exact = genus_series_closed_form(kappa, hbar) if abs(hbar) < TWO_PI - 0.01 else None

    best_g = None
    best_error = float('inf')
    if exact is not None:
        for g, s in partials:
            err = abs(s - exact)
            if err < best_error:
                best_error = err
                best_g = g

    return {
        'kappa': kappa,
        'hbar': hbar,
        'N_star_predicted': N_star,
        'N_star_actual': best_g,
        'instanton_action': A,
        'exp_suppression': math.exp(-A / u) if u > 0 and A / u < 500 else 0.0,
        'within_convergence': abs(hbar) < TWO_PI,
        'certified_optimal_truncation': False,
        'certification': FINITE_WINDOW_DIAGNOSTIC,
        'exact': exact,
        'partial_at_Nstar': (partials[N_star - 1][1]
                             if 0 < N_star <= len(partials) else None),
    }
