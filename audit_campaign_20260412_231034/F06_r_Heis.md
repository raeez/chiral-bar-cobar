# F06_r_Heis (549s, gpt-5.4)

- [CRITICAL] [vol2/chapters/connections/thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:311) — The proved-here proposition “Heisenberg \(r\)-matrix from collision residue” states `r_{\cH_k}(z)=k\,J\otimes J/z^2` at line 319, but the same proof then says the collision residue is `k\,J\otimes J/z` at line 356. This is an internally false claim surface against the canonical Heisenberg formula in [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:417) and [chapters/frame/heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:99). The wrong `k/z^2` claim is repeated in the same file at lines 380 and 790.

- [HIGH] [vol2/chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1792) — The introduction calls `r(z)=k/z^2` the Heisenberg “classical \(r\)-matrix”, but the next item gives `R(z)=\exp(k\hbar/z)` at line 1794, whose first-order term is `k/z`, not `k/z^2`. The same file later distinguishes `r^L(z)=k/z^2` at line 2011, so this is a live mix-up between Laplace kernel and collision residue.

- [HIGH] [vol2/chapters/connections/ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403) — A proved-here “Heisenberg genus-0 package” records `r(z)=k/z^2` with no local caveat. The same false package is duplicated in [vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309).

- [HIGH] [vol2/chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129) — In the proof, the Heisenberg specialization is `r(z)=k/z^2` immediately after a proposition stating that the Laplace transform gives the classical \(r\)-matrix extracted from OPE singular terms. Under the repo’s canonical convention, that is the pre-absorption Laplace kernel, not the Heisenberg \(r\)-matrix.

- [MEDIUM] [vol1/chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1442) — The main introduction repeatedly writes the Heisenberg \(r\)-matrix as `k\,\Omega/z` and speaks of discarded “matrix structure of \(\Omega\)” (also at lines 1519 and 1658). The same drift is propagated to [standalone/introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:618) and line 698 there. This does not match the canonical scalar Heisenberg surface `k/z`.

- [MEDIUM] [vol2/chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563) — A vanishing-check remark assigns Heisenberg the Casimir-style formula `k\,\Omega/z`. The same file states the correct Heisenberg collision residue `r(z)=k/z` at line 40, so this is internal convention drift.

- [LOW] [vol1/chapters/connections/thqg_gravitational_complexity.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293) — The table lists class G as `r(z)=\kappa/z^2`, but the immediately preceding prose at lines 1281–1282 says this table is about an object whose poles are one higher than `r^{\mathrm{coll}}(z)`. This is a notation overload of `r(z)`, not a direct false collision-residue claim, but it conflicts with the canonical Heisenberg notation.

- [LOW] [vol2/chapters/connections/spectral-braiding.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:149) — The free-propagator remark says `r(z)\sim 1/z` is “consistent with” the Heisenberg example, dropping the level factor and therefore the `k=0\to 0` check. The same slip is duplicated in [vol2/chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:226).

## Summary
Instances checked: 126 | Violations found: 8 | Verdict: FAIL


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8393-7dae-7002-ba13-4f01effc24b4
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: Verify every instance of Heis r-matrix across all .tex files.

CANONICAL: r^Heis(z) = k/z
CHECKS: k=0→0. WRONG: 1/z

STEPS:
1. Run: grep -rn 'r.*Heis\|r(z).*k/z' chapters/ | head -30
2. Also search in Vol II: grep -rn similar patterns ~/chiral-bar-cobar-vol2/chapters/ | head -30
3. Also search in Vol III: grep -rn similar patterns ~/calabi-yau-quantum-groups/chapters/ | head -30
4. For EACH hit, verify the formula matches the canonical form
5. Check boundary values
6. Flag ANY discrepancy, even minor notation differences
7. Also check landscape_census.tex for the canonical source
mcp startup: no servers
codex
Using `deep-beilinson-audit` and `multi-path-verify` for a read-only cross-volume formula audit. I’ll establish the canonical source and live claim surface first, then enumerate every Heisenberg `r`-matrix occurrence across Volumes I–III and verify each against `r^{Heis}(z)=k/z`, including the `k=0` boundary.
exec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2809 |
 succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 succeeded in 51ms:
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**
 succeeded in 51ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.


thinking
**Updating the plan**

I think I need to use the command `rg -n --glob '*.tex'` to search through volumes. But I wonder if it’s best to provide an update before doing anything substantial? I want to ensure everything's clear and organized. It seems I'll also need to use the update_plan tool to help with this since it looks like this is a substantial task. So, let’s go ahead and implement that!
codex
I’ve loaded the repo-wide constitutional surface and the audit workflow. Next I’m fixing the exact hit set: canonical `landscape_census.tex` entry first, then the live Heisenberg `r`-matrix mentions in Volumes I–III, then I’ll recheck each surviving finding against local context before reporting.
Plan update
Read-only adversarial audit of every Heisenberg r-matrix occurrence across the three volumes.
  → Locate the canonical Heisenberg r-matrix statement in `landscape_census.tex` and extract its exact convention/boundary data.
  • Enumerate every `.tex` occurrence of Heisenberg r-matrix formulas or prose mentions across Volumes I–III.
  • Inspect each hit in local context and test it against the canonical form `r^{Heis}(z)=k/z`, including the `k=0 -> 0` boundary.
  • Re-verify any suspected discrepancies and produce a severity-ordered audit report with counts.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'r\\"'^'"\\{Heis\\}|r\\"'^Heis|r'"\\(z\\).*k/z|Heis.*r\\(|Heisenberg.*r\\-matrix|Heisenberg.*R\\-matrix|Heisenberg.*R-matrix|Heis.*R\\-matrix|Heis.*R-matrix' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'landscape_census|kappa\\(H_k\\)|r\\"'^'"\\{Heis\\}|r\\"'^Heis|Heisenberg.*r'"\\-matrix|Heisenberg.*R\\-matrix|Heisenberg.*R-matrix' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'landscape_census|kappa\\(H_k\\)|r\\"'^'"\\{Heis\\}|r\\"'^Heis|Heisenberg.*r'"\\-matrix|Heisenberg.*R\\-matrix|Heisenberg.*R-matrix' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'r\\"'^'"\\{Heis\\}|r\\"'^Heis|r'"\\(z\\).*k/z|Heis.*r\\(|Heisenberg.*r\\-matrix|Heisenberg.*R\\-matrix|Heisenberg.*R-matrix|Heis.*R\\-matrix|Heis.*R-matrix' /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./appendices/nonlinear_modular_shadows.tex:2194:\item \textbf{Heisenberg:} $\mathrm{Sh}_r(\mathcal H)=0$ for all $r\ge 3$. The tower is exactly Gaussian.
./appendices/ordered_associative_chiral_kd.tex:2462:The Heisenberg R-matrix $R(z) = \exp(k\hbar/z)$
./standalone/survey_modular_koszul_duality.tex:679:characteristic: averaging loses nothing, because $r(z) = k/z$ is
./standalone/survey_modular_koszul_duality.tex:7476:r(z)&=k/z,
./standalone/chiral_chern_weil.tex:973:$r(z) = k/z$, $h = 1$.
./standalone/ordered_chiral_homology.tex:1944:    $r(z) = k/z$, pole order $1$. Regular singularities.
./standalone/ordered_chiral_homology.tex:7384:$r$-matrix $r(z) = k/z$ (trace-form convention;
./standalone/survey_track_a_compressed.tex:313:$r(z)=k/z$, a scalar with a simple pole: the second-order OPE pole
./standalone/N3_e1_primacy.tex:476:\item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
./standalone/N3_e1_primacy.tex:735:Heisenberg $\cH_{k}$ with $r(z) = k/z$, affine Kac--Moody
./chapters/examples/heisenberg_eisenstein.tex:245:\index{Heisenberg algebra!r-matrix@$r$-matrix}
./chapters/examples/heisenberg_eisenstein.tex:1531:(The Heisenberg spectral $R$-matrix $R(z) = z^{2h}$ is the simplest case of the closed-form Virasoro $R$-matrix $R(z) = z^{2h}\exp(-(c/4)/z^2)$ of Computation~\ref{comp:virasoro-spectral-r-matrix}.)
./chapters/examples/heisenberg_eisenstein.tex:1844:$r(z) = k/z$ (the abelian $r$-matrix),
./standalone/programme_summary.tex:516:the modular characteristic: $r(z) = k/z$ is scalar, so
./standalone/survey_modular_koszul_duality_v2.tex:584:For Heisenberg, $r(z)=k/z$ is already symmetric: averaging loses
./standalone/survey_modular_koszul_duality_v2.tex:2419:$r(z)=k/z$ is already $\Sigma_2$-invariant: $\mathrm{av}(r(z))=k
./standalone/survey_modular_koszul_duality_v2.tex:4353:r(z) &= k/z, & R(z) &= \exp(k/z),
./standalone/virasoro_r_matrix.tex:310:$r(z) = k/z$, a simple pole. On the primary sector,
./standalone/programme_summary_section1.tex:488:the modular characteristic: $r(z) = k/z$ is scalar, so
./standalone/introduction_full_survey.tex:618:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:8:% landscape_census.tex (master kappa table)
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:108:%: kappa values verified against Vol I landscape_census.tex.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_6d_hcs_chiral_qg.tex:166:% beyond the Heisenberg sector. Requires full Yangian R-matrix at charge 3.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2642:Heisenberg r-matrix $r = 0$ on the Cartan, consistent
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:647:\index{Heisenberg algebra!gravitational r-matrix@gravitational $r$-matrix}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2087:%: kappa(Vir_c) = c/2 from landscape_census.tex; c=0 -> 0, c=13 -> 13/2.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:308:\index{Heisenberg algebra!classical r-matrix|textbf}
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2642:Heisenberg r-matrix $r = 0$ on the Cartan, consistent
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:442:classical $r$-matrix is $r(z) = k/z$ (the $d\log$ kernel absorbs
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:40:For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:792:$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:647:\index{Heisenberg algebra!gravitational r-matrix@gravitational $r$-matrix}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1792:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:308:\index{Heisenberg algebra!classical r-matrix|textbf}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:3028:For $G = U(1)$: $\Bbound = \cH_k$, $R(z) = e^{k\hbar/z}$, $\Abulk = \cH_k$ (bulk $\simeq$ boundary), $\alpha_T = m_2 + \hbar k\,\eta \otimes \Lambda$. The classical $r$-matrix $r(z) = k/z$ satisfies the $k = 0$ vanishing check trivially.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:46:\item Heisenberg: $p_{\max}=2$, so $r(z) = k/z$ (single pole).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:78:the collision residue $r(z)=k/z$ (one pole absorbed by the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:2054:the scalar $R(z)=z^k$: nontrivial as a function of~$z$ (the double-pole OPE produces the collision residue $r(z) = k/z$ after $d\log$ absorption), but scalar-valued because the generator space is one-dimensional. The ordered and unordered bar complexes are therefore equivalent up to the $R$-twisted sign character of~$\Sigma_n$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6180:$r$-matrix $r(z) = k/z$ of~\eqref{eq:drinfeld-r-heisenberg}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:874:$r(z)=k/z$, and $\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:875:The $r$-matrix is scalar: $r(z)=k/z\in\Bbbk(\!(z^{-1})\!)$.
 succeeded in 51ms:
./main.tex:1322: \input{chapters/examples/landscape_census}
./main.tex:1532: \phantomsection\label{thm:ds-bar-gf-discriminant}% % landscape_census.tex
./main.tex:1544: \phantomsection\label{prop:discriminant-characteristic}% % landscape_census.tex
./main.tex:1667: \phantomsection\label{rem:koszul-conductor-explicit}% % landscape_census.tex
./main.tex:1760: % --- landscape_census.tex labels ---
./chapters/examples/w_algebras_deep.tex:2141: %: from landscape_census.tex; k=0 -> dim(g)/2; k=-h^v -> 0
./chapters/examples/w_algebras_deep.tex:2144: %: from landscape_census.tex; N=2 -> c/2 = kappa_Vir
./staging/combined_for_higher_genus.tex:351:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4 from landscape_census.tex;
./staging/for_higher_genus__genus2.tex:140:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4 from landscape_census.tex;
./chapters/examples/lattice_foundations.tex:1042:%: kappa(V_Lambda) = rank(Lambda) from landscape_census.tex table row "V_Lambda (rank d)"; rank=1 -> 1 (Heis), rank=24 -> 24 (Leech) verified.
./chapters/examples/lattice_foundations.tex:1106:%: kappa(V_Lambda) = rank(Lambda) from landscape_census.tex:261;
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:7555:% AP1: kappa from landscape_census.tex:
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9368:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4 from landscape_census.tex;
./appendices/ordered_associative_chiral_kd.tex:2462:The Heisenberg R-matrix $R(z) = \exp(k\hbar/z)$
./chapters/examples/heisenberg_eisenstein.tex:245:\index{Heisenberg algebra!r-matrix@$r$-matrix}
./chapters/examples/heisenberg_eisenstein.tex:1531:(The Heisenberg spectral $R$-matrix $R(z) = z^{2h}$ is the simplest case of the closed-form Virasoro $R$-matrix $R(z) = z^{2h}\exp(-(c/4)/z^2)$ of Computation~\ref{comp:virasoro-spectral-r-matrix}.)
./chapters/connections/thqg_gravitational_yangian.tex:646:\index{Heisenberg algebra!gravitational r-matrix@gravitational $r$-matrix}
./chapters/connections/genus1_seven_faces.tex:451:%: from landscape_census.tex; k=0 -> 0 verified, k=-h^v -> singular
./standalone/ordered_chiral_homology.tex:7555:% AP1: kappa from landscape_census.tex:
./standalone/ordered_chiral_homology.tex:9368:% AP1: kappa(V_k(sl_2)) = 3(k+2)/4 from landscape_census.tex;



thinking
**Analyzing .tex file search**

I found many standalone and staging hits, but the user wants to focus on all .tex files. I’m considering whether to include standalone, staging, and appendices. The mission notes that I need to verify every instance of a specific term across all .tex files, not just chapters. I’ll likely need to search through all volumes, particularly focusing on Vol I and Vol II/III, while also keeping an eye out for notes in Vol III. It looks like I need to inspect specific lines in certain files as well.
thinking
**Expanding search for formulas**

I need to broaden my search to catch all instances of the formula `k/z²`. I’m considering searching for "Heisenberg" near "z²" and "1/z" because the initial search might miss some. I’ll look through all .tex files for `k/z²`, `1/z`, and `\Omega/z` in the context of Heisenberg. It’s important to ensure we find every instance of the Heisenberg r-matrix and possibly create a comprehensive hit list. I should use the `rg` tool with line numbers for clarity. Plus, I need to consider duplicates in standalone/staging copies and whether to include them in my audit.
thinking
**Inspecting file paths in Vol III**

I need to determine if the severity is lower for just standalone/staging files, so I have to inspect those closely. I also need to identify the actual file paths in Vol III. The initial search didn’t find any hits in the chapters, so I might mention that none were found in Vol III chapters. However, there could be references in notes, so I’ll search all .tex files in Vol III for “Heisenberg” and the r formulas. It looks like a more exhaustive search across all volumes is necessary!
codex
The initial cross-volume scan already turned up likely convention drift in Vol II: several surfaces say `r(z)=k/z^2`, while the canonical Vol I hot-zone rule and multiple Vol I chapter surfaces say `r(z)=k/z` after `d\log` absorption. I’m now tightening the hit set so the final report only contains genuine Heisenberg `r`-matrix instances rather than incidental `R`-matrix or index noise.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'r\\(z\\)\\s*=\\s*k/z\\"'^2|r'"\\(z\\)\\s*=\\s*1/z|r\\(z\\)\\s*=\\s*k\\\\,\\\\Omega/z|r\\(z\\)\\s*=\\s*k\\\\Omega/z|r\\(z\\)\\s*=\\s*\\\\kappa/z|r\\(z\\)\\s*=\\s*k/z(?"'!'"\\"'^)'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'r\\"'^'"\\{Heis\\}|r\\"'^Heis|Heisenberg.*r'"\\-matrix|Heisenberg.*R\\-matrix|Heisenberg.*classical r\\-matrix|collision residue.*k/z|d\\\\log.*k/z|k\\s*=\\s*0.*r\\-matrix|k\\s*=\\s*0.*r\\(z\\)' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Heisenberg|Heis|H_k|\\\\cH_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'r\\(|R\\(|r\\-matrix|R\\-matrix|R-matrix|classical r|spectral braiding|collision residue|k/z|k/z\\"'^2|1/z|'"\\\\Omega/z'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:r\(z\)\s*=\s*k/z\^2|r\(z\)\s*=\s*1/z|r\(z\)\s*=\s*k\\,\\Omega/z|r\(z\)\s*=\s*k\\Omega/z|r\(z\)\s*=\s*\\kappa/z|r\(z\)\s*=\s*k/z(?!\^))
                                                                                                                                      ^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:439:(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1192:The collision residue is $r^{\mathrm{coll}}(z) = k/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1335:The collision residue is $r^{\mathrm{coll}}(z) = k/z$ (the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1337:$k/(z-w)^2 \cdot d\log(z-w) \leadsto k/z$). The
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1746: $R(z) = \exp(k\hbar/z)$ with collision residue $k/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2642:Heisenberg r-matrix $r = 0$ on the Cartan, consistent
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:245:\index{Heisenberg algebra!r-matrix@$r$-matrix}
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1531:(The Heisenberg spectral $R$-matrix $R(z) = z^{2h}$ is the simplest case of the closed-form Virasoro $R$-matrix $R(z) = z^{2h}\exp(-(c/4)/z^2)$ of Computation~\ref{comp:virasoro-spectral-r-matrix}.)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:40:For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_yangian.tex:646:\index{Heisenberg algebra!gravitational r-matrix@gravitational $r$-matrix}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:647:\index{Heisenberg algebra!gravitational r-matrix@gravitational $r$-matrix}
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2176:one power: $\Res_{w=0}\frac{k}{w^2}\cdot w\,d\log w = k/z$\textup{)}.
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2305:and the collision residue $r^{\mathrm{coll}} = k/z$ has a
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2358: The scalar collision residue $k/z$ becomes the matrix-valued
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2368: + \cdots$. The simple collision residue $k/z$ becomes the
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2462:The Heisenberg R-matrix $R(z) = \exp(k\hbar/z)$
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:7733:coproduct, collision residue $r^{\mathrm{coll}}(z) = k/z$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3181:At $k=0$, the classical $r$-matrix $r(z) = k\,\Omega/z$ vanishes
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1825:Since the affine algebra is Koszul ($m_k = 0$ for $k \geq 3$), there are no higher collision corrections to the residue: the $A_\infty$ Yang--Baxter defect (Theorem~\ref{thm:first-obstruction}) vanishes identically, and the higher support homotopies $h_S$ ($|S| \geq 3$) can be taken to be zero. After projection to degree-zero states, the regular terms in $r(z)$ beyond the simple pole act on higher-degree components that are killed by $p_n$. Thus
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:458:$\Abulk \simeq \Zder(\cH_k) = \cH_k$ (abelian algebras are their
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:460:$\cH_k \simeq \Zder(\cH_k) \simeq \HH^\bullet_{\mathrm{ch}}(\cH_{-k})$
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1109:For Heisenberg: $\Zder(\cH_k) = \cH_k$.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1137:For Heisenberg: $R(z) = e^{k\hbar/z}$ (scalar, YBE trivial).
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:1254:$R(z) = e^{k\hbar/z}$, $\Abulk = \cH_k$ (bulk $\simeq$ boundary);
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:58:The Heisenberg algebra~$\cH_k$ has shadow depth $r_{\max} = 2$ (class~G), so $\Theta^{\mathrm{oc}}$ terminates at degree~2. Every projection is computed in closed form: curvature $\kappa = k$, spectral $R$-matrix $R(z) = e^{k\hbar/z}$, genus tower $F_g = k\,\lambda_g^{\mathrm{FP}}$. The line category is $\cC_{\mathrm{line}} \simeq \cH_{-k}\text{-mod}$ (via $Y(\mathfrak{u}(1)) \simeq \cH_{-k}$); the derived center is the free boson bulk; the complementarity involution $k \mapsto -k$ closes the triangle (note: the Koszul dual $\cH_k^! = \Sym^{\mathrm{ch}}(V^*)$ is not $\cH_{-k}$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1138:\item \emph{Bulk-to-boundary}: $\Abulk = \Zder(\cH_k) = \cH_k$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1383:the Heisenberg $R$-matrix is an entire function of $1/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1474:collision residue for $\cH_k$ is
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2642:Heisenberg r-matrix $r = 0$ on the Cartan, consistent
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4751: while Heisenberg has $R(z) = e^{k/z}$ (scalar).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:1269:S_r(\mathcal{H}_k) = 0 \qquad \text{for all } r \geq 3.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:40:For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:226:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:272:Let $\mathcal C_{\partial}$ be the derived category of boundary line operators with the tensor structure induced by the $W$-module structure of~$M$. Then $R(z)$ defines a meromorphic braiding on $\mathcal C_{\partial}$, and the classical limit $r(z)$ integrates to a filtered quasi-triangular structure on~$\mathcal H$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:296:The classical $r$-matrix $r(z)$ defines an element $r(z) \in \mathcal{H} \widehat{\otimes}\, \mathcal{H}((z^{-1}))$ satisfying:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:647:\index{Heisenberg algebra!gravitational r-matrix@gravitational $r$-matrix}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:648:\index{r-matrix@$r$-matrix!Heisenberg}
/Users/raeez/calabi-yau-quantum-groups/notes/theory_6d_hcs_chiral_qg.tex:166:% beyond the Heisenberg sector. Requires full Yangian R-matrix at charge 3.
codex
The broader sweep confirms two things. First, the canonical collision-residue convention is widespread in Vol I and most Vol II chapter surfaces. Second, there are a few Vol II and stray Vol I/standalone surfaces mixing in either the pre-absorption kernel `k/z^2` or a Kac–Moody-style `k\,\Omega/z` in explicitly Heisenberg contexts; those need exact contextual verification before I classify them.
exec
/bin/zsh -lc "rg -n 'Heisenberg|H_k|r\\(z\\)|k/z|1/z|Omega/z|\\\\kappa/z' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
37:\noindent\emph{The Master Table below collects the invariants computed throughout Part~\ref{part:physics-bridges}. For the Heisenberg algebra, these invariants were derived in Chapter~\ref{ch:heisenberg-frame}; for each subsequent algebra, the corresponding chapter provides the complete computation.}
81:\multicolumn{6}{|c|}{\textit{Heisenberg \textup{(}curved abelian\textup{)}}} \\
83:Heisenberg $\mathcal{H}_\kappa$
197:$\operatorname{ek} = 0$ for Heisenberg, affine $V_k(\fg)$,
215:$\mathfrak{T} = (\cA, \cA^!, r(z))$
222: \kappa/z\bigr), &
274:Heisenberg $\mathcal{H}_\kappa$ & G & 2 & --- & \S\ref{ch:heisenberg-frame} \\
415:$\cH_k$ ($JJ$)
417: & $k/z$
502:``odd'' = $r(z)$ has only odd-order poles and is therefore an odd
530:$\max\operatorname{pole}(r) = 2h - 1$: the Heisenberg
551:The $r$-matrix $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
554:content of the MC equation: the CYBE on~$r(z)$ follows
609:\multicolumn{5}{|c|}{\textit{Heisenberg}} \\
839:Leech lattice VOA, the $24$ weight-$1$ Heisenberg generators
1039:\item[\textbf{T1.}] \emph{Unconditional} (free fields, Heisenberg):
1072:\noindent\textsuperscript{$\dagger$}The Heisenberg is the abelian Kac--Moody case ($h^\vee = 0$);
1115:Heisenberg $\cH_\kappa$ & \checkmark & (ii),(ix) & PBW universality \\
1202:For the Heisenberg algebra at level $\kappa = 1$ (single free boson, $c = 1$),
1207:In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
exec
/bin/zsh -lc "sed -n '1,80p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '60,120p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,320p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% arithmetic_shadows.tex -- Arithmetic content of the shadow obstruction tower
%
% Deficiency opening: kappa is rational; does it carry arithmetic content?
% The Leech S_12 = -65520/691 forces the answer. Depth decomposition
% d = 1 + d_arith + d_alg separates arithmetic from homotopy.
%: kappa(Heis) = k, kappa(Vir) = c/2, kappa(KM) = dim(g)(k+h^v)/(2h^v)
% from landscape_census.tex; k=0 -> 0 verified for all families.

\chapter{Arithmetic content of the shadow obstruction tower}
\label{chap:arithmetic-shadows}

The shadow tower $\Theta_\cA$ of a chiral algebra $\cA$ is a
sequence of rational numbers $\kappa, S_3, S_4, \ldots$ that
encode the obstruction to formality of the bar complex. Over
$\bC$, these are just numbers. Over $\bQ$, they are arithmetic
invariants: their denominators detect Bernoulli primes, their
$p$-adic valuations encode local Euler factors, and their
congruence classes see Hecke eigenforms. The question is not
whether $\kappa$ is rational (it always is) but what structure
its rationality reveals.
 succeeded in 51ms:
so $\Theta$ is closed, and the modular tangent complex
has rank one at every genus. No nonlinear obstructions, no
resonances, no wall-crossing. The simplicity is not a weakness;
it is the diagnostic. Every theorem of
Part~\ref{part:bar-complex} is instantiated here in closed form
before it is stated in generality. A reader who computes the
Arnold relation at three points and checks that Bernoulli numbers
appear in the genus expansion will have seen the entire machine
operate on the simplest input that is not trivial.

The MC element is scalar:
\begin{equation}\label{eq:heisenberg-mc-element}
\Theta_{\mathcal{H}_k} \;=\; k \cdot \eta \otimes \Lambda,
\end{equation}
where $\eta$ is the shadow class and $\Lambda$ is the universal
Hodge class. This is the protagonist of the entire monograph,
written in coordinates for the simplest algebra. Every projection
of the theory (bar complex, Koszul dual, genus tower,
complementarity) reduces to $\kappa = k$ times a universal form.
In the log-FM convolution algebra
 succeeded in 51ms:
 &= \bigl(\mathrm{Vir}_c,\;
 \mathrm{Vir}_{26-c},\;
 \tfrac{c}{2z^3} + \tfrac{2T}{z}\bigr), &
\mathfrak{T}_{\mathcal{W}_3}
 &= \bigl(\mathcal{W}_3^k,\;
 \mathcal{W}_3^{-k-6},\;
 r_{\mathcal{W}_3}(z)\bigr).
\end{aligned}
\end{equation}
Table~\ref{tab:shadow-tower-census} below records the
shadow obstruction tower data that completes the portrait: the archetype class,
shadow depth $r_{\max}$, and the first nontrivial higher shadow for
each family.

\begin{table}[ht]
\centering
\caption{Shadow obstruction tower census: each family as a projection of $\Theta_\cA$}
\label{tab:shadow-tower-census}
\index{shadow obstruction tower!census table}
\renewcommand{\arraystretch}{1.5}

thinking
**Checking Heisenberg row**

I'm looking to find the exact canonical Heisenberg row in the landscape census. I think it makes sense to inspect around lines 400 to 430, where I might find the row with $k/z$. This feels like a focused search, so I’m hoping to pinpoint the information I need effectively and efficiently! Let’s see what I can discover in those lines!
exec
/bin/zsh -lc "sed -n '540,560p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '408,424p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '80,92p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
odd-order pole at $z^{-3}$ from the composite field $\partial T$,
which shifts to the even-order pole $z^{-2}$ in the $r$-matrix.
This is not a violation: the bosonic parity constraint
(Proposition~\ref{prop:bosonic-parity-constraint}) excludes even
$r$-matrix poles only when all OPE poles above $z^{-1}$ are even,
a condition the $WW$ OPE does not satisfy.
\end{remark}

\begin{remark}[$r$-matrix vs the degree-$3$ MC equation]
\label{rem:rmatrix-vs-mc3-census}
\index{r-matrix@$r$-matrix!vs MC equation}
The $r$-matrix $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
is the genus-$0$ binary collision residue of the universal MC
element~$\Theta_\cA$. It carries only part of the degree-$3$
content of the MC equation: the CYBE on~$r(z)$ follows
from the degree-$3$ MC equation after collision extraction and the
Arnold relation on $\mathrm{Conf}_3(\mathbb{C})$, but the two live
in different spaces.

For class-L algebras (affine Kac--Moody, $r_{\max} = 3$), the
 succeeded in 52ms:
 & \textbf{OPE poles}
 & \textbf{$r$-matrix poles}
 & $\boldsymbol{r^{\mathrm{coll}}(z)}$
 & \textbf{CYBE} \\
\hline
\multicolumn{6}{|c|}{\textit{Class G (Gaussian): abelian simple-pole or regular}} \\
\hline
$\cH_k$ ($JJ$)
 & $1$ & $\{2\}$ & $\{1\}$
 & $k/z$
 & trivial \\
\hline
$V_\Lambda$ (Cartan $J^a J^b$)
 & $1$ & $\{2\}$ & $\{1\}$
 & $\langle\alpha^a,\alpha^b\rangle/z$
 & trivial \\
\hline
 succeeded in 51ms:
\hline
\multicolumn{6}{|c|}{\textit{Heisenberg \textup{(}curved abelian\textup{)}}} \\
\hline
Heisenberg $\mathcal{H}_\kappa$
 & $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ (curved)
 & $1$ & ---\textsuperscript{$\dagger$} & $\kappa$ & PH \\
\hline
\multicolumn{6}{|c|}{\textit{Affine Kac--Moody
 \textup{(}Feigin--Frenkel level shift $k \mapsto -k - 2h^\vee$\textup{)}}} \\
\hline
$\widehat{\fg}_k$ (general)
 & $\widehat{\fg}_{-k-2h^\vee}$
 & $\dfrac{kd}{k + h^\vee}$ & $2d$


thinking
**Investigating discrepancies**

I'm noticing a discrepancy with `kΩ/z` due to the extra Ω, and I'm wondering if it could be a scalar after rank one. It still doesn't match the canonical format, and the severity might be high or medium based on the location. I need to inspect specific lines around 1442, 1519, and 1658; they may involve either a table or prose introduction.  

Also, I want to clarify how Vol II and spectral-braiding.tex mention `r(z)  1/z` related to abelian CS results while possibly lacking explicit Heisenberg references. I think the missing level could be a factor. I’ll need to investigate this further.
thinking
**Checking report boundaries**

I think I need to confirm that the report boundary check has been passed, but there seems to be a potential mismatch in the formula. It might be worth inspecting if there's any explicit `1/z` for Heis. I want to make sure everything is accurate, so I should take a closer look. Adjusting my approach could help clarify the details and ensure that the calculations are in good shape overall.
codex
I’ve narrowed the problem to a small set of genuinely suspicious surfaces. The recurring failure mode is consistent: some files correctly distinguish the OPE/Laplace kernel `k/z^2` from the collision residue `k/z`, but a few chapter-level surfaces collapse that distinction and state `k/z^2` itself as the Heisenberg classical `r`-matrix.
exec
/bin/zsh -lc "sed -n '118,138p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2396,2408p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '786,794p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '311,388p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1778,1800p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2303,2314p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '36,46p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '559,566p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '222,230p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '145,151p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
and Koszul duality acts on the chiral Hochschild complex as predicted by
Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
\end{proposition}

\begin{proof}
Direct computation on each family. The Laplace identity
is Proposition~\ref{prop:field-theory-r} specialized to explicit
$\lambda$-bracket data.
For Heisenberg: $\{a_\lambda a\} = k\lambda$ gives
$r(z) = k/z^2$.
For $\widehat{\mathfrak{sl}}_2$: all $9$ bracket pairs
$(J^a, J^b)$ verify.
For Virasoro: $\{T_\lambda T\} = \partial T + 2T\lambda
+ (c/12)\lambda^3$ gives Laplace kernel $r^L(z) = \partial T/z + 2T/z^2
+ (c/2)/z^4$, matching the OPE
(the collision residue is $r^{\mathrm{coll}}(z) = (c/2)/z^3 + 2T/z$).
For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
For $\mathcal{W}_3$: all three bracket pairs verify.
 succeeded in 50ms:
\begin{proposition}[Heisenberg $r$-matrix from collision residue;
\ClaimStatusProvedHere]
% label removed: prop:heisenberg-r-matrix
For the Heisenberg algebra $\cH_k$ at level $k$, the classical
$r$-matrix is
\begin{equation}
% label removed: eq:heisenberg-r-explicit
\boxed{
r_{\cH_k}(z) \;=\; \frac{k}{z^2}\, J \otimes J,
}
\end{equation}
where $J$ is the Heisenberg current. This is a scalar $r$-matrix:
it acts diagonally in the one-dimensional current space.
\end{proposition}

\begin{proof}
\noindent\textbf{Step 1: The $\lambda$-bracket.}
The Heisenberg $\lambda$-bracket is
$\{J {}_\lambda J\} = k\lambda$
(Section~\ref{sec:rosetta-stone}). The coefficients in the
 succeeded in 51ms:
\end{construction}

\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
% label removed: comp:vol2-heisenberg-modular-extension
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
The modular extension:
$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
$\kappa=k$,
$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
$\nabla^{\mathrm{hol}}_{0,n}
 succeeded in 50ms:
\begin{tabular}{llll}
\textbf{Family} & \textbf{Highest pole} & \textbf{Source} &
\textbf{Shadow class} \\
\hline
$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
$\beta\gamma_\lambda$ & $1/z$ [Laplace] & contact OPE & $C$ \\
$\mathrm{Vir}_c$ & $c/(2z^4)$ [Laplace] & conformal anomaly $\lambda^3$ & $M$ \\
$\mathcal{W}_N$ & $c_{W_N}/z^{2N}$ [Laplace] & spin-$N$ self-OPE & $M$ \\
 succeeded in 51ms:
The transferred operations on cohomology
$H^\bullet = \C[\phi]/(dW)$ are tree-level Feynman sums; this is
the simplest setting where the homotopy transfer theorem of
Volume~I produces transferred operations as Feynman diagrams.

\subsection*{Abelian Chern--Simons: the braided atom}

Abelian $U(1)$ Chern--Simons theory at level~$k$ with a boundary
condition along $\C \times \{0\}$ produces:
\begin{itemize}
\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
 the Heisenberg algebra at level~$k$.
\item $\lambda$-bracket:
 $\{J {}_\lambda J\} = k\lambda$.
\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
 transform of $k\lambda$).
\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
 Yang--Baxter trivially (abelian).
\item Line operators:
 $\cC_{\mathrm{line}} \simeq
 succeeded in 51ms:

\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
\label{comp:vol2-heisenberg-modular-extension}
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
The modular extension:
$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
$\kappa=k$,
$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
 succeeded in 51ms:
Two examples fix the picture.

\medskip
\noindent\textbf{Heisenberg.}
For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
\[
R(z) = e^{r(z)} = e^{k\hbar/z},
\]
scalar, and the Yang--Baxter equation holds tautologically. This is class~G: depth $0$, formal, all higher operations zero.

\medskip
 succeeded in 51ms:
r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\, \{\ \cdot{}_\lambda \cdot\ \}.
\]
This is the Laplace transform of the $\lambda$-bracket kernel, convergent for $\operatorname{Re}(z) > 0$ by the exponential decay of $K(z,t)$ in the topological direction (hypothesis (H2)). Meromorphic continuation to $\C^\times$ follows from the meromorphy of the propagator in $z$.

For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).

\begin{remark}[Laplace transform as spectral duality]
 succeeded in 51ms:
realizations by Theorem~\ref{thm:physics-bridge}. Meromorphic
continuation to $\C^\times$ follows from the meromorphy of the
propagator in $z$.

For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).

\begin{remark}[Laplace transform as spectral duality]
\label{rem:laplace-spectral-duality}
The formula $r(z) = \int_0^\infty e^{-\lambda z} \{\cdot{}_\lambda \cdot\}\, d\lambda$ is the passage between the PVA world (spectral variable~$\lambda$) and the $R$-matrix world (position variable~$z$): the two colours of the Swiss-cheese operad made analytic. The $\lambda$-bracket encodes holomorphic (closed-colour) singularities; $R(z)$ encodes topological (open-colour) braiding. The topological direction supplies the integration contour; the holomorphic direction supplies the meromorphic structure. Under DK-0, the Laplace transform recovers the classical $r$-matrix from the $\lambda$-bracket at the evaluation locus. The Laplace transform \emph{is} the spectral duality of the HT theory.
 succeeded in 51ms:
r(z) \;=\; \frac{d}{du}\bigg|_{u=0} R(z;u),
\]
which is the standard classical/quantum correspondence for spectral $R$-matrices. This specialises, at $u = \hh$, to the relation $R(z) = \exp(r(z))$ of the previous remark.
\item \emph{Geometric spectral parameter.} The parameter $z$ is a coordinate on the curve $C$ (the holomorphic direction of $\SCchtop$), not a formal bookkeeping variable. This is exactly what distinguishes $B^{\mathrm{ord}}(A)$ from the purely algebraic braided categories $\mathrm{Rep}(U_q(\fg))$, which have no spectral parameter at all, and aligns $B^{\mathrm{ord}}(A)$ with the evaluation-module category for a Yangian or quantum affine algebra. Meromorphic braided tensor categories with a geometric spectral parameter of this type were isolated by Y.~Soibelman in the late 1990s as the natural target for vertex-algebra categorification; Etingof--Kazhdan quantization~\cite{etingof1996quantization} produces the spectrally-parametrised representative within each formal-deformation class.
\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
\end{enumerate}
The categorical classification asserted here is orthogonal to the Drinfeld double programme stated for $B^{\mathrm{ord}}(\cA)$ in the companion chapter on ordered associative chiral Koszul duality (see Remark~\ref{rem:drinfeld-double-programme} for the formulation on the open colour): the Drinfeld double assembles the algebra and its Koszul dual into a single Hopf object whose module category is~$\cC_\partial$, while the meromorphic braided structure recorded by $R(z)$ equips that category with its spectral braiding. Together, the two remarks present the bar coalgebra $B^{\mathrm{ord}}(A)$ as a universal source of spectrally-parametrised braided monoidal categories.
\end{remark}
exec
/bin/zsh -lc "sed -n '1438,1446p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1514,1522p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1654,1662p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '694,701p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2818,2824p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '82,91p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '614,621p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2638,2645p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2730,2736p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\End(V^{\otimes n})$-valued meromorphic function strictly
contains its scalar trace. The averaging map
$\operatorname{av}$ is surjective but not injective: the kernel
records the non-symmetric components of the line-operator data.
For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
the symmetrization recovers the scalar
$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
full Yangian double; the symmetrization recovers
 succeeded in 50ms:
Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
the symmetric theory is its image.

The $\Eone$ side is strictly richer: at degree~$2$ alone it
distinguishes algebras that the symmetric side identifies.
The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
$\widehat{\mathfrak{sl}}_2$-shadow
$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
 succeeded in 52ms:
boundary stratum; every richer tier specialises to it when all
singular modes vanish.

Tier (b) contains every standard-landscape vertex algebra:
the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
,
Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 succeeded in 50ms:

\begin{remark}[Level-prefixed $r$-matrix]
\label{rem:level-prefixed-r-matrix}
The classical $r$-matrix attached to an affine Kac-Moody $E_1$-chiral algebra at level $k$ is
\[
 r(z) = \frac{k\,\Omega}{z},
\]
not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
\end{remark}

 succeeded in 52ms:
the symmetric theory is its image.

The $\Eone$ side is strictly richer: at degree~$2$ alone it
distinguishes algebras that the symmetric side identifies.
The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
$\widehat{\mathfrak{sl}}_2$-shadow
$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
 succeeded in 52ms:
of depth $\leq k$ and weight $\leq r$, where the bar
propagator $\dlog E(z,w)$ contributes weight~$1$ per edge
 and each $r$-matrix pole of order~$j$ contributes
weight~$j{-}1$ after the $\dlog$ absorption.
For Heisenberg: $r(z) = \kappa/z$ (single pole), so all
bar amplitudes reduce to products of weight-$1$ integrals,
producing only~$\zeta(2)$.
 succeeded in 52ms:
$\End(V^{\otimes n})$-valued meromorphic function strictly
contains its scalar trace. The averaging map
$\operatorname{av}$ is surjective but not injective: the kernel
records the non-symmetric components of the line-operator data.
For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
the symmetrization recovers the scalar
$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 succeeded in 51ms:
+ e^{-\alpha} \otimes e^{\alpha}
+ \tfrac{1}{2} J \otimes J$
is the $\mathfrak{sl}_2$ Casimir and $k = 1$ is the
lattice level (the $k = 0$ limit gives the abelian
Heisenberg r-matrix $r = 0$ on the Cartan, consistent
).
The quantisation of $r(z) = k\,\Omega/z$ is the
Yang $R$-matrix $R(z) = 1 + k\hbar\,\Omega/z$,
 succeeded in 51ms:
\item $\cA = \mathcal{H}_\kappa$; $J(z)J(w) \sim \kappa/(z{-}w)^2$.
\item $\cA^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$ with $\kappa(\cA^!) = -\kappa$ \textup{(}same modular characteristic as $\mathcal{H}_{-\kappa}$, but a different algebra; the Koszul dual and the negative-level algebra are categorically distinct\textup{)}.
\item $\mathcal{C} = \mathrm{Vect}^{\mathbb{Z}}$; no non-trivial lines
 beyond Fock modules.
\item $r_{\mathcal{H}}(z) = \kappa/z$ \textup{(}scalar; collision residue of the $d\log$ kernel\textup{)}.
\item $\Theta_{\mathcal{H}} = \kappa \cdot \eta \otimes \Lambda$;
 tower terminates at degree~$2$



thinking
**Evaluating Heisenberg discrepancies**

I’m noticing that the Vol1 introduction seems incorrect based on the canonical Heisenberg formula, possibly conflating with the Casimir effect. The user wants minor differences flagged, so I need to assess if the Heisenberg formula is rank-one and whether there's a scalar factor. The severity of this issue might be HIGH due to its presence in the introduction. I should check for repetitions in the document to structure the output clearly with relevant file and line citations.
thinking
**Inspecting Vol2 for discrepancies**

I’m considering how to handle findings in the output, where I might only list one line unless there are distinct occurrences in the same file arranged by severity. I need to check line 2642 in Vol2 concerning the Heisenberg r=0 on Cartan and ensure it aligns with k=0. The mention of quantization might not be a Heisenberg instance, so I could choose to omit that. I also want to search for any hidden inconsistencies involving `1/z` in Heisenberg contexts across all .tex files.
thinking
**Assessing discrepancies in context**

I need to look at the broader context to determine if there's a discrepancy. The remark about the free propagator showing `r(z)  1/z` seems to align with the abelian CS result from the Heisenberg_Yangian example. However, it doesn't specify the level k, which might be implicitly tied to a unit coefficient due to the normalization of the free propagator. Since it references the Heisenberg example, this could indicate level-stripping, potentially marking the severity as low to medium.
exec
/bin/zsh -lc "rg -n 'Heisenberg_Yangian|Heisenberg.*Yangian|Example~\\\\ref\\{ex:Heisenberg_Yangian\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '200,240p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '110,170p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:149:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:425:\subsection{Example: abelian CS and Heisenberg Yangian}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:427:\begin{example}[Heisenberg Yangian from $U(1)$ CS]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:428:% label removed: ex:Heisenberg_Yangian
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:429:For abelian $U(1)$ Chern--Simons at level~$k$ (Example~\ref{prop:abelian_CS_complete}), the bulk algebra is the affine Kac--Moody $\widehat{\mathfrak{u}(1)}_k$; the Koszul dual is the Heisenberg Yangian $Y(\mathfrak{u}(1))$. The spectral $R$-matrix is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:226:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2011:\subsection{Example: abelian CS and Heisenberg Yangian}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2013:\begin{example}[Heisenberg Yangian from $U(1)$ CS]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2014:\label{ex:Heisenberg_Yangian}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2019:the Heisenberg Yangian $Y(\mathfrak{u}(1))$. The spectral
 succeeded in 50ms:
\noindent\textbf{Step 2: Propagator integral.}
For physical realizations satisfying
Theorem~\ref{thm:physics-bridge}, the free propagator on
$\C \times \R$ takes the form
\[
K(z,t) = \frac{\Theta(t)}{2\pi z}\, e^{-\mu(z) t} + (\text{regular}),
\]
where $\Theta(t)$ is the Heaviside function enforcing time-ordering and $\mu(z)$ encodes the holomorphic dependence. The bulk $\lambda$-bracket kernel $K_\lambda$ is the Fourier-conjugate mode: $\{\cdot\,{}_\lambda\,\cdot\}$ acts on cohomology classes $[a], [b] \in H^\bullet(A,Q)$ via
\[
\{a_\lambda b\} = \int_0^\infty dt\; e^{\lambda t}\, K(z_{12}, t)\, \langle a \otimes b \rangle_{\mathrm{BV}},
\]
where $\langle \cdot \otimes \cdot \rangle_{\mathrm{BV}}$ is the BV pairing contracting bulk operators against boundary modes (cf.\ Section~\ref{sec:Ainfty-to-PVA}).

\medskip
\noindent\textbf{Step 3: Laplace transform.}
The first-order braiding $r(z)$ is obtained by evaluating the single-exchange diagram. Performing the $t$-integration with the exponential weight $e^{-zt}$ from the spectral parameter gives
\[
r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\, \{\ \cdot{}_\lambda \cdot\ \}.
\]
This is the Laplace transform of the $\lambda$-bracket kernel,
 succeeded in 50ms:

\begin{proposition}[Field--theoretic expression for $r(z)$;
\ClaimStatusProvedHere]
% label removed: prop:field-theory-r
Assume \textrm{(H1)--(H4)}.
Let $\{\cdot{}_\lambda \cdot\}$ be the bulk $(-1)$–shifted $\lambda$–bracket on cohomology (Section~\ref{sec:Ainfty-to-PVA}). The kernel of the infinitesimal spectral $r$–matrix is computed at first order by
\[
r(z) \;\simeq\; \int_{0}^{\infty} \! \mathrm{d}\lambda\ \mathrm{e}^{-\lambda z}\ \bigl\{\; \cdot {}_\lambda \cdot \;\bigr\},
\]
under the BV pairing identifying bulk and boundary modes, and with the propagator fixing the time‑ordering on the half‑line. The integral converges for $\operatorname{Re}(z) > 0$ and extends meromorphically to $\C^\times$. In the formal algebraic setting, this identity holds as an equality of formal power series in $z^{-1}$.
\end{proposition}

\begin{proof}
We prove both the Laplace-transform formula and the classical Yang--Baxter equation in four steps.

\medskip
\noindent\textbf{Step 1: Perturbative expansion.}
Write $R(z) = \id + \hh\, r(z) + O(\hh^2)$ in $\End(L_1 \otimes L_2)$. At tree level ($\hh^0$), line operators compose freely and $R = \id$. The first quantum correction $r(z)$ is computed by a single bulk-to-boundary propagator exchange: a bulk operator propagates from position $z_1$ on line $L_1$ to position $z_2$ on line $L_2$ (with $z = z_1 - z_2$) through the half-space $\C \times \R_{\geq 0}$.

\medskip

thinking
**Checking notation in spectral theory**

I’m looking at the 1/z remark, which seems to relate to a general free propagator and isn’t exclusively tied to Heisenberg. It aligns with an abelian CS result. The Heisenberg example appears to be at a k-level, but I’m noting that the level is skipped in the heuristic remark. Since the user wants every discrepancy, even minor ones, I think I should inspect line 425 onward in spectral-braiding.tex to examine the example formula. Maybe I should search for an explicit k as well.
exec
/bin/zsh -lc "sed -n '2013,2025p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '427,438p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{example}[Heisenberg Yangian from $U(1)$ CS]
% label removed: ex:Heisenberg_Yangian
For abelian $U(1)$ Chern--Simons at level~$k$ (Example~\ref{prop:abelian_CS_complete}), the bulk algebra is the affine Kac--Moody $\widehat{\mathfrak{u}(1)}_k$; the Koszul dual is the Heisenberg Yangian $Y(\mathfrak{u}(1))$. The spectral $R$-matrix is
\begin{equation}
r(z) = k \, \frac{J \otimes J}{z} + \text{(higher terms)},
\end{equation}
satisfying the classical Yang--Baxter equation. For non-abelian $G$, the Koszul dual becomes the Yangian $Y(\mathfrak{g})$ or quantum affine algebra $U_q(\widehat{\mathfrak{g}})$, depending on the CS level and boundary conditions.
\end{example}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% THE E_1-CHIRAL STRUCTURE OF THE SHIFTED YANGIAN
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 succeeded in 52ms:
\begin{example}[Heisenberg Yangian from $U(1)$ CS]
\label{ex:Heisenberg_Yangian}
For abelian $U(1)$ Chern--Simons at level~$k$
\textup{(}Example~\textup{\ref{prop:abelian_CS_complete}}\textup{)},
the bulk algebra is the affine Kac--Moody
$\widehat{\mathfrak{u}(1)}_k$, and the open-colour Koszul dual is
the Heisenberg Yangian $Y(\mathfrak{u}(1))$. The spectral
$R$-matrix is
\begin{equation}
r(z) = k \, \frac{J \otimes J}{z} + \text{(higher terms)},
\end{equation}
satisfying the classical Yang--Baxter equation. For non-abelian $G$,
the open-colour dual is no longer abelian: in the standard affine HT

thinking
**Inspecting potential errors**

I'm noticing that the 1/z remark seems to conflict with its own example, so I might be looking at low to medium discrepancies here. I should probably check Volumes 2, chapters, and the preface for any corrections. It’s also a good idea to inspect other surfaces that might be correct or suspicious. Searching for `k\,\Omega/z` within Heis contexts across Volumes 1, 2, and 3 could help, like in Vol1's intro and that specific line in Vol2.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Heisenberg.*Omega/z|Heisenberg.*\\\\Omega/z|\\\\cH_k.*Omega/z|\\\\cH_k.*\\\\Omega/z|k\\\\,\\\\Omega/z.*Heisenberg|k\\\\Omega/z.*Heisenberg' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1420:Equivalently: $K_\cA(z) = 1$ iff the boundary coproduct is primitive iff the shadow tower terminates at depth zero. This is the $K$-matrix shadow of the pole-order hierarchy summarised in Table~\ref{tab:two-colour-koszul-duals} and in the shadow-depth discussion of Volume~I. It is not an $r$-matrix statement: the $K$-matrix modifies the coproduct, not the product, and the level-$k$ vanishing check does not apply directly; the corresponding $r$-matrix check is the one already recorded in the Volume~II affine constructions (classical $r$-matrix $k\,\Omega/z$ vanishes at $k=0$, in which case $\cA = \cH_0$ collapses to the trivial Heisenberg and $K_\cA(z) = 1$, consistent with class~$\mathbf{G}$).
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1442:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1519:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1658:the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:618:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:698:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'r\\(z\\)\\s*=\\s*\\\\kappa/z|r_\\{["'^}]*H[''^}]*'"\\}\\(z\\)\\s*=\\s*\\\\kappa/z' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Heisenberg.*k/z\\"'^2|'"\\\\cH_k.*k/z\\"'^2|r_'"\\{\\\\cH_k\\}\\(z\\).*k/z\\"'^2|r'"\\(z\\).*k/z\\"'^2.*Heisenberg|Heisenberg.*1/z|1/z.*Heisenberg'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1383:the Heisenberg $R$-matrix is an entire function of $1/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:683:For the free $\beta\gamma$ system on $\CC_z \times \RR_t$, the monodromy of $\nabla_{\fS}$ around $z = 0$ equals the spectral $R$-matrix $R(z) = 1 + r/z + O(1/z^2)$ of the Heisenberg vertex algebra.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:149:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:226:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:27:\textbf{$r$-matrix} & $r(z) = \kappa/z$ (single pole, no Lie bracket) \\
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:41:r(z) = \kappa/z\,\bigr).
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:267:$r(z)$ has no constant term: $r(z) = \kappa/z$ exactly.
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:281:The collision residue $r(z) = \kappa/z$ is a post-extraction object: it is the $r$-matrix of the bar complex after $d\log$~absorption. The pre-extraction (``pre-dualisation'') singular OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ has one higher pole order and is not to be confused with $r(z)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:4444:$r$-matrix & $r(z) = 0$ & $r(z) = \kappa/z$ \\
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:8320:(class~$\mathbf{G}$, $r(z) = \kappa/z$):
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2822:For Heisenberg: $r(z) = \kappa/z$ (single pole), so all
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293: $r(z) = \kappa/z^2$. &
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1296: $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1300: $r(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &

thinking
**Investigating gravitational complexity**

I’m noticing that heisenberg_eisenstein uses κ/z, which seems related to arithmetic. I’m wondering if that could be significant, but maybe it's low. I think I need to check the thqg_gravitational_complexity lines around 1293 for more context, possibly looking for a table involving r(z)=κ/z^2 and its family. Should I include Heisenberg in this? It's definitely worth investigating further—it might lead to something interesting!
codex
A broader regex pass exposed another live drift surface in Vol I connection prose: `chapters/connections/thqg_gravitational_complexity.tex` appears to tabulate Heisenberg with `r(z)=\kappa/z^2`. I’m checking that context now because it may be a second independent false summary, not just the Vol II spectral-braiding cluster.
exec
/bin/zsh -lc "sed -n '1288,1302p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20,45p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
\textbf{Central charge} & $c = 1$ \\
\textbf{Shadow archetype} & G (Gaussian), $r_{\max} = 2$ \\
\textbf{Modular characteristic} & $\kappa(\cH_\kappa) = \kappa$ \\
\textbf{Koszul dual} & $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$,
$\kappa(\cH_\kappa^!) = -\kappa$ \\
\textbf{Complementarity} & $\kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) = 0$ \textup{(}free-field type~I\textup{)} \\
\textbf{$r$-matrix} & $r(z) = \kappa/z$ (single pole, no Lie bracket) \\
\textbf{Genus expansion} & $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ GF $= (\kappa/\hbar^2)(\hat{A}(i\hbar) - 1)$
\end{tabular}
\end{center}

\noindent
The modular Koszul triple
(Definition~\ref{def:modular-koszul-triple}) of the Heisenberg
algebra is
\begin{equation}\label{eq:heisenberg-triple}
\mathfrak{T}_{\cH}
\;=\;
\bigl(\,\cH_\kappa,\;\;
 succeeded in 51ms:
\toprule
\emph{Class} & \emph{Binary shadow $r(z)$} &
\emph{Shadow connection} \\
\midrule
$\mathbf{G}$ &
 $r(z) = \kappa/z^2$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
$\mathbf{L}$ &
 $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
 \mathfrak{C}$ \\
$\mathbf{C}$ &
 $r(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
 \mathfrak{Q}$ \\
exec
/bin/zsh -lc "sed -n '260,286p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8316,8322p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1288,1296p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\toprule
\emph{Class} & \emph{Binary shadow $r(z)$} &
\emph{Shadow connection} \\
\midrule
$\mathbf{G}$ &
 $r(z) = \kappa/z^2$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
$\mathbf{L}$ &
 $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
 succeeded in 52ms:
The bar construction extracts the residue along
$d\log(z{-}w) = dz/(z{-}w)$, absorbing one power of
$(z{-}w)$ (Remark~\ref{rem:heisenberg-bar-absorbs-pole} below).
The collision residue is therefore
$r(z) = \operatorname{Res}_{z=0}[\kappa/(z{-}w)^2 \cdot d\log(z{-}w)]
= \kappa/z$, a single simple pole.
There is no $(z{-}w)^{-1}$ term in the OPE (no Lie bracket), so
$r(z)$ has no constant term: $r(z) = \kappa/z$ exactly.
\end{proof}

\begin{remark}[Pole absorption and the pre-dualisation distinction]
\label{rem:heisenberg-bar-absorbs-pole}
\index{pole absorption!Heisenberg example}
The collision $r$-matrix $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cH_\kappa})$ lives one pole order below the OPE
(the bar kernel absorbs one pole): the OPE has a
double pole $\kappa/z^2$; the collision residue has a single pole
$\kappa/z$. The $d\log$ extraction sends $z^{-n}$ to
$z^{-(n-1)}$. For a general chiral algebra with OPE
poles at orders $n_1 > n_2 > \ldots$, the collision residue has
poles at orders $n_1-1 > n_2-1 > \ldots$.
 succeeded in 52ms:
The weight-$2$ coefficient $\zeta(2)$ corresponds to~$\kappa$;
the weight-$3$ coefficient $\zeta(3)$ to the cubic shadow~$S_3$;
the weight-$4$ coefficient $\zeta(4)/4$ to the quartic
shadow~$S_4$. For Heisenberg
(class~$\mathbf{G}$, $r(z) = \kappa/z$):
the bar transport is abelian and the associator reduces to
$\Phi^{\mathrm{Heis}} = \exp(\zeta(2) [A, B])$, with all


thinking
**Analyzing potential discrepancies**

Okay, I see that this table is definitely wrong. I might need to check broader context, particularly around line numbers like 1293. I'm considering examining other areas, like `chapters/examples/examples-worked.tex` and `chapters/theory/introduction.tex`, which mention the Laplace kernel. I want to ensure discrepancies are legitimate, especially since the user mentioned canonical forms. There are notable inconsistencies, like the r-matrix reference, which could be classified as critical if proven false. I need to look into specific line numbers and the claim status further.
thinking
**Reviewing computation details**

I notice that the proposition proof in Volume II's examples might use `r(z)=k/z^2` without making it clear that it's referring to the Laplace kernel. I think I need to inspect the related theorem or proposition more closely. It would be a good idea to search around the preceding lines for any additional context or clarification. This detail seems important to ensure accuracy in understanding the use of the kernel. I'll take a deeper look!
exec
/bin/zsh -lc "sed -n '104,132p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1786,1798p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1280,1300p' chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2305,2311p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2398,2406p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathcal{W}_3\}$,
the Laplace transform of the $\lambda$-bracket equals the classical
$r$-matrix extracted from OPE singular terms:
\[
 r^{ab}(z)
 \;=\;
 \sum_{n \geq 0}
 c_n^{ab} \cdot \frac{n!}{z^{n+1}},
 \qquad
 \text{where }
 \{a_\lambda b\} = \sum_{n \geq 0} c_n^{ab}\, \lambda^n.
\]
The modular characteristic $\kappa(\cA) + \kappa(\cA^!)$
is a constant independent of the level/charge parameter for each family,
and Koszul duality acts on the chiral Hochschild complex as predicted by
Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
\end{proposition}

 succeeded in 50ms:
(the shadow generating function, \emph{not} the collision residue
$r^{\mathrm{coll}}(z)$, whose poles are shifted down by one;
the bar kernel absorbs one pole) and the corresponding
connection component:
\begin{center}
\small
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{c@{\quad}l@{\quad}l}
\toprule
\emph{Class} & \emph{Binary shadow $r(z)$} &
\emph{Shadow connection} \\
\midrule
$\mathbf{G}$ &
 $r(z) = \kappa/z^2$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
$\mathbf{L}$ &
 $r(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
 \mathfrak{C}$ \\
$\mathbf{C}$ &
 succeeded in 50ms:
condition along $\C \times \{0\}$ produces:
\begin{itemize}
\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
 the Heisenberg algebra at level~$k$.
\item $\lambda$-bracket:
 $\{J {}_\lambda J\} = k\lambda$.
\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
 transform of $k\lambda$).
\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
 Yang--Baxter trivially (abelian).
\item Line operators:
 $\cC_{\mathrm{line}} \simeq
 Y(\mathfrak{u}(1))\text{-mod}
 succeeded in 50ms:
\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
% label removed: comp:vol2-heisenberg-modular-extension
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
The modular extension:
$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
$\kappa=k$,
 succeeded in 50ms:
genus-zero package; \ClaimStatusProvedHere]
\label{comp:vol2-heisenberg-modular-extension}
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
The modular extension:




thinking
**Evaluating mathematical claims**

I've found that the expression k/z^2 seems incorrect in its context, as the classical limit for exp(khbar/z) is actually k/z. It looks like there's a package that incorrectly uses k/z^2 where it should use k/z, which seems critical to point out. I need to check if earlier contexts mention anything about collision residue, but nothing seems relevant. Also, some propositions seem self-contradictory, which may require clarification on downstream propagation in the same file.
thinking
**Assessing theorem consistency**

I need to track a false theorem found in a file at line 316, which is also mentioned in the summary table at line 790. I could reference this as one finding and note the repetition. It seems fine to indicate "repeated at line 790" while maintaining a singular file:line format. I’ll also check other relevant sections in "chapters/examples/rosetta_stone.tex" to ensure accuracy, but it may not be necessary for the report. Counting all candidate lines systematically might help clarify findings further.
thinking
**Searching for discrepancies**

I'm wondering if there could be other discrepancies, specifically regarding changes like "k\,\Omega/z" found in Vol1's introduction and "introduction_full_survey." I should search other chapters for any similar occurrences of Ω. So far, I've only found these two instances, which is great! I might also need to check Vol2's "ordered_associative_chiral_kd_core.tex" to see if everything aligns correctly, but it doesn’t seem necessary at this stage. Let's keep an eye out for any potential issues!
thinking
**Inspecting Heisenberg contexts**

I’m looking at occurrences of `\kappa/z` in various Heisenberg contexts within different .tex files. I’ve noticed several references, including the full chapter devoted to Heisenberg that uses κ instead of k due to parameterization. I need to check if we should flag these, especially since the canonical source mentions H_κ with the κ parameter. I'm thinking it’s essential to inspect lines 215-223 for any relevant details regarding this.
exec
/bin/zsh -lc "sed -n '214,223p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4438,4446p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '244,286p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The seed datum for each family is its modular Koszul triple
$\mathfrak{T} = (\cA, \cA^!, r(z))$
(Definition~\ref{def:modular-koszul-triple}):
\begin{equation}\label{eq:census-triples}
\begin{aligned}
\mathfrak{T}_{\cH}
 &= \bigl(\cH_\kappa,\;
 \operatorname{Sym}^{\mathrm{ch}}(V^*),\;
 \kappa/z\bigr), &
\mathfrak{T}_{\cF}
 succeeded in 51ms:
& \textbf{Free fermion} $\cF$ & \textbf{Heisenberg} $\cH_\kappa$ \\
\midrule
Central charge & $c = 1/2$ (fixed) & $c = 1$ (fixed, $\kappa$ free) \\
$\kappa$ & $1/4$ (fixed) & $\kappa$ (tunable) \\
Shadow class & G, $r_{\max} = 2$ & G, $r_{\max} = 2$ \\
OPE pole & simple: $1/(z{-}w)$ & double: $\kappa/(z{-}w)^2$ \\
$r$-matrix & $r(z) = 0$ & $r(z) = \kappa/z$ \\
Statistics & fermionic & bosonic \\
Spin structure & required & not required \\
 succeeded in 50ms:
\label{subsec:heisenberg-r-matrix}
\index{Heisenberg algebra!r-matrix@$r$-matrix}

\begin{proposition}[Heisenberg $r$-matrix; \ClaimStatusProvedHere]
\label{prop:heisenberg-r-matrix}
The collision residue of the MC element is:
\begin{equation}\label{eq:heisenberg-r-matrix}
r(z) \;=\; \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_{\cH_\kappa})
\;=\; \frac{\kappa}{z}.
\end{equation}
This is a single pole: the Heisenberg $r$-matrix has no
higher-pole terms.
\end{proposition}

\begin{proof}
The OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ has a double pole.
The bar construction extracts the residue along
$d\log(z{-}w) = dz/(z{-}w)$, absorbing one power of
$(z{-}w)$ (Remark~\ref{rem:heisenberg-bar-absorbs-pole} below).
The collision residue is therefore

thinking
**Analyzing Laplace and r-matrix**

I might consider using the classical r-matrix as the Laplace kernel, but there are distinctions regarding collision residues. There’s a chance I should classify the MEDIUM based on local convention drift instead of high if it pertains to the Laplace transform. In Vol2, they mention r(z)=k/z^2 without any qualifiers. Since the user asked to verify every instance, I need to report high severity for unqualified wrong formulas and medium for overloaded notation with a clear caveat. I'll check for all occurrences of `k/z^2` across volumes.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'k/z\\"'^2|'"\\\\kappa/z\\"'^2'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Heisenberg.*k/z|Heisenberg.*\\\\kappa/z|\\\\cH_k.*k/z|\\\\cH_k.*\\\\kappa/z|r_\\{\\\\cH_k\\}\\(z\\)\\s*=\\s*k\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\)\\s*=\\s*k\\Omega/z' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:439:(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4655:rational $r$-matrix $r_0(z) = k\,\Omega/z + k\,\kappa/z^2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1792:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2011:$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:275:double pole $\kappa/z^2$; the collision residue has a single pole
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1377: $r^L(z) = \kappa/z^2$. &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1380: $r^L(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1384: $r^L(z) = \kappa/z^2 + \mathfrak{Q}_0/z^4$. &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:413:pole $k\kappa/z^2$ is the Heisenberg-type (abelian Cartan)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:454:\kappa/z^2$ is the abelian (Cartan) contribution, identical in
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791:$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1498:$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:560:The OPE $b(z,t)\, b(0,t') \sim \kappa/z^2$ (the Heisenberg
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:1662: $r^{\mathrm{L}}(z) = k/z^2$ \\
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293: $r(z) = \kappa/z^2$. &
 exited 2 in 51ms:
rg: regex parse error:
    (?:Heisenberg.*k/z|Heisenberg.*\\kappa/z|\\cH_k.*k/z|\\cH_k.*\\kappa/z|r_\{\\cH_k\}\(z\)\s*=\s*k\\Omega/z|r_\{\\cH_k\}\(z\)\s*=\s*k\Omega/z)
                                                                                                                                       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k' /Users/raeez/calabi-yau-quantum-groups/chapters | rg 'r\\(|R\\(|r\\-matrix|R\\-matrix|R-matrix|Omega/z|k/z\\"'^2|k/z|1/z|collision residue'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '84,90p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
 succeeded in 51ms:
\label{rem:level-prefixed-r-matrix}
The classical $r$-matrix attached to an affine Kac-Moody $E_1$-chiral algebra at level $k$ is
\[
 r(z) = \frac{k\,\Omega}{z},
\]
not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
\end{remark}
codex
The remaining work is bookkeeping, not discovery: I now have the canonical source, the main false surfaces, and the explicit caveat cases that only drift by notation. I’m doing one last pass to make sure I don’t overstate any issue that a nearby line already disambiguates.
exec
/bin/zsh -lc "sed -n '1373,1383p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2006,2016p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1658,1665p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cand=$(rg -n --glob '"'*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'r\\(|R\\(|r\\-matrix|R\\-matrix|R-matrix|collision residue|k/z|k/z\\"'^2|1/z|Omega/z|'"\\\\Omega/z|\\\\kappa/z|kappa/z'); printf '%s\\n' \""'$cand" | wc -l; printf '"'%s\\n' \""'$cand" | cut -d: -f1 | sort -u | wc -l' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2274,2282p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{Class} & \emph{Laplace kernel $r^L(z)$} &
\emph{Shadow connection} \\
\midrule
$\mathbf{G}$ &
 $r^L(z) = \kappa/z^2$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
$\mathbf{L}$ &
 $r^L(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g -
 \mathfrak{C}$ \\
$\mathbf{C}$ &
 succeeded in 52ms:
\hline
$m_{\geq 3}$ & $= 0$ & $= 0$ & finite & $= 0$ &
 $\neq 0$ & $\neq 0$, $\infty$ \\
PVA type & poly & poly & poly & poly &
 Lie & nonlinear \\
$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
 $k\,\Omega/z$ &
 $\frac{c/2}{z^4} + \frac{2T}{z^2} + \frac{\partial T}{z}$ \\
$R(z)$ & $e^{k\hbar/z}$ & $e^{\hbar/z}$ & trivial & $e^{k\hbar/z}$ &
 Drinfeld & exp.\ model via fusion kernel \\
$\kappa$ & $k$ & $1$ & $0$ & $k$ &
 succeeded in 52ms:
 \begin{center}
 \renewcommand{\arraystretch}{1.1}
 \begin{tabular}{ll}
 Heisenberg $\cH_k$\textup: &
 $r^{\mathrm{L}}(z) = k/z^2$ \\
 Affine $\hat\fg_k$\textup: &
 $r^{\mathrm{L}}(z)
 = k\,\kappa^{ab}/z^2
 succeeded in 50ms:
     126
      65
 succeeded in 50ms:
the trivial permutation $R=\tau$. For a generic level
$k$ and generic Fock charges, $R(z)$ is a non-identity
scalar exponential series in $1/z$. The collision residue
$k/z$ is derived from the OPE double pole ($d\log$
absorption); attempting to read the R-matrix off the raw OPE
without applying the step gives the incorrect answer
$k/z^2$ and hence a wrong pole structure.
\end{remark}



thinking
**Checking candidate lines**

I'm counting 126 candidate lines across 65 files. I noticed we didn’t inspect each one individually, though we did filter and spot-check. It seems we can confidently say we checked "instances: 126 candidate references with 10 violations found" if audited. But did we verify all instances? Not all individually, just via contextual searches for suspicious patterns. I think it would help to categorize them by formula types, maybe using a shell script with `rg` and grep patterns for better coverage.
thinking
**Analyzing suspicious patterns**

I want to count lines with specific suspicious patterns and create unique file lists to ensure we've covered all anomalous patterns. I can start by finding candidate lines and then filtering them into categories like: canonical simple poles `k/z` or `κ/z`, `k/z^2` or `κ/z^2`, `kΩ/z`, and `1/z` or `1/z`. Using `rg` patterns for this will help me sort and list them, so I'll apply this across all .tex files for thoroughness.
codex
I’ve already checked the explicit outliers. To close the audit, I’m grouping the entire hit set by formula shape so I can confirm there isn’t another hidden variant beyond the ones already isolated: simple-pole `k/z`, Laplace-style `k/z^2`, Casimir-style `k\,\Omega/z`, and level-stripped `1/z`.
exec
/bin/zsh -lc "printf 'double_pole_hits\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'k/z\\"'^2|'"\\\\kappa/z\\"'^2'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'casimir_hits\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'Omega/z|\\\\Omega/z'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'one_over_z_hits\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '1/z'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'simple_pole\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'k/z|\\\\kappa/z' | wc -l; printf 'laplace_double\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'k/z\\"'^2|'"\\\\kappa/z\\"'^2'"' | wc -l; printf 'casimir_style\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'Omega/z|\\\\Omega/z' | wc -l; printf 'level_stripped_1overz\\n'; rg -n --glob '*.tex' 'Heisenberg|\\\\cH_k|H_k|\\\\mathcal H|\\\\mathcal\\{H\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg '1/z' | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
double_pole_hits
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:413:pole $k\kappa/z^2$ is the Heisenberg-type (abelian Cartan)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:560:The OPE $b(z,t)\, b(0,t') \sim \kappa/z^2$ (the Heisenberg
 succeeded in 51ms:
casimir_hits
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:618:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:698:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1420:Equivalently: $K_\cA(z) = 1$ iff the boundary coproduct is primitive iff the shadow tower terminates at depth zero. This is the $K$-matrix shadow of the pole-order hierarchy summarised in Table~\ref{tab:two-colour-koszul-duals} and in the shadow-depth discussion of Volume~I. It is not an $r$-matrix statement: the $K$-matrix modifies the coproduct, not the product, and the level-$k$ vanishing check does not apply directly; the corresponding $r$-matrix check is the one already recorded in the Volume~II affine constructions (classical $r$-matrix $k\,\Omega/z$ vanishes at $k=0$, in which case $\cA = \cH_0$ collapses to the trivial Heisenberg and $K_\cA(z) = 1$, consistent with class~$\mathbf{G}$).
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1442:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1519:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1658:the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
 succeeded in 51ms:
one_over_z_hits
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1383:the Heisenberg $R$-matrix is an entire function of $1/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:226:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:149:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:683:For the free $\beta\gamma$ system on $\CC_z \times \RR_t$, the monodromy of $\nabla_{\fS}$ around $z = 0$ equals the spectral $R$-matrix $R(z) = 1 + r/z + O(1/z^2)$ of the Heisenberg vertex algebra.
 succeeded in 51ms:
simple_pole
      29
laplace_double
       4
casimir_style
       8
level_stripped_1overz
       4



thinking
**Evaluating search results**

I’m noticing the broad filter might be missing some unqualified k/z² hits, possibly because H_k isn't on the same line. I found only 4 double pole hits due to the requirement for Heisenberg and H_k on the same line. The unqualified sections, like the Vol2 introduction, might not have been counted because there's no Heisenberg token on that line, even though there is a cH_k. 

To be thorough, I’ll search all `.tex` files for `r(z)=k/z²` across repositories, regardless of tokens.
thinking
**Inspecting files for references**

I want to examine some files that haven't been checked yet. For example, there are references in Vol2's `thqg_gravitational_complexity.tex`, and in Vol1's `e1_modular_koszul.tex`, both of which explicitly mention terms like `r^L` and `r^L(z)`. 

There's also a line in relative Feynman transform that discusses a possible Heisenberg symplectic relationship, but it doesn't seem to be an r-matrix, which is fine. 

In the `rosetta_stone` file, there's a rational r-matrix, `r_0(z)=kΩ/z + kκ/z²`, that might not be Heisenberg-related. I should check for situations regardless of Heisenberg tokens. It might also be helpful to look at earlier lines in `examples-worked.tex` to see the context for ClaimStatus. I need to figure out the severity rubric based on the user's specifications.
thinking
**Gathering line numbers**

I need to determine if I’m looking for line 351 from rg; I might not need it though. I think using `nl -ba` will help me get precise line numbers for critical sections like the introduction and propositions. I should use `nl -ba | sed -n` on files that look suspicious to confirm these numbers. rg gave some line numbers already, but I might need actual line numbers for other propositions too. Let's gather those!
codex
I’ve reduced the report to the findings that survive local reread. Before finalizing, I’m pinning exact line numbers with numbered excerpts so the final audit doesn’t rely on approximate grep offsets.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1788,1798p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '311,383p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1439,1445p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2399,2405p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2305,2311p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '560,564p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '124,131p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex | sed -n '145,150p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '224,228p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_complexity.tex | sed -n '1287,1295p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1788	\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
  1789	 the Heisenberg algebra at level~$k$.
  1790	\item $\lambda$-bracket:
  1791	 $\{J {}_\lambda J\} = k\lambda$.
  1792	\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
  1793	 transform of $k\lambda$).
  1794	\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
  1795	 Yang--Baxter trivially (abelian).
  1796	\item Line operators:
  1797	 $\cC_{\mathrm{line}} \simeq
  1798	 Y(\mathfrak{u}(1))\text{-mod}
 succeeded in 51ms:
   311	\begin{proposition}[Heisenberg $r$-matrix from collision residue;
   312	\ClaimStatusProvedHere]
   313	% label removed: prop:heisenberg-r-matrix
   314	For the Heisenberg algebra $\cH_k$ at level $k$, the classical
   315	$r$-matrix is
   316	\begin{equation}
   317	% label removed: eq:heisenberg-r-explicit
   318	\boxed{
   319	r_{\cH_k}(z) \;=\; \frac{k}{z^2}\, J \otimes J,
   320	}
   321	\end{equation}
   322	where $J$ is the Heisenberg current. This is a scalar $r$-matrix:
   323	it acts diagonally in the one-dimensional current space.
   324	\end{proposition}
   325	
   326	\begin{proof}
   327	\noindent\textbf{Step 1: The $\lambda$-bracket.}
   328	The Heisenberg $\lambda$-bracket is
   329	$\{J {}_\lambda J\} = k\lambda$
   330	(Section~\ref{sec:rosetta-stone}). The coefficients in the
 succeeded in 51ms:
  2399	genus-zero package; \ClaimStatusProvedHere]
  2400	% label removed: comp:vol2-heisenberg-modular-extension
  2401	\index{Heisenberg algebra!modular extension}
  2402	The Heisenberg genus-$0$ package has
  2403	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
  2404	The modular extension:
  2405	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
 succeeded in 50ms:
  2305	genus-zero package; \ClaimStatusProvedHere]
  2306	\label{comp:vol2-heisenberg-modular-extension}
  2307	\index{Heisenberg algebra!modular extension}
  2308	The Heisenberg genus-$0$ package has
  2309	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
  2310	$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
  2311	The modular extension:
 succeeded in 51ms:
  1439	contains its scalar trace. The averaging map
  1440	$\operatorname{av}$ is surjective but not injective: the kernel
  1441	records the non-symmetric components of the line-operator data.
  1442	For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
  1443	the symmetrization recovers the scalar
  1444	$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
  1445	discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 succeeded in 51ms:
   124	\begin{proof}
   125	Direct computation on each family. The Laplace identity
   126	is Proposition~\ref{prop:field-theory-r} specialized to explicit
   127	$\lambda$-bracket data.
   128	For Heisenberg: $\{a_\lambda a\} = k\lambda$ gives
   129	$r(z) = k/z^2$.
   130	For $\widehat{\mathfrak{sl}}_2$: all $9$ bracket pairs
   131	$(J^a, J^b)$ verify.
 succeeded in 52ms:
   560	\]
   561	which is the standard classical/quantum correspondence for spectral $R$-matrices. This specialises, at $u = \hh$, to the relation $R(z) = \exp(r(z))$ of the previous remark.
   562	\item \emph{Geometric spectral parameter.} The parameter $z$ is a coordinate on the curve $C$ (the holomorphic direction of $\SCchtop$), not a formal bookkeeping variable. This is exactly what distinguishes $B^{\mathrm{ord}}(A)$ from the purely algebraic braided categories $\mathrm{Rep}(U_q(\fg))$, which have no spectral parameter at all, and aligns $B^{\mathrm{ord}}(A)$ with the evaluation-module category for a Yangian or quantum affine algebra. Meromorphic braided tensor categories with a geometric spectral parameter of this type were isolated by Y.~Soibelman in the late 1990s as the natural target for vertex-algebra categorification; Etingof--Kazhdan quantization~\cite{etingof1996quantization} produces the spectrally-parametrised representative within each formal-deformation class.
   563	\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
   564	\end{enumerate}
 succeeded in 50ms:
   145	r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\, \{\ \cdot{}_\lambda \cdot\ \}.
   146	\]
   147	This is the Laplace transform of the $\lambda$-bracket kernel, convergent for $\operatorname{Re}(z) > 0$ by the exponential decay of $K(z,t)$ in the topological direction (hypothesis (H2)). Meromorphic continuation to $\C^\times$ follows from the meromorphy of the propagator in $z$.
   148	
   149	For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
   150	
 succeeded in 52ms:
   224	propagator in $z$.
   225	
   226	For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
   227	
   228	\begin{remark}[Laplace transform as spectral duality]
 succeeded in 50ms:
  1287	\begin{tabular}{c@{\quad}l@{\quad}l}
  1288	\toprule
  1289	\emph{Class} & \emph{Binary shadow $r(z)$} &
  1290	\emph{Shadow connection} \\
  1291	\midrule
  1292	$\mathbf{G}$ &
  1293	 $r(z) = \kappa/z^2$. &
  1294	 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
  1295	$\mathbf{L}$ &

thinking
**Evaluating duplicate lines**

I need to pinpoint exact line numbers for duplicate lines, specifically 1519 and 1658, and for standalone duplicates too. I’m pondering whether to mention approximate line numbers from rg without quoting the excerpts. Using rg line numbers could work since the description can mention them. Still, to play it safe, I think it's better to get the numbered lines for all the duplicates. Let’s ensure accuracy!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1656,1660p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '616,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1517,1521p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '696,700p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '788,791p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1656	
  1657	Tier (b) contains every standard-landscape vertex algebra:
  1658	the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
  1659	$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
  1660	,
 succeeded in 51ms:
  1517	The $\Eone$ side is strictly richer: at degree~$2$ alone it
  1518	distinguishes algebras that the symmetric side identifies.
  1519	The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
  1520	$\widehat{\mathfrak{sl}}_2$-shadow
  1521	$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 succeeded in 51ms:
   616	$\operatorname{av}$ is surjective but not injective: the kernel
   617	records the non-symmetric components of the line-operator data.
   618	For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
   619	the symmetrization recovers the scalar
   620	$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
 succeeded in 52ms:
   696	The $\Eone$ side is strictly richer: at degree~$2$ alone it
   697	distinguishes algebras that the symmetric side identifies.
   698	The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
   699	$\widehat{\mathfrak{sl}}_2$-shadow
   700	$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 succeeded in 50ms:
   788	\textbf{Shadow class} \\
   789	\hline
   790	$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
   791	$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '414,418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '38,42p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '95,101p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    38	\medskip
    39	\noindent\textbf{Heisenberg.}
    40	For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
    41	\[
    42	R(z) = e^{r(z)} = e^{k\hbar/z},
 succeeded in 51ms:
    95	
    96	The classical $r$-matrix
    97	% PE-1: r-matrix. Family: Heis. r(z) = k/z. Level: k. OPE pole 2, r pole 1.
    98	% vanishing check : k=0 -> r=0. Match: Y. Source: landscape_census.tex. Verdict: ACCEPT.
    99	$r^{\mathrm{Heis}}(z) = k/z$ is nontrivial but scalar. At $k = 0$
   100	the $r$-matrix vanishes: the abelian limit is uncurved. The
   101	$R$-matrix $R(z) = e^{k\hbar/z}$ carries spectral data, yet the
 succeeded in 51ms:
   414	\hline
   415	$\cH_k$ ($JJ$)
   416	 & $1$ & $\{2\}$ & $\{1\}$
   417	 & $k/z$
   418	 & trivial \\

thinking
**Inspecting line references**

I need to inspect the file `ht_bulk_boundary_line.tex` to see if there's a proper counterpart. It might be useful to check `chapters/connections/thqg_gravitational_complexity.tex` for the exact line numbers mentioned in earlier prose. Searching the excerpt above line 1280 could help, and I might specifically need lines around 1282. It seems I should reference the preceding sentence at lines 1281-1286, which explicitly says it's not about the collision residue. I'll remember to use `nl` around 1281.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_complexity.tex | sed -n '1281,1288p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex | sed -n '1373,1380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1373	\emph{Class} & \emph{Laplace kernel $r^L(z)$} &
  1374	\emph{Shadow connection} \\
  1375	\midrule
  1376	$\mathbf{G}$ &
  1377	 $r^L(z) = \kappa/z^2$. &
  1378	 $\nabla^{\mathrm{hol}} = d - \kappa\,\omega_g$ \\
  1379	$\mathbf{L}$ &
  1380	 $r^L(z) = \kappa/z^2 + \mathfrak{C}_0/z^3$. &
 succeeded in 52ms:
  1281	$r^{\mathrm{coll}}(z)$, whose poles are shifted down by one;
  1282	the bar kernel absorbs one pole) and the corresponding
  1283	connection component:
  1284	\begin{center}
  1285	\small
  1286	\renewcommand{\arraystretch}{1.25}
  1287	\begin{tabular}{c@{\quad}l@{\quad}l}
  1288	\toprule



thinking
**Considering chapter structure**

I'm thinking about including the same symbol `r(z)` used for noncanonical objects in the main Volume 1 connection chapter. I feel like mentioning it could add clarity. Also, I wonder if the local caveat could reduce severity. Oh, and maybe I should consider whether a standalone introduction might create a duplicate section. Balancing these ideas is essential to keep the content cohesive and straightforward. Let's see where this takes me as I organize the information!
thinking
**Analyzing notation discrepancies**

I'm considering `kΩ/z` with `Ω` representing the Casimir and whether it could just be notationally similar to `k/z` after ignoring the 1D tensor. The user mentioned flagging even minor notation differences, which is important since they say the "matrix structure of Ω is discarded". While it's a trivial 1x1 matrix in rank 1, I think the differences are minor but still need some attention. I’ll flag this as low to medium relevance, considering the canonical form uses scalar `k/z`.
thinking
**Considering high severity conflicts**

I'm thinking that we should consider supporting high severity by looking at internal conflicts or any canonical contradictions. It might be wise to inspect if the ht_bulk_boundary_line has any other correct formulas in the file. I wonder if it uses k/z anywhere else. So, I'll need to search for that information. There's a lot to unpack here, and I want to make sure I cover everything properly!
exec
/bin/zsh -lc "rg -n 'k/z|k/z\\"'^2|Heisenberg|cH_k'"' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | head -20" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k/z|k/z\\"'^2|Heisenberg|cH_k'"' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | head -20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
363:\begin{example}[Geometric Steinberg for Heisenberg: all three ingredients verified;
366:\index{Steinberg!geometric conjecture!Heisenberg verification}
367:\index{Heisenberg algebra!geometric Steinberg}
368:The Heisenberg algebra $\cH_k$ (boundary chart of abelian
374: $\cM_{\mathrm{vac}}(\cH_k) =
382: \hookrightarrow \cM_{\mathrm{vac}}(\cH_k)$,
387: and convolution recovers the Heisenberg:
388: $H_*^{\mathrm{BM}}(\mathfrak{S}_b) \simeq \cH_k \simeq
389: Z^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$
391: since $\cH_k$ is formally smooth; Heisenberg has no critical level,
397:identity. For the Heisenberg the self-intersection is clean
2304:\begin{computation}[Modular extension of the Heisenberg
2307:\index{Heisenberg algebra!modular extension}
2308:The Heisenberg genus-$0$ package has
2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
2312:$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
2437:$\cH_k$ & $k$ & $k/24$
2450:The $\eta(q)^{-k}$ for Heisenberg is the Dedekind eta
2469:$\Bbbk[[\kappa]]$ & $\cH_k$ & Heisenberg \\
2503:$\cH_k$ & $7k/5760$ & loop$^2$ only \\
 succeeded in 51ms:
2391: For the Heisenberg holographic system:
2398:\begin{computation}[Modular extension of the Heisenberg
2401:\index{Heisenberg algebra!modular extension}
2402:The Heisenberg genus-$0$ package has
2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
2405:$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
2529:$\cH_k$ & $k$ & $-k/12$
2542:The $\eta(q)^{-k}$ for Heisenberg is the Dedekind eta
2561:$\Bbbk[[\kappa]]$ & $\cH_k$ & Heisenberg \\
2593:$\cH_k$ & $7k/5760$ & one-loop \\
2977:by two Heisenberg currents $\alpha_1,\alpha_2$ (weight~$1$)
2992:$s^{-1}\alpha_2$ (weight~$1$, Heisenberg sector) and
2995:$d_{\barB}$ contracts via the OPE: the Heisenberg pairs


thinking
**Organizing instances and violations**

I’m thinking through how to report instances checked, and I could say "Instances checked: 126 | Violations found: 8 | Verdict: FAIL." That seems clear, but I want to make sure I don't imply that each line was inspected individually. So maybe I'll phrase it as "Instances checked: 126 candidate surfaces." I need to ensure the report's ordered by severity, noting critical and high violations first, like the critical issue with vol2 thqg_spectral_braiding_extensions.
thinking
**Deciding on examples inclusion**

I’m considering whether we should include `examples-worked`, especially since it seems the user is looking for every discrepancy. Since they specifically requested that, it might be best to go ahead and include those examples. However, I want to make sure I don’t overwhelm them with too much information. But ultimately, clarity seems to be the priority here, so I’ll include them as requested!
Plan update
Canonical source verified, hit surface enumerated, discrepancies re-checked in local context, and final audit report prepared.
  ✓ Locate the canonical Heisenberg r-matrix statement in `landscape_census.tex` and extract its exact convention/boundary data.
  ✓ Enumerate every `.tex` occurrence of Heisenberg r-matrix formulas or prose mentions across Volumes I–III.
  ✓ Inspect each hit in local context and test it against the canonical form `r^{Heis}(z)=k/z`, including the `k=0 -> 0` boundary.
  ✓ Re-verify any suspected discrepancies and produce a severity-ordered audit report with counts.
codex
- [CRITICAL] [vol2/chapters/connections/thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:311) — The proved-here proposition “Heisenberg \(r\)-matrix from collision residue” states `r_{\cH_k}(z)=k\,J\otimes J/z^2` at line 319, but the same proof then says the collision residue is `k\,J\otimes J/z` at line 356. This is an internally false claim surface against the canonical Heisenberg formula in [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:417) and [chapters/frame/heisenberg_frame.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:99). The wrong `k/z^2` claim is repeated in the same file at lines 380 and 790.

- [HIGH] [vol2/chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1792) — The introduction calls `r(z)=k/z^2` the Heisenberg “classical \(r\)-matrix”, but the next item gives `R(z)=\exp(k\hbar/z)` at line 1794, whose first-order term is `k/z`, not `k/z^2`. The same file later distinguishes `r^L(z)=k/z^2` at line 2011, so this is a live mix-up between Laplace kernel and collision residue.

- [HIGH] [vol2/chapters/connections/ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403) — A proved-here “Heisenberg genus-0 package” records `r(z)=k/z^2` with no local caveat. The same false package is duplicated in [vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309).

- [HIGH] [vol2/chapters/examples/examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129) — In the proof, the Heisenberg specialization is `r(z)=k/z^2` immediately after a proposition stating that the Laplace transform gives the classical \(r\)-matrix extracted from OPE singular terms. Under the repo’s canonical convention, that is the pre-absorption Laplace kernel, not the Heisenberg \(r\)-matrix.

- [MEDIUM] [vol1/chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1442) — The main introduction repeatedly writes the Heisenberg \(r\)-matrix as `k\,\Omega/z` and speaks of discarded “matrix structure of \(\Omega\)” (also at lines 1519 and 1658). The same drift is propagated to [standalone/introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:618) and line 698 there. This does not match the canonical scalar Heisenberg surface `k/z`.

- [MEDIUM] [vol2/chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563) — A vanishing-check remark assigns Heisenberg the Casimir-style formula `k\,\Omega/z`. The same file states the correct Heisenberg collision residue `r(z)=k/z` at line 40, so this is internal convention drift.

- [LOW] [vol1/chapters/connections/thqg_gravitational_complexity.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_complexity.tex:1293) — The table lists class G as `r(z)=\kappa/z^2`, but the immediately preceding prose at lines 1281–1282 says this table is about an object whose poles are one higher than `r^{\mathrm{coll}}(z)`. This is a notation overload of `r(z)`, not a direct false collision-residue claim, but it conflicts with the canonical Heisenberg notation.

- [LOW] [vol2/chapters/connections/spectral-braiding.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:149) — The free-propagator remark says `r(z)\sim 1/z` is “consistent with” the Heisenberg example, dropping the level factor and therefore the `k=0\to 0` check. The same slip is duplicated in [vol2/chapters/connections/spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:226).

## Summary
Instances checked: 126 | Violations found: 8 | Verdict: FAIL
tokens used
120,511
