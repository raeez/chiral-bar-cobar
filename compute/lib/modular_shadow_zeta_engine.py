"""Modular shadow zeta engine for the scalar genus lane.

This module implements the canonical Volume I normalization

    F_g(A) = kappa(A) * lambda_g^FP  (UNIFORM-WEIGHT)

with

    lambda_g^FP = ((2^(2g-1) - 1) / 2^(2g-1)) * |B_{2g}| / (2g)!.

Under this normalization,

    lambda_1^FP = 1/24,
    lambda_2^FP = 7/5760,
    lambda_3^FP = 31/967680.

The frequently confused values 1/1152 and -1/414720 belong to different
Hodge/Witten-Kontsevich normalizations and are not the scalar coefficients
appearing in Theorem D for the uniform-weight lane.

Consequences used below:

    lambda_g^FP = 2 * eta(2g) / (2*pi)^(2g),

where eta is the Dirichlet eta function. Hence lambda_g^FP decays
geometrically like 2 / (2*pi)^(2g), so the Dirichlet series

    Z_A(s) = sum_{g>=1} F_g(A) * g^(-s)

converges absolutely for every complex s. The resulting shadow zeta is
entire in s; there is no surviving factorial-divergence statement in this
normalization.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from math import factorial, pi
from typing import Dict, Iterable, List, Sequence, Tuple, Union

try:
    import numpy as np
except ImportError:  # pragma: no cover - numpy is optional for pole extraction
    np = None


Number = Union[int, float, complex, Fraction]

DEFAULT_MAX_GENUS = 10
SL2_DIM = 3
SL2_H_DUAL = 2


@dataclass(frozen=True)
class GrowthAnalysis:
    """Growth analysis for lambda_g^FP and F_g = kappa * lambda_g^FP."""

    lambda_values: Tuple[Fraction, ...]
    ratio_table: Tuple[float, ...]
    scaled_asymptotic_values: Tuple[float, ...]
    ratio_limit: float
    asymptotic_formula: str
    growth_kind: str
    abscissa_of_convergence: float
    abscissa_of_absolute_convergence: float
    meromorphic_continuation: str
    pole_structure: Tuple[complex, ...]
    exact_representation: str


@dataclass(frozen=True)
class PadeReport:
    """Padé report for one [m/n] approximant."""

    order: Tuple[int, int]
    numerator: Tuple[complex, ...]
    denominator: Tuple[complex, ...]
    poles: Tuple[complex, ...]


@dataclass(frozen=True)
class BorelAnalysis:
    """Borel-transform analysis for F_g = kappa * lambda_g^FP."""

    coefficients: Tuple[Fraction, ...]
    reports: Tuple[PadeReport, ...]
    stable_poles: Tuple[complex, ...]
    entire: bool
    conclusion: str


def bernoulli_number(n: int) -> Fraction:
    """Return the Bernoulli number B_n as an exact Fraction."""

    if n < 0:
        raise ValueError(f"Bernoulli numbers require n >= 0, got {n}")
    if n == 0:
        return Fraction(1)
    a = [Fraction(1, m + 1) for m in range(n + 1)]
    for m in range(n + 1):
        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return a[0]


def _invert_unit_series(coefficients: Sequence[Fraction], degree: int) -> List[Fraction]:
    """Invert a power series with constant term 1 up to the given degree."""

    if degree < 0:
        return []
    if not coefficients or coefficients[0] != 1:
        raise ValueError("Series inversion requires constant term 1")
    inverse = [Fraction(0)] * (degree + 1)
    inverse[0] = Fraction(1)
    for k in range(1, degree + 1):
        inverse[k] = -sum(coefficients[j] * inverse[k - j] for j in range(1, k + 1))
    return inverse


def lambda_fp(genus: int) -> Fraction:
    """Return lambda_g^FP in the canonical Theorem D normalization."""

    if genus < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {genus}")
    b_2g = abs(bernoulli_number(2 * genus))
    numerator = (2 ** (2 * genus - 1) - 1) * b_2g
    denominator = Fraction(2 ** (2 * genus - 1) * factorial(2 * genus), 1)
    return numerator / denominator


def lambda_fp_from_sine_series(genus: int) -> Fraction:
    """Independent exact recovery of lambda_g^FP from (x/2)/sin(x/2)."""

    if genus < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {genus}")
    coefficients = [
        Fraction((-1) ** n, 2 ** (2 * n) * factorial(2 * n + 1))
        for n in range(genus + 1)
    ]
    inverse = _invert_unit_series(coefficients, genus)
    return inverse[genus]


def lambda_fp_eta_numeric(genus: int, terms: int = 2000) -> float:
    """Numerical eta-series reconstruction of lambda_g^FP."""

    if genus < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {genus}")
    total = 0.0
    for n in range(1, terms + 1):
        total += ((-1.0) ** (n - 1)) / (n ** (2 * genus))
    return 2.0 * total / ((2.0 * pi) ** (2 * genus))


def lambda_fp_table(max_genus: int = DEFAULT_MAX_GENUS) -> Dict[int, Fraction]:
    """Exact table g -> lambda_g^FP for g = 1, ..., max_genus."""

    return {genus: lambda_fp(genus) for genus in range(1, max_genus + 1)}


def heisenberg_kappa(level: Fraction) -> Fraction:
    """kappa(H_k) = k."""

    return Fraction(level)


def virasoro_kappa(central_charge: Fraction) -> Fraction:
    """kappa(Vir_c) = c / 2."""

    return Fraction(central_charge, 2)


def affine_km_kappa(level: Fraction, dim_g: int, h_dual: int) -> Fraction:
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2 h^v)."""

    return Fraction(dim_g) * (Fraction(level) + Fraction(h_dual)) / Fraction(2 * h_dual)


def affine_sl2_kappa(level: Fraction) -> Fraction:
    """sl_2 specialization: dim = 3, h^v = 2."""

    return affine_km_kappa(level=level, dim_g=SL2_DIM, h_dual=SL2_H_DUAL)


def free_energy(genus: int, kappa: Fraction) -> Fraction:
    """Return F_g = kappa * lambda_g^FP (UNIFORM-WEIGHT)."""

    return Fraction(kappa) * lambda_fp(genus)


def free_energy_table(kappa: Fraction, max_genus: int = DEFAULT_MAX_GENUS) -> Dict[int, Fraction]:
    """Exact table g -> F_g = kappa * lambda_g^FP (UNIFORM-WEIGHT)."""

    return {genus: free_energy(genus, kappa) for genus in range(1, max_genus + 1)}


def family_zeta_formulas() -> Dict[str, str]:
    """Closed-form prefactor descriptions for standard families."""

    basis = "sum_{g>=1} lambda_g^FP * g^{-s}"
    return {
        "Heis_k": f"Z_H_k(s) = k * {basis}",
        "Vir_c": f"Z_Vir_c(s) = (c/2) * {basis}",
        "KM": f"Z_V_k(g)(s) = dim(g)*(k+h^v)/(2*h^v) * {basis}",
    }


def _dirichlet_weight(genus: int, s: Number) -> Union[Fraction, complex]:
    """Return g^(-s), exact for integer s and numeric otherwise."""

    if isinstance(s, Fraction) and s.denominator == 1:
        s = s.numerator
    if isinstance(s, int):
        if s >= 0:
            return Fraction(1, genus ** s)
        return Fraction(genus ** (-s), 1)
    return cmath.exp(-complex(s) * math.log(genus))


def partial_shadow_zeta(kappa: Fraction, s: Number, max_genus: int = DEFAULT_MAX_GENUS) -> Union[Fraction, complex]:
    """Partial Dirichlet sum Z_A^{<=G}(s) = sum_{g=1}^G F_g * g^(-s)."""

    weights = [_dirichlet_weight(genus, s) for genus in range(1, max_genus + 1)]
    if all(isinstance(weight, Fraction) for weight in weights):
        total = Fraction(0)
        for genus, weight in enumerate(weights, start=1):
            total += free_energy(genus, kappa) * weight
        return total
    total_complex = 0j
    for genus, weight in enumerate(weights, start=1):
        total_complex += complex(free_energy(genus, kappa)) * complex(weight)
    return total_complex


def standard_family_partial_sums(
    s: Number,
    max_genus: int = DEFAULT_MAX_GENUS,
    heisenberg_level: Fraction = Fraction(1),
    virasoro_c: Fraction = Fraction(25),
    affine_level: Fraction = Fraction(1),
    affine_dim: int = SL2_DIM,
    affine_h_dual: int = SL2_H_DUAL,
) -> Dict[str, Union[Fraction, complex]]:
    """Partial modular-shadow zeta sums for representative standard families."""

    return {
        "Heis_k": partial_shadow_zeta(heisenberg_kappa(heisenberg_level), s, max_genus=max_genus),
        "Vir_c": partial_shadow_zeta(virasoro_kappa(virasoro_c), s, max_genus=max_genus),
        "KM": partial_shadow_zeta(
            affine_km_kappa(level=affine_level, dim_g=affine_dim, h_dual=affine_h_dual),
            s,
            max_genus=max_genus,
        ),
    }


def analyze_growth(max_genus: int = DEFAULT_MAX_GENUS) -> GrowthAnalysis:
    """Analyze the canonical growth of lambda_g^FP and F_g."""

    lambda_values = tuple(lambda_fp(genus) for genus in range(1, max_genus + 1))
    ratio_table = tuple(
        float(lambda_values[idx + 1] / lambda_values[idx])
        for idx in range(len(lambda_values) - 1)
    )
    scaled = tuple(
        float(lambda_values[idx] * Fraction.from_float((2.0 * pi) ** (2 * (idx + 1))) / 2)
        for idx in range(len(lambda_values))
    )
    return GrowthAnalysis(
        lambda_values=lambda_values,
        ratio_table=ratio_table,
        scaled_asymptotic_values=scaled,
        ratio_limit=1.0 / ((2.0 * pi) ** 2),
        asymptotic_formula="lambda_g^FP ~ 2 / (2*pi)^(2g)",
        growth_kind="geometric_decay",
        abscissa_of_convergence=float("-inf"),
        abscissa_of_absolute_convergence=float("-inf"),
        meromorphic_continuation="entire",
        pole_structure=tuple(),
        exact_representation=(
            "Z_A(s) = 2*kappa*sum_{n>=1} (-1)^(n-1) * Li_s((2*pi*n)^(-2))"
        ),
    )


def borel_transform_coefficients(kappa: Fraction, max_genus: int = DEFAULT_MAX_GENUS) -> Tuple[Fraction, ...]:
    """Return coefficients of B(t) = sum_g F_g / Gamma(g) * t^(g-1)."""

    return tuple(
        free_energy(genus, kappa) / Fraction(factorial(genus - 1), 1)
        for genus in range(1, max_genus + 1)
    )


def evaluate_borel_transform(kappa: Fraction, t: Number, max_genus: int = DEFAULT_MAX_GENUS) -> complex:
    """Evaluate the truncated Borel transform at t."""

    t_complex = complex(t)
    total = 0j
    for degree, coefficient in enumerate(borel_transform_coefficients(kappa, max_genus=max_genus)):
        total += complex(coefficient) * (t_complex ** degree)
    return total


def _solve_linear_system(matrix: Sequence[Sequence[complex]], rhs: Sequence[complex]) -> List[complex]:
    """Solve a small dense linear system by Gaussian elimination."""

    size = len(rhs)
    augmented = [
        [complex(entry) for entry in row] + [complex(rhs_val)]
        for row, rhs_val in zip(matrix, rhs)
    ]
    for col in range(size):
        pivot = max(range(col, size), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot][col]) < 1e-15:
            raise ValueError("Singular linear system in Padé construction")
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        pivot_value = augmented[col][col]
        for idx in range(col, size + 1):
            augmented[col][idx] /= pivot_value
        for row in range(size):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor == 0:
                continue
            for idx in range(col, size + 1):
                augmented[row][idx] -= factor * augmented[col][idx]
    return [augmented[row][size] for row in range(size)]


def pade_from_series(coefficients: Sequence[Number], m: int, n: int) -> Tuple[Tuple[complex, ...], Tuple[complex, ...]]:
    """Build the [m/n] Padé approximant of a power series."""

    if m < 0 or n < 0:
        raise ValueError("Padé orders must be non-negative")
    if len(coefficients) < m + n + 1:
        raise ValueError("Need at least m+n+1 coefficients for Padé construction")
    coeffs = [complex(value) for value in coefficients]
    if n == 0:
        return tuple(coeffs[: m + 1]), (1.0 + 0j,)
    matrix = []
    rhs = []
    for row in range(n):
        k = m + 1 + row
        matrix.append([coeffs[k - j] for j in range(1, n + 1)])
        rhs.append(-coeffs[k])
    q_tail = _solve_linear_system(matrix, rhs)
    denominator = [1.0 + 0j] + q_tail
    numerator = []
    for k in range(m + 1):
        numerator.append(
            sum(denominator[j] * coeffs[k - j] for j in range(min(k, n) + 1))
        )
    return tuple(numerator), tuple(denominator)


def pade_evaluate(numerator: Sequence[complex], denominator: Sequence[complex], z: Number) -> complex:
    """Evaluate a Padé approximant with low-to-high coefficient order."""

    z_complex = complex(z)
    numerator_value = 0j
    denominator_value = 0j
    for coefficient in reversed(numerator):
        numerator_value = numerator_value * z_complex + coefficient
    for coefficient in reversed(denominator):
        denominator_value = denominator_value * z_complex + coefficient
    if abs(denominator_value) < 1e-15:
        raise ZeroDivisionError("Padé denominator vanishes at evaluation point")
    return numerator_value / denominator_value


def pade_poles(denominator: Sequence[complex]) -> Tuple[complex, ...]:
    """Roots of the Padé denominator, when numpy is available."""

    if len(denominator) <= 1 or np is None:
        return tuple()
    roots = np.roots(list(reversed(denominator)))
    return tuple(complex(root) for root in roots if math.isfinite(root.real) and math.isfinite(root.imag))


def _cluster_stable_poles(reports: Sequence[PadeReport], tolerance: float = 0.35) -> Tuple[complex, ...]:
    """Keep only poles that recur across all Padé orders within a tolerance."""

    if not reports:
        return tuple()
    required_count = len(reports)
    clusters: List[Dict[str, object]] = []
    for report_index, report in enumerate(reports):
        for pole in report.poles:
            if abs(pole) > 50.0:
                continue
            placed = False
            for cluster in clusters:
                center = cluster["center"]
                if abs(pole - center) <= tolerance:
                    report_ids = cluster["report_ids"]
                    poles = cluster["poles"]
                    report_ids.add(report_index)
                    poles.append(pole)
                    cluster["center"] = sum(poles, 0j) / len(poles)
                    placed = True
                    break
            if not placed:
                clusters.append(
                    {
                        "center": pole,
                        "report_ids": {report_index},
                        "poles": [pole],
                    }
                )
    stable = []
    for cluster in clusters:
        report_ids = cluster["report_ids"]
        if len(report_ids) == required_count:
            stable.append(cluster["center"])
    stable.sort(key=lambda pole: (round(pole.real, 12), round(pole.imag, 12)))
    return tuple(stable)


def borel_transform_analysis(
    kappa: Fraction,
    max_genus: int = DEFAULT_MAX_GENUS,
    orders: Sequence[Tuple[int, int]] | None = None,
) -> BorelAnalysis:
    """Analyze the truncated Borel transform and its Padé approximants."""

    coefficients = borel_transform_coefficients(kappa, max_genus=max_genus)
    if orders is None:
        orders = ((4, 4), (4, 5), (5, 4))
    reports = []
    for order in orders:
        m, n = order
        if m + n + 1 > len(coefficients):
            continue
        numerator, denominator = pade_from_series(coefficients, m, n)
        reports.append(
            PadeReport(
                order=order,
                numerator=numerator,
                denominator=denominator,
                poles=pade_poles(denominator),
            )
        )
    stable_poles = _cluster_stable_poles(reports)
    return BorelAnalysis(
        coefficients=coefficients,
        reports=tuple(reports),
        stable_poles=stable_poles,
        entire=True,
        conclusion=(
            "The canonical lambda_g^FP coefficients decay geometrically, and the "
            "extra Gamma(g)^(-1) in the Borel transform forces an entire series. "
            "Any Padé poles here are numerical artifacts unless they stabilize."
        ),
    )


__all__ = [
    "DEFAULT_MAX_GENUS",
    "GrowthAnalysis",
    "PadeReport",
    "BorelAnalysis",
    "bernoulli_number",
    "lambda_fp",
    "lambda_fp_from_sine_series",
    "lambda_fp_eta_numeric",
    "lambda_fp_table",
    "heisenberg_kappa",
    "virasoro_kappa",
    "affine_km_kappa",
    "affine_sl2_kappa",
    "free_energy",
    "free_energy_table",
    "family_zeta_formulas",
    "partial_shadow_zeta",
    "standard_family_partial_sums",
    "analyze_growth",
    "borel_transform_coefficients",
    "evaluate_borel_transform",
    "pade_from_series",
    "pade_evaluate",
    "pade_poles",
    "borel_transform_analysis",
]
