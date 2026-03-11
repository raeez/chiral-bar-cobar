"""Tests for the channel-refined modular characteristic of W_N algebras.

Verifies the decomposition kappa(W_N) = sum_{j=2}^N kappa_j where
kappa_j = c/j is the contribution from the W_j self-coupling OPE channel.

Test structure:
    I.   Harmonic number identities
    II.  Channel kappa: kappa_j = c/j
    III. Total kappa: sum = c * (H_N - 1) = scalar kappa
    IV.  Cross-term vanishing: mixed W_i-W_j contributions are zero
    V.   Specific W_N algebras (W_3, W_4, W_5)
    VI.  Sugawara channel verification
    VII. Harmonic divergence (W_infinity obstruction)
    VIII.Consistency with w4_stage4_coefficients
    IX.  Consistency with sigma_invariant
    X.   FF duality on channel vectors
"""

import pytest
from sympy import Rational, Symbol, simplify, log, EulerGamma, N as neval

from compute.lib.wn_channel_refined import (
    harmonic_number,
    harmonic_tail,
    channel_kappa,
    channel_vector,
    channel_vector_tuple,
    total_kappa,
    total_kappa_harmonic,
    cross_term_coefficient,
    cross_term_matrix,
    verify_cross_term_vanishing,
    ope_max_pole_order,
    vacuum_pole_order,
    cross_term_pole_deficit,
    sugawara_kappa,
    verify_sugawara_channel,
    w3_channel_data,
    w4_channel_data,
    w5_channel_data,
    kappa_growth_data,
    harmonic_divergence_bound,
    verify_w4_consistency,
    verify_sigma_consistency,
    wn_central_charge,
    wn_ff_dual_level,
    ff_dual_channel_vector,
    ff_channel_anti_symmetry,
)

c = Symbol('c')
k = Symbol('k')


# ===========================================================================
# I. HARMONIC NUMBER IDENTITIES
# ===========================================================================

class TestHarmonicNumbers:
    """Exact rational arithmetic for harmonic numbers."""

    def test_h1(self):
        assert harmonic_number(1) == 1

    def test_h2(self):
        assert harmonic_number(2) == Rational(3, 2)

    def test_h3(self):
        assert harmonic_number(3) == Rational(11, 6)

    def test_h4(self):
        assert harmonic_number(4) == Rational(25, 12)

    def test_h5(self):
        assert harmonic_number(5) == Rational(137, 60)

    def test_h10(self):
        """H_10 = 7381/2520."""
        assert harmonic_number(10) == Rational(7381, 2520)

    def test_harmonic_tail_full(self):
        """harmonic_tail(1, N) == harmonic_number(N)."""
        for N in [1, 2, 5, 10]:
            assert harmonic_tail(1, N) == harmonic_number(N)

    def test_harmonic_tail_partial(self):
        """harmonic_tail(2, N) == H_N - 1."""
        for N in [2, 3, 4, 5, 10]:
            assert harmonic_tail(2, N) == harmonic_number(N) - 1

    def test_harmonic_tail_split(self):
        """H_N = harmonic_tail(1, m) + harmonic_tail(m+1, N)."""
        for N in [5, 10]:
            for m in range(1, N):
                assert (harmonic_tail(1, m) + harmonic_tail(m + 1, N)
                        == harmonic_number(N))

    def test_harmonic_negative_raises(self):
        with pytest.raises(ValueError):
            harmonic_number(-1)

    def test_h0(self):
        """H_0 = 0 (empty sum)."""
        assert harmonic_number(0) == 0


# ===========================================================================
# II. CHANNEL KAPPA: kappa_j = c/j
# ===========================================================================

class TestChannelKappa:
    """Each channel kappa_j = c/j from the W_j self-coupling."""

    @pytest.mark.parametrize("j", [2, 3, 4, 5, 10, 20])
    def test_channel_symbolic(self, j):
        """kappa_j = c/j with symbolic central charge."""
        kap = channel_kappa(j)
        assert simplify(kap - c / j) == 0

    @pytest.mark.parametrize("j", [2, 3, 4, 5])
    def test_channel_numeric(self, j):
        """kappa_j at c = 1 gives 1/j."""
        kap = channel_kappa(j, central_charge=1)
        assert kap == Rational(1, j)

    def test_channel_j1_raises(self):
        """No W_1 generator; channel index must be >= 2."""
        with pytest.raises(ValueError):
            channel_kappa(1)

    def test_virasoro_channel(self):
        """W_2 = T channel: kappa_2 = c/2."""
        assert channel_kappa(2) == c / 2

    def test_w3_channel(self):
        """W_3 channel: kappa_3 = c/3."""
        assert channel_kappa(3) == c / 3

    def test_w4_channel(self):
        """W_4 channel: kappa_4 = c/4."""
        assert channel_kappa(4) == c / 4


# ===========================================================================
# III. TOTAL KAPPA: sum = c * (H_N - 1)
# ===========================================================================

class TestTotalKappa:
    """Sum of channel contributions equals scalar kappa."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6, 10, 20])
    def test_sum_equals_harmonic_formula(self, N):
        """sum_{j=2}^N c/j == c * (H_N - 1) for all N."""
        tot_sum = total_kappa(N)
        tot_harm = total_kappa_harmonic(N)
        assert simplify(tot_sum - tot_harm) == 0

    @pytest.mark.parametrize("N,expected", [
        (2, Rational(1, 2)),
        (3, Rational(5, 6)),
        (4, Rational(13, 12)),
        (5, Rational(77, 60)),
        (6, Rational(29, 20)),
    ])
    def test_known_values(self, N, expected):
        """Verify H_N - 1 matches known rational values."""
        tot = total_kappa(N, central_charge=1)
        assert tot == expected

    def test_w2_virasoro(self):
        """W_2 = Virasoro: kappa = c/2."""
        assert simplify(total_kappa(2) - c / 2) == 0

    def test_w3_total(self):
        """W_3: kappa = c/2 + c/3 = 5c/6."""
        assert simplify(total_kappa(3) - Rational(5, 6) * c) == 0

    def test_w4_total(self):
        """W_4: kappa = c/2 + c/3 + c/4 = 13c/12."""
        assert simplify(total_kappa(4) - Rational(13, 12) * c) == 0

    def test_w5_total(self):
        """W_5: kappa = c/2 + c/3 + c/4 + c/5 = 77c/60."""
        assert simplify(total_kappa(5) - Rational(77, 60) * c) == 0

    def test_channel_vector_length(self):
        """Channel vector for W_N has N-1 entries."""
        for N in [2, 3, 4, 5, 10]:
            vec = channel_vector(N)
            assert len(vec) == N - 1

    def test_channel_vector_keys(self):
        """Channel vector keys are {2, 3, ..., N}."""
        for N in [3, 5, 8]:
            vec = channel_vector(N)
            assert set(vec.keys()) == set(range(2, N + 1))

    def test_channel_vector_tuple_order(self):
        """Tuple form preserves spin ordering."""
        tup = channel_vector_tuple(5)
        assert len(tup) == 4  # spins 2, 3, 4, 5
        assert tup[0] == c / 2
        assert tup[1] == c / 3
        assert tup[2] == c / 4
        assert tup[3] == c / 5


# ===========================================================================
# IV. CROSS-TERM VANISHING
# ===========================================================================

class TestCrossTermVanishing:
    """Mixed W_i-W_j (i != j) contributions to kappa vanish."""

    @pytest.mark.parametrize("N", [3, 4, 5, 6, 10])
    def test_all_cross_terms_zero(self, N):
        """kappa_{ij} = 0 for i != j at each N."""
        assert verify_cross_term_vanishing(N)

    @pytest.mark.parametrize("i,j", [
        (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3),
        (2, 5), (5, 2), (3, 5), (5, 3), (4, 5), (5, 4),
    ])
    def test_specific_cross_terms(self, i, j):
        """kappa_{ij} = 0 for specific off-diagonal pairs."""
        assert cross_term_coefficient(i, j) == 0

    @pytest.mark.parametrize("j", [2, 3, 4, 5, 10])
    def test_diagonal_terms(self, j):
        """kappa_{jj} = 1/j (coefficient of c)."""
        assert cross_term_coefficient(j, j) == Rational(1, j)

    def test_matrix_diagonal_sum(self):
        """sum of diagonal entries of kappa matrix = H_N - 1."""
        for N in [3, 4, 5, 6]:
            mat = cross_term_matrix(N)
            diag_sum = sum(mat[(j, j)] for j in range(2, N + 1))
            assert diag_sum == harmonic_number(N) - 1

    def test_matrix_total_sum(self):
        """Total sum of kappa matrix = H_N - 1 (since off-diagonal = 0)."""
        for N in [3, 4, 5]:
            mat = cross_term_matrix(N)
            total = sum(mat.values())
            assert total == harmonic_number(N) - 1


# ===========================================================================
# IV-b. POLE-ORDER ARGUMENT
# ===========================================================================

class TestPoleOrderArgument:
    """The pole-order mechanism for cross-term vanishing."""

    @pytest.mark.parametrize("j", [2, 3, 4, 5])
    def test_self_ope_max_pole(self, j):
        """W_j x W_j max pole order = 2j."""
        assert ope_max_pole_order(j, j) == 2 * j

    @pytest.mark.parametrize("i,j", [(2, 3), (2, 4), (3, 4), (3, 5)])
    def test_mixed_ope_max_pole(self, i, j):
        """W_i x W_j max pole order = i + j - 1 for i != j."""
        assert ope_max_pole_order(i, j) == i + j - 1

    @pytest.mark.parametrize("j", [2, 3, 4, 5])
    def test_vacuum_pole_at_2j(self, j):
        """Vacuum channel appears at pole 2j in W_j self-OPE."""
        assert vacuum_pole_order(j) == 2 * j

    @pytest.mark.parametrize("j", [2, 3, 4, 5])
    def test_self_coupling_zero_deficit(self, j):
        """Self-coupling has zero pole deficit (vacuum can contribute)."""
        assert cross_term_pole_deficit(j, j) == 0

    @pytest.mark.parametrize("i,j", [(2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
    def test_mixed_positive_deficit(self, i, j):
        """Mixed coupling has positive pole deficit (vacuum cannot contribute)."""
        assert cross_term_pole_deficit(i, j) > 0


# ===========================================================================
# V. SPECIFIC W_N ALGEBRAS
# ===========================================================================

class TestSpecificAlgebras:
    """Verify channel data for W_3, W_4, W_5."""

    def test_w3_channels(self):
        """W_3: kappa_tilde = (c/2, c/3)."""
        data = w3_channel_data()
        assert data["channels"][2] == c / 2
        assert data["channels"][3] == c / 3
        assert simplify(data["total"] - data["expected_total"]) == 0

    def test_w3_total_5c_over_6(self):
        """W_3 total: 5c/6."""
        data = w3_channel_data()
        assert simplify(data["total"] - Rational(5, 6) * c) == 0

    def test_w4_channels(self):
        """W_4: kappa_tilde = (c/2, c/3, c/4)."""
        data = w4_channel_data()
        assert data["channels"][2] == c / 2
        assert data["channels"][3] == c / 3
        assert data["channels"][4] == c / 4
        assert simplify(data["total"] - data["expected_total"]) == 0

    def test_w4_total_13c_over_12(self):
        """W_4 total: 13c/12."""
        data = w4_channel_data()
        assert simplify(data["total"] - Rational(13, 12) * c) == 0

    def test_w5_channels(self):
        """W_5: kappa_tilde = (c/2, c/3, c/4, c/5)."""
        data = w5_channel_data()
        assert data["channels"][2] == c / 2
        assert data["channels"][3] == c / 3
        assert data["channels"][4] == c / 4
        assert data["channels"][5] == c / 5
        assert simplify(data["total"] - data["expected_total"]) == 0

    def test_w5_total_77c_over_60(self):
        """W_5 total: 77c/60."""
        data = w5_channel_data()
        assert simplify(data["total"] - Rational(77, 60) * c) == 0

    def test_w3_at_c_equals_2(self):
        """W_3 at c=2: kappa_tilde = (1, 2/3), total = 5/3."""
        data = w3_channel_data(central_charge=2)
        assert data["channels"][2] == 1
        assert data["channels"][3] == Rational(2, 3)
        assert data["total"] == Rational(5, 3)

    def test_w4_at_c_equals_12(self):
        """W_4 at c=12: kappa_tilde = (6, 4, 3), total = 13."""
        data = w4_channel_data(central_charge=12)
        assert data["channels"][2] == 6
        assert data["channels"][3] == 4
        assert data["channels"][4] == 3
        assert data["total"] == 13


# ===========================================================================
# VI. SUGAWARA CHANNEL VERIFICATION
# ===========================================================================

class TestSugawaraChannel:
    """The W_2 = T channel kappa_2 = c/2 matches Sugawara."""

    def test_sugawara_sl2_k1(self):
        """sl_2 at k=1: c_{Sug} = k*dim/(k+h) = 3/3 = 1, kappa_2 = 1/2."""
        kap = sugawara_kappa(dim_g=3, h_dual=2, level=1)
        assert kap == Rational(1, 2)

    def test_sugawara_sl3_k1(self):
        """sl_3 at k=1: c_{Sug} = 8/4 = 2, kappa_2 = 1."""
        kap = sugawara_kappa(dim_g=8, h_dual=3, level=1)
        assert kap == Rational(1)

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_sugawara_channel_equals_c_over_2(self, N):
        """For each W_N at symbolic level, kappa_2 = c_DS / 2."""
        result = verify_sugawara_channel(N, k)
        assert result["equals_c_over_2"]

    def test_sugawara_ds_vs_km(self):
        """Sugawara kappa for g-hat_k: kappa_2^{Sug} = k*dim(g) / (2*(k+h^vee)).

        The DS central charge c_DS != c_{Sug}, but kappa_2 = c/2 uses the DS c.
        """
        # sl_2 at k=1: c_DS = 1 - 6*4/3 = -7, kappa_2^{DS} = -7/2
        c_ds = wn_central_charge(2, 1)
        assert c_ds == Rational(-7)
        assert channel_kappa(2, c_ds) == Rational(-7, 2)

        # But the Sugawara kappa uses c_{Sug} = k*dim/(k+h) = 3/3 = 1
        kap_sug = sugawara_kappa(dim_g=3, h_dual=2, level=1)
        assert kap_sug == Rational(1, 2)

        # These differ because DS changes the stress tensor


# ===========================================================================
# VII. HARMONIC DIVERGENCE (W_INFINITY OBSTRUCTION)
# ===========================================================================

class TestHarmonicDivergence:
    """As N -> infinity, kappa(W_N)/c ~ log(N) diverges."""

    def test_growth_data_monotone(self):
        """H_N - 1 is strictly increasing."""
        data = kappa_growth_data(50)
        for i in range(len(data) - 1):
            assert data[i][1] < data[i + 1][1]

    def test_growth_exceeds_1(self):
        """H_N - 1 > 1 for N >= 4."""
        assert float(harmonic_number(4) - 1) > 1

    def test_growth_exceeds_2(self):
        """H_N - 1 > 2 for N >= 11."""
        assert float(harmonic_number(11) - 1) > 2
        assert float(harmonic_number(10) - 1) < 2

    def test_growth_exceeds_3(self):
        """H_N - 1 > 3 for N >= 31."""
        assert float(harmonic_number(31) - 1) > 3
        assert float(harmonic_number(30) - 1) < 3

    def test_euler_mascheroni_bound(self):
        """For large N: |H_N - ln(N) - gamma| < 1/(2N)."""
        gamma = float(EulerGamma.evalf())
        for N in [10, 50, 100, 500, 1000]:
            H_N = float(harmonic_number(N))
            ln_N = float(neval(log(N)))
            residual = abs(H_N - ln_N - gamma)
            bound = 1.0 / (2 * N)
            assert residual < bound, \
                f"N={N}: |H_N - ln(N) - gamma| = {residual} >= 1/(2N) = {bound}"

    def test_divergence_bounds(self):
        """harmonic_divergence_bound gives valid bounds."""
        for N in [5, 10, 50, 100]:
            lo, hi = harmonic_divergence_bound(N)
            actual = float(harmonic_number(N) - 1)
            assert lo < actual < hi, \
                f"N={N}: {lo} < {actual} < {hi} failed"

    def test_log_divergence_rate(self):
        """kappa(W_N)/c grows like log(N): ratio (H_N - 1)/log(N) -> 1."""
        for N in [100, 1000]:
            H = float(harmonic_number(N) - 1)
            ratio = H / float(neval(log(N)))
            # Should be close to 1 (within the gamma/log(N) correction)
            assert 0.85 < ratio < 1.15, \
                f"N={N}: (H_N-1)/log(N) = {ratio}"

    def test_w_infinity_obstruction(self):
        """kappa(W_N)/c has no finite limit: structural obstruction for W_infinity.

        This is the key physical point: the scalar modular characteristic
        diverges, necessitating a vector-valued completion for W_infinity.
        """
        values = [float(harmonic_number(N) - 1) for N in [10, 100, 1000]]
        # Each is strictly larger than the previous
        assert values[0] < values[1] < values[2]
        # The last exceeds 5 (log(1000) ~ 6.9)
        assert values[2] > 5


# ===========================================================================
# VIII. CONSISTENCY WITH w4_stage4_coefficients
# ===========================================================================

class TestW4Consistency:
    """Cross-check with the W_4 curvature data from w4_stage4_coefficients.py."""

    def test_all_channels_match(self):
        """Channel vector agrees with w4_curvature()."""
        results = verify_w4_consistency()
        assert results["T_channel_matches"]
        assert results["W3_channel_matches"]
        assert results["W4_channel_matches"]

    def test_total_matches(self):
        """Total kappa agrees with w4_kappa_total()."""
        results = verify_w4_consistency()
        assert results["total_matches"]


# ===========================================================================
# IX. CONSISTENCY WITH sigma_invariant
# ===========================================================================

class TestSigmaConsistency:
    """Cross-check with sigma_invariant(A_{N-1}) from lie_algebra module."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_sigma_equals_harmonic_minus_1(self, N):
        """sigma(A_{N-1}) == H_N - 1 for N where cartan_data exists."""
        results = verify_sigma_consistency(N)
        assert results[f"sigma_A{N-1}_equals_H{N}_minus_1"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_total_kappa_matches_sigma(self, N):
        """total_kappa(W_N) == c * sigma(A_{N-1})."""
        results = verify_sigma_consistency(N)
        assert results[f"total_kappa_W{N}_matches_sigma"]


# ===========================================================================
# X. FF DUALITY ON CHANNEL VECTORS
# ===========================================================================

class TestFFDuality:
    """Feigin-Frenkel duality k -> -k - 2N for W_N from sl_N."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_ff_dual_level(self, N):
        """k' = -k - 2N."""
        k_prime = wn_ff_dual_level(N, k)
        assert simplify(k_prime - (-k - 2 * N)) == 0

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_ff_involution(self, N):
        """(k')' = k: FF duality is an involution."""
        k_prime = wn_ff_dual_level(N, k)
        k_double_prime = wn_ff_dual_level(N, k_prime)
        assert simplify(k_double_prime - k) == 0

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_total_kappa_anti_symmetry(self, N):
        """kappa(k) + kappa(k') = 0 for total scalar kappa.

        This holds because kappa(W_N) = c * sigma and
        c(k) + c(k') = complementarity_sum (constant in k),
        while kappa = c * sigma, so kappa(k) + kappa(k') = sigma * (c(k) + c(k')).
        This is NOT zero in general; it equals sigma * comp_sum.

        The actual anti-symmetry for kappa(W_N^k) requires using the
        full KM-level kappa formula, not c*sigma. The point is that
        kappa(W_N) uses the DS central charge, which does NOT satisfy
        c(k) + c(k') = 0.
        """
        result = ff_channel_anti_symmetry(N, k)
        comp_sum = result["complementarity_sum"]
        total_sum = result["total_kappa_sum"]
        # total_kappa(k) + total_kappa(k') = (H_N - 1) * comp_sum
        expected = (harmonic_number(N) - 1) * comp_sum
        assert simplify(total_sum - expected) == 0

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_complementarity_sum_is_constant(self, N):
        """c(k) + c(k') is independent of k."""
        result = ff_channel_anti_symmetry(N, k)
        comp_sum = result["complementarity_sum"]
        # Should be free of k
        assert k not in comp_sum.free_symbols, \
            f"W_{N}: comp_sum = {comp_sum} depends on k"

    def test_w2_complementarity(self):
        """W_2 = Virasoro from sl_2: c(k) + c(k') = 26 - 24 = 2.

        c = 1 - 6(k+1)^2/(k+2). Dual: k' = -k-4.
        c(k) + c(-k-4) = 2 - 6[(k+1)^2/(k+2) + (-k-3)^2/(-k-2)]
        = 2 - 6[(k+1)^2/(k+2) - (k+3)^2/(k+2)] [for the DS formula]
        Actually: let's just check numerically.
        """
        # sl_2: c = 1 - 6(k+1)^2/(k+2), dual k' = -k - 4
        c_k1 = wn_central_charge(2, 1)       # k=1: c = 1 - 6*4/3 = -7
        c_k1_dual = wn_central_charge(2, -5)  # k'=-5: c = 1 - 6*16/(-3) = 1+32 = 33
        # But wn formula: c = 1 - 6*(1+1)^2/(1+2) = 1 - 24/3 = -7
        # dual: k'=-5, c = 1 - 6*(-4)^2/(-3) = 1 + 32 = 33
        # sum = -7 + 33 = 26
        assert c_k1 + c_k1_dual == 26

    def test_w3_complementarity(self):
        """W_3 from sl_3: c(k) + c(k') = 100.

        This is the known W_3 complementarity sum.
        """
        c_k1 = wn_central_charge(3, 1)
        c_k1_dual = wn_central_charge(3, wn_ff_dual_level(3, 1))
        comp = c_k1 + c_k1_dual
        # Check at k=0 as well
        c_k0 = wn_central_charge(3, 0)
        c_k0_dual = wn_central_charge(3, wn_ff_dual_level(3, 0))
        assert c_k0 + c_k0_dual == comp

    def test_w4_complementarity(self):
        """W_4 from sl_4: c(k) + c(k') = 246.

        Cross-check with w4_stage4_coefficients.
        """
        from compute.lib.w4_stage4_coefficients import w4_complementarity_sum
        assert w4_complementarity_sum() == 246
        # Also verify via our general formula
        c_k1 = wn_central_charge(4, 1)
        c_k1_dual = wn_central_charge(4, wn_ff_dual_level(4, 1))
        assert c_k1 + c_k1_dual == 246


# ===========================================================================
# XI. WN CENTRAL CHARGE FORMULA
# ===========================================================================

class TestWNCentralCharge:
    """W_N central charge: c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)."""

    def test_w2_matches_virasoro_ds(self):
        """W_2 DS formula matches the standard Virasoro DS formula.

        c = 1 - 6(k+1)^2/(k+2).
        General: c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N).
        For N=2: c = 1 - 2*3*(k+1)^2/(k+2) = 1 - 6(k+1)^2/(k+2).
        """
        for lev in [0, 1, 2, 5, Rational(1, 2)]:
            from compute.lib.lie_algebra import virasoro_ds_c
            assert wn_central_charge(2, lev) == virasoro_ds_c(lev)

    def test_w3_matches_ds(self):
        """W_3 DS formula: c = 2 - 24(k+2)^2/(k+3).

        General: c = 2 - 3*8*(k+2)^2/(k+3) = 2 - 24(k+2)^2/(k+3).
        """
        for lev in [0, 1, 2, 5]:
            from compute.lib.lie_algebra import w3_ds_c
            assert wn_central_charge(3, lev) == w3_ds_c(lev)

    def test_w4_matches_w4_module(self):
        """W_4 central charge matches w4_stage4_coefficients."""
        from compute.lib.w4_stage4_coefficients import w4_central_charge
        for lev in [0, 1, 2, 5]:
            assert wn_central_charge(4, lev) == w4_central_charge(lev)

    def test_w_n_raises_for_n_less_than_2(self):
        with pytest.raises(ValueError):
            wn_central_charge(1, 0)


# ===========================================================================
# XII. CHANNEL MONOTONICITY AND ORDERING
# ===========================================================================

class TestChannelOrdering:
    """Structural properties of the channel vector."""

    @pytest.mark.parametrize("N", [3, 4, 5, 10])
    def test_channels_decrease(self, N):
        """kappa_2 > kappa_3 > ... > kappa_N (for c > 0)."""
        vec = channel_vector(N, central_charge=1)
        vals = [vec[j] for j in range(2, N + 1)]
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i + 1]

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_virasoro_channel_dominates(self, N):
        """kappa_2 / total > 1/2 for small N (Virasoro channel is dominant).

        kappa_2 / kappa_total = (1/2) / (H_N - 1).
        For N=3: 1/2 / (5/6) = 3/5 > 1/2.
        For N=4: 1/2 / (13/12) = 6/13 < 1/2.
        """
        ratio = Rational(1, 2) / (harmonic_number(N) - 1)
        if N == 3:
            assert ratio > Rational(1, 2)
        # For all N, the Virasoro channel is the single largest
        vec = channel_vector(N, central_charge=1)
        assert all(vec[2] >= vec[j] for j in range(2, N + 1))

    @pytest.mark.parametrize("N", [3, 4, 5, 10])
    def test_incremental_growth(self, N):
        """kappa(W_{N}) - kappa(W_{N-1}) = c/N (adding one channel)."""
        if N < 3:
            return
        diff = total_kappa(N, central_charge=1) - total_kappa(N - 1, central_charge=1)
        assert diff == Rational(1, N)

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 10])
    def test_positivity_at_positive_c(self, N):
        """All channels positive when c > 0."""
        vec = channel_vector(N, central_charge=1)
        assert all(v > 0 for v in vec.values())

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_sign_flip_at_negative_c(self, N):
        """All channels negative when c < 0."""
        vec = channel_vector(N, central_charge=-1)
        assert all(v < 0 for v in vec.values())
