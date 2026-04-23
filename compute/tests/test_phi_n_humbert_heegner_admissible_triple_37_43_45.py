"""Tests for compute.lib.phi_n_humbert_heegner_admissible_triple_37_43_45.

Verifies pentagon coboundary phi^(n) on the higher Humbert-Heegner
admissible triple {37, 43, 45} through multi-path cross-verification.

SCOPE CASCADE (higher tower):
    n = 37: depth-9 stratum D_{37, 9} = 2023, depth-11 stratum
            D_{37, 11} = 378; d_{37} = 10252.  TRIPLE-CONDITIONAL
            (Zagier-Hoffman + Broadhurst-Kreimer + Brown 2017 Conj 5.3).
    n = 43: first admissible weight with D_{n, 13} > 0 (first depth-13
            onset is at n = 39, not admissible).  D_{43, 13} = 924;
            d_{43} = 55405.  QUADRUPLE-CONDITIONAL
            (triple + Broadhurst-Bailey 2010 numerical stability).
    n = 45: simultaneous depth-13 and depth-15 admissible entries:
            D_{45, 13} = 3076, D_{45, 15} = 69 (depth-15 first onset
            coincides with admissible n = 45).  d_{45} = 97229.
            QUINTUPLE-CONDITIONAL (quadruple + Brown 2017 higher-depth
            generation of grt_1 at the depth-15 onset outside any
            Broadhurst-Bailey 2010 tabulated extractor).

For admissible n >= 45, Brown 2017 arXiv:1709.02856 Conj 5.3 is the
DEEPEST load-bearing hypothesis.

MULTI-PATH CROSS-VERIFICATION:
    P_1 Padovan recurrence d_n = d_{n-2} + d_{n-3} (direct).
    P_2 BK two-step row-sum sum_d D_{n+2, d} = d_n.
    P_3 Generating-function coefficient extraction x / (1 - x^2 - x^3).
    P_4 Plastic-number asymptotic rounded d_n = [A rho^n].
    BK_A Symbolic geometric-series expansion.
    BK_B Recursive-inverse Taylor extraction.
    p24_A 24-fold convolution (1 - q^m)^{-1}.
    p24_B Binomial Euler product sum binom(j + 23, 23) q^{mj}.

HUMBERT-HEEGNER ADMISSIBILITY:
    n mod 8 in {3, 5}; admissible at {37, 43, 45}; non-admissible at
    gap weights {38, 39, 40, 41, 42, 44}.
"""
from __future__ import annotations

import math

import pytest

from compute.lib.phi_n_humbert_heegner_admissible_triple_37_43_45 import (
    ADMISSIBLE_HIGHER_TRIPLE,
    admissibility_filter_check_tower,
    bk_depth_check_tower,
    bk_depth_extract,
    bk_depth_multipath_check_tower,
    bk_depth_via_recursive_inverse,
    bk_padovan_twostep_consistency_check_tower,
    bk_parity_split_check_tower,
    borcherds_mzv_ratio_tower,
    brown_2017_deepest_at_n_geq_45,
    depth_13_15_admissible_onset_check,
    first_depth_thirteen_at_39_check,
    hardy_ramanujan_exact_check_tower,
    humbert_heegner_admissible,
    p24_exact,
    p24_multipath_check_tower,
    p24_via_euler_product,
    padovan_asymptotic,
    padovan_count_check_tower,
    padovan_dim,
    padovan_dim_via_bk_rowsum,
    padovan_dim_via_generating_function,
    padovan_dim_via_plastic_rounded,
    padovan_multipath_check_tower,
    phi_n_leading_check_tower,
    phi_n_leading_values_tower,
    phi_n_mzv_leading,
    plastic_asymptotic_precision_check_tower,
    plastic_number,
    scope_cascade_assertion_tower,
    scope_cascade_check_tower,
    scope_tier_at_tower,
    verifier_tower_37_43_45,
)


# ---------------------------------------------------------------------------
# Admissibility
# ---------------------------------------------------------------------------


def test_admissibility_filter():
    assert admissibility_filter_check_tower()


def test_admissible_higher_triple_composition():
    assert ADMISSIBLE_HIGHER_TRIPLE == (37, 43, 45)
    assert all(humbert_heegner_admissible(n) for n in ADMISSIBLE_HIGHER_TRIPLE)
    # Gap rejection
    for n in (38, 39, 40, 41, 42, 44):
        assert not humbert_heegner_admissible(n), f"n = {n} should be rejected"


def test_admissibility_continuation():
    """Admissible sequence continues past 45 to {51, 53, 59, 61, 67, 69, ...}."""
    for n in (51, 53, 59, 61, 67, 69):
        assert humbert_heegner_admissible(n)


# ---------------------------------------------------------------------------
# Padovan counts at higher admissible triple
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "n, expected",
    [(37, 10252), (43, 55405), (45, 97229)],
)
def test_padovan_dim_at_higher_triple(n, expected):
    d = padovan_dim(60)
    assert d[n] == expected


def test_padovan_count_check_tower():
    assert padovan_count_check_tower()


def test_padovan_recurrence_witness():
    """Check the Padovan recurrence d_n = d_{n-2} + d_{n-3} at each admissible n."""
    d = padovan_dim(60)
    for n in ADMISSIBLE_HIGHER_TRIPLE:
        assert d[n] == d[n - 2] + d[n - 3], (
            f"Padovan recurrence fails at n = {n}: "
            f"{d[n]} != {d[n - 2]} + {d[n - 3]} = {d[n - 2] + d[n - 3]}"
        )


def test_padovan_multipath_check_tower():
    assert padovan_multipath_check_tower()


@pytest.mark.parametrize("n", ADMISSIBLE_HIGHER_TRIPLE)
def test_padovan_four_paths_agree(n):
    """Direct recurrence, BK row-sum, generating function, plastic rounding."""
    d = padovan_dim(60)
    D = bk_depth_extract(60, 16)
    d_P3 = padovan_dim_via_generating_function(60)
    d_P4 = padovan_dim_via_plastic_rounded(60)
    p1 = d[n]
    p2 = padovan_dim_via_bk_rowsum(n, D)
    p3 = d_P3[n]
    p4 = d_P4[n]
    assert p1 == p2 == p3 == p4, (
        f"Four-path disagreement at n = {n}: "
        f"P1={p1}, P2={p2}, P3={p3}, P4={p4}"
    )


# ---------------------------------------------------------------------------
# Broadhurst-Kreimer depth strata
# ---------------------------------------------------------------------------


def test_bk_depth_check_tower():
    assert bk_depth_check_tower()


def test_bk_padovan_twostep_consistency_check_tower():
    assert bk_padovan_twostep_consistency_check_tower()


def test_bk_parity_split_check_tower():
    """Odd admissible weights have vanishing even-depth strata."""
    assert bk_parity_split_check_tower()


def test_bk_depth_multipath_check_tower():
    """Geometric-series and recursive-inverse agree on every (n, d) cell."""
    assert bk_depth_multipath_check_tower()


# Critical-cell independent verification
@pytest.mark.parametrize(
    "n, d, expected",
    [
        # depth-9 at each
        (37, 9, 2023),
        (43, 9, 13245),
        (45, 9, 22453),
        # depth-11 at each
        (37, 11, 378),
        (43, 11, 7097),
        (45, 11, 15486),
        # depth-13 at admissible carriers (n=37 empty)
        (37, 13, 0),
        (43, 13, 924),
        (45, 13, 3076),
        # depth-15 at n=45 only
        (37, 15, 0),
        (43, 15, 0),
        (45, 15, 69),
    ],
)
def test_bk_depth_critical_cells(n, d, expected):
    D = bk_depth_extract(60, 16)
    assert D.get((n, d), 0) == expected, (
        f"D_{{{n}, {d}}} = {D.get((n, d), 0)} != expected {expected}"
    )


# ---------------------------------------------------------------------------
# Depth-onset analysis
# ---------------------------------------------------------------------------


def test_first_depth_thirteen_at_39():
    """Depth-13 first appears at n = 39 (not admissible by HH filter)."""
    assert first_depth_thirteen_at_39_check()


def test_depth_13_admissible_entry_at_43():
    """First admissible weight at depth-13 is n = 43."""
    D = bk_depth_extract(60, 16)
    # n = 37 admissible but depth-13 empty
    assert D.get((37, 13), 0) == 0
    # n = 43 admissible with D = 924
    assert D.get((43, 13), 0) == 924


def test_depth_15_onset_coincides_with_admissible_45():
    """Depth-15 first onset and first admissible carrier both at n = 45."""
    D = bk_depth_extract(60, 16)
    # Empty at n < 45
    for n in range(1, 45):
        assert D.get((n, 15), 0) == 0, f"n={n} depth-15 non-empty"
    # Non-empty at n = 45 with D = 69
    assert D.get((45, 15), 0) == 69
    assert humbert_heegner_admissible(45)


def test_depth_13_15_admissible_onset_check():
    assert depth_13_15_admissible_onset_check()


# ---------------------------------------------------------------------------
# Hardy-Ramanujan p_24 exact values and Borcherds/MZV ratios
# ---------------------------------------------------------------------------


def test_p24_exact_OEIS_A006922():
    """Assert exact p_24(k) at k in {19, 22, 23} matches OEIS A006922."""
    assert p24_exact(19) == 69228721526400
    assert p24_exact(22) == 1971466420726656
    assert p24_exact(23) == 5776331152550400


def test_p24_multipath_check_tower():
    """Direct convolution and binomial Euler product agree."""
    assert p24_multipath_check_tower()


@pytest.mark.parametrize(
    "k",
    [19, 22, 23],
)
def test_p24_two_paths_agree(k):
    pA = p24_exact(k)
    pB = p24_via_euler_product(k)
    assert pA == pB, f"p_24({k}): direct={pA}, Euler={pB}"


def test_hardy_ramanujan_exact_check_tower():
    assert hardy_ramanujan_exact_check_tower()


def test_borcherds_mzv_ratio_tower():
    """Ratios at higher admissible triple."""
    r = borcherds_mzv_ratio_tower()
    expected_approx = {
        37: 6.753e9,
        43: 3.558e10,
        45: 5.941e10,
    }
    for n, v_approx in expected_approx.items():
        assert abs(r[n] - v_approx) / v_approx < 5e-3, (
            f"Borcherds/MZV at n = {n}: got {r[n]:.3e}, approx {v_approx:.3e}"
        )


# ---------------------------------------------------------------------------
# Numerical phi^(n) leading values
# ---------------------------------------------------------------------------


def test_phi_n_leading_check_tower():
    assert phi_n_leading_check_tower()


def test_phi_n_leading_numerical_tower():
    """Numerical phi^(n) agrees with d_n zeta(n) / n! within precision."""
    vals = phi_n_leading_values_tower()
    # Reference values from module's direct computation
    expected = {
        37: 7.449e-40,
        43: 9.171e-49,
        45: 8.128e-52,
    }
    for n, v_exp in expected.items():
        rel = abs(vals[n] - v_exp) / v_exp
        assert rel < 5e-3, (
            f"phi^({n}) = {vals[n]:.3e} vs expected {v_exp:.3e}, rel err {rel}"
        )


@pytest.mark.parametrize("n", ADMISSIBLE_HIGHER_TRIPLE)
def test_phi_n_mzv_leading_positive(n):
    """Each phi^(n) leading value is strictly positive."""
    v = phi_n_mzv_leading(n)
    assert v > 0, f"phi^({n}) = {v} should be positive"


# ---------------------------------------------------------------------------
# Scope cascade: triple -> quadruple -> quintuple conditional
# ---------------------------------------------------------------------------


def test_scope_cascade_assertion_tower():
    assert scope_cascade_assertion_tower()


@pytest.mark.parametrize(
    "n, expected_tier",
    [
        (37, "triple-conditional-depth-11"),
        (43, "quadruple-conditional-depth-13"),
        (45, "quintuple-conditional-depth-15"),
    ],
)
def test_scope_tier_per_admissible(n, expected_tier):
    assert scope_tier_at_tower(n) == expected_tier


def test_brown_2017_deepest_at_n_geq_45():
    assert brown_2017_deepest_at_n_geq_45()


# ---------------------------------------------------------------------------
# Plastic-number asymptotic
# ---------------------------------------------------------------------------


def test_plastic_number_value():
    """Plastic number rho satisfies rho^3 = rho + 1."""
    rho = plastic_number()
    assert abs(rho ** 3 - rho - 1) < 1e-12


def test_plastic_asymptotic_precision_check_tower():
    assert plastic_asymptotic_precision_check_tower()


@pytest.mark.parametrize("n", ADMISSIBLE_HIGHER_TRIPLE)
def test_plastic_asymptotic_rounded_equals_padovan(n):
    """At n >= 8, A rho^n rounded equals d_n exactly."""
    d = padovan_dim(60)
    assert round(padovan_asymptotic(n)) == d[n]


# ---------------------------------------------------------------------------
# Aggregate end-to-end check
# ---------------------------------------------------------------------------


def test_verifier_tower_37_43_45_all_pass():
    """Run every verification check together; all must pass."""
    results = verifier_tower_37_43_45()
    failures = [k for k, v in results.items() if not v]
    assert not failures, f"Failed verifications: {failures}"
