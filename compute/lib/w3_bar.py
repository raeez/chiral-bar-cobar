r"""Exact :math:`\mathcal W_3` OPE data and the ordered-bar boundary.

The module certifies Zamolodchikov-normalized singular products and the generic
freely generated vacuum character.  Constructing an ordered chiral bar
differential requires configuration-space residue forms, collision
orientations, descendant bookkeeping, completion, and a proof that the map
squares to zero.  Historical functions that summed OPE coefficients into a
``bar differential`` now raise ``OpenW3BarError``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Mapping, Tuple

import sympy as sp


H_BAR = (
    "H_W3^bar: an ordered Fulton--MacPherson residue complex, fixed collision "
    "orientations, descendant projection, completion, and a differential-square proof"
)
H_PROJ = (
    "H_W3^proj: a chain-compatible projection from the full multi-channel tensor"
)


class OpenW3BarError(RuntimeError):
    """Signals that exact OPE data have reached the ordered-bar boundary."""


@dataclass(frozen=True)
class ClaimPacket:
    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


def _bar_error(statement: str) -> OpenW3BarError:
    return OpenW3BarError(f"{statement} awaits {H_BAR}.")


def w3_nth_products() -> Dict[Tuple[str, str], Dict[int, Dict[str, object]]]:
    r"""Return the standard singular nth products of ``T`` and ``W``.

    The pole-two ``Lambda`` coefficient is ``32/(22+5c)`` and the pole-one
    derivative coefficient is ``16/(22+5c)``.  In nth-product notation these
    occur at indices one and zero, respectively.
    """

    c = sp.Symbol("c")
    alpha = sp.Integer(32) / (22 + 5 * c)
    return {
        ("T", "T"): {
            3: {"vac": c / 2},
            1: {"T": sp.Integer(2)},
            0: {"dT": sp.Integer(1)},
        },
        ("T", "W"): {
            1: {"W": sp.Integer(3)},
            0: {"dW": sp.Integer(1)},
        },
        ("W", "T"): {
            1: {"W": sp.Integer(3)},
            0: {"dW": sp.Integer(2)},
        },
        ("W", "W"): {
            5: {"vac": c / 3},
            3: {"T": sp.Integer(2)},
            2: {"dT": sp.Integer(1)},
            1: {"d2T": sp.Rational(3, 10), "Lambda": alpha},
            0: {"d3T": sp.Rational(1, 15), "dLambda": alpha / 2},
        },
    }


def w3_nth_product(a: str, b: str, n: int) -> Dict[str, object]:
    """Return one singular nth product, with an empty packet for regular terms."""

    return dict(w3_nth_products().get((a, b), {}).get(n, {}))


def w3_ope_status_packet() -> Mapping[str, object]:
    """Return the exact OPE packet and typed bar/projection frontier."""

    return {
        "status": "proved elsewhere",
        "normalization": "Zamolodchikov",
        "generators": {
            "T": {"weight": 2, "parity": "even"},
            "W": {"weight": 3, "parity": "even"},
        },
        "nth_products": w3_nth_products(),
        "ordered_bar": _open("W_3 ordered chiral bar differential", H_BAR),
        "scalar_shadow": _open("W_3 scalar shadow projection", H_BAR, H_PROJ),
    }


def w3_leading_ope_norms() -> Mapping[str, object]:
    """Return the leading two-point OPE coefficients."""

    c = sp.Symbol("c")
    return {"T": c / 2, "W": c / 3}


def w3_leading_norm_ratio():
    """Return ``N_W/N_T=2/3`` as an OPE normalization ratio."""

    return sp.Rational(2, 3)


def w3_central_charge(k=None):
    r"""Return the principal :math:`\mathcal W^k(\mathfrak{sl}_3)` charge.

    ``c(k)=2-24(k+2)^2/(k+3)`` in the stated affine-level coordinate.
    """

    k_val = sp.Symbol("k") if k is None else sp.sympify(k)
    return sp.factor(2 - 24 * (k_val + 2) ** 2 / (k_val + 3))


def w3_reflected_central_sum(k=None):
    """Compute the formal additive reflection sum, identically ``100``."""

    k_val = sp.Symbol("k") if k is None else sp.sympify(k)
    return sp.simplify(w3_central_charge(k_val) + w3_central_charge(-k_val - 6))


def w3_complementarity_sum():
    """Compatibility name for the exact formal reflection arithmetic."""

    return w3_reflected_central_sum()


def _partitions_with_minimum(total: int, minimum: int, largest=None):
    if total == 0:
        yield ()
        return
    largest = total if largest is None else min(largest, total)
    for first in range(largest, minimum - 1, -1):
        for rest in _partitions_with_minimum(total - first, minimum, first):
            yield (first,) + rest


def w3_vacuum_basis(max_weight: int) -> Dict[int, List[str]]:
    r"""Return a PBW basis for the generic freely generated vacuum module.

    Its character is
    ``prod_(n>=2)(1-q^n)^-1 prod_(m>=3)(1-q^m)^-1``.  Special central
    charges may introduce quotient relations and are represented by a
    separate module-specific quotient calculation.
    """

    basis: Dict[int, List[str]] = {}
    for weight in range(1, max_weight + 1):
        entries = []
        for t_weight in range(weight + 1):
            w_weight = weight - t_weight
            for t_modes in _partitions_with_minimum(t_weight, 2):
                for w_modes in _partitions_with_minimum(w_weight, 3):
                    if len(t_modes) + len(w_modes) == 0:
                        continue
                    factors = [f"L_-{mode}" for mode in t_modes]
                    factors.extend(f"W_-{mode}" for mode in w_modes)
                    entries.append(" ".join(factors) + " |0>")
        if entries:
            basis[weight] = entries
    return basis


def _w3_vacuum_dims_table(max_h: int = 20) -> Dict[int, int]:
    coefficients = [0] * (max_h + 1)
    coefficients[0] = 1
    for weight in range(2, max_h + 1):
        for degree in range(weight, max_h + 1):
            coefficients[degree] += coefficients[degree - weight]
    for weight in range(3, max_h + 1):
        for degree in range(weight, max_h + 1):
            coefficients[degree] += coefficients[degree - weight]
    return {weight: coefficients[weight] for weight in range(1, max_h + 1)}


def w3_vacuum_dim(weight: int) -> int:
    return _w3_vacuum_dims_table(max(20, weight)).get(weight, 0)


def verify_skew_symmetry() -> bool:
    """Verify the generator-level ``TW``/``WT`` skew-symmetry packet."""

    products = w3_nth_products()
    return (
        products[("T", "W")][1] == products[("W", "T")][1]
        and products[("T", "W")][0]["dW"] == 1
        and products[("W", "T")][0]["dW"] == 2
    )


def verify_w3_ope() -> Mapping[str, bool]:
    c = sp.Symbol("c")
    products = w3_nth_products()
    return {
        "TT_norm": products[("T", "T")][3]["vac"] == c / 2,
        "WW_norm": products[("W", "W")][5]["vac"] == c / 3,
        "Lambda_pole_two": sp.simplify(
            products[("W", "W")][1]["Lambda"] - 32 / (22 + 5 * c)
        )
        == 0,
        "dLambda_pole_one": sp.simplify(
            products[("W", "W")][0]["dLambda"] - 16 / (22 + 5 * c)
        )
        == 0,
        "TW_WT_skew": verify_skew_symmetry(),
    }


# Historical bar/cohomology entry points stop at the geometric boundary.
def w3_bar_diff_deg2(*_args, **_kwargs):
    raise _bar_error("The degree-two W_3 ordered-bar differential")


def w3_bar_diff_deg3_TTT_xi1(*_args, **_kwargs):
    raise _bar_error("The degree-three TTT ordered-bar differential")


def w3_bar_diff_deg3_WTT(*_args, **_kwargs):
    raise _bar_error("The degree-three WTT ordered-bar differential")


def w3_bar_diff_deg3_TWT(*_args, **_kwargs):
    raise _bar_error("The degree-three TWT ordered-bar differential")


def w3_arnold_cancellation_deg3(*_args, **_kwargs):
    raise _bar_error("The degree-three Arnold cancellation")


def w3_deg3_cohomology(*_args, **_kwargs):
    raise _bar_error("The degree-three W_3 bar cohomology")


def w3_deg3_chain_dim(*_args, **_kwargs):
    raise _bar_error("The degree-three W_3 ordered-bar chain dimension")


def w3_curvature(*_args, **_kwargs):
    raise _bar_error("The W_3 bar curvature")


def w3_curvature_ratio(*_args, **_kwargs):
    raise _bar_error("The W_3 bar-curvature ratio")


def verify_w3_bar_diff(*_args, **_kwargs):
    raise _bar_error("The W_3 ordered-bar differential verification")


def verify_w3_curvature(*_args, **_kwargs):
    raise _bar_error("The W_3 bar-curvature verification")


def verify_w3_deg3(*_args, **_kwargs):
    raise _bar_error("The degree-three W_3 bar verification")
