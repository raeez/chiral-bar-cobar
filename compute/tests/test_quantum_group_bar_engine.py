r"""Tests for explicit U_q(g) construction from the bar complex.

Multi-path verification structure:
  Path 1: Direct algebraic computation (DJ relations, Hopf axioms)
  Path 2: Representation-theoretic checks (highest-weight, tensor products, characters)
  Path 3: R-matrix/YBE verification (QYBE, quasi-triangularity)
  Path 4: Equivalence of presentations (DJ <-> RTT <-> FRT)
  Path 5: Roots of unity and admissible levels (truncation, KL correspondence)
  Path 6: Yangian degeneration (q -> 1 limit)
  Path 7: Cross-checks with manuscript formulas (kappa, DK bridge)

Organization:
  1.  q-arithmetic (3 tests)
  2.  Lie algebra data (3 tests)
  3.  Quantum parameter from level (3 tests)
  4.  U_q(sl_2) DJ relations — multiple representations (5 tests)
  5.  U_q(sl_3) DJ + Serre relations (4 tests)
  6.  Hopf algebra structure (6 tests)
  7.  RTT presentation (4 tests)
  8.  FRT presentation and quantum determinant (4 tests)
  9.  Three-presentation equivalence (2 tests)
  10. Highest-weight modules (5 tests)
  11. Tensor product decomposition (4 tests)
  12. Universal R-matrix and QYBE (4 tests)
  13. Roots of unity truncation (5 tests)
  14. Yangian degeneration (4 tests)
  15. Kappa and modular characteristic (4 tests)
  16. Cross-engine consistency (5 tests)

Total: 65 tests.

References:
  thm:mc2-bar-intrinsic, thm:collision-residue-twisting,
  thm:e1-duality-main, AP19 (pole absorption), AP27 (propagator weight),
  AP33 (Koszul != FF != negative-level),
  Jimbo 1985, Drinfeld 1986, FRT 1990, Kassel 1995.
"""

import cmath
import math

import numpy as np
import pytest

from compute.lib.quantum_group_bar_engine import (
    # q-arithmetic
    q_number,
    q_factorial,
    q_binomial,
    # Lie algebra data
    sl2_data,
    sl3_data,
    slN_data,
    LieAlgebraData,
    # Quantum parameter
    quantum_parameter,
    level_from_q,
    # U_q(sl_2) generators
    uq_sl2_generators,
    verify_dj_relations_sl2,
    UqSl2Generators,
    # U_q(sl_3) generators
    uq_sl3_generators,
    verify_dj_relations_sl3,
    # Hopf algebra
    coproduct_sl2,
    antipode_sl2,
    counit_sl2,
    verify_hopf_axioms_sl2,
    HopfAlgebraStructure,
    # RTT
    jimbo_r_matrix_slN,
    rtt_t_matrix_slN,
    verify_rtt_relation,
    permutation_matrix,
    # FRT
    frt_quantum_determinant_sl2,
    frt_commutation_relations_sl2,
    # Three presentations
    verify_three_presentations_sl2,
    # Highest-weight modules
    highest_weight_module_sl2,
    tensor_product_decomposition_sl2,
    # Universal R-matrix
    universal_r_matrix_sl2,
    verify_universal_r_qybe,
    hbar_expansion_r_matrix,
    # Roots of unity
    root_of_unity_truncation,
    verify_nilpotency_at_root,
    # Yangian
    yangian_from_quantum_group,
    yangian_generators_from_t_matrix,
    # Casimir and dimensions
    quantum_casimir_sl2,
    quantum_dimension_sl2,
    kappa_from_quantum_group,
    # Comprehensive
    comprehensive_uq_sl2_verification,
    comprehensive_uq_sl3_verification,
)


# =========================================================================
# 1. q-arithmetic (3 tests)
# =========================================================================

class TestQArithmetic:
    """Tests for q-number, q-factorial, q-binomial."""

    def test_q_number_classical_limit(self):
        """[n]_q -> n as q -> 1.  Classical limit check."""
        q = 1.0 + 1e-12
        for n in range(1, 8):
            assert abs(q_number(n, q) - n) < 1e-6, f"[{n}]_q != {n} at q=1"

    def test_q_factorial_values(self):
        """[n]_q! matches product formula at generic q."""
        q = cmath.exp(0.3j)
        assert abs(q_factorial(0, q) - 1.0) < 1e-12
        assert abs(q_factorial(1, q) - q_number(1, q)) < 1e-12
        f3 = q_number(1, q) * q_number(2, q) * q_number(3, q)
        assert abs(q_factorial(3, q) - f3) < 1e-10

    def test_q_binomial_pascal(self):
        """q-binomial satisfies q-Pascal identity: [n,k] = q^k [n-1,k] + q^{-(n-k)} [n-1,k-1]."""
        q = cmath.exp(0.5j)
        for n in range(2, 6):
            for k in range(1, n):
                lhs = q_binomial(n, k, q)
                rhs = q ** k * q_binomial(n - 1, k, q) + q ** (-(n - k)) * q_binomial(n - 1, k - 1, q)
                assert abs(lhs - rhs) < 1e-10, f"q-Pascal fails at n={n}, k={k}"


# =========================================================================
# 2. Lie algebra data (3 tests)
# =========================================================================

class TestLieAlgebraData:
    """Tests for Lie algebra data structures."""

    def test_sl2_data(self):
        """sl_2 has rank 1, dim 3, h^vee = 2."""
        d = sl2_data()
        assert d.rank == 1
        assert d.dim == 3
        assert d.h_dual == 2
        assert d.dim_fundamental == 2
        assert len(d.positive_roots) == 1

    def test_sl3_data(self):
        """sl_3 has rank 2, dim 8, h^vee = 3."""
        d = sl3_data()
        assert d.rank == 2
        assert d.dim == 8
        assert d.h_dual == 3
        assert d.dim_fundamental == 3
        # Cartan matrix: [[2,-1],[-1,2]]
        assert d.cartan_matrix[0, 0] == 2
        assert d.cartan_matrix[0, 1] == -1
        assert len(d.positive_roots) == 3  # alpha_1, alpha_2, alpha_1+alpha_2

    def test_slN_consistency(self):
        """slN_data(N) gives dim = N^2 - 1 and h^vee = N."""
        for N in [2, 3, 4, 5]:
            d = slN_data(N)
            assert d.dim == N * N - 1
            assert d.h_dual == N
            assert d.rank == N - 1
            assert d.dim_fundamental == N
            # Number of positive roots = N(N-1)/2
            assert len(d.positive_roots) == N * (N - 1) // 2


# =========================================================================
# 3. Quantum parameter from level (3 tests)
# =========================================================================

class TestQuantumParameter:
    """Tests for q = exp(pi*i/(k + h^vee))."""

    def test_sl2_level1(self):
        """For sl_2 at level 1: q = exp(pi*i/3), a primitive 6th root of unity."""
        q = quantum_parameter(1.0, 2)
        expected = cmath.exp(1j * cmath.pi / 3)
        assert abs(q - expected) < 1e-14

    def test_level_recovery(self):
        """level_from_q is inverse of quantum_parameter."""
        for k in [1.0, 2.0, 5.0, 10.0]:
            for h in [2, 3, 4]:
                q = quantum_parameter(k, h)
                k_rec = level_from_q(q, h)
                assert abs(k_rec - k) < 1e-10, f"Level recovery failed: k={k}, h={h}"

    def test_root_of_unity_at_integer_level(self):
        """At integer level k, q^{2(k+h^vee)} = 1."""
        k = 3
        h = 2  # sl_2
        q = quantum_parameter(k, h)
        # q = exp(pi*i/(k+h)) = exp(pi*i/5)
        # q^{2*5} = exp(2*pi*i) = 1
        q_power = q ** (2 * (k + h))
        assert abs(q_power - 1.0) < 1e-12


# =========================================================================
# 4. U_q(sl_2) DJ relations — multiple representations (5 tests)
# =========================================================================

class TestDJRelationsSl2:
    """Test Drinfeld-Jimbo relations for U_q(sl_2)."""

    @pytest.fixture(params=[0.5, 1.0, 1.5, 2.0])
    def spin(self, request):
        return request.param

    def test_dj_generic_q(self, spin):
        """DJ relations hold at generic q for spin j representations."""
        q = cmath.exp(0.3 + 0.1j)  # generic q
        gen = uq_sl2_generators(q, spin)
        result = verify_dj_relations_sl2(gen)
        assert result["all_hold"], (
            f"DJ relations fail at spin {spin}: max errors "
            f"KEK={result['KEK_inv_error']:.2e}, "
            f"KFK={result['KFK_inv_error']:.2e}, "
            f"EF={result['EF_commutator_error']:.2e}"
        )

    def test_dj_level1_sl2(self):
        """DJ relations at level 1 (q = exp(pi*i/3))."""
        q = quantum_parameter(1.0, 2)
        gen = uq_sl2_generators(q, 0.5)
        result = verify_dj_relations_sl2(gen)
        assert result["all_hold"]


# =========================================================================
# 5. U_q(sl_3) DJ + Serre relations (4 tests)
# =========================================================================

class TestDJRelationsSl3:
    """Test Drinfeld-Jimbo and quantum Serre relations for U_q(sl_3)."""

    def test_dj_cartan_relations(self):
        """K_i E_j K_i^{-1} = q^{a_{ij}} E_j for all i,j."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_dj_relations_sl3(uq_sl3_generators(q))
        for i in range(2):
            for j in range(2):
                assert result[f"KEK_{i}{j}"] < 1e-10
                assert result[f"KFK_{i}{j}"] < 1e-10

    def test_dj_commutator_relations(self):
        """[E_i, F_j] = delta_{ij} (K_i - K_i^{-1})/(q - q^{-1})."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_dj_relations_sl3(uq_sl3_generators(q))
        for i in range(2):
            for j in range(2):
                assert result[f"EF_comm_{i}{j}"] < 1e-10

    def test_quantum_serre_relations(self):
        """Quantum Serre: E_i^2 E_j - (q+q^{-1}) E_i E_j E_i + E_j E_i^2 = 0."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_dj_relations_sl3(uq_sl3_generators(q))
        assert result["serre_E12"] < 1e-10
        assert result["serre_E21"] < 1e-10
        assert result["serre_F12"] < 1e-10
        assert result["serre_F21"] < 1e-10

    def test_all_sl3_relations(self):
        """All DJ + Serre relations hold simultaneously for sl_3."""
        q = quantum_parameter(2.0, 3)  # level 2 for sl_3
        result = verify_dj_relations_sl3(uq_sl3_generators(q))
        assert result["all_hold"], f"Max error: {result['max_error']:.2e}"


# =========================================================================
# 6. Hopf algebra structure (6 tests)
# =========================================================================

class TestHopfAlgebra:
    """Test Hopf algebra axioms from bar coalgebra structure."""

    @pytest.fixture
    def gen(self):
        q = cmath.exp(0.3 + 0.1j)
        return uq_sl2_generators(q, 0.5)

    def test_coassociativity_K(self, gen):
        """(Delta tensor id)(Delta(K)) = (id tensor Delta)(Delta(K))."""
        result = verify_hopf_axioms_sl2(gen)
        assert result["coassoc_K"] < 1e-10

    def test_coassociativity_E(self, gen):
        """(Delta tensor id)(Delta(E)) = (id tensor Delta)(Delta(E))."""
        result = verify_hopf_axioms_sl2(gen)
        assert result["coassoc_E"] < 1e-10

    def test_antipode_K(self, gen):
        """S(K) * K = I (antipode axiom for K)."""
        result = verify_hopf_axioms_sl2(gen)
        assert result["antipode_K"] < 1e-10

    def test_antipode_E(self, gen):
        """m(S tensor id)(Delta(E)) = 0 = eps(E) (antipode axiom for E)."""
        result = verify_hopf_axioms_sl2(gen)
        assert result["antipode_E"] < 1e-10

    def test_antipode_F(self, gen):
        """m(S tensor id)(Delta(F)) = 0 = eps(F) (antipode axiom for F)."""
        result = verify_hopf_axioms_sl2(gen)
        assert result["antipode_F"] < 1e-10

    def test_coproduct_algebra_homomorphism(self, gen):
        """Delta([E,F]) = [Delta(E), Delta(F)] (coproduct is algebra map)."""
        result = verify_hopf_axioms_sl2(gen)
        assert result["coprod_homomorphism"] < 1e-10


# =========================================================================
# 7. RTT presentation (4 tests)
# =========================================================================

class TestRTTPresentation:
    """Test RTT relation R T_1 T_2 = T_2 T_1 R."""

    def test_rtt_sl2_generic(self):
        """RTT relation holds for sl_2 at generic q."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_rtt_relation(q, 2)
        assert result["all_hold"], f"Max error: {result['max_error']:.2e}"

    def test_rtt_sl2_level1(self):
        """RTT relation holds for sl_2 at level 1."""
        q = quantum_parameter(1.0, 2)
        result = verify_rtt_relation(q, 2)
        assert result["all_hold"], f"Max error: {result['max_error']:.2e}"

    def test_rtt_sl3_generic(self):
        """RTT relation holds for sl_3 at generic q."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_rtt_relation(q, 3)
        assert result["all_hold"], f"Max error: {result['max_error']:.2e}"

    def test_rtt_sl3_level2(self):
        """RTT relation holds for sl_3 at level 2."""
        q = quantum_parameter(2.0, 3)
        result = verify_rtt_relation(q, 3)
        assert result["all_hold"], f"Max error: {result['max_error']:.2e}"


# =========================================================================
# 8. FRT presentation and quantum determinant (4 tests)
# =========================================================================

class TestFRTPresentation:
    """Test FRT commutation relations and quantum determinant."""

    def test_quantum_determinant_identity(self):
        """qdet(T) = I for U_q(sl_2) (quantum SL_2 condition)."""
        q = cmath.exp(0.3 + 0.1j)
        result = frt_quantum_determinant_sl2(q)
        assert result["qdet_is_identity"], f"qdet error: {result['qdet_error']:.2e}"

    def test_frt_commutation_ab(self):
        """FRT relation: ab = q * ba."""
        q = cmath.exp(0.3 + 0.1j)
        errors = frt_commutation_relations_sl2(q)
        assert errors["ab_qba"] < 1e-10

    def test_frt_commutation_bc(self):
        """FRT relation: bc = cb (B and C commute)."""
        q = cmath.exp(0.3 + 0.1j)
        errors = frt_commutation_relations_sl2(q)
        assert errors["bc_cb"] < 1e-10

    def test_frt_commutation_ad_da(self):
        """FRT relation: ad - da = (q - q^{-1}) bc."""
        q = cmath.exp(0.3 + 0.1j)
        errors = frt_commutation_relations_sl2(q)
        assert errors["ad_da"] < 1e-10


# =========================================================================
# 9. Three-presentation equivalence (2 tests)
# =========================================================================

class TestThreePresentations:
    """Test equivalence of DJ, RTT, and FRT presentations."""

    def test_three_presentations_generic_q(self):
        """All three presentations hold simultaneously at generic q."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_three_presentations_sl2(q)
        assert result["all_hold"]

    def test_three_presentations_level3(self):
        """All three presentations hold at level 3 for sl_2."""
        q = quantum_parameter(3.0, 2)
        result = verify_three_presentations_sl2(q)
        assert result["all_hold"]


# =========================================================================
# 10. Highest-weight modules (5 tests)
# =========================================================================

class TestHighestWeightModules:
    """Test highest-weight module structure."""

    def test_hw_vector_killed_by_E(self):
        """E|j,j> = 0: highest weight vector is killed by E."""
        q = cmath.exp(0.3 + 0.1j)
        for j in [0.5, 1.0, 1.5, 2.0]:
            result = highest_weight_module_sl2(q, j)
            assert result["E_kills_hw"] < 1e-10, f"E does not kill hw at j={j}"

    def test_hw_vector_K_eigenvalue(self):
        """K|j,j> = q^{2j} |j,j>: correct K eigenvalue on highest weight."""
        q = cmath.exp(0.3 + 0.1j)
        for j in [0.5, 1.0, 1.5]:
            result = highest_weight_module_sl2(q, j)
            assert result["K_eigenvalue_hw"] < 1e-10

    def test_F_generates_module(self):
        """F^n|j,j> spans V_j: F generates the entire module."""
        q = cmath.exp(0.3 + 0.1j)
        for j in [0.5, 1.0, 1.5, 2.0]:
            result = highest_weight_module_sl2(q, j)
            assert result["F_generates_all"], f"F does not generate V_{j}"

    def test_quantum_dimension(self):
        """tr(K) = [2j+1]_q: quantum dimension formula."""
        q = cmath.exp(0.3 + 0.1j)
        for j in [0.5, 1.0, 1.5, 2.0]:
            result = highest_weight_module_sl2(q, j)
            assert result["quantum_dim_error"] < 1e-10, f"Quantum dim error at j={j}"

    def test_casimir_eigenvalue(self):
        """Quantum Casimir acts as expected scalar on V_j."""
        q = cmath.exp(0.3 + 0.1j)
        for j in [0.5, 1.0, 1.5]:
            result = highest_weight_module_sl2(q, j)
            assert result["casimir_scalar_error"] < 1e-8, (
                f"Casimir error at j={j}: {result['casimir_scalar_error']:.2e}"
            )


# =========================================================================
# 11. Tensor product decomposition (4 tests)
# =========================================================================

class TestTensorProducts:
    """Test tensor product decomposition via Casimir spectrum."""

    def test_half_tensor_half(self):
        """V_{1/2} tensor V_{1/2} = V_0 + V_1 (CG decomposition)."""
        q = cmath.exp(0.3 + 0.1j)
        result = tensor_product_decomposition_sl2(q, 0.5, 0.5)
        assert result["decomposition_correct"], (
            f"Decomposition error: {result['eigenvalue_error']:.2e}"
        )
        assert result["n_irreps"] == 2  # V_0 and V_1

    def test_half_tensor_one(self):
        """V_{1/2} tensor V_1 = V_{1/2} + V_{3/2}."""
        q = cmath.exp(0.3 + 0.1j)
        result = tensor_product_decomposition_sl2(q, 0.5, 1.0)
        assert result["decomposition_correct"]
        assert result["n_irreps"] == 2

    def test_one_tensor_one(self):
        """V_1 tensor V_1 = V_0 + V_1 + V_2."""
        q = cmath.exp(0.3 + 0.1j)
        result = tensor_product_decomposition_sl2(q, 1.0, 1.0)
        assert result["decomposition_correct"]
        assert result["n_irreps"] == 3

    def test_tensor_dimensions_additive(self):
        """dim(V_{j1} tensor V_{j2}) = dim(V_{j1}) * dim(V_{j2})."""
        q = cmath.exp(0.3 + 0.1j)
        for j1, j2 in [(0.5, 0.5), (0.5, 1.0), (1.0, 1.0), (1.5, 0.5)]:
            result = tensor_product_decomposition_sl2(q, j1, j2)
            expected_dim = int(2 * j1 + 1) * int(2 * j2 + 1)
            assert result["dim_tensor"] == expected_dim


# =========================================================================
# 12. Universal R-matrix and QYBE (4 tests)
# =========================================================================

class TestUniversalRMatrix:
    """Test the universal R-matrix from the bar complex."""

    def test_qybe_fundamental(self):
        """Universal R-matrix satisfies QYBE on V_{1/2}^{tensor 3}."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_universal_r_qybe(q, 0.5)
        assert result["qybe_holds"], f"QYBE error: {result['qybe_error']:.2e}"

    def test_qybe_spin1(self):
        """Universal R-matrix satisfies QYBE on V_1^{tensor 3}."""
        q = cmath.exp(0.3 + 0.1j)
        result = verify_universal_r_qybe(q, 1.0)
        assert result["qybe_holds"], f"QYBE error: {result['qybe_error']:.2e}"

    def test_jimbo_r_matrix_sl2_qybe(self):
        """Jimbo R-matrix for sl_2 satisfies QYBE."""
        q = cmath.exp(0.3 + 0.1j)
        N = 2
        R = jimbo_r_matrix_slN(q, N)
        R12 = np.kron(R, np.eye(N, dtype=complex))
        R23 = np.kron(np.eye(N, dtype=complex), R)
        d3 = N ** 3
        R13 = np.zeros((d3, d3), dtype=complex)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    for ip in range(N):
                        for kp in range(N):
                            row = i * N * N + j * N + k
                            col = ip * N * N + j * N + kp
                            R13[row, col] += R[i * N + k, ip * N + kp]
        err = float(np.max(np.abs(R12 @ R13 @ R23 - R23 @ R13 @ R12)))
        assert err < 1e-10, f"QYBE error: {err:.2e}"

    def test_classical_limit_recovers_casimir(self):
        """At small hbar, (R - I)/hbar -> Casimir Omega = P - I/N."""
        N = 2
        hbar = 1e-5
        q = cmath.exp(hbar)
        R = jimbo_r_matrix_slN(q, N)
        I_d = np.eye(N * N, dtype=complex)
        r_class = (R - I_d) / hbar
        P = permutation_matrix(N)
        Omega = P - I_d / N
        err = float(np.max(np.abs(r_class - Omega)))
        assert err < 1e-3, f"Classical limit error: {err:.2e}"


# =========================================================================
# 13. Roots of unity truncation (5 tests)
# =========================================================================

class TestRootsOfUnity:
    """Test quantum group truncation at roots of unity."""

    def test_quantum_integer_vanishes(self):
        """[p]_q = 0 at q = exp(2*pi*i/p)."""
        for p in [3, 5, 7, 11]:
            result = root_of_unity_truncation(p)
            assert result["p_quantum_zero"], f"[{p}]_q != 0 at q^{p}=1"

    def test_type1_irrep_count(self):
        """Number of type-1 irreps is p-1."""
        for p in [3, 5, 7]:
            result = root_of_unity_truncation(p)
            assert result["n_type1_irreps"] == p - 1

    def test_kl_correspondence_level(self):
        """KL level: k = p - 2 for sl_2."""
        for p in [3, 4, 5, 6]:
            result = root_of_unity_truncation(p)
            assert result["kl_level"] == p - 2

    def test_nilpotency_E_p(self):
        """E^p = 0 on type-1 representations at root of unity."""
        for p in [3, 5, 7]:
            result = verify_nilpotency_at_root(p)
            for key, val in result.items():
                if key.startswith("E^"):
                    assert val < 1e-8, f"{key} not zero: {val:.2e}"

    def test_nilpotency_F_p(self):
        """F^p = 0 on type-1 representations at root of unity."""
        for p in [3, 5, 7]:
            result = verify_nilpotency_at_root(p)
            for key, val in result.items():
                if key.startswith("F^"):
                    assert val < 1e-8, f"{key} not zero: {val:.2e}"


# =========================================================================
# 14. Yangian degeneration (4 tests)
# =========================================================================

class TestYangianDegeneration:
    """Test Y(g) as rational degeneration q -> 1 of U_q(g)."""

    def test_classical_limit_sl2(self):
        """(R - I)/hbar -> Omega at small hbar for sl_2."""
        result = yangian_from_quantum_group(2, 0.001 + 0j)
        assert result["classical_limit_error"] < 0.01, (
            f"Classical limit error: {result['classical_limit_error']:.2e}"
        )

    def test_classical_limit_sl3(self):
        """(R - I)/hbar -> Omega at small hbar for sl_3."""
        result = yangian_from_quantum_group(3, 0.001 + 0j)
        assert result["classical_limit_error"] < 0.01

    def test_trigonometric_to_rational(self):
        """Trigonometric R / sin(eta) -> Yang R as eta -> 0."""
        result = yangian_from_quantum_group(2, 0.001 + 0j)
        if result["trig_to_rational_error"] is not None:
            assert result["trig_to_rational_error"] < 0.01

    def test_yangian_generator_count(self):
        """Y(sl_N) has N^2 - 1 generators per level."""
        for N in [2, 3, 4]:
            data = yangian_generators_from_t_matrix(N)
            assert data["dim_g"] == N * N - 1
            assert data["rank"] == N - 1


# =========================================================================
# 15. Kappa and modular characteristic (4 tests)
# =========================================================================

class TestKappaModularCharacteristic:
    """Test kappa from quantum group parameter (Theorem D, AP39)."""

    def test_kappa_sl2_level1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        q = quantum_parameter(1.0, 2)
        g = sl2_data()
        kappa = kappa_from_quantum_group(q, g)
        expected = 3 * 3 / 4.0  # dim=3, (k+h)/(2h) = 3/4
        assert abs(kappa - expected) < 1e-8

    def test_kappa_sl2_level2(self):
        """kappa(sl_2, k=2) = 3*4/4 = 3."""
        q = quantum_parameter(2.0, 2)
        g = sl2_data()
        kappa = kappa_from_quantum_group(q, g)
        assert abs(kappa - 3.0) < 1e-8

    def test_kappa_sl3_level1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        q = quantum_parameter(1.0, 3)
        g = sl3_data()
        kappa = kappa_from_quantum_group(q, g)
        expected = 8 * 4 / 6.0
        assert abs(kappa - expected) < 1e-8

    def test_kappa_formula_consistency(self):
        """kappa = dim(g) * (k + h^vee) / (2 * h^vee) for multiple families.

        Cross-check: kappa formula matches quantum parameter derivation (AP39).
        """
        for N in [2, 3, 4]:
            g = slN_data(N)
            for k in [1.0, 2.0, 3.0]:
                q = quantum_parameter(k, g.h_dual)
                kappa = kappa_from_quantum_group(q, g)
                expected = g.dim * (k + g.h_dual) / (2 * g.h_dual)
                assert abs(kappa - expected) < 1e-8, (
                    f"kappa mismatch for sl_{N} at k={k}: "
                    f"got {kappa}, expected {expected}"
                )


# =========================================================================
# 16. Cross-engine consistency (5 tests)
# =========================================================================

class TestCrossEngineConsistency:
    """Cross-checks with other compute engines."""

    def test_jimbo_r_matches_existing(self):
        """Jimbo R-matrix matches quantum_rmatrix_barcomplex engine."""
        try:
            from compute.lib.quantum_rmatrix_barcomplex import (
                uq_sl2_R_fundamental as existing_R_sl2,
            )
            q = cmath.exp(0.3 + 0.1j)
            R_new = jimbo_r_matrix_slN(q, 2)
            R_existing = existing_R_sl2(q)
            err = float(np.max(np.abs(R_new - R_existing)))
            assert err < 1e-10, f"R-matrix mismatch: {err:.2e}"
        except ImportError:
            pytest.skip("quantum_rmatrix_barcomplex not available")

    def test_quantum_dim_matches_root_of_unity_engine(self):
        """Quantum dimension matches quantum_group_root_of_unity_engine."""
        try:
            from compute.lib.quantum_group_root_of_unity_engine import (
                quantum_dimension as existing_qdim,
            )
            q = cmath.exp(0.3j)
            for n in range(1, 6):
                new_val = quantum_dimension_sl2(q, (n - 1) / 2.0)
                existing_val = existing_qdim(n, q)
                assert abs(new_val - existing_val) < 1e-10
        except ImportError:
            pytest.skip("quantum_group_root_of_unity_engine not available")

    def test_casimir_matches_root_of_unity_engine(self):
        """Quantum Casimir matches quantum_group_root_of_unity_engine."""
        try:
            from compute.lib.quantum_group_root_of_unity_engine import (
                quantum_casimir_eigenvalue as existing_casimir,
            )
            q = cmath.exp(0.3j)
            for n in range(2, 6):
                j = (n - 1) / 2.0
                new_val = quantum_casimir_sl2(q, j)
                existing_val = existing_casimir(n, q)
                assert abs(new_val - existing_val) < 1e-10
        except ImportError:
            pytest.skip("quantum_group_root_of_unity_engine not available")

    def test_permutation_matrix_consistency(self):
        """Permutation matrix matches quantum_group_shadow engine."""
        try:
            from compute.lib.quantum_group_shadow import (
                slN_casimir_matrix,
            )
            for N in [2, 3]:
                P_new = permutation_matrix(N)
                P_existing = slN_casimir_matrix(N)
                err = float(np.max(np.abs(P_new - P_existing)))
                assert err < 1e-14, f"Permutation mismatch for N={N}: {err:.2e}"
        except ImportError:
            pytest.skip("quantum_group_shadow not available")

    def test_comprehensive_sl2(self):
        """Full comprehensive verification for sl_2 at level 1."""
        result = comprehensive_uq_sl2_verification(k=1.0)
        # Check critical components
        assert result["level_recovery_error"] < 1e-10
        assert result["dj_j0.5"]["all_hold"]
        assert result["hopf"]["all_hold"]
        assert result["three_presentations"]["all_hold"]
        assert result["universal_r_qybe"]["qybe_holds"]
        assert result["kappa_error"] < 1e-8


# =========================================================================
# Comprehensive suite
# =========================================================================

class TestComprehensiveSl3:
    """Comprehensive tests for sl_3."""

    def test_comprehensive_sl3_level1(self):
        """Full sl_3 verification at level 1."""
        result = comprehensive_uq_sl3_verification(k=1.0)
        assert result["dj_sl3"]["all_hold"]
        assert result["rtt_sl3"]["all_hold"]
        assert result["qybe_sl3_error"] < 1e-10
        assert result["kappa_error"] < 1e-8
