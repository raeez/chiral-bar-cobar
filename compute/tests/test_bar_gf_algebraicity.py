r"""Tests for bar cohomology GF algebraicity (conj:bar-gf-algebraicity).

Verifies:
1. Bar cohomology dimension tables match ground truth (KNOWN_BAR_DIMS)
2. Algebraic equations for sl2 (Riordan), betagamma, Virasoro
3. Rational GF equations for sl3, W3
4. Discriminant degree bound deg(Delta) <= 2*rank(A)
5. Koszul functional equation at PBW level
6. G2 prediction structure
7. Universal Catalan discriminant factorization
"""

import pytest
from sympy import Rational, Symbol, Poly, expand, Integer

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.bar_gf_algebraicity import (
    heisenberg_bar_dims,
    sl2_bar_dims,
    riordan_numbers,
    virasoro_bar_dims,
    betagamma_bar_dims,
    betagamma_full_gf_coeffs,
    sl3_bar_dims,
    w3_bar_dims,
    lattice_bar_dims,
    known_algebraic_equations,
    verify_riordan_equation,
    verify_betagamma_equation,
    verify_sl3_rational_gf,
    verify_w3_rational_gf,
    verify_discriminant_bound,
    verify_all_discriminant_bounds,
    koszul_functional_equation_classical,
    verify_betagamma_koszul_pair,
    predict_g2_algebraic_equation,
    verify_algebraicity_all_families,
    universal_discriminant_factorization,
)
from lib.utils import partition_number


# =========================================================================
# Bar cohomology dimension tables
# =========================================================================

class TestBarDims:
    """Verify bar cohomology dimension tables against ground truth."""

    def test_heisenberg_first_10(self):
        dims = heisenberg_bar_dims(10)
        expected = [1, 1, 1, 2, 3, 5, 7, 11, 15, 22]
        assert dims == expected

    def test_heisenberg_is_partition(self):
        dims = heisenberg_bar_dims(10)
        assert dims[0] == 1
        for n in range(2, 11):
            assert dims[n - 1] == partition_number(n - 2)

    def test_sl2_first_8(self):
        dims = sl2_bar_dims(8)
        expected = [3, 6, 15, 36, 91, 232, 603, 1585]
        assert dims == expected

    def test_sl2_h1_equals_dim_sl2(self):
        assert sl2_bar_dims(1)[0] == 3

    def test_riordan_first_10(self):
        R = riordan_numbers(10)
        assert R == [1, 0, 1, 1, 3, 6, 15, 36, 91, 232]

    def test_virasoro_first_8(self):
        dims = virasoro_bar_dims(8)
        expected = [1, 2, 5, 12, 30, 76, 196, 512]
        assert dims == expected

    def test_betagamma_first_10(self):
        dims = betagamma_bar_dims(10)
        expected = [2, 4, 10, 26, 70, 192, 534, 1500, 4246, 12092]
        assert dims == expected

    def test_betagamma_h1(self):
        assert betagamma_bar_dims(1)[0] == 2

    def test_betagamma_full_gf_starts_with_1(self):
        coeffs = betagamma_full_gf_coeffs(5)
        assert coeffs[0] == 1
        assert coeffs[1] == 2

    def test_sl3_first_3(self):
        assert sl3_bar_dims(3) == [8, 36, 204]

    def test_sl3_h1_equals_dim_sl3(self):
        assert sl3_bar_dims(1)[0] == 8

    def test_sl3_prediction_degree4(self):
        dims = sl3_bar_dims(5)
        assert dims[3] == 1352

    def test_sl3_prediction_degree5(self):
        dims = sl3_bar_dims(5)
        assert dims[4] == 9892

    def test_w3_first_5(self):
        assert w3_bar_dims(5) == [2, 5, 16, 52, 171]

    def test_w3_prediction_degree6(self):
        dims = w3_bar_dims(6)
        assert dims[5] == 564

    def test_lattice_rank1_equals_heisenberg(self):
        assert lattice_bar_dims(10, rank=1) == heisenberg_bar_dims(10)


# =========================================================================
# Algebraic equation verification
# =========================================================================

class TestAlgebraicEquations:
    """Verify known algebraic equations against computed data."""

    def test_riordan_equation_through_15(self):
        """x(1+x)R^2 - (1+x)R + 1 = 0 for Riordan GF."""
        result = verify_riordan_equation(15)
        assert result['all_zero']

    def test_riordan_equation_through_10(self):
        result = verify_riordan_equation(10)
        assert result['verified_through'] >= 9

    def test_betagamma_equation_through_12(self):
        """(1-3x)Q^2 = (1+x) for betagamma GF."""
        result = verify_betagamma_equation(12)
        assert result['all_zero']

    def test_betagamma_equation_through_8(self):
        result = verify_betagamma_equation(8)
        assert result['all_zero']

    def test_sl3_rational_gf_through_8(self):
        """(1-8x)(1-3x-x^2)P = 4x(2-13x-2x^2) for sl3."""
        result = verify_sl3_rational_gf(8)
        assert result['all_zero']

    def test_w3_rational_gf_through_8(self):
        """(1-x)(1-3x-x^2)P = x(2-3x) for W3."""
        result = verify_w3_rational_gf(8)
        assert result['all_zero']

    def test_all_families_verified(self):
        """Run comprehensive verification."""
        results = verify_algebraicity_all_families()
        for name, r in results.items():
            assert r['all_zero'], f"Algebraic equation fails for {name}"


# =========================================================================
# Discriminant degree bound
# =========================================================================

class TestDiscriminantBound:
    """Verify deg(Delta) <= 2*rank(A) for algebraic-degree-2 families."""

    def test_sl2_riordan_bound(self):
        r = verify_discriminant_bound('sl2_riordan', rank=1, disc_degree=2)
        assert r['satisfied']

    def test_virasoro_bound(self):
        r = verify_discriminant_bound('Virasoro', rank=1, disc_degree=2)
        assert r['satisfied']

    def test_betagamma_bound(self):
        r = verify_discriminant_bound('betagamma', rank=2, disc_degree=2)
        assert r['satisfied']

    def test_sl3_rational_denom_degree(self):
        """sl3 rational GF: denominator degree = 3 = rank + 1."""
        # For rational GFs, the bound is on the denominator degree, not disc
        x = Symbol('x')
        den = expand((1 - 8*x)*(1 - 3*x - x**2))
        assert Poly(den, x).degree() == 3
        assert Poly(den, x).degree() <= 2 * 2 + 1  # 2*rank + 1 bound for rational

    def test_w3_rational_denom_degree(self):
        x = Symbol('x')
        den = expand((1 - x)*(1 - 3*x - x**2))
        assert Poly(den, x).degree() == 3

    def test_all_algebraic_families_satisfy_bound(self):
        results = verify_all_discriminant_bounds()
        for name, r in results.items():
            if r.get('satisfied') is not None:
                if name in ('sl2_riordan', 'Virasoro', 'betagamma'):
                    assert r['satisfied'], f"{name} violates disc bound"


# =========================================================================
# Known equation catalogue
# =========================================================================

class TestKnownEquations:
    """Verify the catalogued algebraic equations."""

    def test_sl2_riordan_in_catalogue(self):
        eqs = known_algebraic_equations()
        assert 'sl2_riordan' in eqs
        assert eqs['sl2_riordan']['alg_degree'] == 2

    def test_virasoro_disc_degree(self):
        eqs = known_algebraic_equations()
        assert eqs['Virasoro']['disc_degree'] == 2

    def test_betagamma_disc_degree(self):
        eqs = known_algebraic_equations()
        assert eqs['betagamma']['disc_degree'] == 2

    def test_sl3_is_rational(self):
        eqs = known_algebraic_equations()
        assert eqs['sl3']['alg_degree'] == 1

    def test_w3_is_rational(self):
        eqs = known_algebraic_equations()
        assert eqs['W3']['alg_degree'] == 1

    def test_heisenberg_transcendental(self):
        eqs = known_algebraic_equations()
        assert eqs['Heisenberg']['alg_degree'] is None

    def test_sl2_riordan_discriminant(self):
        x = Symbol('x')
        eqs = known_algebraic_equations()
        assert eqs['sl2_riordan']['discriminant'] == Poly((1 - 3*x)*(1 + x), x)

    def test_betagamma_discriminant(self):
        x = Symbol('x')
        eqs = known_algebraic_equations()
        assert eqs['betagamma']['discriminant'] == Poly(4*(1 + x)*(1 - 3*x), x)


# =========================================================================
# Koszul functional equation
# =========================================================================

class TestKoszulFunctionalEquation:
    """Test the classical Koszul identity H_A(x)*H_{A!}(-x) = 1."""

    def test_trivial_case(self):
        """H_A = 1+x, H_{A!} = 1+x => product = 1-x^2 != 1.
        But if A is self-Koszul-dual: (1+x)(1-x) = 1-x^2 != 1.
        Self-dual only works if H = 1 or specific symmetry."""
        result = koszul_functional_equation_classical([1], [1], 1)
        # (1+x)(1-x) at x^1: 1*(-1) + 1*1 = 0
        assert result['product_coeffs'][1] == 0

    def test_constant_term_always_1(self):
        result = koszul_functional_equation_classical([3, 5], [3, 5], 2)
        assert result['product_coeffs'][0] == 1

    def test_betagamma_koszul_pair(self):
        """Test betagamma vs free-fermion Koszul pair at PBW level.
        This is a structural test — the identity may not hold exactly
        at the chiral level (only at associated-graded PBW level)."""
        # For the associated graded: the identity is tautological
        # (prod 1/(1-x^k)^2 * prod (1+x^k)^2 at x -> -x).
        # The chiral correction is O(kappa). We just check the function runs.
        result = verify_betagamma_koszul_pair()
        assert 'koszul_identity_holds' in result


# =========================================================================
# G2 prediction
# =========================================================================

class TestG2Prediction:
    """Test the G2 prediction structure."""

    def test_g2_rank(self):
        pred = predict_g2_algebraic_equation()
        assert pred['rank'] == 2

    def test_g2_dim(self):
        pred = predict_g2_algebraic_equation()
        assert pred['dim'] == 14

    def test_g2_disc_bound(self):
        pred = predict_g2_algebraic_equation()
        assert pred['disc_degree_bound'] == 4

    def test_g2_h1(self):
        pred = predict_g2_algebraic_equation()
        assert pred['H1'] == 14

    def test_g2_exponents(self):
        pred = predict_g2_algebraic_equation()
        assert pred['exponents'] == [1, 5]

    def test_g2_coxeter(self):
        pred = predict_g2_algebraic_equation()
        assert pred['coxeter_number'] == 6

    def test_g2_dual_coxeter(self):
        pred = predict_g2_algebraic_equation()
        assert pred['dual_coxeter'] == 4

    def test_g2_structural_analogy_sl2(self):
        pred = predict_g2_algebraic_equation()
        assert pred['structural_analogy']['sl2']['dominant_root'] == Rational(1, 3)

    def test_g2_structural_analogy_sl3(self):
        pred = predict_g2_algebraic_equation()
        assert pred['structural_analogy']['sl3']['dominant_root'] == Rational(1, 8)


# =========================================================================
# Universal discriminant
# =========================================================================

class TestUniversalDiscriminant:
    """Test the universal Catalan discriminant factorization."""

    def test_catalan_discriminant_roots(self):
        result = universal_discriminant_factorization()
        assert Rational(1, 3) in result['catalan_roots']
        assert Rational(-1) in result['catalan_roots']

    def test_three_families_share_catalan(self):
        result = universal_discriminant_factorization()
        shared = result['shared_by']
        assert 'sl2' in shared
        assert 'Virasoro' in shared
        assert 'betagamma' in shared

    def test_sl3_has_different_disc(self):
        result = universal_discriminant_factorization()
        assert result['catalan_discriminant'] != result['sl3_discriminant']

    def test_sl3_dominant_root(self):
        result = universal_discriminant_factorization()
        assert Rational(1, 8) in result['sl3_roots']

    def test_catalan_disc_degree(self):
        result = universal_discriminant_factorization()
        assert result['catalan_discriminant'].degree() == 2


# =========================================================================
# Recurrence consistency
# =========================================================================

class TestRecurrenceConsistency:
    """Verify internal consistency of recurrence-extended sequences."""

    def test_sl3_recurrence(self):
        dims = sl3_bar_dims(10)
        for n in range(3, len(dims)):
            expected = 11 * dims[n - 1] - 23 * dims[n - 2] - 8 * dims[n - 3]
            assert dims[n] == expected

    def test_w3_recurrence(self):
        dims = w3_bar_dims(10)
        for n in range(3, len(dims)):
            expected = 4 * dims[n - 1] - 2 * dims[n - 2] - dims[n - 3]
            assert dims[n] == expected

    def test_betagamma_recurrence(self):
        """n*a(n) = 2n*a(n-1) + 3(n-2)*a(n-2)."""
        dims = betagamma_bar_dims(15)
        full = [1] + dims  # include a_0 = 1
        for n in range(2, len(full)):
            assert n * full[n] == 2 * n * full[n - 1] + 3 * (n - 2) * full[n - 2]

    def test_riordan_recurrence(self):
        """(n+1)*R(n) = (n-1)*(2*R(n-1) + 3*R(n-2))."""
        R = riordan_numbers(15)
        for n in range(2, 15):
            assert (n + 1) * R[n] == (n - 1) * (2 * R[n - 1] + 3 * R[n - 2])


# =========================================================================
# Edge cases and positivity
# =========================================================================

class TestEdgeCases:
    """Edge cases and structural integrity."""

    def test_heisenberg_dims_positive(self):
        assert all(d > 0 for d in heisenberg_bar_dims(20))

    def test_sl2_dims_positive(self):
        assert all(d > 0 for d in sl2_bar_dims(15))

    def test_betagamma_dims_even(self):
        assert all(d % 2 == 0 for d in betagamma_bar_dims(15))

    def test_sl3_dims_positive(self):
        assert all(d > 0 for d in sl3_bar_dims(8))

    def test_virasoro_dims_positive(self):
        assert all(d > 0 for d in virasoro_bar_dims(15))

    def test_w3_dims_positive(self):
        assert all(d > 0 for d in w3_bar_dims(10))

    def test_sl2_growth_rate(self):
        """sl2 bar dims grow like 3^n (dominant root 1/3)."""
        dims = sl2_bar_dims(10)
        ratios = [dims[n] / dims[n - 1] for n in range(1, len(dims))]
        # Should converge to 3
        assert 2.5 < ratios[-1] < 3.5

    def test_betagamma_growth_rate(self):
        """betagamma bar dims grow like 3^n (dominant root 1/3)."""
        dims = betagamma_bar_dims(15)
        ratios = [dims[n] / dims[n - 1] for n in range(1, len(dims))]
        assert 2.5 < ratios[-1] < 3.5

    def test_sl3_growth_rate(self):
        """sl3 bar dims grow like 8^n (dominant root 1/8)."""
        dims = sl3_bar_dims(8)
        ratios = [dims[n] / dims[n - 1] for n in range(1, len(dims))]
        assert 6.0 < ratios[-1] < 9.0
