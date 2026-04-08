"""Cross-volume AP49 formula verification tests.

Exhaustive verification that every shared formula between Vol I and Vol II
agrees after accounting for convention differences.

Categories tested:
  (a) kappa formulas for all families (AP1, AP39, AP48)
  (b) F_g = kappa * lambda_g^FP convention (AP22, AP38)
  (c) Complementarity sums kappa + kappa' (AP24)
  (d) Q^contact quartic invariant (AP44)
  (e) Shadow depth classification G/L/C/M (AP14)
  (f) Bar differential grading conventions (AP45)
  (g) R-matrix pole structure (AP19)

Each formula is verified by 3+ independent methods.
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_cross_volume_ap49_engine import (
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_kac_moody,
    kappa_w_n,
    kappa_lattice,
    kappa_beta_gamma,
    harmonic_number,
    anomaly_ratio,
    # Koszul dual
    koszul_dual_c_virasoro,
    koszul_dual_c_w_n,
    koszul_dual_level_km,
    alpha_N,
    K_N_formula,
    # Complementarity
    complementarity_sum_km,
    complementarity_sum_virasoro,
    complementarity_sum_w_n,
    # Quartic contact
    q_contact_virasoro,
    critical_discriminant_virasoro,
    # FP numbers
    lambda_fp,
    F_g_formula,
    # Grading
    desuspension_degree,
    bar_element_degree,
    # R-matrix
    r_matrix_max_pole,
    # Convention
    ope_to_lambda_bracket,
    # Shadow depth
    shadow_depth_class,
    # Superconformal
    kappa_n2_sca,
    # Verification suites
    verify_kappa_heisenberg_cross_volume,
    verify_kappa_virasoro_cross_volume,
    verify_kappa_km_cross_volume,
    verify_kappa_w_n_cross_volume,
    verify_complementarity_cross_volume,
    verify_alpha_N_equals_K_N,
    verify_q_contact_cross_volume,
    verify_faber_pandharipande_cross_volume,
    verify_bar_grading_cross_volume,
    verify_r_matrix_poles_cross_volume,
    verify_ope_lambda_bracket_cross_volume,
    verify_shadow_depth_cross_volume,
    verify_specific_kappa_values,
    verify_superconformal_kappa,
    verify_heisenberg_complementarity,
    verify_w3_specific_values,
    verify_ddca_kappa,
    run_all_verifications,
)


# ============================================================================
# Category (a): kappa formulas — AP1, AP39, AP48
# ============================================================================

class TestKappaHeisenberg:
    """Heisenberg kappa = k (the level), NOT c/2."""

    def test_kappa_equals_level(self):
        """kappa(H_k) = k at k=1."""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)

    def test_kappa_at_negative_level(self):
        """kappa(H_{-1}) = -1."""
        assert kappa_heisenberg(Fraction(-1)) == Fraction(-1)

    def test_kappa_not_c_over_2_ap39(self):
        """AP39: kappa != c/2 for Heisenberg. For rank-1, c = k, kappa = k != k/2."""
        k = Fraction(4)
        assert kappa_heisenberg(k) == k
        assert kappa_heisenberg(k) != k / 2  # AP39 violation check

    def test_cross_volume_agreement(self):
        """Vol I and Vol II use same formula."""
        r = verify_kappa_heisenberg_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Mismatch at {key}: {val}"


class TestKappaVirasoro:
    """Virasoro kappa = c/2."""

    def test_kappa_c1(self):
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)

    def test_kappa_c26(self):
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_c0(self):
        """c=0: uncurved bar complex."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_self_dual_c13(self):
        """Self-dual at c=13 (AP8)."""
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)

    def test_cross_volume_agreement(self):
        r = verify_kappa_virasoro_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Mismatch at {key}: {val}"


class TestKappaKM:
    """KM kappa = dim(g)*(k+h^v)/(2*h^v)."""

    def test_sl2_k1(self):
        """sl_2 at k=1: kappa = 3*3/4 = 9/4."""
        assert kappa_kac_moody(3, Fraction(1), 2) == Fraction(9, 4)

    def test_sl3_k1(self):
        """sl_3 at k=1: kappa = 8*4/6 = 16/3."""
        assert kappa_kac_moody(8, Fraction(1), 3) == Fraction(16, 3)

    def test_g2_k1(self):
        """G_2 at k=1: kappa = 14*5/8 = 35/4."""
        assert kappa_kac_moody(14, Fraction(1), 4) == Fraction(35, 4)

    def test_sl2_critical(self):
        """sl_2 at critical level k=-2: kappa = 0."""
        assert kappa_kac_moody(3, Fraction(-2), 2) == Fraction(0)

    def test_cross_volume_agreement(self):
        r = verify_kappa_km_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Mismatch at {key}: {val}"


class TestKappaWN:
    """W_N kappa = c * (H_N - 1)."""

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro: kappa = c*(H_2-1) = c/2."""
        c = Fraction(10)
        assert kappa_w_n(2, c) == kappa_virasoro(c)

    def test_w3_formula(self):
        """W_3: kappa = 5c/6."""
        c = Fraction(6)
        assert kappa_w_n(3, c) == Fraction(5)
        assert kappa_w_n(3, c) == Fraction(5) * c / 6

    def test_w4_formula(self):
        """W_4: H_4 = 1 + 1/2 + 1/3 + 1/4 = 25/12, rho = 13/12."""
        c = Fraction(12)
        assert kappa_w_n(4, c) == Fraction(13)

    def test_harmonic_numbers(self):
        assert harmonic_number(1) == Fraction(1)
        assert harmonic_number(2) == Fraction(3, 2)
        assert harmonic_number(3) == Fraction(11, 6)
        assert harmonic_number(4) == Fraction(25, 12)

    def test_anomaly_ratio(self):
        assert anomaly_ratio(2) == Fraction(1, 2)
        assert anomaly_ratio(3) == Fraction(5, 6)

    def test_cross_volume_agreement(self):
        r = verify_kappa_w_n_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Mismatch at {key}: {val}"


class TestKappaLattice:
    """Lattice kappa = rank (AP48)."""

    def test_rank_24(self):
        """Leech lattice: kappa = 24, NOT c/2 = 12."""
        assert kappa_lattice(24) == Fraction(24)
        assert kappa_lattice(24) != Fraction(12)  # AP48

    def test_rank_1(self):
        assert kappa_lattice(1) == Fraction(1)


# ============================================================================
# Category (b): F_g = kappa * lambda_g^FP — AP22, AP38
# ============================================================================

class TestFaberPandharipande:
    """Lambda_g^FP values and F_g convention."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760 (NOT 1/1152, AP38)."""
        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp(2) != Fraction(1, 1152)  # AP38 wrong value

    def test_lambda_3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_F1_equals_kappa_over_24(self):
        """F_1(A) = kappa(A)/24 for all A."""
        for kappa in [Fraction(1), Fraction(13, 2), Fraction(5)]:
            assert F_g_formula(kappa, 1) == kappa / 24

    def test_F1_virasoro(self):
        """F_1(Vir_c) = c/48."""
        c = Fraction(26)
        assert F_g_formula(kappa_virasoro(c), 1) == Fraction(13, 24)

    def test_F1_heisenberg(self):
        """F_1(H_k) = k/24."""
        k = Fraction(1)
        assert F_g_formula(kappa_heisenberg(k), 1) == Fraction(1, 24)

    def test_gf_convention_ap22(self):
        """GF uses x^{2g} (not x^{2g-2}). AP22 check."""
        r = verify_faber_pandharipande_cross_volume()
        assert r['GF_convention_AP22']['F1_x_power'] == 2
        assert r['GF_convention_AP22']['Ahat_leading_x_power'] == 2

    def test_cross_volume_agreement(self):
        r = verify_faber_pandharipande_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Mismatch at {key}: {val}"


# ============================================================================
# Category (c): Complementarity sums — AP24
# ============================================================================

class TestComplementarity:
    """kappa(A) + kappa(A!) values across families."""

    def test_km_sum_zero(self):
        """KM: kappa + kappa' = 0 (anti-symmetric)."""
        assert complementarity_sum_km(3, Fraction(1), 2) == Fraction(0)
        assert complementarity_sum_km(8, Fraction(1), 3) == Fraction(0)
        assert complementarity_sum_km(14, Fraction(1), 4) == Fraction(0)

    def test_virasoro_sum_13(self):
        """Virasoro: kappa + kappa' = 13 (AP24: NOT zero)."""
        assert complementarity_sum_virasoro(Fraction(0)) == Fraction(13)
        assert complementarity_sum_virasoro(Fraction(13)) == Fraction(13)
        assert complementarity_sum_virasoro(Fraction(26)) == Fraction(13)

    def test_virasoro_sum_not_zero_ap24(self):
        """AP24: complementarity sum is 13 for Virasoro, not 0."""
        assert complementarity_sum_virasoro(Fraction(1)) != Fraction(0)

    def test_w3_sum_250_over_3(self):
        """W_3: kappa + kappa' = (H_3-1)*alpha_3 = (5/6)*100 = 250/3."""
        s = complementarity_sum_w_n(3, Fraction(10))
        assert s == Fraction(250, 3)

    def test_w_n_c_independent(self):
        """Complementarity sum for W_N is independent of c."""
        for N in [2, 3, 4, 5]:
            s1 = complementarity_sum_w_n(N, Fraction(1))
            s2 = complementarity_sum_w_n(N, Fraction(100))
            assert s1 == s2, f"W_{N} sum depends on c: {s1} != {s2}"

    def test_alpha_equals_K(self):
        """alpha_N = K_N = 4N^3 - 2N - 2."""
        for N in range(2, 8):
            assert alpha_N(N) == K_N_formula(N), f"alpha_{N} != K_{N}"

    def test_specific_alpha_values(self):
        """alpha_2 = 26, alpha_3 = 100, alpha_4 = 258."""
        assert alpha_N(2) == Fraction(26)
        assert alpha_N(3) == Fraction(100)
        assert alpha_N(4) == Fraction(246)

    def test_heisenberg_complementarity(self):
        """Heisenberg: kappa + kappa' = 0."""
        r = verify_heisenberg_complementarity()
        for key, val in r.items():
            assert val['match'], f"Heisenberg mismatch at {key}"

    def test_cross_volume_agreement(self):
        r = verify_complementarity_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Complementarity mismatch at {key}: {val}"


# ============================================================================
# Category (d): Q^contact — AP44
# ============================================================================

class TestQContact:
    """Q^contact = 10/[c(5c+22)] for Virasoro."""

    def test_formula(self):
        """Direct formula check."""
        c = Fraction(1)
        assert q_contact_virasoro(c) == Fraction(10, 27)

    def test_at_c_half(self):
        c = Fraction(1, 2)
        expected = Fraction(10) / (Fraction(1, 2) * (Fraction(5, 2) + 22))
        assert q_contact_virasoro(c) == expected

    def test_critical_discriminant(self):
        """Delta = 40/(5c+22)."""
        c = Fraction(1)
        assert critical_discriminant_virasoro(c) == Fraction(40, 27)

    def test_discriminant_formula(self):
        """Delta = 8 * kappa * S_4 = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22)."""
        for c in [Fraction(1), Fraction(2), Fraction(13), Fraction(26)]:
            delta = critical_discriminant_virasoro(c)
            expected = Fraction(40) / (5 * c + 22)
            assert delta == expected, f"Delta mismatch at c={c}"

    def test_cross_volume_agreement(self):
        r = verify_q_contact_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"Q^contact mismatch at {key}: {val}"


# ============================================================================
# Category (e): Shadow depth G/L/C/M — AP14
# ============================================================================

class TestShadowDepth:
    """Shadow depth classification consistent across volumes."""

    def test_heisenberg_gaussian(self):
        cl, r, _ = shadow_depth_class('heisenberg')
        assert cl == 'G' and r == 2

    def test_km_lie(self):
        cl, r, _ = shadow_depth_class('kac_moody')
        assert cl == 'L' and r == 3

    def test_betagamma_contact(self):
        cl, r, _ = shadow_depth_class('beta_gamma')
        assert cl == 'C' and r == 4

    def test_virasoro_mixed(self):
        cl, r, _ = shadow_depth_class('virasoro')
        assert cl == 'M' and r == -1  # infinity

    def test_w_n_mixed(self):
        cl, r, _ = shadow_depth_class('w_n')
        assert cl == 'M' and r == -1

    def test_lattice_gaussian(self):
        cl, r, _ = shadow_depth_class('lattice')
        assert cl == 'G' and r == 2

    def test_all_families_koszul_ap14(self):
        """AP14: ALL families are chirally Koszul. Depth != Koszulness."""
        r = verify_shadow_depth_cross_volume()
        assert r['all_koszul']['finite_depth_koszul']
        assert r['all_koszul']['infinite_depth_koszul']


# ============================================================================
# Category (f): Bar grading — AP45
# ============================================================================

class TestBarGrading:
    """Bar complex grading conventions."""

    def test_desuspension_lowers_degree(self):
        """s^{-1} lowers cohomological degree by 1 (AP45)."""
        assert desuspension_degree(1) == 0
        assert desuspension_degree(2) == 1
        assert desuspension_degree(0) == -1

    def test_bar_element_degree(self):
        """s^{-1}a_1 tensor s^{-1}a_2: degree = sum|a_i| - n."""
        assert bar_element_degree([1, 1]) == 0
        assert bar_element_degree([1, 1, 1]) == 0
        assert bar_element_degree([2, 1]) == 1

    def test_not_plus_n_ap45(self):
        """AP45: degree is sum - n, NOT sum + n."""
        # Common error: |s^{-1}a| = |a| + 1 (WRONG)
        # Correct: |s^{-1}a| = |a| - 1
        assert bar_element_degree([1, 1]) != 4  # Would be 1+1+2=4 if wrong

    def test_cross_volume_agreement(self):
        r = verify_bar_grading_cross_volume()
        assert r['desuspension_direction']['lowers']
        assert r['bar_element_deg_1_1']['NOT_plus_2']


# ============================================================================
# Category (g): R-matrix poles — AP19
# ============================================================================

class TestRMatrixPoles:
    """R-matrix pole structure after d-log absorption."""

    def test_heisenberg(self):
        """OPE z^{-2} -> r-matrix z^{-1}."""
        assert r_matrix_max_pole(2) == 1

    def test_virasoro(self):
        """OPE z^{-4} -> r-matrix z^{-3}."""
        assert r_matrix_max_pole(4) == 3

    def test_km(self):
        """KM OPE z^{-2} -> r-matrix z^{-1} (Omega/z)."""
        assert r_matrix_max_pole(2) == 1

    def test_w3_self(self):
        """W_3 self OPE z^{-6} -> r-matrix z^{-5}."""
        assert r_matrix_max_pole(6) == 5

    def test_w_n_self(self):
        """W_N self OPE z^{-2N} -> r-matrix z^{-(2N-1)}."""
        for N in [2, 3, 4, 5, 6]:
            assert r_matrix_max_pole(2 * N) == 2 * N - 1

    def test_cross_volume_agreement(self):
        r = verify_r_matrix_poles_cross_volume()
        for key, val in r.items():
            if 'match' in val:
                assert val['match'], f"R-matrix mismatch at {key}: {val}"


# ============================================================================
# OPE vs lambda-bracket — AP44
# ============================================================================

class TestOPELambdaBracket:
    """OPE mode -> lambda-bracket conversion."""

    def test_t3t_divided_power(self):
        """T_{(3)}T = c/2 -> lambda^3 coeff = c/12 (divided by 3! = 6)."""
        c = Fraction(24)
        assert ope_to_lambda_bracket(Fraction(c, 2), 3) == Fraction(c, 12)

    def test_t1t_no_change(self):
        """T_{(1)}T = 2T -> lambda^1 coeff = 2T (1! = 1)."""
        assert ope_to_lambda_bracket(Fraction(2), 1) == Fraction(2)

    def test_t0t_no_change(self):
        """T_{(0)}T = dT -> lambda^0 coeff = dT (0! = 1)."""
        assert ope_to_lambda_bracket(Fraction(1), 0) == Fraction(1)

    def test_full_virasoro_lambda_bracket(self):
        """Full Virasoro: {T_lambda T} = dT + 2*lambda*T + (c/12)*lambda^3."""
        r = verify_ope_lambda_bracket_cross_volume()
        assert r['vir_full_lambda_bracket']['match']

    def test_not_c_over_2_at_lambda3_ap44(self):
        """AP44: coefficient of lambda^3 is c/12, NOT c/2."""
        c = Fraction(12)
        coeff = ope_to_lambda_bracket(Fraction(c, 2), 3)
        assert coeff == Fraction(1)  # c/12 = 12/12 = 1
        assert coeff != Fraction(c, 2)  # NOT c/2 = 6


# ============================================================================
# Specific cross-volume values
# ============================================================================

class TestSpecificValues:
    """Multi-path verified specific kappa values."""

    def test_vir_c26(self):
        r = verify_specific_kappa_values()
        v = r['Vir_c26']
        assert v['method1_direct']
        assert v['method2_complement']
        assert v['method3_F1']

    def test_w3_c100(self):
        r = verify_specific_kappa_values()
        v = r['W3_c100']
        assert v['method1_direct']
        assert v['method2_rho']
        assert v['method3_F1']

    def test_sl2_k1(self):
        r = verify_specific_kappa_values()
        v = r['sl2_k1']
        assert v['method1_direct']
        assert v['method3_complement']

    def test_leech_lattice_ap48(self):
        """AP48: kappa(Leech) = 24, NOT 12 = c/2."""
        r = verify_specific_kappa_values()
        v = r['Leech_lattice']
        assert v['method1_direct']
        assert v['NOT_c_over_2']

    def test_heis_k1(self):
        r = verify_specific_kappa_values()
        v = r['Heis_k1']
        assert v['method1_direct']
        assert v['method2_complement']
        assert v['method3_F1']


class TestSuperconformal:
    """Superconformal kappa values across volumes."""

    def test_n0_virasoro(self):
        r = verify_superconformal_kappa()
        assert r['N0_Vir']['match']

    def test_n1_svir(self):
        """SVir: kappa = (3c-2)/4, self-dual at c = 15/2."""
        r = verify_superconformal_kappa()
        assert r['N1_SVir']['match']

    def test_n2_sca_vol1(self):
        """N=2 SCA: Vol I proves kappa = (6-c)/(2(3-c)), NOT c/2."""
        r = verify_superconformal_kappa()
        assert r['N2_SCA']['match']

    def test_n2_sca_complementarity(self):
        """N=2: kappa(c) + kappa(6-c) = 1."""
        r = verify_superconformal_kappa()
        assert r['N2_complementarity']['match']

    def test_n2_ap49_discrepancy(self):
        """AP49: Vol II incorrectly claims kappa(N=2) = c/2."""
        r = verify_superconformal_kappa()
        assert r['N2_AP49_discrepancy']['discrepancy'], \
            "Vol I and Vol II should DISAGREE on N=2 SCA kappa"

    def test_n4_small_ap49(self):
        """N=4 small: cross-volume parametrization mismatch flagged."""
        r = verify_superconformal_kappa()
        assert r['N4_small_AP49']['convention_mismatch']


class TestW3Specific:
    """W_3-specific cross-volume values."""

    def test_channel_decomposition(self):
        """kappa = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
        r = verify_w3_specific_values()
        assert r['channel_decomposition']['match']

    def test_complementarity_250_over_3(self):
        """kappa + kappa' = 250/3."""
        r = verify_w3_specific_values()
        assert r['complementarity']['match']

    def test_alpha_3_equals_100(self):
        r = verify_w3_specific_values()
        assert r['alpha_3']['match']


class TestDDCA:
    """DDCA kappa cross-check with KM formula."""

    def test_ddca_km_consistency(self):
        """kappa(DDCA_k(gl_K)) = K(k+K)/2 = kappa_KM(gl_K, k)."""
        r = verify_ddca_kappa()
        for key, val in r.items():
            assert val['match'], f"DDCA mismatch at {key}: {val}"


# ============================================================================
# Koszul dual formulas
# ============================================================================

class TestKoszulDual:
    """Koszul dual central charges."""

    def test_vir_dual(self):
        """Vir_c^! = Vir_{26-c}."""
        assert koszul_dual_c_virasoro(Fraction(0)) == Fraction(26)
        assert koszul_dual_c_virasoro(Fraction(13)) == Fraction(13)
        assert koszul_dual_c_virasoro(Fraction(26)) == Fraction(0)

    def test_w_n_dual(self):
        """W_N: c -> alpha_N - c."""
        assert koszul_dual_c_w_n(2, Fraction(0)) == Fraction(26)
        assert koszul_dual_c_w_n(3, Fraction(0)) == Fraction(100)

    def test_km_dual_level(self):
        """FF: k -> -k - 2h^v."""
        assert koszul_dual_level_km(Fraction(1), 2) == Fraction(-5)
        assert koszul_dual_level_km(Fraction(1), 3) == Fraction(-7)

    def test_km_dual_kappa_negated(self):
        """For KM: kappa(k') = -kappa(k)."""
        for (dim_g, h, k) in [(3, 2, Fraction(1)), (8, 3, Fraction(2))]:
            kp = kappa_kac_moody(dim_g, k, h)
            k_dual = koszul_dual_level_km(k, h)
            kp_dual = kappa_kac_moody(dim_g, k_dual, h)
            assert kp + kp_dual == 0


# ============================================================================
# Master verification
# ============================================================================

class TestMasterVerification:
    """Run all verifications and check for any failures."""

    def test_all_verifications_pass(self):
        """Every cross-volume formula check must pass."""
        results = run_all_verifications()
        failures = []
        for category, checks in results.items():
            for check_name, val in checks.items():
                if isinstance(val, dict) and 'match' in val:
                    if not val['match']:
                        failures.append(f"{category}/{check_name}: {val}")
        assert len(failures) == 0, (
            f"AP49 cross-volume failures:\n" + "\n".join(failures)
        )

    def test_total_check_count(self):
        """Verify we have at least 50 individual checks."""
        results = run_all_verifications()
        count = 0
        for category, checks in results.items():
            for check_name, val in checks.items():
                if isinstance(val, dict) and 'match' in val:
                    count += 1
        assert count >= 50, f"Only {count} checks, need >= 50"
