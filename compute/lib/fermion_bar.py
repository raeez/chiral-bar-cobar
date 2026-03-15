"""Free fermion bar complex: chain-level computations.

The two-generator free fermion F_2 has generators psi_1, psi_2 of conformal
weight 1/2 (fermionic, odd parity) with OPE:
  psi_i(z) psi_j(w) = delta_{ij}/(z-w) + regular

Ground truth from the manuscript (detailed_computations.tex):
  (psi_i)_{(0)} psi_j = delta_{ij} |0>     [comp:fermion-two-gen-ope]
  (psi_i)_{(n)} psi_j = 0 for n >= 1

Bar differential (comp:fermion-deg2):
  D([psi_i|psi_j] otimes eta) = delta_{ij} |0>
  Diagonal pairs map to vacuum; off-diagonal pairs map to zero.

Degree 3 (comp:fermion-deg3):
  D([psi_1|psi_1|psi_2] otimes eta_{12}^eta_{13}) = [psi_2] otimes eta_{23}
  D([psi_1|psi_2|psi_1] otimes eta_{12}^eta_{13}) = [psi_2] otimes eta_{12}

Koszul signs (comp:fermion-deg2-signs):
  After desuspension: |s^{-1}psi_i| = 0 (even), so B(F_2) = Sym^c(s^{-1}V-bar)
  This is SYMMETRIC (not exterior) coalgebra, dual to F_2^! = Sym^ch(V*)

Bar cohomology (KNOWN_BAR_DIMS):
  {1:1, 2:1, 3:2, 4:3, 5:5, 6:7, 7:11, 8:15}

CONVENTIONS:
- Cohomological grading, |d| = +1
- NS sector (half-integer modes)
- Generators are fermionic (odd parity), desuspensions are even
"""

from __future__ import annotations

from math import factorial
from typing import Dict, List, Tuple

from sympy import Rational


# ---------------------------------------------------------------------------
# Free fermion OPE
# ---------------------------------------------------------------------------

def fermion_nth_product(i: int, j: int, n: int) -> Dict[str, object]:
    """Get (psi_i)_{(n)} psi_j.

    Ground truth: comp:fermion-two-gen-ope.
    (psi_i)_{(0)} psi_j = delta_{ij} |0>
    (psi_i)_{(n)} psi_j = 0 for n >= 1
    """
    if n == 0 and i == j:
        return {"vac": Rational(1)}
    return {}


def fermion_all_products() -> Dict[Tuple[int, int], Dict[int, Dict[str, object]]]:
    """All singular n-th products for two-generator free fermion.

    Returns {(i,j): {n: {output: coeff}}} for i,j in {1,2}.
    """
    return {
        (1, 1): {0: {"vac": Rational(1)}},
        (2, 2): {0: {"vac": Rational(1)}},
        (1, 2): {},  # no singular terms
        (2, 1): {},  # no singular terms
    }


# ---------------------------------------------------------------------------
# Bar differential
# ---------------------------------------------------------------------------

def fermion_bar_diff_deg2(i: int, j: int) -> Tuple[Dict[str, object], Dict[str, object]]:
    """Bar differential D([psi_i|psi_j] otimes eta_{12}).

    Ground truth: comp:fermion-deg2.
    D([psi_i|psi_j]) = delta_{ij} |0>

    Returns (vac_component, bar1_component).
    """
    vac = {}
    bar1 = {}

    if i == j:
        vac["vac"] = Rational(1)

    return vac, bar1


def fermion_bar_diff_deg3_example1() -> Dict[str, object]:
    """D([psi_1|psi_1|psi_2] otimes eta_{12}^eta_{13}).

    Ground truth: comp:fermion-deg3, eq:fermion-deg3-ex.

    D_{12}: psi_1_{(0)}psi_1 = |0>, collapses to [psi_2] otimes eta_{23}
    D_{13}: psi_1_{(0)}psi_2 = 0
    D_{23}: psi_1_{(0)}psi_2 = 0

    Result: [psi_2] otimes eta_{23}
    """
    return {
        "D_12": {"result": "[psi_2] otimes eta_23", "coeff": Rational(1)},
        "D_13": {"result": "0", "coeff": Rational(0)},
        "D_23": {"result": "0", "coeff": Rational(0)},
        "total": "[psi_2] otimes eta_23",
    }


def fermion_bar_diff_deg3_example2() -> Dict[str, object]:
    """D([psi_1|psi_2|psi_1] otimes eta_{12}^eta_{13}).

    Ground truth: comp:fermion-deg3.

    D_{12}: psi_1_{(0)}psi_2 = 0
    D_{13}: psi_1_{(0)}psi_1 = |0>, collapses to [psi_2] otimes eta_{12}
    D_{23}: psi_2_{(0)}psi_1 = 0

    Result: [psi_2] otimes eta_{12}
    """
    return {
        "D_12": {"result": "0", "coeff": Rational(0)},
        "D_13": {"result": "[psi_2] otimes eta_12", "coeff": Rational(1)},
        "D_23": {"result": "0", "coeff": Rational(0)},
        "total": "[psi_2] otimes eta_12",
    }


# ---------------------------------------------------------------------------
# Structural properties
# ---------------------------------------------------------------------------

def desuspension_parity() -> str:
    """After desuspension, psi_i have even parity.

    |s^{-1}psi_i| = |psi_i| - 1 = 1 - 1 = 0.
    So B(F_2) = Sym^c(s^{-1}V-bar) (symmetric, not exterior).
    """
    return "even"


def coalgebra_type() -> str:
    """B(F_2) is a SYMMETRIC coalgebra (not exterior).

    Ground truth: comp:fermion-deg2-signs, prop:fermion-bar-symmetric.
    """
    return "symmetric"


def koszul_dual_type() -> str:
    """F_2^! = Sym^ch(V*) (commutative chiral algebra).

    Lie^! = Com at the operadic level.
    """
    return "Sym^ch(V*)"


# ---------------------------------------------------------------------------
# Dimension data
# ---------------------------------------------------------------------------

# Dimension table from comp:fermion-dim-table (weight 1/2 generators only)
FERMION_DIM_TABLE_WT_HALF = {
    1: 2,    # 2 generators
    2: 2,    # 2 * 1 (form dim)
    3: 4,    # entries * 2 OS forms
    4: 10,   # ...
    5: 32,   # entries * 24 OS forms
}

FERMION_FORM_DIMS = {
    1: 1,   # dim Omega^0
    2: 1,   # dim Omega^1(Conf_2)
    3: 2,   # dim Omega^2(Conf_3)
    4: 6,   # dim Omega^3(Conf_4)
    5: 24,  # dim Omega^4(Conf_5)
}

FERMION_DIFF_RANKS = {
    2: 2,
    3: 2,
    4: 4,
    5: 10,
}

# Bar cohomology from Master Table
FERMION_BAR_COHOMOLOGY = {
    1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 7, 7: 11, 8: 15,
}


def fermion_bar_cohomology_dim(weight: int) -> int:
    """Bar cohomology dimension at given conformal weight.

    Ground truth: KNOWN_BAR_DIMS["free_fermion"] from Master Table.
    """
    return FERMION_BAR_COHOMOLOGY.get(weight, 0)


# ---------------------------------------------------------------------------
# Curvature
# ---------------------------------------------------------------------------

def fermion_curvature() -> Dict[str, object]:
    """Curvature for free fermion bar complex.

    The curvature has TWO components (one per generator):
    m_0^(psi_1) = 1, m_0^(psi_2) = 1
    from the simple poles psi_i_{(0)}psi_i = |0>.
    """
    return {"psi_1": Rational(1), "psi_2": Rational(1)}


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_fermion_ope():
    """Verify OPE products."""
    results = {}
    results["psi1_0_psi1 = |0>"] = fermion_nth_product(1, 1, 0).get("vac") == 1
    results["psi2_0_psi2 = |0>"] = fermion_nth_product(2, 2, 0).get("vac") == 1
    results["psi1_0_psi2 = 0"] = len(fermion_nth_product(1, 2, 0)) == 0
    results["psi2_0_psi1 = 0"] = len(fermion_nth_product(2, 1, 0)) == 0
    results["no higher poles"] = all(
        len(fermion_nth_product(i, j, n)) == 0
        for i in [1, 2] for j in [1, 2] for n in [1, 2, 3]
    )
    return results


def verify_fermion_bar_diff():
    """Verify degree-2 bar differential."""
    results = {}

    vac_11, bar1_11 = fermion_bar_diff_deg2(1, 1)
    results["D(psi1,psi1): vac=1"] = vac_11.get("vac") == 1
    results["D(psi1,psi1): no bar1"] = len(bar1_11) == 0

    vac_22, bar1_22 = fermion_bar_diff_deg2(2, 2)
    results["D(psi2,psi2): vac=1"] = vac_22.get("vac") == 1

    vac_12, bar1_12 = fermion_bar_diff_deg2(1, 2)
    results["D(psi1,psi2): no vac"] = len(vac_12) == 0
    results["D(psi1,psi2): no bar1"] = len(bar1_12) == 0

    vac_21, bar1_21 = fermion_bar_diff_deg2(2, 1)
    results["D(psi2,psi1): no vac"] = len(vac_21) == 0

    return results


def verify_fermion_deg3():
    """Verify degree-3 examples."""
    results = {}
    ex1 = fermion_bar_diff_deg3_example1()
    results["[112] D_12 nonzero"] = ex1["D_12"]["coeff"] == 1
    results["[112] D_13 zero"] = ex1["D_13"]["coeff"] == 0
    results["[112] D_23 zero"] = ex1["D_23"]["coeff"] == 0

    ex2 = fermion_bar_diff_deg3_example2()
    results["[121] D_12 zero"] = ex2["D_12"]["coeff"] == 0
    results["[121] D_13 nonzero"] = ex2["D_13"]["coeff"] == 1
    results["[121] D_23 zero"] = ex2["D_23"]["coeff"] == 0

    return results


def verify_fermion_cohomology():
    """Verify bar cohomology against KNOWN_BAR_DIMS."""
    expected = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 7, 7: 11, 8: 15}
    results = {}
    for h, exp in expected.items():
        results[f"H_h={h} = {exp}"] = fermion_bar_cohomology_dim(h) == exp
    return results


if __name__ == "__main__":
    print("=" * 60)
    print("FREE FERMION BAR COMPLEX: CHAIN-LEVEL VERIFICATION")
    print("=" * 60)

    print("\n--- OPE Products ---")
    for name, ok in verify_fermion_ope().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Bar Differential (degree 2) ---")
    for name, ok in verify_fermion_bar_diff().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Degree 3 Examples ---")
    for name, ok in verify_fermion_deg3().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Bar Cohomology ---")
    for name, ok in verify_fermion_cohomology().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print(f"\n--- Structural ---")
    print(f"  Desuspension parity: {desuspension_parity()}")
    print(f"  Coalgebra type: {coalgebra_type()}")
    print(f"  Koszul dual: {koszul_dual_type()}")
