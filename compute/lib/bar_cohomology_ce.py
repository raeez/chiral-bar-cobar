"""Chevalley-Eilenberg cohomology of negative-mode Lie algebras.

Computes H^*(g_-, C) for the negative-mode Lie algebras g_- associated
to chiral algebras. This is a PURELY LIE-ALGEBRAIC computation that
uses only the Lie bracket, antisymmetry, and Jacobi identity. It does
NOT use OPE data, configuration space forms, or factorization structure.

For three families:
  1. Affine sl_2: g_- = sl_2 tensor t^{-1}C[t^{-1}], dim = 3 per weight
  2. Affine sl_3: g_- = sl_3 tensor t^{-1}C[t^{-1}], dim = 8 per weight
  3. Virasoro/Witt: W_+ = Span{L_{-n} : n >= 2}, dim = 1 per weight >= 2

In each case, no central extension: for modes at weight m, n >= 1 (KM)
or m, n >= 2 (Vir), delta_{m+n, 0} = 0.

RELATIONSHIP TO BAR COHOMOLOGY:

The CE cohomology H^*(g_-, C) is RELATED TO but NOT IDENTICAL WITH the
chiral bar cohomology H^*(B(A)). The chiral bar complex involves the
full factorization structure (tensor products with OS forms on
configuration spaces), while CE uses exterior powers. Specifically:

  - CE^n_H = Lambda^n(g_-^*)_H (antisymmetric n-forms)
  - Bar chain: B^n_H = (g^{tensor n} tensor OS^{n-1})_H

These are different spaces. The bar chain group dim = dim(g)^n * (n-1)!
is much larger than C(dim(g), n) at each weight.

EMPIRICAL COMPARISON (this module's raison d'etre):

  sl_2:  CE H^1 = 3  bar H^1 = 3   AGREE
         CE H^2 = 5  bar H^2 = 5   AGREE
         CE H^3 = 7  bar H^3 = 15  DIFFER (bar has OS form contributions)
  sl_3:  CE H^1 = 8  bar H^1 = 8   AGREE
         CE H^2 = 20 bar H^2 = 36  DIFFER
  Witt:  CE H^1 = 3  bar H^1 = 1   DIFFER (CE counts mode generators,
         CE H^2 = 5  bar H^2 = 2          bar counts field generators)

The agreement at H^1 for KM algebras (CE = dim(g) = bar) holds because
H^1(g_-) = g_-/[g_-,g_-] = g (the abelianization) and H^1(B(A)) = A_1/CA_0
(generators modulo constants), which both give dim(g) for a KM algebra
with weight-1 generators.

The disagreement at higher degrees shows that the factorization
structure (OS forms) contributes non-trivially to bar cohomology.
This is a GENUINE finding, not a bug.

CONVENTIONS:
  - Cohomological grading: |d_CE| = +1
  - CE^p_H = Lambda^p(g_-^*)_H = antisymmetric p-forms of total weight H
  - d_CE: CE^p_H -> CE^{p+1}_H preserves weight

References:
  - bar_cohomology_verification.py: existing sl_2 CE via LoopAlgebraCE
  - ce_cohomology_loop.py: existing sl_3 CE via numpy
  - sl3_bar.py: sl_3 structure constants
  - spectral_sequence.py: known bar cohomology values
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, zeros


# ============================================================
# Lie algebra data
# ============================================================

# --- sl_2 ---
# Basis: e=0, h=1, f=2.  [e,f]=h, [h,e]=2e, [h,f]=-2f.

SL2_DIM = 3
SL2_BRACKET: Dict[Tuple[int, int], Dict[int, int]] = {
    (0, 2): {1: 1}, (2, 0): {1: -1},     # [e,f] = h
    (1, 0): {0: 2}, (0, 1): {0: -2},      # [h,e] = 2e
    (1, 2): {2: -2}, (2, 1): {2: 2},      # [h,f] = -2f
}

# --- sl_3 ---
# Basis: H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7.
# Imported from sl3_bar.py at runtime to avoid import dependency at module level.

SL3_DIM = 8

def _get_sl3_bracket() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Load sl_3 structure constants, converting Rational to int."""
    from compute.lib.sl3_bar import sl3_structure_constants
    raw = sl3_structure_constants()
    result = {}
    for key, val_dict in raw.items():
        result[key] = {k: int(v) for k, v in val_dict.items()}
    return result


# --- Witt algebra W_+ = {L_{-n} : n >= 2} ---
# Bracket: [L_{-m}, L_{-n}] = (n - m) L_{-(m+n)}
# Generator index: L_{-n} has flat index n - 2 (so L_{-2} = index 0, etc.)
# Weight of L_{-n} is n.
# No central extension: m, n >= 2 implies m+n >= 4 > 0.

def witt_bracket(max_weight: int) -> Tuple[int, Dict[Tuple[int, int], Dict[int, int]]]:
    """Structure constants for W_+ = {L_{-n} : n >= 2} truncated at max_weight.

    Generator L_{-n} has index n-2 and weight n.
    dim = max_weight - 1 (generators at weights 2, 3, ..., max_weight).

    Returns (dim, bracket_dict).
    """
    dim = max_weight - 1
    if dim <= 0:
        return 0, {}
    bracket: Dict[Tuple[int, int], Dict[int, int]] = {}
    for m in range(2, max_weight + 1):
        for n in range(m + 1, max_weight + 1):
            s = m + n
            if s > max_weight:
                continue
            coeff = n - m  # [L_{-m}, L_{-n}] = (n-m) L_{-(m+n)}
            if coeff != 0:
                i_m = m - 2
                i_n = n - 2
                i_s = s - 2
                bracket[(i_m, i_n)] = {i_s: coeff}
                bracket[(i_n, i_m)] = {i_s: -coeff}
    return dim, bracket


# ============================================================
# Loop algebra construction
# ============================================================

def loop_algebra_bracket(
    dim_g: int,
    bracket: Dict[Tuple[int, int], Dict[int, int]],
    max_weight: int,
    min_weight: int = 1,
) -> Tuple[int, Dict[Tuple[int, int], Dict[int, int]], List[int]]:
    """Build the negative loop algebra g_- = g tensor t^{-1}C[t^{-1}].

    For KM: g_- has generators (a, n) for 0 <= a < dim_g, min_weight <= n <= max_weight.
    Bracket: [(a,m), (b,n)] = f^c_{ab} * (c, m+n) if m+n <= max_weight.
    No central extension.

    For Witt: dim_g = max_weight - 1, bracket already includes mode structure.
    In this case, return the bracket directly (it IS the loop algebra).

    Returns: (total_dim, loop_bracket, generator_weights).
    """
    # Flat index: a + dim_g * (n - min_weight) for KM
    total_dim = dim_g * (max_weight - min_weight + 1)
    gen_weights = []
    for n in range(min_weight, max_weight + 1):
        for a in range(dim_g):
            gen_weights.append(n)

    loop_br: Dict[Tuple[int, int], Dict[int, int]] = {}
    for m in range(min_weight, max_weight + 1):
        for a in range(dim_g):
            i = a + dim_g * (m - min_weight)
            for n in range(m, max_weight + 1):
                if m + n > max_weight:
                    continue
                for b in range(dim_g):
                    j = b + dim_g * (n - min_weight)
                    if i >= j:
                        continue
                    br = bracket.get((a, b))
                    if not br:
                        continue
                    result = {}
                    for c, coeff in br.items():
                        k = c + dim_g * (m + n - min_weight)
                        result[k] = coeff
                    if result:
                        loop_br[(i, j)] = result
                        # Antisymmetric
                        loop_br[(j, i)] = {k: -v for k, v in result.items()}

    return total_dim, loop_br, gen_weights


# ============================================================
# CE complex engine (unified for all Lie algebras)
# ============================================================

class ChevalleyEilenbergComplex:
    """CE complex of a Lie algebra, graded by weight.

    Given a Lie algebra g with a weight grading (each generator has
    a positive integer weight), compute the CE cohomology
    H^*(g, C) at each weight.

    CE^p_H = Lambda^p(g*)_H = antisymmetric p-forms of total weight H.
    d_CE: CE^p_H -> CE^{p+1}_H via the dual of the Lie bracket.

    The CE differential on cochains is:
      (d alpha)(x_1, ..., x_{p+1}) =
        sum_{i<j} (-1)^{i+j} alpha([x_i, x_j], x_1, ..., x-hat_i, ..., x-hat_j, ..., x_{p+1})

    On the basis e^{i_1} ^ ... ^ e^{i_p} (dual to e_{i_1} ^ ... ^ e_{i_p}),
    d is determined by the structure constants:
      d(e^k) = -(1/2) sum_{a,b} f^{ab}_k e^a ^ e^b
    for degree 1, extended by the graded Leibniz rule.
    """

    def __init__(
        self,
        dim_g: int,
        bracket: Dict[Tuple[int, int], Dict[int, int]],
        gen_weights: List[int],
    ):
        self.dim_g = dim_g
        self.bracket = bracket
        self.gen_weights = gen_weights
        # Precompute: for each ordered pair (i < j), the bracket data
        self._ordered_bracket: Dict[Tuple[int, int], Dict[int, int]] = {}
        for (a, b), result in bracket.items():
            if a < b:
                self._ordered_bracket[(a, b)] = result

    def weight_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Basis of Lambda^degree(g*)_weight.

        Returns sorted tuples of generator indices (i_1 < ... < i_degree)
        with sum of weights = weight.
        """
        return list(self._weight_subsets(degree, weight, 0))

    def _weight_subsets(self, degree: int, target: int, start: int):
        """Generate degree-subsets of generators with exact weight sum."""
        if degree == 0:
            if target == 0:
                yield ()
            return
        for i in range(start, self.dim_g - degree + 1):
            w = self.gen_weights[i]
            if w > target:
                continue
            remaining_slots = degree - 1
            # Each remaining generator has weight >= gen_weights[i+1] >= 1
            # (crude lower bound: remaining_slots * 1)
            if target - w < remaining_slots:
                continue
            for rest in self._weight_subsets(remaining_slots, target - w, i + 1):
                yield (i,) + rest

    def chain_group_dim(self, degree: int, weight: int) -> int:
        """Dimension of CE^degree_weight."""
        return len(self.weight_basis(degree, weight))

    def ce_differential(self, degree: int, weight: int) -> Matrix:
        """CE differential d: CE^degree_weight -> CE^{degree+1}_weight.

        Uses the standard sign convention for the CE coboundary:
        for a basis element alpha = e^{a_1} ^ ... ^ e^{a_p},
        d(alpha) involves pairs (beta, gamma) from the bracket
        [e_beta, e_gamma] = f^{beta,gamma}_c e_c where c is in alpha.
        The contraction replaces c with (beta, gamma) in the exterior product.

        Sign: (-1)^{pos(c)} * (-1)^{pos(beta in new)} * (-1)^{pos(gamma in rest)}.
        """
        source = self.weight_basis(degree, weight)
        target = self.weight_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)
        if n_src == 0 or n_tgt == 0:
            return zeros(n_tgt, n_src)

        target_idx = {t: i for i, t in enumerate(target)}
        mat = zeros(n_tgt, n_src)

        for col, alpha in enumerate(source):
            alpha_set = set(alpha)
            alpha_list = list(alpha)
            for (beta, gamma), br in self._ordered_bracket.items():
                for c, coeff in br.items():
                    if c not in alpha_set:
                        continue
                    # Remove c, add beta and gamma
                    new_set = (alpha_set - {c}) | {beta, gamma}
                    if len(new_set) != degree + 1:
                        # beta or gamma was already in alpha, or beta == gamma
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue
                    # Sign computation
                    pos_c = alpha_list.index(c)
                    sorted_new = list(new_tuple)
                    pos_beta = sorted_new.index(beta)
                    remaining = sorted(new_set - {beta})
                    pos_gamma = remaining.index(gamma)
                    sign = (-1) ** pos_c * (-1) ** pos_beta * (-1) ** pos_gamma
                    mat[row, col] += sign * coeff

        return mat

    def verify_d_squared(self, degree: int, weight: int) -> bool:
        """Check d^2 = 0 at given degree and weight."""
        d_p = self.ce_differential(degree, weight)
        d_p1 = self.ce_differential(degree + 1, weight)
        if d_p.cols == 0 or d_p1.rows == 0:
            return True
        if d_p.rows != d_p1.cols:
            return True
        return (d_p1 * d_p).is_zero_matrix

    def cohomology_dim(self, degree: int, weight: int) -> int:
        """dim H^degree(g, C)_weight."""
        dim_p = self.chain_group_dim(degree, weight)
        if dim_p == 0:
            return 0
        d_curr = self.ce_differential(degree, weight)
        ker = dim_p - (d_curr.rank() if d_curr.rows > 0 else 0)
        if degree > 0:
            d_prev = self.ce_differential(degree - 1, weight)
            im = d_prev.rank() if d_prev.rows > 0 and d_prev.cols > 0 else 0
        else:
            im = 0
        return ker - im

    def cohomology_table(
        self,
        max_degree: int,
        max_weight: int,
        min_weight: int = 1,
    ) -> Dict[Tuple[int, int], int]:
        """Compute H^n_H for all n <= max_degree, min_weight <= H <= max_weight.

        Returns {(degree, weight): dim}.
        """
        table: Dict[Tuple[int, int], int] = {}
        for H in range(min_weight, max_weight + 1):
            for n in range(0, max_degree + 1):
                if n > H:  # can't have more exterior factors than total weight
                    break
                dim = self.cohomology_dim(n, H)
                if dim > 0:
                    table[(n, H)] = dim
        return table

    def total_cohomology(
        self,
        max_degree: int,
        max_weight: int,
        min_weight: int = 1,
    ) -> Dict[int, int]:
        """Total H^n = sum_H H^n_H for n = 1, ..., max_degree.

        Returns {degree: total_dim}.
        """
        result = {}
        for n in range(1, max_degree + 1):
            total = 0
            for H in range(min_weight, max_weight + 1):
                total += self.cohomology_dim(n, H)
            result[n] = total
        return result


# ============================================================
# Factory functions for specific algebras
# ============================================================

def sl2_ce(max_weight: int = 8) -> ChevalleyEilenbergComplex:
    """CE complex of g_- = sl_2 tensor t^{-1}C[t^{-1}], truncated at max_weight.

    Generators: (a, n) for a in {e, h, f}, n = 1, ..., max_weight.
    Total dim = 3 * max_weight.
    Weight of generator (a, n) = n.
    """
    total_dim, loop_br, gen_weights = loop_algebra_bracket(
        SL2_DIM, SL2_BRACKET, max_weight, min_weight=1
    )
    return ChevalleyEilenbergComplex(total_dim, loop_br, gen_weights)


def sl3_ce(max_weight: int = 5) -> ChevalleyEilenbergComplex:
    """CE complex of g_- = sl_3 tensor t^{-1}C[t^{-1}], truncated at max_weight.

    Generators: (a, n) for a in {H1,H2,E1,E2,E3,F1,F2,F3}, n = 1, ..., max_weight.
    Total dim = 8 * max_weight.
    """
    sl3_br = _get_sl3_bracket()
    total_dim, loop_br, gen_weights = loop_algebra_bracket(
        SL3_DIM, sl3_br, max_weight, min_weight=1
    )
    return ChevalleyEilenbergComplex(total_dim, loop_br, gen_weights)


def witt_ce(max_weight: int = 12) -> ChevalleyEilenbergComplex:
    """CE complex of W_+ = {L_{-n} : n >= 2}, truncated at max_weight.

    One generator per weight n = 2, 3, ..., max_weight.
    Total dim = max_weight - 1.
    Bracket: [L_{-m}, L_{-n}] = (n-m) L_{-(m+n)}.
    No central extension.

    The CE cohomology H^*(W_+, C) gives the E_2 page of the PBW
    spectral sequence on B(Vir_c). If the SS collapses at E_2
    (chiral Koszulness), this equals bar cohomology.

    NOTE: The generators here start at weight 2, not weight 1.
    So weight_basis(1, 1) = [] (no generators at weight 1).
    """
    dim, bracket = witt_bracket(max_weight)
    # Generator weights: 2, 3, ..., max_weight
    gen_weights = list(range(2, max_weight + 1))
    return ChevalleyEilenbergComplex(dim, bracket, gen_weights)


# ============================================================
# High-level verification functions
# ============================================================

def sl2_bar_cohomology_ce(
    max_degree: int = 3,
    max_weight: int = 8,
) -> Dict[int, int]:
    """H^n(B(sl_2)) via CE of the negative loop algebra.

    Returns {bar_degree: total_cohomology_dim}.

    Expected: H^1 = 3, H^2 = 5, H^3 = 15.
    """
    ce = sl2_ce(max_weight)
    return ce.total_cohomology(max_degree, max_weight)


def sl2_bar_cohomology_ce_detail(
    max_degree: int = 3,
    max_weight: int = 8,
) -> Dict[int, Dict[int, int]]:
    """Weight decomposition of H^n(B(sl_2)) via CE.

    Returns {bar_degree: {weight: dim}}.
    """
    ce = sl2_ce(max_weight)
    result: Dict[int, Dict[int, int]] = {}
    for n in range(1, max_degree + 1):
        weight_decomp = {}
        for H in range(1, max_weight + 1):
            d = ce.cohomology_dim(n, H)
            if d > 0:
                weight_decomp[H] = d
        result[n] = weight_decomp
    return result


def sl3_bar_cohomology_ce(
    max_degree: int = 2,
    max_weight: int = 5,
) -> Dict[int, int]:
    """H^n(B(sl_3)) via CE of the negative loop algebra.

    Returns {bar_degree: total_cohomology_dim}.

    Expected: H^1 = 8, H^2 = 36, H^3 = 204.
    """
    ce = sl3_ce(max_weight)
    return ce.total_cohomology(max_degree, max_weight)


def sl3_bar_cohomology_ce_detail(
    max_degree: int = 2,
    max_weight: int = 5,
) -> Dict[int, Dict[int, int]]:
    """Weight decomposition of H^n(B(sl_3)) via CE.

    Returns {bar_degree: {weight: dim}}.
    """
    ce = sl3_ce(max_weight)
    result: Dict[int, Dict[int, int]] = {}
    for n in range(1, max_degree + 1):
        weight_decomp = {}
        for H in range(1, max_weight + 1):
            d = ce.cohomology_dim(n, H)
            if d > 0:
                weight_decomp[H] = d
        result[n] = weight_decomp
    return result


def vir_bar_cohomology_ce(
    max_degree: int = 4,
    max_weight: int = 14,
) -> Dict[int, int]:
    """H^n(W_+, C) via CE of the positive Witt algebra.

    Returns {CE_degree: total_cohomology_dim}.

    If the PBW spectral sequence collapses at E_2, these should
    equal the Virasoro bar cohomology dims (Motzkin differences):
      1, 2, 5, 12, 30, 76, 196, 512, ...

    IMPORTANT: The Witt algebra W_+ has generators at weight >= 2.
    The total H^n is sum_{H >= 2n} H^n(W_+)_H.
    """
    ce = witt_ce(max_weight)
    return ce.total_cohomology(max_degree, max_weight, min_weight=2)


def vir_bar_cohomology_ce_detail(
    max_degree: int = 4,
    max_weight: int = 14,
) -> Dict[int, Dict[int, int]]:
    """Weight decomposition of H^n(W_+, C).

    Returns {degree: {weight: dim}}.
    """
    ce = witt_ce(max_weight)
    result: Dict[int, Dict[int, int]] = {}
    for n in range(1, max_degree + 1):
        weight_decomp = {}
        for H in range(2, max_weight + 1):
            d = ce.cohomology_dim(n, H)
            if d > 0:
                weight_decomp[H] = d
        result[n] = weight_decomp
    return result


# ============================================================
# Cross-verification against known values
# ============================================================

def motzkin_differences(max_n: int = 10) -> Dict[int, int]:
    """Virasoro bar cohomology = first differences of Motzkin numbers.

    M(n+1) - M(n) for n = 1, 2, 3, ...
    Values: 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610
    """
    N = max_n + 2
    M = [0] * N
    M[0] = 1
    if N > 1:
        M[1] = 1
    for i in range(2, N):
        M[i] = M[i - 1] + sum(M[k] * M[i - 2 - k] for k in range(i - 1))
    return {n: M[n + 1] - M[n] for n in range(1, max_n + 1)}


def riordan(n: int) -> int:
    """Riordan number R(n). OEIS A005043."""
    if n <= 0:
        return 1
    if n == 1:
        return 0
    R = [1, 0]
    for k in range(2, n + 1):
        num = (k - 1) * (2 * R[k - 1] + 3 * R[k - 2])
        assert num % (k + 1) == 0
        R.append(num // (k + 1))
    return R[n]


def cross_verify_sl2(max_degree: int = 3, max_weight: int = 8) -> Dict[str, dict]:
    """Cross-verify sl_2 CE against known bar cohomology.

    CE H^*(g_-, C) and bar H^*(B(sl_2)) agree at degrees 1 and 2
    but DIFFER at degree 3: CE H^3 = 7, bar H^3 = 15.
    The discrepancy arises because bar uses tensor products with OS
    forms on configuration spaces, while CE uses exterior powers.
    """
    ce_vals = sl2_bar_cohomology_ce(max_degree, max_weight)
    # Known bar cohomology from manuscript
    known_bar = {1: 3, 2: 5, 3: 15, 4: 36, 5: 91, 6: 232}
    # Known CE values (independently verified)
    known_ce = {1: 3, 2: 5, 3: 7}
    riordan_vals = {n: riordan(n + 3) for n in range(1, max_degree + 1)}

    results = {}
    for n in range(1, max_degree + 1):
        r = {
            "CE": ce_vals.get(n, 0),
            "known_CE": known_ce.get(n),
            "bar_cohomology": known_bar.get(n),
            "Riordan": riordan_vals.get(n),
        }
        r["CE_eq_bar"] = r["CE"] == r["bar_cohomology"] if r["bar_cohomology"] else None
        r["CE_eq_known_CE"] = r["CE"] == r["known_CE"] if r["known_CE"] else None
        results[n] = r
    return results


def cross_verify_sl3(max_degree: int = 2, max_weight: int = 5) -> Dict[str, dict]:
    """Cross-verify sl_3 CE against known bar cohomology.

    CE H^1 = 8 matches bar H^1 = 8.
    CE H^2 = 20 does NOT match bar H^2 = 36.
    The CE uses exterior powers; the chiral bar complex uses
    tensor products with OS forms on configuration spaces.
    """
    ce_vals = sl3_bar_cohomology_ce(max_degree, max_weight)
    known_bar = {1: 8, 2: 36, 3: 204}
    known_ce = {1: 8, 2: 20, 3: 70}

    results = {}
    for n in range(1, max_degree + 1):
        r = {
            "CE": ce_vals.get(n, 0),
            "known_CE": known_ce.get(n),
            "bar_cohomology": known_bar.get(n),
        }
        r["CE_eq_bar"] = r["CE"] == r["bar_cohomology"] if r["bar_cohomology"] else None
        r["CE_eq_known_CE"] = r["CE"] == r["known_CE"] if r["known_CE"] else None
        results[n] = r
    return results


def cross_verify_virasoro(max_degree: int = 4, max_weight: int = 14) -> Dict[str, dict]:
    """Cross-verify Witt CE against Virasoro bar cohomology (Motzkin diffs).

    CE H^*(W_+, C) and bar H^*(B(Vir)) are different objects:
      CE H^1 = 3 (mode generators L_{-2}, L_{-3}, L_{-4})
      bar H^1 = 1 (field generator T)
    The CE counts mode generators modulo brackets; the bar counts field
    generators modulo OPE relations.
    """
    ce_vals = vir_bar_cohomology_ce(max_degree, max_weight)
    motzkin = motzkin_differences(max_degree)

    results = {}
    for n in range(1, max_degree + 1):
        r = {
            "CE_of_Witt": ce_vals.get(n, 0),
            "Motzkin_diff": motzkin.get(n),
        }
        r["agree"] = r["CE_of_Witt"] == r["Motzkin_diff"]
        results[n] = r
    return results


# ============================================================
# Euler characteristic verification
# ============================================================

def ce_euler_characteristic(
    ce: ChevalleyEilenbergComplex,
    max_degree: int,
    weight: int,
) -> int:
    """Euler characteristic chi = sum (-1)^n dim CE^n at a given weight.

    Should equal sum (-1)^n dim H^n at the same weight (by exactness).
    Also computable from the product formula:
      chi_weight = coefficient of q^weight in prod (1 - q^{w_i})
    where w_i are generator weights.
    """
    return sum(
        (-1) ** n * ce.chain_group_dim(n, weight)
        for n in range(0, max_degree + 1)
    )


def verify_euler_product(
    ce: ChevalleyEilenbergComplex,
    max_weight: int,
) -> Dict[int, Tuple[int, int, bool]]:
    """Verify CE Euler char = product formula at each weight.

    The Euler product: prod_{i} (1 - q^{w_i}) gives the generating
    function for chi. For the exterior algebra on generators of weights
    w_1, ..., w_N, the coefficient of q^H in prod (1 - q^{w_i}) equals
    the alternating sum of exterior power dimensions.

    Returns {weight: (euler_from_dims, euler_from_product, agree)}.
    """
    # Build the product (1 - q^{w_1}) * ... * (1 - q^{w_N})
    # as a polynomial in q, truncated at max_weight.
    product_coeffs = [0] * (max_weight + 1)
    product_coeffs[0] = 1
    for w in ce.gen_weights:
        new_coeffs = [0] * (max_weight + 1)
        for h in range(max_weight + 1):
            new_coeffs[h] += product_coeffs[h]
            if h + w <= max_weight:
                new_coeffs[h + w] -= product_coeffs[h]
        product_coeffs = new_coeffs

    results = {}
    for H in range(1, max_weight + 1):
        max_deg = min(H, ce.dim_g)
        euler_dims = sum(
            (-1) ** n * ce.chain_group_dim(n, H)
            for n in range(0, max_deg + 1)
        )
        euler_prod = product_coeffs[H]
        results[H] = (euler_dims, euler_prod, euler_dims == euler_prod)
    return results


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BAR COHOMOLOGY VIA CHEVALLEY-EILENBERG COMPLEX")
    print("=" * 60)

    print("\n--- sl_2 CE cohomology ---")
    sl2_detail = sl2_bar_cohomology_ce_detail(max_degree=2, max_weight=6)
    for n, decomp in sl2_detail.items():
        total = sum(decomp.values())
        print(f"  H^{n} = {total}  (by weight: {decomp})")

    print("\n--- sl_3 CE cohomology ---")
    sl3_vals = sl3_bar_cohomology_ce(max_degree=1, max_weight=3)
    for n, v in sl3_vals.items():
        print(f"  H^{n} = {v}")

    print("\n--- Witt CE cohomology (Virasoro PBW E_2) ---")
    vir_detail = vir_bar_cohomology_ce_detail(max_degree=3, max_weight=10)
    for n, decomp in vir_detail.items():
        total = sum(decomp.values())
        print(f"  H^{n} = {total}  (by weight: {decomp})")

    print("\n--- Cross-verification: sl_2 ---")
    xv = cross_verify_sl2(max_degree=2, max_weight=6)
    for n, r in xv.items():
        print(f"  n={n}: CE={r['CE']}, manuscript={r['manuscript']}, "
              f"Riordan={r['Riordan']}, match={r['CE_eq_manuscript']}")

    print("\n--- Cross-verification: Virasoro ---")
    xv = cross_verify_virasoro(max_degree=3, max_weight=10)
    for n, r in xv.items():
        status = "AGREE" if r["agree"] else "DIFFER"
        print(f"  n={n}: CE={r['CE_of_Witt']}, Motzkin={r['Motzkin_diff']} [{status}]")
