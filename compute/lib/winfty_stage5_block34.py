"""Exact stage-5 W_infinity block-(3,4) coefficient check.

The target coefficient is

    C^res_{3,4;5;0,2}(5) = C^DS_{3,4;5;0,2}(5).

In the normalized principal W_5 package the three-point tensor is

    <W3 W4 W5> = (c/5) g345,

and the W5 metric is eta_55 = c/5.  Contracting with eta^55 = 5/c
therefore gives the OPE/residue coefficient g345 on both sides, once
the same strong-generator sign convention for W5 is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Tuple


Channel = Tuple[int, int, int, int]
BLOCK34_CHANNEL: Channel = (3, 4, 5, 2)


@dataclass(frozen=True)
class SignedQuadraticCoefficient:
    """An algebraic coefficient represented by sign times sqrt(square)."""

    sign: int
    square: Fraction

    def __post_init__(self) -> None:
        if self.sign not in (-1, 0, 1):
            raise ValueError(f"sign must be -1, 0, or 1; got {self.sign}")
        if self.square < 0:
            raise ValueError(f"square must be nonnegative; got {self.square}")
        if self.square == 0 and self.sign != 0:
            object.__setattr__(self, "sign", 0)

    def same_as(self, other: "SignedQuadraticCoefficient") -> bool:
        return self.sign == other.sign and self.square == other.square

    def negated(self) -> "SignedQuadraticCoefficient":
        return SignedQuadraticCoefficient(-self.sign, self.square)


def g345_squared(c: Fraction) -> Fraction:
    r"""Return the W_5 bootstrap value of g_{345}^2.

    Blumenhagen--Eholzer--Flohr--Honecker--Hornfeck--Hubel normalization:

        g345^2 = 1680 c^2 (5c+22)(2c-1)
                 / ((c+24)(7c+68)(3c+46)(10c+197)).
    """

    c = Fraction(c)
    denominator = (c + 24) * (7 * c + 68) * (3 * c + 46) * (10 * c + 197)
    if denominator == 0:
        raise ZeroDivisionError("g345 has a pole at this central charge")
    return Fraction(1680) * c * c * (5 * c + 22) * (2 * c - 1) / denominator


def w5_metric(spin: int, c: Fraction) -> Fraction:
    """Normalized visible W_s two-point metric eta_ss = c/s."""

    if spin <= 0:
        raise ValueError(f"spin must be positive; got {spin}")
    c = Fraction(c)
    if c == 0:
        raise ZeroDivisionError("the visible metric is degenerate at c=0")
    return c / spin


def w3_w4_w5_three_point(
    c: Fraction,
    g345: SignedQuadraticCoefficient,
) -> SignedQuadraticCoefficient:
    """The normalized tensor <W3 W4 W5> = (c/5) g345."""

    scale = w5_metric(5, c)
    return SignedQuadraticCoefficient(g345.sign, g345.square * scale * scale)


def residue_block34_coefficient(
    c: Fraction,
    g345_sign: int = 1,
) -> SignedQuadraticCoefficient:
    r"""Compute C^res_{3,4;5;0,2}(5) by metric contraction.

    The collision tensor is <W3 W4 W5> = eta_55 * g345.  The residue/OPE
    coefficient is eta^55 times this tensor, hence exactly g345.
    """

    c = Fraction(c)
    g345 = SignedQuadraticCoefficient(g345_sign, g345_squared(c))
    tensor = w3_w4_w5_three_point(c, g345)
    inverse_metric_square = Fraction(1, 1) / (w5_metric(5, c) ** 2)
    return SignedQuadraticCoefficient(tensor.sign, tensor.square * inverse_metric_square)


def ds_block34_coefficient(
    c: Fraction,
    g345_sign: int = 1,
) -> SignedQuadraticCoefficient:
    r"""Compute C^DS_{3,4;5;0,2}(5) from the principal W_5 OPE."""

    return SignedQuadraticCoefficient(g345_sign, g345_squared(Fraction(c)))


def block34_defect(
    c: Fraction,
    residue_sign: int = 1,
    ds_sign: int = 1,
) -> Dict[str, object]:
    """Return the exact block-(3,4) comparison data at rational c."""

    residue = residue_block34_coefficient(c, residue_sign)
    ds = ds_block34_coefficient(c, ds_sign)
    return {
        "channel": BLOCK34_CHANNEL,
        "central_charge": Fraction(c),
        "g345_squared": g345_squared(Fraction(c)),
        "residue_coefficient": residue,
        "ds_coefficient": ds,
        "same_sign_convention": residue_sign == ds_sign,
        "defect_zero": residue.same_as(ds),
    }


def visible_normal_form_values(
    c: Fraction,
    g345_sign: int = 1,
) -> Dict[Channel, SignedQuadraticCoefficient]:
    """Stage-5 visible normal form forced by the block-(3,4) coefficient.

    Existing manuscript notation writes

        C_{3,4;5;0,2} = -5/4 A_5,
        C_{4,5;3;0,6} = -3/4 A_5.

    Hence A_5 = -4/5 g345 and C_{4,5;3;0,6} = 3/5 g345.
    """

    g345 = ds_block34_coefficient(c, g345_sign)
    return {
        (3, 4, 5, 2): g345,
        (3, 5, 4, 4): SignedQuadraticCoefficient(-g345.sign, g345.square * Fraction(16, 25)),
        (4, 5, 3, 6): SignedQuadraticCoefficient(g345.sign, g345.square * Fraction(9, 25)),
    }
