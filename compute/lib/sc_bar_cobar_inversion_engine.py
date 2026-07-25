r"""Finite bar calculations and Swiss-cheese scope certificates.

The executable calculation is the ordinary reduced bar complex of

    A_m = Q[x]/(x^m),   epsilon(x)=0.

It is finite in each internal weight.  With ``[a_1|...|a_n]`` denoting the
word ``[x^a_1|...|x^a_n]``, the chosen homological convention is

    d[a_1|...|a_n]
      = sum_i (-1)^i [a_1|...|a_i+a_{i+1}|...|a_n],

where a summand is zero when ``a_i+a_{i+1} >= m``.  Matrices, ranks, and
homology dimensions are therefore exact over ``Q``.

Two worked cases expose the theorem boundary.

* ``A_2`` is quadratic.  Its augmentation ideal has square zero, so the full
  bar differential vanishes and the quadratic coalgebra ``A_2^i`` equals the
  full bar coalgebra.
* ``A_3`` has its first defining relation in degree three.  Its quadratic
  relation space is zero.  The first class missed by ``A_3^i -> Bar(A_3)``
  occurs in internal weight three and bar degree two.

The universal counit ``Omega Bar(A) -> A`` is a different map.  In the
pro-nilpotent Ran ambient it is the Francis--Gaitsgory reconstruction theorem
for every augmented associative algebra.  Quadratic Koszulness governs the
comparison ``q_A: A^i -> Bar(A)``.

The Swiss-cheese ledger uses the standard open/closed typing: ``A`` is the
open algebra and ``RHom_{A^e}(A,A)`` is the closed derived-centre actor.  The
bar construction is a resolution used to compute that centre; it is not a
second colour by itself.

The affine-current calculation at the end verifies only the Lie Jacobi
identity and invariance of the level pairing.  Those checks certify the
current OPE input.  They do not manufacture a chiral bar complex or a
family-wide Koszul theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from typing import Dict, Iterable, Mapping, Optional, Tuple

from sympy import Matrix, Rational, Symbol, zeros

try:
    from compute.lib.theorem_heuts_fg_scope_engine import (
        universal_resolution_certificate,
    )
except ModuleNotFoundError:  # direct execution from compute/lib
    from theorem_heuts_fg_scope_engine import universal_resolution_certificate


Word = Tuple[int, ...]
Vector = Tuple[object, object, object]


@dataclass(frozen=True)
class TruncatedPolynomialAlgebra:
    r"""The augmented algebra ``Q[x]/(x^m)`` with ``m >= 2``."""

    m: int

    def __post_init__(self) -> None:
        if self.m < 2:
            raise ValueError("the truncation exponent m is at least two")

    @property
    def name(self) -> str:
        return f"Q[x]/(x^{self.m})"

    @property
    def augmentation_basis(self) -> Tuple[int, ...]:
        """Exponents labelling ``x, ..., x^(m-1)``."""

        return tuple(range(1, self.m))

    @property
    def relation_degree(self) -> int:
        return self.m

    @property
    def quadratic(self) -> bool:
        return self.m == 2

    def multiply_exponents(self, left: int, right: int) -> Optional[int]:
        """Return the exponent of the product, or ``None`` for the zero product."""

        if left not in self.augmentation_basis or right not in self.augmentation_basis:
            raise ValueError("bar letters belong to the augmentation basis")
        exponent = left + right
        return exponent if exponent < self.m else None


DUAL_NUMBERS = TruncatedPolynomialAlgebra(2)
TRUNCATED_CUBIC = TruncatedPolynomialAlgebra(3)


@lru_cache(maxsize=None)
def _bar_basis_cached(m: int, weight: int, length: int) -> Tuple[Word, ...]:
    if weight < 0 or length < 0:
        return ()
    if length == 0:
        return ((),) if weight == 0 else ()
    if weight == 0:
        return ()

    words = []

    def extend(prefix: Word, remaining_weight: int, remaining_length: int) -> None:
        if remaining_length == 0:
            if remaining_weight == 0:
                words.append(prefix)
            return
        for exponent in range(1, m):
            if exponent <= remaining_weight:
                extend(
                    prefix + (exponent,),
                    remaining_weight - exponent,
                    remaining_length - 1,
                )

    extend((), weight, length)
    return tuple(words)


def bar_basis(
    algebra: TruncatedPolynomialAlgebra, weight: int, length: int
) -> Tuple[Word, ...]:
    r"""Basis of ``Bar_length(A_m)`` in internal weight ``weight``."""

    return _bar_basis_cached(algebra.m, weight, length)


def bar_differential_terms(
    algebra: TruncatedPolynomialAlgebra, word: Word
) -> Dict[Word, int]:
    """Apply the reduced bar differential to one basis word."""

    if any(exponent not in algebra.augmentation_basis for exponent in word):
        raise ValueError("every word entry labels an augmentation-basis monomial")

    terms: Dict[Word, int] = {}
    for index in range(len(word) - 1):
        product_exponent = algebra.multiply_exponents(word[index], word[index + 1])
        if product_exponent is None:
            continue
        target = word[:index] + (product_exponent,) + word[index + 2 :]
        coefficient = 1 if index % 2 == 0 else -1
        terms[target] = terms.get(target, 0) + coefficient
        if terms[target] == 0:
            del terms[target]
    return terms


@dataclass(frozen=True)
class BarDifferential:
    """One finite weight block of the reduced bar differential."""

    weight: int
    source_length: int
    source_basis: Tuple[Word, ...]
    target_basis: Tuple[Word, ...]
    matrix: Matrix

    @property
    def rank(self) -> int:
        return int(self.matrix.rank())


def bar_differential(
    algebra: TruncatedPolynomialAlgebra, weight: int, source_length: int
) -> BarDifferential:
    """Build the exact matrix ``B_n(weight) -> B_(n-1)(weight)``."""

    if source_length < 1:
        raise ValueError("the source bar length is positive")
    source = bar_basis(algebra, weight, source_length)
    target = bar_basis(algebra, weight, source_length - 1)
    row = {word: index for index, word in enumerate(target)}
    matrix = zeros(len(target), len(source))
    for column, word in enumerate(source):
        for image, coefficient in bar_differential_terms(algebra, word).items():
            matrix[row[image], column] += coefficient
    return BarDifferential(
        weight=weight,
        source_length=source_length,
        source_basis=source,
        target_basis=target,
        matrix=matrix,
    )


def bar_d_squared_matrix(
    algebra: TruncatedPolynomialAlgebra, weight: int, source_length: int
) -> Matrix:
    """Return ``d_(n-1) d_n`` in one weight block."""

    if source_length < 2:
        return zeros(0, len(bar_basis(algebra, weight, source_length)))
    upper = bar_differential(algebra, weight, source_length)
    lower = bar_differential(algebra, weight, source_length - 1)
    return lower.matrix * upper.matrix


def verify_bar_d_squared(
    algebra: TruncatedPolynomialAlgebra,
    *,
    max_weight: int,
    max_length: int,
) -> bool:
    """Check every finite block in the requested rectangle."""

    for weight in range(max_weight + 1):
        for length in range(2, max_length + 1):
            square = bar_d_squared_matrix(algebra, weight, length)
            if square != zeros(*square.shape):
                return False
    return True


def bar_homology_dimension(
    algebra: TruncatedPolynomialAlgebra, weight: int, length: int
) -> int:
    r"""Compute ``dim H_length(Bar(A_m))_weight`` exactly."""

    if length < 1 or weight < 1:
        return 0
    chain_dimension = len(bar_basis(algebra, weight, length))
    outgoing_rank = bar_differential(algebra, weight, length).rank
    incoming_rank = bar_differential(algebra, weight, length + 1).rank
    answer = chain_dimension - outgoing_rank - incoming_rank
    if answer < 0:
        raise AssertionError("bar homology dimension became negative")
    return answer


def bar_homology_table(
    algebra: TruncatedPolynomialAlgebra,
    *,
    max_weight: int,
    max_length: int,
) -> Dict[Tuple[int, int], int]:
    """Return the positive homology bidegrees in a finite window."""

    table = {}
    for weight in range(1, max_weight + 1):
        for length in range(1, max_length + 1):
            dimension = bar_homology_dimension(algebra, weight, length)
            if dimension:
                table[(weight, length)] = dimension
    return table


def quadratic_coalgebra_homology_dimension(
    algebra: TruncatedPolynomialAlgebra, weight: int, length: int
) -> int:
    r"""Homology dimension of ``A_m^i`` in the one-generator presentation.

    For ``m=2``, the quadratic relation space is all of ``V tensor V`` and
    the quadratic coalgebra contains the word of every length.  For ``m>2``,
    the quadratic relation space is zero and only the cogenerator survives.
    """

    if algebra.m == 2:
        return int(weight == length and length >= 1)
    return int(weight == 1 and length == 1)


@dataclass(frozen=True)
class QuadraticDefect:
    """A bidegree where ``q_A`` misses bar homology."""

    weight: int
    bar_length: int
    source_homology_dimension: int
    target_homology_dimension: int

    @property
    def cone_homology_dimension(self) -> int:
        return self.target_homology_dimension - self.source_homology_dimension


def quadratic_comparison_defects(
    algebra: TruncatedPolynomialAlgebra,
    *,
    max_weight: int,
    max_length: int,
) -> Tuple[QuadraticDefect, ...]:
    """Locate homology-dimension defects of ``q_A`` in a finite window."""

    defects = []
    for weight in range(1, max_weight + 1):
        for length in range(1, max_length + 1):
            source_dimension = quadratic_coalgebra_homology_dimension(
                algebra, weight, length
            )
            target_dimension = bar_homology_dimension(algebra, weight, length)
            if source_dimension != target_dimension:
                defects.append(
                    QuadraticDefect(
                        weight=weight,
                        bar_length=length,
                        source_homology_dimension=source_dimension,
                        target_homology_dimension=target_dimension,
                    )
                )
    return tuple(defects)


def first_quadratic_obstruction(
    algebra: TruncatedPolynomialAlgebra,
    *,
    max_weight: int = 12,
    max_length: int = 12,
) -> Optional[QuadraticDefect]:
    """Return the lexicographically first computed defect of ``q_A``."""

    defects = quadratic_comparison_defects(
        algebra, max_weight=max_weight, max_length=max_length
    )
    return min(defects, key=lambda defect: (defect.weight, defect.bar_length)) if defects else None


@dataclass(frozen=True)
class SectorLedger:
    """Typed outputs of reconstruction, quadratic compression, and SC centre."""

    open_chart: str
    full_bar_object: str
    universal_reconstruction: str
    quadratic_comparison: str
    closed_actor: str
    open_closed_action: str
    verdier_object: str
    status: Mapping[str, str]


def sector_ledger() -> SectorLedger:
    """Return the map-level Swiss-cheese firewall."""

    return SectorLedger(
        open_chart="A",
        full_bar_object="Bar_X(A)",
        universal_reconstruction="epsilon_A: Omega_X Bar_X(A) -> A",
        quadratic_comparison="q_A: A^i -> Bar_X(A)",
        closed_actor="Z_ch^der(A)=RHom_{A^e}(A,A)",
        open_closed_action="Z_ch^der(A) acts on the open chart A",
        verdier_object="D_Ran Bar_X(A)",
        status={
            "universal_reconstruction": "proved-by-FG in pro-nilpotent Ran",
            "quadratic_comparison": "Koszul criterion; Cone(q_A) is the obstruction",
            "closed_actor": "definition; identification with a physical bulk is conditional",
            "open_closed_action": "algebraic Hochschild action; SC enhancement carries H_OC",
            "verdier_object": "comparison with A^! carries H_VD",
        },
    )


def worked_case_report(
    algebra: TruncatedPolynomialAlgebra,
    *,
    max_weight: int = 8,
    max_length: int = 8,
) -> Dict[str, object]:
    """Combine the point calculation with the Ran theorem certificates."""

    obstruction = first_quadratic_obstruction(
        algebra, max_weight=max_weight, max_length=max_length
    )
    if algebra.m == 2:
        q_status = "proved-all-weights: A^i equals Bar(A)"
    elif obstruction is not None:
        q_status = "computed-obstruction"
    else:
        q_status = "window-clear; global criterion open"

    return {
        "algebra": algebra.name,
        "point_bar_homology": bar_homology_table(
            algebra, max_weight=max_weight, max_length=max_length
        ),
        "theorem_a": universal_resolution_certificate(),
        "theorem_b_map": "q_A: A^i -> Bar(A)",
        "theorem_b_status": q_status,
        "first_cone_obstruction": obstruction,
        "point_to_ran_scope": (
            "the finite calculation is a worked point model; Ran reconstruction "
            "uses the Francis--Gaitsgory ambient theorem"
        ),
    }


_BASIS = ("e", "f", "h")
_ZERO: Vector = (0, 0, 0)


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def _scale(scalar: object, vector: Vector) -> Vector:
    return tuple(scalar * vector[i] for i in range(3))  # type: ignore[return-value]


def _basis_vector(name: str) -> Vector:
    return tuple(int(name == basis_name) for basis_name in _BASIS)  # type: ignore[return-value]


def sl2_bracket(left: str, right: str) -> Vector:
    """The ``sl_2`` bracket in the ordered basis ``(e,f,h)``."""

    table: Dict[Tuple[str, str], Vector] = {
        ("e", "f"): _basis_vector("h"),
        ("f", "e"): _scale(-1, _basis_vector("h")),
        ("h", "e"): _scale(2, _basis_vector("e")),
        ("e", "h"): _scale(-2, _basis_vector("e")),
        ("h", "f"): _scale(-2, _basis_vector("f")),
        ("f", "h"): _scale(2, _basis_vector("f")),
    }
    return table.get((left, right), _ZERO)


def bracket_vector(left: str, right: Vector) -> Vector:
    """Extend the bracket linearly in the second variable."""

    answer = _ZERO
    for coefficient, basis_name in zip(right, _BASIS):
        answer = _add(answer, _scale(coefficient, sl2_bracket(left, basis_name)))
    return answer


def level_pairing(left: str, right: str, level: object) -> object:
    """Invariant current-algebra pairing with ``(h,h)=2k`` and ``(e,f)=k``."""

    if (left, right) in (("e", "f"), ("f", "e")):
        return level
    if (left, right) == ("h", "h"):
        return 2 * level
    return 0


def pairing_vector(left: Vector, right: str, level: object) -> object:
    return sum(
        coefficient * level_pairing(basis_name, right, level)
        for coefficient, basis_name in zip(left, _BASIS)
    )


def affine_sl2_current_certificate(level: object = None) -> Dict[str, object]:
    """Verify Jacobi and invariant pairing for the affine ``sl_2`` OPE input."""

    if level is None:
        level = Symbol("k")

    jacobi_failures = []
    invariance_failures = []
    for x, y, z in product(_BASIS, repeat=3):
        jacobi = _add(
            bracket_vector(x, sl2_bracket(y, z)),
            _add(
                bracket_vector(y, sl2_bracket(z, x)),
                bracket_vector(z, sl2_bracket(x, y)),
            ),
        )
        if jacobi != _ZERO:
            jacobi_failures.append((x, y, z, jacobi))

        left_side = pairing_vector(sl2_bracket(x, y), z, level)
        right_side = pairing_vector(sl2_bracket(y, z), x, level)
        if left_side != right_side:
            invariance_failures.append((x, y, z, left_side, right_side))

    return {
        "level": level,
        "jacobi_verified": not jacobi_failures,
        "pairing_invariance_verified": not invariance_failures,
        "jacobi_failures": tuple(jacobi_failures),
        "pairing_invariance_failures": tuple(invariance_failures),
        "ope_coefficients": {
            "e(z)f(w)": {2: level, 1: "h"},
            "h(z)e(w)": {1: "2e"},
            "h(z)f(w)": {1: "-2f"},
            "h(z)h(w)": {2: 2 * level},
        },
        "bar_claim_status": "uncomputed from OPE data alone",
    }


def verify_engine() -> Dict[str, object]:
    """Run exact internal consistency checks."""

    assert verify_bar_d_squared(DUAL_NUMBERS, max_weight=10, max_length=10)
    assert verify_bar_d_squared(TRUNCATED_CUBIC, max_weight=10, max_length=10)

    dual_report = worked_case_report(DUAL_NUMBERS)
    cubic_report = worked_case_report(TRUNCATED_CUBIC)
    cubic_obstruction = cubic_report["first_cone_obstruction"]
    assert isinstance(cubic_obstruction, QuadraticDefect)
    assert (cubic_obstruction.weight, cubic_obstruction.bar_length) == (3, 2)

    current = affine_sl2_current_certificate()
    assert current["jacobi_verified"] is True
    assert current["pairing_invariance_verified"] is True

    return {
        "status": "verified",
        "dual_numbers": dual_report,
        "truncated_cubic": cubic_report,
        "sectors": sector_ledger(),
        "affine_sl2_current": current,
    }


if __name__ == "__main__":
    report = verify_engine()
    obstruction = report["truncated_cubic"]["first_cone_obstruction"]
    print(f"status: {report['status']}")
    print(f"first cubic q_A obstruction: {obstruction}")
