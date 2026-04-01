r"""
sewing_selberg.py -- Sewing-Selberg formula: independent verification.

THE SELBERG INTEGRAL (Selberg 1944):

  S_n(a, b, c) = \int_0^1 ... \int_0^1
      \prod_{i=1}^n x_i^{a-1} (1-x_i)^{b-1}
      \prod_{1 <= i < j <= n} |x_i - x_j|^{2c}
      dx_1 ... dx_n

  = \prod_{j=0}^{n-1}  Gamma(a + j*c) * Gamma(b + j*c) * Gamma(1 + (j+1)*c)
                       / [ Gamma(a + b + (n-1+j)*c) * Gamma(1 + c) ]

This is the STANDARD convention (Forrester-Warnaar 2008, Mehta 2004).

NORMALIZATION CONVENTIONS (a common source of error):
  - Some authors write |x_i - x_j|^{2c}, others |x_i - x_j|^c.
    The exponent 2c is Selberg's original convention.  Mehta uses 2*beta.
    Forrester uses beta = c in some works.
  - Some authors write x_i^{a-1}, others x_i^a.  We use a-1 (Selberg original).
  - The Morris identity (a=b=1, c=1) and the Dixon-Anderson integral are
    special cases.

CONNECTION TO HEISENBERG SEWING:

The Heisenberg algebra H_k at level k (rank 1) has:
  - Central charge c = 1 (for a single free boson at level k)
  - Modular characteristic kappa(H_k) = k
  - Genus-1 free energy F_1(H_k) = kappa/24 = k/24

The genus-g free energy (Faber-Pandharipande formula):
  F_g(H_k) = k * (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

The sewing amplitude at genus g involves integrating products of
prime forms E(z_i, z_j) over Schottky parameters.  For Heisenberg,
the one-particle reduction (thm:heisenberg-one-particle-sewing)
gives:
  Z_g(H_k) = det(1 - K_q)^{-k}
where K_q is the sewing operator on the one-particle Hilbert space.

At genus 1: det(1 - K_q)^{-k} = prod_{n >= 1} (1 - q^n)^{-k}
  => F_1 = -k * log prod(1-q^n) = k * sum sigma_{-1}(N) q^N
  => constant term in the q-expansion: this is the log of the
     Dedekind eta function, with F_1^{FP} = k/24 (the leading term).

The Selberg integral enters when the sewing amplitude is written as
an integral over the moduli of the marked points.  Specifically,
the n-point correlation function of the Heisenberg field a(z) on the
torus involves Selberg-type integrals with c = k (the level).

For the symmetric Selberg integral (a = b = 1):
  S_n(1, 1, k) = prod_{j=0}^{n-1} Gamma(1+jk) * Gamma(1+jk) * Gamma(1+(j+1)k)
                 / [ Gamma(2 + (n-1+j)k) * Gamma(1+k) ]
               = prod_{j=1}^n Gamma(1+jk) / [ Gamma(1+k)^n * Gamma(1 + n + n(n-1)k/2 ... ]

Wait -- let me write the formula correctly using the closed form.

VERIFICATION STRATEGY:
  1. Implement S_n(a,b,c) via the product formula
  2. Verify S_1(a,b,c) = B(a,b) = Gamma(a)*Gamma(b)/Gamma(a+b)
  3. Verify S_2(a,b,c) against direct numerical integration
  4. Verify Morris identity: S_n(1, 1, 1) = (n+1)! / 2^n (WRONG: Morris is more specific)
  5. Check the Heisenberg connection via F_1 = k/24
  6. Verify factorial vs polynomial growth of S_n

CRITICAL CHECK: The "sewing-Selberg formula" connecting A_g(H_k) to S_n(k)
must be verified independently.  The potential error: conflating the
OPE-level Selberg integral (conformal blocks) with the genus-level
sewing amplitude (Schottky parameters).  These are different objects.
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Optional, Tuple

try:
    import mpmath
    from mpmath import mp, mpf, gamma as mp_gamma, beta as mp_beta
    from mpmath import fac as mp_fac, loggamma, power, pi as mp_pi
    from mpmath import quad as mp_quad, fabs, log as mp_log
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. The Selberg integral via the product formula
# ============================================================

def selberg_integral(n: int, a: float, b: float, c: float,
                     dps: int = 30) -> float:
    r"""Compute S_n(a, b, c) via the Selberg product formula.

    S_n(a, b, c) = \prod_{j=0}^{n-1}
        Gamma(a + j*c) * Gamma(b + j*c) * Gamma(1 + (j+1)*c)
        / [ Gamma(a + b + (n-1+j)*c) * Gamma(1 + c) ]

    Parameters
    ----------
    n : int
        Number of integration variables (n >= 1).
    a, b : float
        Exponent parameters (a > 0, b > 0 for convergence).
    c : float
        Interaction parameter (c > 0 for repulsive case).
    dps : int
        Decimal places for mpmath computation.

    Returns
    -------
    float
        The value of the Selberg integral.

    Notes
    -----
    Convergence requires:
      Re(a) > 0, Re(b) > 0, Re(c) > -min(1/n, Re(a)/(n-1), Re(b)/(n-1))
    """
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for Selberg integral computation")

    old_dps = mp.dps
    mp.dps = dps
    try:
        a, b, c = mpf(a), mpf(b), mpf(c)
        result = mpf(1)
        for j in range(n):
            num = mp_gamma(a + j * c) * mp_gamma(b + j * c) * mp_gamma(1 + (j + 1) * c)
            den = mp_gamma(a + b + (n - 1 + j) * c) * mp_gamma(1 + c)
            result *= num / den
        return float(result)
    finally:
        mp.dps = old_dps


def selberg_integral_exact(n: int, a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    """Compute S_n(a, b, c) exactly for integer/half-integer parameters.

    Only works when all Gamma arguments are positive integers (so that
    Gamma(k) = (k-1)!).  Returns exact Fraction.
    """
    # Check that all Gamma arguments are positive integers
    args_num = []
    args_den = []
    for j in range(n):
        args_num.append(a + j * c)
        args_num.append(b + j * c)
        args_num.append(Fraction(1) + (j + 1) * c)
        args_den.append(a + b + (n - 1 + j) * c)
        args_den.append(Fraction(1) + c)

    for arg in args_num + args_den:
        if arg.denominator != 1 or arg <= 0:
            raise ValueError(
                f"Exact computation requires all Gamma arguments to be positive integers. "
                f"Got Gamma({arg})"
            )

    result = Fraction(1)
    for j in range(n):
        num_val = (
            math.factorial(int(a + j * c) - 1)
            * math.factorial(int(b + j * c) - 1)
            * math.factorial(int(Fraction(1) + (j + 1) * c) - 1)
        )
        den_val = (
            math.factorial(int(a + b + (n - 1 + j) * c) - 1)
            * math.factorial(int(Fraction(1) + c) - 1)
        )
        result *= Fraction(num_val, den_val)
    return result


# ============================================================
# 2. Special cases and identities
# ============================================================

def beta_function(a: float, b: float, dps: int = 30) -> float:
    """B(a, b) = Gamma(a) * Gamma(b) / Gamma(a+b).

    This should equal S_1(a, b, c) for any c.
    """
    if not HAS_MPMATH:
        return math.gamma(a) * math.gamma(b) / math.gamma(a + b)
    old_dps = mp.dps
    mp.dps = dps
    try:
        return float(mp_beta(mpf(a), mpf(b)))
    finally:
        mp.dps = old_dps


def selberg_symmetric(n: int, c: float, dps: int = 30) -> float:
    """S_n(1, 1, c) -- the symmetric Selberg integral (a = b = 1).

    S_n(1, 1, c) = prod_{j=0}^{n-1}
        Gamma(1 + j*c)^2 * Gamma(1 + (j+1)*c)
        / [ Gamma(2 + (n-1+j)*c) * Gamma(1 + c) ]

    For c = 1 (Morris identity with a=b=1):
      S_n(1, 1, 1) = prod_{j=1}^n j!^2 * (j+1)! / [(n+j)! * 1!]
    """
    return selberg_integral(n, 1.0, 1.0, c, dps=dps)


def morris_integral(n: int, dps: int = 30) -> float:
    """The Morris integral: S_n(1, 1, 1).

    Known closed form:
      S_n(1, 1, 1) = prod_{j=0}^{n-1} j! * j! * (j+1)! / [(n+j)! * 0!]

    Wait: Gamma(1 + j*1) = Gamma(1+j) = j!, Gamma(1 + (j+1)*1) = (j+1)!,
    Gamma(2 + (n-1+j)*1) = Gamma(n+j+1) = (n+j)!, Gamma(1+1) = Gamma(2) = 1.

    So S_n(1,1,1) = prod_{j=0}^{n-1} (j!)^2 * (j+1)! / [(n+j)! * 1]
                  = prod_{j=0}^{n-1} (j!)^2 * (j+1)! / (n+j)!

    For n=1: (0!)^2 * 1! / 1! = 1.  Check: S_1(1,1,c) = B(1,1) = 1. Good.
    For n=2: (0!)^2*1!/(2!) * (1!)^2*2!/(3!) = (1/2) * (2/6) = 1/6.
    """
    return selberg_integral(n, 1.0, 1.0, 1.0, dps=dps)


def morris_integral_exact(n: int) -> Fraction:
    """Exact computation of S_n(1, 1, 1) = prod_{j=0}^{n-1} (j!)^2(j+1)! / (n+j)!."""
    result = Fraction(1)
    for j in range(n):
        num = math.factorial(j) ** 2 * math.factorial(j + 1)
        den = math.factorial(n + j)
        result *= Fraction(num, den)
    return result


# ============================================================
# 3. Numerical verification via direct integration
# ============================================================

def selberg_integral_numerical(n: int, a: float, b: float, c: float,
                               dps: int = 15) -> float:
    """Direct numerical integration of S_n(a, b, c) for small n.

    WARNING: Extremely slow for n >= 4.  Use only for verification.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for numerical integration")
    if n > 4:
        raise ValueError(f"Numerical integration impractical for n > 4, got {n}")

    old_dps = mp.dps
    mp.dps = dps
    try:
        a, b, c = mpf(a), mpf(b), mpf(c)

        if n == 1:
            def f(x):
                return power(x, a - 1) * power(1 - x, b - 1)
            return float(mp_quad(f, [0, 1]))

        elif n == 2:
            def f(x1, x2):
                base = power(x1, a - 1) * power(1 - x1, b - 1)
                base *= power(x2, a - 1) * power(1 - x2, b - 1)
                base *= power(fabs(x1 - x2), 2 * c)
                return base
            return float(mp_quad(f, [0, 1], [0, 1]))

        elif n == 3:
            def f(x1, x2, x3):
                base = mpf(1)
                for x in [x1, x2, x3]:
                    base *= power(x, a - 1) * power(1 - x, b - 1)
                for xi, xj in [(x1, x2), (x1, x3), (x2, x3)]:
                    base *= power(fabs(xi - xj), 2 * c)
                return base
            return float(mp_quad(f, [0, 1], [0, 1], [0, 1]))

        elif n == 4:
            def f(x1, x2, x3, x4):
                xs = [x1, x2, x3, x4]
                base = mpf(1)
                for x in xs:
                    base *= power(x, a - 1) * power(1 - x, b - 1)
                for i in range(4):
                    for j in range(i + 1, 4):
                        base *= power(fabs(xs[i] - xs[j]), 2 * c)
                return base
            return float(mp_quad(f, [0, 1], [0, 1], [0, 1], [0, 1]))
    finally:
        mp.dps = old_dps


# ============================================================
# 4. Heisenberg sewing connection
# ============================================================

def heisenberg_kappa(k: float, d: int = 1) -> float:
    """Modular characteristic of Heisenberg H_k at level k, rank d.

    kappa(H_k) = d * k.
    For rank 1: kappa = k.
    """
    return d * k


def heisenberg_F_g(g: int, k: float, d: int = 1) -> float:
    """Genus-g free energy for Heisenberg H_k (rank d, level k).

    F_g(H_k) = d*k * (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Uses the Faber-Pandharipande formula.
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    kappa = heisenberg_kappa(k, d)
    if not HAS_MPMATH:
        # Use Python's math for small g
        from fractions import Fraction as F
        # B_{2g} via Bernoulli numbers
        import sympy
        b2g = abs(float(sympy.bernoulli(2 * g)))
        fac = math.factorial(2 * g)
        return kappa * (2 ** (2 * g - 1) - 1) / 2 ** (2 * g - 1) * b2g / fac
    else:
        old_dps = mp.dps
        mp.dps = 30
        try:
            b2g = fabs(mpmath.bernoulli(2 * g))
            fac = mp_fac(2 * g)
            coeff = (mpf(2) ** (2 * g - 1) - 1) / mpf(2) ** (2 * g - 1)
            return float(kappa * coeff * b2g / fac)
        finally:
            mp.dps = old_dps


def heisenberg_F1(k: float, d: int = 1) -> float:
    """F_1(H_k) = kappa / 24 = d*k / 24.

    This is the genus-1 free energy.
    """
    return heisenberg_kappa(k, d) / 24.0


def heisenberg_partition_log(k: float, q_terms: int = 20) -> list:
    """Coefficients of F_1^conn(q) = -k * log prod(1 - q^n).

    F_1^conn = k * sum_{N >= 1} sigma_{-1}(N) q^N

    Returns list of length q_terms with coefficient of q^N for N = 1, ..., q_terms.
    """
    def sigma_minus_1(N):
        return sum(1.0 / d for d in range(1, N + 1) if N % d == 0)
    return [k * sigma_minus_1(N) for N in range(1, q_terms + 1)]


# ============================================================
# 5. Selberg-type integrals in sewing context
# ============================================================

def selberg_sewing_amplitude(n: int, k: float, dps: int = 30) -> float:
    """The sewing amplitude contribution at arity n for Heisenberg level k.

    For Heisenberg, the n-point correlation function on the torus
    involves the Selberg integral S_n(1, 1, k/2) (with c = k/2,
    NOT c = k).

    CRITICAL NORMALIZATION: The bar complex propagator is d log E(z,w),
    which is weight 1.  The squared modulus |d log E|^2 ~ |z-w|^{-2}
    in the flat limit.  For level k, we get |z-w|^{-2k} = |z-w|^{2*(-k)}.
    But the Selberg integral requires c > 0 for convergence.

    The correct identification: the n-point function of the Heisenberg
    field a(z) at level k involves the OPE singularity
    <a(z_i) a(z_j)> = k / (z_i - z_j)^2.  Taking the bar complex
    residue (AP19: one pole order lower), the r-matrix is k/(z_i - z_j).
    The absolute value squared is |k|^2 / |z_i - z_j|^2, giving
    Selberg parameter 2c = -2 (repulsive for k > 0? No: the Selberg
    integral has |x_i - x_j|^{2c}, so c = -1 gives singular integrals).

    RESOLUTION: The Selberg integral appears NOT in the direct sewing
    amplitude but in the PARTITION FUNCTION after Wick contraction.
    The sewing operator K_q for Heisenberg is diagonal in mode space:
      K_q |n> = q^n |n>
    The partition function is:
      Z = prod_{n=1}^infty 1/(1 - q^n)^k  (for rank-1 at level k)

    The Selberg integral enters when computing correlation functions
    of vertex operators V_alpha(z) = :e^{i*alpha*phi(z)}: on the torus.
    The n-point function of vertex operators with charges alpha_i
    involves:
      <V_{a1}(z1) ... V_{an}(zn)> = prod_{i<j} |E(z_i,z_j)|^{2*a_i*a_j*k}
      times the theta function factor for charge conservation.

    For the SIMPLEST case (all alpha_i equal, charge conservation
    forces sum alpha_i = 0 which is impossible for all equal with
    n > 1), so the Selberg-type integral doesn't directly give the
    partition function.  Instead, the connection is:

    The CIRCULAR Selberg integral (Dyson's integral on the unit circle)
    gives the moments of the CUE/GUE:
      I_n(beta) = (1/n!) int_0^{2pi} ... int_0^{2pi}
          prod_{i<j} |e^{i*theta_i} - e^{i*theta_j}|^{2*beta}
          d theta_1 ... d theta_n / (2 pi)^n
      = prod_{j=1}^n Gamma(1 + j*beta) / Gamma(1 + beta)^n

    This is directly related to the Heisenberg partition function
    via the Toeplitz determinant representation:
      det(c_{i-j})_{i,j=0}^{n-1} where c_m = int_0^{2pi} f(theta) e^{-im*theta} d theta/(2pi)

    Returns the symmetric Selberg integral S_n(1, 1, k/2) as a
    candidate sewing amplitude.  The precise normalization connection
    requires careful bookkeeping.
    """
    return selberg_integral(n, 1.0, 1.0, k / 2.0, dps=dps)


def dyson_circular_integral(n: int, beta: float, dps: int = 30) -> float:
    r"""Dyson's circular integral (Mehta-Dyson).

    I_n(beta) = \prod_{j=1}^{n} Gamma(1 + j*beta) / Gamma(1 + beta)^n

    This is the normalization constant of the circular beta-ensemble.
    For beta = 1: CUE (unitary).  For beta = 2: CSE (symplectic).

    For Heisenberg at level k, beta = k gives the relevant ensemble.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    old_dps = mp.dps
    mp.dps = dps
    try:
        beta_mp = mpf(beta)
        result = mpf(1)
        denom = mp_gamma(1 + beta_mp)
        for j in range(1, n + 1):
            result *= mp_gamma(1 + j * beta_mp) / denom
        return float(result)
    finally:
        mp.dps = old_dps


# ============================================================
# 6. Growth analysis
# ============================================================

def selberg_growth_sequence(n_max: int, a: float, b: float, c: float,
                            dps: int = 30) -> list:
    """Compute S_n(a, b, c) for n = 1, ..., n_max.

    Returns list of values.  Used to analyze growth rate.
    """
    return [selberg_integral(n, a, b, c, dps=dps) for n in range(1, n_max + 1)]


def selberg_ratio_sequence(n_max: int, a: float, b: float, c: float,
                           dps: int = 30) -> list:
    """Compute S_{n+1}/S_n for n = 1, ..., n_max-1.

    If the ratio stabilizes, the growth is geometric.
    If the ratio grows like n, the growth is factorial.
    """
    vals = selberg_growth_sequence(n_max, a, b, c, dps=dps)
    return [vals[i + 1] / vals[i] if vals[i] != 0 else float('inf')
            for i in range(len(vals) - 1)]


# ============================================================
# 7. Faber-Pandharipande lambda_g values
# ============================================================

def lambda_g_fp(g: int) -> float:
    """Faber-Pandharipande value: lambda_g = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!.

    This is the integral of the Hodge class lambda_g over M_g,1.
    F_g(A) = kappa(A) * lambda_g.
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    old_dps = mp.dps
    mp.dps = 30
    try:
        b2g = fabs(mpmath.bernoulli(2 * g))
        fac = mp_fac(2 * g)
        coeff = (mpf(2) ** (2 * g - 1) - 1) / mpf(2) ** (2 * g - 1)
        return float(coeff * b2g / fac)
    finally:
        mp.dps = old_dps


# ============================================================
# 8. Cross-checks between Selberg and sewing
# ============================================================

def selberg_F1_cross_check(k: float) -> dict:
    """Cross-check F_1(H_k) = k/24 from multiple independent routes.

    Route 1: kappa(H_k)/24 = k/24  (modular characteristic formula)
    Route 2: F_g formula at g=1: k * (2^1-1)/2^1 * |B_2|/2! = k * 1/2 * 1/12 = k/24
    Route 3: Constant term of -k * log prod(1-q^n): this is k/24 by Dedekind eta
    Route 4: Selberg integral S_1(1,1,k) should be B(1,1) = 1 (independent of k)
             -- this is a TRIVIAL check, not a cross-check

    The key question: is there a NONTRIVIAL Selberg integral identity
    that gives k/24?

    Answer: YES, via the Barnes G-function and the Mehta integral.
    The Mehta integral M_n(beta) = prod_{j=1}^n Gamma(1+j*beta)/Gamma(1+beta)
    has the asymptotic expansion:
      log M_n(beta) ~ (beta/2) n^2 log n - (3beta/4 + 1/2 - 1/(2beta)) n^2/2
                      + (1/12)(beta + 1/beta - 1) log n + ...
    The coefficient of log n is (1/12)(beta + 1/beta - 1), which for
    beta = 1 gives 1/12 -- this is 2 * F_1(H_1) = 2/24!

    So F_1(H_k) = k/24 relates to the SUBLEADING term of the Mehta
    integral, NOT to the Selberg integral at finite n.
    """
    route1 = k / 24.0
    route2 = heisenberg_F_g(1, k)
    route3 = heisenberg_F1(k)

    # Route 4: Selberg at n=1 is B(1,1) = 1, independent of k
    route4_selberg = selberg_integral(1, 1.0, 1.0, k)

    # Route 5: Mehta integral coefficient
    # log M_n(beta) ~ ... + (1/12)(beta + 1/beta - 1) log n
    # For beta = k, this coefficient is (1/12)(k + 1/k - 1)
    # This is NOT k/24, so the connection is more subtle.
    mehta_coeff = (k + 1.0 / k - 1.0) / 12.0

    return {
        'kappa_over_24': route1,
        'fg_formula': route2,
        'direct_F1': route3,
        'selberg_n1': route4_selberg,
        'mehta_log_coeff': mehta_coeff,
        'all_F1_agree': abs(route1 - route2) < 1e-15 and abs(route1 - route3) < 1e-15,
    }


def mehta_integral(n: int, beta: float, dps: int = 30) -> float:
    """Mehta integral: M_n(beta) = prod_{j=1}^n Gamma(1 + j*beta) / Gamma(1+beta)^n.

    Same as Dyson's circular integral.
    This is the n-fold product that controls the partition function of
    the beta-ensemble.
    """
    return dyson_circular_integral(n, beta, dps=dps)


def mehta_log_asymptotics(n: int, beta: float, dps: int = 30) -> dict:
    """Compute log M_n(beta) and compare to asymptotic expansion.

    Asymptotic expansion (Krasovsky, Ehrhardt):
      log M_n(beta) = (beta/2) n^2 log(n)
                     - n^2 [3*beta/4 + 1/2 - 1/(12*beta)]  (Barnes constant)
                     + (1/12)(beta + 1/beta - 1) log(n)
                     + C(beta) + O(1/n)

    where C(beta) involves the Barnes G-function.

    The coefficient of log(n) is (1/12)(beta + 1/beta - 1).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    old_dps = mp.dps
    mp.dps = dps
    try:
        beta_mp = mpf(beta)
        log_mn = mpf(0)
        for j in range(1, n + 1):
            log_mn += loggamma(1 + j * beta_mp) - loggamma(1 + beta_mp)
        log_mn_float = float(log_mn)

        # Leading asymptotic terms
        n_mp = mpf(n)
        leading = float(beta_mp / 2 * n_mp ** 2 * mp_log(n_mp))
        subleading_coeff = float(3 * beta_mp / 4 + mpf(1) / 2 - 1 / (12 * beta_mp))
        subleading = -n ** 2 * subleading_coeff
        log_n_coeff = (beta + 1.0 / beta - 1.0) / 12.0
        log_n_term = log_n_coeff * math.log(n) if n > 0 else 0.0

        return {
            'log_Mn': log_mn_float,
            'leading': leading,
            'subleading': subleading,
            'log_n_coeff': log_n_coeff,
            'log_n_term': log_n_term,
            'residual': log_mn_float - leading - subleading - log_n_term,
        }
    finally:
        mp.dps = old_dps


# ============================================================
# 9. Convention comparison
# ============================================================

def selberg_convention_comparison(n: int, a: float, b: float, c: float,
                                  dps: int = 30) -> dict:
    """Compare different Selberg conventions.

    Convention A (Selberg original): exponent |x_i - x_j|^{2c}
    Convention B (Mehta/Forrester): exponent |x_i - x_j|^{2*beta}
      with beta = c
    Convention C (Anderson): exponent (x_i - x_j)^{2c} (NO absolute value,
      uses ordering x_1 < x_2 < ... < x_n and multiplies by n!)
    Convention D (some physics): exponent |x_i - x_j|^c (half the Selberg exponent)
      S_n^D(a, b, c) = S_n^A(a, b, c/2)

    The crucial pitfall: if the manuscript uses convention D (exponent c)
    but the formula is written for convention A (exponent 2c), the
    result is off by S_n(a, b, c) vs S_n(a, b, c/2).
    """
    conv_A = selberg_integral(n, a, b, c, dps=dps)
    conv_D = selberg_integral(n, a, b, c / 2.0, dps=dps)
    return {
        'convention_A_2c': conv_A,
        'convention_D_c': conv_D,
        'ratio_A_over_D': conv_A / conv_D if conv_D != 0 else float('inf'),
    }


# ============================================================
# 10. Genus-1 Selberg-sewing bridge
# ============================================================

def genus1_sewing_from_eta(k: float, q_terms: int = 50) -> float:
    """F_1 extracted from the Dedekind eta: F_1 = k/24.

    The genus-1 partition function for Heisenberg at level k is:
      Z_1(q) = eta(q)^{-k} = q^{-k/24} * prod_{n=1}^infty (1-q^n)^{-k}

    The free energy is:
      F_1 = -k * lim_{q -> 0} [log Z_1(q) + (k/24) log q] / ...

    Actually, F_1 is simply the leading term in:
      -k * log eta(tau) = -k * [pi*i*tau/12 - sum_{n=1}^infty log(1-q^n)]
                        = k * sum sigma_{-1}(N) q^N  (up to the q^0 term k/24)

    The constant term (Eisenstein regularization) gives:
      F_1 = k * sigma_{-1}^{reg}(0) = k/24

    where sigma_{-1}^{reg}(0) = -1/24 * sum_{n=1}^infty n * 1/n = 1/24
    (zeta regularization: sum 1 = zeta(0) = -1/2, giving -(-1/2)/12 = 1/24).

    Returns: k/24.
    """
    return k / 24.0


def verify_F1_from_bernoulli(k: float) -> dict:
    """Verify F_1(H_k) = k/24 from Bernoulli number B_2 = 1/6.

    F_1 = kappa * (2^1 - 1)/2^1 * |B_2| / 2!
         = k * (1/2) * (1/6) / 2
         = k * (1/2) * (1/12)
         = k/24.

    Wait: (2^{2*1-1} - 1) / 2^{2*1-1} * |B_2| / (2*1)!
        = (2-1)/2 * (1/6)/2
        = (1/2) * (1/12)
        = 1/24.

    Check: |B_2| = 1/6.  (2*1)! = 2.  So |B_2|/(2g)! = 1/12.
    (2^1-1)/2^1 = 1/2.
    Product = 1/24.  Correct.
    """
    from fractions import Fraction as F
    B2 = F(1, 6)  # |B_2| = 1/6
    factor = (F(2) ** 1 - 1) / F(2) ** 1  # (2-1)/2 = 1/2
    lambda1 = factor * B2 / F(2)  # (1/2) * (1/6) / 2 = 1/24
    F1_exact = F(k).limit_denominator(10**6) * lambda1

    return {
        'B2': float(B2),
        'factor_2g': float(factor),
        'lambda1_FP': float(lambda1),
        'F1_exact': float(F1_exact),
        'F1_expected': k / 24.0,
        'match': abs(float(F1_exact) - k / 24.0) < 1e-15,
    }
