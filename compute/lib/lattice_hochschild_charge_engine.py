r"""Finite-window arithmetic for lattice Hochschild charge gradings.

For a positive-definite even lattice with Gram matrix ``G``, the
conformal energy of a charge ``alpha`` is

    E(alpha) = <alpha, alpha>/2.

This module computes the finite charge set in an energy window, the
degree-dependent Hochschild shift set ``Gamma_{n,N}``, and the exact
filtration reindexing produced by translation through ``N*beta``.
It also compares an ordered collision coefficient with its
reversed-order ratio.  Chain-level group-cohomology and periodicity
comparisons remain separate constructions in the manuscript.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import ceil, sqrt
from typing import Dict, Iterable, Sequence, Tuple


Vector = Tuple[int, ...]
Matrix = Tuple[Tuple[int, ...], ...]


def _fraction_inverse(matrix: Matrix) -> Tuple[Tuple[Fraction, ...], ...]:
    size = len(matrix)
    augmented = [
        [Fraction(entry) for entry in row]
        + [Fraction(int(i == j)) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise ValueError("the Gram matrix must be invertible")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            coefficient = augmented[row][column]
            augmented[row] = [
                left - coefficient * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return tuple(tuple(row[size:]) for row in augmented)


def validate_even_gram(gram: Sequence[Sequence[int]]) -> Matrix:
    """Return a square symmetric even positive-definite Gram matrix."""

    matrix = tuple(tuple(int(entry) for entry in row) for row in gram)
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("the Gram matrix must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(size) for j in range(size)):
        raise ValueError("the Gram matrix must be symmetric")
    if any(matrix[i][i] % 2 for i in range(size)):
        raise ValueError("an even lattice has even diagonal entries")

    # Sylvester's criterion, evaluated exactly through fraction elimination.
    for leading_size in range(1, size + 1):
        leading = tuple(row[:leading_size] for row in matrix[:leading_size])
        inverse = _fraction_inverse(leading)
        # A symmetric matrix with all preceding positive leading minors has
        # positive next pivot precisely when the final inverse diagonal does.
        if inverse[-1][-1] <= 0:
            raise ValueError("the Gram matrix must be positive definite")
    return matrix


def pairing(gram: Matrix, left: Vector, right: Vector) -> int:
    """Evaluate the integral lattice pairing."""

    if len(left) != len(gram) or len(right) != len(gram):
        raise ValueError("charge rank must match the Gram matrix")
    return sum(
        left[i] * gram[i][j] * right[j]
        for i in range(len(gram))
        for j in range(len(gram))
    )


def conformal_energy(gram: Matrix, charge: Vector) -> Fraction:
    """Return ``<charge,charge>/2`` exactly."""

    return Fraction(pairing(gram, charge, charge), 2)


def charges_in_window(gram: Matrix, cutoff: int) -> Tuple[Vector, ...]:
    """Enumerate every lattice charge of conformal energy at most ``cutoff``."""

    if cutoff < 0:
        raise ValueError("the cutoff must be nonnegative")
    inverse = _fraction_inverse(gram)
    bounds = tuple(
        ceil(sqrt(float(2 * cutoff * inverse[i][i])))
        for i in range(len(gram))
    )
    charges = (
        tuple(int(coordinate) for coordinate in candidate)
        for candidate in product(*(range(-bound, bound + 1) for bound in bounds))
    )
    return tuple(
        charge for charge in charges if conformal_energy(gram, charge) <= cutoff
    )


def gamma_shift_set(gram: Matrix, cochain_degree: int, cutoff: int) -> Tuple[Vector, ...]:
    r"""Compute ``Gamma_{n,N}={beta-sum_i alpha_i}`` in a finite window."""

    if cochain_degree < 0:
        raise ValueError("the cochain degree must be nonnegative")
    charges = charges_in_window(gram, cutoff)
    rank = len(gram)
    shifts = set()
    for inputs_and_output in product(charges, repeat=cochain_degree + 1):
        *inputs, output = inputs_and_output
        shifts.add(
            tuple(
                output[j] - sum(input_charge[j] for input_charge in inputs)
                for j in range(rank)
            )
        )
    return tuple(sorted(shifts))


def filtration_reindexing(
    gram: Matrix,
    charge: Vector,
    period: int,
    beta: Vector,
) -> Fraction:
    r"""Return ``E(charge+period*beta)-E(charge)`` by the bilinear formula."""

    return Fraction(period * pairing(gram, charge, beta)) + Fraction(
        period * period * pairing(gram, beta, beta), 2
    )


def translate_charge(charge: Vector, period: int, beta: Vector) -> Vector:
    """Translate a charge by ``period*beta``."""

    if len(charge) != len(beta):
        raise ValueError("charge and period vector must have the same rank")
    return tuple(left + period * right for left, right in zip(charge, beta))


def translation_table(
    gram: Matrix,
    charges: Iterable[Vector],
    period: int,
    beta: Vector,
) -> Dict[Vector, Tuple[Vector, Fraction]]:
    """Construct the charge translation and its exact filtration shift."""

    table: Dict[Vector, Tuple[Vector, Fraction]] = {}
    for charge in charges:
        translated = translate_charge(charge, period, beta)
        shift = filtration_reindexing(gram, charge, period, beta)
        if conformal_energy(gram, translated) - conformal_energy(gram, charge) != shift:
            raise ArithmeticError("bilinear and direct energy shifts must agree")
        table[charge] = (translated, shift)
    return table


def reversed_order_ratio(epsilon_ab: complex, epsilon_ba: complex) -> complex:
    """Return the ratio of an ordered collision coefficient to its reversal."""

    if epsilon_ba == 0:
        raise ZeroDivisionError("the reversed collision coefficient must be invertible")
    return epsilon_ab / epsilon_ba

