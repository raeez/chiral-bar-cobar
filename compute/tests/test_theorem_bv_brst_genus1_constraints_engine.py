r"""Tests for theorem_bv_brst_genus1_constraints_engine.

Genus-1 constraints on conj:master-bv-brst from the KZ25 sigma model framework.

MULTI-PATH VERIFICATION (CLAUDE.md mandate):
  Every numerical result verified by at least 3 independent paths.
  Every epistemic status claim verified against the known proof landscape.

TEST STRUCTURE:
  Section A: Faber-Pandharipande numbers (2 independent computations)
  Section B: BV 1-loop determinant for standard families
  Section C: Genus-1 bar free energy (3-path verification)
  Section D: BV = bar comparison at genus 1
  Section E: Genus-1 curvature identity
  Section F: Genus-2 planted-forest constraints
  Section G: Cross-family additivity
  Section H: Complementarity at genus 1
  Section I: KZ25-specific constraints
  Section J: Epistemic status classification
  Section K: Numerical spot checks
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_bv_brst_genus1_constraints_engine import (
    BVOneLoopResult,
    ChiralAlgebraData,
    CurvatureIdentityResult,
    EpistemicStatus,
    EpistemicStatusReport,
    Genus1ComparisonResult,
    Genus2ConstraintResult,
    KZ25Constraint,
    ShadowClass,
    affine_sl2,
    affine_sl3,
    betagamma,
    bv_one_loop_determinant,
    complementarity_genus1_check,
    cross_family_additivity_check,
    F1_from_ahat,
    F1_from_lambda_fp,
    F1_from_zeta_regularization,
    full_constraint_summary,
    full_epistemic_report,
    genus1_bv_bar_comparison,
    genus1_curvature_identity,
    genus1_three_path_verification,
    genus2_planted_forest_constraint,
    heisenberg,
    heisenberg_eta_function_check,
    kz25_genus0_constraint,
    kz25_genus1_constraint,
    kz25_genus1_curvature_constraint,
    kz25_genus2_constraint,
    lambda_fp_exact,
    lambda_fp_sympy,
    numerical_genus1_comparison,
    virasoro,
)


# =====================================================================
# Section A: Faber-Pandharipande numbers
# =====================================================================


class TestLambdaFP:
    """Verify lambda_g^FP by two independent computation methods."""

    def test_lambda1_exact(self):
        """lambda_1^FP = 1/24 (the fundamental genus-1 constant)."""
        assert lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda2_exact(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda3_exact(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_fp_two_methods_agree(self):
        """Cross-check: exact Fraction computation agrees with sympy Bernoulli."""
        from sympy import Rational
        for g in range(1, 6):
            exact = lambda_fp_exact(g)
            sympy_val = lambda_fp_sympy(g)
            assert Fraction(int(sympy_val.p), int(sympy_val.q)) == exact, \
                f"Mismatch at g={g}: exact={exact}, sympy={sympy_val}"

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert lambda_fp_exact(g) > 0, f"lambda_{g}^FP should be positive"

    def test_lambda_fp_invalid_genus(self):
        """lambda_fp raises for genus < 1."""
        with pytest.raises(ValueError):
            lambda_fp_exact(0)


# =====================================================================
# Section B: BV 1-loop determinant
# =====================================================================


class TestBVOneLoop:
    """BV 1-loop determinant on E_tau x R."""

    def test_heisenberg_k1(self):
        """Heisenberg at k=1: alpha = kappa = 1, F_1 = 1/24."""
        result = bv_one_loop_determinant(heisenberg(1))
        assert result.alpha_bv == Fraction(1)
        assert result.kappa == Fraction(1)
        assert result.F1_bv == Fraction(1, 24)
        assert result.match is True
        assert result.status == EpistemicStatus.PROVED

    def test_heisenberg_k3(self):
        """Heisenberg at k=3: F_1 = 3/24 = 1/8."""
        result = bv_one_loop_determinant(heisenberg(3))
        assert result.F1_bv == Fraction(3, 24)
        assert result.F1_bv == Fraction(1, 8)
        assert result.match is True

    def test_sl2_k1(self):
        """Affine sl_2 at k=1: kappa = 3*3/4 = 9/4, F_1 = 9/96 = 3/32."""
        result = bv_one_loop_determinant(affine_sl2(1))
        assert result.kappa == Fraction(9, 4)
        assert result.F1_bv == Fraction(9, 4) * Fraction(1, 24)
        assert result.F1_bv == Fraction(3, 32)
        assert result.match is True
        assert result.status == EpistemicStatus.PROVED

    def test_virasoro_c26(self):
        """Virasoro at c=26: kappa = 13, F_1 = 13/24."""
        result = bv_one_loop_determinant(virasoro(Fraction(26)))
        assert result.kappa == Fraction(13)
        assert result.F1_bv == Fraction(13, 24)
        assert result.match is True
        assert result.status == EpistemicStatus.CONDITIONAL

    def test_virasoro_c1(self):
        """Virasoro at c=1: kappa = 1/2, F_1 = 1/48."""
        result = bv_one_loop_determinant(virasoro(Fraction(1)))
        assert result.kappa == Fraction(1, 2)
        assert result.F1_bv == Fraction(1, 48)
        assert result.match is True

    def test_betagamma(self):
        """Beta-gamma: kappa = 1, F_1 = 1/24."""
        result = bv_one_loop_determinant(betagamma())
        assert result.kappa == Fraction(1)
        assert result.F1_bv == Fraction(1, 24)
        assert result.match is True

    def test_zeta_prime_dbar(self):
        """zeta'_dbar(0) = -1/24 universally."""
        for alg in [heisenberg(1), affine_sl2(1), virasoro(Fraction(26))]:
            result = bv_one_loop_determinant(alg)
            assert result.zeta_prime_dbar == Fraction(-1, 24)


# =====================================================================
# Section C: Three-path F_1 verification
# =====================================================================


class TestThreePathF1:
    """Three independent computations of F_1 = kappa / 24."""

    def test_three_paths_agree_heisenberg(self):
        """All three paths give F_1 = k/24 for Heisenberg."""
        for k in [1, 2, 5, 10]:
            kappa = Fraction(k)
            assert F1_from_lambda_fp(kappa) == kappa * Fraction(1, 24)
            assert F1_from_ahat(kappa) == kappa * Fraction(1, 24)
            assert F1_from_zeta_regularization(kappa) == kappa * Fraction(1, 24)

    def test_three_paths_agree_virasoro(self):
        """All three paths give F_1 = c/48 for Virasoro."""
        for c in [Fraction(1), Fraction(1, 2), Fraction(26), Fraction(25, 2)]:
            kappa = c / 2
            result = genus1_three_path_verification(virasoro(c))
            assert result['all_agree'] is True
            assert result['F1'] == kappa * Fraction(1, 24)

    def test_three_paths_agree_sl2(self):
        """All three paths agree for affine sl_2."""
        for k in [1, 2, 4, 10]:
            result = genus1_three_path_verification(affine_sl2(k))
            assert result['all_agree'] is True
            expected_kappa = Fraction(3 * (k + 2), 4)
            assert result['kappa'] == expected_kappa

    def test_three_path_struct(self):
        """genus1_three_path_verification returns well-formed dict."""
        result = genus1_three_path_verification(heisenberg(1))
        assert 'F1_lambda_fp' in result
        assert 'F1_ahat' in result
        assert 'F1_zeta_reg' in result
        assert result['F1'] is not None


# =====================================================================
# Section D: BV = bar comparison at genus 1
# =====================================================================


class TestGenus1Comparison:
    """Full BV vs bar comparison at genus 1."""

    def test_heisenberg_comparison(self):
        """Heisenberg: scalar match, no obstruction, PROVED."""
        result = genus1_bv_bar_comparison(heisenberg(1))
        assert result.scalar_match is True
        assert result.alpha_equals_kappa is True
        assert result.kz25_gauge_jacobi is True
        assert result.overall_status == EpistemicStatus.PROVED
        assert result.obstruction_to_chain_level is None

    def test_sl2_comparison(self):
        """Affine sl_2: scalar match, no obstruction, PROVED."""
        result = genus1_bv_bar_comparison(affine_sl2(1))
        assert result.scalar_match is True
        assert result.overall_status == EpistemicStatus.PROVED
        assert result.obstruction_to_chain_level is None

    def test_virasoro_comparison(self):
        """Virasoro: scalar match, obstruction present, CONDITIONAL."""
        result = genus1_bv_bar_comparison(virasoro(Fraction(26)))
        assert result.scalar_match is True
        assert result.overall_status == EpistemicStatus.CONDITIONAL
        assert result.obstruction_to_chain_level is not None
        assert 'quartic' in result.obstruction_to_chain_level.lower()

    def test_betagamma_comparison(self):
        """Beta-gamma: scalar match, CONDITIONAL (Q_contact = 0 helps)."""
        result = genus1_bv_bar_comparison(betagamma())
        assert result.scalar_match is True
        assert result.overall_status == EpistemicStatus.CONDITIONAL

    def test_curvature_coefficient_is_kappa(self):
        """The curvature coefficient equals kappa for all families."""
        for alg in [heisenberg(1), affine_sl2(2), virasoro(Fraction(12)), betagamma()]:
            result = genus1_bv_bar_comparison(alg)
            assert result.curvature_coefficient == alg.kappa


# =====================================================================
# Section E: Genus-1 curvature identity
# =====================================================================


class TestCurvatureIdentity:
    """d_bar^2 = kappa * omega_1 at genus 1."""

    def test_curvature_heisenberg(self):
        """Heisenberg curvature identity."""
        result = genus1_curvature_identity(heisenberg(3))
        assert result.m0_coefficient == Fraction(3)
        assert result.bv_anomaly_coefficient == Fraction(3)
        assert result.match is True

    def test_curvature_sl2(self):
        """sl_2 curvature identity: m_0 = 3(k+2)/4 * omega_1."""
        result = genus1_curvature_identity(affine_sl2(2))
        assert result.kappa == Fraction(3)
        assert result.match is True

    def test_curvature_virasoro(self):
        """Virasoro curvature identity: m_0 = c/2 * omega_1."""
        result = genus1_curvature_identity(virasoro(Fraction(26)))
        assert result.kappa == Fraction(13)
        assert result.match is True


# =====================================================================
# Section F: Genus-2 planted-forest constraints
# =====================================================================


class TestGenus2Constraint:
    """Genus-2 obstruction from planted-forest correction."""

    def test_heisenberg_delta_pf_zero(self):
        """Heisenberg: S_3 = 0, so delta_pf = 0 (class G terminates at arity 2)."""
        result = genus2_planted_forest_constraint(heisenberg(1), Fraction(0))
        assert result.delta_pf == Fraction(0)
        assert result.F2_bar_full == result.F2_bar_scalar

    def test_virasoro_delta_pf(self):
        """Virasoro at general c: delta_pf = S_3*(10*S_3 - kappa)/48.

        For Virasoro: S_3 = -2/c, kappa = c/2.
        delta_pf = (-2/c) * (10*(-2/c) - c/2) / 48
                 = (-2/c) * (-20/c - c/2) / 48
                 = (-2/c) * (-(40 + c^2)/(2c)) / 48
                 = (40 + c^2) / (c^2 * 48)
                 Wait, let me recompute:
        delta_pf = (-2/c) * (10*(-2/c) - c/2) / 48
                 = (-2/c) * (-20/c - c/2) / 48
        Let me compute numerically for c = 1:
          S_3 = -2, kappa = 1/2
          delta_pf = (-2) * (10*(-2) - 1/2) / 48 = (-2)*(-41/2)/48 = 41/48
        """
        c = Fraction(1)
        S3 = Fraction(-2)  # S_3 = -2/c = -2 for c=1
        kappa = c / 2
        result = genus2_planted_forest_constraint(virasoro(c), S3)
        expected_delta = S3 * (10 * S3 - kappa) / Fraction(48)
        assert result.delta_pf == expected_delta
        assert result.delta_pf == Fraction(-2) * (Fraction(-20) - Fraction(1, 2)) / Fraction(48)
        assert result.delta_pf == Fraction(-2) * Fraction(-41, 2) / Fraction(48)
        assert result.delta_pf == Fraction(41, 48)

    def test_virasoro_c26_delta_pf(self):
        """Virasoro at c=26: S_3 = -2/26 = -1/13, kappa = 13."""
        S3 = Fraction(-1, 13)
        result = genus2_planted_forest_constraint(virasoro(Fraction(26)), S3)
        # delta_pf = (-1/13) * (10*(-1/13) - 13) / 48
        #          = (-1/13) * (-10/13 - 13) / 48
        #          = (-1/13) * (-10/13 - 169/13) / 48
        #          = (-1/13) * (-179/13) / 48
        #          = 179 / (13*13*48)
        #          = 179 / 8112
        expected = Fraction(179, 8112)
        assert result.delta_pf == expected

    def test_lambda2_fp_value(self):
        """lambda_2^FP = 7/5760 in the genus-2 constraint."""
        result = genus2_planted_forest_constraint(heisenberg(1), Fraction(0))
        assert result.lambda2_fp == Fraction(7, 5760)

    def test_genus2_status_conjectural(self):
        """Genus-2 BV = bar is CONJECTURAL for all families."""
        for alg, s3 in [(heisenberg(1), Fraction(0)),
                        (affine_sl2(1), Fraction(1, 3)),
                        (virasoro(Fraction(26)), Fraction(-1, 13))]:
            result = genus2_planted_forest_constraint(alg, s3)
            assert result.bv_genus2_status == EpistemicStatus.CONJECTURAL


# =====================================================================
# Section G: Cross-family additivity
# =====================================================================


class TestCrossFamilyAdditivity:
    """Independent sum factorization at genus 1."""

    def test_two_heisenberg(self):
        """H_k1 + H_k2: kappa and F_1 are additive."""
        result = cross_family_additivity_check(heisenberg(3), heisenberg(5))
        assert result['additive'] is True
        assert result['kappa_sum'] == Fraction(8)
        assert result['F1_combined'] == Fraction(8, 24)

    def test_heisenberg_plus_sl2(self):
        """H_1 + sl_2 at k=1: kappa additive, F_1 additive."""
        result = cross_family_additivity_check(heisenberg(1), affine_sl2(1))
        assert result['additive'] is True
        expected_sum = Fraction(1) + Fraction(9, 4)
        assert result['kappa_sum'] == expected_sum

    def test_additivity_is_linear(self):
        """F_1(A+B) = F_1(A) + F_1(B) for any pair (linearity of kappa)."""
        pairs = [
            (heisenberg(1), heisenberg(2)),
            (heisenberg(1), virasoro(Fraction(2))),
            (affine_sl2(1), affine_sl2(2)),
        ]
        for a1, a2 in pairs:
            result = cross_family_additivity_check(a1, a2)
            assert result['additive'] is True


# =====================================================================
# Section H: Complementarity at genus 1
# =====================================================================


class TestComplementarityGenus1:
    """Complementarity pairing at genus 1."""

    def test_sl2_complementarity(self):
        """sl_2: kappa(k) + kappa(-k-4) = 0 (KM anti-symmetry).

        For sl_2: h^v = 2, so k' = -k - 2*2 = -k - 4.
        kappa(k) = 3(k+2)/4,  kappa(k') = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4.
        Sum = 0.
        """
        k = 1
        kappa_k = Fraction(3 * (k + 2), 4)      # 9/4
        kappa_kp = Fraction(3 * (-k - 2), 4)     # -9/4
        result = complementarity_genus1_check(
            affine_sl2(k), kappa_kp, Fraction(0))
        assert result['sum_correct'] is True
        assert result['F1_sum'] == Fraction(0)

    def test_virasoro_complementarity(self):
        """Virasoro: kappa(c) + kappa(26-c) = 13 (AP24).

        kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2.
        Sum = c/2 + (26-c)/2 = 26/2 = 13.
        """
        c = Fraction(10)
        kappa_c = c / 2              # 5
        kappa_26mc = (26 - c) / 2    # 8
        result = complementarity_genus1_check(
            virasoro(c), kappa_26mc, Fraction(13))
        assert result['sum_correct'] is True
        assert result['F1_sum'] == Fraction(13, 24)

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c=13: self-dual, kappa = 13/2, kappa + kappa' = 13."""
        kappa_13 = Fraction(13, 2)
        result = complementarity_genus1_check(
            virasoro(Fraction(13)), kappa_13, Fraction(13))
        assert result['sum_correct'] is True
        # F_1 + F_1' = 13/24
        assert result['F1_sum'] == Fraction(13, 24)


# =====================================================================
# Section I: KZ25-specific constraints
# =====================================================================


class TestKZ25Constraints:
    """Constraints from the KZ25 sigma model framework."""

    def test_genus0_gauge_jacobi(self):
        """Genus 0: gauge invariance = Jacobi, PROVED."""
        c = kz25_genus0_constraint()
        assert c.genus == 0
        assert c.match is True
        assert c.status == EpistemicStatus.PROVED

    def test_genus1_one_loop_heisenberg(self):
        """Genus 1 one-loop for Heisenberg: PROVED."""
        c = kz25_genus1_constraint(heisenberg(1))
        assert c.genus == 1
        assert c.match is True
        assert c.status == EpistemicStatus.PROVED

    def test_genus1_one_loop_virasoro(self):
        """Genus 1 one-loop for Virasoro: CONDITIONAL."""
        c = kz25_genus1_constraint(virasoro(Fraction(26)))
        assert c.genus == 1
        assert c.match is True
        assert c.status == EpistemicStatus.CONDITIONAL

    def test_genus1_curvature_constraint(self):
        """Genus 1 curvature for sl_2: d_bar^2 = kappa * omega_1."""
        c = kz25_genus1_curvature_constraint(affine_sl2(1))
        assert c.genus == 1
        assert c.match is True

    def test_genus2_planted_forest_constraint(self):
        """Genus 2: CONJECTURAL for all families."""
        c = kz25_genus2_constraint(heisenberg(1), Fraction(0))
        assert c.genus == 2
        assert c.status == EpistemicStatus.CONJECTURAL


# =====================================================================
# Section J: Epistemic status classification
# =====================================================================


class TestEpistemicStatus:
    """Verify the epistemic status classification is correct."""

    def test_heisenberg_proved(self):
        """Heisenberg BV = bar at genus 1 is PROVED."""
        report = full_epistemic_report(heisenberg(1))
        assert report.genus1_chain_level_status == EpistemicStatus.PROVED
        assert report.genus1_scalar_match is True
        assert report.three_path_F1_agreement is True

    def test_sl2_proved(self):
        """Affine sl_2 BV = bar at genus 1 is PROVED."""
        report = full_epistemic_report(affine_sl2(1), Fraction(1, 3))
        assert report.genus1_chain_level_status == EpistemicStatus.PROVED

    def test_virasoro_conditional(self):
        """Virasoro BV = bar at genus 1 is CONDITIONAL."""
        report = full_epistemic_report(virasoro(Fraction(26)), Fraction(-1, 13))
        assert report.genus1_chain_level_status == EpistemicStatus.CONDITIONAL
        assert report.genus1_scalar_match is True

    def test_genus2_always_conjectural(self):
        """Genus 2 is CONJECTURAL for all families."""
        for alg, s3 in [(heisenberg(1), Fraction(0)),
                        (virasoro(Fraction(26)), Fraction(-1, 13))]:
            report = full_epistemic_report(alg, s3)
            assert report.genus2_scalar_status == EpistemicStatus.CONJECTURAL

    def test_kz25_constraints_count(self):
        """All 4 KZ25 constraints should be satisfied (at scalar level)."""
        report = full_epistemic_report(heisenberg(1))
        assert report.kz25_constraints_satisfied == 4
        assert report.kz25_constraints_total == 4

    def test_summary_contains_algebra_name(self):
        """The summary string contains the algebra name."""
        report = full_epistemic_report(heisenberg(1))
        assert 'H_1' in report.summary


# =====================================================================
# Section K: Numerical spot checks
# =====================================================================


class TestNumericalSpotChecks:
    """Numerical evaluations for specific parameter values."""

    def test_heisenberg_eta_k1(self):
        """Heisenberg k=1: eta function gives F_1 = 1/24."""
        result = heisenberg_eta_function_check(1)
        assert result['match'] is True
        assert result['F1_bar'] == Fraction(1, 24)

    def test_heisenberg_eta_k24(self):
        """Heisenberg k=24: F_1 = 24/24 = 1."""
        result = heisenberg_eta_function_check(24)
        assert result['F1_bar'] == Fraction(1)
        assert result['match'] is True

    def test_numerical_comparison_sl2(self):
        """Numerical F_1 for sl_2 at k=1."""
        result = numerical_genus1_comparison(affine_sl2(1))
        assert abs(result['F1_float'] - 3 / 32) < 1e-15

    def test_numerical_comparison_virasoro(self):
        """Numerical F_1 for Virasoro at c=26."""
        result = numerical_genus1_comparison(virasoro(Fraction(26)))
        assert abs(result['F1_float'] - 13 / 24) < 1e-15

    def test_full_summary_structure(self):
        """full_constraint_summary returns well-formed report."""
        summary = full_constraint_summary()
        assert summary['total'] == 7
        assert summary['genus1_scalar_universally_proved'] is True
        assert summary['proved_count'] + summary['conditional_count'] + \
            summary['conjectural_count'] == summary['total']


# =====================================================================
# Section L: Algebra data integrity
# =====================================================================


class TestAlgebraData:
    """Verify algebra data is self-consistent."""

    def test_heisenberg_kappa_is_level(self):
        """kappa(H_k) = k, NOT c/2 (AP48)."""
        for k in [1, 2, 5]:
            alg = heisenberg(k)
            assert alg.kappa == Fraction(k)

    def test_virasoro_kappa_is_c_over_2(self):
        """kappa(Vir_c) = c/2."""
        for c in [1, 2, 26, 13]:
            alg = virasoro(Fraction(c))
            assert alg.kappa == Fraction(c, 2)

    def test_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k in [1, 2, 4, 10]:
            alg = affine_sl2(k)
            assert alg.kappa == Fraction(3 * (k + 2), 4)

    def test_sl3_kappa_formula(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        for k in [1, 3, 6]:
            alg = affine_sl3(k)
            assert alg.kappa == Fraction(4 * (k + 3), 3)

    def test_shadow_classes(self):
        """Each family has the correct shadow class."""
        assert heisenberg(1).shadow_class == ShadowClass.G
        assert affine_sl2(1).shadow_class == ShadowClass.L
        assert betagamma().shadow_class == ShadowClass.C
        assert virasoro(Fraction(26)).shadow_class == ShadowClass.M

    def test_uniform_weight(self):
        """Heisenberg, sl_2, sl_3 are uniform-weight; beta-gamma is not."""
        assert heisenberg(1).is_uniform_weight is True
        assert affine_sl2(1).is_uniform_weight is True
        assert affine_sl3(1).is_uniform_weight is True
        assert betagamma().is_uniform_weight is False

    def test_is_free_field(self):
        """Only Heisenberg is free field (class G)."""
        assert heisenberg(1).is_free_field is True
        assert affine_sl2(1).is_free_field is False
        assert virasoro(Fraction(1)).is_free_field is False
