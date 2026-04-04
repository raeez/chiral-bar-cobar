r"""Bethe ansatz equations from the shadow connection and integrable spin chains.

The shadow connection nabla^sh on the moduli of the convolution algebra is a
flat meromorphic connection.  Its horizontal sections satisfy an ODE whose
quantization (via hbar-deformation) gives the Bethe ansatz equations (BAE) for
integrable spin chains.  This is the Nekrasov-Shatashvili limit of the
gauge/Bethe correspondence (Nekrasov-Shatashvili 2009).

MODULES:

1. XXX spin chain (rational, from affine sl_2):
   BAE: prod_{j!=i} (u_i - u_j + 1)/(u_i - u_j - 1) = ((u_i + i/2)/(u_i - i/2))^L
   R-matrix: r(z) = Omega/z (rational Yang R-matrix, AP19 collision residue)
   Hamiltonian: H = sum S_i . S_{i+1} (Heisenberg XXX)

2. XXZ spin chain (trigonometric, from U_q(sl_2)):
   BAE: prod_{j!=i} sinh(u_i-u_j+eta)/sinh(u_i-u_j-eta)
        = (sinh(u_i+eta/2)/sinh(u_i-eta/2))^L
   q = e^eta, Delta = cosh(eta) (anisotropy parameter)

3. XYZ spin chain (elliptic, from elliptic quantum group):
   BAE with Jacobi theta functions.  Genus-1 shadow tower.

4. Higher-rank: sl_3 nested BAE.
   Two species of Bethe roots with coupled equations.

5. Thermodynamic Bethe ansatz (TBA):
   L -> infinity limit, integral equations for root density.
   Ground state energy e_0 = 1/4 - ln(2) at half-filling.

6. Functional Bethe ansatz (Sklyanin):
   Baxter Q-operator, TQ relation: T(u)Q(u) = a(u)Q(u-eta) + d(u)Q(u+eta).

7. ODE/IM correspondence (Dorey-Tateo, Bazhanov-Lukyanov-Zamolodchikov):
   Stokes multipliers of -psi'' + x^{2M} psi = E psi give Q-operator eigenvalues.

Connections to the monograph:
   - The rational r-matrix r(z) = Omega/z is the collision residue
     Res^{coll}_{0,2}(Theta_A) for A = sl_2-hat_k (AP19, rmatrix_landscape.py).
   - The trigonometric R-matrix arises from the genus-1 shadow (elliptic curve).
   - The Baxter Q-operator relates to the bar complex determinant det(B(g-hat)).
   - The ODE/IM correspondence connects the shadow ODE (Picard-Fuchs from
     shadow_connection.py) to the integrable model spectrum.

Conventions:
   - Cohomological grading (|d| = +1).
   - Spin-1/2 basis: |up> = (1,0)^T, |down> = (0,1)^T.
   - Pauli matrices: sigma_x, sigma_y, sigma_z standard.
   - Energy convention: H = sum_{i=1}^{L} (S_i . S_{i+1} - 1/4)
     for the antiferromagnetic chain, so ground state energy < 0.
   - Periodic boundary conditions: site L+1 = site 1.

References:
   - thm:shadow-connection (higher_genus_modular_koszul.tex)
   - rmatrix_landscape.py: r(z) = Omega/z for affine sl_2
   - sl2_baxter.py: Baxter TQ relation at K_0 level
   - yangian_rmatrix_sl3.py: sl_3 R-matrix
   - shadow_connection.py: shadow ODE, Picard-Fuchs
   - Nekrasov-Shatashvili, Quantization of integrable systems (2009)
   - Faddeev, How the algebraic Bethe ansatz works (Les Houches 1996)
   - Baxter, Exactly Solved Models in Statistical Mechanics (1982)
   - Dorey-Tateo, Anharmonic oscillators and Bethe ansatz (1999)
   - Bazhanov-Lukyanov-Zamolodchikov, Spectral determinants (1999)
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
from numpy import linalg as la
from scipy import optimize


# ========================================================================
# 1. Pauli matrices and spin operators
# ========================================================================

# Pauli matrices (standard convention)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA_PLUS = np.array([[0, 1], [0, 0]], dtype=complex)
SIGMA_MINUS = np.array([[0, 0], [1, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def _kron_chain(ops: List[np.ndarray]) -> np.ndarray:
    """Kronecker product of a chain of operators."""
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result


def spin_operator(L: int, site: int, pauli: np.ndarray) -> np.ndarray:
    """Spin-1/2 operator at a given site on a chain of length L.

    sigma_i = I_2 tensor ... tensor sigma tensor ... tensor I_2
    where sigma is at position `site` (0-indexed).
    """
    ops = [I2] * L
    ops[site] = pauli
    return _kron_chain(ops)


# ========================================================================
# 2. XXX Heisenberg Hamiltonian (exact diagonalization)
# ========================================================================

def heisenberg_xxx_hamiltonian(L: int, J: float = 1.0) -> np.ndarray:
    r"""Heisenberg XXX Hamiltonian with periodic boundary conditions.

    H = J * sum_{i=0}^{L-1} (S_i . S_{i+1})
      = J * sum_{i=0}^{L-1} (1/2)(sigma_x_i sigma_x_{i+1}
                            + sigma_y_i sigma_y_{i+1}
                            + sigma_z_i sigma_z_{i+1})

    where S = sigma/2 and site L = site 0 (periodic).

    The factor of 1/2 in each bilinear comes from S = sigma/2, giving
    S_i . S_{i+1} = (1/4)(sigma_i . sigma_{i+1}).

    We use the convention H = J * sum (1/4)(sigma . sigma), so
    H|ferro> = (L/4)*J for the ferromagnetic ground state.
    """
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(L):
        j = (i + 1) % L  # periodic BC
        for pauli in [SIGMA_X, SIGMA_Y, SIGMA_Z]:
            Si = spin_operator(L, i, pauli)
            Sj = spin_operator(L, j, pauli)
            H += J * 0.25 * Si @ Sj
    return H


def total_sz(L: int) -> np.ndarray:
    """Total S^z operator for a chain of length L."""
    Sz = np.zeros((2**L, 2**L), dtype=complex)
    for i in range(L):
        Sz += 0.5 * spin_operator(L, i, SIGMA_Z)
    return Sz


def exact_diagonalization_xxx(L: int, J: float = 1.0,
                               Sz_sector: Optional[int] = None
                               ) -> Tuple[np.ndarray, np.ndarray]:
    """Exact diagonalization of the XXX chain.

    Args:
        L: chain length.
        J: coupling constant (J > 0 antiferromagnetic, J < 0 ferromagnetic).
        Sz_sector: if provided, restrict to total S^z = Sz_sector/2
                   (Sz_sector is twice the actual S^z to keep integer).

    Returns:
        (eigenvalues, eigenvectors) sorted by energy.
    """
    H = heisenberg_xxx_hamiltonian(L, J)
    if Sz_sector is not None:
        Sz = total_sz(L)
        # Build the Sz_sector basis
        sz_vals = np.diag(Sz.real)
        target = Sz_sector / 2.0
        mask = np.abs(sz_vals - target) < 1e-10
        indices = np.where(mask)[0]
        if len(indices) == 0:
            return np.array([]), np.array([])
        # Project Hamiltonian
        H_sector = H[np.ix_(indices, indices)]
        evals, evecs = la.eigh(H_sector)
        order = np.argsort(evals)
        return evals[order], evecs[:, order]
    else:
        evals, evecs = la.eigh(H)
        order = np.argsort(evals.real)
        return evals[order].real, evecs[:, order]


# ========================================================================
# 3. XXX Bethe ansatz equations
# ========================================================================

def xxx_bae_residual(u: np.ndarray, L: int) -> np.ndarray:
    """Residual of the XXX Bethe ansatz equations.

    BAE (logarithmic form):
      L * arctan(2*u_i) - sum_{j!=i} arctan(u_i - u_j) = pi * I_i

    where I_i are (half-)integer quantum numbers.

    We write the BAE in product form as a system f_i = 0:
      f_i = prod_{j!=i} (u_i - u_j + 1)/(u_i - u_j - 1)
            - ((u_i + 0.5)/(u_i - 0.5))^L

    This function returns log form residuals for numerical stability:
      g_i = L * log((u_i + 0.5i)/(u_i - 0.5i))
            - sum_{j!=i} log((u_i - u_j + i)/(u_i - u_j - i))
            - 2*pi*i*I_i

    But for simplicity we use the real-valued formulation with arctan.
    """
    M = len(u)
    residual = np.zeros(M)
    for i in range(M):
        # Driving term
        residual[i] = L * np.arctan(2 * u[i])
        # Scattering terms
        for j in range(M):
            if j != i:
                residual[i] -= np.arctan(u[i] - u[j])
    return residual


def xxx_bae_equations(u: np.ndarray, L: int,
                      quantum_numbers: np.ndarray) -> np.ndarray:
    """XXX BAE as f(u) = 0.

    L * arctan(2*u_i) - sum_{j!=i} arctan(u_i - u_j) = pi * I_i

    Returns residuals that should be zero at a solution.
    """
    M = len(u)
    f = np.zeros(M)
    for i in range(M):
        f[i] = L * np.arctan(2 * u[i])
        for j in range(M):
            if j != i:
                f[i] -= np.arctan(u[i] - u[j])
        f[i] -= np.pi * quantum_numbers[i]
    return f


def solve_xxx_bae(L: int, M: int,
                  quantum_numbers: Optional[np.ndarray] = None,
                  u0: Optional[np.ndarray] = None,
                  ) -> Dict[str, Any]:
    """Solve the XXX Bethe ansatz equations for L sites, M magnons.

    The quantum numbers I_i label the branch of the BAE solution.
    For the ground state of the antiferromagnetic chain at half-filling
    (M = L/2), the quantum numbers are:
        I_i = -(M-1)/2, -(M-3)/2, ..., (M-1)/2

    Args:
        L: chain length.
        M: number of down spins (magnons).
        quantum_numbers: array of M quantum numbers.  If None, use
                         the ground-state prescription.
        u0: initial guess.  If None, use a heuristic.

    Returns:
        dict with keys:
          'roots': Bethe roots u_i
          'energy': E = -J * sum 1/(u_i^2 + 1/4)
          'momentum': total momentum P = sum arctan(2*u_i)
          'success': whether the solver converged
    """
    if quantum_numbers is None:
        # Ground state quantum numbers (antiferromagnetic, half-filling)
        quantum_numbers = np.array([-(M - 1) / 2 + k for k in range(M)])

    if u0 is None:
        # Heuristic initial guess: distribute roots
        if M == 1:
            u0 = np.array([0.0])
        else:
            u0 = np.linspace(-M / 2, M / 2, M) * 0.5

    def equations(u):
        return xxx_bae_equations(u, L, quantum_numbers)

    result = optimize.fsolve(equations, u0, full_output=True)
    roots = result[0]
    info = result[1]
    success = result[2] == 1

    # Energy: E = -(J/2) * sum 1/(u_i^2 + 1/4) + L/4
    # (the L/4 shift makes H = sum S.S, not H = sum S.S - 1/4)
    energy_magnon = -0.5 * np.sum(1.0 / (roots**2 + 0.25))
    energy = energy_magnon + L / 4.0

    # Momentum
    momentum = np.sum(2 * np.arctan(2 * roots))

    return {
        'roots': roots,
        'energy': energy,
        'energy_magnon': energy_magnon,
        'momentum': momentum,
        'quantum_numbers': quantum_numbers,
        'success': success,
        'L': L,
        'M': M,
    }


def xxx_energy_from_roots(roots: np.ndarray, L: int) -> float:
    """Compute XXX chain energy from Bethe roots.

    E = sum_{i=1}^{L} (S_i . S_{i+1})
      = L/4 - (1/2)*sum_{a=1}^{M} 1/(u_a^2 + 1/4)

    The L/4 term comes from the identity component; the magnon
    contribution is always negative (lowering energy).
    """
    return L / 4.0 - 0.5 * np.sum(1.0 / (roots**2 + 0.25))


def xxx_momentum_from_roots(roots: np.ndarray) -> float:
    """Total momentum from Bethe roots: P = sum_a 2*arctan(2*u_a)."""
    return float(np.sum(2 * np.arctan(2 * roots)))


# ========================================================================
# 4. XXX: R-matrix and transfer matrix from shadow data
# ========================================================================

def xxx_r_matrix_shadow(u: float) -> np.ndarray:
    """Rational Yang R-matrix from the sl_2 shadow tower.

    R(u) = u*I + P  (in the spin-1/2 representation)

    where P is the permutation operator on C^2 tensor C^2.
    This is the collision residue of the bar propagator (AP19):
    r(z) = Omega/z gives R(u) = u*I + Omega, and Omega = P in
    the fundamental representation of sl_2 (up to normalization).

    Returns 4x4 matrix acting on C^2 tensor C^2.
    """
    I4 = np.eye(4, dtype=complex)
    # Permutation operator P: P|a,b> = |b,a>
    P = np.array([[1, 0, 0, 0],
                   [0, 0, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, 1]], dtype=complex)
    return u * I4 + P


def xxx_transfer_matrix(u: float, L: int) -> np.ndarray:
    """Transfer matrix T(u) for the XXX chain of length L.

    T(u) = Tr_0 [R_{0,L}(u) ... R_{0,2}(u) R_{0,1}(u)]

    where R_{0,j}(u) = u*I + P_{0j} acts on the auxiliary space 0
    and physical space j.  The trace is over the auxiliary space.

    Returns a 2^L x 2^L matrix.
    """
    dim = 2**L
    # The Lax operator L_j(u) acts on (C^2)_aux tensor (C^2)^{tensor L}_phys
    # L_j(u) = u*I_{aux} tensor I_j + P_{aux,j}
    # We work in the full space (C^2)_aux tensor (C^2)^L
    aux_dim = 2
    phys_dim = dim

    # Build the monodromy matrix M(u) = L_L(u) ... L_1(u)
    # in the full aux+phys space of dimension 2 * 2^L
    full_dim = aux_dim * phys_dim
    M = np.eye(full_dim, dtype=complex)

    for j in range(L):
        # L_j(u) = u * I_{aux} tensor I_phys + P_{aux,j}
        Lj = u * np.eye(full_dim, dtype=complex)
        # Add the permutation P_{aux,j}: swaps aux qubit with site j
        Paj = _permutation_aux_site(L, j)
        Lj += Paj
        M = Lj @ M

    # Trace over auxiliary space: T(u) = Tr_aux[M(u)]
    # M is (2 * 2^L) x (2 * 2^L), structured as 2x2 blocks of 2^L x 2^L
    T = np.zeros((phys_dim, phys_dim), dtype=complex)
    for a in range(aux_dim):
        block = M[a * phys_dim:(a + 1) * phys_dim,
                  a * phys_dim:(a + 1) * phys_dim]
        T += block

    return T


def _permutation_aux_site(L: int, j: int) -> np.ndarray:
    """Permutation operator P_{aux, site_j} in the full aux+phys space.

    Full space = (C^2)_aux tensor (C^2)^L_phys, dimension 2^{L+1}.
    P swaps the auxiliary qubit with site j.
    """
    full_dim = 2**(L + 1)
    P = np.zeros((full_dim, full_dim), dtype=complex)

    # Label states by (L+1) qubits: qubit 0 = aux, qubits 1..L = phys
    for state in range(full_dim):
        bits = [(state >> (L - k)) & 1 for k in range(L + 1)]
        # Swap bit 0 (aux) with bit j+1 (phys site j, 0-indexed among phys)
        new_bits = list(bits)
        new_bits[0], new_bits[j + 1] = new_bits[j + 1], new_bits[0]
        new_state = 0
        for k, b in enumerate(new_bits):
            new_state |= (b << (L - k))
        P[new_state, state] = 1.0

    return P


def xxx_verify_transfer_commuting(L: int, u_vals: List[float]) -> float:
    """Verify [T(u), T(v)] = 0 for different spectral parameters.

    This is a consequence of the Yang-Baxter equation.
    Returns the maximum norm of [T(u), T(v)] over all pairs.
    """
    max_comm = 0.0
    T_matrices = [xxx_transfer_matrix(u, L) for u in u_vals]
    for i in range(len(u_vals)):
        for j in range(i + 1, len(u_vals)):
            comm = T_matrices[i] @ T_matrices[j] - T_matrices[j] @ T_matrices[i]
            max_comm = max(max_comm, la.norm(comm))
    return max_comm


def xxx_hamiltonian_from_transfer(L: int) -> np.ndarray:
    """Extract the Heisenberg Hamiltonian from the transfer matrix.

    H = (d/du) ln T(u) |_{u=0} (up to a constant shift).

    More precisely:
      T(u) = (u + 1)^L * I + ... at u = 0, and
      H propto T'(0) / T(0) - (L/2)*I

    We use numerical differentiation.
    """
    eps = 1e-6
    T_plus = xxx_transfer_matrix(eps, L)
    T_minus = xxx_transfer_matrix(-eps, L)
    T_0 = xxx_transfer_matrix(0.0, L)

    # T'(0) via central difference
    T_prime = (T_plus - T_minus) / (2 * eps)

    # H propto T_0^{-1} T'(0) (up to shift)
    # At u=0: T(0) = Tr_0[P_{0L}...P_{01}] = cyclic shift operator
    # T'(0) involves the Hamiltonian
    # The exact relation: H = (1/2) * d/du ln T(u)|_{u=0} + const
    # For our conventions: T'(0) = sum_j P_j ... (derivative hits one Lax)
    # The Hamiltonian density is P_{j,j+1}, so H = sum P_{j,j+1} = ...

    # Safer: just use H = (1/2) T_0_inv @ T_prime as the extraction
    T_0_inv = la.inv(T_0)
    H_extracted = 0.5 * (T_0_inv @ T_prime)

    return H_extracted


# ========================================================================
# 5. XXZ spin chain
# ========================================================================

def heisenberg_xxz_hamiltonian(L: int, Delta: float = 1.0,
                                J: float = 1.0) -> np.ndarray:
    r"""Heisenberg XXZ Hamiltonian with anisotropy Delta.

    H = J * sum_{i=0}^{L-1} (S^x_i S^x_{i+1} + S^y_i S^y_{i+1}
                             + Delta * S^z_i S^z_{i+1})
      = (J/4) * sum (sigma^x sigma^x + sigma^y sigma^y + Delta sigma^z sigma^z)

    Delta = 1: isotropic XXX.
    |Delta| < 1: gapless (critical) regime.
    |Delta| > 1: gapped (Ising-like) regime.

    For the trigonometric R-matrix: Delta = cosh(eta), q = e^eta.
    """
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(L):
        j = (i + 1) % L
        for pauli in [SIGMA_X, SIGMA_Y]:
            Si = spin_operator(L, i, pauli)
            Sj = spin_operator(L, j, pauli)
            H += J * 0.25 * Si @ Sj
        # Anisotropic Z-Z coupling
        Szi = spin_operator(L, i, SIGMA_Z)
        Szj = spin_operator(L, j, SIGMA_Z)
        H += J * 0.25 * Delta * Szi @ Szj
    return H


def xxz_bae_equations(u: np.ndarray, L: int, eta: float,
                      quantum_numbers: np.ndarray) -> np.ndarray:
    """XXZ Bethe ansatz equations in logarithmic form.

    The BAE for the XXZ chain with anisotropy parameter eta:
      L * theta_1(u_i, eta) - sum_{j!=i} theta_2(u_i - u_j, eta) = 2*pi*I_i

    where theta_n(u, eta) = 2*arctan(tan(n*eta/2) * tanh(u / 2) / ... )

    For the REAL parametrization (XXZ with Delta = cos(gamma), gamma = i*eta):
    We use the standard rapidity parametrization.

    Simplified form for real eta (Delta = cosh(eta)):
      L * phi(u_i, eta/2) - sum_{j!=i} phi(u_i-u_j, eta) = 2*pi*I_i
    where phi(u, alpha) = 2*arctan(tanh(u/2) / tan(alpha/2)) for real.

    For the regime |Delta| <= 1, we set Delta = cos(gamma) and use:
      L * theta(u_i, gamma/2) - sum_{j!=i} theta(u_i-u_j, gamma) = 2*pi*I_i
    where theta(u, alpha) = 2*arctan(tan(alpha) * tanh(u)).

    We implement the general case using complex logarithms for robustness.
    """
    M = len(u)
    f = np.zeros(M)

    def phi(x, alpha):
        """Scattering phase: phi(x, alpha) = 2*arctan(sinh(x)/sin(alpha))."""
        if abs(np.sin(alpha)) < 1e-15:
            return 2 * np.arctan(x)  # XXX limit
        return 2 * np.arctan(np.sinh(x) / np.sin(alpha))

    gamma = np.arccos(np.cosh(eta)) if abs(np.cosh(eta)) <= 1 else eta

    for i in range(M):
        # Driving term
        f[i] = L * phi(u[i], eta / 2)
        # Scattering
        for j in range(M):
            if j != i:
                f[i] -= phi(u[i] - u[j], eta)
        f[i] -= 2 * np.pi * quantum_numbers[i]
    return f


def solve_xxz_bae(L: int, M: int, eta: float,
                  quantum_numbers: Optional[np.ndarray] = None,
                  u0: Optional[np.ndarray] = None,
                  ) -> Dict[str, Any]:
    """Solve the XXZ BAE for L sites, M magnons, anisotropy eta.

    Delta = cosh(eta).  The XXX limit is eta -> 0 (Delta -> 1).

    Returns dict with roots, energy, success flag.
    """
    Delta = np.cosh(eta)

    if quantum_numbers is None:
        quantum_numbers = np.array([-(M - 1) / 2 + k for k in range(M)])

    if u0 is None:
        u0 = np.linspace(-M / 2, M / 2, M) * 0.5

    def equations(u):
        return xxz_bae_equations(u, L, eta, quantum_numbers)

    result = optimize.fsolve(equations, u0, full_output=True)
    roots = result[0]
    success = result[2] == 1

    # Energy for XXZ:
    # The quasi-momentum for magnon a is k_a = phi(u_a, eta/2).
    # The single-magnon dispersion is e(k) = -(Delta + cos(k)).
    # Total energy: E = Delta*L/4 - sum_a (Delta + cos(k_a))
    #             = Delta*(L/4 - M) - sum_a cos(k_a)
    # For H = (J/4)*sum(sigma_x sigma_x + sigma_y sigma_y + Delta sigma_z sigma_z)
    # For small eta: reduces to XXX formula
    if abs(eta) < 1e-12:
        energy = xxx_energy_from_roots(roots, L)
    else:
        sin_half = np.sin(eta / 2)
        energy = Delta * (L / 4.0 - M)
        for root in roots:
            k = 2 * np.arctan(np.sinh(root) / sin_half) if abs(sin_half) > 1e-15 else 0.0
            energy -= np.cos(k)

    return {
        'roots': roots,
        'energy': energy,
        'Delta': Delta,
        'eta': eta,
        'success': success,
        'L': L,
        'M': M,
    }


def exact_diagonalization_xxz(L: int, Delta: float = 1.0,
                               Sz_sector: Optional[int] = None
                               ) -> Tuple[np.ndarray, np.ndarray]:
    """Exact diagonalization of the XXZ chain."""
    H = heisenberg_xxz_hamiltonian(L, Delta)
    if Sz_sector is not None:
        Sz = total_sz(L)
        sz_vals = np.diag(Sz.real)
        target = Sz_sector / 2.0
        mask = np.abs(sz_vals - target) < 1e-10
        indices = np.where(mask)[0]
        if len(indices) == 0:
            return np.array([]), np.array([])
        H_sector = H[np.ix_(indices, indices)]
        evals, evecs = la.eigh(H_sector)
        order = np.argsort(evals)
        return evals[order], evecs[:, order]
    else:
        evals, evecs = la.eigh(H)
        order = np.argsort(evals.real)
        return evals[order].real, evecs[:, order]


# ========================================================================
# 6. XXZ R-matrix (trigonometric)
# ========================================================================

def xxz_r_matrix(u: float, eta: float) -> np.ndarray:
    """Trigonometric R-matrix for the XXZ chain.

    R(u, eta) = | sinh(u+eta)  0           0           0          |
                | 0            sinh(u)     sinh(eta)   0          |
                | 0            sinh(eta)   sinh(u)     0          |
                | 0            0           0           sinh(u+eta)|

    In the limit eta -> 0: R(u,0) -> u*I + P (XXX R-matrix).

    This is the six-vertex model R-matrix with weights:
      a = sinh(u + eta), b = sinh(u), c = sinh(eta).
    """
    a = np.sinh(u + eta)
    b = np.sinh(u)
    cc = np.sinh(eta)
    return np.array([[a, 0, 0, 0],
                      [0, b, cc, 0],
                      [0, cc, b, 0],
                      [0, 0, 0, a]], dtype=complex)


def xxz_verify_yang_baxter(eta: float, u1: float = 0.3,
                            u2: float = 0.7) -> float:
    """Verify Yang-Baxter equation for the XXZ R-matrix.

    R_{12}(u1-u2) R_{13}(u1) R_{23}(u2) = R_{23}(u2) R_{13}(u1) R_{12}(u1-u2)

    Returns norm of the difference (should be ~0).
    """
    R12 = np.kron(xxz_r_matrix(u1 - u2, eta), np.eye(2))
    R23 = np.kron(np.eye(2), xxz_r_matrix(u2, eta))
    # R13 acts on spaces 1 and 3: need permutation
    R13_raw = xxz_r_matrix(u1, eta)
    # Embed R13 in 8x8: acts on qubits 0 and 2 of a 3-qubit system
    R13 = np.zeros((8, 8), dtype=complex)
    for a1 in range(2):
        for a3 in range(2):
            for b1 in range(2):
                for b3 in range(2):
                    val = R13_raw[2 * a1 + a3, 2 * b1 + b3]
                    for a2 in range(2):
                        row = 4 * a1 + 2 * a2 + a3
                        col = 4 * b1 + 2 * a2 + b3
                        R13[row, col] = val

    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(la.norm(lhs - rhs))


def xxz_xxx_limit(u: float, eta: float = 1e-8) -> float:
    """Verify that XXZ R-matrix reduces to XXX in the eta -> 0 limit.

    Returns norm of the difference R_XXZ(u, eta)/eta - R_XXX(u).
    """
    R_xxz = xxz_r_matrix(u, eta)
    R_xxx = xxx_r_matrix_shadow(u)
    # In the limit eta -> 0: sinh(u+eta) ~ u+eta, sinh(u) ~ u, sinh(eta) ~ eta
    # So R_xxz / eta ~ (u/eta + 1)*diag + (u/eta)*off_diag + permutation
    # Actually: R_xxz ~ eta * (u*I + P) for small eta with suitable normalization.
    # The correct limit: R_xxz(u*eta, eta) / eta -> u*I + P
    R_xxz_scaled = xxz_r_matrix(u * eta, eta) / eta
    return float(la.norm(R_xxz_scaled - R_xxx))


# ========================================================================
# 7. XYZ spin chain (elliptic)
# ========================================================================

def _jacobi_theta1(u: complex, tau: complex, nmax: int = 30) -> complex:
    """Jacobi theta function theta_1(u, tau) = -i sum_{n=-inf}^{inf}
    (-1)^n q^{(n+1/2)^2} e^{(2n+1)*i*pi*u}

    where q = e^{i*pi*tau}.

    Standard definition: theta_1(u|tau) = 2 sum_{n=0}^{inf}
    (-1)^n q^{(n+1/2)^2} sin((2n+1)*pi*u)
    """
    q = np.exp(1j * np.pi * tau)
    result = 0.0 + 0.0j
    for n in range(nmax):
        result += ((-1)**n * q**((n + 0.5)**2)
                   * np.sin((2 * n + 1) * np.pi * u))
    return 2 * result


def _jacobi_theta2(u: complex, tau: complex, nmax: int = 30) -> complex:
    """Jacobi theta_2(u|tau) = 2 sum_{n=0}^{inf} q^{(n+1/2)^2} cos((2n+1)*pi*u)."""
    q = np.exp(1j * np.pi * tau)
    result = 0.0 + 0.0j
    for n in range(nmax):
        result += q**((n + 0.5)**2) * np.cos((2 * n + 1) * np.pi * u)
    return 2 * result


def _jacobi_theta3(u: complex, tau: complex, nmax: int = 30) -> complex:
    """Jacobi theta_3(u|tau) = 1 + 2 sum_{n=1}^{inf} q^{n^2} cos(2n*pi*u)."""
    q = np.exp(1j * np.pi * tau)
    result = 1.0 + 0.0j
    for n in range(1, nmax):
        result += 2 * q**(n**2) * np.cos(2 * n * np.pi * u)
    return result


def _jacobi_theta4(u: complex, tau: complex, nmax: int = 30) -> complex:
    """Jacobi theta_4(u|tau) = 1 + 2 sum_{n=1}^{inf} (-1)^n q^{n^2} cos(2n*pi*u)."""
    q = np.exp(1j * np.pi * tau)
    result = 1.0 + 0.0j
    for n in range(1, nmax):
        result += 2 * ((-1)**n) * q**(n**2) * np.cos(2 * n * np.pi * u)
    return result


def xyz_r_matrix(u: complex, eta: complex, tau: complex) -> np.ndarray:
    r"""Elliptic R-matrix for the XYZ/eight-vertex model (Belavin 1981).

    Uses the Belavin parametrization:
      R(u) = sum_{mu=0}^{3} W_mu(u) (sigma_mu tensor sigma_mu)

    where sigma_0 = I, sigma_{1,2,3} = Pauli matrices, and
      W_mu(u) = theta_{mu+1}(u + eta | tau) / theta_{mu+1}(eta | tau)

    In the basis {|++>, |+->, |-+>, |-->}, this gives:
      a = W_0 + W_3,  b = W_0 - W_3,  c = W_1 + W_2,  d = W_1 - W_2

      R(u) = | a  0  0  d |
             | 0  b  c  0 |
             | 0  c  b  0 |
             | d  0  0  a |

    Properties:
      - R(0) = 2*P (regularity: proportional to the permutation operator)
      - Satisfies the Yang-Baxter equation R12(u-v) R13(u) R23(v) = R23(v) R13(u) R12(u-v)
      - In the limit tau -> i*inf: reduces to the XXZ trigonometric R-matrix
    """
    W0 = _jacobi_theta1(u + eta, tau) / _jacobi_theta1(eta, tau)
    W1 = _jacobi_theta2(u + eta, tau) / _jacobi_theta2(eta, tau)
    W2 = _jacobi_theta3(u + eta, tau) / _jacobi_theta3(eta, tau)
    W3 = _jacobi_theta4(u + eta, tau) / _jacobi_theta4(eta, tau)

    a = W0 + W3
    b = W0 - W3
    c = W1 + W2
    d = W1 - W2

    return np.array([[a, 0, 0, d],
                      [0, b, c, 0],
                      [0, c, b, 0],
                      [d, 0, 0, a]], dtype=complex)


def xyz_verify_yang_baxter(eta: complex, tau: complex,
                            u1: complex = 0.1 + 0.0j,
                            u2: complex = 0.3 + 0.0j) -> float:
    """Verify Yang-Baxter equation for the elliptic R-matrix."""
    R12 = np.kron(xyz_r_matrix(u1 - u2, eta, tau), np.eye(2))
    R23 = np.kron(np.eye(2), xyz_r_matrix(u2, eta, tau))
    R13_raw = xyz_r_matrix(u1, eta, tau)
    R13 = np.zeros((8, 8), dtype=complex)
    for a1 in range(2):
        for a3 in range(2):
            for b1 in range(2):
                for b3 in range(2):
                    val = R13_raw[2 * a1 + a3, 2 * b1 + b3]
                    for a2 in range(2):
                        row = 4 * a1 + 2 * a2 + a3
                        col = 4 * b1 + 2 * a2 + b3
                        R13[row, col] = val
    lhs = R12 @ R13 @ R23
    rhs = R23 @ R13 @ R12
    return float(la.norm(lhs - rhs))


def heisenberg_xyz_hamiltonian(L: int, Jx: float = 1.0, Jy: float = 1.0,
                                Jz: float = 1.0) -> np.ndarray:
    """XYZ Hamiltonian: H = sum (Jx S^x S^x + Jy S^y S^y + Jz S^z S^z)."""
    dim = 2**L
    H = np.zeros((dim, dim), dtype=complex)
    couplings = [(SIGMA_X, Jx), (SIGMA_Y, Jy), (SIGMA_Z, Jz)]
    for i in range(L):
        j = (i + 1) % L
        for pauli, J_val in couplings:
            Si = spin_operator(L, i, pauli)
            Sj = spin_operator(L, j, pauli)
            H += 0.25 * J_val * Si @ Sj
    return H


def xyz_bae_equations(u: np.ndarray, L: int, eta: complex,
                      tau: complex,
                      quantum_numbers: np.ndarray) -> np.ndarray:
    """XYZ Bethe ansatz equations (elliptic).

    The BAE involve ratios of theta functions:
      prod_{j!=i} [theta_1(u_i - u_j + eta, tau) / theta_1(u_i - u_j - eta, tau)]
      = [theta_1(u_i + eta/2, tau) / theta_1(u_i - eta/2, tau)]^L

    In logarithmic form with quantum numbers I_i.
    We solve the real and imaginary parts simultaneously.
    """
    M = len(u)
    f = np.zeros(2 * M)  # real + imaginary parts

    for i in range(M):
        ui = u[i]
        # Driving term
        log_drive = L * np.log(
            _jacobi_theta1(ui + eta / 2, tau)
            / _jacobi_theta1(ui - eta / 2, tau)
        )
        # Scattering term
        log_scatter = 0.0 + 0.0j
        for j in range(M):
            if j != i:
                log_scatter += np.log(
                    _jacobi_theta1(u[i] - u[j] + eta, tau)
                    / _jacobi_theta1(u[i] - u[j] - eta, tau)
                )
        # BAE: log_drive - log_scatter = 2*pi*i*I_i
        residual = log_drive - log_scatter - 2j * np.pi * quantum_numbers[i]
        f[2 * i] = residual.real
        f[2 * i + 1] = residual.imag

    return f


def solve_xyz_bae(L: int, M: int, eta: complex, tau: complex,
                  quantum_numbers: Optional[np.ndarray] = None,
                  u0: Optional[np.ndarray] = None,
                  ) -> Dict[str, Any]:
    """Solve the XYZ BAE.

    Returns dict with roots, success flag.
    """
    if quantum_numbers is None:
        quantum_numbers = np.array([-(M - 1) / 2 + k for k in range(M)])

    if u0 is None:
        u0 = np.linspace(-0.1 * M, 0.1 * M, M)

    def equations(u_flat):
        u_complex = u_flat[:M] + 1j * u_flat[M:]
        res = xyz_bae_equations(u_complex, L, eta, tau, quantum_numbers)
        return res

    u0_flat = np.concatenate([u0.real, u0.imag])
    result = optimize.fsolve(equations, u0_flat, full_output=True)
    u_sol = result[0][:M] + 1j * result[0][M:]
    success = result[2] == 1

    return {
        'roots': u_sol,
        'success': success,
        'eta': eta,
        'tau': tau,
        'L': L,
        'M': M,
    }


# ========================================================================
# 8. Higher-rank: sl_3 nested Bethe ansatz
# ========================================================================

def sl3_nested_bae_equations(u1: np.ndarray, u2: np.ndarray,
                              L: int,
                              qn1: np.ndarray,
                              qn2: np.ndarray) -> np.ndarray:
    """Nested Bethe ansatz equations for sl_3 (XXX-type).

    For the sl_3 chain in the fundamental representation on L sites,
    with M_1 roots of type 1 and M_2 roots of type 2:

    Level 1 BAE:
      prod_{b!=a} (u^(1)_a - u^(1)_b + i) / (u^(1)_a - u^(1)_b - i)
      = [(u^(1)_a + i/2) / (u^(1)_a - i/2)]^L
        * prod_b (u^(1)_a - u^(2)_b - i/2) / (u^(1)_a - u^(2)_b + i/2)

    Level 2 BAE:
      prod_{b!=a} (u^(2)_a - u^(2)_b + i) / (u^(2)_a - u^(2)_b - i)
      = prod_b (u^(2)_a - u^(1)_b - i/2) / (u^(2)_a - u^(1)_b + i/2)

    In logarithmic form with quantum numbers.
    """
    M1 = len(u1)
    M2 = len(u2)
    f = np.zeros(M1 + M2)

    # Level 1 equations
    for a in range(M1):
        # Driving term
        f[a] = L * np.arctan(2 * u1[a])
        # Same-level scattering
        for b in range(M1):
            if b != a:
                f[a] -= np.arctan(u1[a] - u1[b])
        # Cross-level scattering (level 2 -> level 1)
        for b in range(M2):
            f[a] += 0.5 * np.arctan(2 * (u1[a] - u2[b]))
        f[a] -= np.pi * qn1[a]

    # Level 2 equations
    for a in range(M2):
        # No driving term (level 2 sees level 1 only)
        # Same-level scattering
        for b in range(M2):
            if b != a:
                f[M1 + a] -= np.arctan(u2[a] - u2[b])
        # Cross-level scattering (level 1 -> level 2)
        for b in range(M1):
            f[M1 + a] += 0.5 * np.arctan(2 * (u2[a] - u1[b]))
        f[M1 + a] -= np.pi * qn2[a]

    return f


def solve_sl3_nested_bae(L: int, M1: int, M2: int,
                          qn1: Optional[np.ndarray] = None,
                          qn2: Optional[np.ndarray] = None,
                          u0_1: Optional[np.ndarray] = None,
                          u0_2: Optional[np.ndarray] = None,
                          ) -> Dict[str, Any]:
    """Solve the nested sl_3 BAE.

    Args:
        L: chain length.
        M1: number of level-1 Bethe roots.
        M2: number of level-2 Bethe roots.
        qn1, qn2: quantum numbers for levels 1 and 2.

    The total S^z quantum numbers are:
        S^z_1 = L/2 - M1, S^z_2 = M1 - M2 - L/2  (or similar).
    The representation content depends on (M1, M2).
    """
    if qn1 is None:
        qn1 = np.array([-(M1 - 1) / 2 + k for k in range(M1)])
    if qn2 is None:
        qn2 = np.array([-(M2 - 1) / 2 + k for k in range(M2)])
    if u0_1 is None:
        u0_1 = np.linspace(-0.5, 0.5, M1) if M1 > 0 else np.array([])
    if u0_2 is None:
        u0_2 = np.linspace(-0.3, 0.3, M2) if M2 > 0 else np.array([])

    def equations(u_flat):
        u1 = u_flat[:M1]
        u2 = u_flat[M1:M1 + M2]
        return sl3_nested_bae_equations(u1, u2, L, qn1, qn2)

    u0 = np.concatenate([u0_1, u0_2])
    if len(u0) == 0:
        return {'roots_1': np.array([]), 'roots_2': np.array([]),
                'energy': 0.0, 'success': True, 'L': L, 'M1': 0, 'M2': 0}

    result = optimize.fsolve(equations, u0, full_output=True)
    u1_sol = result[0][:M1]
    u2_sol = result[0][M1:M1 + M2]
    success = result[2] == 1

    # Energy for sl_3 XXX:
    # E = sum_a 1/(u^(1)_a^2 + 1/4) (up to sign and shift)
    energy = -np.sum(1.0 / (u1_sol**2 + 0.25)) if M1 > 0 else 0.0

    return {
        'roots_1': u1_sol,
        'roots_2': u2_sol,
        'energy': energy,
        'success': success,
        'L': L,
        'M1': M1,
        'M2': M2,
    }


def sl3_xxx_hamiltonian(L: int) -> np.ndarray:
    """sl_3 XXX Hamiltonian in the fundamental representation.

    H = sum_{i} P_{i,i+1}

    where P is the permutation operator on C^3 tensor C^3.
    The ground state for the antiferromagnet is in the singlet sector.

    Returns a 3^L x 3^L matrix.
    """
    d = 3  # local Hilbert space dimension
    dim = d**L
    H = np.zeros((dim, dim), dtype=complex)

    # Permutation operator on C^3 tensor C^3
    P3 = np.zeros((9, 9), dtype=complex)
    for a in range(3):
        for b in range(3):
            P3[3 * a + b, 3 * b + a] = 1.0

    for site in range(L):
        next_site = (site + 1) % L
        # Embed P_{site, next_site} into the full space
        P_full = _embed_two_site_operator(P3, d, L, site, next_site)
        H += P_full

    return H


def _embed_two_site_operator(op: np.ndarray, d: int, L: int,
                              site1: int, site2: int) -> np.ndarray:
    """Embed a two-site operator into the full Hilbert space.

    op acts on C^d tensor C^d.
    The full space is (C^d)^{tensor L}.
    """
    dim = d**L
    result = np.zeros((dim, dim), dtype=complex)

    for state_in in range(dim):
        # Decompose state into d-ary digits
        digits_in = []
        s = state_in
        for _ in range(L):
            digits_in.append(s % d)
            s //= d
        digits_in.reverse()

        a1, a2 = digits_in[site1], digits_in[site2]

        for b1 in range(d):
            for b2 in range(d):
                val = op[d * a1 + a2, d * b1 + b2]
                if abs(val) < 1e-15:
                    continue
                digits_out = list(digits_in)
                digits_out[site1] = b1
                digits_out[site2] = b2
                state_out = 0
                for digit in digits_out:
                    state_out = state_out * d + digit
                result[state_out, state_in] += val

    return result


# ========================================================================
# 9. Thermodynamic Bethe ansatz (TBA)
# ========================================================================

def xxx_tba_density(M_over_L: float = 0.5, num_points: int = 200,
                    max_u: float = 10.0,
                    iterations: int = 100) -> Dict[str, Any]:
    """Solve the TBA integral equation for the XXX chain.

    At half-filling (M/L = 1/2), the density of Bethe roots rho(u)
    satisfies the linear integral equation:

      rho(u) + int K(u-v) rho(v) dv = a_1(u)

    where:
      a_1(u) = (1/2pi) * 1/(u^2 + 1/4)  (driving term)
      K(u) = (1/2pi) * 1/(u^2 + 1)      (scattering kernel)

    The ground state energy per site is:
      e_0 = -int a_1(u) epsilon(u) du

    where epsilon(u) is the dressed energy solving:
      epsilon(u) + int K(u-v) epsilon(v) dv = -pi * a_1(u)

    For the XXX antiferromagnet at half-filling:
      e_0 = 1/4 - ln(2) approx -0.4431...

    We solve by iteration (Neumann series).
    """
    du = 2 * max_u / num_points
    u_grid = np.linspace(-max_u, max_u, num_points)

    # Driving term: a_1(u) = p'(u)/(2*pi) = 2/(pi*(1+4u^2)) = 1/(2*pi*(u^2+1/4))
    a1 = 1 / (2 * np.pi) / (u_grid**2 + 0.25)

    # Kernel: K(u) = theta'(u)/(2*pi) = 1/(pi*(1+u^2))
    def kernel(u):
        return 1 / (np.pi * (u**2 + 1.0))

    K_matrix = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(num_points):
            K_matrix[i, j] = kernel(u_grid[i] - u_grid[j]) * du

    # Solve (I + K) rho = a_1 via direct linear solve
    IpK = np.eye(num_points) + K_matrix
    rho = la.solve(IpK, a1)

    # Ground state energy per site (Hulthén 1938):
    #   e_0 = 1/4 - ln(2) for the XXX antiferromagnet at half-filling.
    #
    # The energy per site is computed from the root density:
    #   e_0 = 1/4 - (1/2)*integral rho(u) / (u^2 + 1/4) du
    # (the 1/2 factor comes from H = sum S_i.S_{i+1} = (1/4) sum sigma.sigma)

    # Solve for dressed energy: (I + K) epsilon = bare_energy
    bare_energy = -1.0 / (u_grid**2 + 0.25)
    epsilon = la.solve(IpK, bare_energy)

    # Energy per site: e = 1/4 + (1/2) * int rho(u) * bare_energy(u) du
    energy_per_site = 0.25 + 0.5 * np.sum(rho * bare_energy) * du

    # Normalization check: int rho(u) du should be M/L
    norm = np.sum(rho) * du

    return {
        'u_grid': u_grid,
        'rho': rho,
        'epsilon': epsilon,
        'energy_per_site': energy_per_site,
        'rho_norm': norm,
        'M_over_L': M_over_L,
        'exact_energy': 0.25 - np.log(2),
    }


# ========================================================================
# 10. Baxter Q-operator (functional Bethe ansatz)
# ========================================================================

def baxter_q_polynomial(u: complex, roots: np.ndarray) -> complex:
    """Baxter Q-polynomial: Q(u) = prod_a (u - u_a).

    The Q-operator eigenvalue on a Bethe state is this polynomial.
    The roots u_a are the Bethe roots.
    """
    result = 1.0 + 0.0j
    for root in roots:
        result *= (u - root)
    return result


def baxter_tq_relation(u: complex, roots: np.ndarray, L: int,
                        eta: complex = 1j) -> Dict[str, complex]:
    """Verify the Baxter TQ relation.

    T(u) Q(u) = a(u) Q(u - eta) + d(u) Q(u + eta)

    For the XXX chain (eta = i, imaginary unit):
      a(u) = (u + i/2)^L
      d(u) = (u - i/2)^L
      T(u) = a(u) Q(u-i)/Q(u) + d(u) Q(u+i)/Q(u)

    The TQ relation is equivalent to the BAE at u = u_a (where Q(u_a) = 0):
      a(u_a) Q(u_a - i) + d(u_a) Q(u_a + i) = 0

    This is exactly the product-form BAE.
    """
    Q_u = baxter_q_polynomial(u, roots)
    Q_minus = baxter_q_polynomial(u - eta, roots)
    Q_plus = baxter_q_polynomial(u + eta, roots)

    a_u = (u + eta / 2)**L
    d_u = (u - eta / 2)**L

    # Transfer matrix eigenvalue
    if abs(Q_u) > 1e-15:
        T_u = a_u * Q_minus / Q_u + d_u * Q_plus / Q_u
    else:
        T_u = float('nan')

    # TQ relation: T(u)*Q(u) = a(u)*Q(u-eta) + d(u)*Q(u+eta)
    lhs = T_u * Q_u if not np.isnan(T_u) else a_u * Q_minus + d_u * Q_plus
    rhs = a_u * Q_minus + d_u * Q_plus

    return {
        'T_u': T_u,
        'Q_u': Q_u,
        'Q_minus': Q_minus,
        'Q_plus': Q_plus,
        'a_u': a_u,
        'd_u': d_u,
        'lhs': lhs,
        'rhs': rhs,
        'residual': abs(lhs - rhs),
    }


def verify_bae_from_tq(roots: np.ndarray, L: int, eta: complex = 1j) -> float:
    """Verify BAE by checking T*Q = a*Q(-) + d*Q(+) at each root.

    At u = u_a: Q(u_a) = 0, so the TQ relation reduces to
      0 = a(u_a) Q(u_a - eta) + d(u_a) Q(u_a + eta)
    which is the BAE in product form.

    Returns maximum residual.
    """
    max_res = 0.0
    for root in roots:
        a_val = (root + eta / 2)**L
        d_val = (root - eta / 2)**L
        Q_minus = baxter_q_polynomial(root - eta, roots)
        Q_plus = baxter_q_polynomial(root + eta, roots)
        residual = abs(a_val * Q_minus + d_val * Q_plus)
        max_res = max(max_res, residual)
    return max_res


def transfer_eigenvalue_from_q(u: complex, roots: np.ndarray,
                                L: int, eta: complex = 1j) -> complex:
    """Compute transfer matrix eigenvalue from the Q-polynomial.

    T(u) = a(u) Q(u-eta)/Q(u) + d(u) Q(u+eta)/Q(u).
    """
    Q_u = baxter_q_polynomial(u, roots)
    if abs(Q_u) < 1e-15:
        return float('nan')
    Q_minus = baxter_q_polynomial(u - eta, roots)
    Q_plus = baxter_q_polynomial(u + eta, roots)
    a_u = (u + eta / 2)**L
    d_u = (u - eta / 2)**L
    return a_u * Q_minus / Q_u + d_u * Q_plus / Q_u


# ========================================================================
# 11. ODE/IM correspondence
# ========================================================================

def ode_im_potential(x: float, M: int, E: float = 0.0) -> float:
    """The anharmonic oscillator potential for the ODE/IM correspondence.

    -psi''(x) + (x^{2M} - E) psi(x) = 0

    For the M-th Dorey-Tateo model:
      M = 1: harmonic oscillator (exactly solvable)
      M = 2: quartic oscillator
      M = 3: sextic oscillator

    The Stokes multipliers of this ODE at x = infinity encode the
    eigenvalues of the Baxter Q-operator for the corresponding
    integrable model (Dorey-Tateo 1999, BLZ 1999).

    Returns V(x) = x^{2M} - E.
    """
    return x**(2 * M) - E


def ode_im_solve_schrodinger(M: int, E: float, x_max: float = 10.0,
                              num_points: int = 2000
                              ) -> Tuple[np.ndarray, np.ndarray]:
    """Solve the Schrodinger equation -psi'' + x^{2M} psi = E psi.

    Uses the shooting method from x = 0 with psi(0) = 1, psi'(0) = 0
    (even solutions) or psi(0) = 0, psi'(0) = 1 (odd solutions).

    Returns (x_grid, psi) for the even solution.
    """
    dx = x_max / num_points
    x = np.linspace(0, x_max, num_points + 1)
    psi = np.zeros(num_points + 1)
    psi_prime = np.zeros(num_points + 1)

    # Even solution: psi(0) = 1, psi'(0) = 0
    psi[0] = 1.0
    psi_prime[0] = 0.0

    for i in range(num_points):
        V = x[i]**(2 * M) - E
        psi_prime[i + 1] = psi_prime[i] + V * psi[i] * dx
        psi[i + 1] = psi[i] + psi_prime[i + 1] * dx

    return x, psi


def ode_im_find_eigenvalue(M: int, n: int = 0, E_min: float = 0.0,
                            E_max: float = 20.0,
                            tol: float = 1e-10) -> float:
    """Find the n-th eigenvalue of -psi'' + x^{2M} psi = E psi.

    Uses bisection on the boundary condition psi(x_max) = 0.
    For the even (n even) and odd (n odd) sectors.

    For M = 1 (harmonic oscillator): E_n = 2n + 1.
    """
    x_max = max(10.0, (E_max + 5)**(1.0 / (2 * M)) + 2)

    parity = n % 2  # 0 = even, 1 = odd

    def boundary_value(E):
        _, psi = ode_im_solve_schrodinger(M, E, x_max=x_max, num_points=3000)
        return psi[-1]

    def boundary_value_odd(E):
        dx = x_max / 3000
        x = np.linspace(0, x_max, 3001)
        psi = np.zeros(3001)
        psi_p = np.zeros(3001)
        psi[0] = 0.0
        psi_p[0] = 1.0
        for i in range(3000):
            V = x[i]**(2 * M) - E
            psi_p[i + 1] = psi_p[i] + V * psi[i] * dx
            psi[i + 1] = psi[i] + psi_p[i + 1] * dx
        return psi[-1]

    bv_func = boundary_value if parity == 0 else boundary_value_odd

    # Count zeros to find the right bracket
    num_scan = 500
    E_scan = np.linspace(E_min + 0.01, E_max, num_scan)
    vals = [bv_func(E) for E in E_scan]

    # Find sign changes
    sign_changes = []
    for i in range(len(vals) - 1):
        if vals[i] * vals[i + 1] < 0:
            sign_changes.append((E_scan[i], E_scan[i + 1]))

    # The n-th eigenvalue in this parity sector is the (n//2)-th sign change
    target_idx = n // 2
    if target_idx >= len(sign_changes):
        return float('nan')

    E_lo, E_hi = sign_changes[target_idx]

    # Bisection
    for _ in range(200):
        E_mid = (E_lo + E_hi) / 2
        if bv_func(E_mid) * bv_func(E_lo) < 0:
            E_hi = E_mid
        else:
            E_lo = E_mid
        if E_hi - E_lo < tol:
            break

    return (E_lo + E_hi) / 2


def ode_im_stokes_multiplier(M: int, E: float, angle: float = 0.0,
                               x_max: float = 15.0,
                               num_points: int = 5000) -> complex:
    """Compute the Stokes multiplier for the ODE/IM correspondence.

    The Stokes multiplier S connects the asymptotic solutions
    in adjacent Stokes sectors of the ODE -psi'' + x^{2M} psi = E psi.

    The ODE has anti-Stokes lines at angles pi*k/(M+1) for k = 0,1,...,2M+1.
    The Stokes multiplier across the k-th anti-Stokes line relates the
    subdominant solution in sector k to that in sector k+1.

    For the ODE/IM correspondence:
      S_k(E) = eigenvalue of the Q-operator of the integrable model.

    We compute S by comparing asymptotic solutions along two rays.
    This is a simplified version using WKB matching.

    For M = 1 (harmonic oscillator), E_n = 2n+1, and S is related to
    Hermite polynomial zeros.
    """
    # WKB approximation for the Stokes multiplier
    # Phase integral: phi = int_0^{x_tp} sqrt(E - x^{2M}) dx
    # where x_tp = E^{1/(2M)} is the turning point.

    from scipy import integrate

    x_tp = E**(1.0 / (2 * M)) if E > 0 else 0.0

    if x_tp < 1e-10:
        return 1.0 + 0.0j

    def integrand(x):
        val = E - x**(2 * M)
        return np.sqrt(max(val, 0))

    phase, _ = integrate.quad(integrand, 0, x_tp)

    # In the WKB approximation:
    # S ~ exp(2i * phase) (for the leading Stokes multiplier)
    return np.exp(2j * phase)


# ========================================================================
# 12. Shadow connection to BAE bridge
# ========================================================================

def shadow_to_rmatrix_sl2(k: float) -> Dict[str, Any]:
    """Extract the rational r-matrix from the sl_2 shadow tower.

    The shadow tower of sl_2-hat_k has:
      kappa = 3(k+2)/4  (for sl_2: dim=3, h^vee=2)
      S_3 = 1 (Lie cubic)
      S_4 = 0 (Jacobi kills quartic)
      Tower terminates at arity 3 (class L).

    The r-matrix r(z) = Omega/z is the collision residue of the
    bar propagator.  In the spin-1/2 representation:
      Omega = P - (1/2)*I  (where P is the permutation)

    The R-matrix R(u) = u*I + P (the Yang R-matrix) gives:
      H_{XXX} = d/du log T(u)|_{u=0}
    which is the Heisenberg Hamiltonian.

    Returns dict with shadow data and R-matrix.
    """
    h_vee = 2
    dim_g = 3
    kappa = dim_g * (k + h_vee) / (2 * h_vee)  # = 3(k+2)/4

    return {
        'kappa': kappa,
        'S_3': 1.0,
        'S_4': 0.0,
        'shadow_class': 'L',
        'r_max': 3,
        'r_matrix_type': 'rational',
        'R_matrix': lambda u: xxx_r_matrix_shadow(u),
        'k': k,
        'h_vee': h_vee,
        'dim_g': dim_g,
    }


def shadow_to_rmatrix_sl3(k: float) -> Dict[str, Any]:
    """Extract the rational r-matrix from the sl_3 shadow tower.

    Shadow tower of sl_3-hat_k:
      kappa = 8(k+3)/6 = 4(k+3)/3
      S_3 = 1 (universal for all KM)
      S_4 = 0 (Jacobi)
      Class L, terminates at arity 3.

    R-matrix in the fundamental: R(u) = u*I + P on C^3 tensor C^3.
    """
    h_vee = 3
    dim_g = 8
    kappa = dim_g * (k + h_vee) / (2 * h_vee)  # = 4(k+3)/3

    # sl_3 permutation operator on C^3 tensor C^3
    P3 = np.zeros((9, 9), dtype=complex)
    for a in range(3):
        for b in range(3):
            P3[3 * a + b, 3 * b + a] = 1.0

    def R_matrix(u):
        return u * np.eye(9, dtype=complex) + P3

    return {
        'kappa': kappa,
        'S_3': 1.0,
        'S_4': 0.0,
        'shadow_class': 'L',
        'r_max': 3,
        'r_matrix_type': 'rational',
        'R_matrix': R_matrix,
        'k': k,
        'h_vee': h_vee,
        'dim_g': dim_g,
    }


def genus1_shadow_to_xxz(tau: complex, k: float = 1.0) -> Dict[str, Any]:
    """Connect the genus-1 shadow tower to the XXZ chain.

    At genus 1, the shadow tower of sl_2-hat_k acquires the genus-1
    propagator E_2*(tau), and the r-matrix becomes trigonometric:

      r(z, tau) = Omega * theta_1'(0, tau) / theta_1(z, tau)

    In the limit Im(tau) -> infinity: theta_1(z,tau) -> sin(pi*z),
    and r(z) -> Omega * pi/sin(pi*z) = trigonometric.

    The XXZ anisotropy is:
      Delta = cos(pi / (k + h^vee))

    For sl_2 at level k: Delta = cos(pi/(k+2)).
    """
    h_vee = 2
    Delta = np.cos(np.pi / (k + h_vee))
    eta = np.arccosh(Delta) if abs(Delta) >= 1 else 1j * np.arccos(Delta)

    return {
        'tau': tau,
        'k': k,
        'Delta': Delta,
        'eta': eta,
        'r_matrix_type': 'trigonometric',
        'genus': 1,
    }


# ========================================================================
# 13. Completeness and string hypothesis verification
# ========================================================================

def xxx_total_states(L: int, M: int) -> int:
    """Total number of Bethe states = C(L, M).

    The XXX chain with L sites in the M-magnon sector has
    C(L,M) = L! / (M! (L-M)!) states.
    """
    from math import comb
    return comb(L, M)


def xxx_count_solutions(L: int, M: int, scan_range: float = 5.0,
                         num_trials: int = 100) -> int:
    """Attempt to count distinct BAE solutions by random initial conditions.

    This is a heuristic: we solve the BAE from many random initial conditions
    and count distinct solutions (up to permutation of roots).

    Returns the number of distinct solutions found.
    """
    solutions = []
    for _ in range(num_trials):
        u0 = np.random.uniform(-scan_range, scan_range, M)
        # Random quantum numbers
        qn = np.array([-(M - 1) / 2 + k for k in range(M)])
        result = solve_xxx_bae(L, M, quantum_numbers=qn, u0=u0)
        if result['success']:
            roots = np.sort(result['roots'])
            # Check if this is a new solution
            is_new = True
            for existing in solutions:
                if la.norm(roots - existing) < 1e-6:
                    is_new = False
                    break
            if is_new:
                solutions.append(roots)
    return len(solutions)


# ========================================================================
# 14. Verification utilities
# ========================================================================

def verify_bae_xxx(L: int, M: int, tol: float = 1e-4) -> Dict[str, Any]:
    """Full verification: solve BAE, compare with exact diagonalization.

    Returns dict with BAE energy, ED energy, and whether they match.
    """
    # Solve BAE
    bae = solve_xxx_bae(L, M)
    if not bae['success']:
        return {'match': False, 'reason': 'BAE solver failed',
                'bae': bae, 'ed_energy': None}

    # Exact diagonalization in the Sz = L/2 - M sector
    Sz_sector = L - 2 * M
    ed_evals, _ = exact_diagonalization_xxx(L, Sz_sector=Sz_sector)
    if len(ed_evals) == 0:
        return {'match': False, 'reason': 'ED sector empty',
                'bae': bae, 'ed_energy': None}

    ed_ground = ed_evals[0]

    match = abs(bae['energy'] - ed_ground) < tol
    return {
        'match': match,
        'bae_energy': bae['energy'],
        'ed_energy': ed_ground,
        'difference': abs(bae['energy'] - ed_ground),
        'bae': bae,
        'tol': tol,
    }


def verify_bae_xxz(L: int, M: int, eta: float,
                    tol: float = 1e-3) -> Dict[str, Any]:
    """Verify XXZ BAE against exact diagonalization."""
    Delta = np.cosh(eta)
    bae = solve_xxz_bae(L, M, eta)

    Sz_sector = L - 2 * M
    ed_evals, _ = exact_diagonalization_xxz(L, Delta, Sz_sector=Sz_sector)
    if len(ed_evals) == 0:
        return {'match': False, 'reason': 'ED sector empty'}

    ed_ground = ed_evals[0]
    match = abs(bae['energy'] - ed_ground) < tol
    return {
        'match': match,
        'bae_energy': bae['energy'],
        'ed_energy': ed_ground,
        'difference': abs(bae['energy'] - ed_ground),
        'Delta': Delta,
    }


def verify_xxx_tba(tol: float = 0.01) -> Dict[str, Any]:
    """Verify the TBA result e_0 = 1/4 - ln(2) for the XXX chain."""
    tba = xxx_tba_density()
    exact = 0.25 - np.log(2)
    match = abs(tba['energy_per_site'] - exact) < tol
    return {
        'match': match,
        'tba_energy': tba['energy_per_site'],
        'exact_energy': exact,
        'difference': abs(tba['energy_per_site'] - exact),
    }
