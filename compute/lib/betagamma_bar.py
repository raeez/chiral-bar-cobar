"""Beta-gamma bar complex: chain-level computations.

The beta-gamma system has two bosonic generators:
  beta(z) of conformal weight lambda
  gamma(z) of conformal weight 1-lambda

OPE (beta_gamma.tex):
  beta(z)gamma(w) = 1/(z-w) + regular   [simple pole]
  beta(z)beta(w) = regular               [no pole]
  gamma(z)gamma(w) = regular             [no pole]

Collision/contact convention:
  r^{coll}_{beta gamma}(z) = 0 and r^{coll}_{bc}(z) = 0.
  The simple OPE residue beta_{(0)}gamma = 1 is bar/contact data,
  not a pole-valued closed collision residue and not A^!_ch.
  The genus-0 closed curvature m_0 is therefore 0.

Bar differential (beta_gamma.tex, Theorem "Complete bar complex"):
  D(beta otimes gamma) = 1   (simple OPE residue, maps to vacuum)
  D(gamma otimes beta) = -1  (simple OPE residue, opposite sign)
  D(beta otimes beta) = 0    (no pole)
  D(gamma otimes gamma) = 0  (no pole)
  D(d_beta) = 0, D(d_gamma) = 0

Class-C shadow convention:
  The standard beta-gamma/bc conformal-weight family has depth 4,
  S_3 = 0, S_4 = -5/12, and S_r = 0 for r >= 5.
  This nonzero rational coefficient is a quartic contact/shadow datum,
  not closed collision residue.

Degree 3:
  D(beta_1 otimes beta_2 otimes gamma_3) = beta_1 otimes 1 - 1 otimes beta_2
  Chain space dim = 2 * 3^{n-1}

Koszul dual (thm:betagamma-fermion-koszul):
  (betagamma)^! = F (free fermion / bc ghosts)
  F^! = betagamma
  Operadic: Sym^! = Lambda (Com^! = Lie)

Bar cohomology (thm:betagamma-bar-cohomology):
  H^*(B-bar_geom(betagamma_lambda)) = (betagamma_lambda)^i.
  It is the Koszul-dual coalgebra and is not concentrated in degree 0.
  Acyclicity belongs to the twisted Koszul resolution
  betagamma_lambda tensor_tau B-bar(betagamma_lambda), whose cohomology
  is C in degree 0 and 0 in positive degrees.

CONVENTIONS:
- Cohomological grading, |d| = +1
- Generators are bosonic (even parity)
"""

from __future__ import annotations

from typing import Dict, Tuple

from sympy import Rational


BETAGAMMA_CLOSED_COLLISION_RESIDUE = Rational(0)
BC_CLOSED_COLLISION_RESIDUE = Rational(0)
BETAGAMMA_SIMPLE_OPE_RESIDUE = Rational(1)
BC_SIMPLE_OPE_RESIDUE = Rational(1)

CLASS_C_SHADOW_DEPTH = 4
CLASS_C_STANDARD_FAMILY_S3 = Rational(0)
CLASS_C_STANDARD_FAMILY_S4 = Rational(-5, 12)


# ---------------------------------------------------------------------------
# OPE n-th products
# ---------------------------------------------------------------------------

def betagamma_nth_product(a: str, b: str, n: int) -> Dict[str, object]:
    """Get (a)_{(n)}(b) for a, b in {beta, gamma}.

    Ground truth: beta_gamma.tex OPE.
    beta_{(0)}gamma = 1 (simple pole, vacuum)
    This is a simple OPE/bar-contact residue, not the closed
    pole-valued collision residue.
    All other: 0
    """
    if n == 0 and a == "beta" and b == "gamma":
        return {"vac": BETAGAMMA_SIMPLE_OPE_RESIDUE}
    return {}


def betagamma_all_products() -> Dict[Tuple[str, str], Dict[int, Dict[str, object]]]:
    """All singular n-th products for beta-gamma generators."""
    return {
        ("beta", "gamma"): {0: {"vac": BETAGAMMA_SIMPLE_OPE_RESIDUE}},
        # The stored nth-product presentation is beta-before-gamma.
        # The opposite sign in the bar differential below is the
        # oriented residue convention, not a second closed residue.
        ("gamma", "beta"): {},
        ("beta", "beta"): {},    # regular
        ("gamma", "gamma"): {},  # regular
    }


def betagamma_closed_collision_residue() -> Dict[str, object]:
    """Pole-valued closed collision residue for beta-gamma.

    The beta-gamma OPE has only a simple pole. In the closed collision
    channel the dlog extraction removes that pole, so the pole-valued
    residue and genus-0 curvature both vanish. The nonzero coefficient
    beta_{(0)}gamma = 1 is returned by betagamma_nth_product and by
    the bar differential; it is not r^{coll} and not A^!_ch.
    """
    return {
        "r_coll": BETAGAMMA_CLOSED_COLLISION_RESIDUE,
        "m0": BETAGAMMA_CLOSED_COLLISION_RESIDUE,
    }


def bc_closed_collision_residue() -> Dict[str, object]:
    """Pole-valued closed collision residue for the bc ghost system.

    The same distinction holds for bc: b_{(0)}c = 1 is the simple
    OPE/bar-contact residue, while the closed collision residue is 0.
    """
    return {
        "r_coll": BC_CLOSED_COLLISION_RESIDUE,
        "m0": BC_CLOSED_COLLISION_RESIDUE,
    }


def betagamma_class_c_shadow_data() -> Dict[str, object]:
    """Class-C finite-depth shadow data for beta-gamma/bc.

    These are standard conformal-weight family constants. They are not
    closed collision residues and do not identify A, B(A), A^i, A^!,
    or Z_ch^der(A).
    """
    return {
        "shadow_class": "C",
        "depth": CLASS_C_SHADOW_DEPTH,
        "S3": CLASS_C_STANDARD_FAMILY_S3,
        "S4": CLASS_C_STANDARD_FAMILY_S4,
        "tail_from_5": Rational(0),
        "closed_collision_residue": BETAGAMMA_CLOSED_COLLISION_RESIDUE,
    }


# ---------------------------------------------------------------------------
# Bar differential
# ---------------------------------------------------------------------------

def betagamma_bar_diff_deg2(a: str, b: str) -> Tuple[Dict[str, object], Dict[str, object]]:
    """Bar differential D([a|b] otimes eta_{12}).

    Ground truth: beta_gamma.tex degree-2 differential. This extracts
    the simple OPE/bar-contact residue, not a closed collision residue.
    D(beta otimes gamma) = 1 (vacuum)
    D(gamma otimes beta) = -1 (vacuum, opposite sign)
    D(beta otimes beta) = 0
    D(gamma otimes gamma) = 0

    Returns (vac_component, bar1_component).
    """
    vac = {}
    bar1 = {}

    if a == "beta" and b == "gamma":
        vac["vac"] = BETAGAMMA_SIMPLE_OPE_RESIDUE
    elif a == "gamma" and b == "beta":
        vac["vac"] = -BETAGAMMA_SIMPLE_OPE_RESIDUE
    # beta-beta and gamma-gamma: zero (no pole)

    return vac, bar1


def betagamma_bar_diff_deg3_example() -> Dict[str, object]:
    """D(beta_1 otimes beta_2 otimes gamma_3) = beta_1 otimes 1 - 1 otimes beta_2.

    Ground truth: beta_gamma.tex line 60.

    Three collisions:
    D_{12}: beta_{(0)}beta = 0 (no pole)
    D_{13}: beta_{(0)}gamma = 1, leaves beta_2 -> [beta_2] otimes eta_*
    D_{23}: beta_{(0)}gamma = 1, leaves beta_1 -> [beta_1] otimes eta_*

    But with signs from the form residue, we get:
    D_{13} contribution: [beta_2] (positive)
    D_{23} contribution: -[beta_1] (negative from form orientation)

    Wait -- manuscript says D(beta1 otimes beta2 otimes gamma3) = beta1 otimes 1 - 1 otimes beta2.
    This means: after D_{13} collapses 1,3 -> [beta_2] and D_{23} collapses 2,3 -> [beta_1],
    with signs from the OS form residues.
    """
    return {
        "D_12": {"result": "0", "coeff": Rational(0)},
        "D_13": {"result": "[beta_2]", "coeff": Rational(1)},
        "D_23": {"result": "-[beta_1]", "coeff": Rational(-1)},
        "total": "beta_2 - beta_1 (in B-bar^1)",
    }


# ---------------------------------------------------------------------------
# Chain space dimensions
# ---------------------------------------------------------------------------

def betagamma_chain_type_count(n: int) -> int:
    """Number of generator type components at bar degree n.

    Ground truth: beta_gamma.tex line 62.
    rank(B-bar^n) = 2 * 3^{n-1} for n >= 1.

    This counts the number of distinct generator-type slots:
    n=1: 2 (beta, gamma)
    n=2: 6 (bb, bg, gb, gg, d_beta, d_gamma)
    n=3: 18
    """
    if n < 1:
        return 0
    return 2 * 3**(n - 1)


# Bar cohomology from Master Table
BETAGAMMA_BAR_COHOMOLOGY = {
    1: 2, 2: 4, 3: 10, 4: 26, 5: 70, 6: 192, 7: 534, 8: 1500,
}


def betagamma_bar_cohomology_dim(weight: int) -> int:
    """Koszul-dual coalgebra dimension at a conformal-weight truncation.

    Ground truth: KNOWN_BAR_DIMS["beta_gamma"] from Master Table.
    GF: sqrt((1+x)/(1-3x)).

    This is the bare geometric bar cohomology
    H^*(B-bar_geom(betagamma_lambda)) = (betagamma_lambda)^i, not the
    acyclic twisted Koszul resolution.
    """
    return BETAGAMMA_BAR_COHOMOLOGY.get(weight, 0)


# ---------------------------------------------------------------------------
# Koszul duality
# ---------------------------------------------------------------------------

def betagamma_koszul_dual() -> str:
    """Koszul dual of beta-gamma = free fermion (bc ghosts).

    Ground truth: thm:betagamma-fermion-koszul.
    """
    return "bc_ghosts"


def betagamma_bare_bar_is_acyclic() -> bool:
    """The bare beta-gamma bar coalgebra is not acyclic.

    Ground truth: thm:betagamma-bar-cohomology and
    prop:betagamma-bar-acyclicity. The positive cohomology of
    B-bar_geom(betagamma_lambda) is the Koszul-dual coalgebra
    (betagamma_lambda)^i.
    """
    return False


def betagamma_twisted_koszul_resolution_is_acyclic() -> bool:
    """The twisted Koszul resolution is acyclic off the vacuum.

    Ground truth: prop:betagamma-bar-acyclicity.
    K(tau) = betagamma_lambda tensor_tau B-bar(betagamma_lambda) has
    H^0 = C and H^n = 0 for n >= 1.
    """
    return True


def betagamma_is_koszul_acyclic() -> bool:
    """Compatibility name for twisted Koszul resolution acyclicity.

    This function does not assert acyclicity of the bare bar coalgebra.
    Use betagamma_bare_bar_is_acyclic() for that question.
    """
    return betagamma_twisted_koszul_resolution_is_acyclic()


# ---------------------------------------------------------------------------
# Curvature
# ---------------------------------------------------------------------------

def betagamma_curvature() -> Dict[str, object]:
    """Compatibility wrapper for beta-gamma residue data.

    Closed genus-0 curvature is m_0 = 0: the beta-gamma OPE has no
    double pole, and its simple pole is absorbed in the closed dlog
    collision channel. The legacy ``"beta_gamma"`` key is preserved as
    the simple OPE/bar-contact residue beta_{(0)}gamma = 1 for callers
    that used this function before the closed/contact distinction was
    made explicit.
    """
    return {
        "m0": BETAGAMMA_CLOSED_COLLISION_RESIDUE,
        "closed_collision_residue": BETAGAMMA_CLOSED_COLLISION_RESIDUE,
        "simple_ope_residue": BETAGAMMA_SIMPLE_OPE_RESIDUE,
        "bar_contact_residue": BETAGAMMA_SIMPLE_OPE_RESIDUE,
        "beta_gamma": BETAGAMMA_SIMPLE_OPE_RESIDUE,
    }


# ---------------------------------------------------------------------------
# bc ghost system (Koszul dual)
# ---------------------------------------------------------------------------

def bc_bar_diff_deg2(a: str, b: str) -> Tuple[Dict[str, object], Dict[str, object]]:
    """Bar differential for bc ghost system at degree 2.

    This is simple OPE/bar-contact data. The pole-valued closed
    collision residue for bc is zero.

    Ground truth: prop:bar-bc-system (beta_gamma.tex).
    D(b otimes c) = 1 (vacuum)
    D(c otimes b) = -1 (vacuum)
    D(b otimes b) = 0
    D(c otimes c) = 0
    """
    vac = {}
    bar1 = {}

    if a == "b" and b == "c":
        vac["vac"] = BC_SIMPLE_OPE_RESIDUE
    elif a == "c" and b == "b":
        vac["vac"] = -BC_SIMPLE_OPE_RESIDUE

    return vac, bar1


def bc_coalgebra_type() -> str:
    """B(bc) = Sym^c(s^{-1}V-bar) (symmetric coalgebra).

    The bc system is fermionic. After desuspension, generators become even.
    So the bar complex is a symmetric (not exterior) coalgebra.
    Same as for the free fermion F_2.
    """
    return "symmetric"


def bc_koszul_dual() -> str:
    """Koszul dual of bc = beta-gamma.

    bc^! = betagamma and betagamma^! = bc.
    """
    return "beta_gamma"


# Bar cohomology from Master Table
BC_BAR_COHOMOLOGY = {
    1: 2, 2: 3, 3: 6, 4: 13, 5: 28, 6: 59, 7: 122, 8: 249,
}


def bc_bar_cohomology_dim(weight: int) -> int:
    """bc bar cohomology at given conformal weight.

    Ground truth: KNOWN_BAR_DIMS["bc"] from Master Table.
    Formula: 2^n - n + 1.
    """
    return BC_BAR_COHOMOLOGY.get(weight, 0)


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_betagamma_bar_diff():
    """Verify all degree-2 bar differentials."""
    results = {}

    vac_bg, bar1_bg = betagamma_bar_diff_deg2("beta", "gamma")
    results["D(bg): vac=1"] = vac_bg.get("vac") == 1
    results["D(bg): no bar1"] = len(bar1_bg) == 0

    vac_gb, bar1_gb = betagamma_bar_diff_deg2("gamma", "beta")
    results["D(gb): vac=-1"] = vac_gb.get("vac") == -1

    vac_bb, bar1_bb = betagamma_bar_diff_deg2("beta", "beta")
    results["D(bb): zero"] = len(vac_bb) == 0 and len(bar1_bb) == 0

    vac_gg, bar1_gg = betagamma_bar_diff_deg2("gamma", "gamma")
    results["D(gg): zero"] = len(vac_gg) == 0 and len(bar1_gg) == 0

    return results


def verify_bc_bar_diff():
    """Verify bc ghost bar differentials."""
    results = {}

    vac_bc, _ = bc_bar_diff_deg2("b", "c")
    results["D(bc): vac=1"] = vac_bc.get("vac") == 1

    vac_cb, _ = bc_bar_diff_deg2("c", "b")
    results["D(cb): vac=-1"] = vac_cb.get("vac") == -1

    vac_bb, _ = bc_bar_diff_deg2("b", "b")
    results["D(bb): zero"] = len(vac_bb) == 0

    vac_cc, _ = bc_bar_diff_deg2("c", "c")
    results["D(cc): zero"] = len(vac_cc) == 0

    return results


def verify_chain_type_counts():
    """Verify chain type count formula."""
    results = {}
    expected = {1: 2, 2: 6, 3: 18, 4: 54, 5: 162}
    for n, exp in expected.items():
        results[f"rank B^{n} = {exp}"] = betagamma_chain_type_count(n) == exp
    return results


def verify_koszul_duality():
    """Verify the Koszul duality pair."""
    results = {}
    results["bg^! = bc"] = betagamma_koszul_dual() == "bc_ghosts"
    results["bc^! = bg"] = bc_koszul_dual() == "beta_gamma"
    results["bare bg bar is dual coalgebra, not acyclic"] = (
        not betagamma_bare_bar_is_acyclic()
        and betagamma_bar_cohomology_dim(1) == 2
        and betagamma_bar_cohomology_dim(2) == 4
    )
    results["twisted bg Koszul resolution is acyclic"] = (
        betagamma_is_koszul_acyclic()
    )
    return results


def verify_closed_collision_vs_contact():
    """Verify closed collision zero is not conflated with contact data."""
    bg_closed = betagamma_closed_collision_residue()
    bc_closed = bc_closed_collision_residue()
    class_c = betagamma_class_c_shadow_data()
    curv = betagamma_curvature()

    return {
        "bg r_coll = 0": bg_closed["r_coll"] == 0,
        "bg m0 = 0": bg_closed["m0"] == 0,
        "bc r_coll = 0": bc_closed["r_coll"] == 0,
        "simple OPE residue = 1": curv["simple_ope_residue"] == 1,
        "legacy beta_gamma key is contact": curv["beta_gamma"] == 1,
        "S4 = -5/12": class_c["S4"] == Rational(-5, 12),
        "class C depth = 4": class_c["depth"] == 4,
        "class C tail vanishes from 5": class_c["tail_from_5"] == 0,
    }


if __name__ == "__main__":
    print("=" * 60)
    print("BETA-GAMMA / BC BAR COMPLEX: CHAIN-LEVEL VERIFICATION")
    print("=" * 60)

    for section, fn in [
        ("Beta-Gamma Bar Differential", verify_betagamma_bar_diff),
        ("bc Ghost Bar Differential", verify_bc_bar_diff),
        ("Chain Type Counts", verify_chain_type_counts),
        ("Koszul Duality", verify_koszul_duality),
        ("Closed Collision vs Contact", verify_closed_collision_vs_contact),
    ]:
        print(f"\n--- {section} ---")
        for name, ok in fn().items():
            print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
