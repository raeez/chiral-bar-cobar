#!/usr/bin/env python3
"""Compute bar complex chain dimensions and differentials for chiral algebras.

ESTABLISHED FACTS (kac_moody_framework.tex rem:bar-dims-level-independent):
  For KM algebras: dim B-bar^n(g-hat_k) = dim(g)^n (level-independent)
  The form factor (n-1)! is implicit (one form per ordering).

The bar DIFFERENTIAL D: B-bar^{n+1} -> B-bar^n depends on level k.
At critical level k=-h*, the bar complex reduces to CE(g).

This script computes:
1. Chain group dimensions (proved: dim(g)^n for KM)
2. The bar differential D for sl2-hat at degree 2->1
3. CE complex cohomology (= bar cohomology at critical level)
4. Documents inconsistency with summary table

Usage:
    python3 compute/scripts/compute_bar_complex.py
"""

import json
import sys
from math import factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sympy import Matrix, Rational, Symbol, zeros, binomial

from lib.bar_complex import KNOWN_BAR_DIMS
from lib.lie_algebra import (
    cartan_data, structure_constants_sl2, structure_constants_sl3,
    killing_form_sl2,
)


def sl2_bar_differential_2to1(k):
    """D: B-bar^2 -> B-bar^1 + B-bar^0 for sl2-hat_k.

    B-bar^2 basis: {(a, b) tensor eta_12}, dim = 9.
    Target: B-bar^1 (dim 3) + B-bar^0 (dim 1) = dim 4.

    D(a tensor b tensor eta_12) = [a, b] + k*(a,b)*vacuum
    """
    basis = ["e", "h", "f"]
    sc = structure_constants_sl2()
    kf = killing_form_sl2()
    D = zeros(4, 9)

    for a_idx, a in enumerate(basis):
        for b_idx, b in enumerate(basis):
            col = a_idx * 3 + b_idx
            for c_idx, c in enumerate(basis):
                coeff = sc.get((a, b), {}).get(c, Rational(0))
                if coeff != 0:
                    D[c_idx, col] = coeff
            kf_val = kf.get((a, b), Rational(0))
            if kf_val != 0:
                D[3, col] = k * kf_val
    return D


def chevalley_eilenberg_sl2():
    """Compute CE complex dimensions and cohomology for sl2.

    CE^n(sl2) = Lambda^n(sl2*), dim = C(3, n).
    d: CE^n -> CE^{n+1} is the Lie algebra coboundary.

    At critical level k=-2, bar complex ~ CE complex.
    """
    print("\n--- Chevalley-Eilenberg complex for sl2 ---")
    basis = ["e", "h", "f"]
    sc = structure_constants_sl2()

    # CE^0 = C, CE^1 = sl2* (dim 3), CE^2 = Lambda^2(sl2*) (dim 3), CE^3 = Lambda^3(sl2*) (dim 1)
    ce_dims = [1, 3, 3, 1]
    print(f"  CE dimensions: {ce_dims}")

    # d_0: CE^0 -> CE^1 is zero (invariants)
    # d_1: CE^1 -> CE^2: d(f)(a,b) = -f([a,b])
    # d_2: CE^2 -> CE^3

    # Basis for CE^1: e*, h*, f* (dual to e, h, f)
    # Basis for CE^2: e*^h*, e*^f*, h*^f*

    # d_1(e*)(a, b) = -e*([a,b])
    # d_1(e*)(h, e) = -e*([h,e]) = -e*(2e) = -2
    # d_1(e*)(h, f) = -e*([h,f]) = -e*(-2f) = 0
    # d_1(e*)(e, f) = -e*([e,f]) = -e*(h) = 0
    # So d_1(e*) = -2 h*^e* = 2 e*^h*

    # d_1(h*)(e, f) = -h*([e,f]) = -h*(h) = -1
    # d_1(h*)(h, e) = -h*([h,e]) = -h*(2e) = 0
    # d_1(h*)(h, f) = -h*([h,f]) = -h*(-2f) = 0
    # So d_1(h*) = -1 e*^f* = -e*^f*

    # d_1(f*)(h, f) = -f*([h,f]) = -f*(-2f) = 2
    # d_1(f*)(e, f) = -f*([e,f]) = -f*(h) = 0
    # d_1(f*)(h, e) = -f*([h,e]) = -f*(2e) = 0
    # So d_1(f*) = 2 h*^f*

    # d_1 matrix (rows = CE^2 basis {e*^h*, e*^f*, h*^f*}, cols = CE^1 basis {e*, h*, f*}):
    d1 = Matrix([
        [2, 0, 0],   # e*^h* coefficient
        [0, -1, 0],  # e*^f* coefficient
        [0, 0, 2],   # h*^f* coefficient
    ])
    r1 = d1.rank()
    print(f"  d_1: CE^1 -> CE^2, rank = {r1}")
    print(f"  H^1 = ker(d_1)/im(d_0) = {3 - r1}/{0} = {3 - r1}")

    # d_2: CE^2 -> CE^3
    # CE^3 = Lambda^3(sl2*) = C * (e*^h*^f*), dim 1
    # d_2(e*^h*)(a,b,c) = sum of terms involving brackets
    # By direct computation or the fact that H^2(sl2) = 0 (semisimple):
    # d_2 must be surjective (rank 1) since H^2 = 0.

    # d_2(e*^h*): evaluated on (e,h,f):
    # = e*([h,f])h*(e) - e*([e,f])h*(h) + h*([e,h])e*(f)  (alternating sum)
    # Wait, the CE differential is:
    # d(alpha)(x_0,...,x_n) = sum_{i<j} (-1)^{i+j} alpha([x_i,x_j], x_0,...,x̂_i,...,x̂_j,...,x_n)

    # d_2(e*^h*)(e, h, f):
    # = (-1)^{0+1}(e*^h*)([e,h], f) + (-1)^{0+2}(e*^h*)([e,f], h) + (-1)^{1+2}(e*^h*)([h,f], f)
    # = -(e*^h*)(-2e, f) + (e*^h*)(h, h) - (e*^h*)(-2f, f)
    # = -(−2·e*(−2e)·h*(f) − 0) + ... this is getting complicated.
    # Let me just use that H^2(sl2) = 0 implies rank(d_2) = dim CE^2 - dim ker(d_2)
    # = 3 - (dim H^2 + rank d_1) = 3 - (0 + 3) = 0... that can't be right.
    # H^2 = ker(d_2)/im(d_1). We need rank(d_2) and dim(im(d_1)).
    # rank(d_1) = 3 (full rank since H^1 = 0 for semisimple).
    # Wait: d_1 is 3x3 with rank 3. But that means im(d_1) = CE^2 (all of it).
    # Then H^2 = ker(d_2)/CE^2. Since ker(d_2) ⊆ CE^2 and H^2 = 0,
    # we need ker(d_2) = CE^2, meaning d_2 = 0.
    # Then H^3 = CE^3/im(d_2) = C/0 = C.

    # Check rank of d1:
    # d1 = [[2,0,0],[0,-1,0],[0,0,2]], clearly rank 3.
    print(f"  d_2: CE^2 -> CE^3, rank = 0 (since H^2=0 and im(d_1)=CE^2)")

    print(f"\n  CE cohomology of sl2:")
    print(f"    H^0 = C (dim 1)")
    print(f"    H^1 = 0")
    print(f"    H^2 = 0")
    print(f"    H^3 = C (dim 1, Cartan 3-form)")


def chevalley_eilenberg_sl3():
    """CE complex dimensions and cohomology for sl3."""
    print("\n--- Chevalley-Eilenberg complex for sl3 ---")
    ce_dims = [int(binomial(8, n)) for n in range(9)]
    print(f"  CE dimensions: {ce_dims}")
    print(f"  CE cohomology (by Hopf's theorem):")
    print(f"    H^0 = C, H^3 = C, H^5 = C, H^8 = C (exterior on deg 3,5)")
    print(f"    All others = 0")
    print(f"  (Poincare polynomial: (1+t^3)(1+t^5))")


def chevalley_eilenberg_G2():
    """CE complex dimensions for G2."""
    print("\n--- Chevalley-Eilenberg complex for G2 ---")
    ce_dims = [int(binomial(14, n)) for n in range(15)]
    print(f"  CE dimensions (first 8): {ce_dims[:8]}")
    print(f"  CE cohomology (by Hopf's theorem):")
    print(f"    Exponents of G2: 1, 5")
    print(f"    Poincare polynomial: (1+t^3)(1+t^11)")
    print(f"    H^0 = H^3 = H^11 = H^14 = C, all others = 0")


def investigate_summary_table():
    """Investigate what the summary table values might represent."""
    print("\n" + "=" * 60)
    print("INVESTIGATING SUMMARY TABLE VALUES")
    print("=" * 60)

    # sl2: 3, 6, 15, 36, 91
    # Check various combinatorial formulas
    print("\n--- sl2 table: 3, 6, 15, 36, 91 ---")
    table_sl2 = [3, 6, 15, 36, 91]

    # C(2n+1, 2)
    for n in range(1, 6):
        print(f"  n={n}: C(2n+1,2)={int(binomial(2*n+1, 2))}", end="")
        print(f"  C(n+2,2)={int(binomial(n+2, 2))}", end="")
        print(f"  C(2n,n)={int(binomial(2*n, n))}", end="")
        print(f"  table={table_sl2[n-1]}")

    # Check: are these Hilbert function of some graded ring?
    # 3, 6, 15, 36, 91
    # Differences: 3, 9, 21, 55
    # Second diff: 6, 12, 34
    # Not a polynomial of degree <= 2

    # Try: 3*C(n,1) + something
    # n=1: 3*1 = 3 ✓
    # n=2: 3*2 = 6 ✓
    # n=3: 3*3 = 9 ✗ (need 15)
    # 15 - 9 = 6 at n=3
    # Maybe quadratic: an^2 + bn + c
    # 3 = a + b + c, 6 = 4a + 2b + c, 15 = 9a + 3b + c
    # From first two: 3 = 3a + b -> b = 3 - 3a
    # From first and third: 12 = 8a + 2b = 8a + 2(3-3a) = 2a + 6 -> a = 3
    # b = 3 - 9 = -6, c = 3 - 3 + 6 = 6
    # P(n) = 3n^2 - 6n + 6
    # P(4) = 48 - 24 + 6 = 30 ≠ 36
    # Not quadratic.

    # Try cubic: an^3 + bn^2 + cn + d
    # 3, 6, 15, 36
    # 3 = a + b + c + d
    # 6 = 8a + 4b + 2c + d
    # 15 = 27a + 9b + 3c + d
    # 36 = 64a + 16b + 4c + d
    # From 1,2: 3 = 7a + 3b + c
    # From 2,3: 9 = 19a + 5b + c
    # From 3,4: 21 = 37a + 7b + c
    # From these: 6 = 12a + 2b -> b = 3 - 6a
    # 12 = 18a + 2b = 18a + 6 - 12a = 6a + 6 -> a = 1
    # b = 3 - 6 = -3
    # c = 3 - 7 + 9 = 5 ... wait: c = 3 - 7(1) - 3(-3) = 3 - 7 + 9 = 5
    # d = 3 - 1 + 3 - 5 = 0
    # P(n) = n^3 - 3n^2 + 5n
    # P(1) = 1 - 3 + 5 = 3 ✓
    # P(2) = 8 - 12 + 10 = 6 ✓
    # P(3) = 27 - 27 + 15 = 15 ✓
    # P(4) = 64 - 48 + 20 = 36 ✓
    # P(5) = 125 - 75 + 25 = 75 ≠ 91

    print(f"\n  Fit cubic: P(n) = n^3 - 3n^2 + 5n")
    for n in range(1, 7):
        val = n**3 - 3*n**2 + 5*n
        print(f"    P({n}) = {val}", end="")
        if n <= 5:
            print(f"  table = {table_sl2[n-1]}", end="")
            print(f"  {'✓' if val == table_sl2[n-1] else '✗'}")
        else:
            print()

    # Matches degrees 1-4 but not 5. So not a polynomial.

    # Try: C(2n, n) / (n+1) * 3 = 3 * Catalan?
    # Catalan: 1, 2, 5, 14, 42. 3*Cat: 3, 6, 15, 42, 126. Matches 1-3 but 42≠36.

    # Try Motzkin-like: M(n) with 3 colors?
    # Motzkin paths with 3 types of horizontal steps: this is a known sequence.
    # Trinomial triangle central elements? T(n,0) for T = (1+x+x^2)^n
    # T(1,0)=1, T(2,0)=3, T(3,0)=7, T(4,0)=19... no.

    # Actually: 3, 6, 15, 36, 91
    # = C(3,1), C(4,2), C(6,2), C(9,2), C(14,2)
    # 3, 6, 15, 36, 91 -- check if 91 = C(14,2) = 91 ✓
    # Hmm: C(3,1)=3, C(4,2)=6, C(6,2)=15, C(9,2)=36, C(14,2)=91
    # The top values: 3, 4, 6, 9, 14
    # Differences: 1, 2, 3, 5 -- Fibonacci!!
    # 3, 3+1=4, 4+2=6, 6+3=9, 9+5=14 -- partial sums of Fibonacci!

    print(f"\n  Checking C(a_n, 2) structure:")
    a = [3, 4, 6, 9, 14]
    for i, ai in enumerate(a):
        val = int(binomial(ai, 2)) if ai >= 2 else ai
        if ai < 2:
            val = ai
        actual = [3, 6, 15, 36, 91][i]
        # For a_0=3: C(3,2)=3? No, C(3,1)=3. Hmm.
        # Actually 3 = C(3,1), 6 = C(4,2), 15 = C(6,2), 36 = C(9,2), 91 = C(14,2)
        # But C(3,1) ≠ C(3,2)=3 -- actually both equal 3.
        print(f"    C({ai}, 2) = {int(binomial(ai, 2))}  (table: {actual})")

    # Interesting! The table values ARE C(a_n, 2) where a_n = 3,4,6,9,14.
    # But this doesn't obviously arise from any standard construction.

    # Let me check sl3: 8, 36, 204
    print(f"\n--- sl3 table: 8, 36, 204 ---")
    # 36 = C(9, 2) = 36. 204 = ?
    # C(9,2) = 36 ✓. C(?, ?) = 204?
    # 204 = C(204/17...) = 12*17 = 204. C(17,2) = 136. C(9,3) = 84. C(12,3)=220.
    # None obvious.
    # S^2(sl3) = C(8+1, 2) = 36 ✓
    # S^3(sl3) = C(8+2, 3) = C(10,3) = 120 ≠ 204
    # Lambda^2(sl3) = C(8,2) = 28 ≠ 36
    # sl3 x sl3 / something = 64 / ? = 36 means quotient by 28-dim subspace
    # 64 - 28 = 36. And Lambda^2(sl3) = 28. So 36 = S^2(sl3) = 64 - 28 = 36.
    print(f"  S^2(sl3) = C(9,2) = {int(binomial(9, 2))}  (table: 36) ✓")
    print(f"  S^3(sl3) = C(10,3) = {int(binomial(10, 3))}  (table: 204) ✗")

    # Hmm, 204 = 8*8*8 * 2 / ... = 1024/5.02... not clean.
    # Or: number of degree-3 monomials in 8 variables allowing repeats
    # with some weight constraint?

    # Let me check if 204 = C(8,3) + something * C(8,2) + ...
    # C(8,3) = 56, 204 - 56 = 148. Not obvious.

    # Wait: for sl3, the bar complex involves the Serre relations.
    # The degree-3 bar has 8^3=512 ordered triples x 2 forms = 1024.
    # Modulo the Serre relations... let me think about what quotient gives 204.
    # 1024 / 5.02 ≈ 204. Not a clean ratio.

    # Actually: dim of the SECOND exterior power:
    # For a Lie algebra of dim n: Lambda^2 has dim C(n,2)
    # For sl3: C(8,2)=28
    # Lambda^3 = C(8,3) = 56
    # S^2 = C(9,2) = 36
    # S^3 = C(10,3) = 120
    # S^2 * (n-1)! = 36 * 1 = 36
    # S^3 * (n-1)! = 120 * 2 = 240. Close to 204 but not equal.

    # Let me try: Lambda^d(g) * (d-1)!
    # d=2: C(8,2)*1 = 28 ≠ 36
    # d=3: C(8,3)*2 = 112 ≠ 204

    # S^d(g) + Lambda^d(g)?
    # d=2: 36 + 28 = 64 = 8^2 (full tensor!) ≠ 36
    # d=3: 120 + 56 = 176 ≠ 204

    # S^d(g) + (d-1)*Lambda^d(g)?
    # d=2: 36 + 28 = 64 ≠ 36
    # d=3: 120 + 2*56 = 232 ≠ 204

    # What about: elements in g^tensor_d modulo the "antisymmetric" part wrt Arnold?
    # For d=2: g^2 / Lambda^2 = S^2 = 36. Matches!
    # For d=3: the Arnold algebra at 3 points has the OS relations.
    # g^3 tensor Omega^2(Conf_3) / Arnold = some quotient.

    # This might be the key: the numbers in the table are NOT dim(g)^n but
    # the dimension of g^n tensored with H^{n-1}(Conf_n) and then QUOTIENTED
    # by something (or it's the symmetric/coinvariant quotient).

    # For d=2, dim = 1 form. The quotient of g^2 by the antisymmetric part
    # (which is the Lie bracket kernel) gives S^2(g) with dim C(d_g+1, 2).
    # For sl3: C(9,2) = 36. ✓

    # For the bar complex of a chirLie (Kac-Moody), the cofree coalgebra
    # is the cocommutative cofree coalgebra, which is S*(g).
    # At degree d: S^d(g) with dim C(d_g + d - 1, d).
    # sl2: C(d+2, d) = C(d+2, 2): 3, 6, 10, 15, 21.
    # sl3: C(d+7, d): 8, 36, 120, 330, 792.
    # These match d=1,2 for both but diverge at d=3.

    # For d=3 sl3: C(10,3) = 120 ≠ 204. So it's NOT simply S^d(g).

    # The number 204: let me check 204 = 8 + 8*8 + (8*7/2)*2
    # = 8 + 64 + 56 = 128. No.
    # 204 = 8*8*8/... no.
    # 204 = 4 * 51 = 4 * 3 * 17. Not obviously related to dim(sl3)=8.

    # Let me check: 204 / 2 = 102. Is this related to dim forms * something?
    # At d=3, forms have dim 2.

    # ALTERNATIVE HYPOTHESIS: The summary table may have been generated
    # with WRONG formulas during an AI session. Given that:
    # - The proved formula is dim = dim(g)^n (from the KM chapter)
    # - The table values don't match ANY standard combinatorial formula at d>=3
    # - The values DO match S^d(g) at d=1,2 which is suggestive
    # The most likely explanation is an error in the table.

    print(f"\n--- CONCLUSION ---")
    print(f"The summary table values in examples_summary.tex appear to be")
    print(f"INCONSISTENT with the proved chain dimensions dim(g)^n.")
    print(f"")
    print(f"At degree 1: table matches dim(g) for all algebras.")
    print(f"At degree 2: table matches S^2(g) = C(dim_g+1, 2).")
    print(f"At degree 3+: table values don't match any standard formula.")
    print(f"")
    print(f"The proved formula (rem:bar-dims-level-independent) says")
    print(f"dim B-bar^n = dim(g)^n, with forms implicit (absorbed into")
    print(f"the notation). This matches detailed_computations.tex.")
    print(f"")
    print(f"RECOMMENDATION: Flag the summary table for correction.")
    print(f"The correct chain dimensions for KM algebras are dim(g)^n")
    print(f"(or dim(g)^n * (n-1)! if counting with the form space).")


def compute_chain_dims():
    """Display proved chain group dimensions."""
    print("=" * 60)
    print("BAR COMPLEX CHAIN GROUP DIMENSIONS")
    print("=" * 60)

    algebras = [
        ("sl2 (A1)", 3, 5),
        ("sl3 (A2)", 8, 5),
        ("G2", 14, 4),
        ("so5 (B2)", 10, 4),
    ]

    for name, dim_g, max_deg in algebras:
        dims = {n: dim_g**n for n in range(1, max_deg + 1)}
        print(f"\n  {name} (dim g = {dim_g}): {dims}")

    print(f"\n  DISCREPANCY with summary table:")
    for alg_key, dim_g in [("sl2", 3), ("sl3", 8)]:
        known = KNOWN_BAR_DIMS.get(alg_key, {})
        proved = {n: dim_g**n for n in range(1, 6)}
        print(f"    {alg_key} proved: {proved}")
        print(f"    {alg_key} table:  {known}")


def main():
    compute_chain_dims()
    chevalley_eilenberg_sl2()
    chevalley_eilenberg_sl3()
    chevalley_eilenberg_G2()
    investigate_summary_table()

    # Compute D21 for sl2 to verify the bar differential structure
    print(f"\n{'='*60}")
    print("sl2 BAR DIFFERENTIAL D: B-bar^2 -> B-bar^1 + B-bar^0")
    print("="*60)
    k = Symbol("k")
    D21 = sl2_bar_differential_2to1(k)
    print(f"Matrix ({D21.rows} x {D21.cols}):")
    basis = ["e", "h", "f"]
    print("Columns: ", end="")
    for a in basis:
        for b in basis:
            print(f"{a}{b} ", end="")
    print()
    print("Rows: e, h, f, vac")
    for i in range(D21.rows):
        row_label = basis[i] if i < 3 else "vac"
        print(f"  {row_label}: [{', '.join(str(D21[i,j]) for j in range(D21.cols))}]")

    # Key checks
    print(f"\n  At k=1: rank = {D21.subs(k, 1).rank()}")
    print(f"  At k=-2 (critical): rank = {D21.subs(k, -2).rank()}")
    print(f"  At k=0: rank = {D21.subs(k, 0).rank()}")

    # D21 restricted to Lie bracket part (rows 0-2)
    D_lie = D21[:3, :]
    print(f"\n  Lie bracket part (k-independent): rank = {D_lie.rank()}")
    print(f"  This is the CE^1 -> CE^2 dual; rank 3 = dim sl2 confirms surjectivity.")

    # Save results
    results = {
        "chain_dims_KM": {
            "formula": "dim(g)^n for KM algebras",
            "sl2": {str(n): 3**n for n in range(1, 6)},
            "sl3": {str(n): 8**n for n in range(1, 6)},
            "G2": {str(n): 14**n for n in range(1, 5)},
        },
        "summary_table_INCONSISTENT": {
            "sl2": dict(KNOWN_BAR_DIMS.get("sl2", {})),
            "sl3": dict(KNOWN_BAR_DIMS.get("sl3", {})),
        },
        "CE_cohomology": {
            "sl2": "H^0=1, H^1=0, H^2=0, H^3=1",
            "sl3": "H^0=1, H^3=1, H^5=1, H^8=1",
            "G2": "H^0=1, H^3=1, H^11=1, H^14=1",
        },
        "G2_bar_deg1": 14,  # = dim(G2) -- answering queue C-001
    }

    out_path = Path(__file__).resolve().parents[1] / "results" / "bar_dims.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults written to {out_path}")


if __name__ == "__main__":
    main()
