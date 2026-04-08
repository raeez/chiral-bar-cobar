r"""Bar cohomology from loop-group CE cohomology: the Garland-Lepowsky engine.

PRIMARY QUESTION
================

Why does bar cohomology of V_k(g) appear to depend only on dim(g)?

ANSWER (direct, from first-principles computation)
===================================================

It does NOT. The claim is FALSE at the level of bigraded dimensions.
It is TRUE at the level of Euler characteristics (signed sums).
It becomes TRUE at the level of total dimensions per weight only for
semisimple g where the Garland-Lepowsky concentration puts each weight
into a SINGLE CE degree, so the signed Euler sum equals the absolute
value of the total.

What does depend only on dim(g):

    chi(B(V_k(g)))_w = sum_p (-1)^p dim H^p(B)_w
                     = coefficient of t^w in prod_{n>=1} (1 - t^n)^{dim g}

(proved: inverse Hilbert series of the PBW filtration, which only sees
the number of generators at each mode).

What does NOT depend only on dim(g):

    dim H^p(B(V_k(g)))_w  (individual bigraded components)
    sum_p dim H^p(B)_w    (total dimension per weight, unsigned)

Concrete falsifications at dim_g = 3 (sl_2 vs abelian^3 vs Heisenberg nilpotent):

    Algebra           Total bar dim at weights 1..6
    sl_2           :  [3,  0,  5,  0,  0,  7]    (Garland-Lepowsky)
    abelian^3      :  [3,  6, 13, 24, 42, 73]    (spread across all degrees)
    nilp Heis_3    :  [3,  4,  9, 16, 24, 39]    (partial cancellation)

All three give the same Euler characteristic -3, 0, 5, 0, 0, -7
= prod(1-t^n)^3 coefficients.

The sl_2 case is SPECIAL: bar cohomology concentrates at bidegree
(p, w) = (p, p(p+1)/2) with dim 2p+1. The total at weight w is nonzero
only when w is a triangular number, and on the diagonal it equals 2p+1.
This matches the signed Euler series because every bidegree outside the
diagonal is zero.

For semisimple g in general, the Garland-Lepowsky theorem concentrates
the CE cohomology of the loop algebra g_- onto a diagonal indexed by
the AFFINE WEYL GROUP W_aff:

    H^p(g_-, k) = direct sum over w in (W_aff)^{min}_p of weight spaces L(w.0)

where (W_aff)^{min}_p is the set of length-p minimal parabolic coset reps.
The specific bidegrees depend on the full root system, not just dim(g).

For sl_2: W_aff = Z rtimes Z/2, and the minimal reps have length p with
a UNIQUE weight contribution at w = p(p+1)/2, giving the clean
dim H^p_{p(p+1)/2} = 2p+1 formula.

For sl_3: W_aff = affine A_2, the minimal reps give richer bidegrees
(computed in this engine).

For abelian g: there is no Weyl group concentration. The bar complex
is the CE complex of a free graded Lie algebra on d generators at each
mode, and cohomology is LARGE (polynomial growth in weight).

TOPOLOGICAL INTERPRETATION
==========================

For simply-connected compact simple G, Garland-Raghunathan identify:

    H*(B(V_k(g)))_(bigraded) = H*_T(Gr_G)  (T-equivariant cohomology of affine Grassmannian)

At the RATIONAL level, Gr_G has a cell decomposition into affine Schubert
cells indexed by the affine Weyl group. The cell dimensions give the
bigrading.

The EULER CHARACTERISTIC of Gr_G (signed sum) depends only on the
Poincare series of U(g_-) as a graded vector space, which is
H_U(g_-)(t) = prod (1 - t^n)^{-d_g}. Hence chi = prod (1-t^n)^d_g.

But the INDIVIDUAL Betti numbers depend on the root system.

BOTT PERIODICITY
================

For compact simple G, Bott computed the Pontryagin algebra H*(Omega G):

    H*(Omega SU(n+1)) = Z[x_2, x_4, ..., x_{2n}]     (polynomial)
    H*(Omega Sp(n))   = Z[x_2, x_6, x_10, ..., x_{4n-2}]
    H*(Omega Spin(2n+1)) = Z[x_2, x_6, ..., x_{4n-2}] tensor exterior
    H*(Omega Spin(2n))   = similar with one extra generator

These are DIFFERENT polynomial algebras even when dim G is the same.
Example: Spin(8) and Spin(7) have different dims (28, 21) but the
general pattern is: the generators of H*(Omega G) are in degrees
2, 2h_1, 2h_2, ..., 2h_r where h_1 < h_2 < ... < h_r are the exponents
of the Lie algebra plus 1.

Comparison with our bar cohomology:
    sl_2 (rank 1, exponents {1}): H*(Omega SU(2)) = Z[x_2]
        Poincare series = 1/(1-t^2) at degrees 0, 2, 4, 6, ...
        Our bar: dim H^p at weight p(p+1)/2 is 2p+1.
        These are DIFFERENT gradings: topological vs. conformal weight.
        The Euler char of Omega SU(2) in the topological grading is
        sum t^{2k} = 1/(1-t^2), which differs from prod (1-t^n) (our series).

The topological H*(Omega G) uses a different grading and is NOT
the same as our bar cohomology. The confusion between them is AP9
(same-name different-object). The connection is indirect: both encode
the loop Lie algebra g_-, but in different categorical frameworks.

INDIVIDUAL COHOMOLOGY VS EULER SERIES
======================================

Conjecture tested (from the task): dim H^p(g_-)_w = (# partitions of w
with p parts) * (something dim-only)?

FALSE. Counterexample at (p=2, w=3) for dim_g = 3:
    sl_2:          dim H^2_3 = 5
    abelian^3:     dim H^2_3 = 9
    nilp Heis_3:   dim H^2_3 = 7

Partition count p(3, 2) = (1+2) = 1 partition with 2 parts: (1,2).
If the formula held, each algebra would have 1 * (dim-only factor) = c
for the same c. But 5, 9, 7 are DIFFERENT. Refuted.

THE RIGHT FORMULA (Garland-Lepowsky for sl_2)
==============================================

For affine sl_2 specifically:

    H^p(g_-)_w = { (2p+1) if w = p(p+1)/2, 0 otherwise }

This matches our first-principles CE computation exactly. The (2p+1)
is the dimension of the p-th spin irrep of sl_2; it arises because
the minimal coset reps of length p in W_aff(sl_2) act on the weight
lattice to produce a single orbit of size 2p+1.

VERIFICATION PATHS IN THIS ENGINE
=================================

1. Direct CE computation via CECurrentAlgebra (from
   bar_cohomology_dimensions.py) for sl_2, sl_3, abelian, nilpotent.
2. Euler series prediction from prod (1-t^n)^d.
3. Cross-check Euler = signed sum of CE bidegrees.
4. Garland-Lepowsky prediction for sl_2: dim H^p_{p(p+1)/2} = 2p+1.
5. Falsification: abelian vs semisimple at same dim give different
   cohomology dimensions.
6. Bott-Pontryagin comparison for sl_2 vs SU(2) loop space.

References:
    Garland-Lepowsky 1976, "Lie algebra homology and the
        Macdonald-Kac formulas"
    Kumar 2002, "Kac-Moody Groups, their Flag Varieties and
        Representation Theory"
    Bott 1958, "The space of loops on a Lie group"
    compute/lib/bar_cohomology_dimensions.py (CECurrentAlgebra)
    compute/lib/bar_cohomology_non_simply_laced_engine.py (ce_euler_series)
    compute/lib/ce_cohomology_loop.py (sl2/sl3 loop CE reference)
    CLAUDE.md anti-pattern AP9 (same-name different-object)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb
from typing import Dict, List, Optional, Tuple

import numpy as np

from compute.lib.bar_cohomology_dimensions import CECurrentAlgebra, SL3_BRACKET


# ============================================================================
# Lie algebra bracket tables
# ============================================================================


def sl2_bracket() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Structure constants for sl_2 in basis (h=0, e=1, f=2).

    [h,e] = 2e, [h,f] = -2f, [e,f] = h.
    Dim 3, rank 1, h^vee = 2.
    """
    return {
        (0, 1): {1: 2}, (1, 0): {1: -2},
        (0, 2): {2: -2}, (2, 0): {2: 2},
        (1, 2): {0: 1}, (2, 1): {0: -1},
    }


def sl3_bracket() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Return sl_3 structure constants (imported from bar_cohomology_dimensions)."""
    return SL3_BRACKET


def abelian_bracket(dim_g: int) -> Dict[Tuple[int, int], Dict[int, int]]:
    """Structure constants for the abelian Lie algebra of dimension dim_g.

    All brackets vanish. Used as the d-colored free graded Lie algebra
    comparison: the loop CE complex is the d-fold tensor product of
    one-generator CE complexes.
    """
    return {}


def heisenberg3_bracket() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Structure constants for the 3-dim Heisenberg Lie algebra.

    Basis (e1=0, e2=1, e3=2, center). [e1, e2] = e3, all other brackets 0.
    Dim 3, rank 0 (no Cartan), 2-step nilpotent. Note: this is the
    FINITE Heisenberg algebra (Lie), NOT the chiral Heisenberg vertex
    algebra H_k which has a single generator with a double-pole OPE.
    """
    return {
        (0, 1): {2: 1}, (1, 0): {2: -1},
    }


def so4_bracket() -> Dict[Tuple[int, int], Dict[int, int]]:
    """Structure constants for so(4) = sl_2 x sl_2 in block-diagonal form.

    Basis: first sl_2 as (0,1,2), second sl_2 as (3,4,5).
    Dim 6, not simple, two commuting sl_2 summands.
    """
    br = {}
    for i_off, offset in [(0, 0), (1, 3)]:
        h, e, f = offset, offset + 1, offset + 2
        br[(h, e)] = {e: 2}
        br[(e, h)] = {e: -2}
        br[(h, f)] = {f: -2}
        br[(f, h)] = {f: 2}
        br[(e, f)] = {h: 1}
        br[(f, e)] = {h: -1}
    return br


# ============================================================================
# Euler characteristic from the signed product prod (1-t^n)^d
# ============================================================================


@lru_cache(maxsize=256)
def ce_euler_series(max_weight: int, dim_g: int) -> Tuple[int, ...]:
    """Signed CE Euler characteristic coefficients of prod_{n>=1} (1-t^n)^d.

    chi_w = sum_p (-1)^p dim Lambda^p(g_-^*)_w.

    This is the coefficient of t^w in the signed product, and depends
    ONLY on d = dim_g. Returns a tuple of length max_weight+1 with entries
    at weights 0, 1, ..., max_weight.
    """
    coeffs = [0] * (max_weight + 1)
    coeffs[0] = 1
    for n in range(1, max_weight + 1):
        old = list(coeffs)
        for j in range(1, dim_g + 1):
            c_dj = comb(dim_g, j) * ((-1) ** j)
            degree = j * n
            if degree > max_weight:
                break
            for w in range(max_weight + 1):
                if w + degree <= max_weight:
                    coeffs[w + degree] += c_dj * old[w]
    return tuple(coeffs)


def pbw_hilbert_series(max_weight: int, dim_g: int) -> Tuple[int, ...]:
    """Hilbert series of U(g_-) = prod_{n>=1} 1/(1-t^n)^d.

    This is the PBW character of the affine vacuum module with the
    central charge k factored out (the PBW filtration is k-independent).

    Coefficient at weight w = number of d-colored partitions of w.
    """
    coeffs = [0] * (max_weight + 1)
    coeffs[0] = 1
    for n in range(1, max_weight + 1):
        # multiply by 1/(1-t^n)^d = sum_{k>=0} C(k+d-1, d-1) t^{nk}
        new_coeffs = list(coeffs)
        k = 1
        while n * k <= max_weight:
            binom = comb(k + dim_g - 1, dim_g - 1)
            shift = n * k
            for w in range(max_weight + 1 - shift):
                new_coeffs[w + shift] += binom * coeffs[w]
            k += 1
        coeffs = new_coeffs
    return tuple(coeffs)


# ============================================================================
# Garland-Lepowsky formula for sl_2
# ============================================================================


def garland_lepowsky_sl2(max_degree: int = 10) -> Dict[Tuple[int, int], int]:
    """Explicit Garland-Lepowsky bidegree table for sl_2.

    Theorem (Garland-Lepowsky): for g = sl_2 and g_- = sl_2 tensor t^{-1} k[t^{-1}],

        dim H^p(g_-, k)_w = (2p+1) if w = p(p+1)/2, else 0.

    The triangular weight p(p+1)/2 and dimension 2p+1 come from the
    affine Weyl group action: the length-p minimal parabolic coset rep
    in W_aff(sl_2) produces the spin-p irrep of sl_2 at weight p(p+1)/2.

    Returns {(p, w): dim} for p = 0, 1, ..., max_degree.
    """
    table = {}
    for p in range(max_degree + 1):
        w = p * (p + 1) // 2
        dim = 2 * p + 1 if p >= 1 else 1  # H^0 = k at weight 0
        if p == 0:
            table[(0, 0)] = 1
        else:
            table[(p, w)] = dim
    return table


def garland_lepowsky_total_dim_sl2(weight: int) -> int:
    """Total dim of H*(g_-)_{weight} for sl_2 via Garland-Lepowsky.

    Nonzero only at triangular weights w = p(p+1)/2, where dim = 2p+1.
    """
    if weight == 0:
        return 1
    # Find p with p(p+1)/2 = weight
    # p^2 + p - 2w = 0; p = (-1 + sqrt(1 + 8w)) / 2
    disc = 1 + 8 * weight
    sq = int(disc ** 0.5)
    if sq * sq != disc and (sq + 1) * (sq + 1) != disc:
        return 0
    if (sq + 1) * (sq + 1) == disc:
        sq = sq + 1
    if (sq - 1) % 2 != 0:
        return 0
    p = (sq - 1) // 2
    if p * (p + 1) // 2 == weight:
        return 2 * p + 1
    return 0


# ============================================================================
# Bar cohomology dimensions from loop CE
# ============================================================================


def bar_bidegree_table(dim_g: int,
                       bracket: Dict[Tuple[int, int], Dict[int, int]],
                       max_weight: int) -> Dict[Tuple[int, int], int]:
    """Compute the bar cohomology bidegree table from the loop CE complex.

    Returns {(p, w): dim H^p(g_-)_w} for 1 <= w <= max_weight, 1 <= p <= w.

    Wrapper around CECurrentAlgebra for the specific comparison question.
    """
    ce = CECurrentAlgebra(dim_g, bracket, max_weight=max_weight)
    table = {}
    for w in range(1, max_weight + 1):
        for p in range(1, w + 1):
            dim = ce.cohomology_at_weight(p, w)
            if dim > 0:
                table[(p, w)] = int(dim)
    return table


def bar_total_dims(dim_g: int,
                   bracket: Dict[Tuple[int, int], Dict[int, int]],
                   max_weight: int) -> List[int]:
    """Total bar cohomology dim per weight: sum_p dim H^p(g_-)_w.

    Returns list of length max_weight (at weights 1, 2, ..., max_weight).
    """
    ce = CECurrentAlgebra(dim_g, bracket, max_weight=max_weight)
    return [int(ce.bar_cohomology_dim(w)) for w in range(1, max_weight + 1)]


def bar_euler_from_bidegrees(dim_g: int,
                             bracket: Dict[Tuple[int, int], Dict[int, int]],
                             max_weight: int) -> List[int]:
    """Compute the signed Euler char per weight from the bidegree table.

    chi_w = sum_p (-1)^p dim H^p(g_-)_w.

    By Hodge/Euler this should equal coefficient of t^w in prod (1-t^n)^{dim_g}.
    """
    ce = CECurrentAlgebra(dim_g, bracket, max_weight=max_weight)
    out = []
    for w in range(1, max_weight + 1):
        chi = 0
        for p in range(0, w + 1):
            chi += ((-1) ** p) * ce.cohomology_at_weight(p, w)
        out.append(int(chi))
    return out


# ============================================================================
# Bott Pontryagin ring for classical compact simple groups
# ============================================================================


def bott_pontryagin_generators(group_type: str, rank: int) -> List[int]:
    """Degrees of the Pontryagin-ring generators of H*(Omega G; Q).

    Bott's theorem: H*(Omega G; Q) is a (graded-commutative) polynomial
    algebra on generators of degrees 2*e_1, 2*e_2, ..., 2*e_r, where
    e_1 < e_2 < ... < e_r are the EXPONENTS of the finite Lie algebra
    (not affine).

    For A_n (SU(n+1)): exponents {1, 2, ..., n} -> gen degrees {2, 4, ..., 2n}
    For B_n (Spin(2n+1)): exponents {1, 3, 5, ..., 2n-1}
    For C_n (Sp(n)): exponents {1, 3, 5, ..., 2n-1}
    For D_n (Spin(2n)): exponents {1, 3, 5, ..., 2n-3, n-1}
    For G_2: exponents {1, 5}
    For F_4: exponents {1, 5, 7, 11}
    For E_6: exponents {1, 4, 5, 7, 8, 11}
    For E_7: exponents {1, 5, 7, 9, 11, 13, 17}
    For E_8: exponents {1, 7, 11, 13, 17, 19, 23, 29}

    Returns the list [2*e_1, 2*e_2, ..., 2*e_r] of topological degrees.
    """
    if group_type == "A":
        return [2 * k for k in range(1, rank + 1)]
    if group_type == "B":
        return [2 * (2 * k - 1) for k in range(1, rank + 1)]
    if group_type == "C":
        return [2 * (2 * k - 1) for k in range(1, rank + 1)]
    if group_type == "D":
        exps = [2 * k - 1 for k in range(1, rank)] + [rank - 1]
        exps.sort()
        return [2 * e for e in exps]
    if group_type == "G" and rank == 2:
        return [2, 10]
    if group_type == "F" and rank == 4:
        return [2, 10, 14, 22]
    if group_type == "E" and rank == 6:
        return [2, 8, 10, 14, 16, 22]
    if group_type == "E" and rank == 7:
        return [2, 10, 14, 18, 22, 26, 34]
    if group_type == "E" and rank == 8:
        return [2, 14, 22, 26, 34, 38, 46, 58]
    raise ValueError(f"Unknown or unsupported Lie type: {group_type}_{rank}")


def bott_pontryagin_poincare_series(group_type: str, rank: int,
                                    max_degree: int) -> List[int]:
    """Poincare series of H*(Omega G; Q) up to degree max_degree.

    H*(Omega G; Q) is a polynomial ring Q[x_{d_1}, ..., x_{d_r}] in
    even-degree generators. Its Poincare series is

        prod_i 1 / (1 - t^{d_i})

    where d_i are the Bott generator degrees. Returns coefficients
    at t^0, t^1, ..., t^{max_degree}.
    """
    gens = bott_pontryagin_generators(group_type, rank)
    coeffs = [0] * (max_degree + 1)
    coeffs[0] = 1
    for d in gens:
        # multiply by 1 / (1 - t^d)
        new_coeffs = list(coeffs)
        k = 1
        while d * k <= max_degree:
            shift = d * k
            for i in range(max_degree + 1 - shift):
                new_coeffs[i + shift] += coeffs[i]
            k += 1
        coeffs = new_coeffs
    return coeffs


# ============================================================================
# Diagnostic reports
# ============================================================================


def dim_only_falsification(max_weight: int = 6) -> Dict[str, Dict]:
    """Run the critical falsification experiment at dim_g = 3.

    Compare sl_2 (semisimple), abelian^3, and nilp Heis_3 at the same
    dim_g. All three must have identical Euler series prod(1-t^n)^3 but
    different total dimensions per weight.

    Returns a dict with per-algebra data and a pass/fail verdict.
    """
    report = {}

    # Predicted Euler series
    pred = ce_euler_series(max_weight, 3)

    for name, br in [
        ("sl_2", sl2_bracket()),
        ("abelian^3", abelian_bracket(3)),
        ("nilp_Heis_3", heisenberg3_bracket()),
    ]:
        totals = bar_total_dims(3, br, max_weight)
        euler = bar_euler_from_bidegrees(3, br, max_weight)
        report[name] = {
            "totals": totals,
            "euler": euler,
            "euler_matches_prediction": all(
                euler[w - 1] == pred[w] for w in range(1, max_weight + 1)
            ),
        }

    # Verify all give same Euler but different totals
    euler_all_equal = all(
        report["sl_2"]["euler"] == report[k]["euler"]
        for k in report
    )
    totals_different = (
        report["sl_2"]["totals"] != report["abelian^3"]["totals"]
    )

    report["verdict"] = {
        "all_euler_equal": euler_all_equal,
        "totals_differ_across_algebras": totals_different,
        "falsifies_dim_only_claim_for_totals": totals_different,
        "confirms_dim_only_claim_for_euler": euler_all_equal,
        "predicted_euler": list(pred[1:max_weight + 1]),
    }

    return report


def sl2_garland_lepowsky_verification(max_weight: int = 15) -> Dict:
    """Verify the Garland-Lepowsky formula for sl_2.

    Prediction: H^p(g_-)_w = (2p+1) iff w = p(p+1)/2, else 0.

    Compare with direct CE computation. Returns a dict with per-bidegree
    comparison and an overall pass/fail.
    """
    # Largest p to test: p such that p(p+1)/2 <= max_weight
    max_p = int((-1 + (1 + 8 * max_weight) ** 0.5) / 2)

    br = sl2_bracket()
    ce = CECurrentAlgebra(3, br, max_weight=max_weight)

    checks = []
    all_ok = True

    for p in range(1, max_p + 1):
        w_tri = p * (p + 1) // 2
        if w_tri > max_weight:
            break
        predicted = 2 * p + 1
        computed = int(ce.cohomology_at_weight(p, w_tri))
        ok = predicted == computed
        checks.append({
            "p": p,
            "w_triangular": w_tri,
            "predicted_dim": predicted,
            "computed_dim": computed,
            "match": ok,
        })
        if not ok:
            all_ok = False

    # Also check OFF-diagonal vanishing
    off_diag_zeros = 0
    off_diag_nonzeros = 0
    for w in range(1, max_weight + 1):
        for p in range(1, w + 1):
            w_tri = p * (p + 1) // 2
            if w == w_tri:
                continue
            dim = int(ce.cohomology_at_weight(p, w))
            if dim == 0:
                off_diag_zeros += 1
            else:
                off_diag_nonzeros += 1
                all_ok = False

    return {
        "diagonal_checks": checks,
        "off_diagonal_zero_count": off_diag_zeros,
        "off_diagonal_nonzero_count": off_diag_nonzeros,
        "all_checks_pass": all_ok,
    }


def bar_cohomology_comparison_table(dims: List[int], max_weight: int = 5
                                    ) -> Dict[int, Dict]:
    """For each dim in dims, compare semisimple vs abelian vs nilpotent.

    Uses simple-Lie structure constants where available (sl_2 for d=3,
    sl_3 for d=8) and the abelian Lie algebra as a comparison.

    Returns {dim_g: {"algebras": {name: totals}, "euler": list}}.
    """
    result = {}
    for d in dims:
        entry = {"algebras": {}}
        # Always include abelian
        entry["algebras"]["abelian"] = bar_total_dims(
            d, abelian_bracket(d), max_weight)

        # Include semisimple at matching dim if possible
        if d == 3:
            entry["algebras"]["sl_2"] = bar_total_dims(
                3, sl2_bracket(), max_weight)
            entry["algebras"]["nilp_Heis_3"] = bar_total_dims(
                3, heisenberg3_bracket(), max_weight)
        if d == 6:
            entry["algebras"]["so_4"] = bar_total_dims(
                6, so4_bracket(), max_weight)
        if d == 8:
            entry["algebras"]["sl_3"] = bar_total_dims(
                8, sl3_bracket(), max_weight)

        # Predicted Euler series
        pred = ce_euler_series(max_weight, d)
        entry["euler_prediction"] = list(pred[1:max_weight + 1])

        result[d] = entry
    return result


# ============================================================================
# Main diagnostic entry point
# ============================================================================


if __name__ == "__main__":
    print("=" * 72)
    print("BAR COHOMOLOGY AS A FUNCTION OF dim(g): DOES IT TRULY ONLY SEE d?")
    print("=" * 72)

    print("\n1. EULER SERIES (signed): depends only on dim(g) = d")
    print("-" * 72)
    for d in [1, 2, 3, 8]:
        print(f"  d={d}: prod(1-t^n)^{d} at weights 0..10:")
        print(f"    {list(ce_euler_series(10, d))}")

    print("\n2. BIGRADED DIMENSIONS: sl_2 (semisimple) at dim 3")
    print("-" * 72)
    bigrade = bar_bidegree_table(3, sl2_bracket(), 10)
    for (p, w), dim in sorted(bigrade.items()):
        print(f"  (p={p}, w={w}) -> dim {dim}  "
              f"[Garland-Lepowsky: p(p+1)/2 = {p * (p + 1) // 2}]")

    print("\n3. FALSIFICATION: same dim_g = 3, DIFFERENT algebras")
    print("-" * 72)
    report = dim_only_falsification(max_weight=6)
    for name in ["sl_2", "abelian^3", "nilp_Heis_3"]:
        r = report[name]
        print(f"  {name:15s}: totals = {r['totals']}")
        print(f"  {'':15s}  euler  = {r['euler']}")
    print(f"\n  Verdict: {report['verdict']}")

    print("\n4. GARLAND-LEPOWSKY for sl_2, max_weight=15")
    print("-" * 72)
    gl = sl2_garland_lepowsky_verification(15)
    for c in gl["diagonal_checks"]:
        print(f"  p={c['p']:2d}, w={c['w_triangular']:3d}: "
              f"predicted={c['predicted_dim']}, computed={c['computed_dim']}, "
              f"match={c['match']}")
    print(f"\n  off-diagonal zeros: {gl['off_diagonal_zero_count']}")
    print(f"  off-diagonal nonzeros: {gl['off_diagonal_nonzero_count']}")
    print(f"  all checks pass: {gl['all_checks_pass']}")

    print("\n5. BOTT PONTRYAGIN for classical compact groups")
    print("-" * 72)
    for gt, r in [("A", 1), ("A", 2), ("C", 2), ("B", 2), ("G", 2), ("F", 4)]:
        gens = bott_pontryagin_generators(gt, r)
        ps = bott_pontryagin_poincare_series(gt, r, 20)
        print(f"  {gt}_{r}: Pontryagin gens at degrees {gens}")
        print(f"    Poincare series 0..20: {ps}")
