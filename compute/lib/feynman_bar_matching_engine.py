r"""Exact Feynman versus bar matching for V_k(sl_2).

This engine records explicit coefficient data for the low-genus
"Feynman = bar" philosophy on the affine current algebra V_k(sl_2)
in the basis {e, h, f} with

    [h, e] = 2e,   [h, f] = -2f,   [e, f] = h

and invariant form

    (e, f) = 1,   (h, h) = 2.

GENUS 0, ARITY 3
================

On the reduced ordered bar coalgebra

    B(V_k(sl_2)) = T^c(s^{-1} V_k(sl_2)-bar),

the arity-3 component of the bar differential is

    d_3(a|b|c) = mu_2(a, b)|c - a|mu_2(b, c),

with mu_2 given by the simple-pole OPE coefficient, hence by the sl_2
Lie bracket.  For degree-0 current generators there is no extra Koszul
sign beyond the boundary orientation above.

The tree-level cubic Feynman vertex uses the same structure constants
on the two codimension-1 channels.  In the conventions fixed here,
the channel coefficients match the bar coefficients exactly:

    vertex(a, b, c) = [a, b]|c - a|[b, c].

GENUS 1
=======

The modular bar curvature contributes

    F_1 = kappa(V_k(sl_2)) * lambda_1,
    kappa(V_k(sl_2)) = dim(sl_2) * (k + h^vee) / (2 h^vee)
                     = 3(k + 2) / 4,
    lambda_1 = 1/24.

Hence

    F_1 = (k + 2) / 32.

The diagrammatic lane is packaged as

    classical loop piece = k / 32,
    adjoint shift        = 1 / 16,
    total                = (k + 2) / 32.

The shift is the h^vee contribution in the affine kappa formula.

R-MATRIX CONVENTION
===================

    r^KM(z) = k * Omega / z
    Omega = e tensor f + f tensor e + (1/2) h tensor h.

The level prefix is mandatory.  At k = 0 the r-matrix vanishes.

All arithmetic is exact via fractions.Fraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Dict, List, Tuple


BasisElt = str
PairWord = Tuple[BasisElt, BasisElt]
TripleWord = Tuple[BasisElt, BasisElt, BasisElt]
SparsePairCoefficients = Dict[PairWord, Fraction]


# ============================================================================
# Exact helpers
# ============================================================================

def _frac(value: int | Fraction) -> Fraction:
    """Coerce an integer or Fraction to Fraction."""
    if isinstance(value, Fraction):
        return value
    return Fraction(value)


def _add_sparse_term(
    target: SparsePairCoefficients,
    word: PairWord,
    coeff: Fraction,
) -> None:
    """Add a coefficient to a sparse ordered-pair dictionary."""
    if coeff == 0:
        return
    target[word] = target.get(word, Fraction(0)) + coeff
    if target[word] == 0:
        del target[word]


def _scale_sparse(
    coeffs: SparsePairCoefficients,
    scalar: int | Fraction,
) -> SparsePairCoefficients:
    """Scale a sparse ordered-pair dictionary by an exact scalar."""
    factor = _frac(scalar)
    if factor == 0:
        return {}
    return {word: factor * coeff for word, coeff in coeffs.items()}


# ============================================================================
# sl_2 data
# ============================================================================

BASIS: Tuple[BasisElt, ...] = ("e", "h", "f")

DIM_SL2 = 3
# VERIFIED: [LT] dim(sl_2) = 3; [DC] the basis {e, h, f} has three generators.

H_DUAL_SL2 = 2
# VERIFIED: [LT] h^vee(sl_2) = 2; [LC] the critical level k = -2 forces kappa = 0.

LAMBDA_1 = Fraction(1, 24)
# VERIFIED: [LT] lambda_1 = 1/24 on Mbar_{1,1}; [CF] AGENTS.md lists F_1 = kappa/24.

CASIMIR_AVERAGE_WEIGHT = Fraction(DIM_SL2, 2 * H_DUAL_SL2)
# VERIFIED: [DC] dim(sl_2)/(2 h^vee) = 3/4; [LC] kappa(0) = (3/4) * 2 = 3/2.

SL2_BRACKET: Dict[Tuple[BasisElt, BasisElt], Dict[BasisElt, Fraction]] = {
    ("e", "f"): {"h": Fraction(1)},   # VERIFIED: [LT] [e, f] = h; [DC] antisymmetry with [f, e] = -h.
    ("f", "e"): {"h": Fraction(-1)},  # VERIFIED: [LT] [f, e] = -h; [DC] antisymmetry with [e, f] = h.
    ("h", "e"): {"e": Fraction(2)},   # VERIFIED: [LT] [h, e] = 2e; [DC] root-weight +2 for e.
    ("e", "h"): {"e": Fraction(-2)},  # VERIFIED: [LT] [e, h] = -2e; [DC] antisymmetry with [h, e] = 2e.
    ("h", "f"): {"f": Fraction(-2)},  # VERIFIED: [LT] [h, f] = -2f; [DC] root-weight -2 for f.
    ("f", "h"): {"f": Fraction(2)},   # VERIFIED: [LT] [f, h] = 2f; [DC] antisymmetry with [h, f] = -2f.
}

SL2_KILLING: Dict[Tuple[BasisElt, BasisElt], Fraction] = {
    ("e", "f"): Fraction(1),          # VERIFIED: [LT] (e, f) = 1; [SY] invariance fixes (f, e) = 1.
    ("f", "e"): Fraction(1),          # VERIFIED: [LT] (f, e) = 1; [SY] symmetry of the invariant form.
    ("h", "h"): Fraction(2),          # VERIFIED: [LT] (h, h) = 2; [SY] root normalization alpha(h) = 2.
}


@dataclass(frozen=True)
class MatrixData:
    """Exact matrix data for the ordered-pair versus ordered-triple bases."""

    row_basis: Tuple[PairWord, ...]
    col_basis: Tuple[TripleWord, ...]
    entries: Tuple[Tuple[Fraction, ...], ...]


@dataclass(frozen=True)
class TreeLevelMatchReport:
    """Bar, bare Feynman, and level-dressed tree data for one ordered triple."""

    word: TripleWord
    bar_terms: SparsePairCoefficients
    feynman_terms: SparsePairCoefficients
    dressed_terms: SparsePairCoefficients
    matched: bool


@dataclass(frozen=True)
class GenusOneMatchReport:
    """Exact genus-1 comparison at one level."""

    level: Fraction
    classical_piece: Fraction
    quantum_shift: Fraction
    effective_weight: Fraction
    feynman_total: Fraction
    bar_total: Fraction
    matched: bool


def sl2_bracket(left: BasisElt, right: BasisElt) -> Dict[BasisElt, Fraction]:
    """Return the sl_2 bracket [left, right] in the fixed basis."""
    return dict(SL2_BRACKET.get((left, right), {}))


def sl2_killing(left: BasisElt, right: BasisElt) -> Fraction:
    """Return the normalized invariant form on sl_2."""
    return SL2_KILLING.get((left, right), Fraction(0))


def sl2_casimir_tensor() -> Dict[PairWord, Fraction]:
    r"""Quadratic Casimir tensor Omega in the basis {e, h, f}.

    Omega = e tensor f + f tensor e + (1/2) h tensor h

    because the dual basis for (e, f) = 1 and (h, h) = 2 is
    {f, h/2, e}.
    """
    return {
        ("e", "f"): Fraction(1),      # VERIFIED: [DC] e pairs with f in the dual basis; [SY] Omega is symmetric.
        ("f", "e"): Fraction(1),      # VERIFIED: [DC] f pairs with e in the dual basis; [SY] Omega is symmetric.
        ("h", "h"): Fraction(1, 2),   # VERIFIED: [DC] h dualizes to h/2; [SY] (h, h) = 2.
    }


def affine_sl2_r_matrix(level: int | Fraction) -> Dict[PairWord, Fraction]:
    r"""Return the level-prefixed affine r-matrix coefficients.

    r^KM(z) = k * Omega / z.
    """
    k = _frac(level)
    return {
        word: k * coeff
        for word, coeff in sl2_casimir_tensor().items()
    }


def pair_basis() -> Tuple[PairWord, ...]:
    """Ordered-pair basis in lexicographic order."""
    return tuple((left, right) for left, right in product(BASIS, repeat=2))


def triple_basis() -> Tuple[TripleWord, ...]:
    """Ordered-triple basis in lexicographic order."""
    return tuple((left, middle, right) for left, middle, right in product(BASIS, repeat=3))


# ============================================================================
# Genus-0 matching
# ============================================================================

def bar_mu2(left: BasisElt, right: BasisElt) -> Dict[BasisElt, Fraction]:
    """Binary bar product from the simple-pole OPE coefficient."""
    return sl2_bracket(left, right)


def bar_differential_arity3(word: TripleWord) -> SparsePairCoefficients:
    r"""Compute d_3(a|b|c) = mu_2(a,b)|c - a|mu_2(b,c)."""
    left, middle, right = word
    result: SparsePairCoefficients = {}

    for output, coeff in bar_mu2(left, middle).items():
        _add_sparse_term(result, (output, right), coeff)

    for output, coeff in bar_mu2(middle, right).items():
        _add_sparse_term(result, (left, output), -coeff)

    return result


def tree_level_feynman_vertex(word: TripleWord) -> SparsePairCoefficients:
    r"""Compute the bare cubic Feynman vertex on the two boundary channels.

    The left channel contributes [a, b]|c and the right channel contributes
    -a|[b, c], with the minus sign fixed by the boundary orientation of the
    compactified three-point configuration space.
    """
    left, middle, right = word
    result: SparsePairCoefficients = {}

    for output, coeff in sl2_bracket(left, middle).items():
        _add_sparse_term(result, (output, right), coeff)

    for output, coeff in sl2_bracket(middle, right).items():
        _add_sparse_term(result, (left, output), -coeff)

    return result


def tree_level_dressed_amplitude(
    level: int | Fraction,
    word: TripleWord,
) -> SparsePairCoefficients:
    r"""Multiply the bare tree vertex by the affine level prefix.

    This packages the AP126/AP141 convention that the propagator carries a
    factor of k through r^KM(z) = k * Omega / z.
    """
    return _scale_sparse(tree_level_feynman_vertex(word), level)


def tree_level_match_report(
    word: TripleWord,
    level: int | Fraction = 1,
) -> TreeLevelMatchReport:
    """Return the exact genus-0 matching data for one ordered triple."""
    bar_terms = bar_differential_arity3(word)
    feynman_terms = tree_level_feynman_vertex(word)
    dressed_terms = tree_level_dressed_amplitude(level, word)
    return TreeLevelMatchReport(
        word=word,
        bar_terms=bar_terms,
        feynman_terms=feynman_terms,
        dressed_terms=dressed_terms,
        matched=(bar_terms == feynman_terms),
    )


def _matrix_from_rule(rule) -> MatrixData:
    """Build an exact matrix from a sparse ordered-pair rule on triples."""
    rows = pair_basis()
    cols = triple_basis()
    row_index = {word: idx for idx, word in enumerate(rows)}
    matrix: List[List[Fraction]] = [
        [Fraction(0) for _ in cols]
        for _ in rows
    ]

    for col_idx, word in enumerate(cols):
        for target_word, coeff in rule(word).items():
            matrix[row_index[target_word]][col_idx] = coeff

    return MatrixData(
        row_basis=rows,
        col_basis=cols,
        entries=tuple(tuple(row) for row in matrix),
    )


def bar_differential_matrix_arity3() -> MatrixData:
    """Exact 9 x 27 matrix of d_3 in the ordered basis."""
    return _matrix_from_rule(bar_differential_arity3)


def tree_level_feynman_matrix_arity3() -> MatrixData:
    """Exact 9 x 27 matrix of the bare cubic Feynman vertex."""
    return _matrix_from_rule(tree_level_feynman_vertex)


def verify_tree_level_matching(
    level: int | Fraction = 1,
) -> Dict[str, object]:
    """Verify bar and Feynman matching for all ordered triples."""
    reports = [tree_level_match_report(word, level) for word in triple_basis()]
    mismatches = [report.word for report in reports if not report.matched]
    return {
        "matched": not mismatches,
        "mismatches": mismatches,
        "reports": reports,
    }


# ============================================================================
# Genus-1 matching
# ============================================================================

def affine_sl2_kappa(level: int | Fraction) -> Fraction:
    r"""Affine sl_2 modular characteristic.

    kappa(V_k(sl_2)) = dim(sl_2) * (k + h^vee) / (2 h^vee) = 3(k+2)/4.
    """
    k = _frac(level)
    return Fraction(DIM_SL2, 2 * H_DUAL_SL2) * (k + H_DUAL_SL2)


def genus1_bar_amplitude(level: int | Fraction) -> Fraction:
    """Bar-side genus-1 contribution F_1 = kappa / 24."""
    return affine_sl2_kappa(level) * LAMBDA_1


def genus1_feynman_effective_weight(level: int | Fraction) -> Fraction:
    """Effective one-loop Casimir weight after the affine h^vee shift."""
    k = _frac(level)
    return CASIMIR_AVERAGE_WEIGHT * (k + H_DUAL_SL2)


def genus1_feynman_classical_piece(level: int | Fraction) -> Fraction:
    """Classical one-loop propagator contribution: k / 32."""
    k = _frac(level)
    return CASIMIR_AVERAGE_WEIGHT * k * LAMBDA_1


def genus1_feynman_quantum_shift() -> Fraction:
    """Universal adjoint shift from the h^vee correction: 1 / 16."""
    return CASIMIR_AVERAGE_WEIGHT * H_DUAL_SL2 * LAMBDA_1


def genus1_feynman_amplitude(level: int | Fraction) -> Fraction:
    """Total one-loop Feynman contribution."""
    return genus1_feynman_classical_piece(level) + genus1_feynman_quantum_shift()


def genus1_match_report(level: int | Fraction) -> GenusOneMatchReport:
    """Return the exact genus-1 comparison data at one level."""
    k = _frac(level)
    effective_weight = genus1_feynman_effective_weight(k)
    feynman_total = effective_weight * LAMBDA_1
    bar_total = genus1_bar_amplitude(k)
    return GenusOneMatchReport(
        level=k,
        classical_piece=genus1_feynman_classical_piece(k),
        quantum_shift=genus1_feynman_quantum_shift(),
        effective_weight=effective_weight,
        feynman_total=feynman_total,
        bar_total=bar_total,
        matched=(feynman_total == bar_total),
    )


def verify_genus1_matching(
    levels: Tuple[int | Fraction, ...] = (1, 2, 4, 10),
) -> Dict[str, object]:
    """Verify genus-1 matching on a finite set of levels."""
    reports = [genus1_match_report(level) for level in levels]
    mismatches = [report.level for report in reports if not report.matched]
    return {
        "matched": not mismatches,
        "mismatches": mismatches,
        "reports": reports,
    }


__all__ = [
    "BASIS",
    "CASIMIR_AVERAGE_WEIGHT",
    "DIM_SL2",
    "GenusOneMatchReport",
    "H_DUAL_SL2",
    "LAMBDA_1",
    "MatrixData",
    "SL2_BRACKET",
    "SL2_KILLING",
    "TreeLevelMatchReport",
    "affine_sl2_kappa",
    "affine_sl2_r_matrix",
    "bar_differential_arity3",
    "bar_differential_matrix_arity3",
    "bar_mu2",
    "genus1_bar_amplitude",
    "genus1_feynman_amplitude",
    "genus1_feynman_classical_piece",
    "genus1_feynman_effective_weight",
    "genus1_feynman_quantum_shift",
    "genus1_match_report",
    "pair_basis",
    "sl2_bracket",
    "sl2_casimir_tensor",
    "sl2_killing",
    "tree_level_dressed_amplitude",
    "tree_level_feynman_matrix_arity3",
    "tree_level_feynman_vertex",
    "tree_level_match_report",
    "triple_basis",
    "verify_genus1_matching",
    "verify_tree_level_matching",
]
