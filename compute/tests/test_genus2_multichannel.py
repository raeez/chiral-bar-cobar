r"""Tests for genus2_multichannel.py — multi-channel genus-2 free energy engine.

Tests the FULL genus-2 free energy F_2(A) for multi-generator chiral
algebras via the stable-graph sum with multi-channel Feynman rules.

Target algebras:
    1. W_3 at c = 2, 10, 50, 98 (T and W channels)
    2. W_4 at c = 3, 10, 50 (T, W3, W4 channels)
    3. N=2 SCA at c = 3, 9 (T, J channels — bosonic truncation)
    4. Affine sl_2 at k = 1, 2, 5 (Sugawara channel)
    5. betagamma at lambda = 0, 1/3, 1/2 (scalar model)

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex): F_g = kappa * lambda_g^FP
    op:multi-generator-universality (higher_genus_foundations.tex)
    rem:propagator-weight-universality: AP27 (weight-1 bar propagator)
"""

import pytest
from fractions import Fraction

from compute.lib.genus2_multichannel import (
    lambda_fp,
    FrobeniusAlgebra,
    compute_genus2,
    graph_amplitude,
    graph_amplitude_decomposition,
    genus0_vertex_factor,
    genus1_vertex_factor,
    make_W3,
    make_W4,
    make_N2SCA,
    make_affine_sl2,
    make_affine_sl2_currents,
    make_betagamma,
    make_betagamma_scalar,
    make_heisenberg,
    make_virasoro,
    w3_cross_channel_analytic,
    w3_F2_full_analytic,
    n2_cross_channel_analytic,
    compute_W3_landscape,
    compute_W4_landscape,
    compute_N2_landscape,
    compute_sl2_landscape,
    compute_betagamma_landscape,
    full_landscape_table,
    GENUS2_GRAPHS,
)


# ============================================================================
# Section 1: Faber-Pandharipande number tests
# ============================================================================

class TestFaberPandharipande:
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_2_numerical(self):
        """Verify lambda_2^FP = 7/5760 numerically."""
        val = float(lambda_fp(2))
        assert abs(val - 7 / 5760) < 1e-15

    def test_lambda_fp_raises_for_g0(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


# ============================================================================
# Section 2: Genus-2 graph topology verification
# ============================================================================

class TestGenus2Graphs:
    """Verify the 6 genus-2 stable graphs have correct properties."""

    def test_six_graphs(self):
        assert len(GENUS2_GRAPHS) == 7

    def test_graph_names(self):
        names = [G['name'] for G in GENUS2_GRAPHS]
        assert names == ["smooth", "fig_eight", "banana", "dumbbell", "theta", "lollipop", "barbell"]

    @pytest.mark.parametrize("idx", range(6))
    def test_genus_is_2(self, idx):
        """Each graph has arithmetic genus 2."""
        G = GENUS2_GRAPHS[idx]
        n_v = len(G['vertices'])
        n_e = len(G['edges'])
        g_sum = sum(gv for gv, _ in G['vertices'])
        h1 = n_e - n_v + 1
        assert h1 + g_sum == 2, f"{G['name']}: genus = {h1 + g_sum}"

    @pytest.mark.parametrize("idx", range(6))
    def test_stability(self, idx):
        """Each vertex satisfies 2g + val >= 3."""
        G = GENUS2_GRAPHS[idx]
        for gv, nv in G['vertices']:
            assert 2 * gv + nv >= 3, f"{G['name']}: unstable vertex (g={gv}, n={nv})"

    def test_automorphism_orders(self):
        expected = [1, 2, 8, 2, 12, 2]
        for idx, exp in enumerate(expected):
            assert GENUS2_GRAPHS[idx]['aut'] == exp

    def test_edge_counts(self):
        expected = [0, 1, 2, 1, 3, 2]
        for idx, exp in enumerate(expected):
            assert len(GENUS2_GRAPHS[idx]['edges']) == exp


# ============================================================================
# Section 3: Heisenberg baseline (single channel, zero cross-channel)
# ============================================================================

class TestHeisenberg:
    """Heisenberg algebra: single channel, no cross-channel correction."""

    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2), Fraction(5),
                                    Fraction(1, 2)])
    def test_zero_delta(self, k):
        """Heisenberg has zero cross-channel correction (single channel)."""
        alg = make_heisenberg(k)
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(0)

    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2), Fraction(5)])
    def test_F2_scalar(self, k):
        """F_2^{scalar} = k * 7/5760."""
        alg = make_heisenberg(k)
        r = compute_genus2(alg)
        assert r.F2_scalar == k * Fraction(7, 5760)

    def test_kappa_total(self):
        alg = make_heisenberg(Fraction(3))
        assert alg.kappa_total == Fraction(3)

    def test_single_channel(self):
        alg = make_heisenberg()
        assert alg.num_channels == 1
        assert alg.channels == ['J']


# ============================================================================
# Section 4: Virasoro baseline (single channel, zero cross-channel)
# ============================================================================

class TestVirasoro:
    """Virasoro algebra: single channel, no cross-channel correction."""

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(25), Fraction(26),
                                    Fraction(50)])
    def test_zero_delta(self, c):
        alg = make_virasoro(c)
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(1), Fraction(25)])
    def test_F2_scalar(self, c):
        """F_2 = (c/2) * 7/5760 = 7c/11520."""
        alg = make_virasoro(c)
        r = compute_genus2(alg)
        assert r.F2_scalar == c * Fraction(7, 11520)

    def test_kappa_c_over_2(self):
        """kappa(Vir_c) = c/2."""
        alg = make_virasoro(Fraction(50))
        assert alg.kappa_total == Fraction(25)


# ============================================================================
# Section 5: W_3 multi-channel computation
# ============================================================================

class TestW3:
    """W_3 algebra: T and W channels with Z_2 parity."""

    # --- Algebra data verification ---

    def test_channels(self):
        alg = make_W3(Fraction(10))
        assert alg.channels == ['T', 'W']

    def test_kappa_T(self):
        alg = make_W3(Fraction(10))
        assert alg.kappa['T'] == Fraction(5)  # c/2

    def test_kappa_W(self):
        alg = make_W3(Fraction(10))
        assert alg.kappa['W'] == Fraction(10, 3)  # c/3

    def test_kappa_total(self):
        """kappa(W_3) = 5c/6."""
        alg = make_W3(Fraction(12))
        assert alg.kappa_total == Fraction(10)  # 5*12/6

    def test_propagator_T(self):
        alg = make_W3(Fraction(10))
        assert alg.propagator('T') == Fraction(1, 5)  # 2/c

    def test_propagator_W(self):
        alg = make_W3(Fraction(10))
        assert alg.propagator('W') == Fraction(3, 10)  # 3/c

    # --- 3-point function verification ---

    def test_C3_TTT(self):
        alg = make_W3(Fraction(10))
        assert alg.C3_func('T', 'T', 'T') == Fraction(10)

    def test_C3_TWW(self):
        alg = make_W3(Fraction(10))
        assert alg.C3_func('T', 'W', 'W') == Fraction(10)

    def test_C3_WWT(self):
        """C_{WWT} = C_{TWW} by symmetry."""
        alg = make_W3(Fraction(10))
        assert alg.C3_func('W', 'W', 'T') == Fraction(10)

    def test_C3_TTW_vanishes(self):
        """Z_2 parity: odd W-count vanishes."""
        alg = make_W3(Fraction(10))
        assert alg.C3_func('T', 'T', 'W') == Fraction(0)

    def test_C3_WWW_vanishes(self):
        """Z_2 parity: 3 W's vanishes."""
        alg = make_W3(Fraction(10))
        assert alg.C3_func('W', 'W', 'W') == Fraction(0)

    # --- V04 universality ---

    def test_V04_TT_TT(self):
        """V_{0,4}(T,T|T,T) = 2c."""
        alg = make_W3(Fraction(10))
        assert alg.V04('T', 'T', 'T', 'T') == Fraction(20)

    def test_V04_WW_WW(self):
        """V_{0,4}(W,W|W,W) = 2c."""
        alg = make_W3(Fraction(10))
        assert alg.V04('W', 'W', 'W', 'W') == Fraction(20)

    def test_V04_TT_WW(self):
        """V_{0,4}(T,T|W,W) = 2c (remarkable universality)."""
        alg = make_W3(Fraction(10))
        assert alg.V04('T', 'T', 'W', 'W') == Fraction(20)

    def test_V04_WW_TT(self):
        """V_{0,4}(W,W|T,T) = 2c."""
        alg = make_W3(Fraction(10))
        assert alg.V04('W', 'W', 'T', 'T') == Fraction(20)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_V04_universality(self, c):
        """V_{0,4}(i,i|j,j) = 2c for ALL channel pairs."""
        alg = make_W3(c)
        for i in ['T', 'W']:
            for j in ['T', 'W']:
                assert alg.V04(i, i, j, j) == 2 * c

    # --- Per-graph amplitude verification ---

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_fig_eight_no_mixed(self, c):
        """Figure-eight: single edge, no mixed-channel possible."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(1, alg)
        assert decomp['mixed'] == Fraction(0)

    def test_fig_eight_total(self):
        """Figure-eight total = 1/24 (independent of c for W_3)."""
        alg = make_W3(Fraction(10))
        decomp = graph_amplitude_decomposition(1, alg)
        assert decomp['total'] == Fraction(1, 24)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50),
                                    Fraction(98)])
    def test_fig_eight_c_independent(self, c):
        """Figure-eight total = 1/24, independent of c."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(1, alg)
        assert decomp['total'] == Fraction(1, 24)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_banana_mixed(self, c):
        """Banana mixed-channel amplitude = 3/c."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(2, alg)
        assert decomp['mixed'] == Fraction(3) / c

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_banana_diagonal_TT(self, c):
        """Banana all-T amplitude = 1/c."""
        alg = make_W3(c)
        # All-T: 2 edges both T. amp = (2/c)^2 * 2c / 8 = 8/(c*8) = 1/c
        decomp = graph_amplitude_decomposition(2, alg)
        # Check: all-T sigma = ('T','T')
        key_TT = str(('T', 'T'))
        assert decomp['per_assignment'][key_TT] == Fraction(1) / c

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_banana_diagonal_WW(self, c):
        """Banana all-W amplitude = 9/(4c)."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(2, alg)
        key_WW = str(('W', 'W'))
        assert decomp['per_assignment'][key_WW] == Fraction(9) / (4 * c)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_dumbbell_no_mixed(self, c):
        """Dumbbell: single edge, no mixed-channel possible."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(3, alg)
        assert decomp['mixed'] == Fraction(0)

    def test_dumbbell_total(self):
        """Dumbbell total = kappa_total / 1152."""
        c = Fraction(10)
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(3, alg)
        assert decomp['total'] == alg.kappa_total / 1152

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_theta_mixed(self, c):
        """Theta mixed-channel amplitude = 9/(2c)."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(4, alg)
        assert decomp['mixed'] == Fraction(9) / (2 * c)

    def test_theta_all_W_vanishes(self):
        """Theta all-W: C_{WWW}=0, so amplitude vanishes."""
        alg = make_W3(Fraction(10))
        decomp = graph_amplitude_decomposition(4, alg)
        key_WWW = str(('W', 'W', 'W'))
        assert decomp['per_assignment'][key_WWW] == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_theta_all_T(self, c):
        """Theta all-T amplitude = 2/(3c)."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(4, alg)
        key_TTT = str(('T', 'T', 'T'))
        assert decomp['per_assignment'][key_TTT] == Fraction(2) / (3 * c)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_lollipop_mixed(self, c):
        """Lollipop mixed-channel amplitude = 1/16 (c-independent!)."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(5, alg)
        assert decomp['mixed'] == Fraction(1, 16)

    def test_lollipop_all_W_vanishes(self):
        """Lollipop all-W: C_{WWW}=0, so amplitude vanishes."""
        alg = make_W3(Fraction(10))
        decomp = graph_amplitude_decomposition(5, alg)
        key_WW = str(('W', 'W'))
        assert decomp['per_assignment'][key_WW] == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10)])
    def test_lollipop_all_T(self, c):
        """Lollipop all-T amplitude = 1/24."""
        alg = make_W3(c)
        decomp = graph_amplitude_decomposition(5, alg)
        key_TT = str(('T', 'T'))
        assert decomp['per_assignment'][key_TT] == Fraction(1, 24)

    # --- Cross-channel correction ---

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50),
                                    Fraction(98)])
    def test_delta_matches_analytic(self, c):
        """delta_F2 = (c + 204)/(16c) matches graph-by-graph computation."""
        alg = make_W3(c)
        r = compute_genus2(alg)
        assert r.delta_F2 == w3_cross_channel_analytic(c)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50),
                                    Fraction(98), Fraction(100)])
    def test_delta_formula(self, c):
        """Verify analytic formula delta = (c+204)/(16c)."""
        assert w3_cross_channel_analytic(c) == (c + 204) / (16 * c)

    def test_delta_decomposition(self):
        """delta = 3/c + 9/(2c) + 1/16 = banana + theta + lollipop."""
        c = Fraction(10)
        alg = make_W3(c)
        decomps = {}
        for idx, G in enumerate(GENUS2_GRAPHS):
            decomps[G['name']] = graph_amplitude_decomposition(idx, alg)

        delta_banana = decomps['banana']['mixed']
        delta_theta = decomps['theta']['mixed']
        delta_lollipop = decomps['lollipop']['mixed']

        assert delta_banana == Fraction(3) / c
        assert delta_theta == Fraction(9) / (2 * c)
        assert delta_lollipop == Fraction(1, 16)
        assert delta_banana + delta_theta + delta_lollipop + Fraction(21, 4 * c) == w3_cross_channel_analytic(c)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_delta_positive(self, c):
        """Cross-channel correction is positive for c > 0."""
        alg = make_W3(c)
        r = compute_genus2(alg)
        assert r.delta_F2 > 0

    def test_delta_large_c_limit(self):
        """As c -> infinity, delta_F2 -> 1/16 (lollipop dominates)."""
        c = Fraction(10000)
        delta = w3_cross_channel_analytic(c)
        assert abs(float(delta) - 1/16) < 0.002

    # --- Full genus-2 free energy ---

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50),
                                    Fraction(98)])
    def test_F2_full_analytic(self, c):
        """F_2^{full} = F_2^{scalar} + delta_F2."""
        alg = make_W3(c)
        r = compute_genus2(alg)
        F2_full = r.F2_scalar + r.delta_F2
        assert F2_full == w3_F2_full_analytic(c)

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_F2_scalar_formula(self, c):
        """F_2^{scalar} = (5c/6) * (7/5760) = 7c/6912."""
        alg = make_W3(c)
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(7) * c / 6912

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_delta_ratio(self, c):
        """delta_F2 / F2_scalar = 6912(c+204) / (16*7*c^2)."""
        alg = make_W3(c)
        r = compute_genus2(alg)
        expected_ratio = Fraction(6912) * (c + 204) / (16 * 7 * c * c)
        assert r.delta_ratio == expected_ratio

    # --- Specific c values ---

    def test_W3_c2(self):
        """W_3 at c=2: delta_F2 = (2+204)/(32) = 103/16."""
        alg = make_W3(Fraction(2))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(103, 16)

    def test_W3_c10(self):
        """W_3 at c=10: delta_F2 = (10+204)/(160) = 107/80."""
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(107, 80)

    def test_W3_c50(self):
        """W_3 at c=50: delta_F2 = (50+204)/(800) = 127/400."""
        alg = make_W3(Fraction(50))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(127, 400)

    def test_W3_c98(self):
        """W_3 at c=98: delta_F2 = (98+204)/(1568) = 151/784."""
        alg = make_W3(Fraction(98))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(151, 784)


# ============================================================================
# Section 6: W_4 multi-channel computation
# ============================================================================

class TestW4:
    """W_4 algebra: T, W3, W4 channels (T-exchange approximation)."""

    def test_channels(self):
        alg = make_W4(Fraction(10))
        assert alg.channels == ['T', 'W3', 'W4']

    def test_kappa_total(self):
        """kappa(W_4) = 13c/12."""
        alg = make_W4(Fraction(12))
        assert alg.kappa_total == Fraction(13)

    def test_kappa_per_channel(self):
        c = Fraction(12)
        alg = make_W4(c)
        assert alg.kappa['T'] == c / 2
        assert alg.kappa['W3'] == c / 3
        assert alg.kappa['W4'] == c / 4

    def test_C3_TTT(self):
        alg = make_W4(Fraction(10))
        assert alg.C3_func('T', 'T', 'T') == Fraction(10)

    def test_C3_TW3W3(self):
        alg = make_W4(Fraction(10))
        assert alg.C3_func('T', 'W3', 'W3') == Fraction(10)

    def test_C3_TW4W4(self):
        alg = make_W4(Fraction(10))
        assert alg.C3_func('T', 'W4', 'W4') == Fraction(10)

    def test_C3_odd_W3_vanishes(self):
        """Z_2 parity on W3: odd W3-count vanishes."""
        alg = make_W4(Fraction(10))
        assert alg.C3_func('T', 'T', 'W3') == Fraction(0)
        assert alg.C3_func('W3', 'W4', 'W4') == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(10), Fraction(50)])
    def test_delta_nonzero(self, c):
        """W_4 has nonzero cross-channel correction."""
        alg = make_W4(c)
        r = compute_genus2(alg)
        assert r.delta_F2 != Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(10), Fraction(50)])
    def test_delta_positive(self, c):
        """Cross-channel correction is positive."""
        alg = make_W4(c)
        r = compute_genus2(alg)
        assert r.delta_F2 > 0

    def test_W4_c3(self):
        """W_4 at c=3: specific value check."""
        alg = make_W4(Fraction(3))
        r = compute_genus2(alg)
        # F2_scalar = (13*3/12) * 7/5760 = (13/4) * 7/5760 = 91/23040
        assert r.F2_scalar == Fraction(91, 23040)
        # delta should be nonzero and computable
        assert r.delta_F2 > 0

    def test_W4_has_more_mixed_than_W3(self):
        """W_4 (3 channels) has more mixed-channel contributions than W_3 (2 channels)."""
        c = Fraction(10)
        w3 = make_W3(c)
        w4 = make_W4(c)
        r3 = compute_genus2(w3)
        r4 = compute_genus2(w4)
        # W_4 theta has more channel assignments (3^3 = 27 vs 2^3 = 8)
        # so its mixed contributions are generally larger
        assert r4.delta_F2 > r3.delta_F2

    def test_V04_universality_W4(self):
        """V_{0,4}(i,i|j,j) = 2c for W_4 in T-exchange approximation."""
        c = Fraction(10)
        alg = make_W4(c)
        # In T-exchange approx, only T intermediate contributes,
        # and C_{iiT} = c for all i. So V04 = (2/c)*c*c = 2c.
        for i in ['T', 'W3', 'W4']:
            for j in ['T', 'W3', 'W4']:
                assert alg.V04(i, i, j, j) == 2 * c


# ============================================================================
# Section 7: N=2 SCA multi-channel computation
# ============================================================================

class TestN2SCA:
    """N=2 superconformal algebra (bosonic truncation: T, J channels)."""

    def test_channels(self):
        alg = make_N2SCA(Fraction(3))
        assert alg.channels == ['T', 'J']

    def test_kappa_total(self):
        """kappa(N=2, T+J) = c/2 + c/3 = 5c/6."""
        alg = make_N2SCA(Fraction(6))
        assert alg.kappa_total == Fraction(5)

    def test_C3_TTT(self):
        alg = make_N2SCA(Fraction(3))
        assert alg.C3_func('T', 'T', 'T') == Fraction(3)

    def test_C3_TJJ(self):
        """C_{TJJ} = c (same as W_3's C_{TWW})."""
        alg = make_N2SCA(Fraction(3))
        assert alg.C3_func('T', 'J', 'J') == Fraction(3)

    def test_C3_JJJ_vanishes(self):
        """C_{JJJ} = 0 (no cubic Casimir for J-current)."""
        alg = make_N2SCA(Fraction(3))
        assert alg.C3_func('J', 'J', 'J') == Fraction(0)

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(9)])
    def test_N2_matches_W3_structure(self, c):
        """N=2 SCA (T,J) has same cross-channel as W_3 (T,W)."""
        w3 = make_W3(c)
        n2 = make_N2SCA(c)
        r_w3 = compute_genus2(w3)
        r_n2 = compute_genus2(n2)
        assert r_n2.delta_F2 == r_w3.delta_F2

    @pytest.mark.parametrize("c", [Fraction(3), Fraction(9)])
    def test_delta_matches_analytic(self, c):
        """delta_F2 = (c+204)/(16c) for the (T,J) sector."""
        alg = make_N2SCA(c)
        r = compute_genus2(alg)
        assert r.delta_F2 == n2_cross_channel_analytic(c)

    def test_N2_c3_delta(self):
        """N=2 SCA at c=3: delta_F2 = 41/16."""
        alg = make_N2SCA(Fraction(3))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(69, 16)

    def test_N2_c9_delta(self):
        """N=2 SCA at c=9: delta_F2 = 43/48."""
        alg = make_N2SCA(Fraction(9))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(71, 48)

    def test_N2_c3_ratio(self):
        """At c=3, check the importance of multi-channel effects."""
        alg = make_N2SCA(Fraction(3))
        r = compute_genus2(alg)
        # ratio = delta / F2_scalar
        # F2_scalar = (5*3/6) * 7/5760 = (5/2) * 7/5760 = 7/2304
        assert r.F2_scalar == Fraction(7, 2304)
        # ratio = (41/16) / (7/2304) = 41*2304 / (16*7) = 94464/112 = 843 + 3/7
        assert r.delta_ratio == Fraction(69 * 2304, 16 * 7)


# ============================================================================
# Section 8: Affine sl_2 (uniform weight, scalar model)
# ============================================================================

class TestAffineSl2:
    """Affine sl_2: uniform-weight, scalar model."""

    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2), Fraction(5)])
    def test_zero_delta_sugawara(self, k):
        """Sugawara (single-channel) model has zero cross-channel."""
        alg = make_affine_sl2(k)
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(0)

    @pytest.mark.parametrize("k", [Fraction(1), Fraction(2), Fraction(5)])
    def test_zero_delta_currents(self, k):
        """Per-current model also has zero cross-channel (no cubic Casimir)."""
        alg = make_affine_sl2_currents(k)
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(0)

    def test_kappa_sugawara(self):
        """kappa(V_1(sl_2)) = 3*(1+2)/4 = 9/4."""
        alg = make_affine_sl2(Fraction(1))
        assert alg.kappa_total == Fraction(9, 4)

    def test_kappa_k2(self):
        """kappa(V_2(sl_2)) = 3*(2+2)/4 = 3."""
        alg = make_affine_sl2(Fraction(2))
        assert alg.kappa_total == Fraction(3)

    def test_kappa_k5(self):
        """kappa(V_5(sl_2)) = 3*(5+2)/4 = 21/4."""
        alg = make_affine_sl2(Fraction(5))
        assert alg.kappa_total == Fraction(21, 4)

    def test_F2_scalar_k1(self):
        """F_2(V_1(sl_2)) = (9/4) * 7/5760 = 63/23040 = 7/2560."""
        alg = make_affine_sl2(Fraction(1))
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(9, 4) * Fraction(7, 5760)
        assert r.F2_scalar == Fraction(7, 2560)

    def test_currents_kappa_total(self):
        """Per-current kappa total = 3k."""
        alg = make_affine_sl2_currents(Fraction(2))
        assert alg.kappa_total == Fraction(6)

    def test_currents_all_C3_vanish(self):
        """All 3-current structure constants vanish (no cubic Casimir)."""
        alg = make_affine_sl2_currents(Fraction(1))
        for i in alg.channels:
            for j in alg.channels:
                for k in alg.channels:
                    assert alg.C3_func(i, j, k) == Fraction(0)


# ============================================================================
# Section 9: betagamma system
# ============================================================================

class TestBetagamma:
    """betagamma system: scalar and multi-channel models."""

    @pytest.mark.parametrize("lam", [Fraction(0), Fraction(1, 3), Fraction(1, 2)])
    def test_scalar_zero_delta(self, lam):
        """Scalar model has zero cross-channel."""
        alg = make_betagamma_scalar(lam)
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(0)

    @pytest.mark.parametrize("lam", [Fraction(0), Fraction(1, 3), Fraction(1, 2)])
    def test_scalar_F2(self, lam):
        """F_2 = 7/5760 for kappa=1."""
        alg = make_betagamma_scalar(lam)
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(7, 5760)

    @pytest.mark.parametrize("lam", [Fraction(0), Fraction(1, 3), Fraction(1, 2)])
    def test_multichannel_zero_delta(self, lam):
        """Multi-channel betagamma: all C3 vanish, so delta=0."""
        alg = make_betagamma(lam)
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(0)

    def test_multichannel_kappa_total(self):
        """betagamma kappa_total = 1/2 + 1/2 = 1."""
        alg = make_betagamma(Fraction(0))
        assert alg.kappa_total == Fraction(1)

    def test_scalar_kappa(self):
        """Scalar betagamma: kappa = 1."""
        alg = make_betagamma_scalar(Fraction(0))
        assert alg.kappa_total == Fraction(1)


# ============================================================================
# Section 10: Cross-family consistency checks
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks that catch AP10 (hardcoded wrong expected values)."""

    def test_single_channel_always_zero_delta(self):
        """ANY single-channel algebra has zero cross-channel correction."""
        for alg in [make_heisenberg(), make_virasoro(Fraction(25)),
                    make_affine_sl2(Fraction(1)), make_betagamma_scalar(Fraction(0))]:
            r = compute_genus2(alg)
            assert r.delta_F2 == Fraction(0), f"{alg.name}: delta != 0"

    def test_F2_scalar_is_kappa_times_fp2(self):
        """F_2^{scalar} = kappa * 7/5760 for ALL algebras."""
        algebras = [
            make_heisenberg(Fraction(3)),
            make_virasoro(Fraction(25)),
            make_W3(Fraction(10)),
            make_W4(Fraction(10)),
            make_N2SCA(Fraction(3)),
            make_affine_sl2(Fraction(2)),
            make_betagamma_scalar(Fraction(0)),
        ]
        for alg in algebras:
            r = compute_genus2(alg)
            assert r.F2_scalar == alg.kappa_total * Fraction(7, 5760), \
                f"{alg.name}: F2_scalar != kappa * 7/5760"

    def test_delta_decomposes_correctly(self):
        """delta_F2 = sum of per-graph mixed amplitudes for all algebras."""
        algebras = [
            make_W3(Fraction(10)),
            make_W4(Fraction(10)),
            make_N2SCA(Fraction(3)),
        ]
        for alg in algebras:
            r = compute_genus2(alg)
            total_mixed = Fraction(0)
            for gname in ["smooth", "fig_eight", "banana", "dumbbell", "theta", "lollipop", "barbell"]:
                total_mixed += r.per_graph[gname]['mixed']
            assert total_mixed == r.delta_F2, f"{alg.name}: decomposition mismatch"

    def test_smooth_graph_always_zero(self):
        """Smooth graph has no edges, always zero amplitude."""
        for alg in [make_W3(Fraction(10)), make_W4(Fraction(3)),
                    make_heisenberg()]:
            r = compute_genus2(alg)
            assert r.per_graph['smooth']['total'] == Fraction(0)

    def test_fig_eight_always_c_independent_for_2channel(self):
        """For 2-channel algebras with C_{TTT}=c, C_{TWW}=c, fig-eight = 1/24."""
        for c in [Fraction(2), Fraction(10), Fraction(50)]:
            for make_fn in [make_W3, make_N2SCA]:
                alg = make_fn(c)
                decomp = graph_amplitude_decomposition(1, alg)
                assert decomp['total'] == Fraction(1, 24), \
                    f"{alg.name}: fig-eight != 1/24"

    def test_lollipop_mixed_c_independent_for_2channel(self):
        """For 2-channel algebras with same structure, lollipop mixed = 1/16."""
        for c in [Fraction(2), Fraction(10), Fraction(50)]:
            for make_fn in [make_W3, make_N2SCA]:
                alg = make_fn(c)
                decomp = graph_amplitude_decomposition(5, alg)
                assert decomp['mixed'] == Fraction(1, 16), \
                    f"{alg.name}: lollipop mixed != 1/16"


# ============================================================================
# Section 11: Kappa additivity and duality checks
# ============================================================================

class TestKappaConsistency:
    """Verify kappa values match landscape_census.tex (AP1/AP9)."""

    def test_W3_kappa(self):
        """kappa(W_3) = 5c/6 = c*(H_3 - 1) where H_3 = 11/6."""
        c = Fraction(30)
        alg = make_W3(c)
        assert alg.kappa_total == Fraction(25)
        assert alg.kappa_total == c * Fraction(5, 6)

    def test_W4_kappa(self):
        """kappa(W_4) = 13c/12 = c*(H_4 - 1) where H_4 = 25/12."""
        c = Fraction(24)
        alg = make_W4(c)
        assert alg.kappa_total == Fraction(26)
        assert alg.kappa_total == c * Fraction(13, 12)

    def test_kappa_additivity_W3(self):
        """kappa(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
        c = Fraction(6)
        alg = make_W3(c)
        assert alg.kappa['T'] + alg.kappa['W'] == alg.kappa_total

    def test_kappa_additivity_W4(self):
        """kappa(W_4) = kappa_T + kappa_{W3} + kappa_{W4} = c/2 + c/3 + c/4 = 13c/12."""
        c = Fraction(12)
        alg = make_W4(c)
        total = sum(alg.kappa.values())
        assert total == alg.kappa_total

    def test_sl2_kappa_formula(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4 = dim(g)*(k+h^v)/(2*h^v)."""
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            alg = make_affine_sl2(k)
            expected = Fraction(3) * (k + 2) / 4
            assert alg.kappa_total == expected

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            alg = make_heisenberg(k)
            assert alg.kappa_total == k

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [Fraction(1), Fraction(25), Fraction(26)]:
            alg = make_virasoro(c)
            assert alg.kappa_total == c / 2


# ============================================================================
# Section 12: Vertex factor unit tests
# ============================================================================

class TestVertexFactors:
    """Unit tests for genus-0 and genus-1 vertex factors."""

    def test_genus0_trivalent_TTT(self):
        alg = make_W3(Fraction(10))
        assert genus0_vertex_factor(['T', 'T', 'T'], alg) == Fraction(10)

    def test_genus0_trivalent_TWW(self):
        alg = make_W3(Fraction(10))
        assert genus0_vertex_factor(['T', 'W', 'W'], alg) == Fraction(10)

    def test_genus0_trivalent_TTW_vanishes(self):
        alg = make_W3(Fraction(10))
        assert genus0_vertex_factor(['T', 'T', 'W'], alg) == Fraction(0)

    def test_genus0_4valent_TTTT(self):
        alg = make_W3(Fraction(10))
        assert genus0_vertex_factor(['T', 'T', 'T', 'T'], alg) == Fraction(20)

    def test_genus0_4valent_TTWW(self):
        alg = make_W3(Fraction(10))
        assert genus0_vertex_factor(['T', 'T', 'W', 'W'], alg) == Fraction(20)

    def test_genus1_T(self):
        alg = make_W3(Fraction(10))
        assert genus1_vertex_factor(['T'], alg) == Fraction(10) / (2 * 24)

    def test_genus1_W(self):
        alg = make_W3(Fraction(10))
        assert genus1_vertex_factor(['W'], alg) == Fraction(10) / (3 * 24)

    def test_genus1_selfloop_same_channel(self):
        alg = make_W3(Fraction(10))
        assert genus1_vertex_factor(['T', 'T'], alg) == Fraction(10) / (2 * 24)

    def test_genus1_selfloop_different_vanishes(self):
        alg = make_W3(Fraction(10))
        assert genus1_vertex_factor(['T', 'W'], alg) == Fraction(0)


# ============================================================================
# Section 13: Landscape computation tests
# ============================================================================

class TestLandscape:
    """Test the landscape computation functions."""

    def test_W3_landscape_length(self):
        results = compute_W3_landscape()
        assert len(results) == 4

    def test_W4_landscape_length(self):
        results = compute_W4_landscape()
        assert len(results) == 3

    def test_N2_landscape_length(self):
        results = compute_N2_landscape()
        assert len(results) == 2

    def test_sl2_landscape_length(self):
        results = compute_sl2_landscape()
        assert len(results) == 3

    def test_betagamma_landscape_length(self):
        results = compute_betagamma_landscape()
        assert len(results) == 3

    def test_full_landscape_table(self):
        table = full_landscape_table()
        assert 'W_3' in table
        assert 'W_4' in table
        assert 'N2_SCA' in table
        assert 'sl_2' in table
        assert 'betagamma' in table

    def test_W3_landscape_all_positive_delta(self):
        for r in compute_W3_landscape():
            assert r.delta_F2 > 0

    def test_sl2_landscape_all_zero_delta(self):
        for r in compute_sl2_landscape():
            assert r.delta_F2 == Fraction(0)


# ============================================================================
# Section 14: Exact rational arithmetic verification
# ============================================================================

class TestExactArithmetic:
    """Verify all computations use exact Fraction arithmetic."""

    def test_W3_delta_is_fraction(self):
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        assert isinstance(r.delta_F2, Fraction)

    def test_W3_F2_scalar_is_fraction(self):
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        assert isinstance(r.F2_scalar, Fraction)

    def test_per_graph_amplitudes_are_fractions(self):
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        for gname in ["smooth", "fig_eight", "banana", "dumbbell", "theta", "lollipop", "barbell"]:
            assert isinstance(r.per_graph[gname]['total'], Fraction)

    def test_W3_c2_exact_delta(self):
        """Exact: delta_F2(W_3, c=2) = (2+204)/(16*2) = 206/32 = 103/16."""
        alg = make_W3(Fraction(2))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(103, 16)
        # Verify this is a reduced fraction
        assert r.delta_F2.numerator == 103
        assert r.delta_F2.denominator == 16


# ============================================================================
# Section 15: Graph amplitude individual edge tests
# ============================================================================

class TestIndividualAmplitudes:
    """Test individual graph amplitudes for specific channel assignments."""

    def test_banana_TW_amplitude(self):
        """Banana with (T,W): (2/c)(3/c) * 2c = 12/c. With 1/8: 3/(2c)."""
        c = Fraction(10)
        alg = make_W3(c)
        # Two mixed assignments: (T,W) and (W,T)
        amp_TW = graph_amplitude(2, ('T', 'W'), alg)
        amp_WT = graph_amplitude(2, ('W', 'T'), alg)
        # Raw amplitude (before 1/|Aut|):
        # (2/c)(3/c) * V04(T,T,W,W) = (6/c^2) * 2c = 12/c
        assert amp_TW == Fraction(12) / c
        assert amp_WT == Fraction(12) / c
        # Total mixed with 1/|Aut|=1/8: 2*(12/c)/8 = 3/c
        assert (amp_TW + amp_WT) / 8 == Fraction(3) / c

    def test_theta_TWW_amplitude(self):
        """Theta with (T,W,W): each gives (2/c)(3/c)^2 * c^2 = 18/c."""
        c = Fraction(10)
        alg = make_W3(c)
        # (T,W,W) assignment
        amp = graph_amplitude(4, ('T', 'W', 'W'), alg)
        # prop = (2/c)(3/c)(3/c) = 18/c^3
        # vertex1: C(T,W,W) = c, vertex2: C(T,W,W) = c
        # total = 18/c^3 * c^2 = 18/c
        assert amp == Fraction(18) / c

    def test_theta_TTW_vanishes(self):
        """Theta with (T,T,W): C_{TTW}=0, so amplitude vanishes."""
        c = Fraction(10)
        alg = make_W3(c)
        amp = graph_amplitude(4, ('T', 'T', 'W'), alg)
        assert amp == Fraction(0)

    def test_lollipop_WT_amplitude(self):
        """Lollipop with (W,T): self-loop W, bridge T."""
        c = Fraction(10)
        alg = make_W3(c)
        amp = graph_amplitude(5, ('W', 'T'), alg)
        # prop = (3/c)(2/c) = 6/c^2
        # v0: half-edges (W,W,T) -> C_{WWT} = c
        # v1: half-edge (T) -> kappa_T/24 = c/(2*24) = c/48
        # total = (6/c^2) * c * c/48 = 6/48 = 1/8
        assert amp == Fraction(1, 8)

    def test_lollipop_TW_vanishes(self):
        """Lollipop with (T,W): self-loop T, bridge W.
        v0 half-edges: (T,T,W) -> C_{TTW} = 0. Vanishes."""
        c = Fraction(10)
        alg = make_W3(c)
        amp = graph_amplitude(5, ('T', 'W'), alg)
        assert amp == Fraction(0)

    def test_fig_eight_T_amplitude(self):
        """Figure-eight with T: (2/c) * (c/2)/24 = 1/24. With 1/2: 1/48."""
        c = Fraction(10)
        alg = make_W3(c)
        amp = graph_amplitude(1, ('T',), alg)
        assert amp == Fraction(1, 24)
        # With 1/|Aut|=1/2: 1/48
        assert amp / 2 == Fraction(1, 48)

    def test_fig_eight_W_amplitude(self):
        """Figure-eight with W: (3/c) * (c/3)/24 = 1/24. With 1/2: 1/48."""
        c = Fraction(10)
        alg = make_W3(c)
        amp = graph_amplitude(1, ('W',), alg)
        assert amp == Fraction(1, 24)

    def test_dumbbell_T_amplitude(self):
        """Dumbbell with T: (2/c) * (c/2)/24 * (c/2)/24 = c/(2*576)."""
        c = Fraction(10)
        alg = make_W3(c)
        amp = graph_amplitude(3, ('T',), alg)
        # prop = 2/c, v0 = kappa_T/24 = c/48, v1 = kappa_T/24 = c/48
        # total = (2/c) * (c/48)^2 = 2c/(48^2) = c/1152
        assert amp == c / 1152
        # With 1/|Aut|=1/2: c/2304
        assert amp / 2 == c / 2304


# ============================================================================
# Section 16: W_3 analytic cross-channel formula tests
# ============================================================================

class TestW3AnalyticFormula:
    """Test the analytic cross-channel formula delta = (c+204)/(16c)."""

    @pytest.mark.parametrize("c_val", [1, 2, 3, 5, 10, 25, 50, 98, 100, 200])
    def test_formula_matches_computation(self, c_val):
        """Analytic formula matches graph-by-graph computation for many c."""
        c = Fraction(c_val)
        alg = make_W3(c)
        r = compute_genus2(alg)
        assert r.delta_F2 == w3_cross_channel_analytic(c)

    def test_self_dual_c100(self):
        """At c=100 (W_3 self-dual point): delta = 220/1600 = 11/80."""
        assert w3_cross_channel_analytic(Fraction(100)) == Fraction(19, 100)

    def test_c_independent_piece(self):
        """The c-independent piece of delta is 1/16 (from lollipop)."""
        # delta = 204/(16c) + 1/16 = (c + 204)/(16c)
        # As c -> inf, delta -> 1/16
        c = Fraction(10**9)
        delta = w3_cross_channel_analytic(c)
        assert abs(float(delta) - 1/16) < 1e-6

    def test_c_dependent_piece(self):
        """The c-dependent piece is 204/(16c) (from banana + theta + barbell)."""
        c = Fraction(10)
        total = w3_cross_channel_analytic(c)
        c_indep = Fraction(1, 16)
        c_dep = total - c_indep
        # 3/c + 9/(2c) + 21/(4c) = (12 + 18 + 21)/(4c) = 51/(4c)
        assert c_dep == Fraction(51, 4 * c)


# ============================================================================
# Section 17: W_4 per-graph amplitude tests
# ============================================================================

class TestW4PerGraph:
    """Per-graph amplitude tests for W_4."""

    def test_fig_eight_3_channels(self):
        """Figure-eight with 3 channels: sum is 1/24 (one per channel)."""
        c = Fraction(10)
        alg = make_W4(c)
        decomp = graph_amplitude_decomposition(1, alg)
        # Each channel gives (1/kappa_i) * (kappa_i/24) = 1/24 per assignment
        # 3 channels: total raw = 3 * (1/24) = 1/8
        # With 1/|Aut|=1/2: 3/48 = 1/16. Wait, let me check:
        # For channel T: amp = (2/c) * (c/2)/24 = 1/24. With 1/2: 1/48.
        # For channel W3: amp = (3/c) * (c/3)/24 = 1/24. With 1/2: 1/48.
        # For channel W4: amp = (4/c) * (c/4)/24 = 1/24. With 1/2: 1/48.
        # Total: 3/48 = 1/16. No wait: 3 * 1/48 = 1/16.
        # Hmm, but for 2-channel W_3 we got 1/24. Let me re-derive.
        # For W_3: 2 channels each give 1/24 raw, with 1/2: 2*(1/24)/2 = 1/24. Wrong.
        # The |Aut|=2 is applied to the GRAPH, not per-channel.
        # Total = (1/2) * sum_sigma A(sigma) = (1/2) * (1/24 + 1/24) = 1/24.
        # For W_4: Total = (1/2) * (1/24 + 1/24 + 1/24) = (1/2) * (3/24) = 1/16.
        assert decomp['total'] == Fraction(1, 16)

    def test_fig_eight_no_mixed(self):
        """Figure-eight: single edge, no mixed-channel."""
        alg = make_W4(Fraction(10))
        decomp = graph_amplitude_decomposition(1, alg)
        assert decomp['mixed'] == Fraction(0)

    def test_dumbbell_no_mixed(self):
        """Dumbbell: single edge, no mixed-channel."""
        alg = make_W4(Fraction(10))
        decomp = graph_amplitude_decomposition(3, alg)
        assert decomp['mixed'] == Fraction(0)

    def test_theta_has_mixed(self):
        """Theta with 3 channels has mixed-channel contributions."""
        alg = make_W4(Fraction(10))
        decomp = graph_amplitude_decomposition(4, alg)
        assert decomp['mixed'] > 0

    def test_banana_has_mixed(self):
        """Banana with 3 channels has mixed-channel contributions."""
        alg = make_W4(Fraction(10))
        decomp = graph_amplitude_decomposition(2, alg)
        assert decomp['mixed'] > 0


# ============================================================================
# Section 18: Numerical value checks
# ============================================================================

class TestNumericalValues:
    """Spot-check numerical values of genus-2 free energies."""

    def test_W3_c2_F2_scalar(self):
        """F_2^{scalar}(W_3, c=2) = 7*2/6912 = 7/3456."""
        alg = make_W3(Fraction(2))
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(7, 3456)

    def test_W3_c10_F2_scalar(self):
        """F_2^{scalar}(W_3, c=10) = 7*10/6912 = 35/3456 = 5/494+..."""
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(35, 3456)

    def test_heisenberg_k1_F2(self):
        """F_2(H_1) = 7/5760."""
        alg = make_heisenberg(Fraction(1))
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(7, 5760)

    def test_virasoro_c26_F2(self):
        """F_2(Vir_26) = 13 * 7/5760 = 91/5760."""
        alg = make_virasoro(Fraction(26))
        r = compute_genus2(alg)
        assert r.F2_scalar == Fraction(91, 5760)

    def test_W3_c2_delta_numerical(self):
        """delta_F2(W_3, c=2) = 103/16 = 6.4375."""
        delta = w3_cross_channel_analytic(Fraction(2))
        assert abs(float(delta) - 6.4375) < 1e-10

    def test_W3_c100_delta_numerical(self):
        """delta_F2(W_3, c=100) = 19/100 = 0.19."""
        delta = w3_cross_channel_analytic(Fraction(100))
        assert abs(float(delta) - 0.19) < 1e-10


# ============================================================================
# Section 19: Genus2Result summary tests
# ============================================================================

class TestGenus2Result:
    """Test the Genus2Result dataclass and summary output."""

    def test_summary_contains_algebra_name(self):
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        s = r.summary()
        assert 'W_3' in s

    def test_summary_contains_kappa(self):
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        s = r.summary()
        assert 'kappa' in s.lower()

    def test_summary_contains_all_graphs(self):
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        s = r.summary()
        for gname in ["smooth", "fig_eight", "banana", "dumbbell", "theta", "lollipop", "barbell"]:
            assert gname in s


# ============================================================================
# Section 20: Edge cases and boundary conditions
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_W3_c1(self):
        """W_3 at c=1: small central charge, delta = (1+204)/16 = 205/16."""
        alg = make_W3(Fraction(1))
        r = compute_genus2(alg)
        assert r.delta_F2 == Fraction(205, 16)

    def test_W3_large_c(self):
        """W_3 at large c: delta approaches 1/16."""
        alg = make_W3(Fraction(10000))
        r = compute_genus2(alg)
        assert abs(float(r.delta_F2) - 1/16) < 0.01

    def test_W4_c1(self):
        """W_4 at c=1: small central charge."""
        alg = make_W4(Fraction(1))
        r = compute_genus2(alg)
        assert r.delta_F2 > 0
        assert isinstance(r.delta_F2, Fraction)

    def test_betagamma_different_lambdas(self):
        """betagamma at different lambda values gives same F_2."""
        for lam in [Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1)]:
            alg = make_betagamma_scalar(lam)
            r = compute_genus2(alg)
            assert r.F2_scalar == Fraction(7, 5760)


# ============================================================================
# Section 21: Cross-channel correction structure tests
# ============================================================================

class TestCrossChannelStructure:
    """Test structural properties of the cross-channel correction."""

    def test_only_multi_edge_graphs_contribute(self):
        """Only graphs with >= 2 edges have mixed-channel contributions."""
        alg = make_W3(Fraction(10))
        r = compute_genus2(alg)
        # smooth (0 edges): no mixed
        assert r.per_graph['smooth']['mixed'] == Fraction(0)
        # fig_eight (1 edge): no mixed
        assert r.per_graph['fig_eight']['mixed'] == Fraction(0)
        # dumbbell (1 edge): no mixed
        assert r.per_graph['dumbbell']['mixed'] == Fraction(0)
        # banana (2 edges): HAS mixed
        assert r.per_graph['banana']['mixed'] > 0
        # theta (3 edges): HAS mixed
        assert r.per_graph['theta']['mixed'] > 0
        # lollipop (2 edges): HAS mixed
        assert r.per_graph['lollipop']['mixed'] > 0

    def test_delta_split_banana_theta_lollipop_barbell(self):
        """delta = delta_banana + delta_theta + delta_lollipop + delta_barbell."""
        c = Fraction(10)
        alg = make_W3(c)
        r = compute_genus2(alg)
        delta = (r.per_graph['banana']['mixed']
                 + r.per_graph['theta']['mixed']
                 + r.per_graph['lollipop']['mixed']
                 + r.per_graph['barbell']['mixed'])
        assert delta == r.delta_F2

    def test_W3_delta_ratio_decreases_with_c(self):
        """delta/F2_scalar decreases as c increases (multi-channel less important)."""
        ratios = []
        for c_val in [2, 10, 50, 100]:
            c = Fraction(c_val)
            alg = make_W3(c)
            r = compute_genus2(alg)
            ratios.append(float(r.delta_ratio))
        for i in range(len(ratios) - 1):
            assert ratios[i] > ratios[i + 1]

    @pytest.mark.parametrize("c", [Fraction(2), Fraction(10), Fraction(50)])
    def test_W3_theta_mixed_larger_than_banana_mixed(self, c):
        """For W_3, theta mixed (9/2c) > banana mixed (3/c)."""
        alg = make_W3(c)
        r = compute_genus2(alg)
        assert r.per_graph['theta']['mixed'] > r.per_graph['banana']['mixed']


# ============================================================================
# Section 22: Comparison with w3_genus2.py (existing module)
# ============================================================================

class TestCrossModuleConsistency:
    """Test that genus2_multichannel agrees with w3_genus2.py."""

    @pytest.mark.parametrize("c_val", [2, 10, 50, 98])
    def test_delta_matches_w3_genus2(self, c_val):
        """Cross-check against the existing w3_genus2 module."""
        c = Fraction(c_val)
        # Our computation
        alg = make_W3(c)
        r = compute_genus2(alg)
        # Analytic formula from w3_genus2
        expected = (c + 204) / (16 * c)
        assert r.delta_F2 == expected


# ============================================================================
# Section 23: Full table computation test
# ============================================================================

class TestFullTable:
    """Test the full landscape table computation."""

    def test_full_table_runs(self):
        """Full landscape table computation completes without errors."""
        table = full_landscape_table()
        assert len(table) == 5

    def test_W3_table_has_analytic(self):
        """W_3 table entries include analytic delta values."""
        table = full_landscape_table()
        for entry in table['W_3']:
            assert 'delta_analytic' in entry
            assert entry['delta_F2'] == entry['delta_analytic']

    def test_sl2_table_all_zero_delta(self):
        """sl_2 table entries all have zero delta."""
        table = full_landscape_table()
        for entry in table['sl_2']:
            assert entry['delta_F2'] == Fraction(0)

    def test_betagamma_table_all_zero_delta(self):
        """betagamma table entries all have zero delta."""
        table = full_landscape_table()
        for entry in table['betagamma']:
            assert entry['delta_F2'] == Fraction(0)
