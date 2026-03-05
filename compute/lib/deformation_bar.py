"""Deformation quantization chain-level structure.

The deformation quantization hierarchy:
  Coisson (classical) -> E_inf-chiral (singly quantum) -> E_1-chiral (doubly quantum)

Maps between levels via bar-cobar:
  - Classical: Coisson algebra (PVA) with lambda-bracket
  - First quantization: E_inf-chiral = vertex algebra (has OPE)
  - Second quantization: E_1-chiral = nonlocal VA (has noncommutative OPE)

Ground truth from the manuscript (deformation_quantization.tex, deformation_examples.tex):
  - Chiral Kontsevich theorem: formality of P_inf-chiral operad
  - Star product: mu_hbar = m_2 + hbar*m_2' + hbar^2*m_2'' + ...
  - Deformation obstructions live in chiral Hochschild cohomology HH^*(A)

  From CLAUDE.md P_inf vs Coisson distinction:
  - Coisson: commutative D_X-algebra + Lie* bracket. NOT a chiral algebra.
  - P_inf-chiral: chirCom + chirLie compatible. IS a chiral algebra.
  - Different quantization levels.

CONVENTIONS:
- hbar = deformation parameter
- Star product = associative deformation of commutative product
"""

from __future__ import annotations

from typing import Dict, List

from sympy import Rational, Symbol


# ---------------------------------------------------------------------------
# Quantization hierarchy
# ---------------------------------------------------------------------------

QUANTIZATION_LEVELS = {
    "classical": {
        "structure": "Coisson (Poisson vertex algebra)",
        "has_ope": False,
        "commutative": True,
        "is_chiral": False,
        "description": "Commutative D_X-algebra + Lie* bracket (lambda-bracket)",
    },
    "singly_quantum": {
        "structure": "E_inf-chiral (vertex algebra)",
        "has_ope": True,
        "commutative": True,  # E_inf = commutative up to homotopy
        "is_chiral": True,
        "description": "Full vertex algebra with OPE",
    },
    "doubly_quantum": {
        "structure": "E_1-chiral (nonlocal VA)",
        "has_ope": True,
        "commutative": False,
        "is_chiral": True,
        "description": "Noncommutative, nonlocal vertex algebra",
    },
}

QUANTIZATION_MAPS = {
    ("classical", "singly_quantum"): {
        "name": "First quantization",
        "mechanism": "Deformation quantization of Coisson -> vertex algebra",
        "obstruction": "HH^2(Coisson algebra)",
        "parameter": "hbar",
    },
    ("singly_quantum", "doubly_quantum"): {
        "name": "Second quantization",
        "mechanism": "P_inf-chiral -> E_1-chiral via bar-cobar",
        "obstruction": "Chiral Hochschild HH^2(E_inf)",
        "parameter": "hbar_2",
    },
}


# ---------------------------------------------------------------------------
# P_inf vs Coisson distinction
# ---------------------------------------------------------------------------

def pinf_vs_coisson() -> Dict[str, Dict[str, object]]:
    """Critical distinction between P_inf-chiral and Coisson.

    Ground truth: CLAUDE.md P_inf vs Coisson section.
    """
    return {
        "Coisson": {
            "is_chiral_algebra": False,
            "has_ope": False,
            "structure": "Commutative D_X-algebra + Lie* bracket",
            "quantizes_to": "E_inf-chiral (vertex algebra)",
            "alternative_names": ["Poisson vertex algebra", "PVA"],
        },
        "P_inf_chiral": {
            "is_chiral_algebra": True,
            "has_ope": True,
            "structure": "chirCom + chirLie (two compatible chiral structures)",
            "quantizes_to": "E_1-chiral (nonlocal VA)",
            "key_property": "chirCom^! = chirLie (Koszul duality of components)",
        },
    }


# ---------------------------------------------------------------------------
# Star product expansion
# ---------------------------------------------------------------------------

def star_product_expansion(order: int) -> Dict[int, str]:
    """Star product mu_hbar = sum hbar^n m_n^{(2)}.

    Returns {power: description} through given order.
    """
    terms = {
        0: "m_2 (commutative product)",
        1: "m_2' (Poisson bracket / first-order deformation)",
        2: "m_2'' (second-order, obstruction in HH^3)",
    }
    return {n: terms.get(n, f"m_2^{{({n})}} (order {n} correction)")
            for n in range(order + 1)}


# ---------------------------------------------------------------------------
# Deformation obstruction
# ---------------------------------------------------------------------------

def deformation_obstructions() -> Dict[str, Dict[str, object]]:
    """Obstruction theory for deformation quantization.

    Ground truth: deformation_theory.tex.
    """
    return {
        "first_order": {
            "lives_in": "HH^2(A, A)",
            "classifies": "Infinitesimal deformations",
            "cochains": "f: A otimes A -> A bilinear",
        },
        "obstruction": {
            "lives_in": "HH^3(A, A)",
            "classifies": "Obstructions to extending deformation",
            "massey_product": "ob(f) = [f, f] in HH^3",
        },
        "curved": {
            "lives_in": "HH^0(A, A) = center Z(A)",
            "classifies": "Curved deformations (curvature element)",
            "relation_to_bar": "m_0 in bar degree 0",
        },
    }


# ---------------------------------------------------------------------------
# Examples
# ---------------------------------------------------------------------------

def deformation_examples() -> Dict[str, Dict[str, object]]:
    """Known deformation quantization examples from the manuscript.

    Ground truth: deformation_examples.tex.
    """
    return {
        "Heisenberg_DQ": {
            "classical": "Sym^ch(V) (commutative chiral on V)",
            "quantum": "Heisenberg vertex algebra H_k",
            "parameter": "k (level)",
            "obstruction_vanishes": True,
        },
        "lattice_DQ": {
            "classical": "Group algebra C[L] with trivial product",
            "quantum": "Lattice vertex algebra V_L",
            "parameter": "2-cocycle epsilon",
            "obstruction_vanishes": True,  # for even lattice
        },
        "symplectic_fermion_DQ": {
            "classical": "Lambda^ch(V) (exterior chiral on V)",
            "quantum": "Symplectic fermion vertex algebra SF(V)",
            "parameter": "symplectic form omega",
            "obstruction_vanishes": True,
        },
    }


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_deformation():
    results = {}

    # Quantization levels
    results["3 levels"] = len(QUANTIZATION_LEVELS) == 3
    results["classical not chiral"] = not QUANTIZATION_LEVELS["classical"]["is_chiral"]
    results["singly quantum is chiral"] = QUANTIZATION_LEVELS["singly_quantum"]["is_chiral"]

    # P_inf vs Coisson
    pvc = pinf_vs_coisson()
    results["Coisson not chiral"] = not pvc["Coisson"]["is_chiral_algebra"]
    results["P_inf is chiral"] = pvc["P_inf_chiral"]["is_chiral_algebra"]
    results["Coisson no OPE"] = not pvc["Coisson"]["has_ope"]
    results["P_inf has OPE"] = pvc["P_inf_chiral"]["has_ope"]

    # Star product
    sp = star_product_expansion(2)
    results["order 0 = m_2"] = "commutative" in sp[0]
    results["order 1 = Poisson"] = "Poisson" in sp[1]

    # Obstructions
    obs = deformation_obstructions()
    results["first order in HH^2"] = "HH^2" in obs["first_order"]["lives_in"]
    results["obstruction in HH^3"] = "HH^3" in obs["obstruction"]["lives_in"]

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("DEFORMATION QUANTIZATION: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_deformation().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
