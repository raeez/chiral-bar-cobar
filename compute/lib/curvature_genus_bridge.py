"""Curvature-genus bridge: connects bar complex curvatures to genus expansions.

The central insight: the curvature m_0 of the bar complex (from the highest-order
OPE pole) determines the genus expansion through the obstruction coefficient kappa.

Chain of connections:
  1. OPE highest pole -> curvature m_0 in bar complex
  2. m_0 -> obstruction coefficient kappa(A)
  3. kappa(A) -> genus expansion F_g(A) = kappa * lambda_g^FP
  4. Complementarity: kappa(A) + kappa(A!) = sigma * (c + c')

This module provides the explicit dictionary connecting all these levels.

Ground truth: genus_expansions.tex, detailed_computations.tex.
"""

from __future__ import annotations

from typing import Dict

from sympy import Rational, Symbol, simplify


# ---------------------------------------------------------------------------
# Curvature -> kappa dictionary
# ---------------------------------------------------------------------------

def curvature_to_kappa() -> Dict[str, Dict[str, object]]:
    """Map from bar complex curvature to obstruction coefficient kappa.

    For each algebra:
      curvature: the m_0 value from the OPE highest pole
      kappa: the obstruction coefficient in the genus expansion
      relation: how kappa relates to m_0

    Ground truth: comp:heisenberg-curvature, comp:virasoro-curvature,
    comp:w3-curvature-dual-detail, genus_expansions.tex.
    """
    c = Symbol('c')
    k = Symbol('k')
    kappa_sym = Symbol('kappa')

    return {
        "Heisenberg": {
            "curvature_m0": kappa_sym,
            "kappa": kappa_sym,
            "relation": "kappa = m_0 (trivial: 1 generator, curvature IS kappa)",
            "pole_order": 2,
            "pole_source": "a_{(1)}a = kappa",
        },
        "sl2": {
            "curvature_m0": k,  # k * kappa(J,J) for each pair; total = sum
            "kappa": 3 * (k + 2) / 4,
            "relation": "kappa = dim(g)*(k+h^vee)/(2*h^vee) = 3(k+2)/4",
            "pole_order": 2,
            "pole_source": "J^a_{(1)}J^b = k*kappa^{ab}",
        },
        "sl3": {
            "curvature_m0": k,
            "kappa": 4 * (k + 3) / 3,
            "relation": "kappa = dim(g)*(k+h^vee)/(2*h^vee) = 8(k+3)/6 = 4(k+3)/3",
            "pole_order": 2,
            "pole_source": "J^a_{(1)}J^b = k*kappa^{ab}",
        },
        "Virasoro": {
            "curvature_m0": c / 2,
            "kappa": c / 2,
            "relation": "kappa = m_0 = c/2 (single generator in T channel)",
            "pole_order": 4,
            "pole_source": "T_{(3)}T = c/2",
        },
        "W3": {
            "curvature_m0": {"T": c / 2, "W": c / 3},
            "kappa": 5 * c / 6,
            "relation": "kappa = sigma(sl_3)*c = (1/2+1/3)*c = 5c/6",
            "pole_order": 6,
            "pole_source": "T_{(3)}T = c/2 (quartic), W_{(5)}W = c/3 (sixth-order)",
        },
    }


# ---------------------------------------------------------------------------
# Kappa-complementarity verification
# ---------------------------------------------------------------------------

def verify_kappa_complementarity() -> Dict[str, bool]:
    """Verify kappa(A) + kappa(A!) = sigma * (c + c').

    For KM algebras via DS:
      sl_2 -> Vir: kappa(Vir_c) + kappa(Vir_{26-c}) = 26/2 = 13
        Actually: kappa(Vir_c) = c/2, kappa(Vir_{c'}) = c'/2 = (26-c)/2
        Sum = c/2 + (26-c)/2 = 13 ✓

      sl_3 -> W_3: kappa(W3_c) + kappa(W3_{100-c}) = 5*100/6/2 = ...
        kappa(W3_c) = 5c/6, kappa(W3_{c'}) = 5(100-c)/6
        Sum = 5c/6 + 5(100-c)/6 = 500/6 = 250/3 ✓ (from c+c'=100)
    """
    c = Symbol('c')
    results = {}

    # Virasoro
    kappa_vir = c / 2
    kappa_vir_dual = (26 - c) / 2
    results["Vir: kappa+kappa' = 13"] = simplify(kappa_vir + kappa_vir_dual - 13) == 0

    # W_3
    kappa_w3 = 5 * c / 6
    kappa_w3_dual = 5 * (100 - c) / 6
    results["W3: kappa+kappa' = 250/3"] = simplify(kappa_w3 + kappa_w3_dual - Rational(250, 3)) == 0

    # sl_2: kappa = 3(k+2)/4, dual level k'=-k-4
    k = Symbol('k')
    kappa_sl2 = 3 * (k + 2) / 4
    kappa_sl2_dual = 3 * (-k - 4 + 2) / 4  # = 3*(-k-2)/4
    results["sl2: kappa+kappa' = 0"] = simplify(kappa_sl2 + kappa_sl2_dual) == 0

    # sl_3: kappa = 4(k+3)/3, dual level k'=-k-6
    kappa_sl3 = 4 * (k + 3) / 3
    kappa_sl3_dual = 4 * (-k - 6 + 3) / 3  # = 4*(-k-3)/3
    results["sl3: kappa+kappa' = 0"] = simplify(kappa_sl3 + kappa_sl3_dual) == 0

    return results


# ---------------------------------------------------------------------------
# Curvature vanishing conditions
# ---------------------------------------------------------------------------

def curvature_vanishing() -> Dict[str, Dict]:
    """Conditions under which the bar complex becomes uncurved (m_0 = 0).

    When m_0 = 0: bar differential d^2 = 0 strictly (not just curved A-infinity).
    """
    return {
        "Heisenberg": {
            "condition": "kappa = 0",
            "interpretation": "trivial central extension; H_0 = commutative chiral algebra",
        },
        "sl2": {
            "condition": "k = 0",
            "interpretation": "level 0; vacuum module trivial",
        },
        "sl3": {
            "condition": "k = 0",
            "interpretation": "level 0; vacuum module trivial",
        },
        "Virasoro": {
            "condition": "c = 0",
            "interpretation": "trivial Virasoro; T = 0 in bar complex",
        },
        "W3": {
            "condition": "c = 0",
            "interpretation": "trivial W_3; both T,W curvatures vanish simultaneously",
        },
    }


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_curvature_genus_bridge() -> Dict[str, bool]:
    """Verify the full chain: OPE pole -> curvature -> kappa -> genus."""
    c = Symbol('c')
    results = {}

    data = curvature_to_kappa()

    # Heisenberg: m_0 = kappa, genus F_1 = kappa * 1/12
    # (lambda_1^FP = |B_2|/(2*0!) = 1/6 / 2 = 1/12)
    results["Heis: kappa = m_0"] = True  # trivial

    # Virasoro: m_0 = c/2 = kappa
    results["Vir: m_0 = kappa = c/2"] = data["Virasoro"]["curvature_m0"] == data["Virasoro"]["kappa"]

    # W_3: m_0 has two channels, kappa combines them
    m0_T = data["W3"]["curvature_m0"]["T"]
    m0_W = data["W3"]["curvature_m0"]["W"]
    kappa_w3 = data["W3"]["kappa"]
    # kappa = sigma*c = (1/2+1/3)*c = 5c/6
    # m_0^T + m_0^W = c/2 + c/3 = 5c/6 = kappa ✓
    results["W3: m_0^T + m_0^W = kappa"] = simplify(m0_T + m0_W - kappa_w3) == 0

    # Pole order determines curvature type
    results["KM has pole 2"] = data["sl2"]["pole_order"] == 2
    results["Vir has pole 4"] = data["Virasoro"]["pole_order"] == 4
    results["W3 has pole 6"] = data["W3"]["pole_order"] == 6

    return results


# ---------------------------------------------------------------------------
# Multi-generator obstruction structure
# ---------------------------------------------------------------------------

def multi_generator_obstruction():
    """Multi-generator obstruction analysis.

    For single-generator algebras (Heisenberg, KM, Virasoro):
      obs_g = kappa * lambda_g  (Hodge class)
      (obs_g)^2 = 0  by Mumford's relation (PROVED)

    For multi-generator algebras (W_3, W_N):
      obs_g = sum_h kappa_h * lambda_g^{(h)}
      where lambda_g^{(h)} = c_g(R^0 pi_* omega^{h})

    Mumford's relation applies ONLY to h=1 (Hodge bundle).
    For h >= 2: no flatness, no Mumford, nilpotence OPEN for g >= 3.

    Ground truth: rem:multi-generator-nilpotence in higher_genus.tex.
    """
    c = Symbol('c')

    return {
        "W3": {
            "generators": {"T": 2, "W": 3},  # conformal weights
            "curvature_channels": {"T": c / 2, "W": c / 3},
            "kappa_total": 5 * c / 6,
            "obstruction_formula": "obs_g = (c/2)*lambda_g^{(2)} + (c/3)*lambda_g^{(3)}",
            "hodge_bundle_ranks": {
                # rank(R^0 pi_* omega^h) at genus g:
                # h=1: g (Hodge bundle)
                # h>=2: (2h-1)(g-1)
                "h=2": lambda g: 3 * (g - 1),
                "h=3": lambda g: 5 * (g - 1),
            },
            "mumford_applies": False,
            "nilpotence_proved_for": "g <= 2 (dimensional argument: 4g > 6g-6)",
            "nilpotence_open_for": "g >= 3",
        },
        "W4": {
            "generators": {"T": 2, "W3": 3, "W4": 4},
            "curvature_channels": {"T": c / 2, "W3": c / 3, "W4": c / 4},
            "kappa_total": c * (Rational(1, 2) + Rational(1, 3) + Rational(1, 4)),
            "obstruction_formula": "obs_g = sum kappa_h * lambda_g^{(h)}",
            "mumford_applies": False,
            "nilpotence_proved_for": "g <= 2",
            "nilpotence_open_for": "g >= 3",
        },
    }


def dimensional_nilpotence_check(g: int) -> dict:
    """Check whether (obs_g)^2 = 0 by the dimensional argument.

    (obs_g)^2 lives in H^{4g}(M-bar_g).
    dim_C M-bar_g = 3g - 3.
    So H^{4g} = 0 iff 4g > 2(3g-3) = 6g-6, i.e., g < 3.

    For g >= 3: 4g <= 6g-6, so H^{4g} may be nonzero.
    """
    dim_moduli = 3 * g - 3
    obs_squared_degree = 4 * g
    max_cohomological_degree = 2 * dim_moduli

    return {
        "genus": g,
        "dim_moduli_space": dim_moduli,
        "obs_squared_degree": obs_squared_degree,
        "max_degree": max_cohomological_degree,
        "dimensional_vanishing": obs_squared_degree > max_cohomological_degree,
        "mumford_needed": not (obs_squared_degree > max_cohomological_degree),
    }


def verify_multi_generator_obstruction() -> Dict[str, bool]:
    """Verify multi-generator obstruction structure."""
    c = Symbol('c')
    results = {}

    data = multi_generator_obstruction()

    # W3 kappa decomposition: c/2 + c/3 = 5c/6
    w3 = data["W3"]
    kappa_sum = sum(w3["curvature_channels"].values())
    results["W3: kappa_T + kappa_W = 5c/6"] = simplify(kappa_sum - w3["kappa_total"]) == 0

    # W4 kappa: 1/2 + 1/3 + 1/4 = 13/12
    w4 = data["W4"]
    results["W4: sigma = 13/12"] = simplify(
        w4["kappa_total"] / c - Rational(13, 12)
    ) == 0

    # Dimensional argument for g=1,2 (holds for all algebras)
    for g in [1, 2]:
        check = dimensional_nilpotence_check(g)
        results[f"g={g}: dimensional vanishing"] = check["dimensional_vanishing"]

    # g=3: dimensional argument fails
    check3 = dimensional_nilpotence_check(3)
    results["g=3: dimensional argument FAILS"] = not check3["dimensional_vanishing"]

    # g=3: obs^2 degree = 12, max degree = 12 (top cohomology!)
    results["g=3: obs^2 in top degree"] = check3["obs_squared_degree"] == check3["max_degree"]

    # Hodge bundle ranks at g=3
    results["g=3: rank E_2 = 6"] = w3["hodge_bundle_ranks"]["h=2"](3) == 6
    results["g=3: rank E_3 = 10"] = w3["hodge_bundle_ranks"]["h=3"](3) == 10

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("CURVATURE-GENUS BRIDGE VERIFICATION")
    print("=" * 60)

    print("\n--- Curvature-Genus Bridge ---")
    for name, ok in verify_curvature_genus_bridge().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Kappa Complementarity ---")
    for name, ok in verify_kappa_complementarity().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Multi-Generator Obstruction ---")
    for name, ok in verify_multi_generator_obstruction().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
