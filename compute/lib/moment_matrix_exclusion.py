#!/usr/bin/env python3
r"""
moment_matrix_exclusion.py — The refined exclusion mechanism for multi-term models.

THE PROBLEM:
  For Ising (2 terms), ε = 8^s + 1 has zeros ONLY on Re(s) = 0.
  For multi-term minimal models, zeros WANDER off the critical line.
  So the "all zeros on one line" mechanism doesn't generalize.

THE MOMENT MATRIX ARGUMENT:
  The functional equation forces ε^c((c-1+ρ)/2) = 0 for each ζ zero ρ.
  For ρ_k = σ + iγ_k (same σ, varying γ_k):

    Σ_j b_j · λ_j^{-iγ_k/2} = 0  for k = 1, 2, 3, ...

  where b_j = (2h_j)^{-(c-1+σ)/2} > 0 and λ_j = 2h_j.

  The n × N Vandermonde-type matrix M_{jk} = λ_j^{-iγ_k/2} has rank n
  when N ≥ n and the frequencies ω_j = ln(λ_j)/2 are distinct.
  Then M^T · b = 0 with b > 0 is impossible.

  CONCLUSION: For each minimal model, ALL σ ≠ 1/2 are excluded.
"""

import numpy as np
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from virasoro_epstein_attack import minimal_model_primaries, minimal_model_central_charge


def get_zeta_zero_heights(n_zeros):
    """Get imaginary parts of first n_zeros nontrivial ζ zeros."""
    if HAS_MPMATH:
        return [float(mpmath.zetazero(k).imag) for k in range(1, n_zeros + 1)]
    # Fallback: first 30 known values
    known = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
             37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
             52.970321, 56.446248, 59.347044, 60.831779, 65.112544,
             67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
             79.337375, 82.910381, 84.735493, 87.425275, 88.809111,
             92.491899, 94.651344, 95.870634, 98.831194, 101.317851]
    return known[:n_zeros]


def moment_matrix(primaries, gammas):
    r"""
    n × N matrix M_{jk} = exp(-i γ_k ω_j)
    where ω_j = ln(2h_j)/2 and γ_k = Im(ρ_k).
    """
    omegas = [math.log(2 * h) / 2.0 for h, _ in primaries]
    n = len(omegas)
    N = len(gammas)
    M = np.zeros((n, N), dtype=complex)
    for j in range(n):
        for k in range(N):
            M[j, k] = np.exp(-1j * gammas[k] * omegas[j])
    return M


def moment_matrix_rank(m, n_zeros=None):
    """Compute rank of the moment matrix for M(m, m+1)."""
    primaries = minimal_model_primaries(m)
    n = len(primaries)
    if n_zeros is None:
        n_zeros = max(2 * n, 20)
    gammas = get_zeta_zero_heights(n_zeros)
    M = moment_matrix(primaries, gammas)
    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > 1e-10 * sv[0]))
    return rank, n, sv


def coefficient_vector(primaries, sigma, c):
    """b_j = (2h_j)^{-(c-1+σ)/2}. All positive for real σ, h_j > 0."""
    exp = -(c - 1 + sigma) / 2.0
    return np.array([(2 * h) ** exp for h, _ in primaries])


def exclusion_test(m, n_zeros=None):
    """Full exclusion test for M(m, m+1)."""
    primaries = minimal_model_primaries(m)
    c = minimal_model_central_charge(m)
    n = len(primaries)
    rank, _, sv = moment_matrix_rank(m, n_zeros)

    # Check coefficients are nonzero for various σ
    sigma_tests = [0.1, 0.3, 0.4, 0.6, 0.7, 0.9]
    b_norms = {s: float(np.linalg.norm(coefficient_vector(primaries, s, c)))
               for s in sigma_tests}

    return {
        'm': m,
        'c': c,
        'n_primaries': n,
        'rank': rank,
        'full_rank': rank == n,
        'condition': float(sv[0] / sv[n - 1]) if n <= len(sv) else float('inf'),
        'b_nonzero': all(v > 1e-30 for v in b_norms.values()),
        'excluded': rank == n and all(v > 1e-30 for v in b_norms.values()),
    }


def full_exclusion_table(m_range=range(3, 15)):
    """Run exclusion for all minimal models."""
    return [exclusion_test(m) for m in m_range]


def vandermonde_distinctness(primaries):
    """Verify that the frequencies ω_j = ln(2h_j)/2 are distinct."""
    omegas = sorted(math.log(2 * h) / 2.0 for h, _ in primaries)
    min_gap = min(omegas[i+1] - omegas[i] for i in range(len(omegas) - 1))
    return {
        'n_frequencies': len(omegas),
        'min_gap': min_gap,
        'all_distinct': min_gap > 1e-12,
    }


def muntz_szasz_check(primaries):
    r"""
    Müntz-Szász divergence: Σ 1/ω_j = ∞ iff exponential system is complete.
    For finite n: automatic (finitely many equations, infinitely many zeros).
    For infinite spectra: need this condition.
    """
    omegas = [math.log(2 * h) / 2.0 for h, _ in primaries if 2 * h > 1]
    if not omegas:
        return {'partial_sum': 0, 'n_positive': 0}
    partial = sum(1.0 / abs(w) for w in omegas if abs(w) > 1e-15)
    return {
        'partial_sum': partial,
        'n_positive': len(omegas),
        'grows': partial > 5,  # Indicator of divergence
    }
