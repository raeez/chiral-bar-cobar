"""
Connected Dirichlet-sewing lift S_A(u) and prime-side Li coefficients.

The connected genus-one sewing free energy F^conn_A(q) = -log det(1 - K_q(A))
has Dirichlet lift S_A(u) = sum_{N>=1} a_A(N) N^{-u}.

For bosonic weight multiset W(A) = {w_i}:
  S_A(u) = zeta(u+1) * sum_i (zeta(u) - H_{w_i - 1}(u))

where H_n(u) = sum_{j=1}^n j^{-u}.

Prime-side Li coefficients: regularize via Xi_A(u) = (u-1)*S_A(u),
  lambda_n(A) = (1/(n-1)!) d^n/du^n [u^{n-1} log Xi_A(u)] |_{u=1}

Key families:
  Heisenberg: W = {1}, S_H(u) = zeta(u)*zeta(u+1)
  Virasoro:   W = {2}, S_Vir(u) = zeta(u+1)*(zeta(u) - 1)
  W_N:        W = {2,...,N}, S_{W_N}(u) = zeta(u+1)*((N-1)*zeta(u) - sum_{j=1}^{N-1} H_j(u))
"""

import numpy as np
from mpmath import (mp, mpf, zeta, euler as euler_gamma, diff, log, gamma as mpgamma,
                    pi, power, fac, stieltjes, inf, nsum, exp, polylog)

mp.dps = 50  # high precision

# =============================================================================
# Core arithmetic functions
# =============================================================================

def harmonic_zeta(n, u):
    """H_n(u) = sum_{j=1}^n j^{-u}"""
    if n <= 0:
        return mpf(0)
    return sum(power(j, -u) for j in range(1, n + 1))


def S_heisenberg(u):
    """S_H(u) = zeta(u)*zeta(u+1)"""
    return zeta(u) * zeta(u + 1)


def S_virasoro(u):
    """S_Vir(u) = zeta(u+1)*(zeta(u) - 1)"""
    return zeta(u + 1) * (zeta(u) - 1)


def S_WN(N, u):
    """S_{W_N}(u) = zeta(u+1) * ((N-1)*zeta(u) - sum_{j=1}^{N-1} H_j(u))"""
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * zeta(u) - harm_sum)


def S_generic(weights, u):
    """S_A(u) for arbitrary weight multiset W(A) = {w_i}"""
    return zeta(u + 1) * sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)


# =============================================================================
# Xi regularization: Xi_A(u) = (u-1)*S_A(u)
# =============================================================================

def _zeta_reg(u):
    """(u-1)*zeta(u), regularized at u=1. Analytic continuation via Laurent."""
    eps = u - 1
    if abs(eps) < mpf('1e-20'):
        # Laurent: (u-1)*zeta(u) = 1 + gamma*(u-1) + gamma_1*(u-1)^2 + ...
        # where gamma_n are Stieltjes constants
        return (1 + euler_gamma * eps + stieltjes(1) * eps**2
                + stieltjes(2) * eps**3 + stieltjes(3) * eps**4)
    return (u - 1) * zeta(u)


def Xi_heisenberg(u):
    """Xi_H(u) = (u-1)*zeta(u) * zeta(u+1)"""
    return _zeta_reg(u) * zeta(u + 1)


def Xi_virasoro(u):
    """Xi_Vir(u) = (u-1) * zeta(u+1) * (zeta(u) - 1)"""
    return zeta(u + 1) * (_zeta_reg(u) - (u - 1))


def Xi_WN(N, u):
    """Xi_{W_N}(u) = (u-1)*S_{W_N}(u)"""
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * _zeta_reg(u) - (u - 1) * harm_sum)


def Xi_generic(weights, u):
    return zeta(u + 1) * sum(_zeta_reg(u) - (u - 1) * harmonic_zeta(w - 1, u) for w in weights)


# =============================================================================
# Prime-side Li coefficients via numerical differentiation
# =============================================================================

def li_coefficients(Xi_func, n_max=20, **kwargs):
    """
    Compute lambda_n(A) = (1/(n-1)!) d^n/du^n [u^{n-1} log Xi_A(u)] |_{u=1}
    for n = 1, ..., n_max.

    Uses mpmath numerical differentiation at high precision.
    """
    results = []
    for n in range(1, n_max + 1):
        def f(u):
            return power(u, n - 1) * log(Xi_func(u, **kwargs))

        # n-th derivative at u=1
        d_n = diff(f, mpf(1), n)
        lam_n = d_n / fac(n - 1)
        results.append(lam_n)
    return results


def li_heisenberg(n_max=20):
    return li_coefficients(lambda u: Xi_heisenberg(u), n_max)


def li_virasoro(n_max=20):
    return li_coefficients(lambda u: Xi_virasoro(u), n_max)


def li_WN(N, n_max=20):
    return li_coefficients(lambda u: Xi_WN(N, u), n_max)


# =============================================================================
# Analytic verification of lambda_1 formulas
# =============================================================================

def lambda1_heisenberg_analytic():
    """lambda_1(H) = gamma + zeta'(2)/zeta(2)"""
    zp2 = diff(zeta, mpf(2))
    z2 = zeta(2)
    return euler_gamma + zp2 / z2


def lambda1_WN_analytic(N):
    """lambda_1(W_N) = zeta'(2)/zeta(2) + gamma + 1 - N/(N-1) * H_{N-1}"""
    zp2 = diff(zeta, mpf(2))
    z2 = zeta(2)
    H = sum(mpf(1) / j for j in range(1, N))
    return zp2 / z2 + euler_gamma + 1 - mpf(N) / (N - 1) * H


def lambda1_asymptotics(N):
    """lambda_1(W_N) ~ -log(N) - 0.147... as N -> infty"""
    return -log(N) - mpf('0.147')


# =============================================================================
# Fourier coefficients a_A(N) of connected free energy
# =============================================================================

def divisor_sigma_minus1(N):
    """sigma_{-1}(N) = sum_{d|N} 1/d"""
    return sum(mpf(1) / d for d in range(1, N + 1) if N % d == 0)


def connected_coefficients_heisenberg(N_max):
    """a_H(N) = sigma_{-1}(N)"""
    return [divisor_sigma_minus1(N) for N in range(1, N_max + 1)]


def connected_coefficients_generic(weights, N_max):
    """
    a_A(N) = sum_i sum_{m >= w_i, m|N} 1/(N/m)

    For F^conn = sum_i sum_{m>=w_i} sum_{r>=1} q^{mr}/r,
    a_A(N) = sum_i sum_{m>=w_i, m|N} 1/(N/m)
           = sum_{d|N} (1/d) * #{i : w_i <= N/d}
    """
    coeffs = []
    for N in range(1, N_max + 1):
        a_N = mpf(0)
        for d in range(1, N + 1):
            if N % d == 0:
                m = N // d  # so q^{m*d} contributes 1/d
                count = sum(1 for w in weights if w <= m)
                a_N += mpf(count) / d
        coeffs.append(a_N)
    return coeffs


# =============================================================================
# Euler product defect analysis
# =============================================================================

def euler_defect_WN(N, u):
    """
    S_{W_N}(u) = (N-1)*zeta(u)*zeta(u+1) - zeta(u+1)*sum_{j=1}^{N-1} H_j(u)

    The "Euler-pure" part is (N-1)*zeta(u)*zeta(u+1).
    The defect is zeta(u+1)*sum_{j=1}^{N-1} H_j(u) -- finite harmonic correction.
    """
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    pure = (N - 1) * zeta(u) * zeta(u + 1)
    defect = zeta(u + 1) * harm_sum
    return pure, defect, pure - defect


# =============================================================================
# Moment matrix: truncated Hankel matrix from shadow data
# =============================================================================

def moment_matrix(moments, size):
    """
    Build size x size Hankel matrix from moment sequence.
    M_{ij} = moments[i+j] for 0-indexed i,j.
    """
    M = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i + j < len(moments):
                M[i, j] = float(moments[i + j])
    return M


def moment_determinants(moments, max_size=5):
    """Leading principal minors of the Hankel moment matrix."""
    dets = []
    for k in range(1, max_size + 1):
        M = moment_matrix(moments, k)
        dets.append(np.linalg.det(M))
    return dets


# =============================================================================
# Two-variable L-object: mixed (s,u) transform
# =============================================================================

def L_mixed_heisenberg(s, u, y_max=10.0, n_pts=10000):
    """
    Numerical approximation of the mixed transform for Heisenberg.
    L_H(s,u) ~ integral_0^infty F^conn_H(e^{-2pi*y}) * E*(iy, s) * y^{u-2} dy

    Using E*(tau, s) ~ y^s + phi(s)*y^{1-s} for tau = iy (completed Eisenstein).
    This is a conceptual placeholder; the true modular integral requires
    the full Θ_A insertion.
    """
    # For now: just compute the factored form
    # L_H(s,u) factors as zeta(u)*zeta(u+1) on the u-side
    # and involves Eisenstein on the s-side
    # The mixed object is morally the Rankin-Selberg of F^conn against E*
    pass


# =============================================================================
# Summary / display
# =============================================================================

def print_li_table(n_max=20):
    """Print Li coefficient table for all test families."""
    print("=" * 90)
    print(f"{'n':>3} | {'Heisenberg':>18} | {'Virasoro':>18} | {'W_3':>18} | {'W_4':>18}")
    print("-" * 90)

    lH = li_heisenberg(n_max)
    lV = li_virasoro(n_max)
    l3 = li_WN(3, n_max)
    l4 = li_WN(4, n_max)

    for n in range(n_max):
        print(f"{n+1:>3} | {float(lH[n]):>18.10f} | {float(lV[n]):>18.10f} | "
              f"{float(l3[n]):>18.10f} | {float(l4[n]):>18.10f}")

    return lH, lV, l3, l4


def print_lambda1_formula_check():
    """Verify analytic lambda_1 formulas against numerical computation."""
    print("\n=== Lambda_1 analytic vs numerical ===")

    # Heisenberg
    l1_H_num = li_heisenberg(1)[0]
    l1_H_ana = lambda1_heisenberg_analytic()
    print(f"Heisenberg: numerical = {float(l1_H_num):.15f}")
    print(f"            analytic  = {float(l1_H_ana):.15f}")
    print(f"            diff      = {float(abs(l1_H_num - l1_H_ana)):.2e}")

    # W_N for N=2,3,4
    for N in [2, 3, 4, 5, 10, 20]:
        l1_num = li_WN(N, 1)[0]
        l1_ana = lambda1_WN_analytic(N)
        print(f"W_{N:>2}: numerical = {float(l1_num):>18.15f}, analytic = {float(l1_ana):>18.15f}, "
              f"diff = {float(abs(l1_num - l1_ana)):.2e}")


def print_asymptotic_check():
    """Check lambda_1(W_N) ~ -log(N) - 0.147... for large N."""
    print("\n=== Lambda_1 asymptotics: lambda_1(W_N) + log(N) ===")
    for N in [2, 3, 5, 10, 20, 50, 100]:
        l1 = lambda1_WN_analytic(N)
        offset = l1 + log(N)
        print(f"N = {N:>3}: lambda_1 = {float(l1):>12.8f}, lambda_1 + log(N) = {float(offset):>12.8f}")


if __name__ == "__main__":
    print_lambda1_formula_check()
    print_asymptotic_check()
    print("\n")
    print_li_table(n_max=10)
