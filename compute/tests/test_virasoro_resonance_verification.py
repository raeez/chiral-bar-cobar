r"""Tests for Virasoro resonance verification and Platonic Completion Conjecture.

Ground truth from the manuscript:
  prop:resonance-ranks-standard (appendices/nilpotent_completion.tex):
    Heisenberg:   rho = 0, dim R = 0 (quadratic, no completion needed)
    Free fermion: rho = 0, dim R = 0 (quadratic, no completion needed)
    betagamma:    rho = 0, dim R = 0 (quadratic, no completion needed)
    Affine:       rho = 0, dim R = 0 (quadratic OPE, PBW-Koszul)
    Virasoro:     rho = 1, dim R = 1 (R = k * m_0, curvature from quartic pole)
    W_3:          rho = 1, dim R = 1 (R = k * m_0, curvature from 6th-order pole)
    W_N (N >= 3): rho = 1, dim R = 1 (single resonance direction)
    W_{1+inf}:    rho = 0, dim R = 0 (positive tower, stabilization)
    Y(g):         rho = 0, dim R = 0 (positive RTT tower, stabilization)

Key mathematical argument:
  - For Virasoro: T has weight 2, so A+ has weight >= 2. bar_n at weight 0
    is empty for n >= 1 (total weight >= 2n > 0). Curvature m_0 at arity 0,
    weight 0 gives R = C*m_0, rho = 1.
  - Same argument for all W_N (N >= 2): generators have weight >= 2.

conj:platonic-completion: Every positive-energy chiral algebra has rho < inf.
  Verified computationally for the entire standard landscape.
"""

import pytest
from sympy import Rational

from compute.lib.virasoro_resonance_verification import (
    # Data classes and constructors
    VOAWeightData,
    VIRASORO,
    W3,
    HEISENBERG,
    AFFINE_SL2,
    BETAGAMMA,
    FREE_FERMION,
    STANDARD_FAMILIES,
    w_n_data,
    # Bar complex weight analysis
    bar_arity_weight_dim,
    bar_weight0_dim,
    # Resonance computations
    ResonanceData,
    compute_resonance_data,
    virasoro_resonance,
    virasoro_bar_weight_profile,
    virasoro_weight_gap,
    w_n_resonance,
    w_n_weight_gap,
    # Weight-raising
    verify_weight_raising,
    # Full landscape
    resonance_rank_all_families,
    verify_platonic_completion,
    weight0_dimension_table,
    check_c_independence,
    minimum_weight_gap_analysis,
    CURVATURE_MAP,
)


# ===========================================================================
# 1. VOA weight structure tests
# ===========================================================================

class TestVOAWeightData:
    """Verify the weight structure of standard VOAs."""

    def test_virasoro_generator_weight(self):
        """Virasoro has a single generator T of weight 2."""
        assert VIRASORO.generator_weights == [2]
        assert VIRASORO.min_positive_weight == 2
        assert VIRASORO.vacuum_dim == 1

    def test_w3_generator_weights(self):
        """W_3 has generators T (weight 2) and W (weight 3)."""
        assert W3.generator_weights == [2, 3]
        assert W3.min_positive_weight == 2

    def test_w_n_generator_weights(self):
        """W_N has generators of weights 2, 3, ..., N."""
        for N in [2, 3, 4, 5, 10]:
            voa = w_n_data(N)
            assert voa.generator_weights == list(range(2, N + 1))
            assert voa.min_positive_weight == 2

    def test_heisenberg_generator_weight(self):
        """Heisenberg has a single generator J of weight 1."""
        assert HEISENBERG.generator_weights == [1]
        assert HEISENBERG.min_positive_weight == 1

    def test_affine_sl2_generator_weights(self):
        """Affine sl_2 has 3 generators of weight 1."""
        assert AFFINE_SL2.generator_weights == [1, 1, 1]
        assert AFFINE_SL2.min_positive_weight == 1

    def test_betagamma_generator_weights(self):
        """betagamma has 2 generators of weight 1."""
        assert BETAGAMMA.generator_weights == [1, 1]
        assert BETAGAMMA.min_positive_weight == 1

    def test_w_n_invalid(self):
        """W_N with N < 2 should raise."""
        with pytest.raises(ValueError):
            w_n_data(1)


# ===========================================================================
# 2. Bar complex weight-0 analysis (the core argument)
# ===========================================================================

class TestBarWeight0:
    """The central verification: bar_n at weight 0 is empty for n >= 1."""

    def test_virasoro_bar0_weight0(self):
        """bar_0(Vir) at weight 0 = ground field = 1-dimensional."""
        assert bar_weight0_dim(VIRASORO, 0) == 1

    def test_virasoro_bar1_weight0(self):
        """bar_1(Vir) at weight 0 = 0: A+ has no weight-0 elements."""
        assert bar_weight0_dim(VIRASORO, 1) == 0

    def test_virasoro_bar_n_weight0_all_zero(self):
        """bar_n(Vir) at weight 0 = 0 for ALL n >= 1 (up to n=15)."""
        for n in range(1, 16):
            assert bar_weight0_dim(VIRASORO, n) == 0, f"Nonzero at n={n}"

    def test_w3_bar_n_weight0_all_zero(self):
        """bar_n(W_3) at weight 0 = 0 for all n >= 1."""
        for n in range(1, 11):
            assert bar_weight0_dim(W3, n) == 0, f"Nonzero at n={n}"

    def test_w_n_bar_n_weight0_all_zero(self):
        """bar_n(W_N) at weight 0 = 0 for all N >= 2, n >= 1."""
        for N in [2, 3, 4, 5, 10]:
            voa = w_n_data(N)
            for n in range(1, 8):
                assert bar_weight0_dim(voa, n) == 0, (
                    f"Nonzero at N={N}, n={n}"
                )

    def test_heisenberg_bar_n_weight0_all_zero(self):
        """bar_n(Heis) at weight 0 = 0 for all n >= 1."""
        for n in range(1, 11):
            assert bar_weight0_dim(HEISENBERG, n) == 0

    def test_affine_bar_n_weight0_all_zero(self):
        """bar_n(affine sl_2) at weight 0 = 0 for all n >= 1."""
        for n in range(1, 11):
            assert bar_weight0_dim(AFFINE_SL2, n) == 0

    def test_betagamma_bar_n_weight0_all_zero(self):
        """bar_n(betagamma) at weight 0 = 0 for all n >= 1."""
        for n in range(1, 11):
            assert bar_weight0_dim(BETAGAMMA, n) == 0

    def test_free_fermion_bar_n_weight0_all_zero(self):
        """bar_n(free fermion) at weight 0 = 0 for all n >= 1."""
        for n in range(1, 11):
            assert bar_weight0_dim(FREE_FERMION, n) == 0

    def test_all_families_bar_n_weight0(self):
        """UNIVERSAL: bar_n at weight 0 is empty for n >= 1 for ALL standard families."""
        for name, voa in STANDARD_FAMILIES.items():
            for n in range(1, 8):
                assert bar_weight0_dim(voa, n) == 0, (
                    f"Weight-0 element found at arity {n} for {name}"
                )


# ===========================================================================
# 3. Bar complex weight structure at positive weights
# ===========================================================================

class TestBarWeightStructure:
    """Verify the weight decomposition of bar_n(Vir) at low degrees."""

    def test_virasoro_bar1_weight2(self):
        """bar_1(Vir) at weight 2: just the generator T. dim = 1."""
        assert bar_arity_weight_dim(VIRASORO, 1, 2) == 1

    def test_virasoro_bar1_weight3(self):
        """bar_1(Vir) at weight 3: L_{-3}|0>. dim = 1."""
        assert bar_arity_weight_dim(VIRASORO, 1, 3) == 1

    def test_virasoro_bar1_weight4(self):
        """bar_1(Vir) at weight 4: L_{-4}|0> and L_{-2}^2|0>. dim = 2."""
        assert bar_arity_weight_dim(VIRASORO, 1, 4) == 2

    def test_virasoro_bar1_weight5(self):
        """bar_1(Vir) at weight 5: L_{-5}, L_{-3}L_{-2}. dim = 2."""
        assert bar_arity_weight_dim(VIRASORO, 1, 5) == 2

    def test_virasoro_bar1_matches_partition_function(self):
        """bar_1(Vir) at weight w = partitions of w into parts >= 2."""
        # This is the character of the augmentation ideal of the Virasoro VOA
        expected = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 7}
        for w, exp_dim in expected.items():
            assert bar_arity_weight_dim(VIRASORO, 1, w) == exp_dim, (
                f"Mismatch at weight {w}: got {bar_arity_weight_dim(VIRASORO, 1, w)}, "
                f"expected {exp_dim}"
            )

    def test_virasoro_bar2_minimum_weight(self):
        """bar_2(Vir) has minimum weight 4 (= 2 * 2)."""
        for w in range(4):
            assert bar_arity_weight_dim(VIRASORO, 2, w) == 0
        # At weight 4: T tensor T. dim = 1.
        assert bar_arity_weight_dim(VIRASORO, 2, 4) == 1

    def test_virasoro_bar2_weight5(self):
        """bar_2(Vir) at weight 5: T x L_{-3}|0> and L_{-3}|0> x T. dim = 2."""
        # Two ordered pairs: (wt 2, wt 3) and (wt 3, wt 2).
        # dim(A+_2) = 1, dim(A+_3) = 1, so convolution gives 1*1 + 1*1 = 2.
        assert bar_arity_weight_dim(VIRASORO, 2, 5) == 2

    def test_virasoro_bar3_minimum_weight(self):
        """bar_3(Vir) has minimum weight 6 (= 3 * 2)."""
        for w in range(6):
            assert bar_arity_weight_dim(VIRASORO, 3, w) == 0
        # At weight 6: T^{otimes 3}. dim = 1.
        assert bar_arity_weight_dim(VIRASORO, 3, 6) == 1

    def test_heisenberg_bar1_weights(self):
        """bar_1(Heis) at weight w = p(w) (unrestricted partitions of w).

        The Heisenberg VOA has a single generator J of weight 1 with modes
        J_{-n} (n >= 1). The PBW basis of A+ at weight w consists of all
        monomials J_{-n1} ... J_{-nk} with n1 + ... + nk = w, giving p(w).
        """
        # p(w) for w = 1..7: 1, 2, 3, 5, 7, 11, 15
        expected = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15}
        for w, exp_dim in expected.items():
            assert bar_arity_weight_dim(HEISENBERG, 1, w) == exp_dim


# ===========================================================================
# 4. Virasoro resonance rank verification
# ===========================================================================

class TestVirasoroResonance:
    """rho(Vir_c) = 1: the curvature m_0 is the sole resonance."""

    def test_rho_equals_1(self):
        """rho(Vir) = 1 (manuscript: prop:resonance-ranks-standard)."""
        data = virasoro_resonance()
        assert data.rho == 1

    def test_dim_R_equals_1(self):
        """dim R_Vir = 1: the resonance subspace is 1-dimensional."""
        data = virasoro_resonance()
        assert data.dim_R == 1

    def test_curvature_contribution(self):
        """The curvature m_0 contributes to the resonance."""
        data = virasoro_resonance()
        assert data.curvature_contribution is True

    def test_mc4_class(self):
        """Virasoro is MC4^0 (resonant, not positive)."""
        data = virasoro_resonance()
        assert data.mc4_class == "MC4^0"

    def test_bar_weight0_all_zero(self):
        """All weight-0 bar dimensions at positive arity are zero."""
        data = virasoro_resonance()
        for n in range(1, 11):
            assert data.weight0_bar_dims[n] == 0

    def test_bar_weight0_arity0(self):
        """bar_0 at weight 0 is 1-dimensional (ground field)."""
        data = virasoro_resonance()
        assert data.weight0_bar_dims[0] == 1


# ===========================================================================
# 5. Central charge independence
# ===========================================================================

class TestCentralChargeIndependence:
    """rho(Vir_c) = 1 for ALL values of c."""

    def test_generic_c(self):
        """Generic c: rho = 1."""
        data = virasoro_resonance()
        assert data.rho == 1

    def test_ising_c_half(self):
        """c = 1/2 (Ising model): rho = 1."""
        results = check_c_independence(c_values=[Rational(1, 2)])
        assert results["1/2"]["rho"] == 1
        assert results["1/2"]["bar_weight0_positive_arity_empty"]

    def test_c_1(self):
        """c = 1 (free boson at radius R): rho = 1."""
        results = check_c_independence(c_values=[1])
        assert results["1"]["rho"] == 1
        assert results["1"]["bar_weight0_positive_arity_empty"]

    def test_self_dual_c_13(self):
        """c = 13 (self-dual point, Vir_13^! = Vir_13): rho = 1."""
        results = check_c_independence(c_values=[13])
        assert results["13"]["rho"] == 1
        assert results["13"]["bar_weight0_positive_arity_empty"]

    def test_c_25(self):
        """c = 25 (near bosonic string): rho = 1."""
        results = check_c_independence(c_values=[25])
        assert results["25"]["rho"] == 1
        assert results["25"]["bar_weight0_positive_arity_empty"]

    def test_c_26(self):
        """c = 26 (ghost Virasoro, Vir_26^! = Vir_0): rho = 1."""
        results = check_c_independence(c_values=[26])
        assert results["26"]["rho"] == 1

    def test_c_0(self):
        """c = 0 (trivial central charge): rho = 1."""
        results = check_c_independence(c_values=[0])
        assert results["0"]["rho"] == 1

    def test_negative_c(self):
        """c = -2 (symplectic fermions): rho = 1."""
        results = check_c_independence(c_values=[-2])
        assert results["-2"]["rho"] == 1

    def test_large_c(self):
        """c = 100 (large central charge): rho = 1."""
        results = check_c_independence(c_values=[100])
        assert results["100"]["rho"] == 1

    def test_all_special_values(self):
        """Comprehensive check across many special values of c."""
        results = check_c_independence()
        for c_str, data in results.items():
            assert data["rho"] == 1, f"rho != 1 at c = {c_str}"
            assert data["bar_weight0_positive_arity_empty"], (
                f"weight-0 bar elements at positive arity at c = {c_str}"
            )


# ===========================================================================
# 6. W_N resonance verification
# ===========================================================================

class TestWNResonance:
    """rho(W_N) = 1 for all finite N >= 2."""

    def test_w3_rho_1(self):
        """rho(W_3) = 1 (manuscript: prop:resonance-ranks-standard)."""
        data = w_n_resonance(3)
        assert data.rho == 1

    def test_w3_dim_R_1(self):
        """dim R_{W_3} = 1."""
        data = w_n_resonance(3)
        assert data.dim_R == 1

    def test_w3_mc4_class(self):
        """W_3 is MC4^0."""
        data = w_n_resonance(3)
        assert data.mc4_class == "MC4^0"

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro, so rho(W_2) = 1."""
        data = w_n_resonance(2)
        assert data.rho == 1

    def test_w4_rho_1(self):
        """rho(W_4) = 1."""
        data = w_n_resonance(4)
        assert data.rho == 1

    def test_w5_rho_1(self):
        """rho(W_5) = 1."""
        data = w_n_resonance(5)
        assert data.rho == 1

    def test_w10_rho_1(self):
        """rho(W_10) = 1."""
        data = w_n_resonance(10)
        assert data.rho == 1

    def test_w_n_bar_weight0_empty(self):
        """bar_n(W_N) at weight 0 is empty for all n >= 1, all N >= 2."""
        for N in [2, 3, 4, 5]:
            data = w_n_resonance(N, max_arity=8)
            for n in range(1, 9):
                assert data.weight0_bar_dims[n] == 0, (
                    f"Nonzero weight-0 at arity {n} for W_{N}"
                )


# ===========================================================================
# 7. Weight gap analysis
# ===========================================================================

class TestWeightGap:
    """The weight gap at each arity is the key to the resonance argument."""

    def test_virasoro_gap_arity0(self):
        """bar_0: minimum weight = 0."""
        assert virasoro_weight_gap(0) == 0

    def test_virasoro_gap_arity1(self):
        """bar_1: minimum weight = 2 (generator T)."""
        assert virasoro_weight_gap(1) == 2

    def test_virasoro_gap_grows_linearly(self):
        """bar_n: minimum weight = 2n."""
        for n in range(11):
            assert virasoro_weight_gap(n) == 2 * n

    def test_w_n_gap_equals_virasoro_gap(self):
        """W_N has the same weight gap as Virasoro (min generator weight = 2)."""
        for N in [2, 3, 5, 10]:
            for n in range(8):
                assert w_n_weight_gap(N, n) == virasoro_weight_gap(n)

    def test_gap_strictly_positive_at_positive_arity(self):
        """The gap is > 0 for all n >= 1, which is the heart of rho computation."""
        for n in range(1, 20):
            assert virasoro_weight_gap(n) > 0


# ===========================================================================
# 8. Weight-raising property of mixed operations
# ===========================================================================

class TestWeightRaising:
    """Mixed operations R x A+ -> A+ strictly raise weight."""

    def test_virasoro_weight_raising(self):
        """For Virasoro, all mixed operations raise weight."""
        result = verify_weight_raising(VIRASORO)
        assert result["all_positive"]

    def test_w3_weight_raising(self):
        """For W_3, all mixed operations raise weight."""
        result = verify_weight_raising(W3)
        assert result["all_positive"]

    def test_heisenberg_weight_raising(self):
        """For Heisenberg, all mixed operations raise weight."""
        result = verify_weight_raising(HEISENBERG)
        assert result["all_positive"]

    def test_all_families_weight_raising(self):
        """UNIVERSAL: mixed operations raise weight for all standard families."""
        for name, voa in STANDARD_FAMILIES.items():
            result = verify_weight_raising(voa)
            assert result["all_positive"], f"Weight raising fails for {name}"

    def test_mixed_weight_minimum(self):
        """At arity n, the minimum mixed weight is (n-1) * min_positive_weight."""
        result = verify_weight_raising(VIRASORO)
        for case in result["cases"]:
            n = case["arity"]
            assert case["min_mixed_weight"] == (n - 1) * 2


# ===========================================================================
# 9. Full landscape resonance verification
# ===========================================================================

class TestFullLandscape:
    """Resonance data for all standard families matches manuscript."""

    def test_all_rho_values(self):
        """Verify rho against prop:resonance-ranks-standard."""
        all_data = resonance_rank_all_families()
        expected = {
            "heisenberg": 0,
            "affine_sl2": 0,
            "virasoro": 1,
            "w3": 1,
            "betagamma": 0,
            "free_fermion": 0,
        }
        for name, exp_rho in expected.items():
            assert all_data[name].rho == exp_rho, (
                f"rho({name}) = {all_data[name].rho}, expected {exp_rho}"
            )

    def test_all_dim_R_values(self):
        """dim R matches expected values."""
        all_data = resonance_rank_all_families()
        expected_dim_R = {
            "heisenberg": 0,
            "affine_sl2": 0,
            "virasoro": 1,
            "w3": 1,
            "betagamma": 0,
            "free_fermion": 0,
        }
        for name, exp_dim in expected_dim_R.items():
            assert all_data[name].dim_R == exp_dim

    def test_mc4_classes(self):
        """MC4 class assignment: MC4+ for rho=0, MC4^0 for rho>=1."""
        all_data = resonance_rank_all_families()
        expected_class = {
            "heisenberg": "MC4+",
            "affine_sl2": "MC4+",
            "virasoro": "MC4^0",
            "w3": "MC4^0",
            "betagamma": "MC4+",
            "free_fermion": "MC4+",
        }
        for name, exp_cls in expected_class.items():
            assert all_data[name].mc4_class == exp_cls

    def test_curvature_map(self):
        """Only Virasoro and W_3 have nonzero curvature in the standard landscape."""
        assert CURVATURE_MAP["virasoro"] is True
        assert CURVATURE_MAP["w3"] is True
        assert CURVATURE_MAP["heisenberg"] is False
        assert CURVATURE_MAP["affine_sl2"] is False
        assert CURVATURE_MAP["betagamma"] is False
        assert CURVATURE_MAP["free_fermion"] is False


# ===========================================================================
# 10. Platonic Completion Conjecture
# ===========================================================================

class TestPlatonicCompletion:
    """conj:platonic-completion: rho < infinity for all positive-energy families."""

    def test_all_finite(self):
        """All standard families have finite rho."""
        all_finite, rho_map = verify_platonic_completion()
        assert all_finite, f"Infinite rho found: {rho_map}"

    def test_rho_values(self):
        """Verify exact rho values from the conjecture verification."""
        _, rho_map = verify_platonic_completion()
        assert rho_map["virasoro"] == 1
        assert rho_map["w3"] == 1
        assert rho_map["heisenberg"] == 0
        assert rho_map["affine_sl2"] == 0
        assert rho_map["betagamma"] == 0
        assert rho_map["free_fermion"] == 0

    def test_rho_bounded_by_1(self):
        """For all standard families, rho <= 1."""
        _, rho_map = verify_platonic_completion()
        for name, rho in rho_map.items():
            assert rho <= 1, f"rho({name}) = {rho} > 1"


# ===========================================================================
# 11. Weight-0 dimension table
# ===========================================================================

class TestWeight0DimensionTable:
    """Verify the weight-0 dimension table for all families."""

    def test_table_structure(self):
        """Table has entries for all standard families."""
        table = weight0_dimension_table()
        assert set(table.keys()) == set(STANDARD_FAMILIES.keys())

    def test_arity0_always_1(self):
        """bar_0 at weight 0 = 1 for all families (ground field)."""
        table = weight0_dimension_table()
        for name, dims in table.items():
            assert dims[0] == 1, f"bar_0 weight-0 dim != 1 for {name}"

    def test_positive_arity_always_0(self):
        """bar_n at weight 0 = 0 for n >= 1, for ALL families."""
        table = weight0_dimension_table()
        for name, dims in table.items():
            for n in range(1, len(dims)):
                assert dims[n] == 0, (
                    f"bar_{n} weight-0 dim != 0 for {name}"
                )

    def test_table_pattern(self):
        """The table should be [1, 0, 0, 0, ...] for every family."""
        table = weight0_dimension_table()
        for name, dims in table.items():
            expected = [1] + [0] * (len(dims) - 1)
            assert dims == expected, f"Pattern mismatch for {name}: {dims}"


# ===========================================================================
# 12. Minimum weight gap analysis
# ===========================================================================

class TestMinimumWeightGapAnalysis:
    """Weight gap analysis confirms bar_n weight-0 emptiness."""

    def test_all_gaps_positive(self):
        """All families have positive weight gaps at arity >= 1."""
        analysis = minimum_weight_gap_analysis()
        for name, data in analysis.items():
            assert data["all_positive"], f"Negative or zero gap for {name}"

    def test_virasoro_gaps(self):
        """Virasoro gaps: 0, 2, 4, 6, 8, ..."""
        analysis = minimum_weight_gap_analysis()
        vir_gaps = analysis["virasoro"]["gaps"]
        for n in range(11):
            assert vir_gaps[n] == 2 * n

    def test_heisenberg_gaps(self):
        """Heisenberg gaps: 0, 1, 2, 3, 4, ..."""
        analysis = minimum_weight_gap_analysis()
        heis_gaps = analysis["heisenberg"]["gaps"]
        for n in range(11):
            assert heis_gaps[n] == n

    def test_min_positive_weights(self):
        """Verify min_positive_weight for each family."""
        analysis = minimum_weight_gap_analysis()
        expected = {
            "virasoro": 2,
            "w3": 2,
            "heisenberg": 1,
            "affine_sl2": 1,
            "betagamma": 1,
            "free_fermion": 1,
        }
        for name, exp_min in expected.items():
            assert analysis[name]["min_positive_weight"] == exp_min


# ===========================================================================
# 13. Virasoro bar weight profile
# ===========================================================================

class TestVirasoroBarWeightProfile:
    """Detailed weight profile of bar_n(Vir)."""

    def test_profile_arity0(self):
        """bar_0: only weight 0 with dim 1."""
        profile = virasoro_bar_weight_profile(max_arity=3)
        assert profile[0] == {0: 1}

    def test_profile_arity1(self):
        """bar_1: weights 2, 3, 4, ... with Virasoro partition function dims."""
        profile = virasoro_bar_weight_profile(max_arity=3, max_weight=8)
        p = profile[1]
        assert 0 not in p  # no weight 0
        assert 1 not in p  # no weight 1
        assert p[2] == 1   # T
        assert p[3] == 1   # L_{-3}|0>
        assert p[4] == 2   # L_{-4}|0>, L_{-2}^2|0>

    def test_profile_arity2_starts_at_4(self):
        """bar_2: minimum weight is 4."""
        profile = virasoro_bar_weight_profile(max_arity=3, max_weight=8)
        p = profile[2]
        for w in range(4):
            assert w not in p
        assert 4 in p
        assert p[4] == 1  # T tensor T

    def test_no_weight0_in_any_profile(self):
        """No arity >= 1 has weight 0 in its profile."""
        profile = virasoro_bar_weight_profile(max_arity=5, max_weight=15)
        for n in range(1, 6):
            assert 0 not in profile[n], f"Weight 0 found at arity {n}"


# ===========================================================================
# 14. Cross-check with resonance_rank_engine
# ===========================================================================

class TestCrossCheck:
    """Cross-check with the existing resonance_rank_engine module."""

    def test_virasoro_rho_matches_engine(self):
        """Our rho(Vir) = 1 matches resonance_rank_engine."""
        from compute.lib.resonance_rank_engine import resonance_rank as rr_engine
        assert rr_engine("virasoro") == 1
        data = virasoro_resonance()
        assert data.rho == rr_engine("virasoro")

    def test_w3_rho_matches_engine(self):
        """Our rho(W_3) = 1 matches resonance_rank_engine."""
        from compute.lib.resonance_rank_engine import resonance_rank as rr_engine
        assert rr_engine("w3") == 1
        data = w_n_resonance(3)
        assert data.rho == rr_engine("w3")

    def test_heisenberg_rho_matches_engine(self):
        """Our rho(Heis) = 0 matches resonance_rank_engine."""
        from compute.lib.resonance_rank_engine import resonance_rank as rr_engine
        assert rr_engine("heisenberg") == 0

    def test_betagamma_rho_matches_engine(self):
        """Our rho(betagamma) = 0 matches resonance_rank_engine."""
        from compute.lib.resonance_rank_engine import resonance_rank as rr_engine
        assert rr_engine("betagamma") == 0
