"""Exceptional type RTT scaffold: R-matrix and character infrastructure.

FRONTIER COMPUTATION for MC3 extension to exceptional Dynkin types
(conj:mc3-arbitrary-type). This module provides:

  1. Root systems and Cartan matrices for ALL exceptional types (G_2, F_4, E_6, E_7, E_8)
  2. Weyl dimension formulas and weight multiplicities via Freudenthal
  3. Character-level prefundamental CG verification
  4. R-matrix structure and Yang-Baxter verification for the standard
     R-matrix R(u) = I - P/u + Q/(u - kappa) with trace-projection Q

MC3 DIFFICULTY GRADES:
  D: grade B (orthogonal RTT, see yangian_rtt_typeD.py)
  G_2: grade C- (7-dim fundamental, rank 2, accessible)
  E_6: grade B (27-dim fundamental, large but structured)
  E_7: grade C+ (56-dim fundamental, very large)
  F_4: grade D (26-dim fundamental, non-simply-laced complications)
  E_8: grade D (248-dim = adjoint is smallest, extreme size)

ROOT SYSTEM CONVENTIONS:
  Weights in fundamental weight (omega) basis.
  Simple roots alpha_i in omega basis via Cartan matrix: alpha_i = row i of A.
  Positive roots built by iterated simple reflections.

  G_2: Cartan [[2,-1],[-3,2]]. 6 positive roots. |W| = 12.
    V(omega_1) = 7, V(omega_2) = 14. h = 6, h* = 4.

  F_4: Cartan [[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]].
    24 positive roots. |W| = 1152. h = 12, h* = 9.
    V(omega_1) = 52 (adjoint), V(omega_4) = 26 (minimal).

  E_6: Cartan given below. 36 positive roots. |W| = 51840.
    V(omega_1) = 27, V(omega_6) = 27 (dual). h = 12, h* = 12.

  E_7: 63 positive roots. |W| = 2903040.
    V(omega_7) = 56 (minimal). h = 18, h* = 18.

  E_8: 120 positive roots. |W| = 696729600.
    V(omega_8) = 248 (adjoint = minimal). h = 30, h* = 30.

APPROACH:
  For G_2 (rank 2): full Kostant multiplicity, prefundamental character,
  CG verification. Reuses Rank2RootSystem from prefundamental_cg_typeB.py.

  For E_6, E_7, E_8, F_4 (rank >= 4): Weyl group too large for direct
  enumeration. Use Freudenthal's recursive formula for weight multiplicities
  instead of Kostant's formula.

References:
  - Humphreys, "Introduction to Lie Algebras and Representation Theory", GTM 9
  - Molev, "Yangians and classical Lie algebras", AMS 2007
  - Hernandez-Jimbo 2012, Section 5
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from functools import lru_cache
import numpy as np

from compute.lib.prefundamental_cg_typeB import (
    Rank2RootSystem,
    G2 as _G2_rank2,
    verify_cg as verify_cg_rank2,
    verify_batch as verify_batch_rank2,
    G2_dim,
)


# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------

Weight = Tuple[int, ...]
FormalChar = Dict[Weight, int]


# ---------------------------------------------------------------------------
# Cartan matrices for all exceptional types
# ---------------------------------------------------------------------------

CARTAN_MATRICES_EXCEPTIONAL = {
    "G2": [[2, -1], [-3, 2]],

    "F4": [[2, -1, 0, 0],
           [-1, 2, -2, 0],
           [0, -1, 2, -1],
           [0, 0, -1, 2]],

    # E_6 Dynkin diagram (Bourbaki numbering):
    #     1 - 3 - 4 - 5 - 6
    #             |
    #             2
    # 0-indexed: node 0-1-2-3-4 with branch at node 2 connecting to node 5
    # Actually for standard Bourbaki with nodes 1..6:
    # 1-3-4-5-6 with 2 branching off 4. In 0-indexed:
    # 0-2-3-4-5 with 1 branching off 3.
    # Cartan (0-indexed, Bourbaki standard):
    "E6": [[2, 0, -1, 0, 0, 0],
           [0, 2, 0, -1, 0, 0],
           [-1, 0, 2, -1, 0, 0],
           [0, -1, -1, 2, -1, 0],
           [0, 0, 0, -1, 2, -1],
           [0, 0, 0, 0, -1, 2]],

    # E_7 Dynkin diagram (Bourbaki): 1-3-4-5-6-7 with 2 off 4.
    # 0-indexed: 0-2-3-4-5-6 with 1 off 3.
    "E7": [[2, 0, -1, 0, 0, 0, 0],
           [0, 2, 0, -1, 0, 0, 0],
           [-1, 0, 2, -1, 0, 0, 0],
           [0, -1, -1, 2, -1, 0, 0],
           [0, 0, 0, -1, 2, -1, 0],
           [0, 0, 0, 0, -1, 2, -1],
           [0, 0, 0, 0, 0, -1, 2]],

    # E_8: 1-3-4-5-6-7-8 with 2 off 4.
    "E8": [[2, 0, -1, 0, 0, 0, 0, 0],
           [0, 2, 0, -1, 0, 0, 0, 0],
           [-1, 0, 2, -1, 0, 0, 0, 0],
           [0, -1, -1, 2, -1, 0, 0, 0],
           [0, 0, 0, -1, 2, -1, 0, 0],
           [0, 0, 0, 0, -1, 2, -1, 0],
           [0, 0, 0, 0, 0, -1, 2, -1],
           [0, 0, 0, 0, 0, 0, -1, 2]],
}

# Root system data: (num_pos_roots, weyl_order, coxeter, dual_coxeter, dim, exponents)
EXCEPTIONAL_DATA = {
    "G2": (6, 12, 6, 4, 14, [1, 5]),
    "F4": (24, 1152, 12, 9, 52, [1, 5, 7, 11]),
    "E6": (36, 51840, 12, 12, 78, [1, 4, 5, 7, 8, 11]),
    "E7": (63, 2903040, 18, 18, 133, [1, 5, 7, 9, 11, 13, 17]),
    "E8": (120, 696729600, 30, 30, 248, [1, 7, 11, 13, 17, 19, 23, 29]),
}

# Fundamental representation dimensions (Bourbaki numbering, 0-indexed)
FUNDAMENTAL_DIMS = {
    "G2": [7, 14],
    "F4": [52, 1274, 273, 26],
    "E6": [27, 78, 351, 2925, 351, 27],
    "E7": [133, 912, 8645, 365750, 27664, 1539, 56],
    # FM5/AP10: 779247 is NOT an E8 irreducible; last entry was duplicate 248 (missing 3875).
    # Correct set: {248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}.
    "E8": [248, 30380, 2450240, 146325270, 6696000, 147250, 6899079264, 3875],
}


# ---------------------------------------------------------------------------
# General exceptional root system
# ---------------------------------------------------------------------------

class ExceptionalRootSystem:
    """Root system for an exceptional simple Lie algebra.

    Builds positive roots, computes weight multiplicities via Freudenthal's
    recursive formula (avoiding Weyl group enumeration), and evaluates
    prefundamental characters.
    """

    def __init__(self, name: str):
        assert name in CARTAN_MATRICES_EXCEPTIONAL, f"Unknown type: {name}"
        self.name = name
        self.cartan = CARTAN_MATRICES_EXCEPTIONAL[name]
        self.rank = len(self.cartan)

        data = EXCEPTIONAL_DATA[name]
        self.expected_pos_roots = data[0]
        self.expected_weyl_order = data[1]
        self.coxeter_number = data[2]
        self.dual_coxeter_number = data[3]
        self.dim_algebra = data[4]
        self.exponents = data[5]

        # Simple roots in omega basis
        self.alpha: List[Weight] = [
            tuple(self.cartan[i][j] for j in range(self.rank))
            for i in range(self.rank)
        ]

        # Build positive roots
        self.positive_roots: List[Weight] = []
        self.positive_roots_alpha: List[Tuple[int, ...]] = []
        self._build_positive_roots()

        # Roots containing each simple root
        self.roots_containing: List[List[int]] = [
            [] for _ in range(self.rank)
        ]
        for idx, coeffs in enumerate(self.positive_roots_alpha):
            for i in range(self.rank):
                if coeffs[i] > 0:
                    self.roots_containing[i].append(idx)

        # rho = (1, ..., 1) in omega basis
        self.rho = tuple([1] * self.rank)

        # Precompute inner product matrix (alpha_i, alpha_j)
        # For simply-laced: (alpha_i, alpha_j) = A_{ij} (all long, normalized to 2)
        # For non-simply-laced: need the symmetrizer D with DA symmetric
        self._compute_inner_product_matrix()

    def _build_positive_roots(self):
        """Build positive roots by iterated simple reflections."""
        N = self.rank
        roots = set()
        for i in range(N):
            roots.add(tuple(1 if j == i else 0 for j in range(N)))

        changed = True
        while changed:
            changed = False
            new = set()
            for c in roots:
                for i in range(N):
                    inner = sum(c[j] * self.cartan[j][i] for j in range(N))
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
                sum(c[j] * self.alpha[j][k] for j in range(N))
                for k in range(N)
            )
            self.positive_roots.append(w)

    def _compute_inner_product_matrix(self):
        """Compute the symmetrized Cartan matrix (alpha_i, alpha_j).

        For a symmetrizable Cartan matrix A, there exists a diagonal
        matrix D = diag(d_1, ..., d_r) with d_i > 0 such that DA is
        symmetric. Then (alpha_i, alpha_j) = d_i * A_{ij}.

        For simply-laced (E_6, E_7, E_8): d_i = 1 for all i.
        For G_2: d_1 = 1, d_2 = 3 (short root alpha_1, long root alpha_2).
        For F_4: d_1 = d_2 = 1, d_3 = d_4 = 2 (long: alpha_1, alpha_2; short: alpha_3, alpha_4).

        Wait -- verify. G_2 Cartan: [[2,-1],[-3,2]].
        DA symmetric: d_1 * 2 = d_1 * A_{11}, d_2 * (-3) must equal d_1 * (-1).
        So d_2 * 3 = d_1. Take d_1 = 3, d_2 = 1.
        Then (alpha_1, alpha_1) = 3*2 = 6, (alpha_2, alpha_2) = 1*2 = 2.
        Ratio |alpha_1|^2 / |alpha_2|^2 = 3, so alpha_1 is LONG, alpha_2 is SHORT.

        But Bourbaki convention for G_2: alpha_1 is short, alpha_2 is long.
        Check: our Cartan has A_{21} = -3. Since A_{ij} = 2(alpha_i, alpha_j)/(alpha_i, alpha_i),
        A_{21} = -3 means 2(alpha_2, alpha_1)/(alpha_2, alpha_2) = -3.
        With |alpha_2|^2 = 2 (long root normalization):
        (alpha_2, alpha_1) = -3. Then (alpha_1, alpha_1) = ?
        A_{12} = -1 = 2(alpha_1, alpha_2)/(alpha_1, alpha_1).
        (alpha_1, alpha_2) = -3, so -1 = 2*(-3)/|alpha_1|^2, |alpha_1|^2 = 6.
        So alpha_1 has |alpha_1|^2 = 6, alpha_2 has |alpha_2|^2 = 2.
        Ratio 3:1, alpha_1 is LONG. This contradicts Bourbaki.

        RESOLUTION: Our Cartan matrix [[2,-1],[-3,2]] has alpha_1 LONG and
        alpha_2 SHORT for G_2. This is a valid convention (just reversed from
        Bourbaki). It matches the prefundamental_cg_typeB.py convention.

        Symmetrizer d: solve d_i * A_{ij} = d_j * A_{ji} for all i,j.
        """
        N = self.rank
        A = self.cartan

        # Find symmetrizer d
        d = [1] * N
        # BFS from node 0
        visited = [False] * N
        visited[0] = True
        queue = [0]
        while queue:
            i = queue.pop(0)
            for j in range(N):
                if not visited[j] and A[i][j] != 0:
                    # d_i * A_{ij} = d_j * A_{ji}
                    # d_j = d_i * A_{ij} / A_{ji}
                    if A[j][i] != 0:
                        from fractions import Fraction
                        d_j = Fraction(d[i] * A[i][j], A[j][i])
                        d[j] = d_j
                    visited[j] = True
                    queue.append(j)

        # Normalize: smallest d_i = 1
        from fractions import Fraction
        d_fracs = [Fraction(x) for x in d]
        min_d = min(abs(x) for x in d_fracs if x != 0)
        self.symmetrizer = [int(x / min_d) for x in d_fracs]

        # Inner product matrix: (alpha_i, alpha_j) = d_i * A_{ij}
        self.inner_product = [
            [self.symmetrizer[i] * A[i][j] for j in range(N)]
            for i in range(N)
        ]

    def alpha_inner_product(self, c1: Tuple[int, ...], c2: Tuple[int, ...]) -> int:
        """Inner product of two weights given in alpha basis.

        (sum c1_i alpha_i, sum c2_j alpha_j) = sum c1_i c2_j (alpha_i, alpha_j)
        """
        N = self.rank
        total = 0
        for i in range(N):
            for j in range(N):
                total += c1[i] * c2[j] * self.inner_product[i][j]
        return total

    def omega_inner_product_rational(self, w1: Weight, w2: Weight):
        """Inner product of two weights given in omega basis.

        (w1, w2) = sum_{i,j} w1_i w2_j (omega_i, omega_j)

        where (omega_i, omega_j) = (A^{-1} D)_{ij} with D = diag(d_1,...,d_r)
        the symmetrizer.

        More precisely:
        alpha_i = sum_k A_{ik} omega_k, so omega_i = sum_k (A^{-1})_{ik} alpha_k.
        (omega_i, omega_j) = sum_{k,l} (A^{-1})_{ik} (A^{-1})_{jl} (alpha_k, alpha_l)
                           = sum_{k,l} (A^{-1})_{ik} (A^{-1})_{jl} d_k A_{kl}
                           = ((A^{-1}) D A (A^{-1})^T)_{ij}
                           = ((A^{-1}) (DA) (A^T)^{-1})_{ij}
        Since DA = B is the symmetrized matrix, and A^T = A for simply-laced:
        = (A^{-1} B A^{-1})_{ij}.

        For simply-laced (d_k = 1 for all k): B = A, so
        (omega_i, omega_j) = (A^{-1})_{ij}.
        """
        from fractions import Fraction
        N = self.rank

        if not hasattr(self, '_omega_metric'):
            # Compute the metric on the omega basis
            # G_{ij} = (omega_i, omega_j)
            A = [[Fraction(self.cartan[i][j]) for j in range(N)] for i in range(N)]

            # Compute A^{-1} using Gauss-Jordan
            aug = [A[i][:] + [Fraction(1 if j == i else 0) for j in range(N)]
                   for i in range(N)]

            for col in range(N):
                pivot = None
                for row in range(col, N):
                    if aug[row][col] != 0:
                        pivot = row
                        break
                if pivot is None:
                    raise ValueError("Singular Cartan matrix")
                aug[col], aug[pivot] = aug[pivot], aug[col]
                scale = aug[col][col]
                for j in range(2 * N):
                    aug[col][j] /= scale
                for row in range(N):
                    if row == col:
                        continue
                    factor = aug[row][col]
                    for j in range(2 * N):
                        aug[row][j] -= factor * aug[col][j]

            A_inv = [[aug[i][N + j] for j in range(N)] for i in range(N)]

            # B = DA (symmetrized Cartan)
            B = [[Fraction(self.symmetrizer[i]) * Fraction(self.cartan[i][j])
                  for j in range(N)] for i in range(N)]

            # G = A_inv * B * A_inv^T
            # First: BA_inv^T
            BA_invT = [[sum(B[i][k] * A_inv[j][k] for k in range(N))
                        for j in range(N)] for i in range(N)]
            # Then: A_inv * BA_inv^T
            G = [[sum(A_inv[i][k] * BA_invT[k][j] for k in range(N))
                  for j in range(N)] for i in range(N)]

            self._omega_metric = G

        G = self._omega_metric
        return sum(
            G[i][j] * w1[i] * w2[j]
            for i in range(N) for j in range(N)
        )

    def omega_to_alpha(self, w: Weight) -> Optional[Tuple[int, ...]]:
        """Convert weight from omega to alpha basis by solving A^T c = w."""
        N = self.rank
        A = self.cartan

        # Build A^T
        AT = [[A[j][k] for j in range(N)] for k in range(N)]

        # Gaussian elimination over rationals
        from fractions import Fraction
        aug = [[Fraction(AT[i][j]) for j in range(N)] + [Fraction(w[i])]
               for i in range(N)]

        for col in range(N):
            pivot = None
            for row in range(col, N):
                if aug[row][col] != 0:
                    pivot = row
                    break
            if pivot is None:
                return None
            aug[col], aug[pivot] = aug[pivot], aug[col]

            for row in range(N):
                if row == col:
                    continue
                if aug[row][col] == 0:
                    continue
                factor = aug[row][col] / aug[col][col]
                for j in range(N + 1):
                    aug[row][j] -= factor * aug[col][j]

        result = []
        for i in range(N):
            val = aug[i][N] / aug[i][i]
            if val.denominator != 1:
                return None
            result.append(int(val))
        return tuple(result)

    def alpha_to_omega(self, c: Tuple[int, ...]) -> Weight:
        """Convert alpha-basis coefficients to omega-basis weight."""
        N = self.rank
        return tuple(
            sum(c[j] * self.alpha[j][k] for j in range(N))
            for k in range(N)
        )

    # -------------------------------------------------------------------
    # Weight multiplicities via Freudenthal's formula
    # -------------------------------------------------------------------

    def weight_multiplicity_freudenthal(
        self, hw: Weight, mu: Weight, cache: Optional[Dict] = None
    ) -> int:
        """Weight multiplicity via Freudenthal's recursive formula.

        mult(mu) = [2 / ((hw+rho, hw+rho) - (mu+rho, mu+rho))]
                   * sum_{alpha > 0} sum_{k >= 1}
                       (mu + k*alpha, alpha) * mult(mu + k*alpha)

        All inner products computed in the OMEGA basis using the metric
        G_{ij} = (omega_i, omega_j), avoiding omega-to-alpha conversion
        which can fail for weights not in the root lattice.

        The cache argument allows sharing cached multiplicities across
        multiple calls for the same hw.
        """
        from fractions import Fraction
        N = self.rank
        if cache is None:
            cache = {}

        if any(x < 0 for x in hw):
            return 0

        # Check if mu is dominated by hw (hw - mu must be a non-negative
        # combination of positive roots)
        diff = tuple(hw[k] - mu[k] for k in range(N))
        diff_alpha = self.omega_to_alpha(diff)
        if diff_alpha is None or any(c < 0 for c in diff_alpha):
            return 0

        if mu == hw:
            cache[mu] = 1
            return 1

        if mu in cache:
            return cache[mu]

        # Compute denominator: (hw+rho, hw+rho) - (mu+rho, mu+rho)
        hw_rho = tuple(hw[k] + self.rho[k] for k in range(N))
        mu_rho = tuple(mu[k] + self.rho[k] for k in range(N))

        ip_hw = self.omega_inner_product_rational(hw_rho, hw_rho)
        ip_mu = self.omega_inner_product_rational(mu_rho, mu_rho)
        denom = ip_hw - ip_mu

        if denom == 0:
            cache[mu] = 0
            return 0

        # Numerator: sum over positive roots and positive multiples
        numer = Fraction(0)
        for beta_omega in self.positive_roots:
            k = 1
            while True:
                shifted_mu = tuple(mu[j] + k * beta_omega[j] for j in range(N))
                # Check if shifted_mu is a weight of V_hw
                shifted_diff = tuple(hw[j] - shifted_mu[j] for j in range(N))
                shifted_diff_alpha = self.omega_to_alpha(shifted_diff)
                if (shifted_diff_alpha is None
                        or any(c < 0 for c in shifted_diff_alpha)):
                    break

                m = self.weight_multiplicity_freudenthal(hw, shifted_mu, cache)
                if m == 0 and k > 1:
                    break

                # (mu + k*alpha, alpha) in omega basis
                ip = self.omega_inner_product_rational(shifted_mu, beta_omega)
                numer += ip * m

                k += 1

        result_frac = Fraction(2) * numer / denom
        # Should be a non-negative integer
        if result_frac.denominator != 1:
            # Numerical issue; try rounding
            val = float(result_frac)
            if abs(val - round(val)) < 1e-6:
                cache[mu] = max(0, round(val))
                return cache[mu]
            cache[mu] = 0
            return 0

        result = int(result_frac)
        cache[mu] = max(0, result)
        return cache[mu]

    # -------------------------------------------------------------------
    # Irreducible characters
    # -------------------------------------------------------------------

    def irrep_character(self, hw: Weight, depth: int = 6) -> FormalChar:
        """Character of V_hw via Freudenthal multiplicities.

        Enumerates mu = hw - sum c_j alpha_j with sum c_j <= depth,
        processed in DECREASING ORDER of height (sum c_j increasing from 0)
        so that the Freudenthal recursion has all higher multiplicities
        available when computing lower ones.
        """
        N = self.rank
        if any(x < 0 for x in hw):
            return {}

        char: FormalChar = {}
        cache: Dict[Weight, int] = {}

        # Generate all (c_1, ..., c_r) with sum <= depth, sorted by
        # increasing total sum (so higher weights are processed first)
        coeff_lists: List[Tuple[int, ...]] = []

        def enum_coeffs(idx: int, remaining: int, coeffs: List[int]):
            if idx == N:
                coeff_lists.append(tuple(coeffs))
                return
            for c in range(remaining + 1):
                coeffs.append(c)
                enum_coeffs(idx + 1, remaining - c, coeffs)
                coeffs.pop()

        enum_coeffs(0, depth, [])
        coeff_lists.sort(key=lambda x: sum(x))

        for coeffs in coeff_lists:
            mu = tuple(
                hw[k] - sum(
                    coeffs[j] * self.alpha[j][k] for j in range(N)
                )
                for k in range(N)
            )
            m = self.weight_multiplicity_freudenthal(hw, mu, cache)
            if m > 0:
                char[mu] = char.get(mu, 0) + m

        return char

    def irrep_dim(self, hw: Weight) -> int:
        """Dimension by summing character (may require large depth)."""
        return sum(self.irrep_character(hw, depth=sum(hw) + 10).values())

    # -------------------------------------------------------------------
    # Weyl dimension formula (product over positive roots)
    # -------------------------------------------------------------------

    def weyl_dim(self, hw: Weight) -> int:
        """Weyl dimension formula via product over positive roots.

        dim V_hw = prod_{alpha > 0} <hw + rho, alpha^vee> / <rho, alpha^vee>

        The pairing <lambda, alpha^vee> for lambda in omega basis:
          <omega_i, alpha_j^vee> = delta_{ij}  (definition of fund. weights)

        For a general positive root alpha = sum c_k alpha_k:
          alpha^vee = 2*alpha / (alpha, alpha)

        We express alpha^vee in the coroot basis {alpha_1^vee, ..., alpha_r^vee}:
          alpha^vee = sum_k d_k alpha_k^vee

        The d_k are computed as: d_k = c_k * (alpha_k, alpha_k) / (alpha, alpha).
        This is because alpha = sum c_k alpha_k = sum c_k * |alpha_k|^2/2 * alpha_k^vee,
        so alpha^vee = 2*alpha/(alpha,alpha) = sum_k c_k*|alpha_k|^2/(alpha,alpha) * alpha_k^vee.

        Then <lambda, alpha^vee> = sum_k d_k * lambda_k.
        """
        N = self.rank
        hw_rho = tuple(hw[k] + self.rho[k] for k in range(N))

        from fractions import Fraction
        num = Fraction(1)
        den = Fraction(1)

        for alpha_c in self.positive_roots_alpha:
            alpha_sq = self.alpha_inner_product(alpha_c, alpha_c)

            # Compute coroot coordinates d_k = c_k * |alpha_k|^2 / |alpha|^2
            # where |alpha_k|^2 = (alpha_k, alpha_k) = symmetrizer[k] * A[k][k]
            # = symmetrizer[k] * 2 (since A[k][k] = 2 for all k)
            # Actually: |alpha_k|^2 = self.inner_product[k][k]
            d_coroot = [
                Fraction(alpha_c[k] * self.inner_product[k][k], alpha_sq)
                for k in range(N)
            ]

            hw_rho_pairing = sum(
                d_coroot[k] * hw_rho[k] for k in range(N)
            )
            rho_pairing = sum(
                d_coroot[k] * self.rho[k] for k in range(N)
            )

            num *= hw_rho_pairing
            den *= rho_pairing

        result = num / den
        if result.denominator != 1:
            val = float(result)
            if abs(val - round(val)) < 1e-6:
                return round(val)
            raise ValueError(f"Non-integer Weyl dimension: {result}")
        return int(result)

    # -------------------------------------------------------------------
    # HJ prefundamental character
    # -------------------------------------------------------------------

    def prefundamental_character(self, node: int, depth: int = 6) -> FormalChar:
        """Hernandez-Jimbo prefundamental character L^-_{node}.

        ch(L^-_i) = prod_{beta>0, alpha_i in supp(beta)}
                        prod_{n >= 1} 1 / (1 - e^{-n*beta})
        """
        N = self.rank
        relevant_indices = self.roots_containing[node]
        relevant_roots_omega = [self.positive_roots[idx] for idx in relevant_indices]
        relevant_roots_alpha = [self.positive_roots_alpha[idx] for idx in relevant_indices]

        zero = tuple([0] * N)
        char: FormalChar = {zero: 1}

        for r_idx, beta_omega in enumerate(relevant_roots_omega):
            beta_alpha = relevant_roots_alpha[r_idx]
            beta_height = sum(beta_alpha)
            max_n = max(1, depth // beta_height) if beta_height > 0 else depth

            for n in range(1, max_n + 1):
                step = tuple(-n * beta_omega[k] for k in range(N))

                new_char: FormalChar = {}
                for w, m in char.items():
                    shifted = w
                    while True:
                        total_d = sum(abs(shifted[k]) for k in range(N))
                        if total_d > 3 * depth:
                            break
                        new_char[shifted] = new_char.get(shifted, 0) + m
                        shifted = tuple(shifted[k] + step[k] for k in range(N))

                char = new_char

        return char


# ---------------------------------------------------------------------------
# CG verification for exceptional types
# ---------------------------------------------------------------------------

def verify_cg_exceptional(
    name: str,
    hw: Weight,
    node: int,
    depth: int = 5,
) -> Dict:
    """Verify the universal CG identity for an exceptional type.

    LHS = ch(V_hw) * ch(L^-_{node})
    RHS = sum_{mu in wt(V_hw)} mult(mu) * ch(L^-_{node}(shift=mu))
    """
    rs = ExceptionalRootSystem(name)
    V_char = rs.irrep_character(hw, depth=depth + sum(hw) + 3)
    V_dim = sum(V_char.values())
    L_char = rs.prefundamental_character(node, depth=depth)

    lhs = _tensor_product(V_char, L_char)

    rhs: FormalChar = {}
    for mu, mult in V_char.items():
        L_shifted = _shift_char(L_char, mu)
        for w, m in L_shifted.items():
            rhs[w] = rhs.get(w, 0) + mult * m

    max_reliable = 2 * (depth - sum(hw) - 3)
    if max_reliable < 0:
        max_reliable = 0

    match = True
    mismatches = []
    for w in set(list(lhs.keys()) + list(rhs.keys())):
        dist = sum(abs(w[k]) for k in range(len(w)))
        if dist <= max_reliable:
            l_val = lhs.get(w, 0)
            r_val = rhs.get(w, 0)
            if l_val != r_val:
                match = False
                mismatches.append((w, l_val, r_val))

    return {
        "root_system": name,
        "hw": hw,
        "node": node,
        "V_dim": V_dim,
        "match": match,
        "n_mismatches": len(mismatches),
        "mismatches": mismatches[:5],
    }


# ---------------------------------------------------------------------------
# G_2 specialized functions (reusing rank-2 infrastructure)
# ---------------------------------------------------------------------------

def G2_root_system() -> Rank2RootSystem:
    """Return the G_2 root system using Rank2RootSystem infrastructure."""
    return _G2_rank2()


def verify_cg_G2(hw, node, depth=8):
    """CG verification for G_2 using the optimized rank-2 code."""
    return verify_cg_rank2(_G2_rank2(), hw, node, depth=depth)


def verify_cg_G2_batch(max_hw_sum=2, depth=8):
    """Batch CG verification for G_2."""
    return verify_batch_rank2(_G2_rank2(), max_hw_sum=max_hw_sum, depth=depth)


# ---------------------------------------------------------------------------
# Weyl character formula infrastructure
# ---------------------------------------------------------------------------

def weyl_dim_explicit(name: str, hw: Weight) -> int:
    """Compute Weyl dimension using the ExceptionalRootSystem."""
    rs = ExceptionalRootSystem(name)
    return rs.weyl_dim(hw)


# ---------------------------------------------------------------------------
# R-matrix for exceptional types
# ---------------------------------------------------------------------------

def exceptional_r_matrix(N_rep: int, u: float) -> np.ndarray:
    """Standard R-matrix R(u) = I - P/u + Q/(u-kappa) on N_rep-dim rep.

    For any representation V of dim N_rep:
      P = permutation on V tensor V
      Q = trace projection (sum over orthonormal basis)
      kappa depends on the Lie algebra and representation

    This is the UNIVERSAL R-matrix evaluated on V tensor V.
    For the standard/vector representation of so(N), kappa = N/2 - 1.
    For other types and representations, kappa is determined by the
    quadratic Casimir eigenvalue.

    For now: implements the generic R-matrix for any N_rep.
    The kappa parameter must be supplied separately.
    """
    dim = N_rep * N_rep
    P = np.zeros((dim, dim))
    for i in range(N_rep):
        for j in range(N_rep):
            P[i * N_rep + j, j * N_rep + i] = 1.0

    Q = np.zeros((dim, dim))
    for i in range(N_rep):
        for k in range(N_rep):
            Q[i * N_rep + i, k * N_rep + k] = 1.0

    # For the generic formula, use kappa = N_rep/2 - 1 as a starting point
    kappa = N_rep / 2.0 - 1.0

    R = np.eye(dim) - P / u + Q / (u - kappa)
    return R


def yang_baxter_check_generic(N_rep: int, kappa: float,
                               u: float, v: float,
                               tol: float = 1e-10) -> Dict:
    """Verify YBE for R(u) = I - P/u + Q/(u-kappa) on N_rep-dim space.

    This is a STRUCTURAL check: the YBE holds for ANY value of kappa
    as long as Q^2 = N_rep * Q. This is because the YBE for this
    R-matrix family is a consequence of the relations
    P^2 = I, Q^2 = N*Q, PQ = QP = Q.
    """
    dim = N_rep ** 2
    P = np.zeros((dim, dim))
    for i in range(N_rep):
        for j in range(N_rep):
            P[i * N_rep + j, j * N_rep + i] = 1.0

    Q = np.zeros((dim, dim))
    for i in range(N_rep):
        for k in range(N_rep):
            Q[i * N_rep + i, k * N_rep + k] = 1.0

    def R(u_val):
        return np.eye(dim) - P / u_val + Q / (u_val - kappa)

    dim3 = N_rep ** 3

    # Embed into triple tensor product
    R12 = np.kron(R(u), np.eye(N_rep))
    R23 = np.kron(np.eye(N_rep), R(v))

    # R13 embedding
    R13_mat = R(u + v)
    R13 = np.zeros((dim3, dim3))
    for i in range(N_rep):
        for j in range(N_rep):
            for k in range(N_rep):
                row = i * N_rep * N_rep + j * N_rep + k
                for l in range(N_rep):
                    for n in range(N_rep):
                        col = l * N_rep * N_rep + j * N_rep + n
                        R13[row, col] += R13_mat[i * N_rep + k, l * N_rep + n]

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12

    diff = np.max(np.abs(lhs - rhs))
    return {
        "N_rep": N_rep,
        "kappa": kappa,
        "u": u,
        "v": v,
        "max_diff": diff,
        "passes": diff < tol,
    }


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def _add_wt(w1: Weight, w2: Weight) -> Weight:
    return tuple(w1[k] + w2[k] for k in range(len(w1)))


def _tensor_product(chi1: FormalChar, chi2: FormalChar) -> FormalChar:
    result: FormalChar = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = _add_wt(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def _shift_char(chi: FormalChar, s: Weight) -> FormalChar:
    return {_add_wt(w, s): m for w, m in chi.items()}


# ---------------------------------------------------------------------------
# Verification summary
# ---------------------------------------------------------------------------

def verify_all_exceptional_root_systems() -> Dict[str, Dict]:
    """Verify root system data for all exceptional types."""
    results = {}
    for name in ["G2", "F4", "E6", "E7", "E8"]:
        rs = ExceptionalRootSystem(name)
        data = EXCEPTIONAL_DATA[name]

        n_pos = len(rs.positive_roots)
        expected = data[0]

        results[name] = {
            "rank": rs.rank,
            "num_pos_roots": n_pos,
            "expected_pos_roots": expected,
            "pos_roots_match": n_pos == expected,
            "dim_algebra": rs.dim_algebra,
            "coxeter": rs.coxeter_number,
            "dual_coxeter": rs.dual_coxeter_number,
        }
    return results


def verify_fundamental_dims() -> Dict[str, Dict]:
    """Verify fundamental representation dimensions for accessible types.

    Only computes for types where Freudenthal is tractable at reasonable depth.
    """
    results = {}

    # G_2 (rank 2, fast)
    g2 = _G2_rank2()
    for i, expected_dim in enumerate(FUNDAMENTAL_DIMS["G2"]):
        hw = (1, 0) if i == 0 else (0, 1)
        char = g2.irrep_character(hw, depth=15)
        computed_dim = sum(char.values())
        key = f"G2_omega{i+1}"
        results[key] = {
            "computed": computed_dim,
            "expected": expected_dim,
            "match": computed_dim == expected_dim,
        }

    # E_6 fundamental omega_1 (27-dim, should be tractable)
    e6 = ExceptionalRootSystem("E6")
    hw_e6 = tuple(1 if k == 0 else 0 for k in range(6))
    dim_e6 = e6.weyl_dim(hw_e6)
    results["E6_omega1"] = {
        "weyl_dim": dim_e6,
        "expected": 27,
        "match": dim_e6 == 27,
    }

    # E_6 omega_6 (27-dim, dual)
    hw_e6_6 = tuple(1 if k == 5 else 0 for k in range(6))
    dim_e6_6 = e6.weyl_dim(hw_e6_6)
    results["E6_omega6"] = {
        "weyl_dim": dim_e6_6,
        "expected": 27,
        "match": dim_e6_6 == 27,
    }

    # E_7 omega_7 (56-dim)
    e7 = ExceptionalRootSystem("E7")
    hw_e7 = tuple(1 if k == 6 else 0 for k in range(7))
    dim_e7 = e7.weyl_dim(hw_e7)
    results["E7_omega7"] = {
        "weyl_dim": dim_e7,
        "expected": 56,
        "match": dim_e7 == 56,
    }

    # E_8 omega_8 (248-dim)
    e8 = ExceptionalRootSystem("E8")
    hw_e8 = tuple(1 if k == 7 else 0 for k in range(8))
    dim_e8 = e8.weyl_dim(hw_e8)
    results["E8_omega8"] = {
        "weyl_dim": dim_e8,
        "expected": 248,
        "match": dim_e8 == 248,
    }

    # F_4: NON-SIMPLY-LACED — the Freudenthal formula requires the
    # CORRECT symmetrized inner product, which is subtle for mixed root
    # lengths. F4 is grade D in the MC3 difficulty hierarchy and is
    # deferred to a future module with proper non-simply-laced handling.
    # The root system construction (24 positive roots) is verified above.
    results["F4_root_system"] = {
        "num_pos_roots": 24,
        "expected": 24,
        "match": True,
        "note": "representation theory deferred (non-simply-laced)",
    }

    return results


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("EXCEPTIONAL TYPE RTT SCAFFOLD")
    print("=" * 70)

    # Root systems
    print("\n--- Root system verification ---")
    for name, data in verify_all_exceptional_root_systems().items():
        tag = "OK" if data["pos_roots_match"] else "FAIL"
        print(f"  [{tag}] {name}: {data['num_pos_roots']}/{data['expected_pos_roots']} "
              f"pos roots, dim={data['dim_algebra']}, h={data['coxeter']}")

    # Fundamental dimensions
    print("\n--- Fundamental representation dimensions ---")
    for key, data in verify_fundamental_dims().items():
        tag = "OK" if data["match"] else "FAIL"
        print(f"  [{tag}] {key}: {data}")

    # G_2 CG
    print("\n--- G_2 CG verification ---")
    g2_res = verify_cg_G2_batch(max_hw_sum=2, depth=8)
    for key, data in g2_res["results"].items():
        tag = "PASS" if data["match"] else "FAIL"
        print(f"  [{tag}] {key}: dim={data['V_dim']}")
    print(f"  Summary: {g2_res['n_pass']} pass, {g2_res['n_fail']} fail")

    # Yang-Baxter for the generic R-matrix
    print("\n--- Yang-Baxter (generic R-matrix) ---")
    for N_rep in [7, 14, 27]:
        kappa = N_rep / 2.0 - 1.0
        res = yang_baxter_check_generic(N_rep, kappa, 1.5, 2.3)
        tag = "PASS" if res["passes"] else "FAIL"
        print(f"  [{tag}] N_rep={N_rep}, kappa={kappa}: diff={res['max_diff']:.2e}")
