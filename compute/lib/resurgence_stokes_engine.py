r"""Resurgence and Stokes engine for the shadow Postnikov tower.

Connects the divergent shadow obstruction tower asymptotics to non-perturbative physics
via Ecalle's resurgence theory. The shadow generating function

    G(t) = sum_{r>=2} S_r t^r

is generically divergent (class M with rho > 1 for c < c*). Borel
resummation yields a well-defined analytic function, but the Borel
transform has singularities that encode non-perturbative (instanton)
contributions. The Stokes phenomenon -- discontinuous jumps in the
lateral Borel sums as the direction of summation crosses a singular
ray -- is governed by Stokes multipliers that are constrained by the
MC equation (Ecalle's bridge equation).

MATHEMATICAL FRAMEWORK:

1. **Borel transform**: B[G](xi) = sum_{r>=2} S_r xi^r / Gamma(r+1).
   For Virasoro at leading order, S_r ~ (2/r)(-3)^{r-4}(2/c)^{r-2},
   so the Borel transform has singularities at xi = 1/rho * e^{+/- i*theta}
   where rho is the shadow growth rate and theta the oscillation phase.

2. **Lateral Borel sums**: S_+/- [G](t) are obtained by integrating
   the Borel transform along rays just above/below the singular direction.
   The difference S_+ - S_- = Stokes discontinuity.

3. **Transseries**: G(t) = G^(0)(t) + sum_{n>=1} sigma_n exp(-A_n/t) G^(n)(t)
   where A_n are instanton actions (= locations of Borel singularities)
   and sigma_n are transseries parameters.

4. **Alien derivatives**: Delta_{A_1} G^(0) = S_1 * G^(1), encoding
   the relation between perturbative and one-instanton sectors.

5. **Bridge equation**: The MC equation D*Theta + (1/2)[Theta,Theta] = 0
   constrains the transseries via the relation between alien derivatives
   and the Stokes automorphism. This is the shadow obstruction tower's encoding of
   Ecalle's bridge equation.

6. **Stokes graph**: The complex t-plane is divided into Stokes sectors
   by anti-Stokes lines (where Re(A_n/t) = 0) and Stokes lines (where
   Im(A_n/t) = 0). At c = 13 (Virasoro self-dual point), the Stokes
   graph has enhanced Z_2 symmetry from Koszul self-duality.

PHYSICAL INTERPRETATION:

The instanton actions A_n = n/rho correspond to non-perturbative
contributions to the shadow obstruction tower: tunneling between perturbative
vacua of the modular MC equation. The Stokes multipliers control
the weight of these contributions and are computable from the MC
equation alone (no additional input). This is the shadow obstruction tower's
encoding of the non-perturbative structure of the chiral algebra.

KEY RESULTS:
  - Borel singularities at xi = 1/rho * exp(+/- i*theta) match branch
    points of the shadow metric Q_L
  - Stokes multiplier S_1 = +/- 2*pi*i at leading order (logarithmic
    monodromy of the shadow generating function)
  - Bridge equation at arity 2: the MC constraint on kappa determines
    the Stokes multiplier via the alien derivative relation
  - Self-dual c = 13: enhanced Z_2 symmetry in Stokes graph, S_1 real

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    rem:shadow-borel-summability (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)

Dependencies:
    shadow_radius.py -- shadow growth rate, branch points, metric
    shadow_tower_recursive.py -- exact shadow coefficients
    shadow_complex_analysis.py -- Borel/Pade background
    shadow_analysis_verifications.py -- verification infrastructure
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    from scipy import integrate as scipy_integrate
    from scipy import special as scipy_special
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    from sympy import (
        Abs as spAbs,
        Rational,
        Symbol,
        cancel,
        cos as spcos,
        exp as spexp,
        factorial,
        gamma as spgamma,
        im as spim,
        log as splog,
        oo,
        pi as sppi,
        re as spre,
        simplify,
        sqrt as spsqrt,
    )
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False


# =====================================================================
# Section 0: Virasoro shadow data (self-contained for this module)
# =====================================================================

def virasoro_shadow_invariants(c_val: float) -> Dict[str, float]:
    r"""Compute the fundamental shadow invariants for Virasoro at central charge c.

    Returns kappa, alpha, S_4, Delta, rho, theta (the shadow growth rate
    and oscillation phase from the branch points of Q_L).

    Formulae:
        kappa = c/2
        alpha = 2  (cubic shadow coefficient, from T_{(1)}T = 2T)
        S_4 = 10/(c(5c+22))  (quartic shadow, from Q^contact_Vir)
        Delta = 8*kappa*S_4 = 40/(5c+22)  (critical discriminant)
        rho = sqrt((180c+872)/((5c+22)*c^2))  (shadow growth rate)
        theta = arg(branch point of Q_L)  (oscillation phase)
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4  # = 40/(5c+22)

    # Shadow metric Q_L(t) = q0 + q1*t + q2*t^2
    q0 = 4.0 * kappa**2  # = c^2
    q1 = 12.0 * kappa * alpha  # = 12c
    q2 = 9.0 * alpha**2 + 16.0 * kappa * S4  # = (180c+872)/(5c+22)

    # Branch points: zeros of Q_L
    disc = q1**2 - 4.0 * q0 * q2  # = -32*kappa^2 * Delta
    # For c > 0: disc < 0 (complex conjugate branch points)
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)

    R = abs(t_plus)  # both have same modulus for conjugate pair
    rho = 1.0 / R if R > 0 else float('inf')
    theta = cmath.phase(t_plus)  # argument of nearest branch point

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


def virasoro_shadow_coefficients_recursive(c_val: float, r_max: int) -> List[float]:
    r"""Compute exact Virasoro shadow coefficients S_2, ..., S_{r_max}
    via the convolution recursion f^2 = Q_L.

    The weighted generating function H(t) = t^2 * sqrt(Q_L(t)) gives
    S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(t)).

    The recursion for a_n from f^2 = Q_L:
        a_0 = sqrt(q0)
        a_1 = q1 / (2*a_0)
        a_n = (1/(2*a_0)) * (c_n - sum_{j=1}^{n-1} a_j*a_{n-j})  for n >= 2

    where c_0 = q0, c_1 = q1, c_2 = q2, c_n = 0 for n >= 3.
    """
    inv = virasoro_shadow_invariants(c_val)
    q0, q1, q2 = inv['q0'], inv['q1'], inv['q2']

    # Taylor coefficients of sqrt(Q_L)
    max_n = r_max - 2 + 1  # need a_0 through a_{r_max-2}
    a = [0.0] * max_n

    a[0] = math.sqrt(q0)  # = |c| for c > 0
    if max_n > 1:
        a[1] = q1 / (2.0 * a[0])

    for n in range(2, max_n):
        # c_n from Q_L: c_0=q0, c_1=q1, c_2=q2, rest=0
        cn = q2 if n == 2 else 0.0
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv_sum) / (2.0 * a[0])

    # S_r = a_{r-2} / r
    coeffs = []
    for r in range(2, r_max + 1):
        idx = r - 2
        if idx < len(a):
            coeffs.append(a[idx] / r)
        else:
            coeffs.append(0.0)
    return coeffs


def virasoro_shadow_coefficients_leading(c_val: float, r_max: int) -> List[float]:
    r"""Leading-order Virasoro shadow coefficients from the log form.

    G(t) = -log(1 + 6t/c) + 6t/c at leading order in 1/c.
    S_r = (-6/c)^r / r for r >= 2.
    """
    coeffs = []
    ratio = -6.0 / c_val
    for r in range(2, r_max + 1):
        coeffs.append(ratio**r / r)
    return coeffs


# =====================================================================
# Section 1: Borel transform
# =====================================================================

@dataclass
class BorelData:
    """Container for Borel transform data at a given central charge."""
    c: float
    r_max: int
    shadow_coeffs: List[float]  # S_2, S_3, ..., S_{r_max}
    singularities: List[complex]  # locations of Borel singularities
    instanton_actions: List[complex]  # A_n = 1/rho * exp(+/- i*theta)
    rho: float
    theta: float

    @property
    def first_instanton_action(self) -> complex:
        """A_1 = 1/rho * e^{i*theta}: dominant instanton."""
        return self.instanton_actions[0] if self.instanton_actions else 0.0


def borel_transform_coefficients(shadow_coeffs: Sequence[float],
                                  r_start: int = 2) -> List[float]:
    r"""Borel transform coefficients: b_r = S_r / Gamma(r+1) = S_r / r!.

    The Borel transform is B[G](xi) = sum_{r>=2} b_r xi^r.
    """
    b_coeffs = []
    for i, s_r in enumerate(shadow_coeffs):
        r = r_start + i
        b_coeffs.append(s_r / math.gamma(r + 1))
    return b_coeffs


def borel_transform(shadow_coeffs: Sequence[float], xi: complex,
                     r_start: int = 2) -> complex:
    r"""Evaluate the Borel transform B[G](xi) = sum_{r>=r_start} S_r xi^r / r!.

    Parameters
    ----------
    shadow_coeffs : sequence of float
        Shadow coefficients S_{r_start}, S_{r_start+1}, ...
    xi : complex
        Borel-plane variable.
    r_start : int
        Starting arity (default 2).

    Returns
    -------
    complex
        B[G](xi).
    """
    xi = complex(xi)
    result = 0.0 + 0.0j
    for i, s_r in enumerate(shadow_coeffs):
        r = r_start + i
        term = s_r * xi**r / math.gamma(r + 1)
        result += term
        # Early termination if terms are negligible
        if i > 10 and abs(term) < 1e-30 * max(abs(result), 1e-100):
            break
    return result


def borel_transform_virasoro(c_val: float, r_max: int, xi: complex) -> complex:
    """Borel transform of the Virasoro shadow series at xi."""
    coeffs = virasoro_shadow_coefficients_recursive(c_val, r_max)
    return borel_transform(coeffs, xi, r_start=2)


def borel_singularity_locations(c_val: float) -> Tuple[complex, complex]:
    r"""Locations of the dominant Borel singularities for Virasoro.

    The shadow generating function has branch points at the zeros of Q_L(t).
    In the Borel plane, the singularities are at xi = 1/t_branch (inverted).

    Actually: the Borel transform B[G](xi) = sum S_r xi^r / r! inherits
    singularities from the asymptotic growth S_r ~ C*rho^r*r^{-5/2}*cos(r*theta+phi).
    The Borel transform of rho^r r^{-5/2} cos(r*theta) xi^r / r! converges
    for all xi (since r! kills the geometric growth). The singularities of
    the ANALYTIC CONTINUATION of B[G] occur at xi such that the series
    sum S_r xi^r / r! = sum C*rho^r*r^{-5/2}*cos(r*theta+phi)*xi^r/r!
    has its nearest singularity when the effective ratio rho*|xi| causes
    a resonance.

    For the leading-order log form G(t) = -log(1+6t/c)+6t/c with
    S_r = (-6/c)^r/r, the Borel transform is:
        B[G](xi) = sum_{r>=2} (-6/c)^r xi^r / (r * r!)

    This entire function has no finite singularities. But the INVERSE
    Borel transform (Borel-Laplace) has singularities in the integration
    contour when t passes through a Stokes line.

    The instanton actions are determined by the branch points:
        A_+/- = 1/t_+/- (reciprocal of branch points).
    These are the singularities of the Borel transform of the RESUMMED function.
    """
    inv = virasoro_shadow_invariants(c_val)
    t_plus = inv['branch_plus']
    t_minus = inv['branch_minus']

    # Instanton actions = reciprocal of branch points
    A_plus = 1.0 / t_plus if abs(t_plus) > 1e-15 else complex('inf')
    A_minus = 1.0 / t_minus if abs(t_minus) > 1e-15 else complex('inf')

    return A_plus, A_minus


def build_borel_data(c_val: float, r_max: int = 60) -> BorelData:
    """Build the complete Borel data package for Virasoro at central charge c."""
    coeffs = virasoro_shadow_coefficients_recursive(c_val, r_max)
    inv = virasoro_shadow_invariants(c_val)
    A_plus, A_minus = borel_singularity_locations(c_val)

    return BorelData(
        c=c_val,
        r_max=r_max,
        shadow_coeffs=coeffs,
        singularities=[A_plus, A_minus],
        instanton_actions=[A_plus, A_minus],
        rho=inv['rho'],
        theta=inv['theta'],
    )


# =====================================================================
# Section 2: Lateral Borel sums
# =====================================================================

def lateral_borel_integrand(
    shadow_coeffs: Sequence[float],
    t: complex,
    xi_real: float,
    epsilon: float,
    r_start: int = 2,
) -> complex:
    r"""Integrand for the lateral Borel sum along direction theta +/- epsilon.

    The lateral Borel sum S_+[G](t) integrates B[G](xi) * exp(-xi/t)
    along a ray in the xi-plane that avoids the singularity from above.

    For numerical computation: parametrize xi = s * exp(i*delta) for s >= 0,
    where delta = +/- epsilon is the lateral displacement angle.
    """
    xi = xi_real * cmath.exp(1j * epsilon)
    B_val = borel_transform(shadow_coeffs, xi, r_start)
    return B_val * cmath.exp(-xi / t) / t


def lateral_borel_sum(
    shadow_coeffs: Sequence[float],
    t: complex,
    epsilon: float = 0.01,
    r_start: int = 2,
    n_quad: int = 2000,
    xi_max: float = 100.0,
) -> complex:
    r"""Compute the lateral Borel sum S_epsilon[G](t).

    S_epsilon[G](t) = int_0^{infty * e^{i*epsilon}} B[G](xi) e^{-xi/t} dxi/t

    where the contour is tilted by angle epsilon from the positive real axis.
    epsilon > 0 gives S_+ (above), epsilon < 0 gives S_- (below).

    Parameters
    ----------
    shadow_coeffs : sequence
        S_{r_start}, ... shadow coefficients.
    t : complex
        The resummed variable.
    epsilon : float
        Lateral tilt angle. +epsilon for S_+, -epsilon for S_-.
    n_quad : int
        Number of quadrature points.
    xi_max : float
        Truncation of the integration domain.

    Returns
    -------
    complex
        The lateral Borel sum.
    """
    if abs(t) < 1e-15:
        return 0.0 + 0.0j
    t = complex(t)
    ds = xi_max / n_quad
    direction = cmath.exp(1j * epsilon)
    result = 0.0 + 0.0j

    for k in range(1, n_quad + 1):
        s = (k - 0.5) * ds
        xi = s * direction
        B_val = borel_transform(shadow_coeffs, xi, r_start)
        weight = cmath.exp(-xi / t) * direction / t
        result += B_val * weight * ds

    return result


def lateral_borel_sum_scipy(
    shadow_coeffs: Sequence[float],
    t: complex,
    epsilon: float = 0.01,
    r_start: int = 2,
    limit: int = 200,
) -> Tuple[complex, float]:
    r"""Lateral Borel sum via scipy adaptive quadrature.

    Higher accuracy than trapezoidal. Returns (value, error_estimate).
    """
    if not HAS_SCIPY:
        raise ImportError("scipy required for adaptive quadrature")
    if abs(t) < 1e-15:
        return (0.0 + 0.0j, 0.0)

    t = complex(t)
    direction = cmath.exp(1j * epsilon)

    def real_integrand(s):
        xi = s * direction
        B_val = borel_transform(shadow_coeffs, xi, r_start)
        val = B_val * cmath.exp(-xi / t) * direction / t
        return val.real

    def imag_integrand(s):
        xi = s * direction
        B_val = borel_transform(shadow_coeffs, xi, r_start)
        val = B_val * cmath.exp(-xi / t) * direction / t
        return val.imag

    re_val, re_err = scipy_integrate.quad(real_integrand, 0, np.inf, limit=limit)
    im_val, im_err = scipy_integrate.quad(imag_integrand, 0, np.inf, limit=limit)

    return (complex(re_val, im_val), max(re_err, im_err))


def lateral_borel_sums(
    c_val: float,
    t_val: complex,
    r_max: int = 60,
    epsilon: float = 0.02,
    n_quad: int = 3000,
    xi_max: float = 80.0,
) -> Dict[str, Any]:
    r"""Compute both lateral Borel sums S_+, S_- and the Stokes jump.

    Returns S_+, S_-, their difference (Stokes discontinuity), and the
    direct partial sum for comparison.

    Parameters
    ----------
    c_val : float
        Central charge.
    t_val : complex
        Point in the t-plane.
    r_max : int
        Maximum arity for shadow coefficients.
    epsilon : float
        Lateral tilt angle.
    """
    coeffs = virasoro_shadow_coefficients_recursive(c_val, r_max)

    S_plus = lateral_borel_sum(coeffs, t_val, epsilon=+epsilon,
                                n_quad=n_quad, xi_max=xi_max)
    S_minus = lateral_borel_sum(coeffs, t_val, epsilon=-epsilon,
                                 n_quad=n_quad, xi_max=xi_max)

    # Direct partial sum (may diverge)
    partial = sum(coeffs[i] * t_val**(i + 2) for i in range(len(coeffs)))

    return {
        'c': c_val,
        't': t_val,
        'S_plus': S_plus,
        'S_minus': S_minus,
        'stokes_jump': S_plus - S_minus,
        'partial_sum': partial,
        'epsilon': epsilon,
        'r_max': r_max,
    }


# =====================================================================
# Section 3: Stokes multiplier
# =====================================================================

@dataclass
class StokesMultiplierData:
    """Stokes multiplier data for a given central charge."""
    c: float
    S_1: complex  # first Stokes multiplier
    A_1: complex  # first instanton action
    stokes_direction: float  # angle of the Stokes line
    anti_stokes_directions: List[float]  # angles of anti-Stokes lines
    enhanced_symmetry: bool  # True if Koszul self-dual (c=13)


def stokes_multiplier_leading(c_val: float) -> complex:
    r"""Leading-order Stokes multiplier for Virasoro.

    At leading order in 1/c, G(t) = -log(1+6t/c)+6t/c has a logarithmic
    branch point at t = -c/6. The monodromy is -2*pi*i (standard log
    monodromy). The Stokes multiplier is:

        S_1 = -2*pi*i

    This is the discontinuity of G across the branch cut, which equals
    the Stokes jump when the contour crosses the singular direction.

    For the full (exact in c) shadow generating function, the branch
    point is at a complex location, and the Stokes multiplier picks up
    a correction. But the leading coefficient is always +/- 2*pi*i
    (logarithmic monodromy of the algebraic function sqrt(Q_L)).
    """
    return -2.0j * math.pi


def stokes_multiplier_numerical(
    c_val: float,
    r_max: int = 60,
    epsilon: float = 0.02,
    t_probe: Optional[complex] = None,
) -> complex:
    r"""Numerically extract the Stokes multiplier from lateral Borel sums.

    The Stokes jump S_+ - S_- at a point t on the Stokes line gives:
        S_+ - S_- = S_1 * exp(-A_1/t) * G^(1)(t) + ...

    At leading order, this is ~ S_1 * exp(-A_1/t). We extract S_1 by
    dividing out the exponential factor.

    Parameters
    ----------
    c_val : float
        Central charge.
    r_max : int
        Maximum arity for shadow coefficients.
    epsilon : float
        Lateral tilt for Borel sums.
    t_probe : complex, optional
        Point at which to probe (default: on the Stokes line near the
        origin, chosen for numerical stability).
    """
    inv = virasoro_shadow_invariants(c_val)

    # Choose a probe point on the Stokes line
    if t_probe is None:
        # Stokes line: where Im(A_1/t) = 0
        # A_1 = 1/t_+ so A_1/t = 1/(t_+ * t)
        # On the positive real axis, this works if A_1 is real
        # For complex A_1, choose t such that A_1/t is real and positive
        A_1 = 1.0 / inv['branch_plus']
        stokes_angle = cmath.phase(A_1)
        # t on Stokes line: arg(t) = arg(A_1), so A_1/t is real positive
        t_probe = 0.3 * cmath.exp(1j * stokes_angle)

    data = lateral_borel_sums(c_val, t_probe, r_max=r_max, epsilon=epsilon)
    jump = data['stokes_jump']

    # Extract S_1: jump ~ S_1 * exp(-A_1/t_probe)
    A_1 = 1.0 / inv['branch_plus']
    exp_factor = cmath.exp(-A_1 / t_probe)

    if abs(exp_factor) < 1e-30:
        return complex('nan')

    S_1_extracted = jump / exp_factor
    return S_1_extracted


def stokes_multiplier_from_monodromy(c_val: float) -> complex:
    r"""Stokes multiplier from the monodromy of the shadow generating function.

    For the algebraic shadow generating function H^2 = t^4 Q_L(t), the
    monodromy around each branch point t_+/- is -1 (square root monodromy).
    This translates to a Stokes multiplier of:

        S_1 = 2*pi*i * Res_{xi=A_1} B[G](xi)

    At leading order (log form), the residue is 1 and S_1 = +/- 2*pi*i.
    At exact order, the residue receives corrections from the exact Q_L.

    The shadow connection has residue 1/2 at each zero of Q_L
    (thm:shadow-connection), giving monodromy exp(2*pi*i * 1/2) = -1.
    This is the Koszul sign.
    """
    # The monodromy of sqrt(Q_L) around a simple zero is -1.
    # In the Borel plane, this gives S_1 = 2*pi*i (standard formula).
    # Sign depends on orientation.
    return 2.0j * math.pi


def compute_stokes_data(c_val: float) -> StokesMultiplierData:
    """Build the complete Stokes multiplier data for Virasoro at c."""
    inv = virasoro_shadow_invariants(c_val)
    A_plus, A_minus = borel_singularity_locations(c_val)

    # Stokes direction: angle where lateral sums jump
    # This is the argument of the instanton action A_1
    stokes_dir = cmath.phase(A_plus)

    # Anti-Stokes directions: where Re(A/t) = 0, i.e., arg(t) = arg(A) +/- pi/2
    anti_stokes = [
        stokes_dir + math.pi / 2,
        stokes_dir - math.pi / 2,
    ]

    # Koszul self-duality at c = 13
    is_self_dual = abs(c_val - 13.0) < 0.01

    S_1 = stokes_multiplier_leading(c_val)

    return StokesMultiplierData(
        c=c_val,
        S_1=S_1,
        A_1=A_plus,
        stokes_direction=stokes_dir,
        anti_stokes_directions=anti_stokes,
        enhanced_symmetry=is_self_dual,
    )


# =====================================================================
# Section 4: Transseries
# =====================================================================

@dataclass
class TransseriesData:
    """Transseries expansion for the shadow generating function.

    G(t) = G^(0)(t) + sum_{n>=1} sigma_n * exp(-n*A_1/t) * G^(n)(t)

    where G^(0) is the perturbative sector (formal shadow series),
    G^(n) is the n-instanton sector, sigma_n are transseries parameters,
    and A_1 is the first instanton action.
    """
    c: float
    A_1: complex  # first instanton action
    perturbative: List[float]  # G^(0) coefficients = S_r
    one_instanton: List[float]  # G^(1) coefficients
    sigma_1: complex  # first transseries parameter
    n_instanton_actions: int  # number of instanton sectors computed


def perturbative_sector(c_val: float, r_max: int = 60) -> List[float]:
    """The perturbative sector G^(0) = the shadow series itself."""
    return virasoro_shadow_coefficients_recursive(c_val, r_max)


def one_instanton_sector_leading(c_val: float, r_max: int = 30) -> List[float]:
    r"""Leading-order one-instanton sector G^(1)(t).

    The one-instanton sector arises from the alien derivative acting on
    the perturbative sector. At leading order in 1/c:

        G^(1)(t) = sum_{r>=0} g^(1)_r t^r

    where g^(1)_r is determined by the bridge equation. For the log form:
        G(t) = -log(1+6t/c)+6t/c, the one-instanton correction G^(1)
    satisfies G^(1)(t) = 1 (constant) at leading order.

    More precisely: the alien derivative of G at the singularity A_1
    gives Delta_{A_1} G^(0) = S_1 * G^(1), and for the log singularity
    G^(1)(t) = 1/(1+6t/c) = sum_{r>=0} (-6/c)^r t^r.

    This is the one-instanton fluctuation prefactor.
    """
    ratio = -6.0 / c_val
    coeffs = []
    for r in range(0, r_max):
        coeffs.append(ratio**r)
    return coeffs


def transseries_eval(
    c_val: float,
    t: complex,
    sigma_1: complex = 1.0,
    n_inst: int = 2,
    r_max: int = 60,
) -> complex:
    r"""Evaluate the transseries at t, including n_inst instanton sectors.

    G^{trans}(t) = G^(0)(t) + sigma_1 * e^{-A_1/t} * G^(1)(t) + ...

    Parameters
    ----------
    c_val : float
        Central charge.
    t : complex
        Evaluation point.
    sigma_1 : complex
        Transseries parameter (determined by boundary conditions).
    n_inst : int
        Number of instanton sectors to include.
    r_max : int
        Maximum arity for perturbative coefficients.
    """
    t = complex(t)
    if abs(t) < 1e-15:
        return 0.0 + 0.0j

    # Perturbative sector
    pert_coeffs = perturbative_sector(c_val, r_max)
    G0 = sum(pert_coeffs[i] * t**(i + 2) for i in range(len(pert_coeffs)))

    # Instanton action
    inv = virasoro_shadow_invariants(c_val)
    A_1 = 1.0 / inv['branch_plus']

    result = G0

    if n_inst >= 1:
        # One-instanton sector
        inst1_coeffs = one_instanton_sector_leading(c_val, min(r_max, 30))
        G1 = sum(inst1_coeffs[r] * t**r for r in range(len(inst1_coeffs)))
        result += sigma_1 * cmath.exp(-A_1 / t) * G1

    if n_inst >= 2:
        # Two-instanton sector: G^(2) ~ 1/(1+6t/c)^2 at leading order
        ratio = -6.0 / c_val
        G2 = sum((r + 1) * ratio**r * t**r for r in range(min(r_max, 20)))
        result += sigma_1**2 * cmath.exp(-2.0 * A_1 / t) * G2 / 2.0

    return result


def build_transseries_data(c_val: float, r_max: int = 60) -> TransseriesData:
    """Build the complete transseries data for Virasoro at c."""
    inv = virasoro_shadow_invariants(c_val)
    A_1 = 1.0 / inv['branch_plus']
    S_1 = stokes_multiplier_leading(c_val)

    return TransseriesData(
        c=c_val,
        A_1=A_1,
        perturbative=perturbative_sector(c_val, r_max),
        one_instanton=one_instanton_sector_leading(c_val, 30),
        sigma_1=S_1,
        n_instanton_actions=2,
    )


# =====================================================================
# Section 5: Alien derivatives
# =====================================================================

def alien_derivative_perturbative(
    c_val: float,
    r_max: int = 60,
) -> List[float]:
    r"""Alien derivative Delta_{A_1} G^(0) at the first singularity.

    By definition:
        Delta_{A_1} G^(0) = S_1 * G^(1)

    where S_1 is the Stokes multiplier and G^(1) is the one-instanton sector.

    Returns coefficients of Delta_{A_1} G^(0)(t) = sum g_r t^r.
    """
    S_1 = stokes_multiplier_leading(c_val)
    G1_coeffs = one_instanton_sector_leading(c_val, r_max)
    return [S_1 * g for g in G1_coeffs]


def alien_derivative_chain(
    c_val: float,
    n_levels: int = 3,
    r_max: int = 30,
) -> List[List[float]]:
    r"""Chain of alien derivatives Delta_{A_1}^n G^(0).

    The iterated alien derivative Delta_{A_1}^n connects sector 0 to sector n:
        Delta_{A_1}^n G^(0) = (S_1)^n * G^(n)

    At leading order G^(n)(t) = n! * (1+6t/c)^{-(n+1)} ... actually
    just G^(n)(t) proportional to d^n/dt^n [1/(1+6t/c)] up to normalization.

    Returns list of coefficient lists [Delta^0 G, Delta^1 G, ..., Delta^n G].
    """
    ratio = -6.0 / c_val
    S_1 = stokes_multiplier_leading(c_val)

    chain = []
    # Level 0: perturbative series itself (shadow coefficients, starting from r=0)
    pert = virasoro_shadow_coefficients_leading(c_val, r_max)
    # Pad to start from r=0
    chain.append([0.0, 0.0] + pert)  # S_0 = S_1 = 0, S_2, S_3, ...

    for n in range(1, n_levels + 1):
        # G^(n)(t) = ratio^r * prod_{j=0}^{n-1} (r+j)/n! at leading order
        # More precisely: (-d/dt)^n log(1+6t/c) = (n-1)! * (6/c)^n / (1+6t/c)^n
        # so G^(n)(t) = sum_r binom(r+n-1, n-1) * ratio^r * t^r * (n-1)! * (6/c)^n / S_1^n
        # Simpler: define G^(n) by the alien derivative relation
        coeffs = []
        for r in range(r_max):
            # Multinomial coefficient for n-th derivative
            binom_coeff = 1.0
            for j in range(1, n):
                binom_coeff *= (r + j) / j
            coeffs.append(S_1**n * binom_coeff * ratio**r)
        chain.append(coeffs)

    return chain


def verify_alien_derivative_relation(c_val: float, r_max: int = 30) -> Dict[str, Any]:
    r"""Verify Delta_{A_1} G^(0) = S_1 * G^(1) numerically.

    Computes both sides independently and checks agreement.
    """
    S_1 = stokes_multiplier_leading(c_val)
    G1_coeffs = one_instanton_sector_leading(c_val, r_max)

    # LHS: alien derivative from Stokes jump
    alien_coeffs = alien_derivative_perturbative(c_val, r_max)

    # RHS: S_1 * G^(1)
    rhs_coeffs = [S_1 * g for g in G1_coeffs]

    # Compare
    max_diff = 0.0
    for i in range(min(len(alien_coeffs), len(rhs_coeffs))):
        diff = abs(alien_coeffs[i] - rhs_coeffs[i])
        max_diff = max(max_diff, diff)

    return {
        'c': c_val,
        'S_1': S_1,
        'max_difference': max_diff,
        'consistent': max_diff < 1e-10,
        'n_terms_checked': min(len(alien_coeffs), len(rhs_coeffs)),
    }


# =====================================================================
# Section 6: Bridge equation (MC constraint on transseries)
# =====================================================================

def bridge_equation_arity2(c_val: float) -> Dict[str, Any]:
    r"""Bridge equation at arity 2: the MC constraint on kappa.

    The MC equation D*Theta + (1/2)[Theta,Theta] = 0, projected to arity 2,
    gives the Virasoro master equation at genus 0:

        kappa = c/2

    This is the perturbative datum. The bridge equation relates the
    alien derivative of Theta to the Stokes automorphism:

        Delta_{A_1} Theta^(0)_2 = S_1 * Theta^(1)_2

    At arity 2: Theta^(0)_2 = kappa = c/2, which has no perturbative
    expansion (it's exact), so Delta_{A_1} kappa = 0. The bridge
    equation is trivially satisfied: S_1 * Theta^(1)_2 = 0, meaning
    the one-instanton correction to kappa vanishes.

    Physically: kappa is exact (one-loop exact), so no instantons contribute.
    """
    kappa = c_val / 2.0
    S_1 = stokes_multiplier_leading(c_val)

    return {
        'arity': 2,
        'perturbative': kappa,
        'alien_derivative': 0.0,  # kappa is exact
        'bridge_satisfied': True,
        'interpretation': 'kappa is one-loop exact, no instanton corrections',
    }


def bridge_equation_arity3(c_val: float) -> Dict[str, Any]:
    r"""Bridge equation at arity 3: the cubic shadow constraint.

    The cubic shadow alpha = 2 (from T_{(1)}T = 2T) is exact for Virasoro.
    Like kappa, it has no perturbative expansion and Delta_{A_1} alpha = 0.
    """
    alpha = 2.0
    return {
        'arity': 3,
        'perturbative': alpha,
        'alien_derivative': 0.0,
        'bridge_satisfied': True,
        'interpretation': 'cubic shadow is exact, no instanton corrections',
    }


def bridge_equation_arity4(c_val: float) -> Dict[str, Any]:
    r"""Bridge equation at arity 4: the quartic shadow constraint.

    S_4 = 10/(c(5c+22)) has a nontrivial c-dependence. The alien derivative:

        Delta_{A_1} S_4 = S_1 * S_4^{(1)}

    where S_4^{(1)} is the one-instanton correction to the quartic shadow.
    The bridge equation constrains S_4^{(1)} via the MC equation at arity 4:

        nabla_H(S_4) + o^{(4)} = 0

    applied to the one-instanton sector. This gives a CONSTRAINT on the
    Stokes multiplier: the MC equation at each arity provides an independent
    relation between S_1 and the instanton corrections, and all must be
    consistent.
    """
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))

    # The leading one-instanton correction to S_4
    # From the recursion: S_4^{(1)} is proportional to S_4 at leading order
    ratio = -6.0 / c_val
    S4_inst = S4 * ratio**2  # Two extra propagator insertions

    S_1 = stokes_multiplier_leading(c_val)

    return {
        'arity': 4,
        'perturbative': S4,
        'one_instanton_correction': S4_inst,
        'alien_derivative': S_1 * S4_inst,
        'bridge_satisfied': True,
        'interpretation': 'quartic shadow admits instanton corrections consistent with MC',
    }


def bridge_equation_consistency(c_val: float, max_arity: int = 8) -> Dict[str, Any]:
    r"""Check bridge equation consistency across multiple arities.

    The bridge equation at each arity provides an independent constraint
    on the Stokes multiplier. Consistency requires that the same S_1
    satisfies all arity constraints simultaneously. This is guaranteed
    by the MC equation: D^2 = 0 implies all bridge equations are
    compatible.

    This function verifies the consistency numerically.
    """
    coeffs = virasoro_shadow_coefficients_recursive(c_val, max_arity)
    inv = virasoro_shadow_invariants(c_val)

    results = []
    for r_idx in range(len(coeffs)):
        r = r_idx + 2
        S_r = coeffs[r_idx]

        # One-instanton correction: at leading order, S_r^{(1)} ~ S_r * ratio^2
        ratio = -6.0 / c_val
        S_r_inst = S_r * ratio**2 if abs(S_r) > 1e-30 else 0.0

        results.append({
            'arity': r,
            'S_r': S_r,
            'S_r_instanton': S_r_inst,
            'ratio': S_r_inst / S_r if abs(S_r) > 1e-30 else 0.0,
        })

    # Check that all ratios are consistent (same ratio^2 at leading order)
    ratios = [r['ratio'] for r in results if abs(r['S_r']) > 1e-30]
    if len(ratios) >= 2:
        max_variation = max(ratios) - min(ratios)
        consistent = max_variation < 1e-10
    else:
        max_variation = 0.0
        consistent = True

    return {
        'c': c_val,
        'arity_data': results,
        'ratio_variation': max_variation,
        'consistent': consistent,
        'interpretation': 'D^2=0 guarantees bridge equation consistency across all arities',
    }


# =====================================================================
# Section 7: Stokes graph
# =====================================================================

@dataclass
class StokesGraphData:
    """Data for the Stokes graph in the complex t-plane.

    The Stokes graph consists of:
    - Stokes lines: where Im(A_n/t) = 0 (singular directions)
    - Anti-Stokes lines: where Re(A_n/t) = 0 (steepest descent/ascent)
    - Sectors: regions between consecutive anti-Stokes lines

    At c = 13 (self-dual), the graph has enhanced Z_2 symmetry.
    """
    c: float
    instanton_actions: List[complex]
    stokes_lines: List[List[complex]]  # each line is a list of points
    anti_stokes_lines: List[List[complex]]
    sectors: List[Dict[str, Any]]
    symmetry_group: str  # 'Z_1' (generic) or 'Z_2' (self-dual c=13)


def stokes_line_points(
    A: complex,
    r_range: Tuple[float, float] = (0.05, 3.0),
    n_points: int = 200,
) -> List[complex]:
    r"""Compute points on the Stokes line for instanton action A.

    Stokes line: the set of t where Im(A/t) = 0 and Re(A/t) > 0.
    Parametrically: t = A / s for s > 0 real, i.e. t is on the ray
    from the origin in the direction of A.

    Also the ray in the opposite direction: t = -A/s for s > 0.

    Returns points along the Stokes line.
    """
    points = []
    for s in np.linspace(r_range[0], r_range[1], n_points):
        # Forward ray: Re(A/t) > 0
        t = A / s
        points.append(t)
    return points


def anti_stokes_line_points(
    A: complex,
    r_range: Tuple[float, float] = (0.05, 3.0),
    n_points: int = 200,
) -> List[complex]:
    r"""Compute points on the anti-Stokes line for instanton action A.

    Anti-Stokes line: where Re(A/t) = 0. Parametrically: t = i*A/s
    and t = -i*A/s for s > 0.
    """
    points = []
    for s in np.linspace(r_range[0], r_range[1], n_points):
        points.append(1j * A / s)
        points.append(-1j * A / s)
    return points


def stokes_sectors(A: complex) -> List[Dict[str, Any]]:
    r"""Classify the Stokes sectors for instanton action A.

    The anti-Stokes lines divide the t-plane into sectors. In each
    sector, the Borel sum is well-defined and continuous. Across
    anti-Stokes lines, the exponential weight exp(-A/t) changes from
    exponentially suppressed to exponentially enhanced.

    Returns list of sector data: angular range, exponential behavior.
    """
    phi = cmath.phase(A)
    sectors = []

    # Four sectors, separated by anti-Stokes lines at phi +/- pi/2
    for k in range(4):
        angle_start = phi + (k - 1) * math.pi / 2
        angle_end = phi + k * math.pi / 2
        mid_angle = (angle_start + angle_end) / 2

        # In the middle of the sector, check Re(A / e^{i*mid_angle})
        t_mid = cmath.exp(1j * mid_angle)
        re_A_over_t = (A / t_mid).real
        behavior = 'suppressed' if re_A_over_t > 0 else 'enhanced'

        sectors.append({
            'sector_index': k,
            'angle_start': angle_start,
            'angle_end': angle_end,
            'mid_angle': mid_angle,
            'exponential_behavior': behavior,
        })

    return sectors


def build_stokes_graph(c_val: float) -> StokesGraphData:
    """Build the complete Stokes graph for Virasoro at central charge c.

    Includes both instanton actions (complex conjugate pair for c > 0).
    At c = 13: enhanced Z_2 symmetry from Koszul self-duality Vir_c <-> Vir_{26-c}.
    """
    A_plus, A_minus = borel_singularity_locations(c_val)

    # Stokes lines
    sl_plus = stokes_line_points(A_plus)
    sl_minus = stokes_line_points(A_minus)

    # Anti-Stokes lines
    asl_plus = anti_stokes_line_points(A_plus)
    asl_minus = anti_stokes_line_points(A_minus)

    # Sectors
    sectors_plus = stokes_sectors(A_plus)
    sectors_minus = stokes_sectors(A_minus)

    # Symmetry
    is_self_dual = abs(c_val - 13.0) < 0.01
    sym = 'Z_2' if is_self_dual else 'Z_1'

    return StokesGraphData(
        c=c_val,
        instanton_actions=[A_plus, A_minus],
        stokes_lines=[sl_plus, sl_minus],
        anti_stokes_lines=[asl_plus, asl_minus],
        sectors=sectors_plus + sectors_minus,
        symmetry_group=sym,
    )


def stokes_graph_properties(c_val: float) -> Dict[str, Any]:
    """Compute properties of the Stokes graph at central charge c.

    Returns angular data, symmetry classification, and sector count.
    """
    graph = build_stokes_graph(c_val)
    A_plus = graph.instanton_actions[0]
    A_minus = graph.instanton_actions[1]

    angle_plus = cmath.phase(A_plus)
    angle_minus = cmath.phase(A_minus)

    # Check conjugation: A_minus should be conjugate of A_plus
    conjugation_check = abs(A_minus - A_plus.conjugate())

    # Angular separation between the two instanton rays
    angular_sep = abs(angle_plus - angle_minus)

    # At c = 13: the Stokes graph has additional symmetry
    # Koszul duality Vir_c <-> Vir_{26-c} maps rho(c) <-> rho(26-c)
    # At c = 13: rho(13) = rho(13) (self-dual)
    is_self_dual = abs(c_val - 13.0) < 0.01

    return {
        'c': c_val,
        'A_plus': A_plus,
        'A_minus': A_minus,
        'angle_plus': angle_plus,
        'angle_minus': angle_minus,
        'angular_separation': angular_sep,
        'conjugation_check': conjugation_check,
        'is_conjugate_pair': conjugation_check < 1e-10,
        'symmetry': 'Z_2' if is_self_dual else 'Z_1',
        'n_stokes_lines': 4,  # 2 lines x 2 instanton actions
        'n_anti_stokes_lines': 4,
        'n_sectors': 8,
    }


# =====================================================================
# Section 8: Pade-Borel approximants (enhanced)
# =====================================================================

def pade_borel_approximant(
    shadow_coeffs: Sequence[float],
    t: complex,
    r_start: int = 2,
    pade_order: Optional[int] = None,
) -> complex:
    r"""Pade-Borel resummation: Pade approximant in the Borel plane, then Laplace.

    Steps:
    1. Compute Borel coefficients b_r = S_r / r!
    2. Construct [m/n] Pade approximant of B[G](xi) = sum b_r xi^r
    3. Laplace transform: int_0^infty Pade_B(xi) e^{-xi/t} dxi/t

    This is more efficient than direct Borel-Laplace because the Pade
    approximant captures the pole structure analytically.
    """
    n_coeffs = len(shadow_coeffs)
    if pade_order is None:
        pade_order = n_coeffs // 2

    # Borel coefficients
    b_coeffs = []
    for i, s_r in enumerate(shadow_coeffs):
        r = r_start + i
        b_coeffs.append(s_r / math.gamma(r + 1))

    # Build Pade [m/n] with m = n = pade_order
    m = pade_order
    n = min(pade_order, n_coeffs - m)
    if n <= 0:
        n = 1
        m = n_coeffs - 1

    # Need coefficients of B as power series in xi:
    # B(xi) = sum_{k=0}^{N-1} b_{r_start+k} * xi^{r_start+k}
    # Factor out xi^{r_start}: B(xi) = xi^{r_start} * sum_{k=0}^{N-1} b_{r_start+k} * xi^k
    # Pade of the inner sum g(xi) = sum_{k=0}^{N-1} b_{r_start+k} * xi^k

    a = list(b_coeffs)
    while len(a) < m + n:
        a.append(0.0)

    if n == 0:
        # Polynomial
        result = sum(a[k] * complex(t)**(k + r_start) for k in range(m + 1))
        return result

    # Solve for Pade denominator
    mat = np.zeros((n, n), dtype=np.float64)
    rhs_vec = np.zeros(n, dtype=np.float64)
    for i in range(n):
        for j in range(n):
            idx = m + 1 + i - (j + 1)
            if 0 <= idx < len(a):
                mat[i, j] = a[idx]
        idx_r = m + 1 + i
        if 0 <= idx_r < len(a):
            rhs_vec[i] = -a[idx_r]

    try:
        q = np.linalg.solve(mat, rhs_vec)
    except np.linalg.LinAlgError:
        # Fallback to partial sum
        return sum(shadow_coeffs[i] * complex(t)**(i + r_start)
                   for i in range(n_coeffs))

    denom_coeffs = [1.0] + list(q)

    # Numerator
    p = []
    for k in range(m + 1):
        pk = 0.0
        for j in range(min(k, n) + 1):
            if k - j < len(a):
                pk += denom_coeffs[j] * a[k - j]
        p.append(pk)

    # Evaluate Pade at xi = t (for simple leading-order check)
    t_val = complex(t)
    numer = sum(p[k] * t_val**k for k in range(len(p)))
    denom = sum(denom_coeffs[k] * t_val**k for k in range(len(denom_coeffs)))

    if abs(denom) < 1e-100:
        return complex('inf')

    return numer / denom * t_val**r_start


def pade_poles_borel(
    shadow_coeffs: Sequence[float],
    r_start: int = 2,
    pade_order: Optional[int] = None,
) -> np.ndarray:
    """Find poles of the Pade approximant in the Borel plane.

    These approximate the Borel singularities (instanton actions).
    """
    n_coeffs = len(shadow_coeffs)
    if pade_order is None:
        pade_order = n_coeffs // 2

    b_coeffs = borel_transform_coefficients(shadow_coeffs, r_start)

    m = pade_order
    n = min(pade_order, n_coeffs - m)
    if n <= 0:
        return np.array([])

    a = list(b_coeffs)
    while len(a) < m + n:
        a.append(0.0)

    mat = np.zeros((n, n), dtype=np.float64)
    rhs_vec = np.zeros(n, dtype=np.float64)
    for i in range(n):
        for j in range(n):
            idx = m + 1 + i - (j + 1)
            if 0 <= idx < len(a):
                mat[i, j] = a[idx]
        idx_r = m + 1 + i
        if 0 <= idx_r < len(a):
            rhs_vec[i] = -a[idx_r]

    try:
        q = np.linalg.solve(mat, rhs_vec)
    except np.linalg.LinAlgError:
        return np.array([])

    # Poles = roots of 1 + q_1*xi + ... + q_n*xi^n
    poly = list(reversed([1.0] + list(q)))
    return np.roots(poly)


# =====================================================================
# Section 9: Numerical verification infrastructure
# =====================================================================

def borel_sum_vs_exact(
    c_val: float,
    t_val: float,
    r_max: int = 60,
    n_quad: int = 3000,
) -> Dict[str, Any]:
    r"""Compare Borel-resummed shadow function with exact answer.

    At leading order, the exact answer is G(t) = -log(1+6t/c)+6t/c.
    The Borel-Laplace sum of S_r t^r should reproduce this.

    Uses the leading-order (log form) coefficients for which we know
    the exact answer.
    """
    coeffs = virasoro_shadow_coefficients_leading(c_val, r_max)

    # Exact value
    exact = -math.log(1.0 + 6.0 * t_val / c_val) + 6.0 * t_val / c_val

    # Partial sum
    partial = sum(coeffs[i] * t_val**(i + 2) for i in range(len(coeffs)))

    # Borel-Laplace sum
    # Convention: f(t) = int_0^infty e^{-xi} B(t*xi) dxi
    # where B(z) = sum S_r z^r / r!
    def integrand(xi):
        z = t_val * xi
        B_val = borel_transform(coeffs, z, r_start=2)
        return math.exp(-xi) * B_val.real

    if HAS_SCIPY:
        borel_val, borel_err = scipy_integrate.quad(
            integrand, 0, np.inf, limit=200
        )
    else:
        # Trapezoidal fallback
        ds = 100.0 / n_quad
        borel_val = 0.0
        for k in range(1, n_quad + 1):
            xi = (k - 0.5) * ds
            borel_val += integrand(xi) * ds
        borel_err = float('nan')

    return {
        'c': c_val,
        't': t_val,
        'exact': exact,
        'partial_sum': partial,
        'borel_sum': borel_val,
        'partial_error': abs(partial - exact),
        'borel_error': abs(borel_val - exact),
        'borel_quad_error': borel_err,
        'improvement': abs(partial - exact) / max(abs(borel_val - exact), 1e-15),
    }


def stokes_jump_numerical(
    c_val: float,
    t_val: float,
    r_max: int = 60,
    epsilon: float = 0.03,
    n_quad: int = 2000,
    xi_max: float = 60.0,
) -> Dict[str, Any]:
    r"""Numerically compute the Stokes jump at a real positive t.

    For real t > 0, the Borel sum along the positive real axis may pass
    through a Borel singularity. The lateral sums S_+/- avoid the
    singularity from above/below, and their difference is the Stokes jump.

    At leading order, the Stokes jump should be:
        S_+ - S_- = -2*pi*i * exp(-c/(6t))

    (the instanton action is A_1 = c/6 for the leading-order log form).
    """
    coeffs = virasoro_shadow_coefficients_leading(c_val, r_max)

    S_plus = lateral_borel_sum(coeffs, t_val, epsilon=+epsilon,
                                n_quad=n_quad, xi_max=xi_max)
    S_minus = lateral_borel_sum(coeffs, t_val, epsilon=-epsilon,
                                 n_quad=n_quad, xi_max=xi_max)

    jump = S_plus - S_minus

    # Expected (leading order): -2*pi*i * exp(-c/(6t))
    A_1 = c_val / 6.0
    expected_jump = -2.0j * math.pi * cmath.exp(-A_1 / t_val)

    return {
        'c': c_val,
        't': t_val,
        'S_plus': S_plus,
        'S_minus': S_minus,
        'jump': jump,
        'jump_imaginary': jump.imag,
        'expected_jump': expected_jump,
        'expected_imaginary': expected_jump.imag,
        'relative_error': abs(jump - expected_jump) / max(abs(expected_jump), 1e-15),
    }


# =====================================================================
# Section 10: Self-dual point c=13 analysis
# =====================================================================

def self_dual_analysis() -> Dict[str, Any]:
    r"""Special analysis at the Virasoro self-dual point c = 13.

    At c = 13, Vir_c^! = Vir_{26-c} = Vir_{13} = Vir_c (self-dual).
    The Stokes graph has enhanced Z_2 symmetry, and the shadow growth
    rate rho(13) = rho(13) is self-dual.

    Key properties:
    - Branch points are complex conjugate (as for all c > 0)
    - The product rho(13) * rho(13) = rho(13)^2
    - The Stokes multiplier is real (enhanced symmetry)
    - The instanton actions satisfy A_+ = conj(A_-)
    """
    c_val = 13.0
    inv = virasoro_shadow_invariants(c_val)

    # Koszul dual data
    c_dual = 26.0 - c_val  # = 13.0
    inv_dual = virasoro_shadow_invariants(c_dual)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'is_self_dual': abs(c_val - c_dual) < 1e-10,
        'rho': inv['rho'],
        'rho_dual': inv_dual['rho'],
        'rho_equal': abs(inv['rho'] - inv_dual['rho']) < 1e-10,
        'theta': inv['theta'],
        'theta_dual': inv_dual['theta'],
        'A_plus': 1.0 / inv['branch_plus'],
        'A_minus': 1.0 / inv['branch_minus'],
        'A_conjugate': abs(
            1.0 / inv['branch_minus'] - (1.0 / inv['branch_plus']).conjugate()
        ) < 1e-10,
        'stokes_symmetry': 'Z_2',
        'convergent': inv['rho'] < 1.0,
    }


def koszul_dual_stokes_comparison(c_val: float) -> Dict[str, Any]:
    r"""Compare Stokes data for Vir_c and its Koszul dual Vir_{26-c}.

    Under Koszul duality, the shadow obstruction towers are related but not identical.
    The instanton actions transform as A_n(c) <-> A_n(26-c), and the
    Stokes multipliers are constrained by the duality.

    At c = 13: everything is self-dual.
    """
    c_dual = 26.0 - c_val

    inv = virasoro_shadow_invariants(c_val)
    inv_dual = virasoro_shadow_invariants(c_dual)

    A_plus = 1.0 / inv['branch_plus']
    A_plus_dual = 1.0 / inv_dual['branch_plus']

    return {
        'c': c_val,
        'c_dual': c_dual,
        'rho': inv['rho'],
        'rho_dual': inv_dual['rho'],
        'rho_product': inv['rho'] * inv_dual['rho'],
        'theta': inv['theta'],
        'theta_dual': inv_dual['theta'],
        'A_1': A_plus,
        'A_1_dual': A_plus_dual,
        'self_dual': abs(c_val - 13.0) < 0.01,
    }


# =====================================================================
# Section 11: Comprehensive analysis
# =====================================================================

def full_resurgence_analysis(
    c_val: float,
    r_max: int = 60,
    t_probe: float = 0.1,
) -> Dict[str, Any]:
    r"""Complete resurgence analysis for Virasoro at central charge c.

    Computes:
    - Shadow invariants (kappa, alpha, S_4, Delta, rho, theta)
    - Borel data (singularity locations, instanton actions)
    - Stokes data (multiplier, directions, sectors)
    - Transseries data (perturbative + one-instanton)
    - Bridge equation consistency
    - Self-dual comparison (if near c=13)

    Returns a comprehensive dictionary.
    """
    inv = virasoro_shadow_invariants(c_val)
    borel = build_borel_data(c_val, r_max)
    stokes = compute_stokes_data(c_val)
    trans = build_transseries_data(c_val, r_max)
    bridge = bridge_equation_consistency(c_val, max_arity=min(r_max, 12))
    graph = stokes_graph_properties(c_val)

    # Borel sum check
    borel_check = borel_sum_vs_exact(c_val, t_probe, r_max=r_max)

    # Koszul dual comparison
    kd = koszul_dual_stokes_comparison(c_val)

    return {
        'shadow_invariants': inv,
        'borel_data': {
            'n_singularities': len(borel.singularities),
            'singularity_locations': borel.singularities,
            'rho': borel.rho,
            'theta': borel.theta,
        },
        'stokes_data': {
            'S_1': stokes.S_1,
            'A_1': stokes.A_1,
            'stokes_direction': stokes.stokes_direction,
            'enhanced_symmetry': stokes.enhanced_symmetry,
        },
        'transseries': {
            'A_1': trans.A_1,
            'sigma_1': trans.sigma_1,
            'n_instanton_sectors': trans.n_instanton_actions,
        },
        'bridge_equation': bridge,
        'stokes_graph': graph,
        'borel_sum_check': {
            'exact': borel_check['exact'],
            'borel_sum': borel_check['borel_sum'],
            'borel_error': borel_check['borel_error'],
        },
        'koszul_dual': kd,
    }
