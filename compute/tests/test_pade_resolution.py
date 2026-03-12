"""Tests for pade_resolution: conj:virasoro-pade resolution via Padé analysis.

Verifies exact matching lengths for [q/q] diagonal Padé approximants of the
Virasoro bar Hilbert series P_Vir(x) = 4x/(1-x+sqrt(1-2x-3x^2))^2.

Key results:
- Matching length = 2q + 2·𝟙(q ≡ 3 mod 6) for q where Padé exists
- Padé is singular (does not exist) for q ≡ 4,5 mod 6
- Error at first mismatch is always exactly 1
- The original O(√q) conjecture is subsumed: excess is O(1), bounded by 2
"""

import pytest
from sympy import Rational

from compute.lib.pade_resolution import (
    motzkin,
    virasoro_bar_dims,
    virasoro_gf_coefficients,
    diagonal_pade,
    pade_predict,
    matching_length,
    systematic_pade_scan,
    capacity_prediction,
    resolve_virasoro_pade,
)


# ---------------------------------------------------------------------------
# Motzkin numbers
# ---------------------------------------------------------------------------

class TestMotzkin:
    """Verify Motzkin number computation against OEIS A001006."""

    KNOWN_MOTZKIN = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798, 15511]

    def test_motzkin_values(self):
        for n, expected in enumerate(self.KNOWN_MOTZKIN):
            assert motzkin(n) == expected, f"M({n}) = {motzkin(n)}, expected {expected}"

    def test_motzkin_recurrence(self):
        """Verify (n+2)*M(n) = (2n+1)*M(n-1) + 3*(n-1)*M(n-2)."""
        for n in range(2, 20):
            lhs = (n + 2) * motzkin(n)
            rhs = (2 * n + 1) * motzkin(n - 1) + 3 * (n - 1) * motzkin(n - 2)
            assert lhs == rhs, f"Recurrence fails at n={n}"


# ---------------------------------------------------------------------------
# Virasoro bar dimensions
# ---------------------------------------------------------------------------

class TestVirasoroBarDims:
    """Verify bar cohomology dimensions = Motzkin differences."""

    KNOWN_DIMS = [1, 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610]

    def test_bar_dims(self):
        dims = virasoro_bar_dims(10)
        for n, expected in enumerate(self.KNOWN_DIMS):
            assert dims[n] == expected, f"h_{n} = {dims[n]}, expected {expected}"

    def test_dim_as_motzkin_difference(self):
        """h_n = M(n+1) - M(n) for n >= 1."""
        dims = virasoro_bar_dims(15)
        for n in range(1, 16):
            assert dims[n] == motzkin(n + 1) - motzkin(n)


# ---------------------------------------------------------------------------
# Padé approximant
# ---------------------------------------------------------------------------

class TestDiagonalPade:
    """Test [q/q] Padé computation."""

    def test_pade_q1(self):
        """[1/1] Padé should exist and match through degree 2."""
        coeffs = virasoro_gf_coefficients(10)
        pade = diagonal_pade(coeffs, 1)
        assert pade is not None
        assert pade["order"] == 1
        assert len(pade["num"]) == 2
        assert len(pade["den"]) == 2

    def test_pade_q3(self):
        """[3/3] Padé should exist (the original spurious recurrence)."""
        coeffs = virasoro_gf_coefficients(15)
        pade = diagonal_pade(coeffs, 3)
        assert pade is not None
        assert pade["order"] == 3

    def test_pade_q4_singular(self):
        """[4/4] Padé should be singular (q ≡ 4 mod 6)."""
        coeffs = virasoro_gf_coefficients(20)
        pade = diagonal_pade(coeffs, 4)
        # Should be None (singular) or raise
        assert pade is None

    def test_pade_q5_singular(self):
        """[5/5] Padé should be singular (q ≡ 5 mod 6)."""
        coeffs = virasoro_gf_coefficients(20)
        pade = diagonal_pade(coeffs, 5)
        assert pade is None

    def test_pade_prediction_q3(self):
        """[3/3] Padé should predict coefficients via recurrence."""
        coeffs = virasoro_gf_coefficients(15)
        pade = diagonal_pade(coeffs, 3)
        assert pade is not None
        predictions = pade_predict(pade, coeffs[:7], 5)
        assert len(predictions) == 5
        # First prediction (degree 7) should match exactly
        assert predictions[0] == coeffs[7]
        # Prediction at degree 8 should match exactly (excess = 2)
        assert predictions[1] == coeffs[8]


# ---------------------------------------------------------------------------
# Matching length — the core conjecture resolution
# ---------------------------------------------------------------------------

class TestMatchingLength:
    """Test matching lengths for [q/q] Padé.

    Key result: excess = 2 if q ≡ 3 mod 6, else 0,
    with Padé singular at q ≡ 4,5 mod 6.
    """

    def test_q1_match(self):
        r = matching_length(1)
        assert r["match_through"] == 2
        assert r["excess"] == 0
        assert r["error_at_mismatch"] == 1

    def test_q2_match(self):
        r = matching_length(2)
        assert r["match_through"] == 4
        assert r["excess"] == 0
        assert r["error_at_mismatch"] == 1

    def test_q3_match_excess2(self):
        """q=3: the original observation. Matches through 8, excess 2."""
        r = matching_length(3)
        assert r["match_through"] == 8
        assert r["excess"] == 2
        assert r["first_mismatch"] == 9
        assert r["error_at_mismatch"] == 1

    def test_q4_singular(self):
        r = matching_length(4)
        assert "error" in r  # singular

    def test_q5_singular(self):
        r = matching_length(5)
        assert "error" in r  # singular

    def test_q6_match(self):
        r = matching_length(6, max_terms=40)
        assert r["match_through"] == 12
        assert r["excess"] == 0
        assert r["error_at_mismatch"] == 1

    def test_q7_match(self):
        r = matching_length(7, max_terms=40)
        assert r["match_through"] == 14
        assert r["excess"] == 0

    def test_q8_match(self):
        r = matching_length(8, max_terms=40)
        assert r["match_through"] == 16
        assert r["excess"] == 0

    def test_q9_match_excess2(self):
        """q=9 ≡ 3 mod 6: excess = 2."""
        r = matching_length(9, max_terms=50)
        assert r["match_through"] == 20
        assert r["excess"] == 2
        assert r["error_at_mismatch"] == 1

    @pytest.mark.slow
    def test_period6_pattern_q1_to_18(self):
        """Verify the full period-6 pattern through q=18 (3 complete periods)."""
        for q in range(1, 19):
            r = matching_length(q, max_terms=4 * q + 20)
            mod6 = q % 6
            if mod6 in (4, 5):
                assert "error" in r, f"q={q} should be singular"
            elif mod6 == 3:
                assert r.get("excess") == 2, f"q={q}: excess should be 2"
                assert r.get("error_at_mismatch") == 1, f"q={q}: error should be 1"
            else:
                assert r.get("excess") == 0, f"q={q}: excess should be 0"
                assert r.get("error_at_mismatch") == 1, f"q={q}: error should be 1"


# ---------------------------------------------------------------------------
# Error always 1
# ---------------------------------------------------------------------------

class TestErrorAlwaysOne:
    """The error at first mismatch is always exactly 1."""

    @pytest.mark.parametrize("q", [1, 2, 3, 6, 7, 8, 9, 12, 13, 14, 15])
    def test_error_is_one(self, q):
        r = matching_length(q, max_terms=4 * q + 20)
        if "error" not in r:  # skip singular
            assert r["error_at_mismatch"] == 1, (
                f"q={q}: error = {r['error_at_mismatch']}, expected 1"
            )


# ---------------------------------------------------------------------------
# Capacity theory
# ---------------------------------------------------------------------------

class TestCapacityTheory:
    """Verify capacity theory computations."""

    def test_branch_points(self):
        cap = capacity_prediction()
        assert cap["branch_points"] == (Rational(-1), Rational(1, 3))

    def test_log_capacity(self):
        """Logarithmic capacity of [-1, 1/3] = 1/3."""
        cap = capacity_prediction()
        assert cap["log_capacity"] == Rational(1, 3)

    def test_radius_of_convergence(self):
        cap = capacity_prediction()
        assert cap["radius_of_convergence"] == Rational(1, 3)

    def test_capacity_ratio(self):
        """cap/R = 1: branch cut fills the disk."""
        cap = capacity_prediction()
        assert cap["capacity_ratio"] == 1


# ---------------------------------------------------------------------------
# Integration: full resolution
# ---------------------------------------------------------------------------

class TestResolution:
    """Test the full resolve_virasoro_pade pipeline."""

    def test_resolution_runs(self):
        result = resolve_virasoro_pade(max_q=3)
        assert "scan" in result
        assert "capacity" in result
        assert "verdict" in result

    def test_excess_bounded(self):
        """Excess is O(1), not O(√q)."""
        result = resolve_virasoro_pade(max_q=9)
        excesses = result["scan"]["excesses"]
        qs = result["scan"]["qs"]
        for q, e in zip(qs, excesses):
            if e is not None:
                assert e <= 2, f"q={q}: excess = {e}, should be ≤ 2"
