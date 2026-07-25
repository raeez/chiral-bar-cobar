"""Exact certificates for ordered-to-symmetric conductor typing.

The engine separates four statements that are frequently conflated:

1. the Reynolds idempotent projects a finite group representation to
   invariants;
2. invariants and coinvariants are canonically isomorphic in
   characteristic zero;
3. an equivariant multilinear operation descends to coinvariants;
4. the Reynolds representative preserves the *untransported* operation
   exactly when its kernel satisfies the corresponding ideal condition.

It also gives the first coalgebra obstruction: the antisymmetric tensor
in arity two lies in the symmetric-coinvariant kernel, while its reduced
deconcatenation survives after applying the arity-one quotient to both
factors.  Thus a symmetric bar coalgebra uses a separately specified
shuffle/factorization coproduct rather than the raw quotient of tensor
deconcatenation.

All calculations use exact SymPy arithmetic.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from math import comb, factorial
from typing import Iterable, Sequence

import sympy as sp


Word = tuple[int, ...]


def tensor_words(dimension: int, arity: int) -> tuple[Word, ...]:
    """Ordered tensor-word basis of ``V**tensor arity``."""
    if dimension < 1 or arity < 0:
        raise ValueError("dimension must be positive and arity nonnegative")
    return tuple(product(range(dimension), repeat=arity))


def symmetric_words(dimension: int, arity: int) -> tuple[Word, ...]:
    """Orbit representatives for position permutations, in lexicographic order."""
    return tuple(word for word in tensor_words(dimension, arity) if tuple(sorted(word)) == word)


def act_on_word(word: Word, permutation: Sequence[int]) -> Word:
    """Permute tensor positions by ``permutation``."""
    if len(word) != len(permutation):
        raise ValueError("word and permutation have different arities")
    return tuple(word[index] for index in permutation)


def permutation_matrix(dimension: int, arity: int, permutation: Sequence[int]) -> sp.Matrix:
    """Exact permutation matrix on the ordered tensor-word basis."""
    words = tensor_words(dimension, arity)
    positions = {word: index for index, word in enumerate(words)}
    matrix = sp.zeros(len(words), len(words))
    for column, word in enumerate(words):
        row = positions[act_on_word(word, permutation)]
        matrix[row, column] = 1
    return matrix


def reynolds_matrix(dimension: int, arity: int) -> sp.Matrix:
    """Reynolds idempotent for position permutations."""
    size = dimension**arity
    result = sp.zeros(size, size)
    group = tuple(permutations(range(arity)))
    for permutation in group:
        result += permutation_matrix(dimension, arity, permutation)
    return result / factorial(arity)


def coinvariant_quotient_matrix(dimension: int, arity: int) -> sp.Matrix:
    """Map every ordered word to its sorted orbit representative."""
    ordered = tensor_words(dimension, arity)
    symmetric = symmetric_words(dimension, arity)
    rows = {word: index for index, word in enumerate(symmetric)}
    quotient = sp.zeros(len(symmetric), len(ordered))
    for column, word in enumerate(ordered):
        quotient[rows[tuple(sorted(word))], column] = 1
    return quotient


@dataclass(frozen=True)
class ReynoldsCoinvariantCertificate:
    dimension: int
    arity: int
    tensor_dimension: int
    invariant_dimension: int
    expected_symmetric_dimension: int
    idempotent: bool
    quotient_after_reynolds_equals_quotient: bool


def reynolds_coinvariant_certificate(dimension: int, arity: int) -> ReynoldsCoinvariantCertificate:
    """Certify the characteristic-zero invariant/coinvariant splitting."""
    reynolds = reynolds_matrix(dimension, arity)
    quotient = coinvariant_quotient_matrix(dimension, arity)
    expected = comb(arity + dimension - 1, dimension - 1)
    return ReynoldsCoinvariantCertificate(
        dimension=dimension,
        arity=arity,
        tensor_dimension=dimension**arity,
        invariant_dimension=reynolds.rank(),
        expected_symmetric_dimension=expected,
        idempotent=reynolds * reynolds == reynolds,
        quotient_after_reynolds_equals_quotient=quotient * reynolds == quotient,
    )


@dataclass(frozen=True)
class DeconcatenationObstruction:
    kernel_vector: sp.Matrix
    quotient_of_kernel_vector: sp.Matrix
    reduced_deconcatenation_after_arity_one_quotients: sp.Matrix
    kernel_is_coideal: bool


def arity_two_deconcatenation_obstruction() -> DeconcatenationObstruction:
    """Return the exact ``e0|e1 - e1|e0`` coideal obstruction."""
    ordered = tensor_words(2, 2)
    positions = {word: index for index, word in enumerate(ordered)}
    antisymmetric = sp.zeros(4, 1)
    antisymmetric[positions[(0, 1)], 0] = 1
    antisymmetric[positions[(1, 0)], 0] = -1

    q2 = coinvariant_quotient_matrix(2, 2)
    # The reduced deconcatenation T^2(V) -> V tensor V is the identity
    # on the ordered arity-two basis.  The arity-one quotient is also
    # the identity, so the obstruction vector survives unchanged.
    reduced = antisymmetric.copy()
    return DeconcatenationObstruction(
        kernel_vector=antisymmetric,
        quotient_of_kernel_vector=q2 * antisymmetric,
        reduced_deconcatenation_after_arity_one_quotients=reduced,
        kernel_is_coideal=(reduced == sp.zeros(4, 1)),
    )


def matrix_commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    """Commutator in ``gl_2``."""
    return left * right - right * left


def z2_conjugation(matrix: sp.Matrix) -> sp.Matrix:
    """The order-two action ``A -> D A D`` for ``D=diag(1,-1)``."""
    diagonal = sp.diag(1, -1)
    return diagonal * matrix * diagonal


def z2_reynolds(matrix: sp.Matrix) -> sp.Matrix:
    """Reynolds projection for the conjugation action."""
    return (matrix + z2_conjugation(matrix)) / 2


@dataclass(frozen=True)
class ReynoldsLieDefectCertificate:
    first_kernel_element: sp.Matrix
    second_kernel_element: sp.Matrix
    bracket: sp.Matrix
    averaged_bracket: sp.Matrix
    bracket_of_averages: sp.Matrix
    defect: sp.Matrix
    reynolds_is_lie_morphism: bool
    kernel_is_lie_ideal: bool


def reynolds_lie_defect_certificate() -> ReynoldsLieDefectCertificate:
    """Exact counterexample to bracket preservation from equivariance alone."""
    e12 = sp.Matrix([[0, 1], [0, 0]])
    e21 = sp.Matrix([[0, 0], [1, 0]])
    bracket = matrix_commutator(e12, e21)
    averaged_bracket = z2_reynolds(bracket)
    bracket_of_averages = matrix_commutator(z2_reynolds(e12), z2_reynolds(e21))
    defect = averaged_bracket - bracket_of_averages

    # e12 is in the Reynolds kernel, while [e12,e21] is invariant.
    kernel_is_ideal = z2_reynolds(matrix_commutator(e12, e21)) == sp.zeros(2)
    return ReynoldsLieDefectCertificate(
        first_kernel_element=e12,
        second_kernel_element=e21,
        bracket=bracket,
        averaged_bracket=averaged_bracket,
        bracket_of_averages=bracket_of_averages,
        defect=defect,
        reynolds_is_lie_morphism=(defect == sp.zeros(2)),
        kernel_is_lie_ideal=kernel_is_ideal,
    )


def concatenation_descends_to_coinvariants(
    dimension: int, left_arity: int, right_arity: int
) -> bool:
    """Exhaustively verify descent of concatenation to symmetric orbits."""
    left_words = tensor_words(dimension, left_arity)
    right_words = tensor_words(dimension, right_arity)
    left_group: Iterable[tuple[int, ...]] = permutations(range(left_arity))
    right_group: tuple[tuple[int, ...], ...] = tuple(permutations(range(right_arity)))

    for left in left_words:
        for right in right_words:
            target_orbit = tuple(sorted(left + right))
            for left_permutation in left_group:
                permuted_left = act_on_word(left, left_permutation)
                for right_permutation in right_group:
                    permuted_right = act_on_word(right, right_permutation)
                    if tuple(sorted(permuted_left + permuted_right)) != target_orbit:
                        return False
            # ``permutations`` returns a one-shot iterator.
            left_group = permutations(range(left_arity))
    return True


def main() -> None:
    """Print the smallest exact certificates."""
    splitting = reynolds_coinvariant_certificate(2, 2)
    coalgebra = arity_two_deconcatenation_obstruction()
    lie = reynolds_lie_defect_certificate()
    print(splitting)
    print(coalgebra)
    print(lie)
    print("concatenation descent:", concatenation_descends_to_coinvariants(2, 2, 2))


if __name__ == "__main__":
    main()
