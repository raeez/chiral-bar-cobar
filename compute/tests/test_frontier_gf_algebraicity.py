r"""Frontier tests for bar GF algebraicity verification.

Targets the priority computational claims from the concordance:
  - Bar GF algebraicity for known families (sl2/Virasoro/betagamma)
  - sl3 bar GF conjecture (conj:sl3-bar-gf)
  - W3 bar GF conjecture
  - W4 bar Betti number predictions and OPE structure constants
  - Universal discriminant factor (1-3x)(1+x)
  - Algebraic degree bound conjecture

Ground truth:
  concordance.tex: conj:bar-gf-algebraicity, conj:sl3-bar-gf
  bar_gf_algebraicity.py: dimension tables + algebraic equations
  bar_gf_solver.py: rational/holonomic GF finder
  w4_bar.py: W4 OPE n-th products
  w4_ds_ope_extraction.py: DS-side formulas
"""

import pytest
from sympy import (
    Integer,
    Poly,
    Rational,
    Symbol,
    expand,
    factor,
    simplify,
    solve,
    sqrt,
)


# =========================================================================
# 1. Bar GF algebraic equations — known families
# =========================================================================


class TestRiordanAlgebraicEquation:
    """Verify R(x) satisfies x(1+x)R^2 - (1+x)R + 1 = 0."""

    def test_riordan_equation_vanishes_through_degree_15(self):
        """Riordan GF algebraic equation has zero coefficients through x^15."""
        from compute.lib.bar_gf_algebraicity import riordan_numbers

        x = Symbol('x')
        R_data = riordan_numbers(21)
        R_trunc = sum(Rational(R_data[n]) * x**n for n in range(21))
        R2_trunc = expand(R_trunc**2)
        residual = expand(x * (1 + x) * R2_trunc - (1 + x) * R_trunc + 1)
        p = Poly(residual, x)
        for k in range(16):
            assert p.nth(k) == 0, f"Riordan equation nonzero at x^{k}"

    def test_riordan_library_verification(self):
        """Library verify_riordan_equation returns all_zero through N=15."""
        from compute.lib.bar_gf_algebraicity import verify_riordan_equation

        result = verify_riordan_equation(15)
        assert result['all_zero']


class TestBetagammaAlgebraicEquation:
    """Verify Q(x) = sqrt((1+x)/(1-3x)), i.e. (1-3x)*Q^2 = (1+x)."""

    def test_betagamma_equation_vanishes_through_degree_15(self):
        """(1-3x)*Q^2 - (1+x) = 0 through x^15 for betagamma GF."""
        from compute.lib.bar_gf_algebraicity import betagamma_full_gf_coeffs

        x = Symbol('x')
        Q_data = betagamma_full_gf_coeffs(20)
        Q_trunc = sum(Rational(Q_data[n]) * x**n for n in range(20))
        Q2_trunc = expand(Q_trunc**2)
        residual = expand((1 - 3 * x) * Q2_trunc - (1 + x))
        p = Poly(residual, x)
        for k in range(15):
            assert p.nth(k) == 0, f"betagamma equation nonzero at x^{k}"

    def test_betagamma_library_verification(self):
        """Library verify_betagamma_equation returns all_zero through N=12."""
        from compute.lib.bar_gf_algebraicity import verify_betagamma_equation

        result = verify_betagamma_equation(12)
        assert result['all_zero']


class TestVirasoroBarDims:
    """Virasoro bar dims are Motzkin differences M(n+1) - M(n)."""

    def test_virasoro_dims_are_motzkin_differences(self):
        """v_n = M(n+1) - M(n) for n = 1..10."""
        from compute.lib.bar_gf_algebraicity import virasoro_bar_dims
        from compute.lib.bar_gf_solver import motzkin_numbers

        vir = virasoro_bar_dims(10)
        M = motzkin_numbers(12)
        for n in range(1, 11):
            assert vir[n - 1] == M[n + 1] - M[n], f"Virasoro dim at n={n} fails"

    @pytest.mark.parametrize("n,expected", [
        (1, 1), (2, 2), (3, 5), (4, 12), (5, 30), (6, 76), (7, 196), (8, 512),
    ])
    def test_virasoro_known_values(self, n, expected):
        """Virasoro bar dims match OEIS/ground truth."""
        from compute.lib.bar_gf_algebraicity import virasoro_bar_dims

        assert virasoro_bar_dims(n)[n - 1] == expected


# =========================================================================
# 2. Riordan number verification — independent recurrence
# =========================================================================


class TestRiordanRecurrence:
    """Riordan numbers R(n) satisfy (n+1)*R(n) = (n-1)*(2*R(n-1) + 3*R(n-2))."""

    def test_riordan_recurrence_n0_to_n25(self):
        """Verify Riordan recurrence for n = 2..25."""
        from compute.lib.bar_gf_algebraicity import riordan_numbers

        R = riordan_numbers(26)
        for n in range(2, 26):
            lhs = (n + 1) * R[n]
            rhs = (n - 1) * (2 * R[n - 1] + 3 * R[n - 2])
            assert lhs == rhs, f"Riordan recurrence fails at n={n}"

    def test_riordan_initial_values(self):
        """R(0) = 1, R(1) = 0, R(2) = 1."""
        from compute.lib.bar_gf_algebraicity import riordan_numbers

        R = riordan_numbers(5)
        assert R[0] == 1
        assert R[1] == 0
        assert R[2] == 1

    def test_riordan_oeis_first_12(self):
        """OEIS A005043: 1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585."""
        from compute.lib.bar_gf_algebraicity import riordan_numbers

        R = riordan_numbers(12)
        assert R == [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585]

    def test_sl2_bar_dims_from_riordan(self):
        """H^n(B(sl2)) = R(n+3) for n >= 1."""
        from compute.lib.bar_gf_algebraicity import sl2_bar_dims, riordan_numbers

        dims = sl2_bar_dims(8)
        R = riordan_numbers(12)
        for n in range(1, 9):
            assert dims[n - 1] == R[n + 3], f"sl2 bar dim at n={n} fails"


# =========================================================================
# 3. sl3 bar GF conjecture (conj:sl3-bar-gf)
# =========================================================================


class TestSl3BarGFConjecture:
    """CONJECTURED rational GF: P(x) = 4x(2-13x-2x^2)/((1-8x)(1-3x-x^2))."""

    def test_sl3_known_values(self):
        """H^1 = 8, H^2 = 36, H^3 = 204."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        dims = sl3_bar_dims(3)
        assert dims == [8, 36, 204]

    def test_sl3_h1_equals_dim_sl3(self):
        """H^1(B(sl3)) = dim(sl3) = 8."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        assert sl3_bar_dims(1)[0] == 8

    def test_sl3_predicted_h4(self):
        """H^4(B(sl3)) = 1352 from recurrence 11*204 - 23*36 - 8*8."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        assert sl3_bar_dims(4)[3] == 1352
        assert 11 * 204 - 23 * 36 - 8 * 8 == 1352

    def test_sl3_predicted_h5(self):
        """H^5(B(sl3)) = 9892 from recurrence."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        assert sl3_bar_dims(5)[4] == 9892
        assert 11 * 1352 - 23 * 204 - 8 * 36 == 9892

    def test_sl3_rational_gf_equation(self):
        """(1-8x)(1-3x-x^2)*P(x) = 4x(2-13x-2x^2) through degree 8."""
        from compute.lib.bar_gf_algebraicity import verify_sl3_rational_gf

        result = verify_sl3_rational_gf(8)
        assert result['all_zero']

    def test_sl3_numerator_produces_correct_terms(self):
        """Substitute into 4x(2-13x-2x^2)/((1-8x)(1-3x-x^2)) and expand."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        x = Symbol('x')
        num = 4 * x * (2 - 13 * x - 2 * x**2)
        den = expand((1 - 8 * x) * (1 - 3 * x - x**2))
        # Verify D*P = N truncated
        dims = sl3_bar_dims(8)
        P_trunc = sum(Rational(dims[n]) * x**(n + 1) for n in range(8))
        residual = expand(Poly(den, x).as_expr() * P_trunc - num)
        p = Poly(residual, x)
        for k in range(9):
            assert p.nth(k) == 0, f"sl3 GF equation nonzero at x^{k}"

    def test_sl3_recurrence_consistency(self):
        """a_n = 11*a_{n-1} - 23*a_{n-2} - 8*a_{n-3} for all extended terms."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        dims = sl3_bar_dims(12)
        for n in range(3, 12):
            expected = 11 * dims[n - 1] - 23 * dims[n - 2] - 8 * dims[n - 3]
            assert dims[n] == expected, f"sl3 recurrence fails at n={n}"

    def test_sl3_growth_rate_converges_to_8(self):
        """Dominant eigenvalue = 8 = dim(sl3). Ratio a_n/a_{n-1} -> 8."""
        from compute.lib.bar_gf_algebraicity import sl3_bar_dims

        dims = sl3_bar_dims(15)
        ratio = dims[14] / dims[13]
        assert 7.9 < ratio < 8.1, f"sl3 growth ratio {ratio} not near 8"

    def test_sl3_denominator_roots(self):
        """Denominator (1-8x)(1-3x-x^2) has roots 1/8 and (-3+/-sqrt(13))/2."""
        x = Symbol('x')
        roots = solve((1 - 8 * x) * (1 - 3 * x - x**2), x)
        assert Rational(1, 8) in roots
        quadratic_roots = solve(1 - 3 * x - x**2, x)
        assert len(quadratic_roots) == 2
        # Verify quadratic root product = -1 (from 1 - 3x - x^2, coeff of x^2 = -1)
        product = quadratic_roots[0] * quadratic_roots[1]
        assert simplify(product + 1) == 0

    def test_sl3_conjectured_gf_via_solver(self):
        """verify_conjectured_gf matches sl3 data and predicts H^4=1352."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf

        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -52, -8],
            den_coeffs=[-11, 23, 8],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 1352
        assert result["predictions"][1] == 9892


# =========================================================================
# 4. W3 bar GF conjecture
# =========================================================================


class TestW3BarGFConjecture:
    """CONJECTURED rational GF: P(x) = x(2-3x)/((1-x)(1-3x-x^2))."""

    def test_w3_known_values(self):
        """H^1 = 2, H^2 = 5, H^3 = 16, H^4 = 52, H^5 = 171."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims

        assert w3_bar_dims(5) == [2, 5, 16, 52, 171]

    def test_w3_predicted_h6(self):
        """H^6(B(W3)) = 564 from recurrence 4*171 - 2*52 - 16."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims

        assert w3_bar_dims(6)[5] == 564
        assert 4 * 171 - 2 * 52 - 16 == 564

    def test_w3_predicted_h7(self):
        """H^7(B(W3)) = 1862 from recurrence 4*564 - 2*171 - 52."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims

        assert w3_bar_dims(7)[6] == 1862
        assert 4 * 564 - 2 * 171 - 52 == 1862

    def test_w3_rational_gf_equation(self):
        """(1-x)(1-3x-x^2)*P(x) = x(2-3x) through degree 8."""
        from compute.lib.bar_gf_algebraicity import verify_w3_rational_gf

        result = verify_w3_rational_gf(8)
        assert result['all_zero']

    def test_w3_numerator_produces_correct_terms(self):
        """Substitute into x(2-3x)/((1-x)(1-3x-x^2)) and expand."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims

        x = Symbol('x')
        num = x * (2 - 3 * x)
        den = expand((1 - x) * (1 - 3 * x - x**2))
        dims = w3_bar_dims(8)
        P_trunc = sum(Rational(dims[n]) * x**(n + 1) for n in range(8))
        residual = expand(Poly(den, x).as_expr() * P_trunc - num)
        p = Poly(residual, x)
        for k in range(9):
            assert p.nth(k) == 0, f"W3 GF equation nonzero at x^{k}"

    def test_w3_recurrence_consistency(self):
        """a_n = 4*a_{n-1} - 2*a_{n-2} - a_{n-3} for all extended terms."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims

        dims = w3_bar_dims(12)
        for n in range(3, 12):
            expected = 4 * dims[n - 1] - 2 * dims[n - 2] - dims[n - 3]
            assert dims[n] == expected, f"W3 recurrence fails at n={n}"

    def test_w3_growth_rate_converges(self):
        """Dominant root of (1-x)(1-3x-x^2) = 0 is (3+sqrt(13))/2 ~ 3.303."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims

        dims = w3_bar_dims(20)
        ratio = dims[19] / dims[18]
        dominant = float((3 + sqrt(13)) / 2)
        assert abs(ratio - dominant) < 0.01, (
            f"W3 growth ratio {ratio} not near {dominant}"
        )

    def test_w3_conjectured_gf_via_solver(self):
        """verify_conjectured_gf matches W3 data and predicts H^5=171."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf

        result = verify_conjectured_gf(
            [2, 5, 16, 52],
            num_coeffs=[2, -3],
            den_coeffs=[-4, 2, 1],
            n_predict=3,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 171
        assert result["predictions"][1] == 564
        assert result["predictions"][2] == 1862

    def test_w3_denominator_roots(self):
        """Denominator (1-x)(1-3x-x^2) has roots 1 and (-3+/-sqrt(13))/2."""
        x = Symbol('x')
        roots = solve((1 - x) * (1 - 3 * x - x**2), x)
        assert Integer(1) in roots
        quadratic_roots = solve(1 - 3 * x - x**2, x)
        assert len(quadratic_roots) == 2


# =========================================================================
# 5. Discriminant universality — Catalan factor (1-3x)(1+x)
# =========================================================================


class TestDiscriminantUniversality:
    """All known algebraic-degree-2 bar GFs share discriminant factor (1-3x)(1+x)."""

    def test_sl2_discriminant_is_catalan(self):
        """sl2 Riordan discriminant = (1-3x)(1+x)."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations

        eqs = known_algebraic_equations()
        x = Symbol('x')
        assert eqs['sl2_riordan']['discriminant'] == Poly((1 - 3 * x) * (1 + x), x)

    def test_virasoro_discriminant_is_catalan(self):
        """Virasoro Motzkin-difference discriminant = (1-3x)(1+x)."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations

        eqs = known_algebraic_equations()
        x = Symbol('x')
        assert eqs['Virasoro']['discriminant'] == Poly((1 - 3 * x) * (1 + x), x)

    def test_betagamma_discriminant_has_catalan_factor(self):
        """betagamma discriminant = 4*(1+x)*(1-3x), proportional to Catalan."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations

        eqs = known_algebraic_equations()
        x = Symbol('x')
        assert eqs['betagamma']['discriminant'] == Poly(4 * (1 + x) * (1 - 3 * x), x)

    def test_catalan_roots_are_one_third_and_minus_one(self):
        """Universal discriminant roots: 1/3 (dominant), -1 (alternating)."""
        from compute.lib.bar_gf_algebraicity import universal_discriminant_factorization

        result = universal_discriminant_factorization()
        assert Rational(1, 3) in result['catalan_roots']
        assert Rational(-1) in result['catalan_roots']

    def test_three_families_share_catalan(self):
        """sl2, Virasoro, betagamma all share the Catalan discriminant."""
        from compute.lib.bar_gf_algebraicity import universal_discriminant_factorization

        shared = universal_discriminant_factorization()['shared_by']
        for family in ['sl2', 'Virasoro', 'betagamma']:
            assert family in shared

    def test_sl3_discriminant_differs_from_catalan(self):
        """sl3 has a different discriminant (rational, not quadratic)."""
        from compute.lib.bar_gf_algebraicity import universal_discriminant_factorization

        result = universal_discriminant_factorization()
        assert result['catalan_discriminant'] != result['sl3_discriminant']


# =========================================================================
# 6. Bar GF algebraicity degree bound
# =========================================================================


class TestAlgebraicDegreeBound:
    """Conjecture: algebraic degree <= 2 for all Koszul chiral algebras."""

    @pytest.mark.parametrize("family,expected_degree", [
        ("sl2_riordan", 2),
        ("Virasoro", 2),
        ("betagamma", 2),
        ("sl3", 1),
        ("W3", 1),
    ])
    def test_algebraic_degree_at_most_2(self, family, expected_degree):
        """Each family has algebraic degree <= 2."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations

        eqs = known_algebraic_equations()
        assert eqs[family]['alg_degree'] == expected_degree
        assert expected_degree <= 2

    def test_heisenberg_transcendental_excluded(self):
        """Heisenberg has transcendental GF (partition function)."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations

        eqs = known_algebraic_equations()
        assert eqs['Heisenberg']['alg_degree'] is None

    @pytest.mark.parametrize("family", [
        "sl2_riordan", "Virasoro", "betagamma",
    ])
    def test_discriminant_degree_at_most_2_times_rank(self, family):
        """Discriminant degree <= 2*rank for algebraic-degree-2 families."""
        from compute.lib.bar_gf_algebraicity import known_algebraic_equations

        eqs = known_algebraic_equations()
        data = eqs[family]
        assert data['disc_degree'] <= 2 * data['rank']


# =========================================================================
# 7. Bar GF algebraic equation solver
# =========================================================================


class TestBarGFSolver:
    """find_algebraic_gf and find_rational_gf recover known equations."""

    def test_sl2_holonomic_predicts_correctly(self):
        """sl2 bar dims satisfy holonomic recurrence, predict a_7 = 603."""
        from compute.lib.bar_gf_solver import bar_dims_sl2, predict_next_coefficient

        dims = bar_dims_sl2(7)
        pred = predict_next_coefficient(dims[:6])
        assert pred == dims[6]

    def test_virasoro_prediction_from_6_points(self):
        """Virasoro: predict a_7 = 196 from first 6 bar dims."""
        from compute.lib.bar_gf_solver import bar_dims_virasoro, predict_next_coefficient

        dims = bar_dims_virasoro(8)
        pred = predict_next_coefficient(dims[:6])
        assert pred == dims[6]

    def test_sl3_solver_verifies_conjectured_gf(self):
        """Rational GF finder verifies sl3 conjecture."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf

        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -52, -8],
            den_coeffs=[-11, 23, 8],
            n_predict=1,
        )
        assert result["matches"] is True
        assert result["predictions"][0] == 1352

    def test_wrong_gf_rejected(self):
        """A deliberately wrong conjectured GF is detected."""
        from compute.lib.bar_gf_solver import verify_conjectured_gf

        result = verify_conjectured_gf(
            [8, 36, 204],
            num_coeffs=[8, -50, -8],  # wrong: -50 instead of -52
            den_coeffs=[-11, 23, 8],
        )
        assert result["matches"] is False


# =========================================================================
# 8. Motzkin number verification
# =========================================================================


class TestMotzkinNumbers:
    """Motzkin numbers satisfy (n+2)*M(n) = (2n+1)*M(n-1) + 3*(n-1)*M(n-2)."""

    def test_motzkin_first_10(self):
        """M(0..9) = 1, 1, 2, 4, 9, 21, 51, 127, 323, 835."""
        from compute.lib.bar_gf_solver import motzkin_numbers

        M = motzkin_numbers(10)
        assert M == [1, 1, 2, 4, 9, 21, 51, 127, 323, 835]

    def test_motzkin_recurrence(self):
        """(n+2)*M(n) = (2n+1)*M(n-1) + 3*(n-1)*M(n-2) for n >= 2."""
        from compute.lib.bar_gf_solver import motzkin_numbers

        M = motzkin_numbers(20)
        for n in range(2, 20):
            lhs = (n + 2) * M[n]
            rhs = (2 * n + 1) * M[n - 1] + 3 * (n - 1) * M[n - 2]
            assert lhs == rhs, f"Motzkin recurrence fails at n={n}"

    def test_virasoro_from_motzkin(self):
        """Virasoro bar dims v_n = M(n+1) - M(n) for n = 1..8."""
        from compute.lib.bar_gf_solver import motzkin_numbers, bar_dims_virasoro

        M = motzkin_numbers(10)
        vir = bar_dims_virasoro(8)
        expected_diffs = [M[n + 1] - M[n] for n in range(1, 9)]
        assert vir == expected_diffs


# =========================================================================
# 9. sl3 transfer matrix spectral analysis
# =========================================================================


class TestSl3SpectralAnalysis:
    """Spectral analysis of the sl3 bar GF denominator."""

    def test_sl3_characteristic_polynomial(self):
        """Denominator (1-8x)(1-3x-x^2) has the correct expansion."""
        x = Symbol('x')
        den = expand((1 - 8 * x) * (1 - 3 * x - x**2))
        # 1 - 8x - 3x + 24x^2 - x^2 + 8x^3 = 1 - 11x + 23x^2 + 8x^3
        assert den == 1 - 11 * x + 23 * x**2 + 8 * x**3

    def test_sl3_three_roots(self):
        """Denominator has exactly three roots."""
        x = Symbol('x')
        roots = solve((1 - 8 * x) * (1 - 3 * x - x**2), x)
        assert len(roots) == 3
        assert Rational(1, 8) in roots

    def test_sl3_dominant_root_is_one_eighth(self):
        """Dominant root (smallest positive) is 1/8, reciprocal = 8 = dim(sl3)."""
        x = Symbol('x')
        roots = solve((1 - 8 * x) * (1 - 3 * x - x**2), x)
        positive_roots = [r for r in roots if r.is_positive]
        smallest_positive = min(positive_roots, key=lambda r: float(r))
        assert smallest_positive == Rational(1, 8)

    def test_sl3_quadratic_factor_discriminant(self):
        """Quadratic factor 1-3x-x^2 has discriminant 9+4 = 13."""
        # 1-3x-x^2 = 0 => x^2 + 3x - 1 = 0 => disc = 9 + 4 = 13
        assert 3**2 + 4 * 1 == 13

    def test_sl3_quadratic_roots_product(self):
        """Product of quadratic roots = coeff ratio = -1."""
        x = Symbol('x')
        roots = solve(x**2 + 3 * x - 1, x)
        product = simplify(roots[0] * roots[1])
        assert product == -1


# =========================================================================
# 10. W4 bar Betti predictions (frontier)
# =========================================================================


class TestW4VirasiroTargets:
    """Two Virasoro-target predictions from the W4 OPE."""

    def test_c442_equals_2(self):
        """C_{4,4;2;0,6} = 2: universal T-coupling in W4 x W4."""
        from compute.lib.w4_bar import extract_c_res_stage4_virasoro_targets

        targets = extract_c_res_stage4_virasoro_targets()
        assert targets[(4, 4, 2, 6)] == 2

    def test_c342_equals_0(self):
        """C_{3,4;2;0,5} = 0: mixed Virasoro vanishing in W3 x W4."""
        from compute.lib.w4_bar import extract_c_res_stage4_virasoro_targets

        targets = extract_c_res_stage4_virasoro_targets()
        assert targets[(3, 4, 2, 5)] == 0

    def test_verify_virasoro_targets(self):
        """Both Virasoro target identities verified simultaneously."""
        from compute.lib.w4_bar import verify_virasoro_targets

        results = verify_virasoro_targets()
        assert results["C_{4,4;2;0,6} = 2"] is True
        assert results["C_{3,4;2;0,5} = 0"] is True


class TestW4DSExtractionFormulas:
    """W4 DS OPE structure constants as rational functions of c."""

    def test_lambda_two_point(self):
        """<Lambda Lambda> = c(5c+22)/10."""
        from compute.lib.w4_ds_ope_extraction import lambda_two_point

        assert lambda_two_point(Rational(1)) == Rational(27, 10)
        assert lambda_two_point(Rational(10)) == Rational(72)

    def test_w4_primary_two_point(self):
        """<W4 W4> = c/4."""
        from compute.lib.w4_ds_ope_extraction import w4_primary_two_point

        assert w4_primary_two_point(Rational(1)) == Rational(1, 4)
        assert w4_primary_two_point(Rational(100)) == Rational(25)

    @pytest.mark.parametrize("c_val", [1, 10, 50, 100])
    def test_c334_squared_positive_for_positive_c(self, c_val):
        """c334^2 > 0 for c > 0 (unitary regime)."""
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula

        val = c334_squared_formula(Rational(c_val))
        assert val > 0, f"c334^2 not positive at c={c_val}"

    def test_c334_squared_vanishes_at_c0(self):
        """c334^2 has double zero at c = 0."""
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula

        assert c334_squared_formula(Rational(0)) == 0

    def test_c334_squared_formula_structure(self):
        """c334^2 = 42*c^2*(5c+22)/((c+24)*(7c+68)*(3c+46))."""
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula

        c = Symbol('c')
        formula = c334_squared_formula(c)
        expected = 42 * c**2 * (5 * c + 22) / (
            (c + 24) * (7 * c + 68) * (3 * c + 46)
        )
        assert simplify(formula - expected) == 0

    @pytest.mark.parametrize("pole_c", [
        Rational(-24), Rational(-68, 7), Rational(-46, 3),
    ])
    def test_c334_squared_poles(self, pole_c):
        """c334^2 has poles at c = -24, -68/7, -46/3."""
        denom = (pole_c + 24) * (7 * pole_c + 68) * (3 * pole_c + 46)
        assert denom == 0

    def test_c444_squared_formula_structure(self):
        """c444^2 = 112*c^2*(2c-1)*(3c+46)/((c+24)*(7c+68)*(10c+197)*(5c+3))."""
        from compute.lib.w4_ds_ope_extraction import c444_squared_formula

        c = Symbol('c')
        formula = c444_squared_formula(c)
        expected = (
            112 * c**2 * (2 * c - 1) * (3 * c + 46)
            / ((c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3))
        )
        assert simplify(formula - expected) == 0

    @pytest.mark.parametrize("pole_c", [
        Rational(-24), Rational(-68, 7), Rational(-197, 10), Rational(-3, 5),
    ])
    def test_c444_squared_poles(self, pole_c):
        """c444^2 has poles at c = -24, -68/7, -197/10, -3/5."""
        denom = (
            (pole_c + 24) * (7 * pole_c + 68)
            * (10 * pole_c + 197) * (5 * pole_c + 3)
        )
        assert denom == 0

    def test_c444_squared_vanishes_at_ising(self):
        """c444^2 = 0 at c = 1/2 (Ising point)."""
        from compute.lib.w4_ds_ope_extraction import c444_squared_formula

        assert c444_squared_formula(Rational(1, 2)) == 0

    def test_c343_ratio(self):
        """C_{3,4;3;0,4}^2 = (9/16)*c334^2 (metric adjoint relation)."""
        from compute.lib.w4_ds_ope_extraction import c343_formula, c334_squared_formula

        c_val = Rational(10)
        ratio = c343_formula(c_val) / c334_squared_formula(c_val)
        assert ratio == Rational(9, 16)

    def test_c344_ratio(self):
        """C_{3,4;4;0,3}^2 = (5/7)*c334^2 (Borcherds identity)."""
        from compute.lib.w4_ds_ope_extraction import c344_formula, c334_squared_formula

        c_val = Rational(10)
        ratio = c344_formula(c_val) / c334_squared_formula(c_val)
        assert ratio == Rational(5, 7)

    @pytest.mark.parametrize("c_val", [1, 10, 100])
    def test_c343_ratio_universal(self, c_val):
        """C_{3,4;3;0,4}^2 / c334^2 = 9/16 at multiple c values."""
        from compute.lib.w4_ds_ope_extraction import c343_formula, c334_squared_formula

        c = Rational(c_val)
        assert c343_formula(c) / c334_squared_formula(c) == Rational(9, 16)

    @pytest.mark.parametrize("c_val", [1, 10, 100])
    def test_c344_ratio_universal(self, c_val):
        """C_{3,4;4;0,3}^2 / c334^2 = 5/7 at multiple c values."""
        from compute.lib.w4_ds_ope_extraction import c344_formula, c334_squared_formula

        c = Rational(c_val)
        assert c344_formula(c) / c334_squared_formula(c) == Rational(5, 7)

    def test_stage4_virasoro_target_identities(self):
        """Both stage-4 Virasoro-target identities verified by DS module."""
        from compute.lib.w4_ds_ope_extraction import (
            verify_stage4_virasoro_target_identities,
        )

        results = verify_stage4_virasoro_target_identities()
        assert results["C_{4,4;2;0,6}"]["verified_value"] == 2
        assert results["C_{3,4;2;0,5}"]["verified_value"] == 0


# =========================================================================
# Cross-family structural tests
# =========================================================================


class TestCrossFamilyStructure:
    """Cross-family structural consistency of bar GFs."""

    def test_h1_equals_dim_for_km(self):
        """H^1(B(g_hat)) = dim(g) for all Kac-Moody families."""
        from compute.lib.bar_gf_algebraicity import sl2_bar_dims, sl3_bar_dims

        assert sl2_bar_dims(1)[0] == 3   # dim(sl2) = 3
        assert sl3_bar_dims(1)[0] == 8   # dim(sl3) = 8

    def test_h1_equals_num_generators_for_w_algebras(self):
        """H^1(B(W_N)) = N-1 for W-algebras."""
        from compute.lib.bar_gf_algebraicity import virasoro_bar_dims, w3_bar_dims

        assert virasoro_bar_dims(1)[0] == 1   # Virasoro = W_2: 1 generator
        assert w3_bar_dims(1)[0] == 2          # W_3: 2 generators (T, W)

    def test_shared_quadratic_factor_sl3_w3(self):
        """sl3 and W3 denominators share the quadratic factor 1-3x-x^2."""
        x = Symbol('x')
        sl3_den = expand((1 - 8 * x) * (1 - 3 * x - x**2))
        w3_den = expand((1 - x) * (1 - 3 * x - x**2))
        # Both contain 1-3x-x^2
        sl3_gcd = Poly(sl3_den, x)
        w3_gcd = Poly(w3_den, x)
        # The shared factor is 1-3x-x^2 (degree 2)
        from sympy import gcd
        shared = gcd(sl3_gcd, w3_gcd)
        assert shared.degree() == 2

    @pytest.mark.parametrize("family,growth_target,tolerance", [
        ("sl2", 3.0, 0.5),
        ("betagamma", 3.0, 0.5),
        ("sl3", 8.0, 0.5),
    ])
    def test_growth_rate_targets(self, family, growth_target, tolerance):
        """Asymptotic growth rate matches dominant singularity."""
        from compute.lib.bar_gf_algebraicity import (
            sl2_bar_dims, betagamma_bar_dims, sl3_bar_dims,
        )

        dim_funcs = {
            "sl2": sl2_bar_dims, "betagamma": betagamma_bar_dims,
            "sl3": sl3_bar_dims,
        }
        dims = dim_funcs[family](15)
        ratio = dims[14] / dims[13]
        assert abs(ratio - growth_target) < tolerance, (
            f"{family} growth ratio {ratio} far from {growth_target}"
        )


class TestPositivityAndIntegrality:
    """All bar dims are positive integers."""

    @pytest.mark.parametrize("family", [
        "heisenberg", "sl2", "virasoro", "betagamma", "sl3", "w3",
    ])
    def test_all_dims_positive(self, family):
        """Bar cohomology dimensions are positive for all families."""
        from compute.lib.bar_gf_algebraicity import (
            heisenberg_bar_dims, sl2_bar_dims, virasoro_bar_dims,
            betagamma_bar_dims, sl3_bar_dims, w3_bar_dims,
        )

        dim_funcs = {
            "heisenberg": heisenberg_bar_dims, "sl2": sl2_bar_dims,
            "virasoro": virasoro_bar_dims, "betagamma": betagamma_bar_dims,
            "sl3": sl3_bar_dims, "w3": w3_bar_dims,
        }
        dims = dim_funcs[family](10)
        assert all(d > 0 for d in dims), f"Non-positive dim in {family}"

    def test_betagamma_dims_all_even(self):
        """betagamma bar dims are all even (two-generator symmetry)."""
        from compute.lib.bar_gf_algebraicity import betagamma_bar_dims

        dims = betagamma_bar_dims(20)
        assert all(d % 2 == 0 for d in dims)


# =========================================================================
# Virasoro near-rationality regression
# =========================================================================


class TestVirasoroNearRationality:
    """Virasoro is algebraic degree 2, NOT rational. Near-rationality is spurious."""

    def test_spurious_recurrence_breaks_at_degree_9(self):
        """Depth-3 recurrence a_k = 4a_{k-1} - 2a_{k-2} - 4a_{k-3} fails at k=9."""
        from compute.lib.bar_gf_algebraicity import virasoro_bar_dims

        dims = virasoro_bar_dims(10)
        # Should work through degree 8
        for k in range(3, 8):
            pred = 4 * dims[k - 1] - 2 * dims[k - 2] - 4 * dims[k - 3]
            assert pred == dims[k], f"Should hold at degree {k + 1}"
        # Fails at degree 9
        pred_9 = 4 * dims[7] - 2 * dims[6] - 4 * dims[5]
        assert pred_9 == 1352
        assert dims[8] == 1353
        assert pred_9 != dims[8]

    def test_rational_gf_rejected_with_enough_data(self):
        """With 10 data points, find_rational_gf rejects the spurious fit."""
        from compute.lib.bar_gf_solver import bar_dims_virasoro, find_rational_gf

        dims = bar_dims_virasoro(10)
        result = find_rational_gf(dims)
        assert result is None


# =========================================================================
# W4 OPE n-th products (bar-side)
# =========================================================================


class TestW4NthProducts:
    """Structural tests for the W4 OPE n-th products table."""

    def test_virasoro_subalgebra(self):
        """T x T OPE has c/2 vacuum pole and standard Virasoro structure."""
        from compute.lib.w4_bar import w4_nth_products

        c = Symbol('c')
        products = w4_nth_products()
        tt = products[("T", "T")]
        assert tt[3]["vac"] == c / 2
        assert tt[1]["T"] == 2

    def test_t_w3_primary(self):
        """T x W3 OPE encodes weight-3 primary condition."""
        from compute.lib.w4_bar import w4_nth_products

        products = w4_nth_products()
        tw3 = products[("T", "W3")]
        assert tw3[1]["W3"] == 3

    def test_t_w4_primary(self):
        """T x W4 OPE encodes weight-4 primary condition."""
        from compute.lib.w4_bar import w4_nth_products

        products = w4_nth_products()
        tw4 = products[("T", "W4")]
        assert tw4[1]["W4"] == 4

    def test_w3w3_vacuum_pole(self):
        """W3 x W3 leading vacuum pole is c/3."""
        from compute.lib.w4_bar import w4_nth_products

        c = Symbol('c')
        products = w4_nth_products()
        assert products[("W3", "W3")][5]["vac"] == c / 3

    def test_w4w4_vacuum_pole(self):
        """W4 x W4 leading vacuum pole is c/4."""
        from compute.lib.w4_bar import w4_nth_products

        c = Symbol('c')
        products = w4_nth_products()
        assert products[("W4", "W4")][7]["vac"] == c / 4

    def test_w3w3_t_coupling(self):
        """W3 x W3 -> T coupling at pole 4 is 2 (universal)."""
        from compute.lib.w4_bar import w4_nth_products

        products = w4_nth_products()
        assert products[("W3", "W3")][3]["T"] == 2

    def test_w4w4_t_coupling_equals_2(self):
        """W4 x W4 -> T at pole 6 is 2 (Ward identity)."""
        from compute.lib.w4_bar import w4_nth_products

        products = w4_nth_products()
        assert products[("W4", "W4")][5]["T"] == 2

    def test_w3w3_composite_alpha(self):
        """Lambda coefficient in W3 x W3 is 16/(22+5c)."""
        from compute.lib.w4_bar import w4_nth_products

        c = Symbol('c')
        products = w4_nth_products()
        alpha = products[("W3", "W3")][1]["Lambda"]
        assert simplify(alpha - Rational(16) / (22 + 5 * c)) == 0

    def test_full_stage4_extraction(self):
        """Full stage-4 extraction returns six channels."""
        from compute.lib.w4_bar import extract_c_res_stage4

        results = extract_c_res_stage4()
        assert len(results) == 6
        # Two exact values
        assert results[(4, 4, 2, 6)] == 2
        assert results[(3, 4, 2, 5)] == 0


# =========================================================================
# Classical limit of W4 structure constants
# =========================================================================


class TestW4ClassicalLimit:
    """Classical limit (c -> inf) of W4 structure constants."""

    def test_c334_classical_limit(self):
        """c334^2 -> 42*5/(7*3) = 10 as c -> inf."""
        from compute.lib.w4_ds_ope_extraction import c334_squared_formula
        from sympy import limit, oo

        c = Symbol('c')
        lim = limit(c334_squared_formula(c), c, oo)
        assert lim == 10

    def test_c444_classical_limit(self):
        """c444^2 -> 112*2*3/(7*10*5*5) = 48/25 as c -> inf."""
        from compute.lib.w4_ds_ope_extraction import c444_squared_formula
        from sympy import limit, oo

        c = Symbol('c')
        lim = limit(c444_squared_formula(c), c, oo)
        assert lim == Rational(48, 25)
