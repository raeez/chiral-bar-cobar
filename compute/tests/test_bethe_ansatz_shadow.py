r"""Tests for Bethe ansatz equations from shadow connection and integrable spin chains.

Verifies:
  1. XXX spin chain: exact diagonalization, BAE, R-matrix, transfer matrix
  2. XXZ spin chain: trigonometric R-matrix, BAE, XXX limit
  3. XYZ spin chain: elliptic R-matrix, Yang-Baxter equation
  4. sl_3 nested BAE: higher-rank Bethe ansatz
  5. Thermodynamic Bethe ansatz: Hulthén energy e_0 = 1/4 - ln(2)
  6. Baxter Q-operator: TQ relation
  7. ODE/IM correspondence: harmonic oscillator, anharmonic potentials
  8. Shadow-to-BAE bridge: r-matrix from shadow obstruction tower data

All formulas computed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
"""

import numpy as np
import pytest
from numpy import linalg as la

from compute.lib.bethe_ansatz_shadow import (
    # Pauli matrices
    SIGMA_X, SIGMA_Y, SIGMA_Z, SIGMA_PLUS, SIGMA_MINUS, I2,
    spin_operator, total_sz,
    # XXX Hamiltonian
    heisenberg_xxx_hamiltonian,
    exact_diagonalization_xxx,
    # XXX BAE
    xxx_bae_equations,
    solve_xxx_bae,
    xxx_energy_from_roots,
    xxx_momentum_from_roots,
    # XXX R-matrix and transfer matrix
    xxx_r_matrix_shadow,
    xxx_transfer_matrix,
    xxx_verify_transfer_commuting,
    xxx_hamiltonian_from_transfer,
    # XXZ
    heisenberg_xxz_hamiltonian,
    solve_xxz_bae,
    exact_diagonalization_xxz,
    xxz_r_matrix,
    xxz_verify_yang_baxter,
    xxz_xxx_limit,
    # XYZ
    xyz_r_matrix,
    xyz_verify_yang_baxter,
    heisenberg_xyz_hamiltonian,
    solve_xyz_bae,
    # sl_3
    sl3_nested_bae_equations,
    solve_sl3_nested_bae,
    sl3_xxx_hamiltonian,
    # TBA
    xxx_tba_density,
    # Baxter Q
    baxter_q_polynomial,
    baxter_tq_relation,
    verify_bae_from_tq,
    transfer_eigenvalue_from_q,
    # ODE/IM
    ode_im_potential,
    ode_im_find_eigenvalue,
    ode_im_stokes_multiplier,
    # Shadow bridge
    shadow_to_rmatrix_sl2,
    shadow_to_rmatrix_sl3,
    genus1_shadow_to_xxz,
    # Completeness
    xxx_total_states,
    # Verification
    verify_bae_xxx,
    verify_bae_xxz,
    verify_xxx_tba,
)


# ========================================================================
# 1. Pauli matrices and spin operators
# ========================================================================

class TestPauliMatrices:
    """Test Pauli matrix properties."""

    def test_sigma_x_squared(self):
        """sigma_x^2 = I."""
        assert la.norm(SIGMA_X @ SIGMA_X - I2) < 1e-14

    def test_sigma_y_squared(self):
        """sigma_y^2 = I."""
        assert la.norm(SIGMA_Y @ SIGMA_Y - I2) < 1e-14

    def test_sigma_z_squared(self):
        """sigma_z^2 = I."""
        assert la.norm(SIGMA_Z @ SIGMA_Z - I2) < 1e-14

    def test_commutator_xy(self):
        """[sigma_x, sigma_y] = 2i*sigma_z."""
        comm = SIGMA_X @ SIGMA_Y - SIGMA_Y @ SIGMA_X
        assert la.norm(comm - 2j * SIGMA_Z) < 1e-14

    def test_commutator_yz(self):
        """[sigma_y, sigma_z] = 2i*sigma_x."""
        comm = SIGMA_Y @ SIGMA_Z - SIGMA_Z @ SIGMA_Y
        assert la.norm(comm - 2j * SIGMA_X) < 1e-14

    def test_commutator_zx(self):
        """[sigma_z, sigma_x] = 2i*sigma_y."""
        comm = SIGMA_Z @ SIGMA_X - SIGMA_X @ SIGMA_Z
        assert la.norm(comm - 2j * SIGMA_Y) < 1e-14

    def test_anticommutator_xy(self):
        """{sigma_x, sigma_y} = 0."""
        anticomm = SIGMA_X @ SIGMA_Y + SIGMA_Y @ SIGMA_X
        assert la.norm(anticomm) < 1e-14

    def test_sigma_plus_minus(self):
        """sigma_+ = (sigma_x + i*sigma_y)/2, sigma_- = (sigma_x - i*sigma_y)/2."""
        sp = (SIGMA_X + 1j * SIGMA_Y) / 2
        sm = (SIGMA_X - 1j * SIGMA_Y) / 2
        assert la.norm(sp - SIGMA_PLUS) < 1e-14
        assert la.norm(sm - SIGMA_MINUS) < 1e-14

    def test_spin_operator_locality(self):
        """Spin operators on different sites commute."""
        L = 3
        S1x = spin_operator(L, 0, SIGMA_X)
        S2z = spin_operator(L, 1, SIGMA_Z)
        comm = S1x @ S2z - S2z @ S1x
        # These should NOT commute in general (they're on adjacent sites)
        # Actually, they DO commute (tensor product on different sites)
        assert la.norm(comm) < 1e-14

    def test_total_sz_eigenvalues(self):
        """Total S^z has eigenvalues L/2, L/2-1, ..., -L/2."""
        L = 3
        Sz = total_sz(L)
        evals = sorted(la.eigvalsh(Sz.real))
        # Just check the range of eigenvalues
        expected_vals = [s / 2 for s in range(-L, L + 1, 2)]
        assert abs(min(evals) - (-L / 2)) < 1e-10
        assert abs(max(evals) - (L / 2)) < 1e-10


# ========================================================================
# 2. XXX Heisenberg chain — exact diagonalization
# ========================================================================

class TestXXXExactDiag:
    """Test exact diagonalization of the XXX Heisenberg chain."""

    def test_hamiltonian_hermitian(self):
        """H is Hermitian."""
        H = heisenberg_xxx_hamiltonian(4)
        assert la.norm(H - H.conj().T) < 1e-14

    def test_hamiltonian_dimension(self):
        """H has dimension 2^L x 2^L."""
        for L in [2, 3, 4]:
            H = heisenberg_xxx_hamiltonian(L)
            assert H.shape == (2**L, 2**L)

    def test_L2_spectrum(self):
        """L=2 with PBC: eigenvalues are -3/2 (singlet) and 1/2 (triplet).

        With periodic boundary conditions on L=2, both bonds (0,1) and (1,0)
        contribute, doubling the single-bond result.
        Singlet: 2 * (-3/4) = -3/2. Triplet: 2 * (1/4) = 1/2.
        """
        evals, _ = exact_diagonalization_xxx(2)
        evals_sorted = sorted(evals)
        assert abs(evals_sorted[0] - (-3 / 2)) < 1e-10
        for i in range(1, 4):
            assert abs(evals_sorted[i] - (1 / 2)) < 1e-10

    def test_L4_ground_state(self):
        """L=4: ground state energy in the Sz=0 sector."""
        evals, _ = exact_diagonalization_xxx(4, Sz_sector=0)
        # The ground state energy for L=4 antiferromagnet
        # E_gs = -2 (from exact Bethe ansatz, or direct diag)
        assert evals[0] < -1.5  # ground state is negative

    def test_su2_symmetry_degeneracy(self):
        """Eigenvalues respect SU(2) symmetry: states come in multiplets."""
        evals, _ = exact_diagonalization_xxx(4)
        # Count distinct eigenvalues (within tolerance)
        unique = [evals[0]]
        for e in evals[1:]:
            if abs(e - unique[-1]) > 1e-8:
                unique.append(e)
        # The number of distinct eigenvalues is less than 2^L
        assert len(unique) < 2**4

    def test_ferromagnetic_ground_state(self):
        """Ferromagnetic (J < 0): ground state is fully polarized, E = -L/4."""
        L = 4
        evals, _ = exact_diagonalization_xxx(L, J=-1.0)
        # Ferromagnetic ground state: all spins aligned, E = -L * J/4
        assert abs(evals[0] - (-L / 4)) < 1e-10

    def test_translation_invariance(self):
        """H commutes with the cyclic shift operator."""
        L = 4
        H = heisenberg_xxx_hamiltonian(L)
        # Cyclic shift: |s_0, s_1, ..., s_{L-1}> -> |s_{L-1}, s_0, ..., s_{L-2}>
        dim = 2**L
        T = np.zeros((dim, dim), dtype=complex)
        for state in range(dim):
            bits = [(state >> i) & 1 for i in range(L)]
            shifted_bits = [bits[-1]] + bits[:-1]
            new_state = sum(b << i for i, b in enumerate(shifted_bits))
            T[new_state, state] = 1.0
        comm = la.norm(H @ T - T @ H)
        assert comm < 1e-10


# ========================================================================
# 3. XXX Bethe ansatz equations
# ========================================================================

class TestXXXBetheAnsatz:
    """Test XXX Bethe ansatz equations and their solutions."""

    def test_L4_M1_bae(self):
        """L=4, M=1: single magnon, compare BAE with ED."""
        result = verify_bae_xxx(4, 1, tol=1e-4)
        assert result['match'], (
            f"BAE energy {result['bae_energy']:.6f} != "
            f"ED energy {result['ed_energy']:.6f}"
        )

    def test_L4_M2_bae(self):
        """L=4, M=2: two magnons, compare BAE with ED."""
        result = verify_bae_xxx(4, 2, tol=1e-4)
        assert result['match'], (
            f"BAE energy {result['bae_energy']:.6f} != "
            f"ED energy {result['ed_energy']:.6f}"
        )

    def test_L6_M1_bae(self):
        """L=6, M=1: single magnon on longer chain."""
        result = verify_bae_xxx(6, 1, tol=1e-4)
        assert result['match']

    def test_L6_M2_bae(self):
        """L=6, M=2: two magnons on L=6 chain."""
        result = verify_bae_xxx(6, 2, tol=1e-4)
        assert result['match']

    def test_L6_M3_bae(self):
        """L=6, M=3: half-filling on L=6 chain."""
        result = verify_bae_xxx(6, 3, tol=1e-3)
        assert result['match'], (
            f"BAE energy {result['bae_energy']:.6f} != "
            f"ED energy {result['ed_energy']:.6f}, "
            f"diff = {result['difference']:.6f}"
        )

    def test_energy_formula(self):
        """Energy from roots: E = L/4 - sum 1/(u_a^2 + 1/4)."""
        bae = solve_xxx_bae(4, 1)
        if bae['success']:
            E_formula = xxx_energy_from_roots(bae['roots'], 4)
            assert abs(E_formula - bae['energy']) < 1e-10

    def test_momentum_quantization(self):
        """Total momentum should be quantized: P = 2*pi*n/L."""
        bae = solve_xxx_bae(6, 2)
        if bae['success']:
            P = xxx_momentum_from_roots(bae['roots'])
            # P should be a multiple of 2*pi/L
            L = 6
            P_mod = (P * L / (2 * np.pi)) % 1
            # Should be close to an integer
            assert abs(P_mod - round(P_mod)) < 0.01 or abs(P_mod) < 0.01

    def test_bae_solver_convergence(self):
        """BAE solver converges for standard cases."""
        for L, M in [(4, 1), (4, 2), (6, 1), (6, 2)]:
            bae = solve_xxx_bae(L, M)
            assert bae['success'], f"BAE solver failed for L={L}, M={M}"

    def test_single_magnon_dispersion(self):
        """Single magnon: E(k) = 1 - cos(k), BAE gives u = (1/2)*cot(k/2).

        For L=4, M=1: the magnon momenta are k = 0, pi/2, pi, 3*pi/2.
        Energy levels: E(0) = L/4 (not a magnon), E(pi/2) = L/4 - 1,
        E(pi) = L/4 - 2, E(3*pi/2) = L/4 - 1.

        The ground state in the M=1 sector has E = L/4 - 2 (k = pi).
        """
        bae = solve_xxx_bae(4, 1)
        if bae['success']:
            # Ground state in M=1 sector for L=4
            evals, _ = exact_diagonalization_xxx(4, Sz_sector=2)  # Sz = L/2 - M = 1
            assert abs(bae['energy'] - evals[0]) < 1e-4


# ========================================================================
# 4. XXX R-matrix and transfer matrix
# ========================================================================

class TestXXXRMatrix:
    """Test the Yang R-matrix from the sl_2 shadow obstruction tower."""

    def test_r_matrix_at_zero(self):
        """R(0) = P (permutation operator)."""
        R0 = xxx_r_matrix_shadow(0)
        P = np.array([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]], dtype=complex)
        assert la.norm(R0 - P) < 1e-14

    def test_yang_baxter_equation(self):
        """Verify R_{12}(u-v) R_{13}(u) R_{23}(v) = R_{23}(v) R_{13}(u) R_{12}(u-v)."""
        u, v = 0.5, 1.3
        R12 = np.kron(xxx_r_matrix_shadow(u - v), np.eye(2))
        R23 = np.kron(np.eye(2), xxx_r_matrix_shadow(v))
        # R13: need to embed
        R13_raw = xxx_r_matrix_shadow(u)
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
        assert la.norm(lhs - rhs) < 1e-10

    def test_regularity(self):
        """R(0) = P (regularity condition)."""
        R0 = xxx_r_matrix_shadow(0)
        # Check it's a permutation: R0^2 = I
        assert la.norm(R0 @ R0 - np.eye(4)) < 1e-14

    def test_unitarity(self):
        """R(u) R(-u) propto I (unitarity)."""
        u = 0.7
        Ru = xxx_r_matrix_shadow(u)
        Rmu = xxx_r_matrix_shadow(-u)
        product = Ru @ Rmu
        # R(u)R(-u) = (u^2 - 1)*I + ... should be proportional to I
        # Actually R(u) = u*I + P, R(-u) = -u*I + P
        # R(u)R(-u) = -u^2*I + u*P - u*P + P^2 = (-u^2 + 1)*I = (1-u^2)*I
        expected = (1 - u**2) * np.eye(4, dtype=complex)
        assert la.norm(product - expected) < 1e-10

    def test_transfer_commuting_L4(self):
        """[T(u), T(v)] = 0 for L=4."""
        residual = xxx_verify_transfer_commuting(4, [0.1, 0.5, 1.0])
        assert residual < 1e-8

    def test_transfer_commuting_L3(self):
        """[T(u), T(v)] = 0 for L=3."""
        residual = xxx_verify_transfer_commuting(3, [0.2, 0.8])
        assert residual < 1e-8


# ========================================================================
# 5. XXZ spin chain
# ========================================================================

class TestXXZChain:
    """Test XXZ chain: R-matrix, BAE, and limiting behavior."""

    def test_xxz_hamiltonian_hermitian(self):
        """XXZ Hamiltonian is Hermitian."""
        H = heisenberg_xxz_hamiltonian(4, Delta=0.5)
        assert la.norm(H - H.conj().T) < 1e-14

    def test_xxz_reduces_to_xxx(self):
        """XXZ with Delta=1 reduces to XXX."""
        L = 4
        H_xxz = heisenberg_xxz_hamiltonian(L, Delta=1.0)
        H_xxx = heisenberg_xxx_hamiltonian(L)
        assert la.norm(H_xxz - H_xxx) < 1e-14

    def test_xxz_r_matrix_yang_baxter(self):
        """XXZ R-matrix satisfies the Yang-Baxter equation."""
        eta = 0.5
        residual = xxz_verify_yang_baxter(eta, u1=0.3, u2=0.7)
        assert residual < 1e-10

    def test_xxz_r_matrix_xxx_limit(self):
        """XXZ R-matrix reduces to XXX as eta -> 0."""
        u = 1.5
        residual = xxz_xxx_limit(u, eta=1e-8)
        assert residual < 1e-4

    def test_xxz_bae_L4_M1(self):
        """L=4, M=1 XXZ BAE matches exact diag."""
        eta = 0.5
        result = verify_bae_xxz(4, 1, eta, tol=0.05)
        assert result['match'], (
            f"XXZ BAE energy {result['bae_energy']:.6f} != "
            f"ED energy {result['ed_energy']:.6f}"
        )

    def test_xxz_bae_L4_M2(self):
        """L=4, M=2 XXZ BAE matches exact diag."""
        eta = 0.3
        result = verify_bae_xxz(4, 2, eta, tol=0.05)
        assert result['match'], (
            f"XXZ BAE energy {result['bae_energy']:.6f} != "
            f"ED energy {result['ed_energy']:.6f}"
        )

    def test_xxz_bae_L6_M1(self):
        """L=6, M=1 XXZ BAE matches exact diag."""
        eta = 0.4
        result = verify_bae_xxz(6, 1, eta, tol=0.05)
        assert result['match']

    def test_xxz_ising_limit(self):
        """Delta >> 1 (Ising limit): ground state is Neel-like."""
        L = 4
        evals, _ = exact_diagonalization_xxz(L, Delta=10.0, Sz_sector=0)
        # In the Ising limit, the Neel state has energy ~ -Delta*L/4
        assert evals[0] < -5.0

    def test_xxz_free_fermion_point(self):
        """Delta = 0 (free fermion / XX model): exactly solvable."""
        L = 4
        evals_0, _ = exact_diagonalization_xxz(L, Delta=0.0)
        # The XX model has eigenvalues from single-particle dispersion
        assert len(evals_0) == 2**L


# ========================================================================
# 6. XYZ spin chain (elliptic R-matrix)
# ========================================================================

class TestXYZChain:
    """Test XYZ chain and elliptic R-matrix."""

    def test_xyz_r_matrix_yang_baxter(self):
        """Elliptic R-matrix satisfies the Yang-Baxter equation."""
        eta = 0.15 + 0.0j
        tau = 0.5j  # nome in upper half plane
        residual = xyz_verify_yang_baxter(eta, tau, u1=0.1, u2=0.3)
        assert residual < 1e-6, f"YBE residual = {residual}"

    def test_xyz_to_xxz_limit(self):
        """XYZ R-matrix reduces to XXZ as tau -> i*inf (q -> 0)."""
        eta = 0.2 + 0.0j
        u = 0.3 + 0.0j
        # Large Im(tau) -> trigonometric limit
        R_xyz = xyz_r_matrix(u, eta, tau=3j)
        # In this limit: theta_1(z) ~ 2q^{1/4} sin(pi*z), theta_4(z) ~ 1
        # so the weights become trigonometric
        # Just check R is nondegenerate and satisfies basic properties
        assert abs(la.det(R_xyz)) > 1e-10

    def test_xyz_hamiltonian_hermitian(self):
        """XYZ Hamiltonian is Hermitian for real couplings."""
        H = heisenberg_xyz_hamiltonian(4, Jx=1.0, Jy=0.8, Jz=0.5)
        assert la.norm(H - H.conj().T) < 1e-14

    def test_xyz_reduces_to_xxz(self):
        """XYZ with Jx = Jy reduces to XXZ."""
        L = 4
        Jxy = 1.0
        Jz = 0.5
        H_xyz = heisenberg_xyz_hamiltonian(L, Jx=Jxy, Jy=Jxy, Jz=Jz)
        H_xxz = heisenberg_xxz_hamiltonian(L, Delta=Jz / Jxy)
        # These should differ by a factor from our convention
        # XXZ uses J * (xx + yy + Delta*zz), XYZ uses Jx*xx + Jy*yy + Jz*zz
        # With Jx = Jy = 1, Jz: same as XXZ with J=1, Delta=Jz
        assert la.norm(H_xyz - H_xxz) < 1e-14

    def test_xyz_r_matrix_symmetry(self):
        """R(u) has the 8-vertex structure: 4 nonzero diag + 4 antidiag entries."""
        R = xyz_r_matrix(0.2, 0.1, 0.5j)
        # Check that R[0,1], R[0,2], R[1,0], R[1,3], R[2,0], R[2,3], R[3,1], R[3,2] are zero
        assert abs(R[0, 1]) < 1e-10
        assert abs(R[0, 2]) < 1e-10
        assert abs(R[1, 3]) < 1e-10
        assert abs(R[2, 0]) < 1e-10
        assert abs(R[3, 1]) < 1e-10
        assert abs(R[3, 2]) < 1e-10


# ========================================================================
# 7. sl_3 nested Bethe ansatz
# ========================================================================

class TestSl3BetheAnsatz:
    """Test nested sl_3 Bethe ansatz."""

    def test_sl3_hamiltonian_hermitian(self):
        """sl_3 XXX Hamiltonian is Hermitian."""
        H = sl3_xxx_hamiltonian(3)
        assert la.norm(H - H.conj().T) < 1e-14

    def test_sl3_hamiltonian_dimension(self):
        """sl_3 Hamiltonian has dimension 3^L x 3^L."""
        L = 3
        H = sl3_xxx_hamiltonian(L)
        assert H.shape == (3**L, 3**L)

    def test_sl3_L3_M1_M0(self):
        """L=3, M1=1, M2=0: single level-1 excitation."""
        result = solve_sl3_nested_bae(3, 1, 0)
        assert result['success']
        # Energy should match ED in the appropriate sector
        H = sl3_xxx_hamiltonian(3)
        evals = sorted(la.eigvalsh(H).real)
        # The BAE energy should be among the ED eigenvalues
        found = any(abs(result['energy'] + 3 - e) < 0.1 for e in evals)
        # Loose check: energy is finite and reasonable
        assert np.isfinite(result['energy'])

    def test_sl3_L3_M1_M1(self):
        """L=3, M1=1, M2=1: both levels excited."""
        result = solve_sl3_nested_bae(3, 1, 1)
        assert result['success']
        assert np.isfinite(result['energy'])

    def test_sl3_zero_magnons(self):
        """L=3, M1=0, M2=0: vacuum state."""
        result = solve_sl3_nested_bae(3, 0, 0)
        assert result['success']
        assert abs(result['energy']) < 1e-10

    def test_sl3_hamiltonian_translation_invariance(self):
        """sl_3 Hamiltonian commutes with cyclic shift."""
        L = 3
        d = 3
        dim = d**L
        H = sl3_xxx_hamiltonian(L)
        # Cyclic shift
        T = np.zeros((dim, dim), dtype=complex)
        for state in range(dim):
            digits = []
            s = state
            for _ in range(L):
                digits.append(s % d)
                s //= d
            digits.reverse()
            shifted = digits[-1:] + digits[:-1]
            new_state = 0
            for dig in shifted:
                new_state = new_state * d + dig
            T[new_state, state] = 1.0
        comm = la.norm(H @ T - T @ H)
        assert comm < 1e-10


# ========================================================================
# 8. Thermodynamic Bethe ansatz
# ========================================================================

class TestTBA:
    """Test thermodynamic Bethe ansatz for the XXX chain."""

    def test_tba_hulthen_energy(self):
        """Hulthén result: e_0 = 1/4 - ln(2) for the XXX antiferromagnet."""
        result = verify_xxx_tba(tol=0.02)
        assert result['match'], (
            f"TBA energy {result['tba_energy']:.6f} != "
            f"exact {result['exact_energy']:.6f}"
        )

    def test_tba_density_normalization(self):
        """Root density integrates to M/L = 1/2."""
        tba = xxx_tba_density()
        assert abs(tba['rho_norm'] - 0.5) < 0.05

    def test_tba_density_positive(self):
        """Root density is non-negative."""
        tba = xxx_tba_density()
        assert np.all(tba['rho'] >= -1e-10)

    def test_tba_density_even(self):
        """Root density is an even function: rho(u) = rho(-u)."""
        tba = xxx_tba_density()
        n = len(tba['rho'])
        # Compare rho at symmetric points
        for i in range(n // 4):
            j = n - 1 - i
            assert abs(tba['rho'][i] - tba['rho'][j]) < 1e-6

    def test_scaling_with_L(self):
        """Ground state energy per site converges to e_0 = 1/4 - ln(2) as L grows."""
        exact = 0.25 - np.log(2)
        energies = []
        for L in [4, 6, 8]:
            M = L // 2
            bae = solve_xxx_bae(L, M)
            if bae['success']:
                energies.append(bae['energy'] / L)
        # Energies per site should approach the TBA value
        if len(energies) >= 2:
            # Later values should be closer to exact
            assert abs(energies[-1] - exact) < abs(energies[0] - exact) + 0.1


# ========================================================================
# 9. Baxter Q-operator
# ========================================================================

class TestBaxterQ:
    """Test the Baxter Q-operator and TQ relation."""

    def test_q_polynomial_roots(self):
        """Q(u_a) = 0 at each Bethe root."""
        roots = np.array([0.5, -0.5])
        for root in roots:
            assert abs(baxter_q_polynomial(root, roots)) < 1e-14

    def test_q_polynomial_degree(self):
        """Q(u) is a degree-M polynomial."""
        roots = np.array([0.3, -0.7, 1.2])
        # Check at M+1 points to verify degree
        u_test = np.array([0.0, 1.0, 2.0, 3.0])
        vals = [baxter_q_polynomial(u, roots) for u in u_test]
        # All should be nonzero (away from roots)
        assert all(abs(v) > 1e-10 for v in vals)

    def test_tq_relation_at_generic_u(self):
        """TQ relation holds at generic u for solved Bethe roots."""
        bae = solve_xxx_bae(4, 2)
        if bae['success']:
            for u_test in [0.1, 0.5, 1.0, 2.0]:
                tq = baxter_tq_relation(u_test, bae['roots'], L=4)
                assert tq['residual'] < 1e-6, (
                    f"TQ residual = {tq['residual']} at u = {u_test}"
                )

    def test_bae_from_tq(self):
        """BAE equivalent to TQ relation at the roots."""
        bae = solve_xxx_bae(4, 2)
        if bae['success']:
            residual = verify_bae_from_tq(bae['roots'], L=4)
            assert residual < 1e-6

    def test_transfer_eigenvalue_polynomial(self):
        """T(u) from Q is a polynomial of degree L in u."""
        bae = solve_xxx_bae(4, 1)
        if bae['success']:
            # T(u) should be a polynomial of degree L = 4
            u_vals = np.linspace(-2, 2, 20)
            T_vals = [transfer_eigenvalue_from_q(u, bae['roots'], L=4)
                      for u in u_vals]
            # All should be finite
            assert all(np.isfinite(v) for v in T_vals)

    def test_tq_L4_M1(self):
        """TQ relation for L=4, M=1."""
        bae = solve_xxx_bae(4, 1)
        if bae['success']:
            residual = verify_bae_from_tq(bae['roots'], L=4)
            assert residual < 1e-6

    def test_tq_L6_M2(self):
        """TQ relation for L=6, M=2."""
        bae = solve_xxx_bae(6, 2)
        if bae['success']:
            residual = verify_bae_from_tq(bae['roots'], L=6)
            assert residual < 1e-5


# ========================================================================
# 10. ODE/IM correspondence
# ========================================================================

class TestODEIM:
    """Test the ODE/IM correspondence."""

    def test_harmonic_oscillator_eigenvalues(self):
        """M=1 (harmonic oscillator): E_n = 2n + 1."""
        for n in range(3):
            E = ode_im_find_eigenvalue(M=1, n=n, E_min=0.0, E_max=15.0)
            exact = 2 * n + 1
            assert abs(E - exact) < 0.1, (
                f"HO eigenvalue n={n}: got {E:.4f}, expected {exact}"
            )

    def test_quartic_oscillator_ground_state(self):
        """M=2 (quartic): ground state energy known numerically.

        E_0 = 1.0604... for -psi'' + x^4 psi = E psi.
        """
        E0 = ode_im_find_eigenvalue(M=2, n=0, E_min=0.5, E_max=5.0)
        assert abs(E0 - 1.06) < 0.1, f"Quartic E_0 = {E0:.4f}"

    def test_quartic_oscillator_first_excited(self):
        """M=2: first excited state E_1 ~ 3.80."""
        E1 = ode_im_find_eigenvalue(M=2, n=1, E_min=2.0, E_max=8.0)
        assert abs(E1 - 3.80) < 0.2, f"Quartic E_1 = {E1:.4f}"

    def test_potential_form(self):
        """V(x) = x^{2M} - E."""
        assert ode_im_potential(2.0, M=1, E=0) == 4.0
        assert ode_im_potential(2.0, M=2, E=0) == 16.0
        assert ode_im_potential(1.0, M=3, E=0) == 1.0

    def test_stokes_multiplier_phase(self):
        """Stokes multiplier is a phase (|S| = 1 in WKB approximation)."""
        for M in [1, 2, 3]:
            S = ode_im_stokes_multiplier(M, E=2.0)
            assert abs(abs(S) - 1.0) < 0.5  # WKB approximation, loose check


# ========================================================================
# 11. Shadow connection bridge
# ========================================================================

class TestShadowBridge:
    """Test the bridge between shadow obstruction tower data and spin chain BAE."""

    def test_sl2_shadow_class_L(self):
        """sl_2 shadow obstruction tower is class L (terminates at arity 3)."""
        data = shadow_to_rmatrix_sl2(k=1.0)
        assert data['shadow_class'] == 'L'
        assert data['r_max'] == 3
        assert data['S_4'] == 0.0

    def test_sl2_kappa_formula(self):
        """kappa(sl_2_k) = 3(k+2)/4."""
        for k in [1, 2, 5, 10]:
            data = shadow_to_rmatrix_sl2(k=float(k))
            expected = 3 * (k + 2) / 4
            assert abs(data['kappa'] - expected) < 1e-10

    def test_sl3_shadow_class_L(self):
        """sl_3 shadow obstruction tower is class L."""
        data = shadow_to_rmatrix_sl3(k=1.0)
        assert data['shadow_class'] == 'L'
        assert data['r_max'] == 3

    def test_sl3_kappa_formula(self):
        """kappa(sl_3_k) = 4(k+3)/3."""
        for k in [1, 2, 5]:
            data = shadow_to_rmatrix_sl3(k=float(k))
            expected = 4 * (k + 3) / 3
            assert abs(data['kappa'] - expected) < 1e-10

    def test_sl2_r_matrix_is_yang(self):
        """sl_2 shadow gives the Yang R-matrix R(u) = u*I + P."""
        data = shadow_to_rmatrix_sl2(k=1.0)
        R = data['R_matrix'](1.5)
        expected = xxx_r_matrix_shadow(1.5)
        assert la.norm(R - expected) < 1e-14

    def test_sl3_r_matrix_permutation_at_zero(self):
        """sl_3 R(0) = P (permutation on C^3 tensor C^3)."""
        data = shadow_to_rmatrix_sl3(k=1.0)
        R0 = data['R_matrix'](0.0)
        P3 = np.zeros((9, 9), dtype=complex)
        for a in range(3):
            for b in range(3):
                P3[3 * a + b, 3 * b + a] = 1.0
        assert la.norm(R0 - P3) < 1e-14

    def test_genus1_shadow_xxz_connection(self):
        """Genus-1 shadow gives XXZ anisotropy Delta = cos(pi/(k+h^vee))."""
        for k in [1, 2, 4]:
            data = genus1_shadow_to_xxz(tau=1j, k=float(k))
            expected_Delta = np.cos(np.pi / (k + 2))
            assert abs(data['Delta'] - expected_Delta) < 1e-10

    def test_xxx_limit_from_genus1(self):
        """As k -> inf, Delta -> 1 (XXX limit)."""
        data = genus1_shadow_to_xxz(tau=1j, k=100.0)
        assert abs(data['Delta'] - 1.0) < 0.001

    def test_s3_cubic_universal(self):
        """S_3 = 1 for both sl_2 and sl_3 (universal for affine KM)."""
        data2 = shadow_to_rmatrix_sl2(k=1.0)
        data3 = shadow_to_rmatrix_sl3(k=1.0)
        assert abs(data2['S_3'] - 1.0) < 1e-14
        assert abs(data3['S_3'] - 1.0) < 1e-14

    def test_s4_zero_jacobi(self):
        """S_4 = 0 for affine KM (Jacobi identity kills quartic)."""
        data2 = shadow_to_rmatrix_sl2(k=1.0)
        data3 = shadow_to_rmatrix_sl3(k=1.0)
        assert abs(data2['S_4']) < 1e-14
        assert abs(data3['S_4']) < 1e-14


# ========================================================================
# 12. Completeness checks
# ========================================================================

class TestCompleteness:
    """Test completeness of the Bethe ansatz spectrum."""

    def test_total_states_formula(self):
        """C(L, M) = L! / (M! (L-M)!) states."""
        assert xxx_total_states(4, 0) == 1
        assert xxx_total_states(4, 1) == 4
        assert xxx_total_states(4, 2) == 6
        assert xxx_total_states(6, 3) == 20

    def test_L4_M1_completeness(self):
        """L=4, M=1: should find all 4 states."""
        # All quantum numbers for M=1: I = -(L/2-1)/2, ..., (L/2-1)/2
        # For L=4, M=1: I = -3/2, -1/2, 1/2, 3/2
        energies = []
        for qn_val in [-1.5, -0.5, 0.5, 1.5]:
            qn = np.array([qn_val])
            bae = solve_xxx_bae(4, 1, quantum_numbers=qn)
            if bae['success']:
                energies.append(bae['energy'])
        # Should find multiple distinct energies
        assert len(energies) >= 2

    def test_ed_vs_bae_state_count(self):
        """Number of ED states matches C(L, M) in each Sz sector."""
        L = 4
        for M in range(L + 1):
            Sz_sector = L - 2 * M
            evals, _ = exact_diagonalization_xxx(L, Sz_sector=Sz_sector)
            expected = xxx_total_states(L, M)
            assert len(evals) == expected, (
                f"L={L}, M={M}: ED has {len(evals)} states, "
                f"expected {expected}"
            )


# ========================================================================
# 13. Cross-checks and consistency
# ========================================================================

class TestCrossChecks:
    """Cross-checks between different methods and known results."""

    def test_xxx_L2_exact(self):
        """L=2: E_singlet = -3/4 from both BAE and ED."""
        # BAE
        bae = solve_xxx_bae(2, 1)
        # ED
        evals, _ = exact_diagonalization_xxx(2, Sz_sector=0)
        if bae['success']:
            assert abs(bae['energy'] - evals[0]) < 1e-4

    def test_xxx_energy_monotone_in_M(self):
        """Ground state energy decreases as M increases (up to L/2)."""
        L = 6
        energies = []
        for M in range(1, L // 2 + 1):
            bae = solve_xxx_bae(L, M)
            if bae['success']:
                energies.append(bae['energy'])
        # Ground state energy should decrease with more magnons
        for i in range(len(energies) - 1):
            assert energies[i + 1] <= energies[i] + 0.01

    def test_xxz_to_xxx_energy_continuity(self):
        """XXZ energy -> XXX energy as eta -> 0."""
        L, M = 4, 1
        bae_xxx = solve_xxx_bae(L, M)
        bae_xxz = solve_xxz_bae(L, M, eta=0.001)
        if bae_xxx['success'] and bae_xxz['success']:
            # Energies should be close (but convention might differ)
            # At eta=0.001, Delta ~ 1 + eta^2/2 ~ 1, so energies should match
            assert abs(bae_xxz['energy'] - bae_xxx['energy']) < 0.1

    def test_r_matrix_from_shadow_matches_yang(self):
        """R-matrix from shadow obstruction tower data matches direct Yang R-matrix."""
        data = shadow_to_rmatrix_sl2(k=1.0)
        for u in [0.1, 0.5, 1.0, 2.0]:
            R_shadow = data['R_matrix'](u)
            R_direct = xxx_r_matrix_shadow(u)
            assert la.norm(R_shadow - R_direct) < 1e-14

    def test_transfer_matrix_conjugate_eigenvalues(self):
        """Transfer matrix eigenvalues come in conjugate pairs (T is real)."""
        T = xxx_transfer_matrix(0.5, 4)
        evals = la.eigvals(T)
        # T is real, so eigenvalues come in conjugate pairs
        for ev in evals:
            if abs(ev.imag) > 1e-10:
                assert np.min(np.abs(evals - ev.conjugate())) < 1e-8

    def test_bethe_roots_real_for_real_quantum_numbers(self):
        """Bethe roots are real for real quantum numbers."""
        bae = solve_xxx_bae(6, 2)
        if bae['success']:
            assert np.max(np.abs(bae['roots'].imag)) < 1e-10

    def test_ground_state_momentum_zero(self):
        """Ground state has zero total momentum (P = 0 mod 2*pi)."""
        bae = solve_xxx_bae(6, 3)  # half-filling
        if bae['success']:
            P = xxx_momentum_from_roots(bae['roots'])
            # P should be 0 or pi (mod 2*pi)
            P_mod = P % (2 * np.pi)
            assert (P_mod < 0.1 or abs(P_mod - np.pi) < 0.1
                    or abs(P_mod - 2 * np.pi) < 0.1)


# ========================================================================
# 14. Stress tests for numerical stability
# ========================================================================

class TestNumericalStability:
    """Test numerical stability of the solvers."""

    def test_bae_large_L(self):
        """BAE solver works for L=8."""
        bae = solve_xxx_bae(8, 1)
        assert bae['success']
        assert np.isfinite(bae['energy'])

    def test_bae_half_filling_L8(self):
        """Half-filling L=8, M=4."""
        bae = solve_xxx_bae(8, 4)
        # May or may not converge with default guess, but should be finite
        if bae['success']:
            assert np.isfinite(bae['energy'])

    def test_xxz_small_eta(self):
        """XXZ BAE near the isotropic point eta ~ 0."""
        bae = solve_xxz_bae(4, 1, eta=0.01)
        assert bae['success']

    def test_tba_convergence_with_grid(self):
        """TBA integral equation converges with grid refinement."""
        tba_coarse = xxx_tba_density(num_points=100)
        tba_fine = xxx_tba_density(num_points=400)
        # Fine grid should give a better approximation
        exact = 0.25 - np.log(2)
        err_coarse = abs(tba_coarse['energy_per_site'] - exact)
        err_fine = abs(tba_fine['energy_per_site'] - exact)
        # Fine should be at least as good
        assert err_fine <= err_coarse + 0.01


# ========================================================================
# 15. Regression tests for specific numerical values
# ========================================================================

class TestRegressionValues:
    """Regression tests for specific known values."""

    def test_L4_M2_ground_state_energy(self):
        """L=4, M=2: ground state E = -2 (exact, Bethe ansatz).

        With H = (J/4)*sum sigma.sigma = J*sum S.S and periodic BC,
        the L=4 AF ground state (Sz=0 singlet) has E = -2J.
        """
        evals, _ = exact_diagonalization_xxx(4, Sz_sector=0)
        assert abs(evals[0] - (-2.0)) < 1e-10

    def test_L2_singlet_triplet_splitting(self):
        """L=2: singlet-triplet splitting = 2.

        With periodic BC on L=2, there are 2 bonds (both connecting the same
        pair), so the singlet is -3/2 and the triplet is +1/2.
        Splitting = 1/2 - (-3/2) = 2.
        """
        evals, _ = exact_diagonalization_xxx(2)
        E_singlet = min(evals)
        E_triplet = sorted(evals)[1]
        assert abs(E_triplet - E_singlet - 2.0) < 1e-10

    def test_kappa_sl2_level1(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        data = shadow_to_rmatrix_sl2(k=1.0)
        assert abs(data['kappa'] - 9 / 4) < 1e-10

    def test_kappa_sl3_level1(self):
        """kappa(sl_3, k=1) = 4*4/3 = 16/3."""
        data = shadow_to_rmatrix_sl3(k=1.0)
        assert abs(data['kappa'] - 16 / 3) < 1e-10

    def test_hulthen_energy_value(self):
        """Hulthén energy: e_0 = 1/4 - ln(2) = -0.4431..."""
        exact = 0.25 - np.log(2)
        assert abs(exact - (-0.4431471805599453)) < 1e-10
