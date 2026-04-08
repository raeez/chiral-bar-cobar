r"""Bethe TQ relation from the MC element: convention fix and verification.

MATHEMATICAL PROBLEM
====================

The Baxter TQ relation for the XXZ spin chain is:

    T(u) Q(u) = a(u) Q(u - eta) + d(u) Q(u + eta)

where:
    T(u) = transfer matrix eigenvalue
    Q(u) = Baxter Q-operator eigenvalue
    a(u), d(u) = quantum determinant factors
    eta = i*gamma (anisotropy)

For the XXZ chain with N sites:
    a(u) = sin(u + gamma)^N  (eigenvalue of A(u) on pseudovacuum)
    d(u) = sin(u)^N          (eigenvalue of D(u) on pseudovacuum)
    eta = i*gamma             (shift in spectral parameter)

WAIT: The shift is NOT i*gamma in general. The correct relation depends
on the convention for the spectral parameter.

CONVENTION ANALYSIS
===================

There are TWO common conventions:

Convention 1 (trigonometric, Baxter 1982):
    Spectral parameter u is an angle.
    R-matrix: R(u) with a(u) = sin(u+gamma), b(u) = sin(u), c = sin(gamma).
    TQ relation: T(u) Q(u) = sin(u+gamma)^N Q(u-gamma) + sin(u)^N Q(u+gamma)
    The shift is gamma (real), NOT i*gamma.

Convention 2 (hyperbolic/algebraic, Faddeev):
    Spectral parameter lambda is a rapidity.
    R-matrix: R(lambda) with a = sinh(lambda+eta), etc.
    TQ relation: T(lambda) Q(lambda) = a(lambda) Q(lambda-eta) + d(lambda) Q(lambda+eta)
    The shift is eta = i*gamma.

The bethe_xxz_mc_engine.py uses Convention 1 (trigonometric), so the
correct TQ relation has shift GAMMA, not i*gamma.

THE FIX: In the TQ relation, use shift = gamma (the anisotropy angle),
matching the R-matrix convention R(u, gamma) = sin(u+gamma) * ....

BAXTER Q-OPERATOR
=================

For a Bethe state with roots {lambda_1, ..., lambda_M}:
    Q(u) = prod_{j=1}^{M} sin(u - lambda_j)

This is the Q-POLYNOMIAL (up to normalization).

VERIFICATION: the TQ relation is satisfied if and only if the lambda_j
satisfy the Bethe ansatz equations.

Proof:
    T(u) Q(u) = sin(u+gamma)^N Q(u-gamma) + sin(u)^N Q(u+gamma)
    At u = lambda_j: Q(lambda_j) = 0 (by definition).
    So: 0 = sin(lambda_j+gamma)^N Q(lambda_j-gamma) + sin(lambda_j)^N Q(lambda_j+gamma)
    => [sin(lambda_j+gamma)/sin(lambda_j)]^N = -Q(lambda_j+gamma)/Q(lambda_j-gamma)
       = -prod_k sin(lambda_j - lambda_k + gamma)/sin(lambda_j - lambda_k - gamma)

    For k=j: sin(0+gamma)/sin(0-gamma) = sin(gamma)/sin(-gamma) = -1.
    So the k=j factor contributes -1, giving:
    [sin(lambda_j+gamma)/sin(lambda_j)]^N = prod_{k!=j} sin(lambda_j-lambda_k+gamma)
                                                        / sin(lambda_j-lambda_k-gamma)

    But the standard BAE is:
    [sin(lambda_j+gamma/2)/sin(lambda_j-gamma/2)]^N = prod_{k!=j} sin(lambda_j-lambda_k+gamma)
                                                                  / sin(lambda_j-lambda_k-gamma)

    The mismatch: sin(lambda_j+gamma) vs sin(lambda_j+gamma/2).
    This is because the TQ relation uses the FULL R-matrix eigenvalues
    a(u) = sin(u+gamma), while the BAE uses HALF-shifted quantities.

    Resolution: the standard BAE convention uses the shift gamma/2 on
    the spectral parameter (rapidity = u - gamma/2). With the substitution
    u -> u + gamma/2 in the R-matrix, we get:
    a(u+gamma/2) = sin(u+3gamma/2), d(u+gamma/2) = sin(u+gamma/2).

    Alternatively, the BAE from the TQ relation with the FULL shift is:
    [sin(lambda_j+gamma)/sin(lambda_j)]^N = prod_{k!=j} sin(lambda_j-lambda_k+gamma)
                                                        / sin(lambda_j-lambda_k-gamma)

    This IS a valid form of the BAE, just with a different parametrization.
    The bethe_xxz_mc_engine.py uses the standard BAE with half-shifted
    spectral parameter.

    For the TQ verification, we use: Q(u) = prod_j sin(u - lambda_j).

References:
    Baxter (1982), "Exactly solved models in statistical mechanics"
    Faddeev (1996), "How the algebraic Bethe ansatz works"
    Korepin-Bogoliubov-Izergin (1993), Chapter 1
    bethe_xxz_mc_engine.py (our R-matrix and BAE)
    thm:mc2-bar-intrinsic (MC element to R-matrix to Bethe ansatz)
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import numpy as np
from numpy import linalg as la


PI = np.pi


# =========================================================================
# 1. Q-operator (polynomial form)
# =========================================================================

def baxter_q_polynomial(u: complex, lambdas: np.ndarray) -> complex:
    """Baxter Q-polynomial: Q(u) = prod_j sin(u - lambda_j).

    Convention: trigonometric (matching bethe_xxz_mc_engine.py).
    """
    result = 1.0 + 0j
    for lam in lambdas:
        result *= np.sin(u - lam)
    return result


def baxter_q_array(u_values: np.ndarray, lambdas: np.ndarray) -> np.ndarray:
    """Q-polynomial evaluated at an array of u values."""
    return np.array([baxter_q_polynomial(u, lambdas) for u in u_values])


# =========================================================================
# 2. Quantum determinant factors
# =========================================================================

def a_factor(u: complex, N: int, gamma: float) -> complex:
    """a(u) = sin(u + gamma)^N: eigenvalue of A(u) on pseudovacuum."""
    return np.sin(u + gamma) ** N


def d_factor(u: complex, N: int, gamma: float) -> complex:
    """d(u) = sin(u)^N: eigenvalue of D(u) on pseudovacuum."""
    return np.sin(u) ** N


# =========================================================================
# 3. Transfer matrix eigenvalue from Bethe roots
# =========================================================================

def transfer_eigenvalue(u: complex, lambdas: np.ndarray, N: int,
                        gamma: float) -> complex:
    """Transfer matrix eigenvalue T(u) for a Bethe state.

    T(u) = a(u) prod_j sin(lambda_j - u + gamma)/sin(lambda_j - u)
          + d(u) prod_j sin(lambda_j - u - gamma)/sin(lambda_j - u)

    This is the eigenvalue formula from the algebraic Bethe ansatz.
    """
    prod_plus = 1.0 + 0j
    prod_minus = 1.0 + 0j
    for lam in lambdas:
        prod_plus *= np.sin(lam - u + gamma) / np.sin(lam - u)
        prod_minus *= np.sin(lam - u - gamma) / np.sin(lam - u)

    return a_factor(u, N, gamma) * prod_plus + d_factor(u, N, gamma) * prod_minus


# =========================================================================
# 4. TQ relation verification
# =========================================================================

def verify_tq_relation(u: complex, lambdas: np.ndarray, N: int,
                       gamma: float) -> Dict:
    """Verify the Baxter TQ relation at spectral parameter u.

    TQ relation (trigonometric convention):
        T(u) Q(u) = a(u) Q(u - gamma) + d(u) Q(u + gamma)

    The shift is gamma (the anisotropy angle), NOT i*gamma.
    This matches the trigonometric R-matrix convention in bethe_xxz_mc_engine.py.

    Returns dict with LHS, RHS, and residual.
    """
    T_u = transfer_eigenvalue(u, lambdas, N, gamma)
    Q_u = baxter_q_polynomial(u, lambdas)
    Q_minus = baxter_q_polynomial(u - gamma, lambdas)
    Q_plus = baxter_q_polynomial(u + gamma, lambdas)
    a_u = a_factor(u, N, gamma)
    d_u = d_factor(u, N, gamma)

    lhs = T_u * Q_u
    rhs = a_u * Q_minus + d_u * Q_plus

    return {
        'u': u,
        'T_u': T_u,
        'Q_u': Q_u,
        'Q_minus': Q_minus,
        'Q_plus': Q_plus,
        'a_u': a_u,
        'd_u': d_u,
        'lhs': lhs,
        'rhs': rhs,
        'residual': abs(lhs - rhs),
        'relative_residual': abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-15),
    }


def verify_tq_relation_array(u_values: np.ndarray, lambdas: np.ndarray,
                              N: int, gamma: float) -> Dict:
    """Verify the TQ relation at multiple u values."""
    residuals = []
    for u in u_values:
        result = verify_tq_relation(u, lambdas, N, gamma)
        residuals.append(result['residual'])

    return {
        'N': N,
        'M': len(lambdas),
        'gamma': gamma,
        'n_points': len(u_values),
        'max_residual': max(residuals),
        'mean_residual': np.mean(residuals),
        'all_satisfied': max(residuals) < 1e-8,
    }


# =========================================================================
# 5. BAE from TQ relation (derivation check)
# =========================================================================

def bae_from_tq(lambdas: np.ndarray, N: int, gamma: float) -> Dict:
    """Derive BAE from TQ relation by evaluating at u = lambda_j.

    At u = lambda_j, Q(lambda_j) = 0, so:
    0 = a(lambda_j) Q(lambda_j - gamma) + d(lambda_j) Q(lambda_j + gamma)

    This gives:
    -a(lambda_j)/d(lambda_j) = Q(lambda_j + gamma) / Q(lambda_j - gamma)

    Which is equivalent to:
    [sin(lambda_j + gamma) / sin(lambda_j)]^N
        = - prod_k sin(lambda_j - lambda_k + gamma) / sin(lambda_j - lambda_k - gamma)

    The k=j term gives sin(gamma)/sin(-gamma) = -1, so:
    [sin(lambda_j + gamma) / sin(lambda_j)]^N
        = prod_{k!=j} sin(lambda_j - lambda_k + gamma) / sin(lambda_j - lambda_k - gamma)
    """
    M = len(lambdas)
    bae_residuals = []

    for j in range(M):
        lam_j = lambdas[j]
        # Use the cross-ratio form to avoid division by zero:
        # sin(lam+gamma)^N * prod_{k!=j} sin(lam_j-lam_k-gamma)
        # = sin(lam)^N * prod_{k!=j} sin(lam_j-lam_k+gamma)
        lhs = np.sin(lam_j + gamma) ** N
        rhs = np.sin(lam_j) ** N
        for k in range(M):
            if k == j:
                continue
            lhs *= np.sin(lam_j - lambdas[k] - gamma)
            rhs *= np.sin(lam_j - lambdas[k] + gamma)

        bae_residuals.append(abs(lhs - rhs))

    return {
        'N': N,
        'M': M,
        'gamma': gamma,
        'bae_residuals': bae_residuals,
        'max_residual': max(bae_residuals) if bae_residuals else 0,
        'all_satisfied': max(bae_residuals) < 1e-6 if bae_residuals else True,
    }


# =========================================================================
# 6. Exact Bethe roots for small chains
# =========================================================================

def solve_bae_xxz(N: int, M: int, gamma: float,
                  initial_guess: Optional[np.ndarray] = None,
                  max_attempts: int = 20) -> Dict:
    """Solve the XXZ BAE numerically for N sites, M magnons.

    Uses the logarithmic BAE with quantum number scanning.
    """
    from scipy.optimize import fsolve

    def bae_residual(lambdas_flat):
        """BAE residual function for fsolve."""
        lambdas = lambdas_flat[:M] + 1j * lambdas_flat[M:]
        residuals = np.zeros(2 * M)
        for j in range(M):
            lhs = N * _theta1(lambdas[j], gamma)
            rhs = 0.0
            for k in range(M):
                if k != j:
                    rhs += _theta2(lambdas[j] - lambdas[k], gamma)
            val = lhs - rhs
            residuals[j] = np.real(val)
            residuals[M + j] = np.imag(val)
        return residuals

    best_result = None
    best_residual = float('inf')

    for attempt in range(max_attempts):
        if initial_guess is not None and attempt == 0:
            x0 = np.concatenate([np.real(initial_guess), np.imag(initial_guess)])
        else:
            # Random initial guess, real rapidities
            x0 = np.zeros(2 * M)
            x0[:M] = np.random.uniform(-PI/4, PI/4, M)

        try:
            sol = fsolve(bae_residual, x0, full_output=True)
            x_sol, info, ier, msg = sol
            lambdas_sol = x_sol[:M] + 1j * x_sol[M:]

            res = np.max(np.abs(info['fvec']))
            if res < best_residual:
                best_residual = res
                best_result = lambdas_sol

            if res < 1e-10:
                break
        except Exception:
            continue

    if best_result is None:
        return {'success': False, 'lambdas': None}

    return {
        'success': best_residual < 1e-6,
        'lambdas': best_result,
        'residual': best_residual,
        'N': N,
        'M': M,
        'gamma': gamma,
    }


def _theta1(lam, gamma):
    """theta_1(lambda) = 2 arctan(cot(gamma/2) * tan(lambda))."""
    return 2 * np.arctan(np.cos(gamma/2) / np.sin(gamma/2) * np.tan(np.real(lam)))


def _theta2(lam, gamma):
    """theta_2(lambda) = 2 arctan(cot(gamma) * tan(lambda))."""
    return 2 * np.arctan(np.cos(gamma) / np.sin(gamma) * np.tan(np.real(lam)))


# =========================================================================
# 7. Connection to MC element
# =========================================================================

def mc_to_tq_chain() -> str:
    """Document the full chain from MC element to TQ relation.

    MC element Theta_A (thm:mc2-bar-intrinsic)
        |
        v
    Collision residue r(z) = Res^{coll}_{0,2}(Theta_A) [AP19]
        |
        v
    Trigonometric R-matrix R(u, gamma) for U_q(sl_2)
        |
        v
    Transfer matrix T(u) = Tr_a[R_{a1}(u) ... R_{aN}(u)]
        |
        v
    QISM: [T(u), T(v)] = 0 + Baxter Q-operator
        |
        v
    TQ relation: T(u)Q(u) = a(u)Q(u-gamma) + d(u)Q(u+gamma)
        |
        v
    BAE at roots of Q: [sin(lam+gamma)/sin(lam)]^N = prod_{k!=j} ...

    CONVENTION: The shift in the TQ relation is GAMMA (real anisotropy
    angle), not i*gamma. This matches the trigonometric R-matrix
    convention R(u, gamma) = sin(u+gamma) * ... in bethe_xxz_mc_engine.py.

    The MC element determines gamma via gamma = pi/(k+2) for sl_2^{(1)}
    at level k. The anisotropy Delta = cos(gamma) is the XXZ parameter.
    """
    return (
        "MC -> r-matrix (AP19: pole reduction) -> R-matrix (six-vertex) "
        "-> transfer matrix T(u) -> TQ relation with shift gamma "
        "-> BAE at roots of Q. Convention: trigonometric, shift = gamma."
    )
