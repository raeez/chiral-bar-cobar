"""Tests for genus-3 Killing correction for sl_2 KM (task B9).

Ground truth:
  - epsilon_g = 0 at ALL genera for KM sl_2
  - Three independent vanishing arguments:
    (1) Strict dg Lie: l_n = 0 for n >= 3, Jacobi kills l_2
    (2) Degree obstruction: H*(Def_cyc) = C[2], l_n lands in degree n+2 > 2
    (3) Graded antisymmetry: l_n(x,...,x) = 0 for even-degree x

The Killing 3-cocycle phi(a,b,c) = kap([a,b],c) generates the one-dimensional
H^2(Def_cyc) = H^3(sl_2) = C. All theta_g are proportional to [phi] in the
Def_cyc direction, so:
  - l_2(theta_{g1}, theta_{g2}) involves [phi, phi]_NR, which vanishes because
    Lambda^5(g*) = 0 for dim(g) = 3.
  - l_3(theta_{g1}, theta_{g2}, theta_{g3}) vanishes on the strict dg Lie
    (original complex), by degree obstruction (minimal model), and by
    graded antisymmetry.
  - l_n for n >= 4 vanishes by all three arguments.

This computation confirms that the universal MC class Theta_A for KM
algebras has no homotopy transfer corrections at any genus.
"""

import pytest
from fractions import Fraction

import numpy as np

from compute.lib.genus3_correction import (
    cyclic_def_complex_dimensions,
    cyclic_def_cohomology_dimensions,
    strict_dg_lie_vanishing,
    degree_obstruction_analysis,
    antisymmetry_vanishing,
    killing_on_repeated_eta,
    higher_genus_vanishing,
    even_arity_antisymmetry_analysis,
    mc_equation_genus_g,
    l3_tree_formula_chain_level,
    nr_bracket_degree_analysis,
    genus3_killing_correction_summary,
    _genus_partitions,
)


# ============================================================
# Cyclic deformation complex structure
# ============================================================

class TestCyclicDefComplex:
    """Verify the cyclic deformation complex dimensions for sl_2."""

    def test_complex_dimensions(self):
        dims = cyclic_def_complex_dimensions()
        assert dims[0] == 3, "Def^0 = g should have dim 3"
        assert dims[1] == 3, "Def^1 = Lambda^2(g*) should have dim 3"
        assert dims[2] == 1, "Def^2 = Lambda^3(g*) should have dim 1"

    def test_complex_total_dimension(self):
        dims = cyclic_def_complex_dimensions()
        assert sum(dims.values()) == 7

    def test_cohomology_dimensions(self):
        """H^0 = H^1 = 0, H^2 = C for semisimple sl_2."""
        h_dims = cyclic_def_cohomology_dimensions()
        assert h_dims[0] == 0, "H^0(Def) = H^1(sl_2) = 0"
        assert h_dims[1] == 0, "H^1(Def) = H^2(sl_2) = 0"
        assert h_dims[2] == 1, "H^2(Def) = H^3(sl_2) = C"

    def test_euler_characteristic(self):
        """chi(Def) = 3 - 3 + 1 = 1; chi(H) = 0 - 0 + 1 = 1."""
        dims = cyclic_def_complex_dimensions()
        h_dims = cyclic_def_cohomology_dimensions()
        chi_complex = sum((-1) ** k * dims[k] for k in dims)
        chi_cohom = sum((-1) ** k * h_dims[k] for k in h_dims)
        assert chi_complex == chi_cohom == 1

    def test_minimal_model_concentrated_in_degree_2(self):
        """The minimal model H is concentrated in degree 2."""
        h_dims = cyclic_def_cohomology_dimensions()
        nonzero_degrees = [k for k, v in h_dims.items() if v > 0]
        assert nonzero_degrees == [2]


# ============================================================
# Argument 1: Strict dg Lie vanishing
# ============================================================

class TestStrictDgLie:
    """Strict dg Lie argument: l_n = 0 for n >= 3."""

    def test_jacobi_holds(self):
        result = strict_dg_lie_vanishing()
        assert result["jacobi_identity_holds"]

    def test_l3_vanishes_on_original(self):
        result = strict_dg_lie_vanishing()
        assert result["l3_vanishes_on_original"]

    def test_l4_plus_vanishes(self):
        result = strict_dg_lie_vanishing()
        assert result["l4_plus_vanishes_on_original"]

    def test_epsilon_2_vanishes(self):
        result = strict_dg_lie_vanishing()
        assert result["epsilon_2_vanishes"]

    def test_epsilon_3_vanishes(self):
        result = strict_dg_lie_vanishing()
        assert result["epsilon_3_vanishes"]

    def test_all_genera_vanish(self):
        result = strict_dg_lie_vanishing()
        assert result["epsilon_g_vanishes_all_g"]


# ============================================================
# Argument 2: Degree obstruction
# ============================================================

class TestDegreeObstruction:
    """Degree obstruction on minimal model."""

    def test_genus_2_vanishes(self):
        result = degree_obstruction_analysis()
        assert result["genus_2_vanishes"]

    def test_genus_3_vanishes(self):
        result = degree_obstruction_analysis()
        assert result["genus_3_vanishes"]

    def test_genus_4_vanishes(self):
        result = degree_obstruction_analysis()
        assert result["genus_4_vanishes"]

    def test_genus_5_vanishes(self):
        result = degree_obstruction_analysis()
        assert result["genus_5_vanishes"]

    def test_genus_2_detail(self):
        """At genus 2, arities 1 and 2 appear.
        l_1 output = 3, l_2 output = 4. Neither is 2."""
        result = degree_obstruction_analysis()
        detail = result["genus_2_detail"]
        arities = {d["arity"] for d in detail}
        assert arities == {1, 2}
        # Check specific output degrees: n+2 for each arity n
        for d in detail:
            assert d["output_degree"] == d["arity"] + 2
            assert not d["lands_in_H"]

    def test_genus_3_detail(self):
        """At genus 3, arities 1, 2, 3 appear.
        l_1 output = 3, l_2 output = 4, l_3 output = 5. None is 2."""
        result = degree_obstruction_analysis()
        detail = result["genus_3_detail"]

        arities = {d["arity"] for d in detail}
        assert arities == {1, 2, 3}

        for d in detail:
            assert not d["lands_in_H"], (
                f"l_{d['arity']} lands in degree {d['output_degree']}, "
                f"should not be in H"
            )

    def test_output_degree_formula(self):
        """Output degree of l_n on n degree-2 inputs is n+2.
        For n >= 1, n+2 >= 3 > 2 = max cohomology degree."""
        for n in range(1, 10):
            output = n * 2 + (2 - n)  # = n + 2
            assert output == n + 2
            assert output > 2, f"l_{n} output degree {output} should exceed 2"


# ============================================================
# Argument 3: Graded antisymmetry
# ============================================================

class TestAntisymmetry:
    """Graded antisymmetry argument."""

    def test_theta_degree_is_2(self):
        result = antisymmetry_vanishing()
        assert result["degree_of_theta"] == 2

    def test_koszul_sign(self):
        """Koszul sign for swapping two degree-2 elements: (-1)^{2*2} = +1."""
        result = antisymmetry_vanishing()
        assert result["koszul_sign"] == Fraction(1)

    def test_antisymmetry_sign(self):
        """L-infinity operations are graded antisymmetric: extra -1 per swap."""
        result = antisymmetry_vanishing()
        assert result["antisymmetry_sign"] == Fraction(-1)

    def test_total_sign(self):
        """Total sign for transposition: +1 * (-1) = -1."""
        result = antisymmetry_vanishing()
        assert result["total_sign_for_transposition"] == Fraction(-1)

    def test_l3_vanishes(self):
        result = antisymmetry_vanishing()
        assert result["l3_vanishes_by_antisymmetry"]

    def test_even_arity_all_vanish(self):
        """l_n(x,...,x) = 0 for all n >= 2 when x has even degree."""
        result = even_arity_antisymmetry_analysis()
        for n in range(2, 8):
            data = result[f"l_{n}_on_repeated_deg2"]
            assert data["vanishes"], f"l_{n} on repeated degree-2 should vanish"
            assert data["swap_sign"] == Fraction(-1)

    def test_mixed_genera_vanish(self):
        """Even with mixed genus inputs, all terms vanish because
        theta_g are proportional to [phi] in the Def_cyc direction."""
        result = even_arity_antisymmetry_analysis()
        assert result["mixed_genera_vanish"]


# ============================================================
# Killing cocycle on repeated arguments
# ============================================================

class TestKillingOnRepeated:
    """l_3([phi], [phi], [phi]) = 0 on the minimal model."""

    def test_phi_generates_H3(self):
        result = killing_on_repeated_eta()
        assert result["phi_generates_H3"]

    def test_H2_Def_one_dimensional(self):
        result = killing_on_repeated_eta()
        assert result["H2_Def_cyclic_dim"] == 1

    def test_l3_target_degree(self):
        """l_3 on three degree-2 inputs: output degree = 2+2+2+(2-3) = 5."""
        result = killing_on_repeated_eta()
        assert result["l3_target_degree"] == 5

    def test_H5_vanishes(self):
        result = killing_on_repeated_eta()
        assert result["H5_dimension"] == 0

    def test_l3_vanishes_by_degree(self):
        result = killing_on_repeated_eta()
        assert result["l3_vanishes_degree"]

    def test_l3_vanishes_by_antisymmetry(self):
        result = killing_on_repeated_eta()
        assert result["l3_vanishes_antisymmetry"]


# ============================================================
# Chain-level tree formula verification
# ============================================================

class TestChainLevelTreeFormula:
    """HTT tree formula gives l_3^{tr}([phi],[phi],[phi]) = 0."""

    def test_l2_phi_phi_vanishes(self):
        """[phi, phi]_NR = 0 because Lambda^5(g) = 0."""
        result = l3_tree_formula_chain_level()
        assert result["l2_phi_phi_vanishes"]

    def test_h_kills_high_degree(self):
        result = l3_tree_formula_chain_level()
        assert result["h_kills_high_degree"]

    def test_tree_term_1_zero(self):
        result = l3_tree_formula_chain_level()
        assert result["tree_term_1_zero"]

    def test_tree_term_2_zero(self):
        result = l3_tree_formula_chain_level()
        assert result["tree_term_2_zero"]

    def test_transferred_l3_is_zero(self):
        result = l3_tree_formula_chain_level()
        assert result["transferred_l3_phi_phi_phi"] == Fraction(0)


# ============================================================
# NR bracket degree analysis
# ============================================================

class TestNRBracketDegrees:
    """Nijenhuis-Richardson bracket degree constraints."""

    def test_l2_on_two_deg2_vanishes(self):
        """NR bracket on two degree-2 elements: needs Lambda^5(g) = 0."""
        result = nr_bracket_degree_analysis()
        assert result["l2_on_two_deg2_inputs_vanishes"]

    def test_def2_x_def2_out_of_range(self):
        """Def^2 x Def^2 -> Def^4: out of range."""
        result = nr_bracket_degree_analysis()
        entry = result["Def^2 x Def^2 -> Def^4"]
        assert not entry["target_in_range"]
        assert not entry["nr_bracket_potentially_nonzero"]

    def test_def1_x_def2_out_of_range(self):
        """Def^1 x Def^2 -> Def^3: out of range."""
        result = nr_bracket_degree_analysis()
        entry = result["Def^1 x Def^2 -> Def^3"]
        assert not entry["target_in_range"]

    def test_def0_x_def2_in_range(self):
        """Def^0 x Def^2 -> Def^2: in range (this is the adjoint action)."""
        result = nr_bracket_degree_analysis()
        entry = result["Def^0 x Def^2 -> Def^2"]
        assert entry["target_in_range"]
        assert entry["nr_bracket_potentially_nonzero"]

    def test_def0_x_def0_in_range(self):
        """Def^0 x Def^0 -> Def^0: in range (this is the Lie bracket)."""
        result = nr_bracket_degree_analysis()
        entry = result["Def^0 x Def^0 -> Def^0"]
        assert entry["target_in_range"]

    def test_def0_x_def1_in_range(self):
        """Def^0 x Def^1 -> Def^1: in range (adjoint on 2-cochains)."""
        result = nr_bracket_degree_analysis()
        entry = result["Def^0 x Def^1 -> Def^1"]
        assert entry["target_in_range"]


# ============================================================
# MC equation: genus-by-genus
# ============================================================

class TestMCGenusEquation:
    """MC equation analysis at specific genera."""

    def test_genus_2_rhs_vanishes(self):
        result = mc_equation_genus_g(2)
        assert result["rhs_vanishes"]
        assert result["theta_g_is_cocycle"]

    def test_genus_3_rhs_vanishes(self):
        result = mc_equation_genus_g(3)
        assert result["rhs_vanishes"]
        assert result["theta_g_is_cocycle"]

    def test_genus_4_rhs_vanishes(self):
        result = mc_equation_genus_g(4)
        assert result["rhs_vanishes"]
        assert result["theta_g_is_cocycle"]

    def test_genus_5_rhs_vanishes(self):
        result = mc_equation_genus_g(5)
        assert result["rhs_vanishes"]
        assert result["theta_g_is_cocycle"]

    def test_genus_3_partitions(self):
        """Genus 3: partitions are (1,2) and (1,1,1)."""
        result = mc_equation_genus_g(3)
        partitions = result["partitions"]
        assert (1, 2) in partitions
        assert (1, 1, 1) in partitions
        assert len(partitions) == 2

    def test_genus_4_partitions(self):
        """Genus 4 partitions: (1,3), (2,2), (1,1,2), (1,1,1,1)."""
        result = mc_equation_genus_g(4)
        partitions = result["partitions"]
        assert (1, 3) in partitions
        assert (2, 2) in partitions
        assert (1, 1, 2) in partitions
        assert (1, 1, 1, 1) in partitions
        assert len(partitions) == 4

    def test_genus_3_degree_targets(self):
        """At genus 3, l_2 targets degree 4, l_3 targets degree 5."""
        result = mc_equation_genus_g(3)
        assert result["l_2(1,2)_degree_target"] == 4
        assert result["l_3(1,1,1)_degree_target"] == 5

    def test_all_degree_targets_miss_H2(self):
        """No l_n term at any genus lands in H^2."""
        for g in range(2, 6):
            result = mc_equation_genus_g(g)
            for key, val in result.items():
                if key.endswith("_degree_target"):
                    assert val != 2, f"Genus {g}: {key} = {val} should not be 2"

    def test_all_strict_vanish(self):
        """Every partition's l_n contribution vanishes by strict dg Lie."""
        for g in range(2, 6):
            result = mc_equation_genus_g(g)
            for key, val in result.items():
                if key.endswith("_strict_vanishes"):
                    assert val, f"Genus {g}: {key} should be True"


# ============================================================
# Higher genus combined verification
# ============================================================

class TestHigherGenusCombined:
    """Combined verification across all three arguments."""

    def test_epsilon_2_vanishes(self):
        result = higher_genus_vanishing()
        assert result["epsilon_2_vanishes"]

    def test_epsilon_3_vanishes(self):
        result = higher_genus_vanishing()
        assert result["epsilon_3_vanishes"]

    def test_epsilon_4_vanishes(self):
        result = higher_genus_vanishing()
        assert result["epsilon_4_vanishes"]

    def test_epsilon_5_vanishes(self):
        result = higher_genus_vanishing()
        assert result["epsilon_5_vanishes"]

    def test_all_three_arguments_agree(self):
        """All three arguments give vanishing at each genus."""
        result = higher_genus_vanishing()
        for g in range(2, 6):
            three_args = result[f"epsilon_{g}_three_arguments"]
            assert three_args["strict_dg_lie"]
            assert three_args["degree_obstruction"]
            assert three_args["antisymmetry_for_l3"]


# ============================================================
# Genus partition helper
# ============================================================

class TestGenusPartitions:
    """Verify genus partition enumeration."""

    def test_partitions_of_2(self):
        p = _genus_partitions(2)
        assert p == [(1, 1)]

    def test_partitions_of_3(self):
        p = _genus_partitions(3)
        assert set(p) == {(1, 2), (1, 1, 1)}

    def test_partitions_of_4(self):
        p = _genus_partitions(4)
        expected = {(1, 3), (2, 2), (1, 1, 2), (1, 1, 1, 1)}
        assert set(p) == expected

    def test_partitions_of_5(self):
        p = _genus_partitions(5)
        expected = {
            (1, 4), (2, 3),           # 2 parts
            (1, 1, 3), (1, 2, 2),     # 3 parts
            (1, 1, 1, 2),             # 4 parts
            (1, 1, 1, 1, 1),          # 5 parts
        }
        assert set(p) == expected

    def test_partitions_sum_correctly(self):
        """Every partition of g sums to g."""
        for g in range(2, 7):
            for p in _genus_partitions(g):
                assert sum(p) == g, f"Partition {p} should sum to {g}"

    def test_partitions_have_at_least_2_parts(self):
        """All partitions have >= 2 parts (single-part is the LHS)."""
        for g in range(2, 7):
            for p in _genus_partitions(g):
                assert len(p) >= 2, f"Partition {p} should have >= 2 parts"


# ============================================================
# Integration test: full summary
# ============================================================

class TestSummary:
    """Integration test: the complete genus-3 correction computation."""

    def test_summary_runs(self):
        summary = genus3_killing_correction_summary()
        assert summary is not None

    def test_infrastructure_valid(self):
        summary = genus3_killing_correction_summary()
        infra = summary["infrastructure"]
        for name, ok in infra["d_squared_zero"].items():
            assert ok, f"d^2 failed: {name}"
        for name, ok in infra["sdr_verified"].items():
            assert ok, f"SDR failed: {name}"
        assert infra["phi_antisymmetric"]
        assert infra["phi_normalization"] == Fraction(-2)

    def test_all_three_arguments_pass(self):
        summary = genus3_killing_correction_summary()
        # Argument 1
        assert summary["argument_1_strict_dg_lie"]["epsilon_g_vanishes_all_g"]
        # Argument 2
        for g in range(2, 6):
            assert summary["argument_2_degree_obstruction"][f"genus_{g}_vanishes"]
        # Argument 3
        assert summary["argument_3_antisymmetry"]["l3_vanishes_by_antisymmetry"]

    def test_chain_level_verification(self):
        summary = genus3_killing_correction_summary()
        chain = summary["chain_level_tree_formula"]
        assert chain["transferred_l3_phi_phi_phi"] == Fraction(0)

    def test_genus_3_mc_equation(self):
        summary = genus3_killing_correction_summary()
        mc3 = summary["mc_equation_by_genus"]["genus_3"]
        assert mc3["rhs_vanishes"]
        assert mc3["theta_g_is_cocycle"]

    def test_genus_4_mc_equation(self):
        summary = genus3_killing_correction_summary()
        mc4 = summary["mc_equation_by_genus"]["genus_4"]
        assert mc4["rhs_vanishes"]

    def test_genus_5_mc_equation(self):
        summary = genus3_killing_correction_summary()
        mc5 = summary["mc_equation_by_genus"]["genus_5"]
        assert mc5["rhs_vanishes"]

    def test_conclusion_text(self):
        summary = genus3_killing_correction_summary()
        assert "epsilon_g = 0" in summary["conclusion"]
        assert "three independent arguments" in summary["conclusion"].lower()

    def test_higher_genus_all_vanish(self):
        summary = genus3_killing_correction_summary()
        for g in range(2, 6):
            assert summary["higher_genus"][f"epsilon_{g}_vanishes"]
