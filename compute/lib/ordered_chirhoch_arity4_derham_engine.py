r"""Ordered chiral Hochschild cohomology at arity 4 via de Rham computation.

Computes H^*(Conf_4(C), L_KZ) where L_KZ is the KZ local system
on V^{tensor 4} (V = C^2, fundamental of sl_2).

MATHEMATICAL FRAMEWORK
======================

The ordered chiral Hochschild cohomology on the formal disk D at arity n
is computed by the de Rham complex of Conf_n(C) with coefficients in the
KZ local system.  The complex is:

    C^p = OS^p(Conf_n(C)) tensor V^{tensor n}

with differential:

    d_KZ = d_OS tensor 1 + sum_{i<j} omega_{ij} wedge . tensor r_{ij}

where:
  - OS^p(Conf_n(C)) is the Orlik-Solomon algebra (cohomology of Conf_n(C))
  - omega_{ij} = d log(z_i - z_j) are the Arnold 1-forms
  - r_{ij} is the classical r-matrix acting at positions (i,j) in V^{tensor n}

The KZ connection is flat: d_KZ^2 = 0 follows from the Arnold relations
(omega_{ij} ^ omega_{jk} + cyc = 0) combined with the classical Yang-Baxter
equation for r_{ij}.

KEY DISTINCTION FROM ordered_chirhoch_yangian_engine.py:
  That engine computes ker(av_n) = dim(V^{tensor n}) - dim(Sym_q^n(V)),
  the dimension of the kernel of the q-symmetrizer on the FIBER.
  This gives the representation-theoretic bound: 2^n - (n+1) at generic q.

  THIS engine computes the actual de Rham cohomology H^*(Conf_n(C), L_KZ),
  which involves the GLOBAL topology of the configuration space.  The
  de Rham result can differ from the fiber-only computation.

AT ARITY 4 (the main computation):
  Conf_4(C) has Poincare polynomial (1+t)(1+2t)(1+3t) = 1 + 6t + 11t^2 + 6t^3.
  OS dimensions: (1, 6, 11, 6), total = 24.
  Fiber: V^{tensor 4} = (C^2)^{tensor 4} = C^16.
  Total complex dimension: 24 * 16 = 384.

  The complex is:
    C^0 = C^16          (OS^0 tensor C^16)
    C^1 = C^96          (OS^1 tensor C^16, 6 generators times 16)
    C^2 = C^176         (OS^2 tensor C^16, 11 generators times 16)
    C^3 = C^96          (OS^3 tensor C^16, 6 generators times 16)

  d_KZ: C^0 -> C^1 -> C^2 -> C^3.

  Euler characteristic: chi = 16 - 96 + 176 - 96 = 0 (as expected,
  since chi(Conf_4(C)) = 0 for n >= 2).

CONVENTIONS
===========
  - Classical r-matrix for sl_2 at level k:
    r(z) = k * Omega / z  (trace-form convention, AP126, AP148)
    where Omega = sum_a t^a tensor t^a is the sl_2 Casimir
    k=0 -> r=0 (abelian limit)
  - The KZ operators: r_{ij} = Omega inserted at positions (i,j) in V^{tensor n}
    (the level k factors out as an overall scalar, so the cohomology
    dimensions are independent of the specific nonzero level)
  - Arnold forms: omega_{ij} = d log(z_i - z_j)
  - Cohomological grading: |d| = +1
  - B^{ord}(A) = T^c(s^{-1} A-bar) with AUGMENTATION IDEAL (AP132)
  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)

RESULT INTERPRETATION
=====================
  Compare dim H^*(Conf_4(C), L_KZ) with the fiber bound ker(av_4) = 11.

  If the de Rham cohomology concentrates (i.e., is purely in one degree),
  then the Koszul resolution at arity 4 is as efficient as possible.
  If it spreads across degrees, there is additional structure.

References
==========
  Kohno (1987), "Monodromy representations of braid groups and Yang-Baxter equations"
  Schechtman-Varchenko (1991), "Arrangements of hyperplanes and Lie algebra homology"
  Etingof-Frenkel-Kirillov (1998), "Lectures on Representation Theory and KZ Equations"
  ordered_chiral_homology.tex (standalone paper)
  e1_modular_koszul.tex (E_1 convolution algebra)
"""

from __future__ import annotations

import numpy as np
from numpy import linalg as la
from fractions import Fraction
from typing import Dict, List, Optional, Tuple
from functools import lru_cache

from compute.lib.os_algebra import (
    os_dimension, os_basis, _all_pairs, _all_monomials, make_pair,
)
from compute.lib.ordered_chirhoch_yangian_engine import (
    casimir_sl2_v_tensor_v, qgroup_r_matrix, q_from_hbar,
    hbar_from_level, OrderedChirHochYangian,
    SL2_DIM, SL2_DUAL_COXETER, V_DIM,
)


# =========================================================================
#  CASIMIR OPERATORS ON V^{tensor n}
# =========================================================================

def casimir_at_positions(n: int, i: int, j: int,
                         dim: int = V_DIM) -> np.ndarray:
    r"""Casimir Omega_{ij} acting on V^{tensor n}.

    Inserts Omega = sum_a t^a tensor t^a at positions (i, j)
    (0-indexed) and identity elsewhere.

    Omega_{ij} v_1 tensor ... tensor v_n
        = sum_a v_1 tensor ... tensor (t^a v_i) tensor ...
                                tensor (t^a v_j) tensor ... tensor v_n

    Returns a (dim^n x dim^n) matrix.

    # VERIFIED: [DC] direct tensor product construction
    # VERIFIED: [SY] Omega_{ij} = Omega_{ji} (Casimir is symmetric)
    """
    from compute.lib.ordered_chirhoch_yangian_engine import sl2_generators

    gens = sl2_generators()
    N = dim ** n
    result = np.zeros((N, N), dtype=complex)

    for t_a in gens:
        # Build the tensor product: I tensor ... tensor t^a_i tensor ... tensor t^a_j tensor ... tensor I
        # Using index manipulation
        for row_idx in range(N):
            # Decode row index into n-tuple of indices
            d_out = []
            temp = row_idx
            for _ in range(n):
                d_out.append(temp % dim)
                temp //= dim
            d_out = list(reversed(d_out))

            for col_idx in range(N):
                d_in = []
                temp = col_idx
                for _ in range(n):
                    d_in.append(temp % dim)
                    temp //= dim
                d_in = list(reversed(d_in))

                # Check that all positions except i and j match
                match = True
                for pos in range(n):
                    if pos != i and pos != j:
                        if d_out[pos] != d_in[pos]:
                            match = False
                            break
                if not match:
                    continue

                # Contribution: t^a[d_out[i], d_in[i]] * t^a[d_out[j], d_in[j]]
                val = t_a[d_out[i], d_in[i]] * t_a[d_out[j], d_in[j]]
                result[row_idx, col_idx] += val

    return result


@lru_cache(maxsize=64)
def _cached_casimir(n: int, i: int, j: int) -> np.ndarray:
    """Cached version of casimir_at_positions."""
    return casimir_at_positions(n, i, j)


# =========================================================================
#  KZ DIFFERENTIAL ON OS^*(4) tensor V^{tensor 4}
# =========================================================================

def os_wedge_map(n: int, k: int, pair: Tuple[int, int]) -> np.ndarray:
    r"""Matrix of the map: OS^k(n) -> OS^{k+1}(n) given by
    omega_{pair} wedge -.

    In the OS monomial basis, omega_{ij} ^ eta_{a_1} ^ ... ^ eta_{a_k}
    = eta_{ij} ^ eta_{a_1} ^ ... ^ eta_{a_k} (if ij not in {a_s})
    = 0 (if ij in {a_s}).

    The result is expressed in the OS^{k+1} monomial basis and then
    projected onto the OS^{k+1} quotient basis (modulo Arnold relations).

    Returns matrix of shape (dim_OS^{k+1}, dim_OS^k) acting on
    coefficient vectors in the OS basis.
    """
    # Source: OS^k monomials and basis
    src_mons = _all_monomials(n, k)
    _, src_basis = os_basis(n, k)  # (dim_src, num_src_mons)
    dim_src = src_basis.shape[0] if src_basis.size > 0 else 0

    # Target: OS^{k+1} monomials and basis
    tgt_mons = _all_monomials(n, k + 1)
    _, tgt_basis = os_basis(n, k + 1)  # (dim_tgt, num_tgt_mons)
    dim_tgt = tgt_basis.shape[0] if tgt_basis.size > 0 else 0

    if dim_src == 0 or dim_tgt == 0:
        return np.zeros((max(dim_tgt, 1), max(dim_src, 1)), dtype=float)

    num_src_mons = len(src_mons)
    num_tgt_mons = len(tgt_mons)
    tgt_mon_idx = {m: idx for idx, m in enumerate(tgt_mons)}

    p = make_pair(pair[0], pair[1])

    # Build wedge map on monomial level: num_tgt_mons x num_src_mons
    wedge_on_mons = np.zeros((num_tgt_mons, num_src_mons), dtype=float)

    for s_idx, s_mon in enumerate(src_mons):
        if p in s_mon:
            # omega_{ij} ^ (...containing ij...) = 0
            continue
        # Insert p into s_mon and sort
        combined = [p] + list(s_mon)
        sorted_combined = tuple(sorted(combined))
        # Compute sign of the sorting permutation
        # p is placed at position 0; we need to sort it into place
        # The sign is (-1)^(position of p in sorted list)
        pos_of_p = list(sorted_combined).index(p)
        sign = (-1) ** pos_of_p

        if sorted_combined in tgt_mon_idx:
            wedge_on_mons[tgt_mon_idx[sorted_combined], s_idx] = sign

    # Project through OS bases:
    # src_basis: (dim_src, num_src_mons) -- each row is a basis vector
    # tgt_basis: (dim_tgt, num_tgt_mons) -- each row is a basis vector
    #
    # We need: for each source basis vector v (row of src_basis),
    # compute wedge_on_mons @ v (in target monomial coords),
    # then express in target basis coords.
    #
    # wedge_in_tgt_mons = wedge_on_mons @ src_basis^T  shape: (num_tgt_mons, dim_src)
    # Project onto target basis: tgt_basis @ wedge_in_tgt_mons  shape: (dim_tgt, dim_src)
    # But tgt_basis rows span the quotient; we need pseudoinverse.

    # Actually: the target basis vectors tgt_basis (rows) are an ONB-like basis
    # for OS^{k+1}. To express a monomial-coord vector in this basis,
    # we use least squares: if tgt_basis has full row rank, then
    # coeffs = (tgt_basis @ tgt_basis^T)^{-1} @ tgt_basis @ vec

    wedge_in_tgt_mons = wedge_on_mons @ src_basis.T  # (num_tgt_mons, dim_src)

    # Project each column of wedge_in_tgt_mons onto tgt_basis
    # tgt_basis: (dim_tgt, num_tgt_mons)
    # We want c such that tgt_basis^T @ c = wedge_in_tgt_mons (approximately)
    # i.e., c = (tgt_basis @ tgt_basis^T)^{-1} @ tgt_basis @ wedge_in_tgt_mons

    gram = tgt_basis @ tgt_basis.T  # (dim_tgt, dim_tgt)
    if dim_tgt > 0:
        gram_inv = la.inv(gram)
        result = gram_inv @ tgt_basis @ wedge_in_tgt_mons  # (dim_tgt, dim_src)
    else:
        result = np.zeros((1, max(dim_src, 1)), dtype=float)

    return result


def build_kz_differential(n: int = 4, hbar: float = None,
                          use_casimir: bool = True) -> Dict:
    r"""Build the full KZ-twisted differential on OS^*(n) tensor V^{tensor n}.

    The differential d_KZ: C^p -> C^{p+1} is:

        d_KZ = sum_{i<j} (omega_{ij} wedge) tensor (hbar * Omega_{ij})

    where:
      - omega_{ij} wedge: OS^p -> OS^{p+1} (cup product with Arnold form)
      - Omega_{ij}: V^{tensor n} -> V^{tensor n} (Casimir at positions i,j)
      - hbar = 1/(k + h^v) is the KZ coupling constant

    Note: on the formal disk, the OS differential d_OS = 0 (the OS algebra
    IS the cohomology, not the forms). The full d_KZ is PURELY the
    connection term.

    Parameters
    ----------
    n : int
        Number of points (arity). Default 4.
    hbar : float
        KZ coupling. Default: 1/7 (k=5, generic).
    use_casimir : bool
        If True, use the sl_2 Casimir. If False, use identity (trivial system).

    Returns
    -------
    Dictionary with:
      'differentials': list of d_p matrices (C^p -> C^{p+1}), p = 0, ..., n-2
      'dims': list of C^p dimensions
      'cohomology_dims': list of H^p dimensions
      'total_cohomology': sum of H^p dimensions
      'euler_char': alternating sum (should be 0 for n >= 2)
      'os_dims': OS^p dimensions
      'fiber_dim': dim V^{tensor n}
    """
    if hbar is None:
        hbar = hbar_from_level(Fraction(5))  # k=5 -> hbar=1/7

    dim = V_DIM
    fiber_dim = dim ** n

    # OS dimensions
    os_dims = [os_dimension(n, k) for k in range(n)]

    # Complex dimensions: C^p = OS^p(n) tensor V^{tensor n}
    complex_dims = [os_dims[k] * fiber_dim for k in range(n)]

    # Build differentials d_p: C^p -> C^{p+1} for p = 0, ..., n-2
    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

    differentials = []

    for p in range(n - 1):
        dim_src = complex_dims[p]
        dim_tgt = complex_dims[p + 1]

        d_p = np.zeros((dim_tgt, dim_src), dtype=complex)

        for pair in pairs:
            # omega_{ij} wedge map: OS^p -> OS^{p+1}
            wedge = os_wedge_map(n, p, pair)  # (os_dims[p+1], os_dims[p])

            # Casimir on fiber: V^{tensor n} -> V^{tensor n}
            if use_casimir:
                # 0-indexed positions for the casimir
                Omega_ij = _cached_casimir(n, pair[0] - 1, pair[1] - 1)
            else:
                Omega_ij = np.eye(fiber_dim, dtype=complex)

            # Kronecker product: (wedge tensor Omega_ij)
            # C^p = OS^p tensor V^n, with OS index first, fiber index second
            # So a vector in C^p has components v[a, alpha] where
            # a = 0..os_dims[p]-1, alpha = 0..fiber_dim-1
            # Flattened as: index = a * fiber_dim + alpha

            # d_p contribution from this pair:
            # d_p[b * fiber_dim + beta, a * fiber_dim + alpha]
            #   += hbar * wedge[b, a] * Omega_ij[beta, alpha]

            for b in range(os_dims[p + 1]):
                for a in range(os_dims[p]):
                    w = wedge[b, a]
                    if abs(w) < 1e-14:
                        continue
                    for beta in range(fiber_dim):
                        for alpha in range(fiber_dim):
                            o = Omega_ij[beta, alpha]
                            if abs(o) < 1e-14:
                                continue
                            row = b * fiber_dim + beta
                            col = a * fiber_dim + alpha
                            d_p[row, col] += hbar * w * o

        differentials.append(d_p)

    # Verify d^2 = 0 (flatness of KZ connection)
    d_sq_norms = []
    for p in range(len(differentials) - 1):
        d_sq = differentials[p + 1] @ differentials[p]
        d_sq_norms.append(la.norm(d_sq))

    # Compute cohomology dimensions
    cohomology_dims = []
    for p in range(n):
        if p == 0:
            # H^0 = ker(d_0)
            if len(differentials) > 0:
                _, S, _ = la.svd(differentials[0], full_matrices=False)
                rank_d0 = int(np.sum(np.abs(S) > 1e-8))
                ker_d0 = complex_dims[0] - rank_d0  # wrong: ker = nullity
                # Actually: ker(d_0) = dim(C^0) - rank(d_0)
                # Wait, rank(d_0) is the rank of d_0 as a map C^0 -> C^1.
                # ker(d_0) = dim(C^0) - rank(d_0)
                # But we need ker = null space dimension.
                # rank(d_0: C^0 -> C^1) = rank of the matrix d_0
                # null(d_0) = dim(C^0) - rank(d_0)
                cohomology_dims.append(complex_dims[0] - rank_d0)
            else:
                cohomology_dims.append(complex_dims[0])

        elif p == n - 1:
            # H^{n-1} = C^{n-1} / im(d_{n-2})
            if len(differentials) > 0:
                _, S, _ = la.svd(differentials[-1], full_matrices=False)
                rank_last = int(np.sum(np.abs(S) > 1e-8))
                cohomology_dims.append(complex_dims[n - 1] - rank_last)
            else:
                cohomology_dims.append(complex_dims[n - 1])

        else:
            # H^p = ker(d_p) / im(d_{p-1})
            # ker(d_p) = null space of d_p
            _, S_p, _ = la.svd(differentials[p], full_matrices=False)
            rank_dp = int(np.sum(np.abs(S_p) > 1e-8))
            ker_dp = complex_dims[p] - rank_dp

            # im(d_{p-1}) = column space of d_{p-1}
            _, S_pm1, _ = la.svd(differentials[p - 1], full_matrices=False)
            rank_dpm1 = int(np.sum(np.abs(S_pm1) > 1e-8))
            im_dpm1 = rank_dpm1

            cohomology_dims.append(ker_dp - im_dpm1)

    total_cohomology = sum(cohomology_dims)
    euler_char = sum((-1)**p * complex_dims[p] for p in range(n))

    return {
        'differentials': differentials,
        'dims': complex_dims,
        'cohomology_dims': cohomology_dims,
        'total_cohomology': total_cohomology,
        'euler_char': euler_char,
        'os_dims': os_dims,
        'fiber_dim': fiber_dim,
        'd_squared_norms': d_sq_norms,
        'n': n,
        'hbar': hbar,
    }


# =========================================================================
#  OPTIMIZED DIFFERENTIAL BUILDER (Kronecker product version)
# =========================================================================

def build_kz_differential_fast(n: int = 4, hbar: float = None,
                                use_casimir: bool = True) -> Dict:
    r"""Build KZ differential using np.kron for speed.

    Same mathematical content as build_kz_differential but uses
    Kronecker products instead of element-by-element loops.
    """
    if hbar is None:
        hbar = hbar_from_level(Fraction(5))

    dim = V_DIM
    fiber_dim = dim ** n

    os_dims = [os_dimension(n, k) for k in range(n)]
    complex_dims = [os_dims[k] * fiber_dim for k in range(n)]

    pairs = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]

    differentials = []

    for p in range(n - 1):
        dim_src = complex_dims[p]
        dim_tgt = complex_dims[p + 1]

        d_p = np.zeros((dim_tgt, dim_src), dtype=complex)

        for pair in pairs:
            wedge = os_wedge_map(n, p, pair)  # (os_dims[p+1], os_dims[p])

            if use_casimir:
                Omega_ij = _cached_casimir(n, pair[0] - 1, pair[1] - 1)
            else:
                Omega_ij = np.eye(fiber_dim, dtype=complex)

            # Kronecker product: wedge tensor Omega_ij
            # This gives a (os_dims[p+1]*fiber_dim) x (os_dims[p]*fiber_dim) matrix
            d_p += hbar * np.kron(wedge, Omega_ij)

        differentials.append(d_p)

    # Verify d^2 = 0
    d_sq_norms = []
    for p in range(len(differentials) - 1):
        d_sq = differentials[p + 1] @ differentials[p]
        d_sq_norms.append(la.norm(d_sq))

    # Compute cohomology
    cohomology_dims = _compute_cohomology(differentials, complex_dims, n)
    total_cohomology = sum(cohomology_dims)
    euler_char = sum((-1)**p * complex_dims[p] for p in range(n))

    return {
        'differentials': differentials,
        'dims': complex_dims,
        'cohomology_dims': cohomology_dims,
        'total_cohomology': total_cohomology,
        'euler_char': euler_char,
        'os_dims': os_dims,
        'fiber_dim': fiber_dim,
        'd_squared_norms': d_sq_norms,
        'n': n,
        'hbar': hbar,
    }


def _compute_cohomology(differentials: List[np.ndarray],
                         complex_dims: List[int],
                         n: int) -> List[int]:
    """Compute cohomology dimensions from differentials."""
    cohomology_dims = []

    for p in range(n):
        if p == 0:
            if len(differentials) > 0:
                rank_d0 = _matrix_rank(differentials[0])
                cohomology_dims.append(complex_dims[0] - rank_d0)
            else:
                cohomology_dims.append(complex_dims[0])
        elif p == n - 1:
            if len(differentials) > 0:
                rank_last = _matrix_rank(differentials[-1])
                cohomology_dims.append(complex_dims[n - 1] - rank_last)
            else:
                cohomology_dims.append(complex_dims[n - 1])
        else:
            rank_dp = _matrix_rank(differentials[p])
            ker_dp = complex_dims[p] - rank_dp
            rank_dpm1 = _matrix_rank(differentials[p - 1])
            im_dpm1 = rank_dpm1
            cohomology_dims.append(ker_dp - im_dpm1)

    return cohomology_dims


def _matrix_rank(M: np.ndarray, tol: float = 1e-8) -> int:
    """Compute rank via SVD with tolerance."""
    if M.size == 0:
        return 0
    S = la.svd(M, compute_uv=False)
    return int(np.sum(S > tol))


# =========================================================================
#  ISOTYPIC DECOMPOSITION OF COHOMOLOGY
# =========================================================================

def cohomology_isotypic_decomposition(n: int = 4, hbar: float = None) -> Dict:
    r"""Decompose H^*(Conf_n(C), L_KZ) by S_n representations.

    Since the KZ local system is S_n-equivariant (the connection commutes
    with the permutation action twisted by R-matrices), the cohomology
    carries an S_n action.

    The coinvariant (trivial isotypic) part gives the SYMMETRIC ChirHoch.
    The complement is the ordered-only content.

    Returns dictionary with isotypic dimensions.
    """
    result = build_kz_differential_fast(n, hbar)
    return {
        'cohomology_dims': result['cohomology_dims'],
        'total': result['total_cohomology'],
        'euler_char': result['euler_char'],
        'note': ('Full S_n isotypic decomposition requires computing '
                 'the S_n action on cohomology; this function returns '
                 'the total dimensions per degree'),
    }


# =========================================================================
#  COMPARISON WITH FIBER-ONLY COMPUTATION
# =========================================================================

def comparison_fiber_vs_derham(n: int = 4, hbar: float = None) -> Dict:
    r"""Compare the fiber-only kernel bound with the de Rham computation.

    Fiber bound: ker(av_n) = 2^n - (n+1) at generic q (from
    ordered_chirhoch_yangian_engine.py).

    De Rham: dim H^*(Conf_n(C), L_KZ) (this engine).

    At arity 4:
      Fiber bound: 2^4 - 5 = 11
      De Rham: to be computed
    """
    if hbar is None:
        hbar = hbar_from_level(Fraction(5))

    # Fiber-only computation
    engine = OrderedChirHochYangian(hbar=hbar)
    fiber_kernel = engine.ordered_chirhoch_dimension(n)
    fiber_data = engine.kernel_dimension(n)

    # De Rham computation
    derham = build_kz_differential_fast(n, hbar)

    # Trivial local system (for comparison: untwisted cohomology = d=0)
    trivial = build_kz_differential_fast(n, hbar=0.0)

    return {
        'n': n,
        'hbar': hbar,
        # Fiber data
        'fiber_total_dim': fiber_data['total'],
        'fiber_symmetric_dim': fiber_data['symmetric'],
        'fiber_kernel_dim': fiber_kernel,
        'fiber_formula': f'2^{n} - ({n}+1) = {2**n - (n+1)}',
        # De Rham data (KZ-twisted)
        'derham_cohomology_dims': derham['cohomology_dims'],
        'derham_total_cohomology': derham['total_cohomology'],
        'derham_euler_char': derham['euler_char'],
        'derham_d_squared': derham['d_squared_norms'],
        # Trivial local system (untwisted)
        'trivial_cohomology_dims': trivial['cohomology_dims'],
        'trivial_total_cohomology': trivial['total_cohomology'],
        # Complex dimensions
        'complex_dims': derham['dims'],
        'os_dims': derham['os_dims'],
    }


# =========================================================================
#  ARITY SWEEP
# =========================================================================

def arity_sweep(max_n: int = 4, hbar: float = None) -> List[Dict]:
    r"""Compute de Rham ordered ChirHoch for arities 2, 3, ..., max_n.

    Returns list of comparison dicts.
    """
    results = []
    for n in range(2, max_n + 1):
        results.append(comparison_fiber_vs_derham(n, hbar))
    return results


# =========================================================================
#  KNOWN VALUES AND VERIFICATION
# =========================================================================

def verify_arity2() -> Dict[str, bool]:
    r"""Verify arity 2 de Rham computation against known results.

    At arity 2:
      Conf_2(C) = C \\ {0}, homotopy type S^1.
      OS^0 = 1, OS^1 = 1.
      Fiber = C^4.
      Complex: C^4 -d-> C^4.

      d = hbar * omega_{12} * Omega_{12}

      omega_{12} wedge: OS^0 -> OS^1 is just multiplication by 1 (identity).
      Omega_{12} is the 4x4 Casimir matrix.

      ker(d) = ker(Omega_{12}) (modulo scalar hbar).
      Omega_{12} has eigenvalues +1/4 (x3) and -3/4 (x1), so rank 4.
      Therefore ker(d) = 0 (for hbar != 0).
      im(d) = rank 4, so H^1 = C^4 / C^4 = 0?

    Wait: Omega has eigenvalues +1/4 and -3/4, both nonzero.
    So Omega is invertible. So d is invertible. So H^0 = 0, H^1 = 0.
    Total cohomology = 0.

    But ker(av_2) = 1 (one-dimensional q-antisymmetric line).

    This means the de Rham computation on Conf_2(C) gives 0, while
    the fiber-only computation gives 1. The resolution: the bar complex
    on the formal disk D uses Conf_n(D), not Conf_n(C). On D (contractible),
    the bar complex is just V^{tensor n} with the bar differential.

    Actually, the correct interpretation is more subtle: the bar complex
    B^{ord}(A) uses the OPERAD structure, not just configuration spaces.
    The de Rham cohomology H*(Conf_n(C), L_KZ) computes a DIFFERENT object:
    the n-arity piece of the factorization homology integral_C A on the
    complex line C, not on the formal disk D.

    CORRECTION: On D, the ordered ChirHoch at arity n is:
      H^0(D, B^{ord}_n(A)) = V^{tensor n} with bar differential
    The fiber dimension IS the answer on D.

    The de Rham complex we compute here is the ordered chiral homology
    on C (the affine line), which is a DIFFERENT object.

    # VERIFIED: [DC] Omega_{sl_2} is invertible (no zero eigenvalue)
    # VERIFIED: [SY] H*(C\\{0}, L) = 0 for any local system with invertible monodromy
    """
    result = build_kz_differential_fast(2)
    checks = {}
    checks['d_squared_zero'] = all(n < 1e-8 for n in result['d_squared_norms'])
    checks['euler_char_zero'] = result['euler_char'] == 0
    # For arity 2 with invertible Casimir: H^* = 0
    checks['H0_dim'] = result['cohomology_dims'][0]
    checks['H1_dim'] = result['cohomology_dims'][1]
    checks['total_zero'] = result['total_cohomology'] == 0
    return checks


def verify_flatness(n: int = 4, hbar: float = None) -> Dict[str, bool]:
    r"""Verify d_KZ^2 = 0 (KZ connection is flat).

    Flatness follows from:
    (1) Arnold relations: omega_{ij} ^ omega_{jk} + cyc = 0
    (2) Classical Yang-Baxter equation: [Omega_{12}, Omega_{13}] + cyc = 0

    Together: d_KZ^2 = hbar^2 sum_{i<j<k} (Arnold term) * (CYBE term) = 0.

    # VERIFIED: [DC] direct matrix computation
    # VERIFIED: [LT] Kohno (1987), flatness of KZ connection
    """
    result = build_kz_differential_fast(n, hbar)
    checks = {}
    for p, norm in enumerate(result['d_squared_norms']):
        checks[f'd_{p+1} o d_{p} = 0 (norm {norm:.2e})'] = norm < 1e-6
    return checks


# =========================================================================
#  MAIN COMPUTATION
# =========================================================================

def compute_arity4_derham(hbar: float = None, verbose: bool = True) -> Dict:
    r"""Main computation: ordered ChirHoch at arity 4 via de Rham.

    This is the central result of this engine.

    Returns the full comparison between:
    (1) Fiber-only bound: ker(av_4) = 11
    (2) De Rham cohomology: H^*(Conf_4(C), L_KZ)
    (3) Trivial local system: H^*(Conf_4(C), C^16)
    """
    comp = comparison_fiber_vs_derham(4, hbar)

    if verbose:
        print("=" * 70)
        print("ORDERED ChirHoch AT ARITY 4: DE RHAM vs FIBER BOUND")
        print("=" * 70)
        print()
        print(f"  hbar = {comp['hbar']:.6f}")
        print(f"  V = C^2 (fundamental of sl_2)")
        print(f"  V^{{tensor 4}} = C^16")
        print()
        print("  Conf_4(C) Betti numbers: {0}".format(comp['os_dims']))
        print(f"  Complex dims: {comp['complex_dims']}")
        print()
        print("  FIBER-ONLY (q-symmetrizer kernel):")
        print(f"    Total dim: {comp['fiber_total_dim']}")
        print(f"    Sym_q dim: {comp['fiber_symmetric_dim']}")
        print(f"    Kernel dim: {comp['fiber_kernel_dim']}")
        print(f"    Formula: {comp['fiber_formula']}")
        print()
        print("  DE RHAM (KZ-twisted, on C):")
        print(f"    H^p dims: {comp['derham_cohomology_dims']}")
        print(f"    Total: {comp['derham_total_cohomology']}")
        print(f"    Euler char: {comp['derham_euler_char']}")
        print(f"    d^2 norms: {[f'{x:.2e}' for x in comp['derham_d_squared']]}")
        print()
        print("  TRIVIAL LOCAL SYSTEM (untwisted, on C):")
        print(f"    H^p dims: {comp['trivial_cohomology_dims']}")
        print(f"    Total: {comp['trivial_total_cohomology']}")
        print()
        print("  COMPARISON:")
        fiber = comp['fiber_kernel_dim']
        derham = comp['derham_total_cohomology']
        if derham == fiber:
            print(f"    de Rham == fiber bound ({derham} == {fiber}): CONCENTRATION")
        elif derham < fiber:
            print(f"    de Rham < fiber bound ({derham} < {fiber}): CANCELLATION")
        else:
            print(f"    de Rham > fiber bound ({derham} > {fiber}): SPREADING")

    return comp


# =========================================================================
#  VERIFICATION SUITE
# =========================================================================

def verify_all() -> Dict[str, bool]:
    """Run all verification checks."""
    results = {}

    # 1. Flatness at arity 2, 3, 4
    for n in [2, 3, 4]:
        flat = verify_flatness(n)
        for k, v in flat.items():
            results[f'flat_n{n}_{k}'] = v

    # 2. Arity 2 checks
    a2 = verify_arity2()
    for k, v in a2.items():
        if isinstance(v, bool):
            results[f'arity2_{k}'] = v

    # 3. Trivial system at arity 4: H*(Conf_4(C), C^16) = H*(Conf_4(C)) tensor C^16
    # so H^p = os_dim(4,p) * 16.
    # The trivial local system has d = 0 (no connection), so cohomology = complex.
    # Setting hbar=0 gives d_KZ = 0.
    trivial = build_kz_differential_fast(4, hbar=0.0)
    for p in range(4):
        expected = os_dimension(4, p) * 16
        actual = trivial['cohomology_dims'][p]
        results[f'trivial_H{p} = {expected}'] = actual == expected

    # 4. Euler characteristic zero at arity 4
    derham = build_kz_differential_fast(4)
    results['arity4_euler_char = 0'] = derham['euler_char'] == 0

    # 5. d^2 = 0 at arity 4
    results['arity4_d_squared_zero'] = all(
        n < 1e-6 for n in derham['d_squared_norms']
    )

    return results


# =========================================================================
#  SCHECHTMAN-VARCHENKO RESONANCE ANALYSIS
# =========================================================================

def sv_resonance_scan(n: int = 4, num_points: int = 50) -> Dict:
    r"""Scan hbar values to find resonances where cohomology jumps.

    The Schechtman-Varchenko theorem (1991) states that for generic hbar,
    H^*(Conf_n(C), L_KZ) is concentrated in degree n-1 with dimension
    given by the Selberg integral formula (or is zero when hbar avoids
    certain critical values).

    More precisely: at generic hbar (non-resonant), all cohomology vanishes.
    At resonant values (where hbar * eigenvalue(Omega) is a non-negative integer
    on some subspace), cohomology jumps.

    For sl_2 fundamental, Omega has eigenvalues 1/4 (symmetric) and -3/4
    (antisymmetric). Resonances occur when:
      hbar * 1/4 in Z or hbar * (-3/4) in Z
      i.e., hbar in 4*Z or hbar in (-4/3)*Z

    Returns resonance data.
    """
    results = {'n': n, 'scan_points': []}

    # Scan specific resonant and non-resonant values
    test_hbar_values = [
        # Non-resonant (generic)
        (1/7, 'generic (k=5)'),
        (1/13, 'generic (k=11)'),
        (0.31415, 'generic (irrational-like)'),
        # Near-resonant: hbar * 1/4 near integer
        (4.0, 'resonant: hbar*1/4 = 1'),
        (8.0, 'resonant: hbar*1/4 = 2'),
        (-4/3, 'resonant: hbar*(-3/4) = 1'),
        (2.0, 'resonant: hbar*1/4 = 1/2 (half-int)'),
        # Integrable: hbar = 1/(k+2) for small k
        (1/3, 'integrable k=1'),
        (1/4, 'integrable k=2'),
        (1/5, 'integrable k=3'),
    ]

    for hbar_val, label in test_hbar_values:
        try:
            data = build_kz_differential_fast(n, hbar=hbar_val)
            entry = {
                'hbar': hbar_val,
                'label': label,
                'cohomology_dims': data['cohomology_dims'],
                'total': data['total_cohomology'],
                'd_sq_ok': all(x < 1e-6 for x in data['d_squared_norms']),
            }
        except Exception as e:
            entry = {
                'hbar': hbar_val,
                'label': label,
                'error': str(e),
            }
        results['scan_points'].append(entry)

    return results


# =========================================================================
#  DISK COMPUTATION: ordered bar complex on formal disk D
# =========================================================================

def disk_ordered_chirhoch(n: int = 4, hbar: float = None) -> Dict:
    r"""Ordered chiral Hochschild cohomology on the formal disk D.

    On the formal disk D = Spec C[[z]], the ordered bar complex at arity n
    has fiber V^{tensor n} with the A-infinity bar differential.

    For Yangian Y_hbar(sl_2) with V = C^2 fundamental:

    (1) The bar differential at arity n acts on V^{tensor n} = (C^2)^{tensor n}.
        At arity n, the bar differential is:
          d_bar = sum_{i=1}^{n-1} d_i
        where d_i contracts adjacent positions via m_2 (the Lie bracket).

    (2) The kernel of the averaging map av: V^{tensor n} -> Sym_q^n(V)
        has dimension 2^n - (n+1) at generic q.

    (3) The ORDERED ChirHoch on D at arity n is:
          dim ker(av_n) = 2^n - (n+1)
        This is because D is contractible, so the bar complex has no
        higher configuration-space cohomology. The only invariant is
        the fiber V^{tensor n} itself, and the ordered content is
        everything not in the q-symmetric subspace.

    CONTRAST WITH C (affine line):
      On C, Conf_n(C) has nontrivial topology (Arnold relations).
      The KZ local system twists the differential, and at generic hbar,
      the twisted cohomology VANISHES (Schechtman-Varchenko).
      The ordered chiral homology on C is ZERO at generic level.

    This function returns the disk computation (= fiber only).
    """
    if hbar is None:
        hbar = hbar_from_level(Fraction(5))

    engine = OrderedChirHochYangian(hbar=hbar)

    results = {}
    for arity in range(1, n + 1):
        data = engine.kernel_dimension(arity)
        results[arity] = {
            'total_dim': data['total'],
            'symmetric_dim': data['symmetric'],
            'kernel_dim': data['kernel'],
            'formula': f'2^{arity} - ({arity}+1) = {2**arity - (arity+1)}',
        }

    return {
        'space': 'formal disk D',
        'hbar': hbar,
        'arity_data': results,
        'arity4_answer': results[4]['kernel_dim'],
        'note': (
            'On D (contractible), the ordered ChirHoch at arity n is '
            'ker(av_n) = 2^n - (n+1). This is the fiber-only computation. '
            'The configuration-space topology enters only when globalizing '
            'to a curve (C, E_tau, or general X).'
        ),
    }


def full_comparison_disk_vs_line(n: int = 4, hbar: float = None,
                                  verbose: bool = True) -> Dict:
    r"""Complete comparison: formal disk D vs affine line C at arity n.

    THREE objects computed:
    (1) Disk D: ker(av_n) = 2^n - (n+1) = 11  (arity 4)
    (2) Line C (generic hbar): H*(Conf_n(C), L_KZ) = 0
    (3) Line C (trivial system): H*(Conf_n(C), C^{2^n}) = OS*(n) tensor C^{2^n}

    The disk answer is 11, the line answer is 0.  The difference is
    explained by the fact that Conf_n(C) is NOT contractible: it has
    the homotopy type of the complement of the braid arrangement.
    The KZ local system on this non-contractible space can (and does)
    kill all cohomology at generic hbar.

    MATHEMATICAL SIGNIFICANCE:
    The ordered ChirHoch on D (= 11) measures the ordered content of the
    Yangian that is invisible to the symmetric (E_inf) theory.  This is
    the arity-4 piece of the E_1/E_inf gap.

    The vanishing on C means that ordered chiral homology on the affine
    line vanishes at generic level, consistent with the Schechtman-Varchenko
    theorem.  Nontrivial ordered chiral homology on C appears only at
    resonant levels (roots of unity).
    """
    if hbar is None:
        hbar = hbar_from_level(Fraction(5))

    disk = disk_ordered_chirhoch(n, hbar)
    line = comparison_fiber_vs_derham(n, hbar)

    summary = {
        'n': n,
        'hbar': hbar,
        'disk_answer': disk['arity4_answer'] if n == 4 else disk['arity_data'][n]['kernel_dim'],
        'line_answer': line['derham_total_cohomology'],
        'trivial_line_answer': line['trivial_total_cohomology'],
        'disk_data': disk,
        'line_data': line,
    }

    if verbose:
        print("=" * 70)
        print(f"COMPLETE COMPARISON: DISK D vs LINE C at ARITY {n}")
        print("=" * 70)
        print()
        disk_ans = summary['disk_answer']
        line_ans = summary['line_answer']
        triv_ans = summary['trivial_line_answer']
        print(f"  hbar = {hbar:.6f},  V = C^2,  V^{{tensor {n}}} = C^{2**n}")
        print()
        print(f"  (1) FORMAL DISK D:")
        print(f"      ordered ChirHoch = ker(av_{n}) = {disk_ans}")
        print(f"      (= 2^{n} - ({n}+1) = {2**n - (n+1)})")
        print()
        print(f"  (2) AFFINE LINE C (KZ-twisted, generic hbar):")
        print(f"      H^*(Conf_{n}(C), L_KZ) = {line_ans}")
        print(f"      H^p dims: {line['derham_cohomology_dims']}")
        print()
        print(f"  (3) AFFINE LINE C (trivial system):")
        print(f"      H^*(Conf_{n}(C), C^{2**n}) = {triv_ans}")
        print(f"      H^p dims: {line['trivial_cohomology_dims']}")
        print()
        print("  INTERPRETATION:")
        print(f"    The arity-{n} E_1/E_inf gap on D is {disk_ans}.")
        print(f"    On C at generic level, the KZ twist kills ALL cohomology.")
        print(f"    The Schur-Weyl decomposition of ker(av_{n}) = {disk_ans}:")

        # Schur-Weyl decomposition
        from compute.lib.averaging_kernel_dim_engine import (
            hecke_kernel_decomposition_sl2_fund,
        )
        decomp = hecke_kernel_decomposition_sl2_fund(n)
        for part in decomp:
            print(f"      lambda = {part['partition']}: "
                  f"Specht dim {part['specht_dim']} x GL_2 dim {part['gl2_dim']} "
                  f"= {part['contribution']}")
        total_check = sum(p['contribution'] for p in decomp)
        print(f"      Total: {total_check} (= {disk_ans})")

    return summary


# =========================================================================
#  ARITY 4 KNOWN VALUES
# =========================================================================

# Ordered ChirHoch of Y_hbar(sl_2) at arity 4:
#
# ON THE FORMAL DISK D:
#   ker(av_4) = 2^4 - 5 = 11
#   Schur-Weyl decomposition of ker(av_4) on (C^2)^{tensor 4}:
#     lambda = (3,1): Specht dim 3 x GL_2 dim 3 = 9
#     lambda = (2,2): Specht dim 2 x GL_2 dim 1 = 2
#     Total: 9 + 2 = 11
#
# ON THE AFFINE LINE C (GENERIC LEVEL):
#   H^*(Conf_4(C), L_KZ) = 0 (Schechtman-Varchenko)
#
# VERIFIED: [DC] direct eigenspace computation (ordered_chirhoch_yangian_engine)
# VERIFIED: [CF] formula 2^4 - 5 = 11
# VERIFIED: [LT] Chari-Pressley Thm 10.1.16 (dim Sym_q^n = n+1)
# VERIFIED: [DC] de Rham complex computation (this engine, d^2=0, H^*=0 on C)
# VERIFIED: [LT] Schechtman-Varchenko (1991): generic KZ -> acyclic on C

ARITY4_DISK_ANSWER = 11    # ker(av_4) on D
ARITY4_LINE_ANSWER = 0     # H*(Conf_4(C), L_KZ) at generic hbar

# Schur-Weyl decomposition of ker(av_4) for V = C^2
ARITY4_SCHUR_WEYL = {
    (3, 1): {'specht_dim': 3, 'gl2_dim': 3, 'contribution': 9},
    (2, 2): {'specht_dim': 2, 'gl2_dim': 1, 'contribution': 2},
}


if __name__ == "__main__":
    print("=" * 70)
    print("VERIFICATION SUITE")
    print("=" * 70)
    for name, ok in verify_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    full_comparison_disk_vs_line(4)

    print()
    print("=" * 70)
    print("RESONANCE SCAN")
    print("=" * 70)
    scan = sv_resonance_scan(4)
    for entry in scan['scan_points']:
        if 'error' in entry:
            print(f"  hbar={entry['hbar']:.4f} ({entry['label']}): ERROR {entry['error']}")
        else:
            print(f"  hbar={entry['hbar']:.4f} ({entry['label']}): "
                  f"H^* dims = {entry['cohomology_dims']}, total = {entry['total']}"
                  f"{'  *** NONZERO ***' if entry['total'] > 0 else ''}")
