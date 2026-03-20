"""Tests for genus-2 boundary strata and graph-by-graph amplitude decomposition.

Verifies:
  1. Stable graph arithmetic (genus formula, h^1 = |E| - |V| + 1)
  2. Genus spectral sequence E_1 page structure
  3. Witten-Kontsevich intersection numbers at genus 2
  4. Faber's intersection numbers on M-bar_2
  5. Mumford relation at genus 2
  6. Graph-by-graph amplitudes for Heisenberg, affine sl_2, Virasoro
  7. Scalar sum identity: Sigma ell_Gamma / |Aut(Gamma)| = kappa * 7/5760
  8. Separating-node factorization: Gamma_3 amplitude = F_1^2 / 2
  9. Boundary strata decomposition
 10. Obstruction map Ob_2 classification by family
 11. Shell profile by shadow depth class

Ground truth:
  concordance.tex, higher_genus_modular_koszul.tex,
  genus2_shell_amplitudes.py, genus_expansion.py.
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, S, bernoulli, factorial

from compute.lib.genus2_boundary_strata import (
    StableGraph,
    genus2_stable_graphs,
    verify_genus2_graph_arithmetic,
    genus_spectral_sequence_e1,
    e1_page_dimensions,
    witten_kontsevich_genus2,
    faber_intersection_numbers_g2,
    faber_intersection_matrix_g2,
    mumford_relation_g2,
    boundary_strata_decomposition,
    genus2_graph_amplitudes_heisenberg,
    genus2_graph_amplitudes_affine_sl2,
    genus2_graph_amplitudes_virasoro,
    verify_scalar_sum,
    obstruction_map_genus2,
    genus2_shell_profile,
    separating_node_factorization,
    genus2_boundary_decomposition,
    genus2_boundary_strata_package,
)
from compute.lib.utils import lambda_fp, F_g


# =====================================================================
# Stable graph arithmetic
# =====================================================================

class TestStableGraphArithmetic:
    """Verify genus formula g = sum g_v + h^1(Gamma) for all 6 graphs."""

    def test_six_graphs(self):
        """There are exactly 6 stable graphs for M-bar_{2,0}."""
        graphs = genus2_stable_graphs()
        assert len(graphs) == 6

    def test_all_genus_2(self):
        """All graphs have total genus 2."""
        for G in genus2_stable_graphs():
            assert G.genus == 2, f"{G.name} has genus {G.genus}"

    def test_genus_formula(self):
        """g = sum g_v + h^1 for each graph."""
        for G in genus2_stable_graphs():
            sum_gv = sum(gv for gv, _ in G.vertices)
            h1 = G.edges - len(G.vertices) + 1
            assert h1 == G.h1, f"{G.name}: h^1 mismatch {h1} != {G.h1}"
            assert sum_gv + h1 == G.genus, f"{G.name}: genus formula fails"

    def test_h1_formula(self):
        """h^1(Gamma) = |E| - |V| + 1 for each graph."""
        results = verify_genus2_graph_arithmetic()
        for name, data in results.items():
            assert data["h1_matches"], f"{name}: h^1 formula fails"
            assert data["genus_matches"], f"{name}: genus formula fails"

    def test_smooth_graph(self):
        """Gamma_0 (smooth): 1 vertex of genus 2, 0 edges, h^1=0."""
        G = genus2_stable_graphs()[0]
        assert G.name == "Gamma_0"
        assert G.vertices == ((2, 0),)
        assert G.edges == 0
        assert G.h1 == 0
        assert G.aut_order == 1

    def test_banana_graph(self):
        """Gamma_2 (banana): 1 vertex of genus 0, 2 edges, h^1=2, |Aut|=8."""
        G = genus2_stable_graphs()[2]
        assert G.name == "Gamma_2"
        assert G.vertices == ((0, 4),)
        assert G.edges == 2
        assert G.h1 == 2
        assert G.aut_order == 8

    def test_theta_graph(self):
        """Gamma_4 (theta): 2 vertices of genus 0, 3 edges, h^1=2, |Aut|=12."""
        G = genus2_stable_graphs()[4]
        assert G.name == "Gamma_4"
        assert G.vertices == ((0, 3), (0, 3))
        assert G.edges == 3
        assert G.h1 == 2
        assert G.aut_order == 12

    def test_separating_graph(self):
        """Gamma_3 (separating): 2 genus-1 vertices, 1 edge, h^1=0, |Aut|=2."""
        G = genus2_stable_graphs()[3]
        assert G.name == "Gamma_3"
        assert G.vertices == ((1, 1), (1, 1))
        assert G.edges == 1
        assert G.h1 == 0
        assert G.aut_order == 2

    def test_h1_range(self):
        """h^1 values for genus-2 graphs are {0, 1, 2}."""
        h1_values = {G.h1 for G in genus2_stable_graphs()}
        assert h1_values == {0, 1, 2}


# =====================================================================
# Genus spectral sequence E_1 page
# =====================================================================

class TestSpectralSequence:
    """Test the E_1 page of the genus spectral sequence at genus 2."""

    def test_e1_page_separation(self):
        """6 graphs separate into h^1=0 (2 graphs), h^1=1 (2), h^1=2 (2)."""
        dims = e1_page_dimensions()
        assert dims == {0: 2, 1: 2, 2: 2}

    def test_e1_page_total(self):
        """Total number of graphs at all levels is 6."""
        dims = e1_page_dimensions()
        assert sum(dims.values()) == 6

    def test_h1_zero_graphs(self):
        """h^1=0 level contains Gamma_0 (smooth) and Gamma_3 (separating)."""
        e1 = genus_spectral_sequence_e1()
        names = {G.name for G in e1[0]}
        assert names == {"Gamma_0", "Gamma_3"}

    def test_h1_one_graphs(self):
        """h^1=1 level contains Gamma_1 (irred 1-nodal) and Gamma_5 (mixed)."""
        e1 = genus_spectral_sequence_e1()
        names = {G.name for G in e1[1]}
        assert names == {"Gamma_1", "Gamma_5"}

    def test_h1_two_graphs(self):
        """h^1=2 level contains Gamma_2 (banana) and Gamma_4 (theta)."""
        e1 = genus_spectral_sequence_e1()
        names = {G.name for G in e1[2]}
        assert names == {"Gamma_2", "Gamma_4"}

    def test_heisenberg_shell_profile(self):
        """Heisenberg genus-2 shell: only Gamma_0 and Gamma_2 active."""
        profile = genus2_shell_profile("heisenberg")
        assert profile["n_active"] == 2
        assert "Gamma_0" in profile["active_graphs"]
        assert "Gamma_2" in profile["active_graphs"]

    def test_affine_shell_profile(self):
        """Affine sl_2: 5 graphs active (all except theta)."""
        profile = genus2_shell_profile("sl2")
        assert profile["n_active"] == 5
        assert "Gamma_4" not in profile["active_graphs"]

    def test_virasoro_shell_profile(self):
        """Virasoro: all 6 graphs active."""
        profile = genus2_shell_profile("virasoro")
        assert profile["n_active"] == 6


# =====================================================================
# Hodge integrals and Witten-Kontsevich
# =====================================================================

class TestHodgeIntegrals:
    """Verify Hodge integrals and Witten-Kontsevich numbers at genus 2."""

    def test_lambda2_integral(self):
        r"""int_{M-bar_2} lambda_2 = 1/240."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_2 (on M-bar_2)"] == Rational(1, 240)

    def test_lambda_fp_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_tau4_genus2(self):
        """<tau_4>_2 = 1/1152 (Witten-Kontsevich)."""
        wk = witten_kontsevich_genus2()
        assert wk["<tau_4>_2"] == Rational(1, 1152)

    def test_lambda2_fp_from_wk(self):
        """lambda_2^FP = 7/5760 matches the Witten-Kontsevich output."""
        wk = witten_kontsevich_genus2()
        assert wk["lambda_2^FP"] == Rational(7, 5760)

    def test_selection_rule_g2_n1(self):
        """Selection rule at g=2, n=1: sum d_i = 3*2-3+1 = 4."""
        wk = witten_kontsevich_genus2()
        assert wk["selection_rule_g2_n1"] == 4

    def test_selection_rule_g2_n0(self):
        """Selection rule at g=2, n=0: sum d_i = 3*2-3+0 = 3."""
        wk = witten_kontsevich_genus2()
        assert wk["selection_rule_g2_n0"] == 3

    def test_lambda2_fp_formula(self):
        """Verify lambda_2^FP = (2^3-1)/2^3 * |B_4|/4!."""
        B4 = bernoulli(4)  # = -1/30
        prefactor = Rational(7, 8)  # (2^3-1)/2^3
        bernoulli_factor = abs(B4) / factorial(4)  # (1/30)/24 = 1/720
        result = prefactor * bernoulli_factor
        assert result == Rational(7, 5760)
        assert result == lambda_fp(2)

    def test_psi_squared_integral(self):
        """int_{M-bar_{2,1}} psi^4 = <tau_4>_2 = 1/1152."""
        faber = faber_intersection_numbers_g2()
        assert faber["psi^4 (on M-bar_{2,1})"] == Rational(1, 1152)

    def test_lambda2_psi2_integral(self):
        """int_{M-bar_{2,1}} lambda_2 psi^2 = 7/5760."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_2 psi^2 (on M-bar_{2,1})"] == Rational(7, 5760)


# =====================================================================
# Faber's intersection numbers
# =====================================================================

class TestFaberRelations:
    """Verify Faber's intersection numbers on M-bar_2."""

    def test_lambda1_cubed(self):
        """int lambda_1^3 = 1/2880 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1^3"] == Rational(1, 2880)

    def test_lambda1_sq_delta0(self):
        """int lambda_1^2 delta_0 = -1/240 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1^2 delta_0"] == Rational(-1, 240)

    def test_lambda1_sq_delta1(self):
        """int lambda_1^2 delta_1 = 1/1440 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1^2 delta_1"] == Rational(1, 1440)

    def test_lambda1_delta0_sq(self):
        """int lambda_1 delta_0^2 = 0 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1 delta_0^2"] == 0

    def test_lambda1_delta0_delta1(self):
        """int lambda_1 delta_0 delta_1 = -1/120 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1 delta_0 delta_1"] == Rational(-1, 120)

    def test_lambda1_delta1_sq(self):
        """int lambda_1 delta_1^2 = 1/576 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1 delta_1^2"] == Rational(1, 576)

    def test_lambda1_sq_equals_lambda2_integral(self):
        """int lambda_1^2 = int lambda_2 = 1/240 on M-bar_2."""
        faber = faber_intersection_numbers_g2()
        assert faber["lambda_1^2 (on M-bar_2)"] == Rational(1, 240)
        assert faber["lambda_2 (on M-bar_2)"] == Rational(1, 240)
        assert faber["lambda_1^2 (on M-bar_2)"] == faber["lambda_2 (on M-bar_2)"]

    def test_intersection_matrix_rank(self):
        """The lambda_1-slice intersection matrix is 3x3."""
        data = faber_intersection_matrix_g2()
        M = data["lambda_1_slice_matrix"]
        assert len(M) == 3
        assert all(len(row) == 3 for row in M)

    def test_intersection_matrix_symmetry(self):
        """The lambda_1-slice matrix is symmetric."""
        data = faber_intersection_matrix_g2()
        M = data["lambda_1_slice_matrix"]
        for i in range(3):
            for j in range(3):
                assert M[i][j] == M[j][i], f"M[{i}][{j}] != M[{j}][{i}]"

    def test_dimension_A1(self):
        """dim A^1(M-bar_2) = 3."""
        data = faber_intersection_matrix_g2()
        assert data["dimension_A1"] == 3

    def test_dimension_A3(self):
        """dim A^3(M-bar_2) = 1 (= Q)."""
        data = faber_intersection_matrix_g2()
        assert data["dimension_A3"] == 1


# =====================================================================
# Mumford relation
# =====================================================================

class TestMumfordRelation:
    """Verify the Mumford relation at genus 2."""

    def test_mumford_coefficients(self):
        """10 lambda_1 = delta_0 + 2 delta_1."""
        mr = mumford_relation_g2()
        assert mr["lambda_1_coeff"] == 10
        assert mr["delta_0_coeff"] == 1
        assert mr["delta_1_coeff"] == 2

    def test_mumford_relation_string(self):
        """The relation string is correct."""
        mr = mumford_relation_g2()
        assert mr["relation"] == "10 lambda_1 = delta_0 + 2 delta_1"


# =====================================================================
# Graph amplitudes: Heisenberg
# =====================================================================

class TestGraphAmplitudesHeisenberg:
    """Verify graph-by-graph amplitudes for Heisenberg."""

    def test_heisenberg_only_smooth_and_banana(self):
        """Only Gamma_0 (smooth) and Gamma_2 (banana) contribute."""
        amps = genus2_graph_amplitudes_heisenberg(1)
        assert amps["Gamma_1 (irred 1-nodal)"] == 0
        assert amps["Gamma_3 (separating)"] == 0
        assert amps["Gamma_4 (theta)"] == 0
        assert amps["Gamma_5 (mixed)"] == 0

    def test_heisenberg_sum_equals_F2(self):
        """Sum of amplitudes = kappa * 7/5760 for Heisenberg at k=1."""
        amps = genus2_graph_amplitudes_heisenberg(1)
        result = verify_scalar_sum(amps, Rational(1))
        assert result["match"]

    def test_heisenberg_k2_sum(self):
        """Sum = 2 * 7/5760 = 7/2880 for Heisenberg at k=2."""
        amps = genus2_graph_amplitudes_heisenberg(2)
        result = verify_scalar_sum(amps, Rational(2))
        assert result["match"]
        assert result["expected (kappa * 7/5760)"] == Rational(7, 2880)

    def test_heisenberg_shadow_depth(self):
        """Heisenberg has shadow depth 2 (Gaussian)."""
        amps = genus2_graph_amplitudes_heisenberg(1)
        assert amps["shadow_depth"] == 2
        assert amps["family"] == "Heisenberg"

    def test_heisenberg_total(self):
        """Total amplitude matches F_2 = kappa * 7/5760."""
        for k in [1, 2, 5, 10]:
            amps = genus2_graph_amplitudes_heisenberg(k)
            expected = Rational(k) * Rational(7, 5760)
            assert amps["total"] == expected

    def test_heisenberg_banana_nonzero(self):
        """The banana contribution is nonzero for k > 0."""
        amps = genus2_graph_amplitudes_heisenberg(3)
        assert amps["Gamma_2 (banana)"] != 0


# =====================================================================
# Graph amplitudes: Affine sl_2
# =====================================================================

class TestGraphAmplitudesAffineSl2:
    """Verify graph-by-graph amplitudes for V_k(sl_2)."""

    def test_affine_sum_equals_F2(self):
        """Sum of amplitudes = kappa * 7/5760 for V_k(sl_2)."""
        amps = genus2_graph_amplitudes_affine_sl2(1)
        kappa = Rational(3) * 3 / 4  # 3(k+2)/4 at k=1
        result = verify_scalar_sum(amps, kappa)
        assert result["match"]

    def test_separating_is_product(self):
        """Gamma_3 amplitude = F_1^2 / 2 (product of genus-1 amplitudes)."""
        for k in [1, 2, 5]:
            amps = genus2_graph_amplitudes_affine_sl2(k)
            kappa = Rational(3) * (Rational(k) + 2) / 4
            F1 = kappa * lambda_fp(1)
            expected = F1 ** 2 / 2
            assert amps["Gamma_3 (separating)"] == expected

    def test_theta_vanishes_sl2(self):
        """Gamma_4 (theta) = 0 for sl_2 (no cubic Casimir)."""
        amps = genus2_graph_amplitudes_affine_sl2(1)
        assert amps["Gamma_4 (theta)"] == 0

    def test_affine_shadow_depth(self):
        """Affine sl_2 has shadow depth 3."""
        amps = genus2_graph_amplitudes_affine_sl2(1)
        assert amps["shadow_depth"] == 3

    def test_affine_critical_level(self):
        """At k = -2 (critical): kappa = 0, F_2 = 0, all amplitudes vanish."""
        amps = genus2_graph_amplitudes_affine_sl2(-2)
        assert amps["total"] == 0
        assert amps["Gamma_3 (separating)"] == 0
        assert amps["Gamma_2 (banana)"] == 0


# =====================================================================
# Graph amplitudes: Virasoro
# =====================================================================

class TestGraphAmplitudesVirasoro:
    """Verify graph-by-graph amplitudes for Virasoro."""

    def test_virasoro_sum_equals_F2(self):
        """Sum of amplitudes = c/2 * 7/5760 for Virasoro."""
        amps = genus2_graph_amplitudes_virasoro(26)
        kappa = Rational(13)
        result = verify_scalar_sum(amps, kappa)
        assert result["match"]

    def test_virasoro_c1(self):
        """At c=1: F_2 = 7/11520."""
        amps = genus2_graph_amplitudes_virasoro(1)
        assert amps["total"] == Rational(7, 11520)

    def test_virasoro_c0(self):
        """At c=0: F_2 = 0."""
        amps = genus2_graph_amplitudes_virasoro(0)
        assert amps["total"] == 0

    def test_virasoro_shadow_depth(self):
        """Virasoro has infinite shadow depth."""
        amps = genus2_graph_amplitudes_virasoro(26)
        assert amps["shadow_depth"] == "infinity"

    def test_virasoro_Q_contact(self):
        """Q^contact_Vir = 10/[c(5c+22)] at c=2."""
        amps = genus2_graph_amplitudes_virasoro(2)
        assert amps["Q_contact"] == Rational(10, 2 * (10 + 22))
        assert amps["Q_contact"] == Rational(10, 64)

    def test_virasoro_separating(self):
        """Gamma_3 separating contribution for Virasoro."""
        amps = genus2_graph_amplitudes_virasoro(26)
        kappa = Rational(13)
        F1 = kappa * lambda_fp(1)  # 13/24
        expected = F1 ** 2 / 2
        assert amps["Gamma_3 (separating)"] == expected


# =====================================================================
# Scalar sum verification
# =====================================================================

class TestScalarSum:
    """Verify the scalar sum identity Sigma ell_Gamma/|Aut| = kappa * 7/5760."""

    def test_heisenberg_multiple_k(self):
        """Scalar sum holds for Heisenberg at k = 1, 2, 3, 5, 10."""
        for k in [1, 2, 3, 5, 10]:
            amps = genus2_graph_amplitudes_heisenberg(k)
            result = verify_scalar_sum(amps, Rational(k))
            assert result["match"], f"Failed at k={k}"

    def test_affine_multiple_k(self):
        """Scalar sum holds for affine sl_2 at k = 1, 2, 5."""
        for k in [1, 2, 5]:
            kappa = Rational(3) * (Rational(k) + 2) / 4
            amps = genus2_graph_amplitudes_affine_sl2(k)
            result = verify_scalar_sum(amps, kappa)
            assert result["match"], f"Failed at k={k}"

    def test_virasoro_multiple_c(self):
        """Scalar sum holds for Virasoro at c = 1, 2, 13, 26."""
        for c in [1, 2, 13, 26]:
            kappa = Rational(c) / 2
            amps = genus2_graph_amplitudes_virasoro(c)
            result = verify_scalar_sum(amps, kappa)
            assert result["match"], f"Failed at c={c}"

    def test_lambda_2_fp_value(self):
        """The target value lambda_2^FP = 7/5760 is correct."""
        result = verify_scalar_sum(
            genus2_graph_amplitudes_heisenberg(1), Rational(1)
        )
        assert result["lambda_2^FP"] == Rational(7, 5760)


# =====================================================================
# Boundary strata
# =====================================================================

class TestBoundaryStrata:
    """Test the boundary strata decomposition of M-bar_2."""

    def test_delta_irr_class(self):
        """Delta_irr is codimension 1, nonseparating."""
        strata = boundary_strata_decomposition()
        assert strata["Delta_irr"]["codimension"] == 1
        assert strata["Delta_irr"]["is_separating"] is False

    def test_delta_1_class(self):
        """Delta_1 is codimension 1, separating."""
        strata = boundary_strata_decomposition()
        assert strata["Delta_1"]["codimension"] == 1
        assert strata["Delta_1"]["is_separating"] is True

    def test_smooth_locus_dimension(self):
        """The smooth locus M_2 has complex dimension 3."""
        strata = boundary_strata_decomposition()
        assert strata["smooth_locus_dim"] == 3

    def test_boundary_sum(self):
        """Interior + Delta_irr + Delta_1 = F_2 for kappa = 1."""
        decomp = genus2_boundary_decomposition(Rational(1))
        assert decomp["sum_matches_F2"]

    def test_boundary_sum_general(self):
        """Interior + boundary = F_2 for several kappa values."""
        for kappa_val in [1, 2, 5, Rational(1, 2), Rational(13)]:
            decomp = genus2_boundary_decomposition(kappa_val)
            assert decomp["sum_matches_F2"], f"Failed at kappa={kappa_val}"


# =====================================================================
# Separating node factorization
# =====================================================================

class TestSeparatingNodeFactorization:
    """Verify Gamma_3 amplitude = F_1^2 / 2."""

    def test_factorization_formula(self):
        """Gamma_3 / |Aut_3| = F_1^2 / 2 = kappa^2 / 1152."""
        for kappa_val in [Rational(1), Rational(2), Rational(13)]:
            result = separating_node_factorization(kappa_val)
            expected = kappa_val ** 2 / Rational(1152)
            assert result["Gamma_3 amplitude"] == expected

    def test_factorization_coefficient(self):
        """The kappa^2 coefficient in the separating node is 1/1152."""
        result = separating_node_factorization(Rational(1))
        assert result["kappa^2_coefficient"] == Rational(1, 1152)

    def test_is_product(self):
        """The separating contribution IS a product of genus-1 amplitudes."""
        result = separating_node_factorization(Rational(1))
        assert result["is_product"]

    def test_F1_squared_consistency(self):
        """F_1 = kappa/24, so F_1^2 = kappa^2/576."""
        result = separating_node_factorization(Rational(1))
        assert result["F_1"] == Rational(1, 24)
        assert result["F_1^2"] == Rational(1, 576)
        assert result["Gamma_3 amplitude"] == Rational(1, 576) / 2


# =====================================================================
# Obstruction map Ob_2
# =====================================================================

class TestObstructionMap:
    """Test the obstruction map Ob_2 classification by family."""

    def test_heisenberg_trivial(self):
        """Heisenberg: d_1 = 0 (pure shell)."""
        ob = obstruction_map_genus2("heisenberg")
        assert "zero" in ob["d1_0_to_1"]
        assert "zero" in ob["d1_1_to_2"]
        assert ob["shadow_class"] == "G (Gaussian)"

    def test_affine_nontrivial(self):
        """Affine: d_1 nontrivial (cubic shadow propagates)."""
        ob = obstruction_map_genus2("sl2")
        assert "nontrivial" in ob["d1_0_to_1"]
        assert ob["shadow_class"] == "L (Lie/tree)"

    def test_virasoro_nontrivial(self):
        """Virasoro: d_1 nontrivial (all arities)."""
        ob = obstruction_map_genus2("virasoro")
        assert "nontrivial" in ob["d1_0_to_1"]
        assert "nontrivial" in ob["d1_1_to_2"]
        assert ob["shadow_class"] == "M (mixed)"
        assert ob["Q_contact"] == "10/[c(5c+22)]"

    def test_betagamma_quartic_vanishes(self):
        """Beta-gamma: quartic correction vanishes (mu = 0)."""
        ob = obstruction_map_genus2("betagamma")
        assert ob["shadow_class"] == "C (contact/quartic)"
        assert "mu" in ob["chain_level_corrections"] and "0" in ob["chain_level_corrections"]

    def test_scalar_level_universal(self):
        """All families have F_2 = kappa * 7/5760 at the scalar level."""
        for family in ["heisenberg", "sl2", "virasoro", "betagamma"]:
            ob = obstruction_map_genus2(family)
            assert "kappa * 7/5760" in ob["scalar_level"]

    def test_unknown_family(self):
        """Unknown family returns error."""
        ob = obstruction_map_genus2("unknown_algebra")
        assert "error" in ob


# =====================================================================
# Complete package
# =====================================================================

class TestCompletePackage:
    """Test the complete genus-2 boundary strata package."""

    def test_package_runs(self):
        """The package assembles without error."""
        pkg = genus2_boundary_strata_package()
        assert "stable_graphs" in pkg
        assert "graph_arithmetic" in pkg
        assert "e1_page_dims" in pkg

    def test_package_has_six_graphs(self):
        """Package contains 6 stable graphs."""
        pkg = genus2_boundary_strata_package()
        assert len(pkg["stable_graphs"]) == 6

    def test_package_e1_dims(self):
        """Package E_1 page dims are {0: 2, 1: 2, 2: 2}."""
        pkg = genus2_boundary_strata_package()
        assert pkg["e1_page_dims"] == {0: 2, 1: 2, 2: 2}

    def test_package_faber_numbers(self):
        """Package contains Faber's intersection numbers."""
        pkg = genus2_boundary_strata_package()
        faber = pkg["faber_numbers"]
        assert faber["lambda_1^3"] == Rational(1, 2880)

    def test_package_witten_kontsevich(self):
        """Package contains Witten-Kontsevich numbers."""
        pkg = genus2_boundary_strata_package()
        wk = pkg["witten_kontsevich"]
        assert wk["<tau_4>_2"] == Rational(1, 1152)


# =====================================================================
# Numerical cross-checks
# =====================================================================

class TestNumericalCrossChecks:
    """Floating-point cross-checks for all computed values."""

    def test_lambda2_fp_decimal(self):
        """7/5760 ~ 0.001215..."""
        val = float(lambda_fp(2))
        assert abs(val - 7 / 5760) < 1e-12

    def test_tau4_decimal(self):
        """1/1152 ~ 0.000868..."""
        wk = witten_kontsevich_genus2()
        val = float(wk["<tau_4>_2"])
        assert abs(val - 1 / 1152) < 1e-12

    def test_faber_lambda1_cubed_decimal(self):
        """1/2880 ~ 0.000347..."""
        faber = faber_intersection_numbers_g2()
        val = float(faber["lambda_1^3"])
        assert abs(val - 1 / 2880) < 1e-12

    def test_separating_kappa1_decimal(self):
        """At kappa=1: separating contribution = 1/1152 ~ 0.000868..."""
        result = separating_node_factorization(Rational(1))
        val = float(result["Gamma_3 amplitude"])
        assert abs(val - 1 / 1152) < 1e-12

    def test_F2_heisenberg_k1_decimal(self):
        """F_2(H_1) = 7/5760 ~ 0.001215..."""
        amps = genus2_graph_amplitudes_heisenberg(1)
        val = float(amps["total"])
        assert abs(val - 7 / 5760) < 1e-12

    def test_F2_virasoro_c26_decimal(self):
        """F_2(Vir_26) = 91/5760 ~ 0.01580..."""
        amps = genus2_graph_amplitudes_virasoro(26)
        val = float(amps["total"])
        assert abs(val - 91 / 5760) < 1e-12
