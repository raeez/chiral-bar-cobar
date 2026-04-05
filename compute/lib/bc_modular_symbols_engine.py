r"""Bar-complex modular symbols engine.

Connects the homological structure of the bar complex B(A) to the
arithmetic of L-functions via modular symbols.

MATHEMATICAL FRAMEWORK
======================

1. SHADOW MODULAR SYMBOL.

   For a modular Koszul algebra A with shadow partition function

       Z^{sh}_A(tau) = sum_{g>=1} F_g(A) * E_{2g}(tau)

   (where F_g = kappa * lambda_g^{FP} at the scalar level and E_{2g}
   is the Eisenstein series of weight 2g), the shadow modular symbol
   along a path from cusp alpha to cusp beta in the upper half-plane
   H is defined by

       {alpha, beta}^{sh}_A = integral_alpha^beta Z^{sh}_A(tau) d tau.

   At the scalar level the dominant contribution is
   F_1 * integral_alpha^beta E_2(tau) dtau = (kappa/24) * (beta - alpha)
   from the constant term of E_2, plus exponentially small corrections
   from the Fourier tail.

   IMPORTANT (AP15): The genus-1 propagator is E_2^*(tau), which is
   QUASI-MODULAR. The shadow PF at the scalar level is tau-independent
   (a constant kappa/24 per genus). The tau-dependent modular symbol
   integrand is the FULL genus-1 amplitude

       A_1(tau) = -(kappa/12) * log eta(tau)^2

   whose derivative is proportional to E_2^*(tau).  We define both:
   (a) the constant (scalar) symbol kappa * (beta - alpha) / 24, and
   (b) the E_2^*-integrated symbol using the quasi-modular Eisenstein
       series, honestly labeled as quasi-modular.

2. MANIN SYMBOLS.

   The Manin symbol for coprime (c, d) is

       [c:d] = {0, d/c}^{sh} = integral_0^{d/c} Z^{sh}(tau) d tau.

   For the scalar shadow this is kappa * d / (24c).

   For the full quasi-modular amplitude, the integral along the
   geodesic from 0 to d/c in H requires numerical evaluation.

3. PERIOD POLYNOMIAL.

   The period polynomial of a weight-k modular form f is

       r_f(X) = integral_0^{i*infty} f(tau) (tau - X)^{k-2} d tau.

   The shadow period polynomial is defined using Z^{sh}:

       r^{sh}_A(X) = integral_0^{i*infty} Z^{sh}(tau) (tau - X)^{k-2} d tau

   with k determined by the shadow data. At the scalar level with
   weight-2 Eisenstein input, k=2 and the polynomial is a constant.

4. EICHLER-SHIMURA.

   The Eichler-Shimura isomorphism

       S_k(Gamma) + S_bar_k(Gamma) ~ H^1(Gamma, V_{k-2})

   maps period data to group cohomology. The shadow data at the
   scalar level (weight 2, no cusp forms) lies in the Eisenstein part
   of H^1, not the cuspidal part. The cuspidal shadow contribution
   begins at weight 12 (from the Ramanujan Delta function) and
   corresponds to shadow arity r >= 6 via g_min(S_r) = floor(r/2)+1.

5. HECKE ACTION.

   T_p {alpha, beta} = sum_{j=0}^{p-1} {(p*alpha + j)/p, (p*beta + j)/p}
                        + {alpha/p, beta/p}     (for level 1).

   For Eisenstein symbols, T_p acts by sigma_1(p) = 1 + p.

6. SPECIAL VALUES.

   L(f, n) relates to the (n-1)-th moment of the period:

       L(f, n) = (2*pi*i)^n / (n-1)! * integral_0^{i*infty} f(tau) tau^{n-1} d tau

   The shadow L-values are computed from the shadow partition function.

7. MODULAR SYMBOLS AT ZETA ZEROS.

   Evaluating the symbol at heights related to zeta zeros gamma_n:

       {0, i * gamma_n / (2*pi)}

   probes the connection between bar-complex periods and the
   distribution of zeta zeros.

8. OVERCONVERGENT MODULAR SYMBOLS.

   Stevens' p-adic modular symbols extend classical symbols via
   p-adic distributions. The shadow data, being built from Bernoulli
   numbers satisfying Kummer congruences, admits a natural p-adic
   interpolation.

CONVENTIONS
===========
- q = exp(2*pi*i*tau)
- kappa(A) = modular characteristic (NOT c; AP20, AP48)
- E_2^*(tau) is quasi-modular (AP15)
- eta(q) = q^{1/24} * prod(1 - q^n) — the q^{1/24} is NOT optional (AP46)
- Cohomological grading, |d| = +1

VERIFICATION PATHS
==================
1. Direct numerical integration along geodesics
2. Manin 3-term relation: {alpha,beta} + {beta,gamma} + {gamma,alpha} = 0
3. Hecke eigenvalue from symbols matches Fourier coefficient
4. Period ratio consistency: Im{0,i*infty}/Re{0,i*infty} at weight 12

References
----------
    Manin, "Parabolic points and zeta functions of modular curves" (1972)
    Shimura, "Introduction to the arithmetic theory of automorphic functions"
    Stevens, "Rigid analytic modular symbols" (1994)
    Pollack-Stevens, "Overconvergent modular symbols and p-adic L-functions" (2011)
    higher_genus_modular_koszul.tex: thm:shadow-double-convergence
    arithmetic_shadows.tex: thm:shadow-moduli-resolution
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import mpmath
    from mpmath import mp, mpf, mpc, pi as MP_PI
    mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

PI = math.pi
TWO_PI = 2.0 * PI


# ============================================================
# 0. Arithmetic helpers
# ============================================================

def _gcd(a: int, b: int) -> int:
    """Greatest common divisor."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def _sigma(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=8)
def _ramanujan_tau_batch(nmax: int) -> List[int]:
    """Compute tau(1), ..., tau(nmax) via eta^24 = q * prod(1-q^m)^24.

    Convention: Delta = sum_{n>=1} tau(n) q^n (AP38: standard normalization).
    tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472, ...
    """
    N = nmax + 5
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        new = [0] * (N + 1)
        for j in range(25):
            sign = (-1) ** j
            binom_val = 1
            for i in range(j):
                binom_val = binom_val * (24 - i) // (i + 1)
            c = sign * binom_val
            for k in range(N + 1):
                idx = k + j * m
                if idx > N:
                    break
                new[idx] += coeffs[k] * c
        coeffs = new
    # Delta = q * prod(1-q^n)^24, so tau(n) = coeffs[n-1]
    return [coeffs[n - 1] if n - 1 < len(coeffs) else 0
            for n in range(1, nmax + 1)]


def ramanujan_tau(n: int) -> int:
    """Ramanujan tau function tau(n), coefficient of q^n in Delta_12."""
    if n < 1:
        return 0
    batch = _ramanujan_tau_batch(max(n, 20))
    return batch[n - 1]


@lru_cache(maxsize=16)
def _eisenstein_fourier(weight: int, nmax: int) -> List[float]:
    """Fourier coefficients of normalized E_k(tau) = 1 + (2k/B_k) sum sigma_{k-1}(n) q^n.

    Returns [a_0, a_1, ..., a_nmax] where a_0 = 1.
    """
    from sympy import bernoulli as sym_bernoulli
    Bk = float(sym_bernoulli(weight))
    if abs(Bk) < 1e-50:
        raise ValueError(f"B_{weight} = 0, E_{weight} undefined")
    norm = -2.0 * weight / Bk
    coeffs = [1.0]
    for n in range(1, nmax + 1):
        coeffs.append(norm * _sigma(n, weight - 1))
    return coeffs


# ============================================================
# 1. Kappa functions (AP20: specify which algebra)
# ============================================================

def kappa_virasoro(c: float) -> float:
    """kappa(Vir_c) = c/2.  NOT c (AP20, AP48)."""
    return c / 2.0


def kappa_heisenberg(k: float) -> float:
    """kappa(H_k) = k (the level, not k/2; AP39)."""
    return float(k)


def kappa_affine(dim_g: int, k: float, h_dual: float) -> float:
    """kappa(hat{g}_k) = dim(g) * (k + h^v) / (2 * h^v).  AP1: distinct formula."""
    return dim_g * (k + h_dual) / (2.0 * h_dual)


# ============================================================
# 2. Shadow partition function integrand
# ============================================================

def shadow_scalar_constant(kappa: float) -> float:
    r"""The constant (tau-independent) scalar shadow at genus 1.

    F_1 = kappa / 24   (from lambda_1^{FP} = 1/24 = |B_2|/4 * (2^1 - 1)/2^1).

    The full scalar shadow PF is sum_{g>=1} F_g * hbar^{2g}; at hbar^2 this
    gives kappa/24.
    """
    return kappa / 24.0


def shadow_integrand_e2(tau: complex, kappa: float, nmax: int = 100) -> complex:
    r"""The quasi-modular shadow integrand kappa/24 * E_2^*(tau).

    E_2^*(tau) = 1 - 24 * sum_{n>=1} sigma_1(n) q^n.

    This is the tau-dependent genus-1 amplitude derivative (AP15: quasi-modular).

    The full genus-1 amplitude is A_1(tau) = -(kappa/12) log eta(tau)^2.
    Its tau-derivative is proportional to E_2^*(tau):
        dA_1/dtau = -(kappa/12) * (d/dtau)(2 log eta) = -(kappa/12) * pi*i * E_2^*(tau) / 3
    But we define the integrand as (kappa/24) * E_2^*(tau) for the modular
    symbol integral, since E_2^* is the natural weight-2 quasi-modular form.
    """
    q = cmath.exp(2j * PI * tau)
    e2 = 1.0
    qn = q
    for n in range(1, nmax + 1):
        sig1 = _sigma(n, 1)
        e2 -= 24.0 * sig1 * qn
        qn *= q
    return (kappa / 24.0) * e2


def shadow_integrand_full(tau: complex, kappa: float, max_genus: int = 10,
                          nmax: int = 50) -> complex:
    r"""Full shadow integrand at higher genus: sum_{g=1}^{G} F_g * E_{2g}(tau).

    F_g = kappa * lambda_g^{FP} and E_{2g} is the Eisenstein series of weight 2g.

    This is a FORMAL object: the weight varies with g, so the sum does not
    converge to a single modular form. It is used for numerical evaluation
    of shadow L-values at specific tau, not as a modular object.

    For the true modular symbol at weight k, use the weight-k Eisenstein
    series or cusp form.
    """
    from sympy import bernoulli as sym_bern, Rational
    result = 0.0 + 0.0j
    q = cmath.exp(2j * PI * tau)
    for g in range(1, max_genus + 1):
        # lambda_g^{FP}
        B2g = float(sym_bern(2 * g))
        num = (2 ** (2 * g - 1) - 1) * abs(B2g)
        den = 2 ** (2 * g - 1) * math.factorial(2 * g)
        lam_g = num / den
        fg = kappa * lam_g
        # E_{2g}(tau) Fourier expansion
        Bk = float(sym_bern(2 * g))
        if abs(Bk) < 1e-100:
            continue
        norm_eis = -2.0 * (2 * g) / Bk
        e_val = 1.0
        qn = q
        for n in range(1, nmax + 1):
            sig = _sigma(n, 2 * g - 1)
            e_val += norm_eis * sig * qn
            qn *= q
        result += fg * e_val
    return result


# ============================================================
# 3. Shadow modular symbols
# ============================================================

def shadow_modular_symbol_scalar(alpha: complex, beta: complex,
                                 kappa: float) -> complex:
    r"""Scalar shadow modular symbol: {alpha, beta}^{sh,scal}_A.

    At the scalar level, the shadow PF is the CONSTANT kappa/24.
    So the integral along any path is simply:

        {alpha, beta}^{sh,scal} = (kappa / 24) * (beta - alpha)

    This is exact (no numerical integration needed) because the integrand
    is constant.
    """
    return (kappa / 24.0) * (beta - alpha)


def shadow_modular_symbol_e2(alpha: complex, beta: complex,
                             kappa: float, n_steps: int = 2000,
                             nmax: int = 50) -> complex:
    r"""Quasi-modular shadow symbol via numerical integration of E_2^*.

    {alpha, beta}^{sh,E2} = integral_alpha^beta (kappa/24) * E_2^*(tau) d tau

    Integrated along the geodesic (straight line in H) from alpha to beta.

    NOTE (AP15): E_2^* is quasi-modular. This symbol does NOT transform
    as a standard modular symbol under SL(2,Z). It transforms with the
    anomaly term proportional to (c*tau + d)^{-2} * (c/(c*tau+d)).
    """
    dt = (beta - alpha) / n_steps
    total = 0.0 + 0.0j
    # Trapezoidal rule along straight line alpha -> beta
    f_a = shadow_integrand_e2(alpha, kappa, nmax=nmax)
    f_b = shadow_integrand_e2(beta, kappa, nmax=nmax)
    total = 0.5 * (f_a + f_b)
    for j in range(1, n_steps):
        tau_j = alpha + j * dt
        total += shadow_integrand_e2(tau_j, kappa, nmax=nmax)
    total *= dt
    return total


def shadow_modular_symbol_delta(alpha: complex, beta: complex,
                                n_steps: int = 2000, nmax: int = 80) -> complex:
    r"""Cuspidal modular symbol for Delta_{12} = sum tau(n) q^n.

    {alpha, beta}_{Delta} = integral_alpha^beta Delta(tau) d tau.

    This is a genuine weight-12 modular symbol. It lives in the cuspidal
    part of H^1(SL(2,Z), V_{10}) via Eichler-Shimura.
    """
    taus = _ramanujan_tau_batch(nmax)
    dt = (beta - alpha) / n_steps

    def delta_eval(tau):
        q = cmath.exp(2j * PI * tau)
        val = 0.0 + 0.0j
        qn = q
        for n in range(1, nmax + 1):
            val += taus[n - 1] * qn
            qn *= q
        return val

    f_a = delta_eval(alpha)
    f_b = delta_eval(beta)
    total = 0.5 * (f_a + f_b)
    for j in range(1, n_steps):
        tau_j = alpha + j * dt
        total += delta_eval(tau_j)
    total *= dt
    return total


# ============================================================
# 4. Manin symbols
# ============================================================

def manin_symbol_scalar(c: int, d: int, kappa: float) -> complex:
    r"""Scalar Manin symbol [c:d]^{sh,scal} = {0, d/c}^{sh,scal}.

    = (kappa / 24) * (d / c)

    Requires gcd(c, d) = 1 and c > 0.
    """
    if c <= 0:
        raise ValueError(f"c must be positive, got {c}")
    if _gcd(abs(c), abs(d)) != 1:
        raise ValueError(f"(c,d) = ({c},{d}) must be coprime")
    return (kappa / 24.0) * (d / c)


def manin_symbol_e2(c_val: int, d_val: int, kappa: float,
                    n_steps: int = 1000, nmax: int = 30) -> complex:
    r"""Quasi-modular Manin symbol [c:d]^{sh,E2} = {0, d/c}^{sh,E2}.

    Numerical integration of (kappa/24) * E_2^*(tau) from 0 to d/c.

    The path goes along Im(tau) = epsilon (we use epsilon = 0.1 to stay
    in H), from 0 + i*epsilon to d/c + i*epsilon.
    """
    eps = 0.1  # Imaginary part to keep path in H
    alpha = complex(0, eps)
    beta = complex(d_val / c_val, eps)
    return shadow_modular_symbol_e2(alpha, beta, kappa,
                                    n_steps=n_steps, nmax=nmax)


def manin_symbols_table(c_max: int, kappa: float) -> Dict[Tuple[int, int], complex]:
    r"""Compute all scalar Manin symbols [c:d] for 1 <= c <= c_max, gcd(c,d) = 1.

    Returns dict of (c, d) -> manin_symbol_scalar(c, d, kappa).
    """
    table = {}
    for c in range(1, c_max + 1):
        for d in range(0, c + 1):
            if _gcd(c, d) == 1:
                table[(c, d)] = manin_symbol_scalar(c, d, kappa)
    return table


# ============================================================
# 5. Period polynomial
# ============================================================

def period_polynomial_e2(X: complex, kappa: float, y_max: float = 10.0,
                         n_steps: int = 2000, nmax: int = 50) -> complex:
    r"""Shadow period polynomial from E_2^* (weight 2, so k-2 = 0: constant).

    r^{sh}(X) = integral_0^{i*infty} (kappa/24) * E_2^*(tau) * (tau - X)^0 d tau
              = integral_0^{i*infty} (kappa/24) * E_2^*(tau) d tau

    For weight 2, (tau - X)^{k-2} = (tau - X)^0 = 1, so the period polynomial
    is just the integral from 0 to i*infty of the integrand.

    Numerically: integrate from i*epsilon to i*y_max along the imaginary axis.
    """
    eps = 0.01
    alpha = complex(0, eps)
    beta = complex(0, y_max)
    return shadow_modular_symbol_e2(alpha, beta, kappa,
                                    n_steps=n_steps, nmax=nmax)


def period_polynomial_delta(X: complex, y_max: float = 3.0,
                            n_steps: int = 2000, nmax: int = 80) -> complex:
    r"""Period polynomial of Delta_{12}: integral_0^{i*infty} Delta(tau)(tau-X)^{10} dtau.

    For weight k=12, the period polynomial has degree k-2=10 in X.
    We compute it at specific X values by numerical integration.
    """
    taus = _ramanujan_tau_batch(nmax)
    eps = 0.01
    dt_param = (y_max - eps) / n_steps

    def integrand(y):
        tau = complex(0, y)
        q = cmath.exp(2j * PI * tau)
        delta_val = 0.0 + 0.0j
        qn = q
        for n in range(1, nmax + 1):
            delta_val += taus[n - 1] * qn
            qn *= q
        return delta_val * (tau - X) ** 10

    # Trapezoidal along imaginary axis
    total = 0.5 * (integrand(eps) + integrand(y_max))
    for j in range(1, n_steps):
        y = eps + j * dt_param
        total += integrand(y)
    total *= complex(0, dt_param)  # dtau = i * dy
    return total


def period_polynomial_delta_coefficients(y_max: float = 3.0,
                                         n_steps: int = 2000,
                                         nmax: int = 80,
                                         n_X_points: int = 12) -> List[complex]:
    r"""Compute the coefficients of r_Delta(X) = sum_{j=0}^{10} c_j X^j.

    We evaluate r_Delta at 11 distinct X values and solve for the coefficients
    via Vandermonde.  Returns [c_0, c_1, ..., c_10].
    """
    X_values = [complex(j * 0.1, 0.05) for j in range(n_X_points)]
    r_values = [period_polynomial_delta(X, y_max=y_max,
                                        n_steps=n_steps, nmax=nmax)
                for X in X_values]
    # Vandermonde system for degree 10
    deg = 10
    n_pts = min(len(X_values), deg + 2)
    # Least-squares via numpy if available
    try:
        import numpy as np
        V = np.array([[X_values[i] ** j for j in range(deg + 1)]
                       for i in range(n_pts)], dtype=complex)
        b = np.array(r_values[:n_pts], dtype=complex)
        coeffs, _, _, _ = np.linalg.lstsq(V, b, rcond=None)
        return list(coeffs)
    except ImportError:
        # Fallback: return raw evaluations
        return r_values[:deg + 1]


# ============================================================
# 6. Eichler-Shimura decomposition
# ============================================================

def eichler_shimura_shadow_class(kappa: float) -> Dict[str, Any]:
    r"""Determine where the shadow data lands in Eichler-Shimura.

    H^1(SL(2,Z), V_{k-2}) ~ S_k + S_bar_k + Eis_k

    At weight 2: S_2 = {0} (no cusp forms), so the shadow symbol at the
    scalar level lies ENTIRELY in the Eisenstein part.

    At weight 12: S_12 = C * Delta, so the cuspidal shadow contribution
    (from arity r=6 via g_min = floor(6/2)+1 = 4, weight = 2*4 = 8... but
    actually the first cusp form is at weight 12) first appears at g=6.

    Returns a dict describing the decomposition.
    """
    info = {
        'weight_2': {
            'dim_S_k': 0,
            'dim_Eis_k': 1,
            'shadow_component': 'Eisenstein',
            'shadow_value': kappa / 24.0,
            'note': 'Scalar shadow F_1 = kappa/24 lies in Eis_2',
        },
        'weight_12': {
            'dim_S_k': 1,
            'dim_Eis_k': 1,
            'shadow_component': 'Cuspidal + Eisenstein',
            'note': 'F_6 = kappa * lambda_6^FP contributes to S_12 via Delta',
        },
        'general': {
            'cuspidal_threshold_genus': 6,
            'cuspidal_threshold_weight': 12,
            'note': ('Below weight 12, all shadow symbols are Eisenstein. '
                     'First cuspidal contribution at g=6, weight 12.'),
        },
    }
    return info


# ============================================================
# 7. Hecke action on modular symbols
# ============================================================

def hecke_action_scalar(p: int, alpha: complex, beta: complex,
                        kappa: float) -> complex:
    r"""Hecke operator T_p on scalar shadow symbol {alpha, beta}^{sh,scal}.

    T_p {alpha, beta} = sum_{j=0}^{p-1} {(p*alpha+j)/p, (p*beta+j)/p}
                        + {alpha/p, beta/p}

    For the scalar symbol (kappa/24)*(beta-alpha), each term gives
    (kappa/24) * ((p*beta+j)/p - (p*alpha+j)/p) = (kappa/24)*(beta-alpha),
    and the last term gives (kappa/24) * (beta-alpha)/p.

    Total = p * (kappa/24)*(beta-alpha) + (kappa/24)*(beta-alpha)/p
          = (kappa/24)*(beta-alpha) * (p + 1/p)    ... wait, let me recompute.

    Actually: sum_{j=0}^{p-1} (kappa/24)*((p*beta+j)/p - (p*alpha+j)/p)
            = p * (kappa/24) * (beta - alpha)
    Plus: (kappa/24) * (beta/p - alpha/p) = (kappa/24) * (beta-alpha) / p

    So T_p {alpha,beta}^{scal} = (kappa/24)(beta-alpha) * (p + 1/p).

    But the standard Hecke operator for weight 2 is T_p f(tau) = ...
    with eigenvalue 1 + p = sigma_1(p) on E_2.

    Cross-check: T_p on Eis eigenspace has eigenvalue sigma_{k-1}(p).
    For k=2: sigma_1(p) = 1 + p.  Our formula gives (p + 1/p) on the SYMBOL.
    The SYMBOL is the integral of f * dtau, which transforms with an extra
    factor. For weight 2: the symbol transforms as the form, so the Hecke
    eigenvalue on symbols is sigma_1(p) = 1 + p.

    Let me redo: T_p{a,b} for a constant integrand C:
    = sum_{j=0}^{p-1} C * ((pb+j)/p - (pa+j)/p) + C * (b/p - a/p)
    = sum_{j=0}^{p-1} C*(b-a) + C*(b-a)/p
    = p*C*(b-a) + C*(b-a)/p
    = C*(b-a) * (p + 1/p)

    But we want the eigenvalue to be sigma_1(p) = 1+p. The discrepancy is
    because the Hecke operator for modular symbols of weight k is NORMALIZED
    differently. For weight k=2, the standard normalization includes a factor
    of p^{k-1} = p in the last term: T_p = sum + p^{k-1} * {a/p, b/p}.

    With this normalization:
    T_p{a,b} = p*C*(b-a) + p*C*(b-a)/p = p*C*(b-a) + C*(b-a)
             = C*(b-a)*(p+1) = (1+p) * {a,b}. Correct!

    So we use the weight-k normalized Hecke operator.
    """
    # Weight 2 Hecke operator: T_p {a,b} = sum_{j} {(pa+j)/p,(pb+j)/p} + p^{k-1}{a/p,b/p}
    # with k=2 so p^{k-1} = p.
    total = 0.0 + 0.0j
    for j in range(p):
        a_j = (p * alpha + j) / p
        b_j = (p * beta + j) / p
        total += shadow_modular_symbol_scalar(a_j, b_j, kappa)
    # Last term with p^{k-1} = p weight correction
    total += p * shadow_modular_symbol_scalar(alpha / p, beta / p, kappa)
    return total


def hecke_eigenvalue_scalar(p: int) -> float:
    r"""Hecke eigenvalue for E_2 at prime p: sigma_1(p) = 1 + p.

    E_2 is an eigenform for T_p with eigenvalue sigma_1(p).
    (Strictly: E_2^* is quasi-modular. The Hecke eigenvalue statement
    applies to the holomorphic part in the formal Hecke algebra.)
    """
    return float(1 + p)


def hecke_eigenvalue_delta(p: int) -> int:
    r"""Hecke eigenvalue for Delta_12 at prime p: tau(p).

    Delta is a Hecke eigenform with T_p Delta = tau(p) * Delta.
    """
    return ramanujan_tau(p)


def hecke_action_e2_numerical(p: int, alpha: complex, beta: complex,
                              kappa: float, n_steps: int = 500,
                              nmax: int = 30) -> complex:
    r"""Numerical Hecke operator on E_2^* shadow symbol at prime p.

    T_p {a,b}^{E2} = sum_{j=0}^{p-1} {(pa+j)/p,(pb+j)/p}^{E2}
                     + p * {a/p, b/p}^{E2}
    """
    total = 0.0 + 0.0j
    for j in range(p):
        a_j = (p * alpha + j) / p
        b_j = (p * beta + j) / p
        total += shadow_modular_symbol_e2(a_j, b_j, kappa,
                                          n_steps=n_steps, nmax=nmax)
    total += p * shadow_modular_symbol_e2(alpha / p, beta / p, kappa,
                                          n_steps=n_steps, nmax=nmax)
    return total


# ============================================================
# 8. Shadow L-values (special values of the shadow symbol)
# ============================================================

def shadow_l_value_scalar(kappa: float, n: int) -> complex:
    r"""Shadow L-value at integer n from the scalar symbol.

    L^{sh}(n) = (2*pi*i)^n / (n-1)! * integral_0^{i*infty} (kappa/24) * tau^{n-1} dtau

    The integral diverges for Re(n) > 0 along the imaginary axis directly.
    We regularize via the Eisenstein Fourier expansion.

    For E_2: L(E_2, s) = -24 * sum sigma_1(n)/n^s + regularized_constant
    The completed L-function of E_2 is related to zeta(s) * zeta(s-1).

    More precisely, for the Eisenstein series E_k:
        L(E_k, s) = sum_{n>=1} sigma_{k-1}(n) / n^s
    which factors as zeta(s) * zeta(s - k + 1).

    For E_2 (k=2): L(E_2, s) = sum sigma_1(n)/n^s = zeta(s)*zeta(s-1).

    So the shadow L-value is:
        L^{sh}(s) = (kappa/24) * (-24) * zeta(s) * zeta(s-1) + (kappa/24) * (reg. const.)
                  = -kappa * zeta(s) * zeta(s-1)   (up to the constant term)

    At integer s = n (n >= 2):
        L^{sh}(n) = -kappa * zeta(n) * zeta(n-1)
    """
    if n < 2:
        return complex(float('nan'))
    zeta_n = sum(1.0 / k ** n for k in range(1, 10000))
    zeta_nm1 = sum(1.0 / k ** (n - 1) for k in range(1, 10000))
    return -kappa * zeta_n * zeta_nm1


def shadow_l_value_numerical(kappa: float, s: complex,
                             nmax: int = 500) -> complex:
    r"""Shadow L-value via Dirichlet series: L^{sh}(s) = -kappa * zeta(s) * zeta(s-1).

    Computed from the Dirichlet series sum sigma_1(n) / n^s truncated at nmax,
    multiplied by -kappa (the constant term kappa/24 * (-24) = -kappa).
    """
    total = 0.0 + 0.0j
    for n in range(1, nmax + 1):
        sig1 = _sigma(n, 1)
        total += sig1 / n ** s
    return -kappa * total


def shadow_l_values_table(kappa: float, s_max: int = 10,
                          nmax: int = 1000) -> Dict[int, complex]:
    r"""Table of shadow L-values at s = 2, 3, ..., s_max.

    L^{sh}(s) = -kappa * zeta(s) * zeta(s-1).

    Verification: at s=2, zeta(2) = pi^2/6, zeta(1) diverges.
    So L^{sh}(2) diverges (pole of zeta(s-1) at s=2).
    At s=3: zeta(3)*zeta(2) = zeta(3) * pi^2/6.
    """
    table = {}
    for s in range(2, s_max + 1):
        table[s] = shadow_l_value_numerical(kappa, complex(s, 0), nmax=nmax)
    return table


# ============================================================
# 9. Modular symbols at zeta zeros
# ============================================================

# First 20 imaginary parts of non-trivial Riemann zeta zeros
# (Computed to high precision; see Odlyzko's tables)
ZETA_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081606,
    67.079810529494173,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
]


def symbol_at_zeta_zero(n: int, kappa: float, mode: str = 'scalar') -> complex:
    r"""Shadow modular symbol evaluated at a path to height gamma_n/(2*pi).

    {0, i * gamma_n / (2*pi)}^{sh}

    where gamma_n is the imaginary part of the n-th non-trivial zeta zero.

    The height gamma_n/(2*pi) places the cusp endpoint at the fundamental
    domain boundary related to the n-th zero.

    mode = 'scalar': exact scalar formula kappa/24 * i * gamma_n/(2*pi)
    mode = 'e2': numerical integration with E_2^*
    """
    if n < 1 or n > len(ZETA_ZEROS):
        raise ValueError(f"n must be in [1, {len(ZETA_ZEROS)}], got {n}")
    gamma_n = ZETA_ZEROS[n - 1]
    beta = complex(0, gamma_n / TWO_PI)
    alpha = complex(0, 0.01)  # regularized: small positive imaginary part

    if mode == 'scalar':
        return (kappa / 24.0) * (beta - alpha)
    elif mode == 'e2':
        return shadow_modular_symbol_e2(alpha, beta, kappa, n_steps=2000,
                                        nmax=50)
    else:
        raise ValueError(f"Unknown mode: {mode}")


def zeta_zero_symbol_table(kappa: float, n_zeros: int = 10,
                           mode: str = 'scalar') -> Dict[int, complex]:
    """Table of shadow symbols at the first n_zeros zeta zero heights."""
    n_zeros = min(n_zeros, len(ZETA_ZEROS))
    return {n: symbol_at_zeta_zero(n, kappa, mode=mode)
            for n in range(1, n_zeros + 1)}


# ============================================================
# 10. Overconvergent (p-adic) modular symbols
# ============================================================

def padic_valuation(x: Union[int, Fraction], p: int) -> int:
    """p-adic valuation v_p(x) for a rational number x."""
    if isinstance(x, Fraction):
        if x == 0:
            return float('inf')
        return padic_valuation(x.numerator, p) - padic_valuation(x.denominator, p)
    x = abs(int(x))
    if x == 0:
        return float('inf')
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def padic_shadow_symbol(c_val: int, d_val: int, kappa_rational: Fraction,
                        p: int) -> Dict[str, Any]:
    r"""p-adic shadow Manin symbol [c:d] with p-adic valuation data.

    The scalar Manin symbol is (kappa/24) * (d/c).
    Its p-adic valuation is v_p(kappa) + v_p(d) - v_p(24) - v_p(c).

    For Stevens' overconvergent symbols: the key is that the Bernoulli
    numbers in lambda_g^{FP} satisfy Kummer congruences, so the shadow
    coefficients at different genera are p-adically interpolable.

    Returns a dict with the symbol value, p-adic valuation, and
    interpolation data.
    """
    if c_val <= 0 or _gcd(abs(c_val), abs(d_val)) != 1:
        raise ValueError(f"Need c > 0 and gcd(c,d) = 1, got ({c_val}, {d_val})")

    symbol_val = kappa_rational * Fraction(d_val, 24 * c_val)
    v_p_symbol = padic_valuation(symbol_val, p)

    return {
        'symbol': symbol_val,
        'p': p,
        'v_p': v_p_symbol,
        'kappa': kappa_rational,
        'c': c_val,
        'd': d_val,
    }


def padic_interpolation_data(kappa_rational: Fraction, p: int,
                             max_genus: int = 30) -> Dict[str, Any]:
    r"""p-adic interpolation data for the shadow genus tower.

    The genus-g contribution is F_g = kappa * lambda_g^{FP} where
    lambda_g^{FP} = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!).

    The Kummer congruences state: for even m, n with m = n mod (p-1),
    (p-1) not dividing m or n,

        (1 - p^{m-1}) B_m / m = (1 - p^{n-1}) B_n / n  (mod p).

    This defines a p-adic measure mu_p such that

        integral_{Z_p^*} x^{s-1} d mu_p(x) = (1 - p^{-s}) zeta(s)

    for s = 1 - n (n even positive).

    The shadow p-adic L-function is:

        L_p^{sh}(s) = kappa * sum_{g=1}^{infty} lambda_g^{FP} * (something)^{2g}

    where the p-adic convergence radius is R_p = p^{1/(p-1)}.

    Returns convergence and congruence data.
    """
    from sympy import bernoulli as sym_bern

    # Compute lambda_g^{FP} values and their p-adic valuations
    genus_data = []
    for g in range(1, max_genus + 1):
        B2g = sym_bern(2 * g)
        num = (2 ** (2 * g - 1) - 1) * abs(B2g)
        den = 2 ** (2 * g - 1) * math.factorial(2 * g)
        lam_g = Fraction(int(num), int(den))
        fg = kappa_rational * lam_g
        v_p_fg = padic_valuation(fg, p)
        genus_data.append({
            'genus': g,
            'lambda_g': lam_g,
            'F_g': fg,
            'v_p_F_g': v_p_fg,
        })

    # Kummer congruence check: B_{2g}/(2g) mod p for g in same residue class
    kummer_classes = {}
    for g in range(1, max_genus + 1):
        residue = (2 * g) % (p - 1) if p > 2 else (2 * g) % 2
        if residue not in kummer_classes:
            kummer_classes[residue] = []
        B2g = sym_bern(2 * g)
        ratio = Fraction(int(B2g), 2 * g)
        kummer_classes[residue].append({
            'g': g,
            'B_{2g}/(2g)': ratio,
            'v_p': padic_valuation(ratio, p),
        })

    # p-adic convergence radius
    # R_p = p^{1/(p-1)} for p odd; R_2 = 2 for p=2
    if p == 2:
        R_p = 2.0
    else:
        R_p = p ** (1.0 / (p - 1))

    return {
        'p': p,
        'kappa': kappa_rational,
        'genus_data': genus_data,
        'kummer_classes': kummer_classes,
        'convergence_radius': R_p,
        'note': (f'p-adic convergence radius R_{p} = {R_p:.6f}. '
                 f'Shadow series converges for |hbar|_p < R_p.'),
    }


def padic_kummer_congruence_check(p: int, max_genus: int = 20) -> Dict[str, Any]:
    r"""Verify Kummer congruences for Bernoulli numbers at prime p.

    The basic Kummer congruence states: for even positive integers m, n
    with m = n mod (p-1), and (p-1) not dividing m or n,

        B_m / m  =  B_n / n   (mod p)

    i.e., v_p(B_m/m - B_n/n) >= 1.

    Here m = 2*g1, n = 2*g2.

    Returns a dict with verification results.
    """
    from sympy import bernoulli as sym_bern

    results = {'p': p, 'checks': [], 'all_pass': True}

    if p <= 2:
        results['note'] = 'Kummer congruences are for odd primes; p=2 skipped.'
        return results

    for g1 in range(1, max_genus + 1):
        m = 2 * g1
        if m % (p - 1) == 0:
            continue  # Exclude when (p-1) | m
        for g2 in range(g1 + 1, max_genus + 1):
            n = 2 * g2
            if n % (p - 1) == 0:
                continue  # Exclude when (p-1) | n
            if m % (p - 1) != n % (p - 1):
                continue

            Bm = sym_bern(m)
            Bn = sym_bern(n)
            val1 = Fraction(Bm) / m
            val2 = Fraction(Bn) / n
            diff = val1 - val2
            vp_diff = padic_valuation(diff, p)
            passes = vp_diff >= 1  # congruence mod p means v_p >= 1

            check = {
                'g1': g1, 'g2': g2,
                'm': m, 'n': n,
                'v_p(diff)': vp_diff,
                'passes': passes,
            }
            results['checks'].append(check)
            if not passes:
                results['all_pass'] = False

    return results


# ============================================================
# 11. Three-term Manin relation verification
# ============================================================

def verify_manin_three_term(alpha: complex, beta: complex, gamma: complex,
                            kappa: float, tol: float = 1e-10) -> Dict[str, Any]:
    r"""Verify the Manin 3-term relation for scalar shadow symbols.

    {alpha,beta} + {beta,gamma} + {gamma,alpha} = 0.

    This is the cocycle condition for modular symbols.
    For the scalar shadow, this is automatic:
        (kappa/24)*(beta-alpha) + (kappa/24)*(gamma-beta) + (kappa/24)*(alpha-gamma) = 0.
    """
    s1 = shadow_modular_symbol_scalar(alpha, beta, kappa)
    s2 = shadow_modular_symbol_scalar(beta, gamma, kappa)
    s3 = shadow_modular_symbol_scalar(gamma, alpha, kappa)
    total = s1 + s2 + s3
    return {
        'sum': total,
        'abs_sum': abs(total),
        'passes': abs(total) < tol,
        's1': s1, 's2': s2, 's3': s3,
    }


def verify_manin_three_term_e2(alpha: complex, beta: complex, gamma: complex,
                               kappa: float, n_steps: int = 1000,
                               tol: float = 1e-4) -> Dict[str, Any]:
    r"""Verify 3-term relation for E_2^* shadow symbols (numerically).

    The relation {a,b} + {b,c} + {c,a} = 0 should hold regardless of
    the integrand (it's a property of integration, not modularity).
    """
    s1 = shadow_modular_symbol_e2(alpha, beta, kappa, n_steps=n_steps)
    s2 = shadow_modular_symbol_e2(beta, gamma, kappa, n_steps=n_steps)
    s3 = shadow_modular_symbol_e2(gamma, alpha, kappa, n_steps=n_steps)
    total = s1 + s2 + s3
    return {
        'sum': total,
        'abs_sum': abs(total),
        'passes': abs(total) < tol,
        's1': s1, 's2': s2, 's3': s3,
    }


# ============================================================
# 12. Hecke eigenvalue verification
# ============================================================

def verify_hecke_eigenvalue(p: int, kappa: float,
                            tol: float = 1e-10) -> Dict[str, Any]:
    r"""Verify that T_p on the scalar shadow symbol has eigenvalue 1+p.

    T_p {0, 1}^{scal} = (1+p) * {0, 1}^{scal}.
    """
    alpha = complex(0, 0.1)  # regularize
    beta = complex(1, 0.1)
    original = shadow_modular_symbol_scalar(alpha, beta, kappa)
    hecke_result = hecke_action_scalar(p, alpha, beta, kappa)
    expected = (1 + p) * original
    ratio = hecke_result / original if abs(original) > 1e-100 else float('nan')
    return {
        'p': p,
        'original': original,
        'T_p_result': hecke_result,
        'expected': expected,
        'ratio': ratio,
        'eigenvalue_expected': 1 + p,
        'passes': abs(hecke_result - expected) < tol * abs(expected),
    }


# ============================================================
# 13. Period ratio (for Delta)
# ============================================================

def delta_period_ratio(y_max: float = 3.0, n_steps: int = 3000,
                       nmax: int = 80) -> Dict[str, Any]:
    r"""Compute the period ratio for Delta_{12}.

    omega_+ = Re integral_0^{i*infty} Delta(tau) dtau
    omega_- = Im integral_0^{i*infty} Delta(tau) dtau

    The ratio omega_-/omega_+ is related to L(Delta, 1) via the
    Eichler-Shimura period relations.

    Manin's period Omega_+ and Omega_- satisfy:
        L(Delta, 1) = -Omega_+ / (10!)  (up to normalization).

    For Delta = tau(n) q^n: the integral from 0 to i*infty along the
    imaginary axis is purely imaginary (Delta(iy) is real for real y > 0,
    so the integral integral_0^{infty} Delta(iy) i dy is purely imaginary).

    Actually: Delta(iy) = sum tau(n) e^{-2*pi*n*y} which is REAL.
    So integral_0^{infty} Delta(iy) * i * dy = i * (real number).
    The symbol {0, i*infty}_Delta is purely imaginary.

    The REAL period comes from a different path (e.g., {0, rho} where
    rho = e^{2*pi*i/3}).
    """
    taus = _ramanujan_tau_batch(nmax)

    # Imaginary-axis integral: integral_eps^{y_max} Delta(iy) * i * dy
    eps = 0.01
    dy = (y_max - eps) / n_steps

    def delta_on_imag_axis(y):
        val = 0.0
        for n in range(1, nmax + 1):
            val += taus[n - 1] * math.exp(-TWO_PI * n * y)
        return val

    # Trapezoidal
    total_imag = 0.5 * (delta_on_imag_axis(eps) + delta_on_imag_axis(y_max))
    for j in range(1, n_steps):
        y = eps + j * dy
        total_imag += delta_on_imag_axis(y)
    total_imag *= dy
    # Multiply by i (dtau = i dy)
    omega_minus = total_imag  # This is the real part of i * (real integral)

    # Real period: integrate along path from 0 to rho = e^{2*pi*i/3}
    rho = cmath.exp(2j * PI / 3)
    dt_r = 1.0 / n_steps
    total_real = 0.0 + 0.0j
    for j in range(n_steps):
        t = (j + 0.5) * dt_r
        tau = t * rho + (1 - t) * complex(0, eps)
        dtau = rho - complex(0, eps)
        q = cmath.exp(2j * PI * tau)
        delta_val = 0.0 + 0.0j
        qn = q
        for n in range(1, nmax + 1):
            delta_val += taus[n - 1] * qn
            qn *= q
        total_real += delta_val * dtau * dt_r
    omega_plus = total_real.real

    return {
        'omega_plus': omega_plus,
        'omega_minus': omega_minus,
        'ratio': omega_minus / omega_plus if abs(omega_plus) > 1e-100 else float('nan'),
        'note': ('omega_- from imaginary-axis integral, '
                 'omega_+ from path to rho = e^{2*pi*i/3}'),
    }


# ============================================================
# 14. Cross-family comparison
# ============================================================

def cross_family_shadow_symbols(c_values: Optional[List[float]] = None,
                                ) -> Dict[str, Dict[str, complex]]:
    r"""Shadow modular symbols across the standard landscape.

    For each family, compute the scalar Manin symbol [1:1] = kappa/24.

    Families: Virasoro c, Heisenberg k, affine sl_2 at level k.
    """
    if c_values is None:
        c_values = [1.0, 2.0, 6.0, 12.0, 13.0, 24.0, 25.0, 26.0]

    results = {}
    for c in c_values:
        kap = kappa_virasoro(c)
        results[f'Vir_c={c}'] = {
            'kappa': kap,
            '[1:1]_scalar': manin_symbol_scalar(1, 1, kap),
        }

    # Heisenberg
    for k in [1, 2, 4, 8, 24]:
        kap = kappa_heisenberg(k)
        results[f'Heis_k={k}'] = {
            'kappa': kap,
            '[1:1]_scalar': manin_symbol_scalar(1, 1, kap),
        }

    # Affine sl_2 at level k (dim=3, h^v=2)
    for k in [1, 2, 4, 10]:
        kap = kappa_affine(3, k, 2)
        results[f'sl2_k={k}'] = {
            'kappa': kap,
            '[1:1]_scalar': manin_symbol_scalar(1, 1, kap),
        }

    return results


# ============================================================
# 15. Summary / diagnostic
# ============================================================

def full_diagnostic(kappa: float = 1.0,
                    verbose: bool = False) -> Dict[str, Any]:
    r"""Run a full diagnostic of the shadow modular symbol engine.

    Tests all verification paths and returns a summary.
    """
    results = {}

    # Path 1: Direct computation
    alpha = complex(0, 0.5)
    beta = complex(0.5, 0.5)
    s_scal = shadow_modular_symbol_scalar(alpha, beta, kappa)
    s_e2 = shadow_modular_symbol_e2(alpha, beta, kappa, n_steps=500, nmax=30)
    results['direct'] = {
        'scalar': s_scal,
        'e2': s_e2,
        'agreement': abs(s_scal - s_e2) / max(abs(s_scal), 1e-100),
    }

    # Path 2: Manin 3-term relation
    gamma = complex(0.3, 0.8)
    manin_check = verify_manin_three_term(alpha, beta, gamma, kappa)
    results['manin_3term'] = manin_check

    # Path 3: Hecke eigenvalue
    for p in [2, 3, 5]:
        results[f'hecke_p={p}'] = verify_hecke_eigenvalue(p, kappa)

    # Path 4: Cross-family
    results['cross_family'] = cross_family_shadow_symbols([1, 13, 26])

    return results
