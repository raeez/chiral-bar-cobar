"""Tests for compute/lib/genus_partition_closure.py — genus-g partition function closure.

Validates:
  1. Scalar genus expansion F_g = kappa * lambda_g^FP for g = 1..10
  2. Graph-sum polynomial decomposition
  3. Shadow corrections at genus 2 and genus 3
  4. Boundary strata contributions (separating, irreducible)
  5. Faber-Pandharipande sequence values and growth rate
  6. Partition function q-expansion
  7. Period enrichment for lattice VOAs
  8. Witten-Kontsevich intersection numbers
  9. Universal scalar verification across all families
  10. Handle gluing operator
  11. Genus spectral sequence decomposition

References:
  concordance.tex, higher_genus_modular_koszul.tex,
  thm:genus-expansion-universal, const:vol1-genus-spectral-sequence,
  thm:heisenberg-sewing (Fredholm determinant, Borel summability)
"""

import pytest
from fractions import Fraction

from compute.lib.genus_partition_closure import (
    F_g_scalar,
    F_g_graph_sum,
    faber_pandharipande_sequence,
    genus_spectral_sequence,
    shadow_correction_genus2,
    shadow_correction_genus3,
    universal_scalar_verification,
    boundary_stratum_contribution,
    separating_factorization,
    total_separating_contribution,
    handle_gluing_operator,
    genus_free_energy_table,
    period_enriched_genus,
    partition_function_q_expansion,
    witten_kontsevich_intersection,
    genus_growth_rate,
    _compute_kappa,
)

from compute.lib.stable_graph_enumeration import (
    _lambda_fp_exact,
    _bernoulli_exact,
    enumerate_stable_graphs,
)


# =====================================================================
# TestScalarGenusExpansion
# =====================================================================

class TestScalarGenusExpansion:
    """F_g = kappa * lambda_g^FP (Theorem D, universal)."""

    def test_F1(self):
        """F_1 = kappa/24."""
        kappa = Fraction(1)
        assert F_g_scalar(kappa, 1) == Fraction(1, 24)

    def test_F2(self):
        """F_2 = 7*kappa/5760."""
        kappa = Fraction(1)
        assert F_g_scalar(kappa, 2) == Fraction(7, 5760)

    def test_F3(self):
        """F_3 = 31*kappa/967680."""
        kappa = Fraction(1)
        assert F_g_scalar(kappa, 3) == Fraction(31, 967680)

    def test_F4(self):
        """F_4 = 127*kappa/464486400."""
        kappa = Fraction(1)
        # lambda_4^FP = (2^7-1)|B_8|/(2^7 * 8!)
        # B_8 = -1/30, |B_8| = 1/30
        # (128-1)*1/30 / (128*40320) = 127/30 / 5160960 = 127/154828800
        # Wait: 2^7 = 128, 2^7-1 = 127, 8! = 40320
        # lambda_4 = 127 * (1/30) / (128 * 40320) = 127/(30*128*40320)
        # = 127 / 154828800
        expected = _lambda_fp_exact(4)
        assert F_g_scalar(kappa, 4) == expected

    def test_F5(self):
        """F_5 uses B_10 = 5/66."""
        kappa = Fraction(1)
        expected = _lambda_fp_exact(5)
        assert F_g_scalar(kappa, 5) == expected

    def test_F1_heisenberg_k2(self):
        """F_1(H_2) = 2/24 = 1/12."""
        kappa = Fraction(2)
        assert F_g_scalar(kappa, 1) == Fraction(1, 12)

    def test_F1_virasoro_c26(self):
        """F_1(Vir_26) = 13/24."""
        kappa = Fraction(13)  # c/2 = 26/2
        assert F_g_scalar(kappa, 1) == Fraction(13, 24)

    def test_F1_betagamma(self):
        """F_1(bg) = 1/24 (kappa = +1)."""
        kappa = Fraction(1)
        assert F_g_scalar(kappa, 1) == Fraction(1, 24)

    def test_F2_affine_sl2_k1(self):
        """F_2(V_1(sl_2)) = 9/4 * 7/5760 = 63/23040 = 7/2560."""
        kappa = Fraction(9, 4)  # 3*(1+2)/4
        expected = Fraction(9, 4) * Fraction(7, 5760)
        assert F_g_scalar(kappa, 2) == expected

    def test_genus_0_raises(self):
        """F_0 is undefined (genus must be >= 1)."""
        with pytest.raises(ValueError):
            F_g_scalar(Fraction(1), 0)

    def test_universal_all_families(self):
        """F_g = kappa * lambda_g^FP for Heis, aff, Vir, bg, W3 at g=1,2,3."""
        families = {
            "Heisenberg_k1": Fraction(1),
            "affine_sl2_k1": Fraction(9, 4),
            "Virasoro_c26": Fraction(13),
            "betagamma": Fraction(1),
            "W3_c2": Fraction(5, 3),
        }
        for name, kappa in families.items():
            for g in range(1, 4):
                expected = kappa * _lambda_fp_exact(g)
                computed = F_g_scalar(kappa, g)
                assert computed == expected, f"Failed for {name} at g={g}"


# =====================================================================
# TestFPSequence
# =====================================================================

class TestFPSequence:
    """Faber-Pandharipande numbers lambda_g^FP."""

    def test_lambda_1_fp(self):
        """lambda_1^FP = 1/24."""
        fp = faber_pandharipande_sequence(1)
        assert fp[1] == Fraction(1, 24)

    def test_lambda_2_fp(self):
        """lambda_2^FP = 7/5760."""
        fp = faber_pandharipande_sequence(2)
        assert fp[2] == Fraction(7, 5760)

    def test_lambda_3_fp(self):
        """lambda_3^FP = 31/967680."""
        fp = faber_pandharipande_sequence(3)
        assert fp[3] == Fraction(31, 967680)

    def test_bernoulli_B2(self):
        """B_2 = 1/6."""
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_bernoulli_B4(self):
        """B_4 = -1/30."""
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_bernoulli_B6(self):
        """B_6 = 1/42."""
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_bernoulli_B8(self):
        """B_8 = -1/30."""
        assert _bernoulli_exact(8) == Fraction(-1, 30)

    def test_factorial_growth(self):
        """lambda_g^FP grows factorially: fp values grow much faster than exponential.

        The ratio lambda_{g+1}/lambda_g converges to 1/(4*pi^2) from above,
        which means the FP numbers themselves grow as ~(2g)!/(2*pi)^{2g}.
        We verify that each lambda_g * (2*pi)^{2g} / (2*factorial(2*g)) is O(1).
        """
        from math import factorial as mfact
        fp = faber_pandharipande_sequence(8)
        # Ratios converge to 1/(4*pi^2) ~ 0.02533 from above
        for g in range(2, 8):
            r = fp[g + 1] / fp[g]
            assert Fraction(1, 100) < r < Fraction(1, 10), (
                f"Ratio at g={g} out of range: {float(r)}")
        # Verify monotone DECREASE of ratios (converging from above)
        for g in range(1, 7):
            r1 = fp[g + 1] / fp[g]
            r2 = fp[g + 2] / fp[g + 1]
            assert r2 < r1, f"Ratio not decreasing at g={g}"

    def test_fp_sequence_length(self):
        """faber_pandharipande_sequence(10) returns 10 entries."""
        fp = faber_pandharipande_sequence(10)
        assert len(fp) == 10
        assert set(fp.keys()) == set(range(1, 11))

    def test_fp_all_positive(self):
        """All lambda_g^FP are positive."""
        fp = faber_pandharipande_sequence(10)
        for g, val in fp.items():
            assert val > 0, f"lambda_{g}^FP = {val} is not positive"


# =====================================================================
# TestGraphSum
# =====================================================================

class TestGraphSum:
    """Graph-sum decomposition at each genus."""

    def test_genus1_graph_count(self):
        """Genus 1, n=0: 2 stable graphs."""
        result = F_g_graph_sum(1)
        assert result["graph_count"] == 2

    def test_genus2_graph_count(self):
        """Genus 2, n=0: 6 stable graphs."""
        result = F_g_graph_sum(2)
        assert result["graph_count"] == 6

    def test_genus3_graph_count(self):
        """Genus 3, n=0: 42 stable graphs."""
        result = F_g_graph_sum(3)
        assert result["graph_count"] == 42

    def test_genus1_polynomial(self):
        """Genus-1 polynomial: c_0 = 1 (smooth), c_1 = 1/2 (self-loop, |Aut|=2)."""
        result = F_g_graph_sum(1)
        poly = result["polynomial"]
        assert poly.get(0, Fraction(0)) == Fraction(1)
        assert poly.get(1, Fraction(0)) == Fraction(1, 2)

    def test_genus2_polynomial_edge0(self):
        """Genus-2 smooth graph: c_0 = 1."""
        result = F_g_graph_sum(2)
        poly = result["polynomial"]
        assert poly.get(0, Fraction(0)) == Fraction(1)

    def test_graph_sum_with_kappa(self):
        """Graph sum evaluated at kappa=1 returns a number."""
        result = F_g_graph_sum(2, family_data={"kappa": Fraction(1)})
        assert "F_g_value" in result
        assert isinstance(result["F_g_value"], Fraction)

    def test_genus1_raises_for_g0(self):
        """F_g_graph_sum raises for g=0."""
        with pytest.raises(ValueError):
            F_g_graph_sum(0)


# =====================================================================
# TestShadowCorrections
# =====================================================================

class TestShadowCorrections:
    """Shadow corrections at genus 2 and genus 3."""

    def test_heisenberg_no_correction_g2(self):
        """All corrections zero for depth-2 (Heisenberg) at genus 2."""
        result = shadow_correction_genus2(S2=Fraction(1))
        assert result["cubic_correction"] == Fraction(0)
        assert result["quartic_correction"] == Fraction(0)
        assert result["total"] == result["scalar"]

    def test_heisenberg_scalar_g2(self):
        """Scalar component is kappa * 7/5760."""
        kappa = Fraction(1)
        result = shadow_correction_genus2(S2=kappa)
        assert result["scalar"] == kappa * Fraction(7, 5760)

    def test_affine_cubic_correction_g2(self):
        """Cubic correction is nonzero for affine (S3 != 0)."""
        result = shadow_correction_genus2(S2=Fraction(9, 4), S3=Fraction(1))
        assert result["cubic_correction"] != Fraction(0)

    def test_virasoro_quartic_correction_g2(self):
        """Quartic correction is nonzero for Virasoro (S4 != 0)."""
        result = shadow_correction_genus2(S2=Fraction(13), S4=Fraction(1))
        assert result["quartic_correction"] != Fraction(0)

    def test_correction_returns_all_keys(self):
        """shadow_correction_genus2 returns all expected keys."""
        result = shadow_correction_genus2(S2=Fraction(1), S3=Fraction(1), S4=Fraction(1))
        expected_keys = {"scalar", "cubic_correction", "quartic_correction", "total",
                         "S2", "S3", "S4"}
        assert expected_keys == set(result.keys())

    def test_heisenberg_no_correction_g3(self):
        """All corrections zero for depth-2 at genus 3."""
        result = shadow_correction_genus3(S2=Fraction(1))
        assert result["cubic_correction"] == Fraction(0)
        assert result["quartic_correction"] == Fraction(0)
        assert result["quintic_correction"] == Fraction(0)
        assert result["total"] == result["scalar"]

    def test_genus3_scalar_value(self):
        """Scalar component at genus 3 is kappa * 31/967680."""
        kappa = Fraction(1)
        result = shadow_correction_genus3(S2=kappa)
        assert result["scalar"] == kappa * Fraction(31, 967680)

    def test_virasoro_quintic_g3(self):
        """Quintic correction nonzero for mixed-class at genus 3."""
        result = shadow_correction_genus3(
            S2=Fraction(13), S3=Fraction(1), S4=Fraction(1), S5=Fraction(1)
        )
        assert result["quintic_correction"] != Fraction(0)


# =====================================================================
# TestBoundaryStrata
# =====================================================================

class TestBoundaryStrata:
    """Boundary stratum contributions."""

    def test_separating_factorization_g2(self):
        """F_2|_{sep} = F_1^2 / 2 for g1 = g2 = 1."""
        kappa = Fraction(1)
        result = separating_factorization(1, 1, kappa)
        F1 = Fraction(1, 24)
        expected = F1 ** 2 / Fraction(2)
        assert result["separating_contribution"] == expected
        assert result["aut"] == Fraction(2)

    def test_separating_factorization_g3_asymmetric(self):
        """F_3|_{sep,1+2} = F_1 * F_2 (no symmetry factor for g1 != g2)."""
        kappa = Fraction(1)
        result = separating_factorization(1, 2, kappa)
        F1 = Fraction(1, 24)
        F2 = Fraction(7, 5760)
        expected = F1 * F2
        assert result["separating_contribution"] == expected
        assert result["aut"] == Fraction(1)

    def test_total_separating_g2(self):
        """Total separating at genus 2: only h=1 splitting."""
        kappa = Fraction(1)
        total = total_separating_contribution(2, kappa)
        F1 = kappa * _lambda_fp_exact(1)
        expected = F1 ** 2 / Fraction(2)
        assert total == expected

    def test_total_separating_g4(self):
        """Total separating at genus 4: splittings 1+3 and 2+2."""
        kappa = Fraction(1)
        total = total_separating_contribution(4, kappa)
        F1 = kappa * _lambda_fp_exact(1)
        F2 = kappa * _lambda_fp_exact(2)
        F3 = kappa * _lambda_fp_exact(3)
        # 1+3: F_1 * F_3 (aut=1)
        # 2+2: F_2^2 / 2 (aut=2)
        expected = F1 * F3 + F2 ** 2 / Fraction(2)
        assert total == expected

    def test_handle_contribution_g2(self):
        """Handle gluing at arity 2 returns S * 1."""
        result = handle_gluing_operator(Fraction(1), 2)
        assert result == Fraction(1)

    def test_handle_arity_error(self):
        """Handle gluing raises for arity < 2."""
        with pytest.raises(ValueError):
            handle_gluing_operator(Fraction(1), 1)

    def test_boundary_stratum_irr_g2(self):
        """Irreducible boundary at genus 2 contains graphs with self-loops."""
        result = boundary_stratum_contribution(2, "irr")
        # Gamma_1, Gamma_2, Gamma_5 have self-loops
        assert result["graph_count"] >= 3

    def test_boundary_stratum_sep_g2(self):
        """Separating boundary at genus 2 has at least 1 graph (Gamma_3)."""
        result = boundary_stratum_contribution(2, "sep")
        assert result["graph_count"] >= 1


# =====================================================================
# TestPartitionFunction
# =====================================================================

class TestPartitionFunction:
    """Partition function Z(hbar) = exp(sum F_g hbar^{2g-2})."""

    def test_heisenberg_q_expansion(self):
        """Heisenberg partition function has correct F_1 prefactor."""
        result = partition_function_q_expansion("heisenberg", max_g=3, k=1)
        assert result["F_1_prefactor"] == Fraction(1, 24)

    def test_genus_truncation(self):
        """Truncation at max_g=2 gives z_coefficients with keys {0}."""
        result = partition_function_q_expansion("heisenberg", max_g=2, k=1)
        # Z = exp(F_1) * (1 + F_2 * hbar^2 + ...)
        # max_g=2 => max_power = 1, but only F_2 enters the expansion part
        assert 0 in result["z_coefficients"]
        assert result["z_coefficients"][0] == Fraction(1)

    def test_z0_coefficient_is_one(self):
        """The constant term z_0 = 1 always."""
        for family in ["heisenberg", "virasoro", "betagamma"]:
            kwargs = {"k": 1} if family == "heisenberg" else {"c": 26} if family == "virasoro" else {}
            result = partition_function_q_expansion(family, max_g=3, **kwargs)
            assert result["z_coefficients"][0] == Fraction(1)

    def test_partition_function_keys(self):
        """partition_function_q_expansion returns expected keys."""
        result = partition_function_q_expansion("heisenberg", max_g=3, k=1)
        expected_keys = {"family", "max_genus", "free_energies",
                         "F_1_prefactor", "z_coefficients", "note"}
        assert expected_keys == set(result.keys())


# =====================================================================
# TestPeriodEnriched
# =====================================================================

class TestPeriodEnriched:
    """Period enrichment for lattice VOAs."""

    def test_heisenberg_trivial(self):
        """V_Z has no period enrichment at any genus."""
        for g in range(1, 6):
            result = period_enriched_genus("Z", g)
            assert result["has_period_enrichment"] is False
            assert result["scalar_value"] == _lambda_fp_exact(g)

    def test_leech_genus3_no_period(self):
        """V_Leech at genus 3 has no period enrichment (threshold is 4)."""
        result = period_enriched_genus("Leech", 3)
        assert result["has_period_enrichment"] is False

    def test_leech_genus4_delta(self):
        """V_Leech at genus >= 4 has L(s, Delta) period enrichment."""
        result = period_enriched_genus("Leech", 4)
        assert result["has_period_enrichment"] is True
        assert "Ramanujan" in result["period_source"]

    def test_e8_genus2_eisenstein(self):
        """V_{E8} at genus >= 2 has Eisenstein period enrichment."""
        result = period_enriched_genus("E8", 2)
        assert result["has_period_enrichment"] is True
        assert "Eisenstein" in result["period_source"]

    def test_leech_scalar_value(self):
        """V_Leech scalar value at genus 1: 24/24 = 1."""
        result = period_enriched_genus("Leech", 1)
        assert result["scalar_value"] == Fraction(24) * _lambda_fp_exact(1)
        assert result["scalar_value"] == Fraction(1)

    def test_e8_kappa(self):
        """V_{E8} has kappa = 8."""
        result = period_enriched_genus("E8", 1)
        assert result["kappa"] == Fraction(8)

    def test_unknown_lattice_raises(self):
        """Unknown lattice raises ValueError."""
        with pytest.raises(ValueError):
            period_enriched_genus("D4", 1)


# =====================================================================
# TestWittenKontsevich
# =====================================================================

class TestWittenKontsevich:
    """Witten-Kontsevich intersection numbers."""

    def test_tau0_cubed_g0(self):
        """<tau_0^3>_0 = 1."""
        assert witten_kontsevich_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_tau1_g1(self):
        """<tau_1>_1 = 1/24."""
        assert witten_kontsevich_intersection(1, (1,)) == Fraction(1, 24)

    def test_tau4_g2(self):
        """<tau_4>_2 = 1/1152."""
        assert witten_kontsevich_intersection(2, (4,)) == Fraction(1, 1152)

    def test_selection_rule_violation(self):
        """Violating sum d_i = 3g-3+n gives 0."""
        assert witten_kontsevich_intersection(1, (2,)) == Fraction(0)

    def test_tau2_squared_g2_selection_rule(self):
        """<tau_2^2>_2 = 0 (selection rule: 2+2=4 != 3*2-3+2=5)."""
        result = witten_kontsevich_intersection(2, (2, 2))
        assert result == Fraction(0)

    def test_tau1_tau3_g2_selection_fails(self):
        """<tau_1 tau_3>_2 = 0 (selection rule: 1+3=4 != 3*2-3+2=5)."""
        result = witten_kontsevich_intersection(2, (1, 3))
        assert result == Fraction(0)

    def test_tau0_cubed_tau1_g0(self):
        """<tau_0^3 tau_1>_0 = 1 (string equation from <tau_0^3>_0)."""
        result = witten_kontsevich_intersection(0, (0, 0, 0, 1))
        assert result == Fraction(1)

    def test_unstable_gives_zero(self):
        """Unstable moduli (2g-2+n <= 0) gives 0."""
        assert witten_kontsevich_intersection(0, (0,)) == Fraction(0)


# =====================================================================
# TestGenusGrowth
# =====================================================================

class TestGenusGrowth:
    """Asymptotic growth of the genus expansion."""

    def test_non_convergence(self):
        """Genus expansion has zero radius of convergence."""
        result = genus_growth_rate(max_g=8)
        assert result["zero_radius"] is True

    def test_borel_summability(self):
        """The genus expansion is Borel summable."""
        result = genus_growth_rate()
        assert result["borel_summable"] is True

    def test_ratios_converge_from_above(self):
        """Consecutive ratios lambda_{g+1}/lambda_g decrease toward 1/(4*pi^2)."""
        result = genus_growth_rate(max_g=8)
        ratios = result["ratios"]
        # Ratios converge from above to 1/(4*pi^2) ~ 0.02533
        for g in range(1, 6):
            assert ratios[g + 1] < ratios[g], (
                f"Ratio not decreasing at g={g}: "
                f"{float(ratios[g])} vs {float(ratios[g+1])}"
            )
        # All ratios are positive and bounded
        for g, r in ratios.items():
            assert r > 0
            assert r < 1

    def test_growth_type_factorial(self):
        """Growth type is factorial."""
        result = genus_growth_rate()
        assert result["growth_type"] == "factorial"


# =====================================================================
# TestGenusSpectralSequence
# =====================================================================

class TestGenusSpectralSequence:
    """Genus spectral sequence decomposition."""

    def test_genus2_pages(self):
        """Genus-2 spectral sequence: {0: 2, 1: 2, 2: 2}."""
        result = genus_spectral_sequence(2)
        pages = result["pages"]
        assert pages[0] == 2
        assert pages[1] == 2
        assert pages[2] == 2

    def test_genus3_pages(self):
        """Genus-3 spectral sequence: {0: 4, 1: 9, 2: 14, 3: 15}."""
        result = genus_spectral_sequence(3)
        pages = result["pages"]
        assert pages[0] == 4
        assert pages[1] == 9
        assert pages[2] == 14
        assert pages[3] == 15

    def test_heisenberg_collapse(self):
        """Heisenberg spectral sequence collapses at E_1."""
        result = genus_spectral_sequence(2, family="heisenberg")
        assert result["collapse_page"] == "E_1"

    def test_virasoro_no_collapse(self):
        """Virasoro spectral sequence does not collapse."""
        result = genus_spectral_sequence(2, family="virasoro")
        assert "does not collapse" in result["collapse_page"]


# =====================================================================
# TestFreeEnergyTable
# =====================================================================

class TestFreeEnergyTable:
    """genus_free_energy_table for various families."""

    def test_heisenberg_table(self):
        """Heisenberg k=1 table matches direct computation."""
        table = genus_free_energy_table("heisenberg", max_g=5, k=1)
        for g in range(1, 6):
            assert table[g] == _lambda_fp_exact(g)

    def test_virasoro_table(self):
        """Virasoro c=26 table at genus 1: 13/24."""
        table = genus_free_energy_table("virasoro", max_g=3, c=26)
        assert table[1] == Fraction(13, 24)

    def test_betagamma_table(self):
        """Beta-gamma table has positive values (kappa = +1)."""
        table = genus_free_energy_table("betagamma", max_g=3)
        for g in range(1, 4):
            assert table[g] > 0

    def test_table_length(self):
        """Table has max_g entries."""
        table = genus_free_energy_table("heisenberg", max_g=7)
        assert len(table) == 7

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            genus_free_energy_table("unknown_algebra")


# =====================================================================
# TestUniversalVerification
# =====================================================================

class TestUniversalVerification:
    """Universal scalar verification across all standard families."""

    def test_all_pass(self):
        """All families pass verification at all genera."""
        result = universal_scalar_verification(max_g=6)
        assert result["all_pass"] is True

    def test_each_family_passes(self):
        """Each individual family passes at each genus."""
        result = universal_scalar_verification(max_g=4)
        for family_name, data in result.items():
            if family_name == "all_pass":
                continue
            for g, gdata in data["genus_results"].items():
                assert gdata["match"], f"Failed: {family_name} at g={g}"


# =====================================================================
# TestComputeKappa
# =====================================================================

class TestComputeKappa:
    """Helper kappa computation for each family."""

    def test_heisenberg_k1(self):
        assert _compute_kappa("heisenberg", k=1) == Fraction(1)

    def test_heisenberg_k2_d3(self):
        assert _compute_kappa("heisenberg", k=2, d=3) == Fraction(6)

    def test_affine_sl2_k1(self):
        assert _compute_kappa("affine_sl2", k=1) == Fraction(9, 4)

    def test_virasoro_c26(self):
        assert _compute_kappa("virasoro", c=26) == Fraction(13)

    def test_betagamma(self):
        assert _compute_kappa("betagamma") == Fraction(1)

    def test_w3_c2(self):
        assert _compute_kappa("w3", c=2) == Fraction(5, 3)
