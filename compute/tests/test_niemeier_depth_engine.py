"""Tests for niemeier_depth_engine.py.

The tested claim surface is the BB3 rank-24 arithmetic depth formula

    d(V_Lambda) = 3 + dim S_{r/2}(SL_2(Z))

for the 24 Niemeier lattice VOAs. At rank 24 this becomes

    d(V_Lambda) = 3 + dim S_12 = 4.

The suite keeps the three verification paths separate:
    1. Standard cusp-dimension formula.
    2. Ring count from M_* = C[E_4, E_6] and S_k = Delta * M_{k-12}.
    3. Explicit Delta = eta^24 together with the level-1 Sturm bound.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.niemeier_depth_engine import (
    E12_Q1_COEFFICIENT,
    NIEMEIER_LATTICES,
    all_niemeier_depth_records,
    depth_from_even_unimodular_rank,
    dim_cusp_forms_formula,
    dim_cusp_forms_via_ring,
    niemeier_cusp_coefficient,
    niemeier_depth_record,
    ramanujan_delta_qexp,
    sturm_bound_level_one,
    verify_weight_12_cusp_dimension,
)


EXPECTED_NIEMEIER_LABELS = (
    "D24",
    "D16+E8",
    "E8^3",
    "A24",
    "D12^2",
    "A17+E7",
    "D10+E7^2",
    "A15+D9",
    "D8^3",
    "A12^2",
    "A11+D7+E6",
    "E6^4",
    "A9^2+D6",
    "D6^4",
    "A8^3",
    "A7^2+D5^2",
    "A6^4",
    "A5^4+D4",
    "D4^6",
    "A4^6",
    "A3^8",
    "A2^12",
    "A1^24",
    "Leech",
)
# VERIFIED: [LT] Niemeier's classification gives exactly 24 even unimodular
# rank-24 lattices, determined by these root systems or the rootless Leech;
# [DC] the engine registry enumerates 24 entries and the non-Leech root systems
# each have total root rank 24 while Leech has 0.

EXPECTED_CUSP_DIMS = {
    2: 0,
    4: 0,
    6: 0,
    8: 0,
    10: 0,
    12: 1,
    14: 0,
    16: 1,
    18: 1,
    20: 1,
    22: 1,
    24: 2,
    26: 1,
    36: 3,
}
# VERIFIED: [DC] dim S_k(SL_2(Z)) = floor(k/12) - 1 on the k == 2 mod 12 branch
# and floor(k/12) otherwise for even k >= 12; [CF] S_k = Delta * M_{k-12} with
# M_* = C[E_4, E_6], so the same values are the monomial counts in weight k-12.

EXPECTED_DELTA_PREFIX = (1, -24, 252, -1472, 4830, -6048)
# VERIFIED: [DC] Delta = eta^24 = q * prod_{n>=1} (1 - q^n)^24 gives these first
# coefficients by direct Euler-product expansion; [LT] these are the classical
# Ramanujan tau values tau(1) through tau(6).

EXPECTED_DEPTH_AT_RANK_24 = 4
# VERIFIED: [DC] d(V_Lambda) = 3 + dim S_12 = 3 + 1; [CF] S_12 = Delta * M_0 is
# one-dimensional, so every rank-24 even unimodular lattice has BB3 depth 4.

EXPECTED_LEECH_CUSP_COEFFICIENT = Fraction(-65520, 691)
# VERIFIED: [DC] Theta_Leech = E_12 + c_Delta * Delta and the q^1 coefficient is
# 0 because Leech has no roots; [CF] E_12 has q^1 coefficient 65520/691 and
# Delta has q^1 coefficient 1, so c_Delta = -65520/691.

SAMPLE_ROOTED_CUSP_COEFFICIENTS = {
    "A1^24": Fraction(-32352, 691),
    "E8^3": Fraction(432000, 691),
    "D24": Fraction(697344, 691),
}
# VERIFIED: [DC] c_Delta = (691 * |R| - 65520) / 691 from the q^1 coefficient;
# [CF] |R(A1^24)| = 48, |R(E8^3)| = 720, |R(D24)| = 1104 from ADE root counts.


def test_registry_lists_all_24_niemeier_lattices() -> None:
    assert tuple(lattice.label for lattice in NIEMEIER_LATTICES) == EXPECTED_NIEMEIER_LABELS
    assert len(NIEMEIER_LATTICES) == 24


@pytest.mark.parametrize("label", EXPECTED_NIEMEIER_LABELS)
def test_each_niemeier_lattice_has_depth_four(label: str) -> None:
    record = niemeier_depth_record(label)
    assert record.rank == 24
    assert record.half_rank_weight == 12
    assert record.dim_s_half_rank == 1
    assert record.depth == EXPECTED_DEPTH_AT_RANK_24
    assert record.cusp_generator == "Ramanujan Delta = eta^24"


def test_all_24_records_are_depth_four_individually() -> None:
    records = all_niemeier_depth_records()
    assert tuple(records) == EXPECTED_NIEMEIER_LABELS
    assert len(records) == 24
    for label in EXPECTED_NIEMEIER_LABELS:
        assert records[label].depth == EXPECTED_DEPTH_AT_RANK_24


def test_dim_s_12_is_verified_by_three_independent_paths() -> None:
    verification = verify_weight_12_cusp_dimension()
    assert verification.dimension_formula_value == 1
    assert verification.ring_theory_value == 1
    assert verification.sturm_bound == 1
    assert verification.delta_generator == "Ramanujan Delta = eta^24"
    assert verification.delta_qexp_prefix == EXPECTED_DELTA_PREFIX
    assert verification.delta_vanishing_order == 1
    assert verification.unique_by_sturm
    assert verification.is_verified
    assert len(verification.verification_paths) == 3


def test_ramanujan_delta_matches_eta24_prefix() -> None:
    coefficients = ramanujan_delta_qexp(6)
    assert tuple(coefficients[index] for index in range(1, 7)) == EXPECTED_DELTA_PREFIX


@pytest.mark.parametrize(("weight", "expected"), EXPECTED_CUSP_DIMS.items())
def test_cusp_dimension_formula_values(weight: int, expected: int) -> None:
    assert dim_cusp_forms_formula(weight) == expected


@pytest.mark.parametrize(("weight", "expected"), EXPECTED_CUSP_DIMS.items())
def test_cusp_dimension_ring_count_values(weight: int, expected: int) -> None:
    assert dim_cusp_forms_via_ring(weight) == expected


@pytest.mark.parametrize("weight", EXPECTED_CUSP_DIMS)
def test_cusp_dimension_formula_matches_ring_theory(weight: int) -> None:
    assert dim_cusp_forms_formula(weight) == dim_cusp_forms_via_ring(weight)


def test_rank_24_depth_formula_returns_four() -> None:
    assert depth_from_even_unimodular_rank(24) == EXPECTED_DEPTH_AT_RANK_24


def test_rank_24_depth_formula_is_uniform_on_all_niemeier_lattices() -> None:
    for label in EXPECTED_NIEMEIER_LABELS:
        record = niemeier_depth_record(label)
        assert record.depth == depth_from_even_unimodular_rank(record.rank)


def test_sturm_bound_at_weight_12_is_one() -> None:
    assert sturm_bound_level_one(12) == 1


def test_leech_has_no_roots_but_still_has_depth_four() -> None:
    leech = niemeier_depth_record("Leech")
    assert leech.root_count == 0
    assert leech.theta_q1_coefficient == 0
    assert leech.depth == EXPECTED_DEPTH_AT_RANK_24
    assert leech.mechanism_kind == "pure_cusp_only"
    assert leech.cusp_coefficient == EXPECTED_LEECH_CUSP_COEFFICIENT


def test_leech_q1_cancellation_is_purely_cuspidal() -> None:
    leech = niemeier_depth_record("Leech")
    assert E12_Q1_COEFFICIENT + leech.cusp_coefficient == 0


def test_rooted_niemeier_lattices_use_root_system_plus_cusp_mechanism() -> None:
    rooted_labels = [label for label in EXPECTED_NIEMEIER_LABELS if label != "Leech"]
    assert len(rooted_labels) == 23
    for label in rooted_labels:
        record = niemeier_depth_record(label)
        assert record.root_count > 0
        assert record.theta_q1_coefficient > 0
        assert record.depth == EXPECTED_DEPTH_AT_RANK_24
        assert record.mechanism_kind == "root_system_plus_cusp"


@pytest.mark.parametrize(("label", "expected"), SAMPLE_ROOTED_CUSP_COEFFICIENTS.items())
def test_sample_rooted_cusp_coefficients(label: str, expected: Fraction) -> None:
    record = niemeier_depth_record(label)
    assert record.cusp_coefficient == expected
    assert niemeier_cusp_coefficient(record.root_count) == expected
