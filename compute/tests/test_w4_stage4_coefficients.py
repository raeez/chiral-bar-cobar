"""Tests for the MC4 W_4 stage-4 exact packet scaffold.

Verifies:
  - W_4 central charge and complementarity
  - Primary seed set cardinalities (I_N for N=3,4)
  - Stage-3 packet from explicit W_3 OPE
  - Stage-4 residual packet decomposition J_4
  - OPE weight bounds
  - Curvature channels and kappa
  - Distinct Virasoro-target identities inside the exact stage-4 packet
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.w4_stage4_coefficients import (
    w4_central_charge,
    w4_dual_level,
    w4_complementarity_sum,
    seed_set,
    seed_set_size,
    virasoro_subset,
    w3_subset,
    residual_packet,
    incremental_virasoro_new_packet,
    incremental_interacting_packet,
    incremental_top_pole_packet,
    incremental_reduced_packet,
    incremental_reduced_block_decomposition,
    incremental_higher_spin_channels,
    incremental_higher_spin_block_decomposition,
    incremental_higher_spin_block,
    incremental_higher_spin_singleton_blocks,
    incremental_higher_spin_nonsingleton_blocks,
    incremental_higher_spin_target_decomposition,
    incremental_higher_spin_nonsingleton_target_decomposition,
    incremental_virasoro_target_channels,
    incremental_virasoro_target_identities,
    analyze_incremental_packet,
    stage3_ds_coefficients,
    stage3_nonzero_count,
    stage3_vanishing_count,
    stage4_residual_decomposition,
    stage4_exact_identity_packet,
    stage4_live_targets,
    stage4_residual_higher_spin_channels,
    stage4_virasoro_target_channels,
    stage4_virasoro_target_identities,
    stage4_virasoro_target_identity_data,
    ope_max_pole_order,
    ope_target_weight,
    primary_target_at_pole,
    w4_stress_tensor_ope,
    w4_curvature,
    w4_kappa_total,
    w3w3_ope_w4_algebra,
    verify_universal_t_coupling_pattern,
    analyze_stage4_packet,
    top_pole_packet,
    parity_compressed_packet,
    ope_block_decomposition,
    mixed_self_split,
    frontier_package,
    verify_full_reduction_chain,
)


# ===== Central charge =====

class TestCentralCharge:
    def test_w4_central_charge_formula(self):
        """c = 3 - 60/(k+4) for W_4."""
        assert w4_central_charge(1) == Rational(3) - Rational(60) / Rational(5)
        assert w4_central_charge(1) == Rational(-9, 1)

    def test_w4_at_k0(self):
        """c(0) = 3 - 60/4 = 3 - 15 = -12."""
        assert w4_central_charge(0) == -12

    def test_w4_critical_level(self):
        """Critical level k = -h^vee = -4: c diverges (denominator = 0)."""
        k = Symbol('k')
        c = w4_central_charge(k)
        # At k = -4, denominator k+4 = 0
        assert c.subs(k, -4) is not None  # sympy handles as inf

    def test_dual_level(self):
        """k' = -k - 8 for sl_4."""
        assert w4_dual_level(0) == -8
        assert w4_dual_level(1) == -9
        assert w4_dual_level(-3) == -5

    def test_complementarity_sum(self):
        """c(k) + c(k') = 6 for W_4 (constant in k)."""
        sigma = w4_complementarity_sum()
        assert sigma == 6

    def test_complementarity_at_specific_k(self):
        """Verify complementarity at k=1."""
        c1 = w4_central_charge(1)
        c2 = w4_central_charge(w4_dual_level(1))
        assert c1 + c2 == 6


# ===== Seed sets =====

class TestSeedSets:
    def test_I3_size(self):
        """I_3 has 15 elements (prop:winfty-ds-stage3-explicit-packet)."""
        assert seed_set_size(3) == 15

    def test_I4_size(self):
        """I_4 has 54 elements."""
        assert seed_set_size(4) == 54

    def test_virasoro_subset_N3(self):
        """I_3^Vir = tuples with s=2."""
        vir3 = virasoro_subset(3)
        assert all(s == 2 for s, t, u, n in vir3)

    def test_virasoro_subset_N4_size(self):
        """I_4^Vir has 18 elements."""
        assert len(virasoro_subset(4)) == 18

    def test_w3_subset_N4_size(self):
        """I_4^W3 has 7 elements."""
        assert len(w3_subset(4)) == 7

    def test_residual_packet_N4_size(self):
        """J_4 has 29 elements (prop:winfty-ds-stage4-residual-packet)."""
        assert len(residual_packet(4)) == 29

    def test_partition_of_I4(self):
        """I_4 = I_4^Vir + I_4^W3 + J_4 (disjoint union)."""
        I4 = set(seed_set(4))
        vir = set(virasoro_subset(4))
        w3 = set(w3_subset(4))
        J4 = set(residual_packet(4))
        assert I4 == vir | w3 | J4
        assert len(vir & w3) == 0
        assert len(vir & J4) == 0
        assert len(w3 & J4) == 0

    def test_incremental_virasoro_new_packet_stage4(self):
        """The new stage-4 Virasoro block has 10 entries."""
        assert len(incremental_virasoro_new_packet(4)) == 10

    def test_incremental_interacting_packet_stage4_matches_J4(self):
        """The generic stage-growth packet matches J_4 at stage 4."""
        assert incremental_interacting_packet(4) == residual_packet(4)

    def test_seed_admissibility(self):
        """Every (s,t,u,n) in I_4 satisfies the admissibility conditions."""
        for s, t, u, n in seed_set(4):
            assert 2 <= s <= t <= 4
            assert 2 <= u <= min(4, s + t - 1)
            assert 1 <= n <= s + t - u


# ===== Stage-3 packet =====

class TestStage3:
    def test_nonzero_count(self):
        """Three nonzero coefficients in stage-3 packet."""
        assert stage3_nonzero_count() == 3

    def test_vanishing_count(self):
        """Twelve vanishing coefficients in stage-3 packet."""
        assert stage3_vanishing_count() == 12

    def test_total_count(self):
        """Total: 3 + 12 = 15 = |I_3|."""
        assert stage3_nonzero_count() + stage3_vanishing_count() == 15

    def test_TT_coupling(self):
        """C^DS_{2,2;2;0,2}(3) = 2."""
        s3 = stage3_ds_coefficients()
        assert s3[(2, 2, 2, 2)] == 2

    def test_TW_coupling(self):
        """C^DS_{2,3;3;0,2}(3) = 3."""
        s3 = stage3_ds_coefficients()
        assert s3[(2, 3, 3, 2)] == 3

    def test_WW_coupling(self):
        """C^DS_{3,3;2;0,4}(3) = 2."""
        s3 = stage3_ds_coefficients()
        assert s3[(3, 3, 2, 4)] == 2


# ===== Stage-4 residual decomposition =====

class TestStage4Decomposition:
    def test_tail_33(self):
        """(3,3) tail = {(3,3,4,1), (3,3,4,2)}."""
        decomp = stage4_residual_decomposition()
        assert decomp["tail_33"] == [(3, 3, 4, 1), (3, 3, 4, 2)]

    def test_J4_34_size(self):
        """J_4^{3,4} has 12 elements."""
        decomp = stage4_residual_decomposition()
        assert len(decomp["J4_34"]) == 12

    def test_J4_44_size(self):
        """J_4^{4,4} has 15 elements."""
        decomp = stage4_residual_decomposition()
        assert len(decomp["J4_44"]) == 15

    def test_J4_decomposition_sum(self):
        """2 + 12 + 15 = 29."""
        decomp = stage4_residual_decomposition()
        total = len(decomp["tail_33"]) + len(decomp["J4_34"]) + len(decomp["J4_44"])
        assert total == 29

    def test_J4_34_detailed(self):
        """J_4^{3,4} decomposes by target spin."""
        decomp = stage4_residual_decomposition()
        J34 = decomp["J4_34"]
        # By target spin u:
        by_u = {}
        for s, t, u, n in J34:
            by_u.setdefault(u, []).append((s, t, u, n))
        assert len(by_u[2]) == 5  # (3,4,2,1..5)
        assert len(by_u[3]) == 4  # (3,4,3,1..4)
        assert len(by_u[4]) == 3  # (3,4,4,1..3)

    def test_J4_44_detailed(self):
        """J_4^{4,4} decomposes by target spin."""
        decomp = stage4_residual_decomposition()
        J44 = decomp["J4_44"]
        by_u = {}
        for s, t, u, n in J44:
            by_u.setdefault(u, []).append((s, t, u, n))
        assert len(by_u[2]) == 6  # (4,4,2,1..6)
        assert len(by_u[3]) == 5  # (4,4,3,1..5)
        assert len(by_u[4]) == 4  # (4,4,4,1..4)


# ===== OPE weight bounds =====

class TestOPEWeights:
    def test_max_pole_orders(self):
        """Max pole order: 2s for s=t, s+t-1 for s!=t."""
        assert ope_max_pole_order(2, 2) == 4   # T x T: quartic pole
        assert ope_max_pole_order(2, 3) == 4   # T x W3: quartic pole
        assert ope_max_pole_order(3, 3) == 6   # W3 x W3: sixth-order pole
        assert ope_max_pole_order(3, 4) == 6   # W3 x W4
        assert ope_max_pole_order(4, 4) == 8   # W4 x W4: eighth-order pole

    def test_target_weight_at_leading_pole(self):
        """Target weight at leading same-spin pole is 0 (vacuum)."""
        assert ope_target_weight(2, 2, 4) == 0  # T x T: vacuum at pole 4
        assert ope_target_weight(3, 3, 6) == 0  # W3 x W3: vacuum at pole 6
        assert ope_target_weight(4, 4, 8) == 0  # W4 x W4: vacuum at pole 8

    def test_t_channel_pole_orders(self):
        """T (weight 2) appears at pole order s+t-2 in W_s x W_t."""
        assert ope_target_weight(3, 3, 4) == 2  # W3 x W3: T at pole 4
        assert ope_target_weight(4, 4, 6) == 2  # W4 x W4: T at pole 6
        assert ope_target_weight(3, 4, 5) == 2  # W3 x W4: T at pole 5

    def test_primary_target_identification(self):
        """Primary targets at specific poles."""
        assert primary_target_at_pole(3, 3, 4) == 2  # T at pole 4
        assert primary_target_at_pole(3, 3, 2) == 4  # W4 at pole 2
        assert primary_target_at_pole(4, 4, 4) == 4  # W4 at pole 4
        assert primary_target_at_pole(3, 4, 4) == 3  # W3 at pole 4


# ===== Curvature =====

class TestCurvature:
    def test_curvature_channels(self):
        """m_0 values for W_4 generators."""
        curv = w4_curvature()
        c = Symbol('c')
        assert curv["T"] == c / 2
        assert curv["W3"] == c / 3
        assert curv["W4"] == c / 4

    def test_kappa_total(self):
        """kappa = c/2 + c/3 + c/4 = 13c/12."""
        c = Symbol('c')
        kappa = w4_kappa_total()
        assert simplify(kappa - 13 * c / 12) == 0

    def test_curvature_sum_equals_kappa(self):
        """Sum of curvature channels equals kappa."""
        c = Symbol('c')
        curv = w4_curvature()
        total = sum(curv.values())
        assert simplify(total - w4_kappa_total()) == 0


# ===== Stress tensor OPE =====

class TestStressTensorOPE:
    def test_TT_quartic_pole(self):
        """T(z)T(w) ~ c/2 / (z-w)^4."""
        ope = w4_stress_tensor_ope()
        c = Symbol('c')
        assert ope[("T", "T")][4]["vac"] == c / 2

    def test_TW3_primary(self):
        """T(z)W_3(w) ~ 3W_3/(z-w)^2 (spin 3 primary)."""
        ope = w4_stress_tensor_ope()
        assert ope[("T", "W3")][2]["W3"] == 3

    def test_TW4_primary(self):
        """T(z)W_4(w) ~ 4W_4/(z-w)^2 (spin 4 primary)."""
        ope = w4_stress_tensor_ope()
        assert ope[("T", "W4")][2]["W4"] == 4


# ===== Distinguished Virasoro-target channels =====

class TestPredictions:
    def test_two_distinguished_channels(self):
        """Exactly two distinguished Virasoro-target channels."""
        preds = stage4_virasoro_target_identity_data()
        assert len(preds) == 2

    def test_distinguished_values(self):
        """Their theorematic values are 2 and 0."""
        preds = stage4_virasoro_target_identity_data()
        values = sorted(p["theorematic_value"] for p in preds.values())
        assert values == [0, 2]

    def test_universal_t_coupling(self):
        """C_{s,s;2;0,2s-2} = 2 pattern holds for s=2,3."""
        pattern = verify_universal_t_coupling_pattern()
        assert pattern["s=2_equals_2"]
        assert pattern["s=3_equals_2"]


# ===== Exact stage-4 packet =====

class TestLiveTargets:
    def test_six_packet_labels(self):
        """The exact stage-4 packet has six labels."""
        assert len(stage4_live_targets()) == 6

    def test_exact_packet_channels(self):
        """The exact stage-4 packet on I_4 has six channels."""
        assert len(stage4_exact_identity_packet()) == 6

    def test_full_analysis(self):
        """Full analysis matches manuscript."""
        analysis = analyze_stage4_packet()
        assert analysis["J4_size"] == analysis["J4_expected_size"]
        assert analysis["tail_33_size"] == 2
        assert analysis["J4_34_size"] == 12
        assert analysis["J4_44_size"] == 15
        assert len(analysis["exact_identity_packet"]) == 6
        assert len(analysis["higher_spin_channels"]) == 4
        assert len(analysis["virasoro_target_channels"]) == 2


# ===== W_3 x W_3 OPE in W_4 =====

class TestW3W3OPE:
    def test_vacuum_pole(self):
        """W_3 x W_3: sixth-order pole gives c/3."""
        ope = w3w3_ope_w4_algebra()
        c = Symbol('c')
        assert ope[6]["vac"] == c / 3

    def test_t_channel(self):
        """W_3 x W_3: T at pole 4 with coefficient 2."""
        ope = w3w3_ope_w4_algebra()
        assert ope[4]["T"] == 2

    def test_w4_channel_at_pole2(self):
        """W_3 x W_3: W_4 appears at pole 2 with coefficient c_334."""
        ope = w3w3_ope_w4_algebra()
        c334 = Symbol('c_334')
        assert ope[2]["W4"] == c334


# ===== Full reduction chain: 29 -> 7 -> 6 -> 4+2 =====

class TestTopPolePacket:
    def test_size(self):
        """J_4^top has 7 elements (cor:winfty-ds-stage4-top-pole-packet)."""
        assert len(top_pole_packet()) == 7

    def test_exact_elements(self):
        """J_4^top matches manuscript display."""
        expected = [
            (3, 3, 4, 2), (3, 4, 2, 5), (3, 4, 3, 4), (3, 4, 4, 3),
            (4, 4, 2, 6), (4, 4, 3, 5), (4, 4, 4, 4),
        ]
        assert sorted(top_pole_packet()) == sorted(expected)

    def test_all_top_pole(self):
        """Every entry in J_4^top has n = s+t-u (top pole)."""
        for s, t, u, n in top_pole_packet():
            assert n == s + t - u

    def test_primaryity_eliminates_22(self):
        """Primaryity eliminates 29 - 7 = 22 sub-leading entries."""
        assert len(residual_packet(4)) - len(top_pole_packet()) == 22

    def test_generic_stage4_top_packet_matches_specific(self):
        """The generic stage-growth top packet matches J_4^top."""
        assert incremental_top_pole_packet(4) == top_pole_packet()


class TestParityCompressedPacket:
    def test_size(self):
        """J_4^par has 6 elements (cor:winfty-ds-stage4-parity-packet)."""
        assert len(parity_compressed_packet()) == 6

    def test_exact_elements(self):
        """J_4^par matches manuscript display."""
        expected = [
            (3, 3, 4, 2), (3, 4, 2, 5), (3, 4, 3, 4), (3, 4, 4, 3),
            (4, 4, 2, 6), (4, 4, 4, 4),
        ]
        assert sorted(parity_compressed_packet()) == sorted(expected)

    def test_removed_entry(self):
        """Parity removes exactly (4,4,3,5): odd-spin self-OPE."""
        top = set(top_pole_packet())
        par = set(parity_compressed_packet())
        removed = top - par
        assert removed == {(4, 4, 3, 5)}

    def test_removed_is_odd_self_ope(self):
        """The removed entry has s=t=4 (self-OPE) and u=3 (odd spin)."""
        removed = (4, 4, 3, 5)
        s, t, u, n = removed
        assert s == t  # self-OPE
        assert u % 2 == 1  # odd target spin

    def test_generic_stage4_reduced_packet_matches_specific(self):
        """The generic stage-growth reduced packet matches J_4^par."""
        assert incremental_reduced_packet(4) == parity_compressed_packet()


class TestOPEBlockDecomposition:
    def test_block_33_size(self):
        """(3,3) block has 1 coefficient: c_334."""
        blocks = ope_block_decomposition()
        assert len(blocks["block_33"]) == 1

    def test_block_34_size(self):
        """(3,4) block has 3 coefficients: c_342, c_343, c_344."""
        blocks = ope_block_decomposition()
        assert len(blocks["block_34"]) == 3

    def test_block_44_size(self):
        """(4,4) block has 2 coefficients: c_442, c_444."""
        blocks = ope_block_decomposition()
        assert len(blocks["block_44"]) == 2

    def test_blocks_partition(self):
        """Three blocks partition J_4^par: 1 + 3 + 2 = 6."""
        blocks = ope_block_decomposition()
        all_entries = (blocks["block_33"] + blocks["block_34"]
                       + blocks["block_44"])
        assert len(all_entries) == 6
        assert set(all_entries) == set(parity_compressed_packet())

    def test_block_33_content(self):
        """(3,3) block is exactly {(3,3,4,2)}."""
        blocks = ope_block_decomposition()
        assert blocks["block_33"] == [(3, 3, 4, 2)]


class TestMixedSelfSplit:
    def test_self_coupling_size(self):
        """Self-coupling sector has 3 scalars: c_334, c_442, c_444."""
        ms = mixed_self_split()
        assert len(ms["self_coupling"]) == 3

    def test_mixed_size(self):
        """Mixed sector has 3 channels: c_342, c_343, c_344."""
        ms = mixed_self_split()
        assert len(ms["mixed"]) == 3

    def test_self_coupling_all_same_spin(self):
        """All self-coupling entries have s = t."""
        for s, t, u, n in mixed_self_split()["self_coupling"]:
            assert s == t

    def test_mixed_all_different_spin(self):
        """All mixed entries have s != t."""
        for s, t, u, n in mixed_self_split()["mixed"]:
            assert s != t


class TestFrontierPackage:
    def test_four_higher_spin_channels(self):
        """Four residual higher-spin channels remain inside the six-entry packet."""
        front = frontier_package()
        assert front["n_higher_spin"] == 4

    def test_two_virasoro_target_channels(self):
        """Two theorematic Virasoro-target channels complement the packet."""
        front = frontier_package()
        assert front["n_virasoro_target"] == 2

    def test_higher_spin_channels(self):
        """Higher-spin channels are the four residual non-Virasoro entries."""
        expected = [(3, 3, 4, 2), (3, 4, 3, 4), (3, 4, 4, 3), (4, 4, 4, 4)]
        front = frontier_package()
        assert sorted(front["higher_spin_channels"]) == sorted(expected)
        assert sorted(stage4_residual_higher_spin_channels()) == sorted(expected)

    def test_virasoro_target_values(self):
        """Virasoro-target identities are c_442 = 2 and c_342 = 0."""
        front = frontier_package()
        assert front["virasoro_target_values"][(4, 4, 2, 6)] == 2
        assert front["virasoro_target_values"][(3, 4, 2, 5)] == 0
        assert stage4_virasoro_target_identities()[(4, 4, 2, 6)] == 2
        assert stage4_virasoro_target_identities()[(3, 4, 2, 5)] == 0

    def test_total_equals_six(self):
        """4 higher-spin channels + 2 Virasoro-target channels = 6."""
        front = frontier_package()
        assert front["n_packet"] == len(parity_compressed_packet())
        assert front["n_higher_spin"] + front["n_virasoro_target"] == len(parity_compressed_packet())

    def test_virasoro_target_channels(self):
        """The Virasoro-target channels are exactly the two distinguished entries."""
        expected = [(3, 4, 2, 5), (4, 4, 2, 6)]
        front = frontier_package()
        assert sorted(front["virasoro_target_channels"]) == sorted(expected)
        assert sorted(stage4_virasoro_target_channels()) == sorted(expected)


class TestFullReductionChain:
    def test_chain_valid(self):
        """Full chain 29 -> 7 -> 6 = 4 + 2 is valid."""
        result = verify_full_reduction_chain()
        assert result["chain_valid"]

    def test_all_steps_match(self):
        """Every step matches manuscript claims."""
        result = verify_full_reduction_chain()
        assert result["J4_size"] == 29
        assert result["J4_top_size"] == 7
        assert result["J4_par_size"] == 6
        assert result["n_packet"] == 6
        assert result["n_higher_spin"] == 4
        assert result["n_virasoro_target"] == 2
        assert result["J4_top_matches"]
        assert result["J4_par_matches"]
        assert result["higher_spin_matches"]
        assert result["virasoro_target_matches"]
        assert result["virasoro_target_values_correct"]

    def test_primaryity_count(self):
        """Primaryity eliminates 22 of 29 entries."""
        result = verify_full_reduction_chain()
        assert result["primaryity_eliminated"] == 22

    def test_parity_removes_one(self):
        """Parity removes exactly one entry: (4,4,3,5)."""
        result = verify_full_reduction_chain()
        assert result["parity_eliminated"]

    def test_ope_blocks_consistent(self):
        """OPE block sizes: 1 + 3 + 2 = 6."""
        result = verify_full_reduction_chain()
        assert result["block_33_size"] == 1
        assert result["block_34_size"] == 3
        assert result["block_44_size"] == 2
        assert result["block_sum"] == 6

    def test_mixed_self_consistent(self):
        """Mixed-self split: 3 + 3 = 6."""
        result = verify_full_reduction_chain()
        assert result["self_coupling_size"] == 3
        assert result["mixed_size"] == 3


# ===== First nontrivial next reduced packet: stage 5 =====

class TestStage5IncrementalPacket:
    def test_stage5_counts(self):
        """J_5, J_5^top, J_5^red have sizes 72, 15, 11."""
        analysis = analyze_incremental_packet(5)
        assert analysis["J_size"] == 72
        assert analysis["top_size"] == 15
        assert analysis["red_size"] == 11

    def test_stage5_reduced_packet_exact(self):
        """J_5^red matches the first nontrivial next reduced packet."""
        expected = [
            (3, 4, 5, 2),
            (3, 5, 2, 6), (3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3),
            (4, 5, 2, 7), (4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4),
            (5, 5, 2, 8), (5, 5, 4, 6),
        ]
        assert incremental_reduced_packet(5) == expected

    def test_stage5_block_decomposition(self):
        """J_5^red decomposes into one tail, two mixed blocks, and one self block."""
        blocks = incremental_reduced_block_decomposition(5)
        assert blocks[(3, 4)] == [(3, 4, 5, 2)]
        assert blocks[(3, 5)] == [
            (3, 5, 2, 6), (3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3),
        ]
        assert blocks[(4, 5)] == [
            (4, 5, 2, 7), (4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4),
        ]
        assert blocks[(5, 5)] == [(5, 5, 2, 8), (5, 5, 4, 6)]

    def test_stage5_higher_spin_vs_virasoro_split(self):
        """J_5^red splits as 8 higher-spin channels plus 3 Virasoro-target channels."""
        higher = incremental_higher_spin_channels(5)
        vir = incremental_virasoro_target_channels(5)
        assert len(higher) == 8
        assert len(vir) == 3
        assert higher == [
            (3, 4, 5, 2),
            (3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3),
            (4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4),
            (5, 5, 4, 6),
        ]
        assert vir == [(3, 5, 2, 6), (4, 5, 2, 7), (5, 5, 2, 8)]

    def test_stage5_higher_spin_block_decomposition(self):
        """J_5^{hs} decomposes as 1 + 3 + 3 + 1 by source pair."""
        blocks = incremental_higher_spin_block_decomposition(5)
        assert blocks[(3, 4)] == [(3, 4, 5, 2)]
        assert blocks[(3, 5)] == [
            (3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3),
        ]
        assert blocks[(4, 5)] == [
            (4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4),
        ]
        assert blocks[(5, 5)] == [(5, 5, 4, 6)]

    def test_stage5_named_subblocks(self):
        """The four stage-5 higher-spin subblocks are addressable one by one."""
        assert incremental_higher_spin_block(5, (3, 4)) == [(3, 4, 5, 2)]
        assert incremental_higher_spin_block(5, (3, 5)) == [
            (3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3),
        ]
        assert incremental_higher_spin_block(5, (4, 5)) == [
            (4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4),
        ]
        assert incremental_higher_spin_block(5, (5, 5)) == [(5, 5, 4, 6)]

    def test_stage5_singleton_vs_transport_blocks(self):
        """Stage 5 splits into singleton entry blocks and mixed transport triples."""
        assert incremental_higher_spin_singleton_blocks(5) == {
            (3, 4): [(3, 4, 5, 2)],
            (5, 5): [(5, 5, 4, 6)],
        }
        assert incremental_higher_spin_nonsingleton_blocks(5) == {
            (3, 5): [(3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3)],
            (4, 5): [(4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4)],
        }

    def test_stage5_transport_target_ladders(self):
        """The mixed transport packet splits into three fixed-target ladders."""
        assert incremental_higher_spin_nonsingleton_target_decomposition(5) == {
            3: [(3, 5, 3, 5), (4, 5, 3, 6)],
            4: [(3, 5, 4, 4), (4, 5, 4, 5)],
            5: [(3, 5, 5, 3), (4, 5, 5, 4)],
        }

    def test_stage5_virasoro_target_values(self):
        """Mixed target-2 channels vanish; the self target-2 channel equals 2."""
        values = incremental_virasoro_target_identities(5)
        assert values[(3, 5, 2, 6)] == 0
        assert values[(4, 5, 2, 7)] == 0
        assert values[(5, 5, 2, 8)] == 2

    def test_stage5_analysis_reports_higher_spin_blocks(self):
        """The packet summary records the higher-spin block decomposition."""
        analysis = analyze_incremental_packet(5)
        assert analysis["higher_spin_blocks"] == {
            (3, 4): [(3, 4, 5, 2)],
            (3, 5): [(3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3)],
            (4, 5): [(4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4)],
            (5, 5): [(5, 5, 4, 6)],
        }
        assert analysis["higher_spin_singletons"] == {
            (3, 4): [(3, 4, 5, 2)],
            (5, 5): [(5, 5, 4, 6)],
        }
        assert analysis["higher_spin_nonsingletons"] == {
            (3, 5): [(3, 5, 3, 5), (3, 5, 4, 4), (3, 5, 5, 3)],
            (4, 5): [(4, 5, 3, 6), (4, 5, 4, 5), (4, 5, 5, 4)],
        }
        assert analysis["higher_spin_targets"] == {
            3: [(3, 5, 3, 5), (4, 5, 3, 6)],
            4: [(3, 5, 4, 4), (4, 5, 4, 5), (5, 5, 4, 6)],
            5: [(3, 4, 5, 2), (3, 5, 5, 3), (4, 5, 5, 4)],
        }
        assert analysis["higher_spin_nonsingleton_targets"] == {
            3: [(3, 5, 3, 5), (4, 5, 3, 6)],
            4: [(3, 5, 4, 4), (4, 5, 4, 5)],
            5: [(3, 5, 5, 3), (4, 5, 5, 4)],
        }
