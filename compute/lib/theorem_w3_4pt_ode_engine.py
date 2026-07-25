r"""Four-point W3 input data and the open scalar-ODE problem.

Möbius gauge fixing leaves one cross-ratio for four marked points.  This
kinematic fact and the W3 OPE packet are exact.  A Fuchsian scalar equation
requires a module on the singular-vector locus, Ward reduction, a flat
connection, and a cyclic scalar functional.  Pole order alone supplies none
of those comparison maps.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Tuple

import sympy as sp

from compute.lib.theorem_w3_commuting_hamiltonians_engine import (
    ClaimPacket,
    H_COLL,
    H_FLAT,
    H_SCALAR,
    H_WARD,
    beta_composite,
    lambda_zero_mode_on_primary,
    leading_norm_packet,
    max_ope_pole,
    max_ope_pole_algebra,
    ope_mode,
    zamolodchikov_metric,
)


H_BS = (
    "H_W3^BS: a Kac--Shapovalov singular-vector locus with the explicit null relation and Ward reduction"
)


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


MAX_OPE_POLE_W3 = 6
K_MAX_W3 = _open("W3 collision depth", H_COLL)
K_MAX_VIR = _open("Virasoro collision depth", H_COLL)
DIFF_ORDER_W3 = _open("W3 scalar differential-equation order", H_COLL, H_WARD, H_FLAT, H_SCALAR)
LAMBDA_COUPLING_NUMERATOR = Fraction(32)
LAMBDA_COUPLING_DENOMINATOR_C_COEFF = Fraction(5)
LAMBDA_COUPLING_DENOMINATOR_CONST = Fraction(22)
LAMBDA_STATE_L4_COEFF = Fraction(-3, 5)
LAMBDA_FIELD_D2T_COEFF = Fraction(-3, 10)
UNIVERSAL_NORMALIZATION_SINGULAR_C = (Fraction(0), Fraction(-22, 5))


def _sym(value):
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.sympify(value)


def lambda_coupling_denominator(c):
    return sp.simplify(5 * _sym(c) + 22)


def zamolodchikov_lambda_norm(c):
    return zamolodchikov_metric(c)


def w3_lambda_coupling(c):
    return beta_composite(c)


def w3_universal_normalization_domain(c) -> Mapping[str, object]:
    c_val = _sym(c)
    denominator = lambda_coupling_denominator(c_val)
    norm = zamolodchikov_lambda_norm(c_val)
    return {
        "c": c_val,
        "lambda_coupling_denominator": denominator,
        "lambda_norm": norm,
        "coupling_chart_regular": sp.simplify(denominator) != 0,
        "gram_regular": sp.simplify(norm) != 0,
        "regular": sp.simplify(denominator) != 0 and sp.simplify(norm) != 0,
    }


def require_regular_universal_normalization(c):
    domain = w3_universal_normalization_domain(c)
    if not domain["regular"]:
        raise ValueError("The selected W3 normalization requires c(5c+22) nonzero.")
    return domain


def w3_channel_norm_matrix(c):
    """Return the exact diagonal leading two-point form on ``(T,W)``."""

    c_val = _sym(c)
    return sp.diag(c_val / 2, c_val / 3)


def w3_channel_kappa_matrix(c):
    """Compatibility packet separating OPE norms from modular curvature."""

    return {
        "mathematical_type": "leading OPE norm matrix",
        "matrix": w3_channel_norm_matrix(c),
        "modular_kappa_matrix": _open("W3 modular channel-curvature matrix", "H_W3^mod"),
    }


def diagnostic_scope_4pt() -> Mapping[str, object]:
    return {
        "cross_ratio_dimension": "exact",
        "finite_OPE": "exact",
        "scalar_ODE": _open("W3 four-point scalar ODE", H_COLL, H_WARD, H_FLAT, H_SCALAR, H_BS),
        "fuchsianity": _open("regular-singular structure of the scalar W3 equation", H_WARD, H_SCALAR, H_BS),
        "commutativity": _open("W3 four-point Hamiltonian flatness", H_COLL, H_WARD, H_FLAT),
    }


def sl2_fixed_positions() -> Mapping[str, object]:
    return {"z1": sp.Integer(0), "z2": sp.Symbol("z"), "z3": sp.Integer(1), "z4": sp.oo}


def n_moduli(n_points: int) -> int:
    if n_points < 3:
        raise ValueError("Stable genus-zero marked curves have at least three markings.")
    return n_points - 3


def virasoro_bpz_4pt_hamiltonian(c, h1, h2, h3, h4) -> ClaimPacket:
    return _open("Virasoro BPZ four-point Hamiltonian", H_WARD, H_FLAT, H_SCALAR, H_BS)


def w3_4pt_hamiltonian(c, h1, h2, h3, h4, w1, w2, w3_ch, w4) -> ClaimPacket:
    return _open("W3 four-point Hamiltonian", H_COLL, H_WARD, H_FLAT)


def extract_scalar_ode_coefficients(*_args, **_kwargs) -> ClaimPacket:
    return _open("scalar W3 four-point ODE coefficients", H_COLL, H_WARD, H_FLAT, H_SCALAR, H_BS)


def t_sector_restriction_4pt(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 T-sector restriction to a Virasoro BPZ equation", H_WARD, H_SCALAR, H_BS)


def w_sector_leading_term(*_args, **_kwargs) -> ClaimPacket:
    return _open("projected W-sector leading term", H_COLL, H_WARD, H_SCALAR)


def ode_order_analysis(family="w3", N=3) -> ClaimPacket:
    return _open(f"{family} scalar ODE order", H_COLL, H_WARD, H_FLAT, H_SCALAR, H_BS)


def w3_exceeds_virasoro_order() -> ClaimPacket:
    return _open("comparison of W3 and Virasoro scalar ODE orders", H_COLL, H_WARD, H_SCALAR, H_BS)


def verify_depth_4_vanishing(c_values=None) -> Mapping[str, object]:
    """Record the exact local coefficient ``W_(4)W=0``."""

    values = c_values or (1, 2, 10)
    return {
        "values": tuple(_sym(value) for value in values),
        "W_(4)W": tuple(ope_mode("W", "W", 4, value) for value in values),
        "all_zero": all(ope_mode("W", "W", 4, value) == {} for value in values),
        "collision_consequence": _open("depth-four collision statement", H_COLL),
    }


def surviving_depths_on_primaries(*_args, **_kwargs) -> ClaimPacket:
    return _open("surviving W3 collision depths on primary modules", H_COLL, H_WARD)


def evaluate_hamiltonian_at_z(*_args, **_kwargs) -> ClaimPacket:
    return _open("numerical evaluation of the W3 Hamiltonian", H_COLL, H_WARD, H_FLAT)


def w3_minimal_model_c2() -> Mapping[str, object]:
    return {
        "c": sp.Integer(2),
        "status": "regular OPE parameter value",
        "minimal_model_identification": _open("minimal-model realization at c=2", H_BS),
    }


def w3_c2_specific_coefficients(h_j, w_j=0) -> Mapping[str, object]:
    h_val = _sym(h_j)
    return {
        "c": sp.Integer(2),
        "WW_to_Lambda": beta_composite(2),
        "WW_to_dLambda": beta_composite(2) / 2,
        "Lambda_zero": lambda_zero_mode_on_primary(2, h_val),
        "W_charge": _sym(w_j),
        "collision_projection": _open("c=2 W3 collision projection", H_COLL, H_WARD),
    }


def fuchsian_structure_4pt() -> ClaimPacket:
    return _open("Fuchsian structure at 0,1,infinity", H_WARD, H_FLAT, H_SCALAR, H_BS)


def channel_structure_4pt(c) -> Mapping[str, object]:
    return {
        "leading_norm_matrix": w3_channel_norm_matrix(c),
        "OPE_pole_orders": {
            "TT": max_ope_pole("T", "T"),
            "TW": max_ope_pole("T", "W"),
            "WT": max_ope_pole("W", "T"),
            "WW": max_ope_pole("W", "W"),
        },
        "max_OPE_pole": max_ope_pole_algebra(),
        "collision_channels": _open("four-point W3 collision channels", H_COLL, H_WARD),
    }


def full_4pt_ode_summary(c, h1, h2, h3, h4, w1=0, w2=0, w3_ch=0, w4=0):
    return {
        "positions": sl2_fixed_positions(),
        "moduli_dimension": n_moduli(4),
        "normalization": w3_universal_normalization_domain(c),
        "channels": channel_structure_4pt(c),
        "Lambda_zero_values": tuple(lambda_zero_mode_on_primary(c, h) for h in (h1, h2, h3, h4)),
        "Hamiltonian": w3_4pt_hamiltonian(c, h1, h2, h3, h4, w1, w2, w3_ch, w4),
        "scalar_ODE": extract_scalar_ode_coefficients(c, h1, h2, h3, h4, w1, w2, w3_ch, w4),
        "scope": diagnostic_scope_4pt(),
    }
