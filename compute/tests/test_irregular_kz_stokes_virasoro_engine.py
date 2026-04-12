r"""Tests for the irregular KZ Stokes engine for Virasoro at arity 2.

Verifies:
1. VirasoroKZData: Poincare rank, Stokes rays, anti-Stokes rays, kappa
2. Scalar solution: exact ODE satisfaction, known values
3. HTL normal form: structure, irregular coefficient, exactness
4. 2x2 Jordan fundamental matrix: ODE satisfaction
5. Stokes matrices: triviality at arity 2 (scalar irregular part)
6. Formal monodromy: analytic formula, unipotent structure
7. Cyclic relation: S_3 * S_2 * S_1 * S_0 * M_formal = M_actual
8. Numerical monodromy: agreement with analytic monodromy
9. Diagonal system: triviality with distinct weights
10. Cross-consistency with resurgence_stokes_engine (shadow invariants)

Every hardcoded expected value has a VERIFIED comment citing 2+
independent sources (AP10/HZ-6/AAP11).

References:
    compute/lib/irregular_kz_stokes_virasoro_engine.py
    compute/lib/resurgence_stokes_engine.py (shadow Stokes, cross-check)
    CLAUDE.md C2, C11 (kappa, r-matrix formulae)
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math

import numpy as np
import pytest


# =====================================================================
# Section 1: VirasoroKZData
# =====================================================================

class TestVirasoroKZData:
    """Test the KZ ODE parameter object."""

    def test_kappa_is_c_over_2(self):
        """kappa(Vir_c) = c/2.
        # VERIFIED: [DC] direct from C2, [LT] Frenkel-Ben-Zvi Thm 5.6.1
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        for c_val in [1.0, 13.0, 25.0, 26.0]:
            kz = VirasoroKZData(c_val)
            assert abs(kz.kappa - c_val / 2.0) < 1e-15

    def test_kappa_c0_vanishes(self):
        """kappa(Vir_0) = 0.
        # VERIFIED: [DC] c/2 at c=0, [LC] trivial Virasoro limit
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(0.0)
        assert kz.kappa == 0.0

    def test_kappa_c13_self_dual(self):
        """kappa(Vir_13) = 13/2 (self-dual point).
        # VERIFIED: [DC] 13/2, [SY] Koszul self-duality c -> 26-c
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        assert abs(kz.kappa - 6.5) < 1e-15

    def test_poincare_rank_is_2(self):
        """Poincare rank = pole_order(A(z)) - 1 = 3 - 1 = 2.
        # VERIFIED: [DC] A(z) has z^{-3} leading, [LT] Wasow Ch.12
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        assert kz.poincare_rank == 2

    def test_n_stokes_rays_is_4(self):
        """2 * Poincare_rank = 4 Stokes rays.
        # VERIFIED: [DC] 2*2=4, [LT] Loday-Richaud Thm 3.1 (2*r rays)
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        assert kz.n_stokes_rays == 4

    def test_stokes_rays_angles(self):
        """Stokes rays at pi/4, 3pi/4, 5pi/4, 7pi/4.
        # VERIFIED: [DC] cos(2*theta)=0 gives theta=pi/4+k*pi/2,
        #           [LT] Balser-Jurkat-Lutz, angular spacing = pi/r = pi/2
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        rays = kz.stokes_rays()
        expected = [math.pi / 4.0 + k * math.pi / 2.0 for k in range(4)]
        assert len(rays) == 4
        for r, e in zip(rays, expected):
            assert abs(r - e) < 1e-15

    def test_anti_stokes_rays_angles(self):
        """Anti-Stokes rays at 0, pi/2, pi, 3pi/2.
        # VERIFIED: [DC] cos(2*theta)=+/-1, [SY] rotated pi/4 from Stokes
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        anti_rays = kz.anti_stokes_rays()
        expected = [k * math.pi / 2.0 for k in range(4)]
        assert len(anti_rays) == 4
        for r, e in zip(anti_rays, expected):
            assert abs(r - e) < 1e-15

    def test_stokes_anti_stokes_interleave(self):
        """Stokes and anti-Stokes rays interleave at pi/4 separation.
        # VERIFIED: [DC] direct comparison, [SY] general irregular ODE theory
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        stokes = kz.stokes_rays()
        anti = kz.anti_stokes_rays()
        # Each Stokes ray is pi/4 ahead of the preceding anti-Stokes ray
        for k in range(4):
            assert abs(stokes[k] - anti[k] - math.pi / 4.0) < 1e-15

    def test_irregular_coefficient(self):
        """Irregular coefficient q = -c/4.
        # VERIFIED: [DC] from exp(-c/(4z^2)), [LT] integral of (c/2)/z^3
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        for c_val in [1.0, 13.0, 26.0]:
            kz = VirasoroKZData(c_val)
            assert abs(kz.irregular_coefficient - (-c_val / 4.0)) < 1e-15

    def test_r_matrix_at_scalar(self):
        """A(z) = (c/2)/z^3 + 2h/z on an eigenspace.
        # VERIFIED: [DC] direct substitution, [LT] CLAUDE.md C11
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(c=10.0)
        z = 2.0 + 1.0j
        h = 3.0
        expected = (10.0 / 2.0) / z**3 + 2.0 * 3.0 / z
        assert abs(kz.r_matrix_at(z, h) - expected) < 1e-14


# =====================================================================
# Section 2: Scalar KZ solution
# =====================================================================

class TestScalarKZSolution:
    """Test the exact scalar solution phi(z) = z^{2h} exp(-c/(4z^2))."""

    def test_known_value_h0(self):
        """At h=0: phi(z) = exp(-c/(4z^2)).
        # VERIFIED: [DC] z^0=1, [LC] h->0 limit
        """
        from lib.irregular_kz_stokes_virasoro_engine import scalar_kz_solution
        c, h = 10.0, 0.0
        z = 1.0 + 0.0j
        expected = cmath.exp(-10.0 / 4.0)
        assert abs(scalar_kz_solution(c, h, z) - expected) < 1e-14

    def test_known_value_z1(self):
        """At z=1: phi(1) = exp(-c/4).
        # VERIFIED: [DC] 1^{2h}=1, [LC] z->1 limit
        """
        from lib.irregular_kz_stokes_virasoro_engine import scalar_kz_solution
        c, h = 6.0, 2.0
        z = 1.0 + 0.0j
        expected = cmath.exp(-6.0 / 4.0)  # z^{2h}=1 at z=1
        assert abs(scalar_kz_solution(c, h, z) - expected) < 1e-14

    def test_ode_satisfaction(self):
        """Scalar solution satisfies dphi/dz = A(z)*phi to high accuracy.
        # VERIFIED: [DC] numerical differentiation, [SY] exact solution has zero residual
        """
        from lib.irregular_kz_stokes_virasoro_engine import scalar_kz_verify_ode
        for c_val in [1.0, 13.0, 25.0]:
            for h_val in [0.5, 1.0, 2.0]:
                z = 1.0 + 0.3j
                result = scalar_kz_verify_ode(c_val, h_val, z)
                assert result['relative_error'] < 1e-6, (
                    f"ODE not satisfied at c={c_val}, h={h_val}: "
                    f"rel_err={result['relative_error']}"
                )

    def test_ode_satisfaction_various_z(self):
        """ODE satisfaction at various points z (away from origin).
        # VERIFIED: [DC] numerical, [SY] exactness of closed-form solution
        """
        from lib.irregular_kz_stokes_virasoro_engine import scalar_kz_verify_ode
        c, h = 13.0, 1.0
        for z in [0.5 + 0.5j, 2.0 + 0.0j, 0.3 + 1.0j, -1.0 + 0.5j]:
            result = scalar_kz_verify_ode(c, h, z)
            assert result['relative_error'] < 1e-5

    def test_c0_reduces_to_power(self):
        """At c=0: phi(z) = z^{2h} (no irregular part).
        # VERIFIED: [DC] exp(0)=1, [LC] c->0 limit of KZ
        """
        from lib.irregular_kz_stokes_virasoro_engine import scalar_kz_solution
        h = 3.0
        z = 2.0 + 1.0j
        result = scalar_kz_solution(0.0, h, z)
        expected = z**(2.0 * h)
        assert abs(result - expected) < 1e-13


# =====================================================================
# Section 3: HTL normal form
# =====================================================================

class TestHTLNormalForm:
    """Test the Hukuhara-Turrittin-Levelt normal form computation."""

    def test_scalar_htl(self):
        """Scalar (1x1) system: Q = -c/4, L = 2h, F = 1.
        # VERIFIED: [DC] direct, [LT] standard HTL for rank-1
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_htl_normal_form
        rho_T = np.array([[3.0]], dtype=complex)
        htl = compute_htl_normal_form(c=10.0, rho_T=rho_T)
        assert htl.dim == 1
        assert abs(htl.q_irregular - (-2.5)) < 1e-15
        assert abs(htl.L_regular[0, 0] - 6.0) < 1e-15
        assert htl.is_exact

    def test_jordan_htl(self):
        """2x2 Jordan block: Q = -c/4, L = 2*[[h,1],[0,h]].
        # VERIFIED: [DC] direct construction, [LT] HTL with scalar Q
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            compute_htl_normal_form, jordan_block_rho_T,
        )
        c, h = 13.0, 2.0
        rho_T = jordan_block_rho_T(h)
        htl = compute_htl_normal_form(c, rho_T)
        assert htl.dim == 2
        assert abs(htl.q_irregular - (-13.0 / 4.0)) < 1e-15
        # L = 2 * rho_T
        assert abs(htl.L_regular[0, 0] - 4.0) < 1e-15
        assert abs(htl.L_regular[0, 1] - 2.0) < 1e-15
        assert abs(htl.L_regular[1, 0]) < 1e-15
        assert abs(htl.L_regular[1, 1] - 4.0) < 1e-15
        assert htl.is_exact

    def test_diagonal_htl(self):
        """Diagonal 2x2: two distinct eigenvalues.
        # VERIFIED: [DC] diagonal rho_T, [SY] diagonal = two scalars
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_htl_normal_form
        rho_T = np.diag([1.0, 3.0]).astype(complex)
        htl = compute_htl_normal_form(c=10.0, rho_T=rho_T)
        assert htl.dim == 2
        assert abs(htl.L_regular[0, 0] - 2.0) < 1e-15
        assert abs(htl.L_regular[1, 1] - 6.0) < 1e-15
        assert htl.is_exact


# =====================================================================
# Section 4: 2x2 Jordan fundamental matrix
# =====================================================================

class TestJordanFundamentalMatrix:
    """Test the fundamental matrix for the 2x2 Jordan system."""

    def test_ode_satisfaction(self):
        """Fundamental matrix satisfies dPhi/dz = A(z) Phi.
        # VERIFIED: [DC] numerical differentiation, [SY] closed-form solution
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            formal_fundamental_matrix_jordan_verify,
        )
        c, h = 13.0, 1.0
        z = 1.0 + 0.5j
        result = formal_fundamental_matrix_jordan_verify(c, h, z)
        assert result['max_relative_error'] < 1e-5, (
            f"Jordan ODE error: {result['max_relative_error']}"
        )

    def test_ode_satisfaction_various_params(self):
        """ODE verification at various (c, h, z).
        # VERIFIED: [DC] numerical, [SY] exactness
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            formal_fundamental_matrix_jordan_verify,
        )
        params = [
            (1.0, 0.5, 1.0 + 0.3j),
            (13.0, 2.0, 0.5 + 0.5j),
            (25.0, 1.0, 2.0 + 0.0j),
            (26.0, 0.0, 0.8 - 0.4j),
        ]
        for c, h, z in params:
            result = formal_fundamental_matrix_jordan_verify(c, h, z)
            assert result['max_relative_error'] < 1e-4, (
                f"c={c}, h={h}, z={z}: err={result['max_relative_error']}"
            )

    def test_lower_right_is_scalar(self):
        """Phi[1,1] = z^{2h} exp(-c/(4z^2)) (scalar solution).
        # VERIFIED: [DC] lower row is decoupled scalar ODE,
        #           [LT] triangular system structure
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            formal_fundamental_matrix_jordan, scalar_kz_solution,
        )
        c, h = 13.0, 2.0
        z = 1.0 + 0.5j
        Phi = formal_fundamental_matrix_jordan(c, h, z)
        phi_scalar = scalar_kz_solution(c, h, z)
        assert abs(Phi[1, 1] - phi_scalar) < 1e-14

    def test_lower_left_is_zero(self):
        """Phi[1,0] = 0 (lower-triangular decoupling).
        # VERIFIED: [DC] A(z) is upper triangular, [SY] block structure
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            formal_fundamental_matrix_jordan,
        )
        c, h = 13.0, 2.0
        z = 1.0 + 0.5j
        Phi = formal_fundamental_matrix_jordan(c, h, z)
        assert abs(Phi[1, 0]) < 1e-15

    def test_upper_right_has_log(self):
        """Phi[0,1] = 2*log(z) * z^{2h} exp(-c/(4z^2)).
        # VERIFIED: [DC] variation of parameters integral,
        #           [SY] integrand 2/z gives 2*log(z)
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            formal_fundamental_matrix_jordan, scalar_kz_solution,
        )
        c, h = 13.0, 2.0
        z = 1.0 + 0.5j
        Phi = formal_fundamental_matrix_jordan(c, h, z)
        phi_scalar = scalar_kz_solution(c, h, z)
        expected = phi_scalar * 2.0 * cmath.log(z)
        assert abs(Phi[0, 1] - expected) < 1e-13

    def test_determinant_is_scalar_squared(self):
        """det(Phi) = (z^{2h} exp(-c/(4z^2)))^2 (from triangular structure).
        # VERIFIED: [DC] det of upper triangular = product of diagonal,
        #           [SY] Liouville formula: det' = tr(A)*det
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            formal_fundamental_matrix_jordan, scalar_kz_solution,
        )
        c, h = 13.0, 2.0
        z = 1.0 + 0.5j
        Phi = formal_fundamental_matrix_jordan(c, h, z)
        det_Phi = np.linalg.det(Phi)
        phi_scalar = scalar_kz_solution(c, h, z)
        expected_det = phi_scalar**2
        assert abs(det_Phi - expected_det) / max(abs(expected_det), 1e-300) < 1e-12


# =====================================================================
# Section 5: Stokes matrices
# =====================================================================

class TestStokesMatrices:
    """Test Stokes matrix computation for the 2x2 Jordan system."""

    def test_stokes_trivial_at_arity_2(self):
        """All Stokes matrices are identity (scalar irregular part).
        # VERIFIED: [DC] M_actual = M_formal => product of S_k = Id,
        #           [LT] Wasow: scalar Q => no Stokes (Thm 19.1)
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            compute_stokes_matrices_jordan,
        )
        c, h = 13.0, 1.0
        result = compute_stokes_matrices_jordan(c, h)
        for k, S_k in enumerate(result.stokes_matrices):
            assert np.allclose(S_k, np.eye(2)), (
                f"S_{k} is not identity: {S_k}"
            )

    def test_stokes_multipliers_zero(self):
        """All Stokes multipliers s_k = 0.
        # VERIFIED: [DC] from cyclic relation, [SY] scalar Q => trivial Stokes
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            compute_stokes_matrices_jordan,
        )
        c, h = 13.0, 1.0
        result = compute_stokes_matrices_jordan(c, h)
        for s_k in result.stokes_multipliers:
            assert abs(s_k) < 1e-15

    def test_cyclic_relation(self):
        """S_3 * S_2 * S_1 * S_0 * M_formal = M_actual.
        # VERIFIED: [DC] explicit product, [LT] Malgrange cyclic relation
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            compute_stokes_matrices_jordan,
        )
        for c_val in [1.0, 13.0, 25.0]:
            for h_val in [0.5, 1.0, 2.0]:
                result = compute_stokes_matrices_jordan(c_val, h_val)
                assert result.cyclic_relation_error < 1e-14, (
                    f"Cyclic error at c={c_val}, h={h_val}: "
                    f"{result.cyclic_relation_error}"
                )

    def test_formal_monodromy_unipotent_structure(self):
        """M_formal = e^{4*pi*i*h} * [[1, 4*pi*i], [0, 1]].
        # VERIFIED: [DC] exp(2*pi*i*L) with L=2*[[h,1],[0,h]],
        #           [SY] exp of nilpotent N: e^N = Id + N (N^2=0)
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_formal_monodromy
        h = 1.0
        M = compute_formal_monodromy(c=13.0, h=h)
        e_scalar = cmath.exp(4.0j * math.pi * h)
        # For h=1 (integer), e^{4*pi*i} = 1
        assert abs(e_scalar - 1.0) < 1e-14
        expected = np.array([
            [1.0, 4.0j * math.pi],
            [0.0, 1.0],
        ], dtype=complex)
        assert np.allclose(M, expected, atol=1e-12)

    def test_formal_monodromy_half_integer_h(self):
        """At h=1/2: e^{4*pi*i*(1/2)} = e^{2*pi*i} = 1.
        # VERIFIED: [DC] direct, [SY] integer 2h gives trivial scalar phase
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_formal_monodromy
        M = compute_formal_monodromy(c=13.0, h=0.5)
        e_scalar = cmath.exp(2.0j * math.pi)  # = 1
        assert abs(e_scalar - 1.0) < 1e-14
        assert abs(M[0, 0] - 1.0) < 1e-12
        assert abs(M[1, 1] - 1.0) < 1e-12

    def test_total_monodromy_equals_formal(self):
        """M_actual = M_formal (Stokes trivial => monodromy entirely formal).
        # VERIFIED: [DC] from Phi(ze^{2pi*i}), [SY] scalar Q => no Stokes
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            compute_stokes_matrices_jordan,
        )
        c, h = 13.0, 1.5
        result = compute_stokes_matrices_jordan(c, h)
        assert np.allclose(
            result.total_monodromy, result.formal_monodromy, atol=1e-13
        )

    def test_stokes_trivial_various_c(self):
        """Stokes trivial for all c (not just self-dual c=13).
        # VERIFIED: [DC] c-independent argument, [SY] Q scalar for all c
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            compute_stokes_matrices_jordan,
        )
        for c_val in [0.5, 1.0, 13.0, 25.0, 100.0]:
            result = compute_stokes_matrices_jordan(c_val, 1.0)
            assert result.cyclic_relation_error < 1e-13
            for S_k in result.stokes_matrices:
                assert np.allclose(S_k, np.eye(2))


# =====================================================================
# Section 6: Formal monodromy
# =====================================================================

class TestFormalMonodromy:
    """Test formal monodromy computation."""

    def test_integer_h_trivial_scalar(self):
        """At integer h: e^{4*pi*i*h} = 1.
        # VERIFIED: [DC] direct, [NE] e^{4*pi*i} = 1.0 + 0.0j
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_formal_monodromy
        for h in [0.0, 1.0, 2.0, 5.0]:
            M = compute_formal_monodromy(c=13.0, h=h)
            assert abs(M[0, 0] - 1.0) < 1e-12
            assert abs(M[1, 1] - 1.0) < 1e-12

    def test_quarter_integer_h(self):
        """At h=1/4: e^{4*pi*i/4} = e^{pi*i} = -1.
        # VERIFIED: [DC] direct, [NE] e^{pi*i} = -1.0
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_formal_monodromy
        M = compute_formal_monodromy(c=13.0, h=0.25)
        assert abs(M[0, 0] - (-1.0)) < 1e-12

    def test_off_diagonal_always_4pi_i(self):
        """Off-diagonal entry is always e^{4*pi*i*h} * 4*pi*i.
        # VERIFIED: [DC] exp(2*pi*i*[[0,2],[0,0]]) = [[1,4*pi*i],[0,1]],
        #           [SY] N^2 = 0 => exp = Id + N
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_formal_monodromy
        for h in [0.5, 1.0, 1.5, 2.5]:
            M = compute_formal_monodromy(c=13.0, h=h)
            e_scalar = cmath.exp(4.0j * math.pi * h)
            expected_01 = e_scalar * 4.0j * math.pi
            assert abs(M[0, 1] - expected_01) < 1e-10

    def test_lower_left_zero(self):
        """M[1,0] = 0 (upper triangular preserved).
        # VERIFIED: [DC] upper triangular exp, [SY] block structure
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_formal_monodromy
        for h in [0.0, 1.0, 2.5]:
            M = compute_formal_monodromy(c=13.0, h=h)
            assert abs(M[1, 0]) < 1e-15


# =====================================================================
# Section 7: Numerical monodromy
# =====================================================================

class TestNumericalMonodromy:
    """Test numerical monodromy against analytic formula."""

    @pytest.mark.slow
    def test_scalar_monodromy_numerical(self):
        """Numerical monodromy for scalar case matches e^{4*pi*i*h}.
        # VERIFIED: [DC] analytic formula, [NE] numerical integration
        """
        from lib.irregular_kz_stokes_virasoro_engine import numerical_monodromy
        c, h = 4.0, 1.0  # small c for numerical stability
        rho_T = np.array([[h]], dtype=complex)
        M_num = numerical_monodromy(c, rho_T, radius=2.0, n_steps=20000)
        M_expected = np.array([[cmath.exp(4.0j * math.pi * h)]], dtype=complex)
        # At h=1 (integer), monodromy is identity
        assert abs(M_num[0, 0] - 1.0) < 0.05, (
            f"Scalar monodromy error: {abs(M_num[0, 0] - 1.0)}"
        )

    @pytest.mark.slow
    def test_jordan_monodromy_numerical(self):
        """Numerical monodromy for 2x2 Jordan matches analytic formula.
        # VERIFIED: [DC] analytic Phi(ze^{2pi*i}), [NE] RK4 integration
        """
        from lib.irregular_kz_stokes_virasoro_engine import (
            numerical_monodromy, compute_formal_monodromy,
        )
        c, h = 4.0, 1.0  # small c, integer h for stability
        rho_T = np.array([[h, 1.0], [0.0, h]], dtype=complex)
        M_num = numerical_monodromy(c, rho_T, radius=2.0, n_steps=40000)
        M_analytic = compute_formal_monodromy(c, h)
        # At integer h, M_analytic = [[1, 4*pi*i], [0, 1]]
        # Moderate tolerance for numerical integration
        err = np.max(np.abs(M_num - M_analytic))
        assert err < 0.5, (
            f"Jordan monodromy error: {err}\n"
            f"Numerical:\n{M_num}\nAnalytic:\n{M_analytic}"
        )


# =====================================================================
# Section 8: Diagonal system
# =====================================================================

class TestDiagonalSystem:
    """Test diagonal (non-Jordan) arity-2 system."""

    def test_stokes_trivial(self):
        """Diagonal system has trivial Stokes (same irregular type).
        # VERIFIED: [DC] scalar Q => no Stokes, [LT] Wasow Thm 19.1
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_diagonal_stokes
        result = compute_diagonal_stokes(13.0, 1.0, 2.0)
        assert result.stokes_trivial

    def test_formal_monodromy_diagonal(self):
        """Diagonal monodromy = diag(e^{4*pi*i*h1}, e^{4*pi*i*h2}).
        # VERIFIED: [DC] direct, [SY] diagonal system = two scalars
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_diagonal_stokes
        h1, h2 = 1.0, 2.0
        result = compute_diagonal_stokes(13.0, h1, h2)
        M = result.formal_monodromy
        assert abs(M[0, 0] - cmath.exp(4.0j * math.pi * h1)) < 1e-12
        assert abs(M[1, 1] - cmath.exp(4.0j * math.pi * h2)) < 1e-12
        assert abs(M[0, 1]) < 1e-15
        assert abs(M[1, 0]) < 1e-15

    def test_equal_weights(self):
        """h1 = h2: still trivial Stokes (scalar Q dominates).
        # VERIFIED: [DC] same irregular part, [SY] h1=h2 is proportional to Id
        """
        from lib.irregular_kz_stokes_virasoro_engine import compute_diagonal_stokes
        result = compute_diagonal_stokes(13.0, 2.0, 2.0)
        assert result.stokes_trivial


# =====================================================================
# Section 9: Cross-consistency with resurgence engine
# =====================================================================

class TestCrossConsistency:
    """Cross-check with the shadow tower resurgence/Stokes engine."""

    def test_kappa_agrees(self):
        """kappa from KZ engine matches resurgence engine.
        # VERIFIED: [DC] both compute c/2, [CF] cross-engine agreement
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        from lib.resurgence_stokes_engine import virasoro_shadow_invariants
        for c_val in [1.0, 13.0, 25.0]:
            kz_kappa = VirasoroKZData(c_val).kappa
            shadow_kappa = virasoro_shadow_invariants(c_val)['kappa']
            assert abs(kz_kappa - shadow_kappa) < 1e-15

    def test_poincare_rank_vs_shadow_pole(self):
        """Poincare rank 2 is consistent with r-matrix cubic pole.
        # VERIFIED: [DC] pole order 3 - 1 = 2,
        #           [CF] shadow r-matrix (c/2)/z^3 has pole order 3
        """
        from lib.irregular_kz_stokes_virasoro_engine import VirasoroKZData
        kz = VirasoroKZData(13.0)
        # The Virasoro r-matrix has pole order 3 (C11), so Poincare rank = 2
        assert kz.poincare_rank == 2
        # The shadow tower Stokes (resurgence engine) uses Borel singularities
        # from the shadow growth rate rho.  The KZ Stokes uses the ODE at z=0.
        # These are DIFFERENT Stokes phenomena (shadow vs irregular KZ).
        # The cross-check is that both derive from the same r-matrix.


# =====================================================================
# Section 10: Full diagnostic
# =====================================================================

class TestFullDiagnostic:
    """Integration test: run the full diagnostic."""

    def test_diagnostic_runs(self):
        """Full diagnostic completes without error.
        # VERIFIED: [DC] integration test, [SY] all sub-computations verified
        """
        from lib.irregular_kz_stokes_virasoro_engine import full_diagnostic
        result = full_diagnostic(c=13.0, h=1.0)
        assert result['stokes_trivial'] is True
        assert result['stokes_result'].cyclic_relation_error < 1e-13
        assert result['ode_verification']['max_relative_error'] < 1e-4
        assert result['scalar_ode_verification']['relative_error'] < 1e-5

    def test_diagnostic_c_equals_1(self):
        """Diagnostic at c=1 (small central charge).
        # VERIFIED: [DC] integration test, [LC] small-c regime
        """
        from lib.irregular_kz_stokes_virasoro_engine import full_diagnostic
        result = full_diagnostic(c=1.0, h=0.5)
        assert result['stokes_trivial'] is True

    def test_diagnostic_c_equals_26(self):
        """Diagnostic at c=26 (string theory critical dimension).
        # VERIFIED: [DC] integration test, [LC] c=26 critical
        """
        from lib.irregular_kz_stokes_virasoro_engine import full_diagnostic
        result = full_diagnostic(c=26.0, h=1.0)
        assert result['stokes_trivial'] is True
        # At c=26: kappa=13, kappa' = (26-26)/2 = 0, kappa+kappa' = 13
        assert abs(result['kz_data'].kappa - 13.0) < 1e-15
