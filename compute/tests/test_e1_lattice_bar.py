"""
Tests for E1 lattice bar complex computations.

Verifies every facet of the quantum lattice algebra construction
for the three main examples:
  1. A_2 with N=3, q=1 (critical / Coxeter)
  2. A_2 with N=5, q=2 (non-standard deformation)
  3. D_4 with N=3, standard edge form (higher rank / triality)
"""

import numpy as np
import pytest
from compute.lib.e1_lattice_bar import (
    cartan_matrix,
    rank,
    num_positive_roots,
    adjacent_pairs,
    simple_root_sectors,
    symmetric_cocycle,
    verify_borcherds_symmetry,
    antisymmetric_form,
    deformed_cocycle,
    cocycle_commutator,
    verify_commutator_from_cocycle,
    is_symmetric_cocycle,
    e1_bar_differential_sector,
    e1_bar_differential_sector_einf,
    n_torsion_check,
    koszul_dual_data,
    full_e1_computation,
    format_complex_exact,
)


# =========================================================================
# Lattice data tests
# =========================================================================

class TestLatticeData:
    def test_a2_cartan(self):
        A = cartan_matrix("A2")
        assert A.shape == (2, 2)
        np.testing.assert_array_equal(A, [[2, -1], [-1, 2]])
        assert np.linalg.det(A) == pytest.approx(3.0)

    def test_d4_cartan(self):
        A = cartan_matrix("D4")
        assert A.shape == (4, 4)
        assert np.linalg.det(A) == pytest.approx(4.0)
        # Node 2 (index 1) is central
        assert A[1, 0] == -1
        assert A[1, 2] == -1
        assert A[1, 3] == -1
        # Non-adjacent: (0,2), (0,3), (2,3)
        assert A[0, 2] == 0
        assert A[0, 3] == 0
        assert A[2, 3] == 0

    def test_positive_roots(self):
        assert num_positive_roots("A2") == 3
        assert num_positive_roots("D4") == 12

    def test_adjacent_pairs_a2(self):
        pairs = adjacent_pairs("A2")
        assert set(pairs) == {(0, 1), (1, 0)}

    def test_adjacent_pairs_d4(self):
        pairs = adjacent_pairs("D4")
        # Node 1 (idx 1) adjacent to 0, 2, 3: gives 6 ordered pairs
        assert len(pairs) == 6
        assert (0, 1) in pairs
        assert (1, 0) in pairs
        assert (1, 2) in pairs
        assert (2, 1) in pairs
        assert (1, 3) in pairs
        assert (3, 1) in pairs

    def test_simple_root_sectors_a2(self):
        sectors = simple_root_sectors("A2")
        assert sectors == [(0, 1)]  # One sector: alpha_1 + alpha_2

    def test_simple_root_sectors_d4(self):
        sectors = simple_root_sectors("D4")
        # 3 unordered adjacent pairs: {0,1}, {1,2}, {1,3}
        assert len(sectors) == 3
        assert (0, 1) in sectors
        assert (1, 2) in sectors
        assert (1, 3) in sectors


# =========================================================================
# Symmetric cocycle tests
# =========================================================================

class TestSymmetricCocycle:
    def test_a2_values(self):
        """FLM convention: eps_0(1,2) = -1, eps_0(2,1) = 1."""
        eps = symmetric_cocycle("A2")
        assert eps[0, 1] == -1  # adjacent, i < j
        assert eps[1, 0] == 1   # adjacent, i > j
        assert eps[0, 0] == 1
        assert eps[1, 1] == 1

    def test_d4_values(self):
        eps = symmetric_cocycle("D4")
        # Adjacent pairs with i < j: (0,1), (1,2), (1,3)
        assert eps[0, 1] == -1
        assert eps[1, 2] == -1
        assert eps[1, 3] == -1
        # Reverse: all +1
        assert eps[1, 0] == 1
        assert eps[2, 1] == 1
        assert eps[3, 1] == 1
        # Non-adjacent: all +1
        assert eps[0, 2] == 1
        assert eps[0, 3] == 1
        assert eps[2, 3] == 1

    def test_borcherds_symmetry_a2(self):
        eps = symmetric_cocycle("A2")
        A = cartan_matrix("A2")
        assert verify_borcherds_symmetry(eps, A)

    def test_borcherds_symmetry_d4(self):
        eps = symmetric_cocycle("D4")
        A = cartan_matrix("D4")
        assert verify_borcherds_symmetry(eps, A)


# =========================================================================
# Antisymmetric form tests
# =========================================================================

class TestAntisymmetricForm:
    def test_a2_standard(self):
        q = antisymmetric_form("A2", 3)
        assert q[0, 1] == 1
        assert q[1, 0] == 2  # = -1 mod 3
        assert q[0, 0] == 0
        assert q[1, 1] == 0

    def test_a2_custom(self):
        q = antisymmetric_form("A2", 5, q_values={(0, 1): 2})
        assert q[0, 1] == 2
        assert q[1, 0] == 3  # = -2 mod 5

    def test_d4_standard(self):
        q = antisymmetric_form("D4", 3)
        # Adjacent pairs get q = 1
        assert q[0, 1] == 1
        assert q[1, 2] == 1
        assert q[1, 3] == 1
        # Non-adjacent: q = 0
        assert q[0, 2] == 0
        assert q[0, 3] == 0
        assert q[2, 3] == 0
        # Antisymmetric
        for i in range(4):
            for j in range(4):
                assert (q[i, j] + q[j, i]) % 3 == 0

    def test_nonzero(self):
        for lt in ["A2", "D4"]:
            q = antisymmetric_form(lt, 3)
            assert np.any(q != 0)


# =========================================================================
# Deformed cocycle tests
# =========================================================================

class TestDeformedCocycle:
    def test_a2_n3_values(self):
        """Explicit numerical values for A_2, N=3, q=1."""
        q = antisymmetric_form("A2", 3)
        eps = deformed_cocycle("A2", 3, q)
        zeta = np.exp(2j * np.pi / 3)

        # eps_{3,1}(alpha_1, alpha_2) = eps_0(1,2) * zeta^1 = (-1)*zeta = -zeta
        assert np.isclose(eps[0, 1], -zeta)

        # eps_{3,1}(alpha_2, alpha_1) = eps_0(2,1) * zeta^{-1} = 1*zeta^2 = zeta^2
        assert np.isclose(eps[1, 0], zeta ** 2)

    def test_a2_n5_q2_values(self):
        """Explicit values for A_2, N=5, q=2."""
        q = antisymmetric_form("A2", 5, q_values={(0, 1): 2})
        eps = deformed_cocycle("A2", 5, q)
        zeta = np.exp(2j * np.pi / 5)

        # eps_{5,2}(alpha_1, alpha_2) = (-1)*zeta^2 = -zeta^2
        assert np.isclose(eps[0, 1], -zeta ** 2)

        # eps_{5,2}(alpha_2, alpha_1) = 1*zeta^{-2} = zeta^3
        assert np.isclose(eps[1, 0], zeta ** 3)

    def test_d4_n3_values(self):
        """Explicit values for D_4, N=3."""
        q = antisymmetric_form("D4", 3)
        eps = deformed_cocycle("D4", 3, q)
        zeta = np.exp(2j * np.pi / 3)

        # (0,1): eps_0 = -1, q = 1 -> -zeta
        assert np.isclose(eps[0, 1], -zeta)
        # (1,0): eps_0 = 1, q = 2 -> zeta^2
        assert np.isclose(eps[1, 0], zeta ** 2)
        # (1,2): eps_0 = -1, q = 1 -> -zeta
        assert np.isclose(eps[1, 2], -zeta)
        # (2,1): eps_0 = 1, q = 2 -> zeta^2
        assert np.isclose(eps[2, 1], zeta ** 2)
        # (1,3): same as (1,2) by triality
        assert np.isclose(eps[1, 3], -zeta)
        # (3,1): same as (2,1)
        assert np.isclose(eps[3, 1], zeta ** 2)

    def test_not_borcherds_symmetric(self):
        """Deformed cocycle is NOT Borcherds-symmetric for N >= 3."""
        for lt, N in [("A2", 3), ("A2", 5), ("D4", 3)]:
            q = antisymmetric_form(lt, N)
            eps = deformed_cocycle(lt, N, q)
            A = cartan_matrix(lt)
            assert not is_symmetric_cocycle(eps, A), \
                f"{lt} at N={N} should NOT be Borcherds-symmetric"


# =========================================================================
# Commutator / braiding tests
# =========================================================================

class TestCommutator:
    def test_a2_n3_braiding(self):
        """c(alpha_1, alpha_2) = (-1)^{-1} * zeta_3^{2*1} = -zeta_3^2."""
        q = antisymmetric_form("A2", 3)
        c = cocycle_commutator("A2", 3, q)
        zeta = np.exp(2j * np.pi / 3)

        assert np.isclose(c[0, 1], -zeta ** 2)
        assert np.isclose(c[1, 0], -zeta ** 1)  # = -zeta = conjugate braiding
        assert np.isclose(c[0, 0], 1.0)
        assert np.isclose(c[1, 1], 1.0)

    def test_a2_n5_q2_braiding(self):
        """c(1,2) = -zeta_5^{2*2} = -zeta_5^4."""
        q = antisymmetric_form("A2", 5, q_values={(0, 1): 2})
        c = cocycle_commutator("A2", 5, q)
        zeta = np.exp(2j * np.pi / 5)

        assert np.isclose(c[0, 1], -zeta ** 4)
        assert np.isclose(c[1, 0], -zeta ** 1)  # -zeta^{2*(-2)} = -zeta^{-4} = -zeta^1

    def test_d4_n3_braiding(self):
        """D_4: adjacent pairs have c = -zeta_3^2, non-adjacent have c = 1."""
        q = antisymmetric_form("D4", 3)
        c = cocycle_commutator("D4", 3, q)
        zeta = np.exp(2j * np.pi / 3)

        # Adjacent: (0,1), (1,2), (1,3) all have c = -zeta^2
        for i, j in [(0, 1), (1, 2), (1, 3)]:
            assert np.isclose(c[i, j], -zeta ** 2), f"c({i},{j}) wrong"

        # Non-adjacent: (0,2), (0,3), (2,3) have c = 1
        for i, j in [(0, 2), (0, 3), (2, 3)]:
            assert np.isclose(c[i, j], 1.0), f"c({i},{j}) should be 1"

    def test_diagonal_trivial(self):
        """c(alpha_i, alpha_i) = 1 for all i (antisymmetry of q)."""
        for lt, N in [("A2", 3), ("A2", 5), ("D4", 3)]:
            q = antisymmetric_form(lt, N)
            c = cocycle_commutator(lt, N, q)
            r = rank(lt)
            for i in range(r):
                assert np.isclose(c[i, i], 1.0)

    def test_commutator_product_one(self):
        """c(i,j) * c(j,i) = 1 for adjacent pairs in even lattice."""
        for lt, N in [("A2", 3), ("A2", 5), ("D4", 3)]:
            q = antisymmetric_form(lt, N)
            c = cocycle_commutator(lt, N, q)
            A = cartan_matrix(lt)
            r = A.shape[0]
            for i in range(r):
                for j in range(r):
                    if i != j and A[i, j] == -1:
                        assert np.isclose(c[i, j] * c[j, i], 1.0), \
                            f"c({i},{j})*c({j},{i}) != 1"

    def test_formula_matches_direct(self):
        """Verify c(i,j) from formula matches eps(i,j)/eps(j,i)."""
        for lt, N in [("A2", 3), ("A2", 5), ("D4", 3)]:
            q = antisymmetric_form(lt, N)
            assert verify_commutator_from_cocycle(lt, N, q)


# =========================================================================
# E1 bar differential and ordering cycle tests
# =========================================================================

class TestE1BarDifferential:
    def test_a2_n3_differential(self):
        """Bar differential in sector alpha_1 + alpha_2 for A_2, N=3."""
        q = antisymmetric_form("A2", 3)
        result = e1_bar_differential_sector("A2", 3, q, 0, 1)
        zeta = np.exp(2j * np.pi / 3)

        # d = (eps_{3,1}(1,2), eps_{3,1}(2,1)) = (-zeta, zeta^2)
        assert np.isclose(result["differential"][0], -zeta)
        assert np.isclose(result["differential"][1], zeta ** 2)
        assert result["rank"] == 1
        assert result["kernel_dim"] == 1

    def test_a2_n3_ordering_cycle(self):
        """Ordering cycle for A_2, N=3."""
        q = antisymmetric_form("A2", 3)
        result = e1_bar_differential_sector("A2", 3, q, 0, 1)
        zeta = np.exp(2j * np.pi / 3)

        xi = result["ordering_cycle"]
        # xi = v_+ + lambda * v_- where lambda = -eps(1,2)/eps(2,1)
        # = -(-zeta)/(zeta^2) = zeta/zeta^2 = zeta^{-1} = zeta^2
        expected_ratio = zeta ** (-1)  # = zeta^2
        assert np.isclose(result["cycle_ratio"], expected_ratio)

        # Verify in kernel: d . xi = 0
        d = result["differential"]
        assert np.isclose(np.dot(d, xi), 0)

    def test_a2_n5_q2_ordering_cycle(self):
        """Ordering cycle for A_2, N=5, q=2."""
        q = antisymmetric_form("A2", 5, q_values={(0, 1): 2})
        result = e1_bar_differential_sector("A2", 5, q, 0, 1)
        zeta = np.exp(2j * np.pi / 5)

        # eps(1,2) = -zeta^2, eps(2,1) = zeta^3
        # lambda = -(-zeta^2)/(zeta^3) = zeta^2/zeta^3 = zeta^{-1} = zeta^4
        expected_ratio = zeta ** (-1)  # = zeta^4
        assert np.isclose(result["cycle_ratio"], expected_ratio)

        # Verify kernel
        assert np.isclose(np.dot(result["differential"], result["ordering_cycle"]), 0)

    def test_d4_n3_three_sectors(self):
        """D_4 has 3 simple-root sectors, each with one ordering cycle."""
        q = antisymmetric_form("D4", 3)
        for i, j in [(0, 1), (1, 2), (1, 3)]:
            result = e1_bar_differential_sector("D4", 3, q, i, j)
            assert result["h2"] == 1
            assert result["h1"] == 0
            # Verify kernel
            assert np.isclose(
                np.dot(result["differential"], result["ordering_cycle"]), 0
            )

    def test_d4_triality_symmetry(self):
        """Sectors (1,2) and (1,3) have the same structure by triality
        (for the standard edge form with q identical on all edges)."""
        q = antisymmetric_form("D4", 3)
        r12 = e1_bar_differential_sector("D4", 3, q, 1, 2)
        r13 = e1_bar_differential_sector("D4", 3, q, 1, 3)

        # Same differential (by triality: same cocycle values)
        assert np.isclose(r12["differential"][0], r13["differential"][0])
        assert np.isclose(r12["differential"][1], r13["differential"][1])
        # Same cycle ratio
        assert np.isclose(r12["cycle_ratio"], r13["cycle_ratio"])

    def test_einf_comparison(self):
        """E-infinity bar complex has H^2 = 0 in these sectors."""
        for lt, (i, j) in [("A2", (0, 1)), ("D4", (0, 1)),
                            ("D4", (1, 2)), ("D4", (1, 3))]:
            result = e1_bar_differential_sector_einf(lt, i, j)
            assert result["h2"] == 0
            assert result["dim_bar2"] == 1  # vs 2 for E1


# =========================================================================
# N-torsion tests
# =========================================================================

class TestNTorsion:
    def test_a2_n3(self):
        q = antisymmetric_form("A2", 3)
        result = n_torsion_check("A2", 3, q)
        assert result["all_pass"]

    def test_a2_n5(self):
        q = antisymmetric_form("A2", 5, q_values={(0, 1): 2})
        result = n_torsion_check("A2", 5, q)
        assert result["all_pass"]

    def test_d4_n3(self):
        q = antisymmetric_form("D4", 3)
        result = n_torsion_check("D4", 3, q)
        assert result["all_pass"]


# =========================================================================
# Koszul dual tests
# =========================================================================

class TestKoszulDual:
    def test_a2_n3_dual_form(self):
        """Koszul dual has q -> -q: for N=3, q=1, -q = 2 mod 3."""
        q = antisymmetric_form("A2", 3)
        kd = koszul_dual_data("A2", 3, q)
        assert kd["q_dual"][0, 1] == 2
        assert kd["q_dual"][1, 0] == 1

    def test_a2_n5_q2_dual_form(self):
        """For N=5, q=2, -q = 3 mod 5."""
        q = antisymmetric_form("A2", 5, q_values={(0, 1): 2})
        kd = koszul_dual_data("A2", 5, q)
        assert kd["q_dual"][0, 1] == 3
        assert kd["q_dual"][1, 0] == 2

    def test_transpose_identity(self):
        """c_{-q}(i,j) = c_q(j,i) for all examples."""
        for lt, N, qv in [("A2", 3, None), ("A2", 5, {(0, 1): 2}), ("D4", 3, None)]:
            q = antisymmetric_form(lt, N, qv)
            kd = koszul_dual_data(lt, N, q)
            assert kd["transpose_identity"], f"Transpose identity failed for {lt}, N={N}"

    def test_product_identity(self):
        """c_q(i,j) * c_{-q}(i,j) = 1 for even lattice."""
        for lt, N, qv in [("A2", 3, None), ("A2", 5, {(0, 1): 2}), ("D4", 3, None)]:
            q = antisymmetric_form(lt, N, qv)
            kd = koszul_dual_data(lt, N, q)
            assert kd["product_identity"], f"Product identity failed for {lt}, N={N}"

    def test_not_self_dual(self):
        """For N >= 3, the algebra is never Koszul self-dual: q != -q mod N."""
        for lt, N, qv in [("A2", 3, None), ("A2", 5, {(0, 1): 2}), ("D4", 3, None)]:
            q = antisymmetric_form(lt, N, qv)
            kd = koszul_dual_data(lt, N, q)
            assert not np.array_equal(kd["q_original"], kd["q_dual"]), \
                f"{lt} at N={N} should NOT be self-dual"


# =========================================================================
# Full computation integration tests
# =========================================================================

class TestFullComputation:
    def test_a2_n3(self):
        result = full_e1_computation("A2", 3)
        assert result["symmetry"]["strictly_e1"]
        assert result["total_ordering_cycles"] == 1
        assert result["n_torsion"]["all_pass"]
        assert result["koszul_dual"]["transpose_identity"]

    def test_a2_n5_q2(self):
        result = full_e1_computation("A2", 5, q_values={(0, 1): 2})
        assert result["symmetry"]["strictly_e1"]
        assert result["total_ordering_cycles"] == 1
        assert result["n_torsion"]["all_pass"]

    def test_d4_n3(self):
        result = full_e1_computation("D4", 3)
        assert result["symmetry"]["strictly_e1"]
        assert result["total_ordering_cycles"] == 3
        assert result["n_torsion"]["all_pass"]
        assert result["koszul_dual"]["transpose_identity"]

    def test_all_examples_consistent(self):
        """Cross-check: different N on same lattice give different braidings."""
        r1 = full_e1_computation("A2", 3)
        r2 = full_e1_computation("A2", 5, q_values={(0, 1): 2})
        c1 = r1["braiding"]["commutator_matrix"][0, 1]
        c2 = r2["braiding"]["commutator_matrix"][0, 1]
        assert not np.isclose(c1, c2), "Different deformations should give different braidings"


# =========================================================================
# LaTeX output tests (format verification)
# =========================================================================

class TestFormatting:
    def test_format_zeta3(self):
        zeta = np.exp(2j * np.pi / 3)
        assert format_complex_exact(zeta, 3) == r"\zeta_{3}"
        assert format_complex_exact(zeta ** 2, 3) == r"\zeta_{3}^{2}"
        assert format_complex_exact(-zeta, 3) == r"-\zeta_{3}"
        assert format_complex_exact(1.0 + 0j, 3) == "1"
        assert format_complex_exact(-1.0 + 0j, 3) == "-1"

    def test_format_zeta5(self):
        zeta = np.exp(2j * np.pi / 5)
        assert format_complex_exact(zeta ** 2, 5) == r"\zeta_{5}^{2}"
        assert format_complex_exact(-zeta ** 4, 5) == r"-\zeta_{5}^{4}"
