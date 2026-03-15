"""Tests for sl_3 Baxter TQ relation at K_0 level — task B4 for MC3 path.

Tests verify:
  1. sl_3 root data: simple roots, positive roots, Cartan matrix, Weyl group
  2. Kostant partition function: basic values, edge cases
  3. Finite-dim characters: V(1,0), V(0,1), V(1,1), V(2,0), V(0,2), Freudenthal
  4. Verma module characters: highest weight, multiplicities, Kostant formula
  5. TQ identity (standard): [V_{omega_1}][M(lam)] = sum [M(lam+mu)]
  6. TQ identity (dual): [V_{omega_2}][M(lam)] = sum [M(lam+mu)]
  7. TQ identity (adjoint): [V_{omega_1+omega_2}][M(lam)] = sum mult*[M(lam+mu)]
  8. Clebsch-Gordan / Chebyshev structure: V(1,0)^2 = V(2,0)+V(0,1), etc.
  9. K_0 lattice consistency
 10. Short exact sequence (filtration) dimensions
"""

import pytest

from compute.lib.sl3_baxter import (
    # Weight operations
    Weight,
    weight_add,
    weight_sub,
    weight_neg,
    weight_scale,
    # Root data
    ALPHA_1,
    ALPHA_2,
    ALPHA_12,
    POSITIVE_ROOTS,
    OMEGA_1,
    OMEGA_2,
    RHO,
    CARTAN_MATRIX,
    inner_product,
    pairing,
    # Weyl group
    weyl_reflect_s1,
    weyl_reflect_s2,
    weyl_orbit,
    is_dominant,
    # Kostant partition function
    kostant_partition,
    verify_kostant_basic,
    verify_kostant_verma_top,
    # Characters
    FormalCharacter,
    sl3_fd_character,
    standard_rep_character,
    dual_rep_character,
    adjoint_rep_character,
    symmetric_square_character,
    dual_symmetric_square_character,
    weyl_dimension,
    tensor_product_characters,
    sum_characters,
    subtract_characters,
    formal_character_equal,
    character_dimension,
    # Verma modules
    sl3_verma_character,
    # TQ relations
    baxter_tq_standard,
    verify_baxter_tq_standard,
    baxter_tq_dual,
    verify_baxter_tq_dual,
    baxter_tq_adjoint,
    verify_baxter_tq_adjoint,
    baxter_tq_general,
    verify_baxter_tq_general,
    # SES
    ses_dimension_check_standard,
    verify_ses_standard,
    # Clebsch-Gordan
    verify_clebsch_gordan_V1_squared,
    verify_clebsch_gordan_V2_squared,
    verify_clebsch_gordan_V1_V2,
    verify_adjoint_decomposition,
    # Shift operator
    verify_shift_operator_standard,
    verify_shift_operator_dual,
    # K_0 lattice
    verify_k0_lattice_consistency,
    # Full suite
    verify_all,
)


# ============================================================================
# sl_3 root data
# ============================================================================

class TestRootData:
    """Test the sl_3 root system data."""

    def test_simple_roots_omega_basis(self):
        """Simple roots in omega-basis: alpha_1 = (2,-1), alpha_2 = (-1,2)."""
        assert ALPHA_1 == (2, -1)
        assert ALPHA_2 == (-1, 2)

    def test_alpha_12(self):
        """alpha_1 + alpha_2 = (1, 1) in omega-basis."""
        assert ALPHA_12 == weight_add(ALPHA_1, ALPHA_2)
        assert ALPHA_12 == (1, 1)

    def test_positive_roots_count(self):
        """sl_3 has exactly 3 positive roots."""
        assert len(POSITIVE_ROOTS) == 3
        assert set(POSITIVE_ROOTS) == {ALPHA_1, ALPHA_2, ALPHA_12}

    def test_fundamental_weights(self):
        """Fundamental weights are (1,0) and (0,1) by definition."""
        assert OMEGA_1 == (1, 0)
        assert OMEGA_2 == (0, 1)

    def test_weyl_vector(self):
        """rho = omega_1 + omega_2 = (1, 1)."""
        assert RHO == weight_add(OMEGA_1, OMEGA_2)
        assert RHO == (1, 1)

    def test_cartan_matrix(self):
        """Cartan matrix of sl_3: [[2,-1],[-1,2]]."""
        assert CARTAN_MATRIX == [[2, -1], [-1, 2]]

    def test_pairing_fundamental_weights(self):
        """<omega_i, alpha_j^vee> = delta_{ij}."""
        assert pairing(OMEGA_1, 1) == 1
        assert pairing(OMEGA_1, 2) == 0
        assert pairing(OMEGA_2, 1) == 0
        assert pairing(OMEGA_2, 2) == 1

    def test_inner_product_simple_roots(self):
        """Inner products of simple roots (using 3*<,>).

        3*<alpha_1, alpha_1> = 3*2 = 6 (since <alpha_i, alpha_i> = 2).
        Let's verify: alpha_1 = (2,-1),
        3*<(2,-1),(2,-1)> = 2*4 + 2*(-1) + (-1)*2 + 2*1 = 8 - 2 - 2 + 2 = 6. Good.

        3*<alpha_1, alpha_2> = 3*(-1) = -3.
        3*<(2,-1),(-1,2)> = 2*2*(-1) + 2*2 + (-1)*(-1) + 2*(-1)*2
                           = -4 + 4 + 1 - 4 = -3. Good.
        """
        assert inner_product(ALPHA_1, ALPHA_1) == 6
        assert inner_product(ALPHA_2, ALPHA_2) == 6
        assert inner_product(ALPHA_1, ALPHA_2) == -3
        assert inner_product(ALPHA_12, ALPHA_12) == 6

    def test_inner_product_symmetry(self):
        """Inner product is symmetric."""
        w1, w2 = (2, 3), (-1, 4)
        assert inner_product(w1, w2) == inner_product(w2, w1)


# ============================================================================
# Weyl group
# ============================================================================

class TestWeylGroup:
    """Test the Weyl group S_3 of sl_3."""

    def test_s1_on_alpha1(self):
        """s_1(alpha_1) = -alpha_1."""
        assert weyl_reflect_s1(ALPHA_1) == weight_neg(ALPHA_1)

    def test_s2_on_alpha2(self):
        """s_2(alpha_2) = -alpha_2."""
        assert weyl_reflect_s2(ALPHA_2) == weight_neg(ALPHA_2)

    def test_s1_on_alpha2(self):
        """s_1(alpha_2) = alpha_1 + alpha_2."""
        assert weyl_reflect_s1(ALPHA_2) == ALPHA_12

    def test_s2_on_alpha1(self):
        """s_2(alpha_1) = alpha_1 + alpha_2."""
        assert weyl_reflect_s2(ALPHA_1) == ALPHA_12

    def test_s1_involution(self):
        """s_1^2 = identity."""
        for w in [(1, 0), (0, 1), (2, -1), (3, 5)]:
            assert weyl_reflect_s1(weyl_reflect_s1(w)) == w

    def test_s2_involution(self):
        """s_2^2 = identity."""
        for w in [(1, 0), (0, 1), (-1, 2), (3, 5)]:
            assert weyl_reflect_s2(weyl_reflect_s2(w)) == w

    def test_weyl_orbit_dominant(self):
        """Orbit of a strictly dominant weight has 6 elements (|S_3| = 6)."""
        orbit = weyl_orbit((2, 3))
        assert len(orbit) == 6

    def test_weyl_orbit_boundary(self):
        """Orbit of omega_1 = (1,0) has 3 elements (stabilizer = S_2)."""
        orbit = weyl_orbit(OMEGA_1)
        assert len(orbit) == 3
        # The orbit should be the weights of V(1,0)
        expected = {(1, 0), (-1, 1), (0, -1)}
        assert set(orbit) == expected

    def test_weyl_orbit_omega2(self):
        """Orbit of omega_2 = (0,1) has 3 elements."""
        orbit = weyl_orbit(OMEGA_2)
        assert len(orbit) == 3
        expected = {(0, 1), (1, -1), (-1, 0)}
        assert set(orbit) == expected

    def test_weyl_orbit_zero(self):
        """Orbit of (0,0) is just {(0,0)}."""
        assert weyl_orbit((0, 0)) == [(0, 0)]

    def test_is_dominant(self):
        """Dominant weights have non-negative Dynkin labels."""
        assert is_dominant((0, 0))
        assert is_dominant((1, 0))
        assert is_dominant((0, 1))
        assert is_dominant((3, 5))
        assert not is_dominant((-1, 0))
        assert not is_dominant((0, -1))
        assert not is_dominant((-1, -1))


# ============================================================================
# Kostant partition function
# ============================================================================

class TestKostantPartition:
    """Test the Kostant partition function for sl_3."""

    def test_p_zero(self):
        """p(0) = 1 (empty sum)."""
        assert kostant_partition((0, 0)) == 1

    def test_p_simple_roots(self):
        """p(alpha_i) = 1 for each simple root."""
        assert kostant_partition(ALPHA_1) == 1
        assert kostant_partition(ALPHA_2) == 1

    def test_p_alpha_12(self):
        """p(alpha_1 + alpha_2) = 2.

        Two decompositions:
        (i)  alpha_1 + alpha_2 as one positive root (n_3=1, n_1=n_2=0)
        (ii) alpha_1 + alpha_2 as sum of two simple roots (n_1=n_2=1, n_3=0)
        """
        assert kostant_partition(ALPHA_12) == 2

    def test_p_2alpha1(self):
        """p(2*alpha_1) = 1 (only n_1=2, n_2=n_3=0)."""
        assert kostant_partition(weight_scale(2, ALPHA_1)) == 1

    def test_p_2alpha2(self):
        """p(2*alpha_2) = 1."""
        assert kostant_partition(weight_scale(2, ALPHA_2)) == 1

    def test_p_2alpha12(self):
        """p(2*(alpha_1+alpha_2)) = p((2,2)).

        Decompositions of (2,2):
        n_3*(1,1): n_3 can be 0, 1, 2.
        n_3=0: need n_1*(2,-1)+n_2*(-1,2)=(2,2). 3n_1=6, n_1=2; 3n_2=6, n_2=2. Valid.
        n_3=1: need (1,1)=n_1*(2,-1)+n_2*(-1,2). 3n_1=3, n_1=1; 3n_2=3, n_2=1. Valid.
        n_3=2: need (0,0). n_1=n_2=0. Valid.
        So p = 3.
        """
        assert kostant_partition((2, 2)) == 3

    def test_p_negative(self):
        """p(beta) = 0 for weights not in the positive root cone."""
        assert kostant_partition((-1, 0)) == 0
        assert kostant_partition((0, -1)) == 0
        assert kostant_partition((-1, -1)) == 0

    def test_verify_kostant_basic(self):
        """Built-in verification of basic Kostant values."""
        assert verify_kostant_basic()

    def test_verify_kostant_top(self):
        """p(0) = 1 for Verma module top weight."""
        assert verify_kostant_verma_top()


# ============================================================================
# Weight operations
# ============================================================================

class TestWeightOperations:
    """Test basic weight arithmetic."""

    def test_add(self):
        assert weight_add((1, 2), (3, -1)) == (4, 1)

    def test_sub(self):
        assert weight_sub((3, 2), (1, 1)) == (2, 1)

    def test_neg(self):
        assert weight_neg((2, -3)) == (-2, 3)

    def test_scale(self):
        assert weight_scale(3, (2, -1)) == (6, -3)
        assert weight_scale(0, (5, 7)) == (0, 0)

    def test_add_inverse(self):
        """w + (-w) = 0."""
        w = (3, -5)
        assert weight_add(w, weight_neg(w)) == (0, 0)


# ============================================================================
# Finite-dimensional representations
# ============================================================================

class TestWeylDimension:
    """Test the Weyl dimension formula."""

    @pytest.mark.parametrize("hw,expected", [
        ((0, 0), 1),
        ((1, 0), 3),
        ((0, 1), 3),
        ((1, 1), 8),
        ((2, 0), 6),
        ((0, 2), 6),
        ((2, 1), 15),
        ((1, 2), 15),
        ((3, 0), 10),
        ((0, 3), 10),
        ((2, 2), 27),
        ((3, 3), 64),
    ])
    def test_weyl_dimension(self, hw, expected):
        """Weyl dimension formula: (a+1)(b+1)(a+b+2)/2."""
        assert weyl_dimension(hw) == expected

    def test_weyl_dimension_negative(self):
        """Negative Dynkin labels give dimension 0."""
        assert weyl_dimension((-1, 0)) == 0
        assert weyl_dimension((0, -1)) == 0


class TestFiniteDimCharacters:
    """Test finite-dimensional representation characters."""

    def test_standard_rep_weights(self):
        """V(1,0) has weights (1,0), (-1,1), (0,-1)."""
        chi = standard_rep_character()
        assert chi == {(1, 0): 1, (-1, 1): 1, (0, -1): 1}

    def test_standard_rep_dimension(self):
        """dim V(1,0) = 3."""
        assert character_dimension(standard_rep_character()) == 3

    def test_dual_rep_weights(self):
        """V(0,1) has weights (0,1), (1,-1), (-1,0)."""
        chi = dual_rep_character()
        assert chi == {(0, 1): 1, (1, -1): 1, (-1, 0): 1}

    def test_dual_rep_dimension(self):
        """dim V(0,1) = 3."""
        assert character_dimension(dual_rep_character()) == 3

    def test_adjoint_rep_dimension(self):
        """dim V(1,1) = 8."""
        assert character_dimension(adjoint_rep_character()) == 8

    def test_adjoint_rep_zero_weight(self):
        """Adjoint has zero weight with multiplicity 2 (= rank)."""
        chi = adjoint_rep_character()
        assert chi[(0, 0)] == 2

    def test_adjoint_rep_root_weights(self):
        """Adjoint contains all roots with multiplicity 1."""
        chi = adjoint_rep_character()
        for alpha in POSITIVE_ROOTS:
            assert chi[alpha] == 1
            assert chi[weight_neg(alpha)] == 1

    def test_symmetric_square_dimension(self):
        """dim V(2,0) = 6 = Sym^2(C^3)."""
        assert character_dimension(symmetric_square_character()) == 6

    def test_dual_symmetric_square_dimension(self):
        """dim V(0,2) = 6."""
        assert character_dimension(dual_symmetric_square_character()) == 6

    def test_dual_symmetric_is_negative(self):
        """V(0,2) has weights that are negatives of V(2,0) weights."""
        chi_20 = symmetric_square_character()
        chi_02 = dual_symmetric_square_character()
        for w, m in chi_20.items():
            assert chi_02.get(weight_neg(w), 0) == m


class TestFreudenthalCharacter:
    """Test the Freudenthal multiplicity formula for general reps."""

    @pytest.mark.parametrize("hw", [
        (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
        (2, 1), (1, 2), (3, 0), (0, 3), (2, 2),
    ])
    def test_dimension_matches_weyl(self, hw):
        """Freudenthal character has correct total dimension."""
        chi = sl3_fd_character(hw)
        assert character_dimension(chi) == weyl_dimension(hw)

    def test_freudenthal_standard_matches_explicit(self):
        """Freudenthal for V(1,0) matches explicit character."""
        assert formal_character_equal(sl3_fd_character((1, 0)),
                                       standard_rep_character())

    def test_freudenthal_dual_matches_explicit(self):
        """Freudenthal for V(0,1) matches explicit character."""
        assert formal_character_equal(sl3_fd_character((0, 1)),
                                       dual_rep_character())

    def test_freudenthal_adjoint_matches_explicit(self):
        """Freudenthal for V(1,1) matches explicit character."""
        assert formal_character_equal(sl3_fd_character((1, 1)),
                                       adjoint_rep_character())

    def test_freudenthal_sym2_matches_explicit(self):
        """Freudenthal for V(2,0) matches explicit character."""
        assert formal_character_equal(sl3_fd_character((2, 0)),
                                       symmetric_square_character())

    def test_highest_weight_multiplicity_one(self):
        """Highest weight always has multiplicity 1."""
        for hw in [(1, 0), (2, 1), (3, 3)]:
            chi = sl3_fd_character(hw)
            assert chi.get(hw, 0) == 1

    def test_v30_is_sym3(self):
        """V(3,0) = Sym^3(C^3), dim 10, all weights mult 1."""
        chi = sl3_fd_character((3, 0))
        assert character_dimension(chi) == 10
        # All multiplicities should be 1 (no repeated weights in Sym^3)
        for m in chi.values():
            assert m == 1


# ============================================================================
# Character operations
# ============================================================================

class TestCharacterOperations:
    """Test tensor product, sum, and subtraction of characters."""

    def test_tensor_product_dimensions(self):
        """dim(V tensor W) = dim(V) * dim(W)."""
        V1 = standard_rep_character()
        V2 = dual_rep_character()
        product = tensor_product_characters(V1, V2)
        assert character_dimension(product) == 3 * 3

    def test_tensor_product_V1_V1(self):
        """V(1,0) tensor V(1,0) has dim 9."""
        V1 = standard_rep_character()
        product = tensor_product_characters(V1, V1)
        assert character_dimension(product) == 9

    def test_sum_characters(self):
        """Direct sum adds multiplicities."""
        chi1 = {(1, 0): 1, (0, 0): 2}
        chi2 = {(0, 0): 3, (-1, 0): 1}
        result = sum_characters(chi1, chi2)
        assert result == {(1, 0): 1, (0, 0): 5, (-1, 0): 1}

    def test_subtract_characters(self):
        """Subtraction for exact sequence verification."""
        chi1 = {(1, 0): 3, (0, 0): 2}
        chi2 = {(1, 0): 1, (0, 0): 2}
        diff = subtract_characters(chi1, chi2)
        assert diff == {(1, 0): 2}

    def test_formal_character_equal(self):
        """Equal characters are detected."""
        chi1 = {(1, 0): 1, (0, -1): 1}
        chi2 = {(0, -1): 1, (1, 0): 1}
        assert formal_character_equal(chi1, chi2)

    def test_formal_character_not_equal(self):
        """Unequal characters are detected."""
        assert not formal_character_equal({(1, 0): 1}, {(1, 0): 2})
        assert not formal_character_equal({(1, 0): 1}, {(0, 1): 1})

    def test_tensor_associativity(self):
        """(V1 tensor V2) tensor V3 = V1 tensor (V2 tensor V3)."""
        V1 = standard_rep_character()
        V2 = dual_rep_character()
        V3 = {(0, 0): 1}  # trivial
        left = tensor_product_characters(
            tensor_product_characters(V1, V2), V3)
        right = tensor_product_characters(
            V1, tensor_product_characters(V2, V3))
        assert formal_character_equal(left, right)


# ============================================================================
# Verma module characters
# ============================================================================

class TestVermaCharacters:
    """Test Verma module characters for sl_3."""

    def test_verma_highest_weight(self):
        """M(lambda) has lambda as its highest weight with mult 1."""
        for lam in [(0, 0), (1, 0), (0, 1), (2, 3)]:
            chi = sl3_verma_character(lam, depth=5)
            assert chi[lam] == 1

    def test_verma_top_weight_unique(self):
        """The highest weight appears with multiplicity 1."""
        chi = sl3_verma_character((3, 2), depth=5)
        assert chi[(3, 2)] == 1

    def test_verma_depth_zero(self):
        """depth=0 gives just the highest weight."""
        chi = sl3_verma_character((2, 1), depth=0)
        assert chi == {(2, 1): 1}

    def test_verma_level_1_multiplicities(self):
        """At level 1 below hw, multiplicities come from Kostant p.

        M(lambda) at weight lambda-alpha_i has multiplicity p(alpha_i)=1.
        """
        lam = (3, 2)
        chi = sl3_verma_character(lam, depth=3)
        for alpha in [ALPHA_1, ALPHA_2]:
            mu = weight_sub(lam, alpha)
            assert chi.get(mu, 0) == 1

    def test_verma_alpha12_multiplicity(self):
        """M(lambda) at weight lambda-(alpha_1+alpha_2) has multiplicity p(alpha_12)=2."""
        lam = (3, 2)
        chi = sl3_verma_character(lam, depth=3)
        mu = weight_sub(lam, ALPHA_12)
        assert chi.get(mu, 0) == 2

    def test_verma_total_weights_grow(self):
        """Number of distinct weights in M(lambda) grows with depth."""
        lam = (1, 1)
        chi3 = sl3_verma_character(lam, depth=3)
        chi5 = sl3_verma_character(lam, depth=5)
        assert len(chi5) > len(chi3)

    @pytest.mark.parametrize("lam", [(0, 0), (1, 0), (0, 1), (1, 1)])
    def test_verma_kostant_consistency(self, lam):
        """Weight multiplicities match independent Kostant computation."""
        chi = sl3_verma_character(lam, depth=5)
        for mu, mult in chi.items():
            beta = weight_sub(lam, mu)
            assert mult == kostant_partition(beta), \
                f"Mismatch at lam={lam}, mu={mu}: got {mult}, expected p({beta})={kostant_partition(beta)}"


# ============================================================================
# Baxter TQ relation: standard rep
# ============================================================================

class TestBaxterTQStandard:
    """Test [V_{omega_1}][M(lam)] = [M(lam+omega_1)] + [M(lam+omega_2-omega_1)] + [M(lam-omega_2)]."""

    @pytest.mark.parametrize("lam", [
        (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
        (2, 1), (1, 2), (3, 0), (0, 3), (2, 2), (3, 1),
    ])
    def test_tq_standard(self, lam):
        """TQ identity holds for the standard rep at various lambda."""
        assert verify_baxter_tq_standard(lam)

    def test_tq_standard_weight_by_weight(self):
        """Detailed weight-by-weight check for lam=(1,1)."""
        lhs, rhs = baxter_tq_standard((1, 1), depth=5)
        # Top weight of LHS: (1,1) + (1,0) = (2,1) from the tensor
        assert lhs.get((2, 1), 0) == rhs.get((2, 1), 0)
        # Check several more
        for w in [(1, 2), (0, 0), (2, -1)]:
            assert lhs.get(w, 0) == rhs.get(w, 0), f"Mismatch at weight {w}"

    def test_tq_standard_top_weight(self):
        """Top weight of V_{omega_1} tensor M(lam) is lam + omega_1."""
        lam = (2, 3)
        lhs, _ = baxter_tq_standard(lam, depth=3)
        top = weight_add(lam, OMEGA_1)  # (3, 3)
        assert lhs.get(top, 0) == 1


class TestBaxterTQDual:
    """Test [V_{omega_2}][M(lam)] = [M(lam+omega_2)] + [M(lam+omega_1-omega_2)] + [M(lam-omega_1)]."""

    @pytest.mark.parametrize("lam", [
        (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
        (2, 1), (1, 2), (3, 0), (0, 3), (2, 2), (3, 1),
    ])
    def test_tq_dual(self, lam):
        """TQ identity holds for the dual rep at various lambda."""
        assert verify_baxter_tq_dual(lam)

    def test_tq_dual_top_weight(self):
        """Top weight of V_{omega_2} tensor M(lam) is lam + omega_2."""
        lam = (2, 3)
        lhs, _ = baxter_tq_dual(lam, depth=3)
        top = weight_add(lam, OMEGA_2)  # (2, 4)
        assert lhs.get(top, 0) == 1


class TestBaxterTQAdjoint:
    """Test the TQ relation for the adjoint rep V(1,1)."""

    @pytest.mark.parametrize("lam", [
        (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
    ])
    def test_tq_adjoint(self, lam):
        """TQ identity holds for the adjoint rep."""
        assert verify_baxter_tq_adjoint(lam)

    def test_tq_adjoint_zero_weight_multiplicity(self):
        """Zero weight in adjoint has mult 2, giving 2*[M(lam)] in the sum."""
        lam = (1, 1)
        _, rhs = baxter_tq_adjoint(lam, depth=5)
        # The zero-weight contribution is 2 * M(1,1)
        # So M(1,1) should appear in the sum with appropriate multiplicity
        # at its highest weight
        assert rhs.get((1, 1), 0) >= 2


class TestBaxterTQGeneral:
    """Test the general TQ relation for arbitrary V."""

    def test_general_with_standard(self):
        """General formula reduces to standard TQ for V_{omega_1}."""
        V_std = standard_rep_character()
        for lam in [(0, 0), (1, 1), (2, 0)]:
            assert verify_baxter_tq_general(V_std, lam)

    def test_general_with_dual(self):
        """General formula reduces to dual TQ for V_{omega_2}."""
        V_dual = dual_rep_character()
        for lam in [(0, 0), (1, 0), (0, 1)]:
            assert verify_baxter_tq_general(V_dual, lam)

    def test_general_with_sym2(self):
        """TQ identity for V(2,0) = Sym^2."""
        V_sym2 = symmetric_square_character()
        for lam in [(0, 0), (1, 0), (1, 1)]:
            assert verify_baxter_tq_general(V_sym2, lam)


# ============================================================================
# Short exact sequence (filtration) dimensions
# ============================================================================

class TestSESDimensions:
    """Test the short exact sequence / filtration at the level of dimensions."""

    @pytest.mark.parametrize("lam", [
        (0, 0), (1, 0), (0, 1), (1, 1), (2, 1),
    ])
    def test_ses_standard(self, lam):
        """SES dimensions match for the standard rep."""
        assert verify_ses_standard(lam)

    def test_ses_weight_data_format(self):
        """ses_dimension_check returns (dim_tensor, dim_rhs) tuples."""
        data = ses_dimension_check_standard((1, 0), depth=3)
        for w, (d_t, d_r) in data.items():
            assert isinstance(d_t, int)
            assert isinstance(d_r, int)

    def test_ses_top_weight_standard(self):
        """At top weight lam+omega_1, only M(lam+omega_1) contributes."""
        lam = (2, 1)
        data = ses_dimension_check_standard(lam, depth=5)
        top = weight_add(lam, OMEGA_1)  # (3, 1)
        d_t, d_r = data[top]
        assert d_t == 1
        assert d_r == 1


# ============================================================================
# Clebsch-Gordan / Chebyshev structure
# ============================================================================

class TestClebschGordan:
    """Test Clebsch-Gordan decompositions — the categorified Chebyshev structure."""

    def test_V1_squared(self):
        """V(1,0) tensor V(1,0) = V(2,0) + V(0,1).

        This is the sl_3 analogue of the Chebyshev relation:
        [V_{omega_1}]^2 = [V_{2*omega_1}] + [V_{omega_2}].
        Dimensions: 9 = 6 + 3.
        """
        assert verify_clebsch_gordan_V1_squared()

    def test_V2_squared(self):
        """V(0,1) tensor V(0,1) = V(0,2) + V(1,0).

        Dual version: [V_{omega_2}]^2 = [V_{2*omega_2}] + [V_{omega_1}].
        Dimensions: 9 = 6 + 3.
        """
        assert verify_clebsch_gordan_V2_squared()

    def test_V1_V2(self):
        """V(1,0) tensor V(0,1) = V(1,1) + V(0,0).

        [V_{omega_1}] * [V_{omega_2}] = [V_{adj}] + [V_0].
        Dimensions: 9 = 8 + 1.
        """
        assert verify_clebsch_gordan_V1_V2()

    def test_adjoint_decomposition(self):
        """V(1,1) tensor V(1,0) = V(2,1) + V(0,2) + V(1,0).

        Dimensions: 24 = 15 + 6 + 3.
        """
        assert verify_adjoint_decomposition()

    def test_V1_squared_dimension(self):
        """Dimension check: 3^2 = 9 = 6 + 3."""
        V_std = standard_rep_character()
        product = tensor_product_characters(V_std, V_std)
        assert character_dimension(product) == 9

    def test_V1_V2_dimension(self):
        """Dimension check: 3 * 3 = 9 = 8 + 1."""
        V_std = standard_rep_character()
        V_dual = dual_rep_character()
        product = tensor_product_characters(V_std, V_dual)
        assert character_dimension(product) == 9

    def test_chebyshev_analog_iterated(self):
        """Iterated CG: V(1,0) tensor V(2,0) = V(3,0) + V(1,1).

        The "Chebyshev recurrence" for sl_3 standard rep:
        [V_{omega_1}] * [V_{2*omega_1}] = [V_{3*omega_1}] + [V_{omega_1+omega_2}].
        Dimensions: 3 * 6 = 18 = 10 + 8.
        """
        V_std = standard_rep_character()
        V_sym2 = symmetric_square_character()
        product = tensor_product_characters(V_std, V_sym2)

        V_30 = sl3_fd_character((3, 0))  # dim 10
        V_11 = adjoint_rep_character()  # dim 8

        rhs = sum_characters(V_30, V_11)
        assert formal_character_equal(product, rhs)


# ============================================================================
# Shift operator
# ============================================================================

class TestShiftOperator:
    """Test that [V_{omega_i}] acts as a shift operator on the Verma lattice."""

    def test_shift_standard(self):
        """[V_{omega_1}] acts as a 3-term shift on M(a,b)."""
        assert verify_shift_operator_standard(max_tests=4, depth=6)

    def test_shift_dual(self):
        """[V_{omega_2}] acts as a 3-term shift on M(a,b)."""
        assert verify_shift_operator_dual(max_tests=4, depth=6)


# ============================================================================
# K_0 lattice
# ============================================================================

class TestK0Lattice:
    """Test the K_0 lattice structure."""

    def test_lattice_consistency(self):
        """The K_0 lattice is consistent with the TQ relation."""
        assert verify_k0_lattice_consistency(max_a=3, max_b=3)

    def test_lattice_self_consistent(self):
        """Both standard and dual TQ give consistent lattice."""
        # Verify that applying V_{omega_1} then V_{omega_2} commutes
        # with applying V_{omega_2} then V_{omega_1}
        V_std = standard_rep_character()
        V_dual = dual_rep_character()
        lam = (1, 1)
        M_lam = sl3_verma_character(lam, depth=6)

        # V1 * (V2 * M)
        inner1 = tensor_product_characters(V_dual, M_lam)
        outer1 = tensor_product_characters(V_std, inner1)

        # V2 * (V1 * M)
        inner2 = tensor_product_characters(V_std, M_lam)
        outer2 = tensor_product_characters(V_dual, inner2)

        # They should be equal (commutativity of tensor product)
        assert formal_character_equal(outer1, outer2)


# ============================================================================
# Integration / comprehensive
# ============================================================================

class TestComprehensive:
    """Integration tests combining multiple aspects."""

    def test_verify_all(self):
        """All verification checks pass."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_tq_standard_implies_ses(self):
        """The K_0 identity is equivalent to the SES dimension identity."""
        for lam in [(0, 0), (1, 1), (2, 0)]:
            assert verify_baxter_tq_standard(lam)
            assert verify_ses_standard(lam)

    def test_standard_and_dual_tq_consistent(self):
        """Standard and dual TQ give the same tensor algebra structure.

        Applying V_{omega_1} then V_{omega_2} should be the same as
        V_{omega_2} then V_{omega_1} (commutativity in K_0).
        """
        V_std = standard_rep_character()
        V_dual = dual_rep_character()

        for lam in [(0, 0), (1, 0), (1, 1)]:
            M = sl3_verma_character(lam, depth=6)
            lhs = tensor_product_characters(V_std,
                                            tensor_product_characters(V_dual, M))
            rhs = tensor_product_characters(V_dual,
                                            tensor_product_characters(V_std, M))
            assert formal_character_equal(lhs, rhs)

    def test_tq_cg_consistency(self):
        """The TQ identity for Verma modules is consistent with the
        Clebsch-Gordan rule for finite-dim reps.

        If we restrict to the fd case (lambda dominant, large enough),
        the Verma tensor formula implies the CG rule.
        """
        # V(1,0) tensor V(1,0) = V(2,0) + V(0,1) (CG)
        assert verify_clebsch_gordan_V1_squared()
        # V(1,0) tensor M(1,0) = M(2,0) + M(0,1) + M(1,-1) (TQ)
        assert verify_baxter_tq_standard((1, 0))

    def test_all_tq_at_rho(self):
        """TQ at lambda = rho = (1,1) for all three reps."""
        assert verify_baxter_tq_standard((1, 1))
        assert verify_baxter_tq_dual((1, 1))
        assert verify_baxter_tq_adjoint((1, 1))


# ============================================================================
# Edge cases
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary tests."""

    def test_tq_at_zero_weight(self):
        """TQ identity holds at lambda = (0, 0)."""
        assert verify_baxter_tq_standard((0, 0))
        assert verify_baxter_tq_dual((0, 0))

    def test_verma_at_origin(self):
        """M(0,0) at depth 0 is just {(0,0): 1}."""
        chi = sl3_verma_character((0, 0), depth=0)
        assert chi == {(0, 0): 1}

    def test_trivial_character(self):
        """Trivial rep V(0,0) = {(0,0): 1}."""
        chi = sl3_fd_character((0, 0))
        assert chi == {(0, 0): 1}

    def test_empty_characters_equal(self):
        """Two empty characters are equal."""
        assert formal_character_equal({}, {})

    def test_tensor_with_trivial(self):
        """V tensor V(0,0) = V for any V."""
        V_std = standard_rep_character()
        V_triv = {(0, 0): 1}
        product = tensor_product_characters(V_std, V_triv)
        assert formal_character_equal(product, V_std)

    def test_negative_weight_tq(self):
        """TQ identity works for non-dominant lambda."""
        # M(lambda) exists for all lambda, not just dominant
        assert verify_baxter_tq_standard((-1, 0))
        assert verify_baxter_tq_dual((0, -1))

    def test_weyl_dimension_symmetry(self):
        """dim V(a,b) = dim V(b,a) (outer automorphism symmetry of sl_3)."""
        for a in range(5):
            for b in range(5):
                assert weyl_dimension((a, b)) == weyl_dimension((b, a))
