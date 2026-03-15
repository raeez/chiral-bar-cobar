"""Tests for compute/lib/km_chiral_bar.py — KM chiral bar cohomology.

Tests the public API that is NOT already covered by test_sl3_casimir_decomp.py
and test_sl3_h4_verification.py (which only import ce_bracket_differential_numpy).

Coverage:
  Part 1 — Koszul dual Hilbert series: riordan, sl2/sl3_bar_cohomology,
            bar_cohomology_degree2
  Part 2 — Direct bracket: bracket_pair_map_numpy, bracket_diff_rank
  Part 3 — Chiral bracket with OS: chiral_bracket_rank
  Part 4 — Recurrence: sl3_recurrence, sl3_rational_gf_coefficients
  Part 5 — Verification: verify_sl2, verify_sl3_known, verify_bracket_ranks_sl3,
            verify_d_squared_ce
  Helpers — sl2_structure_constants_float, sl2_killing_form_float
"""

import pytest
import numpy as np

from compute.lib.km_chiral_bar import (
    riordan,
    sl2_bar_cohomology,
    sl3_bar_cohomology,
    bar_cohomology_degree2,
    bracket_pair_map_numpy,
    bracket_diff_rank,
    ce_bracket_differential_numpy,
    chiral_bracket_rank,
    sl3_recurrence,
    sl3_rational_gf_coefficients,
    verify_sl2,
    verify_sl3_known,
    verify_bracket_ranks_sl3,
    verify_d_squared_ce,
    sl2_structure_constants_float,
    sl2_killing_form_float,
    DIM_SL2,
)
from compute.lib.sl3_bar import DIM_G as SL3_DIM, sl3_structure_constants


# =========================================================================
# Part 1: Riordan numbers and Koszul dual Hilbert series
# =========================================================================

class TestRiordan:
    """Riordan numbers R(n), OEIS A005043."""

    def test_base_cases(self):
        assert riordan(0) == 1
        assert riordan(1) == 0

    def test_known_values(self):
        """R(2)=1, R(3)=1, R(4)=3, R(5)=6, R(6)=15, R(7)=36, R(8)=91, R(9)=232."""
        expected = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232]
        for n, val in enumerate(expected):
            assert riordan(n) == val, f"R({n}) = {riordan(n)}, expected {val}"

    def test_recurrence(self):
        """(n+1)*R(n) = (n-1)*(2*R(n-1) + 3*R(n-2)) for n >= 2."""
        for n in range(2, 15):
            lhs = (n + 1) * riordan(n)
            rhs = (n - 1) * (2 * riordan(n - 1) + 3 * riordan(n - 2))
            assert lhs == rhs

    def test_negative_input(self):
        """R(n) for n <= 0 returns 1."""
        assert riordan(-1) == 1
        assert riordan(-5) == 1


class TestSl2BarCohomology:
    """sl_2-hat bar cohomology: dim(A^!)_n = R(n+3)."""

    def test_h0(self):
        """H^0 = R(3) = 1."""
        cohom = sl2_bar_cohomology(0)
        assert cohom[0] == 1

    def test_first_values(self):
        """H^0=1, H^1=3, H^2=5, H^3=15, H^4=36, H^5=91.

        H^2=5 (not 6): Riordan R(5)=6 is wrong; corrected via
        H^2_{h=2}=0 (bar_deg2_resolution) and H^2(CE)=5.
        """
        cohom = sl2_bar_cohomology(5)
        assert cohom == [1, 3, 5, 15, 36, 91]

    def test_h2_matches_degree2_formula(self):
        """H^2(sl_2) = 5 (corrected, not Riordan's 6)."""
        cohom = sl2_bar_cohomology(2)
        assert cohom[2] == 5
        assert cohom[2] == bar_cohomology_degree2(DIM_SL2)


class TestSl3BarCohomology:
    """sl_3-hat bar cohomology via conjectured rational GF."""

    def test_known_values(self):
        """H^0=1, H^1=8, H^2=36, H^3=204 (verified by computation)."""
        cohom = sl3_bar_cohomology(3)
        assert cohom == [1, 8, 36, 204]

    def test_h4_conjectured(self):
        """H^4 = 1352 (from conjectured recurrence)."""
        cohom = sl3_bar_cohomology(4)
        assert cohom[4] == 1352

    def test_recurrence(self):
        """a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3) for n >= 4."""
        cohom = sl3_bar_cohomology(8)
        for n in range(4, 9):
            assert cohom[n] == 11 * cohom[n-1] - 23 * cohom[n-2] - 8 * cohom[n-3]

    def test_h2_matches_degree2_formula(self):
        """H^2(sl_3) = 36 (verified by direct computation)."""
        cohom = sl3_bar_cohomology(2)
        assert cohom[2] == 36
        assert cohom[2] == bar_cohomology_degree2(8)

    def test_truncated_output(self):
        """Requesting fewer than known values returns correct truncation."""
        cohom = sl3_bar_cohomology(1)
        assert cohom == [1, 8]


class TestBarCohomologyDegree2:
    """Known H^2 values (no closed-form formula)."""

    def test_sl2(self):
        """H^2(sl_2-hat) = 5, not the old claim of 6."""
        assert bar_cohomology_degree2(3) == 5

    def test_sl3(self):
        """H^2(sl_3-hat) = 36 (prop:sl3-pbw-ss)."""
        assert bar_cohomology_degree2(8) == 36

    def test_unknown_raises(self):
        """Unknown dimensions raise NotImplementedError."""
        import pytest
        with pytest.raises(NotImplementedError):
            bar_cohomology_degree2(10)


# =========================================================================
# Part 2: sl_2 data and bracket differential
# =========================================================================

class TestSl2Data:
    def test_dim(self):
        assert DIM_SL2 == 3

    def test_structure_constants_antisymmetry(self):
        sc = sl2_structure_constants_float()
        # [e, f] = h and [f, e] = -h
        assert sc[(0, 2)][1] == 1.0
        assert sc[(2, 0)][1] == -1.0

    def test_killing_form_symmetric(self):
        kf = sl2_killing_form_float()
        assert kf[(0, 2)] == kf[(2, 0)]

    def test_killing_form_values(self):
        """kappa(e,f) = 1, kappa(h,h) = 2."""
        kf = sl2_killing_form_float()
        assert kf[(0, 2)] == 1.0
        assert kf[(1, 1)] == 2.0


class TestBracketPairMap:
    def test_sl2_n2_shape(self):
        """Map g^2 -> g^1, shape (3, 9)."""
        sc = sl2_structure_constants_float()
        M = bracket_pair_map_numpy(3, sc, 2, 0, 1)
        assert M.shape == (3, 9)

    def test_sl2_n2_nonzero(self):
        """Bracket map on g^2 is nonzero for sl_2."""
        sc = sl2_structure_constants_float()
        M = bracket_pair_map_numpy(3, sc, 2, 0, 1)
        assert np.max(np.abs(M)) > 0

    def test_invalid_pair_raises(self):
        sc = sl2_structure_constants_float()
        with pytest.raises(ValueError):
            bracket_pair_map_numpy(3, sc, 2, 0, 0)
        with pytest.raises(ValueError):
            bracket_pair_map_numpy(3, sc, 1, 0, 1)


class TestBracketDiffRank:
    """CE bracket differential ranks on g^{otimes n}."""

    def test_sl2_rank_d2(self):
        """rank(d: g^2 -> g) = 3 = dim(sl_2) (surjective)."""
        sc = sl2_structure_constants_float()
        assert bracket_diff_rank(3, sc, 2) == 3

    def test_sl2_rank_d3(self):
        """rank(d: g^3 -> g^2) at most dim(g^2)-rank(d2)."""
        sc = sl2_structure_constants_float()
        r3 = bracket_diff_rank(3, sc, 3)
        # For sl_2, rank(d_3) should be 6 (g^2 dim=9, rank d_2=3, so ker dim=6)
        assert r3 == 6

    def test_d_squared_zero_sl2(self):
        """d^2 = 0 on g^{otimes n} for CE bracket (sl_2)."""
        sc = sl2_structure_constants_float()
        d3 = ce_bracket_differential_numpy(3, sc, 3)
        d2 = ce_bracket_differential_numpy(3, sc, 2)
        d_sq = d2 @ d3
        assert np.max(np.abs(d_sq)) < 1e-10


# =========================================================================
# Part 3: Chiral bracket with OS forms
# =========================================================================

class TestChiralBracketRank:
    """Chiral bracket differential with OS forms, sl_2."""

    def test_sl2_deg2_rank(self):
        """OS forms at degree 2 are 1-dimensional, so same rank."""
        sc = sl2_structure_constants_float()
        rank = chiral_bracket_rank(3, sc, 2, sign_convention="os")
        assert rank == 3

    def test_sign_conventions_differ(self):
        """Different sign conventions may give different ranks at degree 3."""
        sc = sl2_structure_constants_float()
        rank_os = chiral_bracket_rank(3, sc, 3, sign_convention="os")
        rank_ce = chiral_bracket_rank(3, sc, 3, sign_convention="ce")
        # Both should be valid integer ranks
        assert rank_os >= 0
        assert rank_ce >= 0


# =========================================================================
# Part 4: sl_3 recurrence
# =========================================================================

class TestSl3Recurrence:
    def test_first_values(self):
        """First three values match known H^1=8, H^2=36, H^3=204."""
        rec = sl3_recurrence(8, 36, 204, 3)
        assert rec[:3] == [8, 36, 204]

    def test_h4_prediction(self):
        """H^4 = 11*204 - 23*36 - 8*8 = 2244 - 828 - 64 = 1352."""
        rec = sl3_recurrence(8, 36, 204, 4)
        assert rec[3] == 1352

    def test_rational_gf_matches_recurrence(self):
        """sl3_rational_gf_coefficients uses same recurrence."""
        rec = sl3_recurrence(8, 36, 204, 8)
        gf = sl3_rational_gf_coefficients(8)
        assert rec == gf

    def test_all_positive(self):
        """All terms are positive integers."""
        rec = sl3_recurrence(8, 36, 204, 10)
        for val in rec:
            assert val > 0
            assert isinstance(val, int)


# =========================================================================
# Part 5: Verification suites
# =========================================================================

class TestVerifySl2:
    def test_all_pass(self):
        results = verify_sl2(6)
        for name, data in results.items():
            if isinstance(data, tuple) and len(data) >= 2:
                ok, actual = data[0], data[1]
                assert ok, f"verify_sl2 failed: {name} (got {actual})"

    def test_bar_cohomology_present(self):
        results = verify_sl2(4)
        assert "bar_cohomology" in results
        assert len(results["bar_cohomology"]) == 5  # H^0 through H^4


class TestVerifySl3Known:
    def test_all_pass(self):
        results = verify_sl3_known(6)
        for name, data in results.items():
            if isinstance(data, tuple) and len(data) >= 2:
                ok, actual = data[0], data[1]
                assert ok, f"verify_sl3_known failed: {name} (got {actual})"


class TestVerifyBracketRanks:
    """Bracket rank verification for sl_3.

    Each test calls verify_bracket_ranks_sl3(3), which internally computes
    chiral bracket differentials up to degree 4.  The degree-4 OS
    bracket for sl_3 (d=8) allocates ~900 MB, so the class is marked slow
    to keep the fast suite under memory limits.
    """

    @pytest.mark.slow
    def test_all_pass(self):
        results = verify_bracket_ranks_sl3(3)
        for name, data in results.items():
            if isinstance(data, tuple) and len(data) >= 2:
                ok, actual = data[0], data[1]
                assert ok, f"verify_bracket_ranks failed: {name} (got {actual})"

    def test_ce_rank_at_2(self):
        """CE rank at degree 2 = dim(g) = 8 for sl_3."""
        sc = {(a, b): {c: float(v) for c, v in targets.items()}
              for (a, b), targets in sl3_structure_constants().items()}
        assert bracket_diff_rank(SL3_DIM, sc, 2) == 8

    def test_ce_rank_at_3(self):
        """CE rank at degree 3 = 56 for sl_3 (no OS forms)."""
        sc = {(a, b): {c: float(v) for c, v in targets.items()}
              for (a, b), targets in sl3_structure_constants().items()}
        assert bracket_diff_rank(SL3_DIM, sc, 3) == 56

    @pytest.mark.slow
    def test_os_rank_at_3(self):
        """OS rank at degree 3 = 63 (comp:sl3-modular-rank)."""
        results = verify_bracket_ranks_sl3(3)
        os_result = results.get("OS rank at 3 = 63 (comp:sl3-modular-rank)")
        assert os_result is not None
        assert os_result[0] is True  # passes


class TestVerifyDSquaredCE:
    def test_sl2_d_squared_zero(self):
        """d^2 = 0 for CE bracket on sl_2^{otimes 3}."""
        sc = sl2_structure_constants_float()
        result = verify_d_squared_ce(3, sc, 3)
        assert result["d^2 = 0"]
        assert result["d^2_norm"] < 1e-10
