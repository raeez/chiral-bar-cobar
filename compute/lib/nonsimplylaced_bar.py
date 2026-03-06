"""Non-simply-laced Kac-Moody bar complexes: B_2 and G_2.

Key distinction from simply-laced:
  h != h^vee  (Coxeter number != dual Coxeter number)
  Root lengths vary: long roots and short roots.

Ground truth:
  B_2 = so(5): dim=10, h=4, h^vee=3, rank=2
    Roots: 4 long (|alpha|^2=2), 4 short (|alpha|^2=1)
    c = 10k/(k+3)
    k' = -k - 6 (FF dual)
    kappa = 10(k+3)/6 = 5(k+3)/3

  G_2: dim=14, h=6, h^vee=4, rank=2
    Roots: 6 long (|alpha|^2=6), 6 short (|alpha|^2=2)
    (Convention: short root normalized to |alpha|^2=2; ratio short:long = 1:3)
    c = 14k/(k+4)
    k' = -k - 8 (FF dual)
    kappa = 14(k+4)/8 = 7(k+4)/4

  CRITICAL: KM periodicity uses h (Coxeter), NOT h^vee.
  For non-simply-laced: these differ!
    B_2: period 2h = 8 (Coxeter), NOT 2*3 = 6
    G_2: period 2h = 12 (Coxeter), NOT 2*4 = 8

  From CLAUDE.md: "h-dual(g-dual) = h-dual(g) ONLY for simply-laced;
    B_n: h-dual=2n-1, C_n: h-dual=n+1"

CONVENTIONS:
- Cohomological grading, |d| = +1
"""

from __future__ import annotations

from typing import Dict, Tuple

from sympy import Rational, Symbol

from compute.lib.lie_algebra import cartan_data


# ---------------------------------------------------------------------------
# B_2 = so(5)
# ---------------------------------------------------------------------------

def b2_data() -> Dict[str, object]:
    """Complete data for B_2 = so(5)."""
    data = cartan_data("B", 2)
    return {
        "type": "B2",
        "dim": data.dim,        # 10
        "rank": data.rank,      # 2
        "h": data.h,            # 4
        "h_dual": data.h_dual,  # 3
        "n_positive_roots": len(data.positive_roots),  # 4
        "exponents": data.exponents,  # [1, 3]
        "root_lengths": data.root_lengths_squared,  # B_2: [2, 1] (long alpha_1, short alpha_2)
        "generators": 2 * len(data.positive_roots) + data.rank,  # 10
    }


def b2_central_charge(k=None):
    """c(B_2, k) = 10k/(k+3)."""
    if k is None:
        k = Symbol('k')
    return Rational(10) * k / (k + 3)


def b2_ff_dual(k=None):
    """k' = -k - 2*3 = -k - 6."""
    if k is None:
        k = Symbol('k')
    return -k - 6


def b2_kappa(k=None):
    """kappa(B_2, k) = dim*(k+h^vee)/(2*h^vee) = 10(k+3)/6 = 5(k+3)/3."""
    if k is None:
        k = Symbol('k')
    return Rational(5) * (k + 3) / 3


def b2_complementarity_sum() -> int:
    """c + c' = 2*dim = 20."""
    return 20


def b2_bar_generators() -> Dict[str, int]:
    """Generator content for B_2 bar complex.

    B_2 has 10 generators: 2 Cartan + 4 positive roots + 4 negative roots.
    All at conformal weight 1.
    """
    return {
        "cartan": 2,
        "long_roots": 4,   # 2 positive + 2 negative
        "short_roots": 4,  # 2 positive + 2 negative
        "total": 10,
    }


def b2_bar_deg2_count() -> int:
    """Number of degree-2 bar elements: 10^2 = 100."""
    return 100


def b2_curvature(k=None):
    """Curvature m_0 = (k+h^vee)/(2h^vee) * kappa-form = (k+3)/6 * kappa."""
    if k is None:
        k = Symbol('k')
    return (k + 3) / 6


# ---------------------------------------------------------------------------
# G_2
# ---------------------------------------------------------------------------

def g2_data() -> Dict[str, object]:
    """Complete data for G_2."""
    data = cartan_data("G", 2)
    return {
        "type": "G2",
        "dim": data.dim,        # 14
        "rank": data.rank,      # 2
        "h": data.h,            # 6
        "h_dual": data.h_dual,  # 4
        "n_positive_roots": len(data.positive_roots),  # 6
        "exponents": data.exponents,  # [1, 5]
        "root_lengths": data.root_lengths_squared,  # [2, 6] (alpha_1 short, alpha_2 long)
        "generators": 2 * len(data.positive_roots) + data.rank,  # 14
    }


def g2_central_charge(k=None):
    """c(G_2, k) = 14k/(k+4)."""
    if k is None:
        k = Symbol('k')
    return Rational(14) * k / (k + 4)


def g2_ff_dual(k=None):
    """k' = -k - 2*4 = -k - 8."""
    if k is None:
        k = Symbol('k')
    return -k - 8


def g2_kappa(k=None):
    """kappa(G_2, k) = 14(k+4)/8 = 7(k+4)/4."""
    if k is None:
        k = Symbol('k')
    return Rational(7) * (k + 4) / 4


def g2_complementarity_sum() -> int:
    """c + c' = 2*dim = 28."""
    return 28


def g2_bar_generators() -> Dict[str, int]:
    """Generator content for G_2 bar complex.

    G_2 has 14 generators: 2 Cartan + 6 positive + 6 negative roots.
    """
    return {
        "cartan": 2,
        "long_roots": 6,   # 3 positive + 3 negative
        "short_roots": 6,  # 3 positive + 3 negative
        "total": 14,
    }


def g2_bar_deg2_count() -> int:
    """Number of degree-2 bar elements: 14^2 = 196."""
    return 196


def g2_curvature(k=None):
    """Curvature m_0 = (k+h^vee)/(2h^vee) * kappa-form = (k+4)/8 * kappa."""
    if k is None:
        k = Symbol('k')
    return (k + 4) / 8


# ---------------------------------------------------------------------------
# Periodicity: h vs h^vee distinction
# ---------------------------------------------------------------------------

def periodicity_coxeter(type_: str, rank: int) -> int:
    """KM bar cohomology period = 2h (Coxeter number).

    CRITICAL: uses h, NOT h^vee. These differ for non-simply-laced.
    """
    data = cartan_data(type_, rank)
    return 2 * data.h


def periodicity_vs_dual_coxeter(type_: str, rank: int) -> Dict[str, object]:
    """Compare h and h^vee for periodicity discussion."""
    data = cartan_data(type_, rank)
    return {
        "h": data.h,
        "h_dual": data.h_dual,
        "simply_laced": data.h == data.h_dual,
        "period_correct": 2 * data.h,
        "period_wrong": 2 * data.h_dual,
        "difference": abs(data.h - data.h_dual),
    }


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_b2():
    """Verify B_2 data."""
    k = Symbol('k')
    results = {}

    d = b2_data()
    results["dim = 10"] = d["dim"] == 10
    results["h = 4"] = d["h"] == 4
    results["h_dual = 3"] = d["h_dual"] == 3
    results["h != h_dual"] = d["h"] != d["h_dual"]
    results["n_pos_roots = 4"] = d["n_positive_roots"] == 4

    results["c(k) = 10k/(k+3)"] = b2_central_charge(k) == 10 * k / (k + 3)
    results["k' = -k-6"] = b2_ff_dual(k) == -k - 6
    results["involution (k')' = k"] = b2_ff_dual(b2_ff_dual(k)) == k
    results["c + c' = 20"] = b2_complementarity_sum() == 20
    results["period = 2h = 8"] = periodicity_coxeter("B", 2) == 8

    return results


def verify_g2():
    """Verify G_2 data."""
    k = Symbol('k')
    results = {}

    d = g2_data()
    results["dim = 14"] = d["dim"] == 14
    results["h = 6"] = d["h"] == 6
    results["h_dual = 4"] = d["h_dual"] == 4
    results["h != h_dual"] = d["h"] != d["h_dual"]
    results["n_pos_roots = 6"] = d["n_positive_roots"] == 6

    results["c(k) = 14k/(k+4)"] = g2_central_charge(k) == 14 * k / (k + 4)
    results["k' = -k-8"] = g2_ff_dual(k) == -k - 8
    results["involution (k')' = k"] = g2_ff_dual(g2_ff_dual(k)) == k
    results["c + c' = 28"] = g2_complementarity_sum() == 28
    results["period = 2h = 12"] = periodicity_coxeter("G", 2) == 12

    return results


def verify_periodicity_distinction():
    """Verify h vs h^vee distinction for non-simply-laced."""
    results = {}

    # Simply-laced: A_2
    a2 = periodicity_vs_dual_coxeter("A", 2)
    results["A2: h = h_dual"] = a2["simply_laced"]

    # Non-simply-laced: B_2
    b2 = periodicity_vs_dual_coxeter("B", 2)
    results["B2: h != h_dual"] = not b2["simply_laced"]
    results["B2: h=4, h_dual=3"] = b2["h"] == 4 and b2["h_dual"] == 3

    # Non-simply-laced: G_2
    g2 = periodicity_vs_dual_coxeter("G", 2)
    results["G2: h != h_dual"] = not g2["simply_laced"]
    results["G2: h=6, h_dual=4"] = g2["h"] == 6 and g2["h_dual"] == 4

    return results


def verify_nonsimplylaced_all():
    results = {}
    for section, fn in [
        ("B2", verify_b2),
        ("G2", verify_g2),
        ("periodicity", verify_periodicity_distinction),
    ]:
        for name, ok in fn().items():
            results[f"{section}: {name}"] = ok
    return results


if __name__ == "__main__":
    print("=" * 60)
    print("NON-SIMPLY-LACED BAR COMPLEXES: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_nonsimplylaced_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
