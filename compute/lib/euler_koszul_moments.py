"""
Euler-Koszul moment matrix and quartic resonance connection.

The connected sewing free energy F^conn_A(q) has q-expansion coefficients a_A(N).
The shadow obstruction tower (kappa, cubic, quartic, ...) produces moment constraints
on the spectral measure of the sewing operator.

The central conjecture: the 3x3 leading principal minor of the truncated
surface-Hankel moment matrix equals the modular quartic resonance class R_4^mod(A).

This module computes:
1. Moment sequences from sewing coefficients
2. Hankel determinants
3. Comparison with known quartic shadow values
4. The Euler-Koszul defect for W_N families
"""

import numpy as np
from mpmath import (mp, mpf, zeta, diff, log, euler as euler_gamma,
                    pi, power, fac, matrix as mpmatrix, det as mpdet)

mp.dps = 40


# =============================================================================
# Sewing coefficients a_A(N) for standard families
# =============================================================================

def divisor_sigma(N, s):
    """sigma_s(N) = sum_{d|N} d^s"""
    return sum(power(d, s) for d in range(1, N + 1) if N % d == 0)


def sewing_coeffs_heisenberg(N_max):
    """a_H(N) = sigma_{-1}(N)"""
    return [divisor_sigma(N, -1) for N in range(1, N_max + 1)]


def sewing_coeffs_WN(N_rank, N_max):
    """a_{W_N}(n) for weight multiset {2, 3, ..., N_rank}"""
    coeffs = []
    for n in range(1, N_max + 1):
        a_n = mpf(0)
        for d in range(1, n + 1):
            if n % d == 0:
                m = n // d
                # count weights w_i <= m: weights are {2,...,N_rank}, so count = max(0, m-1) capped at N_rank-1
                count = max(0, min(m - 1, N_rank - 1))
                a_n += mpf(count) / d
        coeffs.append(a_n)
    return coeffs


def sewing_coeffs_generic(weights, N_max):
    """a_A(n) for arbitrary weight multiset"""
    coeffs = []
    for n in range(1, N_max + 1):
        a_n = mpf(0)
        for d in range(1, n + 1):
            if n % d == 0:
                m = n // d
                count = sum(1 for w in weights if w <= m)
                a_n += mpf(count) / d
        coeffs.append(a_n)
    return coeffs


# =============================================================================
# Hankel moment matrix from sewing coefficients
# =============================================================================

def hankel_matrix(coeffs, size):
    """
    Build size x size Hankel matrix M_{ij} = coeffs[i+j].
    coeffs[0] = a_A(1), coeffs[1] = a_A(2), etc.
    """
    M = mpmatrix(size, size)
    for i in range(size):
        for j in range(size):
            idx = i + j
            if idx < len(coeffs):
                M[i, j] = coeffs[idx]
            else:
                M[i, j] = mpf(0)
    return M


def hankel_minors(coeffs, max_size=6):
    """Leading principal minors det(H_k) for k=1,...,max_size."""
    minors = []
    for k in range(1, max_size + 1):
        H = hankel_matrix(coeffs, k)
        minors.append(mpdet(H))
    return minors


# =============================================================================
# Shadow data for comparison
# =============================================================================

def kappa_heisenberg(k=1):
    return mpf(k)

def kappa_virasoro(c):
    return c / 2

def kappa_WN(c, N):
    """kappa(W_N) = c * (H_N - 1) where H_N = 1 + 1/2 + ... + 1/N.

    AP1: kappa(W_3) = 5c/6, NOT c/2 or 3c/2.
    The sum is over 1/s for s = 2, ..., N (i.e., H_N - 1).
    """
    rho = sum(mpf(1) / s for s in range(2, N + 1))
    return c * rho

def Q_contact_virasoro(c):
    """Q^contact_Vir = 10 / [c(5c + 22)]"""
    return mpf(10) / (c * (5 * c + 22))


# =============================================================================
# Euler-Koszul defect structure
# =============================================================================

def euler_defect_coefficients(N_rank, N_max):
    """
    Decompose a_{W_N}(n) = (N_rank-1)*sigma_{-1}(n) - delta(n)
    where delta(n) is the finite harmonic defect.
    """
    a_full = sewing_coeffs_WN(N_rank, N_max)
    a_heis = sewing_coeffs_heisenberg(N_max)
    defect = []
    for i in range(N_max):
        defect.append((N_rank - 1) * a_heis[i] - a_full[i])
    return defect


def euler_defect_support(N_rank, N_max):
    """
    The defect delta(n) has finite support in the sense that only
    modes with m < N_rank contribute to the difference.
    Find effective support.
    """
    defect = euler_defect_coefficients(N_rank, N_max)
    support = [(i + 1, float(d)) for i, d in enumerate(defect) if abs(d) > 1e-20]
    return support


# =============================================================================
# Surface moment determinant vs quartic shadow
# =============================================================================

def moment_ratio_analysis(family_name, coeffs, kappa_val, Q_val=None):
    """
    Analyze the moment structure:
    - det(H_1) = a(1) should relate to kappa
    - det(H_2) / det(H_1) should relate to spectral discriminant
    - det(H_3) / det(H_2) should relate to quartic resonance class
    """
    minors = hankel_minors(coeffs, 6)

    print(f"\n=== {family_name} ===")
    print(f"  kappa = {float(kappa_val):.10f}")
    if Q_val is not None:
        print(f"  Q^contact = {float(Q_val):.10f}")

    for k in range(len(minors)):
        print(f"  det(H_{k+1}) = {float(minors[k]):>20.10f}")

    # Ratios
    print("  Ratios:")
    for k in range(1, len(minors)):
        if abs(minors[k - 1]) > 1e-30:
            ratio = minors[k] / minors[k - 1]
            print(f"    det(H_{k+1})/det(H_{k}) = {float(ratio):>20.10f}")

    # Normalized by kappa
    if abs(kappa_val) > 1e-30:
        print(f"  det(H_1)/kappa = {float(minors[0] / kappa_val):>20.10f}")
        if len(minors) >= 3 and abs(minors[1]) > 1e-30:
            # Is det(H_3)/(det(H_2)*kappa) related to Q^contact?
            ratio3 = minors[2] / (minors[1] * kappa_val)
            print(f"  det(H_3)/(det(H_2)*kappa) = {float(ratio3):>20.10f}")

    return minors


# =============================================================================
# Main analysis
# =============================================================================

def run_full_analysis():
    N_max = 50

    # Heisenberg
    a_H = sewing_coeffs_heisenberg(N_max)
    moment_ratio_analysis("Heisenberg (k=1)", a_H, kappa_heisenberg(1))

    # Virasoro (generic c, use c=26 as test)
    a_V = sewing_coeffs_WN(2, N_max)
    moment_ratio_analysis("Virasoro (generic)", a_V, kappa_virasoro(1), Q_contact_virasoro(1))

    # W_3
    a_W3 = sewing_coeffs_WN(3, N_max)
    moment_ratio_analysis("W_3 (generic)", a_W3, kappa_WN(1, 3))

    # W_4
    a_W4 = sewing_coeffs_WN(4, N_max)
    moment_ratio_analysis("W_4 (generic)", a_W4, kappa_WN(1, 4))

    # Euler defect analysis
    print("\n=== Euler Defect Support ===")
    for N in [2, 3, 4, 5]:
        support = euler_defect_support(N, 30)
        print(f"  W_{N}: nonzero defect at n = {[s[0] for s in support[:10]]}")

    # Key question: is defect finite-rank?
    print("\n=== Defect rank (number of nonzero terms in first 30) ===")
    for N in [2, 3, 4, 5, 10]:
        support = euler_defect_support(N, 30)
        print(f"  W_{N}: {len(support)} nonzero terms")


if __name__ == "__main__":
    run_full_analysis()
