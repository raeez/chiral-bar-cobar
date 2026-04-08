r"""Tests for BV/BRST = bar at genus 1, CHAIN LEVEL, for class L.

THEOREM:
  The BV 1-loop effective action on E_tau x R equals the genus-1 bar complex
  as a CHAIN COMPLEX for class L (affine KM) algebras.

  The scalar-level match F_1^BV = kappa/24 is proved for all standard families.
  The chain-level identification is proved for classes G and L, and conditional
  for classes C and M.

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
  higher_genus_modular_koszul.tex (Theorem D)
  theorem_bv_brst_genus1_constraints_engine.py (scalar-level verification)
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_bv_genus1_chain_level_engine import (
    # Enums and data
    ChiralAlgebraData,
    ShadowClass,
    EpistemicStatus,
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
    sugawara_shift,
    chain_level_comparison,
    # Verification
    verify_jacobi_sl2,
    verify_jacobi_sl3,
    cross_family_chain_level_summary,
    kappa_three_paths,
)


# =====================================================================
# Section A: Algebra data integrity
# =====================================================================


class TestAlgebraData:
    """Verify algebra constructors produce correct data."""

    def test_heisenberg_kappa_is_level(self):
        """kappa(H_k) = k, NOT c/2 (AP48)."""
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

    def test_class_M_zero_modes_do_not_decouple(self):
        """For class M, zero modes do NOT decouple."""
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

    def test_virasoro_does_not_degenerate_E2(self):
        """Virasoro: SS does NOT degenerate at E_2."""
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

    def test_class_M_chain_level_conditional(self):
        """Class M: chain-level comparison is CONDITIONAL."""
        ss = spectral_sequence_analysis(virasoro(Fraction(26)))
        assert ss.chain_level_comparison == EpistemicStatus.CONDITIONAL


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

    def test_virasoro_conditional(self):
        """Virasoro: chain-level CONDITIONAL."""
        cl = chain_level_comparison(virasoro(Fraction(26)))
        assert cl.scalar_match is True
        assert cl.hodge_decouples is False
        assert cl.q_int_squared_zero is False
        assert cl.chain_level_status == EpistemicStatus.CONDITIONAL
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
        assert s['proved_count'] + s['conditional_count'] == s['total']

    def test_class_L_all_proved_in_summary(self):
        """All class L families are proved in the summary."""
        s = cross_family_chain_level_summary()
        assert s['class_L_all_proved'] is True

    def test_class_G_all_proved_in_summary(self):
        """All class G families are proved in the summary."""
        s = cross_family_chain_level_summary()
        assert s['class_G_all_proved'] is True

    def test_no_class_M_proved(self):
        """No class M families are proved at chain level."""
        s = cross_family_chain_level_summary()
        for f in s['families']:
            if f['class'] == 'M':
                assert f['chain_level'] == 'CONDITIONAL'


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
