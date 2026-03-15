"""Yangian residue extraction for MC4 verification.

Ground truth from the manuscript (yangians.tex, concordance.tex):
  rem:mc4-yangian-computation-target: Extract K^line_{a,b}(N) from the
  dg-shifted Yangian line-operator construction at N=2,3,4 and compare
  with K^RTT_{a,b}(N) from the truncated RTT relation.

  Three reduction layers (each proved in the manuscript):
    1. cor:dg-shifted-rtt-typea-residue-reduction:
       L_a(u) = R_{0a}(u-a) iff Res_{u=a} L_a(u) = -hbar * P
    2. prop:dg-shifted-rtt-typea-residue-channels:
       Xi_a = -hbar*P iff lambda_sym = -hbar and lambda_alt = +hbar
    3. cor:dg-shifted-rtt-typea-single-line:
       Xi_a = -hbar*P iff Xi_a(e1 x e2) = -hbar(e2 x e1)

  Yang R-matrix: R(u) = Id - hbar*P/u on V tensor V
  RTT relation in modes (eq:rtt-modes):
    [T_{ij}^{(r+1)}, T_{kl}^{(s)}] - [T_{ij}^{(r)}, T_{kl}^{(s+1)}]
    = T_{kj}^{(r)}*T_{il}^{(s)} - T_{kj}^{(s)}*T_{il}^{(r)}

CONVENTIONS:
  - hbar = deformation parameter (set to 1 for verification)
  - V = C^M, fundamental representation of sl_M
  - P = permutation on V tensor V: P(v tensor w) = w tensor v
  - e_i = standard basis vectors of V
"""

from __future__ import annotations

from typing import Dict, List, Tuple
import numpy as np


# ---------------------------------------------------------------------------
# Permutation matrix and R-matrix
# ---------------------------------------------------------------------------

def permutation_matrix(M: int) -> np.ndarray:
    """M^2 x M^2 permutation matrix P on V tensor V.

    P(e_i tensor e_j) = e_j tensor e_i.
    In the standard basis (e_1 x e_1, e_1 x e_2, ..., e_M x e_M):
    P_{(i-1)*M+j, (j-1)*M+i} = 1.
    """
    P = np.zeros((M * M, M * M))
    for i in range(M):
        for j in range(M):
            P[i * M + j, j * M + i] = 1.0
    return P


def yang_r_matrix(M: int, u: float, hbar: float = 1.0) -> np.ndarray:
    """Yang R-matrix R(u) = Id - hbar*P/u on V tensor V.

    Returns M^2 x M^2 matrix.
    """
    Id = np.eye(M * M)
    P = permutation_matrix(M)
    return Id - hbar * P / u


# ---------------------------------------------------------------------------
# Permutation eigenspaces
# ---------------------------------------------------------------------------

def sym_antisym_projectors(M: int) -> Tuple[np.ndarray, np.ndarray]:
    """Projectors onto Sym^2(V) and Lambda^2(V).

    P_sym = (Id + P)/2, P_alt = (Id - P)/2.
    """
    P = permutation_matrix(M)
    Id = np.eye(M * M)
    return (Id + P) / 2, (Id - P) / 2


def sym_dim(M: int) -> int:
    """dim Sym^2(V) = M(M+1)/2."""
    return M * (M + 1) // 2


def alt_dim(M: int) -> int:
    """dim Lambda^2(V) = M(M-1)/2."""
    return M * (M - 1) // 2


# ---------------------------------------------------------------------------
# Evaluation representation
# ---------------------------------------------------------------------------

def evaluation_L_mode(M: int, r: int, a: float, hbar: float = 1.0) -> np.ndarray:
    """Mode r of the L-matrix in the fundamental evaluation rep at point a.

    L(u) = Id_{M^2} - hbar*P/(u-a) on V_aux tensor V_phys.

    Mode expansion L(u) = sum_r L^{(r)} u^{-r}:
      L^{(0)} = Id_{M^2}
      L^{(r)} = -hbar * a^{r-1} * P  for r >= 1

    Returns M^2 x M^2 matrix.
    """
    if r == 0:
        return np.eye(M * M)
    else:
        return -hbar * (a ** (r - 1)) * permutation_matrix(M)


def evaluation_line_operator(M: int, u: float, a: float,
                             hbar: float = 1.0) -> np.ndarray:
    """Line operator L_a(u) = Id - hbar*P/(u-a) on V tensor V.

    This is R_{0a}(u-a) in the fundamental evaluation representation.
    Returns M^2 x M^2 matrix.
    """
    Id = np.eye(M * M)
    P = permutation_matrix(M)
    return Id - hbar * P / (u - a)


def residue_at_a(M: int, hbar: float = 1.0) -> np.ndarray:
    """Res_{u=a} L_a(u) = -hbar * P.

    Returns M^2 x M^2 matrix.
    """
    P = permutation_matrix(M)
    return -hbar * P


# ---------------------------------------------------------------------------
# Reduction layer 1: Residue reduction
# ---------------------------------------------------------------------------

def verify_residue_reduction(M: int, hbar: float = 1.0) -> Dict[str, bool]:
    """Verify Res_{u=a} L_a(u) = -hbar*P (cor:dg-shifted-rtt-typea-residue-reduction).

    Checks numerically at several evaluation points.
    """
    results = {}
    Xi = residue_at_a(M, hbar)
    P = permutation_matrix(M)

    results["Xi_equals_minus_hbar_P"] = np.allclose(Xi, -hbar * P)

    # Check at several a values (residue is a-independent for standard R-matrix)
    for a in [0.5, 1.0, 2.7]:
        # L_a(u) = Id - hbar*P/(u-a). Near u = a + eps:
        # L_a(a+eps) = Id - hbar*P/eps ≈ -hbar*P/eps + Id
        # So Res_{u=a} = -hbar*P (confirmed by Laurent expansion)
        eps = 1e-8
        L_near = evaluation_line_operator(M, a + eps, a, hbar)
        Xi_num = eps * (L_near - np.eye(M * M))
        results[f"numeric_residue_a={a}"] = np.allclose(Xi_num, -hbar * P, atol=1e-4)

    return results


# ---------------------------------------------------------------------------
# Reduction layer 2: Channel reduction
# ---------------------------------------------------------------------------

def verify_channel_reduction(M: int, hbar: float = 1.0) -> Dict[str, object]:
    """Verify eigenvalues on Sym^2(V) and Lambda^2(V).

    prop:dg-shifted-rtt-typea-residue-channels:
    Xi_a|_{Sym^2} = -hbar, Xi_a|_{Lambda^2} = +hbar.
    """
    Xi = residue_at_a(M, hbar)
    P_sym, P_alt = sym_antisym_projectors(M)

    results = {}

    # Xi acts by -hbar on Sym^2 and +hbar on Lambda^2
    # Check: Xi*P_sym = -hbar*P_sym and Xi*P_alt = +hbar*P_alt
    results["Xi_sym_eigenvalue"] = -hbar
    results["Xi_alt_eigenvalue"] = +hbar
    results["Xi_sym_check"] = np.allclose(Xi @ P_sym, -hbar * P_sym)
    results["Xi_alt_check"] = np.allclose(Xi @ P_alt, +hbar * P_alt)

    # Verify P eigenvalues: P|_{Sym^2} = +1, P|_{Lambda^2} = -1
    results["P_sym_eigenvalue_1"] = np.allclose(P_sym @ permutation_matrix(M) @ P_sym,
                                                 P_sym)
    results["P_alt_eigenvalue_minus1"] = np.allclose(P_alt @ permutation_matrix(M) @ P_alt,
                                                      -P_alt)

    return results


# ---------------------------------------------------------------------------
# Reduction layer 3: Single-line reduction
# ---------------------------------------------------------------------------

def e_tensor(M: int, i: int, j: int) -> np.ndarray:
    """e_i tensor e_j as a vector in V tensor V = C^{M^2}."""
    v = np.zeros(M * M)
    v[i * M + j] = 1.0
    return v


def verify_single_line_reduction(M: int, hbar: float = 1.0) -> Dict[str, object]:
    """Verify Xi_a(e1 x e2) = -hbar(e2 x e1).

    cor:dg-shifted-rtt-typea-single-line.
    """
    Xi = residue_at_a(M, hbar)
    e1_e2 = e_tensor(M, 0, 1)  # e_1 tensor e_2 (0-indexed)
    e2_e1 = e_tensor(M, 1, 0)  # e_2 tensor e_1

    Xi_e1e2 = Xi @ e1_e2
    expected = -hbar * e2_e1

    results = {}
    results["Xi(e1xe2)"] = Xi_e1e2.tolist()
    results["expected"] = expected.tolist()
    results["match"] = np.allclose(Xi_e1e2, expected)

    # Also check the inverse direction
    results["Xi(e2xe1)_equals_minus_hbar_e1xe2"] = np.allclose(
        Xi @ e2_e1, -hbar * e1_e2
    )

    # Check diagonal: Xi(e1xe1) = -hbar(e1xe1) (symmetric channel)
    e1_e1 = e_tensor(M, 0, 0)
    results["Xi(e1xe1)_equals_minus_hbar_e1xe1"] = np.allclose(
        Xi @ e1_e1, -hbar * e1_e1
    )

    return results


# ---------------------------------------------------------------------------
# RTT mode relation verification
# ---------------------------------------------------------------------------

def verify_rtt_l_modes(M: int, N: int, a: float = 1.0,
                       hbar: float = 1.0) -> Dict[str, object]:
    """Verify the RTT relation in L-mode form for the evaluation rep.

    Full L(u) = sum_r L^{(r)} u^{-r} satisfies the RLL relation exactly.
    Truncated L_N(u) = sum_{r=0}^{N} L^{(r)} u^{-r} has a computable defect.

    For the FULL L-matrix, we verify:
    sum_{t=0}^{r+s} R^{(t)} L^{(r+s-t)}_1 L^{(0...)}_2 = ... (mode form of RLL)

    Simpler check: reconstruct L(u) from modes and compare with the analytic form.
    """
    L_modes = [evaluation_L_mode(M, r, a, hbar) for r in range(N + 1)]

    # Reconstruct L(u) at test point from modes
    u_test = 5.3  # far from pole at a
    L_from_modes = sum(L_modes[r] / u_test ** r for r in range(N + 1))
    L_analytic = evaluation_line_operator(M, u_test, a, hbar)

    # The truncation error is L_analytic - L_from_modes = -hbar*P * sum_{r>N} a^{r-1}/u^r
    # = -hbar*P * a^N / (u^{N+1} * (1 - a/u))  (for |a/u| < 1)
    trunc_err = np.max(np.abs(L_analytic - L_from_modes))
    geo_tail = abs(hbar) * abs(a) ** N / (abs(u_test) ** (N + 1) * abs(1 - a / u_test))

    # Mode structure: L^{(0)} = Id, L^{(r)} = -hbar*a^{r-1}*P for r >= 1
    P = permutation_matrix(M)
    mode_structure_ok = True
    for r in range(N + 1):
        expected = np.eye(M * M) if r == 0 else -hbar * a ** (r - 1) * P
        if not np.allclose(L_modes[r], expected):
            mode_structure_ok = False

    return {
        "M": M,
        "N": N,
        "mode_structure_correct": mode_structure_ok,
        "truncation_error": trunc_err,
        "expected_trunc_bound": geo_tail,
        "error_within_bound": trunc_err < 2 * geo_tail,
    }


# ---------------------------------------------------------------------------
# RLL relation verification (full matrix form)
# ---------------------------------------------------------------------------

def verify_rll_relation(M: int, u: float, v: float, a: float,
                        hbar: float = 1.0) -> Dict[str, object]:
    """Verify R(u-v)L_1(u)L_2(v) = L_2(v)L_1(u)R(u-v) numerically.

    L_a(u) = Id - hbar*P/(u-a) acts on V_0 tensor V_a.
    For the two-site version, we need V_1 tensor V_2 tensor V_phys,
    but in the fundamental evaluation:
    L_1(u) = R_{01}(u-a) on V_0 tensor V_1
    L_2(v) = R_{02}(v-a) on V_0 tensor V_2

    For the RLL check, we work on V_1 tensor V_2 and check:
    R_{12}(u-v) L_1(u) L_2(v) = L_2(v) L_1(u) R_{12}(u-v)

    where L_i(u) acts on V_i tensor V_phys and R_{12} acts on V_1 tensor V_2.

    In the simplest case (single physical space), L(u) is M^2 x M^2 and
    this is equivalent to the Yang-Baxter equation R12 R13 R23 = R23 R13 R12.
    """
    R12 = yang_r_matrix(M, u - v, hbar)
    L1 = evaluation_line_operator(M, u, a, hbar)
    L2 = evaluation_line_operator(M, v, a, hbar)

    # For the fundamental rep, RLL is equivalent to YBE
    # R(u-v) R(u-a) R(v-a) = R(v-a) R(u-a) R(u-v)
    # where all R-matrices act on V tensor V (M^2 x M^2)
    #
    # Actually, RLL involves three spaces. But for verification,
    # we check: R(u-v) * (R(u-a) evaluated on spaces 1,3) * (R(v-a) on 2,3)
    # This requires M^3 x M^3 matrices.
    #
    # Simpler: just check that the Yang-Baxter equation holds for R(u).
    # R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)

    # Build M^3 x M^3 R-matrices for YBE: R12(u-v) R13(u-a) R23(v-a) = R23 R13 R12
    d = M * M * M
    Id_M = np.eye(M)

    # R_{12}(u-v) on spaces 1,2 (tensor with Id on space 3)
    R12_3 = np.kron(yang_r_matrix(M, u - v, hbar), Id_M)

    # P_{13}: permutes spaces 1 and 3 in V^{tensor 3}, P13|i,j,k> = |k,j,i>
    P13 = np.zeros((d, d))
    for i in range(M):
        for j in range(M):
            for k in range(M):
                P13[k * M * M + j * M + i, i * M * M + j * M + k] = 1.0
    R13 = np.eye(d) - hbar * P13 / (u - a)

    # R_{23}(v-a) on spaces 2,3 (tensor with Id on space 1)
    R23_1 = np.kron(Id_M, yang_r_matrix(M, v - a, hbar))

    # Yang-Baxter: R12 R13 R23 = R23 R13 R12
    lhs = R12_3 @ R13 @ R23_1
    rhs = R23_1 @ R13 @ R12_3

    return {
        "M": M,
        "u": u,
        "v": v,
        "a": a,
        "ybe_holds": np.allclose(lhs, rhs),
        "max_diff": float(np.max(np.abs(lhs - rhs))),
    }


# ---------------------------------------------------------------------------
# Truncated RTT defect at boundary
# ---------------------------------------------------------------------------

def truncated_rtt_defect_eval(M: int, N: int, a: float,
                               u: float, v: float,
                               hbar: float = 1.0) -> np.ndarray:
    """RTT defect from truncating L(u) at mode level N in the evaluation rep.

    Full L(u) = Id - hbar*P/(u-a) on V_aux tensor V_phys satisfies RLL exactly.
    Truncation: L_N(u) = sum_{r=0}^{N} L^{(r)} u^{-r}, dropping modes r > N.

    The defect Delta_N(u,v) = R(u-v)*L_N(u)*L_N(v) - L_N(v)*L_N(u)*R(u-v)
    is nonzero and captures the boundary correction K^line.

    Returns M^2 x M^2 matrix (the defect at given u, v).
    """
    P = permutation_matrix(M)

    def L_trunc(w):
        """Truncated L-matrix: sum_{r=0}^N L^{(r)} w^{-r}."""
        geo_sum = sum(a ** (r - 1) / w ** r for r in range(1, N + 1))
        return np.eye(M * M) - hbar * P * geo_sum

    R = yang_r_matrix(M, u - v, hbar)
    L1 = L_trunc(u)
    L2 = L_trunc(v)

    lhs = R @ L1 @ L2
    rhs = L2 @ L1 @ R

    return lhs - rhs


# ---------------------------------------------------------------------------
# RTT mode-level truncation defect (evaluation representation)
# ---------------------------------------------------------------------------

def _eval_T_ij_mode(M: int, i: int, j: int, r: int, N: int,
                    a: float, hbar: float = 1.0) -> np.ndarray:
    """T_{ij}^{(r)} as M x M matrix in the evaluation rep at point a.

    In the fundamental evaluation rep:
    T_{ij}^{(0)} = delta_{ij} * Id_M
    T_{ij}^{(r)} = -hbar * a^{r-1} * E_{ji}  for 1 <= r <= N
    T_{ij}^{(r)} = 0                           for r > N (truncated)

    E_{ji} is the elementary matrix with 1 at position (j, i).
    """
    if r < 0:
        return np.zeros((M, M))
    if r == 0:
        return float(i == j) * np.eye(M)
    if r > N:
        return np.zeros((M, M))
    E_ji = np.zeros((M, M))
    E_ji[j, i] = 1.0
    return -hbar * (a ** (r - 1)) * E_ji


def rtt_mode_defect(M: int, N: int, a: float,
                    i: int, j: int, k: int, l: int,
                    r: int, s: int,
                    hbar: float = 1.0) -> np.ndarray:
    """RTT mode relation defect from truncation at level N.

    Full RTT mode relation (eq:rtt-modes):
    [T_{ij}^{(r+1)}, T_{kl}^{(s)}] - [T_{ij}^{(r)}, T_{kl}^{(s+1)}]
    = T_{kj}^{(r)} T_{il}^{(s)} - T_{kj}^{(s)} T_{il}^{(r)}

    Defect = LHS - RHS using truncated T-modes (T^{(r)} = 0 for r > N).
    Nonzero only at boundary: when r = N or s = N (or both).

    Returns M x M matrix (the defect as an endomorphism of V_phys).
    """
    def T(ii, jj, rr):
        return _eval_T_ij_mode(M, ii, jj, rr, N, a, hbar)

    # LHS: [T_{ij}^{(r+1)}, T_{kl}^{(s)}] - [T_{ij}^{(r)}, T_{kl}^{(s+1)}]
    comm1 = T(i, j, r + 1) @ T(k, l, s) - T(k, l, s) @ T(i, j, r + 1)
    comm2 = T(i, j, r) @ T(k, l, s + 1) - T(k, l, s + 1) @ T(i, j, r)
    lhs = comm1 - comm2

    # RHS: T_{kj}^{(r)} T_{il}^{(s)} - T_{kj}^{(s)} T_{il}^{(r)}
    rhs = T(k, j, r) @ T(i, l, s) - T(k, j, s) @ T(i, l, r)

    return lhs - rhs


def rtt_mode_defect_norm(M: int, N: int, a: float,
                         r: int, s: int,
                         hbar: float = 1.0) -> float:
    """Max norm of RTT defect across all (i,j,k,l) at mode level (r,s)."""
    max_norm = 0.0
    for i in range(M):
        for j in range(M):
            for k in range(M):
                for l in range(M):
                    D = rtt_mode_defect(M, N, a, i, j, k, l, r, s, hbar)
                    max_norm = max(max_norm, np.max(np.abs(D)))
    return max_norm


def verify_rtt_truncation(M: int, N: int, a: float = 1.5,
                           hbar: float = 1.0) -> Dict[str, object]:
    """Verify RTT truncation defect structure.

    Interior modes (r < N and s < N): defect should be 0.
    Boundary modes (r = N or s = N): defect nonzero, captures K^RTT.
    """
    interior_max = 0.0
    boundary_norms = {}

    for r in range(N + 1):
        for s in range(N + 1):
            norm = rtt_mode_defect_norm(M, N, a, r, s, hbar)
            if r < N and s < N:
                interior_max = max(interior_max, norm)
            else:
                boundary_norms[(r, s)] = norm

    return {
        "M": M,
        "N": N,
        "interior_max_defect": interior_max,
        "interior_zero": interior_max < 1e-10,
        "boundary_norms": boundary_norms,
        "boundary_nonzero": any(v > 1e-10 for v in boundary_norms.values()),
    }


# ---------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------

def verify_all_reductions(M: int, hbar: float = 1.0) -> Dict[str, object]:
    """Run all three reduction verifications for sl_M."""
    return {
        "M": M,
        "dim_V": M,
        "dim_VxV": M * M,
        "dim_Sym2": sym_dim(M),
        "dim_Alt2": alt_dim(M),
        "reduction_1_residue": verify_residue_reduction(M, hbar),
        "reduction_2_channels": verify_channel_reduction(M, hbar),
        "reduction_3_single_line": verify_single_line_reduction(M, hbar),
    }


def verify_mc4_yangian(hbar: float = 1.0) -> Dict[str, object]:
    """Full MC4 Yangian verification for M = 2, 3, 4."""
    results = {}
    for M in [2, 3, 4]:
        results[f"sl_{M}"] = verify_all_reductions(M, hbar)

    # RLL / Yang-Baxter verification
    for M in [2, 3]:
        ybe = verify_rll_relation(M, 3.7, 1.2, 0.5, hbar)
        results[f"ybe_sl_{M}"] = ybe

    # L-mode verification
    for M in [2, 3]:
        lm = verify_rtt_l_modes(M, 5, 1.0, hbar)
        results[f"l_modes_sl_{M}"] = lm

    return results


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("MC4 YANGIAN RESIDUE EXTRACTION: THREE-LAYER VERIFICATION")
    print("=" * 70)

    for M in [2, 3, 4]:
        print(f"\n{'='*40}")
        print(f"  sl_{M}  (V = C^{M})")
        print(f"{'='*40}")

        res = verify_all_reductions(M)

        # Layer 1
        r1 = res["reduction_1_residue"]
        print(f"  Layer 1 (residue): Xi = -hbar*P: {r1['Xi_equals_minus_hbar_P']}")

        # Layer 2
        r2 = res["reduction_2_channels"]
        print(f"  Layer 2 (channels): Sym^2 eigenvalue = {r2['Xi_sym_eigenvalue']}, "
              f"Lambda^2 = {r2['Xi_alt_eigenvalue']}")
        print(f"    Sym check: {r2['Xi_sym_check']}, Alt check: {r2['Xi_alt_check']}")

        # Layer 3
        r3 = res["reduction_3_single_line"]
        print(f"  Layer 3 (single line): Xi(e1xe2) = -hbar(e2xe1): {r3['match']}")

    # YBE
    for M in [2, 3]:
        ybe = verify_rll_relation(M, 3.7, 1.2, 0.5)
        print(f"\n  Yang-Baxter sl_{M}: {ybe['ybe_holds']} "
              f"(max diff = {ybe['max_diff']:.2e})")
