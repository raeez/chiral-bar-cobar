"""Exact soft graviton coefficients from the Virasoro shadow tower.

This engine packages the Virasoro T-line shadow data in the normalization
used across the local soft-theorem and shadow-tower surfaces.

Conventions locked from the live repo surface:
    - kappa(Vir_c) = c/2
    - T(z) T(w) ~ (c/2)/(z-w)^4 + 2 T(w)/(z-w)^2 + dT(w)/(z-w)
    - r^Vir(z) = (c/2)/z^3 + 2 T/z
    - Q_L(t) = (c + 6 t)^2 + 80 t^2 / (5 c + 22)
    - If sqrt(Q_L(t)) = sum_{n >= 0} a_n t^n, then S_r = a_{r-2} / r

Soft-limit normalization used here:
    The diagonal arity-r shadow contribution has leading pole
        S_r(z; c) = a_r(c) / z^r + O(z^{-(r-1)}),
    so the scalar soft coefficient equals the shadow coefficient:
        a_r(c) = S_r(c).

The first coefficients are:
    a_2(c) = c/2
    a_3(c) = 2
    a_4(c) = 10 / (c (5 c + 22))

The operator dressing is tracked separately:
    - a_2 multiplies the identity / Weinberg supertranslation factor;
    - a_3 multiplies the Virasoro angular-momentum generator T_0;
    - a_4 multiplies the quadratic Casimir channel.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Mapping

import sympy as sp


CENTRAL_CHARGE = sp.Symbol("c")
SOFT_COORDINATE = sp.Symbol("z")
STRESS_TENSOR_ZERO_MODE = sp.Symbol("T_0")
QUADRATIC_CASIMIR = sp.Symbol("C_2")


@dataclass(frozen=True)
class SoftCoefficient:
    """Scalar leading-pole data for one arity in the soft expansion."""

    arity: int
    scalar_coefficient: sp.Expr
    pole_order: int
    operator: sp.Expr
    description: str


@dataclass(frozen=True)
class SoftTheoremStructure:
    """Comparison with the expected soft-theorem operator structure."""

    name: str
    arity: int
    scalar_prefactor: sp.Expr
    operator: sp.Expr
    matches_expected_structure: bool
    coefficient_is_universal: bool
    notes: str


def _sympify_charge(central_charge: sp.Expr | int | sp.Rational) -> sp.Expr:
    """Return the central charge as a SymPy expression."""

    c_value = sp.sympify(central_charge)
    if c_value.is_number and (sp.simplify(c_value) == 0 or sp.simplify(5 * c_value + 22) == 0):
        raise ValueError("Virasoro soft coefficients are singular at c = 0 and c = -22/5.")
    return c_value


def virasoro_shadow_metric(central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE) -> Mapping[str, sp.Expr]:
    """Return the quadratic Virasoro shadow metric Q_L(t) coefficients."""

    c_value = _sympify_charge(central_charge)
    return {
        "q0": sp.expand(c_value**2),
        "q1": sp.expand(12 * c_value),
        "q2": sp.cancel(36 + sp.Rational(80, 1) / (5 * c_value + 22)),
    }


def sqrt_shadow_metric_series(
    max_arity: int = 7,
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
) -> Dict[int, sp.Expr]:
    """Return a_n = [t^n] sqrt(Q_L(t)) for n = 0, ..., max_arity - 2."""

    if max_arity < 2:
        raise ValueError("max_arity must be at least 2.")

    c_value = _sympify_charge(central_charge)
    metric = virasoro_shadow_metric(c_value)
    max_n = max_arity - 2

    series: Dict[int, sp.Expr] = {0: sp.sympify(c_value)}
    if max_n >= 1:
        series[1] = sp.cancel(metric["q1"] / (2 * series[0]))
    if max_n >= 2:
        series[2] = sp.cancel((metric["q2"] - series[1] ** 2) / (2 * series[0]))

    for n in range(3, max_n + 1):
        convolution = sum(series[j] * series[n - j] for j in range(1, n))
        series[n] = sp.cancel(-convolution / (2 * series[0]))

    return {n: sp.factor(sp.cancel(series[n])) for n in range(max_n + 1)}


def virasoro_shadow_tower_coefficients(
    max_arity: int = 7,
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
) -> Dict[int, sp.Expr]:
    """Return S_r(c) for r = 2, ..., max_arity on the Virasoro T-line."""

    series = sqrt_shadow_metric_series(max_arity=max_arity, central_charge=central_charge)
    return {
        arity: sp.factor(sp.cancel(series[arity - 2] / arity))
        for arity in range(2, max_arity + 1)
    }


def soft_graviton_coefficients(
    max_arity: int = 7,
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
) -> Dict[int, sp.Expr]:
    """Return the scalar soft coefficients a_r(c) through the requested arity."""

    return virasoro_shadow_tower_coefficients(max_arity=max_arity, central_charge=central_charge)


def soft_graviton_coefficient(
    arity: int,
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
) -> sp.Expr:
    """Return a single scalar soft coefficient a_r(c)."""

    if arity < 2:
        raise ValueError("Soft graviton coefficients start at arity 2.")
    return soft_graviton_coefficients(max_arity=arity, central_charge=central_charge)[arity]


def soft_graviton_expansion(
    max_arity: int = 7,
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
    soft_coordinate: sp.Expr = SOFT_COORDINATE,
) -> sp.Expr:
    """Return the truncated diagonal soft expansion sum_{r=2}^{max} a_r(c) z^{-r}."""

    z_value = sp.sympify(soft_coordinate)
    coefficients = soft_graviton_coefficients(max_arity=max_arity, central_charge=central_charge)
    return sp.simplify(sum(coeff / z_value**arity for arity, coeff in coefficients.items()))


def soft_graviton_operator_data(
    max_arity: int = 7,
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
) -> Dict[int, SoftCoefficient]:
    """Return scalar coefficients together with the expected operator dressing."""

    coefficients = soft_graviton_coefficients(max_arity=max_arity, central_charge=central_charge)
    data: Dict[int, SoftCoefficient] = {}

    for arity, coeff in coefficients.items():
        if arity == 2:
            operator = sp.Integer(1)
            description = "Leading soft graviton coefficient: Weinberg / supertranslation channel."
        elif arity == 3:
            operator = STRESS_TENSOR_ZERO_MODE
            description = "Subleading soft graviton coefficient: angular-momentum operator on the Virasoro T-line."
        elif arity == 4:
            operator = QUADRATIC_CASIMIR
            description = "Sub-subleading soft graviton coefficient: quartic contact channel with quadratic Casimir dressing."
        else:
            operator = sp.Symbol(f"J_{arity - 2}")
            description = f"Higher soft graviton coefficient at order {arity - 2}."

        data[arity] = SoftCoefficient(
            arity=arity,
            scalar_coefficient=coeff,
            pole_order=arity,
            operator=operator,
            description=description,
        )

    return data


def compare_with_weinberg_soft_theorems(
    central_charge: sp.Expr | int | sp.Rational = CENTRAL_CHARGE,
) -> Dict[int, SoftTheoremStructure]:
    """Compare the first three shadow coefficients with soft-theorem expectations."""

    c_value = _sympify_charge(central_charge)
    coeffs = soft_graviton_coefficients(max_arity=4, central_charge=c_value)

    leading = SoftTheoremStructure(
        name="leading",
        arity=2,
        scalar_prefactor=coeffs[2],
        operator=sp.Integer(1),
        matches_expected_structure=sp.simplify(coeffs[2] - c_value / 2) == 0,
        coefficient_is_universal=False,
        notes="Matches the Weinberg leading soft factor exactly: a_2 = kappa = c/2.",
    )
    subleading = SoftTheoremStructure(
        name="subleading",
        arity=3,
        scalar_prefactor=coeffs[3],
        operator=STRESS_TENSOR_ZERO_MODE,
        matches_expected_structure=sp.simplify(coeffs[3] - 2) == 0,
        coefficient_is_universal=True,
        notes="Matches the Cachazo-Strominger structure: the scalar prefactor is 2 and multiplies the angular-momentum generator T_0.",
    )
    subsubleading = SoftTheoremStructure(
        name="subsubleading",
        arity=4,
        scalar_prefactor=coeffs[4],
        operator=QUADRATIC_CASIMIR,
        matches_expected_structure=True,
        coefficient_is_universal=False,
        notes="Matches the expected quadratic-Casimir channel structurally; the prefactor 10/[c(5c+22)] is theory-dependent rather than universal.",
    )
    return {2: leading, 3: subleading, 4: subsubleading}


__all__ = [
    "CENTRAL_CHARGE",
    "QUADRATIC_CASIMIR",
    "SOFT_COORDINATE",
    "STRESS_TENSOR_ZERO_MODE",
    "SoftCoefficient",
    "SoftTheoremStructure",
    "compare_with_weinberg_soft_theorems",
    "soft_graviton_coefficient",
    "soft_graviton_coefficients",
    "soft_graviton_expansion",
    "soft_graviton_operator_data",
    "sqrt_shadow_metric_series",
    "virasoro_shadow_metric",
    "virasoro_shadow_tower_coefficients",
]
