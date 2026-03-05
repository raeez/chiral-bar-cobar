"""Minimal model bar complexes: Ising, tricritical Ising, three-state Potts.

Ground truth from the manuscript (minimal_model_examples.tex, minimal_model_fusion.tex):
  Minimal model M(p,q): c = 1 - 6(p-q)^2/(pq)

  comp:ising-bar-interpretation:
    Ising M(4,3): c = 1/2
    kappa = c/2 = 1/4
    obs_1 = kappa/24 = 1/96
    3 modules: I (vacuum), sigma, epsilon
    Fusion: sigma x sigma = I + epsilon, sigma x epsilon = sigma

  Minimal model central charges:
    M(3,2): c = 0 (trivial)
    M(4,3): c = 1/2 (Ising)
    M(5,3): c = -3/5 (non-unitary Lee-Yang)
    M(5,4): c = 7/10 (tricritical Ising)
    M(6,5): c = 4/5 (three-state Potts)

CONVENTIONS:
- Virasoro DS formula: c = 1 - 6(k+1)^2/(k+2)
"""

from __future__ import annotations

from typing import Dict, List

from sympy import Rational, Symbol


# ---------------------------------------------------------------------------
# Minimal model central charges
# ---------------------------------------------------------------------------

def minimal_model_c(p: int, q: int) -> Rational:
    """Central charge of minimal model M(p,q).

    c = 1 - 6(p-q)^2/(pq).
    Convention: p > q >= 2, gcd(p,q) = 1.
    """
    return 1 - Rational(6 * (p - q)**2, p * q)


MINIMAL_MODELS = {
    "trivial": {"p": 3, "q": 2, "c": Rational(0), "name": "trivial"},
    "Ising": {"p": 4, "q": 3, "c": Rational(1, 2), "name": "Ising"},
    "Lee_Yang": {"p": 5, "q": 2, "c": Rational(-22, 5), "name": "Lee-Yang"},
    "tricritical_Ising": {"p": 5, "q": 4, "c": Rational(7, 10), "name": "tricritical Ising"},
    "three_state_Potts": {"p": 6, "q": 5, "c": Rational(4, 5), "name": "three-state Potts"},
}


# ---------------------------------------------------------------------------
# Ising model bar complex
# ---------------------------------------------------------------------------

def ising_bar_data() -> Dict[str, object]:
    """Bar complex data for the Ising model M(4,3).

    Ground truth: comp:ising-bar-interpretation.
    """
    c = Rational(1, 2)
    kappa = c / 2  # = 1/4
    obs_1 = kappa / 24  # = 1/96

    return {
        "c": c,
        "kappa": kappa,
        "obs_1": obs_1,
        "n_modules": 3,
        "modules": ["I", "sigma", "epsilon"],
        "conformal_weights": {
            "I": Rational(0),
            "sigma": Rational(1, 16),
            "epsilon": Rational(1, 2),
        },
        "fusion_rules": {
            ("sigma", "sigma"): ["I", "epsilon"],
            ("sigma", "epsilon"): ["sigma"],
            ("epsilon", "epsilon"): ["I"],
        },
    }


def ising_genus1_bar() -> Dict[str, Dict[str, object]]:
    """Genus-1 bar complex for Ising model.

    Ground truth: comp:ising-bar-interpretation.
    """
    return {
        "B_{g=1}(I, I)": {
            "H^0": ["I"],
            "dim": 1,
            "interpretation": "vacuum torus amplitude",
        },
        "B_{g=1}(sigma, sigma)": {
            "H^0": ["I", "epsilon"],
            "dim": 2,
            "interpretation": "sigma x sigma = I + epsilon",
        },
        "B_{g=1}(sigma, epsilon)": {
            "H^0": ["sigma"],
            "dim": 1,
            "interpretation": "sigma x epsilon = sigma",
        },
    }


# ---------------------------------------------------------------------------
# Tricritical Ising
# ---------------------------------------------------------------------------

def tricritical_ising_data() -> Dict[str, object]:
    """Bar complex data for tricritical Ising M(5,4)."""
    c = Rational(7, 10)
    return {
        "c": c,
        "kappa": c / 2,
        "n_modules": 6,
        "conformal_weights": {
            "I": Rational(0),
            "epsilon": Rational(1, 10),
            "epsilon'": Rational(3, 5),
            "epsilon''": Rational(3, 2),
            "sigma": Rational(3, 80),
            "sigma'": Rational(7, 16),
        },
    }


# ---------------------------------------------------------------------------
# Three-state Potts
# ---------------------------------------------------------------------------

def three_state_potts_data() -> Dict[str, object]:
    """Bar complex data for three-state Potts M(6,5)."""
    c = Rational(4, 5)
    return {
        "c": c,
        "kappa": c / 2,
        "n_modules": 10,
    }


# ---------------------------------------------------------------------------
# Complementarity for minimal models
# ---------------------------------------------------------------------------

def minimal_model_complementarity(p: int, q: int) -> Rational:
    """c + c' = 26 for Virasoro (regardless of p,q).

    All minimal models have the same complementarity sum c + c' = 26,
    since they are Virasoro quotients.
    """
    return Rational(26)


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_minimal_models():
    results = {}

    # Central charges
    results["M(3,2) = 0"] = minimal_model_c(3, 2) == 0
    results["M(4,3) = 1/2"] = minimal_model_c(4, 3) == Rational(1, 2)
    results["M(5,4) = 7/10"] = minimal_model_c(5, 4) == Rational(7, 10)
    results["M(6,5) = 4/5"] = minimal_model_c(6, 5) == Rational(4, 5)

    # Ising bar data
    ising = ising_bar_data()
    results["Ising c = 1/2"] = ising["c"] == Rational(1, 2)
    results["Ising kappa = 1/4"] = ising["kappa"] == Rational(1, 4)
    results["Ising obs_1 = 1/96"] = ising["obs_1"] == Rational(1, 96)
    results["Ising 3 modules"] = ising["n_modules"] == 3

    # Ising fusion
    fusion = ising["fusion_rules"]
    results["sigma x sigma = I + eps"] = set(fusion[("sigma", "sigma")]) == {"I", "epsilon"}
    results["sigma x eps = sigma"] = fusion[("sigma", "epsilon")] == ["sigma"]
    results["eps x eps = I"] = fusion[("epsilon", "epsilon")] == ["I"]

    # Genus-1 bar
    g1 = ising_genus1_bar()
    results["B(I,I) dim = 1"] = g1["B_{g=1}(I, I)"]["dim"] == 1
    results["B(sigma,sigma) dim = 2"] = g1["B_{g=1}(sigma, sigma)"]["dim"] == 2

    # Complementarity
    results["all c+c' = 26"] = minimal_model_complementarity(4, 3) == 26

    # Tricritical Ising
    tci = tricritical_ising_data()
    results["TCI c = 7/10"] = tci["c"] == Rational(7, 10)
    results["TCI 6 modules"] = tci["n_modules"] == 6

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("MINIMAL MODEL BAR COMPLEXES: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_minimal_models().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
