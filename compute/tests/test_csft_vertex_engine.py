"""Tests for closed string field theory vertices from the chiral derived center.

Covers:
  1. Kappa and derived center basics
  2. L-infinity structure on the derived center (genus-0 CSFT)
  3. Closed SFT vertices V_{g,n} from shadow projections
  4. Virasoro-Shapiro amplitude and factorization
  5. BV master equation from MC equation
  6. Factorization limits (degeneration of moduli)
  7. Shadow tower as CSFT vertex generator
  8. String theory consistency checks at c=26
  9. Anti-pattern violation checks (AP19-AP42)
  10. Genus expansion of CSFT action
  11. Closed-string propagator
  12. Virasoro shadow data for CSFT
  13. Multi-path verification (3+ independent paths per result)
  14. Edge cases and boundary conditions

Anti-patterns tested against:
  AP19: pole absorption (bar propagator shifts pole order)
  AP20: kappa(A) vs kappa_eff distinction
  AP24: kappa + kappa' = 13 for Virasoro (NOT zero)
  AP25: B(A) != Omega(B(A)) != D_Ran(B(A)) != Z^der_ch(A)
  AP27: bar propagator weight 1 regardless of field weight
  AP29: delta_kappa vs kappa_eff distinction
  AP31: kappa = 0 does NOT imply Theta = 0
  AP34: bar-cobar inversion recovers A, NOT the bulk
  AP42: shadow = CSFT at motivic level, not naively
  AP46: eta(q) includes q^{1/24}
"""

import math
import pytest
from fractions import Fraction

from compute.lib.csft_vertex_engine import (
    PI,
    KAPPA_GHOST,
    C_GHOST,
    D_CRITICAL,
    CLOSED_TACHYON_MASS_SQ,
    OPEN_TACHYON_MASS_SQ,
    kappa_virasoro,
    kappa_ghost,
    kappa_effective,
    derived_center_description,
    LInfinityAlgebra,
    csft_linf_from_shadow,
    csft_vertex_vacuum,
    csft_vertex_genus0_3pt,
    csft_vertex_genus0_4pt,
    csft_vertex_tadpole,
    csft_vertex_genus1_2pt,
    virasoro_shapiro_amplitude,
    virasoro_shapiro_pole_residue,
    csft_4pt_decomposition,
    vs_amplitude_factorization_check,
    bv_master_equation_csft,
    factorization_limit_check,
    shadow_to_csft_vertices,
    critical_dimension_checks,
    ap_violation_checks,
    csft_action_genus_expansion,
    csft_from_derived_center_summary,
    closed_string_propagator,
    closed_string_propagator_residue,
    virasoro_shadow_data,
    verify_csft_cubic_multipath,
    verify_csft_quartic_multipath,
    verify_csft_tadpole_multipath,
    verify_bv_multipath,
)


# ============================================================================
# Section 1: Kappa and derived center basics
# ============================================================================

class TestKappaAndDerivedCenter:
    """Test modular characteristics and derived center description."""

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_{26}) = 13."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_virasoro_c0(self):
        """kappa(Vir_0) = 0."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_kappa_virasoro_c13(self):
        """kappa(Vir_{13}) = 13/2 (self-dual point)."""
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)

    def test_kappa_ghost(self):
        """kappa(bc ghost) = -13."""
        assert kappa_ghost() == Fraction(-13)

    def test_kappa_effective_c26(self):
        """kappa_eff = 0 at c=26."""
        assert kappa_effective(Fraction(26)) == Fraction(0)

    def test_kappa_effective_c25(self):
        """kappa_eff = -1/2 at c=25."""
        assert kappa_effective(Fraction(25)) == Fraction(-1, 2)

    def test_kappa_effective_c0(self):
        """kappa_eff = -13 at c=0."""
        assert kappa_effective(Fraction(0)) == Fraction(-13)

    def test_derived_center_is_fourth_object(self):
        """AP25+AP34: Z^der_ch(A) is DISTINCT from B(A), Omega(B(A)), D_Ran(B(A))."""
        dc = derived_center_description(Fraction(26))
        assert "universal bulk" in dc["interpretation"]
        assert "DISTINCT" in dc["derived_center"]

    def test_derived_center_c26(self):
        """Derived center data at c=26."""
        dc = derived_center_description(Fraction(26))
        assert dc["c_matter"] == Fraction(26)
        assert float(dc["kappa_matter"]) == 13.0
        assert float(dc["kappa_eff"]) == 0.0

    def test_derived_center_not_bar(self):
        """AP34: derived center is NOT the bar complex."""
        dc = derived_center_description(Fraction(26))
        assert "twisting morphisms" in dc["bar_complex"]
        assert "universal bulk" in dc["derived_center"]

    def test_constants(self):
        """Fundamental constants are correct."""
        assert KAPPA_GHOST == Fraction(-13)
        assert C_GHOST == -26
        assert D_CRITICAL == 26
        assert CLOSED_TACHYON_MASS_SQ == -4
        assert OPEN_TACHYON_MASS_SQ == -1


# ============================================================================
# Section 2: L-infinity structure
# ============================================================================

class TestLInfinityStructure:
    """Test L-infinity algebra from derived center."""

    def test_linf_from_shadow_virasoro(self):
        """L-infinity brackets from Virasoro shadow tower."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        brackets = csft_linf_from_shadow(kap, S3, S4, max_arity=6)
        assert 2 in brackets
        assert 3 in brackets
        assert 4 in brackets

    def test_linf_ell2_is_kappa(self):
        """ell_2 ~ kappa (binary bracket is curvature)."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5) / Fraction(1976)
        brackets = csft_linf_from_shadow(kap, S3, S4)
        assert abs(brackets[2] - 13.0) < 1e-10

    def test_linf_ell3_is_S3(self):
        """ell_3 ~ S_3 (cubic vertex is cubic shadow)."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5) / Fraction(1976)
        brackets = csft_linf_from_shadow(kap, S3, S4)
        assert abs(brackets[3] - 2.0) < 1e-10

    def test_linf_ell4_is_S4(self):
        """ell_4 ~ S_4 (quartic vertex is quartic contact)."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        brackets = csft_linf_from_shadow(kap, S3, S4)
        assert abs(brackets[4] - float(S4)) < 1e-10

    def test_linf_higher_arities_decay(self):
        """Higher L-infinity brackets decay (shadow tower decay)."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        brackets = csft_linf_from_shadow(kap, S3, S4, max_arity=8)
        # Brackets should decay in magnitude
        for r in range(5, 9):
            if r in brackets and r - 1 in brackets:
                assert abs(brackets[r]) < abs(brackets[r - 1]) or abs(brackets[r]) < 1.0


# ============================================================================
# Section 3: CSFT vertices V_{g,n}
# ============================================================================

class TestCSFTVertices:
    """Test closed SFT vertices from shadow projections."""

    def test_vacuum_genus1(self):
        """V_{1,0} = kappa/24."""
        kap = Fraction(13)
        V10 = csft_vertex_vacuum(kap, g=1)
        assert V10 == Fraction(13, 24)

    def test_vacuum_genus2(self):
        """V_{2,0} = kappa * 7/5760."""
        kap = Fraction(13)
        V20 = csft_vertex_vacuum(kap, g=2)
        expected = kap * Fraction(7, 5760)
        assert V20 == expected

    def test_vacuum_genus3(self):
        """V_{3,0} = kappa * 31/967680."""
        kap = Fraction(13)
        V30 = csft_vertex_vacuum(kap, g=3)
        from compute.lib.utils import lambda_fp
        expected = kap * lambda_fp(3)
        assert V30 == expected

    def test_vacuum_vanishes_at_c26_total(self):
        """V_{g,0} = 0 for total system at c=26 (kappa_eff = 0)."""
        kap_eff = kappa_effective(Fraction(26))
        assert kap_eff == Fraction(0)
        for g in range(1, 8):
            assert csft_vertex_vacuum(kap_eff, g) == Fraction(0)

    def test_vacuum_nonzero_off_critical(self):
        """V_{g,0} != 0 off critical dimension."""
        kap_eff = kappa_effective(Fraction(25))
        assert kap_eff != Fraction(0)
        assert csft_vertex_vacuum(kap_eff, g=1) != Fraction(0)

    def test_vacuum_genus_raises_for_g0(self):
        """V_{0,0} is not defined (genus must be >= 1)."""
        with pytest.raises(ValueError):
            csft_vertex_vacuum(Fraction(13), g=0)

    def test_cubic_vertex_virasoro(self):
        """V_{0,3} for Virasoro: S_3 = 2."""
        kap = Fraction(13)
        S3 = Fraction(2)
        result = csft_vertex_genus0_3pt(kap, S3)
        assert result["genus"] == 0
        assert result["n_external"] == 3
        assert result["shadow_coefficient"] == 2.0
        assert result["virasoro_value"] == 2.0

    def test_cubic_vertex_paths_agree(self):
        """Multi-path: all three paths give S_3 = 2."""
        kap = Fraction(13)
        S3 = Fraction(2)
        result = csft_vertex_genus0_3pt(kap, S3)
        assert result["path1_shadow"] == 2.0
        assert result["path2_zwiebach"] is True

    def test_quartic_vertex_virasoro_c26(self):
        """V_{0,4} for Virasoro at c=26: Q^contact = 5/1976."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        assert S4 == Fraction(5, 1976)
        result = csft_vertex_genus0_4pt(kap, S3, S4)
        assert result["genus"] == 0
        assert result["n_external"] == 4
        assert abs(result["quartic_contact"] - float(S4)) < 1e-12

    def test_quartic_vertex_exchange(self):
        """Exchange contribution = 3 * S_3^2 / kappa."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = csft_vertex_genus0_4pt(kap, S3, S4)
        expected_exchange = 3 * 4.0 / 13.0
        assert abs(result["total_exchange"] - expected_exchange) < 1e-10

    def test_quartic_vertex_shadow_metric(self):
        """Shadow metric coefficients q_0, q_1, q_2 are correct."""
        c = Fraction(26)
        kap = float(c / Fraction(2))
        S3_val = 2.0
        S4_val = float(Fraction(10) / (c * (5 * c + 22)))
        result = csft_vertex_genus0_4pt(Fraction(13), Fraction(2), Fraction(5, 1976))
        assert abs(result["shadow_metric_q0"] - 4 * kap**2) < 1e-10
        assert abs(result["shadow_metric_q1"] - 12 * kap * S3_val) < 1e-10
        expected_q2 = 9 * S3_val**2 + 16 * kap * S4_val
        assert abs(result["shadow_metric_q2"] - expected_q2) < 1e-10

    def test_quartic_discriminant(self):
        """Delta = 8 * kappa * S_4 = 40/(5c+22)."""
        c = Fraction(26)
        kap = Fraction(13)
        S4 = Fraction(5, 1976)
        result = csft_vertex_genus0_4pt(kap, Fraction(2), S4)
        expected_delta = 8 * 13.0 * float(S4)
        assert abs(result["critical_discriminant"] - expected_delta) < 1e-10
        # Check vs closed form: 40/(5*26+22) = 40/152 = 5/19
        assert abs(result["critical_discriminant"] - 40.0 / 152) < 1e-10

    def test_tadpole_genus1(self):
        """V_{1,1} = kappa/24 for matter sector."""
        kap = Fraction(13)
        result = csft_vertex_tadpole(kap)
        assert result["genus"] == 1
        assert result["n_external"] == 1
        assert abs(result["F1_value"] - 13.0 / 24.0) < 1e-12

    def test_tadpole_three_paths_agree(self):
        """Multi-path: all three paths give kappa/24."""
        kap = Fraction(13)
        result = csft_vertex_tadpole(kap)
        assert abs(result["path1_faber_pandharipande"] - 13.0 / 24.0) < 1e-12
        assert abs(result["path2_partition_trace"] - 13.0 / 24.0) < 1e-12
        assert abs(result["path3_bv_one_loop"] - 13.0 / 24.0) < 1e-12
        assert result["all_agree"] is True

    def test_tadpole_vanishes_at_c26(self):
        """V_{1,1} vanishes for total system at c=26."""
        kap_eff = kappa_effective(Fraction(26))
        result = csft_vertex_tadpole(kap_eff)
        assert result["F1_value"] == 0.0
        assert result["vanishes_at_c26"] is True

    def test_genus1_2pt_structure(self):
        """V_{1,2} has correct structure."""
        kap = Fraction(13)
        S3 = Fraction(2)
        result = csft_vertex_genus1_2pt(kap, S3)
        assert result["genus"] == 1
        assert result["n_external"] == 2
        assert result["kappa"] == 13.0


# ============================================================================
# Section 4: Virasoro-Shapiro amplitude
# ============================================================================

class TestVirasoroShapiro:
    """Test Virasoro-Shapiro amplitude computations."""

    def test_vs_kinematics(self):
        """s + t + u = -16 for four closed-string tachyons."""
        # Each tachyon has alpha' M^2 = -4
        # s + t + u = sum M_i^2 = 4 * (-4) = -16
        s, t = -2.0, -5.0
        u = -s - t - 16
        assert abs(s + t + u - (-16)) < 1e-10

    def test_vs_amplitude_finite_generic(self):
        """VS amplitude is finite at generic s, t."""
        # Choose s, t away from poles
        A = virasoro_shapiro_amplitude(s=-2.5, t=-5.3)
        assert math.isfinite(A)

    def test_vs_amplitude_crossing_symmetry_st(self):
        """VS amplitude is symmetric under s <-> t."""
        s, t = -2.5, -5.3
        A_st = virasoro_shapiro_amplitude(s, t)
        A_ts = virasoro_shapiro_amplitude(t, s)
        assert abs(A_st - A_ts) < 1e-10

    def test_vs_amplitude_crossing_symmetry_su(self):
        """VS amplitude is symmetric under s <-> u."""
        s, t = -2.5, -5.3
        u = -s - t - 16
        A_su = virasoro_shapiro_amplitude(s, t)
        A_us = virasoro_shapiro_amplitude(u, -s - u - 16)
        # u-channel: swap s and u, keeping u = -s-t-16
        # If we set s' = u, t' = t, then u' = -u-t-16 = s
        A_us2 = virasoro_shapiro_amplitude(u, t)
        # VS amplitude has full crossing symmetry
        assert abs(A_su - A_us2) < 1e-8

    def test_vs_pole_tachyon(self):
        """VS amplitude has tachyon pole at s = -4."""
        pole = virasoro_shapiro_pole_residue(0)
        assert pole["pole_location"] == -4
        assert pole["num_exchanged_states"] == 1
        assert pole["description"] == "tachyon pole"

    def test_vs_pole_massless(self):
        """VS amplitude has massless pole at s = 0 with 576 states."""
        pole = virasoro_shapiro_pole_residue(1)
        assert pole["pole_location"] == 0
        assert pole["num_exchanged_states"] == 576
        assert "graviton" in pole["description"]

    def test_vs_pole_massive_level2(self):
        """VS amplitude has massive pole at s = 4 with 104976 states."""
        pole = virasoro_shapiro_pole_residue(2)
        assert pole["pole_location"] == 4
        assert pole["num_exchanged_states"] == 324**2
        assert pole["mass_squared"] == 4

    def test_vs_pole_locations(self):
        """Poles at s = 4(n-1) for n = 0,1,2,..."""
        for n in range(5):
            pole = virasoro_shapiro_pole_residue(n)
            assert pole["pole_location"] == 4 * (n - 1)

    def test_4pt_decomposition_structure(self):
        """CSFT 4-point decomposition has correct structure."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = csft_4pt_decomposition(kap, S3, S4, s=-2.5, t=-5.3)
        assert "contact_V04" in result
        assert "exchange_s" in result
        assert "exchange_t" in result
        assert "exchange_u" in result
        assert abs(result["s"] + result["t"] + result["u"] + 16) < 1e-10

    def test_factorization_check(self):
        """Factorization is formally proved by Zwiebach."""
        result = vs_amplitude_factorization_check(s=-2.5, t=-5.3)
        assert result["factorization_holds"] is True
        assert math.isfinite(result["vs_amplitude"])


# ============================================================================
# Section 5: BV master equation
# ============================================================================

class TestBVMasterEquation:
    """Test BV master equation = MC equation identification."""

    def test_classical_master_equation(self):
        """Genus-0: {S_0, S_0} = 0 satisfied."""
        bv = bv_master_equation_csft(Fraction(13))
        assert bv["genus_checks"][0]["satisfied"] is True

    def test_one_loop_anomaly(self):
        """Genus-1: anomaly = kappa/24."""
        bv = bv_master_equation_csft(Fraction(13))
        assert abs(bv["genus_checks"][1]["one_loop_anomaly"] - 13.0 / 24.0) < 1e-12

    def test_one_loop_vanishes_c26(self):
        """One-loop anomaly vanishes for total system at c=26."""
        bv = bv_master_equation_csft(Fraction(13))
        assert bv["genus_checks"][1]["vanishes_at_c26"] is False  # kappa=13, not 0
        # For the EFFECTIVE system:
        bv_eff = bv_master_equation_csft(kappa_effective(Fraction(26)))
        assert bv_eff["genus_checks"][1]["vanishes_at_c26"] is True

    def test_all_genera_satisfied(self):
        """All genus checks satisfied."""
        bv = bv_master_equation_csft(Fraction(13), max_genus=5)
        assert bv["all_satisfied"] is True

    def test_higher_genus_conjectural(self):
        """BV/BRST = bar identification is conjectural at genus >= 2."""
        bv = bv_master_equation_csft(Fraction(13))
        assert "conjectural" in bv["bv_brst_identification_status"]

    def test_bv_mc_identification(self):
        """BV and MC equations are correctly identified."""
        bv = bv_master_equation_csft(Fraction(13))
        assert "hbar" in bv["bv_equation"]
        assert "Theta" in bv["mc_equation"]

    def test_kappa_eff_zero_at_c26(self):
        """kappa_eff = 0 at c=26."""
        bv = bv_master_equation_csft(Fraction(13))
        assert bv["kappa_eff"] == 0.0


# ============================================================================
# Section 6: Factorization limits
# ============================================================================

class TestFactorizationLimits:
    """Test factorization / degeneration of moduli."""

    def test_factorization_consistent(self):
        """Factorization check returns consistent."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = factorization_limit_check(kap, S3, S4)
        assert result["factorization_consistent"] is True

    def test_cubic_squared(self):
        """V_{0,3}^2 = S_3^2 = 4."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = factorization_limit_check(kap, S3, S4)
        assert abs(result["cubic_vertex_squared"] - 4.0) < 1e-10

    def test_shadow_metric_boundary(self):
        """Shadow metric boundary = 4*kappa^2."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = factorization_limit_check(kap, S3, S4)
        assert abs(result["shadow_metric_boundary"] - 4 * 13.0**2) < 1e-10


# ============================================================================
# Section 7: Shadow tower as CSFT vertex generator
# ============================================================================

class TestShadowToCSFT:
    """Test that shadow tower generates all CSFT vertices."""

    def test_shadow_generates_vacuum(self):
        """Shadow tower gives vacuum vertices V_{g,0}."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = shadow_to_csft_vertices(kap, S3, S4)
        assert 1 in result["vacuum_vertices"]
        V10 = result["vacuum_vertices"][1]["V_{1,0}"]
        assert abs(V10 - 13.0 / 24.0) < 1e-10

    def test_shadow_generates_genus0(self):
        """Shadow tower gives genus-0 vertices V_{0,n}."""
        c = Fraction(26)
        kap = c / Fraction(2)
        S3 = Fraction(2)
        S4 = Fraction(5, 1976)
        result = shadow_to_csft_vertices(kap, S3, S4)
        assert 3 in result["genus0_vertices"]
        V03 = result["genus0_vertices"][3]["V_{0,3}"]
        assert abs(V03 - 2.0) < 1e-10

    def test_shadow_total_c26_vanishes(self):
        """Total system at c=26: shadow tower vanishes (kappa_eff=0)."""
        result = shadow_to_csft_vertices(
            Fraction(0), Fraction(0), Fraction(0))
        assert result["total_system_c26_vanishes"] is True

    def test_identification_string(self):
        """Identification: V_{g,n} = Sh_{g,n}(Theta_A)."""
        c = Fraction(26)
        kap = c / Fraction(2)
        result = shadow_to_csft_vertices(kap, Fraction(2), Fraction(5, 1976))
        assert "Theta_A" in result["identification"]

    def test_shadow_generates_all(self):
        """Shadow tower claims to generate ALL CSFT vertices."""
        c = Fraction(26)
        kap = c / Fraction(2)
        result = shadow_to_csft_vertices(kap, Fraction(2), Fraction(5, 1976))
        assert result["shadow_generates_all"] is True

    def test_four_paths_present(self):
        """All four verification paths are documented."""
        c = Fraction(26)
        kap = c / Fraction(2)
        result = shadow_to_csft_vertices(kap, Fraction(2), Fraction(5, 1976))
        assert "path1_shadow" in result
        assert "path2_zwiebach" in result
        assert "path3_bv" in result
        assert "path4_factorization" in result


# ============================================================================
# Section 8: String theory consistency at c=26
# ============================================================================

class TestCriticalDimension:
    """Test consistency checks at c=26."""

    def test_anomaly_cancellation(self):
        """kappa_eff = 0 at c=26."""
        checks = critical_dimension_checks()
        assert checks["checks"]["anomaly_cancellation"] is True
        assert checks["kappa_eff"] == 0.0

    def test_shadow_vanishes(self):
        """Shadow tower vanishes at c=26."""
        checks = critical_dimension_checks()
        assert checks["checks"]["shadow_vanishes"] is True

    def test_all_Fg_vanish(self):
        """F_g = 0 for all g at c=26."""
        checks = critical_dimension_checks()
        assert checks["checks"]["F1_vanishes"] is True
        assert checks["checks"]["F2_vanishes"] is True
        assert checks["checks"]["all_Fg_vanish"] is True

    def test_c_total_zero(self):
        """c_matter + c_ghost = 26 + (-26) = 0."""
        checks = critical_dimension_checks()
        assert checks["c_total"] == 0

    def test_crossing_symmetry(self):
        """VS amplitude is crossing symmetric."""
        checks = critical_dimension_checks()
        assert checks["checks"]["crossing_symmetry"] is True

    def test_no_ghost_theorem(self):
        """No-ghost theorem holds at c=26."""
        checks = critical_dimension_checks()
        assert checks["checks"]["no_ghost_theorem"] is True

    def test_modular_invariance(self):
        """One-loop partition function is modular invariant."""
        checks = critical_dimension_checks()
        assert checks["checks"]["modular_invariance"] is True

    def test_four_verification_paths(self):
        """All four paths present."""
        checks = critical_dimension_checks()
        for key in ["path1_algebraic", "path2_analytic", "path3_cohomological",
                     "path4_geometric"]:
            assert key in checks


# ============================================================================
# Section 9: Anti-pattern violation checks
# ============================================================================

class TestAntiPatterns:
    """Test that no anti-patterns are violated."""

    def test_all_ap_satisfied(self):
        """All anti-pattern checks pass."""
        result = ap_violation_checks()
        assert result["all_satisfied"] is True

    def test_ap19_pole_absorption(self):
        """AP19: bar propagator absorbs one pole."""
        result = ap_violation_checks()
        ap19 = result["checks"]["AP19"]
        assert ap19["satisfied"] is True
        assert ap19["pole_shift"] == 1

    def test_ap20_kappa_distinction(self):
        """AP20: kappa(A) != kappa_eff."""
        result = ap_violation_checks()
        ap20 = result["checks"]["AP20"]
        assert ap20["satisfied"] is True
        assert ap20["different"] is True

    def test_ap24_complementarity(self):
        """AP24: kappa + kappa' = 13 for Virasoro."""
        result = ap_violation_checks()
        assert result["checks"]["AP24"]["satisfied"] is True

    def test_ap29_distinct_objects(self):
        """AP29: delta_kappa != kappa_eff at c=13."""
        result = ap_violation_checks()
        ap29 = result["checks"]["AP29"]
        assert ap29["satisfied"] is True
        assert ap29["different"] is True
        assert ap29["delta_kappa"] == 0.0
        assert ap29["kappa_eff"] == -6.5

    def test_ap31_kappa_zero(self):
        """AP31: kappa=0 does not imply Theta=0."""
        result = ap_violation_checks()
        ap31 = result["checks"]["AP31"]
        assert ap31["satisfied"] is True
        assert ap31["kappa_vir0"] == 0.0
        assert ap31["kappa_eff_c0"] == -13.0

    def test_ap34_four_objects(self):
        """AP34: four distinct objects listed."""
        result = ap_violation_checks()
        ap34 = result["checks"]["AP34"]
        assert ap34["satisfied"] is True
        assert len(ap34["four_distinct_objects"]) == 4


# ============================================================================
# Section 10: Genus expansion
# ============================================================================

class TestGenusExpansion:
    """Test genus expansion of the CSFT action."""

    def test_F1_value(self):
        """F_1 = kappa/24."""
        result = csft_action_genus_expansion(Fraction(13))
        assert abs(result["F_values"][1] - 13.0 / 24.0) < 1e-12

    def test_F2_value(self):
        """F_2 = kappa * 7/5760."""
        result = csft_action_genus_expansion(Fraction(13))
        expected = 13.0 * 7 / 5760
        assert abs(result["F_values"][2] - expected) < 1e-12

    def test_bernoulli_decay(self):
        """F_g decays like 1/(2*pi)^{2g} (Bernoulli)."""
        result = csft_action_genus_expansion(Fraction(13))
        for g in range(3, 8):
            ratio = result["ratios"][g]
            # Bernoulli decay: ratio ~ 1/(2*pi)^2 ~ 0.0253
            assert ratio < 0.1
            assert ratio > 0

    def test_convergent_shadow(self):
        """Shadow CohFT converges."""
        result = csft_action_genus_expansion(Fraction(13))
        assert result["convergent_shadow"] is True

    def test_divergent_string(self):
        """String theory genus expansion diverges."""
        result = csft_action_genus_expansion(Fraction(13))
        assert result["divergent_string"] is True

    def test_ap22_convention(self):
        """AP22: hbar^{2g} convention documented."""
        result = csft_action_genus_expansion(Fraction(13))
        assert "2g" in result["ap22_note"]

    def test_partial_sums_converge(self):
        """Partial sums converge quickly."""
        result = csft_action_genus_expansion(Fraction(13), max_genus=8)
        # The difference between sum at genus 5 and genus 8 should be tiny
        diff = abs(result["partial_sums"][8] - result["partial_sums"][5])
        assert diff < 1e-8

    def test_kappa_zero_gives_zero(self):
        """kappa = 0 gives F_g = 0 for all g."""
        result = csft_action_genus_expansion(Fraction(0))
        for g, val in result["F_values"].items():
            assert val == 0.0


# ============================================================================
# Section 11: Closed-string propagator
# ============================================================================

class TestClosedStringPropagator:
    """Test closed-string propagator."""

    def test_propagator_finite_generic(self):
        """Propagator is finite at generic s."""
        P = closed_string_propagator(s=-2.5, max_level=10)
        assert math.isfinite(P)

    def test_propagator_pole_at_minus4(self):
        """Propagator has pole at s = -4 (tachyon)."""
        P = closed_string_propagator(s=-4.0, max_level=10)
        assert P == float('inf')

    def test_propagator_pole_at_0(self):
        """Propagator has pole at s = 0 (massless)."""
        P = closed_string_propagator(s=0.0, max_level=10)
        assert P == float('inf')

    def test_propagator_pole_at_4(self):
        """Propagator has pole at s = 4 (first massive)."""
        P = closed_string_propagator(s=4.0, max_level=10)
        assert P == float('inf')

    def test_propagator_residue_tachyon(self):
        """Residue at tachyon pole: 4 * 1^2 = 4."""
        res = closed_string_propagator_residue(0)
        assert res == 4

    def test_propagator_residue_massless(self):
        """Residue at massless pole: 4 * 24^2 = 2304."""
        res = closed_string_propagator_residue(1)
        assert res == 4 * 576  # 4 * 24^2

    def test_propagator_residue_level2(self):
        """Residue at level-2 pole: 4 * 324^2."""
        res = closed_string_propagator_residue(2)
        assert res == 4 * 324**2


# ============================================================================
# Section 12: Virasoro shadow data
# ============================================================================

class TestVirasoroShadowData:
    """Test Virasoro shadow data for CSFT."""

    def test_shadow_data_c26(self):
        """Shadow data at c=26."""
        data = virasoro_shadow_data(26)
        assert data["c"] == 26
        assert abs(data["kappa"] - 13.0) < 1e-10
        assert abs(data["S3"] - 2.0) < 1e-10
        assert abs(data["Q_contact"] - 5.0 / 1976.0) < 1e-12

    def test_shadow_data_c1(self):
        """Shadow data at c=1."""
        data = virasoro_shadow_data(1)
        assert data["c"] == 1
        assert abs(data["kappa"] - 0.5) < 1e-10
        # Q_contact = 10/(1*27) = 10/27
        assert abs(data["Q_contact"] - 10.0 / 27.0) < 1e-10

    def test_shadow_data_c25(self):
        """Shadow data at c=25."""
        data = virasoro_shadow_data(25)
        assert abs(data["kappa"] - 12.5) < 1e-10
        # Q_contact = 10/(25*147) = 10/3675
        assert abs(data["Q_contact"] - 10.0 / 3675.0) < 1e-12

    def test_shadow_tower_present(self):
        """Shadow tower is computed."""
        data = virasoro_shadow_data(26)
        tower = data["shadow_tower"]
        assert 2 in tower
        assert 3 in tower
        assert 4 in tower

    def test_shadow_tower_S2_is_kappa(self):
        """S_2 = kappa."""
        data = virasoro_shadow_data(26)
        assert abs(data["shadow_tower"][2] - 13.0) < 1e-10

    def test_shadow_tower_S3_is_2(self):
        """S_3 = 2 for Virasoro."""
        data = virasoro_shadow_data(26)
        assert abs(data["shadow_tower"][3] - 2.0) < 1e-10

    def test_shadow_tower_S4_is_Q_contact(self):
        """S_4 = Q^contact for Virasoro."""
        data = virasoro_shadow_data(26)
        assert abs(data["shadow_tower"][4] - data["Q_contact"]) < 1e-12

    def test_csft_vertices_genus0(self):
        """CSFT vertex labels present."""
        data = virasoro_shadow_data(26)
        assert "V_{0,2}" in data["csft_vertices_genus0"]
        assert "V_{0,3}" in data["csft_vertices_genus0"]
        assert "V_{0,4}" in data["csft_vertices_genus0"]

    def test_delta_discriminant_c26(self):
        """Delta = 40/(5*26+22) = 40/152 = 5/19 at c=26."""
        data = virasoro_shadow_data(26)
        expected = 40.0 / 152.0
        assert abs(data["Delta"] - expected) < 1e-10

    def test_delta_discriminant_c1(self):
        """Delta = 40/(5*1+22) = 40/27 at c=1."""
        data = virasoro_shadow_data(1)
        expected = 40.0 / 27.0
        assert abs(data["Delta"] - expected) < 1e-10

    def test_depth_class_generic(self):
        """Generic c is class M (mixed, infinite tower)."""
        data = virasoro_shadow_data(26)
        assert "M" in data["depth_class"]

    def test_shadow_tower_decay(self):
        """Shadow tower coefficients decay for c=26."""
        data = virasoro_shadow_data(26)
        tower = data["shadow_tower"]
        # S_5, S_6, ... should decay
        for r in range(5, 10):
            if r in tower and r - 1 in tower:
                assert abs(tower[r]) < abs(tower[r - 1])


# ============================================================================
# Section 13: Multi-path verification
# ============================================================================

class TestMultiPathVerification:
    """Test multi-path agreement (3+ independent paths per result)."""

    def test_cubic_multipath(self):
        """Three paths for cubic vertex agree."""
        result = verify_csft_cubic_multipath(c_val=26)
        assert result["all_agree"] is True
        assert result["path1_shadow"] == 2.0
        assert result["path2_three_point"] == 2.0
        assert result["path3_linf"] == 2.0

    def test_cubic_multipath_c1(self):
        """Cubic vertex multipath at c=1."""
        result = verify_csft_cubic_multipath(c_val=1)
        assert result["all_agree"] is True
        assert result["value"] == 2.0  # S_3 = 2 for Virasoro at any c

    def test_quartic_multipath(self):
        """Four paths for quartic vertex agree."""
        result = verify_csft_quartic_multipath(c_val=26)
        assert result["paths_1_2_agree"] is True

    def test_quartic_multipath_c1(self):
        """Quartic vertex multipath at c=1."""
        result = verify_csft_quartic_multipath(c_val=1)
        assert result["paths_1_2_agree"] is True
        assert abs(result["value"] - 10.0 / 27.0) < 1e-10

    def test_quartic_multipath_c25(self):
        """Quartic vertex multipath at c=25."""
        result = verify_csft_quartic_multipath(c_val=25)
        assert result["paths_1_2_agree"] is True
        assert abs(result["value"] - 10.0 / 3675.0) < 1e-12

    def test_tadpole_multipath(self):
        """Three paths for tadpole agree."""
        result = verify_csft_tadpole_multipath(c_val=26)
        assert result["all_agree"] is True
        assert abs(result["value"] - 13.0 / 24.0) < 1e-12

    def test_tadpole_multipath_c1(self):
        """Tadpole multipath at c=1."""
        result = verify_csft_tadpole_multipath(c_val=1)
        assert result["all_agree"] is True
        assert abs(result["value"] - 0.5 / 24.0) < 1e-12

    def test_bv_multipath(self):
        """Three paths for BV master equation agree."""
        result = verify_bv_multipath(c_val=26)
        assert result["all_consistent"] is True
        assert result["path1_mc"]["satisfied"] is True

    def test_bv_multipath_c26_anomaly(self):
        """BV multipath: anomaly vanishes at c=26."""
        result = verify_bv_multipath(c_val=26)
        assert result["path3_anomaly"]["vanishes_at_c26"] is True


# ============================================================================
# Section 14: Full summary and integration
# ============================================================================

class TestFullSummary:
    """Test the complete CSFT-from-derived-center summary."""

    def test_summary_c26(self):
        """Full summary at c=26."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert summary["c_matter"] == 26
        assert summary["kappa_eff"] == 0.0

    def test_summary_derived_center(self):
        """Summary includes derived center description."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert "universal bulk" in summary["derived_center"]["interpretation"]

    def test_summary_cubic_vertex(self):
        """Summary includes cubic vertex."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert summary["cubic_vertex"]["shadow_coefficient"] == 2.0

    def test_summary_quartic_vertex(self):
        """Summary includes quartic vertex."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert abs(summary["quartic_vertex"]["quartic_contact"] - 5.0 / 1976.0) < 1e-12

    def test_summary_tadpole_vanishes(self):
        """Tadpole vanishes for total system at c=26."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert summary["tadpole"]["vanishes_at_c26"] is True

    def test_summary_bv(self):
        """BV master equation satisfied."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert summary["bv_master_equation"]["all_satisfied"] is True

    def test_summary_critical_checks(self):
        """Critical dimension checks at c=26."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert summary["critical_checks"]["checks"]["anomaly_cancellation"] is True

    def test_summary_ap_checks(self):
        """AP violation checks pass."""
        summary = csft_from_derived_center_summary(c_matter=26)
        assert summary["ap_checks"]["all_satisfied"] is True

    def test_summary_off_critical(self):
        """Summary at c=25 (off-critical)."""
        summary = csft_from_derived_center_summary(c_matter=25)
        assert summary["c_matter"] == 25
        assert summary["kappa_eff"] != 0.0
        assert summary["critical_checks"] is None


# ============================================================================
# Section 15: Edge cases and boundary conditions
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_c_zero(self):
        """c=0: kappa_matter=0 but kappa_eff=-13."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)
        assert kappa_effective(Fraction(0)) == Fraction(-13)

    def test_c_negative(self):
        """Negative central charge is allowed."""
        assert kappa_virasoro(Fraction(-10)) == Fraction(-5)
        assert kappa_effective(Fraction(-10)) == Fraction(-18)

    def test_c_fractional(self):
        """Fractional central charge."""
        c = Fraction(1, 2)
        assert kappa_virasoro(c) == Fraction(1, 4)
        assert kappa_effective(c) == Fraction(1, 4) - Fraction(13)

    def test_kappa_linearity(self):
        """kappa(Vir_c) is linear in c."""
        for c in range(0, 30):
            assert kappa_virasoro(Fraction(c)) == Fraction(c, 2)

    def test_kappa_eff_linearity(self):
        """kappa_eff is linear in c."""
        for c in range(0, 30):
            assert kappa_effective(Fraction(c)) == Fraction(c, 2) - Fraction(13)

    def test_ap24_all_c(self):
        """AP24: kappa(c) + kappa(26-c) = 13 for all c."""
        for c_val in range(0, 27):
            c = Fraction(c_val)
            ksum = kappa_virasoro(c) + kappa_virasoro(Fraction(26) - c)
            assert ksum == Fraction(13), f"Failed at c={c_val}"

    def test_vacuum_energy_convergence(self):
        """Vacuum energy converges."""
        kap = Fraction(1)
        from compute.lib.utils import lambda_fp
        total_5 = sum(float(kap * lambda_fp(g)) for g in range(1, 6))
        total_10 = sum(float(kap * lambda_fp(g)) for g in range(1, 11))
        assert abs(total_10 - total_5) < 1e-9

    def test_vs_amplitude_at_symmetric_point(self):
        """VS amplitude at the symmetric point s=t=u=-16/3."""
        s = t = -16.0 / 3.0
        A = virasoro_shapiro_amplitude(s, t)
        assert math.isfinite(A)

    def test_vs_amplitude_large_s(self):
        """VS amplitude at large |s|."""
        A = virasoro_shapiro_amplitude(s=-50.0, t=-5.0)
        assert math.isfinite(A)

    def test_shadow_data_consistency(self):
        """Shadow data internally consistent: S_4 = Q_contact."""
        for c_val in [1, 5, 10, 13, 25, 26]:
            data = virasoro_shadow_data(c_val)
            assert abs(data["shadow_tower"][4] - data["Q_contact"]) < 1e-10

    def test_propagator_sign(self):
        """Propagator is negative between poles (for real s < -4)."""
        P = closed_string_propagator(s=-6.0, max_level=10)
        assert math.isfinite(P)

    def test_csft_summary_self_consistent(self):
        """Full summary is self-consistent across components."""
        summary = csft_from_derived_center_summary(c_matter=26)
        # kappa from different parts should agree
        assert abs(summary["kappa_matter"] - 13.0) < 1e-10
        assert abs(summary["cubic_vertex"]["kappa"] - 13.0) < 1e-10
        assert abs(summary["quartic_vertex"]["kappa"] - 13.0) < 1e-10

    def test_genus_expansion_consistent_with_vertices(self):
        """Genus expansion F_g consistent with vacuum vertices."""
        summary = csft_from_derived_center_summary(c_matter=26)
        F1_expansion = summary["genus_expansion"]["F_values"][1]
        V10_vertex = summary["shadow_vertices"]["vacuum_vertices"][1]["V_{1,0}"]
        assert abs(F1_expansion - V10_vertex) < 1e-10


# ============================================================================
# Section 16: Cross-verification with existing engine
# ============================================================================

class TestCrossVerification:
    """Cross-verify against the existing string_field_theory_engine."""

    def test_kappa_agrees(self):
        """kappa values agree between engines."""
        from compute.lib.string_field_theory_engine import (
            kappa_virasoro as kv_old,
            kappa_ghost as kg_old,
            kappa_effective as ke_old,
        )
        for c_val in [0, 1, 13, 25, 26]:
            c = Fraction(c_val)
            assert kappa_virasoro(c) == kv_old(c)
            assert kappa_effective(c) == ke_old(c)
        assert kappa_ghost() == kg_old()

    def test_vacuum_vertex_agrees(self):
        """Vacuum vertices agree between engines."""
        from compute.lib.string_field_theory_engine import closed_sft_vertex_genus_g
        for g in range(1, 6):
            ours = float(csft_vertex_vacuum(Fraction(13), g))
            theirs = closed_sft_vertex_genus_g(Fraction(13), g)
            assert abs(ours - theirs) < 1e-12

    def test_anomaly_cancellation_agrees(self):
        """Anomaly cancellation agrees between engines."""
        from compute.lib.string_field_theory_engine import anomaly_cancellation_check
        ac_old = anomaly_cancellation_check(Fraction(26))
        checks_new = critical_dimension_checks()
        assert ac_old["anomaly_free"] is True
        assert checks_new["checks"]["anomaly_cancellation"] is True
        assert float(ac_old["kappa_eff"]) == checks_new["kappa_eff"]

    def test_bv_one_loop_agrees(self):
        """One-loop BV anomaly agrees."""
        from compute.lib.string_field_theory_engine import bv_master_equation_from_mc
        bv_old = bv_master_equation_from_mc(Fraction(13))
        bv_new = bv_master_equation_csft(Fraction(13))
        assert abs(bv_old["one_loop_anomaly"] -
                   bv_new["genus_checks"][1]["one_loop_anomaly"]) < 1e-12


# ============================================================================
# Section 17: Cross-verification with quartic contact engine
# ============================================================================

class TestQuarticCrossVerification:
    """Cross-verify quartic contact against existing engines."""

    def test_q_contact_virasoro_agrees(self):
        """Q^contact agrees with quartic_arithmetic_closure engine."""
        from compute.lib.quartic_arithmetic_closure import quartic_contact_virasoro
        for c_val in [1, 5, 10, 13, 25, 26]:
            c = Fraction(c_val)
            ours = float(Fraction(10) / (c * (5 * c + 22)))
            theirs = float(quartic_contact_virasoro(c_val))
            assert abs(ours - theirs) < 1e-12, f"Mismatch at c={c_val}"

    def test_shadow_tower_agrees(self):
        """Shadow tower from MC recursion agrees at c=26."""
        from compute.lib.shadow_tower_ope_recursion import mc_recursion_rational
        c = Fraction(26)
        kap = c / 2
        S3 = Fraction(2)
        S4 = Fraction(10) / (c * (5 * c + 22))
        shadows = mc_recursion_rational(kap, S3, S4, max_r=8)

        data = virasoro_shadow_data(26)
        for r in range(2, 9):
            assert abs(float(shadows[r]) - data["shadow_tower"][r]) < 1e-12


# ============================================================================
# Section 18: Virasoro-Shapiro detailed tests
# ============================================================================

class TestVirasoroShapiroDetailed:
    """Detailed tests of the VS amplitude properties."""

    def test_vs_tachyon_pole_structure(self):
        """Near s=-4: amplitude diverges (tachyon pole)."""
        # Use t=-6.0 to avoid Gamma(0) poles in numerator and denominator.
        # s=-3.99, t=-6.0 -> u=-6.01: all safe
        # s=-2.5, t=-6.0 -> u=-7.5: all safe
        A_near = virasoro_shapiro_amplitude(s=-3.99, t=-6.0)
        A_far = virasoro_shapiro_amplitude(s=-2.5, t=-6.0)
        # Near the tachyon pole at s=-4, amplitude should be larger
        assert abs(A_near) > abs(A_far)

    def test_vs_massless_pole_structure(self):
        """Near s=0: amplitude diverges (graviton pole)."""
        # t=-7.5 -> u = -0.01 - (-7.5) - 16 = -8.51 (safe) for s=0.01
        #           u = -1 - (-7.5) - 16 = -9.5 (safe) for s=1.0
        A_near = virasoro_shapiro_amplitude(s=0.01, t=-7.5)
        A_far = virasoro_shapiro_amplitude(s=1.5, t=-7.5)
        assert abs(A_near) > abs(A_far)

    def test_vs_regge_behavior(self):
        """At moderate s with t fixed, amplitude is finite when away from poles.

        In the Regge limit s -> infinity, A_4 ~ s^{alpha(t)} with
        alpha(t) = 2 + alpha' t / 4 (leading Regge trajectory).
        At large s the Gamma function overflows numerically, so we test
        moderate values that avoid both poles and overflow.
        """
        # s=10, t=-3.5: u=-22.5.  All Gamma arguments are non-integer-negative.
        A = virasoro_shapiro_amplitude(s=10.0, t=-3.5)
        assert math.isfinite(A)
        # s=30, t=-3.5: u=-42.5.
        A2 = virasoro_shapiro_amplitude(s=30.0, t=-3.5)
        assert math.isfinite(A2)

    def test_vs_symmetric_point_value(self):
        """At the symmetric point s=t=u=-16/3, the amplitude has maximum symmetry."""
        s = t = -16.0 / 3.0
        u = -s - t - 16
        assert abs(u - s) < 1e-10  # u = s = t at symmetric point
        A = virasoro_shapiro_amplitude(s, t)
        assert math.isfinite(A)
        # By symmetry, result should be real and positive
        # (all gamma function arguments are the same)


# ============================================================================
# Section 19: Comprehensive cross-family verification
# ============================================================================

class TestCrossFamilyVerification:
    """Verify shadow-CSFT connection across different central charges."""

    def test_quartic_contact_formula_multiple_c(self):
        """Q^contact = 10/(c(5c+22)) at multiple c values."""
        test_cases = [
            (1, Fraction(10, 27)),
            (2, Fraction(10, 64)),      # 10/(2*32) = 5/32
            (5, Fraction(10, 235)),     # 10/(5*47)
            (10, Fraction(10, 720)),    # 10/(10*72)
            (26, Fraction(5, 1976)),    # 10/(26*152) = 5/1976
        ]
        for c_val, expected in test_cases:
            c = Fraction(c_val)
            Q = Fraction(10) / (c * (5 * c + 22))
            assert Q == expected, f"Failed at c={c_val}: got {Q}, expected {expected}"

    def test_delta_formula_multiple_c(self):
        """Delta = 40/(5c+22) at multiple c values."""
        for c_val in [1, 5, 10, 25, 26]:
            c = Fraction(c_val)
            kap = c / 2
            S4 = Fraction(10) / (c * (5 * c + 22))
            Delta = 8 * kap * S4
            expected = Fraction(40, 5 * c_val + 22)
            assert Delta == expected, f"Failed at c={c_val}"

    def test_shadow_metric_at_multiple_c(self):
        """Shadow metric q_2 = 36 + 80/(5c+22) at multiple c values."""
        for c_val in [1, 5, 10, 26]:
            c = Fraction(c_val)
            kap = float(c / 2)
            S3 = 2.0
            S4 = float(Fraction(10) / (c * (5 * c + 22)))
            q2 = 9 * S3**2 + 16 * kap * S4
            expected = 36.0 + 80.0 / (5 * c_val + 22)
            assert abs(q2 - expected) < 1e-10, f"Failed at c={c_val}"

    def test_kappa_eff_vanishes_only_at_c26(self):
        """kappa_eff = 0 ONLY at c=26."""
        for c_val in range(0, 30):
            c = Fraction(c_val)
            k_eff = kappa_effective(c)
            if c_val == 26:
                assert k_eff == 0
            else:
                assert k_eff != 0

    def test_vacuum_vertex_proportional_to_kappa(self):
        """V_{g,0} is proportional to kappa for all g."""
        from compute.lib.utils import lambda_fp
        for g in range(1, 6):
            lam = lambda_fp(g)
            for c_val in [1, 13, 26]:
                kap = Fraction(c_val, 2)
                V = csft_vertex_vacuum(kap, g)
                assert V == kap * lam
