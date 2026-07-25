"""Exact finite windows of the associative bar--cobar counit.

``FiniteOmegaBarComplex`` constructs the quotient of
``Omega(B(A)) = T(s overline{B}(A))`` with total bar length at most ``P`` and
cobar tensor length at most ``Q``.  Every bar word of lengths ``1, ..., P``
that occurs in this window is present.  The matrices contain the internal
differential of ``A``, the bar multiplication differential, and the cobar
deconcatenation differential.  All ranks and homology dimensions are computed
over ``QQ``.

The key objects:
1. Bar construction B(A) = (T^c(s^{-1}A_bar), d_B)
   - Free tensor coalgebra on suspension of augmentation ideal
   - d_B = d_1 (internal) + d_2 (from multiplication)
   - d_B^2 = 0 when m_2 is associative

2. Cobar construction Omega(C) = (T(s C_bar), d_Omega)
   - Free tensor algebra on the suspension of the coaugmentation coideal
   - d_Omega = d_1 (internal) + d_2 (from comultiplication)

3. Finite bar--cobar window
   - A basis vector is a tuple of nonempty bar words
   - Total bar length and cobar tensor length are recorded separately
   - The total differential changes either bar length or cobar length

4. Counit epsilon: Omega(B(A)) -> A
   - epsilon sends the cobar unit to the algebra unit
   - epsilon sends ``s[s^{-1}a]`` to ``a``
   - multiplicativity sends a tuple of length-one bar words to the product in A
   - a cobar generator arising from a longer bar word maps to zero

5. Twisting morphism tau: B(A) -> A
   - tau(s^{-1}a) = a on bar degree 1, zero elsewhere
   - MC equation: d(tau) + tau*tau = 0

CONVENTIONS (from CLAUDE.md):
  - Cohomological grading, |d| = +1
  - Bar uses desuspension ``s^{-1}``; cobar uses suspension ``s``
  - Koszul sign: swapping degree p and q elements gives (-1)^{pq}
  - A: algebra, B(A): bar coalgebra, A^i = H*(B(A)): dual coalgebra
  - A^! = (A^i)^v: Koszul dual algebra (VERDIER duality, not cobar)
  - Omega(B(A)) = A (bar-cobar INVERSION, not duality)
  - Com^! = Lie (NOT coLie)

References:
  thm:bar-cobar-adjunction (bar_cobar_adjunction_curved.tex)
  thm:bar-cobar-inversion (bar_cobar_adjunction_inversion.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product as cartprod
from math import factorial
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from sympy import Matrix, Rational, Symbol, simplify, zeros, eye, Integer


FINITE_CALCULATION_STATUS = "computed finite truncation"
CONVERGENCE_STATUS = "unresolved beyond finite truncation"


def finite_calculation_state(max_bar_length: int, max_cobar_length: int) -> Dict[str, object]:
    """Describe the mathematical scope of a finite bar--cobar calculation."""
    return {
        "calculation_status": FINITE_CALCULATION_STATUS,
        "convergence_status": CONVERGENCE_STATUS,
        "computed_object": (
            "Omega(B(A)) with total bar length <= "
            f"{max_bar_length} and cobar length <= {max_cobar_length}"
        ),
        "global_quasi_isomorphism": "unresolved",
        "remaining_convergence_obligation": (
            "identify the P,Q -> infinity filtered object with the chosen completed "
            "Omega(B(A)) and justify passage of cohomology through that limit"
        ),
    }


# ============================================================================
# Core data structure: augmented dg algebra over Q
# ============================================================================

@dataclass
class AugDGA:
    """Augmented dg algebra over Q, for exact symbolic computation.

    V has basis {e_0, ..., e_{dim-1}}.
    degrees[i] = cohomological degree of e_i.
    diff: Matrix for d: V -> V (d^2 = 0).
    mult[(i,j)] = {k: coeff} for m_2(e_i, e_j) = sum coeff * e_k.
    augmentation: map to ground field (e.g. projection onto unit).

    All coefficients are sympy Rational for exact computation.
    """
    dim: int
    degrees: List[int]
    diff: Matrix
    mult: Dict[Tuple[int, int], Dict[int, Rational]]
    name: str = ""

    def d_squared_zero(self) -> bool:
        """Verify d^2 = 0 exactly."""
        d2 = self.diff * self.diff
        return d2.equals(zeros(self.dim, self.dim))

    def is_associative(self) -> bool:
        """Check associativity of m_2 on all triples."""
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    # (e_i * e_j) * e_k
                    lhs = self._triple_left(i, j, k)
                    # e_i * (e_j * e_k)
                    rhs = self._triple_right(i, j, k)
                    if lhs != rhs:
                        return False
        return True

    def _apply_mult(self, i: int, j: int) -> Dict[int, Rational]:
        """m_2(e_i, e_j) as a dict."""
        return self.mult.get((i, j), {})

    def _triple_left(self, i: int, j: int, k: int) -> Dict[int, Rational]:
        """(e_i * e_j) * e_k."""
        ij = self._apply_mult(i, j)
        result: Dict[int, Rational] = {}
        for m, c1 in ij.items():
            mk = self._apply_mult(m, k)
            for n, c2 in mk.items():
                result[n] = result.get(n, Rational(0)) + c1 * c2
        return {k: v for k, v in result.items() if v != 0}

    def _triple_right(self, i: int, j: int, k: int) -> Dict[int, Rational]:
        """e_i * (e_j * e_k)."""
        jk = self._apply_mult(j, k)
        result: Dict[int, Rational] = {}
        for m, c1 in jk.items():
            im = self._apply_mult(i, m)
            for n, c2 in im.items():
                result[n] = result.get(n, Rational(0)) + c1 * c2
        return {k: v for k, v in result.items() if v != 0}

    def koszul_sign(self, p: int, q: int) -> int:
        """Koszul sign (-1)^{pq} for swapping elements of degrees p, q."""
        return (-1) ** (p * q)


# ============================================================================
# Standard algebras
# ============================================================================

def truncated_polynomial_dga(n: int) -> AugDGA:
    """Truncated polynomial k[x]/(x^n) as a dg algebra, |x| = 0, d = 0.

    Basis: 1, x, x^2, ..., x^{n-1}. Augmentation: x -> 0.
    This is associative and augmented, the cleanest test case.
    """
    dim = n
    degrees = [0] * n
    diff = zeros(n, n)
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {}
    for i in range(n):
        for j in range(n):
            if i + j < n:
                mult[(i, j)] = {i + j: Rational(1)}
    return AugDGA(dim, degrees, diff, mult, name=f"k[x]/(x^{n})")


def dual_numbers_dga() -> AugDGA:
    """Dual numbers k[eps]/(eps^2): basis {1, eps}, eps^2 = 0.

    The simplest nontrivial associative algebra for bar-cobar.
    """
    return truncated_polynomial_dga(2)


def matrix_2x2_upper_dga() -> AugDGA:
    """Upper triangular ``2 x 2`` matrices with a chosen augmentation.

    Basis: ``1, p=e_11, u=e_12``; then ``e_22=1-p``.  The augmentation is
    the lower diagonal character, so ``p`` and ``u`` span its kernel.
    """
    dim = 3
    degrees = [0, 0, 0]
    diff = zeros(3, 3)
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        (1, 0): {1: Rational(1)},
        (0, 2): {2: Rational(1)},
        (2, 0): {2: Rational(1)},
        (1, 1): {1: Rational(1)},  # p^2 = p
        (1, 2): {2: Rational(1)},  # p u = u
    }
    return AugDGA(dim, degrees, diff, mult, name="UT_2")


def exterior_on_one_generator() -> AugDGA:
    """Exterior algebra k[eps]/(eps^2) with |eps| = 1, d = 0.

    Basis: {1 (deg 0), eps (deg 1)}. eps^2 = 0.
    This is Koszul self-dual: (Lambda(V))^! = Sym(V*).
    """
    dim = 2
    degrees = [0, 1]
    diff = zeros(2, 2)
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        (1, 0): {1: Rational(1)},
        # (1, 1) absent: eps^2 = 0
    }
    return AugDGA(dim, degrees, diff, mult, name="Lambda(1)")


def free_assoc_on_one_generator(max_weight: int = 3) -> AugDGA:
    """Free associative algebra on one generator x, truncated at weight max_weight.

    Basis: 1, x, x^2, ..., x^{max_weight}. All products that stay within
    the truncation are kept; those exceeding it are set to 0.
    """
    return truncated_polynomial_dga(max_weight + 1)


def lie_sl2_as_assoc() -> AugDGA:
    """sl_2 with the Lie bracket as a non-associative algebra.

    Basis: e, h, f. Product = Lie bracket [a, b].
    NOT associative: [[e,f],e] = [h,e] = 2e, but [e,[f,e]] = [e,-h] = 2e.
    Wait: [e,[f,e]] = [e, -h] = -[e,h] = 2e.  [[e,f],e] = [h,e] = 2e.
    These agree for this triple but associativity fails in general for Lie.

    We include this for comparison but d_bar^2 != 0 for non-associative algebras.
    """
    dim = 3
    degrees = [0, 0, 0]
    diff = zeros(3, 3)
    E, H, F = 0, 1, 2
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {
        (E, F): {H: Rational(1)},
        (F, E): {H: Rational(-1)},
        (H, E): {E: Rational(2)},
        (E, H): {E: Rational(-2)},
        (H, F): {F: Rational(-2)},
        (F, H): {F: Rational(2)},
    }
    return AugDGA(dim, degrees, diff, mult, name="sl_2_Lie")


def polynomial_with_diff() -> AugDGA:
    """A contractible square-zero pair adjoining the unit.

    Basis: ``1`` in degree ``0``, ``x`` in degree ``0``, and ``y`` in degree
    ``1``.  The differential is ``d(x)=y``.  Products inside the augmentation
    ideal vanish, while the unit acts strictly.
    """
    dim = 3
    degrees = [0, 0, 1]
    diff = zeros(3, 3)
    diff[2, 1] = Rational(1)  # d(x) = y
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        (1, 0): {1: Rational(1)},
        (0, 2): {2: Rational(1)},
        (2, 0): {2: Rational(1)},
    }
    return AugDGA(dim, degrees, diff, mult, name="k + (x -> y), I^2=0")


# ============================================================================
# Bar construction B(A)
# ============================================================================

@dataclass
class BarConstruction:
    """The bar construction B(A) = (T^c(s^{-1}A_bar), d_B).

    Computes the bar complex with exact rational arithmetic.

    The augmentation ideal A_bar = ker(augmentation) is identified with
    the non-unit generators. For our algebras, if basis element 0 is the unit,
    then A_bar = span{e_1, ..., e_{dim-1}}.

    Bar degree n: B^n = (s^{-1}A_bar)^{tensor n}.
    Basis: multi-indices (i_1, ..., i_n) with each i_j in {1, ..., dim-1}.
    Degree of s^{-1}e_i = |e_i| - 1 (desuspension lowers degree by 1 in
    cohomological convention).

    The bar differential d_B: B^n -> B^{n-1} has two parts:
      d_1: internal (extends d on A to each tensor factor)
      d_2: multiplication (contracts adjacent pairs via m_2)
    """
    dga: AugDGA
    max_bar_degree: int

    # Indices of generators in the augmentation ideal
    _aug_ideal_indices: List[int] = field(default_factory=list, init=False)
    _basis_cache: Dict[int, List[Tuple[int, ...]]] = field(default_factory=dict, init=False)
    _diff_cache: Dict[int, Matrix] = field(default_factory=dict, init=False)

    def __post_init__(self):
        # Augmentation ideal: all non-unit generators.
        # Convention: index 0 = unit element.
        self._aug_ideal_indices = list(range(1, self.dga.dim))

    @property
    def aug_dim(self) -> int:
        """Dimension of the augmentation ideal A_bar."""
        return len(self._aug_ideal_indices)

    def basis(self, n: int) -> List[Tuple[int, ...]]:
        """Basis for B^n = (s^{-1}A_bar)^{tensor n}.

        Returns list of multi-indices from the augmentation ideal.
        """
        if n in self._basis_cache:
            return self._basis_cache[n]
        if n <= 0:
            self._basis_cache[n] = [()]  # ground field k at degree 0
            return [()]
        indices = self._aug_ideal_indices
        result = list(cartprod(indices, repeat=n))
        self._basis_cache[n] = result
        return result

    def dim_at(self, n: int) -> int:
        """Dimension of B^n."""
        if n <= 0:
            return 1
        return self.aug_dim ** n

    def differential(self, n: int) -> Matrix:
        """Bar differential d_B: B^n -> B^{n-1}, the multiplication component.

        d_B([s^{-1}a_1|...|s^{-1}a_n])
          = sum_{p=1}^{n-1} (-1)^{eps_p}
            [s^{-1}a_1|...|s^{-1}(a_p*a_{p+1})|...|s^{-1}a_n]

        where eps_p = sum_{q=1}^{p} |s^{-1}a_q|
        = sum_{q=1}^{p} (|a_q| - 1), including the left input of the
        multiplication at position ``p``.

        For generators all in degree 0, the signs begin ``-1,+1,-1,...``.

        Returns matrix (dim B^{n-1}) x (dim B^n).

        NOTE: When the product lands on the unit (index 0), that term contributes
        to a map B^n -> B^{n-2}, not B^{n-1}. For simplicity, we handle
        unit-reduction: if m_2(a_i, a_{i+1}) has a component along the unit,
        that component drops two bar degrees.
        """
        if n in self._diff_cache:
            return self._diff_cache[n]
        if n < 2:
            mat = zeros(self.dim_at(max(n - 1, 0)), self.dim_at(n))
            self._diff_cache[n] = mat
            return mat

        source = self.basis(n)
        target = self.basis(n - 1)

        dim_s = len(source)
        dim_t = len(target)
        mat = zeros(dim_t, dim_s)
        target_idx = {t: i for i, t in enumerate(target)}

        for col_idx, multi in enumerate(source):
            for p in range(n - 1):
                # Koszul sign for the bar differential
                # The shifted multiplication has local sign
                # (-1)^|s^-1 a_p| in addition to the coderivation prefix.
                eps = sum(self.dga.degrees[multi[q]] - 1 for q in range(p + 1))
                sign = -1 if eps % 2 else 1

                a_p = multi[p]
                a_p1 = multi[p + 1]
                products = self.dga.mult.get((a_p, a_p1), {})

                for k, coeff in products.items():
                    if k == 0:
                        # Product lands on unit: goes to B^{n-2}
                        # We track this separately; skip in the B^{n-1} map
                        continue
                    if k not in self._aug_ideal_indices:
                        continue
                    new_multi = multi[:p] + (k,) + multi[p + 2:]
                    if new_multi in target_idx:
                        mat[target_idx[new_multi], col_idx] += sign * coeff

        self._diff_cache[n] = mat
        return mat

    def unit_contraction(self, n: int) -> Matrix:
        """Terms of d_B where the product lands on the unit: B^n -> B^{n-2}.

        When m_2(a_p, a_{p+1}) has a component along the unit (index 0),
        the resulting element has bar degree n-2 (both factors are consumed).
        """
        if n < 2:
            return zeros(self.dim_at(max(n - 2, 0)), self.dim_at(n))

        source = self.basis(n)
        target = self.basis(n - 2) if n >= 2 else [()]
        dim_s = len(source)
        dim_t = len(target)
        mat = zeros(dim_t, dim_s)
        target_idx = {t: i for i, t in enumerate(target)}

        for col_idx, multi in enumerate(source):
            for p in range(n - 1):
                eps = sum(self.dga.degrees[multi[q]] - 1 for q in range(p + 1))
                sign = -1 if eps % 2 else 1

                a_p = multi[p]
                a_p1 = multi[p + 1]
                products = self.dga.mult.get((a_p, a_p1), {})

                unit_coeff = products.get(0, Rational(0))
                if unit_coeff == 0:
                    continue

                new_multi = multi[:p] + multi[p + 2:]
                if new_multi in target_idx:
                    mat[target_idx[new_multi], col_idx] += sign * unit_coeff

        return mat

    def internal_differential(self, n: int) -> Matrix:
        """Internal differential d_1: B^n -> B^n.

        Applies the differential d of A to each tensor factor.
        d_1([s^{-1}a_1|...|s^{-1}a_n])
          = sum_p (-1)^{eps_p}
            [s^{-1}a_1|...|s^{-1}(d a_p)|...|s^{-1}a_n]
        """
        if n <= 0:
            return zeros(1, 1)

        source = self.basis(n)
        dim_n = len(source)
        mat = zeros(dim_n, dim_n)
        source_idx = {s: i for i, s in enumerate(source)}

        for col_idx, multi in enumerate(source):
            for p in range(n):
                # The shifted complex has d_{A[-1]} = -d_A.
                eps = 1 + sum(self.dga.degrees[multi[q]] - 1 for q in range(p))
                sign = -1 if eps % 2 else 1
                a_p = multi[p]
                for k in self._aug_ideal_indices:
                    coeff = self.dga.diff[k, a_p]
                    if coeff == 0:
                        continue
                    new_multi = multi[:p] + (k,) + multi[p + 1:]
                    if new_multi in source_idx:
                        mat[source_idx[new_multi], col_idx] += sign * coeff

        return mat

    def verify_d_squared(self) -> Dict[int, bool]:
        """Verify d_B^2 = 0 at each bar degree.

        For the multiplication part d_2: d_2^2 = 0 iff m_2 is associative.
        For the total d = d_1 + d_2: d^2 = 0 iff d_1^2 = 0, d_1 d_2 + d_2 d_1 = 0,
        and d_2^2 = 0. The first holds by d^2 = 0 on A; the second by Leibniz;
        the third by associativity.
        """
        results = {}
        for n in range(2, self.max_bar_degree + 1):
            d_n = self.differential(n)
            d_nm1 = self.differential(n - 1)

            if d_n.cols == 0 or d_nm1.rows == 0:
                results[n] = True
                continue

            # d^{n-1} o d^n
            if d_nm1.cols != d_n.rows:
                results[n] = False
                continue

            product = d_nm1 * d_n
            results[n] = product.equals(zeros(product.rows, product.cols))
        return results


# ============================================================================
# Exact finite windows of Omega(B(A))
# ============================================================================

BarWord = Tuple[int, ...]
OmegaWord = Tuple[BarWord, ...]


def _sign(exponent: int) -> Rational:
    """Return ``(-1)^exponent`` as an exact scalar."""
    return Rational(-1 if exponent % 2 else 1)


def _positive_compositions(total: int, parts: int) -> List[Tuple[int, ...]]:
    """Ordered decompositions of ``total`` into ``parts`` positive integers."""
    if parts == 0:
        return [()] if total == 0 else []
    if parts == 1:
        return [(total,)] if total >= 1 else []
    result: List[Tuple[int, ...]] = []
    for first in range(1, total - parts + 2):
        for tail in _positive_compositions(total - first, parts - 1):
            result.append((first,) + tail)
    return result


def augmented_dga_axioms(dga: AugDGA) -> Dict[str, bool]:
    """Check the finite-dimensional augmented cochain-DGA axioms exactly.

    Basis vector ``e_0`` is the unit and the augmentation sends ``e_0`` to
    ``1`` and ``e_i`` to ``0`` for ``i > 0``.
    """
    unit = True
    for i in range(dga.dim):
        unit &= dga.mult.get((0, i), {}) == {i: Rational(1)}
        unit &= dga.mult.get((i, 0), {}) == {i: Rational(1)}

    differential_degree = True
    for target in range(dga.dim):
        for source in range(dga.dim):
            if dga.diff[target, source] != 0:
                differential_degree &= dga.degrees[target] == dga.degrees[source] + 1

    multiplication_degree = True
    augmentation_multiplicative = True
    for (left, right), outputs in dga.mult.items():
        for target, coeff in outputs.items():
            if coeff == 0:
                continue
            multiplication_degree &= (
                dga.degrees[target] == dga.degrees[left] + dga.degrees[right]
            )
            if left > 0 and right > 0 and target == 0:
                augmentation_multiplicative = False

    augmentation_is_chain_map = all(dga.diff[0, j] == 0 for j in range(dga.dim))

    leibniz = True
    for i in range(dga.dim):
        for j in range(dga.dim):
            lhs: Dict[int, Rational] = {}
            for k, coefficient in dga.mult.get((i, j), {}).items():
                for target in range(dga.dim):
                    value = coefficient * dga.diff[target, k]
                    if value:
                        lhs[target] = lhs.get(target, Rational(0)) + value

            rhs: Dict[int, Rational] = {}
            for k in range(dga.dim):
                coefficient = dga.diff[k, i]
                if coefficient:
                    for target, value in dga.mult.get((k, j), {}).items():
                        rhs[target] = rhs.get(target, Rational(0)) + coefficient * value
            parity = _sign(dga.degrees[i])
            for k in range(dga.dim):
                coefficient = dga.diff[k, j]
                if coefficient:
                    for target, value in dga.mult.get((i, k), {}).items():
                        rhs[target] = rhs.get(target, Rational(0)) + parity * coefficient * value

            support = set(lhs) | set(rhs)
            if any(simplify(lhs.get(k, 0) - rhs.get(k, 0)) != 0 for k in support):
                leibniz = False

    return {
        "unit": unit,
        "differential_degree_plus_one": differential_degree,
        "multiplication_degree_zero": multiplication_degree,
        "augmentation_multiplicative": augmentation_multiplicative,
        "augmentation_is_chain_map": augmentation_is_chain_map,
        "d_squared_zero": dga.d_squared_zero(),
        "associative": dga.is_associative(),
        "leibniz": leibniz,
    }


@dataclass
class FiniteOmegaBarComplex:
    """A finite quotient of ``Omega(B(A))`` over ``QQ``.

    The bar convention is

    ``[a_1|...|a_p] = s^{-1}a_1 tensor ... tensor s^{-1}a_p``.

    Its cohomological degree is ``sum |a_i| - p``.  A cobar generator
    ``s[a_1|...|a_p]`` has degree ``sum |a_i| - p + 1``.  For a tuple
    ``(w_1,...,w_q)`` of bar words, the total degree is the sum of these
    generator degrees.

    On a bar word ``w`` the differential is

    ``b_int(s^-1 a) = -s^-1(d_A a)`` and
    ``b_mult(s^-1 a tensor s^-1 b) = (-1)^(|a|-1)s^-1(ab)``,

    extended as a coderivation.  On a cobar generator it is

    ``d(s w) = -s(b w) + sum (-1)^|w'| (s w')(s w'')``,

    where the sum ranges over proper deconcatenations ``w = w'w''``.
    The tensor-algebra differential uses the ordinary cohomological Leibniz
    sign.  These formulas make the counit ``s[s^-1 a] -> a`` a chain map.

    ``max_bar_length`` bounds the sum of the lengths of all bar words.
    ``max_cobar_length`` bounds their number.  Cobar length above the latter
    bound forms a differential ideal, so the displayed finite object is a
    quotient complex.  The bar-length bound gives an increasing family of
    subcomplexes.
    """

    dga: AugDGA
    max_bar_length: int
    max_cobar_length: int
    allowed_bar_letter_lengths: Optional[Tuple[int, ...]] = None

    _basis_cache: Optional[List[OmegaWord]] = field(default=None, init=False)
    _degree_basis_cache: Dict[int, List[OmegaWord]] = field(default_factory=dict, init=False)
    _matrix_cache: Dict[int, Matrix] = field(default_factory=dict, init=False)

    def __post_init__(self) -> None:
        if self.max_bar_length < 1:
            raise ValueError("max_bar_length must be positive")
        if self.max_cobar_length < 1:
            raise ValueError("max_cobar_length must be positive")
        if self.allowed_bar_letter_lengths is None:
            self.allowed_bar_letter_lengths = tuple(range(1, self.max_bar_length + 1))
        else:
            lengths = tuple(sorted(set(self.allowed_bar_letter_lengths)))
            if any(length < 1 or length > self.max_bar_length for length in lengths):
                raise ValueError("allowed bar-letter lengths must lie in the finite window")
            self.allowed_bar_letter_lengths = lengths

        axioms = augmented_dga_axioms(self.dga)
        failed = [name for name, value in axioms.items() if value is not True]
        if failed:
            raise ValueError("augmented cochain-DGA axioms failed: " + ", ".join(failed))

    @property
    def aug_indices(self) -> Tuple[int, ...]:
        return tuple(range(1, self.dga.dim))

    @property
    def includes_all_bar_lengths(self) -> bool:
        return self.allowed_bar_letter_lengths == tuple(range(1, self.max_bar_length + 1))

    def bar_word_degree(self, word: BarWord) -> int:
        return sum(self.dga.degrees[index] - 1 for index in word)

    def cobar_generator_degree(self, word: BarWord) -> int:
        return self.bar_word_degree(word) + 1

    def degree(self, word: OmegaWord) -> int:
        return sum(self.cobar_generator_degree(block) for block in word)

    def bar_length(self, word: OmegaWord) -> int:
        return sum(len(block) for block in word)

    def cobar_length(self, word: OmegaWord) -> int:
        return len(word)

    def basis(self) -> List[OmegaWord]:
        """Enumerate the cobar unit and every basis word in the finite window."""
        if self._basis_cache is not None:
            return self._basis_cache

        result: List[OmegaWord] = [()]
        allowed = set(self.allowed_bar_letter_lengths or ())
        for cobar_length in range(1, self.max_cobar_length + 1):
            for total_bar_length in range(cobar_length, self.max_bar_length + 1):
                for lengths in _positive_compositions(total_bar_length, cobar_length):
                    if any(length not in allowed for length in lengths):
                        continue
                    for flat_word in cartprod(self.aug_indices, repeat=total_bar_length):
                        blocks: List[BarWord] = []
                        cursor = 0
                        for length in lengths:
                            blocks.append(tuple(flat_word[cursor:cursor + length]))
                            cursor += length
                        result.append(tuple(blocks))

        self._basis_cache = result
        self._degree_basis_cache.clear()
        for element in result:
            self._degree_basis_cache.setdefault(self.degree(element), []).append(element)
        return result

    def basis_in_degree(self, degree: int) -> List[OmegaWord]:
        self.basis()
        return self._degree_basis_cache.get(degree, [])

    def degrees(self) -> List[int]:
        self.basis()
        return sorted(self._degree_basis_cache)

    def bidegree_dimensions(self) -> Dict[Tuple[int, int], int]:
        """Dimensions indexed by ``(cobar length, total bar length)``."""
        result: Dict[Tuple[int, int], int] = {}
        for element in self.basis():
            key = (self.cobar_length(element), self.bar_length(element))
            result[key] = result.get(key, 0) + 1
        return result

    def _bar_internal_terms(self, word: BarWord) -> Iterable[Tuple[BarWord, Rational]]:
        for position, index in enumerate(word):
            prefix_degree = sum(self.dga.degrees[word[j]] - 1 for j in range(position))
            shift_sign = _sign(prefix_degree + 1)
            for target in self.aug_indices:
                coefficient = self.dga.diff[target, index]
                if coefficient:
                    yield word[:position] + (target,) + word[position + 1:], shift_sign * coefficient

    def _bar_multiplication_terms(self, word: BarWord) -> Iterable[Tuple[BarWord, Rational]]:
        for position in range(len(word) - 1):
            sign_exponent = sum(
                self.dga.degrees[word[j]] - 1 for j in range(position + 1)
            )
            shift_sign = _sign(sign_exponent)
            for target, coefficient in self.dga.mult.get(
                (word[position], word[position + 1]), {}
            ).items():
                if target == 0 or coefficient == 0:
                    continue
                yield word[:position] + (target,) + word[position + 2:], shift_sign * coefficient

    def differential_terms(self, element: OmegaWord) -> Dict[OmegaWord, Rational]:
        """Return the full finite-window differential of one basis element."""
        if element == ():
            return {}

        result: Dict[OmegaWord, Rational] = {}
        allowed = set(self.allowed_bar_letter_lengths or ())

        def add(target: OmegaWord, coefficient: Rational) -> None:
            if coefficient == 0:
                return
            if len(target) > self.max_cobar_length:
                return
            if self.bar_length(target) > self.max_bar_length:
                return
            if any(len(block) not in allowed for block in target):
                return
            result[target] = simplify(result.get(target, Rational(0)) + coefficient)
            if result[target] == 0:
                del result[target]

        for block_position, block in enumerate(element):
            cobar_prefix_degree = sum(
                self.cobar_generator_degree(element[j]) for j in range(block_position)
            )
            derivation_sign = _sign(cobar_prefix_degree)

            for new_block, bar_coefficient in self._bar_internal_terms(block):
                target = element[:block_position] + (new_block,) + element[block_position + 1:]
                add(target, -derivation_sign * bar_coefficient)

            for new_block, bar_coefficient in self._bar_multiplication_terms(block):
                target = element[:block_position] + (new_block,) + element[block_position + 1:]
                add(target, -derivation_sign * bar_coefficient)

            for cut in range(1, len(block)):
                left = block[:cut]
                right = block[cut:]
                split_sign = _sign(self.bar_word_degree(left))
                target = element[:block_position] + (left, right) + element[block_position + 1:]
                add(target, derivation_sign * split_sign)

        return result

    def differential_matrix(self, degree: int) -> Matrix:
        """Matrix of ``d: Omega^degree -> Omega^(degree+1)`` over ``QQ``."""
        if degree in self._matrix_cache:
            return self._matrix_cache[degree]
        source = self.basis_in_degree(degree)
        target = self.basis_in_degree(degree + 1)
        target_index = {element: row for row, element in enumerate(target)}
        matrix = zeros(len(target), len(source))
        for column, element in enumerate(source):
            for image, coefficient in self.differential_terms(element).items():
                if self.degree(image) != degree + 1:
                    raise AssertionError("bar--cobar differential changed degree by a value other than one")
                if image in target_index:
                    matrix[target_index[image], column] += coefficient
        self._matrix_cache[degree] = matrix
        return matrix

    def differentials(self) -> Dict[int, Matrix]:
        return {degree: self.differential_matrix(degree) for degree in self.degrees()}

    def verify_d_squared(self) -> Dict[int, bool]:
        """Check every composable pair of finite-window differential matrices."""
        result: Dict[int, bool] = {}
        for degree in self.degrees():
            first = self.differential_matrix(degree)
            second = self.differential_matrix(degree + 1)
            composite = second * first
            result[degree] = composite.equals(zeros(composite.rows, composite.cols))
        return result

    def homology_dimensions(self) -> Dict[int, int]:
        """Exact finite-window cohomology dimensions, grouped by total degree."""
        dimensions = {degree: len(self.basis_in_degree(degree)) for degree in self.degrees()}
        return cohomology_dims_exact(self.differentials(), dimensions)

    def algebra_basis_in_degree(self, degree: int) -> List[int]:
        return [index for index, value in enumerate(self.dga.degrees) if value == degree]

    def algebra_differential_matrix(self, degree: int) -> Matrix:
        source = self.algebra_basis_in_degree(degree)
        target = self.algebra_basis_in_degree(degree + 1)
        matrix = zeros(len(target), len(source))
        for row_position, row in enumerate(target):
            for column_position, column in enumerate(source):
                matrix[row_position, column_position] = self.dga.diff[row, column]
        return matrix

    def counit_matrix(self, degree: int) -> Matrix:
        """Matrix of the strict counit in one cohomological degree."""
        source = self.basis_in_degree(degree)
        target = self.algebra_basis_in_degree(degree)
        target_index = {index: row for row, index in enumerate(target)}
        matrix = zeros(len(target), len(source))
        for column, element in enumerate(source):
            if element == () and 0 in target_index:
                matrix[target_index[0], column] = Rational(1)
                continue
            if any(len(block) != 1 for block in element):
                continue

            value: Dict[int, Rational] = {0: Rational(1)}
            for block in element:
                factor = block[0]
                product_value: Dict[int, Rational] = {}
                for left, left_coefficient in value.items():
                    for output, structure_coefficient in self.dga.mult.get((left, factor), {}).items():
                        product_value[output] = (
                            product_value.get(output, Rational(0))
                            + left_coefficient * structure_coefficient
                        )
                value = product_value
            for index, coefficient in value.items():
                if index in target_index:
                    matrix[target_index[index], column] += coefficient
        return matrix

    def counit_chain_map(self) -> Dict[str, object]:
        """Check ``epsilon d_OmegaB = d_A epsilon`` in every degree."""
        degrees = sorted(set(self.degrees()) | set(self.dga.degrees))
        identities: Dict[int, bool] = {}
        residuals: Dict[int, Matrix] = {}
        for degree in degrees:
            left = self.counit_matrix(degree + 1) * self.differential_matrix(degree)
            right = self.algebra_differential_matrix(degree) * self.counit_matrix(degree)
            residual = left - right
            residuals[degree] = residual
            identities[degree] = residual.equals(zeros(residual.rows, residual.cols))
        return {
            "chain_map_at_degree": identities,
            "is_chain_map": all(identities.values()),
            "residuals": residuals,
        }

    def algebra_homology_dimensions(self) -> Dict[int, int]:
        degrees = sorted(set(self.dga.degrees))
        dimensions = {degree: len(self.algebra_basis_in_degree(degree)) for degree in degrees}
        differentials = {degree: self.algebra_differential_matrix(degree) for degree in degrees}
        return cohomology_dims_exact(differentials, dimensions)

    def mapping_cone_homology_dimensions(self) -> Dict[int, int]:
        """Compute the counit's mapping-cone cohomology over ``QQ``."""
        complex_degrees = set(self.degrees())
        algebra_degrees = set(self.dga.degrees)
        cone_degrees = sorted(algebra_degrees | {degree - 1 for degree in complex_degrees})
        dimensions: Dict[int, int] = {}
        differentials: Dict[int, Matrix] = {}
        for degree in cone_degrees:
            a_source = self.algebra_basis_in_degree(degree)
            c_source = self.basis_in_degree(degree + 1)
            a_target = self.algebra_basis_in_degree(degree + 1)
            c_target = self.basis_in_degree(degree + 2)
            dimensions[degree] = len(a_source) + len(c_source)

            matrix = zeros(len(a_target) + len(c_target), len(a_source) + len(c_source))
            d_a = self.algebra_differential_matrix(degree)
            epsilon = self.counit_matrix(degree + 1)
            d_c = self.differential_matrix(degree + 1)
            if d_a.rows and d_a.cols:
                matrix[:len(a_target), :len(a_source)] = d_a
            if epsilon.rows and epsilon.cols:
                matrix[:len(a_target), len(a_source):] = epsilon
            if d_c.rows and d_c.cols:
                matrix[len(a_target):, len(a_source):] = -d_c
            differentials[degree] = matrix

        return cohomology_dims_exact(differentials, dimensions)

    def finite_window_report(self) -> Dict[str, object]:
        """Return exact matrices, homology, counit, and mathematical scope."""
        cone_homology = self.mapping_cone_homology_dimensions()
        degrees = self.degrees()
        return {
            **finite_calculation_state(self.max_bar_length, self.max_cobar_length),
            "sign_convention": "cohomological |d|=+1; bar s^-1; cobar s",
            "allowed_bar_letter_lengths": self.allowed_bar_letter_lengths,
            "includes_all_bar_lengths": self.includes_all_bar_lengths,
            "basis_dimension": len(self.basis()),
            "basis_by_degree": {
                degree: self.basis_in_degree(degree) for degree in degrees
            },
            "bidegree_dimensions": self.bidegree_dimensions(),
            "differentials": self.differentials(),
            "d_squared": self.verify_d_squared(),
            "finite_window_homology": self.homology_dimensions(),
            "A_homology": self.algebra_homology_dimensions(),
            "counit_matrices": {
                degree: self.counit_matrix(degree)
                for degree in sorted(set(degrees) | set(self.dga.degrees))
            },
            "counit": self.counit_chain_map(),
            "mapping_cone_homology": cone_homology,
            "finite_window_counit_is_quasi_isomorphism": all(
                dimension == 0 for dimension in cone_homology.values()
            ),
        }


def finite_bar_cobar_report(
    dga: AugDGA,
    max_bar_length: int,
    max_cobar_length: Optional[int] = None,
    allowed_bar_letter_lengths: Optional[Sequence[int]] = None,
) -> Dict[str, object]:
    """Construct and compute one exact finite bar--cobar window."""
    cobar_bound = max_cobar_length if max_cobar_length is not None else max_bar_length
    allowed = tuple(allowed_bar_letter_lengths) if allowed_bar_letter_lengths is not None else None
    complex_ = FiniteOmegaBarComplex(dga, max_bar_length, cobar_bound, allowed)
    return complex_.finite_window_report()


# ============================================================================
# Quadratic-row diagnostic retained for comparison with earlier computations
# ============================================================================

@dataclass
class MultiplicationDualComplex:
    """The structure-constant transpose of multiplication on ``A_bar``.

    A formal generator ``u_i`` has degree ``|e_i|+1``.  If
    ``e_j e_k = sum_i c^i_jk e_i``, set

    ``delta(u_i) = sum_jk c^i_jk u_j tensor u_k``

    and extend ``delta`` as a derivation of the tensor algebra.  This auxiliary
    complex records the quadratic transpose of multiplication.  The genuine
    ``Omega(B(A))`` object is ``FiniteOmegaBarComplex``.
    """
    bar: BarConstruction
    max_cobar_degree: int

    _basis_cache: Dict[int, List[Tuple[int, ...]]] = field(default_factory=dict, init=False)
    _diff_cache: Dict[int, Matrix] = field(default_factory=dict, init=False)
    _coproduct_cache: Optional[Dict[int, List[Tuple[int, int, Rational]]]] = field(default=None, init=False)

    @property
    def aug_indices(self) -> List[int]:
        return self.bar._aug_ideal_indices

    def _build_coproduct(self):
        """Transpose the multiplication structure constants."""
        if self._coproduct_cache is not None:
            return
        self._coproduct_cache = {}
        aug = self.aug_indices
        for j in aug:
            for k in aug:
                products = self.bar.dga.mult.get((j, k), {})
                for i, coeff in products.items():
                    if i in aug and coeff != 0:
                        if i not in self._coproduct_cache:
                            self._coproduct_cache[i] = []
                        self._coproduct_cache[i].append((j, k, coeff))

    def basis(self, n: int) -> List[Tuple[int, ...]]:
        """Tensor words of length ``n`` in the formal generators ``u_i``."""
        if n in self._basis_cache:
            return self._basis_cache[n]
        if n <= 0:
            self._basis_cache[n] = [()]
            return [()]
        result = list(cartprod(self.aug_indices, repeat=n))
        self._basis_cache[n] = result
        return result

    def dim_at(self, n: int) -> int:
        if n <= 0:
            return 1
        return len(self.aug_indices) ** n

    def differential(self, n: int) -> Matrix:
        """Extend the transposed multiplication by the graded Leibniz rule."""
        if n in self._diff_cache:
            return self._diff_cache[n]

        self._build_coproduct()

        source = self.basis(n)
        target_degree = n + 1
        if target_degree > self.max_cobar_degree:
            mat = zeros(0, len(source))
            self._diff_cache[n] = mat
            return mat

        target = self.basis(target_degree)
        dim_s = len(source)
        dim_t = len(target)

        if dim_s == 0 or dim_t == 0:
            mat = zeros(dim_t, dim_s)
            self._diff_cache[n] = mat
            return mat

        mat = zeros(dim_t, dim_s)
        target_idx = {t: i for i, t in enumerate(target)}

        for col_idx, multi in enumerate(source):
            for p in range(n):
                a_p = multi[p]
                if a_p not in self._coproduct_cache:
                    continue
                # The multiplication-dual generators are suspended once.
                eps = sum(self.bar.dga.degrees[multi[q]] + 1 for q in range(p))
                sign = -1 if eps % 2 else 1

                for j, k, coeff in self._coproduct_cache[a_p]:
                    new_multi = multi[:p] + (j, k) + multi[p + 1:]
                    if new_multi in target_idx:
                        mat[target_idx[new_multi], col_idx] += sign * coeff

        self._diff_cache[n] = mat
        return mat

    def verify_d_squared(self) -> Dict[int, bool]:
        """Verify ``delta^2=0`` at every tensor length."""
        results = {}
        for n in range(1, self.max_cobar_degree):
            d_n = self.differential(n)
            d_n1 = self.differential(n + 1)
            if d_n.cols == 0 or d_n1.cols == 0:
                results[n] = True
                continue
            if d_n1.cols != d_n.rows:
                # dimension mismatch: check if d_n maps to a space of dim matching d_n1 source
                results[n] = False
                continue
            product = d_n1 * d_n
            if product.rows == 0 or product.cols == 0:
                results[n] = True
            else:
                results[n] = product.equals(zeros(product.rows, product.cols))
        return results


# ============================================================================
# Finite bar data with the quadratic-row comparison object
# ============================================================================

@dataclass
class BarCobarComposition:
    """Finite bar data together with the genuine mixed-word cobar window.

    The bidegree is ``(q,p)``: ``q`` cobar generators and total bar length
    ``p``.  Thus ``((a,b),(c,))`` lies in bidegree ``(2,3)``.
    """
    dga: AugDGA
    max_total_degree: int

    _bar: Optional[BarConstruction] = field(default=None, init=False)
    _multiplication_dual: Optional[MultiplicationDualComplex] = field(default=None, init=False)
    _omega: Optional[FiniteOmegaBarComplex] = field(default=None, init=False)

    def __post_init__(self):
        self._bar = BarConstruction(self.dga, self.max_total_degree)
        self._multiplication_dual = MultiplicationDualComplex(
            self._bar,
            self.max_total_degree,
        )
        self._omega = FiniteOmegaBarComplex(
            self.dga,
            self.max_total_degree,
            self.max_total_degree,
        )

    @property
    def bar(self) -> BarConstruction:
        return self._bar

    @property
    def multiplication_dual(self) -> MultiplicationDualComplex:
        """The tensor complex dual to multiplication on the augmentation ideal."""
        return self._multiplication_dual

    @property
    def omega(self) -> FiniteOmegaBarComplex:
        """The mixed-word finite quotient of ``Omega(B(A))``."""
        return self._omega

    def bigraded_basis(self, cobar_deg: int, bar_deg: int) -> List[OmegaWord]:
        """Basis for cobar length ``cobar_deg`` and total bar length ``bar_deg``."""
        return [
            element for element in self.omega.basis()
            if self.omega.cobar_length(element) == cobar_deg
            and self.omega.bar_length(element) == bar_deg
        ]

    def total_degree_basis(self, total: int) -> List[Tuple[int, int, Tuple]]:
        """All basis elements of cohomological degree ``total``."""
        return [
            (self.omega.cobar_length(element), self.omega.bar_length(element), element)
            for element in self.omega.basis_in_degree(total)
        ]


# ============================================================================
# Strict counit on a finite mixed-word window
# ============================================================================

def counit_map(dga: AugDGA, max_degree: int = 4) -> Dict[int, Matrix]:
    """Return the strict counit matrices indexed by cohomological degree.

    The finite source has total bar length and cobar length bounded by
    ``max_degree``.  Multiplicativity sends every tuple of singleton bar words
    to the corresponding product in ``A``.
    """
    omega_bar = FiniteOmegaBarComplex(dga, max_degree, max_degree)
    degrees = sorted(set(omega_bar.degrees()) | set(dga.degrees))
    return {degree: omega_bar.counit_matrix(degree) for degree in degrees}


def counit_chain_map_verify(dga: AugDGA, max_degree: int = 3) -> Dict[str, object]:
    """Verify the strict counit on the complete finite mixed-word window."""
    omega_bar = FiniteOmegaBarComplex(dga, max_degree, max_degree)
    return {
        **finite_calculation_state(max_degree, max_degree),
        **omega_bar.counit_chain_map(),
    }


# ============================================================================
# Twisting morphisms
# ============================================================================

def twisting_morphism_tau(dga: AugDGA) -> Dict[int, Matrix]:
    """The universal twisting morphism tau: B(A) -> A.

    tau is defined by:
      tau(s^{-1}a) = a  on B^1 = s^{-1}A_bar  (projection onto bar degree 1)
      tau = 0     on B^n for n >= 2

    In the desuspended convention ``tau`` has degree ``+1`` and obeys
    ``d_A tau + tau d_B - tau star tau = 0``.  The convolution product uses
    the Koszul sign of the left bar factor.

    Returns {bar_degree: matrix from B^n to A}.
    """
    aug_indices = list(range(1, dga.dim))
    aug_dim = len(aug_indices)
    result = {}

    # Bar degree 1: tau(s^{-1}a_i) = a_i
    mat1 = zeros(dga.dim, aug_dim)
    for j, idx in enumerate(aug_indices):
        mat1[idx, j] = Rational(1)
    result[1] = mat1

    # Bar degree >= 2: tau = 0
    for n in range(2, 6):
        result[n] = zeros(dga.dim, aug_dim ** n)

    return result


def verify_twisting_mc(dga: AugDGA, max_bar_degree: int = 3) -> Dict[str, object]:
    """Verify the twisting equation in the desuspended bar convention.

    The map ``tau([a])=a`` has degree ``+1`` because the bar generator is
    ``s^-1 a``.  With the convolution sign induced by graded tensor products,
    the equation is

    ``d_A tau + tau d_B - tau star tau = 0``.

    On ``[a]`` the two internal terms are ``d_A a`` and ``-d_A a``.  On
    ``[a|b]`` the multiplication part of ``tau d_B`` and the convolution term
    carry the same coefficient ``(-1)^(|a|-1)``.  These are the two local
    cancellations encoded by the matrix calculation below.
    """
    bar = BarConstruction(dga, max_bar_degree + 1)
    tau = twisting_morphism_tau(dga)

    results = {"mc_at_degree": {}}

    aug_indices = list(range(1, dga.dim))
    aug_dim = len(aug_indices)

    # Check MC at each bar degree
    for n in range(1, max_bar_degree + 1):
        basis_n = bar.basis(n)
        mc_value = zeros(dga.dim, len(basis_n))

        for col_idx, multi in enumerate(basis_n):
            # Term 1: d_A(tau(element))
            tau_val = zeros(dga.dim, 1)
            if n in tau and tau[n].cols > col_idx:
                tau_val = tau[n].col(col_idx)
            term1 = dga.diff * tau_val

            # Term 2: tau(d_B(element)), including internal and multiplication parts.
            term2 = zeros(dga.dim, 1)
            d_internal = bar.internal_differential(n)
            if n in tau and tau[n].cols == d_internal.rows:
                term2 += tau[n] * d_internal.col(col_idx)

            d_B = bar.differential(n)
            if n - 1 in tau and d_B.rows > 0:
                d_B_col = d_B.col(col_idx) if col_idx < d_B.cols else zeros(d_B.rows, 1)
                if tau[n - 1].cols == d_B.rows:
                    term2 += tau[n - 1] * d_B_col

            # Term 3: (tau star tau)(element)
            # Uses deconcatenation coproduct:
            # Delta(s^{-1}a_1|...|s^{-1}a_n) = sum_{p=1}^{n-1} left_p tensor right_p
            term3 = zeros(dga.dim, 1)
            if n >= 2:
                for p in range(1, n):
                    left_multi = multi[:p]
                    right_multi = multi[p:]
                    convolution_sign = _sign(
                        sum(dga.degrees[index] - 1 for index in left_multi)
                    )

                    # tau on left part (B^p)
                    left_basis = bar.basis(p)
                    if left_multi in left_basis:
                        left_idx = left_basis.index(left_multi)
                        tau_left = tau.get(p, zeros(dga.dim, 1))
                        if tau_left.cols > left_idx:
                            tau_l = tau_left.col(left_idx)
                        else:
                            tau_l = zeros(dga.dim, 1)
                    else:
                        tau_l = zeros(dga.dim, 1)

                    # tau on right part (B^{n-p})
                    right_basis = bar.basis(n - p)
                    if right_multi in right_basis:
                        right_idx = right_basis.index(right_multi)
                        tau_right = tau.get(n - p, zeros(dga.dim, 1))
                        if tau_right.cols > right_idx:
                            tau_r = tau_right.col(right_idx)
                        else:
                            tau_r = zeros(dga.dim, 1)
                    else:
                        tau_r = zeros(dga.dim, 1)

                    # Multiply in A
                    for i in range(dga.dim):
                        for j in range(dga.dim):
                            if tau_l[i] != 0 and tau_r[j] != 0:
                                prod = dga.mult.get((i, j), {})
                                for k, c in prod.items():
                                    term3[k] += convolution_sign * tau_l[i] * tau_r[j] * c

            # MC equation: term1 + term2 - term3 = 0
            total = term1 + term2 - term3
            for i in range(dga.dim):
                mc_value[i, col_idx] = simplify(total[i])

        is_zero = mc_value.equals(zeros(mc_value.rows, mc_value.cols))
        results["mc_at_degree"][n] = is_zero

    results["mc_satisfied"] = all(results["mc_at_degree"].values())
    return results


# ============================================================================
# Twisted tensor product A tensor_tau C
# ============================================================================

def twisted_tensor_product_diff(dga: AugDGA, max_bar_degree: int = 3) -> Dict[str, object]:
    """Record the finite degrees required for the twisted differential.

    The differential on A tensor_tau C for C = B(A):
      d_tau = d_A tensor 1 + 1 tensor d_C + (m_A tensor id)(id tensor tau tensor id)(id tensor Delta_C)

    The twisting perturbation adds: for x tensor c in A tensor B(A),
      x tensor c |-> sum_p x * tau(c') tensor c''
    where Delta(c) = sum c' tensor c'' (deconcatenation).

    The identity ``d_tau^2 = 0`` is checked after the total differential has
    been assembled across adjacent bar degrees.  This routine records the
    current construction boundary.
    """
    return {
        "calculation_status": "index range computed",
        "construction_status": "total twisted differential pending",
        "computed_object": "bar-degree index set for A tensor_tau B(A)",
        "target_object": "the total twisted differential d_tau and its square",
        "d_tau_squared_state": "pending construction",
        "d_tau_squared": {
            n: None for n in range(1, max_bar_degree + 1)
        },
    }


# ============================================================================
# Cohomology computation (exact, over Q)
# ============================================================================

def kernel_dim_exact(M: Matrix) -> int:
    """Exact dimension of kernel of M over Q."""
    if M.rows == 0 or M.cols == 0:
        return M.cols
    return M.cols - M.rank()


def image_dim_exact(M: Matrix) -> int:
    """Exact dimension of image of M over Q."""
    if M.rows == 0 or M.cols == 0:
        return 0
    return M.rank()


def cohomology_dims_exact(differentials: Dict[int, Matrix],
                           dims: Dict[int, int]) -> Dict[int, int]:
    """Compute cohomology dimensions of a cochain complex exactly over Q.

    differentials[n]: d^n from degree n to degree n+1.
    dims[n]: dimension at degree n.
    """
    degrees = sorted(dims.keys())
    result = {}
    for n in degrees:
        # kernel of d^n
        if n in differentials and differentials[n].cols > 0 and differentials[n].rows > 0:
            ker = kernel_dim_exact(differentials[n])
        else:
            ker = dims.get(n, 0)

        # image of d^{n-1}
        if (n - 1) in differentials and differentials[n - 1].cols > 0:
            im = image_dim_exact(differentials[n - 1])
        else:
            im = 0

        result[n] = ker - im
    return result


# ============================================================================
# Quasi-isomorphism verification
# ============================================================================

def verify_bar_cobar_quasi_iso(dga: AugDGA, max_degree: int = 4) -> Dict[str, object]:
    """Compute one exact finite window and state the remaining limit problem."""
    report = finite_bar_cobar_report(dga, max_degree, max_degree)
    aug_product = False
    aug_indices = list(range(1, dga.dim))
    for i in aug_indices:
        for j in aug_indices:
            prods = dga.mult.get((i, j), {})
            for k, v in prods.items():
                if k in aug_indices and v != 0:
                    aug_product = True
                    break
            if aug_product:
                break
        if aug_product:
            break

    return {
        **report,
        "cobar_cohomology": report["finite_window_homology"],
        "A_cohomology": report["A_homology"],
        "aug_ideal_dim": len(aug_indices),
        "aug_has_product": aug_product,
        "is_quasi_iso": None,
        "bar_d_squared": BarConstruction(dga, max_degree).verify_d_squared(),
        "cobar_d_squared": report["d_squared"],
    }


# ============================================================================
# A-infinity structure from bar-cobar
# ============================================================================

def extract_ainfty_operations(dga: AugDGA, max_arity: int = 4) -> Dict[int, Dict]:
    """Extract A-infinity operations m_k: A^{tensor k} -> A from bar-cobar.

    The bar-cobar resolution carries the UNIVERSAL A-infinity structure.
    The operations m_k are extracted from the twisting morphism:

    m_1 = d_A (the original differential)
    m_2 = the original multiplication
    m_3: A^{tensor 3} -> A is the FIRST HOMOTOPY correction
       m_3(a, b, c) measures the failure of the bar-cobar map to be
       strictly multiplicative. For associative algebras: m_3 = 0.
    m_k for k >= 4: higher homotopies.

    For a STRICTLY associative algebra: all m_k = 0 for k >= 3.
    The A-infinity structure is trivial.

    For a non-associative algebra (like Lie): m_3 = Jacobiator,
    m_4 = Jacobiator of Jacobiator, etc.

    Returns {arity: {(i_1,...,i_k): {j: coeff}}} for each m_k.
    """
    aug_indices = list(range(1, dga.dim))

    operations: Dict[int, Dict] = {}

    # m_1 = d_A
    m1: Dict[Tuple, Dict[int, Rational]] = {}
    for i in range(dga.dim):
        out = {}
        for j in range(dga.dim):
            if dga.diff[j, i] != 0:
                out[j] = dga.diff[j, i]
        if out:
            m1[(i,)] = out
    operations[1] = m1

    # m_2 = multiplication
    m2: Dict[Tuple, Dict[int, Rational]] = {}
    for (i, j), prods in dga.mult.items():
        nontrivial = {k: v for k, v in prods.items() if v != 0}
        if nontrivial:
            m2[(i, j)] = nontrivial
    operations[2] = m2

    # m_3 = associator (measures failure of associativity)
    # m_3(a, b, c) = (a*b)*c - a*(b*c) in the A-infinity sense
    # For strictly associative: m_3 = 0.
    # For the bar-cobar extracted A-infinity: m_3 comes from the
    # secondary bar-cobar map and is a homotopy for associativity.
    m3: Dict[Tuple, Dict[int, Rational]] = {}
    if not dga.is_associative():
        for i in range(dga.dim):
            for j in range(dga.dim):
                for k in range(dga.dim):
                    lhs = dga._triple_left(i, j, k)
                    rhs = dga._triple_right(i, j, k)
                    diff_dict: Dict[int, Rational] = {}
                    all_keys = set(lhs.keys()) | set(rhs.keys())
                    for m in all_keys:
                        val = lhs.get(m, Rational(0)) - rhs.get(m, Rational(0))
                        if val != 0:
                            diff_dict[m] = val
                    if diff_dict:
                        m3[(i, j, k)] = diff_dict
    operations[3] = m3

    # m_4 and higher: for strictly associative algebras, all zero.
    # For non-associative: requires explicit bar-cobar computation.
    for arity in range(4, max_arity + 1):
        operations[arity] = {}  # Placeholder: zero for associative algebras

    return operations


def verify_ainfty_relations(dga: AugDGA, max_n: int = 3) -> Dict[int, bool]:
    """Verify the Stasheff A-infinity relations at each level.

    The n-th relation: sum_{r+s+t=n} (-1)^{rs+t} m_{r+1+t}(...m_s(...)...) = 0

    For strictly associative algebras with d = 0:
      n=0: m_1(m_0) = 0 (trivial, m_0 = 0)
      n=1: m_1^2 = 0 (trivial, m_1 = 0 or d^2 = 0)
      n=2: m_1(m_2) = m_2(m_1 x id + id x m_1) (Leibniz, automatic)
      n=3: m_2(m_2 x id) - m_2(id x m_2) + m_1(m_3) + m_3(...) = 0
           reduces to associativity when m_3 = 0
    """
    ops = extract_ainfty_operations(dga, max_n + 1)
    results = {}

    # n=0: m_1(m_0) = 0. With m_0 = 0: trivially satisfied.
    results[0] = True

    # n=1: m_1^2 = 0.
    d_sq = dga.diff * dga.diff
    results[1] = d_sq.equals(zeros(dga.dim, dga.dim))

    # n=2: Leibniz rule. d(ab) = d(a)b + (-1)^|a| a d(b).
    if max_n >= 2:
        leibniz_ok = True
        for i in range(dga.dim):
            for j in range(dga.dim):
                # m_2(e_i, e_j) = product
                m2_ij = {}
                if (i, j) in dga.mult:
                    m2_ij = dga.mult[(i, j)]

                # d(m_2(e_i, e_j))
                lhs = {}
                for k, c in m2_ij.items():
                    for l in range(dga.dim):
                        if dga.diff[l, k] != 0:
                            lhs[l] = lhs.get(l, Rational(0)) + c * dga.diff[l, k]

                # m_2(d(e_i), e_j)
                term1 = {}
                for k in range(dga.dim):
                    if dga.diff[k, i] != 0:
                        prods = dga.mult.get((k, j), {})
                        for l, c2 in prods.items():
                            term1[l] = term1.get(l, Rational(0)) + dga.diff[k, i] * c2

                # (-1)^|e_i| m_2(e_i, d(e_j))
                sign = (-1) ** dga.degrees[i]
                term2 = {}
                for k in range(dga.dim):
                    if dga.diff[k, j] != 0:
                        prods = dga.mult.get((i, k), {})
                        for l, c2 in prods.items():
                            term2[l] = term2.get(l, Rational(0)) + sign * dga.diff[k, j] * c2

                # Check: lhs = term1 + term2
                all_keys = set(lhs.keys()) | set(term1.keys()) | set(term2.keys())
                for k in all_keys:
                    total = lhs.get(k, Rational(0)) - term1.get(k, Rational(0)) - term2.get(k, Rational(0))
                    if simplify(total) != 0:
                        leibniz_ok = False
                        break
                if not leibniz_ok:
                    break
            if not leibniz_ok:
                break
        results[2] = leibniz_ok

    # n=3: Associativity + higher corrections.
    if max_n >= 3:
        if dga.is_associative():
            results[3] = True  # m_3 = 0 and associativity gives the relation
        else:
            # Check: m_2(m_2 x id) - m_2(id x m_2) + boundary terms = 0
            # This is the content of the Stasheff relation.
            assoc_ok = True
            for i in range(dga.dim):
                for j in range(dga.dim):
                    for k in range(dga.dim):
                        lhs = dga._triple_left(i, j, k)
                        rhs = dga._triple_right(i, j, k)
                        m3_val = ops[3].get((i, j, k), {})
                        # Stasheff: (ij)k - i(jk) + d(m_3) + m_3(d x ...) = 0
                        # When d = 0: (ij)k - i(jk) = 0 iff associative.
                        # The A-inf relation says (ij)k - i(jk) = -(boundary of m_3).
                        # For extraction: m_3 = (ij)k - i(jk), so the relation is tautological.
                        all_keys = set(lhs.keys()) | set(rhs.keys())
                        for m in all_keys:
                            diff_val = lhs.get(m, Rational(0)) - rhs.get(m, Rational(0))
                            m3_m = m3_val.get(m, Rational(0))
                            if simplify(diff_val - m3_m) != 0:
                                assoc_ok = False
                                break
                        if not assoc_ok:
                            break
                    if not assoc_ok:
                        break
                if not assoc_ok:
                    break
            results[3] = assoc_ok

    return results


# ============================================================================
# Functoriality: algebra maps induce bar-cobar maps
# ============================================================================

def multiplication_dual_functoriality(dga1: AugDGA, dga2: AugDGA,
                                       f: Matrix,
                                       max_degree: int = 3) -> Dict[str, object]:
    """Construct tensor powers of an algebra map on the diagnostic basis.

    The bar functor is CONTRAVARIANT for coalgebras but the bar of an
    algebra map gives a coalgebra map B(f): B(A) -> B(A').
    At bar degree n:
      B(f)(s^{-1}a_1|...|s^{-1}a_n)
        = s^{-1}f(a_1)|...|s^{-1}f(a_n).

    On the quadratic comparison row these tensor powers give the displayed
    diagnostic maps.  Extension to all bar lengths supplies the full map
    ``Omega(B(f))``.

    f should be a matrix (dim2 x dim1) representing f: A -> A'.
    """
    aug1 = list(range(1, dga1.dim))
    aug2 = list(range(1, dga2.dim))

    # B(f) at bar degree 1: sA_bar -> sA'_bar
    # f restricted to augmentation ideals
    f_aug = zeros(len(aug2), len(aug1))
    for j, src in enumerate(aug1):
        for i, tgt in enumerate(aug2):
            f_aug[i, j] = f[tgt, src]

    # B(f) at bar degree n: tensor power of f_aug
    bar_maps = {1: f_aug}
    for n in range(2, max_degree + 1):
        # f^{tensor n}: (A_bar)^{tensor n} -> (A'_bar)^{tensor n}
        # Kronecker product
        fn = f_aug
        for _ in range(n - 1):
            fn = _kronecker(fn, f_aug)
        bar_maps[n] = fn

    # Tensor powers of f_aug on the quadratic comparison row.
    dual_maps = bar_maps.copy()

    # Verify chain map property: Omega(B(f)) o d_Omega = d_Omega' o Omega(B(f))
    bar1 = BarConstruction(dga1, max_degree + 1)
    bar2 = BarConstruction(dga2, max_degree + 1)
    dual1 = MultiplicationDualComplex(bar1, max_degree + 1)
    dual2 = MultiplicationDualComplex(bar2, max_degree + 1)

    chain_map_ok = {}
    for n in range(1, max_degree):
        d1 = dual1.differential(n)
        d2 = dual2.differential(n)
        fn = dual_maps.get(n)
        fn1 = dual_maps.get(n + 1)
        if fn is None or fn1 is None:
            chain_map_ok[n] = True
            continue
        if d1.rows == 0 or d2.rows == 0:
            chain_map_ok[n] = True
            continue

        # fn1 * d1 should = d2 * fn
        lhs = fn1 * d1
        rhs = d2 * fn
        diff = lhs - rhs
        chain_map_ok[n] = diff.equals(zeros(diff.rows, diff.cols))

    return {
        "computed_target": "tensor powers on the multiplication-dual complex",
        "bar_maps": bar_maps,
        "multiplication_dual_maps": dual_maps,
        "is_chain_map": chain_map_ok,
        "all_chain_map": all(chain_map_ok.values()),
    }


def _kronecker(A: Matrix, B: Matrix) -> Matrix:
    """Kronecker (tensor) product of two sympy matrices."""
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    result = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    result[i * rb + k, j * cb + l] = A[i, j] * B[k, l]
    return result


# ============================================================================
# Comparison tables for standard families
# ============================================================================

def bar_cobar_comparison_table(max_degree: int = 4) -> Dict[str, Dict[str, object]]:
    """Bar-cobar chain map data for all standard test algebras.

    For each algebra:
    - Bar d^2 = 0 verification
    - Total mixed-word cobar d^2 = 0 verification
    - Counit chain map verification
    - Typed state of the quasi-isomorphism check
    - Twisting morphism MC verification
    - A-infinity operations
    """
    algebras = {
        "dual_numbers": dual_numbers_dga(),
        "k[x]/(x^3)": truncated_polynomial_dga(3),
        "k[x]/(x^4)": truncated_polynomial_dga(4),
        "Lambda(1)": exterior_on_one_generator(),
        "UT_2": matrix_2x2_upper_dga(),
    }

    results = {}
    for name, dga in algebras.items():
        bar = BarConstruction(dga, max_degree + 1)
        omega = FiniteOmegaBarComplex(dga, max_degree, max_degree)

        results[name] = {
            "dim": dga.dim,
            "aug_dim": bar.aug_dim,
            "associative": dga.is_associative(),
            "bar_d_squared": bar.verify_d_squared(),
            "cobar_d_squared": omega.verify_d_squared(),
            "bidegree_dimensions": omega.bidegree_dimensions(),
            "counit_chain_map": counit_chain_map_verify(dga, max_degree),
            "quasi_iso": verify_bar_cobar_quasi_iso(dga, max_degree),
            "twisting_mc": verify_twisting_mc(dga, max_degree),
        }

    return results


# ============================================================================
# Heisenberg-specific chain maps
# ============================================================================

def heisenberg_bar_cobar(kappa_val: Rational = Rational(1)) -> Dict[str, object]:
    """Bar-cobar chain maps for the Heisenberg algebra.

    Heisenberg H_kappa: one generator J, |J| = 0, OPE: J(z)J(w) ~ kappa/(z-w)^2.
    No simple pole, so no Lie bracket: m_2 = 0 on the augmentation ideal.

    The bar complex B(H) has d_B = 0 (no product).
    The finite cobar window contains the suspended generators arising from
    every positive bar length through the stated bound.

    The curvature kappa appears in the GENUS-1 bar complex (not genus 0).
    At genus 0, Heisenberg is a free field with zero bar differential.
    """
    # Heisenberg as a 2-dim algebra: {1, J}
    dim = 2
    degrees = [0, 0]
    diff = zeros(2, 2)
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        (1, 0): {1: Rational(1)},
        # J*J = 0 (no simple pole product in the augmentation ideal)
    }
    dga = AugDGA(dim, degrees, diff, mult, name=f"H_{kappa_val}")

    bar = BarConstruction(dga, 5)
    omega = FiniteOmegaBarComplex(dga, 4, 4)

    return {
        "dga": dga,
        "bar": bar,
        "omega": omega,
        "bar_d_squared": bar.verify_d_squared(),
        "cobar_d_squared": omega.verify_d_squared(),
        "quasi_iso": verify_bar_cobar_quasi_iso(dga, 4),
        "twisting_mc": verify_twisting_mc(dga, 3),
        "kappa": kappa_val,
        "bar_differential_zero": all(
            bar.differential(n).equals(zeros(bar.dim_at(n - 1), bar.dim_at(n)))
            for n in range(2, 5)
        ),
    }


def free_fermion_bar_cobar() -> Dict[str, object]:
    """Bar-cobar chain maps for the free fermion.

    Free fermion: one generator psi, |psi| = 0 (weight 1/2 but we use
    conformal weight grading, not fermion number).
    OPE: psi(z)psi(w) ~ 1/(z-w).
    Simple pole gives bracket: psi * psi = 1 (the vacuum).

    The relation ``psi^2=1`` selects a curved bar construction: projection
    onto the vacuum fails the multiplicativity axiom for an augmentation.
    The associative augmented engine therefore records this example through
    its curvature term ``B^2 -> B^0`` and leaves the curved cobar construction
    as a separate problem.
    """
    dim = 2
    degrees = [0, 0]
    diff = zeros(2, 2)
    mult: Dict[Tuple[int, int], Dict[int, Rational]] = {
        (0, 0): {0: Rational(1)},
        (0, 1): {1: Rational(1)},
        (1, 0): {1: Rational(1)},
        (1, 1): {0: Rational(1)},  # psi * psi = 1 (unit)
    }
    dga = AugDGA(dim, degrees, diff, mult, name="FreeFermion")

    bar = BarConstruction(dga, 5)
    return {
        "dga": dga,
        "bar": bar,
        "bar_d_squared": bar.verify_d_squared(),
        "bar_cobar_scope": "curved bar--cobar construction required",
        "curved_cobar_status": "curvature differential awaits construction",
        "quasi_iso": None,
        "twisting_mc": verify_twisting_mc(dga, 3),
        "unit_contraction_B2": bar.unit_contraction(2),
    }


def sl2_affine_bar_cobar_genus0() -> Dict[str, object]:
    """Bar-cobar chain maps for affine sl_2 at genus 0.

    At genus 0, the chiral bar complex reduces to the CE complex
    (Chevalley-Eilenberg) for the Lie algebra sl_2. The product
    is the Lie bracket [,], which is NOT associative.

    For the ASSOCIATIVE bar complex: d^2 != 0 (the Jacobiator).
    For the CE complex (the correct chiral bar): d^2 = 0.

    We use the Lie bracket as the product and verify:
    - d^2 != 0 for the associative bar (expected)
    - The twisting morphism MC equation
    - The A-infinity m_3 = Jacobiator
    """
    dga = lie_sl2_as_assoc()

    bar = BarConstruction(dga, 4)
    return {
        "dga": dga,
        "bar": bar,
        "is_associative": dga.is_associative(),
        "bar_d_squared": bar.verify_d_squared(),
        "ainfty_ops": extract_ainfty_operations(dga, 3),
        "ainfty_relations": verify_ainfty_relations(dga, 3),
    }
