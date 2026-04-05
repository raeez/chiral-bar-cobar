r"""Lee-Yang zeros, lattice partition zeros, and shadow partition zeros.

MATHEMATICAL FRAMEWORK
======================

1. LATTICE THETA FUNCTIONS AND THEIR ZEROS

For an even positive-definite lattice Lambda of rank r, the theta function is

    Theta_Lambda(q) = sum_{v in Lambda} q^{(v,v)/2}

where q = e^{2 pi i tau}, tau in H (upper half-plane).  The lattice VOA
partition function is Z_Lambda(q) = Theta_Lambda(q) / eta(q)^r.

The zeros of Theta_Lambda(q) in the disk |q| < 1 determine the zeros of
the partition function (eta has no zeros in the unit disk, only the
essential singularity at q = 0).

KEY FACT (Rankin 1977, Borcherds 1995): For the E_8 root lattice, the
theta function Theta_{E_8}(q) = E_4(tau) (the normalized Eisenstein
series of weight 4).  E_4 = 1 + 240*sum sigma_3(n)q^n has ALL POSITIVE
Fourier coefficients, so it has no zeros on the POSITIVE REAL q-axis
(0 < q < 1).  However, E_4(tau) DOES have a zero at tau = rho = e^{2pi i/3}
(the cube root of unity), which lies in the fundamental domain boundary.
The corresponding q-value is |q| = e^{-pi*sqrt(3)} < 1.
For the Niemeier lattice analysis, the key property is that ALL Fourier
coefficients sigma_3(n) > 0, which prevents real-axis cancellation.

For A_1 = Z*sqrt(2): Theta_{A_1}(q) = sum_{n in Z} q^{n^2} = theta_3(0|tau)
(Jacobi theta function).  Its zeros in |q| < 1 are well-known:
they lie on the negative real axis (q real negative), at
q = -e^{-pi}, -e^{-3pi}, -e^{-5pi}, ... (approximately).

For A_2: Theta_{A_2}(q) = sum_{m,n} q^{m^2+mn+n^2}.  The zeros are more
complex and lie on curves in the upper half-plane.

For D_4: Theta_{D_4}(q) = (theta_3(0|tau)^4 + theta_4(0|tau)^4 + theta_2(0|tau)^4)/2.

2. LEE-YANG ZEROS FOR THE ISING MODEL

The Ising partition function on a finite lattice with N sites is

    Z_N(beta, h) = sum_{sigma in {-1,+1}^N} exp(-beta * H(sigma) + h * sum_i sigma_i)

In the fugacity variable z = e^{2h}:

    Z_N(beta, z) = polynomial in z of degree N

The Lee-Yang Circle Theorem (1952): For FERROMAGNETIC interactions
(J_{ij} >= 0), all zeros of Z_N(beta, z) lie on the unit circle |z| = 1.

For the 1D Ising chain with periodic boundary conditions:

    Z_N = lambda_+^N + lambda_-^N

where lambda_pm = e^{beta J} cosh(h) +/- sqrt(e^{2 beta J} sinh^2(h) + e^{-2 beta J})
are the transfer matrix eigenvalues.

The zeros in z = e^{2h} satisfy lambda_+ = -lambda_- * e^{2 pi i k/N},
k = 0, ..., N-1.

3. SHADOW PARTITION ZEROS

The shadow partition function (formal series in genus variable):

    Z^{sh}(q) = exp(sum_{g=1}^{g_max} F_g * q^g)

where F_g = kappa * lambda_g^{FP} (Faber-Pandharipande values).

The Faber-Pandharipande values lambda_g^{FP} are the intersection numbers
int_{M_g} lambda_g, which satisfy:

    lambda_1^{FP} = 1/24
    lambda_2^{FP} = 7/5760    (Convention: Faber-Pandharipande, NOT 1/1152)
    lambda_3^{FP} = 31/967680
    ...

The generating function is sum_{g>=1} lambda_g^{FP} * x^{2g} = x^2/(e^x - 1) - 1 + x/2
(related to the A-hat genus).

IMPORTANT (AP46): eta(q) = q^{1/24} * prod_{n>=1}(1-q^n).  The q^{1/24}
is NOT optional.

4. FISHER ZEROS

Temperature zeros (Fisher 1965): zeros of Z(beta) for complex inverse
temperature beta = 1/T.  For the 2D Ising model on an L x L lattice,
Fisher zeros pinch the real axis at beta_c = (1/2)*log(1+sqrt(2))
as L -> infinity.

5. YANG-BAXTER PARTITION ZEROS

For the XXX spin chain with Bethe ansatz, the partition function
(transfer matrix eigenvalue) is

    T(u) = prod_{i=1}^M (u - u_i + eta/2) / (u - u_i - eta/2)
           + prod_{i=1}^M (u - u_i - eta/2) / (u - u_i + eta/2)

where u_i are Bethe roots satisfying the Bethe ansatz equations.

Setting eta = i*gamma_n where gamma_n = Im(rho_n) (imaginary part of the
n-th nontrivial Riemann zeta zero) connects spin chain spectral data to
number theory.  This is the Benjamin-Chang mechanism (speculative but
computationally verifiable at finite system size).

6. ZERO DENSITY AND JULIA SETS

The density of zeros rho(q) = lim_{L->inf} (#zeros in region) / L^2
defines a continuous measure supported on the accumulation curve of zeros.

Under renormalization group (RG) flow (block-spin transformation),
partition function zeros map to themselves.  The repelling fixed points
of this map generate a Julia set.

References:
    Lee-Yang 1952: Phys Rev 87, 410
    Fisher 1964: in Lectures in Theoretical Physics, Vol. 7C
    Borcherds 1995: alg-geom/9501006
    Rankin 1977: "Modular Forms and Functions"
    Faber-Pandharipande 2000: math/0012064
    Itzykson-Luck-Derrida 1986: J Stat Phys 45, 587 (Fisher zeros)
    Matveev-Shrock 1995: J Phys A 28, 5235 (complex-T zeros)
"""

from __future__ import annotations

import cmath
import math
from typing import Optional

import numpy as np
from numpy.polynomial import polynomial as P


# ============================================================================
# 0. Constants and Faber-Pandharipande values
# ============================================================================

# Faber-Pandharipande lambda_g^FP values: int_{M_g} lambda_g
# Convention: Faber-Pandharipande (AP38).
# Source: the generating function sum_{g>=1} lambda_g x^{2g} is related
# to the Bernoulli numbers via the A-hat genus.
# B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30, B_10 = 5/66, B_12 = -691/2730
# lambda_g^FP = |B_{2g}| / (2g * (2g)!)  (NOT |B_{2g}|/(4g*(2g)!))
# Verification: lambda_1 = |B_2|/(2*2!) = (1/6)/4 = 1/24.  CHECK.
# lambda_2 = |B_4|/(4*4!) = (1/30)/96 = 1/2880.
# WAIT: this gives 1/2880, not 7/5760.  Let me recompute.
#
# The correct formula from the A-hat genus is:
# sum_{g>=0} lambda_g x^{2g} = integral over fibers of A-hat class
# From Faber-Pandharipande (math/0012064, Theorem 2):
# lambda_g = (-1)^g |B_{2g}| / (2g * (2g-2)! * 2)  ... NO.
#
# Let me just use the known values directly.
# lambda_1 = 1/24 (universally agreed)
# lambda_2 = 1/1152 ... NO, this was the WRONG convention (AP38).
# lambda_2 = 7/5760 ... this is from Faber (1999, Thm 3).
#
# Actually: int_{M_2} lambda_2 = 1/240.  But lambda_2^{FP} in the sense
# of the CHERN CHARACTER coefficient is different.
#
# From the manuscript (CLAUDE.md): lambda_2^FP = 7/5760.
# From Faber 1999: int_{M_2} lambda_2 = 1/240.
# These are different normalizations.  The FP value in the manuscript
# refers to the coefficient in the A-hat expansion.
#
# A-hat(ix) = (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760 - ...
# So the coefficients of the EXPANSION of A-hat are:
#   g=0: 1
#   g=1: -1/24  (but F_1 = kappa/24 is POSITIVE, so F_g = kappa * |coeff|)
#   g=2: 7/5760
#   g=3: 31/967680
#
# Verification of 7/5760:
# A-hat(x) = 1 - (1/24)p_1 + (1/5760)(7p_1^2 - 4p_2) + ...
# For a single bundle: p_1 = c_1^2, p_2 = c_2, so the coefficient
# of the degree-4 term with p_1^2 only is 7/5760.
# But we need the expansion of (x/2)/sinh(x/2):
# (x/2)/sinh(x/2) = 1 - x^2/24 + 7x^4/5760 - 31x^6/967680 + ...
# Let me verify: sinh(x/2) = x/2 + x^3/48 + x^5/3840 + ...
# So (x/2)/sinh(x/2) = 1/(1 + x^2/24 + x^4/1920 + ...)
#   = 1 - x^2/24 + (x^2/24)^2 - x^4/1920 + ...
#   = 1 - x^2/24 + x^4/576 - x^4/1920 + ...
#   = 1 - x^2/24 + x^4*(1/576 - 1/1920)
#   = 1 - x^2/24 + x^4*(1920 - 576)/(576*1920)
#   = 1 - x^2/24 + x^4*1344/1105920
#   = 1 - x^2/24 + x^4*7/5760
# CONFIRMED: 7/5760.

FABER_PANDHARIPANDE = {
    1: 1 / 24,
    2: 7 / 5760,
    3: 31 / 967680,
    4: 127 / 154828800,
    5: 73 / 3503554560,
}

# Bernoulli numbers B_{2g} (conventional sign: B_2 = 1/6 > 0)
BERNOULLI_2G = {
    1: 1 / 6,       # B_2
    2: -1 / 30,     # B_4
    3: 1 / 42,      # B_6
    4: -1 / 30,     # B_8
    5: 5 / 66,      # B_10
}


def faber_pandharipande(g: int) -> float:
    """Return lambda_g^{FP}, the coefficient in the A-hat expansion.

    These are the coefficients of x^{2g} in (x/2)/sinh(x/2):
      g=1: 1/24, g=2: 7/5760, g=3: 31/967680, ...

    Convention: Faber-Pandharipande (AP38).  NOT the Mumford convention.
    """
    if g in FABER_PANDHARIPANDE:
        return FABER_PANDHARIPANDE[g]
    # For higher g, compute from the expansion of (x/2)/sinh(x/2)
    # via Taylor series.  The coefficients alternate in sign starting
    # from g=1 (negative), but we take absolute values since
    # F_g = kappa * |coeff| is positive.
    # Actually the expansion itself already gives the right sign pattern.
    # Let's just not go beyond precomputed for now.
    raise ValueError(f"Faber-Pandharipande value not precomputed for g={g}")


# ============================================================================
# 1. LATTICE THETA FUNCTIONS
# ============================================================================

def theta_3(q: complex, n_terms: int = 200) -> complex:
    """Jacobi theta_3(0|tau) = sum_{n=-N}^{N} q^{n^2}, q = e^{2pi i tau}.

    This is the theta function of the rank-1 lattice Z (or equivalently
    A_1 after appropriate normalization).
    """
    result = 1.0 + 0j  # n=0 term
    for n in range(1, n_terms + 1):
        term = q ** (n * n)
        result += 2 * term  # n and -n contribute equally
    return result


def theta_2(q: complex, n_terms: int = 200) -> complex:
    """Jacobi theta_2(0|tau) = 2 * sum_{n=0}^{N} q^{(n+1/2)^2}."""
    result = 0.0 + 0j
    for n in range(n_terms):
        m = n + 0.5
        result += q ** (m * m)
    return 2 * result


def theta_4(q: complex, n_terms: int = 200) -> complex:
    """Jacobi theta_4(0|tau) = sum_{n=-N}^{N} (-1)^n q^{n^2}."""
    result = 1.0 + 0j  # n=0
    for n in range(1, n_terms + 1):
        term = q ** (n * n)
        result += 2 * ((-1) ** n) * term
    return result


def theta_A1(q: complex, n_terms: int = 200) -> complex:
    """Theta function of the A_1 root lattice = Z*sqrt(2).

    Theta_{A_1}(q) = sum_{n in Z} q^{n^2} = theta_3(0|tau).

    Note: the A_1 root lattice has (v,v) = 2n^2 for v = n*alpha,
    alpha = sqrt(2).  So Theta_{A_1}(q) = sum q^{n^2}.
    """
    return theta_3(q, n_terms)


def theta_A2(q: complex, n_terms: int = 100) -> complex:
    """Theta function of the A_2 root lattice.

    The A_2 root lattice has Gram matrix [[2, -1], [-1, 2]].
    Theta_{A_2}(q) = sum_{m,n in Z} q^{m^2 + m*n + n^2}.
    """
    result = 0.0 + 0j
    for m in range(-n_terms, n_terms + 1):
        for n in range(-n_terms, n_terms + 1):
            exponent = m * m + m * n + n * n
            if exponent <= 4 * n_terms:  # convergence cutoff
                result += q ** exponent
    return result


def theta_D4(q: complex, n_terms: int = 10) -> complex:
    """Theta function of the D_4 root lattice.

    D_4 = {(n_1,...,n_4) in Z^4 : n_1+n_2+n_3+n_4 even}.
    Theta_{D_4}(q) = sum_{v in D_4} q^{|v|^2/2}
                   = sum_{n_i, sum even} q^{(n_1^2+...+n_4^2)/2}.

    Direct summation over the lattice with convergence cutoff.
    """
    result = 0.0 + 0j
    N = n_terms
    for n1 in range(-N, N + 1):
        for n2 in range(-N, N + 1):
            for n3 in range(-N, N + 1):
                for n4 in range(-N, N + 1):
                    if (n1 + n2 + n3 + n4) % 2 == 0:
                        norm2 = n1 * n1 + n2 * n2 + n3 * n3 + n4 * n4
                        result += q ** (norm2 / 2)
    return result


def sigma_k(n: int, k: int) -> int:
    """Divisor function sigma_k(n) = sum_{d|n} d^k."""
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def theta_E8(q: complex, n_terms: int = 200) -> complex:
    """Theta function of the E_8 root lattice.

    Theta_{E_8}(q) = E_4(tau) = 1 + 240 * sum_{n=1}^{N} sigma_3(n) * q^n

    where sigma_3(n) = sum_{d|n} d^3 and q = e^{2 pi i tau}.

    This is the Eisenstein series of weight 4 for SL(2,Z).  The equality
    Theta_{E_8} = E_4 is a classical result (Jacobi, cf. Conway-Sloane
    Chapter 4).

    Direct q-expansion via divisor sums (avoids nome convention issues
    with the Jacobi theta formula).
    """
    result = 1.0 + 0j
    for n in range(1, n_terms + 1):
        s3 = sigma_k(n, 3)
        term = 240 * s3 * q ** n
        result += term
        if abs(term) < 1e-30:
            break
    return result


def dedekind_eta(q: complex, n_terms: int = 500) -> complex:
    """Dedekind eta function: eta(q) = q^{1/24} * prod_{n=1}^{N} (1 - q^n).

    CRITICAL (AP46): the q^{1/24} prefactor is NOT optional.
    """
    if abs(q) >= 1.0:
        raise ValueError(f"|q| = {abs(q)} >= 1; eta undefined outside unit disk")
    # q^{1/24}
    result = q ** (1 / 24)
    for n in range(1, n_terms + 1):
        result *= (1 - q ** n)
    return result


def lattice_partition_function(lattice: str, q: complex, n_terms: int = 200) -> complex:
    """Partition function Z_Lambda(q) = Theta_Lambda(q) / eta(q)^rank."""
    theta_funcs = {
        'A1': (theta_A1, 1),
        'A2': (theta_A2, 2),
        'D4': (theta_D4, 4),
        'E8': (theta_E8, 8),
    }
    if lattice not in theta_funcs:
        raise ValueError(f"Unknown lattice: {lattice}")
    theta_func, rank = theta_funcs[lattice]
    theta = theta_func(q, n_terms)
    eta = dedekind_eta(q, n_terms)
    return theta / eta ** rank


# ============================================================================
# 2. LATTICE THETA ZEROS via Newton's method
# ============================================================================

def find_theta_zeros(lattice: str, q_init_list: list[complex],
                     n_terms: int = 200, tol: float = 1e-10,
                     max_iter: int = 100) -> list[complex]:
    """Find zeros of Theta_Lambda(q) in |q| < 1 via Newton's method.

    Parameters
    ----------
    lattice : str
        One of 'A1', 'A2', 'D4', 'E8'.
    q_init_list : list of complex
        Initial guesses for Newton's method.
    n_terms : int
        Number of terms in the theta function evaluation.
    tol : float
        Convergence tolerance |f(q)| < tol.
    max_iter : int
        Maximum Newton iterations.

    Returns
    -------
    List of converged zeros with |q| < 1 and |f(q)| < tol.
    """
    theta_funcs = {
        'A1': theta_A1,
        'A2': theta_A2,
        'D4': theta_D4,
        'E8': theta_E8,
    }
    if lattice not in theta_funcs:
        raise ValueError(f"Unknown lattice: {lattice}")
    f = theta_funcs[lattice]

    zeros = []
    eps = 1e-8  # for numerical derivative
    for q0 in q_init_list:
        q = q0
        for _ in range(max_iter):
            fq = f(q, n_terms)
            if abs(fq) < tol:
                break
            # Numerical derivative df/dq
            dfq = (f(q + eps, n_terms) - f(q - eps, n_terms)) / (2 * eps)
            if abs(dfq) < 1e-15:
                break
            q = q - fq / dfq
        if abs(q) < 1.0 and abs(f(q, n_terms)) < tol * 100:
            # Deduplicate
            is_new = True
            for z in zeros:
                if abs(q - z) < 1e-6:
                    is_new = False
                    break
            if is_new:
                zeros.append(q)
    return zeros


# ============================================================================
# 3. LEE-YANG ZEROS: 1D Ising model
# ============================================================================

def ising_1d_transfer_eigenvalues(beta: float, h: complex) -> tuple[complex, complex]:
    """Transfer matrix eigenvalues for 1D Ising with coupling J=1.

    lambda_pm = e^{beta} cosh(h) +/- sqrt(e^{2beta} sinh^2(h) + e^{-2beta})

    Parameters
    ----------
    beta : float
        Inverse temperature (beta = J/T with J=1).
    h : complex
        External magnetic field (can be complex for Lee-Yang).
    """
    eb = cmath.exp(beta)
    emb = cmath.exp(-beta)
    ch = cmath.cosh(h)
    sh = cmath.sinh(h)
    discriminant = eb * eb * sh * sh + emb * emb
    sq = cmath.sqrt(discriminant)
    lam_plus = eb * ch + sq
    lam_minus = eb * ch - sq
    return lam_plus, lam_minus


def ising_1d_partition(N: int, beta: float, h: complex) -> complex:
    """Partition function of 1D Ising chain with N sites, periodic BC.

    Z_N = lambda_+^N + lambda_-^N
    """
    lp, lm = ising_1d_transfer_eigenvalues(beta, h)
    return lp ** N + lm ** N


def ising_1d_lee_yang_zeros(N: int, beta: float, n_search: int = 500,
                            tol: float = 1e-10) -> list[complex]:
    """Find Lee-Yang zeros of the 1D Ising model in the fugacity z = e^{2h}.

    For the 1D model with N sites, the zeros in z lie on the unit circle
    |z| = 1 (Lee-Yang theorem for ferromagnetic interactions).

    We parametrize z = e^{i*phi} and find zeros of Z_N(beta, h(z)).

    Returns list of z-values (complex) that are zeros.
    """
    zeros = []
    # Scan the unit circle for sign changes / small values
    for k in range(n_search):
        phi = 2 * math.pi * k / n_search
        z = cmath.exp(1j * phi)
        h = cmath.log(z) / 2  # z = e^{2h}, so h = log(z)/2
        val = ising_1d_partition(N, beta, h)
        if abs(val) < tol:
            zeros.append(z)

    # Refine with Newton's method on the circle
    refined = []
    for k in range(n_search):
        phi = 2 * math.pi * k / n_search
        dphi = 2 * math.pi / n_search

        z1 = cmath.exp(1j * phi)
        z2 = cmath.exp(1j * (phi + dphi))
        h1 = cmath.log(z1) / 2
        h2 = cmath.log(z2) / 2
        v1 = ising_1d_partition(N, beta, h1)
        v2 = ising_1d_partition(N, beta, h2)

        # Check for sign change in real part (crude but effective for |z|=1)
        if v1.real * v2.real < 0 or v1.imag * v2.imag < 0:
            # Bisection on the angle
            phi_lo, phi_hi = phi, phi + dphi
            for _ in range(60):
                phi_mid = (phi_lo + phi_hi) / 2
                z_mid = cmath.exp(1j * phi_mid)
                h_mid = cmath.log(z_mid) / 2
                v_mid = ising_1d_partition(N, beta, h_mid)
                if v1.real * v_mid.real < 0:
                    phi_hi = phi_mid
                    v2 = v_mid
                else:
                    phi_lo = phi_mid
                    v1 = v_mid
            z_zero = cmath.exp(1j * (phi_lo + phi_hi) / 2)
            # Verify
            h_check = cmath.log(z_zero) / 2
            if abs(ising_1d_partition(N, beta, h_check)) < 0.1:
                is_new = True
                for zz in refined:
                    if abs(z_zero - zz) < 1e-4:
                        is_new = False
                        break
                if is_new:
                    refined.append(z_zero)
    return refined


def verify_lee_yang_circle(zeros: list[complex], tol: float = 1e-3) -> bool:
    """Verify that all Lee-Yang zeros lie on the unit circle |z| = 1."""
    if not zeros:
        return True
    return all(abs(abs(z) - 1.0) < tol for z in zeros)


# ============================================================================
# 4. SHADOW PARTITION ZEROS
# ============================================================================

def shadow_free_energies(kappa: float, g_max: int = 5) -> dict[int, float]:
    """Shadow free energies F_g = kappa * lambda_g^{FP}.

    Convention: F_g > 0 for kappa > 0 (AP22).  The A-hat generating
    function gives alternating-sign coefficients; the shadow tower
    uses absolute values.

    Parameters
    ----------
    kappa : float
        Modular characteristic of the algebra.
        For Virasoro: kappa = c/2.
        For Heisenberg: kappa = k (the level).
        For affine KM: kappa = dim(g)*(k+h^v)/(2*h^v).
        (AP48: kappa != c/2 in general!)
    g_max : int
        Maximum genus.
    """
    result = {}
    for g in range(1, g_max + 1):
        if g in FABER_PANDHARIPANDE:
            result[g] = abs(kappa * FABER_PANDHARIPANDE[g])
        else:
            break
    return result


def shadow_partition_polynomial(kappa: float, g_max: int = 5,
                                n_terms: int = 20) -> np.ndarray:
    """Compute the polynomial approximation to Z^{sh}(q).

    Z^{sh}(q) = exp(sum_{g=1}^{g_max} F_g * q^g)

    We expand this as a polynomial in q up to degree n_terms by
    exponentiating the truncated series.

    Returns the polynomial coefficients [a_0, a_1, ..., a_{n_terms}]
    so that Z^{sh}(q) ~ sum a_k q^k.
    """
    F = shadow_free_energies(kappa, g_max)

    # Build the exponent polynomial: sum F_g * q^g
    exponent_coeffs = np.zeros(n_terms + 1)
    for g, fg in F.items():
        if g <= n_terms:
            exponent_coeffs[g] = fg

    # Exponentiate the polynomial: exp(p(q)) truncated to degree n_terms
    # Use the recursion: if Z = exp(P), then Z' = P' * Z
    # Z_0 = 1, Z_k = (1/k) * sum_{j=1}^{k} j * P_j * Z_{k-j}
    Z_coeffs = np.zeros(n_terms + 1)
    Z_coeffs[0] = 1.0
    for k in range(1, n_terms + 1):
        s = 0.0
        for j in range(1, k + 1):
            if j < len(exponent_coeffs):
                s += j * exponent_coeffs[j] * Z_coeffs[k - j]
        Z_coeffs[k] = s / k

    return Z_coeffs


def shadow_partition_zeros(kappa: float, g_max: int = 5,
                           n_terms: int = 20) -> np.ndarray:
    """Find zeros of the shadow partition polynomial in the q-plane.

    Returns array of complex zeros.
    """
    coeffs = shadow_partition_polynomial(kappa, g_max, n_terms)
    # Find roots of the polynomial sum a_k q^k = 0
    # np.polynomial.polynomial.polyroots uses coefficients [a_0, a_1, ...]
    # But a_0 = 1, so we can divide: 1 + a_1 q + ... = 0
    # The roots are the zeros of the polynomial.
    if len(coeffs) < 2:
        return np.array([])
    roots = P.polyroots(coeffs)
    return roots


def shadow_partition_value(kappa: float, q: complex, g_max: int = 5) -> complex:
    """Evaluate Z^{sh}(q) = exp(sum F_g q^g) at a specific q."""
    F = shadow_free_energies(kappa, g_max)
    exponent = sum(fg * q ** g for g, fg in F.items())
    return cmath.exp(exponent)


# ============================================================================
# 5. FISHER ZEROS (temperature zeros)
# ============================================================================

def ising_2d_exact_partition_small(L: int, beta: complex) -> complex:
    """Exact 2D Ising partition function on L x L torus (small L).

    For a SQUARE lattice with periodic boundary conditions.

    Uses the Onsager solution: the partition function factors into
    a product over momenta.  For finite L:

    Z = 2^{L^2} * (cosh(2*beta))^{L^2} *
        prod_{k1,k2} [1 - t_1 cos(2*pi*k1/L) - t_2 cos(2*pi*k2/L)]^{1/2}

    where t_1 = t_2 = tanh(beta) for the isotropic model.

    For simplicity, we use the transfer matrix approach for L <= 8.
    """
    # For very small L, use direct enumeration
    if L > 6:
        raise ValueError("Direct enumeration too expensive for L > 6")

    N = L * L
    Z = 0.0 + 0j
    # Enumerate all 2^N spin configurations
    for config in range(2 ** N):
        energy = 0.0
        for i in range(L):
            for j in range(L):
                site = i * L + j
                spin = 1 if (config >> site) & 1 else -1
                # Right neighbor (periodic)
                right = i * L + (j + 1) % L
                spin_r = 1 if (config >> right) & 1 else -1
                # Down neighbor (periodic)
                down = ((i + 1) % L) * L + j
                spin_d = 1 if (config >> down) & 1 else -1
                energy -= spin * spin_r + spin * spin_d
        Z += cmath.exp(-beta * energy)
    return Z


def fisher_zeros_1d_ising(N: int, J: float = 1.0) -> list[complex]:
    """Fisher zeros (temperature zeros) of the 1D Ising model.

    Z_N(beta) = 2^N * (cosh(beta*J))^N * [1 + (tanh(beta*J))^N]

    For periodic BC with h = 0.
    The zeros satisfy tanh(beta*J)^N = -1, i.e.,
    tanh(beta*J) = exp(i*pi*(2k+1)/N), k = 0, ..., N-1.

    Returns list of complex beta values.
    """
    zeros = []
    for k in range(N):
        # tanh(beta*J) = exp(i*pi*(2k+1)/N)
        w = cmath.exp(1j * math.pi * (2 * k + 1) / N)
        # beta*J = arctanh(w) = (1/2) * log((1+w)/(1-w))
        if abs(1 - w) > 1e-15:
            beta_J = 0.5 * cmath.log((1 + w) / (1 - w))
            beta = beta_J / J
            zeros.append(beta)
    return zeros


def fisher_zeros_2d_ising_small(L: int) -> list[complex]:
    """Find Fisher zeros of the 2D Ising model on small L x L lattice.

    Uses Newton's method on the direct-enumeration partition function.
    Only practical for L <= 4.
    """
    if L > 4:
        raise ValueError("Only L <= 4 supported for exact enumeration")

    # Generate initial guesses from the 1D zeros (scaled)
    N = L * L
    init_guesses = fisher_zeros_1d_ising(N)
    # Also add guesses near the critical point
    beta_c = 0.5 * math.log(1 + math.sqrt(2))
    for phi in np.linspace(0, 2 * math.pi, 20):
        init_guesses.append(beta_c + 0.3 * cmath.exp(1j * phi))

    zeros = []
    eps = 1e-7
    for beta0 in init_guesses:
        beta = beta0
        for _ in range(50):
            try:
                Zb = ising_2d_exact_partition_small(L, beta)
                Zb_p = ising_2d_exact_partition_small(L, beta + eps)
                Zb_m = ising_2d_exact_partition_small(L, beta - eps)
                dZb = (Zb_p - Zb_m) / (2 * eps)
                if abs(dZb) < 1e-20:
                    break
                beta = beta - Zb / dZb
            except (OverflowError, ValueError):
                break
        try:
            Zcheck = ising_2d_exact_partition_small(L, beta)
            if abs(Zcheck) < 1e-4 * abs(ising_2d_exact_partition_small(L, beta_c)):
                is_new = True
                for z in zeros:
                    if abs(beta - z) < 1e-4:
                        is_new = False
                        break
                if is_new:
                    zeros.append(beta)
        except (OverflowError, ValueError):
            pass
    return zeros


# ============================================================================
# 6. YANG-BAXTER / BETHE ANSATZ PARTITION ZEROS
# ============================================================================

def bethe_transfer_eigenvalue(u: complex, bethe_roots: list[complex],
                              eta: complex, N: int) -> complex:
    """Transfer matrix eigenvalue for the XXX spin chain.

    T(u) = a(u) * prod_i f(u, u_i) + d(u) * prod_i g(u, u_i)

    For the XXX_{1/2} chain:
    a(u) = (u + eta/2)^N, d(u) = (u - eta/2)^N
    f(u, u_i) = (u - u_i - eta) / (u - u_i)
    g(u, u_i) = (u - u_i + eta) / (u - u_i)

    where eta is the crossing parameter (eta = i for standard XXX).
    """
    M = len(bethe_roots)
    a_u = (u + eta / 2) ** N
    d_u = (u - eta / 2) ** N

    prod_f = 1.0 + 0j
    prod_g = 1.0 + 0j
    for ui in bethe_roots:
        diff = u - ui
        if abs(diff) < 1e-15:
            return float('nan')
        prod_f *= (diff - eta) / diff
        prod_g *= (diff + eta) / diff

    return a_u * prod_f + d_u * prod_g


def bethe_equations(bethe_roots: list[complex], eta: complex, N: int) -> list[complex]:
    """Residual of the Bethe ansatz equations.

    For each Bethe root u_j:
    (u_j + eta/2)^N / (u_j - eta/2)^N = prod_{k != j} (u_j - u_k + eta) / (u_j - u_k - eta)

    Returns list of residuals (should all be zero for valid Bethe roots).
    """
    M = len(bethe_roots)
    residuals = []
    for j in range(M):
        uj = bethe_roots[j]
        lhs = ((uj + eta / 2) / (uj - eta / 2)) ** N

        rhs = 1.0 + 0j
        for k in range(M):
            if k != j:
                diff = uj - bethe_roots[k]
                rhs *= (diff + eta) / (diff - eta)

        residuals.append(lhs - rhs)
    return residuals


def solve_bethe_equations_free_fermion(N: int, M: int,
                                       eta: complex = 1j) -> list[complex]:
    """Solve Bethe equations for the XXX_{1/2} chain, free-fermion sector.

    For the case eta = i (standard XXX), the free-fermion Bethe roots
    for M magnons on N sites are:

    u_j = (eta/2) * cot(pi * I_j / N)

    where I_j are distinct half-integers (for even N) or integers (for odd N)
    from the allowed set.

    This gives the ground state and low-lying excitations.
    """
    roots = []
    # For the ground state with M magnons, the quantum numbers are
    # I_j = -(M-1)/2, -(M-3)/2, ..., (M-1)/2
    for j in range(M):
        I_j = -(M - 1) / 2 + j
        angle = math.pi * I_j / N
        if abs(math.sin(angle)) > 1e-15:
            root = (eta / 2) / math.tan(angle)
            roots.append(root)
    return roots


def transfer_zeros_at_zeta_zeros(N: int, M: int,
                                  zeta_zero_imaginary_parts: list[float],
                                  u_scan: Optional[np.ndarray] = None,
                                  ) -> dict[float, list[complex]]:
    """Compute transfer matrix zeros with eta = i*gamma_n (zeta zeros).

    For each imaginary part gamma_n of a nontrivial Riemann zeta zero,
    set eta = i * gamma_n and compute the Bethe roots, then find zeros
    of the transfer eigenvalue T(u).

    Parameters
    ----------
    N : int
        Chain length.
    M : int
        Number of magnons (Bethe roots).
    zeta_zero_imaginary_parts : list of float
        Imaginary parts of nontrivial zeta zeros (e.g., 14.134...).
    u_scan : ndarray, optional
        Points to scan for transfer eigenvalue zeros.

    Returns
    -------
    Dictionary mapping gamma_n to list of u-values where T(u) ~ 0.
    """
    if u_scan is None:
        u_scan = np.linspace(-5, 5, 500) + 0j

    results = {}
    for gamma in zeta_zero_imaginary_parts:
        eta = 1j * gamma
        # Get Bethe roots for this eta
        bethe_roots = solve_bethe_equations_free_fermion(N, M, eta)
        if not bethe_roots:
            results[gamma] = []
            continue
        # Scan for transfer eigenvalue zeros
        T_vals = [bethe_transfer_eigenvalue(u, bethe_roots, eta, N) for u in u_scan]
        # Find approximate zeros
        zero_candidates = []
        for i in range(len(T_vals) - 1):
            if not (cmath.isnan(T_vals[i]) or cmath.isnan(T_vals[i + 1])):
                if abs(T_vals[i]) < abs(T_vals[i + 1]):
                    if abs(T_vals[i]) < 1.0:
                        zero_candidates.append(u_scan[i])

        results[gamma] = zero_candidates
    return results


# ============================================================================
# 7. ZERO DENSITY
# ============================================================================

def theta_zero_density_estimate(lattice: str, r_inner: float, r_outer: float,
                                n_angular: int = 200,
                                n_terms: int = 200) -> float:
    """Estimate the density of theta function zeros in an annulus.

    Uses the argument principle: (1/2pi i) * integral_{|q|=r} f'(q)/f(q) dq
    counts zeros minus poles inside |q| = r.  Since theta functions are
    entire in q (for |q| < 1), this just counts zeros.

    Parameters
    ----------
    lattice : str
        Lattice type.
    r_inner, r_outer : float
        Inner and outer radii of the annulus (0 < r_inner < r_outer < 1).
    n_angular : int
        Number of angular integration points.

    Returns
    -------
    Estimated number of zeros in the annulus.
    """
    theta_funcs = {
        'A1': theta_A1,
        'A2': theta_A2,
        'D4': theta_D4,
        'E8': theta_E8,
    }
    f = theta_funcs[lattice]
    eps = 1e-8

    count = 0.0
    for r in [r_inner, r_outer]:
        # Integral of f'/f around |q| = r
        integral = 0.0 + 0j
        for k in range(n_angular):
            phi = 2 * math.pi * k / n_angular
            dphi = 2 * math.pi / n_angular
            q = r * cmath.exp(1j * phi)
            fq = f(q, n_terms)
            # Numerical derivative
            dq = eps * cmath.exp(1j * phi)
            fq_p = f(q + dq, n_terms)
            fq_m = f(q - dq, n_terms)
            dfq = (fq_p - fq_m) / (2 * dq)
            if abs(fq) > 1e-30:
                integral += (dfq / fq) * (1j * q) * dphi
        n_r = integral.real / (2 * math.pi)
        if r == r_outer:
            count += n_r
        else:
            count -= n_r
    return abs(count)


# ============================================================================
# 8. JULIA SET (RG flow)
# ============================================================================

def ising_rg_map(q: complex, b: int = 2) -> complex:
    """Renormalization group map for the 1D Ising model.

    Under a block-spin transformation with block size b, the partition
    function transforms as Z_{N/b}(q') = f(q) * Z_N(q) where
    q' = R_b(q) is the RG map.

    For the 1D Ising (transfer matrix), the RG map on the coupling
    K = beta*J is:

    For b=2: tanh(K') = tanh(K)^2  [Kadanoff decimation]

    In the variable x = tanh(K):
    x' = x^2

    In the variable q = exp(-4K):
    K = -log(q)/4, x = (1-q^{1/2})/(1+q^{1/2}) approximately.
    """
    # Using the variable x = tanh(K), the map is x -> x^b
    # Convert: K = -log(q)/4, x = tanh(K)
    if abs(q) < 1e-30:
        return 0.0 + 0j
    K = -cmath.log(q) / 4
    x = (cmath.exp(K) - cmath.exp(-K)) / (cmath.exp(K) + cmath.exp(-K))
    x_new = x ** b
    # Convert back: K' = arctanh(x'), q' = exp(-4K')
    if abs(1 - x_new) < 1e-15:
        return 0.0 + 0j
    K_new = 0.5 * cmath.log((1 + x_new) / (1 - x_new))
    return cmath.exp(-4 * K_new)


def julia_set_sample(rg_map, region_center: complex, region_radius: float,
                     n_points: int = 200, n_iter: int = 50,
                     escape_radius: float = 100.0) -> tuple[np.ndarray, np.ndarray]:
    """Sample the Julia set of the RG map by escape-time algorithm.

    Parameters
    ----------
    rg_map : callable
        The renormalization group map q -> q'.
    region_center : complex
        Center of the sampling region.
    region_radius : float
        Radius of the sampling region.
    n_points : int
        Number of points per axis (total n_points^2 samples).
    n_iter : int
        Maximum number of iterations.
    escape_radius : float
        Escape radius.

    Returns
    -------
    (grid, escape_times) : tuple
        grid[i,j] = complex point, escape_times[i,j] = iteration count.
    """
    x = np.linspace(region_center.real - region_radius,
                     region_center.real + region_radius, n_points)
    y = np.linspace(region_center.imag - region_radius,
                     region_center.imag + region_radius, n_points)
    grid = np.zeros((n_points, n_points), dtype=complex)
    escape_times = np.zeros((n_points, n_points), dtype=int)

    for i in range(n_points):
        for j in range(n_points):
            q = x[i] + 1j * y[j]
            grid[i, j] = q
            for it in range(n_iter):
                try:
                    q = rg_map(q)
                    if abs(q) > escape_radius or cmath.isnan(q) or cmath.isinf(q):
                        escape_times[i, j] = it
                        break
                except (OverflowError, ValueError, ZeroDivisionError):
                    escape_times[i, j] = it
                    break
            else:
                escape_times[i, j] = n_iter

    return grid, escape_times


# ============================================================================
# 9. MODULAR INVARIANCE CONSTRAINTS ON ZERO DISTRIBUTION
# ============================================================================

def modular_s_transform_q(q: complex) -> complex:
    """Under tau -> -1/tau (S-transform), map q to q_dual.

    q = e^{2pi i tau}, so q_dual = e^{-2pi i / tau}.
    We have tau = log(q) / (2pi i), so -1/tau = -2pi i / log(q).
    Then q_dual = e^{2pi i * (-2pi i / log(q))} = e^{4pi^2 / log(q)}.
    """
    if abs(q) < 1e-30:
        return 0.0 + 0j
    log_q = cmath.log(q)
    if abs(log_q) < 1e-30:
        return 0.0 + 0j
    return cmath.exp(4 * math.pi ** 2 / log_q)


def check_modular_invariance_theta(lattice: str, q: complex,
                                    n_terms: int = 200) -> float:
    """Check modular transformation of theta functions.

    For the E_8 lattice (self-dual, even, unimodular):
    Theta_{E_8}(-1/tau) = tau^4 * Theta_{E_8}(tau)
    (weight 4 modular form for SL(2,Z)).

    Returns the relative error |LHS - RHS| / |RHS|.
    """
    if lattice == 'E8':
        tau = cmath.log(q) / (2j * math.pi)
        tau_dual = -1 / tau
        q_dual = cmath.exp(2j * math.pi * tau_dual)
        if abs(q_dual) >= 0.999:
            return float('nan')
        lhs = theta_E8(q_dual, n_terms)
        rhs = tau ** 4 * theta_E8(q, n_terms)
        if abs(rhs) < 1e-30:
            return float('nan')
        return abs(lhs - rhs) / abs(rhs)
    raise NotImplementedError(f"Modular check not implemented for {lattice}")


# ============================================================================
# 10. VIRASORO SHADOW PARTITION ZEROS: c-dependence
# ============================================================================

def virasoro_shadow_zeros(c: float, g_max: int = 5,
                          n_terms: int = 20) -> np.ndarray:
    """Shadow partition zeros for Virasoro at central charge c.

    The modular characteristic is kappa(Vir_c) = c/2 (AP48: this is
    specific to Virasoro, not a general formula).

    Returns array of complex zeros of Z^{sh}(q).
    """
    kappa = c / 2.0
    return shadow_partition_zeros(kappa, g_max, n_terms)


def shadow_zero_modulus_distribution(c_values: list[float],
                                     g_max: int = 5,
                                     n_terms: int = 20
                                     ) -> dict[float, np.ndarray]:
    """For each central charge c, compute |zeros| of the shadow partition fn.

    Returns dict mapping c -> sorted array of |z| for each zero.
    """
    result = {}
    for c in c_values:
        zeros = virasoro_shadow_zeros(c, g_max, n_terms)
        moduli = np.sort(np.abs(zeros))
        result[c] = moduli
    return result


# ============================================================================
# 11. UNIT CIRCLE CONNECTION: partition zeros -> critical line
# ============================================================================

def map_q_to_tau(q: complex) -> complex:
    """Map q -> tau via q = e^{2pi i tau}, so tau = log(q) / (2pi i)."""
    if abs(q) < 1e-30:
        return float('nan') + 0j
    return cmath.log(q) / (2j * math.pi)


def unit_circle_approach_rate(lattice: str, r_values: np.ndarray,
                               n_angular: int = 100,
                               n_terms: int = 200) -> np.ndarray:
    """Compute the minimum |Theta_Lambda| on circles |q| = r approaching 1.

    As r -> 1^-, the minimum of |Theta(q)| on |q| = r should approach zero
    (at the zeros), and the rate of approach encodes information about the
    zero distribution near the unit circle.

    Returns array of min |Theta| values, one per r.
    """
    theta_funcs = {
        'A1': theta_A1,
        'A2': theta_A2,
        'D4': theta_D4,
        'E8': theta_E8,
    }
    f = theta_funcs[lattice]
    min_vals = np.zeros(len(r_values))

    for idx, r in enumerate(r_values):
        min_val = float('inf')
        for k in range(n_angular):
            phi = 2 * math.pi * k / n_angular
            q = r * cmath.exp(1j * phi)
            val = abs(f(q, n_terms))
            if val < min_val:
                min_val = val
        min_vals[idx] = min_val

    return min_vals
