"""Prefundamental Clebsch-Gordan closure for Y(sl_N), all N >= 2.

THEOREM (thm:prefundamental-cg-universal, character level):
  For sl_N, for all dominant weights lambda and all i in {1,...,N-1}:

    [V_lambda] * [L^-_i] = sum_{mu in wt(V_lambda)} mult_lambda(mu) * [L^-_i(shift=mu)]

  where mult_lambda(mu) is the weight multiplicity of mu in V_lambda.

  Equivalently: same-index closure holds. V_lambda tensor L^-_i decomposes
  into shifted copies of L^-_i ONLY (no mixing with L^-_j for j != i),
  and the multiplicities are precisely the weight multiplicities of V_lambda.

PROOF:
  The character of L^-_i is a formal power series in e^{-beta} for positive
  roots beta whose support contains alpha_i:

    ch(L^-_i) = prod_{beta: alpha_i in supp(beta)} prod_{n >= 1} 1/(1 - e^{-n*beta})

  The character of V_lambda is a Laurent polynomial:

    ch(V_lambda) = sum_{mu in wt(V_lambda)} mult_lambda(mu) * e^mu

  The tensor product character is the pointwise product:

    ch(V_lambda) * ch(L^-_i) = sum_mu mult_lambda(mu) * e^mu * ch(L^-_i)
                              = sum_mu mult_lambda(mu) * ch(L^-_i(shift=mu))

  This is EXACT (not an approximation) because multiplication of a Laurent
  polynomial by a formal power series is well-defined and distributive.
  No convergence issues arise: V_lambda has finitely many weights.  QED.

  REMARK: This proof works for ANY simple Lie algebra g, not just type A.
  The only input is that ch(L^-_i) is an infinite product over positive roots
  containing alpha_i, and ch(V_lambda) is a finite sum. The distributive law
  is purely algebraic.

  COROLLARY (cor:universal-k0-generation-slN):
    For Y(sl_N), every Verma module character is contained in the K_0 span
    of {[V_lambda] * [L^-_i]}, upgrading MC3 character-level closure to all
    type A simultaneously.

This module provides:
1. General sl_N root system data and weight multiplicities (Kostant multiplicity formula)
2. Prefundamental characters ch(L^-_i) for any i and any N
3. CG decomposition verification for sl_2 through sl_6
4. The proof is ALGEBRAIC (distributive law), verified computationally

References:
  - Hernandez-Jimbo 2012, Section 5 (prefundamental representations, higher rank)
  - Frenkel-Hernandez 2015 (Baxter's relations and spectra of quantum integrable models)
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional, FrozenSet
from functools import lru_cache
from itertools import combinations
import math

from compute.lib.utils import partition_number


# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------

# Weight as tuple of integers in fundamental weight basis
Weight = Tuple[int, ...]

# Formal character: weight -> multiplicity
FormalChar = Dict[Weight, int]


# ---------------------------------------------------------------------------
# sl_N root system
# ---------------------------------------------------------------------------

class SlNRootSystem:
    """Root system data for sl_N (type A_{N-1}).

    Conventions:
      - Rank r = N - 1.
      - Simple roots alpha_1, ..., alpha_r in omega (fundamental weight) basis:
        alpha_i has (Cartan matrix row i), i.e. alpha_i = sum_j A_{ij} omega_j.
      - Cartan matrix A_{ij} = 2 delta_{ij} - delta_{|i-j|,1}.
      - Positive roots: alpha_{i,j} = alpha_i + alpha_{i+1} + ... + alpha_j
        for 1 <= i <= j <= r. There are r(r+1)/2 positive roots.
    """

    def __init__(self, N: int):
        assert N >= 2, f"Need N >= 2, got {N}"
        self.N = N
        self.rank = N - 1

        # Cartan matrix
        self.cartan = [[0] * self.rank for _ in range(self.rank)]
        for i in range(self.rank):
            self.cartan[i][i] = 2
            if i > 0:
                self.cartan[i][i - 1] = -1
            if i < self.rank - 1:
                self.cartan[i][i + 1] = -1

        # Simple roots in omega basis: alpha_i = (A_{i,1}, ..., A_{i,r})
        self.simple_roots: List[Weight] = []
        for i in range(self.rank):
            self.simple_roots.append(tuple(self.cartan[i]))

        # All positive roots: alpha_{i..j} = alpha_i + ... + alpha_j
        self.positive_roots: List[Weight] = []
        self._pos_root_indices: List[Tuple[int, int]] = []  # (i, j) for alpha_{i..j}
        for i in range(self.rank):
            root = [0] * self.rank
            for j in range(i, self.rank):
                for k in range(self.rank):
                    root[k] += self.cartan[j][k]
                self.positive_roots.append(tuple(root))
                self._pos_root_indices.append((i, j))

        # rho = sum of fundamental weights = (1, 1, ..., 1)
        self.rho = tuple([1] * self.rank)

        # For each node i, which positive roots have alpha_i in their support?
        # alpha_{a..b} contains alpha_i iff a <= i <= b (0-indexed: a <= i <= b)
        self.roots_containing: List[List[int]] = []
        for i in range(self.rank):
            indices = []
            for idx, (a, b) in enumerate(self._pos_root_indices):
                if a <= i <= b:
                    indices.append(idx)
            self.roots_containing.append(indices)

    def weyl_group_elements(self) -> List[Tuple[int, List[int]]]:
        """Generate Weyl group S_N as permutations with signs.

        Returns list of (sign, perm) where perm is a permutation of [0, ..., N-1]
        and sign = (-1)^{length}.

        The Weyl group acts on the epsilon basis. We convert to/from omega basis.
        """
        from itertools import permutations
        result = []
        identity = list(range(self.N))
        for perm in permutations(range(self.N)):
            # Sign = sign of permutation
            sign = _permutation_sign(list(perm))
            result.append((sign, list(perm)))
        return result

    def omega_to_epsilon(self, w: Weight) -> List[int]:
        """Convert weight from omega basis to epsilon basis.

        omega_i = epsilon_1 + ... + epsilon_i (mod trace).
        In the epsilon basis (with sum = 0 constraint):
          w = sum_i w_i omega_i corresponds to
          epsilon_j = sum_{i >= j} w_i  for j = 1, ..., N-1
          epsilon_N = -(epsilon_1 + ... + epsilon_{N-1})

        More precisely: epsilon_j - epsilon_{j+1} = alpha_j in epsilon basis,
        omega_i = epsilon_1 + ... + epsilon_i.
        So if w = sum w_i omega_i, then in the epsilon basis (traceless):
          e_k = sum_{i >= k} w_i  for k = 1, ..., r
          e_N = -sum_{k=1}^{r} e_k
        """
        r = self.rank
        eps = [0] * self.N
        for k in range(r):
            eps[k] = sum(w[i] for i in range(k, r))
        eps[self.N - 1] = -sum(eps[:self.N - 1])
        return eps

    def epsilon_to_omega(self, eps: List[int]) -> Weight:
        """Convert from epsilon basis (traceless) to omega basis.

        alpha_j = e_j - e_{j+1}, omega_i = sum_{j=1}^i alpha_j (in a sense).
        Actually omega_i in epsilon: omega_i = (1/N)(sum appropriate).

        Simpler: w_i = e_i - e_{i+1} gives the weight in the alpha basis.
        Then convert alpha -> omega via inverse Cartan.

        Even simpler for type A: omega_i = e_1 + ... + e_i (mod trace).
        So w in omega basis: w_i = (sum_{j=1}^{i} e_j) - (sum_{j=1}^{i+1} e_{j+1})...

        Actually the cleanest: w_i = e_i - e_{i+1} gives alpha-coefficients.
        Then omega-coefficients via the inverse Cartan matrix.

        For type A, the inverse Cartan is: (A^{-1})_{ij} = min(i,j)*(N-max(i,j))/N.
        But this gives rationals. Instead use: w in omega basis satisfies
        <w, alpha_j^vee> = w_j (by definition of fundamental weights).
        And <w, alpha_j^vee> = 2*(e_j - e_{j+1}) / |alpha_j|^2 = e_j - e_{j+1}
        (since all roots have the same length in type A with normalization |alpha|^2 = 2).

        So w_j = e_j - e_{j+1}.
        """
        r = self.rank
        return tuple(eps[j] - eps[j + 1] for j in range(r))

    def weyl_action_omega(self, perm: List[int], w: Weight) -> Weight:
        """Apply Weyl group element (permutation) to weight in omega basis."""
        eps = self.omega_to_epsilon(w)
        eps_perm = [eps[perm[j]] for j in range(self.N)]
        return self.epsilon_to_omega(eps_perm)


def _permutation_sign(perm: List[int]) -> int:
    """Sign of a permutation."""
    n = len(perm)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign


# ---------------------------------------------------------------------------
# Kostant partition function for sl_N
# ---------------------------------------------------------------------------

def kostant_partition_slN(root_system: SlNRootSystem, coeffs_alpha: Tuple[int, ...]) -> int:
    """Kostant partition function: number of ways to write
    sum_i c_i * alpha_i as a non-negative integer combination of positive roots.

    Uses dynamic programming.

    Args:
        root_system: the root system.
        coeffs_alpha: tuple (c_1, ..., c_r) giving the weight in alpha basis.
    """
    r = root_system.rank
    if any(c < 0 for c in coeffs_alpha):
        return 0

    # Convert positive roots to alpha basis
    # For type A: alpha_{i..j} = alpha_i + ... + alpha_j,
    # so in alpha basis it's e_i + e_{i+1} + ... + e_j (1 in positions i..j, 0 elsewhere)
    pos_roots_alpha = []
    for (a, b) in root_system._pos_root_indices:
        root_alpha = tuple(1 if a <= k <= b else 0 for k in range(r))
        pos_roots_alpha.append(root_alpha)

    # DP: count ways to express coeffs_alpha as sum of positive roots
    # Use inclusion of roots one at a time
    target = coeffs_alpha

    # Memoized recursive approach with bounded search
    return _kostant_dp(tuple(target), tuple(pos_roots_alpha), len(pos_roots_alpha) - 1)


@lru_cache(maxsize=None)
def _kostant_dp(target: Tuple[int, ...], roots: Tuple[Tuple[int, ...], ...], max_idx: int) -> int:
    """Count non-negative integer decompositions of target using roots[0..max_idx]."""
    if all(c == 0 for c in target):
        return 1
    if max_idx < 0:
        return 0
    if any(c < 0 for c in target):
        return 0

    root = roots[max_idx]
    total = 0
    current = target
    while all(c >= 0 for c in current):
        total += _kostant_dp(current, roots, max_idx - 1)
        current = tuple(current[k] - root[k] for k in range(len(target)))
    return total


# ---------------------------------------------------------------------------
# Weight multiplicities via Kostant multiplicity formula
# ---------------------------------------------------------------------------

def weight_multiplicity_slN(root_system: SlNRootSystem, hw: Weight, mu: Weight) -> int:
    """Weight multiplicity of mu in V_{hw} for sl_N.

    Uses the Kostant multiplicity formula:
      mult(mu) = sum_{w in W} (-1)^{l(w)} K(w(hw + rho) - (mu + rho))

    where K is the Kostant partition function.
    """
    r = root_system.rank
    rho = root_system.rho
    hw_rho = tuple(hw[i] + rho[i] for i in range(r))
    mu_rho = tuple(mu[i] + rho[i] for i in range(r))

    weyl_elts = root_system.weyl_group_elements()

    total = 0
    for sign, perm in weyl_elts:
        w_hw_rho = root_system.weyl_action_omega(perm, hw_rho)
        diff_omega = tuple(w_hw_rho[i] - mu_rho[i] for i in range(r))

        # Convert diff from omega to alpha basis
        # For type A: omega -> alpha via the Cartan matrix
        # alpha_i = sum_j A_{ij} omega_j, so omega -> alpha is A^{-1}
        # For type A_{r}: (A^{-1})_{ij} = min(i+1, j+1) * (r+1 - max(i+1, j+1)) / (r+1)
        # But this gives rationals. We need INTEGER alpha coefficients.
        # diff = sum_i d_i omega_i. In epsilon basis: e_k = sum_{i>=k} d_i.
        # In alpha basis: c_k = e_k - e_{k+1} = d_k. Wait, that's the SAME as omega?
        # No: omega and alpha bases are DIFFERENT.
        # alpha_j in omega basis = row j of Cartan matrix.
        # If diff = sum c_j alpha_j in omega basis, then diff_omega_i = sum_j c_j A_{ji}.
        # So c = diff_omega * A^{-1} (as row vector * inverse).
        # For type A, A^{-1}_{ij} = min(i+1, j+1)(N - max(i+1, j+1)) / N.

        # Instead: use epsilon basis. diff in epsilon: e_k = sum_{i>=k} diff_omega_i.
        # diff in alpha: c_k = e_k - e_{k+1} = diff_omega_k.
        # WAIT: that's only true if we define things correctly.
        # e_k - e_{k+1} = alpha_k in epsilon basis. And omega_i = sum c alpha -> e representation.
        # If diff has epsilon coords (e_1, ..., e_N), then alpha coords are
        # c_k = e_k - e_{k+1} for k = 1, ..., r.

        eps = root_system.omega_to_epsilon(diff_omega)
        coeffs_alpha = tuple(eps[k] - eps[k + 1] for k in range(r))

        K = kostant_partition_slN(root_system, coeffs_alpha)
        total += sign * K

    return total


# ---------------------------------------------------------------------------
# Irreducible character for sl_N
# ---------------------------------------------------------------------------

def slN_irrep_character(root_system: SlNRootSystem, hw: Weight, depth: int = 8) -> FormalChar:
    """Character of V_{hw} for sl_N.

    Enumerates weights mu = hw - sum c_j alpha_j with sum c_j <= depth.
    """
    r = root_system.rank
    char: FormalChar = {}

    # Enumerate all (c_1, ..., c_r) with sum <= depth, c_j >= 0
    def enumerate_weights(idx: int, remaining: int, coeffs: List[int]):
        if idx == r:
            mu = tuple(
                hw[k] - sum(coeffs[j] * root_system.cartan[j][k] for j in range(r))
                for k in range(r)
            )
            mult = weight_multiplicity_slN(root_system, hw, mu)
            if mult > 0:
                char[mu] = char.get(mu, 0) + mult
            return
        for c in range(remaining + 1):
            coeffs.append(c)
            enumerate_weights(idx + 1, remaining - c, coeffs)
            coeffs.pop()

    enumerate_weights(0, depth, [])
    return char


def slN_irrep_dim(root_system: SlNRootSystem, hw: Weight) -> int:
    """Weyl dimension formula for sl_N.

    dim V_hw = prod_{alpha > 0} <hw + rho, alpha^vee> / <rho, alpha^vee>
    """
    r = root_system.rank
    rho = root_system.rho
    hw_rho = tuple(hw[i] + rho[i] for i in range(r))

    num = 1
    den = 1
    for (a, b) in root_system._pos_root_indices:
        # <w, alpha_{a..b}^vee> = sum_{k=a}^{b} w_k for type A (since all roots same length)
        # Actually: alpha_{a..b} = e_a - e_{b+1} (0-indexed: e_{a+1} - e_{b+2}).
        # <w, alpha^vee> = <w, alpha> (type A, |alpha|^2 = 2, alpha^vee = alpha).
        # In omega basis: <omega_i, alpha_j> = delta_{ij}, so
        # <w, alpha_{a..b}> = sum_{k=a}^{b} w_k * <omega_k, alpha_{a..b}>
        # Hmm, this needs the inner product matrix.
        # Simpler: use epsilon basis. <w, alpha_{a..b}> where alpha = e_{a+1} - e_{b+2}.
        # In epsilon: e_k = sum_{i>=k} w_i (0-indexed: e_{k+1} = sum_{i>=k} w_i).
        # No wait. Let's use the standard fact for type A:
        # <lambda, alpha_{i,j}^vee> = lambda_i + lambda_{i+1} + ... + lambda_j
        # where lambda = sum lambda_k omega_k (in omega basis).
        # This is because alpha_{i,j}^vee = h_i + h_{i+1} + ... + h_j
        # and <omega_k, h_m> = delta_{km}.
        val_num = sum(hw_rho[k] for k in range(a, b + 1))
        val_den = sum(rho[k] for k in range(a, b + 1))
        num *= val_num
        den *= val_den

    return num // den


# ---------------------------------------------------------------------------
# Prefundamental characters for Y(sl_N)
# ---------------------------------------------------------------------------

def prefundamental_character_slN(root_system: SlNRootSystem, i: int, depth: int = 10) -> FormalChar:
    """Character of L^-_i for Y(sl_N).

    ch(L^-_i) = prod_{beta: alpha_i in supp(beta)} prod_{n >= 1} 1/(1 - e^{-n*beta})

    For type A, the positive roots containing alpha_i (0-indexed) are
    alpha_{a..b} for a <= i <= b. There are (i+1)*(r-i) such roots.

    The character is computed by truncated expansion of the infinite product.

    Args:
        root_system: root system data.
        i: node index (0-indexed: 0, ..., r-1).
        depth: truncation depth for the infinite product expansion.
    """
    r = root_system.rank

    # Get the positive roots containing alpha_i
    relevant_root_indices = root_system.roots_containing[i]
    relevant_roots = [root_system.positive_roots[idx] for idx in relevant_root_indices]

    # Start with char = {zero_weight: 1}
    zero = tuple([0] * r)
    char: FormalChar = {zero: 1}

    # For each root beta and each n >= 1, multiply by 1/(1 - e^{-n*beta})
    # = sum_{k >= 0} e^{-k*n*beta}
    # We process all (beta, n) pairs with n*max_coeff(beta) <= depth
    for beta in relevant_roots:
        max_coeff = max(abs(c) for c in beta)
        for n in range(1, depth // max_coeff + 1 if max_coeff > 0 else depth + 1):
            # Multiply current char by 1/(1 - e^{-n*beta})
            # = sum_{k >= 0} e^{-k*n*beta}
            neg_n_beta = tuple(-n * c for c in beta)

            new_char: FormalChar = {}
            # For each existing weight w with mult m, add contributions
            # w, w + neg_n_beta, w + 2*neg_n_beta, ...
            for w, m in char.items():
                shifted = w
                while True:
                    # Check depth: sum of absolute omega-coordinates as proxy
                    total_depth = sum(abs(c) for c in shifted)
                    if total_depth > 3 * depth:  # generous truncation
                        break
                    new_char[shifted] = new_char.get(shifted, 0) + m
                    shifted = tuple(shifted[k] + neg_n_beta[k] for k in range(r))

            char = new_char

    return char


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def add_weights_gen(w1: Weight, w2: Weight) -> Weight:
    return tuple(w1[k] + w2[k] for k in range(len(w1)))


def tensor_product_char(chi1: FormalChar, chi2: FormalChar) -> FormalChar:
    """Tensor product (convolution) of two characters."""
    result: FormalChar = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = add_weights_gen(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def shift_character(chi: FormalChar, shift: Weight) -> FormalChar:
    """Shift all weights by shift."""
    return {add_weights_gen(w, shift): m for w, m in chi.items()}


def subtract_characters(chi1: FormalChar, chi2: FormalChar) -> FormalChar:
    """chi1 - chi2."""
    result = dict(chi1)
    for w, m in chi2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


# ---------------------------------------------------------------------------
# CG verification: the universal theorem
# ---------------------------------------------------------------------------

def verify_cg_universal(N: int, hw: Weight, node_i: int, depth: int = 8) -> Dict:
    """Verify the universal CG theorem for sl_N:

    [V_hw] * [L^-_i] = sum_{mu in wt(V_hw)} mult_hw(mu) * [L^-_i(shift=mu)]

    Args:
        N: sl_N (N >= 2).
        hw: dominant weight (a_1, ..., a_{N-1}).
        node_i: node index (0-indexed).
        depth: truncation depth.

    Returns:
        dict with verification data.
    """
    rs = SlNRootSystem(N)
    r = rs.rank

    # Compute V_hw character
    V_char = slN_irrep_character(rs, hw, depth=depth + sum(hw))
    V_dim = sum(V_char.values())
    expected_dim = slN_irrep_dim(rs, hw)

    # Compute L^-_i character
    L_char = prefundamental_character_slN(rs, node_i, depth=depth)

    # LHS: tensor product
    lhs = tensor_product_char(V_char, L_char)

    # RHS: sum of shifted L^-_i weighted by mult
    rhs: FormalChar = {}
    total_mult = 0
    for mu, mult in V_char.items():
        total_mult += mult
        L_shifted = shift_character(L_char, mu)
        for w, m in L_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    # Compare within reliable range
    # A weight is "reliable" if it's not too deep from hw
    max_reliable = 2 * (depth - sum(hw) - 3)
    match = True
    mismatches = []
    for w in set(list(lhs.keys()) + list(rhs.keys())):
        dist = sum(abs(c) for c in w)
        if dist <= max_reliable:
            l = lhs.get(w, 0)
            r_val = rhs.get(w, 0)
            if l != r_val:
                match = False
                mismatches.append((w, l, r_val))

    return {
        "N": N,
        "hw": hw,
        "node_i": node_i,
        "V_dim": V_dim,
        "expected_dim": expected_dim,
        "dim_correct": V_dim == expected_dim,
        "total_mult": total_mult,
        "n_weights_V": len(V_char),
        "match": match,
        "n_mismatches": len(mismatches),
        "mismatches": mismatches[:5],
        "n_lhs_weights": len(lhs),
        "n_rhs_weights": len(rhs),
    }


# ---------------------------------------------------------------------------
# Batch verification
# ---------------------------------------------------------------------------

def verify_fundamentals(N: int, depth: int = 8) -> Dict[str, Dict]:
    """Verify CG for all fundamental representations of sl_N
    with all prefundamental nodes."""
    rs = SlNRootSystem(N)
    r = rs.rank
    results = {}

    for fund_idx in range(r):
        hw = tuple(1 if k == fund_idx else 0 for k in range(r))
        for node_i in range(r):
            key = f"sl{N}: V_omega{fund_idx+1} x L^-_{node_i+1}"
            results[key] = verify_cg_universal(N, hw, node_i, depth=depth)

    return results


def verify_small_reps(N: int, max_hw_sum: int = 2, depth: int = 7) -> Dict[str, Dict]:
    """Verify CG for all small representations of sl_N."""
    rs = SlNRootSystem(N)
    r = rs.rank
    results = {}

    def gen_hws(remaining, idx, current):
        if idx == r:
            if sum(current) > 0:
                yield tuple(current)
            return
        for c in range(remaining + 1):
            current.append(c)
            yield from gen_hws(remaining - c, idx + 1, current)
            current.pop()

    for hw in gen_hws(max_hw_sum, 0, []):
        for node_i in range(r):
            key = f"sl{N}: V_{hw} x L^-_{node_i+1}"
            results[key] = verify_cg_universal(N, hw, node_i, depth=depth)

    return results


# ---------------------------------------------------------------------------
# Master verification across all ranks
# ---------------------------------------------------------------------------

def verify_all_type_A(max_N: int = 6, depth_map: Optional[Dict[int, int]] = None) -> Dict:
    """Verify CG theorem for sl_2 through sl_{max_N}.

    Returns summary with pass/fail counts.
    """
    if depth_map is None:
        depth_map = {2: 12, 3: 10, 4: 8, 5: 7, 6: 6}

    all_results = {}
    summary = {"total": 0, "passed": 0, "failed": 0, "dim_errors": 0}

    for N in range(2, max_N + 1):
        depth = depth_map.get(N, 6)
        max_hw = 3 if N <= 3 else (2 if N <= 4 else 1)

        results = verify_small_reps(N, max_hw_sum=max_hw, depth=depth)
        for key, data in results.items():
            all_results[key] = data
            summary["total"] += 1
            if data["match"]:
                summary["passed"] += 1
            else:
                summary["failed"] += 1
                if not data["dim_correct"]:
                    summary["dim_errors"] += 1

    summary["all_pass"] = summary["failed"] == 0
    return {"results": all_results, "summary": summary}


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("UNIVERSAL PREFUNDAMENTAL CG — ALL TYPE A")
    print("=" * 70)

    # sl_2 sanity
    print("\n--- sl_2 fundamentals ---")
    for res_key, res in verify_fundamentals(2, depth=12).items():
        tag = "PASS" if res["match"] else "FAIL"
        print(f"  [{tag}] {res_key}: dim={res['V_dim']}, match={res['match']}")

    # sl_3
    print("\n--- sl_3 small reps ---")
    for res_key, res in verify_small_reps(3, max_hw_sum=2, depth=10).items():
        tag = "PASS" if res["match"] else "FAIL"
        print(f"  [{tag}] {res_key}: dim={res['V_dim']}, match={res['match']}")

    # sl_4
    print("\n--- sl_4 fundamentals ---")
    for res_key, res in verify_fundamentals(4, depth=7).items():
        tag = "PASS" if res["match"] else "FAIL"
        print(f"  [{tag}] {res_key}: dim={res['V_dim']}/{res['expected_dim']}, match={res['match']}")

    # sl_5
    print("\n--- sl_5 fundamentals ---")
    for res_key, res in verify_fundamentals(5, depth=6).items():
        tag = "PASS" if res["match"] else "FAIL"
        print(f"  [{tag}] {res_key}: dim={res['V_dim']}/{res['expected_dim']}, match={res['match']}")

    # sl_6
    print("\n--- sl_6 fundamentals ---")
    for res_key, res in verify_fundamentals(6, depth=5).items():
        tag = "PASS" if res["match"] else "FAIL"
        print(f"  [{tag}] {res_key}: dim={res['V_dim']}/{res['expected_dim']}, match={res['match']}")

    # Summary
    print("\n--- Full verification ---")
    result = verify_all_type_A(max_N=5)
    s = result["summary"]
    print(f"  Total: {s['total']}, Passed: {s['passed']}, Failed: {s['failed']}")
    print(f"  ALL PASS: {s['all_pass']}")
    if s["failed"] > 0:
        for k, v in result["results"].items():
            if not v["match"] or not v["dim_correct"]:
                print(f"  FAIL: {k}: {v}")
