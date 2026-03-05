"""Cross-algebra integration: unified bar complex comparison.

Brings together ALL algebras in the compute engine with a single
interface for comparing bar complex structure across algebras.

Algebras in the engine:
  1. Heisenberg       (1 gen, bosonic, weight 1)
  2. Free fermion     (2 gen, fermionic, weight 1/2 + 1/2)
  3. Beta-gamma       (2 gen, mixed, weight 0 + 1)
  4. bc ghosts        (2 gen, fermionic, weight lambda + (1-lambda))
  5. sl_2             (3 gen, bosonic, weight 1)
  6. sl_3             (8 gen, bosonic, weight 1)
  7. Virasoro         (1 gen, bosonic, weight 2)
  8. W_3              (2 gen, bosonic, weight 2 + 3)
  9. E_8 lattice      (248 gen, bosonic, weight 1)
  10. B_2 (so(5))     (10 gen, bosonic, weight 1)
  11. G_2             (14 gen, bosonic, weight 1)

Ground truth: Master Table (examples_summary.tex), CLAUDE.md verified formulas.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from sympy import Rational, Symbol


# ---------------------------------------------------------------------------
# Unified algebra registry
# ---------------------------------------------------------------------------

ALGEBRA_REGISTRY = {
    "Heisenberg": {
        "n_generators": 1,
        "generator_parity": "bosonic",
        "generator_weights": [1],
        "max_pole_order": 2,
        "curvature_formula": "k/2",
        "complementarity_sum": None,  # no DS reduction
        "koszul_dual": "Sym^ch(V*)",
        "self_dual": False,
        "spectral_collapse": 1,
    },
    "free_fermion": {
        "n_generators": 2,
        "generator_parity": "fermionic",
        "generator_weights": [Rational(1, 2), Rational(1, 2)],
        "max_pole_order": 1,
        "curvature_formula": "0",
        "complementarity_sum": None,
        "koszul_dual": "Sym^ch(V*)",
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "betagamma": {
        "n_generators": 2,
        "generator_parity": "bosonic",
        "generator_weights": [0, 1],
        "max_pole_order": 1,
        "curvature_formula": "0",
        "complementarity_sum": None,
        "koszul_dual": "bc",
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "bc": {
        "n_generators": 2,
        "generator_parity": "fermionic",
        "generator_weights": [Symbol('lambda'), 1 - Symbol('lambda')],
        "max_pole_order": 1,
        "curvature_formula": "0",
        "complementarity_sum": None,
        "koszul_dual": "betagamma",
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "sl2": {
        "n_generators": 3,
        "generator_parity": "bosonic",
        "generator_weights": [1, 1, 1],
        "max_pole_order": 2,
        "curvature_formula": "(k+2)/4 * kappa",
        "complementarity_sum": 6,   # 2*dim = 2*3
        "koszul_dual": "sl2_{-k-4}",
        "self_dual": True,  # as Lie algebra (not as VA at fixed level)
        "spectral_collapse": 1,
    },
    "sl3": {
        "n_generators": 8,
        "generator_parity": "bosonic",
        "generator_weights": [1] * 8,
        "max_pole_order": 2,
        "curvature_formula": "(k+3)/6 * kappa",
        "complementarity_sum": 16,  # 2*dim = 2*8
        "koszul_dual": "sl3_{-k-6}",
        "self_dual": True,
        "spectral_collapse": 1,
    },
    "Virasoro": {
        "n_generators": 1,
        "generator_parity": "bosonic",
        "generator_weights": [2],
        "max_pole_order": 4,
        "curvature_formula": "c/2",
        "complementarity_sum": 26,
        "koszul_dual": "conjectured W_inf-related",
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "W3": {
        "n_generators": 2,
        "generator_parity": "bosonic",
        "generator_weights": [2, 3],
        "max_pole_order": 6,  # W_{(5)}W = c/3 (hextic pole)
        "curvature_formula": "5c/6",
        "complementarity_sum": 100,
        "koszul_dual": "conjectured",
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "E8": {
        "n_generators": 248,
        "generator_parity": "bosonic",
        "generator_weights": [1] * 248,
        "max_pole_order": 2,
        "curvature_formula": "(k+30)/60 * kappa",
        "complementarity_sum": 496,  # 2*248
        "koszul_dual": "E8_{-k-60}",
        "self_dual": True,  # even unimodular lattice
        "spectral_collapse": 1,
    },
    "B2": {
        "n_generators": 10,
        "generator_parity": "bosonic",
        "generator_weights": [1] * 10,
        "max_pole_order": 2,
        "curvature_formula": "(k+3)/6 * kappa",
        "complementarity_sum": 20,
        "koszul_dual": "B2_{-k-6}",
        "self_dual": True,
        "spectral_collapse": 1,
    },
    "G2": {
        "n_generators": 14,
        "generator_parity": "bosonic",
        "generator_weights": [1] * 14,
        "max_pole_order": 2,
        "curvature_formula": "(k+4)/8 * kappa",
        "complementarity_sum": 28,
        "koszul_dual": "G2_{-k-8}",
        "self_dual": True,
        "spectral_collapse": 1,
    },
}


# ---------------------------------------------------------------------------
# Cross-algebra queries
# ---------------------------------------------------------------------------

def algebras_by_property(property_name: str, value: object) -> List[str]:
    """Find all algebras matching a property value."""
    return [name for name, data in ALGEBRA_REGISTRY.items()
            if data.get(property_name) == value]


def curved_algebras() -> List[str]:
    """Algebras with nonzero curvature."""
    return [name for name, data in ALGEBRA_REGISTRY.items()
            if data["curvature_formula"] != "0"]


def uncurved_algebras() -> List[str]:
    """Algebras with zero curvature."""
    return [name for name, data in ALGEBRA_REGISTRY.items()
            if data["curvature_formula"] == "0"]


def kac_moody_algebras() -> List[str]:
    """Kac-Moody algebras (max pole = 2, weight 1 generators)."""
    return [name for name, data in ALGEBRA_REGISTRY.items()
            if data["max_pole_order"] == 2
            and all(w == 1 for w in data["generator_weights"])]


def self_dual_algebras() -> List[str]:
    """Algebras that are Koszul self-dual."""
    return [name for name, data in ALGEBRA_REGISTRY.items()
            if data.get("self_dual")]


def koszul_dual_pairs() -> List[tuple]:
    """Involutive Koszul dual pairs."""
    pairs = []
    seen = set()
    for name, data in ALGEBRA_REGISTRY.items():
        dual = data.get("koszul_dual", "")
        if dual in ALGEBRA_REGISTRY and name not in seen and dual not in seen:
            pairs.append((name, dual))
            seen.add(name)
            seen.add(dual)
    return pairs


def complementarity_table() -> Dict[str, int]:
    """All known complementarity sums c + c'."""
    return {name: data["complementarity_sum"]
            for name, data in ALGEBRA_REGISTRY.items()
            if data["complementarity_sum"] is not None}


def pole_order_table() -> Dict[str, int]:
    """Maximum pole orders by algebra."""
    return {name: data["max_pole_order"]
            for name, data in ALGEBRA_REGISTRY.items()}


# ---------------------------------------------------------------------------
# Structural comparisons
# ---------------------------------------------------------------------------

def bar_degree_2_dim(algebra: str) -> int:
    """Dimension of degree-2 bar complex (using top-degree OS forms).

    For n generators of the same weight:
    dim B^2 = n^2 * 1 (since OS^1(Conf_2) = 1-dimensional).
    """
    data = ALGEBRA_REGISTRY[algebra]
    n = data["n_generators"]
    return n * n  # * os_top_dim(2) = * 1


def curvature_sources(algebra: str) -> str:
    """Describe curvature sources for an algebra."""
    data = ALGEBRA_REGISTRY[algebra]
    pole = data["max_pole_order"]
    if pole <= 1:
        return "No curvature (max pole order <= 1)"
    elif pole == 2:
        return f"Curvature from double pole (Killing form): {data['curvature_formula']}"
    elif pole == 4:
        return f"Curvature from quartic pole: {data['curvature_formula']}"
    elif pole == 6:
        return f"Curvature from hextic pole (W_3): {data['curvature_formula']}"
    return f"Curvature: {data['curvature_formula']}"


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_cross_algebra():
    """Verify cross-algebra consistency."""
    results = {}

    # All algebras registered
    results["11 algebras"] = len(ALGEBRA_REGISTRY) == 11

    # Kac-Moody subset
    km = kac_moody_algebras()
    results["KM algebras correct"] = set(km) == {"Heisenberg", "sl2", "sl3", "E8", "B2", "G2"}

    # Curved/uncurved partition
    curved = set(curved_algebras())
    uncurved = set(uncurved_algebras())
    results["partition complete"] = len(curved) + len(uncurved) == 11
    results["partition disjoint"] = len(curved & uncurved) == 0
    results["free_fermion uncurved"] = "free_fermion" in uncurved
    results["betagamma uncurved"] = "betagamma" in uncurved
    results["bc uncurved"] = "bc" in uncurved
    results["Virasoro curved"] = "Virasoro" in curved

    # Self-dual
    sd = self_dual_algebras()
    results["KM self-dual"] = all(a in sd for a in ["sl2", "sl3", "E8", "B2", "G2"])
    results["Heisenberg NOT self-dual"] = "Heisenberg" not in sd

    # Complementarity
    ct = complementarity_table()
    results["Vir c+c'=26"] = ct["Virasoro"] == 26
    results["W3 c+c'=100"] = ct["W3"] == 100
    results["E8 c+c'=496"] = ct["E8"] == 496
    results["sl2 c+c'=6"] = ct["sl2"] == 6
    results["B2 c+c'=20"] = ct["B2"] == 20
    results["G2 c+c'=28"] = ct["G2"] == 28

    # KM complementarity = 2*dim
    for alg in ["sl2", "sl3", "E8", "B2", "G2"]:
        data = ALGEBRA_REGISTRY[alg]
        results[f"{alg}: c+c'=2*dim"] = ct[alg] == 2 * data["n_generators"]

    # Spectral collapse
    results["KM collapse E_1"] = all(
        ALGEBRA_REGISTRY[a]["spectral_collapse"] == 1 for a in km
    )

    # Koszul dual pairs
    pairs = koszul_dual_pairs()
    results["bg-bc pair"] = ("betagamma", "bc") in pairs or ("bc", "betagamma") in pairs

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("CROSS-ALGEBRA INTEGRATION: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_cross_algebra().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
