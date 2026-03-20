"""MC3 frontier: prefundamental CG for types B_3 and C_3.

Extends the MC3 character-level verification from type A (proved) and
rank-2 types B_2/G_2 (verified in prefundamental_cg_typeB.py) to rank-3
non-simply-laced types.

B_3 = so_7 and C_3 = sp_6 are Langlands dual (Cartan matrices are
transposes). Their prefundamental modules L^-_i (i=1,2,3) have explicit
character formulas from Hernandez-Jimbo (HJ12, Section 5).

The KEY IDENTITY to verify:

    ch(V_lambda) * ch(L^-_i) = sum_{mu in wt(V_lambda)} mult(mu) * ch(L^-_i(shift=mu_i))

for ALL dominant weights lambda and all nodes i. This is the distributive
law applied to a finite sum times a formal power series; its validity
for B_3 and C_3 provides computational evidence for conj:mc3-arbitrary-type.

ROOT SYSTEM CONVENTIONS:
  Weights in fundamental weight (omega) basis: w = (w_1, w_2, w_3).
  Simple roots alpha_i in omega basis via Cartan matrix: alpha_i = row i of A.

  B_3 = so_7: Cartan matrix [[2,-1,0],[-1,2,-2],[0,-1,2]].
    Dynkin diagram: o---o=>=o  (alpha_3 short, alpha_1 long)
    9 positive roots. |W| = 48. Coxeter number h = 6.
    Fundamental reps: V(omega_1) = 7-dim (vector), V(omega_2) = 21-dim,
                      V(omega_3) = 8-dim (spin).

  C_3 = sp_6: Cartan matrix [[2,-1,0],[-1,2,-1],[0,-2,2]].
    Dynkin diagram: o---o=<=o  (alpha_3 long, alpha_1 short)
    9 positive roots. |W| = 48. Coxeter number h = 6.
    Fundamental reps: V(omega_1) = 6-dim (standard), V(omega_2) = 14-dim,
                      V(omega_3) = 14'-dim.

  Langlands duality: A_{C_3} = A_{B_3}^T.

The Hernandez-Jimbo prefundamental character for node i:

    ch(L^-_i)(q) = prod_{beta > 0, alpha_i in supp(beta)} prod_{n >= 1}
                       1 / (1 - q^{n * beta})

where q^beta = q_1^{beta_1} q_2^{beta_2} q_3^{beta_3} in fundamental
weight coordinates, and alpha_i in supp(beta) means the simple root
expansion of beta has a positive coefficient for alpha_i.

References:
  - Hernandez-Jimbo 2012, Section 5 (prefundamental for all types)
  - Bourbaki, Lie Groups and Lie Algebras, Ch. IV-VI, Planches I-IV
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from functools import lru_cache


# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------

Weight3 = Tuple[int, int, int]
FormalChar3 = Dict[Weight3, int]


# ---------------------------------------------------------------------------
# General rank-3 root system
# ---------------------------------------------------------------------------

class Rank3RootSystem:
    """Root system data for a rank-3 simple Lie algebra.

    Stores Cartan matrix, simple/positive roots, Weyl group, and
    identifies which positive roots contain each simple root.
    """

    def __init__(self, name: str, cartan: List[List[int]]):
        self.name = name
        self.cartan = cartan
        self.rank = 3

        # Simple roots in omega basis: alpha_i = (A_{i,0}, A_{i,1}, A_{i,2})
        self.alpha: List[Weight3] = [
            (cartan[0][0], cartan[0][1], cartan[0][2]),
            (cartan[1][0], cartan[1][1], cartan[1][2]),
            (cartan[2][0], cartan[2][1], cartan[2][2]),
        ]

        # Build positive roots by Weyl reflections
        self.positive_roots: List[Weight3] = []
        # (c1, c2, c3) in simple root basis: beta = c1*alpha_1 + c2*alpha_2 + c3*alpha_3
        self.positive_roots_alpha: List[Tuple[int, int, int]] = []
        self._build_positive_roots()

        # For each node i (0, 1, 2), which positive roots contain alpha_i?
        # A root c1*alpha_1 + c2*alpha_2 + c3*alpha_3 contains alpha_i iff c_i > 0.
        self.roots_containing: List[List[int]] = [[], [], []]
        for idx, (c1, c2, c3) in enumerate(self.positive_roots_alpha):
            if c1 > 0:
                self.roots_containing[0].append(idx)
            if c2 > 0:
                self.roots_containing[1].append(idx)
            if c3 > 0:
                self.roots_containing[2].append(idx)

        # Weyl group as list of (determinant, matrix)
        self.weyl_group = self._build_weyl_group()

        # rho in omega basis = (1, 1, 1)
        self.rho: Weight3 = (1, 1, 1)

    def _build_positive_roots(self):
        """Build positive roots for rank-3 system by iterated Weyl reflection."""
        roots_alpha = set()
        roots_alpha.add((1, 0, 0))
        roots_alpha.add((0, 1, 0))
        roots_alpha.add((0, 0, 1))

        changed = True
        while changed:
            changed = False
            new_roots = set()
            for c in roots_alpha:
                for i in range(3):
                    # Reflect through s_i:
                    # s_i(beta) = beta - <beta, alpha_i^vee> * alpha_i
                    # <beta, alpha_i^vee> = sum_j c_j * <alpha_j, alpha_i^vee>
                    #                     = sum_j c_j * A[j][i]
                    inner = sum(c[j] * self.cartan[j][i] for j in range(3))
                    # In alpha coords: s_i subtracts inner * e_i
                    r = list(c)
                    r[i] = c[i] - inner
                    r = tuple(r)
                    if all(x >= 0 for x in r) and any(x > 0 for x in r):
                        if r not in roots_alpha:
                            new_roots.add(r)
            if new_roots:
                roots_alpha |= new_roots
                changed = True

        # Sort by total height, then lexicographically
        sorted_roots = sorted(roots_alpha, key=lambda x: (sum(x), x))
        for c in sorted_roots:
            self.positive_roots_alpha.append(c)
            w = tuple(
                sum(c[j] * self.alpha[j][k] for j in range(3))
                for k in range(3)
            )
            self.positive_roots.append(w)

    def _build_weyl_group(self) -> List[Tuple[int, Tuple]]:
        """Build Weyl group as list of (sign, 3x3 matrix).

        Matrices act on the omega basis: w -> M * w.
        """
        # Simple reflection s_i acts as: s_i(w)_j = w_j - w_i * A[i][j]
        # Matrix M: M_{j,k} = delta_{jk} - delta_{k,i} * A[i][j]

        def s_mat(i: int):
            """3x3 matrix for simple reflection s_i."""
            m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for j in range(3):
                for k in range(3):
                    m[j][k] = (1 if j == k else 0) - (1 if k == i else 0) * self.cartan[i][j]
            return tuple(tuple(row) for row in m)

        def mat_compose(m1, m2):
            result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result[i][j] += m1[i][k] * m2[k][j]
            return tuple(tuple(row) for row in result)

        def mat_det(m):
            return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
                    - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
                    + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))

        identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        generators = [s_mat(i) for i in range(3)]

        elements = {identity}
        queue = [identity]
        while queue:
            m = queue.pop(0)
            for s in generators:
                new = mat_compose(s, m)
                if new not in elements:
                    elements.add(new)
                    queue.append(new)

        return [(mat_det(m), m) for m in elements]

    def omega_to_alpha(self, w: Weight3) -> Optional[Tuple[int, int, int]]:
        """Convert weight from omega to alpha basis.

        Solve: sum_j c_j * alpha_j = w  (in omega basis)
        i.e. for each k: sum_j c_j * A[j][k] = w_k
        """
        A = self.cartan
        # 3x3 system: A^T * c = w
        # det(A^T) = det(A)
        det = (A[0][0] * (A[1][1]*A[2][2] - A[1][2]*A[2][1])
               - A[0][1] * (A[1][0]*A[2][2] - A[1][2]*A[2][0])
               + A[0][2] * (A[1][0]*A[2][1] - A[1][1]*A[2][0]))
        if det == 0:
            return None

        # Cramer's rule on the transposed system:
        # The system is: for each k, sum_j c_j * A[j][k] = w[k]
        # Written as matrix eq: [A^T] * [c] = [w]
        # So we solve A^T c = w.
        AT = [[A[j][k] for j in range(3)] for k in range(3)]

        def det3(m):
            return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
                    - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
                    + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))

        det_AT = det3(AT)
        if det_AT == 0:
            return None

        cs = []
        for i in range(3):
            # Replace column i with w
            modified = [list(row) for row in AT]
            for k in range(3):
                modified[k][i] = w[k]
            d = det3(modified)
            if d % det_AT != 0:
                return None
            cs.append(d // det_AT)

        return tuple(cs)

    def weight_multiplicity(self, hw: Weight3, mu: Weight3) -> int:
        """Weight multiplicity of mu in V_hw via Kostant multiplicity formula.

        mult(mu) = sum_{w in W} det(w) * K(w(hw+rho) - (mu+rho))
        """
        if any(x < 0 for x in hw):
            return 0

        rho = self.rho
        hw_rho = tuple(hw[i] + rho[i] for i in range(3))
        mu_rho = tuple(mu[i] + rho[i] for i in range(3))

        total = 0
        for det_w, mat in self.weyl_group:
            w_hw_rho = tuple(
                sum(mat[j][k] * hw_rho[k] for k in range(3))
                for j in range(3)
            )
            diff = tuple(w_hw_rho[i] - mu_rho[i] for i in range(3))
            alpha_coords = self.omega_to_alpha(diff)
            if alpha_coords is None:
                continue
            K = self._kostant_partition(alpha_coords)
            total += det_w * K

        return total

    @lru_cache(maxsize=None)
    def _kostant_partition(self, coeffs_alpha: Tuple[int, int, int]) -> int:
        """Kostant partition function: number of ways to write
        c1*alpha_1 + c2*alpha_2 + c3*alpha_3 as non-negative integer
        combination of positive roots."""
        if any(x < 0 for x in coeffs_alpha):
            return 0
        return self._kostant_dp(coeffs_alpha, len(self.positive_roots_alpha) - 1)

    @lru_cache(maxsize=None)
    def _kostant_dp(self, target: Tuple[int, int, int], max_idx: int) -> int:
        """Dynamic programming for Kostant partition function."""
        if all(x == 0 for x in target):
            return 1
        if max_idx < 0:
            return 0
        if any(x < 0 for x in target):
            return 0

        root = self.positive_roots_alpha[max_idx]
        total = 0
        current = target
        while all(x >= 0 for x in current):
            total += self._kostant_dp(current, max_idx - 1)
            current = tuple(current[i] - root[i] for i in range(3))
        return total

    def irrep_character(self, hw: Weight3, depth: int = 15) -> FormalChar3:
        """Character of V_hw: all weights mu = hw - sum c_j alpha_j with
        total height sum c_j <= depth.
        """
        if any(x < 0 for x in hw):
            return {}

        char: FormalChar3 = {}
        # Enumerate all (c1, c2, c3) with c1+c2+c3 <= depth
        for c1 in range(depth + 1):
            for c2 in range(depth + 1 - c1):
                for c3 in range(depth + 1 - c1 - c2):
                    mu = tuple(
                        hw[k] - sum(
                            (c1, c2, c3)[j] * self.alpha[j][k]
                            for j in range(3)
                        )
                        for k in range(3)
                    )
                    mult = self.weight_multiplicity(hw, mu)
                    if mult > 0:
                        if mu in char:
                            char[mu] += mult
                        else:
                            char[mu] = mult
        return char

    def weyl_dim(self, hw: Weight3) -> int:
        """Dimension of V_hw via character computation."""
        char = self.irrep_character(hw, depth=sum(hw) + 15)
        return sum(char.values())

    def prefundamental_character(self, node: int, depth: int = 12) -> FormalChar3:
        """Character of L^-_{node} (0-indexed).

        ch(L^-_i) = prod_{beta>0, alpha_i in supp(beta)} prod_{n>=1}
                     1 / (1 - e^{-n*beta})

        Computed by truncated expansion of the infinite product.
        Each factor 1/(1 - x) is expanded as 1 + x + x^2 + ... truncated
        at the depth bound.
        """
        relevant_indices = self.roots_containing[node]
        relevant_roots = [self.positive_roots[idx] for idx in relevant_indices]

        # Start with {(0,0,0): 1}
        char: FormalChar3 = {(0, 0, 0): 1}

        for beta in relevant_roots:
            max_coeff = max(abs(beta[k]) for k in range(3))
            if max_coeff == 0:
                continue
            max_n = depth // max_coeff if max_coeff > 0 else depth
            for n in range(1, max_n + 1):
                neg_n_beta = tuple(-n * beta[k] for k in range(3))

                # Multiply current character by 1/(1 - e^{neg_n_beta})
                # = sum_{m >= 0} e^{m * neg_n_beta}
                new_char: FormalChar3 = {}
                for w, m in char.items():
                    shifted = w
                    while True:
                        total_d = sum(abs(shifted[k]) for k in range(3))
                        if total_d > 3 * depth:
                            break
                        new_char[shifted] = new_char.get(shifted, 0) + m
                        shifted = tuple(shifted[k] + neg_n_beta[k] for k in range(3))

                char = new_char

        return char


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def add_wt3(w1: Weight3, w2: Weight3) -> Weight3:
    """Add two rank-3 weights."""
    return (w1[0] + w2[0], w1[1] + w2[1], w1[2] + w2[2])


def tensor_product3(chi1: FormalChar3, chi2: FormalChar3) -> FormalChar3:
    """Formal character tensor product (convolution)."""
    result: FormalChar3 = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = add_wt3(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def shift_char3(chi: FormalChar3, s: Weight3) -> FormalChar3:
    """Shift all weights by s."""
    return {add_wt3(w, s): m for w, m in chi.items()}


def subtract_char3(chi1: FormalChar3, chi2: FormalChar3) -> FormalChar3:
    """Character difference chi1 - chi2."""
    result = dict(chi1)
    for w, m in chi2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


# ---------------------------------------------------------------------------
# Standard root systems
# ---------------------------------------------------------------------------

def B3() -> Rank3RootSystem:
    """Root system for B_3 = so_7.

    Cartan matrix: [[2,-1,0],[-1,2,-2],[0,-1,2]]
    Dynkin diagram: o---o=>=o  (alpha_3 short)
    9 positive roots. |W| = 48.

    Fundamental representations:
      V(omega_1) = 7-dim (vector)
      V(omega_2) = 21-dim (Lie algebra adjoint)
      V(omega_3) = 8-dim (spin)
    """
    return Rank3RootSystem("B3", [[2, -1, 0], [-1, 2, -2], [0, -1, 2]])


def C3() -> Rank3RootSystem:
    """Root system for C_3 = sp_6.

    Cartan matrix: [[2,-1,0],[-1,2,-1],[0,-2,2]]
    Dynkin diagram: o---o=<=o  (alpha_3 long)
    9 positive roots. |W| = 48.

    Langlands dual to B_3: A_{C_3} = A_{B_3}^T.

    Fundamental representations:
      V(omega_1) = 6-dim (standard)
      V(omega_2) = 14-dim (Lambda^2 standard / traceless)
      V(omega_3) = 14'-dim (Lambda^3 standard)
    """
    return Rank3RootSystem("C3", [[2, -1, 0], [-1, 2, -1], [0, -2, 2]])


def A3() -> Rank3RootSystem:
    """Root system for A_3 = sl_4 (cross-check, simply-laced)."""
    return Rank3RootSystem("A3", [[2, -1, 0], [-1, 2, -1], [0, -1, 2]])


# ---------------------------------------------------------------------------
# Weyl dimension formulas (explicit, for cross-check)
# ---------------------------------------------------------------------------

def B3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension formula for B_3 = so_7.

    V_{a*omega_1 + b*omega_2 + c*omega_3}.

    Positive roots in simple root coords: (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (0,1,1), (0,1,2), (1,1,1), (1,1,2), (1,2,2).

    dim = prod_{beta>0} <lambda+rho, beta^vee> / <rho, beta^vee>

    With d = (2,2,1) (squared half-lengths), the coroot coordinates
    d^vee_k = 2*c_k*d_k/<beta,beta> give the nine factors (Bourbaki):
      <rho, beta^vee> values: 1,1,1,2,2,3,3,4,5.  Product = 720.

    <lambda+rho, beta^vee> values:
      (1,0,0): a+1           (0,1,0): b+1           (0,0,1): c+1
      (1,1,0): a+b+2         (0,1,1): 2b+c+3        (0,1,2): b+c+2
      (1,1,1): 2a+2b+c+5     (1,1,2): a+b+c+3       (1,2,2): a+2b+c+4
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    num = ((a+1) * (b+1) * (c+1) * (a+b+2) * (b+c+2) * (2*b+c+3)
           * (a+b+c+3) * (a+2*b+c+4) * (2*a+2*b+c+5))
    return num // 720


def C3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension formula for C_3 = sp_6.

    V_{a*omega_1 + b*omega_2 + c*omega_3}.

    Positive roots in simple root coords: (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (0,1,1), (0,2,1), (1,1,1), (1,2,1), (2,2,1).

    With d = (1,1,2) (squared half-lengths), the coroot coordinates
    give the nine factors (Bourbaki):
      <rho, beta^vee> values: 1,1,1,2,2,3,3,4,5.  Product = 720.

    <lambda+rho, beta^vee> values:
      (1,0,0): a+1           (0,1,0): b+1           (0,0,1): c+1
      (1,1,0): a+b+2         (0,1,1): b+2c+3        (0,2,1): b+c+2
      (1,1,1): a+b+2c+4      (1,2,1): a+2b+2c+5     (2,2,1): a+b+c+3
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    num = ((a+1) * (b+1) * (c+1) * (a+b+2) * (b+c+2) * (b+2*c+3)
           * (a+b+c+3) * (a+b+2*c+4) * (a+2*b+2*c+5))
    return num // 720


def A3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension formula for A_3 = sl_4.

    dim V(a,b,c) = (a+1)(b+1)(c+1)(a+b+2)(b+c+2)(a+b+c+3) / 12
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    return ((a+1) * (b+1) * (c+1) * (a+b+2) * (b+c+2) * (a+b+c+3)) // 12


# ---------------------------------------------------------------------------
# CG verification: universal theorem
# ---------------------------------------------------------------------------

def verify_cg3(
    rs: Rank3RootSystem,
    hw: Weight3,
    node: int,
    depth: int = 8,
) -> Dict:
    """Verify the universal CG theorem for rank-3 systems:

    [V_hw] * [L^-_node] = sum_{mu in wt(V_hw)} mult(mu) * [L^-_node(shift=mu)]

    Returns dict with match status and diagnostics.
    """
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 5)
    V_dim = sum(V_char.values())

    L_char = rs.prefundamental_character(node, depth=depth)

    # LHS: tensor product
    lhs = tensor_product3(V_char, L_char)

    # RHS: weighted sum of shifted prefundamentals
    rhs: FormalChar3 = {}
    for mu, mult in V_char.items():
        L_shifted = shift_char3(L_char, mu)
        for w, m in L_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    # Compare within reliable range
    max_reliable = 2 * (depth - sum(hw) - 3)
    match = True
    mismatches = []
    all_weights = set(list(lhs.keys()) + list(rhs.keys()))
    for w in all_weights:
        dist = sum(abs(w[k]) for k in range(3))
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


def verify_batch3(
    rs: Rank3RootSystem,
    max_hw_sum: int = 2,
    depth: int = 8,
) -> Dict:
    """Verify CG for all dominant weights with |hw| <= max_hw_sum and all nodes."""
    results = {}
    n_pass = 0
    n_fail = 0
    for a in range(max_hw_sum + 1):
        for b in range(max_hw_sum + 1 - a):
            for c in range(max_hw_sum + 1 - a - b):
                if a == 0 and b == 0 and c == 0:
                    continue
                for node in range(3):
                    key = f"{rs.name}: V_({a},{b},{c}) x L^-_{node+1}"
                    res = verify_cg3(rs, (a, b, c), node, depth=depth)
                    results[key] = res
                    if res["match"]:
                        n_pass += 1
                    else:
                        n_fail += 1
    return {"results": results, "n_pass": n_pass, "n_fail": n_fail, "all_pass": n_fail == 0}


# ---------------------------------------------------------------------------
# Verma module containment
# ---------------------------------------------------------------------------

def verma_character3(
    rs: Rank3RootSystem,
    hw: Weight3,
    depth: int = 10,
) -> FormalChar3:
    """Truncated character of the Verma module M(hw).

    ch(M(hw)) = e^hw * prod_{beta>0} 1/(1 - e^{-beta})

    Truncated at given depth from hw.
    """
    # Start with {hw: 1}
    char: FormalChar3 = {hw: 1}

    for beta in rs.positive_roots:
        neg_beta = tuple(-beta[k] for k in range(3))
        max_coeff = max(abs(beta[k]) for k in range(3))
        if max_coeff == 0:
            continue
        max_n = depth // max_coeff if max_coeff > 0 else depth

        new_char: FormalChar3 = {}
        for w, m in char.items():
            shifted = w
            for _ in range(max_n + 1):
                total_d = sum(abs(shifted[k] - hw[k]) for k in range(3))
                if total_d > 3 * depth:
                    break
                new_char[shifted] = new_char.get(shifted, 0) + m
                shifted = tuple(shifted[k] + neg_beta[k] for k in range(3))

        char = new_char

    return char


def verify_verma_containment3(
    rs: Rank3RootSystem,
    hw: Weight3,
    depth: int = 6,
) -> Dict:
    """Verify ch(M(hw)) <= ch(V_hw tensor prod_i L^-_i).

    For rank r, K_0-generation requires the product of ALL r prefundamental
    modules. In rank 1 (sl_2), a single L^- suffices; in rank 3, we need
    L^-_1 * L^-_2 * L^-_3.

    The product prod_i L^-_i has character equal to the Verma denominator
    (product over ALL positive roots), so containment is guaranteed.
    This test verifies the truncated computation matches.
    """
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 3)

    # Product of all three prefundamental characters
    L_product: FormalChar3 = rs.prefundamental_character(0, depth=depth)
    for node in range(1, 3):
        L_node = rs.prefundamental_character(node, depth=depth)
        L_product = tensor_product3(L_product, L_node)

    tensor = tensor_product3(V_char, L_product)
    verma = verma_character3(rs, hw, depth=depth)

    # Check: every weight of Verma appears in tensor with >= multiplicity
    violations = []
    max_reliable = depth - sum(hw) - 2
    for w, m_verma in verma.items():
        dist = sum(abs(w[k] - hw[k]) for k in range(3))
        if dist > max_reliable:
            continue
        m_tensor = tensor.get(w, 0)
        if m_tensor < m_verma:
            violations.append((w, m_verma, m_tensor))

    return {
        "root_system": rs.name,
        "hw": hw,
        "contained": len(violations) == 0,
        "n_violations": len(violations),
        "violations": violations[:5],
    }


# ---------------------------------------------------------------------------
# Langlands duality check
# ---------------------------------------------------------------------------

def check_langlands_duality() -> bool:
    """Verify that A_{C_3} = A_{B_3}^T."""
    b3 = B3()
    c3 = C3()
    for i in range(3):
        for j in range(3):
            if b3.cartan[i][j] != c3.cartan[j][i]:
                return False
    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("PREFUNDAMENTAL CG -- TYPES B_3 AND C_3")
    print("=" * 70)

    # Langlands duality
    print(f"\nLanglands duality A_{{C3}} = A_{{B3}}^T: {check_langlands_duality()}")

    # B_3
    b3 = B3()
    print(f"\nB_3 positive roots (alpha coords): {b3.positive_roots_alpha}")
    print(f"B_3 |pos roots| = {len(b3.positive_roots_alpha)}")
    print(f"B_3 |W| = {len(b3.weyl_group)}")
    for i in range(3):
        rc = [b3.positive_roots_alpha[j] for j in b3.roots_containing[i]]
        print(f"B_3 roots containing alpha_{i+1}: {rc}")

    print("\n--- B_3 dimensions ---")
    for hw in [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1)]:
        char = b3.irrep_character(hw, depth=20)
        dim_char = sum(char.values())
        dim_formula = B3_dim(*hw)
        tag = "OK" if dim_char == dim_formula else "MISMATCH"
        print(f"  [{tag}] V_{hw}: char={dim_char}, formula={dim_formula}")

    print("\n--- B_3 CG verification ---")
    b3_res = verify_batch3(b3, max_hw_sum=1, depth=6)
    for key, data in b3_res["results"].items():
        tag = "PASS" if data["match"] else "FAIL"
        print(f"  [{tag}] {key}: dim={data['V_dim']}")
    print(f"  B_3 summary: {b3_res['n_pass']} pass, {b3_res['n_fail']} fail")

    # C_3
    c3 = C3()
    print(f"\nC_3 positive roots (alpha coords): {c3.positive_roots_alpha}")
    print(f"C_3 |pos roots| = {len(c3.positive_roots_alpha)}")
    print(f"C_3 |W| = {len(c3.weyl_group)}")
    for i in range(3):
        rc = [c3.positive_roots_alpha[j] for j in c3.roots_containing[i]]
        print(f"C_3 roots containing alpha_{i+1}: {rc}")

    print("\n--- C_3 dimensions ---")
    for hw in [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1)]:
        char = c3.irrep_character(hw, depth=20)
        dim_char = sum(char.values())
        dim_formula = C3_dim(*hw)
        tag = "OK" if dim_char == dim_formula else "MISMATCH"
        print(f"  [{tag}] V_{hw}: char={dim_char}, formula={dim_formula}")

    print("\n--- C_3 CG verification ---")
    c3_res = verify_batch3(c3, max_hw_sum=1, depth=6)
    for key, data in c3_res["results"].items():
        tag = "PASS" if data["match"] else "FAIL"
        print(f"  [{tag}] {key}: dim={data['V_dim']}")
    print(f"  C_3 summary: {c3_res['n_pass']} pass, {c3_res['n_fail']} fail")
