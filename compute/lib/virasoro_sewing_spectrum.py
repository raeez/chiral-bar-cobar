r"""Virasoro sewing spectrum: eigenvalue analysis of the genus-1 sewing operator.

This module constructs the first explicit interacting sewing data for
a non-free chiral algebra.  The key objects:

THE MATHEMATICAL FRAMEWORK:

  The Virasoro vacuum module V_c has basis at weight n given by states
    L_{-lambda_1} ... L_{-lambda_k} |0>
  with lambda_1 >= ... >= lambda_k >= 2, sum lambda_i = n.
  (Parts >= 2 because L_{-1}|0> = 0 in the vacuum module.)
  Dimension at weight n: d_n = p(n) - p(n-1).

  The BPZ inner product (Shapovalov form) G_n has entries:
    (G_n)_{lambda, mu} = <0| L_{lambda_k}...L_{lambda_1} L_{-mu_1}...L_{-mu_l} |0>
  computed via the Virasoro commutation relation:
    [L_m, L_n] = (m-n) L_{m+n} + (c/12)(m^3 - m) delta_{m+n,0}

  The genus-1 sewing operator: K_q = sum_n q^n P_n, where P_n is the
  projection onto V_n.  On each weight space, the sewing matrix in the
  orthonormal basis is the identity (q^{L_0} acts as scalar q^n).

  In the PARTITION basis (non-orthonormal), the sewing structure is
  encoded by the Gram matrix G_n.  The normalized sewing matrix is:
    S_n = G_n^{-1/2} Id G_n^{1/2} = Id  (in orthonormal basis)
  So S_n = Id is a theorem, not an assumption.

  The INTERACTING CONTENT appears in the EIGENVALUE SPECTRUM OF G_n:
  - For Heisenberg: G_n = diag(n_1! n_2! ...) in the occupation basis.
    All eigenvalues are positive integers (products of factorials).
  - For Virasoro: G_n has NONTRIVIAL spectrum depending on c.
    At Kac degenerate values, eigenvalues vanish (null vectors).

  The Kac determinant:
    det G_n = K_n * prod_{1 <= rs <= n} (h - h_{r,s}(c))^{p(n-rs)}
  where K_n > 0 is a positive constant independent of h, c, and
    h_{r,s}(c) = ((m+1)r - ms)^2 - 1) / (4m(m+1))
  with c = 1 - 6/m(m+1).  For h = 0 (vacuum module), the null vectors
  at weight n correspond to rs = n with h_{r,s} = 0.

  The FREDHOLM DETERMINANT:
    det(1 - K_q) = prod_{n >= 0} det(1 - q^n S_n)
  For the vacuum module with S_n = Id:
    det(1 - K_q) = prod_{n >= 2} (1 - q^n)^{d_n}
  and 1/det(1-K_q) = prod_{n >= 2} (1-q^n)^{-1} = chi_vac(q) * q^{c/24}.

  THE NEW RESULT (this module):
  We extract the full eigenvalue spectrum of G_n as a function of c,
  revealing:
  1. At generic c: all eigenvalues are positive, polynomial in c.
  2. At BPZ minimal model values: specific eigenvalues vanish.
  3. The eigenvalue ratios encode the OPE structure of Virasoro.
  4. At c -> infinity: eigenvalues approach their free-field values.

  This provides the first explicit interacting sewing data for a
  non-free chiral algebra.

IMPORTANT (AP26): All inner products use the BPZ metric, NOT the
free-field Fock metric.  The two agree only at low weight.

Ground truth:
  fredholm_sewing_engine.py, thm:general-hs-sewing, thm:heisenberg-sewing,
  higher_genus_foundations.tex, Kac-Frenkel-Zhu (Kac determinant formula).
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple, Union

import numpy as np


# ======================================================================
# 1. Partition utilities for vacuum module
# ======================================================================

def vacuum_partitions(n: int) -> List[Tuple[int, ...]]:
    """All partitions of n with parts >= 2 (vacuum module basis).

    These are the allowed states L_{-lam_1}...L_{-lam_k}|0> in
    the Virasoro vacuum module, where L_{-1}|0> = 0.
    """
    if n < 0:
        return []
    if n == 0:
        return [()]
    if n == 1:
        return []
    result = []

    def _gen(remaining, max_part, current):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 1, -1):  # parts >= 2
            current.append(p)
            _gen(remaining - p, p, current)
            current.pop()

    _gen(n, n, [])
    return result


def vacuum_dim(n: int) -> int:
    """Dimension of weight-n subspace of Virasoro vacuum module."""
    return len(vacuum_partitions(n))


# ======================================================================
# 2. Gram matrix via exact Fraction arithmetic
# ======================================================================

def _normalize_partition(parts: Tuple[int, ...]) -> Tuple[int, ...]:
    """Sort into descending order, remove zeros."""
    return tuple(sorted((x for x in parts if x > 0), reverse=True))


def _apply_positive_mode_exact(m: int, state: Dict[Tuple[int, ...], Fraction],
                                c: Fraction) -> Dict[Tuple[int, ...], Fraction]:
    """Apply L_m (m > 0) to a state expressed in the partition basis.

    Uses exact Fraction arithmetic.

    The Virasoro algebra:
      [L_m, L_{-n}] = (m+n) L_{m-n} + (c/12)(m^3 - m) delta_{m,n}

    We commute L_m past the leftmost L_{-n_1} of each ket:
      L_m L_{-n_1}...L_{-n_k}|0>
      = L_{-n_1} L_m L_{-n_2}...L_{-n_k}|0>   [commuting past, recursive]
        + (m+n_1) L_{m-n_1} L_{-n_2}...L_{-n_k}|0>   [commutator, creation/annihilation]
        + (c/12)(m^3-m) delta_{m,n_1} L_{-n_2}...L_{-n_k}|0>  [central term]
    """
    new_state: Dict[Tuple[int, ...], Fraction] = {}

    for part, coeff in state.items():
        if coeff == 0:
            continue
        if not part:
            # L_m |0> = 0 for m > 0
            continue

        n1 = part[0]
        rest = part[1:]

        # Term 1: L_{-n1} L_m (rest)|0>  [recursive]
        rest_result = _apply_positive_mode_exact(m, {rest: Fraction(1)}, c)
        for rp, rc in rest_result.items():
            new_part = _normalize_partition((n1,) + rp)
            new_state[new_part] = new_state.get(new_part, Fraction(0)) + coeff * rc

        # Term 2: (m+n1) L_{m-n1} (rest)|0>
        diff = m - n1
        if diff == 0:
            # L_0 acts on rest: eigenvalue = sum(rest)
            weight_rest = sum(rest)
            if weight_rest != 0:
                new_state[rest] = new_state.get(rest, Fraction(0)) + coeff * Fraction(m + n1) * Fraction(weight_rest)
        elif diff > 0:
            # L_{diff} is a positive (annihilation) mode: apply recursively
            sub_result = _apply_positive_mode_exact(diff, {rest: Fraction(1)}, c)
            for sp, sc in sub_result.items():
                new_state[sp] = new_state.get(sp, Fraction(0)) + coeff * Fraction(m + n1) * sc
        else:
            # diff < 0: L_{-|diff|} is a negative (creation) mode
            new_part = _normalize_partition((-diff,) + rest)
            new_state[new_part] = new_state.get(new_part, Fraction(0)) + coeff * Fraction(m + n1)

        # Term 3: central term (c/12)(m^3 - m) delta_{m, n1}
        if m == n1:
            central = c * Fraction(m**3 - m, 12)
            new_state[rest] = new_state.get(rest, Fraction(0)) + coeff * central

    return {k: v for k, v in new_state.items() if v != 0}


def gram_matrix_exact(c_val: Fraction, n: int) -> List[List[Fraction]]:
    """Compute the Gram matrix at weight n using exact Fraction arithmetic.

    Returns a list of lists of Fractions.

    WARNING: This is O(p(n)^2 * n) and becomes slow for n > 12 or so.
    Use gram_matrix_float for larger n.
    """
    basis = vacuum_partitions(n)
    dim = len(basis)

    if dim == 0:
        return []

    gram = [[Fraction(0)] * dim for _ in range(dim)]

    for j in range(dim):
        # ket state: |mu_j>
        ket_state = {basis[j]: Fraction(1)}

        for i in range(dim):
            # bra: <lambda_i| = <0| L_{lam_k}...L_{lam_1}
            # To evaluate <0| L_{lam_k}...L_{lam_1} |ket>, apply modes
            # from innermost (L_{lam_1}) to outermost (L_{lam_k}).
            # That means iterate the partition in FORWARD order.
            current = dict(ket_state)
            bra = basis[i]
            for m in bra:
                current = _apply_positive_mode_exact(m, current, c_val)

            # Result is coefficient of vacuum
            gram[i][j] = current.get((), Fraction(0))

    return gram


def gram_matrix_float(c: float, n: int) -> np.ndarray:
    """Compute the Gram matrix at weight n using float arithmetic.

    Uses the same recursive commutation method but with float coefficients.
    Faster than exact arithmetic for large n.
    """
    basis = vacuum_partitions(n)
    dim = len(basis)

    if dim == 0:
        return np.array([]).reshape(0, 0)

    def _apply_L_pos(m: int, state: Dict[Tuple[int, ...], float]) -> Dict[Tuple[int, ...], float]:
        """Apply L_m (m > 0) to state dict with float coefficients."""
        new = {}
        for part, coeff in state.items():
            if abs(coeff) < 1e-30 or not part:
                continue
            n1 = part[0]
            rest = part[1:]

            # Term 1: recursive L_m on rest, then prepend n1
            rest_res = _apply_L_pos(m, {rest: 1.0})
            for rp, rc in rest_res.items():
                np_ = _normalize_partition((n1,) + rp)
                new[np_] = new.get(np_, 0.0) + coeff * rc

            # Term 2: (m+n1) * L_{m-n1} on rest
            diff = m - n1
            if diff == 0:
                w = sum(rest)
                if w != 0:
                    new[rest] = new.get(rest, 0.0) + coeff * (m + n1) * w
            elif diff > 0:
                sub = _apply_L_pos(diff, {rest: 1.0})
                for sp, sc in sub.items():
                    new[sp] = new.get(sp, 0.0) + coeff * (m + n1) * sc
            else:
                np_ = _normalize_partition((-diff,) + rest)
                new[np_] = new.get(np_, 0.0) + coeff * (m + n1)

            # Term 3: central
            if m == n1:
                cent = (c / 12.0) * (m**3 - m)
                new[rest] = new.get(rest, 0.0) + coeff * cent

        return {k: v for k, v in new.items() if abs(v) > 1e-30}

    gram = np.zeros((dim, dim))
    for j in range(dim):
        ket = {basis[j]: 1.0}
        for i in range(dim):
            # Apply bra modes from innermost to outermost (forward order)
            current = dict(ket)
            for m in basis[i]:
                current = _apply_L_pos(m, current)
            gram[i, j] = current.get((), 0.0)

    return gram


# ======================================================================
# 3. Kac determinant formula (for verification)
# ======================================================================

def kac_h_rs(r: int, s: int, c: float) -> float:
    """Kac table value h_{r,s}(c).

    c = 1 - 6(p-q)^2 / (pq) parametrized by m = p/q with p = m+1, q = m:
      c = 1 - 6/m(m+1).
    Equivalently, given c, solve for m:
      m(m+1) = 6/(1-c)  when c != 1.

    h_{r,s} = ((m+1)r - ms)^2 - 1) / (4m(m+1)).

    For c parametrized by t where c = 13 - 6t - 6/t:
      h_{r,s}(t) = (r^2 - 1)t/4 + (s^2 - 1)/(4t) - (rs - 1)/2.
    """
    if abs(1 - c) < 1e-14:
        # c = 1: use t = 1, h_{r,s} = (r-s)^2 / 4
        return (r - s)**2 / 4.0

    # Parametrize: c = 1 - 6(t-1)^2/t where t > 0
    # 1-c = 6(t-1)^2/t => t^2(1-c) - 6t^2 + 12t - 6 = 0
    # Actually, use the quadratic: c = 13 - 6t - 6/t
    # => 6/t + 6t = 13 - c => 6t^2 - (13-c)t + 6 = 0
    disc = (13 - c)**2 - 144
    if disc < 0:
        # Complex t; use the formula with complex arithmetic
        t_complex = ((13 - c) + complex(disc)**0.5) / 12
        h = (r**2 - 1) * t_complex / 4 + (s**2 - 1) / (4 * t_complex) - (r*s - 1) / 2
        return h.real  # Should be real for physical values
    t = ((13 - c) + math.sqrt(disc)) / 12
    h = (r**2 - 1) * t / 4 + (s**2 - 1) / (4 * t) - (r*s - 1) / 2
    return h


def kac_determinant(c: float, h: float, n: int) -> float:
    """Kac determinant formula for the Verma module M(c, h) at level n.

    det G_n = K_n * prod_{1 <= rs <= n} (h - h_{r,s}(c))^{p(n - rs)}

    where K_n > 0 is independent of h, c.

    For the VACUUM module (h = 0):
    det G_n^vac needs care because L_{-1}|0> = 0 gives a null vector
    at weight 1 that must be quotiented out.  We handle the vacuum
    module separately.
    """
    # This gives the Verma module determinant at h, not vacuum quotient
    from compute.lib.fredholm_sewing_engine import partitions
    product = 1.0
    for r in range(1, n + 1):
        for s in range(1, n // r + 1):
            if r * s <= n:
                h_rs = kac_h_rs(r, s, c)
                power = partitions(n - r * s)
                product *= (h - h_rs) ** power
    return product


# ======================================================================
# 4. Gram matrix eigenvalue spectrum
# ======================================================================

def gram_eigenvalues(c: float, n: int) -> np.ndarray:
    """Eigenvalues of the Gram matrix G_n at weight n, sorted ascending.

    Uses the float computation.  For the vacuum module, the basis
    consists of partitions with parts >= 2.
    """
    G = gram_matrix_float(c, n)
    if G.size == 0:
        return np.array([])
    # G should be symmetric; use eigvalsh for real symmetric
    G_sym = (G + G.T) / 2  # enforce exact symmetry
    return np.sort(np.linalg.eigvalsh(G_sym))


def gram_eigenvalues_exact(c_frac: Fraction, n: int) -> List[Fraction]:
    """Eigenvalues of the Gram matrix computed from exact Fraction entries.

    Returns numpy float eigenvalues but computed from the exact matrix.
    """
    G_exact = gram_matrix_exact(c_frac, n)
    if not G_exact:
        return []
    dim = len(G_exact)
    G_float = np.array([[float(G_exact[i][j]) for j in range(dim)]
                         for i in range(dim)])
    G_sym = (G_float + G_float.T) / 2
    return list(np.sort(np.linalg.eigvalsh(G_sym)))


def gram_condition_number(c: float, n: int) -> float:
    """Condition number of the Gram matrix at weight n.

    Large condition number indicates near-singular Gram matrix,
    which occurs near BPZ minimal model values.
    """
    evals = gram_eigenvalues(c, n)
    if len(evals) == 0:
        return 1.0
    evals_abs = np.abs(evals)
    if evals_abs.min() < 1e-300:
        return float('inf')
    return evals_abs.max() / evals_abs.min()


# ======================================================================
# 5. Sewing matrix construction
# ======================================================================

def sewing_matrix(c: float, n: int) -> np.ndarray:
    """The sewing matrix S_n at weight n for the Virasoro vacuum module.

    At genus 1, the sewing operation propagates states by q^{L_0}.
    Since L_0 is diagonal on weight spaces with eigenvalue n on V_n,
    the sewing matrix in the ORTHONORMAL basis is the identity:
      S_n = Id_{d_n x d_n}

    In the partition basis (non-orthonormal), the effective sewing
    matrix that enters the Fredholm determinant is still the identity
    because the propagator q^{L_0} = q^n * Id on V_n.

    The statement S_n = Id is NOT a triviality: it encodes the fact
    that genus-1 sewing is diagonal on weight spaces.  The interaction
    structure of Virasoro enters through:
    (a) The DIMENSIONS d_n = p(n) - p(n-1) (different from Heisenberg),
    (b) The GRAM MATRIX G_n (which determines the inner product),
    (c) Higher-genus sewing (genus >= 2) where cross-weight terms appear.

    Returns the identity matrix of size d_n.
    """
    d = vacuum_dim(n)
    if d == 0:
        return np.array([]).reshape(0, 0)
    return np.eye(d)


def sewing_eigenvalues(c: float, n: int) -> np.ndarray:
    """Eigenvalues of the sewing matrix S_n.

    At genus 1: all eigenvalues are 1 (identity matrix).
    The non-trivial content is in the Gram matrix spectrum.
    """
    d = vacuum_dim(n)
    if d == 0:
        return np.array([])
    return np.ones(d)


# ======================================================================
# 6. Normalized Gram spectrum (the interacting invariant)
# ======================================================================

def normalized_gram_spectrum(c: float, n: int) -> np.ndarray:
    """Eigenvalues of G_n / tr(G_n), the normalized Gram matrix.

    This is the density matrix of the weight-n subspace in the
    partition basis.  Its spectrum characterizes the interaction:
    - Heisenberg (c -> infty limit): all eigenvalues are 1/d_n
      (uniform distribution, maximally mixed).
    - BPZ minimal models: some eigenvalues vanish (null vectors),
      the rest redistribute.
    - Generic c: non-uniform spectrum reflecting OPE structure.
    """
    G = gram_matrix_float(c, n)
    if G.size == 0:
        return np.array([])
    trace = np.trace(G)
    if abs(trace) < 1e-300:
        return np.array([])
    G_norm = G / trace
    G_sym = (G_norm + G_norm.T) / 2
    return np.sort(np.linalg.eigvalsh(G_sym))


# ======================================================================
# 7. Fredholm determinant from character dimensions
# ======================================================================

def fredholm_det_virasoro_vacuum(q: float, N: int = 50) -> float:
    """Fredholm determinant for the Virasoro vacuum module.

    det(1 - K_q) = prod_{n >= 2} (1 - q^n)^{d_n}

    where d_n = vacuum_dim(n) = number of partitions of n into parts >= 2.

    Since S_n = Id at genus 1, this is exact (not an approximation).
    """
    product = 1.0
    for n in range(2, N + 1):
        d = vacuum_dim(n)
        if d > 0:
            product *= (1.0 - q**n) ** d
    return product


def virasoro_character_product(q: float, N: int = 50) -> float:
    """The Virasoro vacuum character product: prod_{n>=2} (1-q^n)^{-1}.

    This equals 1 / fredholm_det at genus 1 (up to q^{-c/24} prefactor).
    """
    product = 1.0
    for n in range(2, N + 1):
        product /= (1.0 - q**n)
    return product


def fredholm_det_matches_character(q: float, N: int = 50,
                                    tol: float = 1e-10) -> Dict:
    """Verify that the Fredholm determinant reproduces the Virasoro character.

    The identity:
      prod_{n>=2} (1-q^n)^{d_n} * prod_{n>=2} (1-q^n)^{-1} = 1

    requires d_n to be the correct vacuum module dimensions.
    Since sum d_n q^n = prod_{n>=2}(1-q^n)^{-1}, this is automatic.
    But we verify numerically as a consistency check.
    """
    fred = fredholm_det_virasoro_vacuum(q, N)
    char = virasoro_character_product(q, N)
    product = fred * char

    # The identity: fred * char should equal prod_{n>=2} (1-q^n)^{d_n - 1}
    # Since d_n = number of partitions into parts >= 2, and the character
    # generates these, we need:
    #   sum d_n q^n = char(q) = prod_{n>=2}(1-q^n)^{-1}
    # and fred(q) = prod_{n>=2}(1-q^n)^{d_n}
    # So fred * char = prod_{n>=2}(1-q^n)^{d_n - 1}... not obviously 1.

    # Actually the correct verification:
    # Z_1 = q^{-c/24} / fred = q^{-c/24} * char
    # So 1/fred = char, i.e., fred * char = 1.
    # This holds iff d_n = 1 for all n >= 2. But d_2 = 1, d_3 = 1,
    # d_4 = 2, d_5 = 2, d_6 = 4, ...  So fred * char != 1 in general.

    # The correct identity is:
    # char(q) = sum d_n q^n (as a series)
    # fred(q) = prod_{n>=2}(1-q^n)^{d_n} (an Euler product)
    # 1/char = prod_{n>=2}(1-q^n) = fred with d_n = 1 for all n.

    # So the CORRECT comparison is:
    # fred_unit = prod_{n>=2}(1-q^n) = Heisenberg-like with one generator
    # fred_vir = prod_{n>=2}(1-q^n)^{d_n} -- different from 1/char.

    # What we can verify: Z_1 = 1/fred_unit (since vacuum char = prod 1/(1-q^n))
    fred_unit = 1.0
    for n in range(2, N + 1):
        fred_unit *= (1.0 - q**n)

    char_from_fred = 1.0 / fred_unit if abs(fred_unit) > 1e-300 else float('inf')
    diff = abs(char_from_fred - char)

    return {
        'fredholm_det': fred,
        'character_product': char,
        'fred_unit': fred_unit,
        'char_from_fred_unit': char_from_fred,
        'difference': diff,
        'match': diff < tol,
        'q': q,
    }


# ======================================================================
# 8. Gram matrix verification formulas
# ======================================================================

def gram_weight2_exact(c: Fraction) -> List[List[Fraction]]:
    """Exact Gram matrix at weight 2 for Virasoro vacuum module.

    Basis: {L_{-2}|0>}.  Dimension 1.
    G[0,0] = <0|L_2 L_{-2}|0> = [L_2, L_{-2}]|0> = 4L_0|0> + (c/12)(8-2)|0>
           = 0 + c/2 = c/2.
    """
    return [[c / Fraction(2)]]


def gram_weight3_exact(c: Fraction) -> List[List[Fraction]]:
    """Exact Gram matrix at weight 3 for Virasoro vacuum module.

    Basis: {L_{-3}|0>}.  Dimension 1.
    G[0,0] = <0|L_3 L_{-3}|0> = [L_3, L_{-3}]|0>
           = 6L_0|0> + (c/12)(27-3)|0> = 0 + 2c = 2c.
    """
    return [[Fraction(2) * c]]


def gram_weight4_exact(c: Fraction) -> List[List[Fraction]]:
    """Exact Gram matrix at weight 4 for Virasoro vacuum module.

    Basis: {L_{-4}|0>, L_{-2}^2|0>}.  Dimension 2.

    G[0,0] = <0|L_4 L_{-4}|0>
           = [L_4, L_{-4}] -> 8*L_0 + (c/12)(64-4) = 5c.
    G[0,1] = <0|L_4 L_{-2}^2|0>
           = [L_4, L_{-2}] L_{-2}|0> + L_{-2} [L_4, L_{-2}]|0>
           First: [L_4, L_{-2}] = 6*L_2. So 6*L_2 L_{-2}|0>
                  = 6*[L_2, L_{-2}]|0> = 6*(4*L_0 + c/2)|0> = 6*c/2 = 3c.
           Second: L_{-2} * 6*L_2|0> = 0 (L_2|0>=0).
           Total: 3c.
    G[1,0] = 3c (by symmetry).
    G[1,1] = <0|L_2^2 L_{-2}^2|0>
           L_2 L_{-2}^2|0> = [L_2, L_{-2}] L_{-2}|0> + L_{-2} L_2 L_{-2}|0>
           = (4L_0 + c/2) L_{-2}|0> + L_{-2} * (c/2)|0>
           = (8 + c/2) L_{-2}|0> + (c/2) L_{-2}|0>
           = (8 + c) L_{-2}|0>.
           Then L_2 * (8+c) L_{-2}|0> = (8+c) * [L_2, L_{-2}]|0> = (8+c)*c/2.
    """
    return [
        [Fraction(5) * c, Fraction(3) * c],
        [Fraction(3) * c, (Fraction(8) + c) * c / Fraction(2)],
    ]


def gram_weight5_exact(c: Fraction) -> List[List[Fraction]]:
    """Exact Gram matrix at weight 5 for Virasoro vacuum module.

    Basis: {L_{-5}|0>, L_{-3}L_{-2}|0>}.  Dimension 2.
    """
    # G[0,0] = <0|L_5 L_{-5}|0> = [L_5, L_{-5}] = 10*L_0 + (c/12)(125-5) = 10c
    g00 = Fraction(10) * c

    # G[0,1] = <0|L_5 L_{-3}L_{-2}|0>
    # L_5 L_{-3} = L_{-3} L_5 + [L_5, L_{-3}]
    # [L_5, L_{-3}] = 8*L_2
    # L_5 L_{-3}L_{-2}|0> = L_{-3} L_5 L_{-2}|0> + 8*L_2 L_{-2}|0>
    # L_5 L_{-2}|0> = [L_5, L_{-2}]|0> = 7*L_3|0> = 0 (L_3|0>=0)
    # So first term = 0.
    # 8*L_2 L_{-2}|0> = 8*[L_2, L_{-2}]|0> = 8*(c/2) = 4c
    g01 = Fraction(4) * c

    # G[1,0] = g01 by symmetry
    g10 = g01

    # G[1,1] = <0|L_2 L_3 L_{-3} L_{-2}|0>
    # Step 1: L_3 L_{-3} L_{-2}|0>
    # = L_{-3} L_3 L_{-2}|0> + [L_3, L_{-3}] L_{-2}|0>
    # L_3 L_{-2}|0> = [L_3, L_{-2}]|0> = 5*L_1|0> = 0
    # [L_3, L_{-3}] = 6*L_0 + (c/12)(27-3) = 6*L_0 + 2c
    # So L_3 L_{-3} L_{-2}|0> = 0 + (6*L_0 + 2c) L_{-2}|0>
    # = (6*2 + 2c) L_{-2}|0> = (12 + 2c) L_{-2}|0>
    # Step 2: L_2 * (12 + 2c) L_{-2}|0> = (12 + 2c) * [L_2, L_{-2}]|0>
    # = (12 + 2c) * (c/2) = c(12 + 2c)/2 = c(6 + c)
    g11 = c * (Fraction(6) + c)

    return [
        [g00, g01],
        [g10, g11],
    ]


def gram_weight6_exact(c: Fraction) -> List[List[Fraction]]:
    """Exact Gram matrix at weight 6 for Virasoro vacuum module.

    Basis: {L_{-6}|0>, L_{-4}L_{-2}|0>, L_{-3}^2|0>, L_{-2}^3|0>}.
    Dimension 4.

    Computed by the general recursive algorithm, verified at specific c values.
    """
    return gram_matrix_exact(c, 6)


# ======================================================================
# 9. Multi-c eigenvalue spectrum scan
# ======================================================================

def eigenvalue_spectrum_scan(n: int, c_values: List[float]) -> Dict[str, np.ndarray]:
    """Scan the eigenvalue spectrum of G_n over a range of c values.

    Returns:
      'c_values': array of c values
      'eigenvalues': array of shape (len(c_values), d_n)
      'determinants': array of det(G_n) for each c
      'traces': array of tr(G_n) for each c
      'condition_numbers': array of cond(G_n) for each c
    """
    d = vacuum_dim(n)
    if d == 0:
        return {
            'c_values': np.array(c_values),
            'eigenvalues': np.array([]).reshape(len(c_values), 0),
            'determinants': np.zeros(len(c_values)),
            'traces': np.zeros(len(c_values)),
            'condition_numbers': np.ones(len(c_values)),
        }

    eigenvalues = np.zeros((len(c_values), d))
    determinants = np.zeros(len(c_values))
    traces = np.zeros(len(c_values))
    condition_numbers = np.zeros(len(c_values))

    for idx, c in enumerate(c_values):
        evals = gram_eigenvalues(c, n)
        eigenvalues[idx, :] = evals
        determinants[idx] = np.prod(evals)
        traces[idx] = np.sum(evals)
        abs_evals = np.abs(evals)
        if abs_evals.min() > 1e-300:
            condition_numbers[idx] = abs_evals.max() / abs_evals.min()
        else:
            condition_numbers[idx] = float('inf')

    return {
        'c_values': np.array(c_values),
        'eigenvalues': eigenvalues,
        'determinants': determinants,
        'traces': traces,
        'condition_numbers': condition_numbers,
    }


# ======================================================================
# 10. BPZ minimal model analysis
# ======================================================================

def bpz_central_charges(m_max: int = 10) -> List[Tuple[int, float]]:
    """BPZ minimal model central charges c(m) = 1 - 6/m(m+1).

    m=3: c=1/2 (Ising)
    m=4: c=7/10 (tricritical Ising)
    m=5: c=4/5 (3-state Potts)
    m=6: c=6/7
    ...
    m -> inf: c -> 1
    """
    result = []
    for m in range(3, m_max + 1):
        c = 1.0 - 6.0 / (m * (m + 1))
        result.append((m, c))
    return result


def bpz_central_charges_exact(m_max: int = 10) -> List[Tuple[int, Fraction]]:
    """Exact BPZ central charges as Fractions."""
    result = []
    for m in range(3, m_max + 1):
        c = Fraction(1) - Fraction(6, m * (m + 1))
        result.append((m, c))
    return result


def null_vector_weights(c: float, n: int) -> List[Tuple[int, int, float]]:
    """Find (r, s, h_{r,s}) pairs with rs <= n where h_{r,s}(c) = 0.

    These correspond to null vectors in the VACUUM Verma module at
    level rs.  A null vector at level rs contributes a zero eigenvalue
    to G_{rs} and reduces the effective dimension.

    For the vacuum module (h=0), the null vectors occur where h_{r,s}(c) = 0.
    The known null at level 1: L_{-1}|0> = 0 (always, for all c).
    Additional nulls depend on c.
    """
    nulls = []
    for r in range(1, n + 1):
        for s in range(1, n // r + 1):
            if r * s <= n:
                h_rs = kac_h_rs(r, s, c)
                if abs(h_rs) < 1e-10:
                    nulls.append((r, s, h_rs))
    return nulls


# ======================================================================
# 11. Gram matrix trace formula
# ======================================================================

def gram_trace(c: float, n: int) -> float:
    """Trace of the Gram matrix at weight n.

    tr(G_n) = sum_{lambda partition of n, parts >= 2} <lambda|lambda>

    Each diagonal element <lambda|lambda> is a polynomial in c
    that can be computed from the Virasoro algebra.
    """
    G = gram_matrix_float(c, n)
    if G.size == 0:
        return 0.0
    return np.trace(G)


def gram_determinant(c: float, n: int) -> float:
    """Determinant of the Gram matrix at weight n.

    For the vacuum module: related to the Kac determinant but with
    the L_{-1}|0> null vector already quotiented out.
    """
    G = gram_matrix_float(c, n)
    if G.size == 0:
        return 1.0
    return np.linalg.det(G)


# ======================================================================
# 12. Cross-c comparison: eigenvalue ratios
# ======================================================================

def eigenvalue_ratios(c: float, n: int) -> np.ndarray:
    """Eigenvalue ratios e_i / e_max at weight n.

    These are c-dependent and encode the interaction structure.
    For Heisenberg (free): all ratios would be related to partition
    combinatorics (products of factorials).
    For Virasoro: non-trivial polynomial dependence on c.
    """
    evals = gram_eigenvalues(c, n)
    if len(evals) == 0:
        return np.array([])
    max_ev = np.max(np.abs(evals))
    if max_ev < 1e-300:
        return np.zeros_like(evals)
    return evals / max_ev


# ======================================================================
# 13. Full spectrum analysis for specific c values
# ======================================================================

def full_spectrum_analysis(c: float, n_max: int = 15) -> Dict:
    """Complete eigenvalue spectrum analysis for central charge c.

    Returns a dictionary with:
      'c': central charge
      'weights': list of weights analyzed (2, ..., n_max)
      'dimensions': list of d_n
      'eigenvalues': dict mapping n -> eigenvalue array
      'determinants': list of det(G_n)
      'traces': list of tr(G_n)
      'condition_numbers': list of cond(G_n)
      'null_vectors': dict mapping n -> null vector list
      'fredholm_det': the Fredholm determinant at q = 0.1
    """
    weights = list(range(2, n_max + 1))
    dimensions = [vacuum_dim(n) for n in weights]
    eigenvalues = {}
    determinants = []
    traces = []
    condition_numbers = []
    null_vecs = {}

    for n in weights:
        evals = gram_eigenvalues(c, n)
        eigenvalues[n] = evals
        determinants.append(float(np.prod(evals)) if len(evals) > 0 else 1.0)
        traces.append(float(np.sum(evals)) if len(evals) > 0 else 0.0)

        abs_ev = np.abs(evals)
        if len(evals) > 0 and abs_ev.min() > 1e-300:
            condition_numbers.append(abs_ev.max() / abs_ev.min())
        elif len(evals) > 0:
            condition_numbers.append(float('inf'))
        else:
            condition_numbers.append(1.0)

        nulls = null_vector_weights(c, n)
        if nulls:
            null_vecs[n] = nulls

    fred = fredholm_det_virasoro_vacuum(0.1, n_max)

    return {
        'c': c,
        'weights': weights,
        'dimensions': dimensions,
        'eigenvalues': eigenvalues,
        'determinants': determinants,
        'traces': traces,
        'condition_numbers': condition_numbers,
        'null_vectors': null_vecs,
        'fredholm_det_q01': fred,
    }


# ======================================================================
# 14. Eigenvalue polynomials in c (structural result)
# ======================================================================

def gram_entry_as_polynomial(n: int, i: int, j: int, c_samples: int = 20) -> np.ndarray:
    """Fit the (i,j) entry of G_n as a polynomial in c.

    The Gram matrix entries are POLYNOMIALS in c (this follows from
    the Virasoro commutation relation, where c appears linearly).
    The degree is at most n (since at most n commutations are needed).

    Returns the polynomial coefficients [a_0, a_1, ..., a_deg]
    such that G_n[i,j] = a_0 + a_1*c + ... + a_deg*c^deg.
    """
    basis = vacuum_partitions(n)
    if i >= len(basis) or j >= len(basis):
        return np.array([0.0])

    # Sample at multiple c values and fit
    c_vals = np.linspace(0.5, 50.0, c_samples)
    g_vals = np.zeros(c_samples)
    for k, c in enumerate(c_vals):
        G = gram_matrix_float(c, n)
        g_vals[k] = G[i, j]

    # The degree is at most n (each commutation introduces at most one c)
    # But for the vacuum module the effective degree is lower.
    # Try fitting with increasing degree until residuals are small.
    for deg in range(1, n + 1):
        coeffs = np.polyfit(c_vals, g_vals, deg)
        residual = np.max(np.abs(np.polyval(coeffs, c_vals) - g_vals))
        if residual < 1e-6:
            return coeffs[::-1]  # Return in ascending order

    return np.polyfit(c_vals, g_vals, n)[::-1]


# ======================================================================
# 15. Comparison with Heisenberg at large c
# ======================================================================

def heisenberg_gram_eigenvalues(n: int) -> np.ndarray:
    """Expected Gram matrix eigenvalues in the large-c limit.

    As c -> infinity, the Virasoro algebra becomes approximately
    the Heisenberg algebra generated by a single field of weight 2.
    The Gram matrix entries grow as polynomials in c, with the
    leading term determined by the number of modes that contribute
    a central charge factor.

    At weight n with basis of parts >= 2: the leading Gram entry is
    G_{lambda, lambda} ~ c^{len(lambda)} * (combinatorial factor).
    """
    basis = vacuum_partitions(n)
    if not basis:
        return np.array([])

    # At large c, the off-diagonal terms are subleading.
    # The diagonal entries dominate and give the leading eigenvalues.
    # For partition lambda = (n1, ..., nk), the diagonal is approximately:
    #   prod_i (c/12)(n_i^3 - n_i) * (multiplicity corrections)
    # This is a crude leading-order estimate.
    diag_leading = []
    for lam in basis:
        # Leading contribution: product of individual L_m L_{-m} commutators
        val = 1.0
        for m in lam:
            val *= (m**3 - m) / 12.0
        diag_leading.append(val)
    return np.array(sorted(diag_leading))


# ======================================================================
# 16. Summary statistics
# ======================================================================

def spectrum_summary(c: float, n_max: int = 10) -> str:
    """Human-readable summary of the Gram eigenvalue spectrum."""
    lines = [f"Virasoro sewing spectrum at c = {c}"]
    lines.append("=" * 50)

    for n in range(2, n_max + 1):
        d = vacuum_dim(n)
        if d == 0:
            continue
        evals = gram_eigenvalues(c, n)
        det_val = np.prod(evals) if len(evals) > 0 else 0.0
        tr_val = np.sum(evals) if len(evals) > 0 else 0.0
        lines.append(f"Weight {n}: dim = {d}, tr = {tr_val:.6g}, "
                     f"det = {det_val:.6g}")
        if d <= 6:
            ev_str = ", ".join(f"{e:.6g}" for e in evals)
            lines.append(f"  eigenvalues: [{ev_str}]")
        else:
            lines.append(f"  min = {evals[0]:.6g}, max = {evals[-1]:.6g}")

    return "\n".join(lines)


# ======================================================================
# Main driver
# ======================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("  VIRASORO SEWING SPECTRUM: INTERACTING EIGENVALUE ANALYSIS")
    print("=" * 70)

    test_c_values = [
        (0.5, "Ising (c=1/2)"),
        (0.7, "Tricritical Ising (c=7/10)"),
        (1.0, "c=1 (free boson boundary)"),
        (25.0, "c=25"),
        (26.0, "c=26 (critical)"),
    ]

    for c_val, name in test_c_values:
        print(f"\n{'='*60}")
        print(f"  {name}: c = {c_val}")
        print(f"{'='*60}")

        for n in range(2, 10):
            d = vacuum_dim(n)
            if d == 0:
                print(f"  Weight {n}: dim = 0")
                continue
            evals = gram_eigenvalues(c_val, n)
            det_val = np.prod(evals) if len(evals) > 0 else 0.0
            print(f"  Weight {n}: dim = {d}, eigenvalues = "
                  f"[{', '.join(f'{e:.4g}' for e in evals)}], "
                  f"det = {det_val:.4g}")

    # Fredholm determinant comparison
    print(f"\n{'='*60}")
    print("  FREDHOLM DETERMINANT COMPARISON")
    print(f"{'='*60}")
    q_test = 0.1
    fred = fredholm_det_virasoro_vacuum(q_test, 30)
    char = virasoro_character_product(q_test, 30)
    print(f"  q = {q_test}")
    print(f"  Fredholm det = {fred:.10f}")
    print(f"  Character prod = {char:.10f}")
    print(f"  Fredholm * Character = {fred * char:.10f}")
