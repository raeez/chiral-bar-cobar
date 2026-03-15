"""Tests for KM bar differential (bracket + curvature).

Key findings verified here:
1. Adjacent-pair bar differential has d² ≠ 0 (Lie bracket not associative)
2. The residual d_br² + d_curv is proportional to (k - 2) for sl₂
3. CE differential d_CE² = 0 (Jacobi identity)
4. Curvature contraction d_ω² = 0 (degree argument)
5. Anticommutator {d_CE, d_ω} ∝ k (the curvature = curved A∞ obstruction)
"""

import pytest
from sympy import Symbol, simplify, Rational


k = Symbol('k')


class TestAdjacentPairBracket:
    """Adjacent-pair bar differential d_bracket."""

    def test_sl2_deg2_shape(self):
        from compute.lib.km_bar_differential import bar_diff_bracket_adjacent
        from compute.lib.chiral_bar import sl2_structure_constants
        d = bar_diff_bracket_adjacent(3, sl2_structure_constants(), 2)
        assert d.shape == (3, 9)

    def test_sl2_deg3_shape(self):
        from compute.lib.km_bar_differential import bar_diff_bracket_adjacent
        from compute.lib.chiral_bar import sl2_structure_constants
        d = bar_diff_bracket_adjacent(3, sl2_structure_constants(), 3)
        assert d.shape == (9, 27)

    def test_sl2_d_squared_not_zero(self):
        """d_bracket² ≠ 0 for adjacent-pair bar (Lie not associative)."""
        from compute.lib.km_bar_differential import bar_diff_bracket_adjacent
        from compute.lib.chiral_bar import sl2_structure_constants
        sc = sl2_structure_constants()
        d3 = bar_diff_bracket_adjacent(3, sc, 3)
        d2 = bar_diff_bracket_adjacent(3, sc, 2)
        d_sq = d2 * d3
        assert not d_sq.is_zero_matrix


class TestAdjacentPairCurvature:
    """Adjacent-pair curvature differential."""

    def test_sl2_deg2_shape(self):
        from compute.lib.km_bar_differential import bar_diff_curvature_adjacent
        from compute.lib.chiral_bar import sl2_killing
        d = bar_diff_curvature_adjacent(3, sl2_killing(), 2, k)
        assert d.shape == (1, 9)

    def test_sl2_deg3_shape(self):
        from compute.lib.km_bar_differential import bar_diff_curvature_adjacent
        from compute.lib.chiral_bar import sl2_killing
        d = bar_diff_curvature_adjacent(3, sl2_killing(), 3, k)
        assert d.shape == (3, 27)

    def test_sl2_curvature_residual(self):
        """d_br² + d_curv ∝ (k-2) for sl₂ adjacent-pair bar."""
        from compute.lib.km_bar_differential import (
            bar_diff_bracket_adjacent, bar_diff_curvature_adjacent
        )
        from compute.lib.chiral_bar import sl2_structure_constants, sl2_killing
        sc = sl2_structure_constants()
        kf = sl2_killing()
        d3_br = bar_diff_bracket_adjacent(3, sc, 3)
        d2_br = bar_diff_bracket_adjacent(3, sc, 2)
        d3_curv = bar_diff_curvature_adjacent(3, kf, 3, k)
        residual = d2_br * d3_br + d3_curv
        # Every nonzero entry should be proportional to (k-2)
        for i in range(residual.rows):
            for j in range(residual.cols):
                val = simplify(residual[i, j])
                if val != 0:
                    # Substitute k=2: should give 0
                    assert val.subs(k, 2) == 0, f"[{i},{j}]={val} not zero at k=2"


class TestCurvedCE:
    """Curved CE complex analysis."""

    def test_ce_squared_zero(self):
        """d_CE² = 0 at all degrees (Jacobi)."""
        from compute.lib.spectral_sequence import curved_ce_d_squared
        from compute.lib.chiral_bar import sl2_structure_constants, sl2_killing
        sc = sl2_structure_constants()
        kf = sl2_killing()
        for deg in range(5):
            result = curved_ce_d_squared(3, sc, kf, deg, k)
            assert result["ce_squared_zero"], f"d_CE² ≠ 0 at degree {deg}"

    def test_omega_squared_zero(self):
        """d_ω² = 0 at all degrees."""
        from compute.lib.spectral_sequence import curved_ce_d_squared
        from compute.lib.chiral_bar import sl2_structure_constants, sl2_killing
        sc = sl2_structure_constants()
        kf = sl2_killing()
        for deg in range(5):
            result = curved_ce_d_squared(3, sc, kf, deg, k)
            assert result["omega_squared_zero"], f"d_ω² ≠ 0 at degree {deg}"

    def test_anticommutator_is_curvature(self):
        """{d_CE, d_ω} is proportional to k (the curvature)."""
        from compute.lib.spectral_sequence import curved_ce_d_squared
        from compute.lib.chiral_bar import sl2_structure_constants, sl2_killing
        sc = sl2_structure_constants()
        kf = sl2_killing()
        for deg in [1, 3]:  # nonzero degrees
            result = curved_ce_d_squared(3, sc, kf, deg, k)
            assert not result["anticommutator_zero"]
            anticomm = result["anticommutator"]
            # At k=0: no central extension, should vanish
            for i in range(anticomm.rows):
                for j in range(anticomm.cols):
                    assert simplify(anticomm[i, j].subs(k, 0)) == 0

    def test_anticommutator_zero_at_even_degrees(self):
        """{d_CE, d_ω} = 0 at degrees 0, 2, 4 for sl₂."""
        from compute.lib.spectral_sequence import curved_ce_d_squared
        from compute.lib.chiral_bar import sl2_structure_constants, sl2_killing
        sc = sl2_structure_constants()
        kf = sl2_killing()
        for deg in [0, 2, 4]:
            result = curved_ce_d_squared(3, sc, kf, deg, k)
            assert result["anticommutator_zero"]


class TestCurvatureContraction:
    """Curvature contraction matrix."""

    def test_sl2_deg2(self):
        """d_ω at degree 2: Λ²(sl₂*) → Λ⁰ = k."""
        from compute.lib.spectral_sequence import curvature_contraction_matrix
        from compute.lib.chiral_bar import sl2_killing
        d = curvature_contraction_matrix(3, sl2_killing(), 2, k)
        assert d.shape == (1, 3)
        # Killing form: κ(e,f)=1, κ(f,e)=1, κ(h,h)=2
        # Basis of Λ²: (0,1)=e∧h, (0,2)=e∧f, (1,2)=h∧f
        # d_ω(e∧f) = (-1)^{0+1} k·κ(e,f) = -k
        # Actually sign is (-1)^{a_pos + b_pos} = (-1)^{0+1} = -1
        # d_ω(e∧h) = k·κ(e,h) = 0
        # d_ω(h∧f) = (-1)^{0+1} k·κ(h,f) = 0
        assert d[0, 0] == 0  # e∧h
        assert simplify(d[0, 1] + k) == 0  # e∧f: -k
        assert d[0, 2] == 0  # h∧f

    def test_sl2_deg3(self):
        """d_ω at degree 3: Λ³ → Λ¹."""
        from compute.lib.spectral_sequence import curvature_contraction_matrix
        from compute.lib.chiral_bar import sl2_killing
        d = curvature_contraction_matrix(3, sl2_killing(), 3, k)
        assert d.shape == (3, 1)
        # Only basis of Λ³: (0,1,2) = e∧h∧f
        # Pairs: (e,h) pos (0,1) κ=0, (e,f) pos (0,2) κ=1, (h,f) pos (1,2) κ=0
        # d_ω(e∧h∧f) from pair (e,f): (-1)^{0+2} k·1 · h = k·h
        # h is basis index 1
        assert simplify(d[1, 0] - k) == 0  # coefficient of h = k
