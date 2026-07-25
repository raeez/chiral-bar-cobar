r"""Exact Neveu--Schwarz mode data for the N=2 superconformal algebra.

This module computes three finite objects:

* the negative-mode Lie superalgebra bracket in the vacuum NS sector;
* the corresponding graded Chevalley--Eilenberg *chain spaces*;
* PBW vacuum-state counts and their charge/parity refinements.

These objects form possible inputs to a PBW spectral sequence.  Chiral bar
cohomology additionally requires the configuration-space residue complex,
its filtration, convergence, and a comparison theorem.  The public boundary
is therefore explicit: cohomology, Koszulness, and modular-conductor requests
raise ``OpenN2BarComparisonError``.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Dict, Iterable, Mapping, Tuple

import sympy as sp


Mode = Tuple[str, Fraction]

PARITY = {"L": 0, "J": 0, "G+": 1, "G-": 1}
CHARGE = {"L": 0, "J": 0, "G+": 1, "G-": -1}
TYPE_ORDER = {"J": 0, "G+": 1, "G-": 2, "L": 3}

H_CE = (
    "H_N2^CE: a fixed continuous Chevalley--Eilenberg convention, a proved "
    "super-sign formula, and convergence of the positive-energy truncations"
)
H_BAR = (
    "H_N2^bar: the ordered Fulton--MacPherson residue complex, completed PBW "
    "filtration, all spectral-sequence differentials, and an E_infinity comparison"
)
H_MOD = (
    "H_N2^mod: a trace-compatible genus-one Kazama--Suzuki curvature comparison"
)


class OpenN2BarComparisonError(RuntimeError):
    """Signals that exact mode data have reached the CE/bar comparison boundary."""


@dataclass(frozen=True)
class ClaimPacket:
    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


def _bar_error(statement: str) -> OpenN2BarComparisonError:
    return OpenN2BarComparisonError(f"{statement} awaits {H_CE} and {H_BAR}.")


def mode_weight_half(mode: Mode) -> int:
    """Return the positive energy in half-integer units."""

    return int(-2 * mode[1])


def mode_parity(mode: Mode) -> int:
    return PARITY[mode[0]]


def mode_charge(mode: Mode) -> int:
    return CHARGE[mode[0]]


def mode_label(mode: Mode) -> str:
    kind, index = mode
    index_text = str(index.numerator) if index.denominator == 1 else str(index)
    return f"{kind}_{index_text}"


def enumerate_creating_modes(max_wh: int) -> Tuple[Mode, ...]:
    """Enumerate vacuum-creating NS modes through energy ``max_wh/2``."""

    modes = []
    for n in range(1, max_wh // 2 + 1):
        modes.append(("J", Fraction(-n)))
    for n in range(2, max_wh // 2 + 1):
        modes.append(("L", Fraction(-n)))
    r = Fraction(3, 2)
    while 2 * r <= max_wh:
        modes.extend((("G+", -r), ("G-", -r)))
        r += 1
    return tuple(
        sorted(modes, key=lambda item: (mode_weight_half(item), TYPE_ORDER[item[0]]))
    )


def bracket(a: Mode, b: Mode, c_val=None) -> Dict[Mode, object]:
    r"""Return the exact negative-mode N=2 Lie superbracket.

    All indices are strictly negative, so the central delta terms vanish.  The
    standard relations are

    ``[L_m,L_n]=(m-n)L_(m+n)``, ``[L_m,J_n]=-nJ_(m+n)``,
    ``[L_m,G_r]=(m/2-r)G_(m+r)``, ``[J_m,G_r^+/-]=+/-G_(m+r)``, and
    ``{G_r^+,G_s^-}=2L_(r+s)+(r-s)J_(r+s)``.
    """

    kind_a, m = a
    kind_b, n = b
    target = m + n
    result: Dict[Mode, object] = {}

    if kind_a == "L" and kind_b == "L":
        coefficient = m - n
        if coefficient:
            result[("L", target)] = coefficient
    elif kind_a == "L" and kind_b == "J":
        if n:
            result[("J", target)] = -n
    elif kind_a == "J" and kind_b == "L":
        if m:
            result[("J", target)] = m
    elif kind_a == "L" and kind_b in ("G+", "G-"):
        coefficient = m / 2 - n
        if coefficient:
            result[(kind_b, target)] = coefficient
    elif kind_a in ("G+", "G-") and kind_b == "L":
        coefficient = -(n / 2 - m)
        if coefficient:
            result[(kind_a, target)] = coefficient
    elif kind_a == "J" and kind_b == "G+":
        result[("G+", target)] = sp.Integer(1)
    elif kind_a == "J" and kind_b == "G-":
        result[("G-", target)] = sp.Integer(-1)
    elif kind_a == "G+" and kind_b == "J":
        result[("G+", target)] = sp.Integer(-1)
    elif kind_a == "G-" and kind_b == "J":
        result[("G-", target)] = sp.Integer(1)
    elif kind_a == "G+" and kind_b == "G-":
        result[("L", target)] = sp.Integer(2)
        coefficient = m - n
        if coefficient:
            result[("J", target)] = coefficient
    elif kind_a == "G-" and kind_b == "G+":
        result[("L", target)] = sp.Integer(2)
        coefficient = n - m
        if coefficient:
            result[("J", target)] = coefficient

    return result


def _linear_outer_bracket(a: Mode, inner: Mapping[Mode, object]) -> Dict[Mode, object]:
    result: Dict[Mode, object] = {}
    for mode, inner_coefficient in inner.items():
        for target, outer_coefficient in bracket(a, mode).items():
            result[target] = sp.simplify(
                result.get(target, 0) + inner_coefficient * outer_coefficient
            )
    return {target: value for target, value in result.items() if value != 0}


def verify_super_jacobi(max_wh: int = 6, c_val=None) -> int:
    """Count violations of the homogeneous super-Jacobi identity."""

    modes = enumerate_creating_modes(max_wh)
    violations = 0
    for x, y, z in product(modes, repeat=3):
        terms = (
            ((-1) ** (mode_parity(x) * mode_parity(z)), _linear_outer_bracket(x, bracket(y, z))),
            ((-1) ** (mode_parity(y) * mode_parity(x)), _linear_outer_bracket(y, bracket(z, x))),
            ((-1) ** (mode_parity(z) * mode_parity(y)), _linear_outer_bracket(z, bracket(x, y))),
        )
        targets = set().union(*(values for _, values in terms))
        if any(
            sp.simplify(sum(sign * values.get(target, 0) for sign, values in terms)) != 0
            for target in targets
        ):
            violations += 1
    return violations


def verify_bracket_relations(c_val=None) -> Mapping[str, bool]:
    """Check a generating packet of exact NS relations."""

    return {
        "G+G-_basic": bracket(("G+", Fraction(-3, 2)), ("G-", Fraction(-3, 2)))
        == {("L", Fraction(-3)): sp.Integer(2)},
        "G+G-_higher": bracket(("G+", Fraction(-3, 2)), ("G-", Fraction(-5, 2)))
        == {("L", Fraction(-4)): sp.Integer(2), ("J", Fraction(-4)): sp.Integer(1)},
        "LG+": bracket(("L", Fraction(-2)), ("G+", Fraction(-3, 2)))
        == {("G+", Fraction(-7, 2)): Fraction(1, 2)},
        "JG+": bracket(("J", Fraction(-1)), ("G+", Fraction(-3, 2)))
        == {("G+", Fraction(-5, 2)): sp.Integer(1)},
        "LJ": bracket(("L", Fraction(-2)), ("J", Fraction(-1)))
        == {("J", Fraction(-3)): sp.Integer(1)},
        "LL": bracket(("L", Fraction(-2)), ("L", Fraction(-3)))
        == {("L", Fraction(-5)): sp.Integer(1)},
    }


def _enumerate_pbw_states(
    modes: Tuple[Mode, ...], target_wh: int, start: int = 0, current: Tuple[Mode, ...] = ()
) -> Iterable[Tuple[Mode, ...]]:
    if target_wh == 0:
        yield current
        return
    for index in range(start, len(modes)):
        mode = modes[index]
        weight = mode_weight_half(mode)
        if weight > target_wh:
            continue
        next_start = index + 1 if mode_parity(mode) else index
        yield from _enumerate_pbw_states(
            modes, target_wh - weight, next_start, current + (mode,)
        )


def enumerate_n2_states(weight_half: int) -> Tuple[Tuple[Mode, ...], ...]:
    """Enumerate PBW monomials in the universal N=2 vacuum module."""

    modes = enumerate_creating_modes(weight_half)
    return tuple(_enumerate_pbw_states(modes, weight_half))


def state_weight_half(state: Tuple[Mode, ...]) -> int:
    return sum(mode_weight_half(mode) for mode in state)


def state_charge(state: Tuple[Mode, ...]) -> int:
    return sum(mode_charge(mode) for mode in state)


def state_parity(state: Tuple[Mode, ...]) -> int:
    return sum(mode_parity(mode) for mode in state) % 2


def state_label(state: Tuple[Mode, ...]) -> str:
    return "1" if len(state) == 0 else " ".join(mode_label(mode) for mode in state)


def n2_weight_space_table(max_wh: int = 12) -> Mapping[int, Mapping[str, object]]:
    """Return PBW vacuum-state dimensions refined by charge and parity."""

    table = {}
    for weight_half in range(max_wh + 1):
        states = enumerate_n2_states(weight_half)
        table[weight_half] = {
            "total": len(states),
            "charges": dict(sorted(Counter(state_charge(state) for state in states).items())),
            "parities": dict(sorted(Counter(state_parity(state) for state in states).items())),
        }
    return table


def vacuum_character_coefficients(max_wh: int = 12) -> Mapping[int, int]:
    r"""Compute the NS vacuum character coefficients by product expansion.

    In half-energy variable ``x=q^(1/2)``, the product is
    ``prod_(n>=1)(1-x^(2n))^-1 prod_(n>=2)(1-x^(2n))^-1
    prod_(r>=3/2)(1+x^(2r))^2``.
    """

    coefficients = [0] * (max_wh + 1)
    coefficients[0] = 1

    def multiply_bosonic(weight: int) -> None:
        for degree in range(weight, max_wh + 1):
            coefficients[degree] += coefficients[degree - weight]

    def multiply_fermionic(weight: int) -> None:
        previous = coefficients[:]
        for degree in range(max_wh + 1):
            value = previous[degree]
            if degree >= weight:
                value += 2 * previous[degree - weight]
            if degree >= 2 * weight:
                value += previous[degree - 2 * weight]
            coefficients[degree] = value

    for n in range(1, max_wh // 2 + 1):
        multiply_bosonic(2 * n)
    for n in range(2, max_wh // 2 + 1):
        multiply_bosonic(2 * n)
    odd_weight = 3
    while odd_weight <= max_wh:
        multiply_fermionic(odd_weight)
        odd_weight += 2
    return {weight: coefficients[weight] for weight in range(max_wh + 1)}


def n1_states(weight_half: int) -> Tuple[Tuple[Mode, ...], ...]:
    """Enumerate PBW states for the N=1 vacuum generator packet ``L,G``."""

    modes = tuple(
        mode for mode in enumerate_creating_modes(weight_half) if mode[0] in ("L", "G+")
    )
    return tuple(_enumerate_pbw_states(modes, weight_half))


def compare_n1_n2(max_wh: int = 12) -> Mapping[int, Mapping[str, int]]:
    return {
        weight: {"N1": len(n1_states(weight)), "N2": len(enumerate_n2_states(weight))}
        for weight in range(max_wh + 1)
    }


class SuperCEComplex:
    """Finite graded CE chain-space presentation of the negative-mode algebra."""

    def __init__(self, max_weight_half: int, c_val=None):
        self.max_wh = max_weight_half
        self.c_val = c_val
        self.modes = enumerate_creating_modes(max_weight_half)

    def weight_basis(self, degree: int, weight_half: int) -> Tuple[Tuple[int, ...], ...]:
        result = []

        def generate(remaining_degree: int, remaining_weight: int, start: int, current):
            if remaining_degree == 0:
                if remaining_weight == 0:
                    result.append(tuple(current))
                return
            for index in range(start, len(self.modes)):
                mode = self.modes[index]
                weight = mode_weight_half(mode)
                if weight > remaining_weight:
                    continue
                # CE parity shift: even Lie generators are exterior; odd are symmetric.
                next_start = index if mode_parity(mode) else index + 1
                generate(
                    remaining_degree - 1,
                    remaining_weight - weight,
                    next_start,
                    current + [index],
                )

        generate(degree, weight_half, 0, [])
        return tuple(result)

    def chain_dim(self, degree: int, weight_half: int) -> int:
        return len(self.weight_basis(degree, weight_half))

    def ce_differential(self, degree: int, weight_half: int):
        raise _bar_error("The continuous super-CE differential")

    def cohomology_dim(self, degree: int, weight_half: int):
        raise _bar_error("The truncated CE cohomology")

    def cohomology_by_charge(self, degree: int, weight_half: int):
        raise _bar_error("The charge-refined CE cohomology")

    def verify_d_squared(self, degree: int, weight_half: int):
        raise _bar_error("The differential-square check")


def verify_d_squared_all(max_wh: int = 10, c_val=None):
    raise _bar_error("The differential-square check")


def spectral_flow_weight_shift(eta, charge, c_val):
    r"""Return ``eta*q+c*eta^2/6`` in the standard spectral-flow convention."""

    return sp.simplify(_as_rational(eta) * _as_rational(charge) + _as_rational(c_val) * _as_rational(eta) ** 2 / 6)


def spectral_flow_packet(eta, h, charge, c_val) -> Mapping[str, object]:
    eta_val = _as_rational(eta)
    charge_val = _as_rational(charge)
    c_value = _as_rational(c_val)
    return {
        "h": sp.simplify(_as_rational(h) + eta_val * charge_val + c_value * eta_val**2 / 6),
        "q": sp.simplify(charge_val + c_value * eta_val / 3),
        "status": "exact N=2 spectral-flow arithmetic",
    }


def _as_rational(value):
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.sympify(value)


def kappa_n2(c_val=None):
    raise OpenN2BarComparisonError(f"N=2 modular kappa awaits {H_MOD}.")


def compute_master(max_wh: int = 12, c_val=None, verbose: bool = False):
    """Return the exact finite mode/PBW packet and typed frontier claims."""

    packet = {
        "bracket_checks": verify_bracket_relations(c_val),
        "super_jacobi_violations": verify_super_jacobi(max_wh, c_val),
        "pbw_weight_spaces": n2_weight_space_table(max_wh),
        "vacuum_character": vacuum_character_coefficients(max_wh),
        "ce_cohomology": _open("continuous N=2 negative-mode CE cohomology", H_CE),
        "chiral_bar": _open("N=2 ordered chiral bar cohomology", H_BAR),
        "koszulness": _open("N=2 chiral Koszulness", H_CE, H_BAR),
        "modular_kappa": _open("N=2 modular kappa", H_MOD),
    }
    if verbose:
        print(packet)
    return packet
