r"""Tests for CSFT action from bar complex.

Verifies the identification:
    shadow obstruction tower = on-shell CSFT action

Structure:
    Section 1: Faber-Pandharipande coefficients (multi-path, 5 tests)
    Section 2: CSFT vertex structure (5 tests)
    Section 3: On-shell free energy = shadow tower (4 tests)
    Section 4: Generating function verification (3 tests)
    Section 5: Anomaly cancellation (4 tests)
    Section 6: Feynman expansion at low genus (3 tests)
    Section 7: Convergence (2 tests)
    Section 8: Cross-family consistency (3 tests)
    Section 9: Quartic contact (2 tests)
    Section 10: MC equation sectors (3 tests)

Total: 34 tests.

Anti-patterns tested against:
    AP1:  kappa values computed from definitions, not copied.
    AP10: Cross-family consistency checks, not just hardcoded values.
    AP22: hbar convention verified at leading order.
    AP24: Virasoro complementarity sum = 13, NOT zero.
    AP27: Bar propagator weight 1 (not field weight).
    AP29: kappa_eff != delta_kappa.
    AP31: kappa = 0 does NOT imply Theta = 0.
    AP35: Each verification path is genuinely independent.
    AP46: eta(q) = q^{1/24} * prod(1 - q^n).

Ground truth:
    Zwiebach (1993), thm:mc2-bar-intrinsic, Theorem D,
    eq:scalar-free-energy-ahat, thm:frontier-sft-vertices,
    Faber-Pandharipande values from OEIS A027641/A027642,
    thm:shadow-double-convergence.
"""

import math
import pytest
from sympy import Rational, bernoulli, factorial, simplify

from compute.lib.csft_from_bar import (
    # Section 1: FP coefficients
    lambda_fp_local,
    ahat_coefficient,
    ahat_generating_function_value,
    # Section 2: CSFT action
    CSFTAction,
    # Section 3: algebra-specific
    csft_heisenberg,
    csft_virasoro,
    csft_affine_sl2,
    csft_affine_sl3,
    csft_beta_gamma,
    # Section 4: on-shell verification
    verify_onshell_csft_equals_shadow_tower,
    verify_generating_function_two_paths,
    # Section 5: Feynman expansion
    feynman_expansion_genus1,
    feynman_expansion_genus2,
    feynman_expansion_genus3,
    # Section 6: anomaly cancellation
    anomaly_cancellation_bosonic_string,
    koszul_complementarity_virasoro,
    # Section 7: convergence
    convergence_analysis,
    # Section 8: cross-family
    cross_family_kappa_additivity,
    # Section 9: quartic contact
    quartic_contact_virasoro,
    # Section 10: dictionary
    csft_bar_dictionary,
    csft_from_bar_summary,
    # Section 11: MC sectors
    KAPPA_GHOST,
)

PI = math.pi


# ==========================================================================
# Section 1: Faber-Pandharipande Coefficients (multi-path verification)
# ==========================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP values by multiple independent paths."""

    def test_lambda_1_equals_1_over_24(self):
        """lambda_1^FP = 1/24.

        Path 1: from definition (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * 1/6 * 1/2 = 1/24.
        Path 2: from A-hat(ix) - 1 = x^2/24 + ... (leading coefficient).
        Path 3: from int_{M-bar_{1,1}} psi^0 lambda_1 = Euler char of M_{1,1} = 1/24.
        """
        # Path 1: definition
        assert lambda_fp_local(1) == Rational(1, 24)
        # Path 2: A-hat coefficient
        assert ahat_coefficient(1) == Rational(1, 24)

    def test_lambda_2_equals_7_over_5760(self):
        """lambda_2^FP = 7/5760.

        Path 1: (2^3-1)/2^3 * |B_4|/4! = 7/8 * (1/30)/24 = 7/5760.
        Path 2: A-hat coefficient at g=2.
        """
        assert lambda_fp_local(2) == Rational(7, 5760)
        assert ahat_coefficient(2) == Rational(7, 5760)

    def test_lambda_3_equals_31_over_967680(self):
        """lambda_3^FP = 31/967680.

        Verify: (2^5-1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/967680.
        """
        assert lambda_fp_local(3) == Rational(31, 967680)

    def test_genus_ratio_F2_over_F1(self):
        """F_2/F_1 = 7/240, independent of kappa (universal ratio).

        This ratio is a UNIVERSAL invariant of the modular operad: it does
        not depend on the algebra A.  This is the two-loop-to-one-loop ratio.
        """
        ratio = lambda_fp_local(2) / lambda_fp_local(1)
        assert ratio == Rational(7, 240)

    def test_ahat_closed_form_vs_series(self):
        """Verify A-hat(ix) = (x/2)/sin(x/2) matches series at x = 1.

        Two independent paths:
            Path 1: closed form evaluation
            Path 2: partial sum of Taylor coefficients
        """
        x = 1.0
        closed_form = (x / 2) / math.sin(x / 2)
        series = 1.0
        for g in range(1, 30):
            series += float(lambda_fp_local(g)) * x ** (2 * g)
        assert abs(closed_form - series) < 1e-12


# ==========================================================================
# Section 2: CSFT Vertex Structure
# ==========================================================================

class TestCSFTVertexStructure:
    """Test the structure of CSFT vertices V_{g,n}."""

    def test_stability_condition(self):
        """Vertices vanish for unstable surfaces: 2g - 2 + n <= 0."""
        csft = csft_heisenberg(1)
        assert csft.vertex(0, 0) == 0  # genus 0, 0 points (unstable)
        assert csft.vertex(0, 1) == 0  # genus 0, 1 point (unstable)
        assert csft.vertex(0, 2) == 0  # genus 0, 2 points (unstable)

    def test_genus0_vertices_non_scalar(self):
        """Genus-0 vertices are NOT captured by kappa alone.

        V_{0,3}, V_{0,4} depend on the full OPE structure.
        At the scalar level, they return 0.
        """
        csft = csft_virasoro(26)
        # Scalar-level projection of genus-0 vertices is zero
        # (the actual vertex depends on the cubic shadow, etc.)
        assert csft.vertex(0, 3) == 0  # scalar projection
        assert csft.vertex(0, 4) == 0  # scalar projection

    def test_tadpole_V11_equals_kappa_over_24(self):
        """V_{1,1} = kappa/24 for all algebras (genus-1 universality).

        This is Theorem D at genus 1: obs_1 = kappa * lambda_1 unconditionally.
        """
        # Heisenberg (kappa = 1)
        csft_h = csft_heisenberg(1)
        assert csft_h.vertex(1, 1) == Rational(1, 24)

        # Virasoro c=26 (kappa = 13)
        csft_v = csft_virasoro(26)
        assert csft_v.vertex(1, 1) == Rational(13, 24)

        # sl_2 at k=1 (kappa = 9/4)
        csft_s = csft_affine_sl2(1)
        assert csft_s.vertex(1, 1) == Rational(9, 4) * Rational(1, 24)

    def test_genus2_vertex_equals_kappa_times_7_over_5760(self):
        """V_{2,0} = F_2 = kappa * 7/5760 at the scalar level."""
        csft = csft_virasoro(2)
        assert csft.vertex(2, 0) == Rational(1) * Rational(7, 5760)

    def test_heisenberg_is_free_theory(self):
        """Heisenberg: shadow class G, depth 2, free CSFT.

        All vertices beyond kappa * lambda_g are zero at the scalar level.
        The CSFT is quadratic: no cubic or higher interactions.
        """
        csft = csft_heisenberg(1)
        assert csft.shadow_class == "G"
        assert csft.shadow_depth == 2
        assert csft.kappa == 1


# ==========================================================================
# Section 3: On-Shell Free Energy = Shadow Tower
# ==========================================================================

class TestOnShellEquality:
    """Verify that on-shell CSFT free energy equals the shadow genus tower."""

    def test_heisenberg_three_path_match(self):
        """Three-path verification for Heisenberg at all genera up to 10."""
        csft = csft_heisenberg(1)
        result = verify_onshell_csft_equals_shadow_tower(csft, max_genus=10)
        assert result["all_match"], "Not all genera match across three paths"

    def test_virasoro_three_path_match(self):
        """Three-path verification for Virasoro c=2 at all genera up to 10."""
        csft = csft_virasoro(2)
        result = verify_onshell_csft_equals_shadow_tower(csft, max_genus=10)
        assert result["all_match"]

    def test_affine_sl2_three_path_match(self):
        """Three-path verification for sl_2 at k=1."""
        csft = csft_affine_sl2(1)
        result = verify_onshell_csft_equals_shadow_tower(csft, max_genus=10)
        assert result["all_match"]

    def test_beta_gamma_three_path_match(self):
        """Three-path verification for beta-gamma system."""
        csft = csft_beta_gamma()
        result = verify_onshell_csft_equals_shadow_tower(csft, max_genus=10)
        assert result["all_match"]


# ==========================================================================
# Section 4: Generating Function Verification
# ==========================================================================

class TestGeneratingFunction:
    """Verify the A-hat generating function by two independent paths."""

    def test_heisenberg_gf_at_hbar_1(self):
        """F(1) for Heisenberg matches closed form and series."""
        csft = csft_heisenberg(1)
        result = verify_generating_function_two_paths(csft, hbar=1.0)
        assert result["match"], f"Difference: {result['absolute_difference']}"

    def test_virasoro_gf_at_hbar_half(self):
        """F(0.5) for Virasoro c=10 matches closed form and series."""
        csft = csft_virasoro(10)
        result = verify_generating_function_two_paths(csft, hbar=0.5)
        assert result["match"]

    def test_ap22_leading_order_check(self):
        """AP22: verify F_1 matches at leading order.

        With convention sum F_g hbar^{2g}, the leading term at hbar -> 0 is:
            F_1 * hbar^2 = (kappa/24) * hbar^2.

        The A-hat formula: kappa * (A-hat(i*hbar) - 1) starts at hbar^2/24.
        Verify these match.
        """
        csft = csft_heisenberg(1)
        hbar = 0.01  # small
        F_approx = csft.free_energy_generating_function(hbar)
        F_leading = float(csft.kappa) * hbar**2 / 24
        # They should agree to high relative precision
        assert abs(F_approx - F_leading) / abs(F_leading) < 1e-3


# ==========================================================================
# Section 5: Anomaly Cancellation
# ==========================================================================

class TestAnomalyCancellation:
    """Test anomaly cancellation at the critical dimension."""

    def test_bosonic_string_c26_anomaly_free(self):
        """kappa_eff = c/2 - 13 = 0 at c = 26."""
        result = anomaly_cancellation_bosonic_string(26)
        assert result["anomaly_free"]
        assert result["kappa_eff"] == 0

    def test_bosonic_string_c26_all_F_g_vanish(self):
        """F_g = 0 for all g >= 1 at c = 26."""
        result = anomaly_cancellation_bosonic_string(26)
        for g in range(1, 6):
            assert result["genera"][g]["F_g_total"] == 0

    def test_kappa_additivity_across_genera(self):
        """F_g(A+B) = F_g(A) + F_g(B) at all genera (additivity)."""
        result = anomaly_cancellation_bosonic_string(26)
        for g in range(1, 6):
            assert result["genera"][g]["additive"]

    def test_virasoro_complementarity_sum_is_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT zero.

        This tests the specific anti-pattern AP24.
        """
        for c in [0, 1, 2, 10, 13, 20, 26]:
            result = koszul_complementarity_virasoro(c)
            assert result["sum_is_13"], f"Failed at c = {c}: sum = {result['sum']}"


# ==========================================================================
# Section 6: Feynman Expansion at Low Genus
# ==========================================================================

class TestFeynmanExpansion:
    """Verify the Feynman expansion of the CSFT action at low genus."""

    def test_genus1_feynman_match(self):
        """Genus-1: single graph, F_1 = kappa/24."""
        result = feynman_expansion_genus1(1)
        assert result["match"]
        assert result["amplitude"] == Rational(1, 24)

    def test_genus2_feynman_match(self):
        """Genus-2: F_2 = kappa * 7/5760 at scalar level."""
        result = feynman_expansion_genus2(1)
        assert result["match"]
        assert result["ratio_F2_F1"] == Rational(7, 240)

    def test_genus3_feynman_match(self):
        """Genus-3: F_3 = kappa * 31/967680 at scalar level.

        42 stable graphs on M-bar_{3,0}.
        """
        result = feynman_expansion_genus3(1)
        assert result["match"]
        assert result["num_stable_graphs"] == 42


# ==========================================================================
# Section 7: Convergence
# ==========================================================================

class TestConvergence:
    """Test convergence of the shadow genus tower."""

    def test_convergence_radius_is_2pi(self):
        """Convergence radius = 2*pi (first zero of sin(hbar/2))."""
        csft = csft_heisenberg(1)
        result = convergence_analysis(csft, max_genus=30)
        assert abs(result["convergence_radius"] - 2 * PI) < 1e-10

    def test_ratio_limit_is_1_over_4pi_squared(self):
        """F_{g+1}/F_g -> 1/(4*pi^2) as g -> infinity.

        This is the Bernoulli asymptotic: |B_{2g}| ~ 2*(2g)!/(2*pi)^{2g}.
        """
        csft = csft_heisenberg(1)
        result = convergence_analysis(csft, max_genus=30)
        assert result["ratio_convergence"], (
            f"Last ratio = {result['last_ratio']}, "
            f"expected ~{result['ratio_limit']}"
        )


# ==========================================================================
# Section 8: Cross-Family Consistency (AP10 guard)
# ==========================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks to guard against AP10 (hardcoded wrong values)."""

    def test_kappa_additivity(self):
        """kappa is additive under direct sum."""
        checks = cross_family_kappa_additivity()
        assert checks["bosonic_string_c26"]["vanishes"]
        assert checks["sl2_k1_plus_heis"]["match"]

    def test_F_g_additivity_across_genera(self):
        """F_g(A+B) = F_g(A) + F_g(B) for sl_2 + Heisenberg."""
        checks = cross_family_kappa_additivity()
        for g in range(1, 4):
            assert checks[f"F_{g}_additivity"]["match"], f"Additivity fails at genus {g}"

    def test_universal_ratio_family_independent(self):
        """F_2/F_1 = 7/240 for ALL families (universal ratio).

        This ratio depends only on the modular operad, not on the algebra.
        """
        for csft in [csft_heisenberg(1), csft_virasoro(10),
                      csft_affine_sl2(3), csft_beta_gamma()]:
            F1 = csft.free_energy_term(1)
            F2 = csft.free_energy_term(2)
            if F1 != 0:
                ratio = F2 / F1
                assert ratio == Rational(7, 240), (
                    f"Universal ratio failed for {csft.family}: "
                    f"F2/F1 = {ratio}"
                )


# ==========================================================================
# Section 9: Quartic Contact
# ==========================================================================

class TestQuarticContact:
    """Test the quartic contact term from the MC equation."""

    def test_Q_contact_virasoro_formula(self):
        """Q^contact_Vir = 10 / [c * (5c + 22)] for Virasoro.

        At c = 2: Q = 10 / (2 * 32) = 10/64 = 5/32.
        """
        result = quartic_contact_virasoro(2)
        assert result["Q_contact"] == Rational(5, 32)

    def test_Q_contact_matches_csft_quartic_obstruction(self):
        """The quartic contact invariant is the (0,4) MC equation obstruction.

        Verify for several c values.
        """
        for c in [1, 2, 5, 10, 26]:
            result = quartic_contact_virasoro(c)
            c_val = Rational(c)
            expected = Rational(10) / (c_val * (5 * c_val + 22))
            assert result["Q_contact"] == expected


# ==========================================================================
# Section 10: MC Equation Sectors
# ==========================================================================

class TestMCEquationSectors:
    """Test the MC equation projected to specific (g, n) sectors."""

    def test_tadpole_sector_1_1(self):
        """The (1,1) sector: V_{1,1} = kappa/24."""
        csft = csft_virasoro(26)
        sector = csft.mc_equation_sector(1, 1)
        assert sector["V_value"] == Rational(13, 24)
        assert sector["scalar_level"] is True

    def test_quartic_sector_0_4(self):
        """The (0,4) sector: quartic obstruction."""
        csft = csft_virasoro(26)
        sector = csft.mc_equation_sector(0, 4)
        assert sector["scalar_level"] is False
        assert "Q" in sector["shadow_name"]

    def test_vacuum_sector_2_0(self):
        """The (2,0) sector: genus-2 vacuum energy."""
        csft = csft_heisenberg(1)
        sector = csft.mc_equation_sector(2, 0)
        assert sector["V_value"] == Rational(7, 5760)
        assert sector["scalar_level"] is True


# ==========================================================================
# Section 11: Summary and Dictionary (sanity)
# ==========================================================================

class TestSummary:
    """Test the identification dictionary and summary."""

    def test_dictionary_has_all_keys(self):
        """The CSFT-bar dictionary covers all expected identifications."""
        d = csft_bar_dictionary()
        assert "CSFT_vertex_V_{g,n}" in d
        assert "CSFT_master_equation" in d
        assert "on_shell_free_energy" in d
        assert "anomaly_cancellation" in d

    def test_summary_status(self):
        """Summary correctly reports the proved/conjectural status."""
        s = csft_from_bar_summary()
        assert s["level_1_proved"] is True
        assert s["level_2_proved"] is True
        assert s["level_3_status"] == "conjectural"
