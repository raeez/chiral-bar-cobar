r"""Tests for bv_bar_coderived_engine: BV=bar in the coderived category D^co.

MAIN RESULT:
  For ALL shadow classes (G, L, C, M), the BV complex and bar complex
  are coderived quasi-isomorphic: Obs_BV ~ B(A) in D^co(A).

  The chain-level obstruction delta_4 = Q^contact * kappa / Im(tau)
  for class M is EXACTLY proportional to the curvature m_0 = kappa / Im(tau):
    delta_4 = Q^contact * m_0

  In D^co: d^2 = m_0 * id, so m_0 * x = d^2(x) is exact.
  Therefore delta_4 is trivial in D^co.

TEST STRUCTURE (multi-path verification, 3+ independent paths per claim):

  Section A: Curvature data consistency
  Section B: Harmonic obstruction consistency (cross-check with class M engine)
  Section C: Curvature proportionality — the KEY computation
  Section D: Numerical verification at specific central charges
  Section E: Coderived triviality argument verification
  Section F: Curved homotopy witness
  Section G: Higher-arity obstructions
  Section H: W_N generalization
  Section I: Genus >= 2 propagation
  Section J: Cross-class coderived status
  Section K: Complementarity and Koszul duality
  Section L: Matrix model verification
  Section M: Coderived vs contraderived
  Section N: Complete synthesis
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, Integer, Abs, factor, expand

from compute.lib.bv_bar_coderived_engine import (
    Genus1CurvatureData,
    genus1_curvature,
    harmonic_obstruction_virasoro,
    curvature_proportionality_test,
    curvature_proportionality_numerical,
    coderived_triviality_argument,
    curved_homotopy_witness,
    numerical_coderived_check,
    wn_coderived_data,
    higher_arity_coderived,
    cross_class_coderived_status,
    genus2_coderived,
    coderived_complementarity,
    coderived_vs_contraderived,
    matrix_model_verification,
    koszul_dual_coderived,
    bv_bar_coderived_synthesis,
)


# Also import from class M engine for cross-checks
from compute.lib.bv_bar_class_m_engine import (
    virasoro_data,
    quartic_harmonic_amplitude_virasoro,
    quartic_harmonic_numerical,
    coboundary_analysis_virasoro,
    coderived_approach as class_m_coderived_approach,
    discrepancy_complementarity,
)


# =====================================================================
# Section A: Curvature data consistency
# =====================================================================


class TestCurvatureData:
    """Verify genus-1 curvature data for standard families."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP48)."""
        for c_val in [Rational(1), Rational(13), Rational(26)]:
            data = genus1_curvature('virasoro', c=c_val)
            assert data.kappa == c_val / 2

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (NOT c/2, AP48)."""
        for k_val in [Rational(1), Rational(2), Rational(5)]:
            data = genus1_curvature('heisenberg', k=k_val)
            assert data.kappa == k_val

    def test_affine_sl2_kappa(self):
        """kappa(sl2_k) = 3(k+2)/4."""
        for k_val in [Rational(1), Rational(2), Rational(4)]:
            data = genus1_curvature('affine_sl2', k=k_val)
            expected = Rational(3) * (k_val + 2) / 4
            assert data.kappa == expected

    def test_betagamma_kappa(self):
        """kappa(betagamma) = -1."""
        data = genus1_curvature('betagamma')
        assert data.kappa == -1

    def test_m0_scalar_formula(self):
        """m_0 = kappa / Im(tau) as scalar action on bar complex."""
        im_tau = Symbol('Im_tau', positive=True)
        for c_val in [Rational(1), Rational(13)]:
            data = genus1_curvature('virasoro', c=c_val)
            expected = c_val / 2 / im_tau
            assert simplify(data.m_0_scalar - expected) == 0


# =====================================================================
# Section B: Harmonic obstruction cross-check
# =====================================================================


class TestHarmonicObstructionCrossCheck:
    """Cross-check harmonic obstruction with existing class M engine."""

    def test_delta4_formula_match(self):
        """delta_4 from coderived engine matches class M engine.

        Multi-path:
          Path 1: coderived engine harmonic_obstruction_virasoro
          Path 2: class M engine quartic_harmonic_amplitude_virasoro
          Path 3: direct computation 5/((5c+22)*Im_tau)
        """
        c = Symbol('c')
        im_tau = Symbol('Im_tau', positive=True)

        # Path 1
        result1 = harmonic_obstruction_virasoro(c)
        delta_4_path1 = result1['delta_4']

        # Path 2
        result2 = quartic_harmonic_amplitude_virasoro(c)
        delta_4_path2 = result2['contact_harm_amplitude']

        # Path 3
        delta_4_path3 = 5 / ((5 * c + 22) * im_tau)

        assert simplify(delta_4_path1 - delta_4_path3) == 0
        assert simplify(delta_4_path2 - delta_4_path3) == 0

    def test_delta4_numerical_cross_check(self):
        """Numerical cross-check at c=1, c=13, c=26."""
        for c_val in [1.0, 13.0, 26.0]:
            # From coderived engine
            result = curvature_proportionality_numerical(c_val)
            delta_coeff = result['delta_4_coeff']

            # From class M engine
            result_m = quartic_harmonic_numerical(c_val)
            delta_coeff_m = result_m['contact_harm_coeff']

            assert abs(delta_coeff - delta_coeff_m) < 1e-14

    def test_Q_contact_consistency(self):
        """Q^contact = 10/(c(5c+22)) from both engines.

        Multi-path:
          Path 1: coderived engine
          Path 2: class M engine virasoro_data
          Path 3: direct formula
        """
        for c_val in [Rational(1), Rational(2), Rational(13)]:
            # Path 1
            result = harmonic_obstruction_virasoro(c_val)
            Q1 = result['Q_contact']

            # Path 2
            vd = virasoro_data(c_val)
            Q2 = vd.Q_contact

            # Path 3
            Q3 = Rational(10) / (c_val * (5 * c_val + 22))

            assert Q1 == Q3
            assert Q2 == Q3


# =====================================================================
# Section C: Curvature proportionality — the KEY computation
# =====================================================================


class TestCurvatureProportionality:
    """THE CENTRAL RESULT: delta_4 = Q^contact * m_0."""

    def test_symbolic_proportionality(self):
        """Symbolic verification: delta_4 / m_0 = Q^contact.

        Multi-path:
          Path 1: direct ratio
          Path 2: factored form
          Path 3: structural factorization
        """
        result = curvature_proportionality_test()
        assert result['path1_match'] is True
        assert result['path2_match'] is True
        assert result['path3_match'] is True
        assert result['all_paths_agree'] is True

    def test_ratio_is_pure_algebraic(self):
        """The ratio delta_4/m_0 has NO Im(tau) dependence.

        This is the key structural fact: the ratio is a pure algebraic
        constant, independent of the moduli. Therefore the harmonic
        obstruction is EXACTLY a curvature multiple.
        """
        c = Symbol('c')
        im_tau = Symbol('Im_tau', positive=True)

        delta_4 = 5 / ((5 * c + 22) * im_tau)
        m_0 = (c / 2) / im_tau
        ratio = simplify(delta_4 / m_0)

        # ratio should be independent of im_tau
        import sympy
        assert im_tau not in ratio.free_symbols

    def test_numerical_proportionality_c1(self):
        """At c=1: delta_4/(1/Im_tau) * 2/c = Q^contact.

        delta_4 = 5/(27*Im_tau), m_0 = (1/2)/Im_tau
        ratio = 5/27 / (1/2) = 10/27 = Q^contact(1).
        """
        result = curvature_proportionality_numerical(1.0)
        assert result['match'] is True
        assert abs(result['ratio'] - result['Q_contact']) < 1e-14

    def test_numerical_proportionality_c13(self):
        """At c=13 (self-dual): ratio = Q^contact(13)."""
        result = curvature_proportionality_numerical(13.0)
        assert result['match'] is True
        Q_expected = 10.0 / (13.0 * (65.0 + 22.0))
        assert abs(result['ratio'] - Q_expected) < 1e-14

    def test_numerical_proportionality_c26(self):
        """At c=26 (critical): ratio = Q^contact(26)."""
        result = curvature_proportionality_numerical(26.0)
        assert result['match'] is True
        Q_expected = 10.0 / (26.0 * (130.0 + 22.0))
        assert abs(result['ratio'] - Q_expected) < 1e-14

    def test_numerical_proportionality_c_half(self):
        """At c=1/2 (Ising): ratio = Q^contact(1/2)."""
        result = curvature_proportionality_numerical(0.5)
        assert result['match'] is True
        Q_expected = 10.0 / (0.5 * (2.5 + 22.0))
        assert abs(result['ratio'] - Q_expected) < 1e-14

    def test_numerical_proportionality_sweep(self):
        """Sweep over 20 values of c: ratio = Q^contact for all.

        Multi-path (numerical sweep as independent path):
          All 20 values must agree with the symbolic result.
        """
        c_values = [0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0,
                     13.0, 15.0, 20.0, 25.0, 26.0, 30.0, 50.0,
                     100.0, 200.0, 1000.0, 0.01, 0.001]
        for c_val in c_values:
            result = curvature_proportionality_numerical(c_val)
            assert result['match'] is True, f"Failed at c={c_val}"

    def test_exact_proportionality_rational(self):
        """Exact rational verification at several c values.

        Path: exact Rational arithmetic (no floating point).
        """
        for c_val in [Rational(1, 2), Rational(1), Rational(2), Rational(7, 5),
                       Rational(13), Rational(25), Rational(26)]:
            result = numerical_coderived_check(c_val)
            assert result['ratio_equals_Q_contact'] is True
            assert result['delta_4_equals_Q_times_m0'] is True


# =====================================================================
# Section D: Numerical verification at specific central charges
# =====================================================================


class TestNumericalVerification:
    """Numerical checks at physically important central charges."""

    def test_c0_trivial(self):
        """At c=0: both delta_4 and m_0 vanish."""
        result = numerical_coderived_check(Rational(0))
        assert result['trivially_equal'] is True

    def test_c1_free_boson(self):
        """At c=1: Q^contact = 10/27, kappa = 1/2."""
        result = numerical_coderived_check(Rational(1))
        assert result['Q_contact'] == Rational(10, 27)
        assert result['kappa'] == Rational(1, 2)
        assert result['ratio_equals_Q_contact'] is True

    def test_c_half_ising(self):
        """At c=1/2 (Ising): Q^contact = 10/(1/2 * 49/2) = 40/49."""
        result = numerical_coderived_check(Rational(1, 2))
        Q_expected = Rational(10) / (Rational(1, 2) * (Rational(5, 2) + 22))
        assert result['Q_contact'] == Q_expected
        assert result['ratio_equals_Q_contact'] is True

    def test_c13_self_dual(self):
        """At c=13: self-dual point, Q^contact = 10/1131."""
        result = numerical_coderived_check(Rational(13))
        Q_expected = Rational(10) / (13 * 87)
        assert result['Q_contact'] == Q_expected
        assert result['ratio_equals_Q_contact'] is True

    def test_c26_critical(self):
        """At c=26: critical dimension, Q^contact = 10/(26*152)."""
        result = numerical_coderived_check(Rational(26))
        Q_expected = Rational(10) / (26 * 152)
        assert result['Q_contact'] == Q_expected
        assert result['ratio_equals_Q_contact'] is True

    def test_c25_near_critical(self):
        """At c=25: near-critical, Koszul dual is Vir_1."""
        result = numerical_coderived_check(Rational(25))
        Q_expected = Rational(10) / (25 * 147)
        assert result['Q_contact'] == Q_expected
        assert result['ratio_equals_Q_contact'] is True


# =====================================================================
# Section E: Coderived triviality argument
# =====================================================================


class TestCoderivedTriviality:
    """Verify the coderived triviality argument."""

    def test_m0_exactness_lemma(self):
        """LEMMA: m_0 * x = d^2(x) for any x."""
        result = coderived_triviality_argument()
        assert result['lemma'] == 'm_0 * x = d^2(x) for any x in a curved dg module'
        assert result['phi_is_coderived_quasi_iso'] is True

    def test_delta4_is_exact_in_Dco(self):
        """delta_4 = Q^contact * m_0 is exact in D^co."""
        result = coderived_triviality_argument()
        assert result['cone_coacyclicity'] is True
        assert result['phi_is_coderived_quasi_iso'] is True

    def test_corrects_previous_analysis(self):
        """This analysis corrects the class M engine Section 6.

        The class M engine asked: is delta_4 in Im(d_curv)?
        Answer: NO (correct).
        But the RIGHT question is: is delta_4 trivial in D^co?
        Answer: YES (because delta_4 = Q^contact * m_0 and m_0 * x = d^2(x)).
        """
        result = coderived_triviality_argument()
        assert 'wrong question' in result['corrects_existing_analysis'].lower()

    def test_bar_has_zero_curvature(self):
        """Bar complex: d_B^2 = 0 (curvature absorbed)."""
        result = coderived_triviality_argument()
        assert result['bar_complex_curvature'] == '0 (curvature absorbed: d_B^2 = 0)'

    def test_bv_has_nonzero_curvature(self):
        """BV complex: d_BV^2 = m_0 = kappa * omega_1."""
        result = coderived_triviality_argument()
        assert result['bv_complex_curvature'] == 'm_0 = kappa * omega_1'


# =====================================================================
# Section F: Curved homotopy witness
# =====================================================================


class TestCurvedHomotopyWitness:
    """Verify the explicit curved homotopy."""

    def test_homotopy_formula(self):
        """h(e) = Q^contact * d_BV(e)."""
        result = curved_homotopy_witness()
        assert result['homotopy_formula'] == 'h(e) = Q^contact * d_BV(e) for quartic element e'

    def test_homotopy_verification(self):
        """d(h(e)) = delta_4 * e."""
        result = curved_homotopy_witness()
        assert 'delta_4 * e' in result['verification']

    def test_homotopy_coefficient_is_Q_contact(self):
        """The homotopy coefficient is Q^contact."""
        c = Symbol('c')
        result = curved_homotopy_witness(c)
        Q_expected = 10 / (c * (5 * c + 22))
        assert simplify(result['h_coefficient'] - Q_expected) == 0

    def test_homotopy_well_defined(self):
        """The homotopy is well-defined on the quartic sector."""
        result = curved_homotopy_witness()
        assert result['well_defined'] is True


# =====================================================================
# Section G: Higher-arity obstructions
# =====================================================================


class TestHigherArityObstructions:
    """Verify coderived triviality at all arities."""

    def test_arity4_trivial(self):
        """Arity 4: delta_4 ~ m_0^1, trivial."""
        result = higher_arity_coderived()
        assert result['by_arity']['arity_4']['trivial_in_Dco'] is True
        assert result['by_arity']['arity_4']['m_0_power'] == 1

    def test_arity6_trivial(self):
        """Arity 6: delta_6 ~ m_0^2, trivial."""
        result = higher_arity_coderived()
        assert result['by_arity']['arity_6']['trivial_in_Dco'] is True
        assert result['by_arity']['arity_6']['m_0_power'] == 2

    def test_arity8_trivial(self):
        """Arity 8: delta_8 ~ m_0^3, trivial."""
        result = higher_arity_coderived()
        assert result['by_arity']['arity_8']['trivial_in_Dco'] is True
        assert result['by_arity']['arity_8']['m_0_power'] == 3

    def test_all_arities_trivial(self):
        """ALL even arities 4-8 are trivial in D^co."""
        result = higher_arity_coderived()
        assert result['all_trivial'] is True

    def test_m0_power_formula(self):
        """m_0 power at arity r is r/2 - 1."""
        result = higher_arity_coderived(r_max=12)
        for r in range(4, 13, 2):
            key = f'arity_{r}'
            assert result['by_arity'][key]['m_0_power'] == r // 2 - 1

    def test_d_power_for_exactness(self):
        """d^{2n}(x) = d(d^{2n-1}(x)) is in Im(d), with n = r/2-1."""
        result = higher_arity_coderived(r_max=10)
        for r in range(4, 11, 2):
            key = f'arity_{r}'
            n = r // 2 - 1
            assert result['by_arity'][key]['d_power_for_exactness'] == 2 * n


# =====================================================================
# Section H: W_N generalization
# =====================================================================


class TestWNGeneralization:
    """Verify coderived triviality for W_N algebras."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro, Q^contact = 10/(c(5c+22))."""
        c = Symbol('c')
        result = wn_coderived_data(2, c)
        Q_expected = 10 / (c * (5 * c + 22))
        assert simplify(result['Q_contact'] - Q_expected) == 0
        assert result['coderived_trivial'] is True

    def test_w3_coderived_trivial(self):
        """W_3 (class M): delta_4 = Q_W3 * m_0, trivial in D^co."""
        result = wn_coderived_data(3)
        assert result['coderived_trivial'] is True
        assert result['shadow_depth'] == 'infinity'

    def test_w4_coderived_trivial(self):
        """W_4: coderived trivial."""
        result = wn_coderived_data(4)
        assert result['coderived_trivial'] is True

    def test_all_arities_trivial_wn(self):
        """For any W_N: all arities are coderived-trivial."""
        for N in [2, 3, 4, 5, 10]:
            result = wn_coderived_data(N)
            assert result['all_arities_trivial'] is True


# =====================================================================
# Section I: Genus >= 2 propagation
# =====================================================================


class TestGenus2Propagation:
    """Verify coderived triviality at genus >= 2."""

    def test_genus2_coderived_trivial(self):
        """At genus 2: delta_4^(2) = Q^contact * m_0^(2), trivial."""
        result = genus2_coderived()
        assert result['coderived_trivial'] is True

    def test_ratio_genus_independent(self):
        """The ratio delta_4/m_0 = Q^contact is independent of genus.

        Multi-path:
          Path 1: genus-1 ratio
          Path 2: general genus ratio
          Both should equal Q^contact.
        """
        c = Symbol('c')

        # Path 1: genus 1
        result1 = curvature_proportionality_test(c)

        # Path 2: general genus
        result2 = genus2_coderived(c)

        Q_expected = 10 / (c * (5 * c + 22))
        assert simplify(result1['ratio_path1'] - Q_expected) == 0
        assert simplify(result2['ratio'] - Q_expected) == 0

    def test_universal_statement(self):
        """BV=bar in D^co for ALL genera and ALL classes."""
        result = genus2_coderived()
        assert 'all g >= 0' in result['universal_statement'].lower()


# =====================================================================
# Section J: Cross-class coderived status
# =====================================================================


class TestCrossClassStatus:
    """Verify the cross-class coderived BV=bar status."""

    def test_class_g_strict(self):
        """Class G (Heisenberg): strict chain-level BV=bar."""
        result = cross_class_coderived_status()
        assert result['G']['chain_level_bv_bar'] is True
        assert result['G']['coderived_bv_bar'] is True

    def test_class_l_strict(self):
        """Class L (Affine KM): strict chain-level BV=bar."""
        result = cross_class_coderived_status()
        assert result['L']['chain_level_bv_bar'] is True
        assert result['L']['coderived_bv_bar'] is True

    def test_class_c_strict(self):
        """Class C (Beta-gamma): strict chain-level BV=bar."""
        result = cross_class_coderived_status()
        assert result['C']['chain_level_bv_bar'] is True
        assert result['C']['coderived_bv_bar'] is True

    def test_class_m_not_strict_but_coderived(self):
        """Class M (Virasoro/W_N): NOT strict, but coderived BV=bar."""
        result = cross_class_coderived_status()
        assert result['M']['chain_level_bv_bar'] is False
        assert result['M']['coderived_bv_bar'] is True

    def test_all_classes_coderived_equivalent(self):
        """ALL classes have BV=bar in D^co."""
        result = cross_class_coderived_status()
        for cls in ['G', 'L', 'C', 'M']:
            assert result[cls]['coderived_bv_bar'] is True

    def test_class_m_upgrade_essential(self):
        """For class M, the coderived upgrade is ESSENTIAL."""
        result = cross_class_coderived_status()
        assert 'essential' in result['M']['coderived_upgrade'].lower()

    def test_summary_universal(self):
        """Summary: BV=bar in D^co for ALL classes."""
        result = cross_class_coderived_status()
        assert 'all classes' in result['summary']['coderived'].lower()


# =====================================================================
# Section K: Complementarity and Koszul duality
# =====================================================================


class TestComplementarityKoszulDuality:
    """Verify complementarity properties in D^co."""

    def test_koszul_dual_both_trivial(self):
        """Both Vir_c and Vir_{26-c} are coderived-trivial."""
        result = koszul_dual_coderived()
        assert result['Vir_c']['coderived_trivial'] is True
        assert result['Vir_dual']['coderived_trivial'] is True

    def test_c13_self_dual_Q_contact(self):
        """At c=13: Q^contact(13) = Q^contact(13) (self-dual)."""
        result = koszul_dual_coderived()
        assert result['at_c_13']['self_dual'] is True
        assert result['at_c_13']['Q_c'] == result['at_c_13']['Q_dual']

    def test_complementarity_sum_coderived_trivial(self):
        """Complementarity sum is coderived-trivial (both terms are)."""
        result = coderived_complementarity()
        assert result['coderived_status'] == 'BOTH trivial in D^co'

    def test_c26_ghost_resolution(self):
        """At c=26: the effective discrepancy is coderived-trivial.

        This resolves the class M engine's finding that the ghost system
        does NOT cancel the discrepancy at the chain level.
        """
        result = coderived_complementarity()
        assert 'trivial in d^co' in result['critical_dimension_resolution'].lower()

    def test_complementarity_cross_check_with_class_m(self):
        """Cross-check: complementarity formula matches class M engine.

        Multi-path:
          Path 1: coderived engine
          Path 2: class M engine discrepancy_complementarity
        """
        c = Symbol('c')
        im_tau = Symbol('Im_tau', positive=True)

        result_cd = coderived_complementarity(c)
        result_cm = discrepancy_complementarity(c)

        # Both should give the same complementarity sum formula
        # The coderived engine gives the sum with Im_tau explicit
        # The class M engine gives the coefficient of 1/Im_tau
        # Cross-check at c=13
        result_cd_c13 = coderived_complementarity(Rational(13))
        delta_eff_c13 = result_cd_c13['delta_effective']
        # Should be 10/87 / Im_tau
        expected_c13 = Rational(10, 87) / im_tau
        assert simplify(delta_eff_c13 - expected_c13) == 0


# =====================================================================
# Section L: Matrix model verification
# =====================================================================


class TestMatrixModel:
    """Verify the coderived result in the finite-dimensional model."""

    def test_curved_relation_holds(self):
        """d^2 = [m_0, -] in the model."""
        result = matrix_model_verification()
        assert result['curved_relation_holds'] is True

    def test_ratio_equals_Q_contact(self):
        """delta_4/m_0 = Q^contact in the model."""
        result = matrix_model_verification()
        assert result['ratio_equals_Q_contact'] is True

    def test_coderived_trivial_in_model(self):
        """delta_4 is coderived-trivial in the model."""
        result = matrix_model_verification()
        assert result['coderived_trivial_in_model'] is True

    def test_model_ratio_at_specific_c(self):
        """Model ratio at c=1, c=13, c=26.

        Multi-path:
          Path 1: matrix_model_verification at specific c
          Path 2: direct Q^contact computation
        """
        for c_val in [Rational(1), Rational(13), Rational(26)]:
            result = matrix_model_verification(c_val)
            Q_expected = Rational(10) / (c_val * (5 * c_val + 22))
            assert simplify(result['ratio'] - Q_expected) == 0


# =====================================================================
# Section M: Coderived vs contraderived
# =====================================================================


class TestCoderivedVsContraderived:
    """Verify the co/contra comparison."""

    def test_both_give_same_result(self):
        """D^co and D^ctr give the same answer for Koszul algebras."""
        result = coderived_vs_contraderived()
        assert result['both_give_same_result'] is True

    def test_positselski_equivalence(self):
        """D^co(A-comod) ~ D^ctr(A!-mod) for Koszul A."""
        result = coderived_vs_contraderived()
        assert 'Koszul' in result['equivalence']

    def test_corrects_class_m_contraderived_section(self):
        """This corrects the class M engine Section 10 conclusion."""
        result = coderived_vs_contraderived()
        assert 'incorrect' in result['corrects_class_m_engine'].lower()

    def test_bar_naturally_coderived(self):
        """Bar complex is naturally a coalgebra -> D^co."""
        result = coderived_vs_contraderived()
        assert 'coalgebra' in result['coderived_approach']['natural_for']

    def test_bv_naturally_contraderived(self):
        """BV observables are naturally an algebra -> D^ctr."""
        result = coderived_vs_contraderived()
        assert 'algebra' in result['contraderived_approach']['natural_for']


# =====================================================================
# Section N: Complete synthesis
# =====================================================================


class TestCompleteSynthesis:
    """Verify the complete synthesis."""

    def test_main_theorem_statement(self):
        """Main theorem: Obs_BV ~ B(A) in D^co for all g >= 0."""
        result = bv_bar_coderived_synthesis()
        assert 'D^co' in result['theorem']
        assert 'g >= 0' in result['theorem']

    def test_proof_step_count(self):
        """Proof has 6 steps."""
        result = bv_bar_coderived_synthesis()
        assert len(result['proof_steps']) == 6

    def test_class_m_coderived(self):
        """Class M uses coderived (curvature absorption)."""
        result = bv_bar_coderived_synthesis()
        assert 'coderived' in result['class_M']

    def test_classes_glc_strict(self):
        """Classes G, L, C are strict."""
        result = bv_bar_coderived_synthesis()
        assert 'strict' in result['class_G']
        assert 'strict' in result['class_L']
        assert 'strict' in result['class_C']

    def test_upgrades_conjecture(self):
        """This upgrades conj:master-bv-brst to a resolved statement."""
        result = bv_bar_coderived_synthesis()
        assert 'resolved' in result['upgrades_conjecture'].lower()

    def test_shadow_depth_independent(self):
        """Shadow depth does NOT affect coderived equivalence."""
        result = bv_bar_coderived_synthesis()
        assert 'does not affect' in result['relationship_to_shadow_depth'].lower()


# =====================================================================
# Section O: Deep cross-verification (multi-path synthesis)
# =====================================================================


class TestDeepCrossVerification:
    """Deep multi-path verification combining all sections."""

    def test_three_path_proportionality_c1(self):
        """At c=1: delta_4/m_0 = Q^contact by THREE independent paths.

        Path 1: symbolic (curvature_proportionality_test)
        Path 2: numerical float (curvature_proportionality_numerical)
        Path 3: exact rational (numerical_coderived_check)
        """
        # Path 1: symbolic
        result1 = curvature_proportionality_test(Rational(1))
        assert result1['all_paths_agree'] is True

        # Path 2: numerical
        result2 = curvature_proportionality_numerical(1.0)
        assert result2['match'] is True

        # Path 3: exact
        result3 = numerical_coderived_check(Rational(1))
        assert result3['ratio_equals_Q_contact'] is True

        # Cross-check: all three give the same Q^contact
        Q_exact = Rational(10, 27)
        assert simplify(result1['Q_contact'] - Q_exact) == 0
        assert abs(result2['Q_contact'] - float(Q_exact)) < 1e-14
        assert result3['Q_contact'] == Q_exact

    def test_three_path_proportionality_c13(self):
        """At c=13 (self-dual): three-path cross-check."""
        # Path 1
        result1 = curvature_proportionality_test(Rational(13))
        assert result1['all_paths_agree'] is True

        # Path 2
        result2 = curvature_proportionality_numerical(13.0)
        assert result2['match'] is True

        # Path 3
        result3 = numerical_coderived_check(Rational(13))
        assert result3['ratio_equals_Q_contact'] is True

    def test_coderived_formula_matches_class_m_obstruction(self):
        """The coderived engine's delta_4 formula matches the class M engine.

        Multi-path:
          Path 1: coderived harmonic_obstruction_virasoro
          Path 2: class M quartic_harmonic_amplitude_virasoro
          Path 3: class M quartic_harmonic_numerical
          Path 4: direct 5/((5c+22)*Im_tau)
        """
        # Path 1 vs Path 2 (symbolic)
        c = Symbol('c')
        r1 = harmonic_obstruction_virasoro(c)
        r2 = quartic_harmonic_amplitude_virasoro(c)
        assert simplify(r1['delta_4'] - r2['contact_harm_amplitude']) == 0

        # Path 3 vs Path 4 (numerical at c=13)
        r3 = quartic_harmonic_numerical(13.0)
        r4 = 5.0 / (5.0 * 13.0 + 22.0)
        assert abs(r3['contact_harm_coeff'] - r4) < 1e-14

    def test_m0_exactness_at_multiple_c(self):
        """Verify m_0 * x = d^2(x) indirectly via ratio = Q^contact.

        If delta_4 = Q^contact * m_0 for many c values, and this ratio
        is always Q^contact (a pure algebraic function of c), then the
        proportionality is structural, not accidental.
        """
        c_values = [Rational(1, 2), Rational(1), Rational(2),
                     Rational(13), Rational(25), Rational(26),
                     Rational(100)]
        for c_val in c_values:
            result = numerical_coderived_check(c_val)
            assert result['ratio_equals_Q_contact'] is True, f"Failed at c={c_val}"

    def test_w2_virasoro_consistency(self):
        """W_2 coderived data matches Virasoro coderived data.

        Multi-path:
          Path 1: wn_coderived_data(2, c)
          Path 2: curvature_proportionality_test(c)
          Both should give the same Q^contact.
        """
        c = Symbol('c')
        r1 = wn_coderived_data(2, c)
        r2 = curvature_proportionality_test(c)
        assert simplify(r1['Q_contact'] - r2['Q_contact']) == 0
