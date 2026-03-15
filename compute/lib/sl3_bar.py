"""sl_3 bar complex: chain-level computations.

The affine Lie algebra sl_3-hat_k has 8 generators:
  {H_1, H_2, E_1, E_2, E_3, F_1, F_2, F_3}
where E_3 = [E_1, E_2], F_3 = [F_2, F_1].

Ground truth from the manuscript (detailed_computations.tex):
  comp:sl3-ope — OPE data
  comp:sl3-bar — bar differential at degree 2

OPE (at level k):
  H_i(z)H_j(w) ~ k*A_{ij}/(z-w)^2
  H_i(z)E_j(w) ~ A_{ij}*E_j(w)/(z-w)
  E_i(z)F_j(w) ~ k*delta_{ij}/(z-w)^2 + delta_{ij}*H_i(w)/(z-w)
  E_1(z)E_2(w) ~ E_3(w)/(z-w)
  E_1(z)E_3(w) ~ 0

Bar differential (degree 2):
  d[H_1|E_1] = 2[E_1]
  d[H_1|E_2] = -[E_2]
  d[E_1|E_2] = [E_3]
  d[E_1|F_1] = [H_1] + k*delta*[1]  (curvature term at m+n=0)

Degree-3: Serre relations as bar cycles.

CONVENTIONS:
- Cohomological grading, |d| = +1
- Generators indexed: H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7
"""

from __future__ import annotations

from typing import Dict, List, Tuple

from sympy import Matrix, Rational, Symbol, zeros


# Generator indices
H1, H2, E1, E2, E3, F1, F2, F3 = range(8)
GEN_NAMES = ["H1", "H2", "E1", "E2", "E3", "F1", "F2", "F3"]
DIM_G = 8

# Cartan matrix for sl_3
CARTAN = Matrix([[2, -1], [-1, 2]])


def sl3_structure_constants() -> Dict[Tuple[int, int], Dict[int, Rational]]:
    """Structure constants for sl_3.

    Ground truth: comp:sl3-ope.
    [H_i, E_j] = A_{ij}*E_j, [H_i, F_j] = -A_{ij}*F_j
    [E_i, F_j] = delta_{ij}*H_i  (i,j in {1,2})
    [E_1, E_2] = E_3, [F_2, F_1] = F_3
    [E_1, E_3] = 0, [E_2, E_3] = 0, etc.
    """
    bracket = {}

    # [H_i, E_j] = A_{ij}*E_j
    for i, hi in enumerate([H1, H2]):
        for j, ej in enumerate([E1, E2]):
            a_ij = CARTAN[i, j]
            if a_ij != 0:
                bracket[(hi, ej)] = {ej: Rational(a_ij)}
                bracket[(ej, hi)] = {ej: Rational(-a_ij)}

    # [H_i, F_j] = -A_{ij}*F_j
    for i, hi in enumerate([H1, H2]):
        for j, fj in enumerate([F1, F2]):
            a_ij = CARTAN[i, j]
            if a_ij != 0:
                bracket[(hi, fj)] = {fj: Rational(-a_ij)}
                bracket[(fj, hi)] = {fj: Rational(a_ij)}

    # [E_i, F_j] = delta_{ij}*H_i
    bracket[(E1, F1)] = {H1: Rational(1)}
    bracket[(F1, E1)] = {H1: Rational(-1)}
    bracket[(E2, F2)] = {H2: Rational(1)}
    bracket[(F2, E2)] = {H2: Rational(-1)}

    # [E_1, E_2] = E_3
    bracket[(E1, E2)] = {E3: Rational(1)}
    bracket[(E2, E1)] = {E3: Rational(-1)}

    # [F_2, F_1] = F_3
    bracket[(F2, F1)] = {F3: Rational(1)}
    bracket[(F1, F2)] = {F3: Rational(-1)}

    # [H_i, E_3]: E_3 = [E_1, E_2] has root alpha_1+alpha_2
    # [H_1, E_3] = (A_{11}+A_{12})*E_3 = (2-1)*E_3 = E_3
    bracket[(H1, E3)] = {E3: Rational(1)}
    bracket[(E3, H1)] = {E3: Rational(-1)}
    # [H_2, E_3] = (A_{21}+A_{22})*E_3 = (-1+2)*E_3 = E_3
    bracket[(H2, E3)] = {E3: Rational(1)}
    bracket[(E3, H2)] = {E3: Rational(-1)}

    # [H_i, F_3]: F_3 has root -(alpha_1+alpha_2)
    bracket[(H1, F3)] = {F3: Rational(-1)}
    bracket[(F3, H1)] = {F3: Rational(1)}
    bracket[(H2, F3)] = {F3: Rational(-1)}
    bracket[(F3, H2)] = {F3: Rational(1)}

    # [E_3, F_1] = [E_1,E_2]F_1 = E_1[E_2,F_1] + [E_1,F_1]E_2
    # [E_2,F_1] = 0, [E_1,F_1] = H_1
    # so [E_3, F_1] = H_1*E_2... wait, this isn't right for the Lie bracket
    # Actually [E_3, F_1] = [[E_1,E_2], F_1] = [E_1,[E_2,F_1]] + [[E_1,F_1],E_2]
    # = [E_1, 0] + [H_1, E_2] = 0 + (-1)*E_2 = -E_2
    bracket[(E3, F1)] = {E2: Rational(-1)}
    bracket[(F1, E3)] = {E2: Rational(1)}

    # [E_3, F_2] = [[E_1,E_2], F_2] = [E_1,[E_2,F_2]] + [[E_1,F_2],E_2]
    # = [E_1, H_2] + [0, E_2] = -(-1)*E_1 = E_1
    # Actually [E_1, H_2] = -[H_2, E_1] = -A_{21}*E_1 = -(-1)*E_1 = E_1
    bracket[(E3, F2)] = {E1: Rational(1)}
    bracket[(F2, E3)] = {E1: Rational(-1)}

    # [E_3, F_3]: [[E_1,E_2],[F_2,F_1]]
    # = [E_1,[E_2,[F_2,F_1]]] + [[E_1,[F_2,F_1]],E_2]
    # [E_2,[F_2,F_1]] = [E_2,F_3] ... this gets complicated
    # Actually: [E_3, F_3] = H_1 + H_2 (standard result for sl_3)
    bracket[(E3, F3)] = {H1: Rational(1), H2: Rational(1)}
    bracket[(F3, E3)] = {H1: Rational(-1), H2: Rational(-1)}

    # [E_1, F_3] = [E_1, [F_2,F_1]] = [[E_1,F_2],F_1] + [F_2,[E_1,F_1]]
    # = [0, F_1] + [F_2, H_1] = 0 + (-F_2) = -F_2
    # (since [F_2, H_1] = -[H_1, F_2] = -(F_2) = -F_2, using [H_1,F_2]=-A_{12}F_2=F_2)
    bracket[(E1, F3)] = {F2: Rational(-1)}
    bracket[(F3, E1)] = {F2: Rational(1)}

    # [E_2, F_3] = [E_2, [F_2,F_1]] = [[E_2,F_2],F_1] + [F_2,[E_2,F_1]]
    # = [H_2, F_1] + [F_2, 0] = A_{21}*(-F_1) = -(-1)*(-F_1)... 
    # [H_2, F_1] = -A_{21}*F_1 = -(-1)*F_1 = F_1
    # Wait: [H_i, F_j] = -A_{ij}*F_j. So [H_2, F_1] = -A_{21}*F_1 = -(-1)*F_1 = F_1
    bracket[(E2, F3)] = {F1: Rational(1)}
    bracket[(F3, E2)] = {F1: Rational(-1)}

    # [E_1, E_3] = [E_1, [E_1, E_2]] = 0 (Serre relation)
    # [E_2, E_3] = [E_2, [E_1, E_2]] = 0 (Serre relation)
    # [F_1, F_3] = 0, [F_2, F_3] = 0

    return bracket


def sl3_killing_form() -> Dict[Tuple[int, int], Rational]:
    """Normalized trace form (H_i, H_j) = A_{ij}, (E_i, F_j) = delta_{ij}.

    Ground truth: comp:sl3-ope.
    """
    kf = {}
    # Cartan: (H_i, H_j) = A_{ij}
    kf[(H1, H1)] = Rational(2)
    kf[(H1, H2)] = Rational(-1)
    kf[(H2, H1)] = Rational(-1)
    kf[(H2, H2)] = Rational(2)
    # Root vectors: (E_i, F_i) = 1
    kf[(E1, F1)] = Rational(1)
    kf[(F1, E1)] = Rational(1)
    kf[(E2, F2)] = Rational(1)
    kf[(F2, E2)] = Rational(1)
    kf[(E3, F3)] = Rational(1)
    kf[(F3, E3)] = Rational(1)
    return kf


# ---------------------------------------------------------------------------
# OPE n-th products
# ---------------------------------------------------------------------------

def sl3_nth_product(a: int, b: int, n: int) -> Dict[str, object]:
    """Get a_{(n)}b for sl_3-hat_k generators.

    n=1: double pole -> k*(a,b)|0> (curvature)
    n=0: simple pole -> [a,b] (structure constant)
    """
    k = Symbol('k')
    bracket = sl3_structure_constants()
    kf = sl3_killing_form()

    if n == 1:
        # Double pole: k * (a, b) * |0>
        kappa = kf.get((a, b), Rational(0))
        if kappa != 0:
            return {"vac": k * kappa}
        return {}

    if n == 0:
        # Simple pole: [a, b]
        br = bracket.get((a, b), {})
        return {GEN_NAMES[c]: coeff for c, coeff in br.items()}

    return {}


# ---------------------------------------------------------------------------
# Bar differential: degree 2
# ---------------------------------------------------------------------------

def sl3_bar_diff_deg2(a: int, b: int) -> Tuple[Dict[str, object], Dict[str, object]]:
    """Bar differential D(a ⊗ b ⊗ eta_{12}).

    D extracts all singular OPE data.
    Returns (vac_component, bar1_component).
    """
    vac = {}
    bar1 = {}

    for n_val in [1, 0]:  # only double and simple poles for KM
        products = sl3_nth_product(a, b, n_val)
        for state, coeff in products.items():
            if state == "vac":
                vac["vac"] = vac.get("vac", 0) + coeff
            else:
                bar1[state] = bar1.get(state, 0) + coeff

    return vac, bar1


# ---------------------------------------------------------------------------
# Key bar differential examples from comp:sl3-bar
# ---------------------------------------------------------------------------

def sl3_bar_diff_examples() -> Dict[str, Dict]:
    """Named examples from comp:sl3-bar.

    d[H_1|E_1] = 2[E_1]
    d[H_1|E_2] = -[E_2]
    d[E_1|E_2] = [E_3]
    d[E_1|F_1] = [H_1] + k*[1]  (curvature term)
    """
    k = Symbol('k')
    return {
        "d[H1|E1] = 2E1": {
            "input": (H1, E1),
            "expected_bar1": {"E1": Rational(2)},
            "expected_vac": {},
        },
        "d[H1|E2] = -E2": {
            "input": (H1, E2),
            "expected_bar1": {"E2": Rational(-1)},
            "expected_vac": {},
        },
        "d[E1|E2] = E3": {
            "input": (E1, E2),
            "expected_bar1": {"E3": Rational(1)},
            "expected_vac": {},
        },
        "d[E1|F1] = H1 + k*vac": {
            "input": (E1, F1),
            "expected_bar1": {"H1": Rational(1)},
            "expected_vac": {"vac": k},
        },
    }


# ---------------------------------------------------------------------------
# Curvature
# ---------------------------------------------------------------------------

def sl3_curvature() -> Dict[Tuple[int, int], object]:
    """Curvature elements for the sl_3-hat bar complex.

    m_0 = k * (a, b) for each generator pair with nonzero Killing form.
    """
    k = Symbol('k')
    kf = sl3_killing_form()
    return {pair: k * kappa for pair, kappa in kf.items()}


def sl3_sugawara_c():
    """Sugawara central charge for sl_3-hat_k.

    c = k * dim(sl_3) / (k + h^vee) = 8k / (k + 3).
    h^vee(sl_3) = 3.
    """
    k = Symbol('k')
    return 8 * k / (k + 3)


# ---------------------------------------------------------------------------
# Serre relations as bar cycles (degree 3)
# ---------------------------------------------------------------------------

def sl3_serre_cycle() -> Dict[str, object]:
    """Serre relation as degree-3 bar cycle.

    Ground truth: comp:sl3-bar.
    [E_1|E_1|E_2] - 2[E_1|E_2|E_1] + [E_2|E_1|E_1]
    is a cycle (its differential gives (ad E_1)^2(E_2) = 0 in U(sl_3-hat)).
    """
    return {
        "generators": [(E1, E1, E2), (E1, E2, E1), (E2, E1, E1)],
        "coefficients": [Rational(1), Rational(-2), Rational(1)],
        "relation": "(ad E_1)^2(E_2) = 0",
        "type": "Serre",
    }


def sl3_serre_vanishes() -> bool:
    """Verify (ad E_1)^2(E_2) = 0 in sl_3.

    The Serre relation: [E_1, [E_1, E_2]] = 0.
    This is what the degree-3 bar complex encodes: the differential
    maps the Serre combination to an element representing (ad E_1)^2(E_2),
    which vanishes in the algebra.

    Ground truth: comp:sl3-bar.
    """
    bracket = sl3_structure_constants()

    # [E_1, E_2] = E_3
    e1_e2 = bracket.get((E1, E2), {})
    # [E_1, [E_1, E_2]] = [E_1, E_3]
    result = {}
    for d_idx, d_coeff in e1_e2.items():
        for e_idx, e_coeff in bracket.get((E1, d_idx), {}).items():
            result[e_idx] = result.get(e_idx, Rational(0)) + d_coeff * e_coeff

    return all(v == 0 for v in result.values())


# ---------------------------------------------------------------------------
# Jacobi identity check
# ---------------------------------------------------------------------------

def sl3_jacobi_check() -> bool:
    """Verify the Jacobi identity for sl_3 structure constants.

    [[a,b],c] + [[b,c],a] + [[c,a],b] = 0 for all a,b,c.
    """
    bracket = sl3_structure_constants()
    for a in range(DIM_G):
        for b in range(DIM_G):
            for c in range(DIM_G):
                total = [Rational(0)] * DIM_G
                # [[a,b],c]
                for d, coeff in bracket.get((a, b), {}).items():
                    for e, coeff2 in bracket.get((d, c), {}).items():
                        total[e] += coeff * coeff2
                # [[b,c],a]
                for d, coeff in bracket.get((b, c), {}).items():
                    for e, coeff2 in bracket.get((d, a), {}).items():
                        total[e] += coeff * coeff2
                # [[c,a],b]
                for d, coeff in bracket.get((c, a), {}).items():
                    for e, coeff2 in bracket.get((d, b), {}).items():
                        total[e] += coeff * coeff2
                if any(t != 0 for t in total):
                    return False
    return True


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_sl3_bar_diff():
    """Verify degree-2 bar differential against comp:sl3-bar examples."""
    k = Symbol('k')
    results = {}

    examples = sl3_bar_diff_examples()
    for name, data in examples.items():
        a, b = data["input"]
        vac, bar1 = sl3_bar_diff_deg2(a, b)

        # Check bar1
        bar1_ok = True
        for state, expected_coeff in data["expected_bar1"].items():
            if bar1.get(state) != expected_coeff:
                bar1_ok = False
        # Check no extra terms in bar1
        for state in bar1:
            if state not in data["expected_bar1"]:
                bar1_ok = False

        # Check vac
        vac_ok = True
        if data["expected_vac"]:
            for state, expected_coeff in data["expected_vac"].items():
                if vac.get(state) != expected_coeff:
                    vac_ok = False
        else:
            if len(vac) > 0:
                vac_ok = False

        results[name] = bar1_ok and vac_ok

    return results


def verify_sl3_serre():
    """Verify Serre relation and Jacobi identity."""
    results = {}
    results["Serre: (ad E1)^2(E2) = 0"] = sl3_serre_vanishes()
    results["Jacobi identity"] = sl3_jacobi_check()
    return results


if __name__ == "__main__":
    print("=" * 60)
    print("sl_3 BAR COMPLEX: CHAIN-LEVEL VERIFICATION")
    print("=" * 60)

    print("\n--- Bar Differential (degree 2) ---")
    for name, ok in verify_sl3_bar_diff().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Serre Relations & Jacobi ---")
    for name, ok in verify_sl3_serre().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Sugawara Central Charge ---")
    print(f"  c = {sl3_sugawara_c()}")
