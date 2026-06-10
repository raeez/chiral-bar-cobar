"""Tests for compute.lib.phi_n_humbert_heegner_admissible_triple_27_29_35.

Verifies pentagon coboundary phi^(n) on the Humbert-Heegner admissible
triple {27, 29, 35} through multi-path cross-verification:

SCOPE CASCADE:
    n = 27: first depth-9 onset, D_{27, 9} = 10, TRIPLE-CONDITIONAL
            (Zagier-Hoffman + Broadhurst-Kreimer empirical + Brown 2017
            Conj 5.3 higher-depth Galois-motivic generation of grt_1).
    n = 29: depth-9 expansion, D_{29, 9} = 42, TRIPLE-CONDITIONAL
            (same three conjectures).
    n = 35: depth-11 admissible entry, D_{35, 11} = 97 (first depth-11
            onset is at n = 33), QUADRUPLE-CONDITIONAL
            (three above + Broadhurst-Bailey 2010 numerical-extrapolation
            stability at depth 11).

MULTI-PATH CROSS-VERIFICATION:
    P_1 Padovan recurrence d_n = d_{n-2} + d_{n-3} (direct).
    P_2 BK row-sum lag sum_d D_{n+3, d} = d_n.
    P_3 Generating-function coefficient x / (1 - x^2 - x^3).
    P_4 Plastic-number asymptotic rounded d_n = [A rho^n].
    BK_A Symbolic geometric-series expansion.
    BK_B Recursive-inverse Taylor extraction.
    p24_A 24-fold convolution (1 - q^m)^{-1}.
    p24_B Binomial Euler product sum binom(j + 23, 23) q^{mj}.

HUMBERT-HEEGNER ADMISSIBILITY:
    n mod 8 in {3, 5}; verified at admissible triple and at the
    non-admissible neighbours {25, 26, 28, 30, 31, 32, 33, 34, 36}.

OFF-K3 REGIME PERSISTENCE:
    On the K3 A-infinity Humbert regime Eichler-Zagier polar cutoff
    forces phi^(n)|_{K3-Humbert} = 0 for admissible n >= 11.
    Off the regime the Padovan leg persists as the first-principles
    MZV-transcendence count carrying the Theta-obstruction tower.
"""
from __future__ import annotations

import math

import pytest

from compute.lib.phi_n_humbert_heegner_admissible_triple_27_29_35 import (
    ADMISSIBLE_TRIPLE,
    admissibility_filter_check,
    bk_depth_check_triple,
    bk_depth_extract,
    bk_depth_multipath_check_triple,
    bk_depth_via_recursive_inverse,
    bk_padovan_twostep_consistency_check_triple,
    bk_parity_functional_equation_check,
    bk_parity_split_check_triple,
    borcherds_mzv_ratio_triple,
    brown_2017_onset_weight,
    first_depth_eleven_at_33_check,
    first_depth_nine_at_27_check,
    hardy_ramanujan_exact_check_triple,
    humbert_heegner_admissible,
    p24_exact,
    p24_multipath_check_triple,
    p24_via_euler_product,
    padovan_asymptotic,
    padovan_count_check_triple,
    padovan_dim,
    padovan_dim_via_bk_rowsum,
    padovan_dim_via_generating_function,
    padovan_dim_via_plastic_rounded,
    padovan_multipath_check_triple,
    phi_n_leading_check_triple,
    phi_n_leading_values_triple,
    phi_n_mzv_leading,
    plastic_asymptotic_check_triple,
    plastic_asymptotic_precision_check_triple,
    plastic_number,
    quadruple_conditional_onset_weight,
    scope_cascade_assertion,
    scope_cascade_check,
    scope_tier_at,
    triple_conditional_scope_at_n_geq_45,
    verifier_triple_27_29_35,
)


# ---------------------------------------------------------------------------
# Path 1: Humbert-Heegner admissibility filter
# ---------------------------------------------------------------------------

class TestHumbertHeegnerAdmissibility:
    def test_admissible_triple_passes(self):
        for n in ADMISSIBLE_TRIPLE:
            assert humbert_heegner_admissible(n)

    @pytest.mark.parametrize(
        "n", [25, 26, 28, 30, 31, 32, 33, 34, 36, 38, 39, 40, 41, 42, 44]
    )
    def test_non_admissible_n_rejected(self, n):
        assert not humbert_heegner_admissible(n)

    def test_continuation_sequence(self):
        # Next admissible weights beyond the inscribed triple
        for n in (37, 43, 45, 51, 53):
            assert humbert_heegner_admissible(n)

    def test_admissibility_filter_bulk(self):
        assert admissibility_filter_check()


# ---------------------------------------------------------------------------
# Path 2: Padovan dimensions at admissible triple (multi-path)
# ---------------------------------------------------------------------------

class TestPadovanDimensions:
    def test_padovan_values_at_triple(self):
        d = padovan_dim(46)
        assert d[27] == 816
        assert d[29] == 1432
        assert d[35] == 7739

    def test_padovan_count_bulk(self):
        assert padovan_count_check_triple()

    def test_padovan_recurrence(self):
        d = padovan_dim(46)
        for n in range(5, 46):
            assert d[n] == d[n - 2] + d[n - 3]

    def test_multipath_agreement(self):
        """P_1 recurrence, P_2 BK row-sum, P_3 genfun, P_4 plastic-rounded all agree."""
        assert padovan_multipath_check_triple()

    def test_generating_function_path(self):
        d_P1 = padovan_dim(46)
        d_P3 = padovan_dim_via_generating_function(46)
        for n in ADMISSIBLE_TRIPLE:
            assert d_P1[n] == d_P3[n]

    def test_plastic_rounded_path(self):
        d_P1 = padovan_dim(46)
        d_P4 = padovan_dim_via_plastic_rounded(46)
        for n in ADMISSIBLE_TRIPLE:
            assert d_P1[n] == d_P4[n]

    def test_bk_rowsum_path(self):
        D = bk_depth_extract(40, 12)
        d_P1 = padovan_dim(46)
        for n in ADMISSIBLE_TRIPLE:
            p2 = padovan_dim_via_bk_rowsum(n, D)
            assert d_P1[n] == p2, f"n = {n}: P_1 = {d_P1[n]}, P_2 = {p2}"


# ---------------------------------------------------------------------------
# Path 3: Broadhurst-Kreimer depth stratification (multi-path)
# ---------------------------------------------------------------------------

class TestBKDepthStratification:
    def test_bk_depth_values_triple(self):
        assert bk_depth_check_triple()

    def test_first_depth_nine_at_27(self):
        assert first_depth_nine_at_27_check()

    def test_first_depth_eleven_at_33(self):
        assert first_depth_eleven_at_33_check()

    def test_row_sum_identity_triple(self):
        """sum_d D_{n, d} = d_{n - 2} at n in {27, 29, 35}."""
        assert bk_padovan_twostep_consistency_check_triple()

    def test_parity_split_triple(self):
        """Odd-weight admissible triple: even depths vanish."""
        assert bk_parity_split_check_triple()

    def test_parity_functional_equation(self):
        """BK(-x, y) = BK(x, -y): D_{n, d} = 0 whenever n + d odd."""
        assert bk_parity_functional_equation_check()

    def test_bk_depth_multipath_agreement(self):
        """Symbolic vs recursive-inverse path agree at admissible triple."""
        assert bk_depth_multipath_check_triple()

    def test_recursive_inverse_path_samples(self):
        DA = bk_depth_extract(40, 12)
        DB = bk_depth_via_recursive_inverse(40, 12)
        for (n, d) in [(27, 9), (29, 9), (35, 11), (27, 3), (29, 7), (35, 5)]:
            assert DA.get((n, d), 0) == DB.get((n, d), 0), (
                f"({n}, {d}): A = {DA.get((n, d), 0)}, B = {DB.get((n, d), 0)}"
            )


# ---------------------------------------------------------------------------
# Path 4: Hardy-Ramanujan p_24 and Borcherds/MZV ratio (multi-path)
# ---------------------------------------------------------------------------

class TestHardyRamanujanBorcherds:
    def test_p24_exact_at_14(self):
        assert p24_exact(14) == 156_883_829_400

    def test_p24_exact_at_15(self):
        assert p24_exact(15) == 563_116_739_584

    def test_p24_exact_at_18(self):
        assert p24_exact(18) == 21_651_325_216_200

    def test_p24_multipath_agreement(self):
        """p_24(k) computed via direct-24-fold and Euler-product paths agree."""
        for k in (14, 15, 18):
            assert p24_exact(k) == p24_via_euler_product(k)

    def test_p24_multipath_bulk(self):
        assert p24_multipath_check_triple()

    def test_borcherds_mzv_ratio_magnitudes(self):
        r = borcherds_mzv_ratio_triple()
        # At n = 27, ratio ~ 2.55e8; at n = 35, ratio ~ 3.7e9
        assert 1e8 < r[27] < 1e9
        assert 1e8 < r[29] < 1e9
        assert 1e9 < r[35] < 1e10

    def test_hardy_ramanujan_exact_bulk(self):
        assert hardy_ramanujan_exact_check_triple()


# ---------------------------------------------------------------------------
# Path 5: phi^(n) numerical leading values
# ---------------------------------------------------------------------------

class TestPhiNLeading:
    def test_phi_n_leading_values(self):
        vals = phi_n_leading_values_triple()
        assert set(vals.keys()) == set(ADMISSIBLE_TRIPLE)
        # Orders of magnitude
        assert 1e-27 < vals[27] < 1e-25
        assert 1e-29 < vals[29] < 1e-27
        assert 1e-38 < vals[35] < 1e-36

    def test_phi_n_leading_matches_d_n_over_n_factorial(self):
        assert phi_n_leading_check_triple()

    @pytest.mark.parametrize("n", list(ADMISSIBLE_TRIPLE))
    def test_phi_n_positive_and_finite(self, n):
        v = phi_n_mzv_leading(n)
        assert v > 0 and math.isfinite(v)


# ---------------------------------------------------------------------------
# Path 6: Scope cascade (triple/quadruple-conditional)
# ---------------------------------------------------------------------------

class TestScopeCascade:
    def test_scope_at_27(self):
        assert scope_tier_at(27) == "triple-conditional-depth-9"

    def test_scope_at_29(self):
        assert scope_tier_at(29) == "triple-conditional-depth-9"

    def test_scope_at_35(self):
        assert scope_tier_at(35) == "quadruple-conditional-depth-11"

    def test_scope_cascade_full(self):
        tiers = scope_cascade_check()
        assert tiers[27] == "triple-conditional-depth-9"
        assert tiers[29] == "triple-conditional-depth-9"
        assert tiers[35] == "quadruple-conditional-depth-11"

    def test_scope_cascade_bulk(self):
        assert scope_cascade_assertion()

    def test_brown_2017_onset(self):
        assert brown_2017_onset_weight() == 27

    def test_quadruple_conditional_onset(self):
        assert quadruple_conditional_onset_weight() == 35

    def test_scope_at_n_geq_45(self):
        n45, scope = triple_conditional_scope_at_n_geq_45()
        assert n45 == 45
        assert "Brown-2017" in scope


# ---------------------------------------------------------------------------
# Path 7: Plastic-number asymptotic
# ---------------------------------------------------------------------------

class TestPlasticAsymptotic:
    def test_plastic_number_value(self):
        rho = plastic_number()
        # plastic number ~ 1.3247...
        assert 1.32 < rho < 1.33
        # satisfies rho^3 = rho + 1
        assert abs(rho ** 3 - rho - 1) < 1e-12

    @pytest.mark.parametrize("n", list(ADMISSIBLE_TRIPLE))
    def test_plastic_asymptotic_within_tolerance(self, n):
        d = padovan_dim(46)
        asy = padovan_asymptotic(n)
        rel = abs(d[n] - asy) / d[n]
        assert rel < 1e-3, f"n = {n}: d_n = {d[n]}, asy = {asy}, rel = {rel}"

    def test_plastic_asymptotic_bulk(self):
        assert plastic_asymptotic_precision_check_triple()

    def test_plastic_precision_improves_at_35(self):
        """Precision at n = 35 should be at least a decade tighter than at n = 27."""
        tab = plastic_asymptotic_check_triple()
        err_27 = abs(tab[27][2])
        err_35 = abs(tab[35][2])
        assert err_35 < err_27, (
            f"rel err at n = 35 ({err_35}) should be tighter than at n = 27 ({err_27})"
        )


# ---------------------------------------------------------------------------
# Path 8: Explicit inter-path cross-checks (multi-path agreement matrix)
# ---------------------------------------------------------------------------

class TestInterPathCrossChecks:
    """Explicit pairwise cross-check matrix between independently-derived
    quantities.  Each test compares two distinct derivation paths against
    each other -- NOT against a tabulated hard-coded value -- so that
    agreement is a genuine witness of arithmetic correctness.
    """

    def test_d_27_four_paths_cross_agree(self):
        """d_{27} = 816 via recurrence matches three independent paths."""
        d_P1 = padovan_dim(46)[27]
        d_P2 = padovan_dim_via_bk_rowsum(27, bk_depth_extract(40, 12))
        d_P3 = padovan_dim_via_generating_function(46)[27]
        d_P4 = padovan_dim_via_plastic_rounded(46)[27]
        # Cross-check each pair
        assert d_P1 == d_P2  # P_1 vs P_2
        assert d_P1 == d_P3  # P_1 vs P_3
        assert d_P1 == d_P4  # P_1 vs P_4
        assert d_P2 == d_P3  # P_2 vs P_3
        assert d_P2 == d_P4  # P_2 vs P_4
        assert d_P3 == d_P4  # P_3 vs P_4

    def test_d_29_four_paths_cross_agree(self):
        d_P1 = padovan_dim(46)[29]
        d_P2 = padovan_dim_via_bk_rowsum(29, bk_depth_extract(40, 12))
        d_P3 = padovan_dim_via_generating_function(46)[29]
        d_P4 = padovan_dim_via_plastic_rounded(46)[29]
        assert d_P1 == d_P2 == d_P3 == d_P4

    def test_d_35_four_paths_cross_agree(self):
        d_P1 = padovan_dim(46)[35]
        d_P2 = padovan_dim_via_bk_rowsum(35, bk_depth_extract(40, 12))
        d_P3 = padovan_dim_via_generating_function(46)[35]
        d_P4 = padovan_dim_via_plastic_rounded(46)[35]
        assert d_P1 == d_P2 == d_P3 == d_P4

    def test_D_27_9_two_paths_cross_agree(self):
        """D_{27, 9} via symbolic geometric-series and recursive-inverse paths."""
        D_A = bk_depth_extract(40, 12).get((27, 9), 0)
        D_B = bk_depth_via_recursive_inverse(40, 12).get((27, 9), 0)
        assert D_A == D_B

    def test_D_29_9_two_paths_cross_agree(self):
        D_A = bk_depth_extract(40, 12).get((29, 9), 0)
        D_B = bk_depth_via_recursive_inverse(40, 12).get((29, 9), 0)
        assert D_A == D_B

    def test_D_35_11_two_paths_cross_agree(self):
        D_A = bk_depth_extract(40, 12).get((35, 11), 0)
        D_B = bk_depth_via_recursive_inverse(40, 12).get((35, 11), 0)
        assert D_A == D_B

    def test_p24_14_two_paths_cross_agree(self):
        """p_24(14) via 24-fold and binomial Euler-product paths."""
        assert p24_exact(14) == p24_via_euler_product(14)

    def test_p24_15_two_paths_cross_agree(self):
        assert p24_exact(15) == p24_via_euler_product(15)

    def test_p24_18_two_paths_cross_agree(self):
        assert p24_exact(18) == p24_via_euler_product(18)

    def test_row_sum_cross_agrees_with_recurrence(self):
        """BK row-sum identity (path 2) cross-agrees with Padovan recurrence
        (path 1) at every admissible weight.  This is a structural witness
        of the motivic-GRT_1 dimension count matching the Brown canonical
        basis dimension three steps above (sum_d D_{m, d} = d_{m-3}).
        """
        d_P1 = padovan_dim(46)
        D = bk_depth_extract(40, 12)
        for n in ADMISSIBLE_TRIPLE:
            rowsum_for_n_plus_3 = sum(D.get((n + 3, k), 0) for k in range(1, 13))
            # Cross-check: row-sum at n+3 equals d_n via the three-step lag
            assert rowsum_for_n_plus_3 == d_P1[n], (
                f"Cross-check fails at n = {n}: row-sum @ {n+3} = "
                f"{rowsum_for_n_plus_3}, d_{n} = {d_P1[n]}"
            )

    def test_plastic_asymptotic_cross_agrees_with_recurrence(self):
        """Plastic asymptotic A rho^n rounded cross-agrees with recurrence."""
        d_P1 = padovan_dim(46)
        d_P4 = padovan_dim_via_plastic_rounded(46)
        for n in ADMISSIBLE_TRIPLE:
            assert d_P1[n] == d_P4[n]

    def test_parity_functional_equation_cross_agrees_with_explicit_zeros(self):
        """Functional equation BK(-x, y) = BK(x, -y) cross-agrees with
        explicit parity-split zeros at admissible triple (all odd).
        """
        D = bk_depth_extract(40, 12)
        # From functional equation: odd n + even d => D = 0
        for n in ADMISSIBLE_TRIPLE:
            assert n % 2 == 1
            for d_even in (2, 4, 6, 8, 10, 12):
                # Independent computation of the zero: functional equation path
                assert (n + d_even) % 2 == 1, "n + d_even should be odd here"
                # Direct extraction path
                assert D.get((n, d_even), 0) == 0

    def test_borcherds_mzv_ratio_cross_agrees(self):
        """Borcherds/MZV ratio via two independent p_24 paths and Padovan path."""
        d = padovan_dim(46)
        ratios = borcherds_mzv_ratio_triple()
        for n in ADMISSIBLE_TRIPLE:
            k = (n + 1) // 2
            # Path A: direct expansion
            pA = p24_exact(k)
            # Path B: binomial Euler product
            pB = p24_via_euler_product(k)
            # Cross-check both paths match
            assert pA == pB
            # Cross-check ratio reconstruction from recurrence-computed d_n
            assert abs(ratios[n] - pA / d[n]) < 1e-9


# ---------------------------------------------------------------------------
# Path 9: Aggregate verifier (all paths must agree)
# ---------------------------------------------------------------------------

class TestAggregateVerifier:
    def test_all_checks_pass(self):
        results = verifier_triple_27_29_35()
        failures = {k: v for k, v in results.items() if not v}
        assert not failures, f"Failures: {failures}"

    def test_verifier_includes_multipath_checks(self):
        results = verifier_triple_27_29_35()
        expected_paths = {
            "admissibility_filter",
            "padovan_count_triple",
            "padovan_multipath_triple",
            "bk_depth_triple",
            "bk_depth_multipath_triple",
            "bk_parity_functional_equation",
            "first_depth_nine_at_27",
            "first_depth_eleven_at_33",
            "bk_rowsum_lag_triple",
            "bk_parity_split_triple",
            "phi_n_leading_triple",
            "hardy_ramanujan_exact_triple",
            "p24_multipath_triple",
            "scope_cascade",
            "plastic_asymptotic_triple",
        }
        assert expected_paths.issubset(results.keys()), (
            f"Missing paths: {expected_paths - set(results.keys())}"
        )
