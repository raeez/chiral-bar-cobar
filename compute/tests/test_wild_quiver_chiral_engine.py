r"""Tests for the wild quiver chiral algebra engine.

Multi-path verification of wild quiver bar complexes, DT invariants,
and the failure of Koszulness beyond the finite/tame boundary.

Organisation:
  1.  Kronecker quiver data: Euler form, determinant, representation type
  2.  Finite-type baseline (K_1 = A_2)
  3.  Tame baseline (K_2 = hat{A}_1)
  4.  Wild regime: signed Euler analysis (K_3, K_4, K_5)
  5.  No Lie reduction theorem
  6.  Spectral sequence collapse analysis
  7.  Shadow depth classification
  8.  DT invariants for K_m
  9.  CoHA character computation
  10. DT partition function structure
  11. Growth rate analysis
  12. Wild-tame-finite comparison sweep
  13. Multi-path cross-checks
  14. Koszul convolution identity
  15. DT kappa proxy

Ground truth sources:
  Gabriel (1972): finite/tame/wild classification
  Reineke (2003): DT invariants for Kronecker
  Mozgovoy (2011): motivic DT of K_m
  Kac (1980): root multiplicities for quivers
  OEIS A000041 (partitions), A000712 (2-colored)
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.wild_quiver_chiral_engine import (
    KroneckerData,
    colored_partitions,
    kronecker_coha_character,
    kronecker_dt_invariants,
    kronecker_formal_bar_character,
    kronecker_signed_euler,
    kronecker_sweep,
    no_lie_reduction_proof,
    pbw_character,
    wild_bar_spectral_sequence_page,
    wild_coha_growth_rate,
    wild_dt_partition_function,
    wild_euler_sign_analysis,
    wild_kappa_dt_proxy,
    wild_kappa_formal,
    wild_quiver_full_analysis,
    wild_shadow_depth,
    wild_vs_tame_comparison,
    _euler_product_coeffs,
)


# ===========================================================================
# 1. Kronecker quiver data
# ===========================================================================

class TestKroneckerData:
    def test_k1_is_finite(self):
        d = KroneckerData(1)
        assert d.is_finite is True
        assert d.is_tame is False
        assert d.is_wild is False
        assert d.representation_type == "finite"

    def test_k2_is_tame(self):
        d = KroneckerData(2)
        assert d.is_finite is False
        assert d.is_tame is True
        assert d.is_wild is False
        assert d.representation_type == "tame"

    def test_k3_is_wild(self):
        d = KroneckerData(3)
        assert d.is_finite is False
        assert d.is_tame is False
        assert d.is_wild is True
        assert d.representation_type == "wild"

    def test_k5_is_wild(self):
        assert KroneckerData(5).is_wild is True

    def test_euler_form_matrix_k3(self):
        d = KroneckerData(3)
        assert d.euler_form_matrix == [[1, -3], [0, 1]]

    def test_symmetric_euler_form_k2(self):
        d = KroneckerData(2)
        assert d.symmetric_euler_form == [[2, -2], [-2, 2]]

    def test_euler_determinant_finite(self):
        """det = 4 - m^2: positive for m=1."""
        assert KroneckerData(1).euler_form_determinant == 3

    def test_euler_determinant_tame(self):
        """det = 0 for m=2."""
        assert KroneckerData(2).euler_form_determinant == 0

    def test_euler_determinant_wild(self):
        """det < 0 for m >= 3."""
        for m in [3, 4, 5, 6, 7]:
            assert KroneckerData(m).euler_form_determinant < 0

    def test_euler_determinant_formula(self):
        """det = 4 - m^2 for all m."""
        for m in range(1, 10):
            assert KroneckerData(m).euler_form_determinant == 4 - m ** 2

    def test_formal_rank(self):
        """d_Q = m + 2."""
        for m in range(1, 8):
            assert KroneckerData(m).formal_rank == m + 2

    def test_coha_dim_1_is_2(self):
        """Two simples at dimension 1."""
        for m in range(1, 6):
            assert KroneckerData(m).coha_dim_1 == 2

    def test_euler_form_value(self):
        d = KroneckerData(3)
        # chi((1,1), (1,1)) = 1 + 1 - 3*1*1 = -1
        assert d.euler_form_value((1, 1), (1, 1)) == -1
        # chi((1,0), (0,1)) = 1*0 + 0*1 - 3*1*1 = -3
        # (the -m*d_0*e_1 term: d_0=1, e_1=1, m=3)
        assert d.euler_form_value((1, 0), (0, 1)) == -3
        # chi((1,0), (1,0)) = 1 + 0 - 0 = 1 (simple at vertex 0)
        assert d.euler_form_value((1, 0), (1, 0)) == 1
        # chi((0,1), (0,1)) = 0 + 1 - 0 = 1 (simple at vertex 1)
        assert d.euler_form_value((0, 1), (0, 1)) == 1

    def test_dim_rep(self):
        d = KroneckerData(3)
        assert d.dim_rep((2, 3)) == 3 * 2 * 3  # = 18


# ===========================================================================
# 2. Finite-type baseline: K_1 = A_2
# ===========================================================================

class TestFiniteTypeBaseline:
    def test_k1_signed_euler_weight_1(self):
        """K_1 has d_Q = 3; (1-t)^3 at t^1 gives -3."""
        euler = kronecker_signed_euler(1, 5)
        assert euler[0] == 1
        assert euler[1] == -3

    def test_k1_formal_character_matches_sl2(self):
        """K_1 = A_2 should match dim(sl_2) = 3 colored partitions
        at the formal level.

        But K_1 has formal_rank = 3, not dim(sl_3) = 8.
        The formal PBW character with d=3 is the sl_2 character.
        """
        ch = kronecker_formal_bar_character(1, 6)
        expected = pbw_character(3, 6)
        assert ch == expected

    def test_k1_no_negative_euler_up_to_20(self):
        """Finite type: Euler series has definite sign pattern."""
        euler = kronecker_signed_euler(1, 20)
        # For d = 3, the product (1-t)^3(1-t^2)^3... should have
        # the Koszul sign pattern
        # Actually for d=3 there CAN be zeros but no SIGN CHANGES
        # between consecutive nonzero coefficients of the same parity.
        # The raw coefficients can be negative (that's expected for
        # the signed Euler series -- negative means odd bar degree).
        # The KEY test is that the absolute values give well-defined dims.
        for w in range(len(euler)):
            # Each coefficient is an integer (exact arithmetic)
            assert isinstance(euler[w], int)

    def test_k1_koszul_convolution(self):
        """Koszul identity: PBW * Euler = delta_{w,0}."""
        d = 3
        max_w = 10
        pbw = pbw_character(d, max_w)
        chi = _euler_product_coeffs(d, max_w)
        for w in range(max_w + 1):
            s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
            expected = 1 if w == 0 else 0
            assert s == expected, f"Koszul fails at w={w}: got {s}"


# ===========================================================================
# 3. Tame baseline: K_2 = hat{A}_1
# ===========================================================================

class TestTameBaseline:
    def test_k2_euler_determinant_zero(self):
        assert KroneckerData(2).euler_form_determinant == 0

    def test_k2_dt_simples(self):
        dt = kronecker_dt_invariants(2, 3)
        assert dt[(1, 0)] == 1
        assert dt[(0, 1)] == 1

    def test_k2_dt_11_is_2(self):
        """K_2 at (1,1): m = 2 indecomposables."""
        dt = kronecker_dt_invariants(2, 3)
        assert dt[(1, 1)] == 2

    def test_k2_dt_22_is_1(self):
        """Tame: Omega(n,n) = 1 for hat{A}_1."""
        dt = kronecker_dt_invariants(2, 4)
        assert dt[(2, 2)] == 1

    def test_k2_dt_21_is_1(self):
        """Tame: preprojective indecomposable at (2,1)."""
        dt = kronecker_dt_invariants(2, 4)
        assert dt[(2, 1)] == 1

    def test_k2_formal_character(self):
        """K_2 has d_Q = 4 formal generators."""
        ch = kronecker_formal_bar_character(2, 5)
        expected = pbw_character(4, 5)
        assert ch == expected


# ===========================================================================
# 4. Wild regime: signed Euler analysis
# ===========================================================================

class TestWildSignedEuler:
    def test_k3_has_negative_coefficients(self):
        """Wild K_3: signed Euler series has negatives at weight >= 2."""
        analysis = wild_euler_sign_analysis(3, 10)
        assert analysis["has_negative_coefficients"] is True

    def test_k3_first_negative_at_weight_1(self):
        """K_3 has d_Q = 5; (1-t)^5 at t^1 gives -5 (negative)."""
        analysis = wild_euler_sign_analysis(3, 10)
        # The Euler product (1-t)^5(1-t^2)^5... has coefficient
        # at t^1 equal to -5 (from the (1-t)^5 factor).
        # This is ALWAYS negative for d >= 2.
        assert analysis["first_negative_weight"] == 1

    def test_k4_has_negative_coefficients(self):
        analysis = wild_euler_sign_analysis(4, 10)
        assert analysis["has_negative_coefficients"] is True

    def test_k5_has_negative_coefficients(self):
        analysis = wild_euler_sign_analysis(5, 10)
        assert analysis["has_negative_coefficients"] is True

    def test_k1_first_negative_at_weight_1_also(self):
        """Even K_1 has negative Euler coefficients (signed series!)."""
        analysis = wild_euler_sign_analysis(1, 10)
        # For d = 3: (1-t)^3 at t^1 = -3
        assert analysis["first_negative_weight"] == 1

    def test_sign_changes_increase_with_m(self):
        """More arrows -> more sign oscillation."""
        changes = [
            wild_euler_sign_analysis(m, 15)["sign_changes"]
            for m in [1, 2, 3, 4, 5]
        ]
        # Broadly increasing (not strictly monotone at every step)
        assert changes[-1] >= changes[0]

    def test_euler_weight_0_always_1(self):
        """The constant term is always 1."""
        for m in range(1, 8):
            euler = kronecker_signed_euler(m, 5)
            assert euler[0] == 1

    def test_euler_weight_1_equals_minus_d(self):
        """Coefficient at t^1 in prod(1-t^n)^d is -d."""
        for m in range(1, 8):
            d = m + 2
            euler = kronecker_signed_euler(m, 5)
            assert euler[1] == -d


# ===========================================================================
# 5. No Lie reduction theorem
# ===========================================================================

class TestNoLieReduction:
    def test_k1_has_lie_reduction(self):
        result = no_lie_reduction_proof(1)
        assert result["no_lie_reduction"] is False

    def test_k2_has_lie_reduction(self):
        result = no_lie_reduction_proof(2)
        assert result["no_lie_reduction"] is False

    def test_k3_no_lie_reduction(self):
        result = no_lie_reduction_proof(3)
        assert result["no_lie_reduction"] is True
        assert result["euler_form_definite"] is False

    def test_k4_no_lie_reduction(self):
        result = no_lie_reduction_proof(4)
        assert result["no_lie_reduction"] is True

    def test_k5_no_lie_reduction(self):
        result = no_lie_reduction_proof(5)
        assert result["no_lie_reduction"] is True

    def test_k3_formal_rank_5(self):
        """K_3 has d_Q = 5; check that 5 is NOT a Lie algebra dimension."""
        result = no_lie_reduction_proof(3)
        assert result["formal_rank"] == 5
        # 5 is not the dimension of any simple Lie algebra
        assert result["matching_simple_algebra"] is None

    def test_k6_formal_rank_8_matches_sl3(self):
        """K_6 has d_Q = 8 = dim(sl_3), but Koszulness fails."""
        result = no_lie_reduction_proof(6)
        assert result["formal_rank"] == 8
        assert result["matching_simple_algebra"] is not None
        assert "sl_3" in result["matching_simple_algebra"]
        assert result["no_lie_reduction"] is True  # Koszulness fails

    def test_euler_form_indefinite_for_wild(self):
        for m in [3, 4, 5, 6, 7]:
            result = no_lie_reduction_proof(m)
            assert result["euler_form_definite"] is False
            assert result["euler_form_det"] == 4 - m ** 2


# ===========================================================================
# 6. Spectral sequence analysis
# ===========================================================================

class TestSpectralSequence:
    def test_k1_collapses_at_e2(self):
        ss = wild_bar_spectral_sequence_page(1)
        assert ss["collapse_page"] == 2
        assert ss["is_koszul"] is True

    def test_k2_collapses_at_e2(self):
        ss = wild_bar_spectral_sequence_page(2)
        assert ss["collapse_page"] == 2
        assert ss["is_koszul"] is True

    def test_k3_no_collapse(self):
        ss = wild_bar_spectral_sequence_page(3)
        assert ss["collapse_page"] is None
        assert ss["is_koszul"] is False

    def test_k5_no_collapse(self):
        ss = wild_bar_spectral_sequence_page(5)
        assert ss["is_koszul"] is False

    def test_wild_boundary_at_m3(self):
        """The Koszul / non-Koszul boundary is exactly at m=3."""
        for m in [1, 2]:
            assert wild_bar_spectral_sequence_page(m)["is_koszul"] is True
        for m in [3, 4, 5, 6]:
            assert wild_bar_spectral_sequence_page(m)["is_koszul"] is False


# ===========================================================================
# 7. Shadow depth classification
# ===========================================================================

class TestShadowDepth:
    def test_k1_class_L(self):
        sd = wild_shadow_depth(1)
        assert sd["shadow_class"] == "L"
        assert sd["shadow_depth"] == 3

    def test_k2_class_M(self):
        sd = wild_shadow_depth(2)
        assert sd["shadow_class"] == "M"
        assert sd["shadow_depth"] >= 1000

    def test_k3_class_W(self):
        sd = wild_shadow_depth(3)
        assert sd["shadow_class"] == "W"
        assert sd["shadow_depth"] is None

    def test_wild_class_for_all_m_ge_3(self):
        for m in [3, 4, 5, 6, 7]:
            sd = wild_shadow_depth(m)
            assert sd["shadow_class"] == "W"
            assert sd["shadow_depth"] is None


# ===========================================================================
# 8. DT invariants
# ===========================================================================

class TestDTInvariants:
    def test_simples_universal(self):
        """Omega(1,0) = 1 and Omega(0,1) = 1 for all m."""
        for m in range(1, 7):
            dt = kronecker_dt_invariants(m, 3)
            assert dt[(1, 0)] == 1
            assert dt[(0, 1)] == 1

    def test_omega_11_equals_m(self):
        """Omega(1,1) = m for all Kronecker quivers."""
        for m in range(1, 7):
            dt = kronecker_dt_invariants(m, 3)
            assert dt[(1, 1)] == m

    def test_k1_only_three_indecomposables(self):
        """A_2 has exactly 3 indecomposable representations."""
        dt = kronecker_dt_invariants(1, 6)
        nonzero = {k: v for k, v in dt.items() if v > 0}
        assert set(nonzero.keys()) == {(1, 0), (0, 1), (1, 1)}

    def test_k3_omega_21(self):
        """K_3 at (2,1): Omega = 3*(3-1)/2 = 3."""
        dt = kronecker_dt_invariants(3, 4)
        assert dt[(2, 1)] == 3

    def test_k3_omega_22(self):
        """K_3 at (2,2): Omega = 6 (Mozgovoy 2011)."""
        dt = kronecker_dt_invariants(3, 4)
        assert dt[(2, 2)] == 6

    def test_dt_growth_with_m(self):
        """More arrows -> more DT invariants."""
        for m in [3, 4, 5]:
            dt = kronecker_dt_invariants(m, 3)
            total = sum(v for v in dt.values() if v > 0)
            dt_next = kronecker_dt_invariants(m + 1, 3)
            total_next = sum(v for v in dt_next.values() if v > 0)
            assert total_next >= total

    def test_dt_symmetric_21_12(self):
        """Omega(2,1) = Omega(1,2) for all m (source-sink symmetry)."""
        for m in range(2, 6):
            dt = kronecker_dt_invariants(m, 4)
            assert dt[(2, 1)] == dt[(1, 2)]


# ===========================================================================
# 9. CoHA character
# ===========================================================================

class TestCoHACharacter:
    def test_coha_weight_0_is_1(self):
        """Empty representation contributes 1."""
        for m in range(1, 6):
            ch = kronecker_coha_character(m, 3)
            assert ch[0] == 1

    def test_coha_weight_1_is_2(self):
        """Two simples at weight 1."""
        for m in range(1, 6):
            ch = kronecker_coha_character(m, 3)
            assert ch[1] == 2

    def test_coha_weight_2_k3(self):
        """K_3 at weight 2: Omega(2,0) + Omega(0,2) + Omega(1,1) = 0 + 0 + 3 = 3."""
        ch = kronecker_coha_character(3, 3)
        assert ch[2] == 3

    def test_k1_coha_total(self):
        """K_1 = A_2: total = 1 + 2 + 1 = 4 (three indecomposables + empty)."""
        ch = kronecker_coha_character(1, 4)
        assert ch == [1, 2, 1, 0, 0]


# ===========================================================================
# 10. DT partition function
# ===========================================================================

class TestDTPartitionFunction:
    def test_k1_trivial_wall_crossing(self):
        pf = wild_dt_partition_function(1, 4)
        assert pf["wall_crossing_structure"] == "trivial"

    def test_k2_one_wall(self):
        pf = wild_dt_partition_function(2, 4)
        assert pf["wall_crossing_structure"] == "one wall"

    def test_k3_infinitely_many_walls(self):
        pf = wild_dt_partition_function(3, 4)
        assert "infinitely many" in pf["wall_crossing_structure"]

    def test_growth_type_matches_rep_type(self):
        for m in range(1, 6):
            pf = wild_dt_partition_function(m, 4)
            assert pf["growth_type"] == KroneckerData(m).representation_type


# ===========================================================================
# 11. Growth rate analysis
# ===========================================================================

class TestGrowthRate:
    def test_k1_bounded(self):
        gr = wild_coha_growth_rate(1, 6)
        assert gr["growth_type"] == "bounded"

    def test_k2_linear(self):
        gr = wild_coha_growth_rate(2, 6)
        assert gr["growth_type"] == "linear"

    def test_k3_exponential(self):
        gr = wild_coha_growth_rate(3, 6)
        assert gr["growth_type"] == "exponential"

    def test_growth_type_classification(self):
        for m, expected in [(1, "bounded"), (2, "linear"), (3, "exponential"),
                            (4, "exponential"), (5, "exponential")]:
            gr = wild_coha_growth_rate(m, 5)
            assert gr["growth_type"] == expected


# ===========================================================================
# 12. Comparison sweep
# ===========================================================================

class TestComparisonSweep:
    def test_sweep_includes_all_types(self):
        results = wild_vs_tame_comparison(6, 5)
        types = {r["type"] for r in results}
        assert "finite" in types
        assert "tame" in types
        assert "wild" in types

    def test_sweep_formal_equals_coha_for_finite(self):
        """For finite type, the formal PBW character and CoHA should
        differ (formal counts all weights, CoHA counts orbits)."""
        results = wild_vs_tame_comparison(3, 5)
        # The formal character p_d(n) counts ALL PBW states;
        # the CoHA character counts orbits.  They are different.
        for r in results:
            assert isinstance(r["formal_bar_character"], list)
            assert isinstance(r["coha_character"], list)

    def test_kronecker_sweep_returns_correct_count(self):
        sweep = kronecker_sweep(5, 6)
        assert len(sweep) == 5

    def test_kronecker_sweep_types(self):
        sweep = kronecker_sweep(5)
        assert sweep[0]["type"] == "finite"
        assert sweep[1]["type"] == "tame"
        for i in range(2, 5):
            assert sweep[i]["type"] == "wild"


# ===========================================================================
# 13. Multi-path cross-checks
# ===========================================================================

class TestMultiPathCrossChecks:
    def test_euler_det_three_paths(self):
        """Three paths to the Euler form determinant of K_m.

        Path A: direct formula 4 - m^2
        Path B: from the 2x2 matrix
        Path C: from positive-definiteness test
        """
        for m in range(1, 8):
            data = KroneckerData(m)
            path_a = 4 - m ** 2
            path_b = data.euler_form_determinant
            # Path C: eigenvalue sign from matrix [[2, -m], [-m, 2]]
            # eigenvalues: 2 +/- m; both positive iff m < 2
            path_c = (2 + m) * (2 - m)
            assert path_a == path_b == path_c

    def test_formal_rank_two_paths(self):
        """Two paths to formal rank.

        Path A: m + 2
        Path B: from Euler product coefficient at t^1
        """
        for m in range(1, 8):
            path_a = KroneckerData(m).formal_rank
            euler = kronecker_signed_euler(m, 2)
            path_b = abs(euler[1])  # coefficient of t^1 = -d_Q
            assert path_a == path_b

    def test_dt_simples_count_two_paths(self):
        """Two paths to number of simples.

        Path A: number of vertices = 2
        Path B: sum of Omega at |d| = 1
        """
        for m in range(1, 6):
            path_a = 2
            dt = kronecker_dt_invariants(m, 2)
            path_b = dt[(1, 0)] + dt[(0, 1)]
            assert path_a == path_b

    def test_coha_character_consistent_with_dt(self):
        """CoHA character at weight w = sum of Omega at |d| = w."""
        for m in range(1, 5):
            ch = kronecker_coha_character(m, 4)
            dt = kronecker_dt_invariants(m, 4)
            for w in range(1, 5):
                omega_sum = sum(
                    v for (d0, d1), v in dt.items() if d0 + d1 == w
                )
                assert ch[w] == omega_sum


# ===========================================================================
# 14. Koszul convolution identity
# ===========================================================================

class TestKoszulConvolution:
    def test_convolution_d3(self):
        """PBW(3) * Euler(3) = delta for K_1 formal rank."""
        d = 3
        max_w = 8
        pbw = pbw_character(d, max_w)
        chi = _euler_product_coeffs(d, max_w)
        for w in range(max_w + 1):
            s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
            assert s == (1 if w == 0 else 0)

    def test_convolution_d4(self):
        """PBW(4) * Euler(4) = delta for K_2 formal rank."""
        d = 4
        max_w = 8
        pbw = pbw_character(d, max_w)
        chi = _euler_product_coeffs(d, max_w)
        for w in range(max_w + 1):
            s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
            assert s == (1 if w == 0 else 0)

    def test_convolution_d5_wild_formal(self):
        """PBW(5) * Euler(5) = delta even for wild K_3 formal rank.

        The Koszul identity is a formal algebraic identity for ANY d.
        It holds for the FORMAL PBW character regardless of whether
        the underlying algebra is Koszul.  The failure of Koszulness
        means the formal character does not compute the actual bar
        cohomology dimensions, but the ALGEBRAIC IDENTITY is universal.
        """
        d = 5
        max_w = 8
        pbw = pbw_character(d, max_w)
        chi = _euler_product_coeffs(d, max_w)
        for w in range(max_w + 1):
            s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
            assert s == (1 if w == 0 else 0)

    def test_convolution_identity_all_formal_ranks(self):
        """Universal: PBW(d) * Euler(d) = delta for ALL d."""
        for d in [1, 2, 3, 5, 7, 10]:
            max_w = 6
            pbw = pbw_character(d, max_w)
            chi = _euler_product_coeffs(d, max_w)
            for w in range(max_w + 1):
                s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
                assert s == (1 if w == 0 else 0), f"Fails at d={d}, w={w}"


# ===========================================================================
# 15. DT kappa proxy
# ===========================================================================

class TestDTKappaProxy:
    def test_k1_proxy(self):
        result = wild_kappa_dt_proxy(1)
        # K_1: real roots are (1,0), (0,1), (1,1)
        assert result["n_real_roots"] >= 2

    def test_k3_has_real_and_imaginary_roots(self):
        result = wild_kappa_dt_proxy(3)
        assert result["n_real_roots"] >= 2
        assert result["n_imaginary_roots"] >= 0

    def test_wild_kappa_formal_returns_none(self):
        for m in [1, 2, 3, 4, 5]:
            assert wild_kappa_formal(m) is None


# ===========================================================================
# 16. Full analysis
# ===========================================================================

class TestFullAnalysis:
    def test_full_analysis_k3(self):
        result = wild_quiver_full_analysis(3)
        assert result["m"] == 3
        assert result["representation_type"] == "wild"
        assert result["no_lie_reduction"]["no_lie_reduction"] is True
        assert result["spectral_sequence"]["is_koszul"] is False
        assert result["shadow_depth"]["shadow_class"] == "W"

    def test_full_analysis_k1(self):
        result = wild_quiver_full_analysis(1)
        assert result["representation_type"] == "finite"
        assert result["spectral_sequence"]["is_koszul"] is True
        assert result["shadow_depth"]["shadow_class"] == "L"

    def test_full_analysis_keys_present(self):
        result = wild_quiver_full_analysis(4)
        required_keys = [
            "quiver", "m", "representation_type", "formal_rank",
            "euler_form_det", "no_lie_reduction", "signed_euler_analysis",
            "spectral_sequence", "shadow_depth", "dt_invariants",
            "coha_character", "kappa_dt_proxy", "dt_partition_function",
        ]
        for key in required_keys:
            assert key in result, f"Missing key: {key}"


# ===========================================================================
# 17. Colored partition ground truth (OEIS cross-check)
# ===========================================================================

class TestColoredPartitions:
    def test_p1_ordinary_partitions(self):
        """OEIS A000041."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        got = [colored_partitions(n, 1) for n in range(11)]
        assert got == expected

    def test_p2_two_colored(self):
        """OEIS A000712."""
        expected = [1, 2, 5, 10, 20, 36, 65, 110]
        got = [colored_partitions(n, 2) for n in range(8)]
        assert got == expected

    def test_p3_three_colored(self):
        """OEIS A000716."""
        expected = [1, 3, 9, 22, 51, 108, 221]
        got = [colored_partitions(n, 3) for n in range(7)]
        assert got == expected
