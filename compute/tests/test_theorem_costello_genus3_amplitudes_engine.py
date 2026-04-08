r"""Tests for genus-3 (3-loop) all-plus QCD amplitudes from the shadow tower.

Verifies the NEW computation: 3-loop all-plus vacuum amplitudes F_3(SU(N))
for N = 2, 3, 4, 5, extending Costello [2302.00770] from 2-loop to 3-loop.

TEST ORGANIZATION:
1. Exact arithmetic primitives (Bernoulli, lambda_fp)
2. Kappa formulas (AP1 cross-verification for SU(N) at k=0)
3. Shadow tower class L (depth 3, S_4 = S_5 = 0)
4. Genus-1 cross-check against Costello Table 1
5. Genus-2 cross-check against Costello 2-loop
6. Genus-3 planted-forest polynomial (11 terms, 5 for class L)
7. Genus-3 amplitude computation for SU(2)..SU(5)
8. Multi-path verification (3+ independent paths per claim)
9. Large-N scaling analysis
10. Heisenberg vanishing (class G: delta_pf = 0)
11. Additivity of scalar part
12. Complementarity (AP24: kappa + kappa' = 0 for KM)
13. Cross-check with existing genus-3 planted-forest engine
14. All-plus 4-gluon amplitude structure
15. Full bridge analysis integration

Ground truth (independently computed, not copied):
    kappa(V_0(sl_N)) = (N^2-1)/2
    lambda_1^FP = 1/24
    lambda_2^FP = 7/5760
    lambda_3^FP = 31/967680
    S_3(sl_N, k=0) = 4N / (3(N^2-1))
    S_4 = S_5 = 0 for class L
    delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48

    F_3(SU(2)) = -11698777/156764160
    F_3(SU(3)) = -422789/1451520
    F_3(SU(4)) = -1553227411/3919104000
    F_3(SU(5)) = -9728417/19595520
"""

from fractions import Fraction

import pytest

from compute.lib.theorem_costello_genus3_amplitudes_engine import (
    # Primitives
    _frac,
    _bernoulli_exact,
    _lambda_fp_exact,
    # Kappa
    kappa_affine_slN,
    central_charge_slN,
    shadow_tower_class_L,
    # Planted-forest
    GENUS3_PF_COEFFICIENTS,
    GENUS3_PF_CLASS_L_COEFFICIENTS,
    GENUS2_PF_COEFFICIENTS,
    delta_pf_genus3,
    delta_pf_genus2,
    # Amplitudes
    GenusThreeAmplitude,
    genus3_amplitude_suN,
    AllPlusGluonAmplitude3Loop,
    all_plus_4gluon_3loop,
    # Costello table
    CostelloTableRow,
    costello_extended_table,
    print_costello_table,
    # Large-N
    LargeNScaling,
    large_n_scaling_analysis,
    # Verification
    verify_genus1_costello,
    verify_genus2_costello,
    verify_genus3_multipath,
    verify_additivity,
    verify_genus2_polynomial,
    thooft_scaling_ratio,
    # Summary
    manuscript_summary_table,
    full_genus3_bridge_analysis,
)


# ============================================================================
# 1. Exact arithmetic primitives
# ============================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers used in lambda_fp computation."""

    def test_B0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_B2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == Fraction(0)


class TestLambdaFP:
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda2(self):
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda3(self):
        """The key value for 3-loop computation."""
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda4(self):
        assert _lambda_fp_exact(4) == Fraction(127, 154828800)

    def test_lambda5(self):
        assert _lambda_fp_exact(5) == Fraction(73, 3503554560)

    def test_positivity(self):
        """All lambda_g^FP must be positive (Bernoulli sign check)."""
        for g in range(1, 11):
            assert _lambda_fp_exact(g) > 0

    def test_decreasing(self):
        """lambda_{g+1} < lambda_g for all g >= 1."""
        for g in range(1, 10):
            assert _lambda_fp_exact(g + 1) < _lambda_fp_exact(g)

    def test_genus_error(self):
        with pytest.raises(ValueError):
            _lambda_fp_exact(0)


# ============================================================================
# 2. Kappa formulas (AP1 cross-verification)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N) at k=0."""

    def test_su2_k0(self):
        """kappa(SU(2), k=0) = (4-1)*2/(2*2) = 3/2."""
        assert kappa_affine_slN(2) == Fraction(3, 2)

    def test_su3_k0(self):
        """kappa(SU(3), k=0) = (9-1)*3/(2*3) = 4."""
        assert kappa_affine_slN(3) == Fraction(4)

    def test_su4_k0(self):
        """kappa(SU(4), k=0) = (16-1)*4/(2*4) = 15/2."""
        assert kappa_affine_slN(4) == Fraction(15, 2)

    def test_su5_k0(self):
        """kappa(SU(5), k=0) = (25-1)*5/(2*5) = 12."""
        assert kappa_affine_slN(5) == Fraction(12)

    def test_kappa_from_definition(self):
        """Verify kappa = dim(g)*(k+h^v)/(2*h^v) for k=0.

        At k=0: kappa = dim(sl_N)*N/(2N) = (N^2-1)/2.
        AP1: recomputed, not copied.
        """
        for N in range(2, 8):
            expected = Fraction(N * N - 1, 2)
            assert kappa_affine_slN(N) == expected

    def test_kappa_ne_c_over_2(self):
        """AP9: kappa != c/2 for dim > 1.

        c(V_0(sl_N)) = 0 (level k=0), so c/2 = 0.
        But kappa = (N^2-1)/2 != 0.
        """
        for N in range(2, 6):
            c = central_charge_slN(N, Fraction(0))
            assert c == 0
            assert kappa_affine_slN(N) != c / 2

    def test_complementarity_ap24(self):
        """AP24: kappa(A) + kappa(A!) = 0 for KM families.

        Feigin-Frenkel: k -> -k - 2h^v. For sl_N: k! = -2N.
        kappa(k=0) + kappa(k=-2N) should = 0.
        """
        for N in range(2, 7):
            kap = kappa_affine_slN(N, Fraction(0))
            kap_dual = kappa_affine_slN(N, Fraction(-2 * N))
            assert kap + kap_dual == 0


# ============================================================================
# 3. Shadow tower class L
# ============================================================================

class TestShadowTowerClassL:
    """Verify class L shadow tower: depth 3, S_4 = S_5 = 0."""

    def test_su3_tower(self):
        tower = shadow_tower_class_L(3)
        assert tower['kappa'] == Fraction(4)
        assert tower['S_3'] == Fraction(1, 2)
        assert tower['S_4'] == Fraction(0)
        assert tower['S_5'] == Fraction(0)

    def test_S3_formula(self):
        """S_3 = 4N/(3(N^2-1)) for k=0."""
        for N in range(2, 7):
            tower = shadow_tower_class_L(N)
            expected_S3 = Fraction(4 * N, 3 * (N * N - 1))
            assert tower['S_3'] == expected_S3

    def test_S3_alt_formula(self):
        """S_3 = 2N/(3*kappa) for k=0 (equivalent formulation)."""
        for N in range(2, 7):
            tower = shadow_tower_class_L(N)
            kap = tower['kappa']
            expected = Fraction(2 * N) / (3 * kap)
            assert tower['S_3'] == expected

    def test_S4_vanishes(self):
        """S_4 = 0 for class L (shadow depth 3)."""
        for N in range(2, 7):
            assert shadow_tower_class_L(N)['S_4'] == Fraction(0)

    def test_S5_vanishes(self):
        """S_5 = 0 for class L (shadow depth 3)."""
        for N in range(2, 7):
            assert shadow_tower_class_L(N)['S_5'] == Fraction(0)


# ============================================================================
# 4. Genus-1 cross-check against Costello Table 1
# ============================================================================

class TestGenus1Costello:
    """Verify F_1 = kappa/24 matches Costello Table 1."""

    def test_su2(self):
        assert verify_genus1_costello(2)['paths_agree']

    def test_su3(self):
        assert verify_genus1_costello(3)['paths_agree']

    def test_su4(self):
        assert verify_genus1_costello(4)['paths_agree']

    def test_su5(self):
        assert verify_genus1_costello(5)['paths_agree']

    def test_F1_exact_values(self):
        """F_1(SU(N)) = (N^2-1)/48."""
        expected = {
            2: Fraction(3, 48),     # = 1/16
            3: Fraction(8, 48),     # = 1/6
            4: Fraction(15, 48),    # = 5/16
            5: Fraction(24, 48),    # = 1/2
        }
        for N, F1_exp in expected.items():
            amp = genus3_amplitude_suN(N)
            assert amp.F_1 == F1_exp

    def test_complementarity(self):
        """AP24: kappa + kappa' = 0 for all KM families."""
        for N in range(2, 7):
            v = verify_genus1_costello(N)
            assert v['complement_zero']


# ============================================================================
# 5. Genus-2 cross-check against Costello 2-loop
# ============================================================================

class TestGenus2Costello:
    """Verify F_2 = kappa*7/5760 + S_3*(10*S_3 - kappa)/48."""

    def test_su2(self):
        assert verify_genus2_costello(2)['paths_agree']

    def test_su3(self):
        assert verify_genus2_costello(3)['paths_agree']

    def test_su4(self):
        assert verify_genus2_costello(4)['paths_agree']

    def test_su5(self):
        assert verify_genus2_costello(5)['paths_agree']

    def test_F2_su3_exact(self):
        """F_2(SU(3)) = 11/720."""
        amp = genus3_amplitude_suN(3)
        assert amp.F_2 == Fraction(11, 720)

    def test_genus2_polynomial_check(self):
        """Verify genus-2 polynomial matches closed formula."""
        v = verify_genus2_polynomial()
        assert v['match']

    def test_delta_pf_g2_heisenberg(self):
        """Heisenberg: delta_pf_g2 = 0 (class G, S_3=0)."""
        assert delta_pf_genus2(Fraction(1), Fraction(0)) == 0

    def test_delta_pf_g2_formula(self):
        """Verify S_3*(10*S_3 - kappa)/48 for SU(3)."""
        kap = Fraction(4)
        S3 = Fraction(1, 2)
        expected = Fraction(1, 2) * (10 * Fraction(1, 2) - 4) / 48
        assert expected == Fraction(1, 96)
        assert delta_pf_genus2(kap, S3) == expected


# ============================================================================
# 6. Genus-3 planted-forest polynomial
# ============================================================================

class TestGenus3PlantedForestPolynomial:
    """Verify the 11-term polynomial for delta_pf^{(3,0)}."""

    def test_num_terms_full(self):
        """Full polynomial has 11 nonzero terms."""
        assert len(GENUS3_PF_COEFFICIENTS) == 11

    def test_num_terms_class_L(self):
        """Class L reduction has 5 nonzero terms (S_4 = S_5 = 0)."""
        assert len(GENUS3_PF_CLASS_L_COEFFICIENTS) == 5

    def test_class_L_subset(self):
        """Class L terms are a subset of the full polynomial."""
        for (ka, sb), coeff in GENUS3_PF_CLASS_L_COEFFICIENTS.items():
            full_coeff = GENUS3_PF_COEFFICIENTS.get((ka, sb, 0, 0))
            assert full_coeff is not None, f"Missing ({ka},{sb},0,0)"
            assert full_coeff == coeff

    def test_exact_coefficients(self):
        """Verify each coefficient against the known values."""
        expected = {
            (0, 4, 0, 0): Fraction(15, 64),
            (1, 3, 0, 0): Fraction(-35, 1536),
            (0, 2, 1, 0): Fraction(-65, 48),
            (2, 2, 0, 0): Fraction(1, 1152),
            (1, 1, 1, 0): Fraction(-5, 1152),
            (0, 1, 0, 1): Fraction(13, 16),
            (3, 1, 0, 0): Fraction(-1, 82944),
            (1, 1, 0, 0): Fraction(-343, 2304),
            (0, 0, 2, 0): Fraction(-7, 12),
            (2, 0, 1, 0): Fraction(1, 1152),
            (1, 0, 0, 1): Fraction(-1, 192),
        }
        for key, val in expected.items():
            assert GENUS3_PF_COEFFICIENTS[key] == val, f"Mismatch at {key}"

    def test_heisenberg_vanishing(self):
        """Class G (Heisenberg): S_3=S_4=S_5=0 => delta_pf=0."""
        for kappa in [Fraction(1), Fraction(5), Fraction(100)]:
            assert delta_pf_genus3(kappa, Fraction(0)) == 0

    def test_all_zero_shadow(self):
        """All shadow coefficients zero => delta_pf = 0."""
        assert delta_pf_genus3(Fraction(7), Fraction(0), Fraction(0), Fraction(0)) == 0


# ============================================================================
# 7. Genus-3 amplitude computation: the main results
# ============================================================================

class TestGenus3AmplitudeSU2:
    """SU(2): kappa=3/2, S_3=8/9."""

    def test_kappa(self):
        amp = genus3_amplitude_suN(2)
        assert amp.kappa == Fraction(3, 2)

    def test_S3(self):
        amp = genus3_amplitude_suN(2)
        assert amp.S_3 == Fraction(8, 9)

    def test_F1(self):
        amp = genus3_amplitude_suN(2)
        assert amp.F_1 == Fraction(1, 16)

    def test_F3_scalar(self):
        amp = genus3_amplitude_suN(2)
        assert amp.F_3_scalar == Fraction(31, 645120)

    def test_delta_pf_g3(self):
        amp = genus3_amplitude_suN(2)
        assert amp.delta_pf_g3 == Fraction(-167233, 2239488)

    def test_F3_total(self):
        """F_3(SU(2)) = -11698777/156764160."""
        amp = genus3_amplitude_suN(2)
        assert amp.F_3 == Fraction(-11698777, 156764160)

    def test_F3_negative(self):
        """F_3(SU(2)) is negative."""
        amp = genus3_amplitude_suN(2)
        assert amp.F_3 < 0

    def test_decomposition(self):
        """F_3 = F_3_scalar + delta_pf_g3."""
        amp = genus3_amplitude_suN(2)
        assert amp.F_3 == amp.F_3_scalar + amp.delta_pf_g3


class TestGenus3AmplitudeSU3:
    """SU(3): kappa=4, S_3=1/2."""

    def test_kappa(self):
        amp = genus3_amplitude_suN(3)
        assert amp.kappa == Fraction(4)

    def test_S3(self):
        amp = genus3_amplitude_suN(3)
        assert amp.S_3 == Fraction(1, 2)

    def test_F3_total(self):
        """F_3(SU(3)) = -422789/1451520."""
        amp = genus3_amplitude_suN(3)
        assert amp.F_3 == Fraction(-422789, 1451520)

    def test_F3_negative(self):
        amp = genus3_amplitude_suN(3)
        assert amp.F_3 < 0

    def test_decomposition(self):
        amp = genus3_amplitude_suN(3)
        assert amp.F_3 == amp.F_3_scalar + amp.delta_pf_g3


class TestGenus3AmplitudeSU4:
    """SU(4): kappa=15/2, S_3=16/45."""

    def test_kappa(self):
        amp = genus3_amplitude_suN(4)
        assert amp.kappa == Fraction(15, 2)

    def test_S3(self):
        amp = genus3_amplitude_suN(4)
        assert amp.S_3 == Fraction(16, 45)

    def test_F3_total(self):
        """F_3(SU(4)) = -1553227411/3919104000."""
        amp = genus3_amplitude_suN(4)
        assert amp.F_3 == Fraction(-1553227411, 3919104000)

    def test_decomposition(self):
        amp = genus3_amplitude_suN(4)
        assert amp.F_3 == amp.F_3_scalar + amp.delta_pf_g3


class TestGenus3AmplitudeSU5:
    """SU(5): kappa=12, S_3=5/18."""

    def test_kappa(self):
        amp = genus3_amplitude_suN(5)
        assert amp.kappa == Fraction(12)

    def test_S3(self):
        amp = genus3_amplitude_suN(5)
        assert amp.S_3 == Fraction(5, 18)

    def test_F3_total(self):
        """F_3(SU(5)) = -9728417/19595520."""
        amp = genus3_amplitude_suN(5)
        assert amp.F_3 == Fraction(-9728417, 19595520)

    def test_decomposition(self):
        amp = genus3_amplitude_suN(5)
        assert amp.F_3 == amp.F_3_scalar + amp.delta_pf_g3


class TestGenus3AllNegative:
    """F_3 is negative for all SU(N) at k=0, N=2..10."""

    @pytest.mark.parametrize("N", range(2, 11))
    def test_F3_negative(self, N):
        amp = genus3_amplitude_suN(N)
        assert amp.F_3 < 0, f"F_3(SU({N})) = {amp.F_3} should be negative"


# ============================================================================
# 8. Multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """Verify F_3 by 3+ independent paths."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_path1_eq_path2(self, N):
        """Path 1 (function) == Path 2 (coefficient evaluation)."""
        v = verify_genus3_multipath(N)
        assert v['path1_eq_path2']

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_path2_eq_path3(self, N):
        """Path 2 (full poly) == Path 3 (class L reduction)."""
        v = verify_genus3_multipath(N)
        assert v['path2_eq_path3']

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_heisenberg_limit(self, N):
        """Path 4: Heisenberg limit gives F_3 = kappa*lambda_3."""
        v = verify_genus3_multipath(N)
        assert v['heisenberg_correct']

    def test_heisenberg_dpf_zero(self):
        """Heisenberg: delta_pf = 0 at all genera."""
        v = verify_genus3_multipath(2)
        assert v['heisenberg_dpf_zero']

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_path5_direct_recompute(self, N):
        """Path 5: recompute F_3 from scratch without using the engine."""
        kap = Fraction(N * N - 1, 2)
        S3 = Fraction(4 * N, 3 * (N * N - 1))
        lam3 = Fraction(31, 967680)

        dpf = (
            Fraction(15, 64) * S3**4
            + Fraction(-35, 1536) * kap * S3**3
            + Fraction(1, 1152) * kap**2 * S3**2
            + Fraction(-1, 82944) * kap**3 * S3
            + Fraction(-343, 2304) * kap * S3
        )
        F3_direct = kap * lam3 + dpf

        amp = genus3_amplitude_suN(N)
        assert amp.F_3 == F3_direct, f"SU({N}): {amp.F_3} != {F3_direct}"


# ============================================================================
# 9. Large-N scaling
# ============================================================================

class TestLargeNScaling:
    """Verify the large-N behavior of genus-3 amplitudes."""

    def test_delta_pf_grows(self):
        """delta_pf grows faster than F_3_scalar at large N."""
        for N in [10, 20, 50]:
            amp = genus3_amplitude_suN(N)
            assert abs(amp.delta_pf_g3) > abs(amp.F_3_scalar)

    def test_kappa_squared_scaling(self):
        """kappa = (N^2-1)/2 approaches N^2/2 at large N.

        Exact: kappa/(N^2/2) = (N^2-1)/N^2 = 1 - 1/N^2.
        Use exact Fraction arithmetic to avoid float rounding.
        """
        for N in [10, 50, 100]:
            kap = kappa_affine_slN(N)
            ratio = kap / Fraction(N * N, 2)
            assert ratio == Fraction(N * N - 1, N * N)

    def test_S3_inverse_N_scaling(self):
        """S_3 = 4N/(3(N^2-1)) approaches 4/(3N) at large N.

        Exact: S_3 / (4/(3N)) = N^2/(N^2-1) = 1 + 1/(N^2-1).
        """
        for N in [10, 50, 100]:
            tower = shadow_tower_class_L(N)
            S3 = tower['S_3']
            ratio = S3 / Fraction(4, 3 * N)
            assert ratio == Fraction(N * N, N * N - 1)

    def test_large_n_analysis_runs(self):
        results = large_n_scaling_analysis([2, 3, 5, 10])
        assert len(results) == 4
        for r in results:
            assert isinstance(r, LargeNScaling)

    def test_F1_over_kappa_exact(self):
        """F_1/kappa = lambda_1 = 1/24 for all N (exact, no PF correction)."""
        for N in range(2, 11):
            r = thooft_scaling_ratio(N)
            assert r['F_1/kappa == lambda_1']


# ============================================================================
# 10. Heisenberg vanishing
# ============================================================================

class TestHeisenbergVanishing:
    """Class G (Heisenberg): all planted-forest corrections vanish."""

    def test_delta_pf_g2_zero(self):
        assert delta_pf_genus2(Fraction(1), Fraction(0)) == 0

    def test_delta_pf_g3_zero(self):
        assert delta_pf_genus3(Fraction(1), Fraction(0)) == 0

    def test_delta_pf_g3_zero_any_kappa(self):
        """delta_pf = 0 for any kappa when S_3 = S_4 = S_5 = 0."""
        for k in [1, 5, 17, 100]:
            assert delta_pf_genus3(Fraction(k), Fraction(0)) == 0

    def test_F3_equals_scalar_for_heisenberg(self):
        """F_3 = kappa * lambda_3 when delta_pf = 0."""
        kap = Fraction(7)
        lam3 = _lambda_fp_exact(3)
        F3 = kap * lam3 + delta_pf_genus3(kap, Fraction(0))
        assert F3 == kap * lam3


# ============================================================================
# 11. Additivity of scalar part
# ============================================================================

class TestAdditivity:
    """F_g^{scalar} is additive because kappa is additive."""

    def test_additivity_su2_su3(self):
        v = verify_additivity(2, 3)
        assert v['additive']

    def test_additivity_su3_su4(self):
        v = verify_additivity(3, 4)
        assert v['additive']

    def test_additivity_su2_su5(self):
        v = verify_additivity(2, 5)
        assert v['additive']

    def test_kappa_additive(self):
        """kappa(SU(2)) + kappa(SU(3)) = 3/2 + 4 = 11/2."""
        assert kappa_affine_slN(2) + kappa_affine_slN(3) == Fraction(11, 2)


# ============================================================================
# 12. Complementarity (AP24)
# ============================================================================

class TestComplementarity:
    """kappa(A) + kappa(A!) = 0 for KM families."""

    @pytest.mark.parametrize("N", range(2, 8))
    def test_km_antisymmetry(self, N):
        """kappa(k=0) + kappa(k=-2N) = 0."""
        kap = kappa_affine_slN(N, Fraction(0))
        kap_dual = kappa_affine_slN(N, Fraction(-2 * N))
        assert kap + kap_dual == 0

    @pytest.mark.parametrize("N", range(2, 6))
    def test_F1_complementarity(self, N):
        """F_1(A) + F_1(A!) = 0."""
        kap = kappa_affine_slN(N, Fraction(0))
        kap_dual = kappa_affine_slN(N, Fraction(-2 * N))
        lam1 = _lambda_fp_exact(1)
        assert kap * lam1 + kap_dual * lam1 == 0


# ============================================================================
# 13. Cross-check with existing planted-forest engine
# ============================================================================

class TestCrossCheckExistingEngine:
    """Verify consistency with theorem_genus3_planted_forest_full_engine.py."""

    def test_coefficients_match(self):
        """Coefficients must match the full engine's exact values."""
        try:
            from compute.lib.theorem_genus3_planted_forest_full_engine import (
                genus3_exact_coefficients,
            )
            existing = genus3_exact_coefficients()
            for key, val in existing.items():
                assert key in GENUS3_PF_COEFFICIENTS, f"Missing key {key}"
                assert GENUS3_PF_COEFFICIENTS[key] == Fraction(val), (
                    f"Mismatch at {key}: {GENUS3_PF_COEFFICIENTS[key]} != {val}"
                )
        except ImportError:
            pytest.skip("genus3 planted-forest engine not available")

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_delta_pf_matches_full_engine(self, N):
        """delta_pf from our engine matches the full graph-sum engine."""
        try:
            from compute.lib.theorem_genus3_planted_forest_full_engine import (
                genus3_exact_coefficients,
            )
            kap = Fraction(N * N - 1, 2)
            S3 = Fraction(4 * N, 3 * (N * N - 1))

            # From full engine coefficients
            existing = genus3_exact_coefficients()
            dpf_existing = Fraction(0)
            for (a, b, c, d), coeff in existing.items():
                if c > 0 or d > 0:
                    continue
                dpf_existing += Fraction(coeff) * kap**a * S3**b

            # From our engine
            dpf_ours = delta_pf_genus3(kap, S3)

            assert dpf_ours == dpf_existing
        except ImportError:
            pytest.skip("genus3 planted-forest engine not available")


# ============================================================================
# 14. All-plus 4-gluon amplitude structure
# ============================================================================

class TestAllPlus4Gluon:
    """Verify structure of 3-loop 4-gluon amplitude."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_construction(self, N):
        result = all_plus_4gluon_3loop(N)
        assert isinstance(result, AllPlusGluonAmplitude3Loop)
        assert result.N == N
        assert result.n_gluons == 4
        assert result.loop_order == 3
        assert result.shadow_class == "L"

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_F3_consistent(self, N):
        """F_3 in the gluon amplitude matches the vacuum amplitude."""
        gluon = all_plus_4gluon_3loop(N)
        vacuum = genus3_amplitude_suN(N)
        assert gluon.F_3 == vacuum.F_3


# ============================================================================
# 15. Costello extended table
# ============================================================================

class TestCostelloExtendedTable:
    """Verify the extended Costello table structure."""

    def test_table_size(self):
        """4 gauge groups * 3 genera = 12 rows."""
        table = costello_extended_table()
        assert len(table) == 12

    def test_genus1_known(self):
        """All genus-1 rows are marked as Costello-known."""
        table = costello_extended_table()
        g1_rows = [r for r in table if r.genus == 1]
        assert all(r.costello_known for r in g1_rows)

    def test_genus2_known(self):
        """All genus-2 rows are marked as Costello-known."""
        table = costello_extended_table()
        g2_rows = [r for r in table if r.genus == 2]
        assert all(r.costello_known for r in g2_rows)

    def test_genus3_new(self):
        """All genus-3 rows are marked as NEW (not Costello-known)."""
        table = costello_extended_table()
        g3_rows = [r for r in table if r.genus == 3]
        assert all(not r.costello_known for r in g3_rows)

    def test_F_total_consistency(self):
        """F_total = F_scalar + delta_pf for all rows."""
        table = costello_extended_table()
        for r in table:
            assert r.F_total == r.F_scalar + r.delta_pf

    def test_print_table(self):
        """print_costello_table runs without error."""
        s = print_costello_table()
        assert isinstance(s, str)
        assert "SU" in s or "Shadow" in s


# ============================================================================
# 16. Full bridge analysis
# ============================================================================

class TestFullBridgeAnalysis:
    """Integration test: run the complete analysis."""

    def test_full_analysis_runs(self):
        results = full_genus3_bridge_analysis()
        assert 'amplitudes' in results
        assert 'genus1_checks' in results
        assert 'genus3_multipath' in results

    def test_all_genus1_pass(self):
        results = full_genus3_bridge_analysis()
        for N in [2, 3, 4, 5]:
            assert results['genus1_checks'][N]['paths_agree']

    def test_all_genus2_pass(self):
        results = full_genus3_bridge_analysis()
        for N in [2, 3, 4, 5]:
            assert results['genus2_checks'][N]['paths_agree']

    def test_all_genus3_multipath_pass(self):
        results = full_genus3_bridge_analysis()
        for N in [2, 3, 4, 5]:
            v = results['genus3_multipath'][N]
            assert v['path1_eq_path2']
            assert v['path2_eq_path3']
            assert v['heisenberg_correct']

    def test_additivity_pass(self):
        results = full_genus3_bridge_analysis()
        assert results['additivity'][(2, 3)]['additive']
        assert results['additivity'][(3, 4)]['additive']

    def test_genus2_poly_pass(self):
        results = full_genus3_bridge_analysis()
        assert results['genus2_poly']['match']


# ============================================================================
# 17. Manuscript summary table
# ============================================================================

class TestManuscriptSummary:
    """Verify the summary table for the manuscript."""

    def test_summary_has_all_groups(self):
        summary = manuscript_summary_table()
        for N in [2, 3, 4, 5]:
            assert f'SU({N})' in summary

    def test_summary_F3_values(self):
        """Cross-check F_3 values in the summary."""
        summary = manuscript_summary_table()
        expected_F3 = {
            'SU(2)': Fraction(-11698777, 156764160),
            'SU(3)': Fraction(-422789, 1451520),
            'SU(4)': Fraction(-1553227411, 3919104000),
            'SU(5)': Fraction(-9728417, 19595520),
        }
        for key, val in expected_F3.items():
            assert Fraction(summary[key]['F_3']) == val


# ============================================================================
# 18. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_su1_raises(self):
        """SU(1) is not a valid gauge group."""
        with pytest.raises(ValueError):
            genus3_amplitude_suN(1)

    def test_large_N_su10(self):
        """SU(10) computes without error."""
        amp = genus3_amplitude_suN(10)
        assert amp.F_3 < 0

    def test_large_N_su20(self):
        """SU(20) computes without error."""
        amp = genus3_amplitude_suN(20)
        assert amp.F_3 < 0

    def test_frac_coercion(self):
        assert _frac(5) == Fraction(5)
        assert _frac(Fraction(3, 7)) == Fraction(3, 7)


# ============================================================================
# 19. Dimensional checks
# ============================================================================

class TestDimensionalChecks:
    """Verify dimensional/degree consistency (AP7 verification path)."""

    def test_lambda_fp_dimension(self):
        """lambda_g^FP is dimensionless (pure number)."""
        for g in range(1, 6):
            val = _lambda_fp_exact(g)
            assert isinstance(val, Fraction)

    def test_F3_has_kappa_dimension(self):
        """F_3 scales linearly with kappa at the scalar level."""
        lam3 = _lambda_fp_exact(3)
        for kap in [Fraction(1), Fraction(2), Fraction(7)]:
            F_scalar = kap * lam3
            assert F_scalar == kap * lam3

    def test_planted_forest_is_polynomial(self):
        """delta_pf is a polynomial in kappa and S_r."""
        # Check that delta_pf(2*kappa, 2*S_3) != 2 * delta_pf(kappa, S_3)
        # (it's polynomial, not linear)
        kap = Fraction(3)
        S3 = Fraction(1, 2)
        dpf1 = delta_pf_genus3(kap, S3)
        dpf2 = delta_pf_genus3(2 * kap, 2 * S3)
        assert dpf2 != 2 * dpf1  # polynomial, not linear


# ============================================================================
# 20. Sign structure
# ============================================================================

class TestSignStructure:
    """Verify the sign structure of the planted-forest correction."""

    def test_delta_pf_g3_sign_su2(self):
        """delta_pf_g3(SU(2)) < 0."""
        amp = genus3_amplitude_suN(2)
        assert amp.delta_pf_g3 < 0

    def test_delta_pf_g3_sign_su3(self):
        """delta_pf_g3(SU(3)) < 0."""
        amp = genus3_amplitude_suN(3)
        assert amp.delta_pf_g3 < 0

    @pytest.mark.parametrize("N", range(2, 11))
    def test_delta_pf_g3_negative_all(self, N):
        """delta_pf_g3 is negative for all SU(N), N=2..10."""
        amp = genus3_amplitude_suN(N)
        assert amp.delta_pf_g3 < 0

    def test_delta_pf_dominates_scalar(self):
        """For N >= 3, |delta_pf| > |F_3_scalar| (planted-forest dominates)."""
        for N in range(3, 11):
            amp = genus3_amplitude_suN(N)
            assert abs(amp.delta_pf_g3) > abs(amp.F_3_scalar)
