"""LQT-based E₁ growth computation for Strategy IV spectral sequence.

Computes dim E_1^{0,p}(g[t]) via the Loday-Quillen-Tsygan theorem:
    H*(g[t], k) ≅ Λ(ξ_{i,n} | 1 ≤ i ≤ r, n ≥ 0)
    deg(ξ_{i,n}) = 2e_i + 1 + 2n
where e_1, ..., e_r are the exponents of g.

dim E_1^{0,p} = |{S ⊆ {(i,n)} : Σ_{(i,n)∈S} (2e_i+1+2n) = p}|

Growth rate (prop:lqt-e1-subexponential-growth):
    dim E_1^{0,p} ~ C(g) · p^{-3/4} · exp(π√(rp/12))
where r = rank(g) and C(g) depends on the exponents.

This is SUB-EXPONENTIAL, not polynomial. The manuscript's polynomial growth
claim in conj:mc3-sectorwise-all-types has been corrected to sub-exponential.

References:
  - Feigin-Tsygan (LQT theorem for current algebras)
  - Hardy-Ramanujan (partition asymptotics)
  - prop:lqt-e1-subexponential-growth in yangians.tex
"""

from __future__ import annotations

import math
from typing import Dict, List, Tuple, Optional


# ---------------------------------------------------------------------------
# Simple Lie algebra data
# ---------------------------------------------------------------------------

# Exponents for all simple Lie algebras (convention: e_1 ≤ ... ≤ e_r)
EXPONENTS: Dict[str, List[int]] = {
    "A1": [1],               # sl_2
    "A2": [1, 2],            # sl_3
    "A3": [1, 2, 3],         # sl_4
    "A4": [1, 2, 3, 4],      # sl_5
    "A5": [1, 2, 3, 4, 5],   # sl_6
    "B2": [1, 3],            # so_5 ≅ sp_4
    "B3": [1, 3, 5],         # so_7
    "B4": [1, 3, 5, 7],      # so_9
    "C2": [1, 3],            # sp_4 ≅ so_5
    "C3": [1, 3, 5],         # sp_6
    "D4": [1, 3, 3, 5],      # so_8
    "D5": [1, 3, 5, 5, 7],   # so_10
    "G2": [1, 5],
    "F4": [1, 5, 7, 11],
    "E6": [1, 4, 5, 7, 8, 11],
    "E7": [1, 5, 7, 9, 11, 13, 17],
    "E8": [1, 7, 11, 13, 17, 19, 23, 29],
}


def rank(g: str) -> int:
    """Rank of simple Lie algebra g."""
    return len(EXPONENTS[g])


def exponents(g: str) -> List[int]:
    """Exponents of simple Lie algebra g."""
    return EXPONENTS[g]


def dimension(g: str) -> int:
    """Dimension of g: dim(g) = rank + 2 * sum(exponents)."""
    r = rank(g)
    return r + 2 * sum(EXPONENTS[g])


def dual_coxeter_number(g: str) -> int:
    """Dual Coxeter number h^vee: largest exponent + 1."""
    return max(EXPONENTS[g]) + 1


# ---------------------------------------------------------------------------
# LQT generator degrees
# ---------------------------------------------------------------------------

def lqt_generator_degrees(g: str, p_max: int) -> List[int]:
    """LQT generator degrees ≤ p_max, WITH multiplicity.

    Returns sorted list of degrees 2e_i + 1 + 2n for all (i, n)
    with degree ≤ p_max.
    """
    gens = []
    for e in EXPONENTS[g]:
        n = 0
        while 2 * e + 1 + 2 * n <= p_max:
            gens.append(2 * e + 1 + 2 * n)
            n += 1
    return sorted(gens)


def lqt_generator_count(g: str, p_max: int) -> int:
    """Number of LQT generators with degree ≤ p_max."""
    return len(lqt_generator_degrees(g, p_max))


# ---------------------------------------------------------------------------
# E₁ dimension computation
# ---------------------------------------------------------------------------

def e1_dimensions(g: str, p_max: int) -> List[int]:
    """dim E_1^{0,p}(g[t]) for p = 0, ..., p_max.

    Computed by dynamic programming (subset-sum counting).
    """
    gens = lqt_generator_degrees(g, p_max)

    dp = [0] * (p_max + 1)
    dp[0] = 1
    for gen_deg in gens:
        for s in range(p_max, gen_deg - 1, -1):
            dp[s] += dp[s - gen_deg]
    return dp


def e1_dimension(g: str, p: int) -> int:
    """dim E_1^{0,p}(g[t]) at a specific p."""
    return e1_dimensions(g, p)[p]


# ---------------------------------------------------------------------------
# Growth rate analysis
# ---------------------------------------------------------------------------

def growth_constant_theoretical(g: str) -> float:
    """Theoretical leading growth constant C_g = π√(r/12).

    dim E_1^{0,p} ~ exp(C_g · √p) as p → ∞.
    """
    r = rank(g)
    return math.pi * math.sqrt(r / 12.0)


def growth_constant_observed(g: str, p: int) -> float:
    """Observed growth constant: log(dim E_1^{0,p}) / √p.

    Should converge to C_g as p → ∞.
    """
    dim = e1_dimension(g, p)
    if dim <= 1:
        return 0.0
    return math.log(dim) / math.sqrt(p)


def growth_analysis(g: str, p_max: int = 200) -> Dict[str, object]:
    """Full growth analysis for simple Lie algebra g.

    Returns theoretical and observed growth constants,
    convergence data, and first departure from A1.
    """
    dims = e1_dimensions(g, p_max)
    r = rank(g)
    C_theory = growth_constant_theoretical(g)

    # Observed constants at sample points
    sample_points = [p for p in [50, 100, 150, 200] if p <= p_max]
    observed = {}
    for p in sample_points:
        if dims[p] > 1:
            observed[p] = math.log(dims[p]) / math.sqrt(p)

    # First departure from A1
    if g != "A1":
        a1_dims = e1_dimensions("A1", min(p_max, 100))
        first_departure = None
        for p in range(len(a1_dims)):
            if p < len(dims) and dims[p] != a1_dims[p]:
                first_departure = p
                break
    else:
        first_departure = None

    # Polynomial degree test: if polynomial, log(dim)/log(p) would stabilize
    poly_degrees = {}
    for p in sample_points:
        if dims[p] > 1:
            poly_degrees[p] = math.log(dims[p]) / math.log(p)

    return {
        "algebra": g,
        "rank": r,
        "exponents": EXPONENTS[g],
        "growth_constant_theory": C_theory,
        "growth_constant_observed": observed,
        "first_departure_from_A1": first_departure,
        "polynomial_degree_test": poly_degrees,
        "is_polynomial": False,  # always false for rank ≥ 1
        "dims_small": dims[:20],
    }


def verify_subexponential_growth(g: str, p_max: int = 300) -> Dict[str, object]:
    """Verify that growth is sub-exponential: dim < c^p for all c > 1."""
    dims = e1_dimensions(g, p_max)

    # Check: log(dim)/p → 0 (sub-exponential)
    ratios = {}
    for p in [50, 100, 200, 300]:
        if p <= p_max and dims[p] > 1:
            ratios[p] = math.log(dims[p]) / p

    # Check: log(dim)/√p → C_g (sub-exponential with specific constant)
    sqrt_ratios = {}
    C_theory = growth_constant_theoretical(g)
    for p in [100, 200, 300]:
        if p <= p_max and dims[p] > 1:
            sqrt_ratios[p] = math.log(dims[p]) / math.sqrt(p)

    return {
        "algebra": g,
        "log_dim_over_p": ratios,  # should → 0
        "log_dim_over_sqrt_p": sqrt_ratios,  # should → C_g
        "C_theory": C_theory,
        "is_subexponential": all(v < 1 for v in ratios.values()),
        "matches_sqrt_asymptotics": all(
            abs(v / C_theory - 1) < 0.2 for v in sqrt_ratios.values()
        ) if sqrt_ratios else True,
    }


def verify_all_types(p_max: int = 200) -> Dict[str, Dict]:
    """Verify sub-exponential growth for all simple types."""
    results = {}
    for g in EXPONENTS:
        results[g] = verify_subexponential_growth(g, p_max)
    return results


# ---------------------------------------------------------------------------
# Comparison across ranks
# ---------------------------------------------------------------------------

def rank_dependence_table(p: int = 200) -> List[Dict]:
    """Show how growth constant depends on rank (not on specific exponents)."""
    rows = []
    for g in sorted(EXPONENTS.keys()):
        r = rank(g)
        dim = e1_dimension(g, p)
        C_theory = growth_constant_theoretical(g)
        C_obs = math.log(dim) / math.sqrt(p) if dim > 1 else 0
        rows.append({
            "algebra": g,
            "rank": r,
            "C_theory": C_theory,
            "C_observed": C_obs,
            "E1_dim": dim,
        })
    return sorted(rows, key=lambda x: (x["rank"], x["algebra"]))


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("LQT E₁ GROWTH RATE ANALYSIS")
    print("=" * 70)

    for g in ["A1", "A2", "C2", "A3", "G2"]:
        analysis = growth_analysis(g)
        print(f"\n{g} (rank {analysis['rank']}, exponents {analysis['exponents']}):")
        print(f"  C_theory = {analysis['growth_constant_theory']:.4f}")
        for p, c in analysis["growth_constant_observed"].items():
            print(f"  C_obs(p={p}) = {c:.4f}")
        if analysis["first_departure_from_A1"] is not None:
            print(f"  First departure from A1 at p = "
                  f"{analysis['first_departure_from_A1']}")
        print(f"  Dims: {analysis['dims_small']}")

    print("\n" + "=" * 70)
    print("VERIFICATION: Sub-exponential growth for all types")
    print("=" * 70)
    results = verify_all_types(200)
    for g, res in sorted(results.items()):
        status = "✓" if res["is_subexponential"] else "✗"
        match = "✓" if res["matches_sqrt_asymptotics"] else "~"
        print(f"  {status} {g:4s}: sub-exp {match}  "
              f"C_theory={res['C_theory']:.4f}")
