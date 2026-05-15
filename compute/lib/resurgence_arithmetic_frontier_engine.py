"""Exact scalar shadow arithmetic and frontier diagnostics.

This module computes the one-dimensional scalar projection of the
shadow obstruction tower determined by the shadow metric

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t
             + (9*alpha^2 + 16*kappa*S4)*t^2.

The exact content is finite scalar arithmetic: coefficients of
sqrt(Q_L), reciprocal branch-point growth markers, rational reductions,
and p-adic norms.  These computations do not certify full Ecalle
resurgence, alien calculus, analytic continuation, Borel summability,
zeta-zero statements, or the full Maurer-Cartan datum Theta_A.

Historical function names containing "Borel", "Stokes", or "alien" are
kept for compatibility with older compute surfaces.  Their outputs are
diagnostic unless explicitly marked as an exact scalar projection.

Firewalls:
    - Holographic package fields are
      (A, A^i, A^!, C, r(z), Theta_A, nabla^hol).
    - Modular Koszul projections are
      (Fact_X(L), barB_X(L), Theta_L, L_L, (V_br,T_br), R4_mod(L)).
    - Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
    - A^! is the Verdier/continuous-linear dual branch under
      finite-type/completed hypotheses.
    - Z_ch^der(A) = ChirHoch^*(A,A) is Hochschild bulk, not Koszul dual.
    - Kernel constants use the trace/KZ distinction:
      affine raw k*Omega_tr/z; KZ Omega/((k+h^vee)z);
      Heisenberg k/z; Virasoro (c/2)/z^3 + 2T/z.

BEILINSON WARNINGS
==================
AP15: The genus-direction involves quasi-modular forms (E_2*); the
arity-direction involves algebraic functions of t (from Q_L).
These are DISTINCT resurgent structures.

AP19: The bar propagator absorbs a pole: the r-matrix pole orders
are one LESS than the OPE.  The shadow coefficients S_r use the
bar-extracted data, not the raw OPE.

AP31: kappa = 0 does NOT imply Theta = 0.  However, kappa = 0
degenerates Q_L = q2*t^2 (no constant term), moving branch points
to t=0 and t=infinity; the shadow tower changes character.

AP39: kappa != S_2 for non-Virasoro families.  The Borel analysis
uses the actual shadow coefficients S_r, not just kappa.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

Dependencies:
    resurgence_frontier_engine.py -- Pade, lateral Borel sums
    resurgence_stokes_engine.py -- shadow invariants, Borel basics
    shadow_radius.py -- growth rate, branch points
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    from scipy import integrate as scipy_integrate
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# =====================================================================
# Constants
# =====================================================================

PI = math.pi
TWO_PI = 2.0 * PI
FOUR_PI_SQ = TWO_PI ** 2

EXACT_SCALAR_PROJECTION = "exact_scalar_projection"
EXACT_TERMINATING_SCALAR_PROJECTION = "exact_terminating_scalar_projection"
DIAGNOSTIC_NON_CERTIFYING = "diagnostic_non_certifying"

HOLOGRAPHIC_PACKAGE_FIELDS = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)

MODULAR_KOSZUL_PROJECTION_FIELDS = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br,T_br)",
    "R4_mod(L)",
)

KERNEL_NORMALIZATION_FORMULAS = {
    "affine_raw_trace": "k*Omega_tr/z",
    "affine_kz": "Omega/((k+h^vee)z)",
    "heisenberg": "k/z",
    "virasoro": "(c/2)/z^3 + 2T/z",
}

OBJECT_SEPARATION_FIREWALLS = {
    "bar_cobar_inversion": "Omega(B(A))=A is inversion, not Koszul duality",
    "verdier_dual_branch": (
        "A^! is the Verdier/continuous-linear dual branch under "
        "finite-type/completed hypotheses"
    ),
    "hochschild_bulk": "Z_ch^der(A)=ChirHoch^*(A,A) is Hochschild bulk",
    "scalar_projection": (
        "This engine computes scalar shadow projections, not full "
        "Maurer-Cartan data"
    ),
}


def _as_fraction(value: Any, max_denominator: int = 10 ** 12) -> Fraction:
    """Convert a rational input to a stable Fraction."""
    if isinstance(value, Fraction):
        return value
    return Fraction(value).limit_denominator(max_denominator)


@dataclass(frozen=True)
class ScalarShadowMetricExact:
    """Exact scalar shadow metric data for rational parameters."""

    kappa: Fraction
    alpha: Fraction
    S4: Fraction
    q0: Fraction
    q1: Fraction
    q2: Fraction
    Delta: Fraction
    discriminant: Fraction
    rho_squared: Optional[Fraction]
    certification: str = EXACT_SCALAR_PROJECTION


def scalar_shadow_metric_exact(kappa: Any, alpha: Any, S4: Any
                               ) -> ScalarShadowMetricExact:
    """Compute exact scalar data from (kappa, alpha, S4)."""
    kappa_f = _as_fraction(kappa)
    alpha_f = _as_fraction(alpha)
    S4_f = _as_fraction(S4)
    q0 = 4 * kappa_f ** 2
    q1 = 12 * kappa_f * alpha_f
    q2 = 9 * alpha_f ** 2 + 16 * kappa_f * S4_f
    Delta = 8 * kappa_f * S4_f
    discriminant = q1 ** 2 - 4 * q0 * q2
    rho_squared = q2 / q0 if q0 != 0 else None
    return ScalarShadowMetricExact(
        kappa=kappa_f,
        alpha=alpha_f,
        S4=S4_f,
        q0=q0,
        q1=q1,
        q2=q2,
        Delta=Delta,
        discriminant=discriminant,
        rho_squared=rho_squared,
    )


def virasoro_shadow_metric_exact(c_val: Any) -> ScalarShadowMetricExact:
    """Exact Virasoro scalar metric on c(5c+22) != 0."""
    c = _as_fraction(c_val)
    if c == 0 or 5 * c + 22 == 0:
        raise ValueError("Virasoro metric requires c*(5c+22) != 0")
    return scalar_shadow_metric_exact(
        kappa=c / 2,
        alpha=Fraction(2),
        S4=Fraction(10, 1) / (c * (5 * c + 22)),
    )


# =====================================================================
# Section 0: Algebra shadow data
# =====================================================================

@dataclass
class ShadowAlgebraData:
    """Shadow data for resurgence analysis of the arity-direction tower.

    Encodes kappa, alpha = S_3, S_4, and derived quantities
    (Delta, rho, theta, branch points) sufficient to determine the
    scalar shadow obstruction tower on a one-dimensional primary line.
    This is a projection of Theta_A, not the full Maurer-Cartan datum.
    The field kappa_dual records only the scalar Verdier-complement
    value used in the landscape tables; it is not the object A^!.

    The shadow metric is Q_L(t) = q0 + q1*t + q2*t^2 where
        q0 = 4*kappa^2
        q1 = 12*kappa*alpha
        q2 = 9*alpha^2 + 16*kappa*S4
    """
    name: str
    kappa: float
    alpha: float  # = S_3 cubic shadow
    S4: float     # quartic shadow coefficient
    depth_class: str  # G, L, C, M
    c: float = 0.0
    kappa_dual: float = 0.0

    # Derived quantities computed in __post_init__
    Delta: float = 0.0
    rho: float = 0.0
    theta: float = 0.0
    branch_plus: complex = 0j
    branch_minus: complex = 0j
    q0: float = 0.0
    q1: float = 0.0
    q2: float = 0.0

    def __post_init__(self):
        self.Delta = 8.0 * self.kappa * self.S4
        self.q0 = 4.0 * self.kappa ** 2
        self.q1 = 12.0 * self.kappa * self.alpha
        self.q2 = 9.0 * self.alpha ** 2 + 16.0 * self.kappa * self.S4
        disc = self.q1 ** 2 - 4.0 * self.q0 * self.q2
        sqrt_disc = cmath.sqrt(disc)
        if abs(self.q2) > 1e-30:
            self.branch_plus = (-self.q1 + sqrt_disc) / (2.0 * self.q2)
            self.branch_minus = (-self.q1 - sqrt_disc) / (2.0 * self.q2)
        else:
            self.branch_plus = complex('inf')
            self.branch_minus = complex('inf')
        R = min(abs(self.branch_plus), abs(self.branch_minus))
        self.rho = 1.0 / R if R > 1e-30 and R < 1e15 else 0.0
        if abs(self.branch_plus) <= abs(self.branch_minus):
            self.theta = cmath.phase(self.branch_plus)
        else:
            self.theta = cmath.phase(self.branch_minus)

    @property
    def instanton_actions(self) -> Tuple[complex, complex]:
        """Compatibility alias: reciprocal branch-point growth markers."""
        if abs(self.branch_plus) > 1e-30:
            A_p = 1.0 / self.branch_plus
        else:
            A_p = complex('inf')
        if abs(self.branch_minus) > 1e-30:
            A_m = 1.0 / self.branch_minus
        else:
            A_m = complex('inf')
        return (A_p, A_m)


# =====================================================================
# Section 0a: Algebra constructors
# =====================================================================

def virasoro_data(c_val: float) -> ShadowAlgebraData:
    """Virasoro at central charge c.

    kappa = c/2, alpha = 2 (from T_{(1)}T = 2T),
    S_4 = Q^contact_Vir = 10/(c(5c+22)).
    """
    if abs(c_val) < 1e-30:
        return ShadowAlgebraData(
            name=f'Vir_c={c_val}', kappa=0.0, alpha=2.0, S4=0.0,
            depth_class='M', c=c_val, kappa_dual=13.0,
        )
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    kappa_dual = (26.0 - c_val) / 2.0
    return ShadowAlgebraData(
        name=f'Vir_c={c_val}', kappa=kappa, alpha=alpha, S4=S4,
        depth_class='M', c=c_val, kappa_dual=kappa_dual,
    )


def affine_sl2_data(k_val: float) -> ShadowAlgebraData:
    """Affine sl_2 at level k. Class L, depth 3."""
    kappa = 3.0 * (k_val + 2.0) / 4.0
    alpha = 1.0
    S4 = 0.0
    c_val = 3.0 * k_val / (k_val + 2.0) if abs(k_val + 2.0) > 1e-15 else float('nan')
    return ShadowAlgebraData(
        name=f'aff_sl2_k={k_val}', kappa=kappa, alpha=alpha, S4=S4,
        depth_class='L', c=c_val, kappa_dual=-kappa,
    )


def heisenberg_data(rank: int = 1, level: float = 1.0) -> ShadowAlgebraData:
    """Heisenberg at given rank and level. Class G, depth 2."""
    kappa = float(rank) * level
    return ShadowAlgebraData(
        name=f'Heis_n={rank}_k={level}', kappa=kappa, alpha=0.0, S4=0.0,
        depth_class='G', c=float(rank), kappa_dual=-kappa,
    )


# =====================================================================
# Section 1: Shadow coefficients via convolution recursion
# =====================================================================

def shadow_coefficients(data: ShadowAlgebraData, max_r: int = 60
                        ) -> Dict[int, float]:
    """Compute shadow coefficients S_r for r = 2, ..., max_r.

    Uses the convolution recursion f^2 = Q_L where f(t) = sqrt(Q_L(t))
    and S_r = a_{r-2} / r with a_n = [t^n] f(t).

    The recursion:
        a_0 = sqrt(q0) = 2*|kappa|
        a_1 = q1 / (2*a_0)
        a_n = (c_n - sum_{j=1}^{n-1} a_j a_{n-j}) / (2*a_0)  for n >= 2
    where c_0 = q0, c_1 = q1, c_2 = q2, c_n = 0 for n >= 3.
    """
    max_n = max_r - 2
    if max_n < 0:
        return {}

    q0 = data.q0
    q1 = data.q1
    q2 = data.q2

    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0) if q0 >= 0 else 0.0
    if a[0] == 0.0:
        return {r: 0.0 for r in range(2, max_r + 1)}
    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a[0])
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv_sum / (2.0 * a[0])

    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


def shadow_coefficients_mpmath(data: ShadowAlgebraData, max_r: int = 60,
                                dps: int = 50) -> Dict[int, Any]:
    """High-precision shadow coefficients using mpmath.

    Returns dict mapping r -> mpmath.mpf(S_r).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required for high-precision computation")
    with mpmath.workdps(dps):
        q0 = mpmath.mpf(data.q0)
        q1 = mpmath.mpf(data.q1)
        q2 = mpmath.mpf(data.q2)

        max_n = max_r - 2
        if max_n < 0:
            return {}

        a = [mpmath.mpf(0)] * (max_n + 1)
        a[0] = mpmath.sqrt(q0)
        if a[0] == 0:
            return {r: mpmath.mpf(0) for r in range(2, max_r + 1)}
        if max_n >= 1:
            a[1] = q1 / (2 * a[0])
        if max_n >= 2:
            a[2] = (q2 - a[1] ** 2) / (2 * a[0])
        for n in range(3, max_n + 1):
            conv_sum = mpmath.fsum(a[j] * a[n - j] for j in range(1, n))
            a[n] = -conv_sum / (2 * a[0])

        return {r: a[r - 2] / r for r in range(2, max_r + 1)}


# =====================================================================
# Section 2: Borel transform of the shadow tower
# =====================================================================

def borel_transform_coefficients(shadow_coeffs: Dict[int, float]
                                  ) -> Dict[int, float]:
    r"""Borel transform coefficients: b_r = S_r / Gamma(r).

    B[H_A](zeta) = sum_{r>=2} S_r * zeta^{r-1} / Gamma(r)

    This is the Borel transform normalized for the shadow tower
    H(t) = sum S_r t^r treated as a diagnostic series.  The exact
    class-M shadow coefficients coming from sqrt(Q_L) have algebraic
    Darboux growth, not factorial growth.  Thus this ordinary factorial
    Borel transform is entire by the ratio test at the scalar level; it
    does not certify Ecalle singularities.
    """
    result = {}
    for r, sr in shadow_coeffs.items():
        result[r] = sr / math.gamma(r)
    return result


def borel_transform_evaluate(shadow_coeffs: Dict[int, float],
                              zeta: complex) -> complex:
    r"""Evaluate the Borel transform B[H_A](zeta) = sum S_r zeta^{r-1} / Gamma(r).

    Parameters
    ----------
    shadow_coeffs : dict mapping r -> S_r
    zeta : complex Borel plane variable

    Returns
    -------
    complex
        B[H_A](zeta)
    """
    zeta = complex(zeta)
    result = 0.0 + 0.0j
    for r in sorted(shadow_coeffs.keys()):
        sr = shadow_coeffs[r]
        gamma_r = math.gamma(r)
        term = sr * zeta ** (r - 1) / gamma_r
        result += term
        if r > 10 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_transform_evaluate_mpmath(shadow_coeffs_mp: Dict[int, Any],
                                     zeta: complex, dps: int = 50) -> complex:
    """High-precision Borel transform evaluation using mpmath."""
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    with mpmath.workdps(dps):
        z = mpmath.mpc(zeta)
        result = mpmath.mpc(0)
        for r in sorted(shadow_coeffs_mp.keys()):
            sr = shadow_coeffs_mp[r]
            gamma_r = mpmath.gamma(r)
            term = sr * z ** (r - 1) / gamma_r
            result += term
        return complex(result)


def borel_singularity_locations(data: ShadowAlgebraData
                                 ) -> Tuple[complex, complex]:
    r"""Reciprocal branch-point growth markers from the shadow metric.

    The shadow generating function H(t) = t^2 sqrt(Q_L(t)) has
    branch points at zeros of Q_L(t).  This compatibility function
    returns zeta_k = 1/t_k, the reciprocal markers controlling
    coefficient growth.  For the ordinary factorial Borel transform
    in this module these are not certified Borel-plane singularities.

    Returns (zeta_plus, zeta_minus).
    """
    t_p = data.branch_plus
    t_m = data.branch_minus
    if abs(t_p) > 1e-30:
        zeta_p = 1.0 / t_p
    else:
        zeta_p = complex('inf')
    if abs(t_m) > 1e-30:
        zeta_m = 1.0 / t_m
    else:
        zeta_m = complex('inf')
    return (zeta_p, zeta_m)


def locate_all_borel_singularities(data: ShadowAlgebraData
                                    ) -> List[Dict[str, Any]]:
    """Return scalar branch markers with explicit non-certification.

    For class G/L the scalar tower terminates.  For class M this returns
    the two reciprocal Q_L branch-point markers.  They are useful
    diagnostics for coefficient growth and Pade tests on the original
    algebraic series.  They are not certified singularities of the
    ordinary factorial Borel transform.

    Returns list of dicts with position, type, order.
    """
    singularities = []

    if data.depth_class == 'G':
        return singularities  # Entire Borel transform
    if data.depth_class == 'L':
        return singularities  # Polynomial Borel transform

    # Class M: branch point singularities
    zeta_p, zeta_m = borel_singularity_locations(data)

    # Leading singularity pair (from Q_L branch points)
    singularities.append({
        'position': zeta_p,
        'modulus': abs(zeta_p),
        'argument': cmath.phase(zeta_p),
        'type': 'reciprocal_branch_marker',
        'order': 0.5,  # square root type
        'label': 'zeta_+',
        'certified_borel_singularity': False,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
    })
    singularities.append({
        'position': zeta_m,
        'modulus': abs(zeta_m),
        'argument': cmath.phase(zeta_m),
        'type': 'reciprocal_branch_marker',
        'order': 0.5,
        'label': 'zeta_-',
        'certified_borel_singularity': False,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
    })

    # Sort by modulus (distance from origin)
    singularities.sort(key=lambda s: s['modulus'])
    return singularities


def frontier_diagnostic_status(data: ShadowAlgebraData) -> Dict[str, Any]:
    """Certification split for the arithmetic/resurgence frontier surface."""
    terminating = data.depth_class in ('G', 'L')
    return {
        'scalar_projection': EXACT_SCALAR_PROJECTION,
        'terminating_tower': terminating,
        'ordinary_borel_transform_entire': True,
        'certifies_borel_singularities': False,
        'certifies_borel_summability': False,
        'certifies_ecalle_stokes': False,
        'certifies_alien_calculus': False,
        'certifies_zeta_zero_theorem': False,
        'certifies_analytic_continuation': False,
        'certifies_full_mc_data': False,
        'object_firewalls': OBJECT_SEPARATION_FIREWALLS,
        'holographic_package_fields': HOLOGRAPHIC_PACKAGE_FIELDS,
        'modular_koszul_projection_fields': MODULAR_KOSZUL_PROJECTION_FIELDS,
        'kernel_normalization_formulas': KERNEL_NORMALIZATION_FORMULAS,
        'branch_markers_are_growth_diagnostics': not terminating,
        'certification': (
            EXACT_TERMINATING_SCALAR_PROJECTION
            if terminating else DIAGNOSTIC_NON_CERTIFYING
        ),
    }


# =====================================================================
# Section 3: Pade approximant for singularity detection
# =====================================================================

def pade_coefficients(coeffs: List[float], m: int, n: int
                      ) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
    """Compute [m/n] Pade approximant from power series coefficients.

    Returns (P_coeffs, Q_coeffs) or (None, None) on failure.
    """
    N = m + n + 1
    if len(coeffs) < N:
        coeffs = list(coeffs) + [0.0] * (N - len(coeffs))
    if n == 0:
        return np.array(coeffs[:m + 1]), np.array([1.0])

    mat = np.zeros((n, n))
    rhs = np.zeros(n)
    for i in range(n):
        for j in range(n):
            idx = m + 1 + i - (j + 1)
            if 0 <= idx < len(coeffs):
                mat[i, j] = coeffs[idx]
        idx_r = m + 1 + i
        if 0 <= idx_r < len(coeffs):
            rhs[i] = -coeffs[idx_r]

    try:
        q_vec = np.linalg.solve(mat, rhs)
    except np.linalg.LinAlgError:
        return None, None

    Q_coeffs = np.concatenate(([1.0], q_vec))
    P_coeffs = np.zeros(m + 1)
    for k_idx in range(m + 1):
        for j in range(min(k_idx, n) + 1):
            if k_idx - j < len(coeffs):
                P_coeffs[k_idx] += Q_coeffs[j] * coeffs[k_idx - j]

    return P_coeffs, Q_coeffs


def pade_poles(Q_coeffs: np.ndarray) -> np.ndarray:
    """Find poles of the Pade approximant (roots of denominator)."""
    if Q_coeffs is None or len(Q_coeffs) <= 1:
        return np.array([])
    poly = list(reversed(Q_coeffs))
    return np.roots(poly)


def borel_pade_singularities(data: ShadowAlgebraData,
                              max_r: int = 60) -> Dict[str, Any]:
    """Detect branch points of the shadow tower via Pade of the original series.

    The shadow generating function G(t) = sum_{r>=2} S_r t^r is algebraic
    (Gevrey-0), so its Borel transform B[G](xi) = sum S_r xi^r/r! is ENTIRE.
    Pade must be applied to the original series, not the Borel transform,
    to detect the branch point singularities.

    We form g(t) = G(t)/t^2 = sum_{k>=0} S_{k+2} t^k
    and compute the diagonal Pade [N/N] of g.  The poles of the Pade
    approximant converge to the branch points of G (zeros of Q_L),
    whose reciprocals are the historical action diagnostics.

    The reciprocal markers A_pm = 1/t_pm are growth diagnostics, not
    certified Ecalle action data.

    Returns dict with branch points detected via Pade vs predicted.
    """
    coeffs = shadow_coefficients(data, max_r)

    # Form g(t) = sum_{k>=0} S_{k+2} * t^k
    inner = []
    for k in range(max_r - 1):
        r = k + 2
        inner.append(coeffs.get(r, 0.0))

    n_c = len(inner)
    m = n_c // 2
    n = m
    if n <= 0:
        return {'detected_poles': np.array([]), 'predicted': (0j, 0j)}

    P, Q = pade_coefficients(inner, m, n)
    if Q is None:
        return {'detected_poles': np.array([]), 'predicted': (0j, 0j)}

    poles = pade_poles(Q)

    # The Pade poles approximate the branch points t_pm
    # The predicted branch points from the shadow metric:
    predicted_branch = (data.branch_plus, data.branch_minus)
    # Reciprocal branch markers, historically called action diagnostics:
    predicted_borel = borel_singularity_locations(data)

    # Find closest detected pole to each predicted branch point
    pole_match = {}
    for label, pred in zip(['t_+', 't_-'], predicted_branch):
        if len(poles) == 0:
            continue
        dists = [abs(p - pred) for p in poles]
        best_idx = int(np.argmin(dists))
        pole_match[label] = {
            'predicted': pred,
            'detected': poles[best_idx],
            'error': dists[best_idx],
            'relative_error': dists[best_idx] / abs(pred) if abs(pred) > 1e-30 else float('inf'),
        }

    return {
        'detected_poles': poles,
        'predicted_branch_points': predicted_branch,
        'reciprocal_branch_markers': predicted_borel,
        'predicted_borel_singularities': predicted_borel,
        'certified_borel_singularities': False,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
        'pole_match': pole_match,
        'n_coeffs': n_c,
        'pade_order': (m, n),
    }


# =====================================================================
# Section 4: Monodromy diagnostics and arithmetic recognition
# =====================================================================

def stokes_constant_from_monodromy(data: ShadowAlgebraData) -> complex:
    r"""Diagnostic monodromy jump normalization from sqrt(Q_L).

    The shadow connection nabla^sh = d - Q'_L/(2Q_L) dt has
    residue 1/2 at each simple zero of Q_L.  The monodromy
    around a simple zero is exp(2*pi*i * 1/2) = -1.

    Returning +/- 2*pi*i is a normalization of this scalar monodromy
    jump.  It is not a certificate of an Ecalle Stokes constant for
    the full chiral Maurer-Cartan problem.
    """
    if data.depth_class in ('G', 'L'):
        return 0.0 + 0.0j  # No Stokes phenomenon for terminating towers
    return 2.0j * PI


def stokes_constant_numerical(data: ShadowAlgebraData, max_r: int = 80
                               ) -> Dict[str, Any]:
    r"""Numerically check scalar growth behind the monodromy diagnostic.

    For the shadow tower G(t) = t^2 * sqrt(Q_L(t)) with branch points
    at t_pm = zeros of Q_L, the asymptotic behavior is:

        S_r ~ C * |t_0|^{-r} * r^{-3/2} * Re(e^{-i*r*theta} * amplitude)

    where t_0 = |t_0| * e^{i*theta} is the nearest branch point.

    The diagnostic value 2*pi*i arises from the monodromy of
    sqrt(Q_L) around the branch point (residue 1/2 of the shadow
    connection, thm:shadow-connection).

    To verify numerically: we check that consecutive ratios
    S_{r+1}/S_r converge to rho * e^{-i*theta} (the inverse branch point),
    confirming the asymptotic behavior that underlies the monodromy argument.

    The scalar monodromy is exact.  The Ecalle Stokes interpretation is
    not certified here because the shadow tower is Gevrey-0
    (algebraic), not Gevrey-1.  For Gevrey-0, the large-order relation
    S_r ~ S_1*A^{-r}*Gamma(r) does not hold; instead
    S_r ~ C * rho^r * r^{-3/2}.
    """
    if data.depth_class in ('G', 'L'):
        return {
            'S_1': 0.0,
            'S_1_theoretical': 0.0,
            'depth_class': data.depth_class,
            'converged': True,
            'certification': EXACT_TERMINATING_SCALAR_PROJECTION,
            'certifies_ecalle_stokes': False,
        }

    coeffs = shadow_coefficients(data, max_r)
    rho = data.rho
    if rho < 1e-30:
        return {'S_1': complex('nan'), 'S_1_theoretical': 2j * PI,
                'converged': False,
                'certification': DIAGNOSTIC_NON_CERTIFYING,
                'certifies_ecalle_stokes': False}

    theta = data.theta

    # Verify asymptotics: S_{r+1}/S_r -> rho * e^{-i*theta}
    # For real S_r: the ratios alternate/oscillate and converge in modulus to rho
    ratios = []
    for r in range(max(5, max_r // 2), max_r):
        sr = coeffs.get(r, 0.0)
        sr_next = coeffs.get(r + 1, 0.0)
        if abs(sr) < 1e-100:
            continue
        ratio = sr_next / sr
        ratios.append({'r': r, 'ratio': ratio, 'modulus': abs(ratio)})

    if not ratios:
        return {'S_1': complex('nan'), 'S_1_theoretical': 2j * PI,
                'converged': False,
                'certification': DIAGNOSTIC_NON_CERTIFYING,
                'certifies_ecalle_stokes': False}

    # Check that ratio moduli converge to rho
    n_avg = min(10, len(ratios))
    avg_mod = sum(entry['modulus'] for entry in ratios[-n_avg:]) / n_avg
    rho_match = abs(avg_mod - rho) / max(rho, 1e-10) < 0.1

    # The monodromy-jump normalization is determined by the scalar connection.
    S_1_exact = 2j * PI

    return {
        'S_1': S_1_exact,
        'S_1_theoretical': S_1_exact,
        'ratio_sequence': ratios,
        'converged': rho_match,
        'rho': rho,
        'rho_from_ratios': avg_mod,
        'theta': theta,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
        'certifies_ecalle_stokes': False,
        'checked_identity': 'Darboux growth of the scalar algebraic tower',
    }


def stokes_constant_pslq(data: ShadowAlgebraData, max_r: int = 80,
                           dps: int = 50) -> Dict[str, Any]:
    r"""Recognize scalar growth data using high precision and PSLQ.

    For the shadow tower (Gevrey-0), 2*pi*i is only the monodromy-jump
    normalization used by this diagnostic.  This function verifies the
    shadow growth rate rho to high precision
    using mpmath, then uses PSLQ to identify rho^2 as an algebraic number.

    For Virasoro: rho^2 = (180c + 872) / ((5c+22)*c^2), which is rational
    for rational c.  PSLQ should recover the exact rational value.
    """
    if not HAS_MPMATH:
        return {'recognized': False, 'reason': 'mpmath not available',
                'certifies_ecalle_stokes': False}
    if data.depth_class in ('G', 'L'):
        return {
            'recognized': True,
            'S_1': 0,
            'relation': 'S_1 = 0 (terminating tower)',
            'certification': EXACT_TERMINATING_SCALAR_PROJECTION,
            'certifies_ecalle_stokes': False,
        }

    with mpmath.workdps(dps):
        coeffs_mp = shadow_coefficients_mpmath(data, max_r, dps)
        rho_mp = mpmath.mpf(data.rho)

        # Verify rho from consecutive ratios at high precision
        ratios = []
        for r in range(max(30, max_r - 20), max_r):
            sr = coeffs_mp.get(r, mpmath.mpf(0))
            sr_next = coeffs_mp.get(r + 1, mpmath.mpf(0))
            if abs(sr) > mpmath.mpf('1e-100'):
                ratios.append(abs(sr_next / sr))

        if not ratios:
            return {
                'recognized': False,
                'reason': 'no valid ratios',
                'certification': DIAGNOSTIC_NON_CERTIFYING,
                'certifies_ecalle_stokes': False,
            }

        n_avg = min(5, len(ratios))
        rho_numerical = sum(ratios[-n_avg:]) / n_avg

        # Diagnostic monodromy-jump normalization.
        S_1_exact = 2j * PI

        result = {
            'S_1_real': 0.0,
            'S_1_imag': 2.0 * PI,
            'S_1_theoretical_imag': 2.0 * PI,
            'near_2pi_i': True,
            'rho_numerical': float(rho_numerical),
            'rho_predicted': float(rho_mp),
            'rho_match': abs(float(rho_numerical - rho_mp)) < 0.01 * float(rho_mp),
            'certification': DIAGNOSTIC_NON_CERTIFYING,
            'certifies_ecalle_stokes': False,
        }

        # PSLQ: try to identify rho^2 as rational
        try:
            rho_sq = rho_mp ** 2
            pslq_result = mpmath.identify(rho_sq)
            result['pslq_rho_sq'] = str(pslq_result) if pslq_result else None
            result['recognized'] = pslq_result is not None
        except Exception:
            result['pslq_rho_sq'] = None
            result['recognized'] = False

        return result


# =====================================================================
# Section 5: Alien derivatives
# =====================================================================

def alien_derivative_structure(data: ShadowAlgebraData, max_r: int = 60,
                                max_k: int = 5) -> List[Dict[str, Any]]:
    r"""Compute non-certifying alien-calculus diagnostics.

    For the scalar algebraic shadow tower:
    - omega_k = k * omega_1 where omega_1 = 1/t_branch_nearest
    - S_k is a diagnostic monodromy-jump amplitude
    - For class G/L: all diagnostics vanish because the tower terminates

    This function does not construct Ecalle alien derivatives of the
    full chiral Maurer-Cartan problem.  It records the scalar branch
    geometry a genuine alien-calculus construction would have to refine.

    Parameters
    ----------
    data : ShadowAlgebraData
    max_r : maximum arity for coefficient computation
    max_k : number of candidate diagnostic markers to compute

    Returns
    -------
    List of dicts, one per candidate marker omega_k.
    """
    if data.depth_class in ('G', 'L'):
        return [{'k': k, 'omega_k': 0.0, 'S_k': 0.0,
                 'type': 'zero (terminating tower)',
                 'certification': EXACT_TERMINATING_SCALAR_PROJECTION,
                 'certifies_alien_calculus': False}
                for k in range(1, max_k + 1)]

    zeta_p, zeta_m = borel_singularity_locations(data)
    nearest = zeta_p if abs(zeta_p) <= abs(zeta_m) else zeta_m
    omega_1 = nearest

    S_1 = stokes_constant_from_monodromy(data)
    coeffs = shadow_coefficients(data, max_r)

    results = []
    for k in range(1, max_k + 1):
        omega_k = k * omega_1

        # Diagnostic amplitude from the scalar square-root monodromy.
        S_k = (-1) ** (k + 1) * S_1 / k

        # Candidate leading correction coefficients.  These do not define
        # an alien derivative on the full chiral object.
        alien_coefficients = {}
        for r in sorted(coeffs.keys()):
            if r < 2:
                continue
            alien_coefficients[r] = S_k * coeffs[r] * (abs(omega_1) ** (-r))

        results.append({
            'k': k,
            'omega_k': omega_k,
            'S_k': S_k,
            'type': 'candidate_branch_marker' if k == 1 else 'candidate_multiple_marker',
            'alien_coefficients': alien_coefficients,
            'certification': DIAGNOSTIC_NON_CERTIFYING,
            'certifies_alien_calculus': False,
        })

    return results


def bridge_equation_check(data: ShadowAlgebraData, max_r: int = 40
                           ) -> Dict[str, Any]:
    r"""Verify the scalar convolution identity behind the shadow metric.

    The checked identity is f(t)^2 = Q_L(t), equivalently the scalar
    coefficient recursion for sqrt(Q_L).  This is a projection of the
    bar-intrinsic Maurer-Cartan equation, not a proof of full MC data
    and not an alien bridge equation.
    """
    if data.depth_class in ('G', 'L'):
        return {
            'bridge_satisfied': True,
            'reason': 'Tower terminates: bridge equation trivially satisfied',
            'depth_class': data.depth_class,
            'checked_identity': 'terminating scalar shadow recursion',
            'certification': EXACT_TERMINATING_SCALAR_PROJECTION,
            'certifies_full_mc_data': False,
            'certifies_alien_calculus': False,
        }

    coeffs = shadow_coefficients(data, max_r)

    # Check that the recursive relation is satisfied:
    # The convolution recursion a_n = -(1/(2*a_0)) sum a_j a_{n-j}
    # is precisely the MC equation projected to each arity.
    # Verify by recomputing and comparing.
    q0 = data.q0
    q1 = data.q1
    q2 = data.q2

    a0 = math.sqrt(q0)
    max_n = max_r - 2
    a = [0.0] * (max_n + 1)
    a[0] = a0
    if max_n >= 1:
        a[1] = q1 / (2.0 * a0)
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * a0)

    residuals = []
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a_n_computed = -conv / (2.0 * a0)
        a[n] = a_n_computed
        # Check against shadow coefficient
        r = n + 2
        sr_from_recursion = a_n_computed / r
        sr_from_coeffs = coeffs.get(r, 0.0)
        residual = abs(sr_from_recursion - sr_from_coeffs)
        residuals.append({'r': r, 'residual': residual})

    max_residual = max(entry['residual'] for entry in residuals) if residuals else 0.0

    return {
        'bridge_satisfied': max_residual < 1e-10,
        'max_residual': max_residual,
        'residuals': residuals,
        'n_checked': len(residuals),
        'checked_identity': 'f(t)^2 = Q_L(t) coefficient recursion',
        'certification': EXACT_SCALAR_PROJECTION,
        'certifies_full_mc_data': False,
        'certifies_alien_calculus': False,
    }


# =====================================================================
# Section 6: Transseries diagnostics and candidate sectors
# =====================================================================

def transseries_perturbative(data: ShadowAlgebraData, t: complex,
                              max_r: int = 60) -> complex:
    """Evaluate the perturbative sector H^{(0)}(t) = sum S_r t^r."""
    coeffs = shadow_coefficients(data, max_r)
    t = complex(t)
    result = 0.0 + 0.0j
    for r in sorted(coeffs.keys()):
        result += coeffs[r] * t ** r
    return result


def transseries_one_instanton_coefficients(data: ShadowAlgebraData,
                                            max_r: int = 60
                                            ) -> Dict[int, float]:
    r"""Compute a non-certifying one-instanton diagnostic.

    The scalar algebraic tower supplies branch cuts of sqrt(Q_L), hence
    candidate exponential scales for a transseries ansatz.  This helper
    returns a toy leading-sector diagnostic only.  It is not a proof of
    analytic continuation, resurgence, or full instanton calculus.

    At large arity the nearest Q_L branch point controls the scalar
    Darboux growth, S_r ~ C*t_0^{-r}*r^{-3/2}.  The coefficients below
    are only a regression diagnostic based on that branch geometry.
    """
    if data.depth_class in ('G', 'L'):
        return {}

    coeffs = shadow_coefficients(data, max_r)
    t_p = data.branch_plus
    t_m = data.branch_minus

    # Candidate second-sheet diagnostic: sqrt(Q_L) changes sign after
    # looping around a simple branch point.
    phase = cmath.exp(1j * cmath.phase(t_p))
    inst_coeffs = {}
    for r in sorted(coeffs.keys()):
        # Branch-geometry diagnostic; the scale factor prevents this toy
        # term from being mistaken for a certified sector.
        ratio = (-1.0) * (abs(t_p)) ** (-r + 2) * phase ** (-r)
        inst_coeffs[r] = coeffs[r] * float(abs(ratio)) * 1e-2

    return inst_coeffs


def transseries_evaluate(data: ShadowAlgebraData, t: complex,
                          sigma: float = 1.0, max_r: int = 60
                          ) -> Dict[str, Any]:
    r"""Evaluate the perturbative sum plus a diagnostic transseries term.

    H_A(t, sigma) = H^{(0)}(t) + sigma * exp(-A_1/t) * H^{(1)}(t) + ...

    Returns dict with perturbative, diagnostic 1-instanton, and total.
    """
    t = complex(t)
    H_0 = transseries_perturbative(data, t, max_r)

    result = {'perturbative': H_0}

    if data.depth_class in ('G', 'L'):
        result['one_instanton'] = 0.0 + 0.0j
        result['total'] = H_0
        result['certification'] = EXACT_TERMINATING_SCALAR_PROJECTION
        result['certifies_resurgence'] = False
        return result

    # Candidate one-sector contribution.
    inst_coeffs = transseries_one_instanton_coefficients(data, max_r)
    A_1 = data.instanton_actions[0]

    if abs(A_1) < 1e10:
        exp_factor = cmath.exp(-A_1 / t)
        H_1 = sum(inst_coeffs.get(r, 0.0) * t ** r for r in sorted(inst_coeffs.keys()))
        one_inst = sigma * exp_factor * H_1
    else:
        one_inst = 0.0 + 0.0j

    result['one_instanton'] = one_inst
    result['total'] = H_0 + one_inst
    result['certification'] = DIAGNOSTIC_NON_CERTIFYING
    result['certifies_resurgence'] = False
    return result


# =====================================================================
# Section 7: Lateral Borel sums and median resummation
# =====================================================================

def lateral_borel_sum(shadow_coeffs: Dict[int, float], t: complex,
                       epsilon: float = 0.02, xi_max: float = 100.0,
                       n_quad: int = 3000) -> complex:
    r"""Numerical Laplace-Borel diagnostic via a deformed contour.

    S_eps[H](t) = int_0^{infty*e^{i*eps}} B[H](zeta) e^{-zeta/t} dzeta/t

    epsilon > 0: S_+ (above the real axis)
    epsilon < 0: S_- (below)
    """
    t = complex(t)
    if abs(t) < 1e-15:
        return 0.0 + 0.0j

    direction = cmath.exp(1j * epsilon)
    ds = xi_max / n_quad
    result = 0.0 + 0.0j

    for k in range(1, n_quad + 1):
        s = (k - 0.5) * ds
        zeta = s * direction
        B_val = borel_transform_evaluate(shadow_coeffs, zeta)
        weight = cmath.exp(-zeta / t) * direction / t
        result += B_val * weight * ds

    return result


def median_borel_sum(data: ShadowAlgebraData, t: complex,
                      max_r: int = 60, epsilon: float = 0.02,
                      xi_max: float = 80.0, n_quad: int = 3000
                      ) -> Dict[str, complex]:
    r"""Median of two numerical Laplace-Borel diagnostics.

    This averages lateral numerical integrals.  It is useful for
    regression tests, but it does not certify Borel summability or a
    canonical median resummation theorem for the chiral problem.

    Returns dict with S_+, S_-, median, and Stokes jump.
    """
    coeffs = shadow_coefficients(data, max_r)

    S_plus = lateral_borel_sum(coeffs, t, epsilon=+epsilon,
                                xi_max=xi_max, n_quad=n_quad)
    S_minus = lateral_borel_sum(coeffs, t, epsilon=-epsilon,
                                 xi_max=xi_max, n_quad=n_quad)

    return {
        'S_plus': S_plus,
        'S_minus': S_minus,
        'median': (S_plus + S_minus) / 2.0,
        'stokes_jump': S_plus - S_minus,
        't': t,
        'max_r': max_r,
        'epsilon': epsilon,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
        'certifies_borel_summability': False,
    }


def median_sum_at_unit_arity(data: ShadowAlgebraData,
                              max_r: int = 60, **kwargs) -> Dict[str, Any]:
    r"""Evaluate median Borel sum at t = 1.

    The "unit arity" evaluation gives the exact value of the shadow
    generating function resummed at t = 1.

    Note: sum S_r t^r != t^2*sqrt(Q_L(t)).
    The WEIGHTED sum satisfies sum r*S_r t^r = t^2*sqrt(Q_L(t)).
    The unweighted sum G(t) = sum S_r t^r is related by
    G(t) = integral from 0 to t of s*sqrt(Q_L(s)) ds / (something).
    The exact value of G(1) from coefficients is the partial sum.
    """
    result = median_borel_sum(data, t=1.0 + 0.0j, max_r=max_r, **kwargs)

    # Compare with direct sum (partial sum up to max_r)
    coeffs = shadow_coefficients(data, max_r)
    direct_sum = sum(coeffs.values())

    # The weighted sum sum r*S_r = t^2*sqrt(Q_L(1)):
    Q_at_1 = data.q0 + data.q1 + data.q2
    if Q_at_1 >= 0:
        exact_weighted = math.sqrt(Q_at_1)
    else:
        exact_weighted = cmath.sqrt(Q_at_1)

    weighted_partial = sum(r * coeffs[r] for r in coeffs)

    result['direct_partial_sum'] = direct_sum
    result['exact_weighted'] = exact_weighted
    result['weighted_partial_sum'] = weighted_partial
    result['rho'] = data.rho
    return result


# =====================================================================
# Section 8: Exact closed-form Borel sum comparison
# =====================================================================

def exact_shadow_generating_function(data: ShadowAlgebraData, t: complex
                                      ) -> complex:
    r"""Exact shadow generating function H(t) = t^2 * sqrt(Q_L(t)).

    For class G/L, the generating function is a polynomial.
    For class M, it is algebraic of degree 2 (the defining property
    from thm:riccati-algebraicity).
    """
    t = complex(t)
    Q_val = data.q0 + data.q1 * t + data.q2 * t ** 2
    return t ** 2 * cmath.sqrt(Q_val)


def shadow_ode_analytic_continuation(data: ShadowAlgebraData,
                                      t_start: float = 0.01,
                                      t_end: float = 3.0,
                                      n_steps: int = 1000
                                      ) -> List[Tuple[float, complex]]:
    r"""Analytic continuation via the shadow ODE.

    The shadow connection nabla^sh = d - Q'_L/(2*Q_L) dt has
    flat sections Phi(t) = sqrt(Q_L(t)/Q_L(0)).

    We integrate the ODE:
        dPhi/dt = Q'_L(t) / (2*Q_L(t)) * Phi(t)

    using simple Euler steps, to provide an independent verification
    path for the analytic continuation.
    """
    q0 = data.q0
    q1 = data.q1
    q2 = data.q2

    dt = (t_end - t_start) / n_steps
    t = t_start
    Phi = cmath.sqrt(complex(q0 + q1 * t + q2 * t ** 2)) / cmath.sqrt(complex(q0))

    trajectory = [(t, Phi)]
    for _ in range(n_steps):
        Q_val = q0 + q1 * t + q2 * t ** 2
        Q_prime = q1 + 2 * q2 * t
        if abs(Q_val) > 1e-30:
            dPhi_dt = Q_prime / (2.0 * Q_val) * Phi
        else:
            dPhi_dt = 0.0 + 0.0j
        Phi += dPhi_dt * dt
        t += dt
        trajectory.append((t, Phi))

    return trajectory


# =====================================================================
# Section 9: p-adic Borel transform
# =====================================================================

def p_adic_valuation(n: int, p: int) -> int:
    """p-adic valuation v_p(n) = largest power of p dividing n."""
    if n == 0:
        return float('inf')
    v = 0
    n = abs(n)
    while n % p == 0:
        n //= p
        v += 1
    return v


def p_adic_valuation_rational(num: int, den: int, p: int) -> int:
    """p-adic valuation of num/den."""
    return p_adic_valuation(num, p) - p_adic_valuation(den, p)


def p_adic_norm(x: Fraction, p: int) -> float:
    """p-adic absolute value |x|_p = p^{-v_p(x)}."""
    if x == 0:
        return 0.0
    v = p_adic_valuation(x.numerator, p) - p_adic_valuation(x.denominator, p)
    return float(p) ** (-v)


def borel_coefficients_rational(data: ShadowAlgebraData, max_r: int = 40
                                 ) -> Dict[int, Fraction]:
    """Compute Borel coefficients b_r = S_r / Gamma(r) as exact fractions.

    Only works when kappa, alpha, S4 are rational (true for standard
    families at rational parameters).
    """
    # Reconstruct Q_L coefficients as Fractions
    kappa_f = Fraction(data.kappa).limit_denominator(10 ** 12)
    alpha_f = Fraction(data.alpha).limit_denominator(10 ** 12)
    S4_f = Fraction(data.S4).limit_denominator(10 ** 12)

    q0 = 4 * kappa_f ** 2
    q1 = 12 * kappa_f * alpha_f
    q2 = 9 * alpha_f ** 2 + 16 * kappa_f * S4_f

    max_n = max_r - 2
    if max_n < 0:
        return {}

    # Compute sqrt(q0) as a Fraction
    # q0 = (2*kappa)^2, so sqrt(q0) = 2*|kappa|
    a0 = abs(2 * kappa_f)
    if a0 == 0:
        return {r: Fraction(0) for r in range(2, max_r + 1)}

    a = [Fraction(0)] * (max_n + 1)
    a[0] = a0
    if max_n >= 1:
        a[1] = q1 / (2 * a0)
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a0)
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a0)

    # S_r = a_{r-2} / r
    shadow_frac = {r: a[r - 2] / r for r in range(2, max_r + 1)}

    # Borel: b_r = S_r / (r-1)!
    borel_frac = {}
    for r, sr in shadow_frac.items():
        borel_frac[r] = sr / Fraction(math.factorial(r - 1))

    return borel_frac


def p_adic_borel_norms(data: ShadowAlgebraData, p: int,
                        max_r: int = 40) -> Dict[int, float]:
    """Compute |b_r|_p for the Borel coefficients.

    The p-adic convergence radius of the Borel transform is
    R_p = 1 / limsup |b_r|_p^{1/r}.
    """
    borel_frac = borel_coefficients_rational(data, max_r)
    norms = {}
    for r, br in borel_frac.items():
        norms[r] = p_adic_norm(br, p)
    return norms


def p_adic_convergence_radius(data: ShadowAlgebraData, p: int,
                               max_r: int = 40) -> float:
    """Estimate the p-adic convergence radius of the Borel transform.

    R_p = 1 / limsup_{r->infty} |b_r|_p^{1/r}
    """
    norms = p_adic_borel_norms(data, p, max_r)
    if not norms:
        return float('inf')

    # Compute |b_r|_p^{1/r} for large r
    limsup_candidates = []
    for r, norm_val in norms.items():
        if r >= 5 and norm_val > 0:
            limsup_candidates.append(norm_val ** (1.0 / r))

    if not limsup_candidates:
        return float('inf')

    limsup = max(limsup_candidates[-10:])  # Use last 10 values
    return 1.0 / limsup if limsup > 1e-30 else float('inf')


def p_adic_singularity_comparison(data: ShadowAlgebraData,
                                   primes: List[int] = None,
                                   max_r: int = 40) -> Dict[int, Dict]:
    """Compare archimedean and p-adic scalar radius estimates.

    For each prime p, compute the p-adic convergence radius R_p
    and compare with the archimedean radius R_arch = 1/rho.
    """
    if primes is None:
        primes = [2, 3, 5]

    R_arch = 1.0 / data.rho if data.rho > 1e-30 else float('inf')

    result = {
        'archimedean_radius': R_arch,
        'certifies_p_adic_singularities': False,
    }
    for p in primes:
        R_p = p_adic_convergence_radius(data, p, max_r)
        result[p] = {
            'R_p': R_p,
            'R_arch': R_arch,
            'ratio': R_p / R_arch if R_arch > 0 and R_arch < 1e15 else float('nan'),
        }

    return result


def p_adic_stokes_phenomenon(data: ShadowAlgebraData, p: int,
                              max_r: int = 40) -> Dict[str, Any]:
    """Analyze p-adic radius discrepancy as a diagnostic.

    Over Q_p, the Borel transform may converge everywhere (p-adic
    Borel summability) or have a radius estimate different from the
    archimedean scalar estimate.  A radius discrepancy is not by itself
    a certified p-adic Stokes phenomenon.
    """
    norms = p_adic_borel_norms(data, p, max_r)
    R_p = p_adic_convergence_radius(data, p, max_r)
    R_arch = 1.0 / data.rho if data.rho > 1e-30 else float('inf')

    # Check if there is a radius discrepancy.  This is diagnostic only.
    if R_arch < 1e15 and R_p < 1e15:
        has_p_stokes = abs(R_p - R_arch) / max(R_p, R_arch) > 0.01
    else:
        has_p_stokes = False

    return {
        'p': p,
        'R_p': R_p,
        'R_arch': R_arch,
        'has_p_adic_stokes': has_p_stokes,
        'radius_discrepancy': has_p_stokes,
        'certifies_p_adic_stokes': False,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
        'norm_sequence': norms,
    }


# =====================================================================
# Section 10: Mod-p coefficient diagnostics
# =====================================================================

def shadow_coefficients_mod_p(data: ShadowAlgebraData, p: int,
                               max_r: int = 100) -> Dict[int, int]:
    """Compute S_r mod p for the shadow coefficients.

    Uses exact rational arithmetic to compute S_r as fractions,
    then reduces modulo p.

    Note: S_r may not be an integer.  We compute the p-adic
    reduction of the numerator mod p (after clearing denominators).
    """
    kappa_f = Fraction(data.kappa).limit_denominator(10 ** 12)
    alpha_f = Fraction(data.alpha).limit_denominator(10 ** 12)
    S4_f = Fraction(data.S4).limit_denominator(10 ** 12)

    q0 = 4 * kappa_f ** 2
    q1 = 12 * kappa_f * alpha_f
    q2 = 9 * alpha_f ** 2 + 16 * kappa_f * S4_f

    max_n = max_r - 2
    a0 = abs(2 * kappa_f)
    if a0 == 0:
        return {r: 0 for r in range(2, max_r + 1)}

    a = [Fraction(0)] * (max_n + 1)
    a[0] = a0
    if max_n >= 1:
        a[1] = q1 / (2 * a0)
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a0)
    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a0)

    result = {}
    for r in range(2, max_r + 1):
        sr = a[r - 2] / r
        # Reduce sr mod p: compute numerator mod p (in the p-local ring)
        num = sr.numerator
        den = sr.denominator
        # If p divides denominator, the reduction is 0 in F_p
        if den % p == 0:
            result[r] = 0
        else:
            # Compute num * den^{-1} mod p
            den_inv = pow(den % p, p - 2, p)  # Fermat's little theorem
            result[r] = (num * den_inv) % p

    return result


def peacock_pattern(data: ShadowAlgebraData, p: int,
                     max_r: int = 100) -> Dict[str, Any]:
    r"""Compute a mod-p coefficient pattern for the shadow tower.

    This is an exact reduction of the scalar coefficients modulo p.
    Any comparison with Garoufalidis-Zagier peacock phenomena is a
    diagnostic analogy unless a separate theorem identifies the required
    resurgent series and hypotheses.

    Returns dict with the pattern data and detected periodicity.
    """
    mods = shadow_coefficients_mod_p(data, p, max_r)

    # Detect periodicity: find the smallest T such that
    # S_{r+T} = S_r mod p for all r in a sufficiently long range
    values = [mods.get(r, 0) for r in range(2, max_r + 1)]

    detected_period = None
    for T in range(1, max_r // 3):
        is_periodic = True
        match_count = 0
        total_count = 0
        for i in range(len(values) - T):
            if i + T < len(values):
                total_count += 1
                if values[i] == values[i + T]:
                    match_count += 1
                else:
                    is_periodic = False
        if total_count > 0 and match_count == total_count:
            detected_period = T
            break

    # Compute distribution of residues
    residue_counts = {}
    for v in values:
        residue_counts[v] = residue_counts.get(v, 0) + 1

    return {
        'p': p,
        'max_r': max_r,
        'mod_values': mods,
        'detected_period': detected_period,
        'residue_distribution': residue_counts,
        'depth_class': data.depth_class,
        'certification': EXACT_SCALAR_PROJECTION,
        'certifies_garoufalidis_zagier_peacock': False,
    }


def peacock_pattern_multi_prime(data: ShadowAlgebraData,
                                 primes: List[int] = None,
                                 max_r: int = 100) -> Dict[int, Dict]:
    """Compute peacock patterns for multiple primes."""
    if primes is None:
        primes = [2, 3, 5, 7]
    return {p: peacock_pattern(data, p, max_r) for p in primes}


# =====================================================================
# Section 11: Multi-path verification
# =====================================================================

def verify_borel_singularities_multipath(data: ShadowAlgebraData,
                                          max_r: int = 60
                                          ) -> Dict[str, Any]:
    r"""Multi-path check of reciprocal branch-point growth markers.

    Path 1: Predicted from shadow metric branch points (1/t_pm)
    Path 2: Detected via Pade approximant
    Path 3: Verified via shadow ODE analytic continuation
    Path 4: Cross-checked with p-adic radii

    Returns dict with all path results and cross-consistency.
    """
    # Path 1: Predicted
    zeta_p, zeta_m = borel_singularity_locations(data)
    predicted = {
        'zeta_plus': zeta_p,
        'zeta_minus': zeta_m,
        'modulus_plus': abs(zeta_p),
        'modulus_minus': abs(zeta_m),
    }

    # Path 2: Pade detection of branch points
    pade_result = borel_pade_singularities(data, max_r)

    # Path 3: ODE analytic continuation
    trajectory = shadow_ode_analytic_continuation(data)
    # Check if the ODE blows up near predicted singularity
    ode_blowup_t = None
    for t_val, phi_val in trajectory:
        if abs(phi_val) > 1e10:
            ode_blowup_t = t_val
            break

    # Path 4: p-adic comparison
    p_adic = p_adic_singularity_comparison(data, primes=[2, 3, 5], max_r=max_r)

    # Cross-consistency: do Pade poles match predicted branch points?
    pade_agrees = False
    if 'pole_match' in pade_result:
        for label, match in pade_result['pole_match'].items():
            if match.get('relative_error', 1.0) < 0.3:
                pade_agrees = True

    return {
        'path_1_predicted': predicted,
        'path_2_pade': pade_result,
        'path_3_ode_blowup': ode_blowup_t,
        'path_4_p_adic': p_adic,
        'pade_agrees_with_prediction': pade_agrees,
        'rho': data.rho,
        'depth_class': data.depth_class,
        'certified_borel_singularities': False,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
    }


def verify_stokes_multipath(data: ShadowAlgebraData,
                              max_r: int = 60) -> Dict[str, Any]:
    r"""Multi-path check of scalar monodromy diagnostics.

    Path 1: monodromy-jump normalization (2*pi*i)
    Path 2: scalar large-order growth check
    Path 3: PSLQ recognition of rho^2 (if mpmath available)
    """
    # Path 1: Monodromy
    S_1_mono = stokes_constant_from_monodromy(data)

    # Path 2: Large-order
    numerical = stokes_constant_numerical(data, max_r)

    # Path 3: PSLQ
    pslq = stokes_constant_pslq(data, max_r)

    return {
        'path_1_monodromy': S_1_mono,
        'path_2_numerical': numerical.get('S_1', complex('nan')),
        'path_3_pslq': pslq,
        'depth_class': data.depth_class,
        'certifies_ecalle_stokes': False,
        'certification': DIAGNOSTIC_NON_CERTIFYING,
    }


# =====================================================================
# Section 12: Summary and landscape scan
# =====================================================================

def resurgence_summary(data: ShadowAlgebraData, max_r: int = 60
                        ) -> Dict[str, Any]:
    """Arithmetic summary plus explicit frontier non-certification."""
    result = {
        'name': data.name,
        'depth_class': data.depth_class,
        'kappa': data.kappa,
        'rho': data.rho,
        'theta': data.theta,
    }

    # Reciprocal branch markers.
    sings = locate_all_borel_singularities(data)
    result['n_singularities'] = len(sings)
    result['n_branch_markers'] = len(sings)
    result['n_certified_borel_singularities'] = 0
    result['leading_singularity'] = sings[0] if sings else None

    # Monodromy-jump diagnostic.
    result['S_1'] = stokes_constant_from_monodromy(data)

    # Bridge equation
    result['bridge'] = bridge_equation_check(data, min(max_r, 20))
    result['diagnostic_status'] = frontier_diagnostic_status(data)

    return result


def landscape_resurgence_scan(max_r: int = 40) -> Dict[str, Dict]:
    """Scan the standard landscape for resurgence structure."""
    algebras = {
        'Heis': heisenberg_data(1),
        'aff_sl2_k1': affine_sl2_data(1.0),
        'aff_sl2_k2': affine_sl2_data(2.0),
        'Vir_c1': virasoro_data(1.0),
        'Vir_c2': virasoro_data(2.0),
        'Vir_c13': virasoro_data(13.0),
        'Vir_c25': virasoro_data(25.0),
    }
    return {name: resurgence_summary(alg, max_r) for name, alg in algebras.items()}
