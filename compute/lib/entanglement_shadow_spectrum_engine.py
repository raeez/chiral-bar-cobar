"""Entanglement shadow spectrum engine for standard chiral-algebra families.

The engine tracks two related scalar quantities:

1. Physical single-interval entropy:
   S_EE = (c / 3) * log(L / eps)

2. Shadow-universal entropy built from the modular characteristic:
   S_shadow = (2 * kappa / 3) * log(L / eps)

The user-requested family data makes these coincide for some families and
separate for others, so both are kept explicit.
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Any, Dict, Iterable, Mapping, Optional


LIE_ALGEBRA_DATA: Dict[str, Dict[str, int]] = {
    "sl_2": {"dim": 3, "h_dual": 2},
    "sl_3": {"dim": 8, "h_dual": 3},
    "e_8": {"dim": 248, "h_dual": 30},
}


DEFAULT_CENSUS_SWEEPS: Dict[str, tuple[Dict[str, Any], ...]] = {
    "heisenberg": ({"k": Fraction(1)},),
    "virasoro": ({"c": Fraction(1)}, {"c": Fraction(13)}),
    "affine_km": (
        {"lie_algebra": "sl_2", "k": Fraction(1)},
        {"lie_algebra": "sl_3", "k": Fraction(1)},
        {"lie_algebra": "e_8", "k": Fraction(1)},
    ),
    "w_n": ({"N": 2, "c": Fraction(1)}, {"N": 3, "c": Fraction(6)}),
    "bc": ({"lam": Fraction(1, 2)}, {"lam": Fraction(2)}),
    "betagamma": ({"lam": Fraction(1, 2)}, {"lam": Fraction(2)}),
    "bershadsky_polyakov": ({"k": Fraction(0)},),
}


def _as_fraction(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value, 1)
    return Fraction(value).limit_denominator()


def _safe_entropy(central_charge: Optional[Fraction], L: float, eps: float) -> Optional[float]:
    if central_charge is None:
        return None
    return entanglement_entropy(central_charge, L, eps)


def _safe_ratio(numerator: Optional[float], denominator: Fraction) -> Optional[float]:
    if numerator is None or denominator == 0:
        return None
    return numerator / float(denominator)


def _format_param_key(params: Mapping[str, Any]) -> str:
    fragments = []
    for key in sorted(params):
        value = params[key]
        if isinstance(value, Fraction):
            fragments.append(f"{key}={value}")
        else:
            fragments.append(f"{key}={value}")
    return ",".join(fragments)


def harmonic_number(n: int) -> Fraction:
    """Return the exact harmonic number H_n."""
    if n < 1:
        raise ValueError("harmonic_number requires n >= 1")
    return sum(Fraction(1, j) for j in range(1, n + 1))


def heisenberg_central_charge() -> Fraction:
    """Return c(H_k) = 1 in the user-requested normalization."""
    return Fraction(1)


def heisenberg_kappa(k: Any) -> Fraction:
    """Return kappa(H_k) = k."""
    return _as_fraction(k)


def virasoro_central_charge(c: Any) -> Fraction:
    """Return the Virasoro central charge parameter c."""
    return _as_fraction(c)


def virasoro_kappa(c: Any) -> Fraction:
    """Return kappa(Vir_c) = c/2."""
    return _as_fraction(c) / 2


def affine_km_central_charge(lie_algebra: str, k: Any) -> Fraction:
    """Return c(V_k(g)) = k * dim(g) / (k + h^v)."""
    kappa_data = affine_km_constants(lie_algebra)
    level = _as_fraction(k)
    denominator = level + kappa_data["h_dual"]
    if denominator == 0:
        raise ValueError("affine central charge has a pole at the critical level")
    return level * kappa_data["dim"] / denominator


def affine_km_kappa(lie_algebra: str, k: Any) -> Fraction:
    """Return kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v)."""
    kappa_data = affine_km_constants(lie_algebra)
    level = _as_fraction(k)
    return kappa_data["dim"] * (level + kappa_data["h_dual"]) / (2 * kappa_data["h_dual"])


def affine_km_constants(lie_algebra: str) -> Dict[str, Fraction]:
    if lie_algebra not in LIE_ALGEBRA_DATA:
        raise ValueError(f"unsupported Lie algebra: {lie_algebra}")
    constants = LIE_ALGEBRA_DATA[lie_algebra]
    return {
        "dim": Fraction(constants["dim"]),
        "h_dual": Fraction(constants["h_dual"]),
    }


def w_algebra_central_charge(c: Any) -> Fraction:
    """Return the supplied principal W_N central charge parameter."""
    return _as_fraction(c)


def w_algebra_kappa(N: int, c: Any) -> Fraction:
    """Return kappa(W_N) = c * (H_N - 1)."""
    if N < 2:
        raise ValueError("W_N requires N >= 2")
    return _as_fraction(c) * (harmonic_number(N) - 1)


def bc_central_charge(lam: Any) -> Fraction:
    """Return c_bc(lambda) = 1 - 3 * (2*lambda - 1)^2."""
    lam_fraction = _as_fraction(lam)
    return Fraction(1) - 3 * (2 * lam_fraction - 1) ** 2


def bc_kappa(lam: Any) -> Fraction:
    """Return kappa_bc(lambda) = c_bc(lambda) / 2."""
    return bc_central_charge(lam) / 2


def betagamma_central_charge(lam: Any) -> Fraction:
    """Return c_bg(lambda) = 2 * (6*lambda^2 - 6*lambda + 1)."""
    lam_fraction = _as_fraction(lam)
    return 2 * (6 * lam_fraction**2 - 6 * lam_fraction + 1)


def betagamma_kappa(lam: Any) -> Fraction:
    """Return kappa_bg(lambda) = c_bg(lambda) / 2."""
    return betagamma_central_charge(lam) / 2


def bershadsky_polyakov_central_charge(k: Any) -> Fraction:
    """Return c_BP(k) = 2 - 24*(k + 1)^2/(k + 3)."""
    level = _as_fraction(k)
    denominator = level + 3
    if denominator == 0:
        raise ValueError("Bershadsky-Polyakov central charge has a pole at k = -3")
    return Fraction(2) - 24 * (level + 1) ** 2 / denominator


def bershadsky_polyakov_kappa(k: Any) -> Fraction:
    """Return kappa_BP(k) = c_BP(k) / 6 from the live census convention."""
    return bershadsky_polyakov_central_charge(k) / 6


def entanglement_entropy(central_charge: Any, L: float, eps: float) -> float:
    """Return S_EE = (c / 3) * log(L / eps)."""
    return float(_as_fraction(central_charge)) * log_ratio(L, eps) / 3.0


def entanglement_shadow_kappa(kappa: Any) -> Fraction:
    """Return kappa_EE = 2*kappa/3."""
    return Fraction(2, 3) * _as_fraction(kappa)


def shadow_entropy(kappa: Any, L: float, eps: float) -> float:
    """Return S_shadow = kappa_EE * log(L / eps)."""
    return float(entanglement_shadow_kappa(kappa)) * log_ratio(L, eps)


def shadow_spectrum_ratio(kappa: Any, L: float, eps: float) -> Optional[float]:
    """Return S_shadow / kappa when kappa is nonzero."""
    kappa_fraction = _as_fraction(kappa)
    if kappa_fraction == 0:
        return None
    return shadow_entropy(kappa_fraction, L, eps) / float(kappa_fraction)


def universal_shadow_ratio(L: float, eps: float) -> float:
    """Return the universal ratio (2/3) * log(L / eps)."""
    return (2.0 / 3.0) * log_ratio(L, eps)


def log_ratio(L: float, eps: float) -> float:
    """Return log(L / eps) using the natural logarithm."""
    if L <= 0 or eps <= 0:
        raise ValueError("L and eps must be positive")
    return math.log(L / eps)


def heisenberg_dual_k(k: Any) -> Fraction:
    return -_as_fraction(k)


def virasoro_dual_c(c: Any) -> Fraction:
    return Fraction(26) - _as_fraction(c)


def affine_km_dual_level(lie_algebra: str, k: Any) -> Fraction:
    constants = affine_km_constants(lie_algebra)
    level = _as_fraction(k)
    return -level - 2 * constants["h_dual"]


def heisenberg_entanglement_koszul_conductor(k: Any) -> Fraction:
    kappa = heisenberg_kappa(k)
    dual_kappa = heisenberg_kappa(heisenberg_dual_k(k))
    return entanglement_shadow_kappa(kappa) + entanglement_shadow_kappa(dual_kappa)


def virasoro_entanglement_koszul_conductor(c: Any) -> Fraction:
    kappa = virasoro_kappa(c)
    dual_kappa = virasoro_kappa(virasoro_dual_c(c))
    return entanglement_shadow_kappa(kappa) + entanglement_shadow_kappa(dual_kappa)


def affine_km_entanglement_koszul_conductor(lie_algebra: str, k: Any) -> Fraction:
    kappa = affine_km_kappa(lie_algebra, k)
    dual_kappa = affine_km_kappa(lie_algebra, affine_km_dual_level(lie_algebra, k))
    return entanglement_shadow_kappa(kappa) + entanglement_shadow_kappa(dual_kappa)


def build_family_record(family: str, L: float, eps: float, **params: Any) -> Dict[str, Any]:
    """Build a full scalar census record for one family/parameter choice."""
    if family == "heisenberg":
        k = _as_fraction(params["k"])
        central_charge = heisenberg_central_charge()
        kappa = heisenberg_kappa(k)
        dual_params = {"k": heisenberg_dual_k(k)}
        kappa_dual = heisenberg_kappa(dual_params["k"])
        conductor = heisenberg_entanglement_koszul_conductor(k)
    elif family == "virasoro":
        c = _as_fraction(params["c"])
        central_charge = virasoro_central_charge(c)
        kappa = virasoro_kappa(c)
        dual_params = {"c": virasoro_dual_c(c)}
        kappa_dual = virasoro_kappa(dual_params["c"])
        conductor = virasoro_entanglement_koszul_conductor(c)
    elif family == "affine_km":
        lie_algebra = params["lie_algebra"]
        level = _as_fraction(params["k"])
        try:
            central_charge = affine_km_central_charge(lie_algebra, level)
        except ValueError:
            central_charge = None
        kappa = affine_km_kappa(lie_algebra, level)
        dual_params = {"lie_algebra": lie_algebra, "k": affine_km_dual_level(lie_algebra, level)}
        kappa_dual = affine_km_kappa(lie_algebra, dual_params["k"])
        conductor = affine_km_entanglement_koszul_conductor(lie_algebra, level)
    elif family == "w_n":
        N = int(params["N"])
        c = _as_fraction(params["c"])
        central_charge = w_algebra_central_charge(c)
        kappa = w_algebra_kappa(N, c)
        dual_params = None
        kappa_dual = None
        conductor = None
    elif family == "bc":
        lam = _as_fraction(params["lam"])
        central_charge = bc_central_charge(lam)
        kappa = bc_kappa(lam)
        dual_params = None
        kappa_dual = None
        conductor = None
    elif family == "betagamma":
        lam = _as_fraction(params["lam"])
        central_charge = betagamma_central_charge(lam)
        kappa = betagamma_kappa(lam)
        dual_params = None
        kappa_dual = None
        conductor = None
    elif family == "bershadsky_polyakov":
        level = _as_fraction(params["k"])
        try:
            central_charge = bershadsky_polyakov_central_charge(level)
        except ValueError:
            central_charge = None
        kappa = bershadsky_polyakov_kappa(level)
        dual_params = None
        kappa_dual = None
        conductor = None
    else:
        raise ValueError(f"unsupported family: {family}")

    entropy = _safe_entropy(central_charge, L, eps)
    shadow = shadow_entropy(kappa, L, eps)
    record = {
        "family": family,
        "params": dict(params),
        "central_charge": central_charge,
        "kappa": kappa,
        "kappa_ee": entanglement_shadow_kappa(kappa),
        "entanglement_entropy": entropy,
        "shadow_entropy": shadow,
        "shadow_spectrum_ratio": shadow_spectrum_ratio(kappa, L, eps),
        "physical_entropy_over_kappa": _safe_ratio(entropy, kappa),
        "log_ratio": log_ratio(L, eps),
        "dual_params": dual_params,
        "kappa_dual": kappa_dual,
        "kappa_ee_dual": None if kappa_dual is None else entanglement_shadow_kappa(kappa_dual),
        "entanglement_koszul_conductor": conductor,
    }
    return record


def generate_census_table(
    L: float,
    eps: float,
    sweeps: Optional[Mapping[str, Iterable[Mapping[str, Any]]]] = None,
) -> Dict[str, Dict[str, Dict[str, Any]]]:
    """Generate a dict-of-dicts census table for family parameter sweeps."""
    active_sweeps = sweeps or DEFAULT_CENSUS_SWEEPS
    table: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for family, family_sweep in active_sweeps.items():
        table[family] = {}
        for param_set in family_sweep:
            key = _format_param_key(param_set)
            table[family][key] = build_family_record(family, L=L, eps=eps, **param_set)
    return table


__all__ = [
    "DEFAULT_CENSUS_SWEEPS",
    "LIE_ALGEBRA_DATA",
    "affine_km_central_charge",
    "affine_km_constants",
    "affine_km_dual_level",
    "affine_km_entanglement_koszul_conductor",
    "affine_km_kappa",
    "bc_central_charge",
    "bc_kappa",
    "bershadsky_polyakov_central_charge",
    "bershadsky_polyakov_kappa",
    "betagamma_central_charge",
    "betagamma_kappa",
    "build_family_record",
    "entanglement_entropy",
    "entanglement_shadow_kappa",
    "generate_census_table",
    "harmonic_number",
    "heisenberg_central_charge",
    "heisenberg_dual_k",
    "heisenberg_entanglement_koszul_conductor",
    "heisenberg_kappa",
    "log_ratio",
    "shadow_entropy",
    "shadow_spectrum_ratio",
    "universal_shadow_ratio",
    "virasoro_central_charge",
    "virasoro_dual_c",
    "virasoro_entanglement_koszul_conductor",
    "virasoro_kappa",
    "w_algebra_central_charge",
    "w_algebra_kappa",
]
