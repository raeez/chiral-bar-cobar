"""Tests for type I (odd unimodular) lattice shadow depth engine.

Validates:
  1. Cusp form dimensions for SL(2,Z) against known tables
  2. Cusp form dimensions for Gamma_0(4) with trivial and chi_{-4} character
  3. Unified dim_cusp_type_I formula for even and odd ranks
  4. Shadow depth formula d = 3 + dim_cusp_type_I(r) at key lattices
  5. Comparison with type II depths at ranks divisible by 8
  6. Depth correction delta = d_I - d_II
  7. Monotonicity and structural properties
  8. Census consistency

References:
  Diamond-Shurman, "A First Course in Modular Forms" (2005), Ch. 3, 6
  Shimura, "On modular forms of half integral weight" (1973)
  Kohnen, "Newforms of half-integral weight" (1982)
  LMFDB Modular Forms Database (https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/)
  lattice_shadow_higher_depth_engine.py (type II baseline)
"""

from __future__ import annotations

import pytest

from compute.lib.lattice_type_i_shadow_depth_engine import (
    dim_cusp_forms_sl2z,
    dim_cusp_forms_gamma0_4,
    dim_cusp_type_I,
    shadow_depth_type_I,
    shadow_depth_type_II,
    depth_correction,
    shadow_depth_census,
)


# ============================================================================
# 1. SL(2,Z) cusp form dimensions (cross-check with lattice_shadow_higher_depth_engine)
# ============================================================================

SL2Z_CUSP_CASES = [
    # (weight, expected_dim)
    # VERIFIED: [DC] standard dimension formula; [LT] Diamond-Shurman Table 3.3 / LMFDB
    (2, 0),
    (4, 0),
    (6, 0),
    (8, 0),
    (10, 0),
    (12, 1),   # VERIFIED: [DC] Delta spans S_12; [LT] Ramanujan 1916
    (14, 0),   # VERIFIED: [DC] 14 mod 12 = 2, floor(14/12)-1 = 0; [LT] LMFDB
    (16, 1),   # VERIFIED: [DC] floor(16/12) = 1; [LT] LMFDB
    (18, 1),
    (20, 1),
    (22, 1),
    (24, 2),   # VERIFIED: [DC] floor(24/12) = 2; [LT] LMFDB
    (26, 1),   # VERIFIED: [DC] 26 mod 12 = 2, floor(26/12)-1 = 1; [LT] LMFDB
    (36, 3),   # VERIFIED: [DC] floor(36/12) = 3; [LT] LMFDB
    (48, 4),   # VERIFIED: [DC] floor(48/12) = 4; [LT] LMFDB
]


@pytest.mark.parametrize(("k", "expected"), SL2Z_CUSP_CASES)
def test_dim_cusp_forms_sl2z(k: int, expected: int) -> None:
    assert dim_cusp_forms_sl2z(k) == expected


def test_sl2z_odd_weight_zero() -> None:
    """Odd weight cusp forms for SL(2,Z) are always zero."""
    for k in [1, 3, 5, 7, 9, 11, 13, 15]:
        assert dim_cusp_forms_sl2z(k) == 0


# ============================================================================
# 2. Gamma_0(4) cusp form dimensions
# ============================================================================

GAMMA04_EVEN_CASES = [
    # (weight, expected_dim) for even weight, trivial character
    # VERIFIED: [DC] dim S_k(Gamma_0(4)) = max(0, k/2 - 2) via Stein Thm 6.1
    #           with g=0, c=3, eps_2=eps_3=0;
    #           [LT] LMFDB level 4 holomorphic forms
    (2, 0),    # VERIFIED: [DC] genus 0; [LT] LMFDB
    (4, 0),    # VERIFIED: [DC] 4/2 - 2 = 0; [LT] LMFDB
    (6, 1),    # VERIFIED: [DC] 6/2 - 2 = 1; [LT] LMFDB
    (8, 2),    # VERIFIED: [DC] 8/2 - 2 = 2; [LT] LMFDB
    (10, 3),   # VERIFIED: [DC] 10/2 - 2 = 3; [LT] LMFDB
    (12, 4),   # VERIFIED: [DC] 12/2 - 2 = 4; [LT] LMFDB
    (14, 5),
    (16, 6),
    (24, 10),
]


@pytest.mark.parametrize(("k", "expected"), GAMMA04_EVEN_CASES)
def test_dim_cusp_gamma04_even(k: int, expected: int) -> None:
    assert dim_cusp_forms_gamma0_4(k, even_weight=True) == expected


GAMMA04_ODD_CASES = [
    # (weight, expected_dim) for odd weight, character chi_{-4}
    # VERIFIED: [DC] dim S_k(Gamma_0(4), chi_{-4}) = max(0, (k-3)/2) via
    #           Cohen-Oesterle dimension formula; [LT] LMFDB level 4 nebentypus
    (3, 0),    # VERIFIED: [DC] (3-3)/2 = 0; [LT] LMFDB
    (5, 1),    # VERIFIED: [DC] (5-3)/2 = 1; [LT] LMFDB
    (7, 2),    # VERIFIED: [DC] (7-3)/2 = 2; [LT] LMFDB
    (9, 3),    # VERIFIED: [DC] (9-3)/2 = 3; [LT] LMFDB
    (11, 4),
    (13, 5),
]


@pytest.mark.parametrize(("k", "expected"), GAMMA04_ODD_CASES)
def test_dim_cusp_gamma04_odd(k: int, expected: int) -> None:
    assert dim_cusp_forms_gamma0_4(k, even_weight=False) == expected


def test_gamma04_even_weight_rejects_odd_k() -> None:
    with pytest.raises(ValueError):
        dim_cusp_forms_gamma0_4(5, even_weight=True)


def test_gamma04_odd_weight_rejects_even_k() -> None:
    with pytest.raises(ValueError):
        dim_cusp_forms_gamma0_4(6, even_weight=False)


# ============================================================================
# 3. Unified dim_cusp_type_I formula
# ============================================================================

DIM_CUSP_TYPE_I_EVEN_RANK_CASES = [
    # (rank, expected) for even rank
    # These unify the Gamma_0(4) results: floor((r/2 - 3)/2) = floor((r-6)/4)
    # VERIFIED: [DC] floor((r-6)/4); [CF] matches dim_cusp_forms_gamma0_4 at each parity
    (2, 0),    # k=1, too small
    (4, 0),    # k=2, too small
    (6, 0),    # k=3, floor(0/2)=0
    (8, 0),    # k=4, floor(1/2)=0. VERIFIED: [CF] matches E8 type II depth
    (10, 1),   # k=5, floor(2/2)=1. First nontrivial case.
    (12, 1),   # k=6, floor(3/2)=1
    (14, 2),   # k=7, floor(4/2)=2
    (16, 2),   # k=8, floor(5/2)=2
    (18, 3),   # k=9, floor(6/2)=3
    (20, 3),   # k=10, floor(7/2)=3
    (24, 4),   # k=12, floor(9/2)=4
    (32, 6),   # k=16, floor(13/2)=6
    (48, 10),  # k=24, floor(21/2)=10
]


@pytest.mark.parametrize(("rank", "expected"), DIM_CUSP_TYPE_I_EVEN_RANK_CASES)
def test_dim_cusp_type_I_even_rank(rank: int, expected: int) -> None:
    assert dim_cusp_type_I(rank) == expected


DIM_CUSP_TYPE_I_ODD_RANK_CASES = [
    # (rank, expected) for odd rank, via Shimura: dim S_{r-1}(SL(2,Z))
    # VERIFIED: [DC] Shimura-Kohnen; [CF] matches dim_cusp_forms_sl2z(r-1)
    (1, 0),    # r-1=0, no cusp forms
    (3, 0),    # r-1=2, dim S_2(SL2Z)=0
    (5, 0),    # r-1=4, dim S_4(SL2Z)=0
    (7, 0),    # r-1=6, dim S_6(SL2Z)=0
    (9, 0),    # r-1=8, dim S_8(SL2Z)=0
    (11, 0),   # r-1=10, dim S_10(SL2Z)=0
    (13, 1),   # r-1=12, dim S_12(SL2Z)=1. VERIFIED: [DC] Ramanujan Delta; [LT] LMFDB
    (15, 0),   # r-1=14, dim S_14(SL2Z)=0 (14 mod 12=2, floor(14/12)-1=0)
    (17, 1),   # r-1=16, dim S_16(SL2Z)=1
    (25, 2),   # r-1=24, dim S_24(SL2Z)=2
    (37, 3),   # r-1=36, dim S_36(SL2Z)=3
    (49, 4),   # r-1=48, dim S_48(SL2Z)=4
]


@pytest.mark.parametrize(("rank", "expected"), DIM_CUSP_TYPE_I_ODD_RANK_CASES)
def test_dim_cusp_type_I_odd_rank(rank: int, expected: int) -> None:
    assert dim_cusp_type_I(rank) == expected


def test_dim_cusp_type_I_rejects_nonpositive() -> None:
    with pytest.raises(ValueError):
        dim_cusp_type_I(0)
    with pytest.raises(ValueError):
        dim_cusp_type_I(-1)


# ============================================================================
# 4. Shadow depth at key lattices
# ============================================================================

SHADOW_DEPTH_TYPE_I_CASES = [
    # (rank, expected_depth)
    # VERIFIED: [DC] d = 3 + dim_cusp_type_I(r);
    # [CF] cross-checked against both Gamma_0(4) and Shimura computations
    (1, 3),    # Z^1: no cusp forms at weight 1/2
    (2, 3),    # Z^2: k=1, no cusp forms
    (3, 3),    # Z^3: dim S_2(SL2Z) = 0 via Shimura
    (4, 3),    # Z^4: k=2, no cusp forms
    (5, 3),    # Z^5: dim S_4(SL2Z) = 0 via Shimura
    (8, 3),    # Z^8: k=4, dim S_4(Gamma_0(4)) = 0. Same as E8!
    (10, 4),   # Z^10: k=5, dim S_5(Gamma_0(4), chi) = 1. FIRST NONTRIVIAL.
    (13, 4),   # Z^13: dim S_12(SL2Z) = 1 via Shimura. First odd rank > 3.
    (16, 5),   # Z^16: k=8, dim S_8(Gamma_0(4)) = 2. Compare E8+E8 (type II, d=3).
    (24, 7),   # Z^24: k=12, dim S_12(Gamma_0(4)) = 4. Compare Leech (type II, d=4).
    (48, 13),  # Z^48: k=24, dim S_24(Gamma_0(4)) = 10
]


@pytest.mark.parametrize(("rank", "expected"), SHADOW_DEPTH_TYPE_I_CASES)
def test_shadow_depth_type_I(rank: int, expected: int) -> None:
    assert shadow_depth_type_I(rank) == expected


def test_shadow_depth_type_I_rejects_nonpositive() -> None:
    with pytest.raises(ValueError):
        shadow_depth_type_I(0)


# ============================================================================
# 5. Type II shadow depth (wrapper cross-check)
# ============================================================================

TYPE_II_CASES = [
    # VERIFIED: [DC] 3 + dim S_{r/2}(SL2Z); [CF] matches lattice_shadow_higher_depth_engine
    (8, 3),    # dim S_4(SL2Z) = 0
    (16, 3),   # dim S_8(SL2Z) = 0
    (24, 4),   # dim S_12(SL2Z) = 1
    (32, 4),   # dim S_16(SL2Z) = 1
    (48, 5),   # dim S_24(SL2Z) = 2
    (72, 6),   # dim S_36(SL2Z) = 3
    (96, 7),   # dim S_48(SL2Z) = 4
]


@pytest.mark.parametrize(("rank", "expected"), TYPE_II_CASES)
def test_shadow_depth_type_II(rank: int, expected: int) -> None:
    assert shadow_depth_type_II(rank) == expected


@pytest.mark.parametrize("rank", [4, 10, 12, 14, 18, 44])
def test_shadow_depth_type_II_rejects_non_mult_8(rank: int) -> None:
    with pytest.raises(ValueError):
        shadow_depth_type_II(rank)


# ============================================================================
# 6. Depth correction delta = d_I - d_II
# ============================================================================

CORRECTION_CASES = [
    # (rank, expected_delta)
    # VERIFIED: [DC] d_I - d_II; [CF] dim_cusp(Gamma_0(4)) - dim_cusp(SL2Z)
    (8, 0),    # Both spaces vanish at weight 4
    (16, 2),   # dim S_8(G04)=2 - dim S_8(SL2Z)=0 = 2
    (24, 3),   # dim S_12(G04)=4 - dim S_12(SL2Z)=1 = 3
    (32, 5),   # dim S_16(G04)=6 - dim S_16(SL2Z)=1 = 5
    (48, 8),   # dim S_24(G04)=10 - dim S_24(SL2Z)=2 = 8
]


@pytest.mark.parametrize(("rank", "expected"), CORRECTION_CASES)
def test_depth_correction(rank: int, expected: int) -> None:
    assert depth_correction(rank) == expected


def test_depth_correction_nonnegative() -> None:
    """Type I depth is always >= type II depth."""
    for r in range(8, 200, 8):
        assert depth_correction(r) >= 0


def test_depth_correction_rejects_non_mult_8() -> None:
    with pytest.raises(ValueError):
        depth_correction(10)


# ============================================================================
# 7. Structural properties
# ============================================================================

def test_type_I_depth_at_least_3() -> None:
    """Shadow depth for any type I lattice is at least 3 (kappa + KS + Eisenstein)."""
    for r in range(1, 100):
        assert shadow_depth_type_I(r) >= 3


def test_type_I_depth_nondecreasing_even_rank() -> None:
    """For even ranks, the depth is non-decreasing."""
    depths = [shadow_depth_type_I(r) for r in range(2, 100, 2)]
    assert depths == sorted(depths)


def test_type_I_depth_nondecreasing_odd_rank() -> None:
    """For odd ranks, the depth is non-decreasing."""
    depths = [shadow_depth_type_I(r) for r in range(1, 100, 2)]
    assert depths == sorted(depths)


def test_type_I_ge_type_II_at_mult_8() -> None:
    """At ranks divisible by 8, type I depth >= type II depth."""
    for r in range(8, 200, 8):
        assert shadow_depth_type_I(r) >= shadow_depth_type_II(r)


def test_rank_8_types_agree() -> None:
    """At rank 8, type I and type II have the same depth (both cusp spaces vanish)."""
    # VERIFIED: [DC] dim S_4(Gamma_0(4)) = dim S_4(SL2Z) = 0;
    # [CF] Z^8 and E8 have the same shadow depth
    assert shadow_depth_type_I(8) == shadow_depth_type_II(8) == 3


def test_first_nontrivial_even_rank() -> None:
    """Rank 10 is the first even rank where type I depth exceeds 3."""
    # VERIFIED: [DC] dim S_5(Gamma_0(4), chi_{-4}) = 1; [NE] direct weight check
    assert shadow_depth_type_I(8) == 3
    assert shadow_depth_type_I(10) == 4


def test_first_nontrivial_odd_rank() -> None:
    """Rank 13 is the first odd rank where type I depth exceeds 3."""
    # VERIFIED: [DC] dim S_12(SL2Z) = 1 (Ramanujan Delta); [LT] Shimura 1973
    for r in range(1, 13, 2):
        assert shadow_depth_type_I(r) == 3
    assert shadow_depth_type_I(13) == 4


# ============================================================================
# 8. Census consistency
# ============================================================================

def test_census_covers_all_ranks() -> None:
    census = shadow_depth_census(48)
    assert set(census.keys()) == set(range(1, 49))


def test_census_depth_matches_direct() -> None:
    census = shadow_depth_census(48)
    for r, entry in census.items():
        assert entry['depth_type_I'] == shadow_depth_type_I(r)


def test_census_type_II_at_mult_8() -> None:
    census = shadow_depth_census(48)
    for r in range(8, 49, 8):
        assert census[r]['depth_type_II'] == shadow_depth_type_II(r)
        assert census[r]['delta'] == depth_correction(r)


def test_census_type_II_none_elsewhere() -> None:
    census = shadow_depth_census(48)
    for r in range(1, 49):
        if r % 8 != 0:
            assert census[r]['depth_type_II'] is None
            assert census[r]['delta'] is None


def test_census_kappa_correct() -> None:
    """kappa = r/2 for all unimodular lattice VOAs (AP1, C1)."""
    from fractions import Fraction
    census = shadow_depth_census(24)
    for r, entry in census.items():
        # VERIFIED: [DC] kappa(lattice) = rank/2; [LC] r=0 -> kappa=0
        assert entry['kappa'] == Fraction(r, 2)


# ============================================================================
# 9. Consistency with even-rank unified formula
# ============================================================================

def test_even_rank_formula_matches_gamma04_direct() -> None:
    """The unified floor((k-3)/2) matches the parity-specific Gamma_0(4) formulas."""
    for r in range(2, 100, 2):
        k = r // 2
        unified = dim_cusp_type_I(r)
        if k % 2 == 0 and k >= 2:
            direct = dim_cusp_forms_gamma0_4(k, even_weight=True)
        else:
            direct = dim_cusp_forms_gamma0_4(k, even_weight=False)
        assert unified == direct, f"Mismatch at rank {r}: unified={unified}, direct={direct}"


def test_odd_rank_formula_matches_sl2z() -> None:
    """The Shimura map gives dim S_{r-1}(SL2Z) for odd rank."""
    for r in range(1, 100, 2):
        assert dim_cusp_type_I(r) == dim_cusp_forms_sl2z(r - 1)
