r"""DS shadow tower transformation engine for sl_2.

Tracks shadow obstruction tower invariants (S_2, S_3, S_4, Delta)
for V_k(sl_2) BEFORE and AFTER Drinfeld-Sokolov reduction to Vir_c.

The class transition L -> M is the structural content:

  BEFORE (affine KM, class L):
    kappa = 3(k+2)/4,  S_3 = 1 (Killing 3-cocycle),  S_4 = 0 (Jacobi),
    Delta = 8*kappa*S_4 = 0.  Finite shadow tower, depth 3.

  AFTER (Virasoro, class M):
    c = 1 - 6(k+1)^2/(k+2)  (Fateev-Lukyanov),
    kappa = c/2,  S_3 = 2,  S_4 = 10/(c(5c+22)),
    Delta = 8*kappa*S_4 = 40/(5c+22) != 0 generically.
    Infinite shadow tower, depth infinity.

The quartic S_4 is created by the BRST differential coupling matter
to ghosts.  Its appearance is the non-commutativity of the DS-shadow
diagram at arity 4 (thm:ds-central-charge-additivity).

Delta = 0  <=>  S_4 = 0  (for kappa != 0)
Delta = 0  <=>  finite shadow tower  <=>  class G, L, or C

Singular loci of the Virasoro tower:
  c = 0:      S_4 has a pole (kappa = 0, class degenerates).
              Reached from DS at k = -1/2 or k = -4/3.
  c = -22/5:  S_4 and Delta have poles (5c+22 = 0).
              The (2,5) minimal model. Reached at k = 1/2 or k = -8/5.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:ds-central-charge-additivity (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)

Cautions:
    AP1:   kappa from census, not memory.  KM: 3(k+2)/4.  Vir: c/2.
    AP126: r-matrix carries level prefix.  r(z) = k*Omega/z.  k=0 -> r=0.
    AP141: k=0 vanishing check after every r-matrix formula.
    AP14:  Shadow depth != Koszulness.  Both V_k(sl_2) and Vir are Koszul.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, Optional, Tuple

from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl


# ============================================================================
# 1. Central charge formulas
# ============================================================================

def c_sugawara_sl2(k: Fraction) -> Fraction:
    r"""Sugawara central charge c(V_k(sl_2)) = 3k/(k+2).

    dim(sl_2) = 3, h^v = 2.  Undefined at critical level k = -2.

    Checks:
      k=1 -> 1   [SU(2) level 1 WZW]
      k=0 -> 0   [trivial]
    """
    if k + 2 == 0:
        raise ValueError("Critical level k = -2: Sugawara undefined")
    return Fraction(3) * k / (k + 2)


def c_ds_sl2(k: Fraction) -> Fraction:
    r"""Central charge of Vir from DS(sl_2) at level k.

    c(k) = 1 - 6(k+1)^2/(k+2)   (Fateev-Lukyanov, N=2)

    This is the canonical c_wn_fl(N=2, k) formula.
    Undefined at critical level k = -2.

    Checks:
      k=-1 -> 1    [Ising model, (3,4) minimal model]
      k=1  -> -7
      k=2  -> -25/2
    """
    return canonical_c_wn_fl(2, k)


def c_ghost_sl2(k: Fraction) -> Fraction:
    r"""Ghost sector central charge for DS(sl_2).

    c_ghost = c(V_k(sl_2)) - c(Vir_DS)
            = 3k/(k+2) - [1 - 6(k+1)^2/(k+2)]
            = [3k - (k+2) + 6(k+1)^2] / (k+2)
            = [6k^2 + 14k] / (k+2)
            = 2k(3k+7) / (k+2)
    """
    if k + 2 == 0:
        raise ValueError("Critical level k = -2: undefined")
    return c_sugawara_sl2(k) - c_ds_sl2(k)


# ============================================================================
# 2. Kappa formulas
# ============================================================================

def kappa_km_sl2(k: Fraction) -> Fraction:
    r"""kappa(V_k(sl_2)) = dim(sl_2)(k + h^v) / (2 h^v) = 3(k+2)/4.

    # AP1: from landscape_census.tex, C3.  dim(sl_2)=3, h^v=2.
    # Checks: k=0 -> 3/2 (NOT zero); k=-2 -> 0 (critical).
    """
    return Fraction(3) * (k + 2) / 4


def kappa_vir(c: Fraction) -> Fraction:
    r"""kappa(Vir_c) = c/2.

    # AP1: from landscape_census.tex, C2.
    # Checks: c=0 -> 0; c=13 -> 13/2 (self-dual).
    """
    return c / 2


# ============================================================================
# 3. Shadow tower invariants
# ============================================================================

def shadow_tower_km_sl2(k: Fraction) -> Dict[str, Any]:
    r"""Shadow obstruction tower for V_k(sl_2).  Class L, depth 3.

    S_2 = kappa = 3(k+2)/4.
    S_3 = 1  (normalized Killing 3-cocycle).
    S_4 = 0  (Jacobi identity kills the quartic obstruction).
    Delta = 8 * kappa * S_4 = 0.

    The r-matrix is r(z) = k * Omega/z  (AP126: level prefix mandatory).
    At k=0: r(z) = 0 (AP141 check).
    """
    kap = kappa_km_sl2(k)
    S2 = kap
    S3 = Fraction(1)
    S4 = Fraction(0)
    Delta = Fraction(8) * kap * S4  # = 0

    return {
        "S2": S2,
        "S3": S3,
        "S4": S4,
        "Delta": Delta,
        "kappa": kap,
        "shadow_class": "L",
        "shadow_depth": 3,
        "r_matrix": f"r(z) = {k} * Omega / z",
        "r_at_k0": Fraction(0),
    }


def shadow_tower_vir(c: Fraction) -> Dict[str, Any]:
    r"""Shadow obstruction tower for Vir_c.  Class M, depth infinity.

    S_2 = kappa = c/2.
    S_3 = 2.
    S_4 = 10 / (c (5c + 22)).
    Delta = 8 * kappa * S_4 = 40 / (5c + 22).

    Singular at c = 0 (S_4 pole) and c = -22/5 (S_4 and Delta pole).

    The r-matrix is r^Vir(z) = (c/2)/z^3 + 2T/z  (AP126: c/2 prefix).
    """
    kap = kappa_vir(c)
    S2 = kap
    S3 = Fraction(2)

    denom_S4 = c * (5 * c + 22)
    if denom_S4 == 0:
        raise ValueError(
            f"Virasoro shadow tower singular at c = {c}: "
            f"c*(5c+22) = {denom_S4}"
        )
    S4 = Fraction(10) / denom_S4

    denom_Delta = 5 * c + 22
    if denom_Delta == 0:
        raise ValueError(f"Delta singular at c = {c}: 5c+22 = 0")
    Delta = Fraction(40) / denom_Delta

    return {
        "S2": S2,
        "S3": S3,
        "S4": S4,
        "Delta": Delta,
        "kappa": kap,
        "shadow_class": "M",
        "shadow_depth": "inf",
    }


# ============================================================================
# 4. DS transition
# ============================================================================

def ds_transition_sl2(k: Fraction) -> Dict[str, Any]:
    r"""Full DS transition V_k(sl_2) -> Vir_c.

    Returns shadow tower data before (class L) and after (class M),
    demonstrating the depth increase mechanism.

    The central structural fact: Delta goes from 0 to nonzero.
    """
    c = c_ds_sl2(k)
    before = shadow_tower_km_sl2(k)
    after = shadow_tower_vir(c)

    return {
        "k": k,
        "c_sugawara": c_sugawara_sl2(k),
        "c_ds": c,
        "c_ghost": c_ghost_sl2(k),
        "before": before,
        "after": after,
        "Delta_before": before["Delta"],
        "Delta_after": after["Delta"],
        "class_before": before["shadow_class"],
        "class_after": after["shadow_class"],
        "depth_increase": True,
    }


def ds_transition_table(k_values: Optional[list] = None) -> list:
    r"""Tabulate the DS transition for multiple levels.

    Default levels: k = 1, 2, 3, 5, 10 (positive integer, non-critical).
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 10]]
    results = []
    for kv in k_values:
        t = ds_transition_sl2(kv)
        results.append({
            "k": kv,
            "c_ds": t["c_ds"],
            "kappa_before": t["before"]["kappa"],
            "kappa_after": t["after"]["kappa"],
            "S4_before": t["before"]["S4"],
            "S4_after": t["after"]["S4"],
            "Delta_before": t["Delta_before"],
            "Delta_after": t["Delta_after"],
            "class_before": t["class_before"],
            "class_after": t["class_after"],
        })
    return results


# ============================================================================
# 5. Singular locus analysis
# ============================================================================

def singular_k_values() -> Dict[str, list]:
    r"""k-values where the post-DS Virasoro tower is singular.

    c = 0:     k = -1/2 or k = -4/3.   (kappa = 0, S_4 pole)
    c = -22/5: k = 1/2 or k = -8/5.    (Delta pole, (2,5) minimal model)
    """
    return {
        "c_eq_0": [Fraction(-1, 2), Fraction(-4, 3)],
        "c_eq_m22o5": [Fraction(1, 2), Fraction(-8, 5)],
    }
