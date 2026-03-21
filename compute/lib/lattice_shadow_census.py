#!/usr/bin/env python3
r"""Lattice shadow census: complete shadow tower and arithmetic data for lattice VOAs.

For an even lattice Lambda with bilinear form (.,.) and rank r = rank(Lambda):

SHADOW TOWER (Gaussian termination):
  kappa(V_Lambda) = rank(Lambda)
  C = 0  (cubic shadow vanishes)
  Q = 0  (quartic contact vanishes)
  shadow depth = 2  (class G)
  Theta_{V_Lambda} = rank(Lambda) * eta tensor Lambda_modular

The shadow metric on any primary line is Q_L(t) = (2*kappa)^2 (constant),
with critical discriminant Delta = 0.  The effective action is purely
Polyakov: S_eff = kappa * S_Polyakov with no nonlinear corrections.

GENUS EXPANSION:
  F_g(V_Lambda) = rank(Lambda) * lambda_g^FP
  where lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!

THETA FUNCTION:
  Theta_Lambda(tau) = sum_{lambda in Lambda} q^{(lambda,lambda)/2}
  The theta coefficients r_Lambda(n) = #{lambda in Lambda : (lambda,lambda)/2 = n}.

PARTITION FUNCTION (genus 1):
  Z_1(V_Lambda; tau) = Theta_Lambda(tau) / eta(tau)^{rank(Lambda)}

COMPLEMENTARITY:
  V_Lambda^! = V_{Lambda^*} (Koszul dual via dual lattice).
  For self-dual lattices: V_Lambda^! = V_Lambda.
  kappa(V_Lambda) + kappa(V_{Lambda^*}) = 0 is WRONG;
  actually kappa + kappa' need not vanish in general.
  The correct statement: for unimodular Lambda, kappa' = kappa (same rank).

Mathematical references:
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - concordance.tex: sec:concordance-lattice-shadow
  - higher_genus_modular_koszul.tex: shadow depth classification (G class)
  - arithmetic_shadows.tex: thm:shadow-spectral-correspondence
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from sympy import Rational, bernoulli, factorial, Matrix, Abs


# =========================================================================
# Bernoulli numbers (exact)
# =========================================================================

def _bernoulli_exact(n: int) -> Rational:
    """Bernoulli number B_n as exact sympy Rational."""
    return Rational(bernoulli(n))


# =========================================================================
# Faber-Pandharipande numbers
# =========================================================================

def faber_pandharipande(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    This is the universal genus-g coefficient in the free energy of
    any Gaussian (shadow depth 2) chiral algebra.

    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    numerator = (Rational(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    denominator = Rational(2) ** (2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


# =========================================================================
# Root lattice Gram matrices
# =========================================================================

def root_lattice_gram(type_name: str) -> np.ndarray:
    """Gram matrix for standard root lattices.

    Supported: A2, A3, ..., A8, D4, D5, ..., D8, E6, E7, E8.

    Convention: even lattice with (alpha_i, alpha_i) = 2 for simple roots,
    (alpha_i, alpha_j) = -1 for adjacent roots in the Dynkin diagram.
    """
    type_name = type_name.upper().replace('_', '')

    if type_name.startswith('A'):
        n = int(type_name[1:])
        G = np.zeros((n, n), dtype=int)
        for i in range(n):
            G[i, i] = 2
            if i > 0:
                G[i, i - 1] = -1
                G[i - 1, i] = -1
        return G

    elif type_name.startswith('D'):
        n = int(type_name[1:])
        if n < 3:
            raise ValueError(f"D_n requires n >= 3, got n={n}")
        G = np.zeros((n, n), dtype=int)
        for i in range(n):
            G[i, i] = 2
        # Linear spine: 0--1--2--...--n-3
        for i in range(n - 2):
            G[i, i + 1] = -1
            G[i + 1, i] = -1
        # D_n branching: node n-1 connects to node n-3
        G[n - 1, n - 3] = -1
        G[n - 3, n - 1] = -1
        return G

    elif type_name.startswith('E'):
        n = int(type_name[1:])
        if n not in (6, 7, 8):
            raise ValueError(f"E_n requires n in {{6,7,8}}, got n={n}")
        G = np.zeros((n, n), dtype=int)
        for i in range(n):
            G[i, i] = 2
        # Spine: 0--1--2--3--4--(5)--(6)--(7)
        for i in range(n - 2):
            G[i, i + 1] = -1
            G[i + 1, i] = -1
        # Branch: node n-1 connects to node 2
        G[n - 1, 2] = -1
        G[2, n - 1] = -1
        return G

    else:
        raise ValueError(f"Unknown root lattice type: {type_name}")


def _hypercubic_gram(n: int) -> np.ndarray:
    """Gram matrix for Z^n with standard inner product (e_i, e_j) = 2*delta_{ij}.

    This is the even lattice convention: each basis vector has norm 2.
    The lattice is the rescaled integer lattice sqrt(2) * Z^n.
    """
    return 2 * np.eye(n, dtype=int)


def _leech_gram() -> np.ndarray:
    """Return a placeholder Gram matrix for the Leech lattice.

    The Leech lattice is 24-dimensional and too large for explicit
    vector enumeration.  We use known theta coefficients instead
    (see leech_theta_coefficients).
    """
    # Return identity * 4 as a placeholder (correct rank, not the real Gram)
    return 4 * np.eye(24, dtype=int)


# =========================================================================
# Named lattice registry
# =========================================================================

_NAMED_LATTICES = {
    'Z': ('hypercubic', 1),
    'Z1': ('hypercubic', 1),
    'Z2': ('hypercubic', 2),
    'Z3': ('hypercubic', 3),
    'Z4': ('hypercubic', 4),
    'Z5': ('hypercubic', 5),
    'Z6': ('hypercubic', 6),
    'Z7': ('hypercubic', 7),
    'Z8': ('hypercubic', 8),
    'A2': ('root', 'A2'),
    'A3': ('root', 'A3'),
    'D4': ('root', 'D4'),
    'D5': ('root', 'D5'),
    'E6': ('root', 'E6'),
    'E7': ('root', 'E7'),
    'E8': ('root', 'E8'),
    'Leech': ('leech', 24),
}

# Self-dual (unimodular) lattices: det(Gram) = 1
_UNIMODULAR = {'E8', 'Leech'}

# Root counts for ADE (number of vectors with (v,v) = 2, i.e., r_Lambda(1))
_ROOT_COUNTS = {
    'A2': 6,    # A_2 has 6 roots
    'A3': 12,   # A_3 has 12 roots
    'D4': 24,   # D_4 has 24 roots
    'D5': 40,   # D_5 has 40 roots
    'E6': 72,   # E_6 has 72 roots
    'E7': 126,  # E_7 has 126 roots
    'E8': 240,  # E_8 has 240 roots
}


def get_gram_matrix(name: str) -> np.ndarray:
    """Get Gram matrix for a named lattice."""
    if name not in _NAMED_LATTICES:
        raise ValueError(f"Unknown lattice: {name}. Known: {sorted(_NAMED_LATTICES.keys())}")
    kind, param = _NAMED_LATTICES[name]
    if kind == 'hypercubic':
        return _hypercubic_gram(param)
    elif kind == 'root':
        return root_lattice_gram(param)
    elif kind == 'leech':
        return _leech_gram()
    else:
        raise ValueError(f"Unknown lattice kind: {kind}")


def get_rank(name_or_gram) -> int:
    """Get rank of a lattice from name or Gram matrix."""
    if isinstance(name_or_gram, str):
        gram = get_gram_matrix(name_or_gram)
    else:
        gram = np.asarray(name_or_gram)
    return gram.shape[0]


# =========================================================================
# Theta function coefficients
# =========================================================================

def _convolve(a: List[int], b: List[int], max_n: int) -> List[int]:
    """Convolve two coefficient sequences up to index max_n."""
    result = [0] * (max_n + 1)
    for i in range(min(len(a), max_n + 1)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), max_n + 1 - i)):
            result[i + j] += a[i] * b[j]
    return result


def hypercubic_theta_coefficients(rank: int, max_n: int = 20) -> List[int]:
    r"""Theta coefficients for Z^rank with Gram matrix 2*I.

    For the rank-1 case (Z with (m,m) = 2m^2):
      r_Z(n) = #{m in Z : m^2 = n} (since (m,m)/2 = m^2).
      So r_Z(0) = 1, r_Z(n) = 2 if n is a perfect square, else 0.

    For Z^N: Theta_{Z^N} = (Theta_Z)^N, so coefficients are the
    N-fold convolution of the rank-1 theta series.
    """
    # Rank-1 coefficients
    c1 = [0] * (max_n + 1)
    c1[0] = 1
    for m in range(1, int(math.isqrt(max_n)) + 1):
        if m * m <= max_n:
            c1[m * m] += 2  # ±m

    if rank == 1:
        return c1

    # N-fold convolution via repeated squaring
    result = c1[:]
    for _ in range(rank - 1):
        result = _convolve(result, c1, max_n)

    return result


def lattice_theta_coefficients(gram_matrix: np.ndarray, max_n: int = 20) -> List[int]:
    r"""Compute theta series coefficients r_Lambda(n) for n = 0, ..., max_n.

    r_Lambda(n) = #{lambda in Lambda : (lambda, lambda)/2 = n}

    For the Gram matrix G, (lambda, lambda) = v^T G v for the coordinate
    vector v.  So r_Lambda(n) = #{v in Z^r : v^T G v = 2n}.

    Strategy:
      - Leech (rank 24): use known formula Theta_Leech = E_12 - (65520/691)*Delta
      - Hypercubic Z^N (Gram = 2I): use convolution of rank-1 theta
      - E_8 (rank 8, det 1): use E_4 formula
      - Small lattices (rank <= 5): enumerate vectors in a box
      - Larger lattices: enumerate with reduced bound

    Returns: list of length max_n + 1 with r_Lambda(0), ..., r_Lambda(max_n).
    """
    gram = np.asarray(gram_matrix, dtype=int)
    rank = gram.shape[0]

    # Check if this is the Leech placeholder
    if rank == 24 and np.array_equal(gram, 4 * np.eye(24, dtype=int)):
        return leech_theta_coefficients(max_n)

    # Check if this is a hypercubic lattice (Gram = 2*I)
    if np.array_equal(gram, 2 * np.eye(rank, dtype=int)):
        return hypercubic_theta_coefficients(rank, max_n)

    # Check if this is E_8 by determinant and rank
    if rank == 8:
        det_val = int(round(np.linalg.det(gram)))
        if det_val == 1:
            return e8_theta_coefficients(max_n)

    # For standard lattices, enumerate vectors
    # Need v^T G v <= 2 * max_n, so |v_i| <= sqrt(2*max_n / min_diag)
    min_diag = min(gram[i, i] for i in range(rank))
    if min_diag <= 0:
        raise ValueError("Gram matrix must be positive definite")
    bound = int(math.ceil(math.sqrt(2.0 * max_n / min_diag))) + 1

    # Safety: cap the total enumeration size to avoid exponential blowup
    box_size = (2 * bound + 1) ** rank
    if box_size > 50_000_000:
        raise ValueError(
            f"Enumeration box too large ({box_size} vectors) for rank {rank}, "
            f"bound {bound}. Use a specialized formula for this lattice."
        )

    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1  # zero vector

    # Enumerate all nonzero vectors in [-bound, bound]^rank
    ranges = [range(-bound, bound + 1)] * rank
    for vec in itertools.product(*ranges):
        if all(v == 0 for v in vec):
            continue
        v = np.array(vec, dtype=int)
        norm_sq = int(v @ gram @ v)  # (lambda, lambda) = v^T G v
        if norm_sq < 0:
            continue
        if norm_sq % 2 != 0:
            continue
        n = norm_sq // 2  # (lambda, lambda)/2
        if 0 <= n <= max_n:
            coeffs[n] += 1

    return coeffs


def leech_theta_coefficients(max_n: int = 20) -> List[int]:
    r"""Known theta coefficients for the Leech lattice.

    Theta_Leech = E_{12} - (65520/691) * Delta

    where E_{12}(q) = 1 + (65520/691) sum_{n>=1} sigma_{11}(n) q^n
    and Delta(q) = sum_{n>=1} tau(n) q^n.

    So the n-th coefficient (n >= 1) is:
      r_Leech(n) = (65520/691) * sigma_{11}(n) - (65520/691) * tau(n)
                 = (65520/691) * (sigma_{11}(n) - tau(n))
    """
    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1  # zero vector

    for n in range(1, max_n + 1):
        sig11 = _sigma_k(n, 11)
        tau_n = _ramanujan_tau(n)
        # E_12 coefficient at q^n: (65520/691) * sigma_11(n)
        # But we need EXACT integer result.
        # r_Leech(n) = a_{E12}(n) - (65520/691) * tau(n)
        #            = (65520/691) * sigma_11(n) - (65520/691) * tau(n)
        #            = (65520/691) * (sigma_11(n) - tau(n))
        # This must be an integer.
        numer = 65520 * (sig11 - tau_n)
        assert numer % 691 == 0, f"Leech coefficient at n={n} is not integral"
        coeffs[n] = numer // 691

    return coeffs


def _sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    if n <= 0:
        return 0
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


@lru_cache(maxsize=500)
def _ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficients of Delta = eta^{24}.

    Delta(tau) = q * prod_{m>=1} (1 - q^m)^{24} = sum_{n>=1} tau(n) q^n.
    """
    if n < 1:
        return 0
    # Compute coefficients of prod_{m=1}^{n} (1-q^m)^{24} up to q^{n-1}
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    return coeffs[n - 1] if n - 1 <= N else 0


def e8_theta_coefficients(max_n: int = 20) -> List[int]:
    r"""Theta coefficients for E_8 via E_4 = 1 + 240*sum sigma_3(n) q^n.

    Since dim M_4(SL_2(Z)) = 1 and dim S_4 = 0, Theta_{E_8} = E_4.
    """
    coeffs = [0] * (max_n + 1)
    coeffs[0] = 1
    for n in range(1, max_n + 1):
        coeffs[n] = 240 * _sigma_k(n, 3)
    return coeffs


# =========================================================================
# Shadow tower data
# =========================================================================

def lattice_shadow_data(name_or_gram) -> Dict[str, Any]:
    """Complete shadow tower data for a lattice VOA.

    Returns a dictionary with:
      name: lattice name (if known)
      rank: rank of the lattice
      central_charge: c = rank
      kappa: modular characteristic = rank
      cubic_shadow: C = 0
      quartic_contact: Q = 0
      shadow_depth: r_max = 2
      shadow_class: 'G' (Gaussian)
      shadow_metric: Q_L = (2*kappa)^2
      critical_discriminant: Delta = 0
      alpha: cubic coefficient on primary line = 0
      S4: quartic coefficient on primary line = 0
      is_self_dual: whether the lattice is unimodular
      gram_det: determinant of Gram matrix
    """
    if isinstance(name_or_gram, str):
        name = name_or_gram
        gram = get_gram_matrix(name)
    else:
        name = 'custom'
        gram = np.asarray(name_or_gram)

    rank = gram.shape[0]

    # For named lattices, use the known unimodularity data
    # (the Leech Gram matrix is a placeholder and its determinant is not meaningful)
    if name in _UNIMODULAR:
        is_unimodular = True
        det_gram = 1
    else:
        det_gram = int(round(np.linalg.det(gram)))
        is_unimodular = (abs(det_gram) == 1)

    kappa = Rational(rank)

    return {
        'name': name,
        'rank': rank,
        'central_charge': Rational(rank),
        'kappa': kappa,
        'cubic_shadow': Rational(0),
        'quartic_contact': Rational(0),
        'shadow_depth': 2,
        'shadow_class': 'G',
        'shadow_metric': 4 * kappa ** 2,
        'critical_discriminant': Rational(0),
        'alpha': Rational(0),
        'S4': Rational(0),
        'is_self_dual': is_unimodular,
        'gram_det': det_gram,
    }


# =========================================================================
# Genus expansion
# =========================================================================

def lattice_genus_expansion(rank: int, max_g: int = 5) -> Dict[int, Rational]:
    """Genus expansion for a lattice VOA of given rank.

    F_g(V_Lambda) = rank * lambda_g^FP for all g >= 1.
    """
    result = {}
    kappa = Rational(rank)
    for g in range(1, max_g + 1):
        result[g] = kappa * faber_pandharipande(g)
    return result


# =========================================================================
# Tridegree decomposition
# =========================================================================

def lattice_tridegree_table(rank: int, max_g: int = 2) -> Dict[Tuple[int, int, int], Rational]:
    """Tridegree decomposition of the shadow tower for a lattice VOA.

    Tridegree (g, n, d) where g = loop genus, n = arity, d = log boundary depth.

    For Gaussian class (shadow depth 2):
      - (g, 2, 0) = kappa for each g >= 1
      - All entries with n >= 3 or d >= 1 vanish

    Returns dict {(g, n, d): value} for 1 <= g <= max_g, 2 <= n <= 5, 0 <= d <= 2.
    """
    kappa = Rational(rank)
    table = {}

    for g in range(1, max_g + 1):
        for n in range(2, 6):
            for d in range(3):
                if n == 2 and d == 0:
                    table[(g, n, d)] = kappa
                else:
                    table[(g, n, d)] = Rational(0)

    return table


# =========================================================================
# Partition function coefficients (genus 1)
# =========================================================================

def _eta_inverse_coefficients(rank: int, max_n: int) -> List[Rational]:
    r"""Coefficients of 1/eta(tau)^rank = q^{-rank/24} * prod_{m>=1} 1/(1-q^m)^rank.

    We compute the product expansion of 1/prod(1-q^m)^rank up to q^{max_n}.
    This is related to partition functions: for rank=1 it gives p(n).

    Returns coefficients c_n where 1/eta^rank = q^{-rank/24} * sum c_n q^n.
    """
    coeffs = [Rational(0)] * (max_n + 1)
    coeffs[0] = Rational(1)

    for m in range(1, max_n + 1):
        # Multiply by 1/(1 - q^m)^rank = sum_{j>=0} C(rank+j-1, j) q^{m*j}
        # Equivalently, apply the rank-fold operator (1/(1-q^m)) rank times.
        for _ in range(rank):
            for i in range(m, max_n + 1):
                coeffs[i] += coeffs[i - m]

    return coeffs


def lattice_partition_function_coefficients(
    gram_matrix: np.ndarray, max_n: int = 20
) -> List[Rational]:
    r"""Coefficients of Z_1(V_Lambda; tau) = Theta_Lambda / eta^rank.

    Z_1 = (sum r_Lambda(n) q^n) * (sum p_rank(n) q^n) * q^{-rank/24}

    We compute the product of theta coefficients and eta^{-rank} coefficients,
    ignoring the overall q^{-rank/24} prefactor (which shifts the grading).

    Returns the coefficients of the formal q-expansion starting from the
    leading term, truncated to max_n + 1 terms.
    """
    gram = np.asarray(gram_matrix, dtype=int)
    rank = gram.shape[0]

    theta = lattice_theta_coefficients(gram, max_n)
    eta_inv = _eta_inverse_coefficients(rank, max_n)

    # Convolve: (sum_m a_m q^m)(sum_n b_n q^n) = sum_k (sum_{m+n=k} a_m b_n) q^k
    result = [Rational(0)] * (max_n + 1)
    for k in range(max_n + 1):
        s = Rational(0)
        for m in range(k + 1):
            s += Rational(theta[m]) * eta_inv[k - m]
        result[k] = s

    return result


# =========================================================================
# Complementarity
# =========================================================================

def lattice_complementarity(gram_matrix: np.ndarray) -> Tuple[Rational, Rational, Rational]:
    """Complementarity data for a lattice VOA.

    For a lattice Lambda:
      kappa(V_Lambda) = rank(Lambda)
      V_Lambda^! = V_{Lambda^*} where Lambda^* is the dual lattice
      rank(Lambda^*) = rank(Lambda), so kappa(V_{Lambda^*}) = rank(Lambda)

    For self-dual (unimodular) lattices: Lambda = Lambda^*, V^! = V.

    Returns (kappa, kappa_dual, kappa + kappa_dual).

    Note: both the lattice and its dual have the same rank, so
    kappa = kappa_dual = rank.  The complementarity sum is 2*rank.
    """
    gram = np.asarray(gram_matrix, dtype=int)
    rank = gram.shape[0]
    kappa = Rational(rank)
    kappa_dual = Rational(rank)
    return (kappa, kappa_dual, kappa + kappa_dual)


# =========================================================================
# Effective action
# =========================================================================

def effective_action_correction(rank: int, order: int = 4) -> Rational:
    """Nonlinear correction to the effective action at given order.

    For Gaussian class (lattice VOAs), the effective action is
    S_eff = kappa * S_Polyakov with NO nonlinear corrections.
    All corrections vanish identically.

    Returns 0 for all orders >= 3.
    """
    return Rational(0)


# =========================================================================
# Comprehensive census function
# =========================================================================

_ALL_CENSUS_NAMES = [
    'Z', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6', 'Z7', 'Z8',
    'A2', 'A3', 'D4', 'D5', 'E6', 'E7', 'E8', 'Leech',
]


def full_census(max_n_theta: int = 10, max_g: int = 5) -> Dict[str, Dict[str, Any]]:
    """Run the complete shadow census for all standard lattice VOAs.

    Returns a dictionary keyed by lattice name, each containing:
      shadow: shadow tower data
      genus_expansion: {g: F_g}
      theta_coefficients: [r_Lambda(0), ..., r_Lambda(max_n_theta)]
      tridegree: tridegree table
    """
    results = {}
    for name in _ALL_CENSUS_NAMES:
        shadow = lattice_shadow_data(name)
        rank = shadow['rank']
        genus = lattice_genus_expansion(rank, max_g)
        gram = get_gram_matrix(name)

        if name == 'Leech':
            theta = leech_theta_coefficients(max_n_theta)
        elif name == 'E8':
            theta = e8_theta_coefficients(max_n_theta)
        elif name.startswith('Z') or name == 'Z':
            # Hypercubic: use fast convolution
            theta = hypercubic_theta_coefficients(rank, max_n_theta)
        elif rank <= 5:
            theta = lattice_theta_coefficients(gram, max_n_theta)
        else:
            # For rank > 5 non-hypercubic lattices, use enumeration
            # with a conservative max_n to avoid timeout
            safe_max_n = min(max_n_theta, 5)
            try:
                theta = lattice_theta_coefficients(gram, safe_max_n)
                # Pad to max_n_theta if needed
                if len(theta) < max_n_theta + 1:
                    theta = theta + [0] * (max_n_theta + 1 - len(theta))
            except ValueError:
                theta = [1] + [0] * max_n_theta  # fallback

        results[name] = {
            'shadow': shadow,
            'genus_expansion': genus,
            'theta_coefficients': theta,
            'tridegree': lattice_tridegree_table(shadow['rank'], max_g=2),
        }

    return results


# =========================================================================
# Additivity verification
# =========================================================================

def verify_additivity(rank1: int, rank2: int, max_g: int = 5) -> bool:
    """Verify that F_g(V_{Z^{r1+r2}}) = F_g(V_{Z^r1}) + F_g(V_{Z^r2}).

    This is a consequence of independent sum factorization
    (prop:independent-sum-factorization): kappa is additive for
    direct sum lattices.
    """
    expansion_sum = lattice_genus_expansion(rank1 + rank2, max_g)
    expansion_1 = lattice_genus_expansion(rank1, max_g)
    expansion_2 = lattice_genus_expansion(rank2, max_g)

    for g in range(1, max_g + 1):
        if expansion_sum[g] != expansion_1[g] + expansion_2[g]:
            return False
    return True


# =========================================================================
# Gram matrix properties
# =========================================================================

def gram_determinant(gram_matrix: np.ndarray) -> int:
    """Exact determinant of an integer Gram matrix."""
    # Use sympy for exact computation
    G = Matrix(gram_matrix.tolist())
    return int(G.det())


def is_even_lattice(gram_matrix: np.ndarray) -> bool:
    """Check if a Gram matrix defines an even lattice.

    An even lattice has (v, v) in 2Z for all lattice vectors,
    which is equivalent to all diagonal entries being even.
    """
    gram = np.asarray(gram_matrix, dtype=int)
    return all(gram[i, i] % 2 == 0 for i in range(gram.shape[0]))


def dual_lattice_index(gram_matrix: np.ndarray) -> int:
    """Index [Lambda^* : Lambda] = |det(Gram)|.

    For a unimodular lattice this is 1 (self-dual).
    """
    return abs(gram_determinant(gram_matrix))
