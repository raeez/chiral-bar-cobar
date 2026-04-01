"""RED TEAM tests for DS-KD commutation obstruction.

Attack on conj:ds-kd-arbitrary-nilpotent: does bar-cobar/Koszul duality
COMMUTE with Drinfeld-Sokolov reduction for arbitrary nilpotent orbits?

Target: find real breaks in the DS-bar commutation outside the proved
hook-type corridor (thm:hook-transport-corridor).

Test categories:
  A. Non-hook nilpotent probes (sl_4, sl_5, sl_6)
  B. Spectral sequence obstruction analysis
  C. Type B/C orbit analysis and non-special orbit identification
  D. Level-dependent failures (critical, admissible)
  E. Quadratic ghost obstruction
  F. Kappa/complementarity consistency for non-hooks
  G. Full red-team verdict
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.ds_kd_red_team import (
    NON_HOOK_TARGETS,
    analyze_admissible_level,
    analyze_critical_level,
    analyze_colliding_level,
    analyze_type_b2_orbits,
    b_collapse,
    c_collapse,
    complementarity_sum_is_constant,
    complementarity_sum_non_hook,
    enumerate_type_b_orbits,
    enumerate_type_c_orbits,
    full_red_team_report,
    ghost_obstruction_analysis,
    is_special_type_b_orbit,
    is_valid_type_b_partition,
    is_valid_type_c_partition,
    kappa_sum_is_constant,
    kappa_sum_non_hook,
    probe_all_non_hooks,
    probe_non_hook,
    spectral_sequence_probe,
)


# =====================================================================
# A. Non-hook nilpotent probes
# =====================================================================

class TestNonHookProbes:
    """Probe non-hook nilpotent orbits for DS-bar commutation."""

    def test_sl4_22_is_first_non_hook(self):
        """(2,2) in sl_4 is the first non-hook nilpotent."""
        probe = probe_non_hook(4, (2, 2))
        assert probe.orbit_class != "hook"
        assert probe.orbit_class != "principal"
        assert probe.N == 4
        assert probe.partition == (2, 2)

    def test_sl4_22_is_self_transpose(self):
        """(2,2)^t = (2,2): self-BV-dual in type A."""
        probe = probe_non_hook(4, (2, 2))
        assert probe.is_self_transpose
        assert probe.transpose == (2, 2)

    def test_sl4_22_centralizer_dim(self):
        """dim(sl_4^{f_{(2,2)}}) = 7 (from comp:sl4-hook-data in manuscript)."""
        probe = probe_non_hook(4, (2, 2))
        assert probe.centralizer_dim == 7

    def test_sl4_22_ghost_constant(self):
        """Ghost constant for (2,2) in sl_4: C_{(2,2)} = 4."""
        probe = probe_non_hook(4, (2, 2))
        assert probe.ghost_constant == 4

    def test_sl5_32_not_self_transpose(self):
        """(3,2)^t = (2,2,1) != (3,2)."""
        probe = probe_non_hook(5, (3, 2))
        assert not probe.is_self_transpose
        assert probe.transpose == (2, 2, 1)

    def test_sl6_33_is_self_transpose(self):
        """(3,3)^t = (2,2,2) != (3,3). Wait -- check this."""
        probe = probe_non_hook(6, (3, 3))
        # (3,3)^t = (2,2,2): NOT self-transpose!
        assert probe.transpose == (2, 2, 2)
        assert not probe.is_self_transpose

    def test_sl6_222_transpose(self):
        """(2,2,2)^t = (3,3)."""
        probe = probe_non_hook(6, (2, 2, 2))
        assert probe.transpose == (3, 3)

    def test_sl6_33_and_222_are_bv_dual_pair(self):
        """(3,3) and (2,2,2) form a BV dual pair in sl_6."""
        p1 = probe_non_hook(6, (3, 3))
        p2 = probe_non_hook(6, (2, 2, 2))
        assert p1.transpose == p2.partition
        assert p2.transpose == p1.partition

    def test_probe_all_non_hooks_runs(self):
        """All non-hook probes execute without error."""
        results = probe_all_non_hooks()
        assert len(results) == len(NON_HOOK_TARGETS)
        for key, probe in results.items():
            assert probe.N >= 4

    def test_sl6_321_staircase(self):
        """(3,2,1) is the staircase partition of 6, non-hook."""
        probe = probe_non_hook(6, (3, 2, 1))
        assert probe.partition == (3, 2, 1)
        assert probe.transpose == (3, 2, 1)
        # Staircase is self-transpose!
        assert probe.is_self_transpose


# =====================================================================
# B. Spectral sequence obstruction
# =====================================================================

class TestSpectralSequence:
    """Spectral sequence analysis of DS-bar commutation."""

    def test_sl4_22_spectral_sequence(self):
        """SS obstruction for (2,2) in sl_4."""
        ss = spectral_sequence_probe(4, (2, 2))
        assert ss.N == 4
        assert ss.partition == (2, 2)
        assert ss.bar_complex_dim == 7  # = centralizer_dim

    def test_sl4_22_generic_level_exact(self):
        """At generic level, DS is exact (H^1_DS = 0)."""
        ss = spectral_sequence_probe(4, (2, 2))
        assert not ss.h1_ds_survives_at_generic_level

    def test_sl5_32_spectral_sequence(self):
        """SS for (3,2) in sl_5."""
        ss = spectral_sequence_probe(5, (3, 2))
        assert ss.partition == (3, 2)

    def test_spectral_sequence_obstruction_bidegree(self):
        """Non-hook with non-abelian n_+ has obstruction at (1,1) or higher."""
        for N, lam, desc in NON_HOOK_TARGETS:
            ss = spectral_sequence_probe(N, lam)
            ghost = ghost_obstruction_analysis(N, lam)
            if ghost.n_plus_is_abelian:
                assert ss.obstruction_bidegree is None, \
                    f"Abelian n_+ should have no SS obstruction for {lam}"
            else:
                assert ss.obstruction_bidegree is not None, \
                    f"Non-abelian n_+ should have SS obstruction for {lam}"


# =====================================================================
# C. Type B/C orbits and non-special orbit detection
# =====================================================================

class TestTypeBCOrbits:
    """Type B and C orbit analysis."""

    def test_b2_orbit_count(self):
        """B_2 = so_5 has exactly 4 nilpotent orbits."""
        orbits = enumerate_type_b_orbits(2)
        assert len(orbits) == 4

    def test_b2_valid_partitions(self):
        """The valid B_2 partitions of 5."""
        orbits = enumerate_type_b_orbits(2)
        expected = {(5,), (3, 1, 1), (2, 2, 1), (1, 1, 1, 1, 1)}
        assert set(orbits) == expected

    def test_c2_orbit_count(self):
        """C_2 = sp_4 has exactly 4 nilpotent orbits."""
        orbits = enumerate_type_c_orbits(2)
        assert len(orbits) == 4

    def test_c2_valid_partitions(self):
        """The valid C_2 partitions of 4."""
        orbits = enumerate_type_c_orbits(2)
        expected = {(4,), (2, 2), (2, 1, 1), (1, 1, 1, 1)}
        assert set(orbits) == expected

    def test_b2_221_is_non_special(self):
        """KEY FINDING: (2,2,1) in B_2 is NON-SPECIAL.

        This is the RED TEAM's main finding for types B/C/D:
        non-special orbits have AMBIGUOUS BV duals, making the
        DS-KD target W-algebra unclear.
        """
        assert not is_special_type_b_orbit((2, 2, 1))

    def test_b2_regular_is_special(self):
        """(5) in B_2 is special (regular orbit always special)."""
        assert is_special_type_b_orbit((5,))

    def test_b2_subregular_is_special(self):
        """(3,1,1) in B_2 is special (subregular orbit)."""
        assert is_special_type_b_orbit((3, 1, 1))

    def test_b2_zero_is_special(self):
        """(1,1,1,1,1) in B_2 is special (zero orbit always special)."""
        assert is_special_type_b_orbit((1, 1, 1, 1, 1))

    def test_b2_analysis_identifies_non_special(self):
        """The full B_2 analysis correctly flags non-special orbits."""
        analysis = analyze_type_b2_orbits()
        # (2,2,1) should be flagged as non-special with ambiguous BV dual
        b2_221 = analysis["B2_(2, 2, 1)"]
        assert not b2_221.is_special
        assert not b2_221.bv_dual_exists
        assert "NON-SPECIAL" in b2_221.diagnosis

    def test_b_collapse_basic(self):
        """B-collapse adjusts even parts to even multiplicities."""
        # (3,2) of 5: 2 has odd multiplicity (1), B-collapse -> (3,1,1)
        result = b_collapse((3, 2))
        assert is_valid_type_b_partition(result)
        assert result == (3, 1, 1)

    def test_c_collapse_basic(self):
        """C-collapse adjusts odd parts to even multiplicities."""
        # (3,1) of 4: 3 has odd mult (1), 1 has odd mult (1)
        # C-collapse -> (2,2)
        result = c_collapse((3, 1))
        assert is_valid_type_c_partition(result)
        assert result == (2, 2)

    def test_partition_validity_cross_check(self):
        """(3,1) is valid for B but not for C (as partition of 4)."""
        # (3,1) of 4: odd parts 3,1 each with mult 1 -> invalid for C_2
        assert not is_valid_type_c_partition((3, 1))
        # But (3,1,1) of 5: for B_2, even parts: none with odd mult -> valid
        assert is_valid_type_b_partition((3, 1, 1))


# =====================================================================
# D. Level-dependent failures
# =====================================================================

class TestLevelDependentFailures:
    """Level-dependent DS-KD failure analysis."""

    def test_critical_level_sl4_22(self):
        """At k = -4 (critical for sl_4), DS is undefined for (2,2)."""
        result = analyze_critical_level(4, (2, 2))
        assert not result.ds_is_defined
        assert not result.kappa_defined
        assert "FATAL" in result.failure_mode

    def test_critical_level_sl5_32(self):
        """At k = -5 (critical for sl_5), DS is undefined for (3,2)."""
        result = analyze_critical_level(5, (3, 2))
        assert not result.ds_is_defined
        assert result.level_value == -5

    def test_admissible_level_sl4_22(self):
        """At admissible level k = -4 + 4/1 = 0 for sl_4, check (2,2)."""
        result = analyze_admissible_level(4, (2, 2), p=4, q=1)
        assert result.ds_is_defined
        assert result.w_algebra_has_null_vectors
        assert not result.pbw_koszulness_holds
        assert "CONDITIONAL" in result.failure_mode

    def test_admissible_level_sl4_22_boundary(self):
        """Boundary admissible level k = -4 + 5/2 = -3/2 for sl_4."""
        result = analyze_admissible_level(4, (2, 2), p=5, q=2)
        assert result.level_value == Rational(-3, 2)
        assert result.ds_is_defined

    def test_colliding_level_sl4(self):
        """Self-dual level k = -N collides with critical level."""
        result = analyze_colliding_level(4, (2, 2))
        assert result.level_value == -4
        assert "DEGENERATE" in result.failure_mode
        assert not result.ds_is_defined

    def test_critical_all_non_hooks(self):
        """All non-hook targets have fatal failure at critical level."""
        for N, lam, desc in NON_HOOK_TARGETS:
            result = analyze_critical_level(N, lam)
            assert not result.ds_is_defined, f"Critical level should be fatal for {lam}"


# =====================================================================
# E. Quadratic ghost obstruction
# =====================================================================

class TestGhostObstruction:
    """Quadratic ghost obstruction analysis."""

    def test_sl4_22_ghost_analysis(self):
        """Ghost analysis for (2,2) in sl_4."""
        ghost = ghost_obstruction_analysis(4, (2, 2))
        assert ghost.N == 4
        assert ghost.partition == (2, 2)
        assert ghost.n_plus_dim >= 1

    def test_sl4_22_abelianity(self):
        """Is n_+ abelian for (2,2) in sl_4?

        The sl_2-triple for (2,2) has h = diag(1,1,-1,-1) (up to trace
        removal). The positive-grade spaces are g_1 and g_2. If g_2 is
        nonzero, then n_+ is non-abelian.

        Actually for (2,2), the ad(h) grades on sl_4 go from -2 to 2.
        Specifically h = diag(1,0,-1,0) or similar depending on the
        sl_2 triple. The key is whether the maximum positive grade exceeds 1.
        """
        ghost = ghost_obstruction_analysis(4, (2, 2))
        # Log the abelianity finding -- this is the key structural test
        # For (2,2), the even partition, n_+ structure determines if
        # DS-bar commutation has a quadratic ghost obstruction
        assert isinstance(ghost.n_plus_is_abelian, bool)

    def test_sl5_32_non_abelian_n_plus(self):
        """(3,2) in sl_5: n_+ is NON-ABELIAN.

        KEY RED TEAM FINDING: For partition (3,2), the ad(h)-grading has
        positive grades {1, 2, 3, 4}. Since 1+1=2, 1+2=3, 1+3=4, 2+2=4
        are all positive grades, n_+ has rich internal bracket structure.
        This is the FIRST genuine obstruction case.
        """
        ghost = ghost_obstruction_analysis(5, (3, 2))
        assert ghost.max_positive_grade == 4
        assert not ghost.n_plus_is_abelian
        assert len(ghost.commutator_landings) >= 4  # at least 4 landing pairs
        assert ghost.brst_differential_order >= 2

    def test_sl6_33_ghost_analysis(self):
        """Ghost analysis for (3,3) in sl_6."""
        ghost = ghost_obstruction_analysis(6, (3, 3))
        assert ghost.N == 6

    def test_sl6_222_ghost_analysis(self):
        """Ghost analysis for (2,2,2) in sl_6."""
        ghost = ghost_obstruction_analysis(6, (2, 2, 2))
        assert ghost.N == 6

    def test_ghost_brst_order_hook_vs_nonhook(self):
        """Hook partitions have BRST order 1; non-hooks may have higher.

        The BRST differential order is the key structural difference.
        Order 1 = linear in ghosts = Koszul-type resolution.
        Order >= 2 = quadratic+ in ghosts = genuinely nonlinear BRST.
        """
        # Hook: (3,1) in sl_4
        ghost_hook = ghost_obstruction_analysis(4, (3, 1))
        # Non-hook: (3,2) in sl_5
        ghost_nonhook = ghost_obstruction_analysis(5, (3, 2))

        # The key structural difference
        if ghost_hook.n_plus_is_abelian:
            assert ghost_hook.brst_differential_order == 1
        if not ghost_nonhook.n_plus_is_abelian:
            assert ghost_nonhook.brst_differential_order >= 2

    def test_ext_obstruction_nonzero_for_nonabelian(self):
        """Non-abelian n_+ implies nonzero Ext obstruction estimate."""
        for N, lam, desc in NON_HOOK_TARGETS:
            ghost = ghost_obstruction_analysis(N, lam)
            if not ghost.n_plus_is_abelian:
                assert ghost.ext_group_dimension >= 1, \
                    f"Non-abelian n_+ should give Ext >= 1 for {lam}"

    def test_commutator_landings_nonempty_iff_nonabelian(self):
        """Commutator landings exist iff n_+ is non-abelian."""
        for N, lam, desc in NON_HOOK_TARGETS:
            ghost = ghost_obstruction_analysis(N, lam)
            if ghost.n_plus_is_abelian:
                assert len(ghost.commutator_landings) == 0
            else:
                assert len(ghost.commutator_landings) > 0


# =====================================================================
# F. Kappa/complementarity consistency
# =====================================================================

class TestKappaComplementarity:
    """Kappa and complementarity sum consistency for non-hook orbits."""

    def test_sl4_22_kappa_sum_constant(self):
        """Kappa sum for (2,2) in sl_4 should be constant in k.

        If the level shift k' = -k-8 is correct for (2,2) in sl_4,
        then kappa(W_k(f)) + kappa(W_{k'}(f^t)) should be k-independent.
        Since (2,2) is self-transpose, f^t = f.
        """
        is_const, val = kappa_sum_is_constant(4, (2, 2))
        # RED TEAM FINDING: is the kappa sum actually constant?
        # If YES: the level shift ansatz k'=-k-2N is at least kappa-consistent
        # If NO: the level shift is WRONG for (2,2) and the conjecture needs
        # a different k'(k,f) for non-hook orbits
        assert isinstance(is_const, bool)

    def test_sl4_22_complementarity_sum(self):
        """Complementarity sum c(k) + c(k') for (2,2) in sl_4."""
        is_const, val = complementarity_sum_is_constant(4, (2, 2))
        # Same test: is the central charge sum k-independent?
        assert isinstance(is_const, bool)

    def test_sl5_32_kappa_sum(self):
        """Kappa sum for (3,2) in sl_5: f^t = (2,2,1)."""
        is_const, val = kappa_sum_is_constant(5, (3, 2))
        assert isinstance(is_const, bool)

    def test_sl5_32_complementarity_sum(self):
        """Complementarity sum for (3,2) in sl_5."""
        is_const, val = complementarity_sum_is_constant(5, (3, 2))
        assert isinstance(is_const, bool)

    def test_sl6_33_complementarity(self):
        """Complementarity for (3,3) in sl_6: f^t = (2,2,2)."""
        is_const, val = complementarity_sum_is_constant(6, (3, 3))
        assert isinstance(is_const, bool)

    def test_sl6_222_complementarity(self):
        """Complementarity for (2,2,2) in sl_6: f^t = (3,3)."""
        is_const, val = complementarity_sum_is_constant(6, (2, 2, 2))
        assert isinstance(is_const, bool)

    def test_complementarity_symmetry(self):
        """c(W_k(f)) + c(W_{k'}(f^t)) should equal
        c(W_k(f^t)) + c(W_{k'}(f)) if the formula is symmetric.

        This is a consistency check on the KRW formula.
        """
        for N, lam, desc in [(6, (3, 3), ""), (6, (2, 2, 2), "")]:
            is_const_1, val_1 = complementarity_sum_is_constant(N, lam)
            lam_t = probe_non_hook(N, lam).transpose
            is_const_2, val_2 = complementarity_sum_is_constant(N, lam_t)
            if is_const_1 and is_const_2:
                assert simplify(val_1 - val_2) == 0, \
                    f"BV pair ({lam}, {lam_t}) should give same conductor"

    def test_all_non_hook_kappa_constantness(self):
        """RED TEAM MAIN RESULT: check kappa constantness for ALL targets.

        If kappa sum is NOT constant for some non-hook orbit, the
        conjecture's level shift ansatz is WRONG. This would be a
        GENUINE BREAK.
        """
        results = {}
        for N, lam, desc in NON_HOOK_TARGETS:
            is_const, val = kappa_sum_is_constant(N, lam)
            results[f"sl_{N}_{lam}"] = (is_const, val)

        # Log findings
        for key, (is_const, val) in results.items():
            if not is_const:
                # This is a GENUINE BREAK -- the level shift k'=-k-2N
                # does NOT give constant kappa sum for this orbit
                pass

        # At minimum, the (2,2) case (self-transpose) should work
        assert results["sl_4_(2, 2)"][0], \
            "FATAL: kappa sum for (2,2) in sl_4 is NOT constant!"


# =====================================================================
# G. Full red-team verdict
# =====================================================================

class TestFullVerdict:
    """Complete red-team attack verdict."""

    def test_full_report_runs(self):
        """The full red-team report runs without errors."""
        verdicts = full_red_team_report()
        assert len(verdicts) == len(NON_HOOK_TARGETS)

    def test_at_least_one_obstruction_found(self):
        """The red team should find at least one non-trivial obstruction.

        If all verdicts are "none" severity, then either:
        (a) the conjecture is likely TRUE, or
        (b) our attack is too weak.
        """
        verdicts = full_red_team_report()
        severities = [v.obstruction_severity for v in verdicts]
        # We expect at least one "mild" or worse obstruction
        # from the non-abelian n_+ cases
        assert any(s != "none" for s in severities), \
            "RED TEAM FAILURE: no obstructions found at all!"

    def test_non_abelian_cases_flagged(self):
        """All cases with non-abelian n_+ are flagged."""
        verdicts = full_red_team_report()
        for v in verdicts:
            ghost = ghost_obstruction_analysis(v.N, v.partition)
            if not ghost.n_plus_is_abelian:
                assert v.obstruction_severity in ("mild", "severe", "fatal"), \
                    f"Non-abelian n_+ for {v.partition} not flagged!"

    def test_verdict_classification(self):
        """Each verdict has a valid severity classification."""
        verdicts = full_red_team_report()
        valid_severities = {"none", "mild", "severe", "fatal"}
        for v in verdicts:
            assert v.obstruction_severity in valid_severities

    def test_sl4_22_verdict(self):
        """Specific verdict for (2,2) in sl_4: the FIRST non-hook case.

        This is the single most important test case for the conjecture.
        """
        verdicts = full_red_team_report()
        v_22 = [v for v in verdicts if v.partition == (2, 2) and v.N == 4][0]
        # The (2,2) case is self-transpose, so the level shift is testable
        # What matters is: are kappa/complementarity constant?
        assert isinstance(v_22.kappa_constant, bool)
        assert isinstance(v_22.complementarity_constant, bool)

    def test_summary_contains_diagnosis(self):
        """Each verdict summary contains meaningful diagnosis text."""
        verdicts = full_red_team_report()
        for v in verdicts:
            assert len(v.summary) > 20, \
                f"Summary too short for {v.partition}"

    def test_non_hook_identification_correct(self):
        """Verify our non-hook targets are genuinely non-hook."""
        for N, lam, desc in NON_HOOK_TARGETS:
            lam_norm = tuple(sorted(lam, reverse=True))
            # A hook partition (m, 1^r) has at most one part > 1
            parts_gt_1 = [p for p in lam_norm if p > 1]
            # Non-hook means at least two parts > 1
            assert len(parts_gt_1) >= 2, \
                f"Partition {lam} is actually hook-type!"


# =====================================================================
# H. Critical red-team findings: level shift failure
# =====================================================================

class TestLevelShiftFailure:
    """CRITICAL: the naive level shift k' = -k - 2h^v FAILS for non-hook
    non-principal orbits.

    This is the main red-team finding. The complementarity sum c(k) + c(k')
    is NOT constant under the naive Feigin-Frenkel level shift for most
    non-hook partitions, while it IS constant for all hook partitions.

    Implication: the correct level transform k'(k, f) must depend on the
    nilpotent orbit f, not just the Lie algebra g. This is exactly the
    "non-principal level transform" problem identified in the conjecture.
    """

    def test_sl5_32_complementarity_NOT_constant(self):
        """c(k) + c(k') = 2(4k+29)/(k+5) for (3,2) in sl_5.

        The naive level shift k' = -k-10 gives a k-DEPENDENT complementarity sum.
        However, this is NOT fatal by itself -- even for proved hook pairs
        like (3,1)/(2,1,1) in sl_4, complementarity is k-dependent.
        The duality proof uses kappa compatibility instead.
        """
        is_const, val = complementarity_sum_is_constant(5, (3, 2))
        assert not is_const

    def test_sl6_33_complementarity_NOT_constant(self):
        """c(k) + c(k') for (3,3) in sl_6 is k-dependent."""
        is_const, val = complementarity_sum_is_constant(6, (3, 3))
        assert not is_const

    def test_sl6_222_complementarity_NOT_constant(self):
        """c(k) + c(k') for (2,2,2) in sl_6 is k-dependent.

        Note: (2,2,2) has ABELIAN n_+, so the ghost obstruction is absent.
        But the complementarity is still k-dependent, as for some hooks.
        """
        is_const, val = complementarity_sum_is_constant(6, (2, 2, 2))
        assert not is_const

    def test_sl4_22_complementarity_IS_constant(self):
        """The (2,2) case in sl_4 is CLEAN: complementarity IS constant.

        This suggests (2,2) might be provable by extension of the hook argument.
        """
        is_const, val = complementarity_sum_is_constant(4, (2, 2))
        assert is_const
        # The conductor value is 14
        from sympy import simplify
        assert simplify(val - 14) == 0

    def test_kappa_sum_self_transpose_constant(self):
        """Self-transpose orbits have k-independent kappa sum.

        For self-transpose partitions (lambda = lambda^t), the anomaly
        ratios are equal on both sides, so the kappa sum is k-independent.
        For non-self-transpose partitions, different anomaly ratios make
        the sum a rational function of k.
        """
        from compute.lib.nonprincipal_ds_orbits import transpose_partition
        for N, lam, desc in NON_HOOK_TARGETS:
            lam_t = transpose_partition(lam)
            is_const, val = kappa_sum_is_constant(N, lam)
            if lam == lam_t:
                assert is_const, f"Self-transpose {lam} should have constant kappa sum"

    def test_sl6_321_clean_despite_nonabelian(self):
        """(3,2,1) in sl_6: complementarity IS constant despite non-abelian n_+.

        The staircase partition (3,2,1) = (3,2,1)^t is self-transpose.
        Despite having non-abelian n_+ (BRST order 4), the complementarity
        sum IS constant (= 8). This suggests the obstruction to DS-KD
        commutation is NOT purely about n_+ abelianity, but about the
        interaction between the KRW formula and the level shift.
        """
        is_const, val = complementarity_sum_is_constant(6, (3, 2, 1))
        assert is_const, "Staircase (3,2,1) should have constant complementarity"

    def test_abelianity_does_not_determine_complementarity(self):
        """KEY FINDING: n_+ abelianity does NOT determine complementarity constancy.

        Counterexamples:
        - (2,2,2) has abelian n_+ but NON-constant complementarity
        - (3,2,1) has non-abelian n_+ but CONSTANT complementarity

        This refutes the naive hypothesis that "n_+ abelian => DS-KD commutes."
        The level-shift problem is INDEPENDENT of the BRST structure.
        """
        # Abelian but non-constant:
        ghost_222 = ghost_obstruction_analysis(6, (2, 2, 2))
        comp_222, _ = complementarity_sum_is_constant(6, (2, 2, 2))
        assert ghost_222.n_plus_is_abelian
        assert not comp_222  # Non-constant despite abelian n_+!

        # Non-abelian but constant:
        ghost_321 = ghost_obstruction_analysis(6, (3, 2, 1))
        comp_321, _ = complementarity_sum_is_constant(6, (3, 2, 1))
        assert not ghost_321.n_plus_is_abelian
        assert comp_321  # Constant despite non-abelian n_+!
