r"""Tests for costello_2loop_qcd_engine: genus-2 shadow meets Costello 2-loop QCD.

Verifies the bridge between:
  - Costello's celestial chiral algebra framework [C23, arXiv:2302.00770]
  - The genus-2 shadow projection of Theta_A (Theorem D)
  - QCD anomaly cancellation in the holomorphic twist

TEST ORGANIZATION (34 tests):
  1. Bernoulli numbers and lambda_fp (multi-path, AP38)
  2. Kappa formulas for sl_N (AP1, AP9: recomputed, != c/2)
  3. Kappa cross-verification via Feigin-Frenkel duality (AP24)
  4. QCD celestial algebra construction (gauge + matter)
  5. Anomaly cancellation: holomorphic vs 4d beta functions (AP29)
  6. Genus-2 free energy F_2 = kappa * 7/5760 (scalar level)
  7. Planted-forest correction at genus 2
  8. Form factor hierarchy: tree=g0, 1-loop=g1, 2-loop=g2
  9. Costello comparison (structural bridge)
 10. Large-N scaling
 11. Ahat generating function
 12. Beilinson falsification of task claims

MULTI-PATH VERIFICATION (3+ paths per claim):
  Path 1: direct computation from definition
  Path 2: Feigin-Frenkel duality (AP24)
  Path 3: cross-family consistency / additivity
  Path 4: comparison with existing engines
  Path 5: limiting cases (k=0, N_f=0, large N)
  Path 6: Ahat generating function

Ground truth (independently computed):
  kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)      [from definition, AP1]
  kappa(V_0(sl_2)) = 3/2                      [3*2/4]
  kappa(V_0(sl_3)) = 4                        [8*3/6]
  kappa(V_0(sl_4)) = 15/2                     [15*4/8]
  kappa(V_0(sl_5)) = 12                       [24*5/10]
  lambda_1^FP = 1/24                          [Faber-Pandharipande]
  lambda_2^FP = 7/5760                        [Faber-Pandharipande]
  lambda_3^FP = 31/967680                     [Faber-Pandharipande]
"""

from fractions import Fraction

import pytest

from compute.lib.costello_2loop_qcd_engine import (
    # Helpers
    _frac,
    _bernoulli_exact,
    _lambda_fp_exact,
    _ahat_coefficient,
    # Lie algebra
    LieAlgebraData,
    sl_N_data,
    # Kappa
    kappa_affine_slN,
    kappa_affine_general,
    central_charge_affine_slN,
    kappa_bc_fundamental,
    kappa_betagamma_fundamental,
    # QCD algebra
    QCDCelestialAlgebra,
    make_qcd_algebra,
    make_pure_ym_algebra,
    # Genus-2 free energy
    Genus2FreeEnergy,
    genus_2_free_energy_pure_ym,
    genus_2_free_energy_qcd,
    # Form factor hierarchy
    FormFactorLevel,
    form_factor_hierarchy,
    # Costello comparison
    CostelloComparison,
    costello_two_loop_comparison,
    # Anomaly
    AnomalyCancellation,
    anomaly_cancellation_analysis,
    find_holomorphic_conformal_N_f,
    find_asymptotic_freedom_bound,
    find_kappa_zero_N_f,
    # Collinear splitting
    CollinearSplittingData,
    collinear_splitting_tower,
    # Shadow tower
    shadow_tower_pure_ym,
    # Cross-check
    KappaCrossCheck,
    kappa_cross_check,
    # Tables
    F_2_numerical_table,
    kappa_total_vs_N_f,
    # Large-N
    LargeNScaling,
    large_N_scaling_analysis,
    # Ahat
    verify_ahat_generating_function,
    # Planted-forest
    planted_forest_genus_2,
    planted_forest_genus_2_pure_ym,
    # Full analysis
    full_costello_2loop_analysis,
)


# ========================================================================
# 1.  Bernoulli numbers and lambda_fp
# ========================================================================

class TestBernoulliAndLambdaFP:
    """Verify exact Bernoulli numbers and Faber-Pandharipande intersection
    numbers via multi-path computation."""

    def test_bernoulli_known_values(self):
        """Path 1: Bernoulli numbers from direct recursion."""
        assert _bernoulli_exact(0) == Fraction(1)
        assert _bernoulli_exact(1) == Fraction(-1, 2)
        assert _bernoulli_exact(2) == Fraction(1, 6)
        assert _bernoulli_exact(4) == Fraction(-1, 30)
        assert _bernoulli_exact(6) == Fraction(1, 42)
        assert _bernoulli_exact(8) == Fraction(-1, 30)
        assert _bernoulli_exact(10) == Fraction(5, 66)

    def test_bernoulli_odd_vanish(self):
        """Path 2: B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert _bernoulli_exact(n) == 0

    def test_lambda_fp_genus_1(self):
        """lambda_1^FP = 1/24 via (2^1 - 1)|B_2|/(2^1 * 2!) = 1/12 / 2 = 1/24."""
        # Direct: (2^1 - 1) * |1/6| / (2^1 * 2!) = 1 * 1/6 / (2 * 2) = 1/24
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_fp_genus_2(self):
        """lambda_2^FP = 7/5760 via (2^3 - 1)|B_4|/(2^3 * 4!) = 7/30 / (8*24)."""
        # Direct: (8-1)*|(-1/30)|/(8*24) = 7*(1/30)/(192) = 7/5760
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_fp_genus_3(self):
        """lambda_3^FP = 31/967680."""
        # (2^5-1)*|B_6|/(2^5 * 6!) = 31*(1/42)/(32*720) = 31/967680
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_fp_genus_4(self):
        """lambda_4^FP = 127/154828800."""
        # (2^7-1)*|B_8|/(2^7*8!) = 127*(1/30)/(128*40320) = 127/154828800
        assert _lambda_fp_exact(4) == Fraction(127, 154828800)

    def test_lambda_fp_positivity(self):
        """All lambda_g^FP are positive (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert _lambda_fp_exact(g) > 0

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is strictly decreasing in g."""
        for g in range(1, 7):
            assert _lambda_fp_exact(g) > _lambda_fp_exact(g + 1)


# ========================================================================
# 2.  Kappa formulas for sl_N (AP1, AP9)
# ========================================================================

class TestKappaFormulas:
    """Verify kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N) from first principles.
    AP1: recomputed, not copied. AP9: kappa != c/2 for dim(g) > 1."""

    def test_kappa_su2_k0(self):
        """SU(2) k=0: dim=3, h^v=2, kappa=3*2/(2*2)=3/2."""
        assert kappa_affine_slN(2, 0) == Fraction(3, 2)

    def test_kappa_su3_k0(self):
        """SU(3) k=0: dim=8, h^v=3, kappa=8*3/(2*3)=4."""
        assert kappa_affine_slN(3, 0) == Fraction(4)

    def test_kappa_su4_k0(self):
        """SU(4) k=0: dim=15, h^v=4, kappa=15*4/(2*4)=15/2."""
        assert kappa_affine_slN(4, 0) == Fraction(15, 2)

    def test_kappa_su5_k0(self):
        """SU(5) k=0: dim=24, h^v=5, kappa=24*5/(2*5)=12."""
        assert kappa_affine_slN(5, 0) == Fraction(12)

    def test_kappa_su3_k1(self):
        """SU(3) k=1: kappa=8*4/6=16/3 (NOT 4; task claim was wrong)."""
        assert kappa_affine_slN(3, 1) == Fraction(16, 3)

    def test_kappa_su2_k1(self):
        """SU(2) k=1: kappa=3*3/4=9/4 (NOT 3/4; task claim was wrong)."""
        assert kappa_affine_slN(2, 1) == Fraction(9, 4)

    def test_kappa_ne_c_over_2_ap9(self):
        """AP9: kappa != c/2 for sl_N with N >= 2 at k != 0.

        kappa = (N^2-1)(k+N)/(2N), c = k(N^2-1)/(k+N).
        c/2 = k(N^2-1)/(2(k+N)).
        kappa/c*2 = (k+N)^2 / (kN) which is != 1 unless k+N = sqrt(kN)
        (impossible for k, N > 0).
        """
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3]:
                kap = kappa_affine_slN(N, k)
                cc = central_charge_affine_slN(N, k)
                assert kap != cc / 2, f"AP9 violation: SU({N}) k={k}"

    def test_kappa_k0_c_is_zero(self):
        """At k=0: c=0, kappa=(N^2-1)/2 != 0. Kappa and c are independent."""
        for N in [2, 3, 4]:
            assert central_charge_affine_slN(N, 0) == 0
            assert kappa_affine_slN(N, 0) != 0

    def test_kappa_formula_consistency_with_general(self):
        """Cross-check: kappa_affine_slN matches kappa_affine_general."""
        for N in [2, 3, 4, 5]:
            for k in [0, 1, 2]:
                kap_specific = kappa_affine_slN(N, k)
                kap_general = kappa_affine_general(N * N - 1, Fraction(k), N)
                assert kap_specific == kap_general


# ========================================================================
# 3.  Feigin-Frenkel duality (AP24)
# ========================================================================

class TestFeiginFrenkelDuality:
    """Verify kappa(k) + kappa(-k-2h^v) = 0 for KM families (AP24)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_complementarity_k0(self, N):
        """AP24 at k=0: kappa(0) + kappa(-2N) = 0."""
        cc = kappa_cross_check(N, 0)
        assert cc.complementarity_sum == 0

    @pytest.mark.parametrize("N,k", [(2, 1), (3, 1), (3, 2), (4, 1), (5, 3)])
    def test_complementarity_general(self, N, k):
        """AP24 at general k."""
        cc = kappa_cross_check(N, k)
        assert cc.complementarity_sum == 0

    def test_dual_level_formula(self):
        """Feigin-Frenkel dual level: k' = -k - 2h^v = -k - 2N."""
        N, k = 3, 1
        k_dual = -Fraction(k) - 2 * N  # = -7
        assert k_dual == Fraction(-7)
        kap = kappa_affine_slN(N, k)
        kap_dual = kappa_affine_slN(N, k_dual)
        assert kap + kap_dual == 0


# ========================================================================
# 4.  QCD celestial algebra
# ========================================================================

class TestQCDCelestialAlgebra:
    """Test QCD celestial algebra: gauge + matter contributions."""

    def test_pure_ym_is_nf_zero(self):
        """Pure YM = QCD with N_f=0."""
        pure = make_pure_ym_algebra(3, 0)
        qcd = make_qcd_algebra(3, 0, 0)
        assert pure.kappa_total == qcd.kappa_total

    def test_kappa_additivity(self):
        """kappa_total = kappa_gauge + N_f * kappa_matter (additivity)."""
        alg = make_qcd_algebra(3, 9, 0)
        assert alg.kappa_total == alg.kappa_gauge + 9 * alg.kappa_matter_per_flavor

    def test_su3_nf9_kappa_gauge(self):
        """SU(3) gauge sector at k=0: kappa = 4."""
        alg = make_qcd_algebra(3, 9, 0)
        assert alg.kappa_gauge == Fraction(4)

    def test_su3_nf9_kappa_matter_per_flavor(self):
        """Each bc flavor in fund of SU(3): kappa = -3."""
        alg = make_qcd_algebra(3, 9, 0)
        assert alg.kappa_matter_per_flavor == Fraction(-3)

    def test_su3_nf9_kappa_total(self):
        """SU(3) N_f=9: kappa_total = 4 + 9*(-3) = 4 - 27 = -23."""
        alg = make_qcd_algebra(3, 9, 0)
        assert alg.kappa_total == Fraction(-23)

    def test_su3_nf0_pure_gauge(self):
        """SU(3) N_f=0: kappa_total = kappa_gauge = 4."""
        alg = make_qcd_algebra(3, 0, 0)
        assert alg.kappa_total == Fraction(4)

    def test_central_charge_gauge_k0(self):
        """c(V_0(sl_3)) = 0 (self-dual level)."""
        alg = make_qcd_algebra(3, 0, 0)
        assert alg.central_charge_gauge == 0

    def test_bc_kappa_sign(self):
        """bc systems (fermionic) have NEGATIVE kappa (AP20)."""
        for N in [2, 3, 4, 5]:
            assert kappa_bc_fundamental(N) < 0

    def test_betagamma_kappa_sign(self):
        """betagamma systems (bosonic) have POSITIVE kappa."""
        for N in [2, 3, 4, 5]:
            assert kappa_betagamma_fundamental(N) > 0

    def test_bc_betagamma_opposite(self):
        """kappa_bc = -kappa_betagamma (same magnitude, opposite sign)."""
        for N in [2, 3, 4, 5]:
            assert kappa_bc_fundamental(N) == -kappa_betagamma_fundamental(N)


# ========================================================================
# 5.  Anomaly cancellation (AP29: three distinct conditions)
# ========================================================================

class TestAnomalyCancellation:
    """Verify anomaly cancellation in the holomorphic twist vs 4d."""

    def test_holomorphic_conformal_nf(self):
        """b_0^hol = 0 at N_f = 2N."""
        for N in [2, 3, 4, 5]:
            assert find_holomorphic_conformal_N_f(N) == 2 * N

    def test_asymptotic_freedom_bound(self):
        """4d asymptotic freedom: N_f < 11N."""
        for N in [2, 3, 4, 5]:
            assert find_asymptotic_freedom_bound(N) == 11 * N

    def test_su3_nf9_holomorphic_beta(self):
        """SU(3) N_f=9: b_0^hol = 3 - 9/2 = -3/2."""
        ac = anomaly_cancellation_analysis(3, 9, 0)
        assert ac.b_0_holomorphic == Fraction(-3, 2)

    def test_su3_nf9_4d_beta(self):
        """SU(3) N_f=9: b_0^4d = 11 - 3 = 8."""
        ac = anomaly_cancellation_analysis(3, 9, 0)
        assert ac.b_0_4d == Fraction(8)

    def test_su3_nf9_asymptotically_free(self):
        """SU(3) N_f=9 is asymptotically free (N_f=9 < 11*3=33)."""
        ac = anomaly_cancellation_analysis(3, 9, 0)
        assert ac.is_asymptotically_free_4d is True

    def test_su3_nf6_holomorphic_conformal(self):
        """SU(3) N_f=6: b_0^hol = 0 (holomorphic conformal)."""
        ac = anomaly_cancellation_analysis(3, 6, 0)
        assert ac.is_holomorphic_conformal is True
        assert ac.b_0_holomorphic == 0

    def test_su3_nf9_not_holomorphic_conformal(self):
        """SU(3) N_f=9: NOT holomorphic conformal (b_0^hol != 0)."""
        ac = anomaly_cancellation_analysis(3, 9, 0)
        assert ac.is_holomorphic_conformal is False

    def test_one_loop_level_shift(self):
        """One-loop level shift = -N + N_f/2."""
        ac = anomaly_cancellation_analysis(3, 9, 0)
        assert ac.one_loop_level_shift == Fraction(3, 2)

    def test_ap29_three_conditions_distinct(self):
        """AP29: the three cancellation conditions are at DIFFERENT N_f.

        For SU(3):
          b_0^hol = 0 at N_f = 6
          b_0^4d = 0 at N_f = 33
          kappa_total = 0 at N_f = 4/3 (not integer)
        """
        N = 3
        nf_hol = find_holomorphic_conformal_N_f(N)
        nf_4d = find_asymptotic_freedom_bound(N)
        nf_kappa = find_kappa_zero_N_f(N, 0)
        assert nf_hol == 6
        assert nf_4d == 33
        assert nf_kappa == Fraction(4, 3)
        # All three are distinct
        assert nf_hol != nf_4d
        assert nf_hol != nf_kappa
        assert nf_4d != nf_kappa


# ========================================================================
# 6.  Genus-2 free energy
# ========================================================================

class TestGenus2FreeEnergy:
    """Test F_2 = kappa * 7/5760 at the scalar level."""

    def test_F2_su2_k0(self):
        """SU(2) k=0: F_2_scalar = (3/2) * 7/5760 = 7/3840."""
        data = genus_2_free_energy_pure_ym(2, 0)
        assert data.F_2_scalar == Fraction(7, 3840)

    def test_F2_su3_k0(self):
        """SU(3) k=0: F_2_scalar = 4 * 7/5760 = 7/1440."""
        data = genus_2_free_energy_pure_ym(3, 0)
        assert data.F_2_scalar == Fraction(7, 1440)

    def test_F2_su4_k0(self):
        """SU(4) k=0: F_2_scalar = (15/2) * 7/5760 = 7/768."""
        data = genus_2_free_energy_pure_ym(4, 0)
        assert data.F_2_scalar == Fraction(7, 768)

    def test_F2_su5_k0(self):
        """SU(5) k=0: F_2_scalar = 12 * 7/5760 = 7/480."""
        data = genus_2_free_energy_pure_ym(5, 0)
        assert data.F_2_scalar == Fraction(7, 480)

    def test_F2_linearity_in_kappa(self):
        """F_2_scalar is linear in kappa: F_2(a*kappa) = a * F_2(kappa)."""
        for N in [2, 3, 4, 5]:
            data = genus_2_free_energy_pure_ym(N, 0)
            assert data.F_2_scalar == data.kappa * Fraction(7, 5760)

    def test_F2_qcd_scalar_uses_kappa_total(self):
        """QCD F_2_scalar uses kappa_total = kappa_gauge + N_f*kappa_matter."""
        data = genus_2_free_energy_qcd(3, 9, 0)
        expected = Fraction(-23) * Fraction(7, 5760)
        assert data.F_2_scalar == expected


# ========================================================================
# 7.  Planted-forest correction at genus 2
# ========================================================================

class TestPlantedForest:
    """Test delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48."""

    def test_pf_formula(self):
        """Direct formula verification."""
        kap = Fraction(4)
        S_3 = Fraction(1, 2)
        delta = planted_forest_genus_2(kap, S_3)
        # S_3 * (10*S_3 - kappa) / 48 = (1/2)*(10/2 - 4)/48 = (1/2)*1/48 = 1/96
        assert delta == Fraction(1, 96)

    def test_pf_su3_k0(self):
        """SU(3) k=0: kappa=4, S_3=2*3/(3*4)=1/2, delta_pf=1/96."""
        data = planted_forest_genus_2_pure_ym(3, 0)
        assert data['kappa'] == Fraction(4)
        assert data['S_3'] == Fraction(1, 2)
        assert data['delta_pf'] == Fraction(1, 96)

    def test_pf_vanishes_for_S3_zero(self):
        """If S_3=0 (e.g. Heisenberg), delta_pf=0."""
        assert planted_forest_genus_2(Fraction(1), Fraction(0)) == Fraction(0)

    def test_F2_total_includes_pf(self):
        """F_2_total = F_2_scalar + delta_pf."""
        data = genus_2_free_energy_pure_ym(3, 0)
        assert data.F_2_total == data.F_2_scalar + data.delta_pf_2

    def test_pf_su3_F2_total(self):
        """SU(3) k=0: F_2_total = 7/1440 + 1/96 = 7/1440 + 15/1440 = 11/720."""
        data = genus_2_free_energy_pure_ym(3, 0)
        # 7/1440 + 1/96 = 7/1440 + 15/1440 = 22/1440 = 11/720
        assert data.F_2_total == Fraction(11, 720)


# ========================================================================
# 8.  Form factor hierarchy
# ========================================================================

class TestFormFactorHierarchy:
    """Test the form factor / shadow tower correspondence."""

    def test_tree_level_vanishes(self):
        """g=0: F_0 = 0 (all-plus vanishes at tree level)."""
        levels = form_factor_hierarchy(3, 0, 3)
        assert levels[0].F_g_scalar == 0
        assert levels[0].loop_order == 0

    def test_one_loop_equals_genus_1(self):
        """1-loop = genus 1: F_1 = kappa/24."""
        levels = form_factor_hierarchy(3, 0, 3)
        assert levels[1].loop_order == 1
        assert levels[1].genus == 1
        assert levels[1].F_g_scalar == Fraction(4) * Fraction(1, 24)
        assert levels[1].F_g_scalar == Fraction(1, 6)

    def test_two_loop_equals_genus_2(self):
        """2-loop = genus 2: F_2 = kappa * 7/5760."""
        levels = form_factor_hierarchy(3, 0, 3)
        assert levels[2].loop_order == 2
        assert levels[2].genus == 2
        assert levels[2].F_g_scalar == Fraction(4) * Fraction(7, 5760)

    def test_genus_loop_identification(self):
        """genus = loop_order at every level."""
        levels = form_factor_hierarchy(3, 0, 5)
        for lvl in levels:
            assert lvl.genus == lvl.loop_order


# ========================================================================
# 9.  Costello comparison
# ========================================================================

class TestCostelloComparison:
    """Test the structural bridge between our F_2 and Costello's 2-loop."""

    def test_bridge_is_structural(self):
        """The match is structural (MC equation = bootstrap), not numerical."""
        comp = costello_two_loop_comparison(3, 0)
        assert comp.bridge_structural is True

    def test_costello_su3_k0(self):
        """SU(3) k=0: F_2 = 7/1440 (scalar) + 1/96 (pf) = 11/720."""
        comp = costello_two_loop_comparison(3, 0)
        assert comp.kappa == Fraction(4)
        assert comp.F_2_scalar == Fraction(7, 1440)
        assert comp.delta_pf == Fraction(1, 96)
        assert comp.F_2_shadow == Fraction(11, 720)

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_costello_F2_scalar_matches_theorem_d(self, N):
        """F_2_scalar = kappa * lambda_2^FP for all N."""
        comp = costello_two_loop_comparison(N, 0)
        assert comp.F_2_scalar == comp.kappa * _lambda_fp_exact(2)


# ========================================================================
# 10.  Large-N scaling
# ========================================================================

class TestLargeNScaling:
    """Test large-N behavior of F_2."""

    def test_kappa_scales_as_N_squared(self):
        """At large N: kappa ~ N^2/2."""
        analysis = large_N_scaling_analysis(10)
        for item in analysis:
            # kappa/(N^2) should approach 1/2
            assert item.kappa_over_N_squared == Fraction(item.N * item.N - 1,
                                                         2 * item.N * item.N)

    def test_F2_scalar_positive(self):
        """F_2_scalar > 0 for all N (kappa > 0, lambda_2 > 0)."""
        analysis = large_N_scaling_analysis(10)
        for item in analysis:
            assert item.F_2_scalar > 0

    def test_pf_to_scalar_ratio_shrinks(self):
        """Planted-forest correction is subleading at large N.
        |delta_pf/F_2_scalar| should decrease as N grows for large N."""
        analysis = large_N_scaling_analysis(10)
        # Compare N=8 vs N=10
        ratio_8 = abs(analysis[6].ratio_pf_to_scalar)
        ratio_10 = abs(analysis[8].ratio_pf_to_scalar)
        assert ratio_10 < ratio_8


# ========================================================================
# 11.  Ahat generating function
# ========================================================================

class TestAhatGeneratingFunction:
    """Verify F_g = kappa * [coefficient of hbar^{2g} in Ahat(i*hbar) - 1]."""

    def test_ahat_coefficients_match_lambda_fp(self):
        """Ahat coefficient at order 2g = lambda_g^FP."""
        for g in range(1, 6):
            assert _ahat_coefficient(g) == _lambda_fp_exact(g)

    @pytest.mark.parametrize("kappa_val", [Fraction(4), Fraction(3, 2),
                                            Fraction(15, 2), Fraction(12)])
    def test_ahat_generating_function(self, kappa_val):
        """F_g = kappa * lambda_g^FP verified via Ahat expansion."""
        results = verify_ahat_generating_function(kappa_val, 5)
        for g, data in results.items():
            assert data['match'] is True
            assert data['F_g'] == kappa_val * _lambda_fp_exact(g)


# ========================================================================
# 12.  Shadow tower
# ========================================================================

class TestShadowTower:
    """Test shadow tower for pure SU(N) YM (class L)."""

    def test_class_L_terminates_at_depth_3(self):
        """Class L: S_r = 0 for r >= 4."""
        for N in [2, 3, 4, 5]:
            tower = shadow_tower_pure_ym(N, 0, 10)
            for r in range(4, 11):
                assert tower[r] == 0

    def test_S2_equals_kappa(self):
        """S_2 = kappa for all N."""
        for N in [2, 3, 4, 5]:
            tower = shadow_tower_pure_ym(N, 0)
            assert tower[2] == kappa_affine_slN(N, 0)

    def test_S3_nonzero_for_kappa_nonzero(self):
        """S_3 != 0 when kappa != 0 (current algebra has cubic shadow)."""
        for N in [2, 3, 4, 5]:
            tower = shadow_tower_pure_ym(N, 0)
            assert tower[3] != 0


# ========================================================================
# 13.  Beilinson falsification of task claims
# ========================================================================

class TestBeilinsonFalsification:
    """Apply Beilinson principle to falsify incorrect claims in the task."""

    def test_task_kappa_su3_k1_is_wrong(self):
        """Task claims kappa(SU(3),k=1) = 4. WRONG: actual = 16/3.

        kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 32/6 = 16/3.
        The value 4 corresponds to k=0, not k=1.
        """
        assert kappa_affine_slN(3, 1) == Fraction(16, 3)
        assert kappa_affine_slN(3, 1) != Fraction(4)
        # The value 4 is for k=0:
        assert kappa_affine_slN(3, 0) == Fraction(4)

    def test_task_kappa_su2_k1_is_wrong(self):
        """Task claims kappa(SU(2),k=1) = 3/4. WRONG: actual = 9/4.

        kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4.
        There is no standard parameter giving kappa = 3/4 for sl_2.
        """
        assert kappa_affine_slN(2, 1) == Fraction(9, 4)
        assert kappa_affine_slN(2, 1) != Fraction(3, 4)

    def test_task_F2_su3_k1_is_wrong(self):
        """Task claims F_2(SU(3),k=1) = 7/1440. WRONG: 7/1440 is for k=0.

        At k=1: F_2 = (16/3)*7/5760 = 112/17280 = 7/1080.
        At k=0: F_2 = 4*7/5760 = 7/1440 (correct for k=0, not k=1).
        """
        assert kappa_affine_slN(3, 0) * _lambda_fp_exact(2) == Fraction(7, 1440)
        assert kappa_affine_slN(3, 1) * _lambda_fp_exact(2) == Fraction(7, 1080)

    def test_task_F2_su2_k1_is_wrong(self):
        """Task claims F_2(SU(2),k=1) = 7/7680. WRONG.

        At k=1: F_2 = (9/4)*7/5760 = 63/23040 = 7/2560.
        At k=0: F_2 = (3/2)*7/5760 = 21/11520 = 7/3840.
        Neither matches 7/7680.
        """
        assert kappa_affine_slN(2, 1) * _lambda_fp_exact(2) == Fraction(7, 2560)
        assert kappa_affine_slN(2, 0) * _lambda_fp_exact(2) == Fraction(7, 3840)

    def test_self_dual_level_is_k0_not_k1(self):
        """The self-dual sector of YM corresponds to k=0, not k=1.

        At k=0: the OPE has only a simple pole (no double pole),
        giving purely self-dual scattering. k=1 is the MHV tree level.
        """
        alg_k0 = make_pure_ym_algebra(3, 0)
        alg_k1 = make_pure_ym_algebra(3, 1)
        # k=0 is self-dual
        assert alg_k0.level == 0
        assert alg_k0.kappa_gauge == Fraction(4)
        # k=1 gives different kappa
        assert alg_k1.kappa_gauge == Fraction(16, 3)
        assert alg_k0.kappa_gauge != alg_k1.kappa_gauge


# ========================================================================
# 14.  Full analysis integration
# ========================================================================

class TestFullAnalysis:
    """Integration test: full_costello_2loop_analysis returns valid data."""

    def test_full_analysis_pure_ym(self):
        """Full analysis for pure SU(3) YM runs without error."""
        result = full_costello_2loop_analysis(3, 0, 0)
        assert 'algebra' in result
        assert 'genus_2' in result
        assert 'costello_comparison' in result
        assert 'form_factor_hierarchy' in result
        assert 'anomaly' in result
        assert result['algebra'].kappa_total == Fraction(4)

    def test_full_analysis_qcd(self):
        """Full analysis for SU(3) QCD with N_f=9 runs without error."""
        result = full_costello_2loop_analysis(3, 9, 0)
        assert result['algebra'].kappa_total == Fraction(-23)
        assert 'genus_2' in result
        assert 'costello_comparison' not in result  # only for N_f=0

    def test_F2_numerical_table_consistency(self):
        """F_2 table is internally consistent."""
        table = F_2_numerical_table(6, 0)
        for N in range(2, 7):
            assert table[N]['kappa'] == kappa_affine_slN(N, 0)
            assert table[N]['F_2_scalar'] == table[N]['kappa'] * Fraction(7, 5760)
            assert table[N]['F_2_total'] == table[N]['F_2_scalar'] + table[N]['delta_pf']

    def test_kappa_vs_nf_scan(self):
        """kappa_total decreases linearly with N_f."""
        table = kappa_total_vs_N_f(3, 0, 10)
        for nf in range(10):
            diff = table[nf + 1]['kappa_total'] - table[nf]['kappa_total']
            # Each additional flavor adds kappa = -3 (for SU(3))
            assert diff == Fraction(-3)
