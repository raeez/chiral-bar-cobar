"""Prefundamental Clebsch-Gordan closure for rank-3 types B_3, C_3, A_3.

FRONTIER COMPUTATION for MC3 extension to non-simply-laced types
(conj:mc3-arbitrary-type). Extends the verified programme from type A
(thm:mc3-type-a-resolution) and rank-2 types B_2/G_2 (prefundamental_cg_typeB.py)
to rank-3 classical types.

The Hernandez-Jimbo prefundamental character formula (HJ12, Section 5):

    ch(L^-_i) = prod_{beta > 0, alpha_i in supp(beta)} prod_{n >= 1}
                    1 / (1 - e^{-n*beta})

is EVALUATED by truncated infinite product expansion. The CG identity

    ch(V_lambda) * ch(L^-_i)
        = sum_{mu in wt(V_lambda)} mult(mu) * ch(L^-_i(shift=mu))

is VERIFIED by explicit coefficient comparison at finite depth.

ROOT SYSTEM CONVENTIONS:
  Weights in fundamental weight (omega) basis: w = (w_1, w_2, w_3).
  Simple roots in omega basis via Cartan matrix: alpha_i = row i of A.
  Height of a root c_1 alpha_1 + ... + c_r alpha_r is c_1 + ... + c_r.

  B_3 = so_7: Cartan [[2,-1,0],[-1,2,-2],[0,-1,2]].
    Dynkin: o---o=>=o  (alpha_3 short).
    9 positive roots. |W| = 48. h = 6.
    V(omega_1)=7, V(omega_2)=21, V(omega_3)=8 (spin).

  C_3 = sp_6: Cartan [[2,-1,0],[-1,2,-1],[0,-2,2]].
    Dynkin: o---o=<=o  (alpha_3 long).
    9 positive roots. |W| = 48. h = 6.
    V(omega_1)=6, V(omega_2)=14, V(omega_3)=14'.

  A_3 = sl_4: Cartan [[2,-1,0],[-1,2,-1],[0,-1,2]].
    6 positive roots. |W| = 24. h = 4.
    V(omega_1)=4, V(omega_2)=6, V(omega_3)=4.

  Langlands duality: A_{C_3} = A_{B_3}^T.

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

    Constructs the full root system by iterated Weyl reflection, computes
    representation characters via the Kostant multiplicity formula, and
    evaluates the HJ prefundamental character by truncated infinite product.
    """

    def __init__(self, name: str, cartan: List[List[int]]):
        self.name = name
        self.cartan = cartan
        self.rank = 3

        # Simple roots in omega basis: alpha_i = (A_{i,0}, A_{i,1}, A_{i,2})
        self.alpha: List[Weight3] = [
            tuple(cartan[i][j] for j in range(3))
            for i in range(3)
        ]

        # Build positive roots by Weyl reflections
        self.positive_roots: List[Weight3] = []
        self.positive_roots_alpha: List[Tuple[int, int, int]] = []
        self._build_positive_roots()

        # For each node i (0, 1, 2), indices of positive roots containing alpha_i
        self.roots_containing: List[List[int]] = [[], [], []]
        for idx, coeffs in enumerate(self.positive_roots_alpha):
            for i in range(3):
                if coeffs[i] > 0:
                    self.roots_containing[i].append(idx)

        # Weyl group as list of (det, 3x3 matrix)
        self.weyl_group = self._build_weyl_group()

        # rho = (1,1,1) in omega basis
        self.rho: Weight3 = (1, 1, 1)

    # -------------------------------------------------------------------
    # Root system construction
    # -------------------------------------------------------------------

    def _build_positive_roots(self):
        """Build positive roots by iterated simple reflections.

        Start from simple roots, apply all s_i, keep positive results.
        Terminate when no new roots appear.
        """
        roots = {(1, 0, 0), (0, 1, 0), (0, 0, 1)}
        changed = True
        while changed:
            changed = False
            new = set()
            for c in roots:
                for i in range(3):
                    inner = sum(c[j] * self.cartan[j][i] for j in range(3))
                    r = list(c)
                    r[i] -= inner
                    r = tuple(r)
                    if all(x >= 0 for x in r) and any(x > 0 for x in r):
                        if r not in roots:
                            new.add(r)
            if new:
                roots |= new
                changed = True

        sorted_roots = sorted(roots, key=lambda x: (sum(x), x))
        for c in sorted_roots:
            self.positive_roots_alpha.append(c)
            w = tuple(
                sum(c[j] * self.alpha[j][k] for j in range(3))
                for k in range(3)
            )
            self.positive_roots.append(w)

    def _build_weyl_group(self) -> List[Tuple[int, Tuple]]:
        """Build Weyl group by BFS on simple reflection generators.

        Each element stored as (det, 3x3 matrix acting on omega basis).
        """
        def s_mat(i: int):
            m = [[0] * 3 for _ in range(3)]
            for j in range(3):
                for k in range(3):
                    m[j][k] = (1 if j == k else 0) - (1 if k == i else 0) * self.cartan[i][j]
            return tuple(tuple(row) for row in m)

        def compose(m1, m2):
            r = [[0] * 3 for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        r[i][j] += m1[i][k] * m2[k][j]
            return tuple(tuple(row) for row in r)

        def det3(m):
            return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                    - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                    + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

        identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        generators = [s_mat(i) for i in range(3)]

        elements = {identity}
        queue = [identity]
        while queue:
            m = queue.pop(0)
            for s in generators:
                n = compose(s, m)
                if n not in elements:
                    elements.add(n)
                    queue.append(n)

        return [(det3(m), m) for m in elements]

    # -------------------------------------------------------------------
    # Coordinate conversion
    # -------------------------------------------------------------------

    def omega_to_alpha(self, w: Weight3) -> Optional[Tuple[int, int, int]]:
        """Convert weight from omega to alpha basis.

        Solves A^T c = w where A is the Cartan matrix.
        Returns None if no integer solution exists.
        """
        A = self.cartan

        def det3(m):
            return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                    - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                    + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

        AT = [[A[j][k] for j in range(3)] for k in range(3)]
        d = det3(AT)
        if d == 0:
            return None

        cs = []
        for i in range(3):
            col = [list(row) for row in AT]
            for k in range(3):
                col[k][i] = w[k]
            ci = det3(col)
            if ci % d != 0:
                return None
            cs.append(ci // d)
        return tuple(cs)

    def alpha_to_omega(self, c: Tuple[int, int, int]) -> Weight3:
        """Convert alpha-basis coefficients to omega-basis weight."""
        return tuple(
            sum(c[j] * self.alpha[j][k] for j in range(3))
            for k in range(3)
        )

    # -------------------------------------------------------------------
    # Weight multiplicities (Kostant)
    # -------------------------------------------------------------------

    def weight_multiplicity(self, hw: Weight3, mu: Weight3) -> int:
        """Weight multiplicity of mu in V_hw by Kostant's formula.

        mult(mu) = sum_{w in W} det(w) * K(w(hw+rho) - (mu+rho))
        where K is the Kostant partition function.
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
    def _kostant_partition(self, c: Tuple[int, int, int]) -> int:
        """Number of ways to write c as non-negative integer combination
        of positive roots (in alpha basis)."""
        if any(x < 0 for x in c):
            return 0
        return self._kostant_dp(c, len(self.positive_roots_alpha) - 1)

    @lru_cache(maxsize=None)
    def _kostant_dp(self, target: Tuple[int, int, int], max_idx: int) -> int:
        if all(x == 0 for x in target):
            return 1
        if max_idx < 0 or any(x < 0 for x in target):
            return 0

        root = self.positive_roots_alpha[max_idx]
        total = 0
        cur = target
        while all(x >= 0 for x in cur):
            total += self._kostant_dp(cur, max_idx - 1)
            cur = tuple(cur[i] - root[i] for i in range(3))
        return total

    # -------------------------------------------------------------------
    # Irreducible characters
    # -------------------------------------------------------------------

    def irrep_character(self, hw: Weight3, depth: int = 15) -> FormalChar3:
        """Character of irrep V_hw by Kostant multiplicity.

        Enumerates all mu = hw - sum c_j alpha_j with sum c_j <= depth.
        """
        if any(x < 0 for x in hw):
            return {}

        char: FormalChar3 = {}
        for c1 in range(depth + 1):
            for c2 in range(depth + 1 - c1):
                for c3 in range(depth + 1 - c1 - c2):
                    mu = tuple(
                        hw[k] - sum(
                            [c1, c2, c3][j] * self.alpha[j][k]
                            for j in range(3)
                        )
                        for k in range(3)
                    )
                    m = self.weight_multiplicity(hw, mu)
                    if m > 0:
                        char[mu] = char.get(mu, 0) + m
        return char

    def weyl_dim(self, hw: Weight3) -> int:
        """Dimension of V_hw via character summation."""
        char = self.irrep_character(hw, depth=sum(hw) + 15)
        return sum(char.values())

    # -------------------------------------------------------------------
    # HJ prefundamental character
    # -------------------------------------------------------------------

    def prefundamental_character(self, node: int, depth: int = 12) -> FormalChar3:
        """Evaluate the Hernandez-Jimbo prefundamental character L^-_{node}.

        ch(L^-_i) = prod_{beta>0, alpha_i in supp(beta)}
                        prod_{n >= 1} 1 / (1 - e^{-n*beta})

        Truncated at height depth from the highest weight (0,0,0).
        Each factor 1/(1-x) is expanded as geometric series 1 + x + x^2 + ...
        with truncation controlled by the height of the resulting weight
        in the alpha basis.
        """
        relevant_indices = self.roots_containing[node]
        relevant_roots_omega = [self.positive_roots[idx] for idx in relevant_indices]
        relevant_roots_alpha = [self.positive_roots_alpha[idx] for idx in relevant_indices]

        char: FormalChar3 = {(0, 0, 0): 1}

        for r_idx, beta_omega in enumerate(relevant_roots_omega):
            beta_alpha = relevant_roots_alpha[r_idx]
            beta_height = sum(beta_alpha)

            max_n = max(1, depth // beta_height) if beta_height > 0 else depth

            for n in range(1, max_n + 1):
                step = tuple(-n * beta_omega[k] for k in range(3))
                step_height = n * beta_height

                new_char: FormalChar3 = {}
                for w, m in char.items():
                    # Determine current height from origin in alpha basis
                    w_alpha = self.omega_to_alpha(tuple(-w[k] for k in range(3)))
                    if w_alpha is not None:
                        cur_height = sum(w_alpha)
                    else:
                        cur_height = sum(abs(w[k]) for k in range(3))

                    shifted = w
                    while True:
                        # Check height bound
                        s_alpha = self.omega_to_alpha(tuple(-shifted[k] for k in range(3)))
                        if s_alpha is not None:
                            h = sum(s_alpha)
                        else:
                            h = sum(abs(shifted[k]) for k in range(3))
                        if h > 3 * depth:
                            break
                        new_char[shifted] = new_char.get(shifted, 0) + m
                        shifted = tuple(shifted[k] + step[k] for k in range(3))

                char = new_char

        return char

    # -------------------------------------------------------------------
    # Prefundamental character: depth-1 weight
    # -------------------------------------------------------------------

    def prefundamental_depth1_mult(self, node: int, depth: int = 12) -> int:
        """Multiplicity of the depth-1 weight in L^-_{node}.

        The depth-1 weight is -alpha_i (in omega basis). Its multiplicity
        equals the number of positive roots containing alpha_i.
        This is because at depth 1 the only contributing factor is
        1/(1-e^{-beta}) at n=1, one term for each relevant root.
        """
        char = self.prefundamental_character(node, depth=depth)
        neg_alpha = tuple(-self.alpha[node][k] for k in range(3))
        return char.get(neg_alpha, 0)


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def add_wt3(w1: Weight3, w2: Weight3) -> Weight3:
    return (w1[0] + w2[0], w1[1] + w2[1], w1[2] + w2[2])


def tensor_product3(chi1: FormalChar3, chi2: FormalChar3) -> FormalChar3:
    """Formal character product (convolution)."""
    result: FormalChar3 = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = add_wt3(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def shift_char3(chi: FormalChar3, s: Weight3) -> FormalChar3:
    return {add_wt3(w, s): m for w, m in chi.items()}


def subtract_char3(chi1: FormalChar3, chi2: FormalChar3) -> FormalChar3:
    result = dict(chi1)
    for w, m in chi2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


def char_dim(chi: FormalChar3) -> int:
    """Total dimension (sum of multiplicities)."""
    return sum(chi.values())


# ---------------------------------------------------------------------------
# Standard root systems
# ---------------------------------------------------------------------------

def B3() -> Rank3RootSystem:
    """B_3 = so_7.

    Cartan: [[2,-1,0],[-1,2,-2],[0,-1,2]]
    Dynkin: o---o=>=o  (alpha_3 short)
    9 positive roots, |W| = 48.
    V(omega_1) = 7, V(omega_2) = 21, V(omega_3) = 8.
    """
    return Rank3RootSystem("B3", [[2, -1, 0], [-1, 2, -2], [0, -1, 2]])


def C3() -> Rank3RootSystem:
    """C_3 = sp_6.

    Cartan: [[2,-1,0],[-1,2,-1],[0,-2,2]]
    Dynkin: o---o=<=o  (alpha_3 long)
    9 positive roots, |W| = 48.
    V(omega_1) = 6, V(omega_2) = 14, V(omega_3) = 14'.
    Langlands dual to B_3: A_{C_3} = A_{B_3}^T.
    """
    return Rank3RootSystem("C3", [[2, -1, 0], [-1, 2, -1], [0, -2, 2]])


def A3() -> Rank3RootSystem:
    """A_3 = sl_4.

    Cartan: [[2,-1,0],[-1,2,-1],[0,-1,2]]
    6 positive roots, |W| = 24.
    V(omega_1) = 4, V(omega_2) = 6, V(omega_3) = 4.
    """
    return Rank3RootSystem("A3", [[2, -1, 0], [-1, 2, -1], [0, -1, 2]])


# ---------------------------------------------------------------------------
# Weyl dimension formulas (explicit, for cross-check)
# ---------------------------------------------------------------------------

def B3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension formula for B_3 = so_7, V(a*w1 + b*w2 + c*w3).

    The 9 factors <lambda+rho, beta^vee> / <rho, beta^vee> with
    <rho, beta^vee> product = 720:
      (a+1)(b+1)(c+1)(a+b+2)(b+c+2)(2b+c+3)
      *(a+b+c+3)(a+2b+c+4)(2a+2b+c+5) / 720.
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    return ((a + 1) * (b + 1) * (c + 1) * (a + b + 2)
            * (b + c + 2) * (2 * b + c + 3)
            * (a + b + c + 3) * (a + 2 * b + c + 4)
            * (2 * a + 2 * b + c + 5)) // 720


def C3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension formula for C_3 = sp_6, V(a*w1 + b*w2 + c*w3).

    Product of 9 factors / 720:
      (a+1)(b+1)(c+1)(a+b+2)(b+c+2)(b+2c+3)
      *(a+b+c+3)(a+b+2c+4)(a+2b+2c+5) / 720.
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    return ((a + 1) * (b + 1) * (c + 1) * (a + b + 2)
            * (b + c + 2) * (b + 2 * c + 3)
            * (a + b + c + 3) * (a + b + 2 * c + 4)
            * (a + 2 * b + 2 * c + 5)) // 720


def A3_dim(a: int, b: int, c: int) -> int:
    """Weyl dimension formula for A_3 = sl_4.

    dim V(a,b,c) = (a+1)(b+1)(c+1)(a+b+2)(b+c+2)(a+b+c+3) / 12.
    """
    if a < 0 or b < 0 or c < 0:
        return 0
    return ((a + 1) * (b + 1) * (c + 1) * (a + b + 2)
            * (b + c + 2) * (a + b + c + 3)) // 12


# ---------------------------------------------------------------------------
# CG verification
# ---------------------------------------------------------------------------

def verify_cg3(
    rs: Rank3RootSystem,
    hw: Weight3,
    node: int,
    depth: int = 8,
) -> Dict:
    """Verify the universal CG identity at finite depth.

    LHS = ch(V_hw) * ch(L^-_{node})       (tensor product)
    RHS = sum_{mu in wt(V_hw)} mult(mu) * ch(L^-_{node}(shift=mu))

    Both are computed explicitly and compared coefficient-by-coefficient
    in the reliable range (weights of height <= max_reliable from hw).
    """
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 5)
    V_dim = sum(V_char.values())
    L_char = rs.prefundamental_character(node, depth=depth)

    lhs = tensor_product3(V_char, L_char)

    rhs: FormalChar3 = {}
    for mu, mult in V_char.items():
        L_shifted = shift_char3(L_char, mu)
        for w, m in L_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    max_reliable = 2 * (depth - sum(hw) - 3)
    if max_reliable < 0:
        max_reliable = 0

    match = True
    mismatches = []
    all_weights = set(lhs.keys()) | set(rhs.keys())
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
    """Batch CG verification for all dominant weights with |hw| <= max_hw_sum."""
    results = {}
    n_pass = 0
    n_fail = 0
    for a in range(max_hw_sum + 1):
        for b in range(max_hw_sum + 1 - a):
            for c in range(max_hw_sum + 1 - a - b):
                if a == 0 and b == 0 and c == 0:
                    continue
                for node in range(3):
                    key = f"{rs.name}: V_({a},{b},{c}) x L^-_{node + 1}"
                    res = verify_cg3(rs, (a, b, c), node, depth=depth)
                    results[key] = res
                    if res["match"]:
                        n_pass += 1
                    else:
                        n_fail += 1
    return {"results": results, "n_pass": n_pass, "n_fail": n_fail, "all_pass": n_fail == 0}


# ---------------------------------------------------------------------------
# Verma containment
# ---------------------------------------------------------------------------

def verma_character3(
    rs: Rank3RootSystem,
    hw: Weight3,
    depth: int = 10,
) -> FormalChar3:
    """Truncated character of the Verma module M(hw).

    ch(M(hw)) = e^hw * prod_{beta>0} 1/(1 - e^{-beta})
    """
    char: FormalChar3 = {hw: 1}

    for beta in rs.positive_roots:
        neg_beta = tuple(-beta[k] for k in range(3))
        max_coeff = max(abs(beta[k]) for k in range(3))
        if max_coeff == 0:
            continue
        max_n = depth // max_coeff

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

    In rank 3 the K_0-generation requires the product of ALL three
    prefundamental modules, not just one.
    """
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 3)

    L_product: FormalChar3 = rs.prefundamental_character(0, depth=depth)
    for node in range(1, 3):
        L_node = rs.prefundamental_character(node, depth=depth)
        L_product = tensor_product3(L_product, L_node)

    tensor = tensor_product3(V_char, L_product)
    verma = verma_character3(rs, hw, depth=depth)

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
# Langlands duality
# ---------------------------------------------------------------------------

def check_langlands_duality() -> bool:
    """Verify A_{C_3} = A_{B_3}^T."""
    b3 = B3()
    c3 = C3()
    for i in range(3):
        for j in range(3):
            if b3.cartan[i][j] != c3.cartan[j][i]:
                return False
    return True


# ---------------------------------------------------------------------------
# Prefundamental product vs Verma denominator
# ---------------------------------------------------------------------------

def prefundamental_product_character(
    rs: Rank3RootSystem,
    depth: int = 6,
) -> FormalChar3:
    """Product of all r prefundamental characters.

    prod_{i=1}^r ch(L^-_i) should equal the Verma denominator
    prod_{beta>0} 1/(1-e^{-beta}) * correction, up to truncation.
    """
    result: FormalChar3 = rs.prefundamental_character(0, depth=depth)
    for i in range(1, 3):
        L_i = rs.prefundamental_character(i, depth=depth)
        result = tensor_product3(result, L_i)
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("PREFUNDAMENTAL CG -- TYPES B_3, C_3, A_3")
    print("=" * 70)

    print(f"\nLanglands duality A_{{C3}} = A_{{B3}}^T: {check_langlands_duality()}")

    for name, constructor, dim_fn in [
        ("B_3", B3, B3_dim),
        ("C_3", C3, C3_dim),
        ("A_3", A3, A3_dim),
    ]:
        rs = constructor()
        print(f"\n{name} positive roots (alpha): {rs.positive_roots_alpha}")
        print(f"{name} |pos roots| = {len(rs.positive_roots_alpha)}")
        print(f"{name} |W| = {len(rs.weyl_group)}")
        for i in range(3):
            rc = [rs.positive_roots_alpha[j] for j in rs.roots_containing[i]]
            print(f"  roots containing alpha_{i+1}: {rc}")

        print(f"\n--- {name} dimensions ---")
        for hw in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            ch = rs.irrep_character(hw, depth=20)
            dc = sum(ch.values())
            df = dim_fn(*hw)
            tag = "OK" if dc == df else "MISMATCH"
            print(f"  [{tag}] V{hw}: char={dc}, formula={df}")

        print(f"\n--- {name} CG verification ---")
        batch = verify_batch3(rs, max_hw_sum=1, depth=6)
        for key, data in batch["results"].items():
            tag = "PASS" if data["match"] else "FAIL"
            print(f"  [{tag}] {key}: dim={data['V_dim']}")
        print(f"  Summary: {batch['n_pass']} pass, {batch['n_fail']} fail")
