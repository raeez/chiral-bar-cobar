r"""Shadow obstruction tower and r-matrix for affine sl_3 at level k.

Computes the complete shadow obstruction tower for the affine Kac-Moody
algebra sl_3-hat_k, verifying class L (Lie/tree) assignment, and the
r-matrix r(z) = Omega/z with CYBE verification in the fundamental.

Shadow obstruction tower data for sl_3-hat_k:
    kappa = dim(sl_3)(k + h^vee) / (2 h^vee) = 8(k+3)/6 = 4(k+3)/3
    S_3   = 1   (cubic shadow, universal for all affine KM; Lie bracket)
    S_4   = 0   (quartic killed by Jacobi identity)
    Delta = 8 * kappa * S_4 = 0
    Class L: tower terminates at arity 3

The cubic shadow C(x,y,z) = kappa(x, [y,z]) on the strict current-level
sector; the scalar projection S_3 = 1 is universal for all simple g
(thm:affine-cubic-normal-form, cor:affine-postnikov-termination).

The quartic obstruction o_4 = (1/2){C, C}_H is the Jacobiator, which
vanishes by the Jacobi identity.  All higher obstructions vanish by
induction.

The r-matrix r(z) = Omega_{sl_3} / z is the collision residue of the
bar propagator d log E(z,w) (AP19: bar absorbs one pole order from
the OPE).  In the fundamental representation V = C^3:
    Omega = P - I/3    (standard sl_3 identity)
where P is the permutation operator on V tensor V.

The classical Yang-Baxter equation (CYBE):
    [r_12(u), r_13(u+v)] + [r_12(u), r_23(v)] + [r_13(u+v), r_23(v)] = 0

Ground truth references:
    kac_moody.tex: sec:sl3-genus-one-pipeline, thm:sl3-genus1-curvature,
        thm:affine-cubic-normal-form, cor:affine-postnikov-termination
    sl3_bar.py: structure constants, Killing form
    yangian_rmatrix_sl3.py: fund rep matrices, Casimir tensor, YBE
    discriminant_atlas_complete.py: alpha(g) = 1 universal for KM
    landscape_census.tex: kappa(sl_3_k) = 4(k+3)/3
    shadow_tower_recursive.py: compute_shadow_tower, depth_classification

Conventions:
    Cohomological grading (|d| = +1).
    Killing form: trace form in the fundamental, (H_i, H_j) = A_{ij}.
    h^vee(sl_3) = 3.  dim(sl_3) = 8.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

import numpy as np
from sympy import Rational, Symbol, simplify, sqrt

from compute.lib.sl3_bar import (
    DIM_G,
    GEN_NAMES,
    H1, H2, E1, E2, E3, F1, F2, F3,
    sl3_structure_constants,
    sl3_killing_form,
    sl3_sugawara_c,
)
from compute.lib.shadow_tower_recursive import (
    ShadowTower,
    compute_shadow_tower,
    depth_classification,
    shadow_metric_from_data,
)
from compute.lib.yangian_rmatrix_sl3 import (
    casimir_tensor_fund,
    fund_rep_matrices,
    inverse_killing_form,
    permutation_matrix_3,
    kappa_sl3,
)


# ============================================================
# Constants
# ============================================================

H_VEE = 3       # dual Coxeter number for sl_3
DIM_SL3 = 8     # dimension of sl_3
FUND_DIM = 3    # dimension of the fundamental representation

k = Symbol('k')


# ============================================================
# Shadow obstruction tower data for sl_3-hat_k
# ============================================================

def sl3_kappa(k_val=None):
    r"""Modular characteristic kappa(sl_3_k) = 4(k+3)/3.

    kappa = dim(g)(k + h^vee) / (2 h^vee) = 8(k+3)/6 = 4(k+3)/3.

    Ground truth: landscape_census.tex, rem:sl3-universality in kac_moody.tex.
    """
    if k_val is not None:
        return Rational(4, 3) * (k_val + H_VEE)
    return Rational(4, 3) * (k + H_VEE)


def sl3_central_charge(k_val=None):
    r"""Sugawara central charge c = 8k/(k+3) for sl_3-hat_k.

    c = k * dim(g) / (k + h^vee) = 8k/(k+3).
    """
    if k_val is not None:
        return Rational(8) * k_val / (k_val + H_VEE)
    return Rational(8) * k / (k + H_VEE)


def sl3_dual_level(k_val=None):
    r"""Koszul dual level k' = -k - 2h^vee = -k - 6 for sl_3.

    From thm:sl3-koszul-dual: (sl_3-hat_k)^! = sl_3-hat_{-k-6}.
    """
    if k_val is not None:
        return -k_val - 2 * H_VEE
    return -k - 2 * H_VEE


def sl3_cubic_shadow():
    r"""Cubic shadow coefficient S_3 = 1 (universal for all affine KM).

    The cubic shadow C(x,y,z) = kappa(x, [y,z]) on the strict current-level
    sector.  The scalar projection S_3 = alpha = 1 is universal for all
    simple g (discriminant_atlas_complete.py, thm:affine-cubic-normal-form).

    The value S_3 = 1 (not 0, not 2): it arises from the normalization
    of the cubic shadow in the recursive tower framework.  For Virasoro,
    S_3 = 2 (the gravitational cubic); for affine KM, S_3 = 1 (the Lie cubic).
    """
    return Rational(1)


def sl3_quartic_shadow():
    r"""Quartic shadow S_4 = 0 for all affine KM.

    The quartic obstruction o_4 = (1/2){C, C}_H is the Jacobiator,
    which vanishes by the Jacobi identity (thm:affine-cubic-normal-form).
    """
    return Rational(0)


def sl3_discriminant():
    r"""Critical discriminant Delta = 8*kappa*S_4 = 0 for sl_3-hat.

    Delta = 0 => class L (Lie/tree archetype), tower terminates at arity 3.
    """
    return Rational(0)


# ============================================================
# Full shadow obstruction tower computation via recursive framework
# ============================================================

def sl3_shadow_tower(k_val=None, max_arity: int = 20) -> ShadowTower:
    r"""Compute the full shadow obstruction tower for sl_3-hat_k.

    Uses the recursive framework from shadow_tower_recursive.py.
    Since S_4 = 0 (and hence Delta = 0), the tower is class L and
    terminates at arity 3: S_r = 0 for all r >= 4.

    Parameters:
        k_val: Level (sympy expression or number). If None, uses symbol k.
        max_arity: Maximum arity to compute (default 20).

    Returns:
        ShadowTower instance with exact coefficients.
    """
    kappa_val = sl3_kappa(k_val)
    alpha_val = sl3_cubic_shadow()
    s4_val = sl3_quartic_shadow()

    numerical_point = None
    if k_val is not None:
        try:
            float(k_val)
            # k_val is numeric; no substitution needed
        except (TypeError, ValueError):
            numerical_point = {k: k_val}

    tower = compute_shadow_tower(
        kappa_val=kappa_val,
        alpha_val=alpha_val,
        S4_val=s4_val,
        max_arity=max_arity,
        algebra_name=f"sl_3-hat at level {k_val if k_val is not None else 'k'}",
        numerical_point=numerical_point,
    )

    return tower


def sl3_shadow_tower_numeric(k_num: float, max_arity: int = 20) -> ShadowTower:
    r"""Compute the shadow obstruction tower for sl_3-hat at a numeric level k.

    Parameters:
        k_num: Numeric level value (float).
        max_arity: Maximum arity (default 20).

    Returns:
        ShadowTower with numerical coefficients.
    """
    kappa_num = 4.0 * (k_num + H_VEE) / 3.0
    alpha_num = 1.0
    s4_num = 0.0

    tower = compute_shadow_tower(
        kappa_val=kappa_num,
        alpha_val=alpha_num,
        S4_val=s4_num,
        max_arity=max_arity,
        algebra_name=f"sl_3-hat at k = {k_num}",
    )

    return tower


# ============================================================
# Depth classification verification
# ============================================================

def verify_class_L() -> Tuple[str, int]:
    r"""Verify that sl_3-hat is class L (depth 3).

    Class L requires: alpha != 0 and Delta = 0.
    For sl_3: alpha = 1 (nonzero), Delta = 8*kappa*0 = 0.
    """
    kappa_val = sl3_kappa()
    alpha_val = sl3_cubic_shadow()
    s4_val = sl3_quartic_shadow()
    return depth_classification(kappa_val, alpha_val, s4_val)


def verify_termination(k_val=None, check_arity: int = 15) -> bool:
    r"""Verify that S_r = 0 for all r >= 4.

    For class L, the shadow metric Q_L(t) is a perfect square:
        Q_L(t) = (2*kappa + 3*alpha*t)^2
    so sqrt(Q_L) is a POLYNOMIAL of degree 1 in t, giving only
    two nonzero Taylor coefficients (a_0, a_1), hence S_r = 0 for r >= 4.

    Parameters:
        k_val: Level value for numeric check (default: k=1).
        check_arity: Check up to this arity (default 15).

    Returns:
        True if all S_r = 0 for r in [4, check_arity].
    """
    if k_val is None:
        k_val = 1
    tower = sl3_shadow_tower_numeric(float(k_val), max_arity=check_arity)
    for r in range(4, check_arity + 1):
        sc = tower.coefficients.get(r)
        if sc is not None and sc.numerical is not None:
            if abs(sc.numerical) > 1e-12:
                return False
    return True


# ============================================================
# Koszul duality verification
# ============================================================

def verify_kappa_anti_symmetry(k_val=None) -> bool:
    r"""Verify kappa(sl_3_k) + kappa(sl_3_{k'}) = 0 for k' = -k-6.

    For KM families, kappa + kappa' = 0 (AP24: this is specific to KM,
    NOT universal; W-algebras have kappa + kappa' = rho*K).

    Returns:
        True if kappa(k) + kappa(-k-6) = 0 (symbolically or numerically).
    """
    if k_val is not None:
        kp = sl3_kappa(k_val)
        kp_dual = sl3_kappa(-k_val - 2 * H_VEE)
        return simplify(kp + kp_dual) == 0
    kp = sl3_kappa()
    k_dual = sl3_dual_level()
    kp_dual = sl3_kappa(k_dual)
    return simplify(kp + kp_dual) == 0


def verify_central_charge_sum(k_val=None) -> bool:
    r"""Verify c(k) + c(k') = 2*dim(sl_3) = 16 for k' = -k-6.

    From eq:sl3-parameters: c + c' = 2*dim(sl_3) = 16.
    """
    if k_val is not None:
        c_val = sl3_central_charge(k_val)
        c_dual = sl3_central_charge(-k_val - 2 * H_VEE)
        return simplify(c_val + c_dual - 2 * DIM_SL3) == 0
    c_val = sl3_central_charge()
    k_dual = sl3_dual_level()
    c_dual = sl3_central_charge(k_dual)
    return simplify(c_val + c_dual - 2 * DIM_SL3) == 0


# ============================================================
# Shadow metric verification
# ============================================================

def sl3_shadow_metric(k_val=None):
    r"""Shadow metric Q_L(t) for sl_3-hat_k.

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

    For class L (Delta = 0):
        Q_L(t) = (2*kappa + 3*t)^2
    which is a perfect square.

    Returns:
        (q0, q1, q2, Delta) tuple.
    """
    kappa_val = sl3_kappa(k_val)
    alpha_val = sl3_cubic_shadow()
    s4_val = sl3_quartic_shadow()
    return shadow_metric_from_data(kappa_val, alpha_val, s4_val)


def verify_perfect_square(k_val=None) -> bool:
    r"""Verify Q_L(t) is a perfect square for sl_3-hat (class L).

    A quadratic q0 + q1*t + q2*t^2 is a perfect square iff
    its discriminant q1^2 - 4*q0*q2 = 0.

    For class L: q0 = 4*kappa^2, q1 = 12*kappa*1 = 12*kappa,
    q2 = 9*1^2 + 0 = 9.  Then q1^2 - 4*q0*q2 = 144*kappa^2 - 144*kappa^2 = 0.
    """
    q0, q1, q2, Delta = sl3_shadow_metric(k_val)
    disc = simplify(q1**2 - 4 * q0 * q2)
    return disc == 0


# ============================================================
# r-matrix from bar collision residue
# ============================================================

def sl3_r_matrix(z: complex) -> np.ndarray:
    r"""r-matrix r(z) = Omega / z for sl_3 in the fundamental.

    The bar construction extracts the collision residue of d log E(z,w),
    which absorbs one pole order (AP19).  The OPE has poles at z^{-2}
    (curvature) and z^{-1} (bracket); the r-matrix has a single pole
    at z^{-1}.

    In V tensor V (9x9):
        r(z) = Omega / z = (P - I/3) / z

    Args:
        z: Spectral parameter (nonzero complex number).

    Returns:
        9x9 complex matrix.
    """
    Omega = casimir_tensor_fund()
    return Omega / z


def sl3_R_matrix_yang(z: complex) -> np.ndarray:
    r"""Yang R-matrix R(z) = z*I + P in the fundamental (additive convention).

    This is the exact rational R-matrix for sl_N Yang.  Equivalent to
    R(z) = I + P/z in the multiplicative convention.

    Eigenvalues on V tensor V:
        z + 1 on Sym^2(V)     (dim 6)
        z - 1 on Lambda^2(V)  (dim 3)

    Args:
        z: Spectral parameter.

    Returns:
        9x9 complex matrix.
    """
    P = permutation_matrix_3()
    I = np.eye(FUND_DIM ** 2, dtype=complex)
    return z * I + P


# ============================================================
# Classical Yang-Baxter equation verification
# ============================================================

def _embed_12(M: np.ndarray) -> np.ndarray:
    """Embed 9x9 matrix into factors 1,2 of V^{otimes 3} (27x27)."""
    return np.kron(M, np.eye(FUND_DIM, dtype=complex))


def _embed_23(M: np.ndarray) -> np.ndarray:
    """Embed 9x9 matrix into factors 2,3 of V^{otimes 3} (27x27)."""
    return np.kron(np.eye(FUND_DIM, dtype=complex), M)


def _embed_13(M: np.ndarray) -> np.ndarray:
    """Embed 9x9 matrix into factors 1,3 of V^{otimes 3} (27x27)."""
    N = FUND_DIM
    d = N ** 3
    R13 = np.zeros((d, d), dtype=complex)
    for i in range(N):
        for j in range(N):
            for kk in range(N):
                for ip in range(N):
                    for kp in range(N):
                        row = i * N * N + j * N + kk
                        col = ip * N * N + j * N + kp
                        R13[row, col] += M[i * N + kk, ip * N + kp]
    return R13


def verify_cybe(u: complex, v: complex) -> float:
    r"""Verify the classical Yang-Baxter equation for r(z) = Omega/z.

    CYBE: [r_12(u), r_13(u+v)] + [r_12(u), r_23(v)] + [r_13(u+v), r_23(v)] = 0

    This is the CLASSICAL YBE (commutators, not products).  The r-matrix
    r(z) = Omega/z satisfies CYBE because Omega is the quadratic Casimir
    (invariant under the adjoint action) and [Omega_12, Omega_13 + Omega_23] = 0
    (the "infinitesimal braid relation").

    Args:
        u, v: Spectral parameters (nonzero, u+v nonzero).

    Returns:
        Frobenius norm of the CYBE residual (should be ~0).
    """
    r12 = _embed_12(sl3_r_matrix(u))
    r13 = _embed_13(sl3_r_matrix(u + v))
    r23 = _embed_23(sl3_r_matrix(v))

    # CYBE: [r12, r13] + [r12, r23] + [r13, r23] = 0
    cybe_lhs = (
        (r12 @ r13 - r13 @ r12)
        + (r12 @ r23 - r23 @ r12)
        + (r13 @ r23 - r23 @ r13)
    )

    return float(np.linalg.norm(cybe_lhs))


def verify_quantum_ybe(z1: complex, z2: complex, z3: complex) -> float:
    r"""Verify the quantum Yang-Baxter equation for R(z) = z*I + P.

    R_12(z1-z2) R_13(z1-z3) R_23(z2-z3) = R_23(z2-z3) R_13(z1-z3) R_12(z1-z2)

    Args:
        z1, z2, z3: Spectral parameters.

    Returns:
        Frobenius norm of LHS - RHS (should be ~0).
    """
    R12 = _embed_12(sl3_R_matrix_yang(z1 - z2))
    R13 = _embed_13(sl3_R_matrix_yang(z1 - z3))
    R23 = _embed_23(sl3_R_matrix_yang(z2 - z3))

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(np.linalg.norm(lhs - rhs))


# ============================================================
# Casimir tensor verification
# ============================================================

def verify_casimir_is_P_minus_I_over_N() -> float:
    r"""Verify Omega = P - I/N on V tensor V for N = 3.

    This is the standard sl_N identity for the quadratic Casimir tensor
    in the fundamental representation with trace-form normalization.

    Returns:
        Frobenius norm of Omega - (P - I/3) (should be ~0).
    """
    Omega = casimir_tensor_fund()
    P = permutation_matrix_3()
    I = np.eye(FUND_DIM ** 2)
    expected = P - I / FUND_DIM
    return float(np.linalg.norm(Omega - expected))


# ============================================================
# F_1 and genus-1 invariants
# ============================================================

def sl3_F1(k_val=None):
    r"""Genus-1 amplitude F_1 = kappa/24 for sl_3-hat_k.

    F_1 = kappa/24 = 4(k+3)/(3*24) = (k+3)/18.

    Ground truth: rem:sl3-universality in kac_moody.tex eq after 3588.
    """
    kappa_val = sl3_kappa(k_val)
    return kappa_val / 24


def sl3_F1_dual(k_val=None):
    r"""F_1 for the Koszul dual sl_3-hat_{-k-6}.

    F_1(k') = kappa(k')/24 = 4(-k-6+3)/(3*24) = 4(-k-3)/(3*24) = -(k+3)/18.
    """
    k_dual = sl3_dual_level(k_val)
    return sl3_F1(k_dual)


def verify_F1_complementarity(k_val=None) -> bool:
    r"""Verify F_1(k) + F_1(k') = 0 for the affine pair.

    This is a consequence of kappa anti-symmetry for KM families.
    """
    f1 = sl3_F1(k_val)
    f1_dual = sl3_F1_dual(k_val)
    return simplify(f1 + f1_dual) == 0


# ============================================================
# Comparison with sl_2
# ============================================================

def comparison_sl2_sl3() -> Dict[str, Any]:
    r"""Comparison of shadow obstruction tower data: sl_2 vs sl_3.

    Both are class L (tower terminates at arity 3).
    The universal structure is identical; only dim(g) and h^vee differ.

    sl_2: dim=3, h^vee=2, kappa=3(k+2)/4, S_3=1, S_4=0
    sl_3: dim=8, h^vee=3, kappa=4(k+3)/3, S_3=1, S_4=0
    """
    return {
        'sl_2': {
            'dim': 3,
            'h_vee': 2,
            'kappa': '3(k+2)/4',
            'S_3': 1,
            'S_4': 0,
            'depth_class': 'L',
            'depth': 3,
        },
        'sl_3': {
            'dim': DIM_SL3,
            'h_vee': H_VEE,
            'kappa': '4(k+3)/3',
            'S_3': 1,
            'S_4': 0,
            'depth_class': 'L',
            'depth': 3,
        },
    }


# ============================================================
# Structure constant verification for cubic shadow
# ============================================================

def verify_cubic_from_structure_constants() -> Dict[str, Any]:
    r"""Verify that the cubic shadow C(x,y,z) = kappa(x, [y,z]) is nonzero.

    On the strict current-level sector, the cubic is determined by
    the Lie bracket.  We verify nonvanishing by computing C(H_1, E_1, F_1).

    C(H_1, E_1, F_1) = kappa(H_1, [E_1, F_1]) = kappa(H_1, H_1) = 2
    (since [E_1, F_1] = H_1 and (H_1, H_1) = A_{11} = 2).

    The cubic is nonzero, confirming S_3 != 0.
    """
    bracket = sl3_structure_constants()
    kf = sl3_killing_form()

    # C(H_1, E_1, F_1) = kappa(H_1, [E_1, F_1])
    # [E_1, F_1] = H_1  (coefficient 1)
    ef_bracket = bracket.get((E1, F1), {})
    # kappa(H_1, result)
    c_val = sum(
        float(coeff) * float(kf.get((H1, c_idx), Rational(0)))
        for c_idx, coeff in ef_bracket.items()
    )

    # C(E_3, E_1, F_3) = kappa(E_3, [E_1, F_3])
    # [E_1, F_3] = -F_2  (from sl3_bar.py)
    e1f3_bracket = bracket.get((E1, F3), {})
    c_val_2 = sum(
        float(coeff) * float(kf.get((E3, c_idx), Rational(0)))
        for c_idx, coeff in e1f3_bracket.items()
    )

    return {
        'C(H1,E1,F1)': c_val,  # expected: 2
        'C(E3,E1,F3)': c_val_2,
        'cubic_nonzero': abs(c_val) > 1e-12,
    }


def verify_jacobi_kills_quartic() -> float:
    r"""Verify that the quartic obstruction vanishes by the Jacobi identity.

    The quartic obstruction is o_4 = (1/2){C, C}_H, which equals the
    Jacobiator kappa([x, [y, z]], w) + cyclic.  For a Lie algebra,
    this vanishes identically.

    We verify this numerically by computing the Jacobiator over all
    basis elements and checking it is zero.

    Returns:
        Maximum absolute value of any Jacobiator component (should be ~0).
    """
    bracket = sl3_structure_constants()
    kf = sl3_killing_form()

    def lie_bracket(a: int, b: int) -> Dict[int, float]:
        """Compute [a, b] as a dict {index: coefficient}."""
        br = bracket.get((a, b), {})
        return {idx: float(c) for idx, c in br.items()}

    def kappa_pair(a: int, b: int) -> float:
        """Compute kappa(a, b)."""
        return float(kf.get((a, b), Rational(0)))

    max_jac = 0.0

    for a in range(DIM_G):
        for b in range(DIM_G):
            for c in range(DIM_G):
                for d in range(DIM_G):
                    # Jacobiator: kappa([a, [b, c]], d) + cyclic over (a,b,c)
                    # Term 1: kappa([a, [b, c]], d)
                    bc = lie_bracket(b, c)
                    term1 = 0.0
                    for idx, coeff in bc.items():
                        a_idx = lie_bracket(a, idx)
                        for idx2, coeff2 in a_idx.items():
                            term1 += coeff * coeff2 * kappa_pair(idx2, d)

                    # Term 2: kappa([b, [c, a]], d)
                    ca = lie_bracket(c, a)
                    term2 = 0.0
                    for idx, coeff in ca.items():
                        b_idx = lie_bracket(b, idx)
                        for idx2, coeff2 in b_idx.items():
                            term2 += coeff * coeff2 * kappa_pair(idx2, d)

                    # Term 3: kappa([c, [a, b]], d)
                    ab = lie_bracket(a, b)
                    term3 = 0.0
                    for idx, coeff in ab.items():
                        c_idx = lie_bracket(c, idx)
                        for idx2, coeff2 in c_idx.items():
                            term3 += coeff * coeff2 * kappa_pair(idx2, d)

                    jac = abs(term1 + term2 + term3)
                    if jac > max_jac:
                        max_jac = jac

    return max_jac
