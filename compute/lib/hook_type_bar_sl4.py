r"""Exact ``sl_4`` hook arithmetic with typed bar-comparison claims.

The partitions ``(2,1,1)`` and ``(3,1)`` form a transpose orbit.  Their
centralizer generator ledgers, good-grading ghost sums, KRW central charges,
and the formal reflection ``k -> -k-8`` are exact.  Every generator is even.

The OPE coefficients of these two universal W-algebras, completed bar
cohomology, curvature comparison, DS--bar commutation, PBW collapse, and
object-level Koszul comparison require explicit calculations and the package
``H_hook^{DS/bar}``.  Their compatibility APIs return typed claim packets.
"""

from __future__ import annotations

from typing import Dict

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    H_HOOK_DS_BAR,
    OpenInvariantError,
    c_sl4_211,
    c_sl4_31,
    complementarity_constant,
    ds_kappa_from_affine,
    ghost_constant,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import transpose_partition


PARTITION_211 = (2, 1, 1)
PARTITION_31 = (3, 1)
N = 4
k = Symbol("k")


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.OPEN, None, hypotheses=tuple(hypotheses))


def _conditional(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.CONDITIONAL, None, hypotheses=tuple(hypotheses))


GENERATORS_211 = {
    "J1": {"weight": Rational(1), "parity": "even", "role": "grade-zero current"},
    "J2": {"weight": Rational(1), "parity": "even", "role": "grade-zero current"},
    "J3": {"weight": Rational(1), "parity": "even", "role": "grade-zero current"},
    "J4": {"weight": Rational(1), "parity": "even", "role": "grade-zero current"},
    "G1": {"weight": Rational(3, 2), "parity": "even", "role": "charged generator"},
    "G2": {"weight": Rational(3, 2), "parity": "even", "role": "charged generator"},
    "G3": {"weight": Rational(3, 2), "parity": "even", "role": "charged generator"},
    "G4": {"weight": Rational(3, 2), "parity": "even", "role": "charged generator"},
    "L": {"weight": Rational(2), "parity": "even", "role": "Virasoro generator"},
}
GENERATOR_NAMES_211 = tuple(GENERATORS_211)

GENERATORS_31 = {
    "J": {"weight": Rational(1), "parity": "even", "role": "grade-zero current"},
    "W1": {"weight": Rational(2), "parity": "even", "role": "weight-two generator"},
    "W2": {"weight": Rational(2), "parity": "even", "role": "weight-two generator"},
    "W3": {"weight": Rational(2), "parity": "even", "role": "weight-two generator"},
    "V": {"weight": Rational(3), "parity": "even", "role": "weight-three generator"},
}
GENERATOR_NAMES_31 = tuple(GENERATORS_31)


def c_211(level=k):
    """Return the exact KRW central charge for ``(2,1,1)``."""

    return c_sl4_211(sympify(level))


def c_31(level=k):
    """Return the exact KRW central charge for ``(3,1)``."""

    return c_sl4_31(sympify(level))


def kappa_211(level=k) -> ClaimPacket:
    return ds_kappa_from_affine(PARTITION_211, sympify(level))


def kappa_31(level=k) -> ClaimPacket:
    return ds_kappa_from_affine(PARTITION_31, sympify(level))


def dual_level(level=k):
    """Return the formal reflection ``k -> -k-8``."""

    return hook_dual_level_sl_n(N, sympify(level))


def kappa_anti_symmetry_sum(level=k) -> ClaimPacket:
    """Return the open modular-conductor packet for the transpose corridor."""

    return kappa_complementarity_sum(PARTITION_31, sympify(level))


def c_complementarity_sum(level=k):
    """Return the exact central-charge sum under formal reflection."""

    kk = sympify(level)
    return simplify(c_31(kk) + c_211(dual_level(kk)))


def complementarity_constant_value():
    """Return the signed transpose ghost sum, an exact combinatorial scalar."""

    return complementarity_constant(PARTITION_31)


def residual_sl2_level(level=k) -> ClaimPacket:
    return _open(
        "residual sl2 current level for the (2,1,1) reduction",
        "an explicit BRST current calculation with normalization",
    )


def residual_u1_level(level=k) -> ClaimPacket:
    return _open(
        "residual u1 current level for the (2,1,1) reduction",
        "an explicit BRST current calculation with normalization",
    )


def ope_weight1_weight1() -> ClaimPacket:
    return _open(
        "weight-one OPE coefficients for W(sl4,f_(2,1,1))",
        "primary-source formulas or a direct BRST OPE calculation",
    )


def ope_virasoro() -> ClaimPacket:
    return _conditional(
        "Virasoro OPE embedded in W(sl4,f_(2,1,1))",
        "the KRW conformal vector and normalization comparison",
    )


def ope_weight1_fermionic() -> ClaimPacket:
    """Compatibility name for the even charged-current OPE obligation."""

    return _open(
        "weight-one/even-charged OPE coefficients for W(sl4,f_(2,1,1))",
        "a direct BRST OPE calculation",
    )


def ope_fermionic_leading() -> ClaimPacket:
    """Compatibility name for the even charged-pair leading OPE obligation."""

    return _open(
        "leading even charged-pair OPE coefficients for W(sl4,f_(2,1,1))",
        "a direct BRST OPE calculation",
    )


def vacuum_character_211(max_weight: int) -> ClaimPacket:
    return _conditional(
        f"vacuum character of W(sl4,f_(2,1,1)) through weight {max_weight}",
        "PBW freeness at the specified level and null-vector control",
    )


def vacuum_dim_211(weight) -> ClaimPacket:
    return vacuum_character_211(int(Rational(weight)) + 1)


def vacuum_character_31(max_weight: int) -> ClaimPacket:
    return _conditional(
        f"vacuum character of W(sl4,f_(3,1)) through weight {max_weight}",
        "PBW freeness at the specified level and null-vector control",
    )


def bar_deg1_dim_211() -> int:
    """Return the exact number of bar filtration-degree-one cogenerators."""

    return len(GENERATORS_211)


def bar_deg2_chain_dim_211(weight) -> ClaimPacket:
    return _conditional(
        f"completed bar filtration-degree-two chain dimension at weight {Rational(weight)}",
        "a chosen completed bar model and PBW freeness",
    )


def bar_deg1_dim_31() -> int:
    """Return the exact number of bar filtration-degree-one cogenerators."""

    return len(GENERATORS_31)


def curvature_211() -> ClaimPacket:
    return _open(
        "curvature element for the completed (2,1,1) chiral bar complex",
        "all normalized binary OPE pairings and the collision kernel",
    )


def curvature_31() -> ClaimPacket:
    return _open(
        "curvature element for the completed (3,1) chiral bar complex",
        "all normalized binary OPE pairings and the collision kernel",
    )


def verify_transport_to_transpose() -> Dict[str, object]:
    """Return exact transpose arithmetic and typed transport claims."""

    return {
        "transpose_relation": transpose_partition(PARTITION_211) == PARTITION_31,
        "transpose_involution": transpose_partition(PARTITION_31) == PARTITION_211,
        "source_generator_count": bar_deg1_dim_211(),
        "target_generator_count": bar_deg1_dim_31(),
        "formal_reflected_level": dual_level(k),
        "formal_central_charge_sum": c_complementarity_sum(k),
        "modular_conductor": kappa_anti_symmetry_sum(k),
        "ds_bar_commutation": _conditional("DS--bar commutation for the sl4 hook pair", H_HOOK_DS_BAR),
        "koszul_duality": _conditional("object-level Koszul comparison for the sl4 hook pair", H_HOOK_DS_BAR),
    }


def verify_ghost_constants() -> Dict[str, bool]:
    """Verify the exact good-grading ghost sums."""

    source = ghost_constant(PARTITION_211)
    target = ghost_constant(PARTITION_31)
    return {
        "C_(2,1,1)=3": source == 3,
        "C_(3,1)=6": target == 6,
        "transpose_ghost_sum=9": source + target == 9,
        "signed_transpose_ghost_sum=-9": complementarity_constant_value() == -9,
    }


def verify_partition_duality() -> Dict[str, bool]:
    """Verify the exact transpose orbit."""

    return {
        "(2,1,1)^t=(3,1)": transpose_partition(PARTITION_211) == PARTITION_31,
        "(3,1)^t=(2,1,1)": transpose_partition(PARTITION_31) == PARTITION_211,
        "(2,2)^t=(2,2)": transpose_partition((2, 2)) == (2, 2),
    }


def ds_bar_commutation_211() -> ClaimPacket:
    return _conditional("DS--bar commutation for partition (2,1,1)", H_HOOK_DS_BAR)


def ds_bar_commutation_31() -> ClaimPacket:
    return _conditional("DS--bar commutation for partition (3,1)", H_HOOK_DS_BAR)


def is_chirally_koszul_211() -> ClaimPacket:
    return _conditional(
        "chiral Koszulness of W(sl4,f_(2,1,1))",
        "H_PBW^bar: filtered chiral bar comparison, convergence, collapse, and extension control",
        H_HOOK_DS_BAR,
    )


def verify_all() -> Dict[str, object]:
    """Return an exact arithmetic audit and typed frontier obligations."""

    data_211 = w_algebra_generator_data(PARTITION_211)
    data_31 = w_algebra_generator_data(PARTITION_31)
    return {
        **verify_partition_duality(),
        **verify_ghost_constants(),
        "source_generator_count=9": data_211.f_centralizer_dimension == 9,
        "target_generator_count=5": data_31.f_centralizer_dimension == 5,
        "source_all_even": data_211.n_odd == 0,
        "target_all_even": data_31.n_odd == 0,
        "source_central_charge": c_211(k),
        "target_central_charge": c_31(k),
        "modular_conductor": kappa_anti_symmetry_sum(k),
        "ds_bar_source": ds_bar_commutation_211(),
        "ds_bar_target": ds_bar_commutation_31(),
        "koszulness": is_chirally_koszul_211(),
    }
