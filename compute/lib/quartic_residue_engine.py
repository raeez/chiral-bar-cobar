r"""
quartic_residue_engine.py — Quartic residue programme: computational engine.

Implements the quartic layer of the shadow-zeta interface, where the shadow
Postnikov tower and zeta-zero residues genuinely meet.  The engine covers:

  1. Shadow data extraction (Virasoro and W_N families)
  2. 3x3 Hankel matrix and Schur complement for quartic contact isolation
  3. Universal residue factor A_c(rho) at nontrivial zeta zeros
  4. Paired residue kernel w_{c,rho,u0}(Delta) with decay exponent
  5. Dirichlet-sewing lift S_A(u) from conformal-weight multisets
  6. Euler-Koszul defect D_A(u)
  7. Prime-side Li coefficients lambda_tilde_n(A)
  8. Surface moment matrix (infinite Hankel from S_A)
  9. Ising model residue moments at first zeta zero
  10. W_3 pure spin-3 slice: multi-channel quartic block
  11. Compatibility ratios (on-line vs off-line distinction)

CONVENTIONS:
  - Cohomological grading, |d| = +1.
  - Central charge c is generic (not specialized to c = 26).
  - Virasoro shadow data: H = c/2, C = 2, Q^ct = 10/[c(5c+22)].
  - Dirichlet-sewing lift: S_A(u) = zeta(u+1) * sum_i (zeta(u) - H_{w_i-1}(u)).
  - Euler-Koszul defect: D_A(u) = S_A(u) / (|W| * zeta(u) * zeta(u+1)).

References:
  arithmetic_shadows.tex sec:quartic-residue-programme
  genus_complete.tex subsec:dirichlet-sewing-lift, subsec:prime-side-li
  Benjamin-Chang arXiv:2208.02259
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple, Union

import mpmath
from mpmath import (
    mp, mpf, mpc,
    pi as mpi, gamma as mpgamma, zeta as mpzeta,
    log as mplog, exp as mpexp, sqrt as mpsqrt,
    cos as mpcos, sin as mpsin,
    arg as mparg, fabs, re as mpre, im as mpim,
    diff as mpdiff, zetazero, conj as mpconj,
    matrix as mpmatrix, det as mpdet, fac, power,
    euler as mpeuler,
)

# Default working precision
DEFAULT_DPS = 50


def _set_dps(dps: int = DEFAULT_DPS) -> None:
    """Set mpmath decimal places."""
    mp.dps = dps


# =====================================================================
# Section 1: Virasoro shadow data
# =====================================================================

def virasoro_shadow_data(c: Union[float, mpf, mpc]) -> Tuple[mpf, mpf, mpf]:
    r"""Return (H, C_cubic, Q_ct) for the Virasoro family at central charge c.

    H = c/2            (curvature / quadratic shadow)
    C_cubic = 2        (cubic shadow, independent of c)
    Q_ct = 10/[c(5c+22)]  (quartic contact invariant)

    These are mu_2, mu_3, Sigma_2 in the centered gauge.
    """
    _set_dps()
    c = mpf(c) if not isinstance(c, (mpf, mpc)) else c
    H = c / 2
    C_cubic = mpf(2)
    Q_ct = mpf(10) / (c * (5 * c + 22))
    return (H, C_cubic, Q_ct)


def w3_shadow_data(c: Union[float, mpf]) -> Tuple[mpf, mpf, mpf]:
    r"""Return shadow data for the W_3 algebra: spin-2 channel.

    Same as Virasoro for the spin-2 channel: H = c/2, C = 2,
    Q^ct = 10/[c(5c+22)].
    """
    return virasoro_shadow_data(c)


def w3_pure_spin3_data(c: Union[float, mpf]) -> Tuple[mpf, mpf]:
    r"""Return (H_3, C_3) for the pure spin-3 slice of W_3.

    On the pure spin-3 slice, the cubic shadow drops out (C_3 = 0)
    because the spin-3 current W(z) has no OPE term at order (z-w)^{-3}
    with itself (the OPE W(z)W(w) starts at (z-w)^{-6}).

    H_3 = c/3   (the quadratic shadow for spin-3)
    C_3 = 0     (cubic vanishes on pure spin-3 slice)
    """
    _set_dps()
    c = mpf(c)
    H_3 = c / 3
    C_3 = mpf(0)
    return (H_3, C_3)


# =====================================================================
# Section 2: Hankel matrix and Schur complement
# =====================================================================

def hankel_3x3(H, C, mu4) -> mpmatrix:
    r"""Build the centered 3x3 Hankel matrix.

    In the centered gauge (mu_0 = 1, mu_1 = 0):

        M = [[1,   0,    H  ],
             [0,   H,    C  ],
             [H,   C,    mu4]]

    where H = mu_2 (curvature), C = mu_3 (cubic shadow),
    mu4 = raw quartic moment.
    """
    _set_dps()
    H, C, mu4 = mpf(H), mpf(C), mpf(mu4)
    M = mpmatrix([
        [mpf(1), mpf(0), H],
        [mpf(0), H, C],
        [H, C, mu4],
    ])
    return M


def hankel_determinant(H, C, mu4) -> mpf:
    r"""Compute det(M) = mu_2 * mu_4 - mu_3^2 - mu_2^3.

    D_2 = H * mu4 - C^2 - H^3
    """
    _set_dps()
    H, C, mu4 = mpf(H), mpf(C), mpf(mu4)
    return H * mu4 - C**2 - H**3


def schur_complement(H, C, mu4) -> mpf:
    r"""Compute the Schur complement Sigma_2 = mu_4 - C^2/H - H^2.

    This is D_2 / D_1 where D_1 = H = mu_2.

    On the potential side, Sigma_2 = Q^ct (quartic contact invariant).
    On the Gram side, Sigma_2 = (Q^ct)^{-1} (quartic resonance norm).
    """
    _set_dps()
    H, C, mu4 = mpf(H), mpf(C), mpf(mu4)
    return mu4 - C**2 / H - H**2


# =====================================================================
# Section 3: Virasoro raw quartic moment
# =====================================================================

def virasoro_mu4(c: Union[float, mpf]) -> mpf:
    r"""Compute the raw quartic moment for Virasoro:

    mu_4^Vir = c^2/4 + 8/c + 10/[c(5c+22)]

    This satisfies mu_4 = H^2 + C^2/H + Q^ct
    with H = c/2, C = 2, Q^ct = 10/[c(5c+22)].
    """
    _set_dps()
    c = mpf(c)
    return c**2 / 4 + mpf(8) / c + mpf(10) / (c * (5 * c + 22))


# =====================================================================
# Section 4: Universal residue factor
# =====================================================================

def universal_residue_factor(c: Union[float, mpf], rho: Union[complex, mpc]) -> mpc:
    r"""Compute A_c(rho), the residue of the functional equation factor F_c(s)
    at s = s_rho = (1+rho)/2.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / [2 * pi^{(rho+1)/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho)]

    Here rho is a nontrivial zero of zeta (so zeta(rho) = 0).
    zeta(1+rho) is well-defined since rho is not at s=0.
    zeta'(rho) = derivative of zeta at the zero.
    """
    _set_dps()
    c = mpf(c) if not isinstance(c, (mpf, mpc)) else c
    rho = mpc(rho) if not isinstance(rho, mpc) else rho

    num = mpgamma((1 + rho) / 2) * mpgamma((c + rho - 1) / 2) * mpzeta(1 + rho)

    # zeta'(rho): since zeta(rho) = 0, use mpmath's diff
    zeta_prime_rho = mpdiff(mpzeta, rho)

    denom = (2 * mpi**((rho + 1) / 2)
             * mpgamma((c - rho - 1) / 2)
             * mpgamma(rho / 2)
             * zeta_prime_rho)

    return num / denom


# =====================================================================
# Section 5: Paired residue kernel
# =====================================================================

def paired_residue_kernel(
    c: Union[float, mpf],
    rho: Union[complex, mpc],
    u0: Union[float, mpf],
    Delta: Union[float, mpf],
) -> mpf:
    r"""Compute the paired real residue kernel at conformal weight Delta:

    w_{c,rho,u0}(Delta) = 2 |A_c(rho)| * (2*Delta)^{-(c+sigma-1)/2}
                           * Delta^{-u0}
                           * cos(gamma/2 * log(2*Delta) + arg(A_c(rho)))

    where sigma = Re(rho), gamma = Im(rho).
    """
    _set_dps()
    c = mpf(c) if not isinstance(c, (mpf, mpc)) else c
    rho = mpc(rho) if not isinstance(rho, mpc) else rho
    u0 = mpf(u0)
    Delta = mpf(Delta)

    A = universal_residue_factor(c, rho)
    sigma = mpre(rho)
    gamma = mpim(rho)

    abs_A = fabs(A)
    arg_A = mparg(A)

    decay = -(c + sigma - 1) / 2
    prefactor = 2 * abs_A * power(2 * Delta, decay) * power(Delta, -u0)
    phase = gamma / 2 * mplog(2 * Delta) + arg_A

    return prefactor * mpcos(phase)


# =====================================================================
# Section 6: Dirichlet-sewing lift
# =====================================================================

def harmonic_partial(n: int, u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Compute H_n(u) = sum_{j=1}^{n} j^{-u}.

    H_0(u) = 0 by convention.
    """
    _set_dps()
    u = mpf(u) if isinstance(u, (int, float)) else u
    if n <= 0:
        return mpf(0) if isinstance(u, mpf) else mpc(0)
    return sum(power(mpf(j), -u) for j in range(1, n + 1))


def dirichlet_sewing_lift(weights: List[int], u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Compute the Dirichlet-sewing lift S_A(u).

    S_A(u) = zeta(u+1) * sum_{i=1}^{r} (zeta(u) - H_{w_i - 1}(u))

    where W(A) = {w_1, ..., w_r} is the conformal-weight multiset of strong generators.

    Standard families:
      Heisenberg:  W = {1}      =>  S = zeta(u) * zeta(u+1)
      betagamma:   W = {1, 1}   =>  S = 2 * zeta(u) * zeta(u+1)
      V_k(g):      W = {1^dim(g)} => S = dim(g) * zeta(u) * zeta(u+1)
      Virasoro:    W = {2}      =>  S = zeta(u+1) * (zeta(u) - 1)
      W_N:         W = {2,...,N} =>  S = zeta(u+1) * ((N-1)*zeta(u) - sum_{j=1}^{N-1} H_j(u))
    """
    _set_dps()
    u_val = mpf(u) if isinstance(u, (int, float)) else u
    z_u = mpzeta(u_val)
    z_u1 = mpzeta(u_val + 1)
    total = sum(z_u - harmonic_partial(w - 1, u_val) for w in weights)
    return z_u1 * total


def dirichlet_sewing_lift_wn(N: int, u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Shortcut: S_{W_N}(u) for the principal W-algebra of type A_{N-1}.

    Strong generators have weights {2, 3, ..., N}.
    """
    weights = list(range(2, N + 1))
    return dirichlet_sewing_lift(weights, u)


# =====================================================================
# Section 7: Euler-Koszul defect
# =====================================================================

def euler_koszul_defect(weights: List[int], u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Compute the Euler-Koszul defect D_A(u).

    D_A(u) = S_A(u) / (|W| * zeta(u) * zeta(u+1))
           = (1/r) * sum_{i=1}^{r} (1 - H_{w_i-1}(u) / zeta(u))

    D = 1 iff all w_i = 1 (exact Euler-Koszul).
    """
    _set_dps()
    r = len(weights)
    u_val = mpf(u) if isinstance(u, (int, float)) else u
    z_u = mpzeta(u_val)
    total = sum(1 - harmonic_partial(w - 1, u_val) / z_u for w in weights)
    return total / r


def euler_koszul_defect_wn(N: int, u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Shortcut: D_{W_N}(u) for the principal W-algebra."""
    weights = list(range(2, N + 1))
    return euler_koszul_defect(weights, u)


# =====================================================================
# Section 8: Prime-side Li coefficients
# =====================================================================

def _xi_function(weights: List[int], u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Compute Xi_A(u) = (u-1) * S_A(u).

    Entire since (u-1)*zeta(u) is entire.
    Near u=1, uses the analytic form:
      Xi_A(u) = (u-1)*zeta(u+1) * sum_i ((u-1)*zeta(u) - (u-1)*H_{w_i-1}(u))
    where (u-1)*zeta(u) -> 1 as u -> 1  (Laurent expansion).
    We use mpmath's zeta residue handling by computing
      (u-1)*zeta(u) via mpmath.
    """
    _set_dps()
    u_val = mpf(u) if isinstance(u, (int, float)) else u
    # (u-1)*zeta(u) is entire: use the Stieltjes expansion near u=1
    # For |u-1| small, evaluate via Taylor coefficients.
    # mpmath can handle this if we avoid zeta(u) alone at u=1.
    # Strategy: compute (u-1)*zeta(u) = 1 + gamma*(u-1) + ... via explicit form
    # But for u away from 1, just use the product.
    eps = fabs(u_val - 1)
    if isinstance(eps, mpc):
        eps = fabs(eps)
    if eps < mpf('1e-10'):
        # Near u=1: use analytic continuation
        # (u-1)*zeta(u) = 1 + gamma*(u-1) + gamma_1*(u-1)^2 + ...
        # where gamma_k are the Stieltjes constants
        # For Xi_A(u): need (u-1) * S_A(u)
        # S_A(u) = zeta(u+1) * sum_i (zeta(u) - H_{w_i-1}(u))
        # (u-1)*S_A(u) = zeta(u+1) * sum_i ((u-1)*zeta(u) - (u-1)*H_{w_i-1}(u))
        z_u1 = mpzeta(u_val + 1)  # zeta(u+1) is regular at u=1 (gives zeta(2))
        # (u-1)*zeta(u): use the series
        um1_zeta_u = mpmath.mpf(1)
        if eps > 0:
            um1_zeta_u = (u_val - 1) * mpzeta(u_val)
        total = sum(um1_zeta_u - (u_val - 1) * harmonic_partial(w - 1, u_val) for w in weights)
        return z_u1 * total
    else:
        return (u_val - 1) * dirichlet_sewing_lift(weights, u_val)


def _um1_zeta(u: Union[mpf, mpc]) -> Union[mpf, mpc]:
    r"""Compute (u-1)*zeta(u) safely, including at u=1.

    Uses the Laurent expansion of zeta around s=1:
      zeta(s) = 1/(s-1) + sum_{k=0}^{M} (-1)^k gamma_k / k! * (s-1)^k
    so (s-1)*zeta(s) = 1 + sum_{k=0}^{M} (-1)^k gamma_k / k! * (s-1)^{k+1}

    This representation is analytic everywhere and avoids the pole.
    For |u-1| > 0.5, we use direct multiplication.
    """
    u = mpf(u) if isinstance(u, (int, float)) else u
    if fabs(u - 1) > mpf('0.5'):
        return (u - 1) * mpzeta(u)
    # Stieltjes expansion for |u-1| <= 0.5
    t = u - 1
    result = mpf(1)
    M = max(20, int(mp.dps * 0.5))  # enough terms for precision
    for k in range(M):
        gk = mpmath.stieltjes(k)
        term = (-1)**k * gk / fac(k) * power(t, k + 1)
        result += term
        if fabs(term) < power(mpf(10), -(mp.dps + 5)):
            break
    return result


def _xi_function_safe(weights: List[int], u: Union[float, mpf, mpc]) -> Union[mpf, mpc]:
    r"""Xi_A(u) = (u-1)*S_A(u) evaluated safely, including at u=1.

    Uses the factored representation:
      Xi_A(u) = zeta(u+1) * sum_i ( (u-1)*zeta(u) - (u-1)*H_{w_i-1}(u) )

    where (u-1)*zeta(u) is computed via _um1_zeta using the Stieltjes
    expansion, avoiding the pole at u=1.
    """
    _set_dps()
    u_val = mpf(u) if isinstance(u, (int, float)) else u
    z_u1 = mpzeta(u_val + 1)

    um1 = u_val - 1
    um1_z = _um1_zeta(u_val)
    total = sum(um1_z - um1 * harmonic_partial(w - 1, u_val) for w in weights)
    return z_u1 * total


def prime_side_li(weights: List[int], n: int, dps: int = DEFAULT_DPS) -> mpf:
    r"""Compute the n-th prime-side Li coefficient lambda_tilde_n(A).

    lambda_tilde_n(A) = (1/(n-1)!) * (d/du)^n [u^{n-1} * log(Xi_A(u))] |_{u=1}

    For n=1: lambda_tilde_1 = (d/du)[log Xi_A(u)] |_{u=1}
                             = Xi_A'(1) / Xi_A(1)

    Uses mpmath numerical differentiation at high precision.
    The function Xi_A(u) = (u-1)*S_A(u) is entire, so differentiation
    is done using _xi_function_safe which avoids the zeta(1) pole.
    """
    mp.dps = dps + 30  # extra guard digits for differentiation

    if n < 1:
        raise ValueError("Li coefficient index n must be >= 1")

    # Step size for centered differences: h = 10^{-dps/3} balances
    # truncation error against round-off.  mpmath's default step size
    # (~ 10^{-dps}) is too small for this function.
    h = power(mpf(10), -(dps // 3))

    def log_xi(u):
        xi_val = _xi_function_safe(weights, u)
        if fabs(xi_val) < mpf('1e-100'):
            return mpf('-inf')
        return mplog(fabs(xi_val))

    if n == 1:
        # 4th-order centered difference for first derivative:
        # f'(x) = [-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)] / (12h)
        x = mpf(1)
        result = (-log_xi(x + 2 * h) + 8 * log_xi(x + h)
                  - 8 * log_xi(x - h) + log_xi(x - 2 * h)) / (12 * h)
        mp.dps = dps
        return result

    if n == 2:
        # 4th-order centered second derivative of u^{n-1} * log Xi(u):
        # f''(x) = [-f(x+2h) + 16f(x+h) - 30f(x) + 16f(x-h) - f(x-2h)] / (12h^2)
        x = mpf(1)
        def f(u):
            return power(u, n - 1) * log_xi(u)
        result = (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x)
                  + 16 * f(x - h) - f(x - 2 * h)) / (12 * h**2)
        mp.dps = dps
        return result / fac(n - 1)

    # General n: use mpmath diff with explicit step size
    def f(u):
        return power(u, n - 1) * log_xi(u)

    deriv = mpdiff(f, mpf(1), n, h=h)
    mp.dps = dps
    return deriv / fac(n - 1)


def prime_side_li_wn(N: int, n: int, dps: int = DEFAULT_DPS) -> mpf:
    r"""Shortcut: lambda_tilde_n(W_N) for the principal W-algebra."""
    weights = list(range(2, N + 1))
    return prime_side_li(weights, n, dps=dps)


# =====================================================================
# Section 9: Surface moment matrix
# =====================================================================

def surface_moment_matrix(
    weights: List[int],
    alpha: Union[float, mpf],
    size: int,
) -> mpmatrix:
    r"""Build the (size x size) surface moment matrix.

    M_A(alpha)_{ij} = S_A(alpha + i + j),  i,j >= 0

    This is a Hankel matrix whose positivity (all leading minors > 0)
    is a necessary condition for the surface polarization programme.
    """
    _set_dps()
    alpha = mpf(alpha)
    M = mpmatrix(size, size)
    # Cache evaluations since S_A(alpha + i + j) = S_A(alpha + i + j)
    # with i+j ranging from 0 to 2*(size-1)
    cache = {}
    for k in range(2 * size - 1):
        val = dirichlet_sewing_lift(weights, alpha + k)
        cache[k] = val
    for i in range(size):
        for j in range(size):
            M[i, j] = cache[i + j]
    return M


def leading_minors(M: mpmatrix) -> List[mpf]:
    r"""Compute all leading principal minors of a square matrix.

    Returns [det(M[0:1,0:1]), det(M[0:2,0:2]), ..., det(M)].
    """
    _set_dps()
    n = M.rows
    minors = []
    for k in range(1, n + 1):
        sub = mpmatrix(k, k)
        for i in range(k):
            for j in range(k):
                sub[i, j] = M[i, j]
        minors.append(mpdet(sub))
    return minors


# =====================================================================
# Section 10: Ising model residue moments
# =====================================================================

# Ising model c = 1/2: scalar primaries
# Virasoro primary operators: identity (Delta=0), sigma (Delta=1/16), epsilon (Delta=1/2)
# For the constrained Epstein / residue programme, Delta=0 is excluded
# (the identity is the vacuum, not a propagating state).
# So we use Delta = 1/16 (spin field) and Delta = 1/2 (energy).

ISING_C = mpf('1/2')
ISING_PRIMARIES = [
    # (Delta, degeneracy)
    (mpf('1/16'), 1),   # sigma (spin field)
    (mpf('1/2'), 1),    # epsilon (energy operator)
]


def ising_residue_moment(
    n: int,
    rho: Union[complex, mpc],
    u0: Union[float, mpf] = 2,
) -> mpc:
    r"""Compute the n-th Ising residue moment:

    I_n = sum_{(Delta, d)} d * (log Delta)^n * w_{1/2, rho, u0}(Delta)

    summed over Ising primaries (Delta = 1/16, 1/2) with degeneracies.
    """
    _set_dps()
    rho = mpc(rho) if not isinstance(rho, mpc) else rho
    u0 = mpf(u0)

    total = mpc(0)
    for Delta, deg in ISING_PRIMARIES:
        w = paired_residue_kernel(ISING_C, rho, u0, Delta)
        total += deg * power(mplog(Delta), n) * w
    return total


# =====================================================================
# Section 11: W_3 multi-channel quartic block
# =====================================================================

def w3_multichannel_hankel(c: Union[float, mpf], mu4_22, mu4_33, mu4_23) -> mpmatrix:
    r"""Build the 6x6 multi-channel Hankel matrix for W_3.

    The W_3 algebra has two channels: spin-2 (stress tensor T) and spin-3 (W).
    The full quartic block mixes moments from both channels.

    The 6x6 matrix is organized as two 3x3 blocks (spin-2 and spin-3)
    plus cross-blocks:

      M = [[M_22,  M_23],
           [M_23^T, M_33]]

    where M_22 is the spin-2 Hankel (Virasoro part),
          M_33 is the spin-3 Hankel (pure spin-3),
          M_23 is the cross-moment block.

    Arguments:
      c: central charge
      mu4_22: raw quartic moment in spin-2 channel
      mu4_33: raw quartic moment in spin-3 channel
      mu4_23: mixed quartic moment (spin-2 x spin-3 cross-channel)
    """
    _set_dps()
    c = mpf(c)
    H2, C2, Q2 = virasoro_shadow_data(c)
    H3, C3 = w3_pure_spin3_data(c)
    mu4_22 = mpf(mu4_22)
    mu4_33 = mpf(mu4_33)
    mu4_23 = mpf(mu4_23)

    # Build 6x6 matrix
    # Rows/cols 0-2: spin-2 (centered: 1, 0, H2)
    # Rows/cols 3-5: spin-3 (centered: 1, 0, H3)
    M = mpmatrix(6, 6)

    # Spin-2 block (top-left 3x3)
    M[0, 0] = 1; M[0, 1] = 0; M[0, 2] = H2
    M[1, 0] = 0; M[1, 1] = H2; M[1, 2] = C2
    M[2, 0] = H2; M[2, 1] = C2; M[2, 2] = mu4_22

    # Spin-3 block (bottom-right 3x3)
    M[3, 3] = 1; M[3, 4] = 0; M[3, 5] = H3
    M[4, 3] = 0; M[4, 4] = H3; M[4, 5] = C3
    M[5, 3] = H3; M[5, 4] = C3; M[5, 5] = mu4_33

    # Cross blocks (off-diagonal 3x3)
    # The cross moments are organized as inner products between
    # centered spin-2 and spin-3 moments.
    # Leading cross-moments: (1,1)=correlation at order 0,
    # (mu_2 x mu_2)=H2*H3 at diagonal, etc.
    # Cross mu4 appears at position (2,5) and (5,2).
    # For a generic cross-structure, the zeroth cross-moment
    # is the overlap <v_2, v_3> which we normalize to 0
    # (orthogonal channels).
    M[0, 3] = 0; M[0, 4] = 0; M[0, 5] = 0
    M[1, 3] = 0; M[1, 4] = 0; M[1, 5] = 0
    M[2, 3] = 0; M[2, 4] = 0; M[2, 5] = mu4_23

    M[3, 0] = 0; M[3, 1] = 0; M[3, 2] = 0
    M[4, 0] = 0; M[4, 1] = 0; M[4, 2] = 0
    M[5, 0] = 0; M[5, 1] = 0; M[5, 2] = mu4_23

    return M


def w3_quartic_resonance_divisor(c: Union[float, mpf]) -> mpf:
    r"""Compute the quartic resonance divisor for W_3 pure spin-3 slice.

    On the pure spin-3 slice, C_3 = 0, so:
      Sigma_2 = mu_4 - 0 - H_3^2 = mu_4 - (c/3)^2

    The quartic contact on the spin-3 slice is:
      Q_3^ct = 10/[c(5c+22)] * 22/(5c+22)
             = 220 / [c * (5c+22)^2]

    (This comes from the W_3 OPE: the spin-3 self-coupling
     has an additional factor from the Jacobi identity constraint.
     The W_3 algebra has the constraint 22+5c != 0 (Zamolodchikov).)

    The resonance divisor is where Q_3^ct has poles: c*(5c+22)^2 = 0,
    i.e. c = 0 or c = -22/5 (double).
    """
    _set_dps()
    c = mpf(c)
    return mpf(220) / (c * (5 * c + 22)**2)


def w3_spin3_mu4(c: Union[float, mpf]) -> mpf:
    r"""Compute mu_4 on the pure spin-3 slice of W_3.

    mu_4 = H_3^2 + Q_3^ct = (c/3)^2 + 220/[c*(5c+22)^2]
    """
    _set_dps()
    c = mpf(c)
    H3 = c / 3
    Q3ct = w3_quartic_resonance_divisor(c)
    return H3**2 + Q3ct


# =====================================================================
# Section 12: Compatibility ratios
# =====================================================================

def compatibility_ratio_pot(
    c: Union[float, mpf],
    m3_sharp: Union[float, mpf],
    s4_res: Union[float, mpf],
) -> mpf:
    r"""Potential-side compatibility ratio:

    C_4^pot(c, rho; u0) = c(5c+22)/10 * S_4^res

    where S_4^res is the Schur complement of the residue moment matrix.
    On-line (RH true): C_4^pot should equal 1.
    """
    _set_dps()
    c = mpf(c)
    s4_res = mpf(s4_res)
    return c * (5 * c + 22) / 10 * s4_res


def compatibility_ratio_gram(
    c: Union[float, mpf],
    s4_res: Union[float, mpf],
) -> mpf:
    r"""Gram-side compatibility ratio:

    C_4^Gram(c, rho; u0) = 10 / [c(5c+22)] / S_4^res

    Reciprocal of C_4^pot.
    """
    _set_dps()
    c = mpf(c)
    s4_res = mpf(s4_res)
    Q_vir = mpf(10) / (c * (5 * c + 22))
    return Q_vir / s4_res


def ising_compatibility_ratio_gram(
    rho: Union[complex, mpc],
    u0: Union[float, mpf] = 2,
) -> mpc:
    r"""Compute the Gram-side compatibility ratio for the Ising model (c = 1/2).

    Steps:
      1. Compute residue moments I_0, ..., I_4 at the given zero rho
      2. Build the 3x3 moment matrix (centered)
      3. Extract Schur complement S_4^res
      4. Compare to Q^ct_Vir = 10/[c(5c+22)]

    NOTE: This is a toy computation since the Ising model has only
    2 scalar primaries.  The 'moments' I_n are discrete sums over
    just 2 terms, not integrals over a continuous spectral measure.
    The result is an approximation illustrating the on-line/off-line
    distinction rather than a rigorous verification.
    """
    _set_dps()
    c = ISING_C
    rho = mpc(rho) if not isinstance(rho, mpc) else rho
    u0 = mpf(u0)

    # Compute raw moments
    I = [ising_residue_moment(n, rho, u0) for n in range(5)]

    # Centering: shift so that mu_0 -> 1, mu_1 -> 0
    # mu_0 = I_0, mu_1 = I_1
    # Centered moments: tilde_mu_k = sum_{j=0}^{k} C(k,j) (-mu_1/mu_0)^j mu_k/mu_0
    # For simplicity, since this is discrete with few terms, work directly.
    if fabs(I[0]) < mpf('1e-40'):
        return mpc('nan')

    # Normalize: mu_k -> I_k / I_0
    mu = [I[k] / I[0] for k in range(5)]
    # mu[0] = 1, mu[1] = I_1/I_0

    # Center: shift by mu[1]
    # mu_2^c = mu[2] - mu[1]^2
    # mu_3^c = mu[3] - 3*mu[2]*mu[1] + 2*mu[1]^3
    # mu_4^c = mu[4] - 4*mu[3]*mu[1] + 6*mu[2]*mu[1]^2 - 3*mu[1]^4
    m1 = mu[1]
    mu2c = mu[2] - m1**2
    mu3c = mu[3] - 3 * mu[2] * m1 + 2 * m1**3
    mu4c = mu[4] - 4 * mu[3] * m1 + 6 * mu[2] * m1**2 - 3 * m1**4

    if fabs(mu2c) < mpf('1e-40'):
        return mpc('nan')

    # Schur complement
    S4 = mu4c - mu3c**2 / mu2c - mu2c**2

    # Gram ratio
    Q_vir = mpf(10) / (c * (5 * c + 22))
    return Q_vir / S4


# =====================================================================
# Section 13: Virasoro Hankel determinant and resonance divisor
# =====================================================================

def virasoro_hankel_det(c: Union[float, mpf]) -> mpf:
    r"""Compute D_2^Vir = 5/(5c+22).

    From thm:schur-complement-quartic + prop:virasoro-quartic-determinant.
    """
    _set_dps()
    c = mpf(c)
    return mpf(5) / (5 * c + 22)


def virasoro_resonance_divisor(c: Union[float, mpf]) -> str:
    r"""The quartic resonance divisor for Virasoro: c(5c+22) = 0.

    Returns the roots as a string for documentation.
    Actual poles: c = 0 and c = -22/5.
    """
    return "c(5c+22) = 0: poles at c = 0 and c = -22/5"


# =====================================================================
# Section 14: First zeta zero utilities
# =====================================================================

def first_zeta_zero(dps: int = DEFAULT_DPS) -> mpc:
    r"""Return rho_1 = 1/2 + i*14.134725... (first nontrivial zero of zeta)."""
    mp.dps = dps
    return zetazero(1)


def nth_zeta_zero(n: int, dps: int = DEFAULT_DPS) -> mpc:
    r"""Return the n-th nontrivial zero of the Riemann zeta function."""
    mp.dps = dps
    return zetazero(n)


# =====================================================================
# Section 15: W_N weight multisets
# =====================================================================

def wn_weights(N: int) -> List[int]:
    """Weight multiset for W_N: {2, 3, ..., N}."""
    return list(range(2, N + 1))


def heisenberg_weights() -> List[int]:
    """Weight multiset for Heisenberg: {1}."""
    return [1]


def virasoro_weights() -> List[int]:
    """Weight multiset for Virasoro = W_2: {2}."""
    return [2]


def betagamma_weights() -> List[int]:
    """Weight multiset for betagamma: {1, 1}."""
    return [1, 1]


def affine_weights(dim_g: int) -> List[int]:
    """Weight multiset for V_k(g): {1^dim(g)}."""
    return [1] * dim_g


# =====================================================================
# Section 16: Li coefficient asymptotic target
# =====================================================================

def li1_asymptotic_target(dps: int = DEFAULT_DPS) -> mpf:
    r"""Compute the asymptotic target for lambda_1(W_N) + log(N):

    lim_{N -> infty} (lambda_1(W_N) + log N) = zeta'(2)/zeta(2) + 1

    Numerically: approx 0.4300.
    """
    mp.dps = dps
    return mpdiff(mpzeta, mpf(2)) / mpzeta(mpf(2)) + 1


# =====================================================================
# Section 17: Convenience: full shadow-arithmetic package
# =====================================================================

def full_virasoro_package(c: Union[float, mpf]) -> Dict:
    r"""Compute the full genus-1 modular datum for Virasoro at central charge c.

    Returns: dict with keys
      kappa, H, C_cubic, Q_ct, mu4, D2, Sigma2, resonance_divisor
    """
    _set_dps()
    c = mpf(c)
    H, C_cubic, Q_ct = virasoro_shadow_data(c)
    mu4 = virasoro_mu4(c)
    D2 = virasoro_hankel_det(c)
    Sigma2 = schur_complement(H, C_cubic, mu4)
    return {
        'c': c,
        'kappa': H,  # kappa = c/2
        'H': H,
        'C_cubic': C_cubic,
        'Q_ct': Q_ct,
        'mu4': mu4,
        'D2': D2,
        'Sigma2': Sigma2,
        'resonance_divisor': 'c(5c+22) = 0',
    }
