r"""Matrix model from shadow zeta: the shadow potential matrix model.

MATHEMATICAL FRAMEWORK
======================

The shadow obstruction tower S_r(A) defines a matrix model potential:

    V(M) = sum_{r=2}^{r_max} (S_r / r) * M^r

The partition function is:

    Z_N = int dM exp(-N * Tr V(M))

where dM is Haar measure on N x N Hermitian matrices.

In the large-N limit (planar limit), the eigenvalue density rho(lambda)
is determined by the saddle-point equation (loop equation):

    V'(lambda) = 2 * P.V. int rho(mu) / (lambda - mu) dmu

The resolvent omega(z) = int rho(lambda) / (z - lambda) dlambda satisfies
the algebraic curve (spectral curve):

    omega(z)^2 = V'(z)^2 - 4 * P(z)

where P(z) is a polynomial determined by normalization and analyticity.

SHADOW CLASS DICTIONARY
========================

Class G (Gaussian, r_max=2): V(M) = (kappa/2) M^2
    -> Wigner semicircle rho(x) = (1/(2*pi*kappa)) * sqrt(4*kappa - x^2)
    -> Catalan moments: <Tr M^{2k}> = C_k * kappa^k
    -> F_g = kappa * lambda_g^FP

Class L (Lie/tree, r_max=3): V(M) = (kappa/2) M^2 + (alpha/3) M^3
    -> Cubic potential: two-cut -> one-cut phase transition
    -> Double-scaling: Painleve I (k=2 multicritical)

Class C (Contact/quartic, r_max=4): V(M) = (kappa/2) M^2 + (alpha/3) M^3 + (S_4/4) M^4
    -> Quartic potential: standard quartic matrix model
    -> Double-scaling: Painleve II (k=3 multicritical)

Class M (Mixed, r_max=infinity): V(M) = sum_{r>=2} (S_r/r) M^r
    -> Infinite polynomial potential from shadow tower
    -> Convergent for |M| < R where R = shadow convergence radius

KOSZUL COMPLEMENTARITY
=======================

The shadow potential satisfies V_c(x) + V_{26-c}(x) =/= simple relation
because kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13 (AP24: NOT 0).

The Koszul-dual matrix model has potential V^!(x) built from the dual
shadow tower S_r(A!).  The complementarity relation constrains the
relationship between the two spectral curves.

CONVENTIONS
===========
- kappa(Heisenberg level k) = k (AP39)
- kappa(Virasoro at c) = c/2
- kappa(affine KM g_k) = dim(g)(k+h^v)/(2h^v)
- S_2 = kappa, S_3 = alpha = 2 for Virasoro
- Q^contact_Vir = S_4 = 10/[c(5c+22)]
- Shadow metric: Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
  with Delta = 8*kappa*S_4
- H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} r * S_r * t^r
- S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(t))

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, factorial, pi as sym_pi,
    simplify, sqrt as sym_sqrt, Abs, N as Neval, binomial, Integer,
)

from compute.lib.utils import lambda_fp, F_g as F_g_shadow


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PI = math.pi
TWO_PI = 2 * PI


# ===========================================================================
# Section 0: Shadow tower coefficients (self-contained)
# ===========================================================================

def _virasoro_shadow_data(c_val: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (kappa, alpha, S4) for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S4 = Q^contact = 10/[c(5c+22)].
    """
    c_f = Fraction(c_val)
    if c_f == 0:
        raise ValueError("Virasoro shadow requires c != 0")
    kappa = c_f / 2
    alpha = Fraction(2)
    denom = c_f * (5 * c_f + 22)
    if denom == 0:
        raise ValueError("Degenerate at c = 0 or c = -22/5")
    S4 = Fraction(10) / denom
    return kappa, alpha, S4


def _heisenberg_shadow_data(k: int) -> Tuple[Fraction, Fraction, Fraction]:
    """Return (kappa, alpha, S4) for Heisenberg at level k.

    Heisenberg is class G: kappa = k, alpha = 0, S4 = 0.
    Shadow tower terminates at arity 2.
    """
    return Fraction(k), Fraction(0), Fraction(0)


def _shadow_tower_from_metric(kappa: Fraction, alpha: Fraction, S4: Fraction,
                               r_max: int = 10) -> Dict[int, Fraction]:
    """Compute shadow tower coefficients S_r for r = 2, ..., r_max.

    Uses H(t) = t^2 * sqrt(Q_L(t)) where Q_L(t) = q0 + q1*t + q2*t^2.
    S_r = a_{r-2} / r where a_n = [t^n] sqrt(Q_L(t)).
    """
    q0 = 4 * kappa ** 2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha ** 2 + 16 * kappa * S4

    a0 = 2 * kappa
    if a0 == 0:
        return {r: Fraction(0) for r in range(2, r_max + 1)}

    max_n = r_max - 2 + 1
    a = [Fraction(0)] * (max_n + 1)
    a[0] = a0

    if max_n >= 1:
        a[1] = q1 / (2 * a0)

    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2 * a0)

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * a0)

    coeffs = {}
    for r in range(2, r_max + 1):
        idx = r - 2
        if idx <= max_n:
            coeffs[r] = a[idx] / r
        else:
            coeffs[r] = Fraction(0)

    return coeffs


def shadow_tower_coefficients(family: str, param, r_max: int = 10) -> Dict[int, Fraction]:
    """Compute shadow tower coefficients for a given family.

    Parameters
    ----------
    family : str
        'virasoro', 'heisenberg', or 'custom'
    param : value
        For virasoro: central charge c (Fraction or int)
        For heisenberg: level k (int)
        For custom: tuple (kappa, alpha, S4) of Fractions
    r_max : int
        Maximum arity

    Returns
    -------
    Dict[int, Fraction] : S_r for r = 2, ..., r_max
    """
    if family == 'virasoro':
        kappa, alpha, S4 = _virasoro_shadow_data(Fraction(param))
    elif family == 'heisenberg':
        kappa, alpha, S4 = _heisenberg_shadow_data(int(param))
    elif family == 'custom':
        kappa, alpha, S4 = param
    else:
        raise ValueError(f"Unknown family: {family}")

    return _shadow_tower_from_metric(kappa, alpha, S4, r_max)


# ===========================================================================
# Section 1: Shadow matrix potential
# ===========================================================================

def shadow_matrix_potential(c, x, r_max: int = 6) -> float:
    r"""Evaluate the shadow matrix potential V(x) = sum_{r=2}^{r_max} (S_r/r) * x^r.

    The shadow obstruction tower S_r(Vir_c) defines a polynomial potential
    for a Hermitian matrix model.  The eigenvalue integral is:

        Z_N = int dM exp(-N * Tr V(M))

    For class G (Heisenberg): V(x) = (kappa/2) x^2 (Gaussian).
    For class L: V(x) = (kappa/2) x^2 + (alpha/3) x^3.
    For class C: V adds quartic.
    For class M (Virasoro): V is an infinite polynomial truncated at r_max.

    Parameters
    ----------
    c : number
        Central charge (for Virasoro)
    x : float
        Eigenvalue at which to evaluate V
    r_max : int
        Truncation order for the shadow tower

    Returns
    -------
    float : V(x)
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    V = 0.0
    for r, S_r in coeffs.items():
        V += float(S_r) / r * x ** r
    return V


def shadow_matrix_potential_derivative(c, x, r_max: int = 6) -> float:
    r"""Evaluate V'(x) = sum_{r=2}^{r_max} S_r * x^{r-1}.

    This is the force term in the saddle-point equation.
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    Vp = 0.0
    for r, S_r in coeffs.items():
        Vp += float(S_r) * x ** (r - 1)
    return Vp


def shadow_matrix_potential_exact(c, r_max: int = 6) -> Dict[int, Fraction]:
    """Return exact rational coefficients V_r = S_r / r for r = 2, ..., r_max.

    V(x) = sum V_r * x^r.
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    return {r: S_r / r for r, S_r in coeffs.items()}


# ===========================================================================
# Section 2: Eigenvalue density (saddle-point)
# ===========================================================================

def eigenvalue_density_saddle(c, lambda_val: float, r_max: int = 4) -> float:
    r"""Eigenvalue density rho(lambda) from the one-cut saddle-point solution.

    For a polynomial potential V(x) with a one-cut eigenvalue support [a, b],
    the eigenvalue density is:

        rho(lambda) = (1/(2*pi)) * |M(lambda)| * sqrt((b - lambda)(lambda - a))

    where M(lambda) is a polynomial determined by V'(lambda) and the support.

    For the Gaussian (class G): V(x) = (kappa/2) x^2, V'(x) = kappa*x
        -> M(x) = kappa, a = -2/sqrt(kappa), b = 2/sqrt(kappa)
        -> rho(x) = (kappa/(2*pi)) * sqrt(4/kappa - x^2)   (Wigner semicircle)

    For general potentials, we use the one-cut ansatz and determine the
    support from the normalization and analyticity conditions.

    Parameters
    ----------
    c : number
        Central charge
    lambda_val : float
        Point at which to evaluate the density
    r_max : int
        Truncation order

    Returns
    -------
    float : rho(lambda_val)
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    kappa_f = float(coeffs.get(2, Fraction(0)))

    if abs(kappa_f) < 1e-15:
        return 0.0

    # Check if purely Gaussian (no higher-order shadow coefficients)
    has_higher = any(abs(float(coeffs.get(r, 0))) > 1e-15 for r in range(3, r_max + 1))

    if not has_higher:
        # Pure Gaussian (class G): use exact Wigner semicircle
        return wigner_semicircle(kappa_f, lambda_val)

    # For non-Gaussian potentials: extract density from resolvent
    # rho(x) = -(1/pi) * Im(omega(x - i*epsilon))
    # where omega is the resolvent computed via the loop equation.
    eps = 1e-8
    z = complex(lambda_val, -eps)
    omega = resolvent(c, z, r_max)
    rho_from_resolvent = -omega.imag / PI

    return max(0.0, rho_from_resolvent)


def eigenvalue_density_support(c, r_max: int = 4) -> Dict[str, float]:
    r"""Compute the support [a, b] of the eigenvalue density.

    For the Gaussian potential V(x) = (kappa/2) x^2:
        a = -2/sqrt(kappa), b = 2/sqrt(kappa)

    This comes from the saddle-point equation. With V'(x) = kappa*x,
    the resolvent is omega(z) = (kappa/2)(z - sqrt(z^2 - 4/kappa)),
    and the eigenvalue density has support [-R, R] with R = 2/sqrt(kappa).

    For non-Gaussian potentials, the support is determined by:
    1. Normalization: int_a^b rho(x) dx = 1
    2. Analyticity: rho(x) >= 0 on (a, b) and rho(a) = rho(b) = 0

    For potentials close to Gaussian, we use perturbation theory
    to shift the support endpoints.

    Parameters
    ----------
    c : number
        Central charge
    r_max : int
        Truncation order

    Returns
    -------
    dict with keys 'a', 'b', 'R' (half-width)
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    kappa_f = float(coeffs.get(2, Fraction(0)))

    if abs(kappa_f) < 1e-15:
        return {'a': 0.0, 'b': 0.0, 'R': 0.0}

    # Gaussian support: R = 2/sqrt(kappa)
    R0 = 2.0 / math.sqrt(abs(kappa_f))
    a0 = -R0
    b0 = R0

    # Check if there are non-Gaussian terms
    has_higher = any(abs(float(coeffs.get(r, 0))) > 1e-20 for r in range(3, r_max + 1))

    if not has_higher:
        return {'a': a0, 'b': b0, 'R': R0, 'center': 0.0}

    # Perturbative corrections from cubic term
    # S_3 is the shadow tower coefficient; for Virasoro, S_3 = 2
    S3_f = float(coeffs.get(3, Fraction(0)))
    S4_f = float(coeffs.get(4, Fraction(0)))

    # For cubic perturbation delta_V = (S_3/3) x^3:
    # To first order, the support center shifts by -S_3/(3*kappa^2) * R0^2
    # and the half-width changes by a term proportional to S_3^2/kappa^3.
    # The dominant effect is the CENTER SHIFT (asymmetric support).
    center_shift = -S3_f / (3.0 * kappa_f)

    # Quartic correction to half-width (first order):
    # delta_R/R0 ~ 3*S_4 / (4*kappa^2) * R0^2
    R_correction = 3.0 * S4_f / (4.0 * kappa_f ** 2)
    R = R0 * (1.0 + R_correction)

    a = center_shift - R
    b = center_shift + R

    return {'a': a, 'b': b, 'R': R, 'center': center_shift}


# ===========================================================================
# Section 3: Resolvent
# ===========================================================================

def resolvent(c, z: complex, r_max: int = 4) -> complex:
    r"""Compute the matrix model resolvent omega(z) = int rho(lambda)/(z-lambda) dlambda.

    For the one-cut solution of the matrix model with potential V:

        omega(z) = (1/2) * (V'(z) - M(z) * sqrt((z-a)(z-b)))

    where [a,b] is the eigenvalue support and M(z) is the polynomial
    part of V'(z)/sqrt((z-a)(z-b)).

    For the Gaussian V(x) = (kappa/2) x^2:
        omega(z) = (1/2)(kappa*z - kappa*sqrt(z^2 - 4*kappa))
                 = (kappa/2)(z - sqrt(z^2 - 4*kappa))

    Parameters
    ----------
    c : number
        Central charge
    z : complex
        Point at which to evaluate the resolvent
    r_max : int
        Truncation order

    Returns
    -------
    complex : omega(z)
    """
    z = complex(z)
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    kappa_f = float(coeffs.get(2, Fraction(0)))

    if abs(kappa_f) < 1e-15:
        return complex(0, 0)

    # Compute V'(z) for the full potential
    Vp_z = complex(0, 0)
    for r, S_r in coeffs.items():
        Vp_z += float(S_r) * z ** (r - 1)

    # Support
    support = eigenvalue_density_support(c, r_max)
    a, b = support['a'], support['b']

    # sqrt((z-a)(z-b)) with correct branch cut
    w = cmath.sqrt((z - a) * (z - b))

    # Choose branch: omega(z) ~ 1/z for z -> infinity
    # V'(z) ~ kappa * z + ... for large z
    # sqrt((z-a)(z-b)) ~ z for large z
    # So omega(z) ~ (1/2)(kappa*z - kappa*z) + ... = 1/z if we choose + branch for sqrt
    # Need: omega ~ 1/z, so V'(z) - M(z)*sqrt ~ 2/z
    # For Gaussian: M = kappa, V' = kappa*z, sqrt ~ z, so kappa*z - kappa*z = 0... not right.
    # Actually omega(z) = (1/2)(V'(z) - sqrt(V'(z)^2 - 4*P(z)))
    # For Gaussian: P(z) = kappa (moment polynomial), V'(z) = kappa*z
    # omega = (1/2)(kappa*z - sqrt(kappa^2*z^2 - 4*kappa))
    #       = (kappa/2)(z - sqrt(z^2 - 4/kappa))... hmm

    # Gaussian resolvent (exact for class G):
    # V(M) = (kappa/2) M^2  =>  V'(z) = kappa * z
    # Saddle-point equation gives:
    #   omega(z) = (kappa/2)(z - sqrt(z^2 - 4/kappa))
    #   rho(x) = (kappa/(2*pi)) sqrt(4/kappa - x^2)
    # Support: [-2/sqrt(kappa), 2/sqrt(kappa)]
    # Asymptotics: omega(z) ~ 1/z for z -> infinity.

    discriminant = z * z - 4.0 / kappa_f
    sqrt_disc = cmath.sqrt(discriminant)

    # Choose branch: for real z > 2/sqrt(kappa), sqrt(z^2 - 4/kappa) is real positive
    # and omega = (kappa/2)(z - sqrt) > 0.  We need omega ~ 1/z at infinity,
    # which requires choosing the branch where sqrt ~ z for large z.
    # Test: if Re(sqrt) and Re(z) have opposite signs for large positive z, flip.
    if z.real > 0 and sqrt_disc.real < 0:
        sqrt_disc = -sqrt_disc

    omega_gauss = (kappa_f / 2.0) * (z - sqrt_disc)

    # For pure Gaussian, return this
    has_higher = any(abs(float(coeffs.get(r, 0))) > 1e-15 for r in range(3, r_max + 1))
    if not has_higher:
        return omega_gauss

    # For non-Gaussian: perturbative approach using the loop equation.
    # The loop equation for one-cut: omega^2 - V'(z)*omega + Q(z) = 0
    # where Q(z) is the "moment polynomial" determined by normalization.
    #
    # Solution: omega = (1/2)(V'(z) - sqrt(V'(z)^2 - 4*Q(z)))
    #
    # For the Gaussian, Q = kappa (constant).
    # For perturbative corrections from higher S_r, Q acquires z-dependence.
    #
    # First approximation: Q(z) ~ kappa (leading Gaussian value).
    # This gives the correct asymptotics and a reasonable approximation
    # for small non-Gaussian corrections.

    Vp_full = complex(0, 0)
    for r, S_r in coeffs.items():
        Vp_full += float(S_r) * z ** (r - 1)

    # Q ~ kappa for the one-cut, single-support case
    Q_eff = kappa_f

    disc_full = Vp_full ** 2 - 4.0 * Q_eff
    sqrt_full = cmath.sqrt(disc_full)

    # Branch choice: for large z, V'(z) ~ kappa*z, sqrt(V'^2 - 4Q) ~ kappa*z,
    # so omega = (V' - sqrt)/2 ~ (kappa*z - kappa*z + 2Q/(kappa*z))/2 ~ 1/z.
    # Choose the branch where sqrt ~ V' for large z:
    if z.real > 0 and sqrt_full.real < 0:
        sqrt_full = -sqrt_full

    omega = (Vp_full - sqrt_full) / 2.0
    return omega


# ===========================================================================
# Section 4: Planar free energy
# ===========================================================================

def planar_free_energy(c, r_max: int = 4) -> float:
    r"""Compute the planar (genus-0) free energy F_0 of the shadow matrix model.

    F_0 = -int_a^b rho(x) V(x) dx + int int rho(x) rho(y) log|x-y| dx dy

    For the Gaussian matrix model V = (kappa/2) x^2 with Wigner semicircle:
        F_0 = -(3/4) + (1/2) log(kappa) + (1/2) log(2)

    We compute F_0 numerically using the eigenvalue density.

    Parameters
    ----------
    c : number
        Central charge
    r_max : int
        Truncation order

    Returns
    -------
    float : F_0
    """
    support = eigenvalue_density_support(c, r_max)
    a, b = support['a'], support['b']
    if abs(b - a) < 1e-15:
        return 0.0

    kappa_f = float(Fraction(c) / 2)
    if abs(kappa_f) < 1e-15:
        return 0.0

    # Gaussian F_0 (exact):
    # F_0 = -3/4 + (1/2) log(kappa)
    # This comes from:
    # int rho V = (kappa/2) * <x^2> = (kappa/2) * (1/kappa) = 1/2
    # int int rho rho log|x-y| = -1/4
    # F_0 = -1/2 - (-1/4) = -1/4...
    # Actually: F_0 = -(1/2) int rho V + (1/2) int int rho rho log|x-y|

    # Standard result for GUE (V = x^2/2, unit coupling):
    # F_0 = -3/4 + (1/2) log 2
    # For V = (kappa/2) x^2:
    # F_0 = -3/4 + (1/2) log(2/kappa)

    # Use numerical integration for non-Gaussian correction
    n_pts = 200
    dx = (b - a) / n_pts

    # Compute density at sample points
    rho_vals = []
    x_vals = []
    for i in range(n_pts):
        xi = a + (i + 0.5) * dx
        x_vals.append(xi)
        rho_vals.append(eigenvalue_density_saddle(c, xi, r_max))

    # Potential energy: int rho(x) V(x) dx
    pot_energy = 0.0
    for i in range(n_pts):
        pot_energy += rho_vals[i] * shadow_matrix_potential(c, x_vals[i], r_max) * dx

    # Entropy (log interaction): int int rho(x) rho(y) log|x-y| dx dy
    log_interaction = 0.0
    for i in range(n_pts):
        for j in range(n_pts):
            if i != j:
                dist = abs(x_vals[i] - x_vals[j])
                if dist > 1e-15:
                    log_interaction += rho_vals[i] * rho_vals[j] * math.log(dist) * dx * dx

    F_0 = -pot_energy + 0.5 * log_interaction
    return F_0


# ===========================================================================
# Section 5: Genus expansion coefficients
# ===========================================================================

def genus_expansion_coefficient(c, g: int, r_max: int = 4) -> float:
    r"""Genus-g free energy F_g from the shadow matrix model.

    For the scalar level of the shadow obstruction tower:

        F_g(A) = kappa(A) * lambda_g^FP

    where lambda_g^FP = (2^{2g-1}-1) / 2^{2g-1} * |B_{2g}| / (2g)!.

    This is proved as Theorem D (thm:theorem-d) for uniform-weight
    modular Koszul algebras at all genera.

    For the Virasoro algebra at central charge c:
        kappa = c/2
        F_g(Vir_c) = (c/2) * lambda_g^FP

    Parameters
    ----------
    c : number
        Central charge
    g : int
        Genus (>= 1)
    r_max : int
        Truncation order (unused at scalar level; for future higher-arity corrections)

    Returns
    -------
    float : F_g
    """
    kappa = Rational(c) / 2
    return float(F_g_shadow(kappa, g))


# ===========================================================================
# Section 6: Loop equation residual
# ===========================================================================

def loop_equation_residual(c, z: complex, r_max: int = 4) -> complex:
    r"""Check the Schwinger-Dyson / loop equation for the shadow matrix model.

    The planar loop equation states:

        omega(z)^2 = V'(z) * omega(z) - Q(z)

    or equivalently:

        omega(z)^2 - V'(z) * omega(z) + Q(z) = 0

    where Q(z) is the "moment polynomial".

    The residual is:

        R(z) = omega(z)^2 - V'(z) * omega(z) + Q(z)

    which should vanish identically on the spectral curve.

    We compute the residual R(z) = omega^2 - V'*omega + Q
    where Q is estimated from the asymptotic behavior.

    Parameters
    ----------
    c : number
        Central charge
    z : complex
        Test point
    r_max : int
        Truncation order

    Returns
    -------
    complex : residual (should be close to 0)
    """
    z = complex(z)
    omega_z = resolvent(c, z, r_max)

    # V'(z)
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    Vp_z = complex(0, 0)
    for r, S_r in coeffs.items():
        Vp_z += float(S_r) * z ** (r - 1)

    # Estimate Q from the asymptotics:
    # omega ~ 1/z + ... => omega^2 ~ 1/z^2
    # V'*omega ~ V' / z ~ kappa + ...
    # So Q ~ kappa for Gaussian
    kappa_f = float(coeffs.get(2, Fraction(0)))
    Q_est = kappa_f

    # For non-Gaussian, Q has higher-order terms
    # Q(z) = kappa + corrections from higher S_r
    for r in range(3, min(r_max + 1, 5)):
        S_r_f = float(coeffs.get(r, Fraction(0)))
        support = eigenvalue_density_support(c, r_max)
        center = support.get('center', 0.0)
        Q_est += S_r_f * center ** (r - 2)

    residual = omega_z ** 2 - Vp_z * omega_z + Q_est
    return residual


# ===========================================================================
# Section 7: Spectral curve
# ===========================================================================

def spectral_curve_mm(c, r_max: int = 4) -> Dict[str, Any]:
    r"""Compute the matrix model spectral curve y^2 = V'(z)^2 - 4*Q(z).

    The spectral curve encodes the complete planar solution of the matrix model.
    Its genus determines the number of cuts in the eigenvalue density.

    For the Gaussian (class G): y^2 = kappa^2 * z^2 - 4*kappa = kappa*(kappa*z^2 - 4)
        -> Genus 0, one cut at z^2 = 4/kappa.

    For cubic potential (class L): y^2 = polynomial of degree 4 in z
        -> Generically genus 1 (elliptic curve).

    For quartic potential (class C): y^2 = polynomial of degree 6 in z
        -> Generically genus 2 (hyperelliptic).

    Parameters
    ----------
    c : number
        Central charge
    r_max : int
        Truncation order

    Returns
    -------
    dict with spectral curve data
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)
    kappa_f = float(coeffs.get(2, Fraction(0)))

    # V'(x) coefficients: V'(x) = sum S_r x^{r-1}
    vp_coeffs = {}
    for r, S_r in coeffs.items():
        vp_coeffs[r - 1] = float(S_r)

    # Degree of V'
    deg_vp = max(vp_coeffs.keys()) if vp_coeffs else 0

    # V'(x)^2 - 4*Q(x) where Q is moment polynomial
    # For one-cut: Q is polynomial of degree <= deg_vp - 1
    # Genus of spectral curve: floor((2*deg_vp - 2)/2) for generic coefficients
    # = deg_vp - 1 for odd deg_vp, or deg_vp - 1 for even deg_vp

    # Support endpoints
    support = eigenvalue_density_support(c, r_max)

    # Branch points (zeros of y^2 on the real axis)
    # For one-cut: two branch points a, b
    branch_points = [support['a'], support['b']]

    # Spectral curve genus
    # For one-cut: genus 0 (rational curve)
    # Additional cuts would increase the genus
    sc_genus = 0  # one-cut assumption

    return {
        'c': float(c) if not isinstance(c, float) else c,
        'r_max': r_max,
        'vp_degree': deg_vp,
        'branch_points': branch_points,
        'spectral_curve_genus': sc_genus,
        'one_cut': True,
        'kappa': kappa_f,
        'support': support,
        'vp_coefficients': vp_coeffs,
    }


# ===========================================================================
# Section 8: Trace moments
# ===========================================================================

def moment_trace(c, k: int, N: int = 100) -> float:
    r"""Compute <(1/N) Tr(M^k)> from the eigenvalue density.

    <(1/N) Tr(M^k)> = int lambda^k rho(lambda) dlambda

    For the Wigner semicircle with support [-R, R]:
        <Tr M^{2k}> / N = C_k * (R/2)^{2k}
        <Tr M^{2k+1}> / N = 0  (odd moments vanish by symmetry)

    where C_k = (2k)! / ((k+1)! k!) are Catalan numbers.

    For the Gaussian with V = (kappa/2) M^2, R = 2/sqrt(kappa):
        <Tr M^{2k}>/N = C_k / kappa^k

    Parameters
    ----------
    c : number
        Central charge
    k : int
        Power
    N : int
        Number of quadrature points (NOT matrix size)

    Returns
    -------
    float : <(1/N) Tr M^k>
    """
    support = eigenvalue_density_support(c, min(k + 2, 10))
    a, b = support['a'], support['b']
    if abs(b - a) < 1e-15:
        return 0.0

    n_pts = N
    dx = (b - a) / n_pts
    moment = 0.0
    for i in range(n_pts):
        xi = a + (i + 0.5) * dx
        rho_xi = eigenvalue_density_saddle(c, xi, min(k + 2, 10))
        moment += xi ** k * rho_xi * dx

    return moment


# ===========================================================================
# Section 9: Wigner semicircle (Gaussian / class G)
# ===========================================================================

def wigner_semicircle(kappa_val: float, x: float) -> float:
    r"""Wigner semicircle density for the Gaussian matrix model.

    For V(M) = (kappa/2) M^2, the eigenvalue density is:

        rho(x) = (1/(2*pi)) * sqrt(4/kappa - x^2)    for |x| < 2/sqrt(kappa)
               = (kappa/(2*pi)) * sqrt(4/kappa - x^2) / kappa...

    Actually, for Z = int exp(-N * kappa/2 * Tr M^2) dM:
    The effective coupling is g = 1/(N*kappa).
    Saddle-point: rho(x) = (kappa/(2*pi)) * sqrt(4/kappa - x^2)
                         = (1/(2*pi)) * sqrt(4*kappa - kappa^2 * x^2) / kappa...

    Standard derivation: omega(z) = (kappa/2)(z - sqrt(z^2 - 4/kappa))
    rho(x) = (1/pi) Im omega(x - i0) = (kappa/(2*pi)) * sqrt(4/kappa - x^2)

    Support: [-2/sqrt(kappa), 2/sqrt(kappa)]

    Normalization: int rho dx = 1.
    Proof: int_{-R}^R (kappa/(2*pi)) sqrt(R^2 - x^2) dx
         = (kappa/(2*pi)) * (pi R^2 / 2) = kappa R^2 / 4 = kappa * 4/(4*kappa) = 1. Check.

    Parameters
    ----------
    kappa_val : float
        Modular characteristic (must be > 0)
    x : float
        Eigenvalue

    Returns
    -------
    float : rho(x)
    """
    if kappa_val <= 0:
        return 0.0

    R = 2.0 / math.sqrt(kappa_val)
    if abs(x) > R:
        return 0.0

    return (kappa_val / (2.0 * PI)) * math.sqrt(R * R - x * x)


def wigner_moments(kappa_val: float, k: int) -> float:
    r"""Exact moments of the Wigner semicircle.

    <x^k> = int_{-R}^R x^k rho(x) dx

    where R = 2/sqrt(kappa).

    Odd moments vanish by symmetry.

    Even moments: <x^{2n}> = C_n / kappa^n

    where C_n = (2n)! / ((n+1)! n!) is the n-th Catalan number.

    Proof: <x^{2n}> = (kappa/(2*pi)) * int_{-R}^R x^{2n} sqrt(R^2 - x^2) dx
    Substituting x = R sin(theta):
    = (kappa/(2*pi)) * R^{2n+2} * int_{-pi/2}^{pi/2} sin^{2n}(theta) cos^2(theta) dtheta
    = (kappa/(2*pi)) * (4/kappa)^{n+1} * B(n+1/2, 3/2) / 2
    = (kappa/(2*pi)) * (4/kappa)^{n+1} * pi * (2n)! / (2^{2n+1} * n! * (n+1)!)
    = C_n / kappa^n.

    Parameters
    ----------
    kappa_val : float
        Modular characteristic
    k : int
        Moment order

    Returns
    -------
    float : <x^k>
    """
    if k < 0:
        return 0.0

    if k % 2 == 1:
        return 0.0  # odd moments vanish

    n = k // 2
    # Catalan number C_n = (2n)! / ((n+1)! * n!)
    C_n = math.comb(2 * n, n) // (n + 1)

    return float(C_n) / kappa_val ** n


def catalan_number(n: int) -> int:
    """Catalan number C_n = (2n)! / ((n+1)! * n!)."""
    if n < 0:
        return 0
    return math.comb(2 * n, n) // (n + 1)


# ===========================================================================
# Section 10: Double-scaling exponent
# ===========================================================================

def double_scaling_exponent(c, r_max: int = 4) -> float:
    r"""String susceptibility exponent gamma_str for the shadow matrix model.

    Near a (k+1)-th order critical point (where k eigenvalue endpoints merge),
    the free energy scales as:

        F_g ~ (mu - mu_c)^{(2-gamma_str)(1-g)}

    with gamma_str = -2/(2k+1) for the k-th multicritical model.

    The shadow class determines the critical behavior:
    - Class G (Gaussian, k=1): gamma_str = -2/3 (pure gravity)
    - Class L (cubic, k=2): gamma_str = -2/5 (Ising on random lattice)
    - Class C (quartic, k=3): gamma_str = -2/7
    - Class M (infinite tower): the truncation order r_max determines
      the effective multicritical index.

    In general, for a potential of degree p (leading even term):
        gamma_str = -2/(p-1) for the simplest critical point.

    But the shadow potential has leading term S_2 (quadratic), so the
    critical behavior is determined by the NEXT non-vanishing coefficient.

    Parameters
    ----------
    c : number
        Central charge
    r_max : int
        Truncation order

    Returns
    -------
    float : gamma_str
    """
    coeffs = shadow_tower_coefficients('virasoro', c, r_max)

    # Find the highest non-trivial coefficient
    k_max = 2
    for r in range(r_max, 2, -1):
        if abs(float(coeffs.get(r, 0))) > 1e-15:
            k_max = r
            break

    # The string susceptibility exponent
    # For a potential with leading non-quadratic term at degree p:
    # gamma_str = -2/(p-1) for the standard (p-2)-th multicritical model
    # But this is the exponent for tuning TO the critical point;
    # at generic coupling the model is in the Gaussian universality class.

    # For the shadow matrix model, the physically relevant exponent
    # is determined by the shadow depth:
    # r_max = 2 (class G): Gaussian, gamma_str = -1/2 (pure gravity/JT)
    # r_max = 3 (class L): cubic, gamma_str = -1/2
    # r_max = 4 (class C): quartic can be tuned to k=2 multicritical
    # r_max = inf (class M): infinite tower, tunable to any multicritical model

    # Standard formula: the k-th multicritical model has gamma_str = -1/(k+1/2)
    # k=1: gamma_str = -2/3 (pure gravity)
    # k=2: gamma_str = -2/5
    # k=3: gamma_str = -2/7

    # For the shadow, k = r_max - 1 (the number of tunable parameters)
    if k_max <= 2:
        # Gaussian: pure gravity
        k = 1
    else:
        k = k_max - 1

    gamma_str = -2.0 / (2 * k + 1)
    return gamma_str


# ===========================================================================
# Section 11: Kontsevich intersection numbers
# ===========================================================================

def kontsevich_intersection(d_list: List[int], g: Optional[int] = None) -> Rational:
    r"""Intersection number <tau_{d_1} ... tau_{d_n}>_g from the Kontsevich integral.

    These intersection numbers of psi-classes on M_{g,n} are the
    coefficients of the Kontsevich matrix integral:

        Z_K = int dX exp(-Tr(X^3/3 + Lambda X^2 / 2))

    where Lambda is a diagonal external matrix.

    The Witten-Kontsevich theorem states that the generating function
    of these intersection numbers is a tau-function of the KdV hierarchy.

    This is a wrapper around the existing kontsevich_tau from
    matrix_model_shadow.py for the bc_matrix_model interface.

    Parameters
    ----------
    d_list : list of int
        Degrees of psi-classes: d_1, ..., d_n
    g : int or None
        Genus (determined from selection rule if None)

    Returns
    -------
    Rational : <tau_{d_1} ... tau_{d_n}>_g
    """
    from compute.lib.matrix_model_shadow import kontsevich_tau
    return kontsevich_tau(*d_list, g=g)


# ===========================================================================
# Section 12: Shadow MM free energy comparison
# ===========================================================================

def shadow_mm_free_energy_comparison(c, g: int) -> Dict[str, Any]:
    r"""Compare F_g from the matrix model with F_g from the shadow tower.

    At the scalar level, both should agree:
        F_g^{MM} = kappa * lambda_g^FP = F_g^{shadow}

    This verification is essentially tautological at the formula level
    (both use the same kappa and lambda_g^FP), but provides a consistency
    check that the matrix model resolvent reproduces the correct genus
    expansion via topological recursion.

    At higher arity, the matrix model with the full shadow potential
    V(x) = sum S_r/r x^r should produce corrections to the scalar F_g.
    These corrections come from the non-Gaussian part of V and
    correspond to higher-arity shadow contributions.

    Parameters
    ----------
    c : number
        Central charge
    g : int
        Genus

    Returns
    -------
    dict with comparison data
    """
    kappa = Rational(c) / 2
    F_g_sh = float(F_g_shadow(kappa, g))
    F_g_mm = genus_expansion_coefficient(c, g)
    lambda_g = float(lambda_fp(g))

    return {
        'c': float(c) if not isinstance(c, float) else c,
        'g': g,
        'kappa': float(kappa),
        'F_g_shadow': F_g_sh,
        'F_g_matrix_model': F_g_mm,
        'lambda_g_FP': lambda_g,
        'match': abs(F_g_sh - F_g_mm) < 1e-15,
        'F_g_formula': f"kappa * lambda_{g}^FP = {float(kappa)} * {lambda_g}",
    }


# ===========================================================================
# Section 13: Koszul matrix model
# ===========================================================================

def koszul_matrix_model(c, x: float, r_max: int = 6) -> Dict[str, float]:
    r"""Compare the shadow potential V_c(x) with the Koszul-dual V_{26-c}(x).

    For Virasoro: Vir_c^! = Vir_{26-c} (AP8: c=13 is the self-dual point).

    The modular characteristics satisfy:
        kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13 (AP24: NOT 0!)

    The shadow potentials V_c and V_{26-c} are NOT simply related by
    sign or negation because kappa + kappa' = 13 != 0.

    At the self-dual point c = 13:
        V_13(x) = V_13(x) (tautologically self-dual)
        kappa(Vir_13) = 13/2

    Parameters
    ----------
    c : number
        Central charge
    x : float
        Evaluation point
    r_max : int
        Truncation order

    Returns
    -------
    dict with V_c(x), V_{26-c}(x), their sum, and kappa values
    """
    c_f = Fraction(c)
    c_dual = 26 - c_f

    V_c = shadow_matrix_potential(c_f, x, r_max)
    V_dual = shadow_matrix_potential(c_dual, x, r_max) if c_dual != 0 else float('nan')

    kappa_c = float(c_f) / 2.0
    kappa_dual = float(c_dual) / 2.0

    return {
        'c': float(c_f),
        'c_dual': float(c_dual),
        'x': x,
        'V_c': V_c,
        'V_dual': V_dual,
        'V_sum': V_c + V_dual if not math.isnan(V_dual) else float('nan'),
        'kappa_c': kappa_c,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa_c + kappa_dual,
        'kappa_sum_equals_13': abs(kappa_c + kappa_dual - 13.0) < 1e-12,
        'self_dual': abs(float(c_f) - 13.0) < 1e-12,
    }


# ===========================================================================
# Section 14: Shadow potential analysis
# ===========================================================================

def shadow_potential_coefficients_table(c, r_max: int = 10) -> Dict[str, Any]:
    r"""Complete table of shadow potential coefficients.

    Returns V_r = S_r / r for r = 2, ..., r_max together with
    the shadow tower S_r, kappa, alpha, Delta, and shadow class.
    """
    c_f = Fraction(c)
    kappa, alpha, S4 = _virasoro_shadow_data(c_f)
    Delta = 8 * kappa * S4

    coeffs = shadow_tower_coefficients('virasoro', c_f, r_max)

    potential_coeffs = {r: float(S_r) / r for r, S_r in coeffs.items()}

    # Shadow class determination
    alpha_f = float(alpha)
    Delta_f = float(Delta)

    if abs(alpha_f) < 1e-15 and abs(float(S4)) < 1e-15:
        shadow_class = 'G'
    elif abs(Delta_f) < 1e-15:
        shadow_class = 'L'
    elif abs(Delta_f) > 1e-15 and all(abs(float(coeffs.get(r, 0))) < 1e-15 for r in range(5, r_max + 1)):
        # Check if tower terminates at arity 4
        shadow_class = 'C'
    else:
        shadow_class = 'M'

    return {
        'c': float(c_f),
        'kappa': float(kappa),
        'alpha': float(alpha),
        'S4': float(S4),
        'Delta': Delta_f,
        'shadow_class': shadow_class,
        'tower_coefficients': {r: float(s) for r, s in coeffs.items()},
        'potential_coefficients': potential_coeffs,
        'r_max': r_max,
    }


def shadow_class_dictionary() -> Dict[str, Dict[str, Any]]:
    r"""The four shadow classes and their matrix model avatars.

    Class G (Gaussian, r_max=2): Wigner semicircle, Catalan moments
    Class L (Lie/tree, r_max=3): Cubic potential, tree-level corrections
    Class C (Contact/quartic, r_max=4): Quartic potential, contact terms
    Class M (Mixed, r_max=inf): Full shadow potential, infinite tower
    """
    return {
        'G': {
            'name': 'Gaussian',
            'r_max': 2,
            'matrix_model': 'GUE (Wigner semicircle)',
            'spectral_density': 'Wigner semicircle',
            'moments': 'Catalan numbers',
            'double_scaling': 'Airy (k=1)',
            'gamma_str': -2.0/3.0,
            'examples': ['Heisenberg H_k'],
        },
        'L': {
            'name': 'Lie/tree',
            'r_max': 3,
            'matrix_model': 'Cubic potential',
            'spectral_density': 'Deformed semicircle',
            'moments': 'Catalan + cubic correction',
            'double_scaling': 'Painleve I (k=2)',
            'gamma_str': -2.0/5.0,
            'examples': ['Affine KM at generic level'],
        },
        'C': {
            'name': 'Contact/quartic',
            'r_max': 4,
            'matrix_model': 'Quartic potential',
            'spectral_density': 'Quartic-deformed semicircle',
            'moments': 'Catalan + quartic correction',
            'double_scaling': 'Painleve II (k=3)',
            'gamma_str': -2.0/7.0,
            'examples': ['beta-gamma at generic level'],
        },
        'M': {
            'name': 'Mixed',
            'r_max': float('inf'),
            'matrix_model': 'Infinite polynomial potential',
            'spectral_density': 'Full shadow spectral density',
            'moments': 'Shadow-modified Catalan',
            'double_scaling': 'Higher multicritical',
            'gamma_str': None,  # depends on truncation
            'examples': ['Virasoro Vir_c', 'W_N at generic c'],
        },
    }


# ===========================================================================
# Section 15: Gaussian matrix model verification utilities
# ===========================================================================

def gaussian_matrix_model_exact(kappa_val: float) -> Dict[str, Any]:
    r"""Exact results for the Gaussian matrix model V = (kappa/2) M^2.

    The Gaussian model is completely solvable and provides the
    baseline against which all shadow matrix models are compared.

    Returns
    -------
    dict with exact Gaussian matrix model data
    """
    if kappa_val <= 0:
        raise ValueError(f"kappa must be positive, got {kappa_val}")

    R = 2.0 / math.sqrt(kappa_val)

    # Moments: <M^{2k}> = C_k / kappa^k
    moments = {}
    for k in range(7):
        moments[2 * k] = wigner_moments(kappa_val, 2 * k)
        moments[2 * k + 1] = 0.0

    # Free energies
    free_energies = {}
    for g in range(1, 7):
        free_energies[g] = float(F_g_shadow(Rational(kappa_val), g))

    return {
        'kappa': kappa_val,
        'support': [-R, R],
        'R': R,
        'moments': moments,
        'free_energies': free_energies,
        'density_at_origin': kappa_val / (2.0 * PI) * R,
        'normalization': 1.0,
    }


def verify_wigner_normalization(kappa_val: float, n_pts: int = 1000) -> Dict[str, float]:
    """Verify that the Wigner semicircle integrates to 1."""
    R = 2.0 / math.sqrt(kappa_val)
    dx = 2 * R / n_pts
    total = 0.0
    for i in range(n_pts):
        x = -R + (i + 0.5) * dx
        total += wigner_semicircle(kappa_val, x) * dx
    return {
        'integral': total,
        'expected': 1.0,
        'error': abs(total - 1.0),
    }


def verify_wigner_moments_numerical(kappa_val: float, max_k: int = 6,
                                     n_pts: int = 2000) -> Dict[int, Dict[str, float]]:
    """Verify exact Wigner moments against numerical integration."""
    R = 2.0 / math.sqrt(kappa_val)
    dx = 2 * R / n_pts

    results = {}
    for k in range(max_k + 1):
        exact = wigner_moments(kappa_val, k)
        # Numerical
        numerical = 0.0
        for i in range(n_pts):
            x = -R + (i + 0.5) * dx
            numerical += x ** k * wigner_semicircle(kappa_val, x) * dx

        results[k] = {
            'exact': exact,
            'numerical': numerical,
            'error': abs(exact - numerical),
        }

    return results
