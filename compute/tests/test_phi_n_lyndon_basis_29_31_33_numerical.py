"""Tests for ``phi_n_lyndon_basis_29_31_33_numerical``.

Verifies:
  - Padovan dimensions at $n = 29, 31, 33$: $(1081, 1897, 3329)$.
  - mod-$8$ admissibility continuation: $\\{27, 29, 35, 37, 43, 45\\}$
    in the range $[27, 50]$.
  - Broadhurst--Kreimer depth rows at $n = 29, 31, 33$ with row-sum
    Padovan identity.
  - Bi-gradings of the canonical Lambda bases at (29, 9), (31, 9),
    (33, 11).
  - Numerical values of primitives via nested truncation, with
    multi-path verification (parity, BK truncation invariance,
    zeta(3,3) closed-form cross-check).

Author: Raeez Lorgat.
"""

from __future__ import annotations

import mpmath
import pytest

from compute.lib.phi_n_lyndon_basis_29_31_33_numerical import (
    LAMBDA_BASIS_29_9_CANONICAL,
    LAMBDA_BASIS_31_9_CANONICAL,
    LAMBDA_BASIS_33_11_CANONICAL,
    admissibility_extension_theorem_data,
    admissible_continuation,
    bk_depth_extract_29_33,
    bk_padovan_rowsum_check_29_33,
    is_admissible_mod8,
    lambda_1_29_numerical,
    lambda_1_31_numerical,
    lambda_1_33_11_numerical,
    padovan_dimensions_29_33,
    verify_bigradings_29_9,
    verify_bigradings_31_9,
    verify_bigradings_33_11,
    verify_padovan_29_31_33,
    verify_primitives_four_voice,
)
from compute.lib.phi_n_lyndon_basis_27_9_numerical import bk_coefficient


class TestPadovanDimensions:
    """Padovan dimensions at n = 29, 31, 33."""

    def test_padovan_29_31_33_values(self) -> None:
        assert verify_padovan_29_31_33() == (1081, 1897, 3329)

    def test_padovan_recurrence_holds(self) -> None:
        d = padovan_dimensions_29_33()
        for n in range(29, 34):
            assert d[n] == d[n - 2] + d[n - 3], (
                f"Padovan recurrence fails at n={n}"
            )

    def test_padovan_seed_matches_27(self) -> None:
        d = padovan_dimensions_29_33()
        # Cross-check with the 27-9 manuscript seed.
        assert d[25] == 351
        assert d[26] == 465
        assert d[27] == 616
        assert d[28] == 816


class TestMod8Admissibility:
    """Humbert--Heegner mod-8 admissibility filter."""

    def test_29_admissible(self) -> None:
        assert is_admissible_mod8(29)

    def test_31_not_admissible(self) -> None:
        assert not is_admissible_mod8(31)

    def test_33_not_admissible(self) -> None:
        assert not is_admissible_mod8(33)

    def test_continuation_to_50(self) -> None:
        expected = [27, 29, 35, 37, 43, 45]
        assert admissible_continuation(n_min=27, n_max=50) == expected

    def test_admissibility_data_structure(self) -> None:
        data = admissibility_extension_theorem_data(n_max=50)
        assert 27 in data["admissible"]
        assert 29 in data["admissible"]
        assert 31 in data["non_admissible"]
        assert 33 in data["non_admissible"]


class TestBKDepthRows:
    """Broadhurst--Kreimer depth-graded coefficients at n = 29, 31, 33."""

    def test_D_29_9(self) -> None:
        assert bk_coefficient(29, 9, N=50, K=20) == 42

    def test_D_31_9(self) -> None:
        assert bk_coefficient(31, 9, N=50, K=20) == 150

    def test_D_33_9(self) -> None:
        assert bk_coefficient(33, 9, N=50, K=20) == 398

    def test_D_33_11_first_depth_11_onset(self) -> None:
        # First non-vanishing depth-11 BK coefficient in the tower.
        assert bk_coefficient(33, 11, N=50, K=20) == 19

    def test_depth_11_empty_below_33(self) -> None:
        for n in range(11, 33):
            assert bk_coefficient(n, 11, N=50, K=20) == 0, (
                f"depth-11 should be empty at n={n}"
            )

    def test_parity_vanishing(self) -> None:
        # n + d odd forces D_{n, d} = 0.
        assert bk_coefficient(29, 8, N=50, K=20) == 0
        assert bk_coefficient(31, 10, N=50, K=20) == 0
        assert bk_coefficient(33, 10, N=50, K=20) == 0
        assert bk_coefficient(29, 10, N=50, K=20) == 0
        assert bk_coefficient(33, 8, N=50, K=20) == 0

    def test_rowsum_padovan_identity(self) -> None:
        assert bk_padovan_rowsum_check_29_33()

    def test_full_rows_structure(self) -> None:
        rows = bk_depth_extract_29_33()
        # n=29 row: only odd-depth entries non-zero
        assert rows[29] == (1, 0, 50, 0, 249, 0, 274, 0, 42, 0, 0)
        # n=31 row
        assert rows[31] == (1, 0, 58, 0, 360, 0, 512, 0, 150, 0, 0)
        # n=33 row: depth-11 entry becomes non-zero
        assert rows[33] == (1, 0, 67, 0, 498, 0, 914, 0, 398, 0, 19)


class TestLambdaBasisBigradings:
    """Verify bi-gradings of the canonical Lambda bases."""

    def test_29_9_all_valid(self) -> None:
        verify_bigradings_29_9()

    def test_31_9_all_valid(self) -> None:
        verify_bigradings_31_9()

    def test_33_11_all_valid(self) -> None:
        verify_bigradings_33_11()

    def test_29_9_cardinality_at_least_10(self) -> None:
        # Canonical representatives; BK says 42 in full, we list 10 Lyndon
        # generators that span a working subset modulo stuffle relations.
        assert len(LAMBDA_BASIS_29_9_CANONICAL) == 10

    def test_31_9_cardinality_at_least_10(self) -> None:
        assert len(LAMBDA_BASIS_31_9_CANONICAL) == 10

    def test_33_11_cardinality_nineteen(self) -> None:
        # First depth-11 stratum has D_{33, 11} = 19, and we list all 19.
        assert len(LAMBDA_BASIS_33_11_CANONICAL) == 19

    def test_compositions_unique_29(self) -> None:
        comps = [s for _, s, _ in LAMBDA_BASIS_29_9_CANONICAL]
        assert len(set(comps)) == len(comps)

    def test_compositions_unique_31(self) -> None:
        comps = [s for _, s, _ in LAMBDA_BASIS_31_9_CANONICAL]
        assert len(set(comps)) == len(comps)

    def test_compositions_unique_33(self) -> None:
        comps = [s for _, s, _ in LAMBDA_BASIS_33_11_CANONICAL]
        assert len(set(comps)) == len(comps)


class TestPrimitiveNumerics:
    """Numerical evaluation of Lambda_1 primitives at weight 29, 31, 33."""

    def test_lambda_1_29_order_of_magnitude(self) -> None:
        mpmath.mp.dps = 30
        v = lambda_1_29_numerical(N=300, dps=30)
        # ~ 1.03e-15
        assert v > mpmath.mpf("1e-15")
        assert v < mpmath.mpf("2e-15")

    def test_lambda_1_31_order_of_magnitude(self) -> None:
        mpmath.mp.dps = 30
        v = lambda_1_31_numerical(N=300, dps=30)
        # ~ 1.03e-15 (same order as n=29 because the driving zeta(3)^8
        # tail dominates; f_5 vs f_7 at slot 9 shifts by ~1e-18)
        assert v > mpmath.mpf("1e-15")
        assert v < mpmath.mpf("2e-15")

    def test_lambda_1_33_11_order_of_magnitude(self) -> None:
        mpmath.mp.dps = 30
        v = lambda_1_33_11_numerical(N=300, dps=30)
        # ~ 2.2e-21 (zeta({3}^11) is ~1e6 times smaller than zeta({3}^9))
        assert v > mpmath.mpf("1e-21")
        assert v < mpmath.mpf("5e-21")

    def test_primitives_monotone_increase_with_N(self) -> None:
        """Partial sums of positive-term MZVs monotonely increase in N."""
        mpmath.mp.dps = 25
        for fn in (lambda_1_29_numerical, lambda_1_31_numerical,
                   lambda_1_33_11_numerical):
            v200 = fn(N=200, dps=25)
            v300 = fn(N=300, dps=25)
            assert v300 > v200, f"{fn.__name__}: N=300 < N=200"


class TestMultiPathVerification:
    """Four/seven-voice multi-path verification."""

    def test_verify_primitives_multi_voice_returns_all_paths(self) -> None:
        result = verify_primitives_four_voice(dps=20)
        assert "V1_nested_truncation" in result
        assert "V2_BK" in result
        assert "V3_tail_bound" in result
        assert "V4_parity" in result
        assert "V5_rowsum" in result
        assert "V6_truncation_invariance" in result
        assert "V7_zeta_33_closed" in result

    def test_V2_BK_coefficients_match(self) -> None:
        result = verify_primitives_four_voice(dps=20)
        assert result["V2_BK"]["D_29_9"] == 42
        assert result["V2_BK"]["D_31_9"] == 150
        assert result["V2_BK"]["D_33_9"] == 398
        assert result["V2_BK"]["D_33_11"] == 19

    def test_V4_parity_all_vanish(self) -> None:
        result = verify_primitives_four_voice(dps=20)
        for key, val in result["V4_parity"].items():
            assert val == 0, f"Parity should vanish at {key}, got {val}"

    def test_V5_rowsum_matches_padovan(self) -> None:
        result = verify_primitives_four_voice(dps=20)
        for n in (29, 31, 33):
            entry = result["V5_rowsum"][n]
            assert entry["row_sum"] == entry["padovan_d_n_minus_2"], (
                f"Row sum vs d_{{n-2}} mismatch at n={n}: {entry}"
            )

    def test_V6_truncation_invariance(self) -> None:
        """BK coefficients stable under K -> 2K (well converged)."""
        result = verify_primitives_four_voice(dps=20)
        assert result["V6_truncation_invariance"]["D_29_9_K14"] == \
               result["V6_truncation_invariance"]["D_29_9_K20"] == 42
        assert result["V6_truncation_invariance"]["D_31_9_K14"] == \
               result["V6_truncation_invariance"]["D_31_9_K20"] == 150
        assert result["V6_truncation_invariance"]["D_33_11_K14"] == \
               result["V6_truncation_invariance"]["D_33_11_K20"] == 19

    @pytest.mark.slow
    def test_V7_zeta_33_closed_form(self) -> None:
        result = verify_primitives_four_voice(dps=30)
        rel_err = result["V7_zeta_33_closed"]["relative_error"]
        assert rel_err < mpmath.mpf("1e-4"), (
            f"zeta(3,3) closed-form cross-check relative error {rel_err} "
            f"exceeds 10^{{-4}}"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
