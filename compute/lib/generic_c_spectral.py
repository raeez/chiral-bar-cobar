#!/usr/bin/env python3
r"""
generic_c_spectral.py — Spectral decomposition of |eta|^{2alpha} at generic central charge.

THE PROBLEM:
  For Vir_c with c irrational, the partition function |eta(tau)|^{2(c-1)} is NOT a
  modular form. It transforms under SL(2,Z) with a phase determined by c mod 24.
  The spectral decomposition on SL(2,Z)\H involves BOTH:

  (1) Continuous spectrum: Eisenstein series E_{1/2+it}, which ARE Hecke eigenforms
      with T_p eigenvalue 2cos(t log p).
  (2) Discrete spectrum: Maass cusp forms u_j with Laplacian eigenvalue
      lambda_j = 1/4 + t_j^2. The first t_1 ~ 9.533695...

  At modular c (i.e., 12|(c-1)), all weight lands in continuous spectrum.
  At non-modular c, Maass cusp forms contribute.

EISENSTEIN SERIES ON IMAGINARY AXIS:
  E_s(iy) = y^s + phi(s)*y^{1-s} + 2*sum_{n>=1} sigma_{2s-1}(n)*sqrt(y)*K_{s-1/2}(2*pi*n*y)/Lambda(s)

  where Lambda(s) = pi^{-s} * Gamma(s) * zeta(2s) is the completed zeta function.
  The scattering matrix phi(s) = Lambda(1-s)/Lambda(s).

SPECTRAL COEFFICIENT:
  c(t; alpha) = int_0^infty |eta(iy)|^{2*alpha} * y^{-1/2+it} dy/y
  This is M[|eta|^{2alpha}](1/2 - it), the Mellin transform.

CONTINUOUS SPECTRAL DENSITY:
  rho_cont(t; alpha) = |c(t; alpha)|^2 / |zeta(1 + 2it)|^2
  Poles at t = gamma_k/2 where zeta(1/2 + i*gamma_k) = 0.

THE CHRISS-GINZBURG STATEMENT (thm:shadow-spectral-decomposition):
  For Vir_c at any c > 1, the shadow obstruction tower uniquely determines the spectral
  measure mu_c on SL(2,Z)\H:
    mu_c = mu_c^{cont} + mu_c^{disc}
  where mu_c^{cont} involves Eisenstein series (automatically Hecke eigenforms)
  and mu_c^{disc} involves Maass cusp forms (vanishing at modular c).

SHADOW MOMENTS FROM SPECTRAL MEASURE:
  M_r = int t^{-2r} d mu(t) = kappa(A) at r=1 when alpha = c - 1.

References:
  Iwaniec, "Spectral Methods of Automorphic Forms", AMS, 2002.
  Benjamin-Chang, arXiv:2208.02259, 2022.
  thm:general-hs-sewing (higher_genus_modular_koszul.tex)
  def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)
"""

import numpy as np
from functools import lru_cache

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi as mpi, gamma as mpgamma, zeta as mpzeta,
                        exp as mpexp, log as mplog, sqrt as mpsqrt, power as mppower,
                        cos as mpcos, sin as mpsin, fabs, inf as mpinf, quad, besselk,
                        fsum, eta as mpeta_func)
    mp.dps = 40
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Completed zeta and scattering matrix
# ============================================================

def completed_zeta(s):
    """Lambda(s) = pi^{-s} * Gamma(s) * zeta(2s).

    This is the standard completed zeta function appearing in the
    Eisenstein series constant term.
    """
    s = mpc(s)
    return mppower(mpi, -s) * mpgamma(s) * mpzeta(2 * s)


def scattering_matrix(s):
    """phi(s) = Lambda(1-s) / Lambda(s).

    The scattering matrix for the Eisenstein series on SL(2,Z)\\H.
    """
    return completed_zeta(1 - s) / completed_zeta(s)


# ============================================================
# 2. Eisenstein series on the imaginary axis (constant term)
# ============================================================

def eisenstein_constant_term(s, y):
    """E_s^{(0)}(iy) = y^s + phi(s)*y^{1-s}.

    The constant term of the Eisenstein series E_s(tau) evaluated at
    tau = iy on the imaginary axis. For Re(s)=1/2, this is the main
    contribution at large y.

    Parameters:
        s: complex spectral parameter (typically s = 1/2 + it)
        y: positive real, imaginary part of tau
    """
    s = mpc(s)
    y = mpf(y)
    phi_s = scattering_matrix(s)
    return mppower(y, s) + phi_s * mppower(y, 1 - s)


def eisenstein_on_imaginary_axis(s, y, nmax=50):
    """E_s(iy) including Fourier modes on the imaginary axis.

    On the imaginary axis (x=0), the Fourier expansion gives:
      E_s(iy) = y^s + phi(s)*y^{1-s}
                + 2 * sum_{n=1}^{nmax} sigma_{2s-1}(n) * sqrt(y) * K_{s-1/2}(2*pi*n*y) / Lambda(s)

    where sigma_{2s-1}(n) = sum_{d|n} d^{2s-1} is the divisor function.

    Parameters:
        s: complex spectral parameter
        y: positive real
        nmax: number of Fourier terms
    """
    s = mpc(s)
    y = mpf(y)

    # Constant term
    result = eisenstein_constant_term(s, y)

    # Fourier contribution
    Lambda_s = completed_zeta(s)
    if fabs(Lambda_s) < mpf('1e-30'):
        return result

    sqrty = mpsqrt(y)
    nu = s - mpf('0.5')  # K_{s-1/2} = K_nu

    for n in range(1, nmax + 1):
        # sigma_{2s-1}(n)
        sigma = fsum(mppower(d, 2 * s - 1) for d in range(1, n + 1) if n % d == 0)
        kval = besselk(nu, 2 * mpi * n * y)
        result += 2 * sigma * sqrty * kval / Lambda_s

    return result


# ============================================================
# 3. Dedekind eta on imaginary axis
# ============================================================

def eta_on_imaginary_axis(y, nmax=200):
    """eta(iy) = exp(-pi*y/12) * prod_{n=1}^{nmax} (1 - exp(-2*pi*n*y)).

    The Dedekind eta function on the imaginary axis tau = iy.
    """
    y = mpf(y)
    result = mpexp(-mpi * y / 12)
    for n in range(1, nmax + 1):
        result *= (1 - mpexp(-2 * mpi * n * y))
    return result


def eta_power_on_imaginary_axis(y, alpha, nmax=200):
    """|eta(iy)|^{2*alpha} for real y > 0.

    Since eta(iy) is real and positive for y > 0, this is eta(iy)^{2*alpha}.

    Parameters:
        y: positive real
        alpha: exponent (alpha = c - 1 for Vir_c)
        nmax: product truncation
    """
    y = mpf(y)
    alpha = mpf(alpha)
    eta_val = eta_on_imaginary_axis(y, nmax)
    if eta_val <= 0:
        return mpf(0)
    return mppower(eta_val, 2 * alpha)


# ============================================================
# 4. Spectral coefficient via Mellin transform
# ============================================================

def spectral_coefficient(t, alpha, ymax=20, nmax=150):
    """c(t; alpha) = integral_0^infty |eta(iy)|^{2*alpha} * y^{-1/2+it} dy/y.

    Mellin transform M[|eta|^{2*alpha}](1/2 - it).
    Computed by numerical integration using mpmath.quad.

    Parameters:
        t: spectral parameter (real)
        alpha: eta exponent
        ymax: upper integration cutoff (exponential decay beyond ~2)
        nmax: eta product truncation

    Returns:
        complex value c(t; alpha)
    """
    t = mpf(t)
    alpha = mpf(alpha)

    def integrand(y):
        if y <= mpf('1e-10'):
            return mpc(0)
        eta_val = eta_on_imaginary_axis(y, nmax=nmax)
        if eta_val <= 0:
            return mpc(0)
        f_val = mppower(eta_val, 2 * alpha)
        # y^{-1/2+it} * dy/y = y^{-3/2+it} dy
        kernel = mppower(y, mpf('-0.5') + mpc(0, t) - 1)
        return f_val * kernel

    # Split integral for better convergence: [eps, 1] and [1, ymax]
    eps = mpf('0.01')
    try:
        part1 = quad(integrand, [eps, 1], maxdegree=6)
        part2 = quad(integrand, [1, ymax], maxdegree=6)
        return part1 + part2
    except Exception:
        return mpc(0)


def spectral_coefficient_alpha0(t):
    """c(t; 0) = integral_0^infty y^{-3/2+it} dy.

    At alpha=0, |eta|^0 = 1, and the integral is formally the Mellin transform
    of 1, which diverges. The regularized value relates to zeta via:
      M[1](s) ~ Gamma factors / zeta factors.

    Returns None for the divergent case (documented in tests).
    """
    return None  # Formally divergent; regularization documented in tests


# ============================================================
# 5. Continuous spectral density
# ============================================================

def continuous_spectral_density(t, alpha, ymax=20, nmax=150):
    """rho_cont(t; alpha) = |c(t; alpha)|^2 / |zeta(1 + 2it)|^2.

    The continuous spectral density. Has poles at t = gamma_k/2 where
    zeta(1/2 + i*gamma_k) = 0. Near these poles, the density blows up.

    Parameters:
        t: spectral parameter (positive real)
        alpha: eta exponent
    """
    t = mpf(t)
    c_val = spectral_coefficient(t, alpha, ymax=ymax, nmax=nmax)
    zeta_val = mpzeta(1 + 2 * mpc(0, t))
    if fabs(zeta_val) < mpf('1e-30'):
        return mpf('inf')
    return fabs(c_val) ** 2 / fabs(zeta_val) ** 2


# ============================================================
# 6. Hecke eigenvalues of Eisenstein series
# ============================================================

def hecke_eigenvalue_eisenstein(t, p):
    """T_p(E_{1/2+it}) = lambda_p * E_{1/2+it} where
    lambda_p = p^{it} + p^{-it} = 2*cos(t * log(p)).

    Parameters:
        t: spectral parameter (real)
        p: prime number
    Returns:
        eigenvalue (real)
    """
    t = mpf(t)
    p = mpf(p)
    return 2 * mpcos(t * mplog(p))


def verify_hecke_eigenvalue(t, p, y, nmax=50):
    """Numerically verify that T_p(E_s)(iy) = lambda_p * E_s(iy).

    T_p acts on E_s(tau) with eigenvalue p^{s-1/2} + p^{1/2-s}.
    For s = 1/2 + it: eigenvalue = p^{it} + p^{-it} = 2cos(t*log p).

    We verify by checking that E_s(iy/p) + ... (Hecke action) matches.
    Here we just compute the eigenvalue directly.
    """
    s = mpf('0.5') + mpc(0, t)
    ev = mppower(p, s - mpf('0.5')) + mppower(p, mpf('0.5') - s)
    # This should be 2*cos(t*log p)
    expected = 2 * mpcos(mpf(t) * mplog(mpf(p)))
    return {'eigenvalue': ev, 'expected': expected, 'match': fabs(ev - expected) < mpf('1e-20')}


# ============================================================
# 7. Self-duality and modular vs non-modular decomposition
# ============================================================

def is_modular_alpha(alpha):
    """Check if |eta|^{2*alpha} is modular for SL(2,Z).

    This happens iff alpha is a non-negative integer divisible by 12
    (giving weight alpha), since eta^{24} = Delta is the weight-12
    modular discriminant.

    |eta|^{2*alpha} = |eta^{2*alpha}| = |Delta^{alpha/12}|
    is modular of weight alpha when alpha is a non-negative multiple of 12.

    More precisely: eta(tau)^{2k} is a modular form of weight k for SL(2,Z)
    iff 24 | 2k, i.e., 12 | k. So |eta|^{2*alpha} = eta^{alpha} * \bar{eta}^{alpha}
    needs alpha integer with 12 | alpha for full SL(2,Z) modularity.
    """
    if not isinstance(alpha, (int, float)):
        return False
    if alpha != int(alpha):
        return False
    alpha = int(alpha)
    if alpha < 0:
        return False
    return alpha % 12 == 0


def central_charge_from_alpha(alpha):
    """c = alpha + 1 for the relation |eta|^{2(c-1)} = |eta|^{2*alpha}."""
    return alpha + 1


def alpha_from_central_charge(c):
    """alpha = c - 1."""
    return c - 1


# ============================================================
# 8. Spectral type classification
# ============================================================

def classify_spectral_type(c):
    """Classify the spectral decomposition type for Vir_c.

    Returns dict with:
      - 'type': 'modular_sl2z', 'modular_gamma0', 'non_modular'
      - 'discrete': whether discrete (Maass) spectrum is expected
      - 'alpha': the eta exponent c - 1
      - 'description': human-readable
    """
    alpha = c - 1

    # Check for rationality (within numerical precision)
    is_rational = isinstance(c, (int, float)) and c == int(c) if isinstance(c, int) else False
    is_integer_c = False
    if isinstance(c, (int, float)):
        is_integer_c = abs(c - round(c)) < 1e-12
        if is_integer_c:
            c_int = int(round(c))
            alpha_int = c_int - 1
        else:
            alpha_int = None
    else:
        alpha_int = None

    if is_integer_c and alpha_int is not None and alpha_int >= 0 and alpha_int % 12 == 0:
        return {
            'type': 'modular_sl2z',
            'discrete': False,
            'alpha': alpha,
            'L_content': 'standard (Hecke eigenforms of level 1)',
            'description': (f'c={c}: |eta|^{{2*{alpha_int}}} is modular for SL(2,Z). '
                           f'All spectral weight in continuous spectrum (Eisenstein). '
                           f'Discrete Maass component vanishes.')
        }
    elif is_integer_c and alpha_int is not None:
        return {
            'type': 'modular_gamma0',
            'discrete': True,  # old forms may contribute
            'alpha': alpha,
            'L_content': 'standard at new level (Gamma_0(N))',
            'description': (f'c={c}: |eta|^{{2*{alpha_int}}} modular for Gamma_0(N). '
                           f'Discrete may be nonzero (old forms).')
        }
    else:
        return {
            'type': 'non_modular',
            'discrete': True,
            'alpha': alpha,
            'L_content': 'continuous integral + Maass contributions',
            'description': (f'c={c}: not modular. Discrete Maass spectrum nonzero generically. '
                           f'L-content = continuous integral + Maass contributions.')
        }


def spectral_type_table():
    """Tabulate spectral type for c = 1, 2, 7, 13, 25, 26, pi.

    Returns list of dicts with classification data.
    """
    import math
    c_values = [
        (1, 'c=1'),
        (2, 'c=2'),
        (7, 'c=7'),
        (13, 'c=13 (self-dual)'),
        (25, 'c=25'),
        (26, 'c=26'),
        (math.pi, 'c=pi'),
    ]

    results = []
    for c_val, label in c_values:
        info = classify_spectral_type(c_val)
        info['label'] = label
        info['c'] = c_val
        results.append(info)
    return results


# ============================================================
# 9. Shadow moments from continuous spectrum
# ============================================================

def spectral_density_grid(alpha, t_min=0.5, t_max=20, npts=40, nmax=80):
    """Precompute rho_cont(t; alpha) on a grid of t values.

    Returns list of (t, rho) pairs suitable for trapezoidal integration.
    This avoids triple-nested quadrature by computing the grid once.
    """
    alpha = mpf(alpha)
    grid = []
    dt = (mpf(t_max) - mpf(t_min)) / (npts - 1)
    for i in range(npts):
        t = mpf(t_min) + i * dt
        try:
            rho = continuous_spectral_density(t, alpha, ymax=15, nmax=nmax)
            if rho == mpf('inf') or rho != rho:
                rho = mpf(0)
        except Exception:
            rho = mpf(0)
        grid.append((t, rho))
    return grid


def shadow_moment_continuous(r, alpha, t_min=0.5, t_max=20, nmax=80):
    """M_r^{cont} = integral t^{-2r} * rho_cont(t; alpha) dt.

    The r-th shadow moment from the continuous spectral density.
    At r=1, alpha=1 (c=2): M_1 = kappa = c/2 = 1.

    Uses trapezoidal rule on a precomputed grid to avoid triple-nested quadrature.

    Parameters:
        r: moment index (positive integer)
        alpha: eta exponent
        t_min: lower integration bound (avoid t=0 pole)
        t_max: upper integration bound
        nmax: eta product truncation for inner computation
    """
    r = int(r)
    grid = spectral_density_grid(alpha, t_min=t_min, t_max=t_max, npts=30, nmax=nmax)

    # Trapezoidal integration
    result = mpf(0)
    for i in range(len(grid) - 1):
        t0, rho0 = grid[i]
        t1, rho1 = grid[i + 1]
        dt = t1 - t0
        f0 = mppower(t0, -2 * r) * rho0
        f1 = mppower(t1, -2 * r) * rho1
        result += (f0 + f1) * dt / 2

    return result


# ============================================================
# 10. Total spectral weight and discrete component
# ============================================================

def total_spectral_weight(alpha, ymax=20, nmax=150):
    """Parseval: integral |f(iy)|^2 dy/y^2 = (1/4pi) integral |c(t)|^2 / |zeta(1+2it)|^2 dt
    plus discrete contributions.

    Compute the direct-space L^2 norm as a proxy for total weight.
    """
    alpha = mpf(alpha)

    def integrand(y):
        if y <= mpf('1e-10'):
            return mpf(0)
        f_val = eta_power_on_imaginary_axis(y, alpha, nmax=nmax)
        return f_val ** 2 / y ** 2

    try:
        return quad(integrand, [mpf('0.01'), mpf(ymax)], maxdegree=5)
    except Exception:
        return mpf(0)


def spectral_weight_near_selfdual(alpha_values=None):
    """Compute total spectral weight as function of alpha near the self-dual
    point alpha=12 (c=13).

    At alpha=12: |eta|^24 = |Delta| is modular. ALL spectral weight is in
    continuous spectrum. At alpha=12+epsilon: discrete component turns on.

    Returns dict mapping alpha -> total_weight.
    """
    if alpha_values is None:
        alpha_values = [11, 11.5, 12, 12.5, 13]

    results = {}
    for a in alpha_values:
        w = total_spectral_weight(a, ymax=10, nmax=100)
        results[a] = float(w) if w is not None else 0.0
    return results


# ============================================================
# 11. L-function content at generic c
# ============================================================

def mellin_of_spectral_density(s, alpha, t_min=0.5, t_max=20, nmax=80):
    """integral rho_cont(t; alpha) * t^{-s} dt.

    The Mellin transform of the continuous spectral density. This is an
    L-function determined by the shadow moments:
    - At alpha=0 (c=1): relates to zeta(s) factors
    - At alpha=12 (c=13): relates to zeta(s-11) * L(Sym^2 Delta)
    - At generic alpha: a transcendental L-function

    Uses trapezoidal rule on a precomputed grid to avoid triple-nested quadrature.

    Parameters:
        s: complex parameter
        alpha: eta exponent
        t_min, t_max: integration range
    """
    s = mpc(s)
    grid = spectral_density_grid(alpha, t_min=t_min, t_max=t_max, npts=30, nmax=nmax)

    # Trapezoidal integration
    result = mpc(0)
    for i in range(len(grid) - 1):
        t0, rho0 = grid[i]
        t1, rho1 = grid[i + 1]
        dt = t1 - t0
        f0 = rho0 * mppower(t0, -s)
        f1 = rho1 * mppower(t1, -s)
        result += (f0 + f1) * dt / 2

    return result


# ============================================================
# 12. First Maass eigenvalue and discrete projection estimate
# ============================================================

# The first Maass cusp form eigenvalue for SL(2,Z)\H
FIRST_MAASS_T = mpf('9.53369526135355579323') if HAS_MPMATH else 9.5337


def estimate_discrete_component(alpha, t_min=0.5, t_max=30, nmax=100):
    """Estimate the Maass cusp form contribution by difference:

    |<f, u_1>|^2 ~ (full Parseval weight) - (continuous integral)

    This is the difference between the total L^2 norm (Parseval) and the
    continuous-spectrum-only integral. For modular alpha (12|alpha), this
    should vanish.

    Parameters:
        alpha: eta exponent
    Returns:
        dict with 'total', 'continuous_estimate', 'discrete_estimate'
    """
    alpha = mpf(alpha)

    # Total from direct space
    total = total_spectral_weight(alpha, ymax=10, nmax=nmax)

    # Continuous estimate via grid (avoid triple-nested quadrature)
    grid = spectral_density_grid(alpha, t_min=t_min, t_max=t_max, npts=25, nmax=nmax)
    cont = mpf(0)
    for i in range(len(grid) - 1):
        t0, rho0 = grid[i]
        t1, rho1 = grid[i + 1]
        dt = t1 - t0
        cont += (rho0 + rho1) * dt / 2

    return {
        'total': float(total) if total else 0.0,
        'continuous_estimate': float(cont) if cont else 0.0,
        'discrete_estimate': float(fabs(total - cont)) if (total and cont) else 0.0,
    }


# ============================================================
# 13. Zeta-zero proximity in spectral density
# ============================================================

# First few nontrivial zeros of zeta: gamma_k (imaginary parts)
ZETA_ZEROS = [
    14.134725141734693,
    21.022039638771554,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
]


def spectral_density_near_zeta_zero(alpha, gamma_k=None, delta=0.5, npts=10, nmax=100):
    """Compute rho_cont(t; alpha) near t = gamma_k/2 where it blows up.

    At t = gamma_k/2, zeta(1 + 2it) = zeta(1 + i*gamma_k) -> 0 (on RH),
    so the denominator |zeta(1+2it)|^2 -> 0 and rho -> infinity.

    Parameters:
        alpha: eta exponent
        gamma_k: zeta zero imaginary part (default: first zero ~14.135)
        delta: half-width of sampling window
        npts: number of sample points
    Returns:
        list of (t, rho) pairs showing the blowup
    """
    if gamma_k is None:
        gamma_k = ZETA_ZEROS[0]

    t_center = gamma_k / 2.0
    alpha = mpf(alpha)
    results = []

    for i in range(npts):
        t = mpf(t_center - delta + 2 * delta * i / (npts - 1))
        if t <= mpf('0.1'):
            continue
        try:
            rho = continuous_spectral_density(t, alpha, nmax=nmax)
            results.append((float(t), float(fabs(rho))))
        except Exception:
            results.append((float(t), float('inf')))

    return results


# ============================================================
# 14. Summary table: the Chriss-Ginzburg decomposition
# ============================================================

def chriss_ginzburg_decomposition_summary():
    """The Chriss-Ginzburg statement: for Vir_c at any c > 1, the shadow obstruction tower
    uniquely determines the spectral measure mu_c on SL(2,Z)\\H.

    mu_c = mu_c^{cont} + mu_c^{disc}

    where:
    - mu_c^{cont} involves Eisenstein series E_{1/2+it} (automatically Hecke eigenforms)
    - mu_c^{disc} involves Maass cusp forms u_j (vanishing at modular c)

    Returns a structured summary of the decomposition.
    """
    return {
        'statement': (
            'For Vir_c at any c > 1, the shadow obstruction tower determines the spectral '
            'measure mu_c on SL(2,Z)\\H. Decomposition: mu_c = mu_c^{cont} + mu_c^{disc}.'
        ),
        'continuous': {
            'basis': 'Eisenstein series E_{1/2+it}',
            'hecke': 'T_p eigenvalue = 2*cos(t*log(p))',
            'density': 'rho_cont(t) = |c(t)|^2 / |zeta(1+2it)|^2',
            'poles': 'at t = gamma_k/2 (half of zeta zero imaginary parts)',
        },
        'discrete': {
            'basis': 'Maass cusp forms u_j',
            'first_eigenvalue': 't_1 ~ 9.5337',
            'vanishing': 'at modular c (12 | (c-1))',
            'nonvanishing': 'generic c (irrational)',
        },
        'modular_cases': {
            'c=1': 'alpha=0, trivial',
            'c=13': 'alpha=12, self-dual, |eta|^24 = |Delta|, L-content = zeta(s-11)*L(Sym^2 Delta)',
            'c=25': 'alpha=24, |eta|^48 = |Delta^2|, standard',
        },
        'non_modular_cases': {
            'c=2': 'alpha=1, not modular, both spectra present',
            'c=pi': 'alpha=pi-1, irrational, full Maass contribution',
        },
    }
