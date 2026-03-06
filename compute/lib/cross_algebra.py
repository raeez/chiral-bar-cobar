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
        "curvature_m0": "k",            # m_0 = k (double pole J_{(1)}J = k; manuscript: free_fields.tex)
        "kappa_formula": "k",          # kappa = k (the level; manuscript: free_fields.tex:1235)
        "complementarity_sum": None,  # no DS reduction
        "koszul_dual": "Sym^ch(V*)",
        "self_dual": False,
        "spectral_collapse": 1,
    },
    # NOTE: The free fermion entry here describes the bc system (b, c generators),
    # which is a 2-generator fermionic system.  In bar_complex.py, the free fermion
    # algebra uses 1 generator (psi of weight 1/2) — that is the single free fermion
    # field.  Both are standard usages; the bc system is the pair (b, c) of conjugate
    # fermions, while the single free fermion psi is the simplest fermionic chiral algebra.
    "free_fermion": {
        "n_generators": 2,
        "generator_parity": "fermionic",
        "generator_weights": [Rational(1, 2), Rational(1, 2)],
        "max_pole_order": 1,
        "curvature_m0": "0",
        "kappa_formula": "0",
        "complementarity_sum": None,
        "koszul_dual": "beta_gamma",  # F^! = beta-gamma (bc/beta-gamma duality, VF014)
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "beta_gamma": {
        "n_generators": 2,
        "generator_parity": "bosonic",
        "generator_weights": [0, 1],
        "max_pole_order": 1,
        "curvature_m0": "0",
        "kappa_formula": "0",
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
        "curvature_m0": "0",
        "kappa_formula": "0",
        "complementarity_sum": None,
        "koszul_dual": "beta_gamma",
        "self_dual": False,
        "spectral_collapse": 2,
    },
    "sl2": {
        "n_generators": 3,
        "generator_parity": "bosonic",
        "generator_weights": [1, 1, 1],
        "max_pole_order": 2,
        "curvature_m0": "k",           # m_0 = level k (from double pole)
        "kappa_formula": "3*(k+2)/4",  # obstruction coefficient kappa = dim*(k+h*)/(2h*)
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
        "curvature_m0": "k",           # m_0 = level k
        "kappa_formula": "8*(k+3)/6",  # = 4*(k+3)/3
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
        "curvature_m0": "c/2",         # m_0 = c/2 (from quartic pole T_{(3)}T)
        "kappa_formula": "c/2",        # kappa = c/2 (same as m_0 for Virasoro)
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
        "curvature_m0": "c/2 + c/3",   # m_0^(T) = c/2, m_0^(W) = c/3
        "kappa_formula": "5c/6",       # kappa = c/2 + c/3 = 5c/6
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
        "curvature_m0": "k",           # m_0 = level k
        "kappa_formula": "248*(k+30)/60",  # = 62*(k+30)/15
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
        "curvature_m0": "k",           # m_0 = level k
        "kappa_formula": "10*(k+3)/6",  # = 5*(k+3)/3
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
        "curvature_m0": "k",           # m_0 = level k
        "kappa_formula": "14*(k+4)/8",  # = 7*(k+4)/4
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
            if data["curvature_m0"] != "0"]


def uncurved_algebras() -> List[str]:
    """Algebras with zero curvature."""
    return [name for name, data in ALGEBRA_REGISTRY.items()
            if data["curvature_m0"] == "0"]


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
    m0 = data["curvature_m0"]
    kap = data["kappa_formula"]
    if pole <= 1:
        return "No curvature (max pole order <= 1)"
    elif pole == 2:
        return f"Curvature m_0={m0} from double pole (Killing form), kappa={kap}"
    elif pole == 4:
        return f"Curvature m_0={m0} from quartic pole, kappa={kap}"
    elif pole == 6:
        return f"Curvature m_0={m0} from hextic pole (W_3), kappa={kap}"
    return f"Curvature m_0={m0}, kappa={kap}"


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_cross_algebra():
    """Verify cross-algebra consistency.

    NOTE: These checks compare hardcoded registry values against hardcoded
    expected values, so they function as regression tests (detecting accidental
    edits to the registry) rather than independent mathematical verification.
    """
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
    results["beta_gamma uncurved"] = "beta_gamma" in uncurved
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

    # Koszul duality chain: free_fermion -> beta_gamma -> bc -> beta_gamma
    results["F! = beta_gamma"] = ALGEBRA_REGISTRY["free_fermion"]["koszul_dual"] == "beta_gamma"
    results["bg! = bc"] = ALGEBRA_REGISTRY["beta_gamma"]["koszul_dual"] == "bc"
    results["bc! = bg"] = ALGEBRA_REGISTRY["bc"]["koszul_dual"] == "beta_gamma"

    return results


def verify_registry_consistency() -> Dict[str, bool]:
    """Cross-check ALGEBRA_REGISTRY against KNOWN_BAR_DIMS, KOSZUL_PAIRS,
    and genus_expansion kappa formulas. Catches data drift between registries."""
    from compute.lib.bar_complex import KNOWN_BAR_DIMS
    from compute.lib.koszul_pairs import KOSZUL_PAIRS
    results = {}

    # 1. Every algebra with known bar dims is in the registry
    skip = {"Yangian_sl2"}  # not in ALGEBRA_REGISTRY (separate module)
    for alg in KNOWN_BAR_DIMS:
        if alg in skip:
            continue
        results[f"bar_dims:{alg} in registry"] = alg in ALGEBRA_REGISTRY

    # 2. Koszul dual consistency: ALGEBRA_REGISTRY vs KOSZUL_PAIRS
    # bg-bc pair
    results["koszul: bg->bc consistent"] = (
        ALGEBRA_REGISTRY["beta_gamma"]["koszul_dual"] == "bc"
        and KOSZUL_PAIRS["beta_gamma_bc"]["A"] == "beta_gamma"
    )
    results["koszul: Heis not self-dual"] = (
        not ALGEBRA_REGISTRY["Heisenberg"]["self_dual"]
        and not KOSZUL_PAIRS["Heisenberg_Symch"]["self_dual"]
    )

    # 3. KM kappa complementarity: kappa(A) + kappa(A!) = 0 (identically in k)
    # The complementarity_sum in ALGEBRA_REGISTRY is c + c' (central charges), not kappa + kappa'.
    from compute.lib.lie_algebra import kappa_km as kappa_fn, ff_dual_level as ff_fn
    from sympy import Symbol, simplify
    k = Symbol('k')
    for typ, rank, name in [("A", 1, "sl2"), ("A", 2, "sl3"), ("G", 2, "G2"), ("B", 2, "B2")]:
        kap = kappa_fn(typ, rank, k)
        kp = ff_fn(typ, rank, k)
        kap_dual = kappa_fn(typ, rank, kp)
        total = simplify(kap + kap_dual)
        results[f"kappa:{name} kappa+kappa'=0"] = (total == 0)

    # 4. Spectral collapse pages match spectral_sequence.py
    from compute.lib.spectral_sequence import spectral_sequence_collapse
    for alg in ["Heisenberg", "sl2", "sl3", "Virasoro"]:
        ss_name = alg
        reg_collapse = ALGEBRA_REGISTRY[alg]["spectral_collapse"]
        ss_collapse = spectral_sequence_collapse(ss_name).get("collapse_page", None)
        if ss_collapse is not None:
            results[f"collapse:{alg} consistent"] = (reg_collapse == ss_collapse)

    return results


def unified_algebra_data(algebra: str) -> Dict:
    """Unified view of an algebra from all registries.

    Combines ALGEBRA_REGISTRY metadata, KNOWN_BAR_DIMS, and
    computed kappa values into a single dict.
    """
    from compute.lib.bar_complex import KNOWN_BAR_DIMS, CONJECTURAL_BAR_DIMS
    data = dict(ALGEBRA_REGISTRY.get(algebra, {}))
    data["name"] = algebra

    # Bar cohomology
    bar_dims = KNOWN_BAR_DIMS.get(algebra, {})
    conj_degs = CONJECTURAL_BAR_DIMS.get(algebra, set())
    data["bar_cohomology"] = bar_dims
    data["conjectural_degrees"] = conj_degs

    return data


if __name__ == "__main__":
    print("=" * 60)
    print("CROSS-ALGEBRA INTEGRATION: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_cross_algebra().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    print("REGISTRY CONSISTENCY:")
    for name, ok in verify_registry_consistency().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
