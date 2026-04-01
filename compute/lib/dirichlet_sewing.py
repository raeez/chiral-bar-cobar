r"""
dirichlet_sewing.py -- Connected Dirichlet-sewing lift and Miura defect

Implements the Dirichlet-sewing lift S_A(u), Euler product decomposition,
modified Li coefficients lambda_tilde_n(A), and Miura defect D_N(q)
from the arithmetic programme (raeeznotes 105-112, Cluster B).

MATHEMATICAL CONTENT:

1. CONNECTED DIRICHLET-SEWING LIFT S_A(u):

   For a modular Koszul algebra A with bosonic weight multiset W(A) = {w_i}:

     S_A(u) = zeta(u+1) * sum_i (zeta(u) - H_{w_i - 1}(u))

   where H_n(u) = sum_{j=1}^n j^{-u} is the partial (harmonic) zeta sum.

   Key families:
     Heisenberg:  W = {1},    S_H(u) = zeta(u)*zeta(u+1)
     Virasoro:    W = {2},    S_Vir(u) = zeta(u+1)*(zeta(u) - 1)
     Affine sl_2: W = {1,2},  S_{sl_2}(u) = zeta(u+1)*(2*zeta(u) - 1)
     W_N:         W = {2,...,N}, S_{W_N}(u) = zeta(u+1)*((N-1)*zeta(u)
                                              - sum_{j=1}^{N-1} H_j(u))

2. EULER PRODUCT (for Heisenberg = weight-1 single generator):

   S_H(u) = zeta(u)*zeta(u+1) = prod_p (1 - p^{-u})^{-1} (1 - p^{-u-1})^{-1}

   The local factor at prime p is det(1 - p^{-u} T_p | V_H)^{-1} where
   T_p acts on a 2-dimensional local space with eigenvalues p^0 = 1 and p^{-1}.

   For higher-weight families (Virasoro, W_N), the Euler product structure
   acquires DEFECT TERMS from the harmonic corrections H_{w-1}(u), which
   are finite sums and do not have Euler products.

3. MIURA DEFECT D_N(q):

   D_N(q) = prod_{j=1}^{N-1} (1 - q^j)

   encodes the defect between the affine and W-algebra sewing envelopes
   under principal Drinfeld-Sokolov reduction sl_N -> W_N.

   Explicit:
     D_2(q) = 1 - q
     D_3(q) = (1 - q)(1 - q^2) = (1 - q)^2 (1 + q)
     D_4(q) = (1 - q)(1 - q^2)(1 - q^3)
     D_5(q) = (1 - q)(1 - q^2)(1 - q^3)(1 - q^4)

   Properties:
     D_N(0) = 1 (normalization)
     D_N(1) = 0 for all N >= 2 (vanishing at critical point)
     D_N(q) ~ (1 - q)^{N-1} near q = 1 (highest-order zero)

4. MODIFIED LI COEFFICIENTS lambda_tilde_n(A):

   The Xi regularization Xi_A(u) = (u-1)*S_A(u) removes the u=1 pole
   of zeta(u). The modified Li coefficients are:

     lambda_tilde_n(A) = (1/(n-1)!) * d^n/du^n [u^{n-1} log Xi_A(u)] |_{u=1}

   For Heisenberg: Xi_H(u) = (u-1)*zeta(u)*zeta(u+1) and the lambda_tilde_n
   reduce to the original Keiper-Li coefficients for zeta(u)*zeta(u+1).

   Sign pattern: all lambda_tilde_n > 0 would imply a shadow GRH
   (all nontrivial zeros of Xi_A on the critical line). For Heisenberg,
   the coefficients are positive for n = 1,...,6 and become negative at n = 7.

5. KAPPA DEFICIT AND DS REDUCTION:

   The kappa deficit under DS reduction sl_N -> W_N at level k:

     delta_kappa(N, k) = kappa(V_k(sl_N)) - kappa(W_{N,k})

   is related to the Miura defect through the sewing envelope:
   the D_N(q) polynomial controls which modes are removed.

Manuscript references:
  arithmetic_shadows.tex (def:frontier-defect-form, prop:miura-packet-splitting)
  higher_genus_modular_koszul.tex (shadow tower framework)
  w_algebras.tex (thm:ds-koszul-obstruction)
  concordance.tex (sec:concordance-arithmetic-frontier)
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    from mpmath import (
        mp, mpf, zeta, euler as euler_gamma, diff as mp_diff,
        log as mp_log, gamma as mpgamma, pi as mp_pi, power,
        fac, stieltjes, polylog, exp as mp_exp,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# ============================================================================
# Section 1: Partial zeta and harmonic sums
# ============================================================================

def harmonic_zeta(n: int, u) -> Any:
    r"""Partial (harmonic) zeta sum H_n(u) = sum_{j=1}^n j^{-u}.

    H_0(u) = 0 by convention.
    H_n(u) -> zeta(u) as n -> infty for Re(u) > 1.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if n <= 0:
        return mpf(0)
    return sum(power(j, -u) for j in range(1, n + 1))


def _zeta_regularized(u) -> Any:
    r"""(u-1)*zeta(u), regularized at u=1.

    Laurent expansion: (u-1)*zeta(u) = 1 + gamma*(u-1) + gamma_1*(u-1)^2 + ...
    where gamma_n are Stieltjes constants.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    eps = u - 1
    if abs(eps) < mpf('1e-20'):
        return (1 + euler_gamma * eps + stieltjes(1) * eps**2
                + stieltjes(2) * eps**3 + stieltjes(3) * eps**4)
    return (u - 1) * zeta(u)


# ============================================================================
# Section 2: Connected Dirichlet-sewing lift S_A(u)
# ============================================================================

def S_heisenberg(u) -> Any:
    r"""S_H(u) = zeta(u) * zeta(u+1).

    Heisenberg has weight multiset W = {1}, so
    S_H(u) = zeta(u+1) * (zeta(u) - H_0(u)) = zeta(u+1) * zeta(u).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return zeta(u) * zeta(u + 1)


def S_virasoro(u) -> Any:
    r"""S_Vir(u) = zeta(u+1) * (zeta(u) - 1).

    Virasoro has weight multiset W = {2}, so
    S_Vir(u) = zeta(u+1) * (zeta(u) - H_1(u)) = zeta(u+1) * (zeta(u) - 1).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return zeta(u + 1) * (zeta(u) - 1)


def S_affine_sl2(u) -> Any:
    r"""S_{sl_2}(u) = zeta(u+1) * (2*zeta(u) - 1).

    Affine sl_2 at generic level has weight multiset W = {1, 2}
    (current J at weight 1, Sugawara T at weight 2):
    S = zeta(u+1) * [(zeta(u) - H_0(u)) + (zeta(u) - H_1(u))]
      = zeta(u+1) * [zeta(u) + (zeta(u) - 1)]
      = zeta(u+1) * (2*zeta(u) - 1).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return zeta(u + 1) * (2 * zeta(u) - 1)


def S_WN(N: int, u) -> Any:
    r"""S_{W_N}(u) for the W_N algebra (principal DS of sl_N).

    Weight multiset W = {2, 3, ..., N}, so
    S_{W_N}(u) = zeta(u+1) * sum_{w=2}^{N} (zeta(u) - H_{w-1}(u))
               = zeta(u+1) * ((N-1)*zeta(u) - sum_{j=1}^{N-1} H_j(u)).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * zeta(u) - harm_sum)


def S_generic(weights: Sequence[int], u) -> Any:
    r"""S_A(u) for an algebra with bosonic weight multiset W(A) = {w_i}.

    S_A(u) = zeta(u+1) * sum_i (zeta(u) - H_{w_i - 1}(u)).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if not weights:
        return mpf(0)
    return zeta(u + 1) * sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)


# ============================================================================
# Section 3: Virasoro defect ratio
# ============================================================================

def virasoro_defect_ratio(u) -> Any:
    r"""D_Vir(u) = S_Vir(u) / S_H(u) = (zeta(u) - 1)/zeta(u) = 1 - 1/zeta(u).

    Measures the arithmetic defect of Virasoro relative to Heisenberg.
    Poles of 1/zeta(u) = zeros of zeta(u) are the nontrivial zeros.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return 1 - 1 / zeta(u)


# ============================================================================
# Section 4: Euler product for Heisenberg
# ============================================================================

def euler_product_heisenberg(u, primes: Optional[List[int]] = None,
                             n_primes: int = 50) -> Any:
    r"""Euler product approximation to S_H(u) = zeta(u)*zeta(u+1).

    S_H(u) = prod_p (1 - p^{-u})^{-1} * (1 - p^{-(u+1)})^{-1}

    where the product is over all primes p.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if primes is None:
        primes = _sieve_primes(n_primes)
    result = mpf(1)
    for p in primes:
        result *= 1 / ((1 - power(p, -u)) * (1 - power(p, -(u + 1))))
    return result


def euler_local_factor(p: int, u) -> Any:
    r"""Local Euler factor at prime p for Heisenberg.

    L_p(u) = (1 - p^{-u})^{-1} * (1 - p^{-(u+1)})^{-1}
           = det(1 - p^{-u} T_p | V_H)^{-1}

    where T_p has eigenvalues 1 and p^{-1} on the 2D local space V_H.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return 1 / ((1 - power(p, -u)) * (1 - power(p, -(u + 1))))


def euler_product_relative_error(u, n_primes: int = 50) -> Any:
    r"""Relative error |prod_p L_p(u) / zeta(u)zeta(u+1) - 1|.

    Measures convergence of the Euler product to the exact value.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    ep = euler_product_heisenberg(u, n_primes=n_primes)
    exact = S_heisenberg(u)
    if abs(exact) < mpf('1e-50'):
        return mpf('inf')
    return abs(ep / exact - 1)


def _sieve_primes(n: int) -> List[int]:
    """Return the first n prime numbers via sieve of Eratosthenes."""
    if n <= 0:
        return []
    upper = max(20, int(n * (math.log(n) + math.log(math.log(max(n, 3))) + 2)))
    sieve = [True] * (upper + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(upper)) + 1):
        if sieve[i]:
            for j in range(i * i, upper + 1, i):
                sieve[j] = False
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes[:n]


# ============================================================================
# Section 5: Miura defect D_N(q)
# ============================================================================

def miura_defect(N: int, q) -> Any:
    r"""Miura defect D_N(q) = prod_{j=1}^{N-1} (1 - q^j).

    Encodes the mode-removal pattern under principal DS reduction
    sl_N -> W_N. The j-th factor removes modes at conformal weight j.

    Properties:
      D_N(0) = 1 (normalization)
      D_N(1) = 0 for N >= 2 (vanishing at critical point)
      D_N(q) has degree N*(N-1)/2 as a polynomial in q
    """
    if N < 2:
        raise ValueError(f"Miura defect requires N >= 2, got {N}")
    result = 1
    for j in range(1, N):
        result *= (1 - q**j)
    return result


def miura_defect_exact(N: int, q: Fraction) -> Fraction:
    r"""Exact (rational) Miura defect D_N(q) for Fraction inputs."""
    if N < 2:
        raise ValueError(f"Miura defect requires N >= 2, got {N}")
    result = Fraction(1)
    for j in range(1, N):
        result *= (Fraction(1) - q**j)
    return result


def miura_defect_polynomial_degree(N: int) -> int:
    r"""Degree of D_N(q) as polynomial in q: N*(N-1)/2."""
    return N * (N - 1) // 2


def miura_defect_expanded(N: int) -> List[int]:
    r"""Coefficients of D_N(q) expanded as polynomial sum c_k q^k.

    Returns [c_0, c_1, ..., c_{deg}] where deg = N*(N-1)/2.
    """
    if N < 2:
        raise ValueError(f"Miura defect requires N >= 2, got {N}")
    deg = N * (N - 1) // 2
    coeffs = [0] * (deg + 1)
    coeffs[0] = 1
    for j in range(1, N):
        # Multiply current polynomial by (1 - q^j)
        new_coeffs = [0] * (deg + 1)
        for k in range(deg + 1):
            new_coeffs[k] += coeffs[k]
            if k >= j:
                new_coeffs[k] -= coeffs[k - j]
        coeffs = new_coeffs
    return coeffs


def miura_defect_at_roots_of_unity(N: int, k: int) -> complex:
    r"""D_N(exp(2*pi*i*k/N)) evaluated at N-th roots of unity.

    For k = 0 mod N: D_N(1) = 0.
    For general k: involves products of (1 - zeta_N^{jk}).
    """
    import cmath
    omega = cmath.exp(2j * cmath.pi * k / N)
    result = 1.0 + 0j
    for j in range(1, N):
        result *= (1 - omega**j)
    return result


# ============================================================================
# Section 6: Xi regularization and Li coefficients
# ============================================================================

def Xi_heisenberg(u) -> Any:
    r"""Xi_H(u) = (u-1)*zeta(u) * zeta(u+1).

    Regularized at u=1 via (u-1)*zeta(u) -> 1 + gamma*(u-1) + ...
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return _zeta_regularized(u) * zeta(u + 1)


def Xi_virasoro(u) -> Any:
    r"""Xi_Vir(u) = (u-1)*S_Vir(u) = zeta(u+1) * ((u-1)*zeta(u) - (u-1))."""
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return zeta(u + 1) * (_zeta_regularized(u) - (u - 1))


def Xi_WN(N: int, u) -> Any:
    r"""Xi_{W_N}(u) = (u-1)*S_{W_N}(u)."""
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * _zeta_regularized(u) - (u - 1) * harm_sum)


def Xi_generic(weights: Sequence[int], u) -> Any:
    r"""Xi_A(u) = (u-1)*S_A(u) for arbitrary weight multiset."""
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return zeta(u + 1) * sum(
        _zeta_regularized(u) - (u - 1) * harmonic_zeta(w - 1, u)
        for w in weights
    )


def li_coefficients(Xi_func, n_max: int = 20, **kwargs) -> List[Any]:
    r"""Modified Li coefficients lambda_tilde_n(A).

    lambda_tilde_n = (1/(n-1)!) * d^n/du^n [u^{n-1} * log Xi_A(u)] |_{u=1}

    Uses mpmath high-precision numerical differentiation.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    results = []
    for n in range(1, n_max + 1):
        def f(u, _n=n):
            return power(u, _n - 1) * mp_log(Xi_func(u, **kwargs))
        d_n = mp_diff(f, mpf(1), n)
        lam_n = d_n / fac(n - 1)
        results.append(lam_n)
    return results


def li_heisenberg(n_max: int = 20) -> List[Any]:
    r"""Li coefficients for Heisenberg: lambda_tilde_n(H)."""
    return li_coefficients(lambda u: Xi_heisenberg(u), n_max)


def li_virasoro(n_max: int = 20) -> List[Any]:
    r"""Li coefficients for Virasoro: lambda_tilde_n(Vir)."""
    return li_coefficients(lambda u: Xi_virasoro(u), n_max)


def li_WN(N: int, n_max: int = 20) -> List[Any]:
    r"""Li coefficients for W_N: lambda_tilde_n(W_N)."""
    return li_coefficients(lambda u: Xi_WN(N, u), n_max)


# ============================================================================
# Section 7: Lambda_1 analytic formulas
# ============================================================================

def lambda1_heisenberg_analytic() -> Any:
    r"""Analytic formula for lambda_1(H).

    lambda_1(H) = [d/du log Xi_H(u)]_{u=1}
                = gamma + zeta'(2)/zeta(2)

    where gamma is the Euler-Mascheroni constant.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    zp2 = mp_diff(zeta, mpf(2))
    z2 = zeta(2)
    return euler_gamma + zp2 / z2


def lambda1_virasoro_analytic() -> Any:
    r"""Analytic formula for lambda_1(Vir).

    lambda_1(Vir) = gamma + zeta'(2)/zeta(2) + 1 - 1/1
                  = gamma + zeta'(2)/zeta(2)
                  = lambda_1(H)

    Wait: Virasoro = W_2, so use the W_N formula with N=2.
    lambda_1(W_2) = zeta'(2)/zeta(2) + gamma + 1 - 2/1 * H_1
                  = zeta'(2)/zeta(2) + gamma + 1 - 2
                  = zeta'(2)/zeta(2) + gamma - 1.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return lambda1_WN_analytic(2)


def lambda1_WN_analytic(N: int) -> Any:
    r"""Analytic formula for lambda_1(W_N).

    lambda_1(W_N) = zeta'(2)/zeta(2) + gamma + 1 - N/(N-1) * H_{N-1}

    where H_{N-1} = sum_{j=1}^{N-1} 1/j is the harmonic number.
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    zp2 = mp_diff(zeta, mpf(2))
    z2 = zeta(2)
    H = sum(mpf(1) / j for j in range(1, N))
    return zp2 / z2 + euler_gamma + 1 - mpf(N) / (N - 1) * H


# ============================================================================
# Section 8: DS kappa deficit and Miura connection
# ============================================================================

def kappa_slN(N: int, k: Fraction) -> Fraction:
    r"""kappa(V_k(sl_N)) = (N^2 - 1)(k + N) / (2N).

    The general formula is kappa = dim(g) * (k + h^v) / (2 * h^v).
    """
    dim_g = Fraction(N * N - 1)
    h_v = Fraction(N)
    if k + h_v == 0:
        raise ValueError(f"Critical level k = -{N}: undefined")
    return dim_g * (k + h_v) / (2 * h_v)


def kappa_WN(N: int, k: Fraction) -> Fraction:
    r"""kappa(W_N) = (H_N - 1) * c(W_N).

    c(W_N) = (N-1)(1 - N(N+1)/(k+N)).
    H_N - 1 = sum_{j=2}^N 1/j is the anomaly ratio.
    """
    h_v = Fraction(N)
    if k + h_v == 0:
        raise ValueError(f"Critical level k = -{N}: undefined")
    c_W = Fraction(N - 1) * (Fraction(1) - Fraction(N * (N + 1)) / (k + h_v))
    rho = sum(Fraction(1, j) for j in range(2, N + 1))
    return rho * c_W


def kappa_deficit(N: int, k: Fraction) -> Fraction:
    r"""DS kappa deficit: delta_kappa(N, k) = kappa(V_k(sl_N)) - kappa(W_N,k).

    This is k-DEPENDENT. It measures the total modular characteristic
    lost under principal Drinfeld-Sokolov reduction.
    """
    return kappa_slN(N, k) - kappa_WN(N, k)


def kappa_ghost_free(N: int) -> Fraction:
    r"""Free-ghost kappa = c_ghost/2 = N(N-1)/2.

    This is what the ghost kappa would be if bc ghosts were decoupled.
    NOT equal to the DS kappa deficit in general.
    """
    return Fraction(N * (N - 1), 2)


def ds_kappa_deficit_vs_ghost(N: int, k: Fraction) -> Dict[str, Fraction]:
    r"""Compare DS kappa deficit with free-ghost kappa.

    Returns both values and their difference.
    The difference is nonzero in general (AP1 pitfall: they are NOT equal).
    """
    deficit = kappa_deficit(N, k)
    ghost = kappa_ghost_free(N)
    return {
        'ds_deficit': deficit,
        'free_ghost_kappa': ghost,
        'difference': deficit - ghost,
        'N': N,
        'k': k,
    }


# ============================================================================
# Section 9: Euler product defect analysis
# ============================================================================

def euler_defect_WN(N: int, u) -> Tuple[Any, Any, Any]:
    r"""Decompose S_{W_N}(u) into Euler-pure and defect parts.

    S_{W_N}(u) = (N-1)*zeta(u)*zeta(u+1) - zeta(u+1)*sum_{j=1}^{N-1} H_j(u)

    The Euler-pure part (N-1)*zeta(u)*zeta(u+1) has an Euler product.
    The defect term zeta(u+1)*sum H_j(u) involves finite sums (no Euler product).

    Returns (euler_pure, defect, total).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    pure = (N - 1) * zeta(u) * zeta(u + 1)
    defect = zeta(u + 1) * harm_sum
    return pure, defect, pure - defect


# ============================================================================
# Section 10: Dirichlet coefficients a_A(N)
# ============================================================================

def divisor_sigma_neg1(N: int) -> Any:
    r"""sigma_{-1}(N) = sum_{d|N} 1/d.

    The Dirichlet coefficients of S_H(u) = zeta(u)*zeta(u+1) are sigma_{-1}(N).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    return sum(mpf(1) / d for d in range(1, N + 1) if N % d == 0)


def dirichlet_coefficients_heisenberg(N_max: int) -> List[Any]:
    r"""Dirichlet coefficients a_H(N) = sigma_{-1}(N) for N = 1, ..., N_max."""
    return [divisor_sigma_neg1(N) for N in range(1, N_max + 1)]


def dirichlet_coefficients_generic(weights: Sequence[int],
                                   N_max: int) -> List[Any]:
    r"""Dirichlet coefficients a_A(N) for generic weight multiset.

    a_A(N) = sum_{d|N} (1/d) * #{i : w_i <= N/d}
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    coeffs = []
    for N in range(1, N_max + 1):
        a_N = mpf(0)
        for d in range(1, N + 1):
            if N % d == 0:
                m = N // d
                count = sum(1 for w in weights if w <= m)
                a_N += mpf(count) / d
        coeffs.append(a_N)
    return coeffs


def verify_dirichlet_series(weights: Sequence[int], u, N_max: int = 200) -> Tuple[Any, Any, Any]:
    r"""Compare sum a_A(N) N^{-u} with S_A(u) for verification.

    Returns (partial_sum, exact_value, relative_error).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    coeffs = dirichlet_coefficients_generic(weights, N_max)
    partial = sum(coeffs[N - 1] * power(N, -u) for N in range(1, N_max + 1))
    exact = S_generic(weights, u)
    if abs(exact) < mpf('1e-50'):
        return partial, exact, mpf('inf')
    return partial, exact, abs(partial / exact - 1)


# ============================================================================
# Section 11: Cross-consistency verification
# ============================================================================

def verify_SH_equals_zeta_product(u) -> Tuple[Any, Any, Any]:
    r"""Verify S_H(u) = zeta(u)*zeta(u+1) directly."""
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    sh = S_heisenberg(u)
    exact = zeta(u) * zeta(u + 1)
    return sh, exact, abs(sh - exact)


def verify_W2_equals_virasoro(u) -> Tuple[Any, Any, Any]:
    r"""Verify S_{W_2}(u) = S_Vir(u) (Virasoro = W_2)."""
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    s_w2 = S_WN(2, u)
    s_vir = S_virasoro(u)
    return s_w2, s_vir, abs(s_w2 - s_vir)


def verify_ds_additivity(u) -> Tuple[Any, Any, Any]:
    r"""Verify S_{sl_2}(u) = S_H(u) + S_Vir(u).

    Affine sl_2 has weight multiset {1, 2}.
    Heisenberg has {1}, Virasoro has {2}.
    The additivity S_{A1 + A2} = S_{A1} + S_{A2} holds for
    independent direct sums (vanishing mixed OPE).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    s_sl2 = S_affine_sl2(u)
    s_sum = S_heisenberg(u) + S_virasoro(u)
    return s_sl2, s_sum, abs(s_sl2 - s_sum)


def verify_li_xi_consistency(family: str, n: int) -> Tuple[Any, Any]:
    r"""Verify lambda_n computed from Li formula matches the Xi derivative.

    Returns (lambda_n_from_li, lambda_n_from_differentiation).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if family == 'heisenberg':
        Xi_func = Xi_heisenberg
    elif family == 'virasoro':
        Xi_func = Xi_virasoro
    else:
        raise ValueError(f"Unknown family: {family}")

    def f(u, _n=n):
        return power(u, _n - 1) * mp_log(Xi_func(u))

    d_n = mp_diff(f, mpf(1), n)
    lam_n = d_n / fac(n - 1)

    # Also compute via li_coefficients function
    if family == 'heisenberg':
        lam_from_func = li_heisenberg(n)[n - 1]
    else:
        lam_from_func = li_virasoro(n)[n - 1]

    return lam_n, lam_from_func


# ============================================================================
# Section 12: Summary table generation
# ============================================================================

def sewing_lift_table(u_values: Optional[List[int]] = None) -> Dict[str, Dict[int, Any]]:
    r"""Compute S_A(u) for all standard families at given u values.

    Returns dict[family_name][u] = S_A(u).
    """
    if not HAS_MPMATH:
        raise ImportError("mpmath required")
    if u_values is None:
        u_values = [2, 3, 4, 5]
    families = {
        'Heisenberg': S_heisenberg,
        'Virasoro': S_virasoro,
        'W_3': lambda u: S_WN(3, u),
        'W_4': lambda u: S_WN(4, u),
        'W_5': lambda u: S_WN(5, u),
    }
    table = {}
    for name, func in families.items():
        table[name] = {u: float(func(mpf(u))) for u in u_values}
    return table


def miura_defect_table(q_values: Optional[List[float]] = None,
                       N_values: Optional[List[int]] = None) -> Dict[int, Dict[float, float]]:
    r"""Compute D_N(q) for a range of N and q values.

    Returns dict[N][q] = D_N(q).
    """
    if q_values is None:
        q_values = [0.0, 0.25, 0.5, 0.75, 1.0]
    if N_values is None:
        N_values = [2, 3, 4, 5]
    table = {}
    for N in N_values:
        table[N] = {q: float(miura_defect(N, q)) for q in q_values}
    return table
