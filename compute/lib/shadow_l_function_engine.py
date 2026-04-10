r"""shadow_l_function_engine.py

Eisenstein-model special values of the shadow L-function for the standard
Volume I families.

This module is intentionally narrower than
``compute.lib.shadow_eisenstein_correct_engine``:

- ``shadow_eisenstein_correct_engine.py`` shows that the coefficient Dirichlet
  series ``sum_{r >= 2} S_r(A) r^{-s}`` is not globally equal to
  ``-kappa(A) * zeta(s) * zeta(s-1)``.
- The present engine therefore does not implement that falsified global
  identity.
- What it does implement is the special-value package requested for the
  compute layer:
  1. the genus points ``s = 1 - 2g`` with ``g = 1, 2, 3``;
  2. the Eisenstein-model poles at ``s = 1`` and ``s = 2``;
  3. exact ``kappa`` values for the standard families;
  4. AP32 scope tags on every ``g >= 2`` value.

Pole structure (AP70)
---------------------
L^sh(s, A) has exactly two poles in the Eisenstein model:

- ``s = 1``: simple pole, residue = ``kappa / 2``.
- ``s = 2``: simple pole, residue = ``-kappa * pi^2 / 6``.

Negative odd integers ``s = 1 - 2g`` for ``g >= 1`` are regular points.
The trivial zeros of the Riemann zeta factors do NOT produce zeros at
these points because the product ``zeta(s) * zeta(s-1)`` compensates.
The genus free-energy coefficients ``F_g = L^sh(1-2g)`` are read off at
these regular points.

Canonical genus normalization in the live repo:

    F_1(A) = kappa(A) / 24
    F_g(A) = kappa(A) * lambda_g^FP   for g >= 2

with the Faber-Pandharipande Bernoulli numbers

    lambda_g^FP = ((2^(2g-1) - 1) / 2^(2g-1)) * |B_{2g}| / (2g)!.

Hence

    lambda_1^FP = 1/24
    lambda_2^FP = 7/5760
    lambda_3^FP = 31/967680.

These are the canonical Volume I free-energy coefficients. They use Bernoulli
numbers, but they are not the incompatible bare normalization
``B_{2g} / (2g(2g-2))``.

Family conventions match the live source:

- Heisenberg ``H_k``: ``kappa = k``
- Virasoro ``Vir_c``: ``kappa = c/2``
- affine ``sl_2`` at level ``k``: ``kappa = 3(k+2)/4``
- principal ``W_3``: ``kappa = 5c/6``
- betagamma at weight ``lambda``: ``kappa = 6 lambda^2 - 6 lambda + 1``
- ``bc`` at weight ``lambda``: ``kappa = -(6 lambda^2 - 6 lambda + 1)``
- free fermion (= ``bc`` at ``lambda = 1/2``): ``c = 1``, ``kappa = 1/2``
"""

from __future__ import annotations

import math
from dataclasses import dataclass, replace
from fractions import Fraction
from typing import Mapping, Optional, Sequence

try:
    import mpmath

    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:  # pragma: no cover - exercised only when mpmath is absent
    mpmath = None
    HAS_MPMATH = False


SUPPORTED_POLES = (1, 2)
SCOPE_ALL_WEIGHT_G1 = "ALL-WEIGHT (g=1)"
SCOPE_UNIFORM_WEIGHT = "UNIFORM-WEIGHT"
SCOPE_UNIFORM_WEIGHT_PROJECTION = "UNIFORM-WEIGHT PROJECTION ONLY"


@dataclass(frozen=True)
class ShadowFamily:
    """Standard-family input data for the special-value engine."""

    key: str
    display_name: str
    parameters: Mapping[str, Fraction]
    kappa: Fraction
    shadow_class: str
    uniform_weight: bool
    family_note: str


@dataclass(frozen=True)
class ShadowLEvaluation:
    """Evaluation datum for one family at one special point."""

    family_key: str
    display_name: str
    s: int
    kappa: Fraction
    kind: str
    genus: Optional[int]
    value_exact: Optional[Fraction]
    value_numeric: Optional[str]
    pole_order: Optional[int]
    residue_exact: Optional[Fraction]
    residue_formula: Optional[str]
    residue_numeric: Optional[str]
    scope_tag: str
    connection_note: str


def _frac(value: Fraction | int) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def _fraction_to_mpf(value: Fraction):
    if not HAS_MPMATH:
        return None
    return mpmath.mpf(value.numerator) / value.denominator


def _numeric_string(value, digits: int = 18) -> Optional[str]:
    if not HAS_MPMATH:
        return None
    return mpmath.nstr(value, n=digits)


def bernoulli_number(n: int) -> Fraction:
    """Bernoulli number ``B_n`` with the Volume I sign convention ``B_1 = -1/2``."""

    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return Fraction(1)

    values = [Fraction(0)] * (n + 1)
    values[0] = Fraction(1)
    for m in range(1, n + 1):
        total = Fraction(0)
        for j in range(m):
            total += Fraction(math.comb(m + 1, j)) * values[j]
        values[m] = -total / Fraction(m + 1)
    return values[n]


def faber_pandharipande_lambda(g: int) -> Fraction:
    """Return ``lambda_g^FP`` in exact rational arithmetic."""

    if g < 1:
        raise ValueError("g must be >= 1")
    if g == 1:
        return Fraction(1, 24)

    bernoulli_abs = abs(bernoulli_number(2 * g))
    prefactor = Fraction(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
    return prefactor * bernoulli_abs / Fraction(math.factorial(2 * g))


def genus_free_energy(kappa: Fraction | int, g: int) -> Fraction:
    """Canonical Volume I free energy ``F_g = kappa * lambda_g^FP``."""

    return _frac(kappa) * faber_pandharipande_lambda(g)


# ========================================================================
# Family constructors
# ========================================================================


def heisenberg_family(k: Fraction | int = Fraction(1)) -> ShadowFamily:
    # AP1: kappa(Heis) = k. Census: landscape_census.tex, C1.
    # k=0 -> kappa=0. k=1 -> kappa=1.
    level = _frac(k)
    return ShadowFamily(
        key=f"Heis(k={level})",
        display_name="Heisenberg",
        parameters={"k": level},
        kappa=level,
        shadow_class="G",
        uniform_weight=True,
        family_note="Single-generator uniform-weight family.",
    )


def virasoro_family(c: Fraction | int = Fraction(26)) -> ShadowFamily:
    # AP1: kappa(Vir) = c/2. Census: landscape_census.tex, C2.
    # c=0 -> kappa=0. c=13 -> kappa=13/2 (self-dual). c=26 -> kappa=13.
    central_charge = _frac(c)
    return ShadowFamily(
        key=f"Vir(c={central_charge})",
        display_name="Virasoro",
        parameters={"c": central_charge},
        kappa=central_charge / 2,
        shadow_class="M",
        uniform_weight=True,
        family_note="Single-generator uniform-weight family.",
    )


def virasoro_self_dual_family() -> ShadowFamily:
    return virasoro_family(Fraction(13))


def affine_sl2_family(k: Fraction | int = Fraction(1)) -> ShadowFamily:
    # AP1: kappa(KM) = dim(g)*(k+h^v)/(2*h^v). For sl_2: dim=3, h^v=2.
    # Census: landscape_census.tex, C3.
    # k=0 -> kappa=3*2/4=3/2 (NOT zero). k=-2 -> kappa=0 (critical).
    level = _frac(k)
    return ShadowFamily(
        key=f"sl2_aff(k={level})",
        display_name="affine sl_2",
        parameters={"k": level},
        kappa=Fraction(3) * (level + 2) / 4,
        shadow_class="L",
        uniform_weight=True,
        family_note="Affine currents all have conformal weight 1.",
    )


def principal_w3_family(c: Fraction | int = Fraction(2)) -> ShadowFamily:
    # AP1: kappa(W_N) = c*(H_N - 1). For W_3: H_3 = 1+1/2+1/3 = 11/6,
    # so H_3 - 1 = 5/6, kappa = 5c/6. Census: landscape_census.tex, C4.
    # N=2 check: H_2-1 = 1/2 so kappa(W_2) = c/2 = kappa(Vir). Correct.
    central_charge = _frac(c)
    return ShadowFamily(
        key=f"W3(c={central_charge})",
        display_name="principal W_3",
        parameters={"c": central_charge},
        kappa=Fraction(5, 6) * central_charge,
        shadow_class="M",
        uniform_weight=False,
        family_note=(
            "Multi-weight family: T has weight 2 and W has weight 3. "
            "For g >= 2 the scalar-lane value is only the uniform-weight "
            "projection; the full family needs delta_F_g^cross."
        ),
    )


def betagamma_family(lam: Fraction | int = Fraction(1, 2)) -> ShadowFamily:
    # AP1/C6: c_bg(lambda) = 2(6*lambda^2 - 6*lambda + 1).
    # kappa_bg = 6*lambda^2 - 6*lambda + 1.
    # Census: shadow_metric_census.py::kappa_betagamma.
    # lambda=1/2: kappa=-1/2. lambda=1: kappa=1. lambda=0: kappa=1.
    weight = _frac(lam)
    kappa = 6 * weight * weight - 6 * weight + 1
    uniform_weight = weight == Fraction(1, 2)
    note = (
        "Uniform-weight symplectic boson pair at lambda = 1/2."
        if uniform_weight
        else "Outside the uniform-weight lane unless lambda = 1/2."
    )
    return ShadowFamily(
        key=f"betagamma(lambda={weight})",
        display_name="betagamma",
        parameters={"lambda": weight},
        kappa=kappa,
        shadow_class="C",
        uniform_weight=uniform_weight,
        family_note=note,
    )


def bc_family(lam: Fraction | int = Fraction(1, 2)) -> ShadowFamily:
    # AP1/C5: c_bc(lambda) = 1 - 3(2*lambda - 1)^2.
    # kappa_bc = -(6*lambda^2 - 6*lambda + 1) = -kappa_bg.
    # Census: shadow_metric_census.py::kappa_bc.
    # lambda=1/2: kappa=1/2, c=1. lambda=2: kappa=-(24-12+1)=-13, c=-26.
    weight = _frac(lam)
    kappa = -(6 * weight * weight - 6 * weight + 1)
    uniform_weight = weight == Fraction(1, 2)
    note = (
        "Two-generator bc system at lambda = 1/2 with c = 1, kappa = 1/2."
        if uniform_weight
        else "Outside the uniform-weight lane unless lambda = 1/2."
    )
    return ShadowFamily(
        key=f"bc(lambda={weight})",
        display_name="bc",
        parameters={"lambda": weight},
        kappa=kappa,
        shadow_class="C",
        uniform_weight=uniform_weight,
        family_note=note,
    )


def free_fermion_family() -> ShadowFamily:
    """The free fermion = bc system at lambda = 1/2.

    Two generators b (weight 1/2) and c (weight 1/2).
    Central charge c_bc(1/2) = 1 - 3(0)^2 = 1.
    kappa = -(6*(1/4) - 3 + 1) = -(3/2 - 3 + 1) = -(-1/2) = 1/2.

    This is the standard "free fermion" of the task specification.
    It is NOT the single real fermion psi with c = 1/2, kappa = 1/4
    (that one-generator object is in the shadow_metric_census as
    FreeFermion with kappa = 1/4).
    """
    family = bc_family(Fraction(1, 2))
    return replace(
        family,
        key="free_fermion(bc,lambda=1/2)",
        display_name="free fermion (bc)",
        family_note=(
            "Free fermion = bc system at lambda = 1/2. "
            "c = 1, kappa = 1/2. Two generators b, c each of weight 1/2."
        ),
    )


def all_standard_families() -> Sequence[ShadowFamily]:
    """Default family list: the original six with Vir at c = 26."""

    return (
        heisenberg_family(),
        virasoro_family(),
        affine_sl2_family(),
        principal_w3_family(),
        betagamma_family(),
        bc_family(),
    )


def task_families() -> Sequence[ShadowFamily]:
    """The six families requested in the shadow L-function evaluation task.

    Heis(k=1), Vir(c=1), sl_2(k=1), W_3(c=2), betagamma(lambda=1),
    free fermion (= bc at lambda=1/2).
    """
    return (
        heisenberg_family(Fraction(1)),
        virasoro_family(Fraction(1)),
        affine_sl2_family(Fraction(1)),
        principal_w3_family(Fraction(2)),
        betagamma_family(Fraction(1)),
        free_fermion_family(),
    )


def with_kappa(family: ShadowFamily, kappa: Fraction | int) -> ShadowFamily:
    """Return a copy of ``family`` with a replaced ``kappa`` value."""

    return replace(family, kappa=_frac(kappa))


# ========================================================================
# Pole data
# ========================================================================


def pole_info(family: ShadowFamily) -> dict:
    """Return pole data for L^sh(s, A) in the Eisenstein model.

    AP70: L^sh has poles at s = 1 and s = 2.
    Negative integers are trivial zeros of zeta(s), but the product
    zeta(s)*zeta(s-1) compensates at the genus points s = 1-2g.

    Returns
    -------
    dict with keys:
        poles : list of dicts, each with 's', 'order', 'residue_exact',
                'residue_formula', 'residue_numeric'.
    """
    poles = []
    # s = 1: simple pole, residue = kappa/2
    res1 = pole_residue_at_one(family.kappa)
    poles.append({
        "s": 1,
        "order": 1,
        "residue_exact": res1,
        "residue_formula": "kappa/2",
        "residue_numeric": _numeric_string(_fraction_to_mpf(res1))
            if HAS_MPMATH else None,
    })
    # s = 2: simple pole, residue = -kappa*pi^2/6
    res2 = pole_residue_at_two(family.kappa)
    poles.append({
        "s": 2,
        "order": 1,
        "residue_exact": None,  # irrational (involves pi^2)
        "residue_formula": "-kappa*pi^2/6",
        "residue_numeric": _numeric_string(res2) if HAS_MPMATH else None,
    })
    return {"poles": poles}


def pole_residue_at_one(kappa: Fraction | int) -> Fraction:
    """Simple-pole residue at ``s = 1``: ``kappa / 2``."""

    return _frac(kappa) / 2


def pole_residue_at_two(kappa: Fraction | int):
    """Simple-pole residue at ``s = 2``: ``-kappa * pi^2 / 6``."""

    if not HAS_MPMATH:
        return None
    kappa_mpf = _fraction_to_mpf(_frac(kappa))
    return -kappa_mpf * (mpmath.pi ** 2) / 6


# ========================================================================
# Scope and connection metadata
# ========================================================================


def _scope_tag(family: ShadowFamily, g: int) -> str:
    if g == 1:
        return SCOPE_ALL_WEIGHT_G1
    if family.uniform_weight:
        return SCOPE_UNIFORM_WEIGHT
    return SCOPE_UNIFORM_WEIGHT_PROJECTION


def _connection_note(family: ShadowFamily, g: int) -> str:
    if g == 1:
        return "Genus-1 identification is unconditional for all standard families."
    if family.uniform_weight:
        return (
            "This family lies on the uniform-weight lane, so the scalar-lane "
            "value equals the genus-g free energy."
        )
    return (
        "This family is multi-weight. The returned value is the scalar-lane "
        "projection kappa * lambda_g^FP; the full genus-g free energy requires "
        "the cross-channel correction delta_F_g^cross."
    )


# ========================================================================
# Main evaluation API
# ========================================================================


def shadow_l_at_s(family: ShadowFamily, s: int) -> ShadowLEvaluation:
    """Evaluate the special-value package at a genus point or pole."""

    if s in SUPPORTED_POLES:
        if s == 1:
            residue = pole_residue_at_one(family.kappa)
            return ShadowLEvaluation(
                family_key=family.key,
                display_name=family.display_name,
                s=s,
                kappa=family.kappa,
                kind="pole",
                genus=None,
                value_exact=None,
                value_numeric=None,
                pole_order=1,
                residue_exact=residue,
                residue_formula="kappa/2",
                residue_numeric=_numeric_string(_fraction_to_mpf(residue)),
                scope_tag="POLE",
                connection_note="Simple Eisenstein-model pole at s = 1.",
            )

        residue = pole_residue_at_two(family.kappa)
        return ShadowLEvaluation(
            family_key=family.key,
            display_name=family.display_name,
            s=s,
            kappa=family.kappa,
            kind="pole",
            genus=None,
            value_exact=None,
            value_numeric=None,
            pole_order=1,
            residue_exact=None,
            residue_formula="-kappa*pi^2/6",
            residue_numeric=_numeric_string(residue),
            scope_tag="POLE",
            connection_note="Simple Eisenstein-model pole at s = 2.",
        )

    if s > -1 or s % 2 == 0:
        raise ValueError("supported values are negative odd genus points and poles s = 1, 2")

    genus = (1 - s) // 2
    value = genus_free_energy(family.kappa, genus)
    return ShadowLEvaluation(
        family_key=family.key,
        display_name=family.display_name,
        s=s,
        kappa=family.kappa,
        kind="special_value",
        genus=genus,
        value_exact=value,
        value_numeric=_numeric_string(_fraction_to_mpf(value)),
        pole_order=None,
        residue_exact=None,
        residue_formula=None,
        residue_numeric=None,
        scope_tag=_scope_tag(family, genus),
        connection_note=_connection_note(family, genus),
    )


def evaluate_standard_families(
    genera: Sequence[int] = (1, 2, 3),
    include_vir_self_dual: bool = False,
) -> Sequence[ShadowLEvaluation]:
    """Evaluate the requested standard families at ``s = 1 - 2g``."""

    families = list(all_standard_families())
    if include_vir_self_dual:
        families.append(virasoro_self_dual_family())

    evaluations = []
    for family in families:
        for g in genera:
            if g < 1:
                raise ValueError("genera must all be >= 1")
            evaluations.append(shadow_l_at_s(family, 1 - 2 * g))
    return tuple(evaluations)


def evaluate_task_families(
    genera: Sequence[int] = (1, 2, 3),
) -> Sequence[ShadowLEvaluation]:
    """Evaluate the task-specified families at ``s = 1 - 2g`` for g = 1, 2, 3.

    Families: Heis(k=1), Vir(c=1), sl_2(k=1), W_3(c=2),
    betagamma(lambda=1), free fermion (bc lambda=1/2).
    """
    evaluations = []
    for family in task_families():
        for g in genera:
            if g < 1:
                raise ValueError("genera must all be >= 1")
            evaluations.append(shadow_l_at_s(family, 1 - 2 * g))
    return tuple(evaluations)


__all__ = [
    "HAS_MPMATH",
    "SUPPORTED_POLES",
    "SCOPE_ALL_WEIGHT_G1",
    "SCOPE_UNIFORM_WEIGHT",
    "SCOPE_UNIFORM_WEIGHT_PROJECTION",
    "ShadowFamily",
    "ShadowLEvaluation",
    "bernoulli_number",
    "faber_pandharipande_lambda",
    "genus_free_energy",
    "heisenberg_family",
    "virasoro_family",
    "virasoro_self_dual_family",
    "affine_sl2_family",
    "principal_w3_family",
    "betagamma_family",
    "bc_family",
    "free_fermion_family",
    "all_standard_families",
    "task_families",
    "with_kappa",
    "pole_info",
    "pole_residue_at_one",
    "pole_residue_at_two",
    "shadow_l_at_s",
    "evaluate_standard_families",
    "evaluate_task_families",
]
