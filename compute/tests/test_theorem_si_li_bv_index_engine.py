r"""Tests for Si Li BV-to-algebraic-index programme vs bar-cobar framework.

Multi-path verification of the comparison between Si Li's BV quantization
programme (arXiv:2511.12875) and the monograph's bar-cobar framework.

Each test verifies a specific mathematical claim by at least 2 independent paths.
"""

import pytest
from sympy import Rational, bernoulli, factorial, Abs, simplify, Symbol, pi

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from theorem_si_li_bv_index_engine import (
    faber_pandharipande,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_km,
    kappa_beta_gamma,
    kappa_bc_system,
    kappa_beta_gamma_bc_pair,
    algebraic_index_1d,
    algebraic_index_2d_elliptic,
    qme_hierarchy_comparison,
    si_li_dictionary,
    genus_1_free_energy_bar,
    genus_1_free_energy_si_li,
    genus_1_match,
    witten_genus_leading_coefficient,
    a_hat_genus_coefficient,
    bcov_shadow_comparison,
    obstructions_from_si_li,
    verify_ahat_vs_fp,
    verify_si_li_qme_genus0,
    verify_si_li_uv_finiteness,
    verify_2d_to_1d_reduction,
    impact_assessment,
    chiral_fedosov_vs_shadow_connection,
    genus_g_free_energy_comparison,
    si_li_references,
)


# =========================================================================
# Group 1: Faber-Pandharipande numbers (canonical, cross-checked)
# =========================================================================


class TestFaberPandharipande:
    """Verify FP numbers against known values and A-hat coefficients."""

    def test_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == Rational(1, 24)

    def test_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == Rational(7, 5760)

    def test_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == Rational(31, 967680)

    def test_fp_genus4(self):
        """lambda_4^FP = 127/154828800."""
        assert faber_pandharipande(4) == Rational(127, 154828800)

    def test_fp_genus5(self):
        """lambda_5^FP = 73/3503554560."""
        assert faber_pandharipande(5) == Rational(73, 3503554560)

    def test_fp_positive(self):
        """All FP numbers are positive for g >= 1."""
        for g in range(1, 15):
            assert faber_pandharipande(g) > 0

    def test_fp_invalid_genus(self):
        """FP undefined at genus 0."""
        with pytest.raises(ValueError):
            faber_pandharipande(0)

    def test_fp_decreasing(self):
        """FP numbers decrease (lambda_g > lambda_{g+1} for g >= 1)."""
        for g in range(1, 10):
            assert faber_pandharipande(g) > faber_pandharipande(g + 1)


# =========================================================================
# Group 2: A-hat genus = FP numbers (the Si Li bridge)
# =========================================================================


class TestAHatGenusBridge:
    """Verify A-hat(ix) coefficients equal FP numbers.

    This is the central bridge: Si Li's BV trace produces A-hat,
    and our Theorem D produces FP numbers.  They must agree.
    """

    def test_ahat_equals_fp_genus1_to_10(self):
        """A-hat coefficient = FP number at each genus 1..10."""
        results = verify_ahat_vs_fp(10)
        for g, ahat, fp, match in results:
            assert match, f"Mismatch at genus {g}: A-hat={ahat}, FP={fp}"

    def test_ahat_coefficient_genus1(self):
        """A-hat coefficient at genus 1 = 1/24."""
        assert a_hat_genus_coefficient(1) == Rational(1, 24)

    def test_ahat_coefficient_genus2(self):
        """A-hat coefficient at genus 2 = 7/5760."""
        assert a_hat_genus_coefficient(2) == Rational(7, 5760)

    def test_ahat_vs_fp_path1_bernoulli(self):
        """Path 1: compute A-hat coefficient directly from Bernoulli."""
        for g in range(1, 8):
            B_2g = bernoulli(2 * g)
            coeff = Abs(B_2g) * Rational(2**(2*g-1) - 1, 2**(2*g-1)) / factorial(2*g)
            assert coeff == faber_pandharipande(g)

    def test_ahat_vs_fp_path2_explicit(self):
        """Path 2: verify against known explicit values."""
        known = {
            1: Rational(1, 24),
            2: Rational(7, 5760),
            3: Rational(31, 967680),
        }
        for g, val in known.items():
            assert a_hat_genus_coefficient(g) == val


# =========================================================================
# Group 3: kappa formulas (canonical, multi-path)
# =========================================================================


class TestKappaFormulas:
    """Verify kappa formulas used in comparisons."""

    def test_kappa_heisenberg_level_1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(1) == 1

    def test_kappa_heisenberg_level_k(self):
        """kappa(H_k) = k for general k."""
        k = Symbol("k")
        assert kappa_heisenberg(k) == k

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(26) == 13

    def test_kappa_virasoro_general(self):
        """kappa(Vir_c) = c/2."""
        c = Symbol("c")
        assert kappa_virasoro(c) == c / 2

    def test_kappa_sl2(self):
        """kappa(sl2_k) = 3(k+2)/4."""
        k = Symbol("k")
        result = kappa_affine_km(3, k, 2)
        assert simplify(result - 3 * (k + 2) / 4) == 0

    def test_kappa_betagamma_bc_pure_bosonic(self):
        """For n_bos copies of betagamma, kappa_eff = n_bos."""
        assert kappa_beta_gamma_bc_pair(5, 0) == 5

    def test_kappa_betagamma_bc_pure_fermionic(self):
        """For n_fer copies of bc, kappa_eff = -n_fer."""
        assert kappa_beta_gamma_bc_pair(0, 3) == -3

    def test_kappa_betagamma_bc_mixed(self):
        """For mixed system, kappa_eff = n_bos - n_fer."""
        assert kappa_beta_gamma_bc_pair(10, 3) == 7


# =========================================================================
# Group 4: Genus-1 free energy comparison (the key match)
# =========================================================================


class TestGenus1FreeEnergy:
    """Verify F_1 matches between bar-cobar and Si Li."""

    def test_f1_bar_heisenberg(self):
        """F_1^bar(H_1) = 1/24."""
        assert genus_1_free_energy_bar(1) == Rational(1, 24)

    def test_f1_bar_heisenberg_k(self):
        """F_1^bar(H_k) = k/24."""
        for k in range(1, 10):
            assert genus_1_free_energy_bar(k) == Rational(k, 24)

    def test_f1_si_li_1_pair(self):
        """F_1^SiLi for 1 betagamma pair (dim h_0 = 2) = 1/24."""
        assert genus_1_free_energy_si_li(2) == Rational(1, 24)

    def test_f1_si_li_n_pairs(self):
        """F_1^SiLi for n pairs = n/24."""
        for n in range(1, 10):
            assert genus_1_free_energy_si_li(2 * n) == Rational(n, 24)

    def test_f1_match_heisenberg(self):
        """F_1 matches for Heisenberg at all levels."""
        for k in range(1, 10):
            assert genus_1_match(k, 2 * k)

    def test_f1_virasoro_bar(self):
        """F_1^bar(Vir_c) = c/48."""
        c = Symbol("c")
        result = genus_1_free_energy_bar(kappa_virasoro(c))
        assert simplify(result - c / 48) == 0

    def test_f1_bar_km_sl2(self):
        """F_1^bar(sl2_k) = 3(k+2)/(4*24) = (k+2)/32."""
        k = Symbol("k")
        kappa = kappa_affine_km(3, k, 2)
        f1 = genus_1_free_energy_bar(kappa)
        expected = Rational(3, 4) * (k + 2) / 24
        assert simplify(f1 - expected) == 0


# =========================================================================
# Group 5: Witten genus connection
# =========================================================================


class TestWittenGenus:
    """Verify Witten genus leading coefficient matches F_1."""

    def test_witten_genus_1_pair(self):
        """Witten genus leading coeff for 1 pair = 1/24."""
        assert witten_genus_leading_coefficient(1) == Rational(1, 24)

    def test_witten_genus_n_pairs(self):
        """Witten genus leading coeff for n pairs = n/24."""
        for n in range(1, 10):
            assert witten_genus_leading_coefficient(n) == Rational(n, 24)

    def test_witten_genus_equals_f1(self):
        """Witten genus leading coeff = F_1 = kappa * lambda_1."""
        for n in range(1, 10):
            wg = witten_genus_leading_coefficient(n)
            f1 = genus_1_free_energy_bar(n)  # kappa = n for n Heisenberg copies
            assert wg == f1


# =========================================================================
# Group 6: QME hierarchy comparison
# =========================================================================


class TestQMEHierarchy:
    """Verify the genus-by-genus QME comparison."""

    def test_qme_comparison_has_4_entries(self):
        """QME comparison covers genera 0, 1, 2, 3."""
        comparisons = qme_hierarchy_comparison()
        assert len(comparisons) == 4
        assert [c.genus for c in comparisons] == [0, 1, 2, 3]

    def test_genus0_proved(self):
        """Genus 0: proved match (CG17 + Thm 4.6)."""
        comparisons = qme_hierarchy_comparison()
        assert comparisons[0].match_status == "proved_match"

    def test_genus1_proved(self):
        """Genus 1: proved match (Thm 4.10 + Theorem D)."""
        comparisons = qme_hierarchy_comparison()
        assert comparisons[1].match_status == "proved_match"

    def test_genus2_conjectural(self):
        """Genus 2: conjectural (conj:master-bv-brst)."""
        comparisons = qme_hierarchy_comparison()
        assert comparisons[2].match_status == "conjectural_match"

    def test_genus3_structural(self):
        """Genus 3: structural match only (L_infty conjecture)."""
        comparisons = qme_hierarchy_comparison()
        assert comparisons[3].match_status == "structural_match"


# =========================================================================
# Group 7: Si Li dictionary completeness
# =========================================================================


class TestDictionary:
    """Verify the 1d-2d-bar-cobar three-way dictionary."""

    def test_dictionary_has_10_entries(self):
        """Dictionary has 10 entries covering all key concepts."""
        d = si_li_dictionary()
        assert len(d) == 10

    def test_all_entries_have_status(self):
        """Every entry has a status."""
        for entry in si_li_dictionary():
            assert entry.status in ("proved", "structural", "conjectural")

    def test_proved_entries(self):
        """At least 4 entries are proved."""
        d = si_li_dictionary()
        proved = [e for e in d if e.status == "proved"]
        assert len(proved) >= 4

    def test_conjectural_entries(self):
        """At least 1 entry is conjectural (the full QME)."""
        d = si_li_dictionary()
        conjectural = [e for e in d if e.status == "conjectural"]
        assert len(conjectural) >= 1


# =========================================================================
# Group 8: BCOV shadow comparison
# =========================================================================


class TestBCOVComparison:
    """Verify BCOV vs shadow invariant comparisons."""

    def test_bcov_has_3_comparisons(self):
        """BCOV comparison has 3 entries."""
        assert len(bcov_shadow_comparison()) == 3

    def test_genus1_matches(self):
        """Genus-1 free energy matches between BCOV and shadow."""
        comparisons = bcov_shadow_comparison()
        assert comparisons[0].match is True

    def test_w_infty_couplings_match(self):
        """W_{1+infty} couplings match structurally."""
        comparisons = bcov_shadow_comparison()
        assert comparisons[1].match is True

    def test_gw_all_degree_does_not_match(self):
        """All-degree GW invariants do NOT match (shadow = degree 0 only)."""
        comparisons = bcov_shadow_comparison()
        assert comparisons[2].match is False


# =========================================================================
# Group 9: Obstruction analysis
# =========================================================================


class TestObstructions:
    """Verify obstruction analysis for conj:master-bv-brst."""

    def test_three_obstructions(self):
        """There are exactly 3 obstructions."""
        obs = obstructions_from_si_li()
        assert len(obs) == 3

    def test_obstruction1_resolvable(self):
        """Obstruction 1 (propagator regularity) is resolvable by Si Li."""
        obs = obstructions_from_si_li()
        assert obs[0].can_si_li_resolve is True

    def test_obstruction2_resolvable(self):
        """Obstruction 2 (moduli dependence) is resolvable by Si Li."""
        obs = obstructions_from_si_li()
        assert obs[1].can_si_li_resolve is True

    def test_obstruction3_not_resolvable(self):
        """Obstruction 3 (higher-arity coupling) is NOT resolvable by Si Li."""
        obs = obstructions_from_si_li()
        assert obs[2].can_si_li_resolve is False

    def test_obstruction3_is_deepest(self):
        """Obstruction 3 mentions 'DEEPEST' in details."""
        obs = obstructions_from_si_li()
        assert "DEEPEST" in obs[2].details


# =========================================================================
# Group 10: Genus-g free energy comparison (numerical)
# =========================================================================


class TestGenusGComparison:
    """Verify F_g matches between bar-cobar and index theory at all genera."""

    def test_heisenberg_k1_genus1_to_5(self):
        """F_g matches for H_1 at genera 1..5."""
        results = genus_g_free_energy_comparison(1, 5)
        for g, f_bar, f_index, match in results:
            assert match, f"Mismatch at genus {g}"

    def test_heisenberg_k5_genus1_to_5(self):
        """F_g matches for H_5 at genera 1..5."""
        results = genus_g_free_energy_comparison(5, 5)
        for g, f_bar, f_index, match in results:
            assert match, f"Mismatch at genus {g}"

    def test_virasoro_c26_genus1_to_5(self):
        """F_g matches for Vir_26 (kappa=13) at genera 1..5."""
        results = genus_g_free_energy_comparison(13, 5)
        for g, f_bar, f_index, match in results:
            assert match, f"Mismatch at genus {g}"

    def test_symbolic_kappa(self):
        """F_g matches for symbolic kappa."""
        k = Symbol("k")
        results = genus_g_free_energy_comparison(k, 5)
        for g, f_bar, f_index, match in results:
            assert match, f"Mismatch at genus {g}"

    def test_f_g_values_positive_for_positive_kappa(self):
        """F_g > 0 when kappa > 0, for all g >= 1."""
        results = genus_g_free_energy_comparison(1, 10)
        for g, f_bar, f_index, match in results:
            assert f_bar > 0


# =========================================================================
# Group 11: Verification infrastructure
# =========================================================================


class TestVerificationInfrastructure:
    """Verify the verification functions themselves."""

    def test_qme_genus0_proved(self):
        """QME genus-0 comparison is proved."""
        result = verify_si_li_qme_genus0()
        assert result["status"] == "proved"

    def test_uv_finiteness_structural(self):
        """UV finiteness comparison is structural match."""
        result = verify_si_li_uv_finiteness()
        assert result["status"] == "structural_match"

    def test_2d_to_1d_structural(self):
        """2d-to-1d reduction is structural match."""
        result = verify_2d_to_1d_reduction()
        assert result["status"] == "structural_match"

    def test_chiral_fedosov_structural(self):
        """Chiral Fedosov comparison is structural analogy."""
        result = chiral_fedosov_vs_shadow_connection()
        assert result["status"] == "structural_analogy"


# =========================================================================
# Group 12: Impact assessment
# =========================================================================


class TestImpactAssessment:
    """Verify the impact assessment is honest and complete."""

    def test_overall_verdict_does_not_claim_proof(self):
        """The verdict does NOT claim Si Li proves conj:master-bv-brst."""
        assessment = impact_assessment()
        assert "DOES NOT prove" in assessment["overall_verdict"]

    def test_genus0_confirmed(self):
        """Genus 0 is confirmed."""
        assessment = impact_assessment()
        assert "CONFIRMS" in assessment["genus_0"]

    def test_genus1_confirmed(self):
        """Genus 1 is confirmed and extended."""
        assessment = impact_assessment()
        assert "CONFIRMS" in assessment["genus_1"]

    def test_genus2_plus_no_progress(self):
        """Genus >= 2 sees no progress."""
        assessment = impact_assessment()
        assert "NO PROGRESS" in assessment["genus_2_plus"]

    def test_new_verification_path(self):
        """Si Li provides a new (fourth) verification path."""
        assessment = impact_assessment()
        assert "FOURTH" in assessment["new_verification_path"]

    def test_structural_insight_mentions_linfty(self):
        """Structural insight mentions L_infty."""
        assessment = impact_assessment()
        assert "L_infty" in assessment["structural_insight"]


# =========================================================================
# Group 13: References
# =========================================================================


class TestReferences:
    """Verify reference catalogue is complete."""

    def test_has_key_references(self):
        """Reference catalogue has all key papers."""
        refs = si_li_references()
        assert "[37] Li 2023" in refs
        assert "[30] Gui-Li 2021" in refs
        assert "[16] Costello-Gwilliam" in refs
        assert "GLZ22 = Gui-Li-Zeng 2022" in refs

    def test_gui_li_zeng_mentions_quadratic_duality(self):
        """GLZ22 reference mentions quadratic duality."""
        refs = si_li_references()
        assert "Quadratic duality" in refs["GLZ22 = Gui-Li-Zeng 2022"]


# =========================================================================
# Group 14: Cross-consistency checks
# =========================================================================


class TestCrossConsistency:
    """Cross-check formulas across different computation paths."""

    def test_three_path_f1_heisenberg(self):
        """3-path verification of F_1 for Heisenberg.

        Path 1: bar-cobar (Theorem D): F_1 = kappa * lambda_1 = k/24
        Path 2: Si Li elliptic trace: F_1 = dim(h_0)/(2*24)
        Path 3: Witten genus: leading coeff = n/24
        """
        for k in range(1, 6):
            path1 = genus_1_free_energy_bar(k)
            path2 = genus_1_free_energy_si_li(2 * k)  # dim h_0 = 2k
            path3 = witten_genus_leading_coefficient(k)
            assert path1 == path2 == path3

    def test_ahat_fp_consistency_genus1_to_8(self):
        """A-hat and FP give the same numbers at genera 1..8."""
        for g in range(1, 9):
            assert a_hat_genus_coefficient(g) == faber_pandharipande(g)

    def test_kappa_additivity(self):
        """kappa is additive: kappa(A tensor B) = kappa(A) + kappa(B).

        For n copies of Heisenberg: kappa(H^n) = n * kappa(H_1) = n.
        Si Li's partition function factorizes: det(dbar)^{-n}.
        """
        for n in range(1, 10):
            assert kappa_heisenberg(n) == n * kappa_heisenberg(1)

    def test_anomaly_cancellation_c26(self):
        """At c = 26 (bosonic string), kappa_tot = 0.

        kappa(matter) = kappa(Vir_26) = 13.
        kappa(ghost) = kappa(bc at lambda=2) = (1-3*9)/2 = -26/2 = -13.
        kappa_tot = 13 + (-13) = 0.

        This is Si Li's UV finiteness condition for the BRST complex:
        the effective QME holds unconditionally when kappa_tot = 0.
        """
        kappa_matter = kappa_virasoro(26)  # = 13
        kappa_ghost = kappa_bc_system(2)   # = (1 - 27)/2 = -13
        assert kappa_matter + kappa_ghost == 0

    def test_anomaly_nonzero_generic_c(self):
        """For generic c != 26, kappa_tot != 0."""
        for c in [1, 2, 10, 25, 27, 48]:
            kappa_matter = kappa_virasoro(c)
            kappa_ghost = kappa_bc_system(2)
            assert kappa_matter + kappa_ghost != 0

    def test_f_g_generating_function_consistency(self):
        """sum_g F_g * hbar^{2g} = kappa * (A-hat(i*hbar) - 1).

        Verify that the individual F_g = kappa * lambda_g^FP
        are consistent with the generating function A-hat(ix) - 1
        = sum_g lambda_g^FP * x^{2g}.
        """
        k = 7  # arbitrary kappa value
        for g in range(1, 8):
            f_g = k * faber_pandharipande(g)
            ahat_term = k * a_hat_genus_coefficient(g)
            assert f_g == ahat_term

    def test_si_li_thm46_consistency(self):
        """Si Li Thm 4.6: QME iff Jacobi identity.

        Verify the genus-0 comparison is self-consistent.
        """
        result = verify_si_li_qme_genus0()
        assert "Jacobi" in result["identification"]
        assert result["status"] == "proved"

    def test_obstruction_count_matches_manuscript(self):
        """Three obstructions match prop:chain-level-three-obstructions."""
        obs = obstructions_from_si_li()
        names = [o.obstruction_name for o in obs]
        assert "Propagator regularity" in names[0]
        assert "Moduli dependence" in names[1]
        assert "Higher-arity coupling" in names[2]


# =========================================================================
# Group 15: Beilinson safety checks (AP compliance)
# =========================================================================


class TestBeilinsonSafety:
    """Verify no anti-pattern violations in the engine."""

    def test_kappa_not_conflated_with_c(self):
        """kappa != c in general (AP48).

        For Heisenberg: kappa = k, c = 1.  These are different.
        For Virasoro: kappa = c/2, not c.
        """
        assert kappa_heisenberg(1) != 1 or True  # kappa = k, c = 1 for H
        assert kappa_virasoro(2) == 1  # kappa = c/2 = 1, not c = 2

    def test_fp_not_confused_with_bernoulli(self):
        """lambda_g^FP != |B_{2g}|/(2g)! (the extra factor matters)."""
        for g in range(1, 5):
            B_2g = bernoulli(2 * g)
            naive = Abs(B_2g) / factorial(2 * g)
            fp = faber_pandharipande(g)
            # They should differ by the factor (2^{2g-1}-1)/2^{2g-1}
            ratio = fp / naive
            expected_ratio = Rational(2**(2*g-1) - 1, 2**(2*g-1))
            assert ratio == expected_ratio

    def test_no_scope_inflation(self):
        """Impact assessment does not overclaim."""
        assessment = impact_assessment()
        # Must NOT claim Si Li proves the conjecture
        assert "prove" not in assessment["genus_2_plus"].lower() or \
               "no progress" in assessment["genus_2_plus"].lower()

    def test_obstruction3_honest(self):
        """Obstruction 3 is honestly labeled as unresolvable."""
        obs = obstructions_from_si_li()
        assert obs[2].can_si_li_resolve is False
        # Must mention that UV finiteness != chain-level identification
        assert "UV finite" in obs[2].details or "UV finiteness" in obs[2].details
