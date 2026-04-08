"""Two-coloured operadic bar construction for the Swiss-cheese operad.

THE FUNDAMENTAL QUESTION: For a two-coloured operad O with colours
{c, o} (closed, open), what is the bar construction B_O of an
O-algebra (V_c, V_o)?

ANSWER (worked out from first principles in this module):

1. CLASSICAL ONE-COLOURED BAR:
   - B_{Ass}(A) = (T^c(s^{-1} A_bar), d_bar) is a coassociative dg
     coalgebra. Here T^c is the cofree tensor coalgebra, s^{-1} is
     desuspension, A_bar = ker(augmentation).
   - B_{Com}(A) = (Sym^c(s^{-1} A_bar), d_bar) is a cocommutative
     (= coLie) dg coalgebra.

2. TWO-COLOURED BAR (Swiss-cheese):
   An SC-algebra is a pair (C, A) where:
     - C is a Com-algebra (closed colour)
     - A is an Ass-algebra (open colour)
     - C acts on A via a Com-module structure (closed-to-open maps)
   The bar construction B_{SC}(C, A) is a two-coloured dg cooperad
   coalgebra with:
     - Closed component: B_{Com}(C) (coLie coalgebra)
     - Open component: B_{Ass}(A) (coAss coalgebra)
     - Mixed structure: the C-action on A induces comodule maps

3. THE PROMOTION FUNCTOR (key insight):
   Given ONLY a Com-algebra C, there is a canonical SC-algebra:
     (C, C) where C acts on itself by multiplication.
   The bar B_{SC}(C, C) then has:
     - Closed part: B_{Com}(C) -- the commutative bar
     - Open part: B_{Ass}(C) -- the associative bar of C
     - Mixed: the action of C on itself by multiplication
   This is exactly what happens for chiral algebras: B^ch(A) is
   ALREADY an SC-coalgebra because the bar differential (closed, from
   FM_k(C)) and the deconcatenation coproduct (open, from Conf_k(R))
   are independent structures on the SAME underlying tensor coalgebra.

4. THE TYPE-CHECKING RESOLUTION:
   A chiral algebra A is a Com^ch-algebra (one-coloured). To get
   an SC^{ch,top}-coalgebra, we do NOT need a separate open input.
   The bar construction B^ch(A) = T^c(s^{-1} A_bar) carries:
     - d_C from FM_k(C): the closed structure
     - Delta from Conf_k(R): the open structure (deconcatenation)
   These COMMUTE (d_C is a coderivation of Delta) because
   FM_k(C) x Conf_k(R) is a product.

   The open-colour data is PRODUCED by the bar construction, not
   assumed as input. This is the content of thm:bar-swiss-cheese.

MATHEMATICAL FRAMEWORK (Loday-Vallette, Chapter 13):

For a coloured operad P with colours I = {c, o}, the bar construction
of a P-algebra V = (V_c, V_o) is:
  B_P(V) = (P^i(s^{-1} V_bar), d)
where P^i is the Koszul dual cooperad and d combines the internal
differential with the cooperad cocomposition twisted by the P-algebra
structure on V.

For P = SC (Swiss-cheese):
  SC^i has components indexed by (input colours; output colour):
    SC^i((c,...,c); c) = Com^i = coLie cooperad
    SC^i((c^k, o^m); o) = Com^i(k) tensor Ass^i(m)
    SC^i(...,o,...; c) = 0  (no open-to-closed)

So B_{SC}(V_c, V_o) decomposes:
  - Output colour c: cofree coLie on s^{-1} V_c
    = B_{Com}(V_c), the Chevalley-Eilenberg complex
  - Output colour o: mixed cofree construction on s^{-1}V_c, s^{-1}V_o
    involves both colours as inputs, with Ass-coalgebra in the open
    slots and Com-coalgebra in the closed slots

CONVENTIONS:
  - Cohomological grading, |d| = +1
  - Bar uses DESUSPENSION: |s^{-1}v| = |v| - 1
  - Com^! = Lie (NOT coLie), so B_{Com} produces coLie
  - Koszul sign: swapping deg p and deg q gives (-1)^{pq}

References:
  Loday-Vallette, "Algebraic Operads" Ch 13 (coloured operads)
  Voronov, "The Swiss-cheese operad" (1999)
  thm:bar-swiss-cheese (en_koszul_duality.tex)
  def:SC (en_koszul_duality.tex)
  constr:sc-operation-space (ordered_associative_chiral_kd.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import combinations, permutations, product as cartprod
from math import factorial
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import Matrix, Rational, Symbol, zeros, eye, simplify


# =========================================================================
#  PART 1: Graded vector spaces and elements
# =========================================================================

@dataclass(frozen=True)
class BasisElement:
    """A basis element of a graded vector space."""
    name: str
    degree: int

    def __repr__(self) -> str:
        return f"{self.name}[{self.degree}]"


@dataclass
class GradedSpace:
    """A finite-dimensional graded vector space over Q."""
    basis: List[BasisElement]
    name: str = ""

    @property
    def dim(self) -> int:
        return len(self.basis)

    def element_index(self, name: str) -> int:
        for i, b in enumerate(self.basis):
            if b.name == name:
                return i
        raise ValueError(f"No basis element named {name}")

    def desuspend(self) -> "GradedSpace":
        """Apply desuspension s^{-1}: lower degree by 1."""
        new_basis = [
            BasisElement(f"s^{{-1}}{b.name}", b.degree - 1)
            for b in self.basis
        ]
        return GradedSpace(new_basis, f"s^{{-1}}({self.name})")


# =========================================================================
#  Linear combination (sparse vector)
# =========================================================================

# A vector is Dict[int, Rational] mapping basis index to coefficient
Vector = Dict[int, Rational]


def vec_add(v1: Vector, v2: Vector) -> Vector:
    """Add two sparse vectors."""
    result = dict(v1)
    for k, c in v2.items():
        result[k] = result.get(k, Rational(0)) + c
    return {k: v for k, v in result.items() if v != 0}


def vec_scale(c: Rational, v: Vector) -> Vector:
    """Scale a vector."""
    if c == 0:
        return {}
    return {k: c * val for k, val in v.items() if c * val != 0}


def vec_zero() -> Vector:
    return {}


# =========================================================================
#  PART 2: Augmented associative algebra
# =========================================================================

@dataclass
class AugAssAlgebra:
    """Augmented associative algebra over Q.

    The unit is basis element 0. The augmentation ideal A_bar
    is spanned by basis elements 1, ..., dim-1.
    """
    space: GradedSpace
    # mult[(i,j)] = {k: coeff} for m_2(e_i, e_j) = sum coeff * e_k
    mult: Dict[Tuple[int, int], Vector]
    name: str = ""

    @property
    def dim(self) -> int:
        return self.space.dim

    @property
    def aug_ideal_dim(self) -> int:
        """Dimension of augmentation ideal (exclude unit)."""
        return self.dim - 1

    def multiply(self, i: int, j: int) -> Vector:
        return dict(self.mult.get((i, j), {}))

    def is_associative(self) -> bool:
        """Check associativity on all triples."""
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    # (e_i * e_j) * e_k
                    ij = self.multiply(i, j)
                    lhs: Vector = {}
                    for m, c1 in ij.items():
                        mk = self.multiply(m, k)
                        for n, c2 in mk.items():
                            lhs[n] = lhs.get(n, Rational(0)) + c1 * c2

                    # e_i * (e_j * e_k)
                    jk = self.multiply(j, k)
                    rhs: Vector = {}
                    for m, c1 in jk.items():
                        im = self.multiply(i, m)
                        for n, c2 in im.items():
                            rhs[n] = rhs.get(n, Rational(0)) + c1 * c2

                    lhs = {k: v for k, v in lhs.items() if v != 0}
                    rhs = {k: v for k, v in rhs.items() if v != 0}
                    if lhs != rhs:
                        return False
        return True

    def is_commutative(self) -> bool:
        """Check commutativity on all pairs."""
        for i in range(self.dim):
            for j in range(self.dim):
                ij = self.multiply(i, j)
                ji = self.multiply(j, i)
                ij_clean = {k: v for k, v in ij.items() if v != 0}
                ji_clean = {k: v for k, v in ji.items() if v != 0}
                if ij_clean != ji_clean:
                    return False
        return True

    def aug_ideal_multiply(self, i: int, j: int) -> Vector:
        """Multiply in the augmentation ideal.

        i, j are indices in A_bar (0-indexed from the aug ideal,
        so actual basis index is i+1, j+1).
        Returns coefficients in A_bar basis (shifted by -1).
        """
        actual_i = i + 1
        actual_j = j + 1
        result = self.multiply(actual_i, actual_j)
        # Project to augmentation ideal (remove unit component)
        return {k - 1: v for k, v in result.items() if k > 0 and v != 0}


# =========================================================================
#  PART 3: Standard algebras
# =========================================================================

def polynomial_algebra(n: int) -> AugAssAlgebra:
    """Truncated polynomial algebra k[x]/(x^n).

    Basis: 1 (unit), x, x^2, ..., x^{n-1}.
    All in degree 0. Augmentation: x -> 0.
    """
    basis = [BasisElement("1", 0)] + [
        BasisElement(f"x^{i}" if i > 1 else "x", 0)
        for i in range(1, n)
    ]
    space = GradedSpace(basis, f"k[x]/(x^{n})")
    mult: Dict[Tuple[int, int], Vector] = {}
    for i in range(n):
        for j in range(n):
            if i + j < n:
                mult[(i, j)] = {i + j: Rational(1)}
    return AugAssAlgebra(space, mult, f"k[x]/(x^{n})")


def dual_numbers() -> AugAssAlgebra:
    """Dual numbers k[eps]/(eps^2). Basis: {1, eps}, eps^2 = 0."""
    return polynomial_algebra(2)


def exterior_algebra_1() -> AugAssAlgebra:
    """Exterior algebra Lambda(V) on one generator.

    Basis: {1 (deg 0), xi (deg 1)}. xi^2 = 0.
    This is commutative in the graded sense: xi*xi = -xi*xi = 0.
    """
    basis = [BasisElement("1", 0), BasisElement("xi", 1)]
    space = GradedSpace(basis, "Lambda(1)")
    mult: Dict[Tuple[int, int], Vector] = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        (1, 0): {1: Rational(1)},
        # (1,1) absent: xi^2 = 0
    }
    return AugAssAlgebra(space, mult, "Lambda(1)")


def symmetric_algebra_truncated(n: int) -> AugAssAlgebra:
    """Sym(V) truncated at degree n, V one-dimensional in degree 0.

    Same as polynomial_algebra(n) but explicitly marked commutative.
    """
    return polynomial_algebra(n)


def matrix_algebra_2x2_upper() -> AugAssAlgebra:
    """Upper triangular 2x2 matrices. Non-commutative.

    Basis: e_11 (unit), e_12, e_22.
    e_11*e_12 = e_12, e_12*e_22 = e_12, e_22*e_22 = e_22.
    Augmentation: e_ij -> delta_{ij}.
    """
    basis = [
        BasisElement("e_11", 0),  # unit
        BasisElement("e_12", 0),
        BasisElement("e_22", 0),
    ]
    space = GradedSpace(basis, "UT_2")
    mult: Dict[Tuple[int, int], Vector] = {
        (0, 0): {0: Rational(1)},  # e_11^2 = e_11
        (0, 1): {1: Rational(1)},  # e_11*e_12 = e_12
        (0, 2): {2: Rational(1)},  # e_11*e_22 = 0? No: e_11*e_22 = 0
        (1, 2): {1: Rational(1)},  # e_12*e_22 = e_12
        (2, 2): {2: Rational(1)},  # e_22^2 = e_22
    }
    # Correct: e_11 is the unit, so e_11*anything = anything if it starts
    # with column 1. Actually for upper triangular:
    # e_11*e_11 = e_11, e_11*e_12 = e_12, e_11*e_22 = 0
    # e_12*e_11 = 0, e_12*e_12 = 0, e_12*e_22 = e_12
    # e_22*e_11 = 0, e_22*e_12 = 0, e_22*e_22 = e_22
    # But with augmentation at e_11 = unit:
    mult = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        # (0, 2): {} -- e_11*e_22 = 0
        # (1, 0): {} -- e_12*e_11 = 0
        # (1, 1): {} -- e_12*e_12 = 0
        (1, 2): {1: Rational(1)},
        # (2, 0): {} -- e_22*e_11 = 0
        # (2, 1): {} -- e_22*e_12 = 0
        (2, 2): {2: Rational(1)},
    }
    return AugAssAlgebra(space, mult, "UT_2")


# =========================================================================
#  PART 4: The associative bar construction B_{Ass}(A)
# =========================================================================

@dataclass(frozen=True)
class BarWord:
    """A bar word [s^{-1}a_1 | ... | s^{-1}a_n] in the tensor coalgebra.

    indices: tuple of indices into the augmentation ideal basis.
    Bar degree = len(indices).
    """
    indices: Tuple[int, ...]

    @property
    def degree(self) -> int:
        """Bar degree = tensor length."""
        return len(self.indices)

    def __repr__(self) -> str:
        if not self.indices:
            return "[]"
        return "[" + "|".join(str(i) for i in self.indices) + "]"


def bar_words_at_degree(n: int, aug_dim: int) -> List[BarWord]:
    """All bar words of bar degree n over an augmentation ideal of given dim."""
    if n == 0:
        return [BarWord(())]
    result = []
    for indices in cartprod(range(aug_dim), repeat=n):
        result.append(BarWord(indices))
    return result


@dataclass
class AssociativeBarComplex:
    """The associative bar construction B_{Ass}(A).

    B_{Ass}(A) = (T^c(s^{-1} A_bar), d_bar) where:
    - T^c is the cofree tensor coalgebra
    - d_bar contracts consecutive pairs via multiplication in A_bar
    - d_bar^2 = 0 when A is associative

    The deconcatenation coproduct Delta is the coassociative structure:
    Delta[a_1|...|a_n] = sum_{i=0}^n [a_1|...|a_i] tensor [a_{i+1}|...|a_n]
    """
    algebra: AugAssAlgebra
    max_degree: int  # truncation

    def bar_differential(self, word: BarWord) -> Dict[BarWord, Rational]:
        """Compute d_bar on a bar word.

        d_bar[a_1|...|a_n] = sum_{i=1}^{n-1} +/- [a_1|...|a_i*a_{i+1}|...|a_n]

        Sign: (-1)^{sum_{j<=i} (|a_j|+1)} before contracting at position i.
        For degree-0 generators: sign is (-1)^i.
        """
        n = word.degree
        if n <= 1:
            return {}

        result: Dict[BarWord, Rational] = {}
        for i in range(n - 1):
            # Contract positions i and i+1
            a_i = word.indices[i]
            a_ip1 = word.indices[i + 1]
            product = self.algebra.aug_ideal_multiply(a_i, a_ip1)

            # Koszul sign from desuspended elements
            # |s^{-1}a_j| = |a_j| - 1 for each generator
            # The sign for contracting at position i is
            # (-1)^{sum_{j=0}^{i-1} |s^{-1}a_j| + 1}
            # For degree-0 generators: |s^{-1}a_j| = -1, so
            # sum = i*(-1) = -i, and sign = (-1)^{-i+1} ...
            # Actually, simpler: in the standard convention,
            # d[a1|...|an] = sum_i (-1)^i [a1|...|a_i*a_{i+1}|...|an]
            # for degree-0 elements. This is the Hochschild sign.
            sign = Rational((-1) ** i)

            for k, coeff in product.items():
                new_indices = word.indices[:i] + (k,) + word.indices[i + 2:]
                new_word = BarWord(new_indices)
                old = result.get(new_word, Rational(0))
                result[new_word] = old + sign * coeff

        return {k: v for k, v in result.items() if v != 0}

    def deconcatenation(self, word: BarWord) -> List[Tuple[BarWord, BarWord]]:
        """Deconcatenation coproduct: the coassociative structure.

        Delta[a_1|...|a_n] = sum_{i=0}^n [a_1|...|a_i] tensor [a_{i+1}|...|a_n]
        """
        n = word.degree
        result = []
        for i in range(n + 1):
            left = BarWord(word.indices[:i])
            right = BarWord(word.indices[i:])
            result.append((left, right))
        return result

    def verify_d_squared_zero(self, max_bar_degree: int = None) -> bool:
        """Verify d^2 = 0 on all bar words up to given degree."""
        if max_bar_degree is None:
            max_bar_degree = self.max_degree
        aug_dim = self.algebra.aug_ideal_dim

        for n in range(2, max_bar_degree + 1):
            words = bar_words_at_degree(n, aug_dim)
            for w in words:
                d_w = self.bar_differential(w)
                d2_w: Dict[BarWord, Rational] = {}
                for w2, c2 in d_w.items():
                    d_w2 = self.bar_differential(w2)
                    for w3, c3 in d_w2.items():
                        old = d2_w.get(w3, Rational(0))
                        d2_w[w3] = old + c2 * c3
                d2_w = {k: v for k, v in d2_w.items() if v != 0}
                if d2_w:
                    return False
        return True

    def verify_d_is_coderivation(self, max_bar_degree: int = None) -> bool:
        """Verify d_bar is a coderivation of Delta.

        This means: Delta(d(x)) = (d tensor id + id tensor d)(Delta(x))
        for all x.
        """
        if max_bar_degree is None:
            max_bar_degree = self.max_degree
        aug_dim = self.algebra.aug_ideal_dim

        for n in range(1, max_bar_degree + 1):
            words = bar_words_at_degree(n, aug_dim)
            for w in words:
                # LHS: Delta(d(w))
                d_w = self.bar_differential(w)
                lhs: Dict[Tuple[BarWord, BarWord], Rational] = {}
                for dw, c in d_w.items():
                    for left, right in self.deconcatenation(dw):
                        pair = (left, right)
                        old = lhs.get(pair, Rational(0))
                        lhs[pair] = old + c

                # RHS: (d tensor id + id tensor d)(Delta(w))
                rhs: Dict[Tuple[BarWord, BarWord], Rational] = {}
                for left, right in self.deconcatenation(w):
                    # d(left) tensor right
                    d_left = self.bar_differential(left)
                    for dl, c in d_left.items():
                        pair = (dl, right)
                        old = rhs.get(pair, Rational(0))
                        rhs[pair] = old + c
                    # left tensor d(right)
                    d_right = self.bar_differential(right)
                    for dr, c in d_right.items():
                        # Sign: (-1)^{|left|} for passing d through left
                        # For bar words, the total degree of a bar word
                        # [a1|...|ak] with all |a_i|=0 is k*(0-1) = -k
                        # i.e. cohomological degree = -k (using desuspension).
                        # Sign = (-1)^{deg(left)} = (-1)^{-left.degree}
                        # = (-1)^{left.degree} (since (-1)^{-n} = (-1)^n).
                        sign = Rational((-1) ** left.degree)
                        pair = (left, dr)
                        old = rhs.get(pair, Rational(0))
                        rhs[pair] = old + sign * c

                # Compare
                lhs_clean = {k: v for k, v in lhs.items() if v != 0}
                rhs_clean = {k: v for k, v in rhs.items() if v != 0}
                if lhs_clean != rhs_clean:
                    return False
        return True

    def bar_cohomology_dims(self, max_bar_degree: int = None) -> Dict[int, int]:
        """Compute dim H^n(B(A)) at each bar degree.

        Returns {bar_degree: dim of cohomology}.
        """
        if max_bar_degree is None:
            max_bar_degree = self.max_degree
        aug_dim = self.algebra.aug_ideal_dim
        if aug_dim == 0:
            return {n: 0 for n in range(max_bar_degree + 1)}

        dims = {}
        for n in range(max_bar_degree + 1):
            words_n = bar_words_at_degree(n, aug_dim)
            if n == 0:
                # Bar degree 0: the ground field. Kernel of d: everything.
                # Image of d from degree 1.
                words_1 = bar_words_at_degree(1, aug_dim)
                image_dim = 0
                # d maps degree 1 -> degree 0, but degree 0 = ground field
                # and d on degree 1 words [a] = 0 (no consecutive pairs).
                # So image = 0.
                dims[0] = 1  # H^0 = k (ground field)
                continue

            dim_n = len(words_n)
            if dim_n == 0:
                dims[n] = 0
                continue

            # Build d: degree n -> degree n-1 as matrix
            words_nm1 = bar_words_at_degree(n - 1, aug_dim)
            if not words_nm1:
                # d maps to 0
                kernel_dim = dim_n
                # image from degree n+1
                if n < max_bar_degree:
                    words_np1 = bar_words_at_degree(n + 1, aug_dim)
                    M_out = self._differential_matrix(words_np1, words_n)
                    image_dim = M_out.rank()
                else:
                    image_dim = 0
                dims[n] = kernel_dim - image_dim
                continue

            M = self._differential_matrix(words_n, words_nm1)
            kernel_dim = dim_n - M.rank()

            # Image from degree n+1
            if n < max_bar_degree:
                words_np1 = bar_words_at_degree(n + 1, aug_dim)
                M_out = self._differential_matrix(words_np1, words_n)
                image_dim = M_out.rank()
            else:
                image_dim = 0

            dims[n] = kernel_dim - image_dim

        return dims

    def _differential_matrix(
        self,
        source_words: List[BarWord],
        target_words: List[BarWord],
    ) -> Matrix:
        """Build the matrix of d from source bar degree to target."""
        if not source_words or not target_words:
            return zeros(len(target_words), len(source_words))

        target_index = {w: i for i, w in enumerate(target_words)}
        rows = len(target_words)
        cols = len(source_words)
        M = zeros(rows, cols)

        for j, w in enumerate(source_words):
            d_w = self.bar_differential(w)
            for w2, c in d_w.items():
                if w2 in target_index:
                    i = target_index[w2]
                    M[i, j] += c

        return M


# =========================================================================
#  PART 5: The commutative bar construction B_{Com}(A)
# =========================================================================

@dataclass(frozen=True)
class SymBarWord:
    """An element of coLie^c_n(s^{-1}V) for the commutative bar complex.

    For generators in degree 0, desuspension gives degree -1.
    The graded-symmetric product of degree -1 elements is the
    EXTERIOR product (antisymmetric in naive sense), because
    (-1)^{(-1)(-1)} = -1.  So coLie^c_n(s^{-1}V) = Lambda^n(s^{-1}V)
    when V is concentrated in degree 0.

    Represented as a strictly increasing tuple (canonical form for
    exterior power basis elements).
    """
    indices: Tuple[int, ...]

    @staticmethod
    def from_unsorted(idx: Tuple[int, ...]) -> "Tuple[SymBarWord, Rational]":
        """Sort indices and return (canonical word, Koszul sign).

        For degree -1 elements, transposing two adjacent elements
        gives a factor of -1 (the Koszul sign (-1)^{(-1)(-1)} = -1).
        So the sign is the signature of the sorting permutation.
        Returns (word, 0) if indices have a repeat (element vanishes
        in exterior power).
        """
        lst = list(idx)
        # Bubble sort to count transpositions
        sign = 1
        n = len(lst)
        for i in range(n):
            for j in range(n - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    sign *= -1
                elif lst[j] == lst[j + 1]:
                    return SymBarWord(tuple(lst)), Rational(0)
        return SymBarWord(tuple(lst)), Rational(sign)

    @property
    def degree(self) -> int:
        return len(self.indices)

    def __repr__(self) -> str:
        if not self.indices:
            return "{}"
        return "{" + ",".join(str(i) for i in self.indices) + "}"


def sym_bar_words_at_degree(n: int, aug_dim: int) -> List[SymBarWord]:
    """All basis elements of coLie^c_n(s^{-1}V) for dim(V) = aug_dim.

    For degree-0 generators (desuspended to degree -1), this is
    Lambda^n(s^{-1}V): strictly increasing n-element subsets of
    {0, ..., aug_dim-1}.  Dimension = C(aug_dim, n).
    """
    if n == 0:
        return [SymBarWord(())]
    if n > aug_dim:
        return []
    result = []
    for combo in combinations(range(aug_dim), n):
        result.append(SymBarWord(combo))
    return result


@dataclass
class CommutativeBarComplex:
    """The commutative bar construction B_{Com}(A).

    For a commutative algebra A with generators in degree 0,
    B_{Com}(A) = (coLie^c(s^{-1} A_bar), d) is a coLie dg coalgebra.

    Since Com^! = Lie, the Koszul dual cooperad is coLie.
    The cofree coLie coalgebra on s^{-1}A_bar (degree -1 elements)
    has components coLie^c_n = Lambda^n(s^{-1}A_bar) (exterior powers,
    because the graded-symmetric product of degree -1 elements is
    antisymmetric: (-1)^{(-1)(-1)} = -1).

    The differential is the Harrison differential: it contracts pairs
    of generators via the commutative product and re-inserts the result,
    with signs from the exterior algebra structure.

    For the CE-like formula on Lambda^n(s^{-1}A_bar):
      d(v_1 ^ ... ^ v_n) = sum_{i<j} (-1)^{i+j} mu(v_i, v_j) ^ v_1 ^ ... hat_i ... hat_j ... ^ v_n
    where indices i,j are 1-based and mu is the product in A_bar.
    """
    algebra: AugAssAlgebra  # must be commutative
    max_degree: int

    def __post_init__(self):
        if not self.algebra.is_commutative():
            raise ValueError("CommutativeBarComplex requires a commutative algebra")

    def harrison_differential(self, word: SymBarWord) -> Dict[SymBarWord, Rational]:
        """Compute the Harrison differential on an exterior bar word.

        d(v_{i_1} ^ ... ^ v_{i_n}) = sum_{a<b} (-1)^{a+b}
            mu(v_{i_a}, v_{i_b}) ^ v_{i_1} ^ ... hat_a ... hat_b ... ^ v_{i_n}

        where a, b are 1-based positions in the word, and the result
        is put into canonical (sorted) form with the appropriate sign.
        """
        n = word.degree
        if n <= 1:
            return {}

        result: Dict[SymBarWord, Rational] = {}
        indices = list(word.indices)

        for pos_a in range(n):
            for pos_b in range(pos_a + 1, n):
                a_val = indices[pos_a]
                b_val = indices[pos_b]
                product = self.algebra.aug_ideal_multiply(a_val, b_val)

                # Sign: (-1)^{(a+1)+(b+1)} = (-1)^{a+b} in 0-based indexing
                # (corresponds to (-1)^{a+b} in 1-based = (-1)^{(a-1)+(b-1)}
                # in 0-based, but let's use the standard CE convention).
                # Moving v_a to position 0: sign (-1)^{pos_a} (past pos_a
                # elements of degree -1, each transposition gives -1).
                # Moving v_b to position 1: sign (-1)^{pos_b - 1} (past
                # pos_b - 1 remaining elements).
                # Total extraction sign: (-1)^{pos_a + pos_b - 1} = (-1)^{pos_a + pos_b + 1}
                extraction_sign = (-1) ** (pos_a + pos_b + 1)

                for k, coeff in product.items():
                    remaining = [indices[l] for l in range(n)
                                 if l != pos_a and l != pos_b]
                    # Insert k into remaining and sort, tracking sign
                    new_unsorted = (k,) + tuple(remaining)
                    new_word, insertion_sign = SymBarWord.from_unsorted(new_unsorted)
                    if insertion_sign == 0:
                        continue  # repeated index -> vanishes in exterior power
                    total_sign = Rational(extraction_sign) * insertion_sign
                    old = result.get(new_word, Rational(0))
                    result[new_word] = old + total_sign * coeff

        return {k: v for k, v in result.items() if v != 0}

    def verify_d_squared_zero(self, max_bar_degree: int = None) -> bool:
        """Verify d^2 = 0 on all symmetric bar words."""
        if max_bar_degree is None:
            max_bar_degree = self.max_degree
        aug_dim = self.algebra.aug_ideal_dim

        for n in range(2, max_bar_degree + 1):
            words = sym_bar_words_at_degree(n, aug_dim)
            for w in words:
                d_w = self.harrison_differential(w)
                d2_w: Dict[SymBarWord, Rational] = {}
                for w2, c2 in d_w.items():
                    d_w2 = self.harrison_differential(w2)
                    for w3, c3 in d_w2.items():
                        old = d2_w.get(w3, Rational(0))
                        d2_w[w3] = old + c2 * c3
                d2_w = {k: v for k, v in d2_w.items() if v != 0}
                if d2_w:
                    return False
        return True


# =========================================================================
#  PART 6: Two-coloured Swiss-cheese bar construction
# =========================================================================

@dataclass(frozen=True)
class TwoColoredBarWord:
    """An element of the two-coloured bar complex B_{SC}(C, A).

    colour: 'c' (closed output) or 'o' (open output)
    For closed output: a symmetric bar word in s^{-1} C_bar
    For open output: a mixed word with
      closed_indices: tuple of indices in C_bar (symmetric)
      open_indices: tuple of indices in A_bar (ordered)
    """
    colour: str  # 'c' or 'o'
    closed_indices: Tuple[int, ...]  # symmetric (sorted)
    open_indices: Tuple[int, ...]    # ordered (for 'o' colour)

    @property
    def closed_degree(self) -> int:
        return len(self.closed_indices)

    @property
    def open_degree(self) -> int:
        return len(self.open_indices)

    @property
    def total_degree(self) -> int:
        return self.closed_degree + self.open_degree

    def __repr__(self) -> str:
        if self.colour == 'c':
            return f"c:{{{','.join(str(i) for i in self.closed_indices)}}}"
        else:
            c_part = f"{{{','.join(str(i) for i in self.closed_indices)}}}"
            o_part = f"[{'|'.join(str(i) for i in self.open_indices)}]"
            return f"o:{c_part};{o_part}"


@dataclass
class SCAlgebra:
    """A Swiss-cheese algebra (C, A, act) where:
    - C is a commutative algebra (closed colour)
    - A is an associative algebra (open colour)
    - act: C tensor A -> A is the closed-to-open action

    act[(c, a)] = {b: coeff} where c in C_bar, a in A_bar, b in A_bar.
    Indices are in the augmentation ideal (0-based).
    """
    closed: AugAssAlgebra   # must be commutative
    open: AugAssAlgebra     # associative
    # action[(c_idx, a_idx)] -> Vector in A_bar
    action: Dict[Tuple[int, int], Vector]
    name: str = ""

    def act(self, c: int, a: int) -> Vector:
        """Action of c in C_bar on a in A_bar."""
        return dict(self.action.get((c, a), {}))

    @staticmethod
    def from_self_action(C: AugAssAlgebra) -> "SCAlgebra":
        """Canonical SC-algebra (C, C) where C acts on itself.

        This is the PROMOTION FUNCTOR: a commutative algebra C becomes
        an SC-algebra by acting on itself via multiplication.
        """
        assert C.is_commutative(), "Closed algebra must be commutative"
        action: Dict[Tuple[int, int], Vector] = {}
        for c in range(C.aug_ideal_dim):
            for a in range(C.aug_ideal_dim):
                prod = C.aug_ideal_multiply(c, a)
                if prod:
                    action[(c, a)] = prod
        return SCAlgebra(C, C, action, f"SC({C.name})")


@dataclass
class SwissCheeseBarComplex:
    """The two-coloured bar construction B_{SC}(C, A).

    Decomposes into:
    1. CLOSED SECTOR: B_{Com}(C) -- the Harrison complex
    2. OPEN SECTOR: B_{Ass}(A) -- the associative bar complex
    3. MIXED: the action of C on A induces additional differential
       components connecting closed inputs to open outputs.

    At low arities:
    - (0 closed, 1 open): s^{-1}a for a in A_bar.
      Differential: 0 (single element).
    - (1 closed, 0 open): s^{-1}c for c in C_bar.
      This is the closed-sector bar degree 1.
    - (0 closed, 2 open): s^{-1}a_1 tensor s^{-1}a_2 for a_i in A_bar.
      Differential: d[a_1|a_2] = a_1*a_2 (associative product in A_bar).
    - (1 closed, 1 open): s^{-1}c tensor s^{-1}a.
      This is a MIXED element. Differential includes:
      d(c; a) = c.a (action of C on A).
    - (2 closed, 0 open): {s^{-1}c_1, s^{-1}c_2}.
      Differential: d{c_1,c_2} = c_1*c_2 (commutative product in C_bar).
    """
    sc_algebra: SCAlgebra
    max_degree: int

    def _ass_bar(self) -> AssociativeBarComplex:
        return AssociativeBarComplex(self.sc_algebra.open, self.max_degree)

    def _com_bar(self) -> CommutativeBarComplex:
        return CommutativeBarComplex(self.sc_algebra.closed, self.max_degree)

    def closed_differential(self, word: TwoColoredBarWord) -> Dict[TwoColoredBarWord, Rational]:
        """Differential in the closed sector.

        For a closed-output word (c_1,...,c_n), this is the Harrison
        differential: contract pairs via the C-multiplication.
        """
        if word.colour != 'c':
            return {}
        sw = SymBarWord(word.closed_indices)
        cb = self._com_bar()
        d_sw = cb.harrison_differential(sw)
        result = {}
        for sw2, c in d_sw.items():
            new_word = TwoColoredBarWord('c', sw2.indices, ())
            result[new_word] = c
        return result

    def open_differential(self, word: TwoColoredBarWord) -> Dict[TwoColoredBarWord, Rational]:
        """Differential in the open sector: contract consecutive open pairs.

        For an element (c_1^...^c_k; [a_1|...|a_m]), the open
        differential contracts consecutive pairs a_i, a_{i+1} via
        the Ass product.

        In the extended-word picture [c_1,...,c_k | a_1,...,a_m],
        the open contractions occur at positions k, k+1, ..., k+m-2
        (0-indexed). Position k+i in the extended word corresponds
        to contracting (a_{i+1}, a_{i+2}), with sign (-1)^{k+i}.

        So: sign at open position i (contracting a_i and a_{i+1})
        is (-1)^{i + n_closed} where n_closed = k.
        """
        if word.colour != 'o':
            return {}
        if word.open_degree <= 1:
            return {}

        result: Dict[TwoColoredBarWord, Rational] = {}
        o_idx = list(word.open_indices)
        n = len(o_idx)
        n_closed = word.closed_degree

        for i in range(n - 1):
            a_i = o_idx[i]
            a_ip1 = o_idx[i + 1]
            product = self.sc_algebra.open.aug_ideal_multiply(a_i, a_ip1)
            sign = Rational((-1) ** (i + n_closed))
            for k, coeff in product.items():
                new_o = tuple(o_idx[:i]) + (k,) + tuple(o_idx[i + 2:])
                new_word = TwoColoredBarWord('o', word.closed_indices, new_o)
                old = result.get(new_word, Rational(0))
                result[new_word] = old + sign * coeff

        return {k: v for k, v in result.items() if v != 0}

    def mixed_differential(self, word: TwoColoredBarWord) -> Dict[TwoColoredBarWord, Rational]:
        """Mixed differential: closed inputs acting on the leftmost open input.

        For an element (c_1^...^c_k; [a_1|...|a_m]), the mixed
        differential extracts one closed element c_j from the exterior
        product and acts on the LEFTMOST open element a_1. This
        corresponds to the contraction at position j in the extended
        word [c_1,...,c_k | a_1,...,a_m], where c_j acts on a_1.

        In the SC-algebra axiom for left modules:
          c.(a_1 * a_2) = (c.a_1) * a_2
        which ensures d^2 = 0 via associativity.

        Sign: extracting c_j from position j in the exterior product
        costs (-1)^j (moving past j elements of degree -1).
        """
        if word.colour != 'o':
            return {}
        if word.closed_degree == 0:
            return {}
        if word.open_degree == 0:
            return {}

        result: Dict[TwoColoredBarWord, Rational] = {}
        c_idx = list(word.closed_indices)
        o_idx = list(word.open_indices)
        a_1 = o_idx[0]  # leftmost open element

        for ci, c_val in enumerate(c_idx):
            acted = self.sc_algebra.act(c_val, a_1)
            # Sign: (-1)^{ci} for extracting from exterior product
            sign = Rational((-1) ** ci)
            for k, coeff in acted.items():
                remaining_c = tuple(c_idx[l] for l in range(len(c_idx))
                                    if l != ci)
                new_o = (k,) + tuple(o_idx[1:])
                new_word = TwoColoredBarWord(
                    'o', remaining_c, new_o
                )
                old = result.get(new_word, Rational(0))
                result[new_word] = old + sign * coeff

        return {k: v for k, v in result.items() if v != 0}

    def mixed_closed_differential(
        self, word: TwoColoredBarWord
    ) -> Dict[TwoColoredBarWord, Rational]:
        """Harrison-type contraction in the closed indices of an open-output word.

        For (c_1,...,c_k; a_1,...,a_m) with k >= 2, contract pairs
        of closed indices via the C-multiplication. Uses the same
        sign convention as the Harrison differential (exterior algebra
        of degree -1 elements).
        """
        if word.colour != 'o':
            return {}
        if word.closed_degree <= 1:
            return {}

        result: Dict[TwoColoredBarWord, Rational] = {}
        c_idx = list(word.closed_indices)
        n_c = len(c_idx)

        for i in range(n_c):
            for j in range(i + 1, n_c):
                c_i = c_idx[i]
                c_j = c_idx[j]
                product = self.sc_algebra.closed.aug_ideal_multiply(c_i, c_j)
                # Same extraction sign as Harrison: (-1)^{i+j+1} (0-based)
                extraction_sign = (-1) ** (i + j + 1)
                for k, coeff in product.items():
                    remaining = [c_idx[l] for l in range(n_c)
                                 if l != i and l != j]
                    new_unsorted = (k,) + tuple(remaining)
                    new_sw, insertion_sign = SymBarWord.from_unsorted(new_unsorted)
                    if insertion_sign == 0:
                        continue
                    total_sign = Rational(extraction_sign) * insertion_sign
                    new_word = TwoColoredBarWord('o', new_sw.indices, word.open_indices)
                    old = result.get(new_word, Rational(0))
                    result[new_word] = old + total_sign * coeff

        return {k: v for k, v in result.items() if v != 0}

    def full_differential(self, word: TwoColoredBarWord) -> Dict[TwoColoredBarWord, Rational]:
        """Total differential: sum of all components."""
        result: Dict[TwoColoredBarWord, Rational] = {}
        for component in [
            self.closed_differential,
            self.open_differential,
            self.mixed_differential,
            self.mixed_closed_differential,
        ]:
            for w, c in component(word).items():
                old = result.get(w, Rational(0))
                result[w] = old + c
        return {k: v for k, v in result.items() if v != 0}

    def verify_d_squared_zero_closed(self, max_deg: int = None) -> bool:
        """Verify d^2 = 0 on the closed sector."""
        if max_deg is None:
            max_deg = self.max_degree
        aug_dim = self.sc_algebra.closed.aug_ideal_dim

        for n in range(2, max_deg + 1):
            swords = sym_bar_words_at_degree(n, aug_dim)
            for sw in swords:
                w = TwoColoredBarWord('c', sw.indices, ())
                d_w = self.full_differential(w)
                d2: Dict[TwoColoredBarWord, Rational] = {}
                for w2, c2 in d_w.items():
                    d_w2 = self.full_differential(w2)
                    for w3, c3 in d_w2.items():
                        old = d2.get(w3, Rational(0))
                        d2[w3] = old + c2 * c3
                d2 = {k: v for k, v in d2.items() if v != 0}
                if d2:
                    return False
        return True

    def verify_d_squared_zero_open(self, max_total_deg: int = None) -> bool:
        """Verify d^2 = 0 on open-output elements at given total degree."""
        if max_total_deg is None:
            max_total_deg = self.max_degree
        c_dim = self.sc_algebra.closed.aug_ideal_dim
        o_dim = self.sc_algebra.open.aug_ideal_dim

        for total in range(2, max_total_deg + 1):
            for n_c in range(total + 1):
                n_o = total - n_c
                if n_o < 0:
                    continue
                # Generate all words with n_c closed + n_o open inputs
                closed_words = sym_bar_words_at_degree(n_c, c_dim) if c_dim > 0 else (
                    [SymBarWord(())] if n_c == 0 else []
                )
                open_words = bar_words_at_degree(n_o, o_dim) if o_dim > 0 else (
                    [BarWord(())] if n_o == 0 else []
                )
                for cw in closed_words:
                    for ow in open_words:
                        w = TwoColoredBarWord('o', cw.indices, ow.indices)
                        d_w = self.full_differential(w)
                        d2: Dict[TwoColoredBarWord, Rational] = {}
                        for w2, c2 in d_w.items():
                            d_w2 = self.full_differential(w2)
                            for w3, c3 in d_w2.items():
                                old = d2.get(w3, Rational(0))
                                d2[w3] = old + c2 * c3
                        d2 = {k: v for k, v in d2.items() if v != 0}
                        if d2:
                            return False
        return True


# =========================================================================
#  PART 7: The chiral bar as SC-coalgebra (conceptual bridge)
# =========================================================================

def chiral_bar_sc_structure_summary() -> dict:
    """Summarise how B^ch(A) is an SC^{ch,top}-coalgebra.

    This is a conceptual function documenting the type-checking
    resolution of the fundamental question.

    For a chiral algebra A (= Com^ch-algebra), the bar construction
    B^ch(A) = T^c(s^{-1} A_bar) is SIMULTANEOUSLY:

    1. A dg coalgebra via d_C (the bar differential from FM_k(C))
       = CLOSED colour structure
    2. A coassociative coalgebra via Delta (deconcatenation)
       = OPEN colour structure
    3. d_C is a coderivation of Delta
       = the SC^{ch,top}-coalgebra compatibility

    The key insight: the bar construction does NOT require a second
    (open-colour) input. It PRODUCES the two-coloured structure from
    a one-coloured input. The open-colour data (deconcatenation) is
    a FORMAL CONSEQUENCE of the tensor coalgebra structure.

    In the Loday-Vallette framework: this corresponds to the fact
    that the forgetful functor from SC-coalgebras to Com-coalgebras
    (forgetting the open sector) has a LEFT ADJOINT that freely
    generates the open-colour structure. The bar construction
    computes this left adjoint on the nose.

    Comparison with the classical case:
    - Classical SC (Voronov): (C, A) with C = Com-algebra, A = Ass-algebra
    - Bar: B_{SC}(C, A) has BOTH closed and open components
    - For the SELF-ACTION case: B_{SC}(C, C) has:
        closed = B_{Com}(C) = coLie coalgebra
        open = B_{Ass}(C) = coAss coalgebra
        mixed = action-induced maps
    - For chiral: A single chiral algebra gives rise to the self-action
      SC-algebra (A, A) where A acts on itself, and B_{SC}(A, A)
      decomposes exactly as described in thm:bar-swiss-cheese.
    """
    return {
        "closed_sector": "B_{Com}(A) = coLie coalgebra from FM_k(C)",
        "open_sector": "B_{Ass}(A) = coAss coalgebra from Conf_k(R)",
        "compatibility": "d_C coderivation of Delta",
        "input": "Single Com-algebra A",
        "output": "SC-coalgebra (B_{Com}(A), B_{Ass}(A), mixed)",
        "key_fact": "Open sector is PRODUCED, not assumed",
        "type_resolution": "Forgetful SC-coalg -> Com-coalg has left adjoint; "
                           "bar computes this adjoint",
        "manuscript_ref": "thm:bar-swiss-cheese (en_koszul_duality.tex)",
    }


# =========================================================================
#  PART 8: Explicit low-arity computations
# =========================================================================

def compute_bar_ass_low_arity(A: AugAssAlgebra, max_deg: int = 4) -> dict:
    """Compute B_{Ass}(A) at low arities with explicit differential."""
    bc = AssociativeBarComplex(A, max_deg)
    aug_dim = A.aug_ideal_dim

    result = {"algebra": A.name, "aug_ideal_dim": aug_dim}
    for n in range(max_deg + 1):
        words = bar_words_at_degree(n, aug_dim)
        diff_data = {}
        for w in words:
            d_w = bc.bar_differential(w)
            if d_w:
                diff_data[str(w)] = {str(k): str(v) for k, v in d_w.items()}
        result[f"degree_{n}"] = {
            "dim": len(words),
            "words": [str(w) for w in words],
            "differential": diff_data,
        }
    return result


def compute_bar_com_low_arity(A: AugAssAlgebra, max_deg: int = 4) -> dict:
    """Compute B_{Com}(A) at low arities with explicit differential."""
    assert A.is_commutative(), "Need commutative algebra for B_{Com}"
    bc = CommutativeBarComplex(A, max_deg)
    aug_dim = A.aug_ideal_dim

    result = {"algebra": A.name, "aug_ideal_dim": aug_dim}
    for n in range(max_deg + 1):
        words = sym_bar_words_at_degree(n, aug_dim)
        diff_data = {}
        for w in words:
            d_w = bc.harrison_differential(w)
            if d_w:
                diff_data[str(w)] = {str(k): str(v) for k, v in d_w.items()}
        result[f"degree_{n}"] = {
            "dim": len(words),
            "words": [str(w) for w in words],
            "differential": diff_data,
        }
    return result


def compute_bar_sc_low_arity(
    sc: SCAlgebra, max_deg: int = 3
) -> dict:
    """Compute B_{SC}(C, A) at low arities."""
    bc = SwissCheeseBarComplex(sc, max_deg)
    c_dim = sc.closed.aug_ideal_dim
    o_dim = sc.open.aug_ideal_dim

    result = {"sc_algebra": sc.name, "c_dim": c_dim, "o_dim": o_dim}

    # Closed sector
    closed_data = {}
    for n in range(1, max_deg + 1):
        swords = sym_bar_words_at_degree(n, c_dim)
        diffs = {}
        for sw in swords:
            w = TwoColoredBarWord('c', sw.indices, ())
            d_w = bc.full_differential(w)
            if d_w:
                diffs[str(w)] = {str(k): str(v) for k, v in d_w.items()}
        closed_data[f"degree_{n}"] = {
            "dim": len(swords),
            "differential": diffs,
        }
    result["closed"] = closed_data

    # Open sector (pure open)
    open_data = {}
    for n in range(1, max_deg + 1):
        words = bar_words_at_degree(n, o_dim)
        diffs = {}
        for bw in words:
            w = TwoColoredBarWord('o', (), bw.indices)
            d_w = bc.full_differential(w)
            if d_w:
                diffs[str(w)] = {str(k): str(v) for k, v in d_w.items()}
        open_data[f"degree_{n}"] = {
            "dim": len(words),
            "differential": diffs,
        }
    result["pure_open"] = open_data

    # Mixed sector
    mixed_data = {}
    for total in range(2, max_deg + 1):
        for n_c in range(1, total):
            n_o = total - n_c
            if n_o < 1:
                continue
            closed_words = sym_bar_words_at_degree(n_c, c_dim) if c_dim > 0 else []
            open_words = bar_words_at_degree(n_o, o_dim) if o_dim > 0 else []
            diffs = {}
            for cw in closed_words:
                for ow in open_words:
                    w = TwoColoredBarWord('o', cw.indices, ow.indices)
                    d_w = bc.full_differential(w)
                    if d_w:
                        diffs[str(w)] = {str(k): str(v) for k, v in d_w.items()}
            key = f"({n_c}c,{n_o}o)"
            mixed_data[key] = {
                "dim": len(closed_words) * len(open_words),
                "differential": diffs,
            }
    result["mixed"] = mixed_data

    return result


# =========================================================================
#  PART 9: Dimension counts and cohomology
# =========================================================================

def bar_ass_euler_char(A: AugAssAlgebra, max_deg: int = 5) -> Rational:
    """Euler characteristic of B_{Ass}(A) up to given degree.

    chi = sum_n (-1)^n dim B^n = sum_n (-1)^n (aug_dim)^n
        = 1/(1 + aug_dim)  (geometric series, formal).

    For k[x]/(x^n): aug_dim = n-1, chi = 1/n.
    """
    d = A.aug_ideal_dim
    chi = Rational(0)
    for n in range(max_deg + 1):
        chi += Rational((-1) ** n) * Rational(d ** n)
    return chi


def bar_ass_formal_euler_char(A: AugAssAlgebra) -> Rational:
    """Formal (infinite) Euler characteristic 1/(1 + aug_dim)."""
    d = A.aug_ideal_dim
    if d == 0:
        return Rational(1)
    return Rational(1, 1 + d)


# =========================================================================
#  PART 10: Promotion functor verification
# =========================================================================

def verify_promotion_functor(C: AugAssAlgebra, max_deg: int = 3) -> dict:
    """Verify that the self-action SC-algebra (C, C) produces
    the expected two-coloured bar construction.

    The closed sector should be B_{Com}(C).
    The open sector should be B_{Ass}(C).
    The mixed differential should be compatible with both.
    """
    assert C.is_commutative(), "Promotion functor requires commutative algebra"

    sc = SCAlgebra.from_self_action(C)
    sc_bar = SwissCheeseBarComplex(sc, max_deg)

    # Check d^2 = 0 on closed sector
    d2_closed = sc_bar.verify_d_squared_zero_closed(max_deg)

    # Check d^2 = 0 on open sector
    d2_open = sc_bar.verify_d_squared_zero_open(max_deg)

    # Check that pure-closed differential matches Harrison
    com_bar = CommutativeBarComplex(C, max_deg)
    harrison_matches = True
    aug_dim = C.aug_ideal_dim
    for n in range(2, max_deg + 1):
        swords = sym_bar_words_at_degree(n, aug_dim)
        for sw in swords:
            w = TwoColoredBarWord('c', sw.indices, ())
            d_sc = sc_bar.full_differential(w)
            d_har = com_bar.harrison_differential(sw)
            # Convert d_har to TwoColoredBarWord keys
            d_har_conv = {}
            for sw2, c in d_har.items():
                d_har_conv[TwoColoredBarWord('c', sw2.indices, ())] = c
            if d_sc != d_har_conv:
                harrison_matches = False
                break

    # Check that pure-open differential matches Ass bar
    ass_bar = AssociativeBarComplex(C, max_deg)
    ass_matches = True
    for n in range(2, max_deg + 1):
        words = bar_words_at_degree(n, aug_dim)
        for bw in words:
            w = TwoColoredBarWord('o', (), bw.indices)
            d_sc_open = sc_bar.open_differential(w)
            d_ass = ass_bar.bar_differential(bw)
            d_ass_conv = {}
            for bw2, c in d_ass.items():
                d_ass_conv[TwoColoredBarWord('o', (), bw2.indices)] = c
            if d_sc_open != d_ass_conv:
                ass_matches = False
                break

    return {
        "algebra": C.name,
        "d_squared_zero_closed": d2_closed,
        "d_squared_zero_open": d2_open,
        "harrison_matches": harrison_matches,
        "ass_bar_matches": ass_matches,
        "all_pass": d2_closed and d2_open and harrison_matches and ass_matches,
    }
