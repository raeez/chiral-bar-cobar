"""
kuznetsov_bridge.py — Kuznetsov trace formula bridge from Kloosterman sums
to spectral data (Hecke eigenvalues and L-functions).

The Rademacher expansion of rational VOA characters involves Kloosterman
sums K(m,n;c).  The Kuznetsov trace formula converts sums of Kloosterman
sums into spectral sums involving Hecke eigenvalues of Maass forms and
the Eisenstein continuous spectrum.

Bridge chain:
  VOA character (Rademacher) → generalized Kloosterman sums K^ρ_{ij}(m,n;c)
  → Kuznetsov spectral inversion → Hecke eigenvalues a_j(n)
  → L-functions L(s, u_j) with Euler products

The non-multiplicativity of character coefficients decomposes as a LINEAR
COMBINATION of multiplicative Hecke eigenvalues:
  a_i(n) = Σ_j S_{ij} · (Σ_k c_{jk} · a_k^{Maass}(n) + continuous)

References:
  Kuznetsov, "Petersson's conjecture for cusp forms of weight zero", 1980.
  Iwaniec, "Spectral Methods of Automorphic Forms", AMS, 2002.
  Bruggeman, "Fourier coefficients of automorphic forms", LNM 865, 1981.
  Proskurin, "On general Kloosterman sums", 2005.
"""

from __future__ import annotations

from functools import lru_cache
from math import gcd
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import mpmath
from mpmath import (
    mp, mpf, mpc, pi, exp, sin, cos, sqrt, log, fsum, power,
    gamma as mpgamma, zeta, besselj, bessely, besselk, besseli,
    quad, inf, re, im, conj, fac, floor, euler as euler_gamma,
    matrix as mpmatrix, nsum, diff,
)


# ---------------------------------------------------------------------------
# Precision
# ---------------------------------------------------------------------------

DEFAULT_DPS = 50


def _set_dps(dps: int = DEFAULT_DPS):
    mp.dps = dps


# ===================================================================
# 1. Classical Kloosterman sums
# ===================================================================

def _mod_inverse(a: int, c: int) -> int:
    """Compute a^{-1} mod c via extended Euclidean algorithm.

    Raises ValueError if gcd(a, c) != 1.
    """
    g, x, _ = _extended_gcd(a, c)
    if g != 1:
        raise ValueError(f"gcd({a}, {c}) = {g}, no inverse mod {c}")
    return x % c


def _extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean: returns (g, x, y) with a*x + b*y = g."""
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


def kloosterman_sum(m: int, n: int, c: int, dps: int = DEFAULT_DPS) -> mpc:
    """Classical Kloosterman sum S(m, n; c).

    S(m, n; c) = Σ_{d (mod c), gcd(d,c)=1} e^{2πi(md + nd')/c}

    where dd' ≡ 1 (mod c).
    """
    _set_dps(dps)
    if c <= 0:
        raise ValueError(f"c must be positive, got {c}")
    if c == 1:
        return mpc(1, 0)

    omega = 2 * pi * mpc(0, 1) / c
    total = mpc(0, 0)
    for d in range(c):
        if gcd(d, c) != 1:
            continue
        d_inv = _mod_inverse(d, c)
        total += exp(omega * (m * d + n * d_inv))
    return total


def kloosterman_sum_real(m: int, n: int, c: int, dps: int = DEFAULT_DPS) -> mpf:
    """Real part of S(m,n;c). For integer m,n, S(m,n;c) is always real."""
    val = kloosterman_sum(m, n, c, dps=dps)
    return re(val)


def euler_totient(n: int) -> int:
    """Euler's totient function φ(n)."""
    if n <= 0:
        raise ValueError(f"n must be positive, got {n}")
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def num_divisors(n: int) -> int:
    """Number of divisors d(n)."""
    if n <= 0:
        raise ValueError
    count = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            count += 1
            if d != n // d:
                count += 1
    return count


def weil_bound(m: int, n: int, c: int) -> mpf:
    """Weil bound: |S(m,n;c)| ≤ d(c) · √c · gcd(m,n,c)^{1/2}."""
    g = gcd(gcd(abs(m), abs(n)), c)
    return mpf(num_divisors(c)) * sqrt(mpf(c)) * sqrt(mpf(g))


def verify_kloosterman_multiplicativity(
    m: int, n: int, c1: int, c2: int, dps: int = DEFAULT_DPS
) -> mpf:
    """Verify multiplicativity of S(m,n;c) for coprime c1, c2.

    S(m,n;c1*c2) = S(m*c2', n*c2'; c1) * S(m*c1', n*c1'; c2)
    where c1' is inverse of c1 mod c2, c2' inverse of c2 mod c1.

    Returns the discrepancy |LHS - RHS|.
    """
    _set_dps(dps)
    if gcd(c1, c2) != 1:
        raise ValueError(f"c1={c1}, c2={c2} must be coprime")

    c1_inv = _mod_inverse(c1, c2)  # c1' mod c2
    c2_inv = _mod_inverse(c2, c1)  # c2' mod c1

    lhs = kloosterman_sum(m, n, c1 * c2, dps=dps)
    rhs = (kloosterman_sum(m * c2_inv, n * c2_inv, c1, dps=dps)
           * kloosterman_sum(m * c1_inv, n * c1_inv, c2, dps=dps))
    return abs(lhs - rhs)


# ===================================================================
# 2. Kloosterman–Dirichlet series Z(m, n; s)
# ===================================================================

def kloosterman_dirichlet_series(
    m: int, n: int, s, c_max: int = 200, dps: int = DEFAULT_DPS
) -> mpc:
    """Z(m, n; s) = Σ_{c=1}^{c_max} S(m,n;c) · c^{-s}.

    Converges absolutely for Re(s) > 3/2 by the Weil bound.
    """
    _set_dps(dps)
    s = mpc(s)
    total = mpc(0, 0)
    for c in range(1, c_max + 1):
        sk = kloosterman_sum(m, n, c, dps=dps)
        total += sk * power(mpf(c), -s)
    return total


def kloosterman_dirichlet_weighted(
    m: int, n: int, s, c_max: int = 200, dps: int = DEFAULT_DPS
) -> mpc:
    """Weighted version: Σ_{c=1}^{c_max} S(m,n;c) · c^{-2s}.

    This is the normalization appearing in the Kuznetsov formula context.
    """
    _set_dps(dps)
    s = mpc(s)
    total = mpc(0, 0)
    for c in range(1, c_max + 1):
        sk = kloosterman_sum(m, n, c, dps=dps)
        total += sk * power(mpf(c), -2 * s)
    return total


def kloosterman_partial_sums(
    m: int, n: int, s, c_max: int = 200, dps: int = DEFAULT_DPS
) -> List[mpc]:
    """Return partial sums Z_N(m,n;s) = Σ_{c=1}^N S(m,n;c)c^{-s} for N=1..c_max.

    Useful for studying convergence.
    """
    _set_dps(dps)
    s = mpc(s)
    partials = []
    running = mpc(0, 0)
    for c in range(1, c_max + 1):
        sk = kloosterman_sum(m, n, c, dps=dps)
        running += sk * power(mpf(c), -s)
        partials.append(running)
    return partials


# ===================================================================
# 3. Generalized Kloosterman sums for Ising model
# ===================================================================

def _ising_modular_data(dps: int = DEFAULT_DPS):
    """Return (S_matrix, T_matrix, labels, conformal_weights, c) for Ising M(4,3).

    Labels: sorted by conformal weight.
    Ising has 3 primaries: (1,1) with h=0, (2,1) with h=1/2, (1,2)=(3,1) with h=1/16.
    Sorted: h=0, h=1/16, h=1/2.
    """
    _set_dps(dps)
    # Ising = M(4,3), c = 1/2
    p, q = 4, 3
    c_val = Fraction(1, 2)

    # Primary labels sorted by h: (1,1) h=0, (3,1)=(1,2) h=1/16, (2,1) h=1/2
    labels = [(1, 1), (3, 1), (2, 1)]
    h_vals = [Fraction(0), Fraction(1, 16), Fraction(1, 2)]
    h_mpf = [mpf(h.numerator) / mpf(h.denominator) for h in h_vals]
    c_mpf = mpf(1) / 2

    # S-matrix: S_{(r,s),(r',s')} = (-1)^{1+rs'+r's} sqrt(8/pq) sin(πrr'/p) sin(πss'/q)
    # But we need to be careful with the sign convention.
    # Standard normalization: S = sqrt(8/(p*q)) * (-1)^{...} * sin * sin
    n = 3
    S = mpmatrix(n, n)
    prefactor = sqrt(mpf(8) / (mpf(p) * mpf(q)))
    for i in range(n):
        r1, s1 = labels[i]
        for j in range(n):
            r2, s2 = labels[j]
            # Sign: (-1)^{1 + r1*s2 + r2*s1}
            # Actually the standard formula has a specific sign.
            # For M(p,q): S_{(r,s),(r',s')} = (-1)^{r*s'+r'*s+r*r'+s*s'} * pref * sin * sin
            # Let me use the explicit verified formula from vvmf_hecke.
            sign = (-1) ** (r1 * s2 + r2 * s1 + r1 * r2 + s1 * s2)
            S[i, j] = sign * prefactor * sin(pi * r1 * r2 / p) * sin(pi * s1 * s2 / q)

    # T-matrix: diagonal, T_{ii} = e^{2πi(h_i - c/24)}
    T = mpmatrix(n, n)
    for i in range(n):
        T[i, i] = exp(2 * pi * mpc(0, 1) * (h_mpf[i] - c_mpf / 24))

    return S, T, labels, h_vals, h_mpf, c_val, c_mpf


def ising_modular_representation(d: int, c: int, dps: int = DEFAULT_DPS) -> mpmatrix:
    """Compute the modular representation matrix ρ(γ) for γ = [[a,b],[c_,d_]] ∈ SL(2,Z).

    For Rademacher-type sums we need ρ(S^{-1} T^d S) and related elements.
    Here we compute ρ(T^d) = T^d (diagonal), since T generates the parabolic.

    For the generalized Kloosterman sums in the Rademacher expansion,
    the relevant element is:
      K^ρ_{ij}(m,n;c) = Σ_{d (mod c), gcd(d,c)=1} ρ(M_d)_{ij} · e^{2πi(m d + n d')/c}

    where M_d is the appropriate SL(2,Z) element.
    """
    _set_dps(dps)
    S, T, *_ = _ising_modular_data(dps=dps)
    # T^d
    n = T.rows
    Td = mpmatrix(n, n)
    for i in range(n):
        Td[i, i] = power(T[i, i], d)
    return Td


def generalized_kloosterman_ising(
    i: int, j: int, m_frac: Fraction, n_int: int, c: int, dps: int = DEFAULT_DPS
) -> mpc:
    """Generalized Kloosterman sum K^ρ_{ij}(m, n; c) for the Ising model.

    K^ρ_{ij}(m, n; c) = Σ_{d (mod c), gcd(d,c)=1}
        ρ(S^{-1} T^d S)_{ij} · e^{2πi(m·d + n·d')/c}

    where m = h_j - c_voa/24 (a rational number, can be negative)
    and n is an integer (or rational offset for non-vacuum).

    For the Rademacher expansion:
      m = h_j - c_voa/24  (conformal weight minus c/24)
      n ranges over non-negative integers (level of the coefficient)

    Args:
        i, j: row and column indices (0=vacuum, 1=σ, 2=ε for Ising)
        m_frac: the rational exponent m (as Fraction)
        n_int: integer n
        c: modulus
    """
    _set_dps(dps)
    if c <= 0:
        raise ValueError(f"c must be positive, got {c}")

    S_mat, T_mat, labels, h_vals, h_mpf, c_val, c_mpf = _ising_modular_data(dps=dps)
    n_prim = S_mat.rows

    # S^{-1} = S^dag = S^T (for unitary symmetric S)
    S_inv = S_mat.T

    m_mpf = mpf(m_frac.numerator) / mpf(m_frac.denominator)
    n_mpf = mpf(n_int)
    omega = 2 * pi * mpc(0, 1)

    total = mpc(0, 0)
    for d in range(c):
        if gcd(d, c) != 1:
            continue
        d_inv = _mod_inverse(d, c)

        # Compute ρ(S^{-1} T^d S)_{ij} = (S^{-1} T^d S)_{ij}
        # T^d is diagonal: (T^d)_{kk} = T_{kk}^d
        # (S^{-1} T^d S)_{ij} = Σ_k S^{-1}_{ik} T_{kk}^d S_{kj}
        rho_ij = mpc(0, 0)
        for k in range(n_prim):
            rho_ij += S_inv[i, k] * power(T_mat[k, k], d) * S_mat[k, j]

        phase = exp(omega * (m_mpf * d + n_mpf * d_inv) / c)
        total += rho_ij * phase

    return total


# ===================================================================
# 4. Kuznetsov spectral side — Bessel transforms and integrals
# ===================================================================

def bessel_kernel_K(x, t, dps: int = DEFAULT_DPS) -> mpf:
    """Kuznetsov Bessel kernel for the discrete spectrum.

    For the Kuznetsov formula with test function h, the Bessel transform is:
    H(t) = ∫_0^∞ h(x) · K(x, t) dx/x

    The kernel for the holomorphic/Maass form case involves
    K_{2it}(x) (K-Bessel function) and J-Bessel functions.

    Standard kernel: K(x, t) = (cosh πt)^{-1} · [J_{2it}(x) + J_{-2it}(x)] / 2
    for the sum formula, or alternatively involving K_{2it}.

    Here we use the kernel appropriate for the Kloosterman-side normalization
    h(x) = x·J_1(x):
      K(x, t) = J_{2it}(x) + J_{-2it}(x)
    """
    _set_dps(dps)
    x, t = mpf(x), mpf(t)
    if x <= 0:
        return mpf(0)
    # J_{2it}(x) = Bessel J with complex order 2it
    j_plus = besselj(2 * mpc(0, 1) * t, x)
    j_minus = besselj(-2 * mpc(0, 1) * t, x)
    return re(j_plus + j_minus)


def bessel_transform_h(t, dps: int = DEFAULT_DPS) -> mpc:
    """Bessel transform H(t) of the test function h(x) = x · J_1(x).

    H(t) = ∫_0^∞ x · J_1(x) · K(x, t) dx / x
         = ∫_0^∞ J_1(x) · [J_{2it}(x) + J_{-2it}(x)] dx

    For small |t| we use numerical integration over a moderate range.
    For larger |t| the Bessel functions J_{±2it}(x) grow exponentially
    in magnitude for real x when the order is purely imaginary, so we
    use the Weber-Schafheitlin closed form:

      ∫_0^∞ J_μ(x) J_ν(x) dx = (2/π) sin(π(μ-ν)/2) Γ((μ+ν+1)/2)
                                  / [Γ((ν-μ+2)/2) Γ((μ-ν+2)/2) Γ((μ+ν+2)/2)]

    valid when Re(μ+ν) > -1 and μ-ν is not an odd integer.

    For μ=1, ν=2it the Weber-Schafheitlin integral gives:
      I(t) = ∫_0^∞ J_1(x) J_{2it}(x) dx
           = Γ((1+2it+1)/2) / [Γ((2it)/2 + 1) · Γ(1)]  (simplified)

    We use the identity:
      ∫_0^∞ J_μ(x) J_ν(x) dx = 1/√π · Γ((μ+ν+1)/2) / Γ((ν-μ)/2 + 1)
    when Re(μ+ν) > -1 and ν-μ is not a negative odd integer.
    (This requires more care with normalization.)

    For safety and correctness, we compute numerically at moderate |t|.
    """
    _set_dps(dps)
    t = mpc(t)
    t_abs = abs(t)

    # For small t, direct numerical integration is stable
    x_max = 20 + 5 * min(float(t_abs), 3)

    def integrand_re(x):
        if x < 1e-15:
            return mpf(0)
        j1 = besselj(1, x)
        j_p = besselj(2 * mpc(0, 1) * t, x)
        j_m = besselj(-2 * mpc(0, 1) * t, x)
        return re(j1 * (j_p + j_m))

    def integrand_im(x):
        if x < 1e-15:
            return mpf(0)
        j1 = besselj(1, x)
        j_p = besselj(2 * mpc(0, 1) * t, x)
        j_m = besselj(-2 * mpc(0, 1) * t, x)
        return im(j1 * (j_p + j_m))

    re_part = quad(integrand_re, [mpf('0.01'), mpf(x_max)], error=True)[0]
    im_part = quad(integrand_im, [mpf('0.01'), mpf(x_max)], error=True)[0]
    return mpc(re_part, im_part)


def continuous_spectral_integrand(t, n: int, dps: int = DEFAULT_DPS) -> mpf:
    """Integrand of the continuous spectral contribution to Kuznetsov.

    (1/π) · |σ_{2it}(n)|² / |ζ(1+2it)|² · H(t)

    σ_{2it}(n) = Σ_{d|n} d^{2it}
    """
    _set_dps(dps)
    t = mpf(t)
    if abs(t) < 1e-15:
        # At t=0: σ_0(n) = d(n), ζ(1) has pole. Handle separately.
        return mpf(0)

    # σ_{2it}(n)
    sigma = mpc(0, 0)
    for d in range(1, n + 1):
        if n % d == 0:
            sigma += power(mpf(d), 2 * mpc(0, 1) * t)

    # |ζ(1+2it)|²
    z = zeta(1 + 2 * mpc(0, 1) * t)
    z_abs_sq = abs(z) ** 2

    if z_abs_sq < mpf('1e-100'):
        return mpf(0)

    # H(t) from Bessel transform
    H = bessel_transform_h(t, dps=dps)

    return re(abs(sigma) ** 2 / z_abs_sq * H) / pi


def continuous_spectral_integral(
    n: int, t_max: mpf = 20, dps: int = DEFAULT_DPS
) -> mpf:
    """Compute the continuous spectral integral for the Kuznetsov formula.

    ∫_0^∞ |σ_{2it}(n)|² / |ζ(1+2it)|² · H(t) dt / π

    Numerically integrated from 0 to t_max.
    """
    _set_dps(dps)

    def integrand(t):
        return continuous_spectral_integrand(t, n, dps=dps)

    result = quad(integrand, [mpf('0.1'), mpf(t_max)], error=True)[0]
    return result


# ===================================================================
# 5. Hecke eigenvalue extraction
# ===================================================================

def divisor_sigma(n: int, s) -> mpc:
    """Divisor function σ_s(n) = Σ_{d|n} d^s."""
    total = mpc(0, 0)
    for d in range(1, n + 1):
        if n % d == 0:
            total += power(mpf(d), s)
    return total


def kloosterman_geometric_side(
    m: int, n: int, c_max: int = 50, dps: int = DEFAULT_DPS
) -> mpc:
    """Compute the geometric (Kloosterman) side of Kuznetsov:

    Σ_{c=1}^{c_max} S(m,n;c)/c · h(4π√(mn)/c)

    where h(x) = x · J_1(x) is the test function.
    """
    _set_dps(dps)
    if m <= 0 or n <= 0:
        raise ValueError("m, n must be positive for standard Kuznetsov")

    total = mpc(0, 0)
    mn_sqrt = sqrt(mpf(m) * mpf(n))
    for c in range(1, c_max + 1):
        s_val = kloosterman_sum(m, n, c, dps=dps)
        x = 4 * pi * mn_sqrt / c
        h_val = x * besselj(1, x)  # h(x) = x * J_1(x)
        total += s_val / c * h_val
    return total


# ===================================================================
# 6. VOA-Kuznetsov bridge for Ising model
# ===================================================================

def ising_character_coefficients(num_terms: int = 30, dps: int = DEFAULT_DPS) -> List[List[int]]:
    """Compute Ising model character q-expansion coefficients.

    Returns a list of 3 lists (one per primary: vacuum, σ, ε),
    each containing integer coefficients of the q-expansion relative
    to q^{h_i - c/24}.

    Uses the Rocha-Caridi formula implemented via the theta/eta convolution.
    """
    _set_dps(dps)
    p, q = 4, 3
    labels = [(1, 1), (3, 1), (2, 1)]  # h=0, h=1/16, h=1/2

    def _inverse_eta_coeffs(num):
        coeffs = [0] * num
        coeffs[0] = 1
        for nn in range(1, num):
            val = 0
            for k in range(1, nn + 1):
                p1 = k * (3 * k - 1) // 2
                p2 = k * (3 * k + 1) // 2
                sign = (-1) ** (k + 1)
                if p1 <= nn:
                    val += sign * coeffs[nn - p1]
                if p2 <= nn:
                    val += sign * coeffs[nn - p2]
            coeffs[nn] = val
        return coeffs

    inv_eta = _inverse_eta_coeffs(num_terms)
    all_coeffs = []

    for r, s in labels:
        # theta[j]: coefficient of q^j in the theta function part
        theta = [0] * num_terms
        for nn in range(-num_terms, num_terms + 1):
            d_plus = nn * (nn * p * q + r * q - s * p)
            if 0 <= d_plus < num_terms:
                theta[d_plus] += 1
            d_minus = (nn * p + r) * (nn * q + s)
            if 0 <= d_minus < num_terms:
                theta[d_minus] -= 1

        # Convolve theta with 1/eta
        coeffs = []
        for mm in range(num_terms):
            val = 0
            for j in range(mm + 1):
                if theta[j] != 0:
                    val += inv_eta[mm - j] * theta[j]
            coeffs.append(val)
        all_coeffs.append(coeffs)

    return all_coeffs


def rademacher_kloosterman_sum(
    i: int, n_level: int, c_max: int = 20, dps: int = DEFAULT_DPS
) -> mpc:
    """Rademacher expansion contribution for the i-th Ising character at level n.

    The Rademacher expansion gives:
      a_i(n) = Σ_j S_{ij} · Σ_{c=1}^∞ K^ρ_{ij}(h_j - c/24, n; c)/c · I_Bessel(...)

    We compute the partial sum over c = 1..c_max of the Kloosterman part.
    This is the Kloosterman-side data that Kuznetsov inverts.
    """
    _set_dps(dps)
    S_mat, T_mat, labels, h_vals, h_mpf, c_val, c_mpf = _ising_modular_data(dps=dps)
    n_prim = S_mat.rows

    total = mpc(0, 0)
    for j in range(n_prim):
        # m = h_j - c/24
        m_frac = h_vals[j] - Fraction(c_val, 24)
        m_mpf = mpf(m_frac.numerator) / mpf(m_frac.denominator)

        # Product √(|m| * n) for the Bessel argument
        m_abs = abs(m_mpf)
        n_mpf = mpf(n_level)

        for c in range(1, c_max + 1):
            # Generalized Kloosterman sum
            K_val = generalized_kloosterman_ising(i, j, m_frac, n_level, c, dps=dps)

            # Rademacher Bessel factor: (2π/c) * I_1(4π√(|m|·n)/c) for m < 0
            # or J_1 factor for m > 0
            if m_abs > mpf('1e-30') and n_level > 0:
                arg = 4 * pi * sqrt(m_abs * n_mpf) / c
                if m_mpf < 0:
                    bessel_val = besseli(1, arg)  # I-Bessel for negative m
                else:
                    bessel_val = besselj(1, arg)
                weight = 2 * pi / c * bessel_val
            else:
                weight = mpc(1) / c

            total += S_mat[i, j] * K_val * weight

    return total


def voa_kuznetsov_spectral_decomposition(
    i: int, n_level: int, c_max: int = 20, dps: int = DEFAULT_DPS
) -> Dict[str, mpc]:
    """Attempt the VOA-Kuznetsov bridge decomposition for the i-th Ising character.

    The bridge decomposes:
      a_i(n) = Σ_j S_{ij} · [discrete_j(n) + continuous_j(n)]

    where discrete_j involves Maass form Hecke eigenvalues and
    continuous_j involves ζ(1+2it) poles.

    Returns dict with 'rademacher' (the Kloosterman sum) and 'direct' (q-expansion).
    """
    _set_dps(dps)

    # Direct computation from q-expansion
    all_coeffs = ising_character_coefficients(num_terms=max(n_level + 5, 30), dps=dps)
    direct_val = all_coeffs[i][n_level] if n_level < len(all_coeffs[i]) else 0

    # Rademacher-Kloosterman side
    rademacher_val = rademacher_kloosterman_sum(i, n_level, c_max=c_max, dps=dps)

    return {
        'direct': mpc(direct_val),
        'rademacher': rademacher_val,
        'discrepancy': abs(mpc(direct_val) - rademacher_val),
    }


# ===================================================================
# 7. L-function content extraction
# ===================================================================

def spectral_l_function_term(
    s, t_j: mpf, a_j_n_func, n_max: int = 50, dps: int = DEFAULT_DPS
) -> mpc:
    """Compute partial L-function L_j(s) = Σ_{n=1}^{n_max} a_j(n) · n^{-s}
    for a Maass form with spectral parameter t_j.

    a_j_n_func(n) returns the n-th Hecke eigenvalue.
    """
    _set_dps(dps)
    s = mpc(s)
    total = mpc(0, 0)
    for n in range(1, n_max + 1):
        total += a_j_n_func(n) * power(mpf(n), -s)
    return total


def continuous_l_function_term(
    s, n: int, dps: int = DEFAULT_DPS
) -> mpc:
    """Continuous spectrum L-function contribution at integer n.

    From the Eisenstein series: σ_{2it}(n) = Σ_{d|n} d^{2it}.
    The L-function is ζ(s-it)ζ(s+it).
    """
    _set_dps(dps)
    s = mpc(s)
    # The Eisenstein contribution to the L-function at parameter n
    # uses ζ(s)ζ(s-1) in the Rankin-Selberg sense
    return zeta(s) * zeta(s - 1 + mpc(0, 0))


def ising_spectral_content(
    i: int, s, c_max: int = 20, n_max: int = 20, dps: int = DEFAULT_DPS
) -> Dict[str, mpc]:
    """Extract the L-function content L_i(s) for the i-th Ising character.

    L_i(s) = Σ_n a_i(n) · n^{-s}

    where a_i(n) are the character coefficients.
    This is a Dirichlet series that (via Kuznetsov) decomposes as a
    sum of automorphic L-functions.
    """
    _set_dps(dps)
    s = mpc(s)

    all_coeffs = ising_character_coefficients(num_terms=n_max + 5, dps=dps)
    coeffs = all_coeffs[i]

    # Direct Dirichlet series
    L_direct = mpc(0, 0)
    for n in range(1, min(n_max + 1, len(coeffs))):
        if coeffs[n] != 0:
            L_direct += coeffs[n] * power(mpf(n), -s)

    return {
        'L_direct': L_direct,
        'num_terms': min(n_max, len(coeffs) - 1),
    }


# ===================================================================
# 8. Kloosterman sum tables and statistics
# ===================================================================

def kloosterman_table(
    m_range: range, n_range: range, c_range: range, dps: int = DEFAULT_DPS
) -> Dict[Tuple[int, int, int], mpf]:
    """Compute S(m,n;c) for all (m,n,c) in given ranges.

    Returns dict keyed by (m,n,c) with real values.
    """
    _set_dps(dps)
    table = {}
    for m in m_range:
        for n in n_range:
            for c in c_range:
                if c <= 0:
                    continue
                table[(m, n, c)] = kloosterman_sum_real(m, n, c, dps=dps)
    return table


def kloosterman_weil_ratio(m: int, n: int, c: int, dps: int = DEFAULT_DPS) -> mpf:
    """Ratio |S(m,n;c)| / (d(c)√c · gcd(m,n,c)^{1/2}).

    Should be ≤ 1 by the Weil bound.
    """
    _set_dps(dps)
    s_val = abs(kloosterman_sum(m, n, c, dps=dps))
    bound = weil_bound(m, n, c)
    if bound < mpf('1e-100'):
        return mpf(0)
    return s_val / bound


def kloosterman_average_cancellation(
    m: int, n: int, c_max: int = 100, dps: int = DEFAULT_DPS
) -> List[mpf]:
    """Compute partial sums Σ_{c≤N} S(m,n;c)/c for N = 1..c_max.

    The Kuznetsov formula implies these partial sums have bounded growth
    (rather than growing like the trivial bound Σ φ(c)/c ~ N).
    """
    _set_dps(dps)
    partials = []
    running = mpf(0)
    for c in range(1, c_max + 1):
        s_val = kloosterman_sum_real(m, n, c, dps=dps)
        running += s_val / c
        partials.append(running)
    return partials


def ramanujan_sum(n: int, c: int) -> int:
    """Ramanujan sum c_c(n) = S(0, n; c) = Σ_{d|gcd(n,c)} d · μ(c/d).

    This equals the Kloosterman sum S(0, n; c) and is always a real integer.
    """
    from math import gcd as _gcd
    g = _gcd(abs(n), c)
    total = 0
    for d in range(1, g + 1):
        if g % d == 0:
            total += d * _mobius(c // d)
    return total


def _mobius(n: int) -> int:
    """Mobius function."""
    if n == 1:
        return 1
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                temp //= d
                count += 1
            if count > 1:
                return 0
            factors.append(d)
        d += 1
    if temp > 1:
        factors.append(temp)
    return (-1) ** len(factors)


# ===================================================================
# 9. Convergence diagnostics
# ===================================================================

def kloosterman_dirichlet_convergence(
    m: int, n: int, s_values: List, c_max: int = 200, dps: int = DEFAULT_DPS
) -> Dict:
    """Study convergence of Z(m,n;s) for multiple s values.

    Returns dict with partial sums at c_max//4, c_max//2, c_max for each s.
    """
    _set_dps(dps)
    results = {}
    checkpoints = [c_max // 4, c_max // 2, c_max]

    for s in s_values:
        partials = kloosterman_partial_sums(m, n, s, c_max=c_max, dps=dps)
        results[str(s)] = {cp: partials[cp - 1] for cp in checkpoints if cp <= len(partials)}

    return results


def weil_bound_saturation(
    m_max: int = 5, n_max: int = 5, c_max: int = 50, dps: int = DEFAULT_DPS
) -> Dict[str, mpf]:
    """Compute maximum Weil bound saturation ratio across parameter ranges.

    Returns the max and average ratio |S(m,n;c)| / weil_bound(m,n,c).
    """
    _set_dps(dps)
    max_ratio = mpf(0)
    total_ratio = mpf(0)
    count = 0

    for m in range(1, m_max + 1):
        for n in range(1, n_max + 1):
            for c in range(2, c_max + 1):
                ratio = kloosterman_weil_ratio(m, n, c, dps=dps)
                if ratio > max_ratio:
                    max_ratio = ratio
                total_ratio += ratio
                count += 1

    return {
        'max_ratio': max_ratio,
        'avg_ratio': total_ratio / count if count > 0 else mpf(0),
        'count': count,
    }
