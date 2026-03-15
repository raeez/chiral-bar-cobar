"""
Tests for quantum lattice screening algebra computations.

Verifies braiding matrices, screening operator nilpotency,
and quantum group comparison data for the quantum group
identification programme (prop:lattice:quantum-group-connection).
"""

import numpy as np
import pytest
from compute.lib.quantum_lattice_screening import (
    cartan_matrix,
    inner_product_matrix,
    standard_antisymmetric_form,
    cocycle_commutator,
    screening_braiding_table,
    quantum_group_dimension,
    quantum_group_num_simples,
    a2_screening_analysis,
    verify_antisymmetry,
    all_antisymmetric_forms,
    a2_full_scan,
)


# ===========================================================
# Cartan matrix tests
# ===========================================================

class TestCartanMatrix:
    def test_a2(self):
        A = cartan_matrix("A2")
        assert A.shape == (2, 2)
        assert A[0, 0] == 2
        assert A[0, 1] == -1
        assert A[1, 0] == -1
        assert A[1, 1] == 2
        # det = 3 for A_2
        assert np.linalg.det(A) == pytest.approx(3.0)

    def test_a3(self):
        A = cartan_matrix("A3")
        assert A.shape == (3, 3)
        # det = 4 for A_3
        assert np.linalg.det(A) == pytest.approx(4.0)

    def test_d4(self):
        A = cartan_matrix("D4")
        assert A.shape == (4, 4)
        # det = 4 for D_4
        assert np.linalg.det(A) == pytest.approx(4.0)

    def test_simply_laced(self):
        """All entries are 2, -1, or 0 for simply-laced."""
        for lt in ["A2", "A3", "D4"]:
            A = cartan_matrix(lt)
            for i in range(A.shape[0]):
                for j in range(A.shape[1]):
                    assert A[i, j] in {-1, 0, 2}


# ===========================================================
# Antisymmetric form tests
# ===========================================================

class TestAntisymmetricForm:
    def test_rank2_basic(self):
        q = standard_antisymmetric_form(2, 5)
        assert q[0, 1] == 1
        assert q[1, 0] == 4  # = -1 mod 5
        assert q[0, 0] == 0
        assert q[1, 1] == 0

    def test_antisymmetry(self):
        for N in range(3, 8):
            q = standard_antisymmetric_form(2, N)
            assert verify_antisymmetry(q, N)

    def test_rank3(self):
        q = standard_antisymmetric_form(3, 5)
        assert verify_antisymmetry(q, 5)
        assert q[0, 1] == 1
        assert q[1, 2] == 1
        assert q[0, 2] == 0  # non-adjacent

    def test_nonzero(self):
        """All standard forms are non-zero for rank >= 2."""
        for r in [2, 3, 4]:
            q = standard_antisymmetric_form(r, 5)
            assert np.any(q != 0)

    def test_enumerate_rank2(self):
        """For rank 2 and N=5, there are 4 non-zero antisymmetric forms."""
        forms = list(all_antisymmetric_forms(2, 5))
        assert len(forms) == 4
        for q in forms:
            assert verify_antisymmetry(q, 5)
            assert np.any(q != 0)


# ===========================================================
# Cocycle commutator / braiding tests
# ===========================================================

class TestCocycleCommutator:
    def test_a2_diagonal_trivial(self):
        """Diagonal braiding c(alpha_i, alpha_i) = 1 for all i.

        This is because q is antisymmetric, so q(alpha_i, alpha_i) = 0,
        and (-1)^{<alpha_i, alpha_i>} = (-1)^2 = 1.
        """
        ip = inner_product_matrix("A2")
        q = standard_antisymmetric_form(2, 5)
        c = cocycle_commutator(ip, q, 5)
        assert np.isclose(c[0, 0], 1.0)
        assert np.isclose(c[1, 1], 1.0)

    def test_a2_off_diagonal(self):
        """Off-diagonal braiding for A_2 with standard form.

        c(alpha_1, alpha_2) = (-1)^{-1} * zeta^{2*1} = -zeta^2.
        """
        N = 5
        zeta = np.exp(2j * np.pi / N)
        ip = inner_product_matrix("A2")
        q = standard_antisymmetric_form(2, N)
        c = cocycle_commutator(ip, q, N)
        assert np.isclose(c[0, 1], -zeta**2)
        assert np.isclose(c[1, 0], -zeta ** (2 * (N - 1)))  # = -zeta^{-2}

    def test_product_c12_c21(self):
        """c(alpha_1, alpha_2) * c(alpha_2, alpha_1) = 1 for A_2.

        This follows from: (-1)^{-1} * zeta^2 * (-1)^{-1} * zeta^{-2} = 1.
        """
        for N in range(3, 10):
            ip = inner_product_matrix("A2")
            q = standard_antisymmetric_form(2, N)
            c = cocycle_commutator(ip, q, N)
            assert np.isclose(c[0, 1] * c[1, 0], 1.0)

    def test_all_N_diagonal_trivial(self):
        """Diagonal braiding is always 1, independent of N."""
        for N in range(3, 15):
            for lt in ["A2", "A3"]:
                ip = inner_product_matrix(lt)
                r = ip.shape[0]
                q = standard_antisymmetric_form(r, N)
                c = cocycle_commutator(ip, q, N)
                for i in range(r):
                    assert np.isclose(c[i, i], 1.0), (
                        f"Non-trivial diagonal at N={N}, {lt}, i={i}"
                    )

    def test_non_adjacent_braiding(self):
        """For non-adjacent nodes, <alpha_i, alpha_j> = 0 and q(i,j) = 0,
        so c(alpha_i, alpha_j) = 1.
        """
        ip = inner_product_matrix("A3")
        q = standard_antisymmetric_form(3, 5)
        c = cocycle_commutator(ip, q, 5)
        # alpha_1 and alpha_3 are non-adjacent in A_3
        assert np.isclose(c[0, 2], 1.0)
        assert np.isclose(c[2, 0], 1.0)


# ===========================================================
# Screening braiding table tests
# ===========================================================

class TestScreeningBraidingTable:
    def test_a2_structure(self):
        table = screening_braiding_table("A2", 5)
        assert len(table["diagonal"]) == 2
        assert len(table["nilpotency_order"]) == 2
        assert all(n == 2 for n in table["nilpotency_order"])

    def test_a2_adjacent_count(self):
        """A_2 has 2 adjacent pairs: (0,1) and (1,0)."""
        table = screening_braiding_table("A2", 5)
        assert len(table["off_diagonal_adjacent"]) == 2

    def test_d4_adjacent_count(self):
        """D_4 has node 1 adjacent to 0, 2, 3 (= 6 ordered pairs)."""
        table = screening_braiding_table("D4", 5)
        assert len(table["off_diagonal_adjacent"]) == 6


# ===========================================================
# Quantum group data tests
# ===========================================================

class TestQuantumGroupData:
    def test_a2_dimension(self):
        """dim u_zeta(sl_3) = N^8 for N odd (dim sl_3 = 8)."""
        assert quantum_group_dimension("A2", 3) == 3**8  # 6561
        assert quantum_group_dimension("A2", 5) == 5**8

    def test_a2_simples(self):
        """Number of simples of u_zeta(sl_3) = N^2."""
        assert quantum_group_num_simples("A2", 3) == 9
        assert quantum_group_num_simples("A2", 5) == 25

    def test_a3_simples(self):
        """Number of simples of u_zeta(sl_4) = N^3."""
        assert quantum_group_num_simples("A3", 3) == 27


# ===========================================================
# Full A_2 analysis tests
# ===========================================================

class TestA2Analysis:
    def test_n3_coxeter(self):
        """N = 3 = h (Coxeter number of A_2) is the critical case."""
        result = a2_screening_analysis(3)
        assert result["N"] == 3
        assert result["braiding_match"]
        assert result["diagonal_trivial"]
        assert result["qg_num_simples"] == 9
        assert all(n == 2 for n in result["nilpotency_orders"])

    def test_n5(self):
        result = a2_screening_analysis(5)
        assert result["braiding_match"]
        assert result["diagonal_trivial"]
        assert np.isclose(result["product_c12_c21"], 1.0)

    def test_scan(self):
        """Full scan for N = 3, ..., 8."""
        results = a2_full_scan(8)
        assert len(results) == 6  # N = 3, 4, 5, 6, 7, 8
        for r in results:
            assert r["braiding_match"]
            assert r["diagonal_trivial"]
            assert np.isclose(r["product_c12_c21"], 1.0)


# ===========================================================
# Consistency tests across Lie types
# ===========================================================

class TestConsistency:
    def test_braiding_varies_with_N(self):
        """Off-diagonal braiding should change with N."""
        braidings = []
        for N in [3, 5, 7]:
            table = screening_braiding_table("A2", N)
            braidings.append(table["off_diagonal_adjacent"][0][2])
        # All three should be distinct
        assert not np.isclose(braidings[0], braidings[1])
        assert not np.isclose(braidings[1], braidings[2])

    def test_braiding_varies_with_q(self):
        """Different antisymmetric forms give different braidings."""
        braidings = []
        for q in all_antisymmetric_forms(2, 7):
            c = cocycle_commutator(inner_product_matrix("A2"), q, 7)
            braidings.append(c[0, 1])
        # Should have 6 distinct values (q = 1, ..., 6)
        assert len(braidings) == 6
        # Check they're pairwise distinct
        for i in range(len(braidings)):
            for j in range(i + 1, len(braidings)):
                assert not np.isclose(braidings[i], braidings[j])

    def test_inverse_form_gives_conjugate_braiding(self):
        """q -> -q sends c(alpha_i, alpha_j) to its complex conjugate
        (up to the sign factor).

        More precisely: c_{N,-q}(alpha_i, alpha_j) = c_{N,q}(alpha_j, alpha_i).
        """
        N = 7
        ip = inner_product_matrix("A2")
        q = standard_antisymmetric_form(2, N)
        q_neg = np.zeros_like(q)
        q_neg[0, 1] = (N - q[0, 1]) % N
        q_neg[1, 0] = (N - q[1, 0]) % N

        c_q = cocycle_commutator(ip, q, N)
        c_negq = cocycle_commutator(ip, q_neg, N)

        # c_{N,-q}(i,j) should equal c_{N,q}(j,i)
        assert np.isclose(c_negq[0, 1], c_q[1, 0])
        assert np.isclose(c_negq[1, 0], c_q[0, 1])
