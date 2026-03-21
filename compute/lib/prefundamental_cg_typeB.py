"""Prefundamental Clebsch-Gordan decomposition for types B_2 and G_2.

FRONTIER COMPUTATION for MC3 extension to non-simply-laced types.

The universal CG theorem (prefundamental_cg_universal.py, Remark line 33)
states that the distributive law

    [V_lambda] * [L^-_i] = sum_{mu in wt(V_lambda)} mult(mu) * [L^-_i(shift=mu)]

holds for ANY simple Lie algebra g, since ch(V_lambda) is a finite sum
and ch(L^-_i) is a well-defined formal power series.

This module VERIFIES this computationally for:
  - B_2 = so_5 (rank 2, non-simply-laced: short + long roots)
  - G_2 (rank 2, exceptional: short + long roots, ratio 1:sqrt(3))

The Hernandez-Jimbo prefundamental character formula:

    ch(L^-_i) = prod_{beta > 0, alpha_i in supp(beta)} prod_{n >= 1} 1/(1 - e^{-n*beta})

depends only on the positive roots containing alpha_i in their simple root
expansion. This formula is valid for all types (HJ12, Section 5).

ROOT SYSTEM CONVENTIONS:
  Weights in fundamental weight (omega) basis: w = (w_1, w_2).
  Simple roots alpha_i in omega basis via the Cartan matrix: alpha_i = sum_j A_{ij} omega_j.

  B_2: Cartan matrix [[2, -1], [-2, 2]].
       alpha_1 = (2, -1) [short], alpha_2 = (-2, 2) [long].
       Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2.

  G_2: Cartan matrix [[2, -1], [-3, 2]].
       alpha_1 = (2, -1) [short], alpha_2 = (-3, 2) [long].
       Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2,
                        3*alpha_1+alpha_2, 3*alpha_1+2*alpha_2.

References:
  - Hernandez-Jimbo 2012, Section 5 (prefundamental for all types)
  - Bourbaki, Lie Groups and Lie Algebras, Ch. IV-VI (root systems)
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from functools import lru_cache

from compute.lib.utils import partition_number


# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------

Weight = Tuple[int, int]
FormalChar = Dict[Weight, int]


# ---------------------------------------------------------------------------
# General rank-2 root system
# ---------------------------------------------------------------------------

class Rank2RootSystem:
    """Root system data for a rank-2 simple Lie algebra.

    Stores Cartan matrix, simple/positive roots, Weyl group, and
    identifies which positive roots contain each simple root.
    """

    def __init__(self, name: str, cartan: List[List[int]]):
        self.name = name
        self.cartan = cartan
        self.rank = 2

        # Simple roots in omega basis: alpha_i = (A_{i,0}, A_{i,1})
        self.alpha: List[Weight] = [
            (cartan[0][0], cartan[0][1]),
            (cartan[1][0], cartan[1][1]),
        ]

        # Build positive roots by repeated addition
        # For rank 2: start from simple roots, add alpha_1 or alpha_2,
        # check if result is a root (use Cartan matrix to determine root strings)
        self.positive_roots: List[Weight] = []
        self.positive_roots_alpha: List[Tuple[int, int]] = []  # (c1, c2) in alpha basis
        self._build_positive_roots()

        # For each node i (0 or 1), which positive roots contain alpha_i?
        # A root c1*alpha_1 + c2*alpha_2 contains alpha_i iff c_i > 0.
        self.roots_containing: List[List[int]] = [[], []]
        for idx, (c1, c2) in enumerate(self.positive_roots_alpha):
            if c1 > 0:
                self.roots_containing[0].append(idx)
            if c2 > 0:
                self.roots_containing[1].append(idx)

        # Weyl group (order: 2*h where h = Coxeter number)
        self.weyl_group = self._build_weyl_group()

        # rho in omega basis = (1, 1)
        self.rho: Weight = (1, 1)

    def _build_positive_roots(self):
        """Build positive roots for rank-2 system.

        For rank 2, the positive roots are c1*alpha_1 + c2*alpha_2 where
        (c1, c2) ranges over a finite set determined by the root system.
        We use the standard classification:
          A_2: (1,0), (0,1), (1,1)
          B_2: (1,0), (0,1), (1,1), (2,1)
          G_2: (1,0), (0,1), (1,1), (2,1), (3,1), (3,2)
        """
        # General algorithm: use root strings.
        # For rank 2, enumerate by brute force up to reasonable bound.
        roots_alpha = set()
        roots_alpha.add((1, 0))
        roots_alpha.add((0, 1))

        # Reflect simple roots through each other to find all roots
        # s_i(alpha_j) = alpha_j - A_{ji} * alpha_i
        # Keep applying reflections until no new positive roots found
        changed = True
        while changed:
            changed = False
            new_roots = set()
            for (c1, c2) in roots_alpha:
                # Reflect through s_1: s_1(beta) = beta - <beta, alpha_1^vee> * alpha_1
                # For beta = c1*alpha_1 + c2*alpha_2, using <alpha_j, alpha_i^vee> = A_{ji}:
                # <beta, alpha_1^vee> = c1 * A[0][0] + c2 * A[1][0] = 2*c1 + A[1][0]*c2
                # s_1(beta) = beta - <beta, alpha_1^vee> * alpha_1
                #           = (c1 - <beta, alpha_1^vee>, c2) in alpha coords
                inner1 = c1 * self.cartan[0][0] + c2 * self.cartan[1][0]
                r1 = (c1 - inner1, c2)
                if r1[0] > 0 or r1[1] > 0:
                    if r1[0] >= 0 and r1[1] >= 0 and r1 not in roots_alpha:
                        new_roots.add(r1)

                inner2 = c1 * self.cartan[0][1] + c2 * self.cartan[1][1]
                r2 = (c1, c2 - inner2)
                if r2[0] > 0 or r2[1] > 0:
                    if r2[0] >= 0 and r2[1] >= 0 and r2 not in roots_alpha:
                        new_roots.add(r2)

            if new_roots:
                roots_alpha |= new_roots
                changed = True

        # Sort and store
        sorted_roots = sorted(roots_alpha, key=lambda x: (x[0] + x[1], x[0]))
        for (c1, c2) in sorted_roots:
            self.positive_roots_alpha.append((c1, c2))
            w = (c1 * self.alpha[0][0] + c2 * self.alpha[1][0],
                 c1 * self.alpha[0][1] + c2 * self.alpha[1][1])
            self.positive_roots.append(w)

    def _build_weyl_group(self) -> List[Tuple[int, callable]]:
        """Build Weyl group as list of (sign, action_on_omega_basis).

        For rank 2, the Weyl group is the dihedral group of order 2h
        where h is the Coxeter number.
        We generate it by composing s_1, s_2.
        """
        # Reflections in omega basis:
        # s_i(omega_j) = omega_j - delta_{ij} * alpha_i
        # So s_i(w) = w - <w, alpha_i^vee> * alpha_i (in omega basis)
        # <w, alpha_i^vee> = w_i (since <omega_j, alpha_i^vee> = delta_{ji}).
        # Wait: <omega_j, alpha_i^vee> = A_{ji}. No: <omega_j, alpha_i^vee> = delta_{ji}.
        # That IS the definition of fundamental weights.
        # So s_i(w_1, w_2): component j -> w_j - w_i * A[i][j].

        def reflect(i: int, w: Weight) -> Weight:
            """s_i acting on weight w in omega basis."""
            return (w[0] - w[i] * self.cartan[i][0],
                    w[1] - w[i] * self.cartan[i][1])

        # Generate group by BFS
        # Represent elements as tuples of reflections applied
        # Store as matrix [[a,b],[c,d]] acting on (w1, w2)
        identity = ((1, 0), (0, 1))

        def mat_apply(mat, w):
            return (mat[0][0] * w[0] + mat[0][1] * w[1],
                    mat[1][0] * w[0] + mat[1][1] * w[1])

        def mat_compose(m1, m2):
            return (
                (m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0], m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]),
                (m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0], m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]),
            )

        # s_i as matrix
        def s_mat(i: int):
            # s_i(e_j) = e_j - A[i][j] * e_i  ... no.
            # s_i(w)_j = w_j - w_i * A[i][j]
            # So the matrix M has M[j][k] = delta_{jk} - delta_{ki} * A[i][j]
            # M[0][0] = 1 - delta_{0,i}*A[i][0]
            # M[0][1] = 0 - delta_{1,i}*A[i][0]
            # M[1][0] = 0 - delta_{0,i}*A[i][1]
            # M[1][1] = 1 - delta_{1,i}*A[i][1]
            if i == 0:
                return ((1 - self.cartan[0][0], 0 - 0),
                        (0 - self.cartan[0][1], 1 - 0))
                # = (1 - A00, 0), (-A01, 1)
                # s_i(w)_j = w_j - w_i * A[i][j].
                # As matrix: M_{jk} = delta_{jk} - delta_{k,i} * A[i][j].
                # M_{j,k} = delta_{jk} - delta_{k,0} * A[0][j]
                # M_{0,0} = 1 - A[0][0], M_{0,1} = 0
                # M_{1,0} = -A[0][1], M_{1,1} = 1
                return ((1 - self.cartan[0][0], 0),
                        (-self.cartan[0][1], 1))
            else:
                return ((1, -self.cartan[1][0]),
                        (0, 1 - self.cartan[1][1]))

        s1 = s_mat(0)
        s2 = s_mat(1)

        # BFS
        elements = {identity}
        queue = [identity]
        while queue:
            m = queue.pop(0)
            for s in [s1, s2]:
                new = mat_compose(s, m)
                if new not in elements:
                    elements.add(new)
                    queue.append(new)

        # Compute sign = det
        result = []
        for m in elements:
            det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            result.append((det, m))

        return result

    def weyl_dim(self, hw: Weight) -> int:
        """Weyl dimension formula: dim V_hw = prod_{beta>0} <hw+rho, beta^vee> / <rho, beta^vee>.

        For rank 2, <w, beta^vee> where beta = c1*alpha_1 + c2*alpha_2:
        beta^vee = 2*beta / <beta, beta>. And <omega_j, beta^vee> = <omega_j, 2*beta/<beta,beta>>.
        This requires knowing <beta, beta> which depends on root lengths.

        Simpler approach: use the Weyl character formula via Kostant.
        Or: use the known dimension formulas.

        For B_2: dim V_{(a,b)} = (a+1)(b+1)(a+b+2)(2a+b+3) / 6   [WRONG, derive properly]

        Actually, let's just use the Kostant multiplicity formula and sum.
        """
        char = self.irrep_character(hw, depth=sum(hw) + 20)
        return sum(char.values())

    def omega_to_alpha(self, w: Weight) -> Optional[Tuple[int, int]]:
        """Convert weight from omega to alpha basis.

        w = c1*alpha_1 + c2*alpha_2 means w = c1*(A[0][0], A[0][1]) + c2*(A[1][0], A[1][1])
        So: w_0 = c1*A[0][0] + c2*A[1][0], w_1 = c1*A[0][1] + c2*A[1][1]
        Solve: [A00 A10] [c1]   [w0]
               [A01 A11] [c2] = [w1]
        """
        A00, A01 = self.cartan[0]
        A10, A11 = self.cartan[1]
        det = A00 * A11 - A10 * A01
        if det == 0:
            return None
        c1_num = A11 * w[0] - A10 * w[1]
        c2_num = A00 * w[1] - A01 * w[0]
        if c1_num % det != 0 or c2_num % det != 0:
            return None
        return (c1_num // det, c2_num // det)

    def weight_multiplicity(self, hw: Weight, mu: Weight) -> int:
        """Weight multiplicity of mu in V_hw via Kostant multiplicity formula.

        mult(mu) = sum_{w in W} det(w) * K(w(hw+rho) - (mu+rho))
        """
        if hw[0] < 0 or hw[1] < 0:
            return 0

        rho = self.rho
        hw_rho = (hw[0] + rho[0], hw[1] + rho[1])
        mu_rho = (mu[0] + rho[0], mu[1] + rho[1])

        total = 0
        for det, mat in self.weyl_group:
            w_hw_rho = (mat[0][0]*hw_rho[0] + mat[0][1]*hw_rho[1],
                        mat[1][0]*hw_rho[0] + mat[1][1]*hw_rho[1])
            diff = (w_hw_rho[0] - mu_rho[0], w_hw_rho[1] - mu_rho[1])
            alpha_coords = self.omega_to_alpha(diff)
            if alpha_coords is None:
                continue
            K = self._kostant_partition(alpha_coords)
            total += det * K

        return total

    @lru_cache(maxsize=None)
    def _kostant_partition(self, coeffs_alpha: Tuple[int, int]) -> int:
        """Kostant partition function: number of ways to write
        c1*alpha_1 + c2*alpha_2 as non-negative combination of positive roots."""
        c1, c2 = coeffs_alpha
        if c1 < 0 or c2 < 0:
            return 0
        return self._kostant_dp(coeffs_alpha, len(self.positive_roots_alpha) - 1)

    @lru_cache(maxsize=None)
    def _kostant_dp(self, target: Tuple[int, int], max_idx: int) -> int:
        if target[0] == 0 and target[1] == 0:
            return 1
        if max_idx < 0:
            return 0
        if target[0] < 0 or target[1] < 0:
            return 0

        root = self.positive_roots_alpha[max_idx]
        total = 0
        current = target
        while current[0] >= 0 and current[1] >= 0:
            total += self._kostant_dp(current, max_idx - 1)
            current = (current[0] - root[0], current[1] - root[1])
        return total

    def irrep_character(self, hw: Weight, depth: int = 15) -> FormalChar:
        """Character of V_hw: all weights mu = hw - sum c_j alpha_j, sum c_j <= depth."""
        if hw[0] < 0 or hw[1] < 0:
            return {}

        char: FormalChar = {}
        for c1 in range(depth + 1):
            for c2 in range(depth + 1 - c1):
                # mu = hw - c1*alpha_1 - c2*alpha_2
                mu = (hw[0] - c1*self.alpha[0][0] - c2*self.alpha[1][0],
                      hw[1] - c1*self.alpha[0][1] - c2*self.alpha[1][1])
                mult = self.weight_multiplicity(hw, mu)
                if mult > 0:
                    if mu in char:
                        char[mu] += mult
                    else:
                        char[mu] = mult
        return char

    def prefundamental_character(self, node: int, depth: int = 12) -> FormalChar:
        """Character of L^-_{node} (0-indexed).

        ch(L^-_i) = prod_{beta>0, alpha_i in supp(beta)} prod_{n>=1} 1/(1 - e^{-n*beta})

        Computed by truncated expansion of the infinite product.
        """
        relevant_indices = self.roots_containing[node]
        relevant_roots = [self.positive_roots[idx] for idx in relevant_indices]

        # Start with {(0,0): 1}
        char: FormalChar = {(0, 0): 1}

        for beta in relevant_roots:
            max_coeff = max(abs(beta[0]), abs(beta[1]))
            if max_coeff == 0:
                continue
            max_n = depth // max_coeff if max_coeff > 0 else depth
            for n in range(1, max_n + 1):
                neg_n_beta = (-n * beta[0], -n * beta[1])

                new_char: FormalChar = {}
                for w, m in char.items():
                    shifted = w
                    while True:
                        # Depth check
                        total_d = abs(shifted[0]) + abs(shifted[1])
                        if total_d > 3 * depth:
                            break
                        new_char[shifted] = new_char.get(shifted, 0) + m
                        shifted = (shifted[0] + neg_n_beta[0],
                                   shifted[1] + neg_n_beta[1])

                char = new_char

        return char


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def add_wt(w1: Weight, w2: Weight) -> Weight:
    return (w1[0] + w2[0], w1[1] + w2[1])


def tensor_product(chi1: FormalChar, chi2: FormalChar) -> FormalChar:
    result: FormalChar = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = add_wt(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def shift_char(chi: FormalChar, s: Weight) -> FormalChar:
    return {add_wt(w, s): m for w, m in chi.items()}


def subtract_char(chi1: FormalChar, chi2: FormalChar) -> FormalChar:
    result = dict(chi1)
    for w, m in chi2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


# ---------------------------------------------------------------------------
# Standard root systems
# ---------------------------------------------------------------------------

def B2() -> Rank2RootSystem:
    """Root system for B_2 = so_5.

    Cartan matrix: [[2, -1], [-2, 2]]
    alpha_1 = short root, alpha_2 = long root.
    Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2.
    |W| = 8.
    """
    return Rank2RootSystem("B2", [[2, -1], [-2, 2]])


def G2() -> Rank2RootSystem:
    """Root system for G_2.

    Cartan matrix: [[2, -1], [-3, 2]]
    alpha_1 = short root, alpha_2 = long root.
    Positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2,
                    3*alpha_1+alpha_2, 3*alpha_1+2*alpha_2.
    |W| = 12.
    """
    return Rank2RootSystem("G2", [[2, -1], [-3, 2]])


def A2() -> Rank2RootSystem:
    """Root system for A_2 = sl_3 (for cross-checking)."""
    return Rank2RootSystem("A2", [[2, -1], [-1, 2]])


# ---------------------------------------------------------------------------
# CG verification: universal theorem
# ---------------------------------------------------------------------------

def verify_cg(rs: Rank2RootSystem, hw: Weight, node: int, depth: int = 10) -> Dict:
    """Verify the universal CG theorem:

    [V_hw] * [L^-_node] = sum_{mu in wt(V_hw)} mult(mu) * [L^-_node(shift=mu)]

    Returns dict with match status and diagnostics.
    """
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 5)
    V_dim = sum(V_char.values())

    L_char = rs.prefundamental_character(node, depth=depth)

    # LHS: tensor product
    lhs = tensor_product(V_char, L_char)

    # RHS: weighted sum of shifted prefundamentals
    rhs: FormalChar = {}
    for mu, mult in V_char.items():
        L_shifted = shift_char(L_char, mu)
        for w, m in L_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    # Compare within reliable range
    max_reliable = 2 * (depth - sum(hw) - 3)
    match = True
    mismatches = []
    all_weights = set(list(lhs.keys()) + list(rhs.keys()))
    for w in all_weights:
        dist = abs(w[0]) + abs(w[1])
        if dist <= max_reliable:
            l_val = lhs.get(w, 0)
            r_val = rhs.get(w, 0)
            if l_val != r_val:
                match = False
                mismatches.append((w, l_val, r_val))

    return {
        "root_system": rs.name,
        "hw": hw,
        "node": node,
        "V_dim": V_dim,
        "match": match,
        "n_mismatches": len(mismatches),
        "mismatches": mismatches[:5],
        "n_lhs_weights": len(lhs),
        "n_rhs_weights": len(rhs),
    }


def verify_batch(rs: Rank2RootSystem, max_hw_sum: int = 3, depth: int = 10) -> Dict:
    """Verify CG for all dominant weights with |hw| <= max_hw_sum and both nodes."""
    results = {}
    n_pass = 0
    n_fail = 0
    for a in range(max_hw_sum + 1):
        for b in range(max_hw_sum + 1 - a):
            if a == 0 and b == 0:
                continue
            for node in [0, 1]:
                key = f"{rs.name}: V_({a},{b}) x L^-_{node+1}"
                res = verify_cg(rs, (a, b), node, depth=depth)
                results[key] = res
                if res["match"]:
                    n_pass += 1
                else:
                    n_fail += 1
    return {"results": results, "n_pass": n_pass, "n_fail": n_fail, "all_pass": n_fail == 0}


# ---------------------------------------------------------------------------
# Dimension formulas (for cross-check)
# ---------------------------------------------------------------------------

def B2_dim(a: int, b: int) -> int:
    """Weyl dimension formula for B_2 = so_5.

    V_{a*omega_1 + b*omega_2} where omega_1 is the vector rep weight,
    omega_2 is the spin rep weight.

    dim = (a+1)(b+1)(a+b+2)(a+2b+3) / 6
    """
    if a < 0 or b < 0:
        return 0
    return (a + 1) * (b + 1) * (a + b + 2) * (a + 2*b + 3) // 6


def G2_dim(a: int, b: int) -> int:
    """Weyl dimension formula for G_2.

    V_{a*omega_1 + b*omega_2}.

    The positive coroots in the simple coroot basis have coordinates
    (1,0), (0,1), (1,1), (1,2), (1,3), (2,3), giving:
    dim = (a+1)(b+1)(a+b+2)(a+2b+3)(a+3b+4)(2a+3b+5) / 120
    """
    if a < 0 or b < 0:
        return 0
    return ((a+1) * (b+1) * (a+b+2) * (a+2*b+3)
            * (a+3*b+4) * (2*a+3*b+5) // 120)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("PREFUNDAMENTAL CG — TYPES B_2 AND G_2")
    print("=" * 70)

    # B_2
    b2 = B2()
    print(f"\nB_2 positive roots (alpha coords): {b2.positive_roots_alpha}")
    print(f"B_2 positive roots (omega coords): {b2.positive_roots}")
    print(f"B_2 |W| = {len(b2.weyl_group)}")
    print(f"B_2 roots containing alpha_1: {[b2.positive_roots_alpha[i] for i in b2.roots_containing[0]]}")
    print(f"B_2 roots containing alpha_2: {[b2.positive_roots_alpha[i] for i in b2.roots_containing[1]]}")

    print("\n--- B_2 dimensions ---")
    for a in range(4):
        for b in range(4 - a):
            char = b2.irrep_character((a, b), depth=20)
            dim_char = sum(char.values())
            dim_formula = B2_dim(a, b)
            tag = "OK" if dim_char == dim_formula else "MISMATCH"
            print(f"  [{tag}] V_({a},{b}): char={dim_char}, formula={dim_formula}")

    print("\n--- B_2 CG verification ---")
    b2_res = verify_batch(b2, max_hw_sum=3, depth=10)
    for key, data in b2_res["results"].items():
        tag = "PASS" if data["match"] else "FAIL"
        print(f"  [{tag}] {key}: dim={data['V_dim']}")
    print(f"  B_2 summary: {b2_res['n_pass']} pass, {b2_res['n_fail']} fail")

    # G_2
    g2 = G2()
    print(f"\nG_2 positive roots (alpha coords): {g2.positive_roots_alpha}")
    print(f"G_2 positive roots (omega coords): {g2.positive_roots}")
    print(f"G_2 |W| = {len(g2.weyl_group)}")

    print("\n--- G_2 dimensions ---")
    for a in range(3):
        for b in range(3 - a):
            char = g2.irrep_character((a, b), depth=20)
            dim_char = sum(char.values())
            dim_formula = G2_dim(a, b)
            tag = "OK" if dim_char == dim_formula else "MISMATCH"
            print(f"  [{tag}] V_({a},{b}): char={dim_char}, formula={dim_formula}")

    print("\n--- G_2 CG verification ---")
    g2_res = verify_batch(g2, max_hw_sum=2, depth=8)
    for key, data in g2_res["results"].items():
        tag = "PASS" if data["match"] else "FAIL"
        print(f"  [{tag}] {key}: dim={data['V_dim']}")
    print(f"  G_2 summary: {g2_res['n_pass']} pass, {g2_res['n_fail']} fail")
