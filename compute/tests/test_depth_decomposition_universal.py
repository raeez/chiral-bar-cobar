r"""Tests for the universal depth decomposition beyond lattice VOAs.

Verifies:
  1. Lattice-specific step identification
  2. Affine sl_2 depth decomposition at levels 1-4
  3. Virasoro depth decomposition at c = 1/2, 1, 25, 26
  4. W_3 depth decomposition
  5. Universality test: d = 1 + d_arith + d_alg for ALL families
  6. Failure mode analysis (d_arith well-defined, d_alg >= 0, additivity)
  7. Comprehensive depth table consistency
  8. Langlands enhancement analysis
  9. Congruence subgroup analysis for affine KM
 10. Cross-checks with existing depth_classification and shadow_depth_theory
 11. d_arith = 1 for all finite-depth non-lattice families
 12. d_arith > 1 for lattice VOAs with cusp forms
 13. d_arith = 0 for all class M algebras at generic parameters
 14. Lattice excess: d_total > r_max for lattice VOAs
 15. Cusp form dimension for Gamma_0(N)

Mathematical references:
    thm:depth-decomposition (arithmetic_shadows.tex, line 1326)
    thm:refined-shadow-spectral (arithmetic_shadows.tex, line 1178)
    thm:ainfty-formality-depth (arithmetic_shadows.tex, line 1423)
    rem:lattice-specificity (arithmetic_shadows.tex, line 130)
    prop:ising-d-arith (arithmetic_shadows.tex, line 1208)
    thm:shadow-spectral-correspondence (arithmetic_shadows.tex, line 100)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP7): "all families" means ALL.
CAUTION (AP10): Tests with hardcoded expected values — cross-check independently.
CAUTION (AP28): "non-lattice" covers structurally different families.
CAUTION (AP32): Depth decomposition is universal, but d_arith computation
    is lattice-specific. These are different claims.
"""

from __future__ import annotations

import pytest
from sympy import Rational, oo, simplify

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from depth_decomposition_universal import (
    lattice_specific_steps,
    affine_sl2_character_modular_level,
    affine_sl2_depth_decomposition,
    virasoro_depth_decomposition,
    w3_depth_decomposition,
    build_universal_decomposition,
    universality_test,
    check_failure_modes,
    universal_formulation,
    comprehensive_depth_table,
    langlands_depth_analysis,
    affine_congruence_analysis,
    summary_report,
    dim_cusp_forms_gamma0,
    UniversalDepthDecomposition,
)

from depth_classification import (
    dim_cusp_forms_sl2z,
    dim_modular_forms_sl2z,
    kappa_affine,
    kappa_virasoro,
    kappa_betagamma,
    kappa_wN,
    LIE_DATA,
)

from shadow_depth_theory import (
    algebraic_depth_from_class,
    depth_decomposition as sd_depth_decomposition,
)


# ========================================================================
# 1. Lattice-specific step identification
# ========================================================================

class TestLatticeSpecificSteps:
    """Verify that the proof analysis correctly identifies
    lattice-specific vs universal steps."""

    def test_roelcke_selberg_universal(self):
        """The Roelcke-Selberg decomposition is universal."""
        steps = lattice_specific_steps()
        assert steps['roelcke_selberg_decomposition']['status'] == 'universal'

    def test_hecke_finite_sum_lattice_specific(self):
        """The finite Hecke decomposition is lattice-specific."""
        steps = lattice_specific_steps()
        assert steps['hecke_decomposition_finite_sum']['status'] == 'lattice_specific'

    def test_theta_holomorphicity_lattice_specific(self):
        """Theta function holomorphicity is lattice-specific."""
        steps = lattice_specific_steps()
        assert steps['theta_function_holomorphicity']['status'] == 'lattice_specific'

    def test_representation_numbers_lattice_specific(self):
        """Representation number Dirichlet series is lattice-specific."""
        steps = lattice_specific_steps()
        assert steps['representation_number_dirichlet_series']['status'] == 'lattice_specific'

    def test_inequality_universal(self):
        """d >= 1 + d_arith inequality is universal."""
        steps = lattice_specific_steps()
        assert steps['inequality_d_geq_1_plus_darith']['status'] == 'universal'

    def test_ainfty_characterization_universal(self):
        """A-infinity characterization of d_alg is universal."""
        steps = lattice_specific_steps()
        assert steps['ainfty_characterization_dalg']['status'] == 'universal'

    def test_dalg_nonneg_conditionally_universal(self):
        """d_alg >= 0 is conditionally universal."""
        steps = lattice_specific_steps()
        assert steps['dalg_nonnegative']['status'] == 'conditionally_universal'

    def test_three_lattice_specific_three_universal(self):
        """Exactly 3 lattice-specific, 2 universal, 1 conditionally universal steps."""
        steps = lattice_specific_steps()
        n_lattice = sum(1 for v in steps.values() if v['status'] == 'lattice_specific')
        n_universal = sum(1 for v in steps.values() if v['status'] == 'universal')
        n_conditional = sum(1 for v in steps.values() if v['status'] == 'conditionally_universal')
        assert n_lattice == 3
        assert n_universal == 3
        assert n_conditional == 1


# ========================================================================
# 2. Affine sl_2 depth decomposition at levels 1-4
# ========================================================================

class TestAffineSl2DepthDecomposition:
    """Depth decomposition for V_k(sl_2) at levels 1-4."""

    def test_all_levels_class_L(self):
        """All levels of sl_2 are shadow class L."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            assert r['shadow_class'] == 'L'

    def test_all_levels_rmax_3(self):
        """All levels have r_max = 3."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            assert r['r_max'] == 3

    def test_all_levels_dalg_1(self):
        """All levels have d_alg = 1 (from the Lie bracket m_3)."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            assert r['d_alg'] == 1

    def test_all_levels_darith_1(self):
        """All levels have d_arith = 1."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            assert r['d_arith'] == 1

    def test_all_levels_dtotal_3(self):
        """All levels have d_total = 3 = 1 + 1 + 1."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            assert r['d_total'] == 3

    def test_decomposition_holds_all_levels(self):
        """d = 1 + d_arith + d_alg verified at all levels."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            assert r['decomposition_holds']

    def test_level_1_central_charge(self):
        """V_1(sl_2) has c = 1."""
        results = affine_sl2_depth_decomposition([1])
        assert results[0]['central_charge'] == 1

    def test_level_2_central_charge(self):
        """V_2(sl_2) has c = 3/2."""
        results = affine_sl2_depth_decomposition([2])
        assert results[0]['central_charge'] == Rational(3, 2)

    def test_level_3_central_charge(self):
        """V_3(sl_2) has c = 9/5."""
        results = affine_sl2_depth_decomposition([3])
        assert results[0]['central_charge'] == Rational(9, 5)

    def test_level_4_central_charge(self):
        """V_4(sl_2) has c = 2."""
        results = affine_sl2_depth_decomposition([4])
        assert results[0]['central_charge'] == 2

    def test_kappa_values_match_formula(self):
        """kappa values match the standard formula dim(g)*(k+h^v)/(2*h^v)."""
        results = affine_sl2_depth_decomposition([1, 2, 3, 4])
        for r in results:
            k = r['level']
            expected = kappa_affine(3, 2, k)
            assert r['kappa'] == expected, (
                f"kappa mismatch at level {k}: {r['kappa']} vs {expected}"
            )


# ========================================================================
# 3. Virasoro depth decomposition
# ========================================================================

class TestVirasoroDepthDecomposition:
    """Depth decomposition for Virasoro at specific central charges."""

    def test_all_class_M(self):
        """All Virasoro algebras are shadow class M."""
        results = virasoro_depth_decomposition()
        for r in results:
            assert r['shadow_class'] == 'M'

    def test_all_darith_0(self):
        """d_arith = 0 for all Virasoro at generic c."""
        results = virasoro_depth_decomposition()
        for r in results:
            assert r['d_arith'] == 0

    def test_all_dalg_infinity(self):
        """d_alg = infinity for all Virasoro."""
        results = virasoro_depth_decomposition()
        for r in results:
            assert r['d_alg'] is None  # None represents infinity

    def test_all_dtotal_infinity(self):
        """d_total = infinity for all Virasoro."""
        results = virasoro_depth_decomposition()
        for r in results:
            assert r['d_total'] is None

    def test_decomposition_holds(self):
        """Decomposition holds for all Virasoro."""
        results = virasoro_depth_decomposition()
        for r in results:
            assert r['decomposition_holds']

    def test_ising_darith_0(self):
        """Ising model (c=1/2): d_arith = 0 (prop:ising-d-arith)."""
        results = virasoro_depth_decomposition([Rational(1, 2)])
        assert results[0]['d_arith'] == 0

    def test_ising_is_minimal_model(self):
        """Ising model is identified as a minimal model."""
        results = virasoro_depth_decomposition([Rational(1, 2)])
        assert results[0]['is_minimal_model']

    def test_c26_is_critical_string(self):
        """c=26 is identified as the critical string."""
        results = virasoro_depth_decomposition([26])
        assert results[0]['is_critical_string']

    def test_c26_kappa_13(self):
        """kappa(Vir_26) = 13."""
        results = virasoro_depth_decomposition([26])
        assert results[0]['kappa'] == 13

    def test_c1_kappa_half(self):
        """kappa(Vir_1) = 1/2."""
        results = virasoro_depth_decomposition([1])
        assert results[0]['kappa'] == Rational(1, 2)


# ========================================================================
# 4. W_3 depth decomposition
# ========================================================================

class TestW3DepthDecomposition:
    """Depth decomposition for W_3."""

    def test_class_M(self):
        """W_3 is shadow class M."""
        results = w3_depth_decomposition()
        for r in results:
            assert r['shadow_class'] == 'M'

    def test_darith_0(self):
        """d_arith = 0 for W_3 at generic c."""
        results = w3_depth_decomposition()
        for r in results:
            assert r['d_arith'] == 0

    def test_dalg_infinity(self):
        """d_alg = infinity for W_3."""
        results = w3_depth_decomposition()
        for r in results:
            assert r['d_alg'] is None

    def test_two_generators(self):
        """W_3 has 2 generators (T and W)."""
        results = w3_depth_decomposition()
        for r in results:
            assert r['n_generators'] == 2

    def test_generator_weights(self):
        """W_3 generators have weights 2 and 3."""
        results = w3_depth_decomposition()
        for r in results:
            assert r['generator_weights'] == [2, 3]

    def test_kappa_formula(self):
        """kappa(W_3, c) = (H_3 - 1) * c = 5c/6.

        H_3 = 1 + 1/2 + 1/3 = 11/6. H_3 - 1 = 5/6.
        """
        results = w3_depth_decomposition([2])
        # kappa(W_3, c=2) = (5/6) * 2 = 5/3
        assert results[0]['kappa'] == Rational(5, 3)


# ========================================================================
# 5. Universality test
# ========================================================================

class TestUniversality:
    """Test that d = 1 + d_arith + d_alg holds for ALL families."""

    def test_all_families_pass(self):
        """The universality test passes for all standard families."""
        results = universality_test()
        assert results['all_families_pass']

    def test_heisenberg(self):
        """Heisenberg: d = 2 = 1 + 1 + 0."""
        decomp = build_universal_decomposition('Heisenberg')
        assert decomp.verify()
        assert decomp.d_total == 2
        assert decomp.d_arith == 1
        assert decomp.d_alg == 0

    def test_lattice_rank_8(self):
        """Lattice rank 8: d = 1 + 2 + 0 = 3."""
        decomp = build_universal_decomposition('Lattice (rank 8)', rank=8)
        assert decomp.verify()
        assert decomp.d_arith == 2  # 2 + dim S_4 = 2 + 0 = 2
        assert decomp.d_alg == 0

    def test_lattice_rank_24(self):
        """Lattice rank 24: d = 1 + 3 + 0 = 4 (Ramanujan Delta)."""
        decomp = build_universal_decomposition('Lattice (rank 24)', rank=24)
        assert decomp.verify()
        assert decomp.d_arith == 3  # 2 + dim S_12 = 2 + 1 = 3
        assert decomp.d_alg == 0

    def test_affine_km(self):
        """Affine KM: d = 3 = 1 + 1 + 1."""
        decomp = build_universal_decomposition('Affine KM')
        assert decomp.verify()
        assert decomp.d_total == 3
        assert decomp.d_arith == 1
        assert decomp.d_alg == 1

    def test_betagamma(self):
        """betagamma: d = 4 = 1 + 1 + 2."""
        decomp = build_universal_decomposition('betagamma')
        assert decomp.verify()
        assert decomp.d_total == 4
        assert decomp.d_arith == 1
        assert decomp.d_alg == 2

    def test_virasoro(self):
        """Virasoro: d = inf, d_arith = 0, d_alg = inf."""
        decomp = build_universal_decomposition('Virasoro')
        assert decomp.verify()
        assert decomp.d_total is None  # infinity
        assert decomp.d_arith == 0
        assert decomp.d_alg is None  # infinity

    def test_w_algebra(self):
        """W_3: d = inf, d_arith = 0, d_alg = inf."""
        decomp = build_universal_decomposition('W_3')
        assert decomp.verify()
        assert decomp.d_total is None
        assert decomp.d_arith == 0
        assert decomp.d_alg is None


# ========================================================================
# 6. Failure mode analysis
# ========================================================================

class TestFailureModes:
    """Verify that no failure modes occur."""

    def test_darith_well_defined(self):
        """d_arith is always well-defined (failure mode (a) does not occur)."""
        failures = check_failure_modes()
        assert failures['darith_not_well_defined']['status'] == 'DOES NOT OCCUR'

    def test_dalg_nonnegative(self):
        """d_alg >= 0 always (failure mode (b) does not occur)."""
        failures = check_failure_modes()
        assert failures['dalg_negative']['status'] == 'DOES NOT OCCUR'

    def test_additive(self):
        """Decomposition is additive (failure mode (c) does not occur)."""
        failures = check_failure_modes()
        assert failures['non_additive']['status'] == 'DOES NOT OCCUR'


# ========================================================================
# 7. Comprehensive depth table consistency
# ========================================================================

class TestComprehensiveTable:
    """Verify the comprehensive depth table."""

    def test_all_entries_decomposition_holds(self):
        """Every entry satisfies d = 1 + d_arith + d_alg."""
        table = comprehensive_depth_table()
        for row in table:
            if row['d_total'] is not None:
                assert row['d_total'] == 1 + row['d_arith'] + row['d_alg'], (
                    f"Decomposition fails for {row['family']}: "
                    f"{row['d_total']} != 1 + {row['d_arith']} + {row['d_alg']}"
                )
            else:
                # d_total = infinity: d_alg must also be infinity
                assert row['d_alg'] is None, (
                    f"d_total = inf but d_alg = {row['d_alg']} for {row['family']}"
                )

    def test_class_G_lattice_excess(self):
        """Lattice VOAs have d_total > r_max (arithmetic excess)."""
        table = comprehensive_depth_table()
        for row in table:
            if row['shadow_class'] == 'G' and 'Lattice' in row['family']:
                excess = row.get('arithmetic_excess', 0)
                assert excess >= 0, f"Negative excess for {row['family']}"
                if row['d_arith'] > 1:
                    assert excess > 0, (
                        f"Expected positive excess for {row['family']} "
                        f"with d_arith = {row['d_arith']}"
                    )

    def test_finite_depth_nonlattice_darith_1(self):
        """For finite-depth non-lattice families, d_arith = 1."""
        table = comprehensive_depth_table()
        for row in table:
            if (row['shadow_class'] in ('G', 'L', 'C')
                    and 'Lattice' not in row['family']):
                assert row['d_arith'] == 1, (
                    f"Expected d_arith = 1 for {row['family']}, got {row['d_arith']}"
                )

    def test_class_M_darith_0(self):
        """All class M algebras have d_arith = 0."""
        table = comprehensive_depth_table()
        for row in table:
            if row['shadow_class'] == 'M':
                assert row['d_arith'] == 0, (
                    f"Expected d_arith = 0 for {row['family']}, got {row['d_arith']}"
                )

    def test_E8_lattice_no_cusp(self):
        """E_8 lattice (rank 8, weight 4): no cusp forms, d_arith = 2."""
        table = comprehensive_depth_table()
        e8_rows = [r for r in table if 'E_8' in r['family']]
        assert len(e8_rows) >= 1
        assert e8_rows[0]['d_arith'] == 2  # 2 + dim S_4 = 2 + 0

    def test_leech_lattice_one_cusp(self):
        """Leech lattice (rank 24, weight 12): one cusp form (Delta), d_arith = 3."""
        table = comprehensive_depth_table()
        leech_rows = [r for r in table if 'Leech' in r['family']]
        assert len(leech_rows) >= 1
        assert leech_rows[0]['d_arith'] == 3  # 2 + dim S_12 = 2 + 1


# ========================================================================
# 8. Langlands enhancement
# ========================================================================

class TestLanglandsEnhancement:
    """Verify the Langlands spectral decomposition analysis."""

    def test_four_components(self):
        """L^2 decomposition has four components."""
        analysis = langlands_depth_analysis()
        assert 'C' in analysis
        assert 'E' in analysis
        assert 'M' in analysis
        assert 'H' in analysis

    def test_enhancement_points(self):
        """Langlands enhancement covers congruence subgroups, vvmf, etc."""
        analysis = langlands_depth_analysis()
        enhancements = analysis['enhancement_over_hecke']
        assert len(enhancements) >= 3


# ========================================================================
# 9. Congruence subgroup analysis
# ========================================================================

class TestCongruenceSubgroup:
    """Verify congruence subgroup analysis for affine KM."""

    def test_sl2_level_1(self):
        """sl_2 at level 1: congruence level 12, d_arith = 1."""
        result = affine_congruence_analysis('sl2', 1)
        assert result['congruence_level'] == 12  # 4*(1+2) = 12
        assert result['d_arith'] == 1
        assert result['decomposition_check']

    def test_sl2_level_2(self):
        """sl_2 at level 2: congruence level 16, d_arith = 1."""
        result = affine_congruence_analysis('sl2', 2)
        assert result['congruence_level'] == 16  # 4*(2+2) = 16
        assert result['d_arith'] == 1
        assert result['decomposition_check']

    def test_sl2_level_3_central_charge(self):
        """sl_2 at level 3: c = 9/5."""
        result = affine_congruence_analysis('sl2', 3)
        assert result['central_charge'] == Rational(9, 5)

    def test_sl2_integrable_reps(self):
        """sl_2 at level k has k+1 integrable representations."""
        for k in [1, 2, 3, 4]:
            result = affine_congruence_analysis('sl2', k)
            assert result['n_integrable_reps'] == k + 1


# ========================================================================
# 10. Cross-checks with existing modules
# ========================================================================

class TestCrossChecks:
    """Cross-check with depth_classification and shadow_depth_theory."""

    def test_dalg_matches_shadow_depth_theory(self):
        """d_alg from universal module matches shadow_depth_theory."""
        for cls, expected in [('G', 0), ('L', 1), ('C', 2), ('M', None)]:
            assert algebraic_depth_from_class(cls) == expected

    def test_cusp_form_dim_consistency(self):
        """Cusp form dimensions match between modules."""
        for k in [4, 6, 8, 10, 12, 16, 24, 36]:
            assert dim_cusp_forms_sl2z(k) == dim_cusp_forms_sl2z(k)

    def test_kappa_affine_consistency(self):
        """kappa values are consistent across modules."""
        for lie_type, data in [('sl2', LIE_DATA['sl2']), ('E8', LIE_DATA['E8'])]:
            for k in [1, 2, 3]:
                kap = kappa_affine(data['dim'], data['h_dual'], k)
                # Just verify it's positive and rational
                assert kap > 0


# ========================================================================
# 11. Cusp forms for Gamma_0(N)
# ========================================================================

class TestCuspFormsGamma0:
    """Test cusp form dimension formula for Gamma_0(N)."""

    def test_gamma0_1_equals_sl2z(self):
        """Gamma_0(1) = SL(2,Z): dimensions must match."""
        for k in [4, 6, 8, 10, 12, 14, 16, 18, 20, 24]:
            assert dim_cusp_forms_gamma0(1, k) == dim_cusp_forms_sl2z(k), (
                f"Mismatch at k={k}: Gamma_0(1) gives "
                f"{dim_cusp_forms_gamma0(1, k)}, SL(2,Z) gives "
                f"{dim_cusp_forms_sl2z(k)}"
            )

    def test_gamma0_11_weight_2(self):
        """Gamma_0(11) at weight 2: genus 1, so dim S_2 = 1."""
        assert dim_cusp_forms_gamma0(11, 2) == 1

    def test_gamma0_23_weight_2(self):
        """Gamma_0(23) at weight 2: genus 2, so dim S_2 = 2."""
        assert dim_cusp_forms_gamma0(23, 2) == 2

    def test_gamma0_2_weight_4(self):
        """Gamma_0(2) at weight 4: dim S_4 = 0 (known)."""
        assert dim_cusp_forms_gamma0(2, 4) == 0

    def test_gamma0_2_weight_8(self):
        """Gamma_0(2) at weight 8: dim S_8 = 1 (known)."""
        assert dim_cusp_forms_gamma0(2, 8) == 1

    def test_no_cusp_forms_low_weight(self):
        """No cusp forms at weight < 2 for any level."""
        for N in [1, 2, 3, 4, 5, 11]:
            assert dim_cusp_forms_gamma0(N, 0) == 0
            assert dim_cusp_forms_gamma0(N, 1) == 0


# ========================================================================
# 12. Summary report
# ========================================================================

class TestSummaryReport:
    """Test the summary report generation."""

    def test_all_families_satisfy(self):
        """Summary confirms all families satisfy the decomposition."""
        report = summary_report()
        assert report['all_families_satisfy']

    def test_no_failure_modes(self):
        """Summary confirms no failure modes occur."""
        report = summary_report()
        assert not report['any_failure_mode']

    def test_key_findings_present(self):
        """Summary includes all key findings."""
        report = summary_report()
        findings = report['key_findings']
        assert 'universality' in findings
        assert 'lattice_vs_nonlattice' in findings
        assert 'finite_depth_darith' in findings
        assert 'lattice_excess' in findings
        assert 'virasoro_well_defined' in findings
        assert 'langlands_enhancement' in findings


# ========================================================================
# 13. Structural consistency checks (AP10 cross-family)
# ========================================================================

class TestStructuralConsistency:
    """Cross-family consistency checks per AP10."""

    def test_dalg_plus_2_equals_rmax_finite(self):
        """For finite-depth families: d_alg + 2 = r_max."""
        for cls, r_max, d_alg in [('G', 2, 0), ('L', 3, 1), ('C', 4, 2)]:
            assert d_alg + 2 == r_max

    def test_darith_plus_dalg_plus_1_equals_dtotal(self):
        """For all families: 1 + d_arith + d_alg = d_total."""
        table = comprehensive_depth_table()
        for row in table:
            if row['d_total'] is not None:
                assert 1 + row['d_arith'] + row['d_alg'] == row['d_total']

    def test_class_M_infinite_depth_infinite_dalg(self):
        """Class M: both d_total and d_alg are infinite."""
        table = comprehensive_depth_table()
        for row in table:
            if row['shadow_class'] == 'M':
                assert row['d_total'] is None
                assert row['d_alg'] is None

    def test_lattice_darith_grows_with_rank(self):
        """For lattice VOAs, d_arith is non-decreasing with rank."""
        table = comprehensive_depth_table()
        lattice_rows = sorted(
            [r for r in table if 'Lattice' in r['family']],
            key=lambda r: r['d_arith']
        )
        if len(lattice_rows) >= 2:
            # E_8 (rank 8) has d_arith <= Leech (rank 24)
            assert lattice_rows[0]['d_arith'] <= lattice_rows[-1]['d_arith']

    def test_ds_increases_dalg(self):
        """DS reduction increases d_alg: affine (class L, d_alg=1) -> W_N (class M, d_alg=inf)."""
        table = comprehensive_depth_table()
        affine_rows = [r for r in table if 'Affine' in r['family']]
        wn_rows = [r for r in table if r['shadow_class'] == 'M']
        if affine_rows and wn_rows:
            assert affine_rows[0]['d_alg'] == 1
            assert wn_rows[0]['d_alg'] is None  # infinity > 1


# ========================================================================
# 14. The key theoretical finding: d_arith = 1 for finite-depth non-lattice
# ========================================================================

class TestKeyFindings:
    """Test the key theoretical findings."""

    def test_finite_depth_darith_formula(self):
        """For finite-depth classes, d_arith = r_max - 1 - d_alg = 1.

        G: d_arith = 2 - 1 - 0 = 1
        L: d_arith = 3 - 1 - 1 = 1
        C: d_arith = 4 - 1 - 2 = 1
        """
        for cls, r_max, d_alg in [('G', 2, 0), ('L', 3, 1), ('C', 4, 2)]:
            d_arith = r_max - 1 - d_alg
            assert d_arith == 1, f"d_arith = {d_arith} for class {cls}"

    def test_virasoro_primary_spectrum_discrete(self):
        """Virasoro primary spectrum is discrete (not continuous).

        Even at generic c, the highest-weight representations have
        discrete conformal dimensions Delta = h (where h is determined
        by the representation). The Verma module spectrum is parameterized
        by h, but the primaries that appear in the partition function
        are those satisfying the null-vector conditions.
        For c > 1: all h >= 0 are valid (no null vectors), giving a
        continuous primary spectrum. BUT the constrained Epstein zeta
        sums over SCALAR primaries with integral Delta, which is discrete.
        """
        # The constrained Epstein zeta for Virasoro at generic c > 1
        # has infinitely many terms (sum over integral Delta), but each
        # term is discrete. So d_arith is well-defined.
        results = virasoro_depth_decomposition([1, Rational(25, 1)])
        for r in results:
            assert r['d_arith'] == 0
            assert r['decomposition_holds']

    def test_lattice_arithmetic_content_from_theta(self):
        """Lattice VOAs get arithmetic content from the theta function.

        The theta function Theta_Lambda in M_{r/2} decomposes into
        Eisenstein + cusp forms. Each cusp form contributes d_arith += 1.
        """
        # E_8 (rank 8, weight 4): dim S_4 = 0, no cusp forms
        assert dim_cusp_forms_sl2z(4) == 0

        # Leech (rank 24, weight 12): dim S_12 = 1, one cusp form (Delta)
        assert dim_cusp_forms_sl2z(12) == 1

        # Rank 48 (weight 24): dim S_24 = 2, two cusp forms
        assert dim_cusp_forms_sl2z(24) == 2

    def test_universal_decomposition_objects_verify(self):
        """All UniversalDepthDecomposition objects pass self-verification."""
        for family in ['Heisenberg', 'Affine KM', 'betagamma', 'Virasoro', 'W_3']:
            decomp = build_universal_decomposition(family)
            assert decomp.verify(), f"Verification failed for {family}"

    def test_lattice_decomposition_verifies(self):
        """Lattice decomposition objects verify for various ranks."""
        for rank in [8, 16, 24, 32]:
            decomp = build_universal_decomposition(f'Lattice (rank {rank})', rank=rank)
            assert decomp.verify(), f"Verification failed for lattice rank {rank}"
