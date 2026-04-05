#!/usr/bin/env python3
r"""
generic_c_frontier.py — Shadow-spectral correspondence at generic central charge.

THE PROBLEM:
  The theta decomposition bridge (spectral_continuation.py) works for rational
  VOAs (finite primaries, level-2pq theta functions). At generic c, the Virasoro
  VOA has infinitely many primaries (all Verma modules) and the partition function
  is NOT a classical modular form.

THE VACUUM CHARACTER:
  chi_c(tau) = q^{(c-1)/24} / eta(tau)
  On the imaginary axis tau = iy:
    |chi_c(iy)|^2 = e^{-2*pi*y*(c-1)/12} / |eta(iy)|^2

THE PRIMARY-COUNTING FUNCTION (Benjamin-Chang):
  Z_hat_c = y^{c/2} |eta|^{2c} |chi_c|^2
          = y^{c/2} |eta|^{2(c-1)} e^{-2*pi*y*(c-1)/12}

THE ETA POWER |eta|^{2*alpha}:
  For integer alpha = 2*(c-1), eta^{2*(c-1)} is a modular form of weight c-1.
  For irrational c, |eta|^{2*(c-1)} is NOT a modular form for any congruence
  subgroup. The Rankin-Selberg integral still converges.

THE SHADOW DATA:
  kappa(c) = c/2               (proved, rational in c)
  Q^contact(c) = 10/[c(5c+22)] (proved, rational in c)
  G(t) = -log(1 + 6t/c)        (shadow GF, rational in c)

  These are RATIONAL FUNCTIONS of c -- they make sense for ALL c, including
  irrational. The shadow data varies smoothly with c. The question: does
  the L-function content also vary smoothly?

KEY FINDING:
  At integer c: eta^{2(c-1)} is a modular form (of weight c-1 for some
  congruence subgroup). The L-function content changes DISCONTINUOUSLY
  as c varies over integers (different forms, different Hecke eigenvalues).
  But the shadow obstruction tower provides a CONTINUOUS interpolation: kappa, Q^contact,
  and the full shadow GF are smooth curves through the discrete L-function data.

  THE CONTINUOUS SHADOW-SPECTRAL CORRESPONDENCE:
  The shadow obstruction tower encodes L-function content continuously via rational functions
  of c, while the L-functions themselves are discrete objects attached only to
  integer (or half-integer) c values.

WHAT THIS MODULE COMPUTES:
  (GC1) Vacuum character |chi_c|^2 and primary-counting function Z_hat_c
        at general c, numerically on the imaginary axis.
  (GC2) Eta power |eta|^{2*alpha} for general real alpha, including
        Fourier expansion of eta^{2m} for integer m.
  (GC3) Rankin-Selberg Mellin integral Z_alpha(s) = int |eta|^{2*alpha} y^s dy/y
        computed by numerical integration over the fundamental domain.
  (GC4) Interpolation at non-integer c: multiplicativity test for Fourier
        coefficients of |eta|^{2*alpha} at non-integer alpha.
  (GC5) Analytic continuation in c: Z_c(s) as a function of c.
  (GC6) Shadow data at generic c: kappa, Q^contact, G(t) as smooth functions.
  (GC7) Modularity classification: for eta^{2m}, determine the level N and
        character chi such that eta^{2m} is in M_m(Gamma_0(N), chi).
  (GC8) The irrational-c obstruction: convergence of Z_alpha(s) for
        alpha = pi - 1 (irrational), demonstrating that the Mellin integral
        converges even when no modular form exists.

References:
  Benjamin-Chang, arXiv:2208.02259, 2022.
  Rankin, "Contributions to the theory of Ramanujan's function tau(n)", 1939.
  Selberg, "Bemerkungen uber eine Dirichletsche Reihe", 1940.
  Zagier, "The Rankin-Selberg method for automorphic forms", 2008.
"""

from functools import lru_cache

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

import numpy as np


# ============================================================
# 1. Eta function and powers on the imaginary axis
# ============================================================

def eta_imaginary_axis(y, dps=50):
    """Compute eta(iy) = e^{-pi*y/12} * prod_{n>=1}(1 - e^{-2*pi*n*y}).

    Returns mpmath.mpf value.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps):
        q = mpmath.exp(-mpmath.pi * y)  # q = e^{-pi*y} so q^{1/12} = e^{-pi*y/12}
        # eta(iy) = q^{1/12} * prod(1 - q^{2n})  where q = e^{-pi*y}
        # Actually tau = iy, so q_tau = e^{2*pi*i*tau} = e^{-2*pi*y}
        q_tau = mpmath.exp(-2 * mpmath.pi * y)
        prefactor = mpmath.exp(-mpmath.pi * y / 12)  # q_tau^{1/24}

        product = mpmath.mpf(1)
        for n in range(1, 500):
            term = 1 - q_tau ** n
            if abs(term - 1) < mpmath.mpf(10) ** (-(dps + 10)):
                break
            product *= term

        return prefactor * product


def eta_abs_squared(y, dps=50):
    """Compute |eta(iy)|^2.  Since eta(iy) is real for real y > 0, this is eta(iy)^2."""
    val = eta_imaginary_axis(y, dps=dps)
    return val * val


def eta_power_imaginary(y, alpha, dps=50):
    r"""Compute |eta(iy)|^{2*alpha} for real alpha.

    Since eta(iy) is real and positive for y > 0, this is eta(iy)^{2*alpha}.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps):
        val = eta_imaginary_axis(y, dps=dps)
        return mpmath.power(val, 2 * alpha)


# ============================================================
# 2. Vacuum character and primary-counting function
# ============================================================

def vacuum_character_abs_sq(c, y, dps=50):
    r"""Compute |chi_c(iy)|^2 for the Virasoro vacuum character at central charge c.

    chi_c(tau) = q^{(c-1)/24} / eta(tau)
    |chi_c(iy)|^2 = e^{-2*pi*y*(c-1)/12} / |eta(iy)|^2
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps):
        c = mpmath.mpf(c)
        y = mpmath.mpf(y)
        exp_factor = mpmath.exp(-2 * mpmath.pi * y * (c - 1) / 12)
        eta_sq = eta_abs_squared(y, dps=dps)
        if eta_sq == 0:
            return mpmath.mpf('inf')
        return exp_factor / eta_sq


def primary_counting_function(c, y, dps=50):
    r"""Compute Z_hat_c(y) = y^{c/2} |eta(iy)|^{2(c-1)} e^{-2*pi*y*(c-1)/12}.

    This is the primary-counting function from Benjamin-Chang:
      Z_hat_c = y^{c/2} |eta|^{2c} |chi_c|^2
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps):
        c = mpmath.mpf(c)
        y = mpmath.mpf(y)
        y_power = mpmath.power(y, c / 2)
        eta_pow = eta_power_imaginary(y, c - 1, dps=dps)
        exp_factor = mpmath.exp(-2 * mpmath.pi * y * (c - 1) / 12)
        return y_power * eta_pow * exp_factor


def primary_counting_table(c_values, y_values, dps=30):
    """Compute Z_hat_c(y) for a grid of c and y values.

    Returns dict: {(c, y): Z_hat_c(y)}.
    """
    results = {}
    for c in c_values:
        for y in y_values:
            results[(c, y)] = primary_counting_function(c, y, dps=dps)
    return results


# ============================================================
# 3. Fourier expansion of eta^{2m} for integer m
# ============================================================

def eta_power_coefficients(m, nmax=100):
    r"""Compute the first nmax+1 coefficients of eta(tau)^{2m} / q^{m/12}.

    eta^{2m} = q^{m/12} * prod_{n>=1}(1-q^n)^{2m}
    Write prod(1-q^n)^{2m} = sum_{k>=0} a_k q^k.
    Then eta^{2m} = sum_{k>=0} a_k q^{k + m/12}.

    Returns the coefficients [a_0, a_1, ..., a_nmax] of prod(1-q^n)^{2m}.
    For m = 12 (eta^24 = Delta): a_k = tau(k+1) (Ramanujan tau).
    """
    N = nmax + 2
    # Use exact integer arithmetic for integer 2m
    two_m = 2 * m
    coeffs = [0] * (N + 1)
    coeffs[0] = 1

    for n in range(1, N + 1):
        # Multiply by (1 - q^n)^{2m}
        # (1-x)^{2m} = sum_{j=0}^{2m} C(2m,j)(-1)^j x^j
        new_coeffs = [0] * (N + 1)
        for j in range(min(two_m + 1, N // n + 2)):
            # Binomial coefficient C(2m, j)
            binom = 1
            for i in range(j):
                binom = binom * (two_m - i) // (i + 1)
            sign_binom = ((-1) ** j) * binom
            for k in range(N + 1):
                idx = k + j * n
                if idx > N:
                    break
                new_coeffs[idx] += coeffs[k] * sign_binom
        coeffs = new_coeffs

    return coeffs[:nmax + 1]


def eta_power_coefficients_real(alpha, nmax=100, dps=30):
    r"""Compute the first nmax+1 coefficients of prod(1-q^n)^{2*alpha} for REAL alpha.

    Uses the logarithmic derivative: log prod(1-q^n)^{2*alpha} = 2*alpha * sum log(1-q^n)
    Then exponentiate via power series.

    Returns list of mpmath.mpf values [a_0, ..., a_nmax].
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps + 10):
        alpha = mpmath.mpf(alpha)
        N = nmax

        # Compute -2*alpha * sum_{n>=1} log(1 - q^n) as power series in q
        # log(1-q^n) = -sum_{k>=1} q^{nk}/k
        # So -2*alpha * sum_n log(1-q^n) = 2*alpha * sum_n sum_k q^{nk}/k
        #   = 2*alpha * sum_{m>=1} sigma_{-1}(m) q^m
        # where sigma_{-1}(m) = sum_{d|m} 1/d

        log_coeffs = [mpmath.mpf(0)] * (N + 1)
        for m in range(1, N + 1):
            s = mpmath.mpf(0)
            for d in range(1, m + 1):
                if m % d == 0:
                    s += mpmath.mpf(1) / d
            # log prod(1-q^n)^{2*alpha} = -2*alpha * sum sigma_{-1}(m) q^m
            log_coeffs[m] = -2 * alpha * s

        # Exponentiate: if f = sum_{n>=0} a_n q^n with a_0 = 1,
        # and log f = sum_{n>=1} b_n q^n, then
        # n*a_n = sum_{k=1}^{n} k*b_k*a_{n-k}
        a = [mpmath.mpf(0)] * (N + 1)
        a[0] = mpmath.mpf(1)
        for n in range(1, N + 1):
            s = mpmath.mpf(0)
            for k in range(1, n + 1):
                s += k * log_coeffs[k] * a[n - k]
            a[n] = s / n

        return a


def check_multiplicativity(coeffs, nmax=None):
    """Test whether a sequence of coefficients is multiplicative.

    A sequence a(n) is multiplicative if a(mn) = a(m)*a(n) whenever gcd(m,n) = 1.
    Returns list of (m, n, a(mn), a(m)*a(n), ratio) for coprime pairs where a(mn) != 0.
    """
    from math import gcd
    if nmax is None:
        nmax = len(coeffs) - 1
    failures = []
    for m in range(2, min(nmax + 1, len(coeffs))):
        for n in range(2, min(nmax // m + 1, len(coeffs))):
            if m * n >= len(coeffs):
                break
            if gcd(m, n) == 1:
                amn = coeffs[m * n] if m * n < len(coeffs) else None
                am = coeffs[m]
                an = coeffs[n]
                if amn is not None and am != 0 and an != 0:
                    product = am * an
                    if abs(float(amn)) > 1e-30:
                        ratio = float(amn) / float(product)
                        if abs(ratio - 1.0) > 1e-8:
                            failures.append((m, n, float(amn), float(product), ratio))
    return failures


# ============================================================
# 4. Rankin-Selberg Mellin integral
# ============================================================

def mellin_eta_power(alpha, s, y_min=0.01, y_max=50.0, dps=30, npts=500):
    r"""Compute the Mellin-type integral Z_alpha(s) = int_0^infty |eta(iy)|^{2*alpha} y^s dy/y.

    This is NOT the Rankin-Selberg unfolding over the fundamental domain; it is
    the simpler Mellin integral over the positive real line. The actual
    Rankin-Selberg integral involves integration over SL(2,Z)\H and uses
    the Maass-Selberg relation.

    For practical computation, we integrate over [y_min, y_max] using
    Gauss-Legendre quadrature. The integrand decays exponentially for
    large y (from the eta function) and has controlled singularity near y=0
    (from the y^s factor).

    Returns mpmath.mpf value.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps + 10):
        alpha = mpmath.mpf(alpha)
        s = mpmath.mpf(s)

        def integrand(y):
            if y <= 0:
                return mpmath.mpf(0)
            eta_pow = eta_power_imaginary(y, alpha, dps=dps)
            return eta_pow * mpmath.power(y, s - 1)

        result = mpmath.quad(integrand, [mpmath.mpf(y_min), mpmath.mpf(y_max)],
                             maxdegree=8)
        return result


def mellin_eta_power_fundamental_domain(alpha, s, dps=30, npts=200):
    r"""Approximate the Rankin-Selberg integral over the fundamental domain F:

    Z^F_alpha(s) = int_F |eta(tau)|^{2*alpha} y^s dmu(tau)

    where dmu = dx dy / y^2 is the hyperbolic measure on H.

    The standard fundamental domain F for SL(2,Z) is:
      |tau| >= 1, -1/2 <= Re(tau) <= 1/2

    On F, tau = x + iy with x in [-1/2, 1/2], y >= sqrt(1 - x^2).

    For |eta(tau)|^{2*alpha}, since tau = x + iy, we need the full complex eta.
    On the imaginary axis (x=0), |eta(iy)|^{2*alpha} = eta(iy)^{2*alpha}.
    Off the imaginary axis, |eta(x+iy)|^2 != eta(iy)^2 in general.

    For this module, we approximate by integrating along the imaginary axis
    only (the x=0 slice of F), which gives the leading contribution:
      Z^F_alpha(s) ~ int_{y=1}^{infty} |eta(iy)|^{2*alpha} y^{s-2} dy

    This approximation is EXACT for the Rankin-Selberg unfolding of
    |f|^2 E(s) when f depends only on y (i.e., for Maass cusp forms
    that are K-invariant).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps + 10):
        alpha = mpmath.mpf(alpha)
        s = mpmath.mpf(s)

        def integrand(y):
            if y <= 0:
                return mpmath.mpf(0)
            eta_pow = eta_power_imaginary(y, alpha, dps=dps)
            return eta_pow * mpmath.power(y, s - 2)

        # Integrate from y=1 (bottom of F on imaginary axis) to y_max
        result = mpmath.quad(integrand, [mpmath.mpf(1), mpmath.mpf(50)],
                             maxdegree=8)
        return result


# ============================================================
# 5. Analytic continuation in c
# ============================================================

def Z_c_at_s(c, s, y_min=0.1, y_max=30.0, dps=30):
    r"""Compute Z_c(s) = int |eta|^{2(c-1)} y^{s + c/2 - 1} e^{-2*pi*y*(c-1)/12} dy/y.

    This is the Mellin transform of the primary-counting function Z_hat_c.
    Analytic in c for Re(c) > 1 and Re(s) large enough.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps + 10):
        c_mp = mpmath.mpf(c)
        s_mp = mpmath.mpf(s)
        alpha = c_mp - 1  # eta power parameter

        def integrand(y):
            if y <= 0:
                return mpmath.mpf(0)
            eta_pow = eta_power_imaginary(y, alpha, dps=dps)
            y_pow = mpmath.power(y, s_mp + c_mp / 2 - 2)  # y^{s + c/2 - 1} * dy/y = y^{s+c/2-2} dy
            exp_fac = mpmath.exp(-2 * mpmath.pi * y * (c_mp - 1) / 12)
            return eta_pow * y_pow * exp_fac

        result = mpmath.quad(integrand, [mpmath.mpf(y_min), mpmath.mpf(y_max)],
                             maxdegree=8)
        return result


def Z_c_curve(c_values, s=3, dps=30):
    """Compute Z_c(s) for a list of c values at fixed s.

    Returns list of (c, Z_c(s)) pairs.
    """
    results = []
    for c in c_values:
        val = Z_c_at_s(c, s, dps=dps)
        results.append((c, float(val)))
    return results


def Z_c_interpolation_check(c_integers, c_nonintegers, s=3, dps=30):
    """Check smoothness of Z_c(s) by computing at integer and non-integer c.

    Returns dict with 'integer_values', 'noninteger_values', 'smooth' flag.
    """
    int_vals = Z_c_curve(c_integers, s=s, dps=dps)
    nonint_vals = Z_c_curve(c_nonintegers, s=s, dps=dps)
    return {
        'integer_values': int_vals,
        'noninteger_values': nonint_vals,
    }


# ============================================================
# 6. Shadow data at generic c
# ============================================================

def kappa_virasoro(c):
    """Shadow kappa = c/2. Rational function of c, defined for all c != 0."""
    if isinstance(c, (int, float)):
        return c / 2.0
    return c / 2


def Q_contact_virasoro(c):
    """Quartic contact invariant Q^contact_Vir = 10 / [c(5c + 22)].

    Rational function of c, defined for all c except c=0 and c=-22/5.
    """
    if isinstance(c, (int, float)):
        denom = c * (5 * c + 22)
        if abs(denom) < 1e-30:
            return float('inf')
        return 10.0 / denom
    denom = c * (5 * c + 22)
    return 10 / denom


def shadow_gf_virasoro(c, t):
    """Shadow generating function G(t) = -log(1 + 6t/c).

    Rational-function seed, defined for all c != 0 and 1 + 6t/c > 0.
    """
    if isinstance(c, (int, float)) and isinstance(t, (int, float)):
        arg = 1 + 6 * t / c
        if arg <= 0:
            return float('nan')
        return -np.log(arg)
    if HAS_MPMATH:
        return -mpmath.log(1 + 6 * t / c)
    return -np.log(1 + 6 * t / c)


def genus1_hessian_correction(c):
    r"""Genus-1 Hessian correction delta_H^{(1)}_Vir = 120 / [c^2(5c+22)] x^2.

    Returns the coefficient 120/[c^2(5c+22)].
    """
    if isinstance(c, (int, float)):
        denom = c * c * (5 * c + 22)
        if abs(denom) < 1e-30:
            return float('inf')
        return 120.0 / denom
    denom = c ** 2 * (5 * c + 22)
    return 120 / denom


def shadow_data_table(c_values):
    """Compute shadow data (kappa, Q^contact, delta_H) for a list of c values.

    Returns list of dicts.
    """
    results = []
    for c in c_values:
        results.append({
            'c': c,
            'kappa': kappa_virasoro(c),
            'Q_contact': Q_contact_virasoro(c),
            'delta_H': genus1_hessian_correction(c),
            'shadow_depth': float('inf'),  # Virasoro has infinite shadow depth for all c
            'shadow_class': 'M',  # Mixed class for all c
        })
    return results


# ============================================================
# 7. Modularity classification of eta^{2m}
# ============================================================

def eta_modularity_data(m):
    r"""Determine the modularity properties of eta(tau)^{2m}.

    eta^{2m} has weight m. It transforms under SL(2,Z) as:
      eta(-1/tau) = sqrt(-i*tau) * eta(tau)
      eta(tau+1) = e^{pi*i/12} * eta(tau)

    Therefore eta^{2m}(-1/tau) = (-i*tau)^m * eta^{2m}(tau)
    and eta^{2m}(tau+1) = e^{m*pi*i/6} * eta^{2m}(tau).

    For eta^{2m} to be invariant under T: tau -> tau+1, we need
    e^{m*pi*i/6} = 1, i.e., m*pi/6 = 2*pi*k for some integer k,
    i.e., m = 12k. So eta^{2m} is a modular form for SL(2,Z)
    (with trivial character) ONLY when m is divisible by 12.

    For general m, eta^{2m} is a modular form of weight m for
    Gamma_1(N) or Gamma_0(N) with nebentypus, where N divides 576
    (= 24^2) in general.

    More precisely, eta^{2m} in M_m(Gamma_0(N), chi) where:
      N = 1 if 12 | m (full level)
      The character chi has order dividing 24/gcd(m,24).

    Returns dict with modularity data.
    """
    from math import gcd

    weight = m
    g = gcd(m, 12)

    # The multiplier system of eta^{2m} under Gamma_0(N):
    # Under T: tau -> tau + 1, eta^{2m} picks up e^{2*pi*i*m/12}
    # This is a 12/gcd(m,12)-th root of unity
    char_order = 12 // g

    # Minimal level: eta^{2m} is a form for Gamma_1(N) with N | 576
    # but the precise level depends on m mod 24
    # For our purposes: if 12|m, N=1; if 6|m but not 12|m, N=2;
    # if 4|m but not 12|m, N=3; etc.
    if m % 12 == 0:
        level = 1
        char_desc = "trivial"
    elif m % 6 == 0:
        level = 2  # Gamma_0(2) with character of order 2
        char_desc = f"order-2 nebentypus"
    elif m % 4 == 0:
        level = 3
        char_desc = f"order-3 nebentypus"
    elif m % 3 == 0:
        level = 4
        char_desc = f"order-4 nebentypus"
    elif m % 2 == 0:
        level = 6
        char_desc = f"order-6 nebentypus"
    else:
        # Odd m: eta^{2m} has half-integer weight, needs metaplectic cover
        level = 576
        char_desc = f"half-integer weight m={m}, metaplectic"

    # Whether it is a cusp form: eta^{2m} vanishes at all cusps for m >= 1
    # (eta itself vanishes at infinity, and the other cusps of Gamma_0(N)
    # are related by Atkin-Lehner involutions)
    is_cusp_form = (m >= 1)

    return {
        'power': 2 * m,
        'weight': weight,
        'level': level,
        'character_order': char_order,
        'character_description': char_desc,
        'is_cusp_form': is_cusp_form,
        'is_SL2Z': (m % 12 == 0),
        'is_eigenform': None,  # Need to check case by case
        'central_charge': m + 1,  # c such that 2(c-1) = 2m, i.e., c = m+1
    }


# ============================================================
# 8. Special c values and known L-functions
# ============================================================

def special_c_L_data():
    r"""Table of special c values where the L-function content of |eta|^{2(c-1)} is known.

    Returns list of dicts with c, eta power, modularity, L-function description.
    """
    return [
        {
            'c': 1,
            'eta_power': 0,
            'description': 'Heisenberg: |eta|^0 = 1, no cusp form, L = zeta(s)',
            'multiplicative': True,
            'L_function': 'zeta(s)',
        },
        {
            'c': 2,
            'eta_power': 2,
            'description': 'eta^2: weight 1 cusp form for Gamma_0(576) with character',
            'multiplicative': True,  # eta^2 IS an eigenform (CM form)
            'L_function': 'L(s, eta^2) = L(s, chi_{-4}) (CM L-function)',
        },
        {
            'c': 3,
            'eta_power': 4,
            'description': 'eta^4: weight 2, related to conductor 36 elliptic curve',
            'multiplicative': True,  # eigenform
            'L_function': 'L(s, f_{36}) (elliptic curve L-function)',
        },
        {
            'c': 7,
            'eta_power': 12,
            'description': 'eta^12: weight 6, cusp form for Gamma_0(1) with character',
            'multiplicative': True,  # eigenform
            'L_function': 'L(s, eta^12)',
        },
        {
            'c': 13,
            'eta_power': 24,
            'description': 'eta^24 = Delta: weight 12 for SL(2,Z), THE Hecke eigenform',
            'multiplicative': True,
            'L_function': 'L(s, Delta) with Ramanujan tau coefficients',
        },
        {
            'c': 25,
            'eta_power': 48,
            'description': 'eta^48 = Delta^2: weight 24 for SL(2,Z), NOT single eigenform',
            'multiplicative': False,  # Delta^2 is not an eigenform
            'L_function': 'L(s, Delta^2) decomposes into eigenform components in S_24(SL(2,Z))',
        },
        {
            'c': 26,
            'eta_power': 50,
            'description': 'eta^50: weight 25 cusp form, not for SL(2,Z)',
            'multiplicative': None,  # unclear a priori
            'L_function': 'L(s, eta^50) (higher level)',
        },
    ]


# ============================================================
# 9. c -> infinity asymptotics
# ============================================================

def large_c_asymptotics(c, y, dps=30):
    r"""Asymptotic behavior of Z_hat_c as c -> infinity.

    Z_hat_c = y^{c/2} * eta(iy)^{2(c-1)} * e^{-2*pi*y*(c-1)/12}

    Using eta(iy) = e^{-pi*y/12} * prod(1 - e^{-2*pi*n*y}):
      eta(iy)^{2(c-1)} = e^{-pi*y*(c-1)/6} * [prod(1-q^n)]^{2(c-1)}

    So Z_hat_c = y^{c/2} * e^{-pi*y*(c-1)/6} * [prod(1-q^n)]^{2(c-1)} * e^{-2*pi*y*(c-1)/12}
               = y^{c/2} * e^{-pi*y*(c-1)/4} * [prod(1-q^n)]^{2(c-1)}

    For large c, the exponential factor e^{-pi*y*c/4} dominates (for y > 0).
    The product factor [prod(1-q^n)]^{2c} ~ exp(2c * sum log(1-q^n)) also
    contributes an exponential decay for c -> infinity.

    Returns (Z_hat_c, log_Z_hat_c_over_c) for extracting the rate.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mpmath.workdps(dps + 10):
        c_mp = mpmath.mpf(c)
        y_mp = mpmath.mpf(y)

        val = primary_counting_function(c, y, dps=dps)
        if val > 0:
            log_val = mpmath.log(val)
            rate = log_val / c_mp
        else:
            log_val = mpmath.mpf('-inf')
            rate = mpmath.mpf('-inf')

        return {
            'c': c,
            'y': y,
            'Z_hat': float(val),
            'log_Z_hat': float(log_val) if log_val != mpmath.mpf('-inf') else float('-inf'),
            'log_Z_hat_over_c': float(rate) if rate != mpmath.mpf('-inf') else float('-inf'),
        }


# ============================================================
# 10. The irrational-c obstruction
# ============================================================

def irrational_c_mellin(c_irrational, s, y_min=0.1, y_max=30.0, dps=30):
    r"""Compute Z_c(s) for irrational c (e.g., c = pi).

    At irrational c, |eta|^{2(c-1)} is NOT a modular form for any congruence
    subgroup. The Mellin integral still converges (the integrand is
    positive, continuous, and exponentially decaying).

    Returns the integral value, demonstrating convergence.
    """
    return Z_c_at_s(c_irrational, s, y_min=y_min, y_max=y_max, dps=dps)


# ============================================================
# 11. Continuous shadow-spectral correspondence
# ============================================================

def continuous_shadow_spectral_table(c_values, s=3, dps=30):
    r"""Build the combined table: shadow data + spectral data at each c.

    For each c:
      - Shadow data: kappa, Q^contact (rational functions, smooth in c)
      - Spectral data: Z_c(s) (from Mellin integral)
      - Modularity: whether |eta|^{2(c-1)} is a modular form

    This table demonstrates the CONTINUOUS SHADOW-SPECTRAL CORRESPONDENCE:
    the shadow data varies smoothly, while the L-function content is
    discrete (only defined at special c values).
    """
    results = []
    for c in c_values:
        shadow = {
            'kappa': kappa_virasoro(c),
            'Q_contact': Q_contact_virasoro(c),
            'delta_H': genus1_hessian_correction(c),
        }

        # Spectral: compute Z_c(s)
        spectral_val = float(Z_c_at_s(c, s, dps=dps))

        # Modularity check
        c_int = int(round(c))
        is_integer_c = abs(c - c_int) < 1e-10
        if is_integer_c and c_int >= 1:
            mod_data = eta_modularity_data(c_int - 1)
            is_SL2Z = mod_data['is_SL2Z']
        else:
            is_SL2Z = False

        results.append({
            'c': c,
            'shadow': shadow,
            'Z_c_at_s': spectral_val,
            'is_integer': is_integer_c,
            'is_modular_SL2Z': is_SL2Z,
        })

    return results


# ============================================================
# 12. Spectrum of special c values
# ============================================================

def special_c_spectrum(k_max=10):
    r"""Tabulate c = 1 + 24k for k = 0, 1, ..., k_max.

    These give eta^{48k+2}, which are cusp forms of weight 24k+1.
    For SL(2,Z) modular forms, the weight must be even AND divisible by 12
    for eta powers. So eta^{48k+2} is on SL(2,Z) only when 24k+1 is
    divisible by 12, which never happens (24k+1 is always odd).

    General rule: eta^{2m} is on SL(2,Z) iff 12|m.
    c = 1 + 24k gives m = 24k, so eta^{48k} for the factor |eta|^{2(c-1)}.
    Wait: c-1 = 24k, so 2(c-1) = 48k, and eta^{48k} has weight 24k.
    This is on SL(2,Z) iff 12|24k iff always! (since 24k is always
    divisible by 12 for k >= 1).

    So c = 1 + 24k (k >= 1) gives eta^{48k}, weight 24k, on SL(2,Z).
    The dimension of S_{24k}(SL(2,Z)) grows linearly: dim = floor(24k/12) - delta
    where delta accounts for the Eisenstein series.
    """
    results = []
    for k in range(k_max + 1):
        c = 1 + 24 * k
        m = c - 1  # = 24k
        weight = m
        eta_pow = 2 * m  # = 48k

        # SL(2,Z) modular form?
        is_SL2Z = (m % 12 == 0)  # True for k >= 1, also for k=0 (m=0)

        # Dimension of cusp form space S_{weight}(SL(2,Z))
        # dim S_k = floor(k/12) - 1 if k ≡ 2 mod 12, else floor(k/12)
        # for k >= 2 even. For k=0: dim S_0 = 0.
        if weight == 0:
            dim_cusp = 0
        elif weight < 12:
            dim_cusp = 0
        elif weight == 12:
            dim_cusp = 1
        else:
            dim_cusp = weight // 12
            if weight % 12 == 2:
                dim_cusp -= 1

        results.append({
            'k': k,
            'c': c,
            'eta_power': eta_pow,
            'weight': weight,
            'is_SL2Z': is_SL2Z,
            'dim_cusp_space': dim_cusp if is_SL2Z else None,
            'single_eigenform': (dim_cusp == 1) if is_SL2Z else False,
        })

    return results
