r"""Finite Bouwknegt--Schoutens data for the standard W3 algebra.

Certified outputs are OPE coefficients, highest-weight mode arithmetic,
minimal-model parameter formulas, and the level-one singular-vector curve.
Collision Hamiltonians, bar curvature, scalar shadows, and differential
equations require named comparison packages and remain open.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, Mapping, Tuple

import sympy as sp


W3_BETA_SINGULAR_C = Fraction(-22, 5)

H_BAR = (
    "H_W3^bar: an ordered configuration-space residue bar complex with fixed signs and completion"
)
H_PROJ = (
    "H_W3^proj: a chain-compatible projection of the full multi-channel Maurer--Cartan tensor"
)
H_COLL = (
    "H_W3^coll: a collision-residue map with descendant and composite channels retained"
)
H_BS = (
    "H_W3^BS: the relevant Kac--Shapovalov determinant locus, singular vector, Ward reduction, and monodromy control"
)
H_MOD = (
    "H_W3^mod: a trace-compatible genus-one curvature calculation"
)
H_DIAG = (
    "H_diag^{g=1}: non-separating sewing traces the diagonal leading-pole pairing and mixed channels are orthogonal"
)
H_DS_BAR = (
    "H_W3^{DS/bar}: the formally reflected principal chart is the chosen bar/Verdier companion"
)


class OpenW3ComparisonError(RuntimeError):
    """Signals that finite W3 data have reached a comparison boundary."""


@dataclass(frozen=True)
class ClaimPacket:
    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


def _conditional(statement: str, value, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "conditional", value, tuple(hypotheses))


def _sym(value):
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.sympify(value)


def _require_regular(c):
    if sp.simplify(5 * _sym(c) + 22) == 0:
        raise ValueError("Zamolodchikov normalization has a pole at c=-22/5.")


def beta_w3(c):
    r"""Return the pole-two ``WW Lambda`` coefficient ``32/(22+5c)``."""

    _require_regular(c)
    c_val = _sym(c)
    return sp.Integer(32) / (5 * c_val + 22)


def reciprocal_weight_diagnostic_w3():
    """Return the generator-weight arithmetic ``1/2+1/3=5/6``."""

    return sp.Rational(5, 6)


def w3_harmonic_ratio():
    """Compatibility name for the reciprocal-weight diagnostic."""

    return reciprocal_weight_diagnostic_w3()


def leading_norm_channels_w3(c) -> Mapping[str, object]:
    """Return the exact leading two-point OPE coefficients."""

    c_val = _sym(c)
    return {
        "T": c_val / 2,
        "W": c_val / 3,
        "weights": {"T": 2, "W": 3},
        "ratio": sp.Rational(2, 3),
        "mathematical_type": "leading OPE norms",
    }


def kappa_channels_w3(c):
    c_val = _sym(c)
    return {
        "status": "conditional",
        "T": ClaimPacket("W3 T-channel modular kappa", "conditional", c_val / 2, (H_DIAG,)),
        "W": ClaimPacket("W3 W-channel modular kappa", "conditional", c_val / 3, (H_DIAG,)),
        "total": ClaimPacket("W3 modular kappa", "conditional", sp.simplify(5 * c_val / 6), (H_DIAG,)),
    }


def kappa_principal_w3(c):
    return kappa_channels_w3(c)["total"]


def kappa_total_w3(c):
    return kappa_principal_w3(c)


def uniform_weight_reduction_diagnostic(c=None) -> Mapping[str, object]:
    """Return exact weights and typed status of any scalar reduction."""

    result = {
        "weights": (2, 3),
        "is_uniform_weight": False,
        "leading_norms": leading_norm_channels_w3(sp.Symbol("c") if c is None else c),
        "scalar_modular_reduction": kappa_principal_w3(sp.Symbol("c") if c is None else c),
        "all_genus_reduction": _open("W3 all-genus scalar reduction", H_MOD, H_PROJ),
    }
    return result


def lambda_zero_witness(h) -> Mapping[str, object]:
    r"""Return the exact action of ``Lambda_0`` on ``|h,w>``."""

    h_val = _sym(h)
    return {
        "normal_ordered_TT_zero": h_val**2 + 2 * h_val,
        "d2T_zero": 6 * h_val,
        "lambda_zero": sp.factor(h_val**2 + h_val / 5),
        "formula": "h^2+h/5",
    }


def lambda_zero_on_primary(c, h):
    return lambda_zero_witness(h)["lambda_zero"]


def w3_ww_ope_modes(c) -> Mapping[str, object]:
    """Return the exact Zamolodchikov-normalized singular WW packet."""

    c_val = _sym(c)
    alpha = beta_w3(c_val)
    return {
        "normalization": "Bouwknegt--Schoutens/Zamolodchikov",
        "mode_5": {"fields": {"vac": c_val / 3}, "ope_pole_order": 6},
        "mode_4": {"fields": {}, "ope_pole_order": 5},
        "mode_3": {"fields": {"T": sp.Integer(2)}, "ope_pole_order": 4},
        "mode_2": {"fields": {"dT": sp.Integer(1)}, "ope_pole_order": 3},
        "mode_1": {
            "fields": {"d2T": sp.Rational(3, 10), "Lambda": alpha},
            "ope_pole_order": 2,
        },
        "mode_0": {
            "fields": {"d3T": sp.Rational(1, 15), "dLambda": alpha / 2},
            "ope_pole_order": 1,
        },
        "alpha_ope": alpha,
        "beta_mode": alpha / 2,
    }


def w3_mode_lambda_coefficient(m, n, c):
    """Return the Lambda-mode coefficient in ``[W_m,W_n]``."""

    return sp.simplify(beta_w3(c) * (_sym(m) - _sym(n)) / 2)


def w3_rmatrix_collision_poles(c) -> ClaimPacket:
    return _open("W3 collision r-matrix poles", H_COLL)


def finite_ope_diagnostic_scope() -> Mapping[str, object]:
    return {
        "finite_ope_modes": "exact",
        "lambda_zero_mode": "exact",
        "level_one_null_curve": "exact determinant equation",
        "collision_hamiltonian": _open("W3 collision Hamiltonian", H_COLL),
        "ordered_bar": _open("W3 ordered bar differential", H_BAR),
        "scalar_shadow": _open("W3 scalar shadow", H_BAR, H_PROJ),
        "modular_kappa": _open("W3 modular kappa", H_MOD),
    }


def w3_minimal_model_c(p, pp):
    r"""Return ``2(1-12(p-p')^2/(pp'))``."""

    p_val, pp_val = _sym(p), _sym(pp)
    if p_val == 0 or pp_val == 0:
        raise ValueError("Minimal-model parameters are nonzero.")
    return sp.factor(2 * (1 - 12 * (p_val - pp_val) ** 2 / (p_val * pp_val)))


def w3_kac_weight(r, s, p, pp):
    """Return the Virasoro-sublattice Kac-weight arithmetic."""

    r_val, s_val, p_val, pp_val = map(_sym, (r, s, p, pp))
    return sp.factor(
        ((r_val * pp_val - s_val * p_val) ** 2 - (pp_val - p_val) ** 2)
        / (4 * p_val * pp_val)
    )


def _sqrt_fraction_if_square(value: Fraction):
    if value < 0:
        return None
    numerator = math.isqrt(value.numerator)
    denominator = math.isqrt(value.denominator)
    if numerator**2 == value.numerator and denominator**2 == value.denominator:
        return Fraction(numerator, denominator)
    return None


def bpz_degenerate_weight(c):
    r"""Return the formal Virasoro level-two roots inside the T-sector."""

    if isinstance(c, (int, Fraction)) and not isinstance(c, bool):
        c_frac = Fraction(c)
        discriminant = (c_frac - 1) * (c_frac - 25)
        square_root = _sqrt_fraction_if_square(discriminant)
        return {
            "discriminant": discriminant,
            "sqrt_discriminant": square_root,
            "h_plus": None if square_root is None else (5 - c_frac + square_root) / 16,
            "h_minus": None if square_root is None else (5 - c_frac - square_root) / 16,
            "exact_rational": square_root is not None,
            "mathematical_type": "Virasoro T-sector determinant roots",
        }
    c_val = _sym(c)
    root = sp.sqrt((c_val - 1) * (c_val - 25))
    return {
        "discriminant": (c_val - 1) * (c_val - 25),
        "sqrt_discriminant": root,
        "h_plus": (5 - c_val + root) / 16,
        "h_minus": (5 - c_val - root) / 16,
        "exact_rational": False,
        "mathematical_type": "Virasoro T-sector determinant roots",
    }


def bpz_null_vector_ode(c, h1, h2, h3, h4) -> ClaimPacket:
    data = {
        "order": 2,
        "leading_coefficient": sp.simplify(2 * (2 * _sym(h1) + 1) / 3),
        "null_vector": "L_-2-3 L_-1^2/[2(2h+1)]",
    }
    return _conditional("Virasoro BPZ equation inside the W3 T-sector", data, H_BS)


def bpz_ode_indicial_exponents(c, h1, h_ext) -> ClaimPacket:
    a_value = sp.simplify(2 * (2 * _sym(h1) + 1) / 3)
    data = {"a_coefficient": a_value, "discriminant": sp.simplify(1 + 4 * _sym(h_ext) / a_value)}
    return _conditional("Virasoro BPZ indicial equation", data, H_BS)


def w3_level_one_null_curve(c, h, w):
    r"""Return the exact level-one determinant polynomial.

    The singular locus is
    ``9 w^2(22+5c)=2 h^2(32h+2-c)``.
    """

    c_val, h_val, w_val = map(_sym, (c, h, w))
    return sp.expand(9 * w_val**2 * (22 + 5 * c_val) - 2 * h_val**2 * (32 * h_val + 2 - c_val))


def level_one_null_status(c, h, w) -> Mapping[str, object]:
    polynomial = w3_level_one_null_curve(c, h, w)
    return {
        "polynomial": polynomial,
        "is_on_curve": sp.simplify(polynomial) == 0,
        "status": "exact level-one Kac--Shapovalov condition",
    }


def collision_depth_ode_virasoro(*_args, **_kwargs) -> ClaimPacket:
    return _open("Virasoro collision-depth Hamiltonian", H_COLL)


def collision_depth_ode_w3(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 collision-depth Hamiltonian", H_COLL)


def compare_bpz_equations(*_args, **_kwargs) -> ClaimPacket:
    return _open("comparison of W3 collision and BPZ equations", H_COLL, H_BS)


def w3_tline_shadow_data(c) -> ClaimPacket:
    return _open("W3 T-line scalar shadow", H_BAR, H_PROJ)


def w3_wline_shadow_data(c) -> ClaimPacket:
    return _open("W3 W-line scalar shadow", H_BAR, H_PROJ)


def w3_extra_depths_on_primaries(*_args, **_kwargs) -> ClaimPacket:
    return _open("W3 projected collision depths on primaries", H_COLL, H_PROJ)


def bs_w3_null_vector_level2(c, h, w) -> ClaimPacket:
    return _open("W3 level-two singular vector and differential equation", H_BS)


def verify_depth_4_vanishing_bs() -> Mapping[str, object]:
    """Record the exact absence of the fifth-order WW pole."""

    return {
        "W_(4)W": sp.Integer(0),
        "status": "exact OPE coefficient",
        "collision_consequence": _open("depth-four collision consequence", H_COLL),
    }


def compare_at_c2(h1=0, h2=0, h3=0, h4=0, w1=0, w2=0, w3_ch=0, w4=0):
    return compare_at_generic_c(Fraction(2), h1, h2, h3, h4, w1, w2, w3_ch, w4)


def compare_at_generic_c(c, h1, h2, h3, h4, w1=0, w2=0, w3_ch=0, w4=0):
    return {
        "c": _sym(c),
        "ope": w3_ww_ope_modes(c),
        "lambda_zero_h1": lambda_zero_on_primary(c, h1),
        "level_one_null_curve_h1": w3_level_one_null_curve(c, h1, w1),
        "collision": _open("W3 collision comparison", H_COLL),
        "bpz": _open("W3/BPZ differential-equation comparison", H_COLL, H_BS),
        "shadow": _open("W3 scalar shadow comparison", H_BAR, H_PROJ),
    }


def full_comparison_summary(c=Fraction(2)):
    return {
        "c": _sym(c),
        "finite_ope": w3_ww_ope_modes(c),
        "leading_norms": leading_norm_channels_w3(c),
        "scope": finite_ope_diagnostic_scope(),
        "status": "finite OPE and determinant arithmetic exact; comparison theorems open",
    }
