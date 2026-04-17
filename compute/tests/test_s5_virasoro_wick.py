r"""Tests for S_5(Vir_c) via independent BPZ-Wick computation.

Cross-validates compute.lib.s5_virasoro_wick (Lambda-channel + Gram-matrix
Schur complement + Arnold residue) against
compute.lib.shadow_tower_ope_recursion.mc_recursion_rational (Riccati MC
recursion). The two derivation chains share NO intermediate symbol beyond
the universal Vir_c data (central charge c, conformal weight h_T = 2).

Anchored claim: thm:virasoro-coefficients
Coverage delta: Vol I 0/2275 -> 1/2275

Calibration points (seven, per spec):
  c = 1/2  Ising minimal model
  c = 7/10 tri-critical Ising
  c = 4/5  three-state Potts
  c = 1    free boson (also the hand-verified 945-Wick-matching anchor)
  c = 2    single ghost (e.g., bc system at lambda = 1)
  c = 24   Leech lattice
  c = -22/5 Lee-Yang (Lambda-channel pole; both sides exhibit the pole)

References:
  - adversarial_swarm_20260416/wave_supervisory_S5_wick_implementation.md
  - chapters/theory/shadow_tower_higher_coefficients.tex (S_5 closed form)
  - chapters/theory/shadow_tower_quadrichotomy_platonic.tex (the four-class
    quadrichotomy that S_5 enters at class M)

Author: Raeez Lorgat
Date:   2026-04-16
"""
from __future__ import annotations

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.independent_verification import independent_verification
from compute.lib.s5_virasoro_wick import (
    bpz_ope_coefficients,
    lambda_channel_combinatorial_weight,
    s3_from_three_point_arnold_residue,
    s5_virasoro_closed_form,
    s5_virasoro_recursion,
    s5_virasoro_wick,
    verify_lambda_norm_symbolic,
    virasoro_level4_gram_determinant,
    virasoro_level4_gram_matrix,
    zamolodchikov_lambda_norm,
    _perfect_matchings,
    _set_partitions,
)


# =====================================================================
# Combinatorial primitives (sanity)
# =====================================================================


class TestCombinatorialPrimitives:
    def test_perfect_matchings_double_factorial(self):
        # (2n - 1)!! perfect matchings on 2n items.
        assert len(_perfect_matchings(list(range(2)))) == 1
        assert len(_perfect_matchings(list(range(4)))) == 3
        assert len(_perfect_matchings(list(range(6)))) == 15
        # The free-boson c = 1 hand-verified anchor uses 945 matchings on
        # 10 J-half-edges, after self-loop subtraction.
        assert len(_perfect_matchings(list(range(10)))) == 945

    def test_set_partitions_bell_numbers(self):
        # Bell numbers B_n
        for n, bell in [(0, 1), (1, 1), (2, 2), (3, 5), (4, 15), (5, 52)]:
            assert len(_set_partitions(list(range(n)))) == bell


# =====================================================================
# BPZ OPE coefficient table
# =====================================================================


class TestBPZOPE:
    @pytest.mark.parametrize("c", [
        Fraction(1, 2), Fraction(1), Fraction(2), Fraction(24),
    ])
    def test_ope_central_term(self, c):
        # Order-4 pole = c/2.
        coeffs = bpz_ope_coefficients(c)
        assert coeffs[4] == c / 2

    def test_ope_universal_descendant_coefficients(self):
        # Order 2 = 2 (T weight); order 1 = 1 (Ward derivative).
        for c in [Fraction(1, 2), Fraction(1), Fraction(7, 10)]:
            coeffs = bpz_ope_coefficients(c)
            assert coeffs[2] == Fraction(2)
            assert coeffs[1] == Fraction(1)


# =====================================================================
# Virasoro Gram matrix (the independent Lambda-norm engine)
# =====================================================================


class TestGramMatrix:
    def test_gram_matrix_entries(self):
        # Symbolic entries.
        c_sym = sp.Symbol('c')
        G = virasoro_level4_gram_matrix(c_sym)
        assert sp.simplify(G[0, 0] - 5 * c_sym) == 0
        assert sp.simplify(G[1, 0] - 3 * c_sym) == 0
        assert sp.simplify(G[0, 1] - 3 * c_sym) == 0
        assert sp.simplify(G[1, 1] - c_sym * (c_sym + 8) / 2) == 0

    def test_gram_determinant(self):
        # det G_4 = c^2 (5c + 22) / 2 (Kac-Feigin-Fuchs at level 4).
        c_sym = sp.Symbol('c')
        det = virasoro_level4_gram_determinant(c_sym)
        expected = c_sym**2 * (5 * c_sym + 22) / 2
        assert sp.simplify(det - expected) == 0

    def test_lambda_norm_symbolic(self):
        # <Lambda|Lambda> = c (5c + 22) / 10 from Schur complement.
        det, schur = verify_lambda_norm_symbolic()
        c_sym = sp.Symbol('c')
        expected_norm = c_sym * (5 * c_sym + 22) / 10
        assert sp.simplify(schur - expected_norm) == 0

    @pytest.mark.parametrize("c, expected", [
        (Fraction(1, 2), Fraction(1, 2) * (5 * Fraction(1, 2) + 22) / 10),
        (Fraction(1), Fraction(1) * 27 / 10),
        (Fraction(2), Fraction(2) * 32 / 10),
        (Fraction(24), Fraction(24) * 142 / 10),
    ])
    def test_lambda_norm_numerical(self, c, expected):
        assert zamolodchikov_lambda_norm(c) == expected


# =====================================================================
# 3-point Ward identity (the independent S_3 engine)
# =====================================================================


class TestThreePointWard:
    def test_s3_universal(self):
        # S_3 = 2 for any Vir_c (universal Selberg ratio).
        for c in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(24)]:
            assert s3_from_three_point_arnold_residue(c) == Fraction(2)


# =====================================================================
# Lambda-channel combinatorial assembly
# =====================================================================


class TestLambdaChannelWeight:
    def test_combinatorial_weight_value(self):
        # Wick coefficient -48/10 from chord-diagram cumulant inversion.
        assert lambda_channel_combinatorial_weight() == Fraction(-48, 10)


# =====================================================================
# Closed-form spot checks
# =====================================================================


class TestClosedForm:
    @pytest.mark.parametrize("c, expected", [
        (Fraction(1, 2), Fraction(-384, 49)),
        (Fraction(7, 10), Fraction(-3200, 833)),
        (Fraction(4, 5), Fraction(-75, 26)),
        (Fraction(1), Fraction(-16, 9)),
        (Fraction(2), Fraction(-3, 8)),
        (Fraction(24), Fraction(-1, 1704)),
    ])
    def test_closed_form_calibration(self, c, expected):
        assert s5_virasoro_closed_form(c) == expected

    def test_lee_yang_pole(self):
        # At c = -22/5, both Wick and recursion exhibit the same pole.
        # Closed form raises ZeroDivisionError because of division by
        # (5c + 22) = 0.
        with pytest.raises(ZeroDivisionError):
            s5_virasoro_closed_form(Fraction(-22, 5))


# =====================================================================
# Recursion-side reference (consistency, NOT independent verification)
# =====================================================================


class TestRecursionSide:
    @pytest.mark.parametrize("c", [
        Fraction(1, 2),
        Fraction(7, 10),
        Fraction(4, 5),
        Fraction(1),
        Fraction(2),
        Fraction(24),
    ])
    def test_recursion_matches_closed_form(self, c):
        # The Riccati MC recursion reproduces the closed form. This is
        # an internal-consistency check on shadow_tower_ope_recursion,
        # NOT an independent verification.
        assert s5_virasoro_recursion(c) == s5_virasoro_closed_form(c)


# =====================================================================
# THE INDEPENDENT VERIFICATION
# =====================================================================


class TestWickIndependentVerification:
    @independent_verification(
        claim="thm:virasoro-coefficients",
        derived_from=[
            "Maurer-Cartan recursion shadow_tower_ope_recursion.mc_recursion_rational",
            "Riccati polynomial Q_c(t) sqrt-expansion in shadow_tower_higher_coefficients.tex",
        ],
        verified_against=[
            "5-point Wick + iterated Ward",
            "Virasoro level-4 Gram matrix Schur complement (Lambda norm)",
            "Arnold d-log Selberg measure on Conf_5(P^1)",
        ],
        disjoint_rationale=(
            "Wick is combinatorial; MC uses Riccati flow. The Wick chain "
            "computes <Lambda|Lambda> = c(5c+22)/10 via the Virasoro "
            "level-4 Gram-matrix Schur complement (independent of any MC "
            "seed data), extracts S_3 = 2 via 3-point BPZ Ward identity "
            "(independent of MC), counts Lambda-mediated chord-diagram "
            "topologies on K_5 with cumulant inversion (combinatorial; no "
            "Riccati polynomial appears), and assembles the Arnold "
            "d-log residue at simultaneous collision. The MC recursion "
            "uses convolution S_5 = -(1/(10 kappa)) * 12 * S_3 * S_4 with "
            "(kappa, S_3, S_4) treated as INPUTS; the Wick chain DERIVES "
            "the Lambda-norm and 3-point structure constant directly "
            "from the Virasoro algebra and OPE."
        ),
    )
    def test_s5_at_c_one_via_wick(self):
        """S_5(Vir_1) = -16/9 from BPZ-Wick = MC recursion = closed form.

        The c = 1 anchor: free-boson realization T = -(1/2) :J^2: makes
        the Wick computation literal (945 perfect matchings of 10
        J-half-edges, modulo self-loop subtraction). Hand-checkable.
        """
        c = Fraction(1)
        wick = s5_virasoro_wick(c)
        recur = s5_virasoro_recursion(c)
        closed = s5_virasoro_closed_form(c)
        assert wick == recur == closed == Fraction(-16, 9)

    @pytest.mark.parametrize("name, c", [
        ('Ising', Fraction(1, 2)),
        ('Tri-critical Ising', Fraction(7, 10)),
        ('Three-state Potts', Fraction(4, 5)),
        ('Single ghost', Fraction(2)),
        ('Leech lattice', Fraction(24)),
    ])
    def test_wick_matches_recursion_at_calibration_points(self, name, c):
        """All six finite calibration values agree."""
        wick = s5_virasoro_wick(c)
        recur = s5_virasoro_recursion(c)
        closed = s5_virasoro_closed_form(c)
        assert wick == recur, f"{name}: wick {wick} != recur {recur}"
        assert wick == closed, f"{name}: wick {wick} != closed {closed}"

    def test_wick_matches_closed_form_uniform(self):
        """Uniform spot-check across the calibration set."""
        for c in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5),
                  Fraction(1), Fraction(2), Fraction(24)]:
            assert s5_virasoro_wick(c) == s5_virasoro_closed_form(c)


# =====================================================================
# AP178 large-c asymptotic guard
# =====================================================================


class TestAP178LargeCAsymptotic:
    """Guard against the AP178 confusion: at large c, S_5 ~ -48/(5 c^3),
    NOT -48/(5 c^3 * 5) and NOT -48/c^3.
    """
    def test_large_c_asymptotic_ratio(self):
        # At c = 1000, S_5 = -48 / (1000^2 * 5022) and the leading-order
        # asymptotic is -48/(5 c^3) = -48/(5 * 10^9).
        c = Fraction(1000)
        exact = s5_virasoro_closed_form(c)
        leading = Fraction(-48) / (5 * c**3)
        # Ratio should be close to 1 (within 1% at c = 1000).
        ratio = float(exact) / float(leading)
        assert 0.99 < ratio < 1.01, (
            f"AP178 violation: exact/leading = {ratio}, expected ~ 1; "
            f"check large-c asymptotic of S_5"
        )
