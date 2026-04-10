r"""Verlinde algebra, fusion rules, and modular tensor category data
from the shadow obstruction tower.

The Verlinde algebra V_k(g) encodes the fusion ring of integrable
representations of the affine Lie algebra g-hat at level k.  Its
structure constants N_{ij}^m (fusion coefficients) are computed from
the modular S-matrix via the Verlinde formula:

    N_{ij}^m = sum_l S_{il} S_{jl} conj(S_{ml}) / S_{0l}

The S-matrix simultaneously encodes:
  (1) Modular transformation of characters: chi_j(-1/tau) = sum_l S_{jl} chi_l(tau)
  (2) Quantum dimensions: d_j = S_{0j}/S_{00}
  (3) Genus-g Verlinde dimension: Z_g = sum_j S_{0j}^{2-2g}
  (4) Connection to the shadow obstruction tower: the genus-1 partition function
      Z_1(g_k) = k+1 (for sl_2) is the number of integrable reps

SHADOW TOWER CONNECTION:

The modular S-matrix controls the genus-1 modular transformation
S: tau -> -1/tau of the shadow partition function.  The T-matrix
T_{jl} = delta_{jl} * exp(2*pi*i*(h_j - c/24)) encodes the genus-1
twist (tau -> tau + 1).  Together (S, T) generate SL(2,Z) and
constitute the genus-1 shadow data.

At the level of the shadow obstruction tower:
  - kappa(g_k) = dim(g)*(k+h^v)/(2*h^v) is the arity-2 shadow
  - The S-matrix eigenvalues d_j = S_{0j}/S_{00} are quantum dimensions
  - The total quantum dimension D^2 = sum d_j^2 = 1/S_{00}^2
  - The Verlinde formula N_{ij}^m = shadow fusion coefficients
  - The genus-g Verlinde dimension Z_g = sum_j S_{0j}^{2-2g}

MTC (MODULAR TENSOR CATEGORY) DATA:

For sl_2 at level k, the MTC has:
  - Objects: integrable representations V_0, V_1, ..., V_k
  - Braiding: c_{V_j, V_l} from the R-matrix
  - Twist: theta_j = exp(2*pi*i * j(j+2)/(4(k+2)))
  - S-matrix: S_{jl} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))
  - Fusion: N_{ij}^m from Verlinde formula
  - Reshetikhin-Turaev invariants from MTC data

HIGHER RANK:

For sl_N at level k, integrable representations are labeled by
Dynkin labels (a_1, ..., a_{N-1}) with sum a_i <= k.
The Weyl-Kac S-matrix formula uses the Weyl alternation sum
with the inner product projected to the traceless hyperplane
of the epsilon coordinate space.

VERLINDE RING STRUCTURE:

For sl_2 at level k, the Verlinde ring has basis {[V_0], ..., [V_k]}
with fusion multiplication [V_i] * [V_j] = sum_m N_{ij}^m [V_m].
The fundamental representation V_1 generates the ring with the
recursion V_1 * V_j = V_{j-1} + V_{j+1} (for 0 < j < k) and
the truncation V_1 * V_k = V_{k-1}.  This means [V_1]^{k+1} = 0
in the Verlinde ring.

CONVENTIONS:
  - Representations labeled j = 0, 1, ..., k (= twice the spin) for sl_2
  - S_{00} > 0 (positive normalization)
  - Quantum dimensions d_j > 0 for all integrable j
  - Genus-g Verlinde formula: Z_g = sum_j S_{0j}^{2-2g}
  - sl_2 S-matrix: S_{jl} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))

Mathematical references:
  Verlinde (1988), Nuclear Phys. B 300, 115--138
  Kac-Peterson (1984), Adv. Math. 53, 125--264
  Bakalov-Kirillov (2001), Lectures on tensor categories and modular functors
  Turaev (2010), Quantum invariants of knots and 3-manifolds
  thm:modular-characteristic (higher_genus_modular_koszul.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

from fractions import Fraction
import math
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from sympy import (
    Matrix,
    Rational,
    Symbol,
    bernoulli as sympy_bernoulli,
    pi,
    simplify,
    sin,
    sqrt,
    sympify,
    S as sympy_S,
)


# =========================================================================
# 1. Modular S-matrix for sl_2
# =========================================================================

def sl2_S_matrix(k: int) -> np.ndarray:
    r"""Modular S-matrix for sl_2 at positive integer level k.

    S_{jl} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))

    for j, l in {0, 1, ..., k}.  Here j labels integrable highest
    weight representations of sl_2-hat at level k: the representation
    with highest weight j*Lambda_1 + (k-j)*Lambda_0, having spin j/2.

    Properties (verified in tests):
      (i)   S is symmetric: S = S^T
      (ii)  S is unitary: S * S^T = I (S is real for sl_2)
      (iii) S^2 = I (identity): this S-matrix is real symmetric orthogonal

    Args:
        k: positive integer level

    Returns:
        (k+1) x (k+1) numpy array with S-matrix entries
    """
    if k < 1:
        raise ValueError(f"Level must be positive, got k={k}")
    n = k + 2
    size = k + 1
    S = np.zeros((size, size))
    prefactor = math.sqrt(2.0 / n)
    for j in range(size):
        for l in range(size):
            S[j, l] = prefactor * math.sin(math.pi * (j + 1) * (l + 1) / n)
    return S


def sl2_S_matrix_exact(k: int) -> Matrix:
    r"""Exact (symbolic) S-matrix for sl_2 at level k.

    Uses sympy for exact trigonometric values.
    """
    if k < 1:
        raise ValueError(f"Level must be positive, got k={k}")
    n = k + 2
    size = k + 1
    prefactor = sqrt(Rational(2, n))
    rows = []
    for j in range(size):
        row = []
        for l in range(size):
            entry = prefactor * sin(pi * (j + 1) * (l + 1) / n)
            row.append(entry)
        rows.append(row)
    return Matrix(rows)


def sl2_T_matrix(k: int) -> np.ndarray:
    r"""Modular T-matrix for sl_2 at level k.

    T_{jl} = delta_{jl} * exp(2*pi*i*(h_j - c/24))

    where h_j = j(j+2)/(4(k+2)) is the conformal weight of V_j
    and c = 3k/(k+2) is the central charge.

    Returns complex (k+1) x (k+1) diagonal matrix.
    """
    if k < 1:
        raise ValueError(f"Level must be positive, got k={k}")
    n = k + 2
    size = k + 1
    c_over_24 = k / (8.0 * n)  # c/24 = 3k/(k+2) / 24 = k/(8(k+2))
    T = np.zeros((size, size), dtype=complex)
    for j in range(size):
        h_j = j * (j + 2) / (4.0 * n)
        phase = 2.0 * math.pi * (h_j - c_over_24)
        T[j, j] = complex(math.cos(phase), math.sin(phase))
    return T


def sl2_charge_conjugation(k: int) -> np.ndarray:
    r"""Charge conjugation matrix C for sl_2 at level k.

    C_{jl} = delta_{j, k-l}

    For sl_2, charge conjugation sends j -> k - j.
    Property: S^2 = I (the sl_2 S-matrix is real symmetric orthogonal).
    """
    size = k + 1
    C = np.zeros((size, size))
    for j in range(size):
        C[j, k - j] = 1.0
    return C


# =========================================================================
# 2. Verlinde formula: fusion coefficients
# =========================================================================

def sl2_fusion_coefficients(k: int) -> np.ndarray:
    r"""All fusion coefficients N_{ij}^m for sl_2 at level k.

    Verlinde formula:
        N_{ij}^m = sum_{l=0}^{k} S_{il} S_{jl} S_{ml} / S_{0l}

    Since S is real, symmetric, and unitary for sl_2: S^{-1} = S^T = S,
    so conj(S_{ml}) = S_{ml}.  The formula simplifies to the triple-S
    product divided by S_{0l}.

    Returns:
        (k+1) x (k+1) x (k+1) array where result[i,j,m] = N_{ij}^m
    """
    if k < 1:
        raise ValueError(f"Level must be positive, got k={k}")
    S = sl2_S_matrix(k)
    size = k + 1
    N = np.zeros((size, size, size))
    for i in range(size):
        for j in range(size):
            for m in range(size):
                total = 0.0
                for l in range(size):
                    if abs(S[0, l]) > 1e-15:
                        total += S[i, l] * S[j, l] * S[m, l] / S[0, l]
                N[i, j, m] = total
    return N


def sl2_fusion_rules_explicit(k: int) -> Dict[Tuple[int, int, int], int]:
    r"""Explicit nonzero fusion rules for sl_2 at level k.

    For sl_2 at level k, the fusion rules are known exactly:
        N_{ij}^m = 1 if |i-j| <= m <= min(i+j, 2k-i-j) and i+j+m even
        N_{ij}^m = 0 otherwise

    This is the truncated Clebsch-Gordan rule.

    Returns dict mapping (i, j, m) -> N_{ij}^m for nonzero entries.
    """
    size = k + 1
    rules = {}
    for i in range(size):
        for j in range(size):
            for m in range(size):
                if (abs(i - j) <= m <= min(i + j, 2 * k - i - j)
                        and (i + j + m) % 2 == 0):
                    rules[(i, j, m)] = 1
    return rules


# =========================================================================
# 3. Quantum dimensions and total quantum dimension
# =========================================================================

def sl2_quantum_dimensions(k: int) -> np.ndarray:
    r"""Quantum dimensions for sl_2 at level k.

    d_j = S_{0j} / S_{00} = sin(pi*(j+1)/(k+2)) / sin(pi/(k+2))

    These are the quantum dimensions of the integrable representations.
    They satisfy:
      d_0 = 1 (vacuum has quantum dimension 1)
      d_j = d_{k-j} (charge conjugation symmetry)
      d_j > 0 for all j = 0, ..., k
      sum d_j^2 = D^2 = 1/S_{00}^2

    Returns array of length k+1.
    """
    if k < 1:
        raise ValueError(f"Level must be positive, got k={k}")
    S = sl2_S_matrix(k)
    s00 = S[0, 0]
    return S[0, :] / s00


def sl2_quantum_dimension_formula(j: int, k: int) -> float:
    r"""Quantum dimension of V_j for sl_2 at level k.

    d_j = sin((j+1)*pi/(k+2)) / sin(pi/(k+2))

    This is the q-number [j+1]_q where q = exp(i*pi/(k+2)).
    """
    n = k + 2
    return math.sin((j + 1) * math.pi / n) / math.sin(math.pi / n)


def sl2_total_quantum_dimension_sq(k: int) -> float:
    r"""Total quantum dimension squared D^2 for sl_2 at level k.

    D^2 = sum_{j=0}^{k} d_j^2 = 1/S_{00}^2

    This is a fundamental invariant of the MTC.
    """
    dims = sl2_quantum_dimensions(k)
    return float(np.sum(dims ** 2))


def sl2_total_quantum_dimension_sq_formula(k: int) -> float:
    r"""D^2 from the closed-form formula: 1/S_{00}^2.

    D^2 = 1 / S_{00}^2 = (k+2) / (2 * sin^2(pi/(k+2)))
    """
    n = k + 2
    return n / (2.0 * math.sin(math.pi / n) ** 2)


# =========================================================================
# 4. Shadow obstruction tower connection: genus-1 data
# =========================================================================

def sl2_conformal_weights(k: int) -> np.ndarray:
    r"""Conformal weights h_j for sl_2 at level k.

    h_j = j(j+2) / (4(k+2))

    for j = 0, 1, ..., k.  The vacuum has h_0 = 0.
    """
    n = k + 2
    return np.array([j * (j + 2) / (4.0 * n) for j in range(k + 1)])


def sl2_central_charge(k: int) -> float:
    r"""Central charge for sl_2-hat at level k.

    c = 3k/(k+2)

    Limits: c -> 0 as k -> 0+, c -> 3 as k -> infinity.
    """
    return 3.0 * k / (k + 2)


def sl2_kappa(k: int) -> float:
    r"""Modular characteristic kappa for sl_2-hat at level k.

    kappa(sl_2, k) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4

    where dim(sl_2) = 3, h^v = 2.
    """
    return 3.0 * (k + 2) / 4.0


def shadow_S_T_from_genus1(k: int) -> Dict[str, Any]:
    r"""Extract S, T matrices from genus-1 shadow transformation properties.

    At genus 1, the shadow partition function transforms under SL(2,Z):
      tau -> -1/tau : Z_1 -> S * Z_1
      tau -> tau + 1 : Z_1 -> T * Z_1

    This function constructs S, T from the fundamental data (conformal
    weights, central charge) and verifies consistency with the explicit
    S-matrix formula.

    Returns dict with S, T matrices and consistency checks.
    """
    S = sl2_S_matrix(k)
    T = sl2_T_matrix(k)
    h = sl2_conformal_weights(k)
    c = sl2_central_charge(k)

    # Verify T diagonal entries match exp(2*pi*i*(h_j - c/24))
    T_expected = np.zeros((k + 1, k + 1), dtype=complex)
    for j in range(k + 1):
        phase = 2.0 * math.pi * (h[j] - c / 24.0)
        T_expected[j, j] = complex(math.cos(phase), math.sin(phase))

    t_match = np.allclose(T, T_expected, atol=1e-12)

    # SL(2,Z) relation: for real symmetric unitary S (S^2 = I),
    # the relation (ST)^3 = e^{-i*pi*c/4} * S^2 = e^{-i*pi*c/4} * I
    # holds.  We check that (ST)^3 is proportional to the identity.
    ST = S @ T
    ST3 = ST @ ST @ ST
    st3_abs = np.abs(ST3)
    sl2z_relation = np.allclose(st3_abs, np.eye(k + 1), atol=1e-10)

    return {
        "S": S,
        "T": T,
        "conformal_weights": h,
        "central_charge": c,
        "T_consistency": t_match,
        "SL2Z_relation_abs": sl2z_relation,
    }


# =========================================================================
# 5. MTC data for sl_2
# =========================================================================

def sl2_twist(k: int) -> np.ndarray:
    r"""Twist (ribbon element) for sl_2 at level k.

    theta_j = exp(2*pi*i * h_j)

    where h_j = j(j+2)/(4(k+2)) is the conformal weight.
    """
    h = sl2_conformal_weights(k)
    return np.exp(2.0j * math.pi * h)


def sl2_braiding_eigenvalues(j1: int, j2: int, k: int) -> Tuple[np.ndarray, List[int]]:
    r"""Braiding eigenvalues for V_{j1} x V_{j2} in sl_2 at level k.

    The braiding c_{j1,j2}: V_{j1} tensor V_{j2} -> V_{j2} tensor V_{j1}
    acts on the fusion channel V_m with eigenvalue:

        exp(i*pi*(h_m - h_{j1} - h_{j2}))

    where h_j = j(j+2)/(4(k+2)) is the conformal weight.

    Returns (eigenvalues_array, channels_list).
    """
    n = k + 2
    channels = []
    eigenvalues = []
    for m in range(k + 1):
        if (abs(j1 - j2) <= m <= min(j1 + j2, 2 * k - j1 - j2)
                and (j1 + j2 + m) % 2 == 0):
            h_m = m * (m + 2) / (4.0 * n)
            h_j1 = j1 * (j1 + 2) / (4.0 * n)
            h_j2 = j2 * (j2 + 2) / (4.0 * n)
            eig = np.exp(1.0j * math.pi * (h_m - h_j1 - h_j2))
            channels.append(m)
            eigenvalues.append(eig)
    return np.array(eigenvalues), channels


def sl2_RT_trefoil(k: int) -> complex:
    r"""Reshetikhin-Turaev invariant of the trefoil for sl_2 at level k.

    The trefoil is the (2,3) torus knot with writhe 3.
    In the fundamental representation (j=1):

        <trefoil>_{V_1} = sum_m (S_{1,m}/S_{0,m}) * theta_m^3

    where theta_m = exp(2*pi*i*h_m) is the twist.

    This is the unnormalized RT invariant.  Dividing by the unknot
    value d_1 gives the normalized (quantum) Jones polynomial.
    """
    if k < 1:
        return 0.0j

    S_mat = sl2_S_matrix(k)
    h = sl2_conformal_weights(k)
    theta = np.exp(2.0j * math.pi * h)

    j = 1  # fundamental
    result = 0.0j
    for m in range(k + 1):
        if abs(S_mat[0, m]) > 1e-15:
            result += (S_mat[j, m] / S_mat[0, m]) * theta[m] ** 3
    return result


def sl2_RT_unknot(k: int, j: int = 1) -> complex:
    r"""RT invariant of the unknot (zero framing) for sl_2 at level k.

    <unknot>_j = d_j = S_{0j}/S_{00} = quantum dimension.
    """
    S_mat = sl2_S_matrix(k)
    return S_mat[0, j] / S_mat[0, 0]


# =========================================================================
# 6. Higher rank: sl_3
# =========================================================================

def sl3_integrable_weights(k: int) -> List[Tuple[int, int]]:
    r"""Integrable highest weights for sl_3-hat at level k.

    An integrable weight at level k is (a1, a2) with a1, a2 >= 0
    and a1 + a2 <= k.  The number of such weights is C(k+2, 2).

    Returns list of (a1, a2) pairs, ordered lexicographically.
    """
    weights = []
    for a1 in range(k + 1):
        for a2 in range(k + 1 - a1):
            weights.append((a1, a2))
    return weights


def sl3_S_matrix(k: int) -> np.ndarray:
    r"""Modular S-matrix for sl_3 at positive integer level k.

    Uses the Weyl-Kac-Peterson formula:

    S_{lambda,mu} = C * sum_{w in S_3} sgn(w) *
        exp(-2*pi*i * <w(lambda+rho), mu+rho>_0 / (k+3))

    where <v, w>_0 denotes the inner product on the TRACELESS
    hyperplane of the epsilon coordinate space:
        <v, w>_0 = sum v_i * w_i - (1/N) * (sum v_i) * (sum w_i)

    The normalization C is determined by the unitarity condition
    S * S^dagger = I, with the convention S_{00} > 0.

    Returns complex (num_weights x num_weights) array.
    """
    N = 3
    n = k + N
    weights = sl3_integrable_weights(k)
    num_weights = len(weights)

    def shifted_eps(a1, a2):
        return np.array([a1 + a2 + 2, a2 + 1, 0], dtype=float)

    def inner_traceless(v, w):
        v_proj = v - np.mean(v)
        w_proj = w - np.mean(w)
        return np.dot(v_proj, w_proj)

    perms = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 0, 1), (1, 2, 0), (2, 1, 0)]
    signs = [1, -1, -1, 1, 1, -1]

    S_raw = np.zeros((num_weights, num_weights), dtype=complex)
    for i, (a1_i, a2_i) in enumerate(weights):
        p = shifted_eps(a1_i, a2_i)
        for j, (a1_j, a2_j) in enumerate(weights):
            q = shifted_eps(a1_j, a2_j)
            val = 0.0j
            for perm, sgn in zip(perms, signs):
                wp = p[list(perm)]
                ip = inner_traceless(wp, q)
                val += sgn * np.exp(-2.0j * math.pi * ip / n)
            S_raw[i, j] = val

    # Normalize: S * S^dag = I
    SSd = S_raw @ np.conj(S_raw.T)
    c = math.sqrt(np.diag(SSd).real[0])
    S_mat = S_raw / c

    # Fix phase: make S_{00} real and positive
    phase = S_mat[0, 0] / abs(S_mat[0, 0])
    S_mat = S_mat / phase

    return S_mat


def sl3_quantum_dimensions(k: int) -> np.ndarray:
    r"""Quantum dimensions for sl_3 at level k.

    d_lambda = S_{0,lambda} / S_{0,0}

    Alternatively, from the Weyl dimension formula at q = exp(2*pi*i/(k+3)):
    d_{(a1,a2)} = prod_{alpha>0} sin(pi*<lambda+rho, alpha>/(k+3))
                 / sin(pi*<rho, alpha>/(k+3))

    Returns array of quantum dimensions (real, positive).
    """
    n = k + 3

    def shifted_eps(a1, a2):
        return np.array([a1 + a2 + 2, a2 + 1, 0], dtype=float)

    rho = shifted_eps(0, 0)  # = [2, 1, 0]
    positive_root_pairs = [(0, 1), (0, 2), (1, 2)]

    weights = sl3_integrable_weights(k)
    dims = np.zeros(len(weights))

    for idx, (a1, a2) in enumerate(weights):
        lam_rho = shifted_eps(a1, a2)
        d = 1.0
        for (i, j) in positive_root_pairs:
            num_val = math.sin(math.pi * (lam_rho[i] - lam_rho[j]) / n)
            den_val = math.sin(math.pi * (rho[i] - rho[j]) / n)
            d *= num_val / den_val
        dims[idx] = d

    return dims


def sl3_fusion_coefficients(k: int) -> np.ndarray:
    r"""Fusion coefficients for sl_3 at level k via Verlinde formula.

    N_{ij}^m = sum_l S_{il} S_{jl} conj(S_{ml}) / S_{0l}

    Returns 3D array indexed by weight list positions.
    """
    S_mat = sl3_S_matrix(k)
    num = S_mat.shape[0]
    N = np.zeros((num, num, num))

    for i in range(num):
        for j in range(num):
            for m in range(num):
                total = 0.0j
                for l in range(num):
                    s0l = S_mat[0, l]
                    if abs(s0l) > 1e-15:
                        total += S_mat[i, l] * S_mat[j, l] * np.conj(S_mat[m, l]) / s0l
                N[i, j, m] = total.real

    return N


# =========================================================================
# 7. Verlinde ring structure
# =========================================================================

def sl2_verlinde_ring_multiplication(k: int) -> np.ndarray:
    r"""Multiplication table for the Verlinde ring V_k(sl_2).

    As a Z-module, V_k has basis {[V_0], ..., [V_k]} with
    multiplication [V_i] * [V_j] = sum_m N_{ij}^m [V_m].
    """
    return sl2_fusion_coefficients(k)


def sl2_generator_powers(k: int) -> List[np.ndarray]:
    r"""Powers of the generator [V_1] in V_k(sl_2).

    In V_k(sl_2), the fundamental representation V_1 generates the ring.
    Compute [V_1]^n for n = 0, 1, ..., k+1 to verify the ring relation
    [V_1]^{k+1} = 0.

    Returns list of coefficient vectors in the basis {[V_0], ..., [V_k]}.
    """
    N = sl2_fusion_coefficients(k)
    size = k + 1

    powers = []

    # [V_1]^0 = [V_0]
    p0 = np.zeros(size)
    p0[0] = 1.0
    powers.append(p0)

    if k < 1:
        return powers

    # [V_1]^1 = [V_1]
    p1 = np.zeros(size)
    p1[1] = 1.0
    powers.append(p1)

    # [V_1]^n = [V_1] * [V_1]^{n-1}
    for n in range(2, k + 2):
        prev = powers[n - 1]
        new = np.zeros(size)
        for j in range(size):
            if abs(prev[j]) > 1e-15:
                for m in range(size):
                    new[m] += prev[j] * N[1, j, m]
        powers.append(new)

    return powers


def sl2_verlinde_ring_relation(k: int) -> Dict[str, Any]:
    r"""Verify the ring relation for V_k(sl_2).

    The fundamental representation V_1 satisfies:
    V_1 * V_j = V_{j-1} + V_{j+1} (for 0 < j < k),
    V_1 * V_0 = V_1, V_1 * V_k = V_{k-1} (truncation).

    This is the Chebyshev recursion: identifying V_j = U_j(V_1/2)
    where U_j is the j-th Chebyshev polynomial of the second kind,
    the ring relation is U_{k+1}(V_1/2) = 0.

    Equivalently: V_{k+1} = 0 in the Verlinde ring, where V_{k+1}
    would be the next element in the Chebyshev recursion
    V_{k+1} = V_1 * V_k - V_{k-1}.

    NOTE: This is NOT the same as [V_1]^{k+1} = 0 (which is false
    in general).  The Chebyshev polynomial U_{k+1}(x/2) is of degree
    k+1 in x = V_1, but with lower-order terms.
    """
    powers = sl2_generator_powers(k)
    size = k + 1
    N = sl2_fusion_coefficients(k)

    # Check Chebyshev recursion: V_1 * V_j = V_{j-1} + V_{j+1} for 0 < j < k
    recursion_holds = True
    for j in range(1, k):
        expected = np.zeros(size)
        expected[j - 1] = 1.0
        expected[j + 1] = 1.0
        actual = N[1, j, :]
        if not np.allclose(actual, expected, atol=1e-10):
            recursion_holds = False
            break

    # Check truncation: V_1 * V_k = V_{k-1} (i.e., V_{k+1} = 0)
    if k >= 1:
        expected_k = np.zeros(size)
        expected_k[k - 1] = 1.0
        truncation_holds = np.allclose(N[1, k, :], expected_k, atol=1e-10)
    else:
        truncation_holds = True

    # Check vacuum identity: V_0 * V_j = V_j
    vacuum_identity = True
    for j in range(size):
        expected_vac = np.zeros(size)
        expected_vac[j] = 1.0
        if not np.allclose(N[0, j, :], expected_vac, atol=1e-10):
            vacuum_identity = False
            break

    return {
        "k": k,
        "generator_powers": powers,
        "chebyshev_recursion_holds": recursion_holds,
        "truncation_holds": truncation_holds,
        "vacuum_identity_holds": vacuum_identity,
    }


# =========================================================================
# 8. Genus-g Verlinde dimensions
# =========================================================================

def sl2_verlinde_genus_g(k: int, g: int) -> float:
    r"""Verlinde dimension at genus g for sl_2 at level k.

    Z_g = sum_{j=0}^{k} S_{0j}^{2-2g}

    This is always a positive integer for g >= 0.

    For g=0: Z_0 = sum S_{0j}^2 = 1 (by unitarity of S)
    For g=1: Z_1 = k+1 (number of integrable reps)
    For g>=2: Z_g = sum S_{0j}^{2-2g} (grows polynomially in k)
    """
    if g < 0:
        raise ValueError(f"Genus must be non-negative, got g={g}")
    S_mat = sl2_S_matrix(k)
    total = 0.0
    for j in range(k + 1):
        s0j = S_mat[0, j]
        if abs(s0j) > 1e-15:
            total += s0j ** (2 - 2 * g)
    return total


def sl2_verlinde_genus_g_exact(k: int, g: int) -> int:
    r"""Exact integer Verlinde dimension at genus g for sl_2 at level k.

    The Verlinde formula always gives a non-negative integer.
    """
    return round(sl2_verlinde_genus_g(k, g))


def sl2_verlinde_genus_g_formula(k: int, g: int) -> float:
    r"""Alternative genus-g formula via quantum dimensions.

    Z_g = (S_{00})^{2-2g} * sum_j d_j^{2-2g}

    where d_j = S_{0j}/S_{00}.  This is equivalent to the direct formula.
    """
    S_mat = sl2_S_matrix(k)
    s00 = S_mat[0, 0]
    dims = sl2_quantum_dimensions(k)
    return s00 ** (2 - 2 * g) * sum(d ** (2 - 2 * g) for d in dims)


def sl2_shadow_F_g(k: int, g: int) -> Fraction:
    r"""Shadow partition function F_g for sl_2-hat at level k.

    At genus g >= 1, the shadow (obstruction) from the arity-2 component:
        F_g = kappa * lambda_g^{FP}

    where kappa = 3(k+2)/4 and
        lambda_g^{FP} = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!).

    For g=1: F_1 = kappa/24 (since lambda_1 = 1/24 on M_bar_{1,1}).

    NOTE: This is NOT the same as the Verlinde dimension.
    The Verlinde dimension counts conformal blocks.
    F_g is the shadow obstruction class integrated over M_bar_g.
    """
    if g < 1:
        raise ValueError(f"F_g defined for g >= 1, got g={g}")

    kappa = Fraction(3 * (k + 2), 4)

    if g == 1:
        return kappa * Fraction(1, 24)

    B2g = sympy_bernoulli(2 * g)
    bernoulli_abs = Fraction(abs(int(B2g.p)), int(B2g.q))
    two_power = 2 ** (2 * g - 1)
    lambda_g_fp = (
        Fraction(two_power - 1, two_power)
        * bernoulli_abs
        / math.factorial(2 * g)
    )
    if g == 2:
        lambda_2_fp = lambda_g_fp
        assert lambda_2_fp == Fraction(7, 5760)
    return kappa * lambda_g_fp


# =========================================================================
# 9. Known exact values and cross-checks
# =========================================================================

# Exact Verlinde dimensions for sl_2 at small k and g
# Computed from Z_g = sum_{j=0}^{k} S_{0j}^{2-2g}
SL2_VERLINDE_TABLE = {
    # (k, g): Z_g
    (1, 0): 1,
    (1, 1): 2,
    (1, 2): 4,
    (1, 3): 8,
    (1, 4): 16,
    (2, 0): 1,
    (2, 1): 3,
    (2, 2): 10,
    (2, 3): 36,
    (2, 4): 136,
    (3, 0): 1,
    (3, 1): 4,
    (3, 2): 20,
    (3, 3): 120,
    (3, 4): 800,
    (4, 0): 1,
    (4, 1): 5,
    (4, 2): 35,
    (4, 3): 329,
    (4, 4): 3611,
    (5, 0): 1,
    (5, 1): 6,
    (5, 2): 56,
    (5, 3): 784,
    (5, 4): 13328,
}


def verify_verlinde_table() -> Dict[Tuple[int, int], bool]:
    r"""Verify computed Verlinde dimensions against known values."""
    results = {}
    for (k, g), expected in SL2_VERLINDE_TABLE.items():
        computed = sl2_verlinde_genus_g_exact(k, g)
        results[(k, g)] = (computed == expected)
    return results
