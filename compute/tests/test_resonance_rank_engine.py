"""Tests for resonance rank classification and MC4 splitting engine.

Ground truth from the manuscript:
  def:resonance-rank: rho(A) = dim of weight-0 resonance subspace
  thm:resonance-filtered-bar-cobar: rho < inf => finite completion steps
  thm:coefficient-stability-criterion: coefficient stabilization
  conj:platonic-completion: rho < inf for all positive-energy algebras
  thm:stabilized-completion-positive: MC4+ automatic for rho = 0

MC4 splitting (concordance.tex):
  MC4+ (positive): Heisenberg, affine, betagamma, W_{1+inf}. rho = 0.
  MC4^0 (resonant): Virasoro, W_N (finite N). rho >= 1.

Virasoro resonance shadow (CLAUDE.md):
  Vir_c^! = Vir_{26-c}. Self-dual at c = 13. Ghost at c = 26.

Weight generating functions:
  Heisenberg:   1/(1-t)
  Affine sl_2:  1/(1-t)^3
  Virasoro:     prod_{n>=2} 1/(1-t^n)
  W_3:          prod_{n>=2} 1/(1-t^n) * prod_{n>=3} 1/(1-t^n)
  betagamma:    1/(1-t)^2
  W_infinity:   prod_{n>=1} 1/(1-t^n) = sum p(q) t^q
"""

import math

import pytest

from compute.lib.resonance_rank_engine import (
    reduced_weight_windows,
    resonance_rank,
    mc4_class,
    coefficient_stabilization_test,
    virasoro_resonance_shadow,
    platonic_completion_check,
    platonic_completion_all,
    weight_generating_function,
    entropy_from_windows,
    entropy_sqrt_normalized,
    hardy_ramanujan_entropy,
    stabilization_defect,
    w_n_resonance_rank,
    shadow_depth,
    shadow_archetype,
    classification_table,
    virasoro_k_q_exact,
    virasoro_gf_euler_product,
    virasoro_gf_from_unrestricted,
    w_n_weight_windows,
    w_n_gf_ratio_at_large_q,
    ALL_STANDARD_FAMILIES,
)
from compute.lib.utils import partition_number


# ===========================================================================
# Reduced-weight windows K_q(A)
# ===========================================================================

class TestReducedWeightWindows:
    """K_q(A) = weight-q bar cohomology dimension."""

    def test_heisenberg_windows(self):
        """K_q(Heis) = 1 for all q.  One generator of weight 1."""
        K = reduced_weight_windows("heisenberg", max_q=15)
        assert len(K) == 16
        assert all(k == 1 for k in K)

    def test_affine_sl2_windows(self):
        """K_q(V_k(sl_2)) = (q+1)(q+2)/2.  Three generators of weight 1."""
        K = reduced_weight_windows("affine_sl2", max_q=10)
        expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]
        assert K == expected

    def test_affine_sl2_is_binom(self):
        """K_q = binom(q+2, 2) for affine sl_2."""
        K = reduced_weight_windows("affine_sl2", max_q=8)
        for q in range(9):
            assert K[q] == (q + 1) * (q + 2) // 2

    def test_virasoro_windows_partitions(self):
        """K_q(Vir) = partitions of q into parts >= 2."""
        K = reduced_weight_windows("virasoro", max_q=12)
        # Ground truth: comp:virasoro-vacuum
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21]
        assert K == expected

    def test_virasoro_first_10(self):
        """Verify first 10 values of K_q(Vir)."""
        K = reduced_weight_windows("virasoro", max_q=9)
        assert K[0] == 1   # empty partition
        assert K[1] == 0   # no partition of 1 into parts >= 2
        assert K[2] == 1   # {2}
        assert K[3] == 1   # {3}
        assert K[4] == 2   # {4}, {2,2}
        assert K[5] == 2   # {5}, {3,2}
        assert K[6] == 4   # {6}, {4,2}, {3,3}, {2,2,2}
        assert K[7] == 4   # {7}, {5,2}, {4,3}, {3,2,2}
        assert K[8] == 7   # {8}, {6,2}, {5,3}, {4,4}, {4,2,2}, {3,3,2}, {2,2,2,2}
        assert K[9] == 8

    def test_betagamma_windows(self):
        """K_q(betagamma) = q + 1.  Two generators of weight 1."""
        K = reduced_weight_windows("betagamma", max_q=10)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        assert K == expected

    def test_w3_windows_first_values(self):
        """K_q(W_3) for the first few values."""
        K = reduced_weight_windows("w3", max_q=10)
        # W_3: generators at weights >= 2 (L) and >= 3 (W)
        # GF = prod_{n>=2} 1/(1-t^n) * prod_{n>=3} 1/(1-t^n)
        # q=0: 1, q=1: 0, q=2: 1, q=3: 2, q=4: 3, q=5: 4, q=6: 8
        assert K[0] == 1
        assert K[1] == 0   # no generators at weight 1
        assert K[2] == 1   # only L_2
        assert K[3] == 2   # L_3 and W_3

    def test_w_infinity_windows_are_partitions(self):
        """K_q(W_infinity) = p(q) (unrestricted partitions)."""
        K = reduced_weight_windows("w_infinity", max_q=15)
        for q in range(16):
            assert K[q] == partition_number(q)

    def test_free_fermion_windows(self):
        """K_0 = 1, K_1 = 1, K_q = 0 for q >= 2 (exterior algebra)."""
        K = reduced_weight_windows("free_fermion", max_q=5)
        assert K == [1, 1, 0, 0, 0, 0]

    def test_affine_g_dim8(self):
        """K_q for affine g with dim g = 8 (e.g., sl_3)."""
        K = reduced_weight_windows("affine_g", max_q=3, dim_g=8)
        # binom(q+7, 7)
        assert K[0] == 1
        assert K[1] == 8
        assert K[2] == 36   # binom(9,7) = 36
        assert K[3] == 120  # binom(10,7) = 120

    def test_unknown_family_raises(self):
        """Unknown family should raise ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            reduced_weight_windows("unknown_algebra", max_q=5)


# ===========================================================================
# Resonance rank rho(A)
# ===========================================================================

class TestResonanceRank:
    """rho(A) = dim of weight-0 resonance subspace."""

    def test_heisenberg_rho_0(self):
        """Heisenberg: rho = 0 (Gaussian, no resonances)."""
        assert resonance_rank("heisenberg") == 0

    def test_affine_rho_0(self):
        """Affine at non-critical level: rho = 0."""
        assert resonance_rank("affine_sl2") == 0

    def test_virasoro_rho_1(self):
        """Virasoro: rho = 1 (single L_0 resonance direction)."""
        assert resonance_rank("virasoro") == 1

    def test_w3_rho_1(self):
        """W_3: rho = 1 (inherited Virasoro resonance)."""
        assert resonance_rank("w3") == 1

    def test_w_infinity_rho_0(self):
        """W_{1+infinity}: rho = 0 (positive tower, MacMahon limit)."""
        assert resonance_rank("w_infinity") == 0

    def test_betagamma_rho_0(self):
        """betagamma: rho = 0 despite quartic shadow depth."""
        assert resonance_rank("betagamma") == 0

    def test_free_fermion_rho_0(self):
        """Free fermion: rho = 0."""
        assert resonance_rank("free_fermion") == 0

    def test_rho_not_shadow_depth(self):
        """rho and shadow depth are INDEPENDENT invariants.

        betagamma: rho = 0, shadow_depth = 4
        Virasoro:  rho = 1, shadow_depth = inf
        Both are Koszul.
        """
        assert resonance_rank("betagamma") == 0
        assert shadow_depth("betagamma") == 4
        assert resonance_rank("virasoro") == 1
        assert shadow_depth("virasoro") == float("inf")


# ===========================================================================
# MC4 splitting
# ===========================================================================

class TestMC4Splitting:
    """MC4 class assignment: MC4+ or MC4^0."""

    def test_heisenberg_mc4_plus(self):
        assert mc4_class("heisenberg") == "MC4+"

    def test_affine_mc4_plus(self):
        assert mc4_class("affine_sl2") == "MC4+"

    def test_virasoro_mc4_zero(self):
        assert mc4_class("virasoro") == "MC4^0"

    def test_w3_mc4_zero(self):
        assert mc4_class("w3") == "MC4^0"

    def test_betagamma_mc4_plus(self):
        assert mc4_class("betagamma") == "MC4+"

    def test_w_infinity_mc4_plus(self):
        assert mc4_class("w_infinity") == "MC4+"

    def test_w_n_classification(self):
        """All finite W_N are MC4^0; W_infinity is MC4+."""
        for N in [2, 3, 4, 5, 10, 100]:
            assert mc4_class("w_N", N=N) == "MC4^0"
        assert mc4_class("w_infinity") == "MC4+"

    def test_mc4_plus_iff_rho_zero(self):
        """MC4+ <=> rho = 0 for all standard families."""
        for fam in ALL_STANDARD_FAMILIES:
            rho = resonance_rank(fam)
            cls = mc4_class(fam)
            if rho == 0:
                assert cls == "MC4+", f"{fam}: rho=0 but class={cls}"
            else:
                assert cls == "MC4^0", f"{fam}: rho={rho} but class={cls}"


# ===========================================================================
# Coefficient stabilization
# ===========================================================================

class TestCoefficientStabilization:
    """thm:coefficient-stability-criterion tests."""

    def test_heisenberg_immediate(self):
        """Heisenberg: automatic stabilization (rho = 0)."""
        result = coefficient_stabilization_test("heisenberg", max_N=8)
        assert result["automatic"] is True
        assert result["stabilized"] is True
        assert result["class"] == "MC4+"

    def test_virasoro_finite_window(self):
        """Virasoro: stabilization via finite resonance window."""
        result = coefficient_stabilization_test("virasoro", max_N=8)
        assert result["automatic"] is False
        assert result["stabilized"] is True
        assert result["class"] == "MC4^0"
        assert result["resonance_window"] == 1

    def test_all_families_stabilize(self):
        """All standard families have stabilized = True."""
        for fam in ALL_STANDARD_FAMILIES:
            result = coefficient_stabilization_test(fam, max_N=6)
            assert result["stabilized"] is True, f"{fam} failed to stabilize"

    def test_cutoff_at_weight_q(self):
        """MC4+ families: cutoff at arity q for weight q."""
        result = coefficient_stabilization_test("heisenberg", max_N=5)
        for q in range(6):
            assert result["cutoffs"][q] == q


# ===========================================================================
# Virasoro resonance shadow
# ===========================================================================

class TestVirasoroResonance:
    """Virasoro depth-zero resonance shadow: Vir_{26-c}."""

    def test_resonance_shadow_formula(self):
        """c + c_dual = 26."""
        data = virasoro_resonance_shadow(7)
        assert data["c"] == 7
        assert data["c_dual"] == 19
        assert data["complementarity_sum"] == 26

    def test_self_dual_c13(self):
        """Vir_13^! = Vir_13 (self-dual point)."""
        data = virasoro_resonance_shadow(13)
        assert data["self_dual"] is True
        assert data["c_dual"] == 13

    def test_ghost_c26(self):
        """Vir_26^! = Vir_0 (ghost Virasoro)."""
        data = virasoro_resonance_shadow(26)
        assert data["c_dual"] == 0
        assert data["ghost"] is True

    def test_c0_dual_is_26(self):
        """Vir_0^! = Vir_26."""
        data = virasoro_resonance_shadow(0)
        assert data["c_dual"] == 26

    def test_depth_zero_model(self):
        """All Virasoro resonance shadows are depth-zero."""
        for c_val in [0, 1, 7, 13, 25, 26]:
            data = virasoro_resonance_shadow(c_val)
            assert data["depth_zero_resonance"] is True
            assert data["rho"] == 1

    def test_complementarity_generic(self):
        """c + c' = 26 for several values."""
        for c_val in [0, 1, 5, 10, 13, 20, 25, 26]:
            data = virasoro_resonance_shadow(c_val)
            assert data["c"] + data["c_dual"] == 26


# ===========================================================================
# Entropy
# ===========================================================================

class TestEntropy:
    """Bar-cohomology entropy h_K = lim log(K_q)/sqrt(q)."""

    def test_heisenberg_entropy_zero(self):
        """Heisenberg has polynomial growth: entropy -> 0."""
        K = reduced_weight_windows("heisenberg", max_q=50)
        h = entropy_from_windows(K)
        assert h is not None
        assert h == 0.0  # log(1)/q = 0

    def test_affine_entropy_zero(self):
        """Affine has polynomial growth: linear entropy -> 0."""
        K = reduced_weight_windows("affine_sl2", max_q=50)
        h = entropy_from_windows(K)
        # log(K_q)/q ~ log(q^2)/q -> 0
        assert h is not None
        assert h < 0.3  # small for large q

    def test_virasoro_entropy_positive(self):
        """Virasoro has superpolynomial growth: entropy > 0."""
        K = reduced_weight_windows("virasoro", max_q=100)
        h = entropy_from_windows(K)
        assert h is not None
        assert h > 0

    def test_hardy_ramanujan_value(self):
        """pi*sqrt(2/3) ~ 2.565."""
        h_HR = hardy_ramanujan_entropy()
        assert abs(h_HR - math.pi * math.sqrt(2.0 / 3.0)) < 1e-10

    def test_virasoro_sqrt_entropy_approaches_hr(self):
        """h_K(Vir) under sqrt normalization -> pi*sqrt(2/3).

        The Hardy-Ramanujan asymptotics: log p_{>=2}(q) ~ pi*sqrt(2q/3).
        Convergence is slow (O(1/sqrt(q)) correction), so at q=200 the
        estimate is still ~27% below the limit. We verify it is in the
        right ballpark (within 30%) and increasing toward the limit.
        """
        K = reduced_weight_windows("virasoro", max_q=200)
        h = entropy_sqrt_normalized(K)
        h_HR = hardy_ramanujan_entropy()
        assert h is not None
        assert abs(h - h_HR) / h_HR < 0.30
        # Check increasing: q=100 estimate < q=200 estimate
        K_100 = reduced_weight_windows("virasoro", max_q=100)
        h_100 = entropy_sqrt_normalized(K_100)
        assert h_100 is not None
        assert h > h_100  # convergence from below

    def test_w_infinity_sqrt_entropy_approaches_hr(self):
        """W_infinity has the same leading asymptotics as partitions.

        Same slow convergence as Virasoro; verify within 25%.
        """
        K = reduced_weight_windows("w_infinity", max_q=200)
        h = entropy_sqrt_normalized(K)
        h_HR = hardy_ramanujan_entropy()
        assert h is not None
        assert abs(h - h_HR) / h_HR < 0.25

    def test_polynomial_growth_sqrt_entropy_small(self):
        """Polynomial growth: sqrt-normalized entropy is much smaller than HR.

        For K_q ~ q^d: log(q^d)/sqrt(q) = d*log(q)/sqrt(q) -> 0 as q -> inf,
        but at finite q this is still O(log(q)/sqrt(q)). At q=100:
        log(100^2)/sqrt(100) = 2*log(100)/10 ~ 0.92. Still far below HR ~ 2.57.
        """
        K = reduced_weight_windows("affine_sl2", max_q=100)
        h = entropy_sqrt_normalized(K)
        h_HR = hardy_ramanujan_entropy()
        assert h is not None
        assert h < h_HR / 2  # polynomial growth is at most half the HR value


# ===========================================================================
# Weight generating function
# ===========================================================================

class TestWeightGF:
    """Weight generating function G_A(t) = sum K_q t^q."""

    def test_heisenberg_gf(self):
        """G_{Heis}(t) = 1/(1-t).  Coefficients are all 1."""
        G = weight_generating_function("heisenberg", max_q=20)
        assert all(g == 1 for g in G)

    def test_affine_gf(self):
        """G_{aff}(t) = 1/(1-t)^3.  Coefficients are triangular numbers."""
        G = weight_generating_function("affine_sl2", max_q=10)
        for q in range(11):
            assert G[q] == (q + 1) * (q + 2) // 2

    def test_betagamma_gf(self):
        """G_{bg}(t) = 1/(1-t)^2.  Coefficients are q+1."""
        G = weight_generating_function("betagamma", max_q=10)
        for q in range(11):
            assert G[q] == q + 1

    def test_virasoro_gf_euler_product(self):
        """G_{Vir}(t) = prod_{n>=2} 1/(1-t^n)."""
        G_direct = weight_generating_function("virasoro", max_q=20)
        G_euler = virasoro_gf_euler_product(max_q=20)
        assert G_direct == G_euler

    def test_virasoro_gf_two_methods(self):
        """Euler product and unrestricted-partition methods agree."""
        G_euler = virasoro_gf_euler_product(max_q=25)
        G_unres = virasoro_gf_from_unrestricted(max_q=25)
        assert G_euler == G_unres

    def test_virasoro_first_coefficients(self):
        """First coefficients of G_{Vir}(t)."""
        G = weight_generating_function("virasoro", max_q=12)
        assert G == [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21]

    def test_virasoro_k_q_exact_matches(self):
        """virasoro_k_q_exact matches reduced_weight_windows."""
        K = reduced_weight_windows("virasoro", max_q=20)
        for q in range(21):
            assert virasoro_k_q_exact(q) == K[q]

    def test_w_infinity_gf_is_partition_function(self):
        """G_{W_inf}(t) = sum p(q) t^q = prod 1/(1-t^n)."""
        G = weight_generating_function("w_infinity", max_q=15)
        expected = [partition_number(q) for q in range(16)]
        assert G == expected

    def test_w3_gf_exceeds_virasoro(self):
        """W_3 has more generators than Virasoro: K_q(W_3) >= K_q(Vir)."""
        G_vir = weight_generating_function("virasoro", max_q=15)
        G_w3 = weight_generating_function("w3", max_q=15)
        for q in range(16):
            assert G_w3[q] >= G_vir[q]

    def test_w_n_monotone_in_N(self):
        """K_q(W_N) <= K_q(W_{N+1}) for all q (more generators)."""
        for N in [2, 3, 4]:
            K_N = w_n_weight_windows(N, max_q=12)
            K_N1 = w_n_weight_windows(N + 1, max_q=12)
            for q in range(13):
                assert K_N[q] <= K_N1[q], (
                    f"Monotonicity failed at N={N}, q={q}: "
                    f"K_{q}(W_{N}) = {K_N[q]} > K_{q}(W_{N+1}) = {K_N1[q]}"
                )

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro (the spin-2 generator only)."""
        K_vir = reduced_weight_windows("virasoro", max_q=15)
        K_w2 = w_n_weight_windows(2, max_q=15)
        assert K_vir == K_w2


# ===========================================================================
# Resonance completion conjecture
# ===========================================================================

class TestPlatonicCompletion:
    """conj:platonic-completion: rho < infinity for all positive-energy."""

    def test_all_standard_finite(self):
        """All standard families have finite resonance rank."""
        all_ok, data = platonic_completion_all()
        assert all_ok
        for fam, d in data.items():
            assert d["finite"], f"{fam} has infinite rho"

    def test_rho_bounded(self):
        """rho <= 1 for all standard families."""
        for fam in ALL_STANDARD_FAMILIES:
            rho = resonance_rank(fam)
            assert rho <= 1, f"{fam}: rho = {rho} > 1"

    def test_platonic_check_structure(self):
        """platonic_completion_check returns correct structure."""
        data = platonic_completion_check("virasoro")
        assert "family" in data
        assert "rho" in data
        assert "finite" in data
        assert "class" in data
        assert data["rho"] == 1
        assert data["class"] == "MC4^0"


# ===========================================================================
# Stabilization defect
# ===========================================================================

class TestStabilizationDefect:
    """stabilization_defect(family, N): coefficients changing at arity N."""

    def test_heisenberg_defect_is_1(self):
        """Heisenberg: K_N = 1, so defect = 1 at each arity."""
        for N in range(1, 8):
            d = stabilization_defect("heisenberg", N)
            assert d == 1

    def test_virasoro_defect_at_1(self):
        """Virasoro: defect at arity 1 includes resonance contribution."""
        d = stabilization_defect("virasoro", 1)
        # K_1 = 0 (no weight-1 bar cohomology) + rho = 1 (resonance)
        assert d == 1

    def test_defect_at_zero(self):
        """Defect at arity 0 is always 0."""
        for fam in ALL_STANDARD_FAMILIES:
            assert stabilization_defect(fam, 0) == 0


# ===========================================================================
# W_N resonance rank
# ===========================================================================

class TestWNResonanceRank:
    """w_n_resonance_rank(N) for the W_N family."""

    def test_w2_rho_1(self):
        assert w_n_resonance_rank(2) == 1

    def test_w3_rho_1(self):
        assert w_n_resonance_rank(3) == 1

    def test_w4_rho_1(self):
        assert w_n_resonance_rank(4) == 1

    def test_w100_rho_1(self):
        assert w_n_resonance_rank(100) == 1

    def test_w_infinity_rho_0(self):
        assert w_n_resonance_rank(float("inf")) == 0

    def test_w1_raises(self):
        with pytest.raises(ValueError, match="N >= 2"):
            w_n_resonance_rank(1)


# ===========================================================================
# Shadow depth / archetype (cross-check)
# ===========================================================================

class TestShadowCrossCheck:
    """Shadow depth and archetype are independent of resonance rank."""

    def test_archetype_letters(self):
        """All archetypes are G, L, C, or M."""
        for fam in ALL_STANDARD_FAMILIES:
            a = shadow_archetype(fam)
            assert a in ("G", "L", "C", "M"), f"{fam}: archetype = {a}"

    def test_heisenberg_gaussian(self):
        assert shadow_archetype("heisenberg") == "G"
        assert shadow_depth("heisenberg") == 2

    def test_affine_lie_tree(self):
        assert shadow_archetype("affine_sl2") == "L"
        assert shadow_depth("affine_sl2") == 3

    def test_betagamma_contact(self):
        assert shadow_archetype("betagamma") == "C"
        assert shadow_depth("betagamma") == 4

    def test_virasoro_mixed(self):
        assert shadow_archetype("virasoro") == "M"
        assert shadow_depth("virasoro") == float("inf")


# ===========================================================================
# Classification table
# ===========================================================================

class TestClassificationTable:
    """Full classification table."""

    def test_table_has_all_families(self):
        table = classification_table()
        families = {row["family"] for row in table}
        for fam in ALL_STANDARD_FAMILIES:
            assert fam in families

    def test_table_rho_matches(self):
        """Table rho values match resonance_rank()."""
        table = classification_table()
        for row in table:
            assert row["rho"] == resonance_rank(row["family"])

    def test_table_k_q_length(self):
        """Each row has 11 K_q values (q = 0..10)."""
        table = classification_table()
        for row in table:
            assert len(row["K_q_first_11"]) == 11
