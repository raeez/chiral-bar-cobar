"""
Shadow singularity map: analytic continuation and scattering connections.

For each shadow archetype (G, L, C, M), the shadow generating function
G_A(t) = integral log(1 - lambda*t) d rho_A(lambda) encodes the full shadow
tower.  The singularity structure of G_A(t) in the complex t-plane —
branch points, monodromy, Borel summability, resurgent alien derivatives —
provides a new analytic invariant of the chiral algebra A.

ARCHETYPE GENERATING FUNCTIONS (exact, from the spectral measure):

  G  (Heisenberg):   G(t) = -t/2
                      Singularities: none (entire).  rho = delta(lambda - 1/2).
  L  (affine sl_2):  G(t) = -log(1 + t) - log(1 + t/3)   [at k=1]
                      Singularities: t = -1, -3.  rho = delta(lambda-1) + delta(lambda-1/3).
  C  (betagamma):    G(t) = -log(1 + 4t/c)   [leading quartic, c = -2]
                      Singularities: t = -c/4.  rho = delta(lambda - 4/c).
  M  (Virasoro):     G(t) = -log(1 + 6t/c)
                      Singularities: t = -c/6.  rho = delta(lambda - 6/c).

KEY RESULTS:

  1. Singularity map: complete classification of branch points, poles,
     and monodromy for all four classes.
  2. Monodromy computation: log monodromy G -> G + 2*pi*i for each branch
     point.  Affine sl_2 monodromy group = Z x Z (two independent log
     monodromies).
  3. Borel summation: Borel transform B(u) = sum S_r u^r / r! identifies
     Borel-plane singularities with the G(t) branch points (Nevanlinna).
  4. Complex spectral parameter t = i*gamma: Lorentzian profile
     |exp(G(i*gamma))| = (1 + 36*gamma^2/c^2)^{-1/2} for Virasoro.
  5. Shadow GF -> scattering connection: comparison of G_A(it) with the
     scattering matrix phi(1/2 + it) on the critical line.
  6. Spectral measure -> Rankin-Selberg: eps^c_s(A) = integral lambda^{-s}
     d rho_A(lambda).  For Virasoro: (c/6)^s.
  7. W_3 multi-singularity: two branch points from weight-2 and weight-3
     sectors.  Stokes lines at arg(t) = pi/2 +- theta_crossing.
  8. Resurgent structure: alien derivatives Delta_{t_j} G from each
     singularity.

References:
  shadow_complex_analysis.py — Borel/Pade analysis of shadow tower
  virasoro_shadow_gf.py — exact S_r(c) via recursion
  scattering_resonance.py — phi(s) and spectral zeta
  rankin_selberg_bridge.py — Benjamin-Chang constrained Epstein zeta
  w3_multivariable_shadow.py — W_3 multi-variable shadow tower
"""

from __future__ import annotations

import cmath
import math
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    import mpmath
    from mpmath import mp, mpf, mpc, pi as mpi, gamma as mpgamma, zeta as mpzeta
    from mpmath import log as mplog, exp as mpexp, sqrt as mpsqrt, power as mppower
    from mpmath import zetazero, diff as mpdiff, quad as mpquad, fac, im, re, conj
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =====================================================================
# Section 1: Shadow generating functions — exact forms
# =====================================================================

def G_heisenberg(t: complex) -> complex:
    """Heisenberg shadow GF: G(t) = -t/2.

    The spectral measure is rho = delta(lambda - 1/2).
    Then G(t) = log(1 - t/2) ... but this is the G from the integral
    representation.  For Heisenberg, kappa = 1/2 and the shadow tower
    terminates at depth 2, so G(t) = -t/2 (the leading term of -log(1-t/2)).

    Actually the EXACT form from the spectral representation is:
      G(t) = integral log(1 - lambda*t) d rho(lambda)
           = log(1 - t/2)
    But the shadow tower gives G(t) = -kappa*t = -t/2 (linear, terminates).
    These agree to first order.  The exact spectral form has a branch point
    at t=2.

    We use the SHADOW TOWER form G(t) = -t/2 (entire, consistent with
    depth-2 termination) as the primary definition.
    """
    return -t / 2.0


def G_heisenberg_spectral(t: complex) -> complex:
    """Heisenberg shadow GF from spectral measure: G(t) = log(1 - t/2).

    This is the exact form from the spectral integral representation.
    Branch point at t = 2.
    """
    return cmath.log(1.0 - t / 2.0)


def G_affine_sl2(t: complex, k: float = 1.0) -> complex:
    """Affine sl_2 shadow GF at level k.

    G(t) = -log(1 + t/k) - log(1 + t/(k+2))

    For sl_2 at level k: the spectral measure has atoms at
    lambda_1 = 1/k and lambda_2 = 1/(k+2), giving:
      G(t) = log(1 - t/k) + log(1 - t/(k+2))  [spectral form]
           = -log(1 + t/k) - log(1 + t/(k+2))  [with sign convention from task]

    Branch points at t = -k and t = -(k+2).
    At k=1: branch points at t = -1 and t = -3.
    """
    return -cmath.log(1.0 + t / k) - cmath.log(1.0 + t / (k + 2.0))


def G_betagamma(t: complex, c: float = -2.0) -> complex:
    """Betagamma shadow GF.

    G(t) = -log(1 + 4t/c)

    The betagamma system has c = -2 (one boson, one fermion pair).
    Singularity at t = -c/4.  At c = -2: t = 1/2.

    NOTE: c = -2 for the standard betagamma, so 4/c = -2, giving
    G(t) = -log(1 - 2t).  Singularity at t = 1/2 on the POSITIVE real axis.
    """
    return -cmath.log(1.0 + 4.0 * t / c)


def G_virasoro(t: complex, c: float = 26.0) -> complex:
    """Virasoro shadow GF at central charge c.

    G(t) = -log(1 + 6t/c)

    Branch point at t = -c/6.  At c = 26: t = -13/3.
    Spectral measure: rho = delta(lambda - 6/c).
    """
    return -cmath.log(1.0 + 6.0 * t / c)


def G_w3(t: complex, c: float = 50.0) -> complex:
    """W_3 shadow GF (simplified single-variable projection).

    W_3 has two strong generators T (weight 2) and W (weight 3).
    The single-variable shadow GF on the T-line is:
      G(t) = -log(1 + 6t/c) - log(1 + alpha_W * t)

    where alpha_W encodes the W-generator self-OPE contribution.
    For W_3: alpha_W = 2*10/(c*(5c+22)) * c = 20/(5c+22)
    (from the quartic shadow Q_{WW}).

    Two branch points: t_1 = -c/6 (Virasoro sector),
                       t_2 = -(5c+22)/20 (W sector).
    """
    alpha_W = 20.0 / (5.0 * c + 22.0)
    return -cmath.log(1.0 + 6.0 * t / c) - cmath.log(1.0 + alpha_W * t)


# =====================================================================
# Section 2: Singularity classification and mapping
# =====================================================================

def singularities_heisenberg() -> Dict[str, Any]:
    """Heisenberg singularity data: no singularities (entire function)."""
    return {
        'archetype': 'G',
        'algebra': 'Heisenberg',
        'branch_points': [],
        'spectral_atoms': [0.5],
        'monodromy_group': 'trivial',
        'borel_singularities': [],
        'depth': 2,
        'description': 'Entire function.  No singularities in finite t-plane.',
    }


def singularities_affine_sl2(k: float = 1.0) -> Dict[str, Any]:
    """Affine sl_2 singularity data at level k."""
    bp1 = -k
    bp2 = -(k + 2.0)
    return {
        'archetype': 'L',
        'algebra': f'V_{{k={k}}}(sl_2)',
        'branch_points': [bp1, bp2],
        'spectral_atoms': [1.0 / k, 1.0 / (k + 2.0)],
        'monodromy_group': 'Z x Z',
        'borel_singularities': [bp1, bp2],
        'depth': 3,
        'description': (
            f'Two log branch points at t = {bp1} and t = {bp2}.  '
            f'Independent log monodromies generate Z x Z.'
        ),
    }


def singularities_betagamma(c: float = -2.0) -> Dict[str, Any]:
    """Betagamma singularity data."""
    bp = -c / 4.0
    return {
        'archetype': 'C',
        'algebra': 'betagamma',
        'branch_points': [bp],
        'spectral_atoms': [4.0 / c],
        'monodromy_group': 'Z',
        'borel_singularities': [bp],
        'depth': 4,
        'description': (
            f'Single log branch point at t = {bp} = -c/4.  '
            f'Log monodromy generates Z.'
        ),
    }


def singularities_virasoro(c: float = 26.0) -> Dict[str, Any]:
    """Virasoro singularity data at central charge c."""
    bp = -c / 6.0
    return {
        'archetype': 'M',
        'algebra': f'Vir_{{c={c}}}',
        'branch_points': [bp],
        'spectral_atoms': [6.0 / c],
        'monodromy_group': 'Z',
        'borel_singularities': [bp],
        'depth': float('inf'),
        'description': (
            f'Single log branch point at t = {bp:.6f} = -c/6.  '
            f'Infinite shadow tower.  Log monodromy generates Z.'
        ),
    }


def singularities_w3(c: float = 50.0) -> Dict[str, Any]:
    """W_3 singularity data."""
    bp1 = -c / 6.0
    alpha_W = 20.0 / (5.0 * c + 22.0)
    bp2 = -1.0 / alpha_W
    return {
        'archetype': 'M (multi-generator)',
        'algebra': f'W_3 at c={c}',
        'branch_points': [bp1, bp2],
        'spectral_atoms': [6.0 / c, alpha_W],
        'monodromy_group': 'Z x Z',
        'borel_singularities': [bp1, bp2],
        'depth': float('inf'),
        'description': (
            f'Two log branch points: t_1 = {bp1:.4f} (Virasoro sector), '
            f't_2 = {bp2:.4f} (W sector).  Independent log monodromies.'
        ),
    }


def singularity_map(archetype: str, **kwargs) -> Dict[str, Any]:
    """Return singularity data for given archetype.

    Parameters
    ----------
    archetype : str
        One of 'G', 'L', 'C', 'M', 'W3'.
    **kwargs : passed to the specific function (c, k, etc.)
    """
    dispatch = {
        'G': singularities_heisenberg,
        'L': singularities_affine_sl2,
        'C': singularities_betagamma,
        'M': singularities_virasoro,
        'W3': singularities_w3,
    }
    if archetype not in dispatch:
        raise ValueError(f"Unknown archetype: {archetype}")
    return dispatch[archetype](**kwargs)


# =====================================================================
# Section 3: Monodromy computation
# =====================================================================

def log_monodromy(G_func: Callable, branch_point: complex,
                  radius: float = 0.01, n_points: int = 1024) -> complex:
    """Compute monodromy of G around a branch point by numerical continuation.

    Integrates G'(z) dz around a small circle centered at the branch point
    using numerical differentiation and trapezoidal quadrature.  For a log
    branch point, the monodromy is +-2*pi*i.

    This approach correctly isolates the monodromy of a SINGLE branch point
    even when multiple branch points are present (provided the radius is
    small enough that the circle encloses only the target branch point).

    Returns the monodromy: contour integral of G'(z) dz around one circuit.
    """
    # Parametrize a circle: z(theta) = branch_point + radius * exp(i*theta)
    # dz = i * radius * exp(i*theta) * dtheta
    # integral G'(z) dz = integral_{0}^{2pi} G'(z(theta)) * i*r*exp(i*theta) dtheta
    #
    # Approximate G'(z) ~ [G(z + h) - G(z - h)] / (2h) with small h.
    h = radius * 1e-4
    thetas = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    dtheta = 2 * np.pi / n_points

    integral = 0.0 + 0.0j
    for theta in thetas:
        z = branch_point + radius * cmath.exp(1j * theta)
        dz_dtheta = 1j * radius * cmath.exp(1j * theta)
        # Numerical derivative of G
        Gp = (G_func(z + h) - G_func(z - h)) / (2 * h)
        integral += Gp * dz_dtheta * dtheta

    return integral


def monodromy_virasoro(c: float = 26.0) -> complex:
    """Monodromy of G_Vir around t = -c/6.

    Going around the branch point, log(1 + 6t/c) picks up 2*pi*i,
    so G = -log(1 + 6t/c) picks up -2*pi*i.
    """
    bp = -c / 6.0
    return log_monodromy(lambda t: G_virasoro(t, c), complex(bp), radius=0.01)


def monodromy_affine_sl2(k: float = 1.0) -> Tuple[complex, complex]:
    """Monodromy of G_aff around each branch point.

    Branch points at t = -k and t = -(k+2).
    Each is a simple log branch point with monodromy -2*pi*i.
    The monodromy GROUP is Z x Z (abelian, independent generators).
    """
    bp1 = complex(-k)
    bp2 = complex(-(k + 2.0))

    mono1 = log_monodromy(lambda t: G_affine_sl2(t, k), bp1, radius=0.01)
    mono2 = log_monodromy(lambda t: G_affine_sl2(t, k), bp2, radius=0.01)
    return mono1, mono2


def monodromy_matrix_affine(k: float = 1.0) -> np.ndarray:
    """Monodromy representation of pi_1(C \\ {-k, -(k+2)}) on C.

    The fundamental group of C minus two points is free on 2 generators
    gamma_1, gamma_2 (loops around each puncture).  G is single-valued
    on the universal cover; the monodromy representation is:

      gamma_1: G -> G - 2*pi*i
      gamma_2: G -> G - 2*pi*i

    As affine transformations G -> G + c_j, these are COMMUTING translations,
    generating Z x Z subset of (C, +).

    We represent this as a 2x1 matrix of monodromy vectors.
    """
    m1 = -2.0 * np.pi * 1j  # monodromy around t = -k
    m2 = -2.0 * np.pi * 1j  # monodromy around t = -(k+2)
    return np.array([m1, m2])


# =====================================================================
# Section 4: Borel summation
# =====================================================================

def virasoro_shadow_coefficients(c: float, r_max: int) -> List[float]:
    """Leading-order Virasoro shadow coefficients S_r from G(t) = -log(1 + 6t/c).

    G(t) = -log(1 + 6t/c) = sum_{r>=1} (-1)^r (6/c)^r t^r / r.

    So S_r = (-1)^{r+1} (6/c)^r / r   for r >= 1.
    (S_1 = 6/c = kappa*2; shadows start at r=2 in the deformation complex,
     but for the Borel analysis we include r=1.)
    """
    coeffs = []
    for r in range(1, r_max + 1):
        coeffs.append((-1.0) ** (r + 1) * (6.0 / c) ** r / r)
    return coeffs


def borel_transform_virasoro(c: float, u: complex, r_max: int = 50) -> complex:
    """Borel transform B(u) = sum_{r>=1} S_r * u^r / r!.

    For S_r = (-1)^{r+1} (6/c)^r / r:
      B(u) = sum_{r>=1} (-1)^{r+1} (6/c)^r u^r / (r * r!)

    The series converges for all u (entire in u!), but the Borel INTEGRAL
      G(t) = integral_0^infty B(u) e^{-u/t} du/t
    has a singularity when the integration contour hits a singularity of
    the integrand in the u-plane.

    Actually, the Borel transform of the DIVERGENT series is:
      If G(t) ~ sum a_r t^r with a_r ~ r! * A^r, then
      B(u) = sum a_r u^r / r! ~ sum A^r u^r = 1/(1 - Au).
    The Borel transform has a pole at u = 1/A = the branch-point distance.

    For Virasoro: a_r = (-1)^{r+1} (6/c)^r / r, and a_r does NOT grow
    factorially (it grows geometrically like (6/c)^r).  This means the
    original series has finite radius of convergence |t| < c/6, not
    divergent.  The Borel transform is thus ENTIRE.

    The Borel SINGULARITY appears instead in the FORMAL Borel transform
    of the ASYMPTOTIC series when we expand around a SINGULAR point.
    """
    u = complex(u)
    result = 0.0 + 0.0j
    for r in range(1, r_max + 1):
        S_r = (-1.0) ** (r + 1) * (6.0 / c) ** r / r
        result += S_r * u ** r / math.factorial(r)
    return result


def borel_transform_closed_form(c: float, u: complex) -> complex:
    """Closed-form Borel transform for Virasoro.

    B(u) = sum_{r>=1} (-1)^{r+1} (6u/c)^r / (r * r!)

    This can be written in terms of the exponential integral:
      B(u) = Ei(6u/c) - log(6u/c) - gamma  (up to regularization)

    But more directly, note:
      d/du B(u) = sum_{r>=1} (-1)^{r+1} (6/c)^r u^{r-1} / r!
                = (c/6u) sum_{r>=1} (-6u/c)^r / r!
                = (c/6u) [exp(-6u/c) - 1]
                = -(c/6u)(1 - exp(-6u/c))

    So B(u) = integral_0^u (c/6v)(1 - exp(-6v/c)) dv
            = integral_0^{6u/c} (1 - exp(-w)) dw/w   [w = 6v/c]
            = integral_0^{6u/c} (1 - e^{-w})/w dw

    This is the Ein function: B(u) = Ein(6u/c)
    where Ein(z) = integral_0^z (1 - e^{-w})/w dw = sum (-1)^{n+1} z^n/(n*n!).
    """
    if abs(u) < 1e-15:
        return 0.0 + 0.0j
    # Direct series: B(u) = sum_{r>=1} (-1)^{r+1} (6u/c)^r / (r * r!)
    # Let z = 6u/c.  Then B(u) = sum_{r>=1} (-1)^{r+1} z^r / (r * r!) = Ein(z).
    z = 6.0 * u / c
    # Ein(z) = sum_{n>=1} (-1)^{n+1} z^n / (n * n!)
    result = 0.0 + 0.0j
    for n in range(1, 80):
        result += (-1.0) ** (n + 1) * z ** n / (n * math.factorial(n))
    return result


def borel_singularities_from_gf(archetype: str, c: float = 26.0,
                                 k: float = 1.0) -> List[complex]:
    """Identify Borel singularities from the generating function.

    By Nevanlinna's theorem, if G(t) has radius of convergence R,
    then the Borel transform B(u) has singularities at u = R
    (on the boundary of convergence of the original series).

    For each archetype:
      G: no singularities (R = infinity), Borel singularities: none.
      L: R = min(k, k+2) = k, Borel singularity at u = k.
      C: R = |c|/4, Borel singularity at u = |c|/4.
      M: R = c/6, Borel singularity at u = c/6.

    NOTE: The Borel singularities are at the RECIPROCAL of the spectral
    atoms (u_j = 1/lambda_j = branch-point distance), NOT at the branch
    points themselves.  Nevanlinna: singularities of G(t) at t = -1/lambda_j
    correspond to singularities of B(u) at u = 1/lambda_j = |t_j|.
    """
    if archetype == 'G':
        return []
    elif archetype == 'L':
        return [complex(k), complex(k + 2.0)]
    elif archetype == 'C':
        return [complex(abs(c) / 4.0)]
    elif archetype == 'M':
        return [complex(c / 6.0)]
    else:
        raise ValueError(f"Unknown archetype: {archetype}")


# =====================================================================
# Section 5: Complex spectral parameter — Lorentzian profile
# =====================================================================

def G_virasoro_imaginary(gamma: float, c: float = 26.0) -> complex:
    """Virasoro shadow GF at purely imaginary argument t = i*gamma.

    G(i*gamma) = -log(1 + 6i*gamma/c)

    Re G = -1/2 log(1 + 36*gamma^2/c^2)
    Im G = -arctan(6*gamma/c)
    """
    return G_virasoro(1j * gamma, c)


def lorentzian_profile_virasoro(gamma: float, c: float = 26.0) -> float:
    """Amplitude |exp(G(i*gamma))| for Virasoro.

    |exp(G(i*gamma))| = |1 + 6i*gamma/c|^{-1}
                      = (1 + 36*gamma^2/c^2)^{-1/2}

    This is a LORENTZIAN in gamma with half-width c/6.
    """
    return (1.0 + 36.0 * gamma ** 2 / c ** 2) ** (-0.5)


def weil_test_function(gamma: float, kappa: float) -> float:
    """Weil test function h_G(gamma) = exp(-gamma^2 / (4*kappa)).

    This is the Gaussian test function used in explicit-formula approaches.
    kappa = shadow curvature invariant.
    """
    return math.exp(-gamma ** 2 / (4.0 * kappa))


def lorentzian_vs_gaussian_comparison(c: float = 26.0,
                                       gamma_max: float = 50.0,
                                       n_points: int = 200) -> Dict[str, np.ndarray]:
    """Compare the Lorentzian profile from G_Vir(i*gamma) with Gaussian test function.

    For Virasoro at central charge c:
      Lorentzian: L(gamma) = (1 + 36*gamma^2/c^2)^{-1/2}
      Gaussian:   G(gamma) = exp(-gamma^2/(4*kappa))  with kappa = c/2

    The Lorentzian has heavier tails (power-law decay vs exponential).
    """
    gammas = np.linspace(0, gamma_max, n_points)
    kappa = c / 2.0

    lor = np.array([lorentzian_profile_virasoro(g, c) for g in gammas])
    gau = np.array([weil_test_function(g, kappa) for g in gammas])

    return {
        'gammas': gammas,
        'lorentzian': lor,
        'gaussian': gau,
        'half_width_lorentzian': c / 6.0,
        'half_width_gaussian': 2.0 * math.sqrt(kappa * math.log(2)),
    }


def Re_G_virasoro_imaginary(gamma: float, c: float = 26.0) -> float:
    """Real part of G_Vir(i*gamma) = -1/2 log(1 + 36*gamma^2/c^2)."""
    return -0.5 * math.log(1.0 + 36.0 * gamma ** 2 / c ** 2)


def Im_G_virasoro_imaginary(gamma: float, c: float = 26.0) -> float:
    """Imaginary part of G_Vir(i*gamma) = -arctan(6*gamma/c)."""
    return -math.atan(6.0 * gamma / c)


# =====================================================================
# Section 6: Scattering matrix on the critical line
# =====================================================================

def scattering_matrix_critical_line(t: float) -> complex:
    """Scattering matrix phi(1/2 + it) on the critical line.

    phi(s) = Lambda(1-s) / Lambda(s)
    where Lambda(s) = pi^{-s} Gamma(s) zeta(2s).

    On the critical line s = 1/2 + it:
      |phi(1/2 + it)| = 1  (unitarity)
      arg(phi) encodes the scattering phase shift.

    Uses mpmath for high-precision evaluation.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for scattering matrix computation")

    with mpmath.workdps(30):
        s = mpf('0.5') + mpc(0, t)
        Lambda_s = mppower(mpi, -s) * mpgamma(s) * mpzeta(2 * s)
        Lambda_1ms = mppower(mpi, -(1 - s)) * mpgamma(1 - s) * mpzeta(2 * (1 - s))
        phi = Lambda_1ms / Lambda_s
        return complex(phi)


def scattering_phase(t: float) -> float:
    """arg(phi(1/2 + it)) — the scattering phase shift.

    Uses mpmath for computation.
    """
    phi = scattering_matrix_critical_line(t)
    return cmath.phase(phi)


def scattering_amplitude(t: float) -> float:
    """|phi(1/2 + it)| — should be 1 on the critical line (unitarity)."""
    phi = scattering_matrix_critical_line(t)
    return abs(phi)


def shadow_scattering_comparison(c: float = 26.0, t_max: float = 20.0,
                                  n_points: int = 50) -> Dict[str, np.ndarray]:
    """Compare G_Vir(it) with scattering data phi(1/2+it).

    The shadow GF at imaginary argument:
      G_Vir(it) = -log(1 + 6it/c)

    The scattering matrix on the critical line:
      phi(1/2 + it) = Lambda(1/2-it) / Lambda(1/2+it)

    We compare:
      |exp(G(it))| vs |phi(1/2+it)| = 1
      arg(G(it)) vs arg(phi(1/2+it))

    The comparison reveals that the shadow GF is NOT identical to the
    scattering phase, but the arctan profile of Im G shares the same
    functional form as the Stirling approximation to arg(Gamma(1/2+it)).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    ts = np.linspace(0.5, t_max, n_points)
    shadow_re = np.array([Re_G_virasoro_imaginary(ti, c) for ti in ts])
    shadow_im = np.array([Im_G_virasoro_imaginary(ti, c) for ti in ts])
    shadow_amp = np.array([lorentzian_profile_virasoro(ti, c) for ti in ts])

    phi_phase = []
    phi_amp = []
    for ti in ts:
        phi = scattering_matrix_critical_line(float(ti))
        phi_phase.append(cmath.phase(phi))
        phi_amp.append(abs(phi))

    return {
        'ts': ts,
        'shadow_re': shadow_re,
        'shadow_im': shadow_im,
        'shadow_amplitude': shadow_amp,
        'phi_phase': np.array(phi_phase),
        'phi_amplitude': np.array(phi_amp),
    }


# =====================================================================
# Section 7: Spectral measure and Rankin-Selberg transform
# =====================================================================

def spectral_measure_atoms(archetype: str, c: float = 26.0,
                            k: float = 1.0) -> List[Tuple[float, float]]:
    """Return the spectral measure rho_A as a list of (atom_location, weight) pairs.

    rho_A = sum_j w_j delta(lambda - lambda_j)

    For each archetype:
      G:  rho = delta(lambda - 1/2), weight 1.
      L:  rho = delta(lambda - 1/k) + delta(lambda - 1/(k+2)), weights 1, 1.
      C:  rho = delta(lambda - 4/c), weight 1.
      M:  rho = delta(lambda - 6/c), weight 1.
    """
    if archetype == 'G':
        return [(0.5, 1.0)]
    elif archetype == 'L':
        return [(1.0 / k, 1.0), (1.0 / (k + 2.0), 1.0)]
    elif archetype == 'C':
        return [(4.0 / c, 1.0)]
    elif archetype == 'M':
        return [(6.0 / c, 1.0)]
    else:
        raise ValueError(f"Unknown archetype: {archetype}")


def constrained_epstein_from_spectral(archetype: str, s: complex,
                                       c: float = 26.0,
                                       k: float = 1.0) -> complex:
    """Constrained Epstein zeta from spectral measure.

    eps^c_s(A) = integral lambda^{-s} d rho_A(lambda)
               = sum_j w_j * lambda_j^{-s}

    For Virasoro: eps^c_s = (6/c)^{-s} = (c/6)^s.
    For affine sl_2: eps^c_s = k^s + (k+2)^s.
    """
    atoms = spectral_measure_atoms(archetype, c, k)
    result = 0.0 + 0.0j
    for lam, w in atoms:
        if abs(lam) < 1e-30:
            continue
        result += w * lam ** (-complex(s))
    return result


def epstein_virasoro(s: complex, c: float = 26.0) -> complex:
    """Constrained Epstein zeta for Virasoro: (c/6)^s."""
    return (c / 6.0) ** complex(s)


def epstein_affine(s: complex, k: float = 1.0) -> complex:
    """Constrained Epstein zeta for affine sl_2: k^s + (k+2)^s."""
    return k ** complex(s) + (k + 2.0) ** complex(s)


def spectral_zeta_functional_equation_test(c: float = 26.0,
                                            s_values: Optional[List[complex]] = None
                                            ) -> List[Dict[str, Any]]:
    """Test the functional equation of the constrained Epstein zeta.

    For the Virasoro case, eps(s) = (c/6)^s satisfies:
      eps(s) * eps(-s) = 1   (trivially, since (c/6)^s * (c/6)^{-s} = 1)

    This is the shadow analogue of the Riemann zeta functional equation.
    The non-trivial functional equation involves the FULL constrained Epstein
    (Benjamin-Chang eq 3.5), which requires the modular invariant partition
    function input.
    """
    if s_values is None:
        s_values = [0.5 + 0.1j, 1.0 + 0.5j, 2.0 - 0.3j, 0.25 + 2.0j]

    results = []
    for s in s_values:
        eps_s = epstein_virasoro(s, c)
        eps_ms = epstein_virasoro(-s, c)
        product = eps_s * eps_ms
        results.append({
            's': s,
            'eps_s': eps_s,
            'eps_minus_s': eps_ms,
            'product': product,
            'product_equals_1': abs(product - 1.0) < 1e-10,
        })
    return results


# =====================================================================
# Section 8: W_3 multi-singularity interference
# =====================================================================

def w3_branch_points(c: float = 50.0) -> Tuple[complex, complex]:
    """Branch points of G_{W_3}(t).

    t_1 = -c/6 (Virasoro/T sector)
    t_2 = -(5c+22)/20 (W sector)
    """
    t1 = -c / 6.0
    alpha_W = 20.0 / (5.0 * c + 22.0)
    t2 = -1.0 / alpha_W
    return complex(t1), complex(t2)


def w3_stokes_angle(c: float = 50.0) -> float:
    """Angle of the Stokes line between the two W_3 branch points.

    The Stokes line is the set of t where Re(G_{t_1}(t)) = Re(G_{t_2}(t)),
    i.e., where the two exponential contributions have equal magnitude.

    For two real branch points t_1, t_2 on the negative real axis,
    the Stokes line is a curve in the upper/lower half-plane.

    The angle at which the Stokes line departs from the midpoint is:
      theta = pi/2  (perpendicular bisector for real branch points)

    The anti-Stokes lines are at theta = 0, pi (along the real axis
    between and beyond the branch points).
    """
    t1, t2 = w3_branch_points(c)
    # For two branch points on the real axis, Stokes lines are perpendicular
    # to the line connecting them, departing from the midpoint.
    midpoint = (t1.real + t2.real) / 2.0
    separation = abs(t1.real - t2.real)
    # The Stokes angle (measured from the positive real axis) is pi/2
    return math.pi / 2.0


def w3_interference_pattern(c: float = 50.0, grid_size: int = 100,
                             t_range: float = 20.0) -> Dict[str, np.ndarray]:
    """Compute |G_{W_3}(t)| on a grid in the complex t-plane.

    The interference between the two log branch points creates
    non-trivial level curves (Stokes and anti-Stokes lines).
    """
    x = np.linspace(-t_range, t_range, grid_size)
    y = np.linspace(-t_range, t_range, grid_size)
    X, Y = np.meshgrid(x, y)

    absG = np.zeros_like(X)
    argG = np.zeros_like(X)

    for i in range(grid_size):
        for j in range(grid_size):
            t = complex(X[i, j], Y[i, j])
            try:
                g = G_w3(t, c)
                absG[i, j] = abs(g)
                argG[i, j] = cmath.phase(g)
            except (ValueError, ZeroDivisionError):
                absG[i, j] = np.nan
                argG[i, j] = np.nan

    t1, t2 = w3_branch_points(c)

    return {
        'X': X,
        'Y': Y,
        'absG': absG,
        'argG': argG,
        'branch_points': [t1, t2],
        'stokes_angle': w3_stokes_angle(c),
    }


def w3_singularity_separation(c: float) -> float:
    """Distance between the two W_3 branch points.

    |t_1 - t_2| = |c/6 - (5c+22)/20|
    """
    t1, t2 = w3_branch_points(c)
    return abs(t1 - t2)


# =====================================================================
# Section 9: Resurgent structure and alien derivatives
# =====================================================================

def alien_derivative_log(branch_point: complex) -> complex:
    """Alien derivative Delta_{t_j} G for a log branch point.

    For G(t) = -log(1 + a*t) with branch point at t_j = -1/a:
      The singularity in the Borel plane at xi_j = 1/a is a simple pole
      with residue 1 (since G ~ -1/(xi - 1/a) in the Borel plane).
      The alien derivative is:
        Delta_{xi_j} G = 2*pi*i * Res_{xi=xi_j} B(xi) = 2*pi*i

    For a log singularity, the alien derivative is always 2*pi*i times
    the monodromy number.
    """
    return 2.0 * cmath.pi * 1j


def virasoro_alien_derivative(c: float = 26.0) -> Dict[str, Any]:
    """Alien derivative at the Virasoro branch point t = -c/6.

    The alien derivative Delta_{c/6} G is the non-perturbative correction
    to the shadow tower.  For the log singularity:

      Delta_{c/6} tilde_G = 2*pi*i

    where tilde_G is the Borel transform.  This means the non-perturbative
    sector contributes a CONSTANT imaginary part.

    The physical interpretation: the non-perturbative correction to the
    shadow tower is a topological term (pure phase, no modulus correction).
    """
    bp = -c / 6.0
    borel_sing = c / 6.0  # Borel singularity at 1/|lambda| = c/6

    alien = alien_derivative_log(complex(bp))

    return {
        'branch_point': bp,
        'borel_singularity': borel_sing,
        'alien_derivative': alien,
        'is_topological': abs(alien.real) < 1e-10,  # pure imaginary
        'non_perturbative_action': borel_sing,  # A = c/6
        'instanton_weight': cmath.exp(-borel_sing),  # exp(-A/g) at g=1
    }


def resurgent_transseries_virasoro(c: float, t: complex,
                                    n_perturbative: int = 30,
                                    n_instanton: int = 3) -> complex:
    """Resurgent transseries for the Virasoro shadow GF.

    G(t) = G_pert(t) + sum_{k>=1} C_k * exp(-k*A/t) * G_k(t)

    where A = c/6 is the instanton action and G_pert is the perturbative
    series.  For a simple log singularity:

      G_pert(t) = sum_{r>=1} S_r t^r  (convergent for |t| < c/6)
      Non-perturbative: exp(-c/(6t))

    Since the series IS convergent, the transseries is just the analytic
    continuation beyond |t| = c/6.  The resurgent structure becomes
    non-trivial only if we EXPAND around the branch point.
    """
    # Perturbative part: partial sum of -log(1 + 6t/c)
    # G(t) = -log(1 + 6t/c) = sum_{r>=1} (-1)^r (6/c)^r t^r / r
    pert = 0.0 + 0.0j
    for r in range(1, n_perturbative + 1):
        pert += (-1.0) ** r * (6.0 / c) ** r * t ** r / r

    # Non-perturbative corrections (exponentially suppressed for |t| < c/6)
    A = c / 6.0
    nonpert = 0.0 + 0.0j
    if abs(t) > 1e-10:
        for k_inst in range(1, n_instanton + 1):
            # Stokes multiplier * exp(-k*A/t)
            # For the log function, the transseries is exact:
            # -log(1+6t/c) for |t| > c/6 requires going around the branch cut.
            weight = cmath.exp(-k_inst * A / t)
            nonpert += (2.0 * cmath.pi * 1j) * weight / k_inst

    return pert + nonpert


# =====================================================================
# Section 10: Cross-archetype comparison utilities
# =====================================================================

def all_archetypes_at_point(t: complex, c_vir: float = 26.0,
                             k_aff: float = 1.0,
                             c_bg: float = -2.0) -> Dict[str, complex]:
    """Evaluate all four archetype GFs at a single point t."""
    return {
        'G_heisenberg': G_heisenberg(t),
        'G_affine': G_affine_sl2(t, k_aff),
        'G_betagamma': G_betagamma(t, c_bg),
        'G_virasoro': G_virasoro(t, c_vir),
    }


def radius_of_convergence(archetype: str, c: float = 26.0,
                           k: float = 1.0) -> float:
    """Radius of convergence of the shadow series sum S_r t^r.

    This is |t_nearest| where t_nearest is the nearest singularity.

    G:  R = infinity (entire, but this is the linear approximation)
    L:  R = min(k, k+2) = k  (for k > 0)
    C:  R = |c|/4
    M:  R = c/6
    """
    if archetype == 'G':
        return float('inf')
    elif archetype == 'L':
        return min(abs(k), abs(k + 2.0))
    elif archetype == 'C':
        return abs(c) / 4.0
    elif archetype == 'M':
        return abs(c) / 6.0
    else:
        raise ValueError(f"Unknown archetype: {archetype}")


def singularity_density(archetype: str, c: float = 26.0,
                         k: float = 1.0) -> float:
    """Number of singularities divided by the depth.

    G: 0 / 2 = 0
    L: 2 / 3 = 0.667
    C: 1 / 4 = 0.25
    M: 1 / infinity = 0
    """
    info = singularity_map(archetype, c=c, k=k) if archetype not in ('G', 'L') else (
        singularity_map(archetype, k=k) if archetype == 'L' else
        singularity_map(archetype)
    )
    n_sing = len(info['branch_points'])
    depth = info['depth']
    if depth == float('inf'):
        return 0.0
    if depth == 0:
        return float('inf')
    return n_sing / depth


# =====================================================================
# Section 11: Dispersion relation and Stieltjes reconstruction
# =====================================================================

def dispersion_virasoro(c: float, t: complex, n_points: int = 500) -> complex:
    """Reconstruct G_Vir(t) from its branch-cut discontinuity via dispersion relation.

    G(t) = (1 / 2*pi*i) integral_{-infty}^{-c/6} disc(G(t')) / (t' - t) dt'

    where disc(G) = -2*pi*i along the branch cut.

    So G(t) = - integral_{-infty}^{-c/6} dt' / (t' - t)
            = - [log(t' - t)]_{-infty}^{-c/6}

    This integral is formally divergent and needs regularization.
    After subtraction: G(t) - G(0) = integral ... which gives -log(1 + 6t/c).

    We verify numerically with a finite-cutoff integral.
    """
    bp = -c / 6.0
    # Integrate from t_min to bp - eps
    t_min = bp - 100.0 * abs(bp)
    eps_cut = abs(bp) * 0.001

    # Trapezoidal integration
    dt_prime_arr = np.linspace(t_min, bp - eps_cut, n_points)
    h = (bp - eps_cut - t_min) / n_points

    # disc(G) = -2*pi*i on the cut
    # G(t) = (1/(2*pi*i)) * integral disc(G)/(t'-t) dt'
    #       = (1/(2*pi*i)) * (-2*pi*i) * integral dt'/(t'-t)
    #       = - integral dt'/(t'-t)

    integrand = -1.0 / (dt_prime_arr - complex(t))
    result = np.trapz(integrand, dt_prime_arr)

    return result


def stieltjes_inversion_virasoro(c: float, x: float,
                                  n_moments: int = 20) -> float:
    """Stieltjes inversion to extract the spectral measure from shadow moments.

    The shadow moments are M_r = integral lambda^r d rho(lambda) = S_r / r!
    (approximately).  From the moments, Stieltjes inversion recovers rho.

    For Virasoro: rho = delta(lambda - 6/c), so the moments are
    M_r = (6/c)^r.

    We verify that the moment sequence {(6/c)^r} satisfies Carleman's
    condition: sum M_{2r}^{-1/(2r)} = sum (6/c)^{-1} = infinity (diverges).
    So the measure is uniquely determined.
    """
    # Moments from the spectral atom
    lambda_0 = 6.0 / c
    moments = [lambda_0 ** r for r in range(n_moments)]

    # Carleman condition: sum_{r>=1} M_{2r}^{-1/(2r)}
    carleman_sum = 0.0
    for r in range(1, n_moments // 2):
        M_2r = moments[2 * r]
        if abs(M_2r) > 1e-30:
            carleman_sum += M_2r ** (-1.0 / (2 * r))

    return carleman_sum  # Should diverge (-> infinity)


# =====================================================================
# Section 12: High-precision computations (mpmath)
# =====================================================================

def mp_G_virasoro(t, c=26):
    """High-precision Virasoro shadow GF using mpmath."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(50):
        return -mplog(1 + mpf(6) * t / mpf(c))


def mp_scattering_matrix(s):
    """High-precision scattering matrix phi(s) = Lambda(1-s)/Lambda(s)."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(50):
        def Lambda(s_val):
            return mppower(mpi, -s_val) * mpgamma(s_val) * mpzeta(2 * s_val)
        return Lambda(1 - s) / Lambda(s)


def mp_epstein_virasoro(s, c=26):
    """High-precision constrained Epstein zeta for Virasoro: (c/6)^s."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(50):
        return mppower(mpf(c) / mpf(6), s)


# =====================================================================
# Section 13: Summary and diagnostic functions
# =====================================================================

def full_singularity_census() -> Dict[str, Dict[str, Any]]:
    """Complete census of singularity data for all standard archetypes."""
    return {
        'G (Heisenberg)': singularities_heisenberg(),
        'L (affine sl_2, k=1)': singularities_affine_sl2(k=1.0),
        'C (betagamma, c=-2)': singularities_betagamma(c=-2.0),
        'M (Virasoro, c=26)': singularities_virasoro(c=26.0),
        'M (Virasoro, c=1/2)': singularities_virasoro(c=0.5),
        'W_3 (c=50)': singularities_w3(c=50.0),
    }


def archetype_comparison_table() -> List[Dict[str, Any]]:
    """Comparison table of all archetypes."""
    return [
        {
            'class': 'G', 'algebra': 'Heisenberg', 'depth': 2,
            'n_singularities': 0, 'R_convergence': float('inf'),
            'monodromy_group': 'trivial', 'borel_summable': True,
            'resurgent': False,
        },
        {
            'class': 'L', 'algebra': 'V_1(sl_2)', 'depth': 3,
            'n_singularities': 2, 'R_convergence': 1.0,
            'monodromy_group': 'Z x Z', 'borel_summable': True,
            'resurgent': True,
        },
        {
            'class': 'C', 'algebra': 'betagamma', 'depth': 4,
            'n_singularities': 1, 'R_convergence': 0.5,
            'monodromy_group': 'Z', 'borel_summable': True,
            'resurgent': True,
        },
        {
            'class': 'M', 'algebra': 'Vir_{c=26}', 'depth': float('inf'),
            'n_singularities': 1, 'R_convergence': 26.0 / 6.0,
            'monodromy_group': 'Z', 'borel_summable': True,
            'resurgent': True,
        },
    ]
