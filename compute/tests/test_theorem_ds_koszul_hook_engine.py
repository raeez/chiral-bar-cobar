r"""Tests for the DS-KD commutation theorem for hook-type nilpotents.

56 tests verifying DS(A^!) = DS(A)^! for hook-type nilpotents via
four independent methods:
  I.   PBW filtration and BRST spectral sequence (11 tests)
  II.  Fehily-CLNS commutative diagram (12 tests)
  III. Transport propagation from principal (8 tests)
  IV.  Shadow tower structural comparison (8 tests)
  V.   Cross-method consistency (7 tests)
  VI.  Numerical cross-checks (6 tests)
  VII. Catalog and edge cases (4 tests)

CRITICAL DISTINCTIONS tested here:
  - Affine KD: kappa(V_k) + kappa(V_{k'}) = 0 (ALWAYS holds)
  - c-complementarity: c(W_k(f_lam)) + c(W_{k'}(f_{lam^t})) = const (the DS-KD test)
  - Kappa sum at the W-algebra level: k-independent for SELF-TRANSPOSE ONLY;
    k-DEPENDENT for non-self-transpose pairs (because rho differs).
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, simplify

from compute.lib.theorem_ds_koszul_hook_engine import (
    DSKDCommutationResult,
    FehilyCLNSDualityData,
    PBWFiltrationData,
    ShadowTowerComparisonData,
    TransportPropagationData,
    anomaly_ratio_duality,
    brst_spectral_sequence_page,
    ds_kd_compatibility_constant,
    fehily_clns_duality,
    generator_matching_under_kd,
    hook_ds_kd_catalog,
    numerical_affine_kappa_check,
    numerical_c_complementarity,
    numerical_self_transpose_kappa,
    pbw_filtration_analysis,
    self_dual_hook_analysis,
    shadow_tower_comparison,
    transport_propagation_analysis,
    verify_ds_kd_hook,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    krw_central_charge,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    hook_partition,
    transpose_partition,
)


k = Symbol('k')


# ===================================================================
# I. Method 1: PBW filtration and BRST spectral sequence
# ===================================================================

class TestPBWFiltration:

    def test_sl3_21_koszul(self):
        """sl_3, f=(2,1): Bershadsky-Polyakov is Koszul."""
        data = pbw_filtration_analysis((2, 1))
        assert data.N == 3
        assert data.w_is_koszul is True

    def test_sl4_31_koszul(self):
        """sl_4, f=(3,1): subregular hook is Koszul."""
        data = pbw_filtration_analysis((3, 1))
        assert data.N == 4
        assert data.e2_collapse is True
        assert data.w_is_koszul is True

    def test_sl4_211_koszul(self):
        """sl_4, f=(2,1,1): minimal hook is Koszul."""
        data = pbw_filtration_analysis((2, 1, 1))
        assert data.w_is_koszul is True

    def test_sl5_41_koszul(self):
        data = pbw_filtration_analysis((4, 1))
        assert data.w_is_koszul is True

    def test_sl5_2111_koszul(self):
        data = pbw_filtration_analysis((2, 1, 1, 1))
        assert data.w_is_koszul is True

    def test_sl6_51_koszul(self):
        data = pbw_filtration_analysis((5, 1))
        assert data.w_is_koszul is True

    def test_n_plus_dim_sl3_21(self):
        """n_+ for sl_3, (2,1): grade 1 (dim 1) + grade 1/2 (dim 2) = 3."""
        data = pbw_filtration_analysis((2, 1))
        assert data.n_plus_dim == 3

    def test_g_half_dim_sl3_21(self):
        """g_{1/2} for sl_3, (2,1) has dimension 2."""
        data = pbw_filtration_analysis((2, 1))
        assert data.g_half_dim == 2

    def test_brst_ss_page_principal(self):
        """Principal nilpotent: SS collapses at E_2."""
        result = brst_spectral_sequence_page((3,))
        assert result["collapse_page"] == 2
        assert result["g_0_reductive"] is True

    def test_brst_ss_page_hook(self):
        """Hook nilpotent: SS collapses at E_1 or E_2."""
        result = brst_spectral_sequence_page((2, 1))
        assert result["collapse_page"] <= 2

    def test_both_sides_koszul_sl4(self):
        """Both W_k(3,1) and W_{k'}(2,1,1) are Koszul."""
        assert pbw_filtration_analysis((3, 1)).w_is_koszul is True
        assert pbw_filtration_analysis((2, 1, 1)).w_is_koszul is True


# ===================================================================
# II. Method 2: Fehily-CLNS commutative diagram
# ===================================================================

class TestFehilyCLNS:

    def test_affine_kd_sl3(self):
        """Affine KD: kappa(V_k(sl_3)) + kappa(V_{k'}(sl_3)) = 0."""
        data = fehily_clns_duality((2, 1))
        assert data.affine_kd_holds is True

    def test_affine_kd_sl4(self):
        """Affine KD: kappa(V_k(sl_4)) + kappa(V_{k'}(sl_4)) = 0."""
        data = fehily_clns_duality((3, 1))
        assert data.affine_kd_holds is True

    def test_c_sum_constant_self_transpose(self):
        """c-sum is k-independent for SELF-TRANSPOSE (2,1) in sl_3."""
        data = fehily_clns_duality((2, 1))
        assert data.c_sum_k_independent is True

    def test_c_sum_k_dependent_non_self_transpose(self):
        """c-sum is k-DEPENDENT for non-self-transpose (3,1) <-> (2,1,1).

        This is correct: the KRW quadratic coefficients
        B_{(3,1)} = 54 and B_{(2,1,1)} = 36 differ, so under the
        standard FF involution k' = -k-2N, the c-sum is not constant.
        The DS-KD commutation is proved at the OPE structure level
        (Fehily-CLNS), not via c-complementarity.
        """
        data = fehily_clns_duality((3, 1))
        assert data.c_sum_k_independent is False

    def test_c_sum_k_dependent_sl4_211(self):
        """Same test from the (2,1,1) side."""
        data = fehily_clns_duality((2, 1, 1))
        assert data.c_sum_k_independent is False

    def test_c_sum_k_dependent_sl5_41(self):
        """Non-self-transpose hooks in sl_5 also have k-dependent c-sum."""
        data = fehily_clns_duality((4, 1))
        assert data.c_sum_k_independent is False

    def test_c_sum_self_transpose_sl5_321(self):
        """Self-transpose hook (3,1,1) in sl_5: (3,1,1)^t = (3,1,1)."""
        lam = (3, 1, 1)
        lam_t = transpose_partition(lam)
        data = fehily_clns_duality(lam)
        if lam == lam_t:
            assert data.c_sum_k_independent is True
        else:
            # Not self-transpose; c-sum may be k-dependent
            pass

    def test_diagram_commutes_sl3(self):
        """Full diagram for sl_3 (2,1)."""
        data = fehily_clns_duality((2, 1))
        assert data.diagram_commutes is True

    def test_diagram_commutes_sl4_31(self):
        """Full diagram for sl_4 (3,1)."""
        data = fehily_clns_duality((3, 1))
        assert data.diagram_commutes is True

    def test_rho_match_self_transpose(self):
        """Self-transpose (2,1) in sl_3: anomaly ratios match."""
        data = fehily_clns_duality((2, 1))
        assert data.rho_match is True
        assert data.source_rho == Rational(1, 6)

    def test_rho_differ_non_self_transpose(self):
        """Non-self-transpose (3,1) in sl_4: anomaly ratios DIFFER."""
        data = fehily_clns_duality((3, 1))
        assert data.rho_match is False
        assert data.source_rho != data.dual_rho

    def test_c_sum_value_sl3_21(self):
        """c-sum for self-transpose (2,1) in sl_3 = 196 (= K_BP).

        # VERIFIED: [DC] c_BP(k)+c_BP(-k-6) = 196 from per-root-pair KRW
        """
        data = fehily_clns_duality((2, 1))
        assert data.c_sum_k_independent is True
        assert simplify(data.c_sum_value - 196) == 0


# ===================================================================
# III. Method 3: Transport propagation from principal
# ===================================================================

class TestTransportPropagation:

    def test_principal_proved_sl3(self):
        """DS-KD for principal of sl_3 is proved."""
        data = transport_propagation_analysis((2, 1))
        assert data.principal_ds_kd_proved is True

    def test_principal_proved_sl4(self):
        data = transport_propagation_analysis((3, 1))
        assert data.principal_ds_kd_proved is True

    def test_hasse_distance_sl3(self):
        """(2,1) is distance 1 from principal (3) in sl_3."""
        data = transport_propagation_analysis((2, 1))
        assert data.hasse_distance == 1

    def test_hasse_distance_sl4_31(self):
        """(3,1) is distance 1 from principal (4)."""
        data = transport_propagation_analysis((3, 1))
        assert data.hasse_distance == 1

    def test_hasse_distance_sl4_211(self):
        """(2,1,1) is distance 2 from principal (4)."""
        data = transport_propagation_analysis((2, 1, 1))
        assert data.hasse_distance == 2

    def test_propagation_sl3(self):
        data = transport_propagation_analysis((2, 1))
        assert data.propagation_holds is True

    def test_propagation_sl4_31(self):
        data = transport_propagation_analysis((3, 1))
        assert data.propagation_holds is True

    def test_propagation_sl5_41(self):
        data = transport_propagation_analysis((4, 1))
        assert data.propagation_holds is True


# ===================================================================
# IV. Method 4: Shadow tower structural comparison
# ===================================================================

class TestShadowTower:

    def test_self_transpose_kappa_sum_sl3(self):
        """Self-transpose (2,1): kappa sum is k-independent."""
        data = shadow_tower_comparison((2, 1))
        assert data.is_self_transpose is True
        assert data.kappa_sum_k_independent is True

    def test_non_self_transpose_kappa_sum_sl4(self):
        """Non-self-transpose (3,1): kappa sum is k-DEPENDENT (different rho)."""
        data = shadow_tower_comparison((3, 1))
        assert data.is_self_transpose is False
        assert data.kappa_sum_k_independent is False

    def test_structural_compatible_sl3(self):
        data = shadow_tower_comparison((2, 1))
        assert data.structurally_compatible is True

    def test_structural_compatible_sl4_31(self):
        data = shadow_tower_comparison((3, 1))
        assert data.structurally_compatible is True

    def test_structural_compatible_sl4_211(self):
        data = shadow_tower_comparison((2, 1, 1))
        assert data.structurally_compatible is True

    def test_structural_compatible_sl5(self):
        for lam in [(4, 1), (3, 1, 1), (2, 1, 1, 1)]:
            data = shadow_tower_comparison(lam)
            assert data.structurally_compatible is True, f"Failed for {lam}"

    def test_anomaly_ratios_recorded(self):
        data = shadow_tower_comparison((3, 1))
        assert data.source_rho == Rational(17, 6)
        assert data.dual_rho == Rational(11, 6)

    def test_depth_classes(self):
        """Shadow depth classes are computed for both sides."""
        data = shadow_tower_comparison((2, 1))
        assert data.source_shadow_class in ("G", "L", "C", "M")
        assert data.dual_shadow_class in ("G", "L", "C", "M")


# ===================================================================
# V. Cross-method consistency
# ===================================================================

class TestCrossMethod:

    def test_all_methods_sl3_21(self):
        result = verify_ds_kd_hook((2, 1))
        assert result.all_methods_agree is True
        assert result.ds_kd_commutes is True

    def test_all_methods_sl4_31(self):
        result = verify_ds_kd_hook((3, 1))
        assert result.all_methods_agree is True
        assert result.ds_kd_commutes is True

    def test_all_methods_sl4_211(self):
        result = verify_ds_kd_hook((2, 1, 1))
        assert result.all_methods_agree is True
        assert result.ds_kd_commutes is True

    def test_is_hook(self):
        for lam in [(2, 1), (3, 1), (2, 1, 1), (4, 1)]:
            assert verify_ds_kd_hook(lam).is_hook is True

    def test_generator_matching_self_transpose(self):
        """Self-transpose (2,1): generator content matches."""
        data = generator_matching_under_kd((2, 1))
        assert data["is_self_transpose"] is True
        assert data["source_n_generators"] == data["dual_n_generators"]
        assert data["weights_match"] is True

    def test_generator_matching_non_self_transpose(self):
        """Non-self-transpose (3,1) <-> (2,1,1): different generator content."""
        data = generator_matching_under_kd((3, 1))
        assert data["is_self_transpose"] is False
        assert data["source_n_generators"] == 5
        assert data["dual_n_generators"] == 9

    def test_sl5_311_full(self):
        result = verify_ds_kd_hook((3, 1, 1))
        assert result.pbw_source_koszul is True
        assert result.pbw_dual_koszul is True
        assert result.clns_diagram_commutes is True
        assert result.transport_propagation_holds is True


# ===================================================================
# VI. Numerical cross-checks
# ===================================================================

class TestNumerical:

    def test_affine_kappa_zero_sl3(self):
        """Affine kappa sum = 0 for sl_3 at multiple k values."""
        results = numerical_affine_kappa_check(3)
        for r in results:
            assert r["is_zero"] is True, f"Affine kappa sum nonzero at k={r['k']}"

    def test_affine_kappa_zero_sl4(self):
        """Affine kappa sum = 0 for sl_4 at multiple k values."""
        results = numerical_affine_kappa_check(4)
        for r in results:
            assert r["is_zero"] is True

    def test_c_complementarity_self_transpose_sl3(self):
        """c-sum is constant for self-transpose (2,1) numerically."""
        results = numerical_c_complementarity((2, 1))
        if len(results) >= 2:
            first = results[0]["c_sum"]
            for r in results[1:]:
                assert r["c_sum"] == first, f"c-sum varies at k={r['k']}"

    def test_c_complementarity_non_self_transpose_varies(self):
        """c-sum varies with k for non-self-transpose (3,1) <-> (2,1,1)."""
        results = numerical_c_complementarity((3, 1))
        if len(results) >= 2:
            sums = set(r["c_sum"] for r in results)
            assert len(sums) > 1, "c-sum should be k-dependent for (3,1)"

    def test_c_complementarity_self_transpose_sl5(self):
        """c-sum is constant for self-transpose (3,1,1) in sl_5."""
        results = numerical_c_complementarity((3, 1, 1))
        if len(results) >= 2:
            first = results[0]["c_sum"]
            for r in results[1:]:
                assert r["c_sum"] == first, f"c-sum varies at k={r['k']}"

    def test_self_transpose_kappa_constant_sl3(self):
        """Self-transpose (2,1): kappa sum is constant numerically."""
        results = numerical_self_transpose_kappa((2, 1))
        if len(results) >= 2:
            first = results[0]["kappa_sum"]
            for r in results[1:]:
                assert r["kappa_sum"] == first, (
                    f"Kappa sum varies: {first} vs {r['kappa_sum']} at k={r['k']}"
                )


# ===================================================================
# VII. Catalog and edge cases
# ===================================================================

class TestCatalog:

    def test_catalog_sl3_to_sl5(self):
        """All hooks for N=3..5 pass all 4 methods."""
        catalog = hook_ds_kd_catalog(max_N=5)
        assert len(catalog) > 0
        for entry in catalog:
            assert entry["is_hook"] is True
            assert entry["pbw_source_koszul"] is True, f"N={entry['N']}, {entry['partition']}"
            assert entry["pbw_dual_koszul"] is True, f"N={entry['N']}, {entry['partition']}"
            assert entry["clns_holds"] is True, f"N={entry['N']}, {entry['partition']}"
            assert entry["transport_holds"] is True, f"N={entry['N']}, {entry['partition']}"
            assert entry["ds_kd_commutes"] is True, f"N={entry['N']}, {entry['partition']}"

    def test_catalog_count(self):
        """Catalog has correct number of hook partitions (excluding principal).

        For each N, hooks (N-r, 1^r) for r=1..N-1, giving N-1 per N.
        N=3: 2, N=4: 3, N=5: 4 => total 9.
        """
        catalog = hook_ds_kd_catalog(max_N=5)
        assert len(catalog) == 9

    def test_self_dual_hooks_odd_N_only(self):
        """Self-dual hooks exist only for odd N."""
        for N in range(3, 8):
            sd = self_dual_hook_analysis(N)
            if N % 2 == 1:
                assert len(sd) > 0, f"No self-dual hook for odd N={N}"
            else:
                assert len(sd) == 0, f"Self-dual hook for even N={N}"

    def test_anomaly_ratio_duality_sl4(self):
        """Anomaly ratio duality: rho(3,1) from (3,1) = rho_dual from (2,1,1)."""
        data_31 = anomaly_ratio_duality((3, 1))
        data_211 = anomaly_ratio_duality((2, 1, 1))
        assert data_31["rho_source"] == data_211["rho_dual"]
        assert data_31["rho_dual"] == data_211["rho_source"]
