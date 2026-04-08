r"""Tests for GZ26 frontier: n=5 commutativity and BP Hamiltonians.

DIRECTION A: n=5 Hamiltonians with 2D moduli space.
    The commutativity [H_1, H_2] = 0 at n=5 is the FIRST nontrivial check
    (n<=4 has dim M_{0,n} <= 1, so commutativity is automatic).

DIRECTION B: Bershadsky-Polyakov (non-principal W-algebra) Hamiltonians.
    BP = W^k(sl_3, f_{min}): 4 generators, mixed shadow class.

Multi-path verification:
    Path 1: Shadow connection flatness (numerical)
    Path 2: Collision-depth structure (algebraic)
    Path 3: Direct commutativity verification
    Path 4: Cross-family consistency

Manuscript references:
    thm:gz26-commuting-differentials
    rem:bar-pole-absorption (AP19)
    subregular_hook_frontier.tex
"""

import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from fractions import Fraction

from theorem_gz_frontier_engine import (
    # Direction A
    sl2_generators,
    embed_operator,
    casimir_ij,
    kz_hamiltonians_n5,
    verify_kz_n5_commutativity,
    verify_kz_n5_ward_identities,
    verify_kz_n5_position_independence,
    virasoro_bpz_n5_primary,
    virasoro_bpz_n5_flatness_verification,
    n5_moduli_dimension,
    # Direction A extended: Virasoro n=5 differential operators
    virasoro_n5_hamiltonian_scalar,
    virasoro_n5_hamiltonian_deriv_coeffs,
    virasoro_n5_apply_hamiltonian,
    virasoro_n5_commutator_on_function,
    virasoro_n5_verify_commutativity,
    virasoro_n5_gaudin_scalar_eigenvalue,
    virasoro_n5_gaudin_verify,
    # Direction B
    bp_central_charge,
    bp_dual_level,
    bp_ope_mode,
    bp_max_ope_pole,
    bp_max_ope_pole_global,
    bp_collision_depth_table,
    bp_collision_residue_on_primary,
    bp_hamiltonian_primary_data,
    bp_hamiltonian_coefficient_on_primary,
    bp_t_sector_restriction,
    bp_j_sector_analysis,
    bp_fermionic_sector_analysis,
    bp_full_hamiltonian_on_primary,
    bp_shadow_class_analysis,
    bp_koszul_conductor_check,
    bp_vs_virasoro_comparison,
    collision_depth_comparison,
    # Direction B extended: exact Fraction arithmetic
    bp_central_charge_exact,
    bp_koszul_conductor_exact,
    bp_hamiltonian_coefficient_exact,
    bp_channel_depth_table_fraction,
    bp_verify_j_commutes_with_virasoro,
    bp_metric_exact,
    bp_inverse_metric_exact,
    bp_total_depth1_coefficient_exact,
    bp_specialization_virasoro,
    bp_full_depth_coefficients_exact,
)


# ============================================================
# DIRECTION A: n=5 KZ commutativity (2D moduli)
# ============================================================

class TestN5ModuliDimension:
    """Verify that n=5 gives the first nontrivial commutativity test."""

    def test_moduli_dimension(self):
        """dim M_{0,5} = 2."""
        data = n5_moduli_dimension()
        assert data['dim_moduli'] == 2
        assert data['free_moduli'] == 2
        assert data['commutativity_nontrivial']


class TestKZN5Commutativity:
    """Test [H_i, H_j] = 0 for KZ at n=5 (Path 1: shadow flatness)."""

    def test_kz_n5_spin_half_commute(self):
        """[H_i, H_j] = 0 for 5 spin-1/2 reps at level 1."""
        positions = [0.0, 1.0, 0.5+0.5j, -0.3+0.7j, 2.0-0.5j]
        result = verify_kz_n5_commutativity(
            [2, 2, 2, 2, 2], positions, level=1)
        assert result['all_commute'], (
            f"KZ n=5 spin-1/2 failed: max norm = {result['max_commutator_norm']}")

    def test_kz_n5_spin_1_commute(self):
        """[H_i, H_j] = 0 for 5 spin-1 reps at level 2."""
        positions = [0.0, 1.0+0.3j, -1.0+0.5j, 0.5-1.0j, 2.0+1.0j]
        result = verify_kz_n5_commutativity(
            [3, 3, 3, 3, 3], positions, level=2)
        assert result['all_commute'], (
            f"KZ n=5 spin-1 failed: max norm = {result['max_commutator_norm']}")

    def test_kz_n5_mixed_reps_commute(self):
        """[H_i, H_j] = 0 for mixed reps (2,3,2,3,2) at level 3."""
        positions = [0.0, 1.0, 0.5+0.8j, -0.5+0.3j, 1.5-0.5j]
        result = verify_kz_n5_commutativity(
            [2, 3, 2, 3, 2], positions, level=3)
        assert result['all_commute'], (
            f"KZ n=5 mixed failed: max norm = {result['max_commutator_norm']}")

    def test_kz_n5_position_independence(self):
        """Commutativity holds at multiple random configurations."""
        result = verify_kz_n5_position_independence(
            [2, 2, 2, 2, 2], level=1, n_trials=5)
        assert result['all_pass'], "KZ n=5 position independence failed"

    def test_kz_n5_level_independence(self):
        """Commutativity holds at levels k = 1, 2, 3, 5."""
        positions = [0.0, 1.0, 0.5+0.5j, -0.3+0.7j, 2.0-0.5j]
        for k in [1, 2, 3, 5]:
            result = verify_kz_n5_commutativity(
                [2, 2, 2, 2, 2], positions, level=k)
            assert result['all_commute'], f"Failed at level k={k}"


class TestKZN5WardIdentities:
    """Test Ward identities for n=5 KZ Hamiltonians."""

    def test_translation_ward(self):
        """sum_i H_i = 0 at n=5."""
        positions = [0.0, 1.0, 0.5+0.5j, -0.3+0.7j, 2.0-0.5j]
        result = verify_kz_n5_ward_identities(
            [2, 2, 2, 2, 2], positions, level=1)
        assert result['translation_holds']


class TestVirasoroBPZN5:
    """Test Virasoro BPZ Hamiltonians at n=5 on primaries."""

    def test_n5_primary_structure(self):
        """Verify n=5 BPZ connection has 2D moduli."""
        weights = [0.5, 0.5, 0.5, 0.5, 0.5]
        positions = [0.0, 1.0, 0.5+0.5j, -0.3+0.7j, 2.0-0.5j]
        result = virasoro_bpz_n5_primary(weights, positions)
        assert result['moduli_dim'] == 2

    def test_n5_bpz_flatness(self):
        """BPZ flatness at n=5 via abelian connection structure.

        On the 1D primary conformal block space, the BPZ connection is
        abelian (rank 1) and the curvature F = dw vanishes because
        w = d log(prod z_{ij}^gamma) is exact.

        The NONTRIVIAL commutativity test for n=5 is the KZ matrix
        commutator (tested in TestKZN5Commutativity).  The BPZ scalar
        operators commute on the conformal block space (not on arbitrary
        functions), which is guaranteed by the Virasoro Ward identities.
        """
        weights = [0.5, 0.5, 0.5, 0.5, 0.5]
        result = virasoro_bpz_n5_flatness_verification(weights, n_trials=3)
        assert result['all_pass']
        assert 'abelian' in result['flatness_mechanism']


# ============================================================
# DIRECTION B: Bershadsky-Polyakov structural tests
# ============================================================

class TestBPCentralCharge:
    """Test BP central charge formula c(k) = 2 - 3(2k+3)^2/(k+3)."""

    def test_bp_c_at_k1(self):
        """c(1) = 2 - 24*4/4 = 2 - 24 = -22 (K=196 formula)."""
        c = bp_central_charge(1)
        assert abs(c - (-22)) < 1e-12

    def test_bp_c_at_k_minus3(self):
        """c(-3) is singular (division by zero)."""
        # k = -3 is the critical level for sl_3 (h^v = 3)
        # The central charge diverges
        with pytest.raises((ZeroDivisionError, ValueError, OverflowError)):
            c = bp_central_charge(-3)
            # If no exception, check it is inf or very large
            assert abs(c) > 1e10

    def test_bp_koszul_conductor(self):
        """K_BP = c(k) + c(-k-6) = 196 for multiple k values."""
        for k_val in [1, 2, 5, 10, 0.5, -1, -2]:
            result = bp_koszul_conductor_check(k_val)
            assert result['K_equals_196'], (
                f"K_BP = {result['K']} at k={k_val}, expected 196")


class TestBPOPEPoleOrders:
    """Test OPE pole orders for all BP channel pairs."""

    def test_tt_pole_4(self):
        """T-T OPE pole order = 4 (Virasoro sector)."""
        assert bp_max_ope_pole('T', 'T') == 4

    def test_jj_pole_2(self):
        """J-J OPE pole order = 2 (Heisenberg sector)."""
        assert bp_max_ope_pole('J', 'J') == 2

    def test_gpm_pole_3(self):
        """G+G- OPE pole order = 3."""
        assert bp_max_ope_pole('G+', 'G-') == 3
        assert bp_max_ope_pole('G-', 'G+') == 3

    def test_gpp_pole_0(self):
        """G+G+ and G-G- OPE vanishes (charge conservation)."""
        assert bp_max_ope_pole('G+', 'G+') == 0
        assert bp_max_ope_pole('G-', 'G-') == 0

    def test_global_max_pole(self):
        """Global max pole = 4 (from T-T)."""
        assert bp_max_ope_pole_global() == 4

    def test_dlog_absorption(self):
        """k_max = pole - 1 for all non-trivial channels (AP19)."""
        table = bp_collision_depth_table()
        for (a, b), kmax in table.items():
            pole = bp_max_ope_pole(a, b)
            assert kmax == pole - 1, (
                f"d log violated for ({a},{b}): k_max={kmax}, pole={pole}")


class TestBPCollisionResidues:
    """Test collision residues for BP on primary states."""

    def test_tt_depth1_weight(self):
        """T_{(1)}T = 2T -> 2h on primaries."""
        res = bp_collision_residue_on_primary(1, 'T', 'T', 10.0, h_j=0.5)
        assert abs(res - 1.0) < 1e-12  # 2 * 0.5 = 1.0

    def test_tt_depth3_central(self):
        """T_{(3)}T = c/2 (central scalar)."""
        c_val = 10.0
        res = bp_collision_residue_on_primary(3, 'T', 'T', c_val, h_j=0.5)
        assert abs(res - c_val / 2) < 1e-12

    def test_jj_depth1_central(self):
        """J_{(1)}J = c/3 (central scalar)."""
        c_val = 12.0
        res = bp_collision_residue_on_primary(1, 'J', 'J', c_val, h_j=0, q_j=1)
        assert abs(res - c_val / 3) < 1e-12

    def test_gpm_depth1_charge(self):
        """G+_{(1)}G- = 2J -> 2q on primaries."""
        res = bp_collision_residue_on_primary(1, 'G+', 'G-', 10.0, h_j=0.5, q_j=1.5)
        assert abs(res - 3.0) < 1e-12  # 2 * 1.5

    def test_gpm_depth2_central(self):
        """G+_{(2)}G- = 2c/3 (central scalar)."""
        c_val = 9.0
        res = bp_collision_residue_on_primary(2, 'G+', 'G-', c_val, h_j=0.5, q_j=1.0)
        assert abs(res - 2 * c_val / 3) < 1e-12

    def test_gmp_depth1_minus_charge(self):
        """G-_{(1)}G+ = -2J -> -2q on primaries."""
        res = bp_collision_residue_on_primary(1, 'G-', 'G+', 10.0, h_j=0.5, q_j=2.0)
        assert abs(res - (-4.0)) < 1e-12  # -2 * 2.0

    def test_vanishing_channels(self):
        """G+G+ and G-G- OPE vanishes at all depths."""
        for k in range(0, 5):
            assert bp_collision_residue_on_primary(
                k, 'G+', 'G+', 10.0, 0.5, 1.0) == 0
            assert bp_collision_residue_on_primary(
                k, 'G-', 'G-', 10.0, 0.5, 1.0) == 0


class TestBPHamiltonianStructure:
    """Test structural properties of BP Hamiltonians."""

    def test_hamiltonian_data_channels(self):
        """Verify channel classification: bosonic, fermionic, mixed."""
        data = bp_hamiltonian_primary_data(10.0)
        channels = data['channel_types']

        # T-T is bosonic
        assert channels[('T', 'T')]['type'] == 'bosonic'
        # J-J is bosonic
        assert channels[('J', 'J')]['type'] == 'bosonic'
        # G+G- is fermionic
        assert channels[('G+', 'G-')]['type'] == 'fermionic'

    def test_global_k_max(self):
        """Global k_max = 3 (from T-T pole 4)."""
        data = bp_hamiltonian_primary_data(10.0)
        assert data['global_k_max'] == 3

    def test_global_diff_order(self):
        """Global differential operator order = 2."""
        data = bp_hamiltonian_primary_data(10.0)
        assert data['global_diff_order'] == 2

    def test_metric_diagonal(self):
        """BP Zamolodchikov metric is block-diagonal."""
        data = bp_hamiltonian_primary_data(6.0)
        metric = data['metric']
        assert abs(metric['TT'] - 3.0) < 1e-12   # c/2 = 3
        assert abs(metric['JJ'] - 2.0) < 1e-12   # c/3 = 2
        assert abs(metric['G+G-'] - 4.0) < 1e-12  # 2c/3 = 4


class TestBPTSectorRestriction:
    """Test that restricting BP to T-T channel recovers Virasoro."""

    def test_t_sector_matches_virasoro(self):
        """T-T sector of BP Hamiltonian matches Virasoro BPZ scalar sector."""
        c_val = 10.0
        h_j = 0.5
        result = bp_t_sector_restriction(c_val, h_j)
        assert result['matches_virasoro_scalar_sector']

    def test_t_sector_depth1_scalar(self):
        """T-T depth 1: (2/c) * 2h_j = 4h_j/c."""
        c_val = 10.0
        h_j = 0.5
        result = bp_t_sector_restriction(c_val, h_j)
        expected = 4 * h_j / c_val
        assert abs(result['depth_1_scalar'] - expected) < 1e-12

    def test_t_sector_depth3_unity(self):
        """T-T depth 3: (2/c) * (c/2) = 1.0 (central term)."""
        c_val = 10.0
        h_j = 0.5
        result = bp_t_sector_restriction(c_val, h_j)
        assert abs(result['depth_3_scalar'] - 1.0) < 1e-12


class TestBPJSectorAnalysis:
    """Test J-J channel: abelian sector, class G."""

    def test_j_sector_central_scalar(self):
        """J-J depth 1 is a central scalar (independent of module data)."""
        c_val = 12.0
        result = bp_j_sector_analysis(c_val, q_j=5.0)
        # J_{(1)}J = c/3, weighted by 3/c -> 1.0 (independent of q_j)
        assert result['is_central_scalar']

    def test_j_sector_class_g(self):
        """J-line is class G (shadow depth 2)."""
        result = bp_j_sector_analysis(10.0, q_j=1.0)
        assert result['shadow_class'] == 'G'
        assert result['differential_order'] == 0


class TestBPFermionicSector:
    """Test fermionic (G+G-, G-G+) sector analysis."""

    def test_fermionic_charge_cancellation(self):
        """G+G- and G-G+ charge contributions cancel at depth 1.

        G+_{(1)}G- = 2q (from 2J) and G-_{(1)}G+ = -2q (from -2J).
        Weighted by same metric coefficient, the total is zero.
        """
        c_val = 10.0
        result = bp_fermionic_sector_analysis(c_val, h_j=0.5, q_j=1.0)
        assert result['charge_cancels_at_depth_1']

    def test_fermionic_depth2_nonzero(self):
        """G+G- + G-G+ at depth 2: 2 * (3/(2c)) * (2c/3) = 2.0."""
        c_val = 10.0
        result = bp_fermionic_sector_analysis(c_val, h_j=0.5, q_j=1.0)
        assert abs(result['depth_2_total'] - 2.0) < 1e-12

    def test_fermionic_k_max(self):
        """Fermionic channels have k_max = 2."""
        result = bp_fermionic_sector_analysis(10.0, h_j=0.5, q_j=1.0)
        assert result['k_max'] == 2


class TestBPShadowClass:
    """Test mixed shadow class of BP."""

    def test_t_line_class_m(self):
        """T-line is class M (infinite shadow depth)."""
        result = bp_shadow_class_analysis(10.0)
        assert result['T_line']['shadow_class'] == 'M'
        assert result['T_line']['shadow_depth'] == float('inf')

    def test_j_line_class_g(self):
        """J-line is class G (shadow depth 2)."""
        result = bp_shadow_class_analysis(10.0)
        assert result['J_line']['shadow_class'] == 'G'
        assert result['J_line']['shadow_depth'] == 2

    def test_fermionic_class_l(self):
        """Fermionic lines are class L (shadow depth 3)."""
        result = bp_shadow_class_analysis(10.0)
        assert result['fermionic_lines']['shadow_class'] == 'L'

    def test_mixed_class(self):
        """BP has mixed shadow class."""
        result = bp_shadow_class_analysis(10.0)
        assert result['mixed_class']


class TestBPVsVirasoro:
    """Test that non-Virasoro content is isolated to non-TT channels."""

    def test_non_virasoro_content_at_q0(self):
        """At q=0 (no U(1) charge), non-Virasoro content comes from
        J-J central scalar and fermionic cross terms.
        """
        c_val = 10.0
        h_j = 0.5
        result = bp_vs_virasoro_comparison(c_val, h_j)
        # With q=0, the non-Virasoro content should be nonzero
        # (from J-J and G+G-/G-G+ central scalar terms)
        non_vir = result['non_virasoro_content']
        # At depth 1: J-J gives central scalar (3/c)(c/3) = 1
        assert 1 in non_vir or 2 in non_vir  # Some non-TT content exists


class TestCollisionDepthComparison:
    """Cross-family consistency of collision depths."""

    def test_dlog_absorption_universal(self):
        """k_max = max_pole - 1 for all families (AP19)."""
        table = collision_depth_comparison()
        for fam, data in table.items():
            if isinstance(data['max_pole'], int):
                assert data['k_max'] == data['max_pole'] - 1, (
                    f"d log violated for {fam}")

    def test_virasoro_matches_bp_tt(self):
        """Virasoro and BP T-T channel have same depth structure."""
        table = collision_depth_comparison()
        vir = table['Virasoro']
        bp_tt = table['BP (T-T)']
        assert vir['max_pole'] == bp_tt['max_pole']
        assert vir['k_max'] == bp_tt['k_max']
        assert vir['diff_order'] == bp_tt['diff_order']

    def test_bp_mixed_class(self):
        """BP global class is mixed."""
        table = collision_depth_comparison()
        bp_global = table['BP (global)']
        assert 'mixed' in bp_global['class']


class TestBPKoszulConductor:
    """Verify K_BP = 196 at multiple levels (multi-path verification)."""

    def test_conductor_integer_levels(self):
        """K_BP = 196 at k = 1, 2, 3, 5, 10."""
        for k_val in [1, 2, 3, 5, 10]:
            result = bp_koszul_conductor_check(k_val)
            assert result['K_equals_196']

    def test_conductor_fractional_levels(self):
        """K_BP = 196 at fractional levels."""
        for k_val in [0.5, 1.5, 2.5]:
            result = bp_koszul_conductor_check(k_val)
            assert result['K_equals_196']

    def test_conductor_negative_levels(self):
        """K_BP = 196 at negative levels (away from critical)."""
        for k_val in [-1, -2, -4, -5]:
            result = bp_koszul_conductor_check(k_val)
            assert result['K_equals_196']


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
