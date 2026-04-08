r"""SFT bar complex comparison engine: E_1 structure and chiral bar dictionary.

MATHEMATICAL FRAMEWORK
======================

This module implements the precise comparison between the bar complex of an
A-infinity algebra (as it appears in open string field theory) and the chiral
bar complex of Vol I/II.  The central question: does the bar coalgebra carry
E_1 structure, and what does the coproduct encode physically?

EIGHT COMPUTATIONAL SECTORS:

1. BAR COALGEBRA AS E_1-COALGEBRA:
   For an A-infinity algebra A, B(A) = T^c(s^{-1} A_+) is the cofree
   conilpotent coalgebra on the desuspension of the augmentation ideal.
   The coproduct is DECONCATENATION:

       Delta([a_1|...|a_n]) = sum_{i=0}^{n} [a_1|...|a_i] otimes [a_{i+1}|...|a_n]

   This is the cofree COASSOCIATIVE (= E_1-coalgebra = Ass^c-coalgebra)
   coproduct.  The bar differential d_B is a CODERIVATION with respect
   to Delta.  Together (B(A), d_B, Delta) is a dg Ass^c-coalgebra.

   KEY POINT: The E_1 coalgebra structure is ALWAYS present on the bar
   complex of any A-infinity algebra.  It is NOT extra structure; it is
   the cofree coalgebra structure on the tensor coalgebra.  The A-infinity
   structure on A is EQUIVALENT to a coderivation d on T^c(s^{-1}A_+)
   with d^2 = 0 (Stasheff's theorem).

2. PHYSICAL INTERPRETATION IN OPEN SFT:
   In Witten's open SFT on C x R:
       - The bar differential d_B = BRST operator Q (from holomorphic
         collisions on FM_k(C), the C-direction)
       - The bar coproduct Delta = string SPLITTING (ordered cutting of
         the worldline on Conf_k(R), the R-direction)
       - Higher A-infinity operations m_n encode higher open SFT vertices

   The deconcatenation coproduct has a PHYSICAL meaning: it encodes how
   an open string state (a word in the boundary operators) can be CUT
   into two subwords at any position.  The ordered nature (E_1, not
   E_infinity) reflects the fact that open strings have ENDPOINTS with
   a canonical ordering.

3. CHIRAL BAR COMPLEX COMPARISON (Vol I/II):
   In the chiral bar complex B^ch(A) of Vol I:
       - The bar differential d_B encodes OPE residues on FM_k(C)
         (holomorphic collisions, the C-direction factorization)
       - The coproduct Delta encodes deconcatenation on Conf_k(R)
         (topological splitting, the R-direction factorization)

   The identification: B^ch(A) is a dg factorization COALGEBRA on Ran(X).
   The coalgebra structure is the deconcatenation coproduct (thm:bar-coalgebra,
   cor:bar-is-dgcoalg in bar_construction.tex).  The differential is a
   coderivation (thm:diff-is-coderivation).

   THIS IS THE SAME STRUCTURE as the SFT bar complex.  The chiral bar
   complex of a chiral algebra A on a curve X carries:
       - E_1 coalgebra structure from deconcatenation (the R-direction)
       - dg structure from OPE residues (the C-direction)
   Together: a dg E_1-coalgebra = dg Ass^c-coalgebra.

4. E_1 vs E_infinity ON THE BAR COMPLEX:
   For an E_infinity-chiral algebra (= vertex algebra, all standard families),
   the bar complex carries MORE than E_1 structure:

   (a) The ORDERED bar B^{ord}(A) on ordered configurations has the
       E_1 coproduct (deconcatenation).  This is ALWAYS present.

   (b) The SYMMETRIC bar B^{Sigma}(A) on Sigma_n-coinvariants has a
       cocommutative coproduct.  This exists only for E_infinity algebras.

   (c) The descent B^{ord} -> B^{Sigma} is R-matrix twisted (AP38 of Vol II):
       B^{Sigma}_n = (B^{ord}_n)^{R-Sigma_n}

   For genuinely E_1 algebras (quantum vertex algebras), only B^{ord}
   exists.  The coproduct is E_1 (coassociative, NOT cocommutative).

   CRITICAL (AP35/AP46 of Vol II): ALL vertex algebras (Heisenberg,
   Kac-Moody, Virasoro, W_N) are E_infinity-chiral.  "E_infinity" means
   LOCAL, not "pole-free."  The E_1 structure on the bar complex is the
   RESTRICTION of the E_infinity structure to ordered configurations.

5. KAJIURA-STASHEFF OCHA:
   For open-closed SFT, Kajiura-Stasheff (2006) define the open-closed
   homotopy algebra (OCHA): a pair (H_c, H_o) where H_c carries L_infinity
   (closed strings) and H_o carries A_infinity (open strings), coupled by
   open-closed operations.  The bar construction of the OCHA is a
   TWO-COLOURED coalgebra:
       B(H_c, H_o) = (B^{Lie}(H_c), B^{Ass}(H_o))
   with the Lie-bar carrying E_infinity coalgebra structure (cocommutative)
   and the Ass-bar carrying E_1 coalgebra structure (coassociative).

   This matches Vol II's Swiss-cheese picture: the closed colour has
   E_infinity operations on FM_k(C) (symmetric), and the open colour
   has E_1 operations on Conf_k(R) (ordered).

6. KONTSEVICH-SOIBELMAN NC GEOMETRY:
   Kontsevich-Soibelman interpret B(A) = T^c(s^{-1}A_+) as the
   "algebra of functions on the formal pointed dg-manifold" dual to A.
   The coproduct Delta is the comultiplication of the coordinate ring
   of a formal NC scheme.  More precisely:

   - The cofree coalgebra T^c(V) = bigoplus_n V^{otimes n} with
     deconcatenation coproduct is the "completed tensor algebra" dual
     to the free algebra T(V*).
   - A coderivation d on T^c(V) with d^2 = 0 is a "homological
     vector field" Q on the formal NC manifold.
   - The MC equation on A corresponds to finding a "point" on this
     formal manifold.

   In the chiral context: the formal NC manifold is the moduli space
   of flat connections (twisting morphisms) on Ran(X).  The bar-cobar
   adjunction Tw(C, A) = Hom(Omega(C), A) = Hom(C, B(A)) identifies
   twisting morphisms with coalgebra maps into B(A).

7. DECONCATENATION COPRODUCT COMPUTATION:
   Explicit computation of the deconcatenation coproduct at low arities,
   for the exterior algebra Wedge*(C^d) (CY brane) and the polynomial
   algebra (Chan-Paton factor).

   For gl_N Chan-Paton: A = gl_N as an associative algebra (concentrated
   in degree 0).  The bar complex B(gl_N) = T^c(s^{-1} gl_N).
   The bar differential comes from the matrix product.
   The bar cohomology H*(B(gl_N)) recovers the Koszul dual coalgebra.
   For gl_N: the Koszul dual is the exterior coalgebra Wedge^c(gl_N*[-1])
   (since Sym^! = Wedge in the ungraded case, but gl_N is not commutative,
   so Ass^!(gl_N) needs the full bar resolution).

8. COMPARISON TABLE:
   ==========================================
   | Structure     | Open SFT       | Chiral bar    |
   |---------------|----------------|---------------|
   | State space   | Fock space     | A (chiral alg)|
   | Differential  | BRST Q         | d_B (OPE res) |
   | Coproduct     | string split   | deconcatenation|
   | Higher ops    | V_n vertices   | m_n A-infinity |
   | MC equation   | EOM Q+**=0     | d+[,]=0       |
   | Coalgebra     | E_1 (Ass^c)   | E_1 (Ass^c)  |
   | Genus-0       | tree-level     | genus-0 bar   |
   | Genus-g       | g-loop         | curved bar    |
   | Curvature     | tadpole        | kappa*omega_g |
   ==========================================

Anti-patterns guarded against:
    AP19: bar propagator d log(z-w) absorbs one pole order from OPE
    AP25: B(A) != Omega(B(A)) != D_Ran(B(A)) -- three functors
    AP34: bar-cobar inversion recovers A, NOT the bulk
    AP45: desuspension s^{-1} LOWERS degree by 1
    AP-OC (Vol II): bar classifies twisting morphisms, NOT bulk observables
    AP35-AP55 (Vol II): E_infinity = local = ALL vertex algebras

References:
    Stasheff, "Homotopy associativity of H-spaces I,II" (1963)
    Witten, "Noncommutative geometry and string field theory" (1986)
    Zwiebach, "Closed string field theory: quantum action..." (1993)
    Kajiura-Stasheff, "Homotopy algebras inspired by OCSFT" (2006)
    Kontsevich-Soibelman, "Notes on A-infinity..." (2006)
    Loday-Vallette, "Algebraic Operads" (2012), Ch. 2, 9, 11
    Vol I: thm:bar-coalgebra, cor:bar-is-dgcoalg, thm:diff-is-coderivation
    Vol I: thm:bar-modular-operad, thm:mc2-bar-intrinsic
    Vol II: SC^{ch,top} Swiss-cheese structure
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from itertools import product as iter_product
from typing import Any, Dict, FrozenSet, List, Optional, Tuple


# =========================================================================
# 1. Deconcatenation coproduct on the tensor coalgebra
# =========================================================================

def deconcatenation_coproduct(word: Tuple[str, ...]) -> List[Tuple[Tuple[str, ...], Tuple[str, ...]]]:
    """Compute the deconcatenation coproduct Delta on a bar element.

    For a word [a_1|...|a_n] in the bar complex (= tensor coalgebra),
    the deconcatenation coproduct is:

        Delta([a_1|...|a_n]) = sum_{i=0}^{n} [a_1|...|a_i] otimes [a_{i+1}|...|a_n]

    where the i=0 term gives () otimes [a_1|...|a_n] (counit on left)
    and the i=n term gives [a_1|...|a_n] otimes () (counit on right).

    Returns list of (left_tensor, right_tensor) pairs.
    Each pair represents one summand of the coproduct.

    Convention: the empty tuple () represents the counit (ground field element).
    """
    n = len(word)
    result = []
    for i in range(n + 1):
        left = word[:i]
        right = word[i:]
        result.append((left, right))
    return result


def reduced_coproduct(word: Tuple[str, ...]) -> List[Tuple[Tuple[str, ...], Tuple[str, ...]]]:
    r"""Compute the REDUCED deconcatenation coproduct.

    The reduced coproduct bar{Delta} omits the counit terms:
        bar{Delta}([a_1|...|a_n]) = sum_{i=1}^{n-1} [a_1|...|a_i] otimes [a_{i+1}|...|a_n]

    This is the coproduct used in the conilpotent filtration.
    For arity 1: bar{Delta} = 0 (the generators are primitive).
    """
    n = len(word)
    result = []
    for i in range(1, n):
        left = word[:i]
        right = word[i:]
        result.append((left, right))
    return result


def iterated_coproduct(word: Tuple[str, ...], depth: int) -> List[Tuple[Tuple[str, ...], ...]]:
    """Compute the iterated coproduct Delta^{(depth)}.

    Delta^{(1)} = Delta (the coproduct itself).
    Delta^{(k)} = (Delta otimes id^{otimes(k-1)}) circ Delta^{(k-1)}.

    Returns list of tuples of words (one tuple per summand).
    Each tuple has (depth+1) entries.

    For a word of length n, the iterated coproduct at depth k gives
    all ordered partitions of [a_1,...,a_n] into (k+1) consecutive blocks.
    """
    if depth == 0:
        return [(word,)]
    if depth == 1:
        return [(left, right) for left, right in deconcatenation_coproduct(word)]

    # Recursive: apply Delta to the first tensor factor of each term
    prev = iterated_coproduct(word, depth - 1)
    result = []
    for summand in prev:
        first_factor = summand[0]
        rest = summand[1:]
        for left, right in deconcatenation_coproduct(first_factor):
            result.append((left, right) + rest)
    return result


def verify_coassociativity(word: Tuple[str, ...]) -> Dict[str, Any]:
    """Verify (Delta otimes id) circ Delta = (id otimes Delta) circ Delta.

    This is the defining axiom of a coalgebra (coassociativity).
    For the deconcatenation coproduct, this is always true because
    both sides enumerate ordered tripartitions of the word.

    Returns verification data including both sides and whether they match.
    """
    n = len(word)

    # Left side: (Delta otimes id) circ Delta
    # First apply Delta, then apply Delta to the left factor
    left_side = []
    for l, r in deconcatenation_coproduct(word):
        for ll, lr in deconcatenation_coproduct(l):
            left_side.append((ll, lr, r))

    # Right side: (id otimes Delta) circ Delta
    # First apply Delta, then apply Delta to the right factor
    right_side = []
    for l, r in deconcatenation_coproduct(word):
        for rl, rr in deconcatenation_coproduct(r):
            right_side.append((l, rl, rr))

    # Sort for comparison (both should enumerate all ordered tripartitions)
    left_sorted = sorted(left_side)
    right_sorted = sorted(right_side)

    return {
        "word": word,
        "length": n,
        "left_side_count": len(left_side),
        "right_side_count": len(right_side),
        "coassociative": left_sorted == right_sorted,
        # Number of tripartitions should be binom(n+2, 2)
        "expected_count": math.comb(n + 2, 2),
        "actual_count": len(left_side),
    }


def verify_counit(word: Tuple[str, ...]) -> Dict[str, Any]:
    """Verify the counit axiom: (epsilon otimes id) circ Delta = id = (id otimes epsilon) circ Delta.

    The counit epsilon: T^c(V) -> k sends non-empty words to 0 and () to 1.
    The left counit axiom says: summing (epsilon(left) * right) = word.
    This holds because only the i=0 term survives (left = (), epsilon(()) = 1).
    """
    # (epsilon otimes id) circ Delta
    left_counit_result = []
    for left, right in deconcatenation_coproduct(word):
        if len(left) == 0:
            left_counit_result.append(right)

    # (id otimes epsilon) circ Delta
    right_counit_result = []
    for left, right in deconcatenation_coproduct(word):
        if len(right) == 0:
            right_counit_result.append(left)

    return {
        "word": word,
        "left_counit_gives_word": left_counit_result == [word],
        "right_counit_gives_word": right_counit_result == [word],
        "counit_axiom": (left_counit_result == [word] and right_counit_result == [word]),
    }


# =========================================================================
# 2. Conilpotent filtration
# =========================================================================

def conilpotent_filtration_level(word: Tuple[str, ...]) -> int:
    """The conilpotent filtration level of a bar element.

    F^n(T^c(V)) = bigoplus_{k <= n} V^{otimes k}.

    A word of length n has filtration level n.
    The reduced coproduct lowers filtration level in each tensor factor.
    The coradical (F^0 = k, F^1 = k oplus V) consists of scalars and
    generators.  Generators are PRIMITIVE: bar{Delta}(v) = 0.

    For the bar complex: bar elements of arity n have filtration n.
    The conilpotent condition means iterated reduced coproducts
    eventually reach zero.  For a length-n word, bar{Delta}^{(n)} = 0.
    """
    return len(word)


def verify_conilpotence(word: Tuple[str, ...]) -> Dict[str, Any]:
    """Verify that iterated reduced coproducts eventually vanish.

    For a word of length n, the (n-1)-fold iterated reduced coproduct
    produces terms of the form (a_1) otimes ... otimes (a_n) (all singletons).
    The n-fold iterated reduced coproduct is zero because at least one
    factor must be empty.

    This is the conilpotence property of the bar coalgebra.
    """
    n = len(word)
    current_terms = [(word,)]

    levels = {}
    for depth in range(1, n + 2):
        new_terms = []
        for summand in current_terms:
            # Apply reduced coproduct to the FIRST factor
            first = summand[0]
            rest = summand[1:]
            red = reduced_coproduct(first)
            if red:
                for left, right in red:
                    new_terms.append((left, right) + rest)
        levels[depth] = len(new_terms)
        current_terms = new_terms
        if not current_terms:
            break

    vanishes_at = min((d for d, c in levels.items() if c == 0), default=None)

    return {
        "word": word,
        "length": n,
        "levels": levels,
        "vanishes_at_depth": vanishes_at,
        "conilpotent": vanishes_at is not None,
        "expected_vanish_depth": n,  # should vanish at exactly depth n
    }


# =========================================================================
# 3. Coderivation property of the bar differential
# =========================================================================

def bar_differential_gl_n(word: Tuple[str, ...],
                          mult_table: Dict[Tuple[str, str], Dict[str, int]]
                          ) -> Dict[Tuple[str, ...], int]:
    """Apply the bar differential to a word in B(gl_N).

    The bar differential for an associative algebra A is:
        d([a_1|...|a_n]) = sum_{i=1}^{n-1} (-1)^{eps_i} [a_1|...|a_i * a_{i+1}|...|a_n]

    where eps_i encodes the Koszul sign from the desuspension.

    For an algebra concentrated in degree 0 (like gl_N):
        |s^{-1}a_j| = |a_j| - 1 = -1

    So eps_i = sum_{j=0}^{i} (|a_j| - 1) = sum_{j=0}^{i} (-1) = -(i+1).
    Sign = (-1)^{-(i+1)} = (-1)^{i+1}.

    Actually, let us use the standard convention from Loday-Vallette (2012),
    Prop 2.2.2: the bar differential b_2 on desuspended elements satisfies
        b([s^{-1}a_1|...|s^{-1}a_n]) = sum_{i=1}^{n-1}
          (-1)^{sum_{j=1}^{i} |s^{-1}a_j|} [s^{-1}a_1|...|s^{-1}(a_i*a_{i+1})|...|s^{-1}a_n]

    For all |a_j| = 0: |s^{-1}a_j| = -1, so
        sum_{j=1}^{i} |s^{-1}a_j| = -i
    and the sign is (-1)^{-i} = (-1)^i.

    mult_table: {(a, b): {c: coefficient}} for a*b = sum coeff*c.
    Returns: {resulting_word: coefficient}.
    """
    n = len(word)
    result: Dict[Tuple[str, ...], int] = defaultdict(int)

    for i in range(n - 1):
        # Multiply word[i] and word[i+1]
        pair = (word[i], word[i + 1])
        if pair not in mult_table:
            continue
        products = mult_table[pair]

        # Koszul sign: (-1)^i for degree-0 generators
        sign = (-1) ** i

        for prod_elem, coeff in products.items():
            new_word = word[:i] + (prod_elem,) + word[i + 2:]
            result[new_word] += sign * coeff

    return {k: v for k, v in result.items() if v != 0}


def verify_coderivation(word: Tuple[str, ...],
                        mult_table: Dict[Tuple[str, str], Dict[str, int]]
                        ) -> Dict[str, Any]:
    """Verify Delta circ d = (d otimes id + id otimes d) circ Delta.

    The coderivation property means the bar differential is compatible
    with the deconcatenation coproduct (it is a derivation of the
    coalgebra structure).

    This is the defining property that makes (B(A), d, Delta) a dg coalgebra.
    """
    # Left side: Delta(d(word))
    d_word = bar_differential_gl_n(word, mult_table)
    left_side: Dict[Tuple[Tuple[str, ...], Tuple[str, ...]], int] = defaultdict(int)
    for term, coeff in d_word.items():
        for left, right in deconcatenation_coproduct(term):
            left_side[(left, right)] += coeff

    # Right side: (d otimes id + id otimes d)(Delta(word))
    right_side: Dict[Tuple[Tuple[str, ...], Tuple[str, ...]], int] = defaultdict(int)
    for left, right in deconcatenation_coproduct(word):
        # d otimes id: apply d to the left factor
        d_left = bar_differential_gl_n(left, mult_table) if len(left) >= 2 else {}
        for d_l_term, d_l_coeff in d_left.items():
            right_side[(d_l_term, right)] += d_l_coeff

        # id otimes d: apply d to the right factor, with appropriate sign
        # The sign comes from passing d past the left factor.
        # For degree-0 elements: |left tensor factor| = -len(left) (sum of degrees -1).
        # Sign = (-1)^{|left|} = (-1)^{-len(left)} = (-1)^{len(left)}.
        d_right = bar_differential_gl_n(right, mult_table) if len(right) >= 2 else {}
        sign = (-1) ** len(left)  # Koszul sign from passing d past left
        for d_r_term, d_r_coeff in d_right.items():
            right_side[(left, d_r_term)] += sign * d_r_coeff

    # Compare
    all_keys = set(left_side.keys()) | set(right_side.keys())
    match = all(left_side.get(k, 0) == right_side.get(k, 0) for k in all_keys)

    return {
        "word": word,
        "coderivation_holds": match,
        "left_side_terms": len(left_side),
        "right_side_terms": len(right_side),
    }


# =========================================================================
# 4. Standard algebras: gl_N multiplication tables
# =========================================================================

def gl_n_basis(n: int) -> List[str]:
    """Basis of gl_N: matrix units e_{ij} for 1 <= i,j <= n.

    Returns list of strings "e_ij".
    Dimension: n^2.
    """
    return [f"e_{i}{j}" for i in range(1, n + 1) for j in range(1, n + 1)]


def gl_n_mult_table(n: int) -> Dict[Tuple[str, str], Dict[str, int]]:
    """Multiplication table for gl_N: e_{ij} * e_{kl} = delta_{jk} * e_{il}.

    Returns {("e_ij", "e_kl"): {"e_il": 1}} when j == k, empty dict otherwise.
    """
    table = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                for l in range(1, n + 1):
                    a = f"e_{i}{j}"
                    b = f"e_{k}{l}"
                    if j == k:
                        table[(a, b)] = {f"e_{i}{l}": 1}
    return table


def gl_1_mult_table() -> Dict[Tuple[str, str], Dict[str, int]]:
    """Multiplication table for gl_1 = k: e * e = e.

    The simplest nontrivial associative algebra.
    """
    return {("e", "e"): {"e": 1}}


def dual_numbers_mult_table() -> Dict[Tuple[str, str], Dict[str, int]]:
    """Multiplication table for k[eps]/(eps^2): {1, eps}, eps^2 = 0.

    The simplest non-semisimple associative algebra.
    Augmentation ideal: span{eps}.
    Bar complex: B(k[eps]/(eps^2)) = T^c(s^{-1}eps) = span{[eps], [eps|eps], ...}
    Bar differential: d([eps|...|eps]) = 0 (since eps*eps = 0).
    So H*(B) = B itself (no differential kills anything).
    The Koszul dual is k[x] (polynomial algebra).
    """
    return {
        ("1", "1"): {"1": 1},
        ("1", "eps"): {"eps": 1},
        ("eps", "1"): {"eps": 1},
        # eps * eps = 0: not in the table
    }


def truncated_poly_mult_table(d: int) -> Dict[Tuple[str, str], Dict[str, int]]:
    """Multiplication table for k[x]/(x^d).

    Basis: {1, x, x^2, ..., x^{d-1}}.
    Product: x^a * x^b = x^{a+b} if a+b < d, else 0.
    Augmentation ideal: span{x, x^2, ..., x^{d-1}}.
    """
    table = {}
    for a in range(d):
        for b in range(d):
            a_str = f"x^{a}" if a > 0 else "1"
            b_str = f"x^{b}" if b > 0 else "1"
            if a + b < d:
                prod_str = f"x^{a+b}" if a + b > 0 else "1"
                table[(a_str, b_str)] = {prod_str: 1}
    return table


# =========================================================================
# 5. Bar complex dimensions and coproduct structure
# =========================================================================

def bar_arity_n_dimension(aug_dim: int, n: int) -> int:
    """Dimension of bar arity n for an algebra with augmentation ideal of dim aug_dim.

    B^n(A) = (s^{-1} A_+)^{otimes n}.
    dim B^n = aug_dim^n.
    """
    return aug_dim ** n


def coproduct_term_count(n: int) -> int:
    """Number of terms in the deconcatenation coproduct of a length-n word.

    Delta([a_1|...|a_n]) has n+1 terms (cut positions 0, 1, ..., n).
    """
    return n + 1


def reduced_coproduct_term_count(n: int) -> int:
    """Number of terms in the reduced coproduct of a length-n word.

    bar{Delta}([a_1|...|a_n]) has n-1 terms (cut positions 1, ..., n-1).
    For n = 0 or 1: 0 terms.
    """
    if n <= 1:
        return 0
    return n - 1


def primitive_elements_count(aug_dim: int) -> int:
    """Number of primitive elements in the bar complex.

    An element x is primitive if bar{Delta}(x) = 0.
    In the tensor coalgebra, the primitives are exactly the
    arity-1 elements (singletons), which have dimension aug_dim.

    This is the coradical: P(T^c(V)) = V.
    """
    return aug_dim


# =========================================================================
# 6. SFT-to-chiral-bar dictionary
# =========================================================================

def sft_chiral_bar_dictionary() -> Dict[str, Dict[str, str]]:
    """Complete dictionary between open SFT structures and chiral bar complex.

    Each entry maps an SFT concept to its chiral bar counterpart and
    the physical/geometric interpretation.
    """
    return {
        "state_space": {
            "sft": "Fock space H (open string Hilbert space)",
            "chiral_bar": "A (chiral algebra on the curve X)",
            "geometric": "sections of the vertex algebra bundle on X",
        },
        "brst_operator": {
            "sft": "Q (BRST charge, ghost number +1)",
            "chiral_bar": "d_B (bar differential, cohomological degree +1)",
            "geometric": "OPE residues on FM_k(C), the C-direction",
        },
        "string_splitting": {
            "sft": "Delta (open string midpoint splitting)",
            "chiral_bar": "Delta (deconcatenation coproduct on T^c(s^{-1}A_+))",
            "geometric": "topological splitting on Conf_k(R), the R-direction",
        },
        "star_product": {
            "sft": "* (Witten star product, cubic vertex V_3)",
            "chiral_bar": "m_2 (binary A-infinity operation)",
            "geometric": "binary OPE on FM_2(C) x Conf_2(R)",
        },
        "higher_vertices": {
            "sft": "V_n (n-string vertex, n >= 4)",
            "chiral_bar": "m_n (n-ary A-infinity operation, n >= 3)",
            "geometric": "higher OPE on FM_n(C) x Conf_n(R)",
        },
        "eom": {
            "sft": "Q*Psi + Psi*Psi + V_3(Psi^3) + ... = 0",
            "chiral_bar": "d_B(Theta) + (1/2)[Theta, Theta] = 0 (MC equation)",
            "geometric": "vanishing of shadow obstruction tower",
        },
        "coalgebra_type": {
            "sft": "E_1-coalgebra (Ass^c, coassociative)",
            "chiral_bar": "E_1-coalgebra (dg Ass^c on Ran(X))",
            "geometric": "cofree on desuspended augmentation ideal",
        },
        "curvature": {
            "sft": "tadpole (one-loop anomaly, genus-1 vacuum)",
            "chiral_bar": "m_0 = kappa(A) * omega_g (curved A-infinity)",
            "geometric": "Hodge class on M-bar_{g,n}",
        },
        "gauge_symmetry": {
            "sft": "L-infinity gauge equivalence, Psi -> Psi + Q*Lambda + ...",
            "chiral_bar": "homotopy transfer on the bar complex",
            "geometric": "twisting morphism gauge equivalence",
        },
        "partition_function": {
            "sft": "Z = exp(sum F_g hbar^{2g}) (string partition function)",
            "chiral_bar": "Z^sh(A) = exp(sum F_g hbar^{2g}) (shadow partition function)",
            "geometric": "F_g = kappa * lambda_g^FP (Faber-Pandharipande)",
        },
    }


def ocha_dictionary() -> Dict[str, Dict[str, str]]:
    """Dictionary for open-closed homotopy algebras (Kajiura-Stasheff).

    Maps OCHA structures to the Vol II Swiss-cheese picture.
    """
    return {
        "closed_sector": {
            "ocha": "H_c with L_infinity structure",
            "vol2": "closed colour of SC^{ch,top}: Z^der_ch(A) = C^bullet_ch(A,A)",
            "coalgebra": "E_infinity (cocommutative bar = Chevalley-Eilenberg)",
        },
        "open_sector": {
            "ocha": "H_o with A_infinity structure",
            "vol2": "open colour of SC^{ch,top}: A (boundary algebra)",
            "coalgebra": "E_1 (coassociative bar = tensor coalgebra)",
        },
        "coupling": {
            "ocha": "open-closed operations f_{p,q}: H_c^{otimes p} otimes H_o^{otimes q} -> H_o",
            "vol2": "SC^{ch,top}(p,q): closed inputs twist open composition",
            "directionality": "CLOSED -> OPEN only; no open-to-closed at genus 0",
        },
        "two_colour_bar": {
            "ocha": "B(H_c, H_o) = (B^{Lie}(H_c), B^{Ass}(H_o))",
            "vol2": "(B^{Sigma}(A), B^{ord}(A)) with R-matrix descent",
            "structure": "two-coloured dg coalgebra",
        },
        "modular_extension": {
            "ocha": "not in Kajiura-Stasheff (genus 0 only)",
            "vol2": "Theta^{oc} = Theta_A + sum mu^{M_j} (open/closed MC element)",
            "novelty": "genus >= 1 requires curved Swiss-cheese (Vol I contribution)",
        },
    }


# =========================================================================
# 7. E_1 vs E_infinity analysis
# =========================================================================

def e1_vs_einfty_on_bar() -> Dict[str, Any]:
    """Analysis of E_1 vs E_infinity structure on the bar complex.

    The bar complex T^c(s^{-1}A_+) ALWAYS carries E_1 coalgebra structure
    (the deconcatenation coproduct, which is coassociative).

    For E_infinity algebras (vertex algebras), there is ADDITIONAL structure:
    the symmetric bar complex B^{Sigma}(A) carries a COCOMMUTATIVE coproduct.
    The ordered bar maps to the symmetric bar by taking Sigma_n coinvariants,
    with the R-matrix as twisting datum.

    This function summarizes the structural analysis.
    """
    return {
        "e1_always_present": True,
        "e1_structure": "deconcatenation coproduct Delta on T^c(s^{-1}A_+)",
        "e1_source": "cofree conilpotent coalgebra structure (automatic for tensor coalgebra)",
        "e1_physical": "open string splitting / topological interval cutting (R-direction)",

        "einfty_when": "A is E_infinity-chiral (= vertex algebra = LOCAL)",
        "einfty_structure": "cocommutative coproduct on B^{Sigma}(A) = Sigma_n-coinvariants",
        "einfty_descent": "B^{ord} -> B^{Sigma} via R-matrix twisted coinvariants (Vol II AP38)",

        "genuinely_e1": "quantum vertex algebras (Etingof-Kazhdan): B^{ord} only, no B^{Sigma}",

        "three_bar_complexes": {
            "B_FG": "Francis-Gaitsgory bar: uses only a_{(0)}b (chiral Lie bracket), misses kappa",
            "B_Sigma": "Symmetric bar: uses all OPE products, Sigma_n coinvariants (Vol I Thm A)",
            "B_ord": "Ordered bar: uses all OPE products, retains linear ordering (Part VII)",
        },

        "maps": "B^{ord} --(coinvariants)--> B^{Sigma} --(assoc graded)--> B^{FG}",

        "key_insight": (
            "The E_1 coalgebra structure on B(A) encodes the TOPOLOGICAL direction "
            "(interval cutting on Conf_k(R)). The differential encodes the HOLOMORPHIC "
            "direction (OPE residues on FM_k(C)). Together they form a dg coalgebra "
            "whose operadic home is SC^{ch,top} (the Swiss-cheese operad). "
            "This is the same structure as open SFT, where Q = C-direction and "
            "Delta = R-direction."
        ),
    }


# =========================================================================
# 8. Explicit computation: gl_N bar complex and coproduct at low orders
# =========================================================================

def gl_n_bar_coproduct_low_arity(n: int, max_arity: int = 3) -> Dict[str, Any]:
    """Compute the bar complex of gl_N and its coproduct at low arities.

    For gl_N (concentrated in degree 0, no differential):
    - Augmentation ideal = gl_N itself (after choosing unit 1 = sum e_{ii})
      Actually, gl_N = k * I oplus sl_N oplus traceless diagonal.
      For simplicity, use the full matrix algebra as augmentation ideal.
    - Bar arity n: dim = (N^2)^n
    - Bar differential from matrix multiplication
    - Coproduct: deconcatenation (E_1)

    Returns dimensions and sample coproducts.
    """
    aug_dim = n * n  # dim gl_N = N^2

    result = {
        "algebra": f"gl_{n}",
        "dimension": aug_dim,
    }

    for arity in range(1, max_arity + 1):
        dim = bar_arity_n_dimension(aug_dim, arity)
        n_coprod_terms = coproduct_term_count(arity)
        n_red_coprod = reduced_coproduct_term_count(arity)

        result[f"arity_{arity}"] = {
            "dimension": dim,
            "coproduct_terms": n_coprod_terms,
            "reduced_coproduct_terms": n_red_coprod,
        }

    result["primitives"] = primitive_elements_count(aug_dim)

    return result


def affine_gl_n_comparison(n: int) -> Dict[str, Any]:
    """Compare the bar complex of gl_N (SFT) with the chiral bar of affine gl_N.

    Open SFT with Chan-Paton factor gl_N:
        A = gl_N (associative algebra in degree 0)
        B(gl_N) = T^c(s^{-1} gl_N) with d from matrix multiplication
        Coproduct: deconcatenation (E_1)

    Chiral bar of affine gl_N at level k:
        A = V_k(gl_N) (vertex algebra, infinite-dimensional)
        B^ch(V_k(gl_N)) = factorization coalgebra on Ran(X)
        Coproduct: deconcatenation (E_1 from R-direction)
        Differential: OPE residues (from C-direction)

    The finite-dimensional gl_N bar complex is the ZERO-MODE TRUNCATION
    of the chiral bar complex: restricting to weight-0 states only.
    """
    aug_dim = n * n
    # kappa for affine gl_N at level k: dim(gl_N) * (k + N) / (2N)
    # For gl_N: dim = N^2, h^v = N
    # We use generic level k as a symbol
    dim_g = n * n
    dual_coxeter = n

    return {
        "algebra": f"gl_{n}",
        "finite_dim_bar": {
            "augmentation_ideal_dim": aug_dim,
            "bar_arity_1_dim": aug_dim,
            "bar_arity_2_dim": aug_dim ** 2,
            "bar_arity_3_dim": aug_dim ** 3,
            "coproduct_type": "E_1 (deconcatenation)",
            "differential": "from gl_N matrix multiplication",
        },
        "chiral_bar": {
            "algebra": f"V_k(gl_{n}) (affine vertex algebra at level k)",
            "state_space": "infinite-dimensional (all descendants)",
            "weight_0_truncation": f"gl_{n} (recovers finite-dim bar)",
            "coproduct_type": "E_1 (deconcatenation on Conf_k(R))",
            "differential": "OPE residues on FM_k(C)",
            "kappa_formula": f"dim(gl_{n}) * (k + {dual_coxeter}) / (2 * {dual_coxeter}) = {dim_g}*(k+{dual_coxeter})/{2*dual_coxeter}",
        },
        "comparison": {
            "coproduct_match": True,
            "differential_match": "at weight 0 only (truncation)",
            "e1_structure": "both carry E_1 coalgebra (deconcatenation)",
            "key_difference": (
                "The finite-dim gl_N bar sees only weight-0 states. "
                "The chiral bar at level k includes ALL descendants "
                "(partial^n J(z) for all n >= 0), giving an infinite-dim "
                "bar complex whose weight-0 truncation recovers B(gl_N). "
                "The curvature kappa * omega_g appears only at genus >= 1 "
                "in the chiral bar."
            ),
        },
    }


# =========================================================================
# 9. Numerical invariants for the comparison
# =========================================================================

def bar_euler_characteristic(aug_dim: int, max_arity: int) -> Fraction:
    """Formal Euler characteristic of the bar complex (truncated).

    chi = sum_{n=1}^{max_arity} (-1)^n * dim B^n
        = sum_{n=1}^{max_arity} (-1)^n * aug_dim^n

    For the FULL (non-truncated) bar complex:
    chi = sum_{n=1}^{infty} (-1)^n * d^n = -d/(1+d)

    This is the formal Euler characteristic of the tensor coalgebra.
    """
    chi = Fraction(0)
    for n in range(1, max_arity + 1):
        chi += Fraction((-1) ** n) * Fraction(aug_dim ** n)
    return chi


def bar_euler_characteristic_exact(aug_dim: int) -> Fraction:
    """Exact formal Euler characteristic: -d/(1+d).

    This is the generating function value at t=-1 of
    sum_{n >= 1} d^n t^n = dt/(1-dt),
    evaluated at t = -1: -d/(1+d).

    For gl_1 (d=1): chi = -1/2.
    For gl_2 (d=4): chi = -4/5.
    """
    d = Fraction(aug_dim)
    return -d / (1 + d)


def coproduct_splitting_count(n: int, k: int) -> int:
    """Number of ways to split a length-n word into k consecutive subwords.

    This is binom(n, k-1) = n! / ((k-1)! * (n-k+1)!) when we allow
    empty subwords at the boundaries... actually:

    With possibly-empty subwords: binom(n + k - 1, k - 1) = "stars and bars."
    Without empty subwords: binom(n - 1, k - 1).

    The deconcatenation coproduct allows empty subwords (the counit terms).
    So the k-fold iterated coproduct of a length-n word has
    binom(n + k, k) terms... let me be precise.

    The number of ordered compositions of n into exactly k parts
    (allowing zero parts) is binom(n + k - 1, k - 1).
    For the (k-1)-fold iterated coproduct (splitting into k pieces),
    we get binom(n + k - 1, k - 1) terms.

    Verification: k=2 (single coproduct): binom(n+1, 1) = n+1. Correct.
    k=3 (double coproduct): binom(n+2, 2). Correct (tripartitions).
    """
    return math.comb(n + k - 1, k - 1)


# =========================================================================
# 10. Full comparison summary
# =========================================================================

def full_comparison_summary() -> Dict[str, Any]:
    """Complete summary of the SFT bar complex / chiral bar complex comparison.

    Central result: the bar coalgebra of an A-infinity algebra ALWAYS carries
    E_1 coalgebra structure (the deconcatenation coproduct).  This is not
    extra structure; it is the AUTOMATIC coalgebra structure on the cofree
    conilpotent coalgebra T^c(s^{-1}A_+).

    In the 3d HT setting (C x R):
    - The E_1 coproduct encodes the R-direction (topological splitting)
    - The bar differential encodes the C-direction (holomorphic collisions)
    - Together: dg E_1-coalgebra = the Swiss-cheese fingerprint

    In open SFT:
    - The E_1 coproduct encodes string splitting
    - The BRST operator Q encodes worldsheet scattering
    - Together: dg E_1-coalgebra = the open SFT structure

    These ARE the same mathematical structure.  The precise dictionary is
    given by sft_chiral_bar_dictionary().
    """
    return {
        "central_theorem": (
            "The bar construction B(A) = T^c(s^{-1}A_+) of an A-infinity algebra A "
            "is a dg E_1-coalgebra (= dg coassociative coalgebra). The E_1 structure "
            "is the deconcatenation coproduct, which is AUTOMATIC (cofree coalgebra). "
            "The A-infinity structure is equivalent to a coderivation d with d^2 = 0."
        ),
        "physical_identification": {
            "sft": "Open SFT: Q = bar differential, Delta = string splitting",
            "chiral": "Chiral bar: d_B = OPE residues on FM_k(C), Delta = splitting on Conf_k(R)",
            "3d_ht": "3d HT on C x R: d = C-direction factorization, Delta = R-direction factorization",
        },
        "e1_vs_einfty": e1_vs_einfty_on_bar(),
        "ocha": ocha_dictionary(),
        "dictionary": sft_chiral_bar_dictionary(),
        "key_distinctions": {
            "bar_not_bulk": (
                "AP34/AP-OC: The bar complex classifies TWISTING MORPHISMS. "
                "The bulk observables are the DERIVED CENTER Z^der_ch(A). "
                "In SFT: the bar complex encodes open-string data; "
                "the closed-string observables are a SEPARATE object."
            ),
            "three_functors": (
                "AP25: Three functors on B(A): "
                "(1) Omega(B(A)) = A (reconstruction/inversion), "
                "(2) D_Ran(B(A)) = B(A!) (Verdier = Koszul dual), "
                "(3) C^bullet_ch(A,A) = derived center (universal bulk). "
                "In SFT: (1) = open string reconstruction, "
                "(2) = D-brane duality, (3) = closed string extraction."
            ),
            "genus_curvature": (
                "At genus g >= 1: the bar differential squares to curvature "
                "m_0 = kappa(A) * omega_g. In SFT: this is the one-loop tadpole "
                "anomaly. The curved A-infinity structure at higher genus is the "
                "mathematical encoding of the SFT loop expansion."
            ),
        },
    }
