r"""Exact central-charge diagnostics for the Bershadsky--Polyakov algebra.

The standard conformal vector is the one used by
Fehily--Kawasetsu--Ridout, CMP 385 (2021), Definition 2.1 and Eq. (2.2):

    c_BP(k) = -(2k+3)(3k+1)/(k+3)
            = 25 - 6(k+3) - 24/(k+3).

The level involution ``k -> -k-6`` sends ``t=k+3`` to ``-t`` and gives
the exact rational-function identity

    c_BP(k) + c_BP(-k-6) = 50.

The same source defines BP as an ordinary (bosonic) vertex algebra.  Its
strong generators ``J, G^+, G^-, T`` are therefore even.  The old
manuscript computation assigned odd parity to ``G^+`` and ``G^-`` and
used the signed reciprocal-weight sum

    1 - 2/3 - 2/3 + 1/2 = 1/6.

With the source-correct parities that expression evaluates instead to
``17/6``.  More importantly, the principal-W reciprocal-exponent formula
has no theorem extending it to this non-principal reduction.  The modular
characteristic ``kappa_BP`` and its companion sum consequently remain open
until an actual genus-one curvature calculation is supplied.

The secondary rational function ``2 - 24(k+1)^2/(k+3)`` remains available
under the explicit name ``c_BP_shifted``; its sum is ``196``.  It has a
separate convention record and never replaces the standard Eq. (2.2)
conformal vector.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Optional, Union


Level = Union[int, Fraction]


class UnverifiedBPInvariantError(RuntimeError):
    """Raised when code requests the open BP genus-one invariant as a number."""


@dataclass(frozen=True)
class BPConformalConvention:
    """A named central-charge normalization and its verified scalar sum."""

    name: str
    formula: str
    conductor: Fraction
    status: str
    source: str


@dataclass(frozen=True)
class BPGenusOneStatus:
    """Epistemic record for the manuscript-specific BP modular characteristic."""

    status: str
    source_fact: str
    invalidated_derivation: str
    resolution_obligation: str


STANDARD_BP_CONVENTION = BPConformalConvention(
    name="standard_fkr_equal_weight_G",
    formula="-(2*k + 3)*(3*k + 1)/(k + 3)",
    conductor=Fraction(50),
    status="proved-primary-source",
    source="Fehily--Kawasetsu--Ridout 2021, Definition 2.1 and Eq. (2.2)",
)

SHIFTED_BP_CONVENTION = BPConformalConvention(
    name="explicit_shifted_formula",
    formula="2 - 24*(k + 1)**2/(k + 3)",
    conductor=Fraction(196),
    status="computed-secondary",
    source="explicit rational function retained for convention separation",
)

BP_CONVENTIONS: Mapping[str, BPConformalConvention] = {
    "standard": STANDARD_BP_CONVENTION,
    "shifted": SHIFTED_BP_CONVENTION,
}

BP_KAPPA_STATUS = BPGenusOneStatus(
    status="open-genus-one-computation",
    source_fact="BP is bosonic; J, G+, G-, T are even strong generators",
    invalidated_derivation="the odd-parity signed sum yielding 1/6",
    resolution_obligation=(
        "compute the full genus-one curvature from the BP chiral/BRST complex, "
        "including charged ghosts, neutral fields, improvement, and mixed channels"
    ),
)

# Exact central-charge constants.
K_BP_EXACT = STANDARD_BP_CONVENTION.conductor
K_BP_SHIFTED_EXACT = SHIFTED_BP_CONVENTION.conductor

# Compatibility names intentionally carry no numeric value.  Their former
# values depended on the invalid odd-parity assignment.
VARRHO_BP: Optional[Fraction] = None
KAPPA_COMPLEMENTARITY_EXACT: Optional[Fraction] = None


# Strong generators: name -> (conformal weight, parity), parity 0 = even.
BP_GENERATORS = {
    "J": (Fraction(1), 0),
    "G+": (Fraction(3, 2), 0),
    "G-": (Fraction(3, 2), 0),
    "T": (Fraction(2), 0),
}


def _regular_level(k: Level) -> Fraction:
    """Return ``k`` as a fraction and enforce the common pole at ``k=-3``."""

    level = Fraction(k)
    if level == Fraction(-3):
        raise ZeroDivisionError(
            "BP central charge has its critical pole at k = -3"
        )
    return level


def c_BP(k: Level) -> Fraction:
    r"""Standard BP central charge from FKR21, Eq. (2.2)."""

    level = _regular_level(k)
    return -(
        (Fraction(2) * level + 3) * (Fraction(3) * level + 1)
    ) / (level + 3)


def c_BP_shifted(k: Level) -> Fraction:
    r"""Secondary shifted rational function with computed sum ``196``."""

    level = _regular_level(k)
    return Fraction(2) - Fraction(24) * (level + 1) ** 2 / (level + 3)


def dual_level(k: Level) -> Fraction:
    r"""Return the involutive companion level ``-k-6``."""

    return -Fraction(k) - Fraction(6)


def K_BP(k: Level) -> Fraction:
    r"""Exact standard companion sum ``c_BP(k)+c_BP(-k-6)=50``."""

    level = Fraction(k)
    return c_BP(level) + c_BP(dual_level(level))


def K_BP_shifted(k: Level) -> Fraction:
    r"""Companion sum of the explicitly named shifted rational function."""

    level = Fraction(k)
    return c_BP_shifted(level) + c_BP_shifted(dual_level(level))


def compute_varrho() -> Fraction:
    r"""Return the source-correct reciprocal-weight diagnostic ``17/6``.

    This diagnostic is not a theorem computing the BP anomaly ratio.  It
    records exactly what the former signed-generator expression becomes after
    correcting the parities.
    """

    return sum(
        (Fraction(-1) if parity else Fraction(1)) / weight
        for weight, parity in BP_GENERATORS.values()
    )


def kappa_BP(k: Level) -> Fraction:
    r"""Signal the open BP genus-one curvature computation."""

    _regular_level(k)
    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def kappa_complementarity(k: Level) -> Fraction:
    r"""Signal the open BP modular-characteristic companion sum."""

    _regular_level(k)
    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def self_dual_level() -> Fraction:
    r"""Return the unique fixed point ``k=-3`` of ``k -> -k-6``."""

    return Fraction(-3)


def verify_all(k_values: Iterable[Level]) -> bool:
    r"""Verify every certified central-charge identity at regular samples."""

    for value in k_values:
        level = Fraction(value)
        if level == self_dual_level():
            continue
        companion = dual_level(level)
        assert dual_level(companion) == level
        assert K_BP(level) == K_BP_EXACT
        assert c_BP(level) + c_BP(companion) == K_BP_EXACT
        assert K_BP_shifted(level) == K_BP_SHIFTED_EXACT

    assert dual_level(self_dual_level()) == self_dual_level()
    assert compute_varrho() == Fraction(17, 6)
    assert K_BP_EXACT == Fraction(50)
    assert K_BP_SHIFTED_EXACT == Fraction(196)
    assert VARRHO_BP is None
    assert KAPPA_COMPLEMENTARITY_EXACT is None
    return True


def summary(k: Level) -> Dict[str, object]:
    r"""Return the standard central packet and the open genus-one status."""

    level = Fraction(k)
    companion = dual_level(level)
    return {
        "k": level,
        "k_dual": companion,
        "c_BP(k)": c_BP(level),
        "c_BP(k_dual)": c_BP(companion),
        "K_BP": K_BP(level),
        "strong_generator_parities": tuple(
            (name, parity) for name, (_weight, parity) in BP_GENERATORS.items()
        ),
        "reciprocal_weight_diagnostic": compute_varrho(),
        "kappa_status": BP_KAPPA_STATUS.status,
        "kappa_BP(k)": None,
        "kappa_complementarity": None,
    }


def main() -> None:
    """Print exact central-charge certificates and the open obligation."""

    test_levels = [0, 1, -1, 2, -2, 5, 10, -4]
    print("BP primary-source normalization diagnostics")
    print("=" * 60)
    for test_level in test_levels:
        print(f"\nk = {test_level}:")
        for key, value in summary(test_level).items():
            print(f"  {key} = {value}")
    print("\n" + "=" * 60)
    print(f"Verification: {verify_all(test_levels)}")
    print(f"K_BP = {K_BP_EXACT}")
    print(f"kappa status = {BP_KAPPA_STATUS.status}")
    print(f"shifted-formula conductor = {K_BP_SHIFTED_EXACT}")


if __name__ == "__main__":
    main()
