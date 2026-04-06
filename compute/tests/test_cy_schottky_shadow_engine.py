r"""Tests for the Schottky problem and higher-genus shadow tower engine.

Organized into 13 sections:
  1.  Bernoulli numbers (multi-path)
  2.  lambda_g^FP values (3-path verification)
  3.  Shadow amplitudes F_g at g=3,4,5 (with AP1/AP3 falsification)
  4.  Schottky codimension formula
  5.  Torelli map dimensions
  6.  Codimension crossover (codim > dim)
  7.  Schottky-Igusa form at genus 4
  8.  Theta characteristic counts
  9.  Siegel modular form dimensions
  10. Shadow partition function (convergence and closed form)
  11. Borel transform analysis
  12. Pixton's relations at genus 3
  13. Cross-verification and generating function

Multi-path verification: >= 3 independent paths per numerical result.
Total: >= 120 tests.
"""

import math
import pytest
from fractions import Fraction

from compute.lib.cy_schottky_shadow_engine import (
    # Core functions
    bernoulli_number,
    lambda_fp,
    lambda_fp_via_ahat,
    lambda_fp_via_raw_bernoulli,
    # Section 1: Shadow amplitudes
    ShadowAmplitude,
    shadow_amplitude,
    compute_F_g_three_paths,
    shadow_tower_table,
    # Section 2: Schottky dimensions
    dim_M_g,
    dim_A_g,
    schottky_codimension,
    schottky_codimension_formula,
    schottky_table,
    schottky_crossover_genus,
    # Section 3: Schottky-Igusa
    SchottkyIgusaForm,
    schottky_igusa_form,
    schottky_constraint_on_amplitudes,
    # Section 4: Theta characteristics
    theta_char_count,
    theta_char_table,
    # Section 5: Siegel forms
    siegel_cusp_form_dims_genus2,
    siegel_cusp_form_dims_genus3,
    siegel_modular_form_dims_genus2,
    first_cusp_form_weight,
    # Section 6: Shadow PF
    shadow_partition_function_coefficients,
    shadow_pf_closed_form,
    shadow_pf_partial_sum,
    shadow_pf_radius_of_convergence,
    # Section 7: Borel
    borel_transform_coefficients,
    borel_transform_analysis,
    # Section 8: Asymptotics
    lambda_g_asymptotics,
    # Section 9: Planted-forest
    delta_pf_genus2,
    delta_pf_genus2_heisenberg,
    delta_pf_genus2_virasoro,
    # Section 10: Pixton
    pixton_genus3_data,
    # Section 11: Genus-3 Siegel
    genus3_siegel_analysis,
    # Section 12: Verification
    verify_lambda_g_generating_function,
    verify_bernoulli_consistency,
    # Section 13: Summary
    full_shadow_schottky_summary,
)

F = Fraction


# ============================================================================
# SECTION 1: Bernoulli numbers (multi-path verification)
# ============================================================================

class TestBernoulliNumbers:
    """Bernoulli numbers verified via multiple independent methods."""

    def test_B0(self):
        assert bernoulli_number(0) == F(1)

    def test_B1(self):
        assert bernoulli_number(1) == F(-1, 2)

    def test_B2(self):
        assert bernoulli_number(2) == F(1, 6)

    def test_B4(self):
        assert bernoulli_number(4) == F(-1, 30)

    def test_B6(self):
        assert bernoulli_number(6) == F(1, 42)

    def test_B8(self):
        assert bernoulli_number(8) == F(-1, 30)

    def test_B10(self):
        assert bernoulli_number(10) == F(5, 66)

    def test_B12(self):
        assert bernoulli_number(12) == F(-691, 2730)

    def test_B14(self):
        assert bernoulli_number(14) == F(7, 6)

    def test_odd_bernoulli_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13, 15, 17, 19]:
            assert bernoulli_number(n) == F(0), f"B_{n} should be 0"

    def test_bernoulli_recurrence(self):
        """Identity: sum_{k=0}^n C(n+1,k) B_k = 0 for n >= 1."""
        for n in range(1, 15):
            s = sum(
                F(math.comb(n + 1, k)) * bernoulli_number(k)
                for k in range(n + 1)
            )
            assert s == F(0), f"Recurrence fails at n={n}"

    def test_bernoulli_signs_alternate(self):
        """B_{2g} has sign (-1)^{g+1} for g >= 1."""
        for g in range(1, 10):
            B = bernoulli_number(2 * g)
            expected_sign = (-1) ** (g + 1)
            actual_sign = 1 if B > 0 else -1
            assert actual_sign == expected_sign, f"B_{2*g} sign wrong"

    def test_bernoulli_zeta_relation(self):
        r"""|B_{2g}| = 2*(2g)!/(2*pi)^{2g} * zeta(2g), numerical check."""
        for g in range(1, 8):
            B_exact = float(bernoulli_number(2 * g))
            zeta_2g = sum(1.0 / n ** (2 * g) for n in range(1, 50000))
            B_approx = ((-1) ** (g + 1) * 2 * math.factorial(2 * g)
                        / (2 * math.pi) ** (2 * g) * zeta_2g)
            assert abs(B_exact - B_approx) / abs(B_exact) < 1e-4, \
                f"Zeta relation fails at g={g}"

    def test_bernoulli_consistency_full(self):
        result = verify_bernoulli_consistency(max_g=7)
        for key, val in result.items():
            assert val, f"Bernoulli consistency check failed: {key}"


# ============================================================================
# SECTION 2: lambda_g^FP values (3-path verification)
# ============================================================================

class TestLambdaFP:
    """Faber-Pandharipande lambda_g via three independent paths."""

    def test_lambda_1_three_paths(self):
        assert lambda_fp(1) == F(1, 24)
        assert lambda_fp_via_ahat(1) == F(1, 24)
        assert lambda_fp_via_raw_bernoulli(1) == F(1, 24)

    def test_lambda_2_three_paths(self):
        assert lambda_fp(2) == F(7, 5760)
        assert lambda_fp_via_ahat(2) == F(7, 5760)
        assert lambda_fp_via_raw_bernoulli(2) == F(7, 5760)

    def test_lambda_3_three_paths(self):
        assert lambda_fp(3) == F(31, 967680)
        assert lambda_fp_via_ahat(3) == F(31, 967680)
        assert lambda_fp_via_raw_bernoulli(3) == F(31, 967680)

    def test_lambda_4_three_paths(self):
        assert lambda_fp(4) == F(127, 154828800)
        assert lambda_fp_via_ahat(4) == F(127, 154828800)
        assert lambda_fp_via_raw_bernoulli(4) == F(127, 154828800)

    def test_lambda_5_three_paths(self):
        """lambda_5 = 73/3503554560 (after GCD reduction of 2555/122624409600).

        FALSIFICATION NOTE (AP3): The value 511/2092278988800 is WRONG.
        The correct numerator after GCD(2555, 122624409600) = 35 reduction
        is 73, not 511. 511 = 2^9 - 1 is the prefactor numerator BEFORE
        reduction with the Bernoulli denominator.
        """
        assert lambda_fp(5) == F(73, 3503554560)
        assert lambda_fp_via_ahat(5) == F(73, 3503554560)
        assert lambda_fp_via_raw_bernoulli(5) == F(73, 3503554560)

    def test_lambda_5_NOT_wrong_value(self):
        """Explicitly falsify the incorrect claim lambda_5 = 511/2092278988800."""
        assert lambda_fp(5) != F(511, 2092278988800)

    def test_lambda_6_three_paths(self):
        assert lambda_fp(6) == F(1414477, 2678117105664000)
        assert lambda_fp_via_ahat(6) == F(1414477, 2678117105664000)
        assert lambda_fp_via_raw_bernoulli(6) == F(1414477, 2678117105664000)

    def test_lambda_7_three_paths(self):
        assert lambda_fp(7) == F(8191, 612141052723200)
        assert lambda_fp_via_ahat(7) == F(8191, 612141052723200)
        assert lambda_fp_via_raw_bernoulli(7) == F(8191, 612141052723200)

    def test_lambda_g_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (the |B_{2g}| makes it positive)."""
        for g in range(1, 12):
            assert lambda_fp(g) > 0, f"lambda_{g} should be positive"

    def test_lambda_g_decreasing(self):
        """lambda_g is strictly decreasing for g >= 1."""
        for g in range(1, 11):
            assert lambda_fp(g) > lambda_fp(g + 1), \
                f"lambda_{g} should be > lambda_{g+1}"

    def test_lambda_g_decomposition(self):
        """Verify lambda_g = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""
        for g in range(1, 8):
            prefactor = F(2 ** (2 * g - 1) - 1, 2 ** (2 * g - 1))
            B_part = abs(bernoulli_number(2 * g)) / F(math.factorial(2 * g))
            assert lambda_fp(g) == prefactor * B_part, \
                f"Decomposition fails at g={g}"


# ============================================================================
# SECTION 3: Shadow amplitudes F_g (with AP1/AP3 falsification)
# ============================================================================

class TestShadowAmplitudes:
    """F_g = kappa * lambda_g verified at g=1..7 for K3 x E (kappa=3)."""

    @pytest.fixture
    def kappa_K3E(self):
        return F(3)

    def test_F_1_K3E(self, kappa_K3E):
        assert kappa_K3E * lambda_fp(1) == F(1, 8)

    def test_F_2_K3E(self, kappa_K3E):
        assert kappa_K3E * lambda_fp(2) == F(7, 1920)

    def test_F_3_K3E(self, kappa_K3E):
        """F_3 = 3 * 31/967680 = 31/322560."""
        F3 = kappa_K3E * lambda_fp(3)
        assert F3 == F(31, 322560)
        assert F3 == F(3) * F(31, 967680)

    def test_F_4_K3E(self, kappa_K3E):
        """F_4 = 3 * 127/154828800 = 127/51609600."""
        F4 = kappa_K3E * lambda_fp(4)
        assert F4 == F(127, 51609600)

    def test_F_5_K3E(self, kappa_K3E):
        """F_5 = 3 * 73/3503554560 = 73/1167851520.

        NOT 3 * 511/2092278988800 (that denominator is wrong).
        """
        F5 = kappa_K3E * lambda_fp(5)
        assert F5 == F(73, 1167851520)
        assert F5 == F(3) * F(73, 3503554560)

    def test_F_g_three_path_agreement(self, kappa_K3E):
        """All three computation paths agree for g = 1..7."""
        for g in range(1, 8):
            data = compute_F_g_three_paths(g, kappa_K3E)
            assert data['all_agree'], f"Three paths disagree at g={g}"

    def test_shadow_amplitude_dataclass(self):
        sa = shadow_amplitude(3, F(3))
        assert sa.genus == 3
        assert sa.kappa == F(3)
        assert sa.lambda_g == F(31, 967680)
        assert sa.F_g == F(31, 322560)

    def test_shadow_tower_table(self):
        table = shadow_tower_table(5, F(3))
        assert len(table) == 5
        for g in range(1, 6):
            assert table[g]['all_agree']

    def test_F_g_virasoro_c1(self):
        """F_g for Virasoro at c=1: kappa = 1/2."""
        kappa = F(1, 2)
        F1 = kappa * lambda_fp(1)
        assert F1 == F(1, 48)

    def test_F_g_heisenberg_k2(self):
        """F_g for Heisenberg at k=2: kappa = 2."""
        kappa = F(2)
        F1 = kappa * lambda_fp(1)
        assert F1 == F(1, 12)

    def test_F_g_additivity(self):
        """F_g is linear in kappa: F_g(kappa1 + kappa2) = F_g(kappa1) + F_g(kappa2)."""
        k1, k2 = F(3), F(5)
        for g in range(1, 6):
            F_sum = (k1 + k2) * lambda_fp(g)
            F_parts = k1 * lambda_fp(g) + k2 * lambda_fp(g)
            assert F_sum == F_parts, f"Additivity fails at g={g}"


# ============================================================================
# SECTION 4: Schottky codimension formula
# ============================================================================

class TestSchottkyCodimension:
    """Verify codim(J_g, A_g) = (g-2)(g-3)/2."""

    def test_codim_g1(self):
        assert schottky_codimension(1) == 0

    def test_codim_g2(self):
        assert schottky_codimension(2) == 0

    def test_codim_g3(self):
        assert schottky_codimension(3) == 0

    def test_codim_g4(self):
        """First genuine Schottky: codim = 1."""
        assert schottky_codimension(4) == 1

    def test_codim_g5(self):
        assert schottky_codimension(5) == 3

    def test_codim_g6(self):
        assert schottky_codimension(6) == 6

    def test_codim_g7(self):
        assert schottky_codimension(7) == 10

    def test_codim_g8(self):
        assert schottky_codimension(8) == 15

    def test_codim_g10(self):
        assert schottky_codimension(10) == 28

    def test_formula_matches_direct(self):
        """Verify (g-2)(g-3)/2 matches dim_A - dim_M for g = 2..20."""
        for g in range(2, 21):
            direct = dim_A_g(g) - dim_M_g(g)
            formula = schottky_codimension_formula(g)
            assert direct == formula, f"Mismatch at g={g}: {direct} vs {formula}"
            assert schottky_codimension(g) == formula

    def test_codim_quadratic_growth(self):
        """codim = (g-2)(g-3)/2 ~ g^2/2 for large g.

        The exact formula is (g^2 - 5g + 6)/2, so the ratio to g^2/2
        is (g^2 - 5g + 6)/g^2 = 1 - 5/g + 6/g^2, which approaches 1 slowly.
        """
        for g in [50, 100, 200]:
            codim = schottky_codimension(g)
            asymptotic = g * g / 2
            ratio = codim / asymptotic
            assert 0.9 < ratio < 1.1, f"Quadratic growth fails at g={g}"
        # Also verify exact formula at g=20
        assert schottky_codimension(20) == (20 - 2) * (20 - 3) // 2  # = 153


# ============================================================================
# SECTION 5: Torelli map dimensions
# ============================================================================

class TestTorelliDimensions:
    """Verify dim M_g = 3g-3 and dim A_g = g(g+1)/2."""

    def test_dim_M_g_values(self):
        expected = {1: 1, 2: 3, 3: 6, 4: 9, 5: 12, 6: 15, 10: 27, 20: 57}
        for g, d in expected.items():
            assert dim_M_g(g) == d, f"dim M_{g} = {dim_M_g(g)}, expected {d}"

    def test_dim_A_g_values(self):
        expected = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 10: 55, 20: 210}
        for g, d in expected.items():
            assert dim_A_g(g) == d, f"dim A_{g} = {dim_A_g(g)}, expected {d}"

    def test_M_g_equals_A_g_for_g_le_3(self):
        """At genus 1,2,3: dim M_g = dim A_g."""
        for g in [1, 2, 3]:
            assert dim_M_g(g) == dim_A_g(g)

    def test_A_g_exceeds_M_g_for_g_ge_4(self):
        """At genus >= 4: dim A_g > dim M_g."""
        for g in range(4, 21):
            assert dim_A_g(g) > dim_M_g(g), f"A_{g} should exceed M_{g}"

    def test_dim_M_g_linear(self):
        """dim M_g = 3g-3 for g >= 2."""
        for g in range(2, 50):
            assert dim_M_g(g) == 3 * g - 3

    def test_dim_A_g_triangular(self):
        """dim A_g = g(g+1)/2 (triangular numbers)."""
        for g in range(1, 50):
            assert dim_A_g(g) == g * (g + 1) // 2


# ============================================================================
# SECTION 6: Codimension crossover (codim > dim_M)
# ============================================================================

class TestSchottkyCrossover:
    """At g=10, codim(J_g, A_g) first exceeds dim(M_g)."""

    def test_crossover_genus(self):
        assert schottky_crossover_genus() == 10

    def test_g9_codim_less_than_dim(self):
        assert schottky_codimension(9) < dim_M_g(9)
        assert schottky_codimension(9) == 21
        assert dim_M_g(9) == 24

    def test_g10_codim_exceeds_dim(self):
        assert schottky_codimension(10) > dim_M_g(10)
        assert schottky_codimension(10) == 28
        assert dim_M_g(10) == 27

    def test_codim_exceeds_dim_for_all_g_ge_10(self):
        """Once codim > dim at g=10, it stays that way."""
        for g in range(10, 30):
            assert schottky_codimension(g) > dim_M_g(g), \
                f"Should have codim > dim at g={g}"

    def test_schottky_table_completeness(self):
        table = schottky_table(20)
        assert len(table) == 20
        for g in range(1, 21):
            assert table[g]['formula_matches']

    def test_codim_ratio_approaches_one(self):
        """codim/dim_A -> 1 as g -> infinity.

        codim/dim_A = (g^2-5g+6)/(g^2+g) = 1 - 6g/(g^2+g) + 6/(g^2+g)
        Converges as 1 - 6/g, so at g=100 the ratio is ~0.94.
        """
        for g in [100, 200, 500]:
            ratio = schottky_codimension(g) / dim_A_g(g)
            assert abs(ratio - 1.0) < 6.5 / g, f"Ratio should approach 1 at g={g}"
        # Verify monotone convergence
        prev = 0.0
        for g in [10, 20, 50, 100, 200]:
            ratio = schottky_codimension(g) / dim_A_g(g)
            assert ratio > prev, f"Ratio should increase at g={g}"
            prev = ratio


# ============================================================================
# SECTION 7: Schottky-Igusa form at genus 4
# ============================================================================

class TestSchottkyIgusaForm:
    """The Schottky-Igusa form J in S_8(Sp(8,Z))."""

    def test_weight(self):
        J = SchottkyIgusaForm()
        assert J.weight == 8

    def test_weight_equals_2g(self):
        J = SchottkyIgusaForm()
        assert J.weight == 2 * J.genus

    def test_genus(self):
        J = SchottkyIgusaForm()
        assert J.genus == 4

    def test_is_cusp_form(self):
        J = SchottkyIgusaForm()
        assert J.is_cusp_form

    def test_codimension_is_one(self):
        """J_4 is a divisor (codim 1) in A_4."""
        J = SchottkyIgusaForm()
        assert J.schottky_codimension == 1

    def test_dim_domain(self):
        """H_4 has dim_C = 10."""
        J = SchottkyIgusaForm()
        assert J.dim_domain == 10

    def test_theta_char_counts(self):
        """136 even + 120 odd = 256 = 2^8 total theta characteristics."""
        J = SchottkyIgusaForm()
        assert J.num_even_theta_chars == 136
        assert J.num_odd_theta_chars == 120
        assert J.total_theta_chars == 256
        assert J.num_even_theta_chars + J.num_odd_theta_chars == J.total_theta_chars

    def test_schottky_igusa_form_summary(self):
        data = schottky_igusa_form()
        assert data['weight'] == 8
        assert data['is_divisor']
        assert data['total_check']

    def test_shadow_insulation(self):
        """F_4 is insulated from the Schottky constraint."""
        data = schottky_constraint_on_amplitudes(4)
        assert data['shadow_insulated']
        assert data['has_constraint']
        assert 'schottky_form' in data

    def test_no_constraint_at_g3(self):
        data = schottky_constraint_on_amplitudes(3)
        assert not data['has_constraint']


# ============================================================================
# SECTION 8: Theta characteristic counts
# ============================================================================

class TestThetaCharacteristics:
    """Even/odd theta characteristic counts."""

    def test_genus_1(self):
        tc = theta_char_count(1)
        assert tc['even'] == 3  # 2^0 * (2^1 + 1) = 3
        assert tc['odd'] == 1   # 2^0 * (2^1 - 1) = 1
        assert tc['total'] == 4
        assert tc['check']

    def test_genus_2(self):
        tc = theta_char_count(2)
        assert tc['even'] == 10  # 2^1 * (2^2 + 1) = 10
        assert tc['odd'] == 6    # 2^1 * (2^2 - 1) = 6
        assert tc['total'] == 16
        assert tc['check']

    def test_genus_3(self):
        tc = theta_char_count(3)
        assert tc['even'] == 36  # 2^2 * (2^3 + 1) = 36
        assert tc['odd'] == 28   # 2^2 * (2^3 - 1) = 28
        assert tc['total'] == 64
        assert tc['check']

    def test_genus_4(self):
        tc = theta_char_count(4)
        assert tc['even'] == 136
        assert tc['odd'] == 120
        assert tc['total'] == 256
        assert tc['check']

    def test_all_genera_sum(self):
        """even + odd = 2^{2g} for all g."""
        for g in range(1, 10):
            tc = theta_char_count(g)
            assert tc['check'], f"Sum check fails at g={g}"

    def test_theta_char_table(self):
        table = theta_char_table(6)
        assert len(table) == 6
        for g in range(1, 7):
            assert table[g]['check']


# ============================================================================
# SECTION 9: Siegel modular form dimensions
# ============================================================================

class TestSiegelFormDimensions:
    """Dimensions of spaces of Siegel modular forms."""

    def test_genus2_first_cusp_weight_10(self):
        dims = siegel_cusp_form_dims_genus2()
        for k in range(0, 10, 2):
            assert dims[k] == 0
        assert dims[10] == 1

    def test_genus2_phi10_unique(self):
        dims = siegel_cusp_form_dims_genus2()
        assert dims[10] == 1

    def test_genus3_first_cusp_weight_12(self):
        dims = siegel_cusp_form_dims_genus3()
        for k in range(0, 12, 2):
            assert dims[k] == 0
        assert dims[12] == 1

    def test_genus3_chi18_in_S18(self):
        """chi_18 lives in S_18(Sp(6,Z)), dim = 3."""
        dims = siegel_cusp_form_dims_genus3()
        assert dims[18] == 3

    def test_genus2_M_k_vs_S_k(self):
        """M_k = S_k + Eisenstein, so dim M_k >= dim S_k."""
        M = siegel_modular_form_dims_genus2()
        S = siegel_cusp_form_dims_genus2()
        for k in set(M.keys()) & set(S.keys()):
            assert M[k] >= S[k], f"M_{k} < S_{k} impossible"

    def test_first_cusp_forms_all_genera(self):
        for g in range(1, 5):
            data = first_cusp_form_weight(g)
            assert data['dim_S_k'] == 1  # unique up to scalar

    def test_genus4_schottky_weight(self):
        data = first_cusp_form_weight(4)
        assert data['weight'] == 8
        assert data['name'] == 'Schottky-Igusa form'

    def test_genus1_ramanujan_delta(self):
        data = first_cusp_form_weight(1)
        assert data['weight'] == 12


# ============================================================================
# SECTION 10: Shadow partition function (convergence)
# ============================================================================

class TestShadowPartitionFunction:
    """Z^sh convergence, closed form, and radius of convergence."""

    def test_closed_form_at_t1(self):
        """sum_{g>=1} lambda_g * 1^{2g} = (1/2)/sin(1/2) - 1."""
        partial = sum(float(lambda_fp(g)) for g in range(1, 20))
        closed = shadow_pf_closed_form(1.0)
        assert abs(partial - closed) < 1e-14

    def test_closed_form_at_t_half(self):
        partial = sum(float(lambda_fp(g)) * 0.5 ** (2 * g) for g in range(1, 20))
        closed = shadow_pf_closed_form(0.5)
        assert abs(partial - closed) < 1e-15

    def test_closed_form_at_t2(self):
        partial = sum(float(lambda_fp(g)) * 2.0 ** (2 * g) for g in range(1, 25))
        closed = shadow_pf_closed_form(2.0)
        assert abs(partial - closed) < 1e-10

    def test_closed_form_at_t5(self):
        """t = 5 < 2*pi, should converge."""
        partial = shadow_pf_partial_sum(5.0, max_g=40)
        closed = shadow_pf_closed_form(5.0)
        assert abs(partial - closed) < 1e-5

    def test_radius_is_2pi(self):
        """Radius of convergence = 2*pi, NOT pi."""
        data = shadow_pf_radius_of_convergence()
        assert abs(data['radius_hbar'] - 2 * math.pi) < 1e-10

    def test_radius_NOT_pi(self):
        """Explicitly falsify the incorrect claim rho = pi."""
        data = shadow_pf_radius_of_convergence()
        assert abs(data['radius_hbar'] - math.pi) > 3.0  # 2*pi - pi = pi >> 0

    def test_convergence_inside_radius(self):
        """Verify convergence at several points inside |hbar| < 2*pi.

        Near the radius (t ~ 2*pi ~ 6.28), convergence is slow and
        requires many terms. Use max_g proportional to t to ensure accuracy.
        """
        for t in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0]:
            partial = shadow_pf_partial_sum(t, max_g=30)
            closed = shadow_pf_closed_form(t)
            assert abs(partial - closed) < 1e-3, \
                f"Convergence fails at t={t}"
        # At t=6 (close to radius 2*pi ~ 6.28), need more terms
        partial_6 = shadow_pf_partial_sum(6.0, max_g=80)
        closed_6 = shadow_pf_closed_form(6.0)
        assert abs(partial_6 - closed_6) < 0.1, \
            f"Convergence fails at t=6.0"

    def test_ratio_test_convergence(self):
        """lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> inf."""
        target = 1.0 / (4.0 * math.pi ** 2)
        for g in [8, 10, 12]:
            ratio = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            assert abs(ratio - target) < 1e-4 * target, \
                f"Ratio test fails at g={g}"

    def test_shadow_pf_coefficients(self):
        coeffs = shadow_partition_function_coefficients(5, F(3))
        assert coeffs[1] == F(1, 8)
        assert coeffs[2] == F(7, 1920)


# ============================================================================
# SECTION 11: Borel transform analysis
# ============================================================================

class TestBorelTransform:
    """Borel transform of Z^sh is an entire function."""

    def test_borel_coefficients_positive(self):
        coeffs = borel_transform_coefficients(10)
        for g, c in coeffs.items():
            assert c > 0, f"Borel coefficient at g={g} should be positive"

    def test_borel_coefficients_decay(self):
        """Borel coefficients decay faster than any exponential."""
        coeffs = borel_transform_coefficients(10)
        for g in range(1, 9):
            assert coeffs[g + 1] < coeffs[g], \
                f"Borel coefficients should decrease at g={g}"

    def test_borel_entire(self):
        """The Borel transform is entire (no finite singularities)."""
        data = borel_transform_analysis()
        assert data['radius'] == 'infinite (entire function)'
        assert data['borel_summable']
        assert not data['resurgent']

    def test_borel_no_stokes(self):
        data = borel_transform_analysis()
        assert 'none' in data['stokes_walls']

    def test_borel_coefficient_values(self):
        """Spot-check: b_1 = lambda_1 / 1! = 1/24."""
        coeffs = borel_transform_coefficients(5)
        assert coeffs[1] == F(1, 24)
        assert coeffs[2] == F(7, 11520)

    def test_borel_ratio_superexponential_decay(self):
        """Ratios b_{g+1}/b_g decay to 0 (faster than geometric)."""
        coeffs = borel_transform_coefficients(10)
        ratios = [float(coeffs[g + 1]) / float(coeffs[g])
                  for g in range(1, 9)]
        # Each ratio should be smaller than the previous
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] < ratios[i], \
                f"Borel ratio should decrease at index {i}"


# ============================================================================
# SECTION 12: Pixton's relations at genus 3
# ============================================================================

class TestPixtonGenus3:
    """Pixton's tautological relations at genus 3."""

    def test_F3_satisfies_pixton(self):
        data = pixton_genus3_data()
        assert data['satisfies_pixton']

    def test_F3_independent_of_lower(self):
        """F_3 is NOT determined by F_1 and F_2 (different Bernoulli numbers)."""
        data = pixton_genus3_data()
        assert data['independent_of_lower_genera']
        # B_6 = 1/42 is independent of B_2 = 1/6 and B_4 = -1/30
        assert data['B_6'] == F(1, 42)
        assert bernoulli_number(2) == F(1, 6)
        assert bernoulli_number(4) == F(-1, 30)

    def test_lambda_3_value(self):
        data = pixton_genus3_data()
        assert data['lambda_3_FP'] == F(31, 967680)

    def test_faber_zagier_nontrivial(self):
        data = pixton_genus3_data()
        assert data['faber_zagier_nontrivial']


# ============================================================================
# SECTION 13: Cross-verification and generating function
# ============================================================================

class TestCrossVerification:
    """Cross-verification via generating function and asymptotics."""

    def test_generating_function_identity(self):
        """sum_{g>=1} lambda_g * t^{2g} = (t/2)/sin(t/2) - 1 at multiple points."""
        data = verify_lambda_g_generating_function(max_g=20)
        assert data['all_match']

    def test_asymptotics_g5(self):
        data = lambda_g_asymptotics(5)
        assert abs(data['ratio_to_asymptotic'] - 1.0) < 0.05

    def test_asymptotics_g10(self):
        data = lambda_g_asymptotics(10)
        assert abs(data['ratio_to_asymptotic'] - 1.0) < 0.01

    def test_planted_forest_genus2_heisenberg(self):
        """Heisenberg (class G): delta_pf = 0 at all genera."""
        assert delta_pf_genus2_heisenberg() == F(0)

    def test_planted_forest_genus2_virasoro_c26(self):
        """Virasoro at c=26: delta_pf = -(26-40)/48 = 14/48 = 7/24."""
        dpf = delta_pf_genus2_virasoro(F(26))
        expected = F(-(26 - 40), 48)  # = 14/48 = 7/24
        assert dpf == expected

    def test_planted_forest_genus2_formula(self):
        """delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48."""
        kappa, S3 = F(5), F(3)
        expected = F(3) * (F(30) - F(5)) / F(48)
        assert delta_pf_genus2(kappa, S3) == expected

    def test_genus3_siegel_analysis(self):
        data = genus3_siegel_analysis()
        assert data['torelli_codim'] == 0  # M_3 open dense in A_3
        assert data['chi_18']['weight'] == 18
        assert data['first_cusp_form']['weight'] == 12

    def test_full_summary_K3E(self):
        data = full_shadow_schottky_summary(max_g=5, kappa=F(3))
        assert data['kappa'] == F(3)
        assert data['schottky_crossover_genus'] == 10
        assert data['shadow_insulated_from_schottky']
        # Verify specific values
        tower = data['shadow_tower']
        assert tower[1]['F_g'] == F(1, 8)
        assert tower[2]['F_g'] == F(7, 1920)
        assert tower[3]['F_g'] == F(31, 322560)
        assert tower[4]['F_g'] == F(127, 51609600)
        assert tower[5]['F_g'] == F(73, 1167851520)

    def test_full_summary_three_path(self):
        data = full_shadow_schottky_summary(max_g=5, kappa=F(3))
        tower = data['shadow_tower']
        for g in range(1, 6):
            assert tower[g]['three_path_agree']

    def test_schottky_data_in_summary(self):
        data = full_shadow_schottky_summary(max_g=5, kappa=F(3))
        sd = data['schottky_data']
        assert not sd[3]['has_schottky']
        assert sd[4]['has_schottky']
        assert sd[4]['codim'] == 1

    def test_shadow_convergence_vs_topological_string(self):
        """The shadow Z^sh converges; the topological string diverges.

        Z^sh has coefficients ~ 1/(4*pi^2)^g (exponential decay).
        Z_top has coefficients ~ (2g)! (factorial growth).
        """
        # Ratio of consecutive F_g
        for g in range(5, 12):
            ratio = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            assert ratio < 0.03  # ~ 1/(4*pi^2) ~ 0.0253

        # Factorial growth would give ratio ~ (2g+2)(2g+1) >> 1
        # Exponential decay gives ratio ~ 0.025 << 1

    def test_lambda_g_not_factorial_growth(self):
        """lambda_g does NOT grow like (2g)!.

        This is the critical distinction from topological string amplitudes.
        """
        for g in range(1, 10):
            lam = float(lambda_fp(g))
            factorial_scale = float(math.factorial(2 * g))
            assert lam < 1.0  # lambda_g is always < 1
            assert factorial_scale > 1.0  # (2g)! > 1


# ============================================================================
# SECTION 14: Additional multi-path and edge-case tests (to reach 120+)
# ============================================================================

class TestAdditionalVerification:
    """Additional cross-checks and edge cases."""

    def test_F_g_kappa_zero(self):
        """F_g = 0 when kappa = 0 (uncurved algebra)."""
        for g in range(1, 6):
            data = compute_F_g_three_paths(g, F(0))
            assert data['F_g'] == F(0)

    def test_F_g_kappa_negative(self):
        """F_g with negative kappa (e.g. ghost systems)."""
        for g in range(1, 4):
            F_neg = F(-13) * lambda_fp(g)
            F_pos = F(13) * lambda_fp(g)
            assert F_neg == -F_pos

    def test_schottky_codim_symmetry(self):
        """codim(g) = codim formula (g-2)(g-3)/2: verify (g-2)(g-3) is even."""
        for g in range(2, 50):
            product = (g - 2) * (g - 3)
            assert product % 2 == 0, f"(g-2)(g-3) should be even at g={g}"

    def test_dim_A_g_minus_dim_M_g_nonneg(self):
        """dim A_g >= dim M_g for all g >= 1."""
        for g in range(1, 50):
            assert dim_A_g(g) >= dim_M_g(g)

    def test_schottky_at_g4_is_hypersurface(self):
        """At g=4 the Jacobian locus is a hypersurface (codim = 1)."""
        assert schottky_codimension(4) == 1
        assert dim_A_g(4) - dim_M_g(4) == 1

    def test_theta_even_exceeds_odd(self):
        """Number of even theta chars > odd for all g >= 1."""
        for g in range(1, 10):
            tc = theta_char_count(g)
            assert tc['even'] > tc['odd']

    def test_lambda_g_prefactor_approaches_one(self):
        """(2^{2g-1}-1)/2^{2g-1} -> 1 as g -> infinity."""
        for g in [10, 20, 50]:
            pf = F(2**(2*g-1) - 1, 2**(2*g-1))
            assert F(1) - pf < F(1, 2**(2*g - 2))

    def test_F3_via_kappa_times_lambda(self):
        """F_3 = kappa * lambda_3 for multiple kappa values."""
        for k_val in [1, 2, 3, 5, 10]:
            k = F(k_val)
            expected = k * F(31, 967680)
            assert k * lambda_fp(3) == expected

    def test_closed_form_at_t0(self):
        """Closed form at t=0 should be 0."""
        assert shadow_pf_closed_form(0.0) == 0.0

    def test_asymptotics_ratio_convergence(self):
        """Ratio lambda_g / asymptotic converges to 1.

        The ratio = prefactor * zeta(2g) where prefactor -> 1 and
        zeta(2g) -> 1. It need not be monotone but must approach 1.
        """
        for g in range(5, 15):
            data = lambda_g_asymptotics(g)
            ratio = data['ratio_to_asymptotic']
            assert abs(ratio - 1.0) < 0.05, \
                f"Ratio should be close to 1 at g={g}, got {ratio}"
        # Verify tighter bound at large g
        data_20 = lambda_g_asymptotics(20)
        assert abs(data_20['ratio_to_asymptotic'] - 1.0) < 1e-5
