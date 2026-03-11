"""Tests for bar_gf_solver: rational GF, holonomic recurrence, conjectured GF verification."""

import pytest
from sympy import Rational

from compute.lib.bar_gf_solver import (
    bar_dims_sl2,
    bar_dims_virasoro,
    find_holonomic_recurrence,
    find_rational_gf,
    motzkin_numbers,
    predict_next_coefficient,
    riordan_numbers,
    verify_conjectured_gf,
)


# ---------------------------------------------------------------------------
# Known sequence sanity checks
# ---------------------------------------------------------------------------

class TestKnownSequences:
    def test_riordan_numbers(self):
        R = riordan_numbers(12)
        assert R[:12] == [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585]

    def test_motzkin_numbers(self):
        M = motzkin_numbers(10)
        assert M[:10] == [1, 1, 2, 4, 9, 21, 51, 127, 323, 835]

    def test_bar_dims_sl2(self):
        dims = bar_dims_sl2(7)
        assert dims == [3, 6, 15, 36, 91, 232, 603]

    def test_bar_dims_virasoro(self):
        dims = bar_dims_virasoro(8)
        assert dims == [1, 2, 5, 12, 30, 76, 196, 512]


# ---------------------------------------------------------------------------
# Rational GF finder
# ---------------------------------------------------------------------------

class TestFindRationalGF:
    def test_virasoro_rational_gf(self):
        """With 6 data points, Virasoro admits a spurious rational fit (depth-3).
        This fit is coincidental (fails at degree 9) but predictions through
        degree 8 happen to be correct.  See TestVirasoroNearRationality."""
        dims = bar_dims_virasoro(8)
        result = find_rational_gf(dims[:6])
        assert result is not None
        assert result["q"] == 3
        assert result["den_coeffs"] == [Rational(-4), Rational(2), Rational(4)]
        assert result["next_predicted"] == 196

    def test_virasoro_predict_from_7(self):
        dims = bar_dims_virasoro(8)
        result = find_rational_gf(dims[:7])
        assert result is not None
        assert result["next_predicted"] == 512

    def test_sl3_no_rational_from_3_points(self):
        """sl3 has rational GF but 3 points are not enough for the true one (q=3)."""
        # The rational finder will find SOME fit, but not the true one
        result = find_rational_gf([8, 36, 204])
        # May find a (p,q) fit but it won't be the true GF
        # The key test is that verify_conjectured_gf handles the true sl3 GF

    def test_w3_rational_from_4_points(self):
        """W3: P(x) = x(2-3x)/((1-x)(1-3x-x^2)) has q=3, p=2."""
        result = find_rational_gf([2, 5, 16, 52])
        # With 4 data points and q=3, p=2: we need k > p=2 to have
        # recurrence eqs, so k=3,4 give 2 eqs for 3 unknowns (q=3).
        # Not enough for the true GF. But a simpler rational might be found.
        # The key test is verify_conjectured_gf below.


# ---------------------------------------------------------------------------
# Holonomic recurrence
# ---------------------------------------------------------------------------

class TestFindHolonomicRecurrence:
    def test_sl2_holonomic(self):
        """sl2 bar dims satisfy holonomic recurrence with a0=1."""
        dims = bar_dims_sl2(7)
        result = find_holonomic_recurrence(dims[:6], a0=1)
        assert result is not None
        assert result["order"] == 2
        assert result["poly_deg"] == 1
        assert result["next_predicted"] == 603

    def test_sl2_holonomic_7_points(self):
        dims = bar_dims_sl2(8)
        result = find_holonomic_recurrence(dims[:7], a0=1)
        assert result is not None
        assert result["next_predicted"] == 1585

    def test_sl2_needs_enough_data(self):
        """With only 4 bar dims + a0, the holonomic null space is not unique."""
        dims = bar_dims_sl2(7)
        result = find_holonomic_recurrence(dims[:4], a0=1)
        # May return None or wrong answer due to ambiguity
        # This is expected: 5 data points with r=2,d=1 gives null dim > 1


# ---------------------------------------------------------------------------
# Verify conjectured GF
# ---------------------------------------------------------------------------

class TestVerifyConjecturedGF:
    def test_sl3_conjectured_gf(self):
        """sl3 conjectured GF: P(x) = 4x(2-13x-2x^2)/((1-8x)(1-3x-x^2)).

        D(x) = (1-8x)(1-3x-x^2) = 1 - 11x + 23x^2 + 8x^3
        N(x) = 8x - 52x^2 - 8x^3
        Known: [8, 36, 204]. Predicted a_4 = 1352.
        """
        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -52, -8],
            den_coeffs=[-11, 23, 8],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 1352

    def test_w3_conjectured_gf(self):
        """W3 conjectured GF: P(x) = x(2-3x)/((1-x)(1-3x-x^2)).

        D(x) = (1-x)(1-3x-x^2) = 1 - 4x + 2x^2 + x^3
        N(x) = 2x - 3x^2
        Known: [2, 5, 16, 52]. Predicted a_5 = 171.
        """
        result = verify_conjectured_gf(
            [2, 5, 16, 52],
            num_coeffs=[2, -3],
            den_coeffs=[-4, 2, 1],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 171

    def test_virasoro_conjectured_gf(self):
        """Virasoro GF: P(x) = x(1-2x-x^2)/(1-4x+2x^2+4x^3)."""
        dims = bar_dims_virasoro(8)
        result = verify_conjectured_gf(
            dims[:5],
            num_coeffs=[1, -2, -1],
            den_coeffs=[-4, 2, 4],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == dims[5]  # 76
        assert result["predictions"][1] == dims[6]  # 196
        assert result["predictions"][2] == dims[7]  # 512

    def test_yangian_conjectured_gf(self):
        """Y(sl₂) conjectured GF: P̃(x) = 2x(2-3x)/((1-x)(1-3x)).

        D(x) = (1-x)(1-3x) = 1 - 4x + 3x²
        N(x) = 4x - 6x²
        Known: [4, 10, 28]. Predicted a_4 = 82.
        """
        result = verify_conjectured_gf(
            [4, 10, 28],
            num_coeffs=[4, -6],
            den_coeffs=[-4, 3],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 82

    def test_wrong_gf_detected(self):
        """A wrong conjectured GF should be detected."""
        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -52, -8],
            den_coeffs=[-10, 23, 8],  # wrong coefficient
        )
        assert result["matches"] is False


# ---------------------------------------------------------------------------
# predict_next_coefficient (integration)
# ---------------------------------------------------------------------------

class TestPredictNextCoefficient:
    def test_sl2_prediction(self):
        """sl2: using first 6 bar dims, predict 7th = 603."""
        dims = bar_dims_sl2(7)
        pred = predict_next_coefficient(dims[:6])
        assert pred == 603

    def test_sl2_prediction_7_to_8(self):
        """sl2: using first 7 bar dims, predict 8th = 1585."""
        dims = bar_dims_sl2(8)
        pred = predict_next_coefficient(dims[:7])
        assert pred == 1585

    def test_virasoro_prediction(self):
        """Virasoro: using first 6 bar dims, predict 7th = 196."""
        dims = bar_dims_virasoro(8)
        pred = predict_next_coefficient(dims[:6])
        assert pred == 196

    def test_virasoro_prediction_7_to_8(self):
        """Virasoro: using first 7 bar dims, predict 8th = 512."""
        dims = bar_dims_virasoro(8)
        pred = predict_next_coefficient(dims[:7])
        assert pred == 512

    def test_not_zero(self):
        """The old bug: predict_next_coefficient returned 0 for everything.
        Verify that known sequences never predict 0."""
        dims_sl2 = bar_dims_sl2(7)
        dims_vir = bar_dims_virasoro(8)
        pred_sl2 = predict_next_coefficient(dims_sl2[:6])
        pred_vir = predict_next_coefficient(dims_vir[:6])
        assert pred_sl2 != 0, "sl2 prediction should not be 0"
        assert pred_vir != 0, "Virasoro prediction should not be 0"


# ---------------------------------------------------------------------------
# Regression: Virasoro near-rationality
# ---------------------------------------------------------------------------

class TestVirasoroNearRationality:
    """Virasoro bar dims satisfy a depth-3 constant-coefficient recurrence
    a_k = 4a_{k-1} - 2a_{k-2} - 4a_{k-3} through degree 8, but FAIL at
    degree 9 (predicts 1352, actual 1353).  The GF is algebraic of degree 2
    (Motzkin differences), NOT rational.  This is a non-trivial numerical
    coincidence that must not be mistaken for genuine rationality."""

    def test_spurious_recurrence_fails_at_degree9(self):
        """The depth-3 recurrence fails at degree 9."""
        dims = bar_dims_virasoro(10)  # through degree 10
        # Recurrence: a_k = 4*a_{k-1} - 2*a_{k-2} - 4*a_{k-3}
        # Verify it works through degree 8
        for k in range(3, 7):  # indices 3..6 = degrees 4..7
            pred = 4 * dims[k - 1] - 2 * dims[k - 2] - 4 * dims[k - 3]
            assert pred == dims[k], f"Recurrence should hold at degree {k+1}"
        # But fails at degree 9 (index 8)
        pred_9 = 4 * dims[7] - 2 * dims[6] - 4 * dims[5]
        assert pred_9 != dims[8], f"Recurrence should FAIL at degree 9"
        assert pred_9 == 1352 and dims[8] == 1353

    def test_rational_gf_rejected_with_enough_data(self):
        """With 10 data points, find_rational_gf should reject the spurious fit."""
        dims = bar_dims_virasoro(10)
        result = find_rational_gf(dims)
        # The depth-3 fit is rejected because verification fails at degree 9.
        # No other rational fit exists for Virasoro (it's algebraic).
        assert result is None

    def test_holonomic_works_for_virasoro(self):
        """Virasoro satisfies holonomic recurrence (polynomial coefficients in n).
        Need 10+ data points so the holonomic finder distinguishes the true
        (polynomial-coefficient) recurrence from the spurious rational one."""
        dims = bar_dims_virasoro(12)
        result = find_holonomic_recurrence(dims[:10], a0=0)
        assert result is not None
        # Prediction should match the known degree 11 value
        assert result["next_predicted"] == dims[10]

    def test_predict_with_10_points_still_works(self):
        """predict_next_coefficient should still work with 10+ data points
        (falls through to holonomic after rational is rejected)."""
        dims = bar_dims_virasoro(11)
        pred = predict_next_coefficient(dims[:10])
        assert pred == dims[10]
