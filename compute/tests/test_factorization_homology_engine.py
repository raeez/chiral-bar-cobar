"""Tests for compute/lib/factorization_homology_engine.py.

Validates the factorization homology engine: the cross-volume bridge
connecting Vol I bar-cobar machinery to Vol II factorization algebra framework.

Coverage:
  1. FH at genus 0 (concentration for all standard families)
  2. FH concentration criterion (= Koszulness)
  3. Excision / sewing factorization
  4. Verlinde formula (sl_2, sl_3)
  5. Boundary acyclicity at low arity
  6. Cross-volume check (Vol I F_g = Vol II integral_{Sigma_g})
  7. Critical level (NOT concentrated)
  8. Koszulness 12-criteria status
  9. Genus dependence and determinant line
  10. Heisenberg explicit FH

References:
  thm:fh-concentration-koszulness (bar_cobar_adjunction_inversion.tex)
  thm:fm-boundary-acyclicity (bar_cobar_adjunction_inversion.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  concordance.tex (sec:concordance-koszulness-programme)
"""

import pytest
from fractions import Fraction

from compute.lib.factorization_homology_engine import (
    fh_genus0,
    fh_genus1,
    fh_genus_g,
    fh_concentration_check,
    fh_koszulness_criterion,
    fh_excision_verify,
    fh_boundary_acyclicity_check,
    fh_conformal_blocks,
    verlinde_formula,
    fh_determinant_line,
    fh_genus_dependence_table,
    fh_cross_volume_check,
    fh_critical_level_check,
    heisenberg_fh_explicit,
    koszulness_12_criteria_status,
)
from compute.lib.stable_graph_enumeration import _lambda_fp_exact


# =====================================================================
# TestFHGenus0 — concentration at genus 0
# =====================================================================

class TestFHGenus0:
    """integral_{P^1} A concentrated in degree 0 for Koszul algebras."""

    def test_heisenberg_concentrated(self):
        """Heisenberg: H^0 = k, H^i = 0 for i != 0."""
        result = fh_genus0("heisenberg")
        assert result["concentrated"] is True
        assert result["H0_dim"] == 1
        assert result["koszul"] is True

    def test_virasoro_concentrated(self):
        """Virasoro: H^0 = k (vacuum), H^i = 0 for i != 0."""
        result = fh_genus0("virasoro")
        assert result["concentrated"] is True
        assert result["H0_dim"] == 1

    def test_affine_sl2_concentrated(self):
        """Affine sl_2 at generic k: concentrated."""
        result = fh_genus0("affine_sl2", k=1)
        assert result["concentrated"] is True
        assert result["koszul"] is True

    def test_betagamma_concentrated(self):
        """beta-gamma: H^0 = k, concentrated."""
        result = fh_genus0("betagamma")
        assert result["concentrated"] is True
        assert result["H0_dim"] == 1

    def test_w3_concentrated(self):
        """W_3: concentrated in degree 0."""
        result = fh_genus0("w3")
        assert result["concentrated"] is True

    def test_free_fermion_concentrated(self):
        """Free fermion: concentrated."""
        result = fh_genus0("free_fermion")
        assert result["concentrated"] is True

    def test_lattice_concentrated(self):
        """Lattice VOA: concentrated."""
        result = fh_genus0("lattice")
        assert result["concentrated"] is True

    def test_all_standard_koszul(self):
        """All standard families are concentrated at genus 0."""
        families = ["heisenberg", "virasoro", "betagamma", "w3",
                     "free_fermion", "lattice"]
        for fam in families:
            result = fh_genus0(fam)
            assert result["concentrated"] is True, f"{fam} not concentrated"
            assert result["koszul"] is True, f"{fam} not Koszul"


# =====================================================================
# TestFHConcentration — concentration at all genera
# =====================================================================

class TestFHConcentration:
    """FH concentration = Koszulness criterion."""

    def test_koszul_implies_concentrated(self):
        """For Koszul algebras, FH concentrated at all genera."""
        result = fh_concentration_check("heisenberg", max_g=3)
        assert result["all_concentrated"] is True

    def test_concentration_at_genus1(self):
        """Genus-1: F_1 = kappa/24, concentrated."""
        result = fh_genus1("heisenberg", k=1)
        assert result["F1"] == Fraction(1, 24)
        assert result["concentrated"] is True

    def test_concentration_at_genus2(self):
        """Genus-2: F_2 = 7*kappa/5760, concentrated."""
        result = fh_genus_g("heisenberg", 2, k=1)
        assert result["F_g"] == Fraction(7, 5760)
        assert result["scalar_match"] is True

    def test_concentration_at_genus3(self):
        """Genus-3: F_3 = 31*kappa/967680, concentrated."""
        result = fh_genus_g("heisenberg", 3, k=1)
        assert result["F_g"] == Fraction(31, 967680)
        assert result["scalar_match"] is True

    def test_virasoro_concentrated_all_genera(self):
        """Virasoro at c=26: concentrated at genera 1,2,3."""
        result = fh_concentration_check("virasoro", max_g=3, c=26)
        assert result["all_concentrated"] is True

    def test_betagamma_concentrated_all_genera(self):
        """beta-gamma: concentrated at genera 1,2,3."""
        result = fh_concentration_check("betagamma", max_g=3)
        assert result["all_concentrated"] is True

    def test_affine_sl2_concentrated_all_genera(self):
        """Affine sl_2 at k=1: concentrated at genera 1,2,3."""
        result = fh_concentration_check("affine_sl2", max_g=3, k=1)
        assert result["all_concentrated"] is True

    def test_koszulness_criterion_heisenberg(self):
        """Full Koszulness criterion for Heisenberg."""
        result = fh_koszulness_criterion("heisenberg", k=1)
        assert result["koszul"] is True
        assert result["genus0_concentrated"] is True
        assert result["genus1_concentrated"] is True
        assert result["higher_concentrated"] is True

    def test_koszulness_criterion_virasoro(self):
        """Full Koszulness criterion for Virasoro."""
        result = fh_koszulness_criterion("virasoro", c=26)
        assert result["koszul"] is True


# =====================================================================
# TestFHExcision — sewing / excision
# =====================================================================

class TestFHExcision:
    """Excision: separating-node contribution factors."""

    def test_sewing_g1_g1(self):
        """integral_{Sigma_2}|_{sep} = F_1 * F_1 / 2 (separating node, g1=g2=1)."""
        result = fh_excision_verify("heisenberg", 1, 1, k=1)
        kappa = Fraction(1)
        F1 = kappa * Fraction(1, 24)
        expected_sep = F1 * F1 / 2  # symmetry factor 2 since g1=g2
        assert result["separating_contribution"] == expected_sep
        assert result["symmetry_factor"] == Fraction(2)
        assert result["factors_correctly"] is True

    def test_sewing_g1_g2(self):
        """integral_{Sigma_3}|_{Delta_1} = F_1 * F_2 (no symmetry)."""
        result = fh_excision_verify("heisenberg", 1, 2, k=1)
        assert result["symmetry_factor"] == Fraction(1)
        assert result["factors_correctly"] is True
        F1 = Fraction(1, 24)
        F2 = Fraction(7, 5760)
        assert result["separating_contribution"] == F1 * F2

    def test_sewing_g2_g2(self):
        """integral_{Sigma_4}|_{Delta_2} = F_2 * F_2 / 2 (symmetry)."""
        result = fh_excision_verify("heisenberg", 2, 2, k=1)
        assert result["symmetry_factor"] == Fraction(2)
        assert result["factors_correctly"] is True

    def test_separating_fraction_genus2(self):
        """Separating contribution is a proper fraction of F_total at genus 2."""
        result = fh_excision_verify("heisenberg", 1, 1, k=1)
        frac = result["fraction_of_total"]
        assert frac is not None
        # Separating contribution is F_1^2/2 = (1/24)^2/2 = 1/1152
        # F_2 = 7/5760
        # Fraction = (1/1152) / (7/5760) = 5760/(7*1152) = 5/7
        assert frac == Fraction(5, 7)

    def test_excision_virasoro(self):
        """Excision for Virasoro at c=26, g1=1, g2=1."""
        result = fh_excision_verify("virasoro", 1, 1, c=26)
        assert result["factors_correctly"] is True
        assert result["kappa"] == Fraction(13)

    def test_excision_affine(self):
        """Excision for affine sl_2 at k=1, g1=1, g2=1."""
        result = fh_excision_verify("affine_sl2", 1, 1, k=1)
        assert result["factors_correctly"] is True
        assert result["kappa"] == Fraction(9, 4)


# =====================================================================
# TestVerlinde — Verlinde formula verification
# =====================================================================

class TestVerlinde:
    """Verlinde formula for sl_2 and sl_3."""

    def test_sl2_k1_g0(self):
        """sl_2, k=1, g=0: dim = 1."""
        assert verlinde_formula("sl2", 1, 0) == 1

    def test_sl2_k1_g1(self):
        """sl_2, k=1, g=1: dim = k+1 = 2."""
        assert verlinde_formula("sl2", 1, 1) == 2

    def test_sl2_k2_g0(self):
        """sl_2, k=2, g=0: dim = 1."""
        assert verlinde_formula("sl2", 2, 0) == 1

    def test_sl2_k2_g1(self):
        """sl_2, k=2, g=1: dim = k+1 = 3."""
        assert verlinde_formula("sl2", 2, 1) == 3

    def test_sl2_k1_g2(self):
        """sl_2, k=1, g=2: dim = 4 (Verlinde, Beauville normalization)."""
        result = verlinde_formula("sl2", 1, 2)
        assert result == 4

    def test_sl2_k2_g2(self):
        """sl_2, k=2, g=2: dim = 10 (Verlinde)."""
        result = verlinde_formula("sl2", 2, 2)
        assert result == 10

    def test_sl2_k3_g1(self):
        """sl_2, k=3, g=1: dim = k+1 = 4."""
        assert verlinde_formula("sl2", 3, 1) == 4

    def test_sl2_k3_g2(self):
        """sl_2, k=3, g=2: dim = 20 (Verlinde, Beauville normalization)."""
        result = verlinde_formula("sl2", 3, 2)
        assert result == 20

    def test_sl3_g0(self):
        """sl_3, any k, g=0: dim = 1."""
        assert verlinde_formula("sl3", 1, 0) == 1
        assert verlinde_formula("sl3", 2, 0) == 1

    def test_sl3_k1_g1(self):
        """sl_3, k=1, g=1: C(3,2) = 3 integrable reps."""
        assert verlinde_formula("sl3", 1, 1) == 3

    def test_sl3_k2_g1(self):
        """sl_3, k=2, g=1: C(4,2) = 6 integrable reps."""
        assert verlinde_formula("sl3", 2, 1) == 6

    def test_conformal_blocks_sl2(self):
        """Conformal blocks for sl_2, level 1, genus 1."""
        result = fh_conformal_blocks("sl2", 1, 1)
        assert result["dim"] == 2


# =====================================================================
# TestBoundaryAcyclicity — FM boundary strata
# =====================================================================

class TestBoundaryAcyclicity:
    """Boundary acyclicity: H^k(i_S^! B_n(A)) = 0."""

    def test_arity2_heisenberg(self):
        """Arity 2, Heisenberg: diagonal stratum acyclic."""
        result = fh_boundary_acyclicity_check("heisenberg", 2)
        assert result["acyclic"] is True
        assert result["num_strata"] == 1

    def test_arity3_arnold(self):
        """Arity 3: Arnold strata acyclic for Koszul algebras."""
        result = fh_boundary_acyclicity_check("heisenberg", 3)
        assert result["acyclic"] is True
        assert result["num_strata"] == 3

    def test_arity4_pentagon(self):
        """Arity 4: associahedron K_4 (pentagon) strata acyclic."""
        result = fh_boundary_acyclicity_check("virasoro", 4)
        assert result["acyclic"] is True
        assert result["num_strata"] == 5

    def test_arity2_betagamma(self):
        """Arity 2, beta-gamma: acyclic (Koszul)."""
        result = fh_boundary_acyclicity_check("betagamma", 2)
        assert result["acyclic"] is True

    def test_arity3_affine(self):
        """Arity 3, affine sl_2: Arnold acyclic."""
        result = fh_boundary_acyclicity_check("affine_sl2", 3)
        assert result["acyclic"] is True

    def test_arity5_catalan(self):
        """Arity 5: Catalan(4) = 14 codim-1 strata."""
        result = fh_boundary_acyclicity_check("heisenberg", 5)
        assert result["acyclic"] is True
        assert result["num_strata"] == 14


# =====================================================================
# TestCrossVolume — Vol I F_g = Vol II integral_{Sigma_g}
# =====================================================================

class TestCrossVolume:
    """Cross-volume bridge: F_g from shadow tower = FH from factorization."""

    def test_fh_equals_Fg_heisenberg(self):
        """integral_{Sigma_g} H_1 = F_g from genus_partition_closure."""
        for g in range(1, 4):
            result = fh_cross_volume_check("heisenberg", g, k=1)
            assert result["all_match"] is True

    def test_fh_equals_Fg_virasoro(self):
        """integral_{Sigma_g} Vir_26 = F_g."""
        for g in range(1, 4):
            result = fh_cross_volume_check("virasoro", g, c=26)
            assert result["all_match"] is True

    def test_fh_equals_Fg_affine(self):
        """integral_{Sigma_g} V_1(sl_2) = F_g."""
        result = fh_cross_volume_check("affine_sl2", 1, k=1)
        assert result["all_match"] is True

    def test_fh_equals_Fg_betagamma(self):
        """integral_{Sigma_g} betagamma = F_g."""
        result = fh_cross_volume_check("betagamma", 2)
        assert result["all_match"] is True

    def test_cross_volume_scalar_values(self):
        """Scalar values match exactly across volumes."""
        result = fh_cross_volume_check("heisenberg", 1, k=1)
        assert result["F_g_vol1"] == Fraction(1, 24)
        assert result["F_g_vol2"] == Fraction(1, 24)
        assert result["F_g_closure"] == Fraction(1, 24)


# =====================================================================
# TestCriticalLevel — FH not concentrated at critical level
# =====================================================================

class TestCriticalLevel:
    """At critical level k = -h^v, FH is NOT concentrated but algebra is still Koszul."""

    def test_sl2_critical_not_concentrated(self):
        """V_{-2}(sl_2): FH not concentrated, but still chirally Koszul."""
        result = fh_critical_level_check("sl2")
        assert result["concentrated"] is False
        assert result["koszul"] is True
        assert result["critical_level"] == -2

    def test_sl3_critical_not_concentrated(self):
        """V_{-3}(sl_3): not concentrated."""
        result = fh_critical_level_check("sl3")
        assert result["concentrated"] is False
        assert result["critical_level"] == -3

    def test_g2_critical_not_concentrated(self):
        """V_{-4}(G_2): not concentrated."""
        result = fh_critical_level_check("g2")
        assert result["concentrated"] is False
        assert result["critical_level"] == -4

    def test_sugawara_undefined_at_critical(self):
        """Sugawara construction undefined at k = -h^v."""
        result = fh_critical_level_check("sl2")
        assert result["sugawara_defined"] is False

    def test_genus0_critical_not_concentrated(self):
        """At genus 0, critical level gives infinite H^0."""
        result = fh_genus0("affine_sl2", k=-2)
        assert result["concentrated"] is False
        assert result["H0_dim"] == float("inf")


# =====================================================================
# TestKoszulCriteria — 12 Koszulness characterizations
# =====================================================================

class TestKoszulCriteria:
    """12 Koszulness characterizations: 10 unconditional + 1 conditional + 1 one-directional."""

    def test_12_criteria_status(self):
        """10 unconditional; (xi) Lagrangian conditional; (xii) D-module purity one-directional."""
        status = koszulness_12_criteria_status()
        assert len(status) == 12
        for name, info in status.items():
            if name == "lagrangian_criterion":
                assert info["proved"] == "conditional", (
                    f"Lagrangian criterion should be 'conditional', got {info['proved']}"
                )
            else:
                assert info["proved"] is True, f"Criterion {name} not proved"

    def test_compute_verified_criteria(self):
        """At least 7 criteria have computational verification."""
        status = koszulness_12_criteria_status()
        verified_count = sum(
            1 for info in status.values() if info["compute_verified"]
        )
        assert verified_count >= 7

    def test_fh_concentration_in_criteria(self):
        """FH concentration is one of the 12 criteria."""
        status = koszulness_12_criteria_status()
        assert "fh_concentration" in status
        assert status["fh_concentration"]["proved"] is True
        assert status["fh_concentration"]["compute_verified"] is True

    def test_fm_boundary_in_criteria(self):
        """FM boundary acyclicity is one of the 12 criteria."""
        status = koszulness_12_criteria_status()
        assert "fm_boundary_acyclicity" in status
        assert status["fm_boundary_acyclicity"]["proved"] is True

    def test_tropical_in_criteria(self):
        """Tropical Koszulness is one of the 12 criteria."""
        status = koszulness_12_criteria_status()
        assert "tropical_koszulness" in status
        assert status["tropical_koszulness"]["proved"] is True


# =====================================================================
# TestHeisenbergExplicit — explicit FH for Heisenberg
# =====================================================================

class TestHeisenbergExplicit:
    """Heisenberg FH: simplest case, shadow depth 2."""

    def test_rank1_genus1(self):
        """H_1 at genus 1: F_1 = 1/24."""
        result = heisenberg_fh_explicit(1, 1)
        assert result["F_g"] == Fraction(1, 24)
        assert result["shadow_depth"] == 2
        assert result["shadow_class"] == "G"

    def test_rank1_genus2(self):
        """H_1 at genus 2: F_2 = 7/5760."""
        result = heisenberg_fh_explicit(1, 2)
        assert result["F_g"] == Fraction(7, 5760)

    def test_rank1_genus3(self):
        """H_1 at genus 3: F_3 = 31/967680."""
        result = heisenberg_fh_explicit(1, 3)
        assert result["F_g"] == Fraction(31, 967680)

    def test_level2_genus1(self):
        """H_2 at genus 1: F_1 = 2/24 = 1/12."""
        result = heisenberg_fh_explicit(2, 1)
        assert result["kappa"] == Fraction(2)
        assert result["F_g"] == Fraction(1, 12)

    def test_rank2_genus1(self):
        """H_1^2 (rank 2) at genus 1: kappa = 2, F_1 = 1/12."""
        result = heisenberg_fh_explicit(1, 1, d=2)
        assert result["kappa"] == Fraction(2)
        assert result["F_g"] == Fraction(1, 12)

    def test_borel_summable(self):
        """Heisenberg FH is Borel summable (Fredholm determinant)."""
        result = heisenberg_fh_explicit(1, 1)
        assert result["borel_summable"] is True


# =====================================================================
# TestDeterminantLine — conformal anomaly
# =====================================================================

class TestDeterminantLine:
    """Determinant line det(H^1)^{c/2} for conformal anomaly."""

    def test_heisenberg_det_power(self):
        """Heisenberg k=1: det power = 1/2."""
        result = fh_determinant_line("heisenberg", 2, k=1)
        assert result["det_power"] == Fraction(1, 2)
        assert result["central_charge"] == 1

    def test_virasoro_c26_det_power(self):
        """Virasoro c=26: det power = 13."""
        result = fh_determinant_line("virasoro", 2, c=26)
        assert result["det_power"] == Fraction(13)

    def test_betagamma_det_power(self):
        """beta-gamma c=-2: det power = -1."""
        result = fh_determinant_line("betagamma", 2)
        assert result["det_power"] == Fraction(-1)
        assert result["central_charge"] == Fraction(-2)

    def test_dim_H1_equals_genus(self):
        """dim H^1(Sigma_g, O) = g."""
        for g in range(1, 5):
            result = fh_determinant_line("heisenberg", g)
            assert result["dim_H1"] == g


# =====================================================================
# TestGenusDependence — table across genera
# =====================================================================

class TestGenusDependence:
    """Genus dependence table: F_g at each genus."""

    def test_heisenberg_table(self):
        """Heisenberg k=1: complete genus table."""
        result = fh_genus_dependence_table("heisenberg", max_g=4, k=1)
        assert result["kappa"] == Fraction(1)
        assert result["table"][1]["F_g"] == Fraction(1, 24)
        assert result["table"][2]["F_g"] == Fraction(7, 5760)

    def test_graph_counts(self):
        """Verify graph counts at each genus."""
        result = fh_genus_dependence_table("heisenberg", max_g=3, k=1)
        assert result["table"][1]["graph_count"] == 2   # genus 1: 2 graphs
        assert result["table"][2]["graph_count"] == 6   # genus 2: 6 graphs

    def test_virasoro_table(self):
        """Virasoro c=26: kappa = 13, F_1 = 13/24."""
        result = fh_genus_dependence_table("virasoro", max_g=2, c=26)
        assert result["kappa"] == Fraction(13)
        assert result["table"][1]["F_g"] == Fraction(13, 24)


# =====================================================================
# TestFHGenusG — scalar formula verification
# =====================================================================

class TestFHGenusG:
    """F_g(A) = kappa(A) * lambda_g^FP at each genus."""

    def test_scalar_formula_genus1(self):
        """F_1 = kappa * 1/24 for all families."""
        families_kappas = [
            ("heisenberg", {"k": 1}, Fraction(1)),
            ("virasoro", {"c": 26}, Fraction(13)),
            ("betagamma", {}, Fraction(1)),  # c(bg,lam=1)=2, kappa=c/2=1
        ]
        for fam, params, kappa in families_kappas:
            result = fh_genus_g(fam, 1, **params)
            assert result["F_g"] == kappa * Fraction(1, 24), f"Failed for {fam}"

    def test_graph_sum_matches_scalar(self):
        """Graph sum reproduces scalar formula at each genus."""
        for g in range(1, 4):
            result = fh_genus_g("heisenberg", g, k=1)
            assert result["scalar_match"] is True, f"Mismatch at genus {g}"

    def test_affine_kappa_correct(self):
        """kappa(V_1(sl_2)) = 3(1+2)/4 = 9/4."""
        result = fh_genus_g("affine_sl2", 1, k=1)
        assert result["kappa"] == Fraction(9, 4)
        assert result["F_g"] == Fraction(9, 4) * Fraction(1, 24)
