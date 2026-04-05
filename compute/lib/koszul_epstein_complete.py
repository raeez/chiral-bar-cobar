#!/usr/bin/env python3
r"""
koszul_epstein_complete.py -- Complete Koszul-Epstein functional equation for all families.

PROGRAMME:
  The Koszul-Epstein function eps^KE_A(s) is a constrained Epstein zeta
  built from the shadow metric Q_L. For class M algebras, it satisfies
  the Epstein functional equation Lambda^KE(s) = Lambda^KE(1-s).

  The constrained Epstein functional equation is:
      eps^c_{c/2-s} = F_c(s) * eps^c_{c/2+s-1}
  where F_c(s) = Gamma(s)*Gamma(s+c/2-1)*zeta(2s) /
                 (pi^{2s-1/2}*Gamma(c/2-s)*Gamma(s-1/2)*zeta(2s-1))

  The scattering factor F_c(s) contains zeta(2s)/zeta(2s-1), linking
  to the zeta zeros: F_c has poles at s = (1+rho)/2 for each nontrivial
  zero rho of zeta (Benjamin-Chang connection).

FAMILIES COVERED:
  (a) Heisenberg H_k: eps^KE = 2*k^{-2s}*zeta(2s), zeros on Re(s) = 1/4
  (b) Virasoro at c = 1/2, 1, 2, 13, 25, 26: theta-function method
  (c) W_3 at c = 2: 2D shadow metric on T and W lines
  (d) E_8 lattice: 240 * 4^{-s} * zeta(s) * zeta(s-3)
  (e) Leech lattice: involves zeta, zeta(s-11), L(s, Delta_{12})

SCATTERING FACTOR AT ZETA ZEROS:
  The universal residue factor is
      A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
                 / (2*pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

  The residue kernel at conformal weight Delta is
      w_{c,rho,u0}(Delta) = 2*|A_c(rho)| * (2*Delta)^{-(c+sigma-1)/2}
                            * Delta^{-u0} * cos(gamma/2 * log(2*Delta) + arg(A_c(rho)))

Manuscript references:
    def:koszul-epstein-function (arithmetic_shadows.tex, line 2819)
    prop:heisenberg-koszul-epstein (line 2909)
    comp:virasoro-c1-koszul-epstein (line 2960)
    eq:constrained-epstein-fe (line 3303)
    def:universal-residue-factor (line 3322)
    prop:on-off-line-distinction (line 3341)
"""

from fractions import Fraction
from typing import Dict, List, Optional, Tuple, Union
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ================================================================
# 1. Shadow data for all standard families
# ================================================================

def virasoro_shadow_data(c):
    r"""Shadow data (kappa, alpha, S4, Delta) for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S4 = 10/(c*(5c+22)), Delta = 40/(5c+22).
    """
    c_f = float(c)
    kappa = c_f / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_f * (5.0 * c_f + 22.0))
    Delta = 40.0 / (5.0 * c_f + 22.0)
    return {'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta}


def heisenberg_shadow_data(k=1):
    r"""Shadow data for Heisenberg at level k.

    kappa = k (the level, NOT c/2; AP1/AP9).
    alpha = 0, S4 = 0, Delta = 0. Class G, shadow depth 2.
    """
    return {'kappa': float(k), 'alpha': 0.0, 'S4': 0.0, 'Delta': 0.0}


def w3_shadow_data(c):
    r"""Shadow data for W_3 at central charge c.

    T-line: same as Virasoro (kappa_T = c/2, alpha_T = 2).
    W-line: kappa_W = c/3, alpha_W = 0, S4_W from W_3 OPE.
    Mixed shadow metric is 2D.
    """
    c_f = float(c)
    T = virasoro_shadow_data(c_f)
    kappa_W = c_f / 3.0
    alpha_W = 0.0
    S4_W = 2560.0 / (c_f * (5.0 * c_f + 22.0) ** 3) if c_f != 0 else 0.0
    Delta_W = 8.0 * kappa_W * S4_W
    return {
        'T_line': T,
        'W_line': {
            'kappa': kappa_W, 'alpha': alpha_W,
            'S4': S4_W, 'Delta': Delta_W,
        },
        'c': c_f,
    }


def minimal_model_c(m):
    r"""Central charge c = 1 - 6/(m(m+1)) for unitary minimal model M(m, m+1)."""
    return Fraction(1) - Fraction(6, m * (m + 1))


# ================================================================
# 2. Binary quadratic form from shadow data
# ================================================================

def binary_form_coefficients(kappa, alpha, S4):
    r"""Coefficients (a, b, c) of Q(m,n) = a*m^2 + b*m*n + c*n^2.

    From Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2.
    """
    a = 4.0 * kappa ** 2
    b = 12.0 * kappa * alpha
    c_coeff = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    return a, b, c_coeff


def form_discriminant(a, b, c):
    r"""Discriminant D = b^2 - 4*a*c."""
    return b * b - 4.0 * a * c


# ================================================================
# 3. Epstein zeta via theta-function splitting (analytic continuation)
# ================================================================

def _theta_binary(t_val, a_c, b_c, c_c, N=25):
    r"""theta(t) = sum_{(m,n)} exp(-pi*t*Q(m,n))."""
    result = mpmath.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            Q = a_c * m * m + b_c * m * n + c_c * n * n
            result += mpmath.exp(-mpmath.pi * t_val * Q)
    return result


def _dual_form(a_c, b_c, c_c):
    r"""Dual form coefficients. If Q = am^2+bmn+cn^2 with disc D = b^2-4ac,
    then Q^*(m,n) = (4/|D|)(c*m^2 - b*mn + a*n^2).
    """
    D = b_c ** 2 - 4.0 * a_c * c_c
    DE = abs(D) / 4.0
    return float(c_c) / DE, -float(b_c) / DE, float(a_c) / DE


def epstein_phi(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Compute phi(s) = pi^{-s} * Gamma(s) * eps_Q(s) via theta splitting.

    Uses Mellin transform with splitting at t=1 and Poisson summation
    for the t < 1 part. Valid for all s (away from pole at s=1).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpf(s_val) if isinstance(s_val, (int, float)) else mpmath.mpc(s_val)

    D = b_c ** 2 - 4.0 * a_c * c_c
    DE = mpmath.mpf(abs(D)) / 4
    factor = 1.0 / mpmath.sqrt(DE)

    a_star, b_star, c_star = _dual_form(a_c, b_c, c_c)

    def integrand_s(t):
        th = _theta_binary(t, a_c, b_c, c_c, N_theta)
        return (th - 1) * mpmath.power(t, s_mp - 1)

    def integrand_dual(t):
        th = _theta_binary(t, a_star, b_star, c_star, N_theta)
        return (th - 1) * mpmath.power(t, -s_mp)

    I_s = mpmath.quad(integrand_s, [1, 10], maxdegree=8)
    I_dual = mpmath.quad(integrand_dual, [1, 10], maxdegree=8)

    R = factor / (s_mp - 1) - 1 / s_mp

    return I_s + factor * I_dual + R


def epstein_zeta(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Epstein zeta eps_Q(s) via analytic continuation (theta splitting)."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpf(s_val) if isinstance(s_val, (int, float)) else mpmath.mpc(s_val)
    phi = epstein_phi(s_val, a_c, b_c, c_c, N_theta)
    return mpmath.power(mpmath.pi, s_mp) / mpmath.gamma(s_mp) * phi


def epstein_zeta_lattice_sum(s, a, b, c_coeff, N=100):
    r"""Epstein zeta by direct lattice sum. Converges only for Re(s) > 1."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    result = mpmath.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m == 0 and n == 0:
                continue
            Q_mn = a * m ** 2 + b * m * n + c_coeff * n ** 2
            if Q_mn > 0:
                result += mpmath.power(mpmath.mpf(Q_mn), -s_mp)
    return complex(result)


def completed_epstein(s_val, a_c, b_c, c_c, N_theta=25):
    r"""Completed Epstein zeta Xi_Q(s) = D_E^{s/2} * pi^{-s} * Gamma(s) * eps_Q(s).

    Satisfies Xi_Q(s) = Xi_Q(1-s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpf(s_val) if isinstance(s_val, (int, float)) else mpmath.mpc(s_val)
    D = b_c ** 2 - 4.0 * a_c * c_c
    DE = abs(D) / 4.0
    phi = epstein_phi(s_val, a_c, b_c, c_c, N_theta)
    return mpmath.power(DE, s_mp / 2) * phi


# ================================================================
# 4. Koszul-Epstein functions for all families
# ================================================================

def koszul_epstein_heisenberg(s, k=1):
    r"""Koszul-Epstein for Heisenberg H_k:

        eps^KE_{H_k}(s) = 2 * k^{-2s} * zeta(2s)

    Zeros at Re(s) = 1/4 (rescaled critical line of zeta).
    (Proposition prop:heisenberg-koszul-epstein)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    return complex(2 * mpmath.power(float(k), -2 * s_mp) * mpmath.zeta(2 * s_mp))


def koszul_epstein_virasoro(s, c, N_theta=20):
    r"""Koszul-Epstein for Virasoro at central charge c.

    This is the Epstein zeta of the shadow metric Q_Vir(m,n).
    Uses theta-function analytic continuation (valid for all s).
    """
    data = virasoro_shadow_data(c)
    a, b, cc = binary_form_coefficients(data['kappa'], data['alpha'], data['S4'])
    return complex(epstein_zeta(s, a, b, cc, N_theta))


def completed_koszul_epstein_virasoro(s, c, N_theta=20):
    r"""Completed Koszul-Epstein for Virasoro."""
    data = virasoro_shadow_data(c)
    a, b, cc = binary_form_coefficients(data['kappa'], data['alpha'], data['S4'])
    return complex(completed_epstein(s, a, b, cc, N_theta))


def koszul_epstein_w3(s, c, line='T', N_theta=20):
    r"""Koszul-Epstein for W_3 at central charge c.

    W_3 has a 2D shadow metric with T-line and W-line projections.
    The T-line projection is the Virasoro shadow metric.
    The W-line projection has its own shadow data.

    Parameters
    ----------
    line : 'T' or 'W'
        Which primary line to compute on.
    """
    w3_data = w3_shadow_data(c)
    if line == 'T':
        data = w3_data['T_line']
    else:
        data = w3_data['W_line']
    a, b, cc = binary_form_coefficients(data['kappa'], data['alpha'], data['S4'])
    D = form_discriminant(a, b, cc)
    if D >= 0:
        # Degenerate case (W-line may have Delta=0)
        return complex(2 * mpmath.power(4 * data['kappa'] ** 2, -mpmath.mpc(s)) *
                       mpmath.zeta(2 * mpmath.mpc(s)))
    return complex(epstein_zeta(s, a, b, cc, N_theta))


def koszul_epstein_e8(s):
    r"""Koszul-Epstein for E_8 lattice VOA (c = 8).

        eps^KE_{E_8}(s) = 240 * 4^{-s} * zeta(s) * zeta(s-3)

    L-function content: zeta(s) and zeta(s-3).
    Critical lines: Re(s) = 1/2 and Re(s) = 7/2.
    Shadow depth 3 (class L, affine E_8 at level 1).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    return complex(240 * mpmath.power(4, -s_mp) * mpmath.zeta(s_mp) * mpmath.zeta(s_mp - 3))


def koszul_epstein_leech(s, n_terms=5000):
    r"""Koszul-Epstein for Leech lattice VOA (c = 24).

    The Leech theta function is
        Theta_Leech(tau) = 1 + 196560*q^2 + 16773120*q^4 + ...

    where q^n counts vectors of norm 2n. No vectors of norm 2.
    The theta series expansion gives:
        E_Leech(s) = sum_{n>=2} r_24(2n) * (2n)^{-s}

    For an even unimodular lattice of rank 24 with no roots, we
    have Theta = E_{12} - 720*Delta, where E_{12} is the Eisenstein
    series and Delta = q*prod(1-q^n)^24 is the Ramanujan discriminant.

    The Epstein zeta factors as:
        E_Leech(s) = c_0(s)*zeta(s)*zeta(s-11) + c_1(s)*L(s, Delta_{12})

    where L(s, Delta_{12}) is the Hecke L-function of the weight-12 cusp form.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)

    # Compute via theta coefficients: r_24(2n) for the Leech lattice.
    # Theta_Leech = E_{12} - 720*Delta
    # E_12 = 1 + (65520/691)*sum sigma_11(n)*q^n
    # Delta = sum tau(n)*q^n
    # So r_24(2n) = (65520/691)*sigma_11(n) - 720*tau(n) for n >= 1
    # and r_24(0) = 1.

    def sigma_k(n, k):
        """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
        return sum(d ** k for d in range(1, n + 1) if n % d == 0)

    def ramanujan_tau(n):
        """Ramanujan tau function via the Delta function expansion.

        Uses Ramanujan's formula: tau(n) is determined by
        Delta(q) = q * prod(1-q^k)^24 = sum tau(n)*q^n.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Compute via explicit product expansion
        # Delta = q * prod_{k=1}^{N} (1-q^k)^24
        # We need coefficients up to q^n, so expand to order n.
        coeffs = [0] * (n + 1)
        coeffs[0] = 1
        for k in range(1, n + 1):
            # Multiply by (1 - q^k)^24
            # Use logarithmic derivative: 24 factors of (1 - q^k)
            new_coeffs = list(coeffs)
            for _ in range(24):
                temp = list(new_coeffs)
                for j in range(k, n + 1):
                    temp[j] = new_coeffs[j] - new_coeffs[j - k]
                new_coeffs = temp
            coeffs = new_coeffs
        # Delta = q * prod = sum tau(n)*q^n
        # so tau(n) = coeffs[n-1] (the q^{n-1} coefficient of the product,
        # shifted by the leading q)
        return coeffs[n - 1] if n - 1 < len(coeffs) else 0

    # Compute the Leech Epstein sum via theta coefficients
    result = mpmath.mpf(0)
    E12_coeff = mpmath.mpf(65520) / mpmath.mpf(691)
    for n in range(1, n_terms + 1):
        r_2n = int(E12_coeff * sigma_k(n, 11)) - 720 * ramanujan_tau(n)
        if r_2n != 0:
            result += r_2n * mpmath.power(2 * n, -s_mp)
    # The constrained Epstein sums over (2*Delta)^{-s} where Delta = |lambda|^2/2.
    # For Leech with norm vectors at 2n: Delta = n, so (2*Delta) = 2n.
    # Wait: the Leech lattice has norms |lambda|^2 = 2n for n=0,2,3,...
    # Actually the Leech has minimum norm 4, so first nonzero at n=2.
    # The r_24(2n) counts vectors with |lambda|^2 = 2n.
    # The constrained Epstein: sum (2*Delta)^{-s} where 2*Delta = |lambda|^2 = 2n.
    # So eps = sum_{n>=2} r_24(2n) * (2n)^{-s}.
    # Above result already sums from n=1, but r_24(2) = 0 (no roots in Leech).
    return complex(result)


# ================================================================
# 5. Constrained Epstein functional equation and scattering factor
# ================================================================

def scattering_factor_Fc(s, c):
    r"""Scattering factor in the constrained Epstein functional equation.

    F_c(s) = Gamma(s)*Gamma(s+c/2-1)*zeta(2s)
             / (pi^{2s-1/2}*Gamma(c/2-s)*Gamma(s-1/2)*zeta(2s-1))

    The FE is:  eps^c_{c/2-s} = F_c(s) * eps^c_{c/2+s-1}

    Poles of F_c at:
      - s = c/2 (from Gamma(c/2-s))
      - s = (1+rho)/2 for nontrivial zeta zeros rho (from zeta(2s-1))
      - s = 1/2 (from Gamma(s-1/2))
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    s_mp = mpmath.mpc(s)
    c_mp = mpmath.mpf(float(c))

    num = (mpmath.gamma(s_mp) *
           mpmath.gamma(s_mp + c_mp / 2 - 1) *
           mpmath.zeta(2 * s_mp))

    denom = (mpmath.power(mpmath.pi, 2 * s_mp - mpmath.mpf('0.5')) *
             mpmath.gamma(c_mp / 2 - s_mp) *
             mpmath.gamma(s_mp - mpmath.mpf('0.5')) *
             mpmath.zeta(2 * s_mp - 1))

    return complex(num / denom)


def universal_residue_factor(rho, c):
    r"""Universal residue factor A_c(rho) at a nontrivial zero rho of zeta.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2)
                  * zeta'(rho))

    (eq:universal-residue, def:universal-residue-factor)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    rho_mp = mpmath.mpc(rho)
    c_mp = mpmath.mpf(float(c))

    num = (mpmath.gamma((1 + rho_mp) / 2) *
           mpmath.gamma((c_mp + rho_mp - 1) / 2) *
           mpmath.zeta(1 + rho_mp))

    # zeta'(rho): the derivative of zeta at the zero
    # For numerical computation, use mpmath.zeta(rho, derivative=1)
    zeta_prime_rho = mpmath.diff(mpmath.zeta, rho_mp)

    denom = (2 * mpmath.power(mpmath.pi, rho_mp + mpmath.mpf('0.5')) *
             mpmath.gamma((c_mp - rho_mp - 1) / 2) *
             mpmath.gamma(rho_mp / 2) *
             zeta_prime_rho)

    return complex(num / denom)


def residue_kernel(Delta, rho, c, u0=0):
    r"""Paired real residue kernel at conformal weight Delta.

    w_{c,rho,u0}(Delta) = 2*|A_c(rho)| * (2*Delta)^{-(c+sigma-1)/2}
                          * Delta^{-u0}
                          * cos(gamma/2 * log(2*Delta) + arg(A_c(rho)))

    where rho = sigma + i*gamma.
    (eq:residue-kernel, prop:on-off-line-distinction)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    A = universal_residue_factor(rho, c)
    sigma = rho.real if isinstance(rho, complex) else float(rho)
    gamma_im = rho.imag if isinstance(rho, complex) else 0.0

    abs_A = abs(A)
    arg_A = math.atan2(A.imag, A.real)
    c_f = float(c)
    Delta_f = float(Delta)

    decay = (2 * Delta_f) ** (-(c_f + sigma - 1) / 2)
    u0_factor = Delta_f ** (-u0) if u0 != 0 else 1.0
    cosine = math.cos(gamma_im / 2 * math.log(2 * Delta_f) + arg_A)

    return 2 * abs_A * decay * u0_factor * cosine


# ================================================================
# 6. Scattering factor at the first zeta zero
# ================================================================

def first_zeta_zero():
    r"""The first nontrivial zero of zeta: rho_1 = 1/2 + i*14.134725..."""
    if not HAS_MPMATH:
        return complex(0.5, 14.134725)
    return complex(mpmath.zetazero(1))


def scattering_at_rho1(c):
    r"""Scattering factor at s_rho1 = (1+rho_1)/2 = 3/4 + i*7.067...

    This is a pole of F_c(s) coming from zeta(2s-1) = zeta(rho_1) = 0
    in the denominator.

    Returns:
      - s_rho1: the evaluation point
      - F_c_nearby: F_c evaluated slightly away from the pole
      - A_c: the universal residue factor
      - residue_kernels: w at Delta = 1, 2, 3
    """
    rho1 = first_zeta_zero()
    s_rho1 = (1 + rho1) / 2

    # F_c has a pole at s_rho1; compute A_c(rho1) instead
    A_c_val = universal_residue_factor(rho1, c)

    # Evaluate F_c slightly away from the pole
    eps_shift = 0.001
    F_nearby_plus = scattering_factor_Fc(s_rho1 + eps_shift, c)
    F_nearby_minus = scattering_factor_Fc(s_rho1 - eps_shift, c)

    # Residue kernels at Delta = 1, 2, 3
    kernels = {}
    for Delta in [1, 2, 3]:
        kernels[Delta] = residue_kernel(Delta, rho1, c)

    return {
        'rho1': rho1,
        's_rho1': s_rho1,
        'A_c': A_c_val,
        'F_nearby_plus': F_nearby_plus,
        'F_nearby_minus': F_nearby_minus,
        'residue_kernels': kernels,
    }


# ================================================================
# 7. Functional equation verification
# ================================================================

def fe_test_epstein(s_val, a_c, b_c, c_c, N_theta=20):
    r"""Test Xi_Q(s) = Xi_Q(1-s). Returns dict with relative error."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    Xi_s = completed_epstein(s_val, a_c, b_c, c_c, N_theta)
    Xi_1s = completed_epstein(1 - s_val, a_c, b_c, c_c, N_theta)
    denom = max(abs(Xi_s), abs(Xi_1s), mpmath.mpf('1e-300'))
    rel_err = float(abs(Xi_s - Xi_1s) / denom)
    return {
        's': s_val,
        'Xi_s': complex(Xi_s),
        'Xi_1ms': complex(Xi_1s),
        'rel_err': rel_err,
        'passes': rel_err < 0.001,
    }


def fe_verify_virasoro(c_val, s_test=None, N_theta=20):
    r"""Verify FE for Virasoro shadow metric at central charge c."""
    if s_test is None:
        s_test = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    data = virasoro_shadow_data(c_val)
    a, b, cc = binary_form_coefficients(data['kappa'], data['alpha'], data['S4'])
    results = []
    for s in s_test:
        r = fe_test_epstein(s, a, b, cc, N_theta)
        r['c'] = float(c_val)
        results.append(r)
    return results


def fe_verify_heisenberg(k=1, s_test=None):
    r"""Verify the Heisenberg Koszul-Epstein functional equation.

    eps^KE_{H_k}(s) = 2*k^{-2s}*zeta(2s).
    Completed: Lambda(s) = k^{-2s} * Lambda_zeta(2s) (up to constants).
    Functional equation of zeta implies a functional equation for eps^KE
    at the level of 2s.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    if s_test is None:
        s_test = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]

    results = []
    for s in s_test:
        val_s = koszul_epstein_heisenberg(s, k)
        val_ref = koszul_epstein_heisenberg(s, k)
        # The Heisenberg FE is inherited from zeta(2s):
        # pi^{-s}*Gamma(s)*zeta(2s) = pi^{-(1/2-s)}*Gamma(1/2-s)*zeta(1-2s)
        # So the completed function is
        # Lambda_H(s) = pi^{-s} * Gamma(s) * k^{-2s} * zeta(2s) / 2
        # Symmetric about s = 1/4 (the critical line of zeta(2s)).
        s_mp = mpmath.mpc(s)
        k_mp = mpmath.mpf(float(k))
        Lam_s = (mpmath.power(mpmath.pi, -s_mp) * mpmath.gamma(s_mp) *
                 mpmath.power(k_mp, -2 * s_mp) * mpmath.zeta(2 * s_mp))
        s_dual = 0.5 - s
        sd_mp = mpmath.mpc(s_dual)
        Lam_dual = (mpmath.power(mpmath.pi, -sd_mp) * mpmath.gamma(sd_mp) *
                    mpmath.power(k_mp, -2 * sd_mp) * mpmath.zeta(2 * sd_mp))
        # These should be proportional (not equal) due to the k factors.
        # The exact relation for zeta(2s): xi(2s) = xi(1-2s)
        # where xi(s) = pi^{-s/2} * Gamma(s/2) * zeta(s)
        # So xi(2s) = pi^{-s} * Gamma(s) * zeta(2s) satisfies xi(2s) = xi(1-2s)
        # i.e. Lam_s / k^{-2s} = Lam_dual / k^{-2*s_dual}
        # which gives Lam_s * k^{2s} = Lam_dual * k^{2*s_dual} = Lam_dual * k^{1-2s}
        ratio_s = complex(Lam_s * mpmath.power(k_mp, 2 * s_mp))
        ratio_d = complex(Lam_dual * mpmath.power(k_mp, 2 * sd_mp))
        denom = max(abs(ratio_s), abs(ratio_d), 1e-300)
        rel_err = abs(ratio_s - ratio_d) / denom
        results.append({
            's': s, 's_dual': s_dual,
            'ratio_s': ratio_s, 'ratio_dual': ratio_d,
            'rel_err': rel_err,
            'passes': rel_err < 1e-10,
        })
    return results


# ================================================================
# 8. Imaginary quadratic field from shadow metric
# ================================================================

def squarefree_part(n):
    r"""Squarefree part of integer n."""
    if n == 0:
        return 0
    sign = 1 if n > 0 else -1
    n = abs(n)
    result = 1
    d = 2
    while d * d <= n:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        if count % 2 == 1:
            result *= d
        d += 1
    result *= n
    return sign * result


def _is_fundamental_discriminant(d):
    r"""Check if d is a fundamental discriminant."""
    if d == 0 or d == 1:
        return False
    if d % 4 == 1:
        return squarefree_part(d) == d
    elif d % 4 == 0:
        m = d // 4
        return (m % 4 in (2, 3)) and squarefree_part(m) == m
    return False


def fundamental_discriminant(D):
    r"""Given D < 0, find (d, f) with D = d*f^2, d fundamental."""
    if D >= 0:
        raise ValueError(f"Expected D < 0, got {D}")
    abs_D = abs(D)
    f = 1
    while f * f <= abs_D:
        if abs_D % (f * f) == 0:
            d_cand = D // (f * f)
            if _is_fundamental_discriminant(d_cand):
                return d_cand, f
        f += 1
    return D, 1


def class_number_small(d):
    r"""Class number h(d) for small negative fundamental discriminants.

    Uses Gauss reduced form enumeration.
    """
    if d >= 0 or not _is_fundamental_discriminant(d):
        raise ValueError(f"{d} is not a negative fundamental discriminant")
    abs_d = abs(d)
    bound = int(math.sqrt(abs_d / 3.0)) + 1
    count = 0
    for a in range(1, bound + 1):
        for b in range(-a, a + 1):
            num = b * b - d
            if num % (4 * a) != 0:
                continue
            c = num // (4 * a)
            if c < a:
                continue
            if abs(b) > a:
                continue
            if abs(b) == a or a == c:
                if b < 0:
                    continue
            count += 1
    return count


def roots_of_unity(d):
    r"""Number of roots of unity w in Q(sqrt(d))."""
    if d == -3:
        return 6
    elif d == -4:
        return 4
    return 2


def quadratic_field_from_virasoro(c_val):
    r"""Determine the quadratic field Q(sqrt(d)) from the Virasoro shadow metric.

    disc(Q) = -320*c^2/(5c+22). The squarefree part of the numerator*denominator
    product determines the field.

    Returns dict with squarefree part, fundamental discriminant, class number.
    """
    if isinstance(c_val, Fraction):
        disc = Fraction(-320) * c_val ** 2 / (5 * c_val + 22)
    else:
        disc = Fraction(-320) * Fraction(c_val).limit_denominator(10 ** 12) ** 2
        disc = disc / (5 * Fraction(c_val).limit_denominator(10 ** 12) + 22)

    p, q = disc.numerator, disc.denominator
    pq = p * q
    sf = squarefree_part(pq)
    fund_disc = sf if sf % 4 == 1 else 4 * sf

    try:
        h = class_number_small(fund_disc)
    except Exception:
        h = None
    w = roots_of_unity(fund_disc)

    return {
        'disc_rational': disc,
        'squarefree': sf,
        'fund_disc': fund_disc,
        'class_number': h,
        'roots_of_unity': w,
    }


def minimal_model_quadratic_fields(m_range=None):
    r"""Compute quadratic fields for all unitary minimal models.

    Returns list of dicts with m, c, field data.
    """
    if m_range is None:
        m_range = range(3, 21)

    results = []
    for m in m_range:
        c = minimal_model_c(m)
        field = quadratic_field_from_virasoro(c)
        results.append({
            'm': m,
            'c': str(c),
            'c_float': float(c),
            'squarefree': field['squarefree'],
            'fund_disc': field['fund_disc'],
            'class_number': field['class_number'],
            'roots_of_unity': field['roots_of_unity'],
        })

    h1_models = [r for r in results if r['class_number'] == 1]
    return {
        'models': results,
        'h1_models': [(r['m'], r['fund_disc']) for r in h1_models],
        'h1_count': len(h1_models),
    }


# ================================================================
# 9. Benjamin-Chang connection analysis
# ================================================================

def benjamin_chang_analysis(c_values=None):
    r"""Analysis of the Benjamin-Chang connection.

    Benjamin-Chang (2022) studied Epstein zeta functions of binary
    quadratic forms and their decomposition into Hecke L-functions.
    Their key result: for a positive definite binary form Q with
    discriminant D < 0,

        Z_Q(s) = (2/w) * sum_{chi in Cl(D)^} chi(cl(Q)) * L(s, chi)

    where w = number of roots of unity, Cl(D) = class group,
    chi ranges over genus characters, and L(s, chi) are Hecke L-functions.

    For the Koszul-Epstein function:
    1. The scattering factor F_c(s) contains zeta(2s)/zeta(2s-1)
    2. This means F_c has poles at s = (1+rho)/2 for zeta zeros rho
    3. The MC equation constrains eps^c_s, hence constrains how
       the Koszul-Epstein function couples to each zeta zero
    4. The structural separation: genus-1 MC lives on the REAL axis,
       while zeta zeros are at s = 1/2 + i*gamma (COMPLEX)

    Returns analysis dict for each c value.
    """
    if c_values is None:
        c_values = [0.5, 1.0, 2.0, 13.0, 25.0, 26.0]

    results = {}
    for c in c_values:
        rho1 = first_zeta_zero()
        s_rho1 = (1 + rho1) / 2

        # The scattering factor diverges at s_rho1
        # Compute the universal residue factor instead
        A = universal_residue_factor(rho1, c)

        # Real-axis evaluation (where the MC equation lives)
        F_real = []
        for s_real in [0.3, 0.5, 0.7, 1.0, 1.5]:
            try:
                F_val = scattering_factor_Fc(s_real, c)
                F_real.append({'s': s_real, 'F': F_val})
            except Exception:
                F_real.append({'s': s_real, 'F': None})

        results[c] = {
            'c': c,
            'rho1': rho1,
            's_rho1': s_rho1,
            'A_c_rho1': A,
            '|A_c_rho1|': abs(A),
            'arg_A_c_rho1': math.atan2(A.imag, A.real),
            'F_real_axis': F_real,
            'structural_separation': (
                'genus-1 MC equation lives on Re(s) axis; '
                'zeta zeros at Re(s) = 1/2 + i*gamma are complex'
            ),
        }

    return results


# ================================================================
# 10. Kronecker symbol and Dirichlet L-functions
# ================================================================

def _jacobi_symbol(a, n):
    r"""Jacobi symbol (a/n) for odd n > 0."""
    if n <= 0 or n % 2 == 0:
        raise ValueError(f"n must be odd positive, got {n}")
    a = a % n
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


def kronecker_symbol(d, n):
    r"""Kronecker symbol (d/n)."""
    if n == 0:
        return 1 if abs(d) == 1 else 0
    if n == 1:
        return 1
    if n < 0:
        n = -n
        if d < 0:
            return -kronecker_symbol(d, n)
        return kronecker_symbol(d, n)
    result = 1
    while n % 2 == 0:
        n //= 2
        if d % 2 == 0:
            return 0
        d8 = d % 8
        if d8 == 3 or d8 == 5:
            result *= -1
    if n > 1:
        result *= _jacobi_symbol(d, n)
    return result


def dirichlet_l(s, d, n_terms=10000):
    r"""L(s, chi_d) = sum_{n>=1} chi_d(n) * n^{-s}."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    s_mp = mpmath.mpc(s)
    result = mpmath.mpf(0)
    for n in range(1, n_terms + 1):
        chi = kronecker_symbol(d, n)
        if chi != 0:
            result += chi * mpmath.power(n, -s_mp)
    return complex(result)


# ================================================================
# 11. Complete family survey
# ================================================================

def complete_family_survey(N_theta=18):
    r"""Complete Koszul-Epstein computation for every standard family.

    Returns dict indexed by family name, with:
      - eps^KE at s=2
      - functional equation verification
      - L-function content description
      - quadratic field (if applicable)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    survey = {}

    # (a) Heisenberg H_k for k = 1, 2
    for k in [1, 2]:
        label = f'Heisenberg_k{k}'
        eps_2 = koszul_epstein_heisenberg(2.0, k)
        # Check: 2 * k^{-4} * zeta(4) = 2 * k^{-4} * pi^4/90
        expected = 2 * k ** (-4) * float(mpmath.zeta(4))
        fe = fe_verify_heisenberg(k)
        survey[label] = {
            'family': 'heisenberg', 'k': k,
            'eps_at_2': eps_2,
            'expected_at_2': expected,
            'match': abs(eps_2 - expected) / abs(expected) < 1e-10,
            'fe_passes': all(r['passes'] for r in fe),
            'zeros': 'Re(s) = 1/4 (from zeta(2s) critical line)',
            'L_content': f'zeta(2s), one critical line',
        }

    # (b) Virasoro at various c
    for c_val, label in [(0.5, 'Ising'), (1.0, 'c=1'), (2.0, 'betagamma'),
                         (13.0, 'self-dual'), (25.0, 'c=25'), (26.0, 'critical_string')]:
        data = virasoro_shadow_data(c_val)
        a, b, cc = binary_form_coefficients(data['kappa'], data['alpha'], data['S4'])
        D = form_discriminant(a, b, cc)

        eps_2 = complex(epstein_zeta(2.0, a, b, cc, N_theta))
        fe = fe_verify_virasoro(c_val, N_theta=N_theta)

        field = quadratic_field_from_virasoro(Fraction(c_val).limit_denominator(1000))

        survey[f'Virasoro_{label}'] = {
            'family': 'virasoro', 'c': c_val,
            'kappa': data['kappa'], 'alpha': data['alpha'],
            'S4': data['S4'], 'Delta': data['Delta'],
            'form': (a, b, cc), 'disc': D,
            'eps_at_2': eps_2,
            'fe_passes': all(r['passes'] for r in fe),
            'fe_details': fe,
            'field': field,
            'L_content': (
                f"Epstein zeta of binary form, disc={D:.4f}, "
                f"Q(sqrt({field['squarefree']})), h={field['class_number']}"
            ),
        }

    # (c) W_3 at c = 2 (T-line and W-line)
    c_w3 = 2.0
    w3 = w3_shadow_data(c_w3)
    for line_name, line_data in [('T', w3['T_line']), ('W', w3['W_line'])]:
        a, b, cc = binary_form_coefficients(
            line_data['kappa'], line_data['alpha'], line_data['S4'])
        D = form_discriminant(a, b, cc)
        if D < 0:
            eps_2 = complex(epstein_zeta(2.0, a, b, cc, N_theta))
            survey[f'W3_c2_{line_name}line'] = {
                'family': 'w3', 'c': c_w3, 'line': line_name,
                'kappa': line_data['kappa'], 'alpha': line_data['alpha'],
                'S4': line_data['S4'],
                'form': (a, b, cc), 'disc': D,
                'eps_at_2': eps_2,
                'L_content': 'Epstein zeta of 2D shadow form',
            }
        else:
            # Degenerate (W-line at c=2 may have very small Delta)
            survey[f'W3_c2_{line_name}line'] = {
                'family': 'w3', 'c': c_w3, 'line': line_name,
                'kappa': line_data['kappa'], 'alpha': line_data['alpha'],
                'S4': line_data['S4'],
                'form': (a, b, cc), 'disc': D,
                'eps_at_2': None,
                'L_content': 'Degenerate (rank 1 or semidefinite)',
            }

    # (d) E_8 lattice
    eps_e8_2 = koszul_epstein_e8(2.0)
    # Expected: 240 * 4^{-2} * zeta(2) * zeta(-1) = 240/16 * pi^2/6 * (-1/12)
    # = 15 * pi^2/6 * (-1/12) = 15 * (-pi^2/72) < 0 ? No, zeta(-1) = -1/12.
    # Actually zeta(s-3) at s=2 is zeta(-1) = -1/12.
    # 240 * 4^{-2} * zeta(2) * zeta(-1) = 240/16 * pi^2/6 * (-1/12)
    # = 15 * 1.6449... * (-0.08333...) = 15 * (-0.137...) = -2.056...
    expected_e8 = complex(240 * mpmath.power(4, -2) * mpmath.zeta(2) * mpmath.zeta(-1))
    survey['E8_lattice'] = {
        'family': 'e8_lattice', 'c': 8,
        'eps_at_2': eps_e8_2,
        'expected_at_2': expected_e8,
        'match': abs(eps_e8_2 - expected_e8) / max(abs(expected_e8), 1e-30) < 1e-10,
        'L_content': '240 * 4^{-s} * zeta(s) * zeta(s-3), two critical lines',
        'critical_lines': ['Re(s) = 1/2', 'Re(s) = 7/2'],
    }

    # (e) Leech lattice (first few terms)
    eps_leech = koszul_epstein_leech(4.0, n_terms=500)
    survey['Leech_lattice'] = {
        'family': 'leech_lattice', 'c': 24,
        'eps_at_4': eps_leech,
        'L_content': 'zeta(s)*zeta(s-11) + L(s, Delta_12), three+ critical lines',
        'critical_lines': ['Re(s) = 1/2', 'Re(s) = 23/2', 'Re(s) = 1/2 (from Delta)'],
    }

    return survey


# ================================================================
# 12. Export all public functions
# ================================================================

__all__ = [
    # Shadow data
    'virasoro_shadow_data', 'heisenberg_shadow_data', 'w3_shadow_data',
    'minimal_model_c',
    # Binary forms
    'binary_form_coefficients', 'form_discriminant',
    # Epstein zeta
    'epstein_zeta', 'epstein_zeta_lattice_sum', 'completed_epstein', 'epstein_phi',
    # Koszul-Epstein by family
    'koszul_epstein_heisenberg', 'koszul_epstein_virasoro',
    'completed_koszul_epstein_virasoro',
    'koszul_epstein_w3', 'koszul_epstein_e8', 'koszul_epstein_leech',
    # Scattering factor and residues
    'scattering_factor_Fc', 'universal_residue_factor',
    'residue_kernel', 'first_zeta_zero', 'scattering_at_rho1',
    # Functional equation
    'fe_test_epstein', 'fe_verify_virasoro', 'fe_verify_heisenberg',
    # Number theory
    'squarefree_part', 'fundamental_discriminant', 'class_number_small',
    'roots_of_unity', 'quadratic_field_from_virasoro',
    'minimal_model_quadratic_fields',
    'kronecker_symbol', 'dirichlet_l',
    # Analysis
    'benjamin_chang_analysis', 'complete_family_survey',
]
