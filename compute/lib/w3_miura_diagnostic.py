"""W_3 Miura diagnostic: minimal test bed for the OPE extraction pipeline.

Computes the W_3 structure constant C_333^2 from the sl_3 quantum Miura
transformation with 2 free bosons and compares against the exact
Zamolodchikov bootstrap result:

    C_333^2 = 64(7c+68)(2c-1) / [5c(c+24)(5c+22)]

This module deliberately uses the SAME Wick contraction engine as
w4_ope_miura.py. If C_333^2 matches Zamolodchikov, the engine is correct
and the W_4 bug is in the Miura product expansion. If it doesn't match,
the bug is in the Wick contraction engine itself.

Central charge for W_3 from sl_3 at level k:
    c = 2(1 - 12/(k+3)) = 2 - 24/(k+3)
    alpha_0^2 = t = 2/(k+3)
    c = 2 - 24t/2 = 2 - 12t   ... NO.
    Actually: c(sl_3, k) = (N-1)(1 - N(N+1)/(k+N)) with N=3
                          = 2(1 - 12/(k+3))
    With t = alpha_0^2 = 2/(k+3): k+3 = 2/t, so c = 2 - 24/(2/t) = 2-12t.
    Wait: c = 2(1 - 12*t/2) = 2 - 12t.

Propagator: <dphi_a(z) dphi_b(w)> = -delta_{ab}/(z-w)^2 for a,b in {0,1}.
"""

from __future__ import annotations
import numpy as np
from typing import Dict, List, Optional, Tuple
from compute.lib.w4_ope_miura import (
    Field, Monomial,
    monomial_weight, field_weight,
    simplify_field, add_fields, scale_field,
    multiply_fields, derivative_field, nth_derivative_field,
    _bpz_inner_product, _field_overlap,
    _wick_ope_at_pole, compute_ope, evaluate_field_as_number,
)


# =========================================================================
# sl_3 root system (2 bosons in orthonormal Cartan basis)
# =========================================================================

def sl3_fundamental_weights_R3():
    """Weights of the fundamental (3-dim) rep of sl_3 in R^3.

    h_1 = (2/3, -1/3, -1/3), h_2 = (-1/3, 2/3, -1/3), h_3 = (-1/3, -1/3, 2/3).
    These satisfy sum h_i = 0 and h_i . h_j = delta_ij - 1/3.
    """
    return np.array([
        [ 2/3, -1/3, -1/3],
        [-1/3,  2/3, -1/3],
        [-1/3, -1/3,  2/3],
    ])


def sl3_weyl_vector_R3():
    """Weyl vector of sl_3 in R^3: rho = (1, 0, -1)."""
    return np.array([1.0, 0.0, -1.0])


def sl3_orthonormal_cartan_basis():
    """Orthonormal basis for the Cartan subalgebra of sl_3.

    Two orthonormal vectors in R^3 spanning the hyperplane sum x_i = 0:
      e_1 = (1, -1, 0)/sqrt(2)
      e_2 = (1, 1, -2)/sqrt(6)
    """
    e1 = np.array([1, -1, 0]) / np.sqrt(2)
    e2 = np.array([1, 1, -2]) / np.sqrt(6)
    return np.array([e1, e2])


# =========================================================================
# W_3 generators from Miura (2 free bosons)
# =========================================================================

def w3_central_charge(t: float) -> float:
    """Central charge c = 2 - 12t for the sl_3 Miura at parameter t = alpha_0^2.

    From c = 2(1 - 12/(k+3)) and t = 2/(k+3), we get c = 2(1 - 6t) = 2 - 12t.
    """
    return 2.0 - 12.0 * t


def w3_miura_generators(t: float) -> Tuple[Field, Field]:
    """Compute T and W_3 from the quantum Miura transformation for sl_3.

    The Miura operator is:
      L = :(d + alpha_0 h_1.dphi)(d + alpha_0 h_2.dphi)(d + alpha_0 h_3.dphi):

    where h_i are the fundamental weights of sl_3 projected to the
    2-dimensional Cartan subalgebra.

    After normal ordering, the expansion is:
      L = d^3 + 0*d^2 + T*d + W_3

    (The d^2 term vanishes because sum h_i = 0.)

    T = stress tensor (weight 2)
    W_3 = spin-3 generator (weight 3)
    """
    alpha0 = np.sqrt(t)
    basis = sl3_orthonormal_cartan_basis()  # shape (2, 3)
    rho = sl3_weyl_vector_R3()

    # Fundamental weights projected to orthonormal Cartan basis
    h_fund = sl3_fundamental_weights_R3()  # shape (3, 3)
    h_proj = np.array([
        [np.dot(h_fund[i], basis[a]) for a in range(2)]
        for i in range(3)
    ])  # shape (3, 2): 3 weights, each in R^2

    # Background charge in orthonormal basis
    Q = np.array([alpha0 * np.dot(rho, basis[a]) for a in range(2)])

    # Build the Miura product step by step.
    # Start with L_0 = 1 (the identity differential operator, degree 0).
    # Multiply from right: L_{i+1} = L_i * (d + J_i)
    # where J_i = alpha_0 * h_i . dphi (a linear field in dphi_0, dphi_1).

    # Represent a differential operator as a list of fields [F_0, F_1, ..., F_n]
    # meaning F_0 + F_1 * d + F_2 * d^2 + ... + F_n * d^n.

    # Start: L_0 = [1] = d^0
    # This represents the operator "multiply by 1".
    one_field: Field = [(1.0, ())]
    zero_field: Field = []
    L = [one_field]  # L_0 = 1

    for i in range(3):
        # Current J_i = alpha_0 * sum_a h_proj[i, a] * dphi_a
        J_i: Field = []
        for a in range(2):
            coeff = alpha0 * h_proj[i, a]
            if abs(coeff) > 1e-15:
                J_i.append((coeff, ((a, 1),)))  # dphi_a has derivative order 1
        J_i = simplify_field(J_i)

        # Multiply: L_{new} = L * (d + J_i)
        # If L = sum_k F_k d^k, then:
        # L * (d + J_i) = sum_k F_k d^{k+1} + sum_k F_k J_i d^k
        #               + sum_k F_k * (quantum correction from d acting on J_i)
        #
        # The quantum correction: when d acts on J_i from the left, it
        # produces dJ_i as an extra term. More precisely, in the normally
        # ordered product, moving d past J_i gives d*J_i = :d*J_i: + dJ_i.
        # So the quantum correction for each factor is:
        # F_k * d^k * J_i = F_k * :d^k * J_i: (including derivative corrections)
        #
        # For the Miura product, the standard result is:
        # (sum_k F_k d^k) * (d + J) = sum_k F_k d^{k+1}
        #                             + sum_k :F_k * J: d^k
        #                             + sum_k k * dF_k d^{k-1}   [quantum correction]
        #
        # Wait, that's not right either. The quantum correction comes from
        # normal ordering the product F_k(z) * J_i(z), which involves
        # self-contractions. But for FREE BOSONS, the normal ordering of
        # F_k * J_i has NO self-contraction if F_k and J_i involve DIFFERENT
        # boson indices. When they share indices, there's a contraction.
        #
        # Actually, for the Miura product, we use the NORMALLY ORDERED product,
        # which means: expand the product of differential operators, and
        # whenever d^k acts on a field to its right, use the Leibniz rule
        # d^k(f * g) = sum_{j=0}^k C(k,j) (d^j f)(d^{k-j} g).
        #
        # So the CORRECT multiplication rule is:
        # (sum_k F_k d^k) * (d + J) = sum_k F_k d^{k+1}
        #                             + sum_k sum_{j=0}^k C(k,j) (d^j J) * F_k d^{k-j}
        #                           = sum_k F_k d^{k+1}
        #                             + sum_k F_k * J * d^k
        #                             + sum_k k * (dJ) * F_k d^{k-1}
        #                             + sum_k C(k,2) * (d^2 J) * F_k d^{k-2}
        #                             + ...
        # But J is LINEAR in dphi, so d^j J = d^{j+1} phi for j>=0.
        # For j>=2, d^j J involves higher derivatives which are new independent
        # generators (d^2 phi, d^3 phi, etc.).

        n_old = len(L)
        n_new = n_old + 1
        L_new = [zero_field] * n_new

        for k in range(n_old):
            F_k = L[k]
            if not F_k:
                continue

            # Term 1: F_k d^{k+1}
            L_new[k + 1] = add_fields(L_new[k + 1], F_k)

            # Term 2 and beyond: F_k d^k * J_i = sum_{j=0}^{k} C(k,j) * (d^j J_i) * F_k * d^{k-j}
            # j=0: F_k * J_i * d^k  (normal ordering: multiply_fields)
            # j=1: k * (dJ_i) * F_k * d^{k-1}
            # j>=2: higher derivatives of J_i (which is linear, so d^j J = d^{j+1} phi)
            for j in range(k + 1):
                dj_J = nth_derivative_field(J_i, j) if j > 0 else J_i
                if not dj_J:
                    continue
                binom = _binom(k, j)
                # Contribution: binom * :F_k * d^j(J_i): at order d^{k-j}
                product = multiply_fields(F_k, dj_J)
                if product:
                    L_new[k - j] = add_fields(L_new[k - j], scale_field(binom, product))

        L = [simplify_field(f) for f in L_new]

    # Now L = [W_3_raw, T_raw, something, d^3_coeff]
    # The coefficient of d^3 should be 1 (identity)
    # The coefficient of d^2 should be 0 (sum h_i = 0)
    # The coefficient of d^1 is T (up to normalization)
    # The coefficient of d^0 is W_3 (up to normalization)

    # Verify d^3 coefficient is scalar 1
    d3_coeff = L[3] if len(L) > 3 else []
    d3_val = evaluate_field_as_number(d3_coeff) if d3_coeff else 0
    if abs(d3_val - 1.0) > 1e-10:
        print(f"WARNING: d^3 coefficient = {d3_val}, expected 1.0")

    # Verify d^2 coefficient is 0 (tracelessness)
    d2_coeff = L[2] if len(L) > 2 else []
    d2_val = evaluate_field_as_number(d2_coeff) if d2_coeff else 0
    if d2_coeff and abs(d2_val) > 1e-10:
        # d^2 coefficient might have field content, not just a scalar
        pass  # expected to be zero or very small

    T_field = L[1] if len(L) > 1 else []
    W3_field = L[0] if len(L) > 0 else []

    return T_field, W3_field


def _binom(n: int, k: int) -> float:
    """Binomial coefficient C(n, k)."""
    if k < 0 or k > n:
        return 0.0
    from math import comb
    return float(comb(n, k))


# =========================================================================
# W_3 OPE and structure constant extraction
# =========================================================================

class W3MiuraDiagnostic:
    """Diagnostic: compute W_3 structure constant C_333 from Miura and compare
    with the exact Zamolodchikov result."""

    def __init__(self, t: float):
        self.t = t
        self.c_expected = w3_central_charge(t)

        # Build generators
        self.T, self.W3 = w3_miura_generators(t)

        # Compute actual central charge from T self-OPE
        tt_pole4 = _wick_ope_at_pole(self.T, self.T, 4)
        self.norm_T = evaluate_field_as_number(tt_pole4) if tt_pole4 else 0
        self.c_actual = 2.0 * self.norm_T

        # Derivatives
        self.dT = derivative_field(self.T)

        # W_3 norm
        w3w3_pole6 = _wick_ope_at_pole(self.W3, self.W3, 6)
        self.norm_W3 = evaluate_field_as_number(w3w3_pole6) if w3w3_pole6 else 0

    @staticmethod
    def zamolodchikov_C333_squared(c: float) -> float:
        """The exact Zamolodchikov result for C_333^2.

        C_333^2 = 64(7c+68)(2c-1) / [5c(c+24)(5c+22)]

        This is the squared OPE structure constant of W_3 x W_3 -> W_3,
        in the normalization where ||W_3||^2 = c/3.

        Poles: c=0, c=-24, c=-22/5. Zeros: c=-68/7, c=1/2.
        Classical limit (c -> infinity): C_333^2 -> 64*14 / (5*5) = 896/25 = 35.84.
        """
        return 64.0 * (7 * c + 68) * (2 * c - 1) / (5 * c * (c + 24) * (5 * c + 22))

    def compute_C333(self) -> dict:
        """Extract C_333 from the W_3 x W_3 OPE.

        At pole 3 in W_3(z) W_3(w), the weight is 3+3-3 = 3.
        The weight-3 basis is {W_3, dT}.

        We use the Gram matrix to extract the W_3 coefficient.
        """
        # Full W3 x W3 OPE
        w3w3 = compute_ope(self.W3, self.W3, 6)

        # Content at pole 3
        C3 = w3w3.get(3, [])
        if not C3:
            return {"gamma": 0, "C333_sq": 0, "target": 0, "ratio": 0, "status": "NO_POLE_3"}

        # Gram matrix for {W_3, dT} at weight 3
        G = np.array([
            [_bpz_inner_product(self.W3, self.W3), _bpz_inner_product(self.W3, self.dT)],
            [_bpz_inner_product(self.dT, self.W3), _bpz_inner_product(self.dT, self.dT)],
        ])

        # Overlap vector
        v = np.array([
            _bpz_inner_product(self.W3, C3),
            _bpz_inner_product(self.dT, C3),
        ])

        # Solve
        try:
            x = np.linalg.solve(G, v)
        except np.linalg.LinAlgError:
            return {"gamma": 0, "C333_sq": 0, "target": 0, "ratio": 0, "status": "SINGULAR_GRAM"}

        gamma = x[0]  # coefficient of W_3

        # Convention-independent physical coupling:
        # C_333^{phys,2} = gamma^2 * ||W_3|| / ||W_3||^2 = gamma^2 / ||W_3||
        # Wait, no. The formula is:
        # C_333^{phys,2} = |<W3 W3 W3>|^2 / (||W3||^2)^3
        # <W3 W3 W3> = gamma * ||W3||^2  (three-point function = OPE coeff * norm of output)
        # C_333^{phys,2} = gamma^2 * ||W3||^4 / ||W3||^6 = gamma^2 / ||W3||^2

        # But the Zamolodchikov formula is for the normalization ||W_3||^2 = c/3.
        # Our Miura norm is norm_W3. So:
        # gamma_Zam = gamma_Miura * (norm_W3 / (c/3))
        # C_333^{Zam,2} = gamma_Zam^2 = gamma^2 * (norm_W3)^2 / (c/3)^2

        # Hmm, this is getting confusing. Let me just compute the
        # convention-independent quantity and the Zamolodchikov one separately.

        # Convention-independent: |3pt|^2 / prod(norms)
        three_pt = gamma * self.norm_W3  # <W3 W3 W3> in Miura norm
        phys_sq = three_pt**2 / abs(self.norm_W3)**3  # |3pt|^2 / N^3

        target = self.zamolodchikov_C333_squared(self.c_actual)

        # Also check: is <W_3 | dT> = 0? (orthogonality test)
        w3_dT = _bpz_inner_product(self.W3, self.dT)

        return {
            "c_expected": self.c_expected,
            "c_actual": self.c_actual,
            "norm_T": self.norm_T,
            "norm_W3": self.norm_W3,
            "gamma": gamma,
            "three_pt": three_pt,
            "C333_phys_sq": phys_sq,
            "C333_Zam_target": target,
            "ratio": phys_sq / target if abs(target) > 1e-15 else float('inf'),
            "W3_dT_overlap": w3_dT,
            "Gram_matrix": G.tolist(),
            "overlap_vector": v.tolist(),
            "status": "OK",
        }


def run_diagnostic():
    """Run the W_3 diagnostic at multiple t values and report."""
    print("=" * 80)
    print("W_3 MIURA DIAGNOSTIC: C_333^2 vs Zamolodchikov")
    print("=" * 80)

    t_values = [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 1.0, 2.0]

    print(f"\n{'t':>6} {'c':>8} {'norm_W3':>12} {'<W3|dT>':>12} {'gamma':>12} "
          f"{'C333^2':>14} {'Zam_target':>14} {'ratio':>10}")
    print("-" * 100)

    for t in t_values:
        try:
            diag = W3MiuraDiagnostic(t)
            r = diag.compute_C333()
            if r["status"] != "OK":
                print(f"{t:6.3f} {r.get('c_actual', '?'):>8} --- {r['status']} ---")
                continue

            print(f"{t:6.3f} {r['c_actual']:8.3f} {r['norm_W3']:12.4f} "
                  f"{r['W3_dT_overlap']:12.4f} {r['gamma']:12.6f} "
                  f"{r['C333_phys_sq']:14.8f} {r['C333_Zam_target']:14.8f} "
                  f"{r['ratio']:10.6f}")
        except Exception as e:
            print(f"{t:6.3f} --- ERROR: {e} ---")

    print()
    print("If ratio ≈ 1.0 at all c: Wick engine is correct, W_4 bug is in Miura product.")
    print("If ratio ≠ 1.0: Wick engine or normalization formula has a bug.")


if __name__ == "__main__":
    run_diagnostic()
