r"""Tests for genus-1 BV/BRST-to-bar strict chain diagnostics.

THEOREM:
  The strict chain comparison at genus 1 identifies the BV differential
  on E_tau x R with the bar coalgebra B(A) for classes G and L.

  The scalar-level match F_1^BV = kappa/24 is proved for all standard families.
  It is not an all-genus BV/BRST=bar equivalence.  Class C is conditional on
  harmonic decoupling, and class M is obstructed at ordinary chain level.

MULTI-PATH VERIFICATION (CLAUDE.md mandate, 3+ paths per claim):
  Path 1: BV 1-loop determinant (Quillen anomaly + zeta regularization)
  Path 2: Spectral sequence E_2 degeneration (PBW + Jacobi)
  Path 3: Hodge decomposition on E_tau (zero-mode decoupling)
  Path 4: Sugawara shift verification
  Path 5: Cross-family consistency (additivity of kappa)
  Path 6: Quartic contact obstruction (class M vs class L)

TEST STRUCTURE:
  Section A: Algebra data integrity (kappa formulas, AP1/AP48 compliance)
  Section B: BV 1-loop determinant and scalar match
  Section C: Hodge decomposition on E_tau
  Section D: Q_int analysis (Jacobi decoupling)
  Section E: Spectral sequence degeneration
  Section F: Quartic contact obstruction
  Section G: Sugawara shift
  Section H: Chain-level comparison (the main theorem)
  Section I: Jacobi identity verification (algebraic)
  Section J: Cross-family summary
  Section K: Multi-path kappa verification

References:
  bv_brst.tex (conj:master-bv-brst, thm:bv-bar-geometric)
  higher_genus_modular_koszul.tex (Theorem D scalar obs_g = kappa lambda_g)
  theorem_bv_brst_genus1_constraints_engine.py (scalar-level verification)
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_bv_genus1_chain_level_engine import (
    # Enums and data
    ChiralAlgebraData,
    ShadowClass,
    EpistemicStatus,
    ComparisonAmbient,
    ChiralObject,
    ComparisonHypotheses,
    # Algebra constructors
    heisenberg,
    affine_sl2,
    affine_sl3,
    affine_slN,
    affine_so,
    affine_sp,
    virasoro,
    betagamma,
    # Core computations
    lambda_fp_exact,
    bv_one_loop,
    hodge_decomposition_torus,
    analyze_q_int,
    spectral_sequence_analysis,
    q_contact_virasoro,
    q_contact_class_L,
    virasoro_shadow_contact_witness,
    sugawara_shift,
    chain_level_comparison,
    validate_bv_bar_hypotheses,
    object_boundary_witness,
    # Verification
    verify_jacobi_sl2,
    verify_jacobi_sl3,
    cross_family_chain_level_summary,
    kappa_three_paths,
)


# =====================================================================
# Section 0: Scope and object-boundary guards
# =====================================================================


class TestScopeGuards:
    """Prevent scalar diagnostics from being read as broader equivalences."""

    def test_strict_chain_rejects_scalar_to_all_genus_promotion(self):
        """Strict chain comparison here is genus-1 only."""
        check = validate_bv_bar_hypotheses(
            ComparisonHypotheses(
                genus=2,
                ambient=ComparisonAmbient.STRICT_CHAIN,
            )
        )
        assert check.valid is False
        reason_text = ' '.join(check.failure_reasons)
        assert 'genus-1 only' in reason_text
        assert 'scalar kappa*lambda_g^FP' in reason_text

    def test_coderived_all_genus_requires_coacyclic_cone(self):
        """All-genus coderived BV/bar needs the coacyclic-cone surface."""
        missing = validate_bv_bar_hypotheses(
            ComparisonHypotheses(
                genus=2,
                ambient=ComparisonAmbient.CODERIVED,
                coacyclic_cone_localization=False,
            )
        )
        assert missing.valid is False
        assert any('coacyclic-cone' in r for r in missing.failure_reasons)

        supplied = validate_bv_bar_hypotheses(
            ComparisonHypotheses(
                genus=2,
                ambient=ComparisonAmbient.CODERIVED,
                coacyclic_cone_localization=True,
            )
        )
        assert supplied.valid is True
        assert 'coacyclic_cone_Verdier_localization' in supplied.required_witnesses

    def test_completed_chain_requires_mittag_leffler(self):
        """Completed chain comparison needs completion and ML witnesses."""
        missing = validate_bv_bar_hypotheses(
            ComparisonHypotheses(
                genus=2,
                ambient=ComparisonAmbient.WEIGHT_COMPLETED,
                weight_completed=True,
                mittag_leffler_witness=False,
            )
        )
        assert missing.valid is False
        assert any('Mittag-Leffler' in r for r in missing.failure_reasons)

        supplied = validate_bv_bar_hypotheses(
            ComparisonHypotheses(
                genus=2,
                ambient=ComparisonAmbient.WEIGHT_COMPLETED,
                weight_completed=True,
                mittag_leffler_witness=True,
            )
        )
        assert supplied.valid is True
        assert 'Mittag_Leffler_cohomology_tower' in supplied.required_witnesses

    def test_wrong_target_objects_rejected(self):
        """This engine compares with B(A), not A, A^i, A^!, or Z."""
        wrong_targets = [
            ChiralObject.ALGEBRA_A,
            ChiralObject.BAR_COHOMOLOGY_COALGEBRA,
            ChiralObject.KOSZUL_DUAL_ALGEBRA,
            ChiralObject.DERIVED_CENTER,
        ]
        for target in wrong_targets:
            check = validate_bv_bar_hypotheses(
                ComparisonHypotheses(target=target)
            )
            assert check.valid is False
            assert any('B(A)' in r for r in check.failure_reasons)

    def test_object_boundary_witness_distinguishes_five_objects(self):
        """A, B(A), A^i, A^!, and Z_ch^der(A) remain separate objects."""
        witness = object_boundary_witness()
        assert witness['B(A)']['is_compute_target'] is True
        assert witness['B(A)']['equals_bar_cohomology'] is False
        assert witness['B(A)']['equals_koszul_dual_algebra'] is False
        assert witness['B(A)']['equals_derived_center'] is False
        assert witness['A^!']['requires_finite_type_or_completed_koszul'] is True
        assert witness['A^!']['available_on_supplied_surface'] is False
        assert witness['Z_ch^der(A)']['equals_bar_coalgebra'] is False


# =====================================================================
# Section A: Algebra data integrity
# =====================================================================


class TestAlgebraData:
    """Verify algebra constructors produce correct data."""

    def test_heisenberg_kappa_is_level(self):
        """kappa(H_k) = k (AP48)."""
        for k in [1, 2, 5, 10]:
            alg = heisenberg(k)
            assert alg.kappa == Fraction(k)

    def test_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k in [1, 2, 4, 10]:
            alg = affine_sl2(k)
            assert alg.kappa == Fraction(3 * (k + 2), 4)

    def test_sl3_kappa(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        for k in [1, 3, 6]:
            alg = affine_sl3(k)
            assert alg.kappa == Fraction(8 * (k + 3), 6)
            assert alg.kappa == Fraction(4 * (k + 3), 3)

    def test_sl4_kappa(self):
        """kappa(sl_4, k) = 15(k+4)/8."""
        alg = affine_slN(4, 1)
        # dim(sl_4) = 15, h^v = 4
        assert alg.kappa == Fraction(15 * 5, 8)
        assert alg.kappa == Fraction(75, 8)

    def test_so5_kappa(self):
        """kappa(so_5, k) = 10(k+3)/6 = 5(k+3)/3."""
        alg = affine_so(5, 1)
        # dim(so_5) = 10, h^v = 3
        assert alg.kappa == Fraction(10 * 4, 6)
        assert alg.kappa == Fraction(20, 3)

    def test_sp4_kappa(self):
        """kappa(sp_4, k) = 10(k+3)/6 = 5(k+3)/3."""
        alg = affine_sp(2, 1)
        # dim(sp_4) = 2*5 = 10, h^v = 3
        assert alg.kappa == Fraction(10 * 4, 6)
        assert alg.kappa == Fraction(20, 3)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [1, 2, 13, 26]:
            alg = virasoro(Fraction(c))
            assert alg.kappa == Fraction(c, 2)

    def test_shadow_classes(self):
        """Each family has the correct shadow class."""
        assert heisenberg(1).shadow_class == ShadowClass.G
        assert affine_sl2(1).shadow_class == ShadowClass.L
        assert affine_sl3(1).shadow_class == ShadowClass.L
        assert virasoro(Fraction(26)).shadow_class == ShadowClass.M
        assert betagamma().shadow_class == ShadowClass.C

    def test_max_ope_pole_order(self):
        """OPE pole orders: 2 for KM, 4 for Virasoro, 1 for beta-gamma."""
        assert heisenberg(1).max_ope_pole_order == 2
        assert affine_sl2(1).max_ope_pole_order == 2
        assert virasoro(Fraction(1)).max_ope_pole_order == 4
        assert betagamma().max_ope_pole_order == 1

    def test_class_L_has_cubic_only(self):
        """Class L algebras have only cubic BV vertices."""
        for alg in [affine_sl2(1), affine_sl3(1), affine_slN(4, 2)]:
            assert alg.has_cubic_only is True

    def test_class_M_not_cubic_only(self):
        """Class M algebras have quartic and higher vertices."""
        assert virasoro(Fraction(1)).has_cubic_only is False

    def test_betagamma_not_cubic_only_for_bv_surface(self):
        """Simple OPE pole order does not remove the class-C BV contact term."""
        alg = betagamma()
        assert alg.max_ope_pole_order == 1
        assert alg.has_cubic_only is False


# =====================================================================
# Section B: BV 1-loop determinant and scalar match
# =====================================================================


class TestBVOneLoop:
    """BV 1-loop determinant on E_tau x R."""

    def test_heisenberg_scalar_match(self):
        """Heisenberg: F_1^BV = k/24 = kappa/24."""
        for k in [1, 3, 5]:
            bv = bv_one_loop(heisenberg(k))
            assert bv.F1_bv == Fraction(k, 24)
            assert bv.scalar_match is True

    def test_sl2_scalar_match(self):
        """sl_2 at k=1: F_1 = 9/96 = 3/32."""
        bv = bv_one_loop(affine_sl2(1))
        assert bv.F1_bv == Fraction(9, 4) * Fraction(1, 24)
        assert bv.F1_bv == Fraction(3, 32)
        assert bv.scalar_match is True

    def test_virasoro_scalar_match(self):
        """Virasoro at c=26: F_1 = 13/24."""
        bv = bv_one_loop(virasoro(Fraction(26)))
        assert bv.F1_bv == Fraction(13, 24)
        assert bv.scalar_match is True

    def test_alpha_equals_kappa(self):
        """The BV exponent alpha equals kappa for all families."""
        families = [heisenberg(1), affine_sl2(2), virasoro(Fraction(12))]
        for alg in families:
            bv = bv_one_loop(alg)
            assert bv.alpha_bv == alg.kappa

    def test_universal_scalar_match(self):
        """F_1^BV = F_1^bar for all standard families."""
        families = [
            heisenberg(1), heisenberg(5),
            affine_sl2(1), affine_sl3(1),
            virasoro(Fraction(1)), virasoro(Fraction(26)),
            betagamma(),
        ]
        for alg in families:
            bv = bv_one_loop(alg)
            assert bv.scalar_match is True, f"Scalar mismatch for {alg.name}"


# =====================================================================
# Section C: Hodge decomposition on E_tau
# =====================================================================


class TestHodgeDecomposition:
    """Hodge decomposition of fields on E_tau."""

    def test_heisenberg_harmonic_dim(self):
        """Heisenberg: 1 generator, harmonic dim = 2."""
        h = hodge_decomposition_torus(heisenberg(1))
        assert h.dim_H0 == 1
        assert h.dim_H1 == 1
        assert h.dim_harmonic == 2

    def test_sl2_harmonic_dim(self):
        """sl_2: 3 generators, harmonic dim = 6."""
        h = hodge_decomposition_torus(affine_sl2(1))
        assert h.dim_H0 == 3
        assert h.dim_H1 == 3
        assert h.dim_harmonic == 6

    def test_sl3_harmonic_dim(self):
        """sl_3: 8 generators, harmonic dim = 16."""
        h = hodge_decomposition_torus(affine_sl3(1))
        assert h.dim_H0 == 8
        assert h.dim_H1 == 8
        assert h.dim_harmonic == 16

    def test_class_L_zero_modes_decouple(self):
        """For class L, zero modes decouple from Q_int."""
        for alg in [affine_sl2(1), affine_sl3(1), affine_slN(4, 1)]:
            h = hodge_decomposition_torus(alg)
            assert h.zero_mode_decouples is True

    def test_class_G_zero_modes_decouple(self):
        """For class G (free), zero modes trivially decouple."""
        h = hodge_decomposition_torus(heisenberg(1))
        assert h.zero_mode_decouples is True

    def test_class_M_zero_modes_remain_coupled(self):
        """For class M, zero modes remain coupled."""
        h = hodge_decomposition_torus(virasoro(Fraction(26)))
        assert h.zero_mode_decouples is False


# =====================================================================
# Section D: Q_int analysis
# =====================================================================


class TestQIntAnalysis:
    """Analysis of the BV interaction operator Q_int."""

    def test_heisenberg_no_interaction(self):
        """Heisenberg: Q_int = 0, no vertices."""
        q = analyze_q_int(heisenberg(1))
        assert q.has_cubic_vertex is False
        assert q.has_quartic_vertex is False
        assert q.q_int_squared_zero is True
        assert q.chain_level_proved is True

    def test_sl2_cubic_only(self):
        """sl_2: cubic vertex only, Q_int^2 = 0 by Jacobi."""
        q = analyze_q_int(affine_sl2(1))
        assert q.has_cubic_vertex is True
        assert q.has_quartic_vertex is False
        assert q.jacobi_holds is True
        assert q.q_int_squared_zero is True
        assert q.chain_level_proved is True

    def test_sl3_cubic_only(self):
        """sl_3: cubic vertex only, Q_int^2 = 0 by Jacobi."""
        q = analyze_q_int(affine_sl3(1))
        assert q.has_cubic_vertex is True
        assert q.has_quartic_vertex is False
        assert q.jacobi_holds is True
        assert q.q_int_squared_zero is True
        assert q.chain_level_proved is True

    def test_virasoro_quartic_obstruction(self):
        """Virasoro: quartic vertex, Q_int^2 != 0."""
        q = analyze_q_int(virasoro(Fraction(26)))
        assert q.has_cubic_vertex is True
        assert q.has_quartic_vertex is True
        assert q.jacobi_holds is False
        assert q.q_int_squared_zero is False
        assert q.chain_level_proved is False
        assert q.obstruction is not None

    def test_betagamma_quartic_present(self):
        """Beta-gamma: quartic vertex present (though Q^contact = 0)."""
        q = analyze_q_int(betagamma())
        assert q.has_quartic_vertex is True
        assert q.chain_level_proved is False

    def test_class_L_all_proved(self):
        """ALL class L algebras have chain-level BV = bar proved."""
        for alg in [affine_sl2(1), affine_sl3(1), affine_slN(4, 2),
                     affine_so(5, 1), affine_sp(2, 1)]:
            q = analyze_q_int(alg)
            assert q.chain_level_proved is True, f"Failed for {alg.name}"


# =====================================================================
# Section E: Spectral sequence degeneration
# =====================================================================


class TestSpectralSequence:
    """Spectral sequence for the BV-to-bar comparison."""

    def test_heisenberg_degenerates_E1(self):
        """Heisenberg: SS degenerates at E_1 (no interaction)."""
        ss = spectral_sequence_analysis(heisenberg(1))
        assert ss.degeneration_page == 1
        assert ss.e2_equals_einfty is True

    def test_class_L_degenerates_E2(self):
        """Class L: SS degenerates at E_2 (Jacobi)."""
        ss = spectral_sequence_analysis(affine_sl2(1))
        assert ss.degeneration_page == 2
        assert ss.d1_squared_zero is True
        assert ss.e2_equals_einfty is True

    def test_virasoro_has_obstruction_beyond_E2(self):
        """Virasoro has a spectral-sequence obstruction beyond E_2."""
        ss = spectral_sequence_analysis(virasoro(Fraction(26)))
        assert ss.d1_squared_zero is False
        assert ss.e2_equals_einfty is False
        assert ss.degeneration_page > 2

    def test_euler_char_always_at_E1(self):
        """The Euler characteristic is determined at E_1 for ALL families."""
        families = [heisenberg(1), affine_sl2(1), virasoro(Fraction(1)),
                     betagamma()]
        for alg in families:
            ss = spectral_sequence_analysis(alg)
            assert ss.euler_char_determined_at == 1

    def test_class_L_chain_level_proved(self):
        """Class L: chain-level comparison is PROVED."""
        for alg in [affine_sl2(1), affine_sl3(1)]:
            ss = spectral_sequence_analysis(alg)
            assert ss.chain_level_comparison == EpistemicStatus.PROVED

    def test_class_M_chain_level_obstructed(self):
        """Class M: ordinary chain-level comparison is OBSTRUCTED."""
        ss = spectral_sequence_analysis(virasoro(Fraction(26)))
        assert ss.chain_level_comparison == EpistemicStatus.OBSTRUCTED


# =====================================================================
# Section F: Quartic contact obstruction
# =====================================================================


class TestQuarticContact:
    """Quartic contact invariant as chain-level obstruction."""

    def test_class_L_contact_zero(self):
        """Class L: Q^contact = 0 identically."""
        assert q_contact_class_L() == Fraction(0)

    def test_virasoro_contact_c26(self):
        """Virasoro at c=26: Q^contact = 10/(26*152) = 5/1976."""
        q = q_contact_virasoro(Fraction(26))
        assert q == Fraction(10, 26 * 152)
        assert q == Fraction(5, 1976)

    def test_virasoro_contact_c13(self):
        """Virasoro at c=13: Q^contact = 10/(13*87) = 10/1131."""
        q = q_contact_virasoro(Fraction(13))
        assert q == Fraction(10, 13 * 87)
        assert q == Fraction(10, 1131)

    def test_virasoro_contact_c1(self):
        """Virasoro at c=1: Q^contact = 10/(1*27) = 10/27."""
        q = q_contact_virasoro(Fraction(1))
        assert q == Fraction(10, 27)

    def test_virasoro_contact_positive(self):
        """Q^contact > 0 for all c > 0 (the obstruction never vanishes)."""
        for c in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(26)]:
            assert q_contact_virasoro(c) > 0

    def test_virasoro_contact_singular_surface_rejected(self):
        """The contact invariant is defined only when c(5c+22) != 0."""
        for c in [Fraction(0), Fraction(-22, 5)]:
            with pytest.raises(ValueError):
                q_contact_virasoro(c)

    def test_virasoro_contact_witness_distinguishes_S4_from_delta(self):
        """S4 is 10/[c(5c+22)], while Delta is 8*kappa*S4."""
        witness = virasoro_shadow_contact_witness(Fraction(26))
        assert witness['S4'] == Fraction(5, 1976)
        assert witness['S4'] == q_contact_virasoro(Fraction(26))
        assert witness['Delta'] == Fraction(40, 152)
        assert witness['Delta'] == Fraction(5, 19)
        assert witness['S4'] != witness['Delta']
        assert witness['S5'] == Fraction(-48, 26 * 26 * 152)


# =====================================================================
# Section G: Sugawara shift
# =====================================================================


class TestSugawaraShift:
    """Sugawara shift from raw determinant to kappa."""

    def test_sl2_sugawara(self):
        """sl_2 at k=1: raw = 3, shifted = 9/4."""
        s = sugawara_shift(dim_g=3, k=1, hv=2)
        assert s['raw_alpha'] == Fraction(3)
        assert s['kappa'] == Fraction(9, 4)
        assert s['shift_factor'] == Fraction(3, 4)

    def test_sl3_sugawara(self):
        """sl_3 at k=1: raw = 8, shifted = 4*4/3 = 16/3."""
        s = sugawara_shift(dim_g=8, k=1, hv=3)
        assert s['raw_alpha'] == Fraction(8)
        assert s['kappa'] == Fraction(16, 3)
        assert s['shift_factor'] == Fraction(4, 6)

    def test_sugawara_c_formula(self):
        """Sugawara central charge c = dim(g)*k/(k+h^v)."""
        s = sugawara_shift(dim_g=3, k=1, hv=2)
        assert s['c_sugawara'] == Fraction(1)  # c(sl_2, k=1) = 3*1/3 = 1

    def test_sugawara_F1_shift(self):
        """F_1 shifts from raw*lambda_1^FP to kappa*lambda_1^FP."""
        s = sugawara_shift(dim_g=3, k=1, hv=2)
        assert s['F1_raw'] == Fraction(3, 24) == Fraction(1, 8)
        assert s['F1_correct'] == Fraction(9, 4) * Fraction(1, 24)
        assert s['F1_correct'] == Fraction(3, 32)
        # The shift changes F_1 from 1/8 to 3/32
        assert s['F1_raw'] != s['F1_correct']


# =====================================================================
# Section H: Chain-level comparison (the main theorem)
# =====================================================================


class TestChainLevelComparison:
    """The main theorem: BV = bar at genus 1, chain level."""

    def test_heisenberg_proved(self):
        """Heisenberg: chain-level PROVED (no interaction)."""
        cl = chain_level_comparison(heisenberg(1))
        assert cl.scalar_match is True
        assert cl.hodge_decouples is True
        assert cl.q_int_squared_zero is True
        assert cl.chain_level_status == EpistemicStatus.PROVED
        assert cl.obstruction is None

    def test_sl2_proved(self):
        """sl_2: chain-level PROVED (Jacobi decoupling)."""
        cl = chain_level_comparison(affine_sl2(1))
        assert cl.scalar_match is True
        assert cl.hodge_decouples is True
        assert cl.q_int_squared_zero is True
        assert cl.ss_degenerates_at == 2
        assert cl.chain_level_status == EpistemicStatus.PROVED
        assert cl.obstruction is None

    def test_sl3_proved(self):
        """sl_3: chain-level PROVED."""
        cl = chain_level_comparison(affine_sl3(1))
        assert cl.chain_level_status == EpistemicStatus.PROVED

    def test_virasoro_obstructed(self):
        """Virasoro: ordinary chain-level OBSTRUCTED."""
        cl = chain_level_comparison(virasoro(Fraction(26)))
        assert cl.scalar_match is True
        assert cl.hodge_decouples is False
        assert cl.q_int_squared_zero is False
        assert cl.chain_level_status == EpistemicStatus.OBSTRUCTED
        assert cl.obstruction is not None

    def test_betagamma_conditional(self):
        """Beta-gamma: chain-level CONDITIONAL."""
        cl = chain_level_comparison(betagamma())
        assert cl.scalar_match is True
        assert cl.chain_level_status == EpistemicStatus.CONDITIONAL

    def test_all_class_L_proved(self):
        """ALL class L algebras: chain-level PROVED."""
        for alg in [affine_sl2(k) for k in [1, 2, 4]] + \
                   [affine_sl3(k) for k in [1, 3]] + \
                   [affine_slN(4, 1), affine_so(5, 1), affine_sp(2, 1)]:
            cl = chain_level_comparison(alg)
            assert cl.chain_level_status == EpistemicStatus.PROVED, \
                f"Chain level should be PROVED for {alg.name}"

    def test_F1_values_consistent(self):
        """F_1^BV = F_1^bar for all families."""
        families = [heisenberg(3), affine_sl2(2), virasoro(Fraction(10))]
        for alg in families:
            cl = chain_level_comparison(alg)
            assert cl.F1_bv == cl.F1_bar


# =====================================================================
# Section I: Jacobi identity verification (algebraic)
# =====================================================================


class TestJacobiIdentity:
    """Verify the Jacobi identity for standard Lie algebras."""

    def test_sl2_jacobi(self):
        """sl_2: all 81 quadruples satisfy Jacobi."""
        result = verify_jacobi_sl2()
        assert result['jacobi_holds'] is True
        assert result['violations'] == 0
        assert result['total_checks'] == 81  # 3^4

    def test_sl3_jacobi(self):
        """sl_3: Jacobi holds (from matrix commutator)."""
        result = verify_jacobi_sl3()
        assert result['jacobi_holds'] is True
        assert result['dim'] == 8
        assert result['max_jacobi_violation'] < 1e-10


# =====================================================================
# Section J: Cross-family summary
# =====================================================================


class TestCrossFamilySummary:
    """Cross-family verification of chain-level status."""

    def test_summary_structure(self):
        """Summary returns well-formed data."""
        s = cross_family_chain_level_summary()
        assert s['total'] == 9
        counted = s['proved_count'] + s['conditional_count'] + s['obstructed_count']
        assert counted == s['total']

    def test_class_L_all_proved_in_summary(self):
        """All class L families are proved in the summary."""
        s = cross_family_chain_level_summary()
        assert s['class_L_all_proved'] is True

    def test_class_G_all_proved_in_summary(self):
        """All class G families are proved in the summary."""
        s = cross_family_chain_level_summary()
        assert s['class_G_all_proved'] is True

    def test_class_M_obstructed(self):
        """Class M families are obstructed at ordinary chain level."""
        s = cross_family_chain_level_summary()
        for f in s['families']:
            if f['class'] == 'M':
                assert f['chain_level'] == 'OBSTRUCTED'


# =====================================================================
# Section K: Multi-path kappa verification
# =====================================================================


class TestKappaMultiPath:
    """Verify kappa by 3 independent paths."""

    def test_heisenberg_three_paths(self):
        """Heisenberg: kappa = k by all three paths."""
        result = kappa_three_paths(heisenberg(5))
        assert result['all_agree'] is True
        assert result['kappa_defining'] == Fraction(5)

    def test_sl2_three_paths(self):
        """sl_2: kappa = 3(k+2)/4 by all three paths."""
        result = kappa_three_paths(affine_sl2(1))
        assert result['all_agree'] is True
        assert result['kappa_defining'] == Fraction(9, 4)

    def test_virasoro_three_paths(self):
        """Virasoro: kappa = c/2 by all three paths."""
        result = kappa_three_paths(virasoro(Fraction(26)))
        assert result['all_agree'] is True
        assert result['kappa_defining'] == Fraction(13)

    def test_so5_three_paths(self):
        """so_5 at k=1: kappa by all three paths."""
        result = kappa_three_paths(affine_so(5, 1))
        assert result['all_agree'] is True

    def test_sp4_three_paths(self):
        """sp_4 at k=1: kappa by all three paths."""
        result = kappa_three_paths(affine_sp(2, 1))
        assert result['all_agree'] is True

    def test_lambda_fp_consistency(self):
        """lambda_1^FP = 1/24 is consistent across all kappa paths."""
        assert lambda_fp_exact(1) == Fraction(1, 24)
        assert lambda_fp_exact(2) == Fraction(7, 5760)
