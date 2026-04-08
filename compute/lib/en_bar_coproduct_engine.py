r"""E_n bar coproduct engine: explicit coproduct structures on B_{E_n}(A) for varying n.

MATHEMATICAL FRAMEWORK
======================

For a P-algebra A (where P is a quadratic operad), the operadic bar construction is

    B_P(A) = (P^{!,c} circ \bar{A}, d_B)

where P^{!,c} is the Koszul dual cooperad and \bar{A} = ker(epsilon) is the
augmentation ideal.  B_P(A) is a COFREE P^!-coalgebra.  The coproduct on B_P(A)
is the cooperadic cocomposition of P^{!,c}.

The key operadic Koszul dualities (Loday-Vallette, Theorem 7.4.2):

    Ass^! = Ass         (associative is self-dual)
    Com^! = Lie          (commutative <-> Lie)
    Lie^! = Com          (Lie <-> commutative)
    E_n^! = E_n{-n}     (E_n is self-dual up to shift)

This gives the bar complex structure:

    B_{Ass}(A) = T^c(s^{-1}\bar{A}) = cofree Ass-coalgebra (tensor coalgebra)
        Coproduct: DECONCATENATION (coassociative, NON-cocommutative)
        Delta([a_1|...|a_n]) = sum_{i=0}^{n} [a_1|...|a_i] tensor [a_{i+1}|...|a_n]

    B_{Com}(A) = Lie^c(s^{-1}\bar{A}) = cofree Lie-coalgebra
        Coproduct: Lie COBRACKET (coantisymmetric, co-Jacobi)
        This is NOT a coassociative coproduct.  The underlying graded vector
        space is Lambda(s^{-1}\bar{A}) (exterior algebra = symmetric coalgebra
        after desuspension sign), but the coalgebra structure is Lie-cooperadic,
        not Ass-cooperadic.  The Harrison complex.

    B_{Lie}(A) = Com^c(s^{-1}\bar{A}) = cofree Com-coalgebra (symmetric coalgebra)
        Coproduct: SHUFFLE (coassociative AND cocommutative)
        Delta(a_1 ... a_n) = sum_{S subset [n]} a_S tensor a_{[n]\S}
        with Koszul signs from desuspension.  This is the CE complex.

    B_{E_n}(A) = E_n{-n}^c(s^{-1}\bar{A}) = cofree E_n{-n}-coalgebra
        Coproduct: E_n-COALGEBRA structure parametrized by Conf_k(R^n).
        At n=1: recovers Ass (deconcatenation).
        At n=2: E_2 coalgebra (braided, homotopy-cocommutative).
        At n=infinity: recovers Com (shuffle/cocommutative).

KEY DISTINCTION: For a COMMUTATIVE algebra A, we can form B_P(A) for
ANY operad P that receives a map from Com (i.e., Com -> P):

    Com -> E_infty -> ... -> E_2 -> E_1 = Ass

Each functor B_P forgets different amounts of commutativity:

    B_{Com}(A): remembers all commutativity.  Lie^c coalgebra.  SMALLEST.
    B_{E_n}(A): remembers E_n commutativity.  E_n^! coalgebra.
    B_{Ass}(A): forgets all commutativity.  Ass coalgebra.  LARGEST.

DIMENSION COMPARISON:

For A = k[x]/(x^{d+1}) with generator x in degree 0:

    B_{Ass}^n(A) = (s^{-1}\bar{A})^{tensor n}
        Basis: [s^{-1}x^{i_1} | ... | s^{-1}x^{i_n}] for 1 <= i_j <= d
        Dimension: d^n  (full tensor power)

    B_{Com}^n(A) = Lambda^n(s^{-1}\bar{A})   (for generators in even degree after desusp)
        Basis: s^{-1}x^{i_1} wedge ... wedge s^{-1}x^{i_n} for 1 <= i_1 < ... < i_n <= d
        Dimension: C(d, n)  (binomial coefficient)

    Ratio: d^n / C(d,n) = n! * d^n / (d!/(d-n)!) -> n! as d -> infty.

THE CHIRAL CASE:

A chiral algebra A on C is E_infty-chiral.  The manuscript's bar complex
B^ch(A) carries an E_1 (coassociative) coproduct from the R-direction,
NOT an E_infty coproduct.  This is because:

    The chiral bar complex = B_{SC^{ch,top}}(A)

where SC^{ch,top} is the holomorphic-topological Swiss-cheese operad.
The differential (C-direction) uses E_2/chiral structure.
The coproduct (R-direction) uses E_1/associative structure.

This is NOT the same as B_{E_2}(A) or B_{Com}(A).  It is a MIXED
(two-colored) construction.  The Swiss-cheese bar complex is LARGER than
B_{E_2}(A) because it retains the ordered tensor structure.  Concretely:

    B_{E_2}(A): elements are symmetric (up to homotopy) in the E_2 sense
    B_{SC}(A):  elements are ORDERED (the R-direction ordering is physical)

The manuscript uses the ordered (tensor coalgebra) structure because:
1. The R-matrix R(z) lives in End(V tensor V), which requires ordering.
2. The Yangian/quantum group structure requires the non-cocommutative part.
3. The Swiss-cheese operad naturally produces ordered bar complexes.

If one took the E_2 bar B_{E_2}(A) instead, one would lose the R-matrix
data and the quantum group structure.  One would retain only the
COMMUTATIVE part of the quantum group: the classical r-matrix r(z).

EXPLICIT COMPUTATIONS (this module):

1. B_{E_1}(k[x]) at arities 1-6: dimensions, coproduct matrices
2. B_{E_infty}(k[x]) at arities 1-6: dimensions, coproduct matrices
3. B_{E_2}(k[x]) at arities 1-6: dimensions (uses Arnold algebra)
4. Dimension ratios dim(B_{E_1}) / dim(B_{E_infty}) at each arity
5. Heisenberg algebra comparison at arities 1-6
6. Verification of coproduct axioms (coassociativity, cocommutativity)

References:
    Loday-Vallette: Algebraic Operads (Grundlehren 346), Ch. 7, 11
    Fresse: Modules over Operads and Functors (LNM 1967)
    Francis: The Tangent Complex and Hochschild Cohomology of E_n Rings
    Lurie: Higher Algebra, Ch. 5
    chapters/theory/en_koszul_duality.tex (thm:en-chiral-bridge, thm:bar-swiss-cheese)
    chapters/theory/bar_construction.tex (thm:diff-is-coderivation)
    AP14: Koszulness != formality
    AP37: Lie homology (exterior) != Hochschild homology (tensor)
    AP45: |s^{-1}v| = |v| - 1 (desuspension LOWERS degree)
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product as iproduct
from math import factorial, comb, prod
from typing import Dict, FrozenSet, List, Optional, Set, Tuple


# ================================================================
# 1. Graded vector spaces and sign conventions
# ================================================================

def koszul_sign(perm: Tuple[int, ...], degrees: Tuple[int, ...]) -> int:
    r"""Koszul sign of a permutation acting on graded elements.

    For elements v_1, ..., v_n of degrees d_1, ..., d_n, the permutation
    sigma acts with sign (-1)^{sum of d_i * d_j for transposed pairs (i,j)}.

    We compute this by counting inversions weighted by degree products.
    """
    n = len(perm)
    sign = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                sign += degrees[perm[i]] * degrees[perm[j]]
    return (-1) ** (sign % 2)


def desuspend_degree(original_degree: int) -> int:
    r"""Desuspension: |s^{-1}v| = |v| - 1 (AP45).

    The bar construction uses desuspension s^{-1}.
    """
    return original_degree - 1


# ================================================================
# 2. E_1 bar = tensor coalgebra (Ass bar)
# ================================================================

class E1BarComplex:
    r"""The E_1 (associative) bar complex B_{E_1}(A) = T^c(s^{-1}\bar{A}).

    The coproduct is DECONCATENATION:
        Delta([a_1|...|a_n]) = sum_{i=0}^{n} [a_1|...|a_i] tensor [a_{i+1}|...|a_n]

    This is coassociative but NOT cocommutative.

    For A = k[x_1, ..., x_d]/(relations), the augmentation ideal
    \bar{A} has basis {x^alpha : alpha != 0, alpha in allowed set}.
    """

    def __init__(self, gen_dim: int, max_arity: int = 6):
        """Initialize with gen_dim generators in degree 0.

        Args:
            gen_dim: number of generators of A (= dim of degree-1 part of bar{A}).
                     For k[x]/(x^{d+1}), gen_dim = d.
                     For Heisenberg at weight <= N, gen_dim = N.
            max_arity: maximum bar arity to compute.
        """
        self.gen_dim = gen_dim
        self.max_arity = max_arity
        # Desuspended degree of each generator: |s^{-1}v| = |v| - 1
        # For generators of A in degree 0: desuspended degree = -1
        # For generators of A in degree 1 (e.g., weight-1 loop generators):
        # desuspended degree = 0
        # We work with degree-0 generators (polynomial algebra case)
        self.desusp_degree = 0  # for weight-1 generators after desuspension

    def dimension(self, arity: int) -> int:
        r"""Dimension of B_{E_1}^n(A) = (s^{-1}\bar{A})^{\otimes n}.

        dim = gen_dim^arity (full tensor power).
        """
        if arity < 0:
            return 0
        if arity == 0:
            return 1  # the ground field (counit target)
        return self.gen_dim ** arity

    def basis(self, arity: int) -> List[Tuple[int, ...]]:
        r"""Ordered basis of B_{E_1}^n.

        Elements are tuples (i_1, ..., i_n) with 0 <= i_j < gen_dim,
        representing [s^{-1}x_{i_1} | ... | s^{-1}x_{i_n}].
        """
        if arity == 0:
            return [()]
        return list(iproduct(range(self.gen_dim), repeat=arity))

    def coproduct(self, element: Tuple[int, ...]) -> List[Tuple[Tuple[int, ...], Tuple[int, ...], Fraction]]:
        r"""Deconcatenation coproduct.

        Delta([a_1|...|a_n]) = sum_{i=0}^{n} [a_1|...|a_i] tensor [a_{i+1}|...|a_n]

        Returns list of (left_part, right_part, coefficient).
        All coefficients are 1 for the tensor coalgebra.
        """
        n = len(element)
        terms = []
        for i in range(n + 1):
            left = element[:i]
            right = element[i:]
            terms.append((left, right, Fraction(1)))
        return terms

    def coproduct_matrix(self, arity: int) -> Dict[Tuple[int, int], List[Tuple[Tuple[int, ...], Fraction]]]:
        r"""Full coproduct as a bigraded map.

        Delta: B^n -> bigoplus_{p+q=n} B^p tensor B^q.

        Returns dict mapping (p, q) to a list of
        (element_index_pair, coefficient) for each basis element.
        """
        result = {}
        basis_n = self.basis(arity)
        for p in range(arity + 1):
            q = arity - p
            result[(p, q)] = []

        for idx, elem in enumerate(basis_n):
            for left, right, coeff in self.coproduct(elem):
                p, q = len(left), len(right)
                result[(p, q)].append((idx, left, right, coeff))
        return result

    def verify_coassociativity(self, arity: int) -> bool:
        r"""Verify (Delta tensor id) circ Delta = (id tensor Delta) circ Delta.

        For each basis element, compute both sides and check equality.
        """
        basis = self.basis(arity)
        for elem in basis:
            # Left: (Delta tensor id) circ Delta
            left_terms = {}  # (a, b, c) -> coefficient
            for l1, r1, c1 in self.coproduct(elem):
                for l2, r2, c2 in self.coproduct(l1):
                    key = (l2, r2, r1)
                    left_terms[key] = left_terms.get(key, Fraction(0)) + c1 * c2

            # Right: (id tensor Delta) circ Delta
            right_terms = {}
            for l1, r1, c1 in self.coproduct(elem):
                for l2, r2, c2 in self.coproduct(r1):
                    key = (l1, l2, r2)
                    right_terms[key] = right_terms.get(key, Fraction(0)) + c1 * c2

            if left_terms != right_terms:
                return False
        return True

    def verify_non_cocommutativity(self, arity: int) -> bool:
        r"""Verify that the coproduct is NOT cocommutative at this arity.

        Cocommutativity would mean tau circ Delta = Delta where tau is the
        swap.  For the tensor coalgebra, this FAILS at arity >= 2 when
        gen_dim >= 2 (there exist elements [a|b] != [b|a]).
        """
        if arity < 2 or self.gen_dim < 2:
            return False  # cannot detect at low arity or dimension

        basis = self.basis(arity)
        for elem in basis:
            coprod = self.coproduct(elem)
            # Original: sum of (left, right)
            # Swapped: sum of (right, left) with Koszul sign
            original = {}
            swapped = {}
            for left, right, coeff in coprod:
                original[(left, right)] = original.get((left, right), Fraction(0)) + coeff
                # The swap map tau(a tensor b) = (-1)^{|a||b|} b tensor a
                # For degree-0 desuspended elements: sign is always +1
                sign = Fraction(1)  # since desusp degree is 0
                swapped[(right, left)] = swapped.get((right, left), Fraction(0)) + sign * coeff

            if original != swapped:
                return True  # found non-cocommutativity
        return False


# ================================================================
# 3. E_infty bar = Lie cooperadic bar (Harrison complex)
# ================================================================

class EInfBarComplex:
    r"""The E_infty (commutative) bar complex B_{Com}(A).

    For P = Com, the Koszul dual cooperad is P^{!,c} = Lie^c.
    The bar construction is:

        B_{Com}(A) = (Lie^c circ s^{-1}\bar{A}, d_B)

    This is the HARRISON COMPLEX (= Chevalley-Eilenberg complex of the
    abelianization, for commutative algebras).

    The underlying graded vector space at arity n is:

        Lie^c(n) tensor_{S_n} (s^{-1}\bar{A})^{tensor n}

    where Lie^c(n) is the n-th component of the Lie cooperad.

    KEY FACT: dim(Lie^c(n)) = (n-1)! as an S_n-module, Lie^c(n)
    is the representation induced from the sign representation of
    the cyclic group Z_n (Klyachko's theorem).

    For gen_dim generators all in the SAME degree after desuspension:
    if desusp_degree is EVEN (e.g., 0 for weight-1 generators):
        the S_n action on (s^{-1}V)^{tensor n} is the trivial action,
        and the coinvariants Lie^c(n) tensor_{S_n} V^{tensor n} have
        dimension (n-1)! * gen_dim^n / n! = gen_dim^n / n
        (this is only approximate; the exact answer depends on the
        representation theory).

    ACTUALLY: Lie^c(n) tensor_{S_n} V^{tensor n} for V of dim d
    has dimension equal to the number of Lyndon words of length n
    in an alphabet of size d, which equals (1/n) * sum_{d|n} mu(n/d) * d^d_alphabet.
    [Correction: the necklace formula.]

    For the cofree Lie coalgebra on V, the arity-n component is:
        CofreeLie^n(V) = Lie^c(n) tensor_{S_n} V^{tensor n}
    with dim = (1/n) * sum_{d|n} mu(n/d) * (dim V)^d  (necklace polynomial).

    The coproduct is the LIE COBRACKET:
        delta: CofreeLie^n(V) -> sum_{p+q=n} CofreeLie^p(V) tensor CofreeLie^q(V)
    satisfying coantisymmetry and co-Jacobi.

    For COMMUTATIVE algebras, there is also the CE complex perspective:
    B_{Com}(A) can be computed as the complex (Lambda(s^{-1}\bar{A}), d_CE)
    where Lambda is the exterior algebra and d_CE is the CE differential.
    The CE complex carries a COCOMMUTATIVE coproduct (the shuffle coproduct).

    CRITICAL DISTINCTION: These are two different presentations of the
    same object!  The Harrison presentation gives a Lie coalgebra;
    the CE presentation gives a cocommutative coalgebra.  They compute
    the same cohomology (Harrison = CE for commutative algebras in char 0),
    but the coalgebra structures are DIFFERENT:
    - Harrison: Lie^c coalgebra (the operadic bar)
    - CE: cocommutative coalgebra (the classical bar, quotiented by shuffle)

    What we compute here: the CE/shuffle presentation, which has
    cocommutative coproduct and dimension C(d, n) at arity n.

    CORRECTION AND CLARIFICATION (essential for the computation):

    For a commutative algebra A, there are THREE bar constructions:

    (a) B_{Ass}(A) = T^c(s^{-1}\bar{A}): tensor coalgebra, dim = d^n.
        Coproduct: deconcatenation (coassociative, non-cocommutative).

    (b) B_{Com}(A) = Lie^c(s^{-1}\bar{A}): cofree Lie coalgebra.
        This is the OPERADIC bar.  It carries a Lie cobracket.
        dim at arity n = necklace polynomial N(n, d).

    (c) B_{Ass}(A) / (shuffle equivalence) = Sym^c(s^{-1}\bar{A}):
        symmetric coalgebra.  This is obtained from (a) by quotienting
        by the shuffle equivalence relation (identifying shuffles).
        Coproduct: shuffle (coassociative AND cocommutative).
        dim = C(d+n-1, n) for symmetric, or C(d, n) for exterior.

    The relationship: (c) is a QUOTIENT of (a), and (b) is a RETRACT
    of (a) (the Eulerian idempotent projects onto the Lie part).

    For the purpose of THIS module's computations, we implement:
    - (a) as E1BarComplex (tensor coalgebra, deconcatenation)
    - (c) as EInfBarComplex (symmetric/exterior coalgebra, shuffle coproduct)
    - The Lie cooperadic bar (b) is recorded dimensionally but its
      coproduct (a Lie cobracket) is a different algebraic structure.

    For weight-1 generators (desuspended degree 0, hence EVEN):
    the symmetric coalgebra has dim = C(d+n-1, n) (stars-and-bars).

    For weight-2 generators (desuspended degree 1, hence ODD):
    the exterior coalgebra has dim = C(d, n) (subsets).
    """

    def __init__(self, gen_dim: int, max_arity: int = 6,
                 desusp_degree: int = 0):
        """Initialize.

        Args:
            gen_dim: dimension of the generating space.
            max_arity: maximum arity.
            desusp_degree: desuspended degree of generators.
                0 = even (symmetric coalgebra), 1 = odd (exterior coalgebra).
        """
        self.gen_dim = gen_dim
        self.max_arity = max_arity
        self.desusp_degree = desusp_degree

    def dimension(self, arity: int) -> int:
        r"""Dimension of B_{Com}^n(A) = Sym^n or Lambda^n of s^{-1}\bar{A}.

        For even desuspended degree: Sym^n(V) has dim C(d+n-1, n).
        For odd desuspended degree: Lambda^n(V) has dim C(d, n).
        """
        if arity < 0:
            return 0
        if arity == 0:
            return 1
        d = self.gen_dim
        if self.desusp_degree % 2 == 0:
            # Symmetric: multisets of size n from d elements
            return comb(d + arity - 1, arity)
        else:
            # Exterior: subsets of size n from d elements
            return comb(d, arity)

    def basis(self, arity: int) -> List[Tuple[int, ...]]:
        r"""Basis of the symmetric/exterior coalgebra at arity n.

        For even degree: weakly increasing tuples (i_1 <= ... <= i_n).
        For odd degree: strictly increasing tuples (i_1 < ... < i_n).
        """
        if arity == 0:
            return [()]
        d = self.gen_dim
        if self.desusp_degree % 2 == 0:
            # Multisets: weakly increasing tuples
            return list(_weakly_increasing_tuples(d, arity))
        else:
            # Subsets: strictly increasing tuples
            return [tuple(c) for c in combinations(range(d), arity)]

    def shuffle_coproduct(self, element: Tuple[int, ...]) -> List[Tuple[Tuple[int, ...], Tuple[int, ...], Fraction]]:
        r"""Shuffle coproduct on the symmetric/exterior coalgebra.

        For the symmetric coalgebra Sym^c(V):
            Delta(v_1 ... v_n) = sum over (p,q)-unshuffles sigma of
                v_{sigma(1)} ... v_{sigma(p)} tensor v_{sigma(p+1)} ... v_{sigma(n)}

        An (p,q)-unshuffle of (1,...,n) is a permutation sigma such that
        sigma(1) < ... < sigma(p) and sigma(p+1) < ... < sigma(n).

        For a weakly/strictly increasing tuple, this simplifies to
        splitting the multiset/set into two parts.

        Returns list of (left_part, right_part, coefficient).
        """
        n = len(element)
        terms = []

        for p in range(n + 1):
            q = n - p
            # For a symmetric/exterior element, we need to enumerate
            # all ways to split the multiset/set into parts of size p and q.
            for left_indices in combinations(range(n), p):
                right_indices = tuple(i for i in range(n) if i not in left_indices)
                left = tuple(element[i] for i in left_indices)
                right = tuple(element[i] for i in right_indices)

                # Normalize: sort each part (they should already be sorted
                # for a sorted input, since we pick indices in order)
                # Koszul sign from the permutation
                sign = _unshuffle_sign(left_indices, right_indices,
                                       tuple(self.desusp_degree for _ in element))

                terms.append((left, right, Fraction(sign)))

        return terms

    def verify_coassociativity(self, arity: int) -> bool:
        r"""Verify (Delta tensor id) circ Delta = (id tensor Delta) circ Delta."""
        basis = self.basis(arity)
        for elem in basis:
            left_terms = {}
            for l1, r1, c1 in self.shuffle_coproduct(elem):
                for l2, r2, c2 in self.shuffle_coproduct(l1):
                    key = (l2, r2, r1)
                    left_terms[key] = left_terms.get(key, Fraction(0)) + c1 * c2

            right_terms = {}
            for l1, r1, c1 in self.shuffle_coproduct(elem):
                for l2, r2, c2 in self.shuffle_coproduct(r1):
                    key = (l1, l2, r2)
                    right_terms[key] = right_terms.get(key, Fraction(0)) + c1 * c2

            # Clean zeros
            left_terms = {k: v for k, v in left_terms.items() if v != 0}
            right_terms = {k: v for k, v in right_terms.items() if v != 0}

            if left_terms != right_terms:
                return False
        return True

    def verify_cocommutativity(self, arity: int) -> bool:
        r"""Verify tau circ Delta = Delta (cocommutativity).

        For the shuffle coproduct, this should hold: the shuffle
        coproduct is symmetric under swapping the two tensor factors
        (with appropriate Koszul signs).
        """
        basis = self.basis(arity)
        for elem in basis:
            coprod = self.shuffle_coproduct(elem)
            original = {}
            swapped = {}
            for left, right, coeff in coprod:
                original[(left, right)] = original.get((left, right), Fraction(0)) + coeff
                # Swap with Koszul sign: tau(a tensor b) = (-1)^{|a||b|} b tensor a
                deg_left = len(left) * self.desusp_degree
                deg_right = len(right) * self.desusp_degree
                swap_sign = (-1) ** (deg_left * deg_right)
                swapped[(right, left)] = swapped.get((right, left), Fraction(0)) + Fraction(swap_sign) * coeff

            original = {k: v for k, v in original.items() if v != 0}
            swapped = {k: v for k, v in swapped.items() if v != 0}

            if original != swapped:
                return False
        return True


def _weakly_increasing_tuples(d: int, n: int):
    """Generate all weakly increasing n-tuples from {0, ..., d-1}."""
    if n == 0:
        yield ()
        return
    for start in range(d):
        for rest in _weakly_increasing_tuples_from(d, n - 1, start):
            yield (start,) + rest


def _weakly_increasing_tuples_from(d: int, n: int, start: int):
    """Generate weakly increasing n-tuples with values >= start."""
    if n == 0:
        yield ()
        return
    for val in range(start, d):
        for rest in _weakly_increasing_tuples_from(d, n - 1, val):
            yield (val,) + rest


def _unshuffle_sign(left_indices: Tuple[int, ...], right_indices: Tuple[int, ...],
                    degrees: Tuple[int, ...]) -> int:
    r"""Koszul sign of an unshuffle permutation.

    The unshuffle takes (0, 1, ..., n-1) to (left_indices, right_indices).
    The sign is (-1)^{number of transpositions weighted by degrees}.
    """
    n = len(left_indices) + len(right_indices)
    perm = list(left_indices) + list(right_indices)
    # Count inversions weighted by degree
    sign_exp = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                sign_exp += degrees[perm[i]] * degrees[perm[j]]
    return (-1) ** (sign_exp % 2)


# ================================================================
# 4. E_2 bar: uses Arnold algebra
# ================================================================

class E2BarComplex:
    r"""The E_2 bar complex B_{E_2}(A).

    For an E_2-algebra A, the bar construction B_{E_2}(A) is an
    E_2-coalgebra (= E_2{-2}-coalgebra more precisely).

    The E_2 bar complex at arity n has the form:

        B_{E_2}^n(A) = C_*(FM_n(C)) tensor_{S_n} (s^{-1}\bar{A})^{tensor n}

    where FM_n(C) = Conf_n(C) is the configuration space of n points in C,
    and C_*(FM_n(C)) is its chain complex.

    The cohomology H*(Conf_n(C)) is the Arnold algebra:
        Generated by omega_{ij} in degree 1 for 1 <= i < j <= n,
        subject to the Arnold relations:
            omega_{ij} omega_{jk} + omega_{jk} omega_{ki} + omega_{ki} omega_{ij} = 0.

    The Poincare polynomial is P_n(t) = prod_{j=0}^{n-1} (1 + jt).
    Total Betti number = n!.

    The E_2 coproduct comes from the operad structure on Conf_*(C):
    the "forgetting a subset" maps provide the coalgebra structure.

    At the cohomological level, the E_2 coalgebra structure includes:
    - An E_1 (coassociative) part: deconcatenation
    - A homotopy-cocommutative part: the braiding from pi_1(Conf_2(C)) = Z
    - The two together: the E_2 coalgebra is "coassociative + homotopy
      cocommutative", where the homotopy is parametrized by the circle
      S^1 = R^2 \ {0}.

    For the DIMENSION computation (which is what we can do explicitly):
    The E_2 bar at arity n lives in the chain complex of FM_n(C) tensor_{S_n} V^n.
    If A has gen_dim generators, the dimension (in a fixed degree) depends
    on the Arnold algebra.  As a TOTAL dimension (summing over all degrees):

        total_dim(B_{E_2}^n) = sum_k dim(H^k(Conf_n(C))) * dim(Sym^{n-k}(V))
                             (approximately; the exact answer uses coinvariants)

    More precisely, for free generators (no relations among them) with
    all generators in the same degree:

        dim(B_{E_2}^n(A)) = sum_{k=0}^{n-1} |s(n, n-k)| * [dim of k-th part]

    where |s(n, n-k)| are unsigned Stirling numbers of the first kind
    (Betti numbers of Conf_n(C)).

    SIMPLIFIED MODEL: For this engine, we compute the E_2 bar dimension
    as the product of Arnold algebra dimension and the tensor/coinvariant part.
    """

    def __init__(self, gen_dim: int, max_arity: int = 6):
        self.gen_dim = gen_dim
        self.max_arity = max_arity

    @staticmethod
    def arnold_poincare(n: int) -> Dict[int, int]:
        r"""Poincare polynomial of Conf_n(C): P_n(t) = prod_{j=0}^{n-1} (1+jt).

        Returns {degree: Betti number}.
        """
        if n <= 0:
            return {0: 1}
        # Multiply (1 + 0*t)(1 + 1*t)(1 + 2*t)...(1 + (n-1)*t)
        result = {0: 1}
        for j in range(1, n):
            new_result = {}
            for deg, coeff in result.items():
                new_result[deg] = new_result.get(deg, 0) + coeff
                new_result[deg + 1] = new_result.get(deg + 1, 0) + j * coeff
            result = new_result
        return result

    @staticmethod
    def arnold_total_betti(n: int) -> int:
        r"""Total Betti number of Conf_n(C) = n!."""
        return factorial(n)

    def dimension_per_degree(self, arity: int) -> Dict[int, int]:
        r"""Dimension of B_{E_2}^arity(A) per Arnold degree.

        At Arnold degree k, we have:
            dim = betti_k * gen_dim^arity
        (for the naive tensor product; the coinvariant version is smaller).

        This is an UPPER BOUND; the actual dimension may be smaller
        due to S_n coinvariants.  For the free E_2-algebra on generators,
        the exact answer involves the character theory of the Arnold
        representation.
        """
        arnold = self.arnold_poincare(arity)
        result = {}
        for deg, betti in arnold.items():
            result[deg] = betti * self.gen_dim ** arity
        return result

    def total_dimension_upper_bound(self, arity: int) -> int:
        """Upper bound: n! * d^n (before coinvariants)."""
        return factorial(arity) * self.gen_dim ** arity

    def e2_coinvariant_dimension(self, arity: int) -> int:
        r"""Dimension of Lie^c(n) tensor_{S_n} V^{tensor n} (the Lie cooperadic part).

        This is the operadic bar B_{Com}(A) at arity n, computed via
        the necklace polynomial:

            N(n, d) = (1/n) * sum_{j|n} mu(n/j) * d^j

        where mu is the Mobius function.

        This gives the dimension of the COMMUTATIVE bar = Harrison complex
        = cofree Lie coalgebra on V at arity n.
        """
        d = self.gen_dim
        if arity == 0:
            return 1
        if arity == 1:
            return d

        # Necklace polynomial: number of aperiodic necklaces
        # = (1/n) * sum_{j|n} mu(n/j) * d^j
        n = arity
        total = 0
        for j in range(1, n + 1):
            if n % j == 0:
                total += _mobius(n // j) * d ** j
        return total // n


def _mobius(n: int) -> int:
    """Mobius function mu(n)."""
    if n == 1:
        return 1
    # Factor n
    factors = []
    temp = n
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            factors.append(d)
            while temp % d == 0:
                temp //= d
                if temp % d == 0 and d in factors:
                    # d^2 divides n
                    return 0
            if temp > 1:
                pass
        d += 1
    if temp > 1:
        factors.append(temp)

    # Check squarefree
    temp2 = n
    for p in factors:
        if temp2 % (p * p) == 0:
            return 0
        temp2 //= p

    # Squarefree: mu = (-1)^(number of prime factors)
    return (-1) ** len(factors)


def mobius(n: int) -> int:
    """Mobius function mu(n), public interface."""
    if n <= 0:
        raise ValueError(f"Mobius function undefined for n={n}")
    if n == 1:
        return 1
    # Trial division for squarefreeness and prime count
    temp = n
    num_primes = 0
    d = 2
    while d * d <= temp:
        if temp % d == 0:
            num_primes += 1
            temp //= d
            if temp % d == 0:
                return 0  # d^2 divides n
        d += 1
    if temp > 1:
        num_primes += 1
    return (-1) ** num_primes


def necklace_polynomial(n: int, d: int) -> int:
    r"""Number of aperiodic necklaces of length n with d colors.

    N(n, d) = (1/n) * sum_{j | n} mu(n/j) * d^j

    This equals dim(Lie^c(n) tensor_{S_n} V^{tensor n}) for dim(V) = d.
    = dim of arity-n part of the free Lie algebra on d generators.
    """
    if n == 0:
        return 1
    if n == 1:
        return d
    total = 0
    for j in range(1, n + 1):
        if n % j == 0:
            total += mobius(n // j) * d ** j
    return total // n


# ================================================================
# 5. Dimension comparison table
# ================================================================

def dimension_comparison_table(gen_dim: int, max_arity: int = 6,
                               desusp_degree: int = 0) -> Dict[int, Dict[str, int]]:
    r"""Compare dimensions of B_{E_1}^n, B_{E_infty}^n, and B_{Com}^n (Harrison).

    For a commutative algebra with gen_dim generators:
        E_1 bar: d^n (full tensor power)
        E_infty bar (symmetric coalgebra): C(d+n-1, n) or C(d, n)
        Harrison (Lie cooperadic): necklace N(n, d)

    Returns dict {arity: {type: dimension}}.
    """
    e1 = E1BarComplex(gen_dim, max_arity)
    einf = EInfBarComplex(gen_dim, max_arity, desusp_degree)

    table = {}
    for n in range(1, max_arity + 1):
        dim_e1 = e1.dimension(n)
        dim_einf = einf.dimension(n)
        dim_harrison = necklace_polynomial(n, gen_dim)
        ratio_e1_einf = Fraction(dim_e1, dim_einf) if dim_einf > 0 else None
        ratio_e1_harrison = Fraction(dim_e1, dim_harrison) if dim_harrison > 0 else None

        table[n] = {
            'E_1': dim_e1,
            'E_inf_symcoalg': dim_einf,
            'Harrison': dim_harrison,
            'ratio_E1_Einf': ratio_e1_einf,
            'ratio_E1_Harrison': ratio_e1_harrison,
        }
    return table


# ================================================================
# 6. Explicit coproduct comparison at low arities
# ================================================================

def explicit_coproduct_comparison_arity2(gen_dim: int = 2) -> Dict[str, object]:
    r"""Compare E_1 and E_infty coproducts at arity 2 explicitly.

    For A = k[x, y] (gen_dim = 2), arity 2:
        E_1 basis: [x|x], [x|y], [y|x], [y|y]  (dim = 4)
        E_infty basis (desusp even): {x,x}, {x,y}, {y,y}  (dim = 3, symmetric)
        E_infty basis (desusp odd): {x,y}  (dim = 1, exterior)

    Coproduct Delta([a|b]):
        E_1: [] tensor [a|b] + [a] tensor [b] + [a|b] tensor []
             = 1 tensor [a|b] + [a] tensor [b] + [a|b] tensor 1
        E_infty: 1 tensor {a,b} + {a} tensor {b} + {b} tensor {a} + {a,b} tensor 1
                 (with appropriate signs and multiplicities)
    """
    result = {}

    # E_1 at arity 2
    e1 = E1BarComplex(gen_dim)
    e1_basis = e1.basis(2)
    e1_coproducts = {}
    for elem in e1_basis:
        e1_coproducts[elem] = e1.coproduct(elem)
    result['E_1_basis'] = e1_basis
    result['E_1_dim'] = len(e1_basis)
    result['E_1_coproducts'] = e1_coproducts

    # E_infty at arity 2 (even desuspension)
    einf_even = EInfBarComplex(gen_dim, desusp_degree=0)
    einf_even_basis = einf_even.basis(2)
    einf_even_coproducts = {}
    for elem in einf_even_basis:
        einf_even_coproducts[elem] = einf_even.shuffle_coproduct(elem)
    result['Einf_even_basis'] = einf_even_basis
    result['Einf_even_dim'] = len(einf_even_basis)
    result['Einf_even_coproducts'] = einf_even_coproducts

    # E_infty at arity 2 (odd desuspension)
    einf_odd = EInfBarComplex(gen_dim, desusp_degree=1)
    einf_odd_basis = einf_odd.basis(2)
    einf_odd_coproducts = {}
    for elem in einf_odd_basis:
        einf_odd_coproducts[elem] = einf_odd.shuffle_coproduct(elem)
    result['Einf_odd_basis'] = einf_odd_basis
    result['Einf_odd_dim'] = len(einf_odd_basis)
    result['Einf_odd_coproducts'] = einf_odd_coproducts

    return result


# ================================================================
# 7. Heisenberg algebra comparison
# ================================================================

def heisenberg_bar_comparison(max_weight: int = 6) -> Dict[int, Dict[str, int]]:
    r"""Compare B_{E_1} and B_{E_infty} dimensions for the Heisenberg algebra.

    The Heisenberg algebra H_k has generators alpha_{-n} for n >= 1,
    one generator per mode.  At mode n, the generator has conformal
    weight n.  After desuspension: |s^{-1}alpha_{-n}| = n - 1.

    For the bar complex truncated at conformal weight <= max_weight:
        Total number of generators = max_weight (one per mode 1, ..., max_weight).

    The E_1 bar at arity n and total weight w:
        Elements: ordered n-tuples (m_1, ..., m_n) with m_i >= 1, sum = w.
        dim = number of compositions of w into n parts >= 1
            = C(w-1, n-1)

    The E_infty bar at arity n and total weight w:
        The generators have DIFFERENT desuspended degrees (0, 1, 2, ...).
        This is a mixed-degree situation.

    For simplicity, we compute total dimensions at each arity n
    (summing over all weights).

    ACTUALLY: for the Heisenberg algebra, the relevant computation
    is the bar complex of the LOOP algebra.  At weight <= N, we have
    N generators, all of desuspended degree 0 (if they all have weight 1)
    or mixed degrees (for the actual Heisenberg).

    For the pure weight-1 case (e.g., sl_2 at weight 1, dim = 3):
        E_1 dim at arity n = 3^n
        E_infty dim at arity n = C(3+n-1, n) = C(n+2, n)

    Let's compute for the Heisenberg at weight <= N, treating each
    alpha_{-n} as a separate generator.  This gives gen_dim = N.
    But the desuspended degrees are mixed: |s^{-1}alpha_{-n}| = n-1.

    For the E_1 bar: full tensor products, no quotient.
        dim at arity k = N^k (each slot picks one of N generators).

    For the E_infty bar (symmetric coalgebra): we need the symmetric
    algebra of the graded vector space V = <alpha_1, ..., alpha_N>
    with |alpha_n| = n-1.  The Hilbert series of Sym(V) depends on
    the graded structure.

    To keep things clean, we report the single-weight comparison
    (all generators in the same degree).
    """
    table = {}
    for N in range(1, max_weight + 1):
        gen_dim = N
        row = {}
        for arity in range(1, 7):
            dim_e1 = gen_dim ** arity
            # For even desuspended degree generators:
            dim_einf = comb(gen_dim + arity - 1, arity)
            dim_harrison = necklace_polynomial(arity, gen_dim)
            row[arity] = {
                'E_1': dim_e1,
                'E_inf': dim_einf,
                'Harrison': dim_harrison,
                'ratio_E1_Einf': Fraction(dim_e1, dim_einf) if dim_einf > 0 else None,
            }
        table[N] = row
    return table


# ================================================================
# 8. The key theorem: Swiss-cheese decomposition
# ================================================================

def swiss_cheese_analysis() -> Dict[str, object]:
    r"""Analyze the Swiss-cheese structure of the chiral bar complex.

    The chiral bar complex B^ch(A) is a Swiss-cheese coalgebra:
    - Differential d_B: from E_2 (holomorphic, Conf_k(C))
    - Coproduct Delta: from E_1 (topological, Conf_k(R))

    This means B^ch(A) is NOT B_{E_2}(A).  It is B_{SC}(A) where
    SC is the Swiss-cheese operad.

    The dimensional consequences:
    - B_{E_2}(A) would have dim involving Arnold algebra / S_n coinvariants
    - B_{SC}(A) = B_{E_1}(A) as a COALGEBRA (tensor coalgebra structure)
      but with a DIFFERENTIAL that uses E_2 data

    So: the coalgebra structure is E_1, the differential is E_2.
    """
    result = {
        'differential_source': 'E_2 (holomorphic, Conf_k(C))',
        'coproduct_source': 'E_1 (topological, Conf_k(R))',
        'operad': 'SC^{ch,top} (Swiss-cheese)',
        'coalgebra_type': 'coassociative (NOT cocommutative)',
        'explanation': (
            'A chiral algebra A on C is E_infty-chiral (commutative OPE), '
            'but the bar complex B^ch(A) carries an E_1 coproduct from the '
            'R-direction ordering.  The E_2 structure contributes ONLY to '
            'the differential (collision residues on Conf_k(C)).  The coproduct '
            'is the deconcatenation Delta on the ordered tensor coalgebra, '
            'corresponding to cutting the R-line at a point.  '
            'This is the Swiss-cheese operad SC^{ch,top}: differential from '
            'the closed (holomorphic) color, coproduct from the open '
            '(topological) color.'
        ),
        'consequence_for_quantum_groups': (
            'The non-cocommutative E_1 coproduct is ESSENTIAL for the '
            'R-matrix / quantum group structure.  If one took the E_2 or '
            'E_infty bar instead, one would lose the ordered tensor structure '
            'and hence the non-commutative part of the quantum group.  '
            'The classical r-matrix r(z) is the image under the '
            'symmetrization map B_{E_1} -> B_{E_infty}; the full quantum '
            'R-matrix R(z) = 1 + r(z)/z + ... has non-symmetric corrections '
            'that live in the kernel of this map.'
        ),
    }
    return result


# ================================================================
# 9. Coproduct type classification by n
# ================================================================

def en_coproduct_classification() -> Dict[str, Dict[str, str]]:
    r"""Classification of B_{E_n}(A) coproduct type by n.

    Returns a table of properties for each n.
    """
    return {
        'n=1 (Ass)': {
            'underlying_space': 'T^c(s^{-1}\\bar{A}) (tensor coalgebra)',
            'coproduct': 'Deconcatenation: Delta([a_1|...|a_n]) = sum [a_1|...|a_i] tensor [a_{i+1}|...|a_n]',
            'coassociative': 'YES',
            'cocommutative': 'NO',
            'coalgebra_type': 'cofree Ass-coalgebra',
            'dual_operad': 'Ass^! = Ass (self-dual)',
            'dimension_arity_n': 'd^n',
            'configuration_space': 'Conf_k(R) = contractible (ordered simplex)',
            'propagator_degree': '0 (no propagator; R \\ {0} = two points)',
        },
        'n=2 (E_2)': {
            'underlying_space': 'E_2^{!,c}(s^{-1}\\bar{A}) (cofree E_2{-2}-coalgebra)',
            'coproduct': 'E_2 coalgebra: coassociative + homotopy-cocommutative',
            'coassociative': 'YES (E_1 subset E_2)',
            'cocommutative': 'NO (only homotopy-cocommutative)',
            'coalgebra_type': 'cofree E_2{-2}-coalgebra',
            'dual_operad': 'E_2^! = E_2{-2}',
            'dimension_arity_n': 'n! * d^n / (S_n coinvariants) -- uses Arnold algebra H*(Conf_k(C))',
            'configuration_space': 'Conf_k(C): Arnold algebra, P(t) = prod(1+jt)',
            'propagator_degree': '1 (from S^1 = R^2 \\ {0})',
        },
        'n=3 (E_3)': {
            'underlying_space': 'E_3^{!,c}(s^{-1}\\bar{A}) (cofree E_3{-3}-coalgebra)',
            'coproduct': 'E_3 coalgebra: coassociative + homotopy-cocommutative (stronger than E_2)',
            'coassociative': 'YES',
            'cocommutative': 'NO (homotopy-cocommutative up to S^2 parameter)',
            'coalgebra_type': 'cofree E_3{-3}-coalgebra',
            'dual_operad': 'E_3^! = E_3{-3}',
            'dimension_arity_n': 'uses H*(Conf_k(R^3)): generators in degree 2',
            'configuration_space': 'Conf_k(R^3): P(t) = prod(1+jt^2), total Betti = n!',
            'propagator_degree': '2 (from S^2 = R^3 \\ {0})',
        },
        'n=inf (Com)': {
            'underlying_space': 'Lie^c(s^{-1}\\bar{A}) (cofree Lie-coalgebra = Harrison complex)',
            'coproduct': 'Lie COBRACKET (NOT a coassociative coproduct)',
            'coassociative': 'NO (Lie cobracket satisfies co-Jacobi, not coassociativity)',
            'cocommutative': 'N/A (coantisymmetric under co-Jacobi)',
            'coalgebra_type': 'cofree Lie-coalgebra',
            'dual_operad': 'Com^! = Lie',
            'dimension_arity_n': 'necklace(n, d) = (1/n) * sum_{j|n} mu(n/j) * d^j',
            'configuration_space': 'Conf_k(R^inf) = contractible (no cohomology above degree 0)',
            'propagator_degree': 'infinite (S^inf contractible; no propagator)',
            'note': (
                'IMPORTANT: The operadic bar B_{Com}(A) is a Lie COALGEBRA, '
                'not a cocommutative coalgebra.  The cocommutative coalgebra '
                '(symmetric coalgebra) is the CE complex, which is a different '
                'model computing the same cohomology in char 0.'
            ),
        },
    }


# ================================================================
# 10. Explicit polynomial algebra computation
# ================================================================

def polynomial_algebra_bar(d: int = 2, max_arity: int = 4) -> Dict[str, object]:
    r"""Compute B_{E_1} and B_{E_infty} for A = k[x_1, ..., x_d].

    For A = k[x_1, ..., x_d], the augmentation ideal is
    \bar{A} = A_+ = span{x^alpha : |alpha| >= 1}.

    Truncating to generators of degree 1 (the x_i themselves):
        B_{E_1}^n: ordered n-tuples of generators, dim = d^n.
        B_{E_infty}^n: unordered multisets of generators, dim = C(d+n-1, n).

    Returns detailed comparison at each arity.
    """
    result = {}
    e1 = E1BarComplex(d, max_arity)
    einf = EInfBarComplex(d, max_arity, desusp_degree=0)

    for n in range(1, max_arity + 1):
        e1_basis = e1.basis(n)
        einf_basis = einf.basis(n)

        # Compute all E_1 coproducts
        e1_coprod_count = 0
        for elem in e1_basis:
            e1_coprod_count += len(e1.coproduct(elem))

        # Compute all E_infty coproducts
        einf_coprod_count = 0
        for elem in einf_basis:
            einf_coprod_count += len(einf.shuffle_coproduct(elem))

        result[n] = {
            'E_1_dim': len(e1_basis),
            'E_inf_dim': len(einf_basis),
            'Harrison_dim': necklace_polynomial(n, d),
            'ratio': Fraction(len(e1_basis), len(einf_basis)),
            'E_1_total_coproduct_terms': e1_coprod_count,
            'E_inf_total_coproduct_terms': einf_coprod_count,
        }

    return result


# ================================================================
# 11. Verification utilities
# ================================================================

def verify_all_axioms(gen_dim: int = 2, max_arity: int = 4) -> Dict[str, bool]:
    r"""Verify all coalgebra axioms at each arity.

    Returns dict of test results.
    """
    e1 = E1BarComplex(gen_dim, max_arity)
    einf = EInfBarComplex(gen_dim, max_arity, desusp_degree=0)

    results = {}
    for n in range(2, max_arity + 1):
        results[f'E_1_coassoc_arity{n}'] = e1.verify_coassociativity(n)
        results[f'E_1_non_cocomm_arity{n}'] = e1.verify_non_cocommutativity(n)
        results[f'Einf_coassoc_arity{n}'] = einf.verify_coassociativity(n)
        results[f'Einf_cocomm_arity{n}'] = einf.verify_cocommutativity(n)

    return results


# ================================================================
# 12. Summary of the chiral bar complex situation
# ================================================================

def chiral_bar_summary() -> str:
    r"""Summary of why the chiral bar has E_1 coproduct, not E_infty.

    This is the answer to the motivating question of this module.
    """
    return """
THE CHIRAL BAR COPRODUCT: A SUMMARY
====================================

Question: A chiral algebra A is E_infty-chiral (commutative OPE).
Why does B^ch(A) carry an E_1 (coassociative, non-cocommutative)
coproduct rather than an E_infty (cocommutative) coproduct?

Answer: The bar complex is NOT B_{E_infty}(A).  It is a SWISS-CHEESE
construction B_{SC^{ch,top}}(A), where:

  - The DIFFERENTIAL uses E_2 (holomorphic) data:
    collision residues on Conf_k(C).

  - The COPRODUCT uses E_1 (topological) data:
    deconcatenation = interval-splitting on Conf_k(R).

The Swiss-cheese operad SC^{ch,top} has two colors:
  closed (holomorphic, contributing to the differential)
  open (topological, contributing to the coproduct)

Why E_1 and not E_2 for the coproduct?
The coproduct comes from the R-direction in C x R.  Points on R
are ORDERED (t_1 < ... < t_n), so the coproduct preserves this
ordering: it cuts the interval [t_1, t_n] at some t_i and
produces an ordered left piece and an ordered right piece.
This is deconcatenation, which is E_1 (coassociative, non-cocommutative).

Why is the ordering physical?
In the 3D holomorphic-topological QFT on C x R:
  - C is the holomorphic direction (chiral algebra = surface observables)
  - R is the topological direction (associative = line observables)
  - The R-ordering determines the QUANTUM GROUP structure:
    the R-matrix R(z) in End(V tensor V) REQUIRES ordered tensor products.
    The non-cocommutative part R(z) - tau(R(z)) encodes the
    quantum group data beyond the classical r-matrix.

What would happen with E_infty coproduct?
If we took B_{E_infty}(A) instead (= Lie cooperadic bar = Harrison complex),
we would lose:
  1. The R-matrix (lives in ordered tensors)
  2. The quantum group (requires non-cocommutative coproduct)
  3. The Yang-Baxter equation (needs ordered triple tensor products)
  4. The modular data at higher genus (Swiss-cheese is essential)

The CLASSICAL r-matrix r(z) is the symmetrization of R(z):
it lives in the E_infty quotient.  But the full quantum R-matrix,
and hence the full quantum group, requires the E_1 structure.

Dimensional comparison for the Heisenberg with N generators:
  B_{E_1}^n: dim = N^n
  B_{E_infty}^n: dim = C(N+n-1, n)  (symmetric coalgebra)
  Harrison: dim = necklace(n, N)     (Lie cooperadic bar)

  Ratio E_1/E_infty = N^n / C(N+n-1, n) ~ n! for large N.

The E_1 bar is n! TIMES LARGER than the symmetric coalgebra at large N.
This extra data is EXACTLY the quantum group structure.
"""


# ================================================================
# 13. The operadic Koszul duality table
# ================================================================

def operadic_koszul_table() -> Dict[str, Dict[str, str]]:
    r"""Summary of P^! for each operad and the resulting bar structure.

    This is the mathematical core: the coproduct on B_P(A)
    is determined by the Koszul dual cooperad P^{!,c}.
    """
    return {
        'P = Ass (E_1)': {
            'P^!': 'Ass',
            'P^{!,c}': 'Ass^c',
            'B_P(A)': 'T^c(s^{-1}bar{A}) = cofree Ass-coalgebra',
            'coproduct_name': 'Deconcatenation',
            'coproduct_formula': 'Delta([a_1|...|a_n]) = sum_{i=0}^n [a_1|...|a_i] tensor [a_{i+1}|...|a_n]',
            'coassociative': True,
            'cocommutative': False,
        },
        'P = Com (E_inf)': {
            'P^!': 'Lie',
            'P^{!,c}': 'Lie^c',
            'B_P(A)': 'Lie^c(s^{-1}bar{A}) = cofree Lie-coalgebra (Harrison complex)',
            'coproduct_name': 'Lie cobracket',
            'coproduct_formula': 'delta(x) = sum [x_i, x_j]^c (coantisymmetric, co-Jacobi)',
            'coassociative': False,  # Lie cobracket is NOT coassociative
            'cocommutative': False,  # it's coANTIsymmetric
        },
        'P = Lie': {
            'P^!': 'Com',
            'P^{!,c}': 'Com^c = Sym^c',
            'B_P(A)': 'Sym^c(s^{-1}bar{A}) = cofree Com-coalgebra (CE complex)',
            'coproduct_name': 'Shuffle coproduct',
            'coproduct_formula': 'Delta(a_1...a_n) = sum_{S} a_S tensor a_{[n]\\S} with Koszul signs',
            'coassociative': True,
            'cocommutative': True,
        },
        'P = E_2': {
            'P^!': 'E_2{-2}',
            'P^{!,c}': 'E_2{-2}^c',
            'B_P(A)': 'E_2{-2}^c(s^{-1}bar{A}) = cofree E_2{-2}-coalgebra',
            'coproduct_name': 'E_2 coalgebra (braided)',
            'coproduct_formula': 'Coassociative + braided homotopy cocommutativity from pi_1(S^1) = Z',
            'coassociative': True,
            'cocommutative': False,  # only homotopy-cocommutative
        },
        'P = E_n (general)': {
            'P^!': 'E_n{-n}',
            'P^{!,c}': 'E_n{-n}^c',
            'B_P(A)': 'E_n{-n}^c(s^{-1}bar{A}) = cofree E_n{-n}-coalgebra',
            'coproduct_name': f'E_n coalgebra',
            'coproduct_formula': 'Interpolates between Ass (n=1) and Lie (n=inf)',
            'coassociative': True,  # E_n contains E_1 for all n >= 1
            'cocommutative': False,  # only for n = inf
        },
    }


# ================================================================
# 14. Arnold algebra dimensions for E_2 bar comparison
# ================================================================

def arnold_betti_numbers(n: int) -> Dict[int, int]:
    r"""Betti numbers of Conf_n(C).

    H^k(Conf_n(C)) has dimension = unsigned Stirling number |s(n, n-k)|.
    Poincare polynomial: P_n(t) = prod_{j=0}^{n-1} (1 + jt).
    """
    return E2BarComplex.arnold_poincare(n)


def e2_vs_e1_dimension_ratio(gen_dim: int, max_arity: int = 6) -> Dict[int, Dict[str, object]]:
    r"""Compare E_2 and E_1 bar dimensions.

    The E_2 bar at arity n uses Arnold algebra data:
        B_{E_2}^n involves H*(Conf_n(C)) tensor (s^{-1}V)^{tensor n} / S_n.

    Upper bound on E_2 dimension: n! * d^n (before coinvariants).
    This equals the E_1 dimension times n!.

    But the S_n coinvariants bring it down.  For the OPERADIC bar
    B_{E_2}(A), the arity-n component has dimension:
        sum_k b_k(Conf_n(C)) * dim(S_n-coinvariants of appropriate tensor)

    For the free E_2-algebra, this is more subtle.  We report bounds.
    """
    table = {}
    for n in range(1, max_arity + 1):
        d = gen_dim
        dim_e1 = d ** n
        arnold_total = factorial(n)  # sum of Betti = n!
        upper_bound = arnold_total * d ** n  # before coinvariants
        harrison = necklace_polynomial(n, d)

        table[n] = {
            'E_1_dim': dim_e1,
            'Arnold_total_Betti': arnold_total,
            'E_2_upper_bound': upper_bound,
            'Harrison_dim': harrison,
            'E_2_over_E_1_upper': Fraction(upper_bound, dim_e1),
            'note': f'E_2 dim is between Harrison ({harrison}) and E_1*n! ({upper_bound})',
        }
    return table
