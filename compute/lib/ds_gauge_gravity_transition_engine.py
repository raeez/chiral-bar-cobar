"""DS gauge/gravity transition engine for V_k(sl_2) -> Vir_c.

This module records the shadow-tower data on the sl_2 Sugawara/T-line before
Drinfeld-Sokolov reduction and on the Virasoro line after reduction.

Conventions used here:
    Pre-DS affine sl_2:
        c_aff = 3k / (k + 2)
        kappa = S_2 = 3(k + 2) / 4
        S_3 = 4 / (k + 2)
        S_4 = 0
        Delta = 8*kappa*S_4 = 0

    Post-DS Virasoro:
        c_DS = 1 - 6(k + 1)^2 / (k + 2)
        kappa = S_2 = c_DS / 2
        S_3 = 2
        S_4 = 10 / [c_DS * (5*c_DS + 22)]
        Delta = 8*kappa*S_4 = 40 / (5*c_DS + 22)

Critical level k = -2:
    The affine Sugawara channel degenerates and DS reduction is undefined.
    We still record the affine limiting data kappa = S_2 = 0, S_4 = 0,
    Delta = 0, while the cubic shadow is singular.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Optional, Sequence


DEFAULT_LEVELS: tuple[Fraction, ...] = tuple(
    Fraction(level) for level in (1, 2, 3, 4, 5, 10, 100)
)
CRITICAL_LEVEL = Fraction(-2)


def _as_fraction(level: int | Fraction) -> Fraction:
    return level if isinstance(level, Fraction) else Fraction(level)


def affine_sl2_sugawara_c(level: int | Fraction) -> Fraction:
    """Sugawara central charge c(V_k(sl_2)) = 3k / (k + 2)."""
    k = _as_fraction(level)
    if k + 2 == 0:
        raise ValueError("Affine sl_2 Sugawara central charge undefined at k = -2")
    return Fraction(3) * k / (k + 2)


def affine_sl2_kappa(level: int | Fraction) -> Fraction:
    """kappa(V_k(sl_2)) = 3(k + 2) / 4."""
    k = _as_fraction(level)
    return Fraction(3) * (k + 2) / 4


def affine_sl2_s3(level: int | Fraction) -> Fraction:
    """Sugawara/T-line cubic shadow S_3 = 4 / (k + 2)."""
    k = _as_fraction(level)
    if k + 2 == 0:
        raise ValueError("Affine sl_2 cubic shadow undefined at k = -2")
    return Fraction(4) / (k + 2)


def affine_sl2_s4(level: int | Fraction) -> Fraction:
    """Affine sl_2 is class L, so the quartic shadow vanishes."""
    _ = _as_fraction(level)
    return Fraction(0)


def ds_sl2_virasoro_c(level: int | Fraction) -> Fraction:
    """DS central charge c_DS = 1 - 6(k + 1)^2 / (k + 2)."""
    k = _as_fraction(level)
    if k + 2 == 0:
        raise ValueError("DS Virasoro central charge undefined at k = -2")
    return Fraction(1) - Fraction(6) * (k + 1) ** 2 / (k + 2)


def virasoro_kappa(central_charge: Fraction) -> Fraction:
    """kappa(Vir_c) = c / 2."""
    return central_charge / 2


def virasoro_s3() -> Fraction:
    """The Virasoro cubic shadow is the universal value 2."""
    return Fraction(2)


def virasoro_s4(central_charge: Fraction) -> Fraction:
    """Quartic contact invariant S_4(Vir_c) = 10 / [c(5c+22)]."""
    if central_charge == 0:
        raise ValueError("Virasoro quartic shadow undefined at c = 0")
    if 5 * central_charge + 22 == 0:
        raise ValueError("Virasoro quartic shadow undefined at c = -22/5")
    return Fraction(10) / (central_charge * (5 * central_charge + 22))


def shadow_discriminant(
    kappa: Optional[Fraction],
    s4: Optional[Fraction],
) -> Optional[Fraction]:
    """Delta = 8*kappa*S_4 when both factors are defined."""
    if kappa is None or s4 is None:
        return None
    return Fraction(8) * kappa * s4


@dataclass(frozen=True)
class ShadowTowerState:
    """Shadow invariants for one algebraic stage of the DS transition."""

    stage: str
    family: str
    shadow_class: str
    level: Fraction
    central_charge: Optional[Fraction]
    kappa: Optional[Fraction]
    S_2: Optional[Fraction]
    S_3: Optional[Fraction]
    S_4: Optional[Fraction]
    Delta: Optional[Fraction]
    tower_depth: Optional[int]
    finite_tower: bool
    convention: str
    singular_reason: Optional[str] = None


@dataclass(frozen=True)
class DSGaugeGravityTransition:
    """Pre-DS and post-DS shadow data at one level."""

    level: Fraction
    pre_ds: ShadowTowerState
    post_ds: ShadowTowerState
    delta_jump: Optional[Fraction]
    quartic_created: bool
    class_transition: tuple[str, str]


def affine_sl2_state(level: int | Fraction) -> ShadowTowerState:
    """Affine sl_2 shadow data on the Sugawara/T-line before DS reduction."""
    k = _as_fraction(level)
    kappa = affine_sl2_kappa(k)
    s4 = affine_sl2_s4(k)
    delta = shadow_discriminant(kappa, s4)

    if k == CRITICAL_LEVEL:
        return ShadowTowerState(
            stage="pre_ds_affine",
            family="V_k(sl_2)",
            shadow_class="L",
            level=k,
            central_charge=None,
            kappa=kappa,
            S_2=kappa,
            S_3=None,
            S_4=s4,
            Delta=delta,
            tower_depth=3,
            finite_tower=True,
            convention="Sugawara/T-line normalization",
            singular_reason=(
                "Critical level k = -2: Sugawara central charge is undefined "
                "and the cubic shadow has a pole."
            ),
        )

    return ShadowTowerState(
        stage="pre_ds_affine",
        family="V_k(sl_2)",
        shadow_class="L",
        level=k,
        central_charge=affine_sl2_sugawara_c(k),
        kappa=kappa,
        S_2=kappa,
        S_3=affine_sl2_s3(k),
        S_4=s4,
        Delta=delta,
        tower_depth=3,
        finite_tower=True,
        convention="Sugawara/T-line normalization",
    )


def ds_virasoro_state(level: int | Fraction) -> ShadowTowerState:
    """Virasoro shadow data after DS reduction."""
    k = _as_fraction(level)
    if k == CRITICAL_LEVEL:
        return ShadowTowerState(
            stage="post_ds_virasoro",
            family="Vir_c",
            shadow_class="critical",
            level=k,
            central_charge=None,
            kappa=None,
            S_2=None,
            S_3=None,
            S_4=None,
            Delta=None,
            tower_depth=None,
            finite_tower=False,
            convention="Virasoro primary-line normalization",
            singular_reason="Critical level k = -2: DS reduction is undefined.",
        )

    central_charge = ds_sl2_virasoro_c(k)
    kappa = virasoro_kappa(central_charge)
    s4 = virasoro_s4(central_charge)
    return ShadowTowerState(
        stage="post_ds_virasoro",
        family="Vir_c",
        shadow_class="M",
        level=k,
        central_charge=central_charge,
        kappa=kappa,
        S_2=kappa,
        S_3=virasoro_s3(),
        S_4=s4,
        Delta=shadow_discriminant(kappa, s4),
        tower_depth=None,
        finite_tower=False,
        convention="Virasoro primary-line normalization",
    )


def ds_transition_at_level(level: int | Fraction) -> DSGaugeGravityTransition:
    """Complete shadow transition data for one level."""
    k = _as_fraction(level)
    pre_ds = affine_sl2_state(k)
    post_ds = ds_virasoro_state(k)
    delta_jump = None
    quartic_created = False

    if pre_ds.Delta is not None and post_ds.Delta is not None:
        delta_jump = post_ds.Delta - pre_ds.Delta
    if pre_ds.S_4 is not None and post_ds.S_4 is not None:
        quartic_created = pre_ds.S_4 == 0 and post_ds.S_4 != 0

    return DSGaugeGravityTransition(
        level=k,
        pre_ds=pre_ds,
        post_ds=post_ds,
        delta_jump=delta_jump,
        quartic_created=quartic_created,
        class_transition=(pre_ds.shadow_class, post_ds.shadow_class),
    )


def transition_table(
    levels: Sequence[int | Fraction] = DEFAULT_LEVELS,
) -> list[DSGaugeGravityTransition]:
    """Transition data for the requested generic levels."""
    return [ds_transition_at_level(level) for level in levels]


def critical_level_transition() -> DSGaugeGravityTransition:
    """Structured degeneration data at the sl_2 critical level."""
    return ds_transition_at_level(CRITICAL_LEVEL)
