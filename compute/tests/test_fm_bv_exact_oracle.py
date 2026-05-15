"""Exact rational FM/OS oracle tests.

These tests pin the no-broken-circuit normal form used before any BV or
Hochschild argument is allowed to appeal to numeric residue coordinates.
"""

from fractions import Fraction
from math import factorial

from compute.lib.fm_bv_exact_oracle import (
    arnold_triangle,
    double_residue,
    eta,
    is_nbc,
    nbc_basis,
    os_dimension_exact,
    reduce_os_nbc,
    reduce_vector,
    residue,
    second_order_deviation,
    wedge,
)


def _poincare_coefficients(n: int) -> list[int]:
    coeffs = [1]
    for i in range(1, n):
        nxt = [0] * (len(coeffs) + 1)
        for j, coeff in enumerate(coeffs):
            nxt[j] += coeff
            nxt[j + 1] += i * coeff
        coeffs = nxt
    return coeffs


def test_exact_nbc_dimensions_match_poincare_polynomial():
    for n in range(2, 7):
        coeffs = _poincare_coefficients(n)
        assert sum(os_dimension_exact(n, k) for k in range(n)) == factorial(n)
        for degree, expected in enumerate(coeffs):
            assert os_dimension_exact(n, degree) == expected


def test_nbc_basis_contains_only_nbc_monomials():
    for n in range(2, 6):
        for degree in range(n):
            for monomial in nbc_basis(n, degree):
                assert is_nbc(n, monomial)


def test_triangle_arnold_relation_reduces_to_zero():
    assert reduce_vector(3, arnold_triangle(3, 1, 2, 3)) == {}


def test_broken_circuit_reduction_normal_form():
    assert reduce_os_nbc(3, ((1, 3), (2, 3))) == {
        ((1, 2), (2, 3)): Fraction(1),
        ((1, 2), (1, 3)): Fraction(-1),
    }


def test_exact_wedge_uses_nbc_normal_form():
    assert wedge(3, eta(3, 1, 3), eta(3, 2, 3)) == {
        ((1, 2), (2, 3)): Fraction(1),
        ((1, 2), (1, 3)): Fraction(-1),
    }


def test_residue_is_exact_rational_and_relabels_collision():
    image = residue(3, {((1, 2), (2, 3)): Fraction(1)}, 1, 2)
    assert image == {((1, 2),): Fraction(1)}
    assert all(isinstance(coeff, Fraction) for coeff in image.values())


def test_residue_annihilates_reduced_arnold_relation():
    relation = reduce_vector(3, arnold_triangle(3, 1, 2, 3))
    assert residue(3, relation, 1, 2) == {}


def test_double_residue_on_nested_collision_tree():
    top = {((1, 2), (2, 3)): Fraction(1)}
    assert double_residue(3, top, (1, 2), (1, 2)) == {(): Fraction(1)}


def test_residue_free_product_is_associative_in_nbc_form():
    assert second_order_deviation(
        4,
        eta(4, 1, 2),
        eta(4, 2, 3),
        eta(4, 3, 4),
    ) == {}
