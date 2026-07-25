"""Genus-1 PBW support for principal finite-type W-algebras.

This module records the structural mechanism used in the manuscript's
all-genera PBW theorem for principal W-algebras:

  - The principal W^k(g) generators have weights m_i + 1, where m_i are the
    exponents of g.
  - The exponent 1 occurs exactly once, so there is a unique weight-2
    generator T (the stress tensor).
  - For a homogeneous state of conformal weight h, the n-th product with a
    generator of weight s has weight h + s - n - 1.
  - Hence every (1)-product from a higher-spin generator (s > 2) strictly
    raises conformal weight, while T_(1) = L_0 preserves weight.

The low-weight vacuum-module engine in ``w3_bar_extended.py`` computes the
``L_0`` action on every displayed PBW state.  Homogeneous product degrees are
exact bookkeeping.  The nonlinear ``W_(1)`` action on composite PBW states is
recorded separately as an open construction problem.
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Sequence, Tuple

from compute.lib.lie_algebra import cartan_data
from compute.lib.w3_bar_extended import ClaimPacket, W3VacuumModule, state_weight


Family = Tuple[str, int]

DEFAULT_FAMILIES: Tuple[Family, ...] = (
    ("A", 1),
    ("A", 2),
    ("A", 3),
    ("B", 2),
    ("C", 2),
    ("G", 2),
    ("F", 4),
)


def principal_generator_weights(type_: str, rank: int) -> List[int]:
    """Generator weights for the principal finite-type W-algebra of g."""
    return [exponent + 1 for exponent in cartan_data(type_, rank).exponents]


def d2_weight_shift(generator_weight: int) -> int:
    """Weight shift of the (1)-product by a generator of weight `generator_weight`."""
    return generator_weight - 2


def d2_target_weight(source_weight: int, generator_weight: int) -> int:
    """Target conformal weight of a_(1) on a source block of weight `source_weight`."""
    return source_weight + d2_weight_shift(generator_weight)


def has_unique_stress_tensor(type_: str, rank: int) -> bool:
    """Principal W-algebras have a unique weight-2 generator."""
    weights = principal_generator_weights(type_, rank)
    return weights.count(2) == 1


def higher_spin_generators(type_: str, rank: int) -> List[int]:
    """Weights of the non-stress strong generators."""
    return [weight for weight in principal_generator_weights(type_, rank) if weight > 2]


def verify_principal_weight_argument(
    families: Sequence[Family] = DEFAULT_FAMILIES,
    max_weight: int = 10,
) -> Dict[str, bool]:
    """Check the generator-weight input behind the triangular d_2 argument."""
    results: Dict[str, bool] = {}

    for type_, rank in families:
        weights = principal_generator_weights(type_, rank)
        label = f"{type_}{rank}"
        results[f"{label} unique weight-2 generator"] = has_unique_stress_tensor(type_, rank)
        results[f"{label} higher generators have weight > 2"] = all(
            weight > 2 for weight in higher_spin_generators(type_, rank)
        )

        for source_weight in range(2, max_weight + 1):
            diagonal_targets = [
                d2_target_weight(source_weight, weight)
                for weight in weights
                if weight == 2
            ]
            off_diagonal_targets = [
                d2_target_weight(source_weight, weight)
                for weight in weights
                if weight > 2
            ]
            results[f"{label} diagonal d2 stays on weight {source_weight}"] = (
                diagonal_targets == [source_weight]
            )
            results[f"{label} off-diagonal d2 raises weight from {source_weight}"] = all(
                target > source_weight for target in off_diagonal_targets
            )

    return results


def verify_w3_l0_scalar(max_weight: int = 8, c_val: float = 7.0) -> Dict[str, bool]:
    """Check that L_0 acts diagonally by conformal weight on W_3 through `max_weight`."""
    module = W3VacuumModule(max_weight=max_weight, c_val=c_val)
    results: Dict[str, bool] = {}

    for weight in range(2, max_weight + 1):
        ok = True
        for state in module.vbar_states_at_weight(weight):
            result = module._L_on_state(0, state)
            same = result.get(state, 0.0)
            off_diagonal = any(
                s != state and abs(coeff) > 1e-12
                for s, coeff in result.items()
            )
            if abs(same - weight) > 1e-12 or off_diagonal:
                ok = False
                break
        results[f"W3 L0 = {weight} id on weight-{weight} sector"] = ok

    return results


def verify_w3_d2_weight_pattern(
    max_weight: int = 8,
    c_val: float = 7.0,
) -> Dict[str, bool]:
    """Compute the homogeneous nth-product target grades for ``W3``.

    For homogeneous ``a,b``, ``wt(a_(1)b)=wt(a)+wt(b)-2``.  This
    determines the grade containing the product whenever the product is
    constructed.  The formula alone supplies neither its matrix entries nor
    its identification with a PBW spectral-sequence differential.
    """
    results: Dict[str, bool] = {}

    for weight in range(2, max_weight + 1):
        results[f"W3 T_(1) target grade at source weight {weight}"] = (
            d2_target_weight(weight, 2) == weight
        )
        results[f"W3 W_(1) target grade at source weight {weight}"] = (
            d2_target_weight(weight, 3) == weight + 1
        )

    return results


def w3_composite_w1_action_claim(max_weight: int = 8) -> ClaimPacket:
    """Return the typed frontier for ``W_(1)`` on composite PBW states."""

    return ClaimPacket(
        f"W_(1) action on composite generic-W3 PBW states through weight {max_weight}",
        "open",
        None,
        (
            "H_W3^nl: a confluent nonlinear mode-algebra quotient on composite PBW states",
            "compatibility of the quotient action with the homogeneous conformal-weight grading",
        ),
    )


def verify_principal_w_pbw_genus1(
    families: Sequence[Family] = DEFAULT_FAMILIES,
    max_weight: int = 8,
    c_val: float = 7.0,
) -> Dict[str, object]:
    """Return exact weight support and the open PBW/genus-one comparison."""
    results: Dict[str, object] = {}
    results.update(verify_principal_weight_argument(families=families, max_weight=max_weight))
    results.update(verify_w3_l0_scalar(max_weight=max_weight, c_val=c_val))
    results.update(verify_w3_d2_weight_pattern(max_weight=max_weight, c_val=c_val))
    results["PBW spectral-sequence identification"] = ClaimPacket(
        "principal-W PBW differential is represented by the displayed (1)-product blocks",
        "open",
        None,
        (
            "H_W^PBW: complete separated filtration, identified pages, all differentials, and convergence",
            "H_W^g1: trace-compatible genus-one comparison",
        ),
    )
    return results
