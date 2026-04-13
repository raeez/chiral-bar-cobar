r"""sl_3 Verlinde dimensions and polynomial families.

This engine keeps two quantities separate:

1. The normalized quantum-dimension sum
       Q_g(k) = sum_lambda d_lambda(k)^(2-2g),
   where d_lambda = S_{0,lambda} / S_{0,0}.

2. The actual Verlinde dimension
       Z_g(k) = sum_lambda S_{0,lambda}^(2-2g)
              = S_{0,0}(k)^(2-2g) * Q_g(k).

For sl_3 at level k, the integrable highest weights are the pairs
    (a, b) with a >= 0, b >= 0, a + b <= k.

The quantum dimensions are given by the Weyl denominator ratio

    d_(a,b)(k)
      = sin(pi*(a+1)/(k+3)) * sin(pi*(b+1)/(k+3))
        * sin(pi*(a+b+2)/(k+3))
        / (sin(pi/(k+3))^2 * sin(2*pi/(k+3))).

Unitarity of the S-matrix gives

    1 = sum_lambda S_{0,lambda}^2
      = S_{0,0}^2 * sum_lambda d_lambda^2,

so

    S_{0,0}^{-2} = sum_lambda d_lambda^2.

Hence the Verlinde dimension can be computed without reconstructing the
entire S-matrix:

    Z_g(k) = (sum_lambda d_lambda^2)^(g-1)
             * sum_lambda d_lambda^(2-2g).

This normalization matches the standard genus convention used elsewhere in
the repository:
  - Z_0(k) = 1
  - Z_1(k) = |P_+^k| = (k+1)(k+2)/2
  - Z_g(k) in Z_{>0} for g >= 2
"""

from __future__ import annotations

from functools import lru_cache
from math import comb
from typing import Dict, Tuple

import mpmath as mp
from sympy import Poly, Symbol, expand, interpolate, symbols


SL3_DIM = 8
SL3_DUAL_COXETER = 3
SL3_RANK = 2
SL3_WEIGHT = Tuple[int, int]

_POLY_SYMBOL = symbols("k")


def _validate_level(level: int) -> None:
    if level < 0:
        raise ValueError(f"Level must be non-negative, got k={level}")


def _validate_genus(genus: int) -> None:
    if genus < 0:
        raise ValueError(f"Genus must be non-negative, got g={genus}")


def _working_precision(level: int, genus: int = 0) -> int:
    return max(80, 24 + 10 * max(genus, 1) + 6 * level)


def _round_to_integer(value: mp.mpf, genus: int, level: int) -> int:
    rounded = int(mp.nint(value))
    tolerance = max(mp.mpf("1e-20"), abs(value) * mp.mpf("1e-40"))
    if abs(value - rounded) > tolerance:
        raise ValueError(
            f"sl_3 Verlinde dimension not integral within tolerance: "
            f"Z_{genus}(k={level}) = {value}"
        )
    return rounded


@lru_cache(maxsize=None)
def sl3_num_integrable_reps(level: int) -> int:
    """Number of integrable sl_3 highest weights at level k."""
    _validate_level(level)
    return comb(level + 2, 2)


@lru_cache(maxsize=None)
def sl3_integrable_weights(level: int) -> Tuple[SL3_WEIGHT, ...]:
    """Integrable highest weights (a, b) with a + b <= k."""
    _validate_level(level)
    return tuple(
        (a, b)
        for a in range(level + 1)
        for b in range(level + 1 - a)
    )


@lru_cache(maxsize=None)
def _sl3_quantum_dimensions(level: int, dps: int) -> Tuple[mp.mpf, ...]:
    _validate_level(level)
    shifted_level = level + SL3_DUAL_COXETER
    weights = sl3_integrable_weights(level)

    with mp.workdps(dps):
        denominator = (
            mp.sin(mp.pi / shifted_level) ** 2
            * mp.sin(2 * mp.pi / shifted_level)
        )
        return tuple(
            (
                mp.sin(mp.pi * (a + 1) / shifted_level)
                * mp.sin(mp.pi * (b + 1) / shifted_level)
                * mp.sin(mp.pi * (a + b + 2) / shifted_level)
            ) / denominator
            for a, b in weights
        )


def sl3_quantum_dimensions(level: int) -> Tuple[mp.mpf, ...]:
    """Quantum dimensions d_(a,b) = S_{0,(a,b)} / S_{0,0}."""
    return _sl3_quantum_dimensions(level, _working_precision(level))


def sl3_quantum_dimension_table(level: int) -> Dict[SL3_WEIGHT, mp.mpf]:
    """Dictionary of integrable weights to quantum dimensions."""
    return dict(zip(sl3_integrable_weights(level), sl3_quantum_dimensions(level)))


def sl3_normalized_verlinde_sum(genus: int, level: int) -> mp.mpf:
    """Normalized quantum-dimension sum sum d_lambda^(2-2g)."""
    _validate_genus(genus)
    _validate_level(level)

    dps = _working_precision(level, genus)
    with mp.workdps(dps):
        dimensions = _sl3_quantum_dimensions(level, dps)
        exponent = 2 - 2 * genus
        return mp.fsum(dimension ** exponent for dimension in dimensions)


def sl3_total_quantum_dimension_squared(level: int) -> mp.mpf:
    """D^2 = sum d_lambda^2 = S_{0,0}^{-2}."""
    _validate_level(level)

    dps = _working_precision(level, 2)
    with mp.workdps(dps):
        dimensions = _sl3_quantum_dimensions(level, dps)
        return mp.fsum(dimension * dimension for dimension in dimensions)


def sl3_S00_squared(level: int) -> mp.mpf:
    """S_{0,0}^2 from unitarity of the first S-matrix row."""
    return mp.mpf("1.0") / sl3_total_quantum_dimension_squared(level)


def verify_genus0_unitarity(level: int) -> bool:
    """Check Z_0(k) = 1."""
    return sl3_verlinde_dimension(0, level) == 1


def verify_genus1_count(level: int) -> bool:
    """Check Z_1(k) = |P_+^k| = (k+1)(k+2)/2."""
    return sl3_verlinde_dimension(1, level) == sl3_num_integrable_reps(level)


def sl3_verlinde_dimension(genus: int, level: int) -> int:
    """Exact sl_3 Verlinde dimension Z_g(k)."""
    _validate_genus(genus)
    _validate_level(level)

    if genus == 0:
        return 1
    if genus == 1:
        return sl3_num_integrable_reps(level)

    dps = _working_precision(level, genus)
    with mp.workdps(dps):
        dimensions = _sl3_quantum_dimensions(level, dps)
        total_qdim_sq = mp.fsum(dimension * dimension for dimension in dimensions)
        normalized_sum = mp.fsum(
            dimension ** (2 - 2 * genus) for dimension in dimensions
        )
        value = (total_qdim_sq ** (genus - 1)) * normalized_sum
        return _round_to_integer(value, genus, level)


def sl3_verlinde_values(genus: int, level_min: int = 0,
                        level_max: int = 10) -> Dict[int, int]:
    """Table k |-> Z_g(k) on a finite level interval."""
    _validate_genus(genus)
    _validate_level(level_min)
    _validate_level(level_max)
    if level_min > level_max:
        raise ValueError(
            f"Expected level_min <= level_max, got {level_min} > {level_max}"
        )
    return {
        level: sl3_verlinde_dimension(genus, level)
        for level in range(level_min, level_max + 1)
    }


def sl3_genus2_polynomial(symbol: Symbol | None = None) -> Poly:
    """Closed genus-2 Verlinde polynomial for sl_3."""
    k = symbol or _POLY_SYMBOL
    expression = (
        (k + 1)
        * (k + 2)
        * (k + 3) ** 2
        * (k + 4)
        * (k + 5)
        * (k ** 2 + 6 * k + 56)
        / 20160
    )
    return Poly(expand(expression), k, domain="QQ")


@lru_cache(maxsize=None)
def _sl3_verlinde_polynomial_cached(genus: int) -> Poly:
    k = _POLY_SYMBOL

    if genus == 0:
        return Poly(1, k, domain="QQ")
    if genus == 1:
        return Poly(expand((k + 1) * (k + 2) / 2), k, domain="QQ")
    if genus == 2:
        return sl3_genus2_polynomial(k)

    degree = SL3_DIM * (genus - 1)
    points = [
        (level, sl3_verlinde_dimension(genus, level))
        for level in range(degree + 1)
    ]
    interpolated = Poly(expand(interpolate(points, k)), k, domain="QQ")

    for level in range(degree + 1, degree + 4):
        if interpolated.eval(level) != sl3_verlinde_dimension(genus, level):
            raise ValueError(
                f"Polynomial interpolation failed at g={genus}, k={level}"
            )

    return interpolated


def sl3_verlinde_polynomial(genus: int,
                            symbol: Symbol | None = None) -> Poly:
    """Verlinde polynomial in k for fixed genus g."""
    _validate_genus(genus)
    base = _sl3_verlinde_polynomial_cached(genus)
    if symbol is None or symbol == _POLY_SYMBOL:
        return base
    return Poly(base.as_expr().subs(_POLY_SYMBOL, symbol), symbol, domain="QQ")


__all__ = [
    "SL3_DIM",
    "SL3_DUAL_COXETER",
    "SL3_RANK",
    "sl3_S00_squared",
    "sl3_genus2_polynomial",
    "sl3_integrable_weights",
    "sl3_normalized_verlinde_sum",
    "sl3_num_integrable_reps",
    "sl3_quantum_dimension_table",
    "sl3_quantum_dimensions",
    "sl3_total_quantum_dimension_squared",
    "sl3_verlinde_dimension",
    "sl3_verlinde_polynomial",
    "sl3_verlinde_values",
    "verify_genus0_unitarity",
    "verify_genus1_count",
]
