"""Exact checks for the formal shadow-Dirichlet surface.

The analytic continuation, genus comparison, motivic realization, and
Kummer transport in the manuscript are conditional packages.  This test
module verifies only the classical algebra and number theory used inside
those implications.
"""

from __future__ import annotations

import sympy as sp
from sympy import Rational, bernoulli, zeta

from compute.lib.independent_verification import independent_verification


@independent_verification(
    claim="classical-dirichlet-absolute-convergence-bound",
    derived_from=[
        "comparison |a_r r^{-s}| <= C r^{N-Re(s)}",
    ],
    verified_against=[
        "p-series convergence criterion",
    ],
    disjoint_rationale=(
        "The coefficient estimate supplies the majorant; the p-series "
        "criterion decides convergence of that independent majorant."
    ),
)
def test_polynomial_growth_gives_the_stated_half_plane():
    """The majorant exponent is below -1 exactly when Re(s)>N+1."""
    for n in range(0, 8):
        sigma = Rational(2 * n + 3, 2)
        assert (n - sigma < -1) == (sigma > n + 1)


@independent_verification(
    claim="classical-zeta-negative-integer-component",
    derived_from=[
        "Euler's formula zeta(-n)=-B_{n+1}/(n+1)",
    ],
    verified_against=[
        "SymPy exact analytic continuation of zeta at negative integers",
    ],
    disjoint_rationale=(
        "Euler's Bernoulli formula and SymPy's symbolic zeta evaluation are "
        "independent implementations of the same classical special value."
    ),
)
def test_unshifted_component_starting_at_r_two():
    """The r>=2 regularized component is zeta(-n)-1."""
    expected = {
        1: Rational(-13, 12),
        2: Rational(-1),
        3: Rational(-119, 120),
        5: Rational(-253, 252),
    }
    for n, value in expected.items():
        euler = -bernoulli(n + 1) / (n + 1) - 1
        direct = zeta(-n) - 1
        assert sp.simplify(euler - value) == 0
        assert sp.simplify(direct - value) == 0


@independent_verification(
    claim="bernoulli-kummer-witnesses-b12-b16",
    derived_from=[
        "Euler--Bernoulli generating function",
    ],
    verified_against=[
        "exact factorization of the reduced numerators 691 and 3617",
    ],
    disjoint_rationale=(
        "The generating function determines the rational Bernoulli values; "
        "integer factorization independently identifies their prime numerators."
    ),
)
def test_exact_bernoulli_witnesses():
    b12 = bernoulli(12)
    b16 = bernoulli(16)
    assert b12 == Rational(-691, 2730)
    assert b16 == Rational(-3617, 510)
    assert sp.factorint(abs(int(b12.p))) == {691: 1}
    assert sp.factorint(abs(int(b16.p))) == {3617: 1}


@independent_verification(
    claim="faber-pandharipande-scalar-boundary-values",
    derived_from=[
        "Mumford genus-one integral and Faber--Pandharipande genus-two integral",
    ],
    verified_against=[
        "exact rational arithmetic after multiplication by sample scalar kappa",
    ],
    disjoint_rationale=(
        "The geometric literature supplies the two tautological constants; "
        "the verification uses only exact rational multiplication."
    ),
)
def test_faber_pandharipande_scalar_values_as_independent_inputs():
    lambda_1_fp = Rational(1, 24)
    lambda_2_fp = Rational(7, 5760)
    kappa = Rational(13, 2)
    assert kappa * lambda_1_fp == Rational(13, 48)
    assert kappa * lambda_2_fp == Rational(91, 11520)


def test_finite_dirichlet_encoding_retains_every_coefficient():
    """A finite Dirichlet polynomial is an injective sequence encoding."""
    s = sp.Symbol("s")
    coefficients = {
        2: Rational(1, 4),
        3: Rational(2),
        4: Rational(40, 49),
    }
    terms = {r: a * sp.Pow(r, -s, evaluate=False) for r, a in coefficients.items()}
    assert set(terms) == set(coefficients)
    for r in coefficients:
        basis = sp.Pow(r, -s, evaluate=False)
        assert terms[r].has(basis)
        assert terms[r].coeff(basis) == coefficients[r]
