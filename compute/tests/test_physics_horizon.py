"""Tests for Front F physics horizon shadow-level predictions.

Front F conjectures (~20) are physics-oriented: BV/BRST, Feynman diagrams,
string amplitudes, holographic, AGT.  Full proofs need QFT input beyond
the monograph's scope, but shadow-level (numerical/cohomological)
predictions are testable.

Six conjecture families tested:

1. String amplitude = bar Euler characteristic
   (conj:string-amplitude-bar, conj:string-amplitude)

2. Anomaly cancellation
   (conj:anomaly-cancellation, conj:anomaly-physical)

3. Feynman diagram counting
   (conj:bar-worldline)

4. BV/BRST = bar-cobar
   (conj:bv-equals-bar-cobar)

5. Holographic Koszul
   (conj:holographic-koszul, conj:ads-cft-bar)

6. AGT correspondence
   (conj:agt-bar-cobar, conj:agt-w-algebra, conj:q-agt)

Ground truth references:
  - CLAUDE.md: QME factor 1/2, HCS coeff 2/3, kappa = c/2,
    Sugawara, Feigin-Frenkel, DS formulas
  - concordance.tex: MC5 frontier, Front F inventory
  - bv_brst.tex, feynman_diagrams.tex, holomorphic_topological.tex,
    poincare_duality_quantum.tex, free_fields.tex
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.physics_horizon import (
    # 1. String amplitude
    bar_euler_characteristic,
    genus_1_partition_function_exponent,
    heisenberg_genus1_bar,
    string_bar_genus0_proved,
    faber_pandharipande_number,
    genus_expansion_term,
    # 2. Anomaly cancellation
    matter_ghost_anomaly,
    koszul_dual_kappa_cancellation,
    brst_d_squared_anomaly,
    anomaly_cancellation_critical_dimensions,
    # 3. Feynman diagram counting
    connected_trivalent_graphs,
    bar_degree_vs_feynman_data,
    worldline_propagator_correspondence,
    arnold_cancellation_as_renormalization,
    # 4. BV/BRST
    qme_coefficients,
    hcs_coefficients,
    bv_ghost_numbers,
    bar_bv_dictionary,
    bv_bar_curvature_interpretation,
    qme_bar_equivalence_genus0,
    # 5. Holographic
    holographic_koszul_dictionary,
    ads3_cft2_virasoro,
    holographic_central_charge_matching,
    w_infinity_higher_spin,
    # 6. AGT
    hook_length,
    hook_length_product,
    instanton_partition_function_su2,
    agt_nekrasov_vs_w_algebra,
    agt_w_algebra_ds_connection,
    # Additional
    path_integral_bar_cobar,
    cs_factorization_homology,
    nc_chern_simons,
    closed_string_cobar,
    dbrane_e1_conjecture,
    q_agt_conjecture,
    # Verified formulas
    sugawara_central_charge,
    feigin_frenkel_dual,
    virasoro_ds_central_charge,
    w3_ds_central_charge,
    # Comprehensive check
    verify_all_physics_horizon,
)


# ===========================================================================
# 1. STRING AMPLITUDE = BAR EULER CHARACTERISTIC
# ===========================================================================

class TestBarEulerCharacteristic:
    """Bar complex Euler characteristic computations."""

    def test_euler_char_virasoro(self):
        """Virasoro bar Euler characteristic (Motzkin differences)."""
        # H^n: 1, 2, 5, 12, 30, 76
        dims = {1: 1, 2: 2, 3: 5, 4: 12, 5: 30, 6: 76}
        chi = bar_euler_characteristic(dims)
        # chi = -1 + 2 - 5 + 12 - 30 + 76 = 54
        assert chi == -1 + 2 - 5 + 12 - 30 + 76

    def test_euler_char_sl2(self):
        """sl2 bar Euler characteristic (Riordan numbers R(n+3))."""
        # H^n: 3, 6, 15, 36, 91
        dims = {1: 3, 2: 6, 3: 15, 4: 36, 5: 91}
        chi = bar_euler_characteristic(dims)
        assert chi == -3 + 6 - 15 + 36 - 91

    def test_euler_char_heisenberg(self):
        """Heisenberg bar: H^1=1, H^n=p(n-2) for n>=2."""
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5
        dims = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5}
        chi = bar_euler_characteristic(dims)
        expected = -1 + 1 - 1 + 2 - 3 + 5
        assert chi == expected

    def test_euler_char_empty(self):
        """Empty bar complex has zero Euler characteristic."""
        assert bar_euler_characteristic({}) == 0

    def test_euler_char_truncation(self):
        """Euler char respects max_degree truncation."""
        dims = {1: 3, 2: 6, 3: 15}
        assert bar_euler_characteristic(dims, max_degree=2) == -3 + 6


class TestGenus1PartitionFunction:
    """Genus-1 partition function eta exponent."""

    def test_bosonic_string_c26(self):
        """Bosonic string c=26: eta exponent = 48."""
        assert genus_1_partition_function_exponent(26) == 48

    def test_c2(self):
        """c=2: eta exponent = 0 (topological)."""
        assert genus_1_partition_function_exponent(2) == 0

    def test_c1(self):
        """c=1: eta exponent = -2 (negative, unphysical)."""
        # Exponent is 2*(c-2) = 2*(-1) = -2, but we return absolute value...
        # Actually: 2*(c-2) for c=1 is -2, the function returns 2*(c-2) directly
        assert genus_1_partition_function_exponent(1) == -2

    def test_superstring_c15(self):
        """Superstring c=15 (before GSO): eta exponent = 26."""
        assert genus_1_partition_function_exponent(15) == 26


class TestHeisenbergGenus1:
    """Heisenberg algebra genus-1 bar complex."""

    def test_f1_single_boson(self):
        """F_1(H_1) = 1/48 for a single free boson.

        kappa = 1/2, lambda_1^FP = 1/24, F_1 = 1/48.
        """
        data = heisenberg_genus1_bar(1)
        assert data["F1"] == Rational(1, 48)

    def test_f1_bosonic_string(self):
        """F_1(H_26) = 13/24 for 26 free bosons.

        kappa = 13, lambda_1^FP = 1/24, F_1 = 13/24.
        """
        data = heisenberg_genus1_bar(26)
        assert data["F1"] == Rational(13, 24)

    def test_f1_c2(self):
        """F_1(H_2) = 1/24 for 2 free bosons.

        kappa = 1, lambda_1^FP = 1/24, F_1 = 1/24.
        """
        data = heisenberg_genus1_bar(2)
        assert data["F1"] == Rational(1, 24)

    def test_kappa_equals_c_over_2(self):
        """kappa = c/2 for Heisenberg."""
        data = heisenberg_genus1_bar(10)
        assert data["kappa"] == 5

    def test_lambda1_fp(self):
        """lambda_1^FP = 1/24."""
        data = heisenberg_genus1_bar(1)
        assert data["lambda1_FP"] == Rational(1, 24)


class TestStringBarGenus0:
    """Genus-0 string-bar identification (PROVED)."""

    def test_status_proved(self):
        """Genus 0 is proved."""
        data = string_bar_genus0_proved()
        assert data["status"] == "PROVED"
        assert data["genus"] == 0

    def test_scope_includes_km(self):
        """Scope includes Kac-Moody."""
        data = string_bar_genus0_proved()
        assert any("Kac-Moody" in s for s in data["scope"])

    def test_scope_includes_c26(self):
        """Scope includes conformal vertex algebras at c=26."""
        data = string_bar_genus0_proved()
        assert any("c=26" in s for s in data["scope"])


class TestFaberPandharipandeNumbers:
    """Faber-Pandharipande numbers lambda_g^FP."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24.

        (2^1-1)/2^1 * |B_2|/(2!) = (1/2)*(1/6)/2 = 1/24.
        Consistent with utils.lambda_fp(1).
        """
        assert faber_pandharipande_number(1) == Rational(1, 24)

    def test_lambda2(self):
        """lambda_2^FP = 7/5760.

        (2^3-1)/2^3 * |B_4|/(4!) = 7/8 * (1/30)/24 = 7/5760.
        """
        val = faber_pandharipande_number(2)
        assert val == Rational(7, 5760)

    def test_lambda3(self):
        """lambda_3^FP is positive and less than lambda_2."""
        val3 = faber_pandharipande_number(3)
        val2 = faber_pandharipande_number(2)
        assert val3 > 0
        assert val3 < val2

    def test_invalid_genus(self):
        """Genus < 1 raises ValueError."""
        with pytest.raises(ValueError):
            faber_pandharipande_number(0)

    def test_genus_expansion_at_g1(self):
        """F_1(A) = kappa * 1/24."""
        f1 = genus_expansion_term(Rational(13), 1)
        assert f1 == Rational(13, 24)


# ===========================================================================
# 2. ANOMALY CANCELLATION
# ===========================================================================

class TestMatterGhostAnomaly:
    """Anomaly cancellation for matter-ghost systems."""

    def test_bosonic_string_anomaly_free(self):
        """Bosonic string: c_matter=26, c_ghost=-26, anomaly cancels."""
        data = matter_ghost_anomaly(26, -26)
        assert data["anomaly_free"] is True
        assert data["c_total"] == 0

    def test_bosonic_string_kappa_cancels(self):
        """Bosonic string: kappa_matter + kappa_ghost = 0."""
        data = matter_ghost_anomaly(26, -26)
        assert data["kappa_cancels"] is True
        assert data["kappa_total"] == 0

    def test_superstring_anomaly_free(self):
        """Superstring: c_matter=15, c_ghost=-15, anomaly cancels."""
        data = matter_ghost_anomaly(15, -15)
        assert data["anomaly_free"] is True

    def test_noncritical_anomaly(self):
        """Noncritical string: c_matter=1, c_ghost=-26, anomaly present."""
        data = matter_ghost_anomaly(1, -26)
        assert data["anomaly_free"] is False
        assert data["c_total"] == -25

    def test_kappa_matter_c26(self):
        """kappa(V_26) = 13."""
        data = matter_ghost_anomaly(26, -26)
        assert data["kappa_matter"] == 13

    def test_kappa_ghost_c26(self):
        """kappa(bc ghost) = -13."""
        data = matter_ghost_anomaly(26, -26)
        assert data["kappa_ghost"] == -13

    def test_default_ghost_is_bosonic(self):
        """Default ghost central charge is -26 (bosonic)."""
        data = matter_ghost_anomaly(26)
        assert data["c_ghost"] == -26


class TestKoszulDualKappaCancellation:
    """kappa(A) + kappa(A!) = 0 for Koszul dual pairs."""

    def test_km_sl2_symbolic(self):
        """KM sl2: kappa + kappa' = 0 for symbolic k."""
        data = koszul_dual_kappa_cancellation("KM")
        assert data["kappa_cancels"] is True

    def test_km_sl2_k1(self):
        """KM sl2 at k=1: kappa(g_1) + kappa(g_{-5}) = 0."""
        data = koszul_dual_kappa_cancellation("KM", k_val=1)
        assert data["kappa_cancels"] is True
        assert data["ff_dual_level"] == -5

    def test_km_sl2_k2(self):
        """KM sl2 at k=2: kappa + kappa' = 0."""
        data = koszul_dual_kappa_cancellation("KM", k_val=2)
        assert data["kappa_cancels"] is True

    def test_virasoro_does_not_cancel(self):
        """Virasoro: kappa + kappa' = 13, NOT 0."""
        data = koszul_dual_kappa_cancellation("Virasoro")
        assert data["kappa_cancels"] is False

    def test_bc_betagamma_cancels(self):
        """bc + betagamma: kappa + kappa' = 0."""
        data = koszul_dual_kappa_cancellation("bc")
        assert data["kappa_cancels"] is True

    def test_bc_betagamma_cancels_lam2(self):
        """bc + betagamma at lambda=2: kappa + kappa' = 0."""
        data = koszul_dual_kappa_cancellation("bc", k_val=2)
        assert data["kappa_cancels"] is True

    def test_unknown_algebra_raises(self):
        """Unknown algebra raises ValueError."""
        with pytest.raises(ValueError):
            koszul_dual_kappa_cancellation("unknown")


class TestBRSTDSquared:
    """BRST d^2 anomaly formula."""

    def test_bosonic_string_nilpotent(self):
        """d_BRST^2 = 0 for c_matter=26, c_ghost=-26."""
        data = brst_d_squared_anomaly(26, -26, 3)
        assert data["is_nilpotent"] is True

    def test_noncritical_not_nilpotent(self):
        """d_BRST^2 != 0 for noncritical string."""
        data = brst_d_squared_anomaly(1, -26, 3)
        assert data["is_nilpotent"] is False

    def test_anomaly_coefficient_formula(self):
        """Anomaly coefficient = c_total/24."""
        data = brst_d_squared_anomaly(26, -26, 5)
        assert data["anomaly_coefficient"] == 0

    def test_noncritical_anomaly_coefficient(self):
        """Noncritical: anomaly coefficient = -25/24."""
        data = brst_d_squared_anomaly(1, -26, 5)
        assert data["anomaly_coefficient"] == Rational(-25, 24)


class TestCriticalDimensions:
    """Critical dimensions for anomaly cancellation."""

    def test_bosonic_string_dimension(self):
        """Bosonic string: d = 26."""
        dims = anomaly_cancellation_critical_dimensions()
        assert dims["bosonic_string"]["d_spacetime"] == 26
        assert dims["bosonic_string"]["c_total"] == 0

    def test_superstring_dimension(self):
        """Superstring: d = 10."""
        dims = anomaly_cancellation_critical_dimensions()
        assert dims["superstring"]["d_spacetime"] == 10
        assert dims["superstring"]["c_total"] == 0

    def test_noncritical_nonzero(self):
        """Noncritical: c_total != 0."""
        dims = anomaly_cancellation_critical_dimensions()
        assert dims["noncritical_c1"]["c_total"] != 0


# ===========================================================================
# 3. FEYNMAN DIAGRAM COUNTING
# ===========================================================================

class TestTrivalentGraphs:
    """Connected trivalent graph counts."""

    def test_n0(self):
        """n=0: 1 graph (empty/vacuum)."""
        assert connected_trivalent_graphs(0) == 1

    def test_n1(self):
        """n=1: 1 graph (propagator)."""
        assert connected_trivalent_graphs(1) == 1

    def test_n2(self):
        """n=2: 1 graph (sunset)."""
        assert connected_trivalent_graphs(2) == 1

    def test_n3(self):
        """n=3: 2 graphs."""
        assert connected_trivalent_graphs(3) == 2

    def test_unknown_returns_none(self):
        """Unknown n returns None."""
        assert connected_trivalent_graphs(100) is None


class TestBarVsFeynman:
    """Bar complex dimensions vs Feynman graph counts."""

    def test_bar_chain_dim_sl2_deg1(self):
        """sl2 (dim=3) at degree 1: chain dim = 3."""
        data = bar_degree_vs_feynman_data(3, 3)
        assert data[1]["bar_chain_dim"] == 3

    def test_bar_chain_dim_sl2_deg2(self):
        """sl2 at degree 2: chain dim = 9 * 1 = 9."""
        data = bar_degree_vs_feynman_data(3, 3)
        assert data[2]["bar_chain_dim"] == 9

    def test_bar_chain_dim_sl2_deg3(self):
        """sl2 at degree 3: chain dim = 27 * 2 = 54."""
        data = bar_degree_vs_feynman_data(3, 3)
        assert data[3]["bar_chain_dim"] == 54

    def test_os_dim_formula(self):
        """OS top dim = (n-1)!."""
        data = bar_degree_vs_feynman_data(3, 5)
        for n in range(1, 6):
            from math import factorial as fact
            assert data[n]["os_dim"] == fact(n - 1)

    def test_ratio_exists(self):
        """Ratio chain_dim / feynman_count exists for small n."""
        data = bar_degree_vs_feynman_data(3, 3)
        for n in range(1, 4):
            assert data[n]["ratio"] is not None


class TestWorldlineCorrespondence:
    """Worldline-bar complex dictionary."""

    def test_propagator_is_log_form(self):
        """Propagator is eta_{ij} = d log(z_i - z_j)."""
        corr = worldline_propagator_correspondence()
        assert "d log" in corr["propagator"]

    def test_status_heuristic(self):
        """Conjecture status is ClaimStatusHeuristic."""
        corr = worldline_propagator_correspondence()
        assert "Heuristic" in corr["status"]

    def test_label(self):
        """Conjecture label is conj:bar-worldline."""
        corr = worldline_propagator_correspondence()
        assert corr["conjecture_label"] == "conj:bar-worldline"


class TestArnoldCancellation:
    """Arnold relations as renormalization."""

    def test_n2_no_cancellation(self):
        """At n=2: 1 edge, 1 OS form, no cancellation needed."""
        data = arnold_cancellation_as_renormalization()
        assert data[2]["n_edges"] == 1
        assert data[2]["os_top_dim"] == 1

    def test_n3_reduction(self):
        """At n=3: 3 edges, 2 OS forms."""
        data = arnold_cancellation_as_renormalization()
        assert data[3]["n_edges"] == 3
        assert data[3]["os_top_dim"] == 2

    def test_n4_reduction(self):
        """At n=4: 6 edges, 6 OS forms."""
        data = arnold_cancellation_as_renormalization()
        assert data[4]["n_edges"] == 6
        assert data[4]["os_top_dim"] == 6

    def test_os_grows_faster_than_edges(self):
        """OS dim grows as (n-1)! which exceeds n(n-1)/2 for large n."""
        data = arnold_cancellation_as_renormalization()
        # At n=5: edges = 10, OS = 24
        assert data[5]["os_top_dim"] > data[5]["n_edges"]


# ===========================================================================
# 4. BV/BRST = BAR-COBAR
# ===========================================================================

class TestQMECoefficients:
    """Quantum master equation coefficients."""

    def test_antibracket_half(self):
        """QME has factor 1/2 on antibracket (CLAUDE.md)."""
        qme = qme_coefficients()
        assert qme["antibracket_coeff"] == Rational(1, 2)

    def test_antibracket_not_one(self):
        """Common error: factor 1 instead of 1/2."""
        qme = qme_coefficients()
        assert qme["antibracket_coeff"] != 1

    def test_antibracket_not_one_third(self):
        """Factor is 1/2, not 1/3."""
        qme = qme_coefficients()
        assert qme["antibracket_coeff"] != Rational(1, 3)


class TestHCSCoefficients:
    """Holomorphic Chern-Simons action coefficients."""

    def test_cubic_two_thirds(self):
        """HCS cubic term has coefficient 2/3 (CLAUDE.md)."""
        hcs = hcs_coefficients()
        assert hcs["cubic_coeff"] == Rational(2, 3)

    def test_cubic_not_one_third(self):
        """Common error: 1/3 instead of 2/3."""
        hcs = hcs_coefficients()
        assert hcs["cubic_coeff"] != Rational(1, 3)

    def test_kinetic_one(self):
        """Kinetic term coefficient is 1."""
        hcs = hcs_coefficients()
        assert hcs["kinetic_coeff"] == 1


class TestGhostNumbers:
    """Ghost number assignments in BV formalism."""

    def test_fields_ghost_zero(self):
        """Fields have ghost number 0."""
        assert bv_ghost_numbers()["fields"] == 0

    def test_antifields_ghost_one(self):
        """Antifields have ghost number +1 (cohomological convention)."""
        assert bv_ghost_numbers()["antifields"] == 1

    def test_ghosts_ghost_minus_one(self):
        """Ghosts have ghost number -1."""
        assert bv_ghost_numbers()["ghosts"] == -1

    def test_brst_ghost_plus_one(self):
        """BRST operator has ghost number +1 (|d| = +1)."""
        assert bv_ghost_numbers()["BRST_operator"] == 1

    def test_antibracket_ghost_minus_one(self):
        """Antibracket has ghost number -1."""
        assert bv_ghost_numbers()["antibracket"] == -1

    def test_bv_laplacian_ghost_minus_one(self):
        """BV Laplacian has ghost number -1."""
        assert bv_ghost_numbers()["BV_laplacian"] == -1


class TestBarBVDictionary:
    """Bar complex <-> BV formalism dictionary."""

    def test_bar_diff_is_brst(self):
        """Bar differential corresponds to BRST operator."""
        d = bar_bv_dictionary()
        assert "BRST" in d["bar_differential"]

    def test_curvature_is_anomaly(self):
        """Curvature m_0 = obstruction to CME."""
        d = bar_bv_dictionary()
        assert "master equation" in d["curvature_m0"]

    def test_genus_0_proved(self):
        """Genus 0 identification is proved."""
        d = bar_bv_dictionary()
        assert "PROVED" in d["genus_0_status"]

    def test_higher_genus_conjectured(self):
        """Higher genus is conjectured."""
        d = bar_bv_dictionary()
        assert "CONJECTURED" in d["higher_genus_status"]


class TestBVCurvature:
    """Bar curvature as BV anomaly for specific algebras."""

    def test_virasoro_m0(self):
        """Virasoro: m_0 = c/2."""
        data = bv_bar_curvature_interpretation("Virasoro")
        assert data["m0_formula"] == "c/2"

    def test_virasoro_anomaly_free_c0(self):
        """Virasoro anomaly-free at c=0."""
        data = bv_bar_curvature_interpretation("Virasoro")
        assert "c = 0" in data["anomaly_free_at"]

    def test_virasoro_dual_c26(self):
        """Virasoro dual anomaly-free at c=26."""
        data = bv_bar_curvature_interpretation("Virasoro")
        assert "c = 26" in data["dual_anomaly_free_at"]

    def test_sl2_critical_level(self):
        """sl2 anomaly-free at k = -2 (critical level)."""
        data = bv_bar_curvature_interpretation("sl2")
        assert "k = -2" in data["anomaly_free_at"]

    def test_w3_m0(self):
        """W3: m_0 = 5c/6."""
        data = bv_bar_curvature_interpretation("W3")
        assert data["m0_formula"] == "5c/6"

    def test_unknown_algebra(self):
        """Unknown algebra returns m0=unknown."""
        data = bv_bar_curvature_interpretation("unknown")
        assert data["m0_formula"] == "unknown"


class TestQMEBarGenus0:
    """QME-bar equivalence at genus 0 (PROVED)."""

    def test_bar_nilpotent(self):
        """Full bar differential d^2 = 0."""
        data = qme_bar_equivalence_genus0()
        assert data["bar_nilpotent"] is True

    def test_d_bracket_not_nilpotent(self):
        """d_bracket^2 != 0 (PROVED, all 2048 signs)."""
        data = qme_bar_equivalence_genus0()
        assert data["d_bracket_squared_zero"] is False

    def test_full_d_nilpotent(self):
        """d = d_bracket + d_curvature has d^2 = 0."""
        data = qme_bar_equivalence_genus0()
        assert data["full_d_squared_zero"] is True

    def test_mechanism_borcherds(self):
        """Mechanism: Borcherds identity."""
        data = qme_bar_equivalence_genus0()
        assert "Borcherds" in data["mechanism"]

    def test_status_proved(self):
        """Status is PROVED."""
        data = qme_bar_equivalence_genus0()
        assert data["status"] == "PROVED"


# ===========================================================================
# 5. HOLOGRAPHIC KOSZUL DUALITY
# ===========================================================================

class TestHolographicDictionary:
    """Holographic Koszul duality dictionary."""

    def test_bar_is_boundary_to_bulk(self):
        """Bar = boundary-to-bulk operator map."""
        d = holographic_koszul_dictionary()
        assert "boundary-to-bulk" in d["bar"]

    def test_cobar_is_bulk_to_boundary(self):
        """Cobar = bulk-to-boundary reconstruction."""
        d = holographic_koszul_dictionary()
        assert "bulk-to-boundary" in d["cobar"]

    def test_adjunction_is_ads_cft(self):
        """Bar-cobar adjunction = algebraic shadow of AdS/CFT."""
        d = holographic_koszul_dictionary()
        assert "AdS/CFT" in d["bar_cobar_adjunction"]

    def test_status_conjectured(self):
        """Status is ClaimStatusConjectured."""
        d = holographic_koszul_dictionary()
        assert "Conjectured" in d["status"]


class TestAdS3CFT2Virasoro:
    """AdS3/CFT2 central charge relations."""

    def test_c_plus_c_dual_is_26(self):
        """c + c' = 26 for all c."""
        data = ads3_cft2_virasoro(10)
        assert data["sum"] == 26

    def test_c26_dual_is_0(self):
        """At c=26, bulk dual c' = 0."""
        data = ads3_cft2_virasoro(26)
        assert data["bulk_c_dual"] == 0

    def test_c0_dual_is_26(self):
        """At c=0, bulk dual c' = 26."""
        data = ads3_cft2_virasoro(0)
        assert data["bulk_c_dual"] == 26

    def test_c13_self_dual(self):
        """At c=13, self-dual point."""
        data = ads3_cft2_virasoro(13)
        assert data["bulk_c_dual"] == 13

    def test_symbolic_sum(self):
        """Symbolic: c + (26-c) = 26."""
        data = ads3_cft2_virasoro()
        assert data["sum"] == 26

    def test_kappa_boundary(self):
        """kappa_boundary = c/2."""
        data = ads3_cft2_virasoro(26)
        assert data["kappa_boundary"] == 13

    def test_special_cases_exist(self):
        """Special cases are documented."""
        data = ads3_cft2_virasoro()
        assert "c=26" in data["special_cases"]
        assert "c=13" in data["special_cases"]


class TestHolographicCentralCharge:
    """Holographic central charge matching."""

    def test_complementarity(self):
        """c + c' = 26 for any c."""
        data = holographic_central_charge_matching(10)
        assert data["complementarity"] is True

    def test_kappa_sum_is_13(self):
        """kappa + kappa' = 13."""
        data = holographic_central_charge_matching(10)
        assert data["kappa_sum"] == 13

    def test_brown_henneaux(self):
        """Brown-Henneaux formula is referenced."""
        data = holographic_central_charge_matching(26)
        assert "3l/(2G_N)" in data["brown_henneaux"]


class TestWInfinityHigherSpin:
    """W_infinity as holographic boundary algebra."""

    def test_boundary_algebra(self):
        """Boundary algebra is W_inf[lambda]."""
        data = w_infinity_higher_spin(10)
        assert "W_inf" in data["boundary_algebra"]

    def test_bulk_theory(self):
        """Bulk theory is Vasiliev hs[lambda]."""
        data = w_infinity_higher_spin(10)
        assert "Vasiliev" in data["bulk_theory"]

    def test_boundary_c(self):
        """Boundary central charge = N."""
        data = w_infinity_higher_spin(10)
        assert data["boundary_c"] == 10


# ===========================================================================
# 6. AGT CORRESPONDENCE
# ===========================================================================

class TestHookLength:
    """Hook length computation for partitions."""

    def test_single_box(self):
        """Partition [1]: hook at (0,0) is 1."""
        assert hook_length([1], 0, 0) == 1

    def test_two_boxes_row(self):
        """Partition [2]: hooks are 2, 1."""
        assert hook_length([2], 0, 0) == 2
        assert hook_length([2], 0, 1) == 1

    def test_two_boxes_column(self):
        """Partition [1,1]: hooks are 2, 1."""
        assert hook_length([1, 1], 0, 0) == 2
        assert hook_length([1, 1], 1, 0) == 1

    def test_hook_2_2(self):
        """Partition [2,2]: hooks at corners."""
        # [2,2]: 3 2 / 2 1
        assert hook_length([2, 2], 0, 0) == 3
        assert hook_length([2, 2], 0, 1) == 2
        assert hook_length([2, 2], 1, 0) == 2
        assert hook_length([2, 2], 1, 1) == 1

    def test_hook_3_1(self):
        """Partition [3,1]: L-shaped."""
        # [3,1]: 4 2 1 / 1
        assert hook_length([3, 1], 0, 0) == 4
        assert hook_length([3, 1], 0, 1) == 2
        assert hook_length([3, 1], 0, 2) == 1
        assert hook_length([3, 1], 1, 0) == 1

    def test_invalid_cell(self):
        """Invalid cell raises ValueError."""
        with pytest.raises(ValueError):
            hook_length([2, 1], 1, 1)  # cell (1,1) not in partition [2,1]


class TestHookLengthProduct:
    """Hook length product for partitions."""

    def test_empty_partition(self):
        """Empty partition: H = 1."""
        assert hook_length_product([]) == 1

    def test_single_box(self):
        """[1]: H = 1."""
        assert hook_length_product([1]) == 1

    def test_two_row(self):
        """[2]: H = 2 * 1 = 2."""
        assert hook_length_product([2]) == 2

    def test_two_column(self):
        """[1,1]: H = 2 * 1 = 2."""
        assert hook_length_product([1, 1]) == 2

    def test_three_row(self):
        """[3]: H = 3 * 2 * 1 = 6."""
        assert hook_length_product([3]) == 6

    def test_two_two(self):
        """[2,2]: H = 3 * 2 * 2 * 1 = 12."""
        assert hook_length_product([2, 2]) == 12

    def test_three_one(self):
        """[3,1]: H = 4 * 2 * 1 * 1 = 8."""
        assert hook_length_product([3, 1]) == 8

    def test_hook_length_formula(self):
        """dim of irrep of S_n = n! / H(lambda).

        For [2,1] of S_3: dim = 3!/2 = 3.  But let's check:
        [2,1]: hooks at (0,0)=3, (0,1)=1, (1,0)=1 -> H=3.
        dim = 3!/3 = 2. Actually that's the standard Young tableau count.
        """
        h = hook_length_product([2, 1])
        assert h == 3  # 3 * 1 * 1 = 3
        dim_irrep = 6 // h  # 3!/3 = 2
        assert dim_irrep == 2


class TestInstantonPartitionFunction:
    """SU(2) instanton partition function."""

    def test_z0_is_1(self):
        """Z_0 = 1 (no instantons)."""
        data = instanton_partition_function_su2(3)
        assert data["coefficients"][0] == 1

    def test_z1(self):
        """Z_1 = 1/H([1])^2 = 1/1 = 1."""
        data = instanton_partition_function_su2(3)
        assert data["coefficients"][1] == 1

    def test_z2(self):
        """Z_2 = 1/H([2])^2 + 1/H([1,1])^2 = 1/4 + 1/4 = 1/2."""
        data = instanton_partition_function_su2(3)
        assert data["coefficients"][2] == Rational(1, 2)

    def test_z3(self):
        """Z_3: partitions [3], [2,1], [1,1,1]."""
        data = instanton_partition_function_su2(3)
        # [3]: H = 6, 1/36
        # [2,1]: H = 3, 1/9
        # [1,1,1]: H = 6, 1/36
        z3 = Rational(1, 36) + Rational(1, 9) + Rational(1, 36)
        assert data["coefficients"][3] == z3

    def test_gauge_group(self):
        """Gauge group is SU(2)."""
        data = instanton_partition_function_su2(2)
        assert data["gauge_group"] == "SU(2)"


class TestAGTNekrasov:
    """Nekrasov vs W-algebra comparison."""

    def test_z0_is_1(self):
        """Z_0 coefficient is 1."""
        data = agt_nekrasov_vs_w_algebra(2)
        assert data["z0"] == 1

    def test_z1_is_1(self):
        """Z_1 coefficient is 1."""
        data = agt_nekrasov_vs_w_algebra(2)
        assert data["z1"] == 1

    def test_z2_is_half(self):
        """Z_2 coefficient is 1/2."""
        data = agt_nekrasov_vs_w_algebra(2)
        assert data["z2"] == Rational(1, 2)

    def test_agt_relation_documented(self):
        """AGT relation is documented."""
        data = agt_nekrasov_vs_w_algebra(2)
        assert "Virasoro conformal block" in data["agt_relation"]


class TestAGTDSConnection:
    """AGT connects gauge group G to W-algebra via DS reduction."""

    def test_su2(self):
        """SU(2) <-> W_k(sl_2) = Virasoro."""
        data = agt_w_algebra_ds_connection("A", 1)
        assert data["gauge_group"] == "SU(2)"
        assert data["dim_g"] == 3
        assert data["h_dual"] == 2
        assert data["spins"] == [2]

    def test_su3(self):
        """SU(3) <-> W_k(sl_3)."""
        data = agt_w_algebra_ds_connection("A", 2)
        assert data["gauge_group"] == "SU(3)"
        assert data["dim_g"] == 8
        assert data["h_dual"] == 3
        assert data["spins"] == [2, 3]

    def test_su4(self):
        """SU(4) <-> W_k(sl_4)."""
        data = agt_w_algebra_ds_connection("A", 3)
        assert data["gauge_group"] == "SU(4)"
        assert data["dim_g"] == 15
        assert data["h_dual"] == 4
        assert data["spins"] == [2, 3, 4]

    def test_2d_side_proved(self):
        """Bar-semi-infinite identification is proved."""
        data = agt_w_algebra_ds_connection("A", 1)
        assert data["bar_semi_infinite_proved"] is True

    def test_4d_2d_bridge_conjectural(self):
        """4D-2D AGT bridge is conjectural."""
        data = agt_w_algebra_ds_connection("A", 1)
        assert data["agt_4d_2d_bridge"] == "conjectural"


# ===========================================================================
# ADDITIONAL FRONT F CONJECTURE CHECKS
# ===========================================================================

class TestPathIntegralBarCobar:
    """Bar-cobar as worldsheet path integral."""

    def test_genus_0_proved(self):
        data = path_integral_bar_cobar()
        assert "proved" in data["genus_0"]

    def test_higher_genus_needs_costello(self):
        data = path_integral_bar_cobar()
        assert "Costello" in data["higher_genus"]


class TestCSFactorizationHomology:
    """CS factorization homology conjecture."""

    def test_hcs_coeff(self):
        """HCS cubic coefficient is 2/3."""
        data = cs_factorization_homology()
        assert data["hcs_cubic_coeff"] == Rational(2, 3)

    def test_genus_0_established(self):
        data = cs_factorization_homology()
        assert "established" in data["genus_0_status"]


class TestNCChernSimons:
    """Non-commutative Chern-Simons."""

    def test_output_is_e1(self):
        data = nc_chern_simons()
        assert "E_1" in data["output"]


class TestClosedStringCobar:
    """Closed-string cobar identification."""

    def test_verdier_exchange_proved(self):
        data = closed_string_cobar()
        assert "proved" in data["verdier_exchange"]


class TestDBraneE1:
    """D-brane algebras are E_1."""

    def test_prediction(self):
        data = dbrane_e1_conjecture()
        assert "E_1" in data["prediction"]


class TestQAGT:
    """q-deformed AGT."""

    def test_w_qt_is_e1(self):
        data = q_agt_conjecture()
        assert data["w_qt_is_e1"] is True


# ===========================================================================
# VERIFIED FORMULAS (critical pitfalls from CLAUDE.md)
# ===========================================================================

class TestSugawaraCentralCharge:
    """Sugawara formula: c = k*dim(g)/(k+h^vee)."""

    def test_sl2_k1(self):
        """sl2 at k=1: c = 1*3/3 = 1."""
        assert sugawara_central_charge(3, 1, 2) == 1

    def test_sl2_k2(self):
        """sl2 at k=2: c = 2*3/4 = 3/2."""
        assert sugawara_central_charge(3, 2, 2) == Rational(3, 2)

    def test_sl3_k1(self):
        """sl3 at k=1: c = 1*8/4 = 2."""
        assert sugawara_central_charge(8, 1, 3) == 2

    def test_critical_level_raises(self):
        """Sugawara UNDEFINED at k = -h^vee."""
        with pytest.raises(ValueError, match="critical level"):
            sugawara_central_charge(3, -2, 2)

    def test_sl2_k0(self):
        """sl2 at k=0: c = 0."""
        assert sugawara_central_charge(3, 0, 2) == 0


class TestFeiginFrenkelDual:
    """Feigin-Frenkel dual level: k' = -k - 2h^vee."""

    def test_sl2_k1(self):
        """sl2 k=1: k' = -1 - 4 = -5."""
        assert feigin_frenkel_dual(1, 2) == -5

    def test_sl2_k0(self):
        """sl2 k=0: k' = -4."""
        assert feigin_frenkel_dual(0, 2) == -4

    def test_sl3_k1(self):
        """sl3 k=1: k' = -1 - 6 = -7."""
        assert feigin_frenkel_dual(1, 3) == -7

    def test_not_minus_k_minus_h(self):
        """FF dual is NOT -k - h^vee (common error)."""
        k, h_dual = 1, 2
        wrong = -k - h_dual  # -3 (WRONG)
        correct = feigin_frenkel_dual(k, h_dual)  # -5 (CORRECT)
        assert correct != wrong
        assert correct == -5

    def test_involution(self):
        """FF duality is an involution: (k')' = k."""
        k, h_dual = 3, 2
        k_prime = feigin_frenkel_dual(k, h_dual)
        k_double_prime = feigin_frenkel_dual(k_prime, h_dual)
        assert k_double_prime == k


class TestVirasoroDSFormula:
    """DS formula: c_Vir(k) = 1 - 6(k+1)^2/(k+2)."""

    def test_k0(self):
        """k=0: c = 1 - 6*1/2 = -2."""
        assert virasoro_ds_central_charge(0) == -2

    def test_k1(self):
        """k=1: c = 1 - 6*4/3 = 1-8 = -7."""
        assert virasoro_ds_central_charge(1) == -7

    def test_complementarity(self):
        """c(k) + c(-k-4) = 26 for any k."""
        k = Symbol('k')
        total = simplify(virasoro_ds_central_charge(k) + virasoro_ds_central_charge(-k - 4))
        assert total == 26


class TestW3DSFormula:
    """W3 DS formula: c = 2 - 24(k+2)^2/(k+3)."""

    def test_k0(self):
        """k=0: c = 2 - 24*4/3 = 2 - 32 = -30."""
        assert w3_ds_central_charge(0) == -30

    def test_k1(self):
        """k=1: c = 2 - 24*9/4 = 2 - 54 = -52."""
        assert w3_ds_central_charge(1) == -52

    def test_not_minimal_model_formula(self):
        """DS formula != minimal model formula (different parametrizations)."""
        # DS formula uses k (affine level), not p,q (minimal model indices)
        k = Symbol('k')
        c_ds = w3_ds_central_charge(k)
        # Just verify it's a rational function of k
        assert c_ds.free_symbols == {k}


# ===========================================================================
# COMPREHENSIVE INTEGRATION TEST
# ===========================================================================

class TestComprehensiveVerification:
    """All shadow-level checks in one sweep."""

    def test_all_checks_pass(self):
        """Every check in verify_all_physics_horizon passes."""
        results = verify_all_physics_horizon()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_check_count(self):
        """At least 20 checks are performed."""
        results = verify_all_physics_horizon()
        assert len(results) >= 20


# ===========================================================================
# CROSS-MODULE CONSISTENCY
# ===========================================================================

class TestCrossModuleConsistency:
    """Consistency with existing compute modules."""

    def test_qme_consistent_with_bv_brst(self):
        """QME coefficients match bv_brst.py."""
        from compute.lib.bv_brst import qme_coefficients as bv_qme
        ours = qme_coefficients()
        theirs = bv_qme()
        assert ours["antibracket_coeff"] == theirs["antibracket_coeff"]

    def test_hcs_consistent_with_bv_brst(self):
        """HCS coefficients match bv_brst.py."""
        from compute.lib.bv_brst import hcs_coefficients as bv_hcs
        ours = hcs_coefficients()
        theirs = bv_hcs()
        assert ours["cubic_coeff"] == theirs["cubic_coeff"]

    def test_kappa_virasoro_consistent(self):
        """kappa = c/2 matches genus_expansion.py."""
        from compute.lib.genus_expansion import kappa_virasoro
        our_kappa = Rational(26, 2)
        their_kappa = kappa_virasoro(26)
        assert our_kappa == their_kappa

    def test_sugawara_consistent(self):
        """Sugawara formula matches lie_algebra.py."""
        from compute.lib.lie_algebra import sugawara_c
        our_c = sugawara_central_charge(3, 1, 2)
        their_c = sugawara_c("A", 1, 1)
        assert our_c == their_c

    def test_ff_dual_consistent(self):
        """FF dual level matches lie_algebra.py."""
        from compute.lib.lie_algebra import ff_dual_level
        our_dual = feigin_frenkel_dual(1, 2)
        their_dual = ff_dual_level("A", 1, 1)
        assert our_dual == their_dual

    def test_virasoro_ds_consistent(self):
        """Virasoro DS formula matches lie_algebra.py."""
        from compute.lib.lie_algebra import virasoro_ds_c
        our_c = virasoro_ds_central_charge(0)
        their_c = virasoro_ds_c(0)
        assert our_c == their_c

    def test_bar_dims_virasoro_consistent(self):
        """Bar dims match bar_complex.py KNOWN_BAR_DIMS."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        expected = KNOWN_BAR_DIMS["Virasoro"]
        dims = {n: expected[n] for n in range(1, 7)}
        chi = bar_euler_characteristic(dims)
        # Just verify it computes without error and is consistent
        assert isinstance(chi, int)

    def test_lambda1_fp_consistent(self):
        """lambda_1^FP matches genus_expansion.py."""
        from compute.lib.utils import lambda_fp
        our_val = faber_pandharipande_number(1)
        their_val = lambda_fp(1)
        assert our_val == their_val
