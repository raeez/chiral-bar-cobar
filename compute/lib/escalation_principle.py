r"""Escalation principle: adversarial analysis of the genus-g Böcherer-Nyman-Beurling chain.

The escalation principle (rem:bocherer-escalation in arithmetic_shadows.tex) claims:
  At genus g, Böcherer-type formulas connect degree-g Fourier coefficients
  to L(1/2, pi_F) for automorphic representations of GSp(2g), and via the
  symmetric power transfer Sym^{g-1}: GL(2) -> GL(g), this accesses
  L(1/2, Sym^{g-1} f x chi_D).

This module implements an adversarial verification of the escalation chain,
tracking at each genus exactly what is PROVED, what is CONJECTURAL, and
where circular dependencies arise.

KEY FINDINGS:
  1. Genus 2: Böcherer factorization PROVED (Furusawa-Morimoto 2021/DPSS 2020).
     Sym^1 = identity, unconditional. THIS IS THE ONLY FULLY PROVED GENUS.
  2. Genus 3: Böcherer-type formula CONJECTURAL. Sym^2 transfer PROVED
     (Gelbart-Jacquet 1978). The Böcherer formula is the bottleneck.
  3. Genus 4: Böcherer CONJECTURAL. Sym^3 PROVED (Kim-Shahidi 2002).
  4. Genus 5: Böcherer CONJECTURAL. Sym^4 PROVED (Kim 2003).
  5. Genus >= 6: BOTH Böcherer AND Sym^{g-1} CONJECTURAL.
     Sym^r for r >= 5 requires Langlands GL(2)->GL(r+1) functoriality (OPEN).
     Newton-Thorne (2021) proves potential automorphy for Sym^r for all r,
     but over CM fields, not Q — the full automorphy over Q is open for r >= 5.

CIRCULARITY ANALYSIS:
  The escalation principle claims to implement Serre's programme: Ramanujan from
  all-genera symmetric-power non-vanishing. But the Böcherer-type formulas at
  genus g require the L-function L(s, pi_F) for GSp(2g) automorphic forms to
  be well-understood. For Saito-Kurokawa lifts (the only case where Böcherer
  is proved), the lift comes FROM GL(2) eigenforms, so no functoriality is
  needed. For genuine GSp(2g) eigenforms at g >= 3, relating L(1/2, pi_F) to
  L(1/2, Sym^{g-1} f) requires knowing that pi_F is a symmetric power lift,
  which IS the Langlands functoriality the programme aims to prove.

  The circularity is:
    Escalation needs: pi_F on GSp(2g) identified with Sym^{g-1}(pi_f) on GL(g)
    This identification IS: Langlands functoriality GL(2) -> GL(g) -> GSp(2g)
    Which is: exactly what Serre's programme (via the escalation) tries to prove

  At genus 2 there is NO circularity because:
    - The Böcherer formula is proved for ALL Sp(4) eigenforms, not just lifts
    - For SK lifts, the connection to GL(2) L-values is via Waldspurger (proved)
    - Sym^1 = id (trivial)

RESIDUAL GAPS:
  Gap R1: K^(g) gives L-values at the SINGLE POINT s = 1/2, not the full
          L^2(0,1) norm needed for Nyman-Beurling.
  Gap R2: The Serre reduction needs ANALYTIC CONTINUATION of Sym^r L-functions
          for all r, not just central values. Central values alone do not
          determine the Dirichlet series.
  Gap R3: The varprojlim K^(infinity) is a formal construction; its analytic
          properties (completeness in the Nyman-Beurling L^2 norm) are unknown.

References:
  - Böcherer (1986): original conjecture
  - Furusawa-Morimoto (2014/2021): refined Böcherer proved for GSp(4)
  - DPSS (2020): Böcherer for full level
  - Gelbart-Jacquet (1978): Sym^2 automorphy
  - Kim-Shahidi (2002): Sym^3 automorphy
  - Kim (2003): Sym^4 automorphy
  - Newton-Thorne (2021): potential automorphy of Sym^r for all r (over CM fields)
  - Serre (1977): Ramanujan from all symmetric powers
  - Nyman (1950), Beurling (1955): L^2 criterion for RH
  - arithmetic_shadows.tex: rem:bocherer-escalation, rem:genus2-beurling-kernel,
    rem:serre-reduction, thm:bocherer-bridge, thm:leech-chi12-projection
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


# ============================================================================
# 1. STATUS CLASSIFICATION
# ============================================================================

class ClaimStatus(Enum):
    """Epistemic status of a mathematical claim."""
    PROVED = "proved"
    CONDITIONAL = "conditional"
    CONJECTURAL = "conjectural"
    OPEN = "open"
    CIRCULAR = "circular"


@dataclass
class EscalationLink:
    """Status of one link in the escalation chain at a given genus."""
    genus: int
    description: str
    status: ClaimStatus
    dependencies: List[str] = field(default_factory=list)
    reference: str = ""
    notes: str = ""


@dataclass
class GenusStatus:
    """Complete status of the escalation chain at genus g."""
    genus: int
    bocherer_status: ClaimStatus
    bocherer_ref: str
    sym_power_status: ClaimStatus
    sym_power_ref: str
    sym_power_r: int  # r = g - 1
    mc_to_fourier_status: ClaimStatus
    overall_status: ClaimStatus
    circularity_analysis: str
    residual_gaps: List[str]


# ============================================================================
# 2. SYMMETRIC POWER TRANSFER STATUS
# ============================================================================

def symmetric_power_status(r: int) -> Tuple[ClaimStatus, str]:
    """Return the status of Sym^r: GL(2) -> GL(r+1) Langlands functoriality.

    Parameters
    ----------
    r : int
        The symmetric power degree.

    Returns
    -------
    (status, reference) pair.
    """
    if r == 0:
        return (ClaimStatus.PROVED, "trivial (Sym^0 = det)")
    elif r == 1:
        return (ClaimStatus.PROVED, "identity map GL(2) -> GL(2)")
    elif r == 2:
        return (ClaimStatus.PROVED, "Gelbart-Jacquet 1978")
    elif r == 3:
        return (ClaimStatus.PROVED, "Kim-Shahidi 2002")
    elif r == 4:
        return (ClaimStatus.PROVED, "Kim 2003")
    else:
        return (ClaimStatus.OPEN,
                f"Langlands GL(2)->GL({r+1}) open for r={r}; "
                f"Newton-Thorne 2021 gives potential automorphy over CM fields, "
                f"not full automorphy over Q")


def symmetric_power_status_table(r_max: int = 12) -> List[Tuple[int, ClaimStatus, str]]:
    """Status table for Sym^r transfer, r = 0, ..., r_max."""
    return [(r,) + symmetric_power_status(r) for r in range(r_max + 1)]


# ============================================================================
# 3. BÖCHERER-TYPE FORMULA STATUS
# ============================================================================

def bocherer_status(g: int) -> Tuple[ClaimStatus, str]:
    """Return the status of Böcherer-type formulas at genus g.

    Parameters
    ----------
    g : int
        The genus (g >= 1).

    Returns
    -------
    (status, reference) pair.

    Notes
    -----
    - g = 1: Waldspurger formula (proved, 1981) — not Böcherer per se,
      but the genus-1 analogue connecting half-integral weight Fourier
      coefficients to central L-values.
    - g = 2: Refined Böcherer conjecture PROVED by Furusawa-Morimoto (2014/2021)
      and DPSS (2020) for full level.
    - g >= 3: CONJECTURAL. No Böcherer-type formula has been proved for
      Siegel modular forms of degree g >= 3. The problem requires understanding
      the spectral decomposition of the Siegel theta lift, which is open.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    elif g == 1:
        return (ClaimStatus.PROVED,
                "Waldspurger 1981 (genus-1 analogue: "
                "half-integral weight coefficients ~ central L-values)")
    elif g == 2:
        return (ClaimStatus.PROVED,
                "Furusawa-Morimoto 2014/2021, DPSS 2020 (full level)")
    else:
        return (ClaimStatus.CONJECTURAL,
                f"No Böcherer-type formula proved for GSp({2*g}) Siegel "
                f"modular forms at genus {g}. The spectral decomposition "
                f"of the degree-{g} theta lift is not understood.")


# ============================================================================
# 4. MC-TO-FOURIER CHAIN STATUS
# ============================================================================

def mc_to_fourier_status(g: int) -> Tuple[ClaimStatus, str]:
    """Status of the MC equation -> genus-g Fourier coefficient chain.

    Parameters
    ----------
    g : int
        The genus.

    Returns
    -------
    (status, reference) pair.

    Notes
    -----
    The MC equation D^2 = 0 at genus g produces the genus-g amplitude
    as a graph sum. For lattice VOAs, this is the genus-g theta series.
    The MC-to-Fourier chain:
      D^2 = 0 -> genus-g graph sum -> Theta^(g)_Lambda -> Fourier coefficients
    is PROVED at all genera (it's a formal consequence of D^2 = 0, which is
    proved by thm:ambient-d-squared-zero).

    However, INTERPRETING the Fourier coefficients as L-values requires
    the Böcherer formula (genus-dependent, see bocherer_status).
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    return (ClaimStatus.PROVED,
            "D^2 = 0 (thm:ambient-d-squared-zero) -> genus-g graph sum -> "
            "Fourier coefficients. The MC-to-Fourier step is unconditional.")


# ============================================================================
# 5. FULL ESCALATION CHAIN AT GENUS g
# ============================================================================

def escalation_chain(g: int) -> GenusStatus:
    """Compute the full escalation chain status at genus g.

    The chain at genus g is:
      MC (D^2=0) -> Theta^(g) -> Böcherer -> L(1/2, pi_F) -> Sym^{g-1} -> L(1/2, Sym^{g-1} f)

    Each link has its own status. The overall status is the MINIMUM
    (weakest link).

    Parameters
    ----------
    g : int
        The genus (>= 1).

    Returns
    -------
    GenusStatus with complete analysis.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")

    mc_stat, mc_ref = mc_to_fourier_status(g)
    boch_stat, boch_ref = bocherer_status(g)
    r = g - 1  # symmetric power degree
    sym_stat, sym_ref = symmetric_power_status(r)

    # Overall status: weakest link
    status_order = {
        ClaimStatus.PROVED: 4,
        ClaimStatus.CONDITIONAL: 3,
        ClaimStatus.CONJECTURAL: 2,
        ClaimStatus.OPEN: 1,
        ClaimStatus.CIRCULAR: 0,
    }
    statuses = [mc_stat, boch_stat, sym_stat]
    overall = min(statuses, key=lambda s: status_order[s])

    # Circularity analysis
    circularity = _circularity_analysis(g, boch_stat, sym_stat)

    # Residual gaps
    gaps = _residual_gaps(g, boch_stat, sym_stat)

    return GenusStatus(
        genus=g,
        bocherer_status=boch_stat,
        bocherer_ref=boch_ref,
        sym_power_status=sym_stat,
        sym_power_ref=sym_ref,
        sym_power_r=r,
        mc_to_fourier_status=mc_stat,
        overall_status=overall,
        circularity_analysis=circularity,
        residual_gaps=gaps,
    )


def _circularity_analysis(g: int, boch_stat: ClaimStatus,
                          sym_stat: ClaimStatus) -> str:
    """Analyze circularity at genus g."""
    if g == 1:
        return ("No circularity. Waldspurger formula is unconditional. "
                "Sym^0 = trivial.")
    elif g == 2:
        return ("No circularity. Böcherer formula proved unconditionally for "
                "ALL Sp(4) eigenforms (Furusawa-Morimoto/DPSS). For SK lifts, "
                "connection to GL(2) L-values via Waldspurger. Sym^1 = identity.")
    elif g <= 5:
        return (
            f"PARTIAL CIRCULARITY. Böcherer-type formula at genus {g} is "
            f"CONJECTURAL: requires understanding spectral decomposition of "
            f"GSp({2*g}) theta lift. Sym^{g-1} transfer is proved "
            f"(r={g-1} <= 4). However, even with Sym^{g-1} proved, "
            f"identifying a GSp({2*g}) automorphic form pi_F as "
            f"Sym^{g-1}(pi_f) for a GL(2) form pi_f requires the "
            f"functorial LIFT, not just the transfer. The Böcherer formula "
            f"bypasses this for g=2 (SK lifts), but at g >= 3 the lift "
            f"structure is unknown."
        )
    else:
        return (
            f"FULL CIRCULARITY at genus {g}. BOTH links are open: "
            f"(1) Böcherer-type formula for GSp({2*g}) is conjectural. "
            f"(2) Sym^{g-1} automorphy for r={g-1} >= 5 requires "
            f"Langlands GL(2)->GL({g}) functoriality, which is OPEN. "
            f"Newton-Thorne gives potential automorphy over CM fields, "
            f"not over Q. The escalation at genus {g} REQUIRES the "
            f"Langlands functoriality it claims to prove via Serre's "
            f"programme — this is circular."
        )


def _residual_gaps(g: int, boch_stat: ClaimStatus,
                   sym_stat: ClaimStatus) -> List[str]:
    """List residual gaps at genus g."""
    gaps = []

    # Gap R1: single-point vs full L^2 norm (applies at all genera)
    gaps.append(
        f"R1 (genus {g}): The genus-{g} Beurling kernel K^({g}) "
        f"gives L-values at the single point s=1/2, not the full "
        f"L^2(0,1) norm required by Nyman-Beurling."
    )

    # Gap R2: analytic continuation (applies at all genera)
    gaps.append(
        f"R2 (genus {g}): The Serre reduction requires ANALYTIC "
        f"CONTINUATION of Sym^r L-functions for all r, not just "
        f"central values. The MC equation gives algebraic relations "
        f"on Dirichlet coefficients (Newton's identities), but "
        f"algebraic relations do not imply analytic continuation."
    )

    # Gap R3: inverse limit convergence
    if g >= 2:
        gaps.append(
            f"R3 (genus {g}): The all-genera kernel "
            f"K^(infty) = varprojlim K^(g) is a formal construction. "
            f"Its completeness in the Nyman-Beurling L^2 norm is unknown."
        )

    # Böcherer-specific gap at g >= 3
    if boch_stat != ClaimStatus.PROVED:
        gaps.append(
            f"R4 (genus {g}): Böcherer-type formula at genus {g} is "
            f"{boch_stat.value}. No spectral decomposition of the "
            f"degree-{g} Siegel theta lift is known."
        )

    # Sym-specific gap at r >= 5
    if sym_stat != ClaimStatus.PROVED:
        gaps.append(
            f"R5 (genus {g}): Sym^{g-1} automorphy (r={g-1}) is "
            f"{sym_stat.value}. This is Langlands GL(2)->GL({g}) "
            f"functoriality, one of the central open problems in "
            f"the Langlands programme."
        )

    return gaps


# ============================================================================
# 6. FULL ESCALATION TABLE
# ============================================================================

def escalation_table(g_max: int = 10) -> List[GenusStatus]:
    """Compute escalation chain status for genera 1 through g_max."""
    return [escalation_chain(g) for g in range(1, g_max + 1)]


def print_escalation_table(g_max: int = 10) -> str:
    """Pretty-print the escalation status table."""
    table = escalation_table(g_max)
    lines = []
    lines.append("=" * 80)
    lines.append("ESCALATION PRINCIPLE: STATUS AT EACH GENUS")
    lines.append("=" * 80)
    lines.append(f"{'g':>3} | {'Sym^r':>5} | {'MC->Fourier':>12} | "
                 f"{'Böcherer':>14} | {'Sym^{g-1}':>12} | {'Overall':>14}")
    lines.append("-" * 80)
    for gs in table:
        lines.append(
            f"{gs.genus:>3} | "
            f"r={gs.sym_power_r:<3} | "
            f"{gs.mc_to_fourier_status.value:>12} | "
            f"{gs.bocherer_status.value:>14} | "
            f"{gs.sym_power_status.value:>12} | "
            f"{gs.overall_status.value:>14}"
        )
    lines.append("=" * 80)
    lines.append("")
    lines.append("LEGEND:")
    lines.append("  MC->Fourier: D^2=0 -> genus-g graph sum -> Fourier coefficients")
    lines.append("  Böcherer: genus-g Böcherer-type formula (Fourier -> L-values)")
    lines.append("  Sym^{g-1}: symmetric power transfer GL(2)->GL(g)")
    lines.append("  Overall: weakest link in the chain")
    return "\n".join(lines)


# ============================================================================
# 7. NYMAN-BEURLING GAP ANALYSIS
# ============================================================================

@dataclass
class NymanBeurlingGapAnalysis:
    """Analysis of the gap between K^(g) and the Nyman-Beurling kernel."""
    genus: int
    spectral_support_match: bool
    single_point_vs_l2: bool  # True = only single point
    analytic_continuation_needed: bool
    inverse_limit_well_defined: bool
    completeness_in_l2: bool
    summary: str


def nyman_beurling_gap(g: int) -> NymanBeurlingGapAnalysis:
    """Analyze the Nyman-Beurling gap at genus g.

    The Nyman-Beurling criterion: RH iff the characteristic functions
    chi_{(0,theta)} for theta in (0,1) span a dense subspace of L^2(0,1).
    Equivalently: the Gram matrix G_{ij} = <rho_{theta_i}, rho_{theta_j}>
    in the L^2 inner product detects completeness.

    The genus-g Beurling kernel K^(g)(D, D') is the analogue with
    Böcherer coefficients replacing dilated fractional parts.

    Gaps:
      g=1: spectral support mismatch (Re(s)>1 vs critical line)
      g=2: spectral support matches, but single-point (s=1/2) not L^2
      g>=3: both Böcherer and (for g>=6) Sym^r are conjectural
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")

    if g == 1:
        return NymanBeurlingGapAnalysis(
            genus=1,
            spectral_support_match=False,
            single_point_vs_l2=True,
            analytic_continuation_needed=True,
            inverse_limit_well_defined=False,
            completeness_in_l2=False,
            summary=(
                "Genus 1: SPECTRAL SUPPORT MISMATCH. The sewing kernel "
                "zeta(s+t)zeta(s+t+1) lives in Re(s)>1; the Nyman-Beurling "
                "kernel involves zeta(s)zeta(1-s) across the critical line. "
                "The two have disjoint spectral support."
            )
        )
    elif g == 2:
        return NymanBeurlingGapAnalysis(
            genus=2,
            spectral_support_match=True,
            single_point_vs_l2=True,
            analytic_continuation_needed=True,
            inverse_limit_well_defined=True,
            completeness_in_l2=False,
            summary=(
                "Genus 2: SPECTRAL SUPPORT MATCHES (Böcherer proved). "
                "The genus-2 Beurling kernel K^(2) involves L-values at "
                "s=1/2, on the critical line. But K^(2) gives L-values at "
                "a SINGLE POINT, while Nyman-Beurling requires the full "
                "L^2(0,1) norm. The residual gap: single-point access != "
                "L^2 completeness."
            )
        )
    else:
        boch_stat, _ = bocherer_status(g)
        sym_stat, _ = symmetric_power_status(g - 1)
        return NymanBeurlingGapAnalysis(
            genus=g,
            spectral_support_match=(boch_stat == ClaimStatus.PROVED),
            single_point_vs_l2=True,
            analytic_continuation_needed=True,
            inverse_limit_well_defined=False,
            completeness_in_l2=False,
            summary=(
                f"Genus {g}: CONJECTURAL. Böcherer formula is "
                f"{boch_stat.value}; Sym^{g-1} transfer is "
                f"{sym_stat.value}. The kernel K^({g}) is not rigorously "
                f"defined. Even if it were, single-point L-values do not "
                f"yield L^2 completeness."
            )
        )


# ============================================================================
# 8. SERRE REDUCTION CHAIN ANALYSIS
# ============================================================================

@dataclass
class SerreReductionStatus:
    """Status of the Serre reduction chain at each stage."""
    stage: int
    description: str
    status: ClaimStatus
    reference: str
    gap_if_open: str


def serre_reduction_chain() -> List[SerreReductionStatus]:
    """The four-station Serre reduction chain.

    Station 1: MC -> shadow tower at all arities (PROVED)
    Station 2: Shadow tower -> symmetric power Dirichlet coefficients (PROVED)
    Station 3: Symmetric power analytic continuation for all r (OPEN for r >= 5)
    Station 4: Serre: all Sym^r analytic + RH -> Ramanujan (PROVED, classical)

    Returns list of four stations.
    """
    return [
        SerreReductionStatus(
            stage=1,
            description="MC (D^2=0) -> shadow tower at all arities",
            status=ClaimStatus.PROVED,
            reference="thm:mc2-bar-intrinsic, thm:ambient-d-squared-zero",
            gap_if_open="",
        ),
        SerreReductionStatus(
            stage=2,
            description="Shadow tower -> Sym^r Dirichlet coefficients (Newton identities)",
            status=ClaimStatus.PROVED,
            reference="prop:shadow-symmetric-power",
            gap_if_open="",
        ),
        SerreReductionStatus(
            stage=3,
            description="Symmetric power analytic continuation for all r",
            status=ClaimStatus.OPEN,
            reference="Langlands GL(2)->GL(r+1) functoriality",
            gap_if_open=(
                "Known for r <= 4 (Gelbart-Jacquet r=2, Kim-Shahidi r=3, "
                "Kim r=4). OPEN for r >= 5. Newton-Thorne (2021) gives "
                "potential automorphy over CM fields. The best unconditional "
                "bound is the Kim-Sarnak exponent |lambda_p| <= 2p^{7/64}."
            ),
        ),
        SerreReductionStatus(
            stage=4,
            description="Serre: all Sym^r analytic + RH -> Ramanujan",
            status=ClaimStatus.CONDITIONAL,
            reference="Serre 1977",
            gap_if_open="Conditional on Station 3 (Langlands functoriality).",
        ),
    ]


# ============================================================================
# 9. MANUSCRIPT HONESTY AUDIT
# ============================================================================

def manuscript_honesty_check() -> List[Tuple[str, str, str]]:
    """Check the manuscript's claims against the adversarial analysis.

    Returns list of (claim_location, claim_text, assessment) triples.
    """
    checks = []

    # Check 1: rem:bocherer-escalation line 9404
    checks.append((
        "rem:bocherer-escalation (line 9404)",
        '"At genus g, conjectural Böcherer-type formulas..."',
        "HONEST: correctly says 'conjectural' for g >= 3."
    ))

    # Check 2: rem:bocherer-escalation line 9410
    checks.append((
        "rem:bocherer-escalation (line 9410)",
        '"Newton-Thorne, conditional for g >= 6"',
        "PARTIALLY HONEST: correctly notes conditionality for g >= 6. "
        "However, the phrasing is misleading: it suggests Newton-Thorne "
        "PROVES Sym^r for r <= 4 (i.e., g <= 5). In fact, Newton-Thorne "
        "proves POTENTIAL automorphy over CM fields for ALL r. The actual "
        "proofs for r <= 4 are by Gelbart-Jacquet, Kim-Shahidi, Kim — "
        "not Newton-Thorne. The Newton-Thorne reference should be reserved "
        "for the conditional/potential result at r >= 5."
    ))

    # Check 3: rem:genus2-beurling-kernel line 3683-3694
    checks.append((
        "rem:genus2-beurling-kernel (lines 3683-3694)",
        '"The escalation principle fills in the missing spectral data... '
        'The all-genera Beurling kernel would have the same spectral '
        'content as the Nyman-Beurling kernel, completing the reduction."',
        "SCOPE INFLATION (AP7/AP42): the 'would' is doing enormous work. "
        "The all-genera kernel is conjectural at g >= 3 (no Böcherer formula), "
        "circular at g >= 6 (requires Langlands functoriality), and even if "
        "fully constructed would give L-values at SINGLE POINTS s=1/2, not "
        "the L^2(0,1) norm. The phrase 'completing the reduction' is false: "
        "three independent gaps remain (R1: single-point vs L^2, R2: analytic "
        "continuation, R3: inverse limit completeness). The text should say "
        "'would narrow the gap' not 'completing the reduction'."
    ))

    # Check 4: rem:serre-reduction line 4889-4908
    checks.append((
        "rem:serre-reduction (lines 4889-4908)",
        '"The shadow tower at all arities encodes all symmetric power '
        'L-functions."',
        "HONEST: correctly identifies the gap as the 'middle arrow' "
        "(analytic continuation). The chain MC -> Sym^r data -> [gap] -> "
        "L(s, Sym^r f) -> Ramanujan is correctly described with the gap "
        "explicitly flagged."
    ))

    # Check 5: rem:bocherer-escalation line 9412-9414
    checks.append((
        "rem:bocherer-escalation (lines 9412-9414)",
        '"The MC equation at all genera thereby implements Serre\'s '
        'programme: Ramanujan follows from all-genera symmetric-power '
        'non-vanishing."',
        "OVERCLAIM (AP42): 'implements' is too strong for a chain that is "
        "conjectural at g >= 3, circular at g >= 6, and has three "
        "independent residual gaps. The MC equation ENCODES the symmetric "
        "power data (proved) but does not IMPLEMENT Serre's programme "
        "(which requires analytic continuation, not just algebraic relations "
        "on Dirichlet coefficients). Should say 'would implement' or "
        "'provides the algebraic backbone for' Serre's programme."
    ))

    # Check 6: circularity
    checks.append((
        "rem:bocherer-escalation (structural)",
        "Escalation at g >= 6 requires Langlands functoriality",
        "CIRCULAR DEPENDENCY: The escalation principle at genus g >= 6 "
        "requires Sym^{g-1} automorphy, which IS Langlands GL(2)->GL(g) "
        "functoriality. But the escalation is being proposed as a route "
        "TO Ramanujan VIA Serre's programme, which itself reduces Ramanujan "
        "to Langlands functoriality. The escalation at high genus does not "
        "provide independent evidence — it restates the problem. This "
        "circularity is NOT flagged in the manuscript."
    ))

    return checks


# ============================================================================
# 10. QUANTITATIVE ASSESSMENT
# ============================================================================

def proved_fraction(g_max: int = 10) -> Tuple[int, int, float]:
    """Count how many genera have fully proved escalation chains.

    Returns (n_proved, n_total, fraction).
    """
    table = escalation_table(g_max)
    n_proved = sum(1 for gs in table
                   if gs.overall_status == ClaimStatus.PROVED)
    n_total = len(table)
    return n_proved, n_total, n_proved / n_total if n_total > 0 else 0.0


def first_conjectural_genus() -> int:
    """Return the smallest genus at which the escalation chain becomes conjectural."""
    for g in range(1, 100):
        gs = escalation_chain(g)
        if gs.overall_status != ClaimStatus.PROVED:
            return g
    return -1  # pragma: no cover


def first_circular_genus() -> int:
    """Return the smallest genus at which circularity appears.

    This is g = 6 (where both Böcherer and Sym^5 are open).
    At g = 3, 4, 5: Böcherer is conjectural but Sym^r is proved,
    so no circularity in the Langlands direction.
    However, even at g = 3-5, there is a STRUCTURAL circularity:
    the Böcherer formula at g >= 3 implicitly requires understanding
    the GSp(2g) spectral theory, which is entangled with functoriality.
    We return g = 6 as the UNAMBIGUOUS circularity genus.
    """
    return 6


# ============================================================================
# 11. SUMMARY
# ============================================================================

def full_summary() -> str:
    """Generate a complete adversarial summary of the escalation principle."""
    lines = []
    lines.append("=" * 80)
    lines.append("ADVERSARIAL ANALYSIS: ESCALATION PRINCIPLE")
    lines.append("(rem:bocherer-escalation in arithmetic_shadows.tex)")
    lines.append("=" * 80)
    lines.append("")

    lines.append("1. ESCALATION TABLE")
    lines.append(print_escalation_table(10))
    lines.append("")

    lines.append("2. SERRE REDUCTION CHAIN")
    lines.append("-" * 40)
    for st in serre_reduction_chain():
        lines.append(f"  Station {st.stage}: {st.description}")
        lines.append(f"    Status: {st.status.value}")
        if st.gap_if_open:
            lines.append(f"    Gap: {st.gap_if_open}")
    lines.append("")

    lines.append("3. PROVED VS CONJECTURAL")
    n_proved, n_total, frac = proved_fraction(10)
    lines.append(f"  Proved genera: {n_proved}/{n_total} ({frac:.0%})")
    lines.append(f"  First conjectural: genus {first_conjectural_genus()}")
    lines.append(f"  First circular: genus {first_circular_genus()}")
    lines.append("")

    lines.append("4. MANUSCRIPT HONESTY CHECK")
    lines.append("-" * 40)
    for loc, claim, assessment in manuscript_honesty_check():
        lines.append(f"  [{loc}]")
        lines.append(f"    Claim: {claim}")
        lines.append(f"    Assessment: {assessment}")
        lines.append("")

    lines.append("5. RESIDUAL GAPS (genus 2, the best case)")
    gaps = _residual_gaps(2, ClaimStatus.PROVED, ClaimStatus.PROVED)
    for gap in gaps:
        lines.append(f"  - {gap}")
    lines.append("")

    lines.append("6. CONCLUSION")
    lines.append(
        "  The escalation principle is CONJECTURAL at g >= 3 and CIRCULAR "
        "at g >= 6. The manuscript correctly labels the Böcherer formula as "
        "'conjectural' at g >= 3 and notes the Newton-Thorne conditionality "
        "at g >= 6. However, the prose in rem:genus2-beurling-kernel overstates "
        "the import: 'completing the reduction' should be 'narrowing the gap', "
        "and 'implements Serre's programme' should be 'encodes the algebraic "
        "data for Serre's programme'. Three independent gaps remain even in the "
        "fully proved genus-2 case: single-point vs L^2, analytic continuation, "
        "and inverse limit completeness."
    )

    return "\n".join(lines)
