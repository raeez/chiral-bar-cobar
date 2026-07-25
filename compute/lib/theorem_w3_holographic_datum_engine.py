r"""Exact local W3 data and typed reconstruction boundaries.

This module certifies the finite Zamolodchikov packet:

* the principal DS central charge and reflected central sum;
* the 32/16 OPE normalization;
* the norm and zero mode of Lambda;
* the level-one Shapovalov matrix and singular-vector curve.

Every passage from these local data to a presentation coalgebra, a
Verdier partner, a collision kernel, a modular scalar, a stable-graph
sum, a shadow metric, a Hamiltonian system, or a holographic lift is
represented by a packet carrying its hypothesis package.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Tuple

import sympy as sp


TYPE_LOCAL = (
    "Open quadrant; universal Zamolodchikov presentation; "
    "Beilinson level 1; H_W3^univ"
)
TYPE_BAR = (
    "Open quadrant; ordered completed chiral bar; "
    "Beilinson level 2; H_W3^bar"
)
TYPE_MODULAR = (
    "Open quadrant; modular trace presentation; "
    "Beilinson level 5; H_W3^mod"
)

H_PRES = "H_W3^pres: topological generators, relations, and q_A comparison"
H_BAR = "H_W3^bar: ordered configuration-space bar, signs, and completion"
H_DS_BAR = "H_W3^DS/bar: PBW convergence, BRST concentration, and bar transport"
H_VERDIER = "H_W3^Verdier: continuous Ran--Verdier duality and rectification"
H_CENTER = "H_W3^cen: derived-centre chain model and family support"
H_COLL = "H_W3^coll: collision residue retaining descendants and composites"
H_MOD = "H_W3^mod: trace-compatible genus-one curvature"
H_RES = "H_W3^res: chain-compatible residue functionals"
H_PROJ = "H_W3^proj: full multi-channel scalar projection"
H_SEW = "H_W3^sew: clutching propagators, graph weights, and convergence"
H_FLAT = "H_W3^flat: representation of the MC equation on conformal blocks"
H_LINE = "H_W3^line: line-category comparison"
H_OC = "H_W3^OC: open--closed comparison with the derived centre"
H_RESCALE = "H_W3^rescale: family contraction and scalar trace identification"


@dataclass(frozen=True)
class ClaimPacket:
    """A value together with its epistemic and type data."""

    statement: str
    status: str
    value: Any = None
    hypotheses: Tuple[str, ...] = ()
    type_signature: str = ""


def exact(statement: str, value: Any, type_signature: str = TYPE_LOCAL) -> ClaimPacket:
    return ClaimPacket(statement, "exact", value, (), type_signature)


def open_claim(
    statement: str,
    *hypotheses: str,
    type_signature: str,
) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses), type_signature)


def conditional(
    statement: str,
    value: Any,
    *hypotheses: str,
    type_signature: str,
) -> ClaimPacket:
    return ClaimPacket(
        statement,
        "conditional",
        value,
        tuple(hypotheses),
        type_signature,
    )


def _sym(value: Any) -> sp.Expr:
    return sp.sympify(value)


def _regular_d(c: Any) -> sp.Expr:
    c_value = _sym(c)
    d_value = sp.expand(5 * c_value + 22)
    if d_value == 0:
        raise ValueError("The Zamolodchikov normalization requires 5*c+22 invertible.")
    return d_value


def w3_generators() -> Mapping[str, Mapping[str, Any]]:
    """Return the exact strong-generator packet."""

    return {
        "T": {"weight": 2, "leading_self_ope": "c/2", "max_ope_pole": 4},
        "W": {"weight": 3, "leading_self_ope": "c/3", "max_ope_pole": 6},
    }


def w3_central_charge(k: Any) -> sp.Expr:
    """Return the principal W3 central charge."""

    k_value = _sym(k)
    if sp.simplify(k_value + 3) == 0:
        raise ValueError("The principal DS formula requires k+3 invertible.")
    return sp.factor(2 - 24 * (k_value + 2) ** 2 / (k_value + 3))


def reflected_level(k: Any) -> sp.Expr:
    return -_sym(k) - 6


def reflected_central_charge(k: Any) -> sp.Expr:
    """Return the central charge evaluated at the reflected parameter."""

    return sp.factor(w3_central_charge(reflected_level(k)))


def reflected_central_sum(k: Any) -> sp.Expr:
    """Return the exact rational-function sum."""

    return sp.factor(w3_central_charge(k) + reflected_central_charge(k))


def reflected_central_packet(k: Any) -> ClaimPacket:
    data = {
        "k": _sym(k),
        "k_reflected": reflected_level(k),
        "c": w3_central_charge(k),
        "c_reflected": reflected_central_charge(k),
        "sum": reflected_central_sum(k),
        "formal_midpoint": sp.Integer(50),
        "mathematical_type": "reflected principal central arithmetic",
    }
    return exact("principal W3 reflected central arithmetic", data)


def reciprocal_weight_diagnostic() -> ClaimPacket:
    """Return the generator-weight arithmetic with an explicit type."""

    data = {
        "weights": (2, 3),
        "value": sp.Rational(1, 2) + sp.Rational(1, 3),
        "mathematical_type": "reciprocal strong-generator weights",
    }
    return exact("W3 reciprocal-weight diagnostic", data)


def leading_ope_norms(c: Any) -> ClaimPacket:
    c_value = _sym(c)
    data = {
        "T": c_value / 2,
        "W": c_value / 3,
        "mathematical_type": "leading self-OPE norms",
    }
    return exact("W3 leading self-OPE norms", data)


def lambda_norm(c: Any) -> sp.Expr:
    """Return the exact Lambda norm."""

    c_value = _sym(c)
    return sp.factor(c_value * (5 * c_value + 22) / 10)


def lambda_virasoro_witness(c: Any) -> ClaimPacket:
    c_value = _sym(c)
    gram = {
        "L_-2^2,L_-2^2": c_value * (c_value + 8) / 2,
        "L_-4,L_-2^2": 3 * c_value,
        "L_-4,L_-4": 5 * c_value,
    }
    state = {"L_-2^2": sp.Integer(1), "L_-4": sp.Rational(-3, 5)}
    data = {
        "state": state,
        "gram": gram,
        "norm": lambda_norm(c_value),
        "L2_image_coefficient": (5 * c_value + 22) / 5,
    }
    return exact("Virasoro construction of Lambda and its norm", data)


def lambda_zero(h: Any) -> sp.Expr:
    h_value = _sym(h)
    return sp.factor(h_value**2 + h_value / 5)


def lambda_zero_packet(h: Any) -> ClaimPacket:
    h_value = _sym(h)
    data = {
        "normal_ordered_TT_zero": h_value**2 + 2 * h_value,
        "d2T_zero": 6 * h_value,
        "lambda_zero": lambda_zero(h_value),
    }
    return exact("Lambda_0 action on a W3 highest-weight vector", data)


def ww_ope_packet(c: Any) -> ClaimPacket:
    """Return the complete singular WW OPE coefficients."""

    c_value = _sym(c)
    d_value = _regular_d(c_value)
    alpha = sp.Integer(32) / d_value
    data = {
        "normalization": "Zamolodchikov/Bouwknegt--Schoutens",
        "pole_6": {"vacuum": c_value / 3},
        "pole_5": {},
        "pole_4": {"T": sp.Integer(2)},
        "pole_3": {"dT": sp.Integer(1)},
        "pole_2": {"d2T": sp.Rational(3, 10), "Lambda": alpha},
        "pole_1": {"d3T": sp.Rational(1, 15), "dLambda": alpha / 2},
        "lambda_ope_coefficient": alpha,
        "lambda_derivative_coefficient": alpha / 2,
        "lambda_mode_coefficient": alpha / 2,
    }
    return exact("complete singular Zamolodchikov WW packet", data)


def lambda_mode_commutator_coefficient(m: Any, n: Any, c: Any) -> sp.Expr:
    """Return the Lambda coefficient in the W-mode commutator."""

    packet = ww_ope_packet(c).value
    return sp.factor(packet["lambda_mode_coefficient"] * (_sym(m) - _sym(n)))


def level_one_gram_matrix(c: Any, h: Any, w: Any) -> sp.Matrix:
    c_value, h_value, w_value = map(_sym, (c, h, w))
    d_value = _regular_d(c_value)
    return sp.Matrix(
        [
            [2 * h_value, 3 * w_value],
            [
                3 * w_value,
                -h_value / 5
                + sp.Integer(32) / d_value * (h_value**2 + h_value / 5),
            ],
        ]
    )


def level_one_null_polynomial(c: Any, h: Any, w: Any) -> sp.Expr:
    """Return the exact determinant polynomial for the level-one curve."""

    c_value, h_value, w_value = map(_sym, (c, h, w))
    return sp.expand(
        9 * w_value**2 * (5 * c_value + 22)
        - 2 * h_value**2 * (32 * h_value + 2 - c_value)
    )


def level_one_packet(c: Any, h: Any, w: Any) -> ClaimPacket:
    matrix = level_one_gram_matrix(c, h, w)
    d_value = _regular_d(c)
    data = {
        "matrix": matrix,
        "determinant": sp.factor(matrix.det()),
        "null_polynomial": level_one_null_polynomial(c, h, w),
        "determinant_identity": sp.simplify(
            d_value * matrix.det() + level_one_null_polynomial(c, h, w)
        ),
        "kernel_vector_for_h_invertible": "W_-1 - (3*w)/(2*h) L_-1",
    }
    return exact("level-one W3 Shapovalov packet", data)


def presentation_coalgebra_packet() -> ClaimPacket:
    return open_claim(
        "W3 presentation coalgebra C_X(s^-1 V,s^-2 R) and q_A",
        H_PRES,
        type_signature=TYPE_BAR,
    )


def ordered_bar_packet() -> ClaimPacket:
    return open_claim(
        "completed ordered W3 bar complex and twisting coderivation",
        H_BAR,
        type_signature=TYPE_BAR,
    )


def koszul_partner_packet(k: Any) -> ClaimPacket:
    candidate = {
        "formal_parameter": reflected_level(k),
        "formal_central_charge": reflected_central_charge(k),
        "candidate": "principal W3 at k_reflected",
    }
    return conditional(
        "strict W3 Koszul partner at the reflected parameter",
        candidate,
        H_PRES,
        H_BAR,
        H_DS_BAR,
        H_VERDIER,
        type_signature=(
            "Open quadrant; completed bar--Verdier presentation; "
            "levels 1<->2; H_W3^DS/bar+H_W3^Verdier"
        ),
    )


def derived_center_packet() -> ClaimPacket:
    value = {
        "formal_target": "Z_ch^der(W3)=C_ch^bullet(W3,W3)",
        "comparison": open_claim(
            "physical HT bulk to chiral derived-centre comparison",
            H_CENTER,
            H_OC,
            type_signature=(
                "Open x CY quadrants; open--closed presentation; "
                "level 3; H_W3^cen+H_W3^OC"
            ),
        ),
    }
    return conditional(
        "concrete W3 chiral derived-centre entry",
        value,
        H_CENTER,
        type_signature=(
            "Open quadrant; chiral Hochschild presentation; "
            "level 3; H_W3^cen"
        ),
    )


def collision_kernel_packet(c: Any) -> ClaimPacket:
    ope = ww_ope_packet(c).value
    candidate = {
        "TT": {"poles": (3, 1), "formula": "(c/2)/z^3+2T/z"},
        "TW": {"poles": (1,), "formula": "3W/z"},
        "WT": {"poles": (1,), "formula": "3W/z"},
        "WW": {
            "poles": (5, 3, 2, 1),
            "coefficients": {
                "z^-5": _sym(c) / 3,
                "z^-3*T": sp.Integer(2),
                "z^-2*dT": sp.Integer(1),
                "z^-1*d2T": sp.Rational(3, 10),
                "z^-1*Lambda": ope["lambda_ope_coefficient"],
            },
        },
        "candidate_max_order": 5,
        "source_type": "exact local OPE after the stated residue convention",
    }
    return conditional(
        "ordered-bar W3 collision kernel",
        candidate,
        H_BAR,
        H_COLL,
        type_signature=TYPE_BAR,
    )


def maurer_cartan_packet() -> ClaimPacket:
    return conditional(
        "completed ordered W3 Maurer--Cartan element",
        {
            "ambient": "Conv(B^ord(W3),W3)",
            "equation": "D Theta + 1/2[Theta,Theta]=0",
        },
        H_PRES,
        H_BAR,
        type_signature=TYPE_BAR,
    )


def holomorphic_connection_packet() -> ClaimPacket:
    return conditional(
        "represented flat W3 holomorphic connection",
        {"formula": "d-Sh_{0,n}(Theta_W3)"},
        H_BAR,
        H_RES,
        H_FLAT,
        type_signature=(
            "Open quadrant; represented ordered bar; level 4; "
            "H_W3^bar+H_W3^res+H_W3^flat"
        ),
    )


def modular_kappa_packet() -> ClaimPacket:
    return open_claim(
        "genus-one scalar kappa_ch(W3)",
        H_MOD,
        H_RES,
        type_signature=TYPE_MODULAR,
    )


def modular_rho_packet() -> ClaimPacket:
    return open_claim(
        "modular anomaly ratio kappa_ch(W3)/c",
        H_MOD,
        H_RES,
        type_signature=TYPE_MODULAR,
    )


def scalar_conductor_packet() -> ClaimPacket:
    return open_claim(
        "scalar Verdier sum K^kappa(W3)",
        H_DS_BAR,
        H_VERDIER,
        H_MOD,
        H_RESCALE,
        type_signature=(
            "Open quadrant; bar--Verdier plus scalar trace; "
            "levels 2->5; H_W3^DS/bar+H_W3^mod+H_W3^rescale"
        ),
    )


def genus_graph_packet(genus: int) -> ClaimPacket:
    if genus < 2:
        raise ValueError("The coloured cross-channel packet starts at genus 2.")
    return open_claim(
        f"genus-{genus} coloured W3 stable-graph sum",
        H_BAR,
        H_PROJ,
        H_SEW,
        type_signature=(
            "Open quadrant; modular coloured graphs; level 5; "
            "H_W3^bar+H_W3^proj+H_W3^sew"
        ),
    )


def scalar_shadow_packet(line: str) -> ClaimPacket:
    if line not in {"T", "W", "mixed"}:
        raise ValueError("The W3 scalar-shadow line is T, W, or mixed.")
    return open_claim(
        f"W3 {line}-line scalar shadow",
        H_RES,
        H_PROJ,
        type_signature=(
            "Open quadrant; scalar projection; level 5; "
            "H_W3^res+H_W3^proj"
        ),
    )


def propagator_mixing_packet() -> ClaimPacket:
    return open_claim(
        "W3 two-channel propagator-mixing coordinate",
        H_RES,
        H_PROJ,
        H_SEW,
        type_signature=(
            "Open quadrant; two-channel scalar projection; level 5; "
            "H_W3^res+H_W3^proj+H_W3^sew"
        ),
    )


def hamiltonian_packet() -> ClaimPacket:
    return conditional(
        "commuting Hamiltonians from the represented W3 connection",
        {"commutator": "[H_i,H_j]=0", "candidate_order_bound": 4},
        H_COLL,
        H_FLAT,
        H_OC,
        type_signature=(
            "Open x CY quadrants; represented ordered bar; level 4; "
            "H_W3^coll+H_W3^flat+H_W3^OC"
        ),
    )


def line_comparison_packet(k: Any) -> ClaimPacket:
    return conditional(
        "W3 evaluation-line comparison",
        {
            "candidate": "Rep_q(sl3)",
            "q": f"exp(pi*i/({_sym(k)}+3))",
        },
        H_LINE,
        type_signature=(
            "Open x CY quadrants; line-category presentation; level 4; "
            "H_W3^line"
        ),
    )


def holographic_lift_packet() -> ClaimPacket:
    return open_claim(
        "full W3 holographic lift",
        H_PRES,
        H_BAR,
        H_DS_BAR,
        H_VERDIER,
        H_CENTER,
        H_COLL,
        H_MOD,
        H_RES,
        H_PROJ,
        H_RESCALE,
        H_SEW,
        H_FLAT,
        H_LINE,
        H_OC,
        type_signature=(
            "Open x CY quadrants; seven-entry reconstruction; "
            "levels 0--5; H_W3^hol"
        ),
    )


def exact_local_packet(k: Any, h: Any = 0, w: Any = 0) -> Mapping[str, ClaimPacket]:
    c_value = w3_central_charge(k)
    return {
        "central": reflected_central_packet(k),
        "ope": ww_ope_packet(c_value),
        "lambda": lambda_virasoro_witness(c_value),
        "lambda_zero": lambda_zero_packet(h),
        "level_one": level_one_packet(c_value, h, w),
    }


def holographic_datum(k: Any) -> Mapping[str, ClaimPacket]:
    """Return the seven entries with their exact epistemic statuses."""

    c_value = w3_central_charge(k)
    chart = exact(
        "principal W3 chart algebra",
        {
            "level": _sym(k),
            "central_charge": c_value,
            "generators": w3_generators(),
            "ope": ww_ope_packet(c_value).value,
        },
    )
    return {
        "A": chart,
        "A_i": presentation_coalgebra_packet(),
        "A_dual": koszul_partner_packet(k),
        "C": derived_center_packet(),
        "K_coll": collision_kernel_packet(c_value),
        "Theta": maurer_cartan_packet(),
        "nabla": holomorphic_connection_packet(),
    }


def verification_surface(k: Any, h: Any = 0, w: Any = 0) -> Mapping[str, Any]:
    """Return the exact packet, reconstruction packets, and total lift."""

    return {
        "exact_local": exact_local_packet(k, h, w),
        "seven_entries": holographic_datum(k),
        "modular": {
            "kappa": modular_kappa_packet(),
            "rho": modular_rho_packet(),
            "K_kappa": scalar_conductor_packet(),
        },
        "graphs": {2: genus_graph_packet(2), 3: genus_graph_packet(3)},
        "shadows": {
            "T": scalar_shadow_packet("T"),
            "W": scalar_shadow_packet("W"),
            "mixed": scalar_shadow_packet("mixed"),
        },
        "mixing": propagator_mixing_packet(),
        "hamiltonians": hamiltonian_packet(),
        "line": line_comparison_packet(k),
        "holographic_lift": holographic_lift_packet(),
    }
