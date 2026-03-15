"""Tests for Baxter TQ derived lift from K_0 to D^b — G4 conjecture verification.

Tests verify the upgrade of the Baxter TQ relation from K_0 level to
distinguished triangles in D^b(O^sh_{<=0}).

The key mathematical fact being tested:
  The K_0 identity [V_1]*[M(lam)] = [M(lam+1)] + [M(lam-1)]
  lifts to the distinguished triangle
  M(lam-1) -> V_1 tensor M(lam) -> M(lam+1) -> M(lam-1)[1]
  which is induced by the SES
  0 -> M(lam-1) -> V_1 tensor M(lam) -> M(lam+1) -> 0.

Tests cover:
  1. SES at weight lambda = 0, 1, 2, 5, 10 (sl_2)
  2. Mapping cone quasi-isomorphism check
  3. Distinguished triangle axioms
  4. Long exact sequence -> K_0 recovery
  5. Octahedral axiom for iterated TQ
  6. sl_3 fundamental x Verma SES check (basic cases)
  7. Higher-spin TQ lift
  8. Iterated TQ lift with binomial structure
"""

import pytest
from math import comb

from compute.lib.baxter_derived_lift import (
    # Core data types
    WeightSpaceModule,
    ChainComplex,
    # SES
    ses_structure_sl2,
    # Mapping cone
    mapping_cone_sl2,
    # Distinguished triangle
    distinguished_triangle_sl2,
    # Long exact sequence
    long_exact_sequence_recovery,
    # sl_3
    sl3_tq_ses_check,
    # Octahedral
    octahedral_axiom_check_sl2,
    # Iterated TQ
    iterated_tq_lift,
    # Higher spin
    higher_spin_tq_lift,
    # Comprehensive
    verify_derived_lift_sl2,
)

from compute.lib.sl2_baxter import (
    sl2_verma_character,
    eval_module_V1,
    eval_module_Vn,
    tensor_product_characters,
    sum_characters,
    subtract_characters,
    formal_character_equal,
)


# ============================================================================
# WeightSpaceModule
# ============================================================================

class TestWeightSpaceModule:
    """Test the WeightSpaceModule helper class."""

    def test_construction(self):
        """WeightSpaceModule wraps a character dict."""
        chi = {2: 1, 0: 1, -2: 1}
        mod = WeightSpaceModule(chi, name="V_2")
        assert mod.dim_at(2) == 1
        assert mod.dim_at(0) == 1
        assert mod.dim_at(-2) == 1
        assert mod.dim_at(99) == 0

    def test_weights(self):
        """Weights are returned in descending order."""
        chi = {2: 1, -2: 1, 0: 1}
        mod = WeightSpaceModule(chi)
        assert mod.weights() == [2, 0, -2]

    def test_total_dim(self):
        """Total dimension is sum of multiplicities."""
        chi = {2: 1, 0: 2, -2: 1}
        mod = WeightSpaceModule(chi)
        assert mod.total_dim_truncated() == 4

    def test_equality(self):
        """Two modules with same characters are equal."""
        m1 = WeightSpaceModule({1: 1, -1: 1})
        m2 = WeightSpaceModule({-1: 1, 1: 1})
        assert m1 == m2

    def test_zero_entries_cleaned(self):
        """Zero multiplicities are removed."""
        mod = WeightSpaceModule({1: 1, 0: 0, -1: 1})
        assert 0 not in mod.character


# ============================================================================
# ChainComplex
# ============================================================================

class TestChainComplex:
    """Test the ChainComplex class."""

    def test_module_as_complex(self):
        """A module in degree 0 is a chain complex."""
        chi = {2: 1, 0: 1}
        cx = ChainComplex({0: chi})
        assert cx.degrees() == [0]
        assert cx.character_at_degree(0) == chi

    def test_empty_degrees_excluded(self):
        """Degrees with zero characters are excluded."""
        cx = ChainComplex({0: {1: 1}, 1: {}, 2: {0: 0}})
        assert cx.degrees() == [0]

    def test_cohomology_of_module(self):
        """Cohomology of a module is itself in degree 0."""
        chi = {3: 1, 1: 1, -1: 1}
        cx = ChainComplex({0: chi})
        coh = cx.cohomology()
        assert 0 in coh
        assert formal_character_equal(coh[0], chi)

    def test_cohomology_of_mapping_cone(self):
        """Mapping cone of injection has H^0 = cokernel, H^{-1} = 0."""
        # f: M(1) -> V_1 tensor M(2), inclusion via singular vector
        M_minus = sl2_verma_character(1, depth=10)
        V1 = eval_module_V1()
        M_lam = sl2_verma_character(2, depth=10)
        tensor = tensor_product_characters(V1, M_lam)
        M_plus = sl2_verma_character(3, depth=10)

        cone = ChainComplex({-1: M_minus, 0: tensor})
        coh = cone.cohomology()

        # H^{-1} should be zero (injection is injective)
        assert -1 not in coh or len(coh.get(-1, {})) == 0
        # H^0 should be M(3)
        assert formal_character_equal(coh.get(0, {}), M_plus)

    def test_euler_characteristic(self):
        """Euler characteristic of cone equals [cokernel] in K_0."""
        M1 = sl2_verma_character(1, depth=10)
        M3 = sl2_verma_character(3, depth=10)
        V1 = eval_module_V1()
        tensor = tensor_product_characters(V1, sl2_verma_character(2, depth=10))

        cone = ChainComplex({-1: M1, 0: tensor})
        euler = cone.euler_characteristic()
        assert formal_character_equal(euler, M3)

    def test_quasi_isomorphism_check(self):
        """is_quasi_isomorphic_to_module correctly identifies q.i."""
        M1 = sl2_verma_character(1, depth=10)
        V1 = eval_module_V1()
        tensor = tensor_product_characters(V1, sl2_verma_character(2, depth=10))
        M3 = sl2_verma_character(3, depth=10)

        cone = ChainComplex({-1: M1, 0: tensor})
        assert cone.is_quasi_isomorphic_to_module(M3)
        assert not cone.is_quasi_isomorphic_to_module(M1)


# ============================================================================
# 1. Short exact sequence structure (sl_2)
# ============================================================================

class TestSESStructureSl2:
    """Test 0 -> M(lam-1) -> V_1 tensor M(lam) -> M(lam+1) -> 0."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_ses_holds(self, lam):
        """SES holds at every weight for various lambda."""
        result = ses_structure_sl2(lam, depth=30)
        assert result['ses_holds'], f"SES fails at lam={lam}"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_injection_well_defined(self, lam):
        """Injection M(lam-1) -> V_1 tensor M(lam) is well-defined."""
        result = ses_structure_sl2(lam, depth=30)
        assert result['injection_well_defined']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_exactness(self, lam):
        """Exactness: dim(mid) = dim(sub) + dim(quot) at every weight."""
        result = ses_structure_sl2(lam, depth=30)
        assert result['exactness']

    @pytest.mark.parametrize("lam", [1, 2, 3, 5, 10])
    def test_singular_vector_annihilated(self, lam):
        """The singular vector w = lam*u2 - u1 is annihilated by e."""
        result = ses_structure_sl2(lam)
        assert result['singular_vector']['e_annihilates']

    def test_singular_vector_coefficients_lam3(self):
        """At lam=3: w = 3*(v_- tensor v_3) - (v_+ tensor f.v_3)."""
        result = ses_structure_sl2(3)
        coeffs = result['singular_vector']['coefficients']
        assert coeffs['v_- tensor v_lam'] == 3
        assert coeffs['v_+ tensor f.v_lam'] == -1

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_euler_characteristic(self, lam):
        """Euler characteristic of the SES is zero."""
        result = ses_structure_sl2(lam)
        assert result['euler_char_check']

    def test_top_weight_analysis_lam5(self):
        """At top weight lam+1=6, only M(6) contributes (not M(4))."""
        result = ses_structure_sl2(5)
        top = result['top_weight_analysis']
        assert top['top_weight'] == 6
        assert top['dim_mid'] == 1
        assert top['dim_sub'] == 0
        assert top['dim_quot'] == 1
        assert top['quotient_generates_M_plus']

    def test_weight_data_structure(self):
        """Weight data has correct tuple format."""
        result = ses_structure_sl2(3, depth=5)
        for w, (d_sub, d_mid, d_quot) in result['weight_data'].items():
            assert isinstance(d_sub, int)
            assert isinstance(d_mid, int)
            assert isinstance(d_quot, int)
            assert d_mid == d_sub + d_quot

    def test_modules_returned(self):
        """ses_structure returns WeightSpaceModule objects."""
        result = ses_structure_sl2(3)
        modules = result['modules']
        assert isinstance(modules['sub'], WeightSpaceModule)
        assert isinstance(modules['mid'], WeightSpaceModule)
        assert isinstance(modules['quot'], WeightSpaceModule)


# ============================================================================
# 2. Mapping cone
# ============================================================================

class TestMappingConeSl2:
    """Test the mapping cone of the inclusion M(lam-1) -> V_1 tensor M(lam)."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_cone_quasi_iso_to_M_plus(self, lam):
        """Cone(f) is quasi-isomorphic to M(lam+1)."""
        result = mapping_cone_sl2(lam, depth=30)
        assert result['quasi_iso_to_M_plus'], \
            f"Cone not q.i. to M({lam + 1}) at lam={lam}"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_H_minus1_vanishes(self, lam):
        """H^{-1}(Cone(f)) = 0 (injection is injective)."""
        result = mapping_cone_sl2(lam, depth=30)
        assert result['H_minus1_is_zero'], \
            f"H^{{-1}} nonzero at lam={lam}"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_H0_is_M_plus(self, lam):
        """H^0(Cone(f)) = M(lam+1) as formal characters."""
        result = mapping_cone_sl2(lam, depth=30)
        M_plus = sl2_verma_character(lam + 1, depth=30)
        assert formal_character_equal(result['H0_character'], M_plus)

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_euler_characteristic_matches(self, lam):
        """Euler characteristic of cone equals [M(lam+1)]."""
        result = mapping_cone_sl2(lam, depth=30)
        assert result['euler_matches_M_plus']

    def test_cone_is_chain_complex(self):
        """The cone object is a ChainComplex instance."""
        result = mapping_cone_sl2(3)
        assert isinstance(result['cone'], ChainComplex)

    def test_cone_degrees(self):
        """Cone lives in degrees -1 and 0."""
        result = mapping_cone_sl2(3)
        cone = result['cone']
        assert -1 in cone.degrees()
        assert 0 in cone.degrees()
        assert len(cone.degrees()) == 2


# ============================================================================
# 3. Distinguished triangle axioms
# ============================================================================

class TestDistinguishedTriangleSl2:
    """Test the distinguished triangle M(lam-1) -> V_1 tensor M(lam) -> M(lam+1) -> M(lam-1)[1]."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_is_distinguished_triangle(self, lam):
        """The triangle satisfies the distinguished triangle axioms."""
        result = distinguished_triangle_sl2(lam, depth=30)
        assert result['is_distinguished_triangle'], \
            f"Not a distinguished triangle at lam={lam}"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_TR1_cone_isomorphism(self, lam):
        """(TR1) Cone(f) is isomorphic to M(lam+1)."""
        result = distinguished_triangle_sl2(lam, depth=30)
        assert result['TR1_cone_isomorphism']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_f_injection(self, lam):
        """The injection f: M(lam-1) -> V_1 tensor M(lam) is well-defined."""
        result = distinguished_triangle_sl2(lam, depth=30)
        assert result['f_injection_well_defined']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_g_surjection(self, lam):
        """The surjection g: V_1 tensor M(lam) -> M(lam+1) is well-defined."""
        result = distinguished_triangle_sl2(lam, depth=30)
        assert result['g_surjection_well_defined']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_exactness(self, lam):
        """im(f) = ker(g) at every weight (exactness)."""
        result = distinguished_triangle_sl2(lam, depth=30)
        assert result['exactness_im_f_eq_ker_g']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_connecting_homomorphism_degree(self, lam):
        """The connecting homomorphism h has degree +1."""
        result = distinguished_triangle_sl2(lam, depth=30)
        h_data = result['connecting_homomorphism']
        assert h_data['degree'] == 1
        assert h_data['source'] == f"M({lam + 1})"
        assert h_data['target'] == f"M({lam - 1})[1]"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_TR2_rotation(self, lam):
        """(TR2) The rotated triangle is also distinguished."""
        result = distinguished_triangle_sl2(lam, depth=30)
        assert result['TR2_rotation']

    def test_triangle_description(self):
        """Triangle has correct string description."""
        result = distinguished_triangle_sl2(3)
        desc = result['triangle_description']
        assert "M(2)" in desc
        assert "V_1 tensor M(3)" in desc
        assert "M(4)" in desc


# ============================================================================
# 4. Long exact sequence -> K_0 recovery
# ============================================================================

class TestLongExactSequenceRecovery:
    """Test that the LES in cohomology recovers the K_0 identity."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_les_reduces_to_ses(self, lam):
        """For modules in degree 0, the LES reduces to the SES."""
        result = long_exact_sequence_recovery(lam, depth=30)
        assert result['les_reduces_to_ses']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_k0_identity_recovered(self, lam):
        """The K_0 identity [V_1]*[M(lam)] = [M(lam+1)] + [M(lam-1)] is recovered."""
        result = long_exact_sequence_recovery(lam, depth=30)
        assert result['k0_identity_recovered']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_k0_direct_check(self, lam):
        """Direct K_0 check also passes (cross-validation)."""
        result = long_exact_sequence_recovery(lam, depth=30)
        assert result['k0_identity_direct_check']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_euler_characteristic_zero(self, lam):
        """Euler characteristic of the triangle is zero in K_0."""
        result = long_exact_sequence_recovery(lam, depth=30)
        assert result['euler_characteristic_zero']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_higher_cohomology_vanishes(self, lam):
        """H^n = 0 for n != 0 (modules are concentrated in degree 0)."""
        result = long_exact_sequence_recovery(lam, depth=30)
        assert result['higher_cohomology_vanishes']

    def test_k0_equation_format(self):
        """K_0 equation has correct format."""
        result = long_exact_sequence_recovery(3)
        assert "[V_1]*[M(3)]" in result['k0_equation']
        assert "[M(4)]" in result['k0_equation']
        assert "[M(2)]" in result['k0_equation']


# ============================================================================
# 5. Octahedral axiom
# ============================================================================

class TestOctahedralAxiomSl2:
    """Test the octahedral axiom for composed TQ relations."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_octahedral_axiom_holds(self, lam):
        """The octahedral axiom is satisfied for V_1 tensor V_1 tensor M(lam)."""
        result = octahedral_axiom_check_sl2(lam, depth=20)
        assert result['octahedral_axiom_holds'], \
            f"Octahedral axiom fails at lam={lam}"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_clebsch_gordan_V1_squared(self, lam):
        """V_1 tensor V_1 = V_2 + V_0 (Clebsch-Gordan)."""
        result = octahedral_axiom_check_sl2(lam)
        assert result['clebsch_gordan_V1_squared']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_way1_decomposition(self, lam):
        """Way 1: (V_1 tensor V_1) tensor M(lam) decomposes correctly."""
        result = octahedral_axiom_check_sl2(lam, depth=20)
        assert result['way1_decomposition_ok']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_way2_decomposition(self, lam):
        """Way 2: V_1 tensor (V_1 tensor M(lam)) decomposes correctly."""
        result = octahedral_axiom_check_sl2(lam, depth=20)
        assert result['way2_decomposition_ok']

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_ways_compatible(self, lam):
        """Both decomposition ways give the same total character."""
        result = octahedral_axiom_check_sl2(lam, depth=20)
        assert result['ways_compatible']

    def test_way1_V2_decomposition(self):
        """V_2 tensor M(lam) = M(lam+2) + M(lam) + M(lam-2)."""
        result = octahedral_axiom_check_sl2(3)
        assert result['way1_V2_decomposition']

    def test_way1_V0_decomposition(self):
        """V_0 tensor M(lam) = M(lam)."""
        result = octahedral_axiom_check_sl2(3)
        assert result['way1_V0_decomposition']

    def test_way2_plus_step(self):
        """V_1 tensor M(lam+1) = M(lam+2) + M(lam)."""
        result = octahedral_axiom_check_sl2(3)
        assert result['way2_plus_step']

    def test_way2_minus_step(self):
        """V_1 tensor M(lam-1) = M(lam) + M(lam-2)."""
        result = octahedral_axiom_check_sl2(3)
        assert result['way2_minus_step']

    def test_filtration_structure(self):
        """The 3-step filtration has correct layers."""
        result = octahedral_axiom_check_sl2(3)
        filt = result['filtration']
        assert "M(1)" in filt['bottom']
        assert "M(3)" in filt['middle']
        assert "M(5)" in filt['top']


# ============================================================================
# 6. sl_3 TQ SES check
# ============================================================================

class TestSl3TQSES:
    """Test the sl_3 fundamental x Verma SES structure."""

    @pytest.mark.parametrize("hw", [
        (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
    ])
    def test_k0_identity_holds(self, hw):
        """K_0 identity holds for V_{omega_1} tensor M(mu) at various mu."""
        result = sl3_tq_ses_check(hw, depth=10)
        assert result['k0_identity_holds'], f"K_0 identity fails at hw={hw}"

    @pytest.mark.parametrize("hw", [
        (0, 0), (1, 0), (0, 1), (1, 1),
    ])
    def test_weight_by_weight_match(self, hw):
        """Character match holds weight-by-weight."""
        result = sl3_tq_ses_check(hw, depth=10)
        assert result['weight_by_weight_match']

    @pytest.mark.parametrize("hw", [
        (0, 0), (1, 0), (0, 1), (1, 1),
    ])
    def test_dual_k0_holds(self, hw):
        """Dual TQ (V_{omega_2}) also holds."""
        result = sl3_tq_ses_check(hw, depth=10)
        assert result['dual_k0_holds']

    def test_filtration_has_three_layers(self):
        """V_{omega_1} tensor M(mu) has a 3-step filtration."""
        result = sl3_tq_ses_check((1, 1), depth=8)
        assert result['num_filtration_steps'] == 3

    def test_filtration_layer_count(self):
        """There are exactly 3 filtration layers (one per weight of V_{omega_1})."""
        result = sl3_tq_ses_check((1, 0), depth=8)
        assert len(result['filtration_layers']) == 3

    def test_total_dim_match(self):
        """Total truncated dimensions match between tensor and sum of Vermas."""
        result = sl3_tq_ses_check((1, 1), depth=8)
        assert result['total_dim_match']

    def test_no_mismatch_weights(self):
        """No mismatch weights detected."""
        result = sl3_tq_ses_check((1, 1), depth=8)
        assert len(result['mismatch_weights']) == 0


# ============================================================================
# 7. Higher-spin TQ lift
# ============================================================================

class TestHigherSpinTQLift:
    """Test the lift of V_n tensor M(lam) to distinguished triangles."""

    @pytest.mark.parametrize("spin,lam", [
        (1, 0), (1, 1), (1, 2), (1, 5),
        (2, 0), (2, 1), (2, 3),
        (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1),
    ])
    def test_k0_identity_holds(self, spin, lam):
        """Higher-spin K_0 identity holds."""
        result = higher_spin_tq_lift(spin, lam, depth=20)
        assert result['k0_identity_holds'], \
            f"K_0 fails for spin={spin}, lam={lam}"

    @pytest.mark.parametrize("spin", [1, 2, 3, 4, 5])
    def test_filtration_length(self, spin):
        """V_n tensor M(lam) has (n+1)-step filtration."""
        result = higher_spin_tq_lift(spin, 0, depth=15)
        assert result['filtration_length'] == spin + 1

    @pytest.mark.parametrize("spin", [1, 2, 3])
    def test_graded_pieces(self, spin):
        """Graded pieces are M(lam+n), M(lam+n-2), ..., M(lam-n)."""
        lam = 5
        result = higher_spin_tq_lift(spin, lam, depth=15)
        pieces = result['graded_pieces']
        expected = [(lam + spin - 2 * j, 1) for j in range(spin + 1)]
        assert pieces == expected

    @pytest.mark.parametrize("spin,lam", [
        (1, 0), (2, 1), (3, 2),
    ])
    def test_top_weight_correct(self, spin, lam):
        """Top weight of V_n tensor M(lam) is lam+n."""
        result = higher_spin_tq_lift(spin, lam, depth=15)
        assert result['top_weight_correct']

    @pytest.mark.parametrize("spin,lam", [
        (1, 0), (2, 1), (3, 2),
    ])
    def test_all_ses_hold(self, spin, lam):
        """All SES in the filtration hold."""
        result = higher_spin_tq_lift(spin, lam, depth=15)
        assert result['all_ses_hold']

    def test_spin1_is_fundamental(self):
        """spin=1 case is the fundamental TQ relation."""
        result = higher_spin_tq_lift(1, 3, depth=20)
        assert result['filtration_length'] == 2
        pieces = result['graded_pieces']
        assert pieces == [(4, 1), (2, 1)]

    def test_direct_check_consistency(self):
        """direct_check (from sl2_baxter) agrees with our character check."""
        for spin in [1, 2, 3]:
            for lam in [0, 1, 3]:
                result = higher_spin_tq_lift(spin, lam, depth=20)
                assert result['direct_check'] == result['k0_identity_holds']


# ============================================================================
# 8. Iterated TQ lift
# ============================================================================

class TestIteratedTQLift:
    """Test V_1^{tensor n} tensor M(lam) decomposition."""

    @pytest.mark.parametrize("lam", [0, 1, 3])
    def test_all_iterations_match(self, lam):
        """Character decomposition matches at every iteration step."""
        result = iterated_tq_lift(lam, n_iterations=4, depth=20)
        assert result['all_iterations_match']

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_summand_count(self, n):
        """V_1^{tensor n} tensor M(lam) decomposes into 2^n Verma modules."""
        result = iterated_tq_lift(0, n_iterations=n, depth=15)
        assert result['summand_count_correct']
        assert result['total_summands'] == 2 ** n

    @pytest.mark.parametrize("n", [1, 2, 3, 4])
    def test_binomial_multiplicities(self, n):
        """Multiplicity of M(lam+n-2j) is C(n,j)."""
        lam = 0
        result = iterated_tq_lift(lam, n_iterations=n, depth=15)
        step = result['steps'][n - 1]  # last step
        summands = step['summands']
        for hw, mult in summands:
            j = (lam + n - hw) // 2
            assert mult == comb(n, j), \
                f"Multiplicity of M({hw}) is {mult}, expected C({n},{j})={comb(n,j)}"

    def test_n1_is_fundamental(self):
        """n=1 gives the fundamental TQ decomposition."""
        result = iterated_tq_lift(3, n_iterations=1, depth=20)
        step = result['steps'][0]
        assert step['summands'] == [(4, 1), (2, 1)]
        assert step['character_match']

    def test_n2_gives_three_summands(self):
        """n=2 gives M(lam+2) + 2*M(lam) + M(lam-2)."""
        lam = 3
        result = iterated_tq_lift(lam, n_iterations=2, depth=20)
        step = result['steps'][1]
        expected = [(5, 1), (3, 2), (1, 1)]
        assert step['summands'] == expected

    def test_n3_gives_four_summands(self):
        """n=3 gives M(lam+3) + 3*M(lam+1) + 3*M(lam-1) + M(lam-3)."""
        lam = 5
        result = iterated_tq_lift(lam, n_iterations=3, depth=15)
        step = result['steps'][2]
        expected = [(8, 1), (6, 3), (4, 3), (2, 1)]
        assert step['summands'] == expected

    def test_total_binomial_check(self):
        """sum_{j=0}^{n} C(n,j) = 2^n at every step."""
        result = iterated_tq_lift(0, n_iterations=5, depth=12)
        for step in result['steps']:
            assert step['total_binomial_check']


# ============================================================================
# Integration / comprehensive
# ============================================================================

class TestComprehensive:
    """Integration tests combining multiple aspects of the derived lift."""

    def test_verify_all_sl2(self):
        """All derived lift verifications pass for sl_2."""
        results = verify_derived_lift_sl2(
            lam_values=[0, 1, 2, 5],
            depth=15,
        )
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_ses_implies_triangle(self):
        """The SES structure implies the distinguished triangle structure."""
        for lam in [1, 3, 5]:
            ses = ses_structure_sl2(lam, depth=20)
            tri = distinguished_triangle_sl2(lam, depth=20)
            # If SES holds, triangle should be distinguished
            assert ses['ses_holds'] == tri['is_distinguished_triangle']

    def test_triangle_implies_k0(self):
        """The distinguished triangle implies the K_0 identity."""
        for lam in [0, 1, 2, 5]:
            tri = distinguished_triangle_sl2(lam, depth=20)
            les = long_exact_sequence_recovery(lam, depth=20)
            if tri['is_distinguished_triangle']:
                assert les['k0_identity_recovered']

    def test_cone_and_ses_consistent(self):
        """The mapping cone and SES give consistent results."""
        for lam in [0, 1, 3]:
            ses = ses_structure_sl2(lam, depth=20)
            cone = mapping_cone_sl2(lam, depth=20)
            assert ses['ses_holds'] == cone['quasi_iso_to_M_plus']

    def test_higher_spin_reduces_to_fundamental(self):
        """Higher spin n=1 gives the same result as the fundamental TQ."""
        for lam in [0, 1, 3, 5]:
            fund_ses = ses_structure_sl2(lam, depth=20)
            spin1 = higher_spin_tq_lift(1, lam, depth=20)
            assert fund_ses['ses_holds'] == spin1['k0_identity_holds']

    def test_octahedral_consistent_with_iterated(self):
        """Octahedral axiom results consistent with iterated TQ (n=2)."""
        for lam in [0, 1, 3]:
            octa = octahedral_axiom_check_sl2(lam, depth=15)
            itr = iterated_tq_lift(lam, n_iterations=2, depth=15)
            assert octa['ways_compatible']
            assert itr['steps'][1]['character_match']

    def test_full_pipeline_lam2(self):
        """Full pipeline test for lam=2: SES -> Cone -> Triangle -> LES -> K_0."""
        lam = 2
        depth = 25

        # Step 1: SES
        ses = ses_structure_sl2(lam, depth=depth)
        assert ses['ses_holds']

        # Step 2: Mapping cone
        cone = mapping_cone_sl2(lam, depth=depth)
        assert cone['quasi_iso_to_M_plus']
        assert cone['H_minus1_is_zero']

        # Step 3: Distinguished triangle
        tri = distinguished_triangle_sl2(lam, depth=depth)
        assert tri['is_distinguished_triangle']

        # Step 4: Long exact sequence
        les = long_exact_sequence_recovery(lam, depth=depth)
        assert les['les_reduces_to_ses']
        assert les['k0_identity_recovered']
        assert les['euler_characteristic_zero']

    def test_sl2_and_sl3_consistent(self):
        """Both sl_2 and sl_3 TQ relations lift to D^b level."""
        # sl_2
        ses2 = ses_structure_sl2(1, depth=15)
        assert ses2['ses_holds']

        # sl_3
        ses3 = sl3_tq_ses_check((1, 0), depth=8)
        assert ses3['k0_identity_holds']


# ============================================================================
# Edge cases
# ============================================================================

class TestEdgeCases:
    """Edge cases for the derived lift."""

    def test_lam_zero(self):
        """lam=0: M(-1) is the submodule (negative hw Verma)."""
        result = ses_structure_sl2(0, depth=30)
        assert result['ses_holds']

    def test_negative_lam(self):
        """Negative lambda: K_0 identity still holds."""
        for lam in [-1, -3, -5]:
            result = ses_structure_sl2(lam, depth=30)
            assert result['ses_holds']

    def test_large_lam(self):
        """Large lambda: computations are feasible and correct."""
        result = ses_structure_sl2(50, depth=60)
        assert result['ses_holds']

    def test_cone_at_lam_zero(self):
        """Mapping cone at lam=0."""
        result = mapping_cone_sl2(0, depth=20)
        assert result['quasi_iso_to_M_plus']

    def test_sl3_at_origin(self):
        """sl_3 TQ at mu=(0,0)."""
        result = sl3_tq_ses_check((0, 0), depth=10)
        assert result['k0_identity_holds']

    def test_iterated_n1(self):
        """Iterated TQ with n=1 is just the fundamental TQ."""
        result = iterated_tq_lift(3, n_iterations=1, depth=15)
        assert result['all_iterations_match']
        assert result['total_summands'] == 2

    def test_higher_spin_zero(self):
        """V_0 tensor M(lam) = M(lam) (trivial tensoring)."""
        result = higher_spin_tq_lift(0, 3, depth=15)
        assert result['k0_identity_holds']
        assert result['filtration_length'] == 1
