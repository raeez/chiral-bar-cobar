r"""Virasoro Ward correlators and the level-four/five vacuum Gram matrices.

The sphere Ward recursion and connected correlators are implemented in
:mod:`compute.lib.virasoro_ward_correlators`.  The functions retained here
give the genuine Virasoro algebra calculations used by earlier callers.

The weighted-Riccati expression

    -48 / (c^2 (5 c + 22))

is exposed as a candidate scalar attached to that recurrence.  Its
identification with an Arnold residue requires the ordered residue complex
``H_res(Vir_c; X)`` and a normalized projection.  The coordinate correlator
supplies the input to that future construction.

Two consistency checks are implemented for the candidate; NEITHER is an
independent residue-complex derivation of ``S_5``:

1. recursion consistency -- the candidate equals the arity-five output of
   the master-equation recurrence (:func:`s5_virasoro_recursion`);
2. inverse-Gram shape -- the level-five vacuum Gram matrix in the basis
   ``(L_{-5}|0>, L_{-3}L_{-2}|0>)`` computed from the Virasoro commutators
   alone has determinant ``2 c^2 (5c+22)``, and the candidate satisfies
   ``S_5 * det G_5 = -96``, the same inverse-Gram shape as
   ``S_4 = 1/<Lambda|Lambda>`` at level four.

The vacuum expectation engine (:func:`virasoro_vacuum_expectation`) uses
only ``[L_m, L_n] = (m-n) L_{m+n} + (c/12)(m^3-m) delta_{m+n,0}`` together
with ``L_n |0> = 0`` for ``n >= -1``; the Gram matrices are recomputed from
it rather than transcribed.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Tuple

import sympy as sp

from compute.lib.virasoro_ward_correlators import (
    CENTRAL_CHARGE,
    ResidueProjectionRequired,
    require_residue_projection,
    standard_points,
    virasoro_connected_correlator,
    virasoro_ward_correlator,
)


def bpz_ope_coefficients(c: Fraction) -> Dict[int, Fraction]:
    r"""Return the coefficients of the singular ``T(z)T(w)`` OPE."""

    return {
        4: Fraction(c) / 2,
        2: Fraction(2),
        1: Fraction(1),
    }


def virasoro_vacuum_expectation(
    modes: Tuple[int, ...], c_sym: sp.Expr
) -> sp.Expr:
    r"""Return ``<0| L_{m_1} ... L_{m_k} |0>`` from the commutators alone.

    Inputs: ``modes = (m_1, ..., m_k)``.  The recursion uses only

        [L_m, L_n] = (m - n) L_{m+n} + (c/12)(m^3 - m) delta_{m+n,0},
        L_n |0> = 0   for n >= -1,
        <0| L_m = 0   for m <= 1,

    and terminates because every step shortens the word by one letter.
    """

    c = sp.sympify(c_sym)

    def vev(word: Tuple[int, ...]) -> sp.Expr:
        if not word:
            return sp.Integer(1)
        m = word[-1]
        if m >= -1:
            return sp.Integer(0)
        # m <= -2: move L_m left past every letter; the surviving term
        # <0| L_m ... vanishes because m <= -2 <= 1.
        prefix = word[:-1]
        total = sp.Integer(0)
        for i, a in enumerate(prefix):
            rest = prefix[:i] + prefix[i + 1 :]
            # [L_a, L_m] = (a - m) L_{a+m} + (c/12)(a^3 - a) delta_{a+m,0}
            replaced = prefix[:i] + (a + m,) + prefix[i + 1 : ]
            total += (a - m) * vev(replaced)
            if a + m == 0:
                total += sp.Rational(1, 12) * c * (a**3 - a) * vev(rest)
        return sp.expand(total)

    return sp.expand(vev(tuple(modes)))


def virasoro_level4_gram_matrix(c_sym: sp.Expr) -> sp.Matrix:
    r"""Return the vacuum Gram matrix on ``(L_-4|0>, L_-2^2|0>)``.

    Repeated use of

        [L_m,L_n] = (m-n)L_{m+n} + c(m^3-m) delta_{m+n,0}/12

    gives entries ``5c``, ``3c``, and ``c(c+8)/2``.
    """

    c = sp.sympify(c_sym)
    return sp.Matrix(
        [
            [5 * c, 3 * c],
            [3 * c, c * (c + 8) / 2],
        ]
    )


def virasoro_level4_gram_matrix_from_commutators(
    c_sym: sp.Expr,
) -> sp.Matrix:
    r"""Recompute the level-four Gram matrix with the vacuum engine.

    Basis ``(L_{-4}|0>, L_{-2}^2|0>)``; adjoints ``L_4`` and ``L_2 L_2``.
    """

    vev = lambda modes: virasoro_vacuum_expectation(modes, c_sym)
    return sp.Matrix(
        [
            [vev((4, -4)), vev((4, -2, -2))],
            [vev((2, 2, -4)), vev((2, 2, -2, -2))],
        ]
    )


def virasoro_level5_gram_matrix(c_sym: sp.Expr) -> sp.Matrix:
    r"""Return the vacuum Gram matrix on ``(L_{-5}|0>, L_{-3}L_{-2}|0>)``.

    Level five of the vacuum module is two-dimensional (partitions of 5
    into parts ``>= 2``: ``5`` and ``3+2``).  The entries are computed by
    :func:`virasoro_vacuum_expectation` from the commutators alone:

        G_11 = <0| L_5 L_{-5} |0>            = 10 c,
        G_12 = <0| L_5 L_{-3} L_{-2} |0>     = 4 c,
        G_22 = <0| L_2 L_3 L_{-3} L_{-2} |0> = c (c + 6).
    """

    vev = lambda modes: virasoro_vacuum_expectation(modes, c_sym)
    return sp.Matrix(
        [
            [vev((5, -5)), vev((5, -3, -2))],
            [vev((2, 3, -5)), vev((2, 3, -3, -2))],
        ]
    )


def virasoro_level5_gram_determinant(c_sym: sp.Expr) -> sp.Expr:
    r"""Return ``det G_5 = 2 c^2 (5c+22)`` by exact determinant."""

    return sp.factor(virasoro_level5_gram_matrix(c_sym).det())


def s5_times_level5_gram_determinant(c: Fraction) -> Fraction:
    r"""Return ``S_5^Ricc(c) * det G_5(c)``; the inverse-Gram shape is -96.

    This is a shape consistency check, not a derivation: it verifies that
    the weighted-Riccati candidate has the form ``const / det G_5``, the
    level-five analogue of ``S_4 = 1/<Lambda|Lambda>``.
    """

    value = Fraction(c)
    determinant = 2 * value**2 * (5 * value + 22)
    symbolic = virasoro_level5_gram_determinant(sp.Rational(value))
    if sp.simplify(symbolic - sp.Rational(determinant)) != 0:
        raise AssertionError(
            "level-5 Gram determinant mismatch between the commutator "
            "engine and the closed form"
        )
    return s5_weighted_riccati_candidate(value) * determinant


def virasoro_level4_gram_determinant(c_sym: sp.Expr) -> sp.Expr:
    r"""Return ``det G_4 = c^2(5c+22)/2`` by exact determinant."""

    return sp.factor(virasoro_level4_gram_matrix(c_sym).det())


def zamolodchikov_lambda_norm(c: Fraction) -> Fraction:
    r"""Return ``<Lambda|Lambda> = c(5c+22)/10`` by Schur complement."""

    value = Fraction(c)
    return value * (5 * value + 22) / 10


def verify_lambda_norm_symbolic() -> Tuple[sp.Expr, sp.Expr]:
    r"""Return the determinant and quasi-primary Schur complement."""

    c = sp.Symbol("c")
    gram = virasoro_level4_gram_matrix(c)
    determinant = sp.factor(gram.det())
    schur_complement = sp.factor(
        gram[1, 1] - gram[0, 1] ** 2 / gram[0, 0]
    )
    return determinant, schur_complement


def bpz_three_point_function() -> sp.Expr:
    r"""Return the three-point stress-tensor correlator from Ward recursion."""

    points = standard_points(3)
    return sp.factor(virasoro_ward_correlator(points, CENTRAL_CHARGE))


def g5_connected_ward_correlator(
    central_charge: object = CENTRAL_CHARGE,
) -> sp.Expr:
    r"""Return the coordinate-dependent connected five-point correlator."""

    return virasoro_connected_correlator(standard_points(5), central_charge)


def g6_connected_ward_correlator(
    central_charge: object = CENTRAL_CHARGE,
) -> sp.Expr:
    r"""Return the coordinate-dependent connected six-point correlator."""

    return virasoro_connected_correlator(standard_points(6), central_charge)


def s3_from_three_point_arnold_residue(_c: Fraction) -> Fraction:
    r"""Request the residue data that define the scalar cubic extraction."""

    require_residue_projection(3)


def lambda_channel_combinatorial_weight() -> Fraction:
    r"""Request the ordered residue normalization of the level-four channel."""

    require_residue_projection(5)


def s5_via_lambda_channel(_c: Fraction) -> Fraction:
    r"""Request the chain map from the level-four channel to the residue."""

    require_residue_projection(5)


def s5_virasoro_wick(_c) -> Fraction:
    r"""Request the datum that projects ``G_5^conn`` to a scalar ``S_5``."""

    require_residue_projection(5)


def s5_weighted_riccati_candidate(c) -> Fraction:
    r"""Return the arity-five value of the weighted-Riccati recurrence."""

    value = Fraction(c)
    return Fraction(-48) / (value**2 * (5 * value + 22))


def s5_virasoro_recursion(c) -> Fraction:
    r"""Return the weighted-Riccati value computed by the recurrence engine."""

    from compute.lib.shadow_tower_ope_recursion import (
        mc_recursion_rational,
        virasoro_shadow_data_frac,
    )

    value = Fraction(c)
    kappa, s3, s4 = virasoro_shadow_data_frac(value)
    return mc_recursion_rational(kappa, s3, s4, max_r=5)[5]


def s5_virasoro_closed_form(c) -> Fraction:
    r"""Compatibility name for the weighted-Riccati candidate formula."""

    return s5_weighted_riccati_candidate(c)


__all__ = [
    "ResidueProjectionRequired",
    "bpz_ope_coefficients",
    "bpz_three_point_function",
    "g5_connected_ward_correlator",
    "g6_connected_ward_correlator",
    "lambda_channel_combinatorial_weight",
    "s3_from_three_point_arnold_residue",
    "s5_times_level5_gram_determinant",
    "s5_via_lambda_channel",
    "s5_virasoro_closed_form",
    "s5_virasoro_recursion",
    "s5_virasoro_wick",
    "s5_weighted_riccati_candidate",
    "verify_lambda_norm_symbolic",
    "virasoro_level4_gram_determinant",
    "virasoro_level4_gram_matrix",
    "virasoro_level4_gram_matrix_from_commutators",
    "virasoro_level5_gram_determinant",
    "virasoro_level5_gram_matrix",
    "virasoro_vacuum_expectation",
    "zamolodchikov_lambda_norm",
]
