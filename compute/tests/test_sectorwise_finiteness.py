"""Tests for sectorwise finiteness and E₁ growth analysis.

Verifies the MC3 lattice bypass route:
  - Lattice bar complex sector dimensions (A₁, A₂, D₄)
  - Sectorwise finiteness for positive-definite lattices
  - E₁ growth rate fits for sl₂, sl₃, sl₄
  - Sub-exponential growth verification
  - LQT asymptotic formula comparison
  - Simply-laced level-1 DK unconditional checks

References:
    prop:lqt-e1-subexponential-growth, conj:mc3-sectorwise-all-types,
    thm:lattice:unimodular-self-dual
"""

import math

import numpy as np
import pytest

from compute.lib.sectorwise_finiteness import (
    CARTAN_MATRICES,
    get_gram_matrix,
    lattice_rank,
    lattice_determinant,
    is_unimodular,
    fock_dim_at_weight,
    lattice_bar_sector_dimension,
    sectorwise_finiteness_check,
    e1_growth_rate,
    lqt_asymptotic_comparison,
    sub_exponential_growth_test,
    lattice_factorization_dk_verification,
    simply_laced_level1_check,
)
from compute.lib.lqt_e1_growth import e1_dimensions


# =========================================================================
# Lattice data tests
# =========================================================================

class TestLatticeData:
    """Test root lattice Gram matrix data."""

    def test_a1_gram(self):
        """A₁ root lattice Gram matrix = [[2]]."""
        gram = get_gram_matrix("A1")
        np.testing.assert_array_equal(gram, [[2]])

    def test_a2_gram(self):
        """A₂ root lattice Gram matrix = Cartan matrix of A₂."""
        gram = get_gram_matrix("A2")
        expected = np.array([[2, -1], [-1, 2]])
        np.testing.assert_array_equal(gram, expected)

    def test_d4_gram(self):
        """D₄ root lattice Gram matrix = Cartan matrix of D₄."""
        gram = get_gram_matrix("D4")
        assert gram.shape == (4, 4)
        # Central node (index 1) connects to 0, 2, 3
        assert gram[1, 0] == -1
        assert gram[1, 2] == -1
        assert gram[1, 3] == -1
        # Non-adjacent
        assert gram[0, 2] == 0
        assert gram[0, 3] == 0
        assert gram[2, 3] == 0

    def test_e8_gram(self):
        """E₈ root lattice Gram matrix is 8×8."""
        gram = get_gram_matrix("E8")
        assert gram.shape == (8, 8)
        # All diagonal entries are 2
        for i in range(8):
            assert gram[i, i] == 2

    def test_a1_rank(self):
        assert lattice_rank("A1") == 1

    def test_a2_rank(self):
        assert lattice_rank("A2") == 2

    def test_d4_rank(self):
        assert lattice_rank("D4") == 4

    def test_e8_rank(self):
        assert lattice_rank("E8") == 8

    def test_a1_determinant(self):
        """det(A₁ Cartan) = 2."""
        assert lattice_determinant("A1") == 2

    def test_a2_determinant(self):
        """det(A₂ Cartan) = 3."""
        assert lattice_determinant("A2") == 3

    def test_a3_determinant(self):
        """det(A₃ Cartan) = 4."""
        assert lattice_determinant("A3") == 4

    def test_d4_determinant(self):
        """det(D₄ Cartan) = 4."""
        assert lattice_determinant("D4") == 4

    def test_d5_determinant(self):
        """det(D₅ Cartan) = 4."""
        assert lattice_determinant("D5") == 4

    def test_e6_determinant(self):
        """det(E₆ Cartan) = 3."""
        assert lattice_determinant("E6") == 3

    def test_e7_determinant(self):
        """det(E₇ Cartan) = 2."""
        assert lattice_determinant("E7") == 2

    def test_e8_determinant(self):
        """det(E₈ Cartan) = 1 (unimodular)."""
        assert lattice_determinant("E8") == 1

    def test_e8_unimodular(self):
        """E₈ is the unique rank-8 even unimodular lattice."""
        assert is_unimodular("E8")

    def test_a1_not_unimodular(self):
        assert not is_unimodular("A1")

    def test_a2_not_unimodular(self):
        assert not is_unimodular("A2")

    def test_d4_not_unimodular(self):
        assert not is_unimodular("D4")

    def test_positive_definite(self):
        """All root lattice Gram matrices are positive definite."""
        for lt in CARTAN_MATRICES:
            gram = get_gram_matrix(lt)
            eigenvalues = np.linalg.eigvalsh(gram)
            assert all(ev > 0 for ev in eigenvalues), \
                f"{lt} Gram matrix not positive definite"

    def test_even(self):
        """All root lattice Gram matrices are even (diagonal entries are 2)."""
        for lt in CARTAN_MATRICES:
            gram = get_gram_matrix(lt)
            for i in range(gram.shape[0]):
                assert gram[i, i] % 2 == 0, \
                    f"{lt} has odd diagonal entry at ({i},{i})"

    def test_symmetric(self):
        """All Gram matrices are symmetric."""
        for lt in CARTAN_MATRICES:
            gram = get_gram_matrix(lt)
            np.testing.assert_array_equal(gram, gram.T)


# =========================================================================
# Fock space dimension tests
# =========================================================================

class TestFockSpace:
    """Test oscillator Fock space partition function."""

    def test_rank1_weight0(self):
        """Rank 1 Fock space at weight 0: 1 state (vacuum)."""
        assert fock_dim_at_weight(1, 0) == 1

    def test_rank1_weight1(self):
        """Rank 1 at weight 1: 1 state (a_{-1}|0>)."""
        assert fock_dim_at_weight(1, 1) == 1

    def test_rank1_weight2(self):
        """Rank 1 at weight 2: 2 states (a_{-2}|0>, a_{-1}^2|0>)."""
        assert fock_dim_at_weight(1, 2) == 2

    def test_rank1_weight3(self):
        """Rank 1 at weight 3: 3 states = p(3)."""
        assert fock_dim_at_weight(1, 3) == 3

    def test_rank1_weight4(self):
        """Rank 1 at weight 4: 5 states = p(4)."""
        assert fock_dim_at_weight(1, 4) == 5

    def test_rank1_weight5(self):
        """Rank 1 at weight 5: 7 states = p(5)."""
        assert fock_dim_at_weight(1, 5) == 7

    def test_rank2_weight0(self):
        """Rank 2 at weight 0: 1 state."""
        assert fock_dim_at_weight(2, 0) == 1

    def test_rank2_weight1(self):
        """Rank 2 at weight 1: 2 states (a^1_{-1}|0>, a^2_{-1}|0>)."""
        assert fock_dim_at_weight(2, 1) == 2

    def test_rank2_weight2(self):
        """Rank 2 at weight 2: 5 states.

        a^i_{-2}|0> (2 states) + a^i_{-1}a^j_{-1}|0> (3 states: i<=j).
        Total: 2 + 3 = 5.
        """
        # Character of rank-2 Fock space: prod_{n>=1} 1/(1-q^n)^2
        # q^0: 1, q^1: 2, q^2: 2+3=5 (partitions of 2 with 2 colors)
        assert fock_dim_at_weight(2, 2) == 5

    def test_negative_weight(self):
        """Negative weight gives 0 states."""
        assert fock_dim_at_weight(1, -1) == 0
        assert fock_dim_at_weight(3, -5) == 0


# =========================================================================
# A₁ lattice sector dimension tests
# =========================================================================

class TestA1SectorDimensions:
    """Test bar complex sector dimensions for A₁ root lattice."""

    def setup_method(self):
        self.gram = get_gram_matrix("A1")
        self.data = {"gram_matrix": self.gram, "rank": 1}

    def test_zero_sector_bar_degree_1(self):
        """Zero sector at bar degree 1: e^0 = identity (weight 0).

        dim B^1(V_Λ)_{0, w=0} = dim(Fock at weight 0) = 1.
        """
        dims = lattice_bar_sector_dimension(self.data, np.array([0]), max_degree=1)
        # Bar degree 1, weight 0: the vacuum sector
        assert 0 in dims[1]
        assert dims[1][0] == 1

    def test_alpha_sector_bar_degree_1(self):
        """Alpha sector at bar degree 1: e^{alpha_1} has weight |alpha_1|^2/2 = 1.

        dim B^1(V_Λ)_{alpha_1, w=1} = dim(Fock at weight 0) = 1.
        """
        dims = lattice_bar_sector_dimension(self.data, np.array([1]), max_degree=1)
        # Sector weight = |alpha_1|^2/2 = 2/2 = 1
        assert 1 in dims[1]
        assert dims[1][1] == 1

    def test_2alpha_sector_bar_degree_1(self):
        """2*alpha sector: weight = |2*alpha_1|^2/2 = 4.

        dim B^1(V_Λ)_{2alpha_1, w=4} = 1 (just the vertex operator).
        """
        dims = lattice_bar_sector_dimension(self.data, np.array([2]), max_degree=1)
        assert 4 in dims[1]
        assert dims[1][4] == 1

    def test_zero_sector_bar_degree_2(self):
        """Zero sector at bar degree 2 has finite dimensions.

        At weight w, counts pairs (alpha, -alpha) with |alpha|^2/2 + oscillators = w.
        """
        dims = lattice_bar_sector_dimension(self.data, np.array([0]), max_degree=2)
        # Should have entries at various weights, all finite
        for w, d in dims[2].items():
            assert d > 0
            assert d < 10000  # sanity bound

    def test_all_dimensions_finite(self):
        """All computed sector dimensions are finite and non-negative."""
        for sector in [[0], [1], [-1], [2]]:
            dims = lattice_bar_sector_dimension(
                self.data, np.array(sector), max_degree=3
            )
            for n, wd in dims.items():
                for w, d in wd.items():
                    assert d >= 0, f"Negative dimension at sector {sector}, n={n}, w={w}"
                    assert math.isfinite(d), f"Infinite dimension at sector {sector}, n={n}, w={w}"


# =========================================================================
# A₂ lattice sector dimension tests
# =========================================================================

class TestA2SectorDimensions:
    """Test bar complex sector dimensions for A₂ root lattice.

    A₂ has 2 nontrivial sectors (det = 3, so 3 cosets of Λ*/Λ).
    The fundamental weights omega_1, omega_2 represent the nontrivial cosets.
    In simple root coordinates: omega_1 = (2/3, 1/3), omega_2 = (1/3, 2/3).
    Since we work on the root lattice, the sectors are labeled by
    lattice vectors modulo 3.
    """

    def setup_method(self):
        self.gram = get_gram_matrix("A2")
        self.data = {"gram_matrix": self.gram, "rank": 2}

    def test_zero_sector_bar1(self):
        """Zero sector at bar degree 1."""
        dims = lattice_bar_sector_dimension(
            self.data, np.array([0, 0]), max_degree=1
        )
        assert 0 in dims[1]
        assert dims[1][0] == 1  # vacuum

    def test_simple_root_sector(self):
        """alpha_1 sector: weight = |alpha_1|^2/2 = 1."""
        dims = lattice_bar_sector_dimension(
            self.data, np.array([1, 0]), max_degree=1
        )
        assert 1 in dims[1]
        assert dims[1][1] == 1

    def test_sum_sector(self):
        """alpha_1 + alpha_2 sector: weight = |alpha_1 + alpha_2|^2/2.

        |alpha_1 + alpha_2|^2 = 2 + 2*(-1) + 2 = 2, so weight = 1.
        """
        dims = lattice_bar_sector_dimension(
            self.data, np.array([1, 1]), max_degree=1
        )
        assert 1 in dims[1]
        assert dims[1][1] == 1

    def test_bar_degree_2_finite(self):
        """Bar degree 2 dimensions are finite in all sectors."""
        for sector in [[0, 0], [1, 0], [0, 1], [1, 1]]:
            dims = lattice_bar_sector_dimension(
                self.data, np.array(sector), max_degree=2
            )
            for w, d in dims.get(2, {}).items():
                assert d >= 0
                assert math.isfinite(d)


# =========================================================================
# Sectorwise finiteness tests
# =========================================================================

@pytest.mark.slow
class TestSectorwiseFiniteness:
    """Test sectorwise finiteness verification for various lattices.

    These tests involve computing lattice theta functions over coset
    sectors at multiple bar degrees, which is expensive for rank ≥ 4.
    """

    def test_a1_sectorwise_finite(self):
        """A₁ root lattice: sectorwise finite."""
        gram = get_gram_matrix("A1")
        result = sectorwise_finiteness_check(gram, max_sectors=5)
        assert result["is_finite"]
        assert result["is_positive_definite"]
        assert result["is_even"]

    def test_a2_sectorwise_finite(self):
        """A₂ root lattice: sectorwise finite."""
        gram = get_gram_matrix("A2")
        result = sectorwise_finiteness_check(gram, max_sectors=5)
        assert result["is_finite"]
        assert result["determinant"] == 3

    def test_d4_sectorwise_finite(self):
        """D₄ root lattice: sectorwise finite."""
        gram = get_gram_matrix("D4")
        result = sectorwise_finiteness_check(gram, max_sectors=5)
        assert result["is_finite"]
        assert result["determinant"] == 4

    def test_e8_sectorwise_finite(self):
        """E₈ root lattice: sectorwise finite (and unimodular)."""
        gram = get_gram_matrix("E8")
        result = sectorwise_finiteness_check(gram, max_sectors=3, max_degree=2)
        assert result["is_finite"]
        assert result["determinant"] == 1

    def test_non_positive_definite_fails(self):
        """A non-positive-definite matrix should fail finiteness."""
        bad_gram = np.array([[2, -3], [-3, 2]])  # det = -5 < 0
        result = sectorwise_finiteness_check(bad_gram, max_sectors=3)
        assert not result["is_finite"]
        assert "not positive definite" in result.get("reason", "").lower() or not result["is_finite"]

    def test_all_simply_laced_finite(self):
        """All simply-laced root lattices in the database are sectorwise finite."""
        for lt in CARTAN_MATRICES:
            gram = get_gram_matrix(lt)
            result = sectorwise_finiteness_check(gram, max_sectors=3, max_degree=2)
            assert result["is_finite"], f"Finiteness failed for {lt}"

    def test_sectors_have_nonneg_weight(self):
        """All sectors have non-negative conformal weight."""
        for lt in ["A1", "A2", "D4"]:
            gram = get_gram_matrix(lt)
            result = sectorwise_finiteness_check(gram, max_sectors=5)
            for sc in result["sectors_checked"]:
                assert sc["sector_weight"] >= -1e-10, \
                    f"Negative sector weight in {lt}: {sc}"


# =========================================================================
# E₁ growth rate tests
# =========================================================================

class TestE1GrowthRate:
    """Test E₁ growth rate computation and fitting."""

    def test_sl2_growth_rate(self):
        """sl₂ growth rate: C = π/√12 ≈ 0.9069."""
        result = e1_growth_rate("A1", 1, max_weight=30)
        assert result["rank"] == 1
        expected_C = math.pi / math.sqrt(12)
        assert abs(result["C_theory"] - expected_C) < 1e-10

    def test_sl3_growth_rate(self):
        """sl₃ growth rate: C = π/√6 ≈ 1.2825."""
        result = e1_growth_rate("A2", 2, max_weight=30)
        assert result["rank"] == 2
        expected_C = math.pi / math.sqrt(6)
        assert abs(result["C_theory"] - expected_C) < 1e-10

    def test_sl4_growth_rate(self):
        """sl₄ growth rate: C = π/2 ≈ 1.5708."""
        result = e1_growth_rate("A3", 3, max_weight=30)
        assert result["rank"] == 3
        expected_C = math.pi / 2
        assert abs(result["C_theory"] - expected_C) < 1e-10

    def test_growth_dimensions_match_lqt(self):
        """E₁ dimensions from growth_rate match lqt_e1_growth module."""
        for lt, r in [("A1", 1), ("A2", 2), ("A3", 3)]:
            result = e1_growth_rate(lt, r, max_weight=20)
            lqt_dims = e1_dimensions(lt, 20)
            assert result["dimensions"] == lqt_dims

    def test_growth_is_converging(self):
        """Growth constant fit is converging for all tested algebras."""
        for lt, r in [("A1", 1), ("A2", 2), ("A3", 3)]:
            result = e1_growth_rate(lt, r, max_weight=30)
            assert result["is_converging"], \
                f"Growth not converging for {lt}"

    def test_rank_mismatch_raises(self):
        """Providing wrong rank raises an assertion error."""
        with pytest.raises(AssertionError):
            e1_growth_rate("A1", 2)  # A1 has rank 1, not 2

    def test_higher_rank_larger_growth(self):
        """Higher rank gives larger growth constant."""
        r1 = e1_growth_rate("A1", 1, max_weight=20)
        r2 = e1_growth_rate("A2", 2, max_weight=20)
        r3 = e1_growth_rate("A3", 3, max_weight=20)
        assert r1["C_theory"] < r2["C_theory"] < r3["C_theory"]


# =========================================================================
# Sub-exponential growth tests
# =========================================================================

class TestSubExponentialGrowth:
    """Test sub-exponential growth verification."""

    def test_sl2_subexponential(self):
        """sl₂ E₁ dimensions grow sub-exponentially."""
        dims = e1_dimensions("A1", 100)
        result = sub_exponential_growth_test(dims)
        assert result["is_sub_exponential"]

    def test_sl3_subexponential(self):
        """sl₃ E₁ dimensions grow sub-exponentially."""
        dims = e1_dimensions("A2", 100)
        result = sub_exponential_growth_test(dims)
        assert result["is_sub_exponential"]

    def test_sl4_subexponential(self):
        """sl₄ E₁ dimensions grow sub-exponentially."""
        dims = e1_dimensions("A3", 100)
        result = sub_exponential_growth_test(dims)
        assert result["is_sub_exponential"]

    def test_d4_subexponential(self):
        """D₄ E₁ dimensions grow sub-exponentially."""
        dims = e1_dimensions("D4", 100)
        result = sub_exponential_growth_test(dims)
        assert result["is_sub_exponential"]

    def test_e8_subexponential(self):
        """E₈ E₁ dimensions grow sub-exponentially.

        E₈ has rank 8, so the LQT growth exp(π√(8n/12)) has a large
        constant.  At n≤100 the √n curvature is not yet visible and the
        fit-based discriminator needs more data (n≥200) to correctly
        identify the sub-exponential regime.
        """
        dims = e1_dimensions("E8", 200)
        result = sub_exponential_growth_test(dims)
        assert result["is_sub_exponential"]

    def test_exponential_sequence_detected(self):
        """An exponentially growing sequence is NOT sub-exponential."""
        # 2^n grows exponentially
        exp_dims = [2 ** n for n in range(50)]
        result = sub_exponential_growth_test(exp_dims)
        assert not result["is_sub_exponential"]

    def test_polynomial_sequence_is_subexponential(self):
        """A polynomially growing sequence IS sub-exponential."""
        poly_dims = [n ** 3 + 1 for n in range(50)]
        result = sub_exponential_growth_test(poly_dims)
        assert result["is_sub_exponential"]

    def test_constant_sequence(self):
        """A constant sequence is sub-exponential."""
        const_dims = [5] * 50
        result = sub_exponential_growth_test(const_dims)
        assert result["is_sub_exponential"]

    def test_super_polynomial_detection(self):
        """E₁ dimensions grow super-polynomially (faster than any polynomial)."""
        dims = e1_dimensions("A2", 100)
        result = sub_exponential_growth_test(dims)
        # Sub-exponential but super-polynomial: the LQT regime
        assert result["is_sub_exponential"]
        assert result["is_super_polynomial"]

    def test_short_sequence_trivial(self):
        """Short sequences are trivially sub-exponential."""
        result = sub_exponential_growth_test([1, 2, 3])
        assert result["is_sub_exponential"]


# =========================================================================
# LQT asymptotic comparison tests
# =========================================================================

class TestLQTAsymptoticComparison:
    """Test comparison of computed E₁ dims with LQT asymptotic formula."""

    def test_sl2_asymptotic(self):
        """sl₂ LQT asymptotic comparison runs without error."""
        result = lqt_asymptotic_comparison("A1", 1, max_weight=30)
        assert result["rank"] == 1
        assert len(result["comparisons"]) > 0
        # Growth constant should be pi*sqrt(1/12)
        assert abs(result["C_growth"] - math.pi * math.sqrt(1 / 12)) < 1e-10

    def test_sl3_asymptotic(self):
        """sl₃ LQT asymptotic comparison."""
        result = lqt_asymptotic_comparison("A2", 2, max_weight=30)
        assert result["rank"] == 2
        assert len(result["comparisons"]) > 0

    def test_sl4_asymptotic(self):
        """sl₄ LQT asymptotic comparison."""
        result = lqt_asymptotic_comparison("A3", 3, max_weight=30)
        assert result["rank"] == 3
        assert len(result["comparisons"]) > 0

    def test_ratios_positive(self):
        """All asymptotic ratios are positive."""
        for lt, r in [("A1", 1), ("A2", 2), ("A3", 3)]:
            result = lqt_asymptotic_comparison(lt, r, max_weight=30)
            for c in result["comparisons"]:
                assert c["ratio"] > 0, \
                    f"Non-positive ratio at p={c['p']} for {lt}"

    def test_growth_constant_correct(self):
        """Growth constant C_g = pi*sqrt(r/12) for all tested types."""
        for lt, r in [("A1", 1), ("A2", 2), ("A3", 3), ("D4", 4)]:
            result = lqt_asymptotic_comparison(lt, r, max_weight=20)
            expected = math.pi * math.sqrt(r / 12.0)
            assert abs(result["C_growth"] - expected) < 1e-10, \
                f"Wrong C_growth for {lt}"

    @pytest.mark.slow
    def test_sl2_asymptotic_stabilizing(self):
        """sl₂ ratios stabilize at large p (convergence to C(g))."""
        result = lqt_asymptotic_comparison("A1", 1, max_weight=200)
        assert result["is_stabilizing"]

    @pytest.mark.slow
    def test_sl3_asymptotic_stabilizing(self):
        """sl₃ ratios stabilize at large p."""
        result = lqt_asymptotic_comparison("A2", 2, max_weight=200)
        assert result["is_stabilizing"]


# =========================================================================
# Lattice factorization DK verification tests
# =========================================================================

@pytest.mark.slow
class TestLatticeFactorizationDK:
    """Test factorization DK verification for lattice VOAs."""

    def test_a1_dk(self):
        """A₁ lattice DK verification."""
        gram = get_gram_matrix("A1")
        result = lattice_factorization_dk_verification(gram, max_sectors=3)
        assert result["sectorwise_finite"]
        assert result["num_cosets"] == 2
        assert not result["is_unimodular"]
        assert result["weights_nonneg"]
        assert result["zero_weight_ok"]

    def test_a2_dk(self):
        """A₂ lattice DK verification."""
        gram = get_gram_matrix("A2")
        result = lattice_factorization_dk_verification(gram, max_sectors=5)
        assert result["sectorwise_finite"]
        assert result["num_cosets"] == 3
        assert result["zero_weight_ok"]

    def test_d4_dk(self):
        """D₄ lattice DK verification."""
        gram = get_gram_matrix("D4")
        result = lattice_factorization_dk_verification(gram, max_sectors=5)
        assert result["sectorwise_finite"]
        assert result["num_cosets"] == 4

    def test_e8_dk(self):
        """E₈ lattice DK verification (unimodular, single sector)."""
        gram = get_gram_matrix("E8")
        result = lattice_factorization_dk_verification(gram, max_sectors=3)
        assert result["sectorwise_finite"]
        assert result["num_cosets"] == 1
        assert result["is_unimodular"]


# =========================================================================
# Simply-laced level 1 tests
# =========================================================================

@pytest.mark.slow
class TestSimplyLacedLevel1:
    """Test simply-laced level-1 DK unconditional verification."""

    def test_a1_level1(self):
        """A₁ at level 1: det = 2, 2 cosets."""
        result = simply_laced_level1_check("A1", 1)
        assert result["is_simply_laced"]
        assert result["lattice_determinant"] == 2
        assert result["num_cosets"] == 2
        assert result["determinant_matches"]
        assert result["dk_unconditional"]

    def test_a2_level1(self):
        """A₂ at level 1: det = 3, 3 cosets (fund. reps)."""
        result = simply_laced_level1_check("A2", 2)
        assert result["lattice_determinant"] == 3
        assert result["num_cosets"] == 3
        assert result["determinant_matches"]
        assert result["dk_unconditional"]

    def test_d4_level1(self):
        """D₄ at level 1: det = 4, 4 cosets (id, vector, spinor+, spinor-)."""
        result = simply_laced_level1_check("D4", 4)
        assert result["lattice_determinant"] == 4
        assert result["num_cosets"] == 4
        assert result["determinant_matches"]
        assert result["dk_unconditional"]

    def test_e8_level1(self):
        """E₈ at level 1: det = 1, unimodular, single sector, self-dual."""
        result = simply_laced_level1_check("E8", 8)
        assert result["lattice_determinant"] == 1
        assert result["is_unimodular"]
        assert result["num_cosets"] == 1
        assert result["determinant_matches"]
        assert result["dk_unconditional"]

    def test_e6_level1(self):
        """E₆ at level 1: det = 3."""
        result = simply_laced_level1_check("E6", 6)
        assert result["lattice_determinant"] == 3
        assert result["dk_unconditional"]

    def test_e7_level1(self):
        """E₇ at level 1: det = 2."""
        result = simply_laced_level1_check("E7", 7)
        assert result["lattice_determinant"] == 2
        assert result["dk_unconditional"]

    def test_all_positive_definite(self):
        """All level-1 lattices are positive definite."""
        for lt, r in [("A1", 1), ("A2", 2), ("A3", 3), ("D4", 4),
                       ("D5", 5), ("E6", 6), ("E7", 7), ("E8", 8)]:
            result = simply_laced_level1_check(lt, r)
            assert result["positive_definite"], f"{lt} not positive definite"

    def test_all_dk_unconditional(self):
        """Factorization DK is unconditional for all simply-laced level-1 VOAs."""
        for lt, r in [("A1", 1), ("A2", 2), ("A3", 3), ("D4", 4),
                       ("D5", 5), ("E6", 6), ("E7", 7), ("E8", 8)]:
            result = simply_laced_level1_check(lt, r)
            assert result["dk_unconditional"], \
                f"DK not unconditional for {lt} at level 1"

    def test_rank_mismatch_detected(self):
        """Wrong rank is detected."""
        result = simply_laced_level1_check("A1", 3)
        assert not result.get("dk_unconditional", False)

    def test_central_charge_a1(self):
        """A₁ at level 1: c = 3/(1+2) = 1."""
        result = simply_laced_level1_check("A1", 1)
        assert result["central_charge_level1"] == pytest.approx(1.0)

    def test_central_charge_e8(self):
        """E₈ at level 1: c = 248/(1+30) = 248/31 = 8."""
        result = simply_laced_level1_check("E8", 8)
        assert result["central_charge_level1"] == pytest.approx(248 / 31)

    def test_dim_e8(self):
        """dim(E₈) = 248."""
        result = simply_laced_level1_check("E8", 8)
        assert result["dim_g"] == 248


# =========================================================================
# Cross-cutting integration tests
# =========================================================================

@pytest.mark.slow
class TestIntegration:
    """Integration tests combining multiple components.

    Calls sectorwise_finiteness_check and lattice_factorization_dk_verification,
    which are expensive for rank ≥ 4.
    """

    def test_finiteness_implies_dk(self):
        """Sectorwise finiteness implies DK is unconditional."""
        for lt in ["A1", "A2", "D4"]:
            gram = get_gram_matrix(lt)
            finite = sectorwise_finiteness_check(gram, max_sectors=3)
            dk = lattice_factorization_dk_verification(gram, max_sectors=3)
            if finite["is_finite"]:
                assert dk["sectorwise_finite"]

    def test_growth_rate_vs_finiteness(self):
        """Sub-exponential growth and sectorwise finiteness are consistent.

        For lattice VOAs, both must hold simultaneously.
        """
        for lt in ["A1", "A2", "D4"]:
            gram = get_gram_matrix(lt)
            finite = sectorwise_finiteness_check(gram, max_sectors=3, max_degree=2)
            assert finite["is_finite"]

            dims = e1_dimensions(lt, 50)
            growth = sub_exponential_growth_test(dims)
            assert growth["is_sub_exponential"]

    def test_unimodular_has_one_sector(self):
        """Unimodular lattices (E₈) have exactly one coset sector."""
        result = simply_laced_level1_check("E8", 8)
        assert result["is_unimodular"]
        assert result["num_cosets"] == 1

    def test_nonunimodular_has_multiple_sectors(self):
        """Non-unimodular lattices have multiple coset sectors."""
        for lt, r, expected_cosets in [("A1", 1, 2), ("A2", 2, 3), ("D4", 4, 4)]:
            result = simply_laced_level1_check(lt, r)
            assert not result["is_unimodular"]
            assert result["num_cosets"] == expected_cosets
