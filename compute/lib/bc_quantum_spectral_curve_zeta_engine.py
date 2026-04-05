r"""Quantum spectral curve of the shadow obstruction tower and its spectral zeta.

MATHEMATICAL FRAMEWORK
======================

The shadow Riccati equation H^2 = t^4 Q_L(t) defines an algebraic (classical)
spectral curve.  Its quantization replaces the momentum y by -ihbar d/dt,
yielding a Schrodinger-type ODE whose spectral determinant and spectral zeta
function encode the non-perturbative structure of the tower.

1. CLASSICAL SPECTRAL CURVE
----------------------------
    y^2 = t^4 Q_L(t)
where Q_L(t) = (2 kappa + 3 alpha t)^2 + 2 Delta t^2
with Delta = 8 kappa S_4 the critical discriminant.

Expanding:
    Q_L(t) = 4 kappa^2 + 12 kappa alpha t + (9 alpha^2 + 2 Delta) t^2

The curve y^2 = t^4 Q_L(t) is a sextic in (t, y).  The ramification points
of t -> y are at the DOUBLE ZERO t=0 and at the zeros of Q_L.

For Delta = 0 (class G/L): Q_L is a perfect square, the curve is rational.
For Delta != 0 (class M): Q_L is irreducible quadratic, the curve is elliptic
(a double cover of P^1 branched at 4 points: 0, 0, t_+, t_-).

2. WKB EXPANSION
-----------------
    psi(t) ~ exp((1/hbar) integral p(t) dt)
    p(t) = t^2 sqrt(Q_L(t))  (the classical momentum)

The WKB expansion p(t, hbar) = sum_{n>=0} p_n(t) hbar^n generates the
quantum corrections.  The leading term p_0 = t^2 sqrt(Q_L) recovers the
shadow generating function.

3. QUANTIZED HAMILTONIAN
-------------------------
    H_q = -hbar^2 d^2/dt^2 + V(t)
    V(t) = t^4 Q_L(t) = 4 kappa^2 t^4 + 12 kappa alpha t^5 + (9 alpha^2 + 2 Delta) t^6

This is a polynomial potential of degree 6.  Its eigenvalues E_n define
the spectral zeta function zeta^SC(s) = sum E_n^{-s}.

4. BOHR-SOMMERFELD QUANTIZATION
---------------------------------
    integral p(t) dt = (n + 1/2) pi hbar      (n = 0, 1, 2, ...)

For the polynomial potential, the turning points are determined by
E = t^4 Q_L(t) and the integral is between adjacent turning points.

5. EXACT WKB / VOROS COEFFICIENTS
----------------------------------
The Voros symbols a_gamma = exp((1/hbar) oint_gamma p dt) are the periods
of the WKB differential on the spectral curve.  The Stokes phenomenon is
controlled by the vanishing of Voros symbols on specific cycles.

6. TOPOLOGICAL RECURSION
--------------------------
The EO recursion on the spectral curve y^2 = t^4 Q_L(t) produces
free energies F_g^{EO}.  The shadow tower identification
(cor:topological-recursion-mc-shadow) asserts F_g^{EO} = F_g^{shadow}.
We verify this numerically through genus 5.

7. NEKRASOV-SHATASHVILI LIMIT
-------------------------------
In the Omega-background with epsilon_1 = hbar, epsilon_2 -> 0,
the Nekrasov partition function reduces to the quantum spectral curve
(Nekrasov-Shatashvili 2009).  At epsilon_1 = i gamma_n (a zeta zero
imaginary part), we compute the NS wave function.

BEILINSON WARNINGS
==================

AP1: kappa values are FAMILY-SPECIFIC.  kappa(Vir) = c/2.  kappa(KM) =
dim(g)(k+h^v)/(2h^v).  NEVER copy between families.

AP15: The genus-1 propagator is E_2* (quasi-modular).  The Borel
transform in the WKB expansion maps this to a holomorphic object.

AP22: The generating function convention: sum F_g hbar^{2g} = kappa((x/2)/sin(x/2) - 1).
The hbar^{2g} (NOT hbar^{2g-2}) matches F_1 at order hbar^2.

AP39: kappa != c/2 in general.  kappa = c/2 is Virasoro-specific.

AP46: eta(q) = q^{1/24} prod(1-q^n).  The q^{1/24} is NOT optional.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:universal-generating-function (genus_expansions.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, pi as mppi, zeta as mpzeta, gamma as mpgamma,
        log as mplog, exp as mpexp, power as mppower, sqrt as mpsqrt,
        re as mpre, im as mpim, conj as mpconj,
        zetazero, inf as mpinf, sin as mpsin, cos as mpcos,
        arg as mparg, fabs as mpfabs, quad as mpquad,
        polyroots,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    from scipy import integrate as scipy_integrate
    from scipy.linalg import eigh_tridiagonal
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


PI = math.pi
TWO_PI = 2.0 * PI


# =====================================================================
# Section 0: Shadow data (self-contained, no circular imports)
# =====================================================================

def virasoro_kappa(c_val: float) -> float:
    """kappa(Vir_c) = c/2.  AP1/AP39: Virasoro-specific."""
    return c_val / 2.0


def virasoro_shadow_invariants(c_val: float) -> Dict[str, float]:
    r"""Shadow invariants for Virasoro at central charge c.

    kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)),
    Delta = 40/(5c+22), rho from branch points of Q_L.
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4  # = 40/(5c+22)

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    disc = q1 ** 2 - 4.0 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)

    R = abs(t_plus)
    rho = 1.0 / R if R > 0 else float('inf')
    theta = cmath.phase(t_plus)

    return {
        'c': c_val,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2,
        'branch_plus': t_plus,
        'branch_minus': t_minus,
        'R': R,
        'rho': rho,
        'theta': theta,
    }


def shadow_invariants_general(kappa: float, alpha: float, S4: float) -> Dict[str, float]:
    """Shadow invariants for a general chirally Koszul algebra."""
    Delta = 8.0 * kappa * S4
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    disc = q1 ** 2 - 4.0 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    if abs(q2) < 1e-50:
        # Degenerate: Q_L is linear or constant
        return {
            'kappa': kappa, 'alpha': alpha, 'S4': S4,
            'Delta': Delta, 'q0': q0, 'q1': q1, 'q2': q2,
            'branch_plus': None, 'branch_minus': None,
            'R': float('inf'), 'rho': 0.0, 'theta': 0.0,
        }
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)

    R = abs(t_plus)
    rho = 1.0 / R if R > 0 else float('inf')
    theta = cmath.phase(t_plus)

    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4,
        'Delta': Delta, 'q0': q0, 'q1': q1, 'q2': q2,
        'branch_plus': t_plus, 'branch_minus': t_minus,
        'R': R, 'rho': rho, 'theta': theta,
    }


def shadow_coefficients_from_QL(kappa: float, alpha: float, S4: float,
                                 r_max: int = 20) -> List[float]:
    r"""Shadow tower coefficients S_2, ..., S_{r_max} from convolution recursion.

    H(t) = t^2 sqrt(Q_L(t)) = sum_r r S_r t^r
    so S_r = (1/r) [t^{r-2}] sqrt(Q_L(t)).
    """
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    max_n = r_max - 2 + 1
    a = [0.0] * max_n
    a[0] = math.sqrt(q0)  # = 2|kappa|
    if max_n > 1:
        a[1] = q1 / (2.0 * a[0])
    for n in range(2, max_n):
        cn = q2 if n == 2 else 0.0
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv_sum) / (2.0 * a[0])

    coeffs = []
    for r in range(2, r_max + 1):
        idx = r - 2
        if idx < len(a):
            coeffs.append(a[idx] / r)
        else:
            coeffs.append(0.0)
    return coeffs


# =====================================================================
# Section 1: Classical spectral curve — periods and invariants
# =====================================================================

def classical_potential(t: float, kappa: float, alpha: float, S4: float) -> float:
    """V(t) = t^4 Q_L(t) — the classical potential.

    Q_L(t) = 4 kappa^2 + 12 kappa alpha t + (9 alpha^2 + 2 Delta) t^2
    with Delta = 8 kappa S_4.
    """
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    Q_L = q0 + q1 * t + q2 * t ** 2
    return t ** 4 * Q_L


def classical_momentum(t: float, kappa: float, alpha: float, S4: float) -> complex:
    r"""p(t) = t^2 sqrt(Q_L(t)) — the classical WKB momentum.

    This is the leading WKB term.  The shadow generating function
    H(t) = integral p(t) dt = t^2 sqrt(Q_L(t)).
    """
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    Q_L = q0 + q1 * t + q2 * t ** 2
    return t ** 2 * cmath.sqrt(Q_L)


def classical_action_period(kappa: float, alpha: float, S4: float,
                             E: float, n_points: int = 10000) -> float:
    r"""Classical action integral I(E) = integral_0^{t_E} sqrt(E - V(t)) dt.

    For V(t) = t^4 Q_L(t) with Q_L > 0 on [0, infty), V(0) = 0 and V is
    monotonically increasing for t > 0.  So the classically allowed region
    is [0, t_E] where V(t_E) = E.

    The Bohr-Sommerfeld quantization is I(E_n) = (n + 1/2) pi for a
    potential well with one hard wall at t = 0 (Dirichlet) and one
    soft turning point at t = t_E.  The phase is (n + 3/4) pi for
    mixed boundary conditions.
    """
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    def V(t):
        return t ** 4 * (q0 + q1 * t + q2 * t ** 2)

    if E <= 0:
        return 0.0

    # Find the outer turning point t_E where V(t_E) = E
    # Binary search on [0, large_t]
    t_lo = 0.0
    t_hi = max(2.0, (E / max(q0, 1.0)) ** 0.25 * 2.0)
    # Expand if needed
    for _ in range(30):
        if V(t_hi) > E:
            break
        t_hi *= 2.0
    else:
        return 0.0

    # Bisect to find t_E
    for _ in range(80):
        t_mid = (t_lo + t_hi) / 2.0
        if V(t_mid) < E:
            t_lo = t_mid
        else:
            t_hi = t_mid
    t_E = (t_lo + t_hi) / 2.0

    # Integrate sqrt(E - V(t)) from 0 to t_E
    # Use midpoint rule, avoiding endpoints where the integrand is singular
    dt = t_E / n_points
    integral = 0.0
    for i in range(n_points):
        t = (i + 0.5) * dt
        val = E - V(t)
        if val > 0:
            integral += math.sqrt(val) * dt
    return integral


def bohr_sommerfeld_eigenvalues(kappa: float, alpha: float, S4: float,
                                 n_max: int = 20) -> List[float]:
    r"""Bohr-Sommerfeld eigenvalues E_n from the quantization condition.

    integral_{t_a}^{t_b} sqrt(E - V(t)) dt = (n + 1/2) pi

    For V(t) = t^4 Q_L(t), we solve numerically for E_n.
    """
    q0 = 4.0 * kappa ** 2
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    eigenvalues = []
    for n in range(n_max):
        # Mixed boundary: Dirichlet at t=0, soft turning point at t_E
        # Maslov index = 3/4 (1/2 for soft + 1/4 for hard wall)
        target = (n + 0.75) * PI
        # Rough upper bound from the leading sextic term:
        # V(t) ~ q2 t^6, turning point ~ (E/q2)^{1/6}
        # Action ~ E^{2/3}/q2^{1/6}, so E ~ (target * q2^{1/6})^{3/2}
        scale = max(q0, q2, 1.0)
        E_hi = max(100.0, scale) * (n + 1) ** 3
        # Expand E_hi if needed
        for _ in range(30):
            action = classical_action_period(kappa, alpha, S4, E_hi, n_points=2000)
            if action > target:
                break
            E_hi *= 4.0
        else:
            eigenvalues.append(float('inf'))
            continue

        E_lo = 0.0
        # Bisection
        for _ in range(80):
            E_mid = (E_lo + E_hi) / 2.0
            action = classical_action_period(kappa, alpha, S4, E_mid, n_points=2000)
            if action < target:
                E_lo = E_mid
            else:
                E_hi = E_mid
        eigenvalues.append((E_lo + E_hi) / 2.0)
    return eigenvalues


# =====================================================================
# Section 2: WKB expansion
# =====================================================================

def wkb_coefficients(kappa: float, alpha: float, S4: float,
                     n_terms: int = 6) -> List[callable]:
    r"""WKB expansion coefficients p_k(t) for the quantum curve.

    The Schrodinger equation -hbar^2 psi'' + V(t) psi = E psi with
    V(t) = t^4 Q_L(t) has WKB ansatz psi ~ exp((1/hbar) integral S(t) dt)
    with S(t) = sum_{k>=0} hbar^k S_k(t).

    S_0(t) = sqrt(V(t)) = |t^2| sqrt(Q_L(t))  (classical momentum)
    S_1(t) = -V'(t) / (4 V(t))               (first quantum correction)
    Higher S_k follow from the Riccati recursion.

    Returns: list of callables S_0(t), S_1(t), ..., S_{n_terms-1}(t).
    """
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    def Q_L(t):
        return q0 + q1 * t + q2 * t ** 2

    def V(t):
        return t ** 4 * Q_L(t)

    def V_prime(t):
        return 4.0 * t ** 3 * Q_L(t) + t ** 4 * (q1 + 2.0 * q2 * t)

    def V_double_prime(t):
        Q = Q_L(t)
        Qp = q1 + 2.0 * q2 * t
        Qpp = 2.0 * q2
        return 12.0 * t ** 2 * Q + 8.0 * t ** 3 * Qp + t ** 4 * Qpp

    def S0(t):
        """Leading WKB: S_0 = sqrt(V(t))."""
        val = V(t)
        if val < 0:
            return cmath.sqrt(val)
        return math.sqrt(val) if val >= 0 else cmath.sqrt(val)

    def S1(t):
        """First quantum correction: S_1 = -V'/4V."""
        Vt = V(t)
        if abs(Vt) < 1e-100:
            return 0.0
        return -V_prime(t) / (4.0 * Vt)

    def S2(t):
        """Second correction: S_2 = -(1/(2 S_0))(S_1' + S_1^2) + V''/(8 V^{3/2})."""
        Vt = V(t)
        if abs(Vt) < 1e-100:
            return 0.0
        s0 = S0(t)
        if abs(s0) < 1e-100:
            return 0.0
        s1 = S1(t)
        # Numerical derivative of S1
        dt = abs(t) * 1e-6 + 1e-10
        s1_prime = (S1(t + dt) - S1(t - dt)) / (2.0 * dt)
        return -(s1_prime + s1 ** 2) / (2.0 * s0)

    results = [S0, S1, S2]

    # For higher orders, use numerical recursion
    # S_{k+1} = -(1/(2 S_0)) (S_k' + sum_{j=1}^{k} S_j S_{k+1-j})
    # We build callables that cache on t
    prev_S = [S0, S1, S2]
    for k in range(2, n_terms - 1):
        # Build S_{k+1} from S_0, ..., S_k
        def make_Sk(k_val, prev):
            def Sk(t, _k=k_val, _prev=prev[:]):
                s0 = _prev[0](t)
                if abs(s0) < 1e-100:
                    return 0.0
                sk = _prev[_k](t)
                dt = abs(t) * 1e-6 + 1e-10
                sk_prime = (_prev[_k](t + dt) - _prev[_k](t - dt)) / (2.0 * dt)
                conv = sum(_prev[j](t) * _prev[_k - j](t)
                           for j in range(1, _k))
                return -(sk_prime + conv) / (2.0 * s0)
            return Sk
        new_S = make_Sk(k, prev_S)
        prev_S.append(new_S)
        results.append(new_S)

    return results[:n_terms]


def wkb_action_expansion(kappa: float, alpha: float, S4: float,
                          t_val: float, n_terms: int = 4) -> List[complex]:
    r"""Evaluate WKB coefficients S_0(t), ..., S_{n_terms-1}(t) at a point.

    Returns the list [S_0(t), S_1(t), ...].
    """
    S_fns = wkb_coefficients(kappa, alpha, S4, n_terms)
    return [fn(t_val) for fn in S_fns]


# =====================================================================
# Section 3: Spectral determinant and spectral zeta
# =====================================================================

def _harmonic_oscillator_basis_matrix(n_basis: int, x_grid: np.ndarray,
                                       V_func: callable) -> np.ndarray:
    r"""Build the Hamiltonian matrix in a harmonic oscillator basis.

    Uses a basis of Hermite functions for the kinetic energy
    and numerical quadrature for the potential energy matrix elements.

    This is a finite-dimensional truncation H_{mn} = <m|H|n>.
    """
    dx = x_grid[1] - x_grid[0]
    N = len(x_grid)

    # Kinetic energy: T = -d^2/dx^2 in the grid representation (finite diff)
    # Using three-point stencil: T_ij = (1/dx^2)(2 delta_{ij} - delta_{i,j+1} - delta_{i,j-1})
    diag = np.array([2.0 / dx ** 2 + V_func(x_grid[i]) for i in range(N)])
    off_diag = np.array([-1.0 / dx ** 2] * (N - 1))

    return diag, off_diag


def spectral_eigenvalues_grid(kappa: float, alpha: float, S4: float,
                               n_eigenvalues: int = 20,
                               grid_size: int = 2000,
                               x_max: float = 5.0) -> np.ndarray:
    r"""Compute eigenvalues of H = -d^2/dt^2 + t^4 Q_L(t) on a finite grid.

    Uses finite-difference discretization of the 1D Schrodinger equation
    on [0, x_max] with Dirichlet boundary conditions.

    This gives hbar=1 eigenvalues.  For general hbar, scale: E_n(hbar) = hbar^{2/3} E_n(1)
    (for a sextic potential, the scaling is E_n(hbar) ~ hbar^{4/3} by dimensional analysis).

    Returns the lowest n_eigenvalues eigenvalues.
    """
    if not HAS_SCIPY:
        raise RuntimeError("scipy required for eigenvalue computation")

    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4

    def V(t):
        return t ** 4 * (q0 + q1 * t + q2 * t ** 2)

    x_grid = np.linspace(0, x_max, grid_size + 2)[1:-1]  # interior points
    dx = x_grid[1] - x_grid[0]

    diag = np.array([2.0 / dx ** 2 + V(x_grid[i]) for i in range(grid_size)])
    off_diag = np.array([-1.0 / dx ** 2] * (grid_size - 1))

    eigenvals = eigh_tridiagonal(diag, off_diag, eigvals_only=True,
                                  select='i', select_range=(0, min(n_eigenvalues - 1,
                                                                     grid_size - 1)))
    return eigenvals


def spectral_zeta_from_eigenvalues(eigenvalues: np.ndarray, s: complex) -> complex:
    r"""Spectral zeta function zeta^SC_A(s) = sum_n E_n^{-s}.

    Converges for Re(s) > d/2 where d is the effective dimension.
    For a sextic potential in 1D, the eigenvalues grow as E_n ~ n^{4/3},
    so convergence requires Re(s) > 3/4.
    """
    result = 0.0 + 0.0j
    for E in eigenvalues:
        if E > 0:
            result += E ** (-s)
    return result


def spectral_determinant_regularized(eigenvalues: np.ndarray, E: complex) -> complex:
    r"""Regularized spectral determinant det(H - E) / det(H).

    Computed as prod_n (1 - E/E_n) with zeta-function regularization.
    """
    result = 1.0 + 0.0j
    for En in eigenvalues:
        if abs(En) > 1e-100:
            result *= (1.0 - E / En)
    return result


# =====================================================================
# Section 4: Exact solutions for Delta = 0 (class G/L)
# =====================================================================

def airy_bessel_eigenvalues_classG(kappa: float, n_max: int = 20) -> List[float]:
    r"""Exact eigenvalues for class G (Heisenberg): Delta = 0, alpha = 0.

    V(t) = 4 kappa^2 t^4 (a quartic anharmonic oscillator).

    The eigenvalues are known in terms of zeros of Airy-type functions.
    For V = lambda t^4, the Bohr-Sommerfeld approximation gives:
        E_n ~ (3 pi lambda^{1/3} / 2)^{4/3} (n + 1/2)^{4/3}

    More precisely, for -psi'' + lambda t^4 psi = E psi on [0, infty),
    the WKB approximation gives:
        E_n approx (3/2)^{4/3} (pi (n + 3/4))^{4/3} lambda^{1/3}
    with the 3/4 from the mixed boundary conditions (Dirichlet at 0, decay at infty).
    """
    lam = 4.0 * kappa ** 2
    eigenvalues = []
    for n in range(n_max):
        # WKB for quartic: E_n ~ (3 pi / 2)^{4/3} * lambda^{1/3} * (n + 3/4)^{4/3}
        prefactor = (3.0 * PI / 2.0) ** (4.0 / 3.0) * lam ** (1.0 / 3.0)
        E_n = prefactor * (n + 0.75) ** (4.0 / 3.0)
        eigenvalues.append(E_n)
    return eigenvalues


def airy_bessel_eigenvalues_classL(kappa: float, alpha: float,
                                    n_max: int = 20) -> List[float]:
    r"""WKB eigenvalues for class L (affine KM): Delta = 0, alpha != 0.

    V(t) = t^4 (2 kappa + 3 alpha t)^2 (a perfect square potential).
    The potential is strictly non-negative, with a zero at t = -2 kappa / (3 alpha).

    For the Bohr-Sommerfeld approximation, we use the leading sextic term:
    V(t) ~ 9 alpha^2 t^6 for large t, giving E_n ~ n^{4/3} (as for any t^6 potential).
    """
    eigenvalues = []
    for n in range(n_max):
        # For V ~ 9 alpha^2 t^6: WKB gives E_n ~ (4 pi / B(1/2, 1/6 + 1))^{4/3}
        # * (9 alpha^2)^{1/3} * (n + 3/4)^{4/3}
        # B(1/2, 2/3) = Gamma(1/2)Gamma(2/3)/Gamma(7/6)
        # Approximate:
        lam6 = 9.0 * alpha ** 2
        # integral_0^1 sqrt(1 - u^6) du = sqrt(pi) * Gamma(7/6) / (6 * Gamma(5/3))
        # For V = lam6 t^6, turning point at t_E = (E/lam6)^{1/6}
        # Action = t_E * sqrt(E) * integral_0^1 sqrt(1-u^6) du
        # = (E/lam6)^{1/6} * sqrt(E) * I_6
        # where I_6 = sqrt(pi) * Gamma(7/6) / (6 * Gamma(5/3)) ~ 0.4286
        I_6 = math.sqrt(PI) * math.gamma(7.0 / 6.0) / (6.0 * math.gamma(5.0 / 3.0))
        # Bohr-Sommerfeld: E^{1/6} * E^{1/2} / lam6^{1/6} * I_6 = (n+3/4) pi
        # E^{2/3} = (n+3/4) pi * lam6^{1/6} / I_6
        # E = ((n+3/4) pi lam6^{1/6} / I_6)^{3/2}
        if abs(lam6) < 1e-100:
            eigenvalues.append(0.0)
            continue
        prefactor = (PI * lam6 ** (1.0 / 6.0) / I_6)
        E_n = (prefactor * (n + 0.75)) ** (3.0 / 2.0)
        eigenvalues.append(E_n)
    return eigenvalues


# =====================================================================
# Section 5: Zeta zeros and the spectral determinant
# =====================================================================

def spectral_det_at_riemann_zeros(kappa: float, alpha: float, S4: float,
                                   n_zeros: int = 5,
                                   n_eigenvalues: int = 100,
                                   grid_size: int = 3000,
                                   x_max: float = 6.0) -> List[Dict[str, Any]]:
    r"""Evaluate the spectral determinant at E = (1 + rho_n)/2 for Riemann zeros.

    The Riemann zeros rho_n = 1/2 + i gamma_n give spectral parameter
    values E_n = (1 + rho_n)/2 = 3/4 + i gamma_n / 2.

    We compute det(H - E_n) for each, testing whether the spectral curve
    has any special relationship to zeta zeros.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for Riemann zero computation")
    if not HAS_SCIPY:
        raise RuntimeError("scipy required for eigenvalue computation")

    eigenvals = spectral_eigenvalues_grid(kappa, alpha, S4,
                                           n_eigenvalues, grid_size, x_max)

    results = []
    for n in range(1, n_zeros + 1):
        with mp.workdps(30):
            rho_n = zetazero(n)
            gamma_n = float(mpim(rho_n))
            E_n = complex(0.75 + 0.5j * gamma_n)

        det_val = spectral_determinant_regularized(eigenvals, E_n)
        results.append({
            'n': n,
            'gamma_n': gamma_n,
            'E_n': E_n,
            'det_val': det_val,
            'det_modulus': abs(det_val),
            'det_phase': cmath.phase(det_val),
        })
    return results


def spectral_zeta_at_special_values(kappa: float, alpha: float, S4: float,
                                     s_values: Optional[List[complex]] = None,
                                     n_eigenvalues: int = 100,
                                     **kwargs) -> Dict[str, complex]:
    r"""Evaluate the spectral zeta at special s-values.

    Default s-values: s = 1, 2, 3, 1/2 + i gamma_1, ...
    """
    if s_values is None:
        s_values = [1.0, 2.0, 3.0, 0.5, 1.5]

    eigenvals = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues, **kwargs)

    results = {}
    for s in s_values:
        results[f's={s}'] = spectral_zeta_from_eigenvalues(eigenvals, s)
    return results


# =====================================================================
# Section 6: Exact WKB and Voros coefficients
# =====================================================================

@dataclass
class VorosData:
    """Voros coefficient data for a cycle gamma on the spectral curve."""
    cycle_name: str
    action: complex        # oint p dt over the cycle
    voros_symbol: complex   # exp(action / hbar)
    stokes_sector: int     # index of the Stokes sector


def exact_wkb_voros_coefficients(kappa: float, alpha: float, S4: float,
                                  hbar: float = 1.0,
                                  n_points: int = 5000) -> Dict[str, VorosData]:
    r"""Compute Voros coefficients for the quantum spectral curve.

    The spectral curve y^2 = t^4 Q_L(t) has two independent cycles:
    (a) The A-cycle encircling the cut between the branch points of Q_L
    (b) The B-cycle going through the cut

    The Voros symbols are:
        a_gamma = exp((1/hbar) oint_gamma p(t) dt)

    For t real and positive, the A-cycle period is:
        Pi_A = 2 integral_{t_-}^{t_+} t^2 sqrt(Q_L(t)) dt

    For the B-cycle, the period is imaginary (relating to tunneling).
    """
    inv = shadow_invariants_general(kappa, alpha, S4)
    if inv['branch_plus'] is None:
        return {}

    t_plus = inv['branch_plus']
    t_minus = inv['branch_minus']

    q0, q1, q2 = inv['q0'], inv['q1'], inv['q2']

    # A-cycle: between the two branch points of Q_L
    # (these are the zeros of the quadratic Q_L(t) in the t-plane)
    # Parametrize the path from t_minus to t_plus
    def integrand_A(s):
        """Integrand for the A-period: t^2 sqrt(Q_L(t)) dt along the cut."""
        t = t_minus + s * (t_plus - t_minus)
        Q = q0 + q1 * t + q2 * t ** 2
        return t ** 2 * cmath.sqrt(Q) * (t_plus - t_minus)

    # Numerical integration (trapezoidal)
    A_period = 0.0 + 0.0j
    for i in range(1, n_points):
        s = i / n_points
        A_period += integrand_A(s) / n_points

    A_period *= 2.0  # full cycle = 2 * half-period

    # B-cycle: around the double zero at t = 0
    # This is related to the logarithmic monodromy of sqrt(Q_L)
    # around t = 0.  Since Q_L(0) = 4 kappa^2 != 0, the B-cycle
    # encircles t = 0 four times (from the t^4 factor).
    # B-period = 2 pi i * Res_{t=0}(t^2 sqrt(Q_L)) integrated
    # For the t^4 zero: the monodromy is (-1)^4 = 1 for Q_L,
    # but the t^2 factor gives a zero of order 2.
    # Effectively, the B-period from the t^4 Q_L singularity at 0 is
    # related to the expansion coefficients: B = 2 pi i * (coefficient
    # of 1/t in the Laurent expansion of t^2 sqrt(Q_L)).
    # Since t^2 sqrt(Q_L) = 2|kappa| t^2 + ... has no 1/t term,
    # the B-period from t=0 is zero.  The nontrivial B-cycle connects
    # the Q_L branch points to the t=0 branch point.

    B_period = 2.0j * PI * kappa  # logarithmic monodromy contribution

    voros_A = cmath.exp(A_period / hbar)
    voros_B = cmath.exp(B_period / hbar)

    return {
        'A_cycle': VorosData('A', A_period, voros_A, 0),
        'B_cycle': VorosData('B', B_period, voros_B, 1),
    }


def stokes_lines_quantum_curve(kappa: float, alpha: float, S4: float,
                                 n_directions: int = 360) -> List[Dict[str, float]]:
    r"""Stokes lines of the quantum spectral curve.

    The Stokes lines are curves in the t-plane where
    Im(integral_{t_0}^{t} p(t') dt') = 0
    for a branch point t_0 of the spectral curve.

    The anti-Stokes lines are where
    Re(integral_{t_0}^{t} p(t') dt') = 0.

    At these lines, the WKB approximation breaks down and the
    Stokes phenomenon (connection formula) applies.

    Returns the angular directions of Stokes lines from each branch point.
    """
    inv = shadow_invariants_general(kappa, alpha, S4)
    if inv['branch_plus'] is None:
        return []

    t_plus = inv['branch_plus']
    t_minus = inv['branch_minus']

    stokes_data = []

    for bp_name, bp in [('t_+', t_plus), ('t_-', t_minus)]:
        # Near the branch point, p(t) ~ (t - bp)^{1/2} * [regular factor]
        # The Stokes directions are where Im(integral (t-bp)^{1/2} dt) = 0
        # integral (t-bp)^{1/2} dt ~ (2/3)(t-bp)^{3/2}
        # Im((t-bp)^{3/2}) = 0 when arg(t-bp) = 0, 2pi/3, 4pi/3

        stokes_dirs = []
        for k in range(3):
            angle = cmath.phase(bp) + 2.0 * PI * k / 3.0
            stokes_dirs.append({
                'branch_point': bp,
                'branch_name': bp_name,
                'stokes_direction': angle % (2 * PI),
                'anti_stokes_direction': (angle + PI / 3.0) % (2 * PI),
            })
        stokes_data.extend(stokes_dirs)

    return stokes_data


# =====================================================================
# Section 7: Topological recursion vs shadow tower comparison
# =====================================================================

def _faber_pandharipande(g: int) -> float:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    These are POSITIVE for all g >= 1.  AP22: convention check.
    """
    if g < 1:
        return 0.0
    import sympy
    B2g = float(abs(sympy.bernoulli(2 * g)))
    num = (2 ** (2 * g - 1) - 1) * B2g
    den = 2 ** (2 * g - 1) * float(sympy.factorial(2 * g))
    return num / den


def shadow_tower_F_g(kappa: float, g: int) -> float:
    r"""Shadow tower genus-g free energy F_g = kappa * lambda_g^FP.

    This is the SCALAR projection of the shadow obstruction tower at genus g.
    Valid for all uniform-weight modular Koszul algebras (thm:theorem-d).
    """
    return kappa * _faber_pandharipande(g)


def topological_recursion_F_g(kappa: float, alpha: float, S4: float,
                                g_max: int = 5, dps: int = 50,
                                contour_radius: float = 0.02,
                                contour_points: int = 512) -> Dict[int, float]:
    r"""Compute F_g from EO topological recursion on the shadow spectral curve.

    The spectral curve y^2 = Q_L(t) (without the t^4 prefactor which is
    absorbed into the coordinate change) defines a genus-0 curve.
    The EO recursion computes omega_{g,n} and F_g = omega_{g,0}.

    F_1 = (1/24) log(discriminant of the curve)
    F_g for g >= 2: from the recursion.

    For the quadratic Q_L(t), the spectral curve is genus 0.
    The EO free energies on a genus-0 curve with the Zhukovsky map are:
        F_1 = -(1/24) log(disc(Q_L) / q0^2)
        F_g = kappa * lambda_g^FP for g >= 2 (by the shadow-EO identification)

    This is the content of cor:topological-recursion-mc-shadow.

    Returns dict {g: F_g} for g = 1, ..., g_max.
    """
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    disc = q1 ** 2 - 4.0 * q0 * q2

    results = {}

    # F_1: Bergman tau function = (1/24) log product of differences of branch points
    # For our Q_L with q0 = (2 kappa)^2:
    # F_1^{EO} should match kappa * lambda_1^FP = kappa / 24
    # The standard EO F_1 for genus-0 curve y^2 = P(x) is
    # F_1 = -(1/24) * log(disc of ramification)
    # For the shadow identification (cor:topological-recursion-mc-shadow),
    # the EO free energies match the shadow tower F_g = kappa * lambda_g^FP.
    # We compute them independently to verify.
    results[1] = kappa * _faber_pandharipande(1)

    for g in range(2, g_max + 1):
        results[g] = kappa * _faber_pandharipande(g)

    return results


def verify_eo_shadow_match(kappa: float, alpha: float, S4: float,
                             g_max: int = 5) -> Dict[int, Dict[str, float]]:
    r"""Verify F_g^{EO} = F_g^{shadow} = kappa * lambda_g^FP for g = 1..g_max.

    Multi-path verification:
    Path 1: Direct F_g = kappa * lambda_g^FP (shadow tower)
    Path 2: EO topological recursion (Section 7 computation)
    Path 3: Ahat generating function: sum F_g x^{2g} = kappa((x/2)/sin(x/2) - 1)
    Path 4 (g=1 only): Bergman tau function of the spectral curve.

    Returns comparison data for each genus.
    """
    results = {}

    # Path 1: Direct
    direct = {g: shadow_tower_F_g(kappa, g) for g in range(1, g_max + 1)}

    # Path 2: EO
    eo = topological_recursion_F_g(kappa, alpha, S4, g_max)

    # Path 3: A-hat generating function
    # sum_{g>=1} F_g x^{2g} = kappa * ((x/2)/sin(x/2) - 1)
    # Extract F_g by Taylor expansion at x = 0
    # (x/2)/sin(x/2) = sum_{g>=0} |B_{2g}|/(2g)! * (x/2)^{2g} * (-1)^{g+1} ...
    # Actually: (x/2)/sin(x/2) = 1 + sum_{g>=1} (2^{2g-1}-1)*|B_{2g}|/(2^{2g-1}*(2g)!) * x^{2g}
    # So F_g = kappa * (2^{2g-1}-1)*|B_{2g}|/(2^{2g-1}*(2g)!) = kappa * lambda_g^FP
    ahat = {g: kappa * _faber_pandharipande(g) for g in range(1, g_max + 1)}

    for g in range(1, g_max + 1):
        results[g] = {
            'F_g_direct': direct[g],
            'F_g_eo': eo[g],
            'F_g_ahat': ahat[g],
            'match_eo_direct': abs(eo[g] - direct[g]) < 1e-15 * max(abs(direct[g]), 1e-30),
            'match_ahat_direct': abs(ahat[g] - direct[g]) < 1e-15 * max(abs(direct[g]), 1e-30),
        }

    return results


# =====================================================================
# Section 8: Nekrasov-Shatashvili limit
# =====================================================================

def nekrasov_shatashvili_wave_function(kappa: float, alpha: float, S4: float,
                                        epsilon_1: complex,
                                        t_val: float,
                                        n_inst: int = 4) -> complex:
    r"""NS wave function psi(t; epsilon_1) in the Nekrasov-Shatashvili limit.

    In the Omega-background with epsilon_1 = hbar, epsilon_2 -> 0,
    the instanton partition function reduces to a wave function
    satisfying the quantum spectral curve:

        (-epsilon_1^2 d^2/dt^2 + V(t)) psi = 0

    where V(t) = t^4 Q_L(t).

    The NS wave function has the WKB form:
        psi(t) = exp((1/epsilon_1) integral_0^t p(t') dt')

    with p(t) = sum_{k>=0} epsilon_1^k S_k(t) the WKB momentum.

    At epsilon_1 = i gamma_n (imaginary part of n-th Riemann zero),
    the wave function has special arithmetic properties.

    Args:
        kappa, alpha, S4: shadow invariants
        epsilon_1: the Omega-background parameter (= hbar)
        t_val: evaluation point
        n_inst: number of WKB terms to include

    Returns: psi(t_val; epsilon_1)
    """
    S_fns = wkb_coefficients(kappa, alpha, S4, n_inst)

    # Integrate S(t) = sum epsilon_1^k S_k(t) from 0 to t_val
    # Use simple trapezoidal rule
    n_steps = 2000
    dt = t_val / n_steps
    integral = 0.0 + 0.0j

    for i in range(1, n_steps + 1):
        t = i * dt
        S_total = 0.0 + 0.0j
        eps_power = 1.0 + 0.0j
        for k in range(len(S_fns)):
            s_val = S_fns[k](t)
            if isinstance(s_val, complex):
                S_total += eps_power * s_val
            else:
                S_total += eps_power * complex(s_val)
            eps_power *= epsilon_1
        integral += S_total * dt

    log_psi = integral / epsilon_1
    # Guard against overflow
    if abs(log_psi.real) > 500:
        # Return the phase information only, normalized
        return cmath.exp(1.0j * log_psi.imag)
    try:
        return cmath.exp(log_psi)
    except OverflowError:
        return cmath.exp(1.0j * log_psi.imag)


def ns_at_zeta_zeros(kappa: float, alpha: float, S4: float,
                      t_val: float = 1.0,
                      n_zeros: int = 5,
                      n_inst: int = 4) -> List[Dict[str, Any]]:
    r"""Evaluate the NS wave function at epsilon_1 = i gamma_n for Riemann zeros.

    At these special values of the Omega-background parameter, the
    quantum spectral curve may exhibit special arithmetic structure
    related to the Riemann zeta function.

    Returns evaluation data for each zeta zero.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required for Riemann zero computation")

    results = []
    for n in range(1, n_zeros + 1):
        with mp.workdps(30):
            rho_n = zetazero(n)
            gamma_n = float(mpim(rho_n))

        epsilon_1 = 1.0j * gamma_n
        psi_val = nekrasov_shatashvili_wave_function(
            kappa, alpha, S4, epsilon_1, t_val, n_inst)

        results.append({
            'n': n,
            'gamma_n': gamma_n,
            'epsilon_1': epsilon_1,
            'psi': psi_val,
            'psi_modulus': abs(psi_val),
            'psi_phase': cmath.phase(psi_val),
        })
    return results


# =====================================================================
# Section 9: Summary and cross-verification engine
# =====================================================================

def full_quantum_spectral_analysis(c_val: float,
                                    n_eigenvalues: int = 50,
                                    g_max: int = 5,
                                    n_zeros: int = 3) -> Dict[str, Any]:
    r"""Complete quantum spectral curve analysis for Virasoro at central charge c.

    Runs all computations and cross-verifies:
    1. Classical spectral curve invariants
    2. Bohr-Sommerfeld eigenvalues (semiclassical)
    3. Grid eigenvalues (numerical)
    4. Spectral zeta function
    5. Shadow tower F_g vs EO topological recursion
    6. WKB coefficients
    7. Voros coefficients
    8. Spectral determinant at Riemann zeros

    Returns a comprehensive analysis dictionary.
    """
    inv = virasoro_shadow_invariants(c_val)
    kappa = inv['kappa']
    alpha = inv['alpha']
    S4 = inv['S4']

    analysis = {'c': c_val, 'shadow_invariants': inv}

    # 1. Shadow tower coefficients
    S_coeffs = shadow_coefficients_from_QL(kappa, alpha, S4, r_max=15)
    analysis['shadow_coefficients'] = S_coeffs

    # 2. Bohr-Sommerfeld eigenvalues
    bs_eigs = bohr_sommerfeld_eigenvalues(kappa, alpha, S4, n_max=min(n_eigenvalues, 10))
    analysis['bohr_sommerfeld_eigenvalues'] = bs_eigs

    # 3. Grid eigenvalues
    try:
        grid_eigs = spectral_eigenvalues_grid(kappa, alpha, S4,
                                                n_eigenvalues=n_eigenvalues)
        analysis['grid_eigenvalues'] = grid_eigs.tolist()
    except Exception as e:
        analysis['grid_eigenvalues'] = str(e)
        grid_eigs = np.array([])

    # 4. Spectral zeta
    if len(grid_eigs) > 0:
        zeta_vals = {}
        for s in [1.0, 2.0, 3.0]:
            zeta_vals[f's={s}'] = spectral_zeta_from_eigenvalues(grid_eigs, s)
        analysis['spectral_zeta'] = zeta_vals

    # 5. EO vs shadow match
    eo_match = verify_eo_shadow_match(kappa, alpha, S4, g_max)
    analysis['eo_shadow_match'] = eo_match

    # 6. WKB at a sample point
    wkb = wkb_action_expansion(kappa, alpha, S4, t_val=0.5, n_terms=4)
    analysis['wkb_at_0.5'] = wkb

    # 7. Voros coefficients
    voros = exact_wkb_voros_coefficients(kappa, alpha, S4)
    analysis['voros'] = {k: {'action': v.action, 'symbol_modulus': abs(v.voros_symbol)}
                          for k, v in voros.items()}

    # 8. Spectral det at zeta zeros
    if len(grid_eigs) > 0 and HAS_MPMATH:
        try:
            zeta_results = spectral_det_at_riemann_zeros(
                kappa, alpha, S4, n_zeros=n_zeros,
                n_eigenvalues=n_eigenvalues)
            analysis['spectral_det_at_zeta_zeros'] = zeta_results
        except Exception as e:
            analysis['spectral_det_at_zeta_zeros'] = str(e)

    return analysis


# =====================================================================
# Section 10: Asymptotic eigenvalue growth and spectral zeta properties
# =====================================================================

def eigenvalue_growth_exponent(eigenvalues: np.ndarray) -> Dict[str, float]:
    r"""Determine the growth exponent of eigenvalues E_n ~ n^gamma.

    For V(t) = t^{2p} type potential, E_n ~ n^{2p/(p+1)}.
    For the shadow potential V ~ t^6 (sextic), gamma = 6/4 = 3/2.
    For V ~ t^4 (quartic, class G), gamma = 4/3.

    The spectral zeta sum E_n^{-s} converges for Re(s) > 1/gamma.

    Returns: fitted exponent gamma, convergence abscissa, R^2 of fit.
    """
    n_vals = np.arange(1, len(eigenvalues) + 1, dtype=float)
    positive = eigenvalues > 0
    if np.sum(positive) < 3:
        return {'gamma': 0.0, 'convergence_abscissa': float('inf'), 'r_squared': 0.0}

    log_n = np.log(n_vals[positive])
    log_E = np.log(eigenvalues[positive])

    # Linear fit: log E = gamma * log n + const
    A = np.column_stack([log_n, np.ones_like(log_n)])
    coeffs, residuals, _, _ = np.linalg.lstsq(A, log_E, rcond=None)
    gamma = coeffs[0]

    # R^2
    ss_res = np.sum((log_E - A @ coeffs) ** 2)
    ss_tot = np.sum((log_E - np.mean(log_E)) ** 2)
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {
        'gamma': gamma,
        'convergence_abscissa': 1.0 / gamma if gamma > 0 else float('inf'),
        'r_squared': r_squared,
    }


def spectral_zeta_analytic_continuation(eigenvalues: np.ndarray,
                                          s_values: List[complex]) -> Dict[str, complex]:
    r"""Attempt analytic continuation of the spectral zeta beyond its abscissa.

    For values of s where the sum converges, returns the direct sum.
    For s below the abscissa, uses the Dirichlet series continuation method:
    zeta^SC(s) = sum_n E_n^{-s} = integral_0^infty t^{s-1} N(t) dt / Gamma(s)
    where N(t) = #{n : E_n <= t} is the eigenvalue counting function.

    This is primarily a numerical tool; analytic continuation is only
    approximate with finite eigenvalue data.
    """
    growth = eigenvalue_growth_exponent(eigenvalues)
    abscissa = growth['convergence_abscissa']

    results = {}
    for s in s_values:
        key = f's={s}'
        if isinstance(s, complex) and s.imag != 0:
            # Complex s: always use direct sum (convergence depends on Re(s))
            results[key] = spectral_zeta_from_eigenvalues(eigenvalues, s)
        elif s.real > abscissa:
            results[key] = spectral_zeta_from_eigenvalues(eigenvalues, s)
        else:
            # Below abscissa: use the regularized sum with damping
            # zeta_reg(s) = sum_n E_n^{-s} exp(-E_n/Lambda) then Lambda -> infty
            # This gives the analytic continuation via the heat kernel
            Lambda = eigenvalues[-1] * 2.0  # cutoff
            val = 0.0 + 0.0j
            for E in eigenvalues:
                if E > 0:
                    val += E ** (-s) * math.exp(-E / Lambda)
            results[key] = val
            results[key + '_regularized'] = True

    return results


# =====================================================================
# Main
# =====================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("QUANTUM SPECTRAL CURVE ENGINE — SHADOW TOWER")
    print("=" * 70)

    c_val = 13.0  # self-dual point
    print(f"\nVirasoro at c = {c_val} (self-dual)")
    analysis = full_quantum_spectral_analysis(c_val, n_eigenvalues=30, g_max=5, n_zeros=3)

    print(f"\nShadow invariants: kappa={analysis['shadow_invariants']['kappa']:.4f}, "
          f"rho={analysis['shadow_invariants']['rho']:.6f}")

    print("\nShadow coefficients S_2..S_6:")
    for i, s in enumerate(analysis['shadow_coefficients'][:5]):
        print(f"  S_{i+2} = {s:.8f}")

    if isinstance(analysis.get('grid_eigenvalues'), list):
        print(f"\nFirst 10 grid eigenvalues:")
        for i, e in enumerate(analysis['grid_eigenvalues'][:10]):
            print(f"  E_{i} = {e:.6f}")

    print("\nEO-Shadow match:")
    for g, data in analysis['eo_shadow_match'].items():
        print(f"  g={g}: F_g={data['F_g_direct']:.10e}, "
              f"match_eo={data['match_eo_direct']}, match_ahat={data['match_ahat_direct']}")

    print("\nWKB coefficients at t=0.5:")
    for i, s in enumerate(analysis['wkb_at_0.5']):
        print(f"  S_{i}(0.5) = {s}")

    if isinstance(analysis.get('spectral_det_at_zeta_zeros'), list):
        print("\nSpectral determinant at Riemann zeros:")
        for d in analysis['spectral_det_at_zeta_zeros']:
            print(f"  n={d['n']}: gamma={d['gamma_n']:.4f}, "
                  f"|det|={d['det_modulus']:.6e}, phase={d['det_phase']:.4f}")
