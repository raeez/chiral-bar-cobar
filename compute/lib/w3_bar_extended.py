"""W_3 bar complex: extended computation of bar cohomology at degrees 1-5.

This module provides:
1. The full W3 vacuum module with mode operator algebra (L_m, W_m, Lambda_n)
2. All n-th OPE products a_{(k)}b including descendants and composite fields
3. Bar chain group dimensions at each degree and conformal weight
4. Verification of generator-level OPE products against ground truth

W3 commutation relations (Zamolodchikov):
  [L_m, L_n] = (m-n) L_{m+n} + c/12 (m^3 - m) delta_{m+n,0}
  [L_m, W_n] = (2m - n) W_{m+n}
  [W_m, W_n] = (m-n) {1/15 (m+n+3)(m+n+2) - 1/6 (m+2)(n+2)} L_{m+n}
               + beta/2 (m-n) Lambda_{m+n}
               + c/360 m(m^2-1)(m^2-4) delta_{m+n,0}

where beta = 16/(22+5c) and Lambda_n is the mode of the composite field
Lambda = :TT: - (3/10) partial^2 T. Concretely:
  Lambda_n = sum_{p <= -2} L_p L_{n-p} + sum_{p >= -1} L_{n-p} L_p
             - (3/10)(n+2)(n+3) L_n

Ground truth (from manuscript):
  Bar cohomology: H^1=2, H^2=5, H^3=16, H^4=52 (tab:bar-dimensions)
  The H^3=16 value is the bar cohomology of the CHIRAL bar complex
  (involving configuration space forms), NOT the CE complex of the
  Lie algebra (V-bar, a_{(0)}). See NOTES below.

  B^1_h dimensions (the manuscript's table has a DISCREPANCY):
  - The GF formula at line 412 gives prod_{n>=2} 1/(1-q^n) * prod_{n>=3} 1/(1-q^n) - 1
  - This evaluates to: 1, 2, 3, 4, 8, 10, 17 at h=2,...,8 (matching PBW)
  - The manuscript TABLE at line 402 says: 1, 2, 4, 6, 11, 16, 26 (different!)
  - The PBW/GF values are CORRECT; the table appears to have an error.

NOTES ON BAR COHOMOLOGY:
  The chiral bar complex uses configuration space forms (Orlik-Solomon algebra)
  and the bar differential involves residues at collision divisors. The residue
  operation uses the FULL OPE (all a_{(k)}b products), not just the simple pole
  a_{(0)}b. The OS forms encode which OPE products contribute at each collision.

  The bar cohomology H^n(B(W3)) = 2, 5, 16, 52, ... cannot be computed by:
  - The associative bar complex with any single product (neither a_{(0)} nor full mu)
  - The Chevalley-Eilenberg complex of the Lie algebra (V-bar, a_{(0)})
  - The Zhu algebra bar complex (since A(W3) has I^2 = I)

  It requires the full chiral/factorization bar construction, which involves
  OS forms on Conf_n(C) and residue calculus. The computation is documented
  in the manuscript's §sec:w3-bar-degree3 for degree 3 only.

CONVENTIONS:
- Cohomological grading, |d| = +1
- Bar differential has bar-degree -1
- States in PBW basis: L_{-l1}...L_{-lk} W_{-w1}...W_{-wl} |0>
  with l1 >= ... >= lk >= 2, w1 >= ... >= wl >= 3
"""

from __future__ import annotations

import numpy as np
from math import factorial
from typing import Dict, List, Optional, Tuple

# =========================================================================
# State representation (PBW basis)
# =========================================================================

State = Tuple[Tuple[int, ...], Tuple[int, ...]]
VACUUM: State = ((), ())


def state_weight(s: State) -> int:
    return sum(s[0]) + sum(s[1])


def make_state(l_modes: Tuple[int, ...], w_modes: Tuple[int, ...]) -> State:
    return (tuple(sorted(l_modes, reverse=True)), tuple(sorted(w_modes, reverse=True)))


# =========================================================================
# PBW basis enumeration
# =========================================================================

def _partitions_into_parts_geq(n: int, min_part: int) -> List[Tuple[int, ...]]:
    if n == 0:
        return [()]
    if n < min_part:
        return []
    result = []

    def backtrack(remaining: int, max_part: int, current: List[int]):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), min_part - 1, -1):
            current.append(p)
            backtrack(remaining - p, p, current)
            current.pop()

    backtrack(n, n, [])
    return result


def vbar_basis(max_weight: int) -> Dict[int, List[State]]:
    """PBW basis for V-bar at each weight up to max_weight.

    V-bar = vacuum module minus vacuum.
    States: L_{-l1}...L_{-lk} W_{-w1}...W_{-wl} |0>
    with l_i >= 2 (descending) and w_j >= 3 (descending).

    Generating function: prod_{n>=2} 1/(1-q^n) * prod_{n>=3} 1/(1-q^n) - 1
    Values: h=2:1, h=3:2, h=4:3, h=5:4, h=6:8, h=7:10, h=8:17
    """
    basis: Dict[int, List[State]] = {}
    for h in range(2, max_weight + 1):
        states: List[State] = []
        for a in range(0, h + 1):
            b = h - a
            for lp in _partitions_into_parts_geq(a, 2):
                for wp in _partitions_into_parts_geq(b, 3):
                    states.append((lp, wp))
        basis[h] = states
    return basis


def dim_vbar(h: int) -> int:
    """Dimension of V-bar at conformal weight h."""
    if h < 2:
        return 0
    count = 0
    for a in range(0, h + 1):
        b = h - a
        count += len(_partitions_into_parts_geq(a, 2)) * len(_partitions_into_parts_geq(b, 3))
    return count


def dim_vbar_gf(max_h: int) -> Dict[int, int]:
    """Compute dim V-bar_h for h=0,...,max_h using the generating function.

    GF = prod_{n>=2} 1/(1-q^n) * prod_{n>=3} 1/(1-q^n) - 1
    """
    c_L = [0] * (max_h + 1)
    c_L[0] = 1
    for n in range(2, max_h + 1):
        for k in range(n, max_h + 1):
            c_L[k] += c_L[k - n]

    c_W = [0] * (max_h + 1)
    c_W[0] = 1
    for n in range(3, max_h + 1):
        for k in range(n, max_h + 1):
            c_W[k] += c_W[k - n]

    product = [0] * (max_h + 1)
    for i in range(max_h + 1):
        for j in range(max_h + 1 - i):
            product[i + j] += c_L[i] * c_W[j]
    product[0] -= 1  # subtract vacuum

    return {h: product[h] for h in range(max_h + 1)}


# =========================================================================
# Bar chain group dimensions
# =========================================================================

def bar_chain_dim(n: int, h: int, vbar_dims: Optional[Dict[int, int]] = None,
                  max_h: int = 30) -> int:
    """Dimension of the bar chain group B^n_h (at bar degree n and total weight h).

    B^n = V-bar^{tensor(n+1)} x OS^n(Conf_{n+1}(C))
    dim B^n_h = (number of ordered (n+1)-tuples at weight h) * n!

    The factor n! = dim OS^n(Conf_{n+1}(C)) is the top OS algebra dimension.
    """
    if vbar_dims is None:
        vbar_dims = dim_vbar_gf(max_h)

    # Count ordered (n+1)-tuples of V-bar states with total weight h
    # Each state has weight >= 2, so h >= 2*(n+1)
    if h < 2 * (n + 1):
        return 0

    # Compute by convolution
    # f^{n+1}(h) = sum_{h1+...+h_{n+1}=h} prod dim(V-bar_{hi})
    prev = {0: 1}  # Start with the "empty" product
    for _ in range(n + 1):
        curr: Dict[int, int] = {}
        for hp, cp in prev.items():
            for hw in range(2, h - hp + 1):
                dw = vbar_dims.get(hw, 0)
                if dw == 0:
                    continue
                ht = hp + hw
                if ht > h:
                    break
                curr[ht] = curr.get(ht, 0) + cp * dw
        prev = curr

    tuple_count = prev.get(h, 0)
    os_dim = factorial(n)  # dim OS^n(Conf_{n+1})
    return tuple_count * os_dim


def bar_chain_table(max_n: int, max_h: int) -> Dict[Tuple[int, int], int]:
    """Compute bar chain group dimensions B^n_h for all n,h."""
    vbar_dims = dim_vbar_gf(max_h)
    result = {}
    for n in range(0, max_n + 1):
        for h in range(2 * (n + 1), max_h + 1):
            d = bar_chain_dim(n, h, vbar_dims, max_h)
            if d > 0:
                result[(n, h)] = d
    return result


# =========================================================================
# W3 vacuum module: matrix representation of mode operators
# =========================================================================

class W3VacuumModule:
    """Numerical representation of the W3 vacuum module truncated to max_weight.

    Builds explicit matrices for L_m and W_m operators on the state space.
    The state space includes the vacuum |0> (weight 0) and all PBW states
    in V-bar up to max_weight.
    """

    def __init__(self, max_weight: int, c_val: float):
        self.max_weight = max_weight
        self.c_val = c_val
        self.beta_val = 16.0 / (22.0 + 5.0 * c_val)

        # Build ordered basis: vacuum first, then V-bar states by weight
        self._vbar_basis = vbar_basis(max_weight)
        self._all_states: List[State] = [VACUUM]
        self._state_to_idx: Dict[State, int] = {VACUUM: 0}
        self._vbar_states: List[State] = []
        self._vbar_to_idx: Dict[State, int] = {}
        for h in range(2, max_weight + 1):
            for s in self._vbar_basis.get(h, []):
                idx = len(self._all_states)
                self._all_states.append(s)
                self._state_to_idx[s] = idx
                vidx = len(self._vbar_states)
                self._vbar_states.append(s)
                self._vbar_to_idx[s] = vidx

        self.total_dim = len(self._all_states)
        self.vbar_dim = len(self._vbar_states)

        # Mode operator cache
        self._L_cache: Dict[int, np.ndarray] = {}
        self._W_cache: Dict[int, np.ndarray] = {}

    def _get_L_matrix(self, m: int) -> np.ndarray:
        """Get or build the L_m matrix."""
        if m not in self._L_cache:
            mat = np.zeros((self.total_dim, self.total_dim))
            for j, s in enumerate(self._all_states):
                result = self._L_on_state(m, s)
                for s2, coeff in result.items():
                    if s2 in self._state_to_idx:
                        mat[self._state_to_idx[s2], j] = coeff
            self._L_cache[m] = mat
        return self._L_cache[m]

    def _get_W_matrix(self, m: int) -> np.ndarray:
        """Get or build the W_m matrix."""
        if m not in self._W_cache:
            mat = np.zeros((self.total_dim, self.total_dim))
            for j, s in enumerate(self._all_states):
                result = self._W_on_state(m, s)
                for s2, coeff in result.items():
                    if s2 in self._state_to_idx:
                        mat[self._state_to_idx[s2], j] = coeff
            self._W_cache[m] = mat
        return self._W_cache[m]

    def _apply_L_mode(self, m: int, state_vec: np.ndarray) -> np.ndarray:
        """Apply L_m to a state vector."""
        return self._get_L_matrix(m) @ state_vec

    def _apply_W_mode(self, m: int, state_vec: np.ndarray) -> np.ndarray:
        """Apply W_m to a state vector."""
        return self._get_W_matrix(m) @ state_vec

    def _L_on_state(self, m: int, state: State) -> Dict[State, float]:
        """Compute L_m |state> using commutation relations.

        Commutes L_m past each mode in the state from left to right.
        """
        l_modes, w_modes = state

        if not l_modes and not w_modes:
            if m >= -1:
                return {}
            return {make_state((-m,), ()): 1.0}

        result: Dict[State, float] = {}

        if l_modes:
            l1 = l_modes[0]
            rest = (l_modes[1:], w_modes)
            n = -l1

            # Term 1: L_{-l1} (L_m |rest>)
            inner = self._L_on_state(m, rest)
            for s, coeff in inner.items():
                new_s = make_state((l1,) + s[0], s[1])
                if state_weight(new_s) <= self.max_weight:
                    result[new_s] = result.get(new_s, 0.0) + coeff

            # Term 2: [L_m, L_{-l1}] |rest> = (m+l1) L_{m-l1} |rest>
            L_coeff = float(m - n)
            mn_sum = m + n
            if L_coeff != 0:
                inner2 = self._L_on_state(mn_sum, rest)
                for s, coeff in inner2.items():
                    if state_weight(s) <= self.max_weight:
                        result[s] = result.get(s, 0.0) + L_coeff * coeff
            if mn_sum == 0:
                vac_coeff = self.c_val / 12.0 * (m**3 - m)
                if vac_coeff != 0:
                    rest_weight = state_weight(rest)
                    if rest_weight <= self.max_weight:
                        result[rest] = result.get(rest, 0.0) + vac_coeff

        elif w_modes:
            w1 = w_modes[0]
            rest = (l_modes, w_modes[1:])
            n = -w1

            # Term 1: W_{-w1} (L_m |rest>)
            inner = self._L_on_state(m, rest)
            for s, coeff in inner.items():
                new_s = make_state(s[0], (w1,) + s[1])
                if state_weight(new_s) <= self.max_weight:
                    result[new_s] = result.get(new_s, 0.0) + coeff

            # Term 2: [L_m, W_{-w1}] |rest> = (2m+w1) W_{m-w1} |rest>
            W_coeff = float(2 * m - n)
            if W_coeff != 0:
                inner2 = self._W_on_state(m + n, rest)
                for s, coeff in inner2.items():
                    if state_weight(s) <= self.max_weight:
                        result[s] = result.get(s, 0.0) + W_coeff * coeff

        return result

    def _W_on_state(self, m: int, state: State) -> Dict[State, float]:
        """Compute W_m |state> using commutation relations."""
        l_modes, w_modes = state

        if not l_modes and not w_modes:
            if m >= -2:
                return {}
            return {make_state((), (-m,)): 1.0}

        result: Dict[State, float] = {}

        if l_modes:
            l1 = l_modes[0]
            rest = (l_modes[1:], w_modes)
            n = -l1

            # Term 1: L_{-l1} (W_m |rest>)
            inner = self._W_on_state(m, rest)
            for s, coeff in inner.items():
                new_s = make_state((l1,) + s[0], s[1])
                if state_weight(new_s) <= self.max_weight:
                    result[new_s] = result.get(new_s, 0.0) + coeff

            # Term 2: [W_m, L_{-l1}] |rest> = (m+2*l1) W_{m-l1} |rest>
            W_coeff = float(m + 2 * l1)
            if W_coeff != 0:
                inner2 = self._W_on_state(m - l1, rest)
                for s, coeff in inner2.items():
                    if state_weight(s) <= self.max_weight:
                        result[s] = result.get(s, 0.0) + W_coeff * coeff

        elif w_modes:
            w1 = w_modes[0]
            rest = ((), w_modes[1:])
            n = -w1
            mn_diff = m - n  # = m + w1
            mn_sum = m + n   # = m - w1

            if mn_diff == 0:
                if mn_sum == 0:
                    vac = self.c_val / 360.0 * m * (m**2 - 1) * (m**2 - 4)
                    if vac != 0:
                        result[rest] = result.get(rest, 0.0) + vac
            else:
                s_mn = mn_sum
                L_coeff = float(mn_diff) * (
                    (s_mn + 3) * (s_mn + 2) / 15.0
                    - (m + 2) * (n + 2) / 6.0
                )
                if L_coeff != 0:
                    inner_L = self._L_on_state(s_mn, rest)
                    for s, coeff in inner_L.items():
                        if state_weight(s) <= self.max_weight:
                            result[s] = result.get(s, 0.0) + L_coeff * coeff

                # Lambda_{m+n} with beta/2 coefficient
                Lambda_coeff = self.beta_val / 2.0 * float(mn_diff)
                if Lambda_coeff != 0:
                    inner_Lambda = self._Lambda_on_state(s_mn, rest)
                    for s, coeff in inner_Lambda.items():
                        if state_weight(s) <= self.max_weight:
                            result[s] = result.get(s, 0.0) + Lambda_coeff * coeff

                if mn_sum == 0:
                    vac = self.c_val / 360.0 * m * (m**2 - 1) * (m**2 - 4)
                    if vac != 0:
                        result[rest] = result.get(rest, 0.0) + vac

        return result

    def _Lambda_on_state(self, n: int, state: State) -> Dict[State, float]:
        """Compute Lambda_n |state> where Lambda is the COMPOSITE field.

        Lambda_n = (:TT:)_n - (3/10)*(n+2)*(n+3)*L_n
        (:TT:)_n = sum_{p <= -2} L_p L_{n-p} + sum_{p >= -1} L_{n-p} L_p
        """
        result: Dict[State, float] = {}
        h_state = state_weight(state)

        # Part 1: (:TT:)_n
        # For p >= -1: L_{n-p} L_p |state>
        for p in range(-1, h_state + 2):
            inner = self._L_on_state(p, state)
            if inner:
                for s, coeff in inner.items():
                    w = state_weight(s)
                    if w > self.max_weight:
                        continue
                    inner2 = self._L_on_state(n - p, s)
                    for s2, coeff2 in inner2.items():
                        if state_weight(s2) <= self.max_weight:
                            result[s2] = result.get(s2, 0.0) + coeff * coeff2

        # For p <= -2: L_p L_{n-p} |state>
        p_min = max(n - h_state - self.max_weight, -self.max_weight - 2)
        for p in range(p_min, -1):
            inner = self._L_on_state(n - p, state)
            if inner:
                for s, coeff in inner.items():
                    w = state_weight(s)
                    if w > self.max_weight:
                        continue
                    inner2 = self._L_on_state(p, s)
                    for s2, coeff2 in inner2.items():
                        if state_weight(s2) <= self.max_weight:
                            result[s2] = result.get(s2, 0.0) + coeff * coeff2

        # Part 2: subtract 3/10 * (n+2)*(n+3) * L_n
        correction_coeff = -0.3 * (n + 2) * (n + 3)
        if correction_coeff != 0:
            inner = self._L_on_state(n, state)
            for s, coeff in inner.items():
                if state_weight(s) <= self.max_weight:
                    result[s] = result.get(s, 0.0) + correction_coeff * coeff

        return result

    def state_vec(self, state: State) -> np.ndarray:
        """Unit vector for a given state."""
        v = np.zeros(self.total_dim)
        if state in self._state_to_idx:
            v[self._state_to_idx[state]] = 1.0
        return v

    def compute_mu(self, a: State, b: State) -> Tuple[np.ndarray, float]:
        """Compute mu(a, b) = sum_{k>=0} a_{(k)}b.

        Returns (vbar_vec, vacuum_coeff) where:
        - vbar_vec is indexed by self._vbar_states
        - vacuum_coeff is the coefficient of |0>
        """
        h_a = state_weight(a)
        h_b = state_weight(b)

        total_vec = np.zeros(self.total_dim)

        for k in range(0, h_a + h_b):
            result_wt = h_a + h_b - k - 1
            if result_wt < 0:
                break
            if result_wt > self.max_weight:
                continue
            prod_vec = self._nth_product_vec(a, b, k)
            total_vec += prod_vec

        vac_coeff = total_vec[0]
        vbar_vec = np.zeros(self.vbar_dim)
        for i, s in enumerate(self._vbar_states):
            vbar_vec[i] = total_vec[self._state_to_idx[s]]

        return vbar_vec, vac_coeff

    def compute_nth_product(self, a: State, b: State, k: int) -> np.ndarray:
        """Compute a_{(k)}b as a full module state vector."""
        return self._nth_product_vec(a, b, k)

    def _nth_product_vec(self, a: State, b: State, k: int) -> np.ndarray:
        """Compute a_{(k)}b as a state vector."""
        l_a, w_a = a

        if len(l_a) == 0 and len(w_a) == 0:
            return np.zeros(self.total_dim)

        b_vec = self.state_vec(b)

        if len(l_a) == 1 and len(w_a) == 0:
            p = l_a[0]
            m = k - p + 1
            coeff = self._L_field_coeff(p, m)
            if abs(coeff) < 1e-15:
                return np.zeros(self.total_dim)
            return coeff * (self._get_L_matrix(m) @ b_vec)

        if len(l_a) == 0 and len(w_a) == 1:
            q = w_a[0]
            m = k - q + 1
            coeff = self._W_field_coeff(q, m)
            if abs(coeff) < 1e-15:
                return np.zeros(self.total_dim)
            return coeff * (self._get_W_matrix(m) @ b_vec)

        return self._iterate_nth_product_vec(a, b, k)

    def _L_field_coeff(self, p: int, m: int) -> float:
        """Coefficient of L_m in field Y(L_{-p}|0>, z).

        Y(L_{-p}|0>,z) = (1/(p-2)!) partial^{p-2} T(z)
        Coefficient: (-1)^{p-2} * prod_{j=2}^{p-1}(m+j) / (p-2)!
        """
        if p == 2:
            return 1.0
        pp = p - 2
        numer = 1.0
        for j in range(2, p):
            numer *= (m + j)
        return ((-1) ** pp) * numer / factorial(pp)

    def _W_field_coeff(self, q: int, m: int) -> float:
        """Coefficient of W_m in field Y(W_{-q}|0>, z).

        Y(W_{-q}|0>,z) = (1/(q-3)!) partial^{q-3} W(z)
        """
        if q == 3:
            return 1.0
        pp = q - 3
        numer = 1.0
        for j in range(3, q):
            numer *= (m + j)
        return ((-1) ** pp) * numer / factorial(pp)

    def _iterate_nth_product_vec(self, a: State, b: State, k: int) -> np.ndarray:
        """Compute a_{(k)}b for multi-mode state a using Borcherds iterate formula."""
        l_a, w_a = a
        result = np.zeros(self.total_dim)

        if l_a:
            p = l_a[0]
            a_prime = (l_a[1:], w_a)
            pp = p - 2

            for j in range(0, pp + 1):
                binom = _binomial(pp, j)
                sign = (-1) ** j
                coeff_j = binom * sign

                # Term 1: L_{k-j-1} (a'_{(pp-j)} b)
                inner1 = self._nth_product_vec(a_prime, b, pp - j)
                if np.any(np.abs(inner1) > 1e-15):
                    result += coeff_j * (self._get_L_matrix(k - j - 1) @ inner1)

                # Term 2: (-1)^{p-1} a'_{(k+pp-j)} (L_{j-1} b)
                sign2 = (-1) ** (p - 1)
                b_vec = self.state_vec(b)
                Lb = self._get_L_matrix(j - 1) @ b_vec
                if np.any(np.abs(Lb) > 1e-15):
                    for idx in range(self.total_dim):
                        if abs(Lb[idx]) > 1e-15:
                            s = self._all_states[idx]
                            inner2 = self._nth_product_vec(a_prime, s, k + pp - j)
                            result += coeff_j * sign2 * Lb[idx] * inner2

        elif w_a:
            q = w_a[0]
            a_prime = (l_a, w_a[1:])
            pp = q - 3

            for j in range(0, pp + 1):
                binom = _binomial(pp, j)
                sign = (-1) ** j
                coeff_j = binom * sign

                # Term 1: W_{k-j-2} (a'_{(pp-j)} b)
                inner1 = self._nth_product_vec(a_prime, b, pp - j)
                if np.any(np.abs(inner1) > 1e-15):
                    result += coeff_j * (self._get_W_matrix(k - j - 2) @ inner1)

                # Term 2: (-1)^{q-2} a'_{(k+pp-j)} (W_{j-2} b)
                sign2 = (-1) ** (q - 2)
                b_vec = self.state_vec(b)
                Wb = self._get_W_matrix(j - 2) @ b_vec
                if np.any(np.abs(Wb) > 1e-15):
                    for idx in range(self.total_dim):
                        if abs(Wb[idx]) > 1e-15:
                            s = self._all_states[idx]
                            inner2 = self._nth_product_vec(a_prime, s, k + pp - j)
                            result += coeff_j * sign2 * Wb[idx] * inner2

        return result

    def vbar_states_at_weight(self, h: int) -> List[State]:
        return self._vbar_basis.get(h, [])

    def vbar_indices_at_weight(self, h: int) -> List[int]:
        return [self._vbar_to_idx[s] for s in self.vbar_states_at_weight(h)]


def _binomial(n: int, k: int) -> int:
    if k < 0 or k > n or n < 0:
        return 0
    result = 1
    for i in range(min(k, n - k)):
        result = result * (n - i) // (i + 1)
    return result


# =========================================================================
# Verification helpers
# =========================================================================

def verify_mu_generators(c_val: float = 7.0, verbose: bool = True) -> Dict[str, bool]:
    """Verify mu(a,b) for generator pairs T, W against known OPE data.

    Ground truth (w3_bar.py, comp:w3-ope):
      mu(T,T) = (c/2)|0> + 2T + dT
      mu(T,W) = 3W + dW
      mu(W,T) = 3W + 2dW
      mu(W,W) = (c/3)|0> + 2T + dT + higher
    """
    mod = W3VacuumModule(10, c_val)

    T = ((2,), ())
    W = ((), (3,))

    results = {}

    # mu(T, T)
    vbar, vac = mod.compute_mu(T, T)
    results["mu(T,T) vac = c/2"] = abs(vac - c_val / 2) < 1e-10
    idx_T = mod._vbar_to_idx[T]
    idx_dT = mod._vbar_to_idx[((3,), ())]
    results["mu(T,T) T = 2"] = abs(vbar[idx_T] - 2.0) < 1e-10
    results["mu(T,T) dT = 1"] = abs(vbar[idx_dT] - 1.0) < 1e-10

    if verbose:
        print(f"mu(T,T) at c={c_val}:")
        print(f"  vacuum: {vac:.6f} (expected {c_val/2:.6f})")
        for i, s in enumerate(mod._vbar_states):
            if abs(vbar[i]) > 1e-12:
                print(f"  {s} (wt={state_weight(s)}): {vbar[i]:.6f}")

    # mu(T, W)
    vbar, vac = mod.compute_mu(T, W)
    idx_W = mod._vbar_to_idx[W]
    idx_dW = mod._vbar_to_idx[((), (4,))]
    results["mu(T,W) vac = 0"] = abs(vac) < 1e-10
    results["mu(T,W) W = 3"] = abs(vbar[idx_W] - 3.0) < 1e-10
    results["mu(T,W) dW = 1"] = abs(vbar[idx_dW] - 1.0) < 1e-10

    if verbose:
        print(f"\nmu(T,W): vac={vac:.6f}, W={vbar[idx_W]:.6f}, dW={vbar[idx_dW]:.6f}")

    # mu(W, T)
    vbar, vac = mod.compute_mu(W, T)
    results["mu(W,T) vac = 0"] = abs(vac) < 1e-10
    results["mu(W,T) W = 3"] = abs(vbar[idx_W] - 3.0) < 1e-10
    results["mu(W,T) dW = 2"] = abs(vbar[idx_dW] - 2.0) < 1e-10

    if verbose:
        print(f"mu(W,T): vac={vac:.6f}, W={vbar[idx_W]:.6f}, dW={vbar[idx_dW]:.6f}")

    # mu(W, W)
    vbar, vac = mod.compute_mu(W, W)
    results["mu(W,W) vac = c/3"] = abs(vac - c_val / 3) < 1e-10
    results["mu(W,W) T = 2"] = abs(vbar[idx_T] - 2.0) < 1e-10
    results["mu(W,W) dT = 1"] = abs(vbar[idx_dT] - 1.0) < 1e-10

    alpha = 16.0 / (22.0 + 5.0 * c_val)
    idx_L4 = mod._vbar_to_idx[((4,), ())]
    idx_L22 = mod._vbar_to_idx[((2, 2), ())]
    expected_L4 = 0.6 - 0.6 * alpha
    expected_L22 = alpha
    results["mu(W,W) L4 correct"] = abs(vbar[idx_L4] - expected_L4) < 1e-8
    results["mu(W,W) L22 correct"] = abs(vbar[idx_L22] - expected_L22) < 1e-8

    if verbose:
        print(f"mu(W,W): vac={vac:.6f} (exp {c_val/3:.6f}), T={vbar[idx_T]:.6f}")
        print(f"  L4={vbar[idx_L4]:.6f} (exp {expected_L4:.6f})")
        print(f"  L22={vbar[idx_L22]:.6f} (exp {expected_L22:.6f})")

    return results


def verify_skew_symmetry(c_val: float = 7.0) -> Dict[str, bool]:
    """Verify W_{(0)}T = 2*dW (skew-symmetry of the OPE).

    Ground truth: W_{(0)}T = 2*partial(W) (comp:w3-skew in w3_bar.py).
    """
    mod = W3VacuumModule(10, c_val)
    T = ((2,), ())
    W = ((), (3,))

    # W_{(0)}T
    v = mod._nth_product_vec(W, T, 0)
    idx_dW = mod._state_to_idx[((), (4,))]

    results = {}
    results["W_{(0)}T = 2*dW"] = abs(v[idx_dW] - 2.0) < 1e-10
    # Check no other components
    for i, s in enumerate(mod._all_states):
        if i != idx_dW and abs(v[i]) > 1e-10:
            results[f"W_(0)T spurious at {s}"] = False

    return results


def verify_ds_central_charge(c_val: float = 7.0) -> Dict[str, bool]:
    """Verify DS central charge formula c = 2 - 24(k+2)^2/(k+3).

    The W3 algebra at level k has c given by the DS formula.
    The complementarity is c + c' = 100 where c' is at k' = -k-6.
    """
    # From c = 2 - 24(k+2)^2/(k+3), solve for k:
    # k+3 = 24(k+2)^2/(2-c) ... too messy. Just check at specific k.
    results = {}

    for k in [1, 2, 3, -1, 0.5]:
        k = float(k)
        c = 2 - 24 * (k + 2)**2 / (k + 3)
        c_prime = 100 - c
        k_prime = -k - 6
        c_from_k_prime = 2 - 24 * (k_prime + 2)**2 / (k_prime + 3)
        results[f"c+c'=100 at k={k:.1f}"] = abs(c + c_from_k_prime - 100) < 1e-10

    return results


# =========================================================================
# Chain dimension analysis
# =========================================================================

def chain_dimension_analysis(max_degree: int = 5, max_weight: int = 20,
                             verbose: bool = True) -> Dict[int, int]:
    """Compute total bar chain dimensions at each degree.

    Returns {degree: total_dim} summed over all weights up to max_weight.
    """
    vbar_dims = dim_vbar_gf(max_weight)

    if verbose:
        print("V-bar dimensions by weight:")
        for h in range(2, min(max_weight + 1, 13)):
            print(f"  h={h}: {vbar_dims.get(h, 0)}")

    result = {}
    for n in range(0, max_degree + 1):
        total = 0
        for h in range(2 * (n + 1), max_weight + 1):
            d = bar_chain_dim(n, h, vbar_dims, max_weight)
            total += d
        result[n] = total
        if verbose:
            print(f"\nB^{n}: total dim = {total} (up to weight {max_weight})")
            # Show weight breakdown
            for h in range(2 * (n + 1), min(max_weight + 1, 2 * (n + 1) + 6)):
                d = bar_chain_dim(n, h, vbar_dims, max_weight)
                if d > 0:
                    print(f"  h={h}: {d}")

    return result


if __name__ == "__main__":
    print("=" * 60)
    print("W3 BAR COMPLEX EXTENDED: VERIFICATION")
    print("=" * 60)

    print("\n--- Generator mu verification ---")
    results = verify_mu_generators(c_val=7.0, verbose=True)
    print("\nSummary:")
    all_pass = True
    for name, ok in results.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        if not ok:
            all_pass = False

    print("\n--- Skew symmetry verification ---")
    results2 = verify_skew_symmetry(c_val=7.0)
    for name, ok in results2.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        if not ok:
            all_pass = False

    print("\n--- DS complementarity ---")
    results3 = verify_ds_central_charge()
    for name, ok in results3.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        if not ok:
            all_pass = False

    print("\n--- Chain dimension analysis ---")
    chain_dimension_analysis(max_degree=4, max_weight=14)

    print(f"\n{'ALL TESTS PASSED' if all_pass else 'SOME TESTS FAILED'}")
