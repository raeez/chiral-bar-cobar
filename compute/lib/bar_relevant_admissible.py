"""Bar-relevant range and admissible-level audit data for simple sl_2 quotients.

Computes:
    1. Bar-relevant range for hat{sl}_2 (strong generators of conformal weight 1)
    2. First null vector weight in vacuum Verma at admissible levels via KK formula
    3. Current audit data for the simple quotient L_k(sl_2) at admissible levels
    4. Numerical verification via Shapovalov determinant computation

Mathematical content:
    For hat{sl}_2 at admissible level k = p/q - 2 (p >= 2, q >= 1, gcd(p,q) = 1):

    (A) BAR-RELEVANT RANGE:
        Strong generators J^+, J^-, J^0 have conformal weight 1.
        Bar degree n >= 2 gives total conformal weight >= 2.
        Bar-relevant range: {h in Z : h >= 2}.

    (B) FIRST NULL VECTOR WEIGHT:
        The Kac-Kazhdan formula for the vacuum Verma M(k*Lambda_0) gives:
        - Positive real root beta_{m,-} = m*delta - alpha at KK value j:
          Condition: m*(k+2) - 1 = j (positive integer), grade = j*m.
          With k+2 = p/q and m = q: j = p-1, grade = (p-1)*q.
        - Positive real root beta_{m,+} = m*delta + alpha at KK value j:
          With m = q: j = p+1, grade = (p+1)*q.

        First null vector: h_null = (p-1)*q  (from beta_{q,-} type root).

        Verification:
          k=0 (p=2,q=1): h_null = 1.  k=1 (p=3,q=1): h_null = 2.
          k=2 (p=4,q=1): h_null = 3.  k=-1/2 (p=3,q=2): h_null = 4.
          k=-4/3 (p=2,q=3): h_null = 3.

    (C) ADMISSIBLE-LEVEL AUDIT STATUS:
        The KK null vector formula gives a concrete obstruction signal in the
        bar-relevant range, but this module does NOT promote a global
        "L_k(sl_2) is chirally Koszul iff ..." theorem for simple admissible
        quotients.

        Instead it records:
        - bar-relevant null-vector data,
        - ordinary-category evidence available in documented cases,
        - a separate obstruction-model verdict, kept distinct from theorem status.

References:
    - Kac, V.G., "Infinite-dimensional Lie algebras" (KK determinant)
    - Kac, V.G. and Wakimoto, M., "Classification of modular invariant
      representations" (admissible level classification)
    - Arakawa, T., "Rationality of admissible affine vertex algebras" (2017)
    - Manuscript: prop:bar-admissible, thm:kw-bar-spectral,
      rem:sl2-admissible, rem:admissible-koszul-status
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Tuple

import numpy as np


# =========================================================================
# Bar-relevant range
# =========================================================================

def bar_relevant_range_sl2() -> Dict:
    """Bar-relevant range for hat{sl}_2.

    Strong generators: J^+, J^-, J^0 of conformal weight 1.
    Bar degree n >= 2 requires n >= 2 inputs of weight 1,
    giving total conformal weight h = n >= 2.

    Returns dict with range description and generator data.
    """
    return {
        'algebra': 'hat{sl}_2',
        'generators': [
            {'name': 'J^+', 'weight': 1},
            {'name': 'J^0', 'weight': 1},
            {'name': 'J^-', 'weight': 1},
        ],
        'bar_relevant_min': 2,
        'bar_relevant_range': 'h >= 2 (h integer)',
        'description': (
            'Bar degree n >= 2 gives conformal weight h = n >= 2. '
            'The bar-relevant range is {h in Z : h >= 2}.'
        ),
    }


# =========================================================================
# First null vector weight (Kac-Kazhdan)
# =========================================================================

@dataclass(frozen=True)
class NullVectorData:
    """Data for the first null vector in the vacuum Verma module."""
    p: int
    q: int
    k: Fraction
    h_null: int              # conformal weight of first null vector
    kk_root_type: str        # which KK root produces the null
    kk_value_j: int          # KK value j
    in_bar_range: bool       # whether h_null >= 2
    sl2_weight: int          # sl_2 weight (h_0 eigenvalue) of the null vector


def first_null_vector_weight_sl2(p: int, q: int) -> NullVectorData:
    """Compute the first null vector weight in the vacuum Verma of hat{sl}_2.

    For hat{sl}_2 at admissible level k = p/q - 2:

    The Kac-Kazhdan determinant for the vacuum Verma M(k*Lambda_0)
    factorizes over positive real roots:

    Type I:  beta_{m,+} = m*delta + alpha  (m >= 0)
      Inner product: <Lambda_0 + rho, beta^v> = m*(k+2) + 1
      KK condition: m*(k+2) + 1 = j (positive integer)
      With k+2 = p/q: j = 1 + m*p/q. Need q | m for j integer.
      Smallest m = q: j = 1 + p, grade = j*m = (1+p)*q.

    Type II: beta_{m,-} = m*delta - alpha  (m >= 1)
      Inner product: <Lambda_0 + rho, beta^v> = m*(k+2) - 1
      KK condition: m*(k+2) - 1 = j (positive integer)
      With k+2 = p/q: j = m*p/q - 1. Need q | m.
      Smallest m = q: j = p - 1, grade = j*m = (p-1)*q.

    Since (p-1)*q < (p+1)*q for p >= 2:
    The first null vector is at grade (p-1)*q, from the Type II root.
    This null has sl_2 weight -2*(p-1) (lowering by the alpha root,
    j = p-1 times).

    Args:
        p: admissible parameter p >= 2
        q: admissible parameter q >= 1, gcd(p,q) = 1

    Returns:
        NullVectorData with all relevant information.
    """
    if p < 2:
        raise ValueError(f"Need p >= 2, got {p}")
    if q < 1:
        raise ValueError(f"Need q >= 1, got {q}")
    if gcd(p, q) != 1:
        raise ValueError(f"Need gcd(p,q) = 1, got gcd({p},{q}) = {gcd(p, q)}")

    k = Fraction(p, q) - 2
    h_null = (p - 1) * q
    j = p - 1

    # The null vector from beta_{q,-} has:
    # Weight Lambda_0 - j*beta_{q,-} = Lambda_0 - (p-1)*(q*delta - alpha)
    # = Lambda_0 - (p-1)*q*delta + (p-1)*alpha
    # sl_2 weight = 0 + 2*(p-1) = 2*(p-1)  (alpha contributes +2 to sl_2 weight)
    # Actually: the null vector has sl_2 weight 2*j = 2*(p-1)
    # (positive because we're adding alpha, not subtracting)
    sl2_weight = 2 * (p - 1)

    return NullVectorData(
        p=p, q=q, k=k,
        h_null=h_null,
        kk_root_type='Type II: beta_{q,-} = q*delta - alpha',
        kk_value_j=j,
        in_bar_range=(h_null >= 2),
        sl2_weight=sl2_weight,
    )


def all_null_vector_grades_sl2(p: int, q: int, max_grade: int) -> List[Tuple[int, str, int]]:
    """List all null vector grades up to max_grade.

    Returns list of (grade, root_type, kk_value_j) triples.
    """
    if gcd(p, q) != 1:
        raise ValueError(f"Need gcd(p,q) = 1")

    nulls = []

    # Type II: beta_{m,-} roots. m = n*q for n >= 1.
    # j = n*p - 1. Grade = j*m = (n*p - 1)*n*q.
    for n in range(1, max_grade + 1):
        m = n * q
        j = n * p - 1
        if j < 1:
            continue
        grade = j * m
        if grade <= max_grade:
            nulls.append((grade, f'Type II: beta_{{m,-}}, m={m}', j))

    # Type I: beta_{m,+} roots. m = n*q for n >= 1.
    # j = n*p + 1. Grade = j*m = (n*p + 1)*n*q.
    for n in range(1, max_grade + 1):
        m = n * q
        j = n * p + 1
        grade = j * m
        if grade <= max_grade:
            nulls.append((grade, f'Type I: beta_{{m,+}}, m={m}', j))

    # Also the trivial null from alpha_1 (m=0): j=1, grade=0
    # Not included since grade 0 is trivial.

    nulls.sort(key=lambda x: x[0])
    return nulls


# =========================================================================
# Koszulness classification
# =========================================================================

@dataclass(frozen=True)
class KoszulnessData:
    """Current audit data for L_k(sl_2) at an admissible level."""
    p: int
    q: int
    k: Fraction
    c: Fraction               # Sugawara central charge
    h_null: int               # first null vector weight
    in_bar_range: bool        # h_null >= 2
    is_integrable: bool       # q == 1
    ordinary_semisimple: bool # ordinary module category semisimple in documented cases
    is_koszul: Optional[bool] # promoted theorem verdict when available
    obstruction_model_verdict: Optional[bool]  # current null-vector model verdict
    theorem_status: str       # current manuscript-facing status tag
    n_admissible_modules: int # |Adm_k| = (p-1)*q
    mechanism: str            # reason for Koszulness or failure


def koszulness_sl2(p: int, q: int) -> KoszulnessData:
    """Collect current audit data for L_k(sl_2) at admissible k = p/q - 2.

    This helper separates:
      - explicit null-vector data in the bar-relevant range,
      - ordinary-module semisimplicity/rationality inputs available in
        documented cases,
      - the current obstruction-model verdict for the simple quotient.

    It deliberately does NOT assert a theorem-level classification of
    chiral Koszulness for all admissible levels.
    """
    if gcd(p, q) != 1:
        raise ValueError(f"Need gcd(p,q) = 1")

    k = Fraction(p, q) - 2
    c = 3 * k / (k + 2)
    h_null = (p - 1) * q
    is_int = (q == 1)
    ordinary_semisimple = is_int or (p, q) == (3, 2)
    n_adm = (p - 1) * q

    if (p, q) == (2, 1):
        theorem_status = 'proved-trivial'
        is_koszul = True
        obstruction_model_verdict = True
        mechanism = (
            'At k = 0 the simple quotient is the trivial algebra '
            'L_0(sl_2) = C, so Koszulness is immediate.'
        )
    elif is_int:
        theorem_status = 'integrable-supported-not-promoted'
        is_koszul = None
        obstruction_model_verdict = None
        mechanism = (
            f'Integrable level k = {p - 2}: the ordinary WZW category is '
            f'semisimple with {p - 1} simples, but this module does not '
            'identify ordinary Ext with the bar-complex Ext groups. '
            'No theorem-level verdict is promoted here.'
        )
    elif (p, q) == (3, 2):
        theorem_status = 'nondegenerate-admissible-live-audit'
        is_koszul = None
        obstruction_model_verdict = False
        mechanism = (
            'At k = -1/2 the reduced associated variety is {0} and the ordinary '
            'admissible category is rational, but the full Artinian Li associated '
            'graded may carry nilpotent bar data. The current obstruction model '
            'flags a non-Koszul signal without promoting a theorem.'
        )
    elif (p, q) == (2, 3):
        theorem_status = 'degenerate-admissible-live-audit'
        is_koszul = None
        obstruction_model_verdict = False
        mechanism = (
            'At k = -4/3 the reduced associated variety is the sl_2 nilcone. '
            'Reduced Poisson cohomology is concentrated, so the remaining issue is '
            'the nilradical of the full non-reduced Li associated graded. The '
            'current obstruction model flags a non-Koszul signal, but the theorem '
            'surface remains open.'
        )
    else:
        theorem_status = 'admissible-live-audit'
        is_koszul = None
        obstruction_model_verdict = False
        mechanism = (
            f'Admissible level k = {k}: the first vacuum null lies at '
            f'h = {h_null}. This gives a bar-relevant obstruction signal, but '
            'the manuscript does not presently promote a global '
            'Koszul/non-Koszul theorem for this simple quotient.'
        )

    return KoszulnessData(
        p=p, q=q, k=k, c=c,
        h_null=h_null,
        in_bar_range=(h_null >= 2),
        is_integrable=is_int,
        ordinary_semisimple=ordinary_semisimple,
        is_koszul=is_koszul,
        obstruction_model_verdict=obstruction_model_verdict,
        theorem_status=theorem_status,
        n_admissible_modules=n_adm,
        mechanism=mechanism,
    )


def koszulness_classification_sl2(
    max_level: float = 5.0,
    max_q: int = 6,
) -> List[KoszulnessData]:
    """Classify Koszulness for all admissible sl_2 levels up to max_level.

    Returns sorted list of KoszulnessData.
    """
    results = []
    for q in range(1, max_q + 1):
        for p in range(2, int(max_level * q) + 3):
            if gcd(p, q) == 1:
                k = Fraction(p, q) - 2
                if float(k) < -2 or float(k) > max_level:
                    continue
                results.append(koszulness_sl2(p, q))
    results.sort(key=lambda x: float(x.k))
    return results


# =========================================================================
# Shapovalov determinant (numerical verification)
# =========================================================================

def _compute_commutator_sl2(t1, m1, t2, m2, k):
    """Commutator [a^{t1}_{m1}, a^{t2}_{m2}] for hat{sl}_2.

    Types: 0=e (J^+), 1=h (J^0), 2=f (J^-).
    Returns list of (coeff, [(type, mode)]) terms.

    Commutation relations:
    [e_m, f_n] = h_{m+n} + m*k*delta_{m+n,0}
    [h_m, e_n] = 2*e_{m+n}
    [h_m, f_n] = -2*f_{m+n}
    [h_m, h_n] = 2*k*m*delta_{m+n,0}
    [e_m, e_n] = 0, [f_m, f_n] = 0
    """
    terms = []
    if t1 == 0 and t2 == 2:
        mn = m1 + m2
        terms.append((1.0, [(1, mn)]))
        if mn == 0:
            terms.append((m1 * k, []))
    elif t1 == 2 and t2 == 0:
        mn = m1 + m2
        terms.append((-1.0, [(1, mn)]))
        if mn == 0:
            terms.append((-m2 * k, []))
    elif t1 == 1 and t2 == 0:
        terms.append((2.0, [(0, m1 + m2)]))
    elif t1 == 0 and t2 == 1:
        terms.append((-2.0, [(0, m1 + m2)]))
    elif t1 == 1 and t2 == 2:
        terms.append((-2.0, [(2, m1 + m2)]))
    elif t1 == 2 and t2 == 1:
        terms.append((2.0, [(2, m1 + m2)]))
    elif t1 == 1 and t2 == 1:
        if m1 + m2 == 0:
            terms.append((2 * k * m1, []))
    return terms


def _normal_order_vev_sl2(ops, k, memo):
    """Compute <0| ops |0> by normal ordering for hat{sl}_2.

    ops: tuple of (type, mode) pairs.
    Zero modes are commuted through (not dropped); they annihilate
    vacuum only at the rightmost position.
    """
    key = ops
    if key in memo:
        return memo[key]
    n = len(ops)
    if n == 0:
        memo[key] = 1.0
        return 1.0
    if ops[-1][1] >= 0:
        memo[key] = 0.0
        return 0.0
    if ops[0][1] <= 0:
        memo[key] = 0.0
        return 0.0
    inv_idx = None
    for i in range(n - 1):
        if ops[i][1] >= 0 and ops[i + 1][1] < 0:
            inv_idx = i
            break
    if inv_idx is None:
        memo[key] = 0.0
        return 0.0
    t1, m1 = ops[inv_idx]
    t2, m2 = ops[inv_idx + 1]
    comm_terms = _compute_commutator_sl2(t1, m1, t2, m2, k)
    result = 0.0
    swapped = ops[:inv_idx] + ((t2, m2), (t1, m1)) + ops[inv_idx + 2:]
    result += _normal_order_vev_sl2(swapped, k, memo)
    for coeff, new_ops_list in comm_terms:
        if len(new_ops_list) == 0:
            reduced = ops[:inv_idx] + ops[inv_idx + 2:]
            result += coeff * _normal_order_vev_sl2(reduced, k, memo)
        else:
            new_t, new_m = new_ops_list[0]
            reduced = ops[:inv_idx] + ((new_t, new_m),) + ops[inv_idx + 2:]
            result += coeff * _normal_order_vev_sl2(reduced, k, memo)
    memo[key] = result
    return result


def _enumerate_pbw_states(grade: int) -> List[tuple]:
    """Enumerate PBW basis states at given grade for hat{sl}_2 vacuum Verma."""
    states: List[tuple] = []

    def generate(remaining, min_pair, current):
        if remaining == 0:
            states.append(tuple(current))
            return
        for m in range(1, remaining + 1):
            for t in range(3):
                pair = (t, m)
                if pair >= min_pair:
                    generate(remaining - m, pair, current + [pair])

    generate(grade, (0, 1), [])
    return states


def shapovalov_null_dimension(k_val: float, grade: int) -> Tuple[int, int, int]:
    """Compute the null space dimension at given grade.

    Returns (n_states, rank, null_dim).
    """
    import sys
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(max(old_limit, 100000))

    sigma_type = {0: 2, 1: 1, 2: 0}
    memo: dict = {}
    states = _enumerate_pbw_states(grade)
    n = len(states)
    S = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            vi = states[i]
            wj = states[j]
            pos_ops = tuple((sigma_type[t], m) for t, m in reversed(vi))
            neg_ops = tuple((t, -m) for t, m in wj)
            all_ops = pos_ops + neg_ops
            S[i, j] = _normal_order_vev_sl2(all_ops, k_val, memo)
    rank = np.linalg.matrix_rank(S, tol=1e-6)
    null_dim = n - rank

    sys.setrecursionlimit(old_limit)
    return n, rank, null_dim


def verify_first_null_weight(p: int, q: int, max_grade: int = 6) -> Dict:
    """Numerically verify the first null vector weight at admissible level.

    Computes the Shapovalov determinant grade by grade and returns the
    first grade where it vanishes.

    WARNING: Expensive for grade > 5 (state count grows rapidly).
    """
    k = float(Fraction(p, q) - 2)
    expected = (p - 1) * q
    found = None

    grades_checked = []
    for g in range(1, min(max_grade, expected + 2) + 1):
        n_states, rank, null_dim = shapovalov_null_dimension(k, g)
        has_null = null_dim > 0
        grades_checked.append({
            'grade': g,
            'n_states': n_states,
            'rank': rank,
            'null_dim': null_dim,
            'has_null': has_null,
        })
        if has_null and found is None:
            found = g

    return {
        'p': p, 'q': q, 'k': k,
        'expected_h_null': expected,
        'found_h_null': found,
        'match': found == expected,
        'grades': grades_checked,
    }


# =========================================================================
# Summary functions
# =========================================================================

def print_classification_table(max_level: float = 4.0, max_q: int = 4):
    """Print the current admissible-level audit table for sl_2."""
    data = koszulness_classification_sl2(max_level, max_q)
    print(f"{'k':>8s}  {'p':>3s}  {'q':>3s}  {'h_null':>6s}  {'c':>8s}  "
          f"{'Theory':>32s}  {'Model':>5s}")
    print("-" * 100)
    for d in data:
        theory = d.theorem_status
        if d.obstruction_model_verdict is True:
            model = "YES"
        elif d.obstruction_model_verdict is False:
            model = "NO"
        else:
            model = "?"
        print(f"  {str(d.k):>6s}  {d.p:3d}  {d.q:3d}  {d.h_null:6d}  "
              f"{float(d.c):8.3f}  {theory:>32s}  {model:>5s}")


# =========================================================================
# Main
# =========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("BAR-RELEVANT RANGE AND SIMPLE-QUOTIENT AUDIT FOR ADMISSIBLE hat{sl}_2")
    print("=" * 70)

    print("\n1. Bar-relevant range:")
    br = bar_relevant_range_sl2()
    print(f"   {br['bar_relevant_range']}")

    print("\n2. First null vector weights:")
    for p, q in [(2, 1), (3, 1), (4, 1), (3, 2), (2, 3), (5, 2), (5, 3)]:
        nv = first_null_vector_weight_sl2(p, q)
        print(f"   k={str(nv.k):>6s} (p={p},q={q}): h_null = {nv.h_null}"
              f"  in_bar = {nv.in_bar_range}")

    print("\n3. Admissible simple-quotient audit table:")
    print_classification_table(4.0, 4)

    print("\n4. Numerical verification (Shapovalov):")
    for p, q in [(3, 1), (4, 1), (3, 2), (2, 3)]:
        result = verify_first_null_weight(p, q, max_grade=5)
        status = "MATCH" if result['match'] else "MISMATCH"
        print(f"   k={result['k']:.4f} (p={p},q={q}): "
              f"expected={result['expected_h_null']}, "
              f"found={result['found_h_null']}  [{status}]")
