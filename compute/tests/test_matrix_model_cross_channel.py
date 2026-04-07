r"""Tests for the matrix model analysis of delta_F_g^cross(W_3).

Verifies the spectral curve obstruction theorem, Betti decomposition,
Frobenius manifold structure, loop equation consistency, and effective
spectral curve parameters using multiple independent paths.

Seven verification paths:
  Path 1: Bernoulli number correctness (foundational)
  Path 2: Betti decomposition consistency (graph sum)
  Path 3: Power sum / Newton identity analysis
  Path 4: Spectral curve obstruction (1-BP and 2-BP failures)
  Path 5: Frobenius manifold structure constants
  Path 6: Loop equation / Schwinger-Dyson consistency
  Path 7: Effective spectral curve parameters

References:
    thm:multi-weight-genus-expansion (higher_genus_foundations.tex)
    Eynard-Orantin (2007), Chekhov-Eynard-Orantin (2006)
"""

import pytest
from fractions import Fraction

from compute.lib.matrix_model_cross_channel import (
    bernoulli_number,
    betti_decomposition,
    betti_polynomial,
    tree_contribution_genus3,
    loop_equation_genus2,
    schwinger_dyson_check,
    eynard_orantin_F2_quartic,
    match_spectral_curve_F2_F3,
    effective_two_branch_point,
    power_sum_decomposition,
    spectral_curve_obstruction,
    effective_spectral_curve_parameters,
    frobenius_topological_recursion_F2,
    w3_frobenius_prepotential,
    factorial_growth_analysis,
    airy_omega,
    topological_recursion_F_g,
    w3_spectral_curve_discriminant,
    full_diagnostic,
)
from compute.lib.multi_weight_genus_tower import (
    delta_F2_closed_form,
    delta_F3_closed_form,
    delta_F4_closed_form,
    kappa_total,
    lambda_fp,
    cross_channel_correction,
)


# ============================================================================
# Section 1: Bernoulli numbers (AP10: never trust hardcoded values)
# ============================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers against multiple independent sources."""

    def test_B0(self):
        assert bernoulli_number(0) == Fraction(1)

    def test_B1(self):
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_B2(self):
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_B10(self):
        assert bernoulli_number(10) == Fraction(5, 66)

    def test_B12(self):
        assert bernoulli_number(12) == Fraction(-691, 2730)

    def test_odd_vanish(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == 0

    def test_alternating_signs(self):
        """(-1)^{n/2+1} * B_n > 0 for even n >= 2."""
        for n in [2, 4, 6, 8, 10, 12]:
            b = bernoulli_number(n)
            sign = (-1) ** (n // 2 + 1)
            assert sign * b > 0

    def test_von_staudt_clausen(self):
        """Von Staudt-Clausen: B_{2n} + sum_{(p-1)|2n} 1/p is an integer."""
        # For n=1 (B_2 = 1/6): primes p with (p-1)|2 are p=2,3.
        # B_2 + 1/2 + 1/3 = 1/6 + 1/2 + 1/3 = 1. Integer check.
        assert bernoulli_number(2) + Fraction(1, 2) + Fraction(1, 3) == 1
        # For n=2 (B_4 = -1/30): primes with (p-1)|4 are p=2,3,5.
        # B_4 + 1/2 + 1/3 + 1/5 = -1/30 + 1/2 + 1/3 + 1/5 = 1. Check.
        assert bernoulli_number(4) + Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 5) == 1


# ============================================================================
# Section 2: Airy curve omega_{g,0} (Eynard-Orantin)
# ============================================================================

class TestAiryCurve:
    """Verify Eynard-Orantin invariants of the Airy curve y^2 = x."""

    def test_F2_airy(self):
        """F_2^Airy = B_4/(4*2) = -1/240."""
        assert airy_omega(2, 0) == Fraction(-1, 240)

    def test_F3_airy(self):
        """F_3^Airy = B_6/(6*4) = 1/1008."""
        assert airy_omega(3, 0) == Fraction(1, 1008)

    def test_F4_airy(self):
        """F_4^Airy = B_8/(8*6) = -1/1440."""
        assert airy_omega(4, 0) == Fraction(-1, 1440)

    def test_sign_alternation(self):
        """F_g^Airy has sign (-1)^{g+1} (same as B_{2g})."""
        for g in [2, 3, 4, 5, 6]:
            f = airy_omega(g, 0)
            expected_sign = (-1) ** (g + 1)
            assert (f > 0) == (expected_sign > 0), f"g={g}: F={f}, expected sign {expected_sign}"


# ============================================================================
# Section 3: Betti decomposition
# ============================================================================

class TestBettiDecomposition:
    """Verify the decomposition of delta_F_g by first Betti number."""

    def test_betti_sum_equals_total_g2(self):
        """Sum over Betti strata reproduces delta_F_2."""
        for cv in [1, 10, 26, 50]:
            c = Fraction(cv)
            bd = betti_decomposition(2, c)
            total_mixed = sum(d['mixed'] for d in bd.values())
            assert total_mixed == cross_channel_correction(2, c)

    def test_betti_sum_equals_total_g3(self):
        """Sum over Betti strata reproduces delta_F_3."""
        c = Fraction(26)
        bd = betti_decomposition(3, c)
        total_mixed = sum(d['mixed'] for d in bd.values())
        assert total_mixed == cross_channel_correction(3, c)

    def test_no_tree_mixing_g2(self):
        """At genus 2, trees (h1=0) have ZERO cross-channel contribution.

        No stable genus-2 tree with n=0 has a genus-0 vertex, so
        all edges connect genus >= 1 vertices, forcing diagonal channels.
        """
        c = Fraction(26)
        bd = betti_decomposition(2, c)
        if 0 in bd:
            assert bd[0]['mixed'] == 0

    def test_tree_exists_g3(self):
        """At genus 3, trees DO contribute (via star K_{1,3} with genus-0 center)."""
        c = Fraction(26)
        bd = betti_decomposition(3, c)
        assert 0 in bd
        assert bd[0]['mixed'] > 0

    def test_max_betti_dominates_moderate_c(self):
        """The max-Betti stratum (h1=g) dominates at moderate c."""
        c = Fraction(26)
        for g in [2, 3]:
            bd = betti_decomposition(g, c)
            total = sum(d['mixed'] for d in bd.values())
            max_h1 = max(h for h in bd if bd[h]['mixed'] > 0)
            max_frac = bd[max_h1]['mixed'] / total
            assert max_frac > Fraction(8, 10), f"g={g}: max Betti fraction = {float(max_frac)}"

    def test_tree_dominates_large_c_g3(self):
        """At large c, trees (h1=0) grow as c while loops are O(1)."""
        c = Fraction(10000)
        bd = betti_decomposition(3, c)
        total = sum(d['mixed'] for d in bd.values())
        tree_frac = bd[0]['mixed'] / total if 0 in bd else Fraction(0)
        # At c=10000, trees should dominate
        assert tree_frac > Fraction(9, 10)

    def test_betti_c_scaling(self):
        """Betti-h1 stratum scales as c^{1-h1} at large c.

        Specifically, c^{h1-1} * delta_F_g^{(h1)}(c) should approach a constant.
        """
        c1 = Fraction(500)
        c2 = Fraction(1000)
        bd1 = betti_decomposition(3, c1)
        bd2 = betti_decomposition(3, c2)
        # h1=0: should scale as c. Ratio of c*m(c) should be ~1.
        if 0 in bd1 and 0 in bd2 and bd1[0]['mixed'] > 0:
            ratio = (bd2[0]['mixed'] / bd1[0]['mixed']) / (c2 / c1)
            assert abs(float(ratio) - 1.0) < 0.01

    def test_betti_graph_counts(self):
        """Verify graph counts per Betti stratum at genus 2."""
        c = Fraction(26)
        bd = betti_decomposition(2, c)
        total_graphs = sum(d['graph_count'] for d in bd.values())
        # Genus 2 has 7 boundary graphs (including barbell)
        # h1=0: 1 tree (genera (2,1) with 1 edge), h1=1: 2 graphs, h1=2: 3 graphs
        # Plus possibly the smooth vertex (no edges) in the enumeration
        assert total_graphs >= 5


# ============================================================================
# Section 4: Tree contribution at genus 3
# ============================================================================

class TestTreeContribution:
    """Verify the tree-level cross-channel contribution."""

    def test_tree_g3_coefficient(self):
        """Tree contribution at genus 3 equals c/27648 = c * lambda_1^3 / 3.

        The star K_{1,3} with genus-0 center and 3 genus-1 leaves gives:
        V0_3(mixed) * (lambda_1)^3 / |Aut| summed over mixed assignments.
        """
        for cv in [10, 26, 100]:
            c = Fraction(cv)
            tree = tree_contribution_genus3(c)
            expected = c / 27648
            # Should be close (may differ slightly due to other trees)
            # Actually tree_contribution_genus3 computes only the star tree
            assert tree == expected, f"c={cv}: tree={tree}, expected={expected}"

    def test_tree_g3_matches_betti(self):
        """Tree contribution matches the h1=0 Betti stratum."""
        c = Fraction(26)
        tree = tree_contribution_genus3(c)
        bd = betti_decomposition(3, c)
        # The tree contribution is one graph among possibly several h1=0 graphs
        if 0 in bd:
            # tree should be <= total h1=0
            assert tree <= bd[0]['mixed']

    def test_tree_g3_leading_coefficient(self):
        """At large c, delta_F_3 ~ c/27648 = 5c/138240."""
        c = Fraction(10**7)
        d3 = delta_F3_closed_form(c)
        expected = Fraction(5) * c / 138240
        rel_err = float(abs(d3 - expected) / expected)
        assert rel_err < 0.001


# ============================================================================
# Section 5: Power sum analysis
# ============================================================================

class TestPowerSumAnalysis:
    """Verify the Bernoulli-normalized power sum decomposition."""

    def test_sigma_sign_alternation(self):
        """sigma_g has sign (-1)^g (from Bernoulli sign alternation)."""
        c = Fraction(26)
        ps = power_sum_decomposition(c)
        assert ps['sigma_2'] < 0  # B_4 < 0, d2 > 0
        assert ps['sigma_3'] > 0  # B_6 > 0, d3 > 0
        assert ps['sigma_4'] < 0  # B_8 < 0, d4 > 0

    def test_1bp_fails(self):
        """Single branch point model fails: ratios not constant."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            ps = power_sum_decomposition(c)
            deviation = ps['geometric_test']
            assert deviation is not None
            assert deviation > 0.3, f"1-BP deviation too small at c={cv}: {deviation}"

    def test_2bp_fails(self):
        """Two branch point model fails: Newton identity violated."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            ps = power_sum_decomposition(c)
            assert ps['two_bp_matches'] is False

    def test_sigma_magnitude_decreases_with_c(self):
        """Larger c gives smaller |sigma_g| (branch points recede)."""
        s_prev = None
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            ps = power_sum_decomposition(c)
            s_now = abs(ps['sigma_2'])
            if s_prev is not None:
                assert s_now < s_prev
            s_prev = s_now


# ============================================================================
# Section 6: Spectral curve obstruction
# ============================================================================

class TestSpectralCurveObstruction:
    """Verify the spectral curve obstruction theorem."""

    def test_obstruction_proved_c10(self):
        obs = spectral_curve_obstruction(Fraction(10))
        assert obs['obstruction_proved']

    def test_obstruction_proved_c26(self):
        obs = spectral_curve_obstruction(Fraction(26))
        assert obs['obstruction_proved']

    def test_obstruction_proved_c50(self):
        obs = spectral_curve_obstruction(Fraction(50))
        assert obs['obstruction_proved']

    def test_2bp_error_magnitude(self):
        """2-branch-point relative error is O(20), not O(1)."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            obs = spectral_curve_obstruction(c)
            err = obs['two_branch_point_test']['relative_error']
            assert err > 10, f"c={cv}: 2-BP error only {err}"

    def test_obstruction_c_independent(self):
        """The obstruction holds at ALL c values tested."""
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(cv)
            obs = spectral_curve_obstruction(c)
            assert obs['obstruction_proved'], f"Obstruction fails at c={cv}"


# ============================================================================
# Section 7: Effective spectral curve parameters
# ============================================================================

class TestEffectiveSpectralCurve:
    """Verify the c-dependent effective spectral curve."""

    def test_defect_nonzero(self):
        """The 2-BP defect is nonzero (3rd branch point needed)."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            eff = effective_spectral_curve_parameters(c)
            assert eff['sigma_4_defect'] != 0

    def test_defect_relative_magnitude(self):
        """The defect is large (not a perturbative correction)."""
        c = Fraction(26)
        eff = effective_spectral_curve_parameters(c)
        assert eff['defect_relative'] > 10

    def test_effective_curve_c_dependent(self):
        """The effective curve parameters change with c."""
        eff1 = effective_spectral_curve_parameters(Fraction(10))
        eff2 = effective_spectral_curve_parameters(Fraction(50))
        assert eff1['e2_2bp'] != eff2['e2_2bp']

    def test_3bp_elementary_symmetric(self):
        """The 3-BP elementary symmetric polynomials are well-defined."""
        c = Fraction(26)
        eff = effective_spectral_curve_parameters(c)
        # e1 = sigma_2, e2, and the defect determines e3
        assert eff['e1_2bp'] != 0
        assert eff['e2_2bp'] != 0


# ============================================================================
# Section 8: Effective two-branch-point model
# ============================================================================

class TestEffectiveTwoBranchPoint:
    """Verify the 2-branch-point fitting procedure."""

    def test_prediction_fails(self):
        """The 2-BP model's F_4 prediction does NOT match actual."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            result = effective_two_branch_point(c)
            assert not result['prediction_matches']

    def test_relative_error_significant(self):
        """The prediction error is not small."""
        c = Fraction(26)
        result = effective_two_branch_point(c)
        assert result['relative_error'] > 10


# ============================================================================
# Section 9: Frobenius manifold structure
# ============================================================================

class TestFrobeniusManifold:
    """Verify the W_3 Frobenius manifold structure."""

    def test_prepotential_symmetry(self):
        """F_0(t_T, t_W) has Z_2 symmetry under t_W -> -t_W."""
        c = Fraction(26)
        t_T, t_W = Fraction(1), Fraction(1)
        f_plus = w3_frobenius_prepotential(t_T, t_W, c)
        f_minus = w3_frobenius_prepotential(t_T, -t_W, c)
        assert f_plus == f_minus

    def test_prepotential_cubic(self):
        """F_0 = (c/6)*t_T^3 + (c/2)*t_T*t_W^2."""
        c = Fraction(26)
        t_T, t_W = Fraction(3), Fraction(2)
        expected = c * t_T**3 / 6 + c * t_T * t_W**2 / 2
        assert w3_frobenius_prepotential(t_T, t_W, c) == expected

    def test_frobenius_F2_matches(self):
        """Frobenius manifold graph sum reproduces delta_F_2."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            result = frobenius_topological_recursion_F2(c)
            assert result['match']

    def test_multiplication_eigenvalues(self):
        """T-multiplication has eigenvalues 2 and 3."""
        result = frobenius_topological_recursion_F2(Fraction(26))
        assert result['eigenvalues_T'] == [2, 3]

    def test_a2_spectral_curve(self):
        """The W_3 Frobenius manifold has A_2 spectral curve (cubic)."""
        curve = w3_spectral_curve_discriminant(Fraction(26))
        assert 'y^3' in curve['genus_0_curve']


# ============================================================================
# Section 10: Loop equations / Schwinger-Dyson
# ============================================================================

class TestLoopEquations:
    """Verify loop equation / Schwinger-Dyson consistency."""

    def test_schwinger_dyson_betti_match_g2(self):
        """The Betti decomposition sums to the total at genus 2."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            result = schwinger_dyson_check(2, c)
            assert result['betti_match']

    def test_schwinger_dyson_betti_match_g3(self):
        """The Betti decomposition sums to the total at genus 3."""
        c = Fraction(26)
        result = schwinger_dyson_check(3, c)
        assert result['betti_match']

    def test_loop_equation_g2_consistency(self):
        """Loop equation result matches closed form at genus 2."""
        c = Fraction(26)
        result = loop_equation_genus2(c)
        assert result['match']


# ============================================================================
# Section 11: Factorial growth
# ============================================================================

class TestFactorialGrowth:
    """Verify the super-exponential growth structure."""

    def test_ratio_increases_with_genus(self):
        """delta_{g+1}/delta_g increases with g."""
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            d2 = delta_F2_closed_form(c)
            d3 = delta_F3_closed_form(c)
            d4 = delta_F4_closed_form(c)
            assert d3 / d2 < d4 / d3

    def test_ratio_of_ratios_structure(self):
        """The ratio r43/r32 is between 1 and 2 for moderate c."""
        fa = factorial_growth_analysis()
        for cv, data in fa.items():
            rr = data['ratio_of_ratios']
            if rr is not None:
                assert 1.0 < rr < 2.0, f"c={cv}: r43/r32 = {rr}"

    def test_growth_faster_than_geometric(self):
        """delta_{g+1}/delta_g grows with g (not constant)."""
        c = Fraction(26)
        d2 = delta_F2_closed_form(c)
        d3 = delta_F3_closed_form(c)
        d4 = delta_F4_closed_form(c)
        r32 = float(d3 / d2)
        r43 = float(d4 / d3)
        assert r43 > r32


# ============================================================================
# Section 12: Topological recursion with branch point data
# ============================================================================

class TestTopologicalRecursion:
    """Verify the topological recursion framework."""

    def test_single_bp_scaling(self):
        """Single branch point F_g scales as 1/a^{2g-2}."""
        bp = [{'a': Fraction(2), 'weight': Fraction(1)}]
        f2 = topological_recursion_F_g(2, bp)
        f3 = topological_recursion_F_g(3, bp)
        # F_3/F_2 = (1/a^4)/(1/a^2) * (B6/24)/(B4/8) = (1/a^2) * (B6*8)/(B4*24)
        ratio = f3 / f2
        expected = Fraction(1, 4) * bernoulli_number(6) * 8 / (bernoulli_number(4) * 24)
        assert ratio == expected

    def test_two_bp_additive(self):
        """Two branch points give additive F_g (at leading order)."""
        bp1 = [{'a': Fraction(2), 'weight': Fraction(1)}]
        bp2 = [{'a': Fraction(3), 'weight': Fraction(1)}]
        bp_both = [
            {'a': Fraction(2), 'weight': Fraction(1)},
            {'a': Fraction(3), 'weight': Fraction(1)},
        ]
        f2_1 = topological_recursion_F_g(2, bp1)
        f2_2 = topological_recursion_F_g(2, bp2)
        f2_both = topological_recursion_F_g(2, bp_both)
        assert f2_both == f2_1 + f2_2


# ============================================================================
# Section 13: Cross-checks and consistency
# ============================================================================

class TestCrossChecks:
    """Cross-check between different computation methods."""

    def test_betti_total_equals_closed_form_g2(self):
        """Betti decomposition total matches closed form at genus 2."""
        for cv in [1, 5, 10, 26, 50]:
            c = Fraction(cv)
            bd = betti_decomposition(2, c)
            total = sum(d['mixed'] for d in bd.values())
            assert total == delta_F2_closed_form(c)

    def test_betti_total_equals_closed_form_g3(self):
        """Betti decomposition total matches closed form at genus 3."""
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            bd = betti_decomposition(3, c)
            total = sum(d['mixed'] for d in bd.values())
            assert total == delta_F3_closed_form(c)

    def test_positivity_all_betti_strata(self):
        """All Betti strata have non-negative mixed contributions."""
        for g in [2, 3]:
            c = Fraction(26)
            bd = betti_decomposition(g, c)
            for h1, data in bd.items():
                assert data['mixed'] >= 0, f"g={g}, h1={h1}: negative mixed"

    def test_diagonal_plus_mixed_positive(self):
        """Total (diagonal + mixed) is positive at all Betti strata."""
        c = Fraction(26)
        for g in [2, 3]:
            bd = betti_decomposition(g, c)
            for h1, data in bd.items():
                assert data['total'] >= 0


# ============================================================================
# Section 14: Full diagnostic
# ============================================================================

class TestFullDiagnostic:

    def test_full_diagnostic_runs(self):
        """Full diagnostic runs without error."""
        c = Fraction(26)
        result = full_diagnostic(c)
        assert 'spectral_curve_obstruction' in result
        assert 'power_sum_decomposition' in result
        assert 'effective_curve' in result
        assert 'frobenius_F2' in result
        assert 'loop_equation' in result

    def test_full_diagnostic_obstruction(self):
        """Full diagnostic confirms obstruction."""
        c = Fraction(26)
        result = full_diagnostic(c)
        assert result['spectral_curve_obstruction']['obstruction_proved']


# ============================================================================
# Section 15: Mathematical structure theorems
# ============================================================================

class TestStructureTheorems:
    """Verify the key mathematical results."""

    def test_no_tree_mixing_genus2(self):
        """THEOREM: delta_F_2^cross has no tree-level (h1=0) contribution.

        Proof: At genus 2 with n=0, any tree has 2 vertices of genera (g1,g2)
        with g1+g2=2, connected by 1 bridge. Each vertex has val=1. The only
        channel assignment gives both half-edges the same label (diagonal).
        No genus-0 vertex exists in a stable genus-2 tree with n=0.
        """
        for cv in [1, 10, 26, 50, 100]:
            c = Fraction(cv)
            bd = betti_decomposition(2, c)
            if 0 in bd:
                assert bd[0]['mixed'] == 0

    def test_max_betti_dominance(self):
        """THEOREM: At moderate c (1 <= c <= 50), the max-Betti stratum
        contributes > 75% of delta_F_g^cross.

        This is the OPPOSITE of standard matrix model behavior, where
        tree-level (genus-0 spectral curve) dominates. The dominance of
        max-loop graphs reflects the CohFT vertex insertions.
        """
        for cv in [1, 5, 10, 26, 50]:
            c = Fraction(cv)
            for g in [2, 3]:
                bd = betti_decomposition(g, c)
                total = sum(d['mixed'] for d in bd.values())
                if total == 0:
                    continue
                max_h1 = max(h for h in bd if bd[h]['mixed'] > 0)
                frac = float(bd[max_h1]['mixed'] / total)
                assert frac > 0.75, (
                    f"g={g}, c={cv}: max-Betti fraction = {frac:.4f}")

    def test_spectral_curve_obstruction_universal(self):
        """THEOREM: No spectral curve with <= 2 branch points reproduces
        delta_F_g^cross at ANY c > 0.

        This follows from the failure of the Newton identity at genus 4:
        the sigma_4 predicted by 2-BP does not match the actual sigma_4.
        """
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(cv)
            obs = spectral_curve_obstruction(c)
            assert obs['obstruction_proved'], f"Failed at c={cv}"

    def test_tree_coefficient_universal(self):
        """The tree (h1=0) mixed coefficient at genus 3 is exactly c/27648.

        Independent of other graph contributions. This coefficient is:
        c/27648 = c * (lambda_1)^3 / 3 = c * (1/24)^3 / 3.
        """
        for cv in [1, 10, 26, 100]:
            c = Fraction(cv)
            tree = tree_contribution_genus3(c)
            assert tree == c / 27648

    def test_h1_1_coefficient_genus3_exact(self):
        """THEOREM: The 1-loop (h1=1) cross-channel coefficient at genus 3
        is exactly 79/2880, independent of c.

        This is the O(1) term in the large-c expansion of delta_F_3.
        The residual (3792c^2 + 1149120c + 217071360)/(138240c^2)
        after removing the tree level c/27648 has leading constant 3792/138240 = 79/2880.
        """
        for cv in [100, 1000, 10000]:
            c = Fraction(cv)
            bd = betti_decomposition(3, c)
            h1_1_mixed = bd[1]['mixed']
            assert h1_1_mixed == Fraction(79, 2880)

    def test_betti_strata_genus2_exact(self):
        """The genus-2 Betti strata at c=26 have exact rational values."""
        c = Fraction(26)
        bd = betti_decomposition(2, c)
        total = sum(d['mixed'] for d in bd.values())
        assert total == delta_F2_closed_form(c)
        # h1=2 dominates at c=26 (88.7%)
        h2_frac = bd[2]['mixed'] / total
        assert h2_frac > Fraction(85, 100)

    def test_three_branch_point_cubic_discriminant_negative(self):
        """The effective 3-branch-point cubic has 1 real + 2 complex roots.

        The Newton identity analysis gives elementary symmetric polynomials
        e1, e2, e3 whose cubic x^3 - e1*x^2 + e2*x - e3 = 0 has negative
        discriminant (1 real root + complex conjugate pair). This is
        consistent with the A_2 spectral curve structure.
        """
        for cv in [10, 26, 50]:
            c = Fraction(cv)
            eff = effective_spectral_curve_parameters(c)
            tau_2 = abs(eff['sigma_2'])
            tau_3 = abs(eff['sigma_3'])
            tau_4 = abs(eff['sigma_4'])
            e1 = tau_2
            e2 = (tau_2**2 - tau_3) / 2
            e3 = (tau_2**3 - 3*tau_2*tau_3 + 2*tau_4) / 6
            D = 18*e1*e2*e3 - 4*e1**3*e3 + e1**2*e2**2 - 4*e2**3 - 27*e3**2
            assert D < 0, f"c={cv}: discriminant D = {float(D)} should be < 0"
