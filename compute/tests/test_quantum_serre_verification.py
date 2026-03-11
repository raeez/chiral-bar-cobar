"""Tests for quantum Serre relation verification on lattice screening operators.

Verifies that the braiding data, quantum group numerology, and Serre relation
structure are consistent with prop:lattice:quantum-group-connection(ii).
"""

import pytest
import cmath
import numpy as np


# ---------------------------------------------------------------------------
# Quantum integer / binomial tests
# ---------------------------------------------------------------------------

class TestQuantumIntegers:
    """Verify quantum integer identities at roots of unity."""

    def test_quantum_2_at_cube_root(self):
        """[2]_ω = ω + ω⁻¹ = -1 where ω = e^{2πi/3}."""
        from compute.lib.quantum_serre_verification import quantum_integer
        omega = cmath.exp(2j * cmath.pi / 3)
        assert abs(quantum_integer(2, omega) - (-1)) < 1e-10

    def test_quantum_n_vanishes(self):
        """[N]_ζ = 0 at ζ = e^{2πi/N} for N = 3,4,5,7."""
        from compute.lib.quantum_serre_verification import quantum_integer
        for N in [3, 4, 5, 7]:
            zeta = cmath.exp(2j * cmath.pi / N)
            assert abs(quantum_integer(N, zeta)) < 1e-10, f"[{N}]_ζ ≠ 0 at N={N}"

    def test_quantum_1_is_1(self):
        """[1]_q = 1 for all q."""
        from compute.lib.quantum_serre_verification import quantum_integer
        for N in [3, 5, 7]:
            zeta = cmath.exp(2j * cmath.pi / N)
            assert abs(quantum_integer(1, zeta) - 1) < 1e-10

    @pytest.mark.parametrize("N", [3, 5, 7])
    def test_quantum_binomial_n_choose_1(self, N):
        """[N choose 1]_ζ = [N]_ζ = 0."""
        from compute.lib.quantum_serre_verification import quantum_binomial
        zeta = cmath.exp(2j * cmath.pi / N)
        assert abs(quantum_binomial(N, 1, zeta)) < 1e-10

    def test_quantum_2_choose_1(self):
        """[2 choose 1]_ζ = [2]_ζ = -1 at N=3."""
        from compute.lib.quantum_serre_verification import quantum_binomial
        omega = cmath.exp(2j * cmath.pi / 3)
        assert abs(quantum_binomial(2, 1, omega) - (-1)) < 1e-10

    def test_quantum_factorial_3_at_cube_root(self):
        """[3]!_ω = [1]_ω · [2]_ω · [3]_ω = 1 · (-1) · 0 = 0."""
        from compute.lib.quantum_serre_verification import quantum_factorial
        omega = cmath.exp(2j * cmath.pi / 3)
        assert abs(quantum_factorial(3, omega)) < 1e-10


# ---------------------------------------------------------------------------
# Braiding tests
# ---------------------------------------------------------------------------

class TestBraiding:
    """Verify screening operator braiding data."""

    def test_diagonal_trivial(self):
        """Self-braiding c(α_i,α_i) = 1 for all i."""
        from compute.lib.quantum_serre_verification import screening_braiding
        for N in [3, 5, 7]:
            result = screening_braiding("A2", N)
            assert result["diagonal_trivial"], f"Diagonal not trivial at N={N}"

    def test_product_symmetry(self):
        """c(α_i,α_j) · c(α_j,α_i) = 1 for adjacent pairs."""
        from compute.lib.quantum_serre_verification import screening_braiding
        for N in [3, 5, 7]:
            result = screening_braiding("A2", N)
            for pair, data in result["products"].items():
                assert data["equals_one"], f"Product ≠ 1 at N={N}, pair {pair}"

    def test_a2_n3_braiding(self):
        """At N=3: c(α₁,α₂) = -ζ² = e^{πi/3}."""
        from compute.lib.quantum_serre_verification import screening_braiding
        result = screening_braiding("A2", 3)
        zeta = cmath.exp(2j * cmath.pi / 3)
        expected = -zeta ** 2
        # Find the (0,1) adjacent braiding
        for b in result["adjacent_braiding"]:
            if b["pair"] == (0, 1):
                assert abs(b["c_ij"] - expected) < 1e-10
                break

    def test_a3_diagonal_trivial(self):
        """A₃ screening braiding has trivial diagonal."""
        from compute.lib.quantum_serre_verification import screening_braiding
        result = screening_braiding("A3", 5)
        assert result["diagonal_trivial"]

    def test_d4_diagonal_trivial(self):
        """D₄ screening braiding has trivial diagonal."""
        from compute.lib.quantum_serre_verification import screening_braiding
        result = screening_braiding("D4", 5)
        assert result["diagonal_trivial"]


# ---------------------------------------------------------------------------
# Quantum Serre analysis
# ---------------------------------------------------------------------------

class TestQuantumSerre:
    """Verify quantum Serre relation structure."""

    def test_a2_n3_serre_satisfied(self):
        """Quantum Serre relations satisfied for A₂ at N=3."""
        from compute.lib.quantum_serre_verification import quantum_serre_analysis
        result = quantum_serre_analysis("A2", 3)
        assert result["all_serre_satisfied"]

    def test_a2_n5_serre_satisfied(self):
        """Quantum Serre relations satisfied for A₂ at N=5."""
        from compute.lib.quantum_serre_verification import quantum_serre_analysis
        result = quantum_serre_analysis("A2", 5)
        assert result["all_serre_satisfied"]

    @pytest.mark.parametrize("N", [3, 4, 5, 7, 9])
    def test_n_quantum_int_zero(self, N):
        """[N]_ζ = 0 for all tested N."""
        from compute.lib.quantum_serre_verification import quantum_serre_analysis
        result = quantum_serre_analysis("A2", N)
        assert result["[N]_q_is_zero"]

    def test_a3_serre(self):
        """Quantum Serre satisfied for A₃ at N=5."""
        from compute.lib.quantum_serre_verification import quantum_serre_analysis
        result = quantum_serre_analysis("A3", 5)
        assert result["all_serre_satisfied"]


# ---------------------------------------------------------------------------
# Module count comparison
# ---------------------------------------------------------------------------

class TestModuleCount:
    """Verify lattice sector count = quantum group simple module count."""

    @pytest.mark.parametrize("N", [3, 5, 7])
    def test_a2_module_count(self, N):
        """A₂: N² lattice sectors = N² QG simples."""
        from compute.lib.quantum_serre_verification import module_count_comparison
        result = module_count_comparison("A2", N)
        assert result["match"]
        assert result["lattice_sectors"] == N ** 2

    @pytest.mark.parametrize("N", [3, 5])
    def test_a3_module_count(self, N):
        """A₃: N³ lattice sectors = N³ QG simples."""
        from compute.lib.quantum_serre_verification import module_count_comparison
        result = module_count_comparison("A3", N)
        assert result["match"]
        assert result["lattice_sectors"] == N ** 3

    def test_d4_module_count(self):
        """D₄: N⁴ lattice sectors = N⁴ QG simples."""
        from compute.lib.quantum_serre_verification import module_count_comparison
        result = module_count_comparison("D4", 3)
        assert result["match"]
        assert result["lattice_sectors"] == 3 ** 4


# ---------------------------------------------------------------------------
# Nichols algebra type
# ---------------------------------------------------------------------------

class TestNicholsType:
    """Verify Nichols algebra type classification."""

    def test_a2_super_type(self):
        """A₂ screening Nichols algebra is super-type (q_{ii}=1)."""
        from compute.lib.quantum_serre_verification import nichols_algebra_type
        result = nichols_algebra_type("A2", 3)
        assert result["is_super_type"]

    def test_nilpotency_order_2(self):
        """Screening operators have nilpotency order 2."""
        from compute.lib.quantum_serre_verification import nichols_algebra_type
        result = nichols_algebra_type("A2", 3)
        assert result["nilpotency_order"] == 2

    def test_qg_nilpotency_n(self):
        """Quantum group has nilpotency order N."""
        from compute.lib.quantum_serre_verification import nichols_algebra_type
        for N in [3, 5, 7]:
            result = nichols_algebra_type("A2", N)
            assert result["qg_nilpotency_order"] == N

    def test_super_cartan_mismatch(self):
        """Super-type vs Cartan-type mismatch is acknowledged."""
        from compute.lib.quantum_serre_verification import nichols_algebra_type
        result = nichols_algebra_type("A2", 3)
        assert result["super_vs_cartan_mismatch"]


# ---------------------------------------------------------------------------
# A₂ N=3 detailed analysis
# ---------------------------------------------------------------------------

class TestA2N3:
    """Detailed tests for the primary A₂, N=3 test case."""

    def test_quantum_2_is_minus_1(self):
        """[2]_ω = -1."""
        from compute.lib.quantum_serre_verification import a2_n3_full_analysis
        result = a2_n3_full_analysis()
        assert result["[2]_ζ = -1"]

    def test_quantum_3_is_zero(self):
        """[3]_ω = 0."""
        from compute.lib.quantum_serre_verification import a2_n3_full_analysis
        result = a2_n3_full_analysis()
        assert result["[3]_ζ = 0"]

    def test_module_count_9(self):
        """9 lattice sectors = 9 QG simples."""
        from compute.lib.quantum_serre_verification import a2_n3_full_analysis
        result = a2_n3_full_analysis()
        assert result["modules"]["lattice_sectors"] == 9
        assert result["modules"]["qg_simples"] == 9
        assert result["modules"]["match"]

    def test_quantum_binomial_vanishing(self):
        """[3 choose k]_ω = 0 for k=1,2."""
        from compute.lib.quantum_serre_verification import a2_n3_full_analysis
        result = a2_n3_full_analysis()
        assert result["[3 choose 1]_ζ = 0"]
        assert result["[3 choose 2]_ζ = 0"]

    def test_serre_satisfied(self):
        """Quantum Serre relations satisfied."""
        from compute.lib.quantum_serre_verification import a2_n3_full_analysis
        result = a2_n3_full_analysis()
        assert result["serre"]["all_serre_satisfied"]


# ---------------------------------------------------------------------------
# Multi-N scan
# ---------------------------------------------------------------------------

class TestMultiNScan:
    """Verify consistency across multiple N values."""

    def test_scan_a2_3_to_9(self):
        """All N from 3 to 9 satisfy Serre and module count."""
        from compute.lib.quantum_serre_verification import scan_quantum_serre
        results = scan_quantum_serre("A2", 3, 9)
        for N, data in results.items():
            assert data["serre_satisfied"], f"Serre failed at N={N}"
            assert data["module_count_match"], f"Module count mismatch at N={N}"
            assert data["[N]_q_zero"], f"[N]_q ≠ 0 at N={N}"
