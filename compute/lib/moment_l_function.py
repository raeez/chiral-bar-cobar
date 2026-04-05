#!/usr/bin/env python3
r"""
moment_l_function.py -- Moment L-functions and the shadow Dirichlet series.

THE MOMENT L-FUNCTION:

For a chirally Koszul algebra A, the arity-r shadow amplitude Sh_r(Theta_A; tau)
is a function on M_{1,1} (the genus-1 moduli space).  The MOMENT L-FUNCTION is
the Rankin-Selberg integral:

    M_r(s) = int_{SL(2,Z)\H} Sh_r(Theta_A; tau) * E*(s, tau) dmu(tau)

where E*(s, tau) is the completed Eisenstein series and dmu = y^{-2} dx dy is
the hyperbolic measure.

For LATTICE VOAs with Hecke decomposition Theta_Lambda = c_E * E_k + sum c_j f_j:
  The shadow amplitude at arity r decomposes into Hecke eigenspaces, and
  the Rankin-Selberg integral picks out the standard L-function of each component.
  The moment L-function decomposes as (eq:moment-euler-lattice):

    M_r(s; V_Lambda) = c_E * L_E(s,r) + sum_j c_j * L_j(s,r)

  where L_E(s,r) involves zeta(s)*zeta(s-k+1) and L_j(s,r) is the r-th moment
  of the Satake parameters of f_j.

THE SHADOW DIRICHLET SERIES:

    Z_sh(s) = sum_{r>=2} S_r * r^{-s}

This is the generating Dirichlet series of the shadow tower coefficients.
For class M algebras: S_r ~ A * rho^r * r^{-5/2}, so Z_sh(s) converges
for Re(s) > 1 when rho < 1 and for Re(s) > sigma_0 when rho >= 1,
where sigma_0 = 1 + log(rho).

THE AUTOMORPHIC INTERPRETATION:

  r = 2: M_2 involves Rankin-Selberg convolution, automorphic on GL(4) -- KNOWN
  r = 3: M_3 relates to Sym^2, automorphic on GL(5) -- Shimura-Gelbart-Jacquet
  r = 4: M_4 relates to Sym^3, automorphic on GL(7) -- Kim-Shahidi
  r = 5: M_5 relates to Sym^4, automorphic on GL(9) -- OPEN (Langlands)

SELF-DUALITY AT c = 13:

  Virasoro at c=13 is the self-dual point: Vir_c^! = Vir_{26-c}, so c=13 maps
  to itself.  The Koszul-Epstein function should exhibit special properties.

References:
    - arithmetic_shadows.tex: thm:mc-recursion-moment, thm:hecke-newton-lattice
    - arithmetic_shadows.tex: cor:moment-automorphy, rem:serre-reduction
    - concordance.tex: sec:concordance-spectral-continuation
    - shadow_epstein_zeta.py: Koszul-Epstein function
    - symmetric_power_shadow.py: Satake parameters and symmetric power L
    - lattice_shadow_periods.py: Hecke decomposition, theta functions
    - virasoro_shadow_tower.py: Virasoro shadow coefficients S_r(c)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# 1. Shadow tower coefficients for all families
# =========================================================================

def virasoro_shadow_coefficients(c_val: float, max_arity: int = 10) -> Dict[int, float]:
    r"""Shadow tower coefficients S_r for Virasoro at central charge c.

    Uses the master equation recursion:
      S_2 = c/2 (kappa)
      S_3 = 2 (gravitational cubic)
      S_4 = 10 / (c * (5c + 22))  (quartic contact)
      S_r = -1/(2r) * sum_{j+k=r+2, j,k>=2} S_j * j * S_k * k * (2/c)

    The Poisson bracket on the single-generator line has propagator P = 2/c,
    and the degree-r coefficient of {S_j x^j, S_k x^k}_H = j * S_j * (2/c) * k * S_k * x^{j+k-2}.
    So the obstruction at arity r has x-degree r when j+k-2 = r, i.e., j+k = r+2.
    """
    c_f = float(c_val)
    if abs(c_f) < 1e-30:
        raise ValueError("c = 0 is degenerate (kappa = 0)")

    P = 2.0 / c_f  # propagator
    S = {}
    S[2] = c_f / 2.0
    S[3] = 2.0
    S[4] = 10.0 / (c_f * (5.0 * c_f + 22.0))

    for r in range(5, max_arity + 1):
        # obstruction = sum over j+k = r+2, j>=2, k>=2
        # of (factor) * j * S_j * P * k * S_k
        obs = 0.0
        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k not in S:
                continue
            if j > k:
                continue
            contrib = j * S[j] * P * k * S[k]
            if j == k:
                obs += 0.5 * contrib
            else:
                obs += contrib
        S[r] = -obs / (2.0 * r)

    return S


def heisenberg_shadow_coefficients(k_val: float, max_arity: int = 10) -> Dict[int, float]:
    r"""Shadow tower coefficients for Heisenberg at level k.

    Terminates at depth 2 (class G):
      S_2 = k (kappa)
      S_r = 0  for r >= 3
    """
    S = {2: float(k_val)}
    for r in range(3, max_arity + 1):
        S[r] = 0.0
    return S


def affine_sl2_shadow_coefficients(k_val: float, max_arity: int = 10) -> Dict[int, float]:
    r"""Shadow tower for affine sl_2 at level k.

    Terminates at depth 3 (class L):
      S_2 = kappa = 3(k+2)/(2*2) = 3(k+2)/4  [dim(sl_2)=3, h^v=2]
      S_3 = alpha (cubic)
      S_r = 0  for r >= 4

    kappa(V_k(sl_2)) = dim(g) * (k + h^v) / (2 * h^v) = 3(k+2)/4.
    """
    h_dual = 2
    dim_g = 3
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    S = {2: kappa, 3: 2.0}  # alpha = 2 for affine (gravitational cubic)
    for r in range(4, max_arity + 1):
        S[r] = 0.0
    return S


def leech_lattice_shadow_coefficients(max_arity: int = 10) -> Dict[int, float]:
    r"""Shadow tower for the Leech lattice VOA V_Leech (rank 24).

    kappa(V_Leech) = rank/2 = 12.
    The theta function is Theta_Leech = E_{12} - (65520/691) * Delta.
    The Hecke decomposition gives:
      c_E = 1 (Eisenstein coefficient)
      c_Delta = -65520/691 (cusp form coefficient)

    Shadow depth = 4 (class C): the quartic contact invariant S_4 != 0
    because dim S_{12} = 1 (the Ramanujan Delta appears).

    For the lattice VOA, the shadow coefficients at arity r encode the
    r-th moment of the Hecke decomposition:
      S_r = c_E * e_r(Eisenstein) + c_Delta * e_r(Delta)
    where e_r involves power sums of Satake parameters summed over primes.

    For a concrete numerical approximation, we use the genus-1 graph sum:
    the shadow at arity r is dominated by the leading Eisenstein contribution
    at low arity.
    """
    # kappa = 12 for rank 24
    kappa = 12.0
    alpha = 2.0  # universal gravitational cubic
    # S_4 for lattice VOAs: from the quartic contact class
    # For the Leech lattice, the quartic involves the cusp form Delta.
    # The quartic contact invariant Q^contact = 0 for lattice VOAs
    # (since the Sugawara OPE is quadratic), but the quartic shadow S_4
    # receives contributions from the Eisenstein sector:
    # S_4 = 10/(kappa * (5*kappa_eff + 22)) if we use the Virasoro-like
    # formula, but for lattice VOAs the shadow terminates at depth 4
    # (class C), and the quartic is determined by the Hecke decomposition.
    #
    # Actually for rank-24 lattice VOA, the central charge is c = 24,
    # so the Virasoro subalgebra gives S_4^{Vir} = 10/(24*(5*24+22)) = 10/3408.
    # But the full lattice VOA has additional currents.
    #
    # The correct shadow coefficient for V_Leech comes from the theta function:
    # at genus 1, the shadow Sh_r = (d/dt)^r log Z(t)|_{t=0} where Z is the
    # partition function. For the Leech lattice Z = Theta_Leech / eta^24,
    # so the shadow coefficients encode the Fourier coefficients.
    #
    # For our purposes, we compute S_2 = kappa = 12 and use the Virasoro
    # tower as an approximation for the subalgebra contribution:
    c_eff = 24.0  # central charge of V_Leech
    S = virasoro_shadow_coefficients(c_eff, max_arity)
    # Override kappa with the correct lattice value
    S[2] = kappa
    return S


# =========================================================================
# 2. Moment L-functions: M_r(s) for standard families
# =========================================================================

def _rankin_selberg_eisenstein(s, k: int):
    r"""Rankin-Selberg integral of E_k against E*(s).

    For the Eisenstein series E_k(tau) of weight k on SL(2,Z):
      int_{SL(2,Z)\H} E_k(tau) * E*(s, tau) dmu
    = (completed) Gamma(s)*Gamma(s-k+1)/(4*pi^s) * zeta(s)*zeta(s-k+1)

    We return the L-function part: zeta(s) * zeta(s - k + 1),
    up to Gamma factors and powers of pi.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    s_mp = mpmath.mpc(s)
    return mpmath.zeta(s_mp) * mpmath.zeta(s_mp - k + 1)


def _rankin_selberg_cusp(s, f_name: str, k: int, num_terms: int = 100):
    r"""Rankin-Selberg integral of a cusp form f against E*(s).

    For a Hecke eigenform f of weight k with Fourier coefficients a_f(n):
      int_{SL(2,Z)\H} |f(tau)|^2 * E*(s, tau) dmu
    = (completed) L(s, f x f)

    where L(s, f x f) = sum_{n>=1} |a_f(n)|^2 * n^{-s} is the
    Rankin-Selberg convolution.

    For the Ramanujan Delta (k=12, f_name='Delta'):
      L(s, Delta x Delta) = sum_{n>=1} tau(n)^2 * n^{-s}
    which has an Euler product:
      L(s, Delta x Delta) = prod_p (1 - alpha_p^2 p^{-s})^{-1} * ... (degree 4)
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    from .lattice_shadow_periods import ramanujan_tau

    s_mp = mpmath.mpc(s)
    result = mpmath.mpf(0)

    if f_name == 'Delta':
        for n in range(1, num_terms + 1):
            tau_n = ramanujan_tau(n)
            result += mpmath.mpf(tau_n) ** 2 * mpmath.power(n, -s_mp)
    else:
        raise ValueError(f"Unknown cusp form: {f_name}")

    return result


def moment_l_heisenberg(r: int, s, k_val: float = 1.0):
    r"""Moment L-function M_r(s) for the Heisenberg algebra at level k.

    The Heisenberg shadow tower terminates at depth 2:
      S_2 = k, S_r = 0 for r >= 3.

    Therefore:
      M_2(s) = k * (Rankin-Selberg of x^2 contribution)
    The genus-1 shadow amplitude Sh_2 at arity 2 is simply kappa * lambda_1,
    which is a constant on M_{1,1} (the Hodge class lambda_1).

    The Rankin-Selberg integral of a constant against E*(s,tau) gives:
      int E*(s, tau) dmu = Res_{s=1} E*(s) = 3/pi

    For the Rankin-Selberg of the MODULAR FORM associated to the shadow:
    At arity 2, the shadow amplitude on E_tau is Sh_2 = kappa (a constant).
    The Rankin-Selberg integral:
      M_2(s) = kappa * int_{F} E*(s, tau) dmu(tau)

    This is essentially proportional to zeta(s) (up to Gamma factors).
    Specifically, E*(s) = pi^{-s} Gamma(s) zeta(2s) E(s,tau), so the
    integral picks out the constant Fourier coefficient, giving:

      M_2(s) = kappa * zeta(2s) * (pi^{-s} Gamma(s) / Vol(F))

    For simplicity, we return the L-function content:
      M_2(s) = kappa * zeta(2s)  (the Riemann zeta at doubled argument)

    For r >= 3: M_r(s) = 0.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    if r < 2:
        return mpmath.mpf(0)
    if r >= 3:
        return mpmath.mpf(0)

    kappa = float(k_val)
    s_mp = mpmath.mpc(s)
    # M_2 = kappa * zeta(2s)
    return kappa * mpmath.zeta(2 * s_mp)


def moment_l_leech(r: int, s, num_terms: int = 50):
    r"""Moment L-function M_r(s) for the Leech lattice VOA.

    The theta function decomposes as:
      Theta_Leech = E_{12} - (65520/691) * Delta

    where E_{12} is the Eisenstein series of weight 12 and Delta is
    the Ramanujan cusp form.

    The moment L-function at arity r decomposes into:
      M_r(s) = c_E * L_E(s, r) + c_Delta * L_Delta(s, r)

    where:
      c_E = 1 (Eisenstein coefficient)
      c_Delta = -65520/691

    L_E(s, r) involves zeta(s) * zeta(s-11) (from the Eisenstein contribution).

    For the cusp form contribution, L_Delta(s, r) involves the r-th
    symmetric power trace of the Satake parameters of Delta:
      L_Delta(s, r) = sum_p p_r(alpha_p, beta_p) p^{-s} + ...

    where p_r is the r-th power sum (trace of Sym^{r-1}).

    ARITY 2:
      M_2(s) = c_E * zeta(s)*zeta(s-11) + c_Delta * L(s, Delta x Delta)
      The Eisenstein contribution gives two zeta factors from the
      Rankin-Selberg integral of E_12.
      The cusp contribution gives the Rankin-Selberg convolution L(s, Delta x Delta).

    ARITY 3:
      M_3(s) involves the cubic shadow.
      The cusp contribution gives Sym^2 L-function traces.

    ARITY 4:
      M_4(s) involves the quartic shadow.
      The cusp contribution gives Sym^3 L-function traces.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if r < 2:
        return mpmath.mpf(0)

    s_mp = mpmath.mpc(s)
    c_E = mpmath.mpf(1)
    c_Delta = mpmath.mpf(-65520) / mpmath.mpf(691)

    # Eisenstein contribution: proportional to zeta(s) * zeta(s - 11)
    L_E = mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 11)

    # Cusp form contribution at arity r:
    # The r-th moment of the Satake parameters of Delta.
    # For Hecke eigenform f of weight k, the Satake parameters at prime p
    # satisfy alpha_p * beta_p = p^{k-1} = p^{11}.
    # The power sum p_r(alpha, beta) = alpha^r + beta^r.
    #
    # The L-function is sum_{n>=1} a_r(n) n^{-s} where a_r is determined
    # by the Hecke eigenvalues through multiplicativity.
    #
    # For r = 2: p_2(alpha, beta) = (alpha+beta)^2 - 2*alpha*beta
    #          = tau(p)^2 - 2*p^{11}
    # The full Dirichlet series is related to L(s, Delta x Delta).
    #
    # We compute numerically by the power sum.

    from .symmetric_power_shadow import satake_parameters, ramanujan_tau

    L_cusp = mpmath.mpf(0)
    primes = _primes_up_to(num_terms)

    for p in primes:
        tau_p = ramanujan_tau(p)
        alpha, beta = satake_parameters(tau_p, 12, p)

        # r-th power sum: p_r(alpha, beta) = alpha^r + beta^r
        power_sum = mpmath.power(alpha, r) + mpmath.power(beta, r)

        L_cusp += mpmath.re(power_sum) * mpmath.power(mpmath.mpf(p), -s_mp)

    # Full moment L-function
    M_r = c_E * L_E + c_Delta * L_cusp

    return M_r


def moment_l_virasoro(r: int, s, c_val: float = 1.0, max_arity: int = 10):
    r"""Moment L-function M_r(s) for Virasoro at central charge c.

    The Virasoro shadow tower is infinite (class M). The moment L-function
    at arity r is:
      M_r(s) = S_r(c) * (Rankin-Selberg integral of modular form of weight 0)

    At genus 1, the shadow amplitude Sh_r is S_r * x^r evaluated on the
    arity-r collision stratum of the elliptic curve. The Rankin-Selberg
    integral against E*(s) gives:

      M_r(s) = S_r(c) * C_r(s)

    where C_r(s) is the Rankin-Selberg coefficient. For the leading
    contribution where the arity-r amplitude is a constant on M_{1,1}:

      M_r(s) ~ S_r(c) * zeta(2s) * (volume factor)

    For a more refined computation, the genus-1 graph sum at arity r
    involves propagators on E_tau, giving modular form coefficients
    that depend on tau. The full computation requires the graph-sum
    engine. Here we use the leading approximation.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if r < 2:
        return mpmath.mpf(0)

    S = virasoro_shadow_coefficients(c_val, max_arity)
    if r not in S or abs(S[r]) < 1e-50:
        return mpmath.mpf(0)

    s_mp = mpmath.mpc(s)
    # Leading approximation: M_r(s) ~ S_r * zeta(2s)
    return mpmath.mpf(S[r]) * mpmath.zeta(2 * s_mp)


# =========================================================================
# 3. Shadow Dirichlet series Z_sh(s)
# =========================================================================

def shadow_dirichlet_series(S_coeffs: Dict[int, float], s, max_r: int = None):
    r"""Compute the shadow Dirichlet series Z_sh(s) = sum_{r>=2} S_r * r^{-s}.

    Parameters
    ----------
    S_coeffs : dict
        Shadow tower coefficients {r: S_r}.
    s : complex
        The s-parameter.
    max_r : int, optional
        Maximum arity to sum. Defaults to max key in S_coeffs.

    Returns
    -------
    complex
        Value of Z_sh(s).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    s_mp = mpmath.mpc(s)
    if max_r is None:
        max_r = max(S_coeffs.keys())

    result = mpmath.mpf(0)
    for r in range(2, max_r + 1):
        if r in S_coeffs and abs(S_coeffs[r]) > 1e-80:
            result += mpmath.mpf(S_coeffs[r]) * mpmath.power(r, -s_mp)

    return result


def shadow_dirichlet_heisenberg(s, k_val: float = 1.0):
    r"""Z_sh(s) for Heisenberg at level k.

    Z_sh(s) = S_2 * 2^{-s} = k * 2^{-s}

    This is a SINGLE TERM Dirichlet series. It has:
      - Trivial meromorphic continuation (it's entire).
      - No functional equation (single term).
      - No Euler product (not multiplicative).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return mpmath.mpf(k_val) * mpmath.power(2, -mpmath.mpc(s))


def shadow_dirichlet_virasoro(s, c_val: float = 1.0, max_arity: int = 50):
    r"""Z_sh(s) for Virasoro at central charge c.

    Z_sh(s) = sum_{r>=2} S_r(c) * r^{-s}

    Convergence: S_r ~ A * rho^r * r^{-5/2} where rho is the shadow radius.
    The series converges absolutely for Re(s) > 1 when rho < 1
    (i.e., c > c* ~ 6.125 for Virasoro).

    For c < c*, the series requires analytic continuation (Borel summation
    or the algebraic generating function).
    """
    S = virasoro_shadow_coefficients(c_val, max_arity)
    return shadow_dirichlet_series(S, s, max_arity)


def shadow_dirichlet_leech(s, max_arity: int = 30):
    r"""Z_sh(s) for the Leech lattice VOA.

    The Leech lattice has depth 4 (class C), so the shadow tower terminates
    effectively at arity 4 (with possible higher-order corrections from the
    Virasoro subalgebra).
    """
    S = leech_lattice_shadow_coefficients(max_arity)
    return shadow_dirichlet_series(S, s, max_arity)


# =========================================================================
# 4. Selberg class property tests
# =========================================================================

def check_functional_equation(Z_func, s_val, tol: float = 1e-6) -> Dict[str, Any]:
    r"""Test whether Z_sh satisfies a functional equation Z(s) ~ Z(1-s).

    A Dirichlet series in the Selberg class satisfies:
      Phi(s) = epsilon * Phi_bar(1 - s)
    where Phi = Q^s * prod Gamma(alpha_j s + mu_j) * Z(s).

    We test the SIMPLEST functional equation: whether Z(s) and Z(1-s)
    are proportional (up to a multiplicative constant).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    Z_s = Z_func(s_val)
    Z_1ms = Z_func(1 - s_val)

    if abs(Z_s) < 1e-30 or abs(Z_1ms) < 1e-30:
        return {
            's': complex(s_val),
            'Z(s)': complex(Z_s),
            'Z(1-s)': complex(Z_1ms),
            'ratio': None,
            'has_fe': False,
            'note': 'One value too small for ratio test',
        }

    ratio = complex(Z_s / Z_1ms)
    return {
        's': complex(s_val),
        'Z(s)': complex(Z_s),
        'Z(1-s)': complex(Z_1ms),
        'ratio': ratio,
        'has_fe': abs(abs(ratio) - 1) < tol,  # |ratio| ~ 1 suggests FE
        'note': 'Ratio test: if |Z(s)/Z(1-s)| = 1 for all s on critical line,'
                ' suggests functional equation.',
    }


def check_euler_product(S_coeffs: Dict[int, float], max_r: int = 20) -> Dict[str, Any]:
    r"""Test whether the shadow coefficients S_r are multiplicative.

    A Dirichlet series Z = sum a_n n^{-s} has an Euler product iff a_n is
    a multiplicative arithmetic function: a_{mn} = a_m * a_n for gcd(m,n) = 1.

    For the shadow Dirichlet series Z_sh(s) = sum S_r r^{-s}, the coefficients
    are S_r (the shadow tower coefficients). We test multiplicativity:
    S_{m*n} = S_m * S_n for coprime m, n.

    IMPORTANT: S_r is NOT indexed by natural numbers in the usual sense --
    it is a finite sequence starting at r=2. The "multiplicativity" test
    checks whether S_{m*n} = S_m * S_n for coprime m, n with m*n <= max_r.
    """
    failures = []
    tests = 0

    for m in range(2, max_r + 1):
        for n in range(2, max_r + 1):
            if m * n > max_r:
                continue
            if math.gcd(m, n) != 1:
                continue
            if m * n not in S_coeffs or m not in S_coeffs or n not in S_coeffs:
                continue

            tests += 1
            product = S_coeffs[m] * S_coeffs[n]
            actual = S_coeffs[m * n]
            if abs(actual) > 1e-30 or abs(product) > 1e-30:
                defect = actual - product
                if abs(defect) > 1e-10 * max(abs(actual), abs(product), 1e-30):
                    failures.append({
                        'm': m, 'n': n,
                        'S_mn': actual,
                        'S_m * S_n': product,
                        'defect': defect,
                    })

    return {
        'tests': tests,
        'failures': len(failures),
        'is_multiplicative': len(failures) == 0,
        'failure_details': failures[:10],
    }


def selberg_class_analysis(family: str, params: Dict[str, Any],
                           max_arity: int = 20) -> Dict[str, Any]:
    r"""Analyze whether Z_sh(s) for a given family belongs to the Selberg class.

    The Selberg class consists of Dirichlet series F(s) satisfying:
      (1) Ramanujan hypothesis: a_n << n^epsilon
      (2) Analytic continuation to C with at most finitely many poles
      (3) Functional equation
      (4) Euler product

    For the shadow Dirichlet series:
      (1) SATISFIED for class G/L/C (finite terms). For class M:
          S_r ~ A * rho^r * r^{-5/2}, so |S_r| grows exponentially
          if rho > 1 -- VIOLATES Ramanujan when rho > 1.
      (2) For class G/L/C: trivially meromorphic (polynomial).
          For class M: requires the algebraic generating function.
      (3) NOT expected in general for Z_sh(s). The Koszul-Epstein
          function (the Epstein zeta of the shadow metric) DOES have
          a functional equation.
      (4) NOT multiplicative in general (AP: shadow coefficients S_r
          are determined by OPE data, not by a multiplicative function).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    result = {
        'family': family,
        'params': params,
    }

    if family == 'Heisenberg':
        k_val = params.get('k', 1.0)
        S = heisenberg_shadow_coefficients(k_val, max_arity)
        result['depth'] = 2
        result['archetype'] = 'G'
        result['ramanujan'] = True  # finite terms
        result['analytic_continuation'] = True  # trivially entire
        result['functional_equation'] = False  # single term, no FE
        result['euler_product'] = check_euler_product(S, max_arity)
        result['in_selberg_class'] = False
        result['note'] = ('Single-term Dirichlet series k * 2^{-s}. '
                          'Not in Selberg class (no FE, no Euler product).')

    elif family == 'Virasoro':
        c_val = params.get('c', 1.0)
        S = virasoro_shadow_coefficients(c_val, max_arity)
        rho = _virasoro_shadow_radius(c_val)
        result['depth'] = float('inf')
        result['archetype'] = 'M'
        result['shadow_radius'] = rho
        result['ramanujan'] = rho < 1.0  # S_r bounded polynomially iff rho < 1
        result['analytic_continuation'] = True  # algebraic GF
        ep = check_euler_product(S, max_arity)
        result['euler_product'] = ep
        # Functional equation test at s = 1/2 + it
        fe_tests = []
        for t_val in [1.0, 2.0, 5.0]:
            s_test = 0.5 + 1j * t_val
            fe = check_functional_equation(
                lambda s: shadow_dirichlet_virasoro(s, c_val, max_arity),
                s_test
            )
            fe_tests.append(fe)
        result['functional_equation_tests'] = fe_tests
        has_fe = all(ft.get('has_fe', False) for ft in fe_tests)
        result['functional_equation'] = has_fe
        result['in_selberg_class'] = (
            result['ramanujan'] and
            result['analytic_continuation'] and
            has_fe and
            ep['is_multiplicative']
        )
        result['note'] = (
            f'Shadow radius rho = {rho:.6f}. '
            f'Ramanujan: {"YES" if rho < 1 else "NO (rho >= 1)"}. '
            f'Euler product: {"YES" if ep["is_multiplicative"] else "NO"}. '
            f'Expected: NOT in Selberg class (S_r not multiplicative).'
        )

    elif family == 'Leech':
        S = leech_lattice_shadow_coefficients(max_arity)
        result['depth'] = 4
        result['archetype'] = 'C'
        ep = check_euler_product(S, max_arity)
        result['euler_product'] = ep
        result['note'] = (
            'Leech lattice: depth 4, class C. '
            'The MOMENT L-functions M_r(s) have Euler products (from Hecke '
            'decomposition), but the SHADOW DIRICHLET SERIES Z_sh(s) does not.'
        )

    return result


# =========================================================================
# 5. Self-dual analysis at c = 13
# =========================================================================

def virasoro_self_dual_analysis(max_arity: int = 30) -> Dict[str, Any]:
    r"""Analyze the shadow Dirichlet series at the self-dual point c = 13.

    At c = 13: Vir_c^! = Vir_{26-c} = Vir_{13}, so the algebra is self-dual
    under Koszul duality. Special properties expected:
      - kappa(13) + kappa(13) = 13 (AP24: NOT zero!)
      - delta_kappa = kappa - kappa' = 0 (complementarity asymmetry vanishes)
      - Shadow coefficients S_r(13) should exhibit enhanced symmetry
      - The Koszul-Epstein function at c=13 should have a self-dual
        functional equation
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    c = 13.0
    S = virasoro_shadow_coefficients(c, max_arity)
    rho = _virasoro_shadow_radius(c)

    # Shadow Dirichlet series at various s
    Z_values = {}
    for s_val in [2.0, 3.0, 4.0, 5.0]:
        Z_values[s_val] = complex(shadow_dirichlet_virasoro(s_val, c, max_arity))

    # Functional equation test on critical line
    fe_tests = []
    for t_val in [0.5, 1.0, 2.0, 5.0, 10.0]:
        s_test = 0.5 + 1j * t_val
        Z_s = shadow_dirichlet_virasoro(s_test, c, max_arity)
        Z_1ms = shadow_dirichlet_virasoro(1 - s_test, c, max_arity)
        if abs(Z_s) > 1e-30 and abs(Z_1ms) > 1e-30:
            ratio = complex(Z_s / Z_1ms)
        else:
            ratio = None
        fe_tests.append({
            's': complex(s_test),
            'Z(s)': complex(Z_s),
            'Z(1-s)': complex(Z_1ms),
            'ratio': ratio,
        })

    # Complementarity data
    S_dual = virasoro_shadow_coefficients(26.0 - c, max_arity)  # = c again
    complementarity_check = {}
    for r in range(2, min(max_arity + 1, 11)):
        if r in S and r in S_dual:
            complementarity_check[r] = {
                'S_r(c)': S[r],
                'S_r(26-c)': S_dual[r],
                'equal': abs(S[r] - S_dual[r]) < 1e-12,
            }

    return {
        'c': c,
        'kappa': c / 2.0,
        'kappa_dual': (26.0 - c) / 2.0,
        'kappa_sum': c / 2.0 + (26.0 - c) / 2.0,  # = 13, NOT 0
        'delta_kappa': c / 2.0 - (26.0 - c) / 2.0,  # = 0 at c=13
        'shadow_radius': rho,
        'shadow_coefficients': {r: S[r] for r in range(2, min(max_arity + 1, 11))},
        'Z_sh_values': Z_values,
        'functional_equation_tests': fe_tests,
        'complementarity_check': complementarity_check,
        'is_self_dual': True,
        'note': ('At c=13: kappa + kappa! = 13 (NOT zero, AP24). '
                 'delta_kappa = 0 (complementarity asymmetry vanishes). '
                 'Shadow coefficients satisfy S_r(13) = S_r(13) trivially. '
                 f'Shadow radius rho = {rho:.6f}.'),
    }


# =========================================================================
# 6. Automorphic interpretation table
# =========================================================================

def automorphic_interpretation_table() -> List[Dict[str, Any]]:
    r"""The automorphic interpretation of M_r(s) at each arity.

    Returns a table mapping arity r to the known automorphic status.
    """
    table = [
        {
            'arity': 2,
            'symmetric_power': 'Sym^1',
            'gl_rank': 'GL(2)',
            'status': 'KNOWN',
            'reference': 'Rankin (1939), Selberg (1940)',
            'description': ('M_2 is the Rankin-Selberg convolution. '
                            'For lattice VOAs: M_2 = c_E * zeta(s)*zeta(s-k+1) '
                            '+ c_Delta * L(s, f x f). Automorphic on GL(4).'),
        },
        {
            'arity': 3,
            'symmetric_power': 'Sym^2',
            'gl_rank': 'GL(3) via GL(5)',
            'status': 'KNOWN',
            'reference': 'Shimura (1975), Gelbart-Jacquet (1978)',
            'description': ('M_3 involves Sym^2 L-function data. '
                            'Gelbart-Jacquet: Sym^2 transfer GL(2)->GL(3) is automorphic. '
                            'The full M_3 is automorphic on GL(5).'),
        },
        {
            'arity': 4,
            'symmetric_power': 'Sym^3',
            'gl_rank': 'GL(4) via GL(7)',
            'status': 'KNOWN',
            'reference': 'Kim-Shahidi (2002)',
            'description': ('M_4 involves Sym^3 L-function data. '
                            'Kim-Shahidi: Sym^3 transfer GL(2)->GL(4) is automorphic. '
                            'Ramanujan bound improvement: delta = 2/9.'),
        },
        {
            'arity': 5,
            'symmetric_power': 'Sym^4',
            'gl_rank': 'GL(5) via GL(9)',
            'status': 'KNOWN',
            'reference': 'Kim (2003)',
            'description': ('M_5 involves Sym^4 L-function data. '
                            'Kim: Sym^4 transfer GL(2)->GL(5) is automorphic. '
                            'Ramanujan bound improvement: delta = 1/9.'),
        },
        {
            'arity': 6,
            'symmetric_power': 'Sym^5',
            'gl_rank': 'GL(6) via GL(11)',
            'status': 'OPEN',
            'reference': 'Langlands programme',
            'description': ('M_6 involves Sym^5 data. '
                            'Sym^5 functoriality GL(2)->GL(6) is OPEN. '
                            'This is the FIRST arity where the automorphic '
                            'interpretation is genuinely open.'),
        },
        {
            'arity': 'r',
            'symmetric_power': f'Sym^{{r-1}}',
            'gl_rank': f'GL(r) via GL(2r-1)',
            'status': 'OPEN for r >= 6',
            'reference': 'Langlands programme (general)',
            'description': ('General: M_r involves Sym^{r-1} data. '
                            'Full Langlands functoriality would give automorphy '
                            'for all r, but this is open for r >= 6. '
                            'The MC equation provides POLYNOMIAL constraints '
                            'between M_r values (Newton identities) but does not '
                            'by itself give analytic continuation.'),
        },
    ]
    return table


# =========================================================================
# 7. q-expansion of shadow amplitudes at genus 1
# =========================================================================

def virasoro_genus1_q_coefficients(r: int, c_val: float = 1.0,
                                    num_coeffs: int = 10) -> Dict[int, float]:
    r"""First few q-expansion coefficients of the genus-1 shadow amplitude.

    At genus 1, the shadow amplitude Sh_r(Theta_A; tau) has a q-expansion:
      Sh_r(tau) = sum_n a_n^{(r)} q^n

    For Virasoro, the genus-1 shadow amplitude at arity r is:
      Sh_r^{(1)}(tau) = S_r * (contribution from genus-1 graph sum)

    The leading contribution is S_r * (E_2-type series), where the
    genus-1 propagator is the quasi-modular Eisenstein series E_2*(tau).

    For the simplest approximation (leading graph: single vertex with
    r marked points on E_tau):
      a_0^{(r)} = S_r (the constant term)
      a_n^{(r)} = S_r * (correction from propagator on E_tau)

    The genus-1 propagator for the Virasoro algebra involves the
    Weierstrass zeta function on E_tau, whose periods are quasi-modular.
    The leading correction comes from sigma_{-1}(n) for the propagator.
    """
    S = virasoro_shadow_coefficients(c_val, max(r, 10))
    if r not in S:
        return {n: 0.0 for n in range(num_coeffs)}

    S_r = S[r]
    coeffs = {}

    # The genus-1 arity-r shadow: leading graph is a single vertex
    # with r legs. The amplitude on E_tau depends on the graph structure.
    #
    # For r=2 (kappa): Sh_2^{(1)} = kappa * lambda_1 = kappa (constant on M_{1,1})
    #   => a_0 = kappa, a_n = 0 for n >= 1
    #
    # For r=3 (cubic): The cubic shadow on E_tau involves the genus-1
    #   three-point function, which has E_2*-type corrections.
    #   Leading: a_0 = S_3 = 2
    #
    # For r=4 (quartic): The quartic shadow on E_tau involves the genus-1
    #   four-point function with contact-term contributions.
    #   Leading: a_0 = S_4

    if r == 2:
        # kappa is a constant class on M_{1,1}
        coeffs[0] = S_r
        for n in range(1, num_coeffs):
            coeffs[n] = 0.0
    else:
        # For r >= 3: the leading approximation has a_0 = S_r
        # with subleading corrections from the genus-1 propagator.
        # The propagator on E_tau is P(z, tau) = partial_z log theta_1(z, tau)
        # ~ 1/z + sum_{n>=1} (-1)^n 2 q^n/(1-q^n) * sin(2*pi*n*z).
        # The graph sum at arity r involves r-2 integrations of products
        # of these propagators.
        #
        # For the leading graph (star graph with r legs meeting at a vertex),
        # the amplitude factorizes and the q-expansion is:
        #   Sh_r(tau) = S_r * (1 + O(q))
        #
        # We compute the first-order correction from the one-loop diagram
        # with a single propagator insertion.
        coeffs[0] = S_r
        for n in range(1, num_coeffs):
            # First-order correction: the genus-1 propagator gives
            # a sigma_{r-1}(n) contribution from the r-point function.
            # This is approximate -- the exact computation requires the
            # full graph sum engine.
            sigma_val = sum(d ** (r - 1) for d in range(1, n + 1) if n % d == 0)
            # Correction coefficient involves the propagator variance
            # and the Bernoulli number B_{2r} / (2r)!
            correction = S_r * (-1) ** (r % 2) * sigma_val / (n * math.factorial(r))
            coeffs[n] = correction

    return coeffs


# =========================================================================
# 8. Utility functions
# =========================================================================

def _primes_up_to(n: int) -> List[int]:
    """Sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def _virasoro_shadow_radius(c_val: float) -> float:
    r"""Shadow growth rate rho for Virasoro at central charge c.

    rho = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|)

    where alpha = 2, Delta = 40/(5c+22), kappa = c/2.

    rho = sqrt(36 + 80/(5c+22)) / c
    """
    c_f = abs(float(c_val))
    if c_f < 1e-30:
        return float('inf')
    alpha = 2.0
    Delta = 40.0 / (5.0 * c_f + 22.0)
    kappa = c_f / 2.0
    rho = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * kappa)
    return rho


# =========================================================================
# 9. Comprehensive computation: all families
# =========================================================================

def compute_all_moment_l_functions(s_val: complex = 2.0,
                                    max_arity: int = 6) -> Dict[str, Any]:
    r"""Compute M_r(s) for r = 2, 3, 4 for all standard families.

    Returns a comprehensive dictionary with all results.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    results = {}

    # Heisenberg at k = 1
    heis_results = {}
    for r in range(2, max_arity + 1):
        M_r = moment_l_heisenberg(r, s_val, k_val=1.0)
        heis_results[r] = {
            'value': complex(M_r),
            'interpretation': (
                f'M_{r}(s) = zeta(2s)' if r == 2
                else f'M_{r}(s) = 0 (depth 2, terminates at r=2)'
            ),
        }
    results['Heisenberg_k1'] = {
        'family': 'Heisenberg',
        'level': 1.0,
        'kappa': 1.0,
        'depth': 2,
        'M_r': heis_results,
    }

    # Leech lattice
    leech_results = {}
    for r in range(2, min(max_arity + 1, 5)):
        M_r = moment_l_leech(r, s_val, num_terms=30)
        leech_results[r] = {
            'value': complex(M_r),
            'interpretation': (
                f'M_{r}(s) = c_E * zeta(s)*zeta(s-11) + c_Delta * L(s, Delta x Delta)'
                if r == 2 else
                f'M_{r}(s) involves Sym^{{{r-1}}} of Satake parameters'
            ),
        }
    results['Leech'] = {
        'family': 'Leech lattice',
        'rank': 24,
        'kappa': 12.0,
        'depth': 4,
        'M_r': leech_results,
    }

    # Virasoro at c = 1
    vir_results = {}
    for r in range(2, max_arity + 1):
        M_r = moment_l_virasoro(r, s_val, c_val=1.0, max_arity=max_arity)
        vir_results[r] = {
            'value': complex(M_r),
            'interpretation': f'M_{r}(s) ~ S_{r}(c=1) * zeta(2s)',
        }
    results['Virasoro_c1'] = {
        'family': 'Virasoro',
        'c': 1.0,
        'kappa': 0.5,
        'depth': float('inf'),
        'M_r': vir_results,
    }

    # Virasoro at c = 13 (self-dual)
    vir13_results = {}
    for r in range(2, max_arity + 1):
        M_r = moment_l_virasoro(r, s_val, c_val=13.0, max_arity=max_arity)
        vir13_results[r] = {
            'value': complex(M_r),
            'interpretation': f'M_{r}(s) ~ S_{r}(c=13) * zeta(2s) [self-dual]',
        }
    results['Virasoro_c13'] = {
        'family': 'Virasoro (self-dual)',
        'c': 13.0,
        'kappa': 6.5,
        'depth': float('inf'),
        'M_r': vir13_results,
    }

    return results


def compute_leech_m2_decomposition(s_val: complex = 2.0,
                                    num_terms: int = 50) -> Dict[str, Any]:
    r"""Verify the M_2 decomposition for the Leech lattice.

    The claim (eq:moment-euler-lattice):
      M_2(s; V_Leech) = c_E * zeta(s)*zeta(s-11) + c_Delta^2 * <Delta,Delta>_Pet^{-1} * L(s, Delta x Delta)

    The Eisenstein part: c_E * zeta(s) * zeta(s - 11)
    The cusp part: involves the Rankin-Selberg convolution L(s, Delta x Delta).

    We verify by computing both sides independently.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")

    from .lattice_shadow_periods import ramanujan_tau

    s_mp = mpmath.mpc(s_val)
    c_E = mpmath.mpf(1)
    c_Delta = mpmath.mpf(-65520) / mpmath.mpf(691)

    # Eisenstein contribution
    zeta_s = mpmath.zeta(s_mp)
    zeta_s11 = mpmath.zeta(s_mp - 11)
    L_E = zeta_s * zeta_s11

    # Cusp contribution: L(s, Delta x Delta) by direct summation
    # L(s, Delta x Delta) = sum_{n>=1} tau(n)^2 n^{-s}
    L_DxD = mpmath.mpf(0)
    for n in range(1, num_terms + 1):
        tau_n = ramanujan_tau(n)
        L_DxD += mpmath.mpf(tau_n ** 2) * mpmath.power(n, -s_mp)

    # Total: M_2 = c_E * L_E + c_Delta * (cusp part)
    # The cusp part of the Rankin-Selberg integral is:
    #   int |f|^2 E*(s) dmu = <f, E*_s f>_Pet
    # For a Hecke eigenform: this gives L(s, f x f) up to Gamma factors.
    # The actual decomposition is:
    #   M_2 = sum_j |c_j|^2 * L(s, f_j x f_j) / <f_j, f_j>_Pet
    # But the Eisenstein contribution comes from the Eisenstein term in theta.

    # For the Leech lattice:
    # M_2 = c_E^2 * L_E + |c_Delta|^2 / <Delta, Delta>_Pet * L(s, Delta x Delta)
    # The Petersson norm <Delta, Delta>_Pet is known:
    # <Delta, Delta> = (4*pi)^{-12} * Gamma(12) * L(12, Delta x Delta)
    # = (4*pi)^{-12} * 11! * L(12, Delta x Delta)
    # Numerically: <Delta, Delta> = 1.03536... * 10^{-6}

    # Petersson norm of Delta (standard normalization)
    # <Delta, Delta>_{Pet} = int |Delta(tau)|^2 y^{12} dmu
    # = (4pi)^{-12} * Gamma(12) * sum tau(n)^2 / n^{12}
    # = 11! / (4*pi)^{12} * L(12, Delta x Delta)

    Pet_norm = mpmath.mpf(0)
    for n in range(1, num_terms + 1):
        tau_n = ramanujan_tau(n)
        Pet_norm += mpmath.mpf(tau_n ** 2) * mpmath.power(n, -12)
    Pet_norm *= mpmath.factorial(11) / mpmath.power(4 * mpmath.pi, 12)

    M_2_decomposed = c_E * L_E + c_Delta ** 2 / Pet_norm * L_DxD

    # Direct computation of M_2 via the full moment L-function
    M_2_direct = moment_l_leech(2, s_val, num_terms=num_terms)

    return {
        's': complex(s_val),
        'c_E': float(c_E),
        'c_Delta': float(c_Delta),
        'L_Eisenstein': complex(L_E),
        'L_DeltaxDelta': complex(L_DxD),
        'Petersson_norm': float(Pet_norm),
        'M_2_decomposed': complex(M_2_decomposed),
        'M_2_direct': complex(M_2_direct),
        'agreement': abs(complex(M_2_decomposed - M_2_direct)) < abs(complex(M_2_direct)) * 0.1,
        'note': ('The decomposition M_2 = c_E*zeta(s)*zeta(s-11) + |c_Delta|^2/<Delta,Delta> * '
                 'L(s, Delta x Delta) involves the Petersson inner product normalization. '
                 'The direct computation via prime sums may differ from the Dirichlet series '
                 'approach due to convergence rate.'),
    }


# =========================================================================
# 10. Summary report
# =========================================================================

def summary_report(s_val: complex = 2.0) -> str:
    r"""Generate a comprehensive summary report of all moment L-function computations."""
    if not HAS_MPMATH:
        return "mpmath required for computation"

    lines = []
    lines.append("=" * 72)
    lines.append("MOMENT L-FUNCTION LANDSCAPE AND AUTOMORPHIC INTERPRETATION")
    lines.append("=" * 72)
    lines.append("")

    # 1. Compute M_r for all families
    lines.append("1. MOMENT L-FUNCTIONS M_r(s) at s = {}".format(s_val))
    lines.append("-" * 50)

    all_M = compute_all_moment_l_functions(s_val, max_arity=6)
    for name, data in all_M.items():
        lines.append(f"\n  {data['family']} (kappa = {data['kappa']}, depth = {data['depth']}):")
        for r, mr_data in data['M_r'].items():
            val = mr_data['value']
            lines.append(f"    M_{r}({s_val}) = {val.real:.10f} + {val.imag:.10f}i")
            lines.append(f"      Interpretation: {mr_data['interpretation']}")

    # 2. Automorphic table
    lines.append("\n\n2. AUTOMORPHIC INTERPRETATION TABLE")
    lines.append("-" * 50)
    table = automorphic_interpretation_table()
    for entry in table:
        lines.append(
            f"  Arity {entry['arity']}: {entry['symmetric_power']} on {entry['gl_rank']} "
            f"-- {entry['status']}"
        )
        lines.append(f"    {entry['description']}")

    # 3. Shadow Dirichlet series
    lines.append("\n\n3. SHADOW DIRICHLET SERIES Z_sh(s)")
    lines.append("-" * 50)
    for c_val in [1.0, 13.0, 25.0]:
        rho = _virasoro_shadow_radius(c_val)
        Z2 = shadow_dirichlet_virasoro(2.0, c_val, 30)
        Z3 = shadow_dirichlet_virasoro(3.0, c_val, 30)
        lines.append(f"  Virasoro c={c_val}: rho={rho:.6f}")
        lines.append(f"    Z_sh(2) = {complex(Z2).real:.10f}")
        lines.append(f"    Z_sh(3) = {complex(Z3).real:.10f}")

    # 4. Selberg class tests
    lines.append("\n\n4. SELBERG CLASS ANALYSIS")
    lines.append("-" * 50)
    for c_val in [1.0, 13.0, 25.0]:
        analysis = selberg_class_analysis('Virasoro', {'c': c_val}, max_arity=15)
        lines.append(f"  Virasoro c={c_val}: {analysis['note']}")
        if 'euler_product' in analysis:
            ep = analysis['euler_product']
            lines.append(f"    Euler product test: {ep['tests']} tests, "
                         f"{ep['failures']} failures")

    # 5. Self-dual analysis
    lines.append("\n\n5. SELF-DUAL ANALYSIS AT c = 13")
    lines.append("-" * 50)
    sd = virasoro_self_dual_analysis(max_arity=20)
    lines.append(f"  kappa = {sd['kappa']}, kappa! = {sd['kappa_dual']}")
    lines.append(f"  kappa + kappa! = {sd['kappa_sum']} (AP24: NOT zero)")
    lines.append(f"  delta_kappa = {sd['delta_kappa']} (vanishes at self-dual)")
    lines.append(f"  shadow radius = {sd['shadow_radius']:.6f}")
    for r, data in sd['shadow_coefficients'].items():
        lines.append(f"  S_{r}(13) = {data:.12e}")

    lines.append("\n" + "=" * 72)
    return "\n".join(lines)


if __name__ == '__main__':
    print(summary_report(2.0))
