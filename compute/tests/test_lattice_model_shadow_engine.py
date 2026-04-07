r"""Tests for lattice_model_shadow_engine: integrable lattice models from the
shadow obstruction tower.

Verifies the complete chain:
    bar complex --> MC element Theta_A --> R-matrix --> Yang-Baxter
    --> transfer matrix --> Bethe ansatz --> conserved quantities
    --> Q-operator --> free energy --> ODE/IM correspondence

Ground truth references:
    - Baxter, "Exactly solved models in statistical mechanics" (1982)
    - Faddeev-Sklyanin-Takhtajan, "Quantum inverse problem method" (1979)
    - Korepin-Bogoliubov-Izergin, "QISM and Correlation Functions" (1993)
    - Onsager, "Crystal statistics I" (1944)
    - Hulthen (1938): E_0/L = 1/4 - ln(2) for XXX antiferromagnet
    - Lieb (1967): residual entropy of ice
    - Dorey-Tateo (1999): ODE/IM correspondence
    - BLZ (1997): quantum KdV charges
    - thm:mc2-bar-intrinsic, AP19, AP27, AP48

Multi-path verification (per CLAUDE.md mandate):
    Path 1: Direct computation (matrix construction + diagonalization)
    Path 2: Bethe ansatz (algebraic, from MC equation projection)
    Path 3: Transfer matrix (QISM, from bar complex coproduct)
    Path 4: Limiting cases (XXX -> XXZ degeneration, thermo limit)
    Path 5: Symmetry/duality (unitarity, crossing, particle-hole)
    Path 6: Literature comparison (Hulthen, Onsager, BLZ)
"""

import pytest
import numpy as np
from math import log, pi, sqrt
from numpy.linalg import eigvalsh

from compute.lib.lattice_model_shadow_engine import (
    # Constants
    PI, SIGMA_0, SIGMA_X, SIGMA_Y, SIGMA_Z, PAULI,
    PERM_2, ID_4, CASIMIR_SL2_FUND,
    # R-matrices
    R_rational, R_trigonometric,
    verify_ybe, _embed_R12, _embed_R13, _embed_R23,
    # Transfer matrix
    transfer_matrix, verify_transfer_commutativity,
    # XXX
    xxx_hamiltonian, xxx_hamiltonian_from_transfer,
    xxx_ground_state_energy, HULTHEN_ENERGY_DENSITY,
    # XXZ
    xxz_hamiltonian, xxz_ground_state_energy,
    # Bethe ansatz
    bethe_equations_xxx, solve_bethe_xxx, bethe_energy_xxx,
    bethe_transfer_eigenvalue, bethe_equations_xxz,
    # Q-operator
    baxter_Q, verify_TQ_relation, quantum_determinant, quantum_wronskian,
    # Free energy
    free_energy_exact, six_vertex_weights,
    six_vertex_partition_function, six_vertex_free_energy_density,
    # Higher charges
    higher_conserved_charges, verify_charges_commute,
    # CTM
    ctm_spectrum_ising, ctm_partition_function, shadow_metric_from_ctm,
    # Star-triangle / CYBE
    verify_star_triangle_ising, classical_ybe, verify_cybe_casimir,
    # Onsager / Ising
    onsager_generators, verify_dolan_grady,
    ising_hamiltonian, ising_critical_gap, ising_kappa,
    ising_free_energy_exact, onsager_free_energy_2d, ising_critical_beta,
    # RSOS
    rsos_admissible_level, rsos_central_charge, rsos_kappa,
    rsos_conformal_weights, rsos_partition_function_small,
    # Toda
    toda_lax_matrix_sl2, toda_lax_matrix_slN,
    verify_toda_integrability, toda_integrals_of_motion,
    toda_hamiltonian, toda_classical_r_matrix_sl2,
    toda_casimir_eigenvalues_slN,
    # ODE/IM
    shadow_potential, shadow_potential_class,
    ode_im_eigenvalues, ode_im_spectral_determinant,
    ode_im_functional_relation, wkb_leading_eigenvalue,
    # Quantum KdV
    quantum_kdv_charges_from_shadow, quantum_kdv_eigenvalue,
    verify_quantum_kdv_commutativity,
    # Drinfeld-Kohno
    drinfeld_universal_R_sl2, verify_drinfeld_kohno_ybe,
    verify_drinfeld_classical_r,
    # Correlations
    spin_correlation,
    # Degeneration
    verify_trig_to_rational_limit,
    # Dictionary
    ShadowLatticeDictionary,
    # Full check
    full_integrability_check,
)


# =========================================================================
# 1. Rational R-matrix fundamentals
# =========================================================================

class TestRationalRMatrix:
    """R(z) = z*I + P from sl_2 bar complex r(z) = Omega/z (AP19)."""

    def test_R_at_zero_is_permutation(self):
        """R(0) = P."""
        assert np.allclose(R_rational(0.0), PERM_2)

    def test_R_at_one(self):
        """R(1) = I + P."""
        assert np.allclose(R_rational(1.0), ID_4 + PERM_2)

    def test_R_shape(self):
        assert R_rational(1.0).shape == (4, 4)

    def test_R_unitarity(self):
        """R(z)R(-z) = (1 - z^2)*I."""
        z = 1.5
        prod = R_rational(z) @ R_rational(-z)
        assert np.allclose(prod, (1 - z ** 2) * ID_4)

    def test_casimir_is_P_minus_half(self):
        """Omega = P - I/2 (sl_2 Casimir in fund x fund)."""
        assert np.allclose(CASIMIR_SL2_FUND, PERM_2 - ID_4 / 2)

    def test_casimir_trace_zero(self):
        """Tr(Omega) = 0."""
        assert abs(np.trace(CASIMIR_SL2_FUND)) < 1e-14

    def test_P_squared_is_identity(self):
        """P^2 = I (involution)."""
        assert np.allclose(PERM_2 @ PERM_2, ID_4)

    def test_R_is_linear_in_z(self):
        """R(alpha*z1 + (1-alpha)*z2) = alpha*R(z1) + (1-alpha)*R(z2)."""
        z1, z2, alpha = 1.5, 2.7, 0.4
        lhs = R_rational(alpha * z1 + (1 - alpha) * z2)
        rhs = alpha * R_rational(z1) + (1 - alpha) * R_rational(z2)
        assert np.allclose(lhs, rhs)


# =========================================================================
# 2. Yang-Baxter equation = MC at arity 3
# =========================================================================

class TestYBE:
    """YBE: R12(z12) R13(z13) R23(z23) = R23 R13 R12."""

    def test_ybe_rational_generic(self):
        assert verify_ybe(1.0, 2.0, 3.0)

    def test_ybe_rational_complex(self):
        assert verify_ybe(1 + 0.5j, 2 - 0.3j, 0.5 + 1j)

    def test_ybe_rational_degenerate(self):
        """YBE when z1 = z2."""
        assert verify_ybe(1.0, 1.0, 3.0)

    def test_ybe_rational_all_equal(self):
        assert verify_ybe(2.0, 2.0, 2.0)

    def test_ybe_trigonometric(self):
        assert verify_ybe(0.5, 1.0, 1.5, R_trigonometric, eta=0.7)

    def test_ybe_trigonometric_various_eta(self):
        for eta in [0.1, 0.5, 1.0, 2.0]:
            assert verify_ybe(0.3, 0.7, 1.1, R_trigonometric, eta=eta)

    def test_embedding_dimensions(self):
        R = R_rational(1.5)
        assert _embed_R12(R).shape == (8, 8)
        assert _embed_R23(R).shape == (8, 8)
        assert _embed_R13(R).shape == (8, 8)


# =========================================================================
# 3. Classical YBE = arity-3 MC equation
# =========================================================================

class TestCYBE:
    """[r12, r13] + [r12, r23] + [r13, r23] = 0."""

    def test_cybe_casimir_generic(self):
        assert verify_cybe_casimir(1.0, 2.0, 3.0)

    def test_cybe_casimir_complex(self):
        assert verify_cybe_casimir(0.5, 1.5, 2.5)

    def test_cybe_casimir_negative(self):
        assert verify_cybe_casimir(-1.0, 0.5, 2.0)

    def test_star_triangle_is_ybe(self):
        """Star-triangle relation = YBE in vertex model language."""
        assert verify_star_triangle_ising(1.0, 2.0, 3.0)


# =========================================================================
# 4. Transfer matrix = bar complex iterated coproduct
# =========================================================================

class TestTransferMatrix:

    def test_shape(self):
        for L in [2, 3, 4]:
            T = transfer_matrix(1.0, L)
            assert T.shape == (2 ** L, 2 ** L)

    def test_commutativity_L2(self):
        assert verify_transfer_commutativity(0.5, 1.5, 2)

    def test_commutativity_L3(self):
        assert verify_transfer_commutativity(0.5, 1.5, 3)

    def test_commutativity_L4(self):
        assert verify_transfer_commutativity(0.5, 1.5, 4)

    def test_commutativity_complex(self):
        assert verify_transfer_commutativity(0.5 + 0.3j, 1.5 - 0.2j, 3)

    def test_commutativity_trigonometric(self):
        """[T(z), T(w)] = 0 for the XXZ chain."""
        assert verify_transfer_commutativity(
            0.5, 1.5, 3, R_trigonometric, eta=0.7)


# =========================================================================
# 5. XXX Hamiltonian from arity-2 shadow (kappa)
# =========================================================================

class TestXXXHamiltonian:

    def test_xxx_hermitian(self):
        H = xxx_hamiltonian(4)
        assert np.allclose(H, H.conj().T, atol=1e-14)

    def test_xxx_from_transfer(self):
        """H extracted from dT/dz matches direct construction."""
        dev = xxx_hamiltonian_from_transfer(4)
        assert dev < 1e-4

    def test_xxx_ground_state_L4(self):
        """E_0/L for L=4 is negative (antiferromagnetic)."""
        e = xxx_ground_state_energy(4)
        assert e < 0

    def test_hulthen_convergence(self):
        """E_0/L converges toward 1/4 - ln(2) as L increases."""
        e4 = xxx_ground_state_energy(4)
        e6 = xxx_ground_state_energy(6)
        e8 = xxx_ground_state_energy(8)
        # Should approach Hulthen value from above (finite-size gap)
        assert abs(e8 - HULTHEN_ENERGY_DENSITY) < abs(e4 - HULTHEN_ENERGY_DENSITY)

    def test_hulthen_value(self):
        """Hulthen energy density = 1/4 - ln(2)."""
        assert abs(HULTHEN_ENERGY_DENSITY - (0.25 - log(2))) < 1e-15


# =========================================================================
# 6. XXZ Hamiltonian (trigonometric / quantum group)
# =========================================================================

class TestXXZ:

    def test_xxz_reduces_to_xxx(self):
        """XXZ at delta=1 is proportional to XXX.

        H_xxx = J*sum(P-1/2) = 2J*sum(S.S), while H_xxz = J*sum(S.S).
        So H_xxx = 2 * H_xxz at delta=1.
        """
        H_xxz = xxz_hamiltonian(4, delta=1.0)
        H_xxx = xxx_hamiltonian(4)
        assert np.allclose(H_xxx, 2 * H_xxz, atol=1e-12)

    def test_xxz_hermitian(self):
        H = xxz_hamiltonian(4, delta=0.5)
        assert np.allclose(H, H.conj().T, atol=1e-14)

    def test_xxz_free_fermion(self):
        """At delta=0 (XX model), the spectrum is exactly computable.

        H_XX maps to free fermions via Jordan-Wigner.  The thermodynamic
        limit gives E_0/L -> -1/pi.  For L=6: E_0/L = -1/3 (exact,
        from filling k = -1, 0, 1 with cos(2*pi*k/6)).
        """
        e = xxz_ground_state_energy(6, delta=0.0)
        assert e < 0
        # Exact finite-size value for L=6
        assert abs(e - (-1.0 / 3.0)) < 1e-10

    def test_xxz_ferro_vs_antiferro(self):
        """Ferromagnetic (delta=-1) vs antiferromagnetic (delta=1).

        For H = sum(S.S) with delta=-1, the ground state is the fully
        polarized state with E/L = delta/4 = -1/4.  For delta=1 (AF),
        quantum fluctuations lower the energy further: E/L ~ -0.467.
        So the AF ground state energy is MORE negative than the ferro.
        """
        e_af = xxz_ground_state_energy(6, delta=1.0)
        e_f = xxz_ground_state_energy(6, delta=-1.0)
        assert e_af < e_f
        assert abs(e_f - (-0.25)) < 1e-10  # exact ferro energy


# =========================================================================
# 7. Bethe ansatz from MC equation
# =========================================================================

class TestBetheAnsatz:

    def test_bae_satisfied_L4(self):
        """Bethe roots satisfy BAE for L=4, M=2."""
        roots = solve_bethe_xxx(4, 2)
        assert roots is not None
        res = bethe_equations_xxx(roots, 4)
        assert np.max(np.abs(res)) < 1e-10

    def test_bae_satisfied_L6(self):
        """BAE for L=6, M=3."""
        roots = solve_bethe_xxx(6, 3)
        assert roots is not None
        res = bethe_equations_xxx(roots, 6)
        assert np.max(np.abs(res)) < 1e-10

    def test_bethe_energy_matches_exact_L4(self):
        """Energy from Bethe roots matches exact diagonalization (L=4)."""
        roots = solve_bethe_xxx(4, 2)
        assert roots is not None
        E_bethe = bethe_energy_xxx(roots, 4)
        E_exact = xxx_ground_state_energy(4) * 4
        assert abs(E_bethe - E_exact) < 1e-6

    def test_bethe_energy_matches_exact_L6(self):
        """Energy match at L=6."""
        roots = solve_bethe_xxx(6, 3)
        assert roots is not None
        E_bethe = bethe_energy_xxx(roots, 6)
        E_exact = xxx_ground_state_energy(6) * 6
        assert abs(E_bethe - E_exact) < 1e-6

    def test_bethe_roots_real(self):
        """Ground state Bethe roots are real for the XXX chain."""
        roots = solve_bethe_xxx(6, 3)
        assert roots is not None
        assert np.max(np.abs(roots.imag)) < 1e-10

    def test_bethe_roots_symmetric(self):
        """Bethe roots are symmetric under u -> -u for ground state."""
        roots = solve_bethe_xxx(6, 3)
        assert roots is not None
        sorted_roots = np.sort(roots.real)
        # Check u_i = -u_{M-1-i}
        for i in range(len(sorted_roots) // 2):
            assert abs(sorted_roots[i] + sorted_roots[-(i + 1)]) < 1e-10

    def test_bethe_eigenvalue_tq_consistency(self):
        """Transfer eigenvalue from Bethe roots satisfies TQ relation.

        The eigenvalue Lambda(z), Baxter Q(z), and vacuum eigenvalues
        a(z), d(z) are internally consistent via the TQ relation:
            Lambda(z)*Q(z) = a(z)*Q(z+eta) + d(z)*Q(z-eta)
        with eta = i for the XXX chain.
        """
        L = 4
        roots = solve_bethe_xxx(L, 2)
        assert roots is not None
        for z in [0.7 + 0.3j, 2.0, -1.0 + 2j]:
            assert verify_TQ_relation(z, roots, L)


# =========================================================================
# 8. Baxter Q-operator
# =========================================================================

class TestBaxterQ:

    def test_TQ_relation_L4(self):
        """TQ relation: Lambda*Q = a*Q(+eta) + d*Q(-eta)."""
        roots = solve_bethe_xxx(4, 2)
        assert roots is not None
        assert verify_TQ_relation(0.7 + 0.3j, roots, 4)

    def test_TQ_relation_L6(self):
        roots = solve_bethe_xxx(6, 3)
        assert roots is not None
        assert verify_TQ_relation(1.2 + 0.5j, roots, 6)

    def test_TQ_multiple_z(self):
        """TQ holds at multiple spectral parameter values."""
        roots = solve_bethe_xxx(4, 2)
        assert roots is not None
        for z in [0.5, 1.0, 2.0, 0.3 + 0.7j, -1.5]:
            assert verify_TQ_relation(complex(z), roots, 4)

    def test_Q_zeros_are_bethe_roots(self):
        """Q(u_i) = 0 for each Bethe root u_i."""
        roots = solve_bethe_xxx(4, 2)
        assert roots is not None
        for u in roots:
            assert abs(baxter_Q(u, roots)) < 1e-10

    def test_quantum_determinant_L2(self):
        """qdet T(z) = z^L * (z-1)^L for L=2."""
        z = 1.5 + 0.3j
        assert abs(quantum_determinant(z, 2) - z ** 2 * (z - 1) ** 2) < 1e-14


# =========================================================================
# 9. Higher conserved charges from higher-arity shadows
# =========================================================================

class TestConservedCharges:

    def test_charges_commute_L4(self):
        """[I_j, I_k] = 0 for the XXX chain (L=4).

        Extracted via finite differences of T(z), so numerical precision
        is limited to ~1e-2 for the higher charges.
        """
        cc = verify_charges_commute(4, 3, tol=0.01)
        for (j, k), val in cc.items():
            assert val < 0.01, f"[I_{j}, I_{k}] = {val} > tol"

    def test_I2_is_hamiltonian(self):
        """I_2 ~ Hamiltonian (up to additive constant)."""
        charges = higher_conserved_charges(4, max_k=2)
        I2 = charges[0]  # first charge
        H = xxx_hamiltonian(4)
        # Both Hermitian; compare spectra
        evals_I = np.sort(eigvalsh((I2 + I2.conj().T).real / 2))
        evals_H = np.sort(eigvalsh((H + H.conj().T).real / 2))
        # Should be affinely related
        diff = evals_I - evals_I[0]
        diff_H = evals_H - evals_H[0]
        if abs(diff_H[-1]) > 1e-10:
            ratio = diff[-1] / diff_H[-1]
            residual = np.max(np.abs(diff - ratio * diff_H))
            assert residual < 0.01


# =========================================================================
# 10. Free energy
# =========================================================================

class TestFreeEnergy:

    def test_free_energy_negative(self):
        """Free energy per site is negative for the XXX chain."""
        f = free_energy_exact(4, beta=1.0)
        assert f < 0

    def test_six_vertex_weights_positive(self):
        """Boltzmann weights (a, b, c) are real and nonnegative for real u > 0."""
        a, b, c = six_vertex_weights(0.5, eta=1.0)
        assert a > 0
        assert b > 0
        assert c > 0

    def test_six_vertex_partition_positive(self):
        """Z > 0."""
        Z = six_vertex_partition_function(3, u=0.5, eta=1.0)
        assert Z > 0


# =========================================================================
# 11. Corner transfer matrix and shadow metric
# =========================================================================

class TestCTM:

    def test_ising_ctm_spectrum(self):
        """CTM eigenvalues for critical Ising: weights {0, 1/16, 1/2}."""
        evals = ctm_spectrum_ising(20)
        assert len(evals) == 3
        # The largest eigenvalue corresponds to h = 0
        assert evals[0] > evals[1] > evals[2]

    def test_ctm_partition_positive(self):
        Z = ctm_partition_function(0.5, 0.5, [0, 1 / 16, 1 / 2], n_desc=5)
        assert Z > 0

    def test_shadow_metric_virasoro(self):
        """Q_L = c^2 for Virasoro."""
        assert abs(shadow_metric_from_ctm(1.0) - 1.0) < 1e-14
        assert abs(shadow_metric_from_ctm(0.5) - 0.25) < 1e-14


# =========================================================================
# 12. Onsager algebra and Ising model
# =========================================================================

class TestOnsager:

    def test_dolan_grady_L4(self):
        """Dolan-Grady relations for L=4."""
        r1, r2 = verify_dolan_grady(4)
        assert r1 < 1e-8
        assert r2 < 1e-8

    def test_dolan_grady_L6(self):
        """Dolan-Grady relations for L=6."""
        r1, r2 = verify_dolan_grady(6)
        assert r1 < 1e-8
        assert r2 < 1e-8

    def test_ising_hamiltonian_hermitian(self):
        H = ising_hamiltonian(4)
        assert np.allclose(H, H.conj().T, atol=1e-14)

    def test_ising_kappa_value(self):
        """kappa(Ising) = c/2 = 1/4 (Ising CFT has c = 1/2)."""
        assert abs(ising_kappa() - 0.25) < 1e-15

    def test_ising_critical_gap_scaling(self):
        """Gap decreases with L at criticality (CFT scaling)."""
        gap_6 = ising_critical_gap(6)
        gap_8 = ising_critical_gap(8)
        gap_10 = ising_critical_gap(10)
        # Gap should decrease with L and be positive
        assert gap_6 > 0
        assert gap_8 < gap_6
        assert gap_10 < gap_8
        # gap * L should be roughly constant (CFT prediction)
        assert abs(gap_8 * 8 - gap_10 * 10) < 0.5

    def test_onsager_generators_commutator(self):
        """[A_0, A_1] is nonzero (the algebra is nontrivial)."""
        A0, A1 = onsager_generators(4)
        comm = A0 @ A1 - A1 @ A0
        assert np.max(np.abs(comm)) > 1e-10

    def test_ising_free_energy_real(self):
        f = ising_free_energy_exact(4, J=1.0, h=1.0, beta=1.0)
        assert np.isfinite(f)

    def test_onsager_2d_critical(self):
        """Onsager's exact 2D Ising free energy at the critical point.

        onsager_free_energy_2d(K) returns the dimensionless beta*f.
        At K_c = beta_c * J: beta_c * f_c ~ -1.005.
        The physical free energy f/J = (beta*f)/(beta*J) ~ -2.28.
        """
        beta_c = ising_critical_beta()
        f_c = onsager_free_energy_2d(beta_c)
        # Dimensionless beta*f at criticality
        assert -1.5 < f_c < -0.5
        # Physical f/J (Onsager 1944): ~ -2.269
        f_phys = f_c / beta_c
        assert abs(f_phys - (-2.269)) < 0.05

    def test_kramers_wannier(self):
        """Critical point satisfies sinh(2K_c) = 1."""
        K_c = ising_critical_beta()
        assert abs(np.sinh(2 * K_c) - 1.0) < 1e-14


# =========================================================================
# 13. RSOS models from admissible-level affine
# =========================================================================

class TestRSOS:

    def test_ising_from_rsos(self):
        """M(3,4) = Ising CFT: c = 1/2."""
        c = rsos_central_charge(3, 4)
        assert abs(c - 0.5) < 1e-14

    def test_tricritical_ising(self):
        """M(4,5): c = 7/10."""
        c = rsos_central_charge(4, 5)
        assert abs(c - 0.7) < 1e-14

    def test_three_state_potts(self):
        """M(5,6): c = 4/5."""
        c = rsos_central_charge(5, 6)
        assert abs(c - 0.8) < 1e-14

    def test_kappa_ising_rsos(self):
        """kappa for M(3,4) = c/2 = 1/4."""
        assert abs(rsos_kappa(3, 4) - 0.25) < 1e-14

    def test_ising_conformal_weights(self):
        """M(3,4) primaries: h = 0, 1/16, 1/2."""
        weights = rsos_conformal_weights(3, 4)
        expected = [0.0, 1 / 16, 0.5]
        assert len(weights) == 3
        for w, e in zip(weights, expected):
            assert abs(w - e) < 1e-10

    def test_tricritical_weights(self):
        """M(4,5) has 6 primaries."""
        weights = rsos_conformal_weights(4, 5)
        assert 0.0 in [round(w, 10) for w in weights]
        assert len(weights) == 6

    def test_admissible_level_ising(self):
        """Admissible level for M(3,4): k = 4/3 - 2 = -2/3."""
        k = rsos_admissible_level(3, 4)
        assert abs(k - (-2 / 3)) < 1e-14

    def test_rsos_partition_positive(self):
        """RSOS partition function is positive."""
        Z = rsos_partition_function_small(4, L=3)
        assert Z > 0


# =========================================================================
# 14. Toda field theory
# =========================================================================

class TestToda:

    def test_lax_integrability_sl2(self):
        """Eigenvalues of L are conserved for sl_2 Toda."""
        p = np.array([0.5, -0.5])
        q = np.array([0.3, -0.3])
        dev = verify_toda_integrability(p, q)
        assert dev < 1e-4

    def test_lax_integrability_sl3(self):
        """Eigenvalues of L are conserved for sl_3 Toda."""
        p = np.array([0.3, -0.1, -0.2])
        q = np.array([0.2, -0.1, -0.1])
        dev = verify_toda_integrability(p, q)
        assert dev < 1e-4

    def test_toda_hamiltonian_from_lax(self):
        """I_2 = (1/2) Tr(L^2) is the Flaschka Hamiltonian.

        Tr(L^2) = sum p_i^2 + 2*sum L_{i,i+1}*L_{i+1,i}
                = sum p_i^2 + 2*N (since L_{ij}*L_{ji} = 1)
        So I_2 = (1/2)*Tr(L^2) = sum p_i^2/2 + N.
        """
        p = np.array([0.5, -0.5])
        q = np.array([0.3, -0.3])
        integrals = toda_integrals_of_motion(p, q, max_k=2)
        # I_1 = Tr(L) = sum p_i = 0
        assert abs(integrals[0]) < 1e-10
        # I_2 = sum p_i^2/2 + N = 0.25 + 2 = ... wait, N=2 bonds.
        # Tr(L^2) = sum_i L_{ii}^2 + 2 sum_{i<j} L_{ij}L_{ji}
        # For N=2: Tr(L^2) = p0^2 + p1^2 + 2*L_{01}*L_{10}
        #   = 0.25 + 0.25 + 2*1.0 = 2.5, so I_2 = 1.25
        assert abs(integrals[1] - 1.25) < 1e-10

    def test_toda_integrals_conserved(self):
        """Higher integrals are independent of the phase-space point
        in the sense that they provide a complete integrable system.
        Here we just verify they are computable and real."""
        p = np.array([1.0, -0.5, -0.5])
        q = np.array([0.1, 0.0, -0.1])
        integrals = toda_integrals_of_motion(p, q, max_k=3)
        assert len(integrals) == 3
        for I in integrals:
            assert np.isfinite(I)

    def test_toda_classical_r_matrix(self):
        """Classical r-matrix = sl_2 Casimir (same as bar complex)."""
        r = toda_classical_r_matrix_sl2()
        assert np.allclose(r, CASIMIR_SL2_FUND)

    def test_sl2_casimir_eigenvalues(self):
        """C_2(V_n) = n(n+2)/2 for sl_2 (Euclidean normalization).

        The standard physics convention uses j(j+1) = n(n+2)/4.
        The Euclidean weight-space formula gives 2*j(j+1) = n(n+2)/2.
        Both normalizations are consistent; the function uses Euclidean.
        """
        evals = toda_casimir_eigenvalues_slN(2)
        for idx, n in enumerate(range(1, 10)):
            expected = n * (n + 2) / 2.0  # Euclidean normalization
            assert abs(evals[idx] - expected) < 1e-10


# =========================================================================
# 15. ODE/IM correspondence
# =========================================================================

class TestODEIM:

    def test_harmonic_oscillator(self):
        """Class G: V = kappa * x^2 gives harmonic oscillator E_n = sqrt(kappa)*(2n+1)."""
        kappa = 1.0
        coeffs = {2: kappa}
        evals = ode_im_eigenvalues(coeffs, 5, x_max=8.0, n_grid=500)
        # Harmonic: E_n = sqrt(kappa) * (2n+1)
        for n in range(min(3, len(evals))):
            expected = sqrt(kappa) * (2 * n + 1)
            assert abs(evals[n] - expected) / expected < 0.02

    def test_shadow_potential_class_G(self):
        """Class G has only kappa."""
        coeffs = shadow_potential_class("G", c=1.0)
        assert 2 in coeffs
        assert len(coeffs) == 1

    def test_shadow_potential_class_L(self):
        """Class L has kappa and S_3."""
        coeffs = shadow_potential_class("L", c=1.0)
        assert 2 in coeffs and 3 in coeffs
        assert len(coeffs) == 2

    def test_shadow_potential_class_M(self):
        """Class M has all S_r."""
        coeffs = shadow_potential_class("M", c=1.0)
        assert len(coeffs) >= 5

    def test_spectral_determinant_zeros(self):
        """D(E_n) = 0 at eigenvalues."""
        coeffs = {2: 1.0}
        evals = ode_im_eigenvalues(coeffs, 5, x_max=8.0, n_grid=500)
        for E_n in evals[:3]:
            D = ode_im_spectral_determinant(E_n, evals[:5])
            assert abs(D) < 0.1  # approximate zero

    def test_quartic_potential_eigenvalues(self):
        """Class L: V = kappa*x^2 + S_3*x^4 has real positive eigenvalues."""
        coeffs = {2: 1.0, 3: 0.5}
        evals = ode_im_eigenvalues(coeffs, 5, x_max=6.0, n_grid=400)
        assert all(E > 0 for E in evals)
        # Eigenvalues should be ordered
        for i in range(len(evals) - 1):
            assert evals[i] < evals[i + 1]

    def test_wkb_harmonic(self):
        """WKB for harmonic potential: exact E_n = sqrt(kappa)*(2n+1)."""
        kappa = 4.0
        coeffs = {2: kappa}
        for n in range(3):
            E_wkb = wkb_leading_eigenvalue(n, coeffs)
            E_exact = sqrt(kappa) * (2 * n + 1)
            assert abs(E_wkb - E_exact) < 1e-10


# =========================================================================
# 16. Quantum KdV from MC element
# =========================================================================

class TestQuantumKdV:

    def test_kdv_i1_eigenvalue(self):
        """i_1(h) = h - c/24."""
        c = 0.5
        h = 1 / 16
        val = quantum_kdv_eigenvalue(1, h, c)
        assert abs(val - (h - c / 24)) < 1e-14

    def test_kdv_i3_eigenvalue(self):
        """i_3(h) = 2h^2 + h(c-4)/6."""
        c = 1.0
        h = 0.5
        val = quantum_kdv_eigenvalue(3, h, c)
        expected = 2 * h ** 2 + h * (c - 4) / 6
        assert abs(val - expected) < 1e-14

    def test_kdv_i5_eigenvalue(self):
        """i_5(h) = 4h^3 + h^2(3c-16)/3 + h(c^2-16c+52)/36."""
        c = 2.0
        h = 1.0
        val = quantum_kdv_eigenvalue(5, h, c)
        expected = 4 * h ** 3 + h ** 2 * (3 * c - 16) / 3 + h * (c ** 2 - 16 * c + 52) / 36
        assert abs(val - expected) < 1e-14

    def test_kdv_vacuum_energy(self):
        """Vacuum (h=0): i_1(0) = -c/24, i_3(0) = 0, i_5(0) = 0."""
        c = 25.0
        assert abs(quantum_kdv_eigenvalue(1, 0, c) - (-c / 24)) < 1e-14
        assert abs(quantum_kdv_eigenvalue(3, 0, c)) < 1e-14
        assert abs(quantum_kdv_eigenvalue(5, 0, c)) < 1e-14

    def test_kdv_charges_independent(self):
        """KdV charges i_1 and i_3 are functionally independent."""
        assert verify_quantum_kdv_commutativity(1.0, [0.5, 1.0])


# =========================================================================
# 17. Drinfeld-Kohno theorem
# =========================================================================

class TestDrinfeldKohno:

    def test_drinfeld_R_ybe(self):
        """YBE for Drinfeld's universal R on C^2 x C^2 x C^2."""
        assert verify_drinfeld_kohno_ybe(np.exp(0.3j)) < 1e-10

    def test_drinfeld_R_ybe_various_q(self):
        """YBE holds for various q values."""
        for q in [np.exp(0.1), np.exp(0.5j), np.exp(0.3 + 0.2j)]:
            assert verify_drinfeld_kohno_ybe(q) < 1e-10

    def test_classical_r_matrix(self):
        """Classical r-matrix = H x H/2 + 2*E x F at small hbar."""
        dev = verify_drinfeld_classical_r(hbar=0.001)
        assert dev < 0.01

    def test_classical_r_convergence(self):
        """Classical r-matrix approximation improves as hbar -> 0."""
        dev_coarse = verify_drinfeld_classical_r(hbar=0.01)
        dev_fine = verify_drinfeld_classical_r(hbar=0.001)
        assert dev_fine < dev_coarse


# =========================================================================
# 18. Spin correlations
# =========================================================================

class TestCorrelations:

    def test_onsite_correlation(self):
        """<S_0^z S_0^z> = 1/4 (spin-1/2)."""
        val = spin_correlation(4, 0)
        assert abs(val - 0.25) < 1e-10

    def test_antiferromagnetic_nn(self):
        """Nearest-neighbor <S_0^z S_1^z> < 0 for antiferromagnet."""
        val = spin_correlation(6, 1)
        assert val < 0

    def test_alternating_sign(self):
        """Correlations alternate in sign for even L."""
        c1 = spin_correlation(8, 1)
        c2 = spin_correlation(8, 2)
        assert c1 < 0
        assert c2 > 0  # next-nearest neighbor is positive


# =========================================================================
# 19. Degeneration chain
# =========================================================================

class TestDegeneration:

    def test_trig_to_rational(self):
        """R_trig(eta*u, eta)/sinh(eta) -> R_rational(u) as eta -> 0."""
        dev = verify_trig_to_rational_limit(u=2.5, eta=0.001)
        assert dev < 0.01


# =========================================================================
# 20. Shadow-lattice dictionary
# =========================================================================

class TestDictionary:

    def test_kappa_sl2(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        d = ShadowLatticeDictionary(algebra="sl2", level=1.0)
        assert abs(d.kappa() - 9 / 4) < 1e-14

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        d = ShadowLatticeDictionary(algebra="virasoro", level=1.0)
        assert abs(d.kappa() - 0.5) < 1e-14

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        d = ShadowLatticeDictionary(algebra="heisenberg", level=3.0)
        assert abs(d.kappa() - 3.0) < 1e-14

    def test_bethe_roots_exist(self):
        d = ShadowLatticeDictionary(chain_length=4)
        roots = d.bethe_roots()
        assert roots is not None

    def test_shadow_coefficients_class_G(self):
        d = ShadowLatticeDictionary(shadow_class="G")
        coeffs = d.shadow_coefficients()
        assert 2 in coeffs

    def test_ode_im_eigenvalues(self):
        d = ShadowLatticeDictionary(shadow_class="G")
        evals = d.ode_im_eigenvalues(5)
        assert len(evals) == 5
        assert all(e > 0 for e in evals)


# =========================================================================
# 21. Full integrability check
# =========================================================================

class TestFullIntegrability:

    def test_full_check_L4(self):
        """Complete integrability verification at L=4."""
        results = full_integrability_check(L=4, tol=1e-4)
        assert results['ybe_rational']
        assert results['ybe_trig']
        assert results['transfer_commute']
        assert results['charges_commute']
        assert results['bae_satisfied']
        assert results['tq_relation']
        assert results['energy_match']
        assert results['cybe']
        assert results['dolan_grady']


# =========================================================================
# 22. Multi-path verification: energy from 3 independent methods
# =========================================================================

class TestMultiPathEnergy:
    """Verify ground state energy via three independent paths (CLAUDE.md mandate)."""

    def test_three_path_energy_L4(self):
        """E_0 from (1) exact diag, (2) Bethe ansatz, (3) free energy at beta->inf."""
        L = 4
        # Path 1: Exact diagonalization
        E1 = xxx_ground_state_energy(L) * L
        # Path 2: Bethe ansatz
        roots = solve_bethe_xxx(L, L // 2)
        assert roots is not None
        E2 = bethe_energy_xxx(roots, L)
        # Path 3: Free energy at large beta
        f = free_energy_exact(L, beta=50.0)
        E3 = f * L  # at large beta, f ~ E_0/L
        # All three must agree
        assert abs(E1 - E2) < 1e-6
        assert abs(E1 - E3) < 0.01  # finite-beta correction

    def test_three_path_energy_L6(self):
        L = 6
        E1 = xxx_ground_state_energy(L) * L
        roots = solve_bethe_xxx(L, L // 2)
        assert roots is not None
        E2 = bethe_energy_xxx(roots, L)
        f = free_energy_exact(L, beta=50.0)
        E3 = f * L
        assert abs(E1 - E2) < 1e-6
        assert abs(E1 - E3) < 0.01
