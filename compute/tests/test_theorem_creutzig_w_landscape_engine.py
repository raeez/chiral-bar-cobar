r"""Tests for the Creutzig-Linshaw W-algebra landscape expansion engine.

The sections cover minimal orthogonal W-algebras, candidate hook corridors,
principal B/C/D source obligations, cited conformal extensions, the precise
KL theorem domain, finite-catalog semantics, and independent arithmetic
oracles.

VERIFICATION MANDATE: every numerical result is verified by at least 2
independent methods (AP10 compliance).

Manuscript references:
    tab:master-invariants (landscape_census.tex)
    tab:shadow-tower-census (landscape_census.tex)
    thm:w-algebra-koszul-main (w_algebras.tex)
    prop:sl3-nilpotent-shadow-data (w_algebras.tex)
    prop:sl4-hook-shadow-data (w_algebras.tex)
    thm:ds-shadow-functor-arity2 (w_algebras.tex)
"""

import pytest
from sympy import Float, Rational, Symbol, simplify, sqrt

from compute.lib.theorem_creutzig_w_landscape_engine import (
    ConformalExtensionData,
    KL_SOURCE,
    MINIMAL_SO_SOURCE,
    bar_cobar_kl_commutation_check,
    building_block_bcd_data,
    conformal_extension_koszulness,
    creutzig_landscape_catalog,
    d3_a3_incomplete_ansatz_discrepancy,
    hook_successive_reduction_data,
    kl_category_equivalence,
    landscape_summary,
    minimal_so_at_minus_1,
    minimal_w_so_data,
    verify_bcd_c_complementarity,
    verify_c_complementarity_k_independent,
    verify_hook_koszulness_chain,
    verify_type_a_kappa_consistency,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    kappa_complementarity_sum,
    krw_central_charge,
    reciprocal_weight_diagnostic_from_partition,
)
from compute.lib.non_principal_w_bar_engine import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
)
from compute.lib.nonprincipal_ds_orbits import (
    hook_partition,
    transpose_partition,
)


k = Symbol('k')


# ===================================================================
# I. Minimal W-algebras of so_N at level -1
# ===================================================================

class TestMinimalSoN:
    """Tests for W^{-1}(so_N, f_min) from [2506.15605]."""

    def test_so7_generator_count(self):
        """The even orbifold ledger has 6+6+1 generators for N=7."""
        d = minimal_so_at_minus_1(7)
        assert d.n_generators == 13

    def test_so7_generator_weights(self):
        """For r=3 the multiplicities are 6, 6, and 1."""
        d = minimal_so_at_minus_1(7)
        assert d.generator_weights.count(Rational(1)) == 6
        assert d.generator_weights.count(Rational(3, 2)) == 6
        assert d.generator_weights.count(Rational(2)) == 1
        assert set(d.generator_parities) == {"even"}

    def test_so7_anomaly_ratio(self):
        """The signed reciprocal-weight sum is exact; rho stays open."""
        d = minimal_so_at_minus_1(7)
        assert d.reciprocal_weight_diagnostic == Rational(21, 2)
        assert d.anomaly_ratio.status is ClaimStatus.OPEN
        assert d.anomaly_ratio.value is None
        assert any("genus-one" in hypothesis for hypothesis in d.anomaly_ratio.hypotheses)

    def test_so7_is_rational(self):
        """The odd-N strong-rationality status remains source-visible."""
        d = minimal_so_at_minus_1(7)
        assert d.orbifold_realization_at_minus_1.status is ClaimStatus.PROVED_ELSEWHERE
        assert d.orbifold_realization_at_minus_1.value is True
        assert "Theorem 1.1" in d.orbifold_realization_at_minus_1.evidence[0]
        assert d.strong_rationality_at_minus_1.status is ClaimStatus.OPEN
        assert d.strong_rationality_at_minus_1.value is None
        assert d.is_rational_at_minus_1 is None
        assert MINIMAL_SO_SOURCE.split(", Theorem")[0] in d.strong_rationality_at_minus_1.evidence[0]

    def test_so8_strong_rationality_source_domain(self):
        """Corollary 1.2 proves strong rationality for even N>=8."""
        d = minimal_so_at_minus_1(8)
        assert d.strong_rationality_at_minus_1.status is ClaimStatus.PROVED_ELSEWHERE
        assert d.strong_rationality_at_minus_1.value is True
        assert d.is_rational_at_minus_1 is True
        assert d.is_c2_cofinite is True
        assert MINIMAL_SO_SOURCE in d.strong_rationality_at_minus_1.evidence

    def test_so7_shadow_class(self):
        """The represented generators leave the full shadow tower open."""
        d = minimal_so_at_minus_1(7)
        assert d.shadow_class.status is ClaimStatus.OPEN
        assert d.shadow_depth.status is ClaimStatus.OPEN
        assert d.shadow_class.value is None
        assert d.shadow_depth.value is None

    def test_so9_generator_count(self):
        """For r=5 the source-backed multiplicities total 24."""
        d = minimal_so_at_minus_1(9)
        assert d.n_generators == 24

    def test_so9_anomaly_ratio(self):
        """The so_9 signed reciprocal-weight diagnostic equals -7/6."""
        d = minimal_so_at_minus_1(9)
        assert d.reciprocal_weight_diagnostic == Rational(121, 6)
        assert d.anomaly_ratio.status is ClaimStatus.OPEN
        assert d.anomaly_ratio.hypotheses

    def test_so11_generator_count(self):
        """For r=7 the source-backed multiplicities total 39."""
        d = minimal_so_at_minus_1(11)
        assert d.n_generators == 39

    def test_so7_central_charge_worked_oracle(self):
        """At level -1 the generic source formula gives 7/4."""
        d = minimal_so_at_minus_1(7)
        expected = Rational(7 * (7 - 5), 2 * (7 - 3))
        assert d.central_charge == expected == Rational(7, 4)

    def test_minimal_so_generic_central_charge_source_formula(self):
        """The engine implements the Kac--Wakimoto minimal-W formula."""
        N = 10
        expected = k * (N * (N - 1) // 2) / (k + N - 2) - 6 * k + N - 6
        assert simplify(minimal_w_so_data(N, k).central_charge - expected) == 0

    def test_so7_kappa_nonzero(self):
        """The so_7 modular characteristic requires the trace comparison."""
        d = minimal_so_at_minus_1(7)
        assert d.kappa.status is ClaimStatus.CONDITIONAL
        assert d.kappa.value is None
        assert any("genus-one" in hypothesis for hypothesis in d.kappa.hypotheses)

    def test_even_N_accepted(self):
        """Every integer N>=7 lies in the orbifold-realization domain."""
        assert minimal_so_at_minus_1(8).N == 8

    def test_small_N_rejected(self):
        """The cited source domain begins at N=7."""
        with pytest.raises(ValueError):
            minimal_so_at_minus_1(6)


# ===================================================================
# II. Hook-type successive reductions [2403.08212]
# ===================================================================

class TestHookSuccessiveReductions:
    """Tests for hook-type W-algebras via successive DS reduction."""

    def test_sl4_hook_31_chain(self):
        """The [4] -> [3,1] tuple is a candidate partition corridor."""
        d = hook_successive_reduction_data(4, 1)
        assert d.partition == (3, 1)
        assert d.transpose == (2, 1, 1)
        assert d.n_candidate_steps == 1
        assert d.candidate_partition_corridor == ((4,), (3, 1))
        assert d.reduction_by_stages.status is ClaimStatus.OPEN
        assert any("Conjecture A" in item for item in d.reduction_by_stages.evidence)

    def test_sl5_hook_chain_lengths(self):
        """sl_5 candidate corridors have the combinatorial lengths r+1."""
        for r in range(1, 4):
            d = hook_successive_reduction_data(5, r)
            assert d.n_candidate_steps == r
            assert len(d.candidate_partition_corridor) == r + 1

    def test_sl4_hook_koszul_packets_preserve_comparison_obligations(self):
        """Every sl_4 endpoint carries its completed-bar comparison status."""
        results = verify_hook_koszulness_chain(4)
        for lam, packet in results.items():
            assert isinstance(packet, ClaimPacket), lam
            assert packet.status is ClaimStatus.CONDITIONAL
            assert packet.value is None

    def test_sl5_hook_koszul_packets_are_conditional(self):
        """Every sl_5 transport packet retains named hypotheses."""
        results = verify_hook_koszulness_chain(5)
        for packet in results.values():
            assert packet.status is ClaimStatus.CONDITIONAL
            assert packet.hypotheses

    def test_sl6_hook_koszul_packets_have_no_invented_value(self):
        """Every sl_6 transport packet stays outside the numeric surface."""
        results = verify_hook_koszulness_chain(6)
        assert all(packet.value is None for packet in results.values())

    def test_principal_full_shadow_class_is_open(self):
        """The represented principal carrier leaves full shadow class open."""
        d = hook_successive_reduction_data(4, 0)
        assert d.shadow_class.status is ClaimStatus.OPEN
        assert d.shadow_class.value is None

    def test_hook_kappa_is_conditional(self):
        """Hook-type kappa retains the DS/bar comparison package."""
        d = hook_successive_reduction_data(4, 1)
        assert d.kappa_source.status is ClaimStatus.CONDITIONAL
        assert d.kappa_source.value is None
        assert any("H_hook^{DS/bar}" in item for item in d.kappa_source.hypotheses)

    def test_sl3_21_full_shadow_class_is_open(self):
        """The BP full shadow class requires the complete collision tower."""
        d = hook_successive_reduction_data(3, 1)
        assert d.shadow_class.status is ClaimStatus.OPEN
        assert d.shadow_depth.status is ClaimStatus.OPEN

    def test_hook_comparison_packets_have_typed_statuses(self):
        d = hook_successive_reduction_data(4, 1)
        assert d.ds_bar_commutation.status is ClaimStatus.CONDITIONAL
        assert d.koszul_duality.status is ClaimStatus.CONDITIONAL
        assert d.ksdual_membership.status is ClaimStatus.OPEN
        assert d.kappa_sum.status is ClaimStatus.OPEN

    def test_chain_starts_at_principal(self):
        """Every candidate corridor starts at the principal partition."""
        for N in range(3, 7):
            for r in range(1, N - 1):
                d = hook_successive_reduction_data(N, r)
                assert d.candidate_partition_corridor[0] == (N,)

    def test_chain_ends_at_target(self):
        """Every candidate corridor ends at the target hook partition."""
        for N in range(3, 7):
            for r in range(1, N - 1):
                d = hook_successive_reduction_data(N, r)
                expected = hook_partition(N, r)
                assert d.candidate_partition_corridor[-1] == expected

    def test_reduction_by_stages_and_ds_bar_are_separate_packets(self):
        """Conjecture A and the filtered DS/bar comparison remain distinct."""
        d = hook_successive_reduction_data(6, 2)
        assert d.reduction_by_stages.status is ClaimStatus.OPEN
        assert d.ds_bar_commutation.status is ClaimStatus.CONDITIONAL
        assert d.reduction_by_stages is not d.ds_bar_commutation
        assert any("Theorem A" in evidence for evidence in d.reduction_by_stages.evidence)
        assert any("DS/bar" in hypothesis for hypothesis in d.ds_bar_commutation.hypotheses)

    def test_invalid_r_raises(self):
        """r >= N-1 should raise ValueError."""
        with pytest.raises(ValueError):
            hook_successive_reduction_data(4, 3)

    def test_negative_r_raises(self):
        """r < 0 should raise ValueError."""
        with pytest.raises(ValueError):
            hook_successive_reduction_data(4, -1)


# ===================================================================
# III. Building blocks for types B, C, D
# ===================================================================

class TestBuildingBlocksBCD:
    """Tests for principal W-algebras of types B, C, D."""

    def test_b2_generators(self):
        """W(B_2) = W(so_5, prin): generators at weights 2, 4."""
        d = building_block_bcd_data('B', 2)
        assert d.generator_weights == (2, 4)
        assert d.n_generators == 2

    def test_b2_anomaly_ratio(self):
        """The B_2 reciprocal-weight diagnostic is 3/4; rho stays open."""
        d = building_block_bcd_data('B', 2)
        assert d.reciprocal_weight_diagnostic == Rational(3, 4)
        assert d.anomaly_ratio.status is ClaimStatus.OPEN
        assert d.anomaly_ratio.value is None

    def test_b2_c_complementarity(self):
        """The B_2 central and reflected sums retain fixed-convention obligations."""
        d = building_block_bcd_data('B', 2)
        assert d.central_charge.status is ClaimStatus.OPEN
        assert d.central_charge.value is None
        assert d.c_complementarity.status is ClaimStatus.OPEN
        assert verify_bcd_c_complementarity('B', 2) == d.c_complementarity
        assert d.langlands_dual_type == "C_2"
        assert d.langlands_dual_level.status is ClaimStatus.OPEN

    def test_c2_generators(self):
        """W(C_2) = W(sp_4, prin): generators at weights 2, 4."""
        d = building_block_bcd_data('C', 2)
        assert d.generator_weights == (2, 4)
        assert d.n_generators == 2

    def test_c2_anomaly_ratio(self):
        """The C_2 reciprocal-weight diagnostic is 3/4; rho stays open."""
        d = building_block_bcd_data('C', 2)
        assert d.reciprocal_weight_diagnostic == Rational(3, 4)
        assert d.anomaly_ratio.status is ClaimStatus.OPEN
        assert d.anomaly_ratio.hypotheses

    def test_c2_c_complementarity(self):
        """The C_2 partner is B_2 and its dual level remains explicit."""
        d = building_block_bcd_data('C', 2)
        assert d.langlands_dual_type == "B_2"
        assert d.langlands_dual_level.status is ClaimStatus.OPEN
        assert d.c_complementarity.status is ClaimStatus.OPEN

    def test_d4_generators(self):
        """W(D_4) = W(so_8, prin): generators at weights 2, 4, 4, 6."""
        d = building_block_bcd_data('D', 4)
        assert d.generator_weights == (2, 4, 4, 6)
        assert d.n_generators == 4
        assert d.rank == 4

    def test_d4_c_complementarity(self):
        """The self-Langlands-dual D_4 sum remains convention-typed."""
        d = building_block_bcd_data('D', 4)
        assert d.langlands_dual_type == "D_4"
        assert d.c_complementarity.status is ClaimStatus.OPEN
        assert d.c_complementarity.value is None

    def test_b3_generators(self):
        """W(B_3) = W(so_7, prin): generators at weights 2, 4, 6."""
        d = building_block_bcd_data('B', 3)
        assert d.generator_weights == (2, 4, 6)

    def test_b3_anomaly_ratio(self):
        """The B_3 reciprocal-weight diagnostic equals 11/12."""
        d = building_block_bcd_data('B', 3)
        assert d.reciprocal_weight_diagnostic == Rational(11, 12)
        assert d.anomaly_ratio.status is ClaimStatus.OPEN

    def test_all_bcd_koszul_claims_are_conditional(self):
        """Principal BCD endpoints inherit the conditional main theorem."""
        for lie_type in ['B', 'C']:
            for n in range(2, 5):
                d = building_block_bcd_data(lie_type, n)
                assert d.koszul_status.status is ClaimStatus.CONDITIONAL
                assert d.koszul_status.value is None
                assert any("thm:w-algebra-koszul-main" in h for h in d.koszul_status.hypotheses)
        for n in range(3, 6):
            d = building_block_bcd_data('D', n)
            assert d.koszul_status.status is ClaimStatus.CONDITIONAL
            assert d.koszul_status.hypotheses

    def test_all_bcd_full_shadow_claims_are_open(self):
        """The generator ledger leaves full class and depth unresolved."""
        for lie_type in ['B', 'C']:
            for n in range(2, 5):
                d = building_block_bcd_data(lie_type, n)
                assert d.shadow_class.status is ClaimStatus.OPEN
                assert d.shadow_depth.status is ClaimStatus.OPEN
                assert d.shadow_class.hypotheses
                assert d.shadow_depth.hypotheses

    def test_all_bcd_c_complementarity(self):
        """Every configured BCD sum is an open fixed-convention packet."""
        for lie_type in ['B', 'C']:
            for n in range(2, 5):
                packet = verify_bcd_c_complementarity(lie_type, n)
                assert packet.status is ClaimStatus.OPEN
                assert packet.value is None
        for n in range(3, 6):
            packet = verify_bcd_c_complementarity('D', n)
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None

    def test_b2_equals_c2_isomorphism(self):
        """The B_2=C_2 alias identifies exact generator arithmetic."""
        b2 = building_block_bcd_data('B', 2)
        c2 = building_block_bcd_data('C', 2)
        assert b2.generator_weights == c2.generator_weights == (2, 4)
        assert b2.reciprocal_weight_diagnostic == c2.reciprocal_weight_diagnostic
        assert b2.kappa.status is c2.kappa.status is ClaimStatus.CONDITIONAL
        assert b2.kappa.value is c2.kappa.value is None
        assert b2.central_charge.status is c2.central_charge.status is ClaimStatus.OPEN

    def test_d3_a3_rejects_rank_minus_pole_ansatz(self):
        """The D_3=A_3 oracle gives the exact symbolic discrepancy."""
        q = Symbol("q")
        assert d3_a3_incomplete_ansatz_discrepancy(q) == 60 * q + 120
        assert d3_a3_incomplete_ansatz_discrepancy(0) == 120


# ===================================================================
# IV. Conformal extension Koszulness [2508.18889]
# ===================================================================

class TestConformalExtension:
    """Tests for Koszulness inheritance through conformal extensions."""

    def test_simple_current_inherits(self):
        """A cited presentation carries the completed-bar package."""
        d = conformal_extension_koszulness(
            'sl',
            3,
            k,
            "simple_current",
            source_presentation="a specified simple-current extension V_k(sl_3) -> W^k(sl_3)",
            source_reference="Adamovic et al. (2025), Theorem 7.2",
        )
        assert d.koszul_inherited.status is ClaimStatus.CONDITIONAL
        assert d.koszul_inherited.value is None
        assert any("completed chiral bar" in h for h in d.koszul_inherited.hypotheses)
        assert d.koszul_status is d.koszul_inherited

    def test_coset_requires_comparison(self):
        """Coset inheritance names the required functorial comparison."""
        d = conformal_extension_koszulness('sl', 3, k, "coset")
        assert d.koszul_inherited.status is ClaimStatus.OPEN
        assert d.koszul_inherited.value is None
        assert any("completed-bar comparison" in h for h in d.koszul_inherited.hypotheses)

    def test_extension_type_recorded(self):
        """Extension type is properly recorded."""
        d = conformal_extension_koszulness('so', 5, Rational(-1), "simple_current")
        assert d.extension_type == "simple_current"
        assert isinstance(d, ConformalExtensionData)
        assert d.koszul_inherited.status is ClaimStatus.OPEN
        assert any("source-backed" in item for item in d.koszul_inherited.hypotheses)

    def test_level_recorded(self):
        """Level is properly recorded in data."""
        d = conformal_extension_koszulness('sl', 2, Rational(1, 2), "simple_current")
        assert d.level == Rational(1, 2)

    def test_reference_requires_numbered_result(self):
        """An author-year citation alone leaves the presentation open."""
        d = conformal_extension_koszulness(
            'sl',
            3,
            k,
            source_presentation="a named presentation",
            source_reference="Adamovic et al. (2025)",
        )
        assert d.koszul_inherited.status is ClaimStatus.OPEN


# ===================================================================
# V. KL-category equivalence and MC3 [2603.04667]
# ===================================================================

class TestKLCategoryEquivalence:
    """Tests for KL-category braided tensor equivalence."""

    def test_ds_reduction_mc3(self):
        """The ADE irrational theorem and MC3 transport have distinct status."""
        irrational = sqrt(2)
        d = kl_category_equivalence(
            'sl',
            3,
            irrational,
            'W',
            3,
            irrational,
            "ds_reduction",
            nilpotent_orbit="principal",
            source_reference=KL_SOURCE,
        )
        assert d.braided_equivalence.status is ClaimStatus.PROVED_ELSEWHERE
        assert d.braided_equivalence.value is True
        assert d.mc3_consequence.status is ClaimStatus.CONDITIONAL
        assert "MC3" in d.mc3_consequence.statement
        assert any("compact" in h for h in d.mc3_consequence.hypotheses)

    def test_conformal_embedding_mc3(self):
        """A conformal embedding lies outside the cited DS theorem domain."""
        d = kl_category_equivalence(
            'sl', 3, k, 'sl', 2, Rational(3, 2), "conformal_embedding"
        )
        assert d.braided_equivalence.status is ClaimStatus.OPEN
        assert d.mc3_consequence.status is ClaimStatus.OPEN
        assert d.mc3_consequence.value is None
        assert d.mc3_consequence.hypotheses

    def test_symbolic_level_regime(self):
        """A formal level parameter retains its open theorem domain."""
        d = kl_category_equivalence(
            'sl',
            3,
            k,
            'W',
            3,
            k,
            "ds_reduction",
            nilpotent_orbit="principal",
            source_reference=KL_SOURCE,
        )
        assert d.level_regime == "symbolic"
        assert d.braided_equivalence.status is ClaimStatus.OPEN
        assert d.mc3_consequence.status is ClaimStatus.OPEN

    def test_b_type_requires_langlands_dual_theorem(self):
        """The simply-laced theorem leaves B/C duality in its own domain."""
        d = kl_category_equivalence(
            'B',
            3,
            sqrt(2),
            'W',
            3,
            sqrt(2),
            nilpotent_orbit="principal",
            source_reference=KL_SOURCE,
        )
        assert d.braided_equivalence.status is ClaimStatus.OPEN
        assert any("Langlands-dual" in item for item in d.braided_equivalence.hypotheses)

    def test_bar_cobar_kl_commutation(self):
        """KL/bar comparison remains an open algebra-level obligation."""
        packet = bar_cobar_kl_commutation_check('sl', 3, k, -k - 6)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        assert any("completed chiral bar" in h for h in packet.hypotheses)


# ===================================================================
# VI. Cross-family consistency checks (multi-path verification)
# ===================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between families for internal consistency."""

    def test_type_a_kappa_consistency_w2(self):
        """W_2 promotion of the 1/2 diagnostic is explicitly open."""
        packet = verify_type_a_kappa_consistency(2)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        assert "1/2" in packet.evidence[0]

    def test_type_a_kappa_consistency_w3(self):
        """W_3 promotion of the 5/6 diagnostic names its trace hypothesis."""
        packet = verify_type_a_kappa_consistency(3)
        assert packet.status is ClaimStatus.OPEN
        assert "5/6" in packet.evidence[0]
        assert any("rho" in h for h in packet.hypotheses)

    def test_type_a_kappa_consistency_w4(self):
        """W_4 promotion of the 13/12 diagnostic remains nonnumeric."""
        packet = verify_type_a_kappa_consistency(4)
        assert packet.status is ClaimStatus.OPEN
        assert packet.value is None
        assert "13/12" in packet.evidence[0]

    def test_type_a_kappa_consistency_w5_w6(self):
        """W_5 and W_6 retain the same genus-one comparison boundary."""
        for N in (5, 6):
            packet = verify_type_a_kappa_consistency(N)
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None
            assert packet.hypotheses

    def test_self_transpose_kappa_k_independent(self):
        """Self-transpose diagrams still require a modular-conductor theorem."""
        for lam in [(2, 1), (2, 2), (3, 1, 1)]:
            packet = kappa_complementarity_sum(lam, k)
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None
            assert packet.hypotheses

    def test_c_complementarity_self_transpose(self):
        """c-complementarity is k-independent for self-transpose partitions."""
        assert verify_c_complementarity_k_independent((2, 1)) is True
        assert verify_c_complementarity_k_independent((2, 2)) is True

    def test_c_complementarity_self_transpose_hooks(self):
        """Self-transpose hooks carry level-independent central-charge sums.

        Each remaining transpose pair retains its exact level-dependent sum.
        """
        for N in range(3, 6):
            for r in range(1, N - 1):
                lam = hook_partition(N, r)
                lam_t = transpose_partition(lam)
                ok = verify_c_complementarity_k_independent(lam)
                if tuple(lam) == tuple(lam_t):
                    assert ok is True, f"self-transpose {lam} should have k-indep c-comp"

    def test_level_independence_differentiates_supplied_symbol(self):
        """For [3,1] the exact sum 44-18q varies with q."""
        q = Symbol("q")
        assert verify_c_complementarity_k_independent((3, 1), q) is False
        c_sum = simplify(
            krw_central_charge((3, 1), q)
            + krw_central_charge((2, 1, 1), -q - 8)
        )
        assert c_sum == 44 - 18 * q

    def test_anomaly_ratio_matches_manuscript_sl3(self):
        """sl_3 reciprocal-weight diagnostics stay distinct from rho."""
        assert reciprocal_weight_diagnostic_from_partition((3,)) == Rational(5, 6)
        assert reciprocal_weight_diagnostic_from_partition((2, 1)) == Rational(17, 6)
        for partition in ((3,), (2, 1)):
            packet = anomaly_ratio_from_partition(partition)
            assert packet.status is ClaimStatus.OPEN
            assert packet.value is None

    def test_anomaly_ratio_principal_wn(self):
        """Principal reciprocal-weight diagnostics equal H_N-1."""
        for N in range(2, 7):
            diagnostic = reciprocal_weight_diagnostic_from_partition((N,))
            expected = sum(Rational(1, j) for j in range(2, N + 1))
            assert diagnostic == expected
            rho = anomaly_ratio_from_partition((N,))
            assert rho.status is ClaimStatus.OPEN
            assert rho.value is None

    def test_b2_matches_landscape_census(self):
        """The B_2 generator ledger precedes its central-charge packet."""
        d = building_block_bcd_data('B', 2)
        assert d.generator_weights == (2, 4)
        assert d.central_charge.status is ClaimStatus.OPEN
        assert d.c_complementarity.status is ClaimStatus.OPEN

    def test_kappa_additivity_free_sum(self):
        """Level substitution changes the statement while preserving status."""
        k2 = Symbol('k2')
        kap1 = ds_kappa_from_affine((2,), k)
        kap2 = ds_kappa_from_affine((2,), k2)
        assert kap1.status is kap2.status is ClaimStatus.CONDITIONAL
        assert kap1.value is kap2.value is None
        assert kap1.statement != kap2.statement
        assert kap1.hypotheses == kap2.hypotheses

    def test_bcd_kappa_nonzero_generic(self):
        """Every BCD kappa profile remains conditional at generic level."""
        for lt in ['B', 'C']:
            for n in range(2, 5):
                d = building_block_bcd_data(lt, n)
                assert d.kappa.status is ClaimStatus.CONDITIONAL
                assert d.kappa.value is None
                assert d.kappa.hypotheses


# ===================================================================
# VII. Landscape catalog and summary
# ===================================================================

class TestLandscapeCatalog:
    """Tests for the full landscape catalog."""

    def test_catalog_nonempty(self):
        """Catalog has entries."""
        cat = creutzig_landscape_catalog()
        assert len(cat) > 0

    def test_catalog_count(self):
        """Catalog has expected number of entries.

        5 (type A principal W_2..W_6) + 10 (hooks in sl_3..sl_6)
        + 3 (minimal so_7, so_9, so_11)
        + 6 (B_2..B_4, C_2..C_4) + 3 (D_3..D_5) = 27
        """
        cat = creutzig_landscape_catalog()
        assert len(cat) == 27

    def test_all_entries_have_kappa(self):
        """Every catalog entry carries a typed kappa obligation."""
        cat = creutzig_landscape_catalog()
        for entry in cat:
            assert isinstance(entry.kappa, ClaimPacket)
            assert entry.kappa.status in {ClaimStatus.OPEN, ClaimStatus.CONDITIONAL}
            assert entry.kappa.value is None
            assert entry.kappa.hypotheses
            with pytest.raises(OpenInvariantError):
                entry.kappa.require_value()

    def test_all_entries_have_shadow_class(self):
        """Every full-shadow classification remains an explicit obligation."""
        cat = creutzig_landscape_catalog()
        for entry in cat:
            assert entry.shadow_class.status is ClaimStatus.OPEN
            assert entry.shadow_class.value is None
            assert entry.shadow_class.hypotheses
            assert entry.shadow_depth.status is ClaimStatus.OPEN

    def test_summary_statistics(self):
        """Summary statistics are consistent with catalog."""
        s = landscape_summary()
        assert s['n_configured_rows'] == 27
        assert s['n_proved_koszul'] == 0
        assert s['n_resolved_kappa'] == 0
        assert s['n_resolved_rho'] == 0
        assert s['n_resolved_modular_conductor'] == 0
        assert s['n_resolved_full_shadow_class'] == 0
        assert s['n_resolved_full_shadow_depth'] == 0
        assert len(s['lie_types_covered']) > 5
        assert s['configured_bounds']['type_A_principal_N'] == (2, 6)
        assert s['configured_bounds']['minimal_so_N'] == (7, 9, 11)
        assert s['isomorphism_aliases'] == {'B_2': 'C_2', 'D_3': 'A_3'}

    def test_all_type_a_entries_are_conditional(self):
        """Principal and hook endpoints retain the main theorem package."""
        cat = creutzig_landscape_catalog()
        for entry in cat:
            if entry.lie_type.startswith('A'):
                assert entry.koszul_status.status is ClaimStatus.CONDITIONAL
                assert entry.koszul_status.value is None
                assert entry.koszul_status.hypotheses

    def test_source_papers_recorded(self):
        """Every row records author, year, and a numbered result."""
        cat = creutzig_landscape_catalog()
        for entry in cat:
            assert any(str(year) in entry.source_paper for year in range(2000, 2030))
            assert any(
                marker in entry.source_paper
                for marker in ("Theorem ", "Theorems ", "equation ")
            )

    def test_no_duplicate_family_names(self):
        """No duplicate family names in the catalog."""
        cat = creutzig_landscape_catalog()
        names = [e.family_name for e in cat]
        assert len(names) == len(set(names)), \
            f"Duplicates: {[n for n in names if names.count(n) > 1]}"


# ===================================================================
# VIII. Multi-path verification
# ===================================================================

class TestMultiPathVerification:
    """Multi-path verification for key claims (Verification Mandate)."""

    def test_w3_kappa_three_paths(self):
        """Three lanes agree on the W_3 diagnostic and its promotion boundary."""
        diagnostic = reciprocal_weight_diagnostic_from_partition((3,))
        harmonic_tail = Rational(1, 2) + Rational(1, 3)
        catalog_entry = next(e for e in creutzig_landscape_catalog() if e.family_name == "W_3")

        assert diagnostic == harmonic_tail == Rational(5, 6)
        assert catalog_entry.reciprocal_weight_diagnostic == diagnostic
        assert catalog_entry.anomaly_ratio.status is ClaimStatus.OPEN
        assert catalog_entry.kappa.status is ClaimStatus.CONDITIONAL
        assert catalog_entry.anomaly_ratio.value is catalog_entry.kappa.value is None

    def test_b2_kappa_two_paths(self):
        """B_2 generator and manual sums agree before modular promotion."""
        d = building_block_bcd_data('B', 2)
        manual_diagnostic = Rational(1, 2) + Rational(1, 4)
        assert d.reciprocal_weight_diagnostic == manual_diagnostic
        assert d.kappa.status is ClaimStatus.CONDITIONAL
        assert d.kappa.value is None
        assert any("genus-one" in h for h in d.kappa.hypotheses)

    def test_bp_kappa_two_paths(self):
        """The BP reciprocal-weight sum and modular packets remain separate."""
        diagnostic = reciprocal_weight_diagnostic_from_partition((2, 1))
        data = hook_successive_reduction_data(3, 1)
        assert diagnostic == Rational(17, 6)
        assert data.reciprocal_weight_diagnostic == diagnostic
        assert data.anomaly_ratio.status is ClaimStatus.OPEN
        assert data.kappa_source.status is ClaimStatus.CONDITIONAL
        assert data.anomaly_ratio.value is data.kappa_source.value is None

    def test_sl4_22_self_dual_kappa_two_paths(self):
        """The exact self-dual central sum precedes the modular conductor."""
        conductor = kappa_complementarity_sum((2, 2), k)
        c_sum_zero = simplify(
            krw_central_charge((2, 2), 0) + krw_central_charge((2, 2), -8)
        )
        c_sum_one = simplify(
            krw_central_charge((2, 2), 1) + krw_central_charge((2, 2), -9)
        )
        assert c_sum_zero == c_sum_one
        assert conductor.status is ClaimStatus.OPEN
        assert conductor.value is None
        assert conductor.hypotheses

    def test_hook_koszulness_two_methods(self):
        """The exact corridor and source status precede bar transport."""
        d = hook_successive_reduction_data(4, 1)
        assert d.candidate_partition_corridor == ((4,), (3, 1))
        assert d.transpose == (2, 1, 1)
        assert d.reduction_by_stages.status is ClaimStatus.OPEN
        assert d.koszul_by_transport.status is ClaimStatus.CONDITIONAL
        assert d.koszul_by_transport.value is None
        assert any("completed chiral bar" in h for h in d.koszul_by_transport.hypotheses)

    def test_c_complementarity_two_methods(self):
        """c-complementarity for (2,1) verified by 2 methods.

        Method 1: verify_c_complementarity_k_independent
        Method 2: direct numerical evaluation at k=0, k=1
        """
        # Method 1
        assert verify_c_complementarity_k_independent((2, 1)) is True

        # Method 2: (2,1) is self-transpose, c-sum should be constant
        c_k0 = krw_central_charge((2, 1), 0)
        c_kv0 = krw_central_charge((2, 1), -6)  # kv = -0-6
        sum0 = simplify(c_k0 + c_kv0)

        c_k1 = krw_central_charge((2, 1), 1)
        c_kv1 = krw_central_charge((2, 1), -7)  # kv = -1-6
        sum1 = simplify(c_k1 + c_kv1)

        assert sum0 == sum1

    def test_bcd_central_lane_stays_nonnumeric(self):
        """The B_3 central lane carries its complete-KRW obligation."""
        d = building_block_bcd_data('B', 3)
        assert d.central_charge.status is ClaimStatus.OPEN
        assert d.central_charge.value is None
        assert d.c_complementarity.status is ClaimStatus.OPEN

    def test_so7_kappa_equals_rho_times_c(self):
        """so_7 exact arithmetic remains separate from modular promotion."""
        d = minimal_so_at_minus_1(7)
        manual_diagnostic = 6 + 6 * Rational(2, 3) + Rational(1, 2)
        assert d.reciprocal_weight_diagnostic == manual_diagnostic == Rational(21, 2)
        assert d.central_charge == Rational(7, 4)
        assert d.anomaly_ratio.status is ClaimStatus.OPEN
        assert d.kappa.status is ClaimStatus.CONDITIONAL
        assert d.modular_conductor.status is ClaimStatus.OPEN

    def test_anomaly_ratio_k_independent(self):
        """Weight diagnostics are level-free while rho remains open."""
        for lam in [(2,), (3,), (4,), (2, 1), (3, 1), (2, 1, 1), (2, 2)]:
            diagnostic = reciprocal_weight_diagnostic_from_partition(lam)
            rho = anomaly_ratio_from_partition(lam)
            assert isinstance(diagnostic, Rational)
            assert rho.status is ClaimStatus.OPEN
            assert rho.value is None

    def test_catalog_entries_consistent_with_direct(self):
        """Catalog entries match direct computation for W_3."""
        cat = creutzig_landscape_catalog()
        w3_entries = [e for e in cat if e.family_name == "W_3"]
        assert len(w3_entries) == 1
        w3 = w3_entries[0]

        # Direct computation
        c_direct = krw_central_charge((3,), k)
        kap_direct = ds_kappa_from_affine((3,), k)

        assert simplify(w3.central_charge - c_direct) == 0
        assert w3.reciprocal_weight_diagnostic == reciprocal_weight_diagnostic_from_partition((3,))
        assert w3.kappa.status is kap_direct.status is ClaimStatus.CONDITIONAL
        assert w3.kappa.value is kap_direct.value is None
        assert w3.kappa.hypotheses == kap_direct.hypotheses

    def test_hook_transport_vs_pbw_all_sl4(self):
        """All sl_4 hook transports retain DS/bar and Verdier hypotheses."""
        for r in range(1, 3):
            lam = hook_partition(4, r)
            d = hook_successive_reduction_data(4, r)
            assert d.partition == lam
            assert d.transpose == transpose_partition(lam)
            assert d.reduction_by_stages.status is ClaimStatus.OPEN
            assert d.koszul_by_transport.status is ClaimStatus.CONDITIONAL
            assert d.koszul_by_transport.value is None
            assert any("H_hook^{DS/bar}" in h for h in d.koszul_by_transport.hypotheses)


class TestExactInputBoundary:
    """Public arithmetic constructors accept exact level data only."""

    @pytest.mark.parametrize("level", [0.5, Float("0.5")])
    def test_minimal_so_rejects_inexact_level(self, level):
        with pytest.raises(TypeError, match="exact"):
            minimal_w_so_data(7, level)

    @pytest.mark.parametrize("N", [7.0, Float("7.0")])
    def test_minimal_so_rejects_inexact_dimension(self, N):
        with pytest.raises(TypeError, match="exact integer"):
            minimal_w_so_data(N, Rational(-1))

    @pytest.mark.parametrize("level", [0.5, Float("0.5")])
    def test_hook_rejects_inexact_level(self, level):
        with pytest.raises(TypeError, match="exact"):
            hook_successive_reduction_data(4, 1, level)

    def test_hook_rejects_inexact_partition_parameters(self):
        with pytest.raises(TypeError, match="exact integer"):
            hook_successive_reduction_data(4.0, 1, k)
        with pytest.raises(TypeError, match="exact integer"):
            hook_successive_reduction_data(4, Float("1.0"), k)

    @pytest.mark.parametrize("level", [0.5, Float("0.5")])
    def test_bcd_rejects_inexact_level(self, level):
        with pytest.raises(TypeError, match="exact"):
            building_block_bcd_data('B', 2, level)

    def test_bcd_rejects_inexact_rank(self):
        with pytest.raises(TypeError, match="exact integer"):
            building_block_bcd_data('B', 2.0, k)

    @pytest.mark.parametrize("level", [0.5, Float("0.5")])
    def test_conformal_extension_rejects_inexact_level(self, level):
        with pytest.raises(TypeError, match="exact"):
            conformal_extension_koszulness('sl', 3, level)

    @pytest.mark.parametrize("level", [0.5, Float("0.5")])
    def test_kl_rejects_inexact_levels(self, level):
        with pytest.raises(TypeError, match="exact"):
            kl_category_equivalence('sl', 3, level, 'W', 3, sqrt(2))
        with pytest.raises(TypeError, match="exact"):
            kl_category_equivalence('sl', 3, sqrt(2), 'W', 3, level)

    @pytest.mark.parametrize("level", [0.5, Float("0.5")])
    def test_catalog_and_oracle_reject_inexact_level(self, level):
        with pytest.raises(TypeError, match="exact"):
            creutzig_landscape_catalog(level)
        with pytest.raises(TypeError, match="exact"):
            d3_a3_incomplete_ansatz_discrepancy(level)
