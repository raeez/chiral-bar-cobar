r"""Tests for the W_3 finite-window generating-function engine.

The certified window is g = 2, 3, 4.  These tests check exact W_3
cross-channel constants, rational diagnostics from those three terms,
scalar FP separation, and negative boundaries: no Pade pole is promoted
to a convergence-radius theorem, no sampled cross/scalar comparison is
promoted to all-c dominance, and no analytic tau-function or hierarchy
membership is certified here.

Checked finite-window properties:

* R_2 and R_3 are not constant in g, so the three-term window is not
  geometric.
* The [1/1] Pade approximant in u = t^2 reconstructs the three input
  coefficients exactly.
* The finite-window Pade pole is positive on the sampled positive c
  values, without any all-genus radius assertion.
* Cross-channel terms can exceed the scalar lane in the sampled small-c
  window, while genus 2 is not uniformly larger as c -> infinity.
* The numerator polynomials have no positive real roots in the checked
  window.
* The Pade pole is independent of the canonical Virasoro T-line shadow
  metric in the tested window.
* As c -> 0, R_3/R_2 has the Betti limit
  alpha_{4,4}*alpha_{2,2}/alpha_{3,3}^2 = 262080891/157803844.
* delta_F_g(c) > 0 for c > 0 in the certified genera.
* delta_F_2 -> 1/16 as c -> infinity; g = 3, 4 have linear leading
  large-c terms.
* D_2 = 16, D_3 = 138240, D_4 = 17418240, and D_g divides (4g)!.

References:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    theorem_multiweight_structure_engine.py
    theorem_multiweight_generating_function_engine.py
"""

from fractions import Fraction

from compute.lib.theorem_multiweight_generating_function_engine import (
    BAR_KOSZUL_OBJECT_ROLES,
    GENUS_WINDOW,
    HOLOGRAPHIC_PACKAGE_ENTRIES,
    MODULAR_KOSZUL_COMPUTE_PROJECTIONS,
    available_genera,
    delta_Fg,
    generating_function,
    generating_function_u,
    evaluate_generating_function,
    evaluate_generating_function_u,
    genus_ratio,
    all_genus_ratios,
    ratio_growth_quotient,
    ratio_growth_exponent,
    ratio_second_difference,
    pade_11,
    pade_evaluate,
    pade_pole,
    pade_reconstruction_error,
    virasoro_t_line_shadow_data,
    w3_diagonal_channel_data,
    shadow_metric_Q_virasoro,
    shadow_metric_zero_modulus_sq,
    shadow_metric_sqrt_series,
    numerator_polynomial,
    numerator_roots_float,
    numerator_rational_roots,
    numerator_gcd_content,
    large_c_leading,
    small_c_leading,
    kappa_w3,
    scalar_lane_decomposition,
    scalar_Fg,
    total_Fg,
    cross_to_scalar_ratio,
    cross_exceeds_scalar,
    denominator_factored,
    full_analysis,
)


# ============================================================================
# Finite-window and firewall discipline
# ============================================================================

class TestFiniteWindowAndFirewalls:
    """Guard the computation surface against package and lane conflations."""

    def test_available_genera_is_exact_window(self):
        """The engine exposes only the certified g=2,3,4 window."""
        assert GENUS_WINDOW == (2, 3, 4)
        assert available_genera() == (2, 3, 4)

    def test_holographic_package_has_seven_entries(self):
        """H(A) has exactly seven entries."""
        assert HOLOGRAPHIC_PACKAGE_ENTRIES == (
            "A",
            "A^i",
            "A^!",
            "C",
            "r(z)",
            "Theta_A",
            "nabla^hol",
        )
        assert len(HOLOGRAPHIC_PACKAGE_ENTRIES) == 7

    def test_modular_koszul_compute_package_has_six_projections(self):
        """Pi_X(L) has exactly six projections and is not H(A)."""
        assert MODULAR_KOSZUL_COMPUTE_PROJECTIONS == (
            "Fact_X(L)",
            "barB_X(L)",
            "Theta_L",
            "L_L",
            "(V_br,T_br)",
            "R4_mod(L)",
        )
        assert len(MODULAR_KOSZUL_COMPUTE_PROJECTIONS) == 6
        assert set(MODULAR_KOSZUL_COMPUTE_PROJECTIONS).isdisjoint(
            HOLOGRAPHIC_PACKAGE_ENTRIES
        )

    def test_bar_koszul_objects_are_distinct(self):
        """A, B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A) stay distinct."""
        assert set(BAR_KOSZUL_OBJECT_ROLES) == {
            "A",
            "B(A)",
            "A^i",
            "A^!",
            "Omega(B(A))",
            "Z_ch^der(A)",
        }
        assert "inversion" in BAR_KOSZUL_OBJECT_ROLES["Omega(B(A))"]
        assert "Verdier" in BAR_KOSZUL_OBJECT_ROLES["A^!"]
        assert "ChirHoch" in BAR_KOSZUL_OBJECT_ROLES["Z_ch^der(A)"]
        assert BAR_KOSZUL_OBJECT_ROLES["A^!"] != BAR_KOSZUL_OBJECT_ROLES["Omega(B(A))"]


# ============================================================================
# Cross-check delta_F_g against theorem_multiweight_structure_engine
# ============================================================================

class TestCrossCheckStructureEngine:
    """Verify delta_F_g against the structure engine."""

    def test_delta_F2_matches_structure_engine(self):
        """delta_F_2 = (c+204)/(16c) matches the structure engine."""
        from compute.lib.theorem_multiweight_structure_engine import (
            delta_Fg_closed as delta_Fg_ref,
        )
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            assert delta_Fg(2, c) == delta_Fg_ref(2, c), (
                f"delta_F_2 mismatch at c={c_val}"
            )

    def test_delta_F3_matches_structure_engine(self):
        """delta_F_3 matches the structure engine."""
        from compute.lib.theorem_multiweight_structure_engine import (
            delta_Fg_closed as delta_Fg_ref,
        )
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            assert delta_Fg(3, c) == delta_Fg_ref(3, c), (
                f"delta_F_3 mismatch at c={c_val}"
            )

    def test_delta_F4_matches_structure_engine(self):
        """delta_F_4 matches the structure engine."""
        from compute.lib.theorem_multiweight_structure_engine import (
            delta_Fg_closed as delta_Fg_ref,
        )
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            assert delta_Fg(4, c) == delta_Fg_ref(4, c), (
                f"delta_F_4 mismatch at c={c_val}"
            )

    def test_delta_F2_explicit_value(self):
        """Direct value: delta_F_2(10) = (10+204)/(16*10) = 107/80."""
        assert delta_Fg(2, Fraction(10)) == Fraction(107, 80)

    def test_delta_F2_at_c1(self):
        """Direct value: delta_F_2(1) = 205/16."""
        assert delta_Fg(2, Fraction(1)) == Fraction(205, 16)


# ============================================================================
# Ratio analysis
# ============================================================================

class TestRatioAnalysis:
    """Test the genus ratio delta_F_{g+1}/delta_F_g."""

    def test_ratios_positive(self):
        """All available ratios are positive at sampled positive c."""
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            ratios = all_genus_ratios(c)
            for g, r in ratios.items():
                assert r > 0, f"Ratio R_{g} negative at c={c_val}"

    def test_ratio_not_constant_in_g(self):
        """R_2 != R_3 in the certified window."""
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            ratios = all_genus_ratios(c)
            assert ratios[2] != ratios[3], (
                f"Ratios equal at c={c_val}: geometric series would be unexpected"
            )

    def test_ratio_growth_exceeds_one(self):
        """R_3 > R_2 for the sampled c < 300 values."""
        for c_val in [1, 4, 10, 26, 50, 100]:
            c = Fraction(c_val)
            ratios = all_genus_ratios(c)
            assert ratios[3] > ratios[2], (
                f"R_3 <= R_2 at c={c_val}: expected R_3 > R_2"
            )

    def test_ratio_growth_varies_with_c(self):
        """R_3/R_2 depends on c in the sampled window."""
        c1, c2 = Fraction(1), Fraction(50)
        r1 = all_genus_ratios(c1)
        r2 = all_genus_ratios(c2)
        growth_1 = r1[3] / r1[2]
        growth_50 = r2[3] / r2[2]
        assert growth_1 != growth_50, "R_3/R_2 is constant across c"

    def test_ratio_growth_quotient_and_exponent_are_separate(self):
        """The exact quotient is not misreported as the logarithmic exponent."""
        c = Fraction(10)
        ratios = all_genus_ratios(c)
        quotient = ratios[3] / ratios[2]
        exponent = ratio_growth_exponent(c)
        assert ratio_growth_quotient(c) == quotient
        assert ratio_second_difference(c) == quotient - 1
        assert exponent is not None
        assert exponent > 0
        assert Fraction.from_float(exponent).limit_denominator() != quotient

    def test_ratio_growth_small_c_limit(self):
        """As c -> 0, R_3/R_2 has the max-Betti quotient.

        This is the max-Betti dominated limit.
        """
        # Betti coefficients from structure engine
        a22 = Fraction(51, 4)
        a33 = Fraction(6281, 4)
        a44 = Fraction(5138841, 16)
        limit_exact = (a44 * a22) / (a33 * a33)
        assert limit_exact == Fraction(262080891, 157803844)

        # At c=1, should be close to this limit
        c = Fraction(1)
        ratios = all_genus_ratios(c)
        growth = ratios[3] / ratios[2]
        # Relative error should be < 1%
        rel_error = abs(float(growth) - float(limit_exact)) / float(limit_exact)
        assert rel_error < 0.01, (
            f"Small-c limit mismatch: growth={float(growth)}, "
            f"limit={float(limit_exact)}, rel_error={rel_error}"
        )

    def test_ratio_second_difference_positive_small_c(self):
        """R_3/R_2 - 1 > 0 for small c (ratios grow with genus)."""
        for c_val in [1, 4, 10, 26]:
            c = Fraction(c_val)
            sd = ratio_second_difference(c)
            assert sd > 0, f"Second difference non-positive at c={c_val}"


# ============================================================================
# Pade approximant
# ============================================================================

class TestPadeApproximant:
    """Test the [1/1] Pade approximant in u = t^2."""

    def test_pade_reconstruction_exact(self):
        """Pade [1/1] reproduces all 3 input coefficients exactly."""
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            errors = pade_reconstruction_error(c)
            for g, err in errors.items():
                assert err == 0, (
                    f"Pade reconstruction error at c={c_val}, g={g}: {err}"
                )

    def test_pade_pole_positive(self):
        """The finite-window Pade pole is positive at sampled positive c."""
        for c_val in [1, 4, 10, 26, 50, 100]:
            c = Fraction(c_val)
            pole = pade_pole(c)
            assert pole > 0, f"Pade pole non-positive at c={c_val}: {pole}"

    def test_pade_pole_diagnostic_monotone_in_sampled_window(self):
        """The finite-window Pade pole increases across the sampled c values."""
        poles = []
        for c_val in [1, 4, 10, 26, 50, 100]:
            c = Fraction(c_val)
            poles.append((c_val, pade_pole(c)))
        for i in range(len(poles) - 1):
            assert poles[i][1] < poles[i + 1][1], (
                f"Pade pole not monotone: u_pole({poles[i][0]}) = {poles[i][1]} "
                f">= u_pole({poles[i+1][0]}) = {poles[i+1][1]}"
            )

    def test_pade_evaluate_matches_series(self):
        """Pade evaluation at small u matches the truncated series."""
        c = Fraction(10)
        u = Fraction(1, 1000)  # small u
        pade_val = pade_evaluate(c, u)
        series_exact = evaluate_generating_function_u(c, u)
        # Pade and series agree to O(u^5) since we matched 3 terms (u^2, u^3, u^4)
        # The O(u^5) remainder gives relative error ~ u^3 ~ 1e-9, but the
        # actual Pade extrapolation introduces geometric-series tails, so
        # use a tolerance of 1e-4 (generous, structural test not numerical).
        diff = abs(float(pade_val - series_exact))
        mag = abs(float(series_exact)) if float(series_exact) != 0 else 1.0
        assert diff / mag < 1e-4, (
            f"Pade-series disagreement: diff/mag = {diff/mag}"
        )


# ============================================================================
# Positivity and sign structure
# ============================================================================

class TestPositivityAndRoots:
    """Test positivity and numerator root structure."""

    def test_delta_Fg_positive(self):
        """delta_F_g(c) > 0 in the certified positive-c samples."""
        for g in [2, 3, 4]:
            for c_val in [1, 2, 4, 10, 26, 50, 100]:
                c = Fraction(c_val)
                val = delta_Fg(g, c)
                assert val > 0, f"delta_F_{g}({c_val}) = {val} <= 0"

    def test_P2_has_root_minus_204(self):
        """P_2(c) = c + 204 has the unique root c = -204."""
        roots = numerator_rational_roots(2)
        assert Fraction(-204) in roots, f"Root -204 not found: {roots}"
        assert len(roots) == 1, f"P_2 should have exactly 1 rational root: {roots}"

    def test_P3_no_positive_rational_roots(self):
        """P_3 has no positive rational roots, so no positive-c zero appears."""
        roots = numerator_rational_roots(3)
        positive = [r for r in roots if r > 0]
        assert len(positive) == 0, f"P_3 has positive rational root: {positive}"

    def test_P4_no_rational_roots(self):
        """P_4 has no rational roots."""
        roots = numerator_rational_roots(4)
        assert len(roots) == 0, f"P_4 has rational roots: {roots}"

    def test_all_float_roots_negative_real_part(self):
        """All checked roots of P_g have Re(c) < 0."""
        for g in [2, 3, 4]:
            roots = numerator_roots_float(g)
            for r in roots:
                assert r.real < 0, (
                    f"Root of P_{g} has non-negative real part: {r}"
                )

    def test_numerator_content_is_one(self):
        """GCD of numerator coefficients is 1 (primitive polynomial)."""
        for g in [2, 3, 4]:
            assert numerator_gcd_content(g) == 1, (
                f"P_{g} is not primitive: GCD = {numerator_gcd_content(g)}"
            )


# ============================================================================
# Shadow metric independence
# ============================================================================

class TestShadowMetricConnection:
    """Test (non-)connection between G and the shadow metric Q_L."""

    def test_virasoro_t_line_constants_are_canonical(self):
        """Canonical T-line constants: S3=2, S4=10/[c(5c+22)], Delta=40/(5c+22)."""
        c = Fraction(10)
        data = virasoro_t_line_shadow_data(c)
        assert data["kappa"] == Fraction(5)
        assert data["S3"] == Fraction(2)
        assert data["S4"] == Fraction(1, 72)
        assert data["Delta"] == Fraction(5, 9)

    def test_shadow_metric_uses_canonical_virasoro_values(self):
        """At c=10, Q(t) = (10+6t)^2 + (10/9)t^2."""
        c = Fraction(10)
        for t in [Fraction(-2), Fraction(0), Fraction(3)]:
            expected = (Fraction(10) + 6 * t) ** 2 + Fraction(10, 9) * t ** 2
            assert shadow_metric_Q_virasoro(c, t) == expected

    def test_shadow_metric_positive_real_line(self):
        """Shadow metric Q_L(t) > 0 for all real t when c > 0."""
        for c_val in [1, 10, 26]:
            c = Fraction(c_val)
            for t_val in [-5, -1, 0, 1, 5, 10]:
                Q = shadow_metric_Q_virasoro(c, Fraction(t_val))
                assert Q > 0, (
                    f"Q_L({t_val}) = {Q} <= 0 at c={c_val}"
                )

    def test_pade_pole_not_proportional_to_Q_zeros(self):
        """u_pole / |t_0(Q_L)|^2 varies by more than 100x across samples.

        This checks that the pole is not a scalar multiple of the metric zero.
        """
        ratios = []
        for c_val in [1, 10, 100]:
            c = Fraction(c_val)
            t0_sq = shadow_metric_zero_modulus_sq(c)
            pole = pade_pole(c)
            if t0_sq > 0:
                ratios.append(float(pole / t0_sq))
        # Ratios should vary by factor > 100
        assert max(ratios) / min(ratios) > 100, (
            f"Pade pole / Q_L zero ratio too stable: {ratios}"
        )

    def test_sqrt_Q_coefficients_well_defined(self):
        """sqrt(Q_L) Taylor expansion has correct leading term 2*kappa."""
        c = Fraction(10)
        sqQ = shadow_metric_sqrt_series(c, max_order=4)
        kappa = c / 2
        assert sqQ[0] == 2 * kappa, (
            f"Leading sqrt(Q_L) coeff = {sqQ[0]}, expected {2*kappa}"
        )
        assert sqQ[1] == Fraction(6)


# ============================================================================
# Cross-channel comparison
# ============================================================================

class TestCrossChannelComparison:
    """Test scalar-lane and cross-channel separation."""

    def test_cross_exceeds_scalar_in_tested_small_c_window(self):
        """delta_F_g > kappa * lambda_g in the tested small-c window."""
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            for g in [2, 3, 4]:
                ratio = cross_to_scalar_ratio(g, c)
                assert ratio > 1, (
                    f"Cross/scalar ratio < 1 at c={c_val}, g={g}: {float(ratio)}"
                )

    def test_cross_scalar_ratio_grows_with_genus_in_sampled_window(self):
        """Cross-to-scalar ratio increases with genus in sampled windows."""
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            r2 = cross_to_scalar_ratio(2, c)
            r3 = cross_to_scalar_ratio(3, c)
            r4 = cross_to_scalar_ratio(4, c)
            assert r3 > r2, (
                f"Cross/scalar ratio not increasing: g=2->{float(r2)}, "
                f"g=3->{float(r3)}"
            )
            assert r4 > r3, (
                f"Cross/scalar ratio not increasing: g=3->{float(r3)}, "
                f"g=4->{float(r4)}"
            )

    def test_genus2_cross_does_not_dominate_for_all_c(self):
        """At genus 2, cross/scalar tends to zero as c grows."""
        c = Fraction(300)
        assert cross_to_scalar_ratio(2, c) < 1
        assert not cross_exceeds_scalar(2, c)

    def test_kappa_w3_is_5c_over_6(self):
        """kappa(W_3) = 5c/6, not the Virasoro T-line value c/2."""
        for c_val in [1, 6, 12, 30]:
            c = Fraction(c_val)
            assert kappa_w3(c) == Fraction(5) * c / Fraction(6), (
                f"kappa(W_3) wrong at c={c_val}"
            )

    def test_diagonal_channel_sum_is_scalar_lane_not_cross_channel(self):
        """kappa_T+kappa_W gives scalar_Fg; delta_Fg is the mixed graph lane."""
        c = Fraction(50)
        channels = w3_diagonal_channel_data(c)
        assert channels["T"].kappa == Fraction(25)
        assert channels["T"].S3 == Fraction(2)
        assert channels["W"].kappa == Fraction(50, 3)
        assert channels["W"].S3 == Fraction(0)
        assert channels["T"].kappa + channels["W"].kappa == kappa_w3(c)

        decomp = scalar_lane_decomposition(2, c)
        assert decomp["scalar"] == Fraction(175, 3456)
        assert decomp["cross"] == Fraction(127, 400)
        assert decomp["total"] == scalar_Fg(2, c) + delta_Fg(2, c)


# ============================================================================
# Bernoulli / Faber-Pandharipande normalization
# ============================================================================

class TestFaberPandharipandeNormalization:
    """Keep scalar FP numbers separate from multi-weight graph constants."""

    def test_lambda_fp_g2_g3_from_bernoulli_formula(self):
        """lambda_g^FP = ((2^(2g-1)-1)/2^(2g-1)) * |B_2g|/(2g)!."""
        from compute.lib.theorem_multiweight_structure_engine import lambda_fp

        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_scalar_lane_uses_w3_kappa_times_fp_not_delta_constants(self):
        """For W3, scalar_Fg=(5c/6)lambda_g^FP and is not delta_Fg."""
        c = Fraction(50)
        assert scalar_Fg(2, c) == Fraction(5, 6) * c * Fraction(7, 5760)
        assert scalar_Fg(2, c) == Fraction(175, 3456)
        assert delta_Fg(2, c) == Fraction(127, 400)
        assert scalar_Fg(2, c) != delta_Fg(2, c)


# ============================================================================
# Asymptotic behavior
# ============================================================================

class TestAsymptotics:
    """Test large-c and small-c leading behavior."""

    def test_large_c_leading_g2(self):
        """delta_F_2 -> 1/16 as c -> infinity."""
        assert large_c_leading(2) == Fraction(1, 16)

    def test_large_c_leading_g3(self):
        """delta_F_3 leading coeff = 5/138240 = 1/27648."""
        assert large_c_leading(3) == Fraction(5, 138240)
        assert large_c_leading(3) == Fraction(1, 27648)

    def test_large_c_leading_g4(self):
        """delta_F_4 leading coeff = 287/17418240."""
        assert large_c_leading(4) == Fraction(287, 17418240)

    def test_large_c_convergence(self):
        """delta_F_2(c) -> 1/16 for large c.

        delta_F_2 = (c+204)/(16c) = 1/16 + 204/(16c), so the correction
        is 204/c relative. At c=100000, rel_err < 0.5%.
        """
        c = Fraction(100000)
        val = delta_Fg(2, c)
        expected = Fraction(1, 16)
        rel_err = abs(float(val - expected)) / float(expected)
        assert rel_err < 0.005, f"Large-c convergence fails: rel_err={rel_err}"

    def test_small_c_scaling(self):
        """delta_F_g(c) ~ alpha_{g,g} * c^{1-g} for small c."""
        c = Fraction(1, 10)
        for g in [2, 3, 4]:
            val = delta_Fg(g, c)
            leading = small_c_leading(g) * c ** (1 - g)
            # Leading term should capture > 90% of the value
            ratio = float(val) / float(leading)
            assert 0.9 < ratio < 1.1, (
                f"Small-c scaling fails at g={g}: ratio={ratio}"
            )


# ============================================================================
# Denominator structure
# ============================================================================

class TestDenominatorStructure:
    """Test the denominator factorization pattern."""

    def test_denominator_factorization_g2(self):
        """D_2 = 16 = 2^4."""
        info = denominator_factored(2)
        assert info['D_g'] == 16
        assert info['prime_factors'] == {2: 4}

    def test_denominator_factorization_g3(self):
        """D_3 = 138240 = 2^{10} * 3^3 * 5."""
        info = denominator_factored(3)
        assert info['D_g'] == 138240
        assert info['prime_factors'] == {2: 10, 3: 3, 5: 1}

    def test_denominator_factorization_g4(self):
        """D_4 = 17418240 = 2^{11} * 3^5 * 5 * 7."""
        info = denominator_factored(4)
        assert info['D_g'] == 17418240
        assert info['prime_factors'] == {2: 11, 3: 5, 5: 1, 7: 1}

    def test_denominator_divides_high_factorial(self):
        """D_g | (4g)! for g = 2, 3, 4.

        The denominator D_g arises from graph automorphism factors and
        vertex combinatorics. Verified: D_g divides (4g)! for g=2,3,4.
        """
        from math import factorial
        for g in [2, 3, 4]:
            D = denominator_factored(g)['D_g']
            f = factorial(4 * g)
            assert f % D == 0, (
                f"D_{g} = {D} does not divide (4g)! = {f}"
            )


# ============================================================================
# Generating function evaluation consistency
# ============================================================================

class TestGeneratingFunctionConsistency:
    """Test generating_function and evaluate_generating_function."""

    def test_generating_function_keys(self):
        """generating_function returns keys {4, 6, 8} for g = 2,3,4."""
        c = Fraction(10)
        gf = generating_function(c)
        assert set(gf.keys()) == {4, 6, 8}
        assert generating_function_u(c) == {
            2: delta_Fg(2, c),
            3: delta_Fg(3, c),
            4: delta_Fg(4, c),
        }

    def test_evaluate_at_zero(self):
        """G(0, c) = 0 for all c."""
        for c_val in [1, 10, 50]:
            assert evaluate_generating_function(Fraction(c_val), Fraction(0)) == 0
            assert evaluate_generating_function_u(Fraction(c_val), Fraction(0)) == 0

    def test_evaluate_t_matches_u_substitution(self):
        """G(t,c) equals G(u,c) after u=t^2 in the finite window."""
        c = Fraction(10)
        t = Fraction(1, 5)
        assert evaluate_generating_function(c, t) == evaluate_generating_function_u(c, t * t)

    def test_total_Fg_sum(self):
        """F_g = scalar + cross: total_Fg = scalar_Fg + delta_Fg."""
        for c_val in [1, 10, 26]:
            c = Fraction(c_val)
            for g in [2, 3, 4]:
                assert total_Fg(g, c) == scalar_Fg(g, c) + delta_Fg(g, c)

    def test_full_analysis_runs(self):
        """full_analysis returns expected keys without error."""
        result = full_analysis(10)
        assert 'delta_F' in result
        assert 'ratios' in result
        assert 'pade_pole' in result
        assert 'total_F' in result
        assert 'scalar_cross_decomposition' in result
        assert result['genus_window'] == (2, 3, 4)
        assert result['c'] == 10


# ============================================================================
# Independent cross-checks for hardcoded values
# ============================================================================

class TestIndependentCrossChecks:
    """Every hardcoded value is checked through an independent route."""

    def test_delta_F2_cross_check_betti(self):
        """Cross-check delta_F_2 via Betti stratum reconstruction.

        Route A: closed-form (c+204)/(16c)
        Route B: Betti sum alpha_{2,1}*c^0 + alpha_{2,2}*c^{-1}
        """
        from compute.lib.theorem_multiweight_structure_engine import (
            delta_Fg_from_betti,
        )
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            path_a = delta_Fg(2, c)
            path_b = delta_Fg_from_betti(2, c)
            assert path_a == path_b, (
                f"delta_F_2 cross-check fails at c={c_val}: "
                f"closed={path_a}, betti={path_b}"
            )

    def test_delta_F3_cross_check_betti(self):
        """Cross-check delta_F_3 via Betti stratum reconstruction."""
        from compute.lib.theorem_multiweight_structure_engine import (
            delta_Fg_from_betti,
        )
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            path_a = delta_Fg(3, c)
            path_b = delta_Fg_from_betti(3, c)
            assert path_a == path_b, (
                f"delta_F_3 cross-check fails at c={c_val}: "
                f"closed={path_a}, betti={path_b}"
            )

    def test_delta_F4_cross_check_betti(self):
        """Cross-check delta_F_4 via Betti stratum reconstruction."""
        from compute.lib.theorem_multiweight_structure_engine import (
            delta_Fg_from_betti,
        )
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            path_a = delta_Fg(4, c)
            path_b = delta_Fg_from_betti(4, c)
            assert path_a == path_b, (
                f"delta_F_4 cross-check fails at c={c_val}: "
                f"closed={path_a}, betti={path_b}"
            )

    def test_large_c_leading_cross_check_direct(self):
        """Cross-check large-c leading coefficients via direct limit.

        Route A: large_c_leading(g) from numerator/denominator data.
        Route B: delta_F_g(c) evaluated at large c, compared to leading term.

        delta_F_g = leading * c^{net_deg} + O(c^{net_deg - 1}).
        For g=2: net_deg=0, correction is 204/c.
        For g>=3: net_deg=1, correction is O(1).
        Use c=1000000 to suppress subleading by 1/c.
        """
        for g in [2, 3, 4]:
            leading = large_c_leading(g)
            c = Fraction(1000000)
            val = delta_Fg(g, c)
            if g == 2:
                ratio = val / leading
            else:
                ratio = val / (leading * c)
            rel_err = abs(float(ratio) - 1.0)
            assert rel_err < 0.01, (
                f"Large-c cross-check fails at g={g}: ratio={float(ratio)}"
            )

    def test_denominator_cross_check_formula(self):
        """Cross-check D_g: verify P_g(c) / (D_g * c^{g-1}) = delta_F_g.

        Recompute P_g from the coefficient list independently.
        """
        for g in [2, 3, 4]:
            coeffs = numerator_polynomial(g)
            D = {2: 16, 3: 138240, 4: 17418240}[g]
            c = Fraction(7)  # arbitrary test point
            deg = len(coeffs) - 1
            P = sum(Fraction(coeffs[k]) * c ** (deg - k) for k in range(len(coeffs)))
            result = P / (Fraction(D) * c ** (g - 1))
            assert result == delta_Fg(g, c), (
                f"Denominator cross-check fails at g={g}"
            )

    def test_kappa_cross_check_structure_engine(self):
        """Cross-check kappa(W_3) = 5c/6 against direct Betti data.

        At large c, delta_F_g ~ alpha_{g,0} * c. The scalar part is
        kappa * lambda_g = (5c/6) * lambda_g. So the large-c ratio
        R_g = alpha_{g,0} / ((5/6) * lambda_g) should match the
        structure engine's LARGE_C_RATIOS.
        """
        from compute.lib.theorem_multiweight_structure_engine import (
            LARGE_C_RATIOS, lambda_fp, betti_coefficient,
        )
        for g in [3, 4]:
            alpha_g0 = betti_coefficient(g, 0)
            kappa_coeff = Fraction(5, 6)
            lam = lambda_fp(g)
            computed_ratio = alpha_g0 / (kappa_coeff * lam)
            assert computed_ratio == LARGE_C_RATIOS[g], (
                f"Large-c ratio cross-check fails at g={g}: "
                f"computed={computed_ratio}, stored={LARGE_C_RATIOS[g]}"
            )

    def test_pade_pole_cross_check_ratio(self):
        """Cross-check Pade pole via independent formula.

        Pade pole = -1/q1 = a_3/a_4 where a_g = delta_F_g.
        Verify this independently of the pade_11 function.
        """
        for c_val in [1, 10, 26]:
            c = Fraction(c_val)
            a3 = delta_Fg(3, c)
            a4 = delta_Fg(4, c)
            pole_direct = a3 / a4
            pole_pade = pade_pole(c)
            assert pole_direct == pole_pade, (
                f"Pade pole cross-check fails at c={c_val}: "
                f"direct={pole_direct}, pade={pole_pade}"
            )

    def test_root_minus_204_cross_check_evaluation(self):
        """Cross-check P_2(-204) = 0 by direct evaluation."""
        c = Fraction(-204)
        coeffs = numerator_polynomial(2)
        P = sum(Fraction(coeffs[k]) * c ** (1 - k) for k in range(len(coeffs)))
        assert P == 0, f"P_2(-204) = {P}, expected 0"

    def test_generating_function_cross_check_summation(self):
        """Cross-check evaluate_generating_function against manual sum."""
        c = Fraction(10)
        t = Fraction(1, 5)
        gf_val = evaluate_generating_function(c, t)
        manual = (
            delta_Fg(2, c) * t ** 4
            + delta_Fg(3, c) * t ** 6
            + delta_Fg(4, c) * t ** 8
        )
        assert gf_val == manual, (
            f"Generating function cross-check fails: {gf_val} != {manual}"
        )

    def test_cross_to_scalar_ratio_cross_check(self):
        """Cross-check cross_to_scalar_ratio via independent division."""
        from compute.lib.theorem_multiweight_structure_engine import lambda_fp
        c = Fraction(10)
        for g in [2, 3, 4]:
            ratio_fn = cross_to_scalar_ratio(g, c)
            ratio_manual = delta_Fg(g, c) / (kappa_w3(c) * lambda_fp(g))
            assert ratio_fn == ratio_manual, (
                f"Cross/scalar ratio cross-check fails at g={g}"
            )
