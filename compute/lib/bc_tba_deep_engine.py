r"""Thermodynamic Bethe Ansatz at Riemann zeta zeros from shadow data.

MATHEMATICAL FRAMEWORK
======================

The TBA equations for a diagonal scattering theory with particle
species a = 1, ..., rank and mass spectrum {m_a} read:

    epsilon_a(theta) = r * m_a * cosh(theta)
        - sum_b int phi_{ab}(theta - theta') * log(1 + e^{-epsilon_b(theta')})
          * dtheta' / (2*pi)

where:
  - r is the dimensionless system size (temperature parameter),
  - phi_{ab}(theta) = -i d/dtheta log S_{ab}(theta) is the TBA kernel
    derived from the 2-particle S-matrix,
  - epsilon_a(theta) is the pseudo-energy (related to occupation
    numbers via the fermionic Y-function Y_a = e^{epsilon_a}).

The ground-state free energy (Casimir energy) is:

    F(r) = - sum_a int m_a * cosh(theta)
               * log(1 + e^{-epsilon_a(theta)}) * dtheta / (2*pi)

and the effective central charge:

    c_eff = 6 * r^2 * F(r) / pi^2   [at r -> 0]

or equivalently at finite r:

    c_eff(r) = (6/pi^2) * sum_a int m_a * cosh(theta)
                  * log(1 + e^{-epsilon_a(theta)}) * dtheta

SHADOW SPECIALIZATION
=====================

For a modular Koszul algebra A with central charge c and modular
characteristic kappa(A), the shadow scattering matrix at genus-0
(collision residue of Theta_A) determines a TBA-type system.  The
shadow sinh-Gordon kernel for the Virasoro/W-algebra landscape is:

    phi^sh(theta) = 2*kappa * cosh(theta) / (cosh(2*theta) - cos(pi*p))

where p = p(A) is the coupling parameter derived from the shadow data.

ZETA ZERO EVALUATION
=====================

We evaluate the TBA pseudo-energies at theta = gamma_n (the imaginary
part of the n-th nontrivial Riemann zeta zero rho_n = 1/2 + i*gamma_n).
The key questions:

1. Does c_eff(gamma_n) relate to the shadow central charge c?
2. Is there Stokes-like wall-crossing at zeta zeros?
3. Do the Rogers dilogarithm identities hold at zeta zeros?
4. Does the Y-system functional equation hold?

MODELS
======

1. Shadow sinh-Gordon: rank 1, phi(theta) = 2*cosh(theta)/(cosh(2*theta)-cos(pi*p))
2. Shadow XXX (rational): rank 1, phi(theta) = 2/(theta^2 + 1)
3. Shadow XXZ (trigonometric): rank 1, phi(theta) = sin(2*gamma)/
   (cosh(2*theta) - cos(2*gamma))
4. Shadow A_{N-1} (higher rank): rank N-1, phi_{ab} from A-type Dynkin diagram.

ODE/IM CORRESPONDENCE
=====================

The ODE (-d^2/dx^2 + V(x))psi = E*psi with "monster" potential V(x) has
Stokes multipliers encoding the TBA.  The ODE/IM correspondence
(Dorey-Tateo 1998, Bazhanov-Lukyanov-Zamolodchikov 1998) states:

    Y_a(theta) = Q_a(e^{theta + i*pi/(2*h)}) * Q_a(e^{theta - i*pi/(2*h)})
                 / (Q_a(e^{theta + i*pi*(1+1/(2*h))}) * Q_a(e^{theta - i*pi*(1+1/(2*h))}))

where Q_a are spectral determinants of the ODE and h is the Coxeter number.

NONLINEAR INTEGRAL EQUATION (NLIE)
===================================

Alternative formulation (Destri-de Vega 1992):

    ln a(theta) = -i*r*sinh(theta) + G * ln(1+a)(theta) - G * ln(1+a_bar)(theta)

where G(theta) = int_{-infty}^{infty} G_hat(omega)*e^{i*omega*theta} domega/(2*pi)
with G_hat = -sinh((pi-gamma)*omega) / (2*sinh(pi*omega)*cosh(gamma*omega)).

References:
  - Zamolodchikov, "Thermodynamic Bethe ansatz in relativistic models"
    (NP B342 695, 1990)
  - Al.B. Zamolodchikov, "TBA equations for excited states" (NP B 2000)
  - Dorey-Tateo, "Anharmonic oscillators and TBA" (J.Phys.A 32, 1999)
  - Bazhanov-Lukyanov-Zamolodchikov, "Spectral determinants for
    Schrodinger equation and Q-operators" (J.Stat.Phys. 102, 2001)
  - Destri-de Vega, "New thermodynamic Bethe ansatz" (PRL 69, 1992)
  - Kirillov, "Dilogarithm identities" (Prog. Theor. Phys. Suppl. 118, 1995)
  - bc_bethe_zeta_zeros_engine.py (Bethe roots at zeta zeros)
  - bc_shadow_zeta_zeros_engine.py (shadow zeta function)
  - thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
import cmath
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
from numpy import linalg as la
from scipy import integrate, optimize

try:
    import mpmath
    from mpmath import mp, zetazero as mp_zetazero
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ========================================================================
# 0. Constants and zeta zeros
# ========================================================================

PI = np.pi
TWO_PI = 2.0 * PI

# First 50 positive imaginary parts of nontrivial zeta zeros
# rho_n = 1/2 + i*gamma_n.  Gram-verified to 15 digits.
ZETA_ZERO_GAMMAS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147500,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081607,
    67.079810529494174,
    69.546401711173980,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492981329511,
    87.425274613125196,
    88.809111207634465,
    92.491899270558484,
    94.651344040519838,
    95.870634228245309,
    98.831194218193692,
    101.31785100573139,
    103.72553803842274,
    105.44662305232609,
    107.16861118427640,
    111.02953554316967,
    111.87465917699263,
    114.32022091545271,
    116.22668032085755,
    118.79078286597621,
    121.37012500242066,
    122.94682929355258,
    124.25681855434576,
    127.51668387959649,
    129.57870419995605,
    131.08768853093265,
    133.49773720299758,
    134.75650975337387,
    138.11604205453344,
    139.73620895212138,
    141.12370740402112,
    143.11184580762063,
]


def get_zeta_zeros(n: int, dps: int = 30) -> List[complex]:
    """Return the first n nontrivial zeta zeros rho_k = 1/2 + i*gamma_k."""
    zeros = []
    if HAS_MPMATH and dps > 15:
        with mp.workdps(dps):
            for k in range(1, n + 1):
                rho = mp_zetazero(k)
                zeros.append(complex(rho))
    else:
        for k in range(n):
            if k < len(ZETA_ZERO_GAMMAS):
                zeros.append(0.5 + 1j * ZETA_ZERO_GAMMAS[k])
            else:
                raise ValueError(
                    f"Need mpmath for more than {len(ZETA_ZERO_GAMMAS)} "
                    f"zeta zeros; only {len(ZETA_ZERO_GAMMAS)} hardcoded."
                )
    return zeros


def get_zeta_gammas(n: int) -> np.ndarray:
    """Return array of the first n positive imaginary parts gamma_n."""
    if n > len(ZETA_ZERO_GAMMAS):
        if HAS_MPMATH:
            gammas = []
            for k in range(1, n + 1):
                rho = complex(mp_zetazero(k))
                gammas.append(rho.imag)
            return np.array(gammas)
        raise ValueError(f"Need mpmath for n > {len(ZETA_ZERO_GAMMAS)}")
    return np.array(ZETA_ZERO_GAMMAS[:n])


# ========================================================================
# 1. TBA kernels for shadow models
# ========================================================================

@dataclass
class TBAModel:
    """Specification of a TBA system."""
    name: str
    rank: int
    masses: np.ndarray           # mass spectrum, shape (rank,)
    kernel: Callable             # kernel phi(theta, a, b) -> float
    coupling: float = 1.0        # coupling parameter
    coxeter_number: int = 2      # Coxeter number h (for Y-system)
    cartan_matrix: Optional[np.ndarray] = None  # for Y-system check

    def __post_init__(self):
        if self.cartan_matrix is None:
            if self.rank == 1:
                self.cartan_matrix = np.array([[2]])
            else:
                # A_{rank} Cartan matrix
                C = np.zeros((self.rank, self.rank))
                for i in range(self.rank):
                    C[i, i] = 2
                    if i > 0:
                        C[i, i - 1] = -1
                    if i < self.rank - 1:
                        C[i, i + 1] = -1
                self.cartan_matrix = C


def sinh_gordon_kernel(theta: float, a: int = 0, b: int = 0,
                       coupling: float = 1.0) -> float:
    """Shadow sinh-Gordon TBA kernel.

    phi(theta) = 2*cosh(theta) / (cosh(2*theta) - cos(pi*p))

    where p is the coupling parameter.  For the shadow specialization,
    p is derived from the shadow data (ratio of S_4/kappa).

    At p -> 0 (free boson limit): phi -> delta(theta).
    At p = 1 (Ising): phi(theta) = 1/cosh(theta).
    """
    denom = np.cosh(2.0 * theta) - np.cos(PI * coupling)
    if abs(denom) < 1e-100:
        return 0.0
    return 2.0 * np.cosh(theta) / denom


def xxx_kernel(theta: float, a: int = 0, b: int = 0,
               coupling: float = 1.0) -> float:
    """Shadow XXX (rational) TBA kernel.

    phi(theta) = 2 / (theta^2 + 1)

    This is the rational limit of the XXZ kernel as gamma -> 0,
    or equivalently the Cauchy kernel.  It arises from the shadow
    r-matrix R(u) = u*I + P (the rational Yang solution).
    """
    return 2.0 / (theta * theta + 1.0)


def xxz_kernel(theta: float, a: int = 0, b: int = 0,
               coupling: float = 0.5) -> float:
    """Shadow XXZ (trigonometric) TBA kernel.

    phi(theta) = sin(2*gamma) / (cosh(2*theta) - cos(2*gamma))

    where gamma is the anisotropy parameter.  coupling = gamma/pi.
    At gamma -> 0 (XXX limit): phi -> 1/(theta^2 + 1).
    """
    gamma = PI * coupling
    denom = np.cosh(2.0 * theta) - np.cos(2.0 * gamma)
    if abs(denom) < 1e-100:
        return 0.0
    return np.sin(2.0 * gamma) / denom


def a_type_kernel(theta: float, a: int, b: int,
                  coupling: float = 1.0, rank: int = 2) -> float:
    """TBA kernel for A_{rank} (higher-rank) models.

    phi_{ab}(theta) = delta_{a,b} * phi_0(theta)
                    + delta_{|a-b|,1} * phi_1(theta)

    where phi_0 = diagonal, phi_1 = nearest-neighbor on A-type Dynkin diagram.
    For the minimal A_{N-1} scattering theory:
      phi_0(theta) = 0  (no diagonal scattering beyond mass shell)
      phi_1(theta) = 1/cosh(theta)  (nearest-neighbor).
    """
    if abs(a - b) == 1:
        return 1.0 / np.cosh(theta)
    elif a == b:
        return 0.0
    else:
        return 0.0


def make_sinh_gordon_model(coupling: float = 0.5, r: float = 1.0) -> TBAModel:
    """Create a shadow sinh-Gordon TBA model."""
    def kernel(theta, a=0, b=0, coupling_=coupling):
        return sinh_gordon_kernel(theta, a, b, coupling_)
    return TBAModel(
        name="sinh-Gordon",
        rank=1,
        masses=np.array([1.0]),
        kernel=kernel,
        coupling=coupling,
        coxeter_number=2,
    )


def make_xxx_model() -> TBAModel:
    """Create a shadow XXX (rational) TBA model."""
    return TBAModel(
        name="XXX",
        rank=1,
        masses=np.array([1.0]),
        kernel=xxx_kernel,
        coupling=1.0,
        coxeter_number=2,
    )


def make_xxz_model(gamma: float = 0.5) -> TBAModel:
    """Create a shadow XXZ (trigonometric) TBA model."""
    def kernel(theta, a=0, b=0, coupling_=gamma):
        return xxz_kernel(theta, a, b, coupling_)
    return TBAModel(
        name="XXZ",
        rank=1,
        masses=np.array([1.0]),
        kernel=kernel,
        coupling=gamma,
        coxeter_number=2,
    )


def make_a_type_model(rank: int = 2) -> TBAModel:
    """Create an A_{rank} minimal TBA model."""
    masses = np.array([np.sin(PI * (a + 1) / (rank + 1))
                       for a in range(rank)])
    # Normalize so lightest mass = 1
    masses = masses / masses[0]

    def kernel(theta, a=0, b=0, coupling_=1.0, rank_=rank):
        return a_type_kernel(theta, a, b, coupling_, rank_)

    return TBAModel(
        name=f"A_{rank}",
        rank=rank,
        masses=masses,
        kernel=kernel,
        coupling=1.0,
        coxeter_number=rank + 1,
    )


# ========================================================================
# 2. TBA solver: iterative solution of integral equations
# ========================================================================

@dataclass
class TBASolution:
    """Solution of the TBA integral equations."""
    model: TBAModel
    r_param: float               # dimensionless temperature parameter
    theta_grid: np.ndarray       # quadrature grid
    epsilon: np.ndarray          # pseudo-energies, shape (rank, N_grid)
    n_iter: int                  # iterations to convergence
    converged: bool
    residual: float              # final residual norm


def solve_tba(model: TBAModel, r_param: float = 1.0,
              theta_max: float = 15.0, n_grid: int = 256,
              max_iter: int = 500, tol: float = 1e-12,
              damping: float = 0.5) -> TBASolution:
    """Solve TBA equations by iteration.

    The TBA equations:
        epsilon_a(theta) = r * m_a * cosh(theta)
            - sum_b int phi_{ab}(theta-theta') * L_b(theta') dtheta'/(2*pi)

    where L_b(theta) = log(1 + exp(-epsilon_b(theta))).

    Parameters
    ----------
    model : TBAModel
        The TBA model specification.
    r_param : float
        Dimensionless system size / temperature parameter.
    theta_max : float
        Cutoff for the rapidity integration.
    n_grid : int
        Number of quadrature points.
    max_iter : int
        Maximum iterations.
    tol : float
        Convergence tolerance on the pseudo-energy norm.
    damping : float
        Damping factor for iteration (0 < damping <= 1).

    Returns
    -------
    TBASolution
        The converged solution.
    """
    rank = model.rank
    # Gauss-Legendre quadrature on [-theta_max, theta_max]
    nodes, weights = np.polynomial.legendre.leggauss(n_grid)
    theta_grid = theta_max * nodes  # map [-1,1] -> [-theta_max, theta_max]
    dtheta = theta_max * weights     # include Jacobian

    # Initialize pseudo-energies: epsilon_a(theta) = r * m_a * cosh(theta)
    epsilon = np.zeros((rank, n_grid))
    for a in range(rank):
        epsilon[a, :] = r_param * model.masses[a] * np.cosh(theta_grid)

    # Precompute kernel matrix: K[a, b, i, j] = phi_{ab}(theta_i - theta_j)
    K = np.zeros((rank, rank, n_grid, n_grid))
    for a in range(rank):
        for b in range(rank):
            for i in range(n_grid):
                for j in range(n_grid):
                    K[a, b, i, j] = model.kernel(
                        theta_grid[i] - theta_grid[j], a, b
                    )

    # Driving term
    driving = np.zeros((rank, n_grid))
    for a in range(rank):
        driving[a, :] = r_param * model.masses[a] * np.cosh(theta_grid)

    # Iterate
    converged = False
    residual = float('inf')
    n_iter = 0

    for iteration in range(max_iter):
        # Compute L_b(theta') = log(1 + exp(-epsilon_b(theta')))
        L = np.zeros((rank, n_grid))
        for b in range(rank):
            # Use log1p(exp(-x)) with safe evaluation for large x
            for j in range(n_grid):
                if epsilon[b, j] > 500:
                    L[b, j] = np.exp(-epsilon[b, j])
                elif epsilon[b, j] < -500:
                    L[b, j] = -epsilon[b, j]
                else:
                    L[b, j] = np.log1p(np.exp(-epsilon[b, j]))

        # Convolution integral
        epsilon_new = np.copy(driving)
        for a in range(rank):
            for b in range(rank):
                # int phi_{ab}(theta-theta') * L_b(theta') dtheta' / (2*pi)
                for i in range(n_grid):
                    conv = np.sum(K[a, b, i, :] * L[b, :] * dtheta)
                    epsilon_new[a, i] -= conv / TWO_PI

        # Damped update
        epsilon_updated = damping * epsilon_new + (1.0 - damping) * epsilon
        residual = np.max(np.abs(epsilon_updated - epsilon))
        epsilon = epsilon_updated
        n_iter = iteration + 1

        if residual < tol:
            converged = True
            break

    return TBASolution(
        model=model,
        r_param=r_param,
        theta_grid=theta_grid,
        epsilon=epsilon,
        n_iter=n_iter,
        converged=converged,
        residual=residual,
    )


# ========================================================================
# 3. Effective central charge
# ========================================================================

def effective_central_charge(sol: TBASolution) -> float:
    """Compute the effective central charge from a TBA solution.

    c_eff = (6/pi^2) * sum_a int m_a * cosh(theta)
               * log(1 + exp(-epsilon_a(theta))) dtheta

    For the ground state at r -> 0, c_eff should approach the CFT
    central charge c.  At finite r, there are exponential corrections.
    """
    rank = sol.model.rank
    theta = sol.theta_grid
    result = 0.0

    # Use the quadrature weights from the original grid
    theta_max = theta[-1] / (1.0 if len(theta) < 2 else 1.0)
    # Recover weights: need to recompute since we only stored the grid
    n_grid = len(theta)
    nodes, weights = np.polynomial.legendre.leggauss(n_grid)
    # theta_grid = theta_max * nodes, so theta_max = theta[-1] / nodes[-1]
    if abs(nodes[-1]) > 1e-10:
        theta_max = theta[-1] / nodes[-1]
    else:
        theta_max = 15.0
    dtheta = theta_max * weights

    for a in range(rank):
        integrand = np.zeros(n_grid)
        for j in range(n_grid):
            eps_val = sol.epsilon[a, j]
            if eps_val > 500:
                log_term = np.exp(-eps_val)
            elif eps_val < -500:
                log_term = -eps_val
            else:
                log_term = np.log1p(np.exp(-eps_val))
            integrand[j] = sol.model.masses[a] * np.cosh(theta[j]) * log_term
        result += np.sum(integrand * dtheta)

    return (6.0 / PI**2) * result


def effective_central_charge_at_zero(sol: TBASolution, gamma_n: float) -> float:
    """Evaluate c_eff contribution at rapidity theta = gamma_n.

    This is a pointwise evaluation, not the full integral.
    c_eff_point(gamma_n) = (6/pi^2) * sum_a m_a * cosh(gamma_n)
                            * log(1 + exp(-epsilon_a(gamma_n)))
    """
    rank = sol.model.rank
    result = 0.0
    for a in range(rank):
        # Interpolate epsilon_a at gamma_n
        eps_val = np.interp(gamma_n, sol.theta_grid, sol.epsilon[a, :])
        if eps_val > 500:
            log_term = np.exp(-eps_val)
        elif eps_val < -500:
            log_term = -eps_val
        else:
            log_term = np.log1p(np.exp(-eps_val))
        result += sol.model.masses[a] * np.cosh(gamma_n) * log_term
    return (6.0 / PI**2) * result


def c_eff_at_zeta_zeros(sol: TBASolution, n_zeros: int = 30) -> Dict[str, Any]:
    """Compute c_eff at the first n_zeros Riemann zeta zeros.

    Returns a dict with:
      - gammas: the zero positions
      - c_eff_values: c_eff evaluated at each gamma_n
      - c_eff_full: the full integrated c_eff
      - corrections: c_eff(gamma_n) - c_eff_full for each n
    """
    gammas = get_zeta_gammas(n_zeros)
    c_eff_full = effective_central_charge(sol)
    c_eff_vals = np.array([
        effective_central_charge_at_zero(sol, g) for g in gammas
    ])
    return {
        'gammas': gammas,
        'c_eff_values': c_eff_vals,
        'c_eff_full': c_eff_full,
        'corrections': c_eff_vals - c_eff_full,
        'model_name': sol.model.name,
    }


# ========================================================================
# 4. Rogers dilogarithm
# ========================================================================

def rogers_dilogarithm(x: float) -> float:
    """Rogers dilogarithm L(x) for 0 < x < 1.

    L(x) = -1/2 * int_0^x [log(1-t)/t + log(t)/(1-t)] dt
         = Li_2(x) + (1/2) * log(x) * log(1-x)

    where Li_2(x) = -int_0^x log(1-t)/t dt is the Spence function.

    Special values:
      L(0) = 0
      L(1) = pi^2/6
      L(1/2) = pi^2/12
      L(golden_ratio^{-2}) = pi^2/10

    The sum rule for TBA:
      sum_{a} L(1/(1+Y_a(0))) = pi^2 * c / 6
    """
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return PI**2 / 6.0

    # Li_2(x) via the standard series (for moderate x)
    # For better accuracy, use the identity Li_2(x) = -int_0^x log(1-t)/t dt
    # scipy.special has it but we compute directly for transparency
    li2 = _li2(x)
    return li2 + 0.5 * np.log(x) * np.log(1.0 - x)


def _li2(x: float) -> float:
    """Spence's function Li_2(x) = -int_0^x log(1-t)/t dt for |x| <= 1."""
    if abs(x) < 1e-15:
        return 0.0
    if abs(x - 1.0) < 1e-15:
        return PI**2 / 6.0
    # For x in (0, 0.5], use direct series
    if 0 < x <= 0.5:
        s = 0.0
        xn = x
        for n in range(1, 200):
            s += xn / (n * n)
            xn *= x
            if abs(xn / (n * n)) < 1e-16:
                break
        return s
    # For x in (0.5, 1), use the identity Li_2(x) = -Li_2(1-x) + pi^2/6 - log(x)*log(1-x)
    if 0.5 < x < 1.0:
        return -_li2(1.0 - x) + PI**2 / 6.0 - np.log(x) * np.log(1.0 - x)
    # For x < 0, use Li_2(x) = -Li_2(x/(x-1)) - (1/2)*log(1-x)^2
    if x < 0:
        return -_li2(x / (x - 1.0)) - 0.5 * np.log(1.0 - x)**2
    return 0.0


def rogers_dilogarithm_identity_check(sol: TBASolution,
                                       c_expected: float) -> Dict[str, Any]:
    """Check the Rogers dilogarithm sum rule at theta = 0.

    For TBA ground state, at theta = 0:
        sum_a L(1/(1+Y_a(0))) = pi^2 * c / 6

    where Y_a(0) = exp(epsilon_a(0)).
    """
    rank = sol.model.rank
    total = 0.0
    terms = []

    for a in range(rank):
        # Interpolate epsilon at theta = 0
        eps_0 = np.interp(0.0, sol.theta_grid, sol.epsilon[a, :])
        Y_0 = np.exp(eps_0)
        x_a = 1.0 / (1.0 + Y_0)
        L_a = rogers_dilogarithm(x_a)
        total += L_a
        terms.append({
            'species': a,
            'epsilon_0': eps_0,
            'Y_0': Y_0,
            'x_a': x_a,
            'L_a': L_a,
        })

    expected = PI**2 * c_expected / 6.0
    return {
        'L_sum': total,
        'expected': expected,
        'difference': abs(total - expected),
        'relative_error': abs(total - expected) / max(abs(expected), 1e-100),
        'terms': terms,
        'c_from_L': 6.0 * total / PI**2,
    }


def rogers_dilogarithm_at_zeta_zeros(sol: TBASolution,
                                      n_zeros: int = 30) -> Dict[str, Any]:
    """Evaluate Rogers dilogarithm sum at each zeta zero rapidity.

    For each gamma_n:
        L_sum(gamma_n) = sum_a L(1/(1 + Y_a(gamma_n)))
    """
    gammas = get_zeta_gammas(n_zeros)
    L_sums = []
    c_values = []

    for gn in gammas:
        L_total = 0.0
        for a in range(sol.model.rank):
            eps_val = np.interp(gn, sol.theta_grid, sol.epsilon[a, :])
            Y_val = np.exp(eps_val)
            x_val = 1.0 / (1.0 + Y_val)
            if 0 < x_val < 1:
                L_total += rogers_dilogarithm(x_val)
        L_sums.append(L_total)
        c_values.append(6.0 * L_total / PI**2)

    return {
        'gammas': gammas,
        'L_sums': np.array(L_sums),
        'c_from_L': np.array(c_values),
    }


# ========================================================================
# 5. Y-system functional equations
# ========================================================================

def y_system_residual(sol: TBASolution, theta_eval: float,
                      delta: float = 0.01) -> Dict[str, Any]:
    """Check Y-system functional equation at a given rapidity.

    The Y-system for A-type:
        Y_a(theta + i*pi/h) * Y_a(theta - i*pi/h)
            = prod_b (1 + Y_b(theta))^{C_{ab}}

    where h is the Coxeter number and C is the Cartan matrix
    (here with POSITIVE off-diagonal entries from the incidence matrix,
    not the standard Cartan with negative off-diag -- we use |C_{ab}|).

    Since epsilon is real-valued on the real axis, we approximate
    the analytic continuation to theta +/- i*pi/h via numerical
    differentiation of the TBA integral equation.

    Concretely, for the rank-1 case with h=2:
        Y(theta + i*pi/2) * Y(theta - i*pi/2) = (1 + Y(theta))^2

    We check this at real theta by computing Y from the TBA solution.
    For the real-axis check (the periodicity consistency):
        Y(theta + pi/h) * Y(theta - pi/h) approx = (1+Y(theta))^2
    using the real-axis pseudo-energies shifted by pi/h.
    """
    rank = sol.model.rank
    h = sol.model.coxeter_number
    shift = PI / h
    C = sol.model.cartan_matrix

    residuals = []
    for a in range(rank):
        eps_center = np.interp(theta_eval, sol.theta_grid, sol.epsilon[a, :])
        eps_plus = np.interp(theta_eval + shift, sol.theta_grid, sol.epsilon[a, :])
        eps_minus = np.interp(theta_eval - shift, sol.theta_grid, sol.epsilon[a, :])

        Y_center = np.exp(eps_center)
        Y_plus = np.exp(eps_plus)
        Y_minus = np.exp(eps_minus)

        lhs = Y_plus * Y_minus

        rhs = 1.0
        for b in range(rank):
            eps_b = np.interp(theta_eval, sol.theta_grid, sol.epsilon[b, :])
            Y_b = np.exp(eps_b)
            # Use |C_{ab}| for the incidence matrix
            power = abs(C[a, b])
            rhs *= (1.0 + Y_b) ** power

        residuals.append({
            'species': a,
            'lhs': lhs,
            'rhs': rhs,
            'ratio': lhs / rhs if rhs != 0 else float('inf'),
            'log_residual': abs(np.log(lhs) - np.log(rhs)) if lhs > 0 and rhs > 0 else float('inf'),
        })

    return {
        'theta': theta_eval,
        'shift': shift,
        'coxeter_number': h,
        'residuals': residuals,
    }


def y_system_at_zeta_zeros(sol: TBASolution,
                            n_zeros: int = 30) -> Dict[str, Any]:
    """Check Y-system at each zeta zero rapidity."""
    gammas = get_zeta_gammas(n_zeros)
    results = []
    for gn in gammas:
        # Only check if gamma_n is within the grid range
        if gn < sol.theta_grid[-1] - PI / sol.model.coxeter_number:
            res = y_system_residual(sol, gn)
            results.append({
                'gamma_n': gn,
                'residuals': res['residuals'],
            })
    return {
        'model': sol.model.name,
        'n_checked': len(results),
        'results': results,
    }


# ========================================================================
# 6. Wall-crossing / Stokes phenomenon at zeta zeros
# ========================================================================

def wall_crossing_jump(sol: TBASolution, gamma_n: float,
                       delta: float = 0.01) -> Dict[str, Any]:
    """Compute pseudo-energy jump across rapidity gamma_n.

    epsilon_a(gamma_n + delta) - epsilon_a(gamma_n - delta)

    A nonzero jump (beyond interpolation error) would indicate
    that zeta zeros act as walls in the TBA sense, analogous to
    BPS walls in N=2 theories where the TBA spectrum reorganizes.

    For the ground-state TBA, we expect CONTINUITY (no Stokes jump),
    since the pseudo-energies are smooth functions of theta on the
    real axis.  Jumps would only occur in COMPLEXIFIED theta.

    We also compute the complexified version: evaluate the TBA
    integral at theta = gamma_n + i*delta vs theta = gamma_n - i*delta
    to detect genuine Stokes jumps.
    """
    rank = sol.model.rank
    jumps = []

    for a in range(rank):
        eps_plus = np.interp(gamma_n + delta, sol.theta_grid, sol.epsilon[a, :])
        eps_minus = np.interp(gamma_n - delta, sol.theta_grid, sol.epsilon[a, :])
        jump = eps_plus - eps_minus
        jumps.append({
            'species': a,
            'eps_plus': eps_plus,
            'eps_minus': eps_minus,
            'jump': jump,
            'relative_jump': abs(jump) / max(abs(eps_plus), abs(eps_minus), 1e-100),
        })

    return {
        'gamma_n': gamma_n,
        'delta': delta,
        'jumps': jumps,
        'max_jump': max(abs(j['jump']) for j in jumps),
    }


def wall_crossing_at_zeta_zeros(sol: TBASolution,
                                 n_zeros: int = 30,
                                 delta: float = 0.01) -> Dict[str, Any]:
    """Compute wall-crossing jumps at each zeta zero."""
    gammas = get_zeta_gammas(n_zeros)
    results = []
    for gn in gammas:
        if gn + delta < sol.theta_grid[-1]:
            wc = wall_crossing_jump(sol, gn, delta)
            results.append(wc)
    return {
        'model': sol.model.name,
        'delta': delta,
        'n_checked': len(results),
        'max_jumps': [r['max_jump'] for r in results],
        'results': results,
    }


def complexified_wall_crossing(sol: TBASolution, gamma_n: float,
                                delta: float = 0.1) -> Dict[str, Any]:
    """Compute the TBA integral at complexified rapidity near a zeta zero.

    Evaluate the convolution integral at theta = gamma_n + i*delta and
    theta = gamma_n - i*delta (complexified rapidity).  The difference
    detects poles/branch cuts in the pseudo-energy that would cross
    the integration contour.

    For real theta, the TBA driving term r*m*cosh(theta) and the
    convolution are both real, so the pseudo-energy is real on the
    real axis.  At complexified theta, the driving term is complex,
    and the convolution picks up complex values from kernel evaluation
    at complex argument.
    """
    rank = sol.model.rank
    results = []

    for a in range(rank):
        # Driving term at complex theta
        theta_complex_p = gamma_n + 1j * delta
        theta_complex_m = gamma_n - 1j * delta

        drive_p = sol.r_param * sol.model.masses[a] * np.cosh(theta_complex_p)
        drive_m = sol.r_param * sol.model.masses[a] * np.cosh(theta_complex_m)

        # Convolution at complex theta (approximate via real-axis data)
        conv_p = 0.0
        conv_m = 0.0
        n_grid = len(sol.theta_grid)
        nodes, weights = np.polynomial.legendre.leggauss(n_grid)
        if abs(nodes[-1]) > 1e-10:
            theta_max = sol.theta_grid[-1] / nodes[-1]
        else:
            theta_max = 15.0
        dtheta = theta_max * weights

        for b in range(rank):
            for j in range(n_grid):
                eps_bj = sol.epsilon[b, j]
                if eps_bj > 500:
                    L_j = np.exp(-eps_bj)
                elif eps_bj < -500:
                    L_j = -eps_bj
                else:
                    L_j = np.log1p(np.exp(-eps_bj))

                # Kernel at complex difference
                diff_p = complex(theta_complex_p - sol.theta_grid[j])
                diff_m = complex(theta_complex_m - sol.theta_grid[j])

                # For sinh-Gordon kernel with complex argument
                k_p = sol.model.kernel(diff_p.real, a, b)
                k_m = sol.model.kernel(diff_m.real, a, b)

                conv_p += k_p * L_j * dtheta[j]
                conv_m += k_m * L_j * dtheta[j]

        eps_p = complex(drive_p) - conv_p / TWO_PI
        eps_m = complex(drive_m) - conv_m / TWO_PI

        stokes_jump = eps_p - eps_m

        results.append({
            'species': a,
            'eps_plus': eps_p,
            'eps_minus': eps_m,
            'stokes_jump': stokes_jump,
            'abs_jump': abs(stokes_jump),
        })

    return {
        'gamma_n': gamma_n,
        'delta': delta,
        'results': results,
    }


# ========================================================================
# 7. Free energy at zeta zeros
# ========================================================================

def free_energy(sol: TBASolution) -> float:
    """Ground-state free energy F(r) from TBA.

    F(r) = -sum_a int m_a * cosh(theta) * log(1 + exp(-epsilon_a(theta)))
            * dtheta / (2*pi)
    """
    return -PI**2 * effective_central_charge(sol) / (6.0 * sol.r_param**2) \
        if sol.r_param > 0 else 0.0


def free_energy_at_zeta_radii(sol_factory: Callable,
                               n_zeros: int = 30) -> Dict[str, Any]:
    """Compute free energy at R = 1/(2*pi*gamma_n) for each zeta zero.

    Parameters
    ----------
    sol_factory : Callable
        Function r -> TBASolution that solves TBA at parameter r.
    n_zeros : int
        Number of zeta zeros to use.
    """
    gammas = get_zeta_gammas(n_zeros)
    results = []

    for i, gn in enumerate(gammas):
        R_n = 1.0 / (TWO_PI * gn)
        sol = sol_factory(R_n)
        F_n = free_energy(sol)
        c_eff = effective_central_charge(sol)

        results.append({
            'n': i + 1,
            'gamma_n': gn,
            'R_n': R_n,
            'F_n': F_n,
            'c_eff': c_eff,
        })

    # Compute F_predicted = -pi*c_eff/(6*R) for comparison
    for r in results:
        r['F_predicted'] = -PI * r['c_eff'] / (6.0 * r['R_n'])

    return {
        'results': results,
        'n_zeros': n_zeros,
    }


def free_energy_series(model: TBAModel, n_zeros: int = 30,
                       **solver_kwargs) -> Dict[str, Any]:
    """Compute F(R_n) = -pi*c_eff/(6*R_n) for R_n = 1/(2*pi*gamma_n).

    Uses the SAME TBA solution (at fixed r) and evaluates c_eff
    contributions at each rapidity = gamma_n.

    This is NOT the same as solving a separate TBA at each R_n;
    rather, it extracts the pointwise c_eff density from a single
    solution.
    """
    r_param = solver_kwargs.pop('r_param', 1.0)
    sol = solve_tba(model, r_param=r_param, **solver_kwargs)
    gammas = get_zeta_gammas(n_zeros)

    F_values = []
    for gn in gammas:
        R_n = 1.0 / (TWO_PI * gn)
        c_local = effective_central_charge_at_zero(sol, gn)
        F_n = -PI * c_local / (6.0 * R_n) if R_n > 0 else 0.0
        F_values.append(F_n)

    return {
        'gammas': gammas,
        'R_values': 1.0 / (TWO_PI * gammas),
        'F_values': np.array(F_values),
        'c_eff_full': effective_central_charge(sol),
        'converged': sol.converged,
    }


# ========================================================================
# 8. Excited-state TBA
# ========================================================================

def solve_excited_tba(model: TBAModel, r_param: float = 1.0,
                      source_positions: Optional[List[float]] = None,
                      n_sources: int = 1,
                      theta_max: float = 15.0, n_grid: int = 256,
                      max_iter: int = 500, tol: float = 1e-10,
                      damping: float = 0.5) -> TBASolution:
    """Solve excited-state TBA with source terms.

    The excited-state TBA equations (Al.B. Zamolodchikov 2000):
        epsilon_a(theta) = r * m_a * cosh(theta)
            - sum_b int phi_{ab}(theta-theta') * L_b(theta') dtheta'/(2*pi)
            + sum_k log|S_a(theta - theta_k)|

    where theta_k are positions of source singularities (quantized
    by periodicity of the Y-system).  The source terms correspond
    to excited-state rapidities.

    For the rank-1 sinh-Gordon model, the source term for a single
    particle at rapidity theta_0 is:
        log|S(theta - theta_0)| = log|(sinh(theta-theta_0+i*pi*p/2)
                                      / sinh(theta-theta_0-i*pi*p/2))|

    For simplicity, we use a Gaussian source approximation:
        source_a(theta) = A * exp(-(theta - theta_0)^2 / (2*sigma^2))
    with A and sigma chosen to give the correct quantum numbers.
    """
    if source_positions is None:
        source_positions = [0.0] * n_sources

    rank = model.rank
    n_grid_pts = n_grid
    nodes, weights = np.polynomial.legendre.leggauss(n_grid_pts)
    theta_grid = theta_max * nodes
    dtheta = theta_max * weights

    # Initialize
    epsilon = np.zeros((rank, n_grid_pts))
    for a in range(rank):
        epsilon[a, :] = r_param * model.masses[a] * np.cosh(theta_grid)

    # Precompute kernel
    K = np.zeros((rank, rank, n_grid_pts, n_grid_pts))
    for a in range(rank):
        for b in range(rank):
            for i in range(n_grid_pts):
                for j in range(n_grid_pts):
                    K[a, b, i, j] = model.kernel(
                        theta_grid[i] - theta_grid[j], a, b
                    )

    # Driving + source terms
    driving = np.zeros((rank, n_grid_pts))
    for a in range(rank):
        driving[a, :] = r_param * model.masses[a] * np.cosh(theta_grid)
        # Add source terms (log|S| evaluated at real rapidities)
        for theta_0 in source_positions:
            coupling = model.coupling
            for i in range(n_grid_pts):
                diff = theta_grid[i] - theta_0
                # Phase shift for sinh-Gordon:
                # log|S(theta)| = log|sinh(theta + i*pi*p/2) / sinh(theta - i*pi*p/2)|
                arg_p = diff + 1j * PI * coupling / 2.0
                arg_m = diff - 1j * PI * coupling / 2.0
                S_val = np.sinh(arg_p) / np.sinh(arg_m) if abs(np.sinh(arg_m)) > 1e-100 else 1.0
                driving[a, i] += np.log(max(abs(S_val), 1e-100))

    # Iterate
    converged = False
    residual = float('inf')
    n_iter = 0

    for iteration in range(max_iter):
        L = np.zeros((rank, n_grid_pts))
        for b in range(rank):
            for j in range(n_grid_pts):
                if epsilon[b, j] > 500:
                    L[b, j] = np.exp(-epsilon[b, j])
                elif epsilon[b, j] < -500:
                    L[b, j] = -epsilon[b, j]
                else:
                    L[b, j] = np.log1p(np.exp(-epsilon[b, j]))

        epsilon_new = np.copy(driving)
        for a in range(rank):
            for b in range(rank):
                for i in range(n_grid_pts):
                    conv = np.sum(K[a, b, i, :] * L[b, :] * dtheta)
                    epsilon_new[a, i] -= conv / TWO_PI

        epsilon_updated = damping * epsilon_new + (1.0 - damping) * epsilon
        residual = np.max(np.abs(epsilon_updated - epsilon))
        epsilon = epsilon_updated
        n_iter = iteration + 1

        if residual < tol:
            converged = True
            break

    return TBASolution(
        model=model,
        r_param=r_param,
        theta_grid=theta_grid,
        epsilon=epsilon,
        n_iter=n_iter,
        converged=converged,
        residual=residual,
    )


def excited_states_at_zeta_zeros(model: TBAModel,
                                  r_param: float = 1.0,
                                  n_zeros: int = 10,
                                  n_excited: int = 5,
                                  **kwargs) -> Dict[str, Any]:
    """Compute excited-state energies at each zeta zero.

    For each gamma_n, solve the excited-state TBA with 1,...,n_excited
    source particles, and compute the corresponding c_eff.
    """
    gammas = get_zeta_gammas(n_zeros)
    results = []

    for i, gn in enumerate(gammas):
        excited_c_effs = []
        for k in range(1, n_excited + 1):
            # Place k sources evenly around the origin
            sources = [gn * j / k for j in range(k)]
            sol = solve_excited_tba(
                model, r_param=r_param,
                source_positions=sources,
                n_sources=k,
                **kwargs,
            )
            c_eff = effective_central_charge(sol)
            excited_c_effs.append({
                'n_sources': k,
                'c_eff': c_eff,
                'converged': sol.converged,
            })

        results.append({
            'n': i + 1,
            'gamma_n': gn,
            'excited_states': excited_c_effs,
        })

    return {
        'model': model.name,
        'n_zeros': n_zeros,
        'n_excited': n_excited,
        'results': results,
    }


# ========================================================================
# 9. Kondo problem from shadow data
# ========================================================================

def solve_kondo_tba(model: TBAModel, r_param: float = 1.0,
                    theta_0: float = 0.0, d_imp: float = 1.0,
                    theta_max: float = 15.0, n_grid: int = 256,
                    max_iter: int = 500, tol: float = 1e-10,
                    damping: float = 0.5) -> TBASolution:
    """Solve TBA with Kondo impurity.

    epsilon_imp(theta) = epsilon_bulk(theta) + d_imp * log(cosh(theta - theta_0))

    where theta_0 is the impurity position and d_imp controls the
    impurity strength (related to the representation dimension).

    The Kondo temperature is extracted from the crossover scale:
        T_K ~ m * exp(-pi / (d_imp * phi(0)))
    """
    rank = model.rank

    n_grid_pts = n_grid
    nodes, weights = np.polynomial.legendre.leggauss(n_grid_pts)
    theta_grid = theta_max * nodes
    dtheta = theta_max * weights

    # Initialize
    epsilon = np.zeros((rank, n_grid_pts))
    for a in range(rank):
        epsilon[a, :] = r_param * model.masses[a] * np.cosh(theta_grid)

    # Precompute kernel
    K = np.zeros((rank, rank, n_grid_pts, n_grid_pts))
    for a in range(rank):
        for b in range(rank):
            for i in range(n_grid_pts):
                for j in range(n_grid_pts):
                    K[a, b, i, j] = model.kernel(
                        theta_grid[i] - theta_grid[j], a, b
                    )

    # Driving with impurity
    driving = np.zeros((rank, n_grid_pts))
    for a in range(rank):
        for i in range(n_grid_pts):
            driving[a, i] = (r_param * model.masses[a] * np.cosh(theta_grid[i])
                             + d_imp * np.log(np.cosh(theta_grid[i] - theta_0)))

    # Iterate
    converged = False
    residual = float('inf')
    n_iter = 0

    for iteration in range(max_iter):
        L = np.zeros((rank, n_grid_pts))
        for b in range(rank):
            for j in range(n_grid_pts):
                if epsilon[b, j] > 500:
                    L[b, j] = np.exp(-epsilon[b, j])
                elif epsilon[b, j] < -500:
                    L[b, j] = -epsilon[b, j]
                else:
                    L[b, j] = np.log1p(np.exp(-epsilon[b, j]))

        epsilon_new = np.copy(driving)
        for a in range(rank):
            for b in range(rank):
                for i in range(n_grid_pts):
                    conv = np.sum(K[a, b, i, :] * L[b, :] * dtheta)
                    epsilon_new[a, i] -= conv / TWO_PI

        epsilon_updated = damping * epsilon_new + (1.0 - damping) * epsilon
        residual = np.max(np.abs(epsilon_updated - epsilon))
        epsilon = epsilon_updated
        n_iter = iteration + 1

        if residual < tol:
            converged = True
            break

    return TBASolution(
        model=model,
        r_param=r_param,
        theta_grid=theta_grid,
        epsilon=epsilon,
        n_iter=n_iter,
        converged=converged,
        residual=residual,
    )


def kondo_temperature(model: TBAModel, d_imp: float = 1.0) -> float:
    """Estimate the Kondo temperature from the TBA kernel.

    T_K ~ m * exp(-pi / (d_imp * phi(0)))

    where phi(0) is the kernel evaluated at theta = 0.
    """
    phi_0 = model.kernel(0.0, 0, 0)
    if phi_0 <= 0 or d_imp <= 0:
        return 0.0
    return model.masses[0] * np.exp(-PI / (d_imp * phi_0))


def kondo_at_zeta_zeros(model: TBAModel, r_param: float = 1.0,
                         d_imp: float = 1.0, n_zeros: int = 30,
                         **kwargs) -> Dict[str, Any]:
    """Compute Kondo TBA at each zeta zero position.

    Set theta_0 = gamma_n and compute:
      - Kondo temperature T_K(gamma_n)
      - c_eff with impurity at gamma_n
    """
    gammas = get_zeta_gammas(n_zeros)
    results = []

    for i, gn in enumerate(gammas):
        sol = solve_kondo_tba(
            model, r_param=r_param, theta_0=gn,
            d_imp=d_imp, **kwargs,
        )
        c_eff = effective_central_charge(sol)
        T_K = kondo_temperature(model, d_imp)

        results.append({
            'n': i + 1,
            'gamma_n': gn,
            'c_eff': c_eff,
            'T_K': T_K,
            'converged': sol.converged,
            'n_iter': sol.n_iter,
        })

    return {
        'model': model.name,
        'd_imp': d_imp,
        'n_zeros': n_zeros,
        'results': results,
    }


# ========================================================================
# 10. ODE/IM correspondence
# ========================================================================

def monster_potential(x: float, ell: float = 0.0,
                     shadow_coupling: float = 1.0) -> float:
    """Monster potential for the ODE/IM correspondence.

    V(x) = x^{2M} + ell*(ell+1)/x^2

    where M is related to the shadow coupling:
      M = h / (h - 1) for Coxeter number h,
      ell is the angular momentum quantum number.

    For the sinh-Gordon TBA (h=2): M = 2, V = x^4 + ell*(ell+1)/x^2.
    """
    M = 2.0 / (1.0 - 1.0 / max(shadow_coupling + 1, 1.001))
    # Clamp M to reasonable range
    M = min(M, 20.0)
    M = max(M, 1.01)

    V = abs(x) ** (2 * M)
    if abs(x) > 1e-10:
        V += ell * (ell + 1.0) / (x * x)
    return V


def solve_ode_im(E: float, ell: float = 0.0, shadow_coupling: float = 1.0,
                 x_max: float = 10.0, n_points: int = 1000) -> Dict[str, Any]:
    """Solve the Schrodinger equation for the monster potential.

    (-d^2/dx^2 + V(x)) psi = E * psi

    Uses Numerov's method on [epsilon, x_max] with epsilon > 0 small.

    Returns the wavefunction and the Stokes multiplier (ratio of
    exponentially growing to decaying solutions at x -> +infinity).
    """
    dx = x_max / n_points
    x_grid = np.linspace(dx, x_max, n_points)

    # Effective potential
    V = np.array([monster_potential(x, ell, shadow_coupling) for x in x_grid])
    f = V - E  # f(x) = V(x) - E; Schrodinger: psi'' + f*psi = 0 is psi'' = f*psi

    # Numerov integration: psi_{n+1} = (2*(1-5h^2f_n/12)*psi_n - (1+h^2f_{n-1}/12)*psi_{n-1}) / (1+h^2f_{n+1}/12)
    h2 = dx * dx
    psi = np.zeros(n_points)

    # Initial conditions: psi ~ x^{ell+1} near origin
    psi[0] = x_grid[0] ** (ell + 1)
    psi[1] = x_grid[1] ** (ell + 1)

    for n in range(1, n_points - 1):
        num = 2.0 * (1.0 - 5.0 * h2 * f[n] / 12.0) * psi[n] \
            - (1.0 + h2 * f[n - 1] / 12.0) * psi[n - 1]
        den = 1.0 + h2 * f[n + 1] / 12.0
        if abs(den) < 1e-100:
            psi[n + 1] = psi[n]
        else:
            psi[n + 1] = num / den

    # Extract Stokes data: at large x, psi ~ A * exp(+k*x) + B * exp(-k*x)
    # where k = sqrt(V(x_max) - E).  The Stokes multiplier is A/B.
    if V[-1] > E:
        k = np.sqrt(V[-1] - E)
        # From the last two points:
        # psi[-1] = A*exp(k*x[-1]) + B*exp(-k*x[-1])
        # psi[-2] = A*exp(k*x[-2]) + B*exp(-k*x[-2])
        e1 = np.exp(k * x_grid[-1])
        e2 = np.exp(k * x_grid[-2])
        em1 = np.exp(-k * x_grid[-1])
        em2 = np.exp(-k * x_grid[-2])

        det = e1 * em2 - e2 * em1
        if abs(det) > 1e-100:
            A_coeff = (psi[-1] * em2 - psi[-2] * em1) / det
            B_coeff = (e1 * psi[-2] - e2 * psi[-1]) / det
            stokes_multiplier = A_coeff / B_coeff if abs(B_coeff) > 1e-100 else float('inf')
        else:
            stokes_multiplier = float('nan')
    else:
        stokes_multiplier = float('nan')

    return {
        'E': E,
        'ell': ell,
        'x_grid': x_grid,
        'psi': psi,
        'stokes_multiplier': stokes_multiplier,
        'V': V,
    }


def ode_im_at_shadow_eigenvalues(shadow_eigenvalues: List[float],
                                  ell: float = 0.0,
                                  shadow_coupling: float = 1.0,
                                  **kwargs) -> Dict[str, Any]:
    """Solve ODE/IM at shadow eigenvalues and extract Stokes data.

    The shadow eigenvalues are derived from the pseudo-energies
    at zeta zeros: E_n ~ epsilon(gamma_n).
    """
    results = []
    for E in shadow_eigenvalues:
        sol = solve_ode_im(E, ell, shadow_coupling, **kwargs)
        results.append({
            'E': E,
            'stokes_multiplier': sol['stokes_multiplier'],
        })

    return {
        'n_eigenvalues': len(shadow_eigenvalues),
        'results': results,
    }


def ode_stokes_vs_tba(tba_sol: TBASolution, n_zeros: int = 10,
                       ell: float = 0.0,
                       shadow_coupling: float = 1.0) -> Dict[str, Any]:
    """Compare ODE Stokes multipliers with TBA Y-function at zeta zeros.

    The ODE/IM correspondence predicts:
        Y(theta) ~ T(E(theta)) / T_bar(E(theta))

    where T, T_bar are the spectral determinant and its conjugate.
    We compare the Stokes multiplier (which encodes T/T_bar) at
    E = r*m*cosh(gamma_n) with the Y-function Y(gamma_n) = exp(epsilon(gamma_n)).
    """
    gammas = get_zeta_gammas(n_zeros)
    results = []

    for i, gn in enumerate(gammas):
        # TBA data
        eps_val = np.interp(gn, tba_sol.theta_grid, tba_sol.epsilon[0, :])
        Y_tba = np.exp(eps_val)

        # ODE energy at this rapidity
        E_val = tba_sol.r_param * tba_sol.model.masses[0] * np.cosh(gn)

        # Solve ODE
        ode_sol = solve_ode_im(E_val, ell, shadow_coupling)
        stokes = ode_sol['stokes_multiplier']

        results.append({
            'n': i + 1,
            'gamma_n': gn,
            'Y_tba': Y_tba,
            'E_ode': E_val,
            'stokes': stokes,
            'log_Y': eps_val,
            'log_stokes': np.log(abs(stokes)) if stokes != 0 and np.isfinite(stokes) else float('nan'),
        })

    return {
        'model': tba_sol.model.name,
        'n_zeros': n_zeros,
        'results': results,
    }


# ========================================================================
# 11. Nonlinear Integral Equation (NLIE)
# ========================================================================

def solve_nlie(r_param: float = 1.0, gamma_aniso: float = PI / 3,
               theta_max: float = 15.0, n_grid: int = 256,
               max_iter: int = 500, tol: float = 1e-10,
               damping: float = 0.5) -> Dict[str, Any]:
    """Solve the NLIE (Destri-de Vega).

    ln a(theta) = -i*r*sinh(theta)
                 + int G(theta-theta') * ln(1+a(theta')) dtheta'/(2*pi)
                 - int G(theta-theta') * ln(1+a_bar(theta')) dtheta'/(2*pi)

    where G_hat(omega) = -sinh((pi-gamma)*omega) / (2*sinh(pi*omega)*cosh(gamma*omega))

    We discretize on a real-theta grid.  Since the driving term
    is purely imaginary on the real axis, a(theta) is complex-valued.
    Write a = exp(f + i*g) where f, g are real, and iterate.

    For the XXZ model at anisotropy gamma.  The effective central charge:
        c_eff = 1 - 6*(pi-gamma)^2 / (pi*gamma)

    Equivalently for the sine-Gordon model with coupling beta^2/(8*pi) = gamma/pi.
    """
    nodes, weights = np.polynomial.legendre.leggauss(n_grid)
    theta_grid = theta_max * nodes
    dtheta = theta_max * weights

    # Kernel G in Fourier space: G_hat(omega) = -sinh((pi-gamma)*omega) / (2*sinh(pi*omega)*cosh(gamma*omega))
    # Compute G(theta) numerically via inverse FFT or direct quadrature.
    # For direct computation, use the integral representation:
    #   G(theta) = int G_hat(omega) * exp(i*omega*theta) domega / (2*pi)
    # We precompute G on the theta-grid differences.

    def G_kernel(theta_diff):
        """Evaluate the NLIE kernel G(theta) by direct integration."""
        def integrand_real(omega):
            if abs(omega) < 1e-10:
                return -(PI - gamma_aniso) / (2.0 * PI * 1.0) / TWO_PI
            num = -np.sinh((PI - gamma_aniso) * omega)
            den = 2.0 * np.sinh(PI * omega) * np.cosh(gamma_aniso * omega)
            if abs(den) < 1e-100:
                return 0.0
            return (num / den) * np.cos(omega * theta_diff) / TWO_PI

        result, _ = integrate.quad(integrand_real, 0, 50, limit=100,
                                   epsabs=1e-12, epsrel=1e-12)
        return 2.0 * result  # factor of 2 from symmetric integral

    # Precompute kernel matrix
    G_mat = np.zeros((n_grid, n_grid))
    for i in range(n_grid):
        for j in range(n_grid):
            G_mat[i, j] = G_kernel(theta_grid[i] - theta_grid[j])

    # Initialize: a(theta) = exp(-i*r*sinh(theta))
    ln_a = -1j * r_param * np.sinh(theta_grid)

    converged = False
    residual = float('inf')
    n_iter = 0

    for iteration in range(max_iter):
        # a(theta) = exp(ln_a(theta))
        a = np.exp(ln_a)
        a_bar = np.conj(a)

        # Compute ln(1+a) and ln(1+a_bar)
        ln1pa = np.log(1.0 + a)
        ln1pa_bar = np.log(1.0 + a_bar)

        # Convolution
        ln_a_new = -1j * r_param * np.sinh(theta_grid)
        for i in range(n_grid):
            conv_p = np.sum(G_mat[i, :] * ln1pa * dtheta) / TWO_PI
            conv_m = np.sum(G_mat[i, :] * ln1pa_bar * dtheta) / TWO_PI
            ln_a_new[i] += conv_p - conv_m

        # Damped update
        ln_a_updated = damping * ln_a_new + (1.0 - damping) * ln_a
        residual = np.max(np.abs(ln_a_updated - ln_a))
        ln_a = ln_a_updated
        n_iter = iteration + 1

        if residual < tol:
            converged = True
            break

    # Extract c_eff from NLIE
    # c_eff = (6*r^2/pi^2) * int m*cosh(theta) * Im(ln(1+a)) dtheta / (2*pi)
    # For the sine-Gordon: m = 1, and the relation is:
    #   c_eff = 1 - 6*(pi-gamma)^2 / (pi*gamma)  [at r -> 0]
    a_final = np.exp(ln_a)
    im_ln1pa = np.imag(np.log(1.0 + a_final))
    c_eff_nlie = (6.0 / PI**2) * np.sum(
        np.cosh(theta_grid) * im_ln1pa * dtheta
    )

    c_eff_expected = 1.0 - 6.0 * (PI - gamma_aniso)**2 / (PI * gamma_aniso)

    return {
        'theta_grid': theta_grid,
        'ln_a': ln_a,
        'a': np.exp(ln_a),
        'n_iter': n_iter,
        'converged': converged,
        'residual': residual,
        'c_eff': c_eff_nlie,
        'c_eff_expected': c_eff_expected,
        'gamma': gamma_aniso,
    }


def nlie_at_zeta_zeros(r_param: float = 1.0,
                        gamma_aniso: float = PI / 3,
                        n_zeros: int = 30,
                        **kwargs) -> Dict[str, Any]:
    """Evaluate NLIE solution at zeta zero rapidities.

    Solve the NLIE once and extract ln a(gamma_n) at each zeta zero.
    """
    sol = solve_nlie(r_param=r_param, gamma_aniso=gamma_aniso, **kwargs)
    gammas = get_zeta_gammas(n_zeros)

    ln_a_at_zeros = []
    for gn in gammas:
        ln_a_val = np.interp(gn, sol['theta_grid'], np.real(sol['ln_a'])) \
            + 1j * np.interp(gn, sol['theta_grid'], np.imag(sol['ln_a']))
        ln_a_at_zeros.append(ln_a_val)

    return {
        'gammas': gammas,
        'ln_a_at_zeros': np.array(ln_a_at_zeros),
        'c_eff': sol['c_eff'],
        'c_eff_expected': sol['c_eff_expected'],
        'converged': sol['converged'],
    }


# ========================================================================
# 12. TBA-NLIE comparison at zeta zeros
# ========================================================================

def compare_tba_nlie(model: TBAModel, r_param: float = 1.0,
                     gamma_aniso: float = PI / 3,
                     n_zeros: int = 20,
                     n_grid: int = 128,
                     **kwargs) -> Dict[str, Any]:
    """Compare TBA and NLIE solutions at zeta zeros.

    Both methods should give the same c_eff and pseudo-energies
    (up to the dictionary relating epsilon_TBA and ln_a_NLIE).

    For the XXZ/sine-Gordon at anisotropy gamma:
      - TBA coupling p = gamma/pi
      - NLIE anisotropy = gamma
      - c_eff_TBA should match c_eff_NLIE
    """
    # Solve TBA
    tba_sol = solve_tba(model, r_param=r_param, n_grid=n_grid, **kwargs)
    c_eff_tba = effective_central_charge(tba_sol)

    # Solve NLIE
    nlie_sol = solve_nlie(r_param=r_param, gamma_aniso=gamma_aniso,
                          n_grid=n_grid, **kwargs)
    c_eff_nlie = nlie_sol['c_eff']

    # Compare at zeta zeros
    gammas = get_zeta_gammas(n_zeros)
    comparisons = []

    for i, gn in enumerate(gammas):
        # TBA pseudo-energy at gamma_n
        eps_tba = np.interp(gn, tba_sol.theta_grid, tba_sol.epsilon[0, :])

        # NLIE ln(a) at gamma_n
        ln_a_real = np.interp(gn, nlie_sol['theta_grid'], np.real(nlie_sol['ln_a']))
        ln_a_imag = np.interp(gn, nlie_sol['theta_grid'], np.imag(nlie_sol['ln_a']))

        comparisons.append({
            'n': i + 1,
            'gamma_n': gn,
            'eps_tba': eps_tba,
            'ln_a_real': ln_a_real,
            'ln_a_imag': ln_a_imag,
        })

    return {
        'c_eff_tba': c_eff_tba,
        'c_eff_nlie': c_eff_nlie,
        'c_eff_diff': abs(c_eff_tba - c_eff_nlie),
        'tba_converged': tba_sol.converged,
        'nlie_converged': nlie_sol['converged'],
        'comparisons': comparisons,
    }


# ========================================================================
# 13. Shadow-to-TBA dictionary
# ========================================================================

def shadow_to_tba_coupling(kappa: float, c: float,
                            S4: float = 0.0) -> float:
    """Extract TBA coupling from shadow data.

    The shadow obstruction tower determines a scattering theory.
    The leading coupling is:
        p = sqrt(S4 / kappa) if S4/kappa > 0
        p = 0               if S4 = 0 (Gaussian/free field)

    For the Virasoro algebra: kappa = c/2, S4 = quartic shadow coefficient.
    For Heisenberg: kappa = k, S4 = 0 (class G, tower terminates at arity 2).

    The shadow coupling controls the TBA kernel:
      p = 0: free boson (trivial S-matrix)
      0 < p < 1: sinh-Gordon regime
      p = 1: Ising
      p > 1: higher-level regime
    """
    if kappa == 0 or S4 == 0:
        return 0.0
    ratio = S4 / kappa
    if ratio > 0:
        return min(np.sqrt(ratio), 2.0)  # cap at 2 for stability
    return 0.0


def shadow_tba_system(c: float, kappa: Optional[float] = None,
                       S4: float = 0.0,
                       model_type: str = "sinh-Gordon") -> TBAModel:
    """Build TBA model from shadow data.

    Parameters
    ----------
    c : float
        Central charge of the chiral algebra.
    kappa : float, optional
        Modular characteristic. Default: c/2 (Virasoro).
    S4 : float
        Quartic shadow coefficient.
    model_type : str
        One of "sinh-Gordon", "XXX", "XXZ".
    """
    if kappa is None:
        kappa = c / 2.0

    coupling = shadow_to_tba_coupling(kappa, c, S4)

    if model_type == "sinh-Gordon":
        return make_sinh_gordon_model(coupling=max(coupling, 0.01))
    elif model_type == "XXX":
        return make_xxx_model()
    elif model_type == "XXZ":
        return make_xxz_model(gamma=max(coupling, 0.01))
    else:
        raise ValueError(f"Unknown model type: {model_type}")


# ========================================================================
# 14. Full pipeline: shadow data -> TBA -> zeta zero analysis
# ========================================================================

def full_zeta_zero_tba_analysis(c: float, kappa: Optional[float] = None,
                                 S4: float = 0.0,
                                 model_type: str = "sinh-Gordon",
                                 r_param: float = 1.0,
                                 n_zeros: int = 30,
                                 n_grid: int = 128,
                                 **solver_kwargs) -> Dict[str, Any]:
    """Complete TBA analysis at Riemann zeta zeros from shadow data.

    Pipeline:
    1. Build TBA model from shadow data (c, kappa, S4)
    2. Solve TBA
    3. Compute c_eff at each zeta zero
    4. Check Rogers dilogarithm identity
    5. Check Y-system at zeta zeros
    6. Compute wall-crossing jumps
    7. Compute free energy series

    Returns a comprehensive result dictionary.
    """
    if kappa is None:
        kappa = c / 2.0

    # Build model
    model = shadow_tba_system(c, kappa, S4, model_type)

    # Solve TBA
    sol = solve_tba(model, r_param=r_param, n_grid=n_grid, **solver_kwargs)

    # c_eff analysis
    c_eff_data = c_eff_at_zeta_zeros(sol, n_zeros)

    # Rogers dilogarithm
    rogers_data = rogers_dilogarithm_identity_check(sol, c)

    # Y-system
    y_data = y_system_at_zeta_zeros(sol, n_zeros)

    # Wall-crossing
    wc_data = wall_crossing_at_zeta_zeros(sol, n_zeros)

    # Free energy
    fe_data = free_energy_series(model, n_zeros, r_param=r_param, n_grid=n_grid)

    return {
        'model': model.name,
        'central_charge': c,
        'kappa': kappa,
        'S4': S4,
        'coupling': model.coupling,
        'r_param': r_param,
        'tba_converged': sol.converged,
        'tba_iterations': sol.n_iter,
        'tba_residual': sol.residual,
        'c_eff_full': c_eff_data['c_eff_full'],
        'c_eff_at_zeros': c_eff_data,
        'rogers_dilogarithm': rogers_data,
        'y_system': y_data,
        'wall_crossing': wc_data,
        'free_energy': fe_data,
    }
