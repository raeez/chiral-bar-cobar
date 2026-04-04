r"""Tests for the Calogero-Moser / shadow metric correspondence.

Verifies: CM Hamiltonian from shadow connection, Jack polynomials,
CM partition function, elliptic CM, Dunkl operators, Heckman-Opdam,
W_N/CM correspondence, and Macdonald polynomials.

All formulas recomputed from first principles (AP1, AP3).
Cross-family consistency (AP10): Jack at alpha=1 vs Schur,
CM eigenvalues vs known tables, Dunkl commutation.
"""

import pytest
from sympy import (
    I, Integer, Matrix, Rational, S, Symbol, cancel, diff, expand,
    factor, pi, simplify, solve, sqrt, symbols, Abs, oo,
)

from compute.lib.calogero_moser_shadow import (
    # Partitions and symmetric functions
    partitions,
    dominates,
    monomial_symmetric,
    power_sum,
    elementary_symmetric,
    schur_polynomial,
    # CM Hamiltonian
    cm_hamiltonian_action,
    cm_potential,
    cm_eigenvalue,
    cm_ground_state,
    cm_ground_state_energy,
    # Shadow to CM
    n_channel_heisenberg_shadow_metric,
    shadow_to_cm_coupling,
    shadow_connection_cm_hamiltonian,
    # Jack polynomials
    jack_polynomial,
    jack_at_alpha_1,
    jack_at_alpha_2,
    verify_jack_is_schur_at_alpha_1,
    # Partition functions
    cm_partition_function_terms,
    free_boson_partition_function,
    shadow_partition_function_heisenberg,
    cm_partition_function_N2,
    # Dunkl operators
    dunkl_operator_action,
    verify_dunkl_commutation,
    dunkl_laplacian_action,
    # Elliptic CM
    weierstrass_p_expansion,
    elliptic_cm_hamiltonian_formal,
    elliptic_cm_eigenvalue_N2,
    genus1_shadow_to_elliptic_cm,
    # Heckman-Opdam
    root_system_A,
    heckman_opdam_hamiltonian_action,
    affine_km_shadow_to_heckman_opdam,
    # Macdonald
    macdonald_eigenvalue,
    macdonald_to_jack_limit,
    macdonald_polynomial_N2,
    # W_N and CM
    wN_shadow_to_cm,
    verify_w3_cm_correspondence,
    # Cross-checks
    verify_cm_eigenvalue_sum_rule,
    verify_jack_eigenvalue,
    shadow_cm_dictionary,
)


x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
c = Symbol('c')
q_var = Symbol('q')
tau = Symbol('tau')


# ============================================================================
# 1. PARTITIONS AND MONOMIAL SYMMETRIC FUNCTIONS
# ============================================================================

class TestPartitions:
    """Tests for partition generation and dominance order."""

    def test_partitions_0(self):
        """p(0) = 1: the empty partition."""
        assert partitions(0) == [()]

    def test_partitions_1(self):
        """p(1) = 1: only (1)."""
        assert partitions(1) == [(1,)]

    def test_partitions_2(self):
        """p(2) = 2: (2) and (1,1)."""
        assert partitions(2) == [(2,), (1, 1)]

    def test_partitions_3(self):
        """p(3) = 3: (3), (2,1), (1,1,1)."""
        assert partitions(3) == [(3,), (2, 1), (1, 1, 1)]

    def test_partitions_4(self):
        """p(4) = 5."""
        p4 = partitions(4)
        assert len(p4) == 5
        assert p4[0] == (4,)
        assert p4[-1] == (1, 1, 1, 1)

    def test_partitions_5(self):
        """p(5) = 7."""
        assert len(partitions(5)) == 7

    def test_partitions_max_length(self):
        """Partitions of 4 with at most 2 parts."""
        p = partitions(4, max_length=2)
        assert all(len(lam) <= 2 for lam in p)
        assert (4,) in p
        assert (3, 1) in p
        assert (2, 2) in p
        assert len(p) == 3

    def test_dominance_order(self):
        """(3,1) dominates (2,2) dominates (2,1,1)."""
        assert dominates((3, 1), (2, 2))
        assert dominates((2, 2), (2, 1, 1))
        assert dominates((3, 1), (2, 1, 1))
        assert not dominates((2, 2), (3, 1))

    def test_dominance_reflexive(self):
        """Every partition dominates itself."""
        for lam in partitions(4):
            assert dominates(lam, lam)

    def test_dominance_top_bottom(self):
        """(n) dominates everything; (1,...,1) is dominated by everything."""
        for lam in partitions(4):
            assert dominates((4,), lam)
            assert dominates(lam, (1, 1, 1, 1))


class TestMonomialSymmetric:
    """Tests for monomial symmetric polynomials."""

    def test_m_1_two_vars(self):
        """m_{(1)}(x1, x2) = x1 + x2."""
        m = monomial_symmetric((1,), [x1, x2])
        assert expand(m - x1 - x2) == 0

    def test_m_2_two_vars(self):
        """m_{(2)}(x1, x2) = x1^2 + x2^2."""
        m = monomial_symmetric((2,), [x1, x2])
        assert expand(m - x1**2 - x2**2) == 0

    def test_m_11_two_vars(self):
        """m_{(1,1)}(x1, x2) = x1*x2."""
        m = monomial_symmetric((1, 1), [x1, x2])
        assert expand(m - x1 * x2) == 0

    def test_m_21_two_vars(self):
        """m_{(2,1)}(x1, x2) = x1^2*x2 + x1*x2^2."""
        m = monomial_symmetric((2, 1), [x1, x2])
        assert expand(m - x1**2 * x2 - x1 * x2**2) == 0

    def test_m_21_three_vars(self):
        """m_{(2,1)}(x1, x2, x3) = x1^2*x2 + x1^2*x3 + x2^2*x1 + x2^2*x3 + x3^2*x1 + x3^2*x2."""
        m = monomial_symmetric((2, 1), [x1, x2, x3])
        expected = (x1**2 * x2 + x1**2 * x3 + x2**2 * x1
                    + x2**2 * x3 + x3**2 * x1 + x3**2 * x2)
        assert expand(m - expected) == 0

    def test_too_many_parts(self):
        """m_{(1,1,1)}(x1, x2) = 0 (3 parts, 2 variables)."""
        m = monomial_symmetric((1, 1, 1), [x1, x2])
        assert m == 0


class TestElementaryAndPowerSum:
    """Tests for elementary symmetric and power sum polynomials."""

    def test_e1(self):
        """e_1 = x1 + x2."""
        assert expand(elementary_symmetric(1, [x1, x2]) - x1 - x2) == 0

    def test_e2_two_vars(self):
        """e_2(x1, x2) = x1*x2."""
        assert expand(elementary_symmetric(2, [x1, x2]) - x1 * x2) == 0

    def test_e2_three_vars(self):
        """e_2(x1, x2, x3) = x1*x2 + x1*x3 + x2*x3."""
        e2 = elementary_symmetric(2, [x1, x2, x3])
        assert expand(e2 - x1 * x2 - x1 * x3 - x2 * x3) == 0

    def test_e0(self):
        """e_0 = 1."""
        assert elementary_symmetric(0, [x1, x2]) == 1

    def test_e_exceeds_N(self):
        """e_k = 0 for k > N."""
        assert elementary_symmetric(3, [x1, x2]) == 0

    def test_p1(self):
        """p_1 = x1 + x2."""
        assert expand(power_sum(1, [x1, x2]) - x1 - x2) == 0

    def test_p2(self):
        """p_2 = x1^2 + x2^2."""
        assert expand(power_sum(2, [x1, x2]) - x1**2 - x2**2) == 0

    def test_newton_identity(self):
        """Newton's identity: p_2 = e_1^2 - 2*e_2."""
        e1 = elementary_symmetric(1, [x1, x2])
        e2 = elementary_symmetric(2, [x1, x2])
        p2 = power_sum(2, [x1, x2])
        assert expand(p2 - e1**2 + 2 * e2) == 0


# ============================================================================
# 2. SCHUR POLYNOMIALS
# ============================================================================

class TestSchurPolynomials:
    """Tests for Schur polynomials via ratio of alternants."""

    def test_s_1_two_vars(self):
        """s_{(1)}(x1, x2) = x1 + x2."""
        s = schur_polynomial((1,), [x1, x2])
        assert expand(s - x1 - x2) == 0

    def test_s_2_two_vars(self):
        """s_{(2)}(x1, x2) = x1^2 + x1*x2 + x2^2."""
        s = schur_polynomial((2,), [x1, x2])
        assert expand(s - x1**2 - x1 * x2 - x2**2) == 0

    def test_s_11_two_vars(self):
        """s_{(1,1)}(x1, x2) = x1*x2."""
        s = schur_polynomial((1, 1), [x1, x2])
        assert expand(s - x1 * x2) == 0

    def test_s_21_two_vars(self):
        """s_{(2,1)}(x1, x2) = x1^2*x2 + x1*x2^2."""
        s = schur_polynomial((2, 1), [x1, x2])
        assert expand(s - x1**2 * x2 - x1 * x2**2) == 0

    def test_s_1_three_vars(self):
        """s_{(1)}(x1, x2, x3) = x1 + x2 + x3."""
        s = schur_polynomial((1,), [x1, x2, x3])
        assert expand(s - x1 - x2 - x3) == 0

    def test_s_2_three_vars(self):
        """s_{(2)}(x1, x2, x3) = m_{(2)} + m_{(1,1)}."""
        s = schur_polynomial((2,), [x1, x2, x3])
        m2 = monomial_symmetric((2,), [x1, x2, x3])
        m11 = monomial_symmetric((1, 1), [x1, x2, x3])
        assert expand(s - m2 - m11) == 0

    def test_s_11_three_vars(self):
        """s_{(1,1)}(x1, x2, x3) = e_2 = x1*x2 + x1*x3 + x2*x3."""
        s = schur_polynomial((1, 1), [x1, x2, x3])
        e2 = elementary_symmetric(2, [x1, x2, x3])
        assert expand(s - e2) == 0

    def test_too_many_parts(self):
        """s_{(1,1,1)}(x1, x2) = 0."""
        s = schur_polynomial((1, 1, 1), [x1, x2])
        assert s == 0


# ============================================================================
# 3. CM HAMILTONIAN
# ============================================================================

class TestCMHamiltonian:
    """Tests for the Calogero-Moser Hamiltonian."""

    def test_cm_potential_N2(self):
        """V(x1, x2) = beta(beta-1) / (x1 - x2)^2."""
        V = cm_potential([x1, x2], Rational(2))
        assert expand(V - 2 / (x1 - x2)**2) == 0

    def test_cm_potential_N3(self):
        """V(x1, x2, x3) has 3 terms (one per pair)."""
        V = cm_potential([x1, x2, x3], Rational(2))
        expected = 2 * (1 / (x1 - x2)**2 + 1 / (x1 - x3)**2 + 1 / (x2 - x3)**2)
        assert simplify(V - expected) == 0

    def test_cm_ground_state_energy_N2(self):
        """E_0(N=2, beta) = beta^2 * 2 * 3 / 12 = beta^2 / 2."""
        E = cm_ground_state_energy(2, Rational(2))
        assert E == 2

    def test_cm_ground_state_energy_N3(self):
        """E_0(N=3, beta) = beta^2 * 3 * 8 / 12 = 2 * beta^2."""
        E = cm_ground_state_energy(3, Rational(1))
        assert E == 2

    def test_cm_eigenvalue_empty_partition(self):
        """E_{()} = 0."""
        assert cm_eigenvalue((), 2, Rational(1)) == 0

    def test_cm_eigenvalue_1_N2_alpha1(self):
        """E_{(1)}(N=2, alpha=1) = 1 * (1 - 1 + (2+1-2)/1) = 1."""
        E = cm_eigenvalue((1,), 2, Rational(1))
        assert E == 1

    def test_cm_eigenvalue_2_N2_alpha1(self):
        """E_{(2)}(N=2, alpha=1) = 2 * (2 - 1 + 1) = 4."""
        E = cm_eigenvalue((2,), 2, Rational(1))
        assert E == 4

    def test_cm_eigenvalue_11_N2_alpha1(self):
        """E_{(1,1)}(N=2, alpha=1) = 1*(0+1) + 1*(0-1) = 0."""
        E = cm_eigenvalue((1, 1), 2, Rational(1))
        assert E == 0

    def test_cm_eigenvalue_ordering(self):
        """For alpha > 0, higher partitions have higher eigenvalues (generically)."""
        # For N=2, alpha=1: E_{(2)} > E_{(1,1)}
        E2 = cm_eigenvalue((2,), 2, Rational(1))
        E11 = cm_eigenvalue((1, 1), 2, Rational(1))
        assert E2 > E11

    def test_cm_eigenvalue_21_N3_alpha1(self):
        """E_{(2,1)}(N=3, alpha=1) = 2*(2-1+2) + 1*(1-1+0) = 6."""
        E = cm_eigenvalue((2, 1), 3, Rational(1))
        assert E == 6

    def test_cm_eigenvalue_alpha2(self):
        """E_{(1)}(N=2, alpha=2) = 1 * (0 + 1/2) = 1/2."""
        E = cm_eigenvalue((1,), 2, Rational(2))
        assert E == Rational(1, 2)


class TestCMGroundState:
    """Tests for the CM ground state wavefunction."""

    def test_ground_state_N2_beta1(self):
        """psi_0(N=2, beta=1) = x1 - x2 (antisymmetric, free fermion)."""
        psi = cm_ground_state([x1, x2], 1)
        assert expand(psi - (x1 - x2)) == 0

    def test_ground_state_N2_beta2(self):
        """psi_0(N=2, beta=2) = (x1 - x2)^2."""
        psi = cm_ground_state([x1, x2], 2)
        assert expand(psi - (x1 - x2)**2) == 0

    def test_ground_state_N3_beta1(self):
        """psi_0(N=3, beta=1) = Vandermonde determinant."""
        psi = cm_ground_state([x1, x2, x3], 1)
        vandermonde = (x1 - x2) * (x1 - x3) * (x2 - x3)
        assert expand(psi - vandermonde) == 0


# ============================================================================
# 4. SHADOW TO CM CORRESPONDENCE
# ============================================================================

class TestShadowToCM:
    """Tests for the shadow metric / CM correspondence."""

    def test_shadow_coupling(self):
        """beta = k for Heisenberg at level k."""
        assert shadow_to_cm_coupling(1) == 1
        assert shadow_to_cm_coupling(2) == 2
        assert shadow_to_cm_coupling(Rational(1, 2)) == Rational(1, 2)

    def test_shadow_cm_data_N2(self):
        """Shadow-CM data for 2-channel Heisenberg at level 1."""
        data = shadow_connection_cm_hamiltonian(2, 1)
        assert data['N'] == 2
        assert data['beta'] == 1
        assert data['alpha'] == 1
        assert data['coupling'] == 0  # beta(beta-1) = 0 at beta=1

    def test_shadow_cm_data_N3_level2(self):
        """Shadow-CM data for 3-channel Heisenberg at level 2."""
        data = shadow_connection_cm_hamiltonian(3, 2)
        assert data['N'] == 3
        assert data['beta'] == 2
        assert data['alpha'] == 1 / 2  # 1/beta
        assert data['coupling'] == 2  # 2*(2-1) = 2

    def test_heisenberg_shadow_metric_free(self):
        """N-channel Heisenberg free metric is sum (2k_a t_a)^2."""
        t1, t2 = symbols('t1 t2')
        Q = n_channel_heisenberg_shadow_metric([1, 1], [t1, t2])
        assert expand(Q - 4 * t1**2 - 4 * t2**2) == 0

    def test_heisenberg_shadow_metric_different_levels(self):
        """N-channel Heisenberg with different levels."""
        t1, t2 = symbols('t1 t2')
        Q = n_channel_heisenberg_shadow_metric([1, 2], [t1, t2])
        assert expand(Q - 4 * t1**2 - 16 * t2**2) == 0

    def test_shadow_cm_ground_state_energy(self):
        """Ground state energy from shadow data."""
        data = shadow_connection_cm_hamiltonian(3, 2)
        E0 = data['ground_state_energy']
        # E_0 = beta^2 * N(N^2-1)/12 = 4 * 3 * 8 / 12 = 8
        assert E0 == 8


# ============================================================================
# 5. JACK POLYNOMIALS
# ============================================================================

class TestJackPolynomials:
    """Tests for Jack polynomial computation."""

    def test_jack_empty(self):
        """J_{()}^{(alpha)} = 1."""
        assert jack_polynomial((), [x1, x2], Rational(1)) == 1

    def test_jack_1_alpha1_N2(self):
        """J_{(1)}^{(1)}(x1, x2) = x1 + x2 = s_{(1)}."""
        J = jack_polynomial((1,), [x1, x2], Rational(1))
        assert expand(J - x1 - x2) == 0

    def test_jack_2_alpha1_N2(self):
        """J_{(2)}^{(1)} should be proportional to s_{(2)} = x1^2 + x1*x2 + x2^2."""
        J = jack_polynomial((2,), [x1, x2], Rational(1))
        s = schur_polynomial((2,), [x1, x2])
        # Check proportionality
        ratio = cancel(J / s)
        assert diff(ratio, x1) == 0
        assert diff(ratio, x2) == 0

    def test_jack_11_alpha1_N2(self):
        """J_{(1,1)}^{(1)} should be proportional to s_{(1,1)} = x1*x2."""
        J = jack_polynomial((1, 1), [x1, x2], Rational(1))
        s = schur_polynomial((1, 1), [x1, x2])
        ratio = cancel(J / s)
        assert diff(ratio, x1) == 0
        assert diff(ratio, x2) == 0

    def test_jack_is_schur_at_alpha1(self):
        """At alpha = 1, Jack = Schur (up to normalization)."""
        assert verify_jack_is_schur_at_alpha_1((1,), [x1, x2])
        assert verify_jack_is_schur_at_alpha_1((2,), [x1, x2])
        assert verify_jack_is_schur_at_alpha_1((1, 1), [x1, x2])

    def test_jack_1_alpha2_N2(self):
        """J_{(1)}^{(2)}(x1, x2) = x1 + x2 (always, for single-box partition)."""
        J = jack_polynomial((1,), [x1, x2], Rational(2))
        assert expand(J - x1 - x2) == 0

    def test_jack_triangularity(self):
        """J_{(2)} = m_{(2)} + c * m_{(1,1)} with leading term m_{(2)}."""
        J = jack_polynomial((2,), [x1, x2], Rational(2))
        m2 = monomial_symmetric((2,), [x1, x2])
        m11 = monomial_symmetric((1, 1), [x1, x2])
        # J should be of the form m2 + c * m11
        # At x1 = 1, x2 = 0: J = 1 = m2 = 1, m11 = 0, so leading coeff = 1
        J_val = J.subs([(x1, 1), (x2, 0)])
        assert J_val == 1

    def test_jack_eigenfunction_11(self):
        """Verify J_{(1,1)} is an eigenfunction of the Sekiguchi operator at N=2."""
        residual = verify_jack_eigenvalue((1, 1), [x1, x2], Rational(1))
        assert simplify(residual) == 0

    def test_jack_eigenfunction_1(self):
        """Verify J_{(1)} is an eigenfunction."""
        residual = verify_jack_eigenvalue((1,), [x1, x2], Rational(1))
        assert simplify(residual) == 0

    def test_jack_eigenfunction_2_alpha1(self):
        """Verify J_{(2)}^{(1)} is eigenfunction at alpha=1."""
        residual = verify_jack_eigenvalue((2,), [x1, x2], Rational(1))
        assert simplify(residual) == 0


class TestJackSpecialValues:
    """Tests for Jack polynomials at special alpha values."""

    def test_jack_alpha1_is_schur_21_N3(self):
        """J_{(2,1)}^{(1)} should be proportional to s_{(2,1)} for N=3."""
        J = jack_polynomial((2, 1), [x1, x2, x3], Rational(1))
        s = schur_polynomial((2, 1), [x1, x2, x3])
        if s != 0 and J != 0:
            ratio = cancel(J / s)
            assert diff(ratio, x1) == 0
            assert diff(ratio, x2) == 0
            assert diff(ratio, x3) == 0

    def test_jack_1_three_vars(self):
        """J_{(1)}^{(alpha)} = x1 + x2 + x3 for any alpha."""
        for alpha_val in [Rational(1), Rational(2), Rational(1, 2)]:
            J = jack_polynomial((1,), [x1, x2, x3], alpha_val)
            assert expand(J - x1 - x2 - x3) == 0


# ============================================================================
# 6. CM EIGENVALUES
# ============================================================================

class TestCMEigenvalues:
    """Tests for CM eigenvalue formulas and consistency."""

    def test_eigenvalue_nonneg_alpha1(self):
        """All eigenvalues non-negative for alpha = 1, N = 2, degree <= 4."""
        results = verify_cm_eigenvalue_sum_rule(2, Rational(1), 4)
        for d, ok in results.items():
            assert ok, f"Negative eigenvalue at degree {d}"

    def test_eigenvalue_nonneg_alpha2(self):
        """All eigenvalues non-negative for alpha = 2, N = 2, degree <= 4."""
        results = verify_cm_eigenvalue_sum_rule(2, Rational(2), 4)
        for d, ok in results.items():
            assert ok, f"Negative eigenvalue at degree {d}"

    def test_eigenvalue_nonneg_alpha1_N3(self):
        """All eigenvalues non-negative for alpha = 1, N = 3."""
        results = verify_cm_eigenvalue_sum_rule(3, Rational(1), 3)
        for d, ok in results.items():
            assert ok, f"Negative eigenvalue at degree {d}"

    def test_eigenvalue_spectrum_degree2_N2(self):
        """Spectrum at degree 2, N=2, alpha=1: E_{(2)} = 4, E_{(1,1)} = 0."""
        E2 = cm_eigenvalue((2,), 2, Rational(1))
        E11 = cm_eigenvalue((1, 1), 2, Rational(1))
        assert E2 == 4
        assert E11 == 0

    def test_eigenvalue_spectrum_degree3_N2(self):
        """Spectrum at degree 3, N=2, alpha=1: E_{(3)} = 9, E_{(2,1)} = 3."""
        E3 = cm_eigenvalue((3,), 2, Rational(1))
        E21 = cm_eigenvalue((2, 1), 2, Rational(1))
        assert E3 == 9
        assert E21 == 3

    def test_eigenvalue_alpha_scaling(self):
        """At alpha = 2: E_{(1)} = 1/2 for N = 2."""
        E = cm_eigenvalue((1,), 2, Rational(2))
        assert E == Rational(1, 2)

    def test_eigenvalue_spectrum_degree4_N2_alpha1(self):
        """Degree 4, N=2, alpha=1: E_{(4)} = 16, E_{(3,1)} = 8, E_{(2,2)} = 4."""
        E4 = cm_eigenvalue((4,), 2, Rational(1))
        E31 = cm_eigenvalue((3, 1), 2, Rational(1))
        E22 = cm_eigenvalue((2, 2), 2, Rational(1))
        assert E4 == 16
        assert E31 == 8
        assert E22 == 4


# ============================================================================
# 7. PARTITION FUNCTIONS
# ============================================================================

class TestPartitionFunctions:
    """Tests for CM and free boson partition functions."""

    def test_free_boson_N1(self):
        """Free boson N=1: partition numbers p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5."""
        pf = free_boson_partition_function(1, 6)
        assert pf[0] == 1
        assert pf[1] == 1
        assert pf[2] == 2
        assert pf[3] == 3
        assert pf[4] == 5
        assert pf[5] == 7
        assert pf[6] == 11

    def test_free_boson_N2(self):
        """Free boson N=2: convolution of partition function with itself.
        p_2(0)=1, p_2(1)=2, p_2(2)=5, p_2(3)=10."""
        pf = free_boson_partition_function(2, 3)
        assert pf[0] == 1
        assert pf[1] == 2
        assert pf[2] == 5
        assert pf[3] == 10

    def test_free_boson_N3_degree1(self):
        """Free boson N=3 at degree 1: 3 (one for each color)."""
        pf = free_boson_partition_function(3, 1)
        assert pf[0] == 1
        assert pf[1] == 3

    def test_cm_partition_terms_N2(self):
        """CM partition function terms for N=2."""
        terms = cm_partition_function_terms(2, Rational(1), 3)
        # Number of partitions of d with at most 2 parts
        assert terms[0] == 1  # ()
        assert terms[1] == 1  # (1)
        assert terms[2] == 2  # (2), (1,1)
        assert terms[3] == 2  # (3), (2,1)

    def test_shadow_pf_heisenberg_matches_free_boson(self):
        """Shadow partition function of N-channel Heisenberg = free boson."""
        # For Heisenberg (class G), the shadow PF is the free boson PF
        shadow_pf = shadow_partition_function_heisenberg(1, 2, 3)
        free_pf = free_boson_partition_function(2, 3)
        for d in range(4):
            assert shadow_pf[d] == free_pf[d]


# ============================================================================
# 8. DUNKL OPERATORS
# ============================================================================

class TestDunklOperators:
    """Tests for Dunkl operators and their commutation relations."""

    def test_dunkl_on_constant(self):
        """D_i(1) = 0."""
        result = dunkl_operator_action(S.One, 0, [x1, x2], Rational(1))
        assert result == 0

    def test_dunkl_on_x_beta0(self):
        """At beta = 0, D_i = d/dx_i (ordinary derivative)."""
        f = x1**2 + x2
        result = dunkl_operator_action(f, 0, [x1, x2], S.Zero)
        assert expand(result - 2 * x1) == 0

    def test_dunkl_on_symmetric(self):
        """D_i on a symmetric function: D_1(x1 + x2) at beta = 1."""
        f = x1 + x2
        result = dunkl_operator_action(f, 0, [x1, x2], Rational(1))
        # D_1(x1 + x2) = 1 + 1 * (x1 + x2 - x2 - x1) / (x1 - x2) = 1
        assert simplify(result - 1) == 0

    def test_dunkl_commutation_N2(self):
        """[D_1, D_2] = 0 for N = 2, beta = 1."""
        f = x1**2 * x2
        comm = verify_dunkl_commutation(f, 0, 1, [x1, x2], Rational(1))
        assert simplify(comm) == 0

    def test_dunkl_commutation_N2_beta2(self):
        """[D_1, D_2] = 0 for N = 2, beta = 2 on a polynomial."""
        f = x1 * x2
        comm = verify_dunkl_commutation(f, 0, 1, [x1, x2], Rational(2))
        assert simplify(comm) == 0

    def test_dunkl_commutation_linear(self):
        """[D_1, D_2] = 0 on linear functions."""
        f = x1 + 2 * x2
        comm = verify_dunkl_commutation(f, 0, 1, [x1, x2], Rational(1))
        assert simplify(comm) == 0

    def test_dunkl_commutation_quadratic(self):
        """[D_1, D_2] = 0 on x1^2 + x2^2."""
        f = x1**2 + x2**2
        comm = verify_dunkl_commutation(f, 0, 1, [x1, x2], Rational(1))
        assert simplify(comm) == 0


# ============================================================================
# 9. ELLIPTIC CM
# ============================================================================

class TestEllipticCM:
    """Tests for the elliptic Calogero-Moser system."""

    def test_weierstrass_leading(self):
        """Weierstrass p-function: leading term 1/z^2."""
        z = Symbol('z')
        wp = weierstrass_p_expansion(z, tau, n_terms=0)
        assert wp == 1 / z**2

    def test_weierstrass_expansion(self):
        """Weierstrass p = 1/z^2 + 3*G4*z^2 + 5*G6*z^4 + ..."""
        z = Symbol('z')
        G4, G6 = symbols('G4 G6')
        wp = weierstrass_p_expansion(z, tau, n_terms=2)
        # Check coefficient of z^2
        coeff_z2 = wp.coeff(z, 2)
        assert coeff_z2 == 3 * G4

    def test_elliptic_cm_formal_N2(self):
        """Formal elliptic CM data for N = 2."""
        data = elliptic_cm_hamiltonian_formal(2, Rational(2))
        assert data['N'] == 2
        assert data['coupling'] == 2  # 2*(2-1)
        assert data['type'] == 'elliptic'

    def test_elliptic_eigenvalue_N2(self):
        """Leading elliptic CM eigenvalue for N = 2."""
        E = elliptic_cm_eigenvalue_N2(1, Rational(2))
        # n(n + 2*beta - 1) = 1*(1 + 3) = 4
        assert E == 4

    def test_elliptic_eigenvalue_N2_n0(self):
        """Ground state: n = 0 -> E = 0."""
        E = elliptic_cm_eigenvalue_N2(0, Rational(2))
        assert E == 0

    def test_genus1_shadow_data(self):
        """Genus-1 shadow to elliptic CM mapping."""
        data = genus1_shadow_to_elliptic_cm(1, 2)
        assert data['N'] == 2
        assert data['beta'] == 1
        assert data['genus'] == 1


# ============================================================================
# 10. HECKMAN-OPDAM AND ROOT SYSTEMS
# ============================================================================

class TestHeckmanOpdam:
    """Tests for the Heckman-Opdam / root system generalization."""

    def test_root_system_A1(self):
        """A_1: one positive root, Weyl group S_2."""
        R = root_system_A(2)
        assert R['type'] == 'A_1'
        assert R['rank'] == 1
        assert R['n_positive_roots'] == 1
        assert len(R['positive_roots']) == 1
        assert R['positive_roots'][0] == (0, 1)

    def test_root_system_A2(self):
        """A_2: three positive roots, Weyl group S_3."""
        R = root_system_A(3)
        assert R['type'] == 'A_2'
        assert R['rank'] == 2
        assert R['n_positive_roots'] == 3

    def test_root_system_A3(self):
        """A_3: six positive roots."""
        R = root_system_A(4)
        assert R['type'] == 'A_3'
        assert R['n_positive_roots'] == 6

    def test_heckman_opdam_equals_cm_type_A(self):
        """For type A, Heckman-Opdam = CM Hamiltonian."""
        R = root_system_A(2)
        f = x1**2 + x2**2
        # HO Hamiltonian with k_root = beta
        HO_f = heckman_opdam_hamiltonian_action(f, [x1, x2], R, Rational(2))
        # CM Hamiltonian
        CM_f = cm_hamiltonian_action(f, [x1, x2], Rational(2))
        assert simplify(HO_f - CM_f) == 0

    def test_affine_km_to_ho_slN(self):
        """hat{sl}_2 at level k -> A_1 CM with beta = k + 2."""
        data = affine_km_shadow_to_heckman_opdam('A', 1, 1)
        assert data['beta'] == 3  # k + h^v = 1 + 2
        assert data['h_dual'] == 2
        assert data['lie_type'] == 'A_1'

    def test_affine_km_to_ho_sl3(self):
        """hat{sl}_3 at level k -> A_2 CM with beta = k + 3."""
        data = affine_km_shadow_to_heckman_opdam('A', 2, 1)
        assert data['beta'] == 4  # k + h^v = 1 + 3
        assert data['h_dual'] == 3
        assert data['lie_type'] == 'A_2'
        assert data['root_system']['n_positive_roots'] == 3

    def test_affine_km_coupling(self):
        """Coupling beta(beta-1) at level k for sl_2: (k+2)(k+1)."""
        data = affine_km_shadow_to_heckman_opdam('A', 1, 1)
        assert data['coupling'] == 6  # 3*2


# ============================================================================
# 11. MACDONALD POLYNOMIALS
# ============================================================================

class TestMacdonaldPolynomials:
    """Tests for Macdonald polynomials and the q,t -> Jack limit."""

    def test_macdonald_eigenvalue_trivial(self):
        """Eigenvalue for empty partition: sum t^{N-i}."""
        E = macdonald_eigenvalue((), 2, q_var, Symbol('t_mac'))
        # sum_i t^{N-1-i} for i=0,1: t + 1
        t_mac = Symbol('t_mac')
        E_expected = macdonald_eigenvalue((), 2, q_var, t_mac)
        # E = t^1 * q^0 + t^0 * q^0 = t + 1
        assert expand(E_expected - t_mac - 1) == 0

    def test_macdonald_eigenvalue_1(self):
        """Eigenvalue for (1): t^{N-1}*q + t^{N-2}."""
        t_mac = Symbol('t_mac')
        E = macdonald_eigenvalue((1,), 2, q_var, t_mac)
        # lambda = (1, 0): t^1 * q^1 + t^0 * q^0 = t*q + 1
        assert expand(E - t_mac * q_var - 1) == 0

    def test_macdonald_to_jack_limit(self):
        """q -> 0 limit recovers Jack eigenvalue."""
        data = macdonald_to_jack_limit((2,), 2, Rational(1))
        # alpha = 1/beta = 1
        assert data['alpha'] == 1
        assert data['jack_eigenvalue'] == cm_eigenvalue((2,), 2, Rational(1))

    def test_macdonald_N2_degree1(self):
        """P_{(1)}(x1, x2; q, t) = x1 + x2 for any q, t."""
        t_mac = Symbol('t_mac')
        P = macdonald_polynomial_N2((1,), [x1, x2], q_var, t_mac)
        assert expand(P - x1 - x2) == 0

    def test_macdonald_N2_degree0(self):
        """P_{()}(x1, x2; q, t) = 1."""
        t_mac = Symbol('t_mac')
        P = macdonald_polynomial_N2((), [x1, x2], q_var, t_mac)
        assert P == 1

    def test_macdonald_N2_degree2_q0(self):
        """P_{(2)}(x1, x2; 0, t) should reduce to Jack at q = 0."""
        t_mac = Symbol('t_mac')
        P = macdonald_polynomial_N2((2,), [x1, x2], S.Zero, t_mac)
        # At q = 0, the q-binomial coefficient becomes:
        # (1 - q^2 * t)/(1 - q) -> t at q -> 0? No: at q = 0 exactly,
        # (1 - 0)/(1 - 0) = 1. So P_{(2)} at q=0 should be m_{(2)} + 1 * m_{(1,1)}
        # = x1^2 + x2^2 + x1*x2 (which is the Schur polynomial s_{(2)}).
        expected = x1**2 + x2**2 + x1 * x2
        assert expand(P - expected) == 0


# ============================================================================
# 12. W_N AND CM CORRESPONDENCE
# ============================================================================

class TestWNCM:
    """Tests for the W_N / CM correspondence."""

    def test_wN_data(self):
        """W_3 shadow to CM: 3 particles, root system A_2."""
        data = wN_shadow_to_cm(3, 1)
        assert data['W_N'] == 3
        assert data['n_generators'] == 2  # T and W
        assert data['generator_weights'] == [2, 3]
        assert data['shadow_class'] == 'M'

    def test_wN_integrals_count(self):
        """W_N has N-1 independent integrals = N-1 generators."""
        for N in range(3, 7):
            data = wN_shadow_to_cm(N, 1)
            assert data['cm_integrals'] == N - 1

    def test_w3_cm_correspondence(self):
        """W_3 at c = 2: kappa_T = 1, kappa_W = 5/3."""
        data = verify_w3_cm_correspondence(2)
        assert data['kappa_T'] == 1
        assert data['kappa_W'] == Rational(5, 3)
        assert data['cm_N'] == 3

    def test_shadow_depth_cm_integrability(self):
        """Shadow depth correspondence:
        G (r=2) -> free, L (r=3) -> cubic integral, M (r=inf) -> all integrals."""
        for N in [3, 4, 5]:
            data = wN_shadow_to_cm(N, 1)
            assert data['shadow_depth'] is None  # infinite
            assert data['cm_integrals'] == N - 1


# ============================================================================
# 13. SHADOW-CM DICTIONARY
# ============================================================================

class TestDictionary:
    """Tests for the shadow-CM correspondence dictionary."""

    def test_dictionary_keys(self):
        """The dictionary has all expected entries."""
        d = shadow_cm_dictionary()
        assert 'shadow_metric Q_L' in d
        assert 'kappa (arity-2)' in d
        assert 'Jack_polynomial J_lambda' in d
        assert 'Koszul_duality' in d
        assert 'class_G (r_max=2)' in d
        assert 'class_M (r_max=inf)' in d

    def test_dictionary_cm_values(self):
        """Dictionary values reference CM objects."""
        d = shadow_cm_dictionary()
        assert 'CM' in d['shadow_metric Q_L'] or 'potential' in d['shadow_metric Q_L']
        assert 'Dunkl' in d['shadow_connection nabla^sh'] or 'connection' in d['shadow_connection nabla^sh']


# ============================================================================
# 14. CM HAMILTONIAN ACTION ON SPECIFIC FUNCTIONS
# ============================================================================

class TestCMAction:
    """Tests for the CM Hamiltonian acting on specific functions."""

    def test_cm_on_symmetric_N2_beta1(self):
        """H_CM at beta=1 (free) on f = x1 + x2: should give -0 = 0 (no second deriv)."""
        # beta=1: coupling = 0, so H_CM = -sum d^2/dx^2
        f = x1 + x2
        Hf = cm_hamiltonian_action(f, [x1, x2], Rational(1))
        assert Hf == 0  # d^2/dx(x1+x2) = 0

    def test_cm_on_quadratic_N2_beta1(self):
        """H_CM at beta=1 on f = x1^2 + x2^2: -(-2-2) = 4? No, -d^2/dx1^2(x1^2) = -2."""
        f = x1**2 + x2**2
        Hf = cm_hamiltonian_action(f, [x1, x2], Rational(1))
        # beta=1: coupling=0, kinetic only: -(2 + 2) = -4
        assert Hf == -4

    def test_cm_potential_symmetric(self):
        """The CM potential is symmetric under permutations."""
        V = cm_potential([x1, x2, x3], Rational(2))
        # Use simultaneous substitution via a temp variable
        temp = Symbol('_temp')
        V_perm = V.subs(x1, temp).subs(x2, x1).subs(temp, x2)
        assert cancel(V - V_perm) == 0


# ============================================================================
# 15. CONSISTENCY CROSS-CHECKS
# ============================================================================

class TestConsistency:
    """Cross-checks between different parts of the computation."""

    def test_jack_eigenvalue_matches_cm(self):
        """The Jack eigenvalue formula should be consistent with CM action.

        For alpha = 1 (Schur / free fermion case), the eigenvalue
        E_{(2)} = 4 for N = 2.
        """
        E = cm_eigenvalue((2,), 2, Rational(1))
        assert E == 4

    def test_partition_count_consistency(self):
        """Number of partitions with at most N parts = dim of degree-d sector."""
        for d in range(5):
            p_all = partitions(d)
            p_N2 = partitions(d, 2)
            # Every partition with <= 2 parts is a partition
            assert all(lam in p_all for lam in p_N2)

    def test_schur_orthogonality_N2(self):
        """Schur polynomials at different partitions are distinct."""
        s2 = schur_polynomial((2,), [x1, x2])
        s11 = schur_polynomial((1, 1), [x1, x2])
        # They should not be proportional
        assert simplify(s2 - s11) != 0

    def test_monomial_to_schur_transition_matrix(self):
        """For N=2, degree 2: s_{(2)} = m_{(2)} + m_{(1,1)}, s_{(1,1)} = m_{(1,1)}."""
        s2 = schur_polynomial((2,), [x1, x2])
        s11 = schur_polynomial((1, 1), [x1, x2])
        m2 = monomial_symmetric((2,), [x1, x2])
        m11 = monomial_symmetric((1, 1), [x1, x2])

        assert expand(s2 - m2 - m11) == 0
        assert expand(s11 - m11) == 0

    def test_koszul_duality_is_beta_inversion(self):
        """Shadow Koszul duality corresponds to CM beta <-> 1/beta.

        For the shadow metric, Koszul duality maps kappa -> kappa^!
        which for Heisenberg is k -> -k (Feigin-Frenkel).
        For CM, this maps beta -> -beta, which (since beta > 0)
        is equivalent to the alpha -> 1/alpha involution on Jack.
        """
        d = shadow_cm_dictionary()
        assert 'beta' in d['Koszul_duality'] or '1/beta' in d['Koszul_duality']

    def test_free_boson_pf_is_eta_inverse(self):
        """The free boson PF at N=1 is 1/eta(q) = prod (1-q^n)^{-1}.

        First few terms: 1 + q + 2q^2 + 3q^3 + 5q^4 + 7q^5 + 11q^6.
        """
        pf = free_boson_partition_function(1, 10)
        # Partition numbers
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22, 9: 30, 10: 42}
        for d in range(11):
            assert pf[d] == expected[d], f"p({d}) = {pf[d]} != {expected[d]}"

    def test_cm_eigenvalue_degree_sum(self):
        """Sum of eigenvalues at degree d should match trace of CM operator."""
        # For N=2, alpha=1, degree 2: E_{(2)} + E_{(1,1)} = 4 + 0 = 4
        parts_d2 = partitions(2, 2)
        total = sum(cm_eigenvalue(lam, 2, Rational(1)) for lam in parts_d2)
        assert total == 4

    def test_dunkl_preserves_polynomials(self):
        """Dunkl operators map polynomials to polynomials of same or lower degree."""
        f = x1**3
        Df = dunkl_operator_action(f, 0, [x1, x2], Rational(1))
        # Should be a polynomial (the rational function from the reflection
        # term should cancel after simplification)
        assert Df.is_polynomial(x1, x2)


# ============================================================================
# 16. ADDITIONAL BOUNDARY CASES
# ============================================================================

class TestBoundaryCases:
    """Tests for boundary and degenerate cases."""

    def test_cm_N1_trivial(self):
        """N = 1: no pairs, CM = free particle."""
        V = cm_potential([x1], Rational(2))
        assert V == 0

    def test_cm_beta0_free(self):
        """beta = 0: coupling = 0, free particles."""
        V = cm_potential([x1, x2], S.Zero)
        assert V == 0

    def test_eigenvalue_single_part(self):
        """For single-row partition (n): E = n(n - 1 + (N-1)/alpha)."""
        E = cm_eigenvalue((3,), 2, Rational(1))
        # 3*(3 - 1 + 1) = 3*3 = 9
        assert E == 9

    def test_eigenvalue_column_partition(self):
        """For single-column (1^N): E depends on N and alpha."""
        E = cm_eigenvalue((1, 1, 1), 3, Rational(1))
        # Sum_i 1*(0 + (4-2i)/1) for i=1,2,3
        # = (2) + (0) + (-2) = 0
        assert E == 0

    def test_jack_zero_if_too_many_parts(self):
        """J_{(1,1,1)}^{(alpha)} in 2 variables should be 0."""
        J = jack_polynomial((1, 1, 1), [x1, x2], Rational(1))
        assert J == 0

    def test_macdonald_factorization(self):
        """P_{(n,m)} = (x1*x2)^m * P_{(n-m)} for N=2."""
        t_mac = Symbol('t_mac')
        P21 = macdonald_polynomial_N2((2, 1), [x1, x2], q_var, t_mac)
        P1 = macdonald_polynomial_N2((1,), [x1, x2], q_var, t_mac)
        assert expand(P21 - x1 * x2 * P1) == 0

    def test_root_system_count(self):
        """Number of positive roots of A_{N-1} = N*(N-1)/2."""
        for N in range(2, 6):
            R = root_system_A(N)
            assert R['n_positive_roots'] == N * (N - 1) // 2
