r"""Shadow coefficients as conformal block integrals: spectral curve periods.

MATHEMATICAL CONTENT:

The closed-form generating function G[F](xi) = kappa*(xi/(2*sin(xi/2)) - 1)
packages all genus-g free energies F_g. Each F_g = kappa * lambda_g^FP is
an integral over M_bar_g of the Faber-Pandharipande lambda class.

Meanwhile, the shadow coefficient S_r is the r-th projection of the MC
element Theta_A.  The shadow metric Q_L(t) controls the tower via

    H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} r * S_r * t^r

so that S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t)).

INVESTIGATION (five questions):

(a) S_r = a_{r-2}/r where a_n is the n-th Taylor coefficient of sqrt(Q_L).
    Is a_n an integral over Conf_n(C)?

    ANSWER: YES, via the Cauchy integral formula.  a_n is exactly the
    contour integral

        a_n = (1/(2*pi*i)) * oint sqrt(Q_L(z)) / z^{n+1} dz

    around z = 0.  This is an integral over a circle in C, hence over a
    1-dimensional configuration space.  More precisely, for the Virasoro
    algebra with Q_L(t) = c^2 + 12ct + alpha(c)*t^2:

        a_n = (1/(2*pi*i)) * oint sqrt(c^2 + 12cz + alpha*z^2) / z^{n+1} dz

    By deformation, this contour integral equals a RESIDUE integral,
    computable by the spectral curve y^2 = Q_L(z).

(b) The convolution recursion a_n = -(1/(2*a_0)) * sum a_j*a_{n-j} looks
    like a SPLITTING FORMULA.  Is it the splitting of Conf_n along a
    boundary divisor?

    ANSWER: YES.  The recursion comes from [t^n](f^2 = Q) where f = sqrt(Q).
    The sum a_j*a_{n-j} is the CAUCHY PRODUCT of {a_n} with itself.  In
    the Cauchy integral picture, this is the CONVOLUTION of the contour
    integral with itself:

        [t^n](f^2) = sum_{j=0}^n a_j * a_{n-j}
                    = (1/(2*pi*i))^2 * oiint f(z1)*f(z2)/(z1^{j+1}*z2^{n-j+1}) dz1 dz2

    This is an integral over Conf_2({z1,z2}) of the PRODUCT f(z1)*f(z2)
    projected to the (j, n-j) diagonal.  The recursion that produces a_n
    from lower a_j's is the RESIDUE of the two-point function on the
    boundary divisor z1 + z2 = z of Conf_2.

(c) sqrt(Q_L) is the PERIOD of the spectral curve y^2 = Q_L.  Are the
    S_r the Fourier coefficients of this period?

    ANSWER: The spectral curve Sigma: y^2 = Q_L(t) is a genus-0 curve
    (since Q_L is quadratic in t).  The period integral is

        Pi(gamma) = oint_gamma y dt = oint_gamma sqrt(Q_L(t)) dt

    around the branch cut connecting the two roots of Q_L.  The Taylor
    coefficients a_n are NOT Fourier coefficients of the period (which is
    a single number for a fixed cycle gamma), but rather the a_n are the
    moments of the spectral density:

        a_n = (1/(2*pi*i)) * oint sqrt(Q_L(z)) z^{-(n+1)} dz

    This is a MOMENT of the spectral measure d*mu = sqrt(Q_L(z)) dz/(2*pi*i*z).

(d) Class G: Q_L = (2*kappa)^2, sqrt(Q_L) = 2*kappa, a_0 = 2*kappa,
    a_n = 0 for n >= 1.  The spectral curve is degenerate (y = const).
    The period is trivial: all moments vanish.

(e) Class M: Q_L irreducible, sqrt(Q_L) genuinely algebraic of degree 2.
    The spectral curve has two branch points.  All moments a_n are nonzero.
    The S_r decay as rho^r * r^{-5/2} (Flajolet-Sedgewick transfer from
    the branch point singularity).

THEOREM (Shadow Period Integral):
    For the Virasoro algebra, define the spectral curve Sigma_c by
    y^2 = c^2 + 12ct + alpha(c)*t^2 where alpha(c) = (180c+872)/(5c+22).
    Then:

    S_r(c) = (1/(2*pi*i*r)) * oint_C y(t) / t^{r-1} dt

    where C is a small positively oriented circle around t = 0.

    Equivalently, using the period integral representation:

    S_r(c) = (1/(r*(r-1))) * d^{r-2}/dt^{r-2} [ sqrt(Q_L(t)) ] |_{t=0} / (r-2)!
           = a_{r-2} / r  (Taylor coefficient formula)

    The integral int_0^1 t^r * sqrt(Q_L(t)) dt is a DIFFERENT object:
    it is the (r+1)-th moment of the spectral density on [0,1], which
    has a closed-form expression via the Euler beta function.

COMPUTATION (moment integrals vs shadow coefficients):

    The integral I_r(c) = int_0^1 t^r * sqrt(Q_L(t)) dt for Q_L = c^2 + 12ct + alpha*t^2
    is computable in closed form for each r via:

        I_r(c) = int_0^1 t^r * sqrt(c^2 + 12ct + alpha*t^2) dt

    This integral is NOT equal to S_r.  The relationship is:

        S_r = (Taylor coefficient of sqrt(Q_L) at t=0) / r

    while I_r is the MOMENT over [0,1]:

        I_r = int_0^1 t^r * sqrt(Q_L(t)) dt = sum_{n=0}^infty a_n * B(r+n+1, 1)
            = sum_{n=0}^infty a_n / (r+n+1)

    where B is the Euler beta function (B(a,b) = Gamma(a)*Gamma(b)/Gamma(a+b))
    and a_n = [t^n] sqrt(Q_L).  So I_r is a TRANSFORM of the a_n sequence,
    not the a_n themselves.

BRIDGE TO WITTEN-KONTSEVICH:
    The genus-g free energy F_g = kappa * lambda_g^FP where

        lambda_g^FP = int_{M_bar_g} lambda_g

    is the integral of the top Chern class of the Hodge bundle.  The
    generating function sum F_g * hbar^{2g} = kappa * (Ahat(i*hbar) - 1)
    packages all genera.  The Bernoulli numbers B_{2g} appear as:

        F_g = kappa * |B_{2g}| / (2g * (2g)!)  (Faber-Pandharipande values)

    These are DIFFERENT objects from S_r: the F_g live on M_bar_g (moduli
    of curves, parametrized by genus), while S_r live on the primary line
    of the deformation complex (parametrized by arity).  The shadow
    obstruction tower and the genus expansion are two DIFFERENT projections
    of the single MC element Theta_A.

    However, there is a STRUCTURAL PARALLEL: the convolution recursion
    for a_n mirrors the clutching/gluing structure on M_bar_g.  Both
    come from the MC equation D*Theta + (1/2)[Theta, Theta] = 0
    projected to different graded components.

References:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    virasoro_shadow_gf.py (closed-form generating function)
    shadow_tower_recursive.py (recursive tower computation)
    shadow_metric_census.py (G/L/C/M classification)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Abs, I, N as Neval, Poly, Rational, Symbol, atan2, bernoulli, binomial,
    cancel, cos, diff, expand, factor, factorial, fraction, gamma, integrate,
    limit, log, numer, denom, oo, pi, series, simplify, sin, solve, sqrt,
    symbols, zoo,
)

c = Symbol('c', positive=True)
t = Symbol('t')


# ============================================================================
# 1. Shadow metric Q_L and spectral curve infrastructure
# ============================================================================

def alpha_virasoro(c_val=None):
    """Quadratic coefficient alpha(c) = (180c + 872) / (5c + 22).

    Equivalently alpha(c) = 36 + 80/(5c+22).
    This controls the Virasoro shadow metric on the primary line.
    """
    if c_val is None:
        c_val = c
    return (180 * c_val + 872) / (5 * c_val + 22)


def Q_L_virasoro(t_val=None, c_val=None):
    """Shadow metric Q_L(t) = c^2 + 12ct + alpha(c)*t^2.

    The spectral curve is Sigma: y^2 = Q_L(t).
    """
    if t_val is None:
        t_val = t
    if c_val is None:
        c_val = c
    a = alpha_virasoro(c_val)
    return c_val**2 + 12 * c_val * t_val + a * t_val**2


def Q_L_general(kappa_val, S3_val, S4_val, t_val=None):
    """General shadow metric Q_L(t) = 4*kappa^2 + 12*kappa*S3*t + (9*S3^2 + 16*kappa*S4)*t^2.

    Parameters:
        kappa_val: S_2 (curvature)
        S3_val: S_3 (cubic shadow)
        S4_val: S_4 (quartic contact invariant)
        t_val: deformation parameter
    """
    if t_val is None:
        t_val = t
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * S3_val
    q2 = 9 * S3_val**2 + 16 * kappa_val * S4_val
    return q0 + q1 * t_val + q2 * t_val**2


def spectral_curve_discriminant(c_val=None):
    """Discriminant of Q_L(t) = c^2 + 12ct + alpha*t^2 as quadratic in t.

    disc = (12c)^2 - 4*alpha*c^2 = c^2*(144 - 4*alpha)
         = c^2*(144 - 4*(180c+872)/(5c+22))
         = c^2*((144*(5c+22) - 4*(180c+872))/(5c+22))
         = c^2*((720c + 3168 - 720c - 3488)/(5c+22))
         = c^2*(-320/(5c+22))
         = -320*c^2/(5c+22)

    This is NEGATIVE for c > 0: the spectral curve has complex conjugate
    branch points, confirming that sqrt(Q_L(t)) is real for all real t.
    """
    if c_val is None:
        c_val = c
    a = alpha_virasoro(c_val)
    return (12 * c_val)**2 - 4 * a * c_val**2


def spectral_curve_branch_points(c_val=None):
    """Branch points of the spectral curve y^2 = Q_L(t).

    t_pm = (-12c +/- sqrt(disc)) / (2*alpha)
         = c * (-6 +/- sqrt(-80/(5c+22))) / alpha

    For c > 0: the branch points are complex conjugates.
    """
    if c_val is None:
        c_val = c
    a = alpha_virasoro(c_val)
    disc = spectral_curve_discriminant(c_val)
    t_plus = (-12 * c_val + sqrt(disc)) / (2 * a)
    t_minus = (-12 * c_val - sqrt(disc)) / (2 * a)
    return t_plus, t_minus


def spectral_curve_branch_point_modulus(c_val_num):
    """Modulus |t_+| of the branch point at a numerical value of c.

    This modulus equals 1/rho where rho is the shadow growth rate.
    """
    a_num = float((180 * c_val_num + 872) / (5 * c_val_num + 22))
    disc_num = float(-320 * c_val_num**2 / (5 * c_val_num + 22))
    sqrt_disc = cmath.sqrt(disc_num)
    t_plus = (-12 * c_val_num + sqrt_disc) / (2 * a_num)
    return abs(t_plus)


# ============================================================================
# 2. Taylor coefficients a_n of sqrt(Q_L) via convolution recursion
# ============================================================================

def sqrt_QL_taylor_coefficients(c_val, max_n, exact=True):
    """Taylor coefficients a_n = [t^n] sqrt(Q_L(t)) for Virasoro.

    Uses the convolution recursion from f^2 = Q_L:
        a_0 = c  (since sqrt(c^2) = c for c > 0)
        a_1 = 12c / (2c) = 6
        a_2 = (alpha - 36) / (2c) = 40 / (c*(5c+22))
        a_n = -(1/(2c)) * sum_{j=1}^{n-1} a_j * a_{n-j}  for n >= 3

    Parameters:
        c_val: central charge (sympy expression or number)
        max_n: compute a_0 through a_{max_n}
        exact: if True, use exact sympy arithmetic

    Returns:
        list [a_0, a_1, ..., a_{max_n}]
    """
    a = alpha_virasoro(c_val)

    q0 = c_val**2
    q1 = 12 * c_val
    q2 = a

    coeffs = [None] * (max_n + 1)

    # a_0 = sqrt(q0) = c
    coeffs[0] = c_val
    if max_n == 0:
        return coeffs

    # a_1 = q1 / (2*a_0) = 12c / (2c) = 6
    coeffs[1] = q1 / (2 * coeffs[0])
    if exact:
        coeffs[1] = simplify(coeffs[1])
    if max_n == 1:
        return coeffs

    # a_2 = (q2 - a_1^2) / (2*a_0) = (alpha - 36) / (2c)
    coeffs[2] = (q2 - coeffs[1]**2) / (2 * coeffs[0])
    if exact:
        coeffs[2] = simplify(coeffs[2])
    if max_n == 2:
        return coeffs

    # a_n for n >= 3: convolution recursion
    for n in range(3, max_n + 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs[n] = -conv_sum / (2 * coeffs[0])
        if exact:
            coeffs[n] = cancel(coeffs[n])

    return coeffs


def shadow_coefficients_from_taylor(c_val, max_r, exact=True):
    """Shadow coefficients S_r = a_{r-2}/r for r = 2, ..., max_r.

    Parameters:
        c_val: central charge
        max_r: maximum arity

    Returns:
        dict {r: S_r} for r = 2 to max_r
    """
    max_n = max_r - 2
    a = sqrt_QL_taylor_coefficients(c_val, max_n, exact)
    S = {}
    for n in range(len(a)):
        r = n + 2
        S[r] = a[n] / r
        if exact:
            S[r] = cancel(S[r])
    return S


# ============================================================================
# 3. Cauchy contour integral representation (exact via residue)
# ============================================================================

def shadow_via_cauchy_integral(r, c_val=None):
    """S_r via the Cauchy integral formula:

        S_r = (1/(2*pi*i*r)) * oint sqrt(Q_L(z)) / z^{r-1} dz
            = a_{r-2} / r

    This is the RESIDUE at z=0 of sqrt(Q_L(z)) / z^{r-1}, divided by r.

    Computation: expand sqrt(Q_L(z)) as a Taylor series in z around 0,
    then the residue picks out the coefficient of z^{r-2}.

    Parameters:
        r: arity (>= 2)
        c_val: central charge (default: symbolic c)
    """
    if c_val is None:
        c_val = c
    # The Cauchy formula gives the Taylor coefficient directly
    # We compute via series expansion
    z = Symbol('z')
    QL = Q_L_virasoro(z, c_val)
    sq = sqrt(QL)
    # Taylor expand to order r-1 (need coefficient of z^{r-2})
    s = series(sq, z, 0, r - 1)
    a_n = s.coeff(z, r - 2)
    return cancel(a_n / r)


# ============================================================================
# 4. Moment integrals: int_0^1 t^r * sqrt(Q_L(t)) dt
# ============================================================================

def moment_integral_exact(r, c_val=None):
    """Compute I_r(c) = int_0^1 t^r * sqrt(Q_L(t)) dt.

    For fixed c, this integral is finite and computable via standard
    techniques (since Q_L(t) > 0 on [0,1] for c > 0).

    Uses sympy integration for exact results.

    Returns a sympy expression in c (or a number if c_val is numeric).
    """
    if c_val is None:
        c_val = c
    QL = Q_L_virasoro(t, c_val)
    integrand = t**r * sqrt(QL)
    return integrate(integrand, (t, 0, 1))


def moment_integral_numerical(r, c_num):
    """Numerical computation of I_r(c) = int_0^1 t^r * sqrt(Q_L(t)) dt.

    Uses Gauss-Legendre quadrature.

    Parameters:
        r: power of t
        c_num: numerical value of central charge (float)

    Returns:
        float approximation of the integral
    """
    a_num = (180 * c_num + 872) / (5 * c_num + 22)

    def integrand(t_val):
        ql = c_num**2 + 12 * c_num * t_val + a_num * t_val**2
        return t_val**r * math.sqrt(max(ql, 0.0))

    # Simpson's rule with 1000 subdivisions
    n_sub = 1000
    h = 1.0 / n_sub
    total = integrand(0.0) + integrand(1.0)
    for i in range(1, n_sub):
        x = i * h
        total += (4 if i % 2 == 1 else 2) * integrand(x)
    return total * h / 3.0


def moment_vs_shadow_comparison(max_r, c_num):
    """Compare moment integrals I_r with shadow coefficients S_r.

    These are DIFFERENT quantities:
        S_r = a_{r-2}/r  (Taylor coefficient of sqrt(Q_L))
        I_r = int_0^1 t^r sqrt(Q_L(t)) dt  (moment integral)

    The relationship is:
        I_r = sum_{n=0}^infty a_n / (r + n + 1)

    where a_n = [t^n] sqrt(Q_L(t)).

    Returns dict of comparisons.
    """
    a_num = (180 * c_num + 872) / (5 * c_num + 22)

    # Compute Taylor coefficients numerically
    a_coeffs = []
    a_coeffs.append(c_num)  # a_0 = c
    a_coeffs.append(6.0)    # a_1 = 6
    a_coeffs.append((a_num - 36) / (2 * c_num))  # a_2

    for n in range(3, max_r + 10):
        conv = sum(a_coeffs[j] * a_coeffs[n - j] for j in range(1, n))
        a_coeffs.append(-conv / (2 * c_num))

    results = {}
    for r in range(0, max_r + 1):
        I_r = moment_integral_numerical(r, c_num)

        # Moment from Taylor coefficients: I_r = sum a_n / (r+n+1)
        I_r_from_taylor = sum(
            a_coeffs[n] / (r + n + 1) for n in range(len(a_coeffs))
        )

        # Shadow coefficient (for r >= 2)
        S_r = a_coeffs[r - 2] / r if r >= 2 else None

        results[r] = {
            'I_r_quadrature': I_r,
            'I_r_from_taylor': I_r_from_taylor,
            'S_r': S_r,
            'I_vs_S_ratio': I_r / S_r if S_r and abs(S_r) > 1e-50 else None,
        }

    return results


# ============================================================================
# 5. Spectral curve period integral
# ============================================================================

def spectral_period_numerical(c_num, n_points=10000):
    """Period integral Pi = oint_gamma sqrt(Q_L(t)) dt around the branch cut.

    For c > 0, the branch points are complex conjugates t_pm.  The
    period is the integral around a cycle enclosing the branch cut.

    By the residue theorem, this equals 2*pi*i * a_{-1} where a_{-1}
    is the coefficient of 1/t in the Laurent expansion of sqrt(Q_L(t)).
    But sqrt(Q_L) is regular at t=0, so the "period at infinity" is
    the residue at t=infinity.

    More precisely: the spectral curve y^2 = Q_L(t) has genus 0.  The
    unique period is:

        Pi = oint_{|t|=R} sqrt(Q_L(t)) dt

    for R > |t_+|.  By the residue at infinity:

        Pi = -2*pi*i * Res_{t=infty} sqrt(Q_L(t))
           = -2*pi*i * (-sqrt(alpha)) (leading coefficient)

    Wait -- more carefully, sqrt(Q_L(t)) ~ sqrt(alpha)*|t| for large |t|,
    so the residue at infinity involves the subleading term.

    For a genus-0 curve y^2 = a*t^2 + b*t + c, the branch cut integral is:

        Pi = oint sqrt(a*z^2 + b*z + c) dz / (2*pi*i)
           = (disc / (8*a)) * [elliptic integral factors]

    But since the curve is rational (genus 0), the period is algebraic.

    COMPUTATION: parametrize the circle |t| = R and integrate numerically.
    """
    a_num = (180 * c_num + 872) / (5 * c_num + 22)

    # Branch point modulus
    disc_num = -320 * c_num**2 / (5 * c_num + 22)
    sqrt_disc = cmath.sqrt(disc_num)
    t_plus = (-12 * c_num + sqrt_disc) / (2 * a_num)
    R = abs(t_plus) * 1.5  # radius outside branch points

    # Integrate on circle |t| = R
    total = 0.0j
    dtheta = 2 * math.pi / n_points
    for k in range(n_points):
        theta = k * dtheta
        z = R * cmath.exp(1j * theta)
        ql = c_num**2 + 12 * c_num * z + a_num * z**2
        sqrt_ql = cmath.sqrt(ql)
        # dt = i*R*e^{i*theta} dtheta
        dz = 1j * R * cmath.exp(1j * theta) * dtheta
        total += sqrt_ql * dz

    return total / (2 * cmath.pi * 1j)


# ============================================================================
# 6. Moment-shadow transform (the precise relationship)
# ============================================================================

def moment_shadow_transform_matrix(max_r, max_n):
    """The transform matrix relating moments I_r to Taylor coefficients a_n.

        I_r = sum_{n=0}^{max_n} a_n / (r + n + 1) = sum_{n} M_{r,n} * a_n

    where M_{r,n} = 1/(r + n + 1).  This is a HILBERT-TYPE matrix.

    The shadow coefficients S_r = a_{r-2}/r are the Taylor coefficients
    (up to the 1/r factor).  So the moment integrals and shadow coefficients
    are related by a Hilbert-type transform, NOT by equality.

    Returns:
        numpy-free matrix as list of lists.
    """
    M = []
    for r in range(max_r + 1):
        row = []
        for n in range(max_n + 1):
            row.append(Rational(1, r + n + 1))
        M.append(row)
    return M


# ============================================================================
# 7. A-hat generating function bridge: F_g from Bernoulli numbers
# ============================================================================

def lambda_g_FP(g):
    """Faber-Pandharipande value: lambda_g^FP = [xi^{2g}] (xi/(2*sin(xi/2)) - 1).

    These are the integrals int_{M_bar_g} lambda_g for g >= 1, extracted
    from the A-hat generating function.

    NOTE: The naive formula |B_{2g}|/(2g*(2g)!) gives the WRONG answer
    for g >= 2.  The correct values come from the Taylor expansion of
    the A-hat genus xi/(2*sin(xi/2)) - 1, which involves ALL Bernoulli
    numbers up to B_{2g}, not just B_{2g} alone.

    Values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
    """
    if g < 1:
        raise ValueError(f"genus g must be >= 1, got {g}")
    xi = Symbol('xi')
    gf = xi / (2 * sin(xi / 2)) - 1
    s = series(gf, xi, 0, 2 * g + 2)
    return s.coeff(xi, 2 * g)


def F_g_scalar(kappa_val, g):
    """Genus-g free energy F_g = kappa * lambda_g^FP.

    Valid on the uniform-weight lane (single-generator or all generators
    having the same conformal weight).  For multi-weight algebras at g >= 2,
    a cross-channel correction delta_F_g^cross must be added.
    """
    return kappa_val * lambda_g_FP(g)


def Ahat_generating_function(xi_val=None):
    """G[F](xi) = kappa * (xi / (2*sin(xi/2)) - 1).

    Packages all F_g via sum_{g>=1} F_g * xi^{2g} = kappa * (xi/(2*sin(xi/2)) - 1).

    NOTE (AP22): The power is xi^{2g}, NOT xi^{2g-2}.  The A-hat function
    minus 1 starts at xi^2, matching g=1 at xi^2.
    """
    if xi_val is None:
        xi_val = Symbol('xi')
    return xi_val / (2 * sin(xi_val / 2)) - 1


# ============================================================================
# 8. Structural parallel: convolution vs clutching
# ============================================================================

@dataclass
class ConvolutionSplittingData:
    """Data recording the structural parallel between the convolution
    recursion for a_n and the clutching/gluing structure on M_bar_g.

    The convolution recursion:
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}

    parallels the boundary structure of M_bar_{g,n}: the codimension-1
    boundary strata of M_bar_g include:
        - Irreducible boundary: a genus-(g-1) curve with one node
        - Reducible boundary: M_bar_{g1,1} x M_bar_{g2,1} with g1+g2=g

    The sum a_j * a_{n-j} corresponds to the reducible boundary
    decomposition, where the "arities" j and n-j split across the node.

    NOTE: This is a STRUCTURAL analogy, not an identification.  The
    convolution recursion lives on the PRIMARY LINE (1D deformation
    parameter space).  The clutching lives on MODULI OF CURVES.
    The two are different projections of the SAME MC equation.
    """
    arity: int = 0
    splitting_pairs: List[Tuple[int, int]] = field(default_factory=list)
    convolution_sum: Any = None
    clutching_analogue: str = ""


def enumerate_splitting_pairs(n):
    """For arity n, list all (j, n-j) splitting pairs with 1 <= j <= n-1.

    These correspond to:
    - In the convolution recursion: the products a_j * a_{n-j}
    - In the clutching structure: the reducible boundary strata
    """
    return [(j, n - j) for j in range(1, n)]


def convolution_as_splitting(c_num, max_n=10):
    """Compute the convolution recursion and record each splitting contribution.

    For each n, computes:
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j}

    and records the individual terms a_j * a_{n-j} as "splitting amplitudes."
    """
    a = [0.0] * (max_n + 1)
    a_num = (180 * c_num + 872) / (5 * c_num + 22)

    a[0] = c_num
    a[1] = 6.0
    a[2] = (a_num - 36) / (2 * c_num)

    results = []
    for n in range(3, max_n + 1):
        pairs = enumerate_splitting_pairs(n)
        amplitudes = {}
        conv_sum = 0.0
        for j, k in pairs:
            amp = a[j] * a[k]
            amplitudes[(j, k)] = amp
            conv_sum += amp
        a[n] = -conv_sum / (2 * a[0])

        results.append(ConvolutionSplittingData(
            arity=n,
            splitting_pairs=pairs,
            convolution_sum=conv_sum,
            clutching_analogue=f"sum of a_j*a_{{n-j}} for j=1..{n-1} = {conv_sum:.6e}",
        ))

    return results, a


# ============================================================================
# 9. Depth classification from spectral curve geometry
# ============================================================================

def depth_from_spectral_curve(kappa_val, S3_val, S4_val):
    """Classify shadow depth from the spectral curve y^2 = Q_L(t).

    - Class G: Q_L = constant (degenerate curve, no branch points) => depth 2
    - Class L: Q_L = perfect square (double branch point) => depth 3
    - Class C: stratum separation => depth 4
    - Class M: Q_L irreducible (two distinct branch points) => depth infinity

    The discriminant Delta = 8*kappa*S4 controls the classification:
        Delta = 0 and S3 = 0 => G
        Delta = 0 and S3 != 0 => L
        Delta != 0 => M (or C via stratum separation)
    """
    Delta = 8 * kappa_val * S4_val
    Delta_simple = simplify(Delta)

    if Delta_simple == 0:
        S3_simple = simplify(S3_val)
        if S3_simple == 0:
            return 'G', 2, "Degenerate spectral curve (y = constant)"
        else:
            return 'L', 3, "Perfect-square spectral curve (double branch point)"
    else:
        return 'M', float('inf'), "Irreducible spectral curve (two distinct branch points)"


# ============================================================================
# 10. Numerical verification suite
# ============================================================================

def verify_cauchy_formula_numerically(r, c_num, n_points=10000):
    """Verify S_r = (1/(2*pi*i*r)) * oint sqrt(Q_L(z)) / z^{r-1} dz numerically.

    Integrates on a small circle |z| = epsilon around z = 0.
    """
    a_num = (180 * c_num + 872) / (5 * c_num + 22)
    epsilon = 0.1  # small radius

    total = 0.0j
    dtheta = 2 * math.pi / n_points
    for k in range(n_points):
        theta = k * dtheta
        z = epsilon * cmath.exp(1j * theta)
        ql = c_num**2 + 12 * c_num * z + a_num * z**2
        sqrt_ql = cmath.sqrt(ql)
        # Integrand: sqrt(Q_L(z)) / z^{r-1}
        integrand_val = sqrt_ql / z**(r - 1)
        # dz = i*epsilon*e^{i*theta} dtheta
        dz = 1j * epsilon * cmath.exp(1j * theta) * dtheta
        total += integrand_val * dz

    # S_r = (1/(2*pi*i*r)) * integral
    return (total / (2 * cmath.pi * 1j * r)).real


def verify_taylor_vs_recursive(c_num, max_r=12):
    """Cross-verify Taylor coefficient method against the Virasoro recursion.

    Two INDEPENDENT computations:
    Path 1: Taylor coefficients a_n of sqrt(Q_L), then S_r = a_{r-2}/r
    Path 2: Direct H-Poisson bracket recursion from virasoro_shadow_gf.py

    These must agree (multi-path verification mandate).
    """
    # Path 1: Taylor coefficients
    S_taylor = {}
    a_num = (180 * c_num + 872) / (5 * c_num + 22)
    a = [0.0] * (max_r + 1)
    a[0] = c_num
    a[1] = 6.0
    a[2] = (a_num - 36) / (2 * c_num)
    for n in range(3, max_r + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * c_num)
    for n in range(len(a)):
        r = n + 2
        if r <= max_r + 2:
            S_taylor[r] = a[n] / r

    # Path 2: Direct recursion (independent implementation)
    S_direct = {}
    S_direct[2] = c_num / 2
    S_direct[3] = 2.0
    S_direct[4] = 10.0 / (c_num * (5 * c_num + 22))

    for r in range(5, max_r + 3):
        total = 0.0
        target = r + 2
        for j in range(3, target):
            k = target - j
            if k < j:
                break
            if k < 3:
                continue
            if j not in S_direct or k not in S_direct:
                continue
            term = 2 * j * k * S_direct[j] * S_direct[k]
            if j == k:
                term /= 2
            total += term
        S_direct[r] = -total / (2 * r * c_num)

    # Compare
    results = {}
    for r in sorted(set(S_taylor.keys()) & set(S_direct.keys())):
        st = S_taylor[r]
        sd = S_direct[r]
        if abs(sd) > 1e-50:
            rel_err = abs(st - sd) / abs(sd)
        else:
            rel_err = abs(st - sd)
        results[r] = {
            'S_taylor': st,
            'S_direct': sd,
            'relative_error': rel_err,
            'agree': rel_err < 1e-10,
        }

    return results


def verify_moment_identity(c_num, max_r=8, max_terms=50):
    """Verify I_r = sum_{n=0}^infty a_n / (r+n+1) numerically.

    The moment integral I_r = int_0^1 t^r sqrt(Q_L(t)) dt has the
    Taylor expansion representation:

        I_r = int_0^1 t^r * sum_n a_n t^n dt = sum_n a_n * int_0^1 t^{r+n} dt
            = sum_n a_n / (r+n+1)

    Verify by comparing quadrature I_r with the truncated Taylor sum.
    """
    a_alpha = (180 * c_num + 872) / (5 * c_num + 22)

    # Taylor coefficients
    a = [0.0] * (max_terms + 1)
    a[0] = c_num
    a[1] = 6.0
    a[2] = (a_alpha - 36) / (2 * c_num)
    for n in range(3, max_terms + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * c_num)

    results = {}
    for r in range(max_r + 1):
        I_quad = moment_integral_numerical(r, c_num)
        I_taylor = sum(a[n] / (r + n + 1) for n in range(max_terms + 1))

        if abs(I_quad) > 1e-50:
            rel_err = abs(I_quad - I_taylor) / abs(I_quad)
        else:
            rel_err = abs(I_quad - I_taylor)

        results[r] = {
            'I_quadrature': I_quad,
            'I_taylor_sum': I_taylor,
            'relative_error': rel_err,
            'agree': rel_err < 1e-4,  # modest threshold due to truncation
        }

    return results


# ============================================================================
# 11. Full landscape: comparison across algebras
# ============================================================================

STANDARD_LANDSCAPE = {
    'Heisenberg_k1': {
        'kappa': 1.0, 'S3': 0.0, 'S4': 0.0,
        'depth': 'G', 'description': 'Heisenberg at k=1',
    },
    'Heisenberg_k2': {
        'kappa': 2.0, 'S3': 0.0, 'S4': 0.0,
        'depth': 'G', 'description': 'Heisenberg at k=2',
    },
    'affine_sl2_k1': {
        'kappa': 3 * (1 + 2) / 4,  # = 9/4 = 2.25
        'S3': 2.0, 'S4': 0.0,
        'depth': 'L', 'description': 'affine sl_2 at k=1',
    },
    'Virasoro_c1': {
        'kappa': 0.5, 'S3': 2.0,
        'S4': 10.0 / (1.0 * (5 * 1.0 + 22)),
        'depth': 'M', 'description': 'Virasoro at c=1',
    },
    'Virasoro_c13': {
        'kappa': 6.5, 'S3': 2.0,
        'S4': 10.0 / (13.0 * (5 * 13.0 + 22)),
        'depth': 'M', 'description': 'Virasoro at c=13 (self-dual)',
    },
    'Virasoro_c26': {
        'kappa': 13.0, 'S3': 2.0,
        'S4': 10.0 / (26.0 * (5 * 26.0 + 22)),
        'depth': 'M', 'description': 'Virasoro at c=26 (critical)',
    },
}


def landscape_spectral_analysis():
    """Analyze spectral curve properties across the standard landscape.

    For each algebra:
    1. Compute spectral curve y^2 = Q_L(t)
    2. Find branch points
    3. Classify depth
    4. Compute first few shadow coefficients
    5. Compare Cauchy integral with recursion
    """
    results = {}
    for name, data in STANDARD_LANDSCAPE.items():
        kap = data['kappa']
        s3 = data['S3']
        s4 = data['S4']

        # Shadow metric
        q0 = 4 * kap**2
        q1 = 12 * kap * s3
        q2 = 9 * s3**2 + 16 * kap * s4
        Delta = 8 * kap * s4

        # Branch points (if Delta != 0)
        disc = q1**2 - 4 * q0 * q2
        if abs(disc) > 1e-20:
            sqrt_disc = cmath.sqrt(disc)
            t_p = (-q1 + sqrt_disc) / (2 * q2) if abs(q2) > 1e-20 else None
            t_m = (-q1 - sqrt_disc) / (2 * q2) if abs(q2) > 1e-20 else None
            rho = 1.0 / abs(t_p) if t_p else None
        else:
            t_p = t_m = None
            rho = 0.0

        # Shadow coefficients via Taylor
        a_coeffs = [0.0] * 12
        a_coeffs[0] = 2 * kap  # sqrt(4*kap^2) = 2*kap for kap > 0
        if abs(a_coeffs[0]) > 1e-50:
            a_coeffs[1] = q1 / (2 * a_coeffs[0])
            a_coeffs[2] = (q2 - a_coeffs[1]**2) / (2 * a_coeffs[0])
            for n in range(3, 12):
                conv = sum(a_coeffs[j] * a_coeffs[n - j] for j in range(1, n))
                a_coeffs[n] = -conv / (2 * a_coeffs[0])

        S_vals = {n + 2: a_coeffs[n] / (n + 2) for n in range(10)}

        results[name] = {
            'Q_L': (q0, q1, q2),
            'Delta': Delta,
            'disc': disc,
            'branch_points': (t_p, t_m),
            'growth_rate': rho,
            'depth': data['depth'],
            'S_coefficients': S_vals,
            'description': data['description'],
        }

    return results


# ============================================================================
# 12. The fundamental distinction: arity vs genus
# ============================================================================

def arity_genus_comparison(c_num, max_g=5, max_r=10):
    """Tabulate both F_g (genus expansion) and S_r (shadow obstruction tower)
    for the Virasoro algebra at central charge c_num.

    F_g = (c/2) * lambda_g^FP  (genus expansion, on M_bar_g)
    S_r = a_{r-2}/r            (shadow tower, on primary line)

    These are DIFFERENT projections of Theta_A:
    - F_g is the genus-g, arity-0 projection
    - S_r is the genus-0, arity-r projection

    Both carry information about the single MC element Theta_A.
    """
    kap = c_num / 2

    # Genus expansion: F_g = kappa * lambda_g^FP from A-hat generating function
    F = {}
    for g in range(1, max_g + 1):
        F[g] = float(kap * Neval(lambda_g_FP(g)))

    # Shadow tower: S_r via Taylor of sqrt(Q_L)
    a_alpha = (180 * c_num + 872) / (5 * c_num + 22)
    a = [0.0] * (max_r + 1)
    a[0] = c_num
    a[1] = 6.0
    a[2] = (a_alpha - 36) / (2 * c_num)
    for n in range(3, max_r + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * c_num)
    S = {n + 2: a[n] / (n + 2) for n in range(max_r + 1)}

    return {
        'c': c_num,
        'kappa': kap,
        'F_g': F,
        'S_r': S,
        'note': (
            "F_g and S_r are DIFFERENT projections of Theta_A. "
            "F_g = genus-g, arity-0 (integral over M_bar_g). "
            "S_r = genus-0, arity-r (Taylor coefficient on primary line). "
            "Both derived from D*Theta + (1/2)[Theta,Theta] = 0."
        ),
    }
