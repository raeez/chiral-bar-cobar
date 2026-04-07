"""Tests for Baxter Q-operator from MC element Theta_A.

Tests verify the complete chain:
  MC element Theta_A -> classical r-matrix -> quantum R-matrix -> transfer matrix T(u)
  -> Baxter Q-operator -> Bethe ansatz equations -> integrability

Three independent verification paths:
  Path A: Direct diagonalization of T(u) (numerical linear algebra)
  Path B: Bethe ansatz roots -> analytic eigenvalue formula -> TQ relation
  Path C: MC projection -> R(u) -> YBE -> [T(u), T(v)] = 0

The Baxter Q-operator is a HIGHER PROJECTION of Theta_A:
  - (g=0, r=2): R(u) = uI + P (Yang R-matrix, from collision residue of Theta_A)
  - (g=0, r=L): T(u) = tr_0 R_{01}...R_{0L} (transfer matrix, from arity-L MC projection)
  - Q(u): the polynomial whose zeros are Bethe roots, satisfying TQ = aQ(u-1) + dQ(u+1)

Convention: FRT (Faddeev-Reshetikhin-Takhtajan), R(u) = uI + P.
  a(u) = (u+1)^L, d(u) = u^L for homogeneous chain.
  BAE: a(u_k)/d(u_k) = prod_{l!=k} (u_k-u_l+1)/(u_k-u_l-1).
"""

import numpy as np
import pytest

from compute.lib.baxter_q_from_mc import (
    # R-matrix
    yang_r_matrix_sl2,
    yang_r_matrix_sl3,
    yang_r_matrix_slN,
    verify_yang_baxter_general,
    # Transfer matrix
    transfer_matrix_sl2,
    transfer_matrix_sl3,
    transfer_matrix_general,
    # TQ apparatus
    a_function,
    d_function,
    q_polynomial,
    transfer_eigenvalue_bethe,
    verify_tq_relation,
    verify_bethe_eigenvalue_vs_diag,
    bethe_ansatz_equations,
    solve_bethe_sl2,
    # Explicit constructions
    find_all_bethe_states,
    baxter_q_sl2_L2,
    baxter_q_sl2_L3,
    baxter_q_sl2_L4,
    # Diagonalization
    diagonalize_transfer_sl2,
    verify_integrability,
    verify_bethe_vs_diag,
    # MC verification
    verify_r_from_mc_sl2,
    verify_r_from_mc_sl3,
    # sl_3
    transfer_eigenvalue_sl3_vacuum,
    verify_sl3_vacuum,
    # Hamiltonian
    heisenberg_hamiltonian_from_transfer,
    heisenberg_hamiltonian_direct,
)


# ============================================================================
# I. R-MATRIX FROM MC PROJECTION (Path C)
# ============================================================================

class TestRMatrixFromMC:
    """Verify the R-matrix arises from the genus-0 arity-2 MC projection."""

    def test_yang_r_sl2_shape(self):
        """R(u) for sl_2 is a 4x4 matrix."""
        R = yang_r_matrix_sl2(1.0)
        assert R.shape == (4, 4)

    def test_yang_r_sl2_at_zero(self):
        """R(0) = P (permutation operator)."""
        R = yang_r_matrix_sl2(0.0)
        P = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                       [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
        assert np.allclose(R, P)

    def test_yang_r_sl2_classical_limit(self):
        """R(u)/u -> I + P/u as u -> infinity (classical limit)."""
        for u in [5.0, 10.0, 100.0]:
            R_norm = yang_r_matrix_sl2(u) / u
            P = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                           [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
            expected = np.eye(4) + P / u
            assert np.allclose(R_norm, expected, atol=1e-12)

    def test_yang_baxter_sl2(self):
        """YBE: R12(u-v) R13(u) R23(v) = R23(v) R13(u) R12(u-v) for sl_2."""
        for u, v in [(1.0, 2.0), (0.5, 3.0), (-1.0, 2.5), (0.3, -0.7)]:
            err = verify_yang_baxter_general(yang_r_matrix_sl2, u, v, dim=2)
            assert err < 1e-10, f"YBE failed at u={u}, v={v}: err={err}"

    def test_yang_r_sl3_shape(self):
        """R(u) for sl_3 is a 9x9 matrix."""
        R = yang_r_matrix_sl3(1.0)
        assert R.shape == (9, 9)

    def test_yang_baxter_sl3(self):
        """YBE for sl_3."""
        for u, v in [(1.0, 2.0), (0.5, 3.0)]:
            err = verify_yang_baxter_general(yang_r_matrix_sl3, u, v, dim=3)
            assert err < 1e-10, f"YBE sl_3 failed at u={u}, v={v}: err={err}"

    def test_yang_r_slN_general(self):
        """R(u) = uI + P satisfies YBE for sl_N, N=2,3,4."""
        for N in [2, 3, 4]:
            R_func = lambda u, n=N: yang_r_matrix_slN(u, n)
            err = verify_yang_baxter_general(R_func, 1.0, 2.0, dim=N)
            assert err < 1e-9, f"YBE sl_{N} failed: err={err}"

    def test_r_matrix_eigenvalues(self):
        """R(u) has eigenvalues u+1 (symmetric) and u-1 (antisymmetric)."""
        u = 2.5
        R = yang_r_matrix_sl2(u)
        evals = sorted(np.linalg.eigvalsh(R.real))
        # sl_2: Sym^2 has dim 3 (eigenvalue u+1), Lambda^2 has dim 1 (eigenvalue u-1)
        expected = sorted([u - 1] + [u + 1] * 3)
        assert np.allclose(evals, expected, atol=1e-10)


# ============================================================================
# II. TRANSFER MATRIX (Path A + C)
# ============================================================================

class TestTransferMatrix:
    """Verify transfer matrix construction and integrability."""

    def test_transfer_sl2_L2_shape(self):
        """T(u) for L=2 is 4x4."""
        T = transfer_matrix_sl2(1.0, [0.0, 0.0])
        assert T.shape == (4, 4)

    def test_transfer_sl2_vacuum_eigenvalue(self):
        """Vacuum eigenvalue: Lambda_vac(u) = (u+1)^L + u^L."""
        for L in [2, 3, 4]:
            a_list = [0.0] * L
            for u in [0.5, 1.0, 2.0]:
                T = transfer_matrix_sl2(u, a_list)
                vac_ev = T[0, 0].real  # |000...0> is the vacuum
                expected = (u + 1) ** L + u ** L
                assert abs(vac_ev - expected) < 1e-10, \
                    f"Vacuum eigenvalue wrong: L={L}, u={u}"

    def test_integrability_sl2(self):
        """[T(u), T(v)] = 0 for sl_2 XXX (consequence of YBE)."""
        for L in [2, 3, 4]:
            assert verify_integrability(L, 2), f"Integrability failed L={L}"

    def test_integrability_sl3(self):
        """[T(u), T(v)] = 0 for sl_3 XXX."""
        assert verify_integrability(2, 3)

    def test_transfer_sl2_at_zero_is_shift(self):
        """T(0) is the cyclic shift operator for homogeneous chain."""
        L = 3
        T0 = transfer_matrix_sl2(0.0, [0.0] * L)
        # The cyclic shift has eigenvalues 1, omega, omega^2 (cube roots of 1)
        evals = np.linalg.eigvals(T0)
        # Check T0^L = I (the shift has order L)
        T0_L = np.linalg.matrix_power(T0.real.astype(int), L)
        assert np.allclose(T0_L, np.eye(2 ** L), atol=1e-10)

    def test_transfer_sz_conservation(self):
        """[T(u), S^z] = 0 (weight conservation)."""
        L = 3
        dim = 2 ** L
        sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
        I2 = np.eye(2, dtype=complex)
        Sz = np.zeros((dim, dim), dtype=complex)
        for j in range(L):
            op = np.eye(1, dtype=complex)
            for k in range(L):
                op = np.kron(op, sigma_z if k == j else I2)
            Sz += 0.5 * op

        for u in [0.5, 1.0, 2.0]:
            T = transfer_matrix_sl2(u, [0.0] * L)
            comm = T @ Sz - Sz @ T
            assert np.linalg.norm(comm) < 1e-10


# ============================================================================
# III. BAXTER TQ RELATION (Path B)
# ============================================================================

class TestBaxterTQ:
    """Verify the TQ relation and Bethe ansatz."""

    def test_a_d_functions(self):
        """a(u) and d(u) for homogeneous chain."""
        a_list = [0.0, 0.0]
        assert abs(a_function(1.0, a_list) - 4.0) < 1e-15  # (1+1)^2
        assert abs(d_function(1.0, a_list) - 1.0) < 1e-15  # 1^2

    def test_tq_algebraic_identity(self):
        """TQ relation is an algebraic identity for any Bethe roots."""
        # The identity Lambda(u)*Q(u) = a(u)*Q(u-1) + d(u)*Q(u+1) holds
        # algebraically when Lambda is defined by the Bethe formula.
        a_list = [0.0, 0.0]
        root = np.array([-0.5], dtype=complex)
        for u in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
            res = verify_tq_relation(u, a_list, root)
            assert res < 1e-12, f"TQ relation failed at u={u}: res={res}"

    def test_bae_L2_M1(self):
        """BAE for L=2, M=1: root u_1 = -1/2."""
        root = np.array([-0.5], dtype=complex)
        a_list = [0.0, 0.0]
        res = bethe_ansatz_equations(root, a_list)
        assert np.max(np.abs(res)) < 1e-12

    def test_bae_L3_M1(self):
        """BAE for L=3, M=1: roots are cube-root-of-unity solutions."""
        import cmath
        a_list = [0.0] * 3
        omega = cmath.exp(2j * cmath.pi / 3)
        for k in [1, 2]:
            root_val = -1 / (1 - omega ** k)
            root = np.array([root_val], dtype=complex)
            res = bethe_ansatz_equations(root, a_list)
            assert np.max(np.abs(res)) < 1e-10, \
                f"BAE failed for L=3 root {root_val}: res={res}"

    def test_bethe_eigenvalue_matches_diag_L2(self):
        """Bethe eigenvalue (real part) matches diag for L=2."""
        a_list = [0.0, 0.0]
        root = np.array([-0.5], dtype=complex)
        for u in [0.5, 1.0, 2.0]:
            err = verify_bethe_eigenvalue_vs_diag(u, a_list, root)
            assert err < 1e-10, f"Bethe vs diag failed at u={u}"

    def test_bethe_eigenvalue_matches_diag_L3(self):
        """Bethe eigenvalue (real part) matches diag for L=3."""
        import cmath
        a_list = [0.0] * 3
        omega = cmath.exp(2j * cmath.pi / 3)
        root = np.array([-1 / (1 - omega)], dtype=complex)
        for u in [0.5, 1.0, 2.0]:
            err = verify_bethe_eigenvalue_vs_diag(u, a_list, root)
            assert err < 1e-10, f"Bethe vs diag L=3 failed at u={u}"


# ============================================================================
# IV. EXPLICIT CONSTRUCTIONS
# ============================================================================

class TestExplicitConstructions:
    """Test explicit Baxter Q for L=2, 3, 4."""

    def test_L2_states(self):
        """L=2 has vacuum (M=0) and singlet (M=1)."""
        states = baxter_q_sl2_L2()
        assert len(states) == 2
        assert states[0].M == 0
        assert states[1].M == 1

    def test_L2_all_pass(self):
        """All L=2 states have small TQ and BAE residuals."""
        for st in baxter_q_sl2_L2():
            assert st.tq_residual < 1e-10
            if len(st.bae_residuals) > 0:
                assert np.max(np.abs(st.bae_residuals)) < 1e-10

    def test_L3_states(self):
        """L=3 produces vacuum + M=1 states."""
        states = baxter_q_sl2_L3()
        assert len(states) >= 2

    def test_L3_all_pass(self):
        """All L=3 states have small TQ and BAE residuals."""
        for st in baxter_q_sl2_L3():
            assert st.tq_residual < 1e-10
            if len(st.bae_residuals) > 0:
                assert np.max(np.abs(st.bae_residuals)) < 1e-10

    def test_L4_states(self):
        """L=4 produces states with M=0, 1, 2."""
        states = baxter_q_sl2_L4()
        ms = {st.M for st in states}
        assert 0 in ms
        assert 1 in ms
        assert 2 in ms

    def test_L4_all_pass(self):
        """All L=4 states have small TQ and BAE residuals."""
        for st in baxter_q_sl2_L4():
            assert st.tq_residual < 1e-9, \
                f"L=4 M={st.M} TQ residual too large: {st.tq_residual}"
            if len(st.bae_residuals) > 0:
                assert np.max(np.abs(st.bae_residuals)) < 1e-9


# ============================================================================
# V. BETHE VS DIAG CROSS-CHECK (Path A vs Path B)
# ============================================================================

class TestBetheVsDiag:
    """Cross-check Bethe eigenvalues against direct diagonalization."""

    def test_L2_M0(self):
        comp = verify_bethe_vs_diag(2, 0)
        assert comp["all_match"]

    def test_L2_M1(self):
        comp = verify_bethe_vs_diag(2, 1)
        assert comp["all_match"]

    def test_L3_M0(self):
        comp = verify_bethe_vs_diag(3, 0)
        assert comp["all_match"]

    def test_L3_M1(self):
        comp = verify_bethe_vs_diag(3, 1)
        assert comp["all_match"]

    def test_L4_M0(self):
        comp = verify_bethe_vs_diag(4, 0)
        assert comp["all_match"]

    def test_L4_M1(self):
        comp = verify_bethe_vs_diag(4, 1)
        assert comp["all_match"]

    def test_L4_M2(self):
        comp = verify_bethe_vs_diag(4, 2)
        assert comp["all_match"]


# ============================================================================
# VI. sl_3 CHECKS
# ============================================================================

class TestSl3:
    """Verify sl_3 transfer matrix and vacuum eigenvalue."""

    def test_sl3_vacuum_L2(self):
        """sl_3 vacuum eigenvalue for L=2."""
        err = verify_sl3_vacuum(2, 1.0)
        assert err < 1e-10

    def test_sl3_vacuum_L3(self):
        """sl_3 vacuum eigenvalue for L=3."""
        err = verify_sl3_vacuum(3, 1.0)
        assert err < 1e-10

    def test_sl3_vacuum_formula(self):
        """Lambda_vac(u) = (u+1)^L + 2*u^L for sl_3."""
        for L in [2, 3]:
            for u in [0.5, 1.0, 2.0]:
                expected = (u + 1) ** L + 2 * u ** L
                actual = transfer_eigenvalue_sl3_vacuum(u, L)
                assert abs(expected - actual) < 1e-12

    def test_sl3_integrability(self):
        """[T(u), T(v)] = 0 for sl_3 XXX, L=2."""
        assert verify_integrability(2, 3)


# ============================================================================
# VII. HAMILTONIAN FROM TRANSFER MATRIX
# ============================================================================

class TestHamiltonian:
    """Verify Hamiltonian extraction from transfer matrix."""

    def test_heisenberg_eigenvalues_L2(self):
        """Heisenberg Hamiltonian from T(u) matches direct construction for L=2."""
        H_t = heisenberg_hamiltonian_from_transfer(2)
        H_d = heisenberg_hamiltonian_direct(2)
        ev_t = sorted(np.linalg.eigvals(H_t).real)
        ev_d = sorted(np.linalg.eigvals(H_d).real)
        # Normalize
        ev_t = np.array(ev_t) - np.mean(ev_t)
        ev_d = np.array(ev_d) - np.mean(ev_d)
        if np.std(ev_t) > 1e-10:
            ev_t /= np.std(ev_t)
            ev_d /= np.std(ev_d)
        assert np.allclose(ev_t, ev_d, atol=1e-8)

    def test_heisenberg_eigenvalues_L3(self):
        """Heisenberg Hamiltonian from T(u) matches direct for L=3."""
        H_t = heisenberg_hamiltonian_from_transfer(3)
        H_d = heisenberg_hamiltonian_direct(3)
        ev_t = sorted(np.linalg.eigvals(H_t).real)
        ev_d = sorted(np.linalg.eigvals(H_d).real)
        ev_t = np.array(ev_t) - np.mean(ev_t)
        ev_d = np.array(ev_d) - np.mean(ev_d)
        if np.std(ev_t) > 1e-10:
            ev_t /= np.std(ev_t)
            ev_d /= np.std(ev_d)
        assert np.allclose(ev_t, ev_d, atol=1e-8)

    def test_heisenberg_eigenvalues_L4(self):
        """Heisenberg Hamiltonian from T(u) matches direct for L=4."""
        H_t = heisenberg_hamiltonian_from_transfer(4)
        H_d = heisenberg_hamiltonian_direct(4)
        ev_t = sorted(np.linalg.eigvals(H_t).real)
        ev_d = sorted(np.linalg.eigvals(H_d).real)
        ev_t = np.array(ev_t) - np.mean(ev_t)
        ev_d = np.array(ev_d) - np.mean(ev_d)
        if np.std(ev_t) > 1e-10:
            ev_t /= np.std(ev_t)
            ev_d /= np.std(ev_d)
        assert np.allclose(ev_t, ev_d, atol=1e-8)


# ============================================================================
# VIII. MC PROJECTION COMPREHENSIVE (Path C)
# ============================================================================

class TestMCProjection:
    """Comprehensive MC projection verification."""

    def test_mc_classical_limits(self):
        """All classical limits pass."""
        r_mc = verify_r_from_mc_sl2()
        for k, v in r_mc.items():
            if "classical" in k:
                assert v < 1e-10, f"{k}: {v}"

    def test_mc_ybe(self):
        """All YBE checks pass."""
        r_mc = verify_r_from_mc_sl2()
        for k, v in r_mc.items():
            if "YBE" in k:
                assert v < 1e-10, f"{k}: {v}"

    def test_mc_integrability(self):
        """All integrability checks pass."""
        r_mc = verify_r_from_mc_sl2()
        for k, v in r_mc.items():
            if "integrability" in k:
                assert v, f"{k}: {v}"

    def test_mc_sl3(self):
        """sl_3 MC projection checks pass."""
        r_sl3 = verify_r_from_mc_sl3()
        for k, v in r_sl3.items():
            if "YBE" in k:
                assert v < 1e-10, f"{k}: {v}"


# ============================================================================
# IX. MASTER VERIFICATION
# ============================================================================

class TestMasterVerification:
    """Run the full verification suite."""

    def test_all_pass(self):
        """All 32 checks in the master suite pass."""
        from compute.lib.baxter_q_from_mc import verify_all_mc_to_baxter
        results = verify_all_mc_to_baxter()
        for name, val in results.items():
            if isinstance(val, bool):
                assert val, f"FAIL: {name} = {val}"
            elif isinstance(val, float):
                assert val < 1e-6, f"FAIL: {name} = {val}"
