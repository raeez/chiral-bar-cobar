"""Tests for explicit Feynman versus bar matching on V_k(sl_2).

Multi-path verification:
  1. Manual sl_2 structure constants versus the engine tables.
  2. Manual ordered-bar d_3 coefficients versus the engine output.
  3. Manual cubic-vertex coefficients versus the engine Feynman matrix.
  4. AP126/AP141 level-prefix checks for r^KM(z) = k * Omega / z.
  5. Genus-1 numeric checks from the closed formula F_1 = (k+2) / 32.
  6. Boundary-value checks at k = 0 and the critical level k = -2.
"""

from fractions import Fraction

import pytest

from compute.lib.feynman_bar_matching_engine import (
    affine_sl2_kappa,
    affine_sl2_r_matrix,
    bar_differential_arity3,
    bar_differential_matrix_arity3,
    genus1_bar_amplitude,
    genus1_feynman_amplitude,
    genus1_feynman_classical_piece,
    genus1_feynman_quantum_shift,
    genus1_match_report,
    tree_level_dressed_amplitude,
    tree_level_feynman_matrix_arity3,
    verify_genus1_matching,
    verify_tree_level_matching,
)


MANUAL_BASIS = ("e", "h", "f")

MANUAL_BRACKET = {
    ("e", "f"): {"h": Fraction(1)},   # VERIFIED: [LT] [e, f] = h; [DC] antisymmetry with [f, e] = -h.
    ("f", "e"): {"h": Fraction(-1)},  # VERIFIED: [LT] [f, e] = -h; [DC] antisymmetry with [e, f] = h.
    ("h", "e"): {"e": Fraction(2)},   # VERIFIED: [LT] [h, e] = 2e; [DC] root-weight +2 for e.
    ("e", "h"): {"e": Fraction(-2)},  # VERIFIED: [LT] [e, h] = -2e; [DC] antisymmetry with [h, e] = 2e.
    ("h", "f"): {"f": Fraction(-2)},  # VERIFIED: [LT] [h, f] = -2f; [DC] root-weight -2 for f.
    ("f", "h"): {"f": Fraction(2)},   # VERIFIED: [LT] [f, h] = 2f; [DC] antisymmetry with [h, f] = -2f.
}


def _manual_bracket(left: str, right: str):
    return dict(MANUAL_BRACKET.get((left, right), {}))


def _add_sparse(target, word, coeff):
    if coeff == 0:
        return
    target[word] = target.get(word, Fraction(0)) + coeff
    if target[word] == 0:
        del target[word]


def _manual_bar_d3(word):
    left, middle, right = word
    result = {}
    for output, coeff in _manual_bracket(left, middle).items():
        _add_sparse(result, (output, right), coeff)
    for output, coeff in _manual_bracket(middle, right).items():
        _add_sparse(result, (left, output), -coeff)
    return result


def _manual_pair_basis():
    return tuple((left, right) for left in MANUAL_BASIS for right in MANUAL_BASIS)


def _manual_triple_basis():
    return tuple(
        (left, middle, right)
        for left in MANUAL_BASIS
        for middle in MANUAL_BASIS
        for right in MANUAL_BASIS
    )


def _manual_matrix():
    rows = _manual_pair_basis()
    cols = _manual_triple_basis()
    row_index = {word: idx for idx, word in enumerate(rows)}
    entries = [
        [Fraction(0) for _ in cols]
        for _ in rows
    ]
    for col_idx, word in enumerate(cols):
        for target_word, coeff in _manual_bar_d3(word).items():
            entries[row_index[target_word]][col_idx] = coeff
    return rows, cols, tuple(tuple(row) for row in entries)


def _manual_f1(level):
    k = Fraction(level)
    return Fraction(k + 2, 32)


class TestGenusZeroTreeMatching:
    def test_r_matrix_has_level_prefix_and_vanishes_at_zero(self):
        expected_level_four = {
            ("e", "f"): Fraction(4),
            ("f", "e"): Fraction(4),
            ("h", "h"): Fraction(2),
        }
        # VERIFIED: [DC] Omega = e tensor f + f tensor e + (1/2) h tensor h;
        # [LC] r^KM(z) = k * Omega / z gives k = 0 -> 0 and k = 4 -> (4, 4, 2).
        assert affine_sl2_r_matrix(4) == expected_level_four
        assert all(coeff == 0 for coeff in affine_sl2_r_matrix(0).values())

    def test_bar_d3_matches_manual_coefficients_on_h_e_f(self):
        expected = {
            ("e", "f"): Fraction(2),
            ("h", "h"): Fraction(-1),
        }
        # VERIFIED: [DC] [h, e] = 2e and [e, f] = h give d_3([h|e|f]) = 2[e|f] - [h|h];
        # [LT] reduced ordered bar formula d_3(a|b|c) = [a,b]|c - a|[b,c].
        assert bar_differential_arity3(("h", "e", "f")) == expected

    def test_bar_d3_sign_is_exact_on_e_f_h(self):
        expected = {
            ("h", "h"): Fraction(1),
            ("e", "f"): Fraction(-2),
        }
        # VERIFIED: [DC] [e, f] = h and [f, h] = 2f give d_3([e|f|h]) = [h|h] - 2[e|f];
        # [LT] the second channel enters with a minus sign.
        assert bar_differential_arity3(("e", "f", "h")) == expected

    def test_bar_matrix_matches_manual_matrix(self):
        manual_rows, manual_cols, manual_entries = _manual_matrix()
        engine_matrix = bar_differential_matrix_arity3()
        assert engine_matrix.row_basis == manual_rows
        assert engine_matrix.col_basis == manual_cols
        assert engine_matrix.entries == manual_entries

    def test_feynman_matrix_matches_manual_matrix(self):
        manual_rows, manual_cols, manual_entries = _manual_matrix()
        engine_matrix = tree_level_feynman_matrix_arity3()
        assert engine_matrix.row_basis == manual_rows
        assert engine_matrix.col_basis == manual_cols
        assert engine_matrix.entries == manual_entries

    def test_tree_level_matching_helper_reports_full_agreement(self):
        result = verify_tree_level_matching(level=4)
        assert result["matched"]
        assert result["mismatches"] == []

    def test_dressed_tree_amplitude_respects_level_prefix(self):
        expected_level_two = {
            ("e", "f"): Fraction(4),
            ("h", "h"): Fraction(-2),
        }
        # VERIFIED: [DC] d_3([h|e|f]) = 2[e|f] - [h|h] and the dressed amplitude multiplies by k;
        # [LC] k = 0 forces the amplitude to vanish because r^KM(z) = k * Omega / z.
        assert tree_level_dressed_amplitude(2, ("h", "e", "f")) == expected_level_two
        assert tree_level_dressed_amplitude(0, ("h", "e", "f")) == {}


class TestGenusOneMatching:
    @pytest.mark.parametrize(
        ("level", "expected"),
        [
            (0, Fraction(3, 2)),
            (-2, Fraction(0)),
        ],
    )
    def test_kappa_boundary_values(self, level, expected):
        # VERIFIED: [DC] kappa(V_k(sl_2)) = 3(k+2)/4; [LC] k = 0 -> 3/2 and k = -2 -> 0.
        assert affine_sl2_kappa(level) == expected

    @pytest.mark.parametrize(
        ("level", "expected"),
        [
            (1, Fraction(3, 32)),
            (2, Fraction(1, 8)),
            (4, Fraction(3, 16)),
            (10, Fraction(3, 8)),
        ],
    )
    def test_genus1_bar_and_feynman_totals_match_manual_values(self, level, expected):
        # VERIFIED: [DC] F_1 = kappa/24 with kappa = 3(k+2)/4, so F_1 = (k+2)/32;
        # [LC] the same formula gives F_1(-2) = 0 and F_1(0) = 1/16.
        assert _manual_f1(level) == expected
        assert genus1_bar_amplitude(level) == expected
        assert genus1_feynman_amplitude(level) == expected

    def test_genus1_feynman_decomposition_at_k4(self):
        classical_piece = Fraction(1, 8)
        quantum_shift = Fraction(1, 16)
        total = Fraction(3, 16)
        # VERIFIED: [DC] classical piece = k/32 and quantum shift = 1/16, so at k = 4 the sum is 3/16;
        # [CF] this equals F_1 = (k+2)/32 from the affine kappa formula.
        assert genus1_feynman_classical_piece(4) == classical_piece
        assert genus1_feynman_quantum_shift() == quantum_shift
        assert genus1_feynman_amplitude(4) == total

    def test_genus1_critical_level_vanishes(self):
        # VERIFIED: [DC] F_1 = (k+2)/32; [LC] the critical level k = -2 gives F_1 = 0.
        assert genus1_bar_amplitude(-2) == Fraction(0)
        assert genus1_feynman_amplitude(-2) == Fraction(0)

    def test_genus1_match_report_agrees_at_sample_level(self):
        report = genus1_match_report(2)
        # VERIFIED: [DC] F_1(2) = (2+2)/32 = 1/8; [CF] bar and Feynman lanes use the same affine shift.
        assert report.classical_piece == Fraction(1, 16)
        assert report.quantum_shift == Fraction(1, 16)
        assert report.feynman_total == Fraction(1, 8)
        assert report.bar_total == Fraction(1, 8)
        assert report.matched

    def test_genus1_matching_helper_reports_full_agreement(self):
        result = verify_genus1_matching(levels=(1, 2, 4, 10, -2))
        assert result["matched"]
        assert result["mismatches"] == []
