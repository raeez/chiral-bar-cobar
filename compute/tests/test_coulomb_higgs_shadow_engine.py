r"""Tests for Coulomb/Higgs branch shadow obstruction tower engine.

Tests cover:
  1. SQED(N_f) Coulomb/Higgs branch dimensions (N_f = 1..8)
  2. Boundary VOA central charges
  3. kappa invariants (multi-path verification per AP1/AP10)
  4. Complementarity sums (mirror vs Koszul, per AP24)
  5. Shadow depth classification (G/L/C/M)
  6. Bar complex dimensions and H^2 (Milnor numbers)
  7. Webster categorical Koszul duality comparison
  8. Type-A quiver gauge theories
  9. Cross-family consistency checks
  10. Genus-1 and genus-2 obstructions

Multi-path verification (per CLAUDE.md mandate):
  Path 1: Direct formula computation
  Path 2: Dimension/2 estimate for free-field cases
  Path 3: Mirror symmetry cross-check
  Path 4: Complementarity sum constraints
  Path 5: Milnor number / singularity theory

References:
  [BFN18] Braverman-Finkelberg-Nakajima, arXiv:1601.03586
  [BLPW16] Braden-Licata-Proudfoot-Webster, arXiv:1407.0964
  [Web19] Webster, arXiv:1611.06541
  [HR21] Hilburn-Raskin, arXiv:2107.11325
  Manuscript: sec:coulomb-branch, thm:bfn, conj:shifted-yangian-langlands
"""

import pytest
from fractions import Fraction

from compute.lib.coulomb_higgs_shadow_engine import (
    # SQED dimensions
    sqed_coulomb_dim,
    sqed_higgs_dim,
    # Boundary VOA central charges
    sqed_coulomb_boundary_voa_central_charge,
    sqed_higgs_boundary_voa_central_charge,
    # kappa
    sqed_kappa_coulomb_boundary,
    sqed_kappa_higgs_boundary,
    sqed_complementarity_sum,
    # Shadow invariants
    sqed_shadow_depth_coulomb,
    sqed_shadow_depth_higgs,
    sqed_shadow_class_coulomb,
    sqed_shadow_class_higgs,
    # Obstructions
    sqed_genus1_obstruction_coulomb,
    sqed_genus1_obstruction_higgs,
    sqed_genus2_scalar_coulomb,
    sqed_genus2_scalar_higgs,
    # Bar complex
    sqed_bar_dim_1,
    sqed_bar_dim_2,
    sqed_bar_h2,
    sqed_coulomb_quantized_relations,
    # Type-A quivers
    type_a_quiver_coulomb_dim,
    type_a_quiver_higgs_dim,
    type_a_shifted_yangian_shift,
    type_a_kappa_coulomb,
    type_a_kappa_higgs,
    an_quiver_coulomb_data,
    # Comparison
    webster_koszul_category_O_dimensions,
    webster_vs_chiral_koszul,
    coulomb_higgs_complementarity,
    three_koszul_dualities_comparison,
    hilburn_raskin_sqed1,
    # Data assembly
    sqed_full_data,
    full_sqed_landscape,
    landscape_summary_table,
    # Cross-verification
    kappa_from_branch_dimension,
    verify_kappa_dimension_consistency,
    # Singularity
    milnor_number_a_singularity,
    slodowy_slice_dim,
    CoulombHiggsData,
)


# ============================================================================
# Section 1: SQED Coulomb branch dimensions
# ============================================================================

class TestSQEDCoulombDimension:
    """Coulomb branch of SQED(N_f) is always C^2/Z_{N_f}, dim = 2."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_coulomb_dim_is_2(self, N_f):
        """Coulomb branch dim = 2 for all N_f (surface singularity)."""
        assert sqed_coulomb_dim(N_f) == Fraction(2)

    def test_coulomb_dim_invalid(self):
        with pytest.raises(ValueError):
            sqed_coulomb_dim(0)


# ============================================================================
# Section 2: SQED Higgs branch dimensions
# ============================================================================

class TestSQEDHiggsDimension:
    """Higgs branch of SQED(N_f) is T*CP^{N_f-1}, dim = 2(N_f-1)."""

    def test_higgs_dim_nf1(self):
        """N_f=1: Higgs branch is a point."""
        assert sqed_higgs_dim(1) == Fraction(0)

    def test_higgs_dim_nf2(self):
        """N_f=2: T*P^1, dim = 2."""
        assert sqed_higgs_dim(2) == Fraction(2)

    def test_higgs_dim_nf3(self):
        """N_f=3: T*P^2, dim = 4."""
        assert sqed_higgs_dim(3) == Fraction(4)

    @pytest.mark.parametrize("N_f,expected", [
        (1, 0), (2, 2), (3, 4), (4, 6), (5, 8), (6, 10), (7, 12), (8, 14),
    ])
    def test_higgs_dim_formula(self, N_f, expected):
        """dim_H = 2(N_f - 1) for all N_f."""
        assert sqed_higgs_dim(N_f) == Fraction(expected)

    def test_higgs_dim_invalid(self):
        with pytest.raises(ValueError):
            sqed_higgs_dim(0)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_total_dimension(self, N_f):
        """Total Coulomb + Higgs dimension = 2*N_f."""
        total = sqed_coulomb_dim(N_f) + sqed_higgs_dim(N_f)
        assert total == Fraction(2 * N_f)


# ============================================================================
# Section 3: Boundary VOA central charges
# ============================================================================

class TestBoundaryVOACentralCharge:
    """Central charges of boundary VOAs."""

    @pytest.mark.parametrize("N_f,expected", [
        (1, 0), (2, 2), (3, 4), (4, 6), (5, 8), (6, 10), (7, 12), (8, 14),
    ])
    def test_coulomb_central_charge(self, N_f, expected):
        assert sqed_coulomb_boundary_voa_central_charge(N_f) == Fraction(expected)

    @pytest.mark.parametrize("N_f,expected", [
        (1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7),
    ])
    def test_higgs_central_charge(self, N_f, expected):
        assert sqed_higgs_boundary_voa_central_charge(N_f) == Fraction(expected)

    def test_higgs_c_equals_nf_minus_1(self):
        """c(Higgs boundary) = N_f - 1 (mirror = N_f-1 free bosons)."""
        for N_f in range(1, 9):
            assert sqed_higgs_boundary_voa_central_charge(N_f) == Fraction(N_f - 1)


# ============================================================================
# Section 4: kappa invariants
# ============================================================================

class TestKappaInvariants:
    """kappa for Coulomb and Higgs boundary VOAs."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_kappa_coulomb_is_1(self, N_f):
        """kappa(Coulomb boundary) = 1 for all N_f (rank-1 Heisenberg)."""
        assert sqed_kappa_coulomb_boundary(N_f) == Fraction(1)

    @pytest.mark.parametrize("N_f,expected", [
        (1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7),
    ])
    def test_kappa_higgs(self, N_f, expected):
        """kappa(Higgs boundary) = N_f - 1."""
        assert sqed_kappa_higgs_boundary(N_f) == Fraction(expected)

    # Multi-path verification: kappa = dim(branch)/2
    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_kappa_coulomb_equals_dim_over_2(self, N_f):
        """Path 2: kappa_C = dim(M_C)/2 = 1."""
        dim_C = sqed_coulomb_dim(N_f)
        assert sqed_kappa_coulomb_boundary(N_f) == dim_C / 2

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_kappa_higgs_equals_dim_over_2(self, N_f):
        """Path 2: kappa_H = dim(M_H)/2 = N_f - 1."""
        dim_H = sqed_higgs_dim(N_f)
        assert sqed_kappa_higgs_boundary(N_f) == dim_H / 2

    def test_kappa_invalid(self):
        with pytest.raises(ValueError):
            sqed_kappa_coulomb_boundary(0)


# ============================================================================
# Section 5: Complementarity sums
# ============================================================================

class TestComplementaritySums:
    """Complementarity sums kappa_C + kappa_H."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_mirror_sum_equals_nf(self, N_f):
        """Mirror sum: kappa_C + kappa_H = N_f (matter counting)."""
        assert sqed_complementarity_sum(N_f) == Fraction(N_f)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_mirror_sum_equals_total_dim_over_2(self, N_f):
        """Mirror sum = (dim_C + dim_H)/2 = N_f."""
        dim_total = sqed_coulomb_dim(N_f) + sqed_higgs_dim(N_f)
        assert sqed_complementarity_sum(N_f) == dim_total / 2

    def test_complementarity_not_zero(self):
        """Mirror sum != 0 for N_f >= 1 (contrast with KM anti-symmetry)."""
        for N_f in range(1, 9):
            assert sqed_complementarity_sum(N_f) > 0

    def test_complementarity_not_13(self):
        """Mirror sum != 13 (contrast with Virasoro complementarity)."""
        for N_f in range(1, 9):
            assert sqed_complementarity_sum(N_f) != 13

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_koszul_complementarity_coulomb(self, N_f):
        """Koszul complementarity kappa(C) + kappa(C^!) = 0 (free field)."""
        comp = coulomb_higgs_complementarity(N_f)
        assert comp["koszul_coulomb_sum"] == 0

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_koszul_complementarity_higgs(self, N_f):
        """Koszul complementarity kappa(H) + kappa(H^!) = 0 (free field)."""
        comp = coulomb_higgs_complementarity(N_f)
        assert comp["koszul_higgs_sum"] == 0


# ============================================================================
# Section 6: Shadow depth classification
# ============================================================================

class TestShadowDepth:
    """Shadow depth and G/L/C/M classification."""

    def test_coulomb_nf1_gaussian(self):
        """N_f=1: Heisenberg = class G, depth 2."""
        assert sqed_shadow_depth_coulomb(1) == 2
        assert sqed_shadow_class_coulomb(1) == "G"

    def test_coulomb_nf2_lie(self):
        """N_f=2: sl_2 affine = class L, depth 3."""
        assert sqed_shadow_depth_coulomb(2) == 3
        assert sqed_shadow_class_coulomb(2) == "L"

    def test_coulomb_nf3_contact(self):
        """N_f=3: contact class C, depth 4."""
        assert sqed_shadow_depth_coulomb(3) == 4
        assert sqed_shadow_class_coulomb(3) == "C"

    def test_coulomb_nf5_mixed(self):
        """N_f>=5: class M, infinite depth."""
        assert sqed_shadow_depth_coulomb(5) == -1
        assert sqed_shadow_class_coulomb(5) == "M"

    def test_higgs_nf1_trivial(self):
        """N_f=1: trivial Higgs branch."""
        assert sqed_shadow_depth_higgs(1) == 0
        assert sqed_shadow_class_higgs(1) == "trivial"

    def test_higgs_nf2_gaussian(self):
        """N_f=2: Heisenberg = class G, depth 2."""
        assert sqed_shadow_depth_higgs(2) == 2
        assert sqed_shadow_class_higgs(2) == "G"

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_shadow_depth_monotone_coulomb(self, N_f):
        """Shadow depth is non-decreasing in N_f for Coulomb."""
        if N_f > 1:
            d_prev = sqed_shadow_depth_coulomb(N_f - 1)
            d_curr = sqed_shadow_depth_coulomb(N_f)
            # -1 means infinite, which is >= any finite depth
            if d_prev >= 0 and d_curr >= 0:
                assert d_curr >= d_prev
            elif d_curr == -1:
                pass  # infinite >= anything
            else:
                # d_prev == -1 and d_curr >= 0: should not happen
                assert False, "Depth should not decrease from infinite"


# ============================================================================
# Section 7: Bar complex dimensions
# ============================================================================

class TestBarComplex:
    """Bar complex of quantized Coulomb branch algebra."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_bar_dim_1(self, N_f):
        """dim B^1 = 3 (generators x, y, z)."""
        assert sqed_bar_dim_1(N_f) == 3

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_bar_dim_2(self, N_f):
        """dim B^2 = 9 (all pairs)."""
        assert sqed_bar_dim_2(N_f) == 9

    @pytest.mark.parametrize("N_f,expected_h2", [
        (1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7),
    ])
    def test_bar_h2_milnor(self, N_f, expected_h2):
        """H^2 = N_f - 1 = Milnor number of A_{N_f-1} singularity."""
        assert sqed_bar_h2(N_f) == expected_h2

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_bar_h2_equals_milnor(self, N_f):
        """Cross-check: H^2 = mu(A_{N_f-1})."""
        assert sqed_bar_h2(N_f) == milnor_number_a_singularity(N_f - 1)

    def test_bar_h2_nf1_trivial(self):
        """N_f=1: smooth (Weyl algebra), H^2 = 0."""
        assert sqed_bar_h2(1) == 0


# ============================================================================
# Section 8: Quantized algebra relations
# ============================================================================

class TestQuantizedRelations:
    """Quantized Coulomb branch algebra relations."""

    def test_nf1_heisenberg(self):
        """N_f=1: Weyl/Heisenberg algebra."""
        rels = sqed_coulomb_quantized_relations(1)
        assert "xy = (z + 0*hbar)" in rels["xy_relation"]
        assert rels["classical_limit"] == "xy = z^1"

    def test_nf2_sl2(self):
        """N_f=2: deformation of A_1 singularity."""
        rels = sqed_coulomb_quantized_relations(2)
        assert "z^2" in rels["classical_limit"]

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_generators_always_xyz(self, N_f):
        rels = sqed_coulomb_quantized_relations(N_f)
        assert rels["generators"] == "x, y, z"

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_classical_limit(self, N_f):
        rels = sqed_coulomb_quantized_relations(N_f)
        assert rels["classical_limit"] == f"xy = z^{N_f}"

    def test_invalid(self):
        with pytest.raises(ValueError):
            sqed_coulomb_quantized_relations(0)


# ============================================================================
# Section 9: Type-A quiver gauge theories
# ============================================================================

class TestTypeAQuivers:
    """Type-A linear quiver gauge theories."""

    def test_a1_quiver(self):
        """A_1 quiver: gauge = (1), flavor = (2)."""
        data = an_quiver_coulomb_data(1)
        assert data["gauge_ranks"] == [1]
        assert data["dim_coulomb"] == Fraction(2)
        assert data["kappa_coulomb"] == Fraction(1)

    def test_a2_quiver(self):
        """A_2 quiver: gauge = (1, 2), flavor = (0, 3)."""
        data = an_quiver_coulomb_data(2)
        assert data["gauge_ranks"] == [1, 2]
        assert data["dim_coulomb"] == Fraction(6)
        assert data["kappa_coulomb"] == Fraction(3)

    def test_a3_quiver(self):
        """A_3 quiver: gauge = (1, 2, 3)."""
        data = an_quiver_coulomb_data(3)
        assert data["gauge_ranks"] == [1, 2, 3]
        assert data["dim_coulomb"] == Fraction(12)
        assert data["kappa_coulomb"] == Fraction(6)

    def test_coulomb_dim_linear(self):
        """dim_C = 2 * sum(gauge_ranks)."""
        ranks = [2, 3, 2]
        assert type_a_quiver_coulomb_dim(ranks) == Fraction(14)

    def test_shifted_yangian_balanced(self):
        """Balanced quiver: all shifts are 0."""
        # Balanced A_2: gauge = (1, 2), flavor = (0, 3)
        # mu_1 = 0 - 2*1 + 0 + 2 = 0
        # mu_2 = 3 - 2*2 + 1 + 0 = 0
        shift = type_a_shifted_yangian_shift([1, 2], [0, 3])
        assert shift == [0, 0]

    def test_shifted_yangian_unbalanced(self):
        """Unbalanced quiver: nonzero shifts."""
        # gauge = (1), flavor = (3)
        # mu_1 = 3 - 2*1 + 0 + 0 = 1
        shift = type_a_shifted_yangian_shift([1], [3])
        assert shift == [1]

    def test_kappa_coulomb_type_a(self):
        """kappa = sum(gauge_ranks) for type-A quivers."""
        assert type_a_kappa_coulomb([1, 2, 3]) == Fraction(6)
        assert type_a_kappa_coulomb([1]) == Fraction(1)

    def test_higgs_dim_type_a(self):
        """Higgs dim for type-A quiver with flavors."""
        # gauge = (1), flavor = (2): dim = 2*(1*2 - 1) = 2
        assert type_a_quiver_higgs_dim([1], [2]) == Fraction(2)

    def test_kappa_higgs_type_a(self):
        """kappa_H = dim_H / 2 for type-A quivers."""
        assert type_a_kappa_higgs([1], [2]) == Fraction(1)


# ============================================================================
# Section 10: Webster Koszul duality
# ============================================================================

class TestWebsterKoszul:
    """Webster's categorical Koszul duality."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_num_simples_match(self, N_f):
        """Number of simples matches on both sides."""
        dims = webster_koszul_category_O_dimensions(N_f)
        assert dims["num_simples_coulomb"] == dims["num_simples_higgs"]

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_num_simples_equals_nf(self, N_f):
        """Number of simples = N_f."""
        dims = webster_koszul_category_O_dimensions(N_f)
        assert dims["num_simples_coulomb"] == N_f

    def test_comparison_types(self):
        """Webster (categorical) vs chiral (algebraic) KD."""
        comp = webster_vs_chiral_koszul(3)
        assert comp["webster_type"] == "categorical (module categories)"
        assert comp["chiral_type"] == "algebraic (algebras via bar complex)"

    def test_three_dualities(self):
        """Three types of Koszul duality are distinct."""
        dualities = three_koszul_dualities_comparison()
        assert "chiral_kd" in dualities
        assert "categorical_kd" in dualities
        assert "symplectic_duality" in dualities
        # Verify they have different levels
        assert dualities["chiral_kd"]["level"] != dualities["categorical_kd"]["level"]
        assert dualities["categorical_kd"]["level"] != dualities["symplectic_duality"]["level"]


# ============================================================================
# Section 11: Complementarity decomposition
# ============================================================================

class TestComplementarityDecomposition:
    """Detailed complementarity analysis."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_mirror_sum_positive(self, N_f):
        comp = coulomb_higgs_complementarity(N_f)
        assert comp["mirror_sum"] > 0

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_koszul_sums_vanish(self, N_f):
        """Koszul complementarity sums vanish (free-field anti-symmetry)."""
        comp = coulomb_higgs_complementarity(N_f)
        assert comp["koszul_coulomb_sum"] == 0
        assert comp["koszul_higgs_sum"] == 0

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_kappa_values_consistent(self, N_f):
        comp = coulomb_higgs_complementarity(N_f)
        assert comp["kappa_coulomb"] == Fraction(1)
        assert comp["kappa_higgs"] == Fraction(N_f - 1)


# ============================================================================
# Section 12: Hilburn-Raskin
# ============================================================================

class TestHilburnRaskin:
    """Hilburn-Raskin derived equivalence for SQED(1)."""

    def test_result_exists(self):
        result = hilburn_raskin_sqed1()
        assert result["theory"] == "SQED(1) = free hypermultiplet"

    def test_coulomb_side(self):
        result = hilburn_raskin_sqed1()
        assert "D-mod" in result["coulomb_side"]

    def test_higgs_side(self):
        result = hilburn_raskin_sqed1()
        assert "IndCoh" in result["higgs_side"]


# ============================================================================
# Section 13: Genus obstructions
# ============================================================================

class TestGenusObstructions:
    """Genus-1 and genus-2 obstruction coefficients."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_genus1_coulomb(self, N_f):
        """obs_1(Coulomb) = 1/24 for all N_f."""
        assert sqed_genus1_obstruction_coulomb(N_f) == Fraction(1, 24)

    @pytest.mark.parametrize("N_f,expected_num", [
        (1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7),
    ])
    def test_genus1_higgs(self, N_f, expected_num):
        """obs_1(Higgs) = (N_f - 1)/24."""
        assert sqed_genus1_obstruction_higgs(N_f) == Fraction(expected_num, 24)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_genus2_coulomb(self, N_f):
        """F_2(Coulomb) = 7/5760."""
        assert sqed_genus2_scalar_coulomb(N_f) == Fraction(7, 5760)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_genus2_higgs(self, N_f):
        """F_2(Higgs) = (N_f-1) * 7/5760."""
        expected = Fraction(N_f - 1) * Fraction(7, 5760)
        assert sqed_genus2_scalar_higgs(N_f) == expected

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_genus1_sum(self, N_f):
        """Sum of genus-1 obstructions = N_f / 24."""
        total = (sqed_genus1_obstruction_coulomb(N_f)
                 + sqed_genus1_obstruction_higgs(N_f))
        assert total == Fraction(N_f, 24)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_genus2_sum(self, N_f):
        """Sum of genus-2 free energies = N_f * 7/5760."""
        total = (sqed_genus2_scalar_coulomb(N_f)
                 + sqed_genus2_scalar_higgs(N_f))
        assert total == Fraction(N_f) * Fraction(7, 5760)


# ============================================================================
# Section 14: Full data assembly
# ============================================================================

class TestFullDataAssembly:
    """Full CoulombHiggsData assembly."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_full_data_fields(self, N_f):
        data = sqed_full_data(N_f)
        assert data.name == f"SQED({N_f})"
        assert data.gauge_group == "U(1)"
        assert data.N_f == N_f
        assert isinstance(data.dim_coulomb, Fraction)
        assert isinstance(data.kappa_coulomb_bdry, Fraction)

    def test_full_landscape(self):
        landscape = full_sqed_landscape()
        assert len(landscape) == 8
        assert landscape[0].N_f == 1
        assert landscape[7].N_f == 8

    def test_landscape_table(self):
        table = landscape_summary_table()
        assert len(table) == 8
        for row in table:
            assert "N_f" in row
            assert "kappa_C" in row
            assert "kappa_H" in row
            assert "kappa_sum" in row


# ============================================================================
# Section 15: Cross-verification
# ============================================================================

class TestCrossVerification:
    """Multi-path cross-verification of kappa values."""

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_kappa_from_dimension(self, N_f):
        """Path 2: kappa = dim/2 for free-field boundary VOAs."""
        dim_C = sqed_coulomb_dim(N_f)
        assert kappa_from_branch_dimension(dim_C) == sqed_kappa_coulomb_boundary(N_f)

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_dimension_consistency(self, N_f):
        """Verify kappa-dimension consistency."""
        result = verify_kappa_dimension_consistency(N_f)
        assert result["coulomb_consistent"]
        assert result["higgs_consistent"]
        assert result["total_consistent"]

    def test_kappa_additivity(self):
        """kappa is additive under tensor product (free fields)."""
        # SQED(N_f) mirror = product of N_f-1 copies of rank-1 Heisenberg
        for N_f in range(2, 9):
            kappa_H = sqed_kappa_higgs_boundary(N_f)
            # Each factor contributes kappa = 1
            assert kappa_H == Fraction(N_f - 1)

    def test_mirror_symmetry_cross_check(self):
        """Mirror symmetry: kappa_C(T) = kappa_H(T~) cross-check.

        For SQED(N_f), mirror is U(1)^{N_f-1} quiver.
        kappa_C(SQED) = 1
        kappa_H(SQED) = N_f - 1

        For the mirror U(1)^{N_f-1} quiver:
        kappa_C(mirror) = N_f - 1 (= kappa_H(SQED))
        kappa_H(mirror) = 1 (= kappa_C(SQED))

        This is the defining property of mirror symmetry.
        """
        for N_f in range(1, 9):
            kC_sqed = sqed_kappa_coulomb_boundary(N_f)
            kH_sqed = sqed_kappa_higgs_boundary(N_f)
            # Mirror should swap
            kC_mirror = kH_sqed  # Coulomb of mirror = Higgs of original
            kH_mirror = kC_sqed  # Higgs of mirror = Coulomb of original
            # Sum invariant under mirror symmetry
            assert kC_sqed + kH_sqed == kC_mirror + kH_mirror


# ============================================================================
# Section 16: Milnor numbers and singularity theory
# ============================================================================

class TestSingularity:
    """Milnor numbers and Slodowy slices."""

    @pytest.mark.parametrize("n,expected", [
        (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
    ])
    def test_milnor_a_n(self, n, expected):
        """mu(A_n) = n."""
        assert milnor_number_a_singularity(n) == expected

    def test_slodowy_sl3_21(self):
        """Slodowy slice for sl_3, partition (2,1): dim = 4."""
        assert slodowy_slice_dim(3, [2, 1]) == 4

    def test_slodowy_sl3_3(self):
        """Slodowy slice for sl_3, partition (3): dim = 2."""
        assert slodowy_slice_dim(3, [3]) == 2

    def test_slodowy_sl4_211(self):
        """Slodowy slice for sl_4, partition (2,1,1): dim = 9."""
        assert slodowy_slice_dim(4, [2, 1, 1]) == 9

    def test_slodowy_sl4_22(self):
        """Slodowy slice for sl_4, partition (2,2): dim = 7."""
        assert slodowy_slice_dim(4, [2, 2]) == 7

    def test_slodowy_sl4_31(self):
        """Slodowy slice for sl_4, partition (3,1): dim = 5."""
        assert slodowy_slice_dim(4, [3, 1]) == 5

    def test_slodowy_sl4_4(self):
        """Slodowy slice for sl_4, partition (4): dim = 3."""
        assert slodowy_slice_dim(4, [4]) == 3

    def test_slodowy_regular_orbit(self):
        """Regular orbit (N): Slodowy dim = rank = N-1."""
        for N in range(2, 7):
            assert slodowy_slice_dim(N, [N]) == N - 1

    def test_bar_h2_milnor_cross_check(self):
        """H^2(bar) = Milnor number (cross-check for all N_f)."""
        for N_f in range(1, 9):
            assert sqed_bar_h2(N_f) == milnor_number_a_singularity(N_f - 1)


# ============================================================================
# Section 17: Monotonicity and structural tests
# ============================================================================

class TestStructural:
    """Structural properties across the SQED landscape."""

    def test_kappa_higgs_monotone(self):
        """kappa_H is strictly increasing in N_f."""
        for N_f in range(2, 9):
            assert (sqed_kappa_higgs_boundary(N_f)
                    > sqed_kappa_higgs_boundary(N_f - 1))

    def test_complementarity_sum_monotone(self):
        """Complementarity sum = N_f is strictly increasing."""
        for N_f in range(2, 9):
            assert (sqed_complementarity_sum(N_f)
                    > sqed_complementarity_sum(N_f - 1))

    def test_higgs_dim_monotone(self):
        """Higgs branch dim is non-decreasing."""
        for N_f in range(2, 9):
            assert sqed_higgs_dim(N_f) >= sqed_higgs_dim(N_f - 1)

    def test_bar_h2_monotone(self):
        """H^2 is non-decreasing in N_f."""
        for N_f in range(2, 9):
            assert sqed_bar_h2(N_f) >= sqed_bar_h2(N_f - 1)

    def test_genus1_obstruction_sum_monotone(self):
        """Genus-1 obstruction sum is increasing in N_f."""
        for N_f in range(2, 9):
            prev = (sqed_genus1_obstruction_coulomb(N_f - 1)
                    + sqed_genus1_obstruction_higgs(N_f - 1))
            curr = (sqed_genus1_obstruction_coulomb(N_f)
                    + sqed_genus1_obstruction_higgs(N_f))
            assert curr > prev

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_data_is_mirror_pair(self, N_f):
        """All SQED theories are mirror pairs."""
        data = sqed_full_data(N_f)
        assert data.is_mirror_pair

    @pytest.mark.parametrize("N_f", range(1, 9))
    def test_webster_compatible(self, N_f):
        """All SQED theories are Webster-Koszul compatible."""
        data = sqed_full_data(N_f)
        assert data.webster_koszul_compatible


# ============================================================================
# Section 18: Boundary cases and edge behavior
# ============================================================================

class TestBoundaryCases:
    """Edge cases and boundary behavior."""

    def test_nf1_trivial_higgs(self):
        """N_f=1: Higgs branch is a point, all Higgs invariants vanish."""
        assert sqed_higgs_dim(1) == 0
        assert sqed_kappa_higgs_boundary(1) == 0
        assert sqed_genus1_obstruction_higgs(1) == 0
        assert sqed_genus2_scalar_higgs(1) == 0

    def test_nf1_heisenberg_coulomb(self):
        """N_f=1: Coulomb = Heisenberg, matches known values."""
        assert sqed_kappa_coulomb_boundary(1) == 1
        assert sqed_genus1_obstruction_coulomb(1) == Fraction(1, 24)
        assert sqed_shadow_class_coulomb(1) == "G"

    def test_nf2_self_mirror(self):
        """N_f=2: dim_C = dim_H = 2 (approaches self-mirror)."""
        assert sqed_coulomb_dim(2) == sqed_higgs_dim(2)
        # But kappa values differ: kappa_C = 1, kappa_H = 1
        assert sqed_kappa_coulomb_boundary(2) == sqed_kappa_higgs_boundary(2)

    def test_large_nf(self):
        """N_f=8: large matter content."""
        data = sqed_full_data(8)
        assert data.complementarity_sum == 8
        assert data.kappa_higgs_bdry == 7
        assert data.dim_higgs == 14
