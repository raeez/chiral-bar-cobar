r"""Tests for the logarithmic VOA shadow engine: triplet W(p) and singlet M(p).

Verifies:
    1. Central charge formula c(p) = 1 - 6(p-1)^2/p (multi-path)
    2. Kappa computation via three independent paths (AP48, AP20)
    3. Generator data (weights, OPE pole orders)
    4. Shadow depth classification (all class M)
    5. Zhu algebra structure (dim 2p, non-semisimple)
    6. Modular representation dimension (3p-1)
    7. Bar cohomology Koszulness prediction
    8. Singlet M(p) vs triplet W(p) comparison
    9. Koszul dual and complementarity (AP24: sum = 13)
    10. Screening parameter consistency
    11. W(2) vs bc ghost system distinction
    12. Shadow tower: vacuum level = Virasoro sub-VOA
    13. Logarithmic effects on shadow tower
    14. Cross-family consistency (kappa additivity)
    15. Shadow metric and discriminant

MANDATE: 3+ independent verification paths per result.

References:
    Kausch (1991), Gaberdiel-Kausch (1996), Adamovic-Milas (2008),
    Feigin-Gainutdinov-Semikhatov-Tipunin (2006), Nagatomo-Tsuchiya (2009),
    Miyamoto (2004), Creutzig-Ridout (2013).
    Manuscript: grand_synthesis_engine.py, higher_genus_modular_koszul.tex,
    concordance.tex.
"""

import pytest
import unittest
from fractions import Fraction

from sympy import Rational, simplify

from compute.lib.logarithmic_voa_shadow_engine import (
    # Central charge
    triplet_central_charge,
    singlet_central_charge,
    triplet_central_charges_table,
    # Screening
    screening_parameters,
    # Generators
    triplet_generators,
    TripletGeneratorData,
    # Kappa
    kappa_path1_virasoro,
    kappa_path2_character,
    kappa_path3_screening,
    verify_kappa_multipath,
    # OPE
    triplet_TT_ope,
    triplet_TW_ope,
    triplet_WW_ope_pole_order,
    triplet_WW_leading_coefficient,
    triplet_ope_summary,
    # Bar complex
    bar_differential_structure,
    bar_cohomology_prediction,
    # Shadow depth
    shadow_depth_class,
    # Zhu algebra
    zhu_algebra_dimension,
    zhu_algebra_structure,
    # Modules
    logarithmic_module_data,
    projective_cover_structure,
    # Modular
    modular_representation_dimension,
    modular_s_matrix_structure,
    t_matrix_jordan_structure,
    # Singlet
    singlet_data,
    # Shadow tower
    shadow_tower_arity2,
    shadow_tower_arity3,
    shadow_tower_quartic_contact,
    shadow_tower_vs_zhu,
    # Koszul dual
    koszul_dual_prediction,
    # Comprehensive
    comprehensive_triplet_analysis,
    triplet_landscape_table,
    # Cross-family
    kappa_additivity_check,
    complementarity_consistency,
    w2_bc_ghost_comparison,
    triplet_vs_virasoro_comparison,
    # Pseudo-trace
    pseudotrace_genus1_structure,
    # Logarithmic effect
    logarithmic_shadow_effect,
    # Shadow metric
    shadow_metric_coefficients,
    # Master table
    master_invariant_table,
)


# =========================================================================
# 1. Central charge: c(p) = 1 - 6(p-1)^2/p
# =========================================================================

class TestCentralCharge(unittest.TestCase):
    """Central charge formula verification.

    Three independent paths:
      Path 1: Direct formula c = 1 - 6(p-1)^2/p
      Path 2: Feigin-Fuchs c = 1 - 3Q^2 from screening parameters
      Path 3: Known values from the literature
    """

    def test_explicit_values(self):
        """Verify against published central charges."""
        # Path 3: literature values
        # Recomputed from first principles: c(p) = 1 - 6(p-1)^2/p
        # p=4: 1 - 6*9/4 = 1 - 27/2 = -25/2
        # p=5: 1 - 6*16/5 = 1 - 96/5 = -91/5
        # p=6: 1 - 6*25/6 = 1 - 25 = -24
        known = {
            2: Rational(-2),
            3: Rational(-7),
            4: Rational(-25, 2),  # 1 - 54/4 = -25/2
            5: Rational(-91, 5),  # 1 - 96/5 = -91/5
            6: Rational(-24),     # 1 - 150/6 = -24
        }
        for p, c_expected in known.items():
            c = triplet_central_charge(p)
            self.assertEqual(c, c_expected,
                             f"W({p}): c = {c}, expected {c_expected}")

    def test_direct_formula(self):
        """Path 1: verify c = 1 - 6(p-1)^2/p from definition."""
        for p in range(2, 12):
            c = triplet_central_charge(p)
            c_manual = Rational(1) - Rational(6 * (p-1)**2, p)
            self.assertEqual(c, c_manual, f"Formula mismatch at p={p}")

    def test_screening_consistency(self):
        """Path 2: verify c from screening parameters Q^2."""
        for p in range(2, 10):
            params = screening_parameters(p)
            self.assertTrue(params['c_consistent'],
                            f"Screening inconsistency at p={p}")
            self.assertEqual(params['c_from_Q'], params['c_from_formula'],
                             f"c mismatch at p={p}")

    def test_singlet_same_as_triplet(self):
        """Singlet and triplet have the same central charge."""
        for p in range(2, 10):
            self.assertEqual(triplet_central_charge(p),
                             singlet_central_charge(p))

    def test_c_monotone_decreasing(self):
        """Central charge is monotone decreasing for p >= 2."""
        for p in range(2, 20):
            c_p = triplet_central_charge(p)
            c_next = triplet_central_charge(p + 1)
            self.assertGreater(c_p, c_next,
                               f"c not decreasing at p={p}")

    def test_c_limit_as_p_to_infinity(self):
        """c(p) -> -infinity as p -> infinity."""
        c_100 = triplet_central_charge(100)
        self.assertLess(float(c_100), -500)

    def test_c_at_p2_is_minus_2(self):
        """W(2) has c = -2 (symplectic fermion central charge)."""
        self.assertEqual(triplet_central_charge(2), Rational(-2))

    def test_central_charges_table(self):
        """Table generation works and is consistent."""
        table = triplet_central_charges_table(8)
        self.assertEqual(len(table), 7)  # p = 2, ..., 8
        for p, c in table.items():
            self.assertEqual(c, triplet_central_charge(p))


# =========================================================================
# 2. Kappa multi-path verification (AP48, AP20, AP39)
# =========================================================================

class TestKappaMultiPath(unittest.TestCase):
    """Kappa verification via three independent paths.

    AP48: kappa depends on the full algebra, not just c.
    For W(p), kappa = c(p)/2 because the genus-1 obstruction
    is controlled by the Virasoro sector.
    """

    def test_three_paths_agree(self):
        """All three kappa paths agree for p = 2, ..., 10."""
        for p in range(2, 11):
            result = verify_kappa_multipath(p)
            self.assertTrue(result['all_agree'],
                            f"Kappa paths disagree at p={p}")

    def test_kappa_equals_c_over_2(self):
        """kappa(W(p)) = c(p)/2."""
        for p in range(2, 15):
            c = triplet_central_charge(p)
            kappa = kappa_path1_virasoro(p)
            self.assertEqual(kappa, c / 2,
                             f"kappa != c/2 at p={p}")

    def test_kappa_explicit_values(self):
        """Verify kappa at specific p values."""
        # W(2): c=-2, kappa=-1
        self.assertEqual(kappa_path1_virasoro(2), Rational(-1))
        # W(3): c=-7, kappa=-7/2
        self.assertEqual(kappa_path1_virasoro(3), Rational(-7, 2))
        # W(4): c=-25/2, kappa=-25/4
        self.assertEqual(kappa_path1_virasoro(4), Rational(-25, 4))

    def test_kappa_not_zero_for_p_geq_2(self):
        """kappa(W(p)) != 0 for all p >= 2 (c < 0 => kappa < 0)."""
        for p in range(2, 20):
            kappa = kappa_path1_virasoro(p)
            self.assertNotEqual(kappa, 0,
                                f"kappa = 0 at p={p}")
            self.assertLess(kappa, 0,
                            f"kappa > 0 at p={p} (expected negative)")

    def test_obs1_formula(self):
        """obs_1 = kappa/24."""
        for p in range(2, 10):
            result = verify_kappa_multipath(p)
            self.assertEqual(result['obs_1'], result['kappa'] / 24)

    def test_kappa_screening_path(self):
        """Screening path gives same kappa."""
        for p in range(2, 10):
            k1 = kappa_path1_virasoro(p)
            k3 = kappa_path3_screening(p)
            self.assertEqual(k1, k3,
                             f"Virasoro and screening paths disagree at p={p}")


# =========================================================================
# 3. Generator data
# =========================================================================

class TestGeneratorData(unittest.TestCase):
    """Generator structure for W(p)."""

    def test_n_generators(self):
        """W(p) has exactly 2 strong generators."""
        for p in range(2, 10):
            gen = triplet_generators(p)
            self.assertEqual(gen.n_generators, 2)

    def test_T_weight(self):
        """T (Virasoro) has weight 2."""
        for p in range(2, 10):
            gen = triplet_generators(p)
            self.assertEqual(gen.T_weight, 2)

    def test_W_weight(self):
        """W has weight 2p-1."""
        for p in range(2, 10):
            gen = triplet_generators(p)
            self.assertEqual(gen.W_weight, 2 * p - 1)

    def test_W_weight_explicit(self):
        """Explicit W weights: p=2->3, p=3->5, p=4->7, p=5->9."""
        expected = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11}
        for p, w in expected.items():
            gen = triplet_generators(p)
            self.assertEqual(gen.W_weight, w)

    def test_not_uniform_weight(self):
        """Generators are NOT uniform weight for any p >= 2."""
        for p in range(2, 10):
            gen = triplet_generators(p)
            self.assertFalse(gen.is_uniform_weight,
                             f"W({p}) falsely claimed uniform weight")

    def test_max_ope_pole(self):
        """Max OPE pole order = 2*(2p-1)."""
        for p in range(2, 10):
            gen = triplet_generators(p)
            self.assertEqual(gen.max_ope_pole_order, 2 * (2 * p - 1))

    def test_bar_r_matrix_pole(self):
        """Bar r-matrix max pole = OPE max pole - 1 (AP19)."""
        for p in range(2, 10):
            gen = triplet_generators(p)
            self.assertEqual(gen.bar_r_matrix_max_pole,
                             gen.max_ope_pole_order - 1)


# =========================================================================
# 4. OPE structure
# =========================================================================

class TestOPEStructure(unittest.TestCase):
    """OPE structure for W(p)."""

    def test_TT_ope_pole_4(self):
        """T-T OPE has max pole 4 (Virasoro)."""
        for p in range(2, 8):
            ope = triplet_TT_ope(p)
            self.assertEqual(max(ope.keys()), 4)

    def test_TT_leading_coefficient(self):
        """T-T leading: c/2."""
        for p in range(2, 8):
            ope = triplet_TT_ope(p)
            c = triplet_central_charge(p)
            self.assertEqual(ope[4], c / 2)

    def test_TW_primary(self):
        """T-W OPE: W is a primary (max pole 2)."""
        for p in range(2, 8):
            ope = triplet_TW_ope(p)
            self.assertEqual(max(ope.keys()), 2)

    def test_WW_pole_order(self):
        """W-W pole order = 2*(2p-1)."""
        self.assertEqual(triplet_WW_ope_pole_order(2), 6)
        self.assertEqual(triplet_WW_ope_pole_order(3), 10)
        self.assertEqual(triplet_WW_ope_pole_order(4), 14)
        self.assertEqual(triplet_WW_ope_pole_order(5), 18)

    def test_ope_summary_consistency(self):
        """OPE summary is internally consistent."""
        for p in range(2, 8):
            summary = triplet_ope_summary(p)
            self.assertEqual(summary['overall_max_pole'],
                             summary['WW_max_pole'])
            self.assertEqual(summary['bar_r_matrix_max_pole'],
                             summary['overall_max_pole'] - 1)

    def test_not_quadratic_for_all_p(self):
        """W(p) has non-quadratic OPE for all p >= 2."""
        for p in range(2, 10):
            summary = triplet_ope_summary(p)
            self.assertFalse(summary['is_quadratic_ope'],
                             f"W({p}) falsely claimed quadratic")


# =========================================================================
# 5. Bar complex structure
# =========================================================================

class TestBarComplex(unittest.TestCase):
    """Bar complex and Koszulness for W(p)."""

    def test_bar_structure(self):
        """Bar differential structure is well-defined."""
        for p in range(2, 8):
            data = bar_differential_structure(p)
            self.assertEqual(data['n_generators'], 2)
            self.assertEqual(data['max_ope_pole'],
                             triplet_WW_ope_pole_order(p))

    def test_no_e2_collapse(self):
        """PBW spectral sequence does NOT collapse at E_2."""
        for p in range(2, 8):
            data = bar_differential_structure(p)
            self.assertFalse(data['e2_collapse'],
                             f"W({p}) falsely has E_2 collapse")

    def test_koszulness_status_open(self):
        """W(p) Koszulness is OPEN (neither proved nor disproved).

        Beilinson rectification: the previous test falsely asserted Koszul.
        Free strong generation of a screening kernel is NOT automatic.
        The koszulness_landscape.py correctly records W(2) as OPEN.
        """
        for p in range(2, 10):
            pred = bar_cohomology_prediction(p)
            self.assertIsNone(pred['koszul_prediction'],
                              f"W({p}) should be OPEN, not decided")
            self.assertIsNone(pred['freely_strongly_generated'],
                              f"W({p}) free strong gen should be unknown")
            self.assertIsNone(pred['vacuum_null_vectors'],
                              f"W({p}) null vector status should be unknown")

    def test_bar_concentration_open(self):
        """Bar concentration status is OPEN (follows Koszulness)."""
        for p in range(2, 10):
            pred = bar_cohomology_prediction(p)
            self.assertIsNone(pred['bar_degree_1_concentrated'],
                              f"W({p}) bar concentration should be unknown")
            self.assertIsNone(pred['H2_prediction'],
                              f"W({p}) H2 prediction should be unknown")
            self.assertIsNone(pred['H_geq2_prediction'],
                              f"W({p}) H_geq2 prediction should be unknown")


# =========================================================================
# 6. Shadow depth classification
# =========================================================================

class TestShadowDepth(unittest.TestCase):
    """Shadow depth classification for W(p)."""

    def test_all_class_M(self):
        """All W(p) for p >= 2 are class M (infinite tower)."""
        for p in range(2, 15):
            data = shadow_depth_class(p)
            self.assertEqual(data['shadow_class'], 'M',
                             f"W({p}) not class M")
            self.assertEqual(data['r_max'], float('inf'))

    def test_d_alg_infinite(self):
        """Algebraic depth is infinite for all W(p)."""
        for p in range(2, 10):
            data = shadow_depth_class(p)
            self.assertEqual(data['d_alg'], float('inf'))

    def test_ww_ope_pole_in_reason(self):
        """Shadow depth reason mentions W-W OPE pole order."""
        for p in range(2, 8):
            data = shadow_depth_class(p)
            ww_pole = triplet_WW_ope_pole_order(p)
            self.assertIn(str(ww_pole), data['reason'])


# =========================================================================
# 7. Zhu algebra
# =========================================================================

class TestZhuAlgebra(unittest.TestCase):
    """Zhu algebra A(W(p)).

    Three paths:
      Path 1: dim A(W(p)) = 2p (Adamovic-Milas)
      Path 2: number of simple modules = 2p
      Path 3: structure (non-semisimple, nilpotent radical dim p)
    """

    def test_dimension_formula(self):
        """dim A(W(p)) = 2p."""
        for p in range(2, 15):
            self.assertEqual(zhu_algebra_dimension(p), 2 * p)

    def test_explicit_dimensions(self):
        """Explicit: dim A(W(2))=4, A(W(3))=6, A(W(4))=8."""
        self.assertEqual(zhu_algebra_dimension(2), 4)
        self.assertEqual(zhu_algebra_dimension(3), 6)
        self.assertEqual(zhu_algebra_dimension(4), 8)
        self.assertEqual(zhu_algebra_dimension(5), 10)

    def test_non_semisimple(self):
        """Zhu algebra is NOT semisimple (logarithmic feature)."""
        for p in range(2, 10):
            data = zhu_algebra_structure(p)
            self.assertFalse(data['is_semisimple'])

    def test_nilpotent_radical(self):
        """Nilpotent radical has dimension p."""
        for p in range(2, 10):
            data = zhu_algebra_structure(p)
            self.assertEqual(data['nilpotent_radical_dim'], p)
            self.assertEqual(data['semisimple_quotient_dim'], p)

    def test_n_simple_modules(self):
        """Number of simple modules = 2p."""
        for p in range(2, 10):
            data = zhu_algebra_structure(p)
            self.assertEqual(data['n_simple_modules'], 2 * p)

    def test_vacuum_weight_zero(self):
        """Vacuum module has conformal weight 0."""
        for p in range(2, 8):
            data = zhu_algebra_structure(p)
            self.assertEqual(data['vacuum_weight'], Rational(0))

    def test_dim_decomposition(self):
        """dim = semisimple + nilpotent."""
        for p in range(2, 10):
            data = zhu_algebra_structure(p)
            self.assertEqual(data['dim_zhu'],
                             data['semisimple_quotient_dim'] +
                             data['nilpotent_radical_dim'])


# =========================================================================
# 8. Modular representation
# =========================================================================

class TestModularRepresentation(unittest.TestCase):
    """SL(2,Z) representation on W(p) characters."""

    def test_dimension_formula(self):
        """dim = 3p - 1 (FGST 2006)."""
        for p in range(2, 15):
            self.assertEqual(modular_representation_dimension(p),
                             3 * p - 1)

    def test_explicit_dimensions(self):
        """Explicit: p=2->5, p=3->8, p=4->11, p=5->14."""
        self.assertEqual(modular_representation_dimension(2), 5)
        self.assertEqual(modular_representation_dimension(3), 8)
        self.assertEqual(modular_representation_dimension(4), 11)
        self.assertEqual(modular_representation_dimension(5), 14)

    def test_decomposition(self):
        """Dimension decomposes: p traces + (2p-1) pseudo-traces."""
        for p in range(2, 10):
            data = modular_s_matrix_structure(p)
            self.assertEqual(data['n_traces'] + data['n_pseudotraces'],
                             data['dim'])

    def test_not_unitary(self):
        """S-matrix is NOT unitary."""
        for p in range(2, 8):
            data = modular_s_matrix_structure(p)
            self.assertFalse(data['is_unitary'])

    def test_T_has_jordan_blocks(self):
        """T-matrix has Jordan blocks (logarithmic)."""
        for p in range(2, 8):
            data = modular_s_matrix_structure(p)
            self.assertTrue(data['T_has_jordan_blocks'])

    def test_verlinde_does_not_apply(self):
        """Standard Verlinde formula does NOT apply."""
        for p in range(2, 8):
            data = modular_s_matrix_structure(p)
            self.assertFalse(data['verlinde_applies'])

    def test_jordan_structure(self):
        """T-matrix Jordan block structure is consistent."""
        for p in range(2, 8):
            data = t_matrix_jordan_structure(p)
            self.assertEqual(len(data['ordinary_eigenvalues']), p)
            self.assertGreaterEqual(data['n_jordan_blocks'], 0)


# =========================================================================
# 9. Singlet M(p) vs triplet W(p)
# =========================================================================

class TestSingletVsTriplet(unittest.TestCase):
    """Comparison of singlet M(p) and triplet W(p)."""

    def test_same_central_charge(self):
        """M(p) and W(p) have the same central charge."""
        for p in range(2, 10):
            self.assertEqual(singlet_central_charge(p),
                             triplet_central_charge(p))

    def test_singlet_not_c2_cofinite(self):
        """M(p) is NOT C_2-cofinite (unlike W(p))."""
        for p in range(2, 8):
            data = singlet_data(p)
            self.assertFalse(data['c2_cofinite'])

    def test_singlet_infinitely_many_modules(self):
        """M(p) has infinitely many simple modules."""
        for p in range(2, 8):
            data = singlet_data(p)
            self.assertEqual(data['n_simple_modules'], float('inf'))

    def test_singlet_same_kappa(self):
        """M(p) and W(p) have the same kappa."""
        for p in range(2, 10):
            data = singlet_data(p)
            c = triplet_central_charge(p)
            self.assertEqual(data['kappa'], c / 2)

    def test_singlet_koszul_open(self):
        """M(p) Koszulness is OPEN (same status as W(p))."""
        for p in range(2, 8):
            data = singlet_data(p)
            self.assertIsNone(data['koszul_prediction'])

    def test_singlet_class_M(self):
        """M(p) is class M (contains Virasoro sub-VOA)."""
        for p in range(2, 8):
            data = singlet_data(p)
            self.assertEqual(data['shadow_class'], 'M')


# =========================================================================
# 10. Koszul dual and complementarity (AP24)
# =========================================================================

class TestKoszulDualComplementarity(unittest.TestCase):
    """Koszul dual structure and complementarity sum.

    AP24: kappa(A) + kappa(A!) = 13 for Virasoro-type families.
    """

    def test_complementarity_sum_13(self):
        """kappa(W(p)) + kappa(W(p)^!) = 13 for all p."""
        for p in range(2, 15):
            data = koszul_dual_prediction(p)
            self.assertEqual(data['complementarity_sum'], 13)
            self.assertTrue(data['complementarity_sum_equals_13'])

    def test_dual_central_charge(self):
        """c^! = 26 - c."""
        for p in range(2, 10):
            data = koszul_dual_prediction(p)
            c = triplet_central_charge(p)
            self.assertEqual(data['c_dual'], 26 - c)

    def test_dual_kappa(self):
        """kappa^! = (26 - c)/2 = 13 - kappa."""
        for p in range(2, 10):
            data = koszul_dual_prediction(p)
            self.assertEqual(data['kappa_dual'], 13 - data['kappa'])

    def test_consistency_batch(self):
        """Batch complementarity check."""
        result = complementarity_consistency(12)
        self.assertTrue(result['all_equal_13'])

    def test_kappa_dual_positive_for_all_p(self):
        """kappa^! > 0 for all p >= 2 (since c < 0 => kappa < 0 => kappa^! > 13)."""
        for p in range(2, 15):
            data = koszul_dual_prediction(p)
            self.assertGreater(data['kappa_dual'], 0)
            self.assertGreater(data['kappa_dual'], 13)


# =========================================================================
# 11. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Cross-family checks for the triplet family."""

    def test_kappa_additivity(self):
        """Kappa is additive for tensor products."""
        for p in range(2, 7):
            result = kappa_additivity_check(p)
            self.assertTrue(result['all_agree'],
                            f"Additivity fails at p={p}")

    def test_w2_vs_bc(self):
        """W(2) and bc ghost system: same kappa, different algebras."""
        data = w2_bc_ghost_comparison()
        self.assertTrue(data['kappas_equal'])
        self.assertFalse(data['algebras_isomorphic'])
        self.assertEqual(data['W2_class'], 'M')
        self.assertEqual(data['bc_class'], 'G')
        self.assertTrue(data['W2_c2_cofinite'])
        self.assertFalse(data['bc_c2_cofinite'])

    def test_triplet_vs_virasoro(self):
        """W(p) and Vir_{c(p)}: same kappa, different algebras."""
        for p in range(2, 8):
            data = triplet_vs_virasoro_comparison(p)
            self.assertTrue(data['kappas_equal'])
            self.assertEqual(data['triplet_n_generators'], 2)
            self.assertEqual(data['virasoro_n_generators'], 1)
            self.assertTrue(data['triplet_c2_cofinite'])
            self.assertFalse(data['virasoro_c2_cofinite'])

    def test_triplet_modules_finite(self):
        """W(p) has finitely many (2p) simple modules."""
        for p in range(2, 8):
            data = triplet_vs_virasoro_comparison(p)
            self.assertEqual(data['triplet_n_simple_modules'], 2 * p)


# =========================================================================
# 12. Shadow tower structure
# =========================================================================

class TestShadowTower(unittest.TestCase):
    """Shadow obstruction tower for W(p)."""

    def test_arity2_kappa(self):
        """Arity-2 shadow = kappa = c/2."""
        for p in range(2, 10):
            data = shadow_tower_arity2(p)
            self.assertEqual(data['kappa'], data['c'] / 2)

    def test_arity2_obs1(self):
        """obs_1 = kappa/24."""
        for p in range(2, 10):
            data = shadow_tower_arity2(p)
            self.assertEqual(data['obs_1'], data['kappa'] / 24)

    def test_arity3_has_virasoro_contribution(self):
        """Cubic shadow has Virasoro contribution."""
        for p in range(2, 8):
            data = shadow_tower_arity3(p)
            self.assertTrue(data['has_W_contribution'])

    def test_arity3_S3_virasoro(self):
        """S_3 from Virasoro: -48/(c^2*(5c+22))."""
        for p in range(2, 8):
            data = shadow_tower_arity3(p)
            c = triplet_central_charge(p)
            if c != 0:
                expected = Rational(-48) / (c**2 * (5*c + 22))
                self.assertEqual(data['S3_virasoro_contribution'], expected)

    def test_quartic_contact(self):
        """Quartic contact invariant from Virasoro: 10/(c*(5c+22))."""
        for p in range(2, 8):
            data = shadow_tower_quartic_contact(p)
            c = triplet_central_charge(p)
            if c != 0 and (5*c + 22) != 0:
                expected = Rational(10) / (c * (5*c + 22))
                self.assertEqual(data['Q_contact_virasoro'], expected)

    def test_shadow_vs_zhu_structure(self):
        """Shadow tower sees more than Zhu algebra."""
        for p in range(2, 6):
            data = shadow_tower_vs_zhu(p)
            self.assertEqual(data['shadow_class'], 'M')
            self.assertEqual(data['shadow_r_max'], float('inf'))
            self.assertGreater(data['zhu_dimension'], 0)


# =========================================================================
# 13. Pseudo-trace and logarithmic effects
# =========================================================================

class TestPseudoTraceAndLogarithmic(unittest.TestCase):
    """Pseudo-trace genus-1 structure and logarithmic effects."""

    def test_vacuum_pseudotrace_zero(self):
        """Pseudo-trace contribution to vacuum genus-1 is zero."""
        for p in range(2, 8):
            data = pseudotrace_genus1_structure(p)
            self.assertEqual(data['F1_pseudotrace_vacuum'], Rational(0))

    def test_F1_total_equals_kappa_over_24(self):
        """Total vacuum F_1 = kappa/24 (no pseudo-trace correction)."""
        for p in range(2, 8):
            data = pseudotrace_genus1_structure(p)
            self.assertEqual(data['F1_total_vacuum'],
                             data['kappa'] / 24)

    def test_n_pseudotrace_functions(self):
        """Number of pseudo-trace functions = 2p-1."""
        for p in range(2, 10):
            data = pseudotrace_genus1_structure(p)
            self.assertEqual(data['n_pseudotrace_functions'],
                             2 * p - 1)

    def test_total_modular_functions(self):
        """Total modular functions = 3p-1."""
        for p in range(2, 10):
            data = pseudotrace_genus1_structure(p)
            self.assertEqual(data['total_modular_functions'],
                             3 * p - 1)

    def test_logarithmic_invisible_at_vacuum(self):
        """Logarithmic structure invisible at vacuum level."""
        for p in range(2, 8):
            data = logarithmic_shadow_effect(p)
            self.assertTrue(data['vacuum_shadow_same_as_virasoro'])

    def test_logarithmic_visible_at_module_level(self):
        """Logarithmic structure visible at module level."""
        for p in range(2, 8):
            data = logarithmic_shadow_effect(p)
            self.assertTrue(data['logarithmic_visible_at']
                            ['module_level_shadows'])
            self.assertTrue(data['logarithmic_visible_at']
                            ['genus_2_planted_forest'])


# =========================================================================
# 14. Shadow metric and discriminant
# =========================================================================

class TestShadowMetric(unittest.TestCase):
    """Shadow metric coefficients for W(p)."""

    def test_delta_nonzero(self):
        """Critical discriminant Delta != 0 (class M confirmation)."""
        for p in range(2, 8):
            data = shadow_metric_coefficients(p)
            if not data.get('degenerate', False):
                self.assertTrue(data['Delta_nonzero'],
                                f"Delta = 0 at p={p}")

    def test_class_M_from_delta(self):
        """Class M confirmed from Delta != 0."""
        for p in range(2, 8):
            data = shadow_metric_coefficients(p)
            if not data.get('degenerate', False):
                self.assertEqual(data['shadow_class_from_Delta'], 'M')

    def test_S3_formula(self):
        """S_3 = -48/(c^2*(5c+22))."""
        for p in range(2, 8):
            data = shadow_metric_coefficients(p)
            if not data.get('degenerate', False):
                c = data['c']
                expected = Rational(-48) / (c**2 * (5*c + 22))
                self.assertEqual(data['S3'], expected)

    def test_S4_formula(self):
        """S_4 = 10/(c*(5c+22)) = Q^contact_Vir."""
        for p in range(2, 8):
            data = shadow_metric_coefficients(p)
            if not data.get('degenerate', False):
                c = data['c']
                expected = Rational(10) / (c * (5*c + 22))
                self.assertEqual(data['S4'], expected)


# =========================================================================
# 15. Projective cover structure
# =========================================================================

class TestProjectiveCovers(unittest.TestCase):
    """Projective cover structure in W(p) module category."""

    def test_projective_covers_exist(self):
        """Every simple has a projective cover."""
        for p in range(2, 8):
            data = projective_cover_structure(p)
            self.assertEqual(len(data['projective_covers']), p)

    def test_loewy_lengths(self):
        """Loewy length: 2 for boundary, 3 for interior."""
        for p in range(3, 8):  # p >= 3 for interior modules
            data = projective_cover_structure(p)
            covers = data['projective_covers']
            # s=1: boundary, loewy = 2 or 3 depending on neighbors
            # Internal modules (2 <= s <= p-1): loewy = 3
            for s in range(2, p):
                self.assertEqual(covers[s]['loewy_length'], 3)


# =========================================================================
# 16. Comprehensive analysis
# =========================================================================

class TestComprehensiveAnalysis(unittest.TestCase):
    """Comprehensive analysis integration tests."""

    def test_analysis_p2(self):
        """Full analysis for W(2)."""
        a = comprehensive_triplet_analysis(2)
        self.assertEqual(a.c, Rational(-2))
        self.assertEqual(a.kappa, Rational(-1))
        self.assertEqual(a.zhu_dim, 4)
        self.assertEqual(a.n_simple_modules, 4)
        self.assertEqual(a.modular_rep_dim, 5)
        self.assertEqual(a.shadow_class, 'M')
        self.assertIsNone(a.koszul)  # OPEN
        self.assertTrue(a.c2_cofinite)
        self.assertEqual(a.complementarity_sum, 13)

    def test_analysis_p3(self):
        """Full analysis for W(3)."""
        a = comprehensive_triplet_analysis(3)
        self.assertEqual(a.c, Rational(-7))
        self.assertEqual(a.kappa, Rational(-7, 2))
        self.assertEqual(a.zhu_dim, 6)
        self.assertEqual(a.n_simple_modules, 6)
        self.assertEqual(a.modular_rep_dim, 8)
        self.assertEqual(a.shadow_class, 'M')
        self.assertIsNone(a.koszul)  # OPEN

    def test_analysis_p5(self):
        """Full analysis for W(5)."""
        a = comprehensive_triplet_analysis(5)
        # c(5) = 1 - 6*16/5 = 1 - 96/5 = -91/5
        self.assertEqual(a.c, Rational(-91, 5))
        self.assertEqual(a.kappa, Rational(-91, 10))
        self.assertEqual(a.zhu_dim, 10)
        self.assertEqual(a.n_simple_modules, 10)
        self.assertEqual(a.modular_rep_dim, 14)
        self.assertEqual(a.ww_ope_pole_order, 18)

    def test_landscape_table(self):
        """Landscape table is consistent."""
        table = triplet_landscape_table(6)
        self.assertEqual(len(table), 5)  # p = 2, ..., 6
        for entry in table:
            self.assertEqual(entry['comp_sum'], 13)
            self.assertEqual(entry['shadow_class'], 'M')
            self.assertIsNone(entry['koszul'])  # OPEN
            self.assertTrue(entry['C_2_cofinite'])

    def test_master_table(self):
        """Master invariant table is self-consistent."""
        table = master_invariant_table(5)
        self.assertEqual(len(table), 4)  # p = 2, ..., 5
        for entry in table:
            self.assertEqual(entry['comp_sum'], 13)
            self.assertEqual(entry['zhu_dim'], 2 * entry['p'])
            self.assertEqual(entry['n_simple'], 2 * entry['p'])
            self.assertEqual(entry['modular_dim'], 3 * entry['p'] - 1)


# =========================================================================
# 17. Numerical consistency checks
# =========================================================================

class TestNumericalConsistency(unittest.TestCase):
    """Numerical cross-checks for computational consistency."""

    def test_c_values_float(self):
        """Float values of c match expectations (recomputed from 1 - 6(p-1)^2/p)."""
        self.assertAlmostEqual(float(triplet_central_charge(2)), -2.0)
        self.assertAlmostEqual(float(triplet_central_charge(3)), -7.0)
        self.assertAlmostEqual(float(triplet_central_charge(4)), -12.5)   # -25/2
        self.assertAlmostEqual(float(triplet_central_charge(5)), -18.2)   # -91/5

    def test_kappa_values_float(self):
        """Float values of kappa match expectations (kappa = c/2)."""
        self.assertAlmostEqual(float(kappa_path1_virasoro(2)), -1.0)
        self.assertAlmostEqual(float(kappa_path1_virasoro(3)), -3.5)
        self.assertAlmostEqual(float(kappa_path1_virasoro(4)), -6.25)  # -25/4

    def test_obs1_values(self):
        """obs_1 = kappa/24 numerical check."""
        self.assertAlmostEqual(
            float(verify_kappa_multipath(2)['obs_1']),
            -1.0/24)
        self.assertAlmostEqual(
            float(verify_kappa_multipath(3)['obs_1']),
            -7.0/48)

    def test_dual_kappa_positive(self):
        """All dual kappas are positive (c < 0 => c^! > 26)."""
        for p in range(2, 20):
            kd = koszul_dual_prediction(p)
            self.assertGreater(float(kd['kappa_dual']), 13)


# =========================================================================
# 18. Boundary cases and error handling
# =========================================================================

class TestBoundaryAndErrors(unittest.TestCase):
    """Boundary cases and error handling."""

    def test_p_less_than_2_raises(self):
        """p < 2 raises ValueError."""
        with self.assertRaises(ValueError):
            triplet_central_charge(1)
        with self.assertRaises(ValueError):
            triplet_central_charge(0)
        with self.assertRaises(ValueError):
            triplet_central_charge(-1)

    def test_large_p(self):
        """Large p values work without error."""
        c = triplet_central_charge(100)
        self.assertIsNotNone(c)
        self.assertLess(float(c), -500)

        gen = triplet_generators(100)
        self.assertEqual(gen.W_weight, 199)

    def test_very_large_p(self):
        """Very large p: c ~ -6p as p -> infinity."""
        p = 1000
        c = triplet_central_charge(p)
        # c = 1 - 6(p-1)^2/p ~ -6p + 12 - 6/p ~ -6p for large p
        self.assertAlmostEqual(float(c) / (-6 * p), 1.0, places=2)


# =========================================================================
# 19. Multi-path verification manifest
# =========================================================================

class TestMultiPathManifest(unittest.TestCase):
    """Verify that every key claim has 3+ independent verification paths.

    This test class verifies the verification infrastructure itself.
    """

    def test_central_charge_3_paths(self):
        """Central charge verified via 3 paths."""
        for p in [2, 3, 5]:
            # Path 1: direct formula
            c1 = triplet_central_charge(p)
            # Path 2: screening parameter
            params = screening_parameters(p)
            c2 = params['c_from_Q']
            # Path 3: explicit known value
            known = {2: Rational(-2), 3: Rational(-7),
                     5: Rational(-91, 5)}
            c3 = known[p]
            self.assertEqual(c1, c2)
            self.assertEqual(c1, c3)

    def test_kappa_3_paths(self):
        """Kappa verified via 3 paths."""
        for p in [2, 3, 5]:
            k1 = kappa_path1_virasoro(p)
            k2 = kappa_path2_character(p)
            k3 = kappa_path3_screening(p)
            self.assertEqual(k1, k2)
            self.assertEqual(k1, k3)

    def test_complementarity_3_paths(self):
        """Complementarity sum verified via 3 paths."""
        for p in [2, 3, 5]:
            # Path 1: direct computation
            kappa = kappa_path1_virasoro(p)
            kd = koszul_dual_prediction(p)
            sum1 = kappa + kd['kappa_dual']
            # Path 2: c + c^! = 26
            c = triplet_central_charge(p)
            sum2 = (c + (26 - c)) / 2
            # Path 3: structural (always 13 for Virasoro-type)
            sum3 = Rational(13)
            self.assertEqual(sum1, sum2)
            self.assertEqual(sum1, sum3)

    def test_zhu_dim_3_paths(self):
        """Zhu dimension verified via 3 paths."""
        for p in [2, 3, 5]:
            # Path 1: formula dim = 2p
            d1 = zhu_algebra_dimension(p)
            # Path 2: structure function
            data = zhu_algebra_structure(p)
            d2 = data['dim_zhu']
            # Path 3: decomposition ss + nilpotent
            d3 = data['semisimple_quotient_dim'] + data['nilpotent_radical_dim']
            self.assertEqual(d1, d2)
            self.assertEqual(d1, d3)


# =========================================================================
# 20. Landscape-level integration
# =========================================================================

class TestLandscapeIntegration(unittest.TestCase):
    """Integration with the broader modular Koszul landscape."""

    def test_c2_cofinite_not_rational(self):
        """W(p) is C_2-cofinite but NOT rational.

        This is the defining feature of logarithmic VOAs:
        they have finite-dimensional Zhu algebra (C_2-cofinite)
        but non-semisimple module category (not rational).
        """
        for p in range(2, 8):
            a = comprehensive_triplet_analysis(p)
            self.assertTrue(a.c2_cofinite)
            # Non-rationality is indicated by non-semisimple Zhu
            zhu = zhu_algebra_structure(p)
            self.assertFalse(zhu['is_semisimple'])

    def test_c2_cofinite_koszul_open(self):
        """W(p) is C_2-cofinite; Koszulness is OPEN.

        The grand_synthesis_engine claims Koszul and C_2 are orthogonal.
        W(p) is C_2-cofinite but Koszulness is OPEN, so this family
        does not yet provide a counterexample to orthogonality.
        """
        for p in range(2, 8):
            a = comprehensive_triplet_analysis(p)
            self.assertIsNone(a.koszul)  # OPEN
            self.assertTrue(a.c2_cofinite)

    def test_triplet_extends_landscape(self):
        """The triplet family extends the standard landscape.

        Standard landscape: rational VOAs (KM, Virasoro, minimal models,
        lattice VOAs, W-algebras).
        W(p): C_2-cofinite, non-rational, Koszulness OPEN.
        Resolving Koszulness would determine whether this is a NEW class.
        """
        for p in range(2, 6):
            a = comprehensive_triplet_analysis(p)
            self.assertIsNone(a.koszul)  # OPEN
            self.assertEqual(a.shadow_class, 'M')
            self.assertEqual(a.complementarity_sum, 13)
            # C_2-cofinite and non-rational
            self.assertTrue(a.c2_cofinite)

    def test_shadow_tower_prediction_summary(self):
        """Summary: what shadow tower sees beyond Zhu."""
        for p in [2, 3, 5]:
            data = shadow_tower_vs_zhu(p)
            # Shadow detects things Zhu cannot
            beyond = data['shadow_detects_additionally']
            self.assertTrue(beyond['non_semisimplicity'])
            self.assertTrue(beyond['logarithmic_mixing'])
            self.assertTrue(beyond['genus_2_anomaly'])
            self.assertTrue(beyond['full_derived_category'])


if __name__ == '__main__':
    unittest.main()
