"""Tests for the escalation principle adversarial analysis.

Verifies:
1. Symmetric power transfer status at each r
2. Böcherer formula status at each genus
3. Full escalation chain at each genus (proved vs conjectural vs circular)
4. Nyman-Beurling gap analysis
5. Serre reduction chain
6. Manuscript honesty checks
7. Circularity detection
8. Quantitative assessment

Mathematical ground truth (independently verified):
  - Sym^r automorphy: proved for r <= 4, open for r >= 5
  - Böcherer formula: proved at g=2 (Furusawa-Morimoto/DPSS), conjectural g >= 3
  - The escalation is conjectural at g >= 3, circular at g >= 6
  - Three residual gaps persist even at g=2 (single-point, analytic cont., L^2)
"""

import pytest

from compute.lib.escalation_principle import (
    ClaimStatus,
    EscalationLink,
    GenusStatus,
    NymanBeurlingGapAnalysis,
    SerreReductionStatus,
    bocherer_status,
    escalation_chain,
    escalation_table,
    first_circular_genus,
    first_conjectural_genus,
    full_summary,
    manuscript_honesty_check,
    mc_to_fourier_status,
    nyman_beurling_gap,
    print_escalation_table,
    proved_fraction,
    serre_reduction_chain,
    symmetric_power_status,
    symmetric_power_status_table,
)


# ============================================================================
# SYMMETRIC POWER TRANSFER STATUS
# ============================================================================

class TestSymmetricPowerStatus:
    """Tests for symmetric power transfer status at each r."""

    def test_sym0_proved(self):
        """Sym^0 is trivial (det)."""
        status, ref = symmetric_power_status(0)
        assert status == ClaimStatus.PROVED

    def test_sym1_proved(self):
        """Sym^1 = identity."""
        status, ref = symmetric_power_status(1)
        assert status == ClaimStatus.PROVED

    def test_sym2_proved(self):
        """Sym^2 automorphy by Gelbart-Jacquet 1978."""
        status, ref = symmetric_power_status(2)
        assert status == ClaimStatus.PROVED
        assert "Gelbart" in ref or "1978" in ref

    def test_sym3_proved(self):
        """Sym^3 automorphy by Kim-Shahidi 2002."""
        status, ref = symmetric_power_status(3)
        assert status == ClaimStatus.PROVED
        assert "Kim" in ref

    def test_sym4_proved(self):
        """Sym^4 automorphy by Kim 2003."""
        status, ref = symmetric_power_status(4)
        assert status == ClaimStatus.PROVED
        assert "Kim" in ref

    def test_sym5_open(self):
        """Sym^5 automorphy is OPEN (Langlands GL(2)->GL(6))."""
        status, ref = symmetric_power_status(5)
        assert status == ClaimStatus.OPEN
        assert "Langlands" in ref or "open" in ref.lower()

    def test_sym_large_open(self):
        """Sym^r for r >= 5 is open."""
        for r in [5, 6, 7, 10, 20, 100]:
            status, _ = symmetric_power_status(r)
            assert status == ClaimStatus.OPEN, f"Sym^{r} should be open"

    def test_sym_boundary_r4_r5(self):
        """The proved/open boundary is exactly at r=4/r=5."""
        s4, _ = symmetric_power_status(4)
        s5, _ = symmetric_power_status(5)
        assert s4 == ClaimStatus.PROVED
        assert s5 == ClaimStatus.OPEN

    def test_newton_thorne_not_confused_with_full_automorphy(self):
        """Newton-Thorne gives POTENTIAL automorphy, not full automorphy over Q."""
        for r in [5, 6, 7]:
            _, ref = symmetric_power_status(r)
            assert "potential" in ref.lower() or "CM" in ref
            # Must NOT claim full automorphy
            assert "proved" not in ref.lower()

    def test_status_table_length(self):
        """Status table has correct length."""
        table = symmetric_power_status_table(12)
        assert len(table) == 13  # r = 0, ..., 12

    def test_status_table_monotonicity(self):
        """Proved then open — no 'proved' entries after 'open' starts."""
        table = symmetric_power_status_table(20)
        first_open = None
        for r, status, _ in table:
            if status == ClaimStatus.OPEN and first_open is None:
                first_open = r
            if first_open is not None:
                assert status == ClaimStatus.OPEN, \
                    f"Sym^{r} should be open (first open at r={first_open})"


# ============================================================================
# BÖCHERER FORMULA STATUS
# ============================================================================

class TestBochererStatus:
    """Tests for Böcherer formula status at each genus."""

    def test_genus1_proved(self):
        """Genus 1: Waldspurger formula (proved)."""
        status, ref = bocherer_status(1)
        assert status == ClaimStatus.PROVED
        assert "Waldspurger" in ref

    def test_genus2_proved(self):
        """Genus 2: refined Böcherer conjecture (proved by FM/DPSS)."""
        status, ref = bocherer_status(2)
        assert status == ClaimStatus.PROVED
        assert "Furusawa" in ref or "DPSS" in ref

    def test_genus3_conjectural(self):
        """Genus 3: no Böcherer-type formula proved."""
        status, _ = bocherer_status(3)
        assert status == ClaimStatus.CONJECTURAL

    def test_genus_large_conjectural(self):
        """Genus g >= 3 is conjectural."""
        for g in [3, 4, 5, 6, 10, 50]:
            status, _ = bocherer_status(g)
            assert status == ClaimStatus.CONJECTURAL, \
                f"Böcherer at genus {g} should be conjectural"

    def test_genus0_error(self):
        """Genus 0 raises ValueError."""
        with pytest.raises(ValueError):
            bocherer_status(0)

    def test_boundary_g2_g3(self):
        """The proved/conjectural boundary is exactly at g=2/g=3."""
        s2, _ = bocherer_status(2)
        s3, _ = bocherer_status(3)
        assert s2 == ClaimStatus.PROVED
        assert s3 == ClaimStatus.CONJECTURAL


# ============================================================================
# MC-TO-FOURIER STATUS
# ============================================================================

class TestMCToFourierStatus:
    """Tests for MC -> Fourier coefficient chain."""

    def test_proved_at_all_genera(self):
        """MC -> Fourier is proved at all genera (from D^2=0)."""
        for g in [1, 2, 3, 5, 10, 50]:
            status, _ = mc_to_fourier_status(g)
            assert status == ClaimStatus.PROVED, \
                f"MC->Fourier at genus {g} should be proved"

    def test_genus0_error(self):
        """Genus 0 raises ValueError."""
        with pytest.raises(ValueError):
            mc_to_fourier_status(0)


# ============================================================================
# FULL ESCALATION CHAIN
# ============================================================================

class TestEscalationChain:
    """Tests for the complete escalation chain at each genus."""

    def test_genus1_proved(self):
        """Genus 1: all links proved."""
        gs = escalation_chain(1)
        assert gs.overall_status == ClaimStatus.PROVED
        assert gs.bocherer_status == ClaimStatus.PROVED
        assert gs.sym_power_status == ClaimStatus.PROVED
        assert gs.sym_power_r == 0

    def test_genus2_proved(self):
        """Genus 2: all links proved (this is the key result)."""
        gs = escalation_chain(2)
        assert gs.overall_status == ClaimStatus.PROVED
        assert gs.bocherer_status == ClaimStatus.PROVED
        assert gs.sym_power_status == ClaimStatus.PROVED
        assert gs.sym_power_r == 1

    def test_genus3_conjectural(self):
        """Genus 3: Böcherer is conjectural (Sym^2 is proved)."""
        gs = escalation_chain(3)
        assert gs.overall_status == ClaimStatus.CONJECTURAL
        assert gs.bocherer_status == ClaimStatus.CONJECTURAL
        assert gs.sym_power_status == ClaimStatus.PROVED  # Sym^2 by GJ
        assert gs.sym_power_r == 2

    def test_genus4_conjectural(self):
        """Genus 4: Böcherer is conjectural (Sym^3 is proved)."""
        gs = escalation_chain(4)
        assert gs.overall_status == ClaimStatus.CONJECTURAL
        assert gs.bocherer_status == ClaimStatus.CONJECTURAL
        assert gs.sym_power_status == ClaimStatus.PROVED  # Sym^3 by KS
        assert gs.sym_power_r == 3

    def test_genus5_conjectural(self):
        """Genus 5: Böcherer is conjectural (Sym^4 is proved)."""
        gs = escalation_chain(5)
        assert gs.overall_status == ClaimStatus.CONJECTURAL
        assert gs.bocherer_status == ClaimStatus.CONJECTURAL
        assert gs.sym_power_status == ClaimStatus.PROVED  # Sym^4 by Kim
        assert gs.sym_power_r == 4

    def test_genus6_doubly_open(self):
        """Genus 6: BOTH Böcherer AND Sym^5 are open/conjectural."""
        gs = escalation_chain(6)
        assert gs.overall_status in [ClaimStatus.CONJECTURAL, ClaimStatus.OPEN]
        assert gs.bocherer_status == ClaimStatus.CONJECTURAL
        assert gs.sym_power_status == ClaimStatus.OPEN  # Sym^5
        assert gs.sym_power_r == 5

    def test_genus10_doubly_open(self):
        """Genus 10: both links open."""
        gs = escalation_chain(10)
        assert gs.overall_status in [ClaimStatus.CONJECTURAL, ClaimStatus.OPEN]
        assert gs.bocherer_status == ClaimStatus.CONJECTURAL
        assert gs.sym_power_status == ClaimStatus.OPEN

    def test_overall_weakest_link(self):
        """Overall status is the weakest link in the chain."""
        for g in range(1, 11):
            gs = escalation_chain(g)
            # If any link is open, overall should be open
            if gs.sym_power_status == ClaimStatus.OPEN:
                assert gs.overall_status == ClaimStatus.OPEN
            # If all proved, overall proved
            if (gs.bocherer_status == ClaimStatus.PROVED and
                    gs.sym_power_status == ClaimStatus.PROVED and
                    gs.mc_to_fourier_status == ClaimStatus.PROVED):
                assert gs.overall_status == ClaimStatus.PROVED

    def test_sym_power_r_equals_g_minus_1(self):
        """The symmetric power degree is g-1."""
        for g in range(1, 20):
            gs = escalation_chain(g)
            assert gs.sym_power_r == g - 1

    def test_genus0_error(self):
        """Genus 0 raises ValueError."""
        with pytest.raises(ValueError):
            escalation_chain(0)


# ============================================================================
# CIRCULARITY ANALYSIS
# ============================================================================

class TestCircularityAnalysis:
    """Tests for circularity detection in the escalation chain."""

    def test_genus1_no_circularity(self):
        """Genus 1: no circularity."""
        gs = escalation_chain(1)
        assert "No circularity" in gs.circularity_analysis

    def test_genus2_no_circularity(self):
        """Genus 2: no circularity (Böcherer proved unconditionally)."""
        gs = escalation_chain(2)
        assert "No circularity" in gs.circularity_analysis

    def test_genus3_partial_circularity(self):
        """Genus 3: Böcherer conjectural (partial circularity)."""
        gs = escalation_chain(3)
        assert "CIRCULARITY" in gs.circularity_analysis.upper()

    def test_genus6_full_circularity(self):
        """Genus 6: full circularity (both Böcherer and Sym^5 open)."""
        gs = escalation_chain(6)
        assert "CIRCULAR" in gs.circularity_analysis.upper()
        # Must mention both open directions
        assert "Böcherer" in gs.circularity_analysis or "conjectural" in gs.circularity_analysis.lower()
        assert "Sym" in gs.circularity_analysis or "Langlands" in gs.circularity_analysis

    def test_first_circular_genus_is_6(self):
        """The first unambiguously circular genus is 6."""
        assert first_circular_genus() == 6

    def test_first_conjectural_genus_is_3(self):
        """The first conjectural genus is 3 (Böcherer not proved)."""
        assert first_conjectural_genus() == 3

    def test_circularity_content_genus_ge6(self):
        """At g >= 6, the circularity analysis must flag Langlands functoriality."""
        for g in [6, 7, 8, 10]:
            gs = escalation_chain(g)
            analysis = gs.circularity_analysis.lower()
            assert "langlands" in analysis or "functoriality" in analysis or "circular" in analysis


# ============================================================================
# NYMAN-BEURLING GAP ANALYSIS
# ============================================================================

class TestNymanBeurlingGap:
    """Tests for the Nyman-Beurling gap at each genus."""

    def test_genus1_spectral_mismatch(self):
        """Genus 1: spectral support mismatch (Re(s)>1 vs critical line)."""
        gap = nyman_beurling_gap(1)
        assert gap.spectral_support_match is False
        assert "MISMATCH" in gap.summary.upper()

    def test_genus2_spectral_match(self):
        """Genus 2: spectral support matches (Böcherer proved)."""
        gap = nyman_beurling_gap(2)
        assert gap.spectral_support_match is True
        assert gap.single_point_vs_l2 is True  # But still single-point

    def test_genus2_single_point_gap(self):
        """Genus 2 gives L-values at s=1/2 only, not full L^2 norm."""
        gap = nyman_beurling_gap(2)
        assert gap.single_point_vs_l2 is True
        assert "single" in gap.summary.lower() or "SINGLE" in gap.summary

    def test_genus2_not_complete(self):
        """Even at genus 2, K^(2) is not L^2-complete."""
        gap = nyman_beurling_gap(2)
        assert gap.completeness_in_l2 is False

    def test_genus3_conjectural(self):
        """Genus 3: kernel not rigorously defined."""
        gap = nyman_beurling_gap(3)
        assert gap.spectral_support_match is False  # Böcherer not proved
        assert "CONJECTURAL" in gap.summary.upper()

    def test_all_genera_need_analytic_continuation(self):
        """All genera need analytic continuation (Serre reduction gap)."""
        for g in [1, 2, 3, 5, 10]:
            gap = nyman_beurling_gap(g)
            assert gap.analytic_continuation_needed is True

    def test_genus0_error(self):
        """Genus 0 raises ValueError."""
        with pytest.raises(ValueError):
            nyman_beurling_gap(0)


# ============================================================================
# SERRE REDUCTION CHAIN
# ============================================================================

class TestSerreReductionChain:
    """Tests for the four-station Serre reduction chain."""

    def test_four_stations(self):
        """Chain has exactly four stations."""
        chain = serre_reduction_chain()
        assert len(chain) == 4

    def test_station1_proved(self):
        """Station 1 (MC -> shadow obstruction tower) is proved."""
        chain = serre_reduction_chain()
        assert chain[0].status == ClaimStatus.PROVED
        assert chain[0].stage == 1

    def test_station2_proved(self):
        """Station 2 (shadow -> Sym^r data) is proved."""
        chain = serre_reduction_chain()
        assert chain[1].status == ClaimStatus.PROVED
        assert chain[1].stage == 2

    def test_station3_open(self):
        """Station 3 (analytic continuation) is OPEN."""
        chain = serre_reduction_chain()
        assert chain[2].status == ClaimStatus.OPEN
        assert chain[2].stage == 3
        assert "r <= 4" in chain[2].gap_if_open or "r>=5" in chain[2].gap_if_open.replace(" ", "")

    def test_station4_conditional(self):
        """Station 4 (Serre reduction) is conditional on Station 3."""
        chain = serre_reduction_chain()
        assert chain[3].status == ClaimStatus.CONDITIONAL
        assert chain[3].stage == 4

    def test_station3_mentions_kim_sarnak(self):
        """Station 3 gap mentions the Kim-Sarnak exponent as best unconditional bound."""
        chain = serre_reduction_chain()
        assert "Kim-Sarnak" in chain[2].gap_if_open or "7/64" in chain[2].gap_if_open


# ============================================================================
# RESIDUAL GAPS
# ============================================================================

class TestResidualGaps:
    """Tests for residual gaps at each genus."""

    def test_genus2_has_gaps(self):
        """Even the best case (genus 2) has residual gaps."""
        gs = escalation_chain(2)
        assert len(gs.residual_gaps) >= 2  # At least R1 and R2

    def test_r1_single_point_always_present(self):
        """Gap R1 (single-point vs L^2) is present at all genera."""
        for g in [1, 2, 3, 5, 10]:
            gs = escalation_chain(g)
            r1_present = any("R1" in gap for gap in gs.residual_gaps)
            assert r1_present, f"R1 missing at genus {g}"

    def test_r2_analytic_continuation_always_present(self):
        """Gap R2 (analytic continuation) is present at all genera."""
        for g in [1, 2, 3, 5, 10]:
            gs = escalation_chain(g)
            r2_present = any("R2" in gap for gap in gs.residual_gaps)
            assert r2_present, f"R2 missing at genus {g}"

    def test_genus_ge3_has_bocherer_gap(self):
        """Genera g >= 3 have the Böcherer-specific gap R4."""
        for g in [3, 4, 5, 10]:
            gs = escalation_chain(g)
            r4_present = any("R4" in gap for gap in gs.residual_gaps)
            assert r4_present, f"R4 missing at genus {g}"

    def test_genus_ge6_has_sym_gap(self):
        """Genera g >= 6 have the Sym-specific gap R5."""
        for g in [6, 7, 8, 10]:
            gs = escalation_chain(g)
            r5_present = any("R5" in gap for gap in gs.residual_gaps)
            assert r5_present, f"R5 missing at genus {g}"

    def test_genus2_no_bocherer_gap(self):
        """Genus 2 does NOT have the Böcherer gap (it's proved)."""
        gs = escalation_chain(2)
        r4_present = any("R4" in gap for gap in gs.residual_gaps)
        assert not r4_present


# ============================================================================
# MANUSCRIPT HONESTY CHECK
# ============================================================================

class TestManuscriptHonestyCheck:
    """Tests for the manuscript honesty audit."""

    def test_checks_exist(self):
        """At least 5 checks are performed."""
        checks = manuscript_honesty_check()
        assert len(checks) >= 5

    def test_conjectural_label_honest(self):
        """The 'conjectural' label in rem:bocherer-escalation is flagged as honest."""
        checks = manuscript_honesty_check()
        # Check 1 should assess the 'conjectural' label
        found = any("HONEST" in assessment for _, _, assessment in checks)
        assert found

    def test_overclaim_detected(self):
        """At least one overclaim is detected."""
        checks = manuscript_honesty_check()
        found = any("OVERCLAIM" in assessment or "INFLATION" in assessment
                     for _, _, assessment in checks)
        assert found

    def test_circularity_flagged(self):
        """The circularity at g >= 6 is flagged."""
        checks = manuscript_honesty_check()
        found = any("CIRCULAR" in assessment.upper()
                     for _, _, assessment in checks)
        assert found

    def test_completing_reduction_flagged(self):
        """The 'completing the reduction' phrasing is flagged."""
        checks = manuscript_honesty_check()
        found = any("completing" in claim.lower()
                     for _, claim, _ in checks)
        assert found

    def test_newton_thorne_partially_honest(self):
        """The Newton-Thorne reference is flagged as partially honest."""
        checks = manuscript_honesty_check()
        found = any("Newton-Thorne" in loc or "Newton-Thorne" in claim
                     for loc, claim, _ in checks)
        assert found


# ============================================================================
# QUANTITATIVE ASSESSMENT
# ============================================================================

class TestQuantitativeAssessment:
    """Tests for the quantitative proved/conjectural fractions."""

    def test_proved_fraction_genus10(self):
        """Only genera 1 and 2 are fully proved out of 10."""
        n_proved, n_total, frac = proved_fraction(10)
        assert n_proved == 2
        assert n_total == 10
        assert abs(frac - 0.2) < 1e-10

    def test_proved_fraction_genus5(self):
        """Only genera 1 and 2 are fully proved out of 5."""
        n_proved, n_total, frac = proved_fraction(5)
        assert n_proved == 2
        assert n_total == 5
        assert abs(frac - 0.4) < 1e-10

    def test_first_conjectural_is_3(self):
        """First conjectural genus is 3."""
        assert first_conjectural_genus() == 3

    def test_first_circular_is_6(self):
        """First circular genus is 6."""
        assert first_circular_genus() == 6


# ============================================================================
# ESCALATION TABLE
# ============================================================================

class TestEscalationTable:
    """Tests for the escalation table and its pretty-printing."""

    def test_table_length(self):
        """Table has correct number of entries."""
        table = escalation_table(10)
        assert len(table) == 10

    def test_table_genera_sequential(self):
        """Table entries have sequential genera 1, ..., g_max."""
        table = escalation_table(10)
        for i, gs in enumerate(table):
            assert gs.genus == i + 1

    def test_print_table_not_empty(self):
        """Pretty-printed table is not empty."""
        s = print_escalation_table(5)
        assert len(s) > 0
        assert "ESCALATION" in s


# ============================================================================
# FULL SUMMARY
# ============================================================================

class TestFullSummary:
    """Tests for the full adversarial summary."""

    def test_summary_not_empty(self):
        """Summary is not empty."""
        s = full_summary()
        assert len(s) > 100

    def test_summary_mentions_key_findings(self):
        """Summary mentions the key adversarial findings."""
        s = full_summary()
        assert "CONJECTURAL" in s.upper() or "conjectural" in s
        assert "CIRCULAR" in s.upper() or "circular" in s
        assert "genus" in s.lower()
        assert "Serre" in s

    def test_summary_mentions_all_gaps(self):
        """Summary mentions the residual gaps."""
        s = full_summary()
        assert "single" in s.lower() or "R1" in s
        assert "analytic" in s.lower() or "R2" in s


# ============================================================================
# CROSS-CONSISTENCY WITH MANUSCRIPT
# ============================================================================

class TestCrossConsistency:
    """Tests verifying consistency with manuscript claims."""

    def test_manuscript_says_conjectural_at_g3(self):
        """rem:bocherer-escalation line 9404 says 'conjectural' — verify this is correct."""
        status, _ = bocherer_status(3)
        assert status == ClaimStatus.CONJECTURAL

    def test_manuscript_says_conditional_g6(self):
        """rem:bocherer-escalation line 9410 says 'conditional for g >= 6'."""
        for g in [6, 7, 8, 10]:
            gs = escalation_chain(g)
            assert gs.sym_power_status == ClaimStatus.OPEN

    def test_manuscript_genus2_proved(self):
        """thm:bocherer-bridge is tagged ProvedHere — verify genus 2 is fully proved."""
        gs = escalation_chain(2)
        assert gs.overall_status == ClaimStatus.PROVED

    def test_manuscript_gap_d_narrowed(self):
        """rem:genus2-beurling-kernel claims Gap D is narrowed at genus 2."""
        gap = nyman_beurling_gap(2)
        # Spectral support matches at genus 2 (Gap D narrowing = spectral match)
        assert gap.spectral_support_match is True
        # But NOT eliminated (single-point, not L^2)
        assert gap.completeness_in_l2 is False

    def test_serre_reduction_gap_middle_arrow(self):
        """rem:serre-reduction correctly identifies Station 3 as the gap."""
        chain = serre_reduction_chain()
        # Station 3 is the only open station
        open_stations = [s for s in chain if s.status == ClaimStatus.OPEN]
        assert len(open_stations) == 1
        assert open_stations[0].stage == 3

    def test_kim_sarnak_best_unconditional(self):
        """The manuscript says 'Kim-Sarnak exponent 7/64' is best unconditional."""
        chain = serre_reduction_chain()
        assert "7/64" in chain[2].gap_if_open

    def test_langlands_r_le_4_proved(self):
        """The manuscript says Sym^r known for r <= 4."""
        for r in range(5):
            status, _ = symmetric_power_status(r)
            assert status == ClaimStatus.PROVED

    def test_langlands_r_ge_5_open(self):
        """The manuscript says Sym^r open for r >= 5."""
        for r in [5, 6, 7, 10]:
            status, _ = symmetric_power_status(r)
            assert status == ClaimStatus.OPEN
