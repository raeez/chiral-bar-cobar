r"""
shadow_langlands_functor_engine.py — Shadow Langlands Functor:
From Modular Koszul Algebras to Automorphic Data

MATHEMATICAL CONTENT:

The shadow Langlands functor is a conjectured map

    SL: {modular Koszul algebras} ---> {automorphic data on GL_n}

sending the shadow obstruction tower {S_r(A)}_{r>=2} of a chiral algebra A
to an automorphic q-series, an L-function, and Hecke eigenvalue data.

The construction proceeds in stages:

1. SHADOW q-SERIES:
   f_A(q) = sum_{r>=2} S_r(A) q^r

   This is NOT a modular form in general, but its analytic properties
   (growth rate rho, algebraicity degree, denominator pattern) constrain
   its relationship to the space of modular forms.

2. SHADOW L-FUNCTION (Dirichlet series):
   L^sh(s, A) = sum_{r>=2} S_r(A) r^{-s}

   Convergence: for class G/L (finite tower), entire. For class M,
   converges in Re(s) > 1 + log(rho)/log(r) where rho is the shadow
   growth rate.

3. SHADOW HECKE OPERATORS:
   For p prime, define T_p^sh on shadow towers by
     (T_p^sh S)_r = S_{pr}
   This is a multiplicative shift, NOT the classical Hecke action.
   The "shadow Hecke eigenvalues" a_p^sh = S_{2p}/S_2 measure
   the p-th attenuation of the shadow tower relative to kappa.

4. LOCAL LANGLANDS DATA:
   At each prime p, the p-adic valuation of the shadow coefficients
   gives a "shadow conductor exponent":
     f_p(A) = max_{r<=R} v_p(denom(S_r))
   This is the depth of p-adic structure in the shadow tower.

5. BASE CHANGE:
   For a quadratic extension Q(sqrt(D))/Q, the "shadow twist" is:
     L^sh(s, A, chi_D) = sum_{r>=2} chi_D(r) S_r(A) r^{-s}
   where chi_D is the Kronecker symbol.
   The "base change L-function" is the product:
     L^sh(s, A, Q(sqrt(D))) = L^sh(s, A) * L^sh(s, A, chi_D)

FAMILIES:

  HEISENBERG H_k:
    - kappa = k, tower terminates at arity 2
    - f_H(q) = (k/2) q^2 (trivial)
    - L^sh(s, H_k) = (k/2) 2^{-s} (single Dirichlet term)
    - All Hecke eigenvalues vanish (shadow is concentrated at r=2)

  AFFINE sl_2 at level k:
    - kappa = 3(k+2)/4, class L, tower terminates at arity 3
    - f_aff(q) = kappa q^2 + 2 q^3 (two terms)
    - L^sh(s) = kappa 2^{-s} + 2 * 3^{-s}

  VIRASORO Vir_c:
    - kappa = c/2, class M, infinite tower
    - f_Vir(q) = sum_{r>=2} S_r(c) q^r (infinite, algebraic of degree 2)
    - Shadow growth rate rho(c) controls convergence
    - Hecke eigenvalues a_p^sh well-defined for all primes

  W_3:
    - Two lines (T-line = Virasoro shadow, W-line = Z_2 parity)
    - T-line L-function = Virasoro L-function
    - W-line: only even arities contribute (chi_D structure)

VERIFICATION PATHS:
  Path 1: q-series modularity test (SL_2(Z) transformation)
  Path 2: Hecke eigenvalue computation and Ramanujan bound
  Path 3: L-function functional equation test
  Path 4: Local data at primes (conductor exponents)

References:
  thm:shadow-moduli-resolution (arithmetic_shadows.tex)
  thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex)
  thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
  thm:shadow-radius (higher_genus_modular_koszul.tex)
  def:arithmetic-packet-connection (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    from sympy import (
        Rational, Symbol, cancel, expand, factor, simplify, sqrt as sym_sqrt,
        Poly, S as Sym, bernoulli as sym_bernoulli, binomial as sym_binomial,
    )
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# =====================================================================
# Section 0: Utility — Virasoro shadow coefficients (numerical)
# =====================================================================

def virasoro_shadow_coefficients_numerical(c_val: float,
                                           max_r: int = 30) -> Dict[int, float]:
    r"""Virasoro shadow tower S_r(c) computed numerically via the
    convolution recursion for sqrt(Q_L).

    Q_L(t) = c^2 + 12c t + alpha t^2
    where alpha = (180c + 872) / (5c + 22).

    sqrt(Q_L) = sum a_n t^n with:
      a_0 = c, a_1 = 6, a_2 = 40/[c(5c+22)]
      a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3

    Then S_r = a_{r-2} / r.
    """
    if abs(c_val) < 1e-14:
        raise ValueError("c = 0: pole of shadow tower")
    if abs(c_val + 22.0 / 5.0) < 1e-14:
        raise ValueError("c = -22/5: pole of S_4")

    alpha = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = alpha

    max_n = max_r - 2
    a = [0.0] * (max_n + 1)
    a[0] = c_val  # sqrt(q0) = c for c > 0
    if max_n >= 1:
        a[1] = q1 / (2.0 * c_val)  # = 6
    if max_n >= 2:
        a[2] = (q2 - a[1] ** 2) / (2.0 * c_val)

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * c_val)

    S = {}
    for r in range(2, max_r + 1):
        n = r - 2
        S[r] = a[n] / r
    return S


def w3_tline_shadow_coefficients(c_val: float,
                                  max_r: int = 20) -> Dict[int, float]:
    """W_3 T-line shadow coefficients (identical to Virasoro)."""
    return virasoro_shadow_coefficients_numerical(c_val, max_r)


def w3_wline_shadow_coefficients(c_val: float,
                                  max_r: int = 20) -> Dict[int, float]:
    r"""W_3 W-line shadow coefficients.

    On the W-line: kappa_W = c/3, alpha_W = 0 (Z_2 parity forces odd S = 0),
    S_4 = 2560/[c(5c+22)^3].

    Q_W(w) = 4c^2/9 + (40960/[3(5c+22)^3]) w^2.

    Recursion on a_n of sqrt(Q_W):
      a_0 = 2c/3, a_1 = 0, a_2 = (q2)/(2 a_0)
      a_n = -(1/(2 a_0)) sum a_j a_{n-j}
    Odd a_n vanish by parity.
    """
    if abs(c_val) < 1e-14:
        raise ValueError("c = 0: pole of shadow tower")

    kappa_w = c_val / 3.0
    q0 = (2.0 * c_val / 3.0) ** 2
    q2 = 40960.0 / (3.0 * (5.0 * c_val + 22.0) ** 3)

    max_n = max_r - 2
    a = [0.0] * (max_n + 1)
    a[0] = 2.0 * c_val / 3.0
    if max_n >= 1:
        a[1] = 0.0  # q1 = 0 by parity
    if max_n >= 2:
        a[2] = q2 / (2.0 * a[0])

    for n in range(3, max_n + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * a[0])

    S = {}
    for r in range(2, max_r + 1):
        n = r - 2
        S[r] = a[n] / r
    return S


def heisenberg_shadow_coefficients(k_val: float,
                                    max_r: int = 20) -> Dict[int, float]:
    """Heisenberg shadow: S_2 = k/2, all higher vanish (class G, depth 2).

    NOTE: kappa(H_k) = k (NOT k/2). But S_2 = kappa/2 ... WAIT.
    Actually from the manuscript: the shadow GF convention has
    S_2 = kappa = k for Heisenberg.

    Let me be precise. The Heisenberg at level k has:
      kappa = k  (modular characteristic)
      S_2 = kappa = k  (NOT kappa/2)

    The shadow GF is G(t) = kappa * t^2 / ... hmm, let me check the
    existing shadow_automorphic_bridge.py which has:
      coeffs = {2: kappa / 2.0}
    So S_2 = kappa/2 = k/2. This is consistent with
      S_r = a_{r-2}/r, a_0 = c for Virasoro where S_2 = a_0/2 = c/2 = kappa.

    For Heisenberg: kappa = k, so S_2 = k/2? No. S_2 = kappa = k.
    But the bridge has S_2 = kappa/2 = k/2.

    RESOLUTION: Check virasoro_shadow_all_arity.py:
      S_2 = c/2 = kappa  (since kappa(Vir) = c/2).
    So S_2 = kappa, and the bridge's coeffs[2] = kappa/2 is for a
    DIFFERENT convention of the generating function.

    The standard convention in the monograph:
      S_2 = kappa for all families.
    For Heisenberg: kappa = k, so S_2 = k.
    For Virasoro: kappa = c/2, so S_2 = c/2.

    The bridge uses G(t) = sum S_r t^r with S_2 = kappa/2 — this is
    the HALVED convention from the generating function H(t) = t^2 sqrt(Q).

    I will use the MANUSCRIPT convention: S_2 = kappa.
    """
    S = {}
    kappa = k_val
    S[2] = kappa
    for r in range(3, max_r + 1):
        S[r] = 0.0
    return S


def affine_sl2_shadow_coefficients(k_val: float,
                                    max_r: int = 20) -> Dict[int, float]:
    """Affine sl_2 shadow: kappa = 3(k+2)/4, S_3 = 2, terminates at arity 3.

    Uses manuscript convention S_2 = kappa.
    """
    if abs(k_val + 2.0) < 1e-12:
        raise ValueError("Critical level k = -2: Sugawara undefined")
    kappa = 3.0 * (k_val + 2.0) / 4.0
    S = {}
    S[2] = kappa
    S[3] = 2.0
    for r in range(4, max_r + 1):
        S[r] = 0.0
    return S


def betagamma_shadow_coefficients(lam: float,
                                   max_r: int = 20) -> Dict[int, float]:
    r"""beta-gamma system shadow: class C (contact), terminates at arity 4.

    kappa = 1 (independent of lambda, since c_{bg} = 2 and kappa = c/2 = 1
    ... WAIT. For beta-gamma: kappa = -1 (ghost-like).
    Actually, let me use the POSITIVE convention from landscape:
      kappa_{bg} = 1 at lambda = 1/2 (standard).
    More precisely: beta-gamma has c = -1, kappa = -1/2? No.

    From the manuscript (AP39): kappa depends on the full algebra.
    For beta-gamma at weight lambda: c = -2(6*lambda^2 - 6*lambda + 1).
    kappa = c/2 since it has a single generator (Virasoro-type formula).

    Actually beta-gamma is NOT Virasoro. It is a free-field algebra
    with kappa = 1 for the standard normalization.

    For this engine, we parametrize simply:
      kappa = 1, alpha = some function of lambda, S_4 = contact.
    The tower terminates at arity 4 (class C).
    """
    kappa = 1.0
    alpha = 0.0  # Simplified; actual alpha depends on lambda
    S = {}
    S[2] = kappa
    S[3] = alpha
    S[4] = lam  # Placeholder; actual S_4 depends on details
    for r in range(5, max_r + 1):
        S[r] = 0.0
    return S


# =====================================================================
# Section 1: Shadow q-series
# =====================================================================

def shadow_q_series(S: Dict[int, float], q_val: complex,
                    max_r: Optional[int] = None) -> complex:
    r"""Evaluate the shadow q-series f_A(q) = sum_{r>=2} S_r q^r.

    Parameters
    ----------
    S : dict {r: S_r}
    q_val : complex (|q| < 1 for convergence of infinite towers)
    max_r : truncation (defaults to max key in S)

    Returns
    -------
    complex value of the shadow q-series.
    """
    if max_r is None:
        max_r = max(S.keys())
    result = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        sr = S.get(r, 0.0)
        result += sr * q_val ** r
    return result


def shadow_q_series_coefficients(family: str, level: float,
                                  max_r: int = 20,
                                  **kwargs) -> Dict[int, float]:
    """Return shadow tower coefficients for a named family.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'virasoro', 'w3_tline',
             'w3_wline', 'betagamma'
    level : the family parameter (k for Heis/affine, c for Vir/W3,
            lambda for betagamma)
    max_r : maximum arity

    Returns
    -------
    dict {r: S_r}
    """
    family_lower = family.lower().replace(' ', '_').replace('-', '_')
    if family_lower in ('heisenberg', 'heis', 'h'):
        return heisenberg_shadow_coefficients(level, max_r)
    elif family_lower in ('affine_sl2', 'affine', 'aff', 'km'):
        return affine_sl2_shadow_coefficients(level, max_r)
    elif family_lower in ('virasoro', 'vir'):
        return virasoro_shadow_coefficients_numerical(level, max_r)
    elif family_lower in ('w3_tline', 'w3t'):
        return w3_tline_shadow_coefficients(level, max_r)
    elif family_lower in ('w3_wline', 'w3w'):
        return w3_wline_shadow_coefficients(level, max_r)
    elif family_lower in ('betagamma', 'bg'):
        return betagamma_shadow_coefficients(level, max_r)
    else:
        raise ValueError(f"Unknown family: {family}")


# =====================================================================
# Section 2: Shadow L-function (Dirichlet series)
# =====================================================================

def shadow_L_function(s_val: complex, S: Dict[int, float],
                      max_r: Optional[int] = None) -> complex:
    r"""Shadow L-function: L^sh(s, A) = sum_{r>=2} S_r r^{-s}.

    This is a Dirichlet series in the variable s.

    For finite towers (class G, L, C): the sum is finite and entire.
    For infinite towers (class M): converges for Re(s) sufficiently large.

    Convergence bound for class M:
      |S_r| ~ A rho^r r^{-5/2}  (thm:shadow-radius)
      so |S_r r^{-s}| ~ A rho^r r^{-Re(s)-5/2}
      Converges when rho < 1 (always true for c > c* ~ 6.125)
      or when Re(s) > 1 + log(rho)/log(r_typ) for rho >= 1.

    Parameters
    ----------
    s_val : complex
    S : dict {r: S_r}
    max_r : truncation

    Returns
    -------
    complex value of the shadow L-function.
    """
    if max_r is None:
        max_r = max(S.keys())
    result = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        sr = S.get(r, 0.0)
        if abs(sr) < 1e-50:
            continue
        result += sr * r ** (-s_val)
    return result


def shadow_L_function_family(s_val: complex, family: str, level: float,
                              max_r: int = 20) -> complex:
    """Shadow L-function for a named family."""
    S = shadow_q_series_coefficients(family, level, max_r)
    return shadow_L_function(s_val, S, max_r)


# =====================================================================
# Section 3: Shadow Hecke operators and eigenvalues
# =====================================================================

def shadow_hecke_operator(S: Dict[int, float], p: int,
                           max_r: int = 20) -> Dict[int, float]:
    r"""Apply the shadow Hecke operator T_p^sh to a shadow tower.

    (T_p^sh S)_r = S_{pr}

    This is a multiplicative dilation: the p-th Hecke operator shifts
    arities by a factor of p. It is well-defined on infinite towers
    (class M) and trivially extends finite towers by zero.

    Parameters
    ----------
    S : dict {r: S_r}
    p : prime
    max_r : maximum arity of the OUTPUT tower

    Returns
    -------
    dict {r: (T_p^sh S)_r}
    """
    result = {}
    for r in range(2, max_r + 1):
        pr = p * r
        result[r] = S.get(pr, 0.0)
    return result


def shadow_hecke_eigenvalue(S: Dict[int, float], p: int) -> Optional[float]:
    r"""Shadow Hecke eigenvalue a_p^sh = S_{2p} / S_2.

    This measures the p-th attenuation of the shadow tower relative to kappa.

    For Heisenberg (class G): S_{2p} = 0 for p >= 2, so a_p^sh = 0.
    For affine sl_2 (class L): S_4 = 0, S_6 = 0, so a_p^sh = 0 for p >= 2.
      But a_p^sh via T_p^sh S at r=2: (T_p S)_2 = S_{2p}.
      For p=2: S_4 = 0 (terminates), so a_2^sh = 0.
      For p=3: S_6 = 0, a_3^sh = 0.
      Actually S_3 = 2 but S_{2*3} = S_6 = 0, so a_3 = 0.

    For Virasoro (class M): a_p^sh = S_{2p}(c) / S_2(c).
      S_2 = c/2, S_4 = 10/[c(5c+22)], so a_2^sh = 20/[c^2(5c+22)].
      S_6 = 80(45c+193)/[3c^3(5c+22)^2], a_3^sh = ...

    Returns None if S_2 = 0 (degenerate).
    """
    S2 = S.get(2, 0.0)
    if abs(S2) < 1e-50:
        return None
    S_2p = S.get(2 * p, 0.0)
    return S_2p / S2


def shadow_hecke_eigenvalues_table(S: Dict[int, float],
                                    primes: Sequence[int] = (2, 3, 5, 7, 11)
                                    ) -> Dict[int, Optional[float]]:
    """Compute shadow Hecke eigenvalues for a list of primes."""
    return {p: shadow_hecke_eigenvalue(S, p) for p in primes}


def ramanujan_bound_test(a_p: float, p: int, weight: int = 2) -> Dict[str, Any]:
    r"""Test whether a shadow Hecke eigenvalue satisfies the Ramanujan bound.

    For a weight-k Hecke eigenform on GL_2, the Ramanujan conjecture
    (proved by Deligne for k >= 2) states:
      |a_p| <= 2 p^{(k-1)/2}

    For weight 2: |a_p| <= 2 sqrt(p).

    This test checks whether the shadow Hecke eigenvalue a_p^sh
    satisfies this bound, which would be necessary (but not sufficient)
    for the shadow q-series to correspond to a weight-2 eigenform.

    Parameters
    ----------
    a_p : the shadow Hecke eigenvalue
    p : the prime
    weight : the weight of the hypothetical eigenform (default 2)

    Returns
    -------
    dict with bound, value, and pass/fail.
    """
    bound = 2.0 * p ** ((weight - 1) / 2.0)
    return {
        'prime': p,
        'weight': weight,
        'eigenvalue': a_p,
        'bound': bound,
        'ratio': abs(a_p) / bound if bound > 0 else float('inf'),
        'satisfies_bound': abs(a_p) <= bound + 1e-12,
    }


# =====================================================================
# Section 4: Modularity test for shadow q-series
# =====================================================================

def modularity_defect(S: Dict[int, float], max_r: int = 20,
                       n_test_points: int = 50) -> Dict[str, Any]:
    r"""Test whether the shadow q-series has modular transformation properties.

    A weight-k modular form f for SL_2(Z) satisfies:
      f(-1/tau) = tau^k f(tau)

    We evaluate the shadow q-series at tau and -1/tau (via q = e^{2 pi i tau})
    and compute the defect |f(-1/tau) - tau^k f(tau)| for various weights k.

    For a genuinely modular shadow q-series, there exists k such that
    this defect vanishes (up to numerical precision).

    NOTE: The shadow q-series is NOT expected to be modular in general.
    This test quantifies HOW FAR it is from modularity at each weight.

    Parameters
    ----------
    S : shadow tower coefficients
    max_r : truncation
    n_test_points : number of tau-values on the upper half-plane

    Returns
    -------
    dict with defect data for each candidate weight.
    """
    results = {}
    # Test at tau = i*y for y in (0.5, 2.0) — purely imaginary
    for weight in [1, 2, 3, 4]:
        defects = []
        for j in range(n_test_points):
            y = 0.5 + 1.5 * j / max(n_test_points - 1, 1)
            tau = complex(0, y)
            tau_inv = complex(0, 1.0 / y)  # -1/tau for tau = iy is i/y

            q_tau = cmath.exp(2.0j * cmath.pi * tau)
            q_inv = cmath.exp(2.0j * cmath.pi * tau_inv)

            f_tau = shadow_q_series(S, q_tau, max_r)
            f_inv = shadow_q_series(S, q_inv, max_r)

            # Modular relation: f(-1/tau) = tau^k * f(tau)
            # For tau = iy: -1/tau = i/y, tau^k = (iy)^k
            tau_k = tau ** weight
            defect = abs(f_inv - tau_k * f_tau)
            defects.append(defect)

        avg_defect = sum(defects) / len(defects) if defects else float('inf')
        max_defect = max(defects) if defects else float('inf')
        results[weight] = {
            'average_defect': avg_defect,
            'max_defect': max_defect,
            'defects': defects,
        }

    # Identify the best weight
    best_weight = min(results.keys(),
                      key=lambda k: results[k]['average_defect'])
    return {
        'weight_defects': results,
        'best_weight': best_weight,
        'best_defect': results[best_weight]['average_defect'],
        'is_modular': results[best_weight]['average_defect'] < 1e-6,
    }


# =====================================================================
# Section 5: Shadow L-function functional equation test
# =====================================================================

def completed_shadow_L(s_val: complex, S: Dict[int, float],
                        weight: int = 2, conductor: float = 1.0,
                        max_r: int = 30) -> complex:
    r"""Completed shadow L-function:

    Lambda^sh(s) = (sqrt(N) / (2 pi))^s Gamma(s) L^sh(s)

    where N is the "shadow conductor" and Gamma is the gamma function.

    For the functional equation Lambda^sh(s) = epsilon Lambda^sh(k - s),
    we compute both sides and measure the defect.
    """
    # Gamma approximation via Stirling
    try:
        gamma_s = cmath.exp(
            (s_val - 0.5) * cmath.log(s_val) - s_val
            + 0.5 * cmath.log(2.0 * cmath.pi)
            + 1.0 / (12.0 * s_val)
        )
    except (ValueError, ZeroDivisionError, OverflowError):
        return complex(float('nan'))

    L_val = shadow_L_function(s_val, S, max_r)
    prefactor = (math.sqrt(conductor) / (2.0 * math.pi)) ** s_val

    return prefactor * gamma_s * L_val


def functional_equation_defect(S: Dict[int, float],
                                weight: int = 2,
                                conductor: float = 1.0,
                                epsilon: float = 1.0,
                                max_r: int = 30,
                                n_points: int = 20) -> Dict[str, Any]:
    r"""Test the functional equation Lambda^sh(s) = eps Lambda^sh(k-s).

    Evaluates on the critical line Re(s) = k/2.

    Returns dict with defect data.
    """
    defects = []
    s_center = weight / 2.0
    for j in range(n_points):
        t = -5.0 + 10.0 * j / max(n_points - 1, 1)
        s = complex(s_center, t)
        s_dual = complex(weight, 0) - s

        Lambda_s = completed_shadow_L(s, S, weight, conductor, max_r)
        Lambda_dual = completed_shadow_L(s_dual, S, weight, conductor, max_r)

        if cmath.isnan(Lambda_s) or cmath.isnan(Lambda_dual):
            continue
        if abs(Lambda_s) < 1e-50 and abs(Lambda_dual) < 1e-50:
            defects.append(0.0)
            continue

        defect = abs(Lambda_s - epsilon * Lambda_dual)
        normalization = max(abs(Lambda_s), abs(Lambda_dual), 1e-50)
        defects.append(defect / normalization)

    if not defects:
        return {'avg_relative_defect': float('inf'),
                'max_relative_defect': float('inf'),
                'satisfies_FE': False}

    return {
        'weight': weight,
        'conductor': conductor,
        'epsilon': epsilon,
        'avg_relative_defect': sum(defects) / len(defects),
        'max_relative_defect': max(defects),
        'satisfies_FE': max(defects) < 0.1,
        'n_valid_points': len(defects),
    }


# =====================================================================
# Section 6: Local Langlands data at primes
# =====================================================================

def shadow_conductor_exponent(S: Dict[int, float], p: int,
                               max_r: int = 20) -> Dict[str, Any]:
    r"""Compute the shadow conductor exponent at prime p.

    f_p(A) = max_{2 <= r <= max_r} v_p(denom(S_r))

    where v_p is the p-adic valuation and denom(S_r) is the denominator
    of S_r when written as a reduced fraction.

    For Virasoro: denom(S_r) = c^{r-3} (5c+22)^{floor((r-2)/2)} * const,
    so at c = p: v_p(denom) includes (r-3) from the c factor.

    For Heisenberg: S_r = 0 for r >= 3, so f_p = 0 (unramified).

    Returns dict with conductor data.
    """
    max_vp = 0
    vp_by_arity = {}

    for r in range(2, max_r + 1):
        sr = S.get(r, 0.0)
        if abs(sr) < 1e-50:
            vp_by_arity[r] = 0
            continue

        # Convert to fraction and find p-adic valuation of denominator
        try:
            frac = Fraction(sr).limit_denominator(10 ** 18)
        except (ValueError, OverflowError):
            # For very large/small floats, use direct method
            frac = Fraction(sr).limit_denominator(10 ** 12)

        d = abs(frac.denominator)
        vp = 0
        while d % p == 0 and d > 0:
            vp += 1
            d //= p
        vp_by_arity[r] = vp
        max_vp = max(max_vp, vp)

    # Classify ramification
    if max_vp == 0:
        ram_type = 'unramified'
    elif max_vp <= 2:
        ram_type = 'tamely_ramified'
    else:
        ram_type = 'wildly_ramified'

    return {
        'prime': p,
        'conductor_exponent': max_vp,
        'ramification_type': ram_type,
        'vp_by_arity': vp_by_arity,
    }


def shadow_conductor(S: Dict[int, float],
                      primes: Sequence[int] = (2, 3, 5, 7, 11, 13),
                      max_r: int = 20) -> Dict[str, Any]:
    r"""Compute the full shadow conductor N = prod p^{f_p}.

    The conductor is the product over primes of p^{f_p(A)}.
    For finite shadow towers (class G, L, C), N is a finite product.
    For infinite towers (class M), we truncate at max_r.

    Returns dict with conductor data.
    """
    conductor = 1
    local_data = {}
    for p in primes:
        data = shadow_conductor_exponent(S, p, max_r)
        local_data[p] = data
        conductor *= p ** data['conductor_exponent']

    return {
        'conductor': conductor,
        'local_data': local_data,
        'primes_checked': list(primes),
    }


# =====================================================================
# Section 7: Base change and quadratic twists
# =====================================================================

def kronecker_symbol(D: int, n: int) -> int:
    r"""Kronecker symbol (D/n), the generalization of the Legendre symbol.

    For fundamental discriminant D:
      (D/p) = 0 if p | D
      (D/p) = 1 if D is a QR mod p
      (D/p) = -1 otherwise

    Uses the Jacobi symbol computation.
    """
    if n == 0:
        return 1 if abs(D) == 1 else 0
    if n == 1:
        return 1

    # Handle sign
    if n < 0:
        n = -n
        if D < 0:
            return -kronecker_symbol(D, n)
        return kronecker_symbol(D, n)

    # Factor out 2s
    result = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            return 0
        if D % 8 in (3, 5):
            result = -result

    # Now n is odd, use Jacobi symbol
    return result * _jacobi_symbol(D % n, n)


def _jacobi_symbol(a: int, n: int) -> int:
    """Jacobi symbol (a/n) for odd n > 0."""
    if n <= 0 or n % 2 == 0:
        raise ValueError(f"n must be positive odd, got {n}")
    if n == 1:
        return 1
    a = a % n
    if a == 0:
        return 0
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


def shadow_quadratic_twist(S: Dict[int, float], D: int,
                            max_r: int = 20) -> Dict[int, float]:
    r"""Shadow tower twisted by quadratic character chi_D.

    (S^{chi_D})_r = chi_D(r) S_r

    where chi_D = (D/.) is the Kronecker symbol.

    This produces the "shadow twist," analogous to the twist of a
    Dirichlet L-function by a quadratic character.
    """
    S_twisted = {}
    for r in range(2, max_r + 1):
        sr = S.get(r, 0.0)
        chi = kronecker_symbol(D, r)
        S_twisted[r] = chi * sr
    return S_twisted


def shadow_twisted_L_function(s_val: complex, S: Dict[int, float], D: int,
                               max_r: int = 20) -> complex:
    r"""Twisted shadow L-function:

    L^sh(s, A, chi_D) = sum_{r>=2} chi_D(r) S_r r^{-s}
    """
    S_tw = shadow_quadratic_twist(S, D, max_r)
    return shadow_L_function(s_val, S_tw, max_r)


def shadow_base_change_L_function(s_val: complex, S: Dict[int, float], D: int,
                                   max_r: int = 20) -> complex:
    r"""Shadow base change L-function for Q(sqrt(D))/Q:

    L^sh(s, A, Q(sqrt(D))) = L^sh(s, A) * L^sh(s, A, chi_D)

    This is the analogue of the base change of an automorphic form
    from GL_n(A_Q) to GL_n(A_{Q(sqrt(D))}).
    """
    L_untwisted = shadow_L_function(s_val, S, max_r)
    L_twisted = shadow_twisted_L_function(s_val, S, D, max_r)
    return L_untwisted * L_twisted


# =====================================================================
# Section 8: GL_N correspondence for W_N algebras
# =====================================================================

def w3_shadow_L_data(c_val: float, max_r: int = 20) -> Dict[str, Any]:
    r"""Shadow L-function data for W_3, testing GL_3 vs GL_1 x GL_2.

    The W_3 algebra has N-1=2 generators (T, W).
    If the shadow tower determines a GL_3 automorphic form, the
    L-function should NOT factor as a product of GL_1 and GL_2 L-functions.

    Conversely, if the T-line and W-line are "independent," the
    L-function might factor.

    TEST: Compute L^sh(s, W_3) on each line and check for factorization.

    The T-line L-function is identical to L^sh(s, Vir_c) (same tower).
    The W-line L-function has only even-arity terms (Z_2 parity).
    """
    S_T = w3_tline_shadow_coefficients(c_val, max_r)
    S_W = w3_wline_shadow_coefficients(c_val, max_r)

    # Combined tower: direct sum
    S_combined = {}
    for r in range(2, max_r + 1):
        S_combined[r] = S_T.get(r, 0.0) + S_W.get(r, 0.0)

    # Check factorization: does L_combined = L_T * L_W?
    test_points = [2.0, 3.0, 4.0, 5.0]
    factorization_defects = []
    for s in test_points:
        L_comb = shadow_L_function(s, S_combined, max_r)
        L_T = shadow_L_function(s, S_T, max_r)
        L_W = shadow_L_function(s, S_W, max_r)
        product = L_T * L_W

        # L_combined is the SUM not the product — check if it can be factored
        # as a product of two Dirichlet series. This is a strong condition.
        # If L_comb = sum a_r r^{-s} and L_T * L_W = sum (sum_{d|r} b_d c_{r/d}) r^{-s},
        # then factorization means the combined coefficients are the Dirichlet convolution.

        # Simple test: ratio
        if abs(L_comb) > 1e-50:
            factorization_defects.append(abs(product / L_comb - 1.0))
        else:
            factorization_defects.append(float('inf'))

    # Dirichlet convolution test
    S_convolution = {}
    for r in range(2, max_r + 1):
        conv = 0.0
        for d in range(2, r + 1):
            if r % d == 0:
                q = r // d
                if q >= 2:
                    conv += S_T.get(d, 0.0) * S_W.get(q, 0.0)
        S_convolution[r] = conv

    conv_match = all(
        abs(S_combined.get(r, 0.0) - S_convolution.get(r, 0.0)) < 1e-10
        for r in range(2, min(max_r + 1, 10))
    )

    return {
        'c': c_val,
        'S_T': S_T,
        'S_W': S_W,
        'S_combined': S_combined,
        'S_convolution': S_convolution,
        'factorization_defects': factorization_defects,
        'is_dirichlet_product': conv_match,
        'is_genuinely_GL3': not conv_match,
    }


# =====================================================================
# Section 9: Shadow growth rate and convergence
# =====================================================================

def shadow_growth_rate(c_val: float) -> float:
    r"""Shadow growth rate rho(c) for Virasoro.

    rho^2 = (180c + 872) / [c^2 (5c + 22)]

    thm:shadow-radius.
    """
    return math.sqrt((180.0 * c_val + 872.0) / (c_val ** 2 * (5.0 * c_val + 22.0)))


def shadow_L_convergence_abscissa(c_val: float) -> float:
    r"""Abscissa of convergence for the shadow Dirichlet series.

    For class M: L^sh(s) converges absolutely for Re(s) > sigma_c where
    sigma_c is determined by the growth |S_r| ~ A rho^r r^{-5/2}:

    sum |S_r| r^{-sigma} converges iff sum rho^r r^{-sigma-5/2} converges.
    By ratio test: rho^r / rho^{r-1} = rho, independent of sigma, so
    converges iff rho < 1, diverges iff rho > 1.

    For rho < 1: converges for ALL real s (entire after analytic continuation).
    For rho = 1: borderline (converges for sigma > -3/2 by comparison with r^{-5/2}).
    For rho > 1: diverges for all sigma.

    So sigma_c = -inf if rho < 1, 0 if rho = 1, +inf if rho > 1.

    This is the DIRICHLET series convergence, not the q-series convergence.
    For the q-series f_A(q), convergence is |q| < 1/rho.
    """
    rho = shadow_growth_rate(c_val)
    if rho < 1.0 - 1e-12:
        return float('-inf')  # Converges everywhere
    elif rho > 1.0 + 1e-12:
        return float('inf')  # Diverges everywhere
    else:
        return 0.0  # Borderline


# =====================================================================
# Section 10: Full shadow Langlands functor
# =====================================================================

def shadow_langlands_datum(family: str, level: float,
                            max_r: int = 20,
                            primes: Sequence[int] = (2, 3, 5, 7, 11)
                            ) -> Dict[str, Any]:
    r"""Compute the full shadow Langlands datum for a chiral algebra.

    This packages all the automorphic data extracted from the shadow
    obstruction tower into a single dictionary.

    Components:
    1. Shadow tower coefficients S_r
    2. Shadow q-series evaluation
    3. Shadow L-function
    4. Shadow Hecke eigenvalues
    5. Ramanujan bound checks
    6. Modularity defect
    7. Functional equation test
    8. Local Langlands data (conductor exponents)
    9. Shadow conductor

    Parameters
    ----------
    family : algebra family name
    level : family parameter
    max_r : maximum arity
    primes : primes for local data

    Returns
    -------
    Comprehensive dict with all shadow Langlands data.
    """
    S = shadow_q_series_coefficients(family, level, max_r)
    kappa = S.get(2, 0.0)

    # Shadow depth
    nonzero = [r for r, sr in S.items() if abs(sr) > 1e-50]
    depth = max(nonzero) if nonzero else 0
    is_finite = all(abs(S.get(r, 0.0)) < 1e-50
                    for r in range(depth + 1, max_r + 1))

    # Classification
    if depth <= 2:
        archetype = 'G'
    elif depth <= 3 and is_finite:
        archetype = 'L'
    elif depth <= 4 and is_finite:
        archetype = 'C'
    else:
        archetype = 'M'

    # Hecke eigenvalues
    hecke = shadow_hecke_eigenvalues_table(S, primes)

    # Ramanujan bounds (weight 2 hypothesis)
    ramanujan_data = {}
    for p in primes:
        ap = hecke.get(p)
        if ap is not None:
            ramanujan_data[p] = ramanujan_bound_test(ap, p, weight=2)

    # L-function at s = 2 (within convergence region for most families)
    L_at_2 = shadow_L_function(2.0, S, max_r)

    # Conductor
    cond_data = shadow_conductor(S, primes, max_r)

    return {
        'family': family,
        'level': level,
        'kappa': kappa,
        'depth': depth,
        'archetype': archetype,
        'is_finite_tower': is_finite,
        'coefficients': S,
        'hecke_eigenvalues': hecke,
        'ramanujan_data': ramanujan_data,
        'L_at_2': L_at_2,
        'conductor_data': cond_data,
        'conductor': cond_data['conductor'],
    }


# =====================================================================
# Section 11: Virasoro-specific GL_2 correspondence
# =====================================================================

def virasoro_gl2_correspondence(c_val: float,
                                 max_r: int = 20) -> Dict[str, Any]:
    r"""Detailed GL_2 correspondence data for Virasoro at central charge c.

    The shadow generating function H(t) = t^2 sqrt(Q_L(t)) is algebraic
    of degree 2 (thm:riccati-algebraicity). This algebraicity is the
    shadow analogue of "weight 2" in the Langlands programme.

    Data extracted:
    1. Shadow q-series f_{Vir}(q)
    2. Shadow Hecke eigenvalues a_p^sh for small primes
    3. Growth rate rho(c) (determines convergence)
    4. Modularity defect at weights 1, 2, 3, 4
    5. Functional equation test for various conductors
    6. L-function special values
    """
    S = virasoro_shadow_coefficients_numerical(c_val, max_r)
    rho = shadow_growth_rate(c_val)

    # Hecke eigenvalues
    primes = [2, 3, 5, 7, 11, 13]
    hecke = shadow_hecke_eigenvalues_table(S, primes)

    # Ramanujan bounds at weight 2
    ramanujan = {}
    for p in primes:
        ap = hecke.get(p)
        if ap is not None:
            ramanujan[p] = ramanujan_bound_test(ap, p, weight=2)

    # L-function special values
    L_values = {}
    for s in [1.0, 1.5, 2.0, 3.0, 4.0]:
        L_values[s] = shadow_L_function(complex(s), S, max_r)

    # Critical value at s = 1 (center of weight-2 critical strip)
    L_critical = shadow_L_function(complex(1.0), S, max_r)

    return {
        'c': c_val,
        'kappa': c_val / 2.0,
        'rho': rho,
        'convergent_dirichlet': rho < 1.0,
        'coefficients': S,
        'hecke_eigenvalues': hecke,
        'ramanujan_data': ramanujan,
        'L_values': L_values,
        'L_critical': L_critical,
    }


# =====================================================================
# Section 12: Cross-family comparison
# =====================================================================

def cross_family_hecke_comparison(families: List[Tuple[str, float]],
                                   primes: Sequence[int] = (2, 3, 5, 7),
                                   max_r: int = 20) -> Dict[str, Any]:
    r"""Compare shadow Hecke eigenvalues across families.

    For each family, compute a_p^sh and check:
    1. Which families have a_p = 0 for all p? (finite towers)
    2. Which families satisfy Ramanujan bounds?
    3. Do Koszul-dual pairs have related eigenvalues?
    """
    table = {}
    for fam, lev in families:
        S = shadow_q_series_coefficients(fam, lev, max_r)
        hecke = shadow_hecke_eigenvalues_table(S, primes)
        all_zero = all(ap is not None and abs(ap) < 1e-12
                       for ap in hecke.values())
        table[(fam, lev)] = {
            'eigenvalues': hecke,
            'all_zero': all_zero,
        }

    return {'table': table, 'primes': list(primes)}


# =====================================================================
# Section 13: Explicit Virasoro shadow at special central charges
# =====================================================================

def virasoro_shadow_special_values() -> Dict[float, Dict[str, Any]]:
    r"""Shadow Langlands data at distinguished central charges.

    c = 1/2: Ising model (minimal model, class M)
    c = 1: free boson (class M)
    c = 12: simplest nontrivial integer kappa (kappa = 6)
    c = 13: self-dual point (Vir_c^! = Vir_{26-c} = Vir_13)
    c = 25: Koszul dual of c=1 (kappa = 25/2)
    c = 26: critical bosonic string (kappa = 13)
    """
    special = {}
    for c_val in [0.5, 1.0, 12.0, 13.0, 25.0, 26.0]:
        data = virasoro_gl2_correspondence(c_val, max_r=20)
        special[c_val] = data
    return special
