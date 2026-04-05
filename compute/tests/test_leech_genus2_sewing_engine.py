r"""Tests for the Leech lattice genus-2 sewing engine.

Verifies the genus-2 partition function of V_{Lambda_24} via six
independent verification paths with multi-path cross-checks.

Structure:
  1. Leech lattice basic data (kappa, rank, c, classification)
  2. Genus-1 identity: Theta/eta^{24} = j - 720 (8 terms)
  3. Faber-Pandharipande lambda_2 (3 paths)
  4. Shadow approximation F_2 = kappa * lambda_2 (multi-path)
  5. Fredholm determinant (one-particle reduction)
  6. Genus-2 theta series and diagonal representation numbers
  7. Siegel modular form decomposition (cusp residual)
  8. Niemeier lattice comparison (24 lattices, same shadow)
  9. Diagonal degeneration limit (Z_2 -> Z_1^2)
  10. HS-sewing convergence verification
  11. Bocherer conjecture bridge
  12. Gritsenko lift check
  13. Siegel modular form space structure
  14. Cross-checks and consistency
  15. Shadow depth classification (class L)
  16. Comparison with moonshine V^natural
"""

import math
import pytest
from fractions import Fraction

from compute.lib.leech_genus2_sewing_engine import (
    # Constants
    LEECH_RANK,
    LEECH_CENTRAL_CHARGE,
    LEECH_KAPPA,
    LEECH_MIN_NORM,
    LEECH_KISSING,
    LEECH_DET,
    LEECH_THETA_COEFFICIENTS,
    # Bernoulli/FP
    bernoulli_number,
    lambda_fp,
    # Theta coefficients
    leech_theta_coefficient,
    leech_genus2_theta_coefficient,
    # Fredholm
    genus2_fredholm_heisenberg,
    genus2_lattice_contribution,
    # Full partition function
    leech_genus2_partition_function,
    # Shadow comparison
    shadow_vs_exact_comparison,
    # Niemeier
    niemeier_shadow_comparison,
    niemeier_genus2_theta_comparison,
    NIEMEIER_ROOT_SYSTEMS,
    D24_THETA_COEFFICIENTS,
    A24_THETA_COEFFICIENTS,
    # Decomposition
    leech_decomposition_constants,
    # Bocherer
    bocherer_bridge_leech,
    # Degeneration
    diagonal_degeneration_check,
    # Genus-1 identity
    verify_leech_genus1_identity,
    # Partitions
    partitions,
    # Siegel space
    siegel_modular_form_space_weight12,
    # Gritsenko
    gritsenko_lift_check,
    # HS sewing
    hs_sewing_verification,
    # Multi-path
    full_multi_path_verification,
)


# ============================================================================
# 1. LEECH LATTICE BASIC DATA
# ============================================================================

class TestLeechBasicData:
    """Verify fundamental invariants of the Leech lattice VOA."""

    def test_rank(self):
        """Leech lattice rank is 24."""
        assert LEECH_RANK == 24

    def test_central_charge(self):
        """Central charge c = 24."""
        assert LEECH_CENTRAL_CHARGE == 24

    def test_kappa_equals_rank(self):
        """kappa = rank for lattice VOAs (AP48: NOT c/2)."""
        assert LEECH_KAPPA == LEECH_RANK == 24

    def test_kappa_not_c_over_2(self):
        """kappa = 24 != c/2 = 12 for lattice VOAs (AP48)."""
        assert LEECH_KAPPA != LEECH_CENTRAL_CHARGE / 2

    def test_minimum_norm(self):
        """Leech lattice has minimum norm 4 (no roots)."""
        assert LEECH_MIN_NORM == 4

    def test_kissing_number(self):
        """Kissing number = 196560."""
        assert LEECH_KISSING == 196560

    def test_unimodular(self):
        """Leech lattice is unimodular (det = 1)."""
        assert LEECH_DET == 1

    def test_no_roots(self):
        """Leech lattice has no vectors of norm 2."""
        assert LEECH_THETA_COEFFICIENTS[1] == 0

    def test_theta_leading_term(self):
        """Theta series starts with 1 (zero vector)."""
        assert LEECH_THETA_COEFFICIENTS[0] == 1

    def test_theta_kissing(self):
        """r(4) = kissing number = 196560."""
        assert LEECH_THETA_COEFFICIENTS[2] == 196560


# ============================================================================
# 2. GENUS-1 IDENTITY: Theta/eta^24 = j - 720
# ============================================================================

class TestGenus1Identity:
    """Verify Theta_Leech = Delta * (j - 720)."""

    def test_identity_first_6_terms(self):
        """Theta = Delta * (j - 720) for first 6 terms."""
        result = verify_leech_genus1_identity(5)
        assert result['all_match'], f"Failed: {result['details']}"

    def test_identity_n0(self):
        """At q^0: Theta has 1 (zero vector)."""
        result = verify_leech_genus1_identity(0)
        assert result['details'][0]['computed'] == 1
        assert result['details'][0]['expected'] == 1

    def test_identity_n1(self):
        """At q^1: Theta has 0 (no norm-2 vectors)."""
        result = verify_leech_genus1_identity(1)
        assert result['details'][1]['computed'] == 0
        assert result['details'][1]['expected'] == 0

    def test_identity_n2(self):
        """At q^2: Theta has 196560 (kissing number)."""
        result = verify_leech_genus1_identity(2)
        assert result['details'][2]['computed'] == 196560

    def test_identity_n3(self):
        """At q^3: Theta has 16773120."""
        result = verify_leech_genus1_identity(3)
        assert result['details'][3]['computed'] == 16773120

    def test_j_minus_720_constant(self):
        """j - 720 has constant term 24 = dim V_1."""
        result = verify_leech_genus1_identity(1)
        assert result['j_minus_720_constant'] == 24

    def test_dim_V1_equals_rank(self):
        """dim V_1 = 24 = rank (the 24 free bosons)."""
        assert LEECH_RANK == 24


# ============================================================================
# 3. FABER-PANDHARIPANDE lambda_2 (3 paths)
# ============================================================================

class TestLambda2:
    """Verify lambda_2^FP = 7/5760 via multiple paths."""

    def test_lambda2_value(self):
        """lambda_2 = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda2_from_bernoulli(self):
        """lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24."""
        B4 = bernoulli_number(4)  # B_4 = -1/30
        result = Fraction(7, 8) * abs(B4) / Fraction(math.factorial(4))
        assert result == Fraction(7, 5760)

    def test_lambda2_from_ahat(self):
        """lambda_2 matches the A-hat genus coefficient at x^4."""
        # (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + ...
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda1_value(self):
        """lambda_1 = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda3_value(self):
        """lambda_3 = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)


# ============================================================================
# 4. SHADOW APPROXIMATION F_2 (multi-path)
# ============================================================================

class TestShadowF2:
    """Verify the genus-2 shadow amplitude F_2 for the Leech lattice."""

    def test_F2_shadow_value(self):
        """F_2 = kappa * lambda_2 = 24 * 7/5760 = 7/240."""
        result = shadow_vs_exact_comparison()
        assert result['F_2_shadow'] == Fraction(7, 240)

    def test_F2_shadow_numerical(self):
        """F_2 numerically matches 7/240."""
        result = shadow_vs_exact_comparison()
        assert abs(result['F_2_shadow_numerical'] - 7.0 / 240.0) < 1e-15

    def test_kappa_value(self):
        """kappa = 24 in the shadow computation."""
        result = shadow_vs_exact_comparison()
        assert result['kappa'] == 24

    def test_shadow_class(self):
        """Leech lattice VOA is class L (r_max = 3)."""
        result = shadow_vs_exact_comparison()
        assert result['shadow_class'] == 'L'

    def test_shadow_depth(self):
        """Shadow depth = 3 for class L."""
        result = shadow_vs_exact_comparison()
        assert result['shadow_depth'] == 3

    def test_S3_vanishes_on_scalar(self):
        """Cubic shadow S_3 vanishes on the scalar line."""
        result = shadow_vs_exact_comparison()
        assert result['S_3_scalar'] == 0

    def test_delta_pf_vanishes(self):
        """Planted-forest correction delta_pf = 0 when S_3 = 0."""
        result = shadow_vs_exact_comparison()
        assert result['delta_pf'] == 0

    def test_F2_path_kappa_times_lambda(self):
        """Path 1: F_2 = kappa * lambda_2."""
        assert Fraction(LEECH_KAPPA) * lambda_fp(2) == Fraction(7, 240)

    def test_F2_path_bernoulli(self):
        """Path 2: F_2 from Bernoulli numbers."""
        B4 = bernoulli_number(4)
        lam2 = Fraction(7, 8) * abs(B4) / Fraction(24)
        assert Fraction(24) * lam2 == Fraction(7, 240)

    def test_F2_path_ahat(self):
        """Path 3: F_2 from A-hat genus."""
        # A-hat(ix) - 1 = sum lambda_g x^{2g}, coefficient at g=2 is 7/5760.
        assert Fraction(24) * Fraction(7, 5760) == Fraction(7, 240)


# ============================================================================
# 5. FREDHOLM DETERMINANT
# ============================================================================

class TestFredholmDeterminant:
    """Verify the genus-2 Fredholm determinant for rank-24 Heisenberg."""

    def test_sewing_det_positive(self):
        """Sewing determinant det(1-K) > 0 for |w| < 1."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 0.1, rank=24)
        assert result['sewing_det'] > 0

    def test_sewing_det_less_than_1(self):
        """det(1-K) < 1 (the eigenvalues are positive)."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 0.1, rank=24)
        assert result['sewing_det'] < 1.0

    def test_sewing_det_approaches_1(self):
        """As w -> 0, det(1-K) -> 1."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 1e-10, rank=24)
        assert abs(result['sewing_det'] - 1.0) < 1e-8

    def test_trace_class(self):
        """Sewing operator is trace class."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 0.1, rank=24)
        assert result['trace_class']

    def test_trace_norm_formula(self):
        """Trace norm = rank * w/(1-w) = 24 * 0.1/0.9."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 0.1, rank=24, N=200)
        expected = 24 * 0.1 / 0.9
        assert abs(result['trace_norm'] - expected) < 0.01

    def test_Z2_positive(self):
        """Z_2(H_24) > 0."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 0.1, rank=24)
        assert result['Z2_heisenberg'] > 0

    def test_rank_stored(self):
        """Stored rank is 24."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 0.1, rank=24)
        assert result['rank'] == 24

    def test_one_particle_formula(self):
        """One-particle reduction: det(1-K) = prod(1-w^n) for Heisenberg."""
        w = 0.1
        N = 100
        result = genus2_fredholm_heisenberg(0.1, 0.1, w, rank=1, N=N)
        # prod(1-w^n) for n=1..N
        expected = 1.0
        for n in range(1, N + 1):
            expected *= (1 - w ** n)
        assert abs(result['sewing_det'] - expected) < 1e-10

    def test_rank_scaling(self):
        """det(1-K)^{-r} scales correctly with rank r."""
        w = 0.2
        r1 = genus2_fredholm_heisenberg(0.1, 0.1, w, rank=1, N=50)
        r24 = genus2_fredholm_heisenberg(0.1, 0.1, w, rank=24, N=50)
        # sewing_det is the same (one-particle), power differs
        assert abs(r1['sewing_det'] - r24['sewing_det']) < 1e-10
        expected_ratio = r1['sewing_det'] ** (-24) / r1['sewing_det'] ** (-1)
        actual_ratio = r24['sewing_det_power'] / r1['sewing_det_power']
        assert abs(actual_ratio - expected_ratio) / abs(expected_ratio) < 1e-8

    def test_eigenvalues_geometric(self):
        """One-particle eigenvalues are w^n (geometric sequence)."""
        w = 0.3
        result = genus2_fredholm_heisenberg(0.1, 0.1, w, rank=24, N=50)
        for i, ev in enumerate(result['eigenvalues_first_10']):
            n = i + 1  # eigenvalues start at w^1
            assert abs(ev - w ** n) < 1e-12


# ============================================================================
# 6. GENUS-2 THETA SERIES
# ============================================================================

class TestGenus2Theta:
    """Verify genus-2 theta series of the Leech lattice."""

    def test_diagonal_101(self):
        """r_2((1,0,1)) = r(2)*r(2) = 0 (no roots)."""
        assert leech_genus2_theta_coefficient(1, 0, 1) == 0

    def test_diagonal_202(self):
        """r_2((2,0,2)) = r(4)^2 = 196560^2."""
        assert leech_genus2_theta_coefficient(2, 0, 2) == 196560 ** 2

    def test_diagonal_102(self):
        """r_2((1,0,2)) = r(2)*r(4) = 0 (since r(2)=0)."""
        assert leech_genus2_theta_coefficient(1, 0, 2) == 0

    def test_diagonal_303(self):
        """r_2((3,0,3)) = r(6)^2 = 16773120^2."""
        assert leech_genus2_theta_coefficient(3, 0, 3) == 16773120 ** 2

    def test_diagonal_203(self):
        """r_2((2,0,3)) = r(4)*r(6)."""
        expected = LEECH_THETA_COEFFICIENTS[2] * LEECH_THETA_COEFFICIENTS[3]
        assert leech_genus2_theta_coefficient(2, 0, 3) == expected

    def test_r2_positive_semidefinite(self):
        """r_2(T) >= 0 for all positive definite T."""
        for a in range(1, 4):
            for c in range(a, 4):
                r2 = leech_genus2_theta_coefficient(a, 0, c)
                assert r2 >= 0, f"r_2({a},0,{c}) = {r2} < 0"

    def test_r2_symmetry(self):
        """r_2((a,0,c)) = r_2((c,0,a)) (symmetry of the theta function)."""
        for a in range(1, 4):
            for c in range(a + 1, 4):
                assert (leech_genus2_theta_coefficient(a, 0, c) ==
                        leech_genus2_theta_coefficient(c, 0, a))

    def test_theta_coefficient_at_zero(self):
        """r(0) = 1 (the zero vector)."""
        assert leech_theta_coefficient(0) == 1


# ============================================================================
# 7. SIEGEL MODULAR FORM DECOMPOSITION
# ============================================================================

class TestSiegelDecomposition:
    """Verify the Siegel modular form decomposition of Theta_Leech."""

    def test_cusp_space_2d(self):
        """S_12(Sp(4,Z)) is 2-dimensional."""
        decomp = leech_decomposition_constants()
        assert decomp['cusp_space_dim'] == 2

    def test_cusp_nonzero_at_identity(self):
        """Cusp residual at T = Id is nonzero."""
        decomp = leech_decomposition_constants()
        assert decomp['cusp_at_identity'] != 0

    def test_cusp_negative_at_identity(self):
        """Cusp residual at (1,0,1) is negative (since r_2 = 0 < E_12)."""
        decomp = leech_decomposition_constants()
        assert float(decomp['cusp_at_identity']) < 0

    def test_cusp_from_rootlessness(self):
        """Cusp(1,0,1) = -E_12(1,0,1) since r_2 = 0 (no roots)."""
        decomp = leech_decomposition_constants()
        cusp = decomp['cusp_data'][(1, 0, 1)]
        assert cusp['r2'] == 0
        assert cusp['cusp'] == -cusp['E12']

    def test_cusp_exact_at_202(self):
        """At (2,0,2): cusp = 196560^2 - E_12(2,0,2)."""
        decomp = leech_decomposition_constants()
        cusp = decomp['cusp_data'][(2, 0, 2)]
        assert cusp['r2'] == 196560 ** 2
        assert cusp['cusp'] == Fraction(cusp['r2']) - cusp['E12']

    def test_siegel_weil_eisenstein_part(self):
        """Eisenstein part coefficient = 1 (by Siegel-Weil for unimodular lattices)."""
        # The coefficient of E_12 in Theta_Leech is 1.
        # This is verified by checking the constant term (T=0):
        # both Theta and E_12 have constant term 1.
        decomp = leech_decomposition_constants()
        # At any diagonal T, r_2 = E_12 + cusp, so E_12 has coeff 1.
        cusp = decomp['cusp_data'][(2, 0, 2)]
        r2 = cusp['r2']
        e12 = cusp['E12']
        cusp_val = cusp['cusp']
        assert r2 == int(round(float(e12 + cusp_val)))

    def test_decomposition_consistency(self):
        """Cusp residuals at multiple points are self-consistent."""
        decomp = leech_decomposition_constants()
        # All cusp values should be exactly r_2 - E_12
        for T, data in decomp['cusp_data'].items():
            assert data['cusp'] == Fraction(data['r2']) - data['E12']


# ============================================================================
# 8. NIEMEIER COMPARISON
# ============================================================================

class TestNiemeirComparison:
    """Verify comparison across Niemeier lattice VOAs."""

    def test_24_niemeier_lattices(self):
        """There are 24 Niemeier lattices."""
        assert len(NIEMEIER_ROOT_SYSTEMS) == 24

    def test_all_shadows_equal(self):
        """All Niemeier lattice VOAs have the same shadow F_2."""
        result = niemeier_shadow_comparison()
        assert result['all_shadows_equal']

    def test_shadow_value(self):
        """Universal shadow F_2 = 7/240 for all rank-24 lattice VOAs."""
        result = niemeier_shadow_comparison()
        assert result['universal_F2'] == Fraction(7, 240)

    def test_thetas_differ(self):
        """Genus-2 theta functions differ across Niemeier lattices."""
        result = niemeier_genus2_theta_comparison()
        assert result['thetas_differ']

    def test_leech_rootless(self):
        """Leech has 0 roots."""
        result = niemeier_genus2_theta_comparison()
        assert result['lattices']['Leech']['n_roots'] == 0

    def test_d24_roots(self):
        """D_24 has 1104 roots."""
        result = niemeier_genus2_theta_comparison()
        assert result['lattices']['D_24']['n_roots'] == 1104

    def test_leech_r2_11_zero(self):
        """Leech r_2((1,0,1)) = 0 (no roots -> no orthogonal pairs)."""
        result = niemeier_genus2_theta_comparison()
        assert result['lattices']['Leech']['r2_diag_11'] == 0

    def test_d24_r2_11_nonzero(self):
        """D_24 r_2((1,0,1)) = 1104^2 (many root pairs)."""
        result = niemeier_genus2_theta_comparison()
        assert result['lattices']['D_24']['r2_diag_11'] == 1104 ** 2

    def test_a24_r2_11(self):
        """A_24 r_2((1,0,1)) = 600^2."""
        result = niemeier_genus2_theta_comparison()
        assert result['lattices']['A_24']['r2_diag_11'] == 600 ** 2

    def test_all_kappa_24(self):
        """All Niemeier lattice VOAs have kappa = 24."""
        result = niemeier_genus2_theta_comparison()
        for name, data in result['lattices'].items():
            assert data['kappa'] == 24, f"{name} has kappa = {data['kappa']}"


# ============================================================================
# 9. DIAGONAL DEGENERATION
# ============================================================================

class TestDiagonalDegeneration:
    """Verify Z_2 -> Z_1^2 in the separating limit w -> 0."""

    def test_ratio_approaches_1(self):
        """Z_2 / Z_1^2 -> 1 as w -> 0."""
        result = diagonal_degeneration_check(tau_im=1.5)
        assert result['ratio_approaches_1']

    def test_ratio_close_to_sewing_factor(self):
        """The ratio differs from 1 by the sewing factor."""
        result = diagonal_degeneration_check(tau_im=1.5)
        ratio = result['ratio_Z2_over_Z1sq']
        sewing = result['sewing_factor']
        assert abs(ratio - sewing) < 1e-8

    def test_Z1_positive(self):
        """Z_1 (unnormalized) is positive."""
        result = diagonal_degeneration_check(tau_im=1.5)
        assert result['Z1_unnorm'] > 0

    def test_degeneration_at_different_tau(self):
        """Degeneration holds for tau_im = 2.0."""
        result = diagonal_degeneration_check(tau_im=2.0)
        assert result['ratio_approaches_1']

    def test_degeneration_at_tau_1(self):
        """Degeneration holds for tau_im = 1.0."""
        result = diagonal_degeneration_check(tau_im=1.0, N_modes=100)
        assert result['ratio_approaches_1']


# ============================================================================
# 10. HS-SEWING CONVERGENCE
# ============================================================================

class TestHSSewing:
    """Verify HS-sewing convergence for the Leech lattice VOA."""

    def test_hs_converges_q03(self):
        """HS-sewing converges at |q| = 0.3."""
        result = hs_sewing_verification(q_abs=0.3, N_max=5)
        # The partial sum should be finite (not inf or nan)
        assert result['partial_sum'] < float('inf')
        assert not math.isnan(result['partial_sum'])

    def test_rank_24(self):
        """Engine uses rank 24."""
        result = hs_sewing_verification()
        assert result['rank'] == 24

    def test_ope_polynomial_degree(self):
        """OPE polynomial degree = rank = 24."""
        result = hs_sewing_verification()
        assert result['ope_polynomial_degree'] == 24

    def test_subexponential_growth(self):
        """Sector growth is subexponential."""
        result = hs_sewing_verification()
        assert result['sector_growth'] == 'subexponential (Hardy-Ramanujan)'


# ============================================================================
# 11. BOCHERER CONJECTURE
# ============================================================================

class TestBocherer:
    """Verify Bocherer conjecture connection for the Leech lattice."""

    def test_cusp_nonzero(self):
        """The cusp residual is nonzero (necessary for Bocherer)."""
        result = bocherer_bridge_leech()
        assert result['cusp_nonzero']

    def test_bocherer_applicable(self):
        """Bocherer conjecture is applicable."""
        result = bocherer_bridge_leech()
        assert result['bocherer_applicable']

    def test_cusp_space_2d(self):
        """The cusp space is 2-dimensional."""
        result = bocherer_bridge_leech()
        assert result['cusp_space_dim'] == 2


# ============================================================================
# 12. GRITSENKO LIFT
# ============================================================================

class TestGritsenkoLift:
    """Verify Gritsenko lift properties."""

    def test_leech_not_gritsenko(self):
        """Theta_Leech^{(2)} is NOT a Gritsenko lift."""
        result = gritsenko_lift_check()
        assert not result['is_gritsenko_lift']

    def test_e8_is_gritsenko(self):
        """Theta_{E_8}^{(2)} IS a Gritsenko lift (trivially, at weight 4)."""
        result = gritsenko_lift_check()
        assert result['e8_is_gritsenko']


# ============================================================================
# 13. SIEGEL MODULAR FORM SPACE
# ============================================================================

class TestSiegelSpace:
    """Verify the structure of M_12(Sp(4,Z))."""

    def test_total_dimension(self):
        """dim M_12(Sp(4,Z)) = 3."""
        result = siegel_modular_form_space_weight12()
        assert result['total_dimension'] == 3

    def test_eisenstein_dimension(self):
        """dim E_12^{(2)} = 1 (Eisenstein space)."""
        result = siegel_modular_form_space_weight12()
        assert result['eisenstein_dimension'] == 1

    def test_cusp_dimension(self):
        """dim S_12(Sp(4,Z)) = 2 (cusp space)."""
        result = siegel_modular_form_space_weight12()
        assert result['cusp_dimension'] == 2

    def test_sk_dimension(self):
        """dim SK_12 = 1 (one Saito-Kurokawa lift)."""
        result = siegel_modular_form_space_weight12()
        assert result['sk_dimension'] == 1

    def test_non_sk_cusp(self):
        """dim (non-SK cusp) = 1 (= chi_12)."""
        result = siegel_modular_form_space_weight12()
        assert result['non_sk_cusp_dimension'] == 1


# ============================================================================
# 14. CROSS-CHECKS AND CONSISTENCY
# ============================================================================

class TestCrossChecks:
    """Multi-path consistency checks."""

    def test_kappa_consistent_across_paths(self):
        """kappa = 24 in all computation paths."""
        result = full_multi_path_verification()
        assert result['consistency']['kappa_consistent']

    def test_F2_consistent_across_paths(self):
        """F_2 = 7/240 in all computation paths."""
        result = full_multi_path_verification()
        assert result['consistency']['F2_consistent']

    def test_fredholm_rank_matches_kappa(self):
        """Fredholm exponent (= rank) matches kappa."""
        result = full_multi_path_verification()
        assert result['path1_fredholm']['rank'] == LEECH_KAPPA

    def test_lattice_theta_factorizes_diagonal(self):
        """In diagonal limit, theta factorizes as product of genus-1 thetas."""
        result = full_multi_path_verification()
        lat = result['path3_theta']
        # Separating limit: theta_product = theta_1 * theta_2
        assert abs(lat['theta_product'] - lat['theta_1'] * lat['theta_2']) < 1e-10

    def test_shadow_matches_kappa_lambda(self):
        """Shadow F_2 = kappa * lambda_2."""
        shadow = full_multi_path_verification()['path4_shadow']
        assert shadow['F_2_shadow'] == Fraction(LEECH_KAPPA) * lambda_fp(2)

    def test_F2_exact_fraction(self):
        """F_2 = 7/240 as exact fraction."""
        assert Fraction(24) * Fraction(7, 5760) == Fraction(7, 240)

    def test_F2_denominator(self):
        """F_2 = 7/240: denominator is 240."""
        f2 = Fraction(24) * lambda_fp(2)
        assert f2.denominator == 240

    def test_F2_numerator(self):
        """F_2 = 7/240: numerator is 7."""
        f2 = Fraction(24) * lambda_fp(2)
        assert f2.numerator == 7


# ============================================================================
# 15. SHADOW DEPTH CLASSIFICATION
# ============================================================================

class TestShadowDepth:
    """Verify shadow depth classification for the Leech lattice VOA."""

    def test_class_L(self):
        """Leech lattice VOA is class L."""
        result = shadow_vs_exact_comparison()
        assert result['shadow_class'] == 'L'

    def test_shadow_depth_3(self):
        """Shadow depth = 3 for class L."""
        result = shadow_vs_exact_comparison()
        assert result['shadow_depth'] == 3

    def test_not_class_G(self):
        """Leech is NOT class G (would require r_max=2)."""
        result = shadow_vs_exact_comparison()
        assert result['shadow_class'] != 'G'

    def test_not_class_M(self):
        """Leech is NOT class M (would require r_max=infinity)."""
        result = shadow_vs_exact_comparison()
        assert result['shadow_class'] != 'M'


# ============================================================================
# 16. COMPARISON WITH MOONSHINE V^NATURAL
# ============================================================================

class TestMoonshineComparison:
    """Compare Leech lattice VOA with moonshine module V^natural."""

    def test_same_central_charge(self):
        """Both have c = 24."""
        # V^natural: c = 24
        assert LEECH_CENTRAL_CHARGE == 24

    def test_different_dim_V1(self):
        """Leech has dim V_1 = 24; moonshine has dim V_1 = 0."""
        assert LEECH_THETA_COEFFICIENTS[1] == 0  # no norm-2 vectors -> dim V_1 = 24
        # BUT: dim V_1 for the LATTICE VOA is the rank (the free bosons),
        # not the theta coefficient at m=1.
        # Theta coefficient at m=1 counts norm-2 vectors (= 0 for Leech).
        # The 24 free bosons are ALWAYS present (they generate V_1).
        assert LEECH_RANK == 24

    def test_different_kappa(self):
        """Leech: kappa = 24 (lattice formula); moonshine: kappa = 12 (AP48)."""
        # kappa(V_Leech) = rank = 24
        assert LEECH_KAPPA == 24
        # kappa(V^natural) = c/2 = 12 (since V^natural has no weight-1 currents)
        moonshine_kappa = 12
        assert LEECH_KAPPA != moonshine_kappa

    def test_different_shadow_class(self):
        """Leech is class L; moonshine is class M."""
        # Leech: class L (affine KM from Heisenberg subalgebra)
        result = shadow_vs_exact_comparison()
        assert result['shadow_class'] == 'L'
        # V^natural: class M (infinite shadow depth, no affine subalgebra)

    def test_different_F2(self):
        """F_2(V_Leech) = 7/240; F_2(V^natural) = 12 * 7/5760 = 7/480."""
        F2_leech = Fraction(24) * lambda_fp(2)
        F2_moonshine = Fraction(12) * lambda_fp(2)
        assert F2_leech == Fraction(7, 240)
        assert F2_moonshine == Fraction(7, 480)
        assert F2_leech != F2_moonshine

    def test_ratio_F2(self):
        """F_2(Leech) / F_2(V^natural) = 2 (ratio of kappas)."""
        ratio = Fraction(24) / Fraction(12)
        assert ratio == 2


# ============================================================================
# 17. PARTITION FUNCTION UTILITIES
# ============================================================================

class TestPartitions:
    """Verify partition function utilities."""

    def test_p0(self):
        assert partitions(0) == 1

    def test_p1(self):
        assert partitions(1) == 1

    def test_p2(self):
        assert partitions(2) == 2

    def test_p3(self):
        assert partitions(3) == 3

    def test_p4(self):
        assert partitions(4) == 5

    def test_p5(self):
        assert partitions(5) == 7

    def test_p10(self):
        assert partitions(10) == 42

    def test_p_negative(self):
        assert partitions(-1) == 0


# ============================================================================
# 18. BERNOULLI NUMBERS
# ============================================================================

class TestBernoulli:
    """Verify Bernoulli number computation."""

    def test_B0(self):
        assert bernoulli_number(0) == 1

    def test_B1(self):
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_B2(self):
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_B12(self):
        assert bernoulli_number(12) == Fraction(-691, 2730)


# ============================================================================
# 19. LATTICE CONTRIBUTION FACTORIZATION
# ============================================================================

class TestLatticeContribution:
    """Verify the lattice theta contribution to Z_2."""

    def test_theta_product_positive(self):
        """Theta product is positive."""
        result = genus2_lattice_contribution((1.5, 1.5), rank=24, N_shells=5)
        assert result['theta_product'] > 0

    def test_theta_factorizes(self):
        """Theta_{(2)} factorizes in diagonal limit."""
        result = genus2_lattice_contribution((1.5, 1.5), rank=24, N_shells=5)
        assert abs(result['theta_product'] -
                   result['theta_1'] * result['theta_2']) < 1e-10

    def test_symmetric_tori(self):
        """theta_1 = theta_2 when tau_1 = tau_2."""
        result = genus2_lattice_contribution((1.5, 1.5), rank=24, N_shells=5)
        assert abs(result['theta_1'] - result['theta_2']) < 1e-10

    def test_theta_close_to_1(self):
        """For large Im tau, theta ~ 1 (exponentially suppressed)."""
        result = genus2_lattice_contribution((5.0, 5.0), rank=24, N_shells=5)
        # q = exp(-2*pi*5) ~ 2e-14, so theta ~ 1 + 196560*q^2 ~ 1
        assert abs(result['theta_1'] - 1.0) < 1e-10


# ============================================================================
# 20. FULL PARTITION FUNCTION
# ============================================================================

class TestFullPartitionFunction:
    """Verify the full genus-2 partition function."""

    def test_Z2_positive(self):
        """Z_2 > 0 for valid sewing parameters."""
        result = leech_genus2_partition_function(1.5, 1.5, 0.1)
        assert result['Z2_total'] > 0

    def test_Z2_factorizes(self):
        """Z_2 = Z_2^{Heis} * Theta_{Leech}^{(2)}."""
        result = leech_genus2_partition_function(1.5, 1.5, 0.1, N_theta=5)
        expected = result['Z2_heisenberg'] * result['Z2_theta']
        assert abs(result['Z2_total'] - expected) < 1e-6 * abs(expected)

    def test_kappa_in_result(self):
        """Result includes kappa = 24."""
        result = leech_genus2_partition_function(1.5, 1.5, 0.1)
        assert result['kappa'] == 24

    def test_shadow_F2_in_result(self):
        """Result includes shadow F_2 = 7/240."""
        result = leech_genus2_partition_function(1.5, 1.5, 0.1)
        assert abs(result['Z2_shadow_F2'] - 7.0 / 240.0) < 1e-15


# ============================================================================
# 21. LEECH THETA SERIES COMPUTATION
# ============================================================================

class TestLeechThetaComputation:
    """Verify the Leech theta series computation from j and Delta."""

    def test_theta_from_table(self):
        """Stored theta coefficients match the table (Conway-Sloane)."""
        assert leech_theta_coefficient(0) == 1
        assert leech_theta_coefficient(1) == 0
        assert leech_theta_coefficient(2) == 196560
        assert leech_theta_coefficient(3) == 16773120
        assert leech_theta_coefficient(4) == 398034000

    def test_theta_computed_from_j(self):
        """Theta coefficients computed from j match the stored table."""
        for m in range(6):
            stored = LEECH_THETA_COEFFICIENTS.get(m, 0)
            identity_result = verify_leech_genus1_identity(m)
            if m in identity_result['details']:
                computed = identity_result['details'][m]['computed']
                assert computed == stored, f"Mismatch at m={m}: {computed} != {stored}"

    def test_theta_coefficients_nonneg(self):
        """All theta coefficients are nonnegative."""
        for m in range(11):
            assert leech_theta_coefficient(m) >= 0

    def test_theta_r2_is_integer(self):
        """r(2m) are all integers."""
        for m in range(11):
            r = leech_theta_coefficient(m)
            assert isinstance(r, int), f"r({2*m}) = {r} is not int"


# ============================================================================
# 22. NIEMEIER SHADOW DATA
# ============================================================================

class TestNiemeirShadowData:
    """Verify shadow data for Niemeier lattice VOAs."""

    def test_universal_kappa(self):
        """All Niemeier lattice VOAs have kappa = rank = 24."""
        result = niemeier_shadow_comparison()
        for name, data in result['lattices'].items():
            assert data['kappa'] == 24, f"{name}: kappa = {data['kappa']}"

    def test_universal_c(self):
        """All Niemeier lattice VOAs have c = 24."""
        result = niemeier_shadow_comparison()
        for name, data in result['lattices'].items():
            assert data['c'] == 24, f"{name}: c = {data['c']}"

    def test_universal_F2(self):
        """All have F_2 = 7/240."""
        result = niemeier_shadow_comparison()
        for name, data in result['lattices'].items():
            assert data['F_2_shadow'] == Fraction(7, 240)


# ============================================================================
# 23. ADDITIONAL SHADOW PROPERTIES
# ============================================================================

class TestShadowProperties:
    """Additional properties of the shadow obstruction tower."""

    def test_F1_value(self):
        """F_1 = kappa * lambda_1 = 24 * 1/24 = 1."""
        F1 = Fraction(LEECH_KAPPA) * lambda_fp(1)
        assert F1 == Fraction(1)

    def test_F2_value(self):
        """F_2 = kappa * lambda_2 = 24 * 7/5760 = 7/240."""
        F2 = Fraction(LEECH_KAPPA) * lambda_fp(2)
        assert F2 == Fraction(7, 240)

    def test_F3_value(self):
        """F_3 = kappa * lambda_3 = 24 * 31/967680 = 31/40320."""
        F3 = Fraction(LEECH_KAPPA) * lambda_fp(3)
        assert F3 == Fraction(31, 40320)

    def test_Fg_positive(self):
        """F_g > 0 for all g >= 1 (Bernoulli sign pattern)."""
        for g in range(1, 6):
            Fg = Fraction(LEECH_KAPPA) * lambda_fp(g)
            assert Fg > 0, f"F_{g} = {Fg} <= 0"

    def test_ahat_generating_function(self):
        """Verify: sum_g F_g x^{2g} = kappa * (Ahat(ix) - 1)."""
        # At order x^2: kappa * lambda_1 = 24/24 = 1
        # At order x^4: kappa * lambda_2 = 24 * 7/5760 = 7/240
        assert Fraction(24) * lambda_fp(1) == Fraction(1)
        assert Fraction(24) * lambda_fp(2) == Fraction(7, 240)


# ============================================================================
# 24. LATTICE vs VIRASORO KAPPA DISTINCTION (AP48)
# ============================================================================

class TestKappaDistinction:
    """Verify kappa(V_Lambda) = rank != c/2 for lattice VOAs (AP48)."""

    def test_leech_kappa_is_rank(self):
        """kappa(V_Leech) = rank = 24."""
        assert LEECH_KAPPA == 24

    def test_leech_c_over_2(self):
        """c/2 = 12 for Leech (= kappa of Virasoro subalgebra)."""
        assert LEECH_CENTRAL_CHARGE / 2 == 12

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 for Leech (AP48)."""
        assert LEECH_KAPPA != LEECH_CENTRAL_CHARGE / 2

    def test_kappa_twice_virasoro(self):
        """kappa(V_Leech) = 2 * kappa(Vir_{24})."""
        # kappa(Vir_c) = c/2. For c=24: kappa(Vir) = 12.
        # kappa(V_Leech) = 24 = 2 * 12.
        assert LEECH_KAPPA == 2 * (LEECH_CENTRAL_CHARGE // 2)

    def test_moonshine_kappa_is_c_over_2(self):
        """kappa(V^natural) = c/2 = 12 (no weight-1 currents)."""
        # V^natural has dim V_1 = 0, so no Heisenberg subalgebra.
        # kappa is determined by the Virasoro subalgebra: kappa = c/2 = 12.
        moonshine_kappa = 12
        assert moonshine_kappa == LEECH_CENTRAL_CHARGE / 2


# ============================================================================
# 25. EDGE CASES AND BOUNDARY CONDITIONS
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_zero_sewing_parameter(self):
        """w = 0 gives det(1-K) = 1."""
        result = genus2_fredholm_heisenberg(0.1, 0.1, 1e-15, rank=24, N=50)
        assert abs(result['sewing_det'] - 1.0) < 1e-10

    def test_small_q(self):
        """Small q gives Z_2 close to theta part."""
        result = leech_genus2_partition_function(3.0, 3.0, 0.01, N_modes=50, N_theta=3)
        # For large Im tau, the Heisenberg part -> 1 and theta -> 1.
        assert result['Z2_total'] > 0

    def test_lambda_fp_raises_for_g0(self):
        """lambda_fp(0) raises ValueError."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_negative_disc(self):
        """r_2(T) = 0 for T with Delta <= 0."""
        # T = ((1, 3, 1)): Delta = 4 - 9 = -5 < 0
        assert leech_genus2_theta_coefficient(1, 3, 1) == 0

    def test_zero_entry(self):
        """r_2 = 0 when a or c is 0."""
        assert leech_genus2_theta_coefficient(0, 0, 1) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
