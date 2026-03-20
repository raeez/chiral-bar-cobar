"""Matrix Rankin-Selberg integral for VVMF character vectors.

For a VVMF F = (chi_0, chi_1, ..., chi_{n-1}) of a RCFT, define the
n x n matrix Rankin-Selberg integral:

    L_{ij}(s) = int_{SL(2,Z) \\ H}  chi_i(tau) * conj(chi_j(tau)) * y^s * dx dy / y^2

The classical scalar Rankin-Selberg integral is the trace L(s) = sum_i L_{ii}(s).

The Rankin-Selberg unfolding reduces L_{ij}(s) to a Dirichlet series:
    L_{ij}(s) = (completed gamma) * sum_n c_{ij}(n) n^{-s}
where c_{ij}(n) = sum_{m : h_i - c/24 + m_1 = n, h_j - c/24 + m_2 = n} a_i(m_1) * a_j(m_2)
           [with appropriate Parseval pairing on x-integral].

More precisely, for i = j:
    c_{ii}(n) = |a_i(n)|^2 = a_i(n)^2     (since a_i are real for minimal models)
For i != j with h_i + h_j - c/12 + m = "n":
    c_{ij}(n) = a_i(m_1) * a_j(m_2) where m_1, m_2 match exponents.

This module implements:
  1. Full numeric integration of L_{ij}(s) on truncated fundamental domain
  2. Unfolded Dirichlet coefficients via Parseval on x-integral
  3. S-matrix diagonalization to eigenbasis characters
  4. Determinant and trace L-functions
  5. Multiplicativity tests for all matrix entries
  6. Conductor/gamma factors and functional equation tests
  7. Comparison with lattice (V_Z) case

Uses mpmath for high-precision computation throughout.

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import mpmath
from mpmath import (mp, mpf, mpc, pi, exp, sin, cos, sqrt, log, fabs,
                    power, gamma as mpgamma, fsum, quad, inf, zeta, conj,
                    re as mpre, im as mpim, matrix as mpmatrix, nstr)

from compute.lib.vvmf_hecke import (
    MinimalModel,
    ising_model,
    tricritical_ising_model,
    three_state_potts_model,
    character_qseries,
    character_value,
    character_vector,
    s_matrix,
    t_matrix,
)


# ---------------------------------------------------------------------------
# Precision
# ---------------------------------------------------------------------------

DEFAULT_DPS = 30


def _set_dps(dps: int = DEFAULT_DPS):
    mp.dps = dps


# ============================================================================
# 1. Ising characters: precompute q-series data
# ============================================================================

def ising_character_data(num_terms: int = 100, dps: int = DEFAULT_DPS):
    """Return Ising model, labels, conformal weights, central charge, and q-series.

    Returns dict with keys:
      'model', 'labels', 'weights', 'c', 'qseries' (list of lists of mpf)
    """
    _set_dps(dps)
    model = ising_model()
    labels = model.primary_labels()
    weights = [model.conformal_weight_mpf(lab.r, lab.s) for lab in labels]
    c = model.central_charge_mpf
    qseries = [
        character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        for lab in labels
    ]
    return {
        'model': model,
        'labels': labels,
        'weights': weights,
        'c': c,
        'qseries': qseries,
    }


# ============================================================================
# 2. Unfolded Dirichlet coefficients: Parseval on x-integral
# ============================================================================

def unfolded_dirichlet_coeffs_diagonal(qseries_i, h_i, c, N_max, dps=DEFAULT_DPS):
    """Diagonal Dirichlet coefficients c_{ii}(n) = a_i(n)^2.

    The x-integral of |chi_i|^2 via Parseval gives:
        integral_{-1/2}^{1/2} |chi_i(x + iy)|^2 dx
        = sum_{n >= 0} |a_i(n)|^2 * exp(-4 pi (h_i - c/24 + n) y)

    After Mellin transform in y, we get the Dirichlet series
        D_{ii}(s) = sum_n |a_i(n)|^2 * (4 pi (h_i - c/24 + n))^{-s}

    We extract coefficients indexed by n (the level).
    Returns list of (exponent, coefficient) pairs.
    """
    _set_dps(dps)
    h0 = h_i - c / 24
    coeffs = []
    for n in range(min(N_max, len(qseries_i))):
        a_n = qseries_i[n]
        if a_n == 0:
            continue
        exponent = h0 + n  # the actual q-exponent
        coeff = a_n * a_n  # |a_i(n)|^2 = a_i(n)^2 since real
        coeffs.append((float(exponent), float(coeff)))
    return coeffs


def unfolded_dirichlet_coeffs_offdiag(qseries_i, qseries_j, h_i, h_j, c,
                                       N_max, dps=DEFAULT_DPS):
    """Off-diagonal Dirichlet coefficients c_{ij}(n) = a_i(n) * a_j(n).

    The x-integral of chi_i * conj(chi_j) via Parseval:
        integral_{-1/2}^{1/2} chi_i(x+iy) * conj(chi_j(x+iy)) dx

    chi_i(tau) = sum_n a_i(n) * q^{h_i - c/24 + n}
               = sum_n a_i(n) * exp(2 pi i (h_i - c/24 + n) tau)

    conj(chi_j(tau)) = sum_m a_j(m) * exp(-2 pi i (h_j - c/24 + m) conj(tau))

    For tau = x + iy:
        chi_i * conj(chi_j) = sum_{n,m} a_i(n) a_j(m)
            * exp(2 pi i (h_i - c/24 + n) x) * exp(-2 pi (h_i - c/24 + n) y)
            * exp(-2 pi i (h_j - c/24 + m) x) * exp(-2 pi (h_j - c/24 + m) y)

    Integrating over x picks out h_i - c/24 + n = h_j - c/24 + m,
    i.e., n - m = h_j - h_i.

    If h_i = h_j: pair (n, n) with coefficient a_i(n) * a_j(n).
    If h_j - h_i = integer k: pair (n, n - k) with coefficient a_i(n) * a_j(n - k).
    If h_j - h_i is non-integer: the x-integral vanishes identically!

    Returns list of (exponent, coefficient) pairs, or empty list if h_j - h_i
    is not an integer.
    """
    _set_dps(dps)
    delta_h = h_j - h_i  # h_j - h_i
    # Check if delta_h is (close to) an integer
    delta_h_float = float(delta_h)
    k = round(delta_h_float)
    if abs(delta_h_float - k) > 1e-10:
        # Non-integer weight difference: x-integral vanishes
        return []

    h0_i = h_i - c / 24
    coeffs = []
    for n in range(min(N_max, len(qseries_i))):
        m = n - k  # m = n - (h_j - h_i) so that exponents match
        if m < 0 or m >= len(qseries_j):
            continue
        a_n = qseries_i[n]
        a_m = qseries_j[m]
        if a_n == 0 or a_m == 0:
            continue
        exponent = h0_i + n  # = h0_j + m
        coeff = a_n * a_m
        coeffs.append((float(exponent), float(coeff)))
    return coeffs


# ============================================================================
# 3. Matrix L-function via numerical integration on fundamental domain
# ============================================================================

def _fundamental_domain_integrand(model, labels, i, j, s, tau, num_terms, dps):
    """Integrand chi_i(tau) * conj(chi_j(tau)) * y^s for the Rankin-Selberg integral."""
    _set_dps(dps)
    chi_i = character_value(model, labels[i].r, labels[i].s, tau,
                            num_terms=num_terms, dps=dps)
    chi_j = character_value(model, labels[j].r, labels[j].s, tau,
                            num_terms=num_terms, dps=dps)
    y = mpim(tau)
    return chi_i * conj(chi_j) * power(y, s)


def matrix_L_numerical(model, s_val, y_min=None, y_max=5.0,
                       nx=80, ny=120, num_terms=100, dps=DEFAULT_DPS):
    """Compute the n x n matrix L_{ij}(s) by numerical integration.

    Integration over the truncated fundamental domain:
        F_T = { tau = x + iy : |tau| >= 1, -1/2 <= x <= 1/2, sqrt(3)/2 <= y <= y_max }

    Uses midpoint-rule quadrature on a grid.

    Returns mpmath matrix L_{ij}(s).
    """
    _set_dps(dps)
    if y_min is None:
        y_min = sqrt(mpf(3)) / 2

    labels = model.primary_labels()
    n = len(labels)
    L = mpmatrix(n, n)

    # Grid on [x_lo, x_hi] x [y_min, y_max]
    dx = mpf(1) / nx
    dy = (mpf(y_max) - y_min) / ny

    for ix in range(nx):
        x = mpf(-0.5) + (ix + mpf(0.5)) * dx
        for iy in range(ny):
            y = y_min + (iy + mpf(0.5)) * dy
            tau = mpc(x, y)
            # Check if tau is in the fundamental domain: |tau| >= 1
            if abs(tau) < mpf(1) - mpf('1e-10'):
                continue
            # Measure: dx dy / y^2
            measure = dx * dy / (y * y)
            # Compute all characters at this point
            chars = character_vector(model, tau, num_terms=num_terms, dps=dps)
            ys = power(y, s_val)
            for i in range(n):
                for j in range(n):
                    L[i, j] += chars[i] * conj(chars[j]) * ys * measure

    return L


def matrix_L_fast(model, s_val, y_max=5.0, ny=200, num_terms=80, dps=DEFAULT_DPS):
    """Faster computation using the unfolded representation.

    After Rankin-Selberg unfolding (strip integration), we get:
        L_{ij}(s) = integral_0^infty phi_{ij}(y) * y^{s-2} dy

    where phi_{ij}(y) = integral_{-1/2}^{1/2} chi_i(tau) conj(chi_j(tau)) dx
    is the zero-th Fourier coefficient of chi_i * conj(chi_j).

    For diagonal i=j: phi_{ii}(y) = sum_n a_i(n)^2 * exp(-4 pi (h_i - c/24 + n) y)
    For off-diagonal: phi_{ij}(y) = sum_n a_i(n) a_j(n-k) * exp(-4 pi (h_i-c/24+n) y)
        if h_j - h_i = k (integer), else 0.

    The Mellin transform then gives:
        L_{ij}(s) = (4 pi)^{-s} * Gamma(s-1) * sum_n c_{ij}(n) * (h_i - c/24 + n)^{-(s-1)}

    This is the KEY formula. We compute it as a sum.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    n_chars = len(labels)
    c = model.central_charge_mpf
    weights = [model.conformal_weight_mpf(lab.r, lab.s) for lab in labels]

    qseries_all = [
        character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        for lab in labels
    ]

    L = mpmatrix(n_chars, n_chars)
    s = mpf(s_val)

    for i in range(n_chars):
        for j in range(n_chars):
            h_i = weights[i]
            h_j = weights[j]
            delta_h = h_j - h_i
            delta_h_f = float(delta_h)
            k = round(delta_h_f)

            if abs(delta_h_f - k) > 1e-10:
                # Non-integer weight difference: vanishes
                L[i, j] = mpf(0)
                continue

            h0_i = h_i - c / 24
            total = mpf(0)
            for m in range(num_terms):
                m2 = m - k  # paired index in chi_j
                if m2 < 0 or m2 >= len(qseries_all[j]):
                    continue
                a_i_m = qseries_all[i][m]
                a_j_m2 = qseries_all[j][m2]
                if a_i_m == 0 or a_j_m2 == 0:
                    continue
                exponent = h0_i + m
                if exponent <= 0:
                    continue
                total += a_i_m * a_j_m2 * power(4 * pi * exponent, -(s - 1))

            L[i, j] = mpgamma(s - 1) * total

    return L


# ============================================================================
# 4. Multiplicativity testing
# ============================================================================

def extract_dirichlet_coeffs(qseries_i, qseries_j, h_i, h_j, c,
                              N_max=50, dps=DEFAULT_DPS):
    """Extract Dirichlet-series coefficients c_{ij}(n).

    From the unfolded integral:
        L_{ij}(s) ~ sum_n c_{ij}(n) * lambda_n^{-s}

    where lambda_n = 4 pi (h_i - c/24 + n) are the eigenvalues,
    and c_{ij}(n) = a_i(n) * a_j(n - k) with k = h_j - h_i.

    Returns list of (n, c_{ij}(n)) for n = 0, 1, ..., N_max-1.
    """
    _set_dps(dps)
    delta_h = h_j - h_i
    delta_h_f = float(delta_h)
    k = round(delta_h_f)

    if abs(delta_h_f - k) > 1e-10:
        return [(n, mpf(0)) for n in range(N_max)]

    result = []
    for n in range(N_max):
        m = n - k
        if m < 0 or m >= len(qseries_j) or n >= len(qseries_i):
            result.append((n, mpf(0)))
        else:
            result.append((n, qseries_i[n] * qseries_j[m]))
    return result


def check_multiplicativity(coeffs, N_max=30):
    """Check whether coefficients c(n) satisfy c(mn) = c(m) c(n) for coprime m, n.

    Returns list of (m, n, c(mn), c(m)*c(n), relative_error) for coprime pairs.
    """
    from math import gcd
    results = []
    for m in range(2, N_max):
        for n in range(2, N_max):
            if m * n >= len(coeffs):
                continue
            if gcd(m, n) != 1:
                continue
            c_mn = coeffs[m * n]
            c_m = coeffs[m]
            c_n = coeffs[n]
            product = c_m * c_n
            if product == 0 and c_mn == 0:
                rel_err = mpf(0)
            elif product == 0:
                rel_err = mpf('inf')
            else:
                rel_err = abs(c_mn - product) / abs(product)
            results.append((m, n, float(c_mn), float(product), float(rel_err)))
    return results


def multiplicativity_score(coeffs, N_max=30):
    """Return fraction of coprime pairs (m,n) with c(mn) = c(m)*c(n) to relative tolerance.

    Score 1.0 = perfectly multiplicative, 0.0 = completely non-multiplicative.
    """
    results = check_multiplicativity(coeffs, N_max)
    if not results:
        return 1.0
    tol = 1e-6
    num_pass = sum(1 for _, _, _, _, err in results if err < tol)
    return num_pass / len(results)


# ============================================================================
# 5. S-matrix diagonalization: eigenbasis characters
# ============================================================================

def s_eigenbasis(model, dps=DEFAULT_DPS):
    """Compute the S-matrix eigenvectors and eigenvalues.

    For a unitary RCFT, S is symmetric and unitary, so S^2 = C (charge conjugation).
    Eigenvalues of S are roots of unity (specifically, values of Gauss sums).

    Returns (eigenvalues, eigenvectors_matrix) where eigenvectors_matrix columns
    are the eigenvectors.
    """
    _set_dps(dps)
    S = s_matrix(model, dps=dps)
    n = S.rows

    # Use mpmath eigensolver
    # S is real symmetric for minimal models
    # Convert to a standard form for eigensolver
    S_list = [[S[i, j] for j in range(n)] for i in range(n)]
    S_mp = mpmatrix(S_list)

    # mpmath eigsy for real symmetric
    eigenvalues, eigenvectors = mpmath.eigsy(S_mp)

    return eigenvalues, eigenvectors


def eigenbasis_characters(model, tau, num_terms=200, dps=DEFAULT_DPS):
    """Compute characters in the S-eigenbasis: psi_k = sum_i U_{ki} chi_i.

    Returns list of psi_k(tau) values.
    """
    _set_dps(dps)
    eigenvalues, U = s_eigenbasis(model, dps=dps)
    chars = character_vector(model, tau, num_terms=num_terms, dps=dps)
    n = len(chars)
    psi = []
    for k in range(n):
        val = fsum(U[k, i] * chars[i] for i in range(n))
        psi.append(val)
    return psi


def eigenbasis_qseries(model, num_terms=100, dps=DEFAULT_DPS):
    """Compute q-series coefficients of eigenbasis characters.

    psi_k = sum_i U_{ki} chi_i, so psi_k coefficients are
    b_k(n) = sum_i U_{ki} a_i(n) (when all weights are equal)
    or more generally a linear combination with weight shifts.

    For the Ising model, all three primaries have DIFFERENT conformal weights
    (0, 1/2, 1/16), so the eigenbasis characters are NOT standard q-series.
    Instead, they are sums of q-series with DIFFERENT leading powers.

    We return the eigenvector matrix U and the individual qseries, so the
    caller can reconstruct psi_k at any tau.
    """
    _set_dps(dps)
    eigenvalues, U = s_eigenbasis(model, dps=dps)
    labels = model.primary_labels()
    qseries = [
        character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)
        for lab in labels
    ]
    return eigenvalues, U, qseries


# ============================================================================
# 6. Eigenbasis Rankin-Selberg
# ============================================================================

def eigenbasis_L_matrix(model, s_val, num_terms=80, dps=DEFAULT_DPS):
    """Compute the Rankin-Selberg L-matrix in the S-eigenbasis.

    If L_{ij}(s) is the matrix in the original basis and U is the
    eigenvector matrix, then in the eigenbasis:
        Lambda_{kl}(s) = sum_{i,j} U_{ki} U_{lj} L_{ij}(s)
                       = (U L U^T)_{kl}

    Returns the transformed matrix.
    """
    _set_dps(dps)
    L = matrix_L_fast(model, s_val, num_terms=num_terms, dps=dps)
    eigenvalues, U = s_eigenbasis(model, dps=dps)
    n = L.rows
    # Lambda = U * L * U^T
    Lambda = U * L * U.T
    return Lambda, eigenvalues


# ============================================================================
# 7. Determinant and trace L-functions
# ============================================================================

def trace_L(L_matrix):
    """Trace of the matrix L-function: tr(L(s)) = sum_i L_{ii}(s)."""
    n = L_matrix.rows
    return fsum(L_matrix[i, i] for i in range(n))


def det_L(L_matrix):
    """Determinant of the matrix L-function: det(L(s))."""
    return mpmath.det(L_matrix)


def trace_L_values(model, s_values, num_terms=80, dps=DEFAULT_DPS):
    """Compute tr(L(s)) for a list of s values."""
    results = {}
    for s in s_values:
        L = matrix_L_fast(model, s, num_terms=num_terms, dps=dps)
        results[s] = trace_L(L)
    return results


def det_L_values(model, s_values, num_terms=80, dps=DEFAULT_DPS):
    """Compute det(L(s)) for a list of s values."""
    results = {}
    for s in s_values:
        L = matrix_L_fast(model, s, num_terms=num_terms, dps=dps)
        results[s] = det_L(L)
    return results


# ============================================================================
# 8. Functional equation infrastructure
# ============================================================================

def completed_L_entry(model, i, j, s_val, num_terms=80, dps=DEFAULT_DPS):
    """Completed L-function entry:

    Lambda_{ij}(s) = pi^{-s} * Gamma(s/2 + mu_{ij}/2) * L_{ij}(s)

    where mu_{ij} depends on h_i - h_j (the spectral parameter shift).

    For the Rankin-Selberg integral on SL(2,Z)\\H, the functional equation relates
    L_{ij}(s) to L_{ji}(1-s) with specific gamma factors.

    The standard Rankin-Selberg functional equation for |f|^2 * E_s is:
        Lambda(s) = Lambda(1-s)

    For the MATRIX version with f_i * conj(f_j), the functional equation becomes:
        Lambda_{ij}(s) = epsilon_{ij} * Lambda_{ji}(1-s)

    where epsilon_{ij} involves the S-matrix.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    h_i = model.conformal_weight_mpf(labels[i].r, labels[i].s)
    h_j = model.conformal_weight_mpf(labels[j].r, labels[j].s)
    mu_ij = h_i - h_j  # spectral parameter

    s = mpf(s_val)
    L = matrix_L_fast(model, s, num_terms=num_terms, dps=dps)
    L_ij = L[i, j]

    # Gamma factor: Gamma_R(s + mu) = pi^{-(s+mu)/2} Gamma((s+mu)/2)
    gamma_factor = power(pi, -(s + mu_ij) / 2) * mpgamma((s + mu_ij) / 2)

    return gamma_factor * L_ij


def functional_equation_test(model, i, j, s_val, num_terms=80, dps=DEFAULT_DPS):
    """Test the functional equation Lambda_{ij}(s) vs Lambda_{ji}(1-s).

    Returns (Lambda_ij(s), Lambda_ji(1-s), ratio).
    """
    _set_dps(dps)
    lhs = completed_L_entry(model, i, j, s_val, num_terms=num_terms, dps=dps)
    rhs = completed_L_entry(model, j, i, 1 - s_val, num_terms=num_terms, dps=dps)
    if abs(rhs) < mpf('1e-50'):
        ratio = mpf('inf') if abs(lhs) > mpf('1e-50') else mpf(1)
    else:
        ratio = lhs / rhs
    return lhs, rhs, ratio


# ============================================================================
# 9. Lattice VOA comparison (V_Z)
# ============================================================================

def lattice_vz_L(s_val, dps=DEFAULT_DPS):
    """L(s) for V_Z (rank-1 lattice VOA with 1 character).

    V_Z has a single character chi_0(tau) = theta_3(tau) / eta(tau)
    (or more precisely the lattice theta function).

    The Rankin-Selberg of |chi_0|^2 against E_s gives:
        L(s) = 4 zeta(2s)  (up to normalization)

    This is perfectly multiplicative because the lattice VOA has rank 1 and
    the divisor sum factorizes over primes.
    """
    _set_dps(dps)
    s = mpf(s_val)
    return 4 * zeta(2 * s)


def lattice_vz_dirichlet_coeffs(N_max=50, dps=DEFAULT_DPS):
    """Dirichlet coefficients for V_Z: c(n) ~ r_2(n) (representation numbers).

    For the theta function theta_3(tau) = sum_{n in Z} q^{n^2},
    |theta_3|^2 * y^s under Rankin-Selberg gives Dirichlet series
    with multiplicative coefficients (sums of two squares).
    """
    _set_dps(dps)
    coeffs = [mpf(0)] * N_max
    for n in range(N_max):
        # r_2(n) = number of ways to write n as sum of two squares (signed)
        # Actually for lattice Rankin-Selberg, the coefficients are
        # c(n) = sigma_0(n) = d(n) for the simplest normalization,
        # coming from |eta|^{-2} decomposition.
        # For V_Z with chi = 1/eta: |1/eta|^2 has Fourier coeffs sum_{k} p(k)^2
        # which is NOT multiplicative.
        #
        # The correct statement: the SCALAR Dirichlet series from sewing
        # for Heisenberg (= V_Z as current algebra) is
        #   S_H(u) = zeta(u) * zeta(u+1) = sum_n sigma_{-1}(n) n^{-u}
        # which IS multiplicative because sigma_{-1} is multiplicative.
        #
        # The partition-function Rankin-Selberg gives a DIFFERENT object.
        # We compute sigma_{-1}(n) for the sewing comparison.
        total = mpf(0)
        for d in range(1, n + 1):
            if n % d == 0:
                total += mpf(1) / d
        coeffs[n] = total
    coeffs[0] = mpf(0)  # n=0 term is special
    return coeffs


# ============================================================================
# 10. Ising matrix L-function: full computation
# ============================================================================

def ising_matrix_L(s_val, num_terms=80, dps=DEFAULT_DPS):
    """Compute the 3x3 matrix L_{ij}(s) for Ising.

    Returns the matrix and metadata (weights, S-matrix, etc.).
    """
    _set_dps(dps)
    model = ising_model()
    L = matrix_L_fast(model, s_val, num_terms=num_terms, dps=dps)
    labels = model.primary_labels()
    weights = [model.conformal_weight_mpf(lab.r, lab.s) for lab in labels]
    S = s_matrix(model, dps=dps)
    return {
        'L': L,
        'weights': weights,
        'S': S,
        'labels': labels,
        's': s_val,
    }


# ============================================================================
# 11. Diagonal vs off-diagonal analysis
# ============================================================================

def diagonal_vs_offdiagonal(model, s_val, num_terms=80, dps=DEFAULT_DPS):
    """Separate diagonal and off-diagonal contributions to L_{ij}(s).

    Returns dict with 'diagonal' (list of L_{ii}), 'offdiagonal' (dict of L_{ij} for i<j),
    'trace', and 'offdiag_sum'.
    """
    _set_dps(dps)
    L = matrix_L_fast(model, s_val, num_terms=num_terms, dps=dps)
    n = L.rows
    diag = [L[i, i] for i in range(n)]
    offdiag = {}
    for i in range(n):
        for j in range(i + 1, n):
            offdiag[(i, j)] = L[i, j]
    tr = fsum(diag)
    offdiag_sum = fsum(offdiag.values())
    return {
        'diagonal': diag,
        'offdiagonal': offdiag,
        'trace': tr,
        'offdiag_sum': offdiag_sum,
        'L': L,
    }


# ============================================================================
# 12. Multiplicativity analysis for all matrix entries
# ============================================================================

def full_multiplicativity_analysis(model, N_max=50, dps=DEFAULT_DPS):
    """Test multiplicativity of c_{ij}(n) for all (i,j) pairs.

    For each (i,j), extract the Dirichlet coefficients and test
    whether c_{ij}(mn) = c_{ij}(m) * c_{ij}(n) for coprime m, n.

    Returns dict mapping (i,j) -> multiplicativity_score.
    """
    _set_dps(dps)
    labels = model.primary_labels()
    n_chars = len(labels)
    c = model.central_charge_mpf
    weights = [model.conformal_weight_mpf(lab.r, lab.s) for lab in labels]
    qseries_all = [
        character_qseries(model, lab.r, lab.s, num_terms=N_max + 10, dps=dps)
        for lab in labels
    ]

    scores = {}
    for i in range(n_chars):
        for j in range(n_chars):
            coeffs_raw = extract_dirichlet_coeffs(
                qseries_all[i], qseries_all[j],
                weights[i], weights[j], c,
                N_max=N_max, dps=dps
            )
            # Extract just the coefficient values
            coeffs = [c_val for _, c_val in coeffs_raw]
            score = multiplicativity_score(coeffs, min(N_max, 20))
            scores[(i, j)] = score
    return scores


# ============================================================================
# 13. S-matrix spectral decomposition of L
# ============================================================================

def s_matrix_spectral_decomposition(model, s_val, num_terms=80, dps=DEFAULT_DPS):
    """Attempt spectral decomposition: L_{ij}(s) = sum_k S_{ik} S_{jk} L_k(s).

    If the L-matrix factors through the S-matrix diagonalization, then
    L_k(s) = (S^{-1} L S^{-T})_{kk} are "principal" L-functions.

    Returns the principal L-values L_k(s) and whether the decomposition
    is diagonal (i.e., off-diagonal entries of S^{-1} L S^{-T} vanish).
    """
    _set_dps(dps)
    S = s_matrix(model, dps=dps)
    L = matrix_L_fast(model, s_val, num_terms=num_terms, dps=dps)
    n = L.rows

    # S is unitary (S^{-1} = S^dag = S^T for real S)
    S_inv = S.T  # since S is real unitary
    transformed = S_inv * L * S_inv.T

    principal_L = [transformed[k, k] for k in range(n)]
    off_diag_norm = mpf(0)
    for i in range(n):
        for j in range(n):
            if i != j:
                off_diag_norm += abs(transformed[i, j]) ** 2
    off_diag_norm = sqrt(off_diag_norm)

    is_diagonal = float(off_diag_norm) < 1e-6

    return {
        'principal_L': principal_L,
        'transformed_matrix': transformed,
        'off_diag_norm': off_diag_norm,
        'is_diagonal': is_diagonal,
    }


# ============================================================================
# 14. Ising weight structure
# ============================================================================

def ising_weight_differences():
    """Compute h_j - h_i for all pairs of Ising primaries.

    Ising primaries (in standard order): (1,1) h=0, (2,1) h=1/2, (1,2)=(3,1) h=1/16.
    Wait -- need to check the actual order from the model.
    """
    model = ising_model()
    labels = model.primary_labels()
    weights = [model.conformal_weight(lab.r, lab.s) for lab in labels]
    diffs = {}
    for i, w_i in enumerate(weights):
        for j, w_j in enumerate(weights):
            diffs[(i, j)] = w_j - w_i
    return weights, diffs, labels


def ising_vanishing_offdiag():
    """Determine which off-diagonal L_{ij} vanish due to non-integer weight differences.

    For Ising: h_0 = 0, h_{1/2} = 1/2, h_{1/16} = 1/16.
    Weight differences:
      h_{1/2} - h_0 = 1/2  (non-integer if 1/2 is not integer... but 1/2 IS half-integer)
      h_{1/16} - h_0 = 1/16 (non-integer)
      h_{1/16} - h_{1/2} = 1/16 - 1/2 = -7/16 (non-integer)

    So for Ising, ALL off-diagonal entries vanish!
    Only h_{1/2} - h_0 = 1/2 which is still non-integer.

    This means L_{ij}(s) is DIAGONAL for Ising -- the matrix is trivially decomposed!
    The scalar trace is just the sum of three independent diagonal L-functions.
    """
    weights, diffs, labels = ising_weight_differences()
    vanishing = {}
    for (i, j), d in diffs.items():
        if i == j:
            vanishing[(i, j)] = False  # diagonal, never vanishes
        else:
            # Vanishes iff d is not an integer
            vanishing[(i, j)] = (d.denominator != 1)
    return vanishing, weights, diffs


# ============================================================================
# 15. Non-diagonal RCFT example: tricritical Ising
# ============================================================================

def tricritical_ising_weight_analysis():
    """Analyze weight differences for tricritical Ising M(5,4).

    c = 7/10, 6 primaries with weights:
      h_{1,1} = 0, h_{2,1} = 7/16, h_{3,1} = 3/2, h_{1,2} = 3/80,
      h_{2,2} = 3/5, h_{3,2} = ... (need to compute)

    Some weight differences might be integers, giving non-trivial off-diagonal entries.
    """
    model = tricritical_ising_model()
    labels = model.primary_labels()
    weights = [model.conformal_weight(lab.r, lab.s) for lab in labels]

    integer_diffs = []
    for i in range(len(weights)):
        for j in range(i + 1, len(weights)):
            d = weights[j] - weights[i]
            if d.denominator == 1:
                integer_diffs.append((i, j, d))

    return {
        'labels': labels,
        'weights': weights,
        'integer_diffs': integer_diffs,
        'num_primaries': len(labels),
    }


# ============================================================================
# 16. Conductor and gamma factors
# ============================================================================

def rankin_selberg_gamma_factor(s_val, h_i, h_j, dps=DEFAULT_DPS):
    """Gamma factor for the (i,j) Rankin-Selberg integral.

    The standard Rankin-Selberg gamma factor is:
        Gamma_RS(s) = pi^{-s} Gamma(s/2) Gamma((s + |h_i - h_j|)/2)

    For h_i = h_j (diagonal):
        Gamma_RS(s) = pi^{-s} Gamma(s/2)^2

    The conductor N is related to the level of the modular representation.
    For minimal model M(p,q): N = lcm(4pq, ...) (depends on the model).
    """
    _set_dps(dps)
    s = mpf(s_val)
    mu = abs(h_i - h_j)

    gamma_fac = power(pi, -s) * mpgamma(s / 2) * mpgamma((s + mu) / 2)
    return gamma_fac


# ============================================================================
# Summary / display
# ============================================================================

def print_ising_matrix_L(s_values=None, num_terms=80, dps=DEFAULT_DPS):
    """Print the Ising 3x3 matrix L_{ij}(s) for several s values."""
    if s_values is None:
        s_values = [2, 3, 4]

    _set_dps(dps)
    model = ising_model()
    labels = model.primary_labels()
    weights = [model.conformal_weight(lab.r, lab.s) for lab in labels]

    print("Ising Model M(4,3): c = 1/2")
    print(f"Primaries: {[(lab.r, lab.s) for lab in labels]}")
    print(f"Weights: {weights}")
    print()

    # Check vanishing structure
    vanishing, _, _ = ising_vanishing_offdiag()
    print("Off-diagonal vanishing (non-integer weight diff):")
    for (i, j), v in vanishing.items():
        if i < j:
            print(f"  L_{{{i},{j}}}(s): {'VANISHES' if v else 'non-vanishing'}")
    print()

    for s_val in s_values:
        L = matrix_L_fast(model, s_val, num_terms=num_terms, dps=dps)
        print(f"L(s={s_val}):")
        for i in range(L.rows):
            row = [nstr(L[i, j], 8) for j in range(L.cols)]
            print(f"  [{', '.join(row)}]")
        print(f"  tr(L) = {nstr(trace_L(L), 10)}")
        print(f"  det(L) = {nstr(det_L(L), 10)}")
        print()


def print_multiplicativity_analysis(model=None, N_max=30, dps=DEFAULT_DPS):
    """Print multiplicativity scores for all matrix entries."""
    if model is None:
        model = ising_model()
    scores = full_multiplicativity_analysis(model, N_max=N_max, dps=dps)
    labels = model.primary_labels()
    n = len(labels)
    print(f"Multiplicativity scores (1.0 = perfectly multiplicative):")
    for i in range(n):
        for j in range(n):
            print(f"  c_{{{i},{j}}}(n): score = {scores[(i,j)]:.4f}")


if __name__ == "__main__":
    print_ising_matrix_L()
    print()
    print_multiplicativity_analysis()
