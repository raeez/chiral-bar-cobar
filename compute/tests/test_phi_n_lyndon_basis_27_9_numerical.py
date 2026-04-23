"""Tests for ``phi_n_lyndon_basis_27_9_numerical``.

Verifies the Broadhurst--Kreimer extraction at weights 25--28, the
bi-grading of the ten Lambda generators, and the Richardson-convergent
numerical value of Lambda_1 = zeta({3}^9).

Author: Raeez Lorgat.
"""

from __future__ import annotations

import mpmath
import pytest

from compute.lib.phi_n_lyndon_basis_27_9_numerical import (
    LAMBDA_BASIS_27_9,
    bk_coefficient,
    bk_depth_extract_25_28,
    bk_padovan_twostep_consistency_check_25_28,
    mzv_depth9_weight27_via_borwein_bradley,
    mzv_hoffman,
    numerical_values_all_ten,
    padovan_count_check_25_28,
    verify_bigradings,
    verify_lambda_1_four_voices,
)


class TestBKExtractor:
    """Verify the Broadhurst--Kreimer depth-grading extractor."""

    def test_d_27_9_equals_ten(self) -> None:
        assert bk_coefficient(27, 9) == 10

    def test_bk_rows_25_28_match_manuscript(self) -> None:
        rows = bk_depth_extract_25_28()
        assert rows[25] == (1, 0, 35, 0, 108, 0, 56, 0, 0)
        assert rows[26] == (0, 10, 0, 88, 0, 139, 0, 28, 0)
        assert rows[27] == (1, 0, 41, 0, 171, 0, 128, 0, 10)
        assert rows[28] == (0, 10, 0, 121, 0, 241, 0, 93, 0)

    def test_row_sum_padovan_identity(self) -> None:
        assert bk_padovan_twostep_consistency_check_25_28()

    def test_depth_9_empty_below_27(self) -> None:
        for n in (9, 11, 13, 15, 17, 19, 21, 23, 25, 26):
            assert bk_coefficient(n, 9) == 0


class TestPadovanRecurrence:
    """Padovan recurrence d_n = d_{n-2} + d_{n-3}."""

    def test_padovan_25_28(self) -> None:
        assert padovan_count_check_25_28() == (351, 465, 616, 816)


class TestLambdaBasis:
    """Ten Lambda generators at bi-degree (27, 9)."""

    def test_cardinality_is_ten(self) -> None:
        assert len(LAMBDA_BASIS_27_9) == 10

    def test_all_bigradings_are_27_9(self) -> None:
        verify_bigradings()

    def test_convergence_first_entries(self) -> None:
        for name, s, _desc in LAMBDA_BASIS_27_9:
            assert s[0] >= 2, f"{name} violates leading-entry convergence"

    def test_names_unique(self) -> None:
        names = [n for n, _, _ in LAMBDA_BASIS_27_9]
        assert len(set(names)) == 10

    def test_compositions_unique(self) -> None:
        comps = [s for _, s, _ in LAMBDA_BASIS_27_9]
        assert len(set(comps)) == 10


class TestLambdaOneNumerical:
    """Lambda_1 = zeta({3}^9) numerical evaluation."""

    @pytest.mark.slow
    def test_lambda_1_leading_digits_N500(self) -> None:
        mpmath.mp.dps = 30
        v = mzv_depth9_weight27_via_borwein_bradley(N=500, dps=30)
        # Richardson-converged leading: 1.035525... times 10^{-15}
        expected_leading = mpmath.mpf("1.0355e-15")
        assert v > mpmath.mpf("1.03e-15")
        assert v < mpmath.mpf("1.04e-15")

    def test_lambda_1_at_N300(self) -> None:
        mpmath.mp.dps = 20
        v = mzv_depth9_weight27_via_borwein_bradley(N=300, dps=20)
        # At N=300, value is 1.033930...e-15
        assert abs(v - mpmath.mpf("1.034e-15")) < mpmath.mpf("1e-17")


class TestZeta33CrossCheck:
    """Independent verification: zeta(3,3) = (zeta(3)^2 - zeta(6))/2."""

    def test_closed_form_convergence(self) -> None:
        mpmath.mp.dps = 40
        closed = (mpmath.zeta(3) ** 2 - mpmath.zeta(6)) / 2
        # Truncation at N=500 should match closed form to 10^{-5}
        direct = mzv_hoffman((3, 3), N=500, dps=40)
        assert abs(closed - direct) < mpmath.mpf("1e-5")

    def test_higher_N_tighter(self) -> None:
        mpmath.mp.dps = 40
        closed = (mpmath.zeta(3) ** 2 - mpmath.zeta(6)) / 2
        direct_500 = mzv_hoffman((3, 3), N=500, dps=40)
        direct_1000 = mzv_hoffman((3, 3), N=1000, dps=40)
        err_500 = abs(closed - direct_500)
        err_1000 = abs(closed - direct_1000)
        # N^{-2} decay: err(1000) / err(500) ~ 1/4
        assert err_1000 < err_500
        ratio = float(err_1000 / err_500)
        assert 0.15 < ratio < 0.40


class TestFourVoiceVerification:
    """Four-voice verification protocol for Lambda_1."""

    @pytest.mark.slow
    def test_four_voices(self) -> None:
        result = verify_lambda_1_four_voices(dps=30)
        # V1: monotonic approach as N grows
        V1 = result["V1_nested_truncation"]
        assert V1[300] < V1[500] < V1[800] < V1[1200]
        # V4: BK coefficient is 10
        assert result["V4_BK_coefficient"] == 10


class TestNumericalValuesAllTen:
    """Compute all ten values at moderate N (smoke test)."""

    @pytest.mark.slow
    def test_all_ten_compute(self) -> None:
        results = numerical_values_all_ten(N=200, dps=25)
        assert len(results) == 10
        names = {name for name, _ in results}
        assert "Lambda_1" in names
        assert "Lambda_10" in names


class TestMultiPathBK:
    """Multi-path verification of Broadhurst--Kreimer depth extraction.

    Path 1: direct series expansion at truncation (N, K).
    Path 2: truncation-invariance: D_{27,9} stable under N -> 2N.
    Path 3: row-sum Padovan identity.
    Path 4: parity identity BK(-x, y) = BK(x, -y): D_{n,d} = 0 when n+d odd.
    """

    def test_truncation_invariance(self) -> None:
        v1 = bk_coefficient(27, 9, N=28, K=10)
        v2 = bk_coefficient(27, 9, N=35, K=12)
        v3 = bk_coefficient(27, 9, N=40, K=15)
        assert v1 == v2 == v3 == 10

    def test_parity_identity(self) -> None:
        # n + d odd forces D_{n,d} = 0. Check at several (n, d).
        odd_parity_pairs = [(9, 4), (11, 6), (13, 2), (25, 2), (26, 3), (27, 4)]
        for n, d in odd_parity_pairs:
            assert bk_coefficient(n, d) == 0, f"D_{{{n},{d}}} should vanish by parity"

    def test_first_depth_9_onset_at_27(self) -> None:
        # D_{n,9} = 0 for n < 27, D_{27,9} = 10 is the onset.
        for n in range(9, 27):
            assert bk_coefficient(n, 9) == 0, f"depth-9 should be empty at n={n}"
        assert bk_coefficient(27, 9) == 10


class TestMultiPathLambdaOne:
    """Multi-path verification of Lambda_1 = zeta({3}^9) numerical value.

    Path 1: nested-truncation convergence at increasing N.
    Path 2: zeta(3,3) closed-form cross-check validates the truncation scheme.
    Path 3: Richardson-like ratio test: (v_{2N} - v_N) / (v_N - v_{N/2}) ~ 1/4.
    Path 4: upper bound via |zeta({3}^k)| <= zeta(3)^k / k! shows order 10^{-15}.
    """

    def test_richardson_ratio(self) -> None:
        mpmath.mp.dps = 30
        # zeta(3,3) Richardson: compare (v_2N - v_N) to (v_N - v_{N/2}).
        N0 = 250
        closed = (mpmath.zeta(3) ** 2 - mpmath.zeta(6)) / 2
        v250 = mzv_hoffman((3, 3), N=250, dps=30)
        v500 = mzv_hoffman((3, 3), N=500, dps=30)
        v1000 = mzv_hoffman((3, 3), N=1000, dps=30)
        diff_1 = v500 - v250
        diff_2 = v1000 - v500
        # Both positive (monotone increasing partial sums); ratio ~ 1/4
        assert diff_1 > 0
        assert diff_2 > 0
        ratio = float(diff_2 / diff_1)
        assert 0.15 < ratio < 0.40, f"Richardson ratio {ratio} outside [0.15, 0.40]"

    def test_upper_bound_order_of_magnitude(self) -> None:
        # |zeta({3}^9)| bounded above by zeta(3)^9 / 9! ~ 1.2^9 / 362880 ~ 1.5e-5 (very loose).
        # But tighter: nested-truncation gives 10^{-15}, consistent with tail ~ (1/n)^3 folded 9 times.
        mpmath.mp.dps = 25
        v = mzv_depth9_weight27_via_borwein_bradley(N=400, dps=25)
        # Loose bound: zeta(3)^9 / 9! ~ 1.44e-5 (product-of-independent-zetas, no ordering)
        zeta3 = mpmath.zeta(3)
        loose_upper = (zeta3 ** 9) / mpmath.factorial(9)
        assert v < loose_upper, f"Lambda_1 = {v} exceeds loose upper bound {loose_upper}"
        # Tight lower bound: v > 10^{-16}
        assert v > mpmath.mpf("1e-16")
        # Tight upper bound: v < 10^{-14}
        assert v < mpmath.mpf("1e-14")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
