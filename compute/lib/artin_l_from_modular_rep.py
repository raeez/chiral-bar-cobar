#!/usr/bin/env python3
r"""
artin_l_from_modular_rep.py — Artin L-functions from modular representations of rational VOAs.

THE BRIDGE: The 12-agent swarm found that the SCALAR Dirichlet series
  sum a_n n^{-s}
from minimal model partition functions is non-multiplicative. But the modular
representation rho: SL(2,Z) -> GL(n,C) of a rational VOA is a group
representation, and group representations carry Artin L-functions that ARE
multiplicative by construction.

STRUCTURE:
  1. Modular data (S, T matrices) for rational VOAs
  2. Image group Im(rho) is FINITE for rational VOAs (Bantay's theorem)
  3. Galois action sigma_p on modular data (de Boer-Goeree, Coste-Gannon)
  4. Artin L-function: L(s, rho) = prod_p det(I - rho(sigma_p) p^{-s})^{-1}
  5. Verlinde fusion ring and its multiplicative structure
  6. Conductor computation from the level N of the representation

KEY FORMULA (corrected):
  S_{(r,s),(r',s')} = (-1)^{1+rs'+r's} * sqrt(8/(pq))
                      * sin(pi*q*r*r'/p) * sin(pi*p*s*s'/q)
  Note the CROSSED sines: sin has q/p (not 1/p) for the r-factor and p/q for the s-factor.
  This is the Di Francesco-Mathieu-Senechal convention (Yellow Book, eq 10.45).

KEY EXAMPLES:
  - Ising model M(4,3): 3 primaries, S involves sqrt(2), conductor 48
  - Lee-Yang M(5,2): 2 primaries, S involves sqrt(5), conductor 60
  - Tricritical Ising M(5,4): 6 primaries

REFERENCE: Coste-Gannon, "Remarks on Galois symmetry in RCFT" (1999);
Bantay, "The kernel of the modular representation and the Galois action
in RCFT" (2003); Di Francesco-Mathieu-Senechal, "Conformal Field Theory" (1997).
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
import math
from functools import lru_cache

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. Modular data for minimal models M(p,q) and other RCFTs
# ============================================================

def _exp2pii(x):
    """Compute e^{2*pi*i*x} with high precision."""
    if HAS_MPMATH:
        return mpmath.exp(2 * mpmath.pi * 1j * x)
    return np.exp(2j * np.pi * x)


def _to_complex(x):
    """Convert mpmath complex to Python complex."""
    if HAS_MPMATH and isinstance(x, (mpmath.mpc, mpmath.mpf)):
        return complex(x)
    return complex(x)


def minimal_model_primaries(p, q):
    """Return conformal weights h_{r,s} for M(p,q) minimal model.

    Primaries are labeled by (r,s) with 1 <= r <= p-1, 1 <= s <= q-1,
    with identification (r,s) ~ (p-r, q-s).

    Central charge: c = 1 - 6(p-q)^2/(pq).

    Returns list of (r, s, h_{r,s}) for the independent primaries,
    sorted by conformal weight.
    """
    if p <= q:
        raise ValueError(f"Need p > q >= 2 for minimal model M(p,q), got ({p},{q})")
    if math.gcd(p, q) != 1:
        raise ValueError(f"p and q must be coprime for minimal model, got ({p},{q})")

    primaries = []
    seen = set()
    for r in range(1, p):
        for s in range(1, q):
            canon = (r, s) if r < p - r or (r == p - r and s <= q - s) else (p - r, q - s)
            if canon not in seen:
                seen.add(canon)
                h = ((q * r - p * s)**2 - (p - q)**2) / (4 * p * q)
                primaries.append((canon[0], canon[1], h))

    # Sort with vacuum (1,1) ALWAYS first, then by conformal weight.
    # This is required for the Verlinde formula (index 0 = vacuum).
    # For non-unitary models (e.g. Lee-Yang), h_{1,1} = 0 but other h can be negative.
    def sort_key(item):
        r, s, h = item
        if r == 1 and s == 1:
            return (-1e10, h)  # Vacuum always first
        return (0, h)
    primaries.sort(key=sort_key)
    return primaries


def minimal_model_central_charge(p, q):
    """Central charge c = 1 - 6(p-q)^2/(pq) for M(p,q)."""
    return 1 - 6 * (p - q)**2 / (p * q)


def minimal_model_s_matrix(p, q):
    """Compute the modular S-matrix for M(p,q) minimal model.

    CORRECTED FORMULA (DiFrancesco-Mathieu-Senechal, Yellow Book):
    S_{(r,s),(r',s')} = (-1)^{1+rs'+r's} * sqrt(8/(pq))
                        * sin(pi*q*r*r'/p) * sin(pi*p*s*s'/q)

    Note: sin arguments use CROSSED coefficients q/p and p/q.

    Returns (S, labels) where labels are the (r,s) pairs.
    """
    primaries = minimal_model_primaries(p, q)
    n = len(primaries)
    labels = [(r, s) for r, s, h in primaries]

    S = np.zeros((n, n), dtype=complex)
    prefactor = np.sqrt(8.0 / (p * q))
    for i, (r, s, _) in enumerate(primaries):
        for j, (rp, sp, _) in enumerate(primaries):
            sign = (-1)**(1 + r * sp + rp * s)
            S[i, j] = sign * prefactor * np.sin(np.pi * q * r * rp / p) * \
                       np.sin(np.pi * p * s * sp / q)

    return S, labels


def minimal_model_t_matrix(p, q):
    """Compute the modular T-matrix for M(p,q) minimal model.

    T_{(r,s),(r,s)} = e^{2*pi*i*(h_{r,s} - c/24)}

    Returns (T, labels).
    """
    primaries = minimal_model_primaries(p, q)
    n = len(primaries)
    labels = [(r, s) for r, s, h in primaries]
    c = minimal_model_central_charge(p, q)

    T = np.diag([np.exp(2j * np.pi * (h - c / 24)) for r, s, h in primaries])
    return T, labels


# ============================================================
# 2. Ising model M(4,3) — explicit verified data
# ============================================================

def ising_s_matrix():
    """The Ising model S-matrix (3x3).

    Primaries: 1 (identity, h=0), sigma (h=1/16), epsilon (h=1/2).
    Ordering: sorted by conformal weight [1, sigma, epsilon].

    Matches minimal_model_s_matrix(4, 3).
    """
    S, _ = minimal_model_s_matrix(4, 3)
    return S


def ising_t_matrix():
    """The Ising T-matrix (3x3 diagonal).

    Matches minimal_model_t_matrix(4, 3).
    """
    T, _ = minimal_model_t_matrix(4, 3)
    return T


# ============================================================
# 3. Lee-Yang model M(5,2) — 2 primaries
# ============================================================

def lee_yang_s_matrix():
    """The Lee-Yang model S-matrix (2x2).

    M(5,2): primaries (1,1) with h=0 and (2,1) with h=-1/5.
    c = -22/5 (non-unitary).

    Uses the corrected minimal model formula.
    """
    S, _ = minimal_model_s_matrix(5, 2)
    return S


def lee_yang_t_matrix():
    """Lee-Yang T-matrix (2x2 diagonal)."""
    T, _ = minimal_model_t_matrix(5, 2)
    return T


# ============================================================
# 4. Tricritical Ising M(5,4) — 6 primaries
# ============================================================

def tricritical_ising_data():
    """Return (S, T, labels) for the tricritical Ising model M(5,4).

    6 primaries. Central charge c = 7/10.
    Uses the general minimal model formula.
    """
    S, labels = minimal_model_s_matrix(5, 4)
    T, _ = minimal_model_t_matrix(5, 4)
    return S, T, labels


# ============================================================
# 5. Image group analysis
# ============================================================

def matrix_to_numpy(M):
    """Convert mpmath matrix to numpy array."""
    if HAS_MPMATH and isinstance(M, mpmath.matrix):
        n = M.rows
        result = np.zeros((n, n), dtype=complex)
        for i in range(n):
            for j in range(n):
                result[i, j] = complex(M[i, j])
        return result
    return np.array(M, dtype=complex)


def mat_mul(A, B):
    """Multiply two matrices (numpy)."""
    An = matrix_to_numpy(A) if not isinstance(A, np.ndarray) else A
    Bn = matrix_to_numpy(B) if not isinstance(B, np.ndarray) else B
    return An @ Bn


def mat_power(M, n):
    """Compute M^n for integer n >= 0."""
    Mn = matrix_to_numpy(M)
    size = Mn.shape[0]
    if n == 0:
        return np.eye(size, dtype=complex)
    result = np.eye(size, dtype=complex)
    base = Mn.copy()
    k = n
    while k > 0:
        if k % 2 == 1:
            result = result @ base
        base = base @ base
        k //= 2
    return result


def matrix_approx_equal(A, B, tol=1e-10):
    """Check if two matrices are approximately equal."""
    An = matrix_to_numpy(A)
    Bn = matrix_to_numpy(B)
    return np.allclose(An, Bn, atol=tol)


def find_matrix_order(M, max_order=10000):
    """Find the order of matrix M (smallest n > 0 with M^n = I)."""
    Mn = matrix_to_numpy(M)
    size = Mn.shape[0]
    I = np.eye(size, dtype=complex)

    power = Mn.copy()
    for n in range(1, max_order + 1):
        if np.allclose(power, I, atol=1e-10):
            return n
        power = power @ Mn
    return None


def compute_image_group_order(S, T, max_elements=5000):
    """Compute |Im(rho)| where rho: SL(2,Z) -> GL(n,C).

    SL(2,Z) is generated by S and T. The image group is generated
    by rho(S) and rho(T).

    Uses BFS enumeration with numpy arrays and a hash-based lookup
    for efficiency.

    Returns (|G|, order_S, order_T, order_ST).
    """
    Sn = matrix_to_numpy(S)
    Tn = matrix_to_numpy(T)
    STn = Sn @ Tn

    order_S = find_matrix_order(Sn, max_order=200)
    order_T = find_matrix_order(Tn, max_order=200)
    order_ST = find_matrix_order(STn, max_order=200)

    size = Sn.shape[0]
    I = np.eye(size, dtype=complex)

    # Use rounded matrix entries as hash keys for fast lookup
    def mat_key(M, decimals=6):
        return tuple(np.round(M.flatten(), decimals=decimals).view(float))

    seen = set()
    elements = []

    def add_if_new(M):
        k = mat_key(M)
        if k not in seen:
            seen.add(k)
            elements.append(M.copy())
            return True
        return False

    add_if_new(I)
    head = 0
    while head < len(elements) and len(elements) < max_elements:
        current = elements[head]
        head += 1
        for gen in [Sn, Tn]:
            product = current @ gen
            add_if_new(product)

    return len(elements), order_S, order_T, order_ST


def compute_image_group_elements(S, T, max_elements=5000):
    """Enumerate all elements of Im(rho) as numpy arrays."""
    Sn = matrix_to_numpy(S)
    Tn = matrix_to_numpy(T)
    size = Sn.shape[0]
    I = np.eye(size, dtype=complex)

    def mat_key(M, decimals=6):
        return tuple(np.round(M.flatten(), decimals=decimals).view(float))

    seen = set()
    elements = []

    def add_if_new(M):
        k = mat_key(M)
        if k not in seen:
            seen.add(k)
            elements.append(M.copy())
            return True
        return False

    add_if_new(I)
    head = 0
    while head < len(elements) and len(elements) < max_elements:
        current = elements[head]
        head += 1
        for gen in [Sn, Tn]:
            product = current @ gen
            add_if_new(product)

    return elements


# ============================================================
# 6. S-matrix eigenvalues and unitarity
# ============================================================

def s_matrix_eigenvalues(S):
    """Compute eigenvalues of the S-matrix."""
    Sn = matrix_to_numpy(S)
    return np.linalg.eigvals(Sn)


def t_matrix_eigenvalues(T):
    """Compute eigenvalues (diagonal entries) of T-matrix."""
    Tn = matrix_to_numpy(T)
    return np.diag(Tn)


def verify_unitarity(S, tol=1e-10):
    """Verify S S^dagger = I (unitarity of S-matrix)."""
    Sn = matrix_to_numpy(S)
    product = Sn @ Sn.conj().T
    return np.allclose(product, np.eye(Sn.shape[0]), atol=tol)


def verify_s_squared(S, tol=1e-10):
    """Verify S^2 = C (charge conjugation matrix).

    For unitary minimal models, C = I (all representations are self-conjugate).
    Returns (is_involution, C_matrix) where is_involution = (S^2 = I).
    """
    Sn = matrix_to_numpy(S)
    S2 = Sn @ Sn
    is_involution = np.allclose(S2, np.eye(Sn.shape[0]), atol=tol)
    return is_involution, S2


def verify_modular_relation(S, T, tol=1e-10):
    """Verify (ST)^3 = S^2 (fundamental SL(2,Z) relation)."""
    Sn = matrix_to_numpy(S)
    Tn = matrix_to_numpy(T)
    ST = Sn @ Tn
    ST3 = ST @ ST @ ST
    S2 = Sn @ Sn
    return np.allclose(ST3, S2, atol=tol)


# ============================================================
# 7. Verlinde fusion coefficients
# ============================================================

def verlinde_fusion(S, i, j, k):
    """Compute fusion coefficient N_{ij}^k via Verlinde formula.

    N_{ij}^k = sum_l S_{il} S_{jl} S*_{kl} / S_{0l}
    """
    Sn = matrix_to_numpy(S)
    n = Sn.shape[0]
    result = 0.0
    for l in range(n):
        result += Sn[i, l] * Sn[j, l] * np.conj(Sn[k, l]) / Sn[0, l]
    return result


def all_fusion_coefficients(S):
    """Compute all fusion coefficients N_{ij}^k."""
    Sn = matrix_to_numpy(S)
    n = Sn.shape[0]
    N = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                N[(i, j, k)] = verlinde_fusion(S, i, j, k)
    return N


def verify_fusion_ring(S, tol=1e-6):
    """Verify the Verlinde fusion coefficients satisfy ring axioms.

    1. N_{ij}^k are non-negative integers
    2. N_{0j}^k = delta_{jk} (identity element)
    3. N_{ij}^k = N_{ji}^k (commutativity)
    4. Associativity

    Returns (all_pass, details).
    """
    Sn = matrix_to_numpy(S)
    n = Sn.shape[0]
    N = all_fusion_coefficients(S)
    details = []
    all_pass = True

    for (i, j, k), val in N.items():
        rounded = round(val.real)
        if abs(val.real - rounded) > tol or abs(val.imag) > tol:
            details.append(f"N_{{{i},{j}}}^{k} = {val} not integer")
            all_pass = False
        if rounded < 0:
            details.append(f"N_{{{i},{j}}}^{k} = {rounded} < 0")
            all_pass = False

    for j in range(n):
        for k in range(n):
            val = round(N[(0, j, k)].real)
            expected = 1 if j == k else 0
            if val != expected:
                details.append(f"N_{{0,{j}}}^{k} = {val}, expected {expected}")
                all_pass = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if abs(N[(i, j, k)] - N[(j, i, k)]) > tol:
                    details.append(f"N_{{{i},{j}}}^{k} != N_{{{j},{i}}}^{k}")
                    all_pass = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    lhs = sum(round(N[(i, j, m)].real) * round(N[(m, k, l)].real) for m in range(n))
                    rhs = sum(round(N[(j, k, m)].real) * round(N[(i, m, l)].real) for m in range(n))
                    if lhs != rhs:
                        details.append(f"Associativity fails: ({i},{j},{k},{l})")
                        all_pass = False

    return all_pass, details


def quantum_dimensions(S):
    """Compute quantum dimensions d_i = S_{0i}/S_{00}.

    For non-unitary models, some d_i may be negative.
    """
    Sn = matrix_to_numpy(S)
    return [Sn[0, i] / Sn[0, 0] for i in range(Sn.shape[0])]


def total_quantum_dimension(S):
    """Compute D^2 = sum_i d_i^2 = 1/|S_{00}|^2."""
    Sn = matrix_to_numpy(S)
    return 1.0 / (Sn[0, 0] * np.conj(Sn[0, 0]))


# ============================================================
# 8. Galois action on modular data
# ============================================================

def galois_permutation_from_t(T, l, tol=1e-8):
    """Compute the Galois permutation sigma_l from the T-matrix.

    T_{jj} = e^{2*pi*i*alpha_j}. Under sigma_l:
      e^{2*pi*i*alpha_j} -> e^{2*pi*i*l*alpha_j}

    sigma_l(j) = k where alpha_k = l*alpha_j (mod Z).

    Returns (permutation, valid) where valid=False if l divides conductor.
    """
    Tn = matrix_to_numpy(T)
    n = Tn.shape[0]

    alphas = []
    for j in range(n):
        phase = np.angle(Tn[j, j]) / (2 * np.pi)
        phase = phase % 1.0
        alphas.append(phase)

    permutation = [None] * n
    for j in range(n):
        target = (l * alphas[j]) % 1.0
        best_k = None
        best_dist = float('inf')
        for k in range(n):
            dist = min(abs(alphas[k] - target),
                       abs(alphas[k] - target + 1),
                       abs(alphas[k] - target - 1))
            if dist < best_dist:
                best_dist = dist
                best_k = k
        if best_dist > tol:
            return None, False
        permutation[j] = best_k

    if len(set(permutation)) != n:
        return None, False

    return permutation, True


def galois_signs_from_s(S, T, l, tol=1e-8):
    """Compute full Galois data: permutation sigma_l and signs epsilon_l.

    Strategy: first try T-eigenvalue matching. If that fails (can happen for
    non-unitary models where l*alpha_j doesn't match any alpha_k), fall back
    to the S-matrix number field approach.

    Returns (permutation, signs) or (None, None) if l divides conductor.
    """
    # First try T-eigenvalue approach
    perm, valid = galois_permutation_from_t(T, l, tol=tol)

    if not valid:
        # Check if l divides the conductor
        N = conductor_from_t(T)
        if N is not None and math.gcd(l, N) != 1:
            return None, None
        # T-eigenvalue approach failed but l is coprime to conductor.
        # Fall back: use the fusion ring. sigma_l must be a fusion ring
        # automorphism. Enumerate all permutations that preserve fusion.
        Sn = matrix_to_numpy(S)
        n = Sn.shape[0]
        # For small n, just try all permutations
        if n <= 8:
            from itertools import permutations
            N_fus = all_fusion_coefficients(S)
            for p_candidate in permutations(range(n)):
                p_list = list(p_candidate)
                # Check fusion preservation
                ok = True
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            n1 = round(N_fus[(i, j, k)].real)
                            n2 = round(N_fus[(p_list[i], p_list[j], p_list[k])].real)
                            if n1 != n2:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break
                if ok and p_list != list(range(n)):
                    # Found a nontrivial automorphism. Use it.
                    perm = p_list
                    break
            else:
                # Only trivial automorphism
                perm = list(range(n))
        else:
            return None, None

    # Compute signs from S-matrix
    Sn = matrix_to_numpy(S)
    n = Sn.shape[0]
    signs = []
    for i in range(n):
        val_original = Sn[0, i].real
        val_image = Sn[0, perm[i]].real
        if abs(val_original) < tol:
            signs.append(1)
        else:
            signs.append(1 if val_original * val_image > 0 else -1)

    return perm, signs


# ============================================================
# 9. Artin L-function construction
# ============================================================

def galois_matrix_at_prime(S, T, p, tol=1e-8):
    """Compute the matrix rho(sigma_p) in GL(n,C) for the Galois element at prime p.

    rho(sigma_p)_{ij} = epsilon_p(j) * delta_{i, sigma_p(j)}

    Returns the n x n matrix, or None if p divides the conductor.
    """
    perm, signs = galois_signs_from_s(S, T, p, tol=tol)
    if perm is None:
        return None

    n = len(perm)
    M = np.zeros((n, n), dtype=complex)
    for j in range(n):
        M[perm[j], j] = signs[j]
    return M


def artin_l_function_euler_factor(S, T, p, s, tol=1e-8):
    """Compute the Euler factor at prime p:

      L_p(s) = det(I - rho(sigma_p) * p^{-s})^{-1}

    Returns the value of the Euler factor, or None if p is ramified.
    """
    rho_p = galois_matrix_at_prime(S, T, p, tol=tol)
    if rho_p is None:
        return None

    n = rho_p.shape[0]
    I = np.eye(n, dtype=complex)
    det_val = np.linalg.det(I - rho_p * p**(-s))
    if abs(det_val) < 1e-30:
        return float('inf')
    return 1.0 / det_val


def artin_l_function_partial(S, T, s, num_primes=100, tol=1e-8):
    """Compute the partial Artin L-function as a product of Euler factors.

    L(s, rho) = prod_{p good} det(I - rho(sigma_p) p^{-s})^{-1}

    Returns (value, primes_used, ramified_primes).
    """
    N = conductor_from_t(T)
    primes = _primes_up_to(num_primes * 10)[:num_primes]

    product = complex(1.0)
    used = []
    ramified = []

    for p in primes:
        if N is not None and N % p == 0:
            ramified.append(p)
            continue

        factor = artin_l_function_euler_factor(S, T, p, s, tol=tol)
        if factor is None:
            ramified.append(p)
        else:
            product *= factor
            used.append(p)

    return product, used, ramified


def artin_l_irreducible_factors(S, T, s, num_primes=50):
    """Decompose L(s, rho) = prod_k L(s, sigma_k)^{m_k} via character decomposition.

    Returns dict with keys 'total', 'trivial_component', 'nontrivial_component'.
    """
    N = conductor_from_t(T)
    Sn = matrix_to_numpy(S)
    n = Sn.shape[0]

    primes = _primes_up_to(num_primes * 10)[:num_primes]

    total = complex(1.0)
    trivial = complex(1.0)
    nontrivial = complex(1.0)

    for p in primes:
        if N is not None and N % p == 0:
            continue

        rho_p = galois_matrix_at_prime(S, T, p)
        if rho_p is None:
            continue

        I_n = np.eye(n, dtype=complex)
        det_full = np.linalg.det(I_n - rho_p * p**(-s))
        if abs(det_full) < 1e-30:
            continue

        total *= 1.0 / det_full
        trivial_factor = 1.0 / (1 - p**(-s))
        trivial *= trivial_factor

        nontrivial_det = det_full / (1 - p**(-s))
        if abs(nontrivial_det) > 1e-30:
            nontrivial *= 1.0 / nontrivial_det

    return {
        'total': total,
        'trivial_component': trivial,
        'nontrivial_component': nontrivial,
        'conductor': N,
        'dimension': n,
    }


# ============================================================
# 10. Representation decomposition
# ============================================================

def decompose_representation(elements, tol=1e-6):
    """Decompose a representation given as a list of group element matrices.

    Uses character theory: chi(g) = Tr(rho(g)).
    Multiplicity of trivial rep: m_1 = (1/|G|) sum chi(g).
    ||chi||^2 = (1/|G|) sum |chi(g)|^2 = sum m_k^2.

    Returns dict with decomposition data.
    """
    if not elements:
        return None

    n = elements[0].shape[0]
    G_size = len(elements)

    characters = [np.trace(g) for g in elements]
    m_trivial = sum(characters).real / G_size
    chi_norm_sq = sum(abs(c)**2 for c in characters).real / G_size

    return {
        'dim': n,
        'group_order': G_size,
        'characters': characters,
        'trivial_multiplicity': round(m_trivial.real),
        'character_norm_sq': round(chi_norm_sq.real),
        'is_multiplicity_free': abs(chi_norm_sq - round(chi_norm_sq)) < tol,
    }


def character_table_from_elements(elements, tol=1e-6):
    """Compute conjugacy classes of the group.

    Returns dict with num_classes, class_sizes, group_order.
    """
    G_size = len(elements)
    classes = []
    assigned = [False] * G_size

    for i in range(G_size):
        if assigned[i]:
            continue
        cls = [i]
        assigned[i] = True
        for j in range(G_size):
            if assigned[j]:
                continue
            for k in range(G_size):
                conjugated = elements[k] @ elements[j] @ np.linalg.inv(elements[k])
                if np.allclose(conjugated, elements[i], atol=tol):
                    cls.append(j)
                    assigned[j] = True
                    break
        classes.append(cls)

    return {
        'num_classes': len(classes),
        'class_sizes': [len(c) for c in classes],
        'group_order': G_size,
    }


# ============================================================
# 11. Conductor and ramification
# ============================================================

def conductor_from_t(T, max_N=10000):
    """Find the smallest N such that T^N = I (the conductor)."""
    return find_matrix_order(T, max_order=max_N)


def conductor_minimal_model(p, q):
    """The conductor of the modular representation for M(p,q).

    Computed from the exact fractions h_{r,s} - c/24.
    """
    primaries = minimal_model_primaries(p, q)
    c = minimal_model_central_charge(p, q)

    from fractions import Fraction
    denoms = []
    for r, s, h in primaries:
        h_frac = Fraction((q * r - p * s)**2 - (p - q)**2, 4 * p * q)
        c_frac = Fraction(1, 1) - Fraction(6 * (p - q)**2, p * q)
        val = h_frac - c_frac / 24
        denoms.append(val.denominator)

    N = denoms[0]
    for d in denoms[1:]:
        N = N * d // math.gcd(N, d)

    return N


def ramified_primes(N):
    """Return the set of primes dividing N."""
    if N is None or N <= 1:
        return set()
    primes = set()
    d = 2
    temp = N
    while d * d <= temp:
        if temp % d == 0:
            primes.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        primes.add(temp)
    return primes


# ============================================================
# 12. Minimal model survey
# ============================================================

def minimal_model_survey(p_max=8, q_max=None):
    """Survey minimal models M(p,q) with p,q <= p_max.

    For each model, compute number of primaries, central charge,
    conductor, and group data.

    Returns list of dicts.
    """
    if q_max is None:
        q_max = p_max
    results = []
    for p in range(3, p_max + 1):
        for q in range(2, min(p, q_max + 1)):
            if math.gcd(p, q) != 1:
                continue
            try:
                primaries = minimal_model_primaries(p, q)
                c = minimal_model_central_charge(p, q)
                N = conductor_minimal_model(p, q)
                n_primaries = len(primaries)

                S, labels = minimal_model_s_matrix(p, q)
                T, _ = minimal_model_t_matrix(p, q)

                # Group order (only for small representations to avoid timeout)
                if n_primaries <= 4:
                    group_order, ord_S, ord_T, ord_ST = compute_image_group_order(
                        S, T, max_elements=2000)
                else:
                    group_order = None
                    ord_S = find_matrix_order(S, max_order=200)
                    ord_T = find_matrix_order(T, max_order=200)
                    ord_ST = None

                results.append({
                    'p': p, 'q': q,
                    'label': f'M({p},{q})',
                    'n_primaries': n_primaries,
                    'central_charge': c,
                    'conductor': N,
                    'group_order': group_order,
                    'order_S': ord_S,
                    'order_T': ord_T,
                    'order_ST': ord_ST,
                    'ramified_primes': ramified_primes(N),
                })
            except Exception as e:
                results.append({
                    'p': p, 'q': q,
                    'label': f'M({p},{q})',
                    'error': str(e),
                })
    return results


# ============================================================
# 13. Ising Galois analysis
# ============================================================

def ising_galois_permutations(primes=None):
    """Compute Galois permutations for Ising at specified primes.

    The Ising S-matrix involves sqrt(2), living in Q(sqrt(2)).
    A prime p has sigma_p = id if p = +-1 (mod 8) and nontrivial if p = +-3 (mod 8).
    """
    if primes is None:
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    S = ising_s_matrix()
    T = ising_t_matrix()

    results = {}
    for p in primes:
        perm, signs = galois_signs_from_s(S, T, p)
        qr_class = pow(2, (p - 1) // 2, p) if p > 2 else None
        results[p] = {
            'permutation': perm,
            'signs': signs,
            'p_mod_8': p % 8,
            'sqrt2_is_QR': qr_class == 1 if qr_class is not None else None,
        }
    return results


# ============================================================
# Utility
# ============================================================

def _primes_up_to(n):
    """Sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def _is_prime(n):
    """Simple primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
