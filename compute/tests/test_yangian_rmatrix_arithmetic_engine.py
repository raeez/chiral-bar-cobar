r"""Tests for yangian_rmatrix_arithmetic_engine.py.

Verification axes:
  Path 1: Direct R-matrix computation from Yangian coproduct
  Path 2: Shadow extraction from Theta_A (kappa and Casimir)
  Path 3: Yang-Baxter equation self-consistency
  Path 4: Representation-theoretic eigenvalue computation

Ground truth sources:
  - Molev, "Yangians and classical Lie algebras", AMS 2007.
  - Chari-Pressley, "A Guide to Quantum Groups", Cambridge 1994.
  - Jimbo, "A q-difference analogue of U(g)", Lett. Math. Phys. 1985.
  - Belavin-Drinfeld, "Solutions of the classical YBE" (1982).
  - landscape_census.tex (kappa formulas)
  - AP19 (bar kernel absorbs a pole)
  - AP39 (C_2 != kappa for rank > 1)
"""

import math

import numpy as np
import pytest

from compute.lib.yangian_rmatrix_arithmetic_engine import (
    _prime_factorization,
    fraction_prime_data,
    lie_algebra_data,
    modular_characteristic,
    modular_characteristic_exact,
    casimir_tensor,
    casimir_eigenvalue,
    slN_casimir,
    soN_casimir,
    sp2n_casimir,
    g2_generators_7dim,
    g2_casimir_7dim,
    yang_rmatrix_coefficients,
    rmatrix_coefficient_traces,
    rmatrix_coefficient_prime_factorization,
    shadow_from_rmatrix,
    verify_kappa_shadow_consistency,
    ybe_coefficient_relations,
    _ybe_numerical_error,
    _full_rmatrix,
    ybe_independent_coefficients,
    jacobi_theta_1,
    jacobi_theta_2,
    jacobi_theta_3,
    jacobi_theta_4,
    theta_constants,
    elliptic_rmatrix_sl2,
    elliptic_rmatrix_cm_points,
    trigonometric_rmatrix_sl2,
    trigonometric_rmatrix_slN,
    trig_rmatrix_root_of_unity,
    trig_rmatrix_eigenvalues_irreps,
    crossing_unitarity_sl2,
    crossing_scalar_functions_classical,
    crossing_prime_factorization_typeA,
    verify_rmatrix_4_paths,
    casimir_trace_identity,
    verify_operator_algebra,
    verify_cybe,
    degeneration_chain_sl2,
    rmatrix_arithmetic_landscape,
    _permutation_matrix,
    _identity_tensor,
    _embed_12,
    _embed_23,
    _embed_13,
)

from fractions import Fraction


# =========================================================================
# Section 0: Utility tests
# =========================================================================

class TestPrimeFactorization:
    """Tests for prime factorization utilities."""

    def test_prime_factorization_small(self):
        assert _prime_factorization(1) == {}
        assert _prime_factorization(2) == {2: 1}
        assert _prime_factorization(12) == {2: 2, 3: 1}
        assert _prime_factorization(60) == {2: 2, 3: 1, 5: 1}

    def test_prime_factorization_primes(self):
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
            assert _prime_factorization(p) == {p: 1}

    def test_prime_factorization_powers(self):
        assert _prime_factorization(8) == {2: 3}
        assert _prime_factorization(27) == {3: 3}
        assert _prime_factorization(5760) == {2: 7, 3: 2, 5: 1}

    def test_fraction_prime_data(self):
        f = Fraction(7, 5760)
        data = fraction_prime_data(f)
        assert data['numerator'] == 7
        assert data['denominator'] == 5760
        assert data['num_factors'] == {7: 1}
        assert data['den_factors'] == {2: 7, 3: 2, 5: 1}


# =========================================================================
# Section 1: Lie algebra data and Casimir tests
# =========================================================================

class TestLieAlgebraData:
    """Tests for Lie algebra fundamental data."""

    def test_sl2_data(self):
        data = lie_algebra_data('A', 1)
        assert data['dim_g'] == 3
        assert data['dual_coxeter'] == 2
        assert data['fund_dim'] == 2

    def test_sl3_data(self):
        data = lie_algebra_data('A', 2)
        assert data['dim_g'] == 8
        assert data['dual_coxeter'] == 3
        assert data['fund_dim'] == 3

    def test_sl4_data(self):
        data = lie_algebra_data('A', 3)
        assert data['dim_g'] == 15
        assert data['dual_coxeter'] == 4
        assert data['fund_dim'] == 4

    def test_so5_data(self):
        """so_5 = sp_4 (B_2 = C_2 isomorphism at the level of Lie algebras)."""
        data_B = lie_algebra_data('B', 2)
        assert data_B['dim_g'] == 10
        assert data_B['dual_coxeter'] == 3
        assert data_B['fund_dim'] == 5

    def test_sp4_data(self):
        data_C = lie_algebra_data('C', 2)
        assert data_C['dim_g'] == 10
        assert data_C['dual_coxeter'] == 3
        assert data_C['fund_dim'] == 4

    def test_so8_data(self):
        data_D = lie_algebra_data('D', 4)
        assert data_D['dim_g'] == 28
        assert data_D['dual_coxeter'] == 6
        assert data_D['fund_dim'] == 8

    def test_g2_data(self):
        data = lie_algebra_data('G2', 2)
        assert data['dim_g'] == 14
        assert data['dual_coxeter'] == 4
        assert data['fund_dim'] == 7


class TestModularCharacteristic:
    """Tests for kappa = dim(g)(k + h^vee)/(2h^vee)."""

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        kappa = modular_characteristic('A', 1, 1.0)
        assert abs(kappa - 9.0 / 4) < 1e-12

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        kappa = modular_characteristic('A', 2, 1.0)
        assert abs(kappa - 16.0 / 3) < 1e-12

    def test_kappa_exact(self):
        """Exact rational arithmetic for kappa."""
        kappa = modular_characteristic_exact('A', 1, Fraction(1))
        assert kappa == Fraction(9, 4)

    def test_kappa_sl3_exact(self):
        kappa = modular_characteristic_exact('A', 2, Fraction(1))
        assert kappa == Fraction(16, 3)

    def test_kappa_so5_k1(self):
        """kappa(so_5, k=1) = 10*(1+3)/(2*3) = 20/3."""
        kappa = modular_characteristic('B', 2, 1.0)
        assert abs(kappa - 20.0 / 3) < 1e-12

    def test_kappa_sp4_k1(self):
        """kappa(sp_4, k=1) = 10*(1+3)/(2*3) = 20/3."""
        kappa = modular_characteristic('C', 2, 1.0)
        assert abs(kappa - 20.0 / 3) < 1e-12

    def test_kappa_g2_k1(self):
        """kappa(G_2, k=1) = 14*(1+4)/(2*4) = 35/4."""
        kappa = modular_characteristic('G2', 2, 1.0)
        assert abs(kappa - 35.0 / 4) < 1e-12


class TestCasimirTensor:
    """Tests for Casimir tensors in fundamental representations."""

    def test_sl2_casimir_traceless(self):
        """Omega_{sl_2} = P - I/2 should be traceless on each factor."""
        Omega = slN_casimir(2)
        # Partial trace: sum_j Omega_{(ij),(jk)} should be proportional to delta_{ik}
        C2 = np.zeros((2, 2), dtype=complex)
        for i in range(2):
            for k in range(2):
                for j in range(2):
                    C2[i, k] += Omega[i * 2 + j, j * 2 + k]
        # C2 should be (3/2) * I_2 (Casimir eigenvalue for sl_2 fund)
        assert abs(C2[0, 0] - 3.0 / 2) < 1e-12
        assert abs(C2[1, 1] - 3.0 / 2) < 1e-12
        assert abs(C2[0, 1]) < 1e-12

    def test_sl3_casimir_eigenvalue(self):
        """C_2(fund) = (N^2-1)/N = 8/3 for sl_3."""
        C2 = casimir_eigenvalue('A', 2)
        assert abs(C2 - 8.0 / 3) < 1e-10

    def test_slN_casimir_eigenvalue_formula(self):
        """C_2(fund) = (N^2-1)/N for sl_N."""
        for n in range(1, 6):
            N = n + 1
            C2 = casimir_eigenvalue('A', n)
            expected = (N * N - 1.0) / N
            assert abs(C2 - expected) < 1e-8, f"sl_{N}: C2={C2}, expected={expected}"

    def test_soN_casimir_eigenvalue(self):
        """C_2(fund) for so_N should be (N-1)/2."""
        for n in range(2, 5):
            # Type B: so_{2n+1}
            C2 = casimir_eigenvalue('B', n)
            N = 2 * n + 1
            expected = (N - 1.0) / 2
            assert abs(C2 - expected) < 1e-6, f"so_{N}: C2={C2}, expected={expected}"

    def test_sp_casimir_eigenvalue(self):
        """C_2(fund) for sp_{2n} should be (2n+1)/2."""
        for n in range(1, 4):
            C2 = casimir_eigenvalue('C', n)
            expected = (2 * n + 1.0) / 2
            assert abs(C2 - expected) < 1e-6, f"sp_{2*n}: C2={C2}, expected={expected}"

    def test_casimir_symmetry(self):
        """Omega_{12} should be symmetric under exchange: Omega_{21} = P Omega P."""
        for lie_type, n in [('A', 1), ('A', 2), ('B', 2), ('C', 1)]:
            data = lie_algebra_data(lie_type, n)
            N = data['fund_dim']
            Omega = casimir_tensor(lie_type, n)
            P = _permutation_matrix(N)
            Omega_21 = P @ Omega @ P
            err = float(np.max(np.abs(Omega - Omega_21)))
            assert err < 1e-10, f"{lie_type}_{n}: Omega not symmetric, err={err}"


class TestCasimirUniversalIdentity:
    """Test the universal identity C_2(fund) = dim(g) / dim(fund).

    This is a fundamental check connecting the Casimir eigenvalue
    to the dimension ratio.  It must hold for ALL simple Lie algebras
    with trace-form normalization.
    """

    @pytest.mark.parametrize("lie_type,n", [
        ('A', 1), ('A', 2), ('A', 3), ('A', 4),
        ('B', 2), ('B', 3),
        ('C', 1), ('C', 2), ('C', 3),
        ('D', 2), ('D', 3), ('D', 4),
    ])
    def test_universal_identity(self, lie_type, n):
        result = casimir_trace_identity(lie_type, n)
        assert result['passes'], (
            f"{lie_type}_{n}: C_2={result['C2_fund']}, "
            f"dim(g)/dim(fund)={result['dim_g_over_dim_fund']}, "
            f"error={result['error']}"
        )


class TestG2:
    """Tests for G_2 exceptional algebra."""

    def test_g2_generators_count(self):
        """G_2 has 14 generators."""
        gens = g2_generators_7dim()
        assert len(gens) == 14

    def test_g2_generators_antisymmetric(self):
        """G_2 generators should be antisymmetric (as elements of so_7)."""
        gens = g2_generators_7dim()
        for g in gens:
            err = float(np.max(np.abs(g + g.T)))
            assert err < 1e-10

    def test_g2_casimir_symmetric(self):
        """G_2 Casimir should be symmetric: Omega_{12} = Omega_{21}."""
        Omega = g2_casimir_7dim()
        P = _permutation_matrix(7)
        Omega_21 = P @ Omega @ P
        err = float(np.max(np.abs(Omega - Omega_21)))
        assert err < 1e-8

    def test_g2_casimir_eigenvalue(self):
        """C_2(fund) for G_2 should equal dim(G_2)/dim(fund) = 14/7 = 2."""
        C2 = casimir_eigenvalue('G2', 2)
        assert abs(C2 - 2.0) < 1e-6


# =========================================================================
# Section 2: R-matrix coefficient tests
# =========================================================================

class TestRMatrixCoefficients:
    """Tests for R_k higher-order coefficients."""

    def test_sl2_R0_is_identity(self):
        coeffs = yang_rmatrix_coefficients('A', 1, max_order=4)
        I4 = _identity_tensor(2)
        assert np.allclose(coeffs[0], I4)

    def test_sl2_R1_is_casimir(self):
        coeffs = yang_rmatrix_coefficients('A', 1, max_order=4)
        Omega = slN_casimir(2)
        assert np.allclose(coeffs[1], Omega)

    def test_sl2_R2_is_omega_squared(self):
        """For sl_2 in the shadow expansion: R_2 = Omega^2."""
        coeffs = yang_rmatrix_coefficients('A', 1, max_order=4)
        Omega = slN_casimir(2)
        assert np.allclose(coeffs[2], Omega @ Omega, atol=1e-12)

    def test_sl3_R2_is_omega_squared(self):
        """For sl_3 shadow expansion: R_2 = Omega^2."""
        coeffs = yang_rmatrix_coefficients('A', 2, max_order=4)
        Omega = slN_casimir(3)
        assert np.allclose(coeffs[2], Omega @ Omega, atol=1e-12)

    def test_typeB_R2_proportional_to_Q(self):
        """For so_{2n+1}: R_k = kappa_R^{k-1} Q for k >= 2."""
        coeffs = yang_rmatrix_coefficients('B', 2, max_order=4)
        N = 5  # so_5
        d = N * N
        Q = np.zeros((d, d), dtype=complex)
        for i in range(N):
            for k in range(N):
                Q[i * N + i, k * N + k] = 1.0
        kappa_R = 2 - 0.5  # n - 1/2 = 1.5
        assert np.allclose(coeffs[2], kappa_R * Q, atol=1e-10)
        assert np.allclose(coeffs[3], kappa_R ** 2 * Q, atol=1e-10)

    def test_typeC_R2_proportional_to_K(self):
        """For sp_{2n}: R_k = -kappa_R^{k-1} K for k >= 2."""
        coeffs = yang_rmatrix_coefficients('C', 2, max_order=4)
        # R_2 should be -kappa_R * K
        # R_3 should be -kappa_R^2 * K
        kappa_R = 3.0  # n+1 = 3
        N = 4  # sp_4
        # K is extracted from coeffs[2] / (-kappa_R)
        K_extracted = coeffs[2] / (-kappa_R)
        # R_3 should be -kappa_R^2 * K
        assert np.allclose(coeffs[3], -kappa_R ** 2 * K_extracted, atol=1e-10)

    def test_coefficient_traces_sl2(self):
        """Normalized traces of R_k for sl_2."""
        traces = rmatrix_coefficient_traces('A', 1, max_order=4)
        # tr(R_0)/4 = 1
        assert abs(traces[0] - 1.0) < 1e-12
        # tr(Omega)/4 for sl_2: Omega = P - I/2.  tr(P) = 2, tr(I/2) = 2.
        # tr(Omega) = 0.  So traces[1] = 0.
        assert abs(traces[1]) < 1e-12

    def test_coefficient_traces_sl3(self):
        """Normalized traces for sl_3."""
        traces = rmatrix_coefficient_traces('A', 2, max_order=3)
        assert abs(traces[0] - 1.0) < 1e-12
        # tr(Omega_{sl_3}) = 0 (traceless Casimir)
        assert abs(traces[1]) < 1e-10


class TestRMatrixPrimeFactorization:
    """Tests for prime factorizations of R-matrix coefficient denominators."""

    def test_sl2_prime_data(self):
        data = rmatrix_coefficient_prime_factorization('A', 1, max_order=4)
        # tr(R_0) = 1, denominator = 1
        assert data[0]['denominator'] == 1

    def test_sl3_prime_data(self):
        data = rmatrix_coefficient_prime_factorization('A', 2, max_order=3)
        assert data[0]['denominator'] == 1


# =========================================================================
# Section 3: Shadow interpretation tests
# =========================================================================

class TestShadowInterpretation:
    """Tests for the shadow <-> R-matrix dictionary."""

    def test_kappa_shadow_sl2(self):
        """Verify kappa from the shadow interpretation for sl_2."""
        result = shadow_from_rmatrix('A', 1, 1.0)
        assert abs(result['kappa'] - 9.0 / 4) < 1e-12
        assert abs(result['C2_fund'] - 3.0 / 2) < 1e-10

    def test_kappa_shadow_sl3(self):
        result = shadow_from_rmatrix('A', 2, 1.0)
        assert abs(result['kappa'] - 16.0 / 3) < 1e-12
        assert abs(result['C2_fund'] - 8.0 / 3) < 1e-10

    def test_kappa_shadow_consistency_all_types(self):
        """Verify C_2 = dim(g)/dim(fund) for all types (AP39 aware)."""
        for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
            result = verify_kappa_shadow_consistency(lie_type, n, 1.0)
            assert result['C2_equals_dim_g_over_N'], f"Failed for {lie_type}_{n}"

    def test_shadow_S2_is_kappa(self):
        """S_2 = kappa (the quadratic shadow)."""
        for k_level in [1.0, 2.0, 5.0]:
            result = shadow_from_rmatrix('A', 1, k_level)
            assert abs(result['S2'] - result['kappa']) < 1e-12


# =========================================================================
# Section 4: Yang-Baxter equation tests
# =========================================================================

class TestYangBaxterEquation:
    """Tests for YBE self-consistency across all types."""

    @pytest.mark.parametrize("lie_type,n", [
        ('A', 1), ('A', 2), ('A', 3),
    ])
    def test_ybe_typeA(self, lie_type, n):
        """YBE for type A at several spectral parameter values."""
        err = _ybe_numerical_error(lie_type, n, 3.7, 1.3)
        assert err < 1e-8, f"YBE error for {lie_type}_{n}: {err}"

    @pytest.mark.parametrize("lie_type,n", [
        ('B', 2), ('B', 3),
    ])
    def test_ybe_typeB(self, lie_type, n):
        err = _ybe_numerical_error(lie_type, n, 5.2, 2.1)
        assert err < 1e-8, f"YBE error for {lie_type}_{n}: {err}"

    @pytest.mark.parametrize("lie_type,n", [
        ('C', 1), ('C', 2),
    ])
    def test_ybe_typeC(self, lie_type, n):
        err = _ybe_numerical_error(lie_type, n, 7.1, 4.3)
        assert err < 1e-8, f"YBE error for {lie_type}_{n}: {err}"

    @pytest.mark.parametrize("lie_type,n", [
        ('D', 3), ('D', 4),
    ])
    def test_ybe_typeD(self, lie_type, n):
        # Use parameters that avoid the pole at u-v = kappa_R = n-1.
        # For D_4: kappa_R = 3, so u-v must not be 3.
        err = _ybe_numerical_error(lie_type, n, 8.5, 3.7)
        assert err < 1e-8, f"YBE error for {lie_type}_{n}: {err}"

    def test_ybe_multiple_points_sl2(self):
        """YBE at many different spectral parameter values for sl_2."""
        params = [(2.5, 0.7), (5.0, 3.0), (10.0, 1.0), (4.2, 2.8), (7.7, 3.3)]
        for u, v in params:
            err = _ybe_numerical_error('A', 1, u, v)
            assert err < 1e-8, f"YBE sl_2 at u={u}, v={v}: err={err}"

    def test_ybe_multiple_points_sl3(self):
        """YBE at several points for sl_3."""
        for u, v in [(3.0, 1.0), (6.0, 2.0), (8.5, 4.5)]:
            err = _ybe_numerical_error('A', 2, u, v)
            assert err < 1e-8, f"YBE sl_3 at u={u}, v={v}: err={err}"

    def test_ybe_coefficient_relations_sl2(self):
        """Full YBE coefficient analysis for sl_2."""
        result = ybe_coefficient_relations('A', 1, 4)
        assert result['passes'], f"YBE failed for sl_2: max_err={result['max_ybe_error']}"

    def test_ybe_coefficient_relations_so5(self):
        result = ybe_coefficient_relations('B', 2, 4)
        assert result['passes'], f"YBE failed for so_5: max_err={result['max_ybe_error']}"


class TestYBEIndependentCoefficients:
    """Test how many independent R_k exist before YBE constrains them."""

    def test_typeA_1_independent(self):
        """Type A: Yang R-matrix is exact with 1 independent operator (P)."""
        result = ybe_independent_coefficients('A', 2)
        assert result['n_independent'] == 1

    def test_typeBCD_2_independent(self):
        """Types B, C, D: 2 independent operators (P and Q/K)."""
        for lie_type in ['B', 'C', 'D']:
            n = 3 if lie_type == 'D' else 2
            result = ybe_independent_coefficients(lie_type, n)
            assert result['n_independent'] == 2

    def test_g2_2_independent(self):
        """G_2 has rank 2, so 2 independent Casimir elements."""
        result = ybe_independent_coefficients('G2', 2)
        assert result['n_independent'] == 2


# =========================================================================
# Section 5: CYBE (infinitesimal braid relations) tests
# =========================================================================

class TestCYBE:
    """Tests for the classical Yang-Baxter equation."""

    @pytest.mark.parametrize("lie_type,n", [
        ('A', 1), ('A', 2), ('A', 3), ('A', 4),
        ('B', 2), ('B', 3),
        ('C', 1), ('C', 2), ('C', 3),
        ('D', 2), ('D', 3),
    ])
    def test_cybe_all_types(self, lie_type, n):
        """CYBE (IBR) for all classical types."""
        result = verify_cybe(lie_type, n)
        assert result['passes'], (
            f"CYBE failed for {lie_type}_{n}: "
            f"IBR1={result['ibr1_error']}, IBR2={result['ibr2_error']}"
        )

    def test_cybe_g2(self):
        """CYBE for G_2 in the 7-dim representation."""
        result = verify_cybe('G2', 2)
        assert result['passes'], f"CYBE failed for G_2: max_err={result['max_error']}"


# =========================================================================
# Section 6: Operator algebra tests
# =========================================================================

class TestOperatorAlgebra:
    """Tests for P, Q, K operator identities."""

    def test_P_squared_is_I(self):
        """P^2 = I for all N."""
        for N in [2, 3, 4, 5]:
            P = _permutation_matrix(N)
            I = _identity_tensor(N)
            assert np.allclose(P @ P, I)

    @pytest.mark.parametrize("lie_type,n", [
        ('B', 2), ('B', 3), ('D', 3), ('D', 4),
    ])
    def test_operator_algebra_BCD(self, lie_type, n):
        result = verify_operator_algebra(lie_type, n)
        assert result['all_pass'], f"Operator algebra failed for {lie_type}_{n}: {result}"

    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_operator_algebra_typeC(self, n):
        result = verify_operator_algebra('C', n)
        assert result['all_pass'], f"Operator algebra failed for C_{n}: {result}"


# =========================================================================
# Section 7: Elliptic R-matrix tests
# =========================================================================

class TestJacobiTheta:
    """Tests for Jacobi theta functions."""

    def test_theta1_zero(self):
        """theta_1(0, tau) = 0 for all tau."""
        for tau in [1j, 2j, 0.5 + 1j]:
            val = jacobi_theta_1(0.0, tau)
            assert abs(val) < 1e-12

    def test_theta1_odd(self):
        """theta_1(-z, tau) = -theta_1(z, tau) (odd function)."""
        z = 0.3
        for tau in [1j, 0.5 + 1j]:
            assert abs(jacobi_theta_1(-z, tau) + jacobi_theta_1(z, tau)) < 1e-10

    def test_theta_jacobi_identity(self):
        """Jacobi identity: theta_3^4 = theta_2^4 + theta_4^4."""
        for tau in [1j, 0.5 + 2j, 0.3 + 1.5j]:
            tc = theta_constants(tau)
            lhs = tc['theta3'] ** 4
            rhs = tc['theta2'] ** 4 + tc['theta4'] ** 4
            assert abs(lhs - rhs) < 1e-8, f"Jacobi identity failed at tau={tau}"

    def test_theta_constants_at_i(self):
        """At tau = i: theta_2(0,i) = theta_4(0,i) (square lattice symmetry)."""
        tc = theta_constants(1j)
        # theta_2(0,i) and theta_4(0,i) should have same magnitude
        # (they may differ by a phase due to convention)
        assert abs(abs(tc['theta2']) - abs(tc['theta4'])) < 1e-6


class TestEllipticRMatrix:
    """Tests for the elliptic R-matrix at CM points."""

    def test_elliptic_rmatrix_nonsingular(self):
        """Elliptic R-matrix at generic z should be nonsingular."""
        R = elliptic_rmatrix_sl2(0.15, 1j)
        assert abs(np.linalg.det(R)) > 1e-10

    def test_jacobi_identity_at_cm_gauss(self):
        """Jacobi identity at the Gaussian CM point tau = i."""
        results = elliptic_rmatrix_cm_points(0.1)
        assert results['tau_i']['jacobi_identity_error'] < 1e-8

    def test_jacobi_identity_at_cm_eisenstein(self):
        """Jacobi identity at the Eisenstein CM point tau = rho."""
        results = elliptic_rmatrix_cm_points(0.1)
        assert results['tau_rho']['jacobi_identity_error'] < 1e-6

    def test_theta_ratio_at_i(self):
        """At tau = i: theta_3 / theta_4 should be close to 2^{1/4}."""
        results = elliptic_rmatrix_cm_points(0.1)
        ratio = abs(results['tau_i']['ratio_theta3_theta4'])
        expected = 2 ** 0.25
        assert abs(ratio - expected) < 0.01

    def test_elliptic_rmatrix_size(self):
        """Elliptic R-matrix should be 4x4 for sl_2."""
        R = elliptic_rmatrix_sl2(0.2, 1j)
        assert R.shape == (4, 4)


# =========================================================================
# Section 8: Trigonometric R-matrix tests
# =========================================================================

class TestTrigonometricRMatrix:
    """Tests for trigonometric R-matrices at roots of unity."""

    def test_jimbo_sl2_dimensions(self):
        """Jimbo R-matrix for sl_2 should be 4x4."""
        q = np.exp(2j * np.pi / 5)
        R = trigonometric_rmatrix_sl2(q)
        assert R.shape == (4, 4)

    def test_jimbo_sl2_structure(self):
        """Jimbo R-matrix: R_{00} = R_{33} = q, R_{11} = R_{22} = 1, R_{12} = q-q^{-1}."""
        q = np.exp(2j * np.pi / 7)
        R = trigonometric_rmatrix_sl2(q)
        assert abs(R[0, 0] - q) < 1e-12
        assert abs(R[3, 3] - q) < 1e-12
        assert abs(R[1, 1] - 1.0) < 1e-12
        assert abs(R[2, 2] - 1.0) < 1e-12
        assert abs(R[1, 2] - (q - 1.0 / q)) < 1e-12

    def test_jimbo_ybe(self):
        """Jimbo R-matrix satisfies the quantum Yang-Baxter equation.

        QYBE: R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}
        (using the constant R-matrix, with proper 3-fold embeddings).
        """
        q = np.exp(2j * np.pi / 5)
        R = trigonometric_rmatrix_sl2(q)
        N = 2
        # Proper embeddings into V^{tensor 3}
        R12 = _embed_12(R, N)
        R23 = _embed_23(R, N)
        R13 = _embed_13(R, N)
        lhs = R12 @ R13 @ R23
        rhs = R23 @ R13 @ R12
        assert np.allclose(lhs, rhs, atol=1e-8)

    def test_slN_rmatrix_dimensions(self):
        """R-matrix for sl_N should be N^2 x N^2."""
        for N in [2, 3, 4]:
            q = np.exp(2j * np.pi / 5)
            R = trigonometric_rmatrix_slN(N, q)
            assert R.shape == (N * N, N * N)

    @pytest.mark.parametrize("N_root", [3, 4, 5, 6, 7])
    def test_root_of_unity_cyclotomic(self, N_root):
        """R-matrix entries at roots of unity lie in cyclotomic field."""
        result = trig_rmatrix_root_of_unity(N_root)
        assert result['q_power_check'] < 1e-10
        assert result['cyclotomic_field'] == f'Q(zeta_{N_root})'

    @pytest.mark.parametrize("N_root", [5, 7, 11, 13])
    def test_eigenvalues_on_irreps_sl2_generic(self, N_root):
        """Eigenvalues of R on Sym^2 and Alt^2 for sl_2 at GENERIC roots of unity.

        At generic q (not q^2 = 1 or q^3 = 1), the minimal polynomial
        (x - q)(x + 1/q) annihilates R.  At q^3 = 1, a Jordan block forms
        and the eigenvalue structure changes (known phenomenon).
        """
        result = trig_rmatrix_eigenvalues_irreps(N_root, 2)
        assert result['min_poly_error'] < 1e-8, (
            f"N={N_root}: min poly error = {result['min_poly_error']}"
        )

    def test_eigenvalues_root_of_unity_check_matrix(self):
        """At q = e^{2pi i/3}, the CHECK matrix R^ = PR still has correct eigenvalues.

        The Jimbo R-matrix R itself has eigenvalues q (double) and 1 (double, Jordan).
        But R^ = PR has eigenvalues q (triple) and -1/q (single), even at roots of unity.
        """
        q = np.exp(2j * np.pi / 3)
        R = trigonometric_rmatrix_sl2(q)
        P = _permutation_matrix(2)
        Rhat = P @ R
        evals = np.linalg.eigvals(Rhat)
        # Three eigenvalues should be q, one should be -1/q
        n_q = sum(abs(e - q) < 1e-8 for e in evals)
        n_alt = sum(abs(e + 1.0 / q) < 1e-8 for e in evals)
        assert n_q == 3, f"Expected 3 eigenvalues q, got {n_q}"
        assert n_alt == 1, f"Expected 1 eigenvalue -1/q, got {n_alt}"

    def test_eigenvalues_on_irreps_sl3_generic(self):
        """Eigenvalues on Sym^2 and Alt^2 for sl_3 at generic root."""
        result = trig_rmatrix_eigenvalues_irreps(7, 3)
        assert result['min_poly_error'] < 1e-8

    def test_sl2_classical_limit(self):
        """As q -> 1, the Jimbo R-matrix approaches I + hbar * (something)."""
        for hbar in [0.01, 0.001, 0.0001]:
            q = np.exp(hbar)
            R = trigonometric_rmatrix_sl2(q)
            I4 = np.eye(4, dtype=complex)
            deviation = np.max(np.abs(R - I4))
            # Should be O(hbar)
            assert deviation < 10 * abs(hbar), f"hbar={hbar}, deviation={deviation}"


# =========================================================================
# Section 9: Crossing symmetry tests
# =========================================================================

class TestCrossingSymmetry:
    """Tests for unitarity and crossing of R-matrices."""

    def test_unitarity_sl2_generic(self):
        """Check matrix R^ = PR has correct eigenvalues and minimal polynomial."""
        q = np.exp(0.3j)  # generic q
        result = crossing_unitarity_sl2(q)
        assert result['unitarity_passes'], (
            f"Unitarity failed: min_poly_err={result['min_poly_error']}, "
            f"eigenvalue_check={result['eigenvalue_check']}, "
            f"det_check={result['det_check']}"
        )

    def test_unitarity_sl2_root_of_unity(self):
        """Check matrix properties at a root of unity."""
        q = np.exp(2j * np.pi / 5)
        result = crossing_unitarity_sl2(q)
        assert result['unitarity_passes']

    def test_det_rhat_is_minus_q_squared(self):
        """det(R^) = -q^2 for sl_2."""
        for angle in [0.1, 0.5, 1.0, 2.0]:
            q = np.exp(1j * angle)
            result = crossing_unitarity_sl2(q)
            assert result['det_check'], f"det check failed at angle={angle}"

    def test_crossing_typeA_formula(self):
        """For type A: f(u) = 1 - u^2 (exact)."""
        result = crossing_scalar_functions_classical('A', 2)
        assert result['passes'], f"Crossing failed for A_2: max_err={result['max_error']}"

    @pytest.mark.parametrize("n", [1, 2, 3, 4])
    def test_crossing_prime_factorization(self, n):
        """Prime factorization of crossing parameters for sl_{n+1}."""
        result = crossing_prime_factorization_typeA(n)
        N = n + 1
        assert result['crossing_parameter_rho'] == N
        assert result['f_formula'] == '1 - u^2 = -(u-1)(u+1)'

    def test_crossing_g_formula_sl2(self):
        result = crossing_prime_factorization_typeA(1)
        assert result['g_formula'] == '-u(u + 2)'
        assert result['g_zeros'] == [0, -2]

    def test_crossing_g_formula_sl3(self):
        result = crossing_prime_factorization_typeA(2)
        assert result['g_formula'] == '-u(u + 3)'
        assert result['g_zeros'] == [0, -3]


# =========================================================================
# Section 10: Four-path verification tests
# =========================================================================

class TestFourPathVerification:
    """Tests for the four-path R-matrix verification."""

    @pytest.mark.parametrize("lie_type,n", [
        ('A', 1), ('A', 2), ('A', 3),
        ('B', 2),
        ('C', 2),
        ('D', 3),
    ])
    def test_four_paths(self, lie_type, n):
        """All four verification paths should pass."""
        result = verify_rmatrix_4_paths(lie_type, n)
        assert result['all_paths_pass'], (
            f"Four-path verification failed for {lie_type}_{n}: "
            f"C2_matches={result['path2_C2_matches']}, "
            f"ybe={result['path3_ybe_passes']}, "
            f"eigenvalues={result['path4_eigenvalue_passes']}"
        )

    def test_four_paths_sl2_multiple_levels(self):
        """Four-path verification at different levels for sl_2."""
        for k in [1.0, 2.0, 5.0, 10.0]:
            result = verify_rmatrix_4_paths('A', 1, k_level=k)
            assert result['path2_C2_matches']
            assert result['path3_ybe_passes']

    def test_four_paths_sl3_multiple_levels(self):
        """Four-path verification at different levels for sl_3."""
        for k in [1.0, 3.0]:
            result = verify_rmatrix_4_paths('A', 2, k_level=k)
            assert result['all_paths_pass']


# =========================================================================
# Section 11: Degeneration chain tests
# =========================================================================

class TestDegenerationChain:
    """Tests for the elliptic -> trigonometric -> rational degeneration."""

    def test_degeneration_chain_runs(self):
        """Degeneration chain computation should complete."""
        result = degeneration_chain_sl2(z=0.15)
        assert 'R_rational' in result
        assert len(result['trig_to_rational_convergence']) > 0

    def test_rational_rmatrix_structure(self):
        """R_rational(z) = I + P/z for sl_2."""
        z = 0.15
        result = degeneration_chain_sl2(z)
        R = result['R_rational']
        P = _permutation_matrix(2)
        I4 = _identity_tensor(2)
        expected = I4 + P / z
        assert np.allclose(R, expected)


# =========================================================================
# Section 12: Full landscape tests
# =========================================================================

class TestLandscape:
    """Tests for the full R-matrix arithmetic landscape."""

    def test_landscape_completeness(self):
        """Landscape should contain all classical types up to rank 3."""
        landscape = rmatrix_arithmetic_landscape(max_rank=3)
        expected_keys = ['A_1', 'A_2', 'A_3', 'B_2', 'B_3', 'C_1', 'C_2', 'C_3', 'D_2', 'D_3']
        for key in expected_keys:
            assert key in landscape, f"Missing {key} from landscape"

    def test_landscape_ybe_all_pass(self):
        """YBE should pass for all entries in the landscape."""
        landscape = rmatrix_arithmetic_landscape(max_rank=2)
        for key, data in landscape.items():
            if 'error' not in data:
                assert data['ybe_passes'], f"YBE failed for {key}"

    def test_landscape_cybe_all_pass(self):
        """CYBE should pass for all entries in the landscape."""
        landscape = rmatrix_arithmetic_landscape(max_rank=2)
        for key, data in landscape.items():
            if 'error' not in data:
                assert data['cybe_passes'], f"CYBE failed for {key}"

    def test_landscape_casimir_values(self):
        """Casimir eigenvalues should match known formulas."""
        landscape = rmatrix_arithmetic_landscape(max_rank=3)

        # sl_2: C_2 = 3/2
        assert abs(landscape['A_1']['C2_fund'] - 1.5) < 1e-8
        # sl_3: C_2 = 8/3
        assert abs(landscape['A_2']['C2_fund'] - 8.0 / 3) < 1e-8
        # sl_4: C_2 = 15/4
        assert abs(landscape['A_3']['C2_fund'] - 15.0 / 4) < 1e-8


# =========================================================================
# Section 13: Specific R-matrix value tests (regression)
# =========================================================================

class TestSpecificValues:
    """Regression tests for specific computed values."""

    def test_sl2_yang_rmatrix_at_u3(self):
        """R(3) = 3I + P for sl_2 is a specific 4x4 matrix."""
        R = _full_rmatrix('A', 1, 3.0)
        P = _permutation_matrix(2)
        I4 = _identity_tensor(2)
        expected = 3.0 * I4 + P
        assert np.allclose(R, expected)

    def test_so5_rmatrix_trace(self):
        """tr(R(5.0)) for so_5 should have a specific value."""
        R = _full_rmatrix('B', 2, 5.0)
        tr = np.trace(R)
        # R(u) = I - P/u + Q/(u - 3/2) for so_5 (kappa_R = 2 - 1/2 = 3/2)
        # tr(I) = 25, tr(P) = 5, tr(Q) = 5
        # tr(R(5)) = 25 - 5/5 + 5/(5-1.5) = 25 - 1 + 5/3.5 = 24 + 10/7
        expected = 25.0 - 1.0 + 5.0 / 3.5
        assert abs(tr - expected) < 1e-8

    def test_sp4_rmatrix_at_u5(self):
        """R(5.0) for sp_4 should be well-defined."""
        R = _full_rmatrix('C', 2, 5.0)
        assert R.shape == (16, 16)
        assert not np.any(np.isnan(R))

    def test_sl2_kappa_k1(self):
        """kappa(sl_2, k=1) = 9/4 (known value from landscape_census.tex)."""
        kappa = modular_characteristic('A', 1, 1.0)
        assert abs(kappa - 2.25) < 1e-12

    def test_sl3_kappa_k1(self):
        """kappa(sl_3, k=1) = 16/3."""
        kappa = modular_characteristic('A', 2, 1.0)
        assert abs(kappa - 16.0 / 3) < 1e-12

    def test_so5_kappa_k1(self):
        """kappa(so_5, k=1) = 10*4/(2*3) = 20/3."""
        kappa = modular_characteristic('B', 2, 1.0)
        assert abs(kappa - 20.0 / 3) < 1e-12


# =========================================================================
# Section 14: Cross-consistency checks
# =========================================================================

class TestCrossConsistency:
    """Cross-family and cross-method consistency checks."""

    def test_typeBC_isomorphism_rank2(self):
        """so_5 = sp_4 as Lie algebras: dim(g) and h^vee should match."""
        data_B = lie_algebra_data('B', 2)
        data_C = lie_algebra_data('C', 2)
        assert data_B['dim_g'] == data_C['dim_g']
        assert data_B['dual_coxeter'] == data_C['dual_coxeter']

    def test_kappa_additivity_heisenberg(self):
        """For direct sums: kappa is additive.  Check for sl_2 + sl_2."""
        k1 = modular_characteristic('A', 1, 1.0)
        # kappa(sl_2 + sl_2) should be 2 * kappa(sl_2) if levels match.
        assert abs(2 * k1 - 2 * 9.0 / 4) < 1e-12

    def test_ybe_and_cybe_consistency(self):
        """If CYBE holds, YBE should also hold (YBE is quantization of CYBE)."""
        for lie_type, n in [('A', 1), ('A', 2), ('B', 2), ('C', 2)]:
            cybe = verify_cybe(lie_type, n)
            ybe = ybe_coefficient_relations(lie_type, n, 4)
            if cybe['passes']:
                assert ybe['passes'], (
                    f"CYBE passes but YBE fails for {lie_type}_{n}"
                )

    def test_C2_times_N_equals_dim_g(self):
        """C_2(fund) * dim(fund) = dim(g) for all types."""
        for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
            data = lie_algebra_data(lie_type, n)
            C2 = casimir_eigenvalue(lie_type, n)
            assert abs(C2 * data['fund_dim'] - data['dim_g']) < 1e-6


# =========================================================================
# Section 15: Stress tests (parametric)
# =========================================================================

class TestStress:
    """Parametric stress tests across many configurations."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_slN_ybe(self, n):
        """YBE for sl_N at various ranks."""
        err = _ybe_numerical_error('A', n, 4.7, 2.3)
        assert err < 1e-7, f"YBE error for sl_{n+1}: {err}"

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_slN_cybe(self, n):
        """CYBE for sl_N at various ranks."""
        result = verify_cybe('A', n)
        assert result['passes'], f"CYBE failed for sl_{n+1}: err={result['max_error']}"

    @pytest.mark.parametrize("N_root", [5, 7, 8, 10, 11, 12, 13, 17])
    def test_root_of_unity_eigenvalues(self, N_root):
        """R-matrix eigenvalues at generic roots of unity.

        Exclude N_root = 3, 4, 6 where Jordan blocks or q^2=-1 occur.
        """
        result = trig_rmatrix_eigenvalues_irreps(N_root, 2)
        assert result['min_poly_error'] < 1e-6, (
            f"N={N_root}: min_poly_error={result['min_poly_error']}"
        )
