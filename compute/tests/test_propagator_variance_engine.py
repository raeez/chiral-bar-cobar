"""Tests for propagator variance and mixing polynomials.

Validates the multi-channel non-autonomy invariant delta_mix,
the mixing polynomial P(W_3) = 25c^2 + 100c - 428, Cauchy-Schwarz
non-negativity, enhanced symmetry detection, DS variance transport,
and the multi-channel shadow metric.

Manuscript references:
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
"""
import pytest
from sympy import (
    Rational, Symbol, simplify, sqrt, S, cancel, factor, numer,
    denom, oo, solve, Matrix, Poly, Float,
)
from compute.lib.propagator_variance_engine import (
    ChannelData,
    PropagatorVarianceData,
    propagator_variance,
    mixing_polynomial_w3,
    mixing_polynomial_wN,
    heisenberg_propagator,
    affine_sl2_propagator,
    virasoro_propagator,
    w3_propagator,
    w4_propagator,
    betagamma_propagator,
    enhanced_symmetry_detection,
    variance_landscape,
    ds_variance_transport,
    multi_channel_shadow_metric,
    sl3_to_w3_transport,
    w3_full_shadow_metric,
    evaluate_w3_variance,
    evaluate_at_special_charges,
)


c = Symbol('c')
k = Symbol('k')


# ============================================================================
# 1. TestSingleChannel
# ============================================================================


class TestSingleChannel:
    """Single channel always has delta_mix = 0 (trivially autonomous)."""

    def test_single_channel_zero_variance(self):
        """A single channel with any kappa and f_quartic has delta_mix = 0."""
        ch = ChannelData(label='X', weight=2, kappa=c / 2, f_quartic=c ** 2)
        assert propagator_variance([ch]) == S.Zero

    def test_empty_channels_zero_variance(self):
        """Empty channel list returns delta_mix = 0."""
        assert propagator_variance([]) == S.Zero

    def test_heisenberg_single_channel(self):
        """Heisenberg has rank 1 and delta_mix = 0."""
        data = heisenberg_propagator()
        assert data.rank == 1
        assert data.delta_mix == S.Zero
        assert data.is_autonomous()

    def test_heisenberg_rank_n(self):
        """Rank-n Heisenberg still single effective channel, delta_mix = 0."""
        for n in [1, 2, 5, 10]:
            data = heisenberg_propagator(n)
            assert data.delta_mix == S.Zero
            assert data.total_kappa == Rational(n, 2)

    def test_virasoro_single_channel(self):
        """Virasoro has rank 1 and delta_mix = 0."""
        data = virasoro_propagator()
        assert data.rank == 1
        assert data.delta_mix == S.Zero
        assert data.is_autonomous()

    def test_virasoro_kappa(self):
        """Virasoro kappa = c/2."""
        data = virasoro_propagator()
        assert simplify(data.total_kappa - c / 2) == 0

    def test_affine_sl2_single_channel(self):
        """Affine sl_2 has rank 1 and delta_mix = 0."""
        data = affine_sl2_propagator()
        assert data.rank == 1
        assert data.delta_mix == S.Zero
        assert data.is_autonomous()

    def test_affine_sl2_kappa_at_level_1(self):
        """Affine sl_2 at k=1: kappa = 3*(1+2)/4 = 9/4."""
        data = affine_sl2_propagator(level=1)
        assert data.total_kappa == Rational(9, 4)


# ============================================================================
# 2. TestCauchySchwarz
# ============================================================================


class TestCauchySchwarz:
    """delta_mix >= 0 always (Cauchy-Schwarz inequality)."""

    def test_two_equal_channels_zero(self):
        """Two channels with identical f/kappa ratio give delta_mix = 0."""
        ch1 = ChannelData(label='A', weight=1, kappa=Rational(3), f_quartic=Rational(6))
        ch2 = ChannelData(label='B', weight=2, kappa=Rational(5), f_quartic=Rational(10))
        # f_A/kappa_A = 2 = f_B/kappa_B => delta_mix = 0
        delta = propagator_variance([ch1, ch2])
        assert simplify(delta) == 0

    def test_two_different_channels_positive(self):
        """Two channels with different f/kappa ratios give delta_mix > 0."""
        ch1 = ChannelData(label='A', weight=1, kappa=Rational(2), f_quartic=Rational(4))
        ch2 = ChannelData(label='B', weight=2, kappa=Rational(3), f_quartic=Rational(9))
        # f_A/kappa_A = 2, f_B/kappa_B = 3 => delta_mix > 0
        delta = propagator_variance([ch1, ch2])
        val = float(delta.evalf())
        assert val > 0

    def test_cauchy_schwarz_positive_numerical(self):
        """Random positive kappa and f values always yield delta_mix >= 0."""
        import random
        random.seed(42)
        for _ in range(20):
            n = random.randint(2, 5)
            channels = []
            for i in range(n):
                kap = Rational(random.randint(1, 20), random.randint(1, 5))
                f = Rational(random.randint(-10, 10), random.randint(1, 5))
                channels.append(ChannelData(
                    label=f'ch_{i}', weight=i + 1, kappa=kap, f_quartic=f
                ))
            delta = propagator_variance(channels)
            val = float(delta.evalf())
            assert val >= -1e-15, f"Cauchy-Schwarz violated: delta = {val}"

    def test_w3_cauchy_schwarz_numerical(self):
        """W_3 delta_mix >= 0 at a range of positive c values."""
        data = w3_propagator()
        assert data.verify_cauchy_schwarz()

    def test_w4_cauchy_schwarz_numerical(self):
        """W_4 delta_mix >= 0 at a range of positive c values."""
        data = w4_propagator()
        assert data.verify_cauchy_schwarz()

    def test_equality_iff_proportional(self):
        """delta_mix = 0 iff f_a/kappa_a = constant."""
        # Proportional case
        lam = Rational(7, 3)
        ch1 = ChannelData(label='A', weight=1, kappa=Rational(4), f_quartic=4 * lam)
        ch2 = ChannelData(label='B', weight=2, kappa=Rational(9), f_quartic=9 * lam)
        ch3 = ChannelData(label='C', weight=3, kappa=Rational(2), f_quartic=2 * lam)
        delta = propagator_variance([ch1, ch2, ch3])
        assert simplify(delta) == 0

    def test_three_channels_generic_positive(self):
        """Three channels with non-proportional f/kappa give positive delta_mix."""
        ch1 = ChannelData(label='A', weight=1, kappa=Rational(1), f_quartic=Rational(1))
        ch2 = ChannelData(label='B', weight=2, kappa=Rational(1), f_quartic=Rational(2))
        ch3 = ChannelData(label='C', weight=3, kappa=Rational(1), f_quartic=Rational(4))
        delta = propagator_variance([ch1, ch2, ch3])
        val = float(delta.evalf())
        assert val > 0

    def test_cauchy_schwarz_ratio_in_01(self):
        """The Cauchy-Schwarz ratio delta/(sum f^2/kappa) is in [0,1]."""
        data = w3_propagator()
        # Evaluate at c = 10 (away from poles)
        ratio_val = float(data.cauchy_schwarz_ratio.subs(c, 10).evalf())
        assert 0 <= ratio_val <= 1 + 1e-12


# ============================================================================
# 3. TestMixingPolynomialW3
# ============================================================================


class TestMixingPolynomialW3:
    """P(W_3) = 25c^2 + 100c - 428."""

    def test_polynomial_coefficients(self):
        """P(W_3) has correct coefficients."""
        P, _ = mixing_polynomial_w3()
        poly = Poly(P, c)
        coeffs = poly.all_coeffs()
        assert coeffs == [25, 100, -428]

    def test_leading_coefficient_25(self):
        """Leading coefficient is 25."""
        P, _ = mixing_polynomial_w3()
        poly = Poly(P, c)
        assert poly.LC() == 25

    def test_constant_term_minus_428(self):
        """P(0) = -428."""
        P, _ = mixing_polynomial_w3()
        assert P.subs(c, 0) == -428

    def test_discriminant(self):
        """Discriminant = 100^2 + 4*25*428 = 10000 + 42800 = 52800."""
        disc = 100 ** 2 + 4 * 25 * 428
        assert disc == 52800

    def test_zeros_count(self):
        """P(W_3) has exactly two real zeros."""
        _, zeros = mixing_polynomial_w3()
        assert len(zeros) == 2

    def test_zeros_approximate_values(self):
        """Zeros are approximately c ~ 2.597 and c ~ -6.597."""
        _, zeros = mixing_polynomial_w3()
        vals = sorted([float(z.evalf()) for z in zeros])
        assert abs(vals[0] - (-6.597)) < 0.01
        assert abs(vals[1] - 2.597) < 0.01

    def test_zeros_exact_form(self):
        """Zeros are c = (-10 +/- 2*sqrt(132))/5."""
        _, zeros = mixing_polynomial_w3()
        # Check that both zeros satisfy 25*c^2 + 100*c - 428 = 0
        for z in zeros:
            assert simplify(25 * z ** 2 + 100 * z - 428) == 0

    def test_P_at_c13(self):
        """P(13) = 25*169 + 1300 - 428 = 5097."""
        P, _ = mixing_polynomial_w3()
        assert P.subs(c, 13) == 25 * 169 + 1300 - 428
        assert P.subs(c, 13) == 5097

    def test_P_positive_at_large_c(self):
        """P(c) > 0 for large positive c."""
        P, _ = mixing_polynomial_w3()
        assert P.subs(c, 100) > 0
        assert P.subs(c, 1000) > 0

    def test_P_negative_at_c0(self):
        """P(0) = -428 < 0, so P crosses zero between 0 and the positive root."""
        P, _ = mixing_polynomial_w3()
        assert P.subs(c, 0) < 0


# ============================================================================
# 4. TestW3Propagator
# ============================================================================


class TestW3Propagator:
    """W_3 has two channels: T (weight 2) and W (weight 3)."""

    def test_w3_rank_2(self):
        """W_3 has rank 2."""
        data = w3_propagator()
        assert data.rank == 2
        assert len(data.channels) == 2

    def test_w3_channel_weights(self):
        """T has weight 2, W has weight 3."""
        data = w3_propagator()
        assert data.channels[0].weight == 2
        assert data.channels[1].weight == 3

    def test_w3_kappa_T(self):
        """kappa_T = c/2."""
        data = w3_propagator()
        assert simplify(data.channels[0].kappa - c / 2) == 0

    def test_w3_kappa_W(self):
        """kappa_W = c/3."""
        data = w3_propagator()
        assert simplify(data.channels[1].kappa - c / 3) == 0

    def test_w3_total_kappa(self):
        """Total kappa = c/2 + c/3 = 5c/6."""
        data = w3_propagator()
        assert simplify(data.total_kappa - 5 * c / 6) == 0

    def test_w3_delta_mix_nonzero_generically(self):
        """delta_mix is generically nonzero for W_3."""
        data = w3_propagator()
        assert not data.is_autonomous()

    def test_w3_delta_mix_at_c10(self):
        """delta_mix at c=10 is numerically positive."""
        data = w3_propagator()
        val = float(data.delta_mix.subs(c, 10).evalf())
        assert val > 0

    def test_w3_delta_mix_vanishes_at_zeros(self):
        """delta_mix = 0 at zeros of P(W_3)."""
        _, zeros = mixing_polynomial_w3()
        data = w3_propagator()
        for z in zeros:
            val = simplify(data.delta_mix.subs(c, z))
            # Numerically verify (symbolic simplification may be complex)
            num_val = float(val.evalf())
            assert abs(num_val) < 1e-10, f"delta_mix at c={z} is {num_val}"

    def test_w3_delta_mix_at_c13(self):
        """Evaluate delta_mix at c=13 (Virasoro self-dual point)."""
        data = w3_propagator()
        val = float(data.delta_mix.subs(c, 13).evalf())
        assert val > 0  # P(13) = 5097 != 0

    def test_w3_depth_class_M(self):
        """Both W_3 channels have depth class M (mixed)."""
        data = w3_propagator()
        assert data.channels[0].depth_class == 'M'
        assert data.channels[1].depth_class == 'M'


# ============================================================================
# 5. TestW4Propagator
# ============================================================================


class TestW4Propagator:
    """W_4 has three channels: weights 2, 3, 4."""

    def test_w4_rank_3(self):
        """W_4 has rank 3."""
        data = w4_propagator()
        assert data.rank == 3
        assert len(data.channels) == 3

    def test_w4_channel_weights(self):
        """W_4 channels at weights 2, 3, 4."""
        data = w4_propagator()
        weights = [ch.weight for ch in data.channels]
        assert weights == [2, 3, 4]

    def test_w4_kappas(self):
        """kappa_j = c/j for j = 2, 3, 4."""
        data = w4_propagator()
        for idx, j in enumerate([2, 3, 4]):
            assert simplify(data.channels[idx].kappa - c / j) == 0

    def test_w4_total_kappa(self):
        """Total kappa = c/2 + c/3 + c/4 = 13c/12."""
        data = w4_propagator()
        expected = c * Rational(13, 12)
        assert simplify(data.total_kappa - expected) == 0

    def test_w4_delta_mix_positive_numerically(self):
        """W_4 delta_mix > 0 at generic c."""
        data = w4_propagator()
        val = float(data.delta_mix.subs(c, 10).evalf())
        assert val > 0

    def test_w4_mixing_polynomial_nonzero(self):
        """W_4 mixing polynomial is nonzero (not identically zero)."""
        data = w4_propagator()
        assert data.mixing_polynomial != S.Zero


# ============================================================================
# 6. TestEnhancedSymmetry
# ============================================================================


class TestEnhancedSymmetry:
    """Enhanced symmetry: f_a/kappa_a = constant (curvature-proportional)."""

    def test_single_channel_trivially_enhanced(self):
        """Single-channel algebras are trivially autonomous."""
        data = virasoro_propagator()
        sym = enhanced_symmetry_detection(data)
        assert sym['is_enhanced']

    def test_w3_generically_not_enhanced(self):
        """W_3 is generically not enhanced."""
        data = w3_propagator()
        sym = enhanced_symmetry_detection(data)
        assert not sym['is_enhanced']
        assert sym['symmetry_type'] == 'generic (non-autonomous)'

    def test_w3_enhanced_at_zeros_numerical(self):
        """At zeros of P(W_3), enhanced symmetry holds."""
        _, zeros = mixing_polynomial_w3()
        for z in zeros:
            data = w3_propagator(z)
            # Evaluate delta numerically
            val = float(data.delta_mix.evalf())
            assert abs(val) < 1e-10

    def test_proportionality_ratios_exist(self):
        """enhanced_symmetry_detection returns proportionality ratios."""
        data = w3_propagator()
        sym = enhanced_symmetry_detection(data)
        assert 'proportionality_ratios' in sym
        assert 'T' in sym['proportionality_ratios']
        assert 'W' in sym['proportionality_ratios']

    def test_heisenberg_enhanced(self):
        """Heisenberg is enhanced (trivially)."""
        data = heisenberg_propagator()
        sym = enhanced_symmetry_detection(data)
        assert sym['is_enhanced']


# ============================================================================
# 7. TestDSTransport
# ============================================================================


class TestDSTransport:
    """DS reduction creates variance from zero variance."""

    def test_sl3_to_w3_creates_variance(self):
        """sl_3 -> W_3: delta_mix goes from 0 to nonzero."""
        tr = sl3_to_w3_transport()
        assert tr['parent_delta'] == S.Zero
        assert tr['delta_created']

    def test_sl3_to_w3_rank_change(self):
        """sl_3 has rank 1, W_3 has rank 2."""
        tr = sl3_to_w3_transport()
        assert tr['parent_rank'] == 1
        assert tr['child_rank'] == 2

    def test_sl3_to_w3_class_change(self):
        """sl_3 is class L, W_3 is class M."""
        tr = sl3_to_w3_transport()
        assert tr['parent_class'] == ['L']
        assert tr['child_class'] == ['M', 'M']

    def test_ds_transport_mechanism_string(self):
        """DS transport has a mechanism description."""
        tr = sl3_to_w3_transport()
        assert 'Ghost sector' in tr['mechanism']

    def test_ds_transport_custom_pair(self):
        """Custom DS transport between two PropagatorVarianceData objects."""
        parent = heisenberg_propagator()
        child = w3_propagator()
        tr = ds_variance_transport(parent, child)
        assert tr['parent'] == 'Heisenberg (rank 1)'
        assert tr['child'] == 'W_3'
        assert tr['delta_created']


# ============================================================================
# 8. TestVarianceLandscape
# ============================================================================


class TestVarianceLandscape:
    """variance_landscape() covers all families."""

    def test_landscape_returns_all_families(self):
        """Landscape contains all standard families."""
        land = variance_landscape()
        assert 'Virasoro' in land
        assert 'W_3' in land
        assert 'W_4' in land
        assert 'Heisenberg' in land
        assert 'V_k(sl_2)' in land

    def test_single_channel_families_zero(self):
        """Virasoro, Heisenberg, affine all have delta = 0 in landscape."""
        land = variance_landscape()
        for _, delta_val in land['Virasoro']:
            assert delta_val == 0
        for _, delta_val in land['Heisenberg']:
            assert delta_val == 0
        for _, delta_val in land['V_k(sl_2)']:
            assert delta_val == 0

    def test_w3_nonzero_in_landscape(self):
        """W_3 has nonzero delta_mix at most c-values in the landscape."""
        land = variance_landscape()
        nonzero_count = sum(1 for _, v in land['W_3'] if v is not None and abs(v) > 1e-12)
        assert nonzero_count > 0

    def test_w4_nonzero_in_landscape(self):
        """W_4 has nonzero delta_mix at most c-values in the landscape."""
        land = variance_landscape()
        nonzero_count = sum(1 for _, v in land['W_4'] if v is not None and abs(v) > 1e-12)
        assert nonzero_count > 0

    def test_landscape_custom_range(self):
        """Landscape with custom c_range works."""
        land = variance_landscape(c_range=[Rational(10), Rational(20)])
        assert len(land['Virasoro']) == 2
        assert len(land['W_3']) == 2


# ============================================================================
# 9. TestMultiChannelShadowMetric
# ============================================================================


class TestMultiChannelShadowMetric:
    """Multi-channel shadow metric construction."""

    def test_empty_channels(self):
        """Empty channel list returns rank 0."""
        result = multi_channel_shadow_metric([])
        assert result['rank'] == 0

    def test_single_channel_rank_1(self):
        """Single channel returns rank 1 with shadow metric."""
        ch = ChannelData(
            label='T', weight=2, kappa=c / 2,
            S4=Rational(10) / (c * (5 * c + 22)),
            Delta=Rational(40) / (5 * c + 22),
        )
        result = multi_channel_shadow_metric([ch])
        assert result['rank'] == 1
        assert 'shadow_metric_quartic' in result

    def test_single_channel_hessian(self):
        """Single-channel hessian is 1x1 with kappa entry."""
        ch = ChannelData(label='T', weight=2, kappa=Rational(5))
        result = multi_channel_shadow_metric([ch])
        H = result['hessian']
        assert H.shape == (1, 1)
        assert H[0, 0] == 5

    def test_two_channel_hessian_diagonal(self):
        """Two-channel hessian is diagonal with kappa entries."""
        ch_T = ChannelData(label='T', weight=2, kappa=c / 2)
        ch_W = ChannelData(label='W', weight=3, kappa=c / 3)
        result = multi_channel_shadow_metric([ch_T, ch_W])
        H = result['hessian']
        assert H.shape == (2, 2)
        assert simplify(H[0, 0] - c / 2) == 0
        assert simplify(H[1, 1] - c / 3) == 0
        assert H[0, 1] == 0

    def test_propagator_inverse_of_hessian(self):
        """Propagator entries are 1/kappa (diagonal)."""
        ch = ChannelData(label='T', weight=2, kappa=Rational(7))
        result = multi_channel_shadow_metric([ch])
        P = result['propagator']
        assert P[0, 0] == Rational(1, 7)

    def test_total_kappa_trace(self):
        """Total kappa equals trace of Hessian."""
        ch_T = ChannelData(label='T', weight=2, kappa=Rational(3))
        ch_W = ChannelData(label='W', weight=3, kappa=Rational(5))
        result = multi_channel_shadow_metric([ch_T, ch_W])
        assert result['total_kappa'] == 8


# ============================================================================
# 10. TestW3FullShadowMetric
# ============================================================================


class TestW3FullShadowMetric:
    """W_3 full 2D shadow metric with Lambda-exchange quartic."""

    def test_quartic_matrix_rank_1(self):
        """The quartic coupling matrix is rank 1 (Lambda exchange)."""
        result = w3_full_shadow_metric()
        assert result['rank_of_quartic'] == 1
        assert result['det_quartic_matrix'] == 0

    def test_quartic_geometric_progression(self):
        """Q_TTWW = Q_0 * alpha, Q_WWWW = Q_0 * alpha^2."""
        result = w3_full_shadow_metric()
        Q0 = result['Q0']
        alpha = result['alpha']
        assert simplify(result['Q_TTWW'] - Q0 * alpha) == 0
        assert simplify(result['Q_WWWW'] - Q0 * alpha ** 2) == 0

    def test_Q0_formula(self):
        """Q_0 = 10/[c(5c+22)]."""
        result = w3_full_shadow_metric()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(result['Q0'] - expected) == 0

    def test_alpha_formula(self):
        """alpha = 16/(5c+22)."""
        result = w3_full_shadow_metric()
        expected = Rational(16) / (5 * c + 22)
        assert simplify(result['alpha'] - expected) == 0

    def test_hessian_correct(self):
        """Hessian = diag(c/2, c/3)."""
        result = w3_full_shadow_metric()
        H = result['hessian']
        assert simplify(H[0, 0] - c / 2) == 0
        assert simplify(H[1, 1] - c / 3) == 0
        assert H[0, 1] == 0

    def test_propagator_correct(self):
        """Propagator = diag(2/c, 3/c)."""
        result = w3_full_shadow_metric()
        P = result['propagator']
        assert simplify(P[0, 0] - Rational(2) / c) == 0
        assert simplify(P[1, 1] - Rational(3) / c) == 0

    def test_factorization_vector(self):
        """Factorization vector is [1, alpha]."""
        result = w3_full_shadow_metric()
        v = result['factorization_vector']
        alpha = Rational(16) / (5 * c + 22)
        assert simplify(v[0] - 1) == 0
        assert simplify(v[1] - alpha) == 0


# ============================================================================
# 11. TestMixingPolynomialWN
# ============================================================================


class TestMixingPolynomialWN:
    """Mixing polynomial for general W_N."""

    def test_w2_is_virasoro_zero(self):
        """W_2 = Virasoro: single channel, P = 0."""
        P, zeros = mixing_polynomial_wN(2)
        assert P == S.Zero
        assert zeros == []

    def test_w3_matches_dedicated(self):
        """W_3 from general formula matches the dedicated function."""
        P_gen, zeros_gen = mixing_polynomial_wN(3)
        P_ded, zeros_ded = mixing_polynomial_w3()
        assert simplify(P_gen - P_ded) == 0

    def test_w4_polynomial_nonzero(self):
        """W_4 mixing polynomial is nonzero."""
        P, _ = mixing_polynomial_wN(4)
        assert P != S.Zero

    def test_invalid_N_raises(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            mixing_polynomial_wN(1)
        with pytest.raises(ValueError):
            mixing_polynomial_wN(0)

    def test_w5_polynomial_exists(self):
        """W_5 mixing polynomial is computable."""
        P, zeros = mixing_polynomial_wN(5)
        assert P != S.Zero


# ============================================================================
# 12. TestNumericalEvaluation
# ============================================================================


class TestNumericalEvaluation:
    """Numerical evaluation of W_3 variance at specific central charges."""

    def test_evaluate_w3_at_c2(self):
        """Evaluate W_3 variance at c=2."""
        result = evaluate_w3_variance(2)
        assert result['c'] == 2.0
        assert result['kappa_T'] == 1.0
        # P(2) = 25*4 + 200 - 428 = 100 + 200 - 428 = -128 < 0
        assert result['P(W_3)'] == pytest.approx(-128.0)

    def test_evaluate_w3_at_c13(self):
        """P(13) = 5097."""
        result = evaluate_w3_variance(13)
        assert result['P(W_3)'] == pytest.approx(5097.0)
        assert not result['is_enhanced']

    def test_evaluate_at_special_charges_returns_list(self):
        """evaluate_at_special_charges returns a non-empty list."""
        results = evaluate_at_special_charges()
        assert len(results) >= 4
        for r in results:
            assert 'c' in r
            assert 'delta_mix' in r
            assert 'P(W_3)' in r

    def test_kappa_values_at_c2(self):
        """At c=2: kappa_T = 1, kappa_W = 2/3."""
        result = evaluate_w3_variance(2)
        assert result['kappa_T'] == pytest.approx(1.0)
        assert result['kappa_W'] == pytest.approx(2.0 / 3.0)

    def test_ratio_difference_nonzero_generically(self):
        """f_T/kappa_T != f_W/kappa_W at generic c."""
        result = evaluate_w3_variance(10)
        assert abs(result['ratio_difference']) > 1e-12


# ============================================================================
# 13. TestBetaGamma
# ============================================================================


class TestBetaGamma:
    """Beta-gamma system with stratum separation."""

    def test_betagamma_rank_1(self):
        """Beta-gamma has rank 1 (after stratum separation)."""
        data = betagamma_propagator()
        assert data.rank == 1

    def test_betagamma_delta_zero(self):
        """Beta-gamma has delta_mix = 0 (stratum separation)."""
        data = betagamma_propagator()
        assert data.delta_mix == S.Zero

    def test_betagamma_depth_class_C(self):
        """Beta-gamma is class C (contact)."""
        data = betagamma_propagator()
        assert data.channels[0].depth_class == 'C'

    def test_betagamma_mu_vanishing(self):
        """f_quartic = 0 on the weight-changing line (mu_bg = 0)."""
        data = betagamma_propagator()
        assert data.channels[0].f_quartic == S.Zero


# ============================================================================
# 14. TestVirasoro
# ============================================================================


class TestVirasoro:
    """Virasoro channel data validation."""

    def test_virasoro_S4(self):
        """S4 = 10/[c(5c+22)] = Q^contact_Vir."""
        data = virasoro_propagator()
        ch = data.channels[0]
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(ch.S4 - expected) == 0

    def test_virasoro_Delta(self):
        """Delta = 8*kappa*S4 = 40/(5c+22)."""
        data = virasoro_propagator()
        ch = data.channels[0]
        expected = Rational(40) / (5 * c + 22)
        assert simplify(ch.Delta - expected) == 0

    def test_virasoro_f_quartic(self):
        """f_quartic = 4*S4*kappa = 20/(5c+22)."""
        data = virasoro_propagator()
        ch = data.channels[0]
        expected = Rational(20) / (5 * c + 22)
        assert simplify(ch.f_quartic - expected) == 0

    def test_virasoro_depth_class_M(self):
        """Virasoro is class M (mixed, infinite tower)."""
        data = virasoro_propagator()
        assert data.channels[0].depth_class == 'M'

    def test_virasoro_at_numeric_c(self):
        """Virasoro at c=26: kappa=13, S4=10/(26*152)."""
        data = virasoro_propagator(cc=Rational(26))
        ch = data.channels[0]
        assert ch.kappa == 13
        expected_S4 = Rational(10, 26 * 152)
        assert simplify(ch.S4 - expected_S4) == 0


# ============================================================================
# 15. TestPropagatorVarianceData
# ============================================================================


class TestPropagatorVarianceData:
    """PropagatorVarianceData methods."""

    def test_is_autonomous_true(self):
        """is_autonomous returns True when delta_mix = 0."""
        data = heisenberg_propagator()
        assert data.is_autonomous()

    def test_is_autonomous_false(self):
        """is_autonomous returns False when delta_mix != 0."""
        data = w3_propagator()
        assert not data.is_autonomous()

    def test_summary_contains_algebra_name(self):
        """summary() string includes the algebra name."""
        data = w3_propagator()
        s = data.summary()
        assert 'W_3' in s

    def test_summary_contains_channel_info(self):
        """summary() string includes channel labels."""
        data = w3_propagator()
        s = data.summary()
        assert 'T' in s
        assert 'W' in s

    def test_verify_cauchy_schwarz_heisenberg(self):
        """Cauchy-Schwarz verification passes for Heisenberg."""
        data = heisenberg_propagator()
        assert data.verify_cauchy_schwarz()
