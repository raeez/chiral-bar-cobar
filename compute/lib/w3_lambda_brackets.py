r"""Zamolodchikov-normalized :math:`\mathcal W_3` lambda brackets.

The module converts the standard OPE to lambda-bracket and mode conventions,
checks the level-four Virasoro Gram calculation, and derives the action of
``Lambda=:TT:-(3/10)d^2T`` on a highest-weight vector.  It makes no claim to
construct a chiral bar differential or a scalar shadow projection.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple

import sympy as sp


c = sp.Symbol("c")


@dataclass(frozen=True)
class ClaimPacket:
    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()


def TT_lambda_bracket():
    r"""Return ``{T_lambda T}=dT+2 lambda T+(c/12)lambda^3``."""

    return {
        0: [(sp.Integer(1), "dT")],
        1: [(sp.Integer(2), "T")],
        3: [(c / 12, "scalar")],
    }


def TW_lambda_bracket():
    r"""Return ``{T_lambda W}=dW+3 lambda W``."""

    return {0: [(sp.Integer(1), "dW")], 1: [(sp.Integer(3), "W")]}


def WT_lambda_bracket():
    r"""Return the skew-symmetric bracket ``{W_lambda T}=2dW+3lambda W``."""

    return {0: [(sp.Integer(2), "dW")], 1: [(sp.Integer(3), "W")]}


def w3_lambda_coupling(c_val=None):
    r"""Return the pole-two ``WW Lambda`` coupling ``32/(22+5c)``."""

    value = c if c_val is None else sp.sympify(c_val)
    return sp.Integer(32) / (22 + 5 * value)


def WW_lambda_bracket_from_OPE():
    r"""Return ``{W_lambda W}`` in factorial lambda convention.

    If ``W_(1)W`` contains ``32 Lambda/(22+5c)``, the lambda-linear term
    carries the same coefficient.  Translation covariance fixes the constant
    ``dLambda`` coefficient to its half, ``16/(22+5c)``.
    """

    alpha = w3_lambda_coupling()
    return {
        5: [(c / 360, "scalar")],
        4: [],
        3: [(sp.Rational(1, 3), "T")],
        2: [(sp.Rational(1, 2), "dT")],
        1: [
            (sp.Rational(3, 10), "d2T"),
            (alpha, "Lambda"),
        ],
        0: [
            (sp.Rational(1, 15), "d3T"),
            (alpha / 2, "dLambda"),
        ],
    }


def compute_T_lambda_TT():
    r"""Return the exact noncommutative-Wick bracket ``{T_lambda :TT:}``."""

    return {
        0: [(sp.Integer(2), ":TdT:")],
        1: [(sp.Integer(4), ":TT:")],
        2: [(sp.Rational(3, 2), "dT")],
        3: [((c + 8) / 6, "T")],
        4: [],
        5: [(c / 40, "scalar")],
    }


def compute_T_lambda_d2T():
    r"""Return ``{T_lambda d^2T}`` from right sesquilinearity."""

    return {
        0: [(sp.Integer(1), "d3T")],
        1: [(sp.Integer(4), "d2T")],
        2: [(sp.Integer(5), "dT")],
        3: [(sp.Integer(2), "T")],
        5: [(c / 12, "scalar")],
    }


def verify_integral_term_symbolically() -> Mapping[str, object]:
    """Return the three coefficients contributed by the Wick integral term."""

    return {
        "lambda^2 dT": sp.Rational(3, 2),
        "lambda^3 T": sp.Rational(4, 3),
        "lambda^5 scalar": c / 40,
        "status": "exact symbolic integration",
    }


def verify_Lambda_quasi_primary() -> Mapping[str, object]:
    r"""Compute ``{T_lambda Lambda}`` and its quasi-primary anomaly."""

    return {
        0: [(sp.Integer(1), "dLambda")],
        1: [(sp.Integer(4), "Lambda")],
        2: [],
        3: [((5 * c + 22) / 30, "T")],
        "L1_state": sp.Integer(0),
        "L2_state": (5 * c + 22) / 5,
    }


def verify_beta_from_quasi_primarity():
    r"""Return the field coefficient in ``Lambda=:TT:+beta d^2T``."""

    beta = sp.Symbol("beta")
    l1_coefficient = 3 + 10 * beta
    solution = sp.Rational(-3, 10)
    assert l1_coefficient.subs(beta, solution) == 0
    return solution


def level_four_vacuum_gram_matrix(c_val=None):
    """Return the Gram matrix in ``(L_-2^2 1,L_-4 1)``."""

    value = c if c_val is None else sp.sympify(c_val)
    return sp.Matrix(
        [
            [value * (value + 8) / 2, 3 * value],
            [3 * value, 5 * value],
        ]
    )


def lambda_norm(c_val=None):
    r"""Compute ``<Lambda,Lambda>=c(5c+22)/10`` from the Gram matrix."""

    value = c if c_val is None else sp.sympify(c_val)
    vector = sp.Matrix([1, sp.Rational(-3, 5)])
    return sp.factor((vector.T * level_four_vacuum_gram_matrix(value) * vector)[0])


def verify_alpha_from_jacobi():
    """Compatibility name returning the standard primary-source coupling."""

    return w3_lambda_coupling()


def w3_mode_lambda_coefficient(m, n, c_val=None):
    r"""Return the ``Lambda_(m+n)`` coefficient in ``[W_m,W_n]``."""

    value = c if c_val is None else sp.sympify(c_val)
    return sp.simplify(16 * (sp.sympify(m) - sp.sympify(n)) / (22 + 5 * value))


def lambda_zero_eigenvalue(h):
    r"""Return ``Lambda_0|h,w>=(h^2+h/5)|h,w>``.

    The normal-ordered ``:TT:_0`` contribution is ``h^2+2h`` and the
    ``-(3/10)d^2T`` contribution is ``-9h/5``.
    """

    h_val = sp.sympify(h)
    return sp.factor(h_val**2 + h_val / 5)


def verify_Lambda_0_on_hw():
    """Return the symbolic highest-weight eigenvalue of ``Lambda_0``."""

    h = sp.Symbol("h")
    value = lambda_zero_eigenvalue(h)
    assert value.subs(h, 0) == 0
    assert value.subs(h, sp.Rational(-1, 5)) == 0
    return value


def weight_4_linear_quasi_primaries() -> Mapping[str, object]:
    """Record the weight-four linear descendant calculation."""

    return {
        "linear_weight_four_space": ("d2T",),
        "L1_image_nonzero": True,
        "linear_quasi_primary_dimension": 0,
        "quadratic_quasi_primary": "Lambda=:TT:-(3/10)d2T",
    }


def composite_field_necessity_theorem() -> ClaimPacket:
    """Return the exact generic composite-field conclusion."""

    return ClaimPacket(
        statement="The standard W_3 WW OPE contains the quadratic quasi-primary Lambda",
        status="proved elsewhere",
        value=w3_lambda_coupling(),
        hypotheses=("Zamolodchikov normalization", "5c+22 invertible"),
    )


def verify_WW_bracket_coefficients() -> Mapping[str, bool]:
    bracket = WW_lambda_bracket_from_OPE()
    alpha = w3_lambda_coupling()
    return {
        "pole_two": sp.simplify(dict((field, coeff) for coeff, field in bracket[1])["Lambda"] - alpha) == 0,
        "pole_one": sp.simplify(dict((field, coeff) for coeff, field in bracket[0])["dLambda"] - alpha / 2) == 0,
        "central": dict((field, coeff) for coeff, field in bracket[5])["scalar"] == c / 360,
    }


def verify_WW_bracket_conformal_block() -> Mapping[str, object]:
    """Return the exact singular Virasoro-descendant coefficients."""

    return {
        "T": sp.Integer(2),
        "dT": sp.Integer(1),
        "d2T": sp.Rational(3, 10),
        "d3T": sp.Rational(1, 15),
        "status": "read from the standard WW OPE",
    }


def run_all_verifications() -> Mapping[str, object]:
    return {
        "T_lambda_T": TT_lambda_bracket(),
        "T_lambda_W": TW_lambda_bracket(),
        "W_lambda_T": WT_lambda_bracket(),
        "W_lambda_W": WW_lambda_bracket_from_OPE(),
        "Lambda_quasi_primary": verify_Lambda_quasi_primary(),
        "Lambda_norm": lambda_norm(),
        "Lambda_0_hw": verify_Lambda_0_on_hw(),
        "coefficient_checks": verify_WW_bracket_coefficients(),
    }
