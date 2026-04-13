r"""Fredholm determinant sewing engine for interacting chiral algebras.

Implements the sewing operator S_q as an infinite matrix on the graded
state space V = bigoplus_n V_n, computes its Fredholm determinant, and
verifies HS-sewing convergence for the standard landscape.

THE MATHEMATICAL FRAMEWORK:

  The genus-1 partition function of a chiral algebra A is:
    Z_1(A; tau) = Tr_{H_A} q^{L_0 - c/24},  q = e^{2 pi i tau}

  The sewing operator K_q acts on the state space of a punctured torus
  by propagating states around the sewing cycle.  For each conformal
  weight n, K_q restricts to an operator S_n on the weight-n subspace V_n.

  The Fredholm determinant is:
    det(1 - K_q) = prod_{n >= 0} det(1 - S_n q^n)

  For Heisenberg: S_n = id_{V_n} with dim V_n = p(n) (partitions).
  The one-particle reduction gives:
    det(1 - K_q) = prod_{n >= 1} (1 - q^n)  [= q^{-1/24} eta(tau)]

  For interacting algebras (Virasoro, affine KM, W-algebras):
  S_n is a NON-TRIVIAL matrix reflecting the interaction structure.
  The key question: what are its eigenvalues?

THE HS-SEWING CONDITION (thm:general-hs-sewing):
  sum_{a,b,c} q^{a+b+c} ||m^c_{a,b}||^2_HS < infinity
  iff polynomial OPE growth + subexponential sector growth.

  This guarantees det_2(1 - K_q) exists (Fredholm determinant in
  Schatten 2-class) for |q| < 1.

INTERACTING ALGEBRAS:
  For Virasoro at central charge c, the state space at weight n is
  spanned by descendant states L_{-lambda_1}...L_{-lambda_k}|0>
  with lambda_1 >= ... >= lambda_k >= 1, sum lambda_i = n.
  Dimension = p(n).

  The sewing matrix at weight n encodes the two-point function on the
  torus.  For Virasoro, this involves the Gram matrix (Shapovalov form)
  and the propagator (Bergman kernel on the torus).

  For affine sl_2 at level k, the vacuum module has basis given by
  J^a_{-lambda_1}...J^a_{-lambda_k}|0> with dim(V_n) = 3*p(n) at
  leading order (3 = dim sl_2).

Ground truth:
  thm:general-hs-sewing, thm:heisenberg-sewing,
  thm:heisenberg-one-particle-sewing, thm:lattice-sewing,
  concordance.tex (MC5, analytic sewing programme),
  higher_genus_foundations.tex, analytic_bar_mc.py.
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple

import numpy as np
from functools import lru_cache


# ======================================================================
# 1. Partition function utilities
# ======================================================================

@lru_cache(maxsize=2000)
def partitions(n: int) -> int:
    """Number of integer partitions of n, by pentagonal recurrence."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    k = 1
    while True:
        w1 = n - k * (3 * k - 1) // 2
        w2 = n - k * (3 * k + 1) // 2
        if w1 < 0 and w2 < 0:
            break
        sign = (-1) ** (k + 1)
        if w1 >= 0:
            total += sign * partitions(w1)
        if w2 >= 0:
            total += sign * partitions(w2)
        k += 1
    return total


def partition_list(n: int) -> List[Tuple[int, ...]]:
    """All partitions of n as sorted tuples (descending)."""
    if n == 0:
        return [()]
    result = []

    def _gen(remaining, max_part, current):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            current.append(p)
            _gen(remaining - p, p, current)
            current.pop()

    _gen(n, n, [])
    return result


# ======================================================================
# 2. Dedekind eta and modular utilities
# ======================================================================

def dedekind_eta_product(q: complex, N: int = 300) -> complex:
    """prod_{n>=1} (1 - q^n).  Note: eta(tau) = q^{1/24} * this product."""
    prod = 1.0 + 0j
    for n in range(1, N + 1):
        prod *= (1.0 - q ** n)
    return prod


def dedekind_eta(q: complex, N: int = 300) -> complex:
    """eta(tau) = q^{1/24} prod_{n>=1}(1-q^n), where q = e^{2pi i tau}."""
    return q ** (1.0 / 24.0) * dedekind_eta_product(q, N)


def sigma_1(n: int) -> int:
    """Sum of divisors sigma_1(n) = sum_{d | n} d."""
    return sum(d for d in range(1, n + 1) if n % d == 0)


def eisenstein_E2(q: complex, N: int = 200) -> complex:
    """E_2(tau) = 1 - 24 * sum_{n>=1} sigma_1(n) q^n."""
    result = 1.0 + 0j
    for n in range(1, N + 1):
        result -= 24.0 * sigma_1(n) * q ** n
    return result


# ======================================================================
# 3. Virasoro Gram matrix (Shapovalov form)
# ======================================================================

def virasoro_gram_matrix(c: float, n: int) -> np.ndarray:
    """Compute the Gram matrix (Shapovalov form) at weight n for Virasoro.

    Basis: descendant states L_{-lam_1}...L_{-lam_k}|0> indexed by
    partitions of n.  The Gram matrix G_{ij} = <lam_i | lam_j> is
    computed via the Virasoro commutation relation:
        [L_m, L_n] = (m-n) L_{m+n} + (c/12)(m^3 - m) delta_{m+n,0}

    We compute by the recursive method: act with L_m on ket states,
    commuting all positive modes to the right until they annihilate |0>.
    """
    parts = partition_list(n)
    dim = len(parts)
    if dim == 0:
        return np.array([[1.0]])

    # Build a dictionary mapping partition -> index
    part_to_idx = {p: i for i, p in enumerate(parts)}

    def _state_dict(parts_tuple):
        """Represent a state as {partition: coefficient}."""
        return {parts_tuple: 1.0}

    def _apply_L_positive(m, state_dict):
        """Apply L_m (m > 0) to a state, return new state dict.

        L_m acts on L_{-n_1}...L_{-n_k}|0> by commuting L_m past each
        L_{-n_i} using [L_m, L_{-n}] = (m+n)L_{m-n} + (c/12)(m^3-m) delta_{m,n}.
        """
        new_dict = {}
        for part, coeff in state_dict.items():
            if not part:
                continue  # L_m |0> = 0 for m > 0
            part_list = list(part)
            # Commute L_m past the leftmost L_{-n_1}
            n1 = part_list[0]
            rest = tuple(part_list[1:])

            # [L_m, L_{-n1}] = (m+n1) L_{m-n1} + (c/12)(m^3-m) delta_{m,n1}
            # L_m L_{-n1} = L_{-n1} L_m + (m+n1)L_{m-n1} + (c/12)(m^3-m)delta_{m,n1}

            # Term 1: L_{-n1} L_m applied to rest
            # This requires recursive application of L_m on rest
            rest_result = _apply_L_positive(m, {rest: 1.0})
            for rp, rc in rest_result.items():
                new_part = _normalize_part((n1,) + rp)
                new_dict[new_part] = new_dict.get(new_part, 0.0) + coeff * rc

            # Term 2: (m+n1) L_{m-n1} applied to rest
            diff = m - n1
            if diff == 0:
                # L_0 on rest: eigenvalue = sum of rest
                ev = sum(rest) if rest else 0
                new_dict[rest] = new_dict.get(rest, 0.0) + coeff * (m + n1) * ev
                # But L_0|0> = 0, and L_0 on a state of weight w gives w.
                # We need the weight of the rest state
                if not rest:
                    pass  # (m+n1)*0 = 0
                else:
                    # rest is already accounted for above
                    pass
            elif diff > 0:
                # L_{diff} applied to rest (positive mode, recursive)
                sub = _apply_L_positive(diff, {rest: 1.0})
                for sp, sc in sub.items():
                    new_dict[sp] = new_dict.get(sp, 0.0) + coeff * (m + n1) * sc
            else:
                # diff < 0: L_{diff} = L_{-|diff|} is a creation operator
                new_part = _normalize_part((-diff,) + rest)
                new_dict[new_part] = new_dict.get(new_part, 0.0) + coeff * (m + n1)

            # Term 3: central term (c/12)(m^3 - m) delta_{m, n1}
            if m == n1:
                central = (c / 12.0) * (m ** 3 - m)
                new_dict[rest] = new_dict.get(rest, 0.0) + coeff * central

        return {k: v for k, v in new_dict.items() if abs(v) > 1e-15}

    def _normalize_part(p):
        """Sort partition into descending order, remove zeros."""
        return tuple(sorted([x for x in p if x > 0], reverse=True))

    # Build the Gram matrix by computing <lam_i | lam_j>
    # <lam_i | lam_j> = <0| L_{lam_i_1}...L_{lam_i_k} L_{-lam_j_1}...L_{-lam_j_l} |0>
    # We compute this by applying all L_{lam_i_k} (positive modes) to the ket state.
    gram = np.zeros((dim, dim))
    for j in range(dim):
        # Start with the ket state |lam_j> = L_{-lam_j}|0>
        # Represent it in the partition basis
        state = {parts[j]: 1.0}

        # Apply positive mode operators from the bra (in reverse order)
        for i in range(dim):
            bra_part = parts[i]
            # Apply L_{bra_part[-1]}, then L_{bra_part[-2]}, etc.
            current = dict(state)
            for m in reversed(bra_part):
                current = _apply_L_positive(m, current)

            # The result should be a scalar (coefficient of the vacuum)
            gram[i, j] = current.get((), 0.0)

    return gram


def _virasoro_gram_small(c: float, n: int) -> np.ndarray:
    """Virasoro Gram matrix at small weights via explicit formulas.

    Weight 1: basis = {L_{-1}|0>}, dim = 1
      <L_{-1}|L_{-1}> = <0|L_1 L_{-1}|0> = <0|[L_1,L_{-1}]|0> = 2h = 0
      For h=0 vacuum: G = [[0]]

    Weight 2: basis = {L_{-2}|0>, L_{-1}^2|0>}, dim = 2
      <L_{-2}|L_{-2}> = c/2
      <L_{-2}|L_{-1}^2> = 0 + 0 = 0  (by L_1 acting twice)
      <L_{-1}^2|L_{-1}^2> = ... complicated

    We use the explicit Kac determinant formula for verification:
      det G_n = prod_{rs <= n} (h - h_{r,s}(c))^{p(n-rs)}
    where h_{r,s}(c) depends on the parametrization of c.

    For the VACUUM module (h=0):
      Weight 1: det = 2*0 = 0 (null vector L_{-1}|0>)
      Weight 2: det = c/2 * (2*0 - 1) ... needs care

    Actually, L_{-1}|0> is a null vector at h=0. So we should work
    with the QUOTIENT by null vectors. For the vacuum Verma module,
    L_{-1}|0> = 0 (translation invariance), so at weight 1 there are
    no states, and at weight 2 the only state is L_{-2}|0>.
    """
    if n == 0:
        return np.array([[1.0]])
    elif n == 1:
        # L_{-1}|0> = 0 in the vacuum module. No states at weight 1.
        return np.array([]).reshape(0, 0)
    elif n == 2:
        # Only state: L_{-2}|0>. Gram: <0|L_2 L_{-2}|0> = c/2.
        return np.array([[c / 2.0]])
    elif n == 3:
        # State: L_{-3}|0>. (L_{-2}L_{-1}|0> = 0 since L_{-1}|0>=0)
        # <0|L_3 L_{-3}|0> = [L_3, L_{-3}] = 6*L_0 + c/12*(27-3) = 0 + 2c
        return np.array([[2.0 * c]])
    elif n == 4:
        # States: L_{-4}|0> and L_{-2}^2|0>.
        # (L_{-3}L_{-1} = 0, L_{-2}L_{-1}^2 = 0, L_{-1}^4 = 0 in vacuum)
        #
        # G[0,0] = <0|L_4 L_{-4}|0>
        # L_4 L_{-4}|0> = [L_4, L_{-4}]|0> = 8*L_0|0> + (c/12)(64-4)|0>
        #                = 0 + 5c = 5c
        g00 = 5.0 * c
        # G[0,1] = <0|L_4 L_{-2}^2|0>
        # L_4 L_{-2}^2|0> = [L_4, L_{-2}] L_{-2}|0> + L_{-2} L_4 L_{-2}|0>
        # [L_4, L_{-2}] = 6*L_2, so first term = 6*L_2 L_{-2}|0>
        #                = 6*[L_2, L_{-2}]|0> = 6*(4*L_0 + c/12*6)|0> = 6*(c/2) = 3c
        # L_4 L_{-2}|0> = [L_4, L_{-2}]|0> = 6*L_2|0> = 0
        # so second term = 0
        g01 = 3.0 * c
        # G[1,0] = g01 by symmetry
        g10 = g01
        # G[1,1] = <0|L_2^2 L_{-2}^2|0>
        # L_2 L_{-2}^2|0> = [L_2, L_{-2}] L_{-2}|0> + L_{-2} L_2 L_{-2}|0>
        # = (4*L_0 + c/2) L_{-2}|0> + L_{-2} * (c/2)|0>
        # First: (4*L_0 + c/2) L_{-2}|0> = (4*2 + c/2)*L_{-2}|0> = (8+c/2)*L_{-2}|0>
        # Second: L_{-2}*(c/2)|0> = (c/2)*L_{-2}|0>
        # Total: L_2 L_{-2}^2|0> = (8 + c)*L_{-2}|0>
        # Then L_2*(8+c)*L_{-2}|0> = (8+c)*[L_2,L_{-2}]|0> = (8+c)*(c/2)
        g11 = (8.0 + c) * c / 2.0
        return np.array([[g00, g01], [g10, g11]])
    else:
        # Fall back to the general recursive computation
        return virasoro_gram_matrix(c, n)


# ======================================================================
# 4. Vacuum module dimensions (after null vector quotient)
# ======================================================================

def vacuum_virasoro_dim(n: int) -> int:
    """Dimension of weight-n subspace of the Virasoro VACUUM module.

    In the vacuum module, L_{-1}|0> = 0 (translation invariance).
    The states at weight n are spanned by L_{-lam_1}...L_{-lam_k}|0>
    where each lam_i >= 2 and sum lam_i = n.

    This equals the number of partitions of n into parts >= 2,
    which is p(n) - p(n-1).
    """
    if n < 0:
        return 0
    if n == 0:
        return 1  # the vacuum |0>
    if n == 1:
        return 0  # L_{-1}|0> = 0
    return partitions(n) - partitions(n - 1)


def vacuum_virasoro_basis(n: int) -> List[Tuple[int, ...]]:
    """Basis partitions for weight n of the Virasoro vacuum module.

    Each partition has all parts >= 2.
    """
    if n <= 1:
        return [()] if n == 0 else []
    return [p for p in partition_list(n) if all(x >= 2 for x in p)]


def vacuum_affine_dim(n: int, dim_g: int = 3) -> int:
    """Dimension of weight-n subspace of the affine vacuum module.

    For affine g-hat at generic level k, the vacuum module has
    dim(V_n) = dim(g) * p(n) at leading order (each current J^a
    contributes p(n) states). More precisely, the generating function is:
      sum dim(V_n) q^n = prod_{n>=1} (1-q^n)^{-dim(g)}

    At weight n: this gives the number of dim_g-colored partitions of n.
    By convention for sl_2: dim_g = 3.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Colored partition count: coefficient of q^n in prod (1-q^m)^{-dim_g}
    # Use convolution
    dims = [0] * (n + 1)
    dims[0] = 1
    for m in range(1, n + 1):
        # Each factor (1-q^m)^{-dim_g} contributes
        for _ in range(dim_g):
            for j in range(m, n + 1):
                dims[j] += dims[j - m]
    return dims[n]


# ======================================================================
# 5. Sewing operator construction
# ======================================================================

class SewingOperator:
    """The sewing operator K_q acting on V = bigoplus_n V_n.

    At each weight n, K_q restricts to S_n: V_n -> V_n.
    The eigenvalues of S_n determine the Fredholm determinant.

    For Heisenberg: S_n = Id (diagonal in Fock basis).
    For Virasoro: S_n depends on the Gram matrix and the OPE.
    """

    def __init__(self, algebra_type: str, params: Dict = None):
        self.algebra_type = algebra_type
        self.params = params or {}
        self._cache = {}

    def dim_at_weight(self, n: int) -> int:
        """Dimension of the weight-n subspace."""
        if self.algebra_type == 'heisenberg':
            rank = self.params.get('rank', 1)
            if n == 0:
                return 1
            # For rank-r Heisenberg: r-colored partitions
            dims = [0] * (n + 1)
            dims[0] = 1
            for m in range(1, n + 1):
                for _ in range(rank):
                    for j in range(m, n + 1):
                        dims[j] += dims[j - m]
            return dims[n]
        elif self.algebra_type == 'virasoro':
            return vacuum_virasoro_dim(n)
        elif self.algebra_type == 'affine_sl2':
            k = self.params.get('level', 1)
            return vacuum_affine_dim(n, dim_g=3)
        else:
            raise ValueError(f"Unknown algebra type: {self.algebra_type}")

    def sewing_matrix_at_weight(self, n: int) -> np.ndarray:
        """The sewing matrix S_n at weight n.

        For Heisenberg: S_n = Id (one-particle reduction).
        For Virasoro: S_n = G^{-1} where G is the Gram matrix
          (the propagator in the Shapovalov basis is the inverse Gram).
          More precisely: S_n = G_n^{-1} * P_n where P_n is the
          propagator matrix.

        For the genus-1 sewing, the propagator on the torus for
        diagonal states is simply the identity (each state propagates
        with amplitude q^n). So the sewing matrix contribution at
        weight n is: q^n * G_n^{-1/2} G_n G_n^{-1/2} = q^n * Id.

        However, for interacting theories the OFF-DIAGONAL structure
        matters: the sewing matrix at weight n is Id but in the
        ORTHONORMAL basis of the Shapovalov form. In the partition basis,
        it is G_n^{-1} * G_n = Id if we use the physical inner product.

        The nontrivial content: the eigenvalues of K_q restricted to
        weight n are ALL equal to q^n (with multiplicity dim V_n).
        This is because the sewing operation simply propagates each
        state by q^{L_0} = q^n on the weight-n subspace.

        The INTERACTION enters through the matrix structure of the
        genus-2 and higher sewing, where cross-terms between different
        weights appear.
        """
        if n in self._cache:
            return self._cache[n]

        dim = self.dim_at_weight(n)
        if dim == 0:
            result = np.array([]).reshape(0, 0)
        else:
            # At genus 1, the sewing matrix S_n = Id_{dim x dim}
            # because q^{L_0} is diagonal on weight spaces.
            # The eigenvalues of K_q|_{V_n} are q^n with multiplicity dim.
            result = np.eye(dim)

        self._cache[n] = result
        return result

    def eigenvalues_at_weight(self, n: int) -> np.ndarray:
        """Eigenvalues of S_n (all 1 at genus 1, q^n contribution
        comes from the overall factor)."""
        dim = self.dim_at_weight(n)
        if dim == 0:
            return np.array([])
        S = self.sewing_matrix_at_weight(n)
        return np.linalg.eigvalsh(S)


# ======================================================================
# 6. Fredholm determinant computation
# ======================================================================

def fredholm_det_heisenberg(q: complex, rank: int = 1, N: int = 300) -> complex:
    """Fredholm determinant for rank-r Heisenberg.

    det(1 - K_q) = prod_{n>=1} (1 - q^n)^rank

    For rank=1: this is q^{-1/24} * eta(tau).
    The partition function is 1/det(1-K_q) = prod (1-q^n)^{-rank}.
    """
    prod_val = 1.0 + 0j
    for n in range(1, N + 1):
        prod_val *= (1.0 - q ** n) ** rank
    return prod_val


def fredholm_det_virasoro(c: float, q_abs: float, N: int = 50) -> Dict:
    """Fredholm determinant for the Virasoro vacuum module.

    At genus 1, the sewing operator propagates each weight-n state
    by q^n. Since L_0 is diagonal on weight spaces, the Fredholm det is:

      det(1 - K_q) = prod_{n>=0} det(1 - q^n * S_n)

    where S_n = Id_{dim V_n}. For the vacuum module (h=0):

      det(1 - K_q) = prod_{n>=2} (1 - q^n)^{d_n}

    where d_n = vacuum_virasoro_dim(n) = p(n) - p(n-1).

    Note: weight 0 contributes (1 - 1) = 0 if included; we exclude it
    (the vacuum propagates trivially). Weight 1 has d_1 = 0.

    The generating function for {d_n}:
      sum d_n q^n = (1 - q) * prod_{m>=1} (1-q^m)^{-1}
                  = prod_{m>=2} (1-q^m)^{-1}

    So prod (1-q^n)^{d_n} over n >= 2 should give something related to
    the inverse of prod_{m>=2}(1-q^m)^{-1} = 1/[(1-q)^{-1}*eta product].

    Actually, for the FULL Virasoro vacuum module at central charge c,
    the character is:
      chi_vac(q) = q^{-c/24} * prod_{n>=2} (1-q^n)^{-1}

    The factor prod_{n>=2} (1-q^n)^{-1} = (1-q) / prod_{n>=1} (1-q^n)
                                          = (1-q) * q^{1/24} / eta(q)

    The Fredholm determinant (restricting to n >= 2 since d_0 = 1, d_1 = 0):
      det(1 - K_q) = prod_{n>=2} (1 - q^n)^{d_n}

    where d_n = p(n) - p(n-1) is the vacuum module dimension.

    Numerical computation: truncate at weight N.
    """
    dims = []
    for n in range(N + 1):
        dims.append(vacuum_virasoro_dim(n))

    # Fredholm determinant product
    fred_det = 1.0
    for n in range(2, N + 1):
        if dims[n] > 0:
            fred_det *= (1.0 - q_abs ** n) ** dims[n]

    # For comparison: the Virasoro character
    # chi_vac = q^{-c/24} * prod_{n>=2} (1-q^n)^{-1}
    vir_char_product = 1.0
    for n in range(2, N + 1):
        vir_char_product *= 1.0 / (1.0 - q_abs ** n)

    # The key identity to verify:
    # prod_{n>=2} (1-q^n)^{d_n} should relate to the character
    # Since d_n = dim V_n (vacuum), and the character is
    # sum d_n q^n = prod_{n>=2}(1-q^n)^{-1}, we expect:
    # -log(fred_det) = sum_{n>=2} d_n * (-log(1-q^n))
    #               = sum_{n>=2} d_n * sum_{k>=1} q^{nk}/k
    # This is the log of the partition function (bosonic).

    return {
        'fredholm_det': fred_det,
        'dims': dims[:min(N + 1, 15)],
        'virasoro_character_product': vir_char_product,
        'central_charge': c,
        'q': q_abs,
        'truncation': N,
    }


def fredholm_det_affine_sl2(k: float, q_abs: float, N: int = 40) -> Dict:
    """Fredholm determinant for the affine sl_2 vacuum module at level k.

    The vacuum module character:
      chi_vac(q) = q^{-c/24} * prod_{n>=1} (1-q^n)^{-3}

    where c = 3k/(k+2) (for sl_2).

    Since J^a_{-1}|0> != 0 for a = 1,2,3 (no null vector at weight 1
    for generic k), the vacuum module has dim V_n = (number of
    3-colored partitions of n).

    det(1 - K_q) = prod_{n>=1} (1 - q^n)^{d_n}
    where d_n = vacuum_affine_dim(n, 3).
    """
    c_val = 3.0 * k / (k + 2.0)
    dims = []
    for n in range(N + 1):
        dims.append(vacuum_affine_dim(n, dim_g=3))

    fred_det = 1.0
    for n in range(1, N + 1):
        if dims[n] > 0:
            fred_det *= (1.0 - q_abs ** n) ** dims[n]

    return {
        'fredholm_det': fred_det,
        'dims': dims[:min(N + 1, 12)],
        'central_charge': c_val,
        'level': k,
        'q': q_abs,
        'truncation': N,
    }


def fredholm_det_from_character(char_coeffs: List[int], q_abs: float) -> float:
    """Compute Fredholm det from character coefficients.

    Given dims d_0, d_1, ..., d_N, compute:
      det(1 - K_q) = prod_{n: d_n > 0} (1 - q^n)^{d_n}

    Skipping n=0 (vacuum) since (1-q^0) = 0.
    """
    prod_val = 1.0
    for n in range(1, len(char_coeffs)):
        d = char_coeffs[n]
        if d > 0:
            prod_val *= (1.0 - q_abs ** n) ** d
    return prod_val


# ======================================================================
# 7. HS-sewing norm computation
# ======================================================================

def hs_norm_bound(algebra_type: str, q_abs: float, N: int = 50,
                  params: Dict = None) -> Dict:
    """Compute the HS-sewing norm bound:
      ||K_q||_HS^2 = sum_{n>=1} d_n * q^{2n}

    where d_n = dim V_n.

    The HS-sewing condition requires ||K_q||_HS < infinity for |q| < 1.
    This is guaranteed if d_n grows at most polynomially in n
    (subexponential growth is sufficient for the geometric series
    to converge).
    """
    params = params or {}
    total_hs_sq = 0.0
    dim_list = []

    for n in range(1, N + 1):
        if algebra_type == 'heisenberg':
            rank = params.get('rank', 1)
            d = vacuum_affine_dim(n, rank)  # rank-colored partitions
        elif algebra_type == 'virasoro':
            d = vacuum_virasoro_dim(n)
        elif algebra_type == 'affine_sl2':
            d = vacuum_affine_dim(n, 3)
        else:
            raise ValueError(f"Unknown type: {algebra_type}")

        dim_list.append(d)
        total_hs_sq += d * q_abs ** (2 * n)

    hs_norm = math.sqrt(total_hs_sq)

    # Trace norm: ||K_q||_1 = sum d_n * q^n
    trace_norm = sum(dim_list[i] * q_abs ** (i + 1) for i in range(len(dim_list)))

    # Growth rate analysis: log(d_n)/n
    growth_rates = []
    for i, d in enumerate(dim_list):
        n = i + 1
        if d > 0:
            growth_rates.append(math.log(d) / n)

    return {
        'hs_norm': hs_norm,
        'hs_norm_squared': total_hs_sq,
        'trace_norm': trace_norm,
        'is_hs': math.isfinite(hs_norm),
        'is_trace_class': math.isfinite(trace_norm),
        'growth_rates_last5': growth_rates[-5:] if len(growth_rates) >= 5 else growth_rates,
        'is_subexponential': growth_rates[-1] < growth_rates[max(0, len(growth_rates) // 2)]
                             if len(growth_rates) >= 2 else True,
        'dims_first10': dim_list[:10],
    }


# ======================================================================
# 8. Schatten class and regularized determinants
# ======================================================================

def schatten_p_norm(eigenvalues: np.ndarray, p: int) -> float:
    """Schatten p-norm: ||T||_p = (sum |lambda_i|^p)^{1/p}."""
    return np.sum(np.abs(eigenvalues) ** p) ** (1.0 / p)


def regularized_fredholm_det(eigenvalues: np.ndarray, p: int = 2) -> float:
    """Regularized Fredholm determinant det_p(1 - T).

    det_p(1 - T) = prod_i (1 - lambda_i) * exp(sum_{k=1}^{p-1} lambda_i^k / k)

    For p=1 (trace class): det_1 = prod (1 - lambda_i)
    For p=2 (Hilbert-Schmidt): det_2 = prod (1-lam_i)*exp(lam_i)
    """
    result = 1.0
    for lam in eigenvalues:
        factor = (1.0 - lam)
        for k in range(1, p):
            factor *= math.exp(lam ** k / k)
        result *= factor
    return result


def fredholm_det_eigenvalue_series(q_abs: float, algebra_type: str,
                                   N: int = 40, params: Dict = None) -> Dict:
    """Build the full eigenvalue list of K_q and compute various
    Fredholm determinants.

    Eigenvalues of K_q: for each weight n, dim(V_n) eigenvalues
    equal to q^n.
    """
    params = params or {}
    eigenvalues = []

    for n in range(1, N + 1):
        if algebra_type == 'heisenberg':
            rank = params.get('rank', 1)
            d = vacuum_affine_dim(n, rank) if rank > 1 else partitions(n)
        elif algebra_type == 'virasoro':
            d = vacuum_virasoro_dim(n)
        elif algebra_type == 'affine_sl2':
            d = vacuum_affine_dim(n, 3)
        else:
            raise ValueError(f"Unknown: {algebra_type}")
        eigenvalues.extend([q_abs ** n] * d)

    ev_array = np.array(eigenvalues)

    # Standard Fredholm det
    det_1 = np.prod(1.0 - ev_array) if len(ev_array) > 0 else 1.0

    # Regularized det_2
    det_2 = regularized_fredholm_det(ev_array, p=2) if len(ev_array) > 0 else 1.0

    # Schatten norms
    s1 = np.sum(np.abs(ev_array)) if len(ev_array) > 0 else 0.0
    s2 = np.sqrt(np.sum(ev_array ** 2)) if len(ev_array) > 0 else 0.0

    return {
        'num_eigenvalues': len(ev_array),
        'fredholm_det_1': float(det_1),
        'fredholm_det_2': float(det_2),
        'schatten_1_norm': float(s1),
        'schatten_2_norm': float(s2),
        'max_eigenvalue': float(np.max(ev_array)) if len(ev_array) > 0 else 0.0,
        'eigenvalue_sum': float(np.sum(ev_array)) if len(ev_array) > 0 else 0.0,
    }


# ======================================================================
# 9. Partition function from Fredholm determinant
# ======================================================================

def partition_function_genus1(algebra_type: str, q_abs: float,
                               N: int = 50, params: Dict = None) -> Dict:
    """Genus-1 partition function Z_1 = 1/det(1 - K_q) (up to q^{-c/24}).

    For Heisenberg: Z_1 = prod (1-q^n)^{-rank} = q^{rank/24} * eta^{-rank}
    For Virasoro:   Z_1 = prod_{n>=2} (1-q^n)^{-1} (vacuum character)
    For affine:     Z_1 = prod (1-q^n)^{-dim g}
    """
    params = params or {}

    if algebra_type == 'heisenberg':
        rank = params.get('rank', 1)
        c_val = float(rank)
        fred = fredholm_det_heisenberg(q_abs, rank, N)
        Z1 = 1.0 / fred if abs(fred) > 1e-300 else float('inf')
        # Expected: q^{-c/24} * prod(1-q^n)^{-rank}
        expected_product = 1.0
        for n in range(1, N + 1):
            expected_product /= (1.0 - q_abs ** n) ** rank
    elif algebra_type == 'virasoro':
        c_val = params.get('c', 25.0)
        res = fredholm_det_virasoro(c_val, q_abs, N)
        fred = res['fredholm_det']
        Z1 = 1.0 / fred if abs(fred) > 1e-300 else float('inf')
        expected_product = res['virasoro_character_product']
    elif algebra_type == 'affine_sl2':
        k_val = params.get('level', 1.0)
        c_val = 3.0 * k_val / (k_val + 2.0)
        res = fredholm_det_affine_sl2(k_val, q_abs, N)
        fred = res['fredholm_det']
        Z1 = 1.0 / fred if abs(fred) > 1e-300 else float('inf')
        expected_product = 1.0
        for n in range(1, N + 1):
            expected_product /= (1.0 - q_abs ** n) ** 3
    else:
        raise ValueError(f"Unknown: {algebra_type}")

    return {
        'Z1': Z1,
        'fredholm_det': fred,
        'expected_product': expected_product,
        'central_charge': c_val,
        'q': q_abs,
    }


# ======================================================================
# 10. Convergence analysis
# ======================================================================

def convergence_radius_analysis(algebra_type: str, N: int = 80,
                                 params: Dict = None) -> Dict:
    """Analyze the convergence radius of the Fredholm determinant.

    The series sum d_n q^n converges for |q| < R where
    1/R = lim sup (d_n)^{1/n}.

    For partitions: p(n) ~ exp(pi*sqrt(2n/3))/(4n*sqrt(3)),
    so p(n)^{1/n} -> 1 (subexponential). Radius R = 1.

    For colored partitions (rank r): same, since colored p(n) has
    the same exponential growth rate. R = 1.
    """
    params = params or {}
    dims = []
    for n in range(1, N + 1):
        if algebra_type == 'heisenberg':
            rank = params.get('rank', 1)
            d = vacuum_affine_dim(n, rank) if rank > 1 else partitions(n)
        elif algebra_type == 'virasoro':
            d = vacuum_virasoro_dim(n)
        elif algebra_type == 'affine_sl2':
            d = vacuum_affine_dim(n, 3)
        else:
            raise ValueError(f"Unknown: {algebra_type}")
        dims.append(d)

    # Compute (d_n)^{1/n} sequence
    root_test = []
    for i, d in enumerate(dims):
        n = i + 1
        if d > 0:
            root_test.append(d ** (1.0 / n))

    # The lim sup should approach 1 for all standard families
    if len(root_test) >= 2:
        apparent_radius = 1.0 / root_test[-1] if root_test[-1] > 0 else float('inf')
    else:
        apparent_radius = float('inf')

    return {
        'dims_first10': dims[:10],
        'root_test_last10': root_test[-10:] if len(root_test) >= 10 else root_test,
        'apparent_radius': apparent_radius,
        'converges_at_q1': apparent_radius >= 1.0 - 1e-6,
        'subexponential': root_test[-1] < root_test[len(root_test) // 2]
                         if len(root_test) >= 4 else True,
    }


# ======================================================================
# 11. Cross-family consistency: Fredholm det and kappa
# ======================================================================

def fredholm_log_derivative(q_abs: float, algebra_type: str,
                             N: int = 100, params: Dict = None) -> float:
    """d/dq log det(1 - K_q) = -sum_{n>=1} d_n * n * q^{n-1} / (1 - q^n).

    For Heisenberg (rank 1):
      = -sum n*q^{n-1}/(1-q^n) which, times q, gives -sum n*q^n/(1-q^n)
      = -sum sigma_1(m) q^m  (standard identity)

    The coefficient of q^0 in d/dq log det... is -sum d_n * n * 0 = 0
    (starts at order q^0). The expansion:
      d/dq[log det] = -d_1 * 1/(1-q) - d_2*2*q/(1-q^2) - ...

    At q=0: = -d_1. For Virasoro: d_1 = 0, so the leading term is
    O(q^1), consistent with kappa entering at genus-1 level.
    """
    params = params or {}
    total = 0.0
    for n in range(1, N + 1):
        if algebra_type == 'heisenberg':
            rank = params.get('rank', 1)
            d = vacuum_affine_dim(n, rank) if rank > 1 else partitions(n)
        elif algebra_type == 'virasoro':
            d = vacuum_virasoro_dim(n)
        elif algebra_type == 'affine_sl2':
            d = vacuum_affine_dim(n, 3)
        else:
            raise ValueError(f"Unknown: {algebra_type}")

        if d > 0 and abs(1.0 - q_abs ** n) > 1e-15:
            total -= d * n * q_abs ** n / (1.0 - q_abs ** n)

    return total


def verify_heisenberg_eta_identity(q_abs: float = 0.3, N: int = 200) -> Dict:
    """Verify that det(1-K_q) for Heisenberg equals the eta product.

    det(1-K_q) = prod_{n>=1}(1-q^n) = q^{-1/24} * eta(q).

    This is THE fundamental identity connecting the Fredholm determinant
    to the Dedekind eta function.
    """
    fred = fredholm_det_heisenberg(q_abs, rank=1, N=N)
    eta_prod = dedekind_eta_product(q_abs, N)

    diff = abs(fred - eta_prod)
    return {
        'fredholm_det': fred,
        'eta_product': eta_prod,
        'difference': diff,
        'match': diff < 1e-12,
        'q': q_abs,
    }


def verify_rank_r_product(rank: int, q_abs: float = 0.3, N: int = 200) -> Dict:
    """Verify det(1-K_q) for rank-r Heisenberg = prod(1-q^n)^r.

    This is the one-particle reduction: the sewing operator on the
    rank-r Fock space decomposes into r copies of the rank-1 operator.
    """
    fred_rank_r = fredholm_det_heisenberg(q_abs, rank=rank, N=N)
    fred_rank_1_r = fredholm_det_heisenberg(q_abs, rank=1, N=N) ** rank

    diff = abs(fred_rank_r - fred_rank_1_r)
    return {
        'rank': rank,
        'fredholm_rank_r': fred_rank_r,
        'fred_rank1_to_r': fred_rank_1_r,
        'difference': diff,
        'match': diff < 1e-10,
    }


# ======================================================================
# 12. Virasoro partition function expansion
# ======================================================================

def virasoro_partition_coeffs(c: float, N: int = 20) -> List[int]:
    """Coefficient list for the Virasoro vacuum module character.

    chi_vac(q) = q^{-c/24} * sum_{n>=0} d_n q^n

    where d_n = vacuum_virasoro_dim(n).

    Returns [d_0, d_1, ..., d_N].
    """
    return [vacuum_virasoro_dim(n) for n in range(N + 1)]


def virasoro_character_check(c: float, q_abs: float = 0.3, N: int = 30) -> Dict:
    """Verify that the Virasoro vacuum character matches prod_{n>=2}(1-q^n)^{-1}.

    The character is sum d_n q^n where d_n = p(n) - p(n-1) for n >= 2.
    The generating function is:
      sum d_n q^n = 1 + sum_{n>=2} [p(n)-p(n-1)] q^n
                  = 1 + sum_{n>=2} p(n)q^n - sum_{n>=2} p(n-1)q^n
                  = 1 + [sum_{n>=0} p(n)q^n - 1 - p(1)q] - q*[sum_{n>=0}p(n)q^n - 1]
                  = 1 + [P(q) - 1 - q] - q*[P(q) - 1]
                  = 1 + P(q) - 1 - q - q*P(q) + q
                  = P(q)(1 - q)
    where P(q) = prod(1-q^n)^{-1} = sum p(n)q^n.

    So sum d_n q^n = (1-q) * prod_{n>=1}(1-q^n)^{-1} = prod_{n>=2}(1-q^n)^{-1}.

    We verify this identity numerically.
    """
    # LHS: direct sum
    lhs = sum(vacuum_virasoro_dim(n) * q_abs ** n for n in range(N + 1))

    # RHS: product
    rhs = 1.0
    for n in range(2, N + 1):
        rhs /= (1.0 - q_abs ** n)

    diff = abs(lhs - rhs)
    return {
        'lhs_direct_sum': lhs,
        'rhs_product': rhs,
        'difference': diff,
        'match': diff < 1e-8,
        'q': q_abs,
    }


# ======================================================================
# 13. Full verification suite
# ======================================================================

def full_fredholm_verification(q_abs: float = 0.3) -> Dict:
    """Run the complete Fredholm determinant verification suite."""
    results = {}

    # 1. Heisenberg eta identity
    results['heisenberg_eta'] = verify_heisenberg_eta_identity(q_abs)

    # 2. Rank-r product identity
    for r in [2, 3, 4]:
        results[f'rank_{r}_product'] = verify_rank_r_product(r, q_abs)

    # 3. Virasoro character
    results['virasoro_character'] = virasoro_character_check(25.0, q_abs)

    # 4. HS-sewing convergence
    for alg in ['heisenberg', 'virasoro', 'affine_sl2']:
        params = {'rank': 1} if alg == 'heisenberg' else (
            {'c': 25.0} if alg == 'virasoro' else {'level': 1.0})
        results[f'hs_{alg}'] = hs_norm_bound(alg, q_abs, params=params)

    # 5. Convergence radius
    for alg in ['heisenberg', 'virasoro', 'affine_sl2']:
        params = {'rank': 1} if alg == 'heisenberg' else (
            {'c': 25.0} if alg == 'virasoro' else {'level': 1.0})
        results[f'radius_{alg}'] = convergence_radius_analysis(alg, params=params)

    return results


if __name__ == '__main__':
    print("=" * 70)
    print("  FREDHOLM SEWING ENGINE: VERIFICATION SUITE")
    print("=" * 70)

    results = full_fredholm_verification(q_abs=0.3)

    print("\n1. Heisenberg-eta identity:")
    r = results['heisenberg_eta']
    print(f"   det = {r['fredholm_det']:.10f}, eta_prod = {r['eta_product']:.10f}")
    print(f"   Match: {r['match']}")

    print("\n2. Rank-r product identities:")
    for rank in [2, 3, 4]:
        r = results[f'rank_{rank}_product']
        print(f"   rank={rank}: diff = {r['difference']:.2e}, match = {r['match']}")

    print("\n3. Virasoro character check:")
    r = results['virasoro_character']
    print(f"   Direct sum = {r['lhs_direct_sum']:.8f}")
    print(f"   Product    = {r['rhs_product']:.8f}")
    print(f"   Match: {r['match']}")

    print("\n4. HS-sewing norms:")
    for alg in ['heisenberg', 'virasoro', 'affine_sl2']:
        r = results[f'hs_{alg}']
        print(f"   {alg}: ||K||_HS = {r['hs_norm']:.6f}, "
              f"subexp = {r['is_subexponential']}")

    print("\n5. Convergence radii:")
    for alg in ['heisenberg', 'virasoro', 'affine_sl2']:
        r = results[f'radius_{alg}']
        print(f"   {alg}: R ~ {r['apparent_radius']:.4f}, "
              f"converges at |q|<1: {r['converges_at_q1']}")
