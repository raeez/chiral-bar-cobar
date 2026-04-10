r"""Tests for the Barnes-Wall BW_48 lattice shadow engine.

Verifies the arithmetic shadow tower of the rank-48 even unimodular lattice
VOA reaches depth 5, the first lattice rank achieving this depth.

Key claims tested:
  1. kappa(V_{BW_48}) = 48 (lattice VOA: kappa = rank)
  2. Theta function weight = rank/2 = 24
  3. dim S_24(SL(2,Z)) = 2 (two independent cusp eigenforms)
  4. dim M_24(SL(2,Z)) = 3
  5. Shadow depth = 3 + dim S_24 = 5
  6. Tower: S_5 != 0, S_6 = 0
  7. Discriminant Delta != 0 (class F_5, not class G)
  8. Rank 48 is the FIRST rank with shadow depth 5
  9. Cusp form product basis: {Delta*E_4^3, Delta*E_6^2}
  10. Hecke eigenvalues satisfy Ramanujan-Petersson bound
  11. T_2 characteristic polynomial on S_24: x^2 - 1080x - 20468736

Cross-verification against:
  - lattice_shadow_higher_depth_engine: shadow_depth_lattice(48) = 5
  - cusp_form_shadow_arity: arithmetic_sieve(48)['depth'] = 5
"""

from __future__ import annotations

import math

import pytest

from compute.lib.barnes_wall_48_shadow_engine import (
    bw48_kappa,
    bw48_theta_coefficients,
    bw48_theta_weight,
    cusp_form_contribution_weight24,
    cusp_form_data_weight24,
    depth_comparison_table,
    dim_cusp_forms,
    dim_modular_forms,
    discriminant_bw48,
    kappa_lattice,
    shadow_depth_bw48,
    shadow_depth_lattice,
    shadow_tower_bw48,
    verify_all,
)


# =========================================================================
# Kappa tests
# =========================================================================


class TestKappa:
    """Tests for kappa(V_{BW_48}) = 48."""

    def test_kappa_bw48_equals_rank(self) -> None:
        # VERIFIED: [DC] 48 Heisenberg bosons at level 1, kappa = 48*1 = 48;
        # [CF] kappa(E_8) = 8, kappa(Leech) = 24, pattern kappa = rank;
        # [LT] lattice_voa_shadows.py: kappa_lattice(r) = r.
        assert bw48_kappa() == 48

    def test_kappa_not_rank_over_two(self) -> None:
        # VERIFIED: [DC] each Heisenberg boson contributes kappa = 1, not 1/2;
        # [CF] kappa(E_8) = 8 (not 4), kappa(Leech) = 24 (not 12).
        # Common error: confusing kappa = rank with weight k = rank/2.
        assert bw48_kappa() != 48 // 2
        assert bw48_kappa() != 24

    def test_kappa_lattice_general(self) -> None:
        # VERIFIED: [DC] kappa = rank for all lattice VOAs;
        # [LT] lattice_voa_shadows.py.
        assert kappa_lattice(8) == 8
        assert kappa_lattice(24) == 24
        assert kappa_lattice(48) == 48
        assert kappa_lattice(72) == 72


# =========================================================================
# Weight and modular form dimension tests
# =========================================================================


class TestModularFormDimensions:
    """Tests for dimensions of M_k and S_k."""

    def test_theta_weight_is_rank_over_two(self) -> None:
        # VERIFIED: [DC] theta function of rank-r lattice has weight r/2;
        # [LT] Serre, "A Course in Arithmetic", Ch. VII.
        assert bw48_theta_weight() == 24

    def test_dim_M_24(self) -> None:
        # VERIFIED: [DC] floor(24/12) + 1 = 3 (24 mod 12 = 0, not 2);
        # [LT] Diamond-Shurman Thm 3.5.1;
        # [NE] LMFDB: 3 modular forms of weight 24, level 1.
        assert dim_modular_forms(24) == 3

    def test_dim_S_24(self) -> None:
        # VERIFIED: [DC] dim M_24 - 1 = 3 - 1 = 2;
        # [LT] LMFDB: 2 newforms of weight 24, level 1;
        # [CF] first weight with dim S_k = 2 (dim S_22 = 1, dim S_24 = 2).
        assert dim_cusp_forms(24) == 2

    def test_dim_S_24_is_first_with_two_cusp_forms(self) -> None:
        # VERIFIED: [DC] dim S_k for k = 12,14,...,22 are all <= 1;
        # [LT] standard tables of cusp form dimensions.
        for k in range(12, 24, 2):
            assert dim_cusp_forms(k) <= 1, f"dim S_{k} > 1 unexpected"
        assert dim_cusp_forms(24) == 2

    def test_dim_cusp_forms_small_weights(self) -> None:
        # VERIFIED: [DC] standard dimension formula applied to each weight;
        # [LT] Diamond-Shurman Table 3.1.
        expected = {
            2: 0, 4: 0, 6: 0, 8: 0, 10: 0,
            12: 1,   # Delta
            14: 0,   # k%12==2, floor(14/12)-1=0
            16: 1,   # Delta*E_4
            18: 1,   # Delta*E_6
            20: 1,
            22: 1,
            24: 2,   # FIRST dim=2
            26: 1,   # k%12==2, floor(26/12)-1=1
            28: 2,
            36: 3,
        }
        for k, exp in expected.items():
            assert dim_cusp_forms(k) == exp, f"dim S_{k} = {dim_cusp_forms(k)}, expected {exp}"


# =========================================================================
# Shadow depth tests
# =========================================================================


class TestShadowDepth:
    """Tests for shadow depth = 3 + dim S_{rank/2}."""

    def test_bw48_depth_equals_5(self) -> None:
        # VERIFIED: [DC] 3 + dim S_24 = 3 + 2 = 5;
        # [CF] lattice_shadow_higher_depth_engine.shadow_depth_lattice(48) = 5;
        # [LT] cusp_form_shadow_arity.py: arithmetic_sieve(48)['depth'] = 5.
        assert shadow_depth_bw48() == 5

    def test_depth_formula_consistency(self) -> None:
        # VERIFIED: [DC] 3 + dim_cusp_forms(24) = 3 + 2 = 5;
        # [CF] shadow_depth_lattice(48) uses the same formula.
        assert shadow_depth_bw48() == 3 + dim_cusp_forms(24)
        assert shadow_depth_lattice(48) == 5

    def test_depth_comparison_across_ranks(self) -> None:
        """Verify depth at landmark ranks."""
        # VERIFIED: [DC] 3 + dim S_{r/2} for each rank;
        # [LT] lattice_shadow_higher_depth_engine test cases.
        expected_depths = {
            8: 3,    # dim S_4 = 0
            16: 3,   # dim S_8 = 0
            24: 4,   # dim S_12 = 1
            32: 4,   # dim S_16 = 1
            40: 4,   # dim S_20 = 1
            48: 5,   # dim S_24 = 2  <-- FIRST DEPTH 5
            56: 5,   # dim S_28 = 2
            64: 6,   # dim S_32 = 3  <-- FIRST DEPTH 6
            72: 6,   # dim S_36 = 3
        }
        for rank, exp_depth in expected_depths.items():
            assert shadow_depth_lattice(rank) == exp_depth, (
                f"rank {rank}: depth = {shadow_depth_lattice(rank)}, expected {exp_depth}"
            )

    def test_depth_is_nondecreasing(self) -> None:
        # VERIFIED: [DC] dim S_k is nondecreasing in k for even k;
        # [SY] cusp form space grows monotonically.
        depths = [shadow_depth_lattice(r) for r in range(8, 97, 8)]
        assert depths == sorted(depths)


# =========================================================================
# Shadow tower structure tests
# =========================================================================


class TestShadowTower:
    """Tests for the arity-by-arity shadow tower."""

    def test_tower_arity_2_is_kappa(self) -> None:
        # VERIFIED: [DC] S_2 = kappa by definition of the shadow tower;
        # [LT] cusp_form_shadow_arity.py: arity 2 always detects curvature.
        tower = shadow_tower_bw48()
        assert tower['tower'][2]['value'] == 48
        assert tower['tower'][2]['nonzero'] is True
        assert tower['tower'][2]['type'] == 'Eisenstein'

    def test_tower_arity_3_nonzero(self) -> None:
        # VERIFIED: [DC] Eisenstein contribution at arity 3 is nonzero for k >= 4;
        # [CF] all ranks >= 8 have nonzero arity-3 shadow.
        tower = shadow_tower_bw48()
        assert tower['tower'][3]['nonzero'] is True
        assert tower['tower'][3]['type'] == 'Eisenstein'

    def test_tower_arity_4_nonzero_first_cusp(self) -> None:
        # VERIFIED: [DC] dim S_24 >= 1, so first cusp form appears at arity 4;
        # [LT] period-shadow dictionary: j-th cusp form at arity 3+j.
        tower = shadow_tower_bw48()
        assert tower['tower'][4]['nonzero'] is True
        assert tower['tower'][4]['type'] == 'cuspidal'

    def test_tower_arity_5_nonzero_second_cusp(self) -> None:
        # VERIFIED: [DC] dim S_24 = 2, so second cusp form appears at arity 5;
        # [LT] period-shadow dictionary: 2nd cusp at arity 3+2 = 5.
        tower = shadow_tower_bw48()
        assert tower['tower'][5]['nonzero'] is True
        assert tower['tower'][5]['type'] == 'cuspidal'

    def test_tower_arity_6_zero(self) -> None:
        # VERIFIED: [DC] dim S_24 = 2, so no cusp form at arity 6 = 3+3;
        # [LT] tower terminates at depth 3 + dim S_k.
        tower = shadow_tower_bw48()
        assert tower['tower'][6]['nonzero'] is False
        assert tower['tower'][6]['value'] == 0

    def test_tower_terminates_at_arity_5(self) -> None:
        # VERIFIED: [DC] last nonzero arity is 5 = 3 + 2;
        # [CF] shadow_depth_bw48() = 5.
        tower = shadow_tower_bw48()
        assert tower['terminates_at_arity'] == 5
        assert tower['first_zero_arity'] == 6

    def test_tower_depth_matches_formula(self) -> None:
        # VERIFIED: [DC] tower reports depth consistent with formula;
        # [CF] shadow_depth_bw48() agrees.
        tower = shadow_tower_bw48()
        assert tower['depth'] == shadow_depth_bw48() == 5


# =========================================================================
# Discriminant tests
# =========================================================================


class TestDiscriminant:
    """Tests for the shadow discriminant Delta = 8*kappa*S_4."""

    def test_discriminant_nonzero(self) -> None:
        # VERIFIED: [DC] kappa = 48 != 0 and dim S_24 >= 1 so S_4 != 0;
        # [LT] concordance: Delta != 0 implies not class G.
        disc = discriminant_bw48()
        assert disc['discriminant_nonzero'] is True

    def test_kappa_component_nonzero(self) -> None:
        # VERIFIED: [DC] kappa = 48;
        # [LT] lattice_voa_shadows: kappa_lattice(48) = 48.
        disc = discriminant_bw48()
        assert disc['kappa'] == 48
        assert disc['kappa_nonzero'] is True

    def test_s4_component_nonzero(self) -> None:
        # VERIFIED: [DC] first cusp form in S_24 contributes at arity 4;
        # [LT] cusp_form_shadow_arity: arity 4 detects cusp forms.
        disc = discriminant_bw48()
        assert disc['S_4_nonzero'] is True

    def test_class_is_F5(self) -> None:
        # VERIFIED: [DC] depth = 5 and Delta != 0;
        # [LT] shadow_class_lattice: F_d for d >= 5.
        disc = discriminant_bw48()
        assert disc['class'] == 'F_5'


# =========================================================================
# Cusp form data tests
# =========================================================================


class TestCuspFormData:
    """Tests for the cusp form space S_24 and Hecke eigenvalues."""

    def test_dim_S_24_in_cusp_data(self) -> None:
        # VERIFIED: [DC] dim S_24 = 2;
        # [LT] LMFDB.
        data = cusp_form_data_weight24()
        assert data['dim_S_24'] == 2

    def test_product_basis(self) -> None:
        # VERIFIED: [DC] wt(Delta*E_4^3) = 12+12 = 24, wt(Delta*E_6^2) = 12+12 = 24;
        # [LT] standard modular form theory: S_k = Delta * M_{k-12}.
        data = cusp_form_data_weight24()
        assert len(data['product_basis']) == 2
        assert 'Delta * E_4^3' in data['product_basis']
        assert 'Delta * E_6^2' in data['product_basis']

    def test_hecke_field(self) -> None:
        # VERIFIED: [DC] T_2 char poly discriminant = 24^2 * 144169;
        # [LT] LMFDB: Hecke field for weight-24 level-1 newforms is Q(sqrt(144169)).
        data = cusp_form_data_weight24()
        assert data['hecke_field'] == 'Q(sqrt(144169))'

    def test_T2_char_poly(self) -> None:
        # VERIFIED: [LT] LMFDB: T_2 on S_24(Gamma_0(1)) has char poly x^2 - 1080x - 20468736;
        # [NE] discriminant = 1080^2 + 4*20468736 = 83041344 = 576*144169.
        data = cusp_form_data_weight24()
        coeffs = data['T2_char_poly']
        assert coeffs == [1, -1080, -20468736]

    def test_T2_discriminant(self) -> None:
        # VERIFIED: [DC] 1080^2 + 4*20468736 = 1166400 + 81874944 = 83041344;
        # [DC] 83041344 / 576 = 144169; 576 = 24^2.
        data = cusp_form_data_weight24()
        assert data['T2_discriminant'] == 83041344
        assert 83041344 == 576 * 144169
        assert 576 == 24**2

    def test_ramanujan_petersson_bound(self) -> None:
        """Both Hecke eigenvalues satisfy |a_2| <= 2 * 2^{23/2}."""
        # VERIFIED: [DC] RP bound = 2^{25/2} ~ 5792.6;
        # [NE] |540 + 12*sqrt(144169)| ~ 5096.4 < 5792.6;
        # [NE] |540 - 12*sqrt(144169)| ~ 4016.4 < 5792.6;
        # [LT] Deligne's theorem (1974) for weight-24 eigenforms.
        data = cusp_form_data_weight24()
        assert data['rp_satisfied'] is True

        # Numerical check
        sqrt_disc = math.sqrt(144169)
        a2_plus = 540 + 12 * sqrt_disc
        a2_minus = 540 - 12 * sqrt_disc
        rp_bound = 2 * 2**(23/2)
        assert abs(a2_plus) < rp_bound, f"|a2+| = {abs(a2_plus)} >= {rp_bound}"
        assert abs(a2_minus) < rp_bound, f"|a2-| = {abs(a2_minus)} >= {rp_bound}"


# =========================================================================
# Cusp form contribution tests
# =========================================================================


class TestCuspFormContribution:
    """Tests for the cusp form contribution structure at weight 24."""

    def test_weight_checks(self) -> None:
        # VERIFIED: [DC] 12 + 3*4 = 24 and 12 + 2*6 = 24;
        # [DA] weight is additive under multiplication.
        data = cusp_form_contribution_weight24()
        assert data['product_basis']['weight_check_alpha'] == 24
        assert data['product_basis']['weight_check_beta'] == 24

    def test_contributes_to_arities_4_and_5(self) -> None:
        # VERIFIED: [DC] 2 cusp forms at arities 3+1=4 and 3+2=5;
        # [LT] period-shadow dictionary.
        data = cusp_form_contribution_weight24()
        assert data['contributes_to_arities'] == [4, 5]


# =========================================================================
# First-depth-5 test
# =========================================================================


class TestFirstDepth5:
    """Verify rank 48 is the first rank achieving shadow depth 5."""

    def test_rank_48_is_first_depth_5(self) -> None:
        # VERIFIED: [DC] ranks 8,16: depth 3; ranks 24,32,40: depth 4; rank 48: depth 5;
        # [CF] no rank < 48 (multiple of 8) has dim S_{r/2} >= 2.
        for rank in range(8, 48, 8):
            assert shadow_depth_lattice(rank) < 5, (
                f"rank {rank} has depth {shadow_depth_lattice(rank)} >= 5"
            )
        assert shadow_depth_lattice(48) == 5

    def test_depth_table_marks_first(self) -> None:
        # VERIFIED: [DC] depth_comparison_table flags first_at_this_depth;
        # [CF] consistent with test_rank_48_is_first_depth_5.
        table = depth_comparison_table()
        bw48 = [e for e in table if e['rank'] == 48][0]
        assert bw48['first_at_this_depth'] is True
        assert bw48['depth'] == 5


# =========================================================================
# Theta coefficients structure test
# =========================================================================


class TestThetaCoefficients:
    """Tests for the theta function decomposition structure."""

    def test_eisenstein_q0_is_one(self) -> None:
        # VERIFIED: [DC] E_24 is normalized with constant term 1;
        # [LT] standard Eisenstein normalization.
        data = bw48_theta_coefficients(5)
        from sympy import Rational
        assert data['eisenstein_coefficients'][0] == Rational(1)

    def test_bernoulli_24(self) -> None:
        # VERIFIED: [DC] B_24 = -236364091/2730 from Bernoulli tables;
        # [LT] OEIS A027641/A027642.
        data = bw48_theta_coefficients(1)
        from sympy import Rational
        assert data['B_24'] == Rational(-236364091, 2730)

    def test_two_free_parameters(self) -> None:
        # VERIFIED: [DC] Theta = E_24 + c_1*f_1 + c_2*f_2 has 2 free params;
        # [DA] dim S_24 = 2 cusp forms require 2 coefficients.
        data = bw48_theta_coefficients(1)
        assert data['num_free_parameters'] == 2


# =========================================================================
# Cross-engine consistency tests
# =========================================================================


class TestCrossEngineConsistency:
    """Cross-check against lattice_shadow_higher_depth_engine."""

    def test_vs_lattice_shadow_higher_depth(self) -> None:
        """BW_48 engine depth must match lattice_shadow_higher_depth_engine."""
        # VERIFIED: [CF] two independent implementations of the same formula;
        # [DC] both compute 3 + dim S_24 = 5.
        from compute.lib.lattice_shadow_higher_depth_engine import (
            shadow_depth_lattice as sdl_other,
            dim_cusp_forms as dcf_other,
        )
        assert shadow_depth_bw48() == sdl_other(48)
        assert dim_cusp_forms(24) == dcf_other(24)

    def test_vs_cusp_form_shadow_arity(self) -> None:
        """BW_48 engine depth must match cusp_form_shadow_arity engine."""
        # VERIFIED: [CF] third independent implementation of the formula;
        # [DC] all three compute depth = 5.
        from compute.lib.cusp_form_shadow_arity import (
            shadow_depth_lattice as sdl_cusp,
            dim_Sk as dim_Sk_cusp,
        )
        assert shadow_depth_bw48() == sdl_cusp(48)
        assert dim_cusp_forms(24) == dim_Sk_cusp(24)


# =========================================================================
# Full verification suite
# =========================================================================


class TestVerifyAll:
    """Test the engine's internal verification suite."""

    def test_verify_all_passes(self) -> None:
        results = verify_all()
        assert results['overall']['all_pass'] is True

    def test_verify_all_individual(self) -> None:
        results = verify_all()
        for key, val in results.items():
            if key == 'overall':
                continue
            assert val['pass'] is True, f"verify_all[{key}] failed: {val}"
