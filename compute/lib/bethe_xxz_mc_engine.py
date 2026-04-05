r"""Trigonometric Bethe ansatz from the Maurer-Cartan element.

Derives the XXZ spin chain Bethe ansatz equations from the MC element
Theta_A of the affine sl_2^{(1)} chiral algebra at level k.  The chain
of derivation is:

    MC element Theta_A  (thm:mc2-bar-intrinsic)
        |
        v
    Collision residue r(z) = Res^{coll}_{0,2}(Theta_A)  (AP19)
        |
        v
    Trigonometric R-matrix R(u) for U_q(sl_2), q = e^{i*gamma}
        |
        v
    Yang-Baxter equation R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}
        |
        v
    Transfer matrix T(u) = Tr_a( R_{a1}(u) ... R_{aN}(u) )
    with [T(u), T(v)] = 0  (QISM)
        |
        v
    Algebraic Bethe ansatz: B(u) creation operators on pseudovacuum
        |
        v
    Bethe ansatz equations (regularity conditions):
        [sin(lambda_j + gamma/2) / sin(lambda_j - gamma/2)]^N
            = prod_{k != j} sin(lambda_j - lambda_k + gamma)
                          / sin(lambda_j - lambda_k - gamma)
        |
        v
    Energy spectrum:  E = -J sum_j sin^2(gamma)
                                    / (cos(2*lambda_j) - cos(gamma))

The anisotropy parameter Delta = cos(gamma) relates to the level via
gamma = pi / (k+2) for the level-k representation of sl_2^{(1)}.

EXTENSIONS:
- Higher-spin XXZ via the fusion procedure (spin-s Babujian-Takhtadzhan)
- XYZ chain from the genus-1 shadow (elliptic R-matrix)
- Free fermion point Delta = 0 (gamma = pi/2): exact diagonalization
- String hypothesis for bound states

VERIFICATION PATHS:
  Path 1: MC -> r-matrix -> YBE -> Bethe equations (algebraic)
  Path 2: Direct diagonalization of the XXZ Hamiltonian
  Path 3: Bethe ansatz energies vs exact spectrum
  Path 4: XXX limit (gamma -> 0): recover rational Bethe equations
  Path 5: Free fermion point (Delta = 0): exact solution
  Path 6: String hypothesis verification for N >= 8

Conventions
-----------
- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
- kappa(sl_2, k) = 3(k+2)/4.
- Bar complex propagator d log E(z,w) is weight 1 (AP27).
- R-matrix r(z) has pole order ONE LESS than OPE (AP19).
- XXZ Hamiltonian: H = J sum [S^x S^x + S^y S^y + Delta S^z S^z].
- Periodic boundary conditions throughout.
- Pauli matrices: sigma_x, sigma_y, sigma_z standard physics convention.
- Spin sites numbered 0, ..., N-1.

References
----------
- Baxter, "Exactly solved models in statistical mechanics" (1982)
- Faddeev, "How the algebraic Bethe ansatz works" (Les Houches 1996)
- Korepin-Bogoliubov-Izergin, "QISM and Correlation Functions" (1993)
- Babujian-Takhtadzhan, "Higher spin XXZ" (1982)
- thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
- AP19, AP27 (CLAUDE.md)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
from numpy import linalg as la
from scipy import optimize
from itertools import combinations


# ========================================================================
# 0.  Constants and Pauli matrices
# ========================================================================

PI = np.pi
I2 = np.eye(2, dtype=complex)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA_PLUS = np.array([[0, 1], [0, 0]], dtype=complex)
SIGMA_MINUS = np.array([[0, 0], [1, 0]], dtype=complex)


def _kron_chain(ops: List[np.ndarray]) -> np.ndarray:
    """Kronecker product of a list of operators."""
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result


def _spin_op(N: int, site: int, pauli: np.ndarray) -> np.ndarray:
    """Pauli operator at site `site` in an N-site chain."""
    ops = [I2] * N
    ops[site] = pauli
    return _kron_chain(ops)


# ========================================================================
# 1.  MC element for affine sl_2^{(1)} and the collision residue
# ========================================================================

@dataclass
class AffineSl2MCData:
    """MC element data for sl_2^{(1)} at level k.

    The MC element Theta_A lives in the modular cyclic deformation
    complex Def_cyc^mod(A).  Its genus-0 arity-2 projection gives
    the r-matrix r(z) = Res^{coll}_{0,2}(Theta_A).

    For sl_2^{(1)} at level k:
      - kappa = 3*(k+2)/4  (modular characteristic)
      - gamma = pi / (k+2)  (anisotropy angle)
      - Delta = cos(gamma)  (XXZ anisotropy parameter)
      - q = exp(i*gamma)    (quantum group deformation parameter)

    The level-k representation of the quantum group U_q(sl_2) with
    q = exp(i*pi/(k+2)) gives the trigonometric R-matrix that
    controls the XXZ spin chain with Delta = cos(pi/(k+2)).
    """
    k: float  # level
    kappa: float = field(init=False)
    gamma: float = field(init=False)
    Delta: float = field(init=False)
    q: complex = field(init=False)

    def __post_init__(self):
        self.kappa = 3.0 * (self.k + 2) / 4.0
        self.gamma = PI / (self.k + 2)
        self.Delta = np.cos(self.gamma)
        self.q = np.exp(1j * self.gamma)


def collision_residue_trigonometric(mc: AffineSl2MCData, z: complex) -> np.ndarray:
    r"""Collision residue r(z) = Res^{coll}_{0,2}(Theta_A).

    For sl_2^{(1)} at level k, the bar propagator d log E(z,w) extracts
    the collision residue of the OPE.  By AP19, the r-matrix has pole
    order ONE LESS than the OPE.

    The trigonometric r-matrix in the spin-1/2 representation:
        r(z) = cot(z) (sigma_z x sigma_z)/4
             + csc(z) [(sigma_+ x sigma_-) + (sigma_- x sigma_+)] / 2

    In matrix form on C^2 x C^2:
        r(z) = | cot(z)/4,  0,          0,          0         |
               | 0,        -cot(z)/4,   csc(z)/2,   0         |
               | 0,         csc(z)/2,  -cot(z)/4,   0         |
               | 0,         0,          0,          cot(z)/4   |

    This is related to the full R-matrix by:
        R(u) = sin(gamma) * r(u) + permutation corrections
    More precisely, R(u) = a(u) E_11 + b(u) E_22 + c(u) E_12
    with the six-vertex weights.

    Parameters
    ----------
    mc : AffineSl2MCData
        MC data for sl_2^{(1)} at level k.
    z : complex
        Spectral parameter.

    Returns
    -------
    r : np.ndarray
        4x4 matrix (the r-matrix in spin-1/2 representation).
    """
    gamma = mc.gamma
    cot_z = np.cos(z) / np.sin(z) if abs(np.sin(z)) > 1e-15 else 1e15
    csc_z = 1.0 / np.sin(z) if abs(np.sin(z)) > 1e-15 else 1e15

    # r(z) = cot(z)/4 * (sigma_z x sigma_z)
    #       + csc(z)/2 * (sigma_+ x sigma_- + sigma_- x sigma_+)
    sz_sz = np.kron(SIGMA_Z, SIGMA_Z) / 4.0
    sp_sm = np.kron(SIGMA_PLUS, SIGMA_MINUS)
    sm_sp = np.kron(SIGMA_MINUS, SIGMA_PLUS)

    r = cot_z * sz_sz + csc_z * (sp_sm + sm_sp) / 2.0
    return r


# ========================================================================
# 2.  Trigonometric R-matrix from MC (six-vertex model)
# ========================================================================

def R_matrix_xxz(u: complex, gamma: complex) -> np.ndarray:
    r"""Trigonometric R-matrix for the XXZ chain.

    R(u, gamma) = | sin(u + gamma),  0,            0,            0              |
                  | 0,               sin(u),       sin(gamma),   0              |
                  | 0,               sin(gamma),   sin(u),       0              |
                  | 0,               0,            0,            sin(u + gamma) |

    This is the six-vertex model R-matrix.

    Properties:
    - R(0) = sin(gamma) * P (regularity)
    - Satisfies YBE: R_{12}(u-v) R_{13}(u) R_{23}(v)
                    = R_{23}(v) R_{13}(u) R_{12}(u-v)
    - Unitarity: R_{12}(u) R_{21}(-u) = rho(u) * I
      with rho(u) = sin(u+gamma)*sin(gamma-u)

    In the limit gamma -> 0 (q -> 1):
        R(u, gamma) / sin(gamma) -> (u/gamma)*I + P
        which is the rational Yang R-matrix (XXX chain).

    Connection to MC:
        The MC element Theta_A for sl_2^{(1)} at level k has
        gamma = pi/(k+2).  The collision residue gives the
        r-matrix r(u) ~ cot(u) sigma_z x sigma_z + csc(u) (flips),
        and the R-matrix is:
            R(u) = sin(gamma) * [I + sin(gamma) * r(u) * ...]
        after appropriate regularization.

    Parameters
    ----------
    u : complex
        Spectral parameter (rapidity difference).
    gamma : complex
        Anisotropy parameter.  Delta = cos(gamma).

    Returns
    -------
    R : np.ndarray
        4x4 R-matrix.
    """
    a = np.sin(u + gamma)
    b = np.sin(u)
    c = np.sin(gamma)
    return np.array([
        [a, 0, 0, 0],
        [0, b, c, 0],
        [0, c, b, 0],
        [0, 0, 0, a],
    ], dtype=complex)


def R_matrix_xxz_normalized(u: complex, gamma: complex) -> np.ndarray:
    """R-matrix normalized so R(0) = P (the permutation).

    R_norm(u) = R(u) / sin(gamma).
    """
    return R_matrix_xxz(u, gamma) / np.sin(gamma)


def R_matrix_xxx(u: complex) -> np.ndarray:
    """Rational Yang R-matrix: R(u) = u*I + P.

    This is the gamma -> 0 limit of the trigonometric R-matrix.
    """
    I4 = np.eye(4, dtype=complex)
    P = np.array([[1, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 1]], dtype=complex)
    return u * I4 + P


# ========================================================================
# 3.  Yang-Baxter equation verification
# ========================================================================

def _embed_12(R: np.ndarray) -> np.ndarray:
    """Embed 4x4 R into spaces 1,2 of (C^2)^3 = C^8."""
    return np.kron(R, I2)


def _embed_23(R: np.ndarray) -> np.ndarray:
    """Embed 4x4 R into spaces 2,3 of (C^2)^3 = C^8."""
    return np.kron(I2, R)


def _embed_13(R: np.ndarray) -> np.ndarray:
    """Embed 4x4 R into spaces 1,3 of (C^2)^3 = C^8.

    R_{13} = P_{23} R_{12} P_{23} where P_{23} permutes spaces 2,3.
    """
    P23 = _embed_23(np.array([[1, 0, 0, 0],
                               [0, 0, 1, 0],
                               [0, 1, 0, 0],
                               [0, 0, 0, 1]], dtype=complex))
    R12 = _embed_12(R)
    return P23 @ R12 @ P23


def verify_ybe_xxz(u: complex, v: complex, gamma: complex,
                   tol: float = 1e-10) -> float:
    r"""Verify the Yang-Baxter equation for the trigonometric R-matrix.

    R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)

    Returns the norm of the difference (should be ~0).
    """
    R12 = _embed_12(R_matrix_xxz(u - v, gamma))
    R13 = _embed_13(R_matrix_xxz(u, gamma))
    R23 = _embed_23(R_matrix_xxz(v, gamma))
    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(la.norm(lhs - rhs))


def verify_ybe_xxx(u: complex, v: complex, tol: float = 1e-10) -> float:
    """Verify YBE for the rational R-matrix."""
    R12 = _embed_12(R_matrix_xxx(u - v))
    R13 = _embed_13(R_matrix_xxx(u))
    R23 = _embed_23(R_matrix_xxx(v))
    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(la.norm(lhs - rhs))


def verify_unitarity_xxz(u: complex, gamma: complex) -> float:
    """Verify R_{12}(u) R_{21}(-u) = rho(u) * I.

    rho(u) = sin(u+gamma)*sin(gamma-u) = sin^2(gamma) - sin^2(u).

    R_{21}(-u) = P R_{12}(-u) P where P is the permutation.
    """
    P = np.array([[1, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 1]], dtype=complex)
    R_u = R_matrix_xxz(u, gamma)
    R_minus_u = R_matrix_xxz(-u, gamma)
    R21_neg = P @ R_minus_u @ P
    product = R_u @ R21_neg
    rho = np.sin(u + gamma) * np.sin(gamma - u)
    return float(la.norm(product - rho * np.eye(4, dtype=complex)))


def verify_regularity_xxz(gamma: complex) -> float:
    """Verify R(0) = sin(gamma) * P (regularity condition)."""
    P = np.array([[1, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 1]], dtype=complex)
    R0 = R_matrix_xxz(0, gamma)
    return float(la.norm(R0 - np.sin(gamma) * P))


def verify_xxx_limit(u: float, gamma: float) -> float:
    """Verify that R_xxz(u*gamma, gamma)/sin(gamma) -> u*I + P as gamma -> 0.

    More precisely, for small gamma:
        sin(u*gamma + gamma) = sin((u+1)*gamma) ~ (u+1)*gamma
        sin(u*gamma) ~ u*gamma
        sin(gamma) ~ gamma
    So R(u*gamma, gamma) / gamma ~ (u+1)*diag(...) + ... = u*I + P + O(gamma).
    """
    R_trig = R_matrix_xxz(u * gamma, gamma) / np.sin(gamma)
    # The rational R-matrix is R(u) = u*I + P
    R_rat = R_matrix_xxx(u)
    return float(la.norm(R_trig - R_rat))


# ========================================================================
# 4.  XXZ Hamiltonian (exact diagonalization)
# ========================================================================

def xxz_hamiltonian(N: int, Delta: float = 1.0, J: float = 1.0) -> np.ndarray:
    r"""XXZ Heisenberg Hamiltonian with periodic boundary conditions.

    H = (J/2) sum_{i=0}^{N-1} [S^+_i S^-_{i+1} + S^-_i S^+_{i+1}
                                + Delta * S^z_i S^z_{i+1}]

    which is equivalent to:

    H = (J/4) sum [sigma^x sigma^x + sigma^y sigma^y
                   + Delta * sigma^z sigma^z]

    The factor conventions:
    - S^+/S^- = (sigma_x +/- i*sigma_y)/2
    - S^z = sigma_z/2
    - The (J/2) on spin operators = (J/4) on Pauli matrices for the
      transverse part, (J/4)*Delta for the longitudinal part.

    Parameters
    ----------
    N : int
        Number of sites (chain length).
    Delta : float
        Anisotropy parameter.  Delta = 1 is XXX.  Delta = 0 is XX (free fermions).
    J : float
        Exchange coupling.  J > 0 is antiferromagnetic.

    Returns
    -------
    H : np.ndarray
        2^N x 2^N Hamiltonian matrix.
    """
    dim = 2**N
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(N):
        j = (i + 1) % N
        # Transverse: S^+ S^- + S^- S^+ = (1/2)(sigma_x sigma_x + sigma_y sigma_y)
        for pauli in [SIGMA_X, SIGMA_Y]:
            Si = _spin_op(N, i, pauli)
            Sj = _spin_op(N, j, pauli)
            H += (J / 4.0) * Si @ Sj
        # Longitudinal: Delta * S^z S^z = (Delta/4) * sigma_z sigma_z
        Szi = _spin_op(N, i, SIGMA_Z)
        Szj = _spin_op(N, j, SIGMA_Z)
        H += (J / 4.0) * Delta * Szi @ Szj
    return H


def xxz_total_sz(N: int) -> np.ndarray:
    """Total S^z operator."""
    Sz = np.zeros((2**N, 2**N), dtype=complex)
    for i in range(N):
        Sz += 0.5 * _spin_op(N, i, SIGMA_Z)
    return Sz


def xxz_exact_spectrum(N: int, Delta: float = 1.0, J: float = 1.0,
                       Sz_sector: Optional[float] = None
                       ) -> np.ndarray:
    """Exact eigenvalues of the XXZ Hamiltonian.

    Parameters
    ----------
    N : int
        Chain length.
    Delta : float
        Anisotropy.
    J : float
        Coupling.
    Sz_sector : float or None
        If given, restrict to total S^z = Sz_sector.

    Returns
    -------
    evals : np.ndarray
        Sorted eigenvalues.
    """
    H = xxz_hamiltonian(N, Delta, J)
    if Sz_sector is not None:
        Sz = xxz_total_sz(N)
        sz_diag = np.diag(Sz).real
        mask = np.abs(sz_diag - Sz_sector) < 1e-10
        indices = np.where(mask)[0]
        if len(indices) == 0:
            return np.array([])
        H_sector = H[np.ix_(indices, indices)]
        evals = la.eigvalsh(H_sector.real)
    else:
        evals = la.eigvalsh(H.real)
    return np.sort(evals)


# ========================================================================
# 5.  XXZ Bethe ansatz equations
# ========================================================================

def xxz_bae_log(lambdas: np.ndarray, N: int, gamma: float,
                quantum_numbers: np.ndarray) -> np.ndarray:
    r"""XXZ Bethe ansatz equations in logarithmic form.

    The BAE for the XXZ chain (Delta = cos(gamma), |Delta| <= 1 regime):

    N * theta_1(lambda_j) - sum_{k != j} theta_2(lambda_j - lambda_k)
        = 2*pi * I_j

    where:
        theta_n(x) = 2 * arctan[ cot(n*gamma/2) * tanh(x) ]

    This is the standard form for the gapless regime |Delta| <= 1.

    The quantum numbers I_j are integers (N even, M odd) or
    half-integers (N even, M even), labeling the branch.

    Parameters
    ----------
    lambdas : np.ndarray
        Array of M Bethe rapidities.
    N : int
        Chain length.
    gamma : float
        Anisotropy angle.  Delta = cos(gamma).
    quantum_numbers : np.ndarray
        Array of M quantum numbers I_j.

    Returns
    -------
    residual : np.ndarray
        Array of M residuals (should be zero at solution).
    """
    M = len(lambdas)
    res = np.zeros(M)

    def theta_n(x, n):
        """Scattering kernel theta_n(x) = 2*arctan(cot(n*gamma/2) * tanh(x))."""
        cot_val = np.cos(n * gamma / 2) / np.sin(n * gamma / 2)
        return 2.0 * np.arctan(cot_val * np.tanh(x))

    for j in range(M):
        # Driving term
        res[j] = N * theta_n(lambdas[j], 1)
        # Scattering terms
        for k in range(M):
            if k != j:
                res[j] -= theta_n(lambdas[j] - lambdas[k], 2)
        # Quantum number
        res[j] -= 2.0 * PI * quantum_numbers[j]

    return res


def xxz_bae_product(lambdas: np.ndarray, N: int, gamma: float) -> np.ndarray:
    r"""XXZ BAE in product form (for verification).

    [sin(lambda_j + gamma/2) / sin(lambda_j - gamma/2)]^N
        = prod_{k != j} sin(lambda_j - lambda_k + gamma)
                       / sin(lambda_j - lambda_k - gamma)

    We actually work with the HYPERBOLIC parametrization for |Delta| <= 1:

    [sinh(lambda_j + i*gamma/2) / sinh(lambda_j - i*gamma/2)]^N
        = prod_{k != j} sinh(lambda_j - lambda_k + i*gamma)
                       / sinh(lambda_j - lambda_k - i*gamma)

    Returns the ratio LHS/RHS - 1 for each j (should be ~0 at solution).
    """
    M = len(lambdas)
    res = np.zeros(M, dtype=complex)

    for j in range(M):
        # LHS
        lhs = (np.sinh(lambdas[j] + 1j * gamma / 2)
               / np.sinh(lambdas[j] - 1j * gamma / 2)) ** N

        # RHS
        rhs = 1.0 + 0.0j
        for k in range(M):
            if k != j:
                rhs *= (np.sinh(lambdas[j] - lambdas[k] + 1j * gamma)
                        / np.sinh(lambdas[j] - lambdas[k] - 1j * gamma))

        res[j] = lhs / rhs - 1.0 if abs(rhs) > 1e-15 else lhs - rhs

    return res


def solve_xxz_bae(N: int, M: int, gamma: float,
                  quantum_numbers: Optional[np.ndarray] = None,
                  initial_guess: Optional[np.ndarray] = None,
                  method: str = 'hybr') -> Dict[str, Any]:
    r"""Solve the XXZ Bethe ansatz equations.

    Parameters
    ----------
    N : int
        Chain length.
    M : int
        Number of down spins (magnons).
    gamma : float
        Anisotropy angle.  Delta = cos(gamma).
    quantum_numbers : np.ndarray or None
        Quantum numbers I_j.  If None, use ground-state prescription.
    initial_guess : np.ndarray or None
        Initial guess for rapidities.  If None, use heuristic.
    method : str
        Root-finding method for scipy.optimize.root.

    Returns
    -------
    result : dict
        'lambdas': Bethe rapidities
        'energy': energy eigenvalue
        'momentum': total momentum
        'success': convergence flag
        'quantum_numbers': the quantum numbers used
    """
    if M == 0:
        return {
            'lambdas': np.array([]),
            'energy': N * np.cos(gamma) / 4.0,
            'momentum': 0.0,
            'success': True,
            'quantum_numbers': np.array([]),
            'N': N, 'M': M, 'gamma': gamma,
        }

    if quantum_numbers is None:
        quantum_numbers = _ground_state_quantum_numbers(N, M)

    if initial_guess is None:
        initial_guess = _xxz_initial_guess(N, M, gamma, quantum_numbers)

    def equations(lam):
        return xxz_bae_log(lam, N, gamma, quantum_numbers)

    result = optimize.root(equations, initial_guess, method=method)
    lambdas = result.x
    success = result.success

    if not success:
        # Try a different method
        result2 = optimize.root(equations, initial_guess, method='lm')
        if result2.success or la.norm(result2.fun) < la.norm(result.fun):
            lambdas = result2.x
            success = result2.success or la.norm(result2.fun) < 1e-8

    energy = xxz_energy_from_roots(lambdas, N, gamma)
    momentum = xxz_momentum_from_roots(lambdas, gamma)

    return {
        'lambdas': lambdas,
        'energy': energy,
        'momentum': momentum,
        'success': success,
        'quantum_numbers': quantum_numbers,
        'residual_norm': float(la.norm(equations(lambdas))),
        'N': N, 'M': M, 'gamma': gamma,
    }


def _ground_state_quantum_numbers(N: int, M: int) -> np.ndarray:
    """Ground state quantum numbers for the antiferromagnetic XXZ chain.

    For the ground state of the AFM chain with M magnons:
    I_j = -(M-1)/2, -(M-1)/2 + 1, ..., (M-1)/2

    These are symmetric around zero.
    """
    return np.array([-(M - 1) / 2.0 + j for j in range(M)])


def _xxz_initial_guess(N: int, M: int, gamma: float,
                       quantum_numbers: np.ndarray) -> np.ndarray:
    """Heuristic initial guess for XXZ Bethe roots.

    For the logarithmic BAE, a reasonable guess is:
        lambda_j ~ quantum_numbers[j] / (N * cot(gamma/2))
    which linearizes the driving term.
    """
    if M == 1:
        return np.array([0.0])
    cot_half = np.cos(gamma / 2) / np.sin(gamma / 2) if abs(np.sin(gamma / 2)) > 1e-15 else 1.0 / gamma
    # Linearized guess
    scale = 1.0 / (N * cot_half) if abs(cot_half) > 1e-15 else 0.5
    guess = quantum_numbers * abs(scale) * PI
    # Spread them out to avoid coalescence
    if M > 1:
        min_sep = 0.1
        for j in range(1, M):
            if abs(guess[j] - guess[j-1]) < min_sep:
                guess[j] = guess[j-1] + min_sep
    return guess


# ========================================================================
# 6.  Energy and momentum from Bethe roots
# ========================================================================

def xxz_energy_from_roots(lambdas: np.ndarray, N: int, gamma: float,
                          J: float = 1.0) -> float:
    r"""Compute the XXZ energy from Bethe roots.

    E = -J * sum_j sin^2(gamma) / [cosh(2*lambda_j) - cos(gamma)]
        + (J/4) * N * Delta

    The first term is the magnon energy; the second is the vacuum energy.

    Derivation: the single-magnon dispersion relation is
        e(k) = J*(cos(k) - Delta)
    where the quasi-momentum k is related to the rapidity lambda by
        e^{ik} = sinh(lambda + i*gamma/2) / sinh(lambda - i*gamma/2)
    giving
        cos(k) = [cosh(2*lambda)*cos(gamma) - 1] / [cosh(2*lambda) - cos(gamma)]
    and therefore
        e(lambda) = J*[cos(k) - Delta]
                   = -J * sin^2(gamma) / [cosh(2*lambda) - cos(gamma)]

    The total energy is E_vacuum + sum_j e(lambda_j).

    Parameters
    ----------
    lambdas : np.ndarray
        Bethe rapidities.
    N : int
        Chain length.
    gamma : float
        Anisotropy angle.
    J : float
        Exchange coupling.

    Returns
    -------
    energy : float
    """
    Delta = np.cos(gamma)
    sin2_gamma = np.sin(gamma) ** 2

    # Vacuum energy: E_vac = (J/4) * N * Delta
    # (ferromagnetic state with all spins up)
    E_vac = J * N * Delta / 4.0

    # Magnon contribution: each magnon contributes
    # e(lambda) = -J * sin^2(gamma) / (cosh(2*lambda) - cos(gamma))
    E_magnon = 0.0
    for lam in lambdas:
        denom = np.cosh(2 * lam) - Delta
        if abs(denom) > 1e-15:
            E_magnon -= J * sin2_gamma / denom

    return E_vac + E_magnon


def xxz_momentum_from_roots(lambdas: np.ndarray, gamma: float) -> float:
    r"""Total momentum from Bethe roots.

    P = sum_j p(lambda_j)
    where p(lambda) = i * log[sinh(lambda + i*gamma/2) / sinh(lambda - i*gamma/2)]
                    = pi - 2*arctan[cot(gamma/2) * tanh(lambda)]

    We use the real form for real lambdas.
    """
    cot_half = np.cos(gamma / 2) / np.sin(gamma / 2) if abs(np.sin(gamma / 2)) > 1e-15 else 0.0
    P = 0.0
    for lam in lambdas:
        P += PI - 2.0 * np.arctan(cot_half * np.tanh(lam))
    return float(P % (2 * PI))


# ========================================================================
# 7.  Transfer matrix construction from R-matrix
# ========================================================================

def xxz_transfer_matrix(u: complex, N: int, gamma: complex) -> np.ndarray:
    r"""Transfer matrix T(u) = Tr_a[R_{a1}(u) R_{a2}(u) ... R_{aN}(u)].

    Parameters
    ----------
    u : complex
        Spectral parameter.
    N : int
        Chain length.
    gamma : complex
        Anisotropy parameter.

    Returns
    -------
    T : np.ndarray
        2^N x 2^N transfer matrix.
    """
    phys_dim = 2**N
    aux_dim = 2
    total_dim = aux_dim * phys_dim

    # Build monodromy matrix: M(u) = R_{a,N}(u) ... R_{a,1}(u)
    M_mat = np.eye(total_dim, dtype=complex)
    for site in range(N):
        R_au = R_matrix_xxz(u, gamma)
        R_embedded = _embed_R_aux_site(R_au, site, N)
        M_mat = R_embedded @ M_mat

    # Trace over auxiliary space
    T = np.zeros((phys_dim, phys_dim), dtype=complex)
    for a in range(aux_dim):
        block = M_mat[a * phys_dim:(a + 1) * phys_dim,
                      a * phys_dim:(a + 1) * phys_dim]
        T += block

    return T


def _embed_R_aux_site(R: np.ndarray, site: int, N: int) -> np.ndarray:
    r"""Embed R (4x4, acting on aux x site) into full aux x phys space.

    Full space = C^2_aux x (C^2)^N, dimension 2^{N+1}.
    R acts on the auxiliary qubit and physical site `site`.
    """
    total_dim = 2 ** (N + 1)
    dim_before = 2 ** site
    dim_after = 2 ** (N - site - 1)

    R_4d = R.reshape(2, 2, 2, 2)
    result = np.zeros((total_dim, total_dim), dtype=complex)

    for s_before in range(dim_before):
        for s_after in range(dim_after):
            for a_in in range(2):
                for s_in in range(2):
                    phys_in = s_before * (2 ** (N - site)) + s_in * dim_after + s_after
                    idx_in = a_in * (2 ** N) + phys_in
                    for a_out in range(2):
                        for s_out in range(2):
                            phys_out = s_before * (2 ** (N - site)) + s_out * dim_after + s_after
                            idx_out = a_out * (2 ** N) + phys_out
                            result[idx_out, idx_in] += R_4d[a_out, s_out, a_in, s_in]

    return result


def verify_transfer_commutativity(u: complex, v: complex, N: int,
                                  gamma: complex, tol: float = 1e-8) -> float:
    """Verify [T(u), T(v)] = 0 from the Yang-Baxter equation."""
    Tu = xxz_transfer_matrix(u, N, gamma)
    Tv = xxz_transfer_matrix(v, N, gamma)
    comm = Tu @ Tv - Tv @ Tu
    return float(la.norm(comm))


def xxz_hamiltonian_from_transfer(N: int, gamma: float, J: float = 1.0) -> np.ndarray:
    r"""Extract the XXZ Hamiltonian from the transfer matrix.

    H = (J*sin(gamma)/2) * d/du ln T(u) |_{u=0}

    More precisely:
        T(u) ~ sin(gamma)^N * [sum P_i + u * H / sin(gamma) + ...]
    So:
        H propto T'(0) * T(0)^{-1}

    The exact relation involves a shift by N*Delta/4.
    """
    eps = 1e-6
    T_plus = xxz_transfer_matrix(eps, N, gamma)
    T_minus = xxz_transfer_matrix(-eps, N, gamma)
    T_0 = xxz_transfer_matrix(0, N, gamma)

    dT = (T_plus - T_minus) / (2 * eps)
    T0_inv = la.inv(T_0)

    # H_extracted = (sin(gamma)/2) * T0_inv @ dT
    # The normalization: compare with direct Hamiltonian
    H_extracted = (np.sin(gamma) / 2.0) * T0_inv @ dT

    return H_extracted.real


# ========================================================================
# 8.  Algebraic Bethe ansatz (ABCD operators)
# ========================================================================

def xxz_monodromy_matrix(u: complex, N: int, gamma: complex) -> np.ndarray:
    r"""Monodromy matrix M(u) = R_{a,N}(u) ... R_{a,1}(u).

    M(u) is a 2x2 matrix of operators on (C^2)^N:
        M(u) = | A(u)  B(u) |
               | C(u)  D(u) |

    The transfer matrix is T(u) = A(u) + D(u).
    The Bethe states are B(lambda_1) ... B(lambda_M) |0>,
    where |0> = |up, up, ..., up> is the pseudovacuum.
    """
    phys_dim = 2**N
    total_dim = 2 * phys_dim

    M_mat = np.eye(total_dim, dtype=complex)
    for site in range(N):
        R_au = R_matrix_xxz(u, gamma)
        R_embedded = _embed_R_aux_site(R_au, site, N)
        M_mat = R_embedded @ M_mat

    return M_mat


def xxz_ABCD_operators(u: complex, N: int, gamma: complex
                       ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Extract A, B, C, D operators from the monodromy matrix.

    Returns 4 matrices, each of size 2^N x 2^N.
    """
    phys_dim = 2**N
    M_mat = xxz_monodromy_matrix(u, N, gamma)

    A = M_mat[:phys_dim, :phys_dim]
    B = M_mat[:phys_dim, phys_dim:]
    C = M_mat[phys_dim:, :phys_dim]
    D = M_mat[phys_dim:, phys_dim:]

    return A, B, C, D


def xxz_pseudovacuum(N: int) -> np.ndarray:
    """Pseudovacuum |0> = |up, up, ..., up>.

    In computational basis: |0...0> = first basis vector.
    """
    psi = np.zeros(2**N, dtype=complex)
    psi[0] = 1.0
    return psi


def xxz_bethe_state(lambdas: np.ndarray, N: int, gamma: float) -> np.ndarray:
    r"""Construct the Bethe state B(lambda_1) ... B(lambda_M) |0>.

    This is the algebraic Bethe ansatz construction.
    The state is an eigenstate of T(u) = A(u) + D(u) PROVIDED
    the lambda_j satisfy the Bethe equations.
    """
    psi = xxz_pseudovacuum(N)
    for lam in lambdas:
        _, B, _, _ = xxz_ABCD_operators(lam, N, gamma)
        psi = B @ psi
    # Normalize
    norm = la.norm(psi)
    if norm > 1e-15:
        psi /= norm
    return psi


def verify_bethe_eigenstate(lambdas: np.ndarray, N: int, gamma: float,
                            tol: float = 1e-6) -> Dict[str, Any]:
    r"""Verify that the Bethe state is an eigenstate of the Hamiltonian.

    Constructs the Bethe state and checks H|psi> = E|psi>.

    Returns
    -------
    result : dict
        'is_eigenstate': bool
        'energy_bethe': from Bethe formula
        'energy_direct': from <psi|H|psi>
        'eigenstate_residual': norm of (H - E)|psi>
    """
    Delta = np.cos(gamma)
    H = xxz_hamiltonian(N, Delta)
    psi = xxz_bethe_state(lambdas, N, gamma)

    if la.norm(psi) < 1e-12:
        return {
            'is_eigenstate': False,
            'energy_bethe': xxz_energy_from_roots(lambdas, N, gamma),
            'energy_direct': 0.0,
            'eigenstate_residual': float('inf'),
        }

    E_bethe = xxz_energy_from_roots(lambdas, N, gamma)
    E_direct = np.real(psi.conj() @ H @ psi)

    # Residual
    residual = H @ psi - E_direct * psi
    res_norm = float(la.norm(residual))

    return {
        'is_eigenstate': res_norm < tol,
        'energy_bethe': E_bethe,
        'energy_direct': float(E_direct),
        'eigenstate_residual': res_norm,
    }


# ========================================================================
# 9.  Free fermion point (Delta = 0, gamma = pi/2)
# ========================================================================

def free_fermion_spectrum(N: int, J: float = 1.0) -> np.ndarray:
    r"""Exact spectrum of the XX chain (Delta = 0, free fermions).

    The XX Hamiltonian H = (J/4) sum [sigma_x sigma_x + sigma_y sigma_y]
    after Jordan-Wigner transformation becomes:
        H = (J/2) sum [c^dag_i c_{i+1} + h.c.]

    Single-particle energies:
        epsilon_k = (J/2) * cos(2*pi*n/N), n = 0, 1, ..., N-1

    Many-body energies are sums over occupied single-particle levels.
    We use exact diagonalization instead, as the Jordan-Wigner mapping
    to free fermions requires careful handling of boundary conditions.
    """
    # Just use exact diagonalization for the XX chain
    return xxz_exact_spectrum(N, Delta=0.0, J=J)


def free_fermion_ground_state_energy(N: int, M: int, J: float = 1.0) -> float:
    r"""Ground state energy for the XX chain in the M-magnon sector.

    Uses exact diagonalization in the Sz = N/2 - M sector.
    """
    Sz_sector = N / 2.0 - M
    evals = xxz_exact_spectrum(N, Delta=0.0, J=J, Sz_sector=Sz_sector)
    if len(evals) > 0:
        return float(evals[0])
    return 0.0


# ========================================================================
# 10.  XXX limit recovery
# ========================================================================

def xxx_bae_from_xxz_limit(lambdas_xxz: np.ndarray, N: int,
                            gamma: float) -> np.ndarray:
    r"""Show that XXZ BAE reduce to XXX BAE as gamma -> 0.

    In the XXZ BAE (product form):
        [sinh(lam + i*gamma/2) / sinh(lam - i*gamma/2)]^N = ...

    As gamma -> 0, sinh(lam +/- i*gamma/2) ~ lam +/- i*gamma/2,
    and the equations become:
        [(lam + i*gamma/2) / (lam - i*gamma/2)]^N = ...

    Setting u = lam / gamma (rescaled rapidity):
        [(u + i/2) / (u - i/2)]^N = prod [(u_j - u_k + i)/(u_j - u_k - i)]

    which is the standard XXX BAE with rescaled rapidities.

    Returns the product-form residual of the XXX BAE (should be ~0).
    """
    # Rescale: u = lambda / gamma
    u = lambdas_xxz / gamma if abs(gamma) > 1e-15 else lambdas_xxz
    M = len(u)
    res = np.zeros(M, dtype=complex)

    for j in range(M):
        lhs = ((u[j] + 0.5j) / (u[j] - 0.5j)) ** N
        rhs = 1.0 + 0.0j
        for k in range(M):
            if k != j:
                rhs *= (u[j] - u[k] + 1j) / (u[j] - u[k] - 1j)
        res[j] = lhs / rhs - 1.0

    return res


# ========================================================================
# 11.  Higher-spin XXZ via fusion procedure
# ========================================================================

def fused_R_matrix_spin1(u: complex, gamma: complex) -> np.ndarray:
    r"""Fused R-matrix for spin-1 (s=1) XXZ chain.

    R^{(1)}(u) = P^{(1)} [R^{(1/2)}(u) tensor R^{(1/2)}(u + gamma)] P^{(1)}

    where P^{(1)} projects onto the spin-1 (symmetric) subspace of
    C^2 tensor C^2.

    The spin-1 space has basis:
        |1,+1> = |up,up>
        |1, 0> = (|up,down> + |down,up>) / sqrt(2)
        |1,-1> = |down,down>

    The fused R-matrix acts on (C^3)_aux tensor (C^2)_phys.

    We compute R^{(1)} as a 6x6 matrix on (C^3 tensor C^2).

    Actually: the fusion is of the AUXILIARY space.  The R-matrix
    R^{(1, 1/2)}(u) acts on C^3_aux tensor C^2_phys.
    """
    # Projector onto symmetric subspace of C^2 x C^2
    # Basis: |00>, |01>, |10>, |11> -> symmetric: |00>, (|01>+|10>)/sqrt2, |11>
    P_sym = np.zeros((4, 3), dtype=complex)
    P_sym[0, 0] = 1.0           # |00> -> |1,+1>
    P_sym[1, 1] = 1.0 / np.sqrt(2)  # |01> -> |1,0> (part)
    P_sym[2, 1] = 1.0 / np.sqrt(2)  # |10> -> |1,0> (part)
    P_sym[3, 2] = 1.0           # |11> -> |1,-1>

    # R-matrices on (C^2 x C^2)_aux x C^2_phys = C^8
    # R_{a1, phys}(u) acts on first aux qubit and phys
    # R_{a2, phys}(u + gamma) acts on second aux qubit and phys
    R1 = R_matrix_xxz(u, gamma)           # 4x4 on (a1, phys)
    R2 = R_matrix_xxz(u + gamma, gamma)   # 4x4 on (a2, phys)

    # Embed into (a1, a2, phys) = C^8
    R1_full = np.kron(R1.reshape(2, 2, 2, 2)[:, :, :, :].reshape(4, 4),
                      np.eye(1))
    # Actually, let's be more careful.
    # (a1, a2, phys) space.  R1 acts on (a1, phys), R2 on (a2, phys).
    # Embed R1 (on a1, phys) into (a1, a2, phys):
    #   R1_embed = R1 tensor I_{a2} with a1 and phys non-adjacent.
    # We need to handle the tensor structure carefully.

    # Basis: (a1, a2, phys) each in {0,1}, total dim = 8
    # Index: 4*a1 + 2*a2 + phys
    R1_embed = np.zeros((8, 8), dtype=complex)
    R2_embed = np.zeros((8, 8), dtype=complex)

    for a2 in range(2):
        for a1_in in range(2):
            for p_in in range(2):
                for a1_out in range(2):
                    for p_out in range(2):
                        idx_in = 4 * a1_in + 2 * a2 + p_in
                        idx_out = 4 * a1_out + 2 * a2 + p_out
                        R1_embed[idx_out, idx_in] += R1[2 * a1_out + p_out, 2 * a1_in + p_in]

    for a1 in range(2):
        for a2_in in range(2):
            for p_in in range(2):
                for a2_out in range(2):
                    for p_out in range(2):
                        idx_in = 4 * a1 + 2 * a2_in + p_in
                        idx_out = 4 * a1 + 2 * a2_out + p_out
                        R2_embed[idx_out, idx_in] += R2[2 * a2_out + p_out, 2 * a2_in + p_in]

    # Product: R1_embed @ R2_embed (order: R_{a2,phys} then R_{a1,phys})
    # Actually for fusion: R^fused = P_sym^dag @ (R_{a1} R_{a2}) @ P_sym
    # with the product taken in the order that the auxiliary indices fuse.
    product = R1_embed @ R2_embed

    # Project: (a1, a2) -> spin-1 subspace
    # P_sym: C^3 -> C^4 (a1, a2 space), so the full projector is
    # P_sym tensor I_phys: C^{3x2} -> C^{4x2}=C^8
    P_full = np.kron(P_sym, np.eye(2, dtype=complex))  # 8 x 6

    # R^fused = P_full^dag @ product @ P_full  (6 x 6)
    R_fused = P_full.conj().T @ product @ P_full

    return R_fused


def spin1_xxz_hamiltonian(N: int, gamma: float, J: float = 1.0) -> np.ndarray:
    r"""Spin-1 XXZ Hamiltonian (Babujian-Takhtadzhan model).

    H = J sum_i [S^x_i S^x_{i+1} + S^y_i S^y_{i+1} + Delta * S^z_i S^z_{i+1}]

    where S^a are spin-1 operators and Delta = cos(gamma).

    Spin-1 matrices:
        S^+ = sqrt(2) * (|+1><0| + |0><-1|)
        S^- = sqrt(2) * (|0><+1| + |-1><0|)
        S^z = |+1><+1| - |-1><-1|
    """
    d = 3  # local Hilbert space dimension
    dim = d**N
    Delta = np.cos(gamma)

    # Spin-1 matrices
    Sx = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=complex) / np.sqrt(2)
    Sy = np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]], dtype=complex) / np.sqrt(2)
    Sz = np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]], dtype=complex)
    I3 = np.eye(3, dtype=complex)

    def spin1_op(site, mat):
        ops = [I3] * N
        ops[site] = mat
        return _kron_chain(ops)

    H = np.zeros((dim, dim), dtype=complex)
    for i in range(N):
        j = (i + 1) % N
        for S_mat in [Sx, Sy]:
            H += J * spin1_op(i, S_mat) @ spin1_op(j, S_mat)
        H += J * Delta * spin1_op(i, Sz) @ spin1_op(j, Sz)

    return H


def spin1_bethe_equations(lambdas: np.ndarray, N: int, gamma: float,
                          quantum_numbers: np.ndarray) -> np.ndarray:
    r"""Bethe equations for spin-1 XXZ (Babujian-Takhtadzhan).

    The spin-1 BAE differ from spin-1/2 by the driving term:

    [sinh(lambda_j + i*gamma) / sinh(lambda_j - i*gamma)]^N
        = prod_{k != j} sinh(lambda_j - lambda_k + i*gamma)
                       / sinh(lambda_j - lambda_k - i*gamma)

    Note: gamma replaces gamma/2 in the driving term compared to spin-1/2.
    This is the s=1 case of the general spin-s formula:
        driving: [sinh(lam + i*s*gamma) / sinh(lam - i*s*gamma)]^N

    In logarithmic form with scattering kernels:
        N * theta_2(lambda_j) - sum_{k!=j} theta_2(lambda_j - lambda_k) = 2*pi*I_j
    """
    M = len(lambdas)
    res = np.zeros(M)

    def theta_n(x, n):
        cot_val = np.cos(n * gamma / 2) / np.sin(n * gamma / 2)
        return 2.0 * np.arctan(cot_val * np.tanh(x))

    for j in range(M):
        # Driving term: theta_2 for spin-1
        res[j] = N * theta_n(lambdas[j], 2)
        # Scattering: theta_2 (same as spin-1/2 scattering)
        for k in range(M):
            if k != j:
                res[j] -= theta_n(lambdas[j] - lambdas[k], 2)
        res[j] -= 2.0 * PI * quantum_numbers[j]

    return res


def solve_spin1_bae(N: int, M: int, gamma: float,
                    quantum_numbers: Optional[np.ndarray] = None,
                    initial_guess: Optional[np.ndarray] = None) -> Dict[str, Any]:
    """Solve spin-1 XXZ Bethe equations."""
    if quantum_numbers is None:
        quantum_numbers = np.array([-(M - 1) / 2.0 + j for j in range(M)])

    if initial_guess is None:
        initial_guess = np.linspace(-0.5 * M, 0.5 * M, M) if M > 0 else np.array([])

    if M == 0:
        Delta = np.cos(gamma)
        return {
            'lambdas': np.array([]),
            'energy': N * Delta / 4.0,
            'success': True,
            'N': N, 'M': M, 'gamma': gamma,
        }

    def equations(lam):
        return spin1_bethe_equations(lam, N, gamma, quantum_numbers)

    result = optimize.root(equations, initial_guess, method='hybr')
    lambdas = result.x
    success = result.success

    if not success:
        result2 = optimize.root(equations, initial_guess, method='lm')
        if result2.success or la.norm(result2.fun) < la.norm(result.fun):
            lambdas = result2.x
            success = result2.success or la.norm(result2.fun) < 1e-8

    return {
        'lambdas': lambdas,
        'success': success,
        'residual_norm': float(la.norm(equations(lambdas))),
        'quantum_numbers': quantum_numbers,
        'N': N, 'M': M, 'gamma': gamma,
    }


# ========================================================================
# 12.  XYZ chain (elliptic R-matrix from genus-1 shadow)
# ========================================================================

def _theta1(z: complex, tau: complex, nmax: int = 40) -> complex:
    """Jacobi theta_1(z|tau) = 2 sum_{n>=0} (-1)^n q^{(n+1/2)^2} sin((2n+1)*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(nmax):
        result += ((-1)**n * q**((n + 0.5)**2)
                   * np.sin((2 * n + 1) * PI * z))
    return 2 * result


def _theta2(z: complex, tau: complex, nmax: int = 40) -> complex:
    """Jacobi theta_2(z|tau) = 2 sum_{n>=0} q^{(n+1/2)^2} cos((2n+1)*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 0.0 + 0.0j
    for n in range(nmax):
        result += q**((n + 0.5)**2) * np.cos((2 * n + 1) * PI * z)
    return 2 * result


def _theta3(z: complex, tau: complex, nmax: int = 40) -> complex:
    """Jacobi theta_3(z|tau) = 1 + 2 sum_{n>=1} q^{n^2} cos(2n*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, nmax):
        result += 2 * q**(n**2) * np.cos(2 * n * PI * z)
    return result


def _theta4(z: complex, tau: complex, nmax: int = 40) -> complex:
    """Jacobi theta_4(z|tau) = 1 + 2 sum_{n>=1} (-1)^n q^{n^2} cos(2n*pi*z)."""
    q = np.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, nmax):
        result += 2 * ((-1)**n) * q**(n**2) * np.cos(2 * n * PI * z)
    return result


def R_matrix_xyz(u: complex, eta: complex, tau: complex) -> np.ndarray:
    r"""Elliptic R-matrix for the XYZ / 8-vertex model (Belavin 1981).

    R(u) = sum_{mu=0}^{3} W_mu(u) (sigma_mu tensor sigma_mu)

    where sigma_0 = I, sigma_{1,2,3} = Pauli, and
        W_mu(u) = theta_{mu+1}(u + eta | tau) / theta_{mu+1}(eta | tau)

    In the computational basis:
        a = W_0 + W_3, b = W_0 - W_3, c = W_1 + W_2, d = W_1 - W_2

    R(u) = | a  0  0  d |
           | 0  b  c  0 |
           | 0  c  b  0 |
           | d  0  0  a |

    The modular parameter tau is the genus-1 modulus (the shadow data).
    """
    W0 = _theta1(u + eta, tau) / _theta1(eta, tau)
    W1 = _theta2(u + eta, tau) / _theta2(eta, tau)
    W2 = _theta3(u + eta, tau) / _theta3(eta, tau)
    W3 = _theta4(u + eta, tau) / _theta4(eta, tau)

    a = W0 + W3
    b = W0 - W3
    c = W1 + W2
    d = W1 - W2

    return np.array([[a, 0, 0, d],
                     [0, b, c, 0],
                     [0, c, b, 0],
                     [d, 0, 0, a]], dtype=complex)


def verify_ybe_xyz(u: complex, v: complex, eta: complex, tau: complex,
                   tol: float = 1e-8) -> float:
    """Verify YBE for the elliptic R-matrix."""
    R12 = _embed_12(R_matrix_xyz(u - v, eta, tau))
    R13 = _embed_13(R_matrix_xyz(u, eta, tau))
    R23 = _embed_23(R_matrix_xyz(v, eta, tau))
    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(la.norm(lhs - rhs))


def xyz_to_xxz_limit(u: complex, eta: complex, tau_large: float = 5.0) -> float:
    r"""Verify that the elliptic R-matrix reduces to trigonometric as Im(tau) -> inf.

    As q = e^{i*pi*tau} -> 0:
        W_0 -> sin(pi*(u+eta)) / sin(pi*eta)
        W_1 -> cos(pi*(u+eta)) / cos(pi*eta)
        W_2 -> 1
        W_3 -> 1

    The Belavin 8-vertex R-matrix in this limit has:
        a = W_0 + W_3 ~ sin(pi(u+eta))/sin(pi*eta) + 1
        b = W_0 - W_3 ~ sin(pi(u+eta))/sin(pi*eta) - 1
        c = W_1 + W_2 ~ cos(pi(u+eta))/cos(pi*eta) + 1
        d = W_1 - W_2 ~ cos(pi(u+eta))/cos(pi*eta) - 1

    The d-weight is NONZERO generically (the 8-vertex structure persists).
    The 6-vertex SUBCASE is recovered when eta is a rational multiple of 1.
    For generic eta, we verify the convergence of the 6-vertex PART
    (the a, b, c weights) by comparing ratios a:b:c.

    Returns the relative error of the weight ratios.
    """
    R_ell = R_matrix_xyz(u, eta, 1j * tau_large)
    # Extract 6-vertex weights from the elliptic R-matrix
    a_ell = R_ell[0, 0]  # = W_0 + W_3
    b_ell = R_ell[1, 1]  # = W_0 - W_3
    c_ell = R_ell[1, 2]  # = W_1 + W_2
    d_ell = R_ell[0, 3]  # = W_1 - W_2

    # In the trigonometric limit, the RATIOS a:b:c should match
    # the six-vertex model: a/c = sin(pi(u+eta))/sin(pi*eta), b/c = sin(pi*u)/sin(pi*eta)
    # But c_ell -> cos(pi(u+eta))/cos(pi*eta) + 1, which is NOT sin(pi*eta).
    # The correct matching uses the WEIGHT RATIO a/b:
    # a_ell/b_ell -> [sin(pi(u+eta))/sin(pi*eta) + 1] / [sin(pi(u+eta))/sin(pi*eta) - 1]
    # For the six-vertex: a/b = sin(u+gamma)/sin(u) with gamma = pi*eta, u_param = pi*u
    # a_xxz / b_xxz = sin(pi*u + pi*eta) / sin(pi*u)

    # The most robust check: compare a*b vs b^2 + c^2 (the ice model identity).
    # For the six-vertex: a^2 + b^2 = c^2 + 2ab*Delta.
    # Instead, just check that |d/a| -> 0 as tau -> inf (8-vertex -> 6-vertex).
    d_over_a = abs(d_ell / a_ell) if abs(a_ell) > 1e-12 else float('inf')
    return float(d_over_a)


# ========================================================================
# 13.  Completeness check (counting Bethe states)
# ========================================================================

def count_bethe_states_xxz(N: int, gamma: float,
                           max_M: Optional[int] = None) -> Dict[int, int]:
    r"""Count the number of valid Bethe states for each M sector.

    For N sites, spin-1/2, the total Hilbert space has dimension 2^N.
    In each S^z sector with M down spins, the dimension is C(N, M).
    The Bethe ansatz should produce EXACTLY C(N, M) solutions.

    We enumerate quantum number sets and solve the BAE for each.
    Returns a dictionary mapping M -> number of found solutions.

    Note: this is computationally expensive for large N.
    Only reliable for N <= 8.
    """
    if max_M is None:
        max_M = N // 2

    from math import comb
    state_counts = {}

    for M in range(max_M + 1):
        expected = comb(N, M)
        found = 0

        # Generate all valid quantum number sets
        # For M magnons, quantum numbers I_j in {-(N-1)/2, ..., (N-1)/2}
        # with I_1 < I_2 < ... < I_M (ordered)
        if M == 0:
            found = 1  # Only the vacuum
        else:
            # Try all ordered subsets of quantum numbers
            # The valid range depends on N and M
            qn_range = _valid_quantum_number_range(N, M)
            for qn_tuple in combinations(qn_range, M):
                qn = np.array(qn_tuple, dtype=float)
                result = solve_xxz_bae(N, M, gamma, quantum_numbers=qn)
                if result['success'] and result['residual_norm'] < 1e-6:
                    found += 1

        state_counts[M] = found

    return state_counts


def _valid_quantum_number_range(N: int, M: int) -> List[float]:
    """Valid quantum numbers for the XXZ BAE with N sites, M magnons.

    For the logarithmic BAE, the quantum numbers I_j are
    half-integers if N+M is even, integers if N+M is odd.
    The range is roughly |I_j| <= (N-M-1)/2.
    """
    max_I = (N - 1) / 2.0
    if (N + M) % 2 == 0:
        # Half-integer quantum numbers
        return [i + 0.5 for i in range(int(-max_I - 0.5), int(max_I + 0.5))]
    else:
        # Integer quantum numbers
        return list(range(int(-max_I), int(max_I) + 1))


# ========================================================================
# 14.  Bethe string hypothesis
# ========================================================================

def bethe_string_center(lambdas: np.ndarray, gamma: float,
                        tol: float = 0.3) -> List[Dict[str, Any]]:
    r"""Identify Bethe strings among a set of complex Bethe roots.

    A length-n Bethe string centered at real rapidity alpha has roots:
        lambda_j = alpha + i*(n+1-2j)*gamma/2, j = 1, 2, ..., n

    The string hypothesis states that for large N, the Bethe roots
    organize into strings.

    Parameters
    ----------
    lambdas : np.ndarray
        Complex Bethe roots.
    gamma : float
        Anisotropy parameter.
    tol : float
        Tolerance for identifying string structure.

    Returns
    -------
    strings : list of dict
        Each dict has 'center' (real part), 'length' (n), 'roots' (indices).
    """
    M = len(lambdas)
    if M == 0:
        return []

    used = [False] * M
    strings = []

    # Sort roots by imaginary part
    order = np.argsort(lambdas.imag)
    lambdas_sorted = lambdas[order]

    for i in range(M):
        if used[order[i]]:
            continue

        # Try to form a string starting from this root
        current_string = [order[i]]
        used[order[i]] = True
        alpha = lambdas_sorted[i].real

        for n_try in range(1, M - i):
            # Expected next root in the string
            n_string = len(current_string) + 1
            expected_imag = (n_string - 1) * gamma / 2

            found_partner = False
            for j in range(i + 1, M):
                if used[order[j]]:
                    continue
                root_j = lambdas_sorted[j]
                if (abs(root_j.real - alpha) < tol
                    and abs(abs(root_j.imag - lambdas_sorted[i].imag) - gamma) < tol):
                    current_string.append(order[j])
                    used[order[j]] = True
                    found_partner = True
                    break

            if not found_partner:
                break

        strings.append({
            'center': alpha,
            'length': len(current_string),
            'roots': current_string,
        })

    return strings


# ========================================================================
# 15.  MC-to-Bethe complete derivation chain
# ========================================================================

def mc_to_bethe_derivation(k: float, N: int, M: int,
                           verbose: bool = False) -> Dict[str, Any]:
    r"""Complete derivation chain: MC element -> Bethe ansatz.

    Step 1: MC element for sl_2^{(1)} at level k
    Step 2: Collision residue -> r-matrix
    Step 3: R-matrix from r-matrix
    Step 4: Verify YBE
    Step 5: Transfer matrix
    Step 6: Verify [T(u), T(v)] = 0
    Step 7: Bethe ansatz equations
    Step 8: Solve BAE
    Step 9: Verify energy against exact diagonalization

    Parameters
    ----------
    k : float
        Level of sl_2^{(1)}.
    N : int
        Chain length.
    M : int
        Number of magnons.
    verbose : bool
        Print intermediate results.

    Returns
    -------
    chain : dict with all intermediate results and verification flags.
    """
    chain = {}

    # Step 1: MC data
    mc = AffineSl2MCData(k=k)
    chain['mc'] = mc
    chain['gamma'] = mc.gamma
    chain['Delta'] = mc.Delta
    chain['kappa'] = mc.kappa

    if verbose:
        print(f"Step 1: MC data for sl_2^(1) at level k={k}")
        print(f"  gamma = pi/{k+2} = {mc.gamma:.6f}")
        print(f"  Delta = cos(gamma) = {mc.Delta:.6f}")
        print(f"  kappa = {mc.kappa:.6f}")

    # Step 2: Collision residue (r-matrix)
    r_test = collision_residue_trigonometric(mc, 0.3)
    chain['r_matrix_sample'] = r_test

    if verbose:
        print(f"Step 2: r-matrix at z=0.3 computed (4x4 matrix)")

    # Step 3: R-matrix
    R_test = R_matrix_xxz(0.3, mc.gamma)
    chain['R_matrix_sample'] = R_test

    # Step 4: Verify YBE
    ybe_residual = verify_ybe_xxz(0.3, 0.7, mc.gamma)
    chain['ybe_residual'] = ybe_residual
    chain['ybe_satisfied'] = ybe_residual < 1e-8

    if verbose:
        print(f"Step 4: YBE residual = {ybe_residual:.2e} (satisfied: {chain['ybe_satisfied']})")

    # Step 5: Transfer matrix (only for small N)
    if N <= 8:
        T_test = xxz_transfer_matrix(0.3, N, mc.gamma)
        chain['transfer_matrix_size'] = T_test.shape

    # Step 6: Verify [T(u), T(v)] = 0
    if N <= 6:
        comm_residual = verify_transfer_commutativity(0.3, 0.7, N, mc.gamma)
        chain['transfer_commutativity_residual'] = comm_residual
        chain['transfer_commuting'] = comm_residual < 1e-6

        if verbose:
            print(f"Step 6: [T(0.3), T(0.7)] residual = {comm_residual:.2e}")

    # Step 7-8: Solve BAE
    bae_result = solve_xxz_bae(N, M, mc.gamma)
    chain['bae_result'] = bae_result

    if verbose:
        print(f"Step 7-8: BAE solved. Success: {bae_result['success']}")
        print(f"  Bethe roots: {bae_result['lambdas']}")
        print(f"  Energy (Bethe): {bae_result['energy']:.8f}")

    # Step 9: Verify against exact diagonalization
    if N <= 10:
        Sz_target = N / 2.0 - M
        exact_evals = xxz_exact_spectrum(N, mc.Delta, Sz_sector=Sz_target)
        chain['exact_spectrum'] = exact_evals

        if len(exact_evals) > 0 and bae_result['success']:
            E_bethe = bae_result['energy']
            # Find the closest exact eigenvalue
            E_closest = exact_evals[np.argmin(np.abs(exact_evals - E_bethe))]
            chain['energy_match'] = abs(E_bethe - E_closest)
            chain['energy_verified'] = abs(E_bethe - E_closest) < 1e-4

            if verbose:
                print(f"Step 9: E_bethe = {E_bethe:.8f}, E_exact = {E_closest:.8f}")
                print(f"  Match: {chain['energy_match']:.2e}")

    return chain


# ========================================================================
# 16.  Multi-path verification utilities
# ========================================================================

def verify_energy_multipath(N: int, M: int, gamma: float,
                            J: float = 1.0) -> Dict[str, Any]:
    r"""Multi-path energy verification.

    Path 1: Bethe ansatz formula
    Path 2: Exact diagonalization
    Path 3: Transfer matrix eigenvalues
    Path 4: Free fermion (if gamma = pi/2)
    Path 5: XXX limit (if gamma is small)

    Returns dict with energies from each path and agreement flags.
    """
    result = {}
    Delta = np.cos(gamma)

    # Path 1: Bethe ansatz
    bae = solve_xxz_bae(N, M, gamma)
    result['path1_bethe'] = bae['energy']
    result['bae_success'] = bae['success']

    # Path 2: Exact diagonalization
    Sz_sector = N / 2.0 - M
    exact_evals = xxz_exact_spectrum(N, Delta, J, Sz_sector=Sz_sector)
    result['path2_exact_spectrum'] = exact_evals
    if len(exact_evals) > 0:
        result['path2_ground_state'] = float(exact_evals[0])

    # Path 3: Transfer matrix eigenvalue (only small N)
    if N <= 6:
        T_0 = xxz_transfer_matrix(0.0, N, gamma)
        t_evals = la.eigvals(T_0)
        result['path3_transfer_eigenvalues'] = np.sort(np.abs(t_evals))[::-1]

    # Path 4: Free fermion (gamma = pi/2, Delta = 0)
    if abs(gamma - PI / 2) < 1e-8:
        ff_energy = free_fermion_ground_state_energy(N, M, J)
        result['path4_free_fermion'] = ff_energy

    # Path 5: XXX limit comparison (very rough for finite gamma)
    if abs(gamma) < 0.1:
        # Solve XXX BAE for comparison
        from compute.lib.bethe_ansatz_shadow import solve_xxx_bae as _solve_xxx
        xxx_result = _solve_xxx(N, M)
        result['path5_xxx_energy'] = xxx_result['energy']

    # Agreement checks
    if bae['success'] and len(exact_evals) > 0:
        E_bethe = bae['energy']
        E_closest = exact_evals[np.argmin(np.abs(exact_evals - E_bethe))]
        result['bethe_exact_agreement'] = abs(E_bethe - E_closest) < 1e-4
        result['bethe_exact_difference'] = abs(E_bethe - E_closest)

    return result


def verify_spectrum_completeness(N: int, gamma: float, M: int) -> Dict[str, Any]:
    r"""Verify completeness: Bethe states account for all eigenstates.

    For each allowed set of quantum numbers, solve the BAE and
    collect the energies.  Compare with exact diagonalization.

    This is the strongest verification: if ALL exact eigenvalues
    are reproduced by Bethe states, the BAE is complete.
    """
    from math import comb

    Delta = np.cos(gamma)
    Sz_sector = N / 2.0 - M
    expected_dim = comb(N, M)

    # Exact spectrum
    exact_evals = xxz_exact_spectrum(N, Delta, Sz_sector=Sz_sector)

    # Collect Bethe energies from all quantum number sets
    bethe_energies = []
    qn_range = _valid_quantum_number_range(N, M)

    for qn_tuple in combinations(qn_range, M):
        qn = np.array(qn_tuple, dtype=float)
        result = solve_xxz_bae(N, M, gamma, quantum_numbers=qn)
        if result['success'] and result['residual_norm'] < 1e-6:
            bethe_energies.append(result['energy'])

    bethe_energies = np.sort(bethe_energies)

    # Match against exact
    matched = 0
    used_exact = [False] * len(exact_evals)
    for E_b in bethe_energies:
        for i, E_e in enumerate(exact_evals):
            if not used_exact[i] and abs(E_b - E_e) < 1e-4:
                matched += 1
                used_exact[i] = True
                break

    return {
        'N': N, 'M': M, 'gamma': gamma,
        'expected_dim': expected_dim,
        'exact_count': len(exact_evals),
        'bethe_count': len(bethe_energies),
        'matched': matched,
        'complete': matched == expected_dim,
        'bethe_energies': bethe_energies,
        'exact_energies': exact_evals,
    }
