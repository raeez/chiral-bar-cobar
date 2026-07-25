r"""Exact W3 OPE inputs and open collision-Hamiltonian obligations.

Finite pole data determine singular products.  A commuting Hamiltonian requires
a geometric collision-residue map, a representation-valued Ward action, a
flatness proof, and a scalar reduction.  This module computes the finite input
and represents every later step by a typed claim packet.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Tuple

import sympy as sp

from compute.lib.w3_bar import w3_nth_product, w3_nth_products


GENERATORS = ("T", "W")
WEIGHTS = {"T": 2, "W": 3}

H_COLL = (
    "H_W3^coll: a coordinate-independent collision-residue map with Arnold forms, orientations, descendants, and composites"
)
H_WARD = (
    "H_W3^Ward: a representation-valued Ward action on the chosen module tensor product"
)
H_FLAT = (
    "H_W3^flat: a proof that the resulting connection is flat on configuration space"
)
H_SCALAR = (
    "H_W3^scalar: a cyclic or conformal-block functional compatible with the connection"
)
H_BAR = (
    "H_W3^bar: the completed ordered residue bar complex and chain comparison"
)
H_MOD = (
    "H_W3^mod: a trace-compatible genus-one curvature calculation"
)
H_DIAG = (
    "H_diag^{g=1}: non-separating sewing traces the diagonal leading-pole pairing, with mixed channels orthogonal"
)
H_DS_BAR = (
    "H_W3^{DS/bar}: the principal reflected chart is identified with the chosen bar/Verdier companion"
)


class OpenW3HamiltonianError(RuntimeError):
    """Signals that OPE data have reached a geometric comparison boundary."""


@dataclass(frozen=True)
class ClaimPacket:
    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


def _sym(value):
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.sympify(value)


def central_charge_from_level(k):
    """Return ``c(k)=2-24(k+2)^2/(k+3)`` for principal W3."""

    k_val = _sym(k)
    return sp.factor(2 - 24 * (k_val + 2) ** 2 / (k_val + 3))


def principal_wN_central_charge(N: int, k):
    """Return the principal type-A central charge in the local coordinate."""

    if N < 2:
        raise ValueError("Principal W_N has N>=2.")
    k_val = _sym(k)
    return sp.factor(
        (N - 1) - N * (N**2 - 1) * (k_val + N - 1) ** 2 / (k_val + N)
    )


def formal_reflected_central_sum_wN(N: int, k=None):
    r"""Compute ``c_N(k)+c_N(-k-2N)=4N^3-2N-2``."""

    k_val = sp.Symbol("k") if k is None else _sym(k)
    return sp.simplify(
        principal_wN_central_charge(N, k_val)
        + principal_wN_central_charge(N, -k_val - 2 * N)
    )


W3_CENTRAL_CHARGE_CONDUCTOR = sp.Integer(100)
W3_KAPPA_CONDUCTOR = ClaimPacket(
    "W3 modular conductor", "conditional", sp.Rational(250, 3), (H_DIAG, H_DS_BAR)
)
W3_KAPPA_RATIO = ClaimPacket(
    "W3 modular characteristic ratio", "conditional", sp.Rational(5, 6), (H_DIAG,)
)
W3_SELF_DUAL_CENTRAL_CHARGE = sp.Integer(50)
W3_SELF_DUAL_KAPPA = ClaimPacket(
    "W3 modular kappa at the formal central midpoint",
    "conditional",
    sp.Rational(125, 3),
    (H_DIAG,),
)


def leading_norm_T(c):
    return _sym(c) / 2


def leading_norm_W(c):
    return _sym(c) / 3


def leading_norm_packet(c) -> Mapping[str, object]:
    c_val = _sym(c)
    return {
        "T": leading_norm_T(c_val),
        "W": leading_norm_W(c_val),
        "ratio": sp.Rational(2, 3),
        "type": "leading OPE two-point coefficients",
    }


def kappa_T(c):
    return ClaimPacket("W3 T-channel modular kappa", "conditional", _sym(c) / 2, (H_DIAG,))


def kappa_W(c):
    return ClaimPacket("W3 W-channel modular kappa", "conditional", _sym(c) / 3, (H_DIAG,))


def kappa_total(c):
    return ClaimPacket("W3 modular kappa", "conditional", sp.simplify(5 * _sym(c) / 6), (H_DIAG,))


def beta_composite(c):
    r"""Return the pole-two ``WW Lambda`` coupling ``32/(22+5c)``."""

    c_val = _sym(c)
    if sp.simplify(5 * c_val + 22) == 0:
        raise ValueError("Zamolodchikov normalization has a pole at c=-22/5.")
    return sp.Integer(32) / (5 * c_val + 22)


def zamolodchikov_metric(c):
    r"""Return ``<Lambda,Lambda>=c(5c+22)/10``."""

    c_val = _sym(c)
    return sp.factor(c_val * (5 * c_val + 22) / 10)


def inverse_metric(c):
    """Return the exact reciprocal Gram entry on its regular locus."""

    metric = zamolodchikov_metric(c)
    if sp.simplify(metric) == 0:
        raise ValueError("The Lambda Gram entry vanishes on this parameter value.")
    return sp.cancel(1 / metric)


def w3_exchange_ratios(c) -> Mapping[str, object]:
    """Separate OPE-normalized and mode-normalized Lambda exchange ratios."""

    c_val = _sym(c)
    norm = zamolodchikov_metric(c_val)
    ope = beta_composite(c_val)
    mode = ope / 2
    return {
        "OPE_normalized": sp.cancel(ope**2 / norm),
        "mode_normalized": sp.cancel(mode**2 / norm),
        "full_quartic_tensor": _open("full W3 quartic tensor", H_COLL, H_SCALAR),
    }


def w3_uniform_weight_reduction(c) -> Mapping[str, object]:
    return {
        "weights": (2, 3),
        "leading_norms": leading_norm_packet(c),
        "uniform_weight": False,
        "scalar_modular_reduction": kappa_total(c),
    }


def w3_shadow_constants(c) -> ClaimPacket:
    return _open("W3 scalar shadow constants", H_BAR, H_COLL, H_SCALAR)


def _substitute_c(packet: Mapping[str, object], c_val):
    c_symbol = sp.Symbol("c")
    return {
        state: sp.simplify(_sym(coefficient).subs(c_symbol, _sym(c_val)))
        for state, coefficient in packet.items()
    }


def ope_mode(a: str, b: str, n: int, c=None):
    """Return one exact singular nth product, optionally specialized in c."""

    packet = w3_nth_product(a, b, n)
    return packet if c is None else _substitute_c(packet, c)


def max_ope_pole(a: str, b: str) -> int:
    products = w3_nth_products().get((a, b), {})
    return 0 if len(products) == 0 else max(products) + 1


def max_ope_pole_algebra() -> int:
    return max(max_ope_pole(a, b) for a in GENERATORS for b in GENERATORS)


def collision_residue_on_primary(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 collision residue on a primary", H_COLL, H_WARD)


def w3_collision_residue_table(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 collision-residue table", H_COLL, H_WARD)


def w3_hamiltonian_primary_coefficient(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 Hamiltonian primary coefficient", H_COLL, H_WARD, H_FLAT)


def w3_hamiltonian_4pt_primary(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 four-point Hamiltonian", H_COLL, H_WARD, H_FLAT)


def virasoro_hamiltonian_primary_coefficient(*_args, **_kwargs) -> ClaimPacket:
    return _open("Virasoro collision Hamiltonian on primaries", H_COLL, H_WARD)


def k_max_family(family: str, N: int = 3):
    raise OpenW3HamiltonianError(
        f"Collision depth for {family} awaits {H_COLL}; finite OPE pole order is available separately."
    )


def differential_operator_order(family: str, N: int = 3):
    raise OpenW3HamiltonianError(
        f"Differential-operator order for {family} awaits {H_COLL}, {H_WARD}, and {H_SCALAR}."
    )


def differential_operator_order_wN(N: int):
    return differential_operator_order("wN", N)


def wN_structure(N: int) -> Mapping[str, object]:
    if N < 2:
        raise ValueError("W_N has N>=2.")
    return {
        "N": N,
        "generator_weights": tuple(range(2, N + 1)),
        "largest_diagonal_leading_OPE_pole": 2 * N,
        "formal_reflected_central_sum": formal_reflected_central_sum_wN(N),
        "collision_depth": _open(f"W_{N} collision depth", H_COLL),
        "scalar_ode_order": _open(f"W_{N} scalar ODE order", H_COLL, H_WARD, H_SCALAR),
    }


def cross_family_comparison() -> Mapping[str, object]:
    return {
        "Virasoro": {"weights": (2,), "max_OPE_pole": 4},
        "W3": {"weights": (2, 3), "max_OPE_pole": 6},
        "W4": {"weights": (2, 3, 4), "max_diagonal_leading_OPE_pole": 8},
        "collision_comparison": _open("cross-family collision-depth comparison", H_COLL),
    }


def t_sector_restriction(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 T-sector collision restriction", H_COLL, H_WARD)


def lambda_zero_mode_on_primary(c, h):
    r"""Return ``Lambda_0|h,w>=(h^2+h/5)|h,w>``."""

    h_val = _sym(h)
    return sp.factor(h_val**2 + h_val / 5)


def lambda_on_primary_w3(c, h, w=0):
    return lambda_zero_mode_on_primary(c, h)


def w3_hamiltonian_on_primaries(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 Hamiltonian action on primaries", H_COLL, H_WARD, H_FLAT)


def w3_hamiltonian_scalar_on_primaries(*_args, **_kwargs) -> ClaimPacket:
    return _open("scalar W3 Hamiltonian on primaries", H_COLL, H_WARD, H_FLAT, H_SCALAR)


def verify_commutativity_4pt_w3(*_args, **_kwargs) -> ClaimPacket:
    return _open("four-point W3 Hamiltonian commutativity", H_COLL, H_WARD, H_FLAT)


def verify_commutativity_5pt_w3(*_args, **_kwargs) -> ClaimPacket:
    return _open("five-point W3 Hamiltonian commutativity", H_COLL, H_WARD, H_FLAT)


def w3_ward_identities(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 Ward identities on the selected module tensor product", H_WARD)


def ode_order_prediction(*_args, **_kwargs) -> ClaimPacket:
    return _open("scalar ODE order extracted from the W3 connection", H_COLL, H_WARD, H_FLAT, H_SCALAR)


def koszul_conductor_wN(N: int):
    harmonic = sum(sp.Rational(1, j) for j in range(2, N + 1))
    return ClaimPacket(
        f"W_{N} modular conductor",
        "conditional",
        sp.simplify(harmonic * formal_reflected_central_sum_wN(N)),
        (H_DIAG, H_DS_BAR),
    )


def full_evaluation(c, h_j=0, w_j=0) -> Mapping[str, object]:
    return {
        "central_charge": _sym(c),
        "OPE": {pair: {n: ope_mode(*pair, n, c) for n in products} for pair, products in w3_nth_products().items()},
        "leading_norms": leading_norm_packet(c),
        "Lambda_norm": zamolodchikov_metric(c),
        "Lambda_zero": lambda_zero_mode_on_primary(c, h_j),
        "level_arithmetic": {"formal_reflected_central_sum": 100},
        "Hamiltonian": _open("W3 commuting Hamiltonian", H_COLL, H_WARD, H_FLAT),
        "scalar_ODE": _open("W3 scalar conformal-block ODE", H_COLL, H_WARD, H_FLAT, H_SCALAR),
    }
