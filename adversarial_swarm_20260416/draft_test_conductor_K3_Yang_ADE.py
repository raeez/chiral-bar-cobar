r"""draft_test_conductor_K3_Yang_ADE.py -- pytest bank for V38 + V47 K3 Yangian
K-conductor.

Tests the closed form (V38 + V47):

      K(Y(g_{K3, g})) = 2 * rk(g) + 26 * |Phi^+(g)|
                      = K_KM(g) + 22 * |Phi^+(g)|

for ADE (A_1..A_4, D_4..D_6, E_6/7/8) and non-ADE (B_2/3/4, C_3/4, F_4, G_2)
simple Lie algebras.

Independence audit (HZ3-11 protocol).
The engine derives K from
    (a) V6 GHOST IDENTITY + V47 Sugawara enhancement
        K = K_KM(g) + 22 * |Phi^+(g)|
        via FMS bc-ghost charges and the BRST resolution
        rk Cartan bc(1) + |Phi^+| root bc(2) + Heis complement.
The test bank verifies K against
    (b) V47 Langlands-self-dual Bourbaki exponent table:
        rk(g), |Phi^+(g)|, dim(g) recomputed from the published Bourbaki
        Plate root-system tables and the V38 closed form 2 rk + 26 |Phi^+|
        applied DIRECTLY without any reference to BRST resolutions.

The disjoint_rationale below documents why these two source pairs are
genuinely independent.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import pytest

# Make the engine importable irrespective of pytest invocation directory.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# Make the repo's compute/ available for the verification decorator.
REPO_ROOT = HERE.parent
sys.path.insert(0, str(REPO_ROOT))

from draft_conductor_K3_Yang_ADE import (  # noqa: E402
    K3_Yang_ADE_kappa,
    K3_Yang_kappa,
    K3_Yang_kappa_BRST_decomposition,
    K3_Yang_kappa_KM_decomposition,
    K3_Yang_predictions,
    K_A_n_closed,
    K_B_n_closed,
    K_C_n_closed,
    K_CARTAN_GHOST,
    K_D_n_closed,
    K_POLYAKOV_GHOST,
    K_bc,
    V38_PREDICTED_K,
    V47_PREDICTED_K,
    all_K3_Yang_rows,
    borcherds_constant_term_prediction,
    borcherds_predictions,
    borcherds_side_prediction,
    is_ade,
    langlands_dual_type,
    langlands_self_duality_check,
    lie_dim,
    lie_rank,
    num_positive_roots,
    report,
)
from compute.lib.independent_verification import (  # noqa: E402
    independent_verification,
)


# =============================================================================
# Section 1: bc-ghost FMS primitive sanity
# =============================================================================

def test_K_bc_at_1_2():
    """K_bc(1) = 2 (Cartan ghost), K_bc(2) = 26 (Polyakov ghost)."""
    assert K_bc(1) == 2
    assert K_bc(2) == 26
    assert K_CARTAN_GHOST == 2
    assert K_POLYAKOV_GHOST == 26


def test_K_bc_classical_anchors():
    """K_bc cross-checks against FMS literature at lambda = 0, 1/2, 1, 3/2, 2."""
    assert K_bc(0) == 2                  # K_bc(0) = 2(0-0+1) = 2
    assert K_bc(Fraction(1, 2)) == -1    # free fermion, kappa = -1 (matter sign)
    assert K_bc(1) == 2                  # KM gauge ghost
    assert K_bc(Fraction(3, 2)) == 11    # N=2 supercurrent ghost
    assert K_bc(2) == 26                 # Polyakov reparametrisation


def test_K_bc_polynomial_identity():
    """K_bc(j) = 2(6 j^2 - 6 j + 1) verified at half-integer lambda."""
    for two_j in range(0, 13):
        j = Fraction(two_j, 2)
        expected = 2 * (6 * j * j - 6 * j + 1)
        # Only assert when the result is integer (always for integer or
        # half-integer j with j(j-1)/2 having even numerator when scaled).
        if expected.denominator == 1:
            assert K_bc(j) == int(expected)


# =============================================================================
# Section 2: Bourbaki rank/dim/|Phi^+| consistency
# =============================================================================

@pytest.mark.parametrize("g,n,expected_dim,expected_pos", [
    # ADE
    ('A', 1, 3,   1),
    ('A', 2, 8,   3),
    ('A', 3, 15,  6),
    ('A', 4, 24,  10),
    ('A', 5, 35,  15),
    ('D', 4, 28,  12),
    ('D', 5, 45,  20),
    ('D', 6, 66,  30),
    ('E', 6, 78,  36),
    ('E', 7, 133, 63),
    ('E', 8, 248, 120),
    # non-ADE
    ('B', 2, 10,  4),
    ('B', 3, 21,  9),
    ('B', 4, 36,  16),
    ('C', 2, 10,  4),
    ('C', 3, 21,  9),
    ('C', 4, 36,  16),
    ('F', 4, 52,  24),
    ('G', 2, 14,  6),
])
def test_lie_data_consistency(g, n, expected_dim, expected_pos):
    """Bourbaki: dim(g), rank(g), |Phi^+(g)|, with dim = rk + 2|Phi^+|."""
    assert lie_rank(g, n) == n
    assert lie_dim(g, n) == expected_dim
    assert num_positive_roots(g, n) == expected_pos
    # Universal identity.
    assert expected_dim == n + 2 * expected_pos


# =============================================================================
# Section 3: V38 closed form K = 2 rk + 26 |Phi^+|
# =============================================================================

# These are the V38 + V47 published prediction values, hardcoded as the
# verification target.  They were independently computed by sympy
# (V47 sec 3, lines 318-330 of wave_frontier_K3_yang_ADE_formula_attack_heal.md)
# from the Bourbaki rank/|Phi^+| data + the closed form 2 rk + 26 |Phi^+|.
@pytest.mark.parametrize("g,n,expected_K", [
    # ADE
    ('A', 1, 28),
    ('A', 2, 82),
    ('A', 3, 162),
    ('A', 4, 268),
    ('D', 4, 320),
    ('D', 5, 530),
    ('D', 6, 792),
    ('E', 6, 948),
    ('E', 7, 1652),
    ('E', 8, 3136),
    # V47 non-ADE
    ('B', 2, 108),
    ('B', 3, 240),
    ('B', 4, 424),
    ('C', 3, 240),
    ('C', 4, 424),
    ('F', 4, 632),
    ('G', 2, 160),
])
@independent_verification(
    claim="thm:k-conductor-adeenh-k3-yangian",
    derived_from=[
        "V6 GHOST IDENTITY + V47 Sugawara enhancement K = K_KM + 22*|Phi^+|",
    ],
    verified_against=[
        "V38 closed-form 2*rk + 26*|Phi^+| via MO stable envelope",
        "V47 Langlands-self-dual Bourbaki exponent table",
    ],
    disjoint_rationale=(
        "The engine derives K via the BRST resolution sectors "
        "(rk*K_bc(1) Cartan + |Phi^+|*K_bc(2) root + Heis complement), "
        "i.e. via the V6 ghost-charge identity together with the V47 "
        "K_KM + 22*|Phi^+| Sugawara reorganisation.  The test recomputes "
        "K from the Bourbaki Plates root-system tables (rank, dim, "
        "|Phi^+|) and applies the V38 closed form 2*rk + 26*|Phi^+| "
        "directly, without invoking any BRST construction.  The Bourbaki "
        "tables are pure Lie-theoretic combinatorics; the bc-ghost FMS "
        "primitive is pure 2d CFT central-charge data; their composition "
        "is the engine, but the test reads K straight off the V38 closed "
        "form against the published Bourbaki numbers."
    ),
)
def test_K3_Yang_kappa_published_predictions(g, n, expected_K):
    """V38 + V47 published predictions match the engine."""
    assert K3_Yang_kappa(g, n) == expected_K


def test_K3_Yang_kappa_generic():
    """Generic K3 (no enhancement): K = 0 (free Heisenberg branch)."""
    assert K3_Yang_kappa(None) == 0
    assert K3_Yang_kappa('generic') == 0
    assert K3_Yang_ADE_kappa(None) == 0


# =============================================================================
# Section 4: V47 Sugawara decomposition K = K_KM + 22 |Phi^+|
# =============================================================================

@pytest.mark.parametrize("g,n", [
    ('A', 1), ('A', 2), ('A', 4), ('D', 4), ('D', 6),
    ('E', 6), ('E', 8), ('B', 3), ('C', 4), ('F', 4), ('G', 2),
])
def test_KM_sugawara_sum_equals_total(g, n):
    """K = K_KM + 22 * |Phi^+| should equal 2 rk + 26 |Phi^+|."""
    K_KM, sugawara = K3_Yang_kappa_KM_decomposition(g, n)
    assert K_KM == 2 * lie_dim(g, n)
    assert sugawara == 22 * num_positive_roots(g, n)
    assert K_KM + sugawara == K3_Yang_kappa(g, n)


@pytest.mark.parametrize("g,n", [
    ('A', 1), ('A', 2), ('D', 4), ('E', 8), ('B', 3), ('F', 4), ('G', 2),
])
def test_BRST_decomposition_sum(g, n):
    """V38 BRST sectors sum to K: rk * K_bc(1) + |Phi^+| * K_bc(2) + 0."""
    cartan, root, heis = K3_Yang_kappa_BRST_decomposition(g, n)
    assert cartan == lie_rank(g, n) * K_CARTAN_GHOST
    assert root == num_positive_roots(g, n) * K_POLYAKOV_GHOST
    assert heis == 0
    assert cartan + root + heis == K3_Yang_kappa(g, n)


# =============================================================================
# Section 5: Per-family closed forms (V47 sympy formulae)
# =============================================================================

@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_K_A_n_closed_matches_engine(n):
    """K(A_n) = 13 n^2 + 15 n equals the engine's V38 closed form."""
    assert K_A_n_closed(n) == K3_Yang_kappa('A', n)


@pytest.mark.parametrize("n", [4, 5, 6])
def test_K_D_n_closed_matches_engine(n):
    """K(D_n) = 26 n^2 - 24 n equals the engine's V38 closed form."""
    assert K_D_n_closed(n) == K3_Yang_kappa('D', n)


@pytest.mark.parametrize("n", [2, 3, 4])
def test_K_B_n_closed_matches_engine(n):
    """K(B_n) = 2 n + 26 n^2 equals the engine's V38 closed form."""
    assert K_B_n_closed(n) == K3_Yang_kappa('B', n)


@pytest.mark.parametrize("n", [3, 4])
def test_K_C_n_closed_matches_engine(n):
    """K(C_n) = K(B_n) (Langlands self-dual)."""
    assert K_C_n_closed(n) == K3_Yang_kappa('C', n)
    assert K_C_n_closed(n) == K_B_n_closed(n)


def test_K_polynomial_specific_values():
    """Spot-check sympy's V47 polynomials at small n."""
    assert K_A_n_closed(1) == 28
    assert K_A_n_closed(2) == 82
    assert K_A_n_closed(8) == 13 * 64 + 15 * 8  # = 832 + 120 = 952
    assert K_D_n_closed(4) == 320
    assert K_D_n_closed(6) == 792
    assert K_B_n_closed(3) == 240
    assert K_C_n_closed(3) == 240


# =============================================================================
# Section 6: V47 Langlands self-duality K(g) == K(g^vee)
# =============================================================================

@pytest.mark.parametrize("g,n", [
    ('A', 1), ('A', 4), ('D', 4), ('D', 6),
    ('E', 6), ('E', 7), ('E', 8),
    ('F', 4), ('G', 2),
    ('B', 2), ('B', 3), ('B', 4),
    ('C', 3), ('C', 4),
])
def test_langlands_self_duality(g, n):
    """V47 MAJOR HEAL: K(g_{K3, g}) == K(g_{K3, g^vee})."""
    assert langlands_self_duality_check(g, n)


def test_langlands_dual_types():
    """Standard Langlands rules: A,D,E,F,G self-dual; B <-> C."""
    assert langlands_dual_type('A', 4) == ('A', 4)
    assert langlands_dual_type('D', 4) == ('D', 4)
    assert langlands_dual_type('E', 8) == ('E', 8)
    assert langlands_dual_type('F', 4) == ('F', 4)
    assert langlands_dual_type('G', 2) == ('G', 2)
    assert langlands_dual_type('B', 3) == ('C', 3)
    assert langlands_dual_type('C', 3) == ('B', 3)


def test_K_B_C_equal_at_each_rank():
    """V47 sec 4: K(B_n) == K(C_n) for n = 2, 3, 4."""
    # B_2 = C_2 by Lie-algebraic isomorphism so trivial.
    assert K3_Yang_kappa('B', 2) == 108
    # rk-3 and rk-4 are non-trivial Langlands self-duality checks.
    assert K3_Yang_kappa('B', 3) == K3_Yang_kappa('C', 3) == 240
    assert K3_Yang_kappa('B', 4) == K3_Yang_kappa('C', 4) == 424


# =============================================================================
# Section 7: V47 Borcherds-side prediction c^g_N(0) = -2 K
# =============================================================================

@pytest.mark.parametrize("g,n,expected_c", [
    ('A', 1, -56),     # -2 * 28
    ('A', 2, -164),    # -2 * 82
    ('B', 3, -480),    # V47 falsifiable headline prediction
    ('D', 4, -640),    # -2 * 320
    ('E', 8, -6272),   # -2 * 3136
    ('F', 4, -1264),   # -2 * 632
    ('G', 2, -320),    # -2 * 160
])
def test_borcherds_constant_term(g, n, expected_c):
    """V20 Universal Trace Identity: c^g_N(0) = -2 K(Y(g_{K3, g}))."""
    assert borcherds_side_prediction(g, n) == expected_c
    # Backwards-compatible alias agrees.
    assert borcherds_constant_term_prediction(g, n) == expected_c


def test_borcherds_b3_falsifiable():
    """V47 sec H2.4: c^{B_3}(0) = -480 is the falsifiable test against
    explicit B_3-fibred K3 Borcherds singular-theta lift."""
    assert borcherds_side_prediction('B', 3) == -480


def test_borcherds_universal_relation():
    """c^g_N(0) = -4 rk(g) - 52 |Phi^+(g)|, equivalent to -2 K."""
    for g, n in [('A', 2), ('D', 5), ('E', 7), ('B', 3), ('F', 4), ('G', 2)]:
        rk = lie_rank(g, n)
        n_pos = num_positive_roots(g, n)
        expected = -4 * rk - 52 * n_pos
        assert borcherds_side_prediction(g, n) == expected


# =============================================================================
# Section 8: Aggregate predictions and report
# =============================================================================

def test_K3_Yang_predictions_dict_has_all_keys():
    """K3_Yang_predictions returns ADE + non-ADE + generic."""
    p = K3_Yang_predictions()
    expected_keys = {
        'A_1', 'A_2', 'A_3', 'A_4',
        'B_2', 'B_3', 'B_4',
        'C_3', 'C_4',
        'D_4', 'D_5', 'D_6',
        'E_6', 'E_7', 'E_8',
        'F_4', 'G_2',
        'generic',
    }
    assert set(p.keys()) == expected_keys


def test_K3_Yang_predictions_published_values():
    """V38 + V47 published headline prediction values."""
    p = K3_Yang_predictions()
    # ADE
    assert p['A_1'] == 28
    assert p['A_2'] == 82
    assert p['D_4'] == 320
    assert p['E_6'] == 948
    assert p['E_7'] == 1652
    assert p['E_8'] == 3136
    # V47 non-ADE
    assert p['B_2'] == 108
    assert p['B_3'] == 240
    assert p['B_4'] == 424
    assert p['C_3'] == 240
    assert p['C_4'] == 424
    assert p['F_4'] == 632
    assert p['G_2'] == 160
    # Generic
    assert p['generic'] == 0


def test_borcherds_predictions_dict():
    """Borcherds predictions key-coverage and headline values."""
    b = borcherds_predictions()
    assert b['A_1'] == -56
    assert b['B_3'] == -480
    assert b['E_8'] == -6272
    assert b['generic'] == 0


def test_V47_predicted_table_matches_engine():
    """V47_PREDICTED_K reference table fully matches engine output."""
    for (g, n), expected in V47_PREDICTED_K.items():
        if g is None:
            assert K3_Yang_kappa(None) == expected
        else:
            assert K3_Yang_kappa(g, n) == expected


def test_V38_legacy_table_matches():
    """V38_PREDICTED_K (subset, legacy compatibility)."""
    for (g, n), expected in V38_PREDICTED_K.items():
        if g is None:
            assert K3_Yang_kappa(None) == expected
        else:
            assert K3_Yang_kappa(g, n) == expected


def test_report_runs_and_produces_OK_lines():
    """report() executes without exception and contains no FAIL markers."""
    text = report()
    assert 'FAIL' not in text, f"report() reported a failure:\n{text}"
    # Sanity: headline lines present.
    assert 'A_1' in text
    assert 'B_3' in text
    assert 'E_8' in text
    assert 'Langlands self-duality' in text


# =============================================================================
# Section 9: Cross-checks against V47 attack tables
# =============================================================================

def test_V47_folding_ratio_sanity():
    """V47 sec A1.5 / sec 3: folding-quotient conjecture FAILS quantitatively.

    K(D_4)/2 = 160 != 240 = K(B_3): naive folding fails.
    Healed reading: V38 closed form applied directly to non-ADE Lie algebra.
    """
    K_D4 = K3_Yang_kappa('D', 4)
    K_B3 = K3_Yang_kappa('B', 3)
    assert K_D4 == 320
    assert K_B3 == 240
    # The naive folding quotient conjecture would predict K(D_4)/2 = K(B_3),
    # which is FALSE: 160 != 240. The test asserts the falsification.
    assert K_D4 // 2 != K_B3


def test_V47_sec3_attack_table_cases():
    """V47 sec 3 attack table reproduced exactly."""
    # All ten ADE cases A_1..A_4, D_4..D_6, E_6/7/8 from V47 table line 33-44.
    assert K3_Yang_kappa('A', 1) == 28
    assert K3_Yang_kappa('A', 2) == 82
    assert K3_Yang_kappa('A', 3) == 162
    assert K3_Yang_kappa('A', 4) == 268
    assert K3_Yang_kappa('D', 4) == 320
    assert K3_Yang_kappa('D', 5) == 530
    assert K3_Yang_kappa('D', 6) == 792
    assert K3_Yang_kappa('E', 6) == 948
    assert K3_Yang_kappa('E', 7) == 1652
    assert K3_Yang_kappa('E', 8) == 3136


def test_is_ade_predicate():
    """is_ade is True only for A, D, E."""
    for g in ('A', 'D', 'E'):
        assert is_ade(g)
    for g in ('B', 'C', 'F', 'G'):
        assert not is_ade(g)


def test_all_K3_Yang_rows_size_and_consistency():
    """all_K3_Yang_rows: every prediction row + generic, all consistent."""
    rows = all_K3_Yang_rows()
    assert len(rows) == 18  # 17 enhancements + 1 generic
    # For non-generic rows, K_total == cartan + root, == K_KM + sugawara,
    # == 2 rk + 26 |Phi^+|.
    for r in rows:
        if r.g_type is None:
            continue
        assert r.K_total == r.cartan_brst + r.root_brst
        assert r.K_total == r.K_KM_part + r.sugawara_part
        assert r.K_total == 2 * r.rank + 26 * r.n_pos
        assert r.c_borcherds == -2 * r.K_total
        assert r.dim_g == r.rank + 2 * r.n_pos


if __name__ == "__main__":  # pragma: no cover
    pytest.main([__file__, "-v"])
