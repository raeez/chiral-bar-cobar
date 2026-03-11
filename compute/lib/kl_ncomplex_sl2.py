"""KL N-complex structure for u_q(sl_2) at roots of unity.

Fills structural gap H4: at admissible levels k = -h^v + p/q, the quantum
group parameter q = e^{2 pi i / N} is a root of unity. This module builds
the small quantum group u_q(sl_2), its bar complex, and studies the bar
cohomology / N-complex structure in connection with the Kazhdan-Lusztig
equivalence programme (MC3 / Front E).

Mathematical content:

  The SMALL quantum group u_q(sl_2) at q = e^{2 pi i / N} (N >= 2) is the
  finite-dimensional Hopf algebra with generators E, F, K satisfying:

    K^N = 1,  E^N = 0,  F^N = 0,
    K E = q^2 E K,  K F = q^{-2} F K,
    E F - F E = (K - K^{-1}) / (q - q^{-1}).

  The PBW basis is {E^a K^b F^c : 0 <= a, b, c <= N-1}, giving
  dim u_q(sl_2) = N^3.

  BAR COMPLEX:

    The (reduced) bar complex B_n(u_q) = I^{otimes n} where I = ker(epsilon)
    is the augmentation ideal. The bar differential d: B_n -> B_{n-1} is:

      d(h_1 | ... | h_n) = sum_{i=1}^{n-1} (-1)^{i+1}
          h_1 | ... | (h_i * h_{i+1}) | ... | h_n

    As u_q is associative, d^2 = 0 always. The bar cohomology
    H^n(u_q) = Ext^n_{u_q}(C, C) computes extensions of the trivial module.

  N-COMPLEX STRUCTURE (Kapranov):

    The N-complex arises not from the bar differential itself (which always
    has d^2 = 0) but from the q-de Rham differential on the quantum group.
    The quantum de Rham complex of u_q has differential D satisfying:

      D^N = 0  but  D^2 != 0  (for N >= 3).

    This gives multiple cohomology flavors:
      H^{j, N-j} = ker(D^j) / im(D^{N-j})  for 1 <= j <= N-1.

    For this module, we construct the QUANTUM DIFFERENTIAL as a q-deformed
    version of the bar differential: the q-bar differential d_q acts on
    B_n = I^{otimes n} by:

      d_q(h_1 | ... | h_n) = sum_{i=1}^{n-1} q^{i-1}
          h_1 | ... | (h_i * h_{i+1}) | ... | h_n

    where the signs (-1)^{i+1} of the classical bar differential are
    replaced by q-weights q^{i-1}. This is the Kapranov-Dubois-Violette
    prescription: the N-complex differential uses q-signs instead of
    ordinary signs. Since q^N = 1, the identity d_q^N = 0 follows from
    the quantum binomial theorem: [N choose k]_q = 0 for 1 <= k <= N-1.

  BAR COHOMOLOGY AT ROOTS OF UNITY:

    The bar cohomology H^*(u_q, C) is isomorphic to Ext^*_{u_q}(C, C).
    At roots of unity, this has special structure:

    1. For generic q: u_q(sl_2) is semisimple, bar cohomology concentrated
       in degree 0.
    2. At roots of unity: u_q(sl_2) is NOT semisimple, and the bar
       cohomology is nontrivial in multiple degrees.
    3. The Ext algebra has periodicity related to the root of unity order.
    4. For sl_2: H^2(u_q, C) = Ext^2(C, C) has dimension related to
       the complexity of the representation theory.

  KEY PREDICTIONS:
    - d_q^N = 0 (N-complex structure via q-signs)
    - d_q^2 != 0 for N >= 3 (genuinely not a chain complex)
    - Bar cohomology H^*(u_q) nontrivial in multiple degrees at roots of unity
    - N-complex cohomology flavors give refined invariants

CONVENTIONS:
  - Cohomological grading: |d| = +1.
  - q = e^{2 pi i / N} is the primitive N-th root of unity.
  - PBW ordered basis: E^a K^b F^c, ordered lexicographically in (a, b, c).
  - dim u_q(sl_2) = N^3.

References:
  - concordance.tex, H4 gap: KL N-complex structure
  - Kapranov, "On the q-analog of homological algebra" (1996)
  - Dubois-Violette, "d^N = 0: generalized homology" (1998)
  - yangians.tex, sec:cat-O-strategies (MC3 programme)
  - Chari-Pressley, "A Guide to Quantum Groups"
  - Ginzburg-Kumar, "Cohomology of quantum groups at roots of unity" (1993)
"""

from __future__ import annotations

import cmath
from typing import Dict, List, Optional, Tuple

import numpy as np


# ---------------------------------------------------------------------------
# Quantum arithmetic at roots of unity
# ---------------------------------------------------------------------------

def root_of_unity(N: int) -> complex:
    """Primitive N-th root of unity: q = e^{2 pi i / N}."""
    return cmath.exp(2j * cmath.pi / N)


def q_integer(n: int, q: complex) -> complex:
    """Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}).

    At q = e^{2 pi i / N}: [n]_q = sin(2 pi n / N) / sin(2 pi / N).
    Note [N]_q = 0 at an N-th root of unity.
    """
    if abs(q - 1.0) < 1e-14:
        return complex(n)
    denom = q - q**(-1)
    if abs(denom) < 1e-14:
        return complex(n)
    return (q**n - q**(-n)) / denom


def q_number(n: int, q: complex) -> complex:
    """Shorthand for quantum integer [n]_q."""
    return q_integer(n, q)


def q_binomial(n: int, k: int, q: complex) -> complex:
    """Quantum binomial coefficient [n choose k]_q.

    [n choose k]_q = [n]!_q / ([k]!_q [n-k]!_q).

    Key property at roots of unity: [N choose k]_q = 0 for 1 <= k <= N-1
    when q^N = 1, which is the mechanism behind d_q^N = 0.
    """
    if k < 0 or k > n:
        return complex(0)
    if k == 0 or k == n:
        return complex(1)
    # Compute [n]! / ([k]! [n-k]!)
    num = complex(1)
    for j in range(1, n + 1):
        num *= q_integer(j, q)
    den_k = complex(1)
    for j in range(1, k + 1):
        den_k *= q_integer(j, q)
    den_nk = complex(1)
    for j in range(1, n - k + 1):
        den_nk *= q_integer(j, q)
    den = den_k * den_nk
    if abs(den) < 1e-14:
        # At roots of unity, use the limiting formula or return 0
        return complex(0)
    return num / den


# ---------------------------------------------------------------------------
# Small quantum group u_q(sl_2)
# ---------------------------------------------------------------------------

class SmallQuantumSl2:
    """The small quantum group u_q(sl_2) at q = e^{2 pi i / N}.

    Generators: E, F, K with relations
        K^N = 1,  E^N = 0,  F^N = 0,
        K E = q^2 E K,  K F = q^{-2} F K,
        E F - F E = (K - K^{-1}) / (q - q^{-1}).

    PBW basis: {E^a K^b F^c : 0 <= a, b, c <= N-1}.
    Dimension: N^3.

    Basis ordering: lexicographic in (a, b, c), so the index of
    E^a K^b F^c is a * N^2 + b * N + c.
    """

    def __init__(self, N: int):
        if N < 2:
            raise ValueError(f"N must be >= 2, got {N}")
        self.N = N
        self.q = root_of_unity(N)
        self.dim = N ** 3

    def basis_index(self, a: int, b: int, c: int) -> int:
        """Index of the PBW basis element E^a K^b F^c.

        Args:
            a: power of E (0 <= a <= N-1)
            b: power of K (0 <= b <= N-1)
            c: power of F (0 <= c <= N-1)

        Returns:
            Integer index in {0, ..., N^3 - 1}.
        """
        N = self.N
        return a * N * N + b * N + c

    def basis_label(self, idx: int) -> Tuple[int, int, int]:
        """Inverse of basis_index: returns (a, b, c) for a given index."""
        N = self.N
        a = idx // (N * N)
        remainder = idx % (N * N)
        b = remainder // N
        c = remainder % N
        return (a, b, c)

    def multiplication_table(self) -> np.ndarray:
        """Compute the full multiplication table as structure constants.

        Returns:
            M: array of shape (dim, dim, dim) where
               M[i, j, k] = coefficient of basis element k in
               (basis element i) * (basis element j).

        The product E^a K^b F^c * E^{a'} K^{b'} F^{c'} is computed by
        commuting K past E and F past E using the relations, then
        reducing modulo E^N = F^N = 0 and K^N = 1.
        """
        N = self.N
        dim = self.dim
        M = np.zeros((dim, dim, dim), dtype=complex)

        for i in range(dim):
            a1, b1, c1 = self.basis_label(i)
            for j in range(dim):
                a2, b2, c2 = self.basis_label(j)
                product = self._multiply_pbw(a1, b1, c1, a2, b2, c2)
                for (ap, bp, cp), coeff in product.items():
                    if 0 <= ap < N and 0 <= bp < N and 0 <= cp < N:
                        k = self.basis_index(ap, bp, cp)
                        M[i, j, k] += coeff
        return M

    def _multiply_pbw(self, a1: int, b1: int, c1: int,
                      a2: int, b2: int, c2: int) -> Dict[Tuple[int, int, int], complex]:
        """Multiply two PBW basis elements and express result in PBW basis.

        (E^a1 K^b1 F^c1) * (E^a2 K^b2 F^c2)

        Strategy:
          1. Commute K^b1 past F^c1 (already in PBW order).
          2. Commute F^c1 past E^a2 using the EF commutation relation.
          3. Commute K^{b1} past E^{a2}: K E = q^2 E K.
          4. Combine powers and reduce modulo E^N = F^N = 0, K^N = 1.

        Returns dict from (a, b, c) -> coefficient (after reduction).
        """
        N = self.N
        q = self.q

        # Compute F^c1 * E^a2 in PBW basis
        fe_product = self._commute_F_past_E(c1, a2)

        result: Dict[Tuple[int, int, int], complex] = {}

        for (ae, bk, cf), coeff in fe_product.items():
            # Now we have E^a1 K^b1 * (E^ae K^bk F^cf) * K^b2 F^c2

            # Commute K^b1 past E^ae:
            # K^b1 E^ae = q^{2 b1 ae} E^ae K^b1
            phase_ke = q ** (2 * b1 * ae)

            total_a = a1 + ae
            total_b_left = (b1 + bk) % N

            # Commute F^cf past K^b2:
            # F^cf K^b2 = q^{2 cf b2} K^b2 F^cf
            #   (FK = q^2 KF, so F^c K^b = q^{2cb} K^b F^c)
            phase_fk = q ** (2 * cf * b2)

            total_b = (total_b_left + b2) % N
            total_c = cf + c2

            # Reduce: E^N = 0, F^N = 0, K^N = 1
            if total_a >= N or total_c >= N:
                continue  # nilpotent truncation

            total_coeff = coeff * phase_ke * phase_fk
            key = (total_a, total_b, total_c)
            result[key] = result.get(key, 0) + total_coeff

        return result

    def _commute_F_past_E(self, c: int, a: int) -> Dict[Tuple[int, int, int], complex]:
        """Express F^c * E^a in PBW basis {E^? K^? F^?}.

        Uses the relation F E = E F + (K^{-1} - K) / (q - q^{-1}).
        Recursion on a: F^c E^a = (F^c E^{a-1}) * E.

        Returns dict (ae, bk, cf) -> coefficient.
        """
        N = self.N

        if c == 0 or a == 0:
            return {(a, 0, c): complex(1)}

        # Induction on a: F^c E^a = (F^c E^{a-1}) * E
        current: Dict[Tuple[int, int, int], complex] = {(0, 0, c): complex(1)}

        for _ in range(a):
            new_current: Dict[Tuple[int, int, int], complex] = {}
            for (ae, bk, cf), coeff in current.items():
                if abs(coeff) < 1e-15:
                    continue
                # Compute E^ae K^bk F^cf * E = E^ae K^bk * (F^cf E)
                fe_terms = self._commute_Fc_past_single_E(cf)
                for (ae2, bk2, cf2), coeff2 in fe_terms.items():
                    # E^ae * K^bk * E^ae2 K^bk2 F^cf2
                    # Commute K^bk past E^ae2
                    phase = self.q ** (2 * bk * ae2)
                    total_a = ae + ae2
                    total_b = (bk + bk2) % N
                    total_c = cf2
                    if total_a >= N or total_c >= N:
                        continue
                    key = (total_a, total_b, total_c)
                    new_current[key] = new_current.get(key, 0) + coeff * coeff2 * phase
            current = new_current

        return current

    def _commute_Fc_past_single_E(self, c: int) -> Dict[Tuple[int, int, int], complex]:
        """Express F^c * E in PBW basis.

        Uses F E = EF + (K^{-1} - K) / (q - q^{-1}).
        Recursion: F^c E = (F^{c-1} E) F + F^{c-1} (K^{-1} - K) / (q - q^{-1}).
        """
        N = self.N
        q = self.q

        if c == 0:
            return {(1, 0, 0): complex(1)}

        prev = self._commute_Fc_past_single_E(c - 1)

        result: Dict[Tuple[int, int, int], complex] = {}

        # Term 1: (F^{c-1} E) * F
        for (ae, bk, cf), coeff in prev.items():
            new_c = cf + 1
            if new_c >= N:
                continue  # F^N = 0
            key = (ae, bk, new_c)
            result[key] = result.get(key, 0) + coeff

        # Term 2: F^{c-1} * (K^{-1} - K) / (q - q^{-1})
        # F^m K = q^{2m} K F^m  (from FK = q^2 KF)
        # F^m K^{-1} = q^{-2m} K^{-1} F^m  (from FK^{-1} = q^{-2} K^{-1} F)
        denom = q - q**(-1)
        if abs(denom) < 1e-14:
            # N = 2 case: q = -1, denom = 0.
            # At N = 2, K = K^{-1}, so K^{-1} - K = 0.
            # The correction term vanishes: FE = EF.
            pass
        else:
            new_c2 = c - 1
            if new_c2 < N:
                # F^{c-1} K^{-1} = q^{-2(c-1)} K^{-1} F^{c-1}
                phase_kinv = q ** (-2 * (c - 1))
                b_kinv = (-1) % N  # K^{-1} = K^{N-1}
                coeff_kinv = phase_kinv / denom
                key_kinv = (0, b_kinv, new_c2)
                result[key_kinv] = result.get(key_kinv, 0) + coeff_kinv

                # -F^{c-1} K = -q^{2(c-1)} K F^{c-1}
                phase_k = q ** (2 * (c - 1))
                b_k = 1 % N
                coeff_k = -phase_k / denom
                key_k = (0, b_k, new_c2)
                result[key_k] = result.get(key_k, 0) + coeff_k

        return result

    def unit_vector(self) -> np.ndarray:
        """The unit element 1 = E^0 K^0 F^0 = basis element 0."""
        v = np.zeros(self.dim, dtype=complex)
        v[self.basis_index(0, 0, 0)] = 1.0
        return v

    def augmentation_map(self) -> np.ndarray:
        """The augmentation epsilon: u_q -> C.

        epsilon(E^a K^b F^c) = delta_{a,0} delta_{c,0}.
        (K^b -> 1 for any b since epsilon is an algebra map and epsilon(K) = 1.)

        Returns:
            1D array of length dim = N^3.
        """
        N = self.N
        eps = np.zeros(self.dim, dtype=complex)
        for b in range(N):
            eps[self.basis_index(0, b, 0)] = 1.0
        return eps


# ---------------------------------------------------------------------------
# Bar complex construction
# ---------------------------------------------------------------------------

class BarComplex:
    """Bar complex of the small quantum group u_q(sl_2).

    The reduced bar complex B_n(u_q) = I^{otimes n} where I = ker(epsilon)
    is the augmentation ideal, with dim I = N^3 - 1.

    The STANDARD bar differential d: B_n -> B_{n-1} always satisfies d^2 = 0
    (this is a theorem for any associative algebra).

    The Q-BAR DIFFERENTIAL d_q: B_n -> B_{n-1} replaces the alternating signs
    (-1)^{i+1} with q-weights q^{i-1}, following Kapranov's N-complex
    construction:

      d_q(h_1 | ... | h_n) = sum_{i=1}^{n-1} q^{i-1}
          h_1 | ... | (h_i * h_{i+1}) | ... | h_n

    This satisfies d_q^N = 0 (N-complex) but d_q^2 != 0 for N >= 3.

    We compute both differentials: the standard one (for bar cohomology)
    and the q-deformed one (for N-complex structure).
    """

    def __init__(self, uq: SmallQuantumSl2, max_degree: int = 3,
                 use_reduced: bool = True):
        """Initialize the bar complex.

        Args:
            uq: the small quantum group.
            max_degree: maximum bar degree to compute.
            use_reduced: if True, use the reduced bar complex
                (augmentation ideal tensors). Default True.
        """
        self.uq = uq
        self.N = uq.N
        self.q = uq.q
        self.max_degree = max_degree
        self.use_reduced = use_reduced

        # Precompute multiplication table
        self._mult = uq.multiplication_table()

        if use_reduced:
            eps = uq.augmentation_map()
            self._setup_reduced_basis(eps)
        else:
            self.I_dim = uq.dim
            self._I_to_full = np.eye(uq.dim, dtype=complex)
            self._full_to_I = np.eye(uq.dim, dtype=complex)

        # Precompute multiplication in I-basis
        self._mu_I = None

        # Caches
        self._differentials: Dict[int, np.ndarray] = {}
        self._q_differentials: Dict[int, np.ndarray] = {}

    def _setup_reduced_basis(self, eps: np.ndarray):
        """Set up a basis for the augmentation ideal I = ker(epsilon).

        Basis for ker(eps):
        1. All PBW basis elements E^a K^b F^c with (a,c) != (0,0):
           these have epsilon = 0. Count: N^3 - N.
        2. K^b - 1 for b = 1,...,N-1. Count: N-1.
        Total: N^3 - 1.
        """
        N = self.N
        uq = self.uq
        dim_full = uq.dim
        dim_I = dim_full - 1
        self.I_dim = dim_I

        I_to_full = np.zeros((dim_full, dim_I), dtype=complex)

        col = 0
        # Type 1: E^a K^b F^c with (a,c) != (0,0)
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    if a == 0 and c == 0:
                        continue
                    idx = uq.basis_index(a, b, c)
                    I_to_full[idx, col] = 1.0
                    col += 1

        # Type 2: K^b - 1 for b = 1,...,N-1
        idx_1 = uq.basis_index(0, 0, 0)
        for b in range(1, N):
            idx_kb = uq.basis_index(0, b, 0)
            I_to_full[idx_kb, col] = 1.0
            I_to_full[idx_1, col] = -1.0
            col += 1

        assert col == dim_I

        self._I_to_full = I_to_full
        self._full_to_I = np.linalg.pinv(I_to_full)

    def _get_mu_I(self) -> np.ndarray:
        """Get (cached) multiplication table in I-basis."""
        if self._mu_I is not None:
            return self._mu_I

        dim_I = self.I_dim
        embed = self._I_to_full
        project = self._full_to_I
        mult = self._mult

        mu_I = np.zeros((dim_I, dim_I, dim_I), dtype=complex)
        for a in range(dim_I):
            va = embed[:, a]
            for b in range(dim_I):
                vb = embed[:, b]
                prod_full = np.einsum('k,l,klm->m', va, vb, mult)
                mu_I[a, b, :] = project @ prod_full

        self._mu_I = mu_I
        return mu_I

    def bar_space_dim(self, degree: int) -> int:
        """Dimension of the bar space B_n."""
        if degree < 0:
            return 0
        if degree == 0:
            return 1
        return self.I_dim ** degree

    def differential(self, degree: int) -> np.ndarray:
        """Standard bar differential d: B_n -> B_{n-1} (d^2 = 0).

        d(h_1 | ... | h_n) = sum_{i=1}^{n-1} (-1)^{i+1}
            h_1 | ... | (h_i * h_{i+1}) | ... | h_n
        """
        if degree in self._differentials:
            return self._differentials[degree]

        if degree <= 1:
            dim_source = self.bar_space_dim(degree)
            dim_target = self.bar_space_dim(degree - 1)
            D = np.zeros((dim_target, dim_source), dtype=complex)
            self._differentials[degree] = D
            return D

        D = self._compute_differential(degree, use_q_signs=False)
        self._differentials[degree] = D
        return D

    def q_differential(self, degree: int) -> np.ndarray:
        """Q-deformed bar differential d_q: B_n -> B_{n-1} (d_q^N = 0).

        d_q(h_1 | ... | h_n) = sum_{i=1}^{n-1} q^{i-1}
            h_1 | ... | (h_i * h_{i+1}) | ... | h_n

        This is the Kapranov N-complex differential. The signs (-1)^{i+1}
        are replaced by q-weights q^{i-1}. Since q^N = 1, the quantum
        binomial theorem gives d_q^N = 0.
        """
        if degree in self._q_differentials:
            return self._q_differentials[degree]

        if degree <= 1:
            dim_source = self.bar_space_dim(degree)
            dim_target = self.bar_space_dim(degree - 1)
            D = np.zeros((dim_target, dim_source), dtype=complex)
            self._q_differentials[degree] = D
            return D

        D = self._compute_differential(degree, use_q_signs=True)
        self._q_differentials[degree] = D
        return D

    def _compute_differential(self, n: int, use_q_signs: bool = False) -> np.ndarray:
        """Compute d or d_q: B_n -> B_{n-1}.

        Args:
            n: source bar degree.
            use_q_signs: if False, use standard signs (-1)^{i+1}.
                         if True, use q-signs q^{i-1}.
        """
        dim_I = self.I_dim
        dim_source = dim_I ** n
        dim_target = dim_I ** (n - 1)
        D = np.zeros((dim_target, dim_source), dtype=complex)

        mu_I = self._get_mu_I()
        q = self.q

        for src_idx in range(dim_source):
            js = self._multi_index(src_idx, n, dim_I)

            for i in range(n - 1):
                if use_q_signs:
                    sign = q ** i
                else:
                    sign = (-1) ** (i + 1)

                prod_vec = mu_I[js[i], js[i + 1]]

                for k in range(dim_I):
                    if abs(prod_vec[k]) < 1e-15:
                        continue
                    target_js = js[:i] + (k,) + js[i+2:]
                    tgt_idx = self._flat_index(target_js, dim_I)
                    D[tgt_idx, src_idx] += sign * prod_vec[k]

        return D

    def _multi_index(self, flat_idx: int, n: int, base: int) -> Tuple[int, ...]:
        """Convert flat index to multi-index (j_1, ..., j_n) in base `base`."""
        digits = []
        for _ in range(n):
            digits.append(flat_idx % base)
            flat_idx //= base
        return tuple(reversed(digits))

    def _flat_index(self, multi_idx: Tuple[int, ...], base: int) -> int:
        """Convert multi-index to flat index."""
        result = 0
        for j in multi_idx:
            result = result * base + j
        return result

    def d_power(self, n: int, power: int, use_q: bool = False) -> np.ndarray:
        """Compute d^power (or d_q^power) starting from bar degree n.

        Returns the matrix of the composition B_n -> B_{n-power}.
        """
        if power <= 0:
            dim = self.bar_space_dim(n)
            return np.eye(dim, dtype=complex)

        diff_fn = self.q_differential if use_q else self.differential
        result = diff_fn(n)
        for k in range(1, power):
            d_next = diff_fn(n - k)
            result = d_next @ result

        return result

    def verify_d_squared(self, degree: int) -> float:
        """Check ||d^2||_F for the STANDARD bar differential.

        Should always be 0 (d^2 = 0 for associative algebras).
        """
        d2 = self.d_power(degree, 2, use_q=False)
        return float(np.linalg.norm(d2))

    def verify_dq_squared(self, degree: int) -> float:
        """Check ||d_q^2||_F for the Q-BAR differential.

        Should be nonzero for N >= 3 (genuine N-complex).
        Should be zero for N = 2 (q = -1 recovers standard signs).
        """
        d2 = self.d_power(degree, 2, use_q=True)
        return float(np.linalg.norm(d2))

    def verify_dq_N(self, degree: int) -> float:
        """Check ||d_q^N||_F for the Q-BAR differential.

        The prediction is d_q^N = 0 (N-complex structure).
        """
        dN = self.d_power(degree, self.N, use_q=True)
        return float(np.linalg.norm(dN))


# ---------------------------------------------------------------------------
# Bar cohomology (standard)
# ---------------------------------------------------------------------------

def bar_cohomology_dim(bar: BarComplex, degree: int) -> Optional[int]:
    """Compute dim H^n(u_q, C) = dim(ker d_n / im d_{n+1}).

    This is the standard bar cohomology (d^2 = 0).
    """
    if degree < 0:
        return 0
    if degree > bar.max_degree:
        return None

    d_n = bar.differential(degree)
    d_n_plus_1 = bar.differential(degree + 1) if degree + 1 <= bar.max_degree else None

    dim_n = bar.bar_space_dim(degree)
    if dim_n == 0:
        return 0

    # ker(d_n)
    ker_dim = dim_n - np.linalg.matrix_rank(d_n, tol=1e-10)

    # im(d_{n+1})
    if d_n_plus_1 is not None:
        im_dim = np.linalg.matrix_rank(d_n_plus_1, tol=1e-10)
    else:
        im_dim = 0

    return int(ker_dim - im_dim)


def all_bar_cohomology(bar: BarComplex) -> Dict[int, Optional[int]]:
    """Compute bar cohomology in all degrees up to max_degree."""
    return {n: bar_cohomology_dim(bar, n) for n in range(bar.max_degree + 1)}


# ---------------------------------------------------------------------------
# N-complex cohomology (q-deformed)
# ---------------------------------------------------------------------------

def ncomplex_cohomology_dim(bar: BarComplex, degree: int,
                            j: int) -> Optional[int]:
    """Compute dim H^{j, N-j}_degree of the N-complex.

    H^{j, N-j}_n = ker(d_q^j : B_n -> B_{n-j}) / im(d_q^{N-j} : B_{n+N-j} -> B_n).

    Args:
        bar: the bar complex.
        degree: the bar degree n.
        j: the cohomology flavor (1 <= j <= N-1).

    Returns:
        Dimension, or None if the required bar degrees exceed max_degree.
    """
    N = bar.N
    if j < 1 or j >= N:
        raise ValueError(f"j must satisfy 1 <= j <= N-1, got j={j}, N={N}")

    source_degree_im = degree + N - j

    if source_degree_im > bar.max_degree:
        return None

    # ker(d_q^j) at degree n
    dj = bar.d_power(degree, j, use_q=True)
    ker_dim = dj.shape[1] - np.linalg.matrix_rank(dj, tol=1e-10)

    # im(d_q^{N-j}) from degree n + N - j to degree n
    dNmj = bar.d_power(source_degree_im, N - j, use_q=True)
    im_dim = np.linalg.matrix_rank(dNmj, tol=1e-10)

    return int(ker_dim - im_dim)


def all_cohomology_flavors(bar: BarComplex, degree: int) -> Dict[int, Optional[int]]:
    """Compute all N-complex cohomology flavors H^{j, N-j} at a given degree.

    Returns dict j -> dim H^{j, N-j}_degree for j = 1, ..., N-1.
    """
    N = bar.N
    return {j: ncomplex_cohomology_dim(bar, degree, j) for j in range(1, N)}


def euler_characteristic_sum(bar: BarComplex, degree: int) -> Optional[complex]:
    """Compute the alternating sum of N-complex cohomology flavor dimensions.

    Returns the sum, or None if any flavor is not computable.
    """
    N = bar.N
    flavors = all_cohomology_flavors(bar, degree)
    if any(v is None for v in flavors.values()):
        return None
    total = sum((-1) ** (j + 1) * flavors[j] for j in range(1, N))
    return total


# ---------------------------------------------------------------------------
# Diagnostic: structure constants verification
# ---------------------------------------------------------------------------

def verify_uq_relations(uq: SmallQuantumSl2) -> Dict[str, bool]:
    """Verify the defining relations of u_q(sl_2).

    Checks:
    1. K^N = 1
    2. E^N = 0
    3. F^N = 0
    4. K E = q^2 E K
    5. K F = q^{-2} F K
    6. E F - F E = (K - K^{-1}) / (q - q^{-1})
    """
    N = uq.N
    q = uq.q
    mult = uq.multiplication_table()
    dim = uq.dim

    def vec(a, b, c):
        v = np.zeros(dim, dtype=complex)
        v[uq.basis_index(a % N, b % N, c % N)] = 1.0
        return v

    def mul(v1, v2):
        return np.einsum('i,j,ijk->k', v1, v2, mult)

    results = {}

    # 1. K^N = 1
    K = vec(0, 1, 0)
    K_power = vec(0, 0, 0).copy()
    for _ in range(N):
        K_power = mul(K_power, K)
    identity = vec(0, 0, 0)
    results["K^N = 1"] = np.allclose(K_power, identity, atol=1e-10)

    # 2. E^N = 0
    E = vec(1, 0, 0)
    E_power = E.copy()
    for _ in range(N - 1):
        E_power = mul(E_power, E)
    results["E^N = 0"] = np.allclose(E_power, 0, atol=1e-10)

    # 3. F^N = 0
    F = vec(0, 0, 1)
    F_power = F.copy()
    for _ in range(N - 1):
        F_power = mul(F_power, F)
    results["F^N = 0"] = np.allclose(F_power, 0, atol=1e-10)

    # 4. KE = q^2 EK
    KE = mul(K, E)
    EK = mul(E, K)
    results["KE = q^2 EK"] = np.allclose(KE, q**2 * EK, atol=1e-10)

    # 5. KF = q^{-2} FK
    KF = mul(K, F)
    FK = mul(F, K)
    results["KF = q^{-2} FK"] = np.allclose(KF, q**(-2) * FK, atol=1e-10)

    # 6. EF - FE = (K - K^{-1}) / (q - q^{-1})
    EF = mul(E, F)
    FE = mul(F, E)
    K_inv = vec(0, N - 1, 0)
    denom = q - q**(-1)
    if abs(denom) > 1e-14:
        rhs = (K - K_inv) / denom
        results["EF - FE = (K-K^{-1})/(q-q^{-1})"] = np.allclose(
            EF - FE, rhs, atol=1e-10)
    else:
        # Degenerate case (N = 2): both sides are 0.
        lhs_zero = np.allclose(EF - FE, 0, atol=1e-10)
        rhs_zero = np.allclose(K - K_inv, 0, atol=1e-10)
        results["EF - FE = (K-K^{-1})/(q-q^{-1})"] = lhs_zero and rhs_zero

    return results


def verify_associativity(uq: SmallQuantumSl2, n_samples: int = 50) -> bool:
    """Spot-check associativity: (ab)c = a(bc) for random triples."""
    mult = uq.multiplication_table()
    dim = uq.dim
    rng = np.random.default_rng(42)

    for _ in range(n_samples):
        a = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
        b = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)
        c = rng.standard_normal(dim) + 1j * rng.standard_normal(dim)

        ab = np.einsum('i,j,ijk->k', a, b, mult)
        ab_c = np.einsum('i,j,ijk->k', ab, c, mult)

        bc = np.einsum('i,j,ijk->k', b, c, mult)
        a_bc = np.einsum('i,j,ijk->k', a, bc, mult)

        if not np.allclose(ab_c, a_bc, atol=1e-8):
            return False
    return True


# ---------------------------------------------------------------------------
# Dimension data and predictions
# ---------------------------------------------------------------------------

def small_quantum_group_dim(N: int) -> int:
    """Dimension of u_q(sl_2) at q = e^{2 pi i / N}."""
    return N ** 3


def bar_space_dims(N: int, max_degree: int) -> Dict[int, int]:
    """Dimensions of reduced bar complex spaces for u_q(sl_2).

    B_n = I^{otimes n} with dim I = N^3 - 1.
    """
    dim_I = N ** 3 - 1
    return {n: dim_I ** n for n in range(max_degree + 1)}


# ---------------------------------------------------------------------------
# Full analysis
# ---------------------------------------------------------------------------

def full_ncomplex_analysis(N: int, max_degree: int = 3) -> Dict:
    """Complete N-complex analysis for u_q(sl_2) at q = e^{2 pi i / N}.

    Returns a dict with:
    - uq_relations: verification of defining relations
    - associativity: spot-check of associativity
    - bar_dims: dimensions of bar spaces
    - d_squared_norms: ||d^2|| at each degree (standard, should always be 0)
    - dq_squared_norms: ||d_q^2|| (q-deformed, nonzero for N >= 3)
    - dq_N_norms: ||d_q^N|| (should be zero)
    - bar_cohomology: standard bar cohomology dimensions
    - ncomplex_flavors: dim H^{j,N-j} at each degree
    - euler_sums: alternating sums of N-complex flavors
    """
    uq = SmallQuantumSl2(N)

    results: Dict = {
        "N": N,
        "q": uq.q,
        "dim_uq": uq.dim,
        "dim_I": uq.dim - 1,
    }

    results["uq_relations"] = verify_uq_relations(uq)
    results["associativity"] = verify_associativity(uq)

    bar = BarComplex(uq, max_degree=max_degree, use_reduced=True)

    results["bar_dims"] = {n: bar.bar_space_dim(n) for n in range(max_degree + 1)}

    # Standard d^2 (should always be 0)
    results["d_squared_norms"] = {}
    for n in range(2, max_degree + 1):
        results["d_squared_norms"][n] = bar.verify_d_squared(n)

    # Q-deformed d_q^2
    results["dq_squared_norms"] = {}
    for n in range(2, max_degree + 1):
        results["dq_squared_norms"][n] = bar.verify_dq_squared(n)

    # Q-deformed d_q^N
    results["dq_N_norms"] = {}
    for n in range(N, max_degree + 1):
        results["dq_N_norms"][n] = bar.verify_dq_N(n)

    # Standard bar cohomology
    results["bar_cohomology"] = all_bar_cohomology(bar)

    # N-complex flavors
    results["ncomplex_flavors"] = {}
    for n in range(1, max_degree + 1):
        results["ncomplex_flavors"][n] = all_cohomology_flavors(bar, n)

    # Euler sums
    results["euler_sums"] = {}
    for n in range(1, max_degree + 1):
        results["euler_sums"][n] = euler_characteristic_sum(bar, n)

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("KL N-COMPLEX STRUCTURE FOR u_q(sl_2) AT ROOTS OF UNITY")
    print("=" * 70)

    for N in [2, 3, 4]:
        print(f"\n{'='*60}")
        print(f"N = {N}, q = e^{{2 pi i / {N}}}")
        print(f"{'='*60}")

        uq = SmallQuantumSl2(N)
        print(f"  dim u_q(sl_2) = {uq.dim}")

        rels = verify_uq_relations(uq)
        print(f"  Relations:")
        for name, ok in rels.items():
            status = "PASS" if ok else "FAIL"
            print(f"    [{status}] {name}")

        assoc = verify_associativity(uq)
        print(f"  Associativity: {'PASS' if assoc else 'FAIL'}")

        max_deg = 3 if N <= 3 else 2
        bar = BarComplex(uq, max_degree=max_deg, use_reduced=True)

        print(f"  Bar space dims (reduced):")
        for n in range(max_deg + 1):
            print(f"    B_{n} = {bar.bar_space_dim(n)}")

        print(f"  Standard ||d^2|| norms (should be 0):")
        for n in range(2, max_deg + 1):
            norm = bar.verify_d_squared(n)
            print(f"    degree {n}: {norm:.6e}")

        print(f"  Q-deformed ||d_q^2|| norms:")
        for n in range(2, max_deg + 1):
            norm = bar.verify_dq_squared(n)
            print(f"    degree {n}: {norm:.6e}")

        if max_deg >= N:
            print(f"  Q-deformed ||d_q^N|| norms (should be 0):")
            for n in range(N, max_deg + 1):
                norm = bar.verify_dq_N(n)
                print(f"    degree {n}: {norm:.6e}")

        print(f"  Bar cohomology (standard):")
        cohom = all_bar_cohomology(bar)
        for n, h in cohom.items():
            if h is not None and h > 0:
                print(f"    H^{n} = {h}")
