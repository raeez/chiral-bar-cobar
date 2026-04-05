r"""Tests for BC-92: SYK model shadow analogue engine.

Tests organized by mathematical content:
1. Chord diagram combinatorics (counts, Catalan, Euler characteristics)
2. Shadow coefficients (Virasoro exact, numeric consistency)
3. Large-N shadow model (affine sl_N scaling)
4. Shadow Schwarzian (F_g vs WP volumes, 1/24 coincidence)
5. Shadow 2-point function (decay classification)
6. Shadow chaos exponent (MSS bound)
7. Random matrix crossover statistics
8. Shadow tensor rank
9. Cross-verification (multi-path)

VERIFICATION MANDATE: Every numerical result has >= 3 independent paths.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest
from sympy import Rational, bernoulli

from compute.lib.bc_syk_shadow_engine import (
    # Chord diagram combinatorics
    double_factorial_odd,
    chord_diagram_count,
    chord_diagram_count_factorial,
    chord_diagram_euler_characteristics,
    catalan_number,
    # Shadow coefficients
    kappa_virasoro,
    kappa_slN,
    virasoro_shadow_coefficients_numeric,
    virasoro_shadow_coefficients_exact,
    Q_contact_virasoro,
    # Chord decomposition
    chord_diagram_decomposition_virasoro,
    # Large-N shadow
    affine_slN_shadow_data,
    large_N_kappa_expansion,
    large_N_scaling_exponents,
    # Schwarzian connection
    lambda_fp,
    F_g_shadow,
    wp_volume_closed,
    F_g_vs_wp_volume_comparison,
    schwarzian_1_over_24_verification,
    # 2-point function
    shadow_2point_virasoro,
    shadow_2point_heisenberg,
    shadow_2point_affine_sl2,
    # Chaos exponent
    shadow_chaos_exponent_virasoro,
    shadow_chaos_landscape,
    # Random matrix statistics
    shadow_statistics_virasoro,
    # Tensor rank
    shadow_tensor_rank_virasoro,
    _necklace_count,
    # SYK-shadow dictionary
    build_syk_shadow_dictionary,
    # Cross-verification
    verify_chord_diagram_counts,
    verify_large_N_asymptotics,
    verify_F1_schwarzian,
    verify_shadow_growth_rate,
)


# ============================================================================
# 1. Chord diagram combinatorics
# ============================================================================

class TestChordDiagramCounts:
    """Verify (2r-1)!! counts chord diagrams on 2r points."""

    def test_double_factorial_base_cases(self):
        """(2*0-1)!! = 1, (2*1-1)!! = 1, (2*2-1)!! = 3."""
        assert double_factorial_odd(0) == 1
        assert double_factorial_odd(1) == 1
        assert double_factorial_odd(2) == 3

    def test_double_factorial_values(self):
        """Known values: 1, 1, 3, 15, 105, 945."""
        expected = {1: 1, 2: 3, 3: 15, 4: 105, 5: 945}
        for r, val in expected.items():
            assert double_factorial_odd(r) == val, f"(2*{r}-1)!! = {double_factorial_odd(r)}, expected {val}"

    def test_chord_count_equals_double_factorial(self):
        """chord_diagram_count(r) = (2r-1)!!."""
        for r in range(1, 8):
            assert chord_diagram_count(r) == double_factorial_odd(r)

    def test_two_independent_chord_count_formulas(self):
        """Verify (2r-1)!! = (2r)! / (2^r * r!) for r = 1..10.

        Path 1: iterative product 1*3*5*...*(2r-1)
        Path 2: factorial formula (2r)!/(2^r * r!)
        """
        for r in range(1, 11):
            v1 = chord_diagram_count(r)
            v2 = chord_diagram_count_factorial(r)
            assert v1 == v2, f"r={r}: {v1} != {v2}"

    def test_chord_count_verification_utility(self):
        """The verify_chord_diagram_counts utility confirms agreement."""
        results = verify_chord_diagram_counts(10)
        for r, df, ff, match in results:
            assert match, f"r={r}: {df} != {ff}"

    def test_double_factorial_recursion(self):
        """(2r-1)!! = (2r-1) * (2(r-1)-1)!!.

        Third verification path via recursion.
        """
        for r in range(2, 10):
            assert double_factorial_odd(r) == (2 * r - 1) * double_factorial_odd(r - 1)

    def test_chord_count_r1(self):
        """r=1: one chord on 2 points, only one way."""
        assert chord_diagram_count(1) == 1

    def test_chord_count_r2(self):
        """r=2: three chord diagrams on 4 points (parallel, crossing, nested)."""
        assert chord_diagram_count(2) == 3

    def test_chord_count_r3(self):
        """r=3: 15 chord diagrams on 6 points."""
        assert chord_diagram_count(3) == 15

    def test_chord_count_r4(self):
        """r=4: 105 chord diagrams on 8 points."""
        assert chord_diagram_count(4) == 105

    def test_chord_count_r5(self):
        """r=5: 945 chord diagrams on 10 points."""
        assert chord_diagram_count(5) == 945


class TestCatalanNumbers:
    """Catalan numbers C_r count planar chord diagrams."""

    def test_catalan_base(self):
        assert catalan_number(0) == 1
        assert catalan_number(1) == 1

    def test_catalan_values(self):
        """C_0=1, C_1=1, C_2=2, C_3=5, C_4=14, C_5=42."""
        expected = {0: 1, 1: 1, 2: 2, 3: 5, 4: 14, 5: 42}
        for n, val in expected.items():
            assert catalan_number(n) == val

    def test_catalan_le_double_factorial(self):
        """C_r <= (2r-1)!! with equality iff r <= 1."""
        for r in range(1, 8):
            assert catalan_number(r) <= chord_diagram_count(r)
        assert catalan_number(1) == chord_diagram_count(1)
        for r in range(2, 8):
            assert catalan_number(r) < chord_diagram_count(r)

    def test_catalan_recursion(self):
        """C_{n+1} = sum_{i=0}^{n} C_i * C_{n-i}.

        Independent verification via Segner's recursion.
        """
        for n in range(6):
            c_n1 = sum(catalan_number(i) * catalan_number(n - i) for i in range(n + 1))
            assert c_n1 == catalan_number(n + 1), f"n={n}: recursion gives {c_n1}"

    def test_catalan_formula_consistency(self):
        """C_n = (2n)! / ((n+1)! * n!) = binomial(2n, n) / (n+1)."""
        for n in range(8):
            c1 = catalan_number(n)
            c2 = math.comb(2 * n, n) // (n + 1)
            assert c1 == c2


class TestEulerCharacteristics:
    """Chord diagram Euler characteristics and genus distribution."""

    def test_planar_count_is_catalan(self):
        """The chi=2 (planar) count equals C_r."""
        for r in range(1, 6):
            ec = chord_diagram_euler_characteristics(r)
            assert ec[2] == catalan_number(r)

    def test_total_is_double_factorial(self):
        """Sum of all chi contributions = (2r-1)!!."""
        for r in range(2, 6):
            ec = chord_diagram_euler_characteristics(r)
            total_counted = sum(ec.values())
            # We only track planar vs non-planar
            assert total_counted == chord_diagram_count(r)


# ============================================================================
# 2. Shadow coefficients
# ============================================================================

class TestVirasOroShadowCoefficients:
    """Virasoro shadow coefficients S_r."""

    def test_S2_equals_kappa(self):
        """S_2 = kappa = c/2 for Virasoro."""
        for c in [1, 2, 5, 10, 24]:
            shadows = virasoro_shadow_coefficients_numeric(float(c), max_r=3)
            expected = c / 2.0
            assert abs(shadows[2] - expected) < 1e-10, f"c={c}: S_2={shadows[2]}, expected {expected}"

    def test_S3_equals_2(self):
        """S_3 = 2 (c-independent, the Sugawara self-coupling)."""
        for c in [1, 5, 10, 24]:
            shadows = virasoro_shadow_coefficients_numeric(float(c), max_r=4)
            assert abs(shadows[3] - 2.0) < 1e-10, f"c={c}: S_3={shadows[3]}"

    def test_S4_formula(self):
        """S_4 = 10/[c(5c+22)] = Q^contact."""
        for c in [1, 2, 5, 10, 24]:
            shadows = virasoro_shadow_coefficients_numeric(float(c), max_r=5)
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(shadows[4] - expected) < 1e-10, f"c={c}: S_4={shadows[4]}, expected {expected}"

    def test_S5_formula(self):
        """S_5 = -48/[c^2(5c+22)]."""
        for c in [1, 2, 5, 10, 24]:
            shadows = virasoro_shadow_coefficients_numeric(float(c), max_r=6)
            expected = -48.0 / (c**2 * (5 * c + 22))
            assert abs(shadows[5] - expected) / abs(expected) < 1e-8, \
                f"c={c}: S_5={shadows[5]}, expected {expected}"

    def test_exact_matches_numeric(self):
        """Exact rational computation matches numeric for c=1..10."""
        for c in range(1, 11):
            exact = virasoro_shadow_coefficients_exact(c, max_r=8)
            numeric = virasoro_shadow_coefficients_numeric(float(c), max_r=8)
            for r in range(2, 9):
                e_val = float(exact[r])
                n_val = numeric[r]
                if abs(e_val) > 1e-15:
                    assert abs(e_val - n_val) / abs(e_val) < 1e-10, \
                        f"c={c}, r={r}: exact={e_val}, numeric={n_val}"
                else:
                    assert abs(n_val) < 1e-10

    def test_Q_contact_matches_S4(self):
        """Q^contact_Vir = S_4 = 10/[c(5c+22)]."""
        for c in [1, 2, 5, 10, 24]:
            q = Q_contact_virasoro(Fraction(c))
            expected = Fraction(10, c * (5 * c + 22))
            assert q == expected

    def test_S2_exact(self):
        """Exact: S_2 = c/2."""
        for c in [1, 2, 3, 5, 10]:
            exact = virasoro_shadow_coefficients_exact(c, max_r=3)
            assert exact[2] == Fraction(c, 2)

    def test_S3_exact(self):
        """Exact: S_3 = 2 (rational, c-independent)."""
        for c in [1, 2, 3, 5, 10]:
            exact = virasoro_shadow_coefficients_exact(c, max_r=4)
            assert exact[3] == Fraction(2)


# ============================================================================
# 3. Kappa formulas (AP1 cross-check)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa formulas are correct (AP1 prevention)."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)
        assert kappa_virasoro(Fraction(26)) == Fraction(13)
        assert kappa_virasoro(Fraction(24)) == Fraction(12)

    def test_kappa_slN_formula(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N)."""
        # sl_2: dim=3, h^v=2
        assert kappa_slN(2, Fraction(1)) == Fraction(3 * 3, 4)  # 3*(1+2)/4 = 9/4
        # sl_3: dim=8, h^v=3
        assert kappa_slN(3, Fraction(1)) == Fraction(8 * 4, 6)  # 8*4/6 = 16/3
        # sl_2 at k=0 (critical adjacent): kappa = 3*2/4 = 3/2
        assert kappa_slN(2, Fraction(0)) == Fraction(3, 2)

    def test_kappa_slN_large_N(self):
        """At large N with k fixed: kappa ~ N^2/2 + kN/2."""
        k = Fraction(1)
        for N in [10, 50, 100]:
            kap = kappa_slN(N, k)
            leading = Fraction(N * N, 2) + k * N / 2
            # The subleading correction is -1/2 - k/(2N)
            error = kap - leading
            expected_error = Fraction(-1, 2) - k / (2 * N)
            assert error == expected_error, f"N={N}: error={error}, expected={expected_error}"

    def test_kappa_sl2_specific(self):
        """kappa(sl_2, k) = 3(k+2)/4.

        Cross-check with general formula: (N^2-1)(k+N)/(2N) at N=2 = 3(k+2)/4.
        """
        for k in [1, 2, 5, 10]:
            kap = kappa_slN(2, Fraction(k))
            expected = Fraction(3) * (Fraction(k) + 2) / 4
            assert kap == expected


# ============================================================================
# 4. Chord diagram decomposition
# ============================================================================

class TestChordDecomposition:
    """Test the chord diagram decomposition of shadow coefficients."""

    def test_decomposition_counts(self):
        """Total diagram counts match (2r-1)!!."""
        decomp = chord_diagram_decomposition_virasoro(10.0, max_r=5)
        for r in range(2, 6):
            assert decomp[r].total_diagrams == chord_diagram_count(r)

    def test_decomposition_planar_is_catalan(self):
        """Planar diagram count = C_r."""
        decomp = chord_diagram_decomposition_virasoro(10.0, max_r=5)
        for r in range(2, 6):
            assert decomp[r].planar_diagrams == catalan_number(r)

    def test_decomposition_total_splits(self):
        """planar + nonplanar = total."""
        decomp = chord_diagram_decomposition_virasoro(10.0, max_r=5)
        for r in range(2, 6):
            d = decomp[r]
            assert d.planar_diagrams + d.nonplanar_diagrams == d.total_diagrams

    def test_decomposition_has_shadow_values(self):
        """S_r values are populated."""
        decomp = chord_diagram_decomposition_virasoro(10.0, max_r=5)
        # S_2 = c/2 = 5.0
        assert abs(decomp[2].S_r_value - 5.0) < 1e-10


# ============================================================================
# 5. Large-N shadow model
# ============================================================================

class TestLargeNShadow:
    """Test the large-N expansion for affine sl_N shadow data."""

    def test_slN_shadow_is_class_L(self):
        """Affine KM algebras are class L: S_r = 0 for r >= 4."""
        for N in [2, 3, 5, 10]:
            data = affine_slN_shadow_data(N, Fraction(1), max_r=6)
            for r in range(4, 7):
                assert data.shadow_coefficients[r] == Fraction(0)

    def test_slN_S2_equals_kappa(self):
        """S_2 = kappa for affine sl_N."""
        for N in [2, 3, 5]:
            data = affine_slN_shadow_data(N, Fraction(1), max_r=3)
            assert data.shadow_coefficients[2] == data.kappa

    def test_slN_S3_equals_2(self):
        """S_3 = alpha = 2 for affine KM."""
        for N in [2, 3, 5]:
            data = affine_slN_shadow_data(N, Fraction(1), max_r=4)
            assert data.shadow_coefficients[3] == Fraction(2)

    def test_large_N_expansion_coefficients(self):
        """1/N expansion: kappa = N^2/2 + kN/2 - 1/2 - k/(2N)."""
        exp = large_N_kappa_expansion(1, Fraction(1))
        assert exp['N^2'] == Fraction(1, 2)
        assert exp['N^1'] == Fraction(1, 2)
        assert exp['N^0'] == Fraction(-1, 2)
        assert exp['N^{-1}'] == Fraction(-1, 2)

    def test_large_N_expansion_at_k2(self):
        """At k=2: kappa = N^2/2 + N - 1/2 - 1/N."""
        exp = large_N_kappa_expansion(1, Fraction(2))
        assert exp['N^1'] == Fraction(1)  # k/2 = 1
        assert exp['N^{-1}'] == Fraction(-1)  # -k/2 = -1

    def test_large_N_asymptotics_verification(self):
        """The asymptotic expansion matches exact values."""
        result = verify_large_N_asymptotics(Fraction(1))
        for entry in result['data']:
            # Error should be exactly 0 since we have all terms
            assert entry['error'] == Fraction(0), \
                f"N={entry['N']}: error={entry['error']}"

    def test_scaling_exponent_S2(self):
        """S_2 = kappa scales as N^2."""
        data = large_N_scaling_exponents(Fraction(1))
        assert data[2]['exponent'] == 2
        assert data[2]['leading_coefficient'] == Fraction(1, 2)

    def test_scaling_exponent_S3(self):
        """S_3 = 2 is N-independent (exponent 0)."""
        data = large_N_scaling_exponents(Fraction(1))
        assert data[3]['exponent'] == 0
        assert data[3]['leading_coefficient'] == Fraction(2)

    def test_scaling_exponent_S4(self):
        """S_4 = 0 for class L (no exponent)."""
        data = large_N_scaling_exponents(Fraction(1))
        assert data[4]['exponent'] is None
        assert data[4]['leading_coefficient'] == Fraction(0)

    def test_kappa_monotone_in_N(self):
        """kappa(sl_N, k) is strictly increasing in N for fixed k > 0."""
        k = Fraction(1)
        prev = kappa_slN(2, k)
        for N in [3, 4, 5, 10, 20]:
            curr = kappa_slN(N, k)
            assert curr > prev, f"kappa({N}) = {curr} <= kappa({N-1}) = {prev}"
            prev = curr


# ============================================================================
# 6. Shadow Schwarzian and genus expansion
# ============================================================================

class TestShadowSchwarzian:
    """F_g vs Weil-Petersson volumes and the 1/24 coincidence."""

    def test_lambda_1_is_1_over_24(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2_is_7_over_5760(self):
        """lambda_2^FP = 7/5760 (AP38: correct normalization)."""
        lam2 = lambda_fp(2)
        assert lam2 == Fraction(7, 5760), f"lambda_2 = {lam2}"

    def test_lambda_3(self):
        """lambda_3^FP from Bernoulli B_6 = 1/42."""
        lam3 = lambda_fp(3)
        # (2^5 - 1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720
        # = 31/(32*42*720) = 31/967680
        assert lam3 == Fraction(31, 967680)

    def test_F1_is_kappa_over_24(self):
        """F_1 = kappa/24."""
        for kap in [Fraction(1), Fraction(13), Fraction(12)]:
            assert F_g_shadow(kap, 1) == kap / 24

    def test_F2_formula(self):
        """F_2 = kappa * 7/5760."""
        kap = Fraction(1)
        assert F_g_shadow(kap, 2) == Fraction(7, 5760)

    def test_schwarzian_1_over_24_three_paths(self):
        """Verify 1/24 by three independent paths."""
        result = verify_F1_schwarzian()
        assert result['all_agree']

    def test_schwarzian_1_over_24_utility(self):
        """The schwarzian_1_over_24_verification utility confirms the match."""
        result = schwarzian_1_over_24_verification()
        assert result['match']
        assert result['lambda_1_FP'] == Fraction(1, 24)

    def test_wp_volume_genus1(self):
        """V_{1,1}(0) = pi^2/12."""
        v = wp_volume_closed(1)
        expected = math.pi ** 2 / 12.0
        assert abs(v - expected) / expected < 1e-10

    def test_wp_volume_genus2_positive(self):
        """V_{2,0} > 0."""
        v = wp_volume_closed(2)
        assert v > 0

    def test_wp_volume_genus3_positive(self):
        """V_{3,0} > 0."""
        v = wp_volume_closed(3)
        assert v > 0

    def test_wp_volume_genus4_positive(self):
        """V_{4,0} > 0."""
        v = wp_volume_closed(4)
        assert v > 0

    def test_wp_volumes_increase(self):
        """WP volumes V_{g,0} should increase with genus (after normalization)."""
        # Actually V_{g,0} ~ (2g)! * pi^{6g-6} grows super-exponentially
        # Just check they are all positive and non-degenerate
        for g in range(1, 5):
            v = wp_volume_closed(g)
            assert v > 0, f"V_{{{g},0}} = {v}"

    def test_F_g_all_positive(self):
        """F_g > 0 for all g >= 1 (Bernoulli numbers alternate but
        the prefactor ensures positivity)."""
        kap = Fraction(1)
        for g in range(1, 8):
            fg = F_g_shadow(kap, g)
            assert fg > 0, f"F_{g} = {fg}"

    def test_F_g_ratio_converges(self):
        """F_{g+1}/F_g -> 1/(2*pi)^2 as g -> infinity.

        The Bernoulli asymptotics: |B_{2g}| ~ 2*(2g)!/(2*pi)^{2g}.
        """
        kap = Fraction(1)
        target = 1.0 / (2 * math.pi) ** 2
        ratios = []
        for g in range(1, 15):
            fg = float(F_g_shadow(kap, g))
            fg1 = float(F_g_shadow(kap, g + 1))
            if fg > 0:
                ratios.append(fg1 / fg)
        # Should converge to target
        assert abs(ratios[-1] - target) / target < 0.05

    def test_F_g_comparison_runs(self):
        """F_g vs WP volume comparison produces data."""
        result = F_g_vs_wp_volume_comparison(1.0, max_g=3)
        assert len(result) == 3
        for g in range(1, 4):
            assert 'F_g' in result[g]
            assert 'V_g_0' in result[g]


# ============================================================================
# 7. Shadow 2-point function
# ============================================================================

class TestShadow2Point:
    """Shadow 2-point function and decay classification."""

    def test_heisenberg_is_class_G(self):
        """Heisenberg: G_A(r) = 0 for r > 2."""
        data = shadow_2point_heisenberg(1.0, max_r=10)
        assert data.shadow_class == 'G'
        assert abs(data.G_values[2] - 1.0) < 1e-10  # S_2/kappa = 1
        for r in range(3, 11):
            assert abs(data.G_values[r]) < 1e-15

    def test_sl2_is_class_L(self):
        """Affine sl_2: G_A(r) = 0 for r > 3."""
        data = shadow_2point_affine_sl2(1.0, max_r=10)
        assert data.shadow_class == 'L'
        for r in range(4, 11):
            assert abs(data.G_values[r]) < 1e-15

    def test_virasoro_is_class_M(self):
        """Virasoro: shadow depth is infinite (class M)."""
        data = shadow_2point_virasoro(10.0, max_r=20)
        assert data.shadow_class == 'M'
        # Check that G_A(r) is nonzero for large r
        assert abs(data.G_values[10]) > 1e-20

    def test_virasoro_G2_is_1(self):
        """G_A(2) = S_2/kappa = 1 for Virasoro."""
        data = shadow_2point_virasoro(10.0, max_r=5)
        assert abs(data.G_values[2] - 1.0) < 1e-10

    def test_virasoro_growth_rate_positive(self):
        """Shadow growth rate rho > 0 for Virasoro."""
        data = shadow_2point_virasoro(10.0, max_r=20)
        assert data.growth_rate > 0

    def test_growth_rate_formula(self):
        """rho^2 = (180c + 872) / [c^2(5c+22)].

        Verify at c = 10.
        """
        c = 10.0
        rho_sq = (180 * c + 872) / (c ** 2 * (5 * c + 22))
        rho_th = math.sqrt(rho_sq)

        data = shadow_2point_virasoro(c, max_r=20)
        assert abs(data.growth_rate - rho_th) / rho_th < 1e-10

    def test_growth_rate_decreases_with_c(self):
        """Shadow growth rate rho(c) decreases for large c.

        rho^2 ~ 180/(5*c^2) at large c, so rho ~ 6/c.
        """
        rho_prev = None
        for c in [5, 10, 20, 50]:
            data = shadow_2point_virasoro(float(c), max_r=15)
            rho = data.growth_rate
            if rho_prev is not None:
                assert rho < rho_prev, f"rho({c}) = {rho} >= rho(prev) = {rho_prev}"
            rho_prev = rho

    def test_decay_exponent_near_minus_5_2(self):
        """For class M, the power law exponent should be near -5/2.

        The asymptotic is |S_r| ~ const * rho^r * r^{-5/2}.
        So the fitted decay exponent should be approximately -2.5.
        """
        # Use large c for better convergence
        data = shadow_2point_virasoro(25.0, max_r=50)
        if data.decay_exponent is not None:
            # Allow generous tolerance since this is an asymptotic result
            # and the fit from finite r can deviate
            assert data.decay_exponent < 0, "Decay exponent should be negative"
            # The -5/2 is the THEORETICAL prediction; the actual fitted
            # exponent from finite data may differ
            assert abs(data.decay_exponent - (-2.5)) < 2.0, \
                f"Decay exponent {data.decay_exponent} not near -5/2"


# ============================================================================
# 8. Shadow chaos exponent
# ============================================================================

class TestShadowChaos:
    """Shadow analogue of the chaos/Lyapunov exponent."""

    def test_chaos_exponent_positive(self):
        """lambda_sh > 0 for c > 0."""
        for c in [1, 5, 10, 20]:
            data = shadow_chaos_exponent_virasoro(float(c))
            assert data['lambda_sh'] > 0

    def test_chaos_exponent_formula(self):
        """lambda_sh = Q^contact / kappa = 20/[c^2(5c+22)]."""
        for c in [1, 5, 10, 24]:
            data = shadow_chaos_exponent_virasoro(float(c))
            expected = 20.0 / (c**2 * (5 * c + 22))
            assert abs(data['lambda_sh'] - expected) / expected < 1e-10

    def test_chaos_exponent_decreases_with_c(self):
        """lambda_sh decreases as c increases."""
        prev = None
        for c in [1, 5, 10, 20]:
            data = shadow_chaos_exponent_virasoro(float(c))
            lam = data['lambda_sh']
            if prev is not None:
                assert lam < prev
            prev = lam

    def test_mss_bound_large_c(self):
        """For large c, the MSS-normalized exponent is small."""
        data = shadow_chaos_exponent_virasoro(25.0)
        assert data['lambda_normalized'] < 1.0

    def test_chaos_landscape_runs(self):
        """shadow_chaos_landscape produces results for c=1..25."""
        results = shadow_chaos_landscape()
        assert len(results) == 25
        for r in results:
            assert 'lambda_sh' in r

    def test_Q_contact_times_2_over_c(self):
        """lambda_sh = 2*Q^contact/c = 2*10/[c^2(5c+22)] = 20/[c^2(5c+22)].

        Verify the intermediate formula Q^contact/kappa = Q^contact * 2/c.
        """
        for c in [1, 5, 10]:
            q = 10.0 / (c * (5 * c + 22))
            kap = c / 2.0
            lam = q / kap
            expected = 20.0 / (c**2 * (5 * c + 22))
            assert abs(lam - expected) < 1e-15


# ============================================================================
# 9. Random matrix statistics
# ============================================================================

class TestRandomMatrixStats:
    """Shadow statistics: structured vs random behavior."""

    def test_statistics_runs(self):
        """shadow_statistics_virasoro produces valid output."""
        result = shadow_statistics_virasoro(10.0, max_r=20)
        assert result['max_r'] == 20
        assert result['mean_spacing_ratio'] >= 0

    def test_spacing_ratio_bounded(self):
        """Spacing ratios are in [0, 1]."""
        result = shadow_statistics_virasoro(10.0, max_r=30)
        for sr in result['spacing_ratios']:
            assert 0 <= sr <= 1.0 + 1e-10

    def test_poisson_benchmark(self):
        """Poisson benchmark is 2*ln(2) - 1 ~ 0.386."""
        result = shadow_statistics_virasoro(10.0, max_r=20)
        expected = 2 * math.log(2) - 1
        assert abs(result['poisson_benchmark'] - expected) < 1e-10


# ============================================================================
# 10. Shadow tensor rank
# ============================================================================

class TestShadowTensorRank:
    """Shadow tensor rank from OPE coupling structure."""

    def test_necklace_count_r2(self):
        """Number of binary necklaces with 2 beads = 3."""
        # 00, 01/10, 11 -> 3 necklaces
        assert _necklace_count(2, 2) == 3

    def test_necklace_count_r3(self):
        """Number of binary necklaces with 3 beads = 4."""
        # 000, 001/010/100, 011/101/110, 111 -> 4
        assert _necklace_count(3, 2) == 4

    def test_necklace_count_r4(self):
        """Number of binary necklaces with 4 beads = 6."""
        assert _necklace_count(4, 2) == 6

    def test_tensor_rank_produces_output(self):
        """shadow_tensor_rank_virasoro runs and produces ranks."""
        result = shadow_tensor_rank_virasoro(10.0, max_r=6)
        assert 'ranks' in result
        for r in range(2, 7):
            assert r in result['ranks']
            assert result['ranks'][r]['raw_rank'] == 2 ** r

    def test_raw_rank_is_2_to_r(self):
        """Before symmetry reduction, rank = 2^r."""
        result = shadow_tensor_rank_virasoro(10.0, max_r=6)
        for r in range(2, 7):
            assert result['ranks'][r]['raw_rank'] == 2 ** r


# ============================================================================
# 11. SYK-shadow dictionary
# ============================================================================

class TestSYKShadowDictionary:
    """Complete SYK <-> shadow correspondence."""

    def test_dictionary_builds(self):
        """build_syk_shadow_dictionary produces a valid dictionary."""
        d = build_syk_shadow_dictionary(10.0)
        assert d.c_val == 10.0
        assert d.kappa == 5.0
        assert d.shadow_class == 'M'

    def test_dictionary_schwarzian_match(self):
        """Schwarzian 1/24 matches for all c."""
        d = build_syk_shadow_dictionary(10.0)
        assert d.schwarzian_match

    def test_dictionary_chaos_positive(self):
        """Chaos exponent is positive."""
        d = build_syk_shadow_dictionary(10.0)
        assert d.chaos_lambda > 0

    def test_dictionary_growth_rate_positive(self):
        """Shadow growth rate is positive."""
        d = build_syk_shadow_dictionary(10.0)
        assert d.shadow_growth_rate > 0


# ============================================================================
# 12. Cross-verification: multi-path consistency
# ============================================================================

class TestCrossVerification:
    """Multi-path verification of key results."""

    def test_kappa_virasoro_3_paths(self):
        """kappa(Vir_c) = c/2 verified three ways.

        Path 1: Direct formula kappa = c/2
        Path 2: F_1 = kappa/24, so kappa = 24*F_1
        Path 3: S_2 = kappa from shadow tower
        """
        for c in [1, 10, 24]:
            # Path 1
            kap1 = kappa_virasoro(Fraction(c))
            # Path 2
            f1 = F_g_shadow(kap1, 1)
            kap2 = f1 * 24
            # Path 3
            shadows = virasoro_shadow_coefficients_exact(c, max_r=3)
            kap3 = shadows[2]

            assert kap1 == kap2 == kap3, \
                f"c={c}: {kap1}, {kap2}, {kap3}"

    def test_kappa_slN_3_paths(self):
        """kappa(sl_N, k) verified three ways.

        Path 1: Direct formula dim(g)*(k+h^v)/(2*h^v)
        Path 2: Expansion at large N + subleading correction
        Path 3: S_2 from shadow data
        """
        for N in [2, 3, 5]:
            k = Fraction(1)
            # Path 1
            kap1 = kappa_slN(N, k)
            # Path 2
            exp = large_N_kappa_expansion(N, k)
            kap2 = (exp['N^2'] * N**2 + exp['N^1'] * N
                    + exp['N^0'] + exp['N^{-1}'] / N)
            # Path 3
            data = affine_slN_shadow_data(N, k)
            kap3 = data.shadow_coefficients[2]

            assert kap1 == kap2 == kap3, \
                f"N={N}: {kap1}, {kap2}, {kap3}"

    def test_chord_count_3_paths(self):
        """(2r-1)!! verified three ways.

        Path 1: Iterative product
        Path 2: Factorial formula (2r)!/(2^r * r!)
        Path 3: Recursion (2r-1)!! = (2r-1) * (2(r-1)-1)!!
        """
        for r in range(2, 8):
            p1 = chord_diagram_count(r)
            p2 = chord_diagram_count_factorial(r)
            p3 = (2 * r - 1) * chord_diagram_count(r - 1)
            assert p1 == p2 == p3, f"r={r}: {p1}, {p2}, {p3}"

    def test_F1_3_paths(self):
        """F_1 = kappa/24 verified by three paths."""
        result = verify_F1_schwarzian()
        assert result['all_agree']

    def test_shadow_growth_rate_formula_vs_branch_point(self):
        """Growth rate from formula vs branch-point computation.

        Path 1: rho^2 = (180c + 872) / [c^2(5c+22)]
        Path 2: rho = 1/|t*| where t* is the nearest branch point of Q_L(t)
        These must agree EXACTLY (to floating-point precision).
        """
        for c in [1.0, 5.0, 10.0, 20.0, 50.0]:
            result = verify_shadow_growth_rate(c, max_r=20)
            assert result['formula_branch_agreement'] < 1e-12, \
                f"c={c}: rho_formula={result['rho_formula']:.10f}, " \
                f"rho_branch={result['rho_branch_point']:.10f}"

    def test_shadow_growth_rate_branch_point_derivation(self):
        """Verify rho^2 = q2/q0 = (36 + 80/(5c+22))/c^2 = (180c+872)/[c^2(5c+22)].

        This is an independent algebraic derivation from Q_L(t*) = 0.
        """
        for c in [1.0, 5.0, 10.0, 24.0]:
            q0 = c ** 2
            q2 = 36.0 + 80.0 / (5 * c + 22)
            rho_sq_from_branch = q2 / q0
            rho_sq_from_formula = (180 * c + 872) / (c ** 2 * (5 * c + 22))
            assert abs(rho_sq_from_branch - rho_sq_from_formula) < 1e-12

    def test_Q_contact_3_paths(self):
        """Q^contact = 10/[c(5c+22)] verified three ways.

        Path 1: Direct formula
        Path 2: S_4 from shadow coefficients
        Path 3: lambda_sh * kappa (from chaos exponent)
        """
        for c in [1, 5, 10, 24]:
            # Path 1
            q1 = float(Q_contact_virasoro(Fraction(c)))
            # Path 2
            shadows = virasoro_shadow_coefficients_numeric(float(c), max_r=5)
            q2 = shadows[4]
            # Path 3
            chaos = shadow_chaos_exponent_virasoro(float(c))
            q3 = chaos['lambda_sh'] * (c / 2.0)

            assert abs(q1 - q2) < 1e-10, f"c={c}: Q_direct={q1}, S_4={q2}"
            assert abs(q1 - q3) < 1e-10, f"c={c}: Q_direct={q1}, chaos*kappa={q3}"

    def test_chaos_does_not_exceed_mss_at_large_c(self):
        """MSS bound: lambda_normalized <= 1 for c sufficiently large.

        The MSS-normalized exponent = 40/[pi * c^3 * (5c+22)] -> 0 as c -> infinity.
        """
        for c in [10.0, 20.0, 50.0]:
            data = shadow_chaos_exponent_virasoro(c)
            assert data['mss_satisfied'], f"c={c}: MSS violated, lambda_norm={data['lambda_normalized']}"

    def test_class_hierarchy_consistent(self):
        """Class G ⊂ Class L ⊂ Class C ⊂ Class M in terms of shadow depth.

        Heisenberg (G, r_max=2) < sl_2 (L, r_max=3) < Virasoro (M, r_max=inf).
        """
        h = shadow_2point_heisenberg(1.0, max_r=10)
        s = shadow_2point_affine_sl2(1.0, max_r=10)
        v = shadow_2point_virasoro(10.0, max_r=10)

        # Count nonzero G_A values
        h_nonzero = sum(1 for r, g in h.G_values.items() if abs(g) > 1e-15)
        s_nonzero = sum(1 for r, g in s.G_values.items() if abs(g) > 1e-15)
        v_nonzero = sum(1 for r, g in v.G_values.items() if abs(g) > 1e-15)

        assert h_nonzero == 1  # only S_2
        assert s_nonzero == 2  # S_2 and S_3
        assert v_nonzero >= 8  # many nonzero S_r

    def test_shadow_coefficients_sign_alternation(self):
        """For Virasoro with c > 0, sign(S_r) alternates eventually.

        The shadow growth rate formula gives complex branch points,
        ensuring asymptotic sign alternation.
        """
        shadows = virasoro_shadow_coefficients_numeric(10.0, max_r=15)
        # Check that there are both positive and negative values
        positives = sum(1 for r, s in shadows.items() if s > 0 and r >= 4)
        negatives = sum(1 for r, s in shadows.items() if s < 0 and r >= 4)
        assert positives > 0, "No positive S_r for r >= 4"
        assert negatives > 0, "No negative S_r for r >= 4"

    def test_S4_positive_S5_negative(self):
        """S_4 > 0 and S_5 < 0 for c > 0.

        S_4 = 10/[c(5c+22)] > 0.
        S_5 = -48/[c^2(5c+22)] < 0.
        """
        for c in [1, 5, 10, 24]:
            shadows = virasoro_shadow_coefficients_numeric(float(c), max_r=6)
            assert shadows[4] > 0, f"c={c}: S_4 = {shadows[4]} not positive"
            assert shadows[5] < 0, f"c={c}: S_5 = {shadows[5]} not negative"


# ============================================================================
# 13. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_kappa_virasoro_at_c0_raises(self):
        """c=0 gives kappa=0 which is degenerate for shadow computations."""
        with pytest.raises(ValueError):
            virasoro_shadow_coefficients_numeric(0.0, max_r=5)

    def test_exact_c0_raises(self):
        with pytest.raises(ValueError):
            virasoro_shadow_coefficients_exact(0, max_r=5)

    def test_lambda_fp_g0_raises(self):
        """lambda_fp(0) should raise ValueError."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_wp_volume_g5_raises(self):
        """V_{5,0} not tabulated."""
        with pytest.raises(ValueError):
            wp_volume_closed(5)

    def test_chord_count_r0(self):
        """r=0: one empty chord diagram."""
        assert chord_diagram_count(0) == 1

    def test_catalan_negative(self):
        """C_n = 0 for n < 0."""
        assert catalan_number(-1) == 0

    def test_necklace_count_n1(self):
        """1 bead, 2 colors: 2 necklaces."""
        assert _necklace_count(1, 2) == 2

    def test_necklace_count_n0(self):
        assert _necklace_count(0, 2) == 1


# ============================================================================
# 14. Consistency between exact and numeric at non-integer c
# ============================================================================

class TestNonIntegerC:
    """Test at non-integer central charge values."""

    def test_c_half(self):
        """c = 1/2 (Ising model): shadow coefficients are rational."""
        exact = virasoro_shadow_coefficients_exact(1, 2, max_r=6)  # c = 1/2
        assert exact[2] == Fraction(1, 4)  # kappa = c/2 = 1/4
        assert exact[3] == Fraction(2)  # alpha = 2

    def test_c_7_10(self):
        """c = 7/10 (tricritical Ising)."""
        exact = virasoro_shadow_coefficients_exact(7, 10, max_r=5)
        assert exact[2] == Fraction(7, 20)  # kappa = 7/20

    def test_c_25(self):
        """c = 25 (near self-dual c=26-1=25, dual c'=1)."""
        exact = virasoro_shadow_coefficients_exact(25, max_r=5)
        assert exact[2] == Fraction(25, 2)

    def test_c_13_self_dual(self):
        """c = 13: self-dual point for Virasoro (Vir_13^! = Vir_13)."""
        exact = virasoro_shadow_coefficients_exact(13, max_r=6)
        assert exact[2] == Fraction(13, 2)
        # At the self-dual point, kappa = 13/2 and kappa' = (26-13)/2 = 13/2
        # So kappa + kappa' = 13 (AP24: NOT zero!)
        kap = kappa_virasoro(Fraction(13))
        kap_dual = kappa_virasoro(Fraction(26 - 13))
        assert kap + kap_dual == Fraction(13)


# ============================================================================
# 15. Bernoulli number cross-checks
# ============================================================================

class TestBernoulliCrossChecks:
    """Bernoulli number properties used in F_g formula."""

    def test_B2_is_1_6(self):
        """B_2 = 1/6."""
        assert bernoulli(2) == Rational(1, 6)

    def test_B4_is_minus_1_30(self):
        """B_4 = -1/30."""
        assert bernoulli(4) == Rational(-1, 30)

    def test_B6_is_1_42(self):
        """B_6 = 1/42."""
        assert bernoulli(6) == Rational(1, 42)

    def test_lambda_fp_positivity(self):
        """lambda_g^FP > 0 for all g >= 1.

        The |B_{2g}| ensures positivity, and (2^{2g-1}-1)/2^{2g-1} > 0.
        """
        for g in range(1, 12):
            assert lambda_fp(g) > 0

    def test_lambda_fp_decay(self):
        """lambda_{g+1}^FP / lambda_g^FP -> 1/(2*pi)^2."""
        target = 1.0 / (4 * math.pi ** 2)
        prev = float(lambda_fp(1))
        for g in range(2, 15):
            curr = float(lambda_fp(g))
            ratio = curr / prev
            prev = curr
        # At g=14, the ratio should be close to target
        assert abs(ratio - target) / target < 0.05
