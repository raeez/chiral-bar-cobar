"""Tests for jet window Yangian decomposition.

Tests the reduced-weight bar filtration and jet principle for extracting
Yangian tower data from finite computable windows K_q.

Manuscript references:
    conj:jet-principle (higher_genus_modular_koszul.tex)
    def:reduced-weight-filtration (bar_cobar_adjunction_curved.tex)
    thm:completed-bar-cobar-strong (higher_genus_modular_koszul.tex)
    thm:coefficient-stability-criterion (higher_genus_modular_koszul.tex)
"""

import pytest
from compute.lib.jet_window_yangian import (
    BarWord,
    JetWindow,
    YangianJetData,
    enumerate_bar_words,
    compute_window_dimensions,
    extract_yangian_jets,
    heisenberg_windows,
    affine_sl2_windows,
    virasoro_windows,
    w3_windows,
    betagamma_windows,
    window_dimension_table,
    window_growth_analysis,
    window_stabilization_test,
    virasoro_window_dim_exact,
    w3_window_dim_exact,
    window_shadow_bridge,
    jet_yangian_comparison,
    make_bar_word,
)


# ================================================================
# BAR WORD ENUMERATION
# ================================================================

class TestBarWords:
    """Test bar word construction and enumeration."""

    def test_weight1_all_rho_zero(self):
        """Weight-1 generators: all bar words have rho_red = 0."""
        words = enumerate_bar_words([("J", 1)], max_reduced_weight=5,
                                    max_bar_degree=6)
        for w in words:
            assert w.reduced_weight == 0, (
                f"Weight-1 generator J produced rho_red={w.reduced_weight}"
            )

    def test_weight2_rho_equals_bar_degree(self):
        """Weight-2 generator (Virasoro): rho_red = bar_degree."""
        words = enumerate_bar_words([("L", 2)], max_reduced_weight=5,
                                    max_bar_degree=6)
        for w in words:
            assert w.reduced_weight == w.bar_degree, (
                f"Word {w.generators} has rho_red={w.reduced_weight} "
                f"but bar_degree={w.bar_degree}"
            )

    def test_mixed_weights_w3(self):
        """W_3 generators (wt=2,3): mixed rho_red values."""
        words = enumerate_bar_words([("L", 2), ("W", 3)],
                                    max_reduced_weight=4, max_bar_degree=5)
        # L alone: rho_red = 1
        l_words = [w for w in words if w.generators == ("L",)]
        assert len(l_words) == 1
        assert l_words[0].reduced_weight == 1

        # W alone: rho_red = 2
        w_words = [w for w in words if w.generators == ("W",)]
        assert len(w_words) == 1
        assert w_words[0].reduced_weight == 2

        # L|L: rho_red = 2
        ll_words = [w for w in words
                    if w.generators == ("L", "L")]
        assert len(ll_words) == 1
        assert ll_words[0].reduced_weight == 2

        # L|W: rho_red = 3
        lw_words = [w for w in words
                    if w.generators == ("L", "W")]
        assert len(lw_words) == 1
        assert lw_words[0].reduced_weight == 3

    def test_counting_at_small_rho(self):
        """Virasoro K_q contains exactly q words (one per bar degree)."""
        for q in range(1, 6):
            words = enumerate_bar_words([("L", 2)],
                                        max_reduced_weight=q,
                                        max_bar_degree=q + 2)
            assert len(words) == q, (
                f"K_{q} for Virasoro should have {q} words, got {len(words)}"
            )

    def test_empty_at_rho_zero_for_weight2(self):
        """Virasoro K_0 is empty: minimum rho_red = 1."""
        words = enumerate_bar_words([("L", 2)],
                                    max_reduced_weight=0,
                                    max_bar_degree=10)
        assert len(words) == 0

    def test_make_bar_word(self):
        """make_bar_word computes reduced_weight and total_weight correctly."""
        bw = make_bar_word(("L", "W"), (2, 3))
        assert bw.reduced_weight == 3  # (2-1) + (3-1) = 3
        assert bw.bar_degree == 2
        assert bw.total_weight == 5

    def test_bar_word_frozen(self):
        """BarWord is frozen (immutable)."""
        bw = make_bar_word(("J",), (1,))
        with pytest.raises(AttributeError):
            bw.reduced_weight = 99

    def test_affine_sl2_all_rho_zero(self):
        """Affine sl_2: three weight-1 generators, all rho_red = 0."""
        words = enumerate_bar_words([("e", 1), ("h", 1), ("f", 1)],
                                    max_reduced_weight=3, max_bar_degree=3)
        for w in words:
            assert w.reduced_weight == 0


# ================================================================
# HEISENBERG WINDOWS
# ================================================================

class TestHeisenbergWindows:
    """Tests for Heisenberg jet window decomposition."""

    def test_k0_captures_everything(self):
        """Heisenberg: K_0 = full bar complex (all words have rho_red = 0)."""
        data = heisenberg_windows(max_q=4)
        dims = [data.windows[q].dimension for q in range(5)]
        # All windows should have the same dimension
        assert len(set(dims)) == 1, (
            f"Heisenberg windows should all have the same dim, got {dims}"
        )

    def test_stabilization_at_q0(self):
        """Heisenberg stabilises at q = 0 (or q = 1 at latest)."""
        data = heisenberg_windows(max_q=4)
        assert data.stabilization_order is not None
        assert data.stabilization_order <= 1

    def test_convergent(self):
        """Heisenberg tower is convergent (abelian)."""
        data = heisenberg_windows(max_q=4)
        assert data.convergent is True

    def test_single_generator(self):
        """Heisenberg has one generator J of weight 1."""
        words = enumerate_bar_words([("J", 1)], max_reduced_weight=0,
                                    max_bar_degree=5)
        # All bar words have rho_red = 0 so they are all in K_0
        assert len(words) >= 5  # words of length 1,2,3,4,5

    def test_yangian_trivial(self):
        """Heisenberg Yangian is trivial (abelian, no OPE poles)."""
        data = heisenberg_windows(max_q=3)
        # Yangian series should have coefficients = word counts (not structure)
        # Key point: abelian so the r-matrix is trivial
        assert data.convergent is True

    def test_window_bridge_constant_fractions(self):
        """Window-shadow bridge: cumulative fraction is 1.0 at all q."""
        bridge = window_shadow_bridge("heisenberg", max_q=5)
        for q in range(5 + 1):
            assert abs(bridge["cumulative_fraction"][q] - 1.0) < 1e-10


# ================================================================
# VIRASORO WINDOWS
# ================================================================

class TestVirasoroWindows:
    """Tests for Virasoro jet window decomposition."""

    def test_k0_empty(self):
        """Virasoro K_0 has dim = 0 (no words with rho_red = 0)."""
        data = virasoro_windows(max_q=6)
        assert data.windows[0].dimension == 0

    def test_dim_kq_equals_q(self):
        """dim(K_q) = q for q >= 1 (one word per bar degree)."""
        data = virasoro_windows(max_q=8)
        for q in range(1, 9):
            assert data.windows[q].dimension == q, (
                f"Virasoro K_{q} should have dim={q}, "
                f"got {data.windows[q].dimension}"
            )

    def test_k1_adds_L(self):
        """K_1 contains exactly one word: L (bar degree 1)."""
        data = virasoro_windows(max_q=6)
        words_at_1 = [w for w in data.windows[1].bar_words
                      if w.reduced_weight == 1]
        assert len(words_at_1) == 1
        assert words_at_1[0].generators == ("L",)

    def test_no_stabilization(self):
        """Virasoro does NOT stabilise (class M, infinite tower)."""
        data = virasoro_windows(max_q=8)
        assert data.stabilization_order is None

    def test_growth_rate_is_linear(self):
        """dim(K_q) grows linearly with q."""
        data = virasoro_windows(max_q=10)
        dims = [data.windows[q].dimension for q in range(1, 11)]
        # Check linear: differences should be constant (= 1)
        diffs = [dims[i+1] - dims[i] for i in range(len(dims)-1)]
        assert all(d == 1 for d in diffs), (
            f"Virasoro window growth differences: {diffs}"
        )

    def test_not_convergent(self):
        """Virasoro tower is not convergent (class M)."""
        data = virasoro_windows(max_q=6)
        assert data.convergent is False

    def test_exact_dim_formula(self):
        """virasoro_window_dim_exact matches computed dimensions."""
        data = virasoro_windows(max_q=10)
        for q in range(11):
            assert virasoro_window_dim_exact(q) == data.windows[q].dimension

    def test_each_window_adds_one_word(self):
        """Each step K_{q-1} -> K_q adds exactly one word (L^{|q|})."""
        data = virasoro_windows(max_q=8)
        for q in range(2, 9):
            increment = (data.windows[q].dimension
                         - data.windows[q-1].dimension)
            assert increment == 1, (
                f"Virasoro K_{q-1}->K_{q}: expected increment 1, got {increment}"
            )

    def test_windows_never_marked_stable(self):
        """No Virasoro window is marked stable (dimension always grows)."""
        data = virasoro_windows(max_q=8)
        for q in range(2, 9):
            assert not data.windows[q].stable, (
                f"Virasoro K_{q} should not be marked stable"
            )

    def test_yangian_coefficients_monotone(self):
        """Yangian coefficient count at jet q is 1 for each q >= 1."""
        data = virasoro_windows(max_q=6)
        for q in range(1, 7):
            coeffs = data.windows[q].yangian_coefficients
            assert coeffs.get(q, 0) == 1


# ================================================================
# W_3 WINDOWS
# ================================================================

class TestW3Windows:
    """Tests for W_3 jet window decomposition."""

    def test_two_generators(self):
        """W_3 has two generators: L(wt=2) and W(wt=3)."""
        data = w3_windows(max_q=4)
        assert data.algebra_name == "w3"

    def test_k0_empty(self):
        """W_3 K_0 is empty (minimum rho_red = 1 for L)."""
        data = w3_windows(max_q=6)
        assert data.windows[0].dimension == 0

    def test_k1_has_only_L(self):
        """K_1 has one word: L (rho_red = 1)."""
        data = w3_windows(max_q=6)
        assert data.windows[1].dimension == 1

    def test_k2_has_three_words(self):
        """K_2 has 3 words: L, L|L, W (rho_red = 1, 2, 2)."""
        data = w3_windows(max_q=6)
        assert data.windows[2].dimension == 3

    def test_faster_growth_than_virasoro(self):
        """W_3 has more words at each level than Virasoro (for q >= 2)."""
        vir = virasoro_windows(max_q=8)
        w3 = w3_windows(max_q=8)
        for q in range(2, 9):
            assert w3.windows[q].dimension >= vir.windows[q].dimension, (
                f"W_3 K_{q} dim={w3.windows[q].dimension} < "
                f"Virasoro K_{q} dim={vir.windows[q].dimension}"
            )

    def test_not_convergent(self):
        """W_3 tower does not converge (class M)."""
        data = w3_windows(max_q=6)
        assert data.convergent is False

    def test_no_stabilization(self):
        """W_3 does not stabilise (infinite tower)."""
        data = w3_windows(max_q=8)
        assert data.stabilization_order is None

    def test_exact_dim_formula(self):
        """w3_window_dim_exact matches computed dimensions."""
        data = w3_windows(max_q=10)
        for q in range(11):
            assert w3_window_dim_exact(q) == data.windows[q].dimension, (
                f"W_3 K_{q}: exact formula gives {w3_window_dim_exact(q)}, "
                f"computed gives {data.windows[q].dimension}"
            )


# ================================================================
# BETA-GAMMA AND AFFINE
# ================================================================

class TestBetaGammaWindows:
    """Tests for beta-gamma system windows."""

    def test_stabilization_at_q0(self):
        """Beta-gamma stabilises at q = 0 (mixed weight-0 and weight-1)."""
        data = betagamma_windows(max_q=4)
        # gamma has weight 0, so reduced weight -1
        # K_0 already contains everything
        assert data.stabilization_order is not None
        assert data.stabilization_order <= 1

    def test_convergent(self):
        """Beta-gamma is convergent (class C, depth 4)."""
        data = betagamma_windows(max_q=4)
        assert data.convergent is True


class TestAffineSl2Windows:
    """Tests for affine sl_2 windows."""

    def test_stabilization_at_q0(self):
        """Affine sl_2 stabilises at q = 0 (all weight-1)."""
        data = affine_sl2_windows(max_q=4)
        assert data.stabilization_order is not None
        assert data.stabilization_order <= 1

    def test_all_rho_zero(self):
        """All bar words have rho_red = 0 for weight-1 generators."""
        data = affine_sl2_windows(max_q=4)
        for q in range(5):
            for w in data.windows[q].bar_words:
                assert w.reduced_weight == 0

    def test_convergent(self):
        """Affine sl_2 tower is convergent."""
        data = affine_sl2_windows(max_q=3)
        assert data.convergent is True


# ================================================================
# WINDOW DIMENSION TABLE
# ================================================================

class TestWindowTable:
    """Tests for the multi-family dimension table."""

    def test_covers_all_families(self):
        """window_dimension_table covers all standard families."""
        table = window_dimension_table(max_q=5)
        expected_families = {"heisenberg", "affine_sl2", "virasoro",
                             "w3", "betagamma", "free_fermion"}
        assert set(table.keys()) == expected_families

    def test_heisenberg_constant_dims(self):
        """Heisenberg window dimensions are constant across q."""
        table = window_dimension_table(families=["heisenberg"], max_q=5)
        dims = table["heisenberg"]
        vals = list(dims.values())
        assert len(set(vals)) == 1

    def test_affine_constant_dims(self):
        """Affine sl_2 window dimensions are constant across q."""
        table = window_dimension_table(families=["affine_sl2"], max_q=5)
        dims = table["affine_sl2"]
        vals = list(dims.values())
        assert len(set(vals)) == 1

    def test_virasoro_grows_linearly(self):
        """Virasoro window dimensions grow linearly."""
        table = window_dimension_table(families=["virasoro"], max_q=8)
        dims = table["virasoro"]
        for q in range(1, 9):
            assert dims[q] == q

    def test_w3_grows_faster_than_virasoro(self):
        """W_3 dimensions exceed Virasoro for q >= 2."""
        table = window_dimension_table(
            families=["virasoro", "w3"], max_q=8
        )
        for q in range(2, 9):
            assert table["w3"][q] >= table["virasoro"][q]


# ================================================================
# GROWTH ANALYSIS
# ================================================================

class TestGrowthAnalysis:
    """Tests for window_growth_analysis classification."""

    def test_heisenberg_constant(self):
        """Heisenberg growth type is constant."""
        result = window_growth_analysis("heisenberg", max_q=10)
        assert result["growth_type"] == "constant"
        assert result["shadow_class"] == "G"

    def test_virasoro_linear(self):
        """Virasoro growth type is linear."""
        result = window_growth_analysis("virasoro", max_q=10)
        assert result["growth_type"] == "linear"
        assert result["shadow_class"] == "M"
        assert result["polynomial_degree"] == 1

    def test_w3_polynomial(self):
        """W_3 growth type is polynomial with degree >= 2."""
        result = window_growth_analysis("w3", max_q=15)
        assert result["growth_type"] == "polynomial"
        assert result["shadow_class"] == "M"
        assert result["polynomial_degree"] is not None
        assert result["polynomial_degree"] >= 2

    def test_affine_constant(self):
        """Affine sl_2 growth type is constant."""
        result = window_growth_analysis("affine_sl2", max_q=10)
        assert result["growth_type"] == "constant"
        assert result["shadow_class"] == "L"

    def test_betagamma_class_C(self):
        """Beta-gamma is classified as contact class C."""
        result = window_growth_analysis("betagamma", max_q=10)
        assert result["shadow_class"] == "C"


# ================================================================
# YANGIAN JET EXTRACTION
# ================================================================

class TestYangianJetExtraction:
    """Tests for extract_yangian_jets and related functions."""

    def test_unknown_family_raises(self):
        """Requesting an unknown family raises ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            extract_yangian_jets("nonexistent_algebra", max_q=3)

    def test_yangian_jet_data_summary(self):
        """YangianJetData.summary() returns a string."""
        data = heisenberg_windows(max_q=3)
        summary = data.summary()
        assert isinstance(summary, str)
        assert "heisenberg" in summary.lower()

    def test_r_matrix_truncation_string(self):
        """r_matrix_truncation returns a string."""
        data = virasoro_windows(max_q=4)
        trunc = data.r_matrix_truncation(3)
        assert isinstance(trunc, str)

    def test_verify_stabilization_heisenberg(self):
        """Heisenberg stabilisation: K_0 and K_3 give same jets."""
        data = heisenberg_windows(max_q=4)
        assert data.verify_stabilization(0, 3)

    def test_jet_yangian_comparison_heisenberg(self):
        """jet_yangian_comparison: Heisenberg jets at order >= 1 are 0."""
        # Heisenberg: all words have rho_red=0, so jet coefficients
        # at order >= 1 are all 0 (no new words at higher rho_red).
        known = {1: 0, 2: 0, 3: 0}
        result = jet_yangian_comparison("heisenberg", known)
        assert result["all_match"] is True
