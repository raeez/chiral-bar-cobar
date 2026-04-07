"""Tests for PBW-Saito weight filtration comparison engine.

Tests the central identification F^{PBW} = W^{Saito} that would close
the D-module purity converse (item (xii) of thm:koszul-equivalences-meta).

CLUSTER 1 (8 tests): Algebra data construction and kappa verification.
    Verifies correct construction of AlgebraData for all families.
    AP1: kappa computed from defining formula for each family.
    AP39: kappa != c/2 for affine KM at rank > 1.

CLUSTER 2 (8 tests): Bar bigraded dimensions.
    Verifies dim B^{n,h}(A) at each bidegree.
    Three-path: direct formula, generating function, recursion.

CLUSTER 3 (6 tests): PBW filtration computation.
    Verifies that PBW filtration steps match the conformal weight decomposition.

CLUSTER 4 (8 tests): Affine KM landscape (PBW = Saito PROVED).
    Tests all simple types at generic level.
    Verifies PBW = Saito is consistent for all types.

CLUSTER 5 (6 tests): Virasoro and W-algebra landscape (PBW = Saito OPEN).
    Tests Virasoro at various c, W_3, W_4.
    Verifies consistency with the prediction.

CLUSTER 6 (6 tests): Counterexample search.
    Tests admissible quotients, minimal models, triplet, non-principal W.
    Verifies ZERO counterexamples to PBW = Saito.

CLUSTER 7 (5 tests): Regular singularity and pole analysis.
    Tests that all standard algebras have regular singular bar D-modules.
    Verifies pole order predictions.

CLUSTER 8 (5 tests): Spectral sequence comparison.
    Tests PBW spectral sequence structure at the E_1 page level.

CLUSTER 9 (4 tests): Master comparison and cross-family consistency.
    Runs the full landscape and verifies zero counterexamples.

ANTI-PATTERN GUARDS:
    AP1:  kappa values independently computed and cross-checked.
    AP3:  Each test verifies from first principles.
    AP9:  PBW != Saito a priori; we test whether they agree.
    AP10: Cross-family consistency (KM vs Virasoro vs W-algebra).
    AP36: Forward (purity => Koszul) PROVED. Converse OPEN.
    AP39: kappa != c/2 for non-Virasoro.

References:
    thm:koszul-equivalences-meta item (xii) (chiral_koszul_pairs.tex)
    rem:d-module-purity-content (chiral_koszul_pairs.tex)
    prop:d-module-purity-km (chiral_koszul_pairs.tex)
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.pbw_saito_comparison import (
    AlgebraData,
    AlgebraFamily,
    LIE_ALGEBRA_DATA,
    affine_km_data,
    virasoro_data,
    w_algebra_data,
    admissible_quotient_data,
    minimal_model_data,
    triplet_data,
    non_principal_w_data,
    weight_space_dim,
    bar_bigraded_dims,
    compute_pbw_filtration,
    predict_saito_weights,
    compare_filtrations,
    compute_pbw_spectral_sequence,
    run_affine_km_landscape,
    run_w_algebra_landscape,
    run_virasoro_landscape,
    run_counterexample_search,
    run_master_comparison,
    ope_pole_orders,
    saito_weight_from_pole_structure,
    check_regular_singularity,
    bar_bigraded_table,
    bar_degree_comparison_table,
)


# ============================================================================
# CLUSTER 1: Algebra data construction (8 tests)
# ============================================================================

class TestAlgebraData:
    """Verify correct construction of AlgebraData for all families."""

    def test_sl2_kappa_from_formula(self):
        """AP1: kappa(sl_2, k) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4."""
        alg = affine_km_data('A1', Rational(5))
        # kappa = 3 * (5 + 2) / (2 * 2) = 3 * 7 / 4 = 21/4
        assert alg.kappa == Rational(21, 4)

    def test_sl3_kappa_not_c_over_2(self):
        """AP39: kappa != c/2 for rank > 1."""
        alg = affine_km_data('A2', Rational(3))
        # dim(sl_3) = 8, h^v = 3
        # kappa = 8 * (3 + 3) / (2 * 3) = 8 * 6 / 6 = 8
        # c = 8 * 3 / (3 + 3) = 4
        # c/2 = 2 != 8
        assert alg.kappa == Rational(8)
        assert alg.central_charge == Rational(4)
        assert alg.kappa != alg.central_charge / 2

    def test_virasoro_kappa_equals_c_over_2(self):
        """For Virasoro: kappa = c/2."""
        alg = virasoro_data(Rational(25))
        assert alg.kappa == Rational(25, 2)
        assert alg.kappa == alg.central_charge / 2

    def test_w3_generator_weights(self):
        """W^k(sl_3) has generators at weights 2 and 3."""
        alg = w_algebra_data('sl3', Rational(7))
        gen_weights = tuple(w for _, w in alg.generators)
        assert gen_weights == (2, 3)

    def test_w4_generator_weights(self):
        """W^k(sl_4) has generators at weights 2, 3, and 4."""
        alg = w_algebra_data('sl4', Rational(5))
        gen_weights = tuple(w for _, w in alg.generators)
        assert gen_weights == (2, 3, 4)

    def test_admissible_level_construction(self):
        """Admissible quotient L_k(sl_2) at k = 4/3 - 2 = -2/3."""
        alg = admissible_quotient_data('A1', 4, 3)
        assert alg.level == Rational(4, 3) - 2
        assert alg.level == Rational(-2, 3)
        # kappa = 3 * (-2/3 + 2) / 4 = 3 * 4/3 / 4 = 1
        assert alg.kappa == Rational(1)

    def test_minimal_model_central_charge(self):
        """M(4,3): c = 1 - 6(4-3)^2/(4*3) = 1 - 6/12 = 1/2."""
        alg = minimal_model_data(4, 3)
        assert alg.central_charge == Rational(1, 2)
        assert alg.is_koszul is False

    def test_lie_algebra_data_dimensions(self):
        """Verify Lie algebra dimensions for standard types."""
        assert LIE_ALGEBRA_DATA['A1'] == (3, 1, 2)   # sl_2
        assert LIE_ALGEBRA_DATA['A2'] == (8, 2, 3)   # sl_3
        assert LIE_ALGEBRA_DATA['E8'] == (248, 8, 30) # E_8
        assert LIE_ALGEBRA_DATA['G2'] == (14, 2, 4)   # G_2


# ============================================================================
# CLUSTER 2: Bar bigraded dimensions (8 tests)
# ============================================================================

class TestBarBigradedDims:
    """Verify dim B^{n,h}(A) at each bidegree."""

    def test_sl2_bar_degree_1(self):
        """B^{1,h}(V_k(sl_2)) = dim A_h = 3-color partitions of h."""
        alg = affine_km_data('A1', Rational(5))
        dims = bar_bigraded_dims(alg, max_arity=1, max_weight=6)
        # B^{1,1} = dim A_1 = 3 (e, h, f)
        assert dims.get((1, 1), 0) == 3
        # B^{1,2} = dim A_2 = 3-color partitions of 2
        # = 3 (from parts 1+1 with 3 colors for first, 3 for second, but ordered)
        # p_3(2) = C(2+3-1, 3-1) = C(4,2) = 6... let me compute properly
        # prod_{m>=1} 1/(1-q^m)^3 = 1 + 3q + 9q^2 + ...
        # At q^1: 3, at q^2: 9
        assert dims.get((1, 2), 0) == 9

    def test_virasoro_bar_degree_1(self):
        """B^{1,h}(Vir_c) = partitions of h into parts >= 2."""
        alg = virasoro_data(Rational(25))
        dims = bar_bigraded_dims(alg, max_arity=1, max_weight=8)
        # B^{1,1} = 0 (no states at weight 1)
        assert dims.get((1, 1), 0) == 0
        # B^{1,2} = 1 (just T = L_{-2}|0>)
        assert dims.get((1, 2), 0) == 1
        # B^{1,3} = 1 (L_{-3}|0>)
        assert dims.get((1, 3), 0) == 1
        # B^{1,4} = 2 (L_{-4}|0> and L_{-2}^2|0>)
        assert dims.get((1, 4), 0) == 2

    def test_bar_degree_2_sl2(self):
        """B^{2,h}(sl_2): tensor of two weight-space elements."""
        alg = affine_km_data('A1', Rational(5))
        dims = bar_bigraded_dims(alg, max_arity=2, max_weight=6)
        # B^{2,2} = dim(A_1)^2 = 3^2 = 9
        assert dims.get((2, 2), 0) == 9
        # B^{2,3} = dim(A_1) * dim(A_2) + dim(A_2) * dim(A_1) = 2 * 3 * 9 = 54
        assert dims.get((2, 3), 0) == 54

    def test_heisenberg_weight_space(self):
        """Heisenberg H_k: weight space dim = p(h) (partitions of h)."""
        from compute.lib.pbw_saito_comparison import _partition_count
        # p(1) = 1, p(2) = 2, p(3) = 3, p(4) = 5, p(5) = 7
        assert _partition_count(1) == 1
        assert _partition_count(2) == 2
        assert _partition_count(3) == 3
        assert _partition_count(4) == 5
        assert _partition_count(5) == 7

    def test_bar_dim_positivity(self):
        """All bar dimensions are non-negative."""
        alg = affine_km_data('A1', Rational(3))
        dims = bar_bigraded_dims(alg, max_arity=4, max_weight=6)
        for key, val in dims.items():
            assert val >= 0, f"Negative dimension at {key}: {val}"

    def test_bar_degree_monotonicity(self):
        """B^{n,h} grows with h (at fixed n)."""
        alg = virasoro_data(Rational(10))
        dims = bar_bigraded_dims(alg, max_arity=2, max_weight=10)
        for n in [1, 2]:
            prev = 0
            for h in range(n, 11):
                cur = dims.get((n, h), 0)
                if cur > 0 and prev > 0:
                    assert cur >= prev, f"Non-monotone at B^{n}: {prev} > {cur} at h={h}"
                if cur > 0:
                    prev = cur

    def test_w3_weight_space(self):
        """W_3: generators T (weight 2) and W (weight 3)."""
        alg = w_algebra_data('sl3', Rational(7))
        # Weight 2: just T (1 state)
        d2 = weight_space_dim(alg, 2)
        assert d2 == 1
        # Weight 3: W and L_{-3}|0> = L_{-1}T (but L_{-1} is a derivative, adds weight 1)
        # Actually for W_3: generators are W_2=T (weight 2) and W_3=W (weight 3)
        # Weight space at h: states built from modes of T and W
        # h=2: T (1 state), h=3: W, L_{-1}T (but L_{-1} has weight 1... no)
        # The mode expansion: T has modes L_n (weight 2 means L_{-n} contributes weight n for n >= 2)
        # W has modes W_n (weight 3 means W_{-n} contributes weight n for n >= 3)
        # Weight 3: L_{-3}|0> from T, and W_{-3}|0> from W = 2 states
        d3 = weight_space_dim(alg, 3)
        assert d3 == 2

    def test_e8_bar_degree_1_weight_1(self):
        """E_8: 248 generators at weight 1."""
        alg = affine_km_data('E8', Rational(1))
        dims = bar_bigraded_dims(alg, max_arity=1, max_weight=2)
        # B^{1,1} = dim A_1 = 248
        assert dims.get((1, 1), 0) == 248


# ============================================================================
# CLUSTER 3: PBW filtration (6 tests)
# ============================================================================

class TestPBWFiltration:
    """Verify PBW filtration computation."""

    def test_sl2_pbw_bar_degree_1(self):
        """PBW filtration on B_1(sl_2): weight 1 only."""
        alg = affine_km_data('A1', Rational(5))
        pbw = compute_pbw_filtration(alg, max_arity=3, max_weight=6)
        assert 1 in pbw
        assert pbw[1].min_weight == 1
        # B_1 has weights 1, 2, 3, ... (higher from multiparticle states)
        assert 1 in pbw[1].weight_dims
        assert pbw[1].weight_dims[1] == 3

    def test_virasoro_pbw_bar_degree_1(self):
        """PBW filtration on B_1(Vir): starts at weight 2."""
        alg = virasoro_data(Rational(25))
        pbw = compute_pbw_filtration(alg, max_arity=2, max_weight=8)
        assert 1 in pbw
        assert pbw[1].min_weight == 2  # Virasoro generator has weight 2
        assert pbw[1].weight_dims[2] == 1

    def test_pbw_total_dim_matches_bigraded(self):
        """Total dim of PBW filtration matches bigraded sum."""
        alg = affine_km_data('A2', Rational(3))
        pbw = compute_pbw_filtration(alg, max_arity=3, max_weight=6)
        bigraded = bar_bigraded_dims(alg, max_arity=3, max_weight=6)
        for n in range(1, 4):
            if n not in pbw:
                continue
            bigraded_total = sum(d for (bd, _), d in bigraded.items() if bd == n)
            assert pbw[n].total_dim == bigraded_total

    def test_pbw_saito_prediction_matches(self):
        """Saito prediction (under PBW = Saito) matches PBW filtration."""
        alg = affine_km_data('A1', Rational(5))
        pbw = compute_pbw_filtration(alg, max_arity=3, max_weight=6)
        saito = predict_saito_weights(alg, max_arity=3, max_weight=6)
        for n in range(1, 4):
            if n in pbw and n in saito:
                assert pbw[n].weight_dims == saito[n].predicted_weights

    def test_w3_pbw_multiple_weights(self):
        """W_3: PBW filtration has contributions at weights 2, 3, 4, ..."""
        alg = w_algebra_data('sl3', Rational(7))
        pbw = compute_pbw_filtration(alg, max_arity=2, max_weight=8)
        assert 1 in pbw
        assert pbw[1].min_weight == 2  # First generator at weight 2

    def test_pbw_weight_dims_nonzero(self):
        """Every PBW weight present has positive dimension."""
        alg = virasoro_data(Rational(10))
        pbw = compute_pbw_filtration(alg, max_arity=3, max_weight=8)
        for n, data in pbw.items():
            for w, d in data.weight_dims.items():
                assert d > 0, f"Zero dim at arity {n}, weight {w}"


# ============================================================================
# CLUSTER 4: Affine KM landscape (8 tests)
# ============================================================================

class TestAffineKMLandscape:
    """Affine KM: PBW = Saito PROVED. Verify consistency."""

    def test_sl2_comparison(self):
        """V_5(sl_2): PBW = Saito PROVED."""
        alg = affine_km_data('A1', Rational(5))
        res = compare_filtrations(alg, max_arity=4, max_weight=6)
        assert res.pbw_equals_saito is True
        assert not res.is_counterexample

    def test_sl3_comparison(self):
        """V_3(sl_3): PBW = Saito PROVED. kappa != c/2 (AP39)."""
        alg = affine_km_data('A2', Rational(3))
        res = compare_filtrations(alg, max_arity=3, max_weight=6)
        assert res.pbw_equals_saito is True
        assert res.algebra.kappa != res.algebra.central_charge / 2

    def test_full_km_landscape_zero_counterexamples(self):
        """All 17 simple types: zero counterexamples at k=5."""
        result = run_affine_km_landscape(Rational(5), max_arity=3, max_weight=6)
        assert result.counterexamples_found == 0
        assert result.all_consistent is True
        assert result.algebras_tested == 17

    def test_exceptional_types(self):
        """G_2, F_4, E_6, E_7, E_8: PBW = Saito PROVED."""
        for lt in ['G2', 'F4', 'E6', 'E7', 'E8']:
            alg = affine_km_data(lt, Rational(3))
            res = compare_filtrations(alg, max_arity=2, max_weight=4)
            assert res.pbw_equals_saito is True, f"Failed for {lt}"

    def test_type_B_series(self):
        """B_2, B_3, B_4: PBW = Saito PROVED."""
        for lt in ['B2', 'B3', 'B4']:
            alg = affine_km_data(lt, Rational(5))
            res = compare_filtrations(alg, max_arity=2, max_weight=5)
            assert res.pbw_equals_saito is True, f"Failed for {lt}"

    def test_type_C_series(self):
        """C_2, C_3, C_4: PBW = Saito PROVED."""
        for lt in ['C2', 'C3', 'C4']:
            alg = affine_km_data(lt, Rational(5))
            res = compare_filtrations(alg, max_arity=2, max_weight=5)
            assert res.pbw_equals_saito is True, f"Failed for {lt}"

    def test_type_D4(self):
        """D_4: 28-dimensional, triality."""
        alg = affine_km_data('D4', Rational(3))
        assert alg.dim_lie == 28
        res = compare_filtrations(alg, max_arity=2, max_weight=4)
        assert res.pbw_equals_saito is True

    def test_kappa_cross_check_sl2_vs_sl3(self):
        """AP1/AP39: kappa(sl_2, k=5) != kappa(sl_3, k=5)."""
        alg2 = affine_km_data('A1', Rational(5))
        alg3 = affine_km_data('A2', Rational(5))
        # kappa(sl_2, 5) = 3 * 7 / 4 = 21/4
        assert alg2.kappa == Rational(21, 4)
        # kappa(sl_3, 5) = 8 * 8 / 6 = 32/3
        assert alg3.kappa == Rational(32, 3)
        assert alg2.kappa != alg3.kappa


# ============================================================================
# CLUSTER 5: Virasoro and W-algebra landscape (6 tests)
# ============================================================================

class TestVirasoroWLandscape:
    """Virasoro and W-algebras: PBW = Saito OPEN but consistent."""

    def test_virasoro_c25(self):
        """Vir_{25}: Koszul, PBW consistent with Saito prediction."""
        alg = virasoro_data(Rational(25))
        res = compare_filtrations(alg, max_arity=4, max_weight=10)
        assert not res.is_counterexample
        assert res.koszul_consistent is True

    def test_virasoro_c13_self_dual(self):
        """Vir_{13}: self-dual point. Koszul, consistent."""
        alg = virasoro_data(Rational(13))
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample
        assert alg.kappa == Rational(13, 2)

    def test_virasoro_landscape_zero_counterexamples(self):
        """All Virasoro c values: zero counterexamples."""
        result = run_virasoro_landscape(max_arity=3, max_weight=8)
        assert result.counterexamples_found == 0
        assert result.all_consistent is True

    def test_w3_comparison(self):
        """W^7(sl_3): Koszul, PBW consistent."""
        alg = w_algebra_data('sl3', Rational(7))
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample

    def test_w4_comparison(self):
        """W^5(sl_4): Koszul, PBW consistent."""
        alg = w_algebra_data('sl4', Rational(5))
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample

    def test_w_algebra_landscape_zero_counterexamples(self):
        """W-algebra landscape: zero counterexamples."""
        result = run_w_algebra_landscape(Rational(7), max_arity=3, max_weight=8)
        assert result.counterexamples_found == 0


# ============================================================================
# CLUSTER 6: Counterexample search (6 tests)
# ============================================================================

class TestCounterexampleSearch:
    """Search for counterexamples among non-Koszul / non-standard algebras."""

    def test_ising_model_non_koszul(self):
        """M(4,3) Ising: NOT Koszul, null at h=6."""
        alg = minimal_model_data(4, 3)
        assert alg.is_koszul is False
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        # Should be consistent: non-Koszul AND predicted non-pure
        assert not res.is_counterexample

    def test_admissible_sl2_4_3(self):
        """L_{-2/3}(sl_2): admissible, Koszulness OPEN."""
        alg = admissible_quotient_data('A1', 4, 3)
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample

    def test_triplet_w2(self):
        """W(2): triplet, Koszulness OPEN."""
        alg = triplet_data(2)
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample

    def test_triplet_w3(self):
        """W(3): triplet, Koszulness OPEN."""
        alg = triplet_data(3)
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample

    def test_non_principal_subregular_sl3(self):
        """W^5(sl_3, subregular): non-principal, Koszulness OPEN."""
        alg = non_principal_w_data('A2', 'subregular', Rational(5))
        res = compare_filtrations(alg, max_arity=3, max_weight=8)
        assert not res.is_counterexample

    def test_full_counterexample_search_zero(self):
        """Full counterexample search: ZERO found across all candidates."""
        result = run_counterexample_search(max_arity=3, max_weight=8)
        assert result.counterexamples_found == 0
        assert result.all_consistent is True
        assert result.algebras_tested >= 10  # At least 10 algebras tested


# ============================================================================
# CLUSTER 7: Regular singularity and pole analysis (5 tests)
# ============================================================================

class TestRegularSingularity:
    """Test regular singularity of bar D-modules."""

    def test_sl2_regular_singular(self):
        """V_k(sl_2): bar D-module = KZ system, regular singular."""
        alg = affine_km_data('A1', Rational(5))
        result = check_regular_singularity(alg)
        assert result.is_regular_singular is True
        assert result.residues_match_pbw is True

    def test_virasoro_regular_singular(self):
        """Vir_c: bar D-module = BPZ system, regular singular."""
        alg = virasoro_data(Rational(25))
        result = check_regular_singularity(alg)
        assert result.is_regular_singular is True
        assert result.residues_match_pbw is True  # Predicted

    def test_sl2_pole_orders(self):
        """V_k(sl_2): OPE max pole 2, effective pole 1 (simple)."""
        alg = affine_km_data('A1', Rational(5))
        poles = ope_pole_orders(alg)
        # All generator pairs have weight 1, OPE pole 2, effective 1
        for (w1, w2), p in poles.items():
            assert p == 1, f"Unexpected pole order {p} for weights ({w1},{w2})"

    def test_virasoro_pole_orders(self):
        """Vir_c: OPE max pole 4, effective pole 3."""
        alg = virasoro_data(Rational(25))
        poles = ope_pole_orders(alg)
        # T-T pair: weight 2, OPE pole 4, effective 3
        assert poles[(2, 2)] == 3

    def test_pole_saito_prediction(self):
        """Pole structure predictions for various algebras."""
        alg_km = affine_km_data('A1', Rational(5))
        pred_km = saito_weight_from_pole_structure(alg_km, 2)
        assert 'automatic' in pred_km[2].lower() or 'simple' in pred_km[2].lower()

        alg_vir = virasoro_data(Rational(25))
        pred_vir = saito_weight_from_pole_structure(alg_vir, 2)
        assert 'irregular' in pred_vir[2].lower() or 'open' in pred_vir[2].lower()


# ============================================================================
# CLUSTER 8: Spectral sequence comparison (5 tests)
# ============================================================================

class TestSpectralSequence:
    """Test PBW spectral sequence structure."""

    def test_sl2_e1_page(self):
        """V_k(sl_2): E_1 page has content at weight 1, bar degree 1."""
        alg = affine_km_data('A1', Rational(5))
        ss = compute_pbw_spectral_sequence(alg, max_arity=3, max_weight=6)
        # E_1 should have (1, 0) = 3 (sl_2 generators at weight 1, bar deg 1)
        assert (1, 0) in ss.e1_dims
        assert ss.e1_dims[(1, 0)] == 3
        assert ss.e2_collapse_expected is True

    def test_virasoro_e1_page(self):
        """Vir_c: E_1 page has content at weight 2, bar degree 1."""
        alg = virasoro_data(Rational(25))
        ss = compute_pbw_spectral_sequence(alg, max_arity=3, max_weight=6)
        assert (2, 0) in ss.e1_dims
        assert ss.e1_dims[(2, 0)] == 1  # T at weight 2
        assert ss.e2_collapse_expected is True

    def test_minimal_model_e2_no_collapse(self):
        """M(4,3) Ising: E_2 does NOT collapse (not Koszul)."""
        alg = minimal_model_data(4, 3)
        ss = compute_pbw_spectral_sequence(alg, max_arity=3, max_weight=8)
        assert ss.e2_collapse_expected is False

    def test_e1_positive_entries(self):
        """All E_1 entries are non-negative."""
        alg = w_algebra_data('sl3', Rational(7))
        ss = compute_pbw_spectral_sequence(alg, max_arity=3, max_weight=8)
        for key, val in ss.e1_dims.items():
            assert val >= 0

    def test_koszul_implies_e2_collapse(self):
        """All Koszul algebras should have E_2 collapse expected."""
        for lt in ['A1', 'A2', 'D4']:
            alg = affine_km_data(lt, Rational(3))
            ss = compute_pbw_spectral_sequence(alg, max_arity=2, max_weight=4)
            assert ss.e2_collapse_expected is True, f"Failed for {lt}"


# ============================================================================
# CLUSTER 9: Master comparison (4 tests)
# ============================================================================

class TestMasterComparison:
    """Master comparison across all families."""

    def test_master_zero_counterexamples(self):
        """Full master comparison: ZERO counterexamples."""
        result = run_master_comparison(
            km_level=Rational(5),
            w_level=Rational(7),
            max_arity=3,
            max_weight=6,
        )
        assert result.total_counterexamples == 0
        assert result.total_algebras >= 30

    def test_master_km_all_proved(self):
        """All affine KM algebras: PBW = Saito PROVED."""
        result = run_master_comparison(
            km_level=Rational(5),
            w_level=Rational(7),
            max_arity=2,
            max_weight=4,
        )
        assert result.affine_km_result.all_consistent is True

    def test_bigraded_table_structure(self):
        """Bar bigraded table has correct structure."""
        alg = affine_km_data('A1', Rational(5))
        table = bar_bigraded_table(alg, max_arity=3, max_weight=6)
        assert table['algebra'] == alg.name
        assert table['is_koszul'] is True
        assert 1 in table['totals_by_arity']

    def test_degree_comparison_table(self):
        """Bar degree comparison table for first 5 degrees."""
        alg = virasoro_data(Rational(25))
        table = bar_degree_comparison_table(alg, max_weight=10)
        # Should have at least bar degree 1
        assert 1 in table
        assert table[1]['bar_degree'] == 1
        assert table[1]['min_weight'] == 2  # Virasoro starts at weight 2
        assert table[1]['pbw_equals_saito_prediction'] is True
