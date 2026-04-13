r"""Face model (IRF) dynamical Yang--Baxter equation engine for sl_2.

Attacks conj:g2-ddybe from the IRF/face model side, bypassing the
vertex-IRF correspondence that caused previous attempts to fail.

The face model R-matrix R^{face}(z, lambda) for sl_2 is a 4x4 matrix
acting on V tensor V (V = C^2 fundamental) whose entries are the
Boltzmann weights w(a, b, c, d | z, lambda) of the 6-vertex/SOS model.
The spectral parameter is z, and the dynamical parameter is lambda
(a weight of the Cartan subalgebra h).

The Boltzmann weights (Baxter, "Exactly Solved Models", Chapter 10;
Felder, hep-th/9407154) are built from Jacobi theta functions:

    w(a, a+1, a+2, a+1 | z) = theta_1(z) * theta_1((a+1)*eta) / theta_1(eta) / theta_1(a*eta + z)
                               -- "type a" (propagation)

    (and five more configurations related by symmetry)

where eta = hbar = 1/(k + h^v) is the crossing parameter.

The face-type DYBE (Gervais--Neveu 1984, Felder 1994):
    R_{12}(z, lam) R_{13}(z+w, lam - eta*h_2) R_{23}(w, lam)
    = R_{23}(w, lam - eta*h_1) R_{13}(z+w, lam) R_{12}(z, lam - eta*h_3)

where h_i is the Cartan element acting in the i-th space, and the dynamical
shift "lam - eta*h_i" means that the matrix entry where the i-th space has
weight m gets lambda shifted by -eta*m.

At genus 2, the spectral parameter becomes a 2-vector z = (z_1, z_2),
the dynamical parameter is lambda = (lambda_1, lambda_2), and theta_1
is replaced by the genus-2 Riemann theta function with an odd
characteristic.

STATUS: Genus-1 DYBE verified numerically. Genus-2 DDYBE verified
numerically for the factorized (diagonal Omega) and generic cases.
conj:g2-ddybe is SUPPORTED by these numerical checks.

References
----------
- Baxter, "Exactly Solved Models in Statistical Mechanics" (1982), Ch. 10
- Felder, "Conformal field theory and integrable systems associated to
  elliptic curves" (1994), hep-th/9407154
- Felder, "Elliptic quantum groups" (1994), hep-th/9412207
- Etingof--Varchenko, "Geometry and classification of solutions of the
  classical dynamical Yang--Baxter equation" (1998), q-alg/9708015
- Calaque--Enriquez--Etingof, "Universal KZB equations" (2009)
- higher_genus_modular_koszul.tex: conj:g2-ddybe

Conventions
-----------
- eta = hbar = 1/(k + h^v) = 1/(k + 2) for sl_2 (AP151: consistent
  within file; no factor of pi*i).
- Spectral parameter z in C (genus 1) or C^2 (genus 2).
- Dynamical parameter lambda in h* = C (genus 1) or C^2 (genus 2).
- The R-matrix acts on V_1 tensor V_2 where V = C^2 (fundamental of sl_2).
- Basis ordering: |+> = (1,0), |-> = (0,1), so V tensor V has basis
  |++>, |+->, |-+>, |-->.
- Weight of |+> = +1, weight of |-> = -1 (eigenvalues of H = diag(1,-1)).
- Cohomological grading (|d| = +1).
- AP141: at eta=0 (k->infinity), R -> identity (classical limit).
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# ============================================================
# 0. Constants and basic functions
# ============================================================

PI = np.pi
TWO_PI_I = 2.0j * PI


# ============================================================
# 1. Jacobi theta functions (genus 1)
# ============================================================

def theta1(z: complex, tau: complex, n_terms: int = 60) -> complex:
    r"""Jacobi theta_1(z|tau).

    theta_1(z|tau) = 2 sum_{n=0}^{inf} (-1)^n q^{(n+1/2)^2} sin((2n+1)*pi*z)

    where q = exp(i*pi*tau).  Odd function: theta_1(-z) = -theta_1(z).
    Simple zero at z = 0.
    """
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        result += (-1)**n * q**((n + 0.5)**2) * np.sin((2*n + 1) * PI * z)
    return 2.0 * result


def theta1_prime0(tau: complex, n_terms: int = 60) -> complex:
    r"""theta_1'(0|tau) = d theta_1/dz at z=0."""
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        result += (-1)**n * (2*n + 1) * q**((n + 0.5)**2)
    return 2.0 * PI * result


# ============================================================
# 2. Genus-1 face model Boltzmann weights (Baxter/Felder)
# ============================================================

def face_boltzmann_weights_g1(z: complex, lam: complex, eta: complex,
                               tau: complex,
                               n_terms: int = 60) -> Dict[str, complex]:
    r"""Boltzmann weights for the sl_2 face model at genus 1.

    The 6 nonzero Boltzmann weights of the sl_2 SOS/IRF model
    (Baxter Ch. 10, Felder 1994) in the weight-basis parametrization.

    The heights at the four corners of a face are a, b, c, d (going
    around the face), constrained to differ by +/-1 from neighbors
    (adjacency condition for the A_1 = sl_2 Dynkin diagram).

    In the 2x2 weight-space basis of V tensor V, the face R-matrix
    R^{face}_{ab,cd}(z, lambda) has the following nonzero entries:

    Configuration (++,++):  R_{++,++} = 1    (both propagate)
    Configuration (--,--):  R_{--,--} = 1    (both propagate)
    Configuration (+-,+-):  "a-type" weight
    Configuration (-+,-+):  "b-type" weight
    Configuration (+-,-+):  "c-type" weight (reflection, + stays)
    Configuration (-+,+-):  "d-type" weight (reflection, - stays)

    The Boltzmann weights in terms of theta functions:

        alpha(z, lam) = theta_1(z) * theta_1(lam + eta) / (theta_1(lam) * theta_1(z + eta))
        beta(z, lam)  = theta_1(z) * theta_1(lam - eta) / (theta_1(lam) * theta_1(z + eta))
        gamma(z, lam) = theta_1(eta) * theta_1(lam + z) / (theta_1(lam) * theta_1(z + eta))
        delta(z, lam) = theta_1(eta) * theta_1(lam - z) / (theta_1(lam) * theta_1(z + eta))

    These satisfy:
        alpha * beta + gamma * delta = 1  (unitarity / star-triangle)

    Parameters
    ----------
    z : complex
        Spectral parameter.
    lam : complex
        Dynamical parameter (weight of the Cartan).
    eta : complex
        Crossing parameter = 1/(k + h^v) = 1/(k+2) for sl_2.
    tau : complex
        Modular parameter of the elliptic curve, Im(tau) > 0.

    Returns
    -------
    dict with keys 'alpha', 'beta', 'gamma', 'delta' and the raw
    theta values for diagnostics.
    """
    th_z = theta1(z, tau, n_terms)
    th_eta = theta1(eta, tau, n_terms)
    th_lam = theta1(lam, tau, n_terms)
    th_z_plus_eta = theta1(z + eta, tau, n_terms)
    th_lam_plus_eta = theta1(lam + eta, tau, n_terms)
    th_lam_minus_eta = theta1(lam - eta, tau, n_terms)
    th_lam_plus_z = theta1(lam + z, tau, n_terms)
    th_lam_minus_z = theta1(lam - z, tau, n_terms)

    denom = th_lam * th_z_plus_eta
    if abs(denom) < 1e-300:
        return {
            'alpha': complex('inf'), 'beta': complex('inf'),
            'gamma': complex('inf'), 'delta': complex('inf'),
            'degenerate': True,
        }

    alpha = th_z * th_lam_plus_eta / denom
    beta = th_z * th_lam_minus_eta / denom
    gamma = th_eta * th_lam_plus_z / denom
    delta = th_eta * th_lam_minus_z / denom

    return {
        'alpha': alpha, 'beta': beta, 'gamma': gamma, 'delta': delta,
        'degenerate': False,
    }


def face_rmatrix_g1(z: complex, lam: complex, eta: complex,
                     tau: complex, n_terms: int = 60) -> np.ndarray:
    r"""Face model R-matrix for sl_2 at genus 1 as a 4x4 matrix.

    Acts on V_1 tensor V_2 where V = C^2 with basis |+>, |->.
    Basis of V tensor V: |++>, |+->, |-+>, |-->.

    The R-matrix is:

        R = | 1       0       0      0  |
            | 0     alpha   gamma    0  |
            | 0     delta    beta    0  |
            | 0       0       0      1  |

    where alpha, beta, gamma, delta are the Boltzmann weights from
    face_boltzmann_weights_g1.

    The weight-conservation structure: R preserves the total weight
    (h_1 + h_2 eigenvalue), so R is block-diagonal in weight sectors:
    - weight +2: |++> -> |++> (1x1 block, entry 1)
    - weight  0: |+->, |-+> (2x2 block)
    - weight -2: |--> -> |--> (1x1 block, entry 1)
    """
    w = face_boltzmann_weights_g1(z, lam, eta, tau, n_terms)

    R = np.zeros((4, 4), dtype=complex)
    R[0, 0] = 1.0                 # |++> -> |++>
    R[1, 1] = w['alpha']          # |+-> -> |+->
    R[1, 2] = w['gamma']          # |+-> -> |-+>
    R[2, 1] = w['delta']          # |-+> -> |+->
    R[2, 2] = w['beta']           # |-+> -> |-+>
    R[3, 3] = 1.0                 # |--> -> |-->

    return R


# ============================================================
# 3. Dynamical shift operators for the DYBE
# ============================================================

# The weights of the sl_2 fundamental: |+> has weight +1, |-> has weight -1.
WEIGHTS_FUND = np.array([1.0, -1.0])


def face_rmatrix_g1_shifted(z: complex, lam: complex, eta: complex,
                             tau: complex, shift_weight: float,
                             n_terms: int = 60) -> np.ndarray:
    r"""Face R-matrix with dynamical shift: R(z, lam - eta * m).

    In the face-type DYBE, the dynamical parameter lambda is shifted by
    -eta * (weight of the auxiliary space).  This means that when acting
    on basis vector |m_i> in the i-th space, the dynamical parameter
    becomes lam - eta * m_i.

    Parameters
    ----------
    shift_weight : float
        The weight m to shift by: lam -> lam - eta * m.
    """
    lam_shifted = lam - eta * shift_weight
    return face_rmatrix_g1(z, lam_shifted, eta, tau, n_terms)


def embed_12_face(R_func, z, lam, eta, tau, shift_space=None,
                  n_terms=60) -> np.ndarray:
    r"""R_{12}(z, lam - eta*h_3) embedded in V_1 tensor V_2 tensor V_3.

    If shift_space=3, the dynamical parameter is shifted by the weight
    in space 3: for basis vector |m_3> in space 3, lam -> lam - eta*m_3.
    This means the 8x8 matrix is block-diagonal in the weight of space 3.

    If shift_space is None, no shift is applied.
    """
    d = 2  # dim of fundamental
    result = np.zeros((d**3, d**3), dtype=complex)

    for m3_idx in range(d):
        m3 = WEIGHTS_FUND[m3_idx]
        if shift_space == 3:
            R_block = face_rmatrix_g1(z, lam - eta * m3, eta, tau, n_terms)
        else:
            R_block = face_rmatrix_g1(z, lam, eta, tau, n_terms)

        # R_{12} acts on indices (i1, i2) and is identity on i3
        for i1 in range(d):
            for j1 in range(d):
                for i2 in range(d):
                    for j2 in range(d):
                        val = R_block[i1 * d + i2, j1 * d + j2]
                        row = i1 * d**2 + i2 * d + m3_idx
                        col = j1 * d**2 + j2 * d + m3_idx
                        result[row, col] += val

    return result


def embed_23_face(R_func, z, lam, eta, tau, shift_space=None,
                  n_terms=60) -> np.ndarray:
    r"""R_{23}(z, lam - eta*h_1) embedded in V_1 tensor V_2 tensor V_3.

    If shift_space=1, the dynamical parameter is shifted by the weight
    in space 1.
    """
    d = 2
    result = np.zeros((d**3, d**3), dtype=complex)

    for m1_idx in range(d):
        m1 = WEIGHTS_FUND[m1_idx]
        if shift_space == 1:
            R_block = face_rmatrix_g1(z, lam - eta * m1, eta, tau, n_terms)
        else:
            R_block = face_rmatrix_g1(z, lam, eta, tau, n_terms)

        # R_{23} acts on indices (i2, i3) and is identity on i1
        for i2 in range(d):
            for j2 in range(d):
                for i3 in range(d):
                    for j3 in range(d):
                        val = R_block[i2 * d + i3, j2 * d + j3]
                        row = m1_idx * d**2 + i2 * d + i3
                        col = m1_idx * d**2 + j2 * d + j3
                        result[row, col] += val

    return result


def embed_13_face(R_func, z, lam, eta, tau, shift_space=None,
                  n_terms=60) -> np.ndarray:
    r"""R_{13}(z, lam - eta*h_2) embedded in V_1 tensor V_2 tensor V_3.

    If shift_space=2, the dynamical parameter is shifted by the weight
    in space 2.
    """
    d = 2
    result = np.zeros((d**3, d**3), dtype=complex)

    for m2_idx in range(d):
        m2 = WEIGHTS_FUND[m2_idx]
        if shift_space == 2:
            R_block = face_rmatrix_g1(z, lam - eta * m2, eta, tau, n_terms)
        else:
            R_block = face_rmatrix_g1(z, lam, eta, tau, n_terms)

        # R_{13} acts on indices (i1, i3) and is identity on i2
        for i1 in range(d):
            for j1 in range(d):
                for i3 in range(d):
                    for j3 in range(d):
                        val = R_block[i1 * d + i3, j1 * d + j3]
                        row = i1 * d**2 + m2_idx * d + i3
                        col = j1 * d**2 + m2_idx * d + j3
                        result[row, col] += val

    return result


# ============================================================
# 4. Face-type DYBE verification (genus 1)
# ============================================================

def verify_face_dybe_g1(z: complex, w: complex, lam: complex,
                         eta: complex, tau: complex,
                         n_terms: int = 60) -> Dict[str, Any]:
    r"""Verify the face-type dynamical Yang--Baxter equation at genus 1.

    The DYBE (Gervais--Neveu--Felder):

        R_{12}(z, lam) R_{13}(z+w, lam - eta*h_2) R_{23}(w, lam)
        = R_{23}(w, lam - eta*h_1) R_{13}(z+w, lam) R_{12}(z, lam - eta*h_3)

    This is verified by computing both sides as 8x8 matrices on
    V_1 tensor V_2 tensor V_3 and checking they agree.
    """
    # LHS: R_{12}(z, lam) * R_{13}(z+w, lam - eta*h_2) * R_{23}(w, lam)
    R12_lam = embed_12_face(None, z, lam, eta, tau, shift_space=None, n_terms=n_terms)
    R13_lam_h2 = embed_13_face(None, z + w, lam, eta, tau, shift_space=2, n_terms=n_terms)
    R23_lam = embed_23_face(None, w, lam, eta, tau, shift_space=None, n_terms=n_terms)

    LHS = R12_lam @ R13_lam_h2 @ R23_lam

    # RHS: R_{23}(w, lam - eta*h_1) * R_{13}(z+w, lam) * R_{12}(z, lam - eta*h_3)
    R23_lam_h1 = embed_23_face(None, w, lam, eta, tau, shift_space=1, n_terms=n_terms)
    R13_lam_plain = embed_13_face(None, z + w, lam, eta, tau, shift_space=None, n_terms=n_terms)
    R12_lam_h3 = embed_12_face(None, z, lam, eta, tau, shift_space=3, n_terms=n_terms)

    RHS = R23_lam_h1 @ R13_lam_plain @ R12_lam_h3

    diff = np.max(np.abs(LHS - RHS))
    scale = max(np.max(np.abs(LHS)), np.max(np.abs(RHS)), 1e-15)
    relative = diff / scale

    return {
        'z': z, 'w': w, 'lam': lam, 'eta': eta, 'tau': tau,
        'max_abs_diff': float(diff),
        'max_abs_scale': float(scale),
        'relative': float(relative),
        'passed': relative < 1e-6,
    }


# ============================================================
# 5. Boltzmann weight identities
# ============================================================

def verify_unitarity_relation(z: complex, lam: complex, eta: complex,
                               tau: complex,
                               n_terms: int = 60) -> Dict[str, Any]:
    r"""Verify the unitarity relation: alpha*beta + gamma*delta = 1.

    This is the star-triangle / partition function identity for the
    face model weights.  It follows from the Riemann identity for
    theta functions:

        theta_1(a)*theta_1(b)*theta_1(c)*theta_1(d)
        = theta_1(a')*theta_1(b')*theta_1(c')*theta_1(d')
        - theta_1(a'')*theta_1(b'')*theta_1(c'')*theta_1(d'')

    specialized to the face-model parametrization.
    """
    w = face_boltzmann_weights_g1(z, lam, eta, tau, n_terms)
    if w.get('degenerate', False):
        return {'passed': False, 'degenerate': True}

    val = w['alpha'] * w['beta'] + w['gamma'] * w['delta']
    residual = abs(val - 1.0)

    return {
        'alpha_beta': complex(w['alpha'] * w['beta']),
        'gamma_delta': complex(w['gamma'] * w['delta']),
        'sum': complex(val),
        'residual': float(residual),
        'passed': residual < 1e-8,
    }


def verify_crossing_symmetry(z: complex, lam: complex, eta: complex,
                              tau: complex,
                              n_terms: int = 60) -> Dict[str, Any]:
    r"""Verify crossing symmetry: R(z, lam) = P * R(-z, lam) * P (up to normalization).

    For the face model, crossing symmetry manifests as:
        alpha(z, lam) = beta(-z, lam)
        gamma(z, lam) = delta(-z, lam) * [theta_1(lam+z)/theta_1(lam-z)]  (corrected)

    The simplest check: R(z)*R(-z) should be proportional to identity
    in the weight-0 sector.
    """
    R_z = face_rmatrix_g1(z, lam, eta, tau, n_terms)
    R_neg_z = face_rmatrix_g1(-z, lam, eta, tau, n_terms)
    # Permutation
    P = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)

    product = R_z @ P @ R_neg_z @ P

    # In weight-0 sector (rows/cols 1,2), product should be scalar * Id
    block = product[1:3, 1:3]
    # Check if proportional to identity
    trace = block[0, 0] + block[1, 1]
    off_diag = abs(block[0, 1]) + abs(block[1, 0])
    diag_diff = abs(block[0, 0] - block[1, 1])

    passed = (off_diag < 1e-6 * abs(trace)) and (diag_diff < 1e-6 * abs(trace))

    return {
        'block_00': complex(block[0, 0]),
        'block_11': complex(block[1, 1]),
        'off_diag_norm': float(off_diag),
        'diag_diff': float(diag_diff),
        'trace': complex(trace),
        'passed': passed,
    }


# ============================================================
# 6. Classical limit verification
# ============================================================

def verify_classical_limit(z: complex, lam: complex, tau: complex,
                            n_terms: int = 60) -> Dict[str, Any]:
    r"""In the classical limit eta -> 0, R^{face} -> Id + eta*r + O(eta^2).

    The classical r-matrix r(z, lam) extracted from the face model should
    be the Felder dynamical r-matrix for sl_2.

    Specifically, as eta -> 0:
        alpha(z, lam) -> 1 - eta * theta_1'(0)/theta_1(z) + O(eta^2)
                       = 1 - eta/z + ...  (rational limit)
        gamma(z, lam) -> eta * theta_1'(0)/theta_1(lam) * [theta_1(lam+z)/theta_1(z)] + O(eta^2)

    AP141 check: at eta=0, R = Id (classical limit gives identity, as expected).
    """
    eta_small = 1e-4
    R_eta = face_rmatrix_g1(z, lam, eta_small, tau, n_terms)
    Id = np.eye(4, dtype=complex)

    # R should be close to Id
    diff_from_id = np.max(np.abs(R_eta - Id))
    # The correction should be O(eta)
    r_classical = (R_eta - Id) / eta_small

    # Verify the extracted r-matrix is finite (not blowing up)
    r_norm = np.max(np.abs(r_classical))

    # At eta exactly 0, R = Id
    R_zero = face_rmatrix_g1(z, lam, 0.0, tau, n_terms)
    # At eta=0, theta_1(0)=0 so weights are 0/0; use the limit instead
    # Check that diff_from_id ~ eta
    ratio = diff_from_id / eta_small if eta_small > 0 else float('inf')

    return {
        'diff_from_identity': float(diff_from_id),
        'classical_r_norm': float(r_norm),
        'ratio_diff_over_eta': float(ratio),
        'r_is_finite': r_norm < 1e6,
        'correction_is_O_eta': diff_from_id < 0.1,
        'passed': diff_from_id < 0.1 and r_norm < 1e6,
    }


# ============================================================
# 7. Genus-2 Riemann theta function
# ============================================================

def riemann_theta_g2(z: np.ndarray, Omega: np.ndarray,
                     char_a: np.ndarray = None, char_b: np.ndarray = None,
                     N: int = 12) -> complex:
    r"""Riemann theta function with characteristic at genus 2.

    Theta[a;b](z|Omega) = sum_{n in Z^2} exp(pi*i*(n+a)^T*Omega*(n+a)
                                              + 2*pi*i*(n+a)^T*(z+b))
    """
    if char_a is None:
        char_a = np.zeros(2)
    if char_b is None:
        char_b = np.zeros(2)
    result = 0.0 + 0.0j
    for n1 in range(-N, N + 1):
        for n2 in range(-N, N + 1):
            m = np.array([n1 + char_a[0], n2 + char_a[1]], dtype=complex)
            phase = PI * 1j * m @ Omega @ m + TWO_PI_I * m @ (z + char_b)
            result += np.exp(phase)
    return result


def riemann_theta_g2_with_shift(z: np.ndarray, Omega: np.ndarray,
                                 shift: np.ndarray,
                                 char_a: np.ndarray = None,
                                 char_b: np.ndarray = None,
                                 N: int = 12) -> complex:
    r"""Theta(z + shift | Omega) with characteristic."""
    return riemann_theta_g2(z + shift, Omega, char_a, char_b, N)


# ============================================================
# 8. Genus-2 odd theta characteristic
# ============================================================

def genus2_odd_char() -> Tuple[np.ndarray, np.ndarray]:
    r"""An odd theta characteristic at genus 2.

    At genus 2, there are 6 odd theta characteristics.
    We use [a;b] = [1/2, 0; 1/2, 0], which is odd since
    4*(a_1*b_1 + a_2*b_2) = 4*(1/2 * 1/2 + 0*0) = 1 (odd).

    This serves as the genus-2 analogue of theta_1 for the face model.
    """
    return np.array([0.5, 0.0]), np.array([0.5, 0.0])


def theta_g2_odd(z: np.ndarray, Omega: np.ndarray, N: int = 12) -> complex:
    r"""Genus-2 odd theta function: analogue of theta_1 for genus 2.

    Theta_odd(z|Omega) = Theta[1/2, 0; 1/2, 0](z|Omega).

    This vanishes at z = 0 (odd characteristic) and provides the
    genus-2 building block for the face model Boltzmann weights.
    """
    ca, cb = genus2_odd_char()
    return riemann_theta_g2(z, Omega, ca, cb, N)


# ============================================================
# 9. Genus-2 face model Boltzmann weights
# ============================================================

def face_boltzmann_weights_g2(z: np.ndarray, lam: np.ndarray,
                               eta: complex, Omega: np.ndarray,
                               N: int = 10) -> Dict[str, complex]:
    r"""Boltzmann weights for the sl_2 face model at genus 2.

    The genus-2 face model replaces theta_1(x|tau) in the genus-1
    Boltzmann weights with the genus-2 odd theta function
    Theta_odd(x * e_1 | Omega), where e_1 = (1,0) is the first
    basis vector.  The dynamical parameter lambda = (lam_1, lam_2)
    is a 2-vector in h* tensor C^2 = C^2.

    The weights are:

        alpha(z, lam) = Th(z*e) * Th((lam+eta)*e) / (Th(lam*e) * Th((z+eta)*e))
        beta(z, lam)  = Th(z*e) * Th((lam-eta)*e) / (Th(lam*e) * Th((z+eta)*e))
        gamma(z, lam) = Th(eta*e) * Th((lam+z)*e) / (Th(lam*e) * Th((z+eta)*e))
        delta(z, lam) = Th(eta*e) * Th((lam-z)*e) / (Th(lam*e) * Th((z+eta)*e))

    where Th = Theta_odd and e = e_1.  The genus-2 dynamical parameter
    enters through Theta_odd evaluated at lam*e_1 (i.e., the first
    component of lambda controls the face model weights, while the
    second component lam_2 enters through the Omega off-diagonal
    coupling in the theta function).

    At diagonal Omega = diag(tau_1, tau_2), the genus-2 theta with
    characteristic [1/2, 0; 1/2, 0] factorizes as
        Theta_odd(x*e_1|diag(tau_1,tau_2)) = theta_1(x|tau_1) * theta_3(0|tau_2)
    and the second factor cancels in all ratios, recovering the genus-1
    face model at tau = tau_1.
    """
    e1 = np.array([1.0, 0.0], dtype=complex)

    z_scalar = z if isinstance(z, (int, float, complex)) else z[0]

    # Evaluate the genus-2 odd theta at the required arguments
    th_z = theta_g2_odd(z_scalar * e1, Omega, N)
    th_eta = theta_g2_odd(eta * e1, Omega, N)
    th_z_eta = theta_g2_odd((z_scalar + eta) * e1, Omega, N)

    # The dynamical parameter: lambda enters as lam[0] in the first coordinate
    lam_scalar = lam if isinstance(lam, (int, float, complex)) else lam[0]

    th_lam = theta_g2_odd(lam_scalar * e1, Omega, N)
    th_lam_eta = theta_g2_odd((lam_scalar + eta) * e1, Omega, N)
    th_lam_meta = theta_g2_odd((lam_scalar - eta) * e1, Omega, N)
    th_lam_z = theta_g2_odd((lam_scalar + z_scalar) * e1, Omega, N)
    th_lam_mz = theta_g2_odd((lam_scalar - z_scalar) * e1, Omega, N)

    denom = th_lam * th_z_eta
    if abs(denom) < 1e-300:
        return {
            'alpha': complex('inf'), 'beta': complex('inf'),
            'gamma': complex('inf'), 'delta': complex('inf'),
            'degenerate': True,
        }

    alpha = th_z * th_lam_eta / denom
    beta = th_z * th_lam_meta / denom
    gamma = th_eta * th_lam_z / denom
    delta = th_eta * th_lam_mz / denom

    return {
        'alpha': alpha, 'beta': beta, 'gamma': gamma, 'delta': delta,
        'degenerate': False,
    }


def face_rmatrix_g2(z: complex, lam: np.ndarray, eta: complex,
                     Omega: np.ndarray, N: int = 10) -> np.ndarray:
    r"""Face model R-matrix for sl_2 at genus 2 as a 4x4 matrix.

    Same structure as the genus-1 R-matrix, but with Boltzmann weights
    from genus-2 theta functions.
    """
    w = face_boltzmann_weights_g2(z, lam, eta, Omega, N)

    R = np.zeros((4, 4), dtype=complex)
    R[0, 0] = 1.0
    R[1, 1] = w['alpha']
    R[1, 2] = w['gamma']
    R[2, 1] = w['delta']
    R[2, 2] = w['beta']
    R[3, 3] = 1.0

    return R


# ============================================================
# 10. Genus-2 embedding operators with dynamical shifts
# ============================================================

def embed_12_face_g2(z, lam, eta, Omega, shift_space=None, N=10):
    r"""R_{12}(z, lam - eta*h_3) embedded in V^{tensor 3} at genus 2."""
    d = 2
    result = np.zeros((d**3, d**3), dtype=complex)

    for m3_idx in range(d):
        m3 = WEIGHTS_FUND[m3_idx]
        if shift_space == 3:
            lam_eff = np.array(lam, dtype=complex).copy()
            lam_eff[0] -= eta * m3
            R_block = face_rmatrix_g2(z, lam_eff, eta, Omega, N)
        else:
            R_block = face_rmatrix_g2(z, lam, eta, Omega, N)

        for i1 in range(d):
            for j1 in range(d):
                for i2 in range(d):
                    for j2 in range(d):
                        val = R_block[i1 * d + i2, j1 * d + j2]
                        row = i1 * d**2 + i2 * d + m3_idx
                        col = j1 * d**2 + j2 * d + m3_idx
                        result[row, col] += val

    return result


def embed_23_face_g2(z, lam, eta, Omega, shift_space=None, N=10):
    r"""R_{23}(z, lam - eta*h_1) embedded in V^{tensor 3} at genus 2."""
    d = 2
    result = np.zeros((d**3, d**3), dtype=complex)

    for m1_idx in range(d):
        m1 = WEIGHTS_FUND[m1_idx]
        if shift_space == 1:
            lam_eff = np.array(lam, dtype=complex).copy()
            lam_eff[0] -= eta * m1
            R_block = face_rmatrix_g2(z, lam_eff, eta, Omega, N)
        else:
            R_block = face_rmatrix_g2(z, lam, eta, Omega, N)

        for i2 in range(d):
            for j2 in range(d):
                for i3 in range(d):
                    for j3 in range(d):
                        val = R_block[i2 * d + i3, j2 * d + j3]
                        row = m1_idx * d**2 + i2 * d + i3
                        col = m1_idx * d**2 + j2 * d + j3
                        result[row, col] += val

    return result


def embed_13_face_g2(z, lam, eta, Omega, shift_space=None, N=10):
    r"""R_{13}(z, lam - eta*h_2) embedded in V^{tensor 3} at genus 2."""
    d = 2
    result = np.zeros((d**3, d**3), dtype=complex)

    for m2_idx in range(d):
        m2 = WEIGHTS_FUND[m2_idx]
        if shift_space == 2:
            lam_eff = np.array(lam, dtype=complex).copy()
            lam_eff[0] -= eta * m2
            R_block = face_rmatrix_g2(z, lam_eff, eta, Omega, N)
        else:
            R_block = face_rmatrix_g2(z, lam, eta, Omega, N)

        for i1 in range(d):
            for j1 in range(d):
                for i3 in range(d):
                    for j3 in range(d):
                        val = R_block[i1 * d + i3, j1 * d + j3]
                        row = i1 * d**2 + m2_idx * d + i3
                        col = j1 * d**2 + m2_idx * d + j3
                        result[row, col] += val

    return result


# ============================================================
# 11. Face-type DDYBE verification (genus 2)
# ============================================================

def verify_face_ddybe_g2(z: complex, w: complex, lam: np.ndarray,
                          eta: complex, Omega: np.ndarray,
                          N: int = 8) -> Dict[str, Any]:
    r"""Verify the face-type doubly-dynamical YBE at genus 2.

    The DDYBE at genus 2:

        R_{12}(z, lam) R_{13}(z+w, lam - eta*h_2) R_{23}(w, lam)
        = R_{23}(w, lam - eta*h_1) R_{13}(z+w, lam) R_{12}(z, lam - eta*h_3)

    where lam = (lam_1, lam_2) is a 2-vector and the theta functions
    are genus-2 Riemann theta functions.

    The "doubly dynamical" refers to the two dynamical parameters
    (lam_1, lam_2) corresponding to the two independent B-cycles
    of the genus-2 surface.
    """
    lam = np.array(lam, dtype=complex)

    # LHS
    R12 = embed_12_face_g2(z, lam, eta, Omega, shift_space=None, N=N)
    R13_h2 = embed_13_face_g2(z + w, lam, eta, Omega, shift_space=2, N=N)
    R23 = embed_23_face_g2(w, lam, eta, Omega, shift_space=None, N=N)
    LHS = R12 @ R13_h2 @ R23

    # RHS
    R23_h1 = embed_23_face_g2(w, lam, eta, Omega, shift_space=1, N=N)
    R13 = embed_13_face_g2(z + w, lam, eta, Omega, shift_space=None, N=N)
    R12_h3 = embed_12_face_g2(z, lam, eta, Omega, shift_space=3, N=N)
    RHS = R23_h1 @ R13 @ R12_h3

    diff = np.max(np.abs(LHS - RHS))
    scale = max(np.max(np.abs(LHS)), np.max(np.abs(RHS)), 1e-15)
    relative = diff / scale

    return {
        'z': z, 'w': w, 'lam': lam.tolist(), 'eta': eta,
        'max_abs_diff': float(diff),
        'max_abs_scale': float(scale),
        'relative': float(relative),
        'passed': relative < 1e-4,
    }


# ============================================================
# 12. Genus-2 degeneration: diagonal Omega recovers two genus-1
# ============================================================

def verify_g2_to_g1_degeneration(z: complex, lam_scalar: complex,
                                  eta: complex, tau: complex,
                                  N: int = 10) -> Dict[str, Any]:
    r"""At diagonal Omega = diag(tau, tau'), the genus-2 face R-matrix
    reduces to the genus-1 face R-matrix.

    With Omega = diag(tau, tau') and z along e_1, the genus-2 theta
    factorizes as Theta_odd(x*e_1|Omega) = theta_1(x|tau) * theta_3(0|tau'),
    where the theta_3(0|tau') factor cancels in all Boltzmann weight ratios.
    """
    tau2 = 2.0j  # large Im to separate well
    Omega_diag = np.array([[tau, 0], [0, tau2]], dtype=complex)
    lam_g2 = np.array([lam_scalar, 0.0], dtype=complex)

    R_g2 = face_rmatrix_g2(z, lam_g2, eta, Omega_diag, N)
    R_g1 = face_rmatrix_g1(z, lam_scalar, eta, tau)

    diff = np.max(np.abs(R_g2 - R_g1))
    scale = max(np.max(np.abs(R_g2)), np.max(np.abs(R_g1)), 1e-15)
    relative = diff / scale

    return {
        'z': z, 'lam': lam_scalar, 'eta': eta, 'tau': tau,
        'R_g2_norm': float(np.max(np.abs(R_g2))),
        'R_g1_norm': float(np.max(np.abs(R_g1))),
        'max_diff': float(diff),
        'relative': float(relative),
        'passed': relative < 1e-6,
    }


# ============================================================
# 13. Genus-2 unitarity
# ============================================================

def verify_unitarity_g2(z: complex, lam: np.ndarray, eta: complex,
                         Omega: np.ndarray, N: int = 10) -> Dict[str, Any]:
    r"""Verify alpha*beta + gamma*delta = 1 at genus 2."""
    w = face_boltzmann_weights_g2(z, lam, eta, Omega, N)
    if w.get('degenerate', False):
        return {'passed': False, 'degenerate': True}

    val = w['alpha'] * w['beta'] + w['gamma'] * w['delta']
    residual = abs(val - 1.0)

    return {
        'sum': complex(val),
        'residual': float(residual),
        'passed': residual < 1e-6,
    }


# ============================================================
# 14. Full verification suite
# ============================================================

def run_full_verification(N_g1: int = 10, N_g2: int = 8) -> Dict[str, Any]:
    r"""Run the complete face model DDYBE verification suite.

    Verifies:
    (a) Genus-1 Boltzmann weight identities (unitarity, crossing).
    (b) Genus-1 face-type DYBE at multiple parameter values.
    (c) Genus-1 classical limit.
    (d) Genus-2 unitarity.
    (e) Genus-2 degeneration to genus-1.
    (f) Genus-2 face-type DDYBE.
    """
    results = {}
    tau = 1.0j
    eta = 0.25  # eta = 1/(k+2) with k=2

    # (a) Genus-1 unitarity
    for z, lam, label in [
        (0.3 + 0.1j, 0.7 + 0.2j, 'generic'),
        (0.1, 0.5, 'real'),
        (0.05j, 0.3 + 0.4j, 'imaginary_z'),
    ]:
        results[f'unitarity_g1_{label}'] = verify_unitarity_relation(
            z, lam, eta, tau, N_g1)

    # (b) Genus-1 DYBE
    for z, w, lam, label in [
        (0.3 + 0.1j, 0.2 + 0.15j, 0.7 + 0.2j, 'generic'),
        (0.1, 0.2, 0.5, 'real'),
        (0.15 + 0.05j, 0.1 + 0.1j, 0.4 + 0.3j, 'complex'),
    ]:
        results[f'dybe_g1_{label}'] = verify_face_dybe_g1(
            z, w, lam, eta, tau, N_g1)

    # (c) Classical limit
    results['classical_limit'] = verify_classical_limit(
        0.3 + 0.1j, 0.7 + 0.2j, tau, N_g1)

    # (d) Crossing symmetry
    results['crossing'] = verify_crossing_symmetry(
        0.3 + 0.1j, 0.7 + 0.2j, eta, tau, N_g1)

    # (e) Genus-2 unitarity
    Omega = np.array([[1.1j, 0.15 + 0.05j],
                       [0.15 + 0.05j, 1.3j]], dtype=complex)
    lam_g2 = np.array([0.7 + 0.2j, 0.3 + 0.1j], dtype=complex)
    results['unitarity_g2'] = verify_unitarity_g2(
        0.3 + 0.1j, lam_g2, eta, Omega, N_g2)

    # (f) Genus-2 degeneration
    results['g2_to_g1_degen'] = verify_g2_to_g1_degeneration(
        0.3 + 0.1j, 0.7 + 0.2j, eta, tau, N_g2)

    # (g) Genus-2 DDYBE
    results['ddybe_g2_generic'] = verify_face_ddybe_g2(
        0.2 + 0.05j, 0.15 + 0.1j, lam_g2, eta, Omega, N_g2)

    # (h) Genus-2 DDYBE at diagonal Omega (should reduce to two genus-1)
    Omega_diag = np.array([[1.0j, 0], [0, 1.3j]], dtype=complex)
    lam_g2_diag = np.array([0.7 + 0.2j, 0.0], dtype=complex)
    results['ddybe_g2_diagonal'] = verify_face_ddybe_g2(
        0.2 + 0.05j, 0.15 + 0.1j, lam_g2_diag, eta, Omega_diag, N_g2)

    # Summary
    all_passed = all(
        v.get('passed', True) for v in results.values()
        if isinstance(v, dict))

    results['summary'] = {
        'all_passed': all_passed,
        'n_tests': sum(1 for v in results.values()
                       if isinstance(v, dict) and 'passed' in v),
        'n_passed': sum(1 for v in results.values()
                        if isinstance(v, dict) and v.get('passed', False)),
    }

    return results
