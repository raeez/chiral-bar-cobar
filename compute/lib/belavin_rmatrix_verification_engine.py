r"""Belavin elliptic r-matrix verification engine.

Three independent verification programmes:

(1) DEGENERATION: tau -> i*infinity recovers the trigonometric r-matrix.
    The further limit z -> 0 (or rescaling z -> z/L, L -> inf) recovers
    the rational r-matrix k*Omega/z.

    The Belavin elliptic r-matrix for sl_2 is built from Jacobi theta
    functions theta_{a+1}(z|tau)/theta_1(z|tau).  As Im(tau) -> infinity,
    q = e^{i*pi*tau} -> 0 and the theta functions reduce to their leading
    terms:
        theta_1(z) ~ 2 q^{1/4} sin(pi*z)
        theta_2(z) ~ 2 q^{1/4} cos(pi*z)
        theta_3(z) ~ 1
        theta_4(z) ~ 1
    The weight functions degenerate:
        w_1(z) = theta_2(z)/theta_1(z) * theta_1'(0)/theta_2(0) -> pi*cot(pi*z)
        w_2(z) = theta_3(z)/theta_1(z) * theta_1'(0)/theta_3(0) -> pi/sin(pi*z)
        w_3(z) = theta_4(z)/theta_1(z) * theta_1'(0)/theta_4(0) -> pi/sin(pi*z)
    This is the trigonometric (XXZ) r-matrix.  In the further limit z -> 0:
        pi*cot(pi*z) ~ 1/z, pi/sin(pi*z) ~ 1/z, so r -> Omega/z (rational).

(2) CYBE VERIFICATION: the classical Yang-Baxter equation
        [r_{12}(z_{12}), r_{13}(z_{13})] + [r_{12}(z_{12}), r_{23}(z_{23})]
        + [r_{13}(z_{13}), r_{23}(z_{23})] = 0
    verified numerically at tau = i (the square lattice) and several other
    tau values, at multiple spectral parameter configurations.

(3) CASIMIR EIGENVALUES: the sl_2 Casimir tensor Omega = E tensor F
    + F tensor E + (1/2) H tensor H acts on C^2 tensor C^2 = Sym^2 + wedge^2.
    Via the identity Omega = (C_2^{tot} - C_2^{(1)} - C_2^{(2)})/2 where
    C_2 = EF + FE + H^2/2 has eigenvalue 3/2 on V_{1/2}:
        Sym^2(C^2) = V_1 (spin 1):   Omega eigenvalue = (4 - 3/2 - 3/2)/2 = +1/2
        wedge^2(C^2) = V_0 (spin 0): Omega eigenvalue = (0 - 3/2 - 3/2)/2 = -3/2

Belavin r-matrix construction
------------------------------
For sl_2 in the fundamental representation, the correct Belavin classical
r-matrix uses the Pauli-matrix decomposition (Belavin 1981, Sklyanin 1982):

    r^{Belavin}(z, tau) = sum_{a=1}^{3} w_a(z, tau) * sigma_a tensor sigma_a / 2

where sigma_a are the Pauli matrices, the normalization 1/2 ensures
Omega = sum sigma_a tensor sigma_a / 2, and the weight functions are:

    w_a(z, tau) = theta_{a+1}(z|tau) / theta_1(z|tau) * theta_1'(0|tau) / theta_{a+1}(0|tau)

Each w_a has a simple pole at z=0 with residue 1, so r(z) ~ Omega/z near z=0.
The three channels have DIFFERENT functions (XYZ/8-vertex anisotropy);
only in the rational limit do they all collapse to 1/z.

The level-prefixed r-matrix is: r^{ell}(z, tau) = k * r^{Belavin}(z, tau).
AP126: at k=0, r = 0 (mandatory vanishing check).

Conventions
-----------
- q = e^{i*pi*tau} (the square root of the nome).
- Jacobi theta functions: standard series representations.
- Cohomological grading (|d| = +1).
- sl_2 generators: E = e_{12}, F = e_{21}, H = diag(1,-1).
- Casimir: Omega = E tensor F + F tensor E + (1/2) H tensor H
         = sum_{a=1}^3 sigma_a tensor sigma_a / 2.

References
----------
- Belavin, "Dynamical symmetry of integrable quantum systems" (1981)
- Belavin-Drinfeld, "Solutions of the classical YBE for simple Lie algebras" (1982)
- Sklyanin, "Some algebraic structures connected with the YBE" (1982)
- Bernard, "On the WZW models on the torus" (1988)
- Felder, "Conformal field theory and integrable systems associated
  to elliptic curves" (1994)
- AP19: bar kernel absorbs one pole (OPE pole - 1 = r-matrix pole)
- AP126: level prefix on r-matrix MANDATORY
- AP141: k=0 vanishing check
- C9: affine KM classical r-matrix (two conventions)
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

import numpy as np


# ============================================================
# 0. Constants and Pauli matrices
# ============================================================

PI = np.pi
TWO_PI_I = 2.0j * PI

SIGMA1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA3 = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMAS = [SIGMA1, SIGMA2, SIGMA3]


# ============================================================
# 1. Jacobi theta functions (high-precision numerical)
# ============================================================

def jacobi_theta1(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_1(z|tau) = 2 sum_{n>=0} (-1)^n q^{(n+1/2)^2} sin((2n+1)*pi*z).

    q = e^{i*pi*tau}.  The unique odd theta function; zeros at Z + Z*tau.
    """
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        sign = (-1) ** n
        q_power = q ** ((n + 0.5) ** 2)
        result += sign * q_power * np.sin((2 * n + 1) * PI * z)
    return 2.0 * result


def jacobi_theta2(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_2(z|tau) = 2 sum_{n>=0} q^{(n+1/2)^2} cos((2n+1)*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        q_power = q ** ((n + 0.5) ** 2)
        result += q_power * np.cos((2 * n + 1) * PI * z)
    return 2.0 * result


def jacobi_theta3(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_3(z|tau) = 1 + 2 sum_{n>=1} q^{n^2} cos(2*n*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        q_power = q ** (n ** 2)
        result += 2.0 * q_power * np.cos(2 * n * PI * z)
    return result


def jacobi_theta4(z: complex, tau: complex, n_terms: int = 80) -> complex:
    r"""Jacobi theta_4(z|tau) = 1 + 2 sum_{n>=1} (-1)^n q^{n^2} cos(2*n*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        sign = (-1) ** n
        q_power = q ** (n ** 2)
        result += 2.0 * sign * q_power * np.cos(2 * n * PI * z)
    return result


def jacobi_theta1_prime0(tau: complex, n_terms: int = 80) -> complex:
    r"""theta_1'(0|tau) = 2*pi sum_{n>=0} (-1)^n (2n+1) q^{(n+1/2)^2}.

    Equals pi * theta_2(0) * theta_3(0) * theta_4(0) by the Jacobi triple product.
    """
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        sign = (-1) ** n
        q_power = q ** ((n + 0.5) ** 2)
        result += sign * (2 * n + 1) * q_power
    return 2.0 * PI * result


THETA_FNS = [jacobi_theta2, jacobi_theta3, jacobi_theta4]


# ============================================================
# 2. sl_2 representation data
# ============================================================

def _sl2_fund_matrices() -> Dict[str, np.ndarray]:
    """E, F, H in the fundamental (2x2) of sl_2."""
    E = np.array([[0, 1], [0, 0]], dtype=complex)
    F = np.array([[0, 0], [1, 0]], dtype=complex)
    H = np.array([[1, 0], [0, -1]], dtype=complex)
    return {'E': E, 'F': F, 'H': H}


def sl2_casimir_tensor() -> np.ndarray:
    r"""Casimir tensor Omega = E tensor F + F tensor E + (1/2) H tensor H.

    Equivalently, Omega = sum_{a=1}^3 sigma_a tensor sigma_a / 2.
    This is the 4x4 matrix on C^2 tensor C^2.
    """
    result = np.zeros((4, 4), dtype=complex)
    for a in range(3):
        result += np.kron(SIGMAS[a], SIGMAS[a]) / 2.0
    return result


def permutation_operator() -> np.ndarray:
    """Permutation P on C^2 tensor C^2: P(v tensor w) = w tensor v."""
    P = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            P[i * 2 + j, j * 2 + i] = 1.0
    return P


def sym2_projector() -> np.ndarray:
    """Projector onto Sym^2(C^2) inside C^2 tensor C^2."""
    return 0.5 * (np.eye(4, dtype=complex) + permutation_operator())


def wedge2_projector() -> np.ndarray:
    """Projector onto wedge^2(C^2) inside C^2 tensor C^2."""
    return 0.5 * (np.eye(4, dtype=complex) - permutation_operator())


# ============================================================
# 3. Belavin weight functions and r-matrix
# ============================================================

def belavin_weight_function(z: complex, tau: complex, a: int,
                             n_terms: int = 80) -> complex:
    r"""Weight function w_a(z, tau) for the Belavin r-matrix, a in {1,2,3}.

    w_a(z, tau) = theta_{a+1}(z|tau) / theta_1(z|tau) * theta_1'(0|tau) / theta_{a+1}(0|tau)

    Each w_a has a simple pole at z=0 with residue 1.
    """
    if a < 1 or a > 3:
        raise ValueError(f"Channel index a must be 1, 2, or 3, got {a}")
    theta_a_fn = THETA_FNS[a - 1]
    tp0 = jacobi_theta1_prime0(tau, n_terms)
    th1_z = jacobi_theta1(z, tau, n_terms)
    tha_z = theta_a_fn(z, tau, n_terms)
    tha_0 = theta_a_fn(0, tau, n_terms)
    if abs(th1_z) < 1e-300 or abs(tha_0) < 1e-300:
        return complex(float('inf'))
    return tha_z / th1_z * tp0 / tha_0


def belavin_r_matrix_sl2(z: complex, tau: complex,
                          n_terms: int = 80) -> np.ndarray:
    r"""Belavin classical elliptic r-matrix for sl_2, fundamental representation.

    r^{Belavin}(z, tau) = sum_{a=1}^{3} w_a(z, tau) * sigma_a tensor sigma_a / 2

    This has a simple pole at z=0 with residue Omega = sum sigma_a tensor sigma_a / 2.
    The three weight functions w_a are generically distinct (XYZ anisotropy).
    """
    r = np.zeros((4, 4), dtype=complex)
    for a in range(3):
        w_a = belavin_weight_function(z, tau, a + 1, n_terms)
        r += w_a * np.kron(SIGMAS[a], SIGMAS[a]) / 2.0
    return r


def leveled_r_matrix_sl2(z: complex, tau: complex, k: float,
                          n_terms: int = 80) -> np.ndarray:
    r"""Level-prefixed elliptic r-matrix: r^{ell}(z, tau) = k * r^{Belavin}(z, tau).

    AP126: k=0 -> r=0.  AP141: verify this after every construction.
    """
    return k * belavin_r_matrix_sl2(z, tau, n_terms)


# ============================================================
# 4. Trigonometric and rational r-matrices (degeneration targets)
# ============================================================

def trigonometric_r_matrix_sl2(z: complex) -> np.ndarray:
    r"""Trigonometric r-matrix for sl_2 (XXZ/6-vertex limit).

    r^{trig}(z) = pi*cot(pi*z) * sigma_1 tensor sigma_1 / 2
                 + pi/sin(pi*z) * sigma_2 tensor sigma_2 / 2
                 + pi/sin(pi*z) * sigma_3 tensor sigma_3 / 2

    Obtained from the Belavin r-matrix as Im(tau) -> infinity.
    """
    if abs(np.sin(PI * z)) < 1e-300:
        return np.full((4, 4), complex(float('inf')))
    cot_piz = np.cos(PI * z) / np.sin(PI * z)
    csc_piz = 1.0 / np.sin(PI * z)
    r = (PI * cot_piz * np.kron(SIGMA1, SIGMA1) / 2.0
         + PI * csc_piz * np.kron(SIGMA2, SIGMA2) / 2.0
         + PI * csc_piz * np.kron(SIGMA3, SIGMA3) / 2.0)
    return r


def rational_r_matrix_sl2(z: complex) -> np.ndarray:
    r"""Rational r-matrix: Omega / z.

    This is the genus-0 collision residue for affine sl_2.
    The target of the double degeneration tau -> i*inf, z -> 0.
    """
    if abs(z) < 1e-300:
        return np.full((4, 4), complex(float('inf')))
    return sl2_casimir_tensor() / z


# ============================================================
# 5. Embedding operators for triple tensor product
# ============================================================

def _embed_12(M: np.ndarray, d: int = 2) -> np.ndarray:
    """Embed d^2 x d^2 matrix M into slots (1,2) of d^3-dimensional space."""
    return np.kron(M, np.eye(d, dtype=complex))


def _embed_23(M: np.ndarray, d: int = 2) -> np.ndarray:
    """Embed d^2 x d^2 matrix M into slots (2,3) of d^3-dimensional space."""
    return np.kron(np.eye(d, dtype=complex), M)


def _embed_13(M: np.ndarray, d: int = 2) -> np.ndarray:
    """Embed d^2 x d^2 matrix M into slots (1,3) of d^3-dimensional space."""
    n = d
    result = np.zeros((n ** 3, n ** 3), dtype=complex)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    val = M[i * n + k, j * n + l]
                    for m in range(n):
                        result[i * n ** 2 + m * n + k,
                               j * n ** 2 + m * n + l] += val
    return result


# ============================================================
# 6. Verification: CYBE
# ============================================================

def verify_cybe(z1: complex, z2: complex, z3: complex,
                tau: complex, k: float = 1.0,
                n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify the classical Yang-Baxter equation for the Belavin r-matrix.

    CYBE (additive form):
        [r_{12}(z_{12}), r_{13}(z_{13})] + [r_{12}(z_{12}), r_{23}(z_{23})]
        + [r_{13}(z_{13}), r_{23}(z_{23})] = 0

    where z_{ij} = z_i - z_j.

    Returns dict with residual norm, relative error, and pass/fail.
    """
    d = 2
    z12 = z1 - z2
    z13 = z1 - z3
    z23 = z2 - z3

    r12 = _embed_12(leveled_r_matrix_sl2(z12, tau, k, n_terms), d)
    r13 = _embed_13(leveled_r_matrix_sl2(z13, tau, k, n_terms), d)
    r23 = _embed_23(leveled_r_matrix_sl2(z23, tau, k, n_terms), d)

    lhs = (r12 @ r13 - r13 @ r12
           + r12 @ r23 - r23 @ r12
           + r13 @ r23 - r23 @ r13)

    residual = np.linalg.norm(lhs)
    scale = max(np.linalg.norm(r12), np.linalg.norm(r13),
                np.linalg.norm(r23), 1.0)
    relative = residual / scale

    return {
        'z12': z12, 'z13': z13, 'z23': z23,
        'tau': tau, 'k': k,
        'residual': float(residual),
        'relative': float(relative),
        'scale': float(scale),
        'passed': relative < 1e-8,
    }


# ============================================================
# 7. Verification: skew-symmetry
# ============================================================

def verify_skew_symmetry(z: complex, tau: complex, k: float = 1.0,
                          n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify r_{12}(z) + r_{21}(-z) = 0 (classical r-matrix skew-symmetry).

    r_{21}(z) = P r_{12}(z) P where P is the permutation operator.
    """
    r_z = leveled_r_matrix_sl2(z, tau, k, n_terms)
    r_mz = leveled_r_matrix_sl2(-z, tau, k, n_terms)
    P = permutation_operator()

    lhs = r_z + P @ r_mz @ P
    residual = np.linalg.norm(lhs)
    scale = max(np.linalg.norm(r_z), 1e-10)

    return {
        'z': z, 'tau': tau,
        'residual': float(residual),
        'relative': float(residual / scale),
        'passed': residual / scale < 1e-8,
    }


# ============================================================
# 8. Verification: pole structure
# ============================================================

def verify_simple_pole_at_origin(tau: complex,
                                  n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify r^{Belavin}(z, tau) has a simple pole at z=0 with residue Omega.

    Each w_a has residue 1 at z=0, so r(z) ~ (1/z) * Omega as z -> 0.
    We check that z * r(z) -> Omega along several approach directions.
    """
    Omega = sl2_casimir_tensor()
    results = {}
    for label, z_small in [
        ('real', 1e-5),
        ('imag', 1e-5j),
        ('diag', (1 + 1j) * 1e-5 / np.sqrt(2)),
        ('neg_real', -1e-5),
    ]:
        r_z = belavin_r_matrix_sl2(z_small, tau, n_terms)
        residue = z_small * r_z
        err = np.linalg.norm(residue - Omega) / np.linalg.norm(Omega)
        results[label] = {
            'z': z_small,
            'residue_error': float(np.real(err)),
            'passed': float(np.real(err)) < 1e-6,
        }

    all_passed = all(v['passed'] for v in results.values())
    return {'directions': results, 'all_passed': all_passed}


# ============================================================
# 9. Verification: degeneration chain
# ============================================================

def verify_degeneration_to_trigonometric(
    z: complex,
    tau_im_values: List[float] = None,
    n_terms: int = 80,
) -> Dict[str, Any]:
    r"""Verify elliptic -> trigonometric as Im(tau) -> infinity.

    The three weight functions degenerate:
        w_1 -> pi*cot(pi*z),  w_2, w_3 -> pi/sin(pi*z).
    """
    if tau_im_values is None:
        tau_im_values = [2.0, 3.0, 5.0, 8.0, 15.0, 30.0]

    r_trig = trigonometric_r_matrix_sl2(z)
    errors = []
    for im_tau in tau_im_values:
        tau = 1j * im_tau
        r_ell = belavin_r_matrix_sl2(z, tau, n_terms)
        err = np.linalg.norm(r_ell - r_trig) / max(np.linalg.norm(r_trig), 1e-10)
        errors.append(float(np.real(err)))

    monotone = all(
        errors[i] >= errors[i + 1] - 1e-12
        for i in range(len(errors) - 1)
    )

    return {
        'z': z,
        'tau_im_values': tau_im_values,
        'errors': errors,
        'monotone_decreasing': monotone,
        'final_error': errors[-1],
        'passed': errors[-1] < 1e-8,
    }


def verify_degeneration_to_rational(
    tau_im: float = 50.0,
    n_terms: int = 80,
) -> Dict[str, Any]:
    r"""Verify r^{ell}(z, tau) -> Omega/z as z -> 0 (at large Im(tau)).

    This is the double degeneration: first elliptic -> trigonometric
    (large Im(tau)), then trigonometric -> rational (small z).
    We verify z * r(z) -> Omega as z -> 0 with convergence rate O(|z|^2).
    """
    tau = 1j * tau_im
    Omega = sl2_casimir_tensor()
    z_values = [0.1 + 0.05j, 0.05 + 0.03j, 0.02 + 0.01j,
                0.005 + 0.003j, 0.001 + 0.0005j]
    errors = []
    for z in z_values:
        r_ell = belavin_r_matrix_sl2(z, tau, n_terms)
        z_r = z * r_ell
        err = np.linalg.norm(z_r - Omega) / np.linalg.norm(Omega)
        errors.append(float(np.real(err)))

    # Check convergence rate: errors should scale as |z|^2
    z_mags = [abs(z) for z in z_values]
    ratios = []
    for i in range(1, len(errors)):
        if errors[i - 1] > 1e-14 and z_mags[i - 1] > 1e-14:
            # error ~ C * |z|^2, so log(err) / log(|z|) ~ 2
            log_ratio = (np.log(errors[i]) - np.log(errors[i - 1])) / \
                        (np.log(z_mags[i]) - np.log(z_mags[i - 1]))
            ratios.append(float(log_ratio))

    return {
        'tau_im': tau_im,
        'z_values': z_values,
        'errors': errors,
        'convergence_exponents': ratios,
        'final_error': errors[-1],
        'passed': errors[-1] < 1e-4,
    }


def verify_degeneration_componentwise(
    z: complex, tau_im: float = 50.0, n_terms: int = 80,
) -> Dict[str, Any]:
    r"""Component-by-component verification that w_a -> 1/z for small z at large Im(tau).

    At large Im(tau):
        w_1 -> pi*cot(pi*z) ~ 1/z for small z
        w_2 -> pi/sin(pi*z) ~ 1/z for small z
        w_3 -> pi/sin(pi*z) ~ 1/z for small z
    """
    tau = 1j * tau_im
    one_over_z = 1.0 / z
    errors = {}
    for a in range(3):
        w_a = belavin_weight_function(z, tau, a + 1, n_terms)
        err = abs(w_a - one_over_z) / abs(one_over_z)
        errors[f'w_{a + 1}'] = float(err)

    return {
        'z': z, 'tau_im': tau_im, '1/z': one_over_z,
        'channel_errors': errors,
        'all_passed': all(e < 0.02 for e in errors.values()),
    }


# ============================================================
# 10. Verification: Casimir eigenvalues
# ============================================================

def casimir_eigenvalues_on_tensor_product() -> Dict[str, Any]:
    r"""Compute eigenvalues of the Casimir tensor Omega on Sym^2(C^2) and wedge^2(C^2).

    Omega = (C_2^{tot} - C_2^{(1)} - C_2^{(2)})/2 with C_2(V_{1/2}) = 3/2.
    On Sym^2 = V_1: C_2^{tot} = 4, so Omega = (4 - 3/2 - 3/2)/2 = +1/2.
    On wedge^2 = V_0: C_2^{tot} = 0, so Omega = (0 - 3/2 - 3/2)/2 = -3/2.
    """
    Omega = sl2_casimir_tensor()

    # Sym^2(C^2) basis: |11>, (|12>+|21>)/sqrt(2), |22>
    sym_basis = np.array([
        [1, 0, 0, 0],
        [0, 1 / np.sqrt(2), 1 / np.sqrt(2), 0],
        [0, 0, 0, 1],
    ], dtype=complex).T  # 4x3

    # wedge^2(C^2) basis: (|12>-|21>)/sqrt(2)
    wedge_basis = np.array([
        [0, 1 / np.sqrt(2), -1 / np.sqrt(2), 0],
    ], dtype=complex).T  # 4x1

    Omega_in_sym = sym_basis.conj().T @ Omega @ sym_basis
    eigs_sym = np.sort(np.real(np.linalg.eigvals(Omega_in_sym)))

    Omega_in_wedge = wedge_basis.conj().T @ Omega @ wedge_basis
    eig_wedge = float(np.real(Omega_in_wedge[0, 0]))

    return {
        'eigenvalues_sym2': list(eigs_sym),
        'eigenvalue_wedge2': eig_wedge,
        'sym2_dim': 3,
        'wedge2_dim': 1,
    }


def verify_casimir_eigenvalues() -> Dict[str, Any]:
    r"""Verify Casimir eigenvalues: +1/2 on Sym^2(C^2), -3/2 on wedge^2(C^2).

    # VERIFIED:
    # [DC] Direct computation from 4x4 matrix
    # [LT] Representation theory: Omega = (C_2^{tot} - 2*C_2(1/2))/2
    #       C_2(j) = j(j+1) with our normalization -> C_2(1/2) = 3/2, C_2(1) = 4, C_2(0) = 0
    """
    result = casimir_eigenvalues_on_tensor_product()
    expected_sym = 0.5
    expected_wedge = -1.5

    eigs_sym = result['eigenvalues_sym2']
    eig_wedge = result['eigenvalue_wedge2']

    sym_check = all(abs(e - expected_sym) < 1e-12 for e in eigs_sym)
    wedge_check = abs(eig_wedge - expected_wedge) < 1e-12

    return {
        'eigenvalues_sym2': eigs_sym,
        'eigenvalue_wedge2': eig_wedge,
        'expected_sym2': expected_sym,
        'expected_wedge2': expected_wedge,
        'sym2_passed': sym_check,
        'wedge2_passed': wedge_check,
        'all_passed': sym_check and wedge_check,
    }


# ============================================================
# 11. Verification: theta function identities
# ============================================================

def verify_jacobi_triple_product(tau: complex, n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify theta_1'(0) = pi * theta_2(0) * theta_3(0) * theta_4(0)."""
    lhs = jacobi_theta1_prime0(tau, n_terms)
    rhs = PI * jacobi_theta2(0, tau, n_terms) * \
        jacobi_theta3(0, tau, n_terms) * jacobi_theta4(0, tau, n_terms)
    err = abs(lhs - rhs) / max(abs(lhs), 1e-10)
    return {
        'lhs': lhs, 'rhs': rhs,
        'relative_error': float(err),
        'passed': err < 1e-10,
    }


def verify_theta1_oddness(z: complex, tau: complex,
                           n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify theta_1(-z|tau) = -theta_1(z|tau)."""
    th1_z = jacobi_theta1(z, tau, n_terms)
    th1_mz = jacobi_theta1(-z, tau, n_terms)
    err = abs(th1_z + th1_mz) / max(abs(th1_z), 1e-10)
    return {'relative_error': float(err), 'passed': err < 1e-12}


def verify_theta_quasi_periodicity(z: complex, tau: complex,
                                    n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify theta_1(z+1|tau) = -theta_1(z|tau) and
    theta_1(z+tau|tau) = -q^{-1} e^{-2*pi*i*z} theta_1(z|tau).
    """
    th1_z = jacobi_theta1(z, tau, n_terms)
    # z -> z+1
    th1_z1 = jacobi_theta1(z + 1, tau, n_terms)
    err_1 = abs(th1_z1 + th1_z) / max(abs(th1_z), 1e-10)

    # z -> z+tau
    th1_ztau = jacobi_theta1(z + tau, tau, n_terms)
    q = np.exp(1j * PI * tau)
    factor = -1.0 / q * np.exp(-2j * PI * z)
    expected = factor * th1_z
    err_tau = abs(th1_ztau - expected) / max(abs(expected), 1e-10)

    return {
        'period_1_error': float(err_1),
        'period_tau_error': float(err_tau),
        'passed': err_1 < 1e-10 and err_tau < 1e-10,
    }


# ============================================================
# 12. Verification: weight function properties
# ============================================================

def verify_weight_residues(tau: complex, n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify each w_a has residue 1 at z=0: z * w_a(z) -> 1 as z -> 0."""
    results = {}
    z_small = 1e-7 + 1e-8j
    for a in range(1, 4):
        w = belavin_weight_function(z_small, tau, a, n_terms)
        residue = z_small * w
        err = abs(residue - 1.0)
        results[f'w_{a}'] = {'residue': complex(residue), 'error': float(err)}
    all_passed = all(v['error'] < 1e-5 for v in results.values())
    return {'channels': results, 'all_passed': all_passed}


def verify_weight_anisotropy(tau: complex, n_terms: int = 80) -> Dict[str, Any]:
    r"""Verify the three weight functions are DISTINCT at generic z and tau.

    This is the XYZ anisotropy: w_1 != w_2 != w_3 generically.
    At tau = i (square lattice), theta_3(0) = theta_4(0) by the
    Jacobi identity, so w_2 and w_3 have a special relationship.
    """
    z = 0.2 + 0.1j
    w1 = belavin_weight_function(z, tau, 1, n_terms)
    w2 = belavin_weight_function(z, tau, 2, n_terms)
    w3 = belavin_weight_function(z, tau, 3, n_terms)

    aniso = bool(abs(w1 - w2) > 1e-10 or abs(w2 - w3) > 1e-10)
    return {
        'w_1': w1, 'w_2': w2, 'w_3': w3,
        'w1_ne_w2': abs(w1 - w2) / max(abs(w1), 1e-10) > 1e-6,
        'w2_ne_w3': abs(w2 - w3) / max(abs(w2), 1e-10) > 1e-6,
        'anisotropic': aniso,
        'passed': aniso,
    }


# ============================================================
# 13. Verification: AP126/AP141
# ============================================================

def verify_level_prefix_k_zero(tau: complex,
                                n_terms: int = 80) -> Dict[str, Any]:
    r"""AP126/AP141: at k=0, the level-prefixed r-matrix MUST vanish."""
    z = 0.1 + 0.2j
    r_k0 = leveled_r_matrix_sl2(z, tau, k=0.0, n_terms=n_terms)
    norm = np.linalg.norm(r_k0)
    return {'norm_at_k0': float(norm), 'passed': norm < 1e-14}


# ============================================================
# 14. Verification: sl_2 algebra
# ============================================================

def verify_sl2_commutation_relations() -> Dict[str, Any]:
    r"""Verify [E, F] = H, [H, E] = 2E, [H, F] = -2F."""
    gens = _sl2_fund_matrices()
    E, F, H = gens['E'], gens['F'], gens['H']

    err_ef = np.linalg.norm(E @ F - F @ E - H)
    err_he = np.linalg.norm(H @ E - E @ H - 2 * E)
    err_hf = np.linalg.norm(H @ F - F @ H + 2 * F)

    return {
        '[E,F]=H': err_ef < 1e-14,
        '[H,E]=2E': err_he < 1e-14,
        '[H,F]=-2F': err_hf < 1e-14,
        'all_passed': err_ef < 1e-14 and err_he < 1e-14 and err_hf < 1e-14,
    }


def verify_omega_equals_pauli_sum() -> Dict[str, Any]:
    r"""Verify Omega = sum_{a=1}^3 sigma_a tensor sigma_a / 2
    = E tensor F + F tensor E + H tensor H / 2."""
    gens = _sl2_fund_matrices()
    E, F, H = gens['E'], gens['F'], gens['H']

    omega_cartan = np.kron(E, F) + np.kron(F, E) + 0.5 * np.kron(H, H)
    omega_pauli = sl2_casimir_tensor()

    err = np.linalg.norm(omega_cartan - omega_pauli)
    return {'error': float(err), 'passed': err < 1e-14}


def verify_casimir_element_eigenvalue() -> Dict[str, Any]:
    r"""Verify C_2 = EF + FE + H^2/2 has eigenvalue 3/2 on V_{1/2}."""
    gens = _sl2_fund_matrices()
    E, F, H = gens['E'], gens['F'], gens['H']
    C2 = E @ F + F @ E + 0.5 * H @ H
    eigs = np.sort(np.real(np.linalg.eigvals(C2)))
    expected = 1.5  # 3/2 on V_{1/2}
    check = all(abs(e - expected) < 1e-12 for e in eigs)
    return {'eigenvalues': list(eigs), 'expected': expected, 'passed': check}


# ============================================================
# 15. Verification: modular property at tau = i (square lattice)
# ============================================================

def verify_square_lattice_symmetry(n_terms: int = 80) -> Dict[str, Any]:
    r"""At tau = i, the lattice Z + iZ is a square lattice with Z_4 symmetry.

    Under z -> iz: the r-matrix transforms by conjugation by a Z_4 twist.
    We verify that the eigenvalue MAGNITUDES of r(z) and r(iz) match.
    """
    tau = 1j
    z = 0.15 + 0.08j
    iz = 1j * z

    r_z = belavin_r_matrix_sl2(z, tau, n_terms)
    r_iz = belavin_r_matrix_sl2(iz, tau, n_terms)

    eigs_z = np.sort(np.abs(np.linalg.eigvals(r_z)))
    eigs_iz = np.sort(np.abs(np.linalg.eigvals(r_iz)))

    err = np.linalg.norm(eigs_z - eigs_iz) / max(np.linalg.norm(eigs_z), 1e-10)
    return {
        'eigenvalue_magnitudes_z': list(eigs_z),
        'eigenvalue_magnitudes_iz': list(eigs_iz),
        'relative_error': float(err),
        'passed': err < 1e-6,
    }


# ============================================================
# 16. Comprehensive runner
# ============================================================

def run_all_verifications(
    tau: complex = 1j,
    k: float = 1.0,
    n_terms: int = 80,
) -> Dict[str, Any]:
    r"""Run all verification programmes and return summary."""
    results = {}

    # Programme 1: Degeneration
    results['degen_trig'] = verify_degeneration_to_trigonometric(
        0.2 + 0.1j, n_terms=n_terms)
    results['degen_rational'] = verify_degeneration_to_rational(n_terms=n_terms)
    results['degen_components'] = verify_degeneration_componentwise(
        0.01 + 0.005j, tau_im=50.0, n_terms=n_terms)

    # Programme 2: CYBE
    z1, z2, z3 = 0.1 + 0.2j, 0.3 + 0.1j, -0.15 + 0.25j
    results['cybe_tau_i'] = verify_cybe(z1, z2, z3, tau=1j, k=k, n_terms=n_terms)
    results['cybe_tau_general'] = verify_cybe(
        z1, z2, z3, tau=0.3 + 0.8j, k=k, n_terms=n_terms)
    results['cybe_tau_pure'] = verify_cybe(
        z1, z2, z3, tau=1.5j, k=k, n_terms=n_terms)

    # Programme 3: Casimir eigenvalues
    results['casimir_eigs'] = verify_casimir_eigenvalues()

    # Supporting
    results['skew_sym'] = verify_skew_symmetry(0.2 + 0.15j, tau, k, n_terms)
    results['pole_structure'] = verify_simple_pole_at_origin(tau, n_terms)
    results['ap126'] = verify_level_prefix_k_zero(tau, n_terms)
    results['sl2_comm'] = verify_sl2_commutation_relations()
    results['omega_pauli'] = verify_omega_equals_pauli_sum()
    results['casimir_elem'] = verify_casimir_element_eigenvalue()
    results['jtp'] = verify_jacobi_triple_product(tau, n_terms)
    results['theta1_odd'] = verify_theta1_oddness(0.3 + 0.2j, tau, n_terms)
    results['theta_qp'] = verify_theta_quasi_periodicity(0.3 + 0.2j, tau, n_terms)
    results['weight_res'] = verify_weight_residues(tau, n_terms)
    results['weight_aniso'] = verify_weight_anisotropy(0.3 + 0.8j, n_terms)
    results['square_lattice'] = verify_square_lattice_symmetry(n_terms)

    n_passed = 0
    n_total = len(results)
    for v in results.values():
        if isinstance(v, dict):
            if v.get('passed', v.get('all_passed', False)):
                n_passed += 1

    results['summary'] = {
        'n_passed': n_passed,
        'n_total': n_total,
        'all_passed': n_passed == n_total,
    }

    return results


__all__ = [
    'PI', 'TWO_PI_I',
    'SIGMA1', 'SIGMA2', 'SIGMA3', 'SIGMAS',
    'jacobi_theta1', 'jacobi_theta2', 'jacobi_theta3', 'jacobi_theta4',
    'jacobi_theta1_prime0',
    'sl2_casimir_tensor', 'permutation_operator',
    'sym2_projector', 'wedge2_projector',
    'belavin_weight_function', 'belavin_r_matrix_sl2', 'leveled_r_matrix_sl2',
    'trigonometric_r_matrix_sl2', 'rational_r_matrix_sl2',
    'casimir_eigenvalues_on_tensor_product', 'verify_casimir_eigenvalues',
    'verify_cybe', 'verify_skew_symmetry',
    'verify_simple_pole_at_origin',
    'verify_degeneration_to_trigonometric',
    'verify_degeneration_to_rational',
    'verify_degeneration_componentwise',
    'verify_jacobi_triple_product', 'verify_theta1_oddness',
    'verify_theta_quasi_periodicity',
    'verify_weight_residues', 'verify_weight_anisotropy',
    'verify_level_prefix_k_zero',
    'verify_sl2_commutation_relations',
    'verify_omega_equals_pauli_sum',
    'verify_casimir_element_eigenvalue',
    'verify_square_lattice_symmetry',
    'run_all_verifications',
]
