"""Weight-filtered completion scaffold for infinite-generator bar complexes.

This module isolates the chain-group side of the completed bar construction
needed for infinite-generator families such as W_infinity. The guiding fact is
simple: if there is one strong generator in every conformal weight s >= 2, then
the completed bar complex is still finite in each total weight h, because only
ordered tuples

    (w_1, ..., w_n),  w_i >= 2,  sum_i w_i = h

can contribute. In particular:

  - only generator weights <= h appear in weight h;
  - the maximal bar degree is floor(h/2);
  - the weight-h, degree-n sector has size C(h-n-1, n-1);
  - the total weight-h sector has size F_{h-1}.

This is the pronilpotent finiteness mechanism behind the first step of the
completed W_infinity bar programme. The actual OPE/differential data still has
to be added separately.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb
from typing import Dict, Iterable, Tuple


WeightMonomial = Tuple[int, ...]


def max_bar_degree(total_weight: int, min_generator_weight: int = 2) -> int:
    """Largest possible bar degree at fixed total conformal weight."""
    if total_weight < 0:
        raise ValueError("total_weight must be nonnegative")
    if min_generator_weight <= 0:
        raise ValueError("min_generator_weight must be positive")
    return total_weight // min_generator_weight


def effective_generator_weights(
    total_weight: int,
    generator_weights: Iterable[int],
) -> Tuple[int, ...]:
    """Discard generators that can never appear in total weight `total_weight`."""
    if total_weight < 0:
        raise ValueError("total_weight must be nonnegative")
    weights = sorted(
        {
            int(weight)
            for weight in generator_weights
            if 2 <= int(weight) <= total_weight
        }
    )
    return tuple(weights)


def w_infinity_generator_weights(total_weight: int) -> Tuple[int, ...]:
    """Effective W_infinity generator weights in total weight `total_weight`."""
    if total_weight < 2:
        return ()
    return tuple(range(2, total_weight + 1))


@lru_cache(maxsize=1024)
def _ordered_weight_monomials_cached(
    total_weight: int,
    generator_weights: Tuple[int, ...],
    bar_degree: int,
) -> Tuple[WeightMonomial, ...]:
    if total_weight < 0 or bar_degree < 0:
        return ()
    if bar_degree == 0:
        return ((),) if total_weight == 0 else ()
    if not generator_weights:
        return ()

    min_weight = generator_weights[0]
    max_weight = generator_weights[-1]
    if total_weight < bar_degree * min_weight:
        return ()
    if total_weight > bar_degree * max_weight:
        return ()

    basis = []
    for first in generator_weights:
        if first > total_weight:
            break
        tails = _ordered_weight_monomials_cached(
            total_weight - first,
            generator_weights,
            bar_degree - 1,
        )
        for tail in tails:
            basis.append((first,) + tail)
    return tuple(basis)


def ordered_weight_monomials(
    total_weight: int,
    generator_weights: Iterable[int],
    bar_degree: int,
) -> Tuple[WeightMonomial, ...]:
    """Ordered generator-weight monomials in fixed total weight and bar degree."""
    weights = effective_generator_weights(total_weight, generator_weights)
    return _ordered_weight_monomials_cached(total_weight, weights, bar_degree)


def weight_sector_profile(
    total_weight: int,
    generator_weights: Iterable[int],
) -> Dict[int, Tuple[WeightMonomial, ...]]:
    """Bar-degree decomposition of the fixed-weight completed chain group."""
    weights = effective_generator_weights(total_weight, generator_weights)
    profile: Dict[int, Tuple[WeightMonomial, ...]] = {}
    for degree in range(1, max_bar_degree(total_weight) + 1):
        monomials = _ordered_weight_monomials_cached(total_weight, weights, degree)
        if monomials:
            profile[degree] = monomials
    return profile


def degree_sector_dimension_formula(total_weight: int, bar_degree: int) -> int:
    """Closed form for ordered compositions of `total_weight` into `bar_degree` parts >= 2."""
    if total_weight < 2 or bar_degree < 1:
        return 0
    if total_weight < 2 * bar_degree:
        return 0
    return comb(total_weight - bar_degree - 1, bar_degree - 1)


def fibonacci(n: int) -> int:
    """Fibonacci number with F_0 = 0, F_1 = 1."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def total_sector_dimension_formula(total_weight: int) -> int:
    """Total number of ordered weight monomials in W_infinity weight `total_weight`."""
    if total_weight < 2:
        return 0
    return fibonacci(total_weight - 1)


def w_infinity_weight_sector(total_weight: int) -> Dict[int, Tuple[WeightMonomial, ...]]:
    """Completed W_infinity chain-group basis in total weight `total_weight`."""
    return weight_sector_profile(total_weight, w_infinity_generator_weights(total_weight))


def verify_w_infinity_completion(max_weight: int = 10) -> Dict[str, bool]:
    """Sanity checks for the weight-filtered W_infinity completion scaffold."""
    results: Dict[str, bool] = {}

    for total_weight in range(2, max_weight + 1):
        profile = w_infinity_weight_sector(total_weight)
        enlarged_profile = weight_sector_profile(
            total_weight,
            range(2, total_weight + 5),
        )

        results[f"weight {total_weight} truncates above spin {total_weight}"] = (
            profile == enlarged_profile
        )

        top_degree = max(profile, default=0)
        results[f"weight {total_weight} max degree is floor(h/2)"] = (
            top_degree == max_bar_degree(total_weight)
        )

        total_dimension = 0
        for degree, basis in profile.items():
            expected_degree_dim = degree_sector_dimension_formula(total_weight, degree)
            total_dimension += len(basis)
            results[f"weight {total_weight} degree {degree} dimension formula"] = (
                len(basis) == expected_degree_dim
            )
            results[f"weight {total_weight} degree {degree} sums to h"] = all(
                len(monomial) == degree and sum(monomial) == total_weight
                for monomial in basis
            )

        results[f"weight {total_weight} Fibonacci total"] = (
            total_dimension == total_sector_dimension_formula(total_weight)
        )

    return results
