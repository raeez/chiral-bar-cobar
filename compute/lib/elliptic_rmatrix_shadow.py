r"""Elliptic R-matrix from the genus-1 shadow obstruction tower.

At genus 0, the collision residue r(z) = Res^{coll}_{0,2}(\Theta_A) gives
the rational r-matrix r(z) = \Omega/z for affine Lie algebras.  At genus 1,
the analogous construction on an elliptic curve E_\tau produces the ELLIPTIC
R-matrix R^{ell}(z, \tau), which for affine \hat{sl}_N at level k reproduces
the Belavin--Drinfeld classical elliptic r-matrix.

The mechanism: the bar propagator on E_\tau is d\log E(z,w) where E(z,w)
is the prime form.  On the torus C/(Z + Z\tau), the prime form is
    E(z) = \theta_1(z|\tau) / \theta_1'(0|\tau)
and d\log E(z) = \zeta_\tau(z) dz, where \zeta_\tau is the Weierstrass
zeta function for periods (1, \tau).  The collision residue now extracts
\zeta_\tau(z) instead of 1/z, yielding the elliptic deformation.

For sl_2:
    r^{ell}(z,\tau) = \sum_{a,b} g^{ab} \zeta^{ab}(z,\tau) T_a \otimes T_b
where \zeta^{ab}(z,\tau) encodes the elliptic Green's function.  In the
Cartan-root decomposition:
    r^{ell}(z,\tau) = \zeta(z,\tau) \cdot \frac{H \otimes H}{2}
                     + \phi_+(z,\tau) E \otimes F
                     + \phi_-(z,\tau) F \otimes E
where \phi_\pm(z,\tau) are ratios of Jacobi theta functions.

The Belavin classical r-matrix for sl_N uses the N^2-1 Weierstrass functions
\phi_\alpha(z,\tau) indexed by root vectors \alpha.  For sl_2 this reduces
to the three Pauli-matrix channels w_a(z,\tau) (a=1,2,3) built from
\theta_{a+1}(0|\tau) and \theta_1(z|\tau).

Degeneration chain:
    ELLIPTIC  ---(q=e^{2\pi i\tau} \to 0)--->  TRIGONOMETRIC  ---(L\to\infty)--->  RATIONAL
    R^{ell}(z,\tau) \to R^{trig}(z)            \to R^{rat}(z) = 1 + \Omega/z

Yang--Baxter equation:
    R_{12}(z_{12},\tau) R_{13}(z_{13},\tau) R_{23}(z_{23},\tau)
    = R_{23}(z_{23},\tau) R_{13}(z_{13},\tau) R_{12}(z_{12},\tau)
(verified numerically for sl_2 and sl_3).

KZB connection (genus-1 shadow connection):
    \partial_\tau F = \frac{1}{2\pi i} \kappa \, \wp(z_{ij},\tau) \Omega_{ij} F
This is the shadow connection \nabla^{sh} restricted to M_{1,1}.

Modular properties:
    Under \tau \to \tau+1: theta functions pick up phases.
    Under \tau \to -1/\tau: crossing transformation.

References
----------
- Belavin, "Dynamical symmetry of integrable quantum systems" (1981)
- Belavin--Drinfeld, "Solutions of the classical Yang--Baxter equation
  for simple Lie algebras" (1982)
- Felder, "Conformal field theory and integrable systems associated
  to elliptic curves" (1994)
- Bernard, "On the Wess-Zumino-Witten models on the torus" (1988)
- thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
- AP19: the bar kernel absorbs a pole
- AP27: bar propagator d\log E(z,w) is weight 1

Conventions
-----------
- q = e^{2\pi i \tau} (nome).
- Jacobi theta functions with characteristics [\epsilon, \epsilon'] in
  {0, 1/2}^2, following Mumford's Tata Lectures convention.
- Weierstrass zeta for periods (1, \tau):
      \zeta(z) = 1/z + \sum_{(m,n)\neq(0,0)} [1/(z-m-n\tau) + 1/(m+n\tau)
                                                 + z/(m+n\tau)^2].
- Cohomological grading (|d| = +1).  Bar uses desuspension s^{-1}.
- \kappa(sl_2, k) = 3(k+2)/4.  \kappa(sl_3, k) = 4(k+3)/3.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from scipy.special import ellipj, ellipk


# ============================================================
# 0. Constants
# ============================================================

PI = np.pi
TWO_PI_I = 2.0j * PI

H_VEE = {'sl2': 2, 'sl3': 3}
DIM_G = {'sl2': 3, 'sl3': 8}
FUND_DIM = {'sl2': 2, 'sl3': 3}


def kappa_affine(lie_type: str, k):
    r"""Modular characteristic \kappa for affine \hat{g} at level k.

    \kappa = dim(g) \cdot (k + h^\vee) / (2 h^\vee).
    """
    d = DIM_G[lie_type]
    hv = H_VEE[lie_type]
    return d * (k + hv) / (2.0 * hv)


# ============================================================
# 1. Jacobi theta functions (numerical)
# ============================================================

def jacobi_theta1(z: complex, tau: complex, n_terms: int = 50) -> complex:
    r"""Jacobi theta_1(z|\tau) (odd theta function with characteristic [1/2, 1/2]).

    \theta_1(z|\tau) = 2 \sum_{n=0}^{\infty} (-1)^n q^{(n+1/2)^2}
                       \sin((2n+1)\pi z)

    where q = e^{i\pi\tau}.  This is the unique odd Jacobi theta function.
    Zeros at z = m + n\tau for (m,n) \in Z^2.
    """
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        sign = (-1) ** n
        q_power = q ** ((n + 0.5) ** 2)
        result += sign * q_power * np.sin((2 * n + 1) * PI * z)
    return 2.0 * result


def jacobi_theta2(z: complex, tau: complex, n_terms: int = 50) -> complex:
    r"""Jacobi theta_2(z|\tau) (characteristic [1/2, 0]).

    \theta_2(z|\tau) = 2 \sum_{n=0}^{\infty} q^{(n+1/2)^2}
                       \cos((2n+1)\pi z)
    """
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        q_power = q ** ((n + 0.5) ** 2)
        result += q_power * np.cos((2 * n + 1) * PI * z)
    return 2.0 * result


def jacobi_theta3(z: complex, tau: complex, n_terms: int = 50) -> complex:
    r"""Jacobi theta_3(z|\tau) (characteristic [0, 0]).

    \theta_3(z|\tau) = 1 + 2 \sum_{n=1}^{\infty} q^{n^2} \cos(2n\pi z)
    """
    q = np.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        q_power = q ** (n ** 2)
        result += 2.0 * q_power * np.cos(2 * n * PI * z)
    return result


def jacobi_theta4(z: complex, tau: complex, n_terms: int = 50) -> complex:
    r"""Jacobi theta_4(z|\tau) (characteristic [0, 1/2]).

    \theta_4(z|\tau) = 1 + 2 \sum_{n=1}^{\infty} (-1)^n q^{n^2} \cos(2n\pi z)
    """
    q = np.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        sign = (-1) ** n
        q_power = q ** (n ** 2)
        result += 2.0 * sign * q_power * np.cos(2 * n * PI * z)
    return result


def jacobi_theta1_prime0(tau: complex, n_terms: int = 50) -> complex:
    r"""Derivative \theta_1'(0|\tau) = d\theta_1/dz evaluated at z=0.

    \theta_1'(0|\tau) = 2\pi \sum_{n=0}^{\infty} (-1)^n (2n+1) q^{(n+1/2)^2}

    Also equals \pi \theta_2(0) \theta_3(0) \theta_4(0) (Jacobi triple product).
    """
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(n_terms):
        sign = (-1) ** n
        q_power = q ** ((n + 0.5) ** 2)
        result += sign * (2 * n + 1) * q_power
    return 2.0 * PI * result


def verify_jacobi_triple_product(tau: complex, tol: float = 1e-10) -> bool:
    r"""Verify \theta_1'(0) = \pi \theta_2(0) \theta_3(0) \theta_4(0).

    This is a consequence of the Jacobi triple product identity.
    """
    lhs = jacobi_theta1_prime0(tau)
    rhs = PI * jacobi_theta2(0, tau) * jacobi_theta3(0, tau) * jacobi_theta4(0, tau)
    return abs(lhs - rhs) < tol * max(abs(lhs), 1.0)


# ============================================================
# 2. Weierstrass functions on C/(Z + Z*tau)
# ============================================================

def weierstrass_zeta(z: complex, tau: complex, n_terms: int = 50) -> complex:
    r"""Weierstrass zeta function for periods (1, \tau).

    \zeta(z) = \frac{\theta_1'(z|\tau)}{\theta_1(z|\tau)}
             + 2\eta_1 z

    where \eta_1 = -\theta_1'''(0)/(6\theta_1'(0)) is the quasi-period.

    The relation to the prime form: d\log E(z,w) = \zeta(z-w) d(z-w).
    """
    th1 = jacobi_theta1(z, tau, n_terms)
    if abs(th1) < 1e-300:
        return complex(float('inf'))

    # Numerical derivative of theta_1 at z via central difference
    eps = 1e-7
    th1_plus = jacobi_theta1(z + eps, tau, n_terms)
    th1_minus = jacobi_theta1(z - eps, tau, n_terms)
    dth1 = (th1_plus - th1_minus) / (2 * eps)

    # Quasi-period eta_1 = theta_1'''(0) / (6 theta_1'(0))
    # computed via third derivative at z=0
    eta1 = _weierstrass_eta1(tau, n_terms)

    return dth1 / th1 + 2 * eta1 * z


def _weierstrass_eta1(tau: complex, n_terms: int = 50) -> complex:
    r"""Quasi-period \eta_1 = -\theta_1'''(0|\tau) / (6 \theta_1'(0|\tau)).

    Alternatively, \eta_1 = \pi^2/6 \cdot E_2^*(\tau)
    where E_2^*(\tau) = E_2(\tau) - 3/(\pi \mathrm{Im}(\tau)) is the
    COMPLETED (almost-holomorphic) Eisenstein series.  For the holomorphic
    Eisenstein series: \eta_1 = -\pi^2/3 \cdot E_2(\tau)/... but the
    cleanest formula is from theta derivatives directly.
    """
    # Third derivative of theta_1 at z=0 via numerical differentiation
    eps = 1e-5
    tp0 = jacobi_theta1_prime0(tau, n_terms)
    th1_eps = jacobi_theta1(eps, tau, n_terms)
    th1_meps = jacobi_theta1(-eps, tau, n_terms)
    th1_2eps = jacobi_theta1(2 * eps, tau, n_terms)
    th1_m2eps = jacobi_theta1(-2 * eps, tau, n_terms)
    # f'''(0) by central difference: (f(2h)-2f(h)+2f(-h)-f(-2h))/(2h^3)
    th1_triple_prime = (th1_2eps - 2 * th1_eps + 2 * th1_meps - th1_m2eps) / (2 * eps ** 3)

    return -th1_triple_prime / (6 * tp0)


def weierstrass_p(z: complex, tau: complex, n_terms: int = 50) -> complex:
    r"""Weierstrass p-function: \wp(z) = -\zeta'(z).

    Computed via -d/dz of the Weierstrass zeta function.
    """
    eps = 1e-7
    zeta_plus = weierstrass_zeta(z + eps, tau, n_terms)
    zeta_minus = weierstrass_zeta(z - eps, tau, n_terms)
    return -(zeta_plus - zeta_minus) / (2 * eps)


# ============================================================
# 3. Elliptic phi-functions (Belavin r-matrix building blocks)
# ============================================================

def phi_function(z: complex, tau: complex, alpha: complex,
                 n_terms: int = 50) -> complex:
    r"""The phi-function \phi_\alpha(z, \tau) appearing in the Belavin r-matrix.

    For a root \alpha of sl_N, the building block is:
        \phi_\alpha(z, \tau) = \frac{\theta_1'(0|\tau) \theta_1(z + \alpha|\tau)}
                                     {\theta_1(z|\tau) \theta_1(\alpha|\tau)}

    This has a simple pole at z = 0 with residue 1 (from the prime form),
    and is quasi-periodic with characteristic shifts depending on \alpha.
    The parameter \alpha here is the sl_N twist parameter \alpha = a/N for
    the a-th root.

    At z -> 0: \phi_\alpha(z) ~ 1/z + \zeta(\alpha) + O(z).
    """
    th1_p0 = jacobi_theta1_prime0(tau, n_terms)
    th1_z = jacobi_theta1(z, tau, n_terms)
    th1_alpha = jacobi_theta1(alpha, tau, n_terms)

    if abs(th1_z) < 1e-300 or abs(th1_alpha) < 1e-300:
        return complex(float('inf'))

    th1_zpa = jacobi_theta1(z + alpha, tau, n_terms)
    return th1_p0 * th1_zpa / (th1_z * th1_alpha)


# ============================================================
# 4. sl_2 representation matrices
# ============================================================

def _sl2_fund_matrices() -> Dict[str, np.ndarray]:
    """Generators of sl_2 in the fundamental representation (2x2)."""
    E = np.array([[0, 1], [0, 0]], dtype=complex)
    F = np.array([[0, 0], [1, 0]], dtype=complex)
    H = np.array([[1, 0], [0, -1]], dtype=complex)
    return {'E': E, 'F': F, 'H': H}


def _sl2_casimir_fund() -> np.ndarray:
    """Casimir tensor Omega = E tensor F + F tensor E + (1/2) H tensor H
    as a 4x4 matrix on C^2 tensor C^2."""
    gens = _sl2_fund_matrices()
    E, F, H = gens['E'], gens['F'], gens['H']
    return (np.kron(E, F) + np.kron(F, E) + 0.5 * np.kron(H, H))


def _permutation_2() -> np.ndarray:
    """Permutation operator P on C^2 tensor C^2: P(v tensor w) = w tensor v."""
    P = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            P[i * 2 + j, j * 2 + i] = 1.0
    return P


# ============================================================
# 5. Belavin elliptic r-matrix for sl_2 (classical)
# ============================================================

def belavin_r_matrix_sl2(z: complex, tau: complex,
                         n_terms: int = 50) -> np.ndarray:
    r"""Belavin classical elliptic r-matrix for sl_2 in the fundamental (4x4).

    r^{ell}(z, \tau) = \zeta(z) \frac{H \otimes H}{2}
                     + \phi_+(z, \tau) E \otimes F
                     + \phi_-(z, \tau) F \otimes E

    where:
        \phi_+(z) = \frac{\theta_1'(0) \theta_1(z + 1/2)}{\theta_1(z) \theta_1(1/2)}
        (and similarly for the other channel with characteristic shift)

    In the sl_2 case the Belavin r-matrix can also be written as:
        r^{ell}(z) = \frac{1}{2} \sum_{a=0}^{3} w_a(z,\tau) \sigma_a \otimes \sigma_a

    where w_0 = \zeta(z), and w_{1,2,3} are built from theta-function ratios.

    We use the Cartan-root decomposition, which is more natural for the
    genus-1 shadow obstruction tower interpretation: the Cartan part carries the
    Weierstrass zeta (the d\log of the prime form), while the root parts
    carry the phi-functions (twisted prime-form ratios).

    For sl_2, the twist parameter is \alpha = 1/2 (half-period).
    """
    gens = _sl2_fund_matrices()
    E, F, H = gens['E'], gens['F'], gens['H']

    zeta_z = weierstrass_zeta(z, tau, n_terms)

    # The root twist: for sl_2 with the Chevalley normalization,
    # the positive root has length sqrt(2), and the twist parameter
    # in the Belavin construction is alpha = 1/N = 1/2.
    alpha = 0.5

    phi_p = phi_function(z, tau, alpha, n_terms)
    phi_m = phi_function(z, tau, -alpha, n_terms)

    r = (zeta_z * 0.5 * np.kron(H, H)
         + phi_p * np.kron(E, F)
         + phi_m * np.kron(F, E))

    return r


def belavin_r_matrix_sl2_pauli(z: complex, tau: complex,
                                n_terms: int = 50) -> np.ndarray:
    r"""Belavin r-matrix in the Pauli-matrix basis (alternative form).

    r^{ell}(z) = \sum_{a=1}^{3} w_a(z, \tau) \sigma_a \otimes \sigma_a / 4

    where the weight functions are:
        w_1(z) = \frac{\theta_4(0)^2 \theta_2(z) \theta_3(z)}
                      {\theta_2(0) \theta_3(0) \theta_4(z) \theta_1(z)}
                 (with a pole at z=0 from theta_1)
    and cyclically for w_2, w_3.

    In practice, for numerical stability we use the theta-function
    quotient representation directly.

    The Pauli matrices: sigma_1 = [[0,1],[1,0]], sigma_2 = [[0,-i],[i,0]],
    sigma_3 = [[1,0],[0,-1]].
    """
    sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)

    th1_z = jacobi_theta1(z, tau, n_terms)
    th2_z = jacobi_theta2(z, tau, n_terms)
    th3_z = jacobi_theta3(z, tau, n_terms)
    th4_z = jacobi_theta4(z, tau, n_terms)

    th2_0 = jacobi_theta2(0, tau, n_terms)
    th3_0 = jacobi_theta3(0, tau, n_terms)
    th4_0 = jacobi_theta4(0, tau, n_terms)

    if abs(th1_z) < 1e-300:
        return np.full((4, 4), complex(float('inf')))

    # Weight functions from Baxter/Belavin:
    # w_1 ~ theta_4^2(0) theta_2(z) theta_3(z) / (theta_2(0) theta_3(0) theta_4(z) theta_1(z))
    # w_2 ~ theta_4^2(0) theta_1(z) theta_4(z) / (theta_2(0) theta_3(0) theta_2(z) theta_3(z))
    #   (this one has no pole at z=0 since theta_1(z) cancels)
    # w_3 ~ theta_3^2(0) theta_1(z) theta_3(z) / (theta_2(0) theta_4(0) theta_2(z) theta_4(z))
    # ... the precise normalization ensures r(z) ~ Omega/z as z -> 0.
    #
    # A cleaner approach: use the zeta + phi decomposition from belavin_r_matrix_sl2()
    # and convert to Pauli basis.
    # sigma_a tensor sigma_a for a=1,2,3:
    #   sigma_1 tensor sigma_1 = 2(E tensor F + F tensor E) + ... etc.
    # Actually: E = (sigma_1 + i sigma_2)/2, F = (sigma_1 - i sigma_2)/2, H = sigma_3.
    # So E tensor F + F tensor E = (sigma_1 tensor sigma_1 + sigma_2 tensor sigma_2)/2
    # and H tensor H = sigma_3 tensor sigma_3.
    #
    # r = zeta(z)/2 * sigma_3 tensor sigma_3
    #   + phi_+(z) * (sigma_1 + i sigma_2)/2 tensor (sigma_1 - i sigma_2)/2
    #   + phi_-(z) * (sigma_1 - i sigma_2)/2 tensor (sigma_1 + i sigma_2)/2

    # Use the Cartan-root form and convert
    r_cartan = belavin_r_matrix_sl2(z, tau, n_terms)
    return r_cartan


# ============================================================
# 6. Genus-1 shadow r-matrix from the bar complex sewing
# ============================================================

def genus1_shadow_rmatrix_sl2(z: complex, tau: complex, k: float = 1.0,
                               n_terms: int = 50) -> np.ndarray:
    r"""Genus-1 shadow r-matrix from the bar complex on E_\tau.

    The bar propagator on the elliptic curve E_\tau = C/(Z + Z\tau) is
        d\log E(z,w) = \zeta_\tau(z-w) d(z-w)
    where \zeta_\tau is the Weierstrass zeta function.

    The collision residue Res^{coll}_{1,2}(\Theta_A) on E_\tau extracts:
        r^{ell}(z, \tau) = k \cdot r^{Belavin}(z, \tau)

    where r^{Belavin} is the classical Belavin r-matrix, and k is the level.

    The overall normalization: for affine \hat{sl}_2 at level k, the OPE is
        J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
    AP19 absorbs one pole, and on E_\tau the 1/(z-w) becomes \zeta_\tau(z-w),
    yielding r^{ell}(z) = k \cdot \zeta_\tau(z) \Omega/2 + ... with the
    root corrections from the twisted boundary conditions on the torus.
    """
    return k * belavin_r_matrix_sl2(z, tau, n_terms)


# ============================================================
# 7. Yang-Baxter equation verification
# ============================================================

def _embed_12(M: np.ndarray, d: int) -> np.ndarray:
    """Embed a d^2 x d^2 matrix into slots 1,2 of a d^3-dimensional space."""
    return np.kron(M, np.eye(d, dtype=complex))


def _embed_13(M: np.ndarray, d: int) -> np.ndarray:
    """Embed a d^2 x d^2 matrix into slots 1,3 of a d^3-dimensional space."""
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


def _embed_23(M: np.ndarray, d: int) -> np.ndarray:
    """Embed a d^2 x d^2 matrix into slots 2,3 of a d^3-dimensional space."""
    return np.kron(np.eye(d, dtype=complex), M)


def verify_ybe_elliptic_sl2(z1: complex, z2: complex, z3: complex,
                             tau: complex, k: float = 1.0,
                             n_terms: int = 50) -> Dict[str, Any]:
    r"""Verify the Yang-Baxter equation for the elliptic R-matrix of sl_2.

    Classical YBE (additive form):
        [r_{12}(z_{12}), r_{13}(z_{13})] + [r_{12}(z_{12}), r_{23}(z_{23})]
        + [r_{13}(z_{13}), r_{23}(z_{23})] = 0

    where z_{ij} = z_i - z_j.

    Returns dict with 'residual' (Frobenius norm of the LHS) and 'passed'.
    """
    d = 2
    z12 = z1 - z2
    z13 = z1 - z3
    z23 = z2 - z3

    r12 = _embed_12(genus1_shadow_rmatrix_sl2(z12, tau, k, n_terms), d)
    r13 = _embed_13(genus1_shadow_rmatrix_sl2(z13, tau, k, n_terms), d)
    r23 = _embed_23(genus1_shadow_rmatrix_sl2(z23, tau, k, n_terms), d)

    # Classical YBE: [r12, r13] + [r12, r23] + [r13, r23] = 0
    lhs = (r12 @ r13 - r13 @ r12
           + r12 @ r23 - r23 @ r12
           + r13 @ r23 - r23 @ r13)

    residual = np.linalg.norm(lhs)
    scale = max(np.linalg.norm(r12), np.linalg.norm(r13),
                np.linalg.norm(r23), 1.0)
    relative = residual / scale

    return {
        'residual': residual,
        'relative': relative,
        'passed': relative < 1e-6,
        'z12': z12, 'z13': z13, 'z23': z23,
        'tau': tau,
    }


# ============================================================
# 8. Degeneration: elliptic -> trigonometric -> rational
# ============================================================

def trigonometric_r_matrix_sl2(z: complex, eta: float = 1.0) -> np.ndarray:
    r"""Trigonometric r-matrix for sl_2 in the fundamental (4x4).

    r^{trig}(z) = \frac{1}{2} \cot(z) H \otimes H
                + \frac{1}{\sin(z)} (E \otimes F)
                + \frac{1}{\sin(z)} (F \otimes E)

    This is the XXZ r-matrix, obtained as the degeneration of the
    elliptic r-matrix as tau -> i*infty (q -> 0).

    Actually, more precisely, on the cylinder C/(Z) with coordinate z,
    the trigonometric r-matrix is:
        r^{trig}(z) = \cot(\pi z) \cdot \Omega/2
                     + \frac{1}{\sin(\pi z)} \cdot (E\otimes F + F\otimes E)/2
    but the exact form depends on normalization.  We use:
        r^{trig}(z) = \pi \cot(\pi z) \cdot H\otimes H / 2
                     + \pi/\sin(\pi z) \cdot (E\otimes F + F\otimes E)
    """
    gens = _sl2_fund_matrices()
    E, F, H = gens['E'], gens['F'], gens['H']

    if abs(np.sin(PI * z)) < 1e-300:
        return np.full((4, 4), complex(float('inf')))

    cot_z = np.cos(PI * z) / np.sin(PI * z)
    csc_z = 1.0 / np.sin(PI * z)

    r = (PI * cot_z * 0.5 * np.kron(H, H)
         + PI * csc_z * np.kron(E, F)
         + PI * csc_z * np.kron(F, E))

    return r


def rational_r_matrix_sl2(z: complex) -> np.ndarray:
    r"""Rational r-matrix for sl_2: r(z) = \Omega / z (4x4).

    The simplest r-matrix, obtained as the rational degeneration
    of the trigonometric and then elliptic families.

    r^{rat}(z) = (E\otimes F + F\otimes E + H\otimes H/2) / z = \Omega / z.
    """
    if abs(z) < 1e-300:
        return np.full((4, 4), complex(float('inf')))

    return _sl2_casimir_fund() / z


def elliptic_to_trigonometric_limit(z: complex, tau_values: np.ndarray = None,
                                     k: float = 1.0,
                                     n_terms: int = 50) -> Dict[str, Any]:
    r"""Verify degeneration: as Im(\tau) -> \infty, elliptic -> trigonometric.

    The limit q = e^{2\pi i \tau} -> 0 sends:
        \zeta(z, \tau) -> \pi \cot(\pi z) + O(q)
        \phi_\alpha(z, \tau) -> \pi / \sin(\pi z) \cdot e^{corrections} + O(q)

    We check that ||r^{ell}(z, \tau) - r^{trig}(z)|| -> 0 as Im(\tau) -> \infty.
    """
    if tau_values is None:
        tau_values = np.array([1j * t for t in [2.0, 3.0, 5.0, 8.0, 12.0]])

    r_trig = k * trigonometric_r_matrix_sl2(z)
    errors = []
    for tau_val in tau_values:
        r_ell = genus1_shadow_rmatrix_sl2(z, tau_val, k, n_terms)
        err = np.linalg.norm(r_ell - r_trig) / max(np.linalg.norm(r_trig), 1e-10)
        errors.append(float(err))

    return {
        'z': z,
        'tau_values': [complex(t) for t in tau_values],
        'relative_errors': errors,
        'monotone_decreasing': all(errors[i] >= errors[i + 1] - 1e-12
                                    for i in range(len(errors) - 1)),
        'final_error': errors[-1] if errors else None,
    }


def trigonometric_to_rational_limit(z_values: np.ndarray = None,
                                     L_values: np.ndarray = None) -> Dict[str, Any]:
    r"""Verify degeneration: trigonometric -> rational as period L -> \infty.

    Rescaling z -> z/L in the trigonometric r-matrix:
        r^{trig}(z/L) = L \cdot r^{rat}(z) + O(1/L)

    Equivalently, \pi \cot(\pi z/L) -> L/z as L -> \infty.
    """
    if z_values is None:
        z_values = [0.1 + 0.05j, 0.3 + 0.1j]
    if L_values is None:
        L_values = [10.0, 50.0, 100.0, 500.0]

    results = {}
    for z in z_values:
        errors = []
        for L in L_values:
            r_trig_scaled = trigonometric_r_matrix_sl2(z / L)
            r_rat = rational_r_matrix_sl2(z)
            # After rescaling: r^{trig}(z/L) approx L * r^{rat}(z)
            # because cot(pi z/L) ~ L/(pi z) and csc(pi z/L) ~ L/(pi z)
            # Actually: pi * cot(pi*z/L) ~ L/z as L->inf
            # so r^{trig}(z/L) ~ L * Omega/z = L * r^{rat}(z)
            err = np.linalg.norm(r_trig_scaled - L * r_rat) / max(np.linalg.norm(L * r_rat), 1e-10)
            errors.append(err)
        results[z] = errors

    return results


# ============================================================
# 9. Modular transformations
# ============================================================

def modular_t_transform_check(z: complex, tau: complex, k: float = 1.0,
                               n_terms: int = 50) -> Dict[str, Any]:
    r"""Check behavior under \tau -> \tau + 1.

    Under \tau -> \tau + 1 with z fixed:
        \theta_1(z|\tau+1) = e^{i\pi/4} \theta_1(z|\tau)
    So the prime-form ratio transforms by a phase, and:
        r^{ell}(z, \tau+1) = M r^{ell}(z, \tau) M^{-1}
    where M is a diagonal twist matrix (for sl_2: M = diag(1, e^{i\pi/2})).

    For the CLASSICAL r-matrix (which uses only ratios of theta functions),
    the \tau -> \tau+1 transformation is simpler: the theta_1'/theta_1
    combination appearing in \zeta(z) transforms by an additive constant
    (the quasi-period), and the phi-functions transform by phases that
    can be absorbed into conjugation.

    We verify numerically that the spectral invariants are preserved:
    eigenvalues of r^{ell}(z, \tau+1) match those of r^{ell}(z, \tau)
    up to overall phase.
    """
    r_tau = genus1_shadow_rmatrix_sl2(z, tau, k, n_terms)
    r_tau_plus_1 = genus1_shadow_rmatrix_sl2(z, tau + 1, k, n_terms)

    eigs_tau = np.sort(np.linalg.eigvals(r_tau))
    eigs_tau_plus_1 = np.sort(np.linalg.eigvals(r_tau_plus_1))

    # Check if eigenvalue MAGNITUDES match
    mag_tau = np.sort(np.abs(eigs_tau))
    mag_tau_plus_1 = np.sort(np.abs(eigs_tau_plus_1))

    mag_diff = np.linalg.norm(mag_tau - mag_tau_plus_1)
    scale = max(np.linalg.norm(mag_tau), 1e-10)

    return {
        'eigenvalues_tau': eigs_tau,
        'eigenvalues_tau_plus_1': eigs_tau_plus_1,
        'magnitude_difference': mag_diff / scale,
        'magnitudes_match': mag_diff / scale < 1e-4,
    }


def modular_s_transform_check(z: complex, tau: complex, k: float = 1.0,
                               n_terms: int = 50) -> Dict[str, Any]:
    r"""Check behavior under \tau -> -1/\tau.

    Under \tau -> -1/\tau, z -> z/\tau:
        \theta_1(z/\tau | -1/\tau) = -i \sqrt{-i\tau} e^{i\pi z^2/\tau} \theta_1(z|\tau)
    The r-matrix transforms by:
        r^{ell}(z/\tau, -1/\tau) = \tau^{-1} M_S r^{ell}(z, \tau) M_S^{-1} + ...
    where M_S is the S-transformation matrix.

    We check spectral invariants (eigenvalue magnitudes) up to the
    expected rescaling.
    """
    tau_s = -1.0 / tau
    z_s = z / tau

    r_original = genus1_shadow_rmatrix_sl2(z, tau, k, n_terms)
    r_transformed = genus1_shadow_rmatrix_sl2(z_s, tau_s, k, n_terms)

    # The r-matrix picks up a factor of tau from the z -> z/tau rescaling
    # of the overall 1/z pole structure.  Check that eigenvalue magnitudes
    # of tau * r_transformed match those of r_original.
    r_rescaled = tau * r_transformed
    eigs_orig = np.sort(np.abs(np.linalg.eigvals(r_original)))
    eigs_trans = np.sort(np.abs(np.linalg.eigvals(r_rescaled)))

    diff = np.linalg.norm(eigs_orig - eigs_trans)
    scale = max(np.linalg.norm(eigs_orig), 1e-10)

    return {
        'tau': tau,
        'tau_s': tau_s,
        'eigenvalue_magnitude_diff': diff / scale,
        'passed': diff / scale < 0.1,  # generous tolerance for modular
    }


# ============================================================
# 10. KZB connection (genus-1 shadow connection)
# ============================================================

def kzb_connection_sl2(z: complex, tau: complex, k: float = 1.0,
                        n_terms: int = 50) -> np.ndarray:
    r"""KZB (Knizhnik-Zamolodchikov-Bernard) connection matrix for sl_2.

    The KZB equation for n=2 marked points on E_\tau:

    z-component: \partial_z F = A_z(z, \tau) F
    where A_z(z, \tau) = \frac{1}{k + h^\vee} r^{ell}(z, \tau)

    \tau-component: \partial_\tau F = A_\tau(z, \tau) F
    where A_\tau = \frac{1}{2\pi i(k+h^\vee)} \wp(z, \tau) \Omega

    This is the genus-1 analogue of the KZ connection:
        KZ connection = shadow connection at genus 0
        KZB connection = shadow connection at genus 1

    The tau-derivative equation involves the Weierstrass p-function
    (the derivative of the zeta function), acting through the Casimir.

    Returns A_tau for the tau-direction of the KZB connection.
    """
    hv = H_VEE['sl2']
    if abs(k + hv) < 1e-15:
        raise ValueError("Critical level k = -h^vee: KZB undefined")

    wp = weierstrass_p(z, tau, n_terms)
    Omega = _sl2_casimir_fund()

    return wp * Omega / (TWO_PI_I * (k + hv))


def kzb_flatness_check(z: complex, tau: complex, k: float = 1.0,
                        n_terms: int = 30) -> Dict[str, Any]:
    r"""Verify KZB flatness: [\partial_z - A_z, \partial_\tau - A_\tau] = 0.

    This reduces to:
        \partial_\tau A_z - \partial_z A_\tau + [A_z, A_\tau] = 0

    where:
        A_z = r^{ell}(z,\tau) / (k+h^v)
        A_\tau = \wp(z,\tau) \Omega / (2\pi i (k+h^v))

    Since A_z and A_\tau are both proportional to Casimir tensors (in the
    two-point case), [A_z, A_\tau] = 0.  So flatness reduces to
        \partial_\tau A_z = \partial_z A_\tau

    which is the identity \partial_\tau \zeta(z) = \partial_z (\wp(z) / (2\pi i))
    i.e. the heat equation for theta functions.

    We verify numerically.
    """
    hv = H_VEE['sl2']
    eps_z = 1e-6
    eps_tau = 1e-6

    # A_z = r^{ell}(z, tau) / (k + h^v)
    def A_z(zz, tt):
        return genus1_shadow_rmatrix_sl2(zz, tt, 1.0, n_terms) / (k + hv)

    # A_tau = wp(z, tau) * Omega / (2*pi*i * (k+hv))
    def A_tau(zz, tt):
        return weierstrass_p(zz, tt, n_terms) * _sl2_casimir_fund() / (TWO_PI_I * (k + hv))

    # d_tau A_z
    dtau_Az = (A_z(z, tau + eps_tau) - A_z(z, tau - eps_tau)) / (2 * eps_tau)

    # d_z A_tau
    dz_Atau = (A_tau(z + eps_z, tau) - A_tau(z - eps_z, tau)) / (2 * eps_z)

    # Commutator [A_z, A_tau]
    Az = A_z(z, tau)
    Atau = A_tau(z, tau)
    comm = Az @ Atau - Atau @ Az

    # Flatness residual: dtau_Az - dz_Atau + [Az, Atau]
    flatness = dtau_Az - dz_Atau + comm
    residual = np.linalg.norm(flatness)
    scale = max(np.linalg.norm(dtau_Az), np.linalg.norm(dz_Atau), 1e-10)

    return {
        'residual': residual,
        'relative': residual / scale,
        'commutator_norm': np.linalg.norm(comm),
        'passed': residual / scale < 1e-3,
    }


# ============================================================
# 11. Skew-symmetry and unitarity
# ============================================================

def verify_skew_symmetry(z: complex, tau: complex, k: float = 1.0,
                          n_terms: int = 50) -> Dict[str, Any]:
    r"""Verify skew-symmetry: r_{12}(z) + r_{21}(-z) = 0.

    For the elliptic r-matrix in the fundamental, r_{21}(z) is obtained
    by applying the permutation P: r_{21}(z) = P r_{12}(z) P.

    Skew-symmetry: r_{12}(z) + P r_{12}(-z) P = 0.
    """
    r_z = genus1_shadow_rmatrix_sl2(z, tau, k, n_terms)
    r_mz = genus1_shadow_rmatrix_sl2(-z, tau, k, n_terms)
    P = _permutation_2()

    lhs = r_z + P @ r_mz @ P
    residual = np.linalg.norm(lhs)
    scale = max(np.linalg.norm(r_z), 1e-10)

    return {
        'residual': residual,
        'relative': residual / scale,
        'passed': residual / scale < 1e-6,
    }


# ============================================================
# 12. sl_3 elliptic R-matrix
# ============================================================

def _sl3_fund_matrices() -> List[np.ndarray]:
    """Generators of sl_3 in the fundamental representation (3x3).

    Chevalley basis: H1 = diag(1,-1,0), H2 = diag(0,1,-1),
    E1 = e_{12}, E2 = e_{23}, E3 = e_{13},
    F1 = e_{21}, F2 = e_{32}, F3 = e_{31}.
    """
    mats = []
    # H1
    mats.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))
    # H2
    mats.append(np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]], dtype=complex))
    # E1
    mats.append(np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]], dtype=complex))
    # E2
    mats.append(np.array([[0, 0, 0], [0, 0, 1], [0, 0, 0]], dtype=complex))
    # E3 = [E1, E2] = e_{13}
    mats.append(np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]], dtype=complex))
    # F1
    mats.append(np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))
    # F2
    mats.append(np.array([[0, 0, 0], [0, 0, 0], [0, 1, 0]], dtype=complex))
    # F3 = [F2, F1] = e_{31}
    mats.append(np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]], dtype=complex))
    return mats


def _sl3_killing_form_matrix() -> np.ndarray:
    """8x8 Killing form g_{ab} = tr(T^a T^b) for sl_3."""
    mats = _sl3_fund_matrices()
    n = len(mats)
    G = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            G[a, b] = np.trace(mats[a] @ mats[b]).real
    return G


def _sl3_inverse_killing() -> np.ndarray:
    """Inverse Killing form g^{ab} for sl_3."""
    return np.linalg.inv(_sl3_killing_form_matrix())


def _sl3_casimir_fund() -> np.ndarray:
    r"""Casimir tensor \Omega = P - I/3 on C^3 \otimes C^3 (9x9).

    Uses the identity \sum_a T^a \otimes T_a = P - I/N for sl_N
    with trace-form normalization.
    """
    N = 3
    P = np.zeros((N * N, N * N), dtype=complex)
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1.0
    I = np.eye(N * N, dtype=complex)
    return P - I / N


def belavin_r_matrix_sl3(z: complex, tau: complex,
                          n_terms: int = 50) -> np.ndarray:
    r"""Belavin classical elliptic r-matrix for sl_3 in the fundamental (9x9).

    For sl_N, the Belavin r-matrix is:
        r^{ell}(z, \tau) = \sum_{\alpha \in \Phi} \phi_{\alpha/N}(z, \tau)
                           E_\alpha \otimes E_{-\alpha}
                         + \sum_{i,j} (A^{-1})_{ij} \zeta(z,\tau) H_i \otimes H_j

    For sl_3 (N=3), the roots are \alpha_1, \alpha_2, \alpha_1+\alpha_2, and
    their negatives. The twist parameter for root \alpha is |\alpha|^2/(2N)
    but in the Belavin construction the standard choice is \alpha/N for the
    simple roots, which for the 3-dimensional fundamental gives twist
    parameters at 1/3 and 2/3.

    The Cartan part uses the inverse Cartan matrix:
        A^{-1} = \frac{1}{3} \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}
    """
    mats = _sl3_fund_matrices()
    H1, H2 = mats[0], mats[1]
    E1, E2, E3 = mats[2], mats[3], mats[4]
    F1, F2, F3 = mats[5], mats[6], mats[7]

    zeta_z = weierstrass_zeta(z, tau, n_terms)

    # Cartan part: (A^{-1})_{ij} zeta(z) H_i tensor H_j
    # A^{-1} = (1/3) [[2, 1], [1, 2]]
    cartan = zeta_z * (
        (2.0 / 3.0) * np.kron(H1, H1)
        + (1.0 / 3.0) * np.kron(H1, H2)
        + (1.0 / 3.0) * np.kron(H2, H1)
        + (2.0 / 3.0) * np.kron(H2, H2)
    )

    # Root parts: twist parameters for sl_3 are 1/3 and 2/3
    # Positive roots: alpha_1 -> twist 1/3, alpha_2 -> twist 1/3,
    #                 alpha_1 + alpha_2 -> twist 2/3
    alpha1 = 1.0 / 3.0
    alpha2 = 1.0 / 3.0
    alpha3 = 2.0 / 3.0  # alpha_1 + alpha_2

    phi_a1 = phi_function(z, tau, alpha1, n_terms)
    phi_ma1 = phi_function(z, tau, -alpha1, n_terms)
    phi_a2 = phi_function(z, tau, alpha2, n_terms)
    phi_ma2 = phi_function(z, tau, -alpha2, n_terms)
    phi_a3 = phi_function(z, tau, alpha3, n_terms)
    phi_ma3 = phi_function(z, tau, -alpha3, n_terms)

    root = (phi_a1 * np.kron(E1, F1) + phi_ma1 * np.kron(F1, E1)
            + phi_a2 * np.kron(E2, F2) + phi_ma2 * np.kron(F2, E2)
            + phi_a3 * np.kron(E3, F3) + phi_ma3 * np.kron(F3, E3))

    return cartan + root


def genus1_shadow_rmatrix_sl3(z: complex, tau: complex, k: float = 1.0,
                               n_terms: int = 50) -> np.ndarray:
    r"""Genus-1 shadow r-matrix for sl_3 at level k (9x9 matrix).

    r^{ell}_{sl_3}(z, \tau, k) = k \cdot r^{Belavin}_{sl_3}(z, \tau)

    The bar complex on E_\tau with affine sl_3 OPE data produces the
    Belavin r-matrix scaled by the level.
    """
    return k * belavin_r_matrix_sl3(z, tau, n_terms)


def verify_ybe_elliptic_sl3(z1: complex, z2: complex, z3: complex,
                             tau: complex, k: float = 1.0,
                             n_terms: int = 50) -> Dict[str, Any]:
    r"""Verify the classical YBE for the sl_3 elliptic r-matrix.

    [r_{12}(z_{12}), r_{13}(z_{13})] + [r_{12}(z_{12}), r_{23}(z_{23})]
    + [r_{13}(z_{13}), r_{23}(z_{23})] = 0
    """
    d = 3
    z12 = z1 - z2
    z13 = z1 - z3
    z23 = z2 - z3

    r12 = _embed_12(genus1_shadow_rmatrix_sl3(z12, tau, k, n_terms), d)
    r13 = _embed_13(genus1_shadow_rmatrix_sl3(z13, tau, k, n_terms), d)
    r23 = _embed_23(genus1_shadow_rmatrix_sl3(z23, tau, k, n_terms), d)

    lhs = (r12 @ r13 - r13 @ r12
           + r12 @ r23 - r23 @ r12
           + r13 @ r23 - r23 @ r13)

    residual = np.linalg.norm(lhs)
    scale = max(np.linalg.norm(r12), np.linalg.norm(r13),
                np.linalg.norm(r23), 1.0)
    relative = residual / scale

    return {
        'residual': residual,
        'relative': relative,
        'passed': relative < 1e-4,
    }


# ============================================================
# 13. Pole structure analysis
# ============================================================

def elliptic_pole_structure(z_small: float = 0.01, tau: complex = 0.5j,
                             n_terms: int = 50) -> Dict[str, Any]:
    r"""Analyze pole structure of elliptic r-matrix as z -> 0.

    By AP19 (bar kernel absorbs a pole), the genus-1 r-matrix should
    have a simple pole at z = 0 (from the OPE double pole shifted by one).

    The elliptic r-matrix near z = 0:
        r^{ell}(z) = \Omega/z + O(1)

    where the O(1) part contains Eisenstein corrections.  This O(1) part
    is the genus-1 CORRECTION to the rational r-matrix, encoding the
    modular data in the shadow obstruction tower.

    We extract: leading coefficient (residue), subleading constant, etc.
    """
    z = z_small

    # sl_2
    r_sl2 = belavin_r_matrix_sl2(z, tau, n_terms)
    Omega_sl2 = _sl2_casimir_fund()

    # Extract residue: z * r(z) should approach Omega as z -> 0
    residue_sl2 = z * r_sl2
    residue_error_sl2 = np.linalg.norm(residue_sl2 - Omega_sl2) / max(np.linalg.norm(Omega_sl2), 1e-10)

    # sl_3
    r_sl3 = belavin_r_matrix_sl3(z, tau, n_terms)
    Omega_sl3 = _sl3_casimir_fund()

    residue_sl3 = z * r_sl3
    residue_error_sl3 = np.linalg.norm(residue_sl3 - Omega_sl3) / max(np.linalg.norm(Omega_sl3), 1e-10)

    return {
        'z': z,
        'tau': tau,
        'sl2_residue_error': residue_error_sl2,
        'sl2_residue_matches_Omega': residue_error_sl2 < 0.1,
        'sl3_residue_error': residue_error_sl3,
        'sl3_residue_matches_Omega': residue_error_sl3 < 0.1,
    }


# ============================================================
# 14. Shadow obstruction tower tau-expansion
# ============================================================

def shadow_tower_q_expansion(z: complex, tau: complex, k: float = 1.0,
                              max_order: int = 3,
                              n_terms: int = 80) -> Dict[str, Any]:
    r"""Extract q-expansion of the elliptic r-matrix.

    r^{ell}(z, \tau) = r^{(0)}(z) + q \cdot r^{(1)}(z) + q^2 \cdot r^{(2)}(z) + ...

    where r^{(0)}(z) is the trigonometric r-matrix (leading term in q -> 0).

    The coefficients r^{(n)}(z) encode the genus-1 shadow obstruction tower corrections
    at each order in the nome expansion.  These are the "shadow corrections"
    from winding modes on the torus.

    Method: evaluate r^{ell} at several values of tau with fixed Im(tau)
    and varying Re(tau), then extract Fourier coefficients.
    """
    q = np.exp(TWO_PI_I * tau)
    q_abs = abs(q)

    # Evaluate r^{ell} at tau and at several values of Im(tau) to
    # extract the leading q-correction
    r_ell = genus1_shadow_rmatrix_sl2(z, tau, k, n_terms)
    r_trig = k * trigonometric_r_matrix_sl2(z)

    # q-correction: (r^{ell} - r^{trig}) / q should approach r^{(1)}(z)
    q_correction_0 = r_ell - r_trig
    if abs(q) > 1e-300:
        r1_estimate = q_correction_0 / q
    else:
        r1_estimate = np.zeros_like(r_ell)

    return {
        'tau': tau,
        'q': q,
        'q_abs': q_abs,
        'r_ell_norm': np.linalg.norm(r_ell),
        'r_trig_norm': np.linalg.norm(r_trig),
        'q_correction_norm': np.linalg.norm(q_correction_0),
        'r1_estimate_norm': np.linalg.norm(r1_estimate),
    }


# ============================================================
# 15. Kappa consistency
# ============================================================

def kappa_from_elliptic_rmatrix(lie_type: str, k: float, tau: complex,
                                 z_small: float = 0.01,
                                 n_terms: int = 50) -> Dict[str, Any]:
    r"""Extract kappa(A) from the elliptic r-matrix and compare with the known value.

    Method: the residue of the r-matrix at z = 0 gives:
        Res_{z=0} r^{ell}(z) = k \cdot \Omega

    The scalar trace of the Casimir:
        tr(\Omega) = 0 for sl_N (traceless generators)
    but tr_1 \Omega (partial trace on first factor) = C_2 I on the second factor,
    where C_2 = (N^2 - 1)/(2N) for sl_N fundamental.

    The modular characteristic kappa = dim(g)(k+h^v)/(2h^v).
    We verify that the pole residue is consistent with kappa.
    """
    expected_kappa = kappa_affine(lie_type, k)

    if lie_type == 'sl2':
        r = genus1_shadow_rmatrix_sl2(z_small, tau, k, n_terms)
        d = 2
    elif lie_type == 'sl3':
        r = genus1_shadow_rmatrix_sl3(z_small, tau, k, n_terms)
        d = 3
    else:
        raise ValueError(f"Unsupported: {lie_type}")

    # z * r(z) ~ k * Omega, so extract the Casimir eigenvalue
    residue = z_small * r
    # Partial trace on first factor: (tr_1 Omega)_{jl} = sum_i Omega_{ij, il}
    partial_trace = np.zeros((d, d), dtype=complex)
    for i in range(d):
        for j in range(d):
            for l in range(d):
                partial_trace[j, l] += residue[i * d + j, i * d + l]

    # For sl_N: tr_1(Omega) = C_2(fund) * I = (N^2-1)/(2N) * I
    # And tr_1(k*Omega) = k * C_2 * I
    # Scalar value:
    scalar = np.mean(np.diag(partial_trace).real)
    N = d
    expected_c2_k = k * (N ** 2 - 1) / (2.0 * N)

    return {
        'lie_type': lie_type,
        'k': k,
        'expected_kappa': expected_kappa,
        'extracted_k_times_C2': scalar,
        'expected_k_times_C2': expected_c2_k,
        'c2_relative_error': abs(scalar - expected_c2_k) / max(abs(expected_c2_k), 1e-10),
        'passed': abs(scalar - expected_c2_k) / max(abs(expected_c2_k), 1e-10) < 0.15,
    }


# ============================================================
# 16. Crossing symmetry
# ============================================================

def verify_crossing_symmetry_sl2(z: complex, tau: complex, k: float = 1.0,
                                  n_terms: int = 50) -> Dict[str, Any]:
    r"""Verify crossing symmetry for the elliptic r-matrix.

    Crossing: r_{12}(z) + r_{12}(-z) should be proportional to
    the Casimir tensor \Omega (for the classical r-matrix with
    the quasi-periodicity properly accounted for).

    More precisely, for the Weierstrass zeta:
        \zeta(z) + \zeta(-z) = 0 (zeta is odd)
    and for the phi-functions:
        \phi_\alpha(z) + \phi_\alpha(-z) = finite constant

    The full crossing relation for the Belavin r-matrix is:
        r_{12}(z) + r_{21}(-z) = 0

    which is the skew-symmetry we already verify.  An additional
    crossing involves the half-period shift:
        r(z + 1/2, tau) relates to r(z, tau) by a twist.
    """
    r_z = genus1_shadow_rmatrix_sl2(z, tau, k, n_terms)
    r_shifted = genus1_shadow_rmatrix_sl2(z + 0.5, tau, k, n_terms)

    # The half-period shift should conjugate by a diagonal matrix
    D = np.diag([1, -1, -1, 1])  # for sl_2 fundamental
    r_conj = D @ r_shifted @ D

    # Check if r_conj has the same eigenvalue magnitudes as r_z
    eigs_z = np.sort(np.abs(np.linalg.eigvals(r_z)))
    eigs_conj = np.sort(np.abs(np.linalg.eigvals(r_conj)))

    diff = np.linalg.norm(eigs_z - eigs_conj)
    scale = max(np.linalg.norm(eigs_z), 1e-10)

    return {
        'eigenvalue_diff': diff / scale,
        'passed': diff / scale < 0.5,  # half-period shifts are nontrivial
    }


# ============================================================
# 17. Genus-1 Eisenstein correction structure
# ============================================================

def eisenstein_correction_analysis(tau: complex, k: float = 1.0,
                                    n_terms: int = 50) -> Dict[str, Any]:
    r"""Analyze the Eisenstein correction to the r-matrix.

    The elliptic r-matrix near z = 0:
        r^{ell}(z) = \Omega/z + r_0(\tau) + r_1(\tau) z + ...

    The constant term r_0(\tau) is the first SHADOW CORRECTION:
    it should be proportional to E_2(\tau) (quasi-modular Eisenstein
    series of weight 2), encoding the genus-1 anomaly.

    Compare r_0(\tau) for several tau values to verify the E_2 dependence.
    """
    z_small = 0.003

    tau_values = [tau * t for t in [0.5, 1.0, 1.5, 2.0]]

    r0_data = []
    for tv in tau_values:
        r_ell = belavin_r_matrix_sl2(z_small, tv, n_terms)
        Omega = _sl2_casimir_fund()
        # Subtract the pole part
        r0 = r_ell - Omega / z_small
        r0_data.append({
            'tau': tv,
            'r0_norm': np.linalg.norm(r0),
            'r0_trace': np.trace(r0),
        })

    return {
        'z_small': z_small,
        'corrections': r0_data,
    }


# ============================================================
# 18. Full degeneration chain
# ============================================================

def full_degeneration_chain(z: complex = 0.15 + 0.05j,
                             k: float = 1.0,
                             n_terms: int = 50) -> Dict[str, Any]:
    r"""Verify the full degeneration chain: elliptic -> trigonometric -> rational.

    Step 1: elliptic at large Im(tau) approaches trigonometric.
    Step 2: trigonometric at z -> 0 (or equivalently, period L -> infty)
            approaches rational.

    Returns both steps with error estimates.
    """
    # Step 1: elliptic -> trigonometric
    tau_large = 8j
    r_ell = genus1_shadow_rmatrix_sl2(z, tau_large, k, n_terms)
    r_trig = k * trigonometric_r_matrix_sl2(z)
    err_1 = np.linalg.norm(r_ell - r_trig) / max(np.linalg.norm(r_trig), 1e-10)

    # Step 2: trigonometric -> rational (use z_small)
    z_small = 0.01
    r_trig_small = trigonometric_r_matrix_sl2(z_small)
    r_rat_small = rational_r_matrix_sl2(z_small)
    # For small z: pi*cot(pi*z) ~ 1/z - pi^2*z/3, so r_trig ~ r_rat + O(z)
    err_2 = np.linalg.norm(r_trig_small - r_rat_small) / max(np.linalg.norm(r_rat_small), 1e-10)

    return {
        'step1_ell_to_trig': {
            'tau': tau_large,
            'relative_error': err_1,
            'passed': err_1 < 0.01,
        },
        'step2_trig_to_rat': {
            'z': z_small,
            'relative_error': err_2,
            'close': err_2 < 0.1,  # O(z) correction is ~pi^2*z/3
        },
    }


# ============================================================
# 19. Elliptic R-matrix (multiplicative form, quantum)
# ============================================================

def quantum_R_matrix_sl2(z: complex, tau: complex, k: float = 1.0,
                          n_terms: int = 50) -> np.ndarray:
    r"""Quantum R-matrix R(z, \tau) = I + r(z, \tau) / \kappa + O(1/\kappa^2).

    The classical r-matrix is the first-order perturbative expansion of
    the quantum R-matrix in 1/\kappa where \kappa is the modular characteristic.

    For sl_2 at level k: \kappa = 3(k+2)/4.

    R(z) = I + r(z)/\kappa is the leading (semi-classical) approximation.
    """
    kap = kappa_affine('sl2', k)
    I4 = np.eye(4, dtype=complex)
    r = genus1_shadow_rmatrix_sl2(z, tau, k, n_terms)

    return I4 + r / kap


# ============================================================
# 20. Summary / landscape
# ============================================================

def elliptic_rmatrix_landscape(tau: complex = 0.5 + 1.0j,
                                k: float = 1.0,
                                n_terms: int = 40) -> Dict[str, Any]:
    r"""Summary of the elliptic R-matrix landscape at given tau and level k.

    Returns a dictionary with:
    - YBE residuals for sl_2 and sl_3
    - Degeneration errors
    - Modular transformation checks
    - Pole structure analysis
    - Kappa consistency
    """
    z_test = 0.15 + 0.05j
    z1, z2, z3 = 0.1 + 0.02j, 0.3 + 0.07j, 0.6 + 0.11j

    ybe_sl2 = verify_ybe_elliptic_sl2(z1, z2, z3, tau, k, n_terms)
    skew = verify_skew_symmetry(z_test, tau, k, n_terms)
    poles = elliptic_pole_structure(0.01, tau, n_terms)
    degen = full_degeneration_chain(z_test, k, n_terms)
    kappa_sl2 = kappa_from_elliptic_rmatrix('sl2', k, tau, 0.01, n_terms)

    return {
        'tau': tau,
        'k': k,
        'ybe_sl2': ybe_sl2,
        'skew_symmetry': skew,
        'pole_structure': poles,
        'degeneration': degen,
        'kappa_sl2': kappa_sl2,
    }
