r"""Tests for the categorical theory of shadow depth.

Verifies:
  1. A-infinity depth computation for all four classes (G/L/C/M)
  2. L-infinity formality level at arities 2-5
  3. Operadic complexity test
  4. Four-way identification (r_max = A-inf depth = L-inf level = op-cx)
  5. Depth decomposition d = 1 + d_arith + d_alg
  6. Arithmetic depth and cusp form threshold
  7. Categorical characterization of D(B(A))
  8. Hochschild cohomology HH^2 dimension
  9. DS depth change
  10. Tensor product depth
  11. All standard families classified

Mathematical references:
    conj:operadic-complexity (higher_genus_modular_koszul.tex)
    prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
    thm:depth-decomposition (arithmetic_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:ds-koszul-obstruction (w_algebras.tex)
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

from __future__ import annotations

import pytest
from sympy import Rational, oo, simplify

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from shadow_depth_theory import (
    AInftyStructure,
    CategoricalCharacterization,
    LinftyFormalityData,
    STANDARD_FAMILIES,
    ainfty_depth_from_algebra,
    ainfty_depth_from_shadow,
    algebraic_depth_from_class,
    arithmetic_depth_lattice,
    arithmetic_depth_table,
    build_ainfty_affine_km,
    build_ainfty_betagamma,
    build_ainfty_heisenberg,
    build_ainfty_virasoro,
    build_linf_formality_affine,
    build_linf_formality_betagamma,
    build_linf_formality_heisenberg,
    build_linf_formality_virasoro,
    categorical_characterization,
    classify_standard_landscape,
    comprehensive_verification,
    cusp_form_dim,
    cusp_form_threshold_arity,
    cusp_form_threshold_genus,
    depth_decomposition,
    ds_depth_change,
    extension_depth_change,
    hh2_dimension,
    linf_formality_from_shadow,
    operadic_complexity,
    quotient_depth_change,
    ramanujan_delta_contribution_genus,
    shadow_visibility_genus,
    tensor_product_depth,
    verify_four_way_identification,
    virasoro_ell5_nonvanishing,
    virasoro_shadow_coefficients,
)


# ========================================================================
# 1. A-infinity depth computation
# ========================================================================

class TestAInftyDepth:
    """Verify A-infinity depth for each shadow class."""

    def test_class_G_depth_2(self):
        """Class G (Heisenberg): A-infinity depth = 2."""
        assert ainfty_depth_from_shadow('G') == 2

    def test_class_L_depth_3(self):
        """Class L (affine KM): A-infinity depth = 3."""
        assert ainfty_depth_from_shadow('L') == 3

    def test_class_C_depth_4(self):
        """Class C (betagamma): A-infinity depth = 4."""
        assert ainfty_depth_from_shadow('C') == 4

    def test_class_M_depth_infinity(self):
        """Class M (Virasoro): A-infinity depth = infinity (None)."""
        assert ainfty_depth_from_shadow('M') is None

    def test_heisenberg_family(self):
        """Heisenberg by family name."""
        assert ainfty_depth_from_algebra('Heisenberg') == 2

    def test_affine_family(self):
        """Affine KM by family name."""
        assert ainfty_depth_from_algebra('Affine KM') == 3

    def test_betagamma_family(self):
        """betagamma by family name."""
        assert ainfty_depth_from_algebra('betagamma') == 4

    def test_virasoro_family(self):
        """Virasoro by family name."""
        assert ainfty_depth_from_algebra('Virasoro') is None

    def test_w_algebra_family(self):
        """W-algebra by family name."""
        assert ainfty_depth_from_algebra('W_3') is None

    def test_lattice_family(self):
        """Lattice VOA by family name."""
        assert ainfty_depth_from_algebra('Lattice') == 2

    def test_fermion_family(self):
        """Free fermion by family name."""
        assert ainfty_depth_from_algebra('Free fermion') == 2

    def test_invalid_class_raises(self):
        """Unknown shadow class should raise."""
        with pytest.raises(ValueError):
            ainfty_depth_from_shadow('X')


# ========================================================================
# 2. A-infinity structure objects
# ========================================================================

class TestAInftyStructure:
    """Verify the A-infinity structure data for each archetype."""

    def test_heisenberg_structure(self):
        """Heisenberg: depth 2, only m_2 nonzero."""
        s = build_ainfty_heisenberg(level=1)
        assert s.shadow_class == 'G'
        assert s.depth == 2
        assert s.nonzero_operations == [2]
        assert s.shadow_coefficients[2] == Rational(1)
        assert s.shadow_coefficients[3] == 0
        assert s.shadow_coefficients[4] == 0
        assert s.verify_depth_consistency()

    def test_heisenberg_level_k(self):
        """Heisenberg at level k: kappa = k."""
        for k in [1, 2, 5, 10]:
            s = build_ainfty_heisenberg(level=k)
            assert s.shadow_coefficients[2] == Rational(k)

    def test_affine_structure(self):
        """Affine KM: depth 3, m_2 and m_3 nonzero."""
        s = build_ainfty_affine_km('sl2', level=1)
        assert s.shadow_class == 'L'
        assert s.depth == 3
        assert 2 in s.nonzero_operations
        assert 3 in s.nonzero_operations
        assert s.shadow_coefficients[4] == 0
        assert s.verify_depth_consistency()

    def test_affine_sl3(self):
        """sl_3 at level 1: kappa = dim(g)*(k+h^v)/(2*h^v) = 8*4/(2*3) = 16/3."""
        s = build_ainfty_affine_km('sl3', level=1)
        # dim(sl_3) = 8, h^v = 3, k = 1: kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert s.shadow_coefficients[2] == Rational(16, 3)

    def test_betagamma_structure(self):
        """betagamma: depth 4, m_2, m_3, m_4 nonzero."""
        s = build_ainfty_betagamma(weight=1)
        assert s.shadow_class == 'C'
        assert s.depth == 4
        assert set(s.nonzero_operations) == {2, 3, 4}
        assert s.shadow_coefficients[5] == 0
        assert s.verify_depth_consistency()

    def test_betagamma_kappa(self):
        """betagamma at lambda=1: kappa = 6-6+1 = 1."""
        s = build_ainfty_betagamma(weight=1)
        assert s.shadow_coefficients[2] == Rational(1)

    def test_betagamma_symplectic(self):
        """betagamma at lambda=1/2: kappa = 6/4 - 3 + 1 = -1/2."""
        s = build_ainfty_betagamma(weight=Rational(1, 2))
        assert s.shadow_coefficients[2] == Rational(-1, 2)

    def test_virasoro_structure(self):
        """Virasoro: depth infinity, many m_k nonzero."""
        s = build_ainfty_virasoro(central_charge=1)
        assert s.shadow_class == 'M'
        assert s.depth is None
        assert len(s.nonzero_operations) >= 5
        assert s.verify_depth_consistency()

    def test_virasoro_kappa(self):
        """Virasoro at c: kappa = c/2."""
        for c_val in [1, 2, 13, 26]:
            s = build_ainfty_virasoro(central_charge=c_val)
            assert s.shadow_coefficients[2] == Rational(c_val, 2)

    def test_virasoro_S3(self):
        """Virasoro S_3 = 2 (c-independent)."""
        for c_val in [1, 2, 13, 26]:
            s = build_ainfty_virasoro(central_charge=c_val)
            assert s.shadow_coefficients[3] == 2

    def test_virasoro_S4_formula(self):
        """Virasoro S_4 = 10/[c(5c+22)]."""
        s = build_ainfty_virasoro(central_charge=1)
        assert s.shadow_coefficients[4] == Rational(10, 27)  # 10/(1*27)

    def test_virasoro_S5_formula(self):
        """Virasoro S_5 = -48/[c^2(5c+22)]."""
        s = build_ainfty_virasoro(central_charge=1)
        assert s.shadow_coefficients[5] == Rational(-48, 27)  # -48/(1*27)


# ========================================================================
# 3. L-infinity formality level
# ========================================================================

class TestLInftyFormality:
    """Verify L-infinity formality levels."""

    def test_formality_G(self):
        """Class G: formality level 2 (fully formal at arity 3+)."""
        assert linf_formality_from_shadow('G') == 2

    def test_formality_L(self):
        """Class L: formality level 3."""
        assert linf_formality_from_shadow('L') == 3

    def test_formality_C(self):
        """Class C: formality level 4."""
        assert linf_formality_from_shadow('C') == 4

    def test_formality_M(self):
        """Class M: formality level infinity (None)."""
        assert linf_formality_from_shadow('M') is None

    def test_virasoro_ell5_nonzero(self):
        """Virasoro ell_5 is nonzero (shadow-formality at arity 5)."""
        data = virasoro_ell5_nonvanishing(central_charge=1)
        assert data['S_5_nonzero'] is True
        assert data['ell_5_nonzero'] is True
        assert data['shadow_formality_match'] is True

    def test_virasoro_ell5_various_c(self):
        """Virasoro ell_5 nonzero for various central charges."""
        for c_val in [1, 2, 5, 13, 25, 26]:
            data = virasoro_ell5_nonvanishing(central_charge=c_val)
            assert data['S_5_nonzero'] is True
            assert data['ell_5_nonzero'] is True

    def test_virasoro_S5_value_c1(self):
        """S_5(c=1) = -48/27."""
        data = virasoro_ell5_nonvanishing(central_charge=1)
        assert data['S_5'] == Rational(-48, 27)

    def test_virasoro_S5_value_c26(self):
        """S_5(c=26) = -48/[676*152] = -48/102752."""
        data = virasoro_ell5_nonvanishing(central_charge=26)
        expected = Rational(-48, 26**2 * (5 * 26 + 22))
        assert data['S_5'] == expected

    def test_heisenberg_formality_data(self):
        """Heisenberg: all ell_k=0 for k>=3."""
        f = build_linf_formality_heisenberg()
        assert f.formality_level == 2
        assert f.nonzero_brackets[3] is False
        assert f.nonzero_brackets[4] is False
        assert f.nonzero_brackets[5] is False

    def test_affine_formality_data(self):
        """Affine KM: ell_3 nonzero, ell_4=0."""
        f = build_linf_formality_affine()
        assert f.formality_level == 3
        assert f.nonzero_brackets[3] is True
        assert f.nonzero_brackets[4] is False

    def test_betagamma_formality_data(self):
        """betagamma: ell_3,4 nonzero, ell_5=0."""
        f = build_linf_formality_betagamma()
        assert f.formality_level == 4
        assert f.nonzero_brackets[3] is True
        assert f.nonzero_brackets[4] is True
        assert f.nonzero_brackets[5] is False

    def test_virasoro_formality_data(self):
        """Virasoro: all ell_k nonzero."""
        f = build_linf_formality_virasoro()
        assert f.formality_level is None
        for k in [2, 3, 4, 5]:
            assert f.nonzero_brackets[k] is True

    def test_shadow_formality_identification_heisenberg(self):
        """Shadow-formality identification for Heisenberg."""
        f = build_linf_formality_heisenberg()
        checks = f.verify_shadow_formality_identification()
        assert all(checks.values())

    def test_shadow_formality_identification_virasoro(self):
        """Shadow-formality identification for Virasoro at arities 2-5."""
        f = build_linf_formality_virasoro()
        checks = f.verify_shadow_formality_identification()
        assert all(checks.values())


# ========================================================================
# 4. Operadic complexity
# ========================================================================

class TestOperadicComplexity:
    """Verify operadic complexity for each class."""

    def test_opcx_G(self):
        assert operadic_complexity('G') == 2

    def test_opcx_L(self):
        assert operadic_complexity('L') == 3

    def test_opcx_C(self):
        assert operadic_complexity('C') == 4

    def test_opcx_M(self):
        assert operadic_complexity('M') is None


# ========================================================================
# 5. Four-way identification
# ========================================================================

class TestFourWayIdentification:
    """Verify the four-way identification for each class."""

    def test_class_G(self):
        result = verify_four_way_identification('G')
        assert result['all_equal'] is True
        assert result['r_max'] == 2
        assert result['ainfty_depth'] == 2
        assert result['linf_formality_level'] == 2
        assert result['operadic_complexity'] == 2

    def test_class_L(self):
        result = verify_four_way_identification('L')
        assert result['all_equal'] is True
        assert result['r_max'] == 3

    def test_class_C(self):
        result = verify_four_way_identification('C')
        assert result['all_equal'] is True
        assert result['r_max'] == 4

    def test_class_M(self):
        result = verify_four_way_identification('M')
        assert result['all_equal'] is True
        assert result['r_max'] is None  # infinity

    def test_all_classes(self):
        """All four classes satisfy the four-way identification."""
        for cls in ['G', 'L', 'C', 'M']:
            result = verify_four_way_identification(cls)
            assert result['all_equal'] is True, f"Failed for class {cls}"


# ========================================================================
# 6. Depth decomposition
# ========================================================================

class TestDepthDecomposition:
    """Verify d = 1 + d_arith + d_alg."""

    def test_class_G_d2(self):
        """Heisenberg: d = 1 + 1 + 0 = 2."""
        assert depth_decomposition(d_alg=0, d_arith=1) == 2

    def test_class_L_d3(self):
        """Affine KM: d = 1 + 1 + 1 = 3."""
        assert depth_decomposition(d_alg=1, d_arith=1) == 3

    def test_class_C_d4(self):
        """betagamma: d = 1 + 1 + 2 = 4."""
        assert depth_decomposition(d_alg=2, d_arith=1) == 4

    def test_class_M_infinity(self):
        """Virasoro: d = infinity (d_alg = infinity)."""
        assert depth_decomposition(d_alg=None, d_arith=1) is None

    def test_degenerate_d1(self):
        """Heisenberg at k=0: d = 1 + 0 + 0 = 1."""
        assert depth_decomposition(d_alg=0, d_arith=0) == 1

    def test_lattice_e8(self):
        """E_8 lattice (rank 8): d_arith = 2, d = 3."""
        # weight = 8/2 = 4, dim S_4 = 0, d_arith = 2 + 0 = 2
        assert depth_decomposition(d_alg=0, d_arith=2) == 3

    def test_lattice_leech(self):
        """Leech lattice (rank 24): d_arith = 3, d = 4."""
        # weight = 24/2 = 12, dim S_12 = 1, d_arith = 2 + 1 = 3
        assert depth_decomposition(d_alg=0, d_arith=3) == 4

    def test_algebraic_depth_G(self):
        assert algebraic_depth_from_class('G') == 0

    def test_algebraic_depth_L(self):
        assert algebraic_depth_from_class('L') == 1

    def test_algebraic_depth_C(self):
        assert algebraic_depth_from_class('C') == 2

    def test_algebraic_depth_M(self):
        assert algebraic_depth_from_class('M') is None


# ========================================================================
# 7. Arithmetic depth and cusp forms
# ========================================================================

class TestArithmeticDepth:
    """Verify cusp form dimensions and arithmetic depth."""

    def test_cusp_dim_below_12(self):
        """No cusp forms below weight 12."""
        for k in [2, 4, 6, 8, 10]:
            assert cusp_form_dim(k) == 0

    def test_cusp_dim_12(self):
        """dim S_12 = 1 (Ramanujan Delta)."""
        assert cusp_form_dim(12) == 1

    def test_cusp_dim_14(self):
        """dim S_14 = 0."""
        assert cusp_form_dim(14) == 0

    def test_cusp_dim_16(self):
        """dim S_16 = 1."""
        assert cusp_form_dim(16) == 1

    def test_cusp_dim_24(self):
        """dim S_24 = 2."""
        assert cusp_form_dim(24) == 2

    def test_cusp_dim_36(self):
        """dim S_36 = 3."""
        assert cusp_form_dim(36) == 3

    def test_cusp_dim_odd(self):
        """No cusp forms at odd weight."""
        for k in [1, 3, 5, 7, 11, 13]:
            assert cusp_form_dim(k) == 0

    def test_cusp_dim_negative(self):
        """No cusp forms at negative weight."""
        assert cusp_form_dim(-2) == 0
        assert cusp_form_dim(-12) == 0

    def test_shadow_visibility_genus(self):
        """g_min(S_r) = floor(r/2) + 1."""
        assert shadow_visibility_genus(2) == 2
        assert shadow_visibility_genus(3) == 2
        assert shadow_visibility_genus(4) == 3
        assert shadow_visibility_genus(5) == 3
        assert shadow_visibility_genus(6) == 4
        assert shadow_visibility_genus(12) == 7

    def test_cusp_form_threshold_arity(self):
        """Cusp forms first contribute at arity 12."""
        assert cusp_form_threshold_arity() == 12

    def test_cusp_form_threshold_genus(self):
        """Cusp forms first contribute at genus 6."""
        assert cusp_form_threshold_genus() == 6

    def test_ramanujan_delta_data(self):
        """Ramanujan Delta function contribution data."""
        data = ramanujan_delta_contribution_genus()
        assert data['dim_S12'] == 1
        assert data['verification'] is True
        assert data['genus_5_has_cusp'] is False
        assert data['genus_6_has_cusp'] is True

    def test_arithmetic_depth_E8(self):
        """E_8 lattice (rank 8): d_arith = 2 (weight 4, dim S_4 = 0)."""
        assert arithmetic_depth_lattice(8) == 2

    def test_arithmetic_depth_Leech(self):
        """Leech lattice (rank 24): d_arith = 3 (weight 12, dim S_12 = 1)."""
        assert arithmetic_depth_lattice(24) == 3

    def test_arithmetic_depth_rank16(self):
        """Rank-16 lattice: d_arith = 2 (weight 8, dim S_8 = 0)."""
        assert arithmetic_depth_lattice(16) == 2

    def test_arithmetic_depth_rank32(self):
        """Rank-32 lattice: d_arith = 3 (weight 16, dim S_16 = 1)."""
        assert arithmetic_depth_lattice(32) == 3

    def test_arithmetic_depth_rank48(self):
        """Rank-48 lattice: d_arith = 4 (weight 24, dim S_24 = 2)."""
        assert arithmetic_depth_lattice(48) == 4

    def test_arithmetic_depth_table_format(self):
        """Arithmetic depth table has correct format."""
        table = arithmetic_depth_table()
        assert len(table) >= 5
        for row in table:
            assert 'rank' in row
            assert 'weight' in row
            assert 'd_arith' in row
            assert 'd_total' in row

    def test_arithmetic_depth_table_consistency(self):
        """Verify d_total = 1 + d_arith + d_alg (d_alg=0 for class G)."""
        for row in arithmetic_depth_table():
            assert row['d_total'] == 1 + row['d_arith'] + 0


# ========================================================================
# 8. Categorical characterization
# ========================================================================

class TestCategorical:
    """Verify categorical characterization of D(B(A))."""

    def test_G_formal(self):
        """Class G: D(B(A)) is formal."""
        cat = categorical_characterization('G')
        assert cat.formal is True
        assert cat.n_independent_extensions == 0

    def test_L_one_extension(self):
        """Class L: exactly one non-trivial extension."""
        cat = categorical_characterization('L')
        assert cat.formal is False
        assert cat.n_independent_extensions == 1

    def test_C_two_extensions(self):
        """Class C: exactly two non-trivial extensions."""
        cat = categorical_characterization('C')
        assert cat.formal is False
        assert cat.n_independent_extensions == 2

    def test_M_infinite_extensions(self):
        """Class M: infinitely many extensions."""
        cat = categorical_characterization('M')
        assert cat.formal is False
        assert cat.n_independent_extensions is None

    def test_extension_count_matches_dalg(self):
        """Number of extensions = d_alg for finite classes."""
        for cls, expected_dalg in [('G', 0), ('L', 1), ('C', 2)]:
            cat = categorical_characterization(cls)
            assert cat.n_independent_extensions == expected_dalg


# ========================================================================
# 9. Hochschild cohomology dimension
# ========================================================================

class TestHH2:
    """Verify HH^2(H*(B(A))) dimension computation."""

    def test_hh2_G(self):
        """Class G: dim HH^2 = 1 (kappa only)."""
        data = hh2_dimension('G')
        assert data['dim_HH2_abstract'] == 1

    def test_hh2_L(self):
        """Class L: dim HH^2 = 2 (kappa and alpha)."""
        data = hh2_dimension('L')
        assert data['dim_HH2_abstract'] == 2

    def test_hh2_C(self):
        """Class C: dim HH^2 = 3 (kappa, alpha, S_4)."""
        data = hh2_dimension('C')
        assert data['dim_HH2_abstract'] == 3

    def test_hh2_M(self):
        """Class M: dim HH^2 = infinity."""
        data = hh2_dimension('M')
        assert data['dim_HH2_abstract'] is None

    def test_hh2_parameters_count(self):
        """Number of deformation parameters matches dim HH^2."""
        for cls, dim in [('G', 1), ('L', 2), ('C', 3)]:
            data = hh2_dimension(cls)
            assert len(data['deformation_parameters']) == dim

    def test_hh2_M_infinite_params(self):
        """Class M has infinitely many deformation parameters."""
        data = hh2_dimension('M')
        # The list has '...' marker
        assert len(data['deformation_parameters']) >= 4

    def test_hh2_family_virasoro(self):
        """Virasoro family: 1 continuous parameter (c)."""
        data = hh2_dimension('M', family='Virasoro')
        assert data['family_parameter_count'] == 1

    def test_hh2_family_heisenberg(self):
        """Heisenberg family: 1 continuous parameter (k)."""
        data = hh2_dimension('G', family='Heisenberg')
        assert data['family_parameter_count'] == 1


# ========================================================================
# 10. DS depth change
# ========================================================================

class TestDSDepthChange:
    """Verify depth change under Drinfeld-Sokolov reduction."""

    def test_sl2_to_virasoro(self):
        """sl_2 (class L) -> Virasoro (class M)."""
        ds = ds_depth_change('sl2')
        assert ds['source_class'] == 'L'
        assert ds['target_class'] == 'M'
        assert ds['source_depth'] == 3
        assert ds['target_depth'] is None  # infinity

    def test_sl3_to_w3(self):
        """sl_3 (class L) -> W_3 (class M)."""
        ds = ds_depth_change('sl3')
        assert ds['source_class'] == 'L'
        assert ds['target_class'] == 'M'
        assert ds['target'] == 'W_3'

    def test_sl4_to_w4(self):
        """sl_4 (class L) -> W_4 (class M)."""
        ds = ds_depth_change('sl4')
        assert ds['source_class'] == 'L'
        assert ds['target_class'] == 'M'
        assert ds['target'] == 'W_4'

    def test_ds_depth_always_increases(self):
        """DS reduction always increases depth from L to M."""
        for lt in ['sl2', 'sl3', 'sl4']:
            ds = ds_depth_change(lt)
            # Source depth (3) < target depth (infinity)
            assert ds['source_depth'] == 3
            assert ds['target_depth'] is None


# ========================================================================
# 11. Tensor product depth
# ========================================================================

class TestTensorProductDepth:
    """Verify depth under tensor product."""

    def test_G_tensor_G(self):
        """G tensor G = G: max(2, 2) = 2."""
        result = tensor_product_depth('G', 'G')
        assert result['tensor_depth'] == 2
        assert result['tensor_class'] == 'G'

    def test_G_tensor_L(self):
        """G tensor L = L: max(2, 3) = 3."""
        result = tensor_product_depth('G', 'L')
        assert result['tensor_depth'] == 3
        assert result['tensor_class'] == 'L'

    def test_L_tensor_L(self):
        """L tensor L = L: max(3, 3) = 3."""
        result = tensor_product_depth('L', 'L')
        assert result['tensor_depth'] == 3
        assert result['tensor_class'] == 'L'

    def test_G_tensor_C(self):
        """G tensor C = C: max(2, 4) = 4."""
        result = tensor_product_depth('G', 'C')
        assert result['tensor_depth'] == 4
        assert result['tensor_class'] == 'C'

    def test_L_tensor_C(self):
        """L tensor C = C: max(3, 4) = 4."""
        result = tensor_product_depth('L', 'C')
        assert result['tensor_depth'] == 4
        assert result['tensor_class'] == 'C'

    def test_any_tensor_M(self):
        """X tensor M = M for any X."""
        for cls in ['G', 'L', 'C', 'M']:
            result = tensor_product_depth(cls, 'M')
            assert result['tensor_depth'] is None
            assert result['tensor_class'] == 'M'

    def test_tensor_commutative(self):
        """Tensor product depth is commutative."""
        for a in ['G', 'L', 'C', 'M']:
            for b in ['G', 'L', 'C', 'M']:
                r1 = tensor_product_depth(a, b)
                r2 = tensor_product_depth(b, a)
                assert r1['tensor_depth'] == r2['tensor_depth']
                assert r1['tensor_class'] == r2['tensor_class']

    def test_tensor_associative_depth(self):
        """Tensor product depth is associative: max(max(a,b), c) = max(a,b,c)."""
        for a in ['G', 'L', 'C']:
            for b in ['G', 'L', 'C']:
                for cc in ['G', 'L', 'C']:
                    d_ab = tensor_product_depth(a, b)['tensor_depth']
                    # Compute class from depth
                    cls_ab = {2: 'G', 3: 'L', 4: 'C'}.get(d_ab, 'M')
                    d_abc_1 = tensor_product_depth(cls_ab, cc)['tensor_depth']

                    d_bc = tensor_product_depth(b, cc)['tensor_depth']
                    cls_bc = {2: 'G', 3: 'L', 4: 'C'}.get(d_bc, 'M')
                    d_abc_2 = tensor_product_depth(a, cls_bc)['tensor_depth']

                    assert d_abc_1 == d_abc_2


# ========================================================================
# 12. Quotient and extension depth
# ========================================================================

class TestQuotientExtensionDepth:
    """Verify depth rules for quotients and extensions."""

    def test_quotient_rule(self):
        """Quotient can only decrease or preserve depth."""
        data = quotient_depth_change()
        assert data['rule'] == 'depth(L_k) <= depth(V_k)'

    def test_extension_lower_bound(self):
        """Extension depth is bounded below by max of components."""
        data = extension_depth_change()
        assert 'max(depth(I), depth(Q)) <= depth(A)' in data['lower_bound']


# ========================================================================
# 13. Standard landscape classification
# ========================================================================

class TestStandardLandscape:
    """Verify all standard families are classified."""

    def test_all_classified(self):
        """All standard families in STANDARD_FAMILIES have 4-way match."""
        landscape = classify_standard_landscape()
        for f in landscape:
            assert f['four_way_match'] is True, f"Failed for {f['family']}"

    def test_standard_families_count(self):
        """At least 12 standard families."""
        assert len(STANDARD_FAMILIES) >= 12

    def test_all_four_classes_present(self):
        """All four shadow classes appear in the landscape."""
        classes = {f[1] for f in STANDARD_FAMILIES}
        assert classes == {'G', 'L', 'C', 'M'}

    def test_heisenberg_in_G(self):
        found = [f for f in STANDARD_FAMILIES if 'Heisenberg' in f[0]]
        assert len(found) >= 1
        assert found[0][1] == 'G'

    def test_affine_in_L(self):
        found = [f for f in STANDARD_FAMILIES if 'Affine' in f[0]]
        assert len(found) >= 1
        assert all(f[1] == 'L' for f in found)

    def test_betagamma_in_C(self):
        found = [f for f in STANDARD_FAMILIES if 'betagamma' in f[0]]
        assert len(found) >= 1
        assert found[0][1] == 'C'

    def test_virasoro_in_M(self):
        found = [f for f in STANDARD_FAMILIES if 'Virasoro' in f[0]]
        assert len(found) >= 1
        assert found[0][1] == 'M'

    def test_W_algebras_in_M(self):
        found = [f for f in STANDARD_FAMILIES if f[0].startswith('W_')]
        assert len(found) >= 2
        assert all(f[1] == 'M' for f in found)


# ========================================================================
# 14. Virasoro shadow coefficient recursion
# ========================================================================

class TestVirasoroShadowRecursion:
    """Verify the shadow coefficient recursion against closed forms."""

    def test_S2_from_recursion(self):
        """S_2 = c/2 from recursion at c=10."""
        S = virasoro_shadow_coefficients(6, central_charge=10)
        assert S[2] == Rational(5)

    def test_S3_from_recursion(self):
        """S_3 = 2 from recursion at c=10."""
        S = virasoro_shadow_coefficients(6, central_charge=10)
        assert S[3] == Rational(2)

    def test_S4_from_recursion(self):
        """S_4 = 10/[c(5c+22)] from recursion at c=10."""
        S = virasoro_shadow_coefficients(6, central_charge=10)
        expected = Rational(10, 10 * (50 + 22))  # 10 / (10 * 72) = 1/72
        assert S[4] == expected

    def test_S5_from_recursion(self):
        """S_5 = -48/[c^2(5c+22)] from recursion at c=10."""
        S = virasoro_shadow_coefficients(7, central_charge=10)
        expected = Rational(-48, 100 * 72)  # -48 / 7200 = -1/150
        assert S[5] == expected

    def test_S5_sign_negative(self):
        """S_5 is negative for positive c."""
        S = virasoro_shadow_coefficients(7, central_charge=1)
        assert S[5] < 0

    def test_shadow_alternation(self):
        """Signs alternate starting at r=5: S_4>0, S_5<0, S_6>0, ..."""
        S = virasoro_shadow_coefficients(9, central_charge=10)
        assert S[4] > 0
        assert S[5] < 0
        if 6 in S:
            assert S[6] > 0
        if 7 in S:
            assert S[7] < 0

    def test_recursion_matches_closed_form_S6(self):
        """S_6 from recursion matches closed form at c=10."""
        S = virasoro_shadow_coefficients(8, central_charge=10)
        # S_6(c) = 80(45c+193) / [3 c^3 (5c+22)^2]
        c_val = 10
        expected = Rational(80) * (45*c_val + 193) / (3 * c_val**3 * (5*c_val + 22)**2)
        assert S[6] == expected

    def test_recursion_matches_closed_form_at_c1(self):
        """Verify all recursion coefficients at c=1."""
        S = virasoro_shadow_coefficients(7, central_charge=1)
        assert S[2] == Rational(1, 2)
        assert S[3] == Rational(2)
        assert S[4] == Rational(10, 27)
        assert S[5] == Rational(-48, 27)




# ========================================================================
# 15. Cross-checks with depth_classification module
# ========================================================================

class TestCrossChecks:
    """Cross-check with the existing depth_classification module."""

    def test_kappa_heisenberg_consistent(self):
        """kappa(Heisenberg, k=1) = 1 in both modules."""
        from depth_classification import kappa_heisenberg as dc_kappa
        s = build_ainfty_heisenberg(level=1)
        assert s.shadow_coefficients[2] == dc_kappa(1)

    def test_kappa_virasoro_consistent(self):
        """kappa(Virasoro, c) = c/2 in both modules."""
        from depth_classification import kappa_virasoro as dc_kappa
        for c_val in [1, 13, 26]:
            s = build_ainfty_virasoro(central_charge=c_val)
            assert s.shadow_coefficients[2] == dc_kappa(c_val)

    def test_kappa_affine_consistent(self):
        """kappa(sl_2, k=1) consistent between modules."""
        from depth_classification import kappa_affine as dc_kappa
        s = build_ainfty_affine_km('sl2', level=1)
        expected = dc_kappa(3, 2, 1)  # dim=3, h^v=2, k=1
        assert s.shadow_coefficients[2] == expected

    def test_class_consistent(self):
        """Shadow class assignment consistent between modules."""
        from depth_classification import classify_glcm
        # G: alpha=0, delta=0
        assert classify_glcm(0, 0)[0] == 'G'
        # L: alpha!=0, delta=0
        assert classify_glcm(1, 0)[0] == 'L'
        # M: alpha!=0, delta!=0
        assert classify_glcm(1, 1)[0] == 'M'

    def test_cusp_dim_consistent(self):
        """Cusp form dimension consistent with depth_classification."""
        from depth_classification import dim_cusp_forms_sl2z as dc_cusp
        for k in [4, 6, 8, 10, 12, 16, 24, 36]:
            assert cusp_form_dim(k) == dc_cusp(k)


# ========================================================================
# 16. Comprehensive verification
# ========================================================================

class TestComprehensive:
    """Run the comprehensive verification suite."""

    def test_all_verifications_pass(self):
        """All comprehensive verifications pass."""
        results = comprehensive_verification()
        for name, ok in results.items():
            assert ok, f"Comprehensive verification failed: {name}"


# ========================================================================
# 17. Edge cases and boundary conditions
# ========================================================================

class TestEdgeCases:
    """Verify edge cases and boundary conditions."""

    def test_virasoro_c0_S5_undefined(self):
        """S_5(c=0) has a pole (c^2 in denominator)."""
        # This should NOT be computed at c=0; the algebra is degenerate
        # We just verify the formula gives a nonzero result for c != 0
        data = virasoro_ell5_nonvanishing(central_charge=Rational(1, 100))
        assert data['S_5_nonzero'] is True

    def test_depth_decomposition_large_arith(self):
        """Large arithmetic depth (rank 48 lattice)."""
        d = depth_decomposition(d_alg=0, d_arith=arithmetic_depth_lattice(48))
        assert d == 1 + arithmetic_depth_lattice(48) + 0

    def test_cusp_dim_weight_48(self):
        """dim S_48 for rank-96 lattice."""
        # 48 % 12 = 0, dim M_48 = 48/12 + 1 = 5, dim S_48 = 4
        assert cusp_form_dim(48) == 4

    def test_shadow_visibility_large_r(self):
        """Shadow visibility genus for large arities."""
        assert shadow_visibility_genus(100) == 51
        assert shadow_visibility_genus(101) == 51

    def test_tensor_all_G(self):
        """G tensor G tensor ... tensor G = G."""
        result = tensor_product_depth('G', 'G')
        assert result['tensor_class'] == 'G'

    def test_tensor_M_absorbs(self):
        """M tensor anything = M."""
        for cls in ['G', 'L', 'C', 'M']:
            result = tensor_product_depth('M', cls)
            assert result['tensor_class'] == 'M'
