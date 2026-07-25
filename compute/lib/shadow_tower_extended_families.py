r"""Exact OPE data and typed shadow obligations for extended families.

The computational boundary in this module is deliberate.  It certifies the
standard :math:`\mathcal W_3` and Bershadsky--Polyakov OPE packets, their
two-point norms, and elementary reflection identities.  A scalar shadow
coefficient belongs to a later construction: the ordered residue bar model,
the full multi-channel Maurer--Cartan tensor, and a chain-compatible scalar
projection.  Requests for that later datum therefore raise
``OpenShadowProjectionError``.

Primary conventions
-------------------

* Zamolodchikov normalization for :math:`\mathcal W_3`, as reviewed by
  Bouwknegt--Schoutens (1993): the pole-two coefficient of
  :math:`\Lambda={:TT:}-\frac3{10}\partial^2T` is
  :math:`32/(22+5c)`; its derivative coefficient is half of this.
* Fehily--Kawasetsu--Ridout (2021), equations (2.1)--(2.2), for the ordinary
  Bershadsky--Polyakov vertex algebra.  The generators
  :math:`J,G^+,G^-,T` are all even and
  :math:`c(k)=-(2k+3)(3k+1)/(k+3)`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple

import sympy as sp


H_BAR = (
    "H_bar: a completed ordered residue bar complex with its signed "
    "Fulton--MacPherson differential"
)
H_PROJ = (
    "H_proj: a chain map from the full multi-channel Maurer--Cartan tensor "
    "to the selected scalar line"
)
H_WINFINITY = (
    "H_Winfinity^(4): a universal-OPE coordinate conversion, normalized "
    "weight-three field, finite-rank comparison, and weight-four Gram matrix"
)
H_SUPER_YANGIAN = (
    "H_gl(1|1)^line: a chiral current realization, nondegenerate invariant "
    "form, parity-compatible ordered residue model, and scalar trace"
)


class OpenShadowProjectionError(RuntimeError):
    """Signals that exact OPE data have reached the projection boundary."""


@dataclass(frozen=True)
class ClaimPacket:
    """A compact epistemic packet for a computed or open claim."""

    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()
    source: str = ""


def _sym(value):
    return sp.sympify(value)


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


def _projection_error(family: str) -> OpenShadowProjectionError:
    return OpenShadowProjectionError(
        f"{family} scalar shadow awaits {H_BAR} and {H_PROJ}."
    )


# ---------------------------------------------------------------------------
# Zamolodchikov-normalized W_3 data
# ---------------------------------------------------------------------------


def zamolodchikov_norm_T(c):
    """Return the leading ``TT`` coefficient ``N_T=c/2``."""

    return _sym(c) / 2


def zamolodchikov_norm_W(c):
    """Return the leading ``WW`` coefficient ``N_W=c/3``."""

    return _sym(c) / 3


def zamolodchikov_norm_Lambda(c):
    r"""Return :math:`N_\Lambda=c(5c+22)/10`.

    This is also obtained from the level-four vacuum Gram matrix in the
    basis ``(L_-2^2 1, L_-4 1)`` and the vector ``(1,-3/5)``.
    """

    c_val = _sym(c)
    return sp.factor(c_val * (5 * c_val + 22) / 10)


def level_four_vacuum_gram_matrix(c):
    """Return the exact level-four Virasoro vacuum Gram matrix."""

    c_val = _sym(c)
    return sp.Matrix(
        [
            [c_val * (c_val + 8) / 2, 3 * c_val],
            [3 * c_val, 5 * c_val],
        ]
    )


def lambda_norm_from_gram(c):
    """Compute ``N_Lambda`` by the independent Gram-matrix route."""

    vector = sp.Matrix([1, sp.Rational(-3, 5)])
    return sp.factor((vector.T * level_four_vacuum_gram_matrix(c) * vector)[0])


def w3_alpha_coefficient(c):
    r"""Return the pole-two :math:`WW\Lambda` coefficient ``32/(22+5c)``."""

    c_val = _sym(c)
    return sp.Integer(32) / (22 + 5 * c_val)


def w3_derivative_lambda_coefficient(c):
    r"""Return the pole-one :math:`\partial\Lambda` coefficient."""

    return sp.simplify(w3_alpha_coefficient(c) / 2)


def w3_mode_lambda_coefficient(m, n, c):
    """Return the coefficient of ``Lambda_(m+n)`` in ``[W_m,W_n]``."""

    return sp.simplify(
        sp.Integer(16) * (_sym(m) - _sym(n)) / (22 + 5 * _sym(c))
    )


def w3_ope_packet(c) -> Mapping[str, object]:
    """Return the exact singular ``WW`` packet in nth-product notation."""

    c_val = _sym(c)
    alpha = w3_alpha_coefficient(c_val)
    return {
        "status": "proved elsewhere",
        "normalization": "Zamolodchikov",
        "source": "Bouwknegt--Schoutens (1993), standard W_3 OPE",
        "generators": {
            "T": {"weight": sp.Integer(2), "parity": "even"},
            "W": {"weight": sp.Integer(3), "parity": "even"},
        },
        "WW": {
            5: {"vac": c_val / 3},
            3: {"T": sp.Integer(2)},
            2: {"dT": sp.Integer(1)},
            1: {"d2T": sp.Rational(3, 10), "Lambda": alpha},
            0: {
                "d3T": sp.Rational(1, 15),
                "dLambda": sp.simplify(alpha / 2),
            },
        },
    }


def virasoro_level_four_inverse_norm(c):
    """Return the exact reciprocal of the ``Lambda`` two-point norm."""

    return sp.cancel(1 / zamolodchikov_norm_Lambda(c))


def w3_t_line_status(c) -> Mapping[str, object]:
    """Return exact T-line data and the typed scalar-projection frontier."""

    c_val = _sym(c)
    return {
        "status": "exact OPE restriction; scalar shadow open",
        "N_T": zamolodchikov_norm_T(c_val),
        "N_Lambda": zamolodchikov_norm_Lambda(c_val),
        "inverse_N_Lambda": virasoro_level_four_inverse_norm(c_val),
        "scalar_shadow": _open("W_3 T-line scalar shadow", H_BAR, H_PROJ),
    }


def w3_w_line_status(c) -> Mapping[str, object]:
    """Return exact W-line OPE inputs and the quartic projection frontier."""

    c_val = _sym(c)
    return {
        "status": "exact OPE inputs; four-channel scalar projection open",
        "N_W": zamolodchikov_norm_W(c_val),
        "N_Lambda": zamolodchikov_norm_Lambda(c_val),
        "WW_to_Lambda": w3_alpha_coefficient(c_val),
        "WW_to_dLambda": w3_derivative_lambda_coefficient(c_val),
        "scalar_quartic": _open(
            "W_3 W-line quartic shadow from TT, T-Lambda, and Lambda-Lambda channels",
            H_BAR,
            H_PROJ,
        ),
    }


# ---------------------------------------------------------------------------
# Bershadsky--Polyakov exact conformal and OPE data
# ---------------------------------------------------------------------------


def bp_c_arakawa(k):
    r"""Return the standard FKR central charge.

    The historical compatibility name is retained because several local
    callers use it; the returned formula is the ordinary BP central charge.
    """

    k_val = _sym(k)
    return sp.factor(-((2 * k_val + 3) * (3 * k_val + 1)) / (k_val + 3))


def bp_shifted_secondary_c(k):
    """Return the separate shifted secondary expression."""

    k_val = _sym(k)
    return sp.factor(2 - 24 * (k_val + 1) ** 2 / (k_val + 3))


def bp_j_level_feigin_semikhatov(k):
    """Return the exact ``J_(1)J`` coefficient ``(2k+3)/3``."""

    return (2 * _sym(k) + 3) / 3


def bp_generator_packet() -> Mapping[str, Mapping[str, object]]:
    """Return the standard strong generators; every generator is even."""

    return {
        "J": {"weight": sp.Integer(1), "parity": "even"},
        "G+": {"weight": sp.Rational(3, 2), "parity": "even"},
        "G-": {"weight": sp.Rational(3, 2), "parity": "even"},
        "T": {"weight": sp.Integer(2), "parity": "even"},
    }


def bp_ope_packet(k) -> Mapping[str, object]:
    """Return the FKR ``JJ`` and ``G+G-`` singular products."""

    k_val = _sym(k)
    return {
        "status": "proved elsewhere",
        "source": "Fehily--Kawasetsu--Ridout (2021), equations (2.1)--(2.2)",
        "central_charge": bp_c_arakawa(k_val),
        "generators": bp_generator_packet(),
        "JJ": {1: {"vac": bp_j_level_feigin_semikhatov(k_val)}},
        "G+G-": {
            2: {"vac": (k_val + 1) * (2 * k_val + 3)},
            1: {"J": 3 * (k_val + 1)},
            0: {
                ":JJ:": sp.Integer(3),
                "dJ": sp.Rational(3, 2) * (k_val + 1),
                "T": -(k_val + 3),
            },
        },
        "reverse_products": "ordinary vertex-algebra skew symmetry",
    }


def bp_t_inverse_norm(k):
    """Return the exact BP T-line reciprocal ``Lambda`` norm."""

    c_val = bp_c_arakawa(k)
    return sp.cancel(10 / (c_val * (5 * c_val + 22)))


def bp_t_inverse_norm_factored(k):
    """Return the independently factored BP reciprocal norm."""

    k_val = _sym(k)
    return sp.cancel(
        10 * (k_val + 3) ** 2
        / (
            3
            * (2 * k_val + 3)
            * (3 * k_val + 1)
            * (10 * k_val**2 + 11 * k_val - 17)
        )
    )


def bp_reflected_central_sum(k):
    """Compute the standard reflected central sum, identically ``50``."""

    k_val = _sym(k)
    return sp.simplify(bp_c_arakawa(k_val) + bp_c_arakawa(-k_val - 6))


def bp_shifted_reflected_sum(k):
    """Compute the shifted secondary reflected sum, identically ``196``."""

    k_val = _sym(k)
    return sp.simplify(
        bp_shifted_secondary_c(k_val) + bp_shifted_secondary_c(-k_val - 6)
    )


def bp_t_line_status(k) -> Mapping[str, object]:
    """Return exact BP T-line data and its multi-channel frontier."""

    k_val = _sym(k)
    return {
        "status": "exact Virasoro restriction; BP scalar projection open",
        "central_charge": bp_c_arakawa(k_val),
        "inverse_N_Lambda": bp_t_inverse_norm(k_val),
        "scalar_quartic": _open(
            "BP T-line quartic shadow including J and charged channels",
            H_BAR,
            H_PROJ,
        ),
    }


def bp_modular_status() -> Mapping[str, ClaimPacket]:
    """Return the open genus-one BP ledger."""

    hypothesis = (
        "H_BP^mod: complete minimal-DS genus-one curvature with charged ghosts, "
        "neutral fields, conformal improvement, and mixed channels"
    )
    return {
        name: _open(f"Bershadsky--Polyakov {name}", hypothesis)
        for name in ("kappa", "rho", "K^kappa")
    }


# ---------------------------------------------------------------------------
# Universal W and super-Yangian frontiers
# ---------------------------------------------------------------------------


def w_infinity_endpoint_status() -> ClaimPacket:
    """Return the typed endpoint quartic comparison obligation."""

    return _open("W_infinity endpoint quartic projection", H_WINFINITY, H_BAR, H_PROJ)


def super_yangian_line_status() -> ClaimPacket:
    """Return the typed gl(1|1) parity-line obligation."""

    return _open("Y_hbar(gl(1|1)) numerical line curvature", H_SUPER_YANGIAN)


def certified_denominator_factors(c, k) -> Mapping[str, object]:
    """Return factors certified directly by OPE norms and couplings."""

    c_val = _sym(c)
    k_val = _sym(k)
    return {
        "N_Lambda": sp.factor(zamolodchikov_norm_Lambda(c_val)),
        "W3_Lambda_coupling_denominator": 22 + 5 * c_val,
        "BP_central_numerator": sp.factor((2 * k_val + 3) * (3 * k_val + 1)),
        "BP_level_four_factor": 10 * k_val**2 + 11 * k_val - 17,
        "shadow_denominator_exponents": _open(
            "powers contributed by the full inverse Gram matrix and projection graph",
            H_BAR,
            H_PROJ,
        ),
    }


# ---------------------------------------------------------------------------
# Compatibility entry points: historical names now stop at the open boundary
# ---------------------------------------------------------------------------


def _open_shadow(*_args, **_kwargs):
    raise _projection_error("Extended-family")


s3_w3_tline = _open_shadow
s3_w3_wline = _open_shadow
s3_w3_mixed_TWW = _open_shadow
s4_w3_tline = _open_shadow
s4_w3_wline = _open_shadow
s4_w3_mixed_TWW = _open_shadow
s3_bp_tline = _open_shadow
s3_bp_jline = _open_shadow
s3_bp_gline = _open_shadow
s4_bp_tline = _open_shadow
s4_bp_jline = _open_shadow
s4_bp_sigma_invariant = _open_shadow
w_infinity_s3_T = _open_shadow
w_infinity_alpha = _open_shadow
w_infinity_s4_W = _open_shadow
sl11_shadow_S2_bosonic = _open_shadow
sl11_shadow_S2_fermionic = _open_shadow
sl11_shadow_S3_fermionic = _open_shadow
sl11_shadow_S3_parity_flip = _open_shadow
denominator_pattern_w3_wline = _open_shadow
denominator_pattern_bp_tline = _open_shadow
verify_s4_w3_wline_denominator = _open_shadow
verify_bp_sigma_is_polynomial = _open_shadow


def verify_bp_tline_rational_k(k_test_values=None):
    """Compare the two exact routes to the BP T-line inverse norm."""

    values = k_test_values or (-2, -1, 0, 1, 2, 5)
    return {
        _sym(k_val): (
            sp.factor(bp_t_inverse_norm(k_val)),
            sp.factor(bp_t_inverse_norm_factored(k_val)),
        )
        for k_val in values
    }
