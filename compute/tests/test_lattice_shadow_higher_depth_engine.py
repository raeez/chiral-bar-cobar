"""Tests for lattice shadow higher depth from cusp-form dimensions.

The verified surface here is the standard full-level formula

    dim S_k(SL(2,Z)) = 0 for odd k and for even k < 12,
    dim S_k(SL(2,Z)) = floor(k/12) - 1 if k % 12 == 2,
    dim S_k(SL(2,Z)) = floor(k/12) otherwise,

with lattice depth d(V_Lambda) = 3 + dim S_{rank/2}.

In particular, the true full-level values are dim S_26 = 1 and dim S_36 = 3.
"""

from __future__ import annotations

import pytest

from compute.lib.lattice_shadow_higher_depth_engine import (
    dim_cusp_forms,
    shadow_depth_lattice,
)


DIM_CUSP_FORM_CASES = [
    (2, 0),   # VERIFIED: k < 12 gives 0 directly from the formula [DC], standard SL(2,Z) tables / Diamond-Shurman / LMFDB [LT]
    (4, 0),   # VERIFIED: k < 12 gives 0 directly from the formula [DC], standard SL(2,Z) tables / Diamond-Shurman / LMFDB [LT]
    (6, 0),   # VERIFIED: k < 12 gives 0 directly from the formula [DC], standard SL(2,Z) tables / Diamond-Shurman / LMFDB [LT]
    (8, 0),   # VERIFIED: k < 12 gives 0 directly from the formula [DC], standard SL(2,Z) tables / Diamond-Shurman / LMFDB [LT]
    (10, 0),  # VERIFIED: k < 12 gives 0 directly from the formula [DC], standard SL(2,Z) tables / Diamond-Shurman / LMFDB [LT]
    (12, 1),  # VERIFIED: floor(12/12) = 1 [DC], Ramanujan Delta spans S_12 in standard references [LT]
    (14, 0),  # VERIFIED: 14 % 12 = 2 so floor(14/12) - 1 = 0 [DC], standard full-level dimension tables [LT]
    (16, 1),  # VERIFIED: floor(16/12) = 1 [DC], standard full-level dimension tables [LT]
    (18, 1),  # VERIFIED: floor(18/12) = 1 [DC], standard full-level dimension tables [LT]
    (20, 1),  # VERIFIED: floor(20/12) = 1 [DC], standard full-level dimension tables [LT]
    (22, 1),  # VERIFIED: floor(22/12) = 1 [DC], standard full-level dimension tables [LT]
    (24, 2),  # VERIFIED: floor(24/12) = 2 [DC], standard full-level dimension tables [LT]
    (26, 1),  # VERIFIED: 26 % 12 = 2 so floor(26/12) - 1 = 1 [DC], standard full-level dimension tables [LT]
    (36, 3),  # VERIFIED: floor(36/12) = 3 [DC], standard full-level dimension tables [LT]
    (48, 4),  # VERIFIED: floor(48/12) = 4 [DC], standard full-level dimension tables [LT]
]

SHADOW_DEPTH_CASES = [
    (8, 3),   # VERIFIED: 3 + dim S_4 = 3 + 0 = 3 [DC], BB3 audit lattice-depth rule [LT]
    (16, 3),  # VERIFIED: 3 + dim S_8 = 3 + 0 = 3 [DC], BB3 audit lattice-depth rule [LT]
    (24, 4),  # VERIFIED: 3 + dim S_12 = 3 + 1 = 4 [DC], BB3 audit lattice-depth rule [LT]
    (48, 5),  # VERIFIED: 3 + dim S_24 = 3 + 2 = 5 [DC], BB3 audit lattice-depth rule [LT]
    (72, 6),  # VERIFIED: 3 + dim S_36 = 3 + 3 = 6 [DC], BB3 audit lattice-depth rule [LT]
    (96, 7),  # VERIFIED: 3 + dim S_48 = 3 + 4 = 7 [DC], BB3 audit lattice-depth rule [LT]
]


@pytest.mark.parametrize(("k", "expected"), DIM_CUSP_FORM_CASES)
def test_dim_cusp_forms(k: int, expected: int) -> None:
    assert dim_cusp_forms(k) == expected


@pytest.mark.parametrize(("rank", "expected"), SHADOW_DEPTH_CASES)
def test_shadow_depth_lattice(rank: int, expected: int) -> None:
    assert shadow_depth_lattice(rank) == expected


@pytest.mark.parametrize("rank", [4, 12, 14, 18, 44, 95])
def test_shadow_depth_lattice_requires_rank_divisible_by_8(rank: int) -> None:
    with pytest.raises(ValueError):
        shadow_depth_lattice(rank)


def test_shadow_depth_is_non_decreasing_on_even_unimodular_ranks() -> None:
    depths = [shadow_depth_lattice(rank) for rank in range(8, 97, 8)]
    assert depths == sorted(depths)
