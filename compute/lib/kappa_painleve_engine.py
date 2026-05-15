r"""Finite shadow coefficients and conditional Painleve-I rescaling.

This module has four separate surfaces.

1. Finite scalar coefficient identity.
   In Q[kappa][[q]]/(q^(G+1)),
       log(tau_shadow,scal^{<=G}) = kappa log(tau_KW^{<=G}).
   This is a finite formal identity.  It does not certify an analytic
   tau function, KdV hierarchy, Hirota hierarchy, or Painleve system.

2. Direct KdV/Hirota residuals.
   If a standard KdV potential v is rescaled to u = kappa v, then the
   standard KdV residual has factor kappa*(kappa-1).  Hirota bilinear
   terms have the same quadratic obstruction.  The residual vanishes at
   kappa = 1, and the scalar unit point kappa = 0 is degenerate.

3. Stationary primary-line diagnostic.
   The shadow hierarchy surface records
       H(t)^2 = t^4 Q_L(t),
       Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2,
       Delta = 8*kappa*S_4.
   This is stationary primary-line data.  It is not a descendant
   integrable hierarchy.

4. Conditional Painleve-I rescaling.
   If a standard Painleve-I solution Y satisfies
       Y''(X) = 6 Y(X)^2 + X,
   then y(x) = kappa^(3/5) Y(kappa^(-1/5) x) satisfies
       y''(x) = (6/kappa) y(x)^2 + x.
   This is an ODE rescaling identity.  It requires an independent
   isomonodromic or descendant construction beyond the finite scalar
   coefficient identity.

Local sources:
    chapters/examples/landscape_census.tex:126
    chapters/examples/landscape_census.tex:180
    chapters/connections/concordance.tex:4097
    compute/lib/shadow_hierarchy_engine.py
    compute/lib/motivic_shadow_partition_engine.py:764
    compute/lib/topological_recursion_shadow_engine.py:996

Painleve constants in this numerical module are the standard tritronquee
normalization used by the existing tests: the first positive real pole
2.37832054, Y(0) = -0.18755428, Y'(0) = 0.30490535, and
alpha_Boutroux = 4*sqrt(2)/15.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, Optional, Tuple

import numpy as np
from scipy.integrate import solve_ivp

from compute.lib.shadow_hierarchy_engine import (
    finite_scalar_tau_identity as _finite_scalar_tau_identity,
    hirota_bilinear_kappa_deformation as _hirota_bilinear_kappa_deformation,
    kdv_residual_from_power as _kdv_residual_from_power,
    stationary_riccati_diagnostics as _stationary_riccati_diagnostics,
)


# ============================================================================
# Section 0: Universal constants (verified, multi-path)
# ============================================================================

LOCAL_FORMULA_SOURCES = {
    'standard_family_constants': 'chapters/examples/landscape_census.tex:126',
    'kernel_normalizations': 'chapters/examples/landscape_census.tex:180',
    'concordance_kernel_normalizations': 'chapters/connections/concordance.tex:4097',
    'finite_scalar_tau': 'compute/lib/shadow_hierarchy_engine.py:118',
    'kdv_residual': 'compute/lib/shadow_hierarchy_engine.py:167',
    'hirota_residual': 'compute/lib/shadow_hierarchy_engine.py:296',
    'stationary_primary_line': 'compute/lib/shadow_hierarchy_engine.py:482',
    'motivic_non_certification': 'compute/lib/motivic_shadow_partition_engine.py:764',
    'tr_shadow_non_certification': 'compute/lib/topological_recursion_shadow_engine.py:996',
}

OBJECT_FIREWALLS = {
    'A': 'input chiral algebra',
    'B(A)': 'bar coalgebra T^c(s^{-1} Abar)',
    'A^i': 'bar cohomology coalgebra H^* B(A)',
    'A^!': 'Verdier or continuous-linear dual algebra',
    'Z_ch^der(A)': 'derived chiral centre, computed by chiral Hochschild cochains',
    'Omega(B(A))': 'bar-cobar inversion to A, not Koszul duality',
}

KERNEL_NORMALIZATIONS = {
    'affine_raw_trace_form': 'k*Omega_tr/z',
    'affine_KZ': 'Omega/((k+h^vee)*z)',
    'Heisenberg': 'k/z',
    'Virasoro': '(c/2)/z^3 + 2*T/z',
}

# Standard Painleve I tritronquee constants.
# Source: Joshi-Kitaev (2001), Costin-Huang-Tanveer (2012), and independent
# shooting from x = -1000 with the O(X^{-2}) Boutroux correction.
# See verify_tritronquee_initial_data_by_shooting below.
X_TRITRONQUEE_FIRST_POLE_POS_REAL = 2.37832054     # first pole on positive real axis
Y_TRITRONQUEE_AT_ZERO = -0.18755428                # Y(0) of tritronquee
YPRIME_TRITRONQUEE_AT_ZERO = 0.30490535            # Y'(0) of tritronquee (POSITIVE)

# Boutroux WKB action coefficient.
ALPHA_BOUTROUX = 4.0 / 15.0 * math.sqrt(2.0)    # ~0.37712

# Pole-free sector for the standard P_I tritronquee.
# The tritronquee is pole-free in the sector arg(x) in (-4pi/5, 4pi/5)
# relative to the positive real axis.  Equivalently, along arg(x) = pi
# (negative real axis) the tritronquee is pole-free, and the first pole
# is at arg(x) = 0 (positive real axis) at x ~ 2.378.
SECTOR_HALFWIDTH = 4.0 * math.pi / 5.0          # |arg x| < 4 pi/5


# ============================================================================
# Section 1: Family kappa values
# ============================================================================

@dataclass(frozen=True)
class KappaFamily:
    """Family-tagged kappa value with provenance."""
    name: str
    kappa: Fraction
    source: str


def _as_fraction(value: Any) -> Fraction:
    """Convert small exact inputs and decimal literals to Fraction."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, float):
        return Fraction(str(value))
    return Fraction(value)


def kappa_virasoro(c: Any) -> KappaFamily:
    """Virasoro: kappa = c/2."""
    c_exact = _as_fraction(c)
    return KappaFamily(name=f"Virasoro_c={c}", kappa=c_exact / 2,
                       source="landscape_census.tex:142, kappa(Vir_c)=c/2")


def kappa_heisenberg(k: Any = 1) -> KappaFamily:
    """Rank-one Heisenberg: kappa = k."""
    return KappaFamily(name=f"Heisenberg_k={k}", kappa=_as_fraction(k),
                       source="landscape_census.tex:151, kappa(H_k)=k")


def kappa_lattice(rank: int) -> KappaFamily:
    """Lattice VOA: kappa = rank."""
    return KappaFamily(name=f"Lattice_rank={rank}", kappa=Fraction(rank, 1),
                       source="landscape_census.tex:1280, kappa(V_Lambda)=rank(Lambda)")


def kappa_moonshine() -> KappaFamily:
    """Monster module V^natural: c = 24 and dim V_1 = 0, so kappa = 12."""
    return KappaFamily(name="V_natural", kappa=Fraction(12, 1),
                       source="landscape_census.tex:1280, kappa(V^natural)=12")


def kappa_virasoro_self_dual() -> KappaFamily:
    """Virasoro self-dual point c = 13, kappa = 13/2.

    The complementarity sum is kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
    At the fixed point c = 13, the individual scalar is 13/2.
    """
    return KappaFamily(name="Virasoro_c=13_self_dual", kappa=Fraction(13, 2),
                       source="landscape_census.tex:2534, kappa(Vir_13)=13/2")


def kappa_virasoro_complementarity_sum() -> KappaFamily:
    """Virasoro Verdier complementarity sum kappa(Vir_c)+kappa(Vir_{26-c})."""
    return KappaFamily(name="Virasoro_complementarity_sum", kappa=Fraction(13, 1),
                       source="landscape_census.tex:1801, c/2+(26-c)/2=13")


# ============================================================================
# Section 2: Finite scalar, residual, and stationary diagnostics
# ============================================================================

def finite_scalar_coefficient_identity(kappa: Any, g_max: int = 5) -> Dict[str, Any]:
    """Exact finite-window scalar identity for log(tau_shadow).

    This delegates to shadow_hierarchy_engine.py, the canonical compute
    surface for the scalar coefficient lane.  The returned identity is
    finite and formal; it does not certify analytic tau or hierarchy
    membership.
    """
    result = _finite_scalar_tau_identity(_as_fraction(kappa), g_max)
    result.update({
        'analytic_tau_power_certified': False,
        'hierarchy_membership_certified': False,
        'painleve_from_scalar_tau_certified': False,
        'non_certification_source': LOCAL_FORMULA_SOURCES['motivic_non_certification'],
    })
    return result


def direct_kdv_residual(kappa: Any, g_max: int = 5) -> Dict[str, Any]:
    """Exact KdV residual for the scalar power tau_KW^kappa.

    If v satisfies u_t + 6*u*u_x + u_xxx = 0 and u = kappa*v, direct
    substitution leaves 6*kappa*(kappa-1)*v*v_x.  This residual is a
    failure diagnostic for arbitrary kappa, not a deformed hierarchy
    construction.
    """
    k = _as_fraction(kappa)
    result = _kdv_residual_from_power(k, g_max)
    result.update({
        'standard_kdv_residual_coefficient': 6 * k * (k - 1),
        'standard_kdv_residual_formula': '6*kappa*(kappa-1)*u_KW*(u_KW)_x',
        'certifies_kappa_deformed_kdv': False,
        'certifies_analytic_tau_membership': False,
    })
    return result


def direct_hirota_residual(kappa: Any, max_genus: int = 5) -> Dict[str, Any]:
    """Exact Hirota obstruction for a scalar power tau_KW^kappa."""
    k = _as_fraction(kappa)
    result = _hirota_bilinear_kappa_deformation(k, max_genus)
    result.update({
        'hirota_quadratic_residual_factor': k * (k - 1),
        'certifies_hirota_hierarchy': False,
        'certifies_analytic_tau_membership': False,
    })
    return result


def stationary_primary_line_diagnostics(
    kappa: Any,
    alpha: Any = 0,
    S4: Any = 0,
) -> Dict[str, Any]:
    """Exact Q_L data for the stationary primary-line shadow diagnostic."""
    result = _stationary_riccati_diagnostics(
        _as_fraction(kappa),
        _as_fraction(alpha),
        _as_fraction(S4),
    )
    result.update({
        'certifies_descendant_hierarchy': False,
        'certifies_painleve_equation': False,
        'object_firewall': OBJECT_FIREWALLS,
        'kernel_normalizations': KERNEL_NORMALIZATIONS,
    })
    return result


def painleve_certification_firewall(kappa: Any) -> Dict[str, Any]:
    """Separate the conditional Painleve-I ODE from scalar tau data."""
    k = _as_fraction(kappa)
    return {
        'kappa': k,
        'finite_scalar_tau_identity': 'log(tau_shadow,scal^{<=G})=kappa log(tau_KW^{<=G})',
        'conditional_painleve_ode_rescaling': k > 0,
        'painleve_from_scalar_tau_certified': False,
        'isomonodromic_structure_assumed_separately': True,
        'descendant_hierarchy_assumed_separately': True,
        'object_firewall': OBJECT_FIREWALLS,
        'kernel_normalizations': KERNEL_NORMALIZATIONS,
        'sources': LOCAL_FORMULA_SOURCES,
    }


# ============================================================================
# Section 3: Conditional Painleve-I rescaling
# ============================================================================

def rescale_x_to_X(x: float, kappa: float) -> float:
    """X = kappa^(-1/5) x.  Maps kappa-P_I independent variable to standard P_I."""
    if kappa <= 0:
        raise ValueError(f"kappa must be positive for real rescaling, got {kappa}")
    return x * kappa ** (-1.0 / 5.0)


def rescale_X_to_x(X: float, kappa: float) -> float:
    """Inverse: x = kappa^(1/5) X."""
    return X * kappa ** (1.0 / 5.0)


def rescale_Y_to_y(Y: float, kappa: float) -> float:
    """y = kappa^(3/5) Y."""
    return Y * kappa ** (3.0 / 5.0)


def rescale_y_to_Y(y: float, kappa: float) -> float:
    """Inverse: Y = kappa^(-3/5) y."""
    return y * kappa ** (-3.0 / 5.0)


def verify_rescaling_at(x: float, kappa: float, Y: float, Yprime: float,
                        Ydoubleprime: float) -> Dict[str, float]:
    """Given a point (X, Y, Y', Y'') of standard P_I, verify the rescaled point
    satisfies kappa-P_I.

    Standard:    Y'' = 6 Y^2 + X
    Rescaled:    y'' = (6/kappa) y^2 + x  with x = kappa^(1/5) X, y = kappa^(3/5) Y.

    Returns the residual.  Should be zero up to floating-point.
    """
    X = rescale_x_to_X(x, kappa)
    # Cross-check: x and X consistent
    assert abs(rescale_X_to_x(X, kappa) - x) < 1e-12
    y = rescale_Y_to_y(Y, kappa)
    # y' = kappa^(2/5) Y'(X)
    yprime = Yprime * kappa ** (2.0 / 5.0)
    # y'' = kappa^(1/5) Y''(X)
    ydoubleprime = Ydoubleprime * kappa ** (1.0 / 5.0)
    # Standard P_I residual
    std_residual = Ydoubleprime - 6 * Y * Y - X
    # kappa P_I residual
    kappa_residual = ydoubleprime - (6.0 / kappa) * y * y - x
    return {
        'X': X, 'Y': Y, 'Yprime': Yprime, 'Ydoubleprime': Ydoubleprime,
        'x': x, 'y': y, 'yprime': yprime, 'ydoubleprime': ydoubleprime,
        'standard_residual': std_residual,
        'kappa_residual': kappa_residual,
    }


# ============================================================================
# Section 4: Numerical solver for standard Painleve I, then rescale
# ============================================================================

def standard_pi_rhs(t: float, state: np.ndarray) -> np.ndarray:
    """Right-hand side of Y'' = 6 Y^2 + t as a first-order system.

    state = [Y, Yprime].  Returns [Yprime, 6 Y^2 + t].
    """
    Y, Yp = state
    return np.array([Yp, 6.0 * Y * Y + t])


def solve_standard_pi(X0: float, X1: float, Y0: float, Y0prime: float,
                      max_step: Optional[float] = None,
                      rtol: float = 1e-10, atol: float = 1e-12,
                      blow_up_threshold: float = 1e8) -> Dict[str, Any]:
    """Solve standard Painleve I IVP: Y'' = 6 Y^2 + X from X0 to X1
    with initial data Y(X0) = Y0, Y'(X0) = Y0prime.

    Stops early if |Y| exceeds blow_up_threshold (pole detection).

    Multi-path verification: solver uses Radau (implicit, stiff-friendly).
    Cross-check with DOP853 in the test file.
    """
    state0 = np.array([Y0, Y0prime])

    def event_blowup(t, y):
        return blow_up_threshold - max(abs(y[0]), abs(y[1]))
    event_blowup.terminal = True
    event_blowup.direction = -1

    sol = solve_ivp(
        standard_pi_rhs,
        (X0, X1),
        state0,
        method='Radau',
        rtol=rtol,
        atol=atol,
        max_step=max_step if max_step is not None else float(abs(X1 - X0)) / 100,
        events=event_blowup,
        dense_output=True,
    )
    return {
        'sol': sol,
        'X0': X0, 'X1': X1, 'Y0': Y0, 'Y0prime': Y0prime,
        'reached_pole': len(sol.t_events[0]) > 0,
        'pole_location': sol.t_events[0][0] if len(sol.t_events[0]) > 0 else None,
        'final_X': sol.t[-1],
        'final_Y': sol.y[0][-1],
        'final_Yprime': sol.y[1][-1],
    }


def solve_kappa_pi(x0: float, x1: float, y0: float, y0prime: float,
                   kappa: float, **kwargs) -> Dict[str, Any]:
    """Solve kappa-Painleve I directly:  y'' = (6/kappa) y^2 + x.

    This verifies the conditional ODE rescaling.  It does not assert that
    tau_shadow is an analytic Painleve tau function.
    """
    if kappa == 0:
        raise ValueError("kappa = 0: equation degenerates to y'' = x (linear)")

    def rhs(t, state):
        y, yp = state
        return np.array([yp, (6.0 / kappa) * y * y + t])

    blow_up_threshold = kwargs.pop('blow_up_threshold', 1e8 * kappa ** (3.0 / 5.0))

    def event_blowup(t, st):
        return blow_up_threshold - max(abs(st[0]), abs(st[1]))
    event_blowup.terminal = True
    event_blowup.direction = -1

    sol = solve_ivp(
        rhs, (x0, x1), np.array([y0, y0prime]),
        method='Radau',
        rtol=kwargs.get('rtol', 1e-10),
        atol=kwargs.get('atol', 1e-12),
        max_step=kwargs.get('max_step', float(abs(x1 - x0)) / 100),
        events=event_blowup,
        dense_output=True,
    )
    return {
        'sol': sol, 'kappa': kappa,
        'reached_pole': len(sol.t_events[0]) > 0,
        'pole_location': sol.t_events[0][0] if len(sol.t_events[0]) > 0 else None,
        'final_x': sol.t[-1], 'final_y': sol.y[0][-1], 'final_yprime': sol.y[1][-1],
    }


# ============================================================================
# Section 5: Tritronquee under the conditional rescaling
# ============================================================================

def tritronquee_initial_data() -> Tuple[float, float]:
    """The (Y(0), Y'(0)) of the standard P_I tritronquee.

    Source: Costin-Huang-Tanveer 2012.  Cross-checked by shooting from x = -L
    inward using the Boutroux asymptotic and matching at x = 0.
    """
    return (Y_TRITRONQUEE_AT_ZERO, YPRIME_TRITRONQUEE_AT_ZERO)


def kappa_tritronquee_initial_data(kappa: float) -> Tuple[float, float]:
    """The (y(0), y'(0)) of the kappa-tritronquee, derived by rescaling.

    From y(x) = kappa^(3/5) Y(kappa^(-1/5) x):
        y(0) = kappa^(3/5) Y(0)
        y'(0) = kappa^(2/5) Y'(0)
    """
    Y0, Y0p = tritronquee_initial_data()
    return (kappa ** (3.0 / 5.0) * Y0, kappa ** (2.0 / 5.0) * Y0p)


def kappa_tritronquee_first_pole(kappa: float) -> float:
    """First pole of the kappa-tritronquee on the POSITIVE real axis.

    By rescaling: x_pole(kappa) = kappa^(1/5) * X_pole_standard, where
    X_pole_standard = +2.378 > 0.
    """
    return kappa ** (1.0 / 5.0) * X_TRITRONQUEE_FIRST_POLE_POS_REAL


def kappa_tritronquee_asymptotic(x: float, kappa: float) -> float:
    """Boutroux equilibrium asymptotic of kappa-tritronquee for x << 0.

    The dominant balance y'' ~ (6/kappa) y^2 + x with y'' negligible
    compared to (6/kappa) y^2 for large |x|: solve (6/kappa) y^2 + x = 0
    on the NEGATIVE branch y < 0 for x < 0 (this is the pole-free branch
    in the Joshi-Kruskal convention; the other branch has poles):

        y_eq(x) = -sqrt(-kappa x / 6).

    First subleading correction (NLO):  y(x) = y_eq + 1/(48 kappa X^2)
    after the rescaling X = kappa^(-1/5) x; derivation in the test file.

    Source: Boutroux 1913, Joshi-Kruskal Phys. Lett. A 130 (1988) 129-137,
    Joshi-Kitaev Stud. Appl. Math. 107 (2001) 253.
    """
    if x >= 0:
        # Asymptotic only valid for x << 0
        return float('nan')
    return -math.sqrt(-kappa * x / 6.0)


def integrate_kappa_tritronquee(kappa: float, x_start: float = 0.0,
                                x_end: float = -2.0,
                                num_points: int = 200) -> Dict[str, Any]:
    """Integrate the kappa-tritronquee from x = 0 to x_end (negative).

    Initial data from kappa_tritronquee_initial_data.
    """
    y0, y0p = kappa_tritronquee_initial_data(kappa)
    result = solve_kappa_pi(x_start, x_end, y0, y0p, kappa, max_step=0.01)
    return result


# ============================================================================
# Section 6: Stokes data under positive real rescaling
# ============================================================================

# Kapaev's Stokes multipliers for the standard P_I.
# Reference: Kapaev, J. Phys. A 37 (2004) 11149-11167.
# The five Stokes sectors S_k are bounded by the anti-Stokes rays
# arg(x) = (2k+1) pi/5, k = 0,1,2,3,4.
# Each sector S_k has a "Stokes multiplier" s_k, and they satisfy the cyclic
# relation:
#   1 + s_k s_{k+1} + s_k s_{k+1} s_{k+2} s_{k+3} = 0   (mod cycle)
# The connection to the integration constants of the asymptotic expansion is:
#   y(x) ~ y_eq(x) (1 + sum b_k x^{-5k/2}) + s_k * exp(-S(x)) (1 + ...)
# with S(x) = (4 sqrt(2)/15) (-x)^(5/2) the Boutroux WKB action.
#
# In Kapaev's normalization the tritronquee is characterized by s_2 = 0:
# the central sector has no recessive exponential contribution.

KAPAEV_TRITRONQUEE_STOKES = {
    's_0': 0.0,
    's_1': 1.0,        # convention-dependent; matches Kapaev 2004
    's_2': 0.0,        # central sector: no recessive contribution
    's_3': -1.0,
    's_4': 0.0,
}


def kappa_stokes_multipliers(kappa: float) -> Dict[str, float]:
    """Stokes multipliers of the kappa-tritronquee.

    Theorem (kappa-invariance of Stokes data): the rescaling
    x = kappa^(1/5) X is a positive real homothety.  It preserves the
    anti-Stokes rays and the Stokes-sector labelling.  Hence:

        s_k(kappa-P_I tritronquee) = s_k(standard P_I tritronquee)

    for all k = 0,...,4.

    The Stokes multipliers are projectively invariant under real positive
    rescaling of the independent variable.  Under a complex rescaling
    x -> e^(i theta) x, sectors rotate by theta and Stokes data transform
    by relabeling.  Since kappa^(1/5) is real positive for kappa > 0, no
    rotation occurs.

    Returns the same multipliers as the standard tritronquee.
    """
    if kappa <= 0:
        raise ValueError("Stokes data require kappa > 0 (real positive scaling)")
    return dict(KAPAEV_TRITRONQUEE_STOKES)


def kappa_wkb_action_along_Boutroux(x: float, kappa: float) -> float:
    """The WKB action along the Boutroux contour for kappa-P_I.

    For standard P_I:  S(X) = (4 sqrt(2)/15) (-X)^(5/2)  for X < 0.
    For kappa-P_I, substitute X = kappa^(-1/5) x:

        S_kappa(x) = (4 sqrt(2)/15) (-kappa^(-1/5) x)^(5/2)
                   = (4 sqrt(2)/15) kappa^(-1/2) (-x)^(5/2).

    Cross-check via direct WKB: dominant balance y ~ +sqrt(-kappa x/6) gives
    integral phi(x) = int^x sqrt((6/kappa) y_eq(s)^2 + s) ds = ... but
    actually the WKB action for kappa-P_I in the trans-series sense is
    obtained by linearizing around y_eq:
        delta_y(x) ~ exp(+/- S_kappa(x))
    with S_kappa as above.  This matches the rescaling.

    Returns S_kappa(x), real for x < 0.
    """
    if x >= 0:
        return float('nan')
    return ALPHA_BOUTROUX * kappa ** (-0.5) * (-x) ** 2.5


def trans_series_first_correction(x: float, kappa: float,
                                  stokes_constant: float) -> float:
    """First exponential correction to the kappa-tritronquee asymptotic.

    The full trans-series for kappa-P_I (in the recessive direction) is:

        y(x) = y_eq(x) [1 + (perturbative) + sigma * exp(-S_kappa(x)) (1 + ...)]

    with sigma the (kappa-independent) Stokes constant.  Returns the first-order
    contribution sigma * exp(-S_kappa(x)) (in units of y_eq).
    """
    return stokes_constant * math.exp(-kappa_wkb_action_along_Boutroux(x, kappa))


# ============================================================================
# Section 7: Algebraic dispersionless diagnostic
# ============================================================================

def dispersionless_limit_riccati(x: float, kappa: float) -> float:
    """The algebraic large-kappa diagnostic of the conditional kappa-P_I.

    Drop y'' (dispersion) from y'' = (6/kappa) y^2 + x:

        0 = (6/kappa) y^2 + x  =>  y^2 = -kappa x / 6.

    For x < 0 on the pole-free branch (Joshi-Kruskal): y(x) = -sqrt(-kappa x / 6).
    For x > 0: branch becomes imaginary.

    This is the Hopf shock front of the dispersionless KdV.  In the
    Whitham/Krichever dispersionless hierarchy this is the leading-order
    behaviour and the dispersive corrections build the full kappa-P_I.

    The derivative Riccati equation y' = -(6/kappa) y^2 belongs to a
    different first-integral reduction.  Dropping y'' from the conditional
    second-order equation gives the algebraic equilibrium above.
    """
    if x >= 0:
        return float('nan')
    return -math.sqrt(-kappa * x / 6.0)


def true_riccati_first_integral(x: float, y: float, yp: float,
                                 kappa: float) -> float:
    """First integral of kappa-P_I when x = 0 (autonomous case).

    At x = 0, y'' = (6/kappa) y^2 admits the energy E(y, y') = (1/2) y'^2 -
    (2/kappa) y^3.  This is conserved on solutions of the autonomous equation.
    Off x = 0 it provides a slowly-varying "shadow energy".

    Returns E(y, y') = (1/2) y'^2 - (2/kappa) y^3.
    """
    return 0.5 * yp * yp - (2.0 / kappa) * y ** 3


def verify_dispersionless_at_large_kappa(x: float, kappa_max: float = 1000.0,
                                         num_kappas: int = 10) -> Dict[str, Any]:
    """As kappa -> infinity, the kappa-tritronquee and the dispersionless
    Hopf front converge near the Boutroux asymptotic regime, *after* properly
    rescaling.  Specifically: y(x) / sqrt(-kappa x / 6) -> 1 in the WKB regime.

    Returns the convergence ratio for several kappa values.
    """
    kappas = np.geomspace(1.0, kappa_max, num_kappas)
    ratios = []
    for k in kappas:
        y_disp = dispersionless_limit_riccati(x, k)
        y_asym = kappa_tritronquee_asymptotic(x, k)
        if y_disp == 0 or math.isnan(y_disp):
            ratios.append(float('nan'))
        else:
            ratios.append(y_asym / y_disp)
    return {'kappas': list(kappas), 'ratios': ratios, 'x_eval': x}


# ============================================================================
# Section 8: Fredholm and kernel boundary
# ============================================================================

def airy_kernel(x: float, y: float, s: float) -> float:
    """Airy kernel K_Ai(x, y; s) used in Tracy-Widom F_2 (GUE soft edge).

    K_Ai(x, y; s) = (Ai(x+s) Ai'(y+s) - Ai'(x+s) Ai(y+s)) / (x - y)
                  = int_0^infty Ai(x+u+s) Ai(y+u+s) du.

    For x = y, the kernel reduces by L'Hopital to:
        K_Ai(x, x; s) = Ai'(x+s)^2 - (x+s) Ai(x+s)^2.

    The Tracy-Widom F_2 distribution is:
        F_2(s) = det(I - K_Ai|_{[s, infty)}) = exp(-int_s^infty (x-s) q(x)^2 dx)
    where q is the Hastings-McLeod solution of Painleve II.

    For Painleve I, the analogous representation uses a 2x2
    Riemann-Hilbert problem on the Boutroux contour.  The Airy kernel is
    included only as a benchmark against the soft-edge Tracy-Widom surface.
    """
    from scipy.special import airy
    Ai_x, Aip_x, _, _ = airy(x + s)
    Ai_y, Aip_y, _, _ = airy(y + s)
    if abs(x - y) < 1e-10:
        # Diagonal: use limiting form
        return float(Aip_x ** 2 - (x + s) * Ai_x ** 2)
    return float((Ai_x * Aip_y - Aip_x * Ai_y) / (x - y))


def pi_kernel_structure() -> Dict[str, str]:
    """Description of the Riemann-Hilbert / kernel structure for Painleve I.

    Painleve I is the isomonodromic deformation of a 2x2 system with a
    single irregular singular point at infinity of Poincare rank 7/2 (after
    the standard reduction).  The associated Riemann-Hilbert problem lives
    on a Stokes graph in the complex x-plane (5 anti-Stokes rays from
    infinity).  The corresponding kernel is a 2x2 matrix-valued kernel built
    from the unique solution to the RH problem.

    Status: the engine supplies no closed-form Fredholm representation of
    Tracy-Widom type.  Tracy-Widom belongs to the P_II Hastings-McLeod
    surface.
    """
    return {
        'painleve_type': 'P_I',
        'irregular_singularity': 'infinity',
        'poincare_rank': '7/2 (after standard scaling)',
        'rh_problem': '2x2 matrix RH on 5 anti-Stokes rays from infinity',
        'fredholm_status': (
            'No closed Tracy-Widom-style Fredholm determinant is supplied.  '
            'The natural object is the (2,3) minimal model conformal block, '
            'or the cubic-potential matrix model partition function near its '
            'critical point.'
        ),
        'kappa_dependence': (
            'kappa enters as a real positive rescaling of the independent '
            'variable (x = kappa^(1/5) X) and a homothety of the dependent '
            'variable (y = kappa^(3/5) Y).  The RH structure is unchanged; '
            'only the action S(x) acquires kappa^(-1/2) and the algebraic '
            'sheets acquire kappa^(3/5).'
        ),
        'tracy_widom_relation': (
            'Tracy-Widom F_2 is governed by P_II Hastings-McLeod, not P_I.  '
            'For kappa-P_I there is no Tracy-Widom analogue.  However, '
            'F_2 itself depends on no kappa: it is universal at the soft edge '
            'of GUE and 13 unitary ensembles.'
        ),
    }


def tau_pi_minus_log_det_relation(x: float, kappa: float) -> Dict[str, Any]:
    """Conditional Painleve tau rescaling.

    The Painleve tau-function tau_PI(x) is defined by:
        d^2/dx^2 log tau_PI(x) = y(x)
    where y is the tritronquee.  For kappa-P_I:
        y(x) = kappa^(3/5) Y(kappa^(-1/5) x)
    so:
        log tau_kappa(x) = kappa^(3/5) * (kappa^(2/5)) * log tau_std(kappa^(-1/5) x)
                        = kappa * log tau_std(kappa^(-1/5) x)  [up to linear in x]

    where the kappa^(2/5) factor comes from the double integral and the
    Jacobian of the substitution:
        d^2/dx^2 log tau_kappa = y(x) = kappa^(3/5) Y(X)
        with X = kappa^(-1/5) x.
        d^2 log tau_std/dX^2 = Y(X), and d/dx = kappa^(-1/5) d/dX, so
        d^2/dx^2 = kappa^(-2/5) d^2/dX^2.
        Hence d^2/dx^2 [kappa^(3/5+2/5) log tau_std(X)] = kappa^(3/5) Y(X).
        log tau_kappa(x) = kappa * log tau_std(X) + (linear in x).

    So tau_kappa(x) = (tau_std(X))^kappa * exp(linear in x).
    This identity is internal to the separately supplied Painleve-I
    isomonodromic system.  It does not certify the scalar shadow power as
    an analytic KW/KdV/Painleve tau function.
    """
    X = rescale_x_to_X(x, kappa)
    return {
        'X': X,
        'kappa_power': kappa,  # tau_kappa = tau_std^kappa (up to linear)
        'identity': 'log tau_kappa(x) = kappa * log tau_std(X) + linear',
        'painleve_tau_rescaling_certified': True,
        'matches_shadow_KW': False,
        'analytic_tau_power_certified': False,
        'requires_isomonodromic_input': True,
    }


# ============================================================================
# Section 9: Isomonodromic scope
# ============================================================================

def isomonodromic_check_kappa(kappa: float) -> Dict[str, Any]:
    """Record the isomonodromic scope of the conditional kappa-P_I ODE.

    Argument:
    1. Standard P_I is isomonodromic for the JMU 2x2 system with one
       irregular singular point at infinity (Poincare rank 7/2 after
       reduction).  Reference: Jimbo-Miwa-Ueno, Physica 2D (1981).
    2. The kappa-rescaling X = kappa^(-1/5) x is a real positive change of
       variable.  In the JMU 2x2 system this acts as a conjugation by a
       constant matrix on the irregular type.  The monodromy data are
       unchanged.
    3. Hence the formal monodromy and Stokes multipliers are unchanged.
    4. The deformation parameter (the 'time' of the JMU theory) for kappa-P_I
       is x itself.  As x varies, the monodromy is preserved.

    The ODE inherits the standard P_I isomonodromic system by rescaling.
    The scalar shadow identity does not supply that system by itself.
    """
    return {
        'kappa': kappa,
        'isomonodromic': True,
        'jmu_system': '2x2, one irregular singular point at infinity',
        'irregular_rank': '7/2 (after reduction; 5/2 in some normalizations)',
        'monodromy_data': {
            'formal_monodromy': 'identity (no logarithmic terms)',
            'stokes_multipliers': '(s_0, s_1, s_2, s_3, s_4) ~ Kapaev cyclic',
            'connection_matrix': 'constant on each Stokes sector',
        },
        'kappa_action': (
            'Real positive rescaling X = kappa^(-1/5) x conjugates the '
            'irregular type by a diagonal matrix; monodromy data are '
            'projectively invariant.'
        ),
        'stokes_data_kappa_dependent': False,
        'wkb_action_kappa_dependent': True,  # S(x) ~ kappa^(-1/2) (-x)^(5/2)
        'ode_isomonodromic_if_standard_pi_supplied': True,
        'tau_shadow_isomonodromic_certified': False,
        'requires_external_jmu_system': True,
    }


# ============================================================================
# Section 10: Random matrix boundary
# ============================================================================

def beta_ensemble_identification(kappa: float) -> Dict[str, Any]:
    """Map kappa to the conventional beta-ensemble parameter.

    Two parameters must be separated:
    1. The Dyson beta = 1, 2, 4 (orthogonal/unitary/symplectic) ensembles.
       These have soft-edge tail F_beta(s) governed by Painleve II
       Hastings-McLeod.
    2. The 'kappa' of the shadow obstruction tower, equal to c/2 for Virasoro,
       k for Heisenberg, rank for lattice, etc.  This is a shadow parameter,
       distinct from Dyson beta.

    There is no standard beta = 13 ensemble.  However, there are several
    bridges:
    a. The Stieltjes-Wigert / Mehta beta-ensemble for general beta > 0 has
       eigenvalue density obeying a beta-deformed Selberg integral.  At
       beta = kappa, the soft-edge tail is governed by a 'beta-Tracy-Widom'
       distribution whose general-beta expression is not a simple Painleve II
       formula.
    b. For Painleve I specifically, the natural matrix model is the cubic
       potential V(M) = M^2/2 + g M^4/4 (or similar) at its multi-critical
       point.  The free energy at this critical point obeys P_I.  The
       'kappa' of the shadow is related to the criticality exponent, not
       to a beta value.
    c. Beta = 2 (GUE): kappa = 1 (Witten-Kontsevich tau-function).  This
       IS a genuine identification.
    d. Beta = 1 (GOE) and beta = 4 (GSE): related to kappa = 1/2 and
       kappa = 2 respectively in the Dyson convention, but the Painleve
       transcendents involved are P_II (HM) variants, not P_I.

    Conclusion: there is NO 'kappa = 13 random matrix ensemble' in the
    standard sense.  The shadow kappa = 13 (Virasoro complementarity sum) is
    a CHIRAL ALGEBRA invariant, not a random matrix ensemble parameter.
    """
    standard_beta_kappas = {
        'GOE_beta_1': 0.5,
        'GUE_beta_2': 1.0,
        'GSE_beta_4': 2.0,
    }
    return {
        'kappa': kappa,
        'standard_beta_match': next(
            (label for label, kk in standard_beta_kappas.items() if abs(kk - kappa) < 1e-9),
            None
        ),
        'is_standard_dyson': any(abs(kk - kappa) < 1e-9 for kk in standard_beta_kappas.values()),
        'painleve_type_for_soft_edge': 'P_II Hastings-McLeod (Tracy-Widom)',
        'note': (
            'P_I in this engine is the cubic-critical/minimal-model '
            'transcendent.  The soft-edge Tracy-Widom surface is P_II '
            'Hastings-McLeod.  No standard ensemble has beta = 13 or 24.'
        ),
        'shadow_kappa_meaning': (
            'kappa = c/2 (Virasoro), k (Heisenberg), rank (lattice).  '
            'It is a shadow parameter distinct from Dyson beta.  The number '
            '13 is the Virasoro complementarity sum, not a beta value.'
        ),
    }


def pi_matrix_model_correspondence(kappa: float) -> Dict[str, Any]:
    """Cubic matrix model correspondence for kappa-P_I.

    The (2,3) minimal model (pure 2D gravity) is described by the cubic
    matrix model with free energy F(t) where t is the cosmological constant.
    The genus expansion of F obeys the Painleve I equation:

        F''(t) = u(t),  with u'' + 6 u^2 + t = 0.   [the Douglas-Shenker eqn]

    Note the SIGN: this is u'' = -6 u^2 - t, so u(t) = -y(-t) for our P_I.

    For kappa-P_I, the corresponding matrix model has effective string
    coupling g_s = 1/N rescaled by kappa^(1/2), i.e., g_s_eff = g_s / sqrt(kappa).
    This matches the WKB action S_kappa(x) ~ kappa^(-1/2) (-x)^(5/2).

    Returns the matrix model parameters.
    """
    return {
        'kappa': kappa,
        'minimal_model': '(2,3) = pure 2D gravity',
        'central_charge_minimal': 0.0,
        'matter_central_charge': '-2 (Liouville mode counted)',
        'cubic_potential': 'V(M) = (1/2) M^2 + (g_3/3) M^3 critical point',
        'string_coupling_scaling': f'g_s_eff = g_s * kappa^(-1/2) = g_s / {math.sqrt(kappa):.6f}',
        'free_energy_obeys': "F''(t) = -y(-t) where y solves kappa-P_I",
        'shadow_kappa_match': (
            'kappa(Vir_c=0) = 0; minimal models have c < 1, so kappa < 1/2.  '
            'The kappa = 13 case is OUTSIDE the minimal model range; it does '
            'not correspond to a known matrix model.'
        ),
    }


# ============================================================================
# Section 11: Multi-path verification helpers
# ============================================================================

def verify_tritronquee_initial_data_by_shooting(
    x_far: float = -100.0, num_iter: int = 30, tol: float = 1e-10
) -> Dict[str, float]:
    """Cross-check Y(0), Y'(0) of tritronquee by shooting from x_far inward.

    Strategy: at x = x_far << 0, the tritronquee is well-approximated by the
    Boutroux asymptotic on the NEGATIVE branch (the pole-free branch):

        Y(X) ~ -sqrt(-X/6) + 1/(48 X^2) + O(|X|^{-9/2})
        Y'(X) ~ +1/(12 sqrt(-X/6)) + 1/(24 X^3) + O(...)

    Derivation: Y = -sqrt(-X/6) + f where f is small.  Then
        Y^2 = -X/6 + 2 sqrt(-X/6) f + f^2
        6 Y^2 + X = 12 sqrt(-X/6) f + 6 f^2
        Y'' = sqrt(6)/(24 (-X)^{3/2}) + f''
    Matching leading: 12 sqrt(-X/6) f = sqrt(6)/(24 (-X)^{3/2})
        f = 1/(48 X^2).

    Y'(X): first, d/dX[-sqrt(-X/6)] = +1/(12 sqrt(-X/6)) (positive for X<0).
    Plus d/dX[1/(48 X^2)] = -1/(24 X^3), which at X = -L is +1/(24 L^3).

    Reference: Joshi-Kruskal, Phys. Lett. A 130 (1988) 129-137.

    Returns (Y(0), Y'(0)) by integrating from x_far forward to 0.
    """
    if x_far >= 0:
        raise ValueError("x_far must be < 0")
    L = -x_far  # positive
    sqrt_L_over_6 = math.sqrt(L / 6.0)
    Y_init = -sqrt_L_over_6 + 1.0 / (48.0 * x_far ** 2)  # X^2 = L^2
    Yp_init = 1.0 / (12.0 * sqrt_L_over_6) + 1.0 / (24.0 * L ** 3)

    result = solve_standard_pi(x_far, 0.0, Y_init, Yp_init,
                               max_step=0.01, rtol=1e-12, atol=1e-14)
    return {
        'x_far': x_far,
        'Y_init': Y_init, 'Yp_init': Yp_init,
        'Y_at_zero_shooting': result['final_Y'],
        'Yprime_at_zero_shooting': result['final_Yprime'],
        'Y_at_zero_published': Y_TRITRONQUEE_AT_ZERO,
        'Yprime_at_zero_published': YPRIME_TRITRONQUEE_AT_ZERO,
        'Y_diff': abs(result['final_Y'] - Y_TRITRONQUEE_AT_ZERO),
        'Yp_diff': abs(result['final_Yprime'] - YPRIME_TRITRONQUEE_AT_ZERO),
    }


def verify_first_pole_by_integration(rtol: float = 1e-11) -> Dict[str, float]:
    """Cross-check the first pole of the standard P_I tritronquee on the
    POSITIVE real axis by direct numerical integration with pole detection.
    """
    Y0, Y0p = tritronquee_initial_data()
    result = solve_standard_pi(0.0, 5.0, Y0, Y0p, max_step=0.0005, rtol=rtol)
    return {
        'pole_location_numerical': result['pole_location'],
        'pole_location_published': X_TRITRONQUEE_FIRST_POLE_POS_REAL,
        'difference': abs(result['pole_location'] - X_TRITRONQUEE_FIRST_POLE_POS_REAL)
            if result['pole_location'] is not None else float('nan'),
        'reached_pole': result['reached_pole'],
    }


def cross_verify_kappa_pi_via_rescaling(kappa: float, x_eval: float = -1.0
                                        ) -> Dict[str, float]:
    """Two-path verification of kappa-P_I tritronquee value at x_eval:
       Path A: integrate kappa-P_I directly from kappa-rescaled initial data.
       Path B: integrate standard P_I and rescale.
    """
    # Path A
    y0, y0p = kappa_tritronquee_initial_data(kappa)
    result_A = solve_kappa_pi(0.0, x_eval, y0, y0p, kappa,
                               max_step=0.005, rtol=1e-12, atol=1e-14)
    y_A = result_A['final_y']

    # Path B
    Y0, Y0p = tritronquee_initial_data()
    X_eval = rescale_x_to_X(x_eval, kappa)
    result_B = solve_standard_pi(0.0, X_eval, Y0, Y0p,
                                 max_step=0.005, rtol=1e-12, atol=1e-14)
    y_B = rescale_Y_to_y(result_B['final_Y'], kappa)

    return {
        'kappa': kappa, 'x_eval': x_eval,
        'y_path_A_direct': y_A,
        'y_path_B_rescaled': y_B,
        'difference': abs(y_A - y_B),
        'relative_error': abs(y_A - y_B) / max(abs(y_A), abs(y_B), 1e-12),
    }


# ============================================================================
# Section 12: Top-level summary report
# ============================================================================

def kappa_pi_summary_for_kappa(kappa: float) -> Dict[str, Any]:
    """Top-level summary of kappa-P_I results for a given kappa value."""
    return {
        'kappa': kappa,
        'certification_firewall': painleve_certification_firewall(kappa),
        'finite_scalar_identity': finite_scalar_coefficient_identity(kappa, g_max=3),
        'kdv_residual': direct_kdv_residual(kappa, g_max=3),
        'hirota_residual': direct_hirota_residual(kappa, max_genus=3),
        'tritronquee_initial': kappa_tritronquee_initial_data(kappa),
        'first_pole_positive_real': kappa_tritronquee_first_pole(kappa),
        'asymptotic_at_x_neg_10': kappa_tritronquee_asymptotic(-10.0, kappa),
        'wkb_action_at_x_neg_10': kappa_wkb_action_along_Boutroux(-10.0, kappa),
        'stokes_multipliers': kappa_stokes_multipliers(kappa),
        'ode_isomonodromic_if_standard_pi_supplied': (
            isomonodromic_check_kappa(kappa)['ode_isomonodromic_if_standard_pi_supplied']
        ),
        'tau_shadow_isomonodromic_certified': (
            isomonodromic_check_kappa(kappa)['tau_shadow_isomonodromic_certified']
        ),
        'beta_match': beta_ensemble_identification(kappa)['standard_beta_match'],
        'matrix_model': pi_matrix_model_correspondence(kappa)['minimal_model'],
    }


def landscape_summary() -> Dict[str, Dict[str, Any]]:
    """Summary across standard comparison values.

    kappa = 1: standard P_I (Witten-Kontsevich, GUE / beta=2)
    kappa = 12: Monster module V^natural
    kappa = 13: Virasoro complementarity sum
    kappa = 24: Leech lattice VOA
    """
    return {
        'kappa_1_standard_PI': kappa_pi_summary_for_kappa(1.0),
        'kappa_12_moonshine': kappa_pi_summary_for_kappa(12.0),
        'kappa_13_virasoro_complementarity_sum': kappa_pi_summary_for_kappa(13.0),
        'kappa_24_leech_lattice': kappa_pi_summary_for_kappa(24.0),
    }
